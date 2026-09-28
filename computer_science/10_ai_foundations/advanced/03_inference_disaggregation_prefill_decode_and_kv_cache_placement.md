# Suy luận (inference / 추론) disaggregation, prefill/decode và placement của KV bộ nhớ đệm (cache / 캐시)

Một hệ thống suy luận (inference / 추론) cho Transformer có thể bắt đầu rất đơn giản: nhận prompt, chạy mô hình (model / 모델) trên một accelerator, sinh đơn vị từ (token / 토큰) rồi trả kết quả. Khi tải công việc (workload / 워크로드) lớn lên, cách nhìn này nhanh chóng mất tác dụng vì hai pha chính của autoregressive suy luận (inference / 추론) dùng tài nguyên theo cách rất khác nhau. **Prefill** xử lý nhiều đơn vị từ (token / 토큰) đầu vào cùng lúc và thường có mức song song cao; **decode** sinh từng đơn vị từ (token / 토큰) kế tiếp, lặp lại nhiều lần và thường bị chi phối mạnh bởi bộ nhớ (memory / 메모리) bandwidth, KV bộ nhớ đệm (cache / 캐시) và scheduling độ trễ (latency / 지연 시간).

Từ khác biệt đó xuất hiện một câu hỏi kiến trúc: có nên để cùng một worker thực hiện cả prefill lẫn decode, hay tách chúng thành các pool chuyên biệt rồi chuyển trạng thái giữa hai pha? Đây là bài toán **suy luận (inference / 추론) disaggregation**. Chapter này không gắn với một serving khung phần mềm (framework / 프레임워크) cụ thể. Mục tiêu là hiểu quyền sở hữu trạng thái (state ownership / 상태 소유권), tài nguyên (resource / 자원) asymmetry, queueing và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) quyết định khi nào disaggregation giúp hệ thống và khi nào nó chỉ thêm mạng (network / 네트워크) hop.

Mô hình tư duy (mental model / 사고 모델) chính:

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

Bất biến (invariant / 불변식) quan trọng nhất là **decode phải tiếp tục từ đúng mô hình (model / 모델) phiên bản (version / 버전) và đúng KV trạng thái (state / 상태) của yêu cầu (request / 요청)**, trong khi scheduler vẫn giữ được độ trễ (latency / 지연 시간)/sức chứa (capacity / 용량) ngân sách (budget / 예산) và reclaim trạng thái (state / 상태) an toàn khi yêu cầu (request / 요청) kết thúc hoặc thất bại.

## 1. Prefill và decode không phải cùng một tải công việc (workload / 워크로드)

Trong prefill, mô hình (model / 모델) xử lý toàn bộ prompt hoặc một chunk lớn của prompt. Phép nhân ma trận (matrix multiplication / 행렬 곱셈) có kích thước lớn hơn, accelerator thường có cơ hội sử dụng compute units hiệu quả hơn. Với prompt dài, prefill có thể tiêu thụ lượng compute đáng kể và tạo KV bộ nhớ đệm (cache / 캐시) cho từng tầng (layer / 계층).

Decode khác. Sau khi có trạng thái (state / 상태) của prompt, hệ thống thường sinh một đơn vị từ (token / 토큰), cập nhật KV bộ nhớ đệm (cache / 캐시), rồi lặp lại. Mỗi iteration có ít đơn vị từ (token / 토큰) mới nhưng phải đọc lượng trạng thái (state / 상태) ngày càng lớn. Khi chuỗi (sequence / 시퀀스) dài, chi phí đọc KV bộ nhớ đệm (cache / 캐시) và giữ working set trong accelerator bộ nhớ (memory / 메모리) có thể trở thành giới hạn thực tế.

