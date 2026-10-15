# 127 ~ 129: 화이트박스 테스트 (White Box Test)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất và phạm vi ứng dụng của Kiểm thử hộp trắng (화이트박스 테스트 - White-box Testing) trong việc phân tích mã nguồn và luồng điều khiển logic nội bộ.
- Thành thạo các kỹ thuật thiết kế ca kiểm thử hộp trắng: Kiểm tra đường dẫn cơ sở (기초 경로 검사 - Basis Path Testing) và Kiểm tra cấu trúc điều khiển (Điều kiện, Vòng lặp, Luồng dữ liệu).
- Áp dụng chuẩn xác các tiêu chí độ phủ mã nguồn (Statement, Decision, Condition, Multiple Condition Coverage) để đánh giá độ tin cậy của bộ ca kiểm thử đơn vị.

## 핵심 키워드 (Từ khóa)
- 화이트박스 테스트 (White-box Testing)
- 내부 로직 및 제어 구조 (Internal Logic & Control Structure)
- 기초 경로 검사 (Basis Path Testing)
- 맥케이브 순환 복잡도 (McCabe Cyclomatic Complexity: $E - N + 2$)
- 제어 구조 검사 (조건, 루프, 데이터 흐름 검사)
- 코드 커버리지 (Code Coverage: 문장, 분기, 조건, 다중조건)

## 선행·연결 개념 (Kiến thức liên kết)
- [52-bai-hoc.md](52-bai-hoc.md): So sánh tổng quan White-box và Black-box Testing.
- [59-bai-hoc.md](59-bai-hoc.md): Các tiêu chuẩn độ phủ White-box Coverage Criteria.
- [65-bai-hoc.md](65-bai-hoc.md): Đối chiếu với phương pháp Kiểm thử hộp đen (Black-box Test).

## 읽는 방법 (Cách đọc)
- Nhớ các từ khóa định danh: **내부 로직 (Logic nội bộ)**, **제어 흐름 (Luồng điều khiển)**, **원시 코드 (Mã nguồn)** $\rightarrow$ Thuộc về **화이트박스**.
- Công thức tính độ phức tạp McCabe khi làm bài tập hình học luồng:
  - Đếm số cạnh $E$, số đỉnh $N \rightarrow V(G) = E - N + 2$.
  - Đếm số vùng kín (Regions) hoặc số nút điều kiện rẽ nhánh $P \rightarrow V(G) = P + 1$.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của White-box Testing:**
  - Là phương pháp kiểm thử mà kiểm thử viên (hoặc lập trình viên) có toàn quyền xem xét và phân tích cấu trúc mã nguồn bên trong của chương trình.
  - Mục tiêu: Kiểm tra xem các câu lệnh có được thực thi đúng không, các nhánh điều kiện True/False có hoạt động chuẩn không, các vòng lặp có điểm dừng an toàn không và các biến dữ liệu có bị dùng trước khi khởi tạo không.
- **Các kỹ thuật thiết kế ca kiểm thử hộp trắng:**
  1. **기초 경로 검사 (Basis Path Testing):**
     - Do Tom McCabe đề xuất. Chuyển đổi mã nguồn thành Đồ thị luồng điều khiển (Control Flow Graph).
     - Tính toán **Độ phức tạp vòng (순환 복잡도 - Cyclomatic Complexity: $V(G)$)** để xác định số lượng đường đi độc lập tuyến tính tối thiểu cần phải kiểm tra.
     - **Công thức tính $V(G)$:**
       $$V(G) = E - N + 2 = P + 1 = \text{Số vùng kín (Regions)}$$
       *(Với $E$ là số cạnh, $N$ là số nút, $P$ là số nút điều kiện có từ 2 nhánh rẽ trở lên)*
  2. **제어 구조 검사 (Control Structure Testing):**
     - **조건 검사 (Condition Testing):** Tập trung kiểm tra các biểu thức logic boolean độc lập bên trong câu lệnh điều kiện.
     - **루프 검사 (Loop Testing):** Kiểm tra các vòng lặp (Đơn giản, Lồng nhau, Nối tiếp) tại các giá trị biên: 0 lần lặp, 1 lần lặp, 2 lần lặp, $m$ lần lặp và $n$ lần lặp tối đa.
     - **데이터 흐름 검사 (Data Flow Testing):** Kiểm tra chu kỳ sống của các biến từ lúc định nghĩa (Define), gán giá trị, sử dụng (Use) cho đến khi hủy (Kill).

- **Thứ bậc các tiêu chuẩn độ phủ (Code Coverage):**
  $$\text{문장 (Statement)} \le \text{분기/결정 (Branch/Decision)} \le \text{조건/분기 (Condition/Branch)} \le \text{다중 조건 (Multiple Condition)}$$

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán mẫu tính McCabe Cyclomatic Complexity trong đề thi:**
  - Cho đồ thị luồng có $E = 11$ cạnh và $N = 9$ nút.
  - Tính số đường đi độc lập cơ sở $V(G)$:
    $$V(G) = 11 - 9 + 2 = \mathbf{4}$$
  - Kết luận: Kiểm thử viên cần thiết kế ít nhất **4 Test Cases** độc lập để bao phủ toàn bộ các nhánh logic của hàm này.

### 복습 체크리스트
- [ ] Định nghĩa White-box Testing là kiểm thử dựa trên mã nguồn và luồng điều khiển nội bộ.
- [ ] Áp dụng chuẩn xác công thức McCabe: $V(G) = E - N + 2 = P + 1$.
- [ ] Kể tên 3 dạng kiểm tra cấu trúc điều khiển: Điều kiện, Vòng lặp, Luồng dữ liệu.
- [ ] Nhớ thứ bậc độ phủ từ yếu nhất (Statement) đến mạnh nhất (Multiple Condition).
