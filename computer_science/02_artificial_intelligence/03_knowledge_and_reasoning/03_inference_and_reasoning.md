# Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence

> **Mạch đọc:** Đặt **suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Deduction** sang **Induction**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Deduction, induction, abduction together

Scientific/AI workflow often cycles:

```text
Abduction: propose explanation/model
Induction: learn/generalize from data
Deduction: derive testable consequences
Observation: compare with reality
```

These are complementary, not competing schools.

## Soundness

Suy luận (inference / 추론) procedure is **sound (건전성)** if:

\[
KB\vdash\alpha\Rightarrow KB\các mô hình (models / 모델들)\alpha
\]

Everything it proves is semantically entailed.

A sound theorem prover does not invent invalid proof conclusions relative to formal hệ thống (system / 시스템).

## Completeness

Procedure is **complete (완전성)** if:

\[
KB\các mô hình (models / 모델들)\alpha\Rightarrow KB\vdash\alpha
\]

Every ngữ nghĩa (semantic / 의미적) consequence can in principle be proved.

Soundness and completeness do not imply efficiency. tìm kiếm (search / 검색) for proof can be enormous or non-terminating in expressive logics.

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

## Memoization

Backward lập luận (reasoning / 추론) can repeatedly solve same subgoal. bộ nhớ đệm (cache / 캐시) kết quả (result / 결과):

```text
subgoal → proven/failed/answers
```

Tabling in lô-gic (logic / 논리) programming avoids loops/repeated computation and can improve completeness properties for certain programs.

This is same dynamic-programming idea across AI.

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

## Default lô-gic (logic / 논리)

Default quy tắc (rule / 규칙) conceptually:

```text
If Bird(x), and no evidence abnormal,
assume Flies(x)
```

This differs from strict implication.

Many nghiệp vụ (business / 비즈니스) rules implicitly use defaults; encoding them as strict FOL creates exceptions bài toán (problem / 문제).

## Circumscription

Circumscription minimizes extension of abnormality predicates.

Example:

```text
Bird(x) ∧ ¬Abnormal(x) → Flies(x)
```

Assume as few objects abnormal as possible consistent with kiến thức (knowledge / 지식).

It formalizes “things are normal unless bằng chứng (evidence / 증거) otherwise”.

## Closed-world suy luận (inference / 추론)

Database-like các hệ thống (systems / 시스템들) often infer false from inability to prove:

```text
not Known(P) → assume ¬P
```

This is safe only when kiến thức (knowledge / 지식) cơ sở (base / 기반) intended complete for predicate.

For medical records, absence of diagnosis may not mean patient does not have disease.

Closed-world chính sách (policy / 정책) should be predicate/domain-specific, not universal habit.

## Truth maintenance

When facts/rules thay đổi (change / 변경), derived conclusions may need retract/cập nhật (update / 업데이트).

Truth Maintenance hệ thống (system / 시스템) tracks justifications/dependencies:

```text
Fact A + Rule R → Conclusion C
```

If A removed, C may need removal unless another justification exists.

Hiện đại (modern / 현대적) dữ liệu (data / 데이터) pipelines similarly need lineage/incremental recomputation.

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

## Lập luận (reasoning / 추론) under inconsistent kiến thức (knowledge / 지식)

Classical lô-gic (logic / 논리) with contradiction can explode.

**Paraconsistent lô-gic (logic / 논리)** allows contradictions without deriving arbitrary everything.

Môi trường vận hành (production / 운영 환경) kiến thức (knowledge / 지식) tích hợp (integration / 통합) may need conflict-tolerant approaches because sources disagree.

Another kỹ thuật (engineering / 엔지니어링) approach: preserve provenance and avoid merging conflicts into single unquestioned truth.

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

## Counterfactual lập luận (reasoning / 추론)

Counterfactual:

> What would have happened if hành động (action / 동작) A had not occurred?

Requires mô hình (model / 모델) of alternate world sharing background factors, not just conditional xác suất (probability / 확률).

