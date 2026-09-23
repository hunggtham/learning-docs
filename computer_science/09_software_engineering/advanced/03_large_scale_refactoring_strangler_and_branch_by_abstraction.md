# Large-scale refactoring, strangler migration và branch-by-abstraction

Refactoring nhỏ có thể hoàn thành trong một commit. Migration lớn kéo dài tuần/tháng phải coexist với production traffic, nhiều binary versions, nhiều teams và state đã tồn tại. Vấn đề chính chuyển từ “code mới đẹp hơn” sang **làm sao đi từ state A tới state B qua một chuỗi trạng thái trung gian luôn deployable, observable và recoverable**.

Mental model trung tâm là: **migration là một distributed state machine của code + data + protocol + traffic + ownership**. Mỗi phase phải có invariant, source of truth, compatibility rule, evidence để chuyển phase và recovery path nếu assumption fail.

## 1. Bài toán ban đầu: production không dừng để architecture được thay

Trong migration dài, old system vẫn nhận bug fixes/feature changes; data tiếp tục tăng; clients không update atomically; deploy rollout mất thời gian.

Vì vậy “new system đúng ở final state” chưa đủ. Engineering phải chứng minh:

```text
old-only state an toàn
coexist state an toàn
cutover state an toàn
new-only state an toàn
```

và transitions giữa chúng không làm mất/duplicate authority.

## 2. Invariant trước roadmap

Trước khi chọn strangler hay rewrite, viết invariants:

```text
mỗi order có đúng một source of truth tại mọi phase
old/new readers đều hiểu schema trong compatibility window
side effect không bị thực hiện hai lần bởi shadow/dual path
rollback không đọc state mà old binary không hiểu
traffic chỉ cutover khi correctness evidence đạt threshold
```

Nếu roadmap chỉ có tasks mà không có phase invariants, migration khó biết khi nào thật sự an toàn để đi tiếp.

## 3. Big-bang rewrite tối đa hóa time-to-feedback và cutover risk

Rewrite toàn bộ hấp dẫn vì “thoát legacy constraints”. Nhưng trong thời gian new system chưa production, old system là moving target.

Risk:

```text
feedback production đến muộn
semantic edge cases bị bỏ sót
migration data chỉ được test gần cuối
cutover blast radius lớn
rollback khó nếu schema/state đã đổi
```

Big-bang có thể hợp lý khi boundary rất nhỏ/cô lập hoặc replacement gần như stateless. Nhưng phải chứng minh thay vì mặc định “rewrite sạch hơn”.

## 4. Strangler migration chuyển capability từng phần

**Strangler pattern** đặt routing/facade seam rồi chuyển từng capability sang implementation mới.

```text
client
  ↓
facade/router
  ├→ old path
  └→ new path
```

Lợi ích: production feedback sớm, blast radius theo slice, rollback traffic dễ hơn.

Điểm khó: nếu data ownership vẫn shared tùy ý, code path tách nhưng invariant vẫn coupled. Seam phải chọn theo capability/state authority, không chỉ URL path.

## 5. Branch by abstraction giữ integration trong mainline

Thay vì long-lived Git branch, tạo abstraction để old/new implementations cùng tồn tại trong mainline.

Typical flow:

```text
introduce abstraction
→ route old implementation through it
→ add new implementation
→ migrate callers/traffic gradually
→ remove old implementation
→ collapse temporary abstraction if no longer useful
```

Lợi ích là continuous integration và giảm merge divergence. Cost là temporary complexity trong codebase; cần deadline/xóa migration scaffolding để nó không thành permanent dual architecture.

## 6. Expand-contract là protocol cho compatibility window

Schema/API change trong distributed deployment hiếm khi atomic. Pattern:

```text
EXPAND:
new producer/consumer version vẫn compatible với old

MIGRATE:
rollout binaries, backfill data, change traffic/authority

CONTRACT:
remove old field/path only after no old reader/writer remains
```

Invariant là **trong mỗi coexist window, mọi live version combination được phép phải hiểu state đủ để giữ correctness**.

Rename DB column trực tiếp có thể fail vì old binary vẫn query tên cũ. Add-new → dual-compatible → migrate → drop-old an toàn hơn nếu state semantics được quản lý rõ.

## 7. Source of truth phải duy nhất hoặc conflict rule phải explicit

