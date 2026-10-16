# Môn 3 · Bài 03 — Cấu trúc quan hệ: Schema, Tuple, Attribute và Domain
# 제3과목: 데이터베이스 구축 — 스키마 3계층, 릴레이션 구조 (튜플·속성·도메인)

> **Mạch đọc:** Tiếp nối từ [Bài 02](02-mo-hinh-du-lieu-va-bieu-do-erd.md) về ánh xạ thực thể và mối quan hệ thành bảng, bài học này mổ xẻ cấu trúc giải phẫu của mô hình dữ liệu quan hệ (Relational Model). Người học sẽ nắm vững kiến trúc 3 tầng lược đồ (External, Conceptual, Internal Schema) tạo nên tính độc lập dữ liệu, phân biệt chính xác Tuple (hàng) và Attribute (cột), tính toán chuẩn xác Degree (bậc) và Cardinality (lực lượng), và hiểu rõ bản chất của miền giá trị nguyên tử Domain.

> **Mạch kết nối 3 bước (3-part Bridge):**
> - **Từ đâu (Khởi đầu):** Sau khi biểu đồ E-R ở Bài 02 được chuyển đổi thành các bảng logic, các bảng này tồn tại dưới dạng các quan hệ toán học (Relation).
> - **Đang giải quyết gì (Bản chất hiện tại):** Định hình ranh giới kỹ thuật giữa người dùng (External), thiết kế logic toàn cục (Conceptual), và lưu trữ vật lý (Internal); đồng thời giải quyết các câu hỏi tính toán cốt lõi trong đề thi về số hàng (Cardinality) và số cột (Degree).
> - **Dùng đi đâu (Đích đến tiếp theo):** Trên nền cấu trúc bảng và thuộc tính này, [Bài 04](04-cac-loai-khoa-va-rang-buoc-toan-ven-du-lieu.md) sẽ thiết lập hệ thống các loại Khóa (Khóa chính, Khóa ngoại, Khóa ứng viên) và các ràng buộc toàn vẹn dữ liệu.

---

## 1. Kiến trúc 3 tầng lược đồ và Tính độc lập dữ liệu (스키마 3계층과 데이터 독립성)

ANSI/SPARC đề xuất kiến trúc 3 tầng lược đồ (Schema) nhằm tách biệt góc nhìn của người dùng với cách thức dữ liệu thực sự được lưu trên ổ đĩa:

```
[외부 스키마 (External Schema)]  ──> Góc nhìn người dùng / Ứng dụng (User Views)
           │
           │  ◄── 논리적 데이터 독립성 (Tính độc lập dữ liệu logic)
           ▼
[개념 스키마 (Conceptual Schema)] ──> Toàn bộ cấu trúc logic toàn cục (Enterprise View)
           │
           │  ◄── 물리적 데이터 독립성 (Tính độc lập dữ liệu vật lý)
           ▼
[내부 스키마 (Internal Schema)]  ──> Cấu trúc lưu trữ vật lý trên đĩa (Physical Storage)
```

### 1.1. Bảng phân tích 3 tầng lược đồ (스키마 3계층)

| Tầng lược đồ (스키마) | Tên gọi khác (별칭) | Góc nhìn và phạm vi (관점 및 범위) | Nội dung cốt lõi |
| :--- | :--- | :--- | :--- |
| **1. 외부 스키마**<br>(External Schema) | `서브스키마`<br>(Subschema / User View) | Góc nhìn cá nhân của từng người dùng hoặc nhóm ứng dụng cụ thể. | Mỗi người dùng chỉ thấy phần dữ liệu liên quan đến nghiệp vụ của mình (thông qua View). Một CSDL có **nhiều 외부 스키마**. |
| **2. 개념 스키마**<br>(Conceptual Schema) | `전체적인 논리적 구조`<br>(Logical Schema / Enterprise View) | Góc nhìn toàn cục của toàn bộ doanh nghiệp/tổ chức. | Định nghĩa toàn bộ thực thể, thuộc tính, mối quan hệ và các ràng buộc toàn vẹn. Một CSDL chỉ có **duy nhất 1 개념 스키마**. |
| **3. 내부 스키마**<br>(Internal Schema) | `물리적 스키마`<br>(Physical Schema / Storage View) | Góc nhìn của phần cứng và hệ thống lưu trữ vật lý. | Định nghĩa cấu trúc bản ghi lưu trữ, đường dẫn truy cập, chỉ mục (index), kiểu mã hóa và khối nhớ trên đĩa. Chỉ có **duy nhất 1 내부 스키마**. |

