# 16 — Privacy-preserving analytics

Privacy là giới hạn thông tin có thể suy ra từ output, không chỉ là access control. Một user không đọc raw PII vẫn có thể suy ra cá nhân nếu query aggregate quá nhỏ hoặc nhiều lần query được kết hợp.

## 1. Threat model

Trước khi chọn kỹ thuật, xác định adversary, auxiliary data, query budget, protected entity và acceptable disclosure. K-anonymity có thể thất bại khi quasi-identifier dễ join với dataset ngoài; suppression không sửa được attribute disclosure.

## 2. Differential privacy

Differential privacy thêm noise có kiểm soát để output của một cá nhân không làm thay đổi phân phối kết quả quá nhiều. Hai tham số cần giải thích:

- epsilon: privacy loss/budget;
- delta: xác suất cho phép ngoại lệ nhỏ.

Composition quan trọng: nhiều query cùng dataset cộng dồn privacy loss. Mỗi dashboard không thể tự dùng một ngân sách vô hạn mà không có accountant trung tâm.

## 3. Aggregate release policy

Policy nên giới hạn minimum group size, query overlap, suppression, rounding, noise, rate limit và retention của output. Một metric hợp lệ riêng lẻ có thể trở thành leak khi người dùng lấy chênh lệch giữa hai filter gần giống nhau.

## 4. Utility trade-off

Noise mạnh bảo vệ privacy nhưng làm metric nhỏ/rare segment không ổn định. Cần công bố confidence/uncertainty và không dùng private estimate cho billing hoặc enforcement nếu chưa có correction model.

## 5. Data lifecycle

Raw, snapshots, backups, logs, caches và notebook extracts đều nằm trong privacy scope. Redaction phải xử lý cả derived features và training artifacts nếu chúng có thể encode thông tin subject.

## 6. Evidence

Lưu policy version, privacy budget consumed, query actor/purpose, dataset snapshot, suppression reason và privacy review. Test adversarial query reconstruction và membership inference theo định kỳ.

Đọc tiếp: [11 — Governance](../11_governance_lineage_security/README.md), [10 — Serving](../10_serving_semantic_layer/README.md), [12 — Cost](../12_cost_performance_capacity/README.md).
