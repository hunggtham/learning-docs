# GoF 23 디자인 패턴 (23 Mẫu thiết kế GoF chuẩn quốc tế)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm, bối cảnh ra đời và phân loại cấu trúc 3 nhóm của 23 Mẫu thiết kế kinh điển do Gang of Four (GoF) hệ thống hóa: Mẫu khởi tạo (`생성 패턴 - 5 mẫu`), Mẫu cấu trúc (`구조 패턴 - 7 mẫu`), và Mẫu hành vi (`행위 패턴 - 11 mẫu`).
- Làm chủ toàn bộ 5 mẫu khởi tạo: `Singleton, Factory Method, Abstract Factory, Builder, Prototype` cùng mục đích thiết kế và ví dụ áp dụng.
- Làm chủ toàn bộ 7 mẫu cấu trúc: `Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy` và nhận diện các bẫy so sánh thường gặp (Adapter vs Facade, Decorator vs Proxy).
- Làm chủ toàn bộ 11 mẫu hành vi, đặc biệt là các mẫu xuất hiện liên tục trong đề thi: `Observer, Strategy, Template Method, State, Command, Iterator, Mediator, Memento`.
- Xây dựng ma trận phản xạ nhận diện tức thì mẫu thiết kế tương ứng với tình huống bài toán đặt ra trong đề thi trắc nghiệm 정보처리기사.

## 핵심 키워드 (Từ khóa)
- GoF 디자인 패턴 (Gang of Four 23 Design Patterns / 생성 5개, 구조 7개, 행위 11개)
- 생성 패턴 (Creational: Abstract Factory, Builder, Factory Method, Prototype, Singleton)
- 구조 패턴 (Structural: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy)
- 행위 패턴 (Behavioral: Chain of Resp., Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor)
- 싱글톤 (Singleton / 유일한 인스턴스 보장 / 전역 접근)
- 팩토리 메소드 vs 추상 팩토리 (Factory Method vs Abstract Factory / 가상 생성자 vs 제품군 생성)
- 어댑터 vs 퍼사드 (Adapter - 인터페이스 변환 호환 vs Facade - 단순화된 통합 인터페이스)
- 데코레이터 vs 프록시 (Decorator - 기능 동적 확장 vs Proxy - 접근 제어 및 대리)
- 옵서버 (Observer / 1:N 알림 / Publish-Subscribe)
- 전략 vs 템플릿 메소드 (Strategy - 알고리즘 캡슐화 교체 vs Template Method - 골격 정의)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ các nguyên tắc [07-huong-doi-tuong-va-nguyen-ly-solid.md](07-huong-doi-tuong-va-nguyen-ly-solid.md) và thiết kế module [08-thiet-ke-module-coupling-cohesion.md](08-thiet-ke-module-coupling-cohesion.md), khi lập trình viên áp dụng các nguyên tắc này vào các bài toán thực tế phức tạp lặp đi lặp lại, cộng đồng kỹ nghệ đã đúc kết thành các giải pháp mẫu mực (Templates) đã được kiểm chứng qua thời gian: Mẫu thiết kế GoF.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp từ vựng chung (Common Vocabulary) và các giải pháp kiến trúc tối ưu để tái sử dụng mã nguồn, giảm thiểu tối đa sự phụ thuộc chặt chẽ giữa các đối tượng và cho phép hệ thống mở rộng linh hoạt mà không cần viết lại mã nguồn cốt lõi.
- **Dùng đi đâu (Forward Handoff):** Sau khi các đối tượng và module nội bộ được thiết kế chuẩn mực bằng các mẫu GoF, bước tiếp theo là kết nối các hệ thống con với nhau và tích hợp với các hệ thống bên ngoài. Toàn bộ kiến thức chuyển giao sang [10-giao-dien-va-middleware.md](10-giao-dien-va-middleware.md) để khảo sát kỹ thuật tích hợp EAI, ESB và các loại Middleware.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng bảng ma trận 23 mẫu phân theo 3 nhóm; thuộc 5 mẫu Creational và 7 mẫu Structural; nắm chắc các từ khóa đề thi kích hoạt nhận diện (ví dụ: `1:N 알림` $\rightarrow$ Observer; `인터페이스 호환` $\rightarrow$ Adapter; `단일 인스턴스` $\rightarrow$ Singleton).
- Đọc TẦNG B để phân biệt chi tiết các cặp mẫu dễ gây nhầm lẫn nhất (Factory Method vs Abstract Factory, Decorator vs Proxy, Strategy vs State) và bài toán mã nguồn mẫu.

