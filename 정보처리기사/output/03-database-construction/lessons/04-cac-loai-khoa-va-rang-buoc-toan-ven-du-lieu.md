# 키의 종류 및 데이터 무결성 (Các loại Khóa và Ràng buộc toàn vẹn dữ liệu)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống phân loại 5 loại Khóa trong mô hình quan hệ: Siêu khóa (`슈퍼키` / Super Key), Khóa ứng viên (`후보키` / Candidate Key), Khóa chính (`기본키` / Primary Key), Khóa thay thế (`대체키` / Alternate Key), Khóa ngoại (`외래키` / Foreign Key).
- Phân biệt bản chất toán học giữa Tính duy nhất (`유일성` / Uniqueness - xác định duy nhất từng tuple) và Tính tối thiểu (`최소성` / Minimality - không chứa thuộc tính dư thừa).
- Làm chủ 3 ràng buộc toàn vẹn dữ liệu cốt lõi: Toàn vẹn thực thể (`개체 무결성` / Entity Integrity), Toàn vẹn tham chiếu (`참조 무결성` / Referential Integrity), Toàn vẹn miền giá trị (`도메인 무결성` / Domain Integrity) cùng Toàn vẹn người dùng định nghĩa (`사용자 정의 무결성`).
- Nắm vững 4 hành vi tham chiếu khóa ngoại khi xóa hoặc cập nhật bản ghi cha: `CASCADE`, `RESTRICT` (hoặc `NO ACTION`), `SET NULL`, `SET DEFAULT`.
- Nhận diện các bẫy trắc nghiệm kinh điển: Khóa ngoại có được nhận giá trị `NULL` không, tính tối thiểu của Super Key, và thứ tự ưu tiên khi chọn Primary Key.

## 핵심 키워드 (Từ khóa)
- 키 (Khóa / Key)
- 슈퍼키 (Siêu khóa / Super Key / 유일성 만족, 최소성 불만족)
- 후보키 (Khóa ứng viên / Candidate Key / 유일성 + 최소성 만족)
- 기본키 (Khóa chính / Primary Key / 주 식별자 / NOT NULL + UNIQUE)
- 대체키 (Khóa thay thế / Alternate Key / 보조키)
- 외래키 (Khóa ngoại / Foreign Key / 참조 무결성)
- 개체 무결성 (Toàn vẹn thực thể / Entity Integrity / 기본키 NULL 불가)
- 참조 무결성 (Toàn vẹn tham chiếu / Referential Integrity / RESTRICT, CASCADE, SET NULL)
- 도메인 무결성 (Toàn vẹn miền giá trị / Domain Integrity / 원자값 및 범위)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở [03-cau-truc-quan-he-schema-tuple-attribute-domain.md](03-cau-truc-quan-he-schema-tuple-attribute-domain.md), ta đã nắm cấu trúc của relation gồm các tuple và attribute trong miền giá trị domain.
- **Đang giải quyết gì (Current Problem):** Một bảng không thể cho phép các dòng trùng lặp vô tội vạ hoặc các liên kết trỏ vào hư vô. Bài học này xây dựng hệ thống các loại khóa để định danh và liên kết dữ liệu, đồng thời thiết lập các rào chắn toàn vẹn dữ liệu bảo vệ tính nhất quán của CSDL.
- **Dùng đi đâu (Forward Handoff):** Khi khóa và ràng buộc toàn vẹn đã hoàn thiện, [05-dai-so-quan-he-va-giai-tich-quan-he.md](05-dai-so-quan-he-va-giai-tich-quan-he.md) sẽ triển khai các phép toán truy vấn dữ liệu: Đại số quan hệ (Select, Project, Join, Division) và Giải tích quan hệ.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng sơ đồ tập hợp lồng nhau của 5 loại khóa, bảng so sánh tính duy nhất/tối thiểu và các tùy chọn tham chiếu cha - con.
- Đọc TẦNG B để phân tích sâu ví dụ bảng thực tế minh họa từng loại khóa, cơ chế thực thi của 4 ràng buộc toàn vẹn và các kịch bản lỗi vi phạm toàn vẹn khi chạy SQL.

---

## 키의 종류 및 데이터 무결성

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Sơ đồ phân loại 5 loại Khóa cốt lõi trong đề thi

Khóa là một thuộc tính hoặc một tập hợp nhiều thuộc tính dùng để phân biệt các dòng (Tuple) khác nhau trong cùng một bảng hoặc tạo liên kết tham chiếu giữa các bảng:

```text
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
                                  │
                                  ▼ (참조 관계)
                       ┌──────────────────────┐
                       │  외래키 (Foreign Key) │ ──> Tham chiếu đến PK bảng khác
                       └──────────────────────┘
```