Counterfactuals matter for explanation, chính sách (policy / 정책) phân tích (analysis / 분석) and credit assignment.

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

## Analogical lập luận (reasoning / 추론)

Map relational cấu trúc (structure / 구조) from nguồn (source / 소스) lĩnh vực (domain / 도메인) to mục tiêu (target / 대상) lĩnh vực (domain / 도메인).

Example electrical circuit analogy to water luồng (flow / 흐름).

Useful for học tập (learning / 학습)/explanation but analogy can mislead when structural ánh xạ (mapping / 매핑) breaks.

LLMs are good at linguistic analogy generation but need xác minh (verification / 확인) for technical transfer.

## Commonsense lập luận (reasoning / 추론)

Commonsense involves defaults, vật lý (physical / 물리적) các ràng buộc (constraints / 제약조건들), xã hội (social / 사회적) expectations and temporal kiến thức (knowledge / 지식).

Challenges:

- enormous breadth;
- exceptions;
- ngữ cảnh (context / 맥락) dependence;
- unstated các giả định (assumptions / 가정들);
- incomplete kiến thức (knowledge / 지식).

Pure symbolic encoding difficult; pure statistical mô hình (model / 모델) can be inconsistent. Hybrid approaches remain active research area.

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

## Deductive databases

Datalog + relational facts enables recursive queries.

Transitive closure example:

```text
Reach(x,y) :- Edge(x,y).
Reach(x,z) :- Edge(x,y), Reach(y,z).
```

This computes đồ thị (graph / 그래프) reachability through logical rules.

Databases and lô-gic (logic / 논리) are deeply connected; truy vấn (query / 쿼리) optimizer is a lập luận (reasoning / 추론)/planning engine over thực thi (execution / 실행) alternatives.

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

## Neural theorem proving

Neural mô hình (model / 모델) can score/select proof steps while symbolic kernel verifies each step.

Advantages:

```text
neural → flexible heuristic over huge search
symbolic → correctness guarantee of accepted proof
```

This is chuẩn gốc (canonical / 정본) neuro-symbolic kiến trúc (architecture / 아키텍처).

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

## Self-consistency

Generate multiple lập luận (reasoning / 추론) paths and select majority/final answer can improve some tasks statistically.

But agreement is not proof. Many samples can share same systematic lỗi (error / 오류).

Self-consistency is an inference-time sampling chiến lược (strategy / 전략), not formal logical consistency guarantee.

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

## Dùng chung (common / 공통) Misconceptions

### “lập luận (reasoning / 추론) = deduction”

Deduction chỉ một family. Real AI uses induction, abduction, probabilistic and quyết định (decision / 결정) lập luận (reasoning / 추론).

### “Formal proof means premise is true”

Proof only guarantees quan hệ (relation / 관계) from premises; nguồn (source / 소스)/mô hình (model / 모델) validity separate.

### “LLM explanation is proof of its answer”

Generated rationale can be post-hoc or erroneous. Independent xác minh (verification / 확인) matters.

### “More rules always improve reasoner”

More rules can create conflicts, cycles and explosion. kiến thức (knowledge / 지식) kỹ thuật (engineering / 엔지니어링) chất lượng (quality / 품질) matters.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Suy luận (inference / 추론) is where KR becomes active. It connects lô-gic (logic / 논리) to tìm kiếm (search / 검색), xác suất (probability / 확률), lập luận nhân quả (causal reasoning / 인과적 추론) and hiện đại (modern / 현대적) tool-backed LLM các hệ thống (systems / 시스템들). Later the tác nhân (agent / 에이전트) section will reuse the same kiến trúc (architecture / 아키텍처): proposal → môi trường (environment / 환경)/công cụ (tool / 도구) xác minh (verification / 확인) → trạng thái (state / 상태) cập nhật (update / 업데이트) → replanning.

Xem tiếp: [Probabilistic Reasoning](./04_probabilistic_reasoning.md).
