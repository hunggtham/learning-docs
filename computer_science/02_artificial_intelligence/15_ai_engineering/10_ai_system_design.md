# Thiết kế hệ thống AI: từ mô hình tới sản phẩm đáng tin cậy

> **Mạch đọc:** Đặt **Thiết kế hệ thống AI: từ mô hình tới sản phẩm đáng tin cậy** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Kiến thức tiên quyết** sang **Bắt đầu từ tác vụ (task / 작업) đặc tả hợp đồng (contract / 계약)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Thiết kế hệ thống AI (AI system design / AI 시스템 설계)** là quá trình tổ chức mô hình, dữ liệu, truy xuất, công cụ, trạng thái (state / 상태), lưu trữ (storage / 저장소), thời gian chạy (runtime / 런타임), quan sát hệ thống và chính sách (policy / 정책) thành một sản phẩm có thể vận hành lâu dài. Một kiến trúc tốt không cố nhét toàn bộ “trí thông minh” vào một mô hình (model / 모델) duy nhất; nó phân tách trách nhiệm để mỗi thành phần có đặc tả hợp đồng (contract / 계약) rõ, có thể kiểm thử và có thể thay thế độc lập.

## Kiến thức tiên quyết

Nên đọc trước [RAG](../09_retrieval_and_rag/README.md), [Agents](../10_agents_and_ai_systems/README.md), [Model Serving](./03_model_serving.md), [Latency/Throughput/Cost](./09_latency_throughput_and_cost.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md) và [Reliability Engineering](../18_evaluation_reliability_interpretability/07_reliability_engineering.md).

## Bắt đầu từ tác vụ (task / 작업) đặc tả hợp đồng (contract / 계약)

Trước khi chọn mô hình (model / 모델), cần định nghĩa:

```text
input là gì?
output contract là gì?
độ trễ mục tiêu là bao nhiêu?
quality target là gì?
error nào chấp nhận được?
error nào buộc phải fail closed?
privacy/security constraint nào phải giữ?
request volume và burst là bao nhiêu?
chi phí tối đa trên mỗi task là bao nhiêu?
```

Nếu đầu ra (output / 출력) phải là JSON đúng lược đồ (schema / 스키마), đó là hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약). Nếu câu trả lời phải trích dẫn nguồn, grounding là yêu cầu (requirement / 요구사항). Nếu hành động (action / 동작) tạo side tác động (effect / 효과), authorization, idempotency và xác minh (verification / 확인) là yêu cầu (requirement / 요구사항).

## Phân tách năng lực (capability / 역량) và điều khiển (control / 제어)

Một kiến trúc môi trường vận hành (production / 운영 환경) thường có:

```text
User / Upstream
      ↓
API / Gateway
      ↓
Orchestrator
  ├─ Retrieval
  ├─ Model
  ├─ Tools
  ├─ Policy / Security
  ├─ State / Memory
  └─ Verifier
      ↓
Response / Action
      ↓
Logs / Metrics / Evaluation
```

Mô hình (model / 모델) cung cấp năng lực (capability / 역량) xác suất. thời gian chạy (runtime / 런타임) sở hữu điều khiển (control / 제어) luồng (flow / 흐름), permission, hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도), ngân sách (budget / 예산), trạng thái (state / 상태) và kiểm tra (audit / 감사).

## Deterministic Shell, Probabilistic cốt lõi (core / 핵심)

Một mẫu (pattern / 패턴) bền vững:

```text
validation xác định
→ mô hình xác suất
→ verification / policy xác định
```

LLM có thể đề xuất truy vấn (query / 쿼리), SQL hoặc hành động (action / 동작), nhưng parser, lược đồ (schema / 스키마) checker, permission hệ thống (system / 시스템) và executor mới quyết định hành động (action / 동작) có được thực thi hay không.

Prompt không phải ranh giới bảo mật (security boundary / 보안 경계).

