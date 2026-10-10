# Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Inference và reasoning trong AI**. Route đi từ deduction → induction/abduction → forward/backward chaining → soundness/completeness → explanation and uncertainty, để mỗi kiểu suy luận có guarantee và giới hạn rõ.

Kiến thức (knowledge / 지식) biểu diễn (representation / 표현) chỉ hữu ích khi hệ thống (system / 시스템) có thể tạo ra conclusion mới hoặc quyết định dựa trên kiến thức (knowledge / 지식). **suy luận (inference / 추론)** là quá trình derive thông tin (information / 정보) từ premises theo một cơ chế (mechanism / 메커니즘); **lập luận (reasoning / 추론)** rộng hơn, bao gồm chọn các giả định (assumptions / 가정들), combine bằng chứng (evidence / 증거), resolve bất định (uncertainty / 불확실성), tìm kiếm (search / 검색) proof, reason về causes/actions và sometimes revise beliefs.

Không có một “lập luận (reasoning / 추론) thuật toán (algorithm / 알고리즘)” universal. Deduction, induction, abduction, default lập luận (reasoning / 추론) và probabilistic suy luận (inference / 추론) trả lời different questions và có different guarantees.

Xem trước: [Propositional Logic](./01_propositional_logic.md) và [First-Order Logic](./02_first_order_logic.md).

## Deduction

Deductive lập luận (reasoning / 추론):

```text
General rule + facts
        ↓
necessary consequence
```

Example:

\[
\forall x\;Human(x)\rightarrow Mortal(x)
\]

\[
Human(Socrates)
\]

therefore:

\[
Mortal(Socrates)
\]

If premises true and suy luận (inference / 추론) valid, conclusion must be true.

Deduction is truth-preserving relative to formal ngữ nghĩa (semantics / 의미론).

Deduction bảo toàn tính đúng khi premises đã đủ, còn induction khái quát từ nhiều quan sát và luôn mang bất định. Vì vậy chuyển từ rule sang dữ liệu kéo theo câu hỏi về độ tin cậy của generalization.

## Induction

Inductive lập luận (reasoning / 추론):

```text
observed examples
        ↓
general pattern/hypothesis
```

Example: observe many transactions and learn classifier predicting fraud.

Conclusion not guaranteed. New examples can falsify mẫu (pattern / 패턴).

Machine học tập (learning / 학습) is largely inductive: finite dữ liệu (data / 데이터) → mô hình (model / 모델) expected to generalize.

Statistics provides khung phần mềm (framework / 프레임워크) to quantify bất định (uncertainty / 불확실성)/generalization.

Induction tìm pattern có thể áp dụng rộng hơn dữ liệu đã thấy; abduction đi ngược lại để tìm giả thuyết tốt nhất giải thích evidence. Hai hướng khác nhau ở việc dự đoán quy luật hay chọn nguyên nhân khả dĩ.

## Abduction

Abduction seeks plausible explanation for observation.

```text
Rule: Fire → Smoke
Observe: Smoke
Possible explanation: Fire
```

This is not deductively valid because other causes can produce smoke.

Medical diagnosis often abductive: symptoms → candidate causes.

Abduction generates hypotheses; xác suất (probability / 확률)/nhân quả (causal / 인과적) kiến thức (knowledge / 지식) ranks them.

Deduction, induction và abduction không cạnh tranh tuyệt đối: hệ thống thường dùng cả ba ở các bước khác nhau của một task. Muốn đánh giá kết quả suy luận, trước hết cần tách soundness khỏi các tiêu chí khác.

## Deduction, induction, abduction together

Scientific/AI workflow often cycles:

```text
Abduction: propose explanation/model
Induction: learn/generalize from data
Deduction: derive testable consequences
Observation: compare with reality
```

These are complementary, not competing schools.

Soundness bảo đảm hệ thống không suy ra kết luận sai từ knowledge hợp lệ. Completeness đặt câu hỏi ngược lại: mọi kết luận được phép suy ra có được tìm thấy hay không.

