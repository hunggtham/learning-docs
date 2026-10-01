# Symbolic AI và Neuro-Symbolic AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Symbolic AI và Neuro-Symbolic AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Symbolic AI bắt đầu từ đâu?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Strength của symbolic các hệ thống (systems / 시스템들)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Artificial Intelligence thường được kể như một cuộc chuyển giao: **Symbolic AI thất bại → Machine học tập (learning / 학습) thắng → Deep học tập (learning / 학습) thay thế mọi thứ cũ**. Câu chuyện này quá đơn giản. Symbolic và neural approaches có strengths khác nhau; nhiều reliable các hệ thống (systems / 시스템들) hiện đại kết hợp learned perception/ngôn ngữ (language / 언어) với tường minh (explicit / 명시적) tools, các ràng buộc (constraints / 제약조건들), tìm kiếm (search / 검색), databases và formal xác minh (verification / 확인).

**Symbolic AI (기호주의 인공지능)** biểu diễn kiến thức (knowledge / 지식) bằng symbols, rules và structured relations. **Neural AI** học phân tán (distributed / 분산) representations và functions từ dữ liệu (data / 데이터). **Neuro-Symbolic AI (신경-기호 인공지능)** là umbrella term cho approaches cố kết hợp hai families, nhưng không có một kiến trúc (architecture / 아키텍처) duy nhất mang tên này.

Xem trước: [Knowledge Representation](./00_knowledge_representation.md), [Inference and Reasoning](./03_inference_and_reasoning.md), và [Knowledge Graphs](./06_knowledge_graphs.md).

## Symbolic AI bắt đầu từ đâu?

Symbolic các hệ thống (systems / 시스템들) giả định nhiều aspects của intelligence có thể modeled bằng:

```text
symbols
+ rules
+ search/inference
```

Examples:

- theorem prover;
- expert hệ thống (system / 시스템);
- STRIPS planner;
- SAT/SMT solver;
- quy tắc (rule / 규칙) engine;
- ontology reasoner.

