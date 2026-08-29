# 정보처리기사 - Subject 1 Part 2

## 1. 회복 (Recovery)
- **개념 (Concept)**: 트랜잭션 도중 장애 발생 시 정상 상태로 복구 (Phục hồi về trạng thái bình thường khi có lỗi).
- **장애의 유형 (Types of Failures)**:
  - **트랜잭션 장애 (Transaction Failure)**: Lỗi nội bộ của giao dịch (ví dụ: dữ liệu sai).
  - **시스템 장애 (System Failure)**: Lỗi phần cứng/phần mềm ảnh hưởng đến tất cả giao dịch.
  - **미디어 장애 (Media Failure)**: Lỗi vật lý của thiết bị lưu trữ (ví dụ: hỏng đĩa).
- **회복 기법 (Recovery Techniques)**: 연기 갱신 (Deferred Update), 즉각 갱신 (Immediate Update), 그림자 페이지 (Shadow Paging), 검사점 (Check Point).
- **Ví dụ**: Hệ thống ngân hàng bị sập khi đang chuyển tiền (hệ thống lỗi), cần hoàn tác (Undo) hoặc chạy lại để khôi phục.
- 💡 **Mẹo ghi nhớ**: 장애 유형: T/S/M (Transaction, System, Media) -> **Tưởng Sợ Ma**

## 2. Commit & Rollback 연산
- **Commit**: Giao dịch thành 정공적으로 종료 (thành công), lưu thay đổi vào CSDL.
- **Rollback**: Giao dịch 비정상적으로 종료 (thất bại), hoàn tác các thay đổi (Undo) để bảo vệ tính nhất quán (Consistency).

## 3. 트랜잭션의 상태 (Transaction States)
- **Active (활동)**: Đang thực thi.
- **Failed (장애)**: Gặp lỗi.
- **Aborted (철회)**: Hủy bỏ và Rollback.
- **Partially Committed (부분 완료)**: Xong lệnh cuối nhưng chưa Commit.
- **Committed (완료)**: Commit thành công.
- 💡 **Mẹo ghi nhớ**: A-PC-C (Thành công) / A-F-Ab (Thất bại)

## 4. 병행 제어 (Concurrency Control)
- **개념 (Concept)**: Điều khiển sự tương tác giữa các giao dịch chạy đồng thời để bảo vệ tính 일관성 (nhất quán).
- **문제점 (Problems)**:
  - **갱신 분실 (Lost Update)**: Mất bản cập nhật.
  - **비완료 의존성 (Uncommitted Dependency)**: Phụ thuộc vào giao dịch chưa commit (Dirty Read).
  - **모순성 (Inconsistency)**: Mâu thuẫn dữ liệu.
  - **연쇄 복귀 (Cascading Rollback)**: Phải rollback dây chuyền.
- **로킹 (Locking)**: Khóa dữ liệu để sử dụng 상호 배타적 (độc quyền - Mutual Exclusion).
  - **로킹 단위 (Locking Granularity)**: Đơn vị khóa. 
    - Đơn vị 크면 (lớn) -> ít khóa, dễ quản lý, nhưng mức đồng thời thấp (낮은 병행성). 
    - Đơn vị 작으면 (nhỏ) -> ngược lại.
- **Ví dụ**: Hai người cùng rút tiền từ một tài khoản, Locking giúp chỉ 1 người được rút tại 1 thời điểm.
- 💡 **Mẹo ghi nhớ**: Vấn đề đồng thời: L/U/I/C (Lost, Uncommitted, Inconsistency, Cascading) -> **Làm Út In Cười**

## 5. 보안 및 암호화 (Security & Encryption)
- **개인키 암호 방식 (Private Key / Secret Key)**: Mã hóa đối xứng (대칭). Dùng cùng 1 khóa (DES). Nhanh, nhưng khó quản lý nhiều khóa.
- **공개키 암호 방식 (Public Key)**: Mã hóa bất đối xứng (비대칭). Khóa 공개키 (công khai) để mã hóa, khóa 비밀키 (bí mật) để giải mã (RSA). Quản lý khóa dễ, nhưng chậm.
- 💡 **Mẹo ghi nhớ**: 개인키 = 빠름, 키많음 (Private = Fast, Many keys). 공개키 = 느림, 키적음 (Public = Slow, Few keys).

