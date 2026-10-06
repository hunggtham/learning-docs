# Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu học tập)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **권장 학습 순서 (Lộ trình đề xuất)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng README làm bản đồ owner của Information System Management, rồi nối mục tiêu, thứ tự học và bài chuyên sâu.

## 학습 목표 (Mục tiêu học tập)

Phần này đặt mục tiêu của bài, để người mới biết mình cần giải thích được điều gì trước khi đi vào thuật ngữ và ví dụ.

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

> **Câu hỏi trung tâm:** Khi học môn này, người học không chỉ cần nhận ra thuật ngữ Hàn mà còn phải giải thích khái niệm đang giải quyết vấn đề nào, dựa trên điều kiện nào và được dùng để nối sang phần kiến thức nào tiếp theo.

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **권장 학습 순서 (Lộ trình đề xuất)** nối từ **학습 목표 (Mục tiêu học tập)** sang **1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 권장 학습 순서 (Lộ trình đề xuất)

Phần này là đường đi của bài giảng: đọc theo thứ tự để mỗi mục sau dùng lại hoặc mở rộng tiêu chí của mục trước.

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước ngôn ngữ:** phần giải thích ưu tiên tiếng Việt; ở mọi lần xuất hiện, thuật ngữ đề thi dùng dạng `nghĩa Việt (English / 한국어)` để không phải quay lại tìm nghĩa.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

> **Mạch giảng:** mỗi mục mở bằng vị trí và mục đích học, đi qua phần giải thích của nguồn, rồi chốt bằng một câu bàn giao sang mục kế tiếp. Hãy đọc các câu nối như một phần của bài giảng: chúng cho biết vì sao kiến thức hiện tại cần thiết trước khi chuyển sang kiến thức sau.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)** nối từ **권장 학습 순서 (Lộ trình đề xuất)** sang **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)

Chúng ta bắt đầu mạch học bằng **1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)**. Trước khi đi vào từng thuật ngữ, hãy giữ câu hỏi trung tâm: phần kiến thức này giải quyết vấn đề gì và vì sao các khái niệm sau phải được đọc trong cùng một bối cảnh? Mục đích của mục 1/86 là tạo điểm tựa để những phần tiếp theo được hiểu theo quan hệ, không chỉ được ghi nhớ như danh sách.

Để đọc **1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)** như một bài học cho người mới, hãy giữ câu hỏi: **một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1.1 구조적 방법론 (Structured Methodology)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1.1 구조적 방법론 (Structured Methodology)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1.1 구조적 방법론 (Structured Methodology)

Bây giờ ta đi vào nội dung của **1.1 구조적 방법론 (Structured Methodology)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1.1 구조적 방법론 (Structured Methodology)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 정형화된 분석 절차에 따라 사용자 요구사항을 파악하여 문서화하는 **처리(Process) 중심**의 방법론이다.
- 복잡한 문제를 다루기 위해 **분할과 정복 (Divide and Conquer)** 원리를 적용한다.
- **Tiếng Việt:** Là phương pháp luận trung tâm vào xử lý (Process), lập tài liệu yêu cầu người dùng theo quy trình phân tích chuẩn. Áp dụng nguyên lý chia để trị (Divide and Conquer) cho các vấn đề phức tạp.
- **Example:**
  - *KR:* 큰 시스템을 여러 개의 작은 모듈로 나누어 개발.
  - *VN:* Chia một hệ thống lớn thành nhiều module nhỏ để phát triển.

Các ý về **1.1 구조적 방법론 (Structured Methodology)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **1.1 구조적 방법론 (Structured Methodology)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **1.2 정보공학 방법론 (Information Engineering Methodology)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **1.2 정보공학 방법론 (Information Engineering Methodology)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 1.2 정보공학 방법론 (Information Engineering Methodology)

Phần nguồn của **1.2 정보공학 방법론 (Information Engineering Methodology)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1.2 정보공학 방법론 (Information Engineering Methodology)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 정보 시스템의 개발을 위해 정형화된 기법들을 상호 연관성 있게 통합 및 적용하는 **자료(Data) 중심**의 방법론이다.
- 데이터베이스 설계를 위한 데이터 모델링으로 **개체 관계도 (ERD; Entity Relationship Diagram)**를 사용한다.
- **Tiếng Việt:** Phương pháp luận trung tâm vào dữ liệu (Data), tích hợp các kỹ thuật chuẩn hóa để phát triển hệ thống. Sử dụng sơ đồ thực thể liên kết (ERD) cho mô hình hóa dữ liệu.
- **Example:**
  - *KR:* 고객과 주문의 관계를 ERD로 모델링하여 시스템 구축.
  - *VN:* Mô hình hóa mối quan hệ giữa Khách hàng và Đơn hàng bằng ERD để xây dựng hệ thống.

Các ý về **1.2 정보공학 방법론 (Information Engineering Methodology)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **1.2 정보공학 방법론 (Information Engineering Methodology)**, đừng bắt đầu lại từ số không. **1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)

Các ý ngay dưới **1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기존의 시스템이나 소프트웨어를 구성하는 **컴포넌트를 조합**하여 하나의 새로운 애플리케이션을 만드는 방법론이다.
- 분석 단계에서 사용자 요구사항 정의서가 산출된다.
- **Tiếng Việt:** Phương pháp luận tạo ứng dụng mới bằng cách kết hợp các thành phần (component) có sẵn. Tài liệu định nghĩa yêu cầu được tạo ra ở bước phân tích.
- **Example:**
  - *KR:* 결제 컴포넌트와 장바구니 컴포넌트를 조립하여 쇼핑몰 구축.
  - *VN:* Lắp ráp component thanh toán và component giỏ hàng để tạo trang thương mại điện tử.
- 💡 **Mẹo ghi nhớ:** CBD = "Lego" (lắp ráp các mảnh ghép có sẵn).

Với **1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)** vừa cho ta cách đặt câu hỏi. Bây giờ **1.4 소프트웨어 개발 프레임워크 (Software Development Framework)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **1.4 소프트웨어 개발 프레임워크 (Software Development Framework)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 1.4 소프트웨어 개발 프레임워크 (Software Development Framework)

Bây giờ ta đi vào nội dung của **1.4 소프트웨어 개발 프레임워크 (Software Development Framework)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1.4 소프트웨어 개발 프레임워크 (Software Development Framework)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 공통적으로 사용되는 구성 요소와 아키텍처를 일반화하여 제공해주는 반제품 형태의 소프트웨어 시스템.
- 사업자 종속성이 해소되며, 객체들의 제어를 프레임워크에 넘김으로써 생산성을 향상시킨다.
- **Tiếng Việt:** Hệ thống phần mềm dạng bán thành phẩm cung cấp các thành phần và kiến trúc chung. Giải quyết sự phụ thuộc vào nhà cung cấp và tăng năng suất.
- **Example:**
  - *KR:* Spring 프레임워크를 사용하여 Java 웹 애플리케이션을 빠르게 개발.
  - *VN:* Sử dụng Spring framework để phát triển nhanh ứng dụng web Java.

Các ý về **1.4 소프트웨어 개발 프레임워크 (Software Development Framework)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Với **1.4 소프트웨어 개발 프레임워크 (Software Development Framework)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)** nối từ **1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)** sang **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)

Sau khi đã đặt nền bằng **1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)**, ta chuyển sang **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)**. Đây là mắt xích 2/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)** như một bài học cho người mới, hãy giữ câu hỏi: **một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **내부적 기준**, **외부적 기준**, **종류** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 테일러링 (Tailoring)**. Hãy xác định **1. 테일러링 (Tailoring)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 테일러링 (Tailoring)

Phần nguồn của **1. 테일러링 (Tailoring)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

프로젝트 특성에 맞게 개발 방법론의 절차나 기법을 수정 및 보완하는 작업.
- **내부적 기준**: 목표 환경, 요구사항, 프로젝트 규모, 보유 기술.
- **외부적 기준**: 법적 제약사항, 표준 품질 기준.

Các bullet của **1. 테일러링 (Tailoring)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 테일러링 (Tailoring)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 소프트웨어 개발 프레임워크 (Framework)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 소프트웨어 개발 프레임워크 (Framework)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 소프트웨어 개발 프레임워크 (Framework)

Các ý ngay dưới **2. 소프트웨어 개발 프레임워크 (Framework)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

공통 사용되는 구성 요소와 아키텍처를 일반화하여 제공하는 반제품 형태의 시스템. (예외 처리, 트랜잭션, DB 연동 등 기본 기능 제공).
- **종류**: 스프링(Spring - Java용), 닷넷(.NET - Windows용), 전자정부 프레임워크(공공부문 지원).

Các bullet của **2. 소프트웨어 개발 프레임워크 (Framework)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 소프트웨어 개발 프레임워크 (Framework)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)** nối từ **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)** sang **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크**, vì cơ chế trước tạo đầu vào cho bước sau.

## 프레임워크 특징 및 SW 신기술 (Framework & SW Tech)

Từ **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)**, ta đã có điểm tựa để bước vào **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/86 trước khi đi vào chi tiết.

Để đọc **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 (Modularity)**, **재사용성 (Reusability)**, **확장성 (Extensibility)**, **제어의 역흐름 (Inversion of Control)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 프레임워크의 특성 (Characteristics of Framework)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 프레임워크의 특성 (Characteristics of Framework)

Các ý ngay dưới **1. 프레임워크의 특성 (Characteristics of Framework)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “1. 프레임워크의 특성 (Characteristics of Framework)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모듈화 (Modularity)**: 캡슐화로 모듈화를 강화하여 변경 영향을 최소화.
- **재사용성 (Reusability)**: 재사용 가능한 모듈 제공으로 생산성 향상.
- **확장성 (Extensibility)**: 다형성을 통한 인터페이스 확장.
- **제어의 역흐름 (Inversion of Control)**: 개발자가 아닌 프레임워크가 객체들을 제어하고 통제.

Các bullet của **1. 프레임워크의 특성 (Characteristics of Framework)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 프레임워크의 특성 (Characteristics of Framework)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. SDE (Software-Defined Everything)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. SDE (Software-Defined Everything)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. SDE (Software-Defined Everything)

Bây giờ ta đi vào nội dung của **2. SDE (Software-Defined Everything)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

하드웨어 자원을 가상화하여 소프트웨어만으로 제어 및 관리하는 기술.
- **SDN**: 소프트웨어 정의 네트워킹 (네트워크 가상화)
- **SDDC**: 소프트웨어 정의 데이터 센터 (데이터 센터 전체 가상화)
- **SDS**: 소프트웨어 정의 스토리지 (스토리지 가상화)

Các bullet của **2. SDE (Software-Defined Everything)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. SDE (Software-Defined Everything)**, đừng bắt đầu lại từ số không. **3. 주요 SW 및 관련 용어** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3. 주요 SW 및 관련 용어**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3. 주요 SW 및 관련 용어

Phần nguồn của **3. 주요 SW 및 관련 용어** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3. 주요 SW 및 관련 용어” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **SOA (Service Oriented Architecture)**: 서비스나 컴포넌트 중심으로 구축하는 아키텍처.
- **디지털 트윈 (Digital Twin)**: 물리적 자산을 소프트웨어로 가상화(복제)하여 효율성을 높이는 기술.
- **텐서플로 (TensorFlow)**: 구글이 만든 딥러닝/데이터 흐름용 오픈소스 라이브러리.
- **도커 (Docker)**: 컨테이너(Container) 기술을 자동화하는 오픈소스 프로젝트.

Các bullet của **3. 주요 SW 및 관련 용어** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 주요 SW 및 관련 용어** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크** nối từ **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)** sang **336. 소프트웨어 개발 프레임워크 (Software Development Framework)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크

Ở bước 4/86, **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크** xuất hiện như phần tiếp nối của **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các đoạn prose và thuật ngữ bên dưới cần được đọc như các bước trả lời cho câu hỏi đó.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Như vậy, **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **336. 소프트웨어 개발 프레임워크 (Software Development Framework)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **336. 소프트웨어 개발 프레임워크 (Software Development Framework)** nối từ **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크** sang **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 336. 소프트웨어 개발 프레임워크 (Software Development Framework)

Sau khi đã đặt nền bằng **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크**, ta chuyển sang **336. 소프트웨어 개발 프레임워크 (Software Development Framework)**. Đây là mắt xích 5/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **336. 소프트웨어 개발 프레임워크 (Software Development Framework)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **특성**, **Tiếng Việt** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “336. 소프트웨어 개발 프레임워크 (Software Development Framework)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 개발에 공통 사용되는 구조를 제공하여 생산성을 높이는 기반.
- **특성**: 모듈화, 재사용성, 확장성, **제어의 역흐름(IoC)**.
- **Tiếng Việt**: Nền tảng cấu trúc sẵn giúp tăng năng suất (như Spring, .NET). Đặc tính: Module hóa, Tái sử dụng, Mở rộng, Đảo ngược luồng điều khiển (IoC).

Ta bắt đầu phần nội dung bằng **자주 혼동하는 판별 포인트**. Hãy xác định **자주 혼동하는 판별 포인트** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 자주 혼동하는 판별 포인트

Phần nguồn của **자주 혼동하는 판별 포인트** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “자주 혼동하는 판별 포인트” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- COCOMO의 고전 유형은 **Organic / Semi-Detached / Embedded**이며 Sequential은 유형명이 아니다.
- RIP는 거리 벡터 방식이고 최대 15홉을 사용한다. OSPF는 링크 상태 방식, BGP는 AS 간 경로 제어다.
- AES·DES·SEED는 대칭키, RSA는 공개키 알고리즘이다. 해시(MD5/SHA 계열)는 암·복호화 키를 교환하는 알고리즘이 아니라 일방향 요약 함수다.
- Chinese Wall은 이해상충 방지, Bell-LaPadula는 기밀성, Biba는 무결성 중심 모델이다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **자주 혼동하는 판별 포인트**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **336. 소프트웨어 개발 프레임워크 (Software Development Framework)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)** nối từ **336. 소프트웨어 개발 프레임워크 (Software Development Framework)** sang **프로젝트 일정 관리 (Project Schedule Management)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)

Từ **336. 소프트웨어 개발 프레임워크 (Software Development Framework)**, ta đã có điểm tựa để bước vào **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 6/86 trước khi đi vào chi tiết.

Để đọc **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **3.1 소프트웨어 프로젝트 관리 (Software Project Management)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 3.1 소프트웨어 프로젝트 관리 (Software Project Management)

Các ý ngay dưới **3.1 소프트웨어 프로젝트 관리 (Software Project Management)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “3.1 소프트웨어 프로젝트 관리 (Software Project Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주어진 기간 내에 최소의 비용으로 사용자를 만족시키는 시스템을 개발하기 위한 전반적인 활동.
- **Tiếng Việt:** Hoạt động tổng thể để phát triển hệ thống làm hài lòng người dùng với chi phí tối thiểu trong thời gian quy định.

Các bullet của **3.1 소프트웨어 프로젝트 관리 (Software Project Management)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **3.1 소프트웨어 프로젝트 관리 (Software Project Management)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **3.2 하향식/상향식 비용 산정 (Cost Estimation)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **3.2 하향식/상향식 비용 산정 (Cost Estimation)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3.2 하향식/상향식 비용 산정 (Cost Estimation)

Bây giờ ta đi vào nội dung của **3.2 하향식/상향식 비용 산정 (Cost Estimation)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần **3.2 하향식/상향식 비용 산정 (Cost Estimation)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **3.2 하향식/상향식 비용 산정 (Cost Estimation)**, đừng bắt đầu lại từ số không. **LOC 기법 (Lines of Code)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **LOC 기법 (Lines of Code)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

#### LOC 기법 (Lines of Code)

Phần nguồn của **LOC 기법 (Lines of Code)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “LOC 기법 (Lines of Code)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 각 기능의 원시 코드 라인 수의 비관치, 낙관치, 기대치를 측정하여 예측.
- **공식 (Formulas):**
  - 노력(인월, Person-Month) = 개발 기간 × 투입 인원 = LOC / 1인당 월평균 생산 코드 라인 수
  - 개발 비용 = 노력(인월) × 단위 비용
  - 개발 기간 = 노력(인월) / 투입 인원
  - 생산성 = LOC / 노력(인월)
- **Tiếng Việt:** Ước tính dựa trên số dòng code. Tính toán Nỗ lực (Person-Month) = Số dòng code / Số dòng code 1 người viết trong 1 tháng.

Với **LOC 기법 (Lines of Code)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**LOC 기법 (Lines of Code)** vừa cho ta cách đặt câu hỏi. Bây giờ **수학적 산정 기법 (Mathematical Models)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **수학적 산정 기법 (Mathematical Models)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

#### 수학적 산정 기법 (Mathematical Models)

Các ý ngay dưới **수학적 산정 기법 (Mathematical Models)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “수학적 산정 기법 (Mathematical Models)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **COCOMO 모형:** 원시 프로그램의 규모(LOC)와 개발 유형에 의한 비용 산정. 고전 COCOMO의 경계는 조직형 `≤ 50 KDSI`, 반분리형 `> 50 ~ 300 KDSI`, 내장형 `> 300 KDSI`로 겹치지 않게 해석한다.
- **Putnam 모형:** 생명 주기 동안 사용될 노력의 분포를 가정 (Rayleigh-Norden 곡선 기초). **SLIM** 도구 사용.
- **기능 점수 (FP) 모형:** 기능적 요구사항을 점수화. 가중치 증대 요인: 자료 입력, 정보 출력, 명령어(질의), 데이터 파일, 외부 루틴 인터페이스.
- **Tiếng Việt:**
  - COCOMO: Dựa vào số dòng code (LOC). Gồm Organic (nhỏ), Semi-Detached (vừa), Embedded (lớn).
  - Putnam: Dựa trên đường cong Rayleigh-Norden (Công cụ: SLIM).
  - FP (Function Point): Dựa trên tính năng.

Các bullet của **수학적 산정 기법 (Mathematical Models)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **수학적 산정 기법 (Mathematical Models)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **3.3 일정 관리 (Schedule Management)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **3.3 일정 관리 (Schedule Management)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3.3 일정 관리 (Schedule Management)

Bây giờ ta đi vào nội dung của **3.3 일정 관리 (Schedule Management)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3.3 일정 관리 (Schedule Management)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **PERT (프로그램 평가 및 검토 기술):** 낙관, 가능, 비관적인 경우로 나누어 종료 시기를 결정. 결정 경로와 임계 경로를 알 수 있음.
- **CPM (임계 경로 기법):** 임계 경로는 프로젝트에서 가장 긴(최장) 경로를 의미한다.
- **간트 차트 (Gantt Chart):** 작업 일정을 막대 도표로 표시 (수평 막대 길이는 기간).
- **Tiếng Việt:**
  - PERT: Dựa trên thời gian lạc quan, bi quan, khả thi.
  - Đường găng (Critical Path): Đường dài nhất trong sơ đồ mạng.
  - Biểu đồ Gantt: Thể hiện tiến độ bằng thanh ngang.

Các bullet của **3.3 일정 관리 (Schedule Management)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **3.3 일정 관리 (Schedule Management)**, đừng bắt đầu lại từ số không. **3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)

Phần nguồn của **3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **위험 관리 (Risk Analysis):** 돌발 상황(위험)을 미리 예상하고 적절한 대책을 수립.
- **방법론 테일러링 (Tailoring):** 프로젝트 상황에 맞게 방법론 절차나 기법을 수정/보완.
  - 내부적 기준: 목표 환경, 요구사항, 프로젝트 규모, 보유 기술.
  - 외부적 기준: 법적 제약사항(Compliance), 표준 품질 기준.
- **Tiếng Việt:** Quản lý rủi ro (lên phương án phòng ngừa) và Cắt may phương pháp (Tailoring) - điều chỉnh quy trình phát triển cho phù hợp với đặc thù dự án.

Các bullet của **3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3.4 위험 관리 및 테일러링 (Risk Management & Tailoring)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **프로젝트 일정 관리 (Project Schedule Management)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **프로젝트 일정 관리 (Project Schedule Management)** nối từ **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)** sang **소프트웨어 비용 산정 기법 (Software Cost Estimation)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 프로젝트 일정 관리 (Project Schedule Management)

Ở bước 7/86, **프로젝트 일정 관리 (Project Schedule Management)** xuất hiện như phần tiếp nối của **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **프로젝트 일정 관리 (Project Schedule Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. PERT (Program Evaluation and Review Technique)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. PERT (Program Evaluation and Review Technique)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. PERT (Program Evaluation and Review Technique)

Bây giờ ta đi vào nội dung của **1. PERT (Program Evaluation and Review Technique)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

과거 경험이 없어 예측이 어려운 프로젝트에 사용. 각 작업별로 낙관치, 기대치, 비관치를 나누어 종료 시기를 계산합니다.
- `예측치 = (비관치 + 4*기대치 + 낙관치) / 6`

Với **1. PERT (Program Evaluation and Review Technique)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. PERT (Program Evaluation and Review Technique)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. CPM (Critical Path Method, 임계 경로 기법)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. CPM (Critical Path Method, 임계 경로 기법)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. CPM (Critical Path Method, 임계 경로 기법)

Phần nguồn của **2. CPM (Critical Path Method, 임계 경로 기법)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

작업 사이의 의존 관계를 노드와 간선으로 구성. 네트워크에서 최장 경로가 **임계 경로(Critical Path)**가 됩니다.

Phần **2. CPM (Critical Path Method, 임계 경로 기법)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. CPM (Critical Path Method, 임계 경로 기법)**, đừng bắt đầu lại từ số không. **3. 간트 차트 (Gantt Chart, 시간선 차트)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **3. 간트 차트 (Gantt Chart, 시간선 차트)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 3. 간트 차트 (Gantt Chart, 시간선 차트)

Các ý ngay dưới **3. 간트 차트 (Gantt Chart, 시간선 차트)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

각 작업의 시작과 종료를 막대 도표로 표시하는 일정표. 적응성이 약하지만 이정표와 작업 기간을 한눈에 파악하기 쉽습니다.

Phần **3. 간트 차트 (Gantt Chart, 시간선 차트)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Như vậy, **3. 간트 차트 (Gantt Chart, 시간선 차트)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **프로젝트 일정 관리 (Project Schedule Management)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **소프트웨어 비용 산정 기법 (Software Cost Estimation)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **소프트웨어 비용 산정 기법 (Software Cost Estimation)** nối từ **프로젝트 일정 관리 (Project Schedule Management)** sang **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 소프트웨어 비용 산정 기법 (Software Cost Estimation)

Sau khi đã đặt nền bằng **프로젝트 일정 관리 (Project Schedule Management)**, ta chuyển sang **소프트웨어 비용 산정 기법 (Software Cost Estimation)**. Đây là mắt xích 8/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **소프트웨어 비용 산정 기법 (Software Cost Estimation)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **공식**, **COCOMO 모형 (Boehm 제안)**, **Putnam 모형 (생명 주기 예측 모형)**, **FP (Function Point, 기능 점수) 모형** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. LOC (Line Of Code) 기법**. Hãy xác định **1. LOC (Line Of Code) 기법** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. LOC (Line Of Code) 기법

Phần nguồn của **1. LOC (Line Of Code) 기법** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. LOC (Line Of Code) 기법” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 원시 코드(Source Code) 라인 수의 낙관치, 비관치, 기대치를 측정해 예측치를 구하여 비용을 산정.
- **공식**:
  - 노력(인월, Man-Month) = `LOC / 1인당 월평균 생산 코드 라인 수` = `개발 기간 × 투입 인원`
  - 개발 비용 = `노력(인월) × 단위 비용(월평균 인건비)`

Với **1. LOC (Line Of Code) 기법**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. LOC (Line Of Code) 기법** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 수학적 산정 기법** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 수학적 산정 기법** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 수학적 산정 기법

Các ý ngay dưới **2. 수학적 산정 기법** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

과거의 프로젝트 데이터를 기반으로 한 상향식 비용 산정 모델입니다.
- **COCOMO 모형 (Boehm 제안)**: LOC 기반 산정. 고전 COCOMO의 경계는 다음처럼 겹치지 않게 해석한다.
  1. **조직형 (Organic)**: `≤ 50 KDSI` (중소 규모 업무용).
  2. **반분리형 (Semi-Detached)**: `> 50 ~ 300 KDSI` (컴파일러, 유틸리티).
  3. **내장형 (Embedded)**: `> 300 KDSI` (초대형 운영체제, 미사일 제어).
- **Putnam 모형 (생명 주기 예측 모형)**: 시간에 따른 **Rayleigh-Norden 곡선**의 노력 분포도를 기초로 산정.
- **FP (Function Point, 기능 점수) 모형**: 알브레히트(Albrecht) 제안. 기능 요인(입력, 출력, 사용자 질의, 데이터 파일, 외부 인터페이스)별로 가중치를 부여해 산정.

> **Vietnamese Explanation**:
> - **LOC**: Tính chi phí dựa trên số dòng code.
> - **COCOMO**: Phân loại theo độ lớn dự án (Organic: nhỏ, Semi: vừa, Embedded: lớn).
> - **Putnam**: Dựa trên đường cong phân bố nỗ lực theo thời gian Rayleigh-Norden.
> - **FP (Function Point)**: Dựa trên số lượng chức năng phần mềm mang lại cho người dùng.

💡 **Mẹo ghi nhớ (Mnemonics):**
- FP의 5가지 요인: **I.O.Q.F.I** (Input, Output, inQuiry, File, Interface).

Các bullet của **2. 수학적 산정 기법** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 수학적 산정 기법** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **소프트웨어 비용 산정 기법 (Software Cost Estimation)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)** nối từ **소프트웨어 비용 산정 기법 (Software Cost Estimation)** sang **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)

Từ **소프트웨어 비용 산정 기법 (Software Cost Estimation)**, ta đã có điểm tựa để bước vào **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 9/86 trước khi đi vào chi tiết.

