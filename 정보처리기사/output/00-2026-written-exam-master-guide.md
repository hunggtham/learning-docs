# 정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **0. Vì sao cần một master guide riêng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **1.1 요구사항 확인 — Requirements confirmation** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng master guide làm bản đồ owner của kỳ thi, rồi nối yêu cầu, các môn, độ sâu và remediation thành lộ trình học.

> Mục tiêu của tệp (file / 파일) này không phải là một bản 요약 (tóm tắt) để học thuộc trong vài giờ. Đây là **xương sống ôn thi** dùng để kiểm tra rằng toàn bộ phạm vi 필기 đã được học đủ, hiểu đủ sâu và có thể phân biệt các khái niệm gần giống nhau trong các tình huống đánh giá.
>
> Thuật ngữ quan trọng giữ nguyên tiếng Hàn, kèm English và nghĩa Việt để khi gặp trực tiếp trong đề thi không phải dịch lại trong đầu.

## 0. Vì sao cần một master guide riêng

정보처리기사 필기 có 5 môn, mỗi môn 20 câu. Điểm trung bình phải từ 60 trở lên, đồng thời **không môn nào được dưới 40**. Điều này tạo ra hai loại rủi ro khác nhau. Rủi ro thứ nhất là không biết đủ rộng: một môn có vài vùng kiến thức bỏ trống sẽ dễ rơi vào 과락. Rủi ro thứ hai là biết nhiều thuật ngữ nhưng không phân biệt được chúng khi đáp án cố tình dùng những khái niệm gần nhau.

Vì vậy cách học ở đây dùng ba lớp.

**Coverage tầng (layer / 계층)** trả lời: phạm vi chính thức có phần nào và mình đã học phần đó chưa?
**Understanding tầng (layer / 계층)** trả lời: cơ chế bên dưới là gì, tại sao khái niệm đó tồn tại, nó khác khái niệm gần nó ở đâu?
**Exam tầng (layer / 계층)** trả lời: nếu câu hỏi đổi cách diễn đạt, cho đoạn mã (code / 코드), SQL, sơ đồ hoặc tình huống thì mình có suy ra được đáp án không?

Bộ 출제기준 áp dụng năm 2026 vẫn dùng 5 môn:

1. 소프트웨어 설계 — Software thiết kế (design / 설계) — Thiết kế phần mềm
2. 소프트웨어 개발 — Software Development — Phát triển phần mềm
3. 데이터베이스 구축 — cơ sở dữ liệu (database / 데이터베이스) Construction — Xây dựng cơ sở dữ liệu
4. 프로그래밍 언어 활용 — Programming ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션) — Ứng dụng ngôn ngữ lập trình
5. 정보시스템 구축관리 — thông tin (information / 정보) hệ thống (system / 시스템) Construction Management — Quản lý xây dựng hệ thống thông tin

Khung ôn dưới đây bám theo 21 chương lớn đang được các giáo trình 2026 tổ chức theo 출제기준: 4 chương ở môn 1, 5 chương ở môn 2, 5 chương ở môn 3, 3 chương ở môn 4 và 4 chương ở môn 5.

---

# 1. 소프트웨어 설계 — Software thiết kế (design / 설계)

Môn 1 kiểm tra khả năng nhìn một hệ thống **trước khi mã (code / 코드)**. Nếu chỉ nhớ từ khóa UML, Agile, 디자인 패턴 mà không hiểu dòng chảy từ yêu cầu → mô hình → kiến trúc → mô-đun (module / 모듈) → giao diện (interface / 인터페이스), rất dễ nhầm đáp án.

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **1.1 요구사항 확인 — Requirements confirmation** nối từ **0. Vì sao cần một master guide riêng** sang **1.2 화면 설계 — UI thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.1 요구사항 확인 — Requirements confirmation

### 현행 시스템 분석 — phân tích hệ thống hiện tại

Trước khi thiết kế hệ thống mới phải biết hệ thống hiện tại đang gồm những subsystem nào, giao tiếp ra sao, dùng OS/DBMS/mạng (network / 네트워크) gì và có giới hạn kỹ thuật nào. Đây không phải thủ tục giấy tờ; nó quyết định liệu yêu cầu mới có khả thi hay không.

Khi đọc câu hỏi về 플랫폼 기능 분석, 플랫폼 성능 특성 분석, 운영체제 분석, 네트워크 분석, DBMS 분석, hãy luôn xác định **đối tượng đang được đánh giá là gì**. Ví dụ, thông lượng (throughput / 처리량) thấp có thể liên quan hiệu năng nền tảng (platform / 플랫폼); một DBMS không hỗ trợ giao dịch (transaction / 트랜잭션) isolation mong muốn lại là giới hạn của cơ sở dữ liệu (database / 데이터베이스) nền tảng (platform / 플랫폼).

### 요구사항 분류

Functional yêu cầu (requirement / 요구사항) — 기능 요구사항 — mô tả hệ thống **phải làm gì**.
Non-functional yêu cầu (requirement / 요구사항) — 비기능 요구사항 — mô tả hệ thống **phải tốt đến mức nào hoặc bị ràng buộc như thế nào**: hiệu năng (performance / 성능), bảo mật (security / 보안), availability, portability, usability, pháp lý.

Ví dụ: “người dùng có thể reset password” là functional. “reset password phải hoàn thành dưới 2 giây và đơn vị từ (token / 토큰) hết hạn sau 10 phút” là non-functional.

Đề thường làm khó bằng cách viết non-functional yêu cầu (requirement / 요구사항) dưới dạng một hành vi. Hãy nhìn vào bản chất: nếu câu nói về chất lượng, giới hạn hoặc ràng buộc (constraint / 제약조건) thì không phải chức năng nghiệp vụ chính.

### 요구사항 개발 프로세스

Elicitation — 도출 — khai thác yêu cầu.
phân tích (analysis / 분석) — 분석 — phân tích xung đột, feasibility, priority.
Specification — 명세 — biểu diễn thành tài liệu/mô hình có thể kiểm tra.
kiểm tra hợp lệ (validation / 검증) — 확인/검증 — xác nhận yêu cầu phản ánh đúng điều stakeholder cần.

Phân biệt **xác minh (verification / 확인)** và **kiểm tra hợp lệ (validation / 검증)** theo câu hỏi nền tảng:

- xác minh (verification / 확인): “Are we building the sản phẩm (product / 제품) right?” — đang xây đúng theo đặc tả không?
- kiểm tra hợp lệ (validation / 검증): “Are we building the right sản phẩm (product / 제품)?” — đặc tả/sản phẩm có đúng nhu cầu không?

### 요구사항 분석 기법

Luồng dữ liệu (data flow / 데이터 흐름) Diagram — DFD — 자료 흐름도 biểu diễn tiến trình (process / 프로세스), luồng dữ liệu (data flow / 데이터 흐름), dữ liệu (data / 데이터) store, bên ngoài (external / 외부) thực thể (entity / 엔터티). DFD tập trung **dữ liệu đi đâu và được biến đổi thế nào**, không mô tả điều khiển (control / 제어) luồng (flow / 흐름) chi tiết như flowchart.

Dữ liệu (data / 데이터) Dictionary — DD — 자료 사전 mô tả cấu trúc dữ liệu và ký hiệu. Các ký hiệu truyền thống như `=`, `+`, `{}`, `[]`, `()` thường được hỏi theo kiểu ghép nghĩa; cần học theo bản chất cấu tạo dữ liệu thay vì chỉ học chuỗi ký hiệu.

Mini-specification — 소단위 명세서 dùng để mô tả lô-gic (logic / 논리) bên trong tiến trình (process / 프로세스) ở mức thấp của DFD khi tên tiến trình (process / 프로세스) chưa đủ rõ.

### UML

UML không phải một diagram mà là một ngôn ngữ mô hình hóa có nhiều diagram.

Structural diagrams — 구조 다이어그램 — mô tả cấu trúc tĩnh: lớp (class / 클래스), đối tượng (object / 객체), thành phần (component / 컴포넌트), triển khai (deployment / 배포), gói (package / 패키지), Composite cấu trúc (structure / 구조).

Behavioral diagrams — 행위 다이어그램 — mô tả hành vi: Use trường hợp (case / 사례), Activity, máy trạng thái (state machine / 상태 머신). tương tác (interaction / 상호작용) diagrams như chuỗi (sequence / 시퀀스), Communication, Timing, tương tác (interaction / 상호작용) Overview là nhóm hành vi tập trung tương tác.

Trong chuỗi (sequence / 시퀀스) Diagram, lifeline đi theo chiều dọc, thời gian tiến từ trên xuống dưới, message biểu diễn tương tác. Trong Activity Diagram, trọng tâm là luồng hoạt động và quyết định (decision / 결정)/parallelism. Trong trạng thái (state / 상태) Diagram, trọng tâm là trạng thái của một đối tượng (object / 객체) và chuyển tiếp (transition / 전이) khi sự kiện (event / 이벤트) xảy ra.

**Bẫy thường gặp:** cùng một nghiệp vụ có thể vẽ bằng nhiều diagram. Câu hỏi hỏi “muốn biết đối tượng (object / 객체) nào gọi đối tượng (object / 객체) nào theo thứ tự thời gian” → chuỗi (sequence / 시퀀스). “Muốn biết trạng thái đối tượng (object / 객체) thay đổi thế nào” → trạng thái (state / 상태). “Muốn biết luồng (flow / 흐름) công việc” → Activity.

### Agile, Scrum, XP

Agile là nhóm tư tưởng/phương pháp ưu tiên phản hồi (feedback / 피드백) nhanh và thích nghi thay đổi; Scrum là khung phần mềm (framework / 프레임워크) quản lý công việc theo sprint; XP tập trung mạnh vào kỹ thuật (engineering / 엔지니어링) practices.

Scrum: sản phẩm (product / 제품) Backlog → Sprint Planning → Sprint Backlog → Sprint → Increment, với Daily Scrum, Sprint rà soát (review / 검토), Sprint Retrospective.

XP thường gắn với Pair Programming, Test-Driven Development, Continuous tích hợp (integration / 통합), Refactoring, Small Releases, Collective quyền sở hữu (ownership / 소유권).

Đừng đồng nhất “Agile = không có tài liệu”. Agile giảm tài liệu không tạo giá trị, không phủ nhận documentation cần thiết.

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **1.2 화면 설계 — UI thiết kế (design / 설계)** nối từ **1.1 요구사항 확인 — Requirements confirmation** sang **1.3 애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.2 화면 설계 — UI thiết kế (design / 설계)

UI thiết kế (design / 설계) không chỉ là bố cục. Đề có thể hỏi 원칙, 유형, 설계 도구, usability và khả năng tiếp cận (accessibility / 접근성).

### UI 유형

CLI — Command Line giao diện (interface / 인터페이스): giao tiếp bằng lệnh.
GUI — Graphical người dùng (user / 사용자) giao diện (interface / 인터페이스): cửa sổ, icon, menu.
NUI — Natural người dùng (user / 사용자) giao diện (interface / 인터페이스): gesture, voice, touch tự nhiên.
OUI — Organic người dùng (user / 사용자) giao diện (interface / 인터페이스): giao diện (interface / 인터페이스) linh hoạt theo vật lý/hình dạng trong cách phân loại truyền thống của giáo trình.

### UI 설계 원칙

직관성 — intuitiveness: người dùng đoán được cách dùng.
유효성 — effectiveness: đạt mục tiêu chính xác.
학습성 — learnability: dễ học.
유연성 — flexibility: thích ứng nhiều tình huống/người dùng.

Các giáo trình có thể diễn đạt thêm consistency, khả năng tiếp cận (accessibility / 접근성), phản hồi (feedback / 피드백). Đề cần đọc đúng thuật ngữ đang hỏi thay vì suy từ “nghe có vẻ tốt”.