Một trong những câu nguy hiểm nhất là “tạm thời cả old và new đều authoritative”. Nếu cả hai accept writes, system cần distributed consistency/conflict semantics thật sự.

Safer patterns thường chọn:

```text
old authoritative, new mirrors
→ compare
→ switch authority once
→ new authoritative, old fallback/read-only if possible
```

Nếu dual authority thật sự cần, conflict/reconciliation phải được thiết kế như distributed system, không gọi nó là temporary migration hack.

## 8. Naive dual-write tạo atomicity gap

Application writes old DB rồi new DB:

```text
write old succeeds
write new fails
```

hoặc ngược lại. Không local transaction nào cover hai stores nếu không dùng distributed protocol.

Outbox/CDC/log-based replication có thể chuyển problem thành durable event + replay/idempotency, nhưng cũng cần lag/replay semantics.

Dual-write chỉ an toàn khi failure state và repair protocol explicit.

## 9. Dual-read có thể che divergence nếu fallback quá tiện

Pattern “read new, nếu miss thì read old” giúp migration nhưng có risk: new store thiếu data lâu mà service vẫn success nhờ fallback, khiến gap không được sửa.

Evidence nên tách:

```text
new hit
fallback-to-old rate
value mismatch rate
age of not-yet-backfilled records
```

Fallback là safety mechanism, không nên biến thành permanent invisibility cloak cho migration debt.

## 10. Backfill là workload production thật

Copy historical data không chỉ là batch script. Backfill tranh CPU, I/O, locks, cache và replication bandwidth với foreground traffic.

Cần:

```text
rate limit / pause-resume
checkpoint progress
idempotent writes
version/conflict rule với concurrent live updates
validation sampling/full comparison
replay after failure
```

Nếu row được update trong lúc backfill copy old snapshot, last-write-wins naïve có thể overwrite fresh state bằng historical state. Ordering/version boundary phải explicit.

## 11. Shadow traffic cho evidence nhưng side effects phải bị cô lập

Shadowing gửi copy request sang new path và bỏ response. Nó giúp compare correctness/performance với production-shaped input.

Nhưng shadow request không được duplicate real side effect: payment, email, external mutation, expensive downstream quota.

Có thể cần stub/sandbox side effect, read-only mode hoặc compare at a lower pure-computation boundary.

## 12. Comparison phải biết semantics, không chỉ byte equality

Old/new responses có thể khác ordering, generated id, timestamp hoặc formatting nhưng semantically equivalent.

Comparator nên classify:

```text
must equal exactly
set-equivalent/order-insensitive
within numeric tolerance
expected intentional difference
hard correctness mismatch
```

Nếu comparison quá strict, noise che signal; quá loose, bug thật bị bỏ.

## 13. Cutover là authority transition có preconditions

Một cutover gate tốt dựa evidence:

```text
backfill complete to known frontier
live replication lag within bound
mismatch rate within accepted threshold
new capacity headroom tested
observability/on-call ready
rollback/roll-forward path rehearsed
old path can be fenced/read-only if needed
```

“Code deployed 100%” không đồng nghĩa migration complete.

## 14. Reversibility phải xét code + data + protocol

Feature flag route về old implementation chỉ là rollback nếu old implementation vẫn hiểu current data/protocol.

Destructive migration có thể làm binary rollback vô nghĩa:

```text
new code writes format old code cannot parse
→ toggle flag back
→ old code crashes/corrupts behavior
```

Reversibility cần backward-compatible state hoặc a forward repair plan. Đôi khi **roll-forward** an toàn hơn rollback.

## 15. Irreversible step phải được nhận diện trước

Examples:

```text
drop old column/data
re-encrypt/delete old key material
send external side effect
change public protocol clients cannot downgrade
reassign irreversible ownership
```

Sau irreversible boundary, recovery plan thay đổi. Runbook phải nói rõ “rollback no longer safe after step X”.

## 16. Traffic ramp phải đi cùng capacity model

Canary 1% traffic không chứng minh new path chịu 100% nếu bottleneck xuất hiện phi tuyến: connection pool, cache hit ratio, DB locks, queueing knee hoặc external quota.

Ramp cần quan sát:

```text
throughput
queue wait
p95/p99
resource saturation
error/mismatch
retry amplification
cache warm-up
```

