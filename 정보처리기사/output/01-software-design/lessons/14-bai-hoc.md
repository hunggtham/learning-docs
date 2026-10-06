# 3. 모델링 및 UML (Mô hình hóa và UML)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **3. 모델링 및 UML (Mô hình hóa và UML)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối modeling với UML, abstraction và traceability, để mô hình làm cầu nối từ yêu cầu đến thiết kế.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **3. 모델링 및 UML (Mô hình hóa và UML)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **3. 모델링 및 UML (Mô hình hóa và UML)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **3. 모델링 및 UML (Mô hình hóa và UML)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

모델링, UML

> **Nối mạch:** Ở chặng này của **3. 모델링 및 UML (Mô hình hóa và UML)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 현행 시스템 파악 (Understanding Current System)**에서 만든 기준을 이어받아 **3. 모델링 및 UML (Mô hình hóa và UML)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **3. 모델링 및 UML (Mô hình hóa và UML)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **3. 모델링 및 UML (Mô hình hóa và UML)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **3. 모델링 및 UML (Mô hình hóa và UML)**, **3. 모델링 및 UML (Mô hình hóa và UML)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 3. 모델링 및 UML (Mô hình hóa và UML)

Sau khi đã đặt nền bằng **3. 현행 시스템 파악 (Understanding Current System)**, ta chuyển sang **3. 모델링 및 UML (Mô hình hóa và UML)**. Đây là mắt xích 14/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **3. 모델링 및 UML (Mô hình hóa và UML)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **013. UML (Unified Modeling Language)**. Hãy xác định **013. UML (Unified Modeling Language)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 013. UML (Unified Modeling Language)

Phần nguồn của **013. UML (Unified Modeling Language)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “013. UML (Unified Modeling Language)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 시스템 개발자와 고객 또는 개발자 상호 간의 의사소통이 원활하게 이루어지도록 표준화한 대표적인 객체지향 모델링 언어이다. (Là ngôn ngữ mô hình hóa hướng đối tượng tiêu biểu được chuẩn hóa để việc giao tiếp giữa nhà phát triển hệ thống và khách hàng, hoặc giữa các nhà phát triển với nhau diễn ra suôn sẻ.)
- 구성 요소 (Components): 사물 (Things - Sự vật), 관계 (Relationships - Mối quan hệ), 다이어그램 (Diagram - Biểu đồ).
- **Ví dụ (Example):** Khi xây nhà cần bản vẽ thiết kế (Blueprint). Khi làm phần mềm, dùng UML làm bản vẽ thiết kế chung để ai cũng hiểu.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **SQĐ** (Sự - Quan - Đa): **Sợ Quá Đi** (Sự vật - Quan hệ - Đa biểu đồ).

Các ý về **013. UML (Unified Modeling Language)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **013. UML (Unified Modeling Language)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 014. UML의 주요 관계 (Các mối quan hệ chính trong UML)

Các ý ngay dưới **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “014. UML의 주요 관계 (Các mối quan hệ chính trong UML)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 일반화 (Generalization) 관계: 하나의 사물이 다른 사물에 비해 더 일반적인지 구체적인지를 표현. (Thể hiện một sự vật là tổng quát hay cụ thể hơn sự vật khác - kế thừa).
- 의존 (Dependency) 관계: 필요에 의해 서로에게 영향을 주는 짧은 시간 동안만 연관을 유지하는 관계를 표현. (Thể hiện mối quan hệ phụ thuộc ngắn hạn, ảnh hưởng lẫn nhau khi cần thiết).
- 실체화 (Realization) 관계: 사물이 할 수 있거나 해야 하는 기능으로 서로를 그룹화 할 수 있는 관계를 표현. (Thể hiện mối quan hệ hiện thực hóa chức năng mà sự vật có thể/phải làm - interface).
- **Ví dụ (Example):** Động vật -> Chó, Mèo là mối quan hệ '일반화' (Generalization).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **NYT** (Nhất - Ý - Thực): **Như Ý Thật** (Nhất quát - Ý tồn - Thực thể).

Các ý về **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)**, đừng bắt đầu lại từ số không. **015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)