---

## GoF 23 디자인 패턴

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Ma trận phân loại 23 Mẫu thiết kế GoF (Gang of Four)
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `GoF(Gang of Four) 디자인 패턴은 에리히 감마(Erich Gamma) 등 4명의 전문가가 객체지향 소프트웨어 설계에서 자주 발생하는 문제들의 재사용 가능한 모범 해결책을 정리한 것으로, 목적(Purpose)에 따라 생성(5개), 구조(7개), 행위(11개) 패턴으로 분류된다.`
  - [Tiếng Việt]: Mẫu thiết kế GoF là tập hợp 23 giải pháp chuẩn mực có khả năng tái sử dụng cao cho các vấn đề thường gặp trong thiết kế phần mềm hướng đối tượng, được phân loại theo mục đích thiết kế thành: 5 Mẫu khởi tạo (Creational), 7 Mẫu cấu trúc (Structural), và 11 Mẫu hành vi (Behavioral).

- **Bảng ma trận tổng hợp 23 Mẫu thiết kế GoF:**

| Nhóm mẫu (Mục đích) | Số lượng | Danh sách các mẫu thiết kế chuẩn (Tên tiếng Hàn & Anh) |
|:---|:---:|:---|
| **생성 패턴 (Creational Patterns)** — *Khởi tạo đối tượng linh hoạt* | **5개** | **Abstract Factory, Builder, Factory Method, Prototype, Singleton** |
| **구조 패턴 (Structural Patterns)** — *Kết hợp lớp & đối tượng* | **7개** | **Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy** |
| **행위 패턴 (Behavioral Patterns)** — *Tương tác & Phân chia thuật toán* | **11개** | **Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor** |

---

#### 2. Chi tiết 5 Mẫu Khởi tạo (생성 패턴 — Creational Patterns)

| Tên mẫu thiết kế | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Từ khóa nhận diện đề thi |
|:---|:---|:---|
| **Singleton** | `싱글톤` (Singleton) | **[Hàn/Anh]:** `어떤 클래스의 인스턴스가 오직 하나임을 보장하고, 이에 대한 전역적인 접근점을 제공하는 패턴.` — **[Tiếng Việt]:** Đảm bảo một lớp **chỉ có duy nhất một thể hiện (Instance)** trong toàn bộ vòng đời ứng dụng và cung cấp một điểm truy cập toàn cục tới nó (ví dụ: Trình quản lý kết nối CSDL, Logger). |
| **Factory Method** | `팩토리 메소드` (Factory Method) | **[Hàn/Anh]:** `객체 생성을 서브 클래스로 위임하여, 부모 클래스는 인스턴스화할 클래스를 미리 알 필요가 없게 하는 패턴 (가상 생성자 - Virtual Constructor).` — **[Tiếng Việt]:** Định nghĩa giao diện tạo đối tượng ở lớp cha, nhưng **để các lớp con tự quyết định khởi tạo lớp nào** cụ thể; lớp cha chỉ làm việc với lớp trừu tượng. |
| **Abstract Factory** | `추상 팩토리` (Abstract Factory) | **[Hàn/Anh]:** `구체적인 클래스를 명시하지 않고, 관련성이 있거나 독립적인 여러 객체들의 군(Family)을 생성하기 위한 인터페이스를 제공하는 패턴 (Kit).` — **[Tiếng Việt]:** Cung cấp giao diện để **khởi tạo cả một họ (Family) các đối tượng có liên quan chặt chẽ với nhau** mà không cần chỉ định tên lớp cụ thể (ví dụ: Bộ giao diện Windows vs Bộ giao diện macOS). |
| **Builder** | `빌더` (Builder) | **[Hàn/Anh]:** `복잡한 객체의 생성 과정과 표현 방법을 분리하여, 동일한 생성 절차에서 서로 다른 표현 결과를 만들 수 있게 하는 패턴.` — **[Tiếng Việt]:** Tách rời **quá trình xây dựng một đối tượng phức tạp nhiều thuộc tính** khỏi cấu trúc biểu diễn của nó, cho phép xây dựng từng bước và tạo ra nhiều biến thể khác nhau. |
| **Prototype** | `프로토타입` (Prototype) | **[Hàn/Anh]:** `원형(Prototype)이 되는 인스턴스를 복사(Clone)하여 새로운 객체를 생성하는 패턴.` — **[Tiếng Việt]:** Tạo ra các đối tượng mới bằng cách **sao chép (Clone / Nhân bản)** từ một đối tượng mẫu có sẵn thay vì khởi tạo mới tốn kém tài nguyên. |