## 6. 분산 데이터베이스 (Distributed Database)
- **4대 목표 (4 Transparencies)**:
  - **위치 투명성 (Location)**: Không cần biết vị trí thật.
  - **중복(복제) 투명성 (Replication)**: Dữ liệu nhân bản nhưng người dùng thấy như một.
  - **병행 투명성 (Concurrency)**: Chạy đồng thời không ảnh hưởng nhau.
  - **장애 투명성 (Failure)**: Lỗi ở 1 nơi vẫn hoạt động đúng.
- 💡 **Mẹo ghi nhớ**: V/T/B/L (Vị trí, Nhân bản, Đồng thời, Lỗi) -> **Vào Trọng Bệnh Lo**

## 7. 자료 구조 (Data Structures)
- **선형 구조 (Linear)**: 배열 (Array), 연결 리스트 (Linked List), 스택 (Stack), 큐 (Queue), 데크 (Deque).
- **비선형 구조 (Non-Linear)**: 트리 (Tree), 그래프 (Graph).
- 💡 **Mẹo ghi nhớ**: 비선형 (Non-linear) là Tree & Graph, còn lại là 선형.

## 8. 연결 리스트, 스택, 큐, 데크 (Data Structure Types)
- **연결 리스트 (Linked List)**: Lưu bằng con trỏ (Pointer). Chèn/xóa dễ, nhưng truy cập chậm.
- **스택 (Stack)**: LIFO (Last-In, First-Out). Dùng cho: Gọi hàm (Function call), Đệ quy (Recursion), Tính biểu thức hậu tố (Postfix). (PUSH/POP)
- **큐 (Queue)**: FIFO (First-In, First-Out). Dùng cho: Lập lịch (Scheduling), Hàng chờ (Waiting list). Có Front/Rear.
- **데크 (Deque)**: Hàng đợi hai đầu. (Scroll: giới hạn đầu vào, Shelf: giới hạn đầu ra)

## 9. 트리 (Tree) 용어
- Node, Root, Degree (차수), Terminal Node (Leaf), Parent, Child, Sibling, Depth/Height.

## 10. 이진 트리의 운행법 (Binary Tree Traversal)
- **Preorder (전위)**: Root -> Left -> Right
- **Inorder (중위)**: Left -> Root -> Right
- **Postorder (후위)**: Left -> Right -> Root

## 11. 수식의 표기법 (Expression Notation)
- Prefix, Infix, Postfix.
- Chuyển đổi qua lại (Infix -> Postfix/Prefix) bằng cách đóng ngoặc và di chuyển toán tử.



## 12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)
- **외부 정렬 (External Sort)**: Dùng bộ nhớ phụ (보조기억장치) để sắp xếp dữ liệu lớn. Chủ yếu dùng Merge Sort (병합 정렬).
  - Phân loại: Balance Merge, Cascade Merge, Polyphase Merge, Oscillating Merge.
- **주요 정렬 알고리즘 (Main Sorting Algorithms)**:
  - **삽입 정렬 (Insertion Sort)**: Chèn phần tử vào đúng vị trí của mảng đã sắp xếp.
  - **버블 정렬 (Bubble Sort)**: Đổi chỗ 2 phần tử kề nhau nếu sai thứ tự (nổi bọt).
  - **선택 정렬 (Selection Sort)**: Tìm phần tử nhỏ nhất và đưa lên đầu.
  - **2-Way 합병 정렬 (2-Way Merge Sort)**: Chia đôi liên tục rồi gộp lại (Merge) theo thứ tự.
- **Ví dụ**: Sắp xếp 8, 5, 6, 2, 4 bằng Bubble Sort: (8,5) đổi -> 5,8,6,2,4 -> ...

## 13. 검색 및 해싱 (Search & Hashing)
- **이분 검색 / 이진 검색 (Binary Search)**:
  - Dữ liệu phải được sắp xếp (순서화).
  - Tìm kiếm bằng cách chia đôi: `M = (F + L) / 2` (F: Đầu, L: Cuối).
  - Cực kỳ nhanh do mỗi lần giảm một nửa phạm vi tìm kiếm.
