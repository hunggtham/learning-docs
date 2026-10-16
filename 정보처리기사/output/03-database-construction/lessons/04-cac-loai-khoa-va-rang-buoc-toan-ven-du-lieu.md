# 키의 종류 및 데이터 무결성 (Các loại Khóa và Ràng buộc toàn vẹn dữ liệu)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống phân loại 5 loại Khóa: Siêu khóa (`슈퍼키`), Khóa ứng viên (`후보키`), Khóa chính (`기본키`), Khóa thay thế (`대체키`), Khóa ngoại (`외래키`).
- Phân biệt bản chất toán học giữa Tính duy nhất (`유일성` - xác định duy nhất 1 dòng) và Tính tối thiểu (`최소성` - không chứa thuộc tính thừa).
- Làm chủ 4 ràng buộc toàn vẹn dữ liệu: Toàn vẹn thực thể (`개체 무결성`), Toàn vẹn tham chiếu (`참조 무결성`), Toàn vẹn miền giá trị (`도메인 무결성`), và Toàn vẹn người dùng định nghĩa.
- Nắm vững 4 hành vi tham chiếu khóa ngoại khi xóa/sửa bản ghi cha: `CASCADE`, `RESTRICT`, `SET NULL`, `SET DEFAULT`.

## 핵심 키워드 (Từ khóa)
- 키 (Khóa / Key)
- 슈퍼키, 후보키 (Super Key, Candidate Key / 유일성 vs 최소성)
- 기본키, 대체키 (Primary Key, Alternate Key / NOT NULL + UNIQUE)
- 외래키 (Foreign Key / 참조 무결성)
- 데이터 무결성 (Toàn vẹn thực thể, tham chiếu, miền giá trị)
- 참조 옵션 (CASCADE, RESTRICT, SET NULL, SET DEFAULT)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Một bảng quan hệ không thể cho phép các dòng trùng lặp hoàn toàn và không thể cho phép liên kết bảng bừa bãi không kiểm soát.
- **Đang giải quyết gì (Current Problem):** Phân biệt ranh giới toán học giữa Tính duy nhất (`유일성`) và Tính tối thiểu (`최소성`) để xếp loại Super Key vs Candidate Key; đồng thời thiết lập 2 luật bất biến: Toàn vẹn thực thể (`개체 무결성` - Khóa chính không rỗng) và Toàn vẹn tham chiếu (`참조 무결성` - Khóa ngoại phải hợp lệ) cùng 4 hành vi tham chiếu (`CASCADE`, `RESTRICT`, `SET NULL`, `SET DEFAULT`).
- **Dùng đi đâu (Forward Handoff):** Khi các khóa và toàn vẹn đã được thiết lập, [05-dai-so-quan-he-va-giai-tich-quan-he.md](05-dai-so-quan-he-va-giai-tich-quan-he.md) sẽ đưa vào các phép toán thao tác dữ liệu: Đại số quan hệ (Select, Project, Join, Division) và Giải tích quan hệ.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng bảng so sánh 5 loại khóa, các bẫy trắc nghiệm về giá trị NULL của khóa ngoại và bảng 4 tùy chọn tham chiếu cha-con.
- Đọc TẦNG B để hiểu sâu bản chất toán học của tính tối thiểu, chi tiết 4 ràng buộc toàn vẹn và các kịch bản thực thi trong hệ thống cơ sở dữ liệu.

---

## 키의 종류 및 데이터 무결성

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 5 loại Khóa cốt lõi trong đề thi

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

| Loại Khóa (키의 종류) | Tính duy nhất (유일성) | Tính tối thiểu (최소성) | Bản chất kỹ thuật & Quy tắc nhận diện |
| :--- | :---: | :---: | :--- |
| **1. 슈퍼키** (Super Key / Siêu khóa) | **Thỏa mãn** (만족) | **KHÔNG** (불만족) | Tập thuộc tính định danh duy nhất từng tuple nhưng còn chứa thuộc tính thừa thãi. *(Ví dụ: `(MSSV, Họ tên)`).* |
| **2. 후보키** (Candidate Key / Khóa ứng viên) | **Thỏa mãn** (만족) | **Thỏa mãn** (만족) | **Vừa duy nhất vừa tối thiểu**. Nếu bỏ bớt bất kỳ thuộc tính nào thì mất ngay tính duy nhất. *(Ví dụ: `MSSV`, `Số CCCD`)*. |
| **3. 기본키** (Primary Key / Khóa chính) | **Thỏa mãn** (만족) | **Thỏa mãn** (만족) | Được chọn từ tập Candidate Key làm định danh chính thức của bảng. **Bắt buộc: NOT NULL + UNIQUE**. |
| **4. 대체키** (Alternate Key / Khóa thay thế) | **Thỏa mãn** (만족) | **Thỏa mãn** (만족) | Các Candidate Key còn lại **không được chọn** làm Primary Key. *(Ví dụ: Chọn `MSSV` làm PK thì `Số CCCD` là Alternate Key)*. |
| **5. 외래키** (Foreign Key / Khóa ngoại) | *Tùy thuộc* | *Tùy thuộc* | Thuộc tính của bảng này **tham chiếu đến Primary Key** của bảng khác. Giá trị phải khớp với PK cha hoặc bằng `NULL`. |

