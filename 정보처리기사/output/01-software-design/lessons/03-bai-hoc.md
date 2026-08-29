# 2. 요구사항 개발 (Phát triển Yêu cầu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **2. 요구사항 개발 (Phát triển Yêu cầu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

요구사항, 개발

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 2. 요구사항 개발 (Phát triển Yêu cầu)

### 007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)
- 성능 요구사항 (Yêu cầu hiệu năng)
- 보안 요구사항 (Yêu cầu bảo mật)
- 품질 요구사항 (Yêu cầu chất lượng)
- 제약사항 (Ràng buộc)
- 인터페이스 요구사항 (Yêu cầu giao diện)
- **Ví dụ (Example):** Chức năng đăng nhập là yêu cầu chức năng. Nhưng "Đăng nhập phải hoàn tất dưới 1 giây" là yêu cầu phi chức năng (hiệu năng - 성능).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **HBCRG** (Hiệu - Bảo - Chất - Ràng - Giao): **Học Bài Chăm Rồi Giỏi**.

### 008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)
- 도출 (Elicitation - Khám phá/Rút ra) → 분석 (Analysis - Phân tích) → 명세 (Specification - Đặc tả) → 확인 (Validation - Xác nhận)
- **Ví dụ (Example):** Phỏng vấn user (도출), lọc ra các yêu cầu hợp lý (분석), viết tài liệu SRS (명세), nhờ user ký duyệt (확인).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ĐPMX** (Đồ - Phân - Minh - Xác): **Đi Phượt Một Xe**.

### 009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)
- 개발 대상에 대한 사용자의 요구사항을 이해하고 문서화(명세화)하는 활동을 의미한다. (Hoạt động hiểu và tài liệu hóa (đặc tả) yêu cầu của người dùng về đối tượng cần phát triển.)
- 소프트웨어 개발의 실제적인 첫 단계이다. (Là bước thực tế đầu tiên của phát triển phần mềm.)
- 사용자 요구의 타당성을 조사하고 비용과 일정에 대한 제약을 설정한다. (Khảo sát tính hợp lý của yêu cầu người dùng và thiết lập các ràng buộc về chi phí, lịch trình.)
- 사용자의 요구를 정확하게 추출하여 목표를 정하고, 해결 방식을 결정한다. (Trích xuất chính xác yêu cầu của người dùng để đặt mục tiêu và quyết định cách giải quyết.)
- **Ví dụ (Example):** Khách hàng muốn "App chạy nhanh". Phân tích viên sẽ dịch thành "Thời gian phản hồi < 2s" và xem xét chi phí server có đủ đáp ứng không (비용/일정 제약).

### 010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소
- 프로세스 (Process - Quy trình): Hình tròn / Hình bầu dục. (Ví dụ: 물품 확인 - Kiểm tra hàng hóa)
- 자료 흐름 (Data Flow - Luồng dữ liệu): Mũi tên. (Ví dụ: 물품 코드 - Mã hàng hóa)
- 자료 저장소 (Data Store - Kho lưu trữ dữ liệu): Hai đường thẳng song song. (Ví dụ: 물품대장 - Sổ hàng hóa)
- 단말 (Terminator - Điểm cuối/Tác nhân ngoài): Hình chữ nhật. (Ví dụ: 공장 - Nhà máy)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **PFST** (Process, Flow, Store, Terminator): **Phải Phạt Sợ Tội**.

### 011. 자료 사전 (Data Dictionary) 의 표기 기호
- `=`: 정의 (Định nghĩa - is composed of)
- `+`: 연결 (Kết nối/Và - and)
- `( )`: 생략 (Có thể bỏ qua/Tùy chọn - optional)
- `[ | ]`: 선택 (Lựa chọn [hoặc] - choose only one)
- `{ }`: 반복 (Lặp lại - iteration)
- `* *`: 설명 (Giải thích/Chú thích - comment)
- **Ví dụ (Example):** `Customer_Name = First_Name + (Middle_Name) + Last_Name`. Middle_Name nằm trong `( )` nghĩa là có thể không có (생략).
- 💡 **Mẹo ghi nhớ (Mnemonic):** `{ }` giống như vòng lặp trong code, nên là lặp lại (반복). `* *` giống comment `/* */` trong code.

### 012. HIPO (Hierarchy plus Input-Process-Output)
- 하향식 소프트웨어 개발을 위한 문서화 도구이다. (Là công cụ tài liệu hóa cho phát triển phần mềm theo hướng từ trên xuống - Top-down.)
- 기호, 도표 등을 사용하므로 보기 쉽고 이해하기도 쉽다. (Sử dụng ký hiệu, biểu đồ nên dễ nhìn và dễ hiểu.)
- 기능과 자료의 의존 관계를 동시에 표현할 수 있다. (Có thể biểu diễn đồng thời mối quan hệ phụ thuộc giữa chức năng và dữ liệu.)
- **Ví dụ (Example):** Vẽ một sơ đồ cây bắt đầu từ Hệ thống chính (Quản lý trường học) rẽ nhánh xuống các chức năng con (Quản lý điểm, Quản lý sinh viên).
