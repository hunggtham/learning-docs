# Môn 3 · Bài 02 — Mô hình dữ liệu và Biểu đồ E-R
# 제3과목: 데이터베이스 구축 — 데이터 모델의 3대 요소 및 E-R 다이어그램

> **Mạch đọc:** Tiếp nối từ [Bài 01](01-quy-trinh-thiet-ke-csdl-khai-niem-logic-vat-ly.md), sau khi nắm vững 5 giai đoạn thiết kế CSDL, bài học này đi sâu vào trọng tâm của giai đoạn Thiết kế khái niệm (`개념적 설계`) và mở đầu Thiết kế logic (`논리적 설계`). Đó là 3 thành phần cấu thành mô hình dữ liệu (`구조 - 연산 - 제약 조건`), ký hiệu chuẩn của biểu đồ E-R (Peter Chen notation) và quy tắc vàng chuyển đổi biểu đồ E-R thành bảng quan hệ.

> **Mạch kết nối 3 bước (3-part Bridge):**
> - **Từ đâu (Khởi đầu):** Ở Bài 01, ta biết rằng sản phẩm cốt lõi của Thiết kế khái niệm là Lược đồ khái niệm (`개념 스키마`), biểu diễn qua biểu đồ E-R hoàn toàn độc lập với DBMS.
> - **Đang giải quyết gì (Bản chất hiện tại):** Chuẩn hóa cách vẽ thế giới thực thành các hình học chuẩn (Entity = Hình chữ nhật, Attribute = Hình elip, Relationship = Hình thoi) và giải quyết bài toán cốt lõi: Làm sao ánh xạ các mối quan hệ 1:1, 1:N, N:M thành các bảng vật lý mà không bị mất mát thông tin hay dư thừa dữ liệu.
> - **Dùng đi đâu (Đích đến tiếp theo):** Khi các bảng được sinh ra từ biểu đồ E-R, [Bài 03](03-cau-truc-quan-he-schema-tuple-attribute-domain.md) sẽ mổ xẻ cấu trúc chi tiết của bảng quan hệ (Tuple, Attribute, Domain và tính độc lập của 3 tầng lược đồ Schema).

---

## 1. Ba yếu tố cấu thành mô hình dữ liệu (데이터 모델에 표시할 3대 요소)

Mọi mô hình dữ liệu trong khoa học máy tính đều phải biểu diễn đầy đủ 3 thành phần cơ bản:

```
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

### 1.1. Bảng phân tích chi tiết 3 yếu tố

| Thành phần (요소) | Tính chất (성격) | Bản chất kỹ thuật (기술적 본질) | Ví dụ minh họa (예시) |
| :--- | :--- | :--- | :--- |
| **1. 구조 (Structure)** | **Tính chất tĩnh**<br>(정적 특성) | Định nghĩa cấu trúc logic của dữ liệu, các kiểu thực thể và mối quan hệ cấu trúc giữa các đối tượng. | Bảng `SINH_VIEN` gồm các cột `MSSV`, `HoTen`, quan hệ với bảng `LOP_HOC`. |
| **2. 연산 (Operation)** | **Tính chất động**<br>(동적 특성) | Các thao tác thực tế tác động lên giá trị dữ liệu được lưu trong cơ sở dữ liệu để tìm kiếm hoặc biến đổi. | Các phép toán Đại số quan hệ ($\sigma, \pi, \bowtie$), các câu lệnh DML (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). |
| **3. 제약 조건 (Constraint)** | **Quy tắc toàn vẹn**<br>(무결성 규칙) | Các ràng buộc logic mà giá trị dữ liệu thực tế bắt buộc phải tuân theo để đảm bảo tính đúng đắn và nhất quán. | Khóa chính không được trùng lặp và không được `NULL`, điểm số phải nằm trong khoảng $0 \le \text{Điểm} \le 10$. |

---

## 2. Biểu đồ E-R và Ký hiệu chuẩn Peter Chen (E-R 다이어그램 표기법)

Biểu đồ thực thể - mối quan hệ (**E-R 다이어그램** / Entity-Relationship Diagram) do Peter Chen đề xuất năm 1976 là chuẩn mực biểu diễn dữ liệu ở tầng khái niệm.

```
       ┌───────────────┐
       │     개체      │ ──> Hình chữ nhật (직사각형): Thực thể (Entity)
       │   (Entity)    │
       └───────┬───────┘
               │
               ▼
       ┌───────────────┐
       │   기본키 속성 │ ──> Hình elip có gạch chân (밑줄 타원): Thuộc tính khóa chính
       └───────────────┘
               │
               ▼
          ◇  관계     ──> Hình thoi (마름모): Mối quan hệ giữa các thực thể (Relationship)
               │
               ▼
        (( 다중값 속성 )) ──> Hình elip kép (이중 타원): Thuộc tính đa trị (Multivalued)
