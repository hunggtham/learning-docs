# 20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **130-132. 트랜잭션 (Transaction)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

쿼리, 성능, 최적화와, 반정규화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **16. 정규화(Normalization)와 이상 현상(Anomaly)**에서 만든 기준을 이어받아 **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)

Từ **16. 정규화(Normalization)와 이상 현상(Anomaly)**, ta đã có điểm tựa để bước vào **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/55 trước khi đi vào chi tiết.

Để đọc **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **쿼리 성능 최적화 (Query Optimization)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 쿼리 성능 최적화 (Query Optimization)

Các ý ngay dưới **쿼리 성능 최적화 (Query Optimization)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Tối ưu hóa tốc độ chạy SQL thông qua **Optimizer (옵티마이저 - Bộ tối ưu)**.
- **RBO (Rule-Based Optimizer):** Tối ưu theo **규칙 (Quy tắc)** định sẵn. Phụ thuộc vào kinh nghiệm người lập trình.
- **CBO (Cost-Based Optimizer):** Tối ưu theo **비용 (Chi phí)** ước tính dựa trên thống kê dữ liệu. Rất thông minh và phổ biến hiện nay.
- **APM (Application Performance Management):** Công cụ giám sát hiệu suất ứng dụng.

Các bullet của **쿼리 성능 최적화 (Query Optimization)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **쿼리 성능 최적화 (Query Optimization)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **반정규화 (Denormalization - Phi chuẩn hóa)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **반정규화 (Denormalization - Phi chuẩn hóa)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 반정규화 (Denormalization - Phi chuẩn hóa)

Bây giờ ta đi vào nội dung của **반정규화 (Denormalization - Phi chuẩn hóa)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **개념:** Cố tình phá vỡ chuẩn hóa (Gộp bảng, thêm dữ liệu trùng lặp).
- **목적:** Để **tăng hiệu suất truy vấn (조회 속도 향상)** khi thao tác JOIN quá nhiều.
- **단점:** Đánh đổi bằng sự **suy giảm tính nhất quán** (데이터 정합성 저하) và khó khăn khi cập nhật dữ liệu.

---

Các bullet của **반정규화 (Denormalization - Phi chuẩn hóa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **반정규화 (Denormalization - Phi chuẩn hóa)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **130-132. 트랜잭션 (Transaction)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.