#### 2. Các hành động tham chiếu khóa ngoại khi xóa/sửa (외래키 참조 조작 옵션)

| Tùy chọn thao tác (참조 옵션) | Hành vi khi bản ghi cha bị Xóa hoặc Sửa (부모 레코드 삭제/수정 시) |
| :--- | :--- |
| **`CASCADE`** (Lan truyền / Thác đổ) | Tự động **xóa hoặc cập nhật hàng loạt** tất cả các bản ghi con tham chiếu tương ứng theo bản ghi cha. *(Ví dụ: Xóa phòng ban thì toàn bộ nhân viên thuộc phòng đó tự động bị xóa theo)*. |
| **`RESTRICT / NO ACTION`** (Cấm / Giới hạn) | Nếu vẫn còn tồn tại ít nhất một bản ghi con đang tham chiếu đến thì **cấm tuyệt đối**, báo lỗi từ chối không cho phép xóa hoặc sửa bản ghi cha. |
| **`SET NULL`** (Gán rỗng) | Cho phép xóa hoặc sửa bản ghi cha, và tự động đặt giá trị khóa ngoại ở tất cả các bản ghi con tương ứng thành **`NULL`**. |
| **`SET DEFAULT`** (Gán mặc định) | Cho phép xóa hoặc sửa bản ghi cha, và tự động đặt giá trị khóa ngoại ở tất cả các bản ghi con tương ứng thành **giá trị mặc định** đã định nghĩa từ trước. |

#### 3. Bẫy đề thi và bài tập nhận diện (시험 대비 함정 & 실전 포인트)

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

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Phân biệt sâu sắc giữa Tính duy nhất (유일성) và Tính tối thiểu (최소성)

- **유일성 (Uniqueness / Tính duy nhất):**
  - Mệnh đề: Không bao giờ có 2 tuple khác nhau có cùng giá trị trên tập thuộc tính khóa.
  - Phân tích: Nếu biết giá trị của khóa, ta truy xuất được **chính xác duy nhất 1 dòng**.
- **최소성 (Minimality / Tính tối thiểu):**
  - Mệnh đề: Tập thuộc tính khóa không được chứa bất kỳ thuộc tính nào dư thừa. Nếu loại bỏ bất kỳ thuộc tính nào khỏi tập hợp đó, tính duy nhất sẽ bị phá vỡ.
  - Ví dụ phản chứng: `(MSSV)` đã đủ để xác định duy nhất sinh viên. Nếu ta lấy `(MSSV, Số điện thoại)` làm khóa thì tập hợp này vẫn có tính duy nhất (vì có MSSV), nhưng **vi phạm tính tối thiểu** vì `Số điện thoại` là thuộc tính thừa $\rightarrow$ Đây là **Super Key**, KHÔNG PHẢI Candidate Key.

#### 2. Các ràng buộc toàn vẹn dữ liệu (데이터베이스 무결성 제약조건)

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

1. **Toàn vẹn thực thể (개체 무결성 / Entity Integrity):** Khóa chính (Primary Key) trong mọi trường hợp không bao giờ được nhận giá trị `NULL` và không được phép trùng lặp giá trị.
2. **Toàn vẹn tham chiếu (참조 무결성 / Referential Integrity):** Giá trị của Khóa ngoại (Foreign Key) phải khớp hoàn toàn với một giá trị Khóa chính đang tồn tại ở bảng cha được tham chiếu, hoặc phải mang giá trị `NULL`.
3. **Toàn vẹn miền giá trị (도메인 무결성 / Domain Integrity):** Giá trị của từng thuộc tính bắt buộc phải là giá trị nguyên tử nằm trong tập hợp các giá trị hợp lệ đã định nghĩa của miền đó.
4. **Toàn vẹn do người dùng định nghĩa (사용자 정의 무결성 / User-defined Integrity):** Các quy tắc nghiệp vụ đặc thù do lập trình viên hoặc DBA thiết lập thông qua điều kiện `CHECK`, `TRIGGER` hoặc `ASSERTION`.

---

### 복습 체크리스트
- [ ] Phân biệt rõ: Siêu khóa (Super Key) chỉ cần duy nhất; Khóa ứng viên (Candidate Key) bắt buộc vừa duy nhất vừa tối thiểu.
- [ ] Nhớ mối quan hệ: Candidate Key không được chọn làm PK thì trở thành Alternate Key (대체키).
- [ ] Thuộc lòng: 개체 무결성 cấm PK bị NULL và cấm trùng; 참조 무결성 yêu cầu FK phải khớp PK hoặc bằng NULL.
- [ ] Phân biệt 4 tùy chọn ngoại khóa: CASCADE (xóa lan truyền), RESTRICT (cấm xóa), SET NULL (gán rỗng), SET DEFAULT (gán mặc định).
