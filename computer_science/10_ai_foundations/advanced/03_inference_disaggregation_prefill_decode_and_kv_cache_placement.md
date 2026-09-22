# Inference disaggregation, prefill/decode và placement của KV cache

Một hệ thống inference cho Transformer có thể bắt đầu rất đơn giản: nhận prompt, chạy model trên một accelerator, sinh token rồi trả kết quả. Khi workload lớn lên, cách nhìn này nhanh chóng mất tác dụng vì hai pha chính của autoregressive inference dùng tài nguyên theo cách rất khác nhau. **Prefill** xử lý nhiều token đầu vào cùng lúc và thường có mức song song cao; **decode** sinh từng token kế tiếp, lặp lại nhiều lần và thường bị chi phối mạnh bởi memory bandwidth, KV cache và scheduling latency.

Từ khác biệt đó xuất hiện một câu hỏi kiến trúc: có nên để cùng một worker thực hiện cả prefill lẫn decode, hay tách chúng thành các pool chuyên biệt rồi chuyển trạng thái giữa hai pha? Đây là bài toán **inference disaggregation**. Chapter này không gắn với một serving framework cụ thể. Mục tiêu là hiểu state ownership, resource asymmetry, queueing và failure semantics quyết định khi nào disaggregation giúp hệ thống và khi nào nó chỉ thêm network hop.

Mental model chính:

```text
request
→ admission
→ tokenize / input state
→ prefill
→ KV state được tạo
→ placement / transfer / registration
→ decode loop
→ token stream
→ completion / cancellation / cleanup
```

Invariant quan trọng nhất là **decode phải tiếp tục từ đúng model version và đúng KV state của request**, trong khi scheduler vẫn giữ được latency/capacity budget và reclaim state an toàn khi request kết thúc hoặc thất bại.

## 1. Prefill và decode không phải cùng một workload

Trong prefill, model xử lý toàn bộ prompt hoặc một chunk lớn của prompt. Matrix multiplication có kích thước lớn hơn, accelerator thường có cơ hội sử dụng compute units hiệu quả hơn. Với prompt dài, prefill có thể tiêu thụ lượng compute đáng kể và tạo KV cache cho từng layer.

Decode khác. Sau khi có state của prompt, hệ thống thường sinh một token, cập nhật KV cache, rồi lặp lại. Mỗi iteration có ít token mới nhưng phải đọc lượng state ngày càng lớn. Khi sequence dài, chi phí đọc KV cache và giữ working set trong accelerator memory có thể trở thành giới hạn thực tế.

Do đó cùng một metric `GPU utilization` có thể che hai bottleneck khác nhau. Prefill có thể compute-bound trong khi decode memory-bound. Một scheduler tối ưu batch lớn cho prefill có thể làm time-to-first-token tốt hơn về throughput nhưng gây queue delay cho request ngắn. Một scheduler tối ưu inter-token latency có thể để accelerator underutilized nếu batch decode quá nhỏ.

## 2. Ba latency cần phân biệt

Không nên nói chung là “inference latency”. Ít nhất phải tách:

```text
queue/admission delay
→ time to first token (TTFT)
→ inter-token latency / time per output token
→ total completion time
```

TTFT chịu ảnh hưởng mạnh của queue và prefill. Inter-token latency chịu ảnh hưởng mạnh của decode scheduling, memory bandwidth, batch composition và KV locality. Total completion time còn phụ thuộc số output token và cancellation.

Nếu chỉ tối ưu average completion latency, hệ thống có thể làm request ngắn chờ sau prompt rất dài. Nếu chỉ tối ưu TTFT, scheduler có thể preempt decode quá nhiều và làm token stream giật cục. Vì vậy policy phải bắt đầu từ service contract: workload interactive, batch, streaming hay mixed.

## 3. KV cache là state, không chỉ là optimization

KV cache thường được giới thiệu như cách tránh tính lại attention cho toàn bộ prefix. Ở mức hệ thống, nó quan trọng hơn: KV cache trở thành **per-request state có identity, lifetime và placement**.

Ta cần biết state này thuộc model version nào, sequence nào, layer nào, token range nào và nằm ở device/host/node nào. Decode worker nhận request nhưng không nhận đúng KV state thì không thể tiếp tục chỉ từ request id.

State path có thể hình dung như sau:

```text
model version + prompt tokens
→ prefill compute
→ KV blocks
→ block metadata / ownership
→ decode placement
→ append token state
→ reclaim
```

Nếu dùng paged/block-based KV management, allocator phải giữ mapping từ logical sequence position sang physical blocks. Fragmentation, eviction và compaction trở thành vấn đề memory management tương tự virtual memory hoặc buffer pool, dù semantics khác.

## 4. Tại sao disaggregate prefill và decode

