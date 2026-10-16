# 릴레이션 구조와 스키마 (Cấu trúc quan hệ: Schema, Tuple, Attribute và Domain)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc hình thức của bảng quan hệ trong CSDL: Lược đồ quan hệ (`릴레이션 스키마` / Intension / 내연) và Thể hiện quan hệ (`릴레이션 인스턴스` / Extension / 외연).
- Hiểu rõ 4 thành phần cấu trúc cốt lõi: Quan hệ (`릴레이션` / Relation), Bộ dữ liệu (`튜플` / Tuple), Thuộc tính (`속성` / Attribute), và Miền giá trị nguyên tử (`도메인` / Domain).
- Phân biệt tuyệt đối giữa Bậc (`디그리 / 차수` / Degree - số lượng cột/thuộc tính) và Lực lượng (`카디널리티 / 기수` / Cardinality - số lượng hàng/bộ).
- Thành thạo công thức tính toán Degree và Cardinality trong các phép toán quan hệ, đặc biệt là phép tích Descartes ($R \times S$).
- Nắm vững 4 đặc trưng toán học nền tảng của quan hệ: Tính duy nhất của Tuple, Tính vô thứ tự của Tuple, Tính vô thứ tự của Attribute, và Tính nguyên tử của giá trị thuộc tính.

## 핵심 키워드 (Từ khóa)
- 릴레이션 스키마 (Lược đồ quan hệ / Relation Schema / 내연 Intension)
- 릴레이션 인스턴스 (Thể hiện quan hệ / Relation Instance / 외연 Extension)
- 릴레이션 (Bảng quan hệ / Relation / Table)
- 튜플, 카디널리티 (Tuple, Cardinality / Bộ dữ liệu / Lực lượng / Số hàng)
- 속성, 디그리, 차수 (Attribute, Degree / Thuộc tính / Bậc / Số cột)
- 도메인 (Miền giá trị / Domain / 원자값 집합)
- 카티션 프로덕트 (Phép tích Descartes / Cartesian Product)
- 릴레이션의 특성 (Đặc trưng của quan hệ: 유일성, 무순서성, 원자성)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở [02-mo-hinh-du-lieu-va-bieu-do-erd.md](02-mo-hinh-du-lieu-va-bieu-do-erd.md), mô hình thực thể quan hệ E-R đã được ánh xạ thành các bảng quan hệ logic.
- **Đang giải quyết gì (Current Problem):** Mổ xẻ cấu trúc toán học của bảng quan hệ theo lý thuyết của E.F. Codd: phân tách cấu trúc định nghĩa tĩnh (Schema/Intension) với dữ liệu thực tế biến động (Instance/Extension); định nghĩa các đơn vị hàng, cột, miền giá trị và cung cấp các quy tắc tính bậc, lực lượng trong đề thi.
- **Dùng đi đâu (Forward Handoff):** Trên cấu trúc các tuple và attribute này, [04-cac-loai-khoa-va-rang-buoc-toan-ven-du-lieu.md](04-cac-loai-khoa-va-rang-buoc-toan-ven-du-lieu.md) sẽ thiết lập các loại Khóa (Super, Candidate, Primary, Alternate, Foreign key) và các quy tắc toàn vẹn thực thể, tham chiếu, miền giá trị.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm vững bảng đối chiếu thuật ngữ toán học - CSDL - hệ thống tệp, công thức tính Degree/Cardinality và câu thần chú `카-튜, 디-속`.
- Đọc TẦNG B để phân biệt sâu sắc khái niệm 내연 (Intension) vs 외연 (Extension) và hiểu cặn kẽ 4 đặc trưng của bảng quan hệ.

---

## 릴레이션 구조와 스키마

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cấu trúc bảng quan hệ (릴레이션 구조)

Bảng quan hệ hai chiều (**릴레이션** / Relation) được cấu thành từ hai phần: phần định nghĩa cấu trúc (Lược đồ - Schema) và phần tập hợp dữ liệu thực tế (Thể hiện - Instance):

```text
       속성 (Attribute / 열 Column) ──> Degree (차수 / Bậc) = Số cột (ở đây = 3)
       ┌───────────┬──────────────┬──────────────┐
       │ 학번(MSSV)│ 이름(Họ tên) │ 학과(Ngành)  │ ◄── 릴레이션 스키마 (Relation Schema / 내연 Intension)
       ├───────────┼──────────────┼──────────────┤
튜플   │ 20260001  │ 홍길동       │ 컴퓨터공학   │
(Tuple)│ 20260002  │ 김영희       │ 소프트웨어   │ ◄── 릴레이션 인스턴스 (Relation Instance / 외연 Extension)
Hàng/행│ 20260003  │ 이철수       │ 정보보안     │
       └───────────┴──────────────┴──────────────┘
       ▲
       └── Cardinality (카디널리티 / 기수 / Lực lượng) = Số hàng (ở đây = 3)
```

