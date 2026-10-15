# 2. 객체지향 (OOP - Object Oriented Programming)

## 학습 목표 (Mục tiêu)
- Nắm vững 5 phương pháp phân tích hướng đối tượng (`객체지향 분석 - OOA`) kinh điển trong kỹ nghệ phần mềm: Rumbaugh, Booch, Jacobson, Coad & Yourdon, và Wirfs-Brock.
- Thuộc nằm lòng thứ tự 3 bước mô hình hóa của phương pháp Rumbaugh (`럼바우 분석 기법 3단계`): Mô hình đối tượng (`객체 모델링`) -> Mô hình động (`동적 모델링`) -> Mô hình chức năng (`기능 모델링`).
- Nhận diện công cụ biểu đồ tương ứng của từng mô hình trong phương pháp Rumbaugh: Object/ERD, State Diagram, và DFD.

## 핵심 키워드 (Từ khóa)
- 객체지향 분석 방법론 (Phương pháp luận phân tích hướng đối tượng / OOA)
- 럼바우 기법 (Phương pháp Rumbaugh / OMT)
- 객체 모델링 (Mô hình đối tượng / Object Modeling / ERD / Class Diagram)
- 동적 모델링 (Mô hình động / Dynamic Modeling / 상태 다이어그램)
- 기능 모델링 (Mô hình chức năng / Functional Modeling / 자료 흐름도 - DFD)
- 부치 (Booch / 미시적·거시적), 야콥슨 (Jacobson / 유스케이스), 코드-요돈 (Coad-Yourdon / E-R), 워프스-브록 (Wirfs-Brock / 책임 주도)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([6. 객체지향](26-bai-hoc.md)):** Sau khi hiểu các khái niệm OOP (Class, Encapsulation, Polymorphism), bài này hệ thống hóa các trường phái phân tích hệ thống hướng đối tượng trong lịch sử kỹ nghệ phần mềm.
- **Tiếp nối sang bài sau ([1. 객체지향 설계 5대 원칙 (SOLID)](28-bai-hoc.md)):** Chuyển từ phân tích sang thiết kế hướng đối tượng với 5 nguyên tắc vàng SOLID do Robert C. Martin chuẩn hóa.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc thứ tự thần chú **객 - 동 - 기** của Rumbaugh và công cụ đi kèm (Đối tượng = ERD, Động = State, Chức năng = DFD) - câu hỏi này xuất hiện trong hầu hết các kỳ thi 정보처리기사.
- Đọc TẦNG B để hiểu tại sao Rumbaugh lại đặt mô hình Đối tượng lên làm bước đầu tiên trước khi xét đến khía cạnh động và chức năng.

---

## 2. 객체지향 (OOP - Object Oriented Programming)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phương pháp phân tích Rumbaugh (OMT - Object Modeling Technique) - Trọng tâm số 1:**
  - Là phương pháp phân tích hướng đối tượng phổ biến nhất, tiếp cận bài toán qua 3 góc nhìn mô hình hóa độc lập được tiến hành theo thứ tự nghiêm ngặt:
    1. **객체 모델링 (Object Modeling - Mô hình hóa đối tượng):**
       - **Bước đầu tiên và quan trọng nhất (`가장 중요하며 선행되어야 함`)**.
       - Mô tả cấu trúc tĩnh của hệ thống: Các đối tượng, lớp, thuộc tính và mối quan hệ giữa chúng.
       - **Công cụ biểu diễn:** Sơ đồ đối tượng (`객체 다이어그램`) / Sơ đồ lớp (`Class Diagram`) / Biểu đồ E-R.
    2. **동적 모델링 (Dynamic Modeling - Mô hình hóa động):**
       - Mô tả sự thay đổi trạng thái, tương tác và hành vi theo thời gian của các đối tượng do các sự kiện kích hoạt.
       - **Công cụ biểu diễn:** Biểu đồ trạng thái (`상태 다이어그램 - State Diagram`).
    3. **기능 모델링 (Functional Modeling - Mô hình hóa chức năng):**
       - Mô tả luồng dữ liệu và các biến đổi logic xử lý tính toán bên trong hệ thống từ đầu vào đến đầu ra.
       - **Công cụ biểu diễn:** Sơ đồ luồng dữ liệu (`자료 흐름도 - DFD`).
    - 💡 **Thần chú nhớ thứ tự Rumbaugh:** **객 - 동 - 기** (Khách Đến Gặp -> Khách/Đối tượng -> Động -> Gặp/Chức năng).
