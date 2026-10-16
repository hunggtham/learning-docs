# Môn 3 · Bài 04 — Các loại Khóa và Ràng buộc toàn vẹn dữ liệu
# 제3과목: 데이터베이스 구축 — 키의 종류(슈퍼키·후보키·기본키·대체키·외래키) 및 데이터 무결성

> **Mạch đọc:** Tiếp nối từ [Bài 03](03-cau-truc-quan-he-schema-tuple-attribute-domain.md) về cấu trúc giải phẫu của bảng quan hệ (Tuple, Attribute, Domain), bài học này giải quyết trái tim logic của toàn bộ hệ quản trị CSDL quan hệ: Cơ chế định danh bản ghi qua hệ thống các loại Khóa (`키의 종류`) và các quy tắc sống còn bảo vệ tính đúng đắn của dữ liệu qua các Ràng buộc toàn vẹn (`데이터 무결성 제약조건`).

> **Mạch kết nối 3 bước (3-part Bridge):**
> - **Từ đâu (Khởi đầu):** Một bảng quan hệ không thể cho phép các dòng trùng lặp hoàn toàn và không thể cho phép liên kết bảng bừa bãi không kiểm soát.
> - **Đang giải quyết gì (Bản chất hiện tại):** Phân biệt ranh giới toán học giữa Tính duy nhất (`유일성`) và Tính tối thiểu (`최소성`) để xếp loại Super Key vs Candidate Key; đồng thời thiết lập 2 luật bất biến: Toàn vẹn thực thể (`개체 무결성` - Khóa chính không rỗng) và Toàn vẹn tham chiếu (`참조 무결성` - Khóa ngoại phải hợp lệ) cùng 4 hành vi tham chiếu (`CASCADE`, `RESTRICT`, `SET NULL`, `SET DEFAULT`).
> - **Dùng đi đâu (Đích đến tiếp theo):** Khi các khóa và toàn vẹn đã được thiết lập, [Bài 05](05-dai-so-quan-he-va-giai-tich-quan-he.md) sẽ đưa vào các phép toán thao tác dữ liệu: Đại số quan hệ (Select, Project, Join, Division) và Giải tích quan hệ.

---

## 1. Hệ thống phân loại Khóa trong CSDL (키의 종류 및 특성)

Khóa là một thuộc tính hoặc một tập hợp nhiều thuộc tính dùng để phân biệt các dòng (Tuple) khác nhau trong cùng một bảng hoặc tạo liên kết giữa các bảng.

```
       ┌────────────────────────────────────────────────────────┐
       │                   슈퍼키 (Super Key)                   │
       │                   [유일성만 만족]                      │
       │  ┌──────────────────────────────────────────────────┐  │
       │  │               후보키 (Candidate Key)             │  │
       │  │             [유일성 + 최소성 모두 만족]          │  │
       │  │  ┌────────────────────────┬───────────────────┐  │  │
       │  │  │ 기본키 (Primary Key)   │ 대체키 (Alternate)│  │  │
       │  │  │ [선택된 주 식별자]     │ [선택되지 않은 키]│  │  │
       │  │  └────────────────────────┴───────────────────┘  │  │
       │  └──────────────────────────────────────────────────┘  │
       └────────────────────────────────────────────────────────┘
```

### 1.1. Bảng so sánh 5 loại Khóa cốt lõi trong đề thi

| Loại Khóa (키의 종류) | Tính duy nhất (유일성) | Tính tối thiểu (최소성) | Bản chất kỹ thuật & Quy tắc nhận diện |
| :--- | :---: | :---: | :--- |
| **1. 슈퍼키**<br>(Super Key / Siêu khóa) | **Thỏa mãn**<br>(만족) | **KHÔNG**<br>(불만족) | Tập thuộc tính định danh duy nhất từng tuple nhưng còn chứa thuộc tính thừa thãi. *(Ví dụ: `(MSSV, Họ tên)`).* |
| **2. 후보키**<br>(Candidate Key / Khóa ứng viên) | **Thỏa mãn**<br>(만족) | **Thỏa mãn**<br>(만족) | **Vừa duy nhất vừa tối thiểu**. Nếu bỏ bớt bất kỳ thuộc tính nào thì mất ngay tính duy nhất. *(Ví dụ: `MSSV`, `Số CCCD`)*. |
| **3. 기본키**<br>(Primary Key / Khóa chính) | **Thỏa mãn**<br>(만족) | **Thỏa mãn**<br>(만족) | Được chọn từ tập Candidate Key làm định danh chính thức của bảng. **Bắt buộc: NOT NULL + UNIQUE**. |
| **4. 대체키**<br>(Alternate Key / Khóa thay thế) | **Thỏa mãn**<br>(만족) | **Thỏa mãn**<br>(만족) | Các Candidate Key còn lại **không được chọn** làm Primary Key. *(Ví dụ: Chọn `MSSV` làm PK thì `Số CCCD` là Alternate Key)*. |
| **5. 외래키**<br>(Foreign Key / Khóa ngoại) | *Tùy thuộc* | *Tùy thuộc* | Thuộc tính của bảng này **tham chiếu đến Primary Key** của bảng khác. Giá trị phải khớp với PK cha hoặc bằng `NULL`. |