Có thể cần staged ramp 1% → 5% → 25% → 50% → 100%, nhưng thresholds phải theo workload/SLO chứ không học thuộc percentages.

## 17. Migration kéo theo observability versioned

Trong coexist phase, metric/log/trace phải biết request chạy old/new path, schema version, data source và migration cohort.

Nếu dashboard gộp tất cả, regression 5% traffic có thể biến mất trong average.

Useful dimensions:

```text
implementation version/path
cohort/tenant/region
source-of-truth version
fallback used?
backfill generation
comparison result
```

## 18. Failure modes cần được test ở transition, không chỉ endpoint

Test đáng giá:

```text
new write succeeds, replication fails
backfill crashes midway
old/new binaries coexist
rollback after partial rollout
queue/backlog grows during cutover
feature flag service unavailable
schema contract violation by stale client
region fails during migration
```

Migration correctness nằm ở transitions/failures, không chỉ final happy path.

## 19. Ownership migration là socio-technical state transition

Tách service sang team mới nhưng on-call/schema knowledge/runbook vẫn ở team cũ không tạo autonomy.

Ownership handoff cần:

```text
code/repo ownership
data/schema authority
deploy permission
on-call/runbook
SLO and incident responsibility
consumer contracts
```

Nếu responsibility split mơ hồ, incidents sẽ tạo human coordination queue.

## 20. Temporary compatibility có carrying cost

Dual paths, adapters, flags, duplicated schemas và fallback đều tăng cognitive load. Nếu không có removal criterion, migration scaffold trở thành permanent architecture.

Mỗi temporary mechanism cần:

```text
owner
delete condition
deadline hoặc trigger
metric proving old usage reached zero
```

Technical debt ở đây không phải code xấu; nó là **extra state space** mà team phải reason trong mỗi change/incident.

## 21. Branching strategy và migration strategy là hai concerns liên quan nhưng khác

Git short-lived branch/mainline integration giảm code divergence. Runtime branch-by-abstraction giảm production behavior divergence bằng controllable route.

Long-lived feature branch + big-bang runtime cutover thường trì hoãn integration ở cả hai dimensions. Better migration thường tích hợp code sớm nhưng expose behavior dần.

## 22. Production evidence cho migration

Một migration dashboard nên trả lời:

```text
Traffic: old/new percentage by cohort
Correctness: mismatch/repair/fallback rate
Data: backfill frontier, replication lag, missing/divergent records
Performance: latency/queue/saturation per path
Reliability: retries/errors by path
Compatibility: live client/schema versions
Ownership: active old dependencies/callers
```

Một metric “migration 80%” không có nghĩa gì nếu không biết 80% theo traffic, records, tenants, binaries hay features.

## 23. Decision gate nên dựa invariant + evidence

Trước mỗi phase transition, hỏi:

```text
Invariant nào phải đúng?
Evidence nào chứng minh nó?
Failure nào evidence chưa cover?
Nếu transition xong, rollback còn hợp lệ không?
Authority/source of truth thay đổi ở đâu?
Temporary mechanism nào có thể xóa?
```

Điều này biến migration từ project checklist thành controlled state machine.

## 24. Mô hình tư duy

> Large-scale refactoring là **thiết kế chuỗi trạng thái trung gian an toàn**. Strangler và branch-by-abstraction giảm blast radius bằng coexistence; expand-contract quản compatibility; backfill/CDC quản state movement; cutover chuyển authority; rollback chỉ tồn tại khi code + data + protocol còn compatible. **Đích cuối quan trọng, nhưng engineering difficulty nằm ở mọi transition phải có invariant, evidence và recovery path.**

## Kết nối

Ôn [maintenance/refactoring foundation](../../basic/09_software_engineering/04_maintenance_evolution_and_technical_debt.md), đọc [architecture decisions/evolution](./00_architecture_decisions_evolution_and_socio_technical_constraints.md), [API/schema evolution](./02_api_schema_compatibility_and_evolutionary_design.md), [deployment safety](./05_deployment_safety_canary_blue_green_flags_and_rollback.md), [schema/protocol contracts](../../08_software_systems/advanced/06_schema_protocol_evolution_and_compatibility_contracts.md), [system boundaries](../../08_software_systems/07_system_decomposition_services_and_boundaries.md) và [distributed transaction/outbox](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md).
