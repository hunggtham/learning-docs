# 3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)

## 학습 목표 (Mục tiêu)
- Nắm vững các kỹ thuật phân tích có cấu trúc truyền thống: Sơ đồ luồng dữ liệu (`자료 흐름도 - DFD`), Từ điển dữ liệu (`자료 사전 - DD`), và Sơ đồ phân cấp HIPO.
- Thuộc nằm lòng 4 ký hiệu hình học của DFD và 6 toán tử biểu diễn cấu trúc của Từ điển dữ liệu, giải quyết chính xác các câu hỏi nhận diện ký hiệu.
- Phân biệt 3 loại biểu đồ trong mô hình HIPO (Biểu đồ mục lục trực quan, Biểu đồ tổng quan, Biểu đồ chi tiết) và phân loại các công cụ CASE (Thượng tầng, Hạ tầng, Tích hợp).

## 핵심 키워드 (Từ khóa)
- 구조적 분석 기법 (Kỹ thuật phân tích có cấu trúc / Structured Analysis)
- 자료 흐름도 (Sơ đồ luồng dữ liệu / Data Flow Diagram - DFD / 버블 차트)
- 프로세스·자료 흐름·자료 저장소·단말 (Process, Data Flow, Data Store, Terminator)
- 자료 사전 (Từ điển dữ liệu / Data Dictionary - DD)
- HIPO (Hierarchy plus Input-Process-Output: 가시적, 총체적, 세부적 도표)
- 상위 CASE / 하위 CASE (Upper CASE / Lower CASE)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([2. 요구사항 정의](07-bai-hoc.md)):** Sau khi xác định rõ định nghĩa yêu cầu, bài này cung cấp các công cụ trực quan hóa và tự động hóa giúp kỹ sư phân tích chi tiết dữ liệu và chức năng hệ thống.
- **Tiếp nối sang bài sau ([1. 요구사항 개발 기법](09-bai-hoc.md)):** Đi sâu vào các kỹ thuật phỏng vấn, khảo sát, lập mô hình tương tác Use Case để thu thập yêu cầu từ người dùng thực tế.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chuẩn xác dạng hình học của 4 thành phần DFD và 6 ký hiệu toán tử của DD - đây là những điểm thi kinh điển trong đề thi quốc gia.
- Đọc TẦNG B để hiểu rõ tại sao DFD chỉ tập trung vào luồng dữ liệu ("Dữ liệu đi đâu, biến đổi thế nào") mà hoàn toàn không biểu diễn luồng điều khiển (không có rẽ nhánh if-else hay vòng lặp thời gian).

---

## 3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 자료 흐름도 (DFD - Data Flow Diagram / Bubble Chart):**
  - **Khái niệm:** Là biểu đồ biểu diễn trực quan con đường dữ liệu đi vào, được xử lý, lưu trữ và đưa ra ngoài hệ thống theo phương pháp phân tích có cấu trúc.
  - **4 thành phần và ký hiệu hình học bắt buộc phải nhớ:**
    1. `프로세스 (Process - Tiến trình)`: Biểu diễn bằng **Hình tròn (원)** hoặc hình elip/chữ nhật bo tròn. Tên tiến trình là Động từ + Danh từ.
    2. `자료 흐름 (Data Flow - Luồng dữ liệu)`: Biểu diễn bằng **Mũi tên (화살표)**. Thể hiện sự chuyển dịch của các gói dữ liệu.
    3. `자료 저장소 (Data Store - Kho lưu trữ dữ liệu)`: Biểu diễn bằng **Hai đường thẳng song song (평행선)**. Thể hiện file, bảng CSDL lưu trữ tĩnh.
    4. `단말 (Terminator / Source & Sink - Tác nhân ngoài)`: Biểu diễn bằng **Hình chữ nhật (직사각형)**. Thể hiện thực thể bên ngoài cấp dữ liệu vào hoặc nhận dữ liệu ra khỏi hệ thống.
  - **Quy tắc quan trọng của DFD:** DFD **chỉ biểu diễn luồng dữ liệu**, KHÔNG biểu diễn luồng điều khiển (Control Flow) như điều kiện hay vòng lặp lặp lại.
- **2. 자료 사전 (DD - Data Dictionary - Từ điển dữ liệu):**
  - **Khái niệm:** Là tài liệu lưu trữ thông tin chi tiết về tất cả các mục dữ liệu xuất hiện trong DFD (`데이터에 대한 데이터 - 메타데이터`).
  - **6 ký hiệu toán tử chuẩn hóa:**
    - `=`: `정의 (Definition)` - Được định nghĩa bởi, bao gồm (is composed of).
    - `+`: `연결 (Concatenation / Sequence)` - Kết nối, và (and).
    - `( )`: `생략 (Optional)` - Có thể có hoặc không, tùy chọn.
    - `[ | ]`: `선택 (Selection)` - Lựa chọn duy nhất một trong các phần tử cách nhau bởi dấu `|`.
    - `{ }`: `반복 (Iteration)` - Lặp lại từ 0 đến N lần (có thể ghi giới hạn số lần như $1\{ \}^n$).
    - `* *`: `설명 / 주석 (Comment)` - Chú thích giải nghĩa.