- **해싱 (Hashing)**: 
  - Tính toán địa chỉ (Home Address) qua hàm băm (Hash Function).
  - Cực nhanh, tốt cho thêm/xóa thường xuyên, nhưng tốn không gian.
  - **Thuật ngữ**:
    - **버킷 (Bucket)**: Khu vực lưu trữ, gồm nhiều Slot.
    - **슬롯 (Slot)**: Chỗ lưu 1 bản ghi (Record).
    - **Collision (충돌)**: 2 khóa ra cùng địa chỉ.
    - **Synonym**: Các khóa cùng địa chỉ.
    - **Overflow (오버플로)**: Hết chỗ lưu khi xảy ra Collision.
- 💡 **Mẹo ghi nhớ**: 해싱 용어: B/S/C/S/O (Bucket, Slot, Collision, Synonym, Overflow) -> **Bỏ Sót Con Sẽ Ôm**

## 14. 파일 편성 방식 (File Organization)
- **순차 파일 (Sequential File)**: Lưu nối tiếp. Phù hợp băng từ (Magnetic Tape). Nhanh khi xử lý tuần tự, chậm khi thêm/xóa/tìm kiếm.
- **색인 순차 파일 (Indexed Sequential File / ISAM)**:
  - Vừa tuần tự vừa ngẫu nhiên (Sequential + Random).
  - Gồm 3 vùng: **기본 구역 (Prime Area)**, **색인 구역 (Index Area)**, **오버플로 구역 (Overflow Area)**.
  - Dễ dàng chèn/xóa, nhưng tốn dung lượng cho Index/Overflow và chậm hơn File ngẫu nhiên thuần.
- 💡 **Mẹo ghi nhớ**: ISAM 3 구역 (P/I/O - Prime, Index, Overflow) -> **Phải In Ô**

---
# 1과목 Chapter 1. 요구사항 확인 (Requirements)

## 1. 현행 시스템 분석 (Current System Analysis)
- **플랫폼 성능 (Platform Performance)**: 
  - 가용성 (Availability), 경과 시간 (Turnaround Time), 응답 시간 (Response Time), 사용률 (Utilization).
- **운영체제 및 DBMS 고려사항 (OS & DBMS Considerations)**: 
  - 신뢰도 (Reliability), 성능 (Performance), 기술 지원 (Tech Support), 주변 기기 (Peripherals), 구축 비용 (Cost), 상호 호환성 (Compatibility).

## 2. 요구사항 정의 (Requirements Definition)
- **기능 요구사항 (Functional)**: Chức năng hệ thống phải có (Ví dụ: Đăng nhập).
- **비기능 요구사항 (Non-Functional)**: Hiệu năng, bảo mật, chất lượng, ràng buộc (Ví dụ: Phản hồi dưới 1s).
- **개발 프로세스 (Development Process)**: 
  1. 도출 (Elicitation) -> 2. 분석 (Analysis) -> 3. 명세 (Specification) -> 4. 확인/검증 (Validation).
- 💡 **Mẹo ghi nhớ**: Đ/P/M/X (Elicitation, Analysis, Spec, Validation) -> **Đi Phượt Một Xe**
- **명세 기법 (Specification Techniques)**:
  - 정형 (Formal): Ký hiệu toán học (Toán học, VDM, Z-schema). Rõ ràng nhưng khó hiểu với user.
  - 비정형 (Informal): Ngôn ngữ tự nhiên (Natural language, FSM, ERD). Dễ hiểu nhưng có thể mơ hồ.

## 3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)
- **자료 흐름도 (DFD - Data Flow Diagram)**:
  - 프로세스 (Process - Tròn), 자료 흐름 (Data Flow - Mũi tên), 자료 저장소 (Data Store - Đường thẳng), 단말 (Terminator - Vuông).
- **자료 사전 (DD - Data Dictionary)**: 
  - `=`: Định nghĩa (is composed of)
  - `+`: Kết nối (and)
  - `( )`: Tùy chọn (Optional)
  - `[ | ]`: Lựa chọn (or)
  - `{ }`: Lặp lại (Iteration)
  - `**`: Ghi chú (Comment)
