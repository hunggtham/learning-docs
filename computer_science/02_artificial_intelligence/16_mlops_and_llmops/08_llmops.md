# LLMOps: vận hành ứng dụng mô hình ngôn ngữ lớn

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **LLMOps: vận hành ứng dụng LLM**. Route đi từ prompt/model bundle → evaluation and tracing → retrieval/tool dependencies → cost/latency controls → safety, privacy, and release management, để ứng dụng LLM có vòng đời quan sát được.

**LLMOps** mở rộng MLOps sang các hệ thống dựa trên mô hình ngôn ngữ lớn (Large Language model — LLM). Điểm khác quan trọng là hành vi của ứng dụng thường không nằm trong một sản phẩm tạo ra (artifact / 산출물) mô hình duy nhất. Nó là kết quả của mô hình (model / 모델), prompt, retrieval, công cụ (tool / 도구), bộ nhớ (memory / 메모리), chính sách (policy / 정책), orchestration và evaluator cùng hoạt động.

Vì vậy đơn vị cần phiên bản (version / 버전) hóa trong LLMOps không phải chỉ là “mô hình (model / 모델)”, mà là **gói hành vi (behavior bundle)** của toàn ứng dụng (application / 애플리케이션).

## Kiến thức tiên quyết

Nên đọc trước [RAG](../09_retrieval_and_rag/README.md), [Agent Systems](../10_agents_and_ai_systems/README.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md), [Evaluation](../18_evaluation_reliability_interpretability/00_evaluation_foundations.md) và [Secure AI System Design](../19_ai_safety_security_alignment/08_secure_ai_system_design.md).

Các kiến thức tiên quyết cung cấp nền tảng; trước hết cần xác định chính xác gói hành vi của ứng dụng LLM.

## Hành vi (behavior / 동작) Bundle

Một phiên bản (version / 버전) ứng dụng LLM nên xác định đầy đủ:

```text
base model / provider + version
system prompt
prompt templates
sampling parameters
embedding model
chunking / parser / index version
retriever / reranker config
context packing policy
tool schemas
agent/workflow graph
memory policy
security/safety policy
evaluation suite
```

Chỉ cần một thành phần đổi, hành vi đầu-cuối có thể đổi dù mô hình (model / 모델) weights giữ nguyên.

Khi gói hành vi đã được xác định, lineage của từng request cho biết thành phần nào đã tạo ra kết quả.

## Lineage của một yêu cầu (request / 요청)

Mỗi yêu cầu (request / 요청) môi trường vận hành (production / 운영 환경) nên truy được về:

```text
request_id
application release
model version
prompt version
retrieval/index version
tool schema version
policy version
memory/context version khi cần
evaluator/verifier version
```

Lineage này giúp trả lời “tại sao hôm nay cùng câu hỏi lại ra kết quả khác tuần trước?”.

Lineage chỉ hữu ích khi prompt cũng có vòng đời và phiên bản có thể truy nguyên.

## Prompt Versioning

Prompt nên được xem như mã (code / 코드)/cấu hình (config / 설정) có vòng đời (lifecycle / 생명주기):

```text
draft
→ review
→ offline eval
→ canary/shadow
→ production
→ rollback/archive
```

Không nên sửa môi trường vận hành (production / 운영 환경) prompt trực tiếp trong UI mà không có kiểm tra (audit / 감사) trail. Prompt diff phải đi cùng kết quả evaluation để biết thay đổi nào tạo regression.

Ngay cả prompt đã được version hóa vẫn có thể thay đổi hành vi khi provider cập nhật, nên bản phát hành phải dựa trên evaluation.

## Provider Drift

Hosted mô hình (model / 모델) có thể được provider cập nhật hoặc alias `latest` có thể thay đổi hành vi (behavior / 동작).

Khi có thể, nên pin phiên bản (version / 버전). Nếu không thể pin, cần:

- lưu provider/mô hình (model / 모델) siêu dữ liệu (metadata / 메타데이터);
- giữ golden/regression set;
- chạy canary định kỳ;
- theo dõi công cụ (tool / 도구)/lược đồ (schema / 스키마) adherence;
- có fallback hoặc chiến lược quay lui (rollback strategy / 롤백 전략).

Provider lớp trừu tượng (abstraction / 추상화) không loại bỏ drift; nó chỉ đổi nơi drift xuất hiện.

Evaluation chỉ đáng tin khi bao phủ cả các trường hợp ổn định, trường hợp ẩn và tải thực tế.

## Bản phát hành (release / 릴리스) dựa trên Evaluation

