# 릴레이션 구조와 스키마 3계층 (Cấu trúc quan hệ: Schema, Tuple, Attribute và Domain)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc 3 tầng lược đồ ANSI/SPARC: Lược đồ ngoài (`외부 스키마`), Lược đồ khái niệm (`개념 스키마`), Lược đồ trong (`내부 스키마`).
- Phân biệt sâu sắc 2 cấp độ độc lập dữ liệu: Độc lập logic (`논리적 데이터 독립성`) và Độc lập vật lý (`물리적 데이터 독립성`).
- Làm chủ cấu trúc quan hệ: Bảng quan hệ (`릴레이션`), Hàng (`튜플`), Cột (`속성`), Miền giá trị nguyên tử (`도메인`).
- Thuộc nằm lòng các công thức tính toán Degree (`디그리 / 차수` = số cột) và Cardinality (`카디널리티 / 기수` = số hàng) trong phép tích Descartes ($R \times S$).
- Nắm vững 4 đặc trưng cốt lõi của Relation: Tính duy nhất, vô thứ tự của hàng, vô thứ tự của cột, và tính nguyên tử của giá trị thuộc tính.

## 핵심 키워드 (Từ khóa)
- 스키마 3계층 (Kiến trúc 3 tầng lược đồ: 외부, 개념, 내부 스키마)
- 데이터 독립성 (Tính độc lập dữ liệu logic và vật lý)
- 릴레이션 (Bảng quan hệ / Relation / Table)
- 튜플, 카디널리티 (Tuple, Cardinality / Số hàng)
- 속성, 디그리, 차수 (Attribute, Degree / Số cột)
- 도메인, 원자값 (Domain, Giá trị nguyên tử / Atomic Value)
- 카티션 프로덕트 (Phép tích Descartes / Degree cộng, Cardinality nhân)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Sau khi biểu đồ E-R ở Bài 02 được chuyển đổi thành các bảng logic, các bảng này tồn tại dưới dạng các quan hệ toán học (Relation).
- **Đang giải quyết gì (Current Problem):** Định hình ranh giới kỹ thuật giữa người dùng (External), thiết kế logic toàn cục (Conceptual), và lưu trữ vật lý (Internal); đồng thời giải quyết các câu hỏi tính toán cốt lõi trong đề thi về số hàng (Cardinality) và số cột (Degree).
- **Dùng đi đâu (Forward Handoff):** Trên nền cấu trúc bảng và thuộc tính này, [04-cac-loai-khoa-va-rang-buoc-toan-ven-du-lieu.md](04-cac-loai-khoa-va-rang-buoc-toan-ven-du-lieu.md) sẽ thiết lập hệ thống các loại Khóa (Khóa chính, Khóa ngoại, Khóa ứng viên) và các ràng buộc toàn vẹn dữ liệu.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ nhanh bảng thuật ngữ tương đương (Toán học - CSDL - File), công thức tích Descartes và các bẫy trắc nghiệm dễ nhầm giữa Degree và Cardinality.
- Đọc TẦNG B để hiểu sâu bản chất 3 tầng lược đồ, tính độc lập dữ liệu 2 cấp độ và 4 đặc tính toán học của quan hệ.

---

## 릴레이션 구조와 스키마 3계층

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng thuật ngữ tương đương giữa Toán học, CSDL và File

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

| Thuật ngữ Quan hệ (관계형 용어) | Thuật ngữ SQL / Bảng (테이블 용어) | Thuật ngữ Hệ thống Tệp (파일 시스템) | Định nghĩa & Đo lường |
| :--- | :--- | :--- | :--- |
| **릴레이션 (Relation)** | `테이블 (Table)` | `파일 (File)` | Toàn bộ cấu trúc bảng 2 chiều. |
| **튜플 (Tuple)** | `행 (Row)` | `레코드 (Record)` | Một dòng dữ liệu đại diện cho một đối tượng. Số lượng tuple gọi là **카디널리티 (Cardinality / Lực lượng)**. |
| **속성 (Attribute)** | `열 (Column)` | `필드 (Field)` | Đặc tính mô tả thực thể. Số lượng attribute gọi là **디그리 (Degree / Bậc / 차수)**. |
| **도메인 (Domain)** | `데이터 타입/제약` (Type/Check) | `값의 범위` (Range) | Tập hợp tất cả các giá trị nguyên tử hợp lệ mà một thuộc tính có thể nhận. |

#### 2. Công thức tính Degree và Cardinality trong đề thi

Giả sử Relation $R$ có Degree $D_1$, Cardinality $C_1$; Relation $S$ có Degree $D_2$, Cardinality $C_2$:
- **Degree của kết quả:** $\text{Degree}(R \times S) = D_1 + D_2$ (Cộng các cột lại).
- **Cardinality của kết quả:** $\text{Cardinality}(R \times S) = C_1 \times C_2$ (Nhân các dòng với nhau).

> **Ví dụ thi:** Bảng $R$ có 4 cột, 5 dòng; Bảng $S$ có 3 cột, 10 dòng. Kết quả phép tích $R \times S$ có:
> - Degree = $4 + 3 = 7$ cột.
> - Cardinality = $5 \times 10 = 50$ dòng.

#### 3. Bẫy đề thi trắc nghiệm kinh điển (기출 함정)