## Soundness

Suy luận (inference / 추론) procedure is **sound (건전성)** if:

\[
KB\vdash\alpha\Rightarrow KB\các mô hình (models / 모델들)\alpha
\]

Everything it proves is semantically entailed.

A sound theorem prover does not invent invalid proof conclusions relative to formal hệ thống (system / 시스템).

Soundness và completeness là hai mặt của correctness, nhưng đạt cả hai chưa nói gì về chi phí tính toán. Trong hệ thống thực, tractability quyết định liệu guarantee đó có dùng được ở quy mô cần thiết.

## Completeness

Procedure is **complete (완전성)** if:

\[
KB\các mô hình (models / 모델들)\alpha\Rightarrow KB\vdash\alpha
\]

Every ngữ nghĩa (semantic / 의미적) consequence can in principle be proved.

Soundness and completeness do not imply efficiency. tìm kiếm (search / 검색) for proof can be enormous or non-terminating in expressive logics.

Trade-off giữa correctness và tractability dẫn trực tiếp đến chiến lược inference. Forward chaining khởi đầu từ facts và lan các rule có thể kích hoạt, phù hợp khi dữ liệu mới liên tục đến.

## Tính đúng đắn (correctness / 정확성) vs tractability

AI lập luận (reasoning / 추론) thiết kế (design / 설계) balances:

```text
expressiveness
soundness/completeness
runtime
memory
maintainability
```

A restricted quy tắc (rule / 규칙) ngôn ngữ (language / 언어) may be preferable to full FOL because predictable suy luận (inference / 추론) matters in môi trường vận hành (production / 운영 환경).

Forward chaining là data-driven; backward chaining là goal-driven, bắt đầu từ query rồi truy ngược các premise cần chứng minh. Chọn hướng nào phụ thuộc branching factor, số query và độ ổn định của facts.

## Forward chaining

Data-driven lập luận (reasoning / 추론):

```text
known facts
    ↓
find rules whose premises match
    ↓
add conclusions
    ↓
repeat to fixed point
```

Example:

```text
Employee(Alice)
Employee(x) → HasBadge(x)
HasBadge(x) → CanEnterLobby(x)
```

Derive badge and truy cập (access / 접근).

Forward chaining useful when facts arrive and many conclusions may be queried.

Backward chaining thường gặp cùng một subgoal qua nhiều nhánh proof. Memoization lưu kết quả trung gian để tránh lặp, nhưng cache phải gắn với version của knowledge và điều kiện suy luận.

## Backward chaining

Goal-driven:

```text
query
 ↓
which rule could conclude it?
 ↓
prove premises
 ↓
recursively continue
```

To prove `CanEnterLobby(Alice)`, reduce to `HasBadge(Alice)`, then `Employee(Alice)`.

Efficient when truy vấn (query / 쿼리) narrow compared with all possible consequences.

Memoization giảm công việc lặp tại từng query, còn fixed-point reasoning mô tả việc lặp rule cho tới khi không sinh thêm fact. Hai ý tưởng gặp nhau khi hệ thống cần closure ổn định của một knowledge base.

## Memoization

Backward lập luận (reasoning / 추론) can repeatedly solve same subgoal. bộ nhớ đệm (cache / 캐시) kết quả (result / 결과):

```text
subgoal → proven/failed/answers
```

Tabling in lô-gic (logic / 논리) programming avoids loops/repeated computation and can improve completeness properties for certain programs.

This is same dynamic-programming idea across AI.

Fixed point cho ta tập consequence đã hội tụ, nhưng nhiều rule có thể cùng áp dụng và dẫn tới kết luận xung đột. Vì vậy inference engine cần conflict policy và provenance để biết vì sao mỗi kết luận xuất hiện.

## Fixed-point lập luận (reasoning / 추론)

Datalog-style rules can be evaluated until no new facts:

\[
T(K)=K\cup\{\văn bản (text / 텍스트){new consequences}\}
\]

