# First-Order Logic cho Artificial Intelligence

Propositional Logic có thể biểu diễn `Rain`, `WetRoad`, nhưng không naturally nói “mọi người”, “một người nào đó”, “Alice là parent của Bob”, hay “mọi doctor là professional”. **First-Order Logic (FOL / 일차 논리 / logic vị từ bậc nhất)** mở rộng logic bằng objects, predicates, functions, variables và quantifiers.

FOL quan trọng trong Knowledge Representation vì nó biểu diễn **internal relational structure** của statements thay vì coi mỗi sentence là atomic symbol. Nó là nền của logic programming, theorem proving, ontologies và formal specifications.

Xem trước: [Propositional Logic](./01_propositional_logic.md).

## Tại sao Propositional Logic không đủ?

Suppose domain có 10,000 people và rule:

> Every human is mortal.

Propositional representation có thể cần viết 10,000 implications:

```text
Human_Alice → Mortal_Alice
Human_Bob → Mortal_Bob
...
```

FOL viết một statement:

\[
\forall x\; Human(x)\rightarrow Mortal(x)
\]

Structure `Human(x)` và variable `x` allow generalization over objects.

## Vocabulary của FOL

Một first-order language có:

- **constants**: `Alice`, `Seoul`, `42`;
- **variables**: `x`, `y`;
- **predicates**: `Human(x)`, `LivesIn(x,y)`;
- **functions**: `MotherOf(x)`;
- **logical connectives**: `¬, ∧, ∨, →, ↔`;
- **quantifiers**: `∀, ∃`.

## Terms và formulas

A **term** refers to object:

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

means every object `x`: if human then mortal.

Important pattern uses implication, not conjunction:

Wrong intended universal:

\[
\forall x\; Human(x)\land Mortal(x)
\]

This asserts every object in domain is both human and mortal.

## Existential quantifier

\[
\exists x\; Human(x)\land LivesIn(x,Seoul)
\]

means at least one object both human and lives in Seoul.

For existential, conjunction is common to describe witness properties.

## Quantifier scope

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

Order matters radically.

This resembles variable scope in programming but semantics are logical quantification.

## Free và bound variables

In:

\[
\forall x\; Parent(x,y)
\]

`x` bound, `y` free.

A sentence/closed formula has no free variables and can receive truth value under interpretation.

Open formula with free variable behaves more like query/property.

## Predicate arity

Unary:

\[
Doctor(x)
\]

Binary:

\[
WorksAt(x,c)
\]

Ternary:

\[
Transferred(x,amount,account)
\]

Predicate semantics depend argument positions. Typed schemas help avoid nonsensical combinations.

## Functions vs relations

Function maps inputs to one object:

\[
MotherOf(x)
\]

Relation can hold between objects:

\[
Mother(m,x)
\]

Function implies uniqueness/existence assumptions. If domain knowledge doesn't guarantee one defined value, relation may be safer.

## Equality

FOL with equality includes:

\[
x=y
\]

and properties of identity.

Unique-name assumption (different names mean different entities) is not automatically part of standard FOL semantics; some knowledge systems add it.

Entity identity is major practical issue in knowledge graphs.

## Interpretation

FOL model includes:

- domain `D` of objects;
- mapping constants → objects;
- predicates → relations over `D`;
- functions → mappings over `D`.

Formula truth depends interpretation.

Syntax `CapitalOf(Seoul,Korea)` alone doesn't force intended meaning; semantics assigns relation extension.

## Translation examples

“Every engineer uses some tool”:

\[
\forall x\;(Engineer(x)\rightarrow \exists y\;(Tool(y)\land Uses(x,y)))
\]

“There is a tool every engineer uses”:

\[
\exists y\;(Tool(y)\land\forall x\;(Engineer(x)\rightarrow Uses(x,y)))
\]

Again quantifier order encodes very different claim.

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

Natural-language scope ambiguity makes formalization nontrivial.

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

But cannot assume `k=Alice` without evidence. Freshness matters for soundness.

## Substitution

Substitution:

\[
\theta=\{x/Alice, y/Bob\}
\]

Applied:

\[
Parent(x,y)\theta=Parent(Alice,Bob)
\]

Substitution is mechanical core of unification and rule application.

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

Unification enables logic programming to match generic rules with specific facts.

## Occurs check

Trying unify:

```text
x = f(x)
```

should fail in standard finite-term unification because would require infinite term.

Occurs check prevents cyclic substitution, though some Prolog implementations historically optimize/modify behavior.

## Generalized Modus Ponens

Rule:

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

Repeatedly match rule premises against facts using unification and add conclusions.

Risk: if functions/new terms generate infinitely many facts, process may not terminate.

Datalog restricts language to achieve finite/tractable behavior in many settings.

## Backward chaining

Goal:

```text
Grandparent(Alice,Carol)?
```

Match rule conclusion:

```text
Grandparent(x,z)
```

substitute `x=Alice,z=Carol`, then subgoals:

```text
Parent(Alice,y)
Parent(y,Carol)
```

Search facts/rules for witness `y`.

This is basis of Prolog-style query resolution.

## Logic programming

Prolog program consists of facts/rules:

```prolog
parent(alice, bob).
parent(bob, carol).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).
```

Query:

```prolog
?- grandparent(alice, carol).
```

Procedural behavior depends rule/order/search strategy even though clauses declarative.

Declarative semantics and operational semantics must both be understood.

