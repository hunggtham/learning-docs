# UML 모델링 및 다이어그램 (Mô hình hóa UML và Hệ thống Biểu đồ)

## 학습 목표 (Mục tiêu)
- Nắm vững lịch sử chuẩn hóa, 3 thành tố cấu tạo (`사물, 관계, 다이어그램`) và vai trò của Ngôn ngữ mô hình hóa thống nhất (`UML - Unified Modeling Language`).
- Làm chủ 6 mối quan hệ cốt lõi trong UML: Liên kết (`연관`), Tập hợp (`집약`), Hợp thành (`합성`), Khái quát hóa (`일반화`), Phụ thuộc (`의존`), và Hiện thực hóa (`실체화`) cùng các ký hiệu hình học chuẩn xác.
- Thuộc nằm lòng các ký hiệu chỉ định quyền truy cập (`접근 제어자: +, -, #, ~`) và cấu trúc 3 ngăn tiêu chuẩn của một lớp trong Biểu đồ lớp (`클래스 다이어그램`).
- Phân biệt tuyệt đối giữa nhóm Biểu đồ cấu trúc tĩnh (`구조적 다이어그램 - 6 loại`) và nhóm Biểu đồ hành vi động (`행위적 다이어그램 - 7 loại`).
- Phân tích sâu 4 biểu đồ xuất hiện nhiều nhất trong đề thi trắc nghiệm: Biểu đồ Use Case (phân biệt quan hệ `<<include>>` bắt buộc vs `<<extend>>` tùy chọn), Biểu đồ tuần tự (Lifeline, Activation Bar, Message), Biểu đồ trạng thái, và Biểu đồ hoạt động (Fork - Join).

## 핵심 키워드 (Từ khóa)
- UML (Unified Modeling Language / 표준 객체 모델링 언어 / OMG / Three Amigos)
- 사물·관계·다이어그램 (3 thành tố UML: Things, Relationships, Diagrams)
- 연관·집약·합성 관계 (Association, Aggregation - 빈 마름모, Composition - 채워진 마름모)
- 일반화·의존·실체화 관계 (Generalization - 빈 삼각, Dependency - 점선 화살표, Realization)
- 접근 제어자 (Access Modifiers: `+` Public, `-` Private, `#` Protected, `~` Package)
- 구조적 다이어그램 (Structural Diagrams: Class, Object, Component, Deployment, Package, Composite)
- 행위적 다이어그램 (Behavioral Diagrams: Use Case, Activity, State, Sequence, Communication)
- 유스케이스 다이어그램 (Use Case: 시스템 경계, 액터, `<<include>>` vs `<<extend>>`)
- 순차 다이어그램 (Sequence Diagram / 생명선 - Lifeline / 실행 상자 - Activation / 동기·비동기)
- 포크 vs 조인 (Fork vs Join / 병렬 처리 분기 및 병합)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ [03-ky-nghe-va-dac-ta-yeu-cau.md](03-ky-nghe-va-dac-ta-yeu-cau.md), các kỹ thuật truyền thống như DFD hay DD chỉ biểu diễn luồng dữ liệu mà không thể hiện được tính đóng gói, quan hệ kế thừa và tương tác đối tượng trong lập trình hiện đại.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp ngôn ngữ thị giác chuẩn quốc tế UML để mô hình hóa toàn diện hệ thống phần mềm hướng đối tượng: từ cấu trúc tĩnh của các class, thuộc tính, quan hệ sở hữu cho đến luồng tương tác thông điệp theo thời gian thực và sự chuyển đổi trạng thái của từng đối tượng.
- **Dùng đi đâu (Forward Handoff):** Khi các biểu đồ tương tác người dùng (Use Case) và cấu trúc lớp đã hoàn tất, bước tiếp theo trong chu trình thiết kế là chuyển hóa các yêu cầu giao diện người dùng thành các màn hình thực tế. Kiến thức này bàn giao trực tiếp sang [05-thiet-ke-giao-dien-ui-ux.md](05-thiet-ke-giao-dien-ui-ux.md) để thiết kế giao diện UI/UX và tương tác người-máy HCI.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc làu bảng ký hiệu hình học của 6 mối quan hệ UML (hình thoi rỗng vs hình thoi đặc; tam giác rỗng liền vs tam giác rỗng đứt); 4 ký hiệu quyền truy cập; và phân loại chính xác 13 biểu đồ vào 2 nhóm Tĩnh vs Động.
- Đọc TẦNG B để hiểu sâu cơ chế sinh tử của Composition so với Aggregation, cách phân biệt chiều mũi tên của `<<include>>` và `<<extend>>`, và bài toán trace thông điệp trong Sequence Diagram.

