# 102. 논리적 설계 (Logical Design / Data Modeling)

## 학습 목표 (Mục tiêu)
- Hiểu rõ bản chất của thiết kế logic (논리적 설계): ánh xạ (mapping) sơ đồ khái niệm thành cấu trúc dữ liệu logic được DBMS hỗ trợ (như cấu trúc bảng trong RDBMS).
- Nhớ chính xác 3 công việc cốt lõi của giai đoạn này: thiết kế lược đồ logic (`논리 스키마 설계`), chuẩn hóa dữ liệu (`정규화`), và thiết kế giao diện giao dịch (`트랜잭션 인터페이스 설계`).
- Nắm vững 3 thành phần của mô hình dữ liệu (`구조 - 연산 - 제약 조건`) và phân biệt rõ: thiết kế logic phụ thuộc vào loại DBMS nhưng độc lập với phần cứng/thiết bị lưu trữ.

## 핵심 키워드 (Từ khóa)
- 논리적 설계 (Thiết kế logic / Logical Design)
- 데이터 모델링 (Mô hình hóa dữ liệu / Data Modeling)
- 논리 스키마 (Lược đồ logic / Logical Schema)
- 매핑 (Ánh xạ / Mapping)
- 정규화 (Chuẩn hóa / Normalization)
- 트랜잭션 인터페이스 (Giao diện giao dịch / Transaction Interface)
- 구조·연산·제약 조건 (Structure - Operation - Constraint)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([101. 개념적 설계](01-bai-hoc.md)):** Sau khi hoàn thành sơ đồ E-R ở tầng khái niệm, ta có mô hình trừu tượng về các thực thể và quan hệ. Nhưng máy tính chưa thể tạo bảng nếu chưa chuyển đổi sang mô hình dữ liệu cụ thể.
- **Tiếp nối sang bài sau ([103. 물리적 설계](03-bai-hoc.md)):** Khi đã có các bảng được chuẩn hóa ở tầng logic, tầng thiết kế vật lý sẽ quyết định cách lưu trữ các bảng đó xuống ổ đĩa, tạo chỉ mục (index) và tối ưu hóa hiệu năng truy xuất.

## 읽는 방법 (Cách đọc)
- Nhớ công thức phân biệt đề thi: Cứ nhắc đến **Bảng (Table)**, **Ánh xạ (Mapping E-R sang Table)**, hoặc **Chuẩn hóa (정규화)** thì 100% là **Thiết kế Logic (논리적 설계)**.
- Ghi nhớ bộ 3 thành phần của mô hình dữ liệu: **Cấu trúc (tĩnh) - Thao tác (động) - Ràng buộc (điều kiện)**.

---

## 102. 논리적 설계 (Logical Design / Data Modeling)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa):** Là quá trình chuyển đổi (ánh xạ / mapping) cấu trúc dữ liệu từ tầng khái niệm thành cấu trúc dữ liệu logic mà hệ quản trị cơ sở dữ liệu mục tiêu (DBMS) hỗ trợ.
- **핵심 키워드 (Từ khóa nhận diện đề thi):**
  - `특정 DBMS가 지원하는 논리적 자료 구조로 변환` (chuyển đổi sang cấu trúc dữ liệu logic DBMS hỗ trợ)
  - `개념 스키마를 논리 스키마로 매핑` (ánh xạ khái niệm sang lược đồ logic)
  - `테이블 설계` (thiết kế bảng trong RDBMS)
  - `정규화 (Normalization)` (chuẩn hóa CSDL để loại bỏ dị thường)
  - `트랜잭션 인터페이스 설계` (thiết kế giao diện cho các giao dịch)
