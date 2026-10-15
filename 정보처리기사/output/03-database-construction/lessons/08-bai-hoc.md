# 12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)

## 학습 목표 (Mục tiêu)
- Nắm vững giải phẫu chi tiết của một Relation (Bảng quan hệ): `튜플 (Tuple)`, `속성 (Attribute)`, `도메인 (Domain)`.
- Phân biệt rõ và tính toán chính xác 2 chỉ số cốt lõi trong đề thi: **Bậc (`차수 / Degree`)** và **Lực lượng (`카디널리티 / Cardinality`)**.
- Hiểu rõ sự khác biệt giữa Lược đồ quan hệ (`릴레이션 스키마`) và Thực thể quan hệ (`릴레이션 인스턴스`).

## 핵심 키워드 (Từ khóa)
- 릴레이션 (Bảng quan hệ / Relation)
- 튜플 (Bản ghi / Hàng / Tuple)
- 속성 (Thuộc tính / Cột / Attribute)
- 차수 (Bậc của bảng / Degree)
- 카디널리티 (Lực lượng của bảng / Cardinality)
- 도메인 (Miền giá trị / Domain)
- 릴레이션 스키마 (Lược đồ quan hệ / Relation Schema)
- 릴레이션 인스턴스 (Dữ liệu quan hệ thực tế / Relation Instance)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([07-bai-hoc.md](07-bai-hoc.md)):** Sau khi tìm hiểu 4 đặc trưng tổng quát của Relation, bài học này đi sâu vào định nghĩa định lượng: cách đếm số cột (Degree) và số hàng (Cardinality).
- **Tiếp nối sang bài sau ([09-bai-hoc.md](09-bai-hoc.md), [10-bai-hoc.md](10-bai-hoc.md)):** Sau khi nắm chắc cấu trúc bảng quan hệ ở tầng logic, ta sẽ đối chiếu lại với các ký hiệu E-R tương ứng ở tầng khái niệm để phục vụ bài toán chuyển đổi E-R sang Table.

## 읽는 방법 (Cách đọc)
- Học thuộc mẹo phân biệt kinh điển: **"De-Col, Car-Row"** (Degree là Column/Cột/Thuộc tính; Cardinality là Row/Hàng/Tuple).
- Đề thi thường cho một bảng mẫu với n cột và m hàng rồi hỏi Degree và Cardinality là bao nhiêu.

---

## 12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Các thành phần cấu tạo Relation (릴레이션의 구조):**
  - **릴레이션 (Relation):** Bảng dữ liệu 2 chiều gồm các hàng và các cột.
  - **튜플 (Tuple):** Mỗi hàng trong bảng, tương ứng với một bản ghi dữ liệu (`레코드 / Record`).
  - **속성 (Attribute):** Mỗi cột trong bảng, thể hiện một mục dữ liệu nhỏ nhất có ý nghĩa (`항목 / Field`).
  - **도메인 (Domain):** Tập hợp tất cả các giá trị nguyên tử (`원자값`) hợp lệ mà một thuộc tính có thể nhận (ví dụ: miền giá trị của Giới tính là `{'Nam', 'Nữ'}`).
- **2. Hai chỉ số định lượng bắt buộc phải tính đúng trong đề thi:**
  - **차수 (Degree / 디그리):** Là **tổng số lượng thuộc tính (`속성의 수 / Cột`)** trong bảng.
    - *Đặc điểm:* Giá trị Degree rất ít khi thay đổi (chỉ đổi khi cấu trúc bảng được thêm/bớt cột bằng DDL).
  - **카디널리티 (Cardinality / 기수):** Là **tổng số lượng bộ dữ liệu (`튜플의 수 / Hàng`)** trong bảng.
    - *Đặc điểm:* Giá trị Cardinality thay đổi liên tục theo thời gian khi người dùng thêm (`INSERT`) hoặc xóa (`DELETE`) bản ghi.
- **3. Phân biệt Lược đồ vs Thực thể dữ liệu:**
  - `릴레이션 스키마 (Relation Schema)`: Là cấu trúc logic định nghĩa tên bảng và danh sách các cột (tính chất tĩnh, mô tả khung).
  - `릴레이션 인스턴스 (Relation Instance)`: Là tập hợp các hàng dữ liệu thực tế tại một thời điểm cụ thể (tính chất động).
- **시험 포인트 (Điểm thi trọng tâm):**
  - **Dạng bài tính toán:** Cho bảng `SINH_VIEN` gồm 5 cột (`MaSV`, `HoTen`, `NgaySinh`, `Lop`, `Diem`) và hiện có 100 sinh viên.
    - Hỏi Degree (차수) = **5** (đếm số cột).
    - Hỏi Cardinality (카디널리티) = **100** (đếm số hàng).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - Đề thi hay đánh tráo: gán Degree cho số hàng và Cardinality cho số cột. Nhớ tuyệt đối: **Degree = Cột (속성)**, **Cardinality = Hàng (튜플)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Degree đếm Cột, Cardinality đếm Hàng".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối quan hệ giữa Phép toán tập hợp và Bậc/Lực lượng:**
  - Phép tích Đề-các (Cartesian Product / 교차곱 $R \times S$):
    - **Degree mới:** Bằng tổng bậc của hai bảng: $\text{Degree}(R \times S) = \text{Degree}(R) + \text{Degree}(S)$.
    - **Cardinality mới:** Bằng tích số hàng của hai bảng: $\text{Cardinality}(R \times S) = \text{Cardinality}(R) \times \text{Cardinality}(S)$.
    - *Đây là câu hỏi cực kỳ phổ biến trong đề thi 실기 và 필기!*
- **Ví dụ minh họa:**
  - Bảng R có Degree = 3, Cardinality = 4.
  - Bảng S có Degree = 2, Cardinality = 5.
  - Khi thực hiện $R \times S$:
    - Bậc mới (Degree) = $3 + 2 = 5$.
    - Lực lượng mới (Cardinality) = $4 \times 5 = 20$.

### 복습 체크리스트
- [ ] Phân biệt chính xác Tuple (hàng) và Attribute (cột).
- [ ] Định nghĩa đúng Degree (số cột) và Cardinality (số hàng).
- [ ] Tính nhẩm chuẩn Degree và Cardinality khi thực hiện phép tích Descartes ($R \times S$).
- [ ] Hiểu rõ Domain là tập hợp các giá trị nguyên tử hợp lệ của một thuộc tính.
