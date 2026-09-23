# 17 — Machine-readable data contracts và compatibility testing

Data contract biến expectation về schema và semantics thành artifact có thể kiểm tra trong CI/CD và runtime. Nó không chỉ là một JSON schema; grain, identity, freshness, quality và ownership cũng là contract.

## 1. Contract layers

```text
syntax → schema/type/nullability/enum
semantics → grain, units, timezone, event/state meaning
behavior → ordering, delivery, retry, delete, late correction
service → freshness, completeness, availability, owner
```

Schema pass mà semantics fail vẫn là breaking change.

## 2. Compatibility matrix

Kiểm tra producer mới với consumer cũ, producer cũ với consumer mới, file/snapshot cũ với reader mới và replay code cũ với schema mới. Add optional field có thể backward compatible; rename, enum narrowing và type reinterpretation thường không.

Compatibility test cần fixture thật có duplicate, null, delete, late event, timezone và large value—không chỉ một record tối giản.

## 3. Consumer-driven contract

Consumer khai báo field/metric/latency mà mình phụ thuộc. Producer chạy test trước deploy và biết blast radius. Cần tránh consumer khai báo mọi implementation detail, nếu không contract trở nên cứng và cản evolution.

## 4. Semantic versioning và deprecation

Breaking semantic change phải tạo version/effective date, dual-run hoặc migration. Telemetry consumer dùng để quyết định khi nào xóa v1; không xóa vì catalog không thấy consumer.

## 5. Runtime enforcement

CI không đủ vì source có thể drift sau deploy. Runtime cần schema/contract check, quarantine hoặc stop-the-line cho breaking change, cùng metric contract violation và owner routing. Enforcement nên phân biệt hard failure với warning có expiry.

## 6. Evidence

Lưu contract version, test result, producer commit, consumer list, compatibility decision, exception expiry và observed schema. Đây là input cho lineage, incident triage và change approval.

Đọc tiếp: [02 — Pipeline](../02_pipeline_architecture.md), [08 — Orchestration](../08_orchestration_and_backfill/README.md), [11 — Governance](../11_governance_lineage_security/README.md).