Repeatedly:

\[
K_{i+1}=T(K_i)
\]

until:

\[
K_{i+1}=K_i
\]

This least fixed điểm (point / 지점) defines ngữ nghĩa (semantics / 의미론) for many positive recursive quy tắc (rule / 규칙) programs.

Conflict resolution quyết định cách xử lý nhiều rule cùng kích hoạt, nhưng trong logic monotonic, thêm facts không được làm mất conclusion đã có. Khi thế giới có exception, giả định này bắt đầu trở nên quá mạnh.

## Quy tắc (rule / 규칙) xung đột (conflict / 충돌)

Real quy tắc (rule / 규칙) bases may derive conflicting conclusions.

Example:

```text
PremiumCustomer(x) → Approve(x)
FraudFlag(x) → Reject(x)
```

Alice satisfies both.

Need xung đột (conflict / 충돌) chính sách (policy / 정책):

- priority;
- specificity;
- deny-overrides;
- provenance/trust;
- non-monotonic lô-gic (logic / 논리).

Formal quy tắc (rule / 규칙) ngữ nghĩa (semantics / 의미론) should specify this explicitly.

Monotonic reasoning thuận tiện cho proof và cache vì knowledge tăng chỉ mở rộng consequence. Non-monotonic reasoning cần cho các default có thể bị rút lại khi evidence mới xuất hiện.

## Monotonic lập luận (reasoning / 추론)

In monotonic lô-gic (logic / 논리):

\[
KB\các mô hình (models / 모델들)\alpha
\]

then adding more premises keeps entailment:

\[
KB\cup\{\beta\}\các mô hình (models / 모델들)\alpha
\]

Classical lô-gic (logic / 논리) monotonic.

Real-world default lập luận (reasoning / 추론) often not.

Non-monotonic reasoning cho phép retract conclusion khi exception xuất hiện. Default logic là một cách viết rõ điều kiện áp dụng và điều kiện rút lại của những conclusion tạm thời ấy.

## Non-monotonic lập luận (reasoning / 추론)

Suppose:

```text
Bird(Tweety)
Normally Bird(x) → Flies(x)
```

Infer `Flies(Tweety)`.

Later learn:

```text
Penguin(Tweety)
Penguin(x) → ¬Flies(x)
```

Need retract previous default conclusion.

Non-monotonic lập luận (reasoning / 추론) các mô hình (models / 모델들) revisable conclusions.

Default logic biểu diễn “thường đúng nếu chưa biết ngoại lệ”, còn circumscription chọn mô hình bằng cách tối thiểu hóa các abnormality. Cả hai đều biến phần ngầm thành assumption có thể kiểm tra.

## Default lô-gic (logic / 논리)

Default quy tắc (rule / 규칙) conceptually:

```text
If Bird(x), and no evidence abnormal,
assume Flies(x)
```

This differs from strict implication.

Many nghiệp vụ (business / 비즈니스) rules implicitly use defaults; encoding them as strict FOL creates exceptions bài toán (problem / 문제).

Circumscription điều khiển abnormal predicates trong một semantics hình thức; closed-world inference thường suy ra false từ việc không tìm thấy fact. Điểm chung là dùng absence, nhưng failure boundary của chúng khác nhau.

## Circumscription

Circumscription minimizes extension of abnormality predicates.

Example:

```text
Bird(x) ∧ ¬Abnormal(x) → Flies(x)
```

Assume as few objects abnormal as possible consistent with kiến thức (knowledge / 지식).

It formalizes “things are normal unless bằng chứng (evidence / 증거) otherwise”.

Closed-world assumption có thể tạo kết luận hữu ích trong database, nhưng khi knowledge cập nhật, kết luận cũ phải được rút lại hoặc đánh dấu stale. Truth maintenance giữ các dependency để thực hiện việc đó.

## Closed-world suy luận (inference / 추론)

Database-like các hệ thống (systems / 시스템들) often infer false from inability to prove:

```text
not Known(P) → assume ¬P
```

This is safe only when kiến thức (knowledge / 지식) cơ sở (base / 기반) intended complete for predicate.

For medical records, absence of diagnosis may not mean patient does not have disease.

Closed-world chính sách (policy / 정책) should be predicate/domain-specific, not universal habit.

Truth maintenance ghi lại premise và justification của từng belief, nhờ vậy hệ thống biết conclusion nào bị ảnh hưởng khi một fact đổi. Explanation xây trên dấu vết ấy để trả lời vì sao hệ thống tin một điều.

## Truth maintenance

When facts/rules thay đổi (change / 변경), derived conclusions may need retract/cập nhật (update / 업데이트).

Truth Maintenance hệ thống (system / 시스템) tracks justifications/dependencies:

```text
Fact A + Rule R → Conclusion C
```

If A removed, C may need removal unless another justification exists.

Hiện đại (modern / 현대적) dữ liệu (data / 데이터) pipelines similarly need lineage/incremental recomputation.

Explanation không chỉ phục vụ giao diện; nó còn làm lộ khi các justification mâu thuẫn nhau. Khi knowledge inconsistent, engine phải giới hạn blast radius thay vì để một contradiction làm mọi kết luận trở nên đúng.

## Explanation

Symbolic suy luận (inference / 추론) can produce proof dấu vết (trace / 추적):

```text
Alice can enter because:
Employee(Alice)
Employee → HasBadge
HasBadge → CanEnterLobby
```

This is stronger than post-hoc “tính năng (feature / 기능) importance” because explanation is actual derivation đường dẫn (path / 경로) under quy tắc (rule / 규칙) hệ thống (system / 시스템).

But explanation only as good as rules/premises.

Inconsistent knowledge là xung đột giữa các claim, còn uncertainty là thiếu chắc chắn về claim hoặc world. Hai vấn đề cần cơ chế khác nhau: paraconsistent handling không thay thế calibrated probability.

## Lập luận (reasoning / 추론) under inconsistent kiến thức (knowledge / 지식)

Classical lô-gic (logic / 논리) with contradiction can explode.

**Paraconsistent lô-gic (logic / 논리)** allows contradictions without deriving arbitrary everything.

Môi trường vận hành (production / 운영 환경) kiến thức (knowledge / 지식) tích hợp (integration / 통합) may need conflict-tolerant approaches because sources disagree.

Another kỹ thuật (engineering / 엔지니어링) approach: preserve provenance and avoid merging conflicts into single unquestioned truth.

Uncertainty mô tả mức tin vào khả năng xảy ra, nhưng causal reasoning hỏi điều gì thay đổi nếu ta can thiệp. Từ phân phối quan sát sang intervention là bước đổi semantics quan trọng.

## Lập luận (reasoning / 추론) under bất định (uncertainty / 불확실성)

Strict quy tắc (rule / 규칙):

\[
Symptom(x)\rightarrow Disease(x)
\]

is often unrealistic.

Probabilistic lập luận (reasoning / 추론) assigns:

\[
P(Disease\mid Symptom)
\]

or factor đồ thị (graph / 그래프)/Bayesian mạng (network / 네트워크).

This changes entailment from nhị phân (binary / 이진) proof to posterior belief computation.

See [Probabilistic Reasoning](./04_probabilistic_reasoning.md).

Causal reasoning cung cấp cấu trúc để đánh giá intervention; counterfactual reasoning đi xa hơn bằng cách hỏi một thế giới giả định khác sẽ ra sao dưới cùng lịch sử. Cả hai cần model và assumption rõ.

## Lập luận nhân quả (causal reasoning / 인과적 추론)

Statistical association:

\[
P(Y\mid X)
\]

Lập luận nhân quả (causal reasoning / 인과적 추론) asks:

\[
P(Y\mid do(X=x))
\]

Intervention differs observation.

A quy tắc (rule / 규칙) like `Rain→WetRoad` may encode nhân quả (causal / 인과적) quan hệ (relation / 관계), but material implication alone does not.

