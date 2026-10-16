# 객체지향 개념 및 SOLID 원칙 (Khái niệm Hướng đối tượng và 5 Nguyên tắc SOLID)

## 학습 목표 (Mục tiêu)
- Nắm vững các khái niệm nền tảng của Lập trình hướng đối tượng (`객체지향 - OOP`): Đối tượng (`객체`), Lớp (`클래스`), Thông điệp (`메시지`), Đóng gói (`캡슐화`), Kế thừa (`상속`), và Đa hình (`다형성`).
- Phân biệt tuyệt đối sự khác nhau về bản chất giữa Nạp chồng phương thức (`오버로딩 - Overloading`) và Ghi đè phương thức (`오버라이딩 - Overriding`).
- Thuộc nằm lòng thứ tự 3 bước của Phương pháp phân tích hướng đối tượng Rumbaugh (`객체 모델링 → 동적 모델링 → 기능 모델링`) bằng thần chú `객 - 동 - 기`.
- Làm chủ 5 nguyên tắc vàng trong thiết kế hướng đối tượng `SOLID` do Robert C. Martin đề xuất: `SRP` (Đơn trách nhiệm), `OCP` (Đóng/Mở), `LSP` (Thay thế Liskov), `ISP` (Phân tách giao diện), và `DIP` (Đảo ngược phụ thuộc) kèm các ví dụ mã nguồn thực tế.