Để đọc **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **종류**, **COCOMO**, **Putnam** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 통계 공식을 활용한 비용 예측 기법 (Dự toán chi phí dựa trên công thức toán học).
- **종류**:
  - **COCOMO**: LOC(라인 수) 기반 (Dựa vào số dòng code).
  - **Putnam**: 시간에 따른 인력 분포 곡선(Rayleigh-Norden) 활용 (Dựa vào đường cong phân bổ nhân lực).
  - **FP (Function Point)**: 입력, 출력, 인터페이스 등 기능적 요인 기반 (Dựa vào điểm chức năng).

Điểm chốt của **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)** đặt đầu vào cho **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)**, rồi **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)** mở rộng hệ quả liên quan.

## 4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)

Ở bước 10/86, **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)** xuất hiện như phần tiếp nối của **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **4.1 ISO/IEC 12207** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **4.1 ISO/IEC 12207** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 4.1 ISO/IEC 12207

Bây giờ ta đi vào nội dung của **4.1 ISO/IEC 12207**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “4.1 ISO/IEC 12207” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **기본 생명 주기:** 획득, 공급, 개발, 운영, 유지보수.
- **지원 생명 주기:** 품질 보증, 검증, 확인, 문서화, 형상 관리 등.
- **조직 생명 주기:** 관리, 기반 구조, 훈련, 개선.
- **Tiếng Việt:** Tiêu chuẩn vòng đời phần mềm gồm: Cơ bản, Hỗ trợ, Tổ chức.

Các bullet của **4.1 ISO/IEC 12207** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **4.1 ISO/IEC 12207** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **4.2 CMMI 성숙도 5단계 (CMMI Maturity Levels)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **4.2 CMMI 성숙도 5단계 (CMMI Maturity Levels)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 4.2 CMMI 성숙도 5단계 (CMMI Maturity Levels)

Phần nguồn của **4.2 CMMI 성숙도 5단계 (CMMI Maturity Levels)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

1. **초기 (Initial):** 프로세스 없음.
2. **관리 (Managed):** 프로젝트 단위 관리.
3. **정의 (Defined):** 조직 차원 표준화.
4. **정량적 관리 (Quantitatively Managed):** 통계적 측정.
5. **최적화 (Optimizing):** 지속적 개선.
- **Tiếng Việt:** 5 cấp độ trưởng thành: Khởi tạo -> Được quản lý -> Được định nghĩa -> Quản lý định lượng -> Tối ưu hóa.
- 💡 **Mẹo ghi nhớ:** I - M - D - Q - O.

Các bullet của **4.2 CMMI 성숙도 5단계 (CMMI Maturity Levels)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **4.2 CMMI 성숙도 5단계 (CMMI Maturity Levels)**, đừng bắt đầu lại từ số không. **4.3 SPICE (ISO/IEC 15504)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **4.3 SPICE (ISO/IEC 15504)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 4.3 SPICE (ISO/IEC 15504)

Các ý ngay dưới **4.3 SPICE (ISO/IEC 15504)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “4.3 SPICE (ISO/IEC 15504)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소프트웨어 프로세스 평가 및 개선 국제 표준.
- **수행 능력 6단계 (Capability Levels):**
  - 0: 불완전 (Incomplete)
  - 1: 수행 (Performed)
  - 2: 관리 (Managed)
  - 3: 확립 (Established)
  - 4: 예측 (Predictable)
  - 5: 최적화 (Optimizing)
- **Tiếng Việt:** Đánh giá năng lực quy trình phần mềm từ Cấp 0 (Chưa hoàn chỉnh) đến Cấp 5 (Tối ưu hóa).

Các bullet của **4.3 SPICE (ISO/IEC 15504)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **4.3 SPICE (ISO/IEC 15504)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)** đặt đầu vào cho **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)**, rồi **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** mở rộng hệ quả liên quan.

## 소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)

Sau khi đã đặt nền bằng **4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)**, ta chuyển sang **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)**. Đây là mắt xích 11/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. ISO/IEC 12207**. Hãy xác định **1. ISO/IEC 12207** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. ISO/IEC 12207

Phần nguồn của **1. ISO/IEC 12207** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

표준 소프트웨어 생명 주기 프로세스. 3가지(기본, 지원, 조직 프로세스)로 분류.

Phần **1. ISO/IEC 12207** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **1. ISO/IEC 12207** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. CMMI (Capability Maturity Model Integration)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. CMMI (Capability Maturity Model Integration)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. CMMI (Capability Maturity Model Integration)

Các ý ngay dưới **2. CMMI (Capability Maturity Model Integration)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

조직의 성숙도를 평가하는 모델 (5단계).
- **초기(Initial) -> 관리(Managed) -> 정의(Defined) -> 정량적 관리(Quantitatively Managed) -> 최적화(Optimizing)**

Các bullet của **2. CMMI (Capability Maturity Model Integration)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. CMMI (Capability Maturity Model Integration)**, đừng bắt đầu lại từ số không. **3. SPICE (ISO/IEC 15504)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. SPICE (ISO/IEC 15504)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. SPICE (ISO/IEC 15504)

Bây giờ ta đi vào nội dung của **3. SPICE (ISO/IEC 15504)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

프로세스 수행 능력 단계를 평가 (6단계).
- **불완전(Incomplete) -> 수행(Performed) -> 관리(Managed) -> 확립(Established) -> 예측(Predictable) -> 최적화(Optimizing)**

> **Vietnamese Explanation**:
> Các tiêu chuẩn như CMMI và SPICE dùng để đánh giá xem một công ty phần mềm làm việc chuyên nghiệp đến đâu. CMMI có 5 cấp độ (từ lộn xộn đến tối ưu hóa liên tục), còn SPICE có 6 cấp độ.

Các bullet của **3. SPICE (ISO/IEC 15504)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. SPICE (ISO/IEC 15504)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)** đặt vấn đề; **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** đối chiếu bằng chứng, rồi **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** mở rộng hệ quả hoặc giới hạn liên quan.

## 1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)

Từ **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)**, ta đã có điểm tựa để bước vào **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 12/86 trước khi đi vào chi tiết.

Để đọc **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1.1 데이터 통신 및 주요 발전** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1.1 데이터 통신 및 주요 발전

Các ý ngay dưới **1.1 데이터 통신 및 주요 발전** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “1.1 데이터 통신 및 주요 발전” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **데이터 통신:** 컴퓨터와 통신기기 사이에서 디지털(0과 1) 정보를 송수신. (데이터 통신 = 데이터 전송 기술 + 데이터 처리 기술).
- **정보 통신:** 전기 통신 + 컴퓨터 (정보 처리). 통신의 3요소: 정보원, 수신원, 전송 매체.
- **주요 시스템:**
  - `SAGE`: 최초의 데이터 통신 시스템.
  - `SABRE`: 최초 상업용.
  - `ARPANET`: 인터넷의 효시.
  - `ALOHA`: 최초 무선 패킷 교환.
- **Tiếng Việt:** Truyền thông dữ liệu truyền thông tin số (0, 1). 3 yếu tố: Nguồn, Đích, Môi trường truyền. ARPANET là tiền thân của Internet.

Với **1.1 데이터 통신 및 주요 발전**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1.1 데이터 통신 및 주요 발전** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **1.2 통신 회선 및 매체 (Transmission Media)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **1.2 통신 회선 및 매체 (Transmission Media)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 1.2 통신 회선 및 매체 (Transmission Media)

Bây giờ ta đi vào nội dung của **1.2 통신 회선 및 매체 (Transmission Media)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1.2 통신 회선 및 매체 (Transmission Media)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **꼬임선 (Twisted Pair):** 저렴하고 설치 간편, 간섭에 취약.
- **동축 케이블 (Coaxial Cable):** 대역폭이 넓고 누화 적음, 중계기 필요.
- **광섬유 케이블 (Optical Fiber):** 빛의 반사 원리. 가장 빠르고 대역폭 큼. 도청 어려워 보안성 우수. 무유도, 무누화.
- **마이크로파/위성 통신:** 장거리 대용량 통신. 다중 접속 방식: FDMA(주파수), TDMA(시간), CDMA(코드).
- **Tiếng Việt:**
  - Twisted Pair: Rẻ, dễ nhiễu.
  - Coaxial: Băng thông rộng, ít nhiễu.
  - Optical Fiber: Cáp quang (phản xạ ánh sáng), siêu tốc, siêu bảo mật.
  - Vệ tinh: Phân chia theo Tần số (FDMA), Thời gian (TDMA), Mã (CDMA).

Các bullet của **1.2 통신 회선 및 매체 (Transmission Media)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **1.2 통신 회선 및 매체 (Transmission Media)**, đừng bắt đầu lại từ số không. **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 1.3 통신 제어장치 (CCU) & 전처리기 (FEP)

Phần nguồn của **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1.3 통신 제어장치 (CCU) & 전처리기 (FEP)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **CCU:** 데이터 신호의 직·병렬 변환 등 전반적인 제어.
- **FEP (Front-End Processor):** 호스트와 단말기 사이에 위치해 통신 제어를 전담하여 메인 컴퓨터의 부하를 줄임.
- **Tiếng Việt:** CCU điều khiển truyền tải. FEP xử lý tiền kỳ để giảm tải cho máy chủ (Host).

Các bullet của **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** đặt vấn đề; **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** đối chiếu bằng chứng, rồi **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)

Ở bước 13/86, **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** xuất hiện như phần tiếp nối của **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)

Bây giờ ta đi vào nội dung của **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **방향에 따른 분류:** 단방향 (Simplex), 반이중 (Half-Duplex, 무전기), 전이중 (Full-Duplex, 전화).
- **비동기식 (Asynchronous):** 문자마다 Start Bit / Stop Bit를 붙여 전송. 저속 단거리, 오버헤드 큼.
- **동기식 (Synchronous):** 프레임(블록) 단위로 일시에 전송. 속도 빠르고 효율 좋음. 비트/블록 동기 방식.
- **Tiếng Việt:**
  - Đơn công (Simplex), Bán song công (Half-Duplex), Song công toàn phần (Full-Duplex).
  - Bất đồng bộ: Dùng Start/Stop bit (overhead cao). Đồng bộ: Truyền theo block (nhanh, hiệu quả).

Các bullet của **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2.2 신호 변환 장치 (MODEM & DSU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2.2 신호 변환 장치 (MODEM & DSU)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2.2 신호 변환 장치 (MODEM & DSU)

Phần nguồn của **2.2 신호 변환 장치 (MODEM & DSU)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2.2 신호 변환 장치 (MODEM & DSU)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모뎀 (MODEM):** 디지털 ↔ 아날로그 변환.
- **DSU (Digital Service Unit):** 디지털 ↔ 디지털 (단극성 ↔ 양극성 변환). 디지털 전용선에 사용.
- **Tiếng Việt:** MODEM (Chuyển đổi Số <-> Tương tự). DSU (Chuyển đổi Số <-> Số).
- 💡 **Mẹo ghi nhớ:** MO-Dem = MOdulation - DEModulation. D-SU = Digital - Digital.

Với **2.2 신호 변환 장치 (MODEM & DSU)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **2.2 신호 변환 장치 (MODEM & DSU)**, đừng bắt đầu lại từ số không. **2.3 디지털 변조 (Digital Modulation - Keying)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **2.3 디지털 변조 (Digital Modulation - Keying)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2.3 디지털 변조 (Digital Modulation - Keying)

Các ý ngay dưới **2.3 디지털 변조 (Digital Modulation - Keying)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2.3 디지털 변조 (Digital Modulation - Keying)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **ASK (진폭 편이):** 진폭 변화.
- **FSK (주파수 편이):** 주파수 변화 (1,200bps 이하).
- **PSK (위상 편이):** 위상 변화 (중/고속 모뎀).
- **QAM (직교 진폭 변조):** 진폭과 위상 동시 변화 (고속, 9,600bps 표준).
- **Tiếng Việt:** Điều chế tín hiệu số sang tương tự: ASK (Biên độ), FSK (Tần số), PSK (Pha), QAM (Biên độ + Pha kết hợp cho tốc độ cao).

Các bullet của **2.3 디지털 변조 (Digital Modulation - Keying)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**2.3 디지털 변조 (Digital Modulation - Keying)** vừa cho ta cách đặt câu hỏi. Bây giờ **2.4 PCM (Pulse Code Modulation)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **2.4 PCM (Pulse Code Modulation)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2.4 PCM (Pulse Code Modulation)

Bây giờ ta đi vào nội dung của **2.4 PCM (Pulse Code Modulation)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2.4 PCM (Pulse Code Modulation)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 아날로그 데이터를 디지털 신호로 변환. CODEC 이용.
- **과정:** 표본화(Sampling) → 양자화(Quantizing) → 부호화(Encoding) → 복호화(Decoding) → 여파화(Filtering).
- **표본화 (Sampling):** 횟수 = 2 × 최고 주파수.
- **Tiếng Việt:** Biến đổi Tương tự -> Số (dùng CODEC). Quá trình: Lấy mẫu -> Lượng tử hóa -> Mã hóa.
- 💡 **Mẹo ghi nhớ:** Mẫu Lượng Mã Giải Lọc (Lấy mẫu -> Lượng tử hóa -> Mã hóa -> Giải mã -> Lọc).

Với **2.4 PCM (Pulse Code Modulation)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **2.4 PCM (Pulse Code Modulation)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** nối từ **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** sang **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)

Sau khi đã đặt nền bằng **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)**, ta chuyển sang **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**. Đây là mắt xích 14/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **3.1 다중화기 (Multiplexer)**. Hãy xác định **3.1 다중화기 (Multiplexer)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 3.1 다중화기 (Multiplexer)

Phần nguồn của **3.1 다중화기 (Multiplexer)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3.1 다중화기 (Multiplexer)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 여러 단말기가 하나의 통신 회선을 공유.
- **FDM (주파수 분할 다중화):** 주파수를 분할. 보호 대역(Guard Band) 필요(대역폭 낭비). 아날로그, 비동기식.
- **TDM (시분할 다중화):** 시간을 분할(Time Slot). 동기식/디지털.
  - **STDM (동기식):** 데이터 유무 상관없이 고정 시간 폭 할당 (효율 낮음).
  - **ATDM (비동기식/통계적):** 데이터가 있는 단말에만 시간 할당 (효율 높음).
- **역 다중화기 (Inverse MUX):** 하나의 고속 채널을 2개의 저속 채널로 분할.
- **집중화기 (Concentrator):** 회선이 부족할 때 동적으로 할당(버퍼 필요). (입력 > 출력 회선).
- **Tiếng Việt:**
  - FDM: Chia tần số (cần khoảng vệ bảo vệ Guard Band).
  - TDM: Chia thời gian. (STDM: Cố định, ATDM: Động/Thống kê).
  - Concentrator: Gom kênh, cần bộ đệm, số đầu vào > đầu ra.

Các bullet của **3.1 다중화기 (Multiplexer)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **3.1 다중화기 (Multiplexer)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **3.2 통신 속도 (Speed Metrics)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **3.2 통신 속도 (Speed Metrics)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 3.2 통신 속도 (Speed Metrics)

Các ý ngay dưới **3.2 통신 속도 (Speed Metrics)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “3.2 통신 속도 (Speed Metrics)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **변조 속도 (Baud):** 1초 동안 신호 변화 횟수. (Baud = Bps / 상태 변화 수).
- **신호 속도 (Bps):** 1초 동안 전송 비트 수.
- **상태 변화 수:** Mono(1), Di(2), Tri(3), Quad(4) bit.
- **Tiếng Việt:** Baud: Số lần đổi trạng thái/s. Bps: Số bit/s.

Với **3.2 통신 속도 (Speed Metrics)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **3.2 통신 속도 (Speed Metrics)**, đừng bắt đầu lại từ số không. **3.3 전송 제어 (Transmission Control)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3.3 전송 제어 (Transmission Control)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3.3 전송 제어 (Transmission Control)

Bây giờ ta đi vào nội dung của **3.3 전송 제어 (Transmission Control)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3.3 전송 제어 (Transmission Control)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **5단계 절차:** 회선 접속 → 링크 설정 → 메시지 전송 → 링크 해제 → 회선 절단.
- **전송 제어 문자:**
  - `SYN`: 동기화
  - `SOH`/`STX`/`ETX`/`ETB`/`EOT`: 헤더, 텍스트(본문), 블록, 전송 종료
  - `ENQ`: 링크 설정 요구
  - `DLE`: 데이터 링크 이스케이프 (투과성 확보)
  - `ACK`/`NAK`: 긍정/부정 응답
- **Tiếng Việt:** Các ký tự điều khiển: SYN (Đồng bộ), STX (Bắt đầu văn bản), ETX (Kết thúc văn bản), ACK (Xác nhận), NAK (Từ chối).

Các bullet của **3.3 전송 제어 (Transmission Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**3.3 전송 제어 (Transmission Control)** vừa cho ta cách đặt câu hỏi. Bây giờ **3.4 HDLC 프로토콜 (High-level Data Link Control)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **3.4 HDLC 프로토콜 (High-level Data Link Control)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3.4 HDLC 프로토콜 (High-level Data Link Control)

Phần nguồn của **3.4 HDLC 프로토콜 (High-level Data Link Control)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3.4 HDLC 프로토콜 (High-level Data Link Control)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **비트(Bit) 위주**의 프로토콜. 전이중/반이중 지원, 동기식 전송.
- **비트 투과성 (Bit Stuffing):** 연속된 '1'이 5개면 강제로 '0' 추가 (플래그 `01111110`과 구분).
- **프레임 종류:**
  - **I (정보):** 데이터 전달 (0으로 시작).
  - **S (감독):** 오류/흐름 제어 (10).
  - **U (비번호):** 링크 모드 설정 (11).
- **전송 모드:** NRM (정규), ARM (비동기), ABM (비동기 균형 - 전이중 P2P).
- **Tiếng Việt:** HDLC là giao thức truyền theo bit. Dùng "Bit Stuffing" để chèn bit '0' sau 5 bit '1' liên tiếp. 3 loại Frame: I (Thông tin), S (Giám sát), U (Không số).

Các bullet của **3.4 HDLC 프로토콜 (High-level Data Link Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **3.4 HDLC 프로토콜 (High-level Data Link Control)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** nối từ **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** sang **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)

Từ **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**, ta đã có điểm tựa để bước vào **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 15/86 trước khi đi vào chi tiết.

Để đọc **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **while문**, **do~while문** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **4.1 오류 발생 원인 및 제어 (Error Causes & Control)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 4.1 오류 발생 원인 및 제어 (Error Causes & Control)

Các ý ngay dưới **4.1 오류 발생 원인 및 제어 (Error Causes & Control)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “4.1 오류 발생 원인 및 제어 (Error Causes & Control)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **원인:** 감쇠, 지연 왜곡, 상호 변조, 누화 잡음, 충격성 잡음(디지털 통신 주요인).
- **FEC (순방향 오류 수정):** 여분 비트를 함께 보내 수신 측이 재전송 없이 오류를 검출·수정 (해밍 코드 등). 오버헤드가 크고 역채널이 필요 없다.
- **BEC/ARQ (역방향 오류 제어):** 수신 측이 오류를 검출한 뒤 송신 측에 재전송을 요청한다. CRC·패리티는 주로 검출에 사용되고, Stop-and-Wait·Go-Back-N·Selective Repeat가 대표적인 ARQ 방식이다.
- **Tiếng Việt:**
  - FEC: Tự sửa lỗi (vd: Hamming Code).
  - BEC: Yêu cầu gửi lại (vd: CRC, Parity).

Các bullet của **4.1 오류 발생 원인 및 제어 (Error Causes & Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **4.1 오류 발생 원인 및 제어 (Error Causes & Control)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 4.2 ARQ (자동 반복 요청) 및 오류 검출 방식

Bây giờ ta đi vào nội dung của **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “4.2 ARQ (자동 반복 요청) 및 오류 검출 방식” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **ARQ 종류:**
  - **Stop-and-Wait:** 한 블록 보내고 기다림.
  - **Go-Back-N:** 오류 발생 지점부터 *모두* 재전송.
  - **Selective Repeat:** 오류 발생 블록*만* 재전송 (버퍼 필요, 복잡).
  - **Adaptive:** 채널 상태에 따라 동적 변경.
- **오류 검출 및 수정:**
  - **패리티 (Parity):** 1비트 검출, 짝수오류 검출 불가.
  - **CRC:** 다항식 기반, 집단 오류 검출 특화 (HDLC 사용).
  - **해밍 코드 (Hamming Code):** 1비트 *수정* 가능. `2^n` 번째 자리에 비트 삽입.
- **Tiếng Việt:**
  - Go-Back-N: Gửi lại từ lỗi. Selective Repeat: Chỉ gửi lại gói lỗi.
  - CRC: Kiểm tra đa thức (phổ biến nhất). Hamming Code: Sửa được lỗi 1 bit.

Các bullet của **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **4.2 ARQ (자동 반복 요청) 및 오류 검출 방식**, đừng bắt đầu lại từ số không. **4.3 교환 방식 (Switching Methods)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **4.3 교환 방식 (Switching Methods)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 4.3 교환 방식 (Switching Methods)

Phần nguồn của **4.3 교환 방식 (Switching Methods)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “4.3 교환 방식 (Switching Methods)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **회선 교환 (Circuit Switching):** 물리적 전용선 할당. 고정 대역, 연속적 데이터 전송. (접속 지연 O, 전송 지연 X). 전화망.
- **축적 교환 (Store-and-Forward):** 데이터를 저장했다가 경로를 찾아 전송.
  - **메시지 교환 (Message Switching):** 전체 메시지 전송. 지연 매우 긺.
  - **패킷 교환 (Packet Switching):** 패킷 단위로 잘라서 전송 (다음 파트에서 상세 서술).
- **Tiếng Việt:**
  - Circuit Switching (Chuyển mạch kênh): Tạo đường truyền vật lý (Điện thoại).
  - Message Switching (Chuyển mạch thông điệp): Lưu rồi chuyển toàn bộ.

Các bullet của **4.3 교환 방식 (Switching Methods)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**4.3 교환 방식 (Switching Methods)** vừa cho ta cách đặt câu hỏi. Bây giờ **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)

Các ý ngay dưới **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **가상 회선 (Virtual Circuit):** 패킷 교환 전에 논리적인 가상 회선을 설정. 전송 순서가 보장되며 신뢰성이 높음. (호 설정 → 데이터 전송 → 호 해제).
- **데이터그램 (Datagram):** 연결 경로 설정 없이 각 패킷이 독립적으로 운반됨. 패킷마다 경로가 다르고 순서가 다를 수 있음. 짧은 데이터 전송에 적합.
- **패킷 교환망의 기능:** 패킷 다중화, 논리 채널 설정, 경로 제어, 순서 제어, 트래픽 제어, 오류 제어.
- **Tiếng Việt:**
  - Virtual Circuit: Tạo đường dẫn ảo trước khi truyền (thứ tự được đảm bảo).
  - Datagram: Truyền độc lập không cần tạo đường dẫn (thứ tự có thể thay đổi).

Các bullet của **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **4.4 패킷 교환 방식 및 네트워크 기능 (Packet Switching & Network Functions)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)

Bây giờ ta đi vào nội dung của **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **경로 설정 방식 (Routing Strategies):**
  - **고정 경로 (Static):** 미리 정해진 경로 사용.
  - **적응 경로 (Adaptive):** 트래픽 상황에 따라 동적 변경.
  - **범람 (Flooding):** 모든 경로로 패킷 복사 전송 (네트워크 정보 불필요).
  - **임의 경로 (Random):** 인접 교환기 중 임의 선택.
- **폭주(혼잡) 제어 (Congestion Control):** 오버플로를 방지하기 위해 네트워크 내 패킷 수 조절.

---

  - `for(초기식; 조건식; 증감식) { 실행문; }`
- **while문**: 조건이 참인 동안 무한 반복 가능. 조건이 거짓이면 한 번도 실행되지 않음. (Vòng lặp kiểm tra điều kiện trước).
  - `while(조건) { 실행문; }`
- **do~while문**: **무조건 한 번은 실행**한 후, 조건을 판단하여 반복 여부 결정. (Vòng lặp kiểm tra điều kiện sau, ít nhất chạy 1 lần).
  - `do { 실행문; } while(조건);`

Các bullet của **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **4.5 트래픽 제어 및 라우팅 심화 (Traffic Control & Routing)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** đặt vấn đề; **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)** đối chiếu bằng chứng, rồi **2. 자원 처리 오류 (Resource Handling Errors)** mở rộng hệ quả hoặc giới hạn liên quan.

## ⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)

Ở bước 16/86, **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)** xuất hiện như phần tiếp nối của **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các đoạn prose và thuật ngữ bên dưới cần được đọc như các bước trả lời cho câu hỏi đó.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Như vậy, **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **2. 자원 처리 오류 (Resource Handling Errors)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)** đặt vấn đề; **2. 자원 처리 오류 (Resource Handling Errors)** đối chiếu bằng chứng, rồi **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. 자원 처리 오류 (Resource Handling Errors)

Sau khi đã đặt nền bằng **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)**, ta chuyển sang **2. 자원 처리 오류 (Resource Handling Errors)**. Đây là mắt xích 17/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **2. 자원 처리 오류 (Resource Handling Errors)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **부적절한 자원 해제 (Improper Resource Release)**, **해제된 자원 사용 (Use After Free)**, **초기화되지 않은 변수 사용 (Uninitialized Variable)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 자원 처리 오류 (Resource Handling Errors)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **부적절한 자원 해제 (Improper Resource Release)**: 힙 메모리나 소켓을 사용 후 반환(close)하지 않아 자원 고갈 발생. (Không giải phóng bộ nhớ, kết nối sau khi dùng xong).
- **해제된 자원 사용 (Use After Free)**: 반환된 메모리를 다시 참조하여 오작동 유발. (Dùng lại vùng nhớ đã được giải phóng).
- **초기화되지 않은 변수 사용 (Uninitialized Variable)**: 변수 선언 후 값을 넣지 않고 사용하여 이전 쓰레기 값이 노출됨. (Dùng biến chưa khởi tạo giá trị).