### UI 설계 산출물

Wireframe tập trung cấu trúc màn hình.
Mockup cho hình thức gần giao diện thật nhưng thường chưa có tương tác đầy đủ.
Prototype mô phỏng tương tác để kiểm chứng luồng (flow / 흐름).
Storyboard mô tả màn hình, chuyển tiếp (transition / 전이) và tương tác (interaction / 상호작용) theo kịch bản.

Bẫy: Prototype có thể low-fidelity hoặc high-fidelity; không phải cứ prototype là sản phẩm chạy hoàn chỉnh.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **1.3 애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)** nối từ **1.2 화면 설계 — UI thiết kế (design / 설계)** sang **1.4 인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.3 애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)

### 모듈 독립성 — mô-đun (module / 모듈) independence

Thiết kế tốt thường hướng tới **high cohesion, low coupling**.

Cohesion — 응집도 — mức các phần bên trong cùng mô-đun (module / 모듈) phục vụ một mục tiêu thống nhất. Thứ tự thường học từ mạnh đến yếu:

Functional → Sequential → Communicational → Procedural → Temporal → Logical → Coincidental.

Coupling — 결합도 — mức mô-đun (module / 모듈) phụ thuộc mô-đun (module / 모듈) khác. Thứ tự thường học từ mạnh/xấu đến yếu/tốt:

Content → dùng chung (common / 공통) → bên ngoài (external / 외부) → điều khiển (control / 제어) → Stamp → dữ liệu (data / 데이터).

Cần hiểu từng loại, không chỉ thuộc thứ tự. dữ liệu (data / 데이터) coupling truyền đúng dữ liệu cần thiết qua parameter. Stamp coupling truyền một cấu trúc tổng hợp dù chỉ dùng một phần. điều khiển (control / 제어) coupling truyền flag làm thay đổi lô-gic (logic / 논리) nội bộ mô-đun (module / 모듈) kia. dùng chung (common / 공통) coupling cùng truy cập toàn cục (global / 전역) dữ liệu (data / 데이터). Content coupling can thiệp trực tiếp nội bộ mô-đun (module / 모듈) khác.

### Fan-in / Fan-out

Fan-in là số mô-đun (module / 모듈) gọi vào một mô-đun (module / 모듈). Fan-out là số mô-đun (module / 모듈) mà mô-đun (module / 모듈) hiện tại gọi ra. Fan-in cao có thể thể hiện reuse tốt; fan-out quá cao thường làm mô-đun (module / 모듈) phụ thuộc nhiều thành phần. Nhưng không dùng chỉ số này máy móc: luôn đọc ngữ cảnh câu hỏi.

### 객체지향 — OOP

Encapsulation — 캡슐화 — che giấu hiện thực (implementation / 구현) và gom trạng thái (state / 상태) + hành vi (behavior / 동작).
Inheritance — 상속 — lớp con kế thừa đặc tính/hành vi.
Polymorphism — 다형성 — cùng giao diện (interface / 인터페이스)/message nhưng hành vi (behavior / 동작) khác theo đối tượng (object / 객체).
lớp trừu tượng (abstraction / 추상화) — 추상화 — giữ bản chất cần thiết, bỏ chi tiết không liên quan.

Overloading = cùng tên phương thức (method / 메서드) nhưng khác parameter danh sách (list / 목록), thường quyết định compile thời gian (time / 시간).
Overriding = subclass định nghĩa lại phương thức (method / 메서드) của superclass với cùng đặc tả hợp đồng (contract / 계약), thường liên quan động (dynamic / 동적) dispatch/thời gian chạy (runtime / 런타임) polymorphism.

### SOLID

SRP: một mô-đun (module / 모듈)/lớp (class / 클래스) nên có một lý do chính để thay đổi.
OCP: mở rộng hành vi (behavior / 동작) mà hạn chế sửa mã (code / 코드) ổn định.
LSP: subtype phải thay thế supertype mà không phá đặc tả hợp đồng (contract / 계약).
ISP: máy khách (client / 클라이언트) không nên phụ thuộc giao diện (interface / 인터페이스) chứa phương thức (method / 메서드) nó không dùng.
DIP: mô-đun (module / 모듈) cấp cao phụ thuộc lớp trừu tượng (abstraction / 추상화) thay vì concrete hiện thực (implementation / 구현).

Không nên học SOLID như khẩu hiệu. Ví dụ nếu `PaymentService` trực tiếp `new KakaoPayClient()` và mọi lô-gic (logic / 논리) lệ thuộc lớp (class / 클래스) đó, DIP bị yếu. Nếu dịch vụ (service / 서비스) nhận `PaymentGateway` giao diện (interface / 인터페이스) qua constructor, phụ thuộc (dependency / 의존성) hướng về lớp trừu tượng (abstraction / 추상화).

### Mẫu thiết kế (design pattern / 디자인 패턴)

Ba nhóm GoF:

Creational — 생성: Abstract Factory, Builder, Factory phương thức (method / 메서드), Prototype, Singleton.
Structural — 구조: Adapter, cầu nối (bridge / 브리지), Composite, Decorator, Facade, Flyweight, Proxy.
Behavioral — 행위: chuỗi (chain / 사슬) of Responsibility, Command, trình thông dịch (interpreter / 인터프리터), Iterator, Mediator, Memento, Observer, trạng thái (state / 상태), chiến lược (strategy / 전략), Template phương thức (method / 메서드), Visitor.

Học mẫu (pattern / 패턴) theo “bài toán (problem / 문제) → cơ chế (mechanism / 메커니즘) → consequence”.

Adapter đổi giao diện (interface / 인터페이스) để hai thành phần không tương thích làm việc với nhau. Decorator bọc đối tượng (object / 객체) để thêm hành vi (behavior / 동작) động. Proxy đứng thay đối tượng (object / 객체) để kiểm soát truy cập/lazy loading/remote truy cập (access / 접근). chiến lược (strategy / 전략) đóng gói thuật toán (algorithm / 알고리즘) có thể thay thế. trạng thái (state / 상태) làm hành vi (behavior / 동작) thay đổi theo trạng thái (state / 상태) nội bộ. Observer phát thông báo một-nhiều khi subject đổi.

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **1.4 인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계)** nối từ **1.3 애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)** sang **2.1 데이터 입출력 구현 — dữ liệu (data / 데이터) I/O hiện thực (implementation / 구현)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.4 인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계)

Giao diện (interface / 인터페이스) giữa hệ thống phải định nghĩa dữ liệu, giao thức (protocol / 프로토콜), timing, lỗi (error / 오류) handling và bảo mật (security / 보안).

EAI — Enterprise ứng dụng (application / 애플리케이션) tích hợp (integration / 통합) thường gặp các topology: Point-to-Point, Hub & Spoke, Message Bus, Hybrid. Point-to-Point đơn giản khi ít hệ thống nhưng số liên kết (connection / 연결) tăng nhanh khi hệ thống tăng. Hub & Spoke tập trung kết nối qua hub nhưng hub có thể trở thành bottleneck/single điểm (point / 지점) of thất bại (failure / 실패). Message Bus giảm coupling nhờ bus/message-oriented tích hợp (integration / 통합).

ESB — Enterprise dịch vụ (service / 서비스) Bus nhấn mạnh dịch vụ (service / 서비스) tích hợp (integration / 통합), routing, transformation và mediation trên bus.

JSON nhẹ, dễ dùng trong web API. XML giàu khả năng mô tả lược đồ (schema / 스키마)/không gian tên (namespace / 네임스페이스) nhưng verbose hơn. AJAX là kỹ thuật trình duyệt (browser / 브라우저) trao đổi dữ liệu bất đồng bộ mà không reload toàn trang; AJAX không phải một dữ liệu (data / 데이터) format.

---

# 2. 소프트웨어 개발 — Software Development

Môn 2 thường gây cảm giác “rải rác” vì trộn 자료구조, testing, packaging, phiên bản (version / 버전) điều khiển (control / 제어), giao diện (interface / 인터페이스). Hãy nhìn nó như giai đoạn **hiện thực (implementation / 구현) → kiểm thử (test / 테스트) → gói (package / 패키지) → integrate**.

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **1.4 인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계)** đặt vấn đề; **2.1 데이터 입출력 구현 — dữ liệu (data / 데이터) I/O hiện thực (implementation / 구현)** đối chiếu bằng chứng, rồi **2.2 통합 구현 — tích hợp (integration / 통합) hiện thực (implementation / 구현)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2.1 데이터 입출력 구현 — dữ liệu (data / 데이터) I/O hiện thực (implementation / 구현)

### 자료구조

Array có truy cập chỉ mục (index / 인덱스) O(1) nhưng insert/delete giữa mảng thường O(n). Linked danh sách (list / 목록) truy cập vị trí bất kỳ O(n), nhưng insert/delete tại nút (node / 노드) đã biết có thể O(1).

Ngăn xếp (stack / 스택) — LIFO — Last In First Out; dùng cho ngăn xếp lời gọi (call stack / 호출 스택), undo, expression evaluation.
hàng đợi (queue / 큐) — FIFO — First In First Out; dùng cho scheduling, buffering.
Deque cho phép thêm/xóa hai đầu.

Cây (tree / 트리) cần nắm gốc (root / 루트), parent, child, sibling, leaf, degree, mức (level / 수준), height/độ sâu (depth / 깊이). nhị phân (binary / 이진) cây (tree / 트리) mỗi nút (node / 노드) tối đa hai child. Full/complete/perfect nhị phân (binary / 이진) cây (tree / 트리) là các khái niệm khác nhau; đề có thể chỉ đưa hình rồi hỏi loại cây.

Traversal:

- Preorder: gốc (root / 루트) → Left → Right
- Inorder: Left → gốc (root / 루트) → Right
- Postorder: Left → Right → gốc (root / 루트)

Tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리) có left < nút (node / 노드) < right theo thứ tự (ordering / 순서) quy tắc (rule / 규칙). Balanced cây (tree / 트리) giữ chiều cao gần log n để tìm kiếm (search / 검색)/insert/delete hiệu quả.

Đồ thị (graph / 그래프) cần phân biệt directed/undirected, weighted/unweighted, degree, đường dẫn (path / 경로), cycle, connected thành phần (component / 컴포넌트). BFS dùng hàng đợi (queue / 큐); DFS dùng ngăn xếp (stack / 스택)/recursion.

### 정렬

Không học sorting chỉ bằng Big-O. Cần biết cơ chế để nhận diện từ mô tả.

Bubble: đổi chỗ phần tử kề nhau, phần tử lớn “nổi” dần về cuối.
Selection: mỗi vòng chọn min/max rồi đặt vào vị trí.
Insertion: mở rộng vùng đã sắp và chèn phần tử mới đúng vị trí.
Quick: chọn pivot, partition rồi đệ quy. Average O(n log n), worst O(n²).
Merge: chia, sort từng nửa, merge; O(n log n), cần bộ nhớ phụ theo hiện thực (implementation / 구현).
vùng nhớ động (heap / 힙): dùng vùng nhớ động (heap / 힙) để lặp lấy min/max; O(n log n).

### 검색 / 해싱

Tìm kiếm nhị phân (binary search / 이진 탐색) yêu cầu dữ liệu có thứ tự; mỗi bước giảm tìm kiếm (search / 검색) không gian (space / 공간) một nửa, O(log n).

Hashing biến key thành bucket/chỉ mục (index / 인덱스). Collision không phải lỗi lô-gic (logic / 논리) bất thường mà là khả năng tự nhiên vì nhiều key có thể ánh xạ cùng vị trí. Cách xử lý: chaining hoặc open addressing như tuyến tính (linear / 선형) probing, quadratic probing, double hashing.