### 1.2. Phân biệt sâu sắc giữa Tính duy nhất (유일성) và Tính tối thiểu (최소성)

- **유일성 (Uniqueness / Tính duy nhất):**
  - Mệnh đề: Không bao giờ có 2 tuple khác nhau có cùng giá trị trên tập thuộc tính khóa.
  - Phân tích: Nếu biết giá trị của khóa, ta truy xuất được **chính xác duy nhất 1 dòng**.
- **최소성 (Minimality / Tính tối thiểu):**
  - Mệnh đề: Tập thuộc tính khóa không được chứa bất kỳ thuộc tính nào dư thừa. Nếu loại bỏ bất kỳ thuộc tính nào khỏi tập hợp đó, tính duy nhất sẽ bị phá vỡ.
  - Ví dụ phản chứng: `(MSSV)` đã đủ để xác định duy nhất sinh viên. Nếu ta lấy `(MSSV, Số điện thoại)` làm khóa thì tập hợp này vẫn có tính duy nhất (vì có MSSV), nhưng **vi phạm tính tối thiểu** vì `Số điện thoại` là thuộc tính thừa $\rightarrow$ Đây là **Super Key**, KHÔNG PHẢI Candidate Key.

---

## 2. Các ràng buộc toàn vẹn dữ liệu (데이터베이스 무결성 제약조건)

Tính toàn vẹn (무결성 / Integrity) đảm bảo dữ liệu trong CSDL luôn chính xác, nhất quán và đáng tin cậy.

```
                  ┌────────────────────────────────────────┐
                  │          데이터베이스 4대 무결성       │
                  │   (4 Ràng buộc Toàn vẹn Dữ liệu)       │
                  └──────────────────┬─────────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
1. 개체 무결성 (Entity)     2. 참조 무결성 (Referential) 3. 도메인 무결성 (Domain)
- Khóa chính (PK)           - Khóa ngoại (FK)            - Miền giá trị hợp lệ
- Không được NULL           - Khớp PK hoặc NULL          - Kiểu dữ liệu, CHECK
- Không được trùng          - Ràng buộc quan hệ          - Quy định miền giá trị
```

### 2.1. Chi tiết 4 ràng buộc toàn vẹn cốt lõi

#### 1. Toàn vẹn thực thể (개체 무결성 / Entity Integrity)
- **Mệnh đề thi gốc:** `기본키(Primary Key)는 어떠한 경우에도 NULL 값을 가질 수 없으며, 중복된 값을 가질 수 없다.`
- **Bản chất:** Đã là thực thể thì phải xác định được danh tính. Nếu Khóa chính bị rỗng (`NULL`) hoặc trùng nhau, hệ thống không thể biết đang thao tác trên đối tượng nào.

#### 2. Toàn vẹn tham chiếu (참조 무결성 / Referential Integrity)
- **Mệnh đề thi gốc:** `외래키(Foreign Key) 값은 참조하는 릴레이션의 기본키 값과 일치하거나, NULL이어야 한다.`
- **Bản chất:** Con không thể trỏ vào một người cha không tồn tại. Nếu bảng `NHAN_VIEN` có cột `ma_phong` tham chiếu đến `PHONG_BAN(ma_phong)`, thì giá trị `ma_phong` của nhân viên phải tồn tại trong bảng `PHONG_BAN`, hoặc nhân viên đó chưa được phân phòng (`ma_phong = NULL`). Tuyệt đối không được gán `ma_phong = 999` nếu công ty chỉ có các phòng 1, 2, 3.

#### 3. Toàn vẹn miền giá trị (도메인 무결성 / Domain Integrity)
- **Mệnh đề thi gốc:** `특정 속성의 값은 그 속성에 정의된 도메인에 속한 원자값이어야 한다.`
- **Bản chất:** Giá trị cột phải đúng kiểu dữ liệu, định dạng và phạm vi (ví dụ: tuổi phải là số nguyên dương $\ge 0$, giới tính chỉ được là `'M'` hoặc `'F'`).