## RAG, Fine-Tuning và Tooling giải quyết bài toán khác nhau

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
RAG       → kiến thức ngoài model hoặc cần cập nhật
Fine-tune → điều chỉnh behavior, style hoặc task distribution
Tooling   → truy cập action, computation hoặc live system
```

Nếu yêu cầu (requirement / 요구사항) là “đọc dữ liệu cơ sở dữ liệu (database / 데이터베이스) hôm nay”, fine-tuning không phải lớp trừu tượng (abstraction / 추상화) phù hợp. Nếu yêu cầu (requirement / 요구사항) là đầu ra (output / 출력) style ổn định, RAG một mình cũng chưa đủ.

## Mô hình triển khai đồng bộ và bất đồng bộ

Không phải mọi tác vụ (task / 작업) nên nằm trong một yêu cầu (request / 요청)/phản hồi (response / 응답) đồng bộ.

```text
chat ngắn / classification
→ synchronous path

tài liệu lớn / video / agent dài
→ create task
→ queue
→ worker
→ persisted state
→ poll / event / callback
```

Tác vụ (task / 작업) dài cần durable trạng thái (state / 상태) và cancellation. Giữ một HTTP liên kết (connection / 연결) quá lâu làm thử lại (retry / 재시도), hết thời gian chờ (timeout / 타임아웃) và khôi phục (recovery / 복구) khó kiểm soát.

## Yêu cầu (request / 요청) Envelope

Một yêu cầu (request / 요청) môi trường vận hành (production / 운영 환경) nên mang siêu dữ liệu (metadata / 메타데이터) đủ để dấu vết (trace / 추적) và enforce chính sách (policy / 정책):

```text
request_id
user / tenant identity
task type
deadline
model/policy version
budget
idempotency key nếu có write
```

Nhờ đó hết thời gian chờ (timeout / 타임아웃), chi phí (cost / 비용), authorization và kiểm tra (audit / 감사) không phụ thuộc vào văn bản (text / 텍스트) prompt.

## Stateless và Stateful dịch vụ (service / 서비스)

Trạng thái (state / 상태) cần được biểu diễn tường minh:

- session/conversation trạng thái (state / 상태);
- workflow trạng thái (state / 상태);
- durable bộ nhớ (memory / 메모리);
- người dùng (user / 사용자) preference;
- giao dịch (transaction / 트랜잭션) trạng thái (state / 상태);
- approval trạng thái (state / 상태).

Không nên dựa vào việc mô hình (model / 모델) “nhớ” trong ngữ cảnh (context / 맥락) nếu workflow cần resume, thử lại (retry / 재시도) hoặc chạy trên worker khác.

## Side tác động (effect / 효과) và Idempotency

Công cụ (tool / 도구) tạo payment, email, thứ tự (order / 순서) hoặc deploy phải có giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론) hoặc idempotency key.

```text
plan
→ validate
→ authorize
→ execute với idempotency
→ verify outcome
→ persist state
```

Thử lại (retry / 재시도) yêu cầu (request / 요청) không được tạo side tác động (effect / 효과) mới ngoài ý muốn.

## Optimistic tính đồng thời (concurrency / 동시성) cho trạng thái (state / 상태) Mutable

Nếu tài nguyên (resource / 자원) có thể thay đổi song song:

```text
read version 10
→ model đề xuất update
→ commit chỉ khi vẫn là version 10
```

Nếu tài nguyên (resource / 자원) đã là phiên bản (version / 버전) 11, thời gian chạy (runtime / 런타임) trả xung đột (conflict / 충돌) để tác nhân (agent / 에이전트) đọc lại và replan. Điều này ngăn mutation dựa trên trạng thái (state / 상태) lỗi thời.

## Mô hình (model / 모델) Routing

Không phải yêu cầu (request / 요청) nào cũng cần mô hình (model / 모델) lớn nhất.

```text
classifier/router
→ task dễ: small model
→ task khó: large model
→ search: embedding + reranker
→ image: vision model
→ deterministic calculation: tool
```

Router có thể dựa trên tác vụ (task / 작업) kiểu (type / 타입), chất lượng (quality / 품질) yêu cầu (requirement / 요구사항), độ trễ (latency / 지연 시간) ngân sách (budget / 예산), đơn vị từ (token / 토큰) length hoặc rủi ro (risk / 위험) lớp (class / 클래스).

Sự đánh đổi (trade-off / 트레이드오프): routing tiết kiệm chi phí (cost / 비용) nhưng thêm một thất bại (failure / 실패) điểm (point / 지점). Router sai có thể làm tác vụ (task / 작업) khó bị đưa sang mô hình (model / 모델) không đủ khả năng.

## Cascade

Một cascade có thể dùng mô hình (model / 모델) rẻ trước:

```text
small model
→ nếu đủ confidence / verifier pass: kết thúc
→ nếu không: escalate sang model mạnh hơn
```

Cascade hiệu quả khi có criterion đáng tin để quyết định “đủ tốt”. Nếu criterion yếu, hệ thống có thể tiết kiệm tiền nhưng tăng silent thất bại (failure / 실패).

## Caching

Có nhiều lớp bộ nhớ đệm (cache / 캐시):

```text
exact request cache
retrieval cache
embedding cache
prefix / prompt cache
semantic cache
```

Bộ nhớ đệm (cache / 캐시) key phải bao gồm những phiên bản (version / 버전) ảnh hưởng ngữ nghĩa (semantics / 의미론): mô hình (model / 모델), prompt, tenant, chỉ mục (index / 인덱스), chính sách (policy / 정책) hoặc công cụ (tool / 도구) trạng thái (state / 상태) khi cần.

Ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시) có rủi ro trả kết quả cũ cho truy vấn (query / 쿼리) “gần giống nhưng khác ý”, vì vậy nên dùng cho lĩnh vực (domain / 도메인) ít thay đổi và có vô hiệu hóa (invalidation / 무효화) chiến lược (strategy / 전략) rõ.

## Backpressure và Admission điều khiển (control / 제어)

Khi GPU hoặc provider quá tải, hàng đợi (queue / 큐) dài vô hạn thường làm p99 độ trễ (latency / 지연 시간) tệ hơn và gây thử lại (retry / 재시도) storm.

Hệ thống cần:

```text
queue limit
priority
per-tenant concurrency
rate limit
load shedding
```

Mục tiêu là giữ hệ thống trong vùng vận hành ổn định thay vì cố nhận mọi yêu cầu (request / 요청).

## Deadline Propagation

Nếu end-to-end deadline là 2 giây, từng stage cần ngân sách (budget / 예산):

```text
retrieval 300 ms
model 1200 ms
verification 200 ms
network + margin 300 ms
```

Downstream lời gọi (call / 호출) phải nhận deadline còn lại. hết thời gian chờ (timeout / 타임아웃) 10 giây ở một phụ thuộc (dependency / 의존성) là vô nghĩa nếu người dùng (user / 사용자) chỉ chờ 2 giây.

## Fallback và Graceful Degradation

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
preferred model
→ fallback model
→ cached/verified result
→ deterministic/manual path
→ explicit failure
```