Do đó cùng một chỉ số (metric / 지표) `GPU utilization` có thể che hai bottleneck khác nhau. Prefill có thể compute-bound trong khi decode memory-bound. Một scheduler tối ưu batch lớn cho prefill có thể làm time-to-first-token tốt hơn về thông lượng (throughput / 처리량) nhưng gây hàng đợi (queue / 큐) delay cho yêu cầu (request / 요청) ngắn. Một scheduler tối ưu inter-token độ trễ (latency / 지연 시간) có thể để accelerator underutilized nếu batch decode quá nhỏ.

## 2. Ba độ trễ (latency / 지연 시간) cần phân biệt

Không nên nói chung là “suy luận (inference / 추론) độ trễ (latency / 지연 시간)”. Ít nhất phải tách:

```text
queue/admission delay
→ time to first token (TTFT)
→ inter-token latency / time per output token
→ total completion time
```

TTFT chịu ảnh hưởng mạnh của hàng đợi (queue / 큐) và prefill. Inter-token độ trễ (latency / 지연 시간) chịu ảnh hưởng mạnh của decode scheduling, bộ nhớ (memory / 메모리) bandwidth, batch composition và KV locality. Total completion thời gian (time / 시간) còn phụ thuộc số đầu ra (output / 출력) đơn vị từ (token / 토큰) và cancellation.

Nếu chỉ tối ưu average completion độ trễ (latency / 지연 시간), hệ thống có thể làm yêu cầu (request / 요청) ngắn chờ sau prompt rất dài. Nếu chỉ tối ưu TTFT, scheduler có thể preempt decode quá nhiều và làm đơn vị từ (token / 토큰) stream giật cục. Vì vậy chính sách (policy / 정책) phải bắt đầu từ dịch vụ (service / 서비스) đặc tả hợp đồng (contract / 계약): tải công việc (workload / 워크로드) interactive, batch, streaming hay mixed.

## 3. KV bộ nhớ đệm (cache / 캐시) là trạng thái (state / 상태), không chỉ là tối ưu hóa (optimization / 최적화)

KV bộ nhớ đệm (cache / 캐시) thường được giới thiệu như cách tránh tính lại attention cho toàn bộ prefix. Ở mức hệ thống, nó quan trọng hơn: KV bộ nhớ đệm (cache / 캐시) trở thành **per-request trạng thái (state / 상태) có định danh (identity / 식별자), thời gian tồn tại (lifetime / 수명) và placement**.

Ta cần biết trạng thái (state / 상태) này thuộc mô hình (model / 모델) phiên bản (version / 버전) nào, chuỗi (sequence / 시퀀스) nào, tầng (layer / 계층) nào, đơn vị từ (token / 토큰) phạm vi (range / 범위) nào và nằm ở thiết bị (device / 장치)/host/nút (node / 노드) nào. Decode worker nhận yêu cầu (request / 요청) nhưng không nhận đúng KV trạng thái (state / 상태) thì không thể tiếp tục chỉ từ yêu cầu (request / 요청) id.

Trạng thái (state / 상태) đường dẫn (path / 경로) có thể hình dung như sau:

```text
model version + prompt tokens
→ prefill compute
→ KV blocks
→ block metadata / ownership
→ decode placement
→ append token state
→ reclaim
```

Nếu dùng paged/block-based KV management, allocator phải giữ ánh xạ (mapping / 매핑) từ logical chuỗi (sequence / 시퀀스) position sang vật lý (physical / 물리적) blocks. Fragmentation, eviction và compaction trở thành vấn đề bộ nhớ (memory / 메모리) management tương tự virtual bộ nhớ (memory / 메모리) hoặc buffer pool, dù ngữ nghĩa (semantics / 의미론) khác.

## 4. Tại sao disaggregate prefill và decode

Trong kiến trúc colocated, một worker có thể xử lý cả hai pha. Ưu điểm lớn nhất là locality: KV bộ nhớ đệm (cache / 캐시) đã nằm trên thiết bị (device / 장치) vừa chạy prefill nên decode có thể tiếp tục mà không transfer trạng thái (state / 상태) qua mạng (network / 네트워크).