Tải (load / 로드) factor tăng cao thường làm collision tăng và hiệu năng (performance / 성능) giảm.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **2.1 데이터 입출력 구현 — dữ liệu (data / 데이터) I/O hiện thực (implementation / 구현)** đặt vấn đề; **2.2 통합 구현 — tích hợp (integration / 통합) hiện thực (implementation / 구현)** đối chiếu bằng chứng, rồi **2.3 제품 소프트웨어 패키징 — sản phẩm (product / 제품) software packaging** mở rộng hệ quả hoặc giới hạn liên quan.

## 2.2 통합 구현 — tích hợp (integration / 통합) hiện thực (implementation / 구현)

Đơn vị (unit / 단위) mô-đun (module / 모듈) cần giao diện (interface / 인터페이스) rõ, đầu vào (input / 입력)/đầu ra (output / 출력) rõ, lỗi (error / 오류) handling rõ và có khả năng kiểm thử (test / 테스트) độc lập.

IPC — Inter-Process Communication gồm pipe, named pipe, message hàng đợi (queue / 큐), dùng chung (shared / 공유) bộ nhớ (memory / 메모리), socket, semaphore/tín hiệu (signal / 신호) tùy phân loại. dùng chung (shared / 공유) bộ nhớ (memory / 메모리) nhanh vì không phải bản sao (copy / 복사) message nhiều lần nhưng cần synchronization cẩn thận. Message hàng đợi (queue / 큐) giảm coupling nhưng có overhead và thứ tự (ordering / 순서)/delivery ngữ nghĩa (semantics / 의미론) cần xem xét.

Tích hợp (integration / 통합) không chỉ “ghép mô-đun (module / 모듈)”; phải kiểm chứng đặc tả hợp đồng (contract / 계약) và luồng dữ liệu (data flow / 데이터 흐름) giữa mô-đun (module / 모듈).

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **2.3 제품 소프트웨어 패키징 — sản phẩm (product / 제품) software packaging** nối từ **2.2 통합 구현 — tích hợp (integration / 통합) hiện thực (implementation / 구현)** sang **2.4 애플리케이션 테스트 관리 — ứng dụng (application / 애플리케이션) kiểm thử (test / 테스트) management**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2.3 제품 소프트웨어 패키징 — sản phẩm (product / 제품) software packaging

Packaging gồm hiện vật bản dựng (build artifact / 빌드 산출물), phụ thuộc (dependency / 의존성), installation/uninstallation, phiên bản (version / 버전), bản phát hành (release / 릴리스) notes, license, DRM khi có nội dung cần bảo vệ.

### 형상 관리 — cấu hình (configuration / 구성) Management

Cấu hình (configuration / 구성) item là sản phẩm tạo ra (artifact / 산출물) được quản lý phiên bản (version / 버전)/cấu hình (configuration / 구성). Các activity thường gặp: identification, phiên bản (version / 버전) điều khiển (control / 제어), thay đổi (change / 변경) điều khiển (control / 제어), cấu hình (configuration / 구성) kiểm tra (audit / 감사)/status accounting.

Git là phân tán (distributed / 분산) phiên bản (version / 버전) điều khiển (control / 제어). SVN là centralized. Không suy luận rằng phân tán (distributed / 분산) luôn tốt hơn; đề thường hỏi đúng thuộc tính kiến trúc.

### DRM

DRM — Digital Rights Management — quản lý quyền sử dụng nội dung số. Thành phần có thể gồm content provider, distributor, clearing house, bên tiêu thụ (consumer / 소비자), license, packaging, encryption/key management.

Phân biệt DRM với encryption: encryption bảo mật dữ liệu bằng biến đổi cryptographic; DRM là hệ thống quản lý **quyền sử dụng và phân phối**, trong đó encryption có thể chỉ là một cơ chế.

### Bản dựng (build / 빌드) automation / CI

Bản dựng (build / 빌드) automation biến nguồn (source / 소스) + phụ thuộc (dependency / 의존성) thành sản phẩm tạo ra (artifact / 산출물) có thể deploy lặp lại. CI thường chạy bản dựng (build / 빌드)/kiểm thử (test / 테스트) mỗi khi thay đổi mã (code / 코드). Jenkins là automation máy chủ (server / 서버); Gradle là bản dựng (build / 빌드) automation công cụ (tool / 도구). Không coi hai công cụ (tool / 도구) là cùng loại chỉ vì cả hai có thể xuất hiện trong chuỗi xử lý (pipeline / 파이프라인).

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **2.4 애플리케이션 테스트 관리 — ứng dụng (application / 애플리케이션) kiểm thử (test / 테스트) management** nối từ **2.3 제품 소프트웨어 패키징 — sản phẩm (product / 제품) software packaging** sang **2.5 인터페이스 구현 — giao diện (interface / 인터페이스) hiện thực (implementation / 구현)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2.4 애플리케이션 테스트 관리 — ứng dụng (application / 애플리케이션) kiểm thử (test / 테스트) management

### Kiểm thử (test / 테스트) principle

Testing phát hiện defect, không chứng minh hệ thống “không có lỗi”. Exhaustive testing gần như không khả thi. Defect clustering gợi ý lỗi tập trung ở một số mô-đun (module / 모듈). Pesticide paradox nói rằng lặp mãi cùng bộ kiểm thử (test / 테스트) sẽ giảm khả năng tìm lỗi mới, nên kiểm thử (test / 테스트) cần được xem xét/cập nhật.

### Static vs động (dynamic / 동적)

Static testing không chạy mã (code / 코드): rà soát (review / 검토), walkthrough, inspection, static phân tích (analysis / 분석). động (dynamic / 동적) testing chạy software với đầu vào (input / 입력)/trạng thái (state / 상태) cụ thể.

### White-box vs Black-box

White-box nhìn cấu trúc bên trong. Coverage cần hiểu:

Statement coverage: mọi statement được chạy ít nhất một lần.
quyết định (decision / 결정)/Branch coverage: mỗi branch true/false được chạy.
điều kiện (condition / 조건) coverage: từng atomic điều kiện (condition / 조건) nhận true và false.
điều kiện (condition / 조건)/quyết định (decision / 결정) và MC/DC là mức mạnh hơn tùy phạm vi tài liệu.

Black-box tập trung đầu vào (input / 입력)/đầu ra (output / 출력) theo specification: equivalence partitioning, ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석), quyết định (decision / 결정) bảng (table / 테이블), chuyển tiếp trạng thái (state transition / 상태 전이), cause-effect đồ thị (graph / 그래프), lỗi (error / 오류) guessing.

Ví dụ trường tuổi hợp lệ 18–65: ranh giới (boundary / 경계) giá trị (value / 값) nên kiểm tra quanh 18 và 65 như 17,18,19,64,65,66 thay vì chỉ nhiều giá trị ngẫu nhiên ở giữa.

### Kiểm thử (test / 테스트) mức (level / 수준)

Đơn vị (unit / 단위) → tích hợp (integration / 통합) → hệ thống (system / 시스템) → Acceptance.

Top-down tích hợp (integration / 통합) dùng **stub** thay mô-đun (module / 모듈) cấp dưới chưa có. Bottom-up dùng **driver** thay mô-đun (module / 모듈) cấp trên chưa có. Đây là cặp rất dễ bị đảo.

Regression testing kiểm tra thay đổi mới không làm hỏng chức năng cũ. Smoke testing kiểm tra nhanh bản dựng (build / 빌드) có đủ ổn để kiểm thử (test / 테스트) sâu hơn. Alpha thường tại môi trường nhà phát triển (developer / 개발자)/organization; beta tại môi trường người dùng (user / 사용자) thực tế với nhóm người dùng bên ngoài.

### Kiểm thử (test / 테스트) oracle

True oracle, sampling oracle, heuristic oracle, consistent oracle được phân loại theo mức biết trước expected kết quả (result / 결과). Đề thường hỏi định nghĩa; hãy gắn “oracle = nguồn quyết định expected kết quả (result / 결과) đúng”.

### Hiệu năng (performance / 성능)

Phản hồi (response / 응답) thời gian (time / 시간) là thời gian từ yêu cầu (request / 요청) đến phản hồi (response / 응답). thông lượng (throughput / 처리량) là lượng công việc trong một đơn vị thời gian. tài nguyên (resource / 자원) usage là CPU/bộ nhớ (memory / 메모리)/I/O/mạng (network / 네트워크) consumption. độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량) không phải hai cách gọi cùng một thứ.

Cyclomatic độ phức tạp (complexity / 복잡도) có thể tính từ control-flow đồ thị (graph / 그래프) theo `M = E - N + 2P`, hoặc với đồ thị (graph / 그래프) connected đơn giản thường là số quyết định (decision / 결정) + 1. Nó liên quan số independent đường dẫn (path / 경로) tối thiểu để basis đường dẫn (path / 경로) testing.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **2.5 인터페이스 구현 — giao diện (interface / 인터페이스) hiện thực (implementation / 구현)** nối từ **2.4 애플리케이션 테스트 관리 — ứng dụng (application / 애플리케이션) kiểm thử (test / 테스트) management** sang **3.1 논리 데이터베이스 설계 — Logical DB thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2.5 인터페이스 구현 — giao diện (interface / 인터페이스) hiện thực (implementation / 구현)

Giao diện (interface / 인터페이스) hiện thực (implementation / 구현) cần kiểm tra message/dữ liệu (data / 데이터) format, ánh xạ (mapping / 매핑), giao thức (protocol / 프로토콜), bảo mật (security / 보안), logging, exception handling và thử lại (retry / 재시도)/idempotency.

Mạng (network / 네트워크) bảo mật (security / 보안) có thể dùng TLS/VPN; ứng dụng (application / 애플리케이션)/giao diện (interface / 인터페이스) tầng (layer / 계층) cần authentication, authorization, đầu vào (input / 입력) kiểm tra hợp lệ (validation / 검증), message integrity và secret management. Không coi “mã hóa đường truyền” là đủ bảo mật cho toàn bộ giao diện (interface / 인터페이스).

---

# 3. 데이터베이스 구축 — cơ sở dữ liệu (database / 데이터베이스) Construction

Môn 3 nên học theo chuỗi **mô hình (model / 모델) → key/phụ thuộc (dependency / 의존성) → normalization → vật lý (physical / 물리적) thiết kế (design / 설계) → SQL → giao dịch (transaction / 트랜잭션)/tính đồng thời (concurrency / 동시성)/khôi phục (recovery / 복구)**. Nếu tách SQL khỏi relational mô hình (model / 모델) sẽ dễ làm đúng câu cú pháp (syntax / 문법) nhưng sai câu lý thuyết.

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **3.1 논리 데이터베이스 설계 — Logical DB thiết kế (design / 설계)** nối từ **2.5 인터페이스 구현 — giao diện (interface / 인터페이스) hiện thực (implementation / 구현)** sang **3.2 물리 데이터베이스 설계 — vật lý (physical / 물리적) DB thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3.1 논리 데이터베이스 설계 — Logical DB thiết kế (design / 설계)

### DBMS và three-schema kiến trúc (architecture / 아키텍처)

Bên ngoài (external / 외부) lược đồ (schema / 스키마) — 외부 스키마 — view của người dùng (user / 사용자)/ứng dụng (application / 애플리케이션).
Conceptual lược đồ (schema / 스키마) — 개념 스키마 — cấu trúc lô-gic (logic / 논리) tổng thể.
nội bộ (internal / 내부) lược đồ (schema / 스키마) — 내부 스키마 — cách lưu trữ vật lý.

Dữ liệu (data / 데이터) independence:

Logical dữ liệu (data / 데이터) independence: thay conceptual lược đồ (schema / 스키마) mà hạn chế ảnh hưởng bên ngoài (external / 외부) lược đồ (schema / 스키마).
vật lý (physical / 물리적) dữ liệu (data / 데이터) independence: thay nội bộ (internal / 내부) lưu trữ (storage / 저장소) mà hạn chế ảnh hưởng conceptual/bên ngoài (external / 외부) lược đồ (schema / 스키마).

### Thực thể (entity / 엔터티)–Relationship mô hình (model / 모델)

Thực thể (entity / 엔터티) là đối tượng cần quản lý. Attribute mô tả thực thể (entity / 엔터티). Relationship biểu diễn liên hệ giữa thực thể (entity / 엔터티). Cardinality 1:1, 1:N, M:N cho biết số instance có thể liên kết.

M:N thường phải giải quyết bằng associative/junction bảng (table / 테이블) khi chuyển sang relational lược đồ (schema / 스키마).

### Key

Super key: tập attribute xác định duy nhất tuple.
Candidate key: super key tối thiểu.
Primary key: candidate key được chọn chính.
Alternate key: candidate key không được chọn làm primary.
Foreign key: attribute tham chiếu key của quan hệ (relation / 관계) khác/cùng quan hệ (relation / 관계).
Composite key: key gồm nhiều attribute.

Minimality áp dụng cho candidate key: bỏ bất kỳ attribute nào thì không còn uniqueness.

### Functional phụ thuộc (dependency / 의존성)

`X → Y` nghĩa là mỗi giá trị X xác định duy nhất Y trong quan hệ (relation / 관계) hợp lệ. Functional phụ thuộc (dependency / 의존성) là nền của normalization.

Partial phụ thuộc (dependency / 의존성): non-prime attribute phụ thuộc một phần composite candidate key.
Transitive phụ thuộc (dependency / 의존성): key → A và A → B, B không phụ thuộc trực tiếp key theo dạng cần loại bỏ ở 3NF.

### Normalization

1NF: attribute atomic, không repeating group theo mô hình quan hệ thông thường.
2NF: 1NF + không partial phụ thuộc (dependency / 의존성) của non-prime attribute vào candidate key.
3NF: 2NF + loại transitive phụ thuộc (dependency / 의존성) không phù hợp.
BCNF: với mọi non-trivial FD `X → Y`, X phải là super key.
4NF: xử lý multivalued phụ thuộc (dependency / 의존성).
5NF: xử lý phép nối (join / 조인) phụ thuộc (dependency / 의존성).

Ví dụ `Enrollment(student_id, course_id, student_name, course_name, grade)` có key `(student_id, course_id)`. `student_name` chỉ phụ thuộc `student_id`, `course_name` chỉ phụ thuộc `course_id`, nên có partial dependencies → chưa đạt 2NF.

Normalization giảm redundancy và anomaly nhưng có thể tăng số phép nối (join / 조인); denormalization đôi khi được dùng có chủ đích vì hiệu năng (performance / 성능), không có nghĩa normalization “sai”.

### Relational algebra

Selection `σ`: chọn row.
Projection `π`: chọn column.
phép nối (join / 조인): kết hợp quan hệ (relation / 관계) theo điều kiện (condition / 조건).
Union, Difference, Cartesian sản phẩm (product / 제품), Intersection, Division cần nhận diện ý nghĩa.

Đừng nhầm SELECT của SQL với Selection của relational algebra: SQL `SELECT column` gần projection; SQL `WHERE` gần selection.

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **3.2 물리 데이터베이스 설계 — vật lý (physical / 물리적) DB thiết kế (design / 설계)** nối từ **3.1 논리 데이터베이스 설계 — Logical DB thiết kế (design / 설계)** sang **3.3 SQL 활용 — SQL utilization**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3.2 물리 데이터베이스 설계 — vật lý (physical / 물리적) DB thiết kế (design / 설계)

Vật lý (physical / 물리적) thiết kế (design / 설계) chuyển logical mô hình (model / 모델) thành cấu trúc (structure / 구조) tối ưu lưu trữ/truy cập.

Chỉ mục (index / 인덱스) tăng tốc read nhưng tốn lưu trữ (storage / 저장소) và làm ghi (write / 쓰기)/cập nhật (update / 업데이트) có thêm chi phí (cost / 비용). B-tree/B+cây (tree / 트리) phù hợp phạm vi (range / 범위) tìm kiếm (search / 검색) và ordered truy cập (access / 접근). băm (hash / 해시) chỉ mục (index / 인덱스) phù hợp equality lookup nhưng không tự nhiên cho phạm vi (range / 범위) truy vấn (query / 쿼리).

Clustered organization ảnh hưởng thứ tự lưu vật lý/logical locality tùy DBMS; non-clustered chỉ mục (index / 인덱스) giữ cấu trúc chỉ mục (index / 인덱스) riêng trỏ về row/page. Cần đọc theo khái niệm chung, không áp một DBMS cụ thể cho mọi câu hỏi.

Partitioning chia dữ liệu thành partition theo phạm vi (range / 범위)/danh sách (list / 목록)/băm (hash / 해시)/composite. Horizontal partition chia row; vertical partition chia column.

Cơ sở dữ liệu (database / 데이터베이스) integrity:

Thực thể (entity / 엔터티) integrity: primary key không null và xác định tuple.
Referential integrity: foreign key phải tham chiếu giá trị tồn tại hoặc null nếu ràng buộc (constraint / 제약조건) cho phép.
lĩnh vực (domain / 도메인) integrity: giá trị thuộc lĩnh vực (domain / 도메인)/phạm vi (range / 범위)/kiểu (type / 타입) hợp lệ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **3.3 SQL 활용 — SQL utilization** nối từ **3.2 물리 데이터베이스 설계 — vật lý (physical / 물리적) DB thiết kế (design / 설계)** sang **3.4 SQL 응용 — SQL ứng dụng (application / 애플리케이션)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3.3 SQL 활용 — SQL utilization

### DDL / DML / DCL / TCL

DDL: CREATE, ALTER, DROP, TRUNCATE theo phân loại phổ biến.
DML: SELECT, INSERT, cập nhật (update / 업데이트), DELETE.
DCL: GRANT, REVOKE.
TCL: lần ghi nhận (commit / 커밋), quay lui (rollback / 롤백), SAVEPOINT trong cách phân loại hiện đại.

### SELECT thực thi (execution / 실행) lập luận (reasoning / 추론)

Logical processing thứ tự (order / 순서) hữu ích để giải câu khó:

FROM/phép nối (join / 조인) → WHERE → GROUP BY → HAVING → SELECT → thứ tự (order / 순서) BY.

`WHERE` lọc row trước grouping. `HAVING` lọc group sau aggregation.

```sql
SELECT department_id, COUNT(*) AS cnt
FROM employee
WHERE active = 'Y'
GROUP BY department_id
HAVING COUNT(*) >= 5;
```

Câu trên không phải “department có ít nhất 5 employee tổng cộng”, mà là có ít nhất 5 employee **active**, vì WHERE đã lọc trước GROUP BY.

### NULL

NULL là unknown/missing, không bằng 0 và không bằng empty string theo SQL tiêu chuẩn (standard / 표준). So sánh `col = NULL` không đúng cách; dùng `IS NULL` / `IS NOT NULL`.

SQL dùng three-valued lô-gic (logic / 논리) TRUE/FALSE/UNKNOWN. Điều này đặc biệt quan trọng với `NOT IN` khi subquery có NULL; trong thực tế nên hiểu ngữ nghĩa (semantics / 의미론) trước khi chọn đáp án.

### Phép nối (join / 조인)

INNER phép nối (join / 조인) chỉ row match. LEFT OUTER phép nối (join / 조인) giữ toàn bộ row bên trái. RIGHT OUTER phép nối (join / 조인) giữ bên phải. FULL OUTER phép nối (join / 조인) giữ cả hai phía. CROSS phép nối (join / 조인) tạo Cartesian sản phẩm (product / 제품).

Self phép nối (join / 조인) là cùng bảng (table / 테이블) xuất hiện nhiều alias để mô tả relationship nội bộ như employee-manager.

### Subquery

Scalar subquery trả một giá trị. Single-row/multi-row subquery cần operator phù hợp. `IN`, `EXISTS`, `ANY/SOME`, `ALL` có ngữ nghĩa (semantics / 의미론) khác nhau.

Correlated subquery phụ thuộc row của outer truy vấn (query / 쿼리) và được đánh giá lô-gic (logic / 논리) theo từng row outer; optimizer có thể rewrite nhưng khi giải đề hãy lập luận (reasoning / 추론) theo ngữ nghĩa (semantics / 의미론).

### Aggregate / cửa sổ (window / 윈도우)

COUNT(*), COUNT(column), SUM, AVG, MIN, MAX. `COUNT(column)` bỏ NULL; `COUNT(*)` đếm row.

Hàm cửa sổ (window function / 윈도우 함수) như `ROW_NUMBER`, `RANK`, `DENSE_RANK` không gom nhiều row thành một row như GROUP BY. `RANK` có gap khi tie; `DENSE_RANK` không có gap; `ROW_NUMBER` luôn tạo chuỗi (sequence / 시퀀스) duy nhất theo thứ tự (ordering / 순서) được định nghĩa.

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **3.4 SQL 응용 — SQL ứng dụng (application / 애플리케이션)** nối từ **3.3 SQL 활용 — SQL utilization** sang **3.5 데이터 전환 — dữ liệu (data / 데이터) conversion / di chuyển (migration / 마이그레이션)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3.4 SQL 응용 — SQL ứng dụng (application / 애플리케이션)

### Procedural SQL

Procedure thực hiện một chuỗi lô-gic (logic / 논리) và có thể có IN/OUT parameter. hàm (function / 함수) thường trả về giá trị (value / 값). Trigger tự động chạy khi sự kiện (event / 이벤트) phù hợp xảy ra. Cursor cho phép xử lý tập kết quả (result set / 결과 집합) theo row trong procedural ngữ cảnh (context / 맥락).

Tên cú pháp (syntax / 문법) cụ thể khác nhau giữa Oracle, PostgreSQL, MySQL, SQL máy chủ (server / 서버); đề thường hỏi concept hơn là vendor-specific cú pháp (syntax / 문법) sâu.

### Giao dịch (transaction / 트랜잭션) — 트랜잭션

ACID:

Atomicity — 원자성: toàn bộ hoặc không gì cả.
Consistency — 일관성: giao dịch (transaction / 트랜잭션) đưa DB từ valid trạng thái (state / 상태) sang valid trạng thái (state / 상태).
Isolation — 격리성: giao dịch (transaction / 트랜잭션) concurrent không gây quan sát sai theo isolation guarantee.
Durability — 영속성: lần ghi nhận (commit / 커밋) tồn tại sau thất bại (failure / 실패).

### Tính đồng thời (concurrency / 동시성) anomalies

Dirty read: đọc dữ liệu giao dịch (transaction / 트랜잭션) khác chưa lần ghi nhận (commit / 커밋).
Non-repeatable read: cùng row đọc hai lần cho kết quả khác vì giao dịch (transaction / 트랜잭션) khác lần ghi nhận (commit / 커밋) cập nhật (update / 업데이트).
Phantom read: cùng predicate truy vấn (query / 쿼리) thấy tập row khác vì insert/delete mới lần ghi nhận (commit / 커밋).

Lost cập nhật (update / 업데이트): hai giao dịch (transaction / 트랜잭션) cùng đọc rồi cập nhật (update / 업데이트), một cập nhật (update / 업데이트) ghi đè cập nhật (update / 업데이트) kia nếu tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) không ngăn.

### Locking / 2PL

