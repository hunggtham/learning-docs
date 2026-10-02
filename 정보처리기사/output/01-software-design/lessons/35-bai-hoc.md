# 8. 디자인 패턴 (Design Patterns)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **8. 디자인 패턴 (Design Patterns)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối software configuration với version, environment, dependency và reproducibility, để thay đổi có thể truy nguyên.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **8. 디자인 패턴 (Design Patterns)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **8. 디자인 패턴 (Design Patterns)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. 디자인 패턴 (Design Patterns - GoF)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **8. 디자인 패턴 (Design Patterns)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

디자인, 패턴

> **Chuyển mạch:** Ở chặng này của **8. 디자인 패턴 (Design Patterns)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**에서 만든 기준을 이어받아 **8. 디자인 패턴 (Design Patterns)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **8. 디자인 패턴 (Design Patterns)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. 디자인 패턴 (Design Patterns)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **8. 디자인 패턴 (Design Patterns)**, **8. 디자인 패턴 (Design Patterns)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 8. 디자인 패턴 (Design Patterns)

Sau khi đã đặt nền bằng **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**, ta chuyển sang **8. 디자인 패턴 (Design Patterns)**. Đây là mắt xích 35/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. 디자인 패턴 (Design Patterns)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **디자인 패턴 (Design Pattern) 개요**. Hãy xác định **디자인 패턴 (Design Pattern) 개요** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 디자인 패턴 (Design Pattern) 개요

Phần nguồn của **디자인 패턴 (Design Pattern) 개요** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “디자인 패턴 (Design Pattern) 개요” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 세부적인 구현 방안을 설계할 때 참조할 수 있는 전형적인 해결 방식 또는 예제를 의미한다. (Là những phương pháp giải quyết hoặc ví dụ điển hình có thể tham khảo khi thiết계 chi tiết phương án triển khai.)
- 3가지 유형 (3 Loại chính): 생성 패턴 (Creational), 구조 패턴 (Structural), 행위 패턴 (Behavioral).

Các ý về **디자인 패턴 (Design Pattern) 개요** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **디자인 패턴 (Design Pattern) 개요** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại

Các ý ngay dưới **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 객체 생성과 관련된 패턴. (Liên quan đến việc tạo đối tượng.)
- **빌더 (Builder):** 작게 분리된 인스턴스를 건축하듯이 조합하여 객체를 생성함. (Tạo đối tượng bằng cách lắp ráp các phần nhỏ như xây nhà.)
- **팩토리 메소드 (Factory Method):** 객체 생성을 서브 클래스에서 처리하도록 분리하여 캡슐화한 패턴으로, 가상 생성자(Virtual Constructor) 패턴이라고도 함. (Giao việc tạo đối tượng cho lớp con, còn gọi là Virtual Constructor).
- **프로토타입 (Prototype):** 원본 객체를 복제하는 방법으로 객체를 생성함. (Tạo đối tượng bằng cách copy/clone từ đối tượng gốc).
- **싱글톤 (Singleton):** 생성된 객체를 여러 프로세스가 동시에 참조할 수는 없음 (하나의 객체만 생성). (Đảm bảo chỉ có 1 instance duy nhất được tạo ra).
- **추상 팩토리 (Abstract Factory):** 서로 연관·의존하는 객체들의 그룹으로 생성하여 추상적으로 표현함. (Tạo ra một nhóm các đối tượng có liên quan với nhau thông qua interface).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **BFPSA** (Build - Fact - Pro - Sing - Ab): **Bạn Phải Phạt Sợ Ai**.

Các bullet của **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại**, đừng bắt đầu lại từ số không. **구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại

Bây giờ ta đi vào nội dung của **구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 클래스나 객체를 조합해 더 큰 구조를 만드는 패턴. (Kết hợp lớp/đối tượng thành cấu trúc lớn hơn).
- **어댑터 (Adapter):** 인터페이스를 다른 클래스가 재사용할 수 있도록 변환함. (Biến đổi interface để lớp khác dùng được, giống như cục sạc chuyển đổi điện).
- **브리지 (Bridge):** 서로가 독립적으로 확장할 수 있도록 구성함. (Tách phần trừu tượng và phần thực thi để cả 2 có thể phát triển độc lập).
- **컴포지트 (Composite):** 복합 객체와 단일 객체를 구분 없이 다루고자 할 때 사용함. (Xử lý đối tượng đơn lẻ và đối tượng phức hợp (nhóm) theo cùng một cách, cấu trúc cây).
- **데코레이터 (Decorator):** 부가적인 기능을 추가하기 위해 다른 객체들을 덧붙이는 방식으로 구현함. (Gắn thêm tính năng mới vào đối tượng có sẵn giống như trang trí).
- **퍼싸드 (Facade):** 복잡한 서브 클래스들을 피해 더 상위에 인터페이스를 구성함. (Tạo một interface cấp cao đơn giản để che giấu hệ thống con phức tạp bên dưới).
- **플라이웨이트 (Flyweight):** 가능한 한 인스턴스를 공유해서 사용함으로써 메모리를 절약하는 패턴. (Chia sẻ instance để tiết kiệm bộ nhớ, tái sử dụng những gì giống nhau).
- **프록시 (Proxy):** 접근이 어려운 객체와 여기에 연결하려는 객체 사이에서 인터페이스 역할을 수행하는 패턴. (Người đại diện, đứng giữa kiểm soát truy cập vào đối tượng thực).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ABCDFFP** (Ad - Bri - Com - Dec - Fac - Fly - Pro): **Anh Bán Cơm Đĩa Phải Phạt Phi**.

Các bullet của **구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại** vừa cho ta cách đặt câu hỏi. Bây giờ **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại

Phần nguồn của **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 객체 간의 상호작용이나 책임 분배에 대한 패턴. (Giao tiếp và phân bổ trách nhiệm giữa các đối tượng).
- **책임 연쇄 (Chain of Responsibility):** 요청을 한 객체가 처리하지 못하면 다음 객체로 넘어가는 형태. (Xử lý dây chuyền, ai làm được thì làm, không thì chuyển người tiếp theo).
- **커맨드 (Command):** 재이용하거나 취소할 수 있도록 요청에 필요한 정보를 저장함. (Đóng gói yêu cầu thành đối tượng, dễ dàng undo/redo).
- **인터프리터 (Interpreter):** 언어에 문법 표현을 정의함. (Định nghĩa ngữ pháp cho ngôn ngữ).
- **반복자 (Iterator):** 접근이 잦은 객체에 대해 동일한 인터페이스를 사용하도록 함. (Duyệt qua các phần tử của tập hợp mà không cần biết cấu trúc bên trong).
- **중재자 (Mediator):** 복잡한 상호 작용을 캡슐화하여 객체로 정의함. (Làm trung gian liên lạc giữa các đối tượng để giảm sự phụ thuộc chéo).
- **메멘토 (Memento):** 객체를 해당 시점의 상태로 돌릴 수 있는 기능을 제공, C + Z와 같은 되돌리기 기능을 개발할 때 주로 이용함. (Lưu trạng thái để khôi phục/Undo).
- **옵서버 (Observer):** 객체에 상속되어 있는 다른 객체들에게 변화된 상태를 전달함. (Một đối tượng thay đổi trạng thái, các đối tượng đăng ký theo dõi sẽ được thông báo - VD: Đăng ký kênh YouTube).
- **상태 (State):** 객체의 상태에 따라 동일한 동작을 다르게 처리해야 할 때 사용함. (Thay đổi hành vi khi trạng thái đối tượng thay đổi).
- **전략 (Strategy):** 동일한 계열의 알고리즘들을 상호 교환할 수 있게 정의함. (Đóng gói thuật toán để có thể thay đổi linh hoạt lúc runtime).
- **템플릿 메소드 (Template Method):** 하위 클래스에서 세부 처리를 구체화함. (Lớp cha định nghĩa khung thuật toán, lớp con implement chi tiết).
- **방문자 (Visitor):** 처리 기능을 분리하여 별도의 클래스로 구성함. (Tách logic xử lý khỏi cấu trúc dữ liệu, đối tượng Visitor đi "thăm" các phần tử để xử lý).

Các bullet của **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **8. 디자인 패턴 (Design Patterns)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **4. 디자인 패턴 (Design Patterns - GoF)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **8. 디자인 패턴 (Design Patterns)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