---

#### 3. Chi tiết 7 Mẫu Cấu trúc (구조 패턴 — Structural Patterns)

| Tên mẫu thiết kế | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Từ khóa nhận diện đề thi |
|:---|:---|:---|
| **Adapter** | `어댑터` (Adapter) | **[Hàn/Anh]:** `호환성이 없는 인터페이스를 가진 클래스들이 함께 작동할 수 있도록 인터페이스를 변환해 주는 패턴 (Wrapper).` — **[Tiếng Việt]:** Đóng vai trò như đầu chuyển giắc cắm, **chuyển đổi giao diện của một lớp thành giao diện mà máy khách kỳ vọng**, giúp các thành phần không tương thích có thể làm việc trơn tru với nhau. |
| **Bridge** | `브리지` (Bridge) | **[Hàn/Anh]:** `구현부에서 추상화 계층을 분리하여, 두 계층이 독립적으로 변형되고 확장될 수 있도록 하는 패턴.` — **[Tiếng Việt]:** Tách rời **phần trừu tượng (Abstraction) khỏi phần hiện thực (Implementation)** bằng một cây cầu liên kết, giúp cả hai nhánh phát triển và biến đổi độc lập. |
| **Composite** | `컴포지트` (Composite) | **[Hàn/Anh]:** `객체들을 트리 구조로 구성하여 개별 객체와 복합 객체를 동일하게 다룰 수 있도록 하는 패턴 (Part-Whole).` — **[Tiếng Việt]:** Xây dựng cấu trúc cây phân cấp **Phần - Toàn thể (Part-Whole hierarchy)**, cho phép máy khách đối xử đồng nhất với một đối tượng lá đơn lẻ cũng như với cả một thư mục/nhánh cây đối tượng. |
| **Decorator** | `데코레이터` (Decorator) | **[Hàn/Anh]:** `객체에 동적으로 새로운 책임(기능)을 추가할 수 있게 하는 패턴으로, 서브클래스를 만드는 것보다 유연한 기능 확장을 제공한다.` — **[Tiếng Việt]:** **Bổ sung thêm chức năng cho đối tượng một cách linh hoạt trong thời gian chạy (Runtime)** bằng cách bọc đối tượng bên trong một vỏ trang trí (ví dụ: Thêm đường viền, thanh cuộn cho cửa sổ). |
| **Facade** | `퍼사드` (Facade) | **[Hàn/Anh]:** `복잡한 서브시스템의 인터페이스들을 모아 단순화된 고수준의 단일 통합 인터페이스를 제공하는 패턴.` — **[Tiếng Việt]:** Đóng vai trò như bàn tiếp tân, cung cấp một **giao diện duy nhất đơn giản hóa** che giấu đi sự phức tạp của hàng chục subsystem bên trong. |
| **Flyweight** | `플라이웨이트` (Flyweight) | **[Hàn/Anh]:** `크기가 작은 다수의 객체를 공유(Sharing)하여 메모리 사용량을 최소화하는 패턴.` — **[Tiếng Việt]:** Tối ưu hóa bộ nhớ bằng cách **chia sẻ chung các đối tượng nhỏ có nội dung giống nhau** thay vì tạo mới hàng ngàn lần (ví dụ: Ký tự chữ cái trong trình soạn thảo văn bản). |
| **Proxy** | `프록시` (Proxy) | **[Hàn/Anh]:** `실제 객체에 대한 접근을 제어하거나 대리자 역할을 수행하는 대리 객체를 제공하는 패턴.` — **[Tiếng Việt]:** Cung cấp một **đối tượng đại diện (Placeholder / Surrogate)** để kiểm soát việc truy cập, tải chậm (Lazy Loading), phân quyền hoặc gọi từ xa tới đối tượng thực. |