## FOL resolution

To use resolution, formulas convert toward clause form via steps such as:

1. eliminate implications;
2. move negation inward;
3. standardize variables;
4. Skolemize existentials;
5. drop universal quantifiers in clause context;
6. convert to CNF;
7. use unification-based resolution.

Skolemization preserves satisfiability, not strict logical equivalence in simple sense.

## Skolemization

Example:

\[
\forall x\exists y\; Loves(x,y)
\]

Replace existential witness by Skolem function:

\[
\forall x\; Loves(x,f(x))
\]

Function `f(x)` represents some loved object depending on x.

If existential not under universal scope, fresh Skolem constant may suffice.

## Decidability

Propositional SAT decidable: finite truth assignments.

General First-Order Logic validity is semi-decidable/undecidable in broad sense: no algorithm terminates with correct yes/no for every arbitrary FOL formula validity case.

This is why practical KR often restricts expressiveness.

## Description Logics

Description Logics are restricted logic families designed for concept/role reasoning with decidability/tractability properties.

Typical constructs:

```text
Person
Doctor ⊑ MedicalProfessional
Doctor ⊓ Researcher
∃worksAt.Hospital
```

They underpin OWL ontology languages.

KR engineering often prefers restricted formalism that supports needed inference reliably over maximal expressiveness.

## Datalog

Datalog is logic-programming language without unrestricted function symbols, often finite relational facts/rules.

Example:

```text
parent(x,y) ∧ parent(y,z) → grandparent(x,z)
```

Datalog connects logic inference with recursive databases and rule engines.

SQL recursive CTE and graph query languages share some conceptual territory.

## Rules and databases

Database facts:

```text
Employee(Alice)
ManagerOf(Alice,Team1)
```

Rule:

```text
ManagerOf(x,t) → CanApprove(x,t)
```

Inference layer derives authorization-like facts.

But security policies require careful formal semantics; naive rules may create privilege escalation.

## Temporal limitation

Basic FOL has no built-in time. To model changing facts:

\[
WorksAt(Alice,Company,2026)
\]

or introduce time argument:

\[
WorksAt(Alice,Company,t)
\]

Temporal Logic provides operators like “always”, “eventually”, “until” for temporal properties.

Planning/state transition logic also explicitly models time/steps.

## Event calculus / situation calculus

Classical AI developed formalisms for actions/change.

**Situation Calculus** represents situations as histories and fluents varying by situation.

**Event Calculus** represents events and intervals over which properties hold.

They address **frame problem**: specifying what stays unchanged when action affects only few facts.

## Frame problem

If robot moves cup from A to B, we want infer:

- cup location changed;
- wall color unchanged;
- robot serial number unchanged;
- thousands other facts unchanged.

Explicitly writing every non-change is impractical.

Planning STRIPS uses add/delete lists to handle frame assumptions operationally.

## Commonsense exception problem

Rule:

\[
Bird(x)\rightarrow Flies(x)
\]

fails for penguins.

Strict FOL rule means no exception unless modeled explicitly.

Default logic/non-monotonic reasoning allows “birds normally fly unless exception known”.

This demonstrates boundary between mathematical logic and commonsense reasoning.

## Knowledge incompleteness

From absence of:

```text
Owns(Alice,Car)
```

FOL does not derive:

```text
¬Owns(Alice,Car)
```

unless closed-world assumption/rule added.

This is critical when integrating databases with logic reasoners.

## FOL và Knowledge Graphs

Triple:

```text
(Alice, worksAt, CompanyX)
```

maps naturally to binary predicate:

\[
WorksAt(Alice,CompanyX)
\]

Ontology axioms add logical semantics.

Graph traversal alone is not full FOL reasoning; graph query semantics depend language/system.

## FOL và Natural Language

Natural language contains quantifiers, negation, relations and scope, so FOL is useful semantic representation.

Sentence:

> Every student read a book.

Can mean each student possibly different book:

\[
\forall x(Student(x)\rightarrow\exists y(Book(y)\land Read(x,y)))
\]

Natural language semantic parsing tries map text into logical/structured forms, but ambiguity/context make task hard.

## LLM to logic

LLM can translate natural-language requirements into logical constraints, then theorem prover/solver validates.

Architecture:

```text
Natural language
     ↓ LLM semantic parsing
FOL / Datalog / SMT-like constraints
     ↓ formal engine
verified answer / counterexample
```

Risk lies in translation correctness. Formal solver only proves the formula it receives, not that formula faithfully represents user intent.

## Mental Model

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

## Common Misconceptions

### “∀x P(x) means P is usually true”

No. Universal quantifier means every object in domain under interpretation satisfies P.

### “∃x means we know which x”

Not necessarily. It asserts at least one witness exists.

### “FOL can represent everything needed in AI”

It is expressive but awkward for uncertainty, defaults, time and computational tractability. Other formalisms complement it.

### “Formal proof guarantees real-world conclusion”

Proof guarantees conclusion follows from formal premises. If premises/modeling are wrong or incomplete, real-world claim may still fail.

## Knowledge Connection

First-Order Logic upgrades propositional reasoning from flat Boolean symbols to relational structures, creating bridge to ontologies, rule engines and Knowledge Graphs. Its limitations motivate [Probabilistic Reasoning](./04_probabilistic_reasoning.md) and non-monotonic/hybrid approaches.

Xem tiếp: [Inference and Reasoning](./03_inference_and_reasoning.md).