- **CASE 도구 (CASE Tools)**: SADT, SREM, PSL/PSA.
- **HIPO (Hierarchical Input Process Output)**: Phân tích Top-down (가시적 도표, 총체적 도표, 세부적 도표).

## 4. UML (Unified Modeling Language)
- **개념**: Ngôn ngữ mô hình hóa hướng đối tượng chuẩn.
- **구성요소**: 사물 (Things), 관계 (Relationships), 다이어그램 (Diagrams).
- **관계 (Relationships)**: 
  - 연관 (Association), 의존 (Dependency), 집합 (Aggregation), 포함 (Composition), 일반화 (Generalization - Kế thừa), 실체화 (Realization - Interface).
- **다이어그램 (Diagrams)**:
  - **구조적/정적 (Structural/Static)**: Class, Object, Component, Deployment, Composite Structure, Package.
  - **행위적/동적 (Behavioral/Dynamic)**: Use Case, Sequence, Communication, State, Activity, Timing.
- 💡 **Mẹo ghi nhớ**: 
  - 정적 다이어그램: 클/객/컴/배/복/패 (Class, Object, Component, Deployment, Composite, Package)
  - 동적 다이어그램: 유/순/커/상/활/타 (Use case, Sequence, Comm, State, Activity, Timing)

## 5. UML 구성요소 상세 (UML Components Detail)
- **클래스 다이어그램 (Class Diagram)**: Class Name, Attribute, Operation.
  - 접근 제어자 (Access Modifier): `+` (Public), `-` (Private), `#` (Protected), `~` (Package).
- **유스케이스 다이어그램 (Use Case Diagram)**: System, Use Case, Actor.
  - Quan hệ: `<<include>>` (Bắt buộc), `<<extend>>` (Tùy chọn), Generalization (Kế thừa).
- **순차 다이어그램 (Sequence Diagram)**: Object, Lifeline, Activation, Message, Self-Message.
  - Thể hiện sự tương tác theo thời gian.

## 6. 애자일 방법론 (Agile Methodology)
- **개념**: Linh hoạt, phản hồi liên tục.
- **4대 핵심 가치 (4 Core Values)**:
  1. Cá nhân và tương tác (개인과의 상호작용) > Quy trình và công cụ.
  2. Phần mềm chạy được (실행되는 소프트웨어) > Tài liệu.
  3. Hợp tác với khách hàng (고객과의 협력) > Đàm phán hợp đồng.
  4. Phản hồi với sự thay đổi (변화에 유연하게 대응) > Tuân thủ kế hoạch.


## 7. 스크럼(Scrum) 및 XP(eXtreme Programming)
- **스크럼 (Scrum)**: Quản lý dự án Agile theo nhóm.
  - **용어**: 제품 백로그 (Product Backlog - Yêu cầu tổng), 스프린트 (Sprint - Chu kỳ 2-4 tuần), 속도 (Velocity), 번 다운 차트 (Burn Down Chart - Biểu đồ tiến độ), PO (Product Owner), SM (Scrum Master).
  - **프로세스**: Backlog -> Sprint Planning -> Sprint Execution (Daily Scrum) -> Sprint Review (Đánh giá) -> Sprint Retrospective (Hồi tưởng/Cải tiến).
- **XP (eXtreme Programming)**: Tối ưu hóa phát triển phần mềm cùng khách hàng.
  - **핵심 가치 (5 Core Values)**: 의사소통 (Communication), 단순성 (Simplicity), 용기 (Courage), 존중 (Respect), 피드백 (Feedback). 
  - 💡 **Mẹo ghi nhớ**: Y/Đ/D/T/P -> **Ý Định Dũng Tướng Phàm**
  - **기본 원리 (Principles)**: Pair Programming, CI (Tích hợp liên tục), TDD (Test-Driven Development), Refactoring (Tái cấu trúc mã), 40-Hour Work.

---
# Chapter 2. 화면 설계 (Screen Design)