---

## UML 모델링 및 다이어그램

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tổng quan về ngôn ngữ UML
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `UML(Unified Modeling Language)은 객체지향 소프트웨어 개발 과정에서 산출물을 명세화, 시각화, 문서화할 때 사용되는 표준 모델링 언어로, OMG(Object Management Group)에서 표준화하였다.`
  - [Tiếng Việt]: UML là ngôn ngữ mô hình hóa hướng đối tượng chuẩn quốc tế do tổ chức OMG chuẩn hóa, hợp nhất công trình của 3 nhà khoa học ("Three Amigos": Grady Booch, James Rumbaugh, Ivar Jacobson) nhằm mục đích đặc tả, trực quan hóa và lập hồ sơ tài liệu cho toàn bộ vòng đời phát triển phần mềm.
- **3 Thành tố cấu tạo của UML:**
  1. `사물 (Things)`: Các phần tử trừu tượng cốt lõi của mô hình (Cấu trúc: Class, Interface, Component, Node; Hành vi: Interaction, State machine; Nhóm: Package; Chú thích: Note).
  2. `관계 (Relationships)`: Các đường nối biểu diễn mối liên kết ngữ nghĩa giữa các sự vật.
  3. `다이어그램 (Diagrams)`: Các bản vẽ trực quan kết hợp sự vật và mối quan hệ để thể hiện một góc nhìn kiến trúc cụ thể.

---

#### 2. 6 Mối quan hệ cốt lõi trong UML (UML 6대 관계)

| Mối quan hệ | Tên tiếng Hàn & Tiếng Anh | Ký hiệu hình học nhận diện | Bản chất kỹ thuật & Ý nghĩa |
|:---|:---|:---:|:---|
| **Quan hệ liên kết** | `연관 관계 (Association)` | Đường nét liền mảnh (`───`), có thể có mũi tên 1 chiều (`──►`) | Thể hiện mối liên kết ngữ nghĩa lâu dài giữa hai lớp đối tượng. Có ghi số lượng tham gia (Multiplicity: `1`, `*`, `0..1`). |
| **Quan hệ tập hợp** | `집약 관계 (Aggregation)` | Đường nét liền gắn **Hình thoi rỗng** (`◇───`) ở phía lớp toàn thể (Whole) | Thể hiện quan hệ "Has-a", **Độc lập về vòng đời**. Khi lớp toàn thể bị hủy, lớp thành phần (Part) vẫn tồn tại độc lập (Ví dụ: Máy tính và Chuột rời). |
| **Quan hệ hợp thành** | `합성 관계 (Composition)` | Đường nét liền gắn **Hình thoi đặc / tô đen** (`◆───`) ở phía lớp toàn thể | Thể hiện quan hệ sở hữu chặt chẽ, **Gắn liền sinh tử**. Khi lớp toàn thể bị hủy, tất cả các lớp thành phần con bị hủy theo (Ví dụ: Nhà và Căn phòng). |
| **Quan hệ khái quát hóa** | `일반화 관계 (Generalization)` | Đường nét liền gắn **Tam giác rỗng** (`◁───`) trỏ về lớp cha | Thể hiện quan hệ **Kế thừa (Inheritance / "Is-a")**. Lớp con kế thừa toàn bộ thuộc tính và hành vi của lớp cha (Ví dụ: Ô tô kế thừa Phương tiện). |
| **Quan hệ phụ thuộc** | `의존 관계 (Dependency)` | **Đường nét đứt có mũi tên nhọn** (`- - - ►`) trỏ về đối tượng được dùng | Thể hiện quan hệ sử dụng tạm thời trong thời gian ngắn (`<<use>>`). Lớp A nhận lớp B làm tham số đầu vào trong một phương thức. |
| **Quan hệ hiện thực hóa** | `실체화 관계 (Realization)` | **Đường nét đứt gắn Tam giác rỗng** (`◁- - -`) trỏ về Interface | Lớp cụ thể cam kết cài đặt hiện thực toàn bộ các phương thức trừu tượng do Interface định nghĩa. |