- **3. HIPO (Hierarchy plus Input-Process-Output):**
  - Là công cụ tài liệu hóa và thiết kế phần mềm theo cấu trúc phân rã chức năng từ trên xuống (`하향식 분석 도구`).
  - **3 loại sơ đồ trong bộ tài liệu HIPO:**
    1. `가시적 도표 (Visual Table of Contents - Mục lục trực quan)`: Sơ đồ dạng cây phân cấp hiển thị toàn bộ cấu trúc chức năng của hệ thống.
    2. `총체적 도표 (Overview Diagram - Biểu đồ tổng thể)`: Mô tả khái quát dòng Đầu vào (Input), Xử lý (Process) và Đầu ra (Output) của một chức năng.
    3. `세부적 도표 (Detail Diagram - Biểu đồ chi tiết)`: Mô tả chi tiết các bước xử lý logic bên trong của từng chức năng con.
- **4. Phân loại công cụ CASE (Computer-Aided Software Engineering):**
  - `상위 CASE (Upper CASE)`: Hỗ trợ các giai đoạn đầu của vòng đời (Lập kế hoạch, Phân tích yêu cầu, Thiết kế kiến trúc). Ví dụ: Sơ đồ hóa DFD, ERD.
  - `하위 CASE (Lower CASE)`: Hỗ trợ các giai đoạn sau (Sinh mã nguồn tự động - Code Generation, Kiểm thử, Tài liệu hóa).
  - `통합 CASE (Integrated CASE / I-CASE)`: Hỗ trợ bao trùm toàn bộ các khâu trong vòng đời phát triển phần mềm.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1 (DFD Control Flow):** Đề hỏi *"DFD có biểu diễn vòng lặp và câu lệnh rẽ nhánh if-else không?"* -> **Hoàn toàn KHÔNG**. DFD chỉ biểu diễn luồng dữ liệu, không biểu diễn luồng điều khiển thời gian.
  - **Bẫy 2 (DD Symbol):** Ký hiệu `[A | B]` nghĩa là chọn A HOẶC B; ký hiệu `(A)` nghĩa là A có thể có hoặc bị bỏ qua; ký hiệu `{A}` nghĩa là A lặp lại nhiều lần. Đề thi thường hoán đổi ý nghĩa giữa `( )` và `[ ]`.
- **한 문장 설명 (Câu chốt ghi nhớ):** "DFD luồng dữ liệu 4 hình; DD từ điển 6 dấu; HIPO phân rã chức năng Top-down gồm Mục lục, Tổng quan và Chi tiết".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ giải nghĩa biểu thức trong Từ điển dữ liệu (DD):**
  - Cho biểu thức:
    $$\text{Hoa\_Don} = \text{So\_HD} + \text{Ngay\_Lap} + \text{Khach\_Hang} + 1\{\text{Hang\_Hoa}\}^N + (\text{Ghi\_Chu}) + [\text{Tien\_Mat} \mid \text{Chuyen\_Khoan}]$$
  - Phân tích cú pháp:
    - Một hóa đơn bao gồm Số hóa đơn VÀ Ngày lập VÀ Thông tin khách hàng.
    - $1\{\text{Hang\_Hoa}\}^N$: Danh sách Hàng hóa lặp lại ít nhất 1 lần và tối đa $N$ lần.
    - $(\text{Ghi\_Chu})$: Phần ghi chú là tùy chọn (có thể có hoặc bỏ qua).
    - $[\text{Tien\_Mat} \mid \text{Chuyen\_Khoan}]$: Phương thức thanh toán bắt buộc chọn MỘT trong hai hình thức Tiền mặt HOẶC Chuyển khoản.
- **Phân cấp DFD (Leveling DFD):**
  - DFD mức 0 (Context Diagram - Biểu đồ ngữ cảnh): Chỉ có duy nhất 1 tiến trình đại diện cho toàn bộ hệ thống, kết nối với các tác nhân ngoài (Terminator).
  - DFD mức 1: Phân rã tiến trình mức 0 thành các phân hệ chức năng chính.
  - DFD mức 2+: Tiếp tục phân rã cho đến khi các tiến trình đạt mức cơ sở không thể chia nhỏ hơn nữa (Primitive Process), khi đó ta dùng Mini-spec (Đặc tả tiến trình con) để mô tả logic.

### 복습 체크리스트
- [ ] Nhận diện được 4 thành phần của DFD (Tiến trình - Tròn, Luồng dữ liệu - Mũi tên, Kho dữ liệu - Song song, Tác nhân ngoài - Chữ nhật).
- [ ] Khẳng định được DFD chỉ mô tả luồng dữ liệu, không mô tả luồng điều khiển.
- [ ] Viết và giải thích đúng ý nghĩa 6 ký hiệu của Từ điển dữ liệu (`=`, `+`, `( )`, `[ | ]`, `{ }`, `* *`).
- [ ] Phân biệt được 3 loại sơ đồ HIPO: 가시적 도표, 총체적 도표, 세부적 도표.
- [ ] Phân biệt được phạm vi hỗ trợ của 상위 CASE và 하위 CASE.
