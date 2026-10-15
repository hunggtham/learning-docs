# 4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)

## 학습 목표 (Mục tiêu)
- Nắm vững các thành phần cấu tạo nền tảng của Cơ sở dữ liệu quan hệ (`관계형 데이터베이스 - RDBMS`): Quan hệ (`릴레이션`), Bộ (`튜플`), Thuộc tính (`속성`), và Miền giá trị (`도메인`).
- Phân biệt tuyệt đối giữa số lượng hàng (`카디널리티 - Cardinality`) và số lượng cột (`디그리 - Degree / 차수`), giải quyết các câu hỏi tính toán bảng dữ liệu trong đề thi.
- Thuộc nằm lòng 5 loại khóa trong CSDL: Khóa chính (`기본키`), Khóa ứng viên (`후보키`), Khóa thay thế (`대체키`), Siêu khóa (`슈퍼키`), và Khóa ngoại (`외래키`).
- Khắc sâu 2 quy tắc ràng buộc toàn vẹn sống còn: Toàn vẹn thực thể (`개체 무결성`) và Toàn vẹn tham chiếu (`참조 무결성`).

## 핵심 키워드 (Từ khóa)
- 릴레이션 (Bảng quan hệ / Relation / Table)
- 튜플 (Bộ / Tuple / Row) vs 속성 (Thuộc tính / Attribute / Column)
- 카디널리티 (Lực lượng / Cardinality / 행의 수)
- 디그리 / 차수 (Bậc / Degree / 열의 수)
- 도메인 (Miền giá trị / Domain / 원자값)
- 후보키 / 기본키 / 슈퍼키 / 외래키 (Candidate, Primary, Super, Foreign Key)
- 개체 무결성 (Toàn vẹn thực thể / Not Null + Unique)
- 참조 무결성 (Toàn vẹn tham chiếu / Foreign Key Constraint)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([14. 미들웨어](40-bai-hoc.md)):** Sau khi xem xét tầng kết nối phần mềm trung gian, bài này bước sang nội dung thiết kế cấu trúc dữ liệu quan hệ trong Môn 1.
- **Tiếp nối sang bài sau ([5. 관계 데이터 연산 및 정규화](42-bai-hoc.md)):** Áp dụng các phép toán đại số quan hệ và kỹ thuật chuẩn hóa dữ liệu từ 1NF đến BCNF trên các bảng quan hệ này.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ công thức tính Cardinality (đếm số hàng) và Degree (đếm số cột) cùng điều kiện của Toàn vẹn thực thể (Khóa chính cấm Null) và Toàn vẹn tham chiếu (Khóa ngoại hoặc Null hoặc khớp khóa chính).
- Đọc TẦNG B để phân tích bảng ví dụ cụ thể minh họa sự khác nhau giữa Super Key (chỉ cần duy nhất) và Candidate Key (duy nhất và tối thiểu).

---

## 4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Cấu trúc bảng quan hệ (릴레이션의 구성 요소):**
  - `릴레이션 (Relation)`: Bảng dữ liệu hai chiều gồm các hàng và cột.
  - `튜플 (Tuple - Bộ)`: **Một hàng (Row)** trong bảng, đại diện cho một thực thể độc lập cụ thể.
  - `속성 (Attribute - Thuộc tính)`: **Một cột (Column)** trong bảng, đại diện cho một đặc tính hoặc trường dữ liệu của thực thể.
  - `도메인 (Domain - Miền giá trị)`: Tập hợp tất cả các giá trị nguyên tử (`원자값 - Atomic value`) hợp lệ mà một thuộc tính được phép nhận (ví dụ: Thuộc tính "Giới tính" chỉ nhận giá trị trong tập `{'Nam', 'Nữ'}`).
  - **2 chỉ số kích thước bảng bắt buộc phải nhớ:**
    - `카디널리티 (Cardinality - Lực lượng)`: **Tổng số lượng các hàng / bộ (튜플의 수)** có trong bảng.
    - `디그리 / 차수 (Degree - Bậc)`: **Tổng số lượng các cột / thuộc tính (속성의 수)** có trong bảng.