## 1. 사용자 인터페이스 (User Interface - UI)
- **UI 유형 (UI Types)**: 
  - CLI (Dòng lệnh), GUI (Đồ họa), NUI (Cử chỉ tự nhiên như chạm, vuốt), OUI (Hữu cơ).
  - **모바일 제스처 (Mobile Gestures)**: Tap (Chạm), Double Tap, Drag (Kéo), Pan (Di chuyển liên tục), Press (Nhấn giữ), Flick (Vuốt nhanh), Pinch (Phóng to/thu nhỏ bằng 2 ngón).
- **UI 기본 원칙 (4 Principles)**:
  - **직관성 (Intuitiveness)**: Dễ hiểu, trực quan.
  - **유효성 (Efficiency)**: Đạt được mục tiêu chính xác.
  - **학습성 (Learnability)**: Dễ học.
  - **유연성 (Flexibility)**: Linh hoạt, giảm thiểu lỗi.
  - 💡 **Mẹo ghi nhớ**: T/H/H/N -> **Trực Học Hằng Ngày**
- **UI 설계 도구 (UI Design Tools)**:
  - **와이어프레임 (Wireframe)**: Khung xương (Tĩnh).
  - **목업 (Mockup)**: Thiết kế tĩnh, giống thật nhất.
  - **스토리보드 (Storyboard)**: Bản hướng dẫn chi tiết, có luồng di chuyển.
  - **프로토타입 (Prototype)**: Mô hình động, có thể tương tác.

---
# Chapter 3. 애플리케이션 설계 (Application Design)

## 1. 소프트웨어 아키텍처 (Software Architecture)
- **상위 설계 (High-level)**: 아키텍처 (Architecture), 자료구조 (Data Structure), 인터페이스 (Interface).
- **하위 설계 (Low-level)**: 모듈 (Module), 프로시저 (Procedure).
- **아키텍처 패턴 (Architecture Patterns)**:
  - **레이어 패턴 (Layers)**: Chia thành các tầng (OSI 7 layer).
  - **클라이언트-서버 패턴 (Client-Server)**: Máy khách - Máy chủ.
  - **파이프-필터 패턴 (Pipe-Filter)**: Dữ liệu qua các bộ lọc liên tiếp (Ví dụ: Unix shell).
  - **MVC 패턴**: Model (Dữ liệu), View (Giao diện), Controller (Điều khiển).
  - **브로커 패턴 (Broker)**: Có môi giới ở giữa.
  - **마스터-슬레이브 (Master-Slave)**: Một chủ, nhiều tớ (Hệ thống thời gian thực).

## 2. 객체지향 (OOP - Object Oriented Programming)
- **구성요소**: 클래스 (Class), 객체 (Object), 메서드 (Method), 메시지 (Message), 인스턴스 (Instance), 속성 (Property).
- **객체지향 기법 (OOP Techniques)**:
  - **캡슐화 (Encapsulation)**: Đóng gói dữ liệu và phương thức, giảm kết dính (Coupling).
  - **정보 은닉 (Information Hiding)**: Giấu thông tin chi tiết.
  - **다형성 (Polymorphism)**: Đa hình (Overloading - Cùng tên khác tham số, Overriding - Ghi đè phương thức cha).
- **객체지향 설계 원칙 (SOLID)**:
  - **S (SRP)**: Đơn trách nhiệm (Một lớp một việc).
  - **O (OCP)**: Đóng-Mở (Mở rộng thì dễ, sửa đổi thì cấm).
  - **L (LSP)**: Thay thế Liskov (Lớp con thay thế được lớp cha).
  - **I (ISP)**: Phân tách Interface (Interface nhỏ gọn).
  - **D (DIP)**: Đảo ngược phụ thuộc (Phụ thuộc vào Interface, không phụ thuộc vào triển khai chi tiết).
- **분석 방법론 (OOA Methods)**:
  - **람바우 (Rumbaugh - OMT)**: 객체 모형 (Object) -> 동적 모형 (Dynamic) -> 기능 모형 (Functional - DFD). 
  - 💡 **Mẹo ghi nhớ**: K/Đ/C -> **Không Đợi Chờ**

