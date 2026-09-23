# 11 — Governance, lineage và security

Governance là cách hệ thống biết dữ liệu nào tồn tại, ai sở hữu, được dùng cho mục đích nào, thay đổi ra sao và phải xóa khi nào. Đây là control plane của data product, không phải tài liệu hành chính nằm ngoài pipeline.

## 1. Data contract

Contract giữa producer và consumer cần bao gồm schema, grain, semantics, quality expectation, compatibility, owner, freshness và incident contact. Contract tốt làm breaking change thành một quy trình có thông báo thay vì surprise.

Schema registry không tự tạo semantic contract. Field `status` có thể parse được nhưng đổi nghĩa từ “payment state” sang “shipment state” vẫn là breaking change.

## 2. Catalog và ownership

Catalog tối thiểu cần biết dataset path, domain, owner, steward, source, grain, sensitivity, freshness SLO, retention và related assets. Dataset không có owner không có người quyết định khi quality fail hoặc schema cần evolve.

Ownership phải gắn với action: ai approve change, ai triage incident, ai xác nhận delete, ai chịu cost.

## 3. Lineage

Lineage là evidence graph từ source → ingestion → transformation → serving → consumer. Static SQL parser có thể bỏ sót dynamic code; runtime lineage có chi phí instrumentation. Nên kết hợp orchestration metadata, query logs, table catalog và deployment version.

Lineage không chứng minh data đúng. Nó giúp khoanh blast radius và lần ngược nguyên nhân nhanh hơn.

## 4. Security boundary

Least privilege áp dụng cho service account, engineer và consumer. Tách quyền đọc raw PII khỏi quyền đọc serving aggregate. Encryption at rest/in transit là baseline; cần thêm masking/tokenization, row/column-level access, audit log và secret rotation.

Development không nên copy production PII mặc định. Nếu cần sample, dùng synthetic hoặc masked data có policy rõ.

## 5. Retention và deletion

Retention phải bao phủ raw files, snapshots, backups, caches, derived tables và downstream exports. Xóa row ở serving nhưng giữ file raw hoặc snapshot cũ vẫn có thể vi phạm deletion requirement.

Replayability và privacy có thể xung đột. Thiết kế cần biết field nào immutable, field nào có thể redact, và khi deletion xảy ra thì state/projection nào phải rebuild.

## 6. Quality và incident

Governance nên liên kết contract với quality checks, lineage-aware alert và runbook. Alert về schema drift phải cho biết consumer bị ảnh hưởng; alert về PII access phải giữ audit evidence; quarantine phải có owner và replay procedure.

## 7. Review checklist

1. Dataset có owner, grain, sensitivity và retention không?
2. Producer/consumer contract và compatibility policy ở đâu?
3. Có thể lần ngược từ metric sai về source snapshot không?
4. Quyền raw/model/serving có tách không?
5. Delete/rectification có lan qua snapshot, backup và derived output không?

Đọc tiếp: [04 — Reliability](../04_reliability_and_production.md), [09 — Warehouse/lakehouse](../09_warehouse_lake_lakehouse/README.md), [10 — Serving](../10_serving_semantic_layer/README.md).

## 8. Classification và policy enforcement

Sensitivity classification nên gắn với column/field và purpose, không chỉ gắn với database. Một dataset có thể chứa PII ở một column, aggregate an toàn ở column khác và secret ở payload nested.

Policy enforcement cần xảy ra cả lúc đọc và lúc copy/export. Masking trong UI không đủ nếu user vẫn có quyền đọc raw file hoặc download cache. Policy test nên kiểm tra role, purpose, environment, region và audit event.

## 9. Lineage confidence

Không phải edge lineage nào cũng có cùng độ tin cậy:

```text
declared contract > runtime observed > static parser > naming convention
```

Catalog nên lưu source của edge và timestamp quan sát. Khi lineage thiếu, hiển thị “unknown” tốt hơn tạo graph giả chắc chắn khiến incident triage đi sai.

## 10. Change management

Một schema/semantic change cần blast-radius query: downstream tables, dashboards, ML features, exports, access policies và cost centers. Owner phê duyệt change phải khác với người chỉ sửa file nếu risk cao.

Deprecation window cần có telemetry consumer. Không xóa field chỉ vì catalog không liệt kê consumer; absence of evidence không phải evidence of absence.

## 11. Data deletion audit

Deletion request nên tạo manifest gồm subject key, source tables, snapshots, derived outputs, backups và completion evidence. Reconciliation sau delete phải chứng minh subject không còn trong các serving path được scope, hoặc ghi rõ retention exception được phê duyệt.