A symbol như `Patient42`, predicate `HasSymptom(x,Fever)` và quy tắc (rule / 규칙) `A∧B→C` có tường minh (explicit / 명시적) ngữ nghĩa (semantics / 의미론) do designer/lĩnh vực (domain / 도메인) define.

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **Strength của symbolic các hệ thống (systems / 시스템들)** tiếp nhận điểm tựa từ **Symbolic AI bắt đầu từ đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weakness của symbolic các hệ thống (systems / 시스템들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Strength của symbolic các hệ thống (systems / 시스템들)

### Explicitness

Quy tắc (rule / 규칙) có thể inspect:

```text
HighRisk(x) ∧ MissingKYC(x) → ManualReview(x)
```

Hệ thống (system / 시스템) designer biết quan hệ (relation / 관계) nào được encoded.

### Xác minh (verification / 확인)

Formal proof/solver có thể guarantee candidate satisfies các ràng buộc (constraints / 제약조건들) relative to mô hình (model / 모델).

### Compositional cấu trúc (structure / 구조)

Symbols và relations combine systematically. quy tắc (rule / 규칙) applies to new entities without retraining if facts fit lược đồ (schema / 스키마).

### Dữ liệu (data / 데이터) efficiency

If lĩnh vực (domain / 도메인) rules known, hệ thống (system / 시스템) không cần thousands examples để rediscover them statistically.

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **Weakness của symbolic các hệ thống (systems / 시스템들)** tiếp nhận điểm tựa từ **Strength của symbolic các hệ thống (systems / 시스템들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Neural các hệ thống (systems / 시스템들) start from học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weakness của symbolic các hệ thống (systems / 시스템들)

### Kiến thức (knowledge / 지식) acquisition bottleneck

Human experts phải encode huge number rules/facts.

### Brittleness

Quy tắc (rule / 규칙) written for clean symbolic đầu vào (input / 입력) may thất bại (fail / 실패) when real dữ liệu (data / 데이터) noisy/ambiguous.

### Perception gap

Images, audio và natural ngôn ngữ (language / 언어) do not arrive as clean symbols.

### Commonsense quy mô (scale / 규모)

Explicitly encoding every exception/ngữ cảnh (context / 맥락) is difficult.

These weaknesses helped drive statistical ML and Deep học tập (learning / 학습).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **Neural các hệ thống (systems / 시스템들) start from học tập (learning / 학습)** tiếp nhận điểm tựa từ **Weakness của symbolic các hệ thống (systems / 시스템들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Symbolic vs neural is not nhị phân (binary / 이진)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Neural các hệ thống (systems / 시스템들) start from học tập (learning / 학습)

Neural mô hình (model / 모델):

\[
f_\theta(x)
\]

learns parameters from dữ liệu (data / 데이터) using tối ưu hóa (optimization / 최적화).

Instead of manually define features/rules, biểu diễn (representation / 표현) can be learned end-to-end.

Strengths:

- perception;
- ngôn ngữ (language / 언어);
- similarity/generalization;
- high-dimensional noisy dữ liệu (data / 데이터);
- scalable học tập (learning / 학습) from massive datasets.

Weaknesses:

- opaque nội bộ (internal / 내부) representations;
- hard guarantees difficult;
- brittle OOD hành vi (behavior / 동작);
- chính xác (exact / 정확한) ràng buộc (constraint / 제약조건) satisfaction not automatic;
- factual kiến thức (knowledge / 지식) hard to cập nhật (update / 업데이트) selectively.

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **Symbolic vs neural is not nhị phân (binary / 이진)** tiếp nhận điểm tựa từ **Neural các hệ thống (systems / 시스템들) start from học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **A useful decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Symbolic vs neural is not nhị phân (binary / 이진)

Many các hệ thống (systems / 시스템들) already hybrid without using label “neuro-symbolic”.

Example tìm kiếm (search / 검색) engine:

```text
neural embedding retrieval
+ boolean filters
+ database indexes
+ ranking rules
```

Example coding tác nhân (agent / 에이전트):

```text
LLM proposes code
+ compiler/type checker
+ tests
+ shell/git tools
```

Trình biên dịch (compiler / 컴파일러) is symbolic/formal thành phần (component / 컴포넌트) providing chính xác (exact / 정확한) phản hồi (feedback / 피드백).

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **A useful decomposition** tiếp nhận điểm tựa từ **Symbolic vs neural is not nhị phân (binary / 이진)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Neural perception → symbolic lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## A useful decomposition

Instead of asking “symbolic or neural?”, ask which thành phần (component / 컴포넌트) requires which thuộc tính (property / 속성):

| Need | Often suitable cơ chế (mechanism / 메커니즘) |
|---|---|
| Perception from raw pixels/audio | neural mô hình (model / 모델) |
| ngữ nghĩa (semantic / 의미적) similarity | embeddings |
| Hard nghiệp vụ (business / 비즈니스) ràng buộc (constraint / 제약조건) | quy tắc (rule / 규칙)/solver |
| chính xác (exact / 정확한) arithmetic | calculator/thời gian chạy (runtime / 런타임) |
| Relational factual store | cơ sở dữ liệu (database / 데이터베이스)/KG |
| Flexible ngôn ngữ (language / 언어) giao diện (interface / 인터페이스) | LLM |
| Formal proof | theorem prover |
| Combinatorial planning | tìm kiếm (search / 검색)/solver + learned heuristic |

Hệ thống (system / 시스템) kiến trúc (architecture / 아키텍처) can compose mechanisms.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **Neural perception → symbolic lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **A useful decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Symbolic cấu trúc (structure / 구조) guiding neural học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Neural perception → symbolic lập luận (reasoning / 추론)

Classic mẫu (pattern / 패턴):

```text
image
 ↓ neural detector
objects + attributes
 ↓ symbolic rules/planner
reasoning/action
```

Rủi ro (risk / 위험): perception errors become wrong symbols. Downstream reasoner may be perfectly logical about incorrect detections.

Need bất định (uncertainty / 불확실성)/confidence at giao diện (interface / 인터페이스).

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **Symbolic cấu trúc (structure / 구조) guiding neural học tập (learning / 학습)** tiếp nhận điểm tựa từ **Neural perception → symbolic lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differentiable lô-gic (logic / 논리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Symbolic cấu trúc (structure / 구조) guiding neural học tập (learning / 학습)

Rules/các ràng buộc (constraints / 제약조건들) can shape huấn luyện (training / 학습) mục tiêu (objective / 목표).

Suppose known ràng buộc (constraint / 제약조건):

\[
A(x)\rightarrow B(x)
\]

One can add penalty when neural predictions violate implication.

This creates **soft ràng buộc (constraint / 제약조건)** rather than guaranteed symbolic enforcement unless final đầu ra (output / 출력) checked separately.

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **Differentiable lô-gic (logic / 논리)** tiếp nhận điểm tựa từ **Symbolic cấu trúc (structure / 구조) guiding neural học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lô-gic (logic / 논리) Tensor Networks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differentiable lô-gic (logic / 논리)

Some methods replace Boolean truth with continuous values `[0,1]` and logical operators with differentiable relaxations.

Example fuzzy-style conjunction may use:

\[
T(a,b)=ab
\]

or other t-norms.

Then logical consistency becomes differentiable mất mát (loss / 손실).

Benefits: train by độ dốc (gradient / 기울기).

Limitation: relaxed truth ngữ nghĩa (semantics / 의미론) differ from classical lô-gic (logic / 논리); satisfaction may be approximate, not proof.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **Lô-gic (logic / 논리) Tensor Networks** tiếp nhận điểm tựa từ **Differentiable lô-gic (logic / 논리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Neural theorem proving** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lô-gic (logic / 논리) Tensor Networks

Lô-gic (logic / 논리) Tensor Network-like approaches ground predicates into neural functions and translate logical formulas into differentiable satisfaction objectives.

Mô hình tư duy (mental model / 사고 모델):

```text
symbolic formula
   ↓ differentiable relaxation
training loss
   ↓
neural parameters
```

This integrates prior kiến thức (knowledge / 지식) into học tập (learning / 학습) but does not automatically inherit classical theorem-proving guarantees.

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **Neural theorem proving** tiếp nhận điểm tựa từ **Lô-gic (logic / 논리) Tensor Networks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Learned heuristic + symbolic tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Neural theorem proving

A learned mô hình (model / 모델) can guide proof tìm kiếm (search / 검색):

```text
current proof state
 ↓ neural model ranks lemmas/tactics
formal prover executes step
 ↓
valid next proof state or failure
```

Tính đúng đắn (correctness / 정확성) comes from formal kernel; neural mạng (network / 네트워크) improves tìm kiếm (search / 검색) efficiency.

This is one of clearest neuro-symbolic patterns because roles are separated cleanly.

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **Learned heuristic + symbolic tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **Neural theorem proving** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM + SAT/SMT solver** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Learned heuristic + symbolic tìm kiếm (search / 검색)

Tìm kiếm (search / 검색) thuật toán (algorithm / 알고리즘) needs heuristic `h(s)` or chính sách (policy / 정책) thứ tự (ordering / 순서). Neural mạng (network / 네트워크) predicts promising actions/giá trị (value / 값), while symbolic chuyển tiếp trạng thái (state transition / 상태 전이) remains chính xác (exact / 정확한).

AlphaZero-like game các hệ thống (systems / 시스템들):

```text
neural policy/value
+ Monte Carlo Tree Search
+ exact game rules
```

Again học tập (learning / 학습) and symbolic/tìm kiếm (search / 검색) computation complement each other.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **LLM + SAT/SMT solver** tiếp nhận điểm tựa từ **Learned heuristic + symbolic tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM + mã (code / 코드) thực thi (execution / 실행)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM + SAT/SMT solver

Natural-language yêu cầu (requirement / 요구사항):

> Schedule 5 workers, no overlapping shifts, Alice unavailable Tuesday...

Kiến trúc (architecture / 아키텍처):

```text
natural language
 ↓ LLM extracts variables/constraints
SMT/CP-SAT model
 ↓ solver
valid assignment / unsat
 ↓ LLM explains
```

The solver guarantees các ràng buộc (constraints / 제약조건들) encoded. The weak link is ngữ nghĩa (semantic / 의미적) translation from người dùng (user / 사용자) văn bản (text / 텍스트) to các ràng buộc (constraints / 제약조건들), so hệ thống (system / 시스템) should expose/check extracted mô hình (model / 모델).

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **LLM + mã (code / 코드) thực thi (execution / 실행)** tiếp nhận điểm tựa từ **LLM + SAT/SMT solver** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM + kiến thức (knowledge / 지식) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM + mã (code / 코드) thực thi (execution / 실행)

For arithmetic/dữ liệu (data / 데이터) phân tích (analysis / 분석):

```text
question
 ↓ LLM writes code/query
runtime executes exact computation
 ↓ actual result
LLM explains result
```

This is a practical hybrid kiến trúc (architecture / 아키텍처). LLM is not asked to simulate calculator internally when deterministic executor exists.

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **LLM + kiến thức (knowledge / 지식) đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **LLM + mã (code / 코드) thực thi (execution / 실행)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RAG as hybrid AI?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM + kiến thức (knowledge / 지식) đồ thị (graph / 그래프)

LLM can perform thực thể (entity / 엔터티) linking/truy vấn (query / 쿼리) generation and verbalization; KG stores tường minh (explicit / 명시적) facts/relations.

```text
user question
 ↓ semantic parse/entity link
structured graph query
 ↓ KG
facts + provenance
 ↓ LLM
answer
```

This enables fresh/updatable kiến thức (knowledge / 지식) and auditability.

But đồ thị (graph / 그래프) coverage may be incomplete; LLM must not infer absence as false unless lược đồ (schema / 스키마) uses closed-world ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **RAG as hybrid AI?** tiếp nhận điểm tựa từ **LLM + kiến thức (knowledge / 지식) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Program synthesis + xác minh (verification / 확인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RAG as hybrid AI?

RAG combines neural retrieval/generation with bên ngoài (external / 외부) symbolic-ish văn bản (text / 텍스트) store/chỉ mục (index / 인덱스), but calling every RAG hệ thống (system / 시스템) “neuro-symbolic” stretches term.

Plain véc-tơ (vector / 벡터) RAG has no tường minh (explicit / 명시적) symbolic lập luận (reasoning / 추론). KG-RAG or solver-backed RAG is more clearly hybrid.

Use kiến trúc (architecture / 아키텍처) description rather than label hype.

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **Program synthesis + xác minh (verification / 확인)** gom các mảnh từ **RAG as hybrid AI?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Ràng buộc (constraint / 제약조건) decoding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Program synthesis + xác minh (verification / 확인)

Neural mô hình (model / 모델) proposes program; tests/static phân tích (analysis / 분석)/formal verifier checks.

Vòng lặp (loop / 루프):

```text
propose
 ↓
execute/verify
 ↓ error/counterexample
repair
 ↺
```

Counterexample provides high-information phản hồi (feedback / 피드백). This mẫu (pattern / 패턴) is central to reliable coding agents.

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **Ràng buộc (constraint / 제약조건) decoding** gom các mảnh từ **Program synthesis + xác minh (verification / 확인)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Typed tools** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ràng buộc (constraint / 제약조건) decoding

Instead of generate arbitrary tokens then reject, decoder can enforce grammar/lược đồ (schema / 스키마) during generation.

Examples:

- JSON grammar;
- SQL grammar;
- finite-state các ràng buộc (constraints / 제약조건들);
- regex/CFG-guided decoding.

This guarantees syntactic cấu trúc (structure / 구조), not necessarily ngữ nghĩa (semantic / 의미적) tính đúng đắn (correctness / 정확성).

`{"age": -500}` can be valid JSON but invalid lĩnh vực (domain / 도메인) giá trị (value / 값).

Ngữ nghĩa (semantic / 의미적) kiểm tra hợp lệ (validation / 검증) remains separate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **Typed tools** tiếp nhận điểm tựa từ **Ràng buộc (constraint / 제약조건) decoding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Separation of proposer and verifier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Typed tools

Hàm (function / 함수) calling lược đồ (schema / 스키마) provides symbolic giao diện (interface / 인터페이스):

```text
search(query: string, top_k: int)
transfer(amount: decimal, account_id: string)
```

Kiểu (type / 타입)/lược đồ (schema / 스키마) reduces hành động (action / 동작) không gian (space / 공간) and allows kiểm tra hợp lệ (validation / 검증).

Công cụ (tool / 도구) hiện thực (implementation / 구현) then interacts with deterministic hệ thống bên ngoài (external system / 외부 시스템).

LLM chooses hành động (action / 동작); công cụ (tool / 도구) enforces ngữ nghĩa (semantics / 의미론)/permissions.

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **Separation of proposer and verifier** tiếp nhận điểm tựa từ **Typed tools** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xác minh (verification / 확인) is only relative to specification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Separation of proposer and verifier

A robust mẫu (pattern / 패턴) across hybrid AI:

```text
Proposer
  flexible / learned / creative
        ↓
Verifier
  strict / deterministic / formal
        ↓
Executor
        ↓
Feedback
```

Examples:

- LLM ↔ trình biên dịch (compiler / 컴파일러);
- planner ↔ ràng buộc (constraint / 제약조건) validator;
- theorem mô hình (model / 모델) ↔ proof kernel;
- mã (code / 코드) mô hình (model / 모델) ↔ tests;
- extraction mô hình (model / 모델) ↔ lược đồ (schema / 스키마) validator.

This kiến trúc (architecture / 아키텍처) reduces need for one mô hình (model / 모델) to be both creative and perfectly reliable.

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **Xác minh (verification / 확인) is only relative to specification** tiếp nhận điểm tựa từ **Separation of proposer and verifier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Soft vs hard các ràng buộc (constraints / 제약조건들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xác minh (verification / 확인) is only relative to specification

A solver can certify:

```text
schedule satisfies encoded constraints
```

It cannot certify:

```text
encoded constraints perfectly reflect stakeholder intent
```

This **specification gap** is central.

Formal xác minh (verification / 확인) moves bất định (uncertainty / 불확실성) from thực thi (execution / 실행) tính đúng đắn (correctness / 정확성) toward modeling tính đúng đắn (correctness / 정확성); it does not eliminate all bất định (uncertainty / 불확실성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **Soft vs hard các ràng buộc (constraints / 제약조건들)** tiếp nhận điểm tựa từ **Xác minh (verification / 확인) is only relative to specification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Neuro-symbolic biểu diễn (representation / 표현) học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Soft vs hard các ràng buộc (constraints / 제약조건들)

Neural mất mát (loss / 손실) penalty:

\[
L=L_{tác vụ (task / 작업)}+\lambda L_{ràng buộc (constraint / 제약조건)}
\]

makes violations costly but possible.

Hard solver ràng buộc (constraint / 제약조건):

\[
g(x)\le0
\]

rejects invalid solutions entirely.

Choose based yêu cầu (requirement / 요구사항). Safety-critical bất biến (invariant / 불변식) usually should not rely only on soft huấn luyện (training / 학습) penalty if deterministic enforcement possible.

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **Neuro-symbolic biểu diễn (representation / 표현) học tập (learning / 학습)** tiếp nhận điểm tựa từ **Soft vs hard các ràng buộc (constraints / 제약조건들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hệ thống (system / 시스템) 1 / hệ thống (system / 시스템) 2 analogy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Neuro-symbolic biểu diễn (representation / 표현) học tập (learning / 학습)

Some methods learn embeddings while preserving known relational cấu trúc (structure / 구조).

Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) embedding trains vectors from triples; đồ thị (graph / 그래프) neural networks propagate typed neighborhood thông tin (information / 정보).

These are hybrid in a broad sense, though not necessarily performing formal symbolic suy luận (inference / 추론).

The term should be used carefully.

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **Hệ thống (system / 시스템) 1 / hệ thống (system / 시스템) 2 analogy** tiếp nhận điểm tựa từ **Neuro-symbolic biểu diễn (representation / 표현) học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **When symbolic rules are a poor fit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ thống (system / 시스템) 1 / hệ thống (system / 시스템) 2 analogy

People sometimes lời gọi (call / 호출) neural mô hình (model / 모델) “hệ thống (system / 시스템) 1” fast intuition and symbolic tìm kiếm (search / 검색) “hệ thống (system / 시스템) 2” slow lập luận (reasoning / 추론), borrowing psychology terminology.

This can be a useful metaphor but is not literal cognitive equivalence. kỹ thuật (engineering / 엔지니어링) kiến trúc (architecture / 아키텍처) should be described concretely: proposal mạng (network / 네트워크), tìm kiếm (search / 검색), verifier, bộ nhớ (memory / 메모리), công cụ (tool / 도구) thực thi (execution / 실행).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **When symbolic rules are a poor fit** tiếp nhận điểm tựa từ **Hệ thống (system / 시스템) 1 / hệ thống (system / 시스템) 2 analogy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **When neural các mô hình (models / 모델들) are a poor fit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## When symbolic rules are a poor fit

Do not force symbolic modeling when:

- category ranh giới (boundary / 경계) inherently fuzzy;
- raw đầu vào (input / 입력) high-dimensional;
- rules impossible to enumerate;
- môi trường (environment / 환경) rapidly changes;
- ngữ nghĩa (semantics / 의미론) learned from examples matter more than formal các ràng buộc (constraints / 제약조건들).

Ảnh (image / 이미지) recognition from pixels is classic example where Deep học tập (learning / 학습) outperforms handcrafted symbolic vision pipelines.

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **When neural các mô hình (models / 모델들) are a poor fit** tiếp nhận điểm tựa từ **When symbolic rules are a poor fit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lỗi (error / 오류) composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## When neural các mô hình (models / 모델들) are a poor fit

Do not ask neural mạng (network / 네트워크) alone for:

- chính xác (exact / 정확한) tax calculation when formula known;
- hard access-control quy tắc (rule / 규칙);
- deterministic cơ sở dữ liệu (database / 데이터베이스) phép nối (join / 조인);
- cryptographic xác minh (verification / 확인);
- proof checker;
- constraint-satisfaction guarantee.

Use deterministic tools and let mô hình (model / 모델) orchestrate when ngôn ngữ (language / 언어) flexibility needed.

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **Lỗi (error / 오류) composition** tiếp nhận điểm tựa từ **When neural các mô hình (models / 모델들) are a poor fit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giao diện (interface / 인터페이스) thiết kế (design / 설계) matters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lỗi (error / 오류) composition

Hybrid hệ thống (system / 시스템) has multiple thất bại (failure / 실패) probabilities:

```text
semantic parse error
+ retrieval error
+ solver/model assumption error
+ tool execution error
+ explanation error
```

Adding verifier does not guarantee entire chuỗi xử lý (pipeline / 파이프라인) if upstream/downstream components can mis-handle results.

Evaluation must be end-to-end plus component-level.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **Giao diện (interface / 인터페이스) thiết kế (design / 설계) matters** tiếp nhận điểm tựa từ **Lỗi (error / 오류) composition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Confidence and abstention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giao diện (interface / 인터페이스) thiết kế (design / 설계) matters

Neural-symbolic ranh giới (boundary / 경계) should expose structured trạng thái (state / 상태), not ambiguous prose where possible.

Good:

```json
{
  "customer_id": "C123",
  "risk_score": 0.82,
  "kyc_status": "MISSING"
}
```

Quy tắc (rule / 규칙) engine can consume reliably.

Free-form sentence parsing at every step adds unnecessary bất định (uncertainty / 불확실성).

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **Confidence and abstention** tiếp nhận điểm tựa từ **Giao diện (interface / 인터페이스) thiết kế (design / 설계) matters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Neuro-symbolic benchmark question** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Confidence and abstention

If neural parser uncertain, hệ thống (system / 시스템) may abstain/ask clarification instead of feed dubious symbols into strict solver.

A perfect solver on wrong parse can create confidently wrong kết quả (outcome / 결과).

Hybrid các hệ thống (systems / 시스템들) need uncertainty-aware handoff.

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, **Neuro-symbolic benchmark question** tiếp nhận điểm tựa từ **Confidence and abstention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Neuro-symbolic benchmark question

When paper claims neuro-symbolic improvement, ask:

- what symbolic kiến thức (knowledge / 지식) is provided?
- what is learned?
- where are guarantees?
- is lô-gic (logic / 논리) hard or differentiable soft?
- how is noise handled?
- does hệ thống (system / 시스템) generalize compositionally or just fit benchmark?

Kiến trúc (architecture / 아키텍처) label alone does not answer chất lượng (quality / 품질).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Symbolic AI và Neuro-Symbolic AI**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Neuro-symbolic benchmark question** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Symbolic AI
  explicit facts/rules/constraints
  + exact search/inference

Neural AI
  learned distributed representations
  + statistical generalization

Hybrid / Neuro-Symbolic
  use each where its strengths fit

Learned proposer → formal verifier → executor → feedback
```

> **Chuyển mạch:** Trong **Symbolic AI và Neuro-Symbolic AI**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Symbolic AI đã chết”

Formal solvers, rules, databases, planners and compilers remain essential; hiện đại (modern / 현대적) AI often embeds them as tools/components.

### “Neuro-symbolic automatically gives neural flexibility + symbolic guarantee”

Only if kiến trúc (architecture / 아키텍처) truly has a sound verifier/enforcement tầng (layer / 계층). Differentiable lô-gic (logic / 논리) penalties are not same as hard proof.

### “RAG = neuro-symbolic AI”

Plain véc-tơ (vector / 벡터) RAG is hybrid retrieval/generation but does not necessarily include symbolic biểu diễn (representation / 표현)/lập luận (reasoning / 추론).

### “Formal verifier makes hệ thống (system / 시스템) correct”

It guarantees properties encoded in specification, not tính đúng đắn (correctness / 정확성) of natural-language interpretation or real-world các giả định (assumptions / 가정들).

> **Chuyển mạch:** Ở chặng này của **Symbolic AI và Neuro-Symbolic AI**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Neuro-symbolic thiết kế (design / 설계) closes the kiến thức (knowledge / 지식) biểu diễn (representation / 표현) tầng (layer / 계층) and prepares the chuyển tiếp (transition / 전이) to Machine học tập (learning / 학습). The central lesson is architectural: learned các mô hình (models / 모델들) are powerful at perception, ngôn ngữ (language / 언어) and heuristic proposal; symbolic/deterministic các hệ thống (systems / 시스템들) are powerful at tường minh (explicit / 명시적) trạng thái (state / 상태), các ràng buộc (constraints / 제약조건들), chính xác (exact / 정확한) computation and xác minh (verification / 확인).

Later sections on RAG, Agents and AI Engineering will reuse this pattern repeatedly.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
