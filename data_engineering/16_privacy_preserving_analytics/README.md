# 16 — Privacy-preserving analytics

> **Mạch đọc:** Đọc **16 — Privacy-preserving analytics** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Threat mô hình (model / 모델)** sang **2. Differential privacy**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Privacy là giới hạn thông tin có thể suy ra từ đầu ra (output / 출력), không chỉ là kiểm soát truy cập (access control / 접근 제어). Một người dùng (user / 사용자) không đọc raw PII vẫn có thể suy ra cá nhân nếu truy vấn (query / 쿼리) aggregate quá nhỏ hoặc nhiều lần truy vấn (query / 쿼리) được kết hợp.

## 1. Threat mô hình (model / 모델)

Trước khi chọn kỹ thuật, xác định adversary, auxiliary dữ liệu (data / 데이터), truy vấn (query / 쿼리) ngân sách (budget / 예산), protected thực thể (entity / 엔터티) và acceptable disclosure. K-anonymity có thể thất bại khi quasi-identifier dễ phép nối (join / 조인) với dataset ngoài; suppression không sửa được attribute disclosure.


> **Chuyển mạch:** Từ **1. Threat mô hình (model / 모델)**, ta sang **2. Differential privacy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Differential privacy

Differential privacy thêm noise có kiểm soát để đầu ra (output / 출력) của một cá nhân không làm thay đổi phân phối kết quả quá nhiều. Hai tham số cần giải thích:

- epsilon: privacy mất mát (loss / 손실)/ngân sách (budget / 예산);
- delta: xác suất cho phép ngoại lệ nhỏ.

Composition quan trọng: nhiều truy vấn (query / 쿼리) cùng dataset cộng dồn privacy mất mát (loss / 손실). Mỗi dashboard không thể tự dùng một ngân sách vô hạn mà không có accountant trung tâm.


> **Chuyển mạch:** Từ **2. Differential privacy**, ta sang **3. Aggregate bản phát hành (release / 릴리스) chính sách (policy / 정책)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Aggregate bản phát hành (release / 릴리스) chính sách (policy / 정책)

Chính sách (policy / 정책) nên giới hạn minimum group kích thước (size / 크기), truy vấn (query / 쿼리) overlap, suppression, rounding, noise, tỷ lệ (rate / 비율) limit và retention của đầu ra (output / 출력). Một chỉ số (metric / 지표) hợp lệ riêng lẻ có thể trở thành leak khi người dùng lấy chênh lệch giữa hai filter gần giống nhau.


> **Chuyển mạch:** Từ **3. Aggregate bản phát hành (release / 릴리스) chính sách (policy / 정책)**, ta sang **4. Utility sự đánh đổi (trade-off / 트레이드오프)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Utility sự đánh đổi (trade-off / 트레이드오프)

Noise mạnh bảo vệ privacy nhưng làm chỉ số (metric / 지표) nhỏ/rare segment không ổn định. Cần công bố confidence/bất định (uncertainty / 불확실성) và không dùng private estimate cho billing hoặc enforcement nếu chưa có correction mô hình (model / 모델).


> **Chuyển mạch:** Từ **4. Utility sự đánh đổi (trade-off / 트레이드오프)**, ta sang **5. dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기)

Raw, snapshots, backups, logs, caches và notebook extracts đều nằm trong privacy phạm vi (scope / 범위). Redaction phải xử lý cả derived features và huấn luyện (training / 학습) artifacts nếu chúng có thể encode thông tin subject.


> **Chuyển mạch:** Từ **5. dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기)**, ta sang **6. bằng chứng (evidence / 증거)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. bằng chứng (evidence / 증거)

Lưu chính sách (policy / 정책) phiên bản (version / 버전), privacy ngân sách (budget / 예산) consumed, truy vấn (query / 쿼리) actor/purpose, dataset snapshot, suppression reason và privacy rà soát (review / 검토). kiểm thử (test / 테스트) adversarial truy vấn (query / 쿼리) reconstruction và membership suy luận (inference / 추론) theo định kỳ.

Đọc tiếp: [11 — Governance](../11_governance_lineage_security/README.md), [10 — Serving](../10_serving_semantic_layer/README.md), [12 — Cost](../12_cost_performance_capacity/README.md).

> **Bàn giao:** Sau **6. bằng chứng (evidence / 증거)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
