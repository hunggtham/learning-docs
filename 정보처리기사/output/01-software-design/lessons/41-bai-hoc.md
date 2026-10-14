# 4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)

## 4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)

### 릴레이션 (Relation / Table) 구성 요소
Phần “릴레이션 (Relation / Table) 구성 요소” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **튜플 (Tuple):** 행(Row), 레코드(Record).
  - 튜플의 수 = **카디널리티 (Cardinality)** = 기수. (Số lượng dòng).
- **속성 (Attribute):** 열(Column), 필드(Field).
  - 속성의 수 = **디그리 (Degree)** = 차수. (Số lượng cột).
- **도메인 (Domain):** 하나의 속성이 취할 수 있는 같은 타입의 원자값들의 집합. (Tập hợp các giá trị hợp lệ của 1 cột. VD: Cột 'Giới tính' có Domain là 'Nam' và 'Nữ').
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TCTD** (Tuple-Card, Thuộc-Deg): **Tính Cẩn Thận Đi** -> Tuple đi với Cardinality, Cột(속성) đi với Degree.

### 릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)
Phần “릴레이션의 4가지 특징 (4 Đặc trưng của Bảng quan hệ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 튜플의 유일성: 한 릴레이션에 포함된 튜플들은 모두 상이하다. (Không có 2 dòng nào hoàn toàn giống nhau).
- 튜플의 무순서: 튜플 사이에는 순서가 없다. (Thứ tự các dòng không quan trọng).
- 속성의 무순서: 속성들 간의 순서는 중요하지 않다. (Thứ tự các cột không quan trọng).
- 속성값의 원자성: 속성은 더 이상 쪼갤 수 없는 원자값만 저장한다. (Giá trị mỗi ô phải là nguyên tử, không chứa mảng hay list).

### 키(Key)의 종류 (Các loại Khóa)
Phần “키(Key)의 종류 (Các loại Khóa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **후보키 (Candidate Key):** 튜플을 유일하게 식별하기 위해 사용하는 속성. **유일성**과 **최소성**을 모두 만족해야 함. (Khóa ứng viên: Duy nhất và Ít thuộc tính nhất).
- **기본키 (Primary Key - PK):** 후보키 중에서 선택한 주키. NULL 값을 가질 수 없고 중복 불가. (Khóa chính: Chọn từ Candidate Key, cấm NULL).
- **대체키 (Alternate Key):** 후보키가 둘 이상일 때 기본키를 제외한 나머지 후보키. (Khóa thay thế: Khóa ứng viên không được chọn làm PK).
- **슈퍼키 (Super Key):** 튜플을 구별할 수 있는 속성들의 집합. 유일성은 만족하지만, 최소성은 만족하지 않음. (Siêu khóa: Gom nhiều cột lại để phân biệt, dư thừa cột cũng không sao).
- **외래키 (Foreign Key - FK):** 참조되는 릴레이션의 기본키와 대응되는 속성. (Khóa ngoại: Dùng để liên kết 2 bảng).

### 무결성 (Integrity / Tính toàn vẹn) 제약조건
Phần “무결성 (Integrity / Tính toàn vẹn) 제약조건” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개체 무결성 (Entity Integrity):** 기본키는 NULL이나 중복값을 가질 수 없다. (PK không được NULL hoặc trùng lặp).
- **참조 무결성 (Referential Integrity):** 외래키 값은 NULL이거나 참조 릴레이션의 기본키 값과 동일해야 한다. (FK phải có giá trị tồn tại trong PK bảng mẹ, hoặc NULL).
- **도메인 무결성 (Domain Integrity):** 특정 속성의 값이 그 속성이 정의된 도메인에 속한 값이어야 한다. (Giá trị phải nằm trong khoảng/định dạng hợp lệ).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TTD** (Thực - Tham - Domain): **Thích Thì Dùng**.