Fallback phải được evaluate và phiên bản (version / 버전) hóa. Silent fallback sang mô hình (model / 모델) yếu hơn có thể nguy hiểm cho high-risk quyết định (decision / 결정).

## Human-in-the-Loop

Human rà soát (review / 검토) phù hợp khi:

- hành động (action / 동작) không thể hoàn tác;
- bất định (uncertainty / 불확실성) cao;
- chính sách (policy / 정책) yêu cầu approval;
- impact lỗi lớn.

Approval điểm (point / 지점) phải nằm trước side tác động (effect / 효과). UI approval nên hiển thị structured parameters, không chỉ prose do mô hình (model / 모델) sinh.

## RAG kiến trúc (architecture / 아키텍처)

Một chuỗi xử lý (pipeline / 파이프라인) RAG môi trường vận hành (production / 운영 환경):

```text
User query
→ authentication / tenant filter
→ query transformation
→ sparse + dense retrieval
→ reranking
→ context packing
→ LLM generation
→ citation / grounding verifier
→ policy
→ response
```

Thất bại (failure / 실패) có thể đến từ parser, chỉ mục (index / 인덱스) stale, ACL filter, retrieval miss, ngữ cảnh (context / 맥락) truncation hoặc unsupported claim. Vì vậy cần thành phần (component / 컴포넌트) evaluation riêng, xem [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md).