- **시험 포인트 (Điểm thi trọng tâm):**
  - **Nhiệm vụ trọng tâm của thiết kế logic:**
    1. Chuyển đổi sơ đồ E-R thành bảng (Relation/Table Schema).
    2. Thực hiện **Chuẩn hóa (정규화)**: Phân rã bảng để loại bỏ dư thừa dữ liệu và các dị thường (Anomaly).
    3. Thiết kế giao diện giao dịch (`트랜잭션 인터페이스 설계` - định nghĩa đầu vào/đầu ra của transaction).
  - **3 thành phần của mô hình dữ liệu (데이터 모델에 표시할 요소):**
    1. `구조 (Structure)`: Thể hiện tính chất tĩnh, cấu trúc dữ liệu và mối quan hệ giữa các kiểu thực thể.
    2. `연산 (Operation)`: Thể hiện tính chất động, các thao tác xử lý dữ liệu thực tế (thêm, sửa, xóa, tìm kiếm).
    3. `제약 조건 (Constraint)`: Các quy tắc ràng buộc logic đối với dữ liệu thực tế (khóa chính, toàn vẹn tham chiếu, miền giá trị).
  - **Tính phụ thuộc công nghệ:** Phụ thuộc vào loại mô hình của DBMS (ví dụ: mô hình quan hệ), nhưng **hoàn toàn độc lập với phần cứng/thiết bị lưu trữ vật lý** (`하드웨어/물리적 저장장치 독립적`).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Chuẩn hóa (정규화) thuộc bước thiết kế nào?"* → **Đáp án là Thiết kế Logic (논리적 설계)**, KHÔNG PHẢI thiết kế vật lý.
  - **Bẫy 2:** *"Xác định Access Path (đường dẫn truy cập) và tạo Index thuộc bước nào?"* → **Đáp án là Thiết kế Vật lý (물리적 설계)**, không phải logic.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Logic là chuyển E-R thành Bảng và làm Chuẩn hóa (정규화)".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế chuyển đổi (E-R to Relational Mapping):**
  - Mỗi Thực thể (Entity) thường được ánh xạ thành một Bảng (Table/Relation).
  - Mỗi Thuộc tính (Attribute) trở thành một Cột (Column/Field).
  - Khóa chính (Primary Key) của thực thể được xác định.
  - Mối quan hệ 1:N được thể hiện bằng cách đưa khóa chính của bên 1 sang làm Khóa ngoại (Foreign Key) ở bên N.
  - Mối quan hệ N:M bắt buộc phải tách thành một bảng trung gian (Junction Table) chứa khóa ngoại tham chiếu đến cả hai bên.
- **Ví dụ đúng bản chất:**
  - Từ sơ đồ E-R ở bài 101: `Học sinh (학생)` đăng ký `Môn học (과목)` theo quan hệ N:M. Ở tầng Logic, kỹ sư thiết kế 3 bảng: bảng `HOC_SINH(ma_hs, ten)`, bảng `MON_HOC(ma_mh, ten_mh)`, và bảng `DANG_KY(ma_hs, ma_mh, ngay_dk)`. Sau đó thực hiện chuẩn hóa đến dạng chuẩn 3NF hoặc BCNF để đảm bảo không bị dị thường khi cập nhật.
- **Liên hệ mạch kiến thức:**
  - Nhận đầu vào từ **Khái niệm (E-R Diagram)**.
  - Xử lý tại **Logic (Tạo bảng + Chuẩn hóa + Ràng buộc khóa)**.
  - Bàn giao sang **Vật lý (Quyết định cách lưu trữ các bảng này vào đĩa cứng, tạo index cho cột `ma_hs` để tìm kiếm nhanh nhất)**.

### 복습 체크리스트
- [ ] Nêu được định nghĩa thiết kế logic (ánh xạ sang cấu trúc bảng của DBMS).
- [ ] Khẳng định được việc Chuẩn hóa (정규화) nằm ở bước thiết kế logic.
- [ ] Kể tên 3 thành phần của mô hình dữ liệu: 구조 (Structure) - 연산 (Operation) - 제약 조건 (Constraint).
- [ ] Phân biệt được tính phụ thuộc DBMS nhưng độc lập phần cứng của thiết kế logic.
