# Testing, verification và debugging

Software correctness không thể dựa vào cảm giác “code nhìn đúng”. Ta cần nhiều techniques với strengths khác nhau: type checking, static analysis, unit/property/integration tests, formal verification, runtime assertions, observability và systematic debugging.

## Test là sample, specification là property

Example-based test chọn input và expected output cụ thể. Nó tốt cho known cases/regressions nhưng không cover infinite domain.

Property-based testing generate many inputs và check invariant: sorting output ordered + permutation of input; serializer roundtrip; parser never crash on valid grammar. Property buộc ta viết specification rõ hơn.

Fuzzing generate/mutate unexpected inputs để tìm crash/security bugs, especially parsers and native code.

## Unit, integration, system

Unit test isolate small component, nhanh và precise diagnosis. Integration test kiểm tra boundaries thật như DB/network/serialization. End-to-end test cover whole flow nhưng chậm/flaky và khó localize failure.

Testing pyramid không phải law; optimal mix phụ thuộc architecture/risk. Contract tests hữu ích cho service APIs.

## Determinism và flaky tests

Flaky test thường do hidden inputs: clock, random seed, thread scheduling, shared state, network, eventual consistency. Inject clock/random source, isolate state, await conditions instead of fixed sleeps, control concurrency where possible.

A flaky test is not merely annoyance; it erodes trust in signal.

## Static analysis

Compiler warnings, linters, dataflow analysis, abstract interpretation và symbolic execution tìm classes bugs without running all paths concretely. They trade precision vs scalability, potentially false positives/negatives.

Undecidability explains why universal perfect analyzer for arbitrary programs impossible; tools solve restricted properties/models.

## Formal methods

Hoare logic uses `{P} C {Q}` precondition/program/postcondition. Model checking explores finite state model. SMT solvers prove constraints. Proof assistants verify machine-checkable proofs.

Formal methods are especially valuable for protocols, crypto, kernels, safety-critical code, but cost/model fidelity matter. Proving wrong model perfectly still leaves real system bugs.

## Debugging as hypothesis testing

Good debugging loop:

1. make failure reproducible/observable;
2. bound where divergence from expected first occurs;
3. form hypothesis tied to mechanism;
4. gather discriminating evidence;
5. change one relevant variable or inspect state;
6. fix root cause and add regression guard.

Random code changes are search without model.

## Logs, traces, metrics and debuggers

Logs record discrete events/context; metrics aggregate numeric time series; traces connect causal request path across components; debugger inspects execution state. Core dumps/profile captures freeze evidence after failure/performance issue.

Each view loses different information. High-cardinality IDs belong naturally in traces/logs more than naive metric labels.

## Reproduction and minimization

Reduce failing input/environment to smallest case. Delta debugging/minimal reproducer removes irrelevant variables and often exposes violated invariant.

For concurrency, deterministic record/replay or stress scheduling can help; for distributed failures, fault injection/network simulation reveals assumptions.

## Tests and refactoring

Tests provide behavioral contract during refactor. But over-mocking implementation details makes tests brittle and blocks internal changes. Test observable contract/invariants, use mocks at meaningful boundaries.

## Mental Model

> Confidence comes from **overlapping evidence**. Types prove one class, tests sample behaviors, static analysis approximates paths, formal proof covers modeled properties, production observability checks reality.

## Common Misconceptions

**“100% code coverage = correct.”** Coverage only says code executed, not assertions meaningful or state space covered.

**“Unit tests should mock everything external.”** Excessive mocks test implementation choreography, not integration contracts.

**“Debugger is first tool for every issue.”** Logs/traces/profiles/reproducers may locate distributed/performance bugs better.

## Kết nối

[Computability limits](../00_computation_information/04_computability_and_limits.md) explain analysis boundaries. [Algorithm invariants](../01_algorithms_data_structures/00_algorithmic_thinking_and_correctness.md) inspire properties. [Observability/reliability](./05_fault_tolerance_observability_and_reliability.md) extends evidence to production.
