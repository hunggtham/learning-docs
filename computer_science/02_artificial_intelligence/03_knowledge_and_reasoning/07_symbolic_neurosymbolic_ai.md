# Symbolic AI và Neuro-Symbolic AI

Artificial Intelligence thường được kể như một cuộc chuyển giao: **Symbolic AI thất bại → Machine Learning thắng → Deep Learning thay thế mọi thứ cũ**. Câu chuyện này quá đơn giản. Symbolic và neural approaches có strengths khác nhau; nhiều reliable systems hiện đại kết hợp learned perception/language với explicit tools, constraints, search, databases và formal verification.

**Symbolic AI (기호주의 인공지능)** biểu diễn knowledge bằng symbols, rules và structured relations. **Neural AI** học distributed representations và functions từ data. **Neuro-Symbolic AI (신경-기호 인공지능)** là umbrella term cho approaches cố kết hợp hai families, nhưng không có một architecture duy nhất mang tên này.

Xem trước: [Knowledge Representation](./00_knowledge_representation.md), [Inference and Reasoning](./03_inference_and_reasoning.md), và [Knowledge Graphs](./06_knowledge_graphs.md).

## Symbolic AI bắt đầu từ đâu?

Symbolic systems giả định nhiều aspects của intelligence có thể modeled bằng:

```text
symbols
+ rules
+ search/inference
```

Examples:

- theorem prover;
- expert system;
- STRIPS planner;
- SAT/SMT solver;
- rule engine;
- ontology reasoner.

A symbol như `Patient42`, predicate `HasSymptom(x,Fever)` và rule `A∧B→C` có explicit semantics do designer/domain define.

## Strength của symbolic systems

### Explicitness

Rule có thể inspect:

```text
HighRisk(x) ∧ MissingKYC(x) → ManualReview(x)
```

System designer biết relation nào được encoded.

### Verification

Formal proof/solver có thể guarantee candidate satisfies constraints relative to model.

### Compositional structure

Symbols và relations combine systematically. Rule applies to new entities without retraining if facts fit schema.

### Data efficiency

If domain rules known, system không cần thousands examples để rediscover them statistically.

## Weakness của symbolic systems

### Knowledge acquisition bottleneck

Human experts phải encode huge number rules/facts.

### Brittleness

Rule written for clean symbolic input may fail when real data noisy/ambiguous.

### Perception gap

Images, audio và natural language do not arrive as clean symbols.

### Commonsense scale

Explicitly encoding every exception/context is difficult.

These weaknesses helped drive statistical ML and Deep Learning.

## Neural systems start from learning

Neural model:

\[
f_\theta(x)
\]

learns parameters from data using optimization.

Instead of manually define features/rules, representation can be learned end-to-end.

Strengths:

- perception;
- language;
- similarity/generalization;
- high-dimensional noisy data;
- scalable learning from massive datasets.

Weaknesses:

- opaque internal representations;
- hard guarantees difficult;
- brittle OOD behavior;
- exact constraint satisfaction not automatic;
- factual knowledge hard to update selectively.

## Symbolic vs neural is not binary

Many systems already hybrid without using label “neuro-symbolic”.

Example search engine:

```text
neural embedding retrieval
+ boolean filters
+ database indexes
+ ranking rules
```

Example coding agent:

```text
LLM proposes code
+ compiler/type checker
+ tests
+ shell/git tools
```

Compiler is symbolic/formal component providing exact feedback.

## A useful decomposition

Instead of asking “symbolic or neural?”, ask which component requires which property:

| Need | Often suitable mechanism |
|---|---|
| Perception from raw pixels/audio | neural model |
| Semantic similarity | embeddings |
| Hard business constraint | rule/solver |
| Exact arithmetic | calculator/runtime |
| Relational factual store | database/KG |
| Flexible language interface | LLM |
| Formal proof | theorem prover |
| Combinatorial planning | search/solver + learned heuristic |

System architecture can compose mechanisms.

## Neural perception → symbolic reasoning

Classic pattern:

```text
image
 ↓ neural detector
objects + attributes
 ↓ symbolic rules/planner
reasoning/action
```

Risk: perception errors become wrong symbols. Downstream reasoner may be perfectly logical about incorrect detections.

Need uncertainty/confidence at interface.

## Symbolic structure guiding neural learning

