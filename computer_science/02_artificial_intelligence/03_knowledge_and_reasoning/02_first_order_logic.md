# First-Order lô-gic (logic / 논리) cho Artificial Intelligence

> **Mạch đọc:** Đặt **First-Order lô-gic (logic / 논리) cho Artificial Intelligence** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Tại sao Propositional lô-gic (logic / 논리) không đủ?** sang **Vocabulary của FOL**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Propositional lô-gic (logic / 논리) có thể biểu diễn `Rain`, `WetRoad`, nhưng không naturally nói “mọi người”, “một người nào đó”, “Alice là parent của Bob”, hay “mọi doctor là professional”. **First-Order lô-gic (logic / 논리)** mở rộng lô-gic (logic / 논리) bằng objects, predicates, functions, variables và quantifiers.

FOL quan trọng trong kiến thức (knowledge / 지식) biểu diễn (representation / 표현) vì nó biểu diễn **nội bộ (internal / 내부) relational cấu trúc (structure / 구조)** của statements thay vì coi mỗi sentence là atomic symbol. Nó là nền của lô-gic (logic / 논리) programming, theorem proving, ontologies và formal specifications.

Xem trước: [Propositional Logic](./01_propositional_logic.md).

## Tại sao Propositional lô-gic (logic / 논리) không đủ?

Suppose lĩnh vực (domain / 도메인) có 10,000 people và quy tắc (rule / 규칙):

> Every human is mortal.

Propositional biểu diễn (representation / 표현) có thể cần viết 10,000 implications:

```text
Human_Alice → Mortal_Alice
Human_Bob → Mortal_Bob
...
```

FOL viết một statement:

\[
\forall x\; Human(x)\rightarrow Mortal(x)
\]

Cấu trúc (structure / 구조) `Human(x)` và variable `x` allow generalization over objects.

## Vocabulary của FOL

Một first-order ngôn ngữ (language / 언어) có:

- **constants**: `Alice`, `Seoul`, `42`;
- **variables**: `x`, `y`;
- **predicates**: `Human(x)`, `LivesIn(x,y)`;
- **functions**: `MotherOf(x)`;
- **logical connectives**: `¬, ∧, ∨, →, ↔`;
- **quantifiers**: `∀, ∃`.

## Terms và formulas

A **term** refers to đối tượng (object / 객체):

```text
Alice
x
MotherOf(Alice)
```

An **atomic formula** applies predicate:

\[
LivesIn(Alice,Seoul)
\]

Complex formula combines atoms/quantifiers.

## Universal quantifier

\[
\forall x\; Human(x)\rightarrow Mortal(x)
\]

means every đối tượng (object / 객체) `x`: if human then mortal.

Important mẫu (pattern / 패턴) uses implication, not conjunction:

Wrong intended universal:

\[
\forall x\; Human(x)\land Mortal(x)
\]

This asserts every đối tượng (object / 객체) in lĩnh vực (domain / 도메인) is both human and mortal.

## Existential quantifier

\[
\exists x\; Human(x)\land LivesIn(x,Seoul)
\]

means at least one đối tượng (object / 객체) both human and lives in Seoul.

For existential, conjunction is dùng chung (common / 공통) to describe witness properties.

## Quantifier phạm vi (scope / 범위)

Compare:

\[
\forall x\exists y\; Loves(x,y)
\]

Everyone loves someone (possibly different people).

vs:

\[
\exists y\forall x\; Loves(x,y)
\]

There exists one person everyone loves.

Thứ tự (order / 순서) matters radically.

This resembles variable phạm vi (scope / 범위) in programming but ngữ nghĩa (semantics / 의미론) are logical quantification.

## Free và bound variables

In:

\[
\forall x\; Parent(x,y)
\]

`x` bound, `y` free.

A sentence/closed formula has no free variables and can receive truth giá trị (value / 값) under interpretation.

Open formula with free variable behaves more like truy vấn (query / 쿼리)/thuộc tính (property / 속성).

## Predicate arity

Unary:

\[
Doctor(x)
\]

Nhị phân (binary / 이진):

\[
WorksAt(x,c)
\]

Ternary:

\[
Transferred(x,amount,account)
\]

Predicate ngữ nghĩa (semantics / 의미론) depend argument positions. Typed schemas help avoid nonsensical combinations.

## Functions vs relations

Hàm (function / 함수) maps inputs to one đối tượng (object / 객체):

\[
MotherOf(x)
\]

Quan hệ (relation / 관계) can hold between objects:

\[
Mother(m,x)
\]

