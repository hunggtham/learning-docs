# 202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối OOP techniques với abstraction, encapsulation, inheritance và polymorphism, để nguyên tắc dẫn tới thiết kế.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

객체지향, 기법, 주요, 원칙

> **Nối mạch:** Ở chặng này của **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**에서 만든 기준을 이어받아 **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**, **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)

Từ **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**, ta đã có điểm tựa để bước vào **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/91 trước khi đi vào chi tiết.

Để đọc **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **구성 요소**, **데이터 (Data/Attribute)**, **연산/메소드 (Method/Operation)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 현실 세계의 개체(Entity)를 기계 부품(Object)처럼 만들어 조립식으로 소프트웨어 개발. 재사용/확장 용이.
- **구성 요소**:
  - **데이터 (Data/Attribute)**: 객체가 가진 정보 (속성, 상태).
  - **연산/메소드 (Method/Operation)**: 데이터를 처리하는 알고리즘/함수.
  - **클래스 (Class)**: 공통 속성/연산을 갖는 객체들의 집합 (틀, Type). 객체를 '인스턴스(Instance)'라고 함.
  - **메시지 (Message)**: 객체 간 상호작용 수단 (명령).
- **주요 기본 원칙**:
  1. **캡슐화 (Encapsulation)**: 데이터와 함수를 하나로 묶음. 재사용 용이, 결합도 낮아짐.
  2. **정보 은닉 (Information Hiding)**: 내부 정보를 숨기고 연산만을 통해 접근 허용 (Side Effect 최소화).
  3. **상속성 (Inheritance)**: 상위 클래스의 속성/연산을 하위 클래스가 물려받음. (다중 상속도 있음).
  4. **추상화 (Abstraction)**: 불필요한 부분 생략, 중요한 부분만 모델화.
  5. **다형성 (Polymorphism)**: 동일한 메시지(메소드명)에 대해 객체마다 다른 응답(기능)을 함.

**Giải thích (Vietnamese):**
OOP (Lập trình hướng đối tượng) giống như trò chơi xếp hình Lego.
- Class: Bản vẽ thiết kế chiếc xe.
- Object (Instance): Chiếc xe thật được lắp ráp.
- Tính đóng gói (Encapsulation): Gói gọn các bộ phận động cơ vào trong vỏ xe.
- Tính đa hình (Polymorphism): Cùng là lệnh "Kêu", con chó kêu "Gâu", con mèo kêu "Meo".

**💡 Mẹo ghi nhớ (Mnemonics):**
**캡정상추다** (Đóng - Ẩn - Kế - Trừu - Đa): 캡슐화, 정보 은닉, 상속성, 추상화, 다형성.

---

Điểm chốt của **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