Rules/constraints can shape training objective.

Suppose known constraint:

\[
A(x)\rightarrow B(x)
\]

One can add penalty when neural predictions violate implication.

This creates **soft constraint** rather than guaranteed symbolic enforcement unless final output checked separately.

## Differentiable logic

Some methods replace Boolean truth with continuous values `[0,1]` and logical operators with differentiable relaxations.

Example fuzzy-style conjunction may use:

\[
T(a,b)=ab
\]

or other t-norms.

Then logical consistency becomes differentiable loss.

Benefits: train by gradient.

Limitation: relaxed truth semantics differ from classical logic; satisfaction may be approximate, not proof.

## Logic Tensor Networks

Logic Tensor Network-like approaches ground predicates into neural functions and translate logical formulas into differentiable satisfaction objectives.

Mental model:

```text
symbolic formula
   ↓ differentiable relaxation
training loss
   ↓
neural parameters
```

This integrates prior knowledge into learning but does not automatically inherit classical theorem-proving guarantees.

## Neural theorem proving

A learned model can guide proof search:

```text
current proof state
 ↓ neural model ranks lemmas/tactics
formal prover executes step
 ↓
valid next proof state or failure
```

Correctness comes from formal kernel; neural network improves search efficiency.

This is one of clearest neuro-symbolic patterns because roles are separated cleanly.

## Learned heuristic + symbolic search

Search algorithm needs heuristic `h(s)` or policy ordering. Neural network predicts promising actions/value, while symbolic state transition remains exact.

AlphaZero-like game systems:

```text
neural policy/value
+ Monte Carlo Tree Search
+ exact game rules
```

Again learning and symbolic/search computation complement each other.

## LLM + SAT/SMT solver

Natural-language requirement:

> Schedule 5 workers, no overlapping shifts, Alice unavailable Tuesday...

Architecture:

```text
natural language
 ↓ LLM extracts variables/constraints
SMT/CP-SAT model
 ↓ solver
valid assignment / unsat
 ↓ LLM explains
```

The solver guarantees constraints encoded. The weak link is semantic translation from user text to constraints, so system should expose/check extracted model.

## LLM + code execution

For arithmetic/data analysis:

```text
question
 ↓ LLM writes code/query
runtime executes exact computation
 ↓ actual result
LLM explains result
```

This is a practical hybrid architecture. LLM is not asked to simulate calculator internally when deterministic executor exists.

## LLM + Knowledge Graph

LLM can perform entity linking/query generation and verbalization; KG stores explicit facts/relations.

```text
user question
 ↓ semantic parse/entity link
structured graph query
 ↓ KG
facts + provenance
 ↓ LLM
answer
```

This enables fresh/updatable knowledge and auditability.

But graph coverage may be incomplete; LLM must not infer absence as false unless schema uses closed-world semantics.

## RAG as hybrid AI?

RAG combines neural retrieval/generation with external symbolic-ish text store/index, but calling every RAG system “neuro-symbolic” stretches term.

Plain vector RAG has no explicit symbolic reasoning. KG-RAG or solver-backed RAG is more clearly hybrid.

Use architecture description rather than label hype.

## Program synthesis + verification

Neural model proposes program; tests/static analysis/formal verifier checks.

Loop:

```text
propose
 ↓
execute/verify
 ↓ error/counterexample
repair
 ↺
```

Counterexample provides high-information feedback. This pattern is central to reliable coding agents.

## Constraint decoding

Instead of generate arbitrary tokens then reject, decoder can enforce grammar/schema during generation.

Examples:

- JSON grammar;
- SQL grammar;
- finite-state constraints;
- regex/CFG-guided decoding.

This guarantees syntactic structure, not necessarily semantic correctness.

`{"age": -500}` can be valid JSON but invalid domain value.

Semantic validation remains separate.

## Typed tools

Function calling schema provides symbolic interface:

```text
search(query: string, top_k: int)
transfer(amount: decimal, account_id: string)
```

Type/schema reduces action space and allows validation.

Tool implementation then interacts with deterministic external system.

LLM chooses action; tool enforces semantics/permissions.

## Separation of proposer and verifier

A robust pattern across hybrid AI:

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

- LLM ↔ compiler;
- planner ↔ constraint validator;
- theorem model ↔ proof kernel;
- code model ↔ tests;
- extraction model ↔ schema validator.

