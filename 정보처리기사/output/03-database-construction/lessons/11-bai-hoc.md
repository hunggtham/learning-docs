# 110-114. 키 (Keys)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và phân loại 5 loại khóa trong mô hình quan hệ: Siêu khóa (`슈퍼키`), Khóa ứng viên (`후보키`), Khóa chính (`기본키`), Khóa thay thế (`대체키`), và Khóa ngoại (`외래키`).
- Phân biệt chính xác hai tính chất sống còn của khóa: **Tính duy nhất (`유일성 / Uniqueness`)** và **Tính tối thiểu (`최소성 / Minimality`)**.
- Nhớ rõ điều kiện ràng buộc đối với Khóa chính (Không NULL, không trùng lặp) và Khóa ngoại (Tham chiếu hợp lệ hoặc NULL).

## 핵심 키워드 (Từ khóa)
- 키 (Khóa / Key)
- 슈퍼키 (Siêu khóa / Super Key)
- 후보키 (Khóa ứng viên / Candidate Key)
- 기본키 (Khóa chính / Primary Key)
- 대체키 (Khóa thay thế / Alternate Key)
- 외래키 (Khóa ngoại / Foreign Key)
- 유일성 (Tính duy nhất / Uniqueness)
- 최소성 (Tính tối thiểu / Minimality)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([08-bai-hoc.md](08-bai-hoc.md), [10-bai-hoc.md](10-bai-hoc.md)):** Để thỏa mãn đặc trưng bất biến của Relation là tính duy nhất của tuple (`튜플의 유일성`), CSDL quan hệ bắt buộc phải dùng Khóa (Key) để phân biệt các hàng với nhau.
- **Tiếp nối sang các bài sau ([12-bai-hoc.md](12-bai-hoc.md), [14-bai-hoc.md](14-bai-hoc.md), [15-bai-hoc.md](15-bai-hoc.md)):** Khái niệm Khóa chính và Khóa ngoại là nền tảng trực tiếp dẫn đến hai quy tắc toàn vẹn kinh điển: Toàn vẹn thực thể (`개체 무결성`) và Toàn vẹn tham chiếu (`참조 무결성`).

## 읽는 방법 (Cách đọc)
- Học thuộc bảng ma trận tính chất ở TẦNG A: **Super Key = Duy nhất O, Tối thiểu X; Candidate Key = Duy nhất O, Tối thiểu O**.
- Bám sát sơ đồ phân cấp: Tất cả Candidate Key đều là Super Key, nhưng ngược lại thì không.

---

## 110-114. 키 (Keys)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Hai tính chất đo lường của Khóa (키의 특성):**
  - **유일성 (Tính duy nhất / Uniqueness):** Giá trị của khóa có thể phân biệt duy nhất từng hàng (tuple) trong bảng. Không có 2 hàng nào có cùng giá trị khóa.
  - **최소성 (Tính tối thiểu / Minimality):** Khóa được cấu thành từ số lượng thuộc tính vừa đủ nhỏ nhất để đảm bảo tính duy nhất; nếu bỏ bớt bất kỳ thuộc tính nào ra khỏi khóa thì tính duy nhất sẽ bị mất.
- **2. Bảng phân loại 5 loại Khóa theo đề thi (키의 5가지 종류):**
  | Loại Khóa | Thuật ngữ Hàn | Tính duy nhất (유일성) | Tính tối thiểu (최소성) | Đặc điểm thi trắc nghiệm |
  |---|---|:---:|:---:|---|
  | **Siêu khóa** | `슈퍼키 (Super Key)` | **O** | **X** | Phân biệt được các hàng nhưng bị thừa thuộc tính (ví dụ: `(MãSV, HọTên)`). |
  | **Khóa ứng viên** | `후보키 (Candidate Key)` | **O** | **O** | Đủ điều kiện làm khóa chính, vừa duy nhất vừa gọn nhất (ví dụ: `MãSV`, `SốCCCD`). |
  | **Khóa chính** | `기본키 (Primary Key)` | **O** | **O** | Được chọn từ 1 trong các Khóa ứng viên. **Tuyệt đối cấm NULL và cấm trùng lặp**. |
  | **Khóa thay thế** | `대체키 (Alternate Key)` | **O** | **O** | Là các Khóa ứng viên còn lại sau khi đã chọn xong Khóa chính (`후보키 - 기본키`). |
  | **Khóa ngoại** | `외래키 (Foreign Key)` | - | - | Thuộc tính tham chiếu đến Khóa chính của bảng khác để tạo mối liên kết. |
- **3. Quy tắc cốt lõi về Khóa chính và Khóa ngoại:**
  - **기본키 (Primary Key):** Không được chứa giá trị `NULL` và không được trùng lặp giá trị (`NULL 불가, 중복 불가` - Ràng buộc Toàn vẹn thực thể).
  - **외래키 (Foreign Key):** Phải trỏ đến một giá trị Khóa chính đang thực sự tồn tại ở bảng được tham chiếu, HOẶC phải mang giá trị `NULL` (nếu không bắt buộc liên kết - Ràng buộc Toàn vẹn tham chiếu).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - Đề hỏi: *"Khóa nào thỏa mãn tính duy nhất nhưng KHÔNG thỏa mãn tính tối thiểu?"* → Đáp án luôn là **슈퍼키 (Super Key)**.
  - Đề hỏi: *"Khóa thay thế (대체키) là gì?"* → Là **Khóa ứng viên không được chọn làm khóa chính**.
  - Đề hỏi: *"Khóa ngoại có được phép chứa giá trị NULL không?"* → **ĐƯỢC PHÉP**, trừ khi có ràng buộc `NOT NULL` bổ sung.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Super thừa thuộc tính; Candidate vừa đủ; Primary chọn một; Alternate là phần còn lại; Foreign để trỏ sang bảng khác".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ minh họa trực quan:**
  - Bảng `SINH_VIEN(MaSV, SoCCCD, HoTen, Email, Lop)`:
    - `(MaSV, HoTen)` hoặc `(SoCCCD, Lop)` là **슈퍼키 (Super Key)** vì giúp phân biệt duy nhất từng người, nhưng thừa cột `HoTen` hoặc `Lop`.
    - `MaSV` và `SoCCCD` là hai **후보키 (Candidate Key)** vì vừa xác định duy nhất sinh viên, vừa không thể rút gọn thêm.
    - Nhà thiết kế chọn `MaSV` làm **기본키 (Primary Key)**.
    - Thuộc tính `SoCCCD` trở thành **대체키 (Alternate Key)**.
  - Bảng `DANG_KY_HOC(MaDK, MaSV, MaMH)`:
    - Cột `MaSV` ở bảng này là **외래키 (Foreign Key)** tham chiếu đến `MaSV` của bảng `SINH_VIEN`.
- **Quan hệ bao hàm toán học:**
  $$\text{Khóa chính} \subset \text{Khóa ứng viên} \subset \text{Siêu khóa}$$

### 복습 체크리스트
- [ ] Phân biệt được 유일성 (duy nhất) và 최소성 (tối thiểu).
- [ ] Nhớ rõ 슈퍼키 chỉ thỏa mãn 유일성, không thỏa mãn 최소성.
- [ ] Nêu được định nghĩa 대체키 (후보키 còn lại).
- [ ] Khẳng định được điều kiện cấm của 기본키 (không NULL, không trùng lặp).
