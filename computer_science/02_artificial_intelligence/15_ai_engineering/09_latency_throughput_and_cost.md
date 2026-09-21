# Latency, Throughput và Cost trong hệ thống AI

Production AI không chỉ hỏi “mô hình có chính xác không?” mà còn phải hỏi **mất bao lâu, phục vụ được bao nhiêu request và tốn bao nhiêu tiền**. Ba đại lượng `latency`, `throughput` và `cost` liên hệ chặt chẽ nhưng không cùng hướng tối ưu.

## Latency

Latency là thời gian từ request tới response. Với Generative AI cần tách:

```text
queue time
preprocessing / context assembly
prefill
TTFT (time to first token)
decode time
postprocessing / tool verification
network overhead
```

Total latency có thể cao dù riêng model inference rất nhanh.

## Tail Latency

Average latency không đủ. Production thường theo dõi `p50`, `p95`, `p99`.

Nếu p99 bằng 8 giây, một nhóm người dùng vẫn có trải nghiệm rất kém dù average chỉ 1 giây.

Tail latency thường đến từ queueing, straggler, cold start, prompt dài, tool chậm hoặc noisy neighbor.

## Throughput

Thông lượng (throughput) là lượng công việc hoàn thành trong một đơn vị thời gian:

\[
Throughput=\frac{Completed\ Work}{Time}
\]

Với LLM có thể đo bằng requests/s hoặc tokens/s.

Batching thường giúp tăng throughput nhưng có thể tăng queue latency.

## Capacity và Utilization

Nếu utilization quá thấp, tài nguyên bị lãng phí. Nếu utilization quá cao, queueing tăng mạnh.

Capacity planning cần chừa headroom cho burst và failure.

Autoscaling cũng cần đúng signal. CPU utilization không phải lúc nào cũng phản ánh bottleneck ở GPU hoặc KV cache.

## Chi phí trên mỗi Request

Xấp xỉ:

\[
Cost/request\approx\frac{Infrastructure\ cost\ per\ time}{requests\ per\ time}
\]

Nhưng generative workload biến động mạnh theo token count, vì vậy cost/token hoặc cost/task đôi khi có ý nghĩa hơn cost/request.

## Economics của Input và Output Token

Prompt dài làm prefill compute và KV memory tăng. Output dài làm số bước decode tăng.

Hai request đều được tính là “một chat message” nhưng cost có thể khác nhau hàng chục lần.

## Chi phí của Chất lượng

Mô hình lớn hơn có thể tăng chất lượng nhưng đắt hơn. Production system thường dùng:

```text
small/default model
→ confidence/router
→ escalate sang expensive model khi cần
```

Model routing biến trade-off giữa quality và cost thành một policy động.

## Latency Budget

SLO end-to-end nên chia budget theo stage:

```text
API gateway        50 ms
retrieval         150 ms
reranking         100 ms
model TTFT        500 ms
tool call         700 ms
postprocess       100 ms
```

Nếu không có budget cho từng stage, đội ngũ dễ tối ưu nhầm chỗ.

## Little's Law và Queueing

\[
L=\lambda W
\]

Khi arrival rate tiến gần service capacity, `W` tăng mạnh. Vì vậy “GPU luôn chạy 100%” có thể làm user latency tệ hơn đáng kể.

## Trade-Off của Batching

Batch lớn hơn thường có:

```text
+ accelerator utilization
+ throughput
- memory headroom
- latency có thể tăng
```

Online scheduler cần tìm operating point phù hợp với SLO.

## Memory-Bound và Compute-Bound

Một kernel có thể bị giới hạn bởi **compute** hoặc **memory bandwidth**.

Quantization hữu ích nhất khi memory bandwidth là bottleneck. Nếu compute kernel chiếm ưu thế, compression có thể mang lợi ích khác.

Tư duy kiểu roofline giúp tránh tối ưu mù.

## Chi phí của RAG

RAG không chỉ tốn cost cho embedding search. Pipeline còn có:

```text
query rewrite
retrieval
reranking
context tokens
LLM generation
```

Retrieve nhiều chunk có thể tăng recall nhưng đồng thời làm context cost và latency tăng.

## Chi phí của Agent

Agent có số bước biến động. Một task tưởng như đơn giản có thể loop qua nhiều model/tool call.

Nên có:

- step budget;
- token budget;
- tool cost budget;
- timeout;
- loop detection.

Nếu không có budget, phân phối cost có thể có heavy tail rất lớn.

## Economics của Caching

Cache hit tránh expensive compute nhưng cần storage và invalidation. Giá trị của cache phụ thuộc tần suất tái sử dụng và mức freshness mà hệ thống chấp nhận.

## Cost Offline và Online

Batch processing thường tận dụng hardware tốt hơn. Nếu kết quả có thể tái sử dụng, precompute giúp chuyển chi phí ra khỏi hot path.

## Cost Attribution

Nền tảng multi-tenant nên quy chi phí theo tenant, feature, model và workflow. Nếu chỉ nhìn tổng GPU bill, rất khó biết feature nào thực sự tạo giá trị.

## Thứ tự tối ưu hợp lý

Trước khi tune kernel thấp tầng:

```text
1. profile end-to-end
2. bỏ các call không cần thiết
3. giảm data/token movement
4. cache / reuse
5. batching
6. chọn mô hình nhỏ hoặc chuyên biệt hơn
7. quantize / compress
8. tối ưu kernel thấp tầng
```

Optimization ở cấp architecture thường tạo gain lớn hơn micro-optimization.

## Mô hình tư duy

```text
Latency    = thời gian người dùng trải nghiệm cho một task
Throughput = lượng công việc hoàn thành trong một đơn vị thời gian
Cost       = tài nguyên tiêu thụ cho một outcome hữu ích
```

Mục tiêu cuối không phải tối thiểu từng metric riêng lẻ mà là đạt **chất lượng và độ tin cậy yêu cầu trong giới hạn ngân sách**.

## Những nhầm lẫn thường gặp

### “Tokens/second cao nghĩa là user experience tốt”

Không. TTFT hoặc queue time vẫn có thể rất tệ.

### “Mô hình nhỏ hơn luôn rẻ hơn”

Không. Nếu chất lượng thấp làm retry hoặc escalation tăng, end-to-end cost có thể cao hơn.

### “Chỉ cần tối ưu model inference là đủ”

Không. Retrieval, tool, parsing và network có thể mới là bottleneck chính.

## Liên kết kiến thức

Xem [Caching and Batching](./05_caching_and_batching.md), [Model Compression](./08_model_compression.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md) và [AI Compute](../17_ai_compute_and_infrastructure/README.md).