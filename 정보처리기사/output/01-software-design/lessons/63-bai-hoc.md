# 10. 소프트웨어 설계 원리 (Software Design Principles)

## 학습 목표 (Mục tiêu)
- Nắm vững 5 nguyên lý thiết kế phần mềm kinh điển (`소프트웨어 설계 기본 원리`): Trừu tượng hóa (`추상화`), Mô-đun hóa (`모듈화`), Che giấu thông tin (`정보 은닉`), Tinh chỉnh từng bước (`단계적 분할 / 정제`), và Cấu trúc hóa (`구조화`).
- Phân biệt 3 cấp độ trừu tượng hóa: Trừu tượng hóa quá trình (`과정 추상화`), Trừu tượng hóa dữ liệu (`데이터 추상화`), và Trừu tượng hóa điều khiển (`제어 추상화`).
- Thuộc nằm lòng vai trò của nguyên lý Che giấu thông tin do David Parnas đề xuất và nguyên lý Tinh chỉnh từng bước do Niklaus Wirth đề xuất.

## 핵심 키워드 (Từ khóa)
- 설계 기본 원리 (Nguyên lý thiết kế phần mềm / Software Design Principles)
- 추상화 (Trừu tượng hóa / Abstraction: 과정, 데이터, 제어 추상화)
- 모듈화 (Mô-đun hóa / Modularity / 결합도↓, 응집도↑)
- 정보 은닉 (Che giấu thông tin / Information Hiding / David Parnas)
- 단계적 분할 / 정제 (Stepwise Refinement / 하향식 점진적 구체화 / Niklaus Wirth)
- 구조화 (Cấu trúc hóa / Structuring / 순차, 선택, 반복)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([6. 구조적 분석 도구](62-bai-hoc.md)):** Sau khi xem xét các công cụ phân tích có cấu trúc, bài này trang bị hệ thống tư duy nguyên lý chỉ đạo việc thiết kế phần mềm đạt độ độc lập cao.
- **Tiếp nối sang bài sau ([3. 결합도 (Coupling - Độ phụ thuộc)](64-bai-hoc.md)):** Đi sâu vào công cụ định lượng đánh giá mức độ phụ thuộc giữa các mô-đun thiết kế.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 3 dạng trừu tượng hóa (Quá trình, Dữ liệu, Điều khiển) và 2 tên tác giả gắn liền với nguyên lý: Parnas (Che giấu thông tin) và Wirth (Tinh chỉnh từng bước).
- Đọc TẦNG B để hiểu tại sao việc che giấu thông tin giúp một lập trình viên có thể tối ưu hóa thuật toán bên trong hàm mà không làm đổ vỡ các hệ thống bên ngoài đang gọi hàm đó.

---

