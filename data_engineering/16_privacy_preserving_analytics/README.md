# 16 — Privacy-preserving analytics

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **16 — Privacy-preserving analytics**. Route đi từ threat model và inference risk → differential privacy → k-anonymity/aggregation và query budgets → access, governance và retention → privacy/utility trade-offs, để bảo vệ dữ liệu được đánh giá theo thông tin có thể suy ra.

Privacy là giới hạn thông tin có thể suy ra từ đầu ra (output / 출력), không chỉ là kiểm soát truy cập (access control / 접근 제어). Một người dùng (user / 사용자) không đọc raw PII vẫn có thể suy ra cá nhân nếu truy vấn (query / 쿼리) aggregate quá nhỏ hoặc nhiều lần truy vấn (query / 쿼리) được kết hợp.

## 1. Threat mô hình (model / 모델)

Trước khi chọn kỹ thuật, xác định adversary, auxiliary dữ liệu (data / 데이터), truy vấn (query / 쿼리) ngân sách (budget / 예산), protected thực thể (entity / 엔터티) và acceptable disclosure. K-anonymity có thể thất bại khi quasi-identifier dễ phép nối (join / 조인) với dataset ngoài; suppression không sửa được attribute disclosure.

> **Chuyển mạch:** **Threat model** xác định ai có thể suy ra điều gì; **Differential privacy** biến rủi ro đó thành noise budget, rồi **Aggregate release policy** kiểm soát cách phát hành.

## 2. Differential privacy

Differential privacy thêm noise có kiểm soát để đầu ra (output / 출력) của một cá nhân không làm thay đổi phân phối kết quả quá nhiều. Hai tham số cần giải thích:

- epsilon: privacy mất mát (loss / 손실)/ngân sách (budget / 예산);
- delta: xác suất cho phép ngoại lệ nhỏ.

Composition quan trọng: nhiều truy vấn (query / 쿼리) cùng dataset cộng dồn privacy mất mát (loss / 손실). Mỗi dashboard không thể tự dùng một ngân sách vô hạn mà không có accountant trung tâm.

> **Chuyển mạch:** **Aggregate release policy** ràng buộc query, population và budget; **Utility trade-off** đo phần thông tin còn dùng được sau ràng buộc đó.

## 3. Aggregate bản phát hành (release / 릴리스) chính sách (policy / 정책)

Chính sách (policy / 정책) nên giới hạn minimum group kích thước (size / 크기), truy vấn (query / 쿼리) overlap, suppression, rounding, noise, tỷ lệ (rate / 비율) limit và retention của đầu ra (output / 출력). Một chỉ số (metric / 지표) hợp lệ riêng lẻ có thể trở thành leak khi người dùng lấy chênh lệch giữa hai filter gần giống nhau.

> **Chuyển mạch:** **Utility trade-off** cho biết privacy cost ảnh hưởng kết quả ra sao; **Data lifecycle** đặt quyết định đó vào collection, retention, deletion và access.

## 4. Utility sự đánh đổi (trade-off / 트레이드오프)

Noise mạnh bảo vệ privacy nhưng làm chỉ số (metric / 지표) nhỏ/rare segment không ổn định. Cần công bố confidence/bất định (uncertainty / 불확실성) và không dùng private estimate cho billing hoặc enforcement nếu chưa có correction mô hình (model / 모델).

> **Chuyển mạch:** Trong **16 — Privacy-preserving analytics**, **4. Utility sự đánh đổi (trade-off / 트레이드오프)** nêu điều cần giải thích; **5. dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기)

Raw, snapshots, backups, logs, caches và notebook extracts đều nằm trong privacy phạm vi (scope / 범위). Redaction phải xử lý cả derived features và huấn luyện (training / 학습) artifacts nếu chúng có thể encode thông tin subject.

> **Chuyển mạch:** **Data lifecycle** chỉ có giá trị khi có log và policy evidence; **Evidence** khóa lại claim về privacy, utility và quyền truy cập bằng dấu vết có thể kiểm tra.

## 6. bằng chứng (evidence / 증거)

Lưu chính sách (policy / 정책) phiên bản (version / 버전), privacy ngân sách (budget / 예산) consumed, truy vấn (query / 쿼리) actor/purpose, dataset snapshot, suppression reason và privacy rà soát (review / 검토). kiểm thử (test / 테스트) adversarial truy vấn (query / 쿼리) reconstruction và membership suy luận (inference / 추론) theo định kỳ.

Đọc tiếp: [11 — Governance](../11_governance_lineage_security/README.md), [10 — Serving](../10_serving_semantic_layer/README.md), [12 — Cost](../12_cost_performance_capacity/README.md).

> **Bàn giao:** Sau **6. bằng chứng (evidence / 증거)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