Dùng chung (shared / 공유) khóa (lock / 잠금) cho read và có thể coexist với dùng chung (shared / 공유) khóa (lock / 잠금). Exclusive khóa (lock / 잠금) cho ghi (write / 쓰기) và xung đột với dùng chung (shared / 공유)/exclusive khóa (lock / 잠금) khác trên cùng tài nguyên (resource / 자원) theo ma trận (matrix / 행렬) thông thường.

Two-Phase Locking — 2PL có growing phase chỉ acquire khóa (lock / 잠금) và shrinking phase chỉ bản phát hành (release / 릴리스). Strict 2PL thường giữ exclusive locks đến lần ghi nhận (commit / 커밋)/quay lui (rollback / 롤백), giúp tránh cascading quay lui (rollback / 롤백) và tạo serializability phù hợp.

### Deadlock

Bốn điều kiện Coffman: mutual exclusion, hold and wait, no preemption, circular wait.

Prevention phá ít nhất một điều kiện. Avoidance dùng trạng thái safe/unsafe, ví dụ Banker’s thuật toán (algorithm / 알고리즘). Detection cho phép deadlock xảy ra rồi phát hiện cycle/wait-for đồ thị (graph / 그래프). khôi phục (recovery / 복구) abort/quay lui (rollback / 롤백)/preempt theo chiến lược.

### Khôi phục (recovery / 복구)

Log-based khôi phục (recovery / 복구) dùng before/after ảnh (image / 이미지) tùy giao thức (protocol / 프로토콜). Undo đảo giao dịch (transaction / 트랜잭션) chưa lần ghi nhận (commit / 커밋); redo áp lại giao dịch (transaction / 트랜잭션) đã lần ghi nhận (commit / 커밋) nhưng chưa flush đầy đủ. Checkpoint giảm lượng log phải quét khi khôi phục (recovery / 복구).

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **3.4 SQL 응용 — SQL ứng dụng (application / 애플리케이션)** đặt vấn đề; **3.5 데이터 전환 — dữ liệu (data / 데이터) conversion / di chuyển (migration / 마이그레이션)** đối chiếu bằng chứng, rồi **4.1 서버 프로그램 구현 — máy chủ (server / 서버) program hiện thực (implementation / 구현)** mở rộng hệ quả hoặc giới hạn liên quan.

## 3.5 데이터 전환 — dữ liệu (data / 데이터) conversion / di chuyển (migration / 마이그레이션)

Di chuyển (migration / 마이그레이션) cần extraction, cleansing, transformation, loading, kiểm tra hợp lệ (validation / 검증), reconciliation và quay lui (rollback / 롤백) plan. ánh xạ (mapping / 매핑) source-to-target phải quản lý kiểu (type / 타입), mã (code / 코드) conversion, null/default, key relationship.

Quan trọng: “tải (load / 로드) xong không lỗi” không đồng nghĩa dữ liệu (data / 데이터) conversion đúng. Cần kiểm tra count, checksum/aggregate, referential integrity, nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) và sampling/detail reconciliation.

---

# 4. 프로그래밍 언어 활용 — Programming ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)

Đây là môn cần chuyển từ học thuộc sang **dấu vết (trace / 추적) thực thi (execution / 실행)**. Chỉ đọc cú pháp (syntax / 문법) không đủ. Mỗi đoạn mã (code / 코드) phải tự mô phỏng variable/trạng thái (state / 상태)/ngăn xếp lời gọi (call stack / 호출 스택).

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **3.5 데이터 전환 — dữ liệu (data / 데이터) conversion / di chuyển (migration / 마이그레이션)** đặt vấn đề; **4.1 서버 프로그램 구현 — máy chủ (server / 서버) program hiện thực (implementation / 구현)** đối chiếu bằng chứng, rồi **4.2 프로그래밍 언어 활용 — ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)** mở rộng hệ quả hoặc giới hạn liên quan.

## 4.1 서버 프로그램 구현 — máy chủ (server / 서버) program hiện thực (implementation / 구현)

Development môi trường (environment / 환경) gồm IDE/editor, trình biên dịch (compiler / 컴파일러)/trình thông dịch (interpreter / 인터프리터), bản dựng (build / 빌드) công cụ (tool / 도구), phụ thuộc (dependency / 의존성) manager, phiên bản (version / 버전) điều khiển (control / 제어), thời gian chạy (runtime / 런타임), DB, middleware, kiểm thử (test / 테스트)/gỡ lỗi (debug / 디버그) công cụ (tool / 도구).

Máy chủ (server / 서버) program thường phân lớp presentation/controller → dịch vụ (service / 서비스)/nghiệp vụ (business / 비즈니스) → dữ liệu (data / 데이터) truy cập (access / 접근)/repository. Layering giảm coupling nhưng không có nghĩa mọi hệ thống bắt buộc cùng một kiến trúc (architecture / 아키텍처).

Batch program xử lý lượng công việc định kỳ hoặc theo lịch, khác interactive yêu cầu (request / 요청)/phản hồi (response / 응답). Cần hiểu scheduling, logging, thử lại (retry / 재시도), idempotency, checkpoint khi job dài.

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **4.2 프로그래밍 언어 활용 — ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)** nối từ **4.1 서버 프로그램 구현 — máy chủ (server / 서버) program hiện thực (implementation / 구현)** sang **4.3 응용 SW 기초 기술 활용 — Basic ứng dụng (application / 애플리케이션) software technologies**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4.2 프로그래밍 언어 활용 — ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)

### Dữ liệu (data / 데이터) kiểu (type / 타입) / operator

Phải nắm integer vs floating-point, signed/unsigned ở C khi có phạm vi, boolean, char/string, array/danh sách (list / 목록), đối tượng (object / 객체)/tham chiếu (reference / 참조).

Operator precedence chỉ nên học các nhóm quan trọng và dùng ngoặc khi tự viết. Khi thi dấu vết (trace / 추적) mã (code / 코드), đừng dựa vào cảm giác. Ghi từng bước: unary → multiplicative → additive → comparison → equality → logical AND/OR → assignment theo ngôn ngữ cụ thể.

Short-circuit: `A && B` không evaluate B nếu A false; `A || B` không evaluate B nếu A true. Điều này có thể làm side tác động (effect / 효과) không xảy ra.

### C

C dễ ra pointer, array, string, hàm (function / 함수), struct, operator.

`int *p` là pointer tới int. `*p` dereference lấy/ghi giá trị (value / 값) tại address. `&x` lấy address của x.

Array name trong nhiều expression decay thành pointer tới first element, nhưng array và pointer không hoàn toàn là cùng một kiểu (type / 타입)/đối tượng. `p + 1` tăng theo kích thước (size / 크기) của pointed kiểu (type / 타입), không phải luôn tăng 1 byte.

Ví dụ:

```c
int a[] = {10, 20, 30};
int *p = a;
printf("%d", *(p + 2));
```

Kết quả là `30` vì `p + 2` trỏ tới `a[2]`.

C string kết thúc bằng `\0`. Buffer kích thước (size / 크기) phải tính cả terminator. Câu hỏi về `strlen` và `sizeof` rất dễ nhầm: `strlen` đếm character trước `\0`; `sizeof(array)` cho kích thước array theo byte trong phạm vi (scope / 범위) còn là array.

Pre-increment `++i` tăng rồi trả giá trị (value / 값) mới; post-increment `i++` trả giá trị (value / 값) cũ rồi tăng. Với expression phức tạp có nhiều side tác động (effect / 효과) lên cùng variable, tránh suy luận nếu hành vi (behavior / 동작) không được định nghĩa rõ trong C; đề chuẩn thường tránh undefined hành vi (behavior / 동작).

### Java

Java thành phần nguyên thủy (primitive / 기본 요소) khác tham chiếu (reference / 참조). `==` với thành phần nguyên thủy (primitive / 기본 요소) so giá trị (value / 값); với đối tượng (object / 객체) tham chiếu (reference / 참조) kiểm tra tham chiếu (reference / 참조) định danh (identity / 식별자), trong khi `.equals()` thường dùng giá trị (value / 값) equality nếu lớp (class / 클래스) override đúng.

Inheritance + overriding tạo động (dynamic / 동적) dispatch.

```java
class A { void f(){ System.out.print("A"); } }
class B extends A { @Override void f(){ System.out.print("B"); } }
A x = new B();
x.f();
```

In `B` vì thời gian chạy (runtime / 런타임) đối tượng (object / 객체) là `B` và phương thức (method / 메서드) bị override.

Overloading được chọn theo signature/compile-time ngữ cảnh (context / 맥락); overriding theo thời gian chạy (runtime / 런타임) dispatch cho instance phương thức (method / 메서드).

`static` member thuộc lớp (class / 클래스), không phải polymorphism kiểu instance overriding thông thường. `final` có nghĩa khác theo ngữ cảnh (context / 맥락): variable không reassign, phương thức (method / 메서드) không override, lớp (class / 클래스) không extend.

Exception: checked và unchecked là phân loại quan trọng. `try-catch-finally`; `finally` thường chạy dù có exception/return, trừ các tình huống thời gian chạy (runtime / 런타임) termination đặc biệt.

### Python

Python động (dynamic / 동적) typing nhưng đối tượng (object / 객체) vẫn có kiểu (type / 타입). danh sách (list / 목록) mutable; tuple immutable; set unique unordered theo ngữ nghĩa (semantic / 의미적); dict map key→giá trị (value / 값).

Slicing `a[start:stop:step]` không gồm `stop`.

```python
x = [0, 1, 2, 3, 4]
print(x[1:4])
```

Kết quả `[1, 2, 3]`.

Mutable aliasing rất dễ ra dạng suy luận:

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

`a` cũng thành `[1, 2, 3]` vì `a` và `b` cùng tham chiếu (reference / 참조) danh sách (list / 목록) đối tượng (object / 객체).

`is` kiểm tra định danh (identity / 식별자); `==` kiểm tra equality. Không dùng `is` như thay thế chung cho `==`.

### Recursion

Recursion phải có cơ sở (base / 기반) trường hợp (case / 사례) và tiến về cơ sở (base / 기반) trường hợp (case / 사례). Khi dấu vết (trace / 추적), ghi ngăn xếp lời gọi (call stack / 호출 스택) từ ngoài vào rồi unwind ngược ra.

Ví dụ factorial `f(4)` tạo `4 * f(3)`, `3 * f(2)`, `2 * f(1)`, sau đó trả ngược.

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **4.3 응용 SW 기초 기술 활용 — Basic ứng dụng (application / 애플리케이션) software technologies** nối từ **4.2 프로그래밍 언어 활용 — ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)** sang **5.1 소프트웨어 개발 방법론 활용 — Software development methodology**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4.3 응용 SW 기초 기술 활용 — Basic ứng dụng (application / 애플리케이션) software technologies

### Operating hệ thống (system / 시스템)

Tiến trình (process / 프로세스) là chương trình đang thực thi với address không gian (space / 공간)/resources riêng; luồng thực thi (thread / 스레드) là đơn vị (unit / 단위) thực thi (execution / 실행) trong tiến trình (process / 프로세스) và thường share address không gian (space / 공간)/resources với luồng thực thi (thread / 스레드) cùng tiến trình (process / 프로세스).

Tiến trình (process / 프로세스) states thường gồm New, Ready, Running, Waiting/Blocked, Terminated. ngữ cảnh (context / 맥락) switch lưu/khôi phục ngữ cảnh (context / 맥락) khi CPU đổi thực thi (execution / 실행) thực thể (entity / 엔터티).

### CPU scheduling

FCFS: đơn giản nhưng có convoy tác động (effect / 효과).
SJF: chọn burst ngắn nhất, tối ưu average waiting trong điều kiện biết burst nhưng dễ starvation.
SRTF: preemptive SJF.
Priority: chọn priority cao; low priority có thể starvation, aging giảm starvation.
Round Robin: thời gian (time / 시간) quantum; quantum quá lớn gần FCFS, quá nhỏ làm context-switch overhead cao.

