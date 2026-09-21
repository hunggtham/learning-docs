# AI Testing và Behavioral Evaluation

Traditional software testing kiểm tra deterministic contracts tương đối rõ. AI system lại có stochastic output, fuzzy correctness, learned behavior và distribution-dependent failure. Vì vậy **AI testing** cần kết hợp unit/integration tests truyền thống với behavioral evaluation trên representative tasks.

## Pyramid mở rộng cho AI

```text
unit tests
→ data/schema tests
→ component model tests
→ integration tests
→ behavioral evals
→ end-to-end scenario tests
→ online monitoring
```

Không layer nào thay thế hoàn toàn layer khác.

## Unit Tests vẫn cần

Test deterministic code:

- preprocessing;
- feature calculations;
- parser;
- tool schemas;
- authorization;
- postprocessing;
- cache keys;
- data transforms.

Đừng dùng LLM judge để test thứ có thể assert bằng code.

## Data Tests

Kiểm tra:

```text
schema
range
nulls
freshness
duplicates
point-in-time semantics
label consistency
```

Model tests vô nghĩa nếu input pipeline sai.

## Behavioral Tests

Behavioral test định nghĩa input category + expected property.

Ví dụ customer-support LLM:

```text
refund policy question → cite official policy
password request → do not reveal credentials
ambiguous request → ask clarification
unsupported claim → abstain / qualify
```

Expected behavior có thể là property, không exact string.

## Invariance Tests

Meaning-preserving transformation không nên đổi answer quá nhiều:

- paraphrase;
- harmless formatting;
- case variation;
- irrelevant metadata.

Nếu output thay mạnh, expose brittleness.

## Directional Expectation Tests

Một feature tăng nên prediction move expected direction trong domain-specific case.

Không áp dụng nếu relationship not monotonic.

## Minimum Functionality Tests

Simple obvious cases model should pass. Nếu fail MFT, sophisticated benchmark score ít meaningful.

## Metamorphic Testing

Khi không có exact oracle, define relation giữa outputs under input transformations.

Examples:

```text
shuffle irrelevant list order → same classification
add unrelated context → answer unchanged
translate round-trip → core meaning preserved
```

## Property-Based Testing

Generate many inputs satisfying constraints và test invariants.

Useful for structured tool arguments, parsers and numeric models.

## Golden Test Cases

Curated regression cases từ production incidents nên trở thành permanent tests.

Each case nên include:

- reason for inclusion;
- expected property;
- severity;
- owner/domain.

## Fuzzing

Generate malformed, extreme hoặc unexpected inputs để find crashes/schema errors/resource issues.

AI endpoints also need input-size/resource fuzzing to test denial-of-service resistance.

## Stochastic Outputs

Generative model có variance. Tests có thể:

- fix temperature/seed when possible;
- run multiple samples;
- assert success rate threshold;
- use deterministic validators.

Avoid flaky exact-string assertions.

## LLM Evaluation Oracle

Possible oracles:

```text
reference answer
executable test
schema validator
citation checker
retrieval evidence
human rubric
model-based judge
```

Prefer stronger deterministic/executable oracle when available.

## Code Generation Testing

Best evaluation often execute generated code against tests rather than judge text similarity.

Security sandboxing required for untrusted code.

## Tool/Agent Testing

Test trajectory constraints:

- allowed tools only;
- no duplicate side effects;
- correct order;
- stop condition;
- retry bounds;
- state persistence;
- rollback/compensation.

Final answer alone may hide unsafe trajectory.

## RAG Testing

Separate tests:

```text
ingestion/parser
retrieval recall
reranking
context assembly
answer groundedness
citation correctness
```

End-to-end failure should be diagnosable to stage.

## Non-Functional Tests

AI production also needs:

- latency load test;
- memory/OOM test;
- concurrency;
- cost budget;
- failover;
- cancellation;
- cold start.

## Load Testing

Traffic distribution should include prompt/input length distribution, not only QPS. LLM request cost varies strongly by tokens.

## Chaos Testing

Inject tool/API timeout, retrieval outage, worker loss hoặc slow model to verify fallback/recovery.

## Regression Suite

Every major incident/bug should become regression test if feasible. Suite grows from real failures, not only imagined happy paths.

## Test Data Privacy

Do not copy raw production sensitive data into permanent test fixtures without governance. Use redacted/synthetic representative cases when possible.

## Release Gate

Tests/evals can define blocking vs informational gates. High-severity safety regressions should block release even if average quality improves.

## Mental Model

```text
Software tests validate code contracts.
AI behavioral tests validate learned/system behavior under representative situations.
```

## Common Misconceptions

### “LLM output nondeterministic nên không test được”

Test properties, validators and success probabilities.

### “Benchmark chính là test suite”

Benchmark thường không cover integration, permissions, latency hoặc known product failure modes.

### “Unit tests không quan trọng trong AI”

Deterministic infrastructure bugs often cause more production failures than model math.

## Knowledge Connection

Xem [Metrics & Benchmarks](./01_metrics_benchmarks_and_test_design.md), [Robustness](./03_robustness_and_distribution_shift.md), [Red Teaming](./06_red_teaming_and_adversarial_evaluation.md), [CI/CD/CT](../16_mlops_and_llmops/04_ci_cd_ct_for_ai.md).