# Inference và Reasoning trong Artificial Intelligence

Knowledge Representation chỉ hữu ích khi system có thể tạo ra conclusion mới hoặc quyết định dựa trên knowledge. **Inference (추론 / suy luận)** là quá trình derive information từ premises theo một mechanism; **reasoning** rộng hơn, bao gồm chọn assumptions, combine evidence, resolve uncertainty, search proof, reason về causes/actions và sometimes revise beliefs.

Không có một “reasoning algorithm” universal. Deduction, induction, abduction, default reasoning và probabilistic inference trả lời different questions và có different guarantees.

Xem trước: [Propositional Logic](./01_propositional_logic.md) và [First-Order Logic](./02_first_order_logic.md).

## Deduction

Deductive reasoning:

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

If premises true and inference valid, conclusion must be true.

Deduction is truth-preserving relative to formal semantics.

## Induction

Inductive reasoning:

```text
observed examples
        ↓
general pattern/hypothesis
```

Example: observe many transactions and learn classifier predicting fraud.

Conclusion not guaranteed. New examples can falsify pattern.

Machine Learning is largely inductive: finite data → model expected to generalize.

Statistics provides framework to quantify uncertainty/generalization.

## Abduction

Abduction seeks plausible explanation for observation.

```text
Rule: Fire → Smoke
Observe: Smoke
Possible explanation: Fire
```

This is not deductively valid because other causes can produce smoke.

Medical diagnosis often abductive: symptoms → candidate causes.

Abduction generates hypotheses; probability/causal knowledge ranks them.

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

Inference procedure is **sound (건전성)** if:

\[
KB\vdash\alpha\Rightarrow KB\models\alpha
\]

Everything it proves is semantically entailed.

A sound theorem prover does not invent invalid proof conclusions relative to formal system.

## Completeness

Procedure is **complete (완전성)** if:

\[
KB\models\alpha\Rightarrow KB\vdash\alpha
\]

Every semantic consequence can in principle be proved.

Soundness and completeness do not imply efficiency. Search for proof can be enormous or non-terminating in expressive logics.

## Correctness vs tractability

AI reasoning design balances:

```text
expressiveness
soundness/completeness
runtime
memory
maintainability
```

A restricted rule language may be preferable to full FOL because predictable inference matters in production.

## Forward chaining

Data-driven reasoning:

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

Derive badge and access.

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

Efficient when query narrow compared with all possible consequences.

## Memoization

Backward reasoning can repeatedly solve same subgoal. Cache result:

```text
subgoal → proven/failed/answers
```

Tabling in logic programming avoids loops/repeated computation and can improve completeness properties for certain programs.

This is same dynamic-programming idea across AI.

## Fixed-point reasoning

Datalog-style rules can be evaluated until no new facts:

\[
T(K)=K\cup\{\text{new consequences}\}
\]

Repeatedly:

\[
K_{i+1}=T(K_i)
\]

until:

\[
K_{i+1}=K_i
\]

This least fixed point defines semantics for many positive recursive rule programs.

## Rule conflict

Real rule bases may derive conflicting conclusions.

Example:

```text
PremiumCustomer(x) → Approve(x)
FraudFlag(x) → Reject(x)
```

Alice satisfies both.

Need conflict policy:

- priority;
- specificity;
- deny-overrides;
- provenance/trust;
- non-monotonic logic.

Formal rule semantics should specify this explicitly.

## Monotonic reasoning

In monotonic logic:

\[
KB\models\alpha
\]

then adding more premises keeps entailment:

\[
KB\cup\{\beta\}\models\alpha
\]

Classical logic monotonic.

Real-world default reasoning often not.

## Non-monotonic reasoning

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

Non-monotonic reasoning models revisable conclusions.

## Default logic

Default rule conceptually:

```text
If Bird(x), and no evidence abnormal,
assume Flies(x)
```

This differs from strict implication.

Many business rules implicitly use defaults; encoding them as strict FOL creates exceptions problem.

## Circumscription

Circumscription minimizes extension of abnormality predicates.

Example:

```text
Bird(x) ∧ ¬Abnormal(x) → Flies(x)
```

Assume as few objects abnormal as possible consistent with knowledge.

It formalizes “things are normal unless evidence otherwise”.

## Closed-world inference

Database-like systems often infer false from inability to prove:

```text
not Known(P) → assume ¬P
```

This is safe only when knowledge base intended complete for predicate.

For medical records, absence of diagnosis may not mean patient does not have disease.

Closed-world policy should be predicate/domain-specific, not universal habit.

## Truth maintenance

When facts/rules change, derived conclusions may need retract/update.

Truth Maintenance System tracks justifications/dependencies:

```text
Fact A + Rule R → Conclusion C
```

If A removed, C may need removal unless another justification exists.

Modern data pipelines similarly need lineage/incremental recomputation.

## Explanation

Symbolic inference can produce proof trace:

```text
Alice can enter because:
Employee(Alice)
Employee → HasBadge
HasBadge → CanEnterLobby
```

This is stronger than post-hoc “feature importance” because explanation is actual derivation path under rule system.

But explanation only as good as rules/premises.

## Reasoning under inconsistent knowledge

Classical logic with contradiction can explode.

**Paraconsistent logic** allows contradictions without deriving arbitrary everything.

Production knowledge integration may need conflict-tolerant approaches because sources disagree.

Another engineering approach: preserve provenance and avoid merging conflicts into single unquestioned truth.