Nhân quả (causal / 인과적) graphs and structural nhân quả (causal / 인과적) các mô hình (models / 모델들) explicitly represent mechanisms/interventions.

Counterfactuals dùng model để trả lời “nếu đã làm khác thì sao”; case-based reasoning dùng các tình huống đã gặp để gợi ý quyết định cho case mới. Một bên dựng scenario, bên kia truy hồi precedent.

## Counterfactual lập luận (reasoning / 추론)

Counterfactual:

> What would have happened if hành động (action / 동작) A had not occurred?

Requires mô hình (model / 모델) of alternate world sharing background factors, not just conditional xác suất (probability / 확률).

Counterfactuals matter for explanation, chính sách (policy / 정책) phân tích (analysis / 분석) and credit assignment.

Case-based reasoning dựa vào similarity của tình huống, còn analogical reasoning cần map cấu trúc quan hệ giữa source và target. Vì thế phép tương tự không chỉ là tìm ví dụ có từ khóa giống nhau.

## Case-based lập luận (reasoning / 추론)

Instead of general rules, retrieve similar past cases and adapt solution.

Workflow:

```text
retrieve similar case
reuse solution
revise for new context
retain new experience
```

This is ancestor-like idea to retrieval-based các hệ thống (systems / 시스템들), though hiện đại (modern / 현대적) RAG usually retrieves văn bản (text / 텍스트)/ngữ cảnh (context / 맥락) rather than formal trường hợp (case / 사례) adaptation.

Analogical reasoning có thể chuyển cấu trúc hữu ích sang miền mới, nhưng độ đúng phụ thuộc background knowledge và boundary của phép ánh xạ. Commonsense reasoning cung cấp phần ngầm đó và cũng là nơi dễ phát sinh exception.

## Analogical lập luận (reasoning / 추론)

Map relational cấu trúc (structure / 구조) from nguồn (source / 소스) lĩnh vực (domain / 도메인) to mục tiêu (target / 대상) lĩnh vực (domain / 도메인).

Example electrical circuit analogy to water luồng (flow / 흐름).

Useful for học tập (learning / 학습)/explanation but analogy can mislead when structural ánh xạ (mapping / 매핑) breaks.

LLMs are good at linguistic analogy generation but need xác minh (verification / 확인) for technical transfer.

Analogical reasoning chuyển cấu trúc giữa hai miền, nhưng muốn biết mapping có hợp lệ hay không, agent cần tri thức nền về những điều thường đúng và ngoại lệ. Commonsense reasoning cung cấp context đó nhưng không bao giờ hoàn toàn đầy đủ.

## Commonsense lập luận (reasoning / 추론)

Commonsense involves defaults, vật lý (physical / 물리적) các ràng buộc (constraints / 제약조건들), xã hội (social / 사회적) expectations and temporal kiến thức (knowledge / 지식).

Challenges:

- enormous breadth;
- exceptions;
- ngữ cảnh (context / 맥락) dependence;
- unstated các giả định (assumptions / 가정들);
- incomplete kiến thức (knowledge / 지식).

Pure symbolic encoding difficult; pure statistical mô hình (model / 모델) can be inconsistent. Hybrid approaches remain active research area.

Commonsense reasoning thường phải nối nhiều bước nhỏ, từ observation đến một kết luận hành động. Khi chain dài, có thể xem việc suy luận như search trên không gian proof và state.

## Multi-step lập luận (reasoning / 추론) as tìm kiếm (search / 검색)

Proof lập luận (reasoning / 추론) can be modeled as tìm kiếm (search / 검색):

```text
state = current facts/goals
operator = inference rule
successor = new derived statement/subgoal
objective = proof/counterexample
```

Heuristic theorem proving prioritizes promising clauses.

This connects kiến thức (knowledge / 지식) lập luận (reasoning / 추론) back to [Heuristic Search](../02_search_reasoning_and_planning/02_heuristic_search.md).