```

### 2.1. Bảng ký hiệu chuẩn Peter Chen trong đề thi

| Ký hiệu hình học (도형) | Thuật ngữ gốc (원문) | Ý nghĩa kỹ thuật | Ví dụ thực tế |
| :--- | :--- | :--- | :--- |
| **Hình chữ nhật**<br>(직사각형) | `개체 (Entity)` | Đối tượng độc lập trong thế giới thực cần quản lý dữ liệu. | `Học sinh (학생)`, `Giảng viên (교수)`, `Môn học (과목)` |
| **Hình thoi**<br>(마름모) | `관계 (Relationship)` | Mối liên hệ logic giữa hai hoặc nhiều thực thể. | `Đăng ký học (수강)`, `Giảng dạy (강의)`, `Thuộc về (소속)` |
| **Hình elip**<br>(타원) | `속성 (Attribute)` | Đặc tính chi tiết mô tả thực thể hoặc mối quan hệ. | `Họ tên (이름)`, `Địa chỉ (주소)`, `Ngày sinh (생년월일)` |
| **Hình elip có gạch chân**<br>(밑줄 타원) | `기본키 속성 (Primary Key)` | Thuộc tính định danh duy nhất cho từng thể hiện của thực thể. | `Mã sinh viên (학번)`, `Số CMND/CCCD (주민번호)` |
| **Hình elip kép**<br>(이중 타원) | `다중값 속성 (Multivalued)` | Thuộc tính có thể chứa nhiều giá trị cùng lúc cho 1 thực thể. | `Số điện thoại (전화번호)` (một người có 2-3 số) |
| **Hình elip phân nhánh**<br>(복합 속성) | `복합 속성 (Composite)` | Thuộc tính lớn có thể chia nhỏ thành các thuộc tính độc lập. | `Địa chỉ (주소)` $\rightarrow$ `Thành phố`, `Quận/Huyện`, `Số nhà` |
| **Đường nối thẳng**<br>(선 / Line) | `연결 (Link)` | Nối giữa Thực thể với Quan hệ, hoặc Thực thể với Thuộc tính. | Đường nối kèm tỷ lệ tham gia: `1:1`, `1:N`, hoặc `N:M` |

---

## 3. Quy tắc ánh xạ E-R sang lược đồ quan hệ (E-R to Relational Mapping)

Đây là nội dung chuyển giao cốt lõi từ Thiết kế khái niệm sang Thiết kế logic:

```
[Sơ đồ E-R Khái niệm] ───────────────────────────> [Lược đồ Bảng Quan hệ (Logic)]
- Thực thể (Entity)   ── biến thành ──> Bảng (Table / Relation)
- Thuộc tính (Attribute) ── biến thành ──> Cột (Column / Field)
- Khóa chính (PK)     ── biến thành ──> Khóa chính của bảng (Primary Key)
```

### 3.1. Ánh xạ các kiểu quan hệ (관계 매핑 규칙)

#### 1. Quan hệ 1:1 (1대1 관계)
- **Quy tắc:** Lấy Khóa chính của Thực thể bên này đưa sang làm Khóa ngoại (Foreign Key) ở Thực thể bên kia, hoặc gộp cả hai thực thể thành một Bảng duy nhất nếu mối quan hệ là bắt buộc cả hai phía.
- **Ví dụ:** Thực thể `Hôn phu` (1) $\leftrightarrow$ `Hôn thê` (1). Ta có thể đưa `Mã_hôn_phu` vào làm khóa ngoại trong bảng `HON_THE`.

#### 2. Quan hệ 1:N (1대N 관계)
- **Quy tắc sống còn:** **Luôn đưa Khóa chính của phía "1" sang làm Khóa ngoại (Foreign Key) ở phía "N"**.
- **Lý do kỹ thuật:** Phía "N" có nhiều bản ghi, mỗi bản ghi chỉ tham chiếu về đúng 1 bản ghi của phía "1", đảm bảo không bị lặp mảng giá trị (vi phạm 1NF).
- **Ví dụ:** `Khoa (학과)` (1) $\leftrightarrow$ `Sinh viên (학생)` (N).
  - Bảng `KHOA(ma_khoa, ten_khoa)` (PK: `ma_khoa`).
  - Bảng `SINH_VIEN(ma_sv, ho_ten, ma_khoa)` (`ma_khoa` là Foreign Key trỏ về `KHOA`).

#### 3. Quan hệ N:M (N대M 다대다 관계)
- **Quy tắc sống còn:** **Bắt buộc phải tách thành một Bảng trung gian (Junction Table / 교차 테이블 / 관계 테이블)**.
- **Cấu trúc bảng trung gian:**
  - Chứa Khóa chính của cả hai thực thể tham gia. Hai khóa này kết hợp lại tạo thành Khóa chính phức hợp (Composite Primary Key), đồng thời mỗi khóa đơn lẻ đóng vai trò là Khóa ngoại (Foreign Key) tham chiếu về bảng gốc tương ứng.
  - Có thể chứa thêm các thuộc tính riêng của mối quan hệ (ví dụ: ngày đăng ký, điểm thi).
- **Ví dụ:** `Sinh viên (학생)` (N) $\leftrightarrow$ `Môn học (과목)` (M) qua quan hệ `Đăng ký (수강)`.
  - Bảng `SINH_VIEN(ma_sv, ho_ten)`
  - Bảng `MON_HOC(ma_mh, ten_mh)`
  - Bảng trung gian `DANG_KY(ma_sv, ma_mh, diem_so)` $\rightarrow$ Khóa chính là tổ hợp `(ma_sv, ma_mh)`.

---

## 4. Bẫy đề thi và bài tập nhận diện (시험 대비 함정 & 실전 포인트)

### 4.1. Bẫy đề thi trắc nghiệm (기출 함정)
- **Bẫy 1: Ký hiệu 다중값 속성 (Multivalued Attribute):**
  - Đề thi hay hỏi: *"Ký hiệu nào biểu diễn thuộc tính có thể mang nhiều giá trị (như số điện thoại, bằng cấp)?"*
  - **Đáp án đúng:** **Hình elip kép (이중 타원)**. Bẫy sai thường đưa ra *Hình elip nét đứt* (thuộc tính dẫn xuất) hoặc *Hình chữ nhật kép* (thực thể yếu).
- **Bẫy 2: Ánh xạ quan hệ 1:N:**
  - Đề thi hỏi: *"Trong quan hệ 1:N giữa Phòng ban và Nhân viên, khóa ngoại được đặt ở đâu?"*
  - **Đáp án đúng:** Đặt ở bảng **Nhân viên (phía N)**. Không bao giờ đặt ở bảng Phòng ban (phía 1) vì sẽ vi phạm tính nguyên tử của thuộc tính.
- **Bẫy 3: Đòi hỏi của quan hệ N:M:**
  - *"Một quan hệ N:M trong sơ đồ E-R khi chuyển sang mô hình quan hệ cần tối thiểu bao nhiêu bảng?"*
  - **Đáp án đúng:** **3 bảng** (2 bảng cho 2 thực thể + 1 bảng quan hệ trung gian).

---

## 5. Checklist ôn thi (복습 체크리스트)

- [ ] Thuộc 3 thành phần của mô hình dữ liệu: Cấu trúc (`구조` - tĩnh), Thao tác (`연산` - động), Ràng buộc (`제약 조건` - quy tắc).
- [ ] Nhận diện 5 ký hiệu Peter Chen: Thực thể (Chữ nhật), Quan hệ (Thoi), Thuộc tính (Elip), Khóa chính (Elip gạch chân), Thuộc tính đa trị (Elip kép).
- [ ] Nhớ quy tắc chuyển đổi: Quan hệ 1:N đưa PK bên 1 sang làm FK bên N; Quan hệ N:M tạo bảng trung gian có PK phức hợp gồm 2 FK.
