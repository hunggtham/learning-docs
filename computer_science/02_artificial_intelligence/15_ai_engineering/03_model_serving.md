# Mô hình (model / 모델) Serving trong AI

> **Mạch đọc:** Đặt **mô hình (model / 모델) Serving trong AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Đường đi của Serving** sang **Stateless và Stateful Serving**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Phục vụ mô hình (model serving / 모델 서빙)** là lớp biến một mô hình đã được huấn luyện thành một khả năng mà ứng dụng (application / 애플리케이션) có thể gọi ổn định qua API, RPC, batch job hoặc embedded thời gian chạy (runtime / 런타임). huấn luyện (training / 학습) tạo ra parameter; serving chịu trách nhiệm nạp mô hình, nhận yêu cầu (request / 요청), chuẩn hóa đầu vào (input / 입력), chạy suy luận (inference / 추론), kiểm soát tài nguyên, trả đầu ra (output / 출력) và quan sát hành vi trong môi trường vận hành (production / 운영 환경).

Serving không chỉ là `model.predict()`. Một môi trường vận hành (production / 운영 환경) dịch vụ (service / 서비스) còn phải giải quyết tính đồng thời (concurrency / 동시성), hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도), queueing, autoscaling, mô hình (model / 모델) phiên bản (version / 버전), rollout, quay lui (rollback / 롤백), batching, accelerator utilization, bộ nhớ (memory / 메모리) pressure và khả năng quan sát (observability / 관측 가능성).

## Đường đi của Serving

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

Mỗi stage đều có thể trở thành bottleneck. Một GPU nhanh không giúp nhiều nếu tokenizer, retrieval, serialization hoặc mạng (network / 네트워크) chiếm phần lớn độ trễ (latency / 지연 시간).

## Stateless và Stateful Serving

Một ảnh (image / 이미지) classifier thường gần như stateless: các yêu cầu (request / 요청) độc lập và mô hình chỉ cần đầu vào (input / 입력) hiện tại. tác nhân (agent / 에이전트) hoặc conversational LLM hệ thống (system / 시스템) thường stateful hơn vì cần conversation trạng thái (state / 상태), công cụ (tool / 도구) kết quả (result / 결과), bộ nhớ (memory / 메모리) hoặc workflow progress.

Tuy nhiên nên giữ mô hình (model / 모델) máy chủ (server / 서버) càng stateless càng tốt nếu có thể. Persistent trạng thái (state / 상태) nên đặt trong cơ sở dữ liệu (database / 데이터베이스) hoặc trạng thái (state / 상태) store chuyên dụng để horizontal scaling, thử lại (retry / 재시도) và failover dễ hơn.

## Suy luận đồng bộ và bất đồng bộ

**Suy luận đồng bộ (synchronous inference)** phù hợp khi người dùng chờ phản hồi trực tiếp, ví dụ autocomplete hoặc chat. độ trễ (latency / 지연 시간) ngân sách (budget / 예산) là ràng buộc (constraint / 제약조건) chính.

**Suy luận bất đồng bộ (asynchronous inference)** phù hợp với tác vụ (task / 작업) dài như transcription video, document processing hoặc large batch embedding. máy khách (client / 클라이언트) nhận job ID, hệ thống xử lý qua hàng đợi (queue / 큐) rồi lưu kết quả.

## Vòng đời yêu cầu (request / 요청)

Một yêu cầu (request / 요청) môi trường vận hành (production / 운영 환경) nên có correlation ID để dấu vết (trace / 추적) xuyên các dịch vụ (service / 서비스). kiểm tra hợp lệ (validation / 검증) phải kiểm tra lược đồ (schema / 스키마), kích thước đầu vào (input / 입력), permission và quota trước khi chiếm compute đắt tiền.

Mô hình (model / 모델) máy chủ (server / 서버) cần hết thời gian chờ (timeout / 타임아웃) rõ ràng. Nếu upstream đã hủy yêu cầu (request / 요청) nhưng backend vẫn tiếp tục sinh hàng nghìn đơn vị từ (token / 토큰) thì tài nguyên bị lãng phí.

Vì vậy cancellation propagation đặc biệt quan trọng với generative serving.

## Nạp mô hình