## 3. 모듈 (Module)
- **결합도 (Coupling - Độ kết dính giữa các module)**: Càng thấp càng tốt.
  - 자료 (Data - Tốt nhất) < 스탬프 (Stamp) < 제어 (Control) < 외부 (External) < 공통 (Common) < 내용 (Content - Tệ nhất).
  - 💡 **Mẹo ghi nhớ**: T/S/C/N/C/N (Tốt -> Tệ) -> **Tính Sao Cho Nhẹ Cả Người**
- **응집도 (Cohesion - Độ gắn kết trong 1 module)**: Càng cao càng tốt.
  - 기능적 (Functional - Tốt nhất) > 순차적 (Sequential) > 통신적 (Communication) > 절차적 (Procedural) > 시간적 (Temporal) > 논리적 (Logical) > 우연적 (Coincidental - Tệ nhất).
  - 💡 **Mẹo ghi nhớ**: K/T/T/T/T/L/N (Tốt -> Tệ) -> **Không Thể Tin Thằng Trẻ Làm Ngốc**
- **팬인 (Fan-In) / 팬아웃 (Fan-Out)**:
  - Fan-in (Số module gọi nó): Cao thì tốt (tái sử dụng nhiều).
  - Fan-out (Số module nó gọi): Càng thấp càng tốt.

## 4. 디자인 패턴 (Design Patterns - GoF)
- **생성 패턴 (Creational - 5)**: Abstract Factory, Builder, Factory Method, Prototype, Singleton. (Tạo đối tượng)
- **구조 패턴 (Structural - 7)**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy. (Cấu trúc, ghép nối)
- **행위 패턴 (Behavioral - 11)**: Strategy, Mediator, Command, Observer, State, Iterator, Visitor, Chain of Responsibility, Interpreter, Memento, Template Method. (Hành vi, tương tác)

---
# Chapter 4. 인터페이스 설계 (Interface Design)

## 1. 요구사항 개발 기법 (Requirements Elicitation Techniques)
- **도출 (Elicitation) 기법**:
  - **인터뷰 (Interview)**: Phỏng vấn.
  - **브레인스토밍 (Brainstorming)**: Công não ý tưởng (Không chỉ trích).
  - **델파이 기법 (Delphi)**: Hỏi ý kiến chuyên gia ẩn danh.
  - **프로토타이핑 (Prototyping)**: Làm mẫu thử.


## 2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)
- **정형 기술 검토 (FTR - Formal Technical Review)**:
  - **동료검토 (Peer Review)**: Tác giả tự giải thích tài liệu, đồng nghiệp tìm lỗi.
  - **워크 스루 (Walk Through)**: Gửi tài liệu trước, họp review ngắn để tìm lỗi nhanh.
  - **인스펙션 (Inspection)**: Chuyên gia khác (không phải tác giả) kiểm tra chặt chẽ để tìm lỗi.
  - 💡 **Mẹo ghi nhớ**: 동료(Tự thuyết trình) / 워크스루(Họp ngắn) / 인스펙션(Chuyên gia chém).
- **연계 기술 (Connection Tech)**: 
  - DB Link, API, Socket (Cấp phát cổng), JDBC.
- **미들웨어 (Middleware)**: Phần mềm trung gian kết nối các hệ thống khác biệt.
  - **TP Monitor**: Giám sát Transaction (Giao dịch).
  - **MOM (Message-Oriented)**: Bất đồng bộ (비동기), dùng hàng đợi tin nhắn (메시지 큐).
  - **ORB (Object Request Broker)**: Hướng đối tượng, chuẩn CORBA.
  - **WAS (Web Application Server)**: Xử lý nội dung web động (동적인 콘텐츠).

---
# 소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)

## 1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)
- **개념**: Toàn bộ quá trình phát triển (Yêu cầu -> Thiết kế -> Code -> Test -> Bảo trì). Là tiêu chuẩn để quản lý dự án, chi phí, nhân lực.
- **폭포수 모형 (Waterfall Model)**: 
  - Tuần tự (선형 순차적). Xong bước này mới qua bước khác. Không quay lại được.
  - Phù hợp dự án có yêu cầu rõ ràng, hệ thống nhà nước/ngân hàng. Tài liệu là trọng tâm.