---

#### 3. Biểu đồ lớp (Class Diagram) và Ký hiệu quyền truy cập

##### A. Ký hiệu quyền truy cập (접근 제어자 - Access Modifiers)
- `+` : **Public** — Truy cập tự do từ bất kỳ đâu bên ngoài lớp.
- `-` : **Private** — Chỉ có các phương thức nội bộ của chính lớp đó mới được phép truy cập.
- `#` : **Protected** — Chỉ lớp đó và các lớp con kế thừa từ nó mới được phép truy cập.
- `~` : **Package (Default)** — Tất cả các lớp nằm trong cùng một gói package mới được phép truy cập.

##### B. Cấu trúc 3 ngăn tiêu chuẩn của một Class
1. **Ngăn 1 (Tên lớp - Class Name):** In đậm ở trên cùng.
2. **Ngăn 2 (Thuộc tính - Attributes):** `[접근제어자] 속성명 : 자료형 [= 기본값]`
   - *Ví dụ:* `- balance : double = 0.0` (Thuộc tính Private `balance`, kiểu double, mặc định là 0.0).
3. **Ngăn 3 (Phương thức - Operations / Methods):** `[접근제어자] 메서드명(매개변수: 자료형) : 반환형`
   - *Ví dụ:* `+ deposit(amount: double) : boolean` (Phương thức Public `deposit`, nhận tham số amount, trả về boolean).

---

#### 4. Phân loại 13 biểu đồ UML (UML 2.x Diagrams)

##### A. Biểu đồ cấu trúc tĩnh (구조적 다이어그램 - Structural Diagrams / 6 loại)
1. `클래스 다이어그램 (Class Diagram)`: Biểu diễn cấu trúc tĩnh gồm các lớp, thuộc tính, phương thức và các mối quan hệ giữa chúng. Là biểu đồ được dùng nhiều nhất.
2. `객체 다이어그램 (Object Diagram)`: Biểu diễn các thể hiện đối tượng cụ thể (Instance) tại một thời điểm nhất định trong thời gian chạy.
3. `컴포넌트 다이어그램 (Component Diagram)`: Biểu diễn các thành phần module mã nguồn, thư viện, file thực thi và mối quan hệ phụ thuộc giữa chúng.
4. `배포 다이어그램 (Deployment Diagram)`: Biểu diễn cấu trúc triển khai vật lý của hệ thống: các nút phần cứng (Node), máy chủ, thiết bị mạng và vị trí đặt các component.
5. `패키지 다이어그램 (Package Diagram)`: Biểu diễn cấu trúc gom nhóm logic các phần tử mô hình theo các gói phân cấp.
6. `복합체 구조 다이어그램 (Composite Structure Diagram)`: Biểu diễn cấu trúc bên trong của một lớp phức hợp và các cổng kết nối (Port).