Nhược điểm là hai tải công việc (workload / 워크로드) cạnh tranh cùng tài nguyên (resource / 자원) và scheduler. Một prefill lớn có thể chiếm compute đủ lâu để decode đang streaming bị jitter. Ngược lại, decode batch nhỏ liên tục có thể làm prefill khó đạt thông lượng (throughput / 처리량) tốt.

Disaggregation tách worker pool:

```text
prefill pool
→ state handoff
→ decode pool
```

Điều này cho phép quy mô (scale / 규모) hai pha độc lập, chọn hardware/chính sách (policy / 정책) khác nhau và giảm interference. Nhưng lợi ích chỉ tồn tại nếu chi phí (cost / 비용) của handoff nhỏ hơn lợi ích từ specialization và independent scaling.

## 5. Handoff của KV trạng thái (state / 상태) là đường găng (critical path / 임계 경로) mới

Khi prefill và decode ở khác thiết bị (device / 장치) hoặc nút (node / 노드), KV bộ nhớ đệm (cache / 캐시) phải được chuyển hoặc làm accessible theo một cơ chế (mechanism / 메커니즘) nào đó. Transfer này có thể đi qua thiết bị (device / 장치) interconnect, host bộ nhớ (memory / 메모리), RDMA-capable mạng (network / 네트워크) hoặc một trạng thái (state / 상태) dịch vụ (service / 서비스) tùy kiến trúc.

Không cần gắn vào vận chuyển (transport / 전송) cụ thể để thấy bất biến (invariant / 불변식):

```text
producer hoàn tất đúng prefix
→ state được publish
→ consumer thấy đủ metadata + bytes
→ consumer xác nhận ownership/lease
→ decode mới bắt đầu
```

Nếu siêu dữ liệu (metadata / 메타데이터) được publish trước khi dữ liệu (data / 데이터) thực sự visible, decode có thể đọc trạng thái (state / 상태) chưa hoàn tất. Nếu producer giải phóng buffer trước khi bên tiêu thụ (consumer / 소비자) sở hữu nó, ta có use-after-free ở quy mô phân tán (distributed / 분산). Nếu thử lại (retry / 재시도) tạo hai bên tiêu thụ (consumer / 소비자) cùng tin rằng mình sở hữu chuỗi (sequence / 시퀀스), tài nguyên (resource / 자원) leak hoặc duplicate generation có thể xảy ra.

Đây là lý do suy luận (inference / 추론) disaggregation là bài toán phân tán (distributed / 분산) trạng thái (state / 상태) transfer chứ không chỉ “thêm một RPC”.

## 6. Placement là bài toán locality + sức chứa (capacity / 용량) + fairness

Decode scheduler không chỉ cần worker còn trống. Nó cần worker có đủ accelerator bộ nhớ (memory / 메모리) cho KV growth, phù hợp mô hình (model / 모델) phiên bản (version / 버전), có locality tốt với trạng thái (state / 상태) hiện tại và không làm một tenant chiếm hết sức chứa (capacity / 용량).

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

Headroom vì vậy không phải bộ nhớ (memory / 메모리) lãng phí. Nó là phần sức chứa (capacity / 용량) dành cho growth bất định (uncertainty / 불확실성), fragmentation, failover và burst.

## 7. Continuous batching và scheduler pressure

Decode có lợi khi nhiều chuỗi (sequence / 시퀀스) được batch cùng iteration. Nhưng chuỗi (sequence / 시퀀스) không có cùng độ dài hoặc cùng thời điểm hoàn tất. **Continuous batching** cho phép yêu cầu (request / 요청) rời/vào batch theo thời gian thay vì chờ một batch cố định hoàn tất.

Cơ chế này tăng utilization nhưng tạo scheduler trạng thái (state / 상태) phức tạp hơn. Scheduler phải quyết định yêu cầu (request / 요청) nào được chạy ở iteration tiếp theo, ngân sách (budget / 예산) đơn vị từ (token / 토큰) nào dành cho prefill, yêu cầu (request / 요청) nào bị preempt và KV khối (block / 블록) nào cần giữ.

