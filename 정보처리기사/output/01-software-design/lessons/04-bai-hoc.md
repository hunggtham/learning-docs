# 2. 요구사항 개발 (Phát triển Yêu cầu)

## 학습 목표 (Mục tiêu)
- Phân biệt chính xác giữa Yêu cầu chức năng (`기능 요구사항`) và Yêu cầu phi chức năng (`비기능 요구사항`), nhận diện nhanh các câu hỏi phân loại trong đề thi.
- Thuộc nằm lòng Quy trình phát triển yêu cầu 4 bước (`요구사항 개발 프로세스`): Thu thập (`도출`) -> Phân tích (`분석`) -> Đặc tả (`명세`) -> Xác minh (`확인`).
- Nắm vững các công cụ phân tích có cấu trúc kinh điển: 4 ký hiệu của Sơ đồ luồng dữ liệu (`DFD`), 6 ký hiệu toán tử của Từ điển dữ liệu (`DD`), và mô hình phân rã phân cấp `HIPO`.

## 핵심 키워드 (Từ khóa)
- 기능 요구사항 (Yêu cầu chức năng / Functional Requirements)
- 비기능 요구사항 (Yêu cầu phi chức năng / Non-functional Requirements)
- 도출·분석·명세·확인 (Elicitation, Analysis, Specification, Validation)
- DFD (자료 흐름도 / Data Flow Diagram)
- 프로세스·자료 흐름·자료 저장소·단말 (Process, Data Flow, Data Store, Terminator)
- 자료 사전 (Từ điển dữ liệu / Data Dictionary: `=, +, (), [|], {}, **`)
- HIPO (Hierarchy plus Input-Process-Output / 하향식 분석)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([1. 소프트웨어 공학 및 개발 방법론](03-bai-hoc.md)):** Sau khi chọn phương pháp luận phát triển, bước đầu tiên và cốt lõi là định hình bài toán thông qua việc phát triển yêu cầu người dùng.
- **Tiếp nối sang bài sau ([9. 요구사항 및 시스템 파악](05-bai-hoc.md)):** Từ việc hiểu các yêu cầu và công cụ mô hình hóa, ta tiến hành thẩm định yêu cầu (Review, Walkthrough, Inspection) và phân tích môi trường hiện trạng hệ thống.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chắc chắn bảng ký hiệu DFD (hình dạng hình học) và 6 ký hiệu toán tử DD - đây là dạng bài tập nhận diện ký hiệu ăn điểm tuyệt đối.
- Đọc TẦNG B để hiểu rõ tại sao yêu cầu phi chức năng (bảo mật, thời gian đáp ứng) lại thường khó kiểm thử và tốn kém chi phí hơn yêu cầu chức năng thuần túy.

---

## 2. 요구사항 개발 (Phát triển Yêu cầu)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Phân loại yêu cầu người dùng:**
  - **기능 요구사항 (Yêu cầu chức năng):** Mô tả hệ thống phải làm gì (`무엇을 하는지`), các dịch vụ, chức năng cụ thể và dữ liệu đầu vào/đầu ra (Ví dụ: chức năng đăng nhập, tính tiền giỏ hàng, in báo cáo hóa đơn).
  - **비기능 요구사항 (Yêu cầu phi chức năng):** Các tiêu chuẩn chất lượng và ràng buộc vận hành hệ thống:
    - `성능 (Hiệu năng)`: Thời gian phản hồi < 1 giây, xử lý 10.000 giao dịch/giây.
    - `보안 (Bảo mật)`: Mã hóa mật khẩu bằng SHA-256, phân quyền truy cập người dùng.
    - `품질 (Chất lượng)`: Độ tin cậy, tính sẵn sàng 99.99%, khả năng phục hồi khi có sự cố.
    - `제약사항 (Ràng buộc)`: Phải chạy trên hệ điều hành Linux, tuân thủ tiêu chuẩn ISO 27001.
    - `인터페이스 (Giao diện)`: Tương thích với cổng thanh toán điện tử của ngân hàng.
- **요구사항 개발 프로세스 (Quy trình phát triển yêu cầu 4 bước):**
  1. `도출 (Elicitation - Thu thập/Khám phá)`: Phỏng vấn, khảo sát, làm việc với người dùng để tìm hiểu mong muốn.
  2. `분석 (Analysis - Phân tích)`: Phân loại, giải quyết xung đột, xác định tính khả thi và ràng buộc kỹ thuật.
  3. `명세 (Specification - Đặc tả)`: Viết thành tài liệu đặc tả yêu cầu phần mềm chuẩn (SRS - Software Requirements Specification).
  4. `확인 / 검증 (Validation / Verification - Thẩm định)`: Kiểm tra xem tài liệu đặc tả có phản ánh đúng nhu cầu người dùng, đầy đủ và không mâu thuẫn hay không.