- **Bẫy 1: Nhầm lẫn giữa Degree và Cardinality:**
  - *Câu hỏi:* "Số lượng hàng (Tuple) trong bảng quan hệ được gọi là gì?"
  - *Đáp án đúng:* **카디널리티 (Cardinality / 기수)**.
  - *Mẹo nhớ:* **"Cột = Cấp độ (Degree), Hàng = Hàng hóa chất đầy (Cardinality)"**.
- **Bẫy 2: Số lượng của các tầng Schema:**
  - *Câu hỏi:* "Trong một hệ quản trị CSDL, có bao nhiêu 개념 스키마 (Conceptual Schema) và bao nhiêu 외부 스키마 (External Schema)?"
  - *Đáp án đúng:* **Chỉ có DUY NHẤT 1 개념 스키마 và 1 내부 스키마**, nhưng có thể có **NHIỀU 외부 스키마**.
- **Bẫy 3: Phân biệt độc lập logic vs độc lập vật lý:**
  - *Câu hỏi:* "Khi DBA tạo thêm chỉ mục (Index) hoặc đổi ổ cứng mà không làm ảnh hưởng đến cấu trúc logic của bảng thì hệ thống thỏa mãn tính chất nào?"
  - *Đáp án đúng:* **Tính độc lập dữ liệu vật lý (물리적 데이터 독립성)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Kiến trúc 3 tầng lược đồ và Tính độc lập dữ liệu (스키마 3계층과 데이터 독립성)

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

| Tầng lược đồ (스키마) | Tên gọi khác (별칭) | Góc nhìn và phạm vi (관점 및 범위) | Nội dung cốt lõi |
| :--- | :--- | :--- | :--- |
| **1. 외부 스키마** (External Schema) | `서브스키마` (Subschema / User View) | Góc nhìn cá nhân của từng người dùng hoặc nhóm ứng dụng cụ thể. | Mỗi người dùng chỉ thấy phần dữ liệu liên quan đến nghiệp vụ của mình (thông qua View). Một CSDL có **nhiều 외부 스키마**. |
| **2. 개념 스키마** (Conceptual Schema) | `전체적인 논리적 구조` (Logical Schema / Enterprise View) | Góc nhìn toàn cục của toàn bộ doanh nghiệp/tổ chức. | Định nghĩa toàn bộ thực thể, thuộc tính, mối quan hệ và các ràng buộc toàn vẹn. Một CSDL chỉ có **duy nhất 1 개념 스키마**. |
| **3. 내부 스키마** (Internal Schema) | `물리적 스키마` (Physical Schema / Storage View) | Góc nhìn của phần cứng và hệ thống lưu trữ vật lý. | Định nghĩa cấu trúc bản ghi lưu trữ, đường dẫn truy cập, chỉ mục (index), kiểu mã hóa và khối nhớ trên đĩa. Chỉ có **duy nhất 1 내부 스키마**. |

##### Tính độc lập dữ liệu 2 cấp độ
1. **논리적 데이터 독립성 (Tính độc lập dữ liệu logic):** Khả năng thay đổi Lược đồ khái niệm (`개념 스키마`) mà không làm ảnh hưởng đến Lược đồ ngoài (`외부 스키마`) và các chương trình ứng dụng (ví dụ thêm cột mới không làm hỏng giao diện cũ).
2. **물리적 데이터 독립성 (Tính độc lập dữ liệu vật lý):** Khả năng thay đổi Lược đồ trong (`내부 스키마`) như thay đổi cấu trúc lưu trữ, định dạng file hoặc tạo thêm Index mà không làm thay đổi Lược đồ khái niệm (`개념 스키마`) và Lược đồ ngoài.

#### 2. Bốn đặc trưng cốt lõi của Relation (릴레이션의 4대 특성)

1. **튜플의 유일성 (Tính duy nhất của Tuple):** Trong một relation không bao giờ tồn tại hai tuple giống hệt nhau ở mọi thuộc tính (bắt buộc phải có khóa chính để phân biệt).
2. **튜플의 무순서성 (Tính vô thứ tự của Tuple):** Thứ tự trên-dưới của các dòng trong bảng hoàn toàn không ảnh hưởng đến ngữ nghĩa hay tính đúng đắn của dữ liệu.
3. **속성의 무순서성 (Tính vô thứ tự của Attribute):** Thứ tự trái-phải của các cột trong bảng không có ý nghĩa toán học (cột `Họ tên` đứng trước hay đứng sau `Ngày sinh` đều như nhau).
4. **속성의 원자성 (Tính nguyên tử của thuộc tính):** Mỗi ô dữ liệu tại giao điểm giữa một dòng và một cột chỉ được phép chứa **duy nhất một giá trị nguyên tử (Atomic value)**, không được chứa mảng hoặc danh sách giá trị lặp (chuẩn 1NF).

---

### 복습 체크리스트
- [ ] Phân biệt 3 tầng Schema: External (người dùng/view), Conceptual (toàn cục logic), Internal (lưu trữ đĩa).
- [ ] Nhớ rõ số lượng: CSDL chỉ có 1 Conceptual Schema và 1 Internal Schema, nhưng có nhiều External Schema.
- [ ] Phân biệt Degree (số cột / 차수) và Cardinality (số hàng / 카디널리티).
- [ ] Thuộc công thức phép tích Descartes: Degree cộng dồn ($D_1 + D_2$), Cardinality nhân chéo ($C_1 \times C_2$).
- [ ] Thuộc 4 đặc trưng của Relation: Tuple duy nhất, Tuple vô thứ tự, Attribute vô thứ tự, Giá trị nguyên tử.