## Reasoning under uncertainty

Strict rule:

\[
Symptom(x)\rightarrow Disease(x)
\]

is often unrealistic.

Probabilistic reasoning assigns:

\[
P(Disease\mid Symptom)
\]

or factor graph/Bayesian network.

This changes entailment from binary proof to posterior belief computation.

See [Probabilistic Reasoning](./04_probabilistic_reasoning.md).

## Causal reasoning

Statistical association:

\[
P(Y\mid X)
\]

Causal reasoning asks:

\[
P(Y\mid do(X=x))
\]

Intervention differs observation.

A rule like `Rain→WetRoad` may encode causal relation, but material implication alone does not.

Causal graphs and structural causal models explicitly represent mechanisms/interventions.

## Counterfactual reasoning

Counterfactual:

> What would have happened if action A had not occurred?

Requires model of alternate world sharing background factors, not just conditional probability.

Counterfactuals matter for explanation, policy analysis and credit assignment.

## Case-based reasoning

Instead of general rules, retrieve similar past cases and adapt solution.

Workflow:

```text
retrieve similar case
reuse solution
revise for new context
retain new experience
```

This is ancestor-like idea to retrieval-based systems, though modern RAG usually retrieves text/context rather than formal case adaptation.

## Analogical reasoning

Map relational structure from source domain to target domain.

Example electrical circuit analogy to water flow.

Useful for learning/explanation but analogy can mislead when structural mapping breaks.

LLMs are good at linguistic analogy generation but need verification for technical transfer.

## Commonsense reasoning

Commonsense involves defaults, physical constraints, social expectations and temporal knowledge.

Challenges:

- enormous breadth;
- exceptions;
- context dependence;
- unstated assumptions;
- incomplete knowledge.

Pure symbolic encoding difficult; pure statistical model can be inconsistent. Hybrid approaches remain active research area.

## Multi-step reasoning as search

Proof reasoning can be modeled as search:

```text
state = current facts/goals
operator = inference rule
successor = new derived statement/subgoal
objective = proof/counterexample
```

Heuristic theorem proving prioritizes promising clauses.

This connects Knowledge Reasoning back to [Heuristic Search](../02_search_reasoning_and_planning/02_heuristic_search.md).

## Proof search complexity

Even if each inference rule simple, number possible derivations explodes.

Reasoning system needs:

- indexing;
- rule ordering;
- subsumption;
- memoization;
- pruning;
- heuristics.

Formal correctness does not imply computational practicality.

## Deductive databases

Datalog + relational facts enables recursive queries.

Transitive closure example:

```text
Reach(x,y) :- Edge(x,y).
Reach(x,z) :- Edge(x,y), Reach(y,z).
```

This computes graph reachability through logical rules.

Databases and logic are deeply connected; query optimizer is a reasoning/planning engine over execution alternatives.

## Inference in Knowledge Graphs

Rules:

```text
parentOf(x,y) ∧ parentOf(y,z)
→ grandparentOf(x,z)
```

Ontology inference:

```text
Doctor subClassOf MedicalProfessional
Alice type Doctor
→ Alice type MedicalProfessional
```

Embedding-based KG completion instead predicts likely missing edges statistically. One gives logical entailment, other probabilistic score.

## Neural theorem proving

Neural model can score/select proof steps while symbolic kernel verifies each step.

Advantages:

```text
neural → flexible heuristic over huge search
symbolic → correctness guarantee of accepted proof
```

This is canonical neuro-symbolic architecture.

## LLM reasoning và verification

LLM-generated chain of thought may be fluent but invalid.

Reliable architecture can externalize verifiable intermediate artifact:

```text
LLM proposes SQL / code / proof / plan
      ↓
parser/type checker/solver executes or verifies
      ↓
feedback to model
      ↓
repair
```

The verifier should check domain property, not just text style.

## Self-consistency

Generate multiple reasoning paths and select majority/final answer can improve some tasks statistically.

But agreement is not proof. Many samples can share same systematic error.

Self-consistency is an inference-time sampling strategy, not formal logical consistency guarantee.

## Chain-of-thought vs formal derivation

Natural-language reasoning:

- flexible;
- readable;
- ambiguous;
- may omit steps.

Formal derivation:

- precise syntax;
- checkable;
- domain-limited;
- potentially expensive to construct.

Modern systems can use natural language for proposal and formal representation for verification.

## Reasoning trace provenance

For enterprise AI, useful output may include:

```text
answer
supporting sources
rules used
calculations/tool outputs
uncertainty
```

This is more auditable than opaque final answer.

Provenance should reflect actual process, not fabricated explanation.

## Mental Model

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

## Common Misconceptions

### “Reasoning = deduction”

Deduction chỉ một family. Real AI uses induction, abduction, probabilistic and decision reasoning.

### “Formal proof means premise is true”

Proof only guarantees relation from premises; source/model validity separate.

### “LLM explanation is proof of its answer”

Generated rationale can be post-hoc or erroneous. Independent verification matters.

### “More rules always improve reasoner”

More rules can create conflicts, cycles and explosion. Knowledge engineering quality matters.

## Knowledge Connection

Inference is where KR becomes active. It connects Logic to Search, Probability, Causal Reasoning and modern tool-backed LLM systems. Later the Agent section will reuse the same architecture: proposal → environment/tool verification → state update → replanning.

Xem tiếp: [Probabilistic Reasoning](./04_probabilistic_reasoning.md).