Ta có thể khép mục **2. 자원 처리 오류 (Resource Handling Errors)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **2. 자원 처리 오류 (Resource Handling Errors)** đặt vấn đề; **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)** đối chiếu bằng chứng, rồi **네트워크 관련 장비 (Network Equipment)** mở rộng hệ quả hoặc giới hạn liên quan.

## 5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)

Từ **2. 자원 처리 오류 (Resource Handling Errors)**, ta đã có điểm tựa để bước vào **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/86 trước khi đi vào chi tiết.

Để đọc **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **5.1 신기술 동향 (New Technologies)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 5.1 신기술 동향 (New Technologies)

Các ý ngay dưới **5.1 신기술 동향 (New Technologies)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “5.1 신기술 동향 (New Technologies)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **SDN (Software Defined Networking):** 네트워크를 가상화하여 소프트웨어로 제어/관리.
- **SDS (Software-Defined Storage):** 물리적 스토리지를 가상화하여 하나처럼 관리.
- **SDDC (Software Defined Data Center):** 데이터 센터의 모든 자원을 가상화하여 소프트웨어 조작만으로 자동 제어.
- **클라우드 기반 HSM:** 클라우드 기반 암호화 키 생성/처리 하드웨어 보안기기.
- **파스-타 (PaaS-TA):** 개발 환경을 제공하는 개방형 클라우드 플랫폼.
- **징 (Zing):** 10cm 이내에서 3.5Gbps 속도의 초고속 근접무선통신.
- **스마트 그리드 (Smart Grid):** 전력선을 기반으로 효율적 에너지 관리 통합 시스템.
- **SSO (Single Sign On):** 한 번 로그인으로 여러 사이트 이용.
- **메시 네트워크 (Mesh Network):** 여러 디바이스를 그물망처럼 유기적으로 연결.
- **피코넷 (PICONET):** 블루투스/UWB 기술로 형성하는 독립적 무선망.
- **Tiếng Việt:**
  - SDN/SDS/SDDC: Ảo hóa và điều khiển mạng/lưu trữ/trung tâm dữ liệu bằng phần mềm.
  - PaaS-TA: Nền tảng cloud mở của Hàn Quốc.
  - SSO: Đăng nhập một lần.
  - Zing: Giao tiếp không dây tầm cực gần, tốc độ cao.

Các bullet của **5.1 신기술 동향 (New Technologies)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **5.1 신기술 동향 (New Technologies)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **5.2 LAN 표준 및 위상 (LAN Standards & Topology)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **5.2 LAN 표준 및 위상 (LAN Standards & Topology)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 5.2 LAN 표준 및 위상 (LAN Standards & Topology)

Bây giờ ta đi vào nội dung của **5.2 LAN 표준 및 위상 (LAN Standards & Topology)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “5.2 LAN 표준 및 위상 (LAN Standards & Topology)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **CSMA/CD:** IEEE 802.3 유선 LAN 매체 접속 제어 방식 (충돌 감지).
- **CSMA/CA:** 무선 랜(WLAN) 데이터 전송 시 충돌을 피하기 위해 일정 시간 기다림 (충돌 회피).
- **WPA (Wi-Fi Protected Access):** 무선 랜 인증/암호화 표준.
- **802.11e:** QoS 기능 지원을 위해 MAC 계층 수정.
- **버스형 (Bus Topology):** 한 통신 회선에 여러 단말장치 연결.
- **VLAN (Virtual LAN):** 물리적 배치와 무관하게 논리적으로 네트워크 분리.
- **WDM (Wavelength Division Multiplexing):** 파장이 다른 광선을 이용해 동시 통신 (광다중화).
- **Tiếng Việt:**
  - CSMA/CD: Phát hiện xung đột (Mạng có dây).
  - CSMA/CA: Tránh xung đột (Mạng không dây).
  - VLAN: Mạng LAN ảo, phân chia logic không phụ thuộc vật lý.

Các bullet của **5.2 LAN 표준 및 위상 (LAN Standards & Topology)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **5.2 LAN 표준 및 위상 (LAN Standards & Topology)**, đừng bắt đầu lại từ số không. **5.3 라우팅 프로토콜 및 흐름 제어 (Routing Protocols & Flow Control)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **5.3 라우팅 프로토콜 및 흐름 제어 (Routing Protocols & Flow Control)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 5.3 라우팅 프로토콜 및 흐름 제어 (Routing Protocols & Flow Control)

Phần nguồn của **5.3 라우팅 프로토콜 및 흐름 제어 (Routing Protocols & Flow Control)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “5.3 라우팅 프로토콜 및 흐름 제어 (Routing Protocols & Flow Control)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **ARP (Address Resolution Protocol):** IP 주소를 MAC 주소로 변환.
- **RIP (Routing Information Protocol):** 거리 벡터 라우팅 (최대 홉 15 제한).
- **OSPF (Open Shortest Path First):** 링크 상태 기반 최단 경로 라우팅 (대규모 망).
- **흐름 제어 - 정지-대기 (Stop-and-Wait):** 수신 측의 ACK(확인 신호)를 받은 후 다음 패킷 전송.
- **Tiếng Việt:**
  - ARP: IP -> MAC.
  - RIP: Dựa trên số Hop (tối đa 15).
  - OSPF: Dựa trên trạng thái Link, tìm đường ngắn nhất.
  - Stop-and-Wait: Chờ phản hồi (ACK) rồi mới gửi tiếp.

Các bullet của **5.3 라우팅 프로토콜 및 흐름 제어 (Routing Protocols & Flow Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **5.3 라우팅 프로토콜 및 흐름 제어 (Routing Protocols & Flow Control)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **네트워크 관련 장비 (Network Equipment)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **네트워크 관련 장비 (Network Equipment)** nối từ **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)** sang **네트워크 구조 및 기술 (Network Structures & Technologies)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 네트워크 관련 장비 (Network Equipment)

Ở bước 19/86, **네트워크 관련 장비 (Network Equipment)** xuất hiện như phần tiếp nối của **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **네트워크 관련 장비 (Network Equipment)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **NIC (Network Interface Card)**, **허브 (Hub)**, **리피터 (Repeater)**, **브리지 (Bridge)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “네트워크 관련 장비 (Network Equipment)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **NIC (Network Interface Card)**: 컴퓨터와 네트워크 연결 (랜카드).
- **허브 (Hub)**: 여러 컴퓨터 연결 및 회선 통합 관리 (리피터 역할 포함).
- **리피터 (Repeater)**: 약해진 신호를 증폭/재생하여 다시 전송.
- **브리지 (Bridge)**: LAN과 LAN을 연결 (MAC 주소 기반).
- **스위치 (Switch)**: 브리지와 유사하나 하드웨어 기반으로 속도가 더 빠름.
- **라우터 (Router)**: 최적 경로(Routing) 선택, 서로 다른 네트워크 연결 (네트워크 계층).
- **게이트웨이 (Gateway)**: 프로토콜이 전혀 다른 네트워크들을 연결하는 출입구 역할 (전 계층).

💡 **Mẹo ghi nhớ (Mnemonics):**
- **Repeater**: Tầng 1 (Khuếch đại tín hiệu).
- **Bridge/Switch**: Tầng 2 (Nối LAN).
- **Router**: Tầng 3 (Tìm đường IP).
- **Gateway**: Tầng 4-7 (Cổng nối các mạng khác biệt).

Như vậy, **네트워크 관련 장비 (Network Equipment)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **네트워크 구조 및 기술 (Network Structures & Technologies)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **네트워크 구조 및 기술 (Network Structures & Technologies)** nối từ **네트워크 관련 장비 (Network Equipment)** sang **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 네트워크 구조 및 기술 (Network Structures & Technologies)

Sau khi đã đặt nền bằng **네트워크 관련 장비 (Network Equipment)**, ta chuyển sang **네트워크 구조 및 기술 (Network Structures & Technologies)**. Đây là mắt xích 20/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **네트워크 구조 및 기술 (Network Structures & Technologies)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **성형 (Star, 중앙 집중형)**, **링형 (Ring, 루프형)**, **버스형 (Bus)**, **계층형 (Tree, 분산형)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 네트워크 설치 구조 (Network Topologies)**. Hãy xác định **1. 네트워크 설치 구조 (Network Topologies)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 네트워크 설치 구조 (Network Topologies)

Phần nguồn của **1. 네트워크 설치 구조 (Network Topologies)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 네트워크 설치 구조 (Network Topologies)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **성형 (Star, 중앙 집중형)**: 중앙 컴퓨터를 중심으로 단말기가 연결 (Point-to-Point).
- **링형 (Ring, 루프형)**: 이웃하는 장치끼리 연결. 단방향 시 하나만 고장나도 전체 마비.
- **버스형 (Bus)**: 한 개의 통신 회선에 여러 장치 연결 (단말기 추가/제거 용이).
- **계층형 (Tree, 분산형)**: 중앙에서 중간 단말장치로 다시 분기되는 형태.
- **망형 (Mesh)**: 모든 지점을 연결. 통신량이 많을 때 유리하며 회선이 가장 많이 필요함 (`n(n-1)/2` 개).

Các bullet của **1. 네트워크 설치 구조 (Network Topologies)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 네트워크 설치 구조 (Network Topologies)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 근거리 통신망 (LAN) 표준 및 기술** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 근거리 통신망 (LAN) 표준 및 기술** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 근거리 통신망 (LAN) 표준 및 기술

Các ý ngay dưới **2. 근거리 통신망 (LAN) 표준 및 기술** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2. 근거리 통신망 (LAN) 표준 및 기술” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **IEEE 802 규격**: 802.3(CSMA/CD), 802.4(토큰 버스), 802.5(토큰 링), 802.11(무선 LAN).
- **VLAN**: 물리적 배치와 상관없이 논리적으로 분리하는 기술.
- **CSMA/CA**: 무선 LAN(802.11)에서 매체가 비어있음을 확인 후 충돌 회피(Avoidance)를 위해 기다렸다가 전송하는 방식.

Các bullet của **2. 근거리 통신망 (LAN) 표준 및 기술** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 근거리 통신망 (LAN) 표준 및 기술**, đừng bắt đầu lại từ số không. **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)

Bây giờ ta đi vào nội dung của **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **IGP (내부 게이트웨이 프로토콜)**: AS 내에서 사용. **RIP**(거리 벡터, 최대 15홉 제한)와 **OSPF**(링크 상태, 대규모 망)가 있음.
- **EGP / BGP**: AS(자율 시스템) 간의 라우팅 프로토콜.
- **흐름 제어**: **정지-대기(Stop-and-Wait)** (수신 확인 후 다음 패킷 전송) / **슬라이딩 윈도우(Sliding Window)** (수신 확인 없이 윈도우 크기만큼 연속 전송).

💡 **Mẹo ghi nhớ (Mnemonics):**
- **RIP**: 15 Hops max (Dùng cho mạng nhỏ).
- **OSPF**: Link State (Dùng cho mạng lớn).
- **CSMA/CD**: Mạng LAN có dây (Collision Detection).
- **CSMA/CA**: Mạng không dây (Collision Avoidance).

Các bullet của **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **네트워크 구조 및 기술 (Network Structures & Technologies)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** nối từ **네트워크 구조 및 기술 (Network Structures & Technologies)** sang **네트워크 보안 기술 (Network Security Tech)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 네트워크 및 정보 침해 공격 (Network & Info Security Attacks)

Từ **네트워크 구조 및 기술 (Network Structures & Technologies)**, ta đã có điểm tựa để bước vào **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/86 trước khi đi vào chi tiết.

Để đọc **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **DDoS (분산 서비스 거부 공격)**, **스머핑 (SMURFING)**, **세션 하이재킹 (Session Hijacking)**, **스위치 재밍 (Switch Jamming)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 네트워크 공격** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 네트워크 공격

Các ý ngay dưới **1. 네트워크 공격** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “1. 네트워크 공격” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DDoS (분산 서비스 거부 공격)**: 여러 대의 PC(Agent/Zombie)를 이용해 특정 서버에 대량의 트래픽을 보내 마비시킴. (툴: Trin00, TFN, TFN2K, Stacheldraht).
- **스머핑 (SMURFING)**: IP/ICMP 특성을 악용해 한 사이트에 엄청난 데이터를 집중시키는 공격.
- **세션 하이재킹 (Session Hijacking)**: 클라이언트 세션을 가로채어 정상적인 사용자인 척하는 공격.
- **스위치 재밍 (Switch Jamming)**: 위조된 MAC 주소를 대량으로 보내 스위치를 더미 허브처럼 작동하게 만듦.

Các bullet của **1. 네트워크 공격** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 네트워크 공격** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 블루투스 공격** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. 블루투스 공격**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. 블루투스 공격

Bây giờ ta đi vào nội dung của **2. 블루투스 공격**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. 블루투스 공격” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **블루버그 (BlueBug)**: 원격 조종 및 통화 감청.
- **블루스나프 (BlueSnarf)**: 장비 파일에 접근해 정보 탈취.
- **블루재킹 (BlueJacking)**: 스팸 메시지를 익명으로 퍼뜨림.

Các bullet của **2. 블루투스 공격** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 블루투스 공격**, đừng bắt đầu lại từ số không. **3. 시스템 및 소프트웨어 공격** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3. 시스템 및 소프트웨어 공격**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3. 시스템 및 소프트웨어 공격

Phần nguồn của **3. 시스템 및 소프트웨어 공격** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3. 시스템 및 소프트웨어 공격” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **제로 데이 공격 (Zero Day Attack)**: 보안 취약점이 공표되기 전, 혹은 패치가 나오기 전에 신속하게 이루어지는 공격.
- **랜섬웨어 (Ransomware)**: 파일을 암호화하고 돈(Ransom)을 요구하는 악성 프로그램.
- **백도어 (Back Door)**: 관리자 편의를 위해 만들어 놓은 비밀 통로를 악용.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **BlueSnarf**: Sniff (Đánh hơi/Trộm thông tin).
- **BlueBug**: Bug (Cài bọ/Nghe lén).
- **BlueJacking**: Hijack (Chặn tin/Gửi tin nhắn rác).

Các bullet của **3. 시스템 및 소프트웨어 공격** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 시스템 및 소프트웨어 공격** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **네트워크 보안 기술 (Network Security Tech)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **네트워크 보안 기술 (Network Security Tech)** nối từ **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)** sang **계층별 주요 프로토콜 (Major Protocols by Layer)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 네트워크 보안 기술 (Network Security Tech)

Ở bước 22/86, **네트워크 보안 기술 (Network Security Tech)** xuất hiện như phần tiếp nối của **네트워크 및 정보 침해 공격 (Network & Info Security Attacks)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **네트워크 보안 기술 (Network Security Tech)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **VPN (가상 사설 통신망)**, **SSH (시큐어 셸)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “네트워크 보안 기술 (Network Security Tech)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **VPN (가상 사설 통신망)**: 공중 네트워크를 전용 회선처럼 사용할 수 있게 해주는 암호화 보안 솔루션.
- **SSH (시큐어 셸)**: 원격 로그인, 파일 복사 등을 안전하게 수행하는 프로토콜 (포트 22번 사용, 데이터 암호화 지원).

Như vậy, **네트워크 보안 기술 (Network Security Tech)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **계층별 주요 프로토콜 (Major Protocols by Layer)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **계층별 주요 프로토콜 (Major Protocols by Layer)** nối từ **네트워크 보안 기술 (Network Security Tech)** sang **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 계층별 주요 프로토콜 (Major Protocols by Layer)

Sau khi đã đặt nền bằng **네트워크 보안 기술 (Network Security Tech)**, ta chuyển sang **계층별 주요 프로토콜 (Major Protocols by Layer)**. Đây là mắt xích 23/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **계층별 주요 프로토콜 (Major Protocols by Layer)** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **FTP**, **TELNET**, **TCP**, **UDP** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 응용 계층 (Application)**. Hãy xác định **1. 응용 계층 (Application)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 응용 계층 (Application)

Phần nguồn của **1. 응용 계층 (Application)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 응용 계층 (Application)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **FTP**: 파일 전송 / **SMTP**: 이메일 송신 / **HTTP**: 웹 문서 송수신
- **TELNET**: 원격 접속 가상 터미널 / **DNS**: 도메인 네임을 IP 주소로 변환

Các bullet của **1. 응용 계층 (Application)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 응용 계층 (Application)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 전송 계층 (Transport)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 전송 계층 (Transport)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 전송 계층 (Transport)

Các ý ngay dưới **2. 전송 계층 (Transport)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2. 전송 계층 (Transport)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **TCP**: 연결 지향, 양방향, 신뢰성 보장, 스트림 위주 전달, 흐름 및 순서 제어 기능 제공.
- **UDP**: 비연결형, 빠른 전송 속도 (실시간 전송 유리, 오버헤드 적음).

Các bullet của **2. 전송 계층 (Transport)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 전송 계층 (Transport)**, đừng bắt đầu lại từ số không. **3. 인터넷 계층 (Internet / Network)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. 인터넷 계층 (Internet / Network)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. 인터넷 계층 (Internet / Network)

Bây giờ ta đi vào nội dung của **3. 인터넷 계층 (Internet / Network)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. 인터넷 계층 (Internet / Network)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **IP**: 데이터 주소 지정 및 경로 설정.
- **ICMP**: 제어 메시지 및 오류 처리 관리.
- **ARP**: IP 주소 -> MAC 주소 (물리적 주소)로 변환.
- **RARP**: MAC 주소 -> IP 주소로 변환.

Các bullet của **3. 인터넷 계층 (Internet / Network)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**3. 인터넷 계층 (Internet / Network)** vừa cho ta cách đặt câu hỏi. Bây giờ **4. 네트워크 액세스 계층 (Data Link & Physical)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **4. 네트워크 액세스 계층 (Data Link & Physical)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 4. 네트워크 액세스 계층 (Data Link & Physical)

Phần nguồn của **4. 네트워크 액세스 계층 (Data Link & Physical)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “4. 네트워크 액세스 계층 (Data Link & Physical)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Ethernet (IEEE 802.3)**, **HDLC**, **X.25**, **RS-232C** 등.

Các bullet của **4. 네트워크 액세스 계층 (Data Link & Physical)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **4. 네트워크 액세스 계층 (Data Link & Physical)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **계층별 주요 프로토콜 (Major Protocols by Layer)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **계층별 주요 프로토콜 (Major Protocols by Layer)** đặt vấn đề; **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** đối chiếu bằng chứng, rồi **데이터베이스 신기술 (DB New Technologies)** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)

Từ **계층별 주요 프로토콜 (Major Protocols by Layer)**, ta đã có điểm tựa để bước vào **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/86 trước khi đi vào chi tiết.

Để đọc **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **7.1 회복 및 동시성 제어 (Recovery & Concurrency)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 7.1 회복 및 동시성 제어 (Recovery & Concurrency)

Các ý ngay dưới **7.1 회복 및 동시성 제어 (Recovery & Concurrency)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “7.1 회복 및 동시성 제어 (Recovery & Concurrency)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **회복 (Recovery):** 장애 발생 시 손상 이전의 정상 상태로 복구.
- **즉각 갱신 기법 (Immediate Update):** 트랜잭션 부분 완료 전이라도 즉시 DB에 반영. 갱신 내용은 **Log에 보관**하여 회복에 대비.
- **로킹 단위 (Locking Granularity):** 병행제어에서 한꺼번에 로킹하는 객체 크기.
  - **단위가 크면:** 로크 수가 작아 관리하기 쉽지만 병행성 저하.
  - **단위가 작으면:** 로크 수가 많아 관리 복잡/오버헤드 증가, 하지만 병행성 상승.
- **타임 스탬프 순서 (Time Stamp Ordering):** 직렬성 순서를 결정하기 위해 트랜잭션 처리 순서를 미리 선택.
- **Tiếng Việt:**
  - Immediate Update: Cập nhật ngay lập tức (dùng Log để phục hồi).
  - Locking Granularity: Kích thước khóa. Khóa lớn -> dễ quản lý, đồng thời thấp. Khóa nhỏ -> khó quản lý, đồng thời cao.

Các bullet của **7.1 회복 및 동시성 제어 (Recovery & Concurrency)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **7.1 회복 및 동시성 제어 (Recovery & Concurrency)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **7.2 교착상태 (Deadlock)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **7.2 교착상태 (Deadlock)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 7.2 교착상태 (Deadlock)

Bây giờ ta đi vào nội dung của **7.2 교착상태 (Deadlock)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “7.2 교착상태 (Deadlock)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **발생 4가지 조건:** 상호 배제(Mutual Exclusion), 점유와 대기(Hold and Wait), 비선점(Non-preemption), 환형 대기(Circular Wait).
- **회피 기법 (Avoidance):** 교착상태 가능성을 피해 나가는 방법. 주로 **은행원 알고리즘 (Banker's Algorithm, E. J. Dijkstra)** 사용.
- **Tiếng Việt:** 4 điều kiện Deadlock: Loại trừ lẫn nhau, Giữ & Chờ, Không trưng dụng, Chờ vòng tròn. Tránh Deadlock dùng Thuật toán Nhà băng.
- 💡 **Mẹo ghi nhớ:** Điều kiện Deadlock: Độc Giữ Không Vòng (Độc quyền, Giữ và chờ, Không ưu tiên, Vòng tròn).

Các bullet của **7.2 교착상태 (Deadlock)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **7.2 교착상태 (Deadlock)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **데이터베이스 신기술 (DB New Technologies)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)** đặt vấn đề; **데이터베이스 신기술 (DB New Technologies)** đối chiếu bằng chứng, rồi **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** mở rộng hệ quả hoặc giới hạn liên quan.

## 데이터베이스 신기술 (DB New Technologies)

Ở bước 25/86, **데이터베이스 신기술 (DB New Technologies)** xuất hiện như phần tiếp nối của **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **데이터베이스 신기술 (DB New Technologies)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **하둡 (Hadoop)**, **맵리듀스 (MapReduce)**, **데이터 마이닝 (Data Mining)**, **OLAP** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 빅데이터 및 분석 기술** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 빅데이터 및 분석 기술** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 빅데이터 및 분석 기술

Bây giờ ta đi vào nội dung của **1. 빅데이터 및 분석 기술**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. 빅데이터 및 분석 기술” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **하둡 (Hadoop)**: 대용량 데이터를 병렬로 처리하기 위한 자바 소프트웨어 프레임워크 (오픈소스).
- **맵리듀스 (MapReduce)**: 하둡 기반 분산 처리 프로그래밍 모델 (Map으로 분류, Reduce로 추출).
- **데이터 마이닝 (Data Mining)**: 대량의 데이터에서 패턴을 규명하여 유용한 정보를 추출하는 기법.
- **OLAP**: 다차원 데이터로부터 통계적 요약 정보를 분석하여 의사결정에 활용. (연산: Roll-up, Drill-down, Pivoting 등).

Các bullet của **1. 빅데이터 및 분석 기술** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **1. 빅데이터 및 분석 기술**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **데이터베이스 신기술 (DB New Technologies)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** nối từ **데이터베이스 신기술 (DB New Technologies)** sang **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)

Sau khi đã đặt nền bằng **데이터베이스 신기술 (DB New Technologies)**, ta chuyển sang **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)**. Đây là mắt xích 26/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **8.1 보안 기본 요소 및 프레임워크**. Hãy xác định **8.1 보안 기본 요소 및 프레임워크** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 8.1 보안 기본 요소 및 프레임워크

Phần nguồn của **8.1 보안 기본 요소 및 프레임워크** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “8.1 보안 기본 요소 및 프레임워크” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **보안 3대 요소 (CIA Triad):**
  - **기밀성 (Confidentiality):** 인가된 사용자에게만 접근 허용.
  - **무결성 (Integrity):** 인가된 사용자만 수정 가능.
  - **가용성 (Availability):** 인가받은 사용자는 언제라도 사용 가능.
- **Seven Touchpoints:** 소프트웨어 보안 모범사례를 SDLC(소프트웨어 생명주기)에 통합.
- **OWASP:** 웹 보안 취약점을 연구하는 비영리 단체.
- **관리적/물리적/기술적 보안:**
  - 관리적 (정책, 교육), 물리적 (출입 통제, 재해 복구), 기술적 (사용자 인증, 접근 제어).
- **Tiếng Việt:** 3 yếu tố bảo mật CIA: Tính bảo mật, Tính toàn vẹn, Tính sẵn sàng.

Các bullet của **8.1 보안 기본 요소 및 프레임워크** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **8.1 보안 기본 요소 및 프레임워크** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **8.2 시스템 보안 기술** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **8.2 시스템 보안 기술** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 8.2 시스템 보안 기술

Các ý ngay dưới **8.2 시스템 보안 기술** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “8.2 시스템 보안 기술” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **TCP 래퍼 (TCP Wrapper):** 외부 접속 인가 여부를 점검하여 허용/거부하는 도구.
- **Secure OS:** 보안 기능을 갖춘 커널을 이식하여 시스템 자원 보호.
- **침입 탐지 시스템 (IDS):** 실시간으로 비정상적 사용 탐지 (오용 탐지: 패턴 기반, 이상 탐지: 평균 상태 기준).
- **고가용성 솔루션 (HACMP):** 장애 발생 시 즉시 다른 시스템으로 대체 가능하게 하는 환경.
- **인증 (Authentication):** 지식 기반(패스워드), 소유 기반(스마트카드), 행위 기반(서명).
- **커널 로그:**
  - `wtmp`: 성공한 로그인/로그아웃.
  - `utmp`: 현재 로그인 상태.
  - `btmp`: 실패한 로그인.
  - `lastlog`: 마지막 성공 로그인.
- **Tiếng Việt:** Secure OS, IDS (phát hiện xâm nhập), HACMP (giải pháp độ sẵn sàng cao). Phân loại log kernel (wtmp, utmp, v.v.).

Các bullet của **8.2 시스템 보안 기술** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **8.2 시스템 보안 기술** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** nối từ **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)** sang **정보 보안 및 하드웨어 신기술 (Security & HW Tech)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)

Từ **8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)**, ta đã có điểm tựa để bước vào **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/86 trước khi đi vào chi tiết.

Để đọc **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **10.1 웹 및 애플리케이션 취약점** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 10.1 웹 및 애플리케이션 취약점