---

#### 4. Chi tiết 11 Mẫu Hành vi (행위 패턴 — Behavioral Patterns)

| Tên mẫu thiết kế | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Từ khóa nhận diện đề thi |
|:---|:---|:---|
| **Observer** | `옵서버` (Observer) | **[Hàn/Anh]:** `한 객체의 상태가 변하면 그 객체에 의존하는 모든 객체들에게 자동으로 통지가 전달되고 상태가 갱신되는 1:N 의존 관계를 정의하는 패턴 (Publish-Subscribe).` — **[Tiếng Việt]:** Mối quan hệ phụ thuộc 1:N (Xuất bản - Đăng ký); khi đối tượng chủ thể (Subject) thay đổi, **tất cả các Observer đăng ký theo dõi sẽ tự động nhận thông báo và cập nhật**. |
| **Strategy** | `전략` (Strategy) | **[Hàn/Anh]:** `동일 계열의 알고리즘들을 각각 캡슐화하여 상호 교환이 가능하도록 만들고, 클라이언트와 독립적으로 알고리즘을 변경할 수 있게 하는 패턴.` — **[Tiếng Việt]:** Đóng gói **các thuật toán nghiệp vụ có thể hoán đổi cho nhau** vào các lớp riêng biệt, cho phép máy khách tự do thay đổi thuật toán tại thời gian chạy (ví dụ: Chọn thuật toán tính tiền mặt, thẻ tín dụng, PayPal). |
| **Template Method** | `템플릿 메소드` (Template Method) | **[Hàn/Anh]:** `상위 클래스에서 알고리즘의 골격(전체 절차)을 정의하고, 구체적인 세부 단계는 서브클래스에서 재정의할 수 있도록 하는 패턴.` — **[Tiếng Việt]:** Lớp cha định nghĩa **khung xương tổng thể của thuật toán**, các lớp con kế thừa chỉ việc ghi đè (Override) các bước cụ thể mà không làm thay đổi cấu trúc luồng của thuật toán. |
| **Command** | `커맨드` (Command) | **[Hàn/Anh]:** `요청을 객체의 형태로 캡슐화하여 사용자가 매개변수화, 요청 큐, 작업 취소(Undo) 등을 지원할 수 있게 하는 패턴.` — **[Tiếng Việt]:** Đóng gói **một yêu cầu thao tác thành một đối tượng độc lập**, cho phép lưu lịch sử thao tác, hoàn tác (Undo/Redo), và xếp hàng đợi xử lý lệnh. |
| **State** | `상태` (State) | **[Hàn/Anh]:** `객체의 내부 상태가 변함에 따라 객체의 행동이 마치 클래스를 바꾸는 것처럼 스스로 변화하게 만드는 패턴.` — **[Tiếng Việt]:** Đóng gói các trạng thái thành các lớp riêng biệt; **hành vi của đối tượng sẽ tự động thay đổi khi trạng thái nội bộ thay đổi**. |
| **Iterator** | `반복자` (Iterator) | **[Hàn/Anh]:** `내부 표현 방식을 노출하지 않고 집합 객체의 원소들을 순차적으로 접근할 수 있는 방법을 제공하는 패턴.` — **[Tiếng Việt]:** Cung cấp cơ chế **duyệt tuần tự các phần tử của một tập hợp** mà không cần để lộ cấu trúc dữ liệu bên dưới (mảng, danh sách liên kết, cây). |
| **Mediator** | `중재자` (Mediator) | **[Hàn/Anh]:** `객체들 간의 상호작용을 캡슐화하여 결합도를 낮추고, 모든 상호작용이 중재자 객체를 통해서만 이루어지도록 하는 패턴.` — **[Tiếng Việt]:** Đóng vai trò như **trạm điều phối không lưu**, mọi đối tượng chỉ giao tiếp qua trung gian điều phối Mediator, triệt tiêu sự phụ thuộc chéo rối rắm giữa các đối tượng. |
| **Memento** | `메멘토` (Memento) | **[Hàn/Anh]:** `캡슐화를 위배하지 않고 객체의 내부 상태를 포착하여 외부에 저장해 둔 후, 나중에 원래 상태로 복구할 수 있게 하는 패턴.` — **[Tiếng Việt]:** Chụp và lưu trữ **trạng thái nội bộ của đối tượng tại một thời điểm** để sau này có thể khôi phục lại trạng thái cũ mà không vi phạm tính đóng gói. |
| **Chain of Responsibility** | `책임 연쇄` (Chain of Resp.) | **[Hàn/Anh]:** `요청을 처리할 수 있는 객체들이 연결되어 있을 때, 요청을 처리할 수 있는 객체를 만날 때까지 메시지를 체인을 따라 전달하는 패턴.` — **[Tiếng Việt]:** Chuyển giao yêu cầu dọc theo **một chuỗi các đối tượng xử lý** cho đến khi có một đối tượng phù hợp tiếp nhận và giải quyết nó. |
| **Visitor** | `비지터` (Visitor) | **[Hàn/Anh]:** `객체 구조의 요소들을 변경하지 않고도 그 요소들에 대해 새로운 연산을 정의할 수 있게 하는 패턴.` — **[Tiếng Việt]:** Cho phép **bổ sung các phép toán xử lý mới lên các phần tử của một cấu trúc đối tượng** mà không cần sửa đổi mã nguồn của các phần tử đó. |
| **Interpreter** | `인터프리터` (Interpreter) | **[Hàn/Anh]:** `문법을 위한 표현을 정의하고, 그 언어로 된 문장을 해석하는 해석기를 구현하는 패턴.` — **[Tiếng Việt]:** Định nghĩa biểu diễn ngữ pháp cho một ngôn ngữ và xây dựng bộ thông dịch để phân tích và thực thi các câu lệnh trong ngôn ngữ đó (ví dụ: Biểu thức chính quy Regex, bộ thông dịch SQL). |