##### B. Biểu đồ hành vi động (행위적 다이어그램 - Behavioral Diagrams / 7 loại)
1. `유스케이스 다이어그램 (Use Case Diagram)`: Biểu diễn các chức năng của hệ thống dưới góc nhìn của người dùng bên ngoài.
2. `활동 다이어그램 (Activity Diagram)`: Biểu diễn luồng công việc (Workflow) và các bước xử lý nghiệp vụ tuần tự hoặc song song.
3. `상태 머신 다이어그램 (State Machine Diagram)`: Biểu diễn toàn bộ vòng đời và các trạng thái chuyển tiếp của MỘT đối tượng khi có sự kiện tác động.
4. **Nhóm biểu đồ tương tác (Interaction Diagrams - 4 loại):**
   - `순차 다이어그램 (Sequence Diagram)`: Biểu diễn tương tác giữa các đối tượng theo **thứ tự thời gian (시간 순서)**.
   - `통신 다이어그램 (Communication Diagram)`: Biểu diễn tương tác tập trung vào cấu trúc liên kết và thông điệp trao đổi giữa các đối tượng.
   - `타이밍 다이어그램 (Timing Diagram)`: Biểu diễn sự thay đổi trạng thái của đối tượng theo thang thời gian thực chính xác.
   - `상호작용 개요 다이어그램 (Interaction Overview Diagram)`: Kết hợp giữa Activity Diagram và các đoạn Sequence Diagram con.

---

#### 5. Chi tiết các biểu đồ trọng tâm thi trắc nghiệm

##### A. Biểu đồ trường hợp sử dụng (Use Case Diagram)
- **4 Thành phần cốt lõi:**
  - `시스템 범위 (System Boundary)`: Khung chữ nhật bao quanh toàn bộ các Use Case của hệ thống.
  - `액터 (Actor)`: Thực thể bên ngoài tương tác với hệ thống (Người dùng, Hệ thống ngoài, Thiết bị). Gồm Tác nhân chính (Primary Actor - bên trái) và Tác nhân phụ/hệ thống ngoài (Secondary Actor - bên phải).
  - `유스케이스 (Use Case)`: Hình oval nằm bên trong System Boundary, đại diện cho một chức năng hoàn chỉnh mang lại giá trị cho người dùng.
  - `관계 (Relationships)`:
    - **연관 (Association):** Đường nối giữa Actor và Use Case.
    - **포함 관계 (`<<include>>` — Quan hệ bao hàm):**
      - [Hàn/Anh]: `하나의 유스케이스가 실행될 때 반드시 함께 실행되어야 하는 필수적인 관계이다.`
      - [Tiếng Việt]: Quan hệ **bắt buộc**. Use Case con bắt buộc phải thực thi mỗi khi Use Case cha chạy.
      - **Chiều mũi tên:** Mũi tên nét đứt trỏ từ **Use Case cha $\rightarrow$ Use Case được bao hàm** (`기본 유스케이스 - - - > 포함될 유스케이스`). Ví dụ: `[Chuyển tiền] - - - > <<include>> - - - > [Đăng nhập]`.
    - **확장 관계 (`<<extend>>` — Quan hệ mở rộng):**
      - [Hàn/Anh]: `특정 조건이 만족될 때만 선택적으로 실행되는 관계이다.`
      - [Tiếng Việt]: Quan hệ **tùy chọn / ngoại lệ**. Chỉ thực thi khi thỏa mãn một điều kiện mở rộng (Extension Point).
      - **Chiều mũi tên:** Mũi tên nét đứt trỏ ngược từ **Use Case mở rộng $\rightarrow$ Use Case cơ sở** (`확장 유스케이스 - - - > 기본 유스케이스`). Ví dụ: `[Nhận mã giảm giá] - - - > <<extend>> - - - > [Thanh toán đơn hàng]`.