Các ý ngay dưới **10.1 웹 및 애플리케이션 취약점** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “10.1 웹 및 애플리케이션 취약점” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **SQL 삽입 (SQL Injection):** SQL을 삽입하여 DB 유출/변조 및 인증 우회.
- **크로스사이트 스크립팅 (XSS):** 악의적인 스크립트를 삽입하여 방문자 정보 탈취.
- **경로 조작 및 자원 삽입:** 데이터 입출력 경로 조작으로 자원 삭제/수정.
- **메모리 버퍼 오버플로:** 메모리 범위를 넘어선 위치에서 쓰기 시도. 방어 기술로 **스택 가드(Stack Guard)** 사용.
- **하드코드된 비밀번호:** 소스코드 내부에 비밀번호를 직접 입력하는 취약점.
- **Tiếng Việt:** Các lỗ hổng web: SQL Injection (chèn lệnh SQL), XSS (chèn script độc hại), Buffer Overflow (tràn bộ đệm - phòng bằng Stack Guard).

Các bullet của **10.1 웹 및 애플리케이션 취약점** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **10.1 웹 및 애플리케이션 취약점** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)

Bây giờ ta đi vào nội dung của **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **세션 하이재킹 (Session Hijacking):** 클라이언트의 세션 정보를 가로채는 공격.
- **DDoS 공격:** 여러 분산된 지점에서 한 곳을 공격. (툴: Trin00, TFN, TFN2K, Stacheldraht).
- **Ping of Death:** 허용 범위 이상의 큰 ICMP 패킷을 전송해 마비시킴.
- **Ping Flood:** 많은 ICMP 메시지를 보내 응답으로 자원 고갈시킴.
- **스머핑 (SMURFING):** IP/ICMP 특성을 악용해 한 사이트에 집중적으로 데이터 보냄.
- **DPI (Deep Packet Inspection):** 전 계층의 프로토콜과 패킷 내부를 파악해 침입 탐지.
- **Tiếng Việt:**
  - DDoS: Tấn công từ chối dịch vụ phân tán.
  - Ping of Death: Gửi gói ICMP quá lớn.
  - SMURFING: Gửi lượng lớn dữ liệu tập trung.

Các bullet của **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **10.2 네트워크 및 분산 서비스 거부 공격 (DoS/DDoS)**, đừng bắt đầu lại từ số không. **10.3 시스템 해킹 및 악성코드** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **10.3 시스템 해킹 및 악성코드**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 10.3 시스템 해킹 및 악성코드

Phần nguồn của **10.3 시스템 해킹 및 악성코드** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “10.3 시스템 해킹 및 악성코드” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **백도어 (Back Door):** 보안을 제거하고 만들어 놓은 비밀 통로 (탐지: 무결성 검사, 열린 포트 등).
- **키로거 공격 (Key Logger):** 키보드 움직임을 탐지해 개인정보 탈취.
- **랜섬웨어 (Ransomware):** 문서 암호화 후 돈(Ransom)을 요구.
- **웜 (Worm):** 네트워크를 통해 스스로 전파·복제되는 악성 코드로, 숙주 파일에 기생해야 하는 바이러스와 구분한다.
- **허니팟 (Honeypot):** 비정상 접근 탐지를 위해 의도적으로 설치한 시스템 (미끼).
- **피싱 (Phishing):** 공공/금융 기관을 사칭해 개인정보 탈취.
- **Tiếng Việt:** Backdoor (Cửa hậu), Key Logger (Ghi thao tác bàn phím), Ransomware (Mã độc tống tiền), Worm (Giun máy tính - tự nhân bản), Honeypot (Hệ thống mồi nhử).

Các bullet của **10.3 시스템 해킹 및 악성코드** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**10.3 시스템 해킹 및 악성코드** vừa cho ta cách đặt câu hỏi. Bây giờ **10.4 기타 네트워크 공격** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **10.4 기타 네트워크 공격** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 10.4 기타 네트워크 공격

Các ý ngay dưới **10.4 기타 네트워크 공격** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “10.4 기타 네트워크 공격” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **스위치 재밍 (Switch Jamming):** 위조된 MAC 주소를 흘려보내 스위치를 더미 허브로 작동하게 만듦.
- **블루투스 관련 공격:**
  - **블루버그 (BlueBug):** 취약한 연결 관리 악용.
  - **블루스나프 (BlueSnarf):** 취약점 활용해 파일 접근.
  - **블루프린팅 (BluePrinting):** 공격 대상 장비 검색.
  - **블루재킹 (BlueJacking):** 익명으로 스팸 메시지 퍼뜨림.
- **Tiếng Việt:** Tấn công Switch Jamming (biến Switch thành Hub) và các tấn công Bluetooth (BlueBug, BlueSnarf, BlueJacking).
- 💡 **Mẹo ghi nhớ:** Blue**Jacking** = **Spam message**. Blue**Snarf** = **Snatch files** (cướp file).

Với **10.4 기타 네트워크 공격**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **10.4 기타 네트워크 공격**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **정보 보안 및 하드웨어 신기술 (Security & HW Tech)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** nối từ **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)** sang **소프트웨어 보안 (Software Security)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 정보 보안 및 하드웨어 신기술 (Security & HW Tech)

Ở bước 28/86, **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** xuất hiện như phần tiếp nối của **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **BaaS (Blockchain as a Service)**, **OWASP**, **허니팟 (Honeypot)**, **Secure OS** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 보안 용어 및 Secure OS** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 보안 용어 및 Secure OS** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 보안 용어 및 Secure OS

Bây giờ ta đi vào nội dung của **1. 보안 용어 및 Secure OS**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. 보안 용어 및 Secure OS” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **BaaS (Blockchain as a Service)**: 클라우드 기반 블록체인 개발 환경 제공.
- **OWASP**: 웹 취약점을 연구하는 비영리 단체 (10대 취약점 발표).
- **허니팟 (Honeypot)**: 침입자를 속여 정보를 수집하기 위해 설치해 둔 시스템 (미끼).
- **Secure OS**: 기존 OS에 보안 기능 커널을 이식한 운영체제. 암호적, 논리적, 시간적, 물리적 분리 방법을 통해 보호하며 식별, 인증, 접근통제(MAC, DAC) 기능을 제공합니다.

Các bullet của **1. 보안 용어 및 Secure OS** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 보안 용어 및 Secure OS** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 하드웨어 신기술** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 하드웨어 신기술**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 하드웨어 신기술

Phần nguồn của **2. 하드웨어 신기술** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. 하드웨어 신기술” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **HA (High Availability, 고가용성)**: 장애 발생 시 즉시 다른 시스템으로 대체 가능한 이중화 환경.
- **RAID**: 여러 개의 하드디스크에 데이터를 분산 저장하여 속도와 안정성을 향상시키는 기술.
- **트러스트존 (TrustZone)**: 프로세서 내에 일반 구역과 보안 구역을 분할하는 ARM의 하드웨어 보안 기술.

Các bullet của **2. 하드웨어 신기술** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 하드웨어 신기술** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **소프트웨어 보안 (Software Security)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **소프트웨어 보안 (Software Security)** nối từ **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** sang **인증 및 보안 체계 (Authentication & Security System)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 소프트웨어 보안 (Software Security)

Sau khi đã đặt nền bằng **정보 보안 및 하드웨어 신기술 (Security & HW Tech)**, ta chuyển sang **소프트웨어 보안 (Software Security)**. Đây là mắt xích 29/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **소프트웨어 보안 (Software Security)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **기밀성 (Confidentiality)**, **무결성 (Integrity)**, **가용성 (Availability)**, **방법론** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 보안 3대 요소 (CIA Triad)**. Hãy xác định **1. 보안 3대 요소 (CIA Triad)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 보안 3대 요소 (CIA Triad)

Phần nguồn của **1. 보안 3대 요소 (CIA Triad)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 보안 3대 요소 (CIA Triad)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **기밀성 (Confidentiality)**: 인가된 사용자만 접근 가능 (암호화).
- **무결성 (Integrity)**: 인가된 사용자만 수정 가능 (변조 방지).
- **가용성 (Availability)**: 인가된 사용자는 언제든 사용 가능.
- 기타: 인증(Authentication), 부인 방지(Non-Repudiation).

Các bullet của **1. 보안 3대 요소 (CIA Triad)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 보안 3대 요소 (CIA Triad)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. Secure SDLC** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. Secure SDLC** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. Secure SDLC

Các ý ngay dưới **2. Secure SDLC** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

보안상 안전한 SW 개발을 위해 SDLC(생명주기)에 보안 활동을 추가한 것.
- **방법론**: CLASP(초기 단계 중심), SDL(MS사 개발), Seven Touchpoints(각 단계별 모범사례 적용).

Các bullet của **2. Secure SDLC** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. Secure SDLC**, đừng bắt đầu lại từ số không. **3. 주요 보안 약점 및 방어** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. 주요 보안 약점 및 방어**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. 주요 보안 약점 및 방어

Bây giờ ta đi vào nội dung của **3. 주요 보안 약점 및 방어**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. 주요 보안 약점 및 방어” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **SQL 삽입 (SQL Injection)**: 입력 폼에 SQL 명령어를 넣어 DB를 조작. (방어: 입력값 필터링 및 매개변수화).
- **XSS (크로스사이트 스크립팅)**: 웹페이지에 악성 스크립트를 삽입해 사용자 정보 탈취. (방어: `<, >, &` 등 특수문자 치환).
- **메모리 버퍼 오버플로**: 할당된 메모리 범위를 넘어서 기록하여 오동작 유발.
  - **스택 가드 (Stack Guard)**: 복귀 주소와 변수 사이에 특정 값을 넣어 오버플로를 탐지하는 기술.
- **접근 지정자 (Access Modifier)**: `Public`(모두 접근), `Protected`(패키지+상속), `Default`(같은 패키지), `Private`(클래스 내부만).

💡 **Mẹo ghi nhớ (Mnemonics):**
- 보안 3요소: **C.I.A** (Confidentiality - Integrity - Availability).
- 접근 한정자: **P.P.D.P** (Public - Protected - Default - Private).

Các bullet của **3. 주요 보안 약점 및 방어** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 주요 보안 약점 및 방어** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **소프트웨어 보안 (Software Security)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **인증 및 보안 체계 (Authentication & Security System)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **인증 및 보안 체계 (Authentication & Security System)** nối từ **소프트웨어 보안 (Software Security)** sang **소프트웨어 개발 보안 관련 법규**, vì cơ chế trước tạo đầu vào cho bước sau.

## 인증 및 보안 체계 (Authentication & Security System)

Từ **소프트웨어 보안 (Software Security)**, ta đã có điểm tựa để bước vào **인증 및 보안 체계 (Authentication & Security System)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 30/86 trước khi đi vào chi tiết.

Để đọc **인증 및 보안 체계 (Authentication & Security System)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **지식 기반 (Something You Know)**, **소유 기반 (Something You Have)**, **생체 기반 (Something You Are)**, **위치 기반 (Somewhere You Are)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 인증 수단 4가지** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 인증 수단 4가지

Các ý ngay dưới **1. 인증 수단 4가지** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “1. 인증 수단 4가지” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **지식 기반 (Something You Know)**: 패스워드, PIN (머릿속 기억).
- **소유 기반 (Something You Have)**: 신분증, 스마트카드, OTP.
- **생체 기반 (Something You Are)**: 지문, 홍채, 정맥 인식.
- **위치 기반 (Somewhere You Are)**: 접속 IP 위치, GPS.

Các bullet của **1. 인증 수단 4가지** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 인증 수단 4가지** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 보안 체계 3영역** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. 보안 체계 3영역**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. 보안 체계 3영역

Bây giờ ta đi vào nội dung của **2. 보안 체계 3영역**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. 보안 체계 3영역” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **관리적 보안**: 정보보호 정책, 조직, 교육 등 사람 중심.
- **물리적 보안**: 출입 통제, 전산실 관리 등 물리적 보호.
- **기술적 보안**: 사용자 인증, 암호화, 접근 제어 등 IT 기술 보호.

Các bullet của **2. 보안 체계 3영역** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 보안 체계 3영역** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **인증 및 보안 체계 (Authentication & Security System)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **소프트웨어 개발 보안 관련 법규**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **소프트웨어 개발 보안 관련 법규** nối từ **인증 및 보안 체계 (Authentication & Security System)** sang **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 소프트웨어 개발 보안 관련 법규

Ở bước 31/86, **소프트웨어 개발 보안 관련 법규** xuất hiện như phần tiếp nối của **인증 및 보안 체계 (Authentication & Security System)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **소프트웨어 개발 보안 관련 법규** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개인정보 보호법**, **정보통신망법**, **신용정보법**, **위치정보법** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “소프트웨어 개발 보안 관련 법규” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개인정보 보호법**: 개인정보 처리 및 보호에 관한 전반적 사항.
- **정보통신망법**: 정보통신망을 통한 개인정보 수집/이용 보호.
- **신용정보법**: 개인의 신용정보 취급 보호.
- **위치정보법**: 개인 위치정보 수집 및 제공 보호.

Như vậy, **소프트웨어 개발 보안 관련 법규** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)** nối từ **소프트웨어 개발 보안 관련 법규** sang **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)**, vì cơ chế trước tạo đầu vào cho bước sau.

## ⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)

Sau khi đã đặt nền bằng **소프트웨어 개발 보안 관련 법규**, ta chuyển sang **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)**. Đây là mắt xích 32/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các đoạn prose và thuật ngữ bên dưới cần được đọc như các bước trả lời cho câu hỏi đó.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta có thể khép mục **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)** nối từ **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)** sang **9. 암호화 기술 (Công nghệ Mã hóa)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)

Từ **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)**, ta đã có điểm tựa để bước vào **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/86 trước khi đi vào chi tiết.

Để đọc **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **적절한 인증 없이 중요기능 허용 (Missing Authentication)**, **중요정보 평문 저장 및 전송 (Plaintext Storage/Transmission)**, **하드코드된 비밀번호 (Hardcoded Password)**, **오류 메시지 통한 정보 노출 (Information Exposure Through Error Message)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **적절한 인증 없이 중요기능 허용 (Missing Authentication)**: 중대한 기능에 재인증이 없음. (Không yêu cầu xác thực lại khi làm việc quan trọng).
- **중요정보 평문 저장 및 전송 (Plaintext Storage/Transmission)**: 패스워드를 암호화 없이 저장/전송. (Lưu hoặc truyền mật khẩu không mã hóa).
- **하드코드된 비밀번호 (Hardcoded Password)**: 소스코드에 비밀번호를 직접 작성. (Ghi cứng mật khẩu trong source code).
- **오류 메시지 통한 정보 노출 (Information Exposure Through Error Message)**: 시스템 내부 구조나 파일 경로가 오류 메시지에 포함되어 노출됨. (Thông báo lỗi làm lộ đường dẫn nội mục hệ thống).
- **예시 (Example)**:
  - (KR) DB 연결 실패 시 "root 계정 연결 실패" 같은 메시지를 띄우지 않고 "일시적인 오류입니다"로 대체.
  - (VN) Thay vì hiện lỗi "Không kết nối được tài khoản root", chỉ hiển thị "Lỗi hệ thống tạm thời".

---

Điểm chốt của **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **9. 암호화 기술 (Công nghệ Mã hóa)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **9. 암호화 기술 (Công nghệ Mã hóa)** nối từ **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)** sang **암호화 기법 (Encryption Techniques)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. 암호화 기술 (Công nghệ Mã hóa)

Ở bước 34/86, **9. 암호화 기술 (Công nghệ Mã hóa)** xuất hiện như phần tiếp nối của **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **9. 암호화 기술 (Công nghệ Mã hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)

Bây giờ ta đi vào nội dung của **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개인키(대칭키) 암호화 (Private/Symmetric Key):**
  - **동일한 키**로 암호화/복호화. 속도가 빠름. 암호화 키 개수: n(n-1)/2.
  - 종류:
    - **블록 암호화:** DES, SEED, AES, ARIA, IDEA
    - **스트림 암호화:** LFSR, RC4
- **공개키(비대칭키) 암호화 (Public/Asymmetric Key):**
  - 암호화(공개키), 복호화(비밀키/개인키). 키 개수: **2n**.
  - 대표 알고리즘: **RSA** (소인수분해 기반).
- **Tiếng Việt:**
  - Khóa cá nhân (Đối xứng): Cùng 1 khóa, nhanh. (DES, AES, ARIA).
  - Khóa công khai (Bất đối xứng): 2 khóa (Public để mã hóa, Private để giải mã), an toàn nhưng chậm. (RSA).

Các bullet của **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **9.2 해시 및 기타 암호화 요소** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **9.2 해시 및 기타 암호화 요소**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 9.2 해시 및 기타 암호화 요소

Phần nguồn của **9.2 해시 및 기타 암호화 요소** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “9.2 해시 및 기타 암호화 요소” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **해시 (Hash):** 임의의 길이를 고정된 길이로 변환. 복호화가 불가한 **일방향 함수**. (종류: SHA, MD4, MD5 등).
- **솔트 (Salt):** 암호화 전 원문에 무작위 값을 덧붙이는 과정. (패스워드 보안 강화용).
- **Tiếng Việt:** Hash là hàm một chiều không thể giải mã (SHA, MD5). Salt là thêm chuỗi ngẫu nhiên trước khi mã hóa để chống tấn công từ điển.

Các bullet của **9.2 해시 및 기타 암호화 요소** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **9.2 해시 및 기타 암호화 요소** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **9. 암호화 기술 (Công nghệ Mã hóa)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **암호화 기법 (Encryption Techniques)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **암호화 기법 (Encryption Techniques)** nối từ **9. 암호화 기술 (Công nghệ Mã hóa)** sang **1. 암호화 기본 개념 (Concepts)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 암호화 기법 (Encryption Techniques)

Sau khi đã đặt nền bằng **9. 암호화 기술 (Công nghệ Mã hóa)**, ta chuyển sang **암호화 기법 (Encryption Techniques)**. Đây là mắt xích 35/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **암호화 기법 (Encryption Techniques)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **종류**, **종류**, **해시 (Hash)**, **솔트 (Salt)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)**. Hãy xác định **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)

Phần nguồn của **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 암호화와 복호화에 **동일한 키(비밀키)**를 사용합니다.
- 장점: 속도가 빠름 / 단점: 키 분배가 어렵고 키 개수가 많아짐.
- 필요한 키의 개수: `n(n-1) / 2`
- **종류**: DES, 3DES, AES, SEED(국내), ARIA(국내).

Các bullet của **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)

Các ý ngay dưới **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 암호화할 때는 공개키(Public Key), 복호화할 때는 비밀키(Private Key)를 사용합니다.
- 장점: 키 분배 용이, 키 개수 적음 / 단점: 암복호화 속도가 느림.
- 필요한 키의 개수: `2n`
- **종류**: RSA.

Các bullet của **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)**, đừng bắt đầu lại từ số không. **3. 해시(Hash)와 솔트(Salt)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. 해시(Hash)와 솔트(Salt)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. 해시(Hash)와 솔트(Salt)

Bây giờ ta đi vào nội dung của **3. 해시(Hash)와 솔트(Salt)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. 해시(Hash)와 솔트(Salt)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **해시 (Hash)**: 임의의 길이 데이터를 고정된 길이의 값으로 변환하는 일방향 함수다. 무결성 검증에 사용하며, 패스워드는 전용 password hashing/KDF와 salt를 사용해야 한다. 해시는 암호화처럼 복호화하지 않는다 (예: SHA-256, MD5).
- **솔트 (Salt)**: 암호화 전 원문에 덧붙이는 무작위 값. 동일한 패스워드라도 솔트가 다르면 해시값이 달라져 레인보우 테이블 공격을 방어합니다.

> **Vietnamese Explanation**:
> **Mã hóa đối xứng (Private Key)**: Dùng chung 1 chìa khóa để khóa và mở (nhanh nhưng khó chia sẻ chìa khóa an toàn).
> **Mã hóa bất đối xứng (Public Key)**: Dùng khóa công khai để khóa, khóa bí mật để mở (chậm hơn nhưng an toàn).
> **Hash (Băm)** là mã hóa 1 chiều (không dịch ngược được). **Salt (Muối)** là thêm chuỗi ngẫu nhiên vào mật khẩu trước khi băm để tăng độ khó.

Các bullet của **3. 해시(Hash)와 솔트(Salt)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 해시(Hash)와 솔트(Salt)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **암호화 기법 (Encryption Techniques)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 암호화 기본 개념 (Concepts)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **1. 암호화 기본 개념 (Concepts)** nối từ **암호화 기법 (Encryption Techniques)** sang **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1. 암호화 기본 개념 (Concepts)

Từ **암호화 기법 (Encryption Techniques)**, ta đã có điểm tựa để bước vào **1. 암호화 기본 개념 (Concepts)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 36/86 trước khi đi vào chi tiết.

Để đọc **1. 암호화 기본 개념 (Concepts)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **평문 (Plain)**, **암호문 (Cipher)**, **치환 암호 (Substitution Cipher)**, **전치 암호 (Transposition Cipher)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 암호화 기본 개념 (Concepts)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **평문 (Plain)**: Bản rõ (chưa mã hoá)
- **암호문 (Cipher)**: Bản mã (đã mã hoá)
- **치환 암호 (Substitution Cipher)**: 문자를 다른 문자로 대체 (Mã hoá thay thế, vd: A -> C).
- **전치 암호 (Transposition Cipher)**: 문자의 위치를 바꿈 (Mã hoá hoán vị, vd: ABC -> BCA).

Điểm chốt của **1. 암호화 기본 개념 (Concepts)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)** nối từ **1. 암호화 기본 개념 (Concepts)** sang **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)

Ở bước 37/86, **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)** xuất hiện như phần tiếp nối của **1. 암호화 기본 개념 (Concepts)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **2.1 소프트웨어 재사용 (Software Reuse)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **2.1 소프트웨어 재사용 (Software Reuse)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 2.1 소프트웨어 재사용 (Software Reuse)

Bây giờ ta đi vào nội dung của **2.1 소프트웨어 재사용 (Software Reuse)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2.1 소프트웨어 재사용 (Software Reuse)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **이점 (Benefits):** 개발 시간과 비용 단축, 품질 향상, 생산성 향상, 시스템 명세/설계/코드 등 문서 공유.
- **방법 (Methods):**
  - **합성 중심 (Composition-based):** 전자 칩 같은 소프트웨어 부품(모듈)을 만들어 끼워 맞추는 방법.
  - **생성 중심 (Generation-based):** 추상화 형태로 쓰여진 명세를 구체화하여 프로그램을 만드는 방법.
- **Tiếng Việt:** Tái sử dụng phần mềm giúp giảm thời gian/chi phí, tăng chất lượng.
  - Tổng hợp: lắp ráp các module (như chip).
  - Khởi tạo: tạo chương trình từ đặc tả trừu tượng.
- **Example:**
  - *KR:* 이전에 만든 로그인 모듈을 새 프로젝트에 그대로 재사용.
  - *VN:* Tái sử dụng nguyên bản module đăng nhập đã làm trước đó cho dự án mới.

Các ý về **2.1 소프트웨어 재사용 (Software Reuse)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **2.1 소프트웨어 재사용 (Software Reuse)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2.2 소프트웨어 재공학 (Software Reengineering)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2.2 소프트웨어 재공학 (Software Reengineering)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2.2 소프트웨어 재공학 (Software Reengineering)

Phần nguồn của **2.2 소프트웨어 재공학 (Software Reengineering)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2.2 소프트웨어 재공학 (Software Reengineering)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기존 소프트웨어의 데이터와 기능을 변경 및 개선하여 유지보수성과 품질을 높이는 기법.
- **이점 (Benefits):** 위험 부담 감소, 개발 시간/비용 단축, 시스템 명세 오류 억제.
- **주요 활동 (Activities):**
  - **분석 (Analysis):** 명세서 확인 및 재공학 대상 선정.
  - **재구성 (Restructuring):** 코드 재구성하여 구조 향상.
  - **역공학 (Reverse Engineering):** 기존 소프트웨어를 분석하여 설계 정보를 재발견하는 활동.
  - **이식 (Migration):** 다른 운영체제나 하드웨어 환경으로 변환.
- **Tiếng Việt:** Tái thiết kế phần mềm cũ để dễ bảo trì. Các hoạt động chính: Phân tích, Tái cấu trúc, Dịch ngược (Reverse Engineering), và Di chuyển (Migration).
- 💡 **Mẹo ghi nhớ:** Các bước Reengineering: "Phân Tích -> Tái Cấu Trúc -> Dịch Ngược -> Di Chuyển".

Các bullet của **2.2 소프트웨어 재공학 (Software Reengineering)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2.2 소프트웨어 재공학 (Software Reengineering)**, đừng bắt đầu lại từ số không. **2.3 CASE (Computer Aided Software Engineering)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **2.3 CASE (Computer Aided Software Engineering)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2.3 CASE (Computer Aided Software Engineering)

Các ý ngay dưới **2.3 CASE (Computer Aided Software Engineering)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2.3 CASE (Computer Aided Software Engineering)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소프트웨어 개발 과정 전체 또는 일부를 자동화하는 전용 도구.
- **원천 기술 (Core Technologies):** 구조적 기법, 프로토타이핑, 자동 프로그래밍, 정보 저장소, 분산처리.
- **주요 기능 (Major Functions):** 생명 주기 전 단계 연결, 다양한 모델 지원, 그래픽 지원, 자료 흐름도 작성, 모순 검사 등.
- **Tiếng Việt:** Công cụ tự động hóa toàn bộ hoặc một phần quá trình phát triển phần mềm. Hỗ trợ đồ họa, vẽ sơ đồ, kiểm tra lỗi.
- **Example:**
  - *KR:* UML 설계 도구를 사용하여 코드를 자동 생성.
  - *VN:* Sử dụng công cụ thiết kế UML để tự động sinh code.

Các ý về **2.3 CASE (Computer Aided Software Engineering)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Như vậy, **2.3 CASE (Computer Aided Software Engineering)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)** nối từ **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)** sang **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)