Nếu admission chỉ nhìn yêu cầu (request / 요청) count mà bỏ qua expected đơn vị từ (token / 토큰) ngân sách (budget / 예산), một yêu cầu (request / 요청) có ngữ cảnh (context / 맥락) rất dài có thể tiêu thụ bộ nhớ (memory / 메모리) tương đương nhiều yêu cầu (request / 요청) ngắn. Sức chứa (capacity / 용량) mô hình (model / 모델) nên lập luận (reasoning / 추론) bằng công việc (work / 작업) units phù hợp như đầu vào (input / 입력) tokens, active KV bytes, output-token tỷ lệ (rate / 비율) và thiết bị (device / 장치) bộ nhớ (memory / 메모리) headroom, không chỉ QPS.

## 8. Prefix reuse và bộ nhớ đệm (cache / 캐시) ngữ nghĩa (semantics / 의미론)

Nhiều yêu cầu (request / 요청) có thể chia sẻ prefix giống nhau: hệ thống (system / 시스템) prompt, document ngữ cảnh (context / 맥락) hoặc conversation lịch sử (history / 이력). Prefix caching có thể tái sử dụng KV trạng thái (state / 상태), nhưng tính đúng đắn (correctness / 정확성) phụ thuộc định danh (identity / 식별자) của prefix.

Bộ nhớ đệm (cache / 캐시) key không thể chỉ là raw văn bản (text / 텍스트) nếu tokenizer, mô hình (model / 모델) weights, positional ngữ nghĩa (semantics / 의미론) hoặc suy luận (inference / 추론) cấu hình (configuration / 구성) làm biểu diễn (representation / 표현) thay đổi. Một key đúng cần phản ánh đủ ngữ cảnh (context / 맥락) để bảo đảm cached trạng thái (state / 상태) tương đương với trạng thái (state / 상태) sẽ được tính lại.

Stale prefix bộ nhớ đệm (cache / 캐시) ở đây không giống stale HTTP bộ nhớ đệm (cache / 캐시). Nếu reuse trạng thái (state / 상태) của mô hình (model / 모델) phiên bản (version / 버전) khác, đầu ra (output / 출력) ngữ nghĩa (semantics / 의미론) có thể sai mà không tạo exception rõ ràng. Versioning phải là một phần của bộ nhớ đệm (cache / 캐시) định danh (identity / 식별자).

## 9. Thất bại (failure / 실패), thử lại (retry / 재시도) và cancellation

Yêu cầu (request / 요청) suy luận (inference / 추론) có thể thất bại trong prefill, trong handoff hoặc giữa decode. Thử lại (retry / 재시도) toàn yêu cầu (request / 요청) dễ hiểu nhưng tốn compute. Resume từ checkpoint/KV trạng thái (state / 상태) tiết kiệm hơn nhưng cần biết trạng thái (state / 상태) nào đã được lần ghi nhận (commit / 커밋) đủ để tiếp tục.

Streaming còn tạo ambiguity: máy khách (client / 클라이언트) có thể đã nhận một số đơn vị từ (token / 토큰) trước khi liên kết (connection / 연결) đứt. Máy chủ (server / 서버) thử lại (retry / 재시도) không thể giả định máy khách (client / 클라이언트) chưa thấy đầu ra (output / 출력). Vì vậy “exactly once đơn vị từ (token / 토큰) delivery” không tự xuất hiện chỉ vì backend có yêu cầu (request / 요청) id.

Cancellation cũng là tài nguyên (resource / 자원) sự kiện (event / 이벤트). Khi máy khách (client / 클라이언트) bỏ yêu cầu (request / 요청), scheduler cần dừng future công việc (work / 작업) và reclaim KV trạng thái (state / 상태). Nếu cancellation tín hiệu (signal / 신호) chậm hoặc bị mất, orphaned trạng thái (state / 상태) có thể giữ accelerator bộ nhớ (memory / 메모리) và làm sức chứa (capacity / 용량) suy giảm từ từ.