---

#### 5. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (Phân loại nhóm mẫu):** Đề thi trắc nghiệm luôn hỏi *"Mẫu nào sau đây KHÔNG PHẢI là Mẫu cấu trúc (Structural Pattern)?"* $\rightarrow$ Đưa ra 3 mẫu Structural (Adapter, Bridge, Proxy) và 1 mẫu Creational (như **Singleton** hay **Builder**) hoặc Behavioral (như **Strategy**).
- **Bẫy 2 (Adapter vs Facade):**
  - Đổi giao diện không tương thích để hai bên làm việc được $\rightarrow$ **어댑터 (Adapter)**.
  - Gom hệ thống phức tạp lại thành một giao diện đơn giản duy nhất $\rightarrow$ **퍼사드 (Facade)**.
- **Bẫy 3 (Strategy vs Template Method):**
  - Đóng gói toàn bộ thuật toán hoán đổi linh hoạt qua Interface (Ủy quyền - Delegation) $\rightarrow$ **전략 (Strategy)**.
  - Lớp cha định nghĩa khung thuật toán, lớp con kế thừa ghi đè bước nhỏ (Kế thừa - Inheritance) $\rightarrow$ **템플릿 메소드 (Template Method)**.
- **Bẫy 4 (Observer):** Cứ thấy xuất hiện từ khóa "Mối quan hệ 1:N phụ thuộc", "Thay đổi trạng thái tự động báo tin", "Publish-Subscribe" $\rightarrow$ Chắc chắn là **옵서버 (Observer)**.