Sau khi đã đặt nền bằng **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)**, ta chuyển sang **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)**. Đây là mắt xích 38/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **6.1 최신 IT 기술 동향**. Hãy xác định **6.1 최신 IT 기술 동향** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 6.1 최신 IT 기술 동향

Phần nguồn của **6.1 최신 IT 기술 동향** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “6.1 최신 IT 기술 동향” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **도커 (Docker):** 컨테이너 기술을 자동화하여 쉽게 사용할 수 있게 하는 오픈소스 프로젝트.
- **매시업 (Mashup):** 웹에서 제공하는 정보/서비스를 융합하여 새로운 서비스를 만드는 기술.
- **디지털 트윈 (Digital Twin):** 현실 속 사물을 소프트웨어로 가상화한 모델.
- **서비스형 블록체인 (BaaS):** 블록체인 앱 개발 환경을 클라우드 기반으로 제공.
- **스크래피 (Scrapy):** Python 기반의 대규모 웹 크롤링 프레임워크.
- **텐서플로 (TensorFlow):** 구글의 기계학습/데이터 흐름 프로그래밍용 오픈소스 라이브러리.
- **앤 스크린 (N-Screen):** 여러(N개) 단말기에서 동일한 콘텐츠를 자유롭게 이용.
- **Tiếng Việt:**
  - Docker: Nền tảng container hóa mã nguồn mở.
  - Mashup: Kết hợp các API/dịch vụ web để tạo dịch vụ mới.
  - Digital Twin: Bản sao kỹ thuật số của thế giới thực.
  - N-Screen: Xem một nội dung trên nhiều thiết bị.

Các bullet của **6.1 최신 IT 기술 동향** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **6.1 최신 IT 기술 동향** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **6.2 데이터 분석 및 분산 처리** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **6.2 데이터 분석 및 분산 처리** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 6.2 데이터 분석 및 분산 처리

Các ý ngay dưới **6.2 데이터 분석 및 분산 처리** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “6.2 데이터 분석 및 분산 처리” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **하둡 (Hadoop):** 오픈소스 기반 분산 컴퓨팅 플랫폼. 대용량 데이터 전송에 **스쿱(Sqoop)** 사용.
- **맵리듀스 (MapReduce):** 대용량 데이터를 분산 처리하기 위한 프로그래밍 모델.
- **데이터 마이닝 (Data Mining):** 대량의 데이터에서 유용한 정보를 발견하는 기법.
- **OLAP (Online Analytical Processing):** 다차원 데이터에서 통계적 요약 정보를 분석하여 의사결정에 활용. (연산: Roll-up, Drill-down, Pivoting, Slicing, Dicing 등).
- **Tiếng Việt:**
  - Hadoop: Nền tảng điện toán phân tán (dùng Sqoop kết nối RDB).
  - MapReduce: Mô hình lập trình xử lý phân tán.
  - Data Mining: Khai phá dữ liệu.
  - OLAP: Xử lý phân tích đa chiều trực tuyến.

Các bullet của **6.2 데이터 분석 및 분산 처리** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **6.2 데이터 분석 및 분산 처리**, đừng bắt đầu lại từ số không. **6.3 시스템 아키텍처 및 프로그래밍 요소** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **6.3 시스템 아키텍처 및 프로그래밍 요소**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 6.3 시스템 아키텍처 및 프로그래밍 요소

Bây giờ ta đi vào nội dung của **6.3 시스템 아키텍처 및 프로그래밍 요소**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “6.3 시스템 아키텍처 및 프로그래밍 요소” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **SOA (Service Oriented Architecture) 기반 계층:** 표현(Presentation) → 업무 프로세스 → 서비스 중간 → 애플리케이션 → 데이터 저장.
- **접근 지정자 (Access Modifiers):** 외부로부터의 접근을 제한 (Public, Protected, Default, Private).
- **Tiếng Việt:** Kiến trúc hướng dịch vụ (SOA) và các chỉ định truy cập trong lập trình hướng đối tượng (OOP).

Các bullet của **6.3 시스템 아키텍처 및 프로그래밍 요소** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **6.3 시스템 아키텍처 및 프로그래밍 요소** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)** nối từ **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)** sang **핵심 257: 분기/제어 (break, continue)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. 보충 및 심화 내용 (Bổ sung & Nâng cao)

Từ **6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)**, ta đã có điểm tựa để bước vào **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 39/86 trước khi đi vào chi tiết.

Để đọc **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **11.1 소프트웨어 프레임워크 및 개발 심화** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 11.1 소프트웨어 프레임워크 및 개발 심화

Các ý ngay dưới **11.1 소프트웨어 프레임워크 및 개발 심화** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “11.1 소프트웨어 프레임워크 및 개발 심화” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **프레임워크의 특성 (Framework Characteristics):**
  - **모듈화 (Modularity):** 캡슐화를 통해 변경의 영향을 최소화하고 품질 향상.
  - **재사용성 (Reusability):** 재사용 가능한 모듈 제공 (생산성 향상).
  - **확장성 (Extensibility):** 다형성을 통한 인터페이스 확장.
  - **제어의 역흐름 (Inversion of Control):** 객체 제어 권한을 프레임워크에 넘김.
- **프레임워크 종류 (Framework Types):**
  - **스프링 (Spring):** 자바 플랫폼을 위한 경량형 오픈소스 프레임워크.
  - **전자정부 (e-Government):** 공공부문 정보화 사업을 지원하는 프레임워크.
  - **닷넷 (.NET):** 마이크로소프트의 Windows 개발 및 실행 환경.
- **Tiếng Việt:** Đặc điểm của Framework: Mô-đun hóa, Tái sử dụng, Khả năng mở rộng, và Đảo ngược quyền điều khiển (IoC - Inversion of Control). Các loại: Spring (Java), e-Government (Hàn Quốc), .NET (Microsoft).

Các bullet của **11.1 소프트웨어 프레임워크 및 개발 심화** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **11.1 소프트웨어 프레임워크 및 개발 심화** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **11.2 네트워크 구조 및 표준 심화** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **11.2 네트워크 구조 및 표준 심화**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 11.2 네트워크 구조 및 표준 심화

Bây giờ ta đi vào nội dung của **11.2 네트워크 구조 및 표준 심화**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “11.2 네트워크 구조 및 표준 심화” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **네트워크 토폴로지 (Network Topology):**
  - **성형 (Star):** 중앙 컴퓨터를 중심으로 연결 (포인트 투 포인트).
  - **링형 (Ring):** 이웃하는 단말끼리 원형으로 연결.
  - **버스형 (Bus):** 하나의 통신 회선에 여러 단말 연결 (신뢰성 높음).
  - **망형 (Mesh):** 모든 지점을 서로 연결. 회선 수 = `n(n-1)/2`.
- **IEEE 802 표준 규격:**
  - `802.3`: CSMA/CD (유선 LAN)
  - `802.11`: 무선 LAN (WLAN)
    - `802.11a/g`: 54Mbps
    - `802.11i`: 보안 표준 (WPA/WPA2)
    - `802.11n`: 2.4GHz/5GHz 듀얼 대역, 최고 600Mbps
- **경로 제어 프로토콜 (Routing Protocols):**
  - **IGP (내부):** AS 내부 라우팅 (RIP, OSPF)
  - **EGP (외부):** AS 간의 라우팅
  - **BGP (Border Gateway Protocol):** EGP 단점 보완. 변화된 정보만 교환.
- **흐름 제어 (Flow Control):**
  - **정지-대기 (Stop-and-Wait):** ACK를 받은 후 다음 패킷 전송.
  - **슬라이딩 윈도우 (Sliding Window):** ACK 없이도 미리 정해진 윈도우 크기(Window Size)만큼 연속 전송.
- **Tiếng Việt:**
  - Topology mạng: Star, Ring, Bus, Mesh (Số đường truyền = n(n-1)/2).
  - IEEE 802.11: Tiêu chuẩn mạng không dây (Wi-Fi).
  - Flow Control: Sliding Window truyền liên tục dựa vào kích thước cửa sổ mà không cần chờ ACK cho từng gói.

Với **11.2 네트워크 구조 및 표준 심화**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **11.2 네트워크 구조 및 표준 심화**, đừng bắt đầu lại từ số không. **11.3 데이터베이스 동시성 및 교착상태 심화** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **11.3 데이터베이스 동시성 및 교착상태 심화**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 11.3 데이터베이스 동시성 및 교착상태 심화

Phần nguồn của **11.3 데이터베이스 동시성 및 교착상태 심화** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “11.3 데이터베이스 동시성 및 교착상태 심화” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **교착상태 해결 방법 (Deadlock Handling):**
  - **예방 (Prevention):** 발생 4조건(상호배제, 점유대기, 비선점, 환형대기) 중 하나를 부정 (자원 낭비 심함).
  - **회피 (Avoidance):** 가능성을 피함 (**은행원 알고리즘**).
  - **발견 (Detection):** 교착상태가 발생했는지 점검.
  - **회복 (Recovery):** 프로세스 종료 또는 자원 선점.
- **회복 기법 (Recovery):**
  - **연기 갱신 기법 (Deferred Update):** 트랜잭션 부분 완료 전까지 실제 DB 반영을 연기하고 Log에 기록 (Redo만 가능).
  - **즉각 갱신 기법 (Immediate Update):** 즉시 반영. 장애 시 Undo, Redo 모두 사용 가능.
  - **그림자 페이지 대체 기법 (Shadow Paging):** 그림자 페이지 보관 (Log, Undo, Redo 불필요).
  - **검사점 기법 (Check Point):** 검사점부터 회복하여 시간 절약.
- **Tiếng Việt:** Xử lý Deadlock: Phòng ngừa (Prevention) -> Tránh (Avoidance - Thuật toán Banker) -> Phát hiện (Detection) -> Phục hồi (Recovery). Phục hồi DB bằng Log, Shadow Paging, Check Point.

Các bullet của **11.3 데이터베이스 동시성 및 교착상태 심화** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**11.3 데이터베이스 동시성 및 교착상태 심화** vừa cho ta cách đặt câu hỏi. Bây giờ **11.4 암호화 및 해시 알고리즘 심화** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **11.4 암호화 및 해시 알고리즘 심화** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 11.4 암호화 및 해시 알고리즘 심화

Các ý ngay dưới **11.4 암호화 및 해시 알고리즘 심화** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “11.4 암호화 및 해시 알고리즘 심화” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **암호화 키 개수 (Key Count):**
  - **개인키(대칭키):** `n(n-1)/2` 개
  - **공개키(비대칭키):** `2n` 개
- **블록 암호화 알고리즘 (Block Ciphers):**
  - **SEED:** 한국인터넷진흥원(KISA) 개발 (128/256bit).
  - **ARIA:** 국가정보원 및 산학연 협회 개발 (128/192/256bit).
  - **DES:** 미국 NBS 발표, 64bit 블록 / 56bit 키 (3DES로 강화됨).
  - **AES:** DES 한계 극복, NIST 발표 (128/192/256bit).
- **해시 함수 종류 (Hash Functions):**
  - **SHA 시리즈:** 미국 NSA 설계, NIST 발표.
  - **MD5:** R. Rivest 고안 (128bit 키).
  - **N-NASH, SNEFRU.**
- **Tiếng Việt:** Thuật toán mã hóa Hàn Quốc: SEED, ARIA. Thuật toán quốc tế: DES, AES, RSA. Số lượng khóa đối xứng = n(n-1)/2. Số lượng khóa bất đối xứng = 2n.

Với **11.4 암호화 및 해시 알고리즘 심화**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **11.4 암호화 및 해시 알고리즘 심화** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **11.5 기타 보안 및 공격 기법 심화** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **11.5 기타 보안 및 공격 기법 심화**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 11.5 기타 보안 및 공격 기법 심화

Bây giờ ta đi vào nội dung của **11.5 기타 보안 및 공격 기법 심화**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “11.5 기타 보안 및 공격 기법 심화” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Secure SDLC 방법론:**
  - **CLASP:** 활동 중심, 역할 기반 (초기 단계 보안 강화).
  - **MS SDL:** 마이크로소프트의 나선형 모델 기반 방법론.
  - **Seven Touchpoints:** 모범사례를 SDLC에 통합 (위험 분석 및 테스트).
- **추가 웹 보안 약점 (Additional Web Vulnerabilities):**
  - **운영체제 명령어 삽입:** 외부 입력으로 시스템 명령어 실행 유도.
  - **위험한 파일 업로드:** 스크립트 파일 업로드로 시스템 제어.
  - **신뢰되지 않는 URL 주소로 자동접속 연결 (Open Redirect):** 피싱 사이트로 유도.
- **분산 서비스 공격용 툴 (DDoS Tools):**
  - **Trin00:** UDP Flooding 주도.
  - **TFN / TFN2K:** UDP/TCP SYN, 스머핑 동시 수행.
  - **Stacheldraht:** 암호화된 통신 수행 및 자동 업데이트.
- **새로운 공격 기법 (New Attack Vectors):**
  - **제로 데이 공격 (Zero Day Attack):** 보안 취약점이 공표되기도 전에 이루어지는 신속한 공격.
  - **스미싱 (Smishing):** SMS를 이용한 개인정보 탈취.
  - **Evil Twin Attack:** 실제와 동일한 이름의 가짜 Wi-Fi(AP)를 송출해 정보 탈취.
- **Tiếng Việt:**
  - Zero Day Attack: Tấn công khai thác lỗ hổng trước khi có bản vá.
  - Smishing: Phishing qua tin nhắn SMS.
  - Evil Twin: Tấn công bằng trạm Wi-Fi giả mạo tên (SSID) giống hệt trạm thật.
  - DDoS Tools: Trin00, TFN, Stacheldraht (ẩn danh và mã hóa liên lạc).

Các bullet của **11.5 기타 보안 및 공격 기법 심화** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **11.5 기타 보안 및 공격 기법 심화** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **핵심 257: 분기/제어 (break, continue)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **핵심 257: 분기/제어 (break, continue)** nối từ **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)** sang **핵심 258, 259, 260: 배열 (Array)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 257: 분기/제어 (break, continue)

Ở bước 40/86, **핵심 257: 분기/제어 (break, continue)** xuất hiện như phần tiếp nối của **11. 보충 및 심화 내용 (Bổ sung & Nâng cao)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **핵심 257: 분기/제어 (break, continue)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **break**, **continue** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 257: 분기/제어 (break, continue)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **break**: 자신이 속한 가장 가까운 반복문이나 switch문을 탈출. (Thoát khỏi vòng lặp hoặc switch).
- **continue**: 현재 반복의 나머지 부분을 건너뛰고, 다음 반복(조건식이나 증감식)으로 넘어감. 반복문에서만 사용 가능. (Bỏ qua phần còn lại của lần lặp này, chuyển sang lần lặp tiếp theo).

Như vậy, **핵심 257: 분기/제어 (break, continue)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 258, 259, 260: 배열 (Array)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **핵심 258, 259, 260: 배열 (Array)** nối từ **핵심 257: 분기/제어 (break, continue)** sang **핵심 261: C언어의 문자열 배열**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 258, 259, 260: 배열 (Array)

Sau khi đã đặt nền bằng **핵심 257: 분기/제어 (break, continue)**, ta chuyển sang **핵심 258, 259, 260: 배열 (Array)**. Đây là mắt xích 41/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 258, 259, 260: 배열 (Array)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **특징**, **초기화** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 258, 259, 260: 배열 (Array)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 동일한 자료형의 여러 변수를 연속된 메모리 공간에 묶어서 하나의 이름으로 관리. (Mảng: Tập hợp các biến cùng kiểu).
- **특징**:
  - C언어에서 인덱스(첨자)는 **0부터 시작**. (Chỉ số bắt đầu từ 0).
  - 1차원 배열: `int a[5];` (Mảng 1 chiều).
  - 2차원 배열: `int a[3][4];` (행(Row)과 열(Column)로 구성 / Mảng 2 chiều: Dòng và Cột).
- **초기화**:
  - `int a[3] = {1, 2, 3};`
  - 지정한 요소 개수보다 초기값이 적으면 나머지는 **0으로 채워짐**. (Nếu khai báo thiếu giá trị, các phần tử còn lại tự động bằng 0).

Ta có thể khép mục **핵심 258, 259, 260: 배열 (Array)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 261: C언어의 문자열 배열**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **핵심 261: C언어의 문자열 배열** nối từ **핵심 258, 259, 260: 배열 (Array)** sang **핵심 262: 포인터와 포인터 변수 (Pointer)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 261: C언어의 문자열 배열

Từ **핵심 258, 259, 260: 배열 (Array)**, ta đã có điểm tựa để bước vào **핵심 261: C언어의 문자열 배열**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 42/86 trước khi đi vào chi tiết.

Để đọc **핵심 261: C언어의 문자열 배열** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 261: C언어의 문자열 배열” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- C언어에는 문자열 전용 자료형(String)이 없어, `char` 배열이나 포인터를 사용. (C không có kiểu String, dùng mảng char).
- 배열 초기화 시 문자열을 큰따옴표로 묶어 할당하면, 끝에 **자동으로 널 문자(` `)가 삽입**됨. 따라서 크기 지정 시 글자 수 + 1 이상이어야 함. (Cuối chuỗi luôn tự động thêm ký tự NULL ` `).
  - 예: `char a[5] = "love";` ('l', 'o', 'v', 'e', ' ').

Điểm chốt của **핵심 261: C언어의 문자열 배열** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **핵심 262: 포인터와 포인터 변수 (Pointer)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **핵심 262: 포인터와 포인터 변수 (Pointer)** nối từ **핵심 261: C언어의 문자열 배열** sang **포인터와 배열 (Pointer and Array)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 262: 포인터와 포인터 변수 (Pointer)

Ở bước 43/86, **핵심 262: 포인터와 포인터 변수 (Pointer)** xuất hiện như phần tiếp nối của **핵심 261: C언어의 문자열 배열**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **핵심 262: 포인터와 포인터 변수 (Pointer)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **기호**, **Example (KR/VN)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 262: 포인터와 포인터 변수 (Pointer)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 변수의 **메모리 주소**를 저장하는 변수. 동적 메모리(Heap) 접근 시 활용. (Con trỏ: Biến lưu trữ địa chỉ bộ nhớ).
- **기호**:
  - `*`: 포인터 선언 시 사용 (예: `int *p;`). 또는 포인터가 가리키는 주소의 **값(Value)**을 참조할 때 사용 (`*p = 10;`). (Dùng để khai báo con trỏ, hoặc lấy giá trị tại địa chỉ đó).
  - `&`: 특정 변수의 **주소(Address)**를 가져올 때 사용. (Dùng để lấy địa chỉ của biến).
- **Example (KR/VN)**:
  - `int a = 50;` (변수 a 생성 및 50 저장 / Tạo biến a, gán 50).
  - `int *p = &a;` (포인터 p에 a의 주소 저장 / Con trỏ p lưu địa chỉ của a).
  - `*p = 70;` (p가 가리키는 곳(a)의 값을 70으로 변경 / Đổi giá trị tại địa chỉ p trỏ đến thành 70. Lúc này a = 70).
- 💡 **Mẹo ghi nhớ**: `&`(And)는 주소(Address), `*`(Star)는 값(Value)을 가리킨다고 기억하세요.

Như vậy, **핵심 262: 포인터와 포인터 변수 (Pointer)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **포인터와 배열 (Pointer and Array)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **포인터와 배열 (Pointer and Array)** nối từ **핵심 262: 포인터와 포인터 변수 (Pointer)** sang **Python의 기본 문법 (Python Basic Syntax)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 포인터와 배열 (Pointer and Array)

Sau khi đã đặt nền bằng **핵심 262: 포인터와 포인터 변수 (Pointer)**, ta chuyển sang **포인터와 배열 (Pointer and Array)**. Đây là mắt xích 44/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **포인터와 배열 (Pointer and Array)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **특징** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “포인터와 배열 (Pointer and Array)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: C언어에서 배열을 포인터(Pointer/Con trỏ) 변수에 저장한 후 포인터를 이용해 배열의 요소에 접근할 수 있습니다.
- **특징**:
  - 배열 위치를 나타내는 첨자를 생략하고 배열의 대표명만 지정하면 배열의 첫 번째 요소의 주소를 지정하는 것과 같습니다. (예: `b = a;` 는 `b = &a[0];` 와 동일)
  - 배열 요소에 대한 주소를 지정할 때는 일반 변수와 동일하게 `&` 연산자를 사용합니다.
  - 배열의 요소가 포인터인 포인터형 배열을 선언할 수 있습니다.
  - 포인터 값에 정수를 더하면, 포인터가 가리키는 자료형의 크기(예: 정수형은 4바이트)만큼 물리적 주소가 증가합니다. (예: `p+1`은 4바이트 뒤의 주소)

> **Vietnamese Explanation**:
> Trong C, tên của mảng (array) chính là con trỏ (pointer) trỏ đến phần tử đầu tiên của mảng đó. Bạn có thể gán mảng cho một biến con trỏ, từ đó dùng con trỏ để truy cập các phần tử thay vì dùng chỉ số (index). Khi cộng 1 vào con trỏ, địa chỉ bộ nhớ sẽ tăng thêm số byte tương ứng với kiểu dữ liệu của nó (ví dụ int tăng 4 byte).

**예시 / Ví dụ:**
```c
int a[5] = {10, 11, 12, 13, 14};
int *p = a; // p trỏ tới a[0]
printf("%d", *(p+1)); // 출력/Output: 11
```

💡 **Mẹo ghi nhớ (Mnemonics):**
**Tên mảng = Địa chỉ đầu**. Mảng không cần `&` khi trỏ vào, nhưng phần tử thì cần (ví dụ `&a[0]`).

Ta có thể khép mục **포인터와 배열 (Pointer and Array)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **Python의 기본 문법 (Python Basic Syntax)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **Python의 기본 문법 (Python Basic Syntax)** nối từ **포인터와 배열 (Pointer and Array)** sang **Python 데이터 입·출력 함수 (Python Input/Output Functions)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Python의 기본 문법 (Python Basic Syntax)

Từ **포인터와 배열 (Pointer and Array)**, ta đã có điểm tựa để bước vào **Python의 기본 문법 (Python Basic Syntax)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 45/86 trước khi đi vào chi tiết.

Để đọc **Python의 기본 문법 (Python Basic Syntax)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “Python의 기본 문법 (Python Basic Syntax)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **특징**:
  - 변수의 자료형(Data Type/Kiểu dữ liệu)에 대한 선언이 없습니다.
  - 문장의 끝을 의미하는 세미콜론(`;`)을 사용할 필요가 없습니다.
  - 변수에 연속하여 값을 저장하는 것이 가능합니다. (예: `x, y, z = 10, 20, 30`)
  - `if`나 `for`와 같이 코드 블록(Code Block/Khối lệnh)을 포함하는 명령문을 작성할 때, 콜론(`:`)과 여백(Indentation/Thụt lề)으로 구분합니다.
  - 여백은 일반적으로 4칸 또는 한 개의 탭(Tab)만큼 띄워야 하며, 같은 수준의 코드들은 반드시 동일한 여백을 가져야 합니다.

> **Vietnamese Explanation**:
> Khác với C hay Java, Python không cần khai báo kiểu dữ liệu cho biến, không cần dấu chấm phẩy `;` ở cuối dòng. Python dùng khoảng trắng (thụt lề) để phân chia các khối lệnh thay vì dùng dấu ngoặc nhọn `{}`.

**예시 / Ví dụ:**
```python
x, y = 10, 20
if x < y:
    print("x is smaller") # Thụt lề 4 khoảng trắng
```

💡 **Mẹo ghi nhớ (Mnemonics):**
**P.I.T** - **P**ython **I**ndents **T**hings (Python thụt lề mọi thứ).

Điểm chốt của **Python의 기본 문법 (Python Basic Syntax)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **Python 데이터 입·출력 함수 (Python Input/Output Functions)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **Python 데이터 입·출력 함수 (Python Input/Output Functions)** nối từ **Python의 기본 문법 (Python Basic Syntax)** sang **입력 값의 형변환 (Type Casting)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Python 데이터 입·출력 함수 (Python Input/Output Functions)

Ở bước 46/86, **Python 데이터 입·출력 함수 (Python Input/Output Functions)** xuất hiện như phần tiếp nối của **Python의 기본 문법 (Python Basic Syntax)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **Python 데이터 입·출력 함수 (Python Input/Output Functions)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **형식**, **형식** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. input( ) 함수** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. input( ) 함수** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. input( ) 함수

Bây giờ ta đi vào nội dung của **1. input( ) 함수**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. input( ) 함수” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Python의 표준 입력 함수로, 키보드로 입력받아 변수에 문자열(String) 형태로 저장합니다.
- **형식**: `변수 = input('출력문자')`

Với **1. input( ) 함수**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. input( ) 함수** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. print( ) 함수** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. print( ) 함수**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. print( ) 함수

Phần nguồn của **2. print( ) 함수** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. print( ) 함수” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식**: `print(출력값1, 출력값2, ..., sep='분리문자', end='종료문자')`
  - `sep`: 여러 값을 출력할 때 값 사이를 구분하는 문자 (기본값: 공백 한 칸)
  - `end`: 맨 마지막에 표시할 문자 (기본값: 줄 바꿈 `\n`)

> **Vietnamese Explanation**:
> Hàm `input()` dùng để nhận dữ liệu nhập từ bàn phím (mặc định luôn là chuỗi string). Hàm `print()` dùng để in ra màn hình, có thể tùy chỉnh dấu ngăn cách giữa các giá trị `sep` và ký tự kết thúc `end`.

**예시 / Ví dụ:**
```python
print(82, 24, sep='-', end=',')
# 출력/Output: 82-24,
```

Các ý về **2. print( ) 함수** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **2. print( ) 함수** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **Python 데이터 입·출력 함수 (Python Input/Output Functions)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **입력 값의 형변환 (Type Casting)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **입력 값의 형변환 (Type Casting)** nối từ **Python 데이터 입·출력 함수 (Python Input/Output Functions)** sang **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 입력 값의 형변환 (Type Casting)

