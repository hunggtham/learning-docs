# Môn 2 · Bài 16 — Kiểm thử hộp đen và kỹ thuật thiết kế Test Case

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Nếu như [Bài 15: Kiểm thử hộp trắng và độ bao phủ kiểm thử](15-kiem-thu-hop-trang-va-coverage.md) tập trung vào cấu trúc giải thuật và luồng điều khiển bên trong mã nguồn, thì bài học này chuyển sang nửa đối trọng còn lại: **명세 기반 테스트 (Kiểm thử dựa trên đặc tả)**, tức **블랙박스 테스트 (Black-Box Testing)**. Bài học trang bị toàn bộ các kỹ thuật thiết kế ca kiểm thử hộp đen kinh điển và quy chuẩn soạn thảo tài liệu Test Case, Test Scenario theo tiêu chuẩn quốc tế ISO/IEC/IEEE 29119-3.

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ các bài học cũ `52-bai-hoc.md` (phần Black-box), `56-bai-hoc.md` và `65-bai-hoc.md` (tương ứng với các mục 15, 35, 130 & 131 trong tài liệu chuẩn gốc). Toàn bộ ví dụ bài toán phân vùng biên và bảng quyết định được đối chiếu với các dạng câu hỏi thực chiến của HRDK.

> **Mạch kiến thức:** Làm thế nào để kiểm thử một hệ thống khi ta không được phép (hoặc không thể) đọc mã nguồn? Bài học này giải quyết ba vấn đề kỹ thuật: (1) Làm sao chia miền dữ liệu thành các lớp tương đương và chọn các điểm biên nhạy cảm nhất ($min, max$) để tối ưu số lượng test case? (2) Khi nào cần dùng đồ thị nguyên nhân - kết quả và bảng quyết định để mô hình hóa logic nghiệp vụ phức tạp? (3) Một bản mô tả ca kiểm thử (Test Case) và kịch bản kiểm thử (Test Scenario) chuẩn mực quốc tế gồm những thành phần nào để bảo đảm ma trận truy xuất nguồn gốc (RTM)?

---

## 1. 블랙박스 테스트의 개념과 특징 — Khái niệm và đặc điểm kiểm thử hộp đen

**블랙박스 테스트는 소프트웨어의 내부 구조나 작동 원리를 모르는 상태에서 요구사항 명세서를 기반으로 기능이 정상적으로 동작하는지 검증하는 방법이다.**

Kiểm thử hộp đen (Black-Box Testing, còn gọi là Functional Testing — Kiểm thử chức năng hay Opaque-Box Testing) là phương pháp kiểm thử mà kiểm thử viên xem hệ thống như một "chiếc hộp đen bí ẩn", hoàn toàn không nhìn thấy và không cần quan tâm đến cấu trúc mã nguồn bên trong. Thay vào đó, kiểm thử viên tập trung đưa các tập dữ liệu đầu vào (Input) hợp lệ lẫn bất hợp lệ và quan sát xem kết quả đầu ra (Output) có đáp ứng đúng như bản đặc tả yêu cầu chức năng (SRS) hay không.

### Đặc trưng bản chất
- **Đối tượng kiểm tra:** Giao diện bên ngoài (UI/API), các tính năng nghiệp vụ, dữ liệu nhập xuất và khả năng xử lý lỗi ngoại lệ.
- **Thời điểm áp dụng:** Được áp dụng chủ yếu ở các tầng cao như **통합 테스트 (Integration Test)**, **시스템 테스트 (System Test)** và **인수 테스트 (Acceptance Test)**.
- **Mục tiêu chính:** Phát hiện các tính năng bị lập trình viên bỏ sót (omission faults), lỗi tương tác giao diện người dùng, sai lệch định dạng dữ liệu vào/ra và các lỗi nghiệp vụ không đúng như khách hàng mong đợi.

---

## 2. 블랙박스 테스트 케이스 설계 기법 — Các kỹ thuật thiết kế ca kiểm thử hộp đen

Đề thi Kỹ sư Xử lý Thông tin thường xuyên kiểm tra việc nhận diện định nghĩa và áp dụng vào bài tập tình huống thực tế của các kỹ thuật kiểm thử hộp đen sau:

### 2.1. 동치(동등) 분할 (Equivalence Partitioning — Phân vùng tương đương)
- **Cơ chế:** Chia toàn bộ miền giá trị dữ liệu đầu vào của một trường thành các phân vùng logic gọi là **동치 클래스 (Equivalence Classes — Lớp tương đương)**:
  - **유효 동치 클래스 (Valid Equivalence Class):** Miền giá trị hợp lệ mà hệ thống phải chấp nhận và xử lý đúng nghiệp vụ.
  - **무효 동치 클래스 (Invalid Equivalence Class):** Miền giá trị không hợp lệ mà hệ thống phải từ chối và đưa ra thông báo lỗi phù hợp.
- **Nguyên tắc chọn mẫu:** Giả định rằng mọi giá trị trong cùng một lớp tương đương sẽ được chương trình xử lý giống hệt nhau. Do đó, **chỉ cần chọn duy nhất 1 giá trị đại diện từ mỗi lớp** để lập ca kiểm thử, giúp giảm thiểu tối đa số lượng test case mà vẫn đảm bảo độ bao phủ.
- **Ví dụ thực tế trong đề:**
  - Quy tắc: "Điểm thi của sinh viên là số nguyên từ 0 đến 100".
  - Ta chia thành 3 lớp tương đương:
    1. Lớp không hợp lệ 1: $\text{Điểm} < 0 \rightarrow$ Chọn giá trị đại diện: `-5`
    2. Lớp hợp lệ: $0 \le \text{Điểm} \le 100 \rightarrow$ Chọn giá trị đại diện: `75`
    3. Lớp không hợp lệ 2: $\text{Điểm} > 100 \rightarrow$ Chọn giá trị đại diện: `120`
  - Chỉ cần 3 Test Cases để bao phủ toàn bộ miền dữ liệu của trường này.

### 2.2. 경계값 분석 (Boundary Value Analysis — Phân tích giá trị biên)
- **Cơ chế:** Kinh nghiệm kỹ nghệ phần mềm chứng minh rằng: **Phần lớn lỗi lập trình xảy ra tại các đường ranh giới của điều kiện** (do lập trình viên dùng nhầm toán tử so sánh, ví dụ dùng `>` thay vì `>=`, hoặc `<` thay vì `<=`, lỗi lệch 1 đơn vị Off-by-one). Kỹ thuật này tập trung chọn các giá trị nằm ngay sát hai đầu mép biên để kiểm tra.
- **Quy tắc chọn điểm biên:**
  - **Phương pháp 2 điểm biên (Robustness cơ bản):** Chọn giá trị ngay tại biên ($min, max$) và giá trị ngoài biên không hợp lệ ($min - 1, max + 1$).
  - **Phương pháp 3 điểm biên (Standard BVA):** Với mỗi đường biên, chọn 3 giá trị: sát bên trong ($min + 1$), ngay tại biên ($min$), và sát bên ngoài ($min - 1$).
- **Ví dụ thực tế trong đề:**
  - Với điều kiện $0 \le \text{Điểm} \le 100$:
  - Tại biên dưới ($0$): Chọn `-1` (ngoài biên), `0` (ngay biên), `1` (trong biên).
  - Tại biên trên ($100$): Chọn `99` (trong biên), `100` (ngay biên), `101` (ngoài biên).
  - Bộ giá trị kiểm thử tối ưu: $\mathbf{\{-1, 0, 1, 99, 100, 101\}}$.

### 2.3. 원인-효과 그래프 (Cause-Effect Graphing — Đồ thị nguyên nhân - kết quả)
- **Cơ chế:** Khi hành vi của hệ thống phụ thuộc vào sự kết hợp phức tạp của nhiều điều kiện đầu vào đồng thời, việc phân vùng đơn lẻ không còn hiệu quả. Kỹ thuật này sử dụng các ký hiệu logic Boolean:
  - **원인 (Causes — Nguyên nhân):** Đại diện cho các điều kiện dữ liệu đầu vào.
  - **효과 (Effects — Kết quả):** Đại diện cho các hành vi hoặc trạng thái đầu ra của hệ thống.
  - Các toán tử logic liên kết: `AND`, `OR`, `NOT`, cùng các ràng buộc loại trừ (`E` - Exclusive, `I` - Inclusive, `O` - One and only one, `R` - Requires).
- **Quy trình chuyển đổi:** Đồ thị nguyên nhân - kết quả sau khi vẽ sẽ được chuyển đổi trực tiếp thành **의사결정 테이블 (Decision Table — Bảng quyết định)** để từ đó viết ra các ca kiểm thử cụ thể.