#### 4. Toàn vẹn do người dùng định nghĩa (사용자 정의 무결성 / User-defined Integrity)
- **Bản chất:** Các quy tắc nghiệp vụ đặc thù do lập trình viên hoặc DBA thiết lập thông qua điều kiện `CHECK`, `TRIGGER` hoặc `ASSERTION` (ví dụ: ngày kết thúc hợp đồng phải lớn hơn ngày ký).

---

## 3. Các hành động tham chiếu khóa ngoại khi xóa/sửa (외래키 참조 조작 옵션)

Khi một bản ghi ở bảng cha (chứa Primary Key) bị `DELETE` hoặc `UPDATE`, CSDL cung cấp 4 tùy chọn xử lý đối với các bản ghi con tương ứng ở bảng con (chứa Foreign Key):

| Tùy chọn thao tác (참조 옵션) | Hành vi khi bản ghi cha bị Xóa hoặc Sửa (부모 레코드 삭제/수정 시) |
| :--- | :--- |
| **`CASCADE`**<br>(Lan truyền / Thác đổ) | Tự động **xóa hoặc cập nhật hàng loạt** tất cả các bản ghi con tham chiếu tương ứng theo bản ghi cha. *(Ví dụ: Xóa phòng ban thì toàn bộ nhân viên thuộc phòng đó tự động bị xóa theo)*. |
| **`RESTRICT / NO ACTION`**<br>(Cấm / Giới hạn) | Nếu vẫn còn tồn tại ít nhất một bản ghi con đang tham chiếu đến thì **cấm tuyệt đối**, báo lỗi từ chối không cho phép xóa hoặc sửa bản ghi cha. |
| **`SET NULL`**<br>(Gán rỗng) | Cho phép xóa hoặc sửa bản ghi cha, và tự động đặt giá trị khóa ngoại ở tất cả các bản ghi con tương ứng thành **`NULL`**. |
| **`SET DEFAULT`**<br>(Gán mặc định) | Cho phép xóa hoặc sửa bản ghi cha, và tự động đặt giá trị khóa ngoại ở tất cả các bản ghi con tương ứng thành **giá trị mặc định** đã định nghĩa từ trước. |

---

## 4. Bẫy đề thi và bài tập nhận diện (시험 대비 함정 & 실전 포인트)

### 4.1. Bẫy đề thi trắc nghiệm (기출 함정)
- **Bẫy 1: Khóa ứng viên vs Siêu khóa:**
  - *Câu hỏi:* "Tập hợp thuộc tính thỏa mãn tính duy nhất nhưng không thỏa mãn tính tối thiểu là loại khóa nào?"
  - *Đáp án đúng:* **슈퍼키 (Super Key)**. Thỏa mãn cả hai mới là **후보키 (Candidate Key)**.
- **Bẫy 2: Giá trị NULL của Khóa ngoại:**
  - *Câu hỏi:* "Khóa ngoại (Foreign Key) có bao giờ được phép mang giá trị NULL không?"
  - *Đáp án đúng:* **HOÀN TOÀN ĐƯỢC PHÉP** (trừ phi cột đó được định nghĩa thêm ràng buộc `NOT NULL`). Khóa chính mới là đối tượng tuyệt đối cấm NULL.
- **Bẫy 3: Ràng buộc khi xóa cha (CASCADE vs RESTRICT):**
  - *Câu hỏi:* "Tùy chọn nào ngăn chặn việc xóa bản ghi cha nếu còn bản ghi con tham chiếu?"
  - *Đáp án đúng:* **RESTRICT** (hoặc NO ACTION). `CASCADE` là xóa luôn bản ghi con.

---

## 5. Checklist ôn thi (복습 체크리스트)

- [ ] Phân biệt rõ: Siêu khóa (Super Key) chỉ cần duy nhất; Khóa ứng viên (Candidate Key) bắt buộc vừa duy nhất vừa tối thiểu.
- [ ] Nhớ mối quan hệ: Candidate Key không được chọn làm PK thì trở thành Alternate Key (대체키).
- [ ] Thuộc lòng: 개체 무결성 cấm PK bị NULL và cấm trùng; 참조 무결성 yêu cầu FK phải khớp PK hoặc bằng NULL.
- [ ] Phân biệt 4 tùy chọn ngoại khóa: CASCADE (xóa lan truyền), RESTRICT (cấm xóa), SET NULL (gán rỗng), SET DEFAULT (gán mặc định).
