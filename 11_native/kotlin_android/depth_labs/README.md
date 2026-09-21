# Kotlin + Android Depth Labs

`depth_labs/` là tầng đọc sâu nằm sau các file chính, `deep_dive/` và Production Casebook. Mục tiêu của thư mục này không phải mở thêm domain Android mới, mà **đào sâu các chủ đề đã có tới mức có thể reasoning về correctness khi production không chạy theo happy path**.

Nếu Production Casebook trả lời “các subsystem ghép lại như thế nào?”, Depth Labs trả lời “tại sao thiết kế đó vẫn đúng khi thứ tự execution thay đổi, có race, process chết, request timeout sau remote commit, state bị stale, release bị rollback hoặc SDK chạy trong app consumer khác?”.

## Thứ tự đọc

1. [`01_architecture_invariants_boundary_reasoning.md`](01_architecture_invariants_boundary_reasoning.md) — bắt đầu từ invariant, state ownership, source of truth, transaction boundary, stale snapshot, ambiguous outcome, navigation identity và architecture timeline.
2. [`02_offline_sync_consistency_race_conditions.md`](02_offline_sync_consistency_race_conditions.md) — consistency model, durable outbox, idempotency, retry/jitter, ordering, queue compaction, version/conflict, tombstone, sync cursor, account isolation và failure injection.
3. [`03_coroutine_flow_concurrency_failure_semantics.md`](03_coroutine_flow_concurrency_failure_semantics.md) — Job tree, structured concurrency, cancellation, dispatcher, Mutex/actor, cold/hot Flow, state/event distinction, backpressure, callbackFlow, stale-request race và deterministic coroutine test.
4. [`04_compose_runtime_state_performance_semantics.md`](04_compose_runtime_state_performance_semantics.md) — Snapshot state, identity, effect lifetime, composition/layout/draw invalidation, stability, modifier order, custom layout/draw, semantics/accessibility và evidence-based performance optimization.
5. [`05_testing_reliability_observability_failure_injection.md`](05_testing_reliability_observability_failure_injection.md) — invariant-based testing, fake/mock fidelity, migration/rollback test, race/failure injection, process death, Macrobenchmark, SLI/SLO, telemetry, staged rollout và incident feedback loop.
6. [`06_build_compatibility_startup_release_forensics.md`](06_build_compatibility_startup_release_forensics.md) — Gradle/variant/manifest/resource merge, generated code, D8/R8, signing, API-level compatibility, SDK Extensions, OEM/WebView variation, cold-start critical path và release artifact forensics.
7. [`07_sdk_native_boundary_api_evolution_consumer_safety.md`](07_sdk_native_boundary_api_evolution_consumer_safety.md) — public API/ABI, dependency leakage, Java/Kotlin interop, SDK initialization/thread/error contract, consumer R8, JNI ownership, ABI/native crash, deprecation, SemVer và consumer compatibility testing.
8. [`08_version_compatibility_migration_forensics.md`](08_version_compatibility_migration_forensics.md) — Kotlin metadata, pre-release binary, language/API/JVM target contract, compiler-plugin lockstep, Compose compiler migration, KSP/kapt, public inline/default-arg/const/value-class ABI, Android target migration, transitive dependency floor và version-upgrade forensic playbook.

## Cách dùng cùng Production Casebook

Depth Labs không thay Casebook. Nên đọc chúng theo cặp:

```text
Case 01 Architecture
→ Depth Lab 01 Architecture invariants

Case 03 Offline-first
→ Depth Lab 02 Sync correctness

Case 02/08/09 Coroutine + runtime
→ Depth Lab 03 Concurrency semantics

Case 11 Compose UI system
→ Depth Lab 04 Compose runtime reasoning

Case 05/13 Reliability/release
→ Depth Lab 05 Testing + observability

Case 15/18/19 Build/compat/startup
→ Depth Lab 06 Build + release forensics

Case 17/20 NDK + SDK authoring
→ Depth Lab 07 Consumer/native safety

05 Version Evolution + Case 08/15/18/20
→ Depth Lab 08 Version compatibility + migration forensics
```

## Quy tắc học

Không đọc Depth Lab như danh sách best practice để học thuộc. Với mỗi section, hãy tự tạo một timeline hoặc failure scenario rồi trả lời:

```text
invariant nào phải giữ?
owner là ai?
state nào authoritative?
operation có thể bị replay không?
outcome có thể ambiguous không?
process death xảy ra ở đây thì sao?
request/result cũ có thể overwrite state mới không?
release cũ có đọc data/artifact mới không?
metric/log nào chứng minh behavior production?
version change nào làm producer/consumer contract thay đổi?
artifact hoặc metadata nào thật sự khác trước?
```

Nếu chỉ biết tên API nhưng không trả lời được các câu trên, kiến thức vẫn đang ở mức implementation chứ chưa tới mức engineering reasoning.

## Mental model chung

```text
Requirement
-> Invariant
-> Ownership
-> State / Source of Truth
-> Execution Context
-> Concurrency / Ordering
-> Failure / Cancellation / Retry
-> Persistence / Reconstruction
-> Compatibility
-> Version / Artifact Contract
-> Observability
-> Release / Recovery
```

Đây là lớp kiến thức cuối cùng trước khi chuyển từ “biết Android” sang “có thể giải thích và vận hành một hệ thống Android production”.