Weights có thể rất lớn. Việc nạp từ đối tượng (object / 객체) lưu trữ (storage / 저장소) vào host RAM rồi GPU bộ nhớ (memory / 메모리) có thể mất đáng kể thời gian.

Các kỹ thuật thường dùng:

- warm replica;
- lazy loading;
- bộ nhớ (memory / 메모리) ánh xạ (mapping / 매핑);
- sharded loading;
- giữ mô hình (model / 모델) dùng thường xuyên resident trong bộ nhớ (memory / 메모리);
- routing theo mô hình (model / 모델) affinity.

Cold start là vấn đề lớn trong serverless suy luận (inference / 추론).

## CPU, GPU và Accelerator

CPU phù hợp với mô hình (model / 모델) nhỏ, cây (tree / 트리)/mô hình tuyến tính (linear model / 선형 모델) hoặc tải công việc (workload / 워크로드) có thông lượng (throughput / 처리량) thấp. GPU phù hợp dense ma trận (matrix / 행렬) computation và batch suy luận (inference / 추론). Việc chọn accelerator phụ thuộc mô hình (model / 모델) kiến trúc (architecture / 아키텍처), precision, batch kích thước (size / 크기) và độ trễ (latency / 지연 시간) mục tiêu (target / 대상).

Không nên mặc định GPU luôn rẻ hơn. Nếu utilization thấp, accelerator đắt tiền có thể tạo chi phí (cost / 비용)/yêu cầu (request / 요청) rất cao.

## Tính đồng thời (concurrency / 동시성) và Queueing

Nếu tốc độ yêu cầu (request / 요청) đến lớn hơn tốc độ xử lý, hàng đợi (queue / 큐) tăng và tail độ trễ (latency / 지연 시간) bùng nổ.

Little's Law cho trực giác:

\[
L=\lambda W
\]

`L` là số yêu cầu (request / 요청) trung bình trong hệ thống, `λ` là arrival thông lượng (throughput / 처리량) và `W` là thời gian trung bình trong hệ thống.

Khi utilization tiến sát 100%, queueing delay thường tăng mạnh. môi trường vận hành (production / 운영 환경) dịch vụ (service / 서비스) cần headroom thay vì cố chạy hardware luôn ở mức full tuyệt đối.

## Batching trong Serving

Batching gộp nhiều yêu cầu (request / 요청) để accelerator xử lý hiệu quả hơn. Static batching chờ batch cố định; động (dynamic / 동적) hoặc continuous batching gom yêu cầu (request / 요청) theo thời điểm và trạng thái thực thi (execution / 실행).

LLM generation đặc biệt khó vì yêu cầu (request / 요청) có prompt length và đầu ra (output / 출력) length khác nhau. Continuous batching cho phép đưa yêu cầu (request / 요청) mới vào khi chuỗi (sequence / 시퀀스) khác hoàn thành thay vì chờ cả batch đồng bộ hoàn toàn.

## Streaming

Generative AI thường stream đơn vị từ (token / 토큰) để giảm độ trễ (latency / 지연 시간) mà người dùng cảm nhận.

Các chỉ số (metric / 지표) quan trọng:

- **TTFT — thời gian (time / 시간) To First đơn vị từ (token / 토큰)**;
- **TPOT — thời gian (time / 시간) Per đầu ra (output / 출력) đơn vị từ (token / 토큰)**;
- total generation độ trễ (latency / 지연 시간).

Trải nghiệm người dùng có thể cải thiện mạnh dù tổng compute không đổi nếu first đơn vị từ (token / 토큰) xuất hiện sớm.

## Routing

Router có thể chọn:

```text
mô hình nhỏ → request dễ
mô hình lớn → request khó
mô hình chuyên biệt → request theo domain
cached answer → request lặp lại
```

Đây là **định tuyến mô hình (model routing)**. Routing đúng có thể giảm chi phí mà vẫn giữ chất lượng.

Nhưng router cũng là một thành phần cần evaluation; routing sai có thể tạo chất lượng (quality / 품질) regression khó thấy.

## Versioning và triển khai (deployment / 배포)

Không nên thay trực tiếp mô hình (model / 모델) môi trường vận hành (production / 운영 환경) nếu có thể. Các chiến lược thường dùng:

- shadow triển khai (deployment / 배포);
- canary bản phát hành (release / 릴리스);
- blue/green triển khai (deployment / 배포);
- A/B kiểm thử (test / 테스트).