Hàm (function / 함수) implies uniqueness/existence các giả định (assumptions / 가정들). If lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) doesn't guarantee one defined giá trị (value / 값), quan hệ (relation / 관계) may be safer.

## Equality

FOL with equality includes:

\[
x=y
\]

and properties of định danh (identity / 식별자).

Unique-name giả định (assumption / 가정) (different names mean different entities) is not automatically part of tiêu chuẩn (standard / 표준) FOL ngữ nghĩa (semantics / 의미론); some kiến thức (knowledge / 지식) các hệ thống (systems / 시스템들) add it.

Thực thể (entity / 엔터티) định danh (identity / 식별자) is major practical issue in kiến thức (knowledge / 지식) graphs.

## Interpretation

FOL mô hình (model / 모델) includes:

- lĩnh vực (domain / 도메인) `D` of objects;
- ánh xạ (mapping / 매핑) constants → objects;
- predicates → relations over `D`;
- functions → mappings over `D`.

Formula truth depends interpretation.

Cú pháp (syntax / 문법) `CapitalOf(Seoul,Korea)` alone doesn't force intended meaning; ngữ nghĩa (semantics / 의미론) assigns quan hệ (relation / 관계) extension.

## Translation examples

“Every engineer uses some công cụ (tool / 도구)”:

\[
\forall x\;(Engineer(x)\rightarrow \exists y\;(Tool(y)\land Uses(x,y)))
\]

“There is a công cụ (tool / 도구) every engineer uses”:

\[
\exists y\;(Tool(y)\land\forall x\;(Engineer(x)\rightarrow Uses(x,y)))
\]

Again quantifier thứ tự (order / 순서) encodes very different claim.

## Negating quantifiers

De Morgan-like quantifier laws:

\[
\neg\forall x\;P(x)\equiv\exists x\;\neg P(x)
\]

“Not everyone passed” = “someone did not pass”.

\[
\neg\exists x\;P(x)\equiv\forall x\;\neg P(x)
\]

“No one passed” = “everyone did not pass”.

Natural-language phạm vi (scope / 범위) ambiguity makes formalization nontrivial.

## Universal instantiation

From:

\[
\forall x\; Human(x)\rightarrow Mortal(x)
\]

instantiate `x=Socrates`:

\[
Human(Socrates)\rightarrow Mortal(Socrates)
\]

Then with `Human(Socrates)`, Modus Ponens derives `Mortal(Socrates)`.

## Existential instantiation

From:

\[
\exists x\; Human(x)
\]

introduce fresh symbol `k` representing some witness:

\[
Human(k)
\]

But cannot assume `k=Alice` without bằng chứng (evidence / 증거). Freshness matters for soundness.

## Substitution

Substitution:

\[
\theta=\{x/Alice, y/Bob\}
\]

Applied:

\[
Parent(x,y)\theta=Parent(Alice,Bob)
\]

Substitution is mechanical cốt lõi (core / 핵심) of unification and quy tắc (rule / 규칙) ứng dụng (application / 애플리케이션).

## Unification

Unification finds substitution making expressions identical.

Example:

```text
Knows(x, Seoul)
Knows(Alice, y)
```

Most general unifier:

\[
\{x/Alice, y/Seoul\}
\]

Unification enables lô-gic (logic / 논리) programming to match generic rules with specific facts.

## Occurs check

Trying unify:

```text
x = f(x)
```

should thất bại (fail / 실패) in tiêu chuẩn (standard / 표준) finite-term unification because would require infinite term.

Occurs check prevents cyclic substitution, though some Prolog implementations historically optimize/modify hành vi (behavior / 동작).

## Generalized Modus Ponens

Quy tắc (rule / 규칙):

\[
P_1\land\cdots\land P_n\rightarrow Q
\]

If facts unify with premises under substitution `θ`, infer `Qθ`.

Example:

```text
Parent(x,y) ∧ Parent(y,z) → Grandparent(x,z)
Parent(Alice,Bob)
Parent(Bob,Carol)
```

Infer:

```text
Grandparent(Alice,Carol)
```

## Forward chaining in FOL

Repeatedly match quy tắc (rule / 규칙) premises against facts using unification and add conclusions.

Rủi ro (risk / 위험): if functions/new terms generate infinitely many facts, tiến trình (process / 프로세스) may not terminate.

Datalog restricts ngôn ngữ (language / 언어) to achieve finite/tractable hành vi (behavior / 동작) in many settings.

## Backward chaining

Goal:

```text
Grandparent(Alice,Carol)?
```

Match quy tắc (rule / 규칙) conclusion:

```text
Grandparent(x,z)
```