This architecture reduces need for one model to be both creative and perfectly reliable.

## Verification is only relative to specification

A solver can certify:

```text
schedule satisfies encoded constraints
```

It cannot certify:

```text
encoded constraints perfectly reflect stakeholder intent
```

This **specification gap** is central.

Formal verification moves uncertainty from execution correctness toward modeling correctness; it does not eliminate all uncertainty.

## Soft vs hard constraints

Neural loss penalty:

\[
L=L_{task}+\lambda L_{constraint}
\]

makes violations costly but possible.

Hard solver constraint:

\[
g(x)\le0
\]

rejects invalid solutions entirely.

Choose based requirement. Safety-critical invariant usually should not rely only on soft training penalty if deterministic enforcement possible.

## Neuro-symbolic representation learning

Some methods learn embeddings while preserving known relational structure.

Knowledge Graph embedding trains vectors from triples; graph neural networks propagate typed neighborhood information.

These are hybrid in a broad sense, though not necessarily performing formal symbolic inference.

The term should be used carefully.

## System 1 / System 2 analogy

People sometimes call neural model “System 1” fast intuition and symbolic search “System 2” slow reasoning, borrowing psychology terminology.

This can be a useful metaphor but is not literal cognitive equivalence. Engineering architecture should be described concretely: proposal network, search, verifier, memory, tool execution.

## When symbolic rules are a poor fit

Do not force symbolic modeling when:

- category boundary inherently fuzzy;
- raw input high-dimensional;
- rules impossible to enumerate;
- environment rapidly changes;
- semantics learned from examples matter more than formal constraints.

Image recognition from pixels is classic example where Deep Learning outperforms handcrafted symbolic vision pipelines.

## When neural models are a poor fit

Do not ask neural network alone for:

- exact tax calculation when formula known;
- hard access-control rule;
- deterministic database join;
- cryptographic verification;
- proof checker;
- constraint-satisfaction guarantee.

Use deterministic tools and let model orchestrate when language flexibility needed.

## Error composition

Hybrid system has multiple failure probabilities:

```text
semantic parse error
+ retrieval error
+ solver/model assumption error
+ tool execution error
+ explanation error
```

Adding verifier does not guarantee entire pipeline if upstream/downstream components can mis-handle results.

Evaluation must be end-to-end plus component-level.

## Interface design matters

Neural-symbolic boundary should expose structured state, not ambiguous prose where possible.

Good:

```json
{
  "customer_id": "C123",
  "risk_score": 0.82,
  "kyc_status": "MISSING"
}
```

Rule engine can consume reliably.

Free-form sentence parsing at every step adds unnecessary uncertainty.

## Confidence and abstention

If neural parser uncertain, system may abstain/ask clarification instead of feed dubious symbols into strict solver.

A perfect solver on wrong parse can create confidently wrong outcome.

Hybrid systems need uncertainty-aware handoff.

## Neuro-symbolic benchmark question

When paper claims neuro-symbolic improvement, ask:

- what symbolic knowledge is provided?
- what is learned?
- where are guarantees?
- is logic hard or differentiable soft?
- how is noise handled?
- does system generalize compositionally or just fit benchmark?

Architecture label alone does not answer quality.

## Mental Model

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

## Common Misconceptions

### “Symbolic AI đã chết”

Formal solvers, rules, databases, planners and compilers remain essential; modern AI often embeds them as tools/components.

### “Neuro-symbolic automatically gives neural flexibility + symbolic guarantee”

Only if architecture truly has a sound verifier/enforcement layer. Differentiable logic penalties are not same as hard proof.

### “RAG = neuro-symbolic AI”

Plain vector RAG is hybrid retrieval/generation but does not necessarily include symbolic representation/reasoning.

### “Formal verifier makes system correct”

It guarantees properties encoded in specification, not correctness of natural-language interpretation or real-world assumptions.

## Knowledge Connection

Neuro-symbolic design closes the Knowledge Representation layer and prepares the transition to Machine Learning. The central lesson is architectural: learned models are powerful at perception, language and heuristic proposal; symbolic/deterministic systems are powerful at explicit state, constraints, exact computation and verification.

Later sections on RAG, Agents and AI Engineering will reuse this pattern repeatedly.