Mô hình (model / 모델) phiên bản (version / 버전) phải đi cùng tokenizer, preprocessing, tính năng (feature / 기능) lược đồ (schema / 스키마) và cấu hình (configuration / 구성). Chỉ phiên bản (version / 버전) weight tệp (file / 파일) là chưa đủ.

## Xử lý thất bại (failure / 실패)

Serving tầng (layer / 계층) cần fallback rõ ràng:

```text
primary model fail
→ retry có giới hạn
→ fallback model / cached result / deterministic path
→ trả lỗi rõ cho user nếu vẫn thất bại
```

Thử lại (retry / 재시도) không được vô hạn và phải chú ý idempotency nếu yêu cầu (request / 요청) liên quan công cụ (tool / 도구) hoặc hành động (action / 동작) có side tác động (effect / 효과).

## Khả năng quan sát (observability / 관측 가능성)

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

Average độ trễ (latency / 지연 시간) dễ che mất tail độ trễ (latency / 지연 시간). Trải nghiệm thực tế thường bị chi phối nhiều bởi p95/p99.

## Ranh giới bảo mật

Mô hình (model / 모델) máy chủ (server / 서버) không nên tin đầu vào (input / 입력). Cần validate kích thước để tránh tài nguyên (resource / 자원) exhaustion, sanitize tệp (file / 파일)/parser đường dẫn (path / 경로), enforce auth/tenant ranh giới (boundary / 경계) và không để prompt văn bản (text / 텍스트) tự trở thành authorization quyết định (decision / 결정).

## Đặc thù LLM Serving

LLM suy luận (inference / 추론) có hai phase chính:

```text
Prefill → xử lý toàn bộ prompt
Decode  → sinh token autoregressively
```

Prefill thường thiên về compute; decode thường nhạy hơn với bộ nhớ (memory / 메모리) bandwidth và KV bộ nhớ đệm (cache / 캐시).

KV bộ nhớ đệm (cache / 캐시) lưu key/giá trị (value / 값) của đơn vị từ (token / 토큰) trước đó để tránh tính lại toàn bộ chuỗi (sequence / 시퀀스) ở mỗi decode step. Tuy nhiên long ngữ cảnh (context / 맥락) làm KV bộ nhớ đệm (cache / 캐시) lớn và giảm tính đồng thời (concurrency / 동시성).

## Serving không đồng nghĩa triển khai (deployment / 배포)

Triển khai (deployment / 배포) là đưa sản phẩm tạo ra (artifact / 산출물) và cấu hình (configuration / 구성) vào môi trường (environment / 환경). Serving là hành vi thời gian chạy (runtime / 런타임) khi nhận và xử lý suy luận (inference / 추론) yêu cầu (request / 요청). MLOps bao phủ rộng hơn: vòng đời (lifecycle / 생명주기), versioning, monitoring và quản trị (governance / 거버넌스).

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Serving = mô hình + runtime + tài nguyên + queue + API + observability + failure policy
```

Một mô hình (model / 모델) benchmark nhanh không bảo đảm dịch vụ (service / 서비스) nhanh. hiệu năng (performance / 성능) của hệ thống phụ thuộc toàn chuỗi xử lý (pipeline / 파이프라인).

## Những nhầm lẫn thường gặp

### “Có endpoint là đã production-ready”

Không. Endpoint chưa giải quyết scaling, rollout, hết thời gian chờ (timeout / 타임아웃), khả năng quan sát (observability / 관측 가능성) hay quay lui (rollback / 롤백).

### “GPU utilization càng gần 100% càng tốt”

Không. Utilization quá cao có thể khiến queueing và tail độ trễ (latency / 지연 시간) mất kiểm soát.

### “Streaming làm suy luận (inference / 추론) nhanh hơn”

Không nhất thiết. Streaming chủ yếu giảm perceived độ trễ (latency / 지연 시간); tổng compute có thể không đổi.

## Liên kết kiến thức

Xem [Inference Pipeline](./02_inference_pipeline.md), [Batch vs Online Inference](./04_batch_vs_online_inference.md), [Caching and Batching](./05_caching_and_batching.md) và [AI Compute & Infrastructure](../17_ai_compute_and_infrastructure/README.md).
