# Subject 1 - Part 3

## 1. 객체지향 설계 5대 원칙 (SOLID)
**개념 (Khái niệm):** 시스템의 변경이나 확장에 유연하게 대응하기 위해 지켜야 할 5가지 원칙 (5 nguyên tắc thiết kế hướng đối tượng giúp hệ thống linh hoạt trước các thay đổi và mở rộng).

*   **SRP (Single Responsibility Principle - 단일 책임 원칙):**
    *   **Korean:** 객체는 '단 하나의 책임'만 가져야 함. 클래스를 수정해야 할 이유는 단 하나여야 함.
    *   **Vietnamese:** Nguyên tắc Đơn trách nhiệm. Một đối tượng (hoặc lớp) chỉ nên có một trách nhiệm duy nhất. Lý do để sửa đổi một lớp chỉ nên có một.
    *   **Example:**
        *   *KR:* 보고서를 생성하는 클래스와 출력하는 클래스를 분리.
        *   *VN:* Tách biệt lớp tạo báo cáo và lớp in báo cáo, không để chung một lớp.
*   **OCP (Open-Closed Principle - 개방-폐쇄 원칙):**
    *   **Korean:** 기능 추가에는 열려(Open) 있어야 하고, 기존 코드 변경에는 닫혀(Closed) 있어야 함. 인터페이스로 캡슐화.
    *   **Vietnamese:** Nguyên tắc Đóng - Mở. Mở rộng chức năng thì dễ dàng (Open), nhưng không được sửa đổi mã nguồn hiện tại (Closed). Thường dùng Interface để đóng gói.
    *   **Example:**
        *   *KR:* 결제 수단(카드, 페이 등)을 인터페이스로 구현하여 새로운 결제 수단 추가 시 기존 코드 수정 없이 확장.
        *   *VN:* Dùng Interface cho phương thức thanh toán, khi thêm phương thức mới (ví dụ: ví điện tử) thì không cần sửa mã cũ.
*   **LSP (Liskov Substitution Principle - 리스코프 치환 원칙):**
    *   **Korean:** 자식 클래스는 최소한 부모 클래스의 행위를 수행할 수 있어야 함. 부모의 의도를 훼손하지 않고 확장.
    *   **Vietnamese:** Nguyên tắc Thay thế Liskov. Lớp con phải có thể thay thế lớp cha mà không làm hỏng tính đúng đắn của chương trình. Lớp con chỉ nên mở rộng, không làm sai lệch ý định của lớp cha.
    *   **Example:**
        *   *KR:* 새(Bird) 부모 클래스를 상속받은 펭귄(Penguin)이 날기(fly) 메서드를 가지면 LSP 위반.
        *   *VN:* Chim cánh cụt kế thừa từ lớp Chim, nhưng nếu gọi hàm bay() sẽ bị lỗi, vi phạm LSP. Cần thiết kế lại.
*   **ISP (Interface Segregation Principle - 인터페이스 분리 원칙):**
    *   **Korean:** 사용하지 않는 인터페이스에 의존하지 않도록 분리.
    *   **Vietnamese:** Nguyên tắc Phân tách Interface. Không nên ép các lớp phụ thuộc vào những interface mà chúng không sử dụng. Hãy chia nhỏ interface khổng lồ thành các interface cụ thể.
    *   **Example:**
        *   *KR:* 복합기 인터페이스를 프린터, 스캐너, 팩스 인터페이스로 분리.
        *   *VN:* Tách interface của máy photocopy đa năng thành các interface riêng: In, Quét, Fax.
*   **DIP (Dependency Inversion Principle - 의존 역전 원칙):**
    *   **Korean:** 구체적인 클래스보다 추상화된 클래스(인터페이스)에 의존해야 함.
    *   **Vietnamese:** Nguyên tắc Đảo ngược phụ thuộc. Các module cấp cao không nên phụ thuộc vào module cấp thấp, cả hai nên phụ thuộc vào abstractions (interface).
    *   **Example:**
        *   *KR:* 자동차가 스노우타이어(구체) 대신 타이어(추상) 인터페이스에 의존.
        *   *VN:* Lớp xe hơi phụ thuộc vào interface "Lốp xe" nói chung, thay vì phụ thuộc trực tiếp vào "Lốp đi tuyết".