substitute `x=Alice,z=Carol`, then subgoals:

```text
Parent(Alice,y)
Parent(y,Carol)
```

Tìm kiếm (search / 검색) facts/rules for witness `y`.

This is basis of Prolog-style truy vấn (query / 쿼리) resolution.

## Lô-gic (logic / 논리) programming

Prolog program consists of facts/rules:

```prolog
parent(alice, bob).
parent(bob, carol).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).
```

Truy vấn (query / 쿼리):

```prolog
?- grandparent(alice, carol).
```

Procedural hành vi (behavior / 동작) depends quy tắc (rule / 규칙)/thứ tự (order / 순서)/tìm kiếm (search / 검색) chiến lược (strategy / 전략) even though clauses declarative.

Declarative ngữ nghĩa (semantics / 의미론) and operational ngữ nghĩa (semantics / 의미론) must both be understood.

## FOL resolution

To use resolution, formulas convert toward clause form via steps such as:

1. eliminate implications;
2. move negation inward;
3. standardize variables;
4. Skolemize existentials;
5. drop universal quantifiers in clause ngữ cảnh (context / 맥락);
6. convert to CNF;
7. use unification-based resolution.

Skolemization preserves satisfiability, not strict logical equivalence in simple sense.

## Skolemization

Example:

\[
\forall x\exists y\; Loves(x,y)
\]

Replace existential witness by Skolem hàm (function / 함수):

\[
\forall x\; Loves(x,f(x))
\]

Hàm (function / 함수) `f(x)` represents some loved đối tượng (object / 객체) depending on x.

If existential not under universal phạm vi (scope / 범위), fresh Skolem constant may suffice.

## Decidability

Propositional SAT decidable: finite truth assignments.

General First-Order lô-gic (logic / 논리) validity is semi-decidable/undecidable in broad sense: no thuật toán (algorithm / 알고리즘) terminates with correct yes/no for every arbitrary FOL formula validity trường hợp (case / 사례).

This is why practical KR often restricts expressiveness.

## Description Logics

Description Logics are restricted lô-gic (logic / 논리) families designed for concept/role lập luận (reasoning / 추론) with decidability/tractability properties.

Typical constructs:

```text
Person
Doctor ⊑ MedicalProfessional
Doctor ⊓ Researcher
∃worksAt.Hospital
```

They underpin OWL ontology languages.

KR kỹ thuật (engineering / 엔지니어링) often prefers restricted formalism that supports needed suy luận (inference / 추론) reliably over maximal expressiveness.

## Datalog

Datalog is logic-programming ngôn ngữ (language / 언어) without unrestricted hàm (function / 함수) symbols, often finite relational facts/rules.

Example:

```text
parent(x,y) ∧ parent(y,z) → grandparent(x,z)
```

Datalog connects lô-gic (logic / 논리) suy luận (inference / 추론) with recursive databases and quy tắc (rule / 규칙) engines.

SQL recursive CTE and đồ thị (graph / 그래프) truy vấn (query / 쿼리) languages share some conceptual territory.

## Rules and databases

Cơ sở dữ liệu (database / 데이터베이스) facts:

```text
Employee(Alice)
ManagerOf(Alice,Team1)
```

Quy tắc (rule / 규칙):

```text
ManagerOf(x,t) → CanApprove(x,t)
```

Suy luận (inference / 추론) tầng (layer / 계층) derives authorization-like facts.

But bảo mật (security / 보안) policies require careful formal ngữ nghĩa (semantics / 의미론); naive rules may create privilege escalation.

## Temporal limitation

Basic FOL has no built-in thời gian (time / 시간). To mô hình (model / 모델) changing facts:

\[
WorksAt(Alice,Company,2026)
\]

or introduce thời gian (time / 시간) argument:

\[
WorksAt(Alice,Company,t)
\]

Temporal lô-gic (logic / 논리) provides operators like “always”, “eventually”, “until” for temporal properties.

Planning/chuyển tiếp trạng thái (state transition / 상태 전이) lô-gic (logic / 논리) also explicitly các mô hình (models / 모델들) thời gian (time / 시간)/steps.

## Sự kiện (event / 이벤트) calculus / situation calculus

Classical AI developed formalisms for actions/thay đổi (change / 변경).

**Situation Calculus** represents situations as histories and fluents varying by situation.

**sự kiện (event / 이벤트) Calculus** represents events and intervals over which properties hold.

They address **frame bài toán (problem / 문제)**: specifying what stays unchanged when hành động (action / 동작) affects only few facts.

## Frame bài toán (problem / 문제)

If robot moves cup from A to B, we want infer:

- cup location changed;
- wall color unchanged;
- robot serial number unchanged;
- thousands other facts unchanged.

Explicitly writing every non-change is impractical.

Planning STRIPS uses add/delete lists to handle frame các giả định (assumptions / 가정들) operationally.

## Commonsense exception bài toán (problem / 문제)

Quy tắc (rule / 규칙):

\[
Bird(x)\rightarrow Flies(x)
\]

fails for penguins.

Strict FOL quy tắc (rule / 규칙) means no exception unless modeled explicitly.

Default lô-gic (logic / 논리)/non-monotonic lập luận (reasoning / 추론) allows “birds normally fly unless exception known”.

This demonstrates ranh giới (boundary / 경계) between mathematical lô-gic (logic / 논리) and commonsense lập luận (reasoning / 추론).

## Kiến thức (knowledge / 지식) incompleteness

From absence of:

```text
Owns(Alice,Car)
```

FOL does not derive:

```text
¬Owns(Alice,Car)
```

unless closed-world giả định (assumption / 가정)/quy tắc (rule / 규칙) added.

This is trọng yếu (critical / 중요) when integrating databases with lô-gic (logic / 논리) reasoners.

## FOL và kiến thức (knowledge / 지식) Graphs

Triple:

```text
(Alice, worksAt, CompanyX)
```

maps naturally to nhị phân (binary / 이진) predicate:

\[
WorksAt(Alice,CompanyX)
\]

Ontology axioms add logical ngữ nghĩa (semantics / 의미론).

Đồ thị (graph / 그래프) traversal alone is not full FOL lập luận (reasoning / 추론); đồ thị (graph / 그래프) truy vấn (query / 쿼리) ngữ nghĩa (semantics / 의미론) depend ngôn ngữ (language / 언어)/hệ thống (system / 시스템).

## FOL và Natural ngôn ngữ (language / 언어)

Natural ngôn ngữ (language / 언어) contains quantifiers, negation, relations and phạm vi (scope / 범위), so FOL is useful ngữ nghĩa (semantic / 의미적) biểu diễn (representation / 표현).

Sentence:

> Every student read a book.

Can mean each student possibly different book:

\[
\forall x(Student(x)\rightarrow\exists y(Book(y)\land Read(x,y)))
\]

Natural ngôn ngữ (language / 언어) ngữ nghĩa (semantic / 의미적) parsing tries map văn bản (text / 텍스트) into logical/structured forms, but ambiguity/ngữ cảnh (context / 맥락) make tác vụ (task / 작업) hard.

## LLM to lô-gic (logic / 논리)

LLM can translate natural-language requirements into logical các ràng buộc (constraints / 제약조건들), then theorem prover/solver validates.

Kiến trúc (architecture / 아키텍처):

```text
Natural language
     ↓ LLM semantic parsing
FOL / Datalog / SMT-like constraints
     ↓ formal engine
verified answer / counterexample
```

Rủi ro (risk / 위험) lies in translation tính đúng đắn (correctness / 정확성). Formal solver only proves the formula it receives, not that formula faithfully represents người dùng (user / 사용자) intent.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Constant   = named object
Variable   = placeholder object
Predicate  = property/relation
Function   = object-producing mapping
∀          = for every object
∃          = there exists an object
Unification = find substitution matching structures
Inference  = derive statements under formal rules
```

## Dùng chung (common / 공통) Misconceptions

### “∀x P(x) means P is usually true”

No. Universal quantifier means every đối tượng (object / 객체) in lĩnh vực (domain / 도메인) under interpretation satisfies P.

### “∃x means we know which x”

Not necessarily. It asserts at least one witness exists.

### “FOL can represent everything needed in AI”

It is expressive but awkward for bất định (uncertainty / 불확실성), defaults, thời gian (time / 시간) and computational tractability. Other formalisms complement it.

### “Formal proof guarantees real-world conclusion”

Proof guarantees conclusion follows from formal premises. If premises/modeling are wrong or incomplete, real-world claim may still thất bại (fail / 실패).

## Liên kết kiến thức (knowledge connection / 지식 연결)

First-Order lô-gic (logic / 논리) upgrades propositional lập luận (reasoning / 추론) from flat Boolean symbols to relational structures, creating cầu nối (bridge / 브리지) to ontologies, quy tắc (rule / 규칙) engines and kiến thức (knowledge / 지식) Graphs. Its limitations motivate [Probabilistic Reasoning](./04_probabilistic_reasoning.md) and non-monotonic/hybrid approaches.

Xem tiếp: [Inference and Reasoning](./03_inference_and_reasoning.md).