## Tác nhân (agent / 에이전트) kiến trúc (architecture / 아키텍처)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
Goal
→ planner
→ candidate action
→ schema + permission + risk validation
→ execute
→ observe
→ verify
→ persist state
→ continue / stop
```

Tác nhân (agent / 에이전트) cần step ngân sách (budget / 예산), vòng lặp (loop / 루프) detection, durable trạng thái (state / 상태) và khôi phục (recovery / 복구). Không nên để mô hình (model / 모델) tự sở hữu stop chính sách (policy / 정책) hoặc permission.

## Evaluation kiến trúc (architecture / 아키텍처)

Evaluation nên tồn tại ở nhiều cấp:

```text
component eval  → retrieval / model / tool
trajectory eval → Agent steps
end-to-end eval → task success
online eval     → production behavior
```

Mỗi bản phát hành (release / 릴리스) phải truy được về mô hình (model / 모델), prompt, chỉ mục (index / 인덱스), công cụ (tool / 도구) lược đồ (schema / 스키마) và chính sách (policy / 정책) phiên bản (version / 버전).

## Khả năng quan sát (observability / 관측 가능성)

Một dấu vết (trace / 추적) tốt nên nối:

```text
request
→ retrieval span
→ model span
→ tool span
→ verifier span
→ persistence span
```

Theo dõi:

- p50/p95/p99 độ trễ (latency / 지연 시간);
- hàng đợi (queue / 큐) thời gian (time / 시간);
- đơn vị từ (token / 토큰) count;
- bộ nhớ đệm (cache / 캐시) hit;
- fallback tỷ lệ (rate / 비율);
- công cụ (tool / 도구) lỗi (error / 오류);
- verified success;
- chi phí (cost / 비용)/tác vụ (task / 작업).

Không log raw secret hoặc PII theo mặc định.

## Sức chứa (capacity / 용량) thiết kế (design / 설계)

Cần ước lượng:

```text
peak QPS
input/output token distribution
concurrency
model memory
KV-cache memory
batching efficiency
headroom khi failover
```

Average traffic không đủ để sizing môi trường vận hành (production / 운영 환경). Burst và failover thường quyết định sức chứa (capacity / 용량) thật.

## Chi phí (cost / 비용) mô hình (model / 모델)

Tổng chi phí (cost / 비용)/tác vụ (task / 작업) có thể xem gần đúng:

\[
C_{tác vụ (task / 작업)}=C_{mô hình (model / 모델)}+C_{retrieval}+C_{công cụ (tool / 도구)}+C_{infra}+C_{human}
\]

Mô hình (model / 모델) rẻ hơn trên mỗi đơn vị từ (token / 토큰) chưa chắc rẻ hơn trên mỗi tác vụ (task / 작업) nếu cần thử lại (retry / 재시도) nhiều hoặc tạo nhiều human escalation.

Mục tiêu nên là **chi phí (cost / 비용) per successful tác vụ (task / 작업)**, không phải chỉ chi phí (cost / 비용) per yêu cầu (request / 요청).

## Triển khai (deployment / 배포) chiến lược (strategy / 전략)

Thay đổi mô hình (model / 모델) hoặc ứng dụng (application / 애플리케이션) nên đi qua:

```text
offline eval
→ shadow
→ canary
→ monitor
→ expand traffic
→ rollback nếu gate fail
```

Quay lui (rollback / 롤백) phải khôi phục hành vi (behavior / 동작) bundle tương thích: mô hình (model / 모델) + prompt + retrieval cấu hình (config / 설정) + công cụ (tool / 도구) lược đồ (schema / 스키마) khi cần.

## Vòng phản hồi (feedback loop / 피드백 루프) của dữ liệu (data / 데이터)

Môi trường vận hành (production / 운영 환경) quyết định (decision / 결정) ảnh hưởng dữ liệu tương lai. Recommendation thay đổi nội dung người dùng (user / 사용자) nhìn thấy; fraud mô hình (model / 모델) thay đổi giao dịch (transaction / 트랜잭션) nào được rà soát (review / 검토).

Dữ liệu mới vì vậy không trung tính. Trước retraining cần hiểu selection độ lệch (bias / 편향) và chính sách (policy / 정책) phản hồi (feedback / 피드백).

## Bản dựng (build / 빌드) hay Buy

Hosted API giảm gánh nặng serving nhưng tăng phụ thuộc (dependency / 의존성) vào provider. Self-host tăng điều khiển (control / 제어) nhưng cần expertise về GPU, sức chứa (capacity / 용량), bảo mật (security / 보안), upgrades và sự cố (incident / 인시던트) phản hồi (response / 응답).

Nên quyết định theo:

```text
volume
privacy/compliance
latency
customization
operational capability
provider lock-in risk
```

## Thất bại (failure / 실패) Modes xuyên suốt hệ thống

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

```text
retrieval stale
prompt/config mismatch
model timeout
schema invalid
tool permission error
state conflict
cache poisoning / stale cache
queue saturation
fallback regression
cost runaway
```

Thiết kế tốt phải biết mỗi thất bại (failure / 실패) được phát hiện ở đâu, ai sở hữu khôi phục (recovery / 복구) và fallback nào hợp lệ.

## Ranh giới bảo mật (security boundary / 보안 경계)

AI hệ thống (system / 시스템) mở thêm attack surface: prompt injection, malicious document, công cụ (tool / 도구) abuse, exfiltration, poisoned corpus và supply-chain rủi ro (risk / 위험).

Bảo mật (security / 보안) phải nằm trong mã (code / 코드), permission, mạng (network / 네트워크) và chính sách (policy / 정책) tầng (layer / 계층). Xem [Secure AI System Design](../19_ai_safety_security_alignment/08_secure_ai_system_design.md).

## Mô hình tư duy

> **Sản phẩm AI = năng lực (capability / 역량) xác suất nằm bên trong một operational đặc tả hợp đồng (contract / 계약) có tính xác định.**

Mô hình (model / 모델) chỉ là một thành phần. môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질) đến từ cách toàn bộ đồ thị (graph / 그래프) giới hạn, quan sát, xác minh và phục hồi lỗi.

## Những nhầm lẫn thường gặp

### “Mô hình tốt hơn sẽ sửa kiến trúc (architecture / 아키텍처) tệ”

Không. Permission sai, retrieval cũ, trạng thái (state / 상태) lỗi hoặc thử lại (retry / 재시도) không idempotent vẫn gây thất bại (failure / 실패).

### “tác nhân (agent / 에이전트) khung phần mềm (framework / 프레임워크) tự giải quyết độ tin cậy (reliability / 신뢰성)”

Không. khung phần mềm (framework / 프레임워크) cung cấp lớp trừu tượng (abstraction / 추상화); trạng thái (state / 상태) durability, bảo mật (security / 보안), evaluation và khôi phục (recovery / 복구) vẫn là trách nhiệm hệ thống.

### “môi trường vận hành (production / 운영 환경) AI chỉ là deploy endpoint”

Không. môi trường vận hành (production / 운영 환경) còn có routing, trạng thái (state / 상태), vòng đời (lifecycle / 생명주기), monitoring, quay lui (rollback / 롤백), dữ liệu (data / 데이터) phản hồi (feedback / 피드백) và quản trị (governance / 거버넌스).

### “GPU utilization càng cao càng tốt”

Không. Nếu không còn headroom, burst nhỏ cũng có thể làm tail độ trễ (latency / 지연 시간) tăng mạnh.

## Liên kết kiến thức

Chapter này nối [RAG](../09_retrieval_and_rag/README.md), [Agents](../10_agents_and_ai_systems/README.md), [Data for AI](../14_data_for_ai/README.md), [Model Serving](./03_model_serving.md), [MLOps / LLMOps](../16_mlops_and_llmops/README.md), [Evaluation](../18_evaluation_reliability_interpretability/README.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md) và [Security](../19_ai_safety_security_alignment/README.md).