## 10. Pressure làm hành vi (behavior / 동작) đổi phase

Suy luận (inference / 추론) serving thường có phase chuyển tiếp (transition / 전이) rõ. Khi arrival tỷ lệ (rate / 비율) thấp, hàng đợi (queue / 큐) gần như bằng không và độ trễ (latency / 지연 시간) chủ yếu là dịch vụ (service / 서비스) thời gian (time / 시간). Khi accelerator hoặc bộ nhớ (memory / 메모리) tiến gần saturation, hàng đợi (queue / 큐) tăng nhanh. Batch lớn hơn có thể cải thiện thông lượng (throughput / 처리량) nhưng tăng waiting thời gian (time / 시간). KV pressure có thể kích hoạt eviction/di chuyển (migration / 마이그레이션), làm mạng (network / 네트워크) tăng và kéo thông lượng (throughput / 처리량) xuống, tạo vòng phản hồi (feedback loop / 피드백 루프).

Do đó autoscaling chỉ dựa trên utilization có thể phản ứng muộn. Bằng chứng (evidence / 증거) nên gồm hàng đợi (queue / 큐) age, admitted vs rejected công việc (work / 작업), active sequences, đơn vị từ (token / 토큰) thông lượng (throughput / 처리량), TTFT, inter-token độ trễ (latency / 지연 시간), KV bytes/fragmentation, transfer thời gian (time / 시간), prefill/decode utilization riêng và cancellation/thử lại (retry / 재시도) tỷ lệ (rate / 비율).

## 11. Lower layers thực sự quyết định hành vi (behavior / 동작)

Ở tầng dưới, hành vi (behavior / 동작) phụ thuộc bộ nhớ (memory / 메모리) hierarchy và interconnect. KV bộ nhớ đệm (cache / 캐시) lớn có thể biến decode thành memory-bandwidth bài toán (problem / 문제). Transfer giữa thiết bị (device / 장치) có thể bị giới hạn bởi topology, PCIe/NVLink-class interconnect hoặc mạng (network / 네트워크). NUMA placement của host staging buffer có thể ảnh hưởng handoff. Thermal/power throttling có thể làm sustained accelerator thông lượng (throughput / 처리량) thấp hơn benchmark ngắn.

Vì vậy suy luận (inference / 추론) diagnosis cần nối sang [SIMD/GPU execution model](../../02_computer_architecture/advanced/06_simd_vector_isa_and_gpu_execution_model.md), [power/thermal/DVFS](../../02_computer_architecture/advanced/07_power_thermal_dvfs_and_sustained_performance.md), [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md), [capacity/admission](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md) và [fleet profiling](../../08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md).

## 12. Bằng chứng vận hành (production evidence / 운영 증거) và debugging workflow

Khi TTFT tăng nhưng inter-token độ trễ (latency / 지연 시간) ổn, hypothesis đầu tiên nên tập trung hàng đợi (queue / 큐)/prefill/handoff. Khi TTFT ổn nhưng đơn vị từ (token / 토큰) stream chậm, xem decode batch, bộ nhớ (memory / 메모리) bandwidth, KV locality và scheduler. Khi chỉ một cohort chậm, phân tách theo mô hình (model / 모델) phiên bản (version / 버전), hardware lớp (class / 클래스), region, worker pool và sequence-length phân phối (distribution / 분포).

Dấu vết (trace / 추적) nên biểu diễn ít nhất các phase:

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

Chỉ số (metric / 지표) aggregate không đủ nếu mất cohort. Average KV usage 60% có thể che một nhóm worker ở 98% và liên tục OOM. Average TTFT tốt có thể che prompt dài hoặc tenant cụ thể bị starvation.