Multi-step reasoning as search làm lộ branching factor, depth và chi phí của từng bước. Proof search complexity quyết định khi nào cần heuristic, pruning hoặc giới hạn tài nguyên.

## Proof tìm kiếm (search / 검색) độ phức tạp (complexity / 복잡도)

Even if each suy luận (inference / 추론) quy tắc (rule / 규칙) simple, number possible derivations explodes.

Lập luận (reasoning / 추론) hệ thống (system / 시스템) needs:

- indexing;
- quy tắc (rule / 규칙) thứ tự (ordering / 순서);
- subsumption;
- memoization;
- pruning;
- heuristics.

Formal tính đúng đắn (correctness / 정확성) does not imply computational practicality.

Proof search có thể lặp lại cùng subproof và tốn chi phí lớn. Deductive databases giảm phần này bằng cách lưu fact/rule có cấu trúc và dùng evaluation strategy thay vì tìm lại từ đầu.

## Deductive databases

Datalog + relational facts enables recursive queries.

Transitive closure example:

```text
Reach(x,y) :- Edge(x,y).
Reach(x,z) :- Edge(x,y), Reach(y,z).
```

This computes đồ thị (graph / 그래프) reachability through logical rules.

Databases and lô-gic (logic / 논리) are deeply connected; truy vấn (query / 쿼리) optimizer is a lập luận (reasoning / 추론)/planning engine over thực thi (execution / 실행) alternatives.

Deductive database tối ưu suy luận trên schema và rule; knowledge graph mở rộng bài toán sang thực thể, relation và path giữa nhiều nguồn. Inference trên graph phải giữ cả semantics của edge lẫn provenance.

## Suy luận (inference / 추론) in kiến thức (knowledge / 지식) Graphs

Rules:

```text
parentOf(x,y) ∧ parentOf(y,z)
→ grandparentOf(x,z)
```

Ontology suy luận (inference / 추론):

```text
Doctor subClassOf MedicalProfessional
Alice type Doctor
→ Alice type MedicalProfessional
```

Embedding-based KG completion instead predicts likely missing edges statistically. One gives logical entailment, other probabilistic score.

Knowledge graph cung cấp cấu trúc tường minh để proof search lần theo edge, còn neural theorem proving học representation hoặc heuristic để tìm proof trong không gian lớn. Neural proposal vẫn cần verifier hình thức hoặc constraint rõ.

## Neural theorem proving

Neural mô hình (model / 모델) can score/select proof steps while symbolic kernel verifies each step.

Advantages:

```text
neural → flexible heuristic over huge search
symbolic → correctness guarantee of accepted proof
```

This is chuẩn gốc (canonical / 정본) neuro-symbolic kiến trúc (architecture / 아키텍처).

Neural theorem proving gợi ý các bước chứng minh nhưng không tự bảo đảm soundness. LLM reasoning vì vậy phải đi kèm verification để tách câu trả lời có vẻ hợp lý khỏi derivation hợp lệ.

## LLM lập luận (reasoning / 추론) và xác minh (verification / 확인)

LLM-generated chuỗi (chain / 사슬) of thought may be fluent but invalid.

Reliable kiến trúc (architecture / 아키텍처) can externalize verifiable intermediate sản phẩm tạo ra (artifact / 산출물):

```text
LLM proposes SQL / code / proof / plan
      ↓
parser/type checker/solver executes or verifies
      ↓
feedback to model
      ↓
repair
```

The verifier should check lĩnh vực (domain / 도메인) thuộc tính (property / 속성), not just văn bản (text / 텍스트) style.

Verification có thể kiểm tra từng claim hoặc kết quả cuối, trong khi self-consistency lấy nhiều trajectory rồi tìm đáp án ổn định. Agreement tăng tín hiệu nhưng không thay thế một proof độc lập.

## Self-consistency

Generate multiple lập luận (reasoning / 추론) paths and select majority/final answer can improve some tasks statistically.

