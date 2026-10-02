# Propositional lô-gic (logic / 논리) cho Artificial Intelligence

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Propositional logic cho AI**. Route đi từ propositions/valuation → connectives → entailment/satisfiability → CNF/resolution → knowledge-base queries, để logic nối trực tiếp với cơ chế suy luận.

**Propositional lô-gic (logic / 논리)** là một formal ngôn ngữ (language / 언어) để biểu diễn statements có truth giá trị (value / 값) và suy luận từ chúng bằng rules chính xác. Nó là hệ lô-gic (logic / 논리) đơn giản hơn First-Order lô-gic (logic / 논리) nhưng cực kỳ quan trọng vì cho ta vocabulary về cú pháp (syntax / 문법), ngữ nghĩa (semantics / 의미론), entailment, proof, satisfiability và mô hình (model / 모델) checking.

Trong AI, Propositional lô-gic (logic / 논리) xuất hiện trong quy tắc (rule / 규칙) các hệ thống (systems / 시스템들), SAT solving, planning encodings, xác minh (verification / 확인) và ràng buộc (constraint / 제약조건) lập luận (reasoning / 추론). Học nó không phải để viết mọi kiến thức (knowledge / 지식) thành `P ∧ Q`; mục tiêu là hiểu formal lập luận (reasoning / 추론) khác với statistical mẫu (pattern / 패턴) matching ở đâu.

Xem trước: [Knowledge Representation](./00_knowledge_representation.md).

## Proposition

Một proposition là statement có thể true hoặc false.

Examples:

```text
P: It is raining.
Q: The road is wet.
```

Không phải proposition:

```text
"Close the door!"      → command
"What time is it?"     → question
x > 3                   → open formula until x assigned/quantified
```

Propositional lô-gic (logic / 논리) treats `P` như atomic symbol; nó không nhìn inside cấu trúc (structure / 구조) “raining”.

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Connectives** tiếp nhận điểm tựa từ **Proposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Truth bảng (table / 테이블)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Connectives

Dùng chung (common / 공통) logical connectives:

| Symbol | English | 한국어 | Meaning |
|---|---|---|---|
| `¬P` | NOT | 부정 | không P |
| `P ∧ Q` | AND | 논리곱 / 그리고 | P và Q |
| `P ∨ Q` | OR | 논리합 / 또는 | P hoặc Q inclusive |
| `P → Q` | implication | 함의 | nếu P thì Q |
| `P ↔ Q` | biconditional | 동치 | P iff Q |

`∨` mặc định inclusive OR: true khi một hoặc cả hai true.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Truth bảng (table / 테이블)** tiếp nhận điểm tựa từ **Connectives** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cú pháp (syntax / 문법) vs ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truth bảng (table / 테이블)

Implication often causes confusion:

| P | Q | `P → Q` |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

Why is implication true when P false?

Because `P→Q` equivalent:

\[
\neg P\lor Q
\]

It only forbids trường hợp (case / 사례) P true and Q false.

Natural-language “if” may carry nhân quả (causal / 인과적)/temporal meaning not captured by material implication.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Cú pháp (syntax / 문법) vs ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **Truth bảng (table / 테이블)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cú pháp (syntax / 문법) vs ngữ nghĩa (semantics / 의미론)

**cú pháp (syntax / 문법)** defines well-formed formulas.

Example:

\[
(P\land Q)\rightarrow R
\]

**ngữ nghĩa (semantics / 의미론)** defines truth under an interpretation/mô hình (model / 모델) assigning truth values to symbols.

This distinction is fundamental:

```text
syntax    = expression structure
semantics = what makes expression true/false
```

LLM can generate syntactically valid-looking formula while ngữ nghĩa (semantic / 의미적) ánh xạ (mapping / 매핑) to lĩnh vực (domain / 도메인) may still be wrong.

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Mô hình (model / 모델)** tiếp nhận điểm tựa từ **Cú pháp (syntax / 문법) vs ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Satisfiable, valid và unsatisfiable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델)

A mô hình (model / 모델) `M` is assignment of truth values to propositions.

If:

```text
P=true
Q=false
```

then `M` satisfies `P∨Q` but not `P∧Q`.

Notation:

\[
M\các mô hình (models / 모델들)\alpha
\]

means mô hình (model / 모델) `M` satisfies formula `α`.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Satisfiable, valid và unsatisfiable** tiếp nhận điểm tựa từ **Mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Entailment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Satisfiable, valid và unsatisfiable

Formula is **satisfiable** if at least one mô hình (model / 모델) makes it true.

**Valid / tautology** if every mô hình (model / 모델) makes it true.

Example:

\[
P\lor\neg P
\]

always true.

**Unsatisfiable / contradiction** if no mô hình (model / 모델) makes true:

\[
P\land\neg P
\]

These concepts power SAT solving and proof by contradiction.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Entailment** tiếp nhận điểm tựa từ **Satisfiable, valid và unsatisfiable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Entailment

Kiến thức (knowledge / 지식) cơ sở (base / 기반) `KB` entails `α`:

\[
KB\các mô hình (models / 모델들)\alpha
\]

if every mô hình (model / 모델) satisfying `KB` also satisfies `α`.

Important:

> Entailment is ngữ nghĩa (semantic / 의미적) necessity, not merely that α “sounds plausible”.

Example:

\[
KB=\{P\rightarrow Q, P\}
\]

then:

\[
KB\các mô hình (models / 모델들) Q
\]

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Entailment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Modus Ponens** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Suy luận (inference / 추론)

Suy luận (inference / 추론) procedure derives formula syntactically:

\[
KB\vdash\alpha
\]

Distinguish:

```text
⊨ semantic entailment
⊢ syntactic derivability/proof
```

A proof hệ thống (system / 시스템) is **sound** if it derives only entailed statements.

It is **complete** if every entailed statement can in principle be derived.

These terms are about proof các hệ thống (systems / 시스템들), not ML accuracy.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Modus Ponens** tiếp nhận điểm tựa từ **Suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Modus Tollens** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Modus Ponens

Quy tắc (rule / 규칙):

\[
P,\quad P\rightarrow Q
\]

therefore:

\[
Q
\]

Example:

```text
ServerDown → Alert
ServerDown
∴ Alert
```

This is valid regardless lĩnh vực (domain / 도메인) meaning.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Modus Tollens** tiếp nhận điểm tựa từ **Modus Ponens** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logical equivalences** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Modus Tollens

\[
P\rightarrow Q,\quad \neg Q
\]

therefore:

\[
\neg P
\]

But **affirming the consequent** is invalid:

\[
P\rightarrow Q,\quad Q
\]

does not imply `P` because Q may have other causes.

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Logical equivalences** tiếp nhận điểm tựa từ **Modus Tollens** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Normal forms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logical equivalences

Useful transformations:

Double negation:

\[
\neg\neg P\equiv P
\]

De Morgan:

\[
\neg(P\land Q)\equiv \neg P\lor\neg Q
\]

\[
\neg(P\lor Q)\equiv \neg P\land\neg Q
\]

Implication elimination:

\[
P\rightarrow Q\equiv\neg P\lor Q
\]

Biconditional:

\[
P\leftrightarrow Q
\equiv
(P\rightarrow Q)\land(Q\rightarrow P)
\]

These matter when converting formulas to normal forms.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Normal forms** tiếp nhận điểm tựa từ **Logical equivalences** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Clause và literal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Normal forms

### Conjunctive Normal Form

CNF is conjunction of clauses; each clause is disjunction of literals.

\[
(A\lor\neg B)\land(C\lor D)\land(\neg A\lor E)
\]

SAT solvers commonly operate on CNF.

### Disjunctive Normal Form

DNF is disjunction of conjunctions.

\[
(A\land B)\lor(\neg A\land C)
\]

Any propositional formula can be represented in CNF/DNF, but naive conversion may cause exponential blow-up. Tseitin transformation introduces auxiliary variables to produce equisatisfiable CNF with linear-size growth.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Clause và literal** tiếp nhận điểm tựa từ **Normal forms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Resolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Clause và literal

A **literal** is proposition or negation:

```text
P
¬Q
```

Clause:

\[
P\lor\neg Q\lor R
\]

CNF formula is set/conjunction of clauses.

SAT solving uses this cấu trúc (structure / 구조) heavily.

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Resolution** tiếp nhận điểm tựa từ **Clause và literal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Proof by contradiction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Resolution

Resolution quy tắc (rule / 규칙):

\[
(P\lor A),\quad(\neg P\lor B)
\]

infer:

\[
A\lor B
\]

If repeated resolution derives empty clause `□`, contradiction found.

To prove `KB⊨α`, add `¬α` to KB and show unsatisfiable by resolution.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Proof by contradiction** tiếp nhận điểm tựa từ **Resolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Horn clauses** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Proof by contradiction

Want prove `Q` from:

```text
P
P → Q
```

Convert implication:

\[
\neg P\lor Q
\]

Add `¬Q`.

Resolve `¬P∨Q` with `¬Q` → `¬P`.

Resolve `¬P` with `P` → empty clause.