Generative đầu ra (output / 출력) không hoàn toàn deterministic nên exact-string đơn vị (unit / 단위) kiểm thử (test / 테스트) thường quá giòn. bản phát hành (release / 릴리스) gate nên kết hợp:

```text
semantic correctness
groundedness
citation support
schema validity
tool selection
security cases
latency
cost
```

Nên dùng deterministic validator cho thuộc tính (property / 속성) kiểm trực tiếp được, human/tham chiếu (reference / 참조) set cho chất lượng (quality / 품질) cần judgment và model-based evaluator khi đã hiểu độ lệch (bias / 편향) của evaluator.

Ba loại set bổ trợ cho nhau; eval tiering quyết định khi nào cần chạy mỗi loại để cân bằng chi phí.

## Golden Set, Hidden Set và môi trường vận hành (production / 운영 환경) Set

**Golden set** phù hợp cho regression thường xuyên.

**Hidden/holdout set** giảm nguy cơ overfit vào bộ kiểm thử (test / 테스트) quen thuộc.

**Production-derived set** phản ánh tải công việc (workload / 워크로드) mới xuất hiện.

Một hệ thống trưởng thành cần cả ba thay vì chỉ giữ một benchmark tĩnh.

Khi evaluation đã được phân tầng, cần kiểm soát riêng vòng đời của dữ liệu và chỉ mục trong RAG.

## Eval Tiering

Để cân bằng chi phí:

```text
Tier 1: nhanh/rẻ, chạy mỗi commit
Tier 2: behavioral + RAG/tool, chạy trước release
Tier 3: safety/red-team + human eval, chạy định kỳ hoặc trước thay đổi lớn
Tier 4: shadow/canary online
```

Không cần chạy bộ đánh giá đắt nhất cho mọi thay đổi nhỏ.

RAG có nhiều stage độc lập; vì vậy lineage và freshness của index phải được theo dõi như một phần của release.

## RAGOps

RAG có vòng đời (lifecycle / 생명주기) riêng:

```text
source ingestion
→ parser
→ chunking
→ embedding
→ index build
→ metadata / ACL
→ retrieval
→ reranking
→ context packing
```

Mọi stage có thể tạo regression. Ví dụ mô hình (model / 모델) không đổi nhưng parser mới làm mất heading, khiến chunking và retrieval giảm chất lượng.

Biết nguồn gốc và độ mới của index vẫn chưa đủ; cần đo trực tiếp regression ở bước retrieval.

## Chỉ mục (index / 인덱스) Lineage và Freshness

Cần biết:

```text
index được build từ source snapshot nào?
parser/chunker version nào?
embedding version nào?
ACL metadata version nào?
index build hoàn tất khi nào?
```

Chỉ mục (index / 인덱스) stale là thất bại (failure / 실패) môi trường vận hành (production / 운영 환경) ngay cả khi mô hình (model / 모델) endpoint hoàn toàn khỏe.

Khi retrieval được kiểm soát, phạm vi quan sát mở rộng sang trajectory và các side effect của agent.

## Retrieval Regression

Generation chất lượng (quality / 품질) giảm có thể bắt nguồn từ retrieval.

Nên đo riêng:

- Recall@k;
- MRR / nDCG;
- tỷ lệ retrieval rỗng;
- tỷ lệ relevant ngữ cảnh (context / 맥락);
- citation hỗ trợ (support / 지원);
- ACL-filter tính đúng đắn (correctness / 정확성);
- chỉ mục (index / 인덱스) freshness.

Xem [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md).

AgentOps cần dấu vết bền vững để tái dựng các quyết định và chuyển trạng thái của tác nhân.

## AgentOps

Tác nhân (agent / 에이전트) thêm trajectory động:

```text
planner decisions
tool calls
state transitions
retry / loop
human approvals
side effects
verification
```

Phiên bản (version / 버전) tác nhân (agent / 에이전트) phải bao gồm workflow đồ thị (graph / 그래프), công cụ (tool / 도구) lược đồ (schema / 스키마), trạng thái (state / 상태) chính sách (policy / 정책) và ngân sách (budget / 예산), không chỉ prompt.

Trace cho biết điều gì đã xảy ra; tiếp theo cần kiểm soát hợp đồng của các công cụ mà tác nhân gọi.

## Durable dấu vết (trace / 추적) cho tác nhân (agent / 에이전트)

Dấu vết (trace / 추적) nên đủ để reconstruct:

```text
state trước step
action được đề xuất
policy decision
tool result
state sau step
verification
cost / latency
```

Raw chain-of-thought không phải yêu cầu (requirement / 요구사항) vận hành; structured sự kiện (event / 이벤트) và quyết định (decision / 결정) siêu dữ liệu (metadata / 메타데이터) mới là phần cần cho debugging/kiểm tra (audit / 감사).

