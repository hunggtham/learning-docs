# Privacy threat models, governance và accountability

Privacy engineering không đồng nhất với security. Một system có thể không bị hack nhưng vẫn thu thập quá nhiều data, dùng data ngoài purpose ban đầu hoặc giữ data lâu hơn cần thiết. Vì vậy privacy cần threat model riêng về **linkability, identifiability, inference, secondary use và power over data lifecycle**.

## Bắt đầu từ data flow, không chỉ database schema

Vẽ data source → collection → transformation → storage → sharing → analytics → deletion. Cùng một attribute có thể xuất hiện trong logs, cache, backup, warehouse và third-party telemetry.

“Xóa user khỏi main DB” chưa chắc là deletion hoàn chỉnh nếu identifiers còn trong event stream/backups/search index. Data inventory phải theo flow và copies.

## Data minimization là architecture constraint

Cách bảo vệ tốt nhất cho data không cần thiết là không thu nó. Nếu feature chỉ cần age band, lưu full birth date tạo thêm sensitivity mà không tăng utility tương ứng.

Minimization có thể áp ở collection, precision, retention và access. Ví dụ location có thể coarse-grain trước khi lưu nếu exact coordinate không cần cho business logic.

## Purpose limitation và function creep

Data thu để chống fraud sau đó dùng cho marketing có thể thay risk/expectation. Technical teams cần metadata/policy để biết dataset được phép dùng vào purpose nào, thay vì giả định “đã có data thì dùng được”.

Governance tốt nối business purpose với schema/catalog/access policy và review process.

## Pseudonymization không phải anonymization tuyệt đối

Thay name bằng random ID giảm direct identification nhưng các quasi-identifiers hoặc linkage với dataset khác vẫn có thể re-identify. Timestamp, location pattern, rare attributes có thể đủ đặc trưng.

Privacy risk vì vậy phụ thuộc adversary auxiliary information, không chỉ việc xóa cột `name`.

## Access control và accountability

Least privilege giới hạn ai đọc data; auditability cho biết ai đã đọc gì và vì sao. High-risk access thường cần purpose/approval context, not only role.

Audit log phải chống tampering đủ mức, nhưng log cũng chứa personal data nên cần retention/access policy của chính nó.

## Retention là state machine

“Giữ 30 ngày” nghe đơn giản nhưng cần định nghĩa event bắt đầu, legal/business exception, backups, delayed jobs và derived data. Retention implementation thường là workflow:

```text
active → expired → deletion queued → deleted from primary → aged out from backups
```

Nếu system không biết data ở đâu, không thể thực thi retention đáng tin.

## Accountability cần trace decision

Khi automated system ảnh hưởng user, cần tái dựng input/version/policy/model/output liên quan. Provenance hỗ trợ debugging, audit và contestability.

Nhưng logging mọi feature/input cũng tăng privacy surface. Accountability và minimization phải được thiết kế cùng nhau: lưu evidence cần thiết, không copy toàn payload vô hạn.

## Privacy metric không thay normative decision

Differential privacy cung cấp formal framework cho leakage qua statistical release, nhưng parameter choice và applicability vẫn gắn với product context. K-anonymity-like heuristics có limitations trước linkage attacks.

Technical metric không tự quyết định “acceptable use”; governance cần stakeholders, law/policy context và impact analysis.

## Mental Model

> Privacy engineering là quản lý **data lifecycle + allowed purpose + inference/linkage risk + accountability**. Security bảo vệ khỏi unauthorized access; privacy còn hỏi authorized system có nên thu, dùng và giữ data đó theo cách này hay không.

## Kết nối

Ôn [privacy/professional foundation](../../basic/12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md), [data governance](../../basic/12_society_ethics_profession/01_data_governance_bias_and_algorithmic_impact.md) và [security threat models](../../basic/07_security_reliability/00_threat_models_and_security_principles.md).