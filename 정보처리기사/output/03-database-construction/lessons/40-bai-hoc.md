# 106-107. 튜플(Tuple)과 속성(Attribute)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của hai thành phần cấu tạo nền tảng trong Mô hình dữ liệu quan hệ: **Bộ dữ liệu (`튜플 / Tuple / Row`)** và **Thuộc tính (`속성 / Attribute / Column`)**.
- Phân biệt chính xác hai đại lượng đo lường cấu trúc bảng: **Số lượng hàng gọi là Lượng số (`카디널리티 / Cardinality`)** và **Số lượng cột gọi là Bậc (`디그리 / Degree`)**.
- Nhắc lại và củng cố 4 đặc trưng bất biến của Quan hệ (`릴레이션의 4대 특징`): Tính duy nhất của tuple, Tính vô thứ tự của tuple, Tính vô thứ tự của thuộc tính, và Tính nguyên tử của thuộc tính.

## 핵심 키워드 (Từ khóa)
- 튜플 (Bộ dữ liệu / Hàng / Tuple / Row)
- 속성 (Thuộc tính / Cột / Attribute / Column)
- 카디널리티 (Lượng số / Cardinality: Số lượng hàng)
- 디그리 (Bậc / Degree: Số lượng cột)
- 도메인 (Miền giá trị / Domain)
- 튜플의 유일성 (Tính duy nhất của hàng)
- 속성의 원자성 (Tính nguyên tử của cột)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([08-bai-hoc.md](08-bai-hoc.md), [11-bai-hoc.md](11-bai-hoc.md), [16-bai-hoc.md](16-bai-hoc.md)):** Khái niệm Tuple và Attribute đã xuất hiện xuyên suốt các phép toán đại số quan hệ (Select lọc Tuple, Project chọn Attribute) và tích Đề-các ($Degree_R + Degree_S$, $Cardinality_R \times Cardinality_S$).
- **Tiếp nối sang bài sau ([41-bai-hoc.md](41-bai-hoc.md)):** Để bảo đảm giá trị của mỗi Attribute luôn hợp lệ, bài học tiếp theo sẽ đào sâu vào Miền giá trị nguyên tử (`도메인 / Domain`).

## 읽는 방법 (Cách đọc)
- Khắc sâu cặp từ khóa đo lường bằng câu khẩu quyết:
  - **Tu - Car (Tuple = Cardinality = Số hàng ngang).**
  - **At - De (Attribute = Degree = Số cột dọc).**
- Ghi nhớ bản chất: **Attribute là đơn vị logic nhỏ nhất** cấu thành cơ sở dữ liệu quan hệ (`데이터베이스를 구성하는 가장 작은 논리적 단위`).

---

## 106-107. 튜플(Tuple)과 속성(Attribute)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu Tuple vs Attribute theo chuẩn đề thi:**
  | Tiêu chí | 튜플 (Tuple / Bộ dữ liệu) | 속성 (Attribute / Thuộc tính) |
  |---|---|---|
  | **Vị trí hình học** | Các **hàng ngang (Row)** trong bảng | Các **cột dọc (Column)** trong bảng |
  | **Ý nghĩa bản chất** | Đại diện cho **một thực thể cụ thể** chứa tập hợp các giá trị thuộc tính liên quan | Đại diện cho **một đặc trưng, tính chất** của thực thể; là **đơn vị logic nhỏ nhất** của CSDL |
  | **Đại lượng đo lường** | **카디널리티 (Cardinality / Lượng số / 기수):** Tổng số hàng hiện có trong bảng | **디그리 (Degree / Bậc / 차수):** Tổng số cột hiện có trong cấu trúc bảng |
  | **Quy luật biến động** | Thay đổi liên tục theo thời gian thực khi người dùng INSERT / DELETE dữ liệu | Tương đối cố định, chỉ thay đổi khi người quản trị chạy lệnh DDL `ALTER TABLE` |
  | **Quy tắc bắt buộc** | **Phải là duy nhất (`튜플의 유일성`)**, không được tồn tại 2 hàng giống hệt nhau | **Phải mang giá trị nguyên tử (`원자값`)**, không được phân chia thành mảng hay danh sách |

- **2. Bốn đặc trưng bất biến của Quan hệ (릴레이션의 4대 특징 요약):**
  1. **튜플의 유일성 (Tính duy nhất của hàng):** Mọi hàng trong bảng phải phân biệt được với nhau nhờ Khóa chính (Primary Key).
  2. **튜플의 무순서성 (Tính vô thứ tự của hàng):** Thứ tự trên dưới của các hàng không mang ý nghĩa logic; đảo vị trí các hàng không làm thay đổi bản chất dữ liệu.
  3. **속성의 무순서성 (Tính vô thứ tự của cột):** Thứ tự trái phải của các cột không mang ý nghĩa logic; đảo vị trí các cột trong bảng không làm sai lệch dữ liệu.
  4. **속성의 원자성 (Tính nguyên tử của cột):** Mọi giá trị tại giao điểm giữa hàng và cột bắt buộc phải là một giá trị đơn nhất, không thể chia nhỏ hơn nữa.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Đơn vị logic nhỏ nhất cấu thành cơ sở dữ liệu là gì?"* $\rightarrow$ Đáp án: **속성 (Attribute / Thuộc tính)** (không phải Tuple hay Table).
  - Đề cho bảng có 5 cột và 20 dòng, hỏi Cardinality và Degree là bao nhiêu:
    - **Degree (디그리) = 5** (số cột).
    - **Cardinality (카디널리티) = 20** (số dòng). Tuyệt đối không được đảo ngược hai con số này!

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa bằng bảng sinh viên thực tế:**
  - Bảng `SINH_VIEN`:
    | MaSV (Cột 1) | HoTen (Cột 2) | Tuoi (Cột 3) | Lop (Cột 4) |
    |:---:|---|:---:|:---:|
    | B2101 | Nguyễn Văn A | 20 | IT01 |
    | B2102 | Trần Thị B | 21 | IT02 |
    | B2103 | Lê Văn C | 20 | IT01 |
  - **Phân tích số liệu:**
    - Có 4 cột $\rightarrow$ **Degree (디그리 / Bậc) = 4**.
    - Có 3 dòng $\rightarrow$ **Cardinality (카디널리티 / Lượng số) = 3**.
    - Mỗi dòng dữ liệu như `(B2101, Nguyễn Văn A, 20, IT01)` là một **Tuple**.
    - Mỗi đặc trưng như `MaSV`, `HoTen` là một **Attribute**.

### 복습 체크리스트
- [ ] Phân biệt được Tuple (hàng ngang) và Attribute (cột dọc).
- [ ] Ghi nhớ chính xác: số lượng Tuple là Cardinality, số lượng Attribute là Degree.
- [ ] Khẳng định được Attribute là đơn vị logic nhỏ nhất của cơ sở dữ liệu.
- [ ] Nêu đầy đủ 4 đặc trưng của Quan hệ (duy nhất hàng, vô thứ tự hàng, vô thứ tự cột, nguyên tử cột).