Trong kiến trúc colocated, một worker có thể xử lý cả hai pha. Ưu điểm lớn nhất là locality: KV cache đã nằm trên device vừa chạy prefill nên decode có thể tiếp tục mà không transfer state qua network.

Nhược điểm là hai workload cạnh tranh cùng resource và scheduler. Một prefill lớn có thể chiếm compute đủ lâu để decode đang streaming bị jitter. Ngược lại, decode batch nhỏ liên tục có thể làm prefill khó đạt throughput tốt.

Disaggregation tách worker pool:

```text
prefill pool
→ state handoff
→ decode pool
```

Điều này cho phép scale hai pha độc lập, chọn hardware/policy khác nhau và giảm interference. Nhưng lợi ích chỉ tồn tại nếu cost của handoff nhỏ hơn lợi ích từ specialization và independent scaling.

## 5. Handoff của KV state là critical path mới

Khi prefill và decode ở khác device hoặc node, KV cache phải được chuyển hoặc làm accessible theo một mechanism nào đó. Transfer này có thể đi qua device interconnect, host memory, RDMA-capable network hoặc một state service tùy kiến trúc.

Không cần gắn vào transport cụ thể để thấy invariant:

```text
producer hoàn tất đúng prefix
→ state được publish
→ consumer thấy đủ metadata + bytes
→ consumer xác nhận ownership/lease
→ decode mới bắt đầu
```

Nếu metadata được publish trước khi data thực sự visible, decode có thể đọc state chưa hoàn tất. Nếu producer giải phóng buffer trước khi consumer sở hữu nó, ta có use-after-free ở quy mô distributed. Nếu retry tạo hai consumer cùng tin rằng mình sở hữu sequence, resource leak hoặc duplicate generation có thể xảy ra.

Đây là lý do inference disaggregation là bài toán distributed state transfer chứ không chỉ “thêm một RPC”.

## 6. Placement là bài toán locality + capacity + fairness

Decode scheduler không chỉ cần worker còn trống. Nó cần worker có đủ accelerator memory cho KV growth, phù hợp model version, có locality tốt với state hiện tại và không làm một tenant chiếm hết capacity.

Placement sai có thể tạo vòng lặp:

```text
worker gần đầy
→ request mới vẫn được đặt vào
→ KV growth vượt headroom
→ eviction / migration / OOM
→ retry hoặc reschedule
→ network + queue tăng
→ tail latency xấu hơn
```

Headroom vì vậy không phải memory lãng phí. Nó là phần capacity dành cho growth uncertainty, fragmentation, failover và burst.

## 7. Continuous batching và scheduler pressure

Decode có lợi khi nhiều sequence được batch cùng iteration. Nhưng sequence không có cùng độ dài hoặc cùng thời điểm hoàn tất. **Continuous batching** cho phép request rời/vào batch theo thời gian thay vì chờ một batch cố định hoàn tất.

Cơ chế này tăng utilization nhưng tạo scheduler state phức tạp hơn. Scheduler phải quyết định request nào được chạy ở iteration tiếp theo, budget token nào dành cho prefill, request nào bị preempt và KV block nào cần giữ.

Nếu admission chỉ nhìn request count mà bỏ qua expected token budget, một request có context rất dài có thể tiêu thụ memory tương đương nhiều request ngắn. Capacity model nên reasoning bằng work units phù hợp như input tokens, active KV bytes, output-token rate và device memory headroom, không chỉ QPS.

## 8. Prefix reuse và cache semantics

Nhiều request có thể chia sẻ prefix giống nhau: system prompt, document context hoặc conversation history. Prefix caching có thể tái sử dụng KV state, nhưng correctness phụ thuộc identity của prefix.

Cache key không thể chỉ là raw text nếu tokenizer, model weights, positional semantics hoặc inference configuration làm representation thay đổi. Một key đúng cần phản ánh đủ context để bảo đảm cached state tương đương với state sẽ được tính lại.

Stale prefix cache ở đây không giống stale HTTP cache. Nếu reuse state của model version khác, output semantics có thể sai mà không tạo exception rõ ràng. Versioning phải là một phần của cache identity.

## 9. Failure, retry và cancellation

Request inference có thể thất bại trong prefill, trong handoff hoặc giữa decode. Retry toàn request dễ hiểu nhưng tốn compute. Resume từ checkpoint/KV state tiết kiệm hơn nhưng cần biết state nào đã được commit đủ để tiếp tục.

Streaming còn tạo ambiguity: client có thể đã nhận một số token trước khi connection đứt. Server retry không thể giả định client chưa thấy output. Vì vậy “exactly once token delivery” không tự xuất hiện chỉ vì backend có request id.

Cancellation cũng là resource event. Khi client bỏ request, scheduler cần dừng future work và reclaim KV state. Nếu cancellation signal chậm hoặc bị mất, orphaned state có thể giữ accelerator memory và làm capacity suy giảm từ từ.

