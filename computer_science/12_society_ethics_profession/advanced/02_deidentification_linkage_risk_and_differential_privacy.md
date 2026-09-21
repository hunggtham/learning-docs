# De-identification, linkage risk và differential privacy intuition

Xóa tên và email khỏi dataset không tự động làm dữ liệu anonymous. Nhiều thuộc tính tưởng vô hại khi kết hợp có thể nhận diện lại cá nhân qua external datasets. Privacy engineering vì thế phải reasoning về information leakage, không chỉ direct identifiers.

## Quasi-identifiers

Ngày sinh, postcode, nghề nghiệp hoặc timestamp có thể không unique riêng lẻ nhưng combination có thể rất hiếm. **Linkage attack** nối dataset đã “ẩn danh” với nguồn khác để suy ra identity hoặc sensitive attribute.

Risk phụ thuộc population và auxiliary information attacker có thể có.

## Hashing identifier

Hash email/phone deterministic vẫn cho phép dictionary attack nếu input space đoán được. Salt/secret key giúp chống lookup nhưng hashed identifier vẫn có thể là pseudonymous stable identifier, không nhất thiết anonymous.

Pseudonymization hữu ích để giảm exposure nhưng vẫn cần access control và retention policy.

## k-anonymity intuition

k-anonymity cố làm mỗi record indistinguishable với ít nhất k-1 records theo quasi-identifiers. Generalization/suppression giảm re-identification risk nhưng mất utility.

Nó không tự bảo vệ attribute disclosure nếu cả group có cùng sensitive value, và không model mọi auxiliary information.

## Differential privacy

**Differential Privacy (DP)** thay câu hỏi: output của analysis có thay đổi đáng kể nếu một cá nhân được thêm/bớt khỏi dataset không? Nếu ảnh hưởng bị bounded, observer khó suy ra participation của một người từ output.

Noise được calibrated theo sensitivity và privacy parameters. DP là property của randomized mechanism/query process, không phải “thêm noise ngẫu nhiên vào file rồi gọi là private”.

## Privacy budget

Nhiều queries cùng dataset làm leakage tích lũy. Privacy accounting theo dõi composition; budget hữu hạn buộc organization quyết định queries nào đáng tiêu privacy loss.

Đây là connection với resource budgeting: privacy trở thành quantity cần governance, dù interpretation không đơn giản như tiền.

## Utility trade-off

Noise nhiều tăng privacy nhưng giảm accuracy. Dataset nhỏ hoặc query sensitivity cao khó đạt cả utility và strong privacy.

Do đó cần xác định decision cần độ chính xác nào, population nào và risk model nào trước khi chọn parameters.

## Governance

Technical anonymization không thay thế purpose limitation, retention và access control. Raw data vẫn có thể tồn tại ở pipeline khác; logs/exports/backups có thể tái tạo risk.

Xem thêm: [Data minimization, purpose limitation và retention engineering](./01_data_minimization_purpose_limitation_and_retention_engineering.md).

## Mental Model

> Privacy không phải xóa vài columns. Hãy hỏi attacker có thể kết hợp thông tin nào và output làm thay đổi knowledge của họ bao nhiêu. De-identification giảm linkability; differential privacy giới hạn influence của từng cá nhân lên aggregate output.