- **2. Bảng phân loại 5 loại khóa trong CSDL quan hệ:**
  - `슈퍼키 (Super Key - Siêu khóa)`:
    - Tập thuộc tính xác định duy nhất từng bộ trong bảng.
    - **Thỏa mãn Tính duy nhất (`유일성`), nhưng KHÔNG thỏa mãn Tính tối thiểu (`최소성`)**. (Ví dụ: `(MSSV, Họ tên)` là một siêu khóa).
  - `후보키 (Candidate Key - Khóa ứng viên)`:
    - Khóa có thể được dùng làm khóa chính.
    - **Thỏa mãn CẢ Tính duy nhất (`유일성`) VÀ Tính tối thiểu (`최소성`)**. (Ví dụ: `MSSV`, hoặc `Số CCCD`).
  - `기본키 (Primary Key - Khóa chính)`:
    - Là một Khóa ứng viên được người thiết kế cơ sở dữ liệu lựa chọn làm đại diện duy nhất để phân biệt các hàng trong bảng.
    - **Quy tắc tuyệt đối:** **Không được trùng lặp và KHÔNG ĐƯỢC PHÉP CHỨA GIÁ TRỊ NULL (`Unique & Not Null`)**.
  - `대체키 (Alternate Key - Khóa thay thế / Khóa phụ)`:
    - Là các Khóa ứng viên còn lại không được chọn làm khóa chính (Ví dụ: chọn `MSSV` làm khóa chính thì `Số CCCD` trở thành khóa thay thế).
  - `외래키 (Foreign Key - Khóa ngoại)`:
    - Thuộc tính trong một bảng tham chiếu đến Khóa chính của một bảng khác, dùng để thiết lập mối quan hệ liên kết giữa các bảng.
- **3. Hai ràng buộc toàn vẹn sống còn (무결성 제약조건):**
  - **개체 무결성 (Entity Integrity - Toàn vẹn thực thể):**
    - Quy định: **Khóa chính (`기본키`) tuyệt đối không bao giờ được nhận giá trị NULL và không được trùng lặp giá trị giữa các hàng trong bảng**.
  - **참조 무결성 (Referential Integrity - Toàn vẹn tham chiếu):**
    - Quy định: **Giá trị của Khóa ngoại (`외래키`) hoặc là phải mang giá trị NULL, hoặc là phải trùng khớp hoàn toàn với một giá trị khóa chính đang tồn tại thực tế ở bảng được tham chiếu**.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Cardinality là số cột, Degree là số hàng?"* -> **Sai ngược hoàn toàn**. **Cardinality là SỐ HÀNG (튜플 수), Degree là SỐ CỘT (속성 수)**.
  - **Bẫy 2:** *"Khóa ngoại có được phép nhận giá trị NULL không?"* -> **ĐƯỢC PHÉP (NULL 가능)**, miễn là nếu có giá trị thì phải tồn tại ở bảng cha. Nhưng Khóa chính thì tuyệt đối KHÔNG ĐƯỢC NULL.
  - **Bẫy 3:** *"Khóa thỏa mãn tính duy nhất nhưng không thỏa mãn tính tối thiểu là khóa gì?"* -> **슈퍼키 (Super Key)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Hàng là Tuple đếm ra Cardinality; Cột là Attribute đếm ra Degree; Toàn vẹn thực thể cấm Null khóa chính, Toàn vẹn tham chiếu ràng buộc khóa ngoại".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán mẫu trắc nghiệm tính Cardinality và Degree:**
  - Cho bảng `Học_Sinh` gồm các cột: `Mã_HS`, `Họ_Tên`, `Lớp`, `Điểm_Toán`. Bảng hiện có 50 học sinh đăng ký.
  - Ta xác định:
    - Số cột (Degree / 차수) = $4$.
    - Số hàng (Cardinality / 카디널리티) = $50$.
  - Nếu ta thêm một cột mới `Điểm_Văn` và xóa đi 5 học sinh:
    - Degree mới = $4 + 1 = 5$.
    - Cardinality mới = $50 - 5 = 45$.

### 복습 체크리스트
- [ ] Phân biệt được Tuple (hàng) và Attribute (cột).
- [ ] Tính đúng Cardinality (số hàng) và Degree (số cột) từ một bảng CSDL cho trước.
- [ ] Nhớ Super Key chỉ có 유일성, còn Candidate Key có cả 유일성 và 최소성.
- [ ] Định nghĩa chuẩn 개체 무결성 (Khóa chính Not Null & Unique).
- [ ] Định nghĩa chuẩn 참조 무결성 (Khóa ngoại hoặc Null hoặc khớp bảng tham chiếu).
