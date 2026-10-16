# 데이터 모델 및 E-R 다이어그램 (Mô hình dữ liệu và Biểu đồ E-R)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 thành phần cấu thành mô hình dữ liệu: Cấu trúc (`구조` - tĩnh), Thao tác (`연산` - động), Ràng buộc (`제약 조건` - quy tắc toàn vẹn).
- Nhận diện và vẽ chuẩn xác các ký hiệu chuẩn Peter Chen: Thực thể (chữ nhật), Thực thể yếu (chữ nhật kép), Quan hệ (thoi), Thuộc tính (elip), Khóa chính (elip gạch chân), Thuộc tính đa trị (elip kép), Thuộc tính suy diễn/dẫn xuất (elip nét đứt).
- Phân biệt ký pháp Peter Chen cổ điển và ký pháp Chân quạ IE Crow's foot (새발 표기법) phổ biến trong thiết kế thực tế và các công cụ CASE.
- Làm chủ khái niệm Bản số (Cardinality: 1:1, 1:N, N:M) và Tính tham gia bắt buộc/tùy chọn (Optionality / Participation: Mandatory vs Optional) thông qua 4 ký hiệu đầu mút Crow's foot (`||`, `O|`, `|<`, `O<`).
- Nắm vững quy tắc vàng ánh xạ biểu đồ E-R sang bảng quan hệ: 1:1, 1:N (đưa PK bên 1 sang làm FK bên N), và N:M (bắt buộc tạo bảng trung gian với PK phức hợp).