But agreement is not proof. Many samples can share same systematic lỗi (error / 오류).

Self-consistency is an inference-time sampling chiến lược (strategy / 전략), not formal logical consistency guarantee.

Self-consistency dựa trên sự hội tụ của nhiều đường suy luận; chain-of-thought có thể hữu ích để phân tích nhưng không đồng nghĩa formal derivation. Cần phân biệt trace giải thích với proof có semantics kiểm chứng được.

## Chain-of-thought vs formal derivation

Natural-language lập luận (reasoning / 추론):

- flexible;
- readable;
- ambiguous;
- may omit steps.

Formal derivation:

- precise cú pháp (syntax / 문법);
- checkable;
- domain-limited;
- potentially expensive to construct.

Hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) can use natural ngôn ngữ (language / 언어) for proposal and formal biểu diễn (representation / 표현) for xác minh (verification / 확인).

Formal derivation cho biết conclusion được suy ra bằng rule nào; trace provenance cho biết premise, nguồn và phiên bản nào đứng sau claim. Hai lớp này giúp audit mà không biến một chuỗi văn bản tự sự thành bằng chứng.

## Lập luận (reasoning / 추론) dấu vết (trace / 추적) provenance

For enterprise AI, useful đầu ra (output / 출력) may include:

```text
answer
supporting sources
rules used
calculations/tool outputs
uncertainty
```

This is more auditable than opaque final answer.

Provenance should reflect actual tiến trình (process / 프로세스), not fabricated explanation.

Provenance làm rõ boundary của niềm tin: điều gì là source fact, điều gì là inference và điều gì do model đề xuất. Mental model cuối chương gom các lớp đó thành quy trình đánh giá có thể lặp lại.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Deduction  = premises guarantee conclusion
Induction  = examples suggest general pattern
Abduction  = observation suggests explanation
Default    = assume normal until exception
Probabilistic = rank beliefs under uncertainty
Causal     = reason about intervention
Search     = explore possible derivations/plans
Verification = check candidate against explicit rules
```

Mental model giúp nối inference method với guarantee, uncertainty, cost và failure boundary. Nhờ vậy có thể sửa các misconception phổ biến thay vì coi mọi câu trả lời trôi chảy là reasoning đúng.

## Dùng chung (common / 공통) Misconceptions

### “lập luận (reasoning / 추론) = deduction”

Deduction chỉ một family. Real AI uses induction, abduction, probabilistic and quyết định (decision / 결정) lập luận (reasoning / 추론).

### “Formal proof means premise is true”

Proof only guarantees quan hệ (relation / 관계) from premises; nguồn (source / 소스)/mô hình (model / 모델) validity separate.

### “LLM explanation is proof of its answer”

Generated rationale can be post-hoc or erroneous. Independent xác minh (verification / 확인) matters.

### “More rules always improve reasoner”

More rules can create conflicts, cycles and explosion. kiến thức (knowledge / 지식) kỹ thuật (engineering / 엔지니어링) chất lượng (quality / 품질) matters.

Những phân biệt này nối inference với knowledge representation, search, probabilistic/causal reasoning và LLM verification. Chọn cơ chế suy luận đúng nghĩa là chọn cả guarantee, audit trail và cách xử lý khi knowledge không đủ.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Suy luận (inference / 추론) is where KR becomes active. It connects lô-gic (logic / 논리) to tìm kiếm (search / 검색), xác suất (probability / 확률), lập luận nhân quả (causal reasoning / 인과적 추론) and hiện đại (modern / 현대적) tool-backed LLM các hệ thống (systems / 시스템들). Later the tác nhân (agent / 에이전트) section will reuse the same kiến trúc (architecture / 아키텍처): proposal → môi trường (environment / 환경)/công cụ (tool / 도구) xác minh (verification / 확인) → trạng thái (state / 상태) cập nhật (update / 업데이트) → replanning.

Xem tiếp: [Probabilistic Reasoning](./04_probabilistic_reasoning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