## 10. Pressure làm behavior đổi phase

Inference serving thường có phase transition rõ. Khi arrival rate thấp, queue gần như bằng không và latency chủ yếu là service time. Khi accelerator hoặc memory tiến gần saturation, queue tăng nhanh. Batch lớn hơn có thể cải thiện throughput nhưng tăng waiting time. KV pressure có thể kích hoạt eviction/migration, làm network tăng và kéo throughput xuống, tạo feedback loop.

Do đó autoscaling chỉ dựa trên utilization có thể phản ứng muộn. Evidence nên gồm queue age, admitted vs rejected work, active sequences, token throughput, TTFT, inter-token latency, KV bytes/fragmentation, transfer time, prefill/decode utilization riêng và cancellation/retry rate.

## 11. Lower layers thực sự quyết định behavior

Ở tầng dưới, behavior phụ thuộc memory hierarchy và interconnect. KV cache lớn có thể biến decode thành memory-bandwidth problem. Transfer giữa device có thể bị giới hạn bởi topology, PCIe/NVLink-class interconnect hoặc network. NUMA placement của host staging buffer có thể ảnh hưởng handoff. Thermal/power throttling có thể làm sustained accelerator throughput thấp hơn benchmark ngắn.

Vì vậy inference diagnosis cần nối sang [SIMD/GPU execution model](../../02_computer_architecture/advanced/06_simd_vector_isa_and_gpu_execution_model.md), [power/thermal/DVFS](../../02_computer_architecture/advanced/07_power_thermal_dvfs_and_sustained_performance.md), [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md), [capacity/admission](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md) và [fleet profiling](../../08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md).

## 12. Production evidence và debugging workflow

Khi TTFT tăng nhưng inter-token latency ổn, hypothesis đầu tiên nên tập trung queue/prefill/handoff. Khi TTFT ổn nhưng token stream chậm, xem decode batch, memory bandwidth, KV locality và scheduler. Khi chỉ một cohort chậm, phân tách theo model version, hardware class, region, worker pool và sequence-length distribution.

Trace nên biểu diễn ít nhất các phase:

```text
admission
→ queue
→ prefill
→ KV publish/transfer
→ decode admission
→ decode iterations
→ stream/write
→ cleanup
```

Metric aggregate không đủ nếu mất cohort. Average KV usage 60% có thể che một nhóm worker ở 98% và liên tục OOM. Average TTFT tốt có thể che prompt dài hoặc tenant cụ thể bị starvation.

## 13. Worked reasoning: tại sao tách pool lại chậm hơn

Giả sử hệ thống tách prefill và decode để giảm interference nhưng TTFT tăng sau rollout. Không nên kết luận ngay rằng disaggregation là sai. Ta phân rã:

```text
TTFT = admission wait + prefill service + handoff + decode-start wait + first decode step
```

Nếu prefill service giảm nhưng handoff tăng nhiều hơn, bottleneck nằm ở state transfer/locality. Nếu handoff nhỏ nhưng decode-start wait tăng, placement hoặc capacity ratio giữa hai pool có thể sai. Nếu chỉ prompt dài chậm, KV transfer volume có thể là biến chính. Nếu mọi cohort cùng chậm khi load cao, queueing và admission policy có thể mới là owner của symptom.

Cách reasoning này quan trọng hơn tên framework: tìm stage nào sở hữu latency, invariant nào stage đó giữ và lower layer nào quyết định service time.

## 14. Senior note: disaggregation là đổi boundary sở hữu state

Sai lầm phổ biến là xem disaggregation như một optimization deployment. Thực chất nó đổi boundary sở hữu state. Khi colocated, KV lifetime có thể được quản lý trong một process/device. Khi disaggregated, hệ thống cần protocol cho publication, identity, transfer, ownership, retry và cleanup.

Do đó decision phải so sánh:

```text
specialization + independent scaling + interference reduction

với

state-transfer cost + extra queue + failure surface + operational complexity
```

Không có câu trả lời đúng cho mọi workload. Prompt length distribution, output length, SLO, hardware topology, model size và traffic burstiness quyết định trade-off.

## 15. Mental model cuối

Inference serving hiện đại là một stateful queueing system chạy trên memory-constrained accelerators. Model weights là shared state; KV cache là request state; prefill và decode là hai service phases có resource profile khác nhau; scheduler là nơi biến capacity thành latency; network/interconnect trở thành một phần của critical path khi state bị tách khỏi compute.

Khi debug, đừng bắt đầu bằng câu hỏi “GPU có đủ mạnh không?”. Hãy hỏi: **work đang chờ ở phase nào, state đang nằm ở đâu, ai sở hữu nó, resource nào giới hạn progress, và evidence nào chứng minh hypothesis đó?**