💡 **Mẹo ghi nhớ (Mnemonics):** **SOLID** (S = Single, O = Open, L = Liskov, I = Interface, D = Dependency)

---

## 2. 모듈 (Module) & 독립성 (Independence)
**개념 (Khái niệm):** 시스템의 기능을 분리한 단위. 단독 컴파일과 재사용 가능 (Module là các đơn vị chức năng được phân tách của hệ thống, có thể biên dịch độc lập và tái sử dụng).

*   **기능적 독립성 (Functional Independence - Tính độc lập chức năng):**
    *   **Korean:** 각 모듈이 하나의 기능만을 수행하고 상호작용을 최소화하는 것. 결합도(Coupling)는 약하게(Weak), 응집도(Cohesion)는 강하게(Strong) 해야 함.
    *   **Vietnamese:** Mỗi module chỉ thực hiện một chức năng và hạn chế tương tác với bên ngoài. Cần Độ phụ thuộc (Coupling) thấp và Độ gắn kết (Cohesion) cao. Kích thước module nên nhỏ gọn.
    *   **Example:**
        *   *KR:* 독립된 로그인 모듈은 다른 모듈 변경 시 영향을 받지 않음.
        *   *VN:* Module đăng nhập đứng độc lập, khi sửa giỏ hàng thì module đăng nhập không bị ảnh hưởng.

---

## 3. 결합도 (Coupling - Độ phụ thuộc)
**개념 (Khái niệm):** 모듈 간의 의존성 정도 (Mức độ phụ thuộc giữa các module với nhau). **낮을수록 좋음 (Càng thấp càng tốt).**

순서 (Từ Tốt nhất đến Xấu nhất): **자료(Data) -> 스탬프(Stamp) -> 제어(Control) -> 외부(External) -> 공통(Common) -> 내용(Content)**
💡 **Mẹo ghi nhớ:** T-S-C-N-C-N (Data-Stamp-Control-External-Common-Content) -> **Tính Sao Cho Nhẹ Cả Người**

1.  **자료 결합도 (Data Coupling) - TỐT NHẤT:**
    *   **Korean:** 파라미터(자료 요소)만 전달.
    *   **Vietnamese:** Chỉ truyền tham số dữ liệu cần thiết.
    *   **Example:** `sum(a, b)` truyền đúng 2 số a, b.
2.  **스탬프 결합도 (Stamp Coupling):**
    *   **Korean:** 배열/레코드 등 자료구조가 전달됨.
    *   **Vietnamese:** Truyền toàn bộ cấu trúc dữ liệu (mảng, đối tượng) nhưng chỉ dùng 1 phần.
    *   **Example:** Truyền đối tượng `User` nhưng chỉ dùng `User.name`.
3.  **제어 결합도 (Control Coupling):**
    *   **Korean:** 제어 신호(Flag)를 전달하여 모듈 흐름 제어.
    *   **Vietnamese:** Truyền cờ điều khiển (flag, boolean) can thiệp vào logic của module khác.
    *   **Example:** Truyền `isExpress=true` để quyết định cách xử lý.
4.  **외부 결합도 (External Coupling):**
    *   **Korean:** 외부 변수/데이터 참조.
    *   **Vietnamese:** Cùng phụ thuộc vào dữ liệu / file / thiết bị bên ngoài.
    *   **Example:** Hai module dùng chung một file `config.txt`.
5.  **공통 결합도 (Common Coupling):**
    *   **Korean:** 공통 데이터 영역(전역 변수) 공유.
    *   **Vietnamese:** Nhiều module dùng chung biến toàn cục (global variables).
    *   **Example:** Sử dụng `public static int totalCount` chung.
6.  **내용 결합도 (Content Coupling) - XẤU NHẤT:**
    *   **Korean:** 내부 기능/자료 직접 참조. 스파게티 코드.
    *   **Vietnamese:** Truy cập, sửa đổi trực tiếp dữ liệu/logic nội bộ của module khác.
    *   **Example:** `moduleB.internalValue = 10` từ module A.