| Loại Khóa (키의 종류) | Tính duy nhất (유일성) | Tính tối thiểu (최소성) | Bản chất kỹ thuật & Quy tắc nhận diện |
| :--- | :---: | :---: | :--- |
| **1. 슈퍼키** (Super Key / Siêu khóa) | **Thỏa mãn** (만족) | **KHÔNG** (불만족) | Tập thuộc tính định danh duy nhất từng tuple nhưng còn chứa thuộc tính dư thừa. *(Ví dụ: `(MSSV, Họ tên)`).* |
| **2. 후보키** (Candidate Key / Khóa ứng viên) | **Thỏa mãn** (만족) | **Thỏa mãn** (만족) | **Vừa duy nhất vừa tối thiểu**. Bỏ bớt bất kỳ thuộc tính nào sẽ mất ngay tính duy nhất. *(Ví dụ: `MSSV`, `Số CCCD`)*. |
| **3. 기본키** (Primary Key / Khóa chính) | **Thỏa mãn** (만족) | **Thỏa mãn** (만족) | Được chọn từ Candidate Key làm định danh chính thức của bảng. **Bắt buộc: NOT NULL + UNIQUE**. |
| **4. 대체키** (Alternate Key / Khóa thay thế) | **Thỏa mãn** (만족) | **Thỏa mãn** (만족) | Các Candidate Key còn lại **không được chọn** làm Primary Key. *(Ví dụ: Chọn `MSSV` làm PK thì `Số CCCD` là Alternate Key)*. |
| **5. 외래키** (Foreign Key / Khóa ngoại) | *Tùy thuộc* | *Tùy thuộc* | Thuộc tính của bảng này **tham chiếu đến Primary Key** của bảng khác. Giá trị phải khớp với PK cha hoặc bằng `NULL`. |

#### 2. Các ràng buộc toàn vẹn dữ liệu cốt lõi (데이터 무결성 제약조건)

| Ràng buộc (무결성) | Tên tiếng Hàn & Anh | Quy tắc bắt buộc | Hậu quả nếu vi phạm |
| :--- | :--- | :--- | :--- |
| **Toàn vẹn thực thể** | `개체 무결성 (Entity Integrity)` | Khóa chính (PK) **không bao giờ được phép mang giá trị NULL** và **không được trùng lặp**. | Hệ thống báo lỗi từ chối thao tác INSERT/UPDATE (`ORA-00001: unique constraint violated`). |
| **Toàn vẹn tham chiếu** | `참조 무결성 (Referential Integrity)` | Khóa ngoại (FK) bắt buộc phải **bằng NULL** hoặc **khớp hoàn toàn với một giá trị PK đang tồn tại** ở bảng cha. | Không thể thêm con nếu chưa có cha; không thể tùy tiện xóa cha khi con đang tham chiếu. |
| **Toàn vẹn miền giá trị** | `도메인 무결성 (Domain Integrity)` | Giá trị của mọi thuộc tính phải thuộc miền giá trị hợp lệ (kiểu dữ liệu, độ dài, CHECK constraint). | Báo lỗi kiểu hoặc vi phạm điều kiện CHECK (ví dụ: tuổi âm, điểm thi > 10). |

#### 3. Các hành động tham chiếu khóa ngoại khi xóa/sửa (외래키 참조 조작 옵션)

Khi bản ghi cha (chứa PK) bị `DELETE` hoặc `UPDATE`, bảng con (chứa FK) sẽ phản ứng theo 1 trong 4 tùy chọn sau:

| Tùy chọn thao tác (참조 옵션) | Hành vi khi bản ghi cha bị Xóa hoặc Sửa (부모 레코드 삭제/수정 시) |
| :--- | :--- |
| **`CASCADE`** (Lan truyền / Thác đổ) | Tự động **xóa hoặc cập nhật hàng loạt** tất cả các bản ghi con tham chiếu tương ứng theo bản ghi cha. *(Ví dụ: Xóa phòng ban thì toàn bộ nhân viên thuộc phòng đó tự động bị xóa theo)*. |
| **`RESTRICT / NO ACTION`** (Cấm / Giới hạn) | Nếu vẫn còn tồn tại ít nhất một bản ghi con đang tham chiếu đến thì **cấm tuyệt đối**, báo lỗi từ chối không cho phép xóa hoặc sửa bản ghi cha. |
| **`SET NULL`** (Gán rỗng) | Cho phép xóa hoặc sửa bản ghi cha, và tự động đặt giá trị khóa ngoại ở tất cả các bản ghi con tương ứng thành **`NULL`**. |
| **`SET DEFAULT`** (Gán mặc định) | Cho phép xóa hoặc sửa bản ghi cha, và tự động đặt giá trị khóa ngoại ở tất cả các bản ghi con tương ứng thành **giá trị mặc định** đã định nghĩa từ trước. |

#### 4. Bẫy đề thi và bài tập nhận diện (시험 대비 함정 & 실전 포인트)

- **Bẫy 1: Khóa ứng viên vs Siêu khóa:**
  - *Câu hỏi:* "Tập hợp thuộc tính thỏa mãn tính duy nhất nhưng không thỏa mãn tính tối thiểu là loại khóa nào?"
  - *Đáp án đúng:* **슈퍼키 (Super Key)**. Thỏa mãn cả hai mới là **후보키 (Candidate Key)**.