- **Các công cụ phân tích có cấu trúc cổ điển:**
  - **자료 흐름도 (DFD - Data Flow Diagram):**
    - `프로세스 (Process - Tiến trình)`: Biểu diễn bằng **Hình tròn (원)** hoặc hình chữ nhật bo tròn góc.
    - `자료 흐름 (Data Flow - Luồng dữ liệu)`: Biểu diễn bằng **Mũi tên (화살표)**.
    - `자료 저장소 (Data Store - Kho lưu trữ dữ liệu)`: Biểu diễn bằng **Hai đường thẳng song song (평행선)**.
    - `단말 (Terminator - Tác nhân ngoài / Nguồn và đích)`: Biểu diễn bằng **Hình chữ nhật (직사각형)**.
  - **자료 사전 (DD - Data Dictionary): 6 ký hiệu cốt lõi:**
    - `=`: `정의` (Định nghĩa / is composed of)
    - `+`: `연결` (Kết nối, và / and)
    - `( )`: `생략` (Có thể lược bỏ, tùy chọn / optional)
    - `[ | ]`: `선택` (Lựa chọn một trong các phương án / or)
    - `{ }`: `반복` (Lặp lại / iteration)
    - `* *`: `설명 / 주석` (Giải thích, chú thích / comment)
  - **HIPO (Hierarchy plus Input-Process-Output):**
    - Là công cụ mô tả hệ thống theo cấu trúc phân rã từ trên xuống (`하향식 분석 도구`).
    - Gồm 3 loại biểu đồ: Biểu đồ mục lục trực quan (`가시적 도표`), Biểu đồ tổng thể (`총체적 도표`), Biểu đồ chi tiết (`세부적 도표`).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1 (Ký hiệu DFD):** Đề hỏi *"Kho lưu trữ dữ liệu (자료 저장소) trong DFD được ký hiệu bằng hình gì?"* -> **Hai đường song song (평행선)**, không phải hình chữ nhật (Terminator) hay hình trụ (Database vật lý).
  - **Bẫy 2 (Ký hiệu DD):** Đề hỏi *"Ký hiệu `{ }` trong Từ điển dữ liệu mang ý nghĩa gì?"* -> **반복 (Lặp lại)**, KHÔNG PHẢI lựa chọn (`[ | ]`) hay lược bỏ (`( )`).
  - **Bẫy 3:** *"Phần mềm phải xử lý được 1.000 giao dịch đồng thời là yêu cầu chức năng hay phi chức năng?"* -> **Phi chức năng (비기능 - 성능 요구사항)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Yêu cầu gồm Chức năng và Phi chức năng; quy trình Đ-P-M-X; DFD 4 hình; DD 6 toán tử biểu diễn dữ liệu".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế hoạt động của Từ điển dữ liệu (Data Dictionary):**
  - Từ điển dữ liệu là tài liệu mô tả chi tiết tất cả các luồng dữ liệu và kho dữ liệu xuất hiện trong DFD.
  - Ví dụ biểu diễn thông tin sinh viên:
    $$\text{Sinh\_Vien} = \text{MSSV} + \text{Ho\_Ten} + (\text{So\_Dien\_Thoai}) + [\text{Nam} \mid \text{Nu}] + \{\text{Mon\_Hoc}\} + *\text{Thong tin ho so}*$$
    - Diễn giải: Sinh viên gồm có Mã số sinh viên VÀ Họ tên, CÓ THỂ CÓ Số điện thoại (tùy chọn), CHỌN Nam hoặc Nữ, CÓ THỂ LẶP LẠI nhiều Môn học, và đoạn chú thích giải thích hồ sơ.
- **Sự khác biệt giữa Xác nhận (Validation) và Xác minh (Verification):**
  - `Verification (검증)`: "Chúng ta có đang xây dựng hệ thống ĐÚNG CÁCH không?" (Đúng theo tài liệu thiết kế và tiêu chuẩn kỹ thuật).
  - `Validation (확인)`: "Chúng ta có đang xây dựng ĐÚNG HỆ THỐNG mà người dùng thực sự cần không?" (Đúng mục đích và kỳ vọng của khách hàng).

### 복습 체크리스트
- [ ] Phân biệt được chức năng (what system does) và phi chức năng (performance, security, quality).
- [ ] Nhớ thứ tự quy trình 4 bước: 도출 (Elicitation) -> 분석 (Analysis) -> 명세 (Specification) -> 확인 (Validation).
- [ ] Nhận diện được 4 ký hiệu hình học của DFD (Tròn, Mũi tên, Hai đường song song, Chữ nhật).
- [ ] Thuộc nằm lòng 6 ký hiệu toán tử của Data Dictionary: `=`, `+`, `( )`, `[ | ]`, `{ }`, `* *`.
- [ ] Nhớ HIPO là công cụ phân tích từ trên xuống (하향식) gồm 3 loại sơ đồ (가시적, 총체적, 세부적).