- **한 문장 설명 (Câu chốt ghi nhớ):** "Khởi tạo 5 mẫu nhớ kỹ Singleton-Builder-Prototype-Factory; Cấu trúc 7 mẫu nhớ giắc Adapter và mặt tiền Facade; Hành vi 11 mẫu nhớ đinh ninh Observer báo tin và Strategy chọn chiến thuật".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Phân biệt chuyên sâu các cặp mẫu dễ gây nhầm lẫn nhất

##### A. Factory Method vs Abstract Factory
- **Factory Method (팩토리 메소드):** Tập trung vào việc tạo ra **MỘT đối tượng đơn lẻ**. Sử dụng cơ chế kế thừa: Lớp con ghi đè phương thức factory để trả về một thể hiện cụ thể (Ví dụ: `PizzaStore` có phương thức `createPizza()` do `NYPizzaStore` và `ChicagoPizzaStore` ghi đè).
- **Abstract Factory (추상 팩토리):** Tập trung vào việc tạo ra **CẢ MỘT BỘ / HỌ CÁC ĐỐI TƯỢNG LIÊN QUAN (Product Family)**. Sử dụng cơ chế ủy quyền (Composition): Interface `GUIFactory` có phương thức `createButton()` và `createCheckbox()`; khi chọn `WinFactory` sẽ sinh ra cả nút và checkbox chuẩn Windows, khi chọn `MacFactory` sinh ra cả nút và checkbox chuẩn macOS.

##### B. Decorator vs Proxy
- **Decorator (데코레이터):** Mục đích cốt lõi là **Mở rộng thêm tính năng mới (Add Responsibilities)** cho đối tượng trong lúc chạy mà không cần sửa code cũ. Decorator bọc đối tượng gốc và bổ sung thêm hành vi (ví dụ: bọc thêm lớp bảo mật, thêm lớp nén dữ liệu).
- **Proxy (프록시):** Mục đích cốt lõi là **Kiểm soát quyền truy cập (Control Access)** vào đối tượng gốc. Proxy có cùng giao diện với đối tượng gốc, đóng vai trò như một người gác cổng (ví dụ: kiểm tra quyền người dùng trước khi cho phép gọi hàm, trì hoãn việc nạp dữ liệu ảnh dung lượng nặng - Virtual Proxy).

#### 2. Minh họa mã nguồn Mẫu Observer (Publish - Subscribe)
```java
// 1. Giao diện Người theo dõi (Observer)
interface Observer { void update(String news); }

// 2. Giao diện Chủ thể phát tin (Subject)
interface Subject {
    void registerObserver(Observer o);
    void notifyObservers();
}

// 3. Hiện thực hóa Chủ thể phát tin (Kênh tin tức)
class NewsChannel implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private String news;
    public void setNews(String news) {
        this.news = news;
        notifyObservers(); // Tự động phát tin cho toàn bộ 1:N subscriber!
    }
    public void registerObserver(Observer o) { observers.add(o); }
    public void notifyObservers() {
        for (Observer o : observers) o.update(news);
    }
}
```
Mô hình trên thể hiện sức mạnh của **Loose Coupling**: Kênh tin tức phát tin mà không cần biết các máy khách cụ thể là ai; bất kỳ đối tượng nào chỉ cần cài đặt `Observer` đều có thể đăng ký nhận tin tức tức thì.