Khi gặp bài tính turnaround/waiting thời gian (time / 시간), vẽ Gantt chart trước rồi tính:

Turnaround = completion − arrival.
Waiting = turnaround − burst (nếu chỉ một CPU burst tổng quát).

### Bộ nhớ (memory / 메모리)

Paging chia logical bộ nhớ (memory / 메모리) thành fixed-size page, vật lý (physical / 물리적) bộ nhớ (memory / 메모리) thành frame. Bảng trang (page table / 페이지 테이블) map page→frame. nội bộ (internal / 내부) fragmentation có thể xuất hiện ở page cuối; paging tránh bên ngoài (external / 외부) fragmentation theo mô hình cơ bản.

Segmentation chia theo logical đơn vị (unit / 단위) variable-size và có thể bên ngoài (external / 외부) fragmentation.

Virtual bộ nhớ (memory / 메모리) dùng page replacement khi page fault và frame cần thay.

FIFO thay page vào sớm nhất; có thể gặp Belady’s anomaly. LRU thay page lâu nhất chưa dùng. Optimal thay page sẽ được dùng xa nhất trong tương lai, dùng làm benchmark vì thời gian chạy (runtime / 런타임) không biết tương lai.

### Deadlock

Cùng 4 điều kiện Coffman đã nêu ở DB/hệ thống (system / 시스템) tính đồng thời (concurrency / 동시성). Hãy liên kết thay vì học hai lần tách biệt.

### Mạng (network / 네트워크)

OSI 7 layers:

7 ứng dụng (application / 애플리케이션)
6 Presentation
5 Session
4 vận chuyển (transport / 전송)
3 mạng (network / 네트워크)
2 dữ liệu (data / 데이터) Link
1 vật lý (physical / 물리적)

TCP/IP mô hình (model / 모델) thường gộp thành ứng dụng (application / 애플리케이션), vận chuyển (transport / 전송), Internet, truy cập mạng (network access / 네트워크 접근)/Link.

TCP connection-oriented, reliable byte stream, sequencing, ACK/retransmission, luồng (flow / 흐름)/congestion điều khiển (control / 제어). UDP connectionless, datagram, overhead thấp, không bảo đảm delivery/thứ tự (order / 순서) ở giao thức (protocol / 프로토콜) tầng (layer / 계층).

IP routing thuộc mạng (network / 네트워크) tầng (layer / 계층). Ethernet/MAC switching thuộc dữ liệu (data / 데이터) Link. TCP/UDP thuộc vận chuyển (transport / 전송). HTTP/DNS/SMTP ứng dụng (application / 애플리케이션) protocols.

### IPv4 subnetting

CIDR `/n` nghĩa n bit mạng (network / 네트워크) prefix. Số IPv4 address trong subnet = `2^(32-n)`. Trong subnet truyền thống, usable host thường = total − 2 (network + broadcast), nhưng một số special subnet như /31 có ngữ nghĩa (semantics / 의미론) đặc biệt; câu thi cơ bản thường dùng công thức truyền thống.

Ví dụ `/26`: `2^(6)=64` address, thông thường 62 usable host.

### Dùng chung (common / 공통) giao thức (protocol / 프로토콜)/cổng (port / 포트) associations

Không nên chỉ học cổng (port / 포트) number, nhưng các cặp kinh điển cần nhận diện: HTTP 80, HTTPS 443, SSH 22, FTP điều khiển (control / 제어) 21, DNS 53, SMTP 25, POP3 110, IMAP 143. Hãy nhớ đây là well-known defaults; thực tế dịch vụ (service / 서비스) có thể cấu hình cổng (port / 포트) khác.

---

# 5. 정보시스템 구축관리 — thông tin (information / 정보) hệ thống (system / 시스템) Construction Management

Môn 5 rộng nhất về management + hạ tầng (infrastructure / 인프라) + bảo mật (security / 보안). Đây là môn dễ bị “biết IT nhưng vẫn sai” vì nhiều thuật ngữ bảo mật và quản lý có định nghĩa rất sát nhau.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **5.1 소프트웨어 개발 방법론 활용 — Software development methodology** nối từ **4.3 응용 SW 기초 기술 활용 — Basic ứng dụng (application / 애플리케이션) software technologies** sang **5.2 IT 프로젝트 정보시스템 구축관리 — IT dự án (project / 프로젝트) / hạ tầng (infrastructure / 인프라) construction management**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5.1 소프트웨어 개발 방법론 활용 — Software development methodology

Waterfall đi theo phase tương đối tuần tự, phù hợp khi yêu cầu (requirement / 요구사항) ổn định và quản trị (governance / 거버넌스) cần checkpoint rõ. Prototype dùng bản mẫu để làm rõ yêu cầu (requirement / 요구사항)/UX. Spiral lặp theo vòng và nhấn mạnh rủi ro (risk / 위험) phân tích (analysis / 분석). Iterative/Incremental phát triển qua nhiều iteration/increment. Agile thích nghi phản hồi (feedback / 피드백) nhanh.

### Estimation

COCOMO truyền thống ước lượng effort theo KLOC và dự án (project / 프로젝트) chế độ (mode / 모드) (Organic, Semi-detached, Embedded) với coefficient khác nhau. Không cần chỉ thuộc hệ số nếu tài liệu/출제기준 không yêu cầu chi tiết công thức, nhưng phải hiểu đầu vào (input / 입력)/đầu ra (output / 출력) và ý nghĩa chế độ (mode / 모드).

Hàm (function / 함수) điểm (point / 지점) đo kích thước chức năng nhìn từ người dùng (user / 사용자), dùng các thành phần như bên ngoài (external / 외부) đầu vào (input / 입력)/đầu ra (output / 출력)/inquiry, nội bộ (internal / 내부) logical tệp (file / 파일), bên ngoài (external / 외부) giao diện (interface / 인터페이스) tệp (file / 파일) trong mô hình truyền thống. Khác KLOC vì không phụ thuộc trực tiếp số dòng mã (code / 코드).

### Tailoring

Methodology tailoring là điều chỉnh tiến trình (process / 프로세스)/sản phẩm tạo ra (artifact / 산출물)/điều khiển (control / 제어) phù hợp kích thước (size / 크기), rủi ro (risk / 위험), nhóm (team / 팀), lĩnh vực (domain / 도메인), compliance. Tailoring không có nghĩa tùy tiện bỏ phase; phải giữ các điều khiển (control / 제어) cần thiết theo rủi ro (risk / 위험) và yêu cầu (requirement / 요구사항).

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **5.2 IT 프로젝트 정보시스템 구축관리 — IT dự án (project / 프로젝트) / hạ tầng (infrastructure / 인프라) construction management** nối từ **5.1 소프트웨어 개발 방법론 활용 — Software development methodology** sang **5.3 소프트웨어 개발 보안 구축 — Secure software development**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5.2 IT 프로젝트 정보시스템 구축관리 — IT dự án (project / 프로젝트) / hạ tầng (infrastructure / 인프라) construction management

Phần này cần phủ mạng (network / 네트워크), software, hardware, cơ sở dữ liệu (database / 데이터베이스) và vận hành.

### Mạng (network / 네트워크) construction

Switch chủ yếu forward frame dựa trên MAC ở L2; router forward packet dựa trên IP ở L3. L3 switch có routing năng lực (capability / 역량). VLAN chia broadcast lĩnh vực (domain / 도메인) lô-gic (logic / 논리). NAT chuyển đổi address; PAT/NAPT dùng cổng (port / 포트) để nhiều private host share công khai (public / 공개) IP.

Firewall kiểm soát traffic theo quy tắc (rule / 규칙). IDS phát hiện và cảnh báo; IPS có thể chặn/prevent inline. WAF tập trung HTTP/web ứng dụng (application / 애플리케이션) traffic. VPN tạo encrypted tunnel qua mạng (network / 네트워크) không tin cậy.

Bộ cân bằng tải (load balancer / 로드 밸런서) phân phối traffic qua nhiều backend; health check giúp tránh gửi yêu cầu (request / 요청) đến instance lỗi. L4 tải (load / 로드) balancing dựa vận chuyển (transport / 전송) thông tin (information / 정보); L7 hiểu ứng dụng (application / 애플리케이션) giao thức (protocol / 프로토콜) như HTTP và có thể tuyến (route / 경로) theo host/đường dẫn (path / 경로)/header.

### Hardware / lưu trữ (storage / 저장소)

RAID cần hiểu mục tiêu sức chứa (capacity / 용량), hiệu năng (performance / 성능), redundancy:

RAID 0: striping, không redundancy.
RAID 1: mirroring.
RAID 5: striping + phân tán (distributed / 분산) single parity, chịu một disk thất bại (failure / 실패).
RAID 6: dual parity, chịu hai disk failures.
RAID 10: mirror + stripe, cần nhiều disk nhưng hiệu năng (performance / 성능)/redundancy tốt.

RAID không thay backup. RAID xử lý disk thất bại (failure / 실패); backup xử lý deletion, corruption, ransomware, disaster theo retention/phiên bản (version / 버전).

### Virtualization / Cloud / bộ chứa (container / 컨테이너)

Virtual machine virtualize hardware và chạy guest OS riêng. bộ chứa (container / 컨테이너) share host kernel theo mô hình phổ biến và isolate tiến trình (process / 프로세스)/filesystem/mạng (network / 네트워크) không gian tên (namespace / 네임스페이스), nhẹ hơn VM nhưng ranh giới (boundary / 경계) khác.

IaaS cung cấp compute/mạng (network / 네트워크)/lưu trữ (storage / 저장소) cơ bản. PaaS cung cấp nền tảng (platform / 플랫폼)/thời gian chạy (runtime / 런타임) để deploy app. SaaS cung cấp ứng dụng (application / 애플리케이션) hoàn chỉnh.

Công khai (public / 공개)/private/hybrid cloud nói về triển khai (deployment / 배포) mô hình (model / 모델), khác IaaS/PaaS/SaaS là dịch vụ (service / 서비스) mô hình (model / 모델).

### Availability / DR

Availability khác độ tin cậy (reliability / 신뢰성). Availability quan tâm tỷ lệ hệ thống sẵn sàng; độ tin cậy (reliability / 신뢰성) khả năng hoạt động đúng liên tục trong khoảng thời gian.

RTO — khôi phục (recovery / 복구) thời gian (time / 시간) mục tiêu (objective / 목표): thời gian downtime tối đa mục tiêu.
RPO — khôi phục (recovery / 복구) điểm (point / 지점) mục tiêu (objective / 목표): mức dữ liệu (data / 데이터) mất mát (loss / 손실) theo thời gian có thể chấp nhận.

Nếu RPO = 15 phút, backup/replication chiến lược (strategy / 전략) phải đủ để mất tối đa khoảng 15 phút dữ liệu theo mục tiêu (objective / 목표). Nếu RTO = 1 giờ, dịch vụ (service / 서비스) cần được khôi phục trong mục tiêu (target / 대상) một giờ.

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **5.3 소프트웨어 개발 보안 구축 — Secure software development** nối từ **5.2 IT 프로젝트 정보시스템 구축관리 — IT dự án (project / 프로젝트) / hạ tầng (infrastructure / 인프라) construction management** sang **5.4 시스템 보안 구축 — hệ thống (system / 시스템) bảo mật (security / 보안) construction**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5.3 소프트웨어 개발 보안 구축 — Secure software development

### CIA triad

Confidentiality — 기밀성: chỉ chủ thể được phép đọc.
Integrity — 무결성: dữ liệu không bị sửa trái phép.
Availability — 가용성: dịch vụ/dữ liệu sẵn sàng khi cần.