---

## 4. 응집도 (Cohesion - Độ gắn kết)
**개념 (Khái niệm):** 모듈 내부 요소들이 서로 밀접하게 관련되어 있는 정도 (Mức độ liên quan chặt chẽ của các thành phần BÊN TRONG 1 module). **강할수록 좋음 (Càng cao càng tốt).**

순서 (Từ Tốt nhất đến Xấu nhất): **기능(Functional) -> 순차(Sequential) -> 교환(Communication) -> 절차(Procedural) -> 시간(Temporal) -> 논리(Logical) -> 우연(Coincidental)**
💡 **Mẹo ghi nhớ:** K-S-K-C-S-N-U (Kì-Sun-Kiều-Chul-Shi-Non-U) -> **Không Tin Kiều Chỉ Sợ Người Ù**

1.  **기능적 응집도 (Functional):**
    *   **Korean:** 단일 문제와 연관되어 수행. (Tốt nhất)
    *   **Vietnamese:** Mọi thành phần trong module cùng giải quyết MỘT bài toán duy nhất.
2.  **순차적 응집도 (Sequential):**
    *   **Korean:** 출력 데이터가 다음 활동의 입력 데이터로 사용됨.
    *   **Vietnamese:** Đầu ra của bước này là đầu vào của bước kia (trong cùng module).
3.  **교환(통신)적 응집도 (Communication):**
    *   **Korean:** 동일한 입출력을 사용하여 서로 다른 기능 수행.
    *   **Vietnamese:** Các chức năng khác nhau dùng chung một tập dữ liệu đầu vào / đầu ra.
4.  **절차적 응집도 (Procedural):**
    *   **Korean:** 기능들을 순차적으로 수행.
    *   **Vietnamese:** Các phần tử được thực hiện theo trình tự thời gian / kịch bản nhất định.
5.  **시간적 응집도 (Temporal):**
    *   **Korean:** 특정 시간에 처리되는 기능들을 모음.
    *   **Vietnamese:** Gom các tác vụ xảy ra cùng một thời điểm (VD: khối khởi tạo hệ thống Init).
6.  **논리적 응집도 (Logical):**
    *   **Korean:** 유사한 성격/형태로 분류되는 요소들을 모음.
    *   **Vietnamese:** Gom các hàm có tính chất logic giống nhau (VD: Hàm in các loại báo cáo, mặc dù báo cáo khác nhau).
7.  **우연적 응집도 (Coincidental) - XẤU NHẤT:**
    *   **Korean:** 아무 관련 없이 구성됨.
    *   **Vietnamese:** Các phần tử gom lại ngẫu nhiên, không liên quan gì nhau.

---

## 5. Fan-In / Fan-Out (팬인 / 팬아웃)
**개념 (Khái niệm):** 모듈 간의 호출 관계를 나타내는 지표 (Chỉ số thể hiện mức độ gọi lẫn nhau giữa các module).

*   **Fan-In (들어옴 / Đi vào):**
    *   **Korean:** 나를 호출하는 모듈 수. **높게(High)** 설계하는 것이 재사용성 측면에서 좋음. (단, 단일 장애점 주의)
    *   **Vietnamese:** Số lượng module gọi đến module hiện tại. Fan-In CAO là tốt vì chứng tỏ module được tái sử dụng nhiều, nhưng cần cẩn thận vì nó là trung tâm (Single Point of Failure).
*   **Fan-Out (나감 / Đi ra):**
    *   **Korean:** 내가 호출하는 모듈 수. **낮게(Low)** 설계하여 단순화해야 함.
    *   **Vietnamese:** Số lượng module mà module hiện tại gọi. Fan-Out THẤP là tốt, tránh việc module phụ thuộc vào quá nhiều nơi khác.

💡 **Mẹo ghi nhớ:** Fan-In = Gọi VÀO tôi (High is good) / Fan-Out = Tôi gọi RA (Low is good).

---

## 6. N-S 차트 (Nassi-Schneiderman Chart)
**개념 (Khái niệm):** 논리 기술 중점의 박스 다이어그램 (Biểu đồ dạng hộp tập trung mô tả logic).