## 10. 소프트웨어 설계 원리 (Software Design Principles)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **5 nguyên lý thiết kế phần mềm cơ bản (설계 5대 기본 원리):**
  1. **추상화 (Abstraction - Tính trừu tượng hóa):**
     - Bỏ qua các chi tiết cài đặt cụ thể phức tạp bên trong, **chỉ tập trung vào các đặc tính bản chất cốt lõi nhất (`불필요한 부분을 생략하고 핵심적인 내용만 포괄적으로 표현`)**.
     - **3 dạng trừu tượng hóa trong đề thi:**
       - `과정 / 프로시저 추상화 (Process / Procedural Abstraction)`: Trừu tượng hóa một chuỗi các câu lệnh xử lý thành một tên gọi hàm tổng quát (ví dụ: hàm `calculateInterest()` tính lãi suất).
       - `데이터 추상화 (Data Abstraction)`: Trừu tượng hóa cấu trúc dữ liệu và tập hợp các phép toán hợp lệ trên dữ liệu đó (ví dụ: kiểu dữ liệu trừu tượng ADT - Stack, List).
       - `제어 추상화 (Control Abstraction)`: Trừu tượng hóa các cơ chế điều khiển luồng thực thi trong ngôn ngữ (ví dụ: vòng lặp duyệt phần tử for-each, khối bắt ngoại lệ try-catch).
  2. **모듈화 (Modularity - Tính mô-đun hóa):**
     - Phân chia hệ thống lớn phức tạp thành các đơn vị mô-đun độc lập nhỏ hơn.
     - **Mục tiêu thiết kế:** Đạt **Độ kết hợp thấp (`결합도는 낮추고`)** và **Độ gắn kết cao (`응집도는 높임`)**.
  3. **정보 은닉 (Information Hiding - Che giấu thông tin):**
     - Do nhà khoa học **David Parnas** đề xuất.
     - Mỗi mô-đun phải giấu kín chi tiết cài đặt và cấu trúc dữ liệu nội bộ của mình, chỉ cung cấp giao diện công khai chuẩn hóa để bên ngoài giao tiếp.
     - **Lợi ích:** Khi một mô-đun thay đổi cấu trúc mã nguồn bên trong, **các mô-đun khác hoàn toàn không bị ảnh hưởng (`다른 모듈에 영향을 주지 않음`)**, giúp việc bảo trì trở nên an toàn.
  4. **단계적 분할 / 단계적 정제 (Stepwise Refinement - Tinh chỉnh từng bước):**
     - Do nhà khoa học **Niklaus Wirth** đề xuất.
     - Tiếp cận bài toán theo hướng từ trên xuống (**Top-down**); bắt đầu từ một ý niệm trừu tượng ở mức cao nhất, sau đó tiến hành phân tích chi tiết hóa dần dần từng bước xuống các mức thấp hơn cho đến khi đạt được các chỉ dẫn lập trình cụ thể.
  5. **구조화 (Structuring - Cấu trúc hóa):**
     - Tổ chức toàn bộ luồng điều khiển của phần mềm dựa trên 3 cấu trúc chuẩn hóa duy nhất: Tuần tự (`순차`), Lựa chọn (`선택`), và Lặp lại (`반복`).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Ai là người đề xuất nguyên lý Che giấu thông tin (Information Hiding)?"* -> **David Parnas (파나스)**.
  - **Bẫy 2:** *"Ai là người đề xuất nguyên lý Tinh chỉnh từng bước (Stepwise Refinement) theo hướng Top-down?"* -> **Niklaus Wirth (워스)**.
  - **Bẫy 3:** *"3 dạng trừu tượng hóa là gì?"* -> **과정 추상화 (Quá trình), 데이터 추상화 (Dữ liệu), và 제어 추상화 (Điều khiển)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Trừu tượng hóa gồm Quá trình, Dữ liệu, Điều khiển; Parnas giấu thông tin bảo vệ nội bộ; Wirth tinh chỉnh Top-down từng bước cụ thể hóa".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ tương hỗ giữa Abstraction và Stepwise Refinement:**
  - Hai nguyên lý này là hai mặt của cùng một đồng xu trong thiết kế Top-down:
    - Ở tầng trên cùng, kỹ sư sử dụng **Abstraction** để phát biểu bài toán tổng quát: "Hệ thống mua sắm trực tuyến gồm Giỏ hàng, Thanh toán và Vận chuyển".
    - Sau đó, kỹ sư sử dụng **Stepwise Refinement** để bóc tách tầng 2: "Phần Thanh toán gồm Kiểm tra thẻ tín dụng, Tính phí vận chuyển, Trừ tiền ngân hàng". Tiếp tục tinh chỉnh tầng 3 xuống các dòng mã giả (Pseudocode) cụ thể.

### 복습 체크리스트
- [ ] Kể tên đầy đủ 5 nguyên lý thiết kế phần mềm cơ bản.
- [ ] Phân biệt được 3 dạng trừu tượng hóa: 과정, 데이터, 제어 추상화.
- [ ] Nhớ tên Parnas gắn liền với 정보 은닉 (Information Hiding).
- [ ] Nhớ tên Wirth gắn liền với 단계적 분할/정제 (Stepwise Refinement).