Sau khi đã đặt nền bằng **Python 데이터 입·출력 함수 (Python Input/Output Functions)**, ta chuyển sang **입력 값의 형변환 (Type Casting)**. Đây là mắt xích 47/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **입력 값의 형변환 (Type Casting)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **변환할 데이터가 1개일 때**, **변환할 데이터가 2개 이상일 때** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “입력 값의 형변환 (Type Casting)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `input()` 함수는 입력되는 값을 무조건 문자열(String)로 저장하므로, 숫자로 사용하기 위해서는 형(Type)을 변환해야 합니다.
- **변환할 데이터가 1개일 때**: `int()`, `float()` 사용
- **변환할 데이터가 2개 이상일 때**: `map()`과 `split()` 사용
  - 형식: `변수1, 변수2 = map(int, input().split())`

> **Vietnamese Explanation**:
> Vì `input()` trả về chuỗi, bạn phải ép kiểu sang số thực (`float`) hoặc số nguyên (`int`). Để nhập nhiều số cùng lúc trên một dòng, dùng `split()` để tách chuỗi và `map()` để ép kiểu hàng loạt cho tất cả các phần tử.

**예시 / Ví dụ:**
```python
a, b = map(int, input("Nhập 2 số: ").split())
# Nếu nhập "10 20", a=10, b=20
```

💡 **Mẹo ghi nhớ (Mnemonics):**
**M.I.S** - **M**ap **I**nt **S**plit để nhập nhiều số nguyên cùng lúc.

Ta có thể khép mục **입력 값의 형변환 (Type Casting)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)** nối từ **입력 값의 형변환 (Type Casting)** sang **슬라이스 (Slice)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)

Từ **입력 값의 형변환 (Type Casting)**, ta đã có điểm tựa để bước vào **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/86 trước khi đi vào chi tiết.

Để đọc **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **형식**, **형식**, **List**, **Dict** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 리스트 (List / Danh sách)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 리스트 (List / Danh sách)

Các ý ngay dưới **1. 리스트 (List / Danh sách)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “1. 리스트 (List / Danh sách)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- C/Java의 배열(Array)과 달리 크기를 지정하지 않으며, 정수/실수/문자열 등 다양한 자료형을 섞어서 저장할 수 있습니다.
- 위치(Index)는 0부터 시작합니다.
- **형식**: `리스트명 = [값1, 값2, ...]` 또는 `list([값1, 값2, ...])`

Với **1. 리스트 (List / Danh sách)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. 리스트 (List / Danh sách)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 딕셔너리 (Dictionary / Từ điển)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. 딕셔너리 (Dictionary / Từ điển)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. 딕셔너리 (Dictionary / Từ điển)

Bây giờ ta đi vào nội dung của **2. 딕셔너리 (Dictionary / Từ điển)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. 딕셔너리 (Dictionary / Từ điển)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 연관된 값을 묶어서 저장하는 용도로, 인덱스 대신 사용자가 원하는 값을 키(Key)로 지정해 사용합니다. 키-값 쌍(Key-Value pairs) 형태로 저장합니다.
- **형식**: `딕셔너리명 = {키1:값1, 키2:값2, ...}` 또는 `dict(...)`

> **Vietnamese Explanation**:
> List giống như Array nhưng linh hoạt hơn nhiều (có thể chứa nhiều kiểu dữ liệu cùng lúc, tự động thay đổi kích thước). Dictionary lưu dữ liệu theo dạng Cặp Chìa khóa - Giá trị (Key-Value), cho phép tra cứu nhanh theo Key.

**예시 / Ví dụ:**
```python
# List
my_list = [10, "mike", 23.45]
# Dictionary
my_dict = {"이름": "홍길동", "나이": 25}
my_dict["주소"] = "서울" # Thêm phần tử
```

💡 **Mẹo ghi nhớ (Mnemonics):**
- **List**: Ngoặc vuông `[]` (Ví dụ: cái hộp hình vuông chứa đủ đồ).
- **Dict**: Ngoặc nhọn `{}` (Có dạng `Key: Value`).

Với **2. 딕셔너리 (Dictionary / Từ điển)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **2. 딕셔너리 (Dictionary / Từ điển)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **슬라이스 (Slice)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **슬라이스 (Slice)** nối từ **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)** sang **Python 제어문 (Control Statements): if문, for문**, vì cơ chế trước tạo đầu vào cho bước sau.

## 슬라이스 (Slice)

Ở bước 49/86, **슬라이스 (Slice)** xuất hiện như phần tiếp nối của **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **슬라이스 (Slice)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **형식** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “슬라이스 (Slice)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 문자열이나 리스트와 같은 순차형 객체에서 일부를 잘라(Slicing) 반환하는 기능입니다.
- **형식**: `객체명[초기위치:최종위치:증가값]`
  - `초기위치`에서 `최종위치 - 1` 까지의 요소들을 가져옵니다.
  - 인수를 생략하면 전체를 의미하거나, 기본값(처음, 끝, 1씩 증가)이 적용됩니다.

> **Vietnamese Explanation**:
> Slice (cắt lát) giúp lấy ra một phần của List hoặc String một cách dễ dàng. Nhớ là vị trí kết thúc không bao giờ được bao gồm (chỉ lấy đến `cuối - 1`).

**예시 / Ví dụ:**
```python
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:3])    # ['b', 'c']
print(a[0:5:2])  # ['a', 'c', 'e'] (Lấy cách nhau 2 bước)
print(a[::-1])   # Lật ngược list (âm là đi lùi)
```

Như vậy, **슬라이스 (Slice)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **Python 제어문 (Control Statements): if문, for문**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **Python 제어문 (Control Statements): if문, for문** nối từ **슬라이스 (Slice)** sang **Python 클래스 (Class) - 기초 (Cơ bản)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Python 제어문 (Control Statements): if문, for문

Sau khi đã đặt nền bằng **슬라이스 (Slice)**, ta chuyển sang **Python 제어문 (Control Statements): if문, for문**. Đây là mắt xích 50/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **Python 제어문 (Control Statements): if문, for문** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **형식**, **형식 1 (range 이용)**, **형식 2 (리스트 이용)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. if문 (if Statement / Câu lệnh điều kiện)**. Hãy xác định **1. if문 (if Statement / Câu lệnh điều kiện)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. if문 (if Statement / Câu lệnh điều kiện)

Phần nguồn của **1. if문 (if Statement / Câu lệnh điều kiện)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. if문 (if Statement / Câu lệnh điều kiện)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식**:
  ```python
  if 조건:
      실행할 문장
  ```
- 조건 뒤에 콜론(`:`)을 붙이고, 실행할 문장은 반드시 여백(Indentation)을 주어야 합니다.

Các bullet của **1. if문 (if Statement / Câu lệnh điều kiện)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. if문 (if Statement / Câu lệnh điều kiện)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. for문 (for Statement / Vòng lặp for)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. for문 (for Statement / Vòng lặp for)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. for문 (for Statement / Vòng lặp for)

Các ý ngay dưới **2. for문 (for Statement / Vòng lặp for)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2. for문 (for Statement / Vòng lặp for)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식 1 (range 이용)**:
  ```python
  for 변수 in range(초기값, 최종값, 증가값):
      실행할 문장
  ```
  - `최종값` - 1 까지 반복합니다.
- **형식 2 (리스트 이용)**:
  ```python
  for 변수 in 리스트:
      실행할 문장
  ```

> **Vietnamese Explanation**:
> `if` dùng để rẽ nhánh điều kiện. `for` dùng để lặp. Hàm `range(start, end, step)` sinh ra một dãy số từ `start` tới `end-1` với khoảng cách là `step`.

**예시 / Ví dụ:**
```python
# Tính tổng các số từ 1 đến 4
sum = 0
for i in range(1, 5):
    sum += i
print(sum) # Output: 10 (1+2+3+4)
```

Với **2. for문 (for Statement / Vòng lặp for)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **2. for문 (for Statement / Vòng lặp for)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **Python 제어문 (Control Statements): if문, for문** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **Python 클래스 (Class) - 기초 (Cơ bản)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **Python 클래스 (Class) - 기초 (Cơ bản)** nối từ **Python 제어문 (Control Statements): if문, for문** sang **Python 클래스와 함수 (Class and Functions)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Python 클래스 (Class) - 기초 (Cơ bản)

Từ **Python 제어문 (Control Statements): if문, for문**, ta đã có điểm tựa để bước vào **Python 클래스 (Class) - 기초 (Cơ bản)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/86 trước khi đi vào chi tiết.

Để đọc **Python 클래스 (Class) - 기초 (Cơ bản)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “Python 클래스 (Class) - 기초 (Cơ bản)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **정의 형식**:
  ```python
  class 클래스명:
      def 메소드명(self, 인수):
          실행할 문장
          return 값
  ```
- `def`는 메소드(Method/Phương thức)를 정의하는 예약어입니다.
- `self`는 메소드에서 자기 클래스에 속한 변수에 접근할 때 사용하는 명칭으로 첫 번째 인수로 반드시 작성합니다.

> **Vietnamese Explanation**:
> Class là khuôn mẫu để tạo ra các đối tượng (Objects). Hàm định nghĩa bên trong class được gọi là method (phương thức) và luôn phải có tham số `self` đại diện cho chính đối tượng đó.

Điểm chốt của **Python 클래스 (Class) - 기초 (Cơ bản)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **Python 클래스와 함수 (Class and Functions)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **Python 클래스와 함수 (Class and Functions)** nối từ **Python 클래스 (Class) - 기초 (Cơ bản)** sang **Python 제어문: while문 (While Loop)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Python 클래스와 함수 (Class and Functions)

Ở bước 52/86, **Python 클래스와 함수 (Class and Functions)** xuất hiện như phần tiếp nối của **Python 클래스 (Class) - 기초 (Cơ bản)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **Python 클래스와 함수 (Class and Functions)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **클래스 기반 객체 생성**, **함수 (클래스 없는 메소드)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 객체 생성 및 메소드 (Objects and Methods)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 객체 생성 및 메소드 (Objects and Methods)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 객체 생성 및 메소드 (Objects and Methods)

Bây giờ ta đi vào nội dung của **1. 객체 생성 및 메소드 (Objects and Methods)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. 객체 생성 및 메소드 (Objects and Methods)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **클래스 기반 객체 생성**: `변수명 = 클래스명()`
  - 예: `a = Cls()` (Cls 클래스의 객체 a를 생성)
  - 객체의 속성(변수)이나 메소드(함수)에 접근할 때는 마침표(`.`)를 사용합니다. (예: `a.x`, `a.chg()`)
- **함수 (클래스 없는 메소드)**: C언어의 함수처럼 클래스 없이 독립적으로 `def`를 이용해 메소드를 선언하고 사용할 수 있습니다.

> **Vietnamese Explanation**:
> Bạn có thể tạo đối tượng (object) từ một class bằng cú pháp `tên_biến = TênClass()`. Để truy cập biến hay hàm bên trong, ta dùng dấu chấm `.`. Ngoài ra, Python cũng cho phép định nghĩa các hàm độc lập không cần nằm trong class bằng từ khóa `def`.

**예시 / Ví dụ:**
```python
# Hàm độc lập (Function)
def calc(x, y):
    return x * y

a = calc(3, 4) # a = 12
```

Với **1. 객체 생성 및 메소드 (Objects and Methods)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **1. 객체 생성 및 메소드 (Objects and Methods)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **Python 클래스와 함수 (Class and Functions)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **Python 제어문: while문 (While Loop)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **Python 제어문: while문 (While Loop)** nối từ **Python 클래스와 함수 (Class and Functions)** sang **프로그래밍 언어의 분류 (Classification of Programming Languages)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Python 제어문: while문 (While Loop)

Sau khi đã đặt nền bằng **Python 클래스와 함수 (Class and Functions)**, ta chuyển sang **Python 제어문: while문 (While Loop)**. Đây là mắt xích 53/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **Python 제어문: while문 (While Loop)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “Python 제어문: while문 (While Loop)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식**:
  ```python
  while 조건:
      실행할 문장
  ```
- 조건이 참(True)인 동안 실행할 문장을 반복 수행합니다.

**예시 / Ví dụ:**
```python
i = 0
while i < 5:
    i += 1
```

Ta có thể khép mục **Python 제어문: while문 (While Loop)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **프로그래밍 언어의 분류 (Classification of Programming Languages)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **프로그래밍 언어의 분류 (Classification of Programming Languages)** nối từ **Python 제어문: while문 (While Loop)** sang **라이브러리 및 예외 처리 (Libraries and Exception Handling)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 프로그래밍 언어의 분류 (Classification of Programming Languages)

Từ **Python 제어문: while문 (While Loop)**, ta đã có điểm tựa để bước vào **프로그래밍 언어의 분류 (Classification of Programming Languages)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/86 trước khi đi vào chi tiết.

Để đọc **프로그래밍 언어의 분류 (Classification of Programming Languages)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **C**, **ALGOL**, **COBOL**, **FORTRAN** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 절차적 프로그래밍 언어 (Procedural)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 절차적 프로그래밍 언어 (Procedural)

Các ý ngay dưới **1. 절차적 프로그래밍 언어 (Procedural)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “1. 절차적 프로그래밍 언어 (Procedural)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **C**: UNIX의 일부를 구현한 언어. 시스템 프로그래밍에 적합하며 포인터(Pointer) 제공.
- **ALGOL**: 과학 기술 계산용. PASCAL과 C의 모체.
- **COBOL**: 사무 처리용. 영어 문장 형식 (4개의 DIVISION).
- **FORTRAN**: 수학과 공학 등 과학 기술 계산용.

Các bullet của **1. 절차적 프로그래밍 언어 (Procedural)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 절차적 프로그래밍 언어 (Procedural)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 객체지향 프로그래밍 언어 (Object-Oriented)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. 객체지향 프로그래밍 언어 (Object-Oriented)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. 객체지향 프로그래밍 언어 (Object-Oriented)

Bây giờ ta đi vào nội dung của **2. 객체지향 프로그래밍 언어 (Object-Oriented)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. 객체지향 프로그래밍 언어 (Object-Oriented)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **JAVA**: 분산 네트워크 환경 적합, 멀티스레드(Multi-thread) 지원, 이식성 강함.
- **C++**: C언어에 객체지향 개념을 추가.
- **Smalltalk**: 1세대 순수 객체지향 언어로, 최초로 GUI를 제공.

Các bullet của **2. 객체지향 프로그래밍 언어 (Object-Oriented)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 객체지향 프로그래밍 언어 (Object-Oriented)**, đừng bắt đầu lại từ số không. **3. 스크립트 언어 (Scripting)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3. 스크립트 언어 (Scripting)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3. 스크립트 언어 (Scripting)

Phần nguồn của **3. 스크립트 언어 (Scripting)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3. 스크립트 언어 (Scripting)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **클라이언트 측 (Client-side)**:
  - **JavaScript**: 웹 페이지 동작 제어.
  - **VBScript**: Microsoft 애플리케이션 제어 (Active X).
- **서버 측 (Server-side)**:
  - **ASP**: Microsoft 제작, Windows 전용.
  - **JSP**: Java 기반, 다양한 운영체제 지원.
  - **PHP**: C/Java와 유사한 문법, Linux/Unix/Windows 등 다양하게 지원.
- **기타**: Python(대화형 인터프리터, 플랫폼 독립적), Shell Script(유닉스/리눅스 명령어 조합).

Các bullet của **3. 스크립트 언어 (Scripting)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**3. 스크립트 언어 (Scripting)** vừa cho ta cách đặt câu hỏi. Bây giờ **4. 선언형 프로그래밍 언어 (Declarative)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **4. 선언형 프로그래밍 언어 (Declarative)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 4. 선언형 프로그래밍 언어 (Declarative)

Các ý ngay dưới **4. 선언형 프로그래밍 언어 (Declarative)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “4. 선언형 프로그래밍 언어 (Declarative)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **HTML**: 하이퍼텍스트 웹 표준 문서 생성.
- **LISP**: 인공지능 분야. 연결 리스트(Linked List) 및 재귀(Recursion) 호출 사용.
- **PROLOG**: 논리학 기초, 인공지능 논리 추론.
- **XML**: HTML 단점 보완, 태그(Tag) 사용자 정의 가능.
- **Haskell**: 함수형 언어로 부작용(Side Effect)이 없음.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **C.A.C.F** = Các ngôn ngữ thủ tục (C, Algol, Cobol, Fortran).
- **J.A.P** = Các ngôn ngữ kịch bản Server-side (JSP, ASP, PHP).

Với **4. 선언형 프로그래밍 언어 (Declarative)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **4. 선언형 프로그래밍 언어 (Declarative)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **프로그래밍 언어의 분류 (Classification of Programming Languages)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **라이브러리 및 예외 처리 (Libraries and Exception Handling)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **라이브러리 및 예외 처리 (Libraries and Exception Handling)** nối từ **프로그래밍 언어의 분류 (Classification of Programming Languages)** sang **운영체제 (OS: Operating System) 기초**, vì cơ chế trước tạo đầu vào cho bước sau.

## 라이브러리 및 예외 처리 (Libraries and Exception Handling)

Ở bước 55/86, **라이브러리 및 예외 처리 (Libraries and Exception Handling)** xuất hiện như phần tiếp nối của **프로그래밍 언어의 분류 (Classification of Programming Languages)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **라이브러리 및 예외 처리 (Libraries and Exception Handling)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 라이브러리 (Library)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 라이브러리 (Library)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 라이브러리 (Library)

Bây giờ ta đi vào nội dung của **1. 라이브러리 (Library)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. 라이브러리 (Library)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자주 사용하는 함수나 데이터들을 미리 만들어 모아 놓은 집합체 (표준 라이브러리, 외부 라이브러리).
- **C언어 대표 표준 라이브러리**:
  - `stdio.h`: 입출력 (`printf`, `scanf`)
  - `math.h`: 수학 함수 (`sqrt`, `pow`)
  - `string.h`: 문자열 처리 (`strlen`, `strcpy`)
  - `stdlib.h`: 자료형 변환, 메모리 할당, 난수 (`atoi`, `malloc`, `rand`)
  - `time.h`: 시간 처리 (`time`)

Các bullet của **1. 라이브러리 (Library)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 라이브러리 (Library)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 예외 처리 (Exception Handling)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 예외 처리 (Exception Handling)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 예외 처리 (Exception Handling)

Phần nguồn của **2. 예외 처리 (Exception Handling)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. 예외 처리 (Exception Handling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로그램의 정상적인 실행을 방해하는 조건이나 상태를 예외(Exception)라고 합니다.
- 예외 발생 시 비정상 종료를 막고 대비해 놓은 처리 루틴을 수행하는 것을 의미합니다.

> **Vietnamese Explanation**:
> Thư viện (Library) là nơi chứa các hàm viết sẵn để bạn gọi ra dùng (ví dụ nhập xuất, toán học). Xử lý ngoại lệ (Exception Handling) là việc bắt các lỗi có thể xảy ra trong lúc chạy (như chia cho 0, mất kết nối) để chương trình không bị sập ngang.

Các ý về **2. 예외 처리 (Exception Handling)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **2. 예외 처리 (Exception Handling)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **라이브러리 및 예외 처리 (Libraries and Exception Handling)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **운영체제 (OS: Operating System) 기초**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **운영체제 (OS: Operating System) 기초** nối từ **라이브러리 및 예외 처리 (Libraries and Exception Handling)** sang **Windows와 UNIX 운영체제 (Windows & UNIX)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 운영체제 (OS: Operating System) 기초

Sau khi đã đặt nền bằng **라이브러리 및 예외 처리 (Libraries and Exception Handling)**, ta chuyển sang **운영체제 (OS: Operating System) 기초**. Đây là mắt xích 56/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **운영체제 (OS: Operating System) 기초** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **성능 평가 4가지 기준**, **제어 프로그램 (Control Program)**, **처리 프로그램 (Processing Program)**, **Hiệu suất OS** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 정의 및 목적**. Hãy xác định **1. 정의 및 목적** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 정의 및 목적

Phần nguồn của **1. 정의 및 목적** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 정의 및 목적” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 하드웨어를 제어하고 사용자가 편리하게 컴퓨터를 사용할 수 있도록 돕는 시스템 소프트웨어.
- **성능 평가 4가지 기준**:
  1. **처리 능력 (Throughput)**: 일정 시간 내에 시스템이 처리하는 일의 양. (높을수록 좋음)
  2. **반환 시간 (Turn Around Time)**: 작업 의뢰부터 완료될 때까지 걸린 시간. (짧을수록 좋음)
  3. **사용 가능도 (Availability)**: 시스템을 필요할 때 즉시 사용할 수 있는 정도. (높을수록 좋음)
  4. **신뢰도 (Reliability)**: 시스템이 문제를 정확하게 해결하는 정도. (높을수록 좋음)

Các bullet của **1. 정의 및 목적** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 정의 및 목적** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 운영체제의 구성** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 운영체제의 구성** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 운영체제의 구성

Các ý ngay dưới **2. 운영체제의 구성** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2. 운영체제의 구성” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **제어 프로그램 (Control Program)**:
  - 감시 프로그램 (Supervisor): 자원 할당 및 작동 감시 (가장 핵심).
  - 작업 관리 (Job Management): 작업 순서 및 방법 관리.
  - 데이터 관리 (Data Management): 데이터/파일 처리 관리.
- **처리 프로그램 (Processing Program)**:
  - 언어 번역 프로그램 (컴파일러, 어셈블러 등).
  - 서비스 프로그램 (유틸리티 등).

💡 **Mẹo ghi nhớ (Mnemonics):**
- **Hiệu suất OS**: T.T.A.R (Throughput - Turnaround - Availability - Reliability).
- **Chương trình điều khiển**: Giám sát (Supervisor) - Công việc (Job) - Dữ liệu (Data).

Các bullet của **2. 운영체제의 구성** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 운영체제의 구성** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **운영체제 (OS: Operating System) 기초** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **Windows와 UNIX 운영체제 (Windows & UNIX)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **Windows와 UNIX 운영체제 (Windows & UNIX)** nối từ **운영체제 (OS: Operating System) 기초** sang **UNIX 주요 구성요소 (UNIX Components)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Windows와 UNIX 운영체제 (Windows & UNIX)

Từ **운영체제 (OS: Operating System) 기초**, ta đã có điểm tựa để bước vào **Windows와 UNIX 운영체제 (Windows & UNIX)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 57/86 trước khi đi vào chi tiết.

Để đọc **Windows와 UNIX 운영체제 (Windows & UNIX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **GUI (Graphic User Interface)**, **선점형 멀티태스킹 (Preemptive Multi-Tasking)**, **PnP (Plug and Play)**, **OLE (Object Linking and Embedding)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. Windows 주요 특징** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. Windows 주요 특징

Các ý ngay dưới **1. Windows 주요 특징** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “1. Windows 주요 특징” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **GUI (Graphic User Interface)**: 마우스 기반 그래픽 환경.
- **선점형 멀티태스킹 (Preemptive Multi-Tasking)**: 응용 프로그램 문제 시 OS가 강제 종료시켜 자원 반환.
- **PnP (Plug and Play)**: 하드웨어 설치 시 OS가 자동 감지 및 환경 구성.
- **OLE (Object Linking and Embedding)**: 문자/그림 개체를 다른 문서에 연결하거나 삽입.
- **긴 파일명**: 최대 255자 지정 가능 (VFAT 이용).

Các bullet của **1. Windows 주요 특징** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. Windows 주요 특징** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. UNIX 주요 특징** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. UNIX 주요 특징**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. UNIX 주요 특징

Bây giờ ta đi vào nội dung của **2. UNIX 주요 특징**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. UNIX 주요 특징” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 대화식 시분할 시스템 (Time Sharing System) 및 개방형 시스템 (Open System).
- 주로 **C언어**로 작성되어 이식성이 높고 파일 시스템은 트리(Tree) 구조를 가짐.
- **다중 사용자 (Multi-User)** 및 **다중 작업 (Multi-Tasking)** 지원.

Các bullet của **2. UNIX 주요 특징** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. UNIX 주요 특징**, đừng bắt đầu lại từ số không. **3. 파일 디스크립터 (File Descriptor)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3. 파일 디스크립터 (File Descriptor)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3. 파일 디스크립터 (File Descriptor)

Phần nguồn của **3. 파일 디스크립터 (File Descriptor)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3. 파일 디스크립터 (File Descriptor)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 파일 제어 블록(FCB; File Control Block)이라고도 하며, 시스템(OS)이 필요로 하는 파일에 대한 정보를 가진 제어 블록.
- 파일마다 독립적으로 존재하며 보통 보조기억장치에 있다가 파일이 열릴(Open) 때 주기억장치로 옮겨집니다.

Các bullet của **3. 파일 디스크립터 (File Descriptor)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**3. 파일 디스크립터 (File Descriptor)** vừa cho ta cách đặt câu hỏi. Bây giờ **4. UNIX 시스템 구조: 커널 (Kernel)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **4. UNIX 시스템 구조: 커널 (Kernel)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 4. UNIX 시스템 구조: 커널 (Kernel)

Các ý ngay dưới **4. UNIX 시스템 구조: 커널 (Kernel)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “4. UNIX 시스템 구조: 커널 (Kernel)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- UNIX의 가장 **핵심적인 부분**. 프로그램과 하드웨어 간의 인터페이스 역할을 담당하며 프로세스, 메모리, 입출력 관리 등을 수행합니다.

> **Vietnamese Explanation**:
> Windows nổi bật với giao diện chuột GUI, Plug and Play (cắm là chạy). UNIX là hệ điều hành mã nguồn mở, đa nhiệm, đa người dùng, chủ yếu viết bằng C. Trong UNIX, Kernel (nhân) là phần cốt lõi quản lý phần cứng và giao tiếp với phần mềm. File Descriptor lưu giữ thông tin quan trọng về các file đang được hệ thống quản lý.

Các bullet của **4. UNIX 시스템 구조: 커널 (Kernel)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **4. UNIX 시스템 구조: 커널 (Kernel)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **Windows와 UNIX 운영체제 (Windows & UNIX)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **UNIX 주요 구성요소 (UNIX Components)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **UNIX 주요 구성요소 (UNIX Components)** nối từ **Windows와 UNIX 운영체제 (Windows & UNIX)** sang **메모리 관리 (Memory Management)**, vì cơ chế trước tạo đầu vào cho bước sau.

## UNIX 주요 구성요소 (UNIX Components)

Ở bước 58/86, **UNIX 주요 구성요소 (UNIX Components)** xuất hiện như phần tiếp nối của **Windows와 UNIX 운영체제 (Windows & UNIX)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **UNIX 주요 구성요소 (UNIX Components)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 쉘 (Shell)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 쉘 (Shell)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 쉘 (Shell)

Bây giờ ta đi vào nội dung của **1. 쉘 (Shell)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. 쉘 (Shell)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 사용자의 명령어를 인식하여 프로그램을 호출하고 명령을 수행하는 **명령어 해석기**입니다.
- 주기억장치에 상주하지 않고 명령어가 포함된 파일 형태로 존재합니다.
- 파이프라인 기능을 지원하며 입·출력 재지정(Redirection)이 가능합니다.
- 예: Bourne Shell, C Shell, Korn Shell 등

Các bullet của **1. 쉘 (Shell)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 쉘 (Shell)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 유틸리티 프로그램 (Utility Program)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 유틸리티 프로그램 (Utility Program)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 유틸리티 프로그램 (Utility Program)

Phần nguồn của **2. 유틸리티 프로그램 (Utility Program)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. 유틸리티 프로그램 (Utility Program)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 일반 사용자가 작성한 응용 프로그램을 처리하는 데 사용됩니다. (에디터, 컴파일러, 디버거 등)

> **Vietnamese Explanation**:
> Shell trong UNIX đóng vai trò như người phiên dịch, nhận lệnh từ người dùng và giao cho hệ thống xử lý. Chương trình tiện ích (Utility) là các công cụ hỗ trợ người dùng như trình soạn thảo, trình biên dịch.

Các bullet của **2. 유틸리티 프로그램 (Utility Program)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 유틸리티 프로그램 (Utility Program)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **UNIX 주요 구성요소 (UNIX Components)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **메모리 관리 (Memory Management)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **메모리 관리 (Memory Management)** nối từ **UNIX 주요 구성요소 (UNIX Components)** sang **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 메모리 관리 (Memory Management)

Sau khi đã đặt nền bằng **UNIX 주요 구성요소 (UNIX Components)**, ta chuyển sang **메모리 관리 (Memory Management)**. Đây là mắt xích 59/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **메모리 관리 (Memory Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **최초 적합 (First Fit)**, **최적 적합 (Best Fit)**, **최악 적합 (Worst Fit)**, **페이징(Paging) 기법** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 배치 전략 (Placement Strategy)**. Hãy xác định **1. 배치 전략 (Placement Strategy)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 배치 전략 (Placement Strategy)

Phần nguồn của **1. 배치 전략 (Placement Strategy)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

새로 반입되는 프로그램이나 데이터를 주기억장치의 어디에 위치시킬 것인지 결정합니다.
- **최초 적합 (First Fit)**: 빈 영역 중 첫 번째 분할 영역에 배치.
- **최적 적합 (Best Fit)**: 단편화(Fragmentation/Khoảng trống thừa)를 가장 작게 남기는 분할 영역에 배치.
- **최악 적합 (Worst Fit)**: 단편화를 가장 많이 남기는 분할 영역에 배치.

Các bullet của **1. 배치 전략 (Placement Strategy)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 배치 전략 (Placement Strategy)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 가상기억장치 구현 기법 (Virtual Memory Techniques)

Các ý ngay dưới **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2. 가상기억장치 구현 기법 (Virtual Memory Techniques)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **페이징(Paging) 기법**: 가상기억장치와 주기억장치를 **동일한 크기**로 나누어 적재. (프로그램 단위: 페이지, 주기억장치 단위: 페이지 프레임)
  - 외부 단편화는 발생하지 않으나, **내부 단편화**는 발생 가능.
- **세그먼테이션(Segmentation) 기법**: 프로그램을 배열이나 함수 등 **다양한 크기의 논리적인 단위(세그먼트)**로 나누어 적재.
  - 내부 단편화는 발생하지 않으나, **외부 단편화**는 발생 가능.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **Paging**: Bằng nhau (Page). Lỗi nội bộ (내부 단편화).
- **Segmentation**: Khác nhau (Theo logic). Lỗi bên ngoài (외부 단편화).

Các bullet của **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **메모리 관리 (Memory Management)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)** nối từ **메모리 관리 (Memory Management)** sang **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)

Từ **메모리 관리 (Memory Management)**, ta đã có điểm tựa để bước vào **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 60/86 trước khi đi vào chi tiết.

Để đọc **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **OPT (Optimal)**, **FIFO (First In First Out)**, **LRU (Least Recently Used)**, **LFU (Least Frequently Used)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 페이지 교체 알고리즘 (Page Replacement Algorithms)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 페이지 교체 알고리즘 (Page Replacement Algorithms)

Các ý ngay dưới **1. 페이지 교체 알고리즘 (Page Replacement Algorithms)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

페이지 부재(Page Fault) 발생 시, 어떤 페이지 프레임을 교체할 것인지 결정합니다.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용하지 않을 페이지 교체 (가장 효율적이나 미래 예측이 필요해 비현실적).
- **FIFO (First In First Out)**: 가장 먼저 들어와서 가장 오래 있었던 페이지 교체.
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 사용하지 않은 페이지 교체 (계수기나 스택 사용).
- **LFU (Least Frequently Used)**: 사용 빈도(횟수)가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: LRU의 오버헤드를 줄이기 위해 참조 비트와 변형 비트를 사용하여 최근 사용 안 된 페이지 교체.
- **SCR (Second Chance Replacement)**: FIFO의 단점을 보완하여 자주 사용되는 페이지는 한 번 더 기회를 줌.

Các bullet của **1. 페이지 교체 알고리즘 (Page Replacement Algorithms)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 페이지 교체 알고리즘 (Page Replacement Algorithms)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 페이지 크기 (Page Size)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. 페이지 크기 (Page Size)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. 페이지 크기 (Page Size)

Bây giờ ta đi vào nội dung của **2. 페이지 크기 (Page Size)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. 페이지 크기 (Page Size)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **크기가 작을 경우**: 페이지 단편화 감소, 워킹 셋 효율 증가, Locality 일치로 기억장치 효율 상승. 단, 페이지 맵 테이블 크기가 커지고 매핑 속도가 느려지며 디스크 입출력 횟수가 증가.
- **크기가 클 경우**: 페이지 맵 테이블 크기 감소, 매핑 속도 상승, 디스크 입출력 횟수 감소. 단, 불필요한 내용까지 적재될 수 있고 페이지 단편화가 증가.

Các bullet của **2. 페이지 크기 (Page Size)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 페이지 크기 (Page Size)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)** đặt đầu vào cho **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**, rồi **프로세스와 스레드 (Process and Thread)** mở rộng hệ quả liên quan.

