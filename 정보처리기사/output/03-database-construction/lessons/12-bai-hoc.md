# 173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)

## 학습 목표 (Mục tiêu)
- Tổng hợp toàn diện 4 ràng buộc toàn vẹn dữ liệu quan trọng: Toàn vẹn thực thể (`개체 무결성`), Toàn vẹn tham chiếu (`참조 무결성`), Toàn vẹn miền (`도메인 무결성`), và Toàn vẹn người dùng định nghĩa (`사용자 정의 무결성`).
- Nắm vững khái niệm nền tảng của Đại số quan hệ (`관계대수`): Ngôn ngữ thủ tục (`절차적 언어`), thao tác trên quan hệ đầu vào và trả về kết quả là một quan hệ mới.
- Phân biệt rõ hai nhóm toán tử trong đại số quan hệ: 4 toán tử quan hệ thuần túy (`순수 관계 연산자`: Select, Project, Join, Division) và 4 toán tử tập hợp kinh điển (`일반 집합 연산자`: Union, Intersection, Difference, Cartesian Product).
- Ghi nhớ công thức tính Degree (Bậc) và Cardinality (Lượng số) khi thực hiện phép tích Đề-các (Cartesian Product).

## 핵심 키워드 (Từ khóa)
- 개체 무결성 (Toàn vẹn thực thể / Entity Integrity)
- 참조 무결성 (Toàn vẹn tham chiếu / Referential Integrity)
- 도메인 무결성 (Toàn vẹn miền giá trị / Domain Integrity)
- 사용자 정의 무결성 (Toàn vẹn người dùng định nghĩa / User-Defined Integrity)
- 관계대수 (Đại số quan hệ / Relational Algebra)
- 순수 관계 연산자 (Toán tử quan hệ thuần túy / Pure Relational Operators)
- 일반 집합 연산자 (Toán tử tập hợp / General Set Operators)
- 수평 연산 (Phép toán ngang - Select) / 수직 연산 (Phép toán dọc - Project)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([08-bai-hoc.md](08-bai-hoc.md), [11-bai-hoc.md](11-bai-hoc.md)):** Để bảo vệ tính duy nhất của tuple và duy trì các mối liên kết khóa chính - khóa ngoại, hệ thống CSDL phải thực thi các quy tắc toàn vẹn dữ liệu (`무결성 제약조건`).
- **Tiếp nối sang các bài sau ([14-bai-hoc.md](14-bai-hoc.md), [15-bai-hoc.md](15-bai-hoc.md), [16-bai-hoc.md](16-bai-hoc.md)):** Bài học này đóng vai trò bản đồ tóm lược cốt lõi để chuẩn bị đi sâu vào cơ chế chi tiết của từng phép toán đại số quan hệ ($\sigma, \pi, \bowtie, \div$) và đại số giải tích quan hệ (`관계해석`).

## 읽는 방법 (Cách đọc)
- Học thuộc 4 quy tắc toàn vẹn ở TẦNG A trước vì đây là câu hỏi chắc chắn có trong đề thi trắc nghiệm.
- Ghi nhớ ngay quy tắc hình học: **Select = Cắt ngang theo hàng (수평 연산)**; **Project = Cắt dọc theo cột (수직 연산)**.
- Ghi nhớ công thức Cartesian Product: Bậc cộng lại ($Degree_R + Degree_S$), Lượng số nhân lên ($Cardinality_R \times Cardinality_S$).

---

## 173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bốn quy tắc toàn vẹn dữ liệu cốt lõi (데이터 무결성 4대 제약조건):**
  | Tên quy tắc (Hàn - Anh - Việt) | Điều kiện bắt buộc | Ví dụ vi phạm |
  |---|---|---|
  | **개체 무결성 (Entity Integrity / Toàn vẹn thực thể)** | Thuộc tính khóa chính (`기본키`) **tuyệt đối không được NULL và không được trùng lặp**. | Cột `MãSV` bị để trống hoặc nhập 2 sinh viên cùng mã `B2101`. |
  | **참조 무결성 (Referential Integrity / Toàn vẹn tham chiếu)** | Giá trị khóa ngoại (`외래키`) phải **bằng một giá trị khóa chính đang tồn tại** ở bảng tham chiếu, hoặc phải mang giá trị **NULL**. | Đăng ký học cho sinh viên có mã `B9999` trong khi bảng Sinh Viên chưa có mã này. |
  | **도메인 무결성 (Domain Integrity / Toàn vẹn miền)** | Giá trị của thuộc tính phải nằm đúng trong tập hợp các giá trị hợp lệ đã định nghĩa cho miền đó. | Nhập điểm thi là `15` (trong khi thang điểm là 0-10), hoặc nhập `Nam/Nữ` thành `X`. |
  | **사용자 정의 무결성 (User-Defined Integrity / Toàn vẹn người dùng)** | Dữ liệu phải thỏa mãn các quy tắc nghiệp vụ đặc thù do người dùng / lập trình viên thiết lập. | Ràng buộc nghiệp vụ: "Lương nhân viên không được âm (`Lương >= 0`)". |