- **Bẫy 2: Giá trị NULL của Khóa ngoại:**
  - *Câu hỏi:* "Khóa ngoại (Foreign Key) có bao giờ được phép mang giá trị NULL không?"
  - *Đáp án đúng:* **HOÀN TOÀN ĐƯỢC PHÉP** (trừ phi cột đó được định nghĩa thêm ràng buộc `NOT NULL`). Khóa chính mới là đối tượng tuyệt đối cấm NULL.
- **Bẫy 3: Ràng buộc khi xóa cha (CASCADE vs RESTRICT):**
  - *Câu hỏi:* "Tùy chọn nào ngăn chặn việc xóa bản ghi cha nếu còn bản ghi con tham chiếu?"
  - *Đáp án đúng:* **RESTRICT** (hoặc NO ACTION). `CASCADE` là tự động xóa lan truyền bản ghi con.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Phân biệt sâu sắc giữa Tính duy nhất (유일성) và Tính tối thiểu (최소성)

Xét bảng sinh viên: `SINH_VIEN(MSSV, SoCCCD, Email, HoTen, MaLop)`:
- **Tập hợp siêu khóa (슈퍼키 / Super Key):**
  - `{MSSV}`, `{SoCCCD}`, `{Email}`
  - `{MSSV, HoTen}`, `{MSSV, MaLop}`, `{SoCCCD, Email, HoTen}`
  - Tất cả các tập hợp trên đều phân biệt được từng sinh viên (đạt tính duy nhất `유일성`).
- **Tập hợp khóa ứng viên (후보키 / Candidate Key):**
  - Chỉ gồm các tập hợp tối thiểu: `{MSSV}`, `{SoCCCD}`, `{Email}`.
  - Tập `{MSSV, HoTen}` không phải Candidate Key vì nếu bỏ `HoTen`, một mình `{MSSV}` vẫn định danh duy nhất được từng dòng $\rightarrow$ `HoTen` là thuộc tính dư thừa làm mất tính tối thiểu (`최소성`).
- **Chọn khóa chính (기본키 / Primary Key):**
  - Người thiết kế chọn `{MSSV}` làm Primary Key vì ngắn gọn, quen thuộc và không đổi theo thời gian.
- **Khóa thay thế (대체키 / Alternate Key):**
  - Các Candidate Key còn lại chưa được chọn: `{SoCCCD}`, `{Email}`.

#### 2. Phân tích chi tiết 3 loại toàn vẹn dữ liệu

##### 2.1. Toàn vẹn thực thể (개체 무결성 / Entity Integrity)
- Bản chất: Mỗi thực thể trong thế giới thực phải tồn tại độc lập và được định danh rõ ràng.
- Ràng buộc: Cột Khóa chính không được mang giá trị `NULL`. Nếu Khóa chính gồm 2 cột `(A, B)` thì **cả A và B đều không được NULL**.

##### 2.2. Toàn vẹn tham chiếu (참조 무결성 / Referential Integrity)
- Bản chất: Quan hệ giữa hai bảng thể hiện qua Khóa ngoại. Không thể có một liên kết trỏ đến một đối tượng không có thật.
- Ví dụ: Bảng `NHAN_VIEN` có cột `MaPhong` trỏ sang bảng `PHONG_BAN(MaPhong)`. Nếu bảng `PHONG_BAN` chỉ có các phòng `P01, P02, P03` thì cột `MaPhong` của nhân viên chỉ được nhận giá trị `P01, P02, P03` hoặc nhận giá trị `NULL` (nếu nhân viên mới vào chưa được xếp phòng). Cấm tuyệt đối gán `P99`.

##### 2.3. Toàn vẹn miền giá trị (도메인 무결성 / Domain Integrity)
- Bản chất: Giá trị của một thuộc tính phải nằm trong tập hợp các giá trị hợp lệ được quy định bởi kiểu dữ liệu và ràng buộc `CHECK`.
- Ví dụ:
  - Cột `GioiTinh` chỉ nhận `'Nam'` hoặc `'Nữ'`.
  - Cột `DiemThi` có kiểu số thực với điều kiện ràng buộc `CHECK (DiemThi BETWEEN 0 AND 10)`.

---

### 복습 체크리스트
- [ ] Phân biệt rõ: Siêu khóa (Super Key) chỉ cần duy nhất; Khóa ứng viên (Candidate Key) bắt buộc vừa duy nhất vừa tối thiểu.
- [ ] Nhớ mối quan hệ: Candidate Key không được chọn làm PK thì trở thành Alternate Key (대체키).
- [ ] Thuộc lòng: 개체 무결성 cấm PK bị NULL và cấm trùng; 참조 무결성 yêu cầu FK phải khớp PK hoặc bằng NULL.
- [ ] Phân biệt 4 tùy chọn ngoại khóa: CASCADE (xóa lan truyền), RESTRICT (cấm xóa cha), SET NULL (gán con thành NULL), SET DEFAULT (gán mặc định).
- [ ] Hiểu rõ toàn vẹn miền giá trị (도메인 무결성): kiểm tra kiểu dữ liệu và điều kiện CHECK.