## 프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)

Ở bước 61/86, **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** xuất hiện như phần tiếp nối của **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **시간 구역성 (Temporal Locality)**, **공간 구역성 (Spatial Locality)**, **방지 방법** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. Locality (국부성, 구역성)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. Locality (국부성, 구역성)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. Locality (국부성, 구역성)

Bây giờ ta đi vào nội dung của **1. Locality (국부성, 구역성)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

프로세스 실행 중 일부 페이지만 집중적으로 참조하는 성질.
- **시간 구역성 (Temporal Locality)**: 하나의 페이지를 짧은 시간 동안 집중 참조 (반복문, 스택 등).
- **공간 구역성 (Spatial Locality)**: 특정 위치 주변의 페이지를 집중 참조 (배열, 순차적 코드 등).

Các bullet của **1. Locality (국부성, 구역성)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. Locality (국부성, 구역성)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 워킹 셋 (Working Set)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 워킹 셋 (Working Set)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 워킹 셋 (Working Set)

Phần nguồn của **2. 워킹 셋 (Working Set)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

프로세스가 일정 시간 동안 자주 참조하는 페이지들의 집합. (시간에 따라 변함). 주기억장치에 상주시키면 페이지 부재 현상이 줄어듭니다.

Phần **2. 워킹 셋 (Working Set)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. 워킹 셋 (Working Set)**, đừng bắt đầu lại từ số không. **3. 스래싱 (Thrashing)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **3. 스래싱 (Thrashing)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 3. 스래싱 (Thrashing)

Các ý ngay dưới **3. 스래싱 (Thrashing)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

프로세스 처리 시간보다 페이지 교체에 소요되는 시간이 더 많아져 시스템 성능이 급격히 저하되는 현상.
- **방지 방법**: 다중 프로그래밍 정도 조절, 페이지 부재 빈도 조절, 워킹 셋 유지 등.

> **Vietnamese Explanation**:
> **Locality** là tính cục bộ (hay dùng lại chỗ vừa dùng). **Working Set** là tập hợp các trang bộ nhớ đang được dùng nhiều nhất, cần giữ lại ở RAM. **Thrashing** là hiện tượng "giậm chân tại chỗ", máy bận rộn tráo đổi dữ liệu với ổ cứng nhiều hơn là thực sự chạy chương trình, làm máy bị đơ.

Các bullet của **3. 스래싱 (Thrashing)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 스래싱 (Thrashing)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **프로세스와 스레드 (Process and Thread)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** đặt đầu vào cho **프로세스와 스레드 (Process and Thread)**, rồi **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** mở rộng hệ quả liên quan.

## 프로세스와 스레드 (Process and Thread)

Sau khi đã đặt nền bằng **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**, ta chuyển sang **프로세스와 스레드 (Process and Thread)**. Đây là mắt xích 62/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **프로세스와 스레드 (Process and Thread)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **PCB(Process Control Block)**, **주요 용어**, **Dispatch (디스패치)**, **Wake Up (웨이크 업)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 프로세스 (Process)**. Hãy xác định **1. 프로세스 (Process)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 프로세스 (Process)

Phần nguồn của **1. 프로세스 (Process)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 프로세스 (Process)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- CPU에 의해 처리되는 실행 중인 프로그램 (작업/Job, 태스크/Task).
- **PCB(Process Control Block)**: 운영체제가 프로세스에 대한 중요한 정보를 저장하는 곳. (현재 상태, 포인터, 고유 식별자, 스케줄링 우선순위 등). 프로세스 생성 시 만들어지고 완료 시 제거됨.

Các bullet của **1. 프로세스 (Process)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 프로세스 (Process)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 프로세스 상태 전이 (Process State Transition)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 프로세스 상태 전이 (Process State Transition)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 프로세스 상태 전이 (Process State Transition)

Các ý ngay dưới **2. 프로세스 상태 전이 (Process State Transition)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2. 프로세스 상태 전이 (Process State Transition)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **제출(Submit) -> 접수(Hold) -> 준비(Ready) -> 실행(Run) -> 대기(Wait/Block) -> 종료(Exit)**
- **주요 용어**:
  - **Dispatch (디스패치)**: 준비 상태 -> 실행 상태로 전이 (CPU 할당).
  - **Wake Up (웨이크 업)**: 입·출력 완료 후 대기 상태 -> 준비 상태로 전이.
  - **Spooling (스풀링)**: 디스크를 버퍼처럼 활용해 느린 입출력 장치와 CPU 간 속도 차이를 보완.

Các bullet của **2. 프로세스 상태 전이 (Process State Transition)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 프로세스 상태 전이 (Process State Transition)**, đừng bắt đầu lại từ số không. **3. 스레드 (Thread)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. 스레드 (Thread)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. 스레드 (Thread)

Bây giờ ta đi vào nội dung của **3. 스레드 (Thread)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. 스레드 (Thread)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로세스 내에서의 작업 단위 (경량 프로세스/Light Weight Process).
- 동일 프로세스 환경에서 서로 독립적인 다중 수행이 가능하여 응답 시간을 단축하고 기억장소 낭비를 줄입니다.

> **Vietnamese Explanation**:
> **Process** là một chương trình đang chạy. **Thread** là các luồng xử lý nhỏ nằm bên trong Process. Dùng nhiều thread giúp chương trình chạy nhanh hơn và chia sẻ bộ nhớ tốt hơn (ví dụ nhiều tab trên trình duyệt). **Dispatch** là hành động cấp CPU cho một tiến trình đang xếp hàng chờ.

Các ý về **3. 스레드 (Thread)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Như vậy, **3. 스레드 (Thread)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **프로세스와 스레드 (Process and Thread)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **프로세스와 스레드 (Process and Thread)** đặt đầu vào cho **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**, rồi **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** mở rộng hệ quả liên quan.

## 주요 스케줄링 알고리즘 (Major Scheduling Algorithms)

Từ **프로세스와 스레드 (Process and Thread)**, ta đã có điểm tựa để bước vào **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 63/86 trước khi đi vào chi tiết.

Để đọc **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. FCFS (First Come First Service) / FIFO** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. FCFS (First Come First Service) / FIFO

Các ý ngay dưới **1. FCFS (First Come First Service) / FIFO** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

준비 큐에 도착한 순서대로 CPU를 할당하는 기법 (선입선출). 구현은 가장 간단하나, 긴 작업이 먼저 오면 뒤의 짧은 작업이 오래 기다리게 됨.

Phần **1. FCFS (First Come First Service) / FIFO** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **1. FCFS (First Come First Service) / FIFO** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. SJF (Shortest Job First)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. SJF (Shortest Job First)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. SJF (Shortest Job First)

Bây giờ ta đi vào nội dung của **2. SJF (Shortest Job First)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

실행 시간이 가장 짧은 프로세스에게 먼저 CPU를 할당하는 기법. 가장 적은 평균 대기 시간을 제공하지만, 실행 시간이 긴 프로세스는 무한정 기다릴 수 있음.

Phần **2. SJF (Shortest Job First)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. SJF (Shortest Job First)**, đừng bắt đầu lại từ số không. **3. HRN (Highest Response-ratio Next)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3. HRN (Highest Response-ratio Next)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3. HRN (Highest Response-ratio Next)

Phần nguồn của **3. HRN (Highest Response-ratio Next)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

SJF의 단점(긴 작업 불리)을 보완하여 대기 시간과 실행 시간을 함께 고려함.
- **우선순위 계산식**: `(대기 시간 + 서비스 시간) / 서비스 시간`
- 결과값이 높은 것부터 우선순위를 부여함.

Các bullet của **3. HRN (Highest Response-ratio Next)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. HRN (Highest Response-ratio Next)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** nối từ **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)** sang **IP 주소 및 서브네팅 (IP Address & Subnetting)**, vì cơ chế trước tạo đầu vào cho bước sau.

## UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)

Ở bước 64/86, **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** xuất hiện như phần tiếp nối của **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 주요 환경 변수 (Environment Variables)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 주요 환경 변수 (Environment Variables)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 주요 환경 변수 (Environment Variables)

Bây giờ ta đi vào nội dung của **1. 주요 환경 변수 (Environment Variables)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

환경 변수를 사용할 때는 변수명 앞에 `$`를 붙입니다.
- `$HOME`: 사용자의 홈 디렉터리
- `$PWD`: 현재 작업하는 디렉터리
- `$PATH`: 실행 파일을 찾는 경로
- `$USER`: 사용자의 이름

Các bullet của **1. 주요 환경 변수 (Environment Variables)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 주요 환경 변수 (Environment Variables)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 기본 명령어 (Basic Commands)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 기본 명령어 (Basic Commands)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 기본 명령어 (Basic Commands)

Phần nguồn của **2. 기본 명령어 (Basic Commands)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. 기본 명령어 (Basic Commands)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `cat`: 파일 내용 화면 표시
- `chmod`: 파일 보호 모드 설정 (사용 허가 지정)
- `chown`: 파일 소유자 변경
- `cp`: 파일 복사 / `rm`: 파일 삭제
- `find`: 파일 검색
- `fork`: 새로운 프로세스 생성 (프로세스 복제)
- `fsck`: 파일 시스템 검사 및 보수
- `ls`: 현재 디렉터리 내 파일 목록 확인

> **Vietnamese Explanation**:
> Biến môi trường trong UNIX/LINUX giúp hệ thống biết các cài đặt mặc định (như đường dẫn `$PATH`, thư mục chủ `$HOME`). Các lệnh cơ bản như `chmod` dùng để phân quyền file, `fork` để nhân bản tiến trình.

Các bullet của **2. 기본 명령어 (Basic Commands)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 기본 명령어 (Basic Commands)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **IP 주소 및 서브네팅 (IP Address & Subnetting)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **IP 주소 및 서브네팅 (IP Address & Subnetting)** nối từ **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** sang **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, vì cơ chế trước tạo đầu vào cho bước sau.

## IP 주소 및 서브네팅 (IP Address & Subnetting)

Sau khi đã đặt nền bằng **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)**, ta chuyển sang **IP 주소 및 서브네팅 (IP Address & Subnetting)**. Đây là mắt xích 65/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **IP 주소 및 서브네팅 (IP Address & Subnetting)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **A Class**, **B Class**, **C Class**, **D Class** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. IPv4 주소 (Internet Protocol version 4)**. Hãy xác định **1. IPv4 주소 (Internet Protocol version 4)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. IPv4 주소 (Internet Protocol version 4)

Phần nguồn của **1. IPv4 주소 (Internet Protocol version 4)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. IPv4 주소 (Internet Protocol version 4)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 8비트씩 4부분, 총 **32비트**로 구성됩니다.
- 네트워크 크기에 따라 A~E 클래스로 나뉩니다.
  - **A Class**: 국가/대형 망 (0~127)
  - **B Class**: 중대형 망 (128~191)
  - **C Class**: 소규모 망 (192~223)
  - **D Class**: 멀티캐스트용 (224~239)
  - **E Class**: 실험적 주소

Các bullet của **1. IPv4 주소 (Internet Protocol version 4)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. IPv4 주소 (Internet Protocol version 4)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 서브네팅 (Subnetting)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 서브네팅 (Subnetting)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 서브네팅 (Subnetting)

Các ý ngay dưới **2. 서브네팅 (Subnetting)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

할당된 네트워크 주소를 다시 여러 개의 작은 네트워크로 나누어 사용하는 기법입니다. (서브넷 마스크 활용).

Phần **2. 서브네팅 (Subnetting)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. 서브네팅 (Subnetting)**, đừng bắt đầu lại từ số không. **3. IPv6 주소 (Internet Protocol version 6)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. IPv6 주소 (Internet Protocol version 6)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. IPv6 주소 (Internet Protocol version 6)

Bây giờ ta đi vào nội dung của **3. IPv6 주소 (Internet Protocol version 6)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. IPv6 주소 (Internet Protocol version 6)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- IPv4의 주소 부족 문제를 해결하기 위해 개발되었습니다.
- 16비트씩 8부분, 총 **128비트**로 구성되며 콜론(`:`)으로 구분합니다.
- 인증성, 기밀성, 무결성을 지원하여 보안이 뛰어나고, 주소 확장성과 호환성이 좋습니다.
- **주소 체계**:
  - **유니캐스트 (Unicast)**: 1 대 1 통신
  - **멀티캐스트 (Multicast)**: 1 대 다 통신
  - **애니캐스트 (Anycast)**: 1 대 1 통신 (가장 가까운 수신자에게 전송)

💡 **Mẹo ghi nhớ (Mnemonics):**
- **IPv4**: 32-bit (4 x 8).
- **IPv6**: 128-bit (8 x 16), **U.M.A** (Unicast, Multicast, Anycast).

Các bullet của **3. IPv6 주소 (Internet Protocol version 6)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. IPv6 주소 (Internet Protocol version 6)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **IP 주소 및 서브네팅 (IP Address & Subnetting)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **IP 주소 및 서브네팅 (IP Address & Subnetting)** dẫn sang **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **5과목 정보시스템 구축 관리 (Information System Construction Management)** mở rộng hệ quả liên quan.

## OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)

Từ **IP 주소 및 서브네팅 (IP Address & Subnetting)**, ta đã có điểm tựa để bước vào **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 66/86 trước khi đi vào chi tiết.

Để đọc **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **물리 계층 (Physical)**, **데이터 링크 계층 (Data Link)**, **네트워크 계층 (Network)**, **전송 계층 (Transport)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

국제표준화기구(ISO)에서 제안한 통신 규약으로, 하위 3계층과 상위 4계층으로 나뉩니다.
- **물리 계층 (Physical)**: 실제 접속, 기계적/전기적 특성 정의.
- **데이터 링크 계층 (Data Link)**: 인접 시스템 간 신뢰성 있는 전송, 흐름 제어, 오류 제어, 동기화.
- **네트워크 계층 (Network)**: 경로 설정(Routing), 트래픽 제어, 패킷 전송.
- **전송 계층 (Transport)**: 종단(End-to-End) 간 신뢰성 있는 데이터 전송, 연결 설정, 다중화.
- **세션 계층 (Session)**: 대화(회화) 제어, 동기 제어.
- **표현 계층 (Presentation)**: 데이터 형식 변환, 암호화, 압축.
- **응용 계층 (Application)**: 사용자에게 통신 서비스 제공.

> **Vietnamese Explanation**:
> Mô hình OSI chia quá trình truyền mạng thành 7 lớp. 3 lớp dưới (Physical, Data Link, Network) lo việc truyền dẫn tín hiệu, tìm đường (routing). 4 lớp trên (Transport, Session, Presentation, Application) lo việc kiểm tra lỗi, mã hóa dữ liệu và giao tiếp với người dùng.

Điểm chốt của **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **5과목 정보시스템 구축 관리 (Information System Construction Management)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **5과목 정보시스템 구축 관리 (Information System Construction Management)** nối từ **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)** sang **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5과목 정보시스템 구축 관리 (Information System Construction Management)

Ở bước 67/86, **5과목 정보시스템 구축 관리 (Information System Construction Management)** xuất hiện như phần tiếp nối của **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **5과목 정보시스템 구축 관리 (Information System Construction Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **구조적 방법론 (Structured)**, **정보공학 방법론 (Information Engineering)**, **컴포넌트 기반 방법론 (CBD)**, **소프트웨어 재사용 (Reuse)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **소프트웨어 개발 방법론 (Software Development Methodologies)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **소프트웨어 개발 방법론 (Software Development Methodologies)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 소프트웨어 개발 방법론 (Software Development Methodologies)

Bây giờ ta đi vào nội dung của **소프트웨어 개발 방법론 (Software Development Methodologies)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “소프트웨어 개발 방법론 (Software Development Methodologies)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **구조적 방법론 (Structured)**: 처리(Process) 중심. 분할과 정복(Divide and Conquer) 원리 적용.
- **정보공학 방법론 (Information Engineering)**: 자료(Data) 중심. 대규모 정보 시스템 구축에 적합.
- **컴포넌트 기반 방법론 (CBD)**: 기존 컴포넌트를 조합하여 새로운 애플리케이션 생성. 재사용성(Reusability)과 확장성이 높고 유지보수 비용 최소화.

Các bullet của **소프트웨어 개발 방법론 (Software Development Methodologies)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **소프트웨어 개발 방법론 (Software Development Methodologies)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)

Phần nguồn của **소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **소프트웨어 재사용 (Reuse)**: 이미 검증된 소프트웨어를 새로운 개발에 사용하여 개발 시간 및 비용 단축, 품질 향상.
- **소프트웨어 재공학 (Reengineering)**: 기존 시스템의 분석·재구성·역공학·이식 등을 통해 유지보수성과 수명을 개선하는 활동이다. 신규 기능 추가 자체와 동일한 개념은 아니다.

> **Vietnamese Explanation**:
> - **Methodologies**: Structured (Tập trung vào quá trình), Information Engineering (Tập trung vào dữ liệu), CBD (Lắp ráp từ các linh kiện có sẵn).
> - **Reuse**: Dùng lại code/module cũ cho dự án mới để tiết kiệm chi phí.
> - **Reengineering**: Tái cấu trúc, cải tiến hệ thống cũ để dễ bảo trì và đáp ứng nhu cầu mới.

Các bullet của **소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **5과목 정보시스템 구축 관리 (Information System Construction Management)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** nối từ **5과목 정보시스템 구축 관리 (Information System Construction Management)** sang **CASE (Computer Aided Software Engineering)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)

Sau khi đã đặt nền bằng **5과목 정보시스템 구축 관리 (Information System Construction Management)**, ta chuyển sang **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)**. Đây là mắt xích 68/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **합성 중심 (Composition-Based)**, **생성 중심 (Generation-Based)**, **분석 (Analysis)**, **재구성 (Restructuring)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 재사용 방법 (Reuse Methods)**. Hãy xác định **1. 재사용 방법 (Reuse Methods)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 재사용 방법 (Reuse Methods)

Phần nguồn của **1. 재사용 방법 (Reuse Methods)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 재사용 방법 (Reuse Methods)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **합성 중심 (Composition-Based)**: 소프트웨어 부품(블록)을 만들어 끼워 맞추어 완성시키는 방법. (블록 구성 방법)
- **생성 중심 (Generation-Based)**: 추상화 형태의 명세를 구체화하여 프로그램을 만드는 방법. (패턴 구성 방법)

Các bullet của **1. 재사용 방법 (Reuse Methods)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 재사용 방법 (Reuse Methods)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 재공학 주요 활동 (Reengineering Activities)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 재공학 주요 활동 (Reengineering Activities)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 재공학 주요 활동 (Reengineering Activities)

Các ý ngay dưới **2. 재공학 주요 활동 (Reengineering Activities)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

기존 시스템을 개선하고 유지보수성을 높이는 활동입니다.
- **분석 (Analysis)**: 기존 명세서를 확인해 동작을 이해하고 대상을 선정.
- **재구성 (Restructuring)**: 외적인 동작은 유지하면서 코드 구조를 향상.
- **역공학 (Reverse Engineering)**: 기존 코드를 분석해 설계 정보나 구성 요소를 다시 추출(도출)해 내는 활동.
- **이식 (Migration)**: 다른 운영체제나 하드웨어 환경에서 사용할 수 있도록 변환.