#### 3. Bảng ma trận phân loại toàn diện 23 GoF Design Patterns và Hệ thống Mẹo ghi nhớ (Mnemonics)

##### A. Bảng ma trận 2 chiều phân loại GoF (Mục đích x Phạm vi áp dụng)
Trong công trình kinh điển của Gang of Four, 23 mẫu thiết kế được định vị chính xác theo 2 chiều kiến trúc: **Mục đích thiết kế (Purpose)** và **Phạm vi đối tượng xử lý (Scope)**:

| Phạm vi áp dụng (Scope) | 생성 패턴 (Creational - 5 mẫu) | 구조 패턴 (Structural - 7 mẫu) | 행위 패턴 (Behavioral - 11 mẫu) |
|:---|:---|:---|:---|
| **클래스 (Class Scope: Kế thừa tĩnh lúc biên dịch)** | Factory Method | Adapter (Class Adapter - Đa kế thừa) | Interpreter, Template Method |
| **객체 (Object Scope: Ủy quyền động lúc chạy)** | Abstract Factory, Builder, Prototype, Singleton | Adapter (Object Adapter), Bridge, Composite, Decorator, Facade, Flyweight, Proxy | Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Visitor |

*Điểm bẫy trắc nghiệm:* Đề thi trắc nghiệm thường hỏi mẫu nào áp dụng ở phạm vi **Lớp (Class Scope)**? Đáp án chỉ có 4 mẫu: **Factory Method, Adapter (Class), Interpreter, Template Method**. Toàn bộ 19 mẫu còn lại đều hoạt động ở phạm vi **Đối tượng (Object Scope)** thông qua con trỏ và quan hệ hợp thành/ủy quyền (Composition & Delegation).

##### B. Hệ thống Thần chú ghi nhớ tốc biến (Exam Mnemonics)
Để nhận diện ngay lập tức 23 mẫu thiết kế trong phòng thi trắc nghiệm mà không bị lẫn lộn giữa các nhóm, hãy áp dụng bộ thần chú chữ đầu chuẩn xác:

1. **생성 패턴 (Mẫu khởi tạo - 5 mẫu):** **빌 - 팩 - 프 - 싱 - 추** (*Build - Fact - Pro - Sing - Chu*)
   - **빌**더 (Builder): Xây dựng đối tượng phức tạp nhiều tham số qua từng bước (Step-by-step construction).
   - **팩**토리 메소드 (Factory Method): Ủy quyền quyết định khởi tạo lớp cụ thể cho các lớp con (Virtual Constructor).
   - **프**로토타입 (Prototype): Tạo đối tượng mới bằng cách sao chép nhân bản từ mẫu có sẵn (Clone/Copy).
   - **싱**글톤 (Singleton): Đảm bảo chỉ tồn tại duy nhất một thể hiện trong toàn hệ thống, cung cấp điểm truy cập toàn cục.
   - **추**상 팩토리 (Abstract Factory): Cung cấp giao diện tạo cả một bộ/họ sản phẩm liên quan (Kit/Product Family).

2. **구조 패턴 (Mẫu cấu trúc - 7 mẫu):** **어 - 브 - 컴 - 데 - 퍼 - 플 - 프** (*Eo - Beu - Keom - De - Peo - Peul - Peu*)
   - **어**댑터 (Adapter): Bộ chuyển đổi giao diện không tương thích thành tương thích theo mong đợi (Wrapper).
   - **브**리지 (Bridge): Xây cây cầu tách rời tầng trừu tượng (Abstraction) khỏi hiện thực (Implementation) để cả hai phát triển độc lập.
   - **컴**포지트 (Composite): Xây dựng cấu trúc cây Part-Whole, đối xử đồng nhất giữa đối tượng đơn lẻ và tập hợp phức hợp.
   - **데**코레이터 (Decorator): Bọc thêm vỏ để bổ sung tính năng mới linh hoạt trong thời gian chạy (Runtime Extension).
   - **퍼**사드 (Facade): Bàn tiếp tân cung cấp một giao diện đơn giản duy nhất che giấu sự phức tạp của hàng chục subsystem bên trong.
   - **플**라이웨이트 (Flyweight): Chia sẻ chung các đối tượng hạt mịn (Fine-grained) để tối ưu hóa bộ nhớ RAM.
   - **프**록시 (Proxy): Đối tượng đại diện đóng vai trò người gác cổng kiểm soát quyền truy cập, lazy loading hoặc gọi từ xa.