- **나선형 모형 (Spiral Model)**:
  - Do Boehm đề xuất. Trọng tâm: Phân tích rủi ro (위험 분석).
  - Chu trình: Kế hoạch (계획) -> Phân tích rủi ro (위험) -> Phát triển (개발) -> Đánh giá (평가). 
  - Phù hợp dự án lớn, rủi ro cao.
- **프로토타입 모형 (Prototype Model)**:
  - Làm bản nháp (시제품) trước khi phát triển thật. Phù hợp khi yêu cầu chưa rõ ràng.
- **V-모형 (V-Model)**:
  - Mỗi bước phát triển tương ứng với một bước Test (Ánh xạ Dev-Test). Yêu cầu chất lượng cực cao (Y tế, Hàng không).

## 2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)
- **스크럼 프로세스 (Scrum Process)**:
  - **일일 스크럼 (Daily Scrum)**: Họp đứng 15 phút. Cập nhật tiến độ lên Burn-down Chart (Biểu đồ tiêu hao).
  - **스프린트 검토 (Sprint Review)**: Demo sản phẩm cho khách hàng xem có đúng ý không.
  - **스프린트 회고 (Sprint Retrospective)**: Nội bộ team họp để rút kinh nghiệm, cải tiến quy trình.
- **XP 기법 상세 (XP Details)**:
  - **사용자 스토리 (User Story)**: Kịch bản do khách hàng viết (đơn vị chức năng), có thể chứa Test Case.
  - **릴리즈 계획 (Release Planning)**: Kế hoạch phát hành từng phần sản phẩm (v1.0, v1.1).
  - **스파이크 (Spike)**: Chương trình nhỏ, code thử nghiệm nhanh để kiểm tra tính khả thi của công nghệ nhằm giảm rủi ro (기술적 위험 감소). Code này có thể bị vứt đi sau khi test.


## 3. 현행 시스템 파악 (Understanding Current System)
- **1단계**: 시스템 구성 (기간 업무/지원 업무), 기능 (계층형), 인터페이스 (Giao thức, loại liên kết).
- **2단계**: 아키텍처 구성 (Kiến trúc), 소프트웨어 구성 (Bản quyền - 라이선스).
- **3단계**: 하드웨어 구성 (Dự phòng - 이중화/Redundancy), 네트워크 구성 (Vị trí vật lý, mạng).

## 4. 운영 환경 구축 고려사항 (Operation Environment Considerations)
- **운영체제 (OS)** & **DBMS**: 가용성 (Availability), 성능 (Performance), 기술 지원 (Tech Support), 구축 비용 (Cost). 
  - OS có thêm: 주변 기기 (Thiết bị ngoại vi).
  - DBMS có thêm: 상호 호환성 (Khả năng tương thích - JDBC/ODBC).
- **WAS (Web Application Server)**: Xử lý nội dung động. Có thêm **가비지 컬렉션 (GC - Dọn rác)**.
- **오픈 소스 (Open Source)**: Cần chú ý 라이선스 (Bản quyền), 사용자 수 (Số lượng người dùng), 기술의 지속 가능성 (Khả năng duy trì công nghệ).

## 5. 요구공학 (Requirements Engineering)
- **도출 (Elicitation)**: Lặp đi lặp lại trong suốt vòng đời (SDLC).
- **분석 (Analysis)**: Giải quyết xung đột (중재), dùng DFD, DD.
- **명세 (Specification)**: Viết tài liệu (Mini-Spec), đảm bảo tính truy xuất (추적성).
  - 정형 (Toán học, VDM) vs 비정형 (Ngôn ngữ tự nhiên, ERD).
- **확인 (Validation)**: 
  - 확인 (Validation): Có đúng sản phẩm khách cần không? (Right product).
  - 검증 (Verification): Có làm đúng quy trình không? (Product right).
  - Cần quản lý cấu hình (형상 관리).