- **2. Bảng đối chiếu các phương pháp phân tích OOA khác:**
  - `부치 (Booch) 기법`: Phân tích theo hai cấp độ: **Vi mô (미시적 개발 프로세스 - Micro)** và **Vĩ mô (거시적 개발 프로세스 - Macro)**; dùng các biểu đồ lớp và đối tượng dạng đám mây.
  - `야콥슨 (Jacobson) 기법 (OOSE)`: Phân tích hướng ca sử dụng (**유스케이스 - Use Case**), lấy tương tác của người dùng làm trung tâm để thúc đẩy toàn bộ quy trình phát triển.
  - `코드와 요돈 (Coad & Yourdon) 기법`: Sử dụng mô hình E-R trực quan hóa cấu trúc thực thể, thuộc tính và mối liên kết hướng đối tượng.
  - `워프스-브록 (Wirfs-Brock) 기법`: Phân tích định hướng trách nhiệm (**책임 주도 설계 - Responsibility-Driven Design**), xác định đối tượng chịu trách nhiệm gì và cộng tác với ai (thẻ CRC: Class-Responsibility-Collaboration).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1 (Thứ tự Rumbaugh):** Đề hỏi *"Thứ tự các bước phân tích theo phương pháp Rumbaugh là gì?"* -> **객체 모델링 $\rightarrow$ 동적 모델링 $\rightarrow$ 기능 모델링 (객 - 동 - 기)**.
  - **Bẫy 2 (Công cụ của Rumbaugh):** Đề hỏi *"Trong phương pháp Rumbaugh, mô hình động (동적 모델링) sử dụng công cụ gì?"* -> **상태 다이어그램 (State Diagram)**, KHÔNG PHẢI DFD hay ERD.
  - **Bẫy 3:** *"Phương pháp phân tích nào chia quy trình thành Micro và Macro?"* -> **부치 (Booch) 기법**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Rumbaugh phân tích qua 3 bước Khách - Động - Gặp (Đối tượng ERD, Động State, Chức năng DFD); Booch Vi-Vĩ mô, Jacobson Use Case, Wirfs-Brock Trách nhiệm".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tại sao lại có sự phân chia 3 mô hình trong OMT:**
  - Một hệ thống phần mềm phức tạp không thể hiểu thấu đáo chỉ qua 1 góc nhìn:
    - Nếu chỉ nhìn vào `객체 모델링`, ta chỉ thấy các bảng tĩnh mà không biết chúng vận hành ra sao.
    - Bổ sung `동적 모델링` giúp ta thấy nút nào bấm trước, nút nào bấm sau, tài khoản đang ở trạng thái `Hoạt động` hay `Bị khóa`.
    - Bổ sung `기능 모델링` giúp ta thấy công thức tính lãi suất hay thuật toán mã hóa mật khẩu vận hành bên trong.
  - Ba mô hình này sau đó đã được James Rumbaugh kết hợp với Booch và Jacobson để khai sinh ra chuẩn UML hiện đại.

### 복습 체크리스트
- [ ] Thuộc thần chú 객-동-기 biểu thị thứ tự 3 bước phân tích theo phương pháp Rumbaugh.
- [ ] Nhớ chính xác công cụ biểu diễn tương ứng: 객체 = ERD/Class, 동적 = 상태도, 기능 = DFD.
- [ ] Khẳng định được 객체 모델링 là bước quan trọng nhất và phải thực hiện đầu tiên.
- [ ] Nối đúng tên tác giả với đặc trưng: Booch (Vi mô/Vĩ mô), Jacobson (Use Case), Wirfs-Brock (Trách nhiệm CRC).
