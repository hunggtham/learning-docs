# 핵심 031: 모듈 구현 (Module Implementation)

## 학습 목표 (Mục tiêu)
- Định nghĩa khái niệm Triển khai mô-đun (모듈 구현 - Module Implementation / Coding) với tư cách là giai đoạn chuyển hóa bản vẽ thiết kế thành mã nguồn thực thi.
- Nằm lòng trình tự 4 bước chuẩn tắc trong quy trình triển khai mô-đun: Lập kế hoạch mã hóa $\rightarrow$ Viết mã $\rightarrow$ Biên dịch $\rightarrow$ Kiểm thử đơn vị.
- Phân biệt rõ sự khác nhau giữa Mô-đun (Module - Đơn vị chức năng mã nguồn) và Thành phần (Component - Khối phần mềm đóng gói độc lập giao tiếp qua Interface).

## 핵심 키워드 (Từ khóa)
- 모듈 구현 (Module Implementation / Coding)
- 구현 작업 절차 (Coding Plan → Coding → Compile → Test)
- 코딩 계획 (Coding Plan) & 코딩 (Coding)
- 컴파일 (Compile) & 테스트 (Test)
- 모듈 (Module) vs 컴포넌트 (Component)
- 인터페이스 기반 재사용 (Interface-based Reuse)

## 선행·연결 개념 (Kiến thức liên kết)
- [31-bai-hoc.md](31-bai-hoc.md): Định nghĩa 단위 모듈 (Unit Module) và các cơ chế IPC.
- [33-bai-hoc.md](33-bai-hoc.md): Nguyên tắc viết bản đặc tả chức năng mô-đun (Abstraction, Structuring, Information Hiding).
- [35-bai-hoc.md](35-bai-hoc.md): Kiểm thử mô-đun đơn vị và xây dựng Test Case.

## 읽는 방법 (Cách đọc)
- Học thuộc trình tự 4 bước: **Kế hoạch $\rightarrow$ Code $\rightarrow$ Compile $\rightarrow$ Test** (코딩 계획 $\rightarrow$ 코딩 $\rightarrow$ 컴파일 $\rightarrow$ 테스트).
- Nắm vững cặp khái niệm Module vs Component:
  - Module: Đơn vị mã nguồn (Source Code level) được gom lại để tạo nên chương trình.
  - Component: Khối nhị phân đóng gói độc lập (Binary Component level), cắm vào hệ thống qua giao diện **Interface** mà không cần sửa code bên trong.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của Triển khai phần mềm (구현 - Implementation):**
  - Là quá trình hiện thực hóa các bản vẽ đặc tả thiết kế (Design Specifications) thành mã nguồn chương trình bằng các ngôn ngữ lập trình cụ thể để máy tính có thể hiểu và thực thi được.
- **Trình tự 4 bước triển khai mô-đun chuẩn:**
  $$\mathbf{코딩\ 계획 (Lập\ kế\ hoạch)} \longrightarrow \mathbf{코딩 (Viết\ mã)} \longrightarrow \mathbf{컴파일 (Biên\ dịch)} \longrightarrow \mathbf{테스트 (Kiểm\ thử)}$$
  1. **코딩 계획 (Coding Planning):** Xác định chuẩn quy ước đặt tên (Coding Conventions), môi trường phát triển (IDE), các thư viện dùng chung và phân công nhiệm vụ.
  2. **코딩 (Coding / Programming):** Tiến hành viết mã nguồn logic xử lý theo đúng thuật toán và tài liệu thiết kế chi tiết.
  3. **컴파일 (Compilation):** Sử dụng trình biên dịch để chuyển mã nguồn sang mã máy/mã byte, phát hiện và sửa sạch các lỗi cú pháp (Syntax Errors).
  4. **테스트 (Unit Testing):** Thực thi các ca kiểm thử đơn vị để xác minh tính đúng đắn của logic thuật toán.

- **So sánh chi tiết Mô-đun (Module) vs Thành phần (Component):**

| Tiêu chí | 모듈 (Module) | 컴포넌트 (Component) |
| :--- | :--- | :--- |
| **Cấp độ trừu tượng** | Cấp độ mã nguồn phần mềm (Class, File mã nguồn, Thư viện hàm) | Cấp độ khối nhị phân đóng gói hoàn chỉnh (Executable, DLL, JAR, Web Service) |
| **Tính độc lập** | Phụ thuộc vào mã nguồn và ngôn ngữ của toàn dự án | **Hoàn toàn độc lập**, có thể tồn tại và phân phối riêng rẽ |
| **Phương thức giao tiếp** | Lời gọi hàm nội bộ, truyền tham số biến trực tiếp | **Chỉ giao tiếp thông qua giao diện chuẩn (인터페이스 - Interface)** |
| **Mục đích thiết kế** | Tách nhỏ bài toán để dễ lập trình và quản lý cấu trúc | **Tái sử dụng lắp ghép (Plug & Play)** linh hoạt giữa nhiều hệ thống khác nhau |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Chuẩn mực mã sạch (Clean Code) trong triển khai mô-đun:**
  - Mô-đun triển khai đạt chuẩn chất lượng phải tuân thủ các tiêu chí:
    - **가독성 (Readability):** Mã nguồn rõ ràng, tường minh, đặt tên biến và hàm theo đúng quy ước CamelCase hoặc snake_case.
    - **단순성 (Simplicity):** Tránh các cấu trúc logic lồng nhau quá sâu (Deep Nesting), hạn chế phân nhánh phức tạp.
    - **의존성 배제 (Loose Coupling):** Không phụ thuộc trực tiếp vào biến toàn cục, chỉ tương tác qua tham số.

### 복습 체크리스트
- [ ] Định nghĩa Implementation là quá trình chuyển thiết kế thành mã thực thi.
- [ ] Đọc đúng thứ tự 4 bước: 코딩 계획 $\rightarrow$ 코딩 $\rightarrow$ 컴파일 $\rightarrow$ 테스트.
- [ ] Phân biệt được sự khác nhau căn bản giữa Module (mã nguồn) và Component (đóng gói qua Interface).
- [ ] Nêu được vai trò của giai đoạn Compile (bắt lỗi cú pháp) và Test (bắt lỗi logic).