Authentication — 인증 — “bạn là ai?”.
Authorization — 인가 — “bạn được làm gì?”.
Accounting/Auditing — 기록/감사 — “đã làm gì?”.

### Cryptography

Symmetric encryption dùng cùng/dùng chung (shared / 공유) secret key, nhanh, phù hợp bulk encryption nhưng key phân phối (distribution / 분포) khó. AES là ví dụ phổ biến.

Asymmetric encryption dùng công khai (public / 공개)/private key pair, hỗ trợ key exchange, encryption/signature theo thuật toán (algorithm / 알고리즘)/use trường hợp (case / 사례), nhưng chậm hơn. RSA/ECC là ví dụ family phổ biến.

Băm (hash / 해시) hàm (function / 함수) là one-way ánh xạ (mapping / 매핑), không phải encryption vì không có decrypt key. SHA-2/SHA-3 là băm (hash / 해시) families. Password nên dùng password hashing KDF có salt và chi phí (cost / 비용) như PBKDF2/bcrypt/scrypt/Argon2 trong thực tế; không lưu plain SHA-256 password đơn thuần.

Digital signature thường băm (hash / 해시) message rồi ký digest bằng private key theo scheme; verifier dùng công khai (public / 공개) key để kiểm tra authenticity/integrity/non-repudiation theo các giả định (assumptions / 가정들) phù hợp.

### Dùng chung (common / 공통) attack classes

SQL Injection: đầu vào (input / 입력) bị ghép thành SQL làm thay đổi truy vấn (query / 쿼리). Defense chính: parameterized truy vấn (query / 쿼리)/prepared statement, kiểm tra hợp lệ (validation / 검증) và least privilege.

XSS: attacker đưa script/content hoạt động trong trình duyệt (browser / 브라우저) ngữ cảnh (context / 맥락). Stored, Reflected, DOM-based là các loại phổ biến. Defense: context-aware đầu ra (output / 출력) encoding, safe templating, CSP hỗ trợ, kiểm tra hợp lệ (validation / 검증)/sanitization phù hợp.

CSRF: trình duyệt (browser / 브라우저) của người dùng (user / 사용자) đã authenticated bị dụ gửi yêu cầu (request / 요청) ngoài ý muốn. Defense: CSRF đơn vị từ (token / 토큰), SameSite cookie, kiểm tra origin/re-authentication tùy thao tác (operation / 연산).

Command Injection: untrusted đầu vào (input / 입력) điều khiển OS command. Dùng API thay shell, allowlist và escaping đúng ngữ cảnh (context / 맥락) nếu buộc phải invoke shell.

Đường dẫn (path / 경로) Traversal: `../` hoặc biến thể vượt thư mục cho phép. Canonicalize/resolve đường dẫn (path / 경로), allowlist cơ sở (base / 기반) đường dẫn (path / 경로) và kiểm tra containment.

Buffer Overflow: ghi vượt bộ nhớ (memory / 메모리) ranh giới (boundary / 경계), đặc biệt C/C++. Defense gồm memory-safe ngôn ngữ (language / 언어), bounds checking, ASLR, ngăn xếp (stack / 스택) canary, DEP/NX nhưng prevention ở nguồn (source / 소스) vẫn quan trọng.

Race điều kiện (condition / 조건)/TOCTOU: trạng thái (state / 상태) thay đổi giữa check và use. Dùng atomic thao tác (operation / 연산), locking/giao dịch (transaction / 트랜잭션) và secure API.

### Kiểm soát truy cập (access control / 접근 제어) các mô hình (models / 모델들)

DAC — Discretionary kiểm soát truy cập (access control / 접근 제어): đơn vị sở hữu (owner / 오너) có quyền phân phối permission.
MAC — Mandatory kiểm soát truy cập (access control / 접근 제어): chính sách (policy / 정책)/label bắt buộc, người dùng (user / 사용자) không tùy ý cấp lại.
RBAC — Role-Based kiểm soát truy cập (access control / 접근 제어): quyền gắn role.
ABAC — Attribute-Based kiểm soát truy cập (access control / 접근 제어): quyết định (decision / 결정) dựa attribute của subject/tài nguyên (resource / 자원)/hành động (action / 동작)/ngữ cảnh (context / 맥락).

Least privilege và separation of duties là nguyên tắc xuyên suốt.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **5.4 시스템 보안 구축 — hệ thống (system / 시스템) bảo mật (security / 보안) construction** nối từ **5.3 소프트웨어 개발 보안 구축 — Secure software development** sang **7.1 mã (code / 코드) tracing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5.4 시스템 보안 구축 — hệ thống (system / 시스템) bảo mật (security / 보안) construction

### Malware / attack vocabulary

Virus cần host và lan khi host thực thi. Worm tự lan qua mạng (network / 네트워크). Trojan giả dạng hợp pháp để thực hiện hành vi độc hại. Ransomware mã hóa/khóa tài nguyên để đòi tiền. Rootkit che giấu/duy trì quyền kiểm soát. Bot/botnet tập hợp host bị điều khiển.

Phishing lừa người dùng (user / 사용자) qua message/site; spear phishing nhắm mục tiêu cụ thể. Pharming chuyển hướng nạn nhân bằng DNS/host manipulation. Smishing dùng SMS. Vishing dùng voice.

DoS làm cạn tài nguyên (resource / 자원) từ một/few nguồn (source / 소스); DDoS từ nhiều phân tán (distributed / 분산) nguồn (source / 소스). SYN flood lợi dụng TCP handshake bằng nhiều half-open liên kết (connection / 연결). Amplification dùng giao thức (protocol / 프로토콜) phản hồi lớn hơn yêu cầu (request / 요청) và spoof nguồn (source / 소스).

### Mạng (network / 네트워크) attack concepts

Sniffing nghe lén traffic. Spoofing giả định danh (identity / 식별자)/address. MITM đứng giữa hai bên. Session hijacking chiếm session. ARP spoofing đầu độc ánh xạ (mapping / 매핑) IP-MAC trong LAN. DNS poisoning thao túng name resolution/bộ nhớ đệm (cache / 캐시).

### Bảo mật (security / 보안) điều khiển (control / 제어) categories

Preventive ngăn xảy ra. Detective phát hiện. Corrective khắc phục. Deterrent răn đe. khôi phục (recovery / 복구) khôi phục. Một điều khiển (control / 제어) có thể có nhiều vai trò nhưng đề thường mô tả mục tiêu chính.

Vật lý (physical / 물리적), administrative/managerial, technical/logical là cách phân loại theo nature.

### Bảo mật (security / 보안) operations

Logging chỉ có giá trị nếu thời gian (time / 시간) sync, retention, integrity và monitoring phù hợp. SIEM thu thập/correlate sự kiện (event / 이벤트) từ nhiều nguồn. SOC là tổ chức/quy trình vận hành bảo mật (security / 보안) monitoring/phản hồi (response / 응답), không phải một công cụ (tool / 도구) duy nhất.

Vulnerability assessment tìm weakness; penetration testing chủ động khai thác có kiểm soát để đánh giá exploitability/impact. Patch management giảm known vulnerability nhưng cần inventory, prioritization, testing và rollout/quay lui (rollback / 롤백).

Backup chiến lược (strategy / 전략) cần xét full/incremental/differential, retention, offsite/immutable bản sao (copy / 복사) và restore kiểm thử (test / 테스트). Backup chưa từng restore-test không bảo đảm khôi phục (recovery / 복구) thực tế.

---

# 6. Các cặp khái niệm phải phân biệt ngay lập tức

Đây là nhóm dễ mất điểm dù “đã từng học”. Mỗi cặp phải nói được **một câu phân biệt bản chất**, không chỉ đọc định nghĩa riêng rẽ.

| Cặp | Điểm phân biệt cốt lõi |
|---|---|
| xác minh (verification / 확인) / kiểm tra hợp lệ (validation / 검증) | làm sản phẩm đúng đặc tả / làm đúng sản phẩm người dùng cần |
| Functional / Non-functional yêu cầu (requirement / 요구사항) | hệ thống làm gì / hệ thống phải đạt chất lượng hoặc ràng buộc (constraint / 제약조건) nào |
| Cohesion / Coupling | liên kết bên trong mô-đun (module / 모듈) / phụ thuộc giữa mô-đun (module / 모듈) |
| Overloading / Overriding | cùng tên khác parameter / subclass định nghĩa lại hành vi (behavior / 동작) |
| Adapter / Decorator / Proxy | đổi giao diện (interface / 인터페이스) / thêm hành vi (behavior / 동작) / kiểm soát truy cập hoặc đại diện |
| ngăn xếp (stack / 스택) / hàng đợi (queue / 큐) | LIFO / FIFO |
| BFS / DFS | hàng đợi (queue / 큐) / ngăn xếp (stack / 스택) hoặc recursion |
| Stub / Driver | thay mô-đun (module / 모듈) cấp dưới / thay mô-đun (module / 모듈) cấp trên |
| Static / động (dynamic / 동적) testing | không chạy mã (code / 코드) / chạy mã (code / 코드) |
| White-box / Black-box | cấu trúc nội bộ / hành vi (behavior / 동작) theo specification |
| WHERE / HAVING | lọc row trước group / lọc group sau aggregation |
| Candidate / Primary / Foreign key | key tối thiểu khả dĩ / key được chọn / key tham chiếu |
| 2NF / 3NF / BCNF | bỏ partial / bỏ transitive / mọi determinant phải là super key |
| Dirty / Non-repeatable / Phantom | đọc uncommitted / cùng row đổi / tập row đổi |
| Undo / Redo | đảo giao dịch (transaction / 트랜잭션) chưa lần ghi nhận (commit / 커밋) / áp lại giao dịch (transaction / 트랜잭션) đã lần ghi nhận (commit / 커밋) |
| tiến trình (process / 프로세스) / luồng thực thi (thread / 스레드) | thực thi (execution / 실행) ngữ cảnh (context / 맥락) riêng / đơn vị (unit / 단위) thực thi (execution / 실행) chia sẻ tiến trình (process / 프로세스) resources |
| Paging / Segmentation | fixed-size / logical variable-size |
| TCP / UDP | reliable connection-oriented stream / connectionless datagram |
| Authentication / Authorization | bạn là ai / bạn được làm gì |
| Encryption / Hashing | reversible bằng key phù hợp / one-way digest |
| Symmetric / Asymmetric | dùng chung (shared / 공유) secret / public-private key pair |
| IDS / IPS | detect-alert / detect-and-block inline |
| Firewall / WAF | mạng (network / 네트워크)/vận chuyển (transport / 전송) quy tắc (rule / 규칙) rộng / web ứng dụng (application / 애플리케이션) HTTP-focused |
| RAID / Backup | availability khi disk lỗi / khôi phục dữ liệu theo phiên bản (version / 버전)/disaster |
| RTO / RPO | thời gian phục hồi / mức mất dữ liệu theo thời gian |
| VM / bộ chứa (container / 컨테이너) | guest OS isolation / share host kernel theo mô hình phổ biến |
| IaaS / PaaS / SaaS | hạ tầng (infrastructure / 인프라) / nền tảng (platform / 플랫폼) / ứng dụng (application / 애플리케이션) |

---

# 7. Những dạng phải làm được bằng tay