*   **Korean:** GOTO나 화살표를 사용하지 않음. 단일 입구/단일 출구. Box Diagram, Chapin Chart라고도 부름. 순차, 선택, 반복 논리 구조 시각화.
*   **Vietnamese:** Đặc điểm quan trọng nhất: **KHÔNG DÙNG GOTO và KHÔNG CÓ MŨI TÊN**. Có một lối vào và một lối ra duy nhất. Còn gọi là Box Diagram hoặc Chapin Chart. Gồm 3 cấu trúc: Tuần tự, Lựa chọn (If-else), Lặp (Loop). Dễ chuyển sang code nhưng khó vẽ.

---

## 7. 공통 모듈 (Common Module)
**개념 (Khái niệm):** 여러 프로그램에서 공통적으로 사용할 수 있는 모듈 (Module dùng chung cho nhiều chương trình, ví dụ: Đăng nhập, tính toán).

*   **명세 기법 5가지 (5 nguyên tắc viết đặc tả module):**
    1.  **정확성 (Correctness):** 정확히 작성 (Chính xác).
    2.  **명확성 (Clarity):** 중의적이지 않게 (Rõ ràng, không mơ hồ).
    3.  **완전성 (Completeness):** 모든 것을 빠짐없이 (Đầy đủ).
    4.  **일관성 (Consistency):** 상호 충돌 없게 (Nhất quán).
    5.  **추적성 (Traceability):** 출처, 관계 추적 가능 (Có thể truy xuất nguồn gốc).
💡 **Mẹo ghi nhớ:** C-M-H-N-T (Chính-Rõ-Đủ-Nhất-Truy) -> **Chỉ Mong Học Nhất Trường**

---

## 8. 재사용 (Reuse)
**개념 (Khái niệm):** 기존 기능을 최적화하여 다시 쓰는 것 (Tái sử dụng chức năng để tiết kiệm thời gian và chi phí).

*   **Korean:** 결합도는 낮고 응집도는 높아야 함.
*   **Vietnamese:** Yêu cầu: Độ phụ thuộc (Coupling) THẤP và Độ gắn kết (Cohesion) CAO.
*   **분류 (Phân loại):**
    *   **함수와 객체 (Function & Object):** 소스 코드 단위 (Mức mã nguồn / Class).
    *   **컴포넌트 (Component):** 인터페이스 통신 (Mức Interface, không sửa code gốc).
    *   **애플리케이션 (Application):** 시스템 전체 (Mức ứng dụng hoàn chỉnh).

---

## 9. 효과적인 모듈 설계 방안 (Effective Module Design)
*   **Korean:** 결합도↓, 응집도↑. 모듈의 영향 영역(Scope of Effect)이 제어 영역(Scope of Control) 안에 있어야 함. 단일 입구/단일 출구(Single Entry, Single Exit). 복잡도와 중복성 감소.
*   **Vietnamese:** Coupling thấp, Cohesion cao. **Phạm vi ảnh hưởng (Scope of Effect) phải nằm TRONG Phạm vi kiểm soát (Scope of Control)** của module. Chỉ có 1 đầu vào và 1 đầu ra. Giảm độ phức tạp và dư thừa.
*   **Example:** Một hàm sắp xếp chỉ nên thay đổi mảng truyền vào nó (trong vùng kiểm soát), không nên vô tình thay đổi giao diện UI (vùng ảnh hưởng ngoài kiểm soát).

---
## 10. 코드 (Code) 개요 & 종류
**개념 (Khái niệm):** 데이터를 식별, 분류, 배열하기 위해 사용하는 기호 (Ký hiệu dùng để nhận dạng, phân loại và sắp xếp dữ liệu).

