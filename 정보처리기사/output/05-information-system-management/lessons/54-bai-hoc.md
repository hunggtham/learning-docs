# 프로그래밍 언어의 분류 (Classification of Programming Languages)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **프로그래밍 언어의 분류 (Classification of Programming Languages)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối programming language classification với paradigm, type system, runtime và abstraction, để khác biệt gắn với cách thực thi.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **프로그래밍 언어의 분류 (Classification of Programming Languages)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **프로그래밍 언어의 분류 (Classification of Programming Languages)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **라이브러리 및 예외 처리 (Libraries and Exception Handling)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **프로그래밍 언어의 분류 (Classification of Programming Languages)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

프로그래밍, 언어의, 분류

> **Chuyển mạch:** Ở chặng này của **프로그래밍 언어의 분류 (Classification of Programming Languages)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **Python 제어문: while문 (While Loop)**에서 만든 기준을 이어받아 **프로그래밍 언어의 분류 (Classification of Programming Languages)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **프로그래밍 언어의 분류 (Classification of Programming Languages)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **프로그래밍 언어의 분류 (Classification of Programming Languages)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **프로그래밍 언어의 분류 (Classification of Programming Languages)**, **프로그래밍 언어의 분류 (Classification of Programming Languages)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 프로그래밍 언어의 분류 (Classification of Programming Languages)

Từ **Python 제어문: while문 (While Loop)**, ta đã có điểm tựa để bước vào **프로그래밍 언어의 분류 (Classification of Programming Languages)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/86 trước khi đi vào chi tiết.

Để đọc **프로그래밍 언어의 분류 (Classification of Programming Languages)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **C**, **ALGOL**, **COBOL**, **FORTRAN** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 절차적 프로그래밍 언어 (Procedural)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 절차적 프로그래밍 언어 (Procedural)

Các ý ngay dưới **1. 절차적 프로그래밍 언어 (Procedural)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

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

Các ý ngay dưới **4. 선언형 프로그래밍 언어 (Declarative)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

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

> **Bàn giao:** Sau **프로그래밍 언어의 분류 (Classification of Programming Languages)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