### 1.2. Tính độc lập dữ liệu 2 cấp độ (데이터 독립성 2단계)

- **1. 논리적 데이터 독립성 (Tính độc lập dữ liệu logic):**
  - **Khái niệm:** Khả năng thay đổi Lược đồ khái niệm (`개념 스키마`) mà **không làm ảnh hưởng** đến Lược đồ ngoài (`외부 스키마`) và các chương trình ứng dụng.
  - **Ví dụ:** Thêm một cột mới hoặc thêm một bảng mới vào CSDL không làm hỏng các màn hình giao diện hiện có của nhân viên.
- **2. 물리적 데이터 독립성 (Tính độc lập dữ liệu vật lý):**
  - **Khái niệm:** Khả năng thay đổi Lược đồ trong (`내부 스키마`) như thay đổi cấu trúc lưu trữ, định dạng file hoặc tạo thêm Index mà **không làm thay đổi** Lược đồ khái niệm (`개념 스키마`) và Lược đồ ngoài.
  - **Ví dụ:** DBA chuyển dữ liệu từ ổ HDD sang ổ SSD hoặc tạo thêm chỉ mục B-Tree để tăng tốc mà không cần sửa câu lệnh SQL của ứng dụng.

---

## 2. Cấu trúc bảng quan hệ (릴레이션의 구조: 튜플, 속성, 도메인)

Mô hình dữ liệu quan hệ tổ chức dữ liệu thành bảng 2 chiều gọi là **릴레이션 (Relation)**.

```
       속성 (Attribute, 열/Column) ──> Degree (차수) = số cột
       ┌───────────┬──────────────┬──────────────┐
       │ 학번(MSSV)│ 이름(Họ tên) │ 학과(Ngành)  │ ◄── 릴레이션 스키마 (Relation Schema)
       ├───────────┼──────────────┼──────────────┤
튜플   │ 20260001  │ 홍길동       │ 컴퓨터공학   │
(Tuple)│ 20260002  │ 김영희       │ 소프트웨어   │ ◄── 릴레이션 인스턴스 (Relation Instance)
Row/행 │ 20260003  │ 이철수       │ 정보보안     │
       └───────────┴──────────────┴──────────────┘
       ▲
       └── Cardinality (카디널리티, 기수) = số hàng (ở đây = 3)
```

### 2.1. Bảng thuật ngữ tương đương giữa Toán học, CSDL và File

| Thuật ngữ Quan hệ (관계형 용어) | Thuật ngữ SQL / Bảng (테이블 용어) | Thuật ngữ Hệ thống Tệp (파일 시스템) | Định nghĩa & Đo lường |
| :--- | :--- | :--- | :--- |
| **릴레이션 (Relation)** | `테이블 (Table)` | `파일 (File)` | Toàn bộ cấu trúc bảng 2 chiều. |
| **튜플 (Tuple)** | `행 (Row)` | `레코드 (Record)` | Một dòng dữ liệu đại diện cho một đối tượng. Số lượng tuple gọi là **카디널리티 (Cardinality / Lực lượng)**. |
| **속성 (Attribute)** | `열 (Column)` | `필드 (Field)` | Đặc tính mô tả thực thể. Số lượng attribute gọi là **디그리 (Degree / Bậc / 차수)**. |
| **도메인 (Domain)** | `데이터 타입/제약` (Type/Check) | `값의 범위` (Range) | Tập hợp tất cả các giá trị nguyên tử hợp lệ mà một thuộc tính có thể nhận. |

### 2.2. Bốn đặc trưng cốt lõi của Relation (릴레이션의 4대 특성)