*   **기능 (Chức năng):** 식별(Nhận dạng), 분류(Phân loại), 배열(Sắp xếp), 표준화(Chuẩn hóa), 간소화(Đơn giản hóa).
*   **종류 (Các loại Code):**
    1.  **순차 코드 (Sequential):** 발생 순서대로 일련번호 부여 (Đánh số thứ tự 1, 2, 3...).
    2.  **블록 코드 (Block):** 공통성 있는 항목을 블록으로 묶음 (Phân khối theo nhóm chung).
    3.  **10진 코드 (Decimal):** 0~9까지 10진 분할 반복, 도서분류 (Phân loại thập phân như sách thư viện).
    4.  **그룹 분류 코드 (Group Classification):** 대/중/소분류 (Phân nhóm lớn/vừa/nhỏ như 1-01-001).
    5.  **연상 코드 (Mnemonic):** 명칭이나 약호와 관계있는 기호 (Mã gợi nhớ, ví dụ: TV-40 cho Tivi 40 inch).
    6.  **표의 숫자 코드 (Significant Digit):** 물리적 수치를 직접 적용 (Dùng kích thước vật lý làm mã).
    7.  **합성 코드 (Combined):** 2개 이상 조합 (Kết hợp nhiều mã).

*   **코드 부여 체계 (Code Assignment System):**
    *   **Korean:** 이름만으로 개체의 용도와 적용 범위를 알 수 있게 상세 명시 (자릿수, 구분자).
    *   **Vietnamese:** Hệ thống đánh mã sao cho nhìn vào tên mã là biết ngay công dụng và phạm vi (cần nêu rõ số chữ số, dấu phân cách).
    *   **Example:** 연도(00) + 학과(00) + 개인번호(000) -> 2401001.

---

## 11. 디자인 패턴 (Design Pattern)
**개념 (Khái niệm):** 설계 시 참조할 수 있는 전형적인 해결 방식 (Các mẫu giải pháp tiêu chuẩn dùng tham khảo khi thiết kế phần mềm). GoF (Gang of Four)가 23개로 체계화.
💡 **Mẹo ghi nhớ:** "바퀴를 다시 발명하지 마라 (Don't reinvent the wheel)" - Đừng phát minh lại bánh xe, hãy dùng các mẫu đã được kiểm chứng.

*   **장단점 (Ưu & Nhược điểm):**
    *   장점: 구조 파악 용이, 의사소통 원활, 생산성 향상 (Dễ nắm cấu trúc, giao tiếp tốt, tăng năng suất).
    *   단점: **초기 투자 비용 부담**, 객체지향 전용 (Tốn chi phí/thời gian học ban đầu, chỉ hợp với Hướng đối tượng).

### 11.1 생성 패턴 (Creational - 5개)
객체 생성 캡슐화 (Đóng gói quá trình tạo đối tượng).
1.  **추상 팩토리 (Abstract Factory):** 연관된 객체 그룹 생성 (Tạo nhóm đối tượng liên quan).
2.  **빌더 (Builder):** 생성 과정과 표현 방법 분리 (Tách quá trình xây dựng và biểu diễn).
3.  **팩토리 메소드 (Factory Method):** 객체 생성을 서브 클래스에 위임, 가상 생성자 (Giao việc tạo đối tượng cho lớp con).
4.  **프로토타입 (Prototype):** 원본 객체 복제 (Nhân bản đối tượng nguyên mẫu Clone).
5.  **싱글톤 (Singleton):** 인스턴스가 하나뿐임을 보장 (Đảm bảo chỉ có 1 instance duy nhất).

### 11.2 구조 패턴 (Structural - 7개)
객체 조합으로 더 큰 구조 생성 (Kết hợp đối tượng thành cấu trúc lớn hơn).
1.  **어댑터 (Adapter):** 호환 안 되는 인터페이스 변환 (Chuyển đổi interface không tương thích).
2.  **브리지 (Bridge):** 구현과 추상층 분리 (Tách biệt phần triển khai và phần trừu tượng).
3.  **컴포지트 (Composite):** 트리 구조, 단일/복합 객체 동일하게 다룸 (Cấu trúc cây, xử lý đối tượng đơn và phức như nhau).
4.  **데코레이터 (Decorator):** 동적으로 기능 덧붙임 (Thêm chức năng linh hoạt bằng cách bọc đối tượng).
5.  **퍼싸드 (Facade):** 복잡한 서브 시스템 위에 통합 인터페이스(Wrapper) 제공 (Tạo mặt tiền/giao diện chung đơn giản cho hệ thống phức tạp).
6.  **플라이웨이트 (Flyweight):** 인스턴스 공유로 메모리 절약 (Chia sẻ đối tượng để tiết kiệm bộ nhớ).
7.  **프록시 (Proxy):** 접근 어려운 객체를 대리 수행 (Đại diện/ủy quyền truy cập cho đối tượng khác).

