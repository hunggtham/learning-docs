# De-identification, linkage rủi ro (risk / 위험) và differential privacy intuition

> **Mạch đọc:** Đặt **De-identification, linkage rủi ro (risk / 위험) và differential privacy intuition** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Quasi-identifiers** sang **Hashing identifier**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Xóa tên và email khỏi dataset không tự động làm dữ liệu anonymous. Nhiều thuộc tính tưởng vô hại khi kết hợp có thể nhận diện lại cá nhân qua bên ngoài (external / 외부) datasets. Privacy kỹ thuật (engineering / 엔지니어링) vì thế phải lập luận (reasoning / 추론) về thông tin (information / 정보) leakage, không chỉ direct identifiers.

## Quasi-identifiers

Ngày sinh, postcode, nghề nghiệp hoặc timestamp có thể không unique riêng lẻ nhưng combination có thể rất hiếm. **Linkage attack** nối dataset đã “ẩn danh” với nguồn khác để suy ra định danh (identity / 식별자) hoặc sensitive attribute.

Rủi ro (risk / 위험) phụ thuộc population và auxiliary thông tin (information / 정보) attacker có thể có.


> **Chuyển mạch:** Từ **Quasi-identifiers**, ta sang **Hashing identifier** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hashing identifier

Băm (hash / 해시) email/phone deterministic vẫn cho phép dictionary attack nếu đầu vào (input / 입력) không gian (space / 공간) đoán được. Salt/secret key giúp chống lookup nhưng hashed identifier vẫn có thể là pseudonymous stable identifier, không nhất thiết anonymous.

Pseudonymization hữu ích để giảm exposure nhưng vẫn cần kiểm soát truy cập (access control / 접근 제어) và retention chính sách (policy / 정책).


> **Chuyển mạch:** Từ **Hashing identifier**, ta sang **k-anonymity intuition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## k-anonymity intuition

k-anonymity cố làm mỗi bản ghi (record / 레코드) indistinguishable với ít nhất k-1 records theo quasi-identifiers. Generalization/suppression giảm re-identification rủi ro (risk / 위험) nhưng mất utility.

Nó không tự bảo vệ attribute disclosure nếu cả group có cùng sensitive giá trị (value / 값), và không mô hình (model / 모델) mọi auxiliary thông tin (information / 정보).


> **Chuyển mạch:** Từ **k-anonymity intuition**, ta sang **Differential privacy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Differential privacy

**Differential Privacy (DP)** thay câu hỏi: đầu ra (output / 출력) của phân tích (analysis / 분석) có thay đổi đáng kể nếu một cá nhân được thêm/bớt khỏi dataset không? Nếu ảnh hưởng bị bounded, observer khó suy ra participation của một người từ đầu ra (output / 출력).

Noise được calibrated theo sensitivity và privacy parameters. DP là thuộc tính (property / 속성) của randomized cơ chế (mechanism / 메커니즘)/truy vấn (query / 쿼리) tiến trình (process / 프로세스), không phải “thêm noise ngẫu nhiên vào tệp (file / 파일) rồi gọi là private”.


> **Chuyển mạch:** Từ **Differential privacy**, ta sang **Privacy ngân sách (budget / 예산)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Privacy ngân sách (budget / 예산)

Nhiều queries cùng dataset làm leakage tích lũy. Privacy accounting theo dõi composition; ngân sách (budget / 예산) hữu hạn buộc organization quyết định queries nào đáng tiêu privacy mất mát (loss / 손실).

Đây là liên kết (connection / 연결) với tài nguyên (resource / 자원) budgeting: privacy trở thành quantity cần quản trị (governance / 거버넌스), dù interpretation không đơn giản như tiền.


> **Chuyển mạch:** Từ **Privacy ngân sách (budget / 예산)**, ta sang **Utility sự đánh đổi (trade-off / 트레이드오프)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Utility sự đánh đổi (trade-off / 트레이드오프)

Noise nhiều tăng privacy nhưng giảm accuracy. Dataset nhỏ hoặc truy vấn (query / 쿼리) sensitivity cao khó đạt cả utility và strong privacy.

Do đó cần xác định quyết định (decision / 결정) cần độ chính xác nào, population nào và rủi ro (risk / 위험) mô hình (model / 모델) nào trước khi chọn parameters.


> **Chuyển mạch:** Từ **Utility sự đánh đổi (trade-off / 트레이드오프)**, ta sang **quản trị (governance / 거버넌스)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Quản trị (governance / 거버넌스)

Technical anonymization không thay thế purpose limitation, retention và kiểm soát truy cập (access control / 접근 제어). Raw dữ liệu (data / 데이터) vẫn có thể tồn tại ở chuỗi xử lý (pipeline / 파이프라인) khác; logs/exports/backups có thể tái tạo rủi ro (risk / 위험).

Xem thêm: [Data minimization, purpose limitation và retention engineering](./01_data_minimization_purpose_limitation_and_retention_engineering.md).


> **Chuyển mạch:** Từ **quản trị (governance / 거버넌스)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Privacy không phải xóa vài columns. Hãy hỏi attacker có thể kết hợp thông tin nào và đầu ra (output / 출력) làm thay đổi kiến thức (knowledge / 지식) của họ bao nhiêu. De-identification giảm linkability; differential privacy giới hạn influence của từng cá nhân lên aggregate đầu ra (output / 출력).

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 privacy threat models governance and accountability](./00_privacy_threat_models_governance_and_accountability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
