# Propositional Logic cho Artificial Intelligence

**Propositional Logic (명제 논리 / logic mệnh đề)** là một formal language để biểu diễn statements có truth value và suy luận từ chúng bằng rules chính xác. Nó là hệ logic đơn giản hơn First-Order Logic nhưng cực kỳ quan trọng vì cho ta vocabulary về syntax, semantics, entailment, proof, satisfiability và model checking.

Trong AI, Propositional Logic xuất hiện trong rule systems, SAT solving, planning encodings, verification và constraint reasoning. Học nó không phải để viết mọi knowledge thành `P ∧ Q`; mục tiêu là hiểu formal reasoning khác với statistical pattern matching ở đâu.

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

Propositional Logic treats `P` như atomic symbol; nó không nhìn inside structure “raining”.

## Connectives

Common logical connectives:

| Symbol | English | 한국어 | Meaning |
|---|---|---|---|
| `¬P` | NOT | 부정 | không P |
| `P ∧ Q` | AND | 논리곱 / 그리고 | P và Q |
| `P ∨ Q` | OR | 논리합 / 또는 | P hoặc Q inclusive |
| `P → Q` | implication | 함의 | nếu P thì Q |
| `P ↔ Q` | biconditional | 동치 | P iff Q |

`∨` mặc định inclusive OR: true khi một hoặc cả hai true.

## Truth table

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

It only forbids case P true and Q false.

Natural-language “if” may carry causal/temporal meaning not captured by material implication.

## Syntax vs semantics

**Syntax** defines well-formed formulas.

Example:

\[
(P\land Q)\rightarrow R
\]

**Semantics** defines truth under an interpretation/model assigning truth values to symbols.

This distinction is fundamental:

```text
syntax    = expression structure
semantics = what makes expression true/false
```

LLM can generate syntactically valid-looking formula while semantic mapping to domain may still be wrong.

## Model

A model `M` is assignment of truth values to propositions.

If:

```text
P=true
Q=false
```

then `M` satisfies `P∨Q` but not `P∧Q`.

Notation:

\[
M\models\alpha
\]

means model `M` satisfies formula `α`.

## Satisfiable, valid và unsatisfiable

Formula is **satisfiable** if at least one model makes it true.

**Valid / tautology** if every model makes it true.

Example:

\[
P\lor\neg P
\]

always true.

**Unsatisfiable / contradiction** if no model makes true:

\[
P\land\neg P
\]

These concepts power SAT solving and proof by contradiction.

## Entailment

Knowledge base `KB` entails `α`:

\[
KB\models\alpha
\]

if every model satisfying `KB` also satisfies `α`.

Important:

> Entailment is semantic necessity, not merely that α “sounds plausible”.

Example:

\[
KB=\{P\rightarrow Q, P\}
\]

then:

\[
KB\models Q
\]

## Inference

Inference procedure derives formula syntactically:

\[
KB\vdash\alpha
\]

Distinguish:

```text
⊨ semantic entailment
⊢ syntactic derivability/proof
```

A proof system is **sound** if it derives only entailed statements.

It is **complete** if every entailed statement can in principle be derived.

These terms are about proof systems, not ML accuracy.

## Modus Ponens

Rule:

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

This is valid regardless domain meaning.

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

SAT solving uses this structure heavily.

## Resolution

Resolution rule:

\[
(P\lor A),\quad(\neg P\lor B)
\]

infer:

\[
A\lor B
\]

If repeated resolution derives empty clause `□`, contradiction found.

To prove `KB⊨α`, add `¬α` to KB and show unsatisfiable by resolution.

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

Thus assumptions + `¬Q` inconsistent, so Q entailed.

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

Horn logic supports efficient forward/backward chaining and underlies rule systems/logic programming fragments.

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

## Backward chaining

Start from query/goal and ask what premises would prove it.

To prove `D`:

```text
Need C
To prove C need A and B
Check facts A,B
```

Backward chaining is **goal-driven**.