3. **행위 패턴 (Mẫu hành vi - 11 mẫu):** **책 - 커 - 인 - 반 - 중 - 메 - 옵 - 상 - 전 - 템 - 비** (*Chaek - Keo - In - Ban - Jung - Me - Op - Sang - Jeon - Tem - Bi*) hoặc mẹo tiếng Anh **CCII MMO SST V**:
   - **책**임 연쇄 (Chain of Responsibility): Chuyển tiếp yêu cầu dọc theo một chuỗi mắt xích cho đến khi có đối tượng xử lý.
   - **커**맨드 (Command): Đóng gói trọn vẹn yêu cầu thành một đối tượng độc lập (Hỗ trợ hàng đợi lệnh, ghi log và Undo/Redo).
   - **인**터프리터 (Interpreter): Xây dựng bộ thông dịch biểu diễn ngữ pháp ngôn ngữ đặc thù (như Regex, SQL Parser).
   - **반**복자 (Iterator): Cung cấp cơ chế duyệt tuần tự các phần tử của tập hợp mà không để lộ cấu trúc dữ liệu bên dưới.
   - **중**재자 (Mediator): Trạm điều phối trung tâm, các đối tượng chỉ tương tác qua nó để giảm thiểu tối đa coupling chéo hình mạng nhện.
   - **메**멘토 (Memento): Chụp và lưu snapshot trạng thái nội bộ của đối tượng để khôi phục lại khi cần mà không phá vỡ tính đóng gói.
   - **옵**서버 (Observer): Cơ chế 1:N Publish-Subscribe, khi chủ thể Subject thay đổi trạng thái thì toàn bộ Observer tự động nhận thông báo.
   - **상**태 (State): Đối tượng tự động thay đổi hành vi tương ứng khi trạng thái nội bộ bên trong nó biến đổi.
   - **전**략 (Strategy): Đóng gói các thuật toán nghiệp vụ cùng họ vào các lớp riêng biệt, cho phép hoán đổi thuật toán linh hoạt lúc chạy.
   - **템**플릿 메소드 (Template Method): Lớp cha định hình khung xương thuật toán tổng thể, các lớp con kế thừa chỉ ghi đè các bước con cụ thể.
   - **비**지터 (Visitor): Tách rời thuật toán xử lý khỏi cấu trúc dữ liệu, bổ sung phép toán mới mà không làm thay đổi các lớp phần tử.

---

### 복습 체크리스트
- [ ] Nhớ tên nhóm tác giả GoF và số lượng mẫu trong 3 nhóm: 생성 (5개), 구조 (7개), 행위 (11개) = tổng cộng 23 mẫu.
- [ ] Kể tên đủ 5 mẫu Creational: Abstract Factory, Builder, Factory Method, Prototype, Singleton.
- [ ] Kể tên đủ 7 mẫu Structural: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy.
- [ ] Phân biệt được sự khác nhau giữa Singleton (1 thể hiện duy nhất) và Prototype (nhân bản clone từ mẫu có sẵn).
- [ ] Phân biệt được Adapter (đổi giao diện tương thích) và Facade (giao diện đơn giản hóa cho hệ thống con).
- [ ] Giải thích được cơ chế hoạt động của Observer Pattern (1:N Publish-Subscribe).
- [ ] Phân biệt được Strategy (đóng gói thuật toán hoán đổi) và Template Method (lớp cha định khung, lớp con ghi đè bước nhỏ).
