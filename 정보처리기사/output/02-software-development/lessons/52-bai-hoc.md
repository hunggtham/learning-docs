# 15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)

## 학습 목표 (Mục tiêu)
- Phân biệt rạch ròi hai phương pháp kiểm thử phần mềm nền tảng: Kiểm thử hộp trắng (화이트박스 테스트 - White-box Testing) và Kiểm thử hộp đen (블랙박스 테스트 - Black-box Testing).
- Nắm vững các kỹ thuật kiểm thử hộp trắng: Kiểm tra đường dẫn cơ sở (기초 경로 검사 - Basis Path Testing) và Kiểm tra cấu trúc điều khiển (제어 구조 검사: Điều kiện, Vòng lặp, Luồng dữ liệu).
- Nằm lòng các kỹ thuật kiểm thử hộp đen kinh điển: Phân vùng tương đương (동치 분할), Phân tích giá trị biên (경계값 분석), Đồ thị nguyên nhân - kết quả (원인-효과 그래프), Đoán lỗi (오류 예측) và Kiểm thử so sánh (비교 검사).

## 핵심 키워드 (Từ khóa)
- 화이트박스 테스트 (White-box Testing / 구조 테스트 / 로직 검증)
- 기초 경로 검사 (Basis Path Testing / 맥케이브 복잡도)
- 제어 구조 검사 (Control Structure Testing: 조건, 루프, 데이터 흐름)
- 블랙박스 테스트 (Black-box Testing / 기능 테스트 / 요구사항 검증)
- 동치 분할 (Equivalence Partitioning) & 경계값 분석 (Boundary Value Analysis)
- 원인-효과 그래프 (Cause-Effect Graphing) & 오류 예측 (Error Guessing)

## 선행·연결 개념 (Kiến thức liên kết)
- [35-bai-hoc.md](35-bai-hoc.md): Kiểm thử mô-đun đơn vị và xây dựng Test Case.
- [53-bai-hoc.md](53-bai-hoc.md): Các cấp độ kiểm thử phần mềm (Unit, Integration, System, Acceptance).
- [59-bai-hoc.md](59-bai-hoc.md): Các tiêu chí độ phủ (Coverage) trong kiểm thử hộp trắng.
- [65-bai-hoc.md](65-bai-hoc.md): Chi tiết các kỹ thuật thiết kế ca kiểm thử hộp đen.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh từ khóa phân loại đề thi:
  - Cứ thấy **"원시 코드 (Mã nguồn)", "내부 논리 구조 (Cấu trúc logic nội bộ)", "제어 흐름 (Luồng điều khiển)", "경로 (Đường dẫn)"** $\rightarrow$ **화이트박스 (White-box)**.
  - Cứ thấy **"요구사항 명세서 (Đặc tả yêu cầu)", "인터페이스 입출력 (Đầu vào/Đầu ra)", "동치 분할", "경계값"** $\rightarrow$ **블랙박스 (Black-box)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh đối đầu toàn diện White-box vs Black-box Testing:**

| Tiêu chí so sánh | 화이트박스 테스트 (White-box Testing) | 블랙박스 테스트 (Black-box Testing) |
| :--- | :--- | :--- |
| **Tên gọi khác** | Kiểm thử cấu trúc (Structural), Glass-box, Clear-box | Kiểm thử chức năng (Functional), Opaque-box |
| **Đối tượng kiểm tra** | **Mã nguồn (Source Code) và cấu trúc logic bên trong** | **Chức năng nghiệp vụ và dữ liệu vào/ra (I/O)** |
| **Góc nhìn kiểm thử** | Góc nhìn của **Lập trình viên (Developer)** | Góc nhìn của **Người dùng cuối (User) hoặc Tester** |
| **Thời điểm áp dụng** | Chủ yếu ở tầng **Kiểm thử đơn vị (Unit Test)** | Chủ yếu ở tầng **Tích hợp, Hệ thống, Chấp nhận (System / Acceptance Test)** |
| **Mục tiêu chính** | Tìm lỗi thuật toán, vòng lặp vô hạn, nhánh lệnh chết (Dead Code), rò rỉ bộ nhớ | Tìm lỗi thiếu chức năng, giao diện sai lệch, lỗi cơ sở dữ liệu, lỗi hiệu năng |

- **Bảng phân loại các kỹ thuật kiểm thử cốt lõi (Rất hay hỏi xếp nhóm):**

| Nhóm kiểm thử | Các kỹ thuật thiết kế ca kiểm thử tiêu biểu (Từ khóa đề thi) |
| :--- | :--- |
| **화이트박스 (White-box)** | 1. **기초 경로 검사 (Basis Path Testing):** Dùng độ phức tạp McCabe để xác định tập đường đi độc lập cơ sở; 2. **조건 검사 (Condition Testing):** Kiểm tra các điều kiện logic boolean; 3. **루프 검사 (Loop Testing):** Kiểm tra giới hạn của các vòng lặp (while, for); 4. **데이터 흐름 검사 (Data Flow Testing):** Kiểm tra vòng đời biến số (Định nghĩa $\rightarrow$ Sử dụng $\rightarrow$ Hủy bỏ). |
| **블랙박스 (Black-box)** | 1. **동치(동등) 분할 (Equivalence Partitioning):** Chia miền dữ liệu thành các lớp tương đương hợp lệ và không hợp lệ, lấy 1 giá trị đại diện; 2. **경계값 분석 (Boundary Value Analysis):** Chọn các giá trị nằm ngay sát đường biên ($min, min+1, max-1, max$); 3. **원인-효과 그래프 (Cause-Effect Graphing):** Dùng đồ thị logic (AND, OR, NOT) biểu diễn quan hệ giữa đầu vào và đầu ra; 4. **오류 예측 (Error Guessing):** Dựa vào trực giác và kinh nghiệm của tester để phán đoán lỗi tiềm ẩn; 5. **비교 검사 (Comparison Testing):** Chạy cùng một bộ dữ liệu trên nhiều phiên bản phần mềm để so sánh kết quả. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Độ phức tạp vòng McCabe (Cyclomatic Complexity - $V(G)$):**
  - Trong kỹ thuật kiểm tra đường dẫn cơ sở (Basis Path Testing), Thomas McCabe đưa ra công thức tính số lượng ca kiểm thử tối thiểu cần thiết để bao phủ toàn bộ các đường đi độc lập trong đồ thị luồng điều khiển:
    $$V(G) = E - N + 2$$
    *(Với $E$ là số cạnh 간선, $N$ là số nút 정점 trong đồ thị luồng)*
    Hoặc: $V(G) = P + 1$ (với $P$ là số nút điều kiện rẽ nhánh / Predicate Nodes).

### 복습 체크리스트
- [ ] Phân biệt được bản chất White-box (nhìn thấy code) và Black-box (chỉ nhìn Input/Output).
- [ ] Nhớ tên các kỹ thuật White-box: Basis Path, Condition, Loop, Data Flow.
- [ ] Nhớ tên các kỹ thuật Black-box: Equivalence Partitioning, Boundary Value, Cause-Effect, Error Guessing, Comparison.
- [ ] Áp dụng đúng công thức McCabe: $V(G) = E - N + 2$ hoặc $P + 1$.