Khi schema của tool được quản lý như một API contract, vòng đời của bộ nhớ trở thành phụ thuộc tiếp theo cần version hóa.

## Công cụ (tool / 도구) lược đồ (schema / 스키마) Evolution

Nếu API/công cụ (tool / 도구) đổi trường dữ liệu (field / 필드) hoặc ngữ nghĩa (semantics / 의미론), LLM có thể vẫn sinh argument theo đặc tả hợp đồng (contract / 계약) cũ.

Cần:

```text
schema version
compatibility test
migration window
fallback behavior
deprecation policy
```

Công cụ (tool / 도구) đặc tả hợp đồng (contract / 계약) nên được quản lý giống normal Đặc tả API (API contract / API 계약).

Bộ nhớ có trạng thái lâu dài nên cần chính sách ghi, sửa và xóa; cache lại cần thêm nhận thức về phiên bản.

## Bộ nhớ (memory / 메모리) vòng đời (lifecycle / 생명주기)

Persistent bộ nhớ (memory / 메모리) là một dữ liệu (data / 데이터) store và cần:

- ghi (write / 쓰기) chính sách (policy / 정책);
- retrieval chính sách (policy / 정책);
- provenance;
- TTL/retention;
- correction/delete ngữ nghĩa (semantics / 의미론);
- tenant/người dùng (user / 사용자) phạm vi (scope / 범위);
- privacy controls.

Bộ nhớ (memory / 메모리) ghi (write / 쓰기) từ mô hình (model / 모델) không nên được coi là truth mặc định. Xem [Agent Memory](../10_agents_and_ai_systems/04_agent_memory.md).

Cache phải phản ánh các phiên bản tạo nên kết quả; sau đó router mới có thể chọn model và release một cách có kiểm soát.

## Bộ nhớ đệm (cache / 캐시) và phiên bản (version / 버전) Awareness

Prompt bộ nhớ đệm (cache / 캐시), chính xác (exact / 정확한) bộ nhớ đệm (cache / 캐시), ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시) và retrieval bộ nhớ đệm (cache / 캐시) đều có vô hiệu hóa (invalidation / 무효화) bài toán (problem / 문제).

Bộ nhớ đệm (cache / 캐시) key có thể cần chứa:

```text
model version
prompt version
index version
policy version
tenant/user scope
```

Nếu không, bản phát hành (release / 릴리스) mới có thể tiếp tục trả đầu ra (output / 출력) được tạo bởi hành vi (behavior / 동작) bundle cũ.

Routing làm thay đổi phân bổ tải và chi phí, vì vậy cần đo token, cost và budget theo tác vụ.

## Mô hình (model / 모델) Routing và bản phát hành (release / 릴리스)

Nếu app tuyến (route / 경로) yêu cầu (request / 요청) sang nhiều mô hình (model / 모델), bản phát hành (release / 릴리스) không chỉ là “một mô hình (model / 모델) mới”. Cần phiên bản (version / 버전) router chính sách (policy / 정책) và đánh giá phân phối (distribution / 분포) yêu cầu (request / 요청) theo từng tuyến (route / 경로).

Một thay đổi nhỏ trong router có thể làm chi phí (cost / 비용) hoặc thất bại (failure / 실패) tỷ lệ (rate / 비율) tăng mạnh dù từng mô hình (model / 모델) không đổi.

Chi phí theo tác vụ cần được đọc cùng độ trễ từng stage để biết phần nào đang tạo ra bottleneck.

## Đơn vị từ (token / 토큰), chi phí (cost / 비용) và ngân sách (budget / 예산)

Nên theo dõi theo yêu cầu (request / 요청)/tác vụ (task / 작업):

```text
input tokens
output tokens
model calls
retrieval calls
tool calls
cache hits
agent steps
human escalation
cost / task
```

Với tác nhân (agent / 에이전트), `cost per successful task` có ý nghĩa hơn chi phí (cost / 비용) mỗi mô hình (model / 모델) lời gọi (call / 호출).

Các trace về latency cũng giúp xác định nơi cần tối ưu, nhưng mọi tối ưu phải giữ nguyên các bất biến bảo mật.

## Độ trễ (latency / 지연 시간) Decomposition

Không chỉ đo tổng độ trễ (latency / 지연 시간). dấu vết (trace / 추적) nên tách:

```text
retrieval
reranking
prefill
decode
tool wait
verification
queue time
```