##### B. Biểu đồ tuần tự (Sequence Diagram)
- **Đặc trưng:** Biểu diễn các thông điệp trao đổi giữa các đối tượng theo trục dọc thời gian chảy từ trên xuống dưới.
- **Các thành phần:**
  - `액터 (Actor)`: Người hoặc hệ thống kích hoạt luồng tương tác.
  - `생명선 (Lifeline)`: Đường nét đứt thẳng đứng xuất phát từ đáy của hình hộp đối tượng, biểu thị sự tồn tại của đối tượng theo thời gian.
  - `실행 상자 (Activation Bar / Execution Specification)`: Hình chữ nhật hẹp nằm dọc trên Lifeline, biểu thị khoảng thời gian đối tượng đang trực tiếp chiếm giữ CPU để thực thi thao tác.
  - `메시지 (Message)`:
    - `동기 메시지 (Synchronous Message)`: Đường nét liền có **mũi tên tam giác đặc** (`──►`). Người gửi bị chặn (block) và chờ đợi phản hồi trước khi đi tiếp.
    - `비동기 메시지 (Asynchronous Message)`: Đường nét liền có **mũi tên nhọn hở** (`──>`). Người gửi gửi thông điệp xong lập tức tiếp tục công việc của mình mà không cần đợi phản hồi.
    - `응답 메시지 (Return Message)`: **Đường nét đứt có mũi tên nhọn** (`- - ->`). Trả về kết quả sau khi thực hiện xong thông điệp đồng bộ.

##### C. Biểu đồ trạng thái và Biểu đồ hoạt động
- **상태 머신 다이어그램 (State Machine Diagram):**
  - Biểu diễn vòng đời của **MỘT đối tượng**.
  - Ký hiệu: `초기 상태 (Trạng thái bắt đầu - Chấm tròn đen đặc)`, `종료 상태 (Trạng thái kết thúc - Hình tròn mắt bò)`, `상태 전이 (Chuyển tiếp - Mũi tên kèm Event và Guard condition: [Điều kiện])`.
- **활동 다이어그램 (Activity Diagram):**
  - Biểu diễn luồng công việc nhiều tác vụ, tương tự Flowchart nhưng hỗ trợ xử lý song song.
  - **포크 (Fork):** Thanh ngang màu đen đặc nhận **1 luồng vào và chia thành nhiều luồng chạy song song**.
  - **조인 (Join):** Thanh ngang màu đen đặc nhận **nhiều luồng song song vào và chỉ xuất ra 1 luồng duy nhất** sau khi tất cả các luồng vào đã hoàn thành đồng bộ.

#### 6. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (Phân biệt Aggregation vs Composition):**
  - Vòng đời độc lập, lớp cha hủy con vẫn sống, **hình thoi rỗng** $\rightarrow$ **집약 관계 (Aggregation)**.
  - Vòng đời phụ thuộc sinh tử, lớp cha hủy con chết theo, **hình thoi đặc** $\rightarrow$ **합성 관계 (Composition)**.
- **Bẫy 2 (Chiều mũi tên include vs extend):**
  - `<<include>>`: Mũi tên trỏ từ **Gốc $\rightarrow$ Bao hàm** (Tôi cần bạn).
  - `<<extend>>`: Mũi tên trỏ ngược từ **Mở rộng $\rightarrow$ Gốc** (Tôi phụ thuộc vào bạn). Đề thi trắc nghiệm rất hay vẽ ngược chiều mũi tên của `<<extend>>` để đánh bẫy.
- **Bẫy 3 (Phân loại biểu đồ Tĩnh vs Động):**
  - Đề hỏi *"Biểu đồ nào sau đây KHÔNG PHẢI là biểu đồ cấu trúc tĩnh?"* $\rightarrow$ Đưa vào 3 cái tĩnh (Class, Component, Deployment) và 1 cái động (ví dụ: **Sequence Diagram** hoặc **Activity Diagram**).
- **Bẫy 4 (Đối tượng của State Machine):** Biểu đồ trạng thái chỉ theo dõi sự thay đổi trạng thái của **MỘT đối tượng duy nhất** trong suốt vòng đời của nó, không biểu diễn sự phối hợp giữa nhiều đối tượng.