Các bullet của **2. 재공학 주요 활동 (Reengineering Activities)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 재공학 주요 활동 (Reengineering Activities)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **CASE (Computer Aided Software Engineering)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** nêu quy tắc; **CASE (Computer Aided Software Engineering)** thử quy tắc trong tình huống, rồi **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** mở rộng hệ quả.

## CASE (Computer Aided Software Engineering)

Từ **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)**, ta đã có điểm tựa để bước vào **CASE (Computer Aided Software Engineering)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 69/86 trước khi đi vào chi tiết.

Để đọc **CASE (Computer Aided Software Engineering)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “CASE (Computer Aided Software Engineering)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소프트웨어 개발 생명 주기(요구 분석, 설계, 구현, 검사 등) 전체 또는 일부를 **컴퓨터와 전용 도구를 사용해 자동화**하는 기법.
- 개발의 표준화를 지향하며 생산성 및 품질을 향상시킵니다.

Điểm chốt của **CASE (Computer Aided Software Engineering)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **CASE (Computer Aided Software Engineering)** nêu quy tắc; **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** thử quy tắc trong tình huống, rồi **교착상태 (Dead Lock)** mở rộng hệ quả.

## DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)

Ở bước 70/86, **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** xuất hiện như phần tiếp nối của **CASE (Computer Aided Software Engineering)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **연기 갱신 (Deferred Update)**, **즉각 갱신 (Immediate Update)**, **그림자 페이지 (Shadow Paging)**, **검사점 (Check Point)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 회복 기법 (Recovery)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 회복 기법 (Recovery)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 회복 기법 (Recovery)

Bây giờ ta đi vào nội dung của **1. 회복 기법 (Recovery)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

장애 발생 시 데이터베이스를 정상 상태로 복구합니다.
- **연기 갱신 (Deferred Update)**: 트랜잭션이 완료될 때까지 DB 갱신을 연기하고 로그(Log)에 보관. 실패 시 무시하면 됨. (Redo만 가능).
- **즉각 갱신 (Immediate Update)**: 즉시 DB에 갱신하고 로그에 보관. 실패 시 취소(Undo)와 재실행(Redo) 모두 사용.
- **그림자 페이지 (Shadow Paging)**: 복사본(그림자) 페이지를 보관해두고, 실패 시 대체하는 방식 (로그 불필요).
- **검사점 (Check Point)**: 특정 단계에 검사점을 찍어 장애 시 그 시점부터 회복(시간 절약).

Các bullet của **1. 회복 기법 (Recovery)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 회복 기법 (Recovery)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 병행 제어 기법 (Concurrency Control)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 병행 제어 기법 (Concurrency Control)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 병행 제어 기법 (Concurrency Control)

Phần nguồn của **2. 병행 제어 기법 (Concurrency Control)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

다중 트랜잭션 실행 시 DB의 일관성이 파괴되지 않도록 제어합니다.
- **로킹 (Locking)**: 데이터 엑세스 전에 Lock(잠금)을 요청하는 기법. (로킹 단위: DB, 파일, 레코드 등 한꺼번에 잠그는 크기).
- **타임 스탬프 순서 (Time Stamp Ordering)**: 트랜잭션 실행 전 시간표(Time Stamp)를 부여해 그 순서대로 처리 (교착상태 미발생).
- **다중 버전 기법**: 갱신될 때마다 새로운 버전(Version)을 부여해 관리.

> **Vietnamese Explanation**:
> **Recovery (Phục hồi DB)** có Deferred (chờ xong mới cập nhật - chỉ Redo), Immediate (cập nhật ngay - cần cả Undo và Redo).
> **Concurrency Control (Kiểm soát đồng thời)** dùng Locking (khóa dữ liệu khi đang dùng) hoặc Time Stamp (cấp tem thời gian để xếp hàng trước sau) tránh việc 2 giao dịch cùng sửa 1 dữ liệu gây lỗi.

Các bullet của **2. 병행 제어 기법 (Concurrency Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 병행 제어 기법 (Concurrency Control)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **교착상태 (Dead Lock)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **교착상태 (Dead Lock)** nối từ **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)** sang **침입 탐지 시스템 (IDS; Intrusion Detection System)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 교착상태 (Dead Lock)

Sau khi đã đặt nền bằng **DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)**, ta chuyển sang **교착상태 (Dead Lock)**. Đây là mắt xích 71/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **교착상태 (Dead Lock)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **상호 배제 (Mutual Exclusion)**, **점유와 대기 (Hold and Wait)**, **비선점 (Non-preemption)**, **환형 대기 (Circular Wait)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

둘 이상의 프로세스가 자원을 점유한 상태에서 서로 다른 프로세스의 자원을 무한정 기다리는 현상.

Ta bắt đầu phần nội dung bằng **1. 교착상태 발생의 4가지 필요충분조건**. Hãy xác định **1. 교착상태 발생의 4가지 필요충분조건** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 교착상태 발생의 4가지 필요충분조건

Phần nguồn của **1. 교착상태 발생의 4가지 필요충분조건** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

모두 충족해야 교착상태가 발생합니다.
- **상호 배제 (Mutual Exclusion)**: 한 번에 한 프로세스만 자원 사용.
- **점유와 대기 (Hold and Wait)**: 자원을 점유한 채로 다른 자원을 대기.
- **비선점 (Non-preemption)**: 할당된 자원을 강제로 빼앗을 수 없음.
- **환형 대기 (Circular Wait)**: 대기하는 프로세스들이 원형(Cycle)을 이룸.

Các bullet của **1. 교착상태 발생의 4가지 필요충분조건** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 교착상태 발생의 4가지 필요충분조건** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 교착상태 해결 방법** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 교착상태 해결 방법** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 교착상태 해결 방법

Các ý ngay dưới **2. 교착상태 해결 방법** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2. 교착상태 해결 방법” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **예방 (Prevention)**: 4가지 조건 중 하나를 제거 (자원 낭비가 가장 심함).
- **회피 (Avoidance)**: 발생 가능성을 인정하고 적절히 피해감 (**은행원 알고리즘 / Banker's Algorithm**).
- **발견 (Detection)**: 발생 여부를 점검 (자원 할당 그래프 등).
- **회복 (Recovery)**: 교착상태에 있는 프로세스를 종료하거나 자원을 선점하여 회복.

> **Vietnamese Explanation**:
> **Deadlock (Bế tắc)** giống như kẹt xe ở ngã tư, ai cũng chờ người kia nhường đường nên không ai đi được. Để giải quyết, phương pháp **Avoidance (Né tránh)** dùng thuật toán Banker (người giữ tiền) để đảm bảo luôn có đủ tài nguyên cấp phát một cách an toàn.

Các bullet của **2. 교착상태 해결 방법** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 교착상태 해결 방법** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **교착상태 (Dead Lock)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **침입 탐지 시스템 (IDS; Intrusion Detection System)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **침입 탐지 시스템 (IDS; Intrusion Detection System)** nối từ **교착상태 (Dead Lock)** sang **리눅스의 커널 로그 (Linux Kernel Logs)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 침입 탐지 시스템 (IDS; Intrusion Detection System)

Từ **교착상태 (Dead Lock)**, ta đã có điểm tựa để bước vào **침입 탐지 시스템 (IDS; Intrusion Detection System)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 72/86 trước khi đi vào chi tiết.

Để đọc **침입 탐지 시스템 (IDS; Intrusion Detection System)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **오용 탐지 (Misuse Detection)**, **이상 탐지 (Anomaly Detection)**, **종류**, **HIDS (Host-Based)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

컴퓨터 시스템의 비정상적인 사용, 오용, 남용 등을 실시간으로 탐지하는 시스템.
- **오용 탐지 (Misuse Detection)**: 미리 입력해 둔 공격 패턴 감지 (시그니처 기반).
- **이상 탐지 (Anomaly Detection)**: 평균적인 상태를 기준으로 비정상 행위 감지 (행위 기반).
- **종류**:
  - **HIDS (Host-Based)**: 내부 시스템 감시 (OSSEC 등).
  - **NIDS (Network-Based)**: 외부로부터의 네트워크 트래픽 감시 (Snort 등).

Điểm chốt của **침입 탐지 시스템 (IDS; Intrusion Detection System)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **리눅스의 커널 로그 (Linux Kernel Logs)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **리눅스의 커널 로그 (Linux Kernel Logs)** nối từ **침입 탐지 시스템 (IDS; Intrusion Detection System)** sang **소프트웨어 생명주기 모델 (SDLC Models)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 리눅스의 커널 로그 (Linux Kernel Logs)

Ở bước 73/86, **리눅스의 커널 로그 (Linux Kernel Logs)** xuất hiện như phần tiếp nối của **침입 탐지 시스템 (IDS; Intrusion Detection System)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **리눅스의 커널 로그 (Linux Kernel Logs)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “리눅스의 커널 로그 (Linux Kernel Logs)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `/var/log/wtmp`: 성공한 로그인/로그아웃 및 시스템 시작/종료 시간 기록.
- `/var/run/utmp`: 현재 로그인한 사용자의 상태 기록.
- `/var/log/btmp`: 실패한 로그인 기록.
- `/var/log/lastlog`: 마지막으로 성공한 로그인 기록.

Như vậy, **리눅스의 커널 로그 (Linux Kernel Logs)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **소프트웨어 생명주기 모델 (SDLC Models)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **소프트웨어 생명주기 모델 (SDLC Models)** nối từ **리눅스의 커널 로그 (Linux Kernel Logs)** sang **스토리지 시스템 (Storage Systems)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 소프트웨어 생명주기 모델 (SDLC Models)

Sau khi đã đặt nền bằng **리눅스의 커널 로그 (Linux Kernel Logs)**, ta chuyển sang **소프트웨어 생명주기 모델 (SDLC Models)**. Đây là mắt xích 74/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **소프트웨어 생명주기 모델 (SDLC Models)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **폭포수 모델 (Waterfall)**, **프로토타입 모델 (Prototyping)**, **나선형 모델 (Spiral)**, **V 모델 (V Model)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “소프트웨어 생명주기 모델 (SDLC Models)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **폭포수 모델 (Waterfall)**: 각 단계를 명확히 마무리한 후 다음 단계로 넘어가는 선형 순차적 모델 (요구사항 변경 어려움).
- **프로토타입 모델 (Prototyping)**: 시제품(Prototype)을 만들어 최종 결과물을 예측.
- **나선형 모델 (Spiral)**: 점진적으로 개발하며 **위험 분석(Risk Analysis)** 기능을 추가한 대형 프로젝트용 모델.
- **V 모델 (V Model)**: 폭포수 모델에 테스트 단계를 세부적으로 추가하여 검증을 강화한 모델.

> **Vietnamese Explanation**:
> - **Waterfall (Thác nước)**: Làm xong bước này mới qua bước khác.
> - **Prototyping (Mẫu thử)**: Làm một bản nháp cho khách hàng xem trước.
> - **Spiral (Xoắn ốc)**: Làm từng phần và liên tục đánh giá rủi ro (Risk analysis).
> - **V Model (Chữ V)**: Nhấn mạnh vào việc kiểm thử (Testing) ở mỗi giai đoạn tương ứng.

Ta có thể khép mục **소프트웨어 생명주기 모델 (SDLC Models)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **스토리지 시스템 (Storage Systems)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **스토리지 시스템 (Storage Systems)** nối từ **소프트웨어 생명주기 모델 (SDLC Models)** sang **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 스토리지 시스템 (Storage Systems)

Từ **소프트웨어 생명주기 모델 (SDLC Models)**, ta đã có điểm tựa để bước vào **스토리지 시스템 (Storage Systems)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 75/86 trước khi đi vào chi tiết.

Để đọc **스토리지 시스템 (Storage Systems)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **DAS (Direct Attached Storage)**, **NAS (Network Attached Storage)**, **SAN (Storage Area Network)**, **DAS** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

대용량 데이터를 저장하기 위한 장치 구성 방식.
- **DAS (Direct Attached Storage)**: 서버와 스토리지를 전용 케이블로 **직접 연결**.
- **NAS (Network Attached Storage)**: 서버와 스토리지를 **네트워크(LAN)**로 연결.
- **SAN (Storage Area Network)**: 스토리지 전용 **광 채널 네트워크(FC-SAN)**를 별도로 구성하여 고속 전송.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **DAS**: Direct (Cắm trực tiếp).
- **NAS**: Network (Qua mạng LAN).
- **SAN**: Area Network (Mạng quang riêng tốc độ cao).

Điểm chốt của **스토리지 시스템 (Storage Systems)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **스토리지 시스템 (Storage Systems)** đặt đầu vào cho **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**, rồi **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)** mở rộng hệ quả liên quan.

## 1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)

Ở bước 76/86, **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** xuất hiện như phần tiếp nối của **스토리지 시스템 (Storage Systems)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **Tiếng Việt**, **예시 (Example)**, **대책** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 연속된 메모리 공간을 사용하는 프로그램에서 할당된 메모리의 범위를 넘어선 위치에서 자료를 읽거나 쓰려고 할 때 발생하는 취약점.
- **Tiếng Việt**: Lỗ hổng xảy ra khi chương trình ghi hoặc đọc dữ liệu vượt quá giới hạn vùng nhớ đã được cấp phát.
- **예시 (Example)**:
  - (KR) 10바이트 공간에 20바이트의 데이터를 입력하면 다른 메모리 영역을 침범함.
  - (VN) Nhập 20 byte dữ liệu vào mảng chỉ có kích thước 10 byte, làm ghi đè lên các vùng nhớ khác.
- **대책**: 버퍼의 크기를 적절히 설정.
- 💡 **Mẹo ghi nhớ**: Buffer Overflow = Bơm nước quá đầy làm tràn ly.

Như vậy, **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** đặt đầu vào cho **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)**, rồi **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)** mở rộng hệ quả liên quan.

## 2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)

Sau khi đã đặt nền bằng **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**, ta chuyển sang **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)**. Đây là mắt xích 77/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념**, **Tiếng Việt**, **예시 (Example)**, **대책** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 외부 입력값을 통해 시스템 명령어의 실행을 유도함으로써 권한을 탈취하거나 장애를 유발하는 취약점.
- **Tiếng Việt**: Chèn các lệnh hệ điều hành thông qua đầu vào của người dùng để thực thi trái phép trên server.
- **예시 (Example)**:
  - (KR) 웹 입력창에 `; rm -rf /` 와 같은 명령어를 삽입하여 서버 파일을 삭제.
  - (VN) Chèn lệnh `; rm -rf /` vào ô input trên web để xoá file trên máy chủ.
- **대책**: 외부 입력값을 검증 없이 내부 명령어로 사용하지 않음.

Ta có thể khép mục **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)** nối từ **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)** sang **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)

Từ **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)**, ta đã có điểm tựa để bước vào **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 78/86 trước khi đi vào chi tiết.

Để đọc **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **Tiếng Việt**, **예시 (Example)**, **대책** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 로그인 세션이나 쿠키가 남아 있는 사용자의 브라우저가 공격자가 의도한 상태 변경 요청을 보내도록 유도하는 취약점.
- **Tiếng Việt**: Lợi dụng phiên đăng nhập (session) hợp lệ của người dùng để thực hiện các yêu cầu không mong muốn.
- **예시 (Example)**:
  - (KR) 로그인된 상태에서 공격자가 보낸 링크를 클릭하면 내 계정에서 몰래 송금이 됨.
  - (VN) Khi đang đăng nhập ngân hàng, lỡ click vào link của hacker thì bị tự động chuyển tiền.
- **대책**: CSRF 토큰과 SameSite 쿠키를 사용하고, 서버에서 Origin/Referer와 인증 상태를 검증한다. POST만으로는 충분하지 않다.
- 💡 **Mẹo ghi nhớ**: C-S-R-F = Cứ Sợ Rằng Fake (Sợ người dùng thật nhưng gửi request fake).

Điểm chốt của **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)** dẫn sang **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** mở rộng hệ quả liên quan.

## 1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)

Ở bước 79/86, **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** xuất hiện như phần tiếp nối của **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념**, **Tiếng Việt**, **예시 (Example)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 널 포인터(값이 없는 메모리 주소)가 가리키는 메모리에 값을 저장하거나 읽을 때 발생하는 오류.
- **Tiếng Việt**: Lỗi xảy ra khi cố gắng đọc/ghi dữ liệu thông qua con trỏ đang có giá trị Null.
- **예시 (Example)**:
  - (KR) 객체가 생성되지 않았는데 그 객체의 메서드를 호출하여 시스템이 다운됨.
  - (VN) Gọi hàm của một đối tượng chưa được khởi tạo (bằng Null), làm app bị crash.

Như vậy, **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** nối từ **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** sang **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)

Sau khi đã đặt nền bằng **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**, ta chuyển sang **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**. Đây là mắt xích 80/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념**, **Tiếng Việt**, **예시 (Example)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 입력 길이·권한·오류 조건을 충분히 검증하지 않는 API를 사용하여 취약점을 만드는 것 (예: C언어의 `strcpy`, `strcat`).
- **Tiếng Việt**: Sử dụng các hàm không an toàn, dễ gây lỗi tràn bộ đệm (như `strcpy`).
- **예시 (Example)**:
  - (KR) 길이 제한이 없는 `strcpy()` 대신 입력 길이와 널 종료를 명시적으로 검증한다. `strncpy()`도 널 종료가 보장되지 않을 수 있으므로 무조건 안전한 대체재로 보지 않는다.
  - (VN) Dùng `strncpy()` (có giới hạn độ dài) thay cho `strcpy()` (copy không giới hạn).

---

Ta có thể khép mục **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** nối từ **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** sang **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)

Từ **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**, ta đã có điểm tựa để bước vào **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 81/86 trước khi đi vào chi tiết.

Để đọc **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các đoạn prose và thuật ngữ bên dưới cần được đọc như các bước trả lời cho câu hỏi đó.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Điểm chốt của **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** nối từ **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** sang **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)

Ở bước 82/86, **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** xuất hiện như phần tiếp nối của **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **대칭 키 (Symmetric Key)**, **비대칭 키 (Asymmetric Key)**, **Backdoor (백도어)**, **Key Logger (키로거)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **대칭 키 (Symmetric Key)**: 암호화 키 = 복호화 키 (비밀 키).
  - 속도가 빠름, 키 관리가 어려움 (Nhanh nhưng khó quản lý phân phối key).
  - 종류 (Các loại): DES, AES, SEED, ARIA, IDEA (Block); RC4, LFSR (Stream).
- **비대칭 키 (Asymmetric Key)**: 암호화 키(공개 키) ≠ 복호화 키(개인 키).
  - 속도가 느림, 키 분배 및 관리가 쉬움 (Chậm nhưng dễ phân phối key, an toàn).
  - 종류 (Các loại): RSA, ECC, Diffie-Hellman.
- 💡 **Mẹo ghi nhớ**:
  - 대칭 (Đại xưng) = 비밀 (Bí mật chung) -> AES, DES.
  - 비대칭 (Bất đại xưng) = 공개 (Công khai 1 nửa) -> RSA.

---

# 107 서비스 공격 기법 (Service Attack Techniques / Kỹ thuật tấn công dịch vụ)
Phần “107 서비스 공격 기법 (Service Attack Techniques / Kỹ thuật tấn công dịch vụ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Backdoor (백도어)**: 시스템 인증 절차를 우회하여 몰래 접속하는 경로 (Cửa sau, lách xác thực).
- **Key Logger (키로거)**: 키보드 입력 움직임을 탐지하여 비밀번호 등을 탈취 (Ghi lại thao tác bàn phím).
- **Rootkit (루트킷)**: 시스템 침입 사실을 숨기고 관리자 권한을 유지하는 도구 모음 (Bộ công cụ che giấu xâm nhập và giữ quyền admin).
- **Phishing, Smishing, Qshing (피싱, 스미싱, 큐싱)**: 이메일(Phishing), 문자(Smishing), QR코드(Qshing)로 개인정보 탈취 (Lừa đảo lấy thông tin qua mail, SMS, mã QR).
- **Zombie PC & Botnet (좀비 PC & 봇넷)**: 악성 봇에 감염되어 해커(C&C서버)의 명령에 따라 DDoS 공격 등을 수행하는 PC 무리 (Máy tính bị nhiễm bot, bị điều khiển hàng loạt).
- **Ransomware (랜섬웨어)**: 파일을 암호화하고 돈을 요구하는 악성 프로그램 (Mã độc tống tiền).
- **Zero Day Attack (제로데이 공격)**: 취약점이 공표되기도 전에 이루어지는 공격 (Tấn công ngay khi lỗ hổng vừa được phát hiện, chưa có bản vá).
- **Sniffing (스니핑)**: 네트워크 패킷을 몰래 엿보며 정보 수집 (Nghe lén gói tin trên mạng).
- **Spoofing (스푸핑 - IP, ARP)**: 위조된 IP나 MAC 주소로 속여 인증을 통과하거나 패킷을 가로챔 (Giả mạo địa chỉ IP hoặc MAC).
- **Session Hijacking (세션 하이재킹)**: 이미 로그인된 세션 정보를 가로채어 권한 획득 (Cướp phiên đăng nhập).
- 💡 **Mẹo ghi nhớ**: Spoof = 속이다 (Fake/Giả mạo), Sniff = 킁킁거리다 (Nghe lén/Trộm xem).

---

Như vậy, **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)** nối từ **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** sang **1. 인증 기술 (Authentication Types)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)

Sau khi đã đặt nền bằng **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)**, ta chuyển sang **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)**. Đây là mắt xích 83/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các đoạn prose và thuật ngữ bên dưới cần được đọc như các bước trả lời cho câu hỏi đó.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta có thể khép mục **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 인증 기술 (Authentication Types)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **1. 인증 기술 (Authentication Types)** nối từ **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)** sang **2. 접근 제어 정책 (Access Control Policies)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1. 인증 기술 (Authentication Types)

Từ **108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)**, ta đã có điểm tựa để bước vào **1. 인증 기술 (Authentication Types)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 84/86 trước khi đi vào chi tiết.

Để đọc **1. 인증 기술 (Authentication Types)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **지식 기반 (Knowledge)**, **소유 기반 (Possession)**, **생체 기반 (Biometric)**, **행위 기반 (Behavior)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 인증 기술 (Authentication Types)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **지식 기반 (Knowledge)**: 알고 있는 것 (Mật khẩu, mã PIN).
- **소유 기반 (Possession)**: 가지고 있는 것 (Token, Smart Card, OTP).
- **생체 기반 (Biometric)**: 고유한 신체 특징 (Vân tay, mống mắt).
- **행위 기반 (Behavior)**: 행동 특징 (Chữ ký, dáng đi).

Điểm chốt của **1. 인증 기술 (Authentication Types)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 접근 제어 정책 (Access Control Policies)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **2. 접근 제어 정책 (Access Control Policies)** nối từ **1. 인증 기술 (Authentication Types)** sang **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. 접근 제어 정책 (Access Control Policies)

Ở bước 85/86, **2. 접근 제어 정책 (Access Control Policies)** xuất hiện như phần tiếp nối của **1. 인증 기술 (Authentication Types)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 접근 제어 정책 (Access Control Policies)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **DAC (임의적 접근 통제 / Discretionary)**, **MAC (강제적 접근 통제 / Mandatory)**, **RBAC (역할 기반 접근 통제 / Role-Based)**, **방화벽 (Firewall)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 접근 제어 정책 (Access Control Policies)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DAC (임의적 접근 통제 / Discretionary)**: 신분(Identity) 기반. 데이터 소유자가 권한 부여.
- **MAC (강제적 접근 통제 / Mandatory)**: 보안등급(Label) 기반. 시스템 관리자가 강제로 권한 부여.
- **RBAC (역할 기반 접근 통제 / Role-Based)**: 역할(Role) 기반. 변경이 용이.
- 💡 **Mẹo ghi nhớ**: DAC = Danh tính, MAC = Mức độ bảo mật, RBAC = Role (Vai trò).

---

# 110 네트워크 보안 솔루션 (Network Security Solutions)
Phần “110 네트워크 보안 솔루션 (Network Security Solutions)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **방화벽 (Firewall)**: 트래픽 접근 허용/차단 (Tường lửa cơ bản).
- **WAF (웹 방화벽)**: SQL 인젝션, XSS 등 웹 특화 공격 방어 (Tường lửa chuyên cho Web).
- **IDS (침입 탐지 시스템)**: 침입을 실시간으로 "탐지(Detect)" (Hệ thống phát hiện xâm nhập).
- **IPS (침입 방지 시스템)**: 유해 트래픽을 실시간으로 "차단(Prevent)" (Hệ thống ngăn chặn xâm nhập).
- **VPN (가상사설망)**: 공중망을 전용망처럼 안전하게 사용 (Mạng riêng ảo).

---

Như vậy, **2. 접근 제어 정책 (Access Control Policies)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)**, **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)** nối từ **2. 접근 제어 정책 (Access Control Policies)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)

Sau khi đã đặt nền bằng **2. 접근 제어 정책 (Access Control Policies)**, ta chuyển sang **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)**. Đây là mắt xích 86/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **방법**, **합성 중심 (Composition-Based)**, **생성 중심 (Generation-Based)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 검증된 소프트웨어의 일부를 다시 사용 (Sử dụng lại các phần mềm đã được kiểm chứng để giảm chi phí, tăng chất lượng).
- **방법**:
  - **합성 중심 (Composition-Based)**: 블록 조립 (Lắp ráp các block như Lego).
  - **생성 중심 (Generation-Based)**: 추상적 명세로 코드 자동 생성 (Tự động sinh code từ bản đặc tả).

Khép lại **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)**, điều cần giữ lại là mối quan hệ giữa mục đích, cơ chế và điểm giới hạn của các khái niệm trong nguồn. Khi ôn lại, hãy tự giải thích chúng bằng một câu hoàn chỉnh rồi đối chiếu với các điểm dễ nhầm trước khi chuyển sang bài tổng hợp của môn.

> **Bàn giao:** Sau **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
