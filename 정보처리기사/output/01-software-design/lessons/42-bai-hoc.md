# 5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 phép toán đại số quan hệ thuần túy: Chọn hàng (`Select` - $\sigma$), Chọn cột (`Project` - $\pi$), Nối (`Join` - $\bowtie$), và Chia (`Division` - $\div$).
- Phân biệt bản chất 3 hiện tượng bất thường trong cơ sở dữ liệu chưa chuẩn hóa: Bất thường chèn (`삽입 이상`), Bất thường xóa (`삭제 이상`), và Bất thường cập nhật (`갱신 이상`).
- Thuộc nằm lòng thứ tự và điều kiện chuyển đổi của 6 cấp độ chuẩn hóa cơ sở dữ liệu qua câu thần chú kinh điển: **도 - 부 - 이 - 결 - 다 - 조**.

## 핵심 키워드 (Từ khóa)
- 관계대수 (Đại số quan hệ / Relational Algebra / 절차적 언어)
- 순수 관계 연산자 (Select $\sigma$, Project $\pi$, Join $\bowtie$, Division $\div$)
- 카티션 프로덕트 (Tích Descartes $\times$ / Degree cộng, Cardinality nhân)
- 이상 현상 (Hiện tượng bất thường / Anomalies: 삽입, 삭제, 갱신)
- 정규화 6단계 (6 cấp độ chuẩn hóa: 1NF, 2NF, 3NF, BCNF, 4NF, 5NF)
- 도·부·이·결·다·조 (Nguyên tử, Từng phần, Bắc cầu, Định danh, Đa trị, Kết nối)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([4. 관계형 데이터베이스 구조](41-bai-hoc.md)):** Sau khi xây dựng cấu trúc bảng và các ràng buộc khóa, bài này cung cấp các phép toán thao tác dữ liệu và quy trình chuẩn hóa triệt tiêu dư thừa dữ liệu.
- **Tiếp nối sang bài sau ([6. SQL과 객체, 시스템 개념](43-bai-hoc.md)):** Chuyển từ đại số quan hệ lý thuyết sang ngôn ngữ truy vấn thực tế SQL, đối tượng View và tính chất giao dịch ACID.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc làu câu thần chú chuẩn hóa **도 - 부 - 이 - 결 - 다 - 조** và ký hiệu đại số quan hệ ($\sigma$ chọn hàng, $\pi$ chọn cột).
- Đọc TẦNG B để theo dõi bài toán mẫu tính Degree và Cardinality khi thực hiện phép tích Descartes ($R \times S$).

---

## 5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phép toán Đại số quan hệ (관계대수 - Relational Algebra):**
  - Là ngôn ngữ thao tác dữ liệu mang tính **Thủ tục (`절차적 언어`)**, chỉ rõ trình tự các bước hệ thống phải làm thế nào để thu được tập kết quả mong muốn.
  - **4 phép toán đại số quan hệ thuần túy (순수 관계 연산자):**
    1. `Select (셀렉트 - Ký hiệu: σ / Sigma)`: Chọn ra tập hợp các **HÀNG (튜플 - Tuples)** thỏa mãn điều kiện logic (cắt lát ngang bảng dữ liệu).
    2. `Project (프로젝트 - Ký hiệu: π / Pi)`: Chọn ra tập hợp các **CỘT (속성 - Attributes)** được chỉ định (cắt lát dọc bảng dữ liệu).
    3. `Join (조인 - Ký hiệu: ⋈ / Bowtie)`: Kết hợp các hàng từ hai bảng khác nhau dựa trên điều kiện so sánh giá trị của thuộc tính chung.
    4. `Division (디비전 - Ký hiệu: ÷)`: Tìm các bộ trong bảng A có chứa toàn bộ các giá trị thuộc tính xuất hiện trong bảng B.
  - **Quy tắc tính kích thước phép Tích Descartes ($R \times S$):**
    - $\text{Bậc mới (Degree)} = \text{Degree}(R) + \text{Degree}(S)$ (Cộng số cột).
    - $\text{Lực lượng mới (Cardinality)} = \text{Cardinality}(R) \times \text{Cardinality}(S)$ (Nhân số hàng).
- **2. 3 hiện tượng bất thường trong CSDL chưa chuẩn hóa (이상 현상 - Anomalies):**
  - `삽입 이상 (Insertion Anomaly - Bất thường chèn)`: Khi muốn thêm một dữ liệu mới, ta buộc phải nhập kèm theo những dữ liệu không mong muốn hoặc chưa có sẵn (ví dụ: muốn thêm môn học mới nhưng chưa có sinh viên đăng ký thì không chèn được vì mã sinh viên là khóa chính).
  - `삭제 이상 (Deletion Anomaly - Bất thường xóa)`: Khi xóa một mẩu thông tin nào đó, ta vô tình làm mất luôn những thông tin quan trọng khác đi kèm (ví dụ: sinh viên duy nhất hủy môn học làm hệ thống xóa luôn thông tin về môn học đó).
  - `갱신 이상 (Update Anomaly - Bất thường cập nhật)`: Khi chỉnh sửa một giá trị thuộc tính bị trùng lặp ở nhiều hàng, nếu chỉ sửa ở một vài hàng mà quên sửa các hàng khác sẽ dẫn đến mâu thuẫn dữ liệu trong cùng một bảng.