## 핵심 키워드 (Từ khóa)
- 객체지향 (Object-Oriented Programming - OOP / 상태 + 행위)
- 캡슐화 및 정보 은닉 (Encapsulation & Information Hiding / 응집도↑, 결합도↓)
- 다형성 (Polymorphism / 오버로딩 vs 오버라이딩)
- 럼바우 분석 기법 (Rumbaugh OMT: 객체 모델링, 동적 모델링, 기능 모델링 / 객-동-기)
- 객체지향 5대 설계 원칙 (SOLID Principles)
- SRP (Single Responsibility Principle / 단일 책임 원칙 / 변경 이유 하나)
- OCP (Open-Closed Principle / 개방-폐쇄 원칙 / 확장 Open, 수정 Closed)
- LSP (Liskov Substitution Principle / 리스코프 치환 원칙 / 자식은 부모 대체 가능)
- ISP (Interface Segregation Principle / 인터페이스 분리 원칙 / 사용하지 않는 메서드 분리)
- DIP (Dependency Inversion Principle / 의존성 역전 원칙 / 추상화에 의존)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ [06-thiet-ke-kien-truc-va-chat-luong-phan-mem.md](06-thiet-ke-kien-truc-va-chat-luong-phan-mem.md), sau khi bộ khung kiến trúc tổng thể của hệ thống được xác lập, chúng ta cần phương pháp luận mô hình hóa từng thành phần và các nguyên tắc thiết kế mã nguồn chuẩn mực để bảo đảm tính mở rộng và khả năng bảo trì.
- **Đang giải quyết gì (Current Problem):** Bài học này trang bị tư duy Hướng đối tượng (OOP) và 5 nguyên tắc chỉ đạo thiết kế SOLID nhằm giải quyết triệt để vấn đề "Code bốc mùi" (Code Smells), sự phụ thuộc chặt chẽ giữa các lớp (Tight Coupling), và nguy cơ đổ vỡ hệ thống khi có yêu cầu thay đổi mới.
- **Dùng đi đâu (Forward Handoff):** Khi đã nắm vững tư duy đối tượng và các nguyên tắc SOLID, bước tiếp theo là phân tích sâu cấu trúc độc lập của từng module thông qua hai chỉ số định lượng then chốt: Coupling (Độ phụ thuộc) và Cohesion (Độ gắn kết nội tại). Kiến thức này chuyển giao trực tiếp sang [08-thiet-ke-module-coupling-cohesion.md](08-thiet-ke-module-coupling-cohesion.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng bảng phân biệt Overloading vs Overriding; thần chú Rumbaugh **Khách - Động - Cơ** (`객 - 동 - 기`); và 5 phát biểu tiếng Hàn kinh điển của bộ nguyên tắc SOLID.
- Đọc TẦNG B để phân tích ví dụ vi phạm nguyên tắc LSP (Bài toán Hình chữ nhật - Hình vuông) và cơ chế Tiêm phụ thuộc (Dependency Injection) hiện thực hóa nguyên tắc DIP.

---

## 객체지향 개념 및 SOLID 원칙

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các khái niệm cốt lõi của Lập trình hướng đối tượng (OOP)
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `객체지향(Object-Oriented)은 현실 세계의 개체(Entity)를 데이터와 이를 처리하는 함수를 하나로 묶은 객체(Object)로 모델링하여, 객체들 간의 상호작용을 통해 프로그램을 개발하는 패러다임이다.`
  - [Tiếng Việt]: Hướng đối tượng là mô hình lập trình xem thế giới thực là tập hợp các đối tượng độc lập, trong đó mỗi đối tượng đóng gói cả dữ liệu (trạng thái) lẫn hành vi (phương thức thao tác), và toàn bộ hệ thống hoạt động thông qua việc các đối tượng gửi thông điệp cho nhau.

- **6 Thành tố nền tảng của OOP:**
  1. `객체 (Object — Đối tượng)`: Là thực thể cụ thể gồm dữ liệu thuộc tính (`속성 / 상태 - Attribute/State`) và các hành vi thao tác trên dữ liệu đó (`메서드 / 연산 - Method/Operation`).
  2. `클래스 (Class — Lớp)`: Là bản thiết kế khuôn mẫu (`틀 / 청사진 - Blueprint`) định nghĩa các thuộc tính và phương thức chung. Đối tượng cụ thể được cấp phát bộ nhớ từ lớp gọi là **인스턴스 (Instance)**.
  3. `메시지 (Message — Thông điệp)`: Lời yêu cầu một đối tượng khác thực thi một phương thức cụ thể; gồm tên đối tượng nhận, tên phương thức và tham số truyền vào.
  4. `캡슐화 (Encapsulation — Đóng gói)`: Gom nhóm dữ liệu và phương thức xử lý vào trong cùng một đối tượng; kết hợp với `정보 은닉 (Information Hiding)` để bảo vệ dữ liệu nội bộ khỏi sự can thiệp trực tiếp từ bên ngoài.
  5. `상속 (Inheritance — Kế thừa)`: Lớp con (Subclass) tự động thừa hưởng toàn bộ thuộc tính và phương thức của lớp cha (Superclass); thúc đẩy tối đa khả năng **tái sử dụng mã nguồn (`재사용성`)**.
  6. `다형성 (Polymorphism — Đa hình)`: Cùng một tên thông điệp nhưng khi gửi đến các đối tượng thuộc các lớp khác nhau sẽ kích hoạt các hành vi xử lý hoàn toàn khác nhau.

- **Bảng phân biệt sống còn: Overloading vs Overriding:**

| Tiêu chí so sánh | 오버로딩 (Overloading — Nạp chồng) | 오버라이딩 (Overriding — Ghi đè) |
|:---|:---|:---|
| **Phạm vi áp dụng** | Xảy ra **trong cùng một lớp (Class)** | Xảy ra giữa **Lớp cha và Lớp con (Kế thừa)** |
| **Quy tắc tên phương thức** | **Trùng tên** phương thức | **Trùng tên** phương thức |
| **Quy tắc tham số** | **Bắt buộc KHÁC NHAU** về số lượng hoặc kiểu dữ liệu | **Bắt buộc GIỐNG NHAU HOÀN TOÀN** về danh sách tham số |
| **Quy tắc kiểu trả về** | Có thể giống hoặc khác nhau | **Bắt buộc GIỐNG NHAU** (hoặc kiểu đồng biến Subtype) |
| **Thời điểm quyết định** | **Compile-time** (Biên dịch tĩnh) | **Runtime** (Thời gian chạy động / Dynamic Dispatch) |

---

#### 2. Các phương pháp luận phân tích hướng đối tượng (OOA Methodologies)

##### A. Phương pháp Rumbaugh (OMT — Object Modeling Technique)
- Do James Rumbaugh phát triển, là phương pháp phân tích OOA xuất hiện nhiều nhất trong đề thi 정보처리기사.
- Phân tích hệ thống qua 3 mô hình theo trình tự bất di bất dịch:
  $$\text{객체 모델링 (Object)} \rightarrow \text{동적 모델링 (Dynamic)} \rightarrow \text{기능 모델링 (Functional)}$$
- **Mẹo ghi nhớ thần chú:** **객 - 동 - 기** (*Khách - Động - Cơ*).

| Thứ tự mô hình | Tên tiếng Hàn & Tiếng Anh | Biểu đồ sử dụng | Mục tiêu phân tích cốt lõi |
|:---:|:---|:---|:---|
| Thứ tự mô hình | Tên tiếng Hàn & Tiếng Anh | Biểu đồ sử dụng | Mục tiêu phân tích cốt lõi |
|:---:|:---|:---|:---|
| **Bước 1** | **객체 모델링** (Object Modeling — Mô hình đối tượng) | **ER 다이어그램 (ERD), 클래스 다이어그램** | **Quan trọng nhất, thực hiện đầu tiên**. Mô tả cấu trúc tĩnh của các đối tượng và mối quan hệ giữa chúng. |
| **Bước 2** | **동적 모델링** (Dynamic Modeling — Mô hình động) | **상태 다이어그램 (State Diagram)** | Mô tả sự biến đổi trạng thái, tương tác và chuỗi hành vi của đối tượng theo thời gian khi có sự kiện tác động. |
| **Bước 3** | **기능 모델링** (Functional Modeling — Mô hình chức năng) | **자료 흐름도 (DFD - Data Flow Diagram)** | Mô tả quá trình biến đổi dữ liệu đầu vào thành dữ liệu đầu ra qua các tiến trình tính toán. |

##### B. Các phương pháp OOA tiêu biểu khác
- `Coad와 Yourdon 방법`: Sử dụng biểu đồ E-R để mô hình hóa cấu trúc thực thể và quan hệ đối tượng.
- `Booch(부치) 방법`: Tiếp cận theo hai cấp độ: Quy trình vi mô (Micro process) và Quy trình vĩ mô (Macro process).
- `Wirfs-Brock(워프스-브록) 방법`: Tiếp cận theo hướng trách nhiệm (Responsibility-Driven Design), phân tích vai trò và trách nhiệm của từng lớp.
- `Jacobson(제이콥슨) 방법`: Phân tích định hướng trường hợp sử dụng (`Use Case-Driven`), lấy Use Case làm trung tâm xuyên suốt vòng đời.

---

#### 3. 5 Nguyên tắc vàng thiết kế hướng đối tượng SOLID
Do Robert C. Martin ("Uncle Bob") hệ thống hóa, là tiêu chuẩn vàng của ngành phần mềm để xây dựng hệ thống hướng đối tượng dễ bảo trì, dễ mở rộng và chống lại sự suy thoái kiến trúc.

##### A. SRP (Single Responsibility Principle — 단일 책임 원칙)
- **핵심 원리 (Mệnh đề thi tiếng Hàn):**
  - [Hàn/Anh]: `하나의 클래스는 단 하나의 책임만을 가져야 하며, 클래스가 변경되어야 하는 이유는 단 하나뿐이어야 한다.`
  - [Tiếng Việt]: Mỗi lớp chỉ nên đảm nhận một trách nhiệm duy nhất, và chỉ nên có một lý do duy nhất để thay đổi.
- **Ý nghĩa kỹ thuật:** Nếu một lớp vừa xử lý logic nghiệp vụ, vừa định dạng in báo cáo, vừa ghi dữ liệu vào CSDL, khi một trong ba yêu cầu thay đổi, toàn bộ lớp sẽ bị ảnh hưởng. Tách lớp này thành các lớp chuyên biệt sẽ tối đa hóa tính gắn kết nội tại (`응집도 향상`).

##### B. OCP (Open-Closed Principle — 개방-폐쇄 원칙)
- **핵심 원리 (Mệnh đề thi tiếng Hàn):**
  - [Hàn/Anh]: `소프트웨어 개체(클래스, 모듈, 함수 등)는 확장에 대해서는 열려(Open) 있어야 하지만, 수정에 대해서는 닫혀(Closed) 있어야 한다.`
  - [Tiếng Việt]: Một thực thể phần mềm phải **mở cho việc mở rộng tính năng mới (Open)**, nhưng phải **đóng trước việc sửa đổi mã nguồn hiện có (Closed)**.
- **Ý nghĩa kỹ thuật:** Khi cần thêm tính năng mới, ta chỉ cần tạo thêm lớp mới kế thừa hoặc hiện thực hóa giao diện (Interface) chung mà không cần sửa bất kỳ dòng mã nào trong các lớp cũ đã kiểm thử ổn định.

##### C. LSP (Liskov Substitution Principle — 리스코프 치환 원칙)
- **핵심 원리 (Mệnh đề thi tiếng Hàn):**
  - [Hàn/Anh]: `서브 타입(자식 클래스)은 언제나 자신의 기반 타입(부모 클래스)을 대체할 수 있어야 한다.`
  - [Tiếng Việt]: Lớp con phải có khả năng thay thế hoàn toàn cho lớp cha của nó mà không làm phá vỡ tính đúng đắn hay thay đổi hành vi kỳ vọng của chương trình.
- **Ý nghĩa kỹ thuật:** Lớp con không được phép vứt bỏ hay thay đổi ngữ nghĩa các phương thức của lớp cha (ví dụ: chim biết bay, nếu tạo lớp Chim cánh cụt kế thừa lớp Chim nhưng lại ném ngoại lệ ở phương thức `fly()` thì đã vi phạm nghiêm trọng nguyên tắc LSP).

##### D. ISP (Interface Segregation Principle — 인터페이스 분리 원칙)
- **핵심 원리 (Mệnh đề thi tiếng Hàn):**
  - [Hàn/Anh]: `클라이언트는 자신이 사용하지 않는 메서드에 의존하지 않아야 한다.`
  - [Tiếng Việt]: Một máy khách không bao giờ bị ép buộc phải phụ thuộc vào các phương thức trong giao diện mà nó không hề sử dụng.
- **Ý nghĩa kỹ thuật:** Thay vì tạo ra một giao diện "béo phì" (Fat/Monolithic Interface) chứa 50 phương thức dùng chung cho mọi đối tượng, hãy chia nhỏ thành nhiều giao diện chuyên biệt, hẹp và tinh gọn (Role Interfaces). Mỗi client chỉ `implements` đúng giao diện mà nó thực sự cần.

##### E. DIP (Dependency Inversion Principle — 의존성 역전 원칙)
- **핵심 원리 (Mệnh đề thi tiếng Hàn):**
  - [Hàn/Anh]: `고수준 모듈은 저수준 모듈에 의존해서는 안 되며, 둘 다 추상화에 의존해야 한다. 또한 추상화는 세부 사항에 의존해서는 안 되며, 세부 사항이 추상화에 의존해야 한다.`
  - [Tiếng Việt]: Các module cấp cao (quản lý chính sách nghiệp vụ) không được phụ thuộc trực tiếp vào các module cấp thấp (chi tiết kỹ thuật như cơ sở dữ liệu, cổng thanh toán); cả hai bắt buộc phải cùng phụ thuộc vào lớp trừu tượng (Interface).
- **Ý nghĩa kỹ thuật:** Hiện thực hóa thông qua kỹ thuật **Tiêm phụ thuộc (Dependency Injection - DI)**. Dịch vụ thanh toán `PaymentService` không trực tiếp khởi tạo `new KakaoPayClient()`, mà nó phụ thuộc vào giao diện `PaymentGateway`; khi muốn đổi sang `ApplePayClient`, mã nguồn của `PaymentService` hoàn toàn không cần sửa đổi.

---

#### 4. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (Thứ tự phương pháp Rumbaugh):** Đề thi trắc nghiệm đảo lộn thứ tự các bước trong OMT. Nhớ chắc chắn: **Bước 1 là 객체 (Object) $\rightarrow$ Bước 2 là 동적 (Dynamic) $\rightarrow$ Bước 3 là 기능 (Functional)** (Thần chú: **객 - 동 - 기**). Mô hình thực hiện đầu tiên và quan trọng nhất luôn là **객체 모델링**.
- **Bẫy 2 (Overloading vs Overriding):**
  - Cùng tên, khác tham số, cùng lớp, Compile-time $\rightarrow$ **오버로딩 (Overloading)**.
  - Cùng tên, cùng tham số, lớp cha-con, Runtime $\rightarrow$ **오버라이딩 (Overriding)**.
- **Bẫy 3 (Phân biệt 5 nguyên tắc SOLID):**
  - Gắn với từ khóa "Lớp chỉ có 1 lý do để thay đổi" $\rightarrow$ **SRP**.
  - Gắn với từ khóa "Mở cho mở rộng, đóng cho sửa đổi" $\rightarrow$ **OCP**.
  - Gắn với từ khóa "Lớp con thay thế hoàn hảo cho lớp cha" $\rightarrow$ **LSP**.
  - Gắn với từ khóa "Chia nhỏ giao diện lớn, không phụ thuộc hàm không dùng" $\rightarrow$ **ISP**.
  - Gắn với từ khóa "Phụ thuộc vào Interface trừu tượng, không phụ thuộc class cụ thể" $\rightarrow$ **DIP**.

- **💡 Khẩu quyết thần chú đề thi:**
  - 4 Trụ cột OOP: **캡-상-다-추** (캡슐화, 상속, 다형성, 추상화).
  - Rumbaugh OMT 3 bước: **객-동-기** (`객`체 모델링 $\rightarrow$ `동`적 모델링 $\rightarrow$ `기`능 모델링).
  - SOLID 5 nguyên tắc: **단-개-리-인-의** (`단`일 책임, `개`방-폐쇄, `리`스코프 치환, `인`터페이스 분리, `의`존성 역전).
  - Câu chốt ghi nhớ: "OOP gồm Đóng gói, Kế thừa, Đa hình, Trừu tượng; Rumbaugh ba bước Khách - Động - Cơ; SOLID giữ vững Đơn trách, Đóng mở, Liskov thay thế, Tách giao diện, Đảo ngược phụ thuộc".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Phân tích 4 Trụ cột Lập trình Hướng đối tượng (4 Pillars of OOP)

```text
               ┌─────────────────────────────────────────────────────────┐
               │           4 TRỤ CỘT HƯỚNG ĐỐI TƯỢNG (4 PILLARS)          │
               ├────────────────────────────┬────────────────────────────┤
               │ 1. 캡슐화 (Encapsulation)  │ 2. 상속성 (Inheritance)    │
               │ - Gom dữ liệu & hành vi    │ - Kế thừa lớp cha $\rightarrow$ con│
               │ - Che giấu thông tin nội bộ│ - Tái sử dụng mã nguồn     │
               ├────────────────────────────┼────────────────────────────┤
               │ 3. 다형성 (Polymorphism)   │ 4. 추상화 (Abstraction)    │
               │ - 1 thông điệp, đa hành vi │ - Trích xuất đặc trưng lõi │
               │ - Overloading / Overriding │ - Ẩn chi tiết triển khai   │
               └────────────────────────────┴────────────────────────────┘
```

1. **캡슐화 (Encapsulation - Đóng gói):**
   - Đóng gói thuộc tính (State) và phương thức (Behavior) vào chung trong một đơn vị đối tượng độc lập.
   - Kết hợp với `정보 은닉 (Information Hiding)` thông qua các phạm vi truy cập (`private`, `protected`, `public`) để bảo vệ dữ liệu nội tại, ngăn chặn truy cập trái phép từ bên ngoài, giúp hệ thống đạt chuẩn "Gắn kết cao, Phụ thuộc thấp" (`응집도↑, 결합도↓`).
2. **상속성 (Inheritance - Kế thừa):**
   - Cho phép lớp con (`자식 클래스 / 서브 클래스`) tái sử dụng toàn bộ cấu trúc thuộc tính và phương thức của lớp cha (`부모 클래스 / 슈퍼 클래스`).
   - Thúc đẩy việc tái sử dụng phần mềm (`소프트웨어 재사용성`), tránh trùng lặp mã nguồn và tạo nền tảng thiết lập quan hệ gia đình (IS-A relationship).
3. **다형성 (Polymorphism - Đa hình):**
   - Cùng một tên thông điệp gửi đến các đối tượng thuộc các kiểu dữ liệu khác nhau sẽ kích hoạt phương thức xử lý chuyên biệt tương ứng.
   - Hiện thực hóa qua hai cơ chế: Nạp chồng (`오버로딩` - tĩnh, tại thời điểm biên dịch) và Ghi đè (`오버라이딩` - động, tại thời điểm thực thi nhờ Dynamic Method Dispatch).
4. **추상화 (Abstraction - Trừu tượng hóa):**
   - Quá trình tập trung vào các đặc tính bản chất cốt lõi của một thực thể trong thế giới thực và bỏ qua các chi tiết kỹ thuật phức tạp không cần thiết ở cấp độ hiện tại.
   - Ba cấp độ trừu tượng hóa kinh điển: Trừu tượng hóa quá trình (`과정 추상화`), Trừu tượng hóa dữ liệu (`데이터 추상화`), và Trừu tượng hóa điều khiển (`제어 추상화`).

#### 2. So sánh đối chiếu toàn diện 5 Nguyên tắc SOLID qua Ví dụ Code thực chiến

##### A. SRP (Single Responsibility Principle)
- **Vi phạm SRP:**
  ```java
  class UserService {
      public void registerUser(String email, String password) {
          // 1. Logic nghiệp vụ tạo User
          User user = new User(email, password);
          // 2. Vi phạm: Chứa trực tiếp mã truy vấn CSDL
          String sql = "INSERT INTO users VALUES ('" + email + "')";
          database.execute(sql);
          // 3. Vi phạm: Chứa trực tiếp logic gửi email
          EmailClient.send(email, "Chào mừng bạn!");
      }
  }
  ```
- **Tuân thủ SRP:**
  ```java
  class UserService {
      private final UserRepository userRepository;
      private final NotificationService notificationService;
      public UserService(UserRepository repo, NotificationService noti) {
          this.userRepository = repo;
          this.notificationService = noti;
      }
      public void registerUser(String email, String password) {
          User user = new User(email, password);
          userRepository.save(user); // Chỉ điều phối nghiệp vụ
          notificationService.sendWelcome(user);
      }
  }
  ```

##### B. OCP (Open-Closed Principle)
- **Vi phạm OCP (Dùng if-else/switch dựa trên loại hình cụ thể):**
  ```java
  class AreaCalculator {
      public double calculateArea(Object shape) {
          if (shape instanceof Circle) {
              Circle c = (Circle) shape;
              return Math.PI * c.radius * c.radius;
          } else if (shape instanceof Rectangle) {
              Rectangle r = (Rectangle) shape;
              return r.width * r.height;
          }
          // Mỗi khi thêm hình mới (Tam giác, Hình thang) -> Bắt buộc phải SỬA hàm calculateArea!
          return 0;
      }
  }
  ```
- **Tuân thủ OCP (Sử dụng Interface trừu tượng):**
  ```java
  interface Shape {
      double getArea();
  }
  class Circle implements Shape {
      private double radius;
      public double getArea() { return Math.PI * radius * radius; }
  }
  class Rectangle implements Shape {
      private double width, height;
      public double getArea() { return width * height; }
  }
  // Khi cần thêm Triangle, chỉ cần tạo: class Triangle implements Shape
  // Lớp AreaCalculator hoàn toàn KHÔNG CẦN CHỈNH SỬA MÃ NGUỒN CŨ!
  class AreaCalculator {
      public double calculateArea(Shape shape) { return shape.getArea(); }
  }
  ```

##### C. LSP (Liskov Substitution Principle)
- **Bài toán kinh điển vi phạm LSP: Hình chữ nhật vs Hình vuông:**
  ```java
  class Rectangle {
      protected int width, height;
      public void setWidth(int w) { this.width = w; }
      public void setHeight(int h) { this.height = h; }
      public int getArea() { return width * height; }
  }
  class Square extends Rectangle {
      @Override
      public void setWidth(int w) { this.width = w; this.height = w; }
      @Override
      public void setHeight(int h) { this.width = h; this.height = h; }
  }
  ```
- **Hậu quả vi phạm LSP:**
  ```java
  void verifyRectangle(Rectangle r) {
      r.setWidth(5);
      r.setHeight(4);
      // Kết quả kỳ vọng: 5 * 4 = 20.
      // Nếu r là Rectangle: getArea() == 20 (Đúng).
      // Nhưng nếu r là Square: getArea() == 16 (Sai logic hoàn toàn!).
      assert r.getArea() == 20;
  }
  ```
- **Cách giải quyết tuân thủ LSP:** Tách cả hai thành hai lớp độc lập cùng hiện thực hóa giao diện chung `Shape`, không gượng ép `Square extends Rectangle`.

##### D. ISP (Interface Segregation Principle)
- **Vi phạm ISP (Giao diện béo phì Fat Interface):**
  ```java
  interface MultiFunctionDevice {
      void print();
      void scan();
      void fax();
  }
  class BasicPrinter implements MultiFunctionDevice {
      public void print() { System.out.println("Đang in văn bản..."); }
      // Vi phạm: Bị ép cài đặt các phương thức không hỗ trợ!
      public void scan() { throw new UnsupportedOperationException(); }
      public void fax() { throw new UnsupportedOperationException(); }
  }
  ```
- **Tuân thủ ISP (Phân tách thành các giao diện vai trò hẹp):**
  ```java
  interface Printer { void print(); }
  interface Scanner { void scan(); }
  interface Fax { void fax(); }

  // Máy in cơ bản chỉ cần cài đặt đúng Printer
  class BasicPrinter implements Printer {
      public void print() { System.out.println("Đang in văn bản..."); }
  }
  // Máy đa chức năng cao cấp cài đặt cả 3 giao diện
  class AdvancedAllInOne implements Printer, Scanner, Fax {
      public void print() { /* in */ }
      public void scan() { /* quét */ }
      public void fax() { /* fax */ }
  }
  ```

##### E. DIP (Dependency Inversion Principle)
- **Vi phạm DIP (Module cấp cao phụ thuộc trực tiếp vào Module cấp thấp):**
  ```java
  class OrderService {
      // Vi phạm: Gắn chặt vào lớp cụ thể MySQLDatabase
      private MySQLDatabase db = new MySQLDatabase();
      public void processOrder(Order o) { db.save(o); }
  }
  ```
- **Tuân thủ DIP (Cả hai phụ thuộc vào Interface trừu tượng qua Dependency Injection):**
  ```java
  interface Database {
      void save(Order o);
  }
  // Module cấp thấp hiện thực hóa Interface
  class MySQLDatabase implements Database { public void save(Order o) { /* SQL */ } }
  class MongoDatabase implements Database { public void save(Order o) { /* NoSQL */ } }

  // Module cấp cao chỉ phụ thuộc vào Interface trừu tượng
  class OrderService {
      private final Database database;
      public OrderService(Database database) { // Tiêm phụ thuộc qua Constructor
          this.database = database;
      }
      public void processOrder(Order o) {
          database.save(o); // Độc lập hoàn toàn với loại CSDL cụ thể
      }
  }
  ```

---

### 복습 체크리스트
- [ ] Định nghĩa được 6 khái niệm OOP: 객체 (Đối tượng), 클래스 (Lớp), 메시지 (Thông điệp), 캡슐화 (Đóng gói), 상속 (Kế thừa), 다형성 (Đa hình).
- [ ] Phân biệt rõ sự khác nhau giữa 오버로딩 (Overloading - cùng lớp, khác tham số) và 오버라이딩 (Overriding - kế thừa cha con, ghi đè).
- [ ] Đọc vanh vách thần chú Rumbaugh OMT theo đúng thứ tự: 객체 모델링 (ERD/Class) $\rightarrow$ 동적 모델링 (State) $\rightarrow$ 기능 모델링 (DFD).
- [ ] Nhớ tên các tác giả OOA khác: Coad-Yourdon (E-R), Booch (Micro/Macro), Jacobson (Use Case).
- [ ] Nhận diện chuẩn xác 5 nguyên tắc SOLID qua các câu trắc nghiệm tình huống:
  - SRP: Một lớp chỉ có 1 lý do để thay đổi.
  - OCP: Mở rộng tính năng mới, đóng sửa đổi code cũ.
  - LSP: Lớp con thay thế hoàn hảo cho lớp cha.
  - ISP: Chia nhỏ giao diện, không ép dùng phương thức thừa.
  - DIP: Cả cấp cao và cấp thấp đều phụ thuộc vào Interface trừu tượng.
- [ ] Giải thích được tại sao bài toán Hình vuông kế thừa Hình chữ nhật lại vi phạm LSP.