### 11.3 행위 패턴 (Behavioral - 11개)
객체 간 상호작용 및 책임 분배 (Tương tác và phân chia trách nhiệm giữa các đối tượng).
1.  **책임 연쇄 (Chain of Responsibility):** 고리를 따라 책임 넘김 (Truyền yêu cầu theo chuỗi xử lý).
2.  **커맨드 (Command):** 요청을 객체로 캡슐화 (로그, Undo) (Đóng gói yêu cầu thành đối tượng, tiện cho Undo/Log).
3.  **인터프리터 (Interpreter):** 언어 문법 정의 (Định nghĩa cú pháp ngôn ngữ).
4.  **반복자 (Iterator):** 내부 노출 없이 순차 접근 (Truy cập tuần tự không lộ cấu trúc).
5.  **중재자 (Mediator):** 복잡한 상호작용을 통제/지시 (Điều phối viên trung gian để giảm phụ thuộc chéo).
6.  **메멘토 (Memento):** 상태 스냅샷 저장/복원 (Lưu trạng thái để Undo/Khôi phục).
7.  **옵서버 (Observer):** 상태 변화를 구독자에게 전파 (Publish/Subscribe, thông báo khi có thay đổi).
8.  **상태 (State):** 상태에 따라 다른 동작 (Hành vi thay đổi theo trạng thái).
9.  **전략 (Strategy):** 알고리즘 캡슐화하여 교체 가능 (Đóng gói thuật toán, dễ dàng hoán đổi).
10. **템플릿 메소드 (Template Method):** 상위가 골격, 하위가 세부 구현 (Lớp cha tạo khung, lớp con điền chi tiết).
11. **방문자 (Visitor):** 처리 기능을 분리하여 방문 수행 (Tách logic xử lý ra khỏi cấu trúc dữ liệu, đi "thăm" từng phần tử).

---

## 12. 요구사항 (Requirements)
### 요구사항 분석 (Requirements Analysis)
*   **분류 (Phân loại):** 기능적(Functional) / 비기능적(Non-functional)으로 조직화.
*   **절차 (Quy trình 5 bước):** 선별(목록 작성) -> 자료 준비 -> 분류(기능/비기능) -> 분석 및 수정 -> 전달 (Lọc -> Chuẩn bị -> Phân loại -> Phân tích/Sửa -> Truyền đạt).

### 요구사항 검증 (Requirements Verification)
**설계 및 구현 전에 베이스라인(Baseline) 설정** (Xác minh trước khi thiết kế/code để chốt Baseline làm chuẩn).
*   **검증 방법 (Các phương pháp kiểm tra):**
    *   수작업: 동료검토(Peer Review), 워크스루(Walkthrough), 인스펙션(Inspection).
    *   **프로토타이핑 (Prototyping):** 견본 제작 (Làm bản mẫu dùng thử).
    *   **테스트 설계 (Test Design):** 테스트 케이스 생성 (Viết test case trước để xem có test được không).
    *   **CASE 도구:** 자동화 도구로 일관성 분석 (Dùng phần mềm check logic).

### 요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)
1.  **완전성 (Completeness):** 누락 없이 (Đầy đủ).
2.  **일관성 (Consistency):** 충돌 없이 (Nhất quán).
3.  **명확성 (Unambiguity):** 똑같이 이해되게 (Rõ ràng).
4.  **기능성 (Functionality):** '어떻게'보다 '무엇을(What)' (Tập trung vào tính năng "Làm gì" hơn là "Làm như thế nào").
5.  **검증 가능성 (Verifiability):** 테스트 가능 여부 (Có thể kiểm chứng/test được).
6.  **추적 가능성 (Traceability):** 설계서와 연결 (Có thể truy xuất).
7.  **변경 용이성 (Easily Changeable):** 수정 용이 (Dễ thay đổi).