- **2. Tổng quan Đại số quan hệ (관계대수 개요):**
  - **Định nghĩa:** Là ngôn ngữ truy vấn mang tính **thủ tục (`절차적 언어 / Procedural Language`)**, chỉ rõ trình tự các bước (`연산 순서`) cần thực hiện để tìm ra kết quả mong muốn từ CSDL quan hệ.
  - **Đặc trưng:** Cả toán hạng đầu vào (toán hạng) và kết quả trả về đều là các **Quan hệ (Relation)**.
- **3. Phân loại 2 nhóm toán tử đại số quan hệ:**
  - **순수 관계 연산자 (Toán tử quan hệ thuần túy):**
    1. **Select ($\sigma$ - Sigma):** Lọc các bộ (tuple) thỏa mãn điều kiện chọn $\rightarrow$ **Phép toán ngang (`수평 연산`)**.
    2. **Project ($\pi$ - Pi):** Trích xuất danh sách các thuộc tính (cột) được yêu cầu $\rightarrow$ **Phép toán dọc (`수직 연산`)**. Tự động loại bỏ các hàng trùng lặp trong kết quả.
    3. **Join ($\bowtie$ - Bowtie):** Kết hợp hai quan hệ thành một quan hệ mới dựa trên thuộc tính chung.
    4. **Division ($\div$ - Phép chia):** Tìm các bộ trong quan hệ $R$ có chứa toàn bộ tập thuộc tính của quan hệ $S$.
  - **일반 집합 연산자 (Toán tử tập hợp thông thường):**
    - **Hợp (`UNION`, $\cup$):** Gộp hai bảng có cùng cấu trúc; loại bỏ bộ trùng lặp.
    - **Giao (`INTERSECTION`, $\cap$):** Lấy các bộ xuất hiện ở cả hai bảng.
    - **Hiệu (`DIFFERENCE`, $-$):** Lấy các bộ có trong bảng $R$ nhưng không có trong bảng $S$.
    - **Tích Đề-các (`CARTESIAN PRODUCT`, $\times$):** Tạo tất cả các cặp kết hợp giữa hai bảng.
      - **Bậc kết quả (Degree):** $Degree(R \times S) = Degree(R) + Degree(S)$
      - **Lượng số kết quả (Cardinality):** $Cardinality(R \times S) = Cardinality(R) \times Cardinality(S)$
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Đại số quan hệ là ngôn ngữ gì?"* $\rightarrow$ Đáp án: **절차적 언어 (Ngôn ngữ thủ tục)**. (Ngược lại, Đại số giải tích quan hệ `관계해석` là **비절차적 언어 - phi thủ tục**).
  - Đề hỏi: *"Phép toán Select lọc hàng hay lọc cột?"* $\rightarrow$ **Select lọc hàng (hàng ngang - 수평 연산)**; **Project lọc cột (cột dọc - 수직 연산)**.
  - Phép toán Cartesian Product có Degree bằng phép cộng ($+$) và Cardinality bằng phép nhân ($\times$). Nhớ kỹ không được đảo ngược!

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa trực quan Cartesian Product:**
  - Bảng $R$ có 3 sinh viên (Cardinality = 3), gồm 2 cột `(MaSV, TenSV)` (Degree = 2).
  - Bảng $S$ có 4 môn học (Cardinality = 4), gồm 3 cột `(MaMH, TenMH, SoTinChi)` (Degree = 3).
  - Kết quả phép nhân $R \times S$:
    - Bậc mới: $2 + 3 = 5$ thuộc tính `(MaSV, TenSV, MaMH, TenMH, SoTinChi)`.
    - Lượng số mới: $3 \times 4 = 12$ hàng kết hợp.
- **Ý nghĩa thực tế của Toàn vẹn tham chiếu trong hệ quản trị CSDL:**
  - Khi xóa hoặc sửa dữ liệu ở bảng cha (bảng được tham chiếu), hệ thống thường cung cấp các tùy chọn:
    - `RESTRICT / NO ACTION`: Chặn thao tác nếu còn dữ liệu con tham chiếu đến.
    - `CASCADE`: Tự động xóa/sửa hàng loạt ở bảng con khi bảng cha thay đổi.
    - `SET NULL`: Tự động gán khóa ngoại ở bảng con thành `NULL`.

### 복습 체크리스트
- [ ] Kể tên và giải thích được 4 loại toàn vẹn: 개체 무결성, 참조 무결성, 도메인 무결성, 사용자 정의 무결성.
- [ ] Phân biệt được Select là phép toán ngang (수평 연산) và Project là phép toán dọc (수직 연산).
- [ ] Tính được Degree và Cardinality của phép tích Cartesian Product ($+$, $\times$).
- [ ] Khẳng định được 관계대수 là 절차적 언어 (ngôn ngữ thủ tục).