- **한 문장 설명 (Câu chốt ghi nhớ):** "UML có 3 Amigos; Rỗng tập hợp độc lập, Đặc hợp thành sinh tử; Include bắt buộc trỏ đi, Extend tùy chọn trỏ về; Lifeline trục dọc thời gian, Fork chia Join gộp song song".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cơ chế sinh tử trong Lập trình: Aggregation vs Composition
Để hiểu vì sao đề thi luôn tập trung vào sự khác biệt giữa hai hình thoi:
- **Aggregation (집약 - Hình thoi rỗng):**
  - Mã nguồn thực tế: Lớp `Computer` nhận một đối tượng `Mouse` thông qua hàm khởi tạo (Dependency Injection) từ bên ngoài:
    ```java
    class Computer {
        private Mouse mouse;
        public Computer(Mouse m) { this.mouse = m; }
    }
    ```
  - Khi đối tượng `Computer` bị thu hồi bộ nhớ (Garbage Collected), đối tượng `Mouse` vẫn tồn tại nguyên vẹn trong bộ nhớ.
- **Composition (합성 - Hình thoi đặc):**
  - Mã nguồn thực tế: Lớp `House` tự mình khởi tạo đối tượng `Room` bên trong constructor của nó:
    ```java
    class House {
        private Room room;
        public House() { this.room = new Room(); }
    }
    ```
  - Khi đối tượng `House` bị hủy bỏ khỏi bộ nhớ, biến tham chiếu `room` biến mất và đối tượng `Room` bên trong lập tức bị hủy theo. Tính chất này gọi là "Ràng buộc vòng đời vĩnh viễn" (Coincident Lifetime).

#### 2. Kỹ thuật Stereotype (`<<...>>`) trong mở rộng UML
- UML cung cấp cơ chế mở rộng gọi là **스테레오 타입 (Stereotype)**, được đặt trong dấu ngoặc kép dạng chevron `<< >>` để bổ sung ý nghĩa ngữ nghĩa mới cho một phần tử chuẩn:
  - `<<interface>>`: Định nghĩa một giao diện thuần túy chỉ có các phương thức trừu tượng.
  - `<<entity>>`: Đại diện cho lớp chứa dữ liệu nghiệp vụ lưu trữ lâu dài trong cơ sở dữ liệu.
  - `<<boundary>>`: Đại diện cho lớp giao tiếp ở biên giới hệ thống (Giao diện màn hình, cổng giao tiếp API).
  - `<<control>>`: Đại diện cho lớp điều phối luồng logic nghiệp vụ nằm giữa Boundary và Entity (tương tự Controller trong mô hình MVC).

---

### 복습 체크리스트
- [ ] Nhớ tên tổ chức OMG và 3 nhà khoa học (Three Amigos: Booch, Rumbaugh, Jacobson) chuẩn hóa UML.
- [ ] Phân biệt được 6 mối quan hệ UML và vẽ đúng ký hiệu: Association (nét liền), Aggregation (hình thoi rỗng), Composition (hình thoi đặc), Generalization (tam giác rỗng), Dependency (nét đứt nhọn), Realization (nét đứt tam giác rỗng).
- [ ] Thuộc lòng 4 ký hiệu quyền truy cập: `+` (Public), `-` (Private), `#` (Protected), `~` (Package).
- [ ] Phân loại chính xác 6 biểu đồ cấu trúc tĩnh (Class, Object, Component, Deployment, Package, Composite) và 7 biểu đồ hành vi động.
- [ ] Phân biệt được chiều mũi tên và bản chất bắt buộc của `<<include>>` vs bản chất tùy chọn của `<<extend>>`.
- [ ] Vẽ và gọi tên đúng các thành phần trong Sequence Diagram: Lifeline (nét đứt dọc), Activation Bar (cột chữ nhật đứng), Thông điệp đồng bộ (tam giác đặc) vs Bất đồng bộ (mũi tên nhọn).
- [ ] Nhớ chức năng của thanh Fork (chia luồng song song) và thanh Join (đồng bộ gộp luồng song song) trong Activity Diagram.