---

## 13. 시스템 연계 및 인터페이스 (System Interface & Integration)
### 13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)
1.  **DB Link:** DB 객체 이용 (Kết nối trực tiếp qua DB Link).
2.  **API/Open API:** 프로그램 인터페이스 (Mở cổng API để ứng dụng khác gọi).
3.  **EAI (연계 솔루션):** 중계 서버/클라이언트 사용 (Dùng máy chủ trung gian Enterprise Application Integration).
4.  **Socket:** 포트 할당하여 연결 (Mở port mạng Socket để truyền dữ liệu).
5.  **Web Service:** WSDL, UDDI, SOAP 프로토콜 사용 (Dịch vụ web dùng giao thức chuẩn XML/SOAP).

### 13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)
*   **통신 유형 (Loại Giao tiếp):**
    *   **단방향 (Unidirectional):** 응답 없음 (Chỉ gửi, không cần phản hồi).
    *   **동기 (Synchronous):** 응답 대기 (Gửi và đợi phản hồi).
    *   **비동기 (Asynchronous):** 다른 작업 수행 (Gửi xong làm việc khác, trả lời sau).
*   **처리 유형 (Loại Xử lý):**
    *   **실시간 (Real-time):** 즉시 처리 (Xử lý ngay lập tức).
    *   **지연 처리 (Deferred):** 비용 절감을 위해 모아서 처리 (Trì hoãn xử lý để tiết kiệm chi phí).
    *   **배치 (Batch):** 대용량 일괄 처리 (Gom dữ liệu lớn xử lý 1 lần).

### 13.3 명세화 (Specification)
*   **송수신 데이터 명세화:** 데이터 필드명, 타입, 사이즈, **암호화 여부** 정의 (Đặc tả dữ liệu: Tên trường, Kiểu, Kích thước, và có Cần Mã hóa không).
*   **오류 식별 및 처리 방안 명세화:** 오류 코드, 메시지, 해결 방법 정의 (Đặc tả lỗi: Mã lỗi, Thông báo, Cách xử lý để dễ vận hành).

---

## 14. 미들웨어 (Middleware)
**개념 (Khái niệm):** 운영체제와 응용 프로그램 사이의 중재자 (Phần mềm trung gian đứng giữa OS và Ứng dụng).
💡 **Mẹo ghi nhớ 미들웨어:** DB, RPC, MOM, TP-Monitor, ORB, WAS

1.  **DB 미들웨어:** 2-Tier 원격 연결 (ODBC, IDAPI, Glue). (Kết nối CSDL 2 lớp).
2.  **RPC (Remote Procedure Call):** 원격을 로컬처럼 호출 (Entera, ONC/RPC). (Gọi hàm từ xa như gọi hàm cục bộ).
3.  **MOM (Message Oriented Middleware):** 비동기 메시지, 데이터 동기 (IBM MQ, JMS). (Truyền tin nhắn bất đồng bộ, đồng bộ dữ liệu hệ thống khác nền tảng).
4.  **TP-Monitor (Transaction Processing):** 항공/철도 예약, 빠른 응답/트랜잭션 감시 (tuxedo, tmax). (Giám sát giao dịch, đảm bảo tốc độ phản hồi nhanh cho đặt vé).
5.  **ORB (Object Request Broker):** 객체 지향, CORBA 표준 (Orbix). (Môi giới yêu cầu đối tượng, chuẩn CORBA).
6.  **WAS (Web Application Server):** 동적 콘텐츠, 웹 환경 핵심(Java/EJB) (WebLogic, WebSphere). (Xử lý nội dung web động, tác vụ doanh nghiệp quan trọng).
    *   *Example:* Apache là Web Server (tĩnh), còn WebLogic/Tomcat là WAS (động).

*   **솔루션 식별 & 명세서 작성:** 아키텍처 구성 정보, 구매 내역 확인 -> 제약사항 확인 (Xác định Middleware dựa trên kiến trúc và hóa đơn mua sắm -> Kiểm tra các hạn chế / constraints).