### 2.4. Các kỹ thuật kiểm thử hộp đen khác
- **의사결정 테이블 테스팅 (Decision Table Testing):** Lập bảng gồm hàng Điều kiện (Conditions) và hàng Hành động (Actions), mỗi cột biểu diễn một quy tắc nghiệp vụ (Rule) độc lập để kiểm tra.
- **상태 전이 테스팅 (State Transition Testing — Kiểm thử chuyển trạng thái):** Mô hình hóa hệ thống bằng máy trạng thái hữu hạn (FSM). Thiết kế ca kiểm thử để kiểm tra xem khi có sự kiện (Event) tác động, hệ thống có chuyển đúng từ Trạng thái A sang Trạng thái B hay không (rất phổ biến trong kiểm thử máy rút tiền ATM, quy trình đặt vé).
- **오류 예측 (Error Guessing — Đoán lỗi):** Hoàn toàn không dựa trên công thức toán học mà dựa vào **trực giác, sự nhạy cảm và kinh nghiệm tích lũy của kiểm thử viên** để phán đoán các tình huống bất thường mà lập trình viên dễ quên (ví dụ: chia cho số 0, nhập chuỗi rỗng `""`, nhập ký tự xuống dòng, chèn mã SQL Injection).
- **페어와이즈 테스팅 (Pairwise Testing — Kiểm thử cặp):** Dựa trên thực nghiệm chỉ ra rằng phần lớn lỗi phát sinh từ sự tương tác giữa 2 yếu tố bất kỳ. Thay vì thử mọi tổ hợp $N$ yếu tố, kỹ thuật này chỉ cần bảo đảm mọi cặp 2 yếu tố đều được kiểm tra cùng nhau ít nhất một lần, giúp giảm số lượng test case từ hàng nghìn xuống vài chục.
- **비교 검사 (Comparison Testing — Kiểm tra so sánh):** Nạp cùng một tập dữ liệu đầu vào vào hai hoặc nhiều phiên bản phần mềm độc lập để đối chiếu xem kết quả có đồng nhất 100% hay không.

---

## 3. 테스트 케이스 및 테스트 시나리오 — Thiết kế tài liệu ca kiểm thử chuẩn quốc tế

Theo tiêu chuẩn quốc tế **ISO/IEC/IEEE 29119-3**, tài liệu kiểm thử phải được thiết kế có cấu trúc và có thể định lượng, nhằm bảo đảm khả năng lặp lại và bàn giao công việc giữa các kỹ sư.

### 3.1. Cấu trúc chuẩn của một Test Case (테스트 케이스)

Bản mô tả ca kiểm thử (Test Case) là tài liệu kỹ thuật xác định một tập hợp các giá trị đầu vào, điều kiện thực thi và kết quả kỳ vọng cho một mục tiêu kiểm tra đơn lẻ.

| Thành phần cấu tạo | Tên tiếng Hàn & Anh | Ý nghĩa và Quy chuẩn nội dung |
| :--- | :--- | :--- |
| **Mã định danh** | **테스트 식별자 (Test ID)** | Mã duy nhất để phân loại và truy vết (ví dụ: `TC_AUTH_LOGIN_001`) |
| **Hạng mục kiểm tra** | **테스트 항목 (Test Item)** | Tên chức năng hoặc module được kiểm tra (ví dụ: Đăng nhập hệ thống) |
| **Điều kiện tiên quyết** | **환경 설정 / 전제 조건 (Pre-conditions)** | Trạng thái bắt buộc của hệ thống trước khi bắt đầu test (ví dụ: Đã có tài khoản kích hoạt) |
| **Dữ liệu đầu vào** | **입력 명세 (Input Specification)** | Các tham số cụ thể truyền vào (ví dụ: `Username = "admin"`, `Password = "1234"`) |
| **Kết quả kỳ vọng** | **출력 명세 / 기대 결과 (Expected Result)** | Hành vi và giá trị hệ thống phải trả về (ví dụ: Hiển thị thông báo "Mật khẩu sai", không được vào Dashboard) |
| **Thủ tục thực hiện** | **특수 절차 요구 (Special Procedures)** | Các thao tác môi trường đặc thù (ví dụ: Rút dây mạng trong lúc bấm Đăng nhập) |
| **Quan hệ phụ thuộc** | **의존성 기술 (Inter-case Dependencies)** | Chỉ rõ Test Case này có bắt buộc phải chạy sau Test Case nào khác không |

### 3.2. Phân biệt Test Case vs Test Scenario