#### 2. Bảng đối chiếu thuật ngữ tương đương (Toán học, CSDL và Tệp tin)

| Thuật ngữ Toán học (관계형 모델) | Thuật ngữ SQL / CSDL (RDBMS) | Thuật ngữ Hệ thống Tệp (File System) | Bản chất kỹ thuật & Đơn vị đo |
| :--- | :--- | :--- | :--- |
| **릴레이션 (Relation)** | `테이블 (Table)` | `파일 (File)` | Toàn bộ bảng 2 chiều chứa cấu trúc và dữ liệu. |
| **튜플 (Tuple / Bộ)** | `행 (Row)` | `레코드 (Record)` | Một bản ghi đại diện cho một đối tượng. Số hàng = **카디널리티 (Cardinality / Lực lượng / 기수)**. |
| **속성 (Attribute / Thuộc tính)** | `열 (Column)` | `필드 (Field)` | Đơn vị logic nhỏ nhất mô tả một đặc tính. Số cột = **디그리 (Degree / Bậc / 차수)**. |
| **도메인 (Domain / Miền giá trị)** | `데이터 타입 / 제약` (Type/CHECK) | `값의 범위` (Range) | Tập hợp tất cả các giá trị nguyên tử (원자값) hợp lệ mà một thuộc tính có thể nhận. |

#### 3. Bậc (Degree) vs Lực lượng (Cardinality) & Công thức tính tích Descartes

| Chỉ số đo lường | Tên tiếng Hàn | Đối tượng đếm | Khả năng thay đổi | Giá trị tối thiểu |
| :--- | :--- | :--- | :--- | :--- |
| **디그리 (Degree / Bậc)** | `차수 (Degree)` | Số lượng **속성 (Attribute / Cột)** | Thường cố định theo thời gian (tĩnh) | Tối thiểu $\ge 1$ (bảng phải có ít nhất 1 cột) |
| **카디널리티 (Cardinality / Lực lượng)** | `기수 (Cardinality)` | Số lượng **튜플 (Tuple / Hàng)** | Thay đổi liên tục theo thao tác INSERT/DELETE (động) | Có thể bằng 0 (khi bảng rỗng mới tạo) |

##### Công thức đề thi: Phép tích Descartes ($R \times S$)
Giả sử Relation $R$ có Degree $D_1$, Cardinality $C_1$; Relation $S$ có Degree $D_2$, Cardinality $C_2$:
- **Degree của kết quả:** $\text{Degree}(R \times S) = D_1 + D_2$ (Cộng số lượng cột lại).
- **Cardinality của kết quả:** $\text{Cardinality}(R \times S) = C_1 \times C_2$ (Nhân số lượng dòng với nhau).

> **Ví dụ thi kinh điển:** Bảng $R$ có 4 cột, 6 dòng; Bảng $S$ có 3 cột, 10 dòng. Kết quả $R \times S$ có:
> - Degree = $4 + 3 = 7$ cột.
> - Cardinality = $6 \times 10 = 60$ dòng.

#### 4. Bẫy đề thi và khẩu quyết ghi nhớ (시험 대비 함정 & 암기 팁)

##### Các bẫy trắc nghiệm kinh điển
- **Bẫy 1: Nhầm lẫn giữa Degree và Cardinality:**
  - *Câu hỏi:* "Số lượng hàng (Tuple) trong bảng quan hệ được gọi là gì?"
  - *Đáp án đúng:* **카디널리티 (Cardinality / 기수)**.
  - *Bẫy sai:* Thí sinh chọn nhầm *디그리 (Degree / 차수)*.
- **Bẫy 2: Phân biệt Schema (내연 Intension) vs Instance (외연 Extension):**
  - *Câu hỏi:* "Thành phần nào của bảng quan hệ là tĩnh, biểu diễn tên bảng và danh sách các cột?"
  - *Đáp án đúng:* **릴레이션 스키마 (Relation Schema / 내연 Intension)**.
  - Ngược lại, tập hợp dữ liệu thực tế tại một thời điểm là **릴레이션 인스턴스 (Relation Instance / 외연 Extension)** mang tính chất động.
- **Bẫy 3: Miền giá trị (도메인) chứa giá trị gì:**
  - *Câu hỏi:* "Một Domain trong mô hình quan hệ chứa các giá trị thuộc dạng nào?"
  - *Đáp án đúng:* **Tập hợp các giá trị nguyên tử (원자값 - Atomic value)**. Không được chứa mảng hay tập hợp phức tạp.

##### Khẩu quyết ghi nhớ thần chú (Mnemonic)
- **Thần chú cặp đôi:** `"카-튜, 디-속"` (hoặc `"Tu-Car, At-De"`)
  - `카 - 튜`: **카**디널리티 = **튜**플 (Cardinality = Tuple = Số Hàng).
  - `디 - 속`: **디**그리 = **속**성 (Degree = 속성/Attribute = Số Cột).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Chi tiết Schema vs Instance: Intension (내연) và Extension (외연)