Nếu p99 tăng, decomposition giúp biết cần tối ưu mô hình (model / 모델), chỉ mục (index / 인덱스), công cụ (tool / 도구) hay sức chứa (capacity / 용량).

Các rủi ro đã xác định cần được chuyển thành regression scenario để trở thành một phần của release gate.

## Bảo mật (security / 보안) trong LLMOps

LLMOps phải theo dõi và kiểm thử:

- prompt injection;
- malicious retrieved content;
- công cụ (tool / 도구) abuse;
- cross-tenant retrieval;
- secret leakage;
- bộ nhớ (memory / 메모리) poisoning;
- chính sách (policy / 정책) bypass.

Document được retrieve là dữ liệu không đáng tin mặc định. hệ thống (system / 시스템) prompt không phải ranh giới bảo mật (security boundary / 보안 경계). Xem [Prompt Injection](../19_ai_safety_security_alignment/03_prompt_injection_and_jailbreaks.md).

Regression suite cho biết hệ thống có giữ được bất biến hay không; monitoring sẽ cho biết chúng có bị phá vỡ trong môi trường vận hành hay không.

## Bảo mật (security / 보안) Regression Suite

Mỗi bảo mật (security / 보안) sự cố (incident / 인시던트) hoặc bypass quan trọng nên thành regression scenario:

```text
attack case
→ expected security invariant
→ automated evaluation
→ release gate
```

Ví dụ bất biến (invariant / 불변식): “công cụ (tool / 도구) ghi (write / 쓰기) không chạy nếu không có approval”, bất kể mô hình (model / 모델) đầu ra (output / 출력) nói gì.

Trace vận hành cần được nối với các tín hiệu chất lượng online, nhất là khi ground truth chưa có ngay.

## Monitoring và khả năng quan sát (observability / 관측 가능성)

Một dấu vết (trace / 추적) môi trường vận hành (production / 운영 환경) có thể là:

```text
request
→ prompt assembly
→ retrieval
→ model call
→ tool call
→ model call
→ verifier
→ output
```

Mỗi span nên có độ trễ (latency / 지연 시간), chi phí (cost / 비용), lỗi (error / 오류) và phiên bản (version / 버전) siêu dữ liệu (metadata / 메타데이터).

Không nên log raw prompt/công cụ (tool / 도구) kết quả (result / 결과) nhạy cảm mặc định; cần redaction, sampling và retention chính sách (policy / 정책).

Các proxy online cần được kiểm định theo thời gian, vì chính eval suite cũng có thể drift.

## Online chất lượng (quality / 품질) Signals

Ground truth thường đến trễ. Có thể dùng:

- verified completion;
- người dùng (user / 사용자) correction;
- human escalation;
- citation xác minh (verification / 확인);
- công cụ (tool / 도구) thất bại (failure / 실패);
- nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과);
- delayed labels.

Proxy tín hiệu (signal / 신호) phải được hiểu là proxy, không phải ground truth tuyệt đối.

Khi evaluation phát hiện một cluster thất bại, sự cố cần được phân loại và gắn với kế hoạch quay lui phù hợp.

## Evaluation Drift

Tải công việc (workload / 워크로드) thay đổi theo thời gian. Eval suite cũ có thể không còn đại diện.

Môi trường vận hành (production / 운영 환경) thất bại (failure / 실패) cluster nên quay lại thành kiểm thử (test / 테스트) mới:

```text
production issue
→ classify failure
→ create reproducible case
→ add eval
→ fix
→ prevent regression
```

Rollback là biện pháp khôi phục; canary và shadow giúp thu thập bằng chứng trước khi mở rộng bản phát hành.

## Sự cố (incident / 인시던트) và quay lui (rollback / 롤백)

Quay lui (rollback / 롤백) phải khôi phục **hành vi (behavior / 동작) bundle** tương thích:

```text
model
prompt
retrieval/index config
tool schema
policy
```

Chỉ quay lui (rollback / 롤백) mô hình (model / 모델) có thể không đủ nếu sự cố (incident / 인시던트) đến từ chỉ mục (index / 인덱스) hoặc công cụ (tool / 도구) lược đồ (schema / 스키마) mới.

Xem [Incident Response](./09_incident_response_and_lifecycle.md).

Canary và shadow giảm rủi ro nhưng thêm chi phí và độ phức tạp; đó là sự đánh đổi cần quản lý theo rủi ro.

## Canary và Shadow

Shadow cho candidate nhận production-like yêu cầu (request / 요청) nhưng không tác động người dùng (user / 사용자).

Canary cho một phần traffic thật sử dụng candidate.