| Tiêu chí | 테스트 케이스 (Test Case) | 테스트 시나리오 (Test Scenario) |
| :--- | :--- | :--- |
| **Bản chất** | **Phép thử đơn lẻ cho một trường hợp cụ thể** | **Kịch bản chuỗi hành vi liên hoàn của người dùng** |
| **Độ chi tiết** | Cực kỳ chi tiết: từng tham số đầu vào, từng thông báo lỗi mong đợi | Mô tả luồng nghiệp vụ ở mức tổng quan |
| **Mối quan hệ** | **Nhiều Test Case kết hợp lại tạo thành một Test Scenario** | Là tài liệu khung định hướng để suy ra tập hợp các Test Case |
| **Ví dụ minh họa** | Kiểm tra trường Mật khẩu để trống có hiện chữ đỏ "Vui lòng nhập mật khẩu" hay không | Kịch bản mua hàng: Đăng nhập $\rightarrow$ Tìm kiếm sản phẩm $\rightarrow$ Thêm giỏ hàng $\rightarrow$ Thanh toán qua cổng VNPay |

### 3.3. Ma trận truy xuất nguồn gốc kiểm thử (RTM - Requirements Traceability Matrix)
- Trong các dự án phần mềm chuyên nghiệp, mỗi Test Case bắt buộc phải được liên kết ngược về tài liệu Yêu cầu (Software Requirements Specification - SRS).
- **Mục đích:** Bảo đảm **100% yêu cầu nghiệp vụ của khách hàng đều có ít nhất một Test Case bao phủ**, không để lọt bất kỳ tính năng nào chưa được kiểm tra trước khi bàn giao sản phẩm.

---

## 4. Nối mạch kiến thức sang bài tiếp theo

Sau khi đã nắm vững các kỹ thuật kiểm tra bên trong mã nguồn ([Bài 15: Kiểm thử hộp trắng](15-kiem-thu-hop-trang-va-coverage.md)) và các kỹ thuật thiết kế ca kiểm thử chức năng bên ngoài ([Bài 16: Kiểm thử hộp đen](16-kiem-thu-hop-den-va-test-case.md)), câu hỏi tiếp theo của kỹ nghệ phần mềm là: **Các bài kiểm thử này được phân bổ vào các giai đoạn phát triển như thế nào, và làm sao máy tính biết được một ca kiểm thử chạy ra kết quả là ĐÚNG hay SAI?**

Để trả lời trọn vẹn câu hỏi đó, chúng ta sẽ chuyển sang **[Bài 17: Cấp độ kiểm thử V-Model, kiểm thử tích hợp và Test Oracle](17-v-model-kiem-thu-tich-hop-va-oracle.md)**, nơi ta sẽ khảo sát mô hình V-Model đối ứng, các kỹ thuật tích hợp hạ thấu (Stub) / thượng thăng (Driver) và cơ chế thẩm định kết quả bằng Test Oracle.

---

## 5. 복습 체크리스트 (Checklist ôn tập)

- [ ] Định nghĩa Black-Box Testing là kiểm thử chức năng dựa trên đặc tả yêu cầu, không nhìn mã nguồn.
- [ ] Phân biệt 유효 동치 클래스 (Lớp hợp lệ) và 무효 동치 클래스 (Lớp không hợp lệ) trong kỹ thuật 동치 분할 (Equivalence Partitioning).
- [ ] Áp dụng đúng kỹ thuật 경계값 분석 (Boundary Value Analysis): Chọn các giá trị ngay tại biên, sát dưới biên và sát trên biên ($min-1, min, min+1$).
- [ ] Nhớ đồ thị nguyên nhân - kết quả (Cause-Effect Graphing) sử dụng logic Boolean để chuyển thành Bảng quyết định (Decision Table).
- [ ] Nhận diện kỹ thuật 오류 예측 (Error Guessing) dựa hoàn toàn vào kinh nghiệm và trực giác của kiểm thử viên.
- [ ] Kể tên tiêu chuẩn quốc tế về tài liệu kiểm thử: ISO/IEC/IEEE 29119-3.
- [ ] Liệt kê đủ các trường cấu tạo chuẩn của Test Case: ID, Item, Pre-conditions, Input, Expected Output.
- [ ] Phân biệt Test Case (phép thử cụ thể) và Test Scenario (kịch bản chuỗi nghiệp vụ liên hoàn).
- [ ] Nêu vai trò của Ma trận truy xuất nguồn gốc RTM (bảo đảm 100% yêu cầu được kiểm thử).