## 핵심 키워드 (Từ khóa)
- 데이터 모델 (Mô hình dữ liệu / Data Model)
- 구조, 연산, 제약 조건 (Cấu trúc, Thao tác, Ràng buộc toàn vẹn)
- E-R 다이어그램 (Biểu đồ E-R / Entity-Relationship Diagram / 피터 첸 표기법)
- 새발 표기법 (Ký pháp chân quạ / IE Crow's Foot Notation / Information Engineering)
- 개체, 관계, 속성 (Thực thể, Mối quan hệ, Thuộc tính)
- 다중값 속성 (Thuộc tính đa trị / Multivalued Attribute / 이중 타원)
- 유도 속성 (Thuộc tính suy diễn / Derived Attribute / 점선 타원)
- 카디널리티 (Bản số / Cardinality: 1, N, M)
- 참여도 / 선택도 (Tính tham gia: 필수 참여 Mandatory vs 선택 참여 Optional)
- 관계 매핑 (Ánh xạ quan hệ / 교차 테이블 Junction Table)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở [01-quy-trinh-thiet-ke-csdl-khai-niem-logic-vat-ly.md](01-quy-trinh-thiet-ke-csdl-khai-niem-logic-vat-ly.md), ta biết rằng sản phẩm cốt lõi của Thiết kế khái niệm là Lược đồ khái niệm (`개념 스키마`), biểu diễn qua biểu đồ E-R hoàn toàn độc lập với DBMS.
- **Đang giải quyết gì (Current Problem):** Chuẩn hóa cách biểu diễn thế giới thực thành các hình học chuẩn (Peter Chen và IE Crow's foot), mô tả chính xác bản số và sự ràng buộc tham gia của các thực thể, đồng thời cung cấp thuật toán ánh xạ các mối quan hệ (1:1, 1:N, N:M) sang bảng quan hệ logic mà không làm mất mát ngữ nghĩa.
- **Dùng đi đâu (Forward Handoff):** Khi các bảng được sinh ra từ biểu đồ E-R, [03-cau-truc-quan-he-schema-tuple-attribute-domain.md](03-cau-truc-quan-he-schema-tuple-attribute-domain.md) sẽ mổ xẻ cấu trúc chi tiết của bảng quan hệ (Tuple, Attribute, Domain, Bậc Degree và Lực lượng Cardinality của quan hệ).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm chắc bảng đối chiếu ký hiệu Peter Chen vs Crow's foot, ý nghĩa 4 tổ hợp ký hiệu chân quạ và quy tắc chuyển đổi quan hệ sang bảng.
- Đọc TẦNG B để phân tích sâu cơ chế thuộc tính suy diễn (Derived Attribute), bản số chi tiết (Min, Max) và bài tập tình huống thực tế thường gặp trong đề thi.

---

## 데이터 모델 및 E-R 다이어그램

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Ký pháp Peter Chen trong đề thi (피터 첸 표기법)

Biểu đồ thực thể - mối quan hệ (**E-R 다이어그램** / Entity-Relationship Diagram) do Peter Chen đề xuất năm 1976 là chuẩn mực biểu diễn dữ liệu ở tầng khái niệm trong kỳ thi 정보처리기사:

```text
       ┌───────────────┐
       │     개체      │ ──> Hình chữ nhật (직사각형): Thực thể mạnh (Strong Entity)
       └───────┬───────┘
       ╔═══════╧═══════╗
       ║   약한 개체   ║ ──> Hình chữ nhật kép (이중 직사각형): Thực thể yếu (Weak Entity)
       ╚═══════════════╝
               │
               ▼
       ┌───────────────┐
       │   기본키 속성 │ ──> Hình elip có gạch chân (밑줄 타원): Thuộc tính khóa chính (PK)
       └───────────────┘
               │
               ▼
          ◇  관계     ──> Hình thoi (마름모): Mối quan hệ giữa các thực thể (Relationship)
               │
          ◈ 식별 관계  ──> Hình thoi kép (이중 마름모): Quan hệ xác định cho thực thể yếu
               │
               ▼
        (( 다중값 속성 )) ──> Hình elip kép (이중 타원): Thuộc tính đa trị (Multivalued Attribute)
               │
               ▼
        - - ( 유도 속성 ) - - ──> Hình elip nét đứt (점선 타원): Thuộc tính suy diễn / dẫn xuất (Derived)
```

| Ký hiệu Peter Chen | Tên tiếng Hàn & Anh | Ý nghĩa kỹ thuật | Ví dụ thực tế |
| :--- | :--- | :--- | :--- |
| **Hình chữ nhật** (직사각형) | `개체 (Entity)` | Đối tượng độc lập trong thế giới thực cần quản lý dữ liệu. | `Học sinh (학생)`, `Khách hàng (고객)` |
| **Hình chữ nhật kép** (이중 직사각형) | `약한 개체 (Weak Entity)` | Thực thể không thể tồn tại độc lập nếu thiếu thực thể cha. | `Thân nhân (가족)`, `Phòng khách sạn` |
| **Hình thoi** (마름모) | `관계 (Relationship)` | Mối liên hệ logic giữa các thực thể. | `Đăng ký (수강)`, `Đặt hàng (주문)` |
| **Hình thoi kép** (이중 마름모) | `식별 관계 (Identifying Rel)` | Mối quan hệ nối thực thể mạnh với thực thể yếu. | `Nhân viên` $\leftrightarrow$ `Thân nhân` |
| **Hình elip** (타원) | `속성 (Attribute)` | Đặc tính chi tiết mô tả thực thể hoặc quan hệ. | `Họ tên (이름)`, `Địa chỉ (주소)` |
| **Hình elip có gạch chân** (밑줄 타원) | `기본키 (Primary Key)` | Thuộc tính định danh duy nhất cho từng bản ghi. | `Mã SV (학번)`, `Mã đơn hàng (주문번호)` |
| **Hình elip kép** (이중 타원) | `다중값 속성 (Multivalued)` | Thuộc tính có thể chứa nhiều giá trị cùng lúc. | `Số điện thoại (전화번호)`, `Sở thích` |
| **Hình elip nét đứt** (점선 타원) | `유도 속성 (Derived Attribute)` | Giá trị được tính toán từ các thuộc tính khác. | `Tuổi (나이)` (tính từ ngày sinh), `Thành tiền` |
| **Hình elip phân nhánh** (복합 속성) | `복합 속성 (Composite)` | Thuộc tính lớn chia nhỏ thành nhiều phần. | `Địa chỉ (주소)` $\rightarrow$ `Tỉnh, Huyện, Xã` |

#### 2. Ký pháp Chân quạ IE (새발 표기법 / Information Engineering Crow's Foot)

Trong thiết kế CSDL hiện đại và đề thi ứng dụng, ký pháp IE Crow's Foot được sử dụng phổ biến với các ký hiệu đầu mút đường quan hệ:

```text
Ký hiệu đầu mút Crow's Foot:
  ──||──   Mandatory One (Bắt buộc duy nhất một: Min=1, Max=1)
  ──O|──   Optional One (Tùy chọn một: Min=0, Max=1)
  ──|<──   Mandatory Many (Bắt buộc nhiều: Min=1, Max=N)
  ──O<──   Optional Many (Tùy chọn nhiều: Min=0, Max=N)
```

| Ký hiệu IE | Tên gọi chuẩn đề thi | Bản số (Min, Max) | Ý nghĩa nghiệp vụ |
| :--- | :--- | :--- | :--- |
| `──||──` | **필수 1 (Mandatory One)** | Min = 1, Max = 1 | Bắt buộc phải có đúng 1 thể hiện liên kết (không được trống, không được nhiều hơn 1). |
| `──O|──` | **선택 1 (Optional One)** | Min = 0, Max = 1 | Có thể không có hoặc có tối đa 1 thể hiện liên kết (ví dụ: Nhân viên có thể chưa có xe công ty). |
| `──|<──` | **필수 다중 (Mandatory Many)** | Min = 1, Max = N | Bắt buộc phải có ít nhất 1 và có thể có nhiều thể hiện liên kết (ví dụ: Đơn hàng phải có ít nhất 1 món). |
| `──O<──` | **선택 다중 (Optional Many)** | Min = 0, Max = N | Có thể không có hoặc có nhiều thể hiện liên kết (ví dụ: Khách hàng mới có thể chưa mua đơn hàng nào). |

#### 3. Quy tắc ánh xạ E-R sang lược đồ quan hệ (E-R to Relational Mapping)

```text
[Sơ đồ E-R Khái niệm] ───────────────────────────> [Lược đồ Bảng Quan hệ (Logic)]
- Thực thể (Entity)   ── biến thành ──> Bảng (Table / Relation)
- Thuộc tính (Attribute) ── biến thành ──> Cột (Column / Field)
- Khóa chính (PK)     ── biến thành ──> Khóa chính của bảng (Primary Key)
```

##### 1. Quan hệ 1:1 (1대1 관계)
- Lấy Khóa chính của Thực thể bên này đưa sang làm Khóa ngoại (Foreign Key) ở Thực thể bên kia, hoặc gộp cả hai thực thể thành một Bảng duy nhất nếu mối quan hệ là bắt buộc cả hai phía (`||` cả hai đầu).

##### 2. Quan hệ 1:N (1대N 관계)
- **Quy tắc sống còn:** **Luôn đưa Khóa chính của phía "1" sang làm Khóa ngoại (Foreign Key) ở phía "N"**.
- Phía "N" có nhiều bản ghi, mỗi bản ghi chỉ tham chiếu về đúng 1 bản ghi của phía "1", đảm bảo tính nguyên tử (1NF).

##### 3. Quan hệ N:M (N대M 다대다 관계)
- **Quy tắc sống còn:** **Bắt buộc phải tách thành một Bảng trung gian (Junction Table / 교차 테이블 / 관계 테이블)**.
- Bảng trung gian chứa Khóa chính của cả hai thực thể tham gia. Hai khóa này kết hợp lại tạo thành Khóa chính phức hợp (Composite Primary Key), đồng thời mỗi khóa đơn lẻ đóng vai trò là Khóa ngoại (Foreign Key).

#### 4. Bẫy đề thi kinh điển (시험 대비 함정 포인트)
- **Bẫy 1: Phân biệt elip kép vs elip nét đứt:**
  - Elip kép (`이중 타원`): Thuộc tính đa trị (`다중값 속성` - chứa danh sách nhiều giá trị).
  - Elip nét đứt (`점선 타원`): Thuộc tính suy diễn/dẫn xuất (`유도 속성` - không lưu trực tiếp mà tính toán từ cột khác).
- **Bẫy 2: Số bảng tối thiểu khi chuyển quan hệ N:M:**
  - Đề thi hỏi: *"Chuyển đổi 2 thực thể có mối quan hệ N:M sang mô hình dữ liệu quan hệ thì cần tối thiểu bao nhiêu bảng?"*
  - **Đáp án đúng:** **3 bảng** (Bảng A + Bảng B + Bảng liên kết trung gian).
- **Bẫy 3: Ký hiệu Chân quạ (Crow's foot) đọc theo chiều nào:**
  - Ký hiệu gần thực thể đích biểu diễn bản số của thực thể đích đối với thực thể gốc: Vòng tròn `O` là số 0 (Optional, Min=0); Vạch đứng `|` là số 1; Nhánh quạ `<` là nhiều (N).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Ba yếu tố cấu thành mô hình dữ liệu (데이터 모델의 3대 요소)

Mọi mô hình dữ liệu trong khoa học máy tính đều phải biểu diễn đầy đủ 3 thành phần cơ bản:

```text
                  ┌────────────────────────────────────────┐
                  │      데이터 모델의 3대 표시 요소       │
                  │ (3 thành phần cốt lõi của Data Model)  │
                  └──────────────────┬─────────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
  1. 구조 (Structure)         2. 연산 (Operation)        3. 제약 조건 (Constraint)
  - Tĩnh (정적 특성)           - Động (동적 특성)           - Quy tắc logic
  - Kiểu dữ liệu, cấu trúc     - SELECT, INSERT, UPDATE     - Khóa chính, Khóa ngoại
  - Mối quan hệ giữa thực thể  - Thao tác xử lý dữ liệu     - Miền giá trị (Domain)
```

| Thành phần (요소) | Tính chất (성격) | Bản chất kỹ thuật (기술적 본질) | Ví dụ minh họa (예시) |
| :--- | :--- | :--- | :--- |
| **1. 구조 (Structure)** | **Tính chất tĩnh** (정적 특성) | Định nghĩa cấu trúc logic của dữ liệu, các kiểu thực thể và mối quan hệ cấu trúc giữa các đối tượng. | Bảng `SINH_VIEN` gồm các cột `MSSV`, `HoTen`, quan hệ với bảng `LOP_HOC`. |
| **2. 연산 (Operation)** | **Tính chất động** (동적 특성) | Các thao tác thực tế tác động lên giá trị dữ liệu được lưu trong cơ sở dữ liệu để tìm kiếm hoặc biến đổi. | Các phép toán Đại số quan hệ ($\sigma, \pi, \bowtie$), các câu lệnh DML (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). |
| **3. 제약 조건 (Constraint)** | **Quy tắc toàn vẹn** (무결성 규칙) | Các ràng buộc logic mà giá trị dữ liệu thực tế bắt buộc phải tuân theo để đảm bảo tính đúng đắn và nhất quán. | Khóa chính không được trùng lặp và không được `NULL`, điểm số phải nằm trong khoảng $0 \le \text{Điểm} \le 10$. |

#### 2. Phân tích chi tiết Bản số (Cardinality) và Tham gia (Optionality)

##### 2.1. Cặp giá trị (Min, Max)
Trong mô hình thực thể quan hệ nâng cao, mỗi đầu mối quan hệ được gắn một cặp bản số `(Min, Max)`:
- `Min = 0`: Tham gia tùy chọn (`선택 참여` - Optional). Một thực thể có thể tồn tại mà không cần liên kết với thực thể kia.
- `Min = 1`: Tham gia bắt buộc (`필수 참여` - Mandatory). Mọi thể hiện của thực thể bắt buộc phải liên kết với ít nhất một thể hiện của thực thể kia.
- `Max = 1`: Tối đa 1 liên kết (Single).
- `Max = N` hoặc `*`: Tối đa nhiều liên kết (Many).

##### 2.2. Minh họa bằng hệ thống Thương mại điện tử (E-Commerce)
Xét quan hệ giữa `Khách hàng (고객)` và `Đơn hàng (주문)`:
- Một Khách hàng có thể vừa tạo tài khoản và chưa mua hàng bao giờ $\rightarrow$ `Min = 0`. Một khách hàng có thể mua nhiều đơn hàng $\rightarrow$ `Max = N`. Đầu phía Đơn hàng là: `선택 다중 (0, N)` hoặc ký hiệu Crow's foot `──O<──`.
- Một Đơn hàng khi đã tạo ra bắt buộc phải thuộc về đúng 1 Khách hàng $\rightarrow$ `Min = 1, Max = 1`. Đầu phía Khách hàng là: `필수 1 (1, 1)` hoặc ký hiệu Crow's foot `──||──`.

```text
[고객 (Khách hàng)] ──────||───────────────O<────── [주문 (Đơn hàng)]
                   (Đúng 1 khách)     (0 hoặc nhiều đơn)
```

#### 3. Ví dụ thực hành chi tiết ánh xạ quan hệ

##### Ví dụ quan hệ 1:N: Khoa $\leftrightarrow$ Sinh viên
- `Khoa (학과)` (1) $\leftrightarrow$ `Sinh viên (학생)` (N).
  - Bảng `KHOA(ma_khoa, ten_khoa)` (PK: `ma_khoa`).
  - Bảng `SINH_VIEN(ma_sv, ho_ten, ma_khoa)` (`ma_khoa` là Foreign Key trỏ về `KHOA`).

##### Ví dụ quan hệ N:M: Sinh viên $\leftrightarrow$ Môn học
- `Sinh viên (학생)` (N) $\leftrightarrow$ `Môn học (과목)` (M) qua quan hệ `Đăng ký (수강)`.
  - Bảng `SINH_VIEN(ma_sv, ho_ten)`
  - Bảng `MON_HOC(ma_mh, ten_mh)`
  - Bảng trung gian `DANG_KY(ma_sv, ma_mh, diem_so)` $\rightarrow$ Khóa chính là tổ hợp `(ma_sv, ma_mh)`, đồng thời `ma_sv` là FK tham chiếu `SINH_VIEN`, `ma_mh` là FK tham chiếu `MON_HOC`.

---

### 복습 체크리스트
- [ ] Thuộc 3 thành phần của mô hình dữ liệu: Cấu trúc (`구조` - tĩnh), Thao tác (`연산` - động), Ràng buộc (`제약 조건` - quy tắc).
- [ ] Phân biệt đầy đủ 7 ký hiệu Peter Chen: Thực thể mạnh (Chữ nhật), Thực thể yếu (Chữ nhật kép), Quan hệ (Thoi), Quan hệ xác định (Thoi kép), Thuộc tính (Elip), Khóa chính (Elip gạch chân), Thuộc tính đa trị (Elip kép), Thuộc tính suy diễn (Elip nét đứt).
- [ ] Đọc và giải thích được 4 ký hiệu chân quạ IE Crow's foot: `||` (Mandatory 1), `O|` (Optional 1), `|<` (Mandatory Many), `O<` (Optional Many).
- [ ] Nắm vững quy tắc chuyển đổi: Quan hệ 1:N đưa PK bên 1 sang làm FK bên N; Quan hệ N:M bắt buộc tạo bảng trung gian có PK phức hợp gồm 2 FK.