Guardrail cần gồm chất lượng (quality / 품질), độ trễ (latency / 지연 시간), chi phí (cost / 비용) và bảo mật (security / 보안) tín hiệu (signal / 신호); không chỉ HTTP lỗi (error / 오류) tỷ lệ (rate / 비율).

Các đánh đổi trên thường bộc lộ qua những failure mode lặp lại trong triển khai.

## Sự đánh đổi (trade-off / 트레이드오프)

LLMOps sâu làm tăng số sản phẩm tạo ra (artifact / 산출물), phiên bản (version / 버전) và evaluation cần quản lý. Quá nhiều gate có thể làm bản phát hành (release / 릴리스) chậm; quá ít gate làm regression khó phát hiện.

Mục tiêu là tăng mức kiểm soát theo rủi ro (risk / 위험) và độ phức tạp (complexity / 복잡도) của ứng dụng (application / 애플리케이션), không xây nền tảng (platform / 플랫폼) nặng nề hơn nhu cầu.

Những failure mode này có thể được đặt vào một mô hình triển khai khép kín để theo dõi từ build đến production.

## Thất bại (failure / 실패) Modes phổ biến

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

- prompt thay đổi nhưng không version;
- model provider update âm thầm;
- index mới build từ corpus thiếu dữ liệu;
- embedding đổi nhưng index chưa rebuild;
- tool schema thay đổi không có compatibility test;
- semantic cache trả result cũ;
- eval set overfit;
- dấu vết (trace / 추적) thiếu phiên bản (version / 버전) siêu dữ liệu (metadata / 메타데이터);
- tác nhân (agent / 에이전트) vòng lặp (loop / 루프) chi phí (cost / 비용) runaway;
- quay lui (rollback / 롤백) chỉ đổi mô hình (model / 모델) nhưng không đổi prompt/chỉ mục (index / 인덱스).

Chuỗi triển khai trên là mô hình tư duy để nối artifact, evaluation, quan sát và phản hồi thành một vòng đời.

## Mô hình triển khai LLMOps

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Git / config registry
→ build behavior bundle
→ offline eval
→ artifact/index registry
→ shadow/canary
→ production
→ trace/monitor
→ feedback + incidents
→ eval dataset update
→ next release
```

Đây là một vòng phản hồi (feedback loop / 피드백 루프) vận hành, không phải chuỗi xử lý (pipeline / 파이프라인) một chiều.

Những nhầm lẫn sau đây kiểm tra xem mô hình vòng đời đó có bị giản lược quá mức hay không.

## Mô hình tư duy

> **LLMOps là quản lý vòng đời của toàn bộ đồ thị (graph / 그래프) tạo hành vi, không chỉ riêng mô hình ngôn ngữ.**

Nếu không truy vết được mô hình (model / 모델) + prompt + retrieval + công cụ (tool / 도구) + chính sách (policy / 정책) đã tạo một đầu ra (output / 출력), hệ thống chưa thật sự reproducible ở cấp ứng dụng (application / 애플리케이션).

Phần liên kết kiến thức đặt LLMOps cạnh các nhánh RAG, agent, evaluation, reliability và security.

## Những nhầm lẫn thường gặp

### “Prompt tốt thì chỉ cần lưu văn bản (text / 텍스트) prompt”

Không. hành vi (behavior / 동작) còn phụ thuộc mô hình (model / 모델), ngữ cảnh (context / 맥락), retrieval, công cụ (tool / 도구) và decoding cấu hình (config / 설정).

### “RAG không train mô hình (model / 모델) nên không cần MLOps”

Không. chỉ mục (index / 인덱스), dữ liệu (data / 데이터) và cấu hình (config / 설정) vẫn cần versioning, evaluation và monitoring.

### “tác nhân (agent / 에이전트) dấu vết (trace / 추적) chỉ để gỡ lỗi (debug / 디버그)”

Không. dấu vết (trace / 추적) còn cần cho evaluation, bảo mật (security / 보안) kiểm tra (audit / 감사), chi phí (cost / 비용) attribution và sự cố (incident / 인시던트) phản hồi (response / 응답).

### “Dùng hosted API thì provider lo hết operations”

Không. Provider chỉ vận hành mô hình (model / 모델) endpoint; ứng dụng (application / 애플리케이션) vòng đời (lifecycle / 생명주기) vẫn thuộc trách nhiệm của bạn.

Các liên kết cuối chương giúp chọn nhánh học tiếp theo và giữ ranh giới của LLMOps.

## Liên kết kiến thức

LLMOps nối [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md), [Evaluation Foundations](../18_evaluation_reliability_interpretability/00_evaluation_foundations.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md) và [Security](../19_ai_safety_security_alignment/08_secure_ai_system_design.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