1. **튜플의 유일성 (Tính duy nhất của Tuple):** Trong một relation không bao giờ tồn tại hai tuple giống hệt nhau ở mọi thuộc tính (bắt buộc phải có khóa chính để phân biệt).
2. **튜플의 무순서성 (Tính vô thứ tự của Tuple):** Thứ tự trên-dưới của các dòng trong bảng hoàn toàn không ảnh hưởng đến ngữ nghĩa hay tính đúng đắn của dữ liệu.
3. **속성의 무순서성 (Tính vô thứ tự của Attribute):** Thứ tự trái-phải của các cột trong bảng không có ý nghĩa toán học (cột `Họ tên` đứng trước hay đứng sau `Ngày sinh` đều như nhau).
4. **속성의 원자성 (Tính nguyên tử của thuộc tính):** Mỗi ô dữ liệu tại giao điểm giữa một dòng và một cột chỉ được phép chứa **duy nhất một giá trị nguyên tử (Atomic value)**, không được chứa mảng hoặc danh sách giá trị lặp (chuẩn 1NF).

---

## 3. Công thức tính Degree và Cardinality trong đề thi (계산 공식)

Trong các bài toán đại số quan hệ và đề thi 정보처리기사:

### 3.1. Phép tích Descartes (카티션 프로덕트 / Cartesian Product: $R \times S$)
Giả sử Relation $R$ có Degree $D_1$, Cardinality $C_1$; Relation $S$ có Degree $D_2$, Cardinality $C_2$:
- **Degree của kết quả:** 

$$\text{Degree}(R \times S) = D_1 + D_2 \quad (\text{Cộng các cột lại})$$

- **Cardinality của kết quả:** 

$$\text{Cardinality}(R \times S) = C_1 \times C_2 \quad (\text{Nhân các dòng với nhau})$$

> **Ví dụ:** Bảng $R$ có 4 cột, 5 dòng; Bảng $S$ có 3 cột, 10 dòng. Kết quả phép tích $R \times S$ có:
> - Degree = $4 + 3 = 7$ cột.
> - Cardinality = $5 \times 10 = 50$ dòng.

---

## 4. Bẫy đề thi và bài tập nhận diện (시험 대비 함정 & 실전 포인트)

### 4.1. Bẫy đề thi trắc nghiệm (기출 함정)
- **Bẫy 1: Nhầm lẫn giữa Degree và Cardinality:**
  - *Câu hỏi:* "Số lượng hàng (Tuple) trong bảng quan hệ được gọi là gì?"
  - *Đáp án đúng:* **카디널리티 (Cardinality / 기수)**.
  - *Bẫy sai:* Thí sinh rất hay nhầm sang **디그리 (Degree / 차수)** (Degree là số cột).
  - *Mẹo nhớ:* **"Cột = Cấp độ (Degree), Hàng = Hàng hóa chất đầy (Cardinality)"**.
- **Bẫy 2: Số lượng của các tầng Schema:**
  - *Câu hỏi:* "Trong một hệ quản trị CSDL, có bao nhiêu khái niệm 스키마 (Conceptual Schema) và bao nhiêu 외부 스키마 (External Schema)?"
  - *Đáp án đúng:* **Chỉ có DUY NHẤT 1 개념 스키마 và 1 내부 스키마**, nhưng có thể có **NHIỀU 외부 스키마**.
- **Bẫy 3: Phân biệt độc lập logic vs độc lập vật lý:**
  - *Câu hỏi:* "Khi DBA tạo thêm chỉ mục (Index) hoặc đổi ổ cứng mà không làm ảnh hưởng đến cấu trúc logic của bảng thì hệ thống thỏa mãn tính chất nào?"
  - *Đáp án đúng:* **Tính độc lập dữ liệu vật lý (물리적 데이터 독립성)**.

---

## 5. Checklist ôn thi (복습 체크리스트)

- [ ] Phân biệt 3 tầng Schema: External (người dùng/view), Conceptual (toàn cục logic), Internal (lưu trữ đĩa).
- [ ] Nhớ rõ số lượng: CSDL chỉ có 1 Conceptual Schema và 1 Internal Schema, nhưng có nhiều External Schema.
- [ ] Phân biệt Degree (số cột / 차수) và Cardinality (số hàng / 카디널리티).
- [ ] Thuộc công thức phép tích Descartes: Degree cộng dồn ($D_1 + D_2$), Cardinality nhân chéo ($C_1 \times C_2$).
- [ ] Thuộc 4 đặc trưng của Relation: Tuple duy nhất, Tuple vô thứ tự, Attribute vô thứ tự, Giá trị nguyên tử.
