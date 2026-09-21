# Model Serving trong AI

**Phục vụ mô hình (model serving / 모델 서빙)** là lớp biến một mô hình đã được huấn luyện thành một khả năng mà application có thể gọi ổn định qua API, RPC, batch job hoặc embedded runtime. Training tạo ra parameter; serving chịu trách nhiệm nạp mô hình, nhận request, chuẩn hóa input, chạy inference, kiểm soát tài nguyên, trả output và quan sát hành vi trong production.

Serving không chỉ là `model.predict()`. Một production service còn phải giải quyết concurrency, timeout, retry, queueing, autoscaling, model version, rollout, rollback, batching, accelerator utilization, memory pressure và observability.

## Đường đi của Serving

```text
Client
  ↓
Gateway / API
  ↓
Validation + Auth
  ↓
Preprocessing / Context Assembly
  ↓
Inference Runtime
  ↓
Postprocessing / Safety / Verification
  ↓
Response
  ↓
Logs + Metrics + Traces
```

Mỗi stage đều có thể trở thành bottleneck. Một GPU nhanh không giúp nhiều nếu tokenizer, retrieval, serialization hoặc network chiếm phần lớn latency.

## Stateless và Stateful Serving

Một image classifier thường gần như stateless: các request độc lập và mô hình chỉ cần input hiện tại. Agent hoặc conversational LLM system thường stateful hơn vì cần conversation state, tool result, memory hoặc workflow progress.

Tuy nhiên nên giữ model server càng stateless càng tốt nếu có thể. Persistent state nên đặt trong database hoặc state store chuyên dụng để horizontal scaling, retry và failover dễ hơn.

## Suy luận đồng bộ và bất đồng bộ

**Suy luận đồng bộ (synchronous inference)** phù hợp khi người dùng chờ phản hồi trực tiếp, ví dụ autocomplete hoặc chat. Latency budget là constraint chính.

**Suy luận bất đồng bộ (asynchronous inference)** phù hợp với task dài như transcription video, document processing hoặc large batch embedding. Client nhận job ID, hệ thống xử lý qua queue rồi lưu kết quả.

## Vòng đời Request

Một request production nên có correlation ID để trace xuyên các service. Validation phải kiểm tra schema, kích thước input, permission và quota trước khi chiếm compute đắt tiền.

Model server cần timeout rõ ràng. Nếu upstream đã hủy request nhưng backend vẫn tiếp tục sinh hàng nghìn token thì tài nguyên bị lãng phí.

Vì vậy cancellation propagation đặc biệt quan trọng với generative serving.

## Nạp mô hình

Weights có thể rất lớn. Việc nạp từ object storage vào host RAM rồi GPU memory có thể mất đáng kể thời gian.

Các kỹ thuật thường dùng:

- warm replica;
- lazy loading;
- memory mapping;
- sharded loading;
- giữ model dùng thường xuyên resident trong memory;
- routing theo model affinity.

Cold start là vấn đề lớn trong serverless inference.

## CPU, GPU và Accelerator

CPU phù hợp với model nhỏ, tree/linear model hoặc workload có throughput thấp. GPU phù hợp dense matrix computation và batch inference. Việc chọn accelerator phụ thuộc model architecture, precision, batch size và latency target.

Không nên mặc định GPU luôn rẻ hơn. Nếu utilization thấp, accelerator đắt tiền có thể tạo cost/request rất cao.

## Concurrency và Queueing

Nếu tốc độ request đến lớn hơn tốc độ xử lý, queue tăng và tail latency bùng nổ.

Little's Law cho trực giác:

\[
L=\lambda W
\]

`L` là số request trung bình trong hệ thống, `λ` là arrival throughput và `W` là thời gian trung bình trong hệ thống.

Khi utilization tiến sát 100%, queueing delay thường tăng mạnh. Production service cần headroom thay vì cố chạy hardware luôn ở mức full tuyệt đối.

## Batching trong Serving

Batching gộp nhiều request để accelerator xử lý hiệu quả hơn. Static batching chờ batch cố định; dynamic hoặc continuous batching gom request theo thời điểm và trạng thái execution.