Prolog-style reasoning uses backward chaining with unification at First-Order level.

## SAT problem

SAT asks:

> Is there an assignment to Boolean variables making formula true?

SAT is NP-complete, yet modern solvers handle enormous structured instances.

Applications:

- hardware verification;
- planning;
- scheduling/configuration;
- dependency resolution;
- theorem proving;
- software analysis.

## DPLL

DPLL extends backtracking SAT with:

- unit propagation;
- pure literal elimination;
- branching.

Modern CDCL solvers build on related foundation with conflict learning and non-chronological backtracking.

## Unit propagation

Clause:

\[
A\lor B\lor C
\]

If `A=false` and `B=false`, then `C=true` forced.

Propagate forced assignments before branching.

This is same “reason before search” principle seen in CSP.

## Conflict-Driven Clause Learning

When assignments cause conflict, analyze implication graph and learn clause preventing same reason for conflict.

CDCL loop conceptually:

```text
propagate
  ↓
branch
  ↓
conflict?
  ├─ no → continue
  └─ yes → analyze → learn clause → backjump
```

Learned clause is logically implied, so solver becomes smarter without sacrificing correctness.

## Knowledge-base consistency

If KB contains:

\[
P
\]

and:

\[
\neg P
\]

classical logic KB inconsistent.

Under principle of explosion, from contradiction arbitrary formula can be derived in classical logic.

Real knowledge bases may contain conflicts, motivating paraconsistent logics, provenance-aware reasoning or explicit conflict-resolution policies.

## Closed-world reasoning

Propositional logic itself does not say absent facts false. Closed-world assumption is extra semantic policy.

Rule engine may implement **negation as failure**:

```text
if cannot prove P, assume not P
```

This differs from classical logical negation.

Confusing them causes subtle bugs.

## Logic và software conditions

Boolean logic underlies code:

```java
if (authenticated && !locked) {
    allow();
}
```

But program state/time/side effects make full software semantics richer than propositional formulas.

Formal verification often translates program properties into SAT/SMT constraints.

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

requires arithmetic theory, not pure Boolean atoms alone unless encoded.

SMT is highly relevant for program verification and solver-backed agents.

## Logic vs probability

Classical logic:

```text
P true / false
```

Probability:

```text
P(P)=0.7
```

Logic captures structural certainty; probability captures uncertainty.

A rule `Smoke→Fire` in strict logic means every smoke case implies fire. Real-world relation is probabilistic, so forcing it into strict implication is wrong modeling.

Representation must match domain semantics.

## Logic vs LLM reasoning

LLM can produce logically valid sequences but next-token generation does not guarantee sound proof.

Hybrid approach:

```text
LLM proposes theorem/proof steps
        ↓
formal logic engine checks validity
        ↓
accept / reject / repair
```

This pattern combines flexible language reasoning with symbolic verification.

## Planning as SAT

Bounded planning can introduce Boolean variables:

```text
ActionA_t
AtRobotRoom1_t
AtRobotRoom2_t
```

Constraints encode action preconditions, effects and exactly-one conditions.

SAT solver finding assignment corresponds to plan.

This illustrates representational reduction: planning becomes satisfiability.

## Mental Model

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

## Common Misconceptions

### “P→Q means P causes Q”

Material implication encodes truth condition, not causality.

### “If Q is true and P→Q, then P must be true”

Affirming consequent is invalid.

### “Not known means false”

Only under explicit closed-world/negation-as-failure assumptions.

### “SAT is NP-complete nên solver practical không dùng được”

Worst-case hardness does not prevent solving many large structured instances efficiently.

## Knowledge Connection

Propositional Logic connects KR with CSP/SAT, planning and formal verification. It introduces the semantic/syntactic distinction needed before First-Order Logic and gives a baseline for understanding why probabilistic/neural reasoning offer different trade-offs.

Xem tiếp: [First-Order Logic](./02_first_order_logic.md) và [Inference and Reasoning](./03_inference_and_reasoning.md).