Thus các giả định (assumptions / 가정들) + `¬Q` inconsistent, so Q entailed.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Horn clauses** tiếp nhận điểm tựa từ **Proof by contradiction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Forward chaining** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Horn clauses

Horn clause has at most one positive literal.

Example:

\[
\neg P\lor\neg Q\lor R
\]

which corresponds:

\[
P\land Q\rightarrow R
\]

Horn lô-gic (logic / 논리) supports efficient forward/backward chaining and underlies quy tắc (rule / 규칙) các hệ thống (systems / 시스템들)/lô-gic (logic / 논리) programming fragments.

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Forward chaining** tiếp nhận điểm tựa từ **Horn clauses** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backward chaining** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Forward chaining

Start with known facts and repeatedly fire rules whose premises satisfied.

```text
Facts: A, B
Rules:
A ∧ B → C
C → D
```

Derive C, then D.

Forward chaining is **data-driven**.

Useful when many possible conclusions or streaming facts.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Backward chaining** tiếp nhận điểm tựa từ **Forward chaining** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SAT bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backward chaining

Start from truy vấn (query / 쿼리)/goal and ask what premises would prove it.

To prove `D`:

```text
Need C
To prove C need A and B
Check facts A,B
```

Backward chaining is **goal-driven**.

Prolog-style lập luận (reasoning / 추론) uses backward chaining with unification at First-Order mức (level / 수준).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **SAT bài toán (problem / 문제)** tiếp nhận điểm tựa từ **Backward chaining** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DPLL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SAT bài toán (problem / 문제)

SAT asks:

> Is there an assignment to Boolean variables making formula true?

SAT is NP-complete, yet hiện đại (modern / 현대적) solvers handle enormous structured instances.

Applications:

- hardware xác minh (verification / 확인);
- planning;
- scheduling/cấu hình (configuration / 구성);
- phụ thuộc (dependency / 의존성) resolution;
- theorem proving;
- software phân tích (analysis / 분석).

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **DPLL** tiếp nhận điểm tựa từ **SAT bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đơn vị (unit / 단위) propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DPLL

DPLL extends backtracking SAT with:

- đơn vị (unit / 단위) propagation;
- pure literal elimination;
- branching.

Hiện đại (modern / 현대적) CDCL solvers bản dựng (build / 빌드) on related foundation with xung đột (conflict / 충돌) học tập (learning / 학습) and non-chronological backtracking.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Đơn vị (unit / 단위) propagation** tiếp nhận điểm tựa từ **DPLL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conflict-Driven Clause học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị (unit / 단위) propagation

Clause:

\[
A\lor B\lor C
\]

If `A=false` and `B=false`, then `C=true` forced.

Propagate forced assignments before branching.

This is same “reason before tìm kiếm (search / 검색)” principle seen in CSP.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Conflict-Driven Clause học tập (learning / 학습)** tiếp nhận điểm tựa từ **Đơn vị (unit / 단위) propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Knowledge-base consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conflict-Driven Clause học tập (learning / 학습)

When assignments cause xung đột (conflict / 충돌), analyze implication đồ thị (graph / 그래프) and learn clause preventing same reason for xung đột (conflict / 충돌).

CDCL vòng lặp (loop / 루프) conceptually:

```text
propagate
  ↓
branch
  ↓
conflict?
  ├─ no → continue
  └─ yes → analyze → learn clause → backjump
```

Learned clause is logically implied, so solver becomes smarter without sacrificing tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Knowledge-base consistency** tiếp nhận điểm tựa từ **Conflict-Driven Clause học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Closed-world lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Knowledge-base consistency

If KB contains:

\[
P
\]

and:

\[
\neg P
\]

classical lô-gic (logic / 논리) KB inconsistent.

Under principle of explosion, from contradiction arbitrary formula can be derived in classical lô-gic (logic / 논리).

Real kiến thức (knowledge / 지식) bases may contain conflicts, motivating paraconsistent logics, provenance-aware lập luận (reasoning / 추론) or tường minh (explicit / 명시적) conflict-resolution policies.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Closed-world lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Knowledge-base consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lô-gic (logic / 논리) và software conditions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Closed-world lập luận (reasoning / 추론)

Propositional lô-gic (logic / 논리) itself does not say absent facts false. Closed-world giả định (assumption / 가정) is extra ngữ nghĩa (semantic / 의미적) chính sách (policy / 정책).

Quy tắc (rule / 규칙) engine may implement **negation as thất bại (failure / 실패)**:

```text
if cannot prove P, assume not P
```

This differs from classical logical negation.