## 13. Worked lập luận (reasoning / 추론): tại sao tách pool lại chậm hơn

Giả sử hệ thống tách prefill và decode để giảm interference nhưng TTFT tăng sau rollout. Không nên kết luận ngay rằng disaggregation là sai. Ta phân rã:

```text
TTFT = admission wait + prefill service + handoff + decode-start wait + first decode step
```

Nếu prefill dịch vụ (service / 서비스) giảm nhưng handoff tăng nhiều hơn, bottleneck nằm ở trạng thái (state / 상태) transfer/locality. Nếu handoff nhỏ nhưng decode-start wait tăng, placement hoặc sức chứa (capacity / 용량) ratio giữa hai pool có thể sai. Nếu chỉ prompt dài chậm, KV transfer volume có thể là biến chính. Nếu mọi cohort cùng chậm khi tải (load / 로드) cao, queueing và admission chính sách (policy / 정책) có thể mới là đơn vị sở hữu (owner / 오너) của symptom.

Cách lập luận (reasoning / 추론) này quan trọng hơn tên khung phần mềm (framework / 프레임워크): tìm stage nào sở hữu độ trễ (latency / 지연 시간), bất biến (invariant / 불변식) nào stage đó giữ và lower tầng (layer / 계층) nào quyết định dịch vụ (service / 서비스) thời gian (time / 시간).

## 14. Cấp cao (senior / 시니어) ghi chú (note / 노트): disaggregation là đổi ranh giới (boundary / 경계) sở hữu trạng thái (state / 상태)

Sai lầm phổ biến là xem disaggregation như một tối ưu hóa (optimization / 최적화) triển khai (deployment / 배포). Thực chất nó đổi ranh giới (boundary / 경계) sở hữu trạng thái (state / 상태). Khi colocated, KV thời gian tồn tại (lifetime / 수명) có thể được quản lý trong một tiến trình (process / 프로세스)/thiết bị (device / 장치). Khi disaggregated, hệ thống cần giao thức (protocol / 프로토콜) cho publication, định danh (identity / 식별자), transfer, quyền sở hữu (ownership / 소유권), thử lại (retry / 재시도) và cleanup.

Do đó quyết định (decision / 결정) phải so sánh:

```text
specialization + independent scaling + interference reduction

với

state-transfer cost + extra queue + failure surface + operational complexity
```

Không có câu trả lời đúng cho mọi tải công việc (workload / 워크로드). Prompt length phân phối (distribution / 분포), đầu ra (output / 출력) length, SLO, hardware topology, mô hình (model / 모델) kích thước (size / 크기) và traffic burstiness quyết định sự đánh đổi (trade-off / 트레이드오프).

## 15. Mô hình tư duy (mental model / 사고 모델) cuối

Suy luận (inference / 추론) serving hiện đại là một stateful queueing hệ thống (system / 시스템) chạy trên memory-constrained accelerators. Mô hình (model / 모델) weights là trạng thái dùng chung (shared state / 공유 상태); KV bộ nhớ đệm (cache / 캐시) là yêu cầu (request / 요청) trạng thái (state / 상태); prefill và decode là hai dịch vụ (service / 서비스) phases có tài nguyên (resource / 자원) profile khác nhau; scheduler là nơi biến sức chứa (capacity / 용량) thành độ trễ (latency / 지연 시간); mạng (network / 네트워크)/interconnect trở thành một phần của đường găng (critical path / 임계 경로) khi trạng thái (state / 상태) bị tách khỏi compute.

Khi gỡ lỗi (debug / 디버그), đừng bắt đầu bằng câu hỏi “GPU có đủ mạnh không?”. Hãy hỏi: **công việc (work / 작업) đang chờ ở phase nào, trạng thái (state / 상태) đang nằm ở đâu, ai sở hữu nó, tài nguyên (resource / 자원) nào giới hạn progress, và bằng chứng (evidence / 증거) nào chứng minh hypothesis đó?**