LLM generation đặc biệt khó vì request có prompt length và output length khác nhau. Continuous batching cho phép đưa request mới vào khi sequence khác hoàn thành thay vì chờ cả batch đồng bộ hoàn toàn.

## Streaming

Generative AI thường stream token để giảm latency mà người dùng cảm nhận.

Các metric quan trọng:

- **TTFT — Time To First Token**;
- **TPOT — Time Per Output Token**;
- total generation latency.

Trải nghiệm người dùng có thể cải thiện mạnh dù tổng compute không đổi nếu first token xuất hiện sớm.

## Routing

Router có thể chọn:

```text
mô hình nhỏ → request dễ
mô hình lớn → request khó
mô hình chuyên biệt → request theo domain
cached answer → request lặp lại
```

Đây là **định tuyến mô hình (model routing)**. Routing đúng có thể giảm chi phí mà vẫn giữ chất lượng.

Nhưng router cũng là một thành phần cần evaluation; routing sai có thể tạo quality regression khó thấy.

## Versioning và Deployment

Không nên thay trực tiếp model production nếu có thể. Các chiến lược thường dùng:

- shadow deployment;
- canary release;
- blue/green deployment;
- A/B test.

Model version phải đi cùng tokenizer, preprocessing, feature schema và configuration. Chỉ version weight file là chưa đủ.

## Xử lý Failure

Serving layer cần fallback rõ ràng:

```text
primary model fail
→ retry có giới hạn
→ fallback model / cached result / deterministic path
→ trả lỗi rõ cho user nếu vẫn thất bại
```

Retry không được vô hạn và phải chú ý idempotency nếu request liên quan tool hoặc action có side effect.

## Observability

Ít nhất nên theo dõi:

```text
request rate
error rate
latency p50 / p95 / p99
queue time
GPU / CPU utilization
memory
batch size
TTFT / token rate
model/version distribution
quality proxy nếu có
```

Average latency dễ che mất tail latency. Trải nghiệm thực tế thường bị chi phối nhiều bởi p95/p99.

## Ranh giới bảo mật

Model server không nên tin input. Cần validate kích thước để tránh resource exhaustion, sanitize file/parser path, enforce auth/tenant boundary và không để prompt text tự trở thành authorization decision.

## Đặc thù LLM Serving

LLM inference có hai phase chính:

```text
Prefill → xử lý toàn bộ prompt
Decode  → sinh token autoregressively
```

Prefill thường thiên về compute; decode thường nhạy hơn với memory bandwidth và KV cache.

KV cache lưu key/value của token trước đó để tránh tính lại toàn bộ sequence ở mỗi decode step. Tuy nhiên long context làm KV cache lớn và giảm concurrency.

## Serving không đồng nghĩa Deployment

Deployment là đưa artifact và configuration vào environment. Serving là hành vi runtime khi nhận và xử lý inference request. MLOps bao phủ rộng hơn: lifecycle, versioning, monitoring và governance.

## Mô hình tư duy

```text
Serving = mô hình + runtime + tài nguyên + queue + API + observability + failure policy
```

Một model benchmark nhanh không bảo đảm service nhanh. Performance của hệ thống phụ thuộc toàn pipeline.

## Những nhầm lẫn thường gặp

### “Có endpoint là đã production-ready”

Không. Endpoint chưa giải quyết scaling, rollout, timeout, observability hay rollback.

### “GPU utilization càng gần 100% càng tốt”

Không. Utilization quá cao có thể khiến queueing và tail latency mất kiểm soát.

### “Streaming làm inference nhanh hơn”

Không nhất thiết. Streaming chủ yếu giảm perceived latency; tổng compute có thể không đổi.

## Liên kết kiến thức

Xem [Inference Pipeline](./02_inference_pipeline.md), [Batch vs Online Inference](./04_batch_vs_online_inference.md), [Caching and Batching](./05_caching_and_batching.md) và [AI Compute & Infrastructure](../17_ai_compute_and_infrastructure/README.md).