Bây giờ ta đi vào nội dung của **015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 클래스 다이어그램 (Class Diagram)
- 객체 다이어그램 (Object Diagram)
- 컴포넌트 다이어그램 (Component Diagram)
- 배치 다이어그램 (Deployment Diagram)
- 복합체 구조 다이어그램 (Composite Structure Diagram)
- 패키지 다이어그램 (Package Diagram)
- **Ví dụ (Example):** Class Diagram thể hiện cấu trúc tĩnh của hệ thống, giống như sơ đồ tổ chức của một công ty.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **LĐCBPG** (Lớp - Đối - Com - Bố - Phức - Gói): **Làm Được Có Bữa Phải Giỏi**. Các biểu đồ này thể hiện cấu trúc "Tĩnh" (정적).

Các ý về **015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)** vừa cho ta cách đặt câu hỏi. Bây giờ **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)

Phần nguồn của **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 유스케이스 다이어그램 (Use Case Diagram)
- 순차 다이어그램 (Sequence Diagram)
- 커뮤니케이션 다이어그램 (Communication Diagram)
- 상태 다이어그램 (State Diagram)
- 활동 다이어그램 (Activity Diagram)
- 상호작용 개요 다이어그램 (Interaction Overview Diagram)
- 타이밍 다이어그램 (Timing Diagram)
- **Ví dụ (Example):** Sequence Diagram thể hiện trình tự thời gian gửi tin nhắn (메시지) giữa các đối tượng (hành vi động).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **UTCTHTT** (Use - Trình - Com - Trạng - Hoạt - Tương - Time): **Uống Trà Chiều Thấy Hay Thật Tuyệt**. Các biểu đồ này thể hiện đặc tính "Động" (동적).

Các ý về **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **017. 스테레오 타입 (Stereotype)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **017. 스테레오 타입 (Stereotype)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 017. 스테레오 타입 (Stereotype)

Các ý ngay dưới **017. 스테레오 타입 (Stereotype)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “017. 스테레오 타입 (Stereotype)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- UML에서 표현하는 기본 기능 외에 추가적인 기능을 표현하기 위해 사용한다. (Dùng để biểu diễn các chức năng bổ sung ngoài chức năng cơ bản trong UML.)
- 길러멧(Guilemet)이라고 부르는 겹화살괄호(`<< >>`) 사이에 표현할 형태를 기술한다. (Viết hình thái muốn biểu diễn giữa cặp dấu ngoặc nhọn kép `<< >>` gọi là Guilemet.)
- **Ví dụ (Example):** `<<include>>` hoặc `<<extend>>` trong Use Case Diagram.

Các ý về **017. 스테레오 타입 (Stereotype)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **017. 스테레오 타입 (Stereotype)**, đừng bắt đầu lại từ số không. **018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)

Bây giờ ta đi vào nội dung của **018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 시스템과 상호작용을 하는 모든 외부 요소로, 사람이나 외부 시스템을 의미한다. (Là tất cả các yếu tố bên ngoài tương tác với hệ thống, có nghĩa là con người hoặc hệ thống bên ngoài.)
- 주액터 (Primary Actor): 시스템을 사용함으로써 이득을 얻는 대상으로, 주로 사람이 해당함. (Đối tượng nhận được lợi ích khi dùng hệ thống, chủ yếu là con người - ví dụ: Khách hàng.)
- 부액터 (Secondary Actor): 주액터의 목적 달성을 위해 시스템에 서비스를 제공하는 외부 시스템으로, 조직이나 기관 등이 될 수 있음. (Hệ thống bên ngoài cung cấp dịch vụ cho hệ thống để đạt mục đích của Primary Actor - ví dụ: Cổng thanh toán ngân hàng.)

Các ý về **018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)** vừa cho ta cách đặt câu hỏi. Bây giờ **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)

Phần nguồn của **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 액터 (Actor - Tác nhân)
- 객체 (Object - Đối tượng)
- 생명선 (Lifeline - Đường đời)
- 실행 상자 (Active Box - Hộp thực thi)
- 메시지 (Message - Thông điệp)
- **Ví dụ (Example):** Khi user (Actor) ấn nút mua hàng, một mũi tên (Message) sẽ được gửi đến Giỏ hàng (Object). Đường nét đứt sổ dọc xuống từ Giỏ hàng là 생명선 (Lifeline).

Các ý về **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Với **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **3. 모델링 및 UML (Mô hình hóa và UML)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **3. 모델링 및 UML (Mô hình hóa và UML)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