- **3. Quy trình 6 cấp độ chuẩn hóa (정규화 - Normalization):**
  - **Mục đích:** Loại bỏ dư thừa dữ liệu (Data Redundancy) và triệt tiêu 3 hiện tượng bất thường.
  - **Thần chú thứ tự 6 cấp độ chuẩn hóa (Bắt buộc phải thuộc):**
    $$\mathbf{도 \rightarrow 부 \rightarrow 이 \rightarrow 결 \rightarrow 다 \rightarrow 조}$$
    - **1NF (제1정규형):** **도** (`도메인이 원자값`) - Tất cả các giá trị thuộc tính trong bảng đều là **giá trị nguyên tử (Atomic Value)**, loại bỏ thuộc tính đa trị hoặc mảng lặp lại.
    - **2NF (제2정규형):** **부** (`부분적 함수 종속 제거`) - Loại bỏ phụ thuộc hàm từng phần, đạt **phụ thuộc hàm hoàn toàn (완전 함수 종속)** vào khóa chính phức hợp.
    - **3NF (제3정규형):** **이** (`이행적 함수 종속 제거`) - Loại bỏ phụ thuộc hàm bắc cầu ($X \rightarrow Y$ và $Y \rightarrow Z$ thì $X \rightarrow Z$).
    - **BCNF (보이스-코드 정규형):** **결** (`결정자이면서 후보키가 아닌 것 제거`) - Mọi thuộc tính quyết định (Determinant) đều phải là Khóa ứng viên (Candidate Key).
    - **4NF (제4정규형):** **다** (`다치 종속 제거`) - Loại bỏ phụ thuộc đa trị (Multivalued Dependency - MVD).
    - **5NF (제5정규형):** **조** (`조인 종속성 이용`) - Loại bỏ phụ thuộc kết nối (Join Dependency), đảm bảo phép phân rã không mất mát thông tin (Lossless Join).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1 (Ký hiệu Select vs Project):** Chọn hàng là gì? -> **$\sigma$ (Sigma / Select)**. Chọn cột là gì? -> **$\pi$ (Pi / Project)**.
  - **Bẫy 2 (Thứ tự chuẩn hóa):** Loại bỏ phụ thuộc bắc cầu đưa bảng lên dạng chuẩn nào? -> **3NF (제3정규형 - chữ "이")**.
  - **Bẫy 3:** *"Bảng có khóa chính đơn (1 thuộc tính duy nhất) và đã đạt 1NF thì tự động đạt 2NF?"* -> **Đúng**, vì không thể có phụ thuộc từng phần vào khóa đơn.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Select xẻ hàng, Project chọn cột; Chuẩn hóa 6 bước thần chú Đô - Phụ - Di - Quyết - Đa - Tổ (도-부-이-결-다-조)".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ minh họa tính toán Cartesian Product ($R \times S$):**
  - Bảng $R$ có 3 cột, 4 hàng.
  - Bảng $S$ có 2 cột, 5 hàng.
  - Kết quả phép tích Descartes $R \times S$ sẽ có:
    - Bậc (Degree / số cột) = $3 + 2 = 5$ cột.
    - Lực lượng (Cardinality / số hàng) = $4 \times 5 = 20$ hàng.
- **Minh họa phụ thuộc hàm bắc cầu (3NF):**
  - Bảng `Sinh_Vien`: `Mã_SV` $\rightarrow$ `Mã_Khoa`, và `Mã_Khoa` $\rightarrow$ `Tên_Khoa`.
  - Ở đây tồn tại phụ thuộc bắc cầu `Mã_SV` $\rightarrow$ `Tên_Khoa`. Chuẩn hóa lên 3NF bằng cách tách thành 2 bảng: `Sinh_Vien (Mã_SV, Mã_Khoa)` và `Khoa (Mã_Khoa, Tên_Khoa)`.

### 복습 체크리스트
- [ ] Nhận diện đúng ký hiệu toán học: Select ($\sigma$), Project ($\pi$), Join ($\bowtie$), Division ($\div$).
- [ ] Tính đúng Degree (cộng) và Cardinality (nhân) của phép tích Descartes.
- [ ] Phân biệt được 3 hiện tượng bất thường: 삽입, 삭제, 갱신 이상.
- [ ] Đọc vanh vách 6 bước chuẩn hóa theo thần chú: 도 - 부 - 이 - 결 - 다 - 조.
