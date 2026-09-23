# 8. 디자인 패턴 (Design Patterns)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **8. 디자인 패턴 (Design Patterns)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

디자인, 패턴

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 8. 디자인 패턴 (Design Patterns)

### 디자인 패턴 (Design Pattern) 개요
- 세부적인 구현 방안을 설계할 때 참조할 수 있는 전형적인 해결 방식 또는 예제를 의미한다. (Là những phương pháp giải quyết hoặc ví dụ điển hình có thể tham khảo khi thiết계 chi tiết phương án triển khai.)
- 3가지 유형 (3 Loại chính): 생성 패턴 (Creational), 구조 패턴 (Structural), 행위 패턴 (Behavioral).

### 생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại
- 객체 생성과 관련된 패턴. (Liên quan đến việc tạo đối tượng.)
- **빌더 (Builder):** 작게 분리된 인스턴스를 건축하듯이 조합하여 객체를 생성함. (Tạo đối tượng bằng cách lắp ráp các phần nhỏ như xây nhà.)
- **팩토리 메소드 (Factory Method):** 객체 생성을 서브 클래스에서 처리하도록 분리하여 캡슐화한 패턴으로, 가상 생성자(Virtual Constructor) 패턴이라고도 함. (Giao việc tạo đối tượng cho lớp con, còn gọi là Virtual Constructor).
- **프로토타입 (Prototype):** 원본 객체를 복제하는 방법으로 객체를 생성함. (Tạo đối tượng bằng cách copy/clone từ đối tượng gốc).
- **싱글톤 (Singleton):** 생성된 객체를 여러 프로세스가 동시에 참조할 수는 없음 (하나의 객체만 생성). (Đảm bảo chỉ có 1 instance duy nhất được tạo ra).
- **추상 팩토리 (Abstract Factory):** 서로 연관·의존하는 객체들의 그룹으로 생성하여 추상적으로 표현함. (Tạo ra một nhóm các đối tượng có liên quan với nhau thông qua interface).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **BFPSA** (Build - Fact - Pro - Sing - Ab): **Bạn Phải Phạt Sợ Ai**.

### 구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại
- 클래스나 객체를 조합해 더 큰 구조를 만드는 패턴. (Kết hợp lớp/đối tượng thành cấu trúc lớn hơn).
- **어댑터 (Adapter):** 인터페이스를 다른 클래스가 재사용할 수 있도록 변환함. (Biến đổi interface để lớp khác dùng được, giống như cục sạc chuyển đổi điện).
- **브리지 (Bridge):** 서로가 독립적으로 확장할 수 있도록 구성함. (Tách phần trừu tượng và phần thực thi để cả 2 có thể phát triển độc lập).
- **컴포지트 (Composite):** 복합 객체와 단일 객체를 구분 없이 다루고자 할 때 사용함. (Xử lý đối tượng đơn lẻ và đối tượng phức hợp (nhóm) theo cùng một cách, cấu trúc cây).
- **데코레이터 (Decorator):** 부가적인 기능을 추가하기 위해 다른 객체들을 덧붙이는 방식으로 구현함. (Gắn thêm tính năng mới vào đối tượng có sẵn giống như trang trí).
- **퍼싸드 (Facade):** 복잡한 서브 클래스들을 피해 더 상위에 인터페이스를 구성함. (Tạo một interface cấp cao đơn giản để che giấu hệ thống con phức tạp bên dưới).
- **플라이웨이트 (Flyweight):** 가능한 한 인스턴스를 공유해서 사용함으로써 메모리를 절약하는 패턴. (Chia sẻ instance để tiết kiệm bộ nhớ, tái sử dụng những gì giống nhau).
- **프록시 (Proxy):** 접근이 어려운 객체와 여기에 연결하려는 객체 사이에서 인터페이스 역할을 수행하는 패턴. (Người đại diện, đứng giữa kiểm soát truy cập vào đối tượng thực).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ABCDFFP** (Ad - Bri - Com - Dec - Fac - Fly - Pro): **Anh Bán Cơm Đĩa Phải Phạt Phi**.

### 행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại
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