Confusing them causes subtle bugs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Lô-gic (logic / 논리) và software conditions** tiếp nhận điểm tựa từ **Closed-world lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SAT vs SMT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lô-gic (logic / 논리) và software conditions

Boolean lô-gic (logic / 논리) underlies mã (code / 코드):

```java
if (authenticated && !locked) {
    allow();
}
```

But program trạng thái (state / 상태)/thời gian (time / 시간)/side effects make full software ngữ nghĩa (semantics / 의미론) richer than propositional formulas.

Formal xác minh (verification / 확인) often translates program properties into SAT/SMT các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **SAT vs SMT** tiếp nhận điểm tựa từ **Lô-gic (logic / 논리) và software conditions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lô-gic (logic / 논리) vs xác suất (probability / 확률)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SAT vs SMT

SAT variables Boolean.

**SMT (Satisfiability Modulo Theories)** adds theories such as:

- integers/reals;
- arrays;
- bit-vectors;
- strings;
- uninterpreted functions.

Example:

\[
x>3\land y=x+2\land y<4
\]

requires arithmetic lý thuyết (theory / 이론), not pure Boolean atoms alone unless encoded.

SMT is highly relevant for program xác minh (verification / 확인) and solver-backed agents.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Lô-gic (logic / 논리) vs xác suất (probability / 확률)** tiếp nhận điểm tựa từ **SAT vs SMT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lô-gic (logic / 논리) vs LLM lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lô-gic (logic / 논리) vs xác suất (probability / 확률)

Classical lô-gic (logic / 논리):

```text
P true / false
```

Xác suất (probability / 확률):

```text
P(P)=0.7
```

Lô-gic (logic / 논리) captures structural certainty; xác suất (probability / 확률) captures bất định (uncertainty / 불확실성).

A quy tắc (rule / 규칙) `Smoke→Fire` in strict lô-gic (logic / 논리) means every smoke trường hợp (case / 사례) implies fire. Real-world quan hệ (relation / 관계) is probabilistic, so forcing it into strict implication is wrong modeling.

Biểu diễn (representation / 표현) must match lĩnh vực (domain / 도메인) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Lô-gic (logic / 논리) vs LLM lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Lô-gic (logic / 논리) vs xác suất (probability / 확률)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Planning as SAT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lô-gic (logic / 논리) vs LLM lập luận (reasoning / 추론)

LLM can produce logically valid sequences but next-token generation does not guarantee sound proof.

Hybrid approach:

```text
LLM proposes theorem/proof steps
        ↓
formal logic engine checks validity
        ↓
accept / reject / repair
```

This mẫu (pattern / 패턴) combines flexible ngôn ngữ (language / 언어) lập luận (reasoning / 추론) with symbolic xác minh (verification / 확인).

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Planning as SAT** tiếp nhận điểm tựa từ **Lô-gic (logic / 논리) vs LLM lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Planning as SAT

Bounded planning can introduce Boolean variables:

```text
ActionA_t
AtRobotRoom1_t
AtRobotRoom2_t
```

Các ràng buộc (constraints / 제약조건들) encode hành động (action / 동작) preconditions, effects and exactly-one conditions.

SAT solver finding assignment corresponds to plan.

This illustrates representational reduction: planning becomes satisfiability.

> **Chuyển mạch:** Ở chặng này của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Planning as SAT** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Proposition  = atomic true/false claim
Formula      = claims combined by logical operators
Model        = assignment making formulas true/false
Entailment   = true in every model of KB
Proof        = syntactic derivation
SAT          = does at least one model exist?
Resolution   = mechanical inference over clauses
Forward chain = facts → consequences
Backward chain = goal → required premises
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “P→Q means P causes Q”

Material implication encodes truth điều kiện (condition / 조건), not causality.

### “If Q is true and P→Q, then P must be true”

Affirming consequent is invalid.

### “Not known means false”

Only under tường minh (explicit / 명시적) closed-world/negation-as-failure các giả định (assumptions / 가정들).

### “SAT is NP-complete nên solver practical không dùng được”

Worst-case hardness does not prevent solving many large structured instances efficiently.

> **Chuyển mạch:** Trong **Propositional lô-gic (logic / 논리) cho Artificial Intelligence**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Propositional lô-gic (logic / 논리) connects KR with CSP/SAT, planning and formal xác minh (verification / 확인). It introduces the ngữ nghĩa (semantic / 의미적)/syntactic distinction needed before First-Order lô-gic (logic / 논리) and gives a baseline for understanding why probabilistic/neural lập luận (reasoning / 추론) offer different trade-offs.

Xem tiếp: [First-Order Logic](./02_first_order_logic.md) và [Inference and Reasoning](./03_inference_and_reasoning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