## 6. 구조적 분석 도구 (Structured Analysis Tools)
- Phân tích Top-down (하향식), dùng biểu đồ (도형).
- **DFD (Biểu đồ luồng dữ liệu)**: Process (Tròn), Flow (Mũi tên), Data Store (Vạch ngang), Terminator (Vuông).
- **DD (Từ điển dữ liệu)**: 
  - `=`: Định nghĩa
  - `+`: Nối
  - `( )`: Tùy chọn (Optional)
  - `[ | ]`: Chọn 1 trong các (Or)
  - `{ }`: Lặp (Iteration)
  - `* *`: Chú thích
- **HIPO**: Biểu đồ phân cấp (가시적, 총체적, 세부적).

## 7. UML 심화 (Advanced UML)
- Do OMG chuẩn hóa từ phương pháp của Rumbaugh, Booch, Jacobson.
- **다이어그램 (Diagrams)**:
  - 구조적 (Structural / Tĩnh): Class, Object, Component, Deployment, Composite, Package.
  - 행위적 (Behavioral / Động): Use Case, Sequence, Communication, State, Activity, Timing.
- **스테레오 타입 (Stereotype)**: Mở rộng UML bằng dấu `<< >>` (Guillemet). Ví dụ: `<<include>>`, `<<extend>>`.


## 8. UI 및 UX, HCI (UI, UX, HCI)
- **UI 유형**: CLI (Văn bản), GUI (Đồ họa), NUI (Tự nhiên - Giọng nói/Hành động), OUI (Hữu cơ - Gắn với đồ vật vật lý).
- **UI 설계 도구**: Wireframe (Khung xương), Mockup (Mô hình tĩnh giống thật), Storyboard (Kịch bản chi tiết), Prototype (Mô hình động tương tác).
- **HCI (Human Computer Interaction)**: Nghiên cứu tương tác người-máy tính để mang lại trải nghiệm tốt nhất (UX).
- **UX (User Experience - Trải nghiệm người dùng)**:
  - **주관성 (Subjectivity)**: Tính chủ quan.
  - **정황성 (Contextuality)**: Phụ thuộc vào hoàn cảnh (thời gian, địa điểm).
  - **총체성 (Holistic)**: Trải nghiệm tổng thể.
- **감성공학 (Affective Engineering)**: Khoa học kết hợp cảm xúc con người vào thiết kế (Dựa trên -> Thực hiện -> Ứng dụng).

## 9. 소프트웨어 품질 특성 (ISO/IEC 9126)
- 6 tiêu chuẩn chất lượng:
  1. **기능성 (Functionality - Chức năng)**: Bảo mật, Tương tác, Chính xác.
  2. **신뢰성 (Reliability - Độ tin cậy)**: Không lỗi, Phục hồi (회복성), Chịu lỗi (고장 허용성).
  3. **사용성 (Usability - Khả năng sử dụng)**: Dễ học, Dễ hiểu, Hấp dẫn.
  4. **효율성 (Efficiency - Hiệu quả)**: Thời gian phản hồi, Tiết kiệm tài nguyên.
  5. **유지 보수성 (Maintainability - Khả năng bảo trì)**: Dễ phân tích, Dễ thay đổi, Ổn định.
  6. **이식성 (Portability - Khả năng thay thế/di chuyển)**: Cài đặt dễ, Tương thích, Thay thế.

## 10. 소프트웨어 설계 원리 (Software Design Principles)
- **모듈화 (Modularity)**: 
  - Module quá nhỏ -> Chi phí tích hợp (Integration Cost) tăng.
  - Module quá lớn -> Chi phí phát triển từng module (Development Cost) tăng.
- **추상화 (Abstraction)**: 3 loại (과정 - Quá trình, 데이터 - Dữ liệu, 제어 - Điều khiển).
- **단계적 분해 (Stepwise Refinement)**: Đi từ trên xuống (Top-down).
- **정보 은닉 (Information Hiding)**: Giấu thông tin để giảm phụ thuộc.
- **시스템 타입 (System Types)**:
  - **대화형 (Interactive)**: Tương tác (VD: Web bán hàng).
  - **이벤트 중심 (Event-driven)**: Dựa trên sự kiện (VD: Chuông báo cháy).
  - **변환형 (Transformational)**: Biến đổi dữ liệu (VD: Trình biên dịch - Compiler).
  - **객체 영속형 (Object Persistence)**: Lưu trữ lâu dài (VD: Database Server).