Nếu chỉ đọc lý thuyết mà không làm được các thao tác sau thì coverage chưa đủ.

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **7.1 mã (code / 코드) tracing** nối từ **5.4 시스템 보안 구축 — hệ thống (system / 시스템) bảo mật (security / 보안) construction** sang **7.2 SQL lập luận (reasoning / 추론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.1 mã (code / 코드) tracing

Với C/Java/Python, phải dấu vết (trace / 추적) được:

- vòng lặp lồng nhau;
- recursion;
- array/danh sách (list / 목록)/string indexing;
- pointer cơ bản của C;
- pre/post increment;
- inheritance/overriding Java;
- mutable aliasing Python;
- short-circuit lô-gic (logic / 논리);
- hàm (function / 함수) lời gọi (call / 호출) và phạm vi (scope / 범위) cơ bản.

Cách làm: tạo bảng từng dòng gồm `step | statement | variable state | output`. Không tính nhẩm toàn đoạn mã (code / 코드).

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **7.2 SQL lập luận (reasoning / 추론)** nối từ **7.1 mã (code / 코드) tracing** sang **7.3 Scheduling**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.2 SQL lập luận (reasoning / 추론)

Phải tự viết/đọc được:

- SELECT + WHERE + GROUP BY + HAVING + thứ tự (order / 순서) BY;
- INNER/LEFT phép nối (join / 조인);
- subquery IN/EXISTS;
- aggregate + NULL;
- INSERT/cập nhật (update / 업데이트)/DELETE;
- GRANT/REVOKE;
- giao dịch (transaction / 트랜잭션) lần ghi nhận (commit / 커밋)/quay lui (rollback / 롤백);
- normalization từ functional phụ thuộc (dependency / 의존성) đơn giản.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **7.3 Scheduling** nối từ **7.2 SQL lập luận (reasoning / 추론)** sang **7.4 Page replacement**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.3 Scheduling

Cho arrival/burst/priority/quantum, phải vẽ Gantt chart cho FCFS, SJF/SRTF, Priority, Round Robin rồi tính waiting/turnaround.

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **7.4 Page replacement** nối từ **7.3 Scheduling** sang **7.5 Subnetting**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.4 Page replacement

Cho tham chiếu (reference / 참조) string và số frame, phải mô phỏng FIFO/LRU/Optimal và đếm page fault. Dùng bảng frame theo từng tham chiếu (reference / 참조), không làm bằng trực giác.

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **7.5 Subnetting** nối từ **7.4 Page replacement** sang **7.6 cây (tree / 트리) / đồ thị (graph / 그래프) / độ phức tạp (complexity / 복잡도)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.5 Subnetting

Từ CIDR phải suy được số host, mạng (network / 네트워크) phạm vi (range / 범위)/broadcast trong bài cơ bản. Cần nhớ prefix dài hơn → subnet nhỏ hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **7.6 cây (tree / 트리) / đồ thị (graph / 그래프) / độ phức tạp (complexity / 복잡도)** nối từ **7.5 Subnetting** sang **7.7 giao dịch (transaction / 트랜잭션) / locking**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.6 cây (tree / 트리) / đồ thị (graph / 그래프) / độ phức tạp (complexity / 복잡도)

Phải viết được preorder/inorder/postorder; nhận biết BFS/DFS; so sánh O(1), O(log n), O(n), O(n log n), O(n²), O(2^n), O(n!).

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **7.7 giao dịch (transaction / 트랜잭션) / locking** nối từ **7.6 cây (tree / 트리) / đồ thị (graph / 그래프) / độ phức tạp (complexity / 복잡도)** sang **Môn 1**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.7 giao dịch (transaction / 트랜잭션) / locking

Từ lịch interleaving đơn giản phải nhận diện dirty read, lost cập nhật (update / 업데이트), non-repeatable read, phantom và deadlock.

---

# 8. 과락 방지 — Checklist chống rớt từng môn

Mục tiêu của checklist không phải tự tin mơ hồ. Chỉ đánh dấu khi có thể **giải thích bằng lời của mình và làm một câu biến thể**.

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **Môn 1** nối từ **7.7 giao dịch (transaction / 트랜잭션) / locking** sang **Môn 2**, vì cơ chế trước tạo đầu vào cho bước sau.

## Môn 1

- [ ] phân loại functional / non-functional yêu cầu (requirement / 요구사항);
- [ ] đọc DFD/UML và chọn đúng diagram theo mục đích;
- [ ] phân biệt Scrum / XP / Agile;
- [ ] phân biệt wireframe / mockup / prototype / storyboard;
- [ ] nhớ và hiểu cohesion/coupling theo thứ tự;
- [ ] hiểu OOP, SOLID, GoF mẫu (pattern / 패턴) cốt lõi;
- [ ] hiểu EAI/ESB, JSON/XML/AJAX và giao diện (interface / 인터페이스) bảo mật (security / 보안).

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **Môn 2** nối từ **Môn 1** sang **Môn 3**, vì cơ chế trước tạo đầu vào cho bước sau.

## Môn 2

- [ ] ngăn xếp (stack / 스택)/hàng đợi (queue / 큐)/cây (tree / 트리)/đồ thị (graph / 그래프)/traversal;
- [ ] sorting/tìm kiếm (search / 검색)/băm (hash / 해시) và độ phức tạp (complexity / 복잡도);
- [ ] IPC/mô-đun (module / 모듈) tích hợp (integration / 통합);
- [ ] SCM/Git/SVN/bản phát hành (release / 릴리스)/gói (package / 패키지)/DRM;
- [ ] static/động (dynamic / 동적), white/black box;
- [ ] kiểm thử (test / 테스트) mức (level / 수준), stub/driver, oracle;
- [ ] hiệu năng (performance / 성능) chỉ số (metric / 지표) và cyclomatic độ phức tạp (complexity / 복잡도);
- [ ] giao diện (interface / 인터페이스) hiện thực (implementation / 구현)/xác minh (verification / 확인).

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **Môn 3** nối từ **Môn 2** sang **Môn 4**, vì cơ chế trước tạo đầu vào cho bước sau.

## Môn 3

- [ ] lược đồ (schema / 스키마)/dữ liệu (data / 데이터) independence/ER mô hình (model / 모델);
- [ ] all key types và functional phụ thuộc (dependency / 의존성);
- [ ] 1NF→BCNF, anomaly;
- [ ] relational algebra;
- [ ] chỉ mục (index / 인덱스)/partition/integrity;
- [ ] SQL phép nối (join / 조인)/group/subquery/NULL;
- [ ] procedure/hàm (function / 함수)/trigger;
- [ ] ACID/isolation anomaly;
- [ ] khóa (lock / 잠금)/2PL/deadlock/khôi phục (recovery / 복구);
- [ ] di chuyển (migration / 마이그레이션) kiểm tra hợp lệ (validation / 검증).

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **Môn 4** nối từ **Môn 3** sang **Môn 5**, vì cơ chế trước tạo đầu vào cho bước sau.

## Môn 4

- [ ] C pointer/array/string/operator;
- [ ] Java inheritance/overload/override/static/final/exception;
- [ ] Python danh sách (list / 목록)/tuple/set/dict/slicing/tham chiếu (reference / 참조);
- [ ] recursion và thực thi (execution / 실행) dấu vết (trace / 추적);
- [ ] tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드)/scheduling;
- [ ] paging/segmentation/page replacement;
- [ ] deadlock;
- [ ] OSI/TCP-IP/TCP/UDP/giao thức (protocol / 프로토콜);
- [ ] IPv4/CIDR cơ bản.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng**, **Môn 5** nối từ **Môn 4** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## Môn 5

- [ ] vòng đời (lifecycle / 생명주기)/methodology/estimation/tailoring;
- [ ] mạng (network / 네트워크) thiết bị (device / 장치)/VLAN/NAT/tải (load / 로드) balancing;
- [ ] RAID/lưu trữ (storage / 저장소)/virtualization/cloud;
- [ ] availability/RTO/RPO/backup/DR;
- [ ] CIA/authentication/authorization;
- [ ] symmetric/asymmetric/băm (hash / 해시)/signature;
- [ ] SQLi/XSS/CSRF/command/đường dẫn (path / 경로)/buffer/race;
- [ ] DAC/MAC/RBAC/ABAC;
- [ ] malware/phishing/DoS/spoofing/MITM;
- [ ] firewall/IDS/IPS/WAF/VPN/SIEM;
- [ ] vulnerability/patch/backup/sự cố (incident / 인시던트) fundamentals.

---

# 9. Cách sử dụng bộ lesson hiện có với master guide này

Các folder môn hiện tại chứa nhiều lesson nhỏ được sinh/tổng hợp từ nhiều nguồn và có phần trùng chủ đề. Không cần đọc tuần tự hàng chục tệp (file / 파일) như một cuốn sách từ trang 1 đến cuối.

Quy trình hợp lý hơn là:

**Bước 1 — Coverage pass.** Đọc master guide và đánh dấu phần hoàn toàn chưa biết.
**Bước 2 — Deep pass.** Mở `01-tai-lieu-hoc-day-du.md` của đúng môn và lesson liên quan để đọc giải thích dài, ví dụ và terminology.
**Bước 3 — Retrieval pass.** Đóng tài liệu và tự giải thích lại khái niệm, tự dấu vết (trace / 추적) mã (code / 코드)/SQL/calculation.
**Bước 4 — Mixed practice.** Trộn câu từ nhiều chương để tránh chỉ nhớ ngữ cảnh (context / 맥락) ngay trước đó.
**Bước 5 — lỗi (error / 오류) log.** Mỗi câu sai ghi `khái niệm bị nhầm → tại sao nhầm → quy tắc phân biệt → một ví dụ mới`. Không chỉ ghi đáp án A/B/C/D.

Sau hai lần thi chưa đạt, điều quan trọng nhất không phải đọc lại toàn bộ tài liệu theo cùng một cách, mà là xác định **coverage hole** và **confusion pair**. Một câu sai vì chưa từng thấy thuật ngữ là coverage hole. Một câu sai vì nhầm hai thuật ngữ đã học là discrimination/retrieval bài toán (problem / 문제). Một câu sai vì tính nhầm mã (code / 코드)/SQL là procedural practice bài toán (problem / 문제). Ba loại lỗi cần cách sửa khác nhau.

---

# 10. Nguồn kiểm chứng phạm vi

Phạm vi thi và điều kiện đỗ phải ưu tiên Q-Net (한국산업인력공단) làm nguồn chính thức. Năm 2026 có 출제기준 riêng áp dụng `2026.1.1 ~ 2026.12.31`.

Để kiểm tra cách các mục chính thức được triển khai thành chapter học, đối chiếu nhiều giáo trình 2026 như 시나공, 수제비, 흥달쌤 và curriculum đào tạo nghề; không dùng một giáo trình duy nhất làm “chuẩn đề”.

Tài liệu này cố ý **không sao chép câu hỏi 기출 nguyên văn**. Ví dụ/mã (code / 코드) được viết lại để luyện cơ chế và tránh phụ thuộc vào việc nhớ đáp án của một câu cụ thể.

---

# 11. Definition of Done trước khi thi lại

Không coi “đã đọc hết tệp (file / 파일)” là hoàn thành. Chỉ coi một chương đã sẵn sàng khi đáp ứng cả bốn điều kiện:

1. Có thể giải thích khái niệm chính bằng tiếng Việt nhưng vẫn nhận ra thuật ngữ Korean/English trong đề.
2. Có thể phân biệt nó với ít nhất một khái niệm gần nhất mà không nhìn tài liệu.
3. Với phần procedural, có thể tự làm một ví dụ mới: mã (code / 코드) dấu vết (trace / 추적), SQL, normalization, scheduling, page replacement, subnetting hoặc giao dịch (transaction / 트랜잭션).
4. Làm mixed practice sau vài ngày vẫn suy ra được, không chỉ nhớ vì vừa đọc.

Nếu một môn có bất kỳ vùng lớn nào trong checklist chưa đạt, ưu tiên lấp vùng đó trước khi tối ưu điểm môn mạnh. Đây là cách trực tiếp nhất để giảm rủi ro 과락 và đồng thời nâng điểm trung bình.

> **Bàn giao:** Sau **Môn 5**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
