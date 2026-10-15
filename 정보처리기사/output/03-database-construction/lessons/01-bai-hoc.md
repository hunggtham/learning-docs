# 101. 개념적 설계 (Conceptual Design)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và bản chất của thiết kế khái niệm (개념적 설계): trừu tượng hóa thế giới thực thành cấu trúc thông tin độc lập với DBMS.
- Nhớ chính xác 2 công việc cốt lõi được thực hiện song song: mô hình hóa lược đồ khái niệm (`개념 스키마 모델링`) và mô hình hóa giao dịch (`트랜잭션 모델링`).
- Nhận diện công cụ đầu ra tiêu biểu nhất là Sơ đồ E-R (`E-R 다이어그램`) và tránh bẫy đề thi về tính độc lập công nghệ.

## 핵심 키워드 (Từ khóa)
- 개념적 설계 (Thiết kế khái niệm / Conceptual Design)
- 추상적 개념 (Khái niệm trừu tượng / Abstract Concept)
- 개념 스키마 모델링 (Mô hình hóa lược đồ khái niệm / Conceptual Schema Modeling)
- 트랜잭션 모델링 (Mô hình hóa giao dịch / Transaction Modeling)
- E-R 다이어그램 (Sơ đồ thực thể - mối quan hệ / E-R Diagram)
- DBMS 독립적 (Độc lập với DBMS / DBMS Independent)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước / Điểm khởi đầu:** Đây là bước thiết kế đầu tiên ngay sau giai đoạn phân tích yêu cầu (`요구조건 분석`). Từ tài liệu đặc tả của người dùng, kỹ sư trích xuất các thực thể và quan hệ mà chưa cần quan tâm hệ thống sẽ chạy Oracle, MySQL hay NoSQL.
- **Tiếp nối sang bài sau ([102. 논리적 설계](02-bai-hoc.md)):** Sau khi hoàn thiện sơ đồ khái niệm (E-R Diagram), bước tiếp theo là chuyển đổi (mapping) sơ đồ này thành cấu trúc bảng logic và thực hiện chuẩn hóa dữ liệu.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm vững từ khóa ăn điểm: `개념 스키마`, `E-R 다이어그램`, `트랜잭션 모델링 병행`, và đặc tính sống còn `DBMS 독립적`.
- Đọc TẦNG B để hiểu rõ tại sao cần làm song song cả lược đồ dữ liệu lẫn mô hình giao dịch, giúp xử lý các câu hỏi tình huống trong đề thi.

---

## 101. 개념적 설계 (Conceptual Design)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa):** Là quá trình nhận thức thế giới thực và biểu diễn thành các khái niệm trừu tượng nhằm định hình cấu trúc thông tin (`정보의 구조`), hoàn toàn độc lập với hệ quản trị cơ sở dữ liệu (`DBMS 독립적`).
- **핵심 키워드 (Từ khóa nhận diện đề thi):**
  - `현실 세계의 인식` (nhận thức thế giới thực)
  - `추상적 개념으로 표현` (biểu diễn thành khái niệm trừu tượng)
  - `개념 스키마 모델링` (mô hình hóa lược đồ khái niệm)
  - `트랜잭션 모델링 병행` (thực hiện song song mô hình hóa giao dịch)
  - `E-R 다이어그램` (sơ đồ thực thể - mối quan hệ)
- **시험 포인트 (Điểm thi trọng tâm):**
  - **2 hoạt động thực hiện song song:**
    1. `개념 스키마 모델링`: Xác định các thực thể (Entity), thuộc tính (Attribute) và mối quan hệ (Relationship).
    2. `트랜잭션 모델링`: Xác định các yêu cầu xử lý nghiệp vụ, luồng giao dịch mà hệ thống cần đáp ứng.
  - **Sản phẩm đầu ra cốt lõi:** Biểu đồ thực thể - mối quan hệ (`E-R 다이어그램`).
  - **Đặc tính kỹ thuật quan trọng nhất:** **Hoàn toàn độc lập với DBMS (`DBMS 독립적`)**.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** Đề hỏi *"Vẽ sơ đồ E-R thuộc bước nào?"* → **Đáp án là Thiết kế Khái niệm (개념적 설계)**.
  - **Bẫy 2:** Đề hỏi *"Chuyển đổi sơ đồ E-R thành bảng (Table) thuộc bước nào?"* → **Đáp án là Thiết kế Logic (논리적 설계)**, KHÔNG PHẢI thiết kế khái niệm.
  - **Bẫy 3:** Đề hỏi *"Thiết kế khái niệm có phụ thuộc vào phần mềm DBMS mục tiêu không?"* → **Hoàn toàn KHÔNG phụ thuộc** (`DBMS 독립적`).
- **한 문장 설명 (Câu chốt ghi nhớ):** "Khái niệm là vẽ E-R, trừu tượng hóa và chưa phụ thuộc DBMS".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế và phương pháp thực hiện:**
  - Từ tài liệu phân tích yêu cầu (`요구조건 명세서`), kỹ sư trích xuất các danh từ để làm thực thể (Entity), các động từ chỉ mối liên hệ để làm quan hệ (Relationship), và các tính chất chi tiết để làm thuộc tính (Attribute).
  - Việc tiến hành song song `트랜잭션 모델링` giúp kiểm tra chéo xem lược đồ khái niệm vừa vẽ có đủ dữ liệu để thực hiện các thao tác người dùng mong muốn hay không, tránh tình trạng thiết kế xong bảng mới phát hiện thiếu trường dữ liệu để truy vấn.
- **Ví dụ đúng bản chất:**
  - Trong bài toán quản lý trường học: Ta nhận diện thực thể `Học sinh (학생)` và thực thể `Môn học (과목)`, giữa chúng có mối quan hệ `Đăng ký học (수강)`. Kỹ sư vẽ hình chữ nhật biểu diễn `학생`, hình thoi biểu diễn `수강`, hình elip biểu diễn `mã_học_sinh`. Đây là thiết kế khái niệm thuần túy — chưa hề có câu lệnh SQL, chưa có kiểu dữ liệu `INT`/`VARCHAR`, và chưa gắn với MySQL hay Oracle.
- **Liên hệ mạch kiến thức:**
  - Từ **Yêu cầu (Requirements)**: "Người dùng cần lưu trữ và quản lý những gì?"
  - Sang **Khái niệm (Conceptual)**: "Thế giới thực có những thực thể nào và tương tác với nhau ra sao?" (Sơ đồ E-R).
  - Bàn giao sang **Logic (Logical)**: "Làm thế nào để ánh xạ sơ đồ E-R này thành các bảng quan hệ và chuẩn hóa chúng để không bị trùng lặp dữ liệu?"

### 복습 체크리스트
- [ ] Định nghĩa được 개념적 설계 là gì (biểu diễn thế giới thực thành khái niệm trừu tượng).
- [ ] Nhớ được 2 nhiệm vụ tiến hành song song: khái niệm lược đồ + mô hình hóa giao dịch.
- [ ] Khẳng định được tính chất độc lập với DBMS (DBMS 독립적).
- [ ] Phân biệt chính xác giữa vẽ E-R (khái niệm) và chuyển E-R thành bảng (logic).
