# Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Deduction** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Induction** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Induction** tiếp nhận điểm tựa từ **Deduction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Abduction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Abduction** tiếp nhận điểm tựa từ **Induction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deduction, induction, abduction together** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Deduction, induction, abduction together** tiếp nhận điểm tựa từ **Abduction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Soundness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deduction, induction, abduction together

Scientific/AI workflow often cycles:

```text
Abduction: propose explanation/model
Induction: learn/generalize from data
Deduction: derive testable consequences
Observation: compare with reality
```

These are complementary, not competing schools.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Soundness** tiếp nhận điểm tựa từ **Deduction, induction, abduction together** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Completeness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Soundness

Suy luận (inference / 추론) procedure is **sound (건전성)** if:

\[
KB\vdash\alpha\Rightarrow KB\các mô hình (models / 모델들)\alpha
\]

Everything it proves is semantically entailed.

A sound theorem prover does not invent invalid proof conclusions relative to formal hệ thống (system / 시스템).

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Completeness** tiếp nhận điểm tựa từ **Soundness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính đúng đắn (correctness / 정확성) vs tractability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Completeness

Procedure is **complete (완전성)** if:

\[
KB\các mô hình (models / 모델들)\alpha\Rightarrow KB\vdash\alpha
\]

Every ngữ nghĩa (semantic / 의미적) consequence can in principle be proved.

Soundness and completeness do not imply efficiency. tìm kiếm (search / 검색) for proof can be enormous or non-terminating in expressive logics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Tính đúng đắn (correctness / 정확성) vs tractability** tiếp nhận điểm tựa từ **Completeness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Forward chaining** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Forward chaining** tiếp nhận điểm tựa từ **Tính đúng đắn (correctness / 정확성) vs tractability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backward chaining** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Backward chaining** tiếp nhận điểm tựa từ **Forward chaining** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Memoization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Memoization** tiếp nhận điểm tựa từ **Backward chaining** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fixed-point lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memoization

Backward lập luận (reasoning / 추론) can repeatedly solve same subgoal. bộ nhớ đệm (cache / 캐시) kết quả (result / 결과):

```text
subgoal → proven/failed/answers
```

Tabling in lô-gic (logic / 논리) programming avoids loops/repeated computation and can improve completeness properties for certain programs.

