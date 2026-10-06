# 2. 요구사항 개발 (Phát triển Yêu cầu)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **2. 요구사항 개발 (Phát triển Yêu cầu)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối requirements development với elicitation, specification và validation, để yêu cầu có thể truy nguyên từ nhu cầu đến tiêu chí chấp nhận.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. 요구사항 개발 (Phát triển Yêu cầu)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. 요구사항 개발 (Phát triển Yêu cầu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **2. 요구사항 개발 (Phát triển Yêu cầu)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

요구사항, 개발

> **Nối mạch:** Ở chặng này của **2. 요구사항 개발 (Phát triển Yêu cầu)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)**에서 만든 기준을 이어받아 **2. 요구사항 개발 (Phát triển Yêu cầu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **2. 요구사항 개발 (Phát triển Yêu cầu)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **2. 요구사항 개발 (Phát triển Yêu cầu)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **2. 요구사항 개발 (Phát triển Yêu cầu)**, **2. 요구사항 개발 (Phát triển Yêu cầu)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 2. 요구사항 개발 (Phát triển Yêu cầu)

Ở bước 4/69, **2. 요구사항 개발 (Phát triển Yêu cầu)** xuất hiện như phần tiếp nối của **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 요구사항 개발 (Phát triển Yêu cầu)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)

Bây giờ ta đi vào nội dung của **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 성능 요구사항 (Yêu cầu hiệu năng)
- 보안 요구사항 (Yêu cầu bảo mật)
- 품질 요구사항 (Yêu cầu chất lượng)
- 제약사항 (Ràng buộc)
- 인터페이스 요구사항 (Yêu cầu giao diện)
- **Ví dụ (Example):** Chức năng đăng nhập là yêu cầu chức năng. Nhưng "Đăng nhập phải hoàn tất dưới 1 giây" là yêu cầu phi chức năng (hiệu năng - 성능).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **HBCRG** (Hiệu - Bảo - Chất - Ràng - Giao): **Học Bài Chăm Rồi Giỏi**.

Các ý về **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)

Phần nguồn của **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 도출 (Elicitation - Khám phá/Rút ra) → 분석 (Analysis - Phân tích) → 명세 (Specification - Đặc tả) → 확인 (Validation - Xác nhận)
- **Ví dụ (Example):** Phỏng vấn user (도출), lọc ra các yêu cầu hợp lý (분석), viết tài liệu SRS (명세), nhờ user ký duyệt (확인).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ĐPMX** (Đồ - Phân - Minh - Xác): **Đi Phượt Một Xe**.

Các ý về **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)**, đừng bắt đầu lại từ số không. **009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)

Các ý ngay dưới **009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 개발 대상에 대한 사용자의 요구사항을 이해하고 문서화(명세화)하는 활동을 의미한다. (Hoạt động hiểu và tài liệu hóa (đặc tả) yêu cầu của người dùng về đối tượng cần phát triển.)
- 소프트웨어 개발의 실제적인 첫 단계이다. (Là bước thực tế đầu tiên của phát triển phần mềm.)
- 사용자 요구의 타당성을 조사하고 비용과 일정에 대한 제약을 설정한다. (Khảo sát tính hợp lý của yêu cầu người dùng và thiết lập các ràng buộc về chi phí, lịch trình.)
- 사용자의 요구를 정확하게 추출하여 목표를 정하고, 해결 방식을 결정한다. (Trích xuất chính xác yêu cầu của người dùng để đặt mục tiêu và quyết định cách giải quyết.)
- **Ví dụ (Example):** Khách hàng muốn "App chạy nhanh". Phân tích viên sẽ dịch thành "Thời gian phản hồi < 2s" và xem xét chi phí server có đủ đáp ứng không (비용/일정 제약).

Các ý về **009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** vừa cho ta cách đặt câu hỏi. Bây giờ **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소

Bây giờ ta đi vào nội dung của **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로세스 (Process - Quy trình): Hình tròn / Hình bầu dục. (Ví dụ: 물품 확인 - Kiểm tra hàng hóa)
- 자료 흐름 (Data Flow - Luồng dữ liệu): Mũi tên. (Ví dụ: 물품 코드 - Mã hàng hóa)
- 자료 저장소 (Data Store - Kho lưu trữ dữ liệu): Hai đường thẳng song song. (Ví dụ: 물품대장 - Sổ hàng hóa)
- 단말 (Terminator - Điểm cuối/Tác nhân ngoài): Hình chữ nhật. (Ví dụ: 공장 - Nhà máy)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **PFST** (Process, Flow, Store, Terminator): **Phải Phạt Sợ Tội**.

Các ý về **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **011. 자료 사전 (Data Dictionary) 의 표기 기호** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **011. 자료 사전 (Data Dictionary) 의 표기 기호**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 011. 자료 사전 (Data Dictionary) 의 표기 기호

Phần nguồn của **011. 자료 사전 (Data Dictionary) 의 표기 기호** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “011. 자료 사전 (Data Dictionary) 의 표기 기호” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `=`: 정의 (Định nghĩa - is composed of)
- `+`: 연결 (Kết nối/Và - and)
- `( )`: 생략 (Có thể bỏ qua/Tùy chọn - optional)
- `[ | ]`: 선택 (Lựa chọn [hoặc] - choose only one)
- `{ }`: 반복 (Lặp lại - iteration)
- `* *`: 설명 (Giải thích/Chú thích - comment)
- **Ví dụ (Example):** `Customer_Name = First_Name + (Middle_Name) + Last_Name`. Middle_Name nằm trong `( )` nghĩa là có thể không có (생략).
- 💡 **Mẹo ghi nhớ (Mnemonic):** `{ }` giống như vòng lặp trong code, nên là lặp lại (반복). `* *` giống comment `/* */` trong code.

Với **011. 자료 사전 (Data Dictionary) 의 표기 기호**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **011. 자료 사전 (Data Dictionary) 의 표기 기호**, đừng bắt đầu lại từ số không. **012. HIPO (Hierarchy plus Input-Process-Output)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **012. HIPO (Hierarchy plus Input-Process-Output)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 012. HIPO (Hierarchy plus Input-Process-Output)

Các ý ngay dưới **012. HIPO (Hierarchy plus Input-Process-Output)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “012. HIPO (Hierarchy plus Input-Process-Output)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 하향식 소프트웨어 개발을 위한 문서화 도구이다. (Là công cụ tài liệu hóa cho phát triển phần mềm theo hướng từ trên xuống - Top-down.)
- 기호, 도표 등을 사용하므로 보기 쉽고 이해하기도 쉽다. (Sử dụng ký hiệu, biểu đồ nên dễ nhìn và dễ hiểu.)
- 기능과 자료의 의존 관계를 동시에 표현할 수 있다. (Có thể biểu diễn đồng thời mối quan hệ phụ thuộc giữa chức năng và dữ liệu.)
- **Ví dụ (Example):** Vẽ một sơ đồ cây bắt đầu từ Hệ thống chính (Quản lý trường học) rẽ nhánh xuống các chức năng con (Quản lý điểm, Quản lý sinh viên).

Các ý về **012. HIPO (Hierarchy plus Input-Process-Output)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Như vậy, **012. HIPO (Hierarchy plus Input-Process-Output)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **2. 요구사항 개발 (Phát triển Yêu cầu)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **2. 요구사항 개발 (Phát triển Yêu cầu)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
