# 095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)

## 학습 목표 (Mục tiêu)
- Định nghĩa Kiểm thử mô-đun đơn vị (단위 모듈 테스트 - Unit Test) với tư cách là tầng kiểm thử đầu tiên được tiến hành ngay sau khi hoàn thành việc viết mã.
- Hiểu rõ việc áp dụng chủ đạo phương pháp Kiểm thử hộp trắng (화이트박스 테스트 - White-box Test) trong kiểm thử đơn vị để rà soát lỗi cấu trúc logic và thuật toán.
- Định nghĩa Bộ ca kiểm thử (테스트 케이스 - Test Case) gồm 3 thành phần cốt lõi: Giá trị đầu vào, Điều kiện thực thi và Kết quả kỳ vọng; nắm vững nguyên tắc vàng: **Bắt buộc phải biên soạn Test Case từ trước khi tiến hành kiểm thử**.

## 핵심 키워드 (Từ khóa)
- 단위 모듈 테스트 (Unit Module Test)
- 화이트박스 테스트 (White-box Testing)
- 알고리즘 및 로직 검증 (Algorithm & Logic Verification)
- 테스트 케이스 (Test Case)
- 입력 값 (Input Value)
- 실행 조건 (Execution Condition)
- 기대 결과 (Expected Result)
- 사전에 정의 (Pre-defined / Must be written in advance)

## 선행·연결 개념 (Kiến thức liên kết)
- [32-bai-hoc.md](32-bai-hoc.md): Trình tự 4 bước triển khai mô-đun (Test là bước thứ 4 sau Compile).
- [33-bai-hoc.md](33-bai-hoc.md): Bản đặc tả chức năng đơn vị làm cơ sở xây dựng Test Case.
- [52-bai-hoc.md](52-bai-hoc.md): So sánh tổng quan Kiểm thử hộp trắng (White-box) và Kiểm thử hộp đen (Black-box).

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi nhắc đến: **"코딩 직후 최소 단위인 모듈이나 컴포넌트에 초점을 맞춘 테스트"** (Kiểm thử tập trung vào đơn vị nhỏ nhất ngay sau khi viết code) $\rightarrow$ Khẳng định ngay **단위 테스트 (Unit Test)**.
- Ghi nhớ 3 thành phần không thể thiếu của một Test Case: **Đầu vào (Input) + Điều kiện (Condition) + Kết quả mong đợi (Expected Output)**.
- Nhớ quy tắc quản lý: Test Case **phải được soạn thảo trước (사전에 정의)** để tránh lãng phí nhân lực và thời gian thử nghiệm mò mẫm.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Đặc trưng của Kiểm thử mô-đun đơn vị (단위 모듈 테스트 - Unit Test):**
  - **Thời điểm thực hiện:** Tiến hành ngay sau khi lập trình viên hoàn tất việc viết code và biên dịch thành công cho từng mô-đun riêng lẻ.
  - **Mục tiêu:** Rà soát và phát hiện các sai sót về thuật toán, tính toán số học sai, vòng lặp vô hạn, xử lý sai điều kiện biên và xung đột giao tiếp dữ liệu nội tại.
  - **Phương pháp kiểm thử chủ đạo:** **Kiểm thử hộp trắng (화이트박스 테스트 - White-box Test)** - Người kiểm thử nhìn thấy toàn bộ mã nguồn bên trong để kiểm tra các nhánh lệnh (Branch Coverage), câu lệnh (Statement Coverage) và điều kiện logic (Condition Coverage).
- **Khái niệm và Cấu trúc của Test Case (테스트 케이스):**
  - **Định nghĩa:** Là tập tài liệu kỹ thuật chứa các thông số cụ thể được thiết kế có chủ đích để kiểm chứng xem phần mềm có thỏa mãn đúng yêu cầu đề ra hay không.
  - **3 thành phần cốt lõi của một Test Case chuẩn:**
    1. **입력 값 (Input Value):** Dữ liệu mẫu truyền vào hàm/mô-đun (bao gồm cả dữ liệu hợp lệ và dữ liệu dị thường/biên).
    2. **실행 조건 (Execution Condition / Pre-condition):** Môi trường hệ thống, trạng thái dữ liệu và các điều kiện tiên quyết cần có trước khi bấm chạy test.
    3. **기대 결과 (Expected Result):** Kết quả chính xác mà hàm phải trả về nếu mã nguồn hoạt động hoàn toàn đúng.
  - **Nguyên tắc quản lý chất lượng:**
    - **테스트 케이스는 반드시 사전에 작성되어야 한다 (Test Case bắt buộc phải được định nghĩa từ trước).**
    - Nếu kiểm thử tự do không có Test Case định trước (Ad-hoc Testing), kiểm thử viên sẽ dễ bị thiên kiến xác nhận, bỏ sót các trường hợp ngoại lệ và gây lãng phí nhân lực trầm trọng.

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Thành phần nào sau đây KHÔNG THUỘC cấu trúc cơ bản của một Test Case?"* $\rightarrow$ 3 thành phần chuẩn là Input, Condition, Expected Result. Các đáp án đưa ra như "Source Code", "Tên lập trình viên" là đáp án nhiễu.
  - **Bẫy 2:** *"Phương pháp kiểm thử nào được sử dụng chủ yếu trong kiểm thử đơn vị?"* $\rightarrow$ Đáp án: **화이트박스 테스트 (White-box Testing)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kiểm thử tự động hóa đơn vị (Unit Testing Frameworks):**
  - Trong công nghệ phần mềm thực tế, kiểm thử đơn vị hiện đại được tự động hóa hoàn toàn thông qua các bộ khung kiểm thử nổi tiếng:
    - **JUnit** (dành cho Java).
    - **NUnit** (dành cho .NET/C#).
    - **PyTest / Unittest** (dành cho Python).
    - **Jest / Mocha** (dành cho JavaScript/TypeScript).
  - Đây là nền tảng sống còn để vận hành phương pháp luận Phát triển hướng kiểm thử **TDD (Test-Driven Development)**: Viết Test Case thất bại trước $\rightarrow$ Viết Code vừa đủ để Test Pass $\rightarrow$ Tái cấu trúc Refactoring.

### 복습 체크리스트
- [ ] Định nghĩa Unit Test là kiểm thử đơn vị nhỏ nhất ngay sau khi viết code.
- [ ] Nhớ phương pháp chủ đạo trong Unit Test là White-box Testing.
- [ ] Nằm lòng 3 thành phần cốt lõi của Test Case: Input, Condition, Expected Result.
- [ ] Khẳng định quy tắc bắt buộc: Test Case phải được biên soạn từ trước (사전에 정의).