This is same dynamic-programming idea across AI.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Fixed-point lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Memoization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy tắc (rule / 규칙) xung đột (conflict / 충돌)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Quy tắc (rule / 규칙) xung đột (conflict / 충돌)** tiếp nhận điểm tựa từ **Fixed-point lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Monotonic lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Monotonic lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Quy tắc (rule / 규칙) xung đột (conflict / 충돌)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Non-monotonic lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Non-monotonic lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Monotonic lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Default lô-gic (logic / 논리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Default lô-gic (logic / 논리)** tiếp nhận điểm tựa từ **Non-monotonic lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Circumscription** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Default lô-gic (logic / 논리)

Default quy tắc (rule / 규칙) conceptually:

```text
If Bird(x), and no evidence abnormal,
assume Flies(x)
```

This differs from strict implication.

Many nghiệp vụ (business / 비즈니스) rules implicitly use defaults; encoding them as strict FOL creates exceptions bài toán (problem / 문제).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Circumscription** tiếp nhận điểm tựa từ **Default lô-gic (logic / 논리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Closed-world suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Circumscription

Circumscription minimizes extension of abnormality predicates.

Example:

```text
Bird(x) ∧ ¬Abnormal(x) → Flies(x)
```

Assume as few objects abnormal as possible consistent with kiến thức (knowledge / 지식).

It formalizes “things are normal unless bằng chứng (evidence / 증거) otherwise”.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Closed-world suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Circumscription** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Truth maintenance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Closed-world suy luận (inference / 추론)

Database-like các hệ thống (systems / 시스템들) often infer false from inability to prove:

```text
not Known(P) → assume ¬P
```

This is safe only when kiến thức (knowledge / 지식) cơ sở (base / 기반) intended complete for predicate.

For medical records, absence of diagnosis may not mean patient does not have disease.

Closed-world chính sách (policy / 정책) should be predicate/domain-specific, not universal habit.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Truth maintenance** tiếp nhận điểm tựa từ **Closed-world suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Explanation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truth maintenance

When facts/rules thay đổi (change / 변경), derived conclusions may need retract/cập nhật (update / 업데이트).

Truth Maintenance hệ thống (system / 시스템) tracks justifications/dependencies:

```text
Fact A + Rule R → Conclusion C
```

If A removed, C may need removal unless another justification exists.

Hiện đại (modern / 현대적) dữ liệu (data / 데이터) pipelines similarly need lineage/incremental recomputation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Explanation** tiếp nhận điểm tựa từ **Truth maintenance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lập luận (reasoning / 추론) under inconsistent kiến thức (knowledge / 지식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Lập luận (reasoning / 추론) under inconsistent kiến thức (knowledge / 지식)** tiếp nhận điểm tựa từ **Explanation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lập luận (reasoning / 추론) under bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lập luận (reasoning / 추론) under inconsistent kiến thức (knowledge / 지식)

Classical lô-gic (logic / 논리) with contradiction can explode.

**Paraconsistent lô-gic (logic / 논리)** allows contradictions without deriving arbitrary everything.

Môi trường vận hành (production / 운영 환경) kiến thức (knowledge / 지식) tích hợp (integration / 통합) may need conflict-tolerant approaches because sources disagree.

Another kỹ thuật (engineering / 엔지니어링) approach: preserve provenance and avoid merging conflicts into single unquestioned truth.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Lập luận (reasoning / 추론) under bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **Lập luận (reasoning / 추론) under inconsistent kiến thức (knowledge / 지식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lập luận nhân quả (causal reasoning / 인과적 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Lập luận nhân quả (causal reasoning / 인과적 추론)** tiếp nhận điểm tựa từ **Lập luận (reasoning / 추론) under bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Counterfactual lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Counterfactual lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Lập luận nhân quả (causal reasoning / 인과적 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Case-based lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Counterfactual lập luận (reasoning / 추론)

Counterfactual:

> What would have happened if hành động (action / 동작) A had not occurred?

Requires mô hình (model / 모델) of alternate world sharing background factors, not just conditional xác suất (probability / 확률).

Counterfactuals matter for explanation, chính sách (policy / 정책) phân tích (analysis / 분석) and credit assignment.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Counterfactual lập luận (reasoning / 추론)** cho ta quy tắc; **Case-based lập luận (reasoning / 추론)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Analogical lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Case-based lập luận (reasoning / 추론)** cho ta quy tắc; **Analogical lập luận (reasoning / 추론)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Commonsense lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Analogical lập luận (reasoning / 추론)

Map relational cấu trúc (structure / 구조) from nguồn (source / 소스) lĩnh vực (domain / 도메인) to mục tiêu (target / 대상) lĩnh vực (domain / 도메인).

Example electrical circuit analogy to water luồng (flow / 흐름).

Useful for học tập (learning / 학습)/explanation but analogy can mislead when structural ánh xạ (mapping / 매핑) breaks.

LLMs are good at linguistic analogy generation but need xác minh (verification / 확인) for technical transfer.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Commonsense lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Analogical lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-step lập luận (reasoning / 추론) as tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Commonsense lập luận (reasoning / 추론)

Commonsense involves defaults, vật lý (physical / 물리적) các ràng buộc (constraints / 제약조건들), xã hội (social / 사회적) expectations and temporal kiến thức (knowledge / 지식).

Challenges:

- enormous breadth;
- exceptions;
- ngữ cảnh (context / 맥락) dependence;
- unstated các giả định (assumptions / 가정들);
- incomplete kiến thức (knowledge / 지식).

Pure symbolic encoding difficult; pure statistical mô hình (model / 모델) can be inconsistent. Hybrid approaches remain active research area.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Multi-step lập luận (reasoning / 추론) as tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **Commonsense lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Proof tìm kiếm (search / 검색) độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Proof tìm kiếm (search / 검색) độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **Multi-step lập luận (reasoning / 추론) as tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deductive databases** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Deductive databases** tiếp nhận điểm tựa từ **Proof tìm kiếm (search / 검색) độ phức tạp (complexity / 복잡도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Suy luận (inference / 추론) in kiến thức (knowledge / 지식) Graphs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deductive databases

Datalog + relational facts enables recursive queries.

Transitive closure example:

```text
Reach(x,y) :- Edge(x,y).
Reach(x,z) :- Edge(x,y), Reach(y,z).
```

This computes đồ thị (graph / 그래프) reachability through logical rules.

Databases and lô-gic (logic / 논리) are deeply connected; truy vấn (query / 쿼리) optimizer is a lập luận (reasoning / 추론)/planning engine over thực thi (execution / 실행) alternatives.

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Suy luận (inference / 추론) in kiến thức (knowledge / 지식) Graphs** tiếp nhận điểm tựa từ **Deductive databases** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Neural theorem proving** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Neural theorem proving** tiếp nhận điểm tựa từ **Suy luận (inference / 추론) in kiến thức (knowledge / 지식) Graphs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM lập luận (reasoning / 추론) và xác minh (verification / 확인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Neural theorem proving

Neural mô hình (model / 모델) can score/select proof steps while symbolic kernel verifies each step.

Advantages:

```text
neural → flexible heuristic over huge search
symbolic → correctness guarantee of accepted proof
```

This is chuẩn gốc (canonical / 정본) neuro-symbolic kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **LLM lập luận (reasoning / 추론) và xác minh (verification / 확인)** tiếp nhận điểm tựa từ **Neural theorem proving** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Self-consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Self-consistency** tiếp nhận điểm tựa từ **LLM lập luận (reasoning / 추론) và xác minh (verification / 확인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chain-of-thought vs formal derivation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Self-consistency

Generate multiple lập luận (reasoning / 추론) paths and select majority/final answer can improve some tasks statistically.

But agreement is not proof. Many samples can share same systematic lỗi (error / 오류).

Self-consistency is an inference-time sampling chiến lược (strategy / 전략), not formal logical consistency guarantee.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Chain-of-thought vs formal derivation** tiếp nhận điểm tựa từ **Self-consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lập luận (reasoning / 추론) dấu vết (trace / 추적) provenance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Lập luận (reasoning / 추론) dấu vết (trace / 추적) provenance** tiếp nhận điểm tựa từ **Chain-of-thought vs formal derivation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Lập luận (reasoning / 추론) dấu vết (trace / 추적) provenance** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “lập luận (reasoning / 추론) = deduction”

Deduction chỉ một family. Real AI uses induction, abduction, probabilistic and quyết định (decision / 결정) lập luận (reasoning / 추론).

### “Formal proof means premise is true”

Proof only guarantees quan hệ (relation / 관계) from premises; nguồn (source / 소스)/mô hình (model / 모델) validity separate.

### “LLM explanation is proof of its answer”

Generated rationale can be post-hoc or erroneous. Independent xác minh (verification / 확인) matters.

### “More rules always improve reasoner”

More rules can create conflicts, cycles and explosion. kiến thức (knowledge / 지식) kỹ thuật (engineering / 엔지니어링) chất lượng (quality / 품질) matters.

> **Chuyển mạch:** Trong **Suy luận (inference / 추론) và lập luận (reasoning / 추론) trong Artificial Intelligence**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Suy luận (inference / 추론) is where KR becomes active. It connects lô-gic (logic / 논리) to tìm kiếm (search / 검색), xác suất (probability / 확률), lập luận nhân quả (causal reasoning / 인과적 추론) and hiện đại (modern / 현대적) tool-backed LLM các hệ thống (systems / 시스템들). Later the tác nhân (agent / 에이전트) section will reuse the same kiến trúc (architecture / 아키텍처): proposal → môi trường (environment / 환경)/công cụ (tool / 도구) xác minh (verification / 확인) → trạng thái (state / 상태) cập nhật (update / 업데이트) → replanning.

Xem tiếp: [Probabilistic Reasoning](./04_probabilistic_reasoning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