Trong lý thuyết cơ sở dữ liệu quan hệ của E.F. Codd:
- **릴레이션 스키마 (Relation Schema / 내연 Intension):**
  - Biểu diễn cấu trúc logic của quan hệ: $R(A_1, A_2, \dots, A_n)$ trong đó $R$ là tên quan hệ, $A_i$ là các thuộc tính.
  - Mang tính chất **tĩnh (정적 특성)**: Sau khi đã thiết kế và tạo bảng, schema hiếm khi thay đổi trừ khi có lệnh DDL `ALTER TABLE`.
- **릴레이션 인스턴스 (Relation Instance / 외연 Extension):**
  - Là tập hợp các bộ dữ liệu thực tế ($t_1, t_2, \dots, t_m$) tồn tại trong quan hệ tại một thời điểm cụ thể.
  - Mang tính chất **động (동적 특성)**: Mỗi khi người dùng thực hiện câu lệnh `INSERT`, `DELETE`, `UPDATE`, instance của quan hệ sẽ lập tức thay đổi.

#### 2. Miền giá trị (도메인 / Domain) và tính nguyên tử

- **Khái niệm:** Domain là tập hợp tất cả các giá trị nguyên tử (Atomic values) có cùng kiểu dữ liệu mà một thuộc tính có thể nhận hợp lệ.
- **Ví dụ minh họa:**
  - Thuộc tính `Giới tính (성별)` có Domain = `{'Nam', 'Nữ'}`.
  - Thuộc tính `Điểm trung bình (학점)` có Domain = Số thực từ $0.0$ đến $4.5$.
  - Thuộc tính `Mã sinh viên (학번)` có Domain = Chuỗi ký tự số gồm đúng 8 chữ số.
- **Ý nghĩa kỹ thuật:** Domain đóng vai trò là cơ chế kiểm tra kiểu và kiểm tra phạm vi giá trị tự động (Domain Constraint) nhằm bảo đảm dữ liệu nhập vào luôn đúng đắn và có ý nghĩa nghiệp vụ.

#### 3. Bốn đặc trưng cốt lõi của Relation (릴레이션의 4대 특성)

1. **튜플의 유일성 (Tính duy nhất của Tuple):**
   - Trong một bảng quan hệ không bao giờ được phép tồn tại hai tuple giống hệt nhau ở mọi thuộc tính. Luôn phải tồn tại một tập hợp thuộc tính (Khóa chính) có giá trị phân biệt hoàn toàn giữa các tuple.
2. **튜플의 무순서성 (Tính vô thứ tự của Tuple):**
   - Thứ tự trên - dưới của các dòng trong bảng không có ý nghĩa toán học. Dữ liệu dòng thứ nhất được lưu trước hay dòng thứ mười được lưu trước thì ý nghĩa nghiệp vụ của bảng vẫn giữ nguyên không đổi.
3. **속성의 무순서성 (Tính vô thứ tự của Attribute):**
   - Thứ tự trái - phải của các cột trong bảng không ảnh hưởng đến ngữ nghĩa của relation. Cột `Tên` đứng trước cột `Tuổi` hay cột `Tuổi` đứng trước cột `Tên` thì relation vẫn biểu diễn cùng một bản thể dữ liệu.
4. **속성의 원자성 (Tính nguyên tử của thuộc tính):**
   - Tại giao điểm giữa một hàng và một cột (mỗi ô dữ liệu), chỉ được phép lưu trữ duy nhất một giá trị nguyên tử không thể phân chia tiếp theo nghiệp vụ dữ liệu (`원자값만 가짐`). Đây là điều kiện tiên quyết để đạt chuẩn hóa dạng 1NF.

---

### 복습 체크리스트
- [ ] Phân biệt rõ: Relation Schema (`릴레이션 스키마` / 내연 Intension - tĩnh) và Relation Instance (`릴레이션 인스턴스` / 외연 Extension - động).
- [ ] Nhớ khẩu quyết thần chú: `"카-튜, 디-속"` (Cardinality = Tuple = Số hàng; Degree = Attribute = Số cột).
- [ ] Hiểu rõ miền giá trị (Domain): Là tập hợp các giá trị nguyên tử hợp lệ của một thuộc tính.
- [ ] Làm chủ công thức tích Descartes $R \times S$: Degree cộng ($D_1 + D_2$), Cardinality nhân ($C_1 \times C_2$).
- [ ] Nắm vững 4 đặc trưng của Relation: Tính duy nhất của Tuple, Tính vô thứ tự của Tuple, Tính vô thứ tự của Attribute, Tính nguyên tử của giá trị thuộc tính.
