# 정보처리기사 필기 2026 — Korean Term Bridge

> Mục tiêu: khi gặp thuật ngữ tiếng Hàn trong đề, phải map ngay được sang **English concept → nghĩa Việt → mechanism**, không dừng ở dịch từ. File này chỉ giữ các thuật ngữ có giá trị phân biệt cao hoặc dễ gây nhầm.

---

# 1. 소프트웨어 설계 — Software Design

## 요구사항 — Requirement

**요구사항** → Requirement → yêu cầu hệ thống.

- **기능 요구사항** → Functional Requirement → hệ thống phải làm gì.
- **비기능 요구사항** → Non-functional Requirement → chất lượng/ràng buộc phải đạt.
- **요구사항 도출** → Requirement Elicitation → khai thác yêu cầu từ stakeholder/source.
- **요구사항 분석** → Requirement Analysis → xử lý conflict, dependency, feasibility, priority.
- **요구사항 명세** → Requirement Specification → đặc tả yêu cầu rõ, testable.
- **요구사항 확인/검증** → Requirement Validation/Verification tùy ngữ cảnh giáo trình → kiểm tính đúng/đủ/phù hợp.
- **추적성** → Traceability → liên kết requirement với source/design/code/test.

### Dấu hiệu

`추적`, `영향 분석`, `요구사항 변경` thường kéo về traceability/change impact.

---

## 구조적 분석 — Structured Analysis

- **자료 흐름도** → Data Flow Diagram, DFD → sơ đồ luồng dữ liệu.
- **자료 사전** → Data Dictionary → từ điển dữ liệu.
- **소단위 명세서** → Mini-specification → đặc tả logic process chi tiết.
- **프로세스** → Process → biến đổi input data thành output data trong DFD.
- **자료 저장소** → Data Store → nơi lưu dữ liệu.
- **단말/외부 개체** → External Entity → nguồn/đích ngoài system boundary.

---

## UML

- **유스케이스 다이어그램** → Use Case Diagram.
- **클래스 다이어그램** → Class Diagram.
- **객체 다이어그램** → Object Diagram.
- **순차 다이어그램** → Sequence Diagram.
- **활동 다이어그램** → Activity Diagram.
- **상태 다이어그램** → State Diagram.
- **컴포넌트 다이어그램** → Component Diagram.
- **배치 다이어그램** → Deployment Diagram.
- **일반화** → Generalization.
- **연관** → Association.
- **집합** → Aggregation.
- **합성** → Composition.
- **의존** → Dependency.
- **실체화** → Realization.

### Dấu hiệu

`시간 순서`, `메시지` → Sequence.

`상태 변화`, `이벤트` → State.

`노드`, `배치` → Deployment.

---

## Module Design

- **응집도** → Cohesion → mức gắn kết bên trong module.
- **결합도** → Coupling → mức phụ thuộc giữa modules.
- **기능적 응집도** → Functional Cohesion.
- **순차적 응집도** → Sequential Cohesion.
- **통신적 응집도** → Communicational Cohesion.
- **절차적 응집도** → Procedural Cohesion.
- **시간적 응집도** → Temporal Cohesion.
- **논리적 응집도** → Logical Cohesion.
- **우연적 응집도** → Coincidental Cohesion.

Coupling:

- **내용 결합도** → Content Coupling.
- **공통 결합도** → Common Coupling.
- **외부 결합도** → External Coupling.
- **제어 결합도** → Control Coupling.
- **스탬프 결합도** → Stamp Coupling.
- **자료 결합도** → Data Coupling.

### Trật tự thi hay hỏi

Cohesion: càng functional càng mạnh/tốt.

Coupling: càng data càng yếu/tốt trong bộ classic.

---

## OOP / Design Pattern

- **캡슐화** → Encapsulation → đóng gói/kiểm soát state.
- **상속** → Inheritance → kế thừa.
- **다형성** → Polymorphism → đa hình.
- **추상화** → Abstraction → trừu tượng hóa.
- **오버로딩** → Overloading.
- **오버라이딩** → Overriding.

Pattern terms:

- **전략 패턴** → Strategy Pattern.
- **상태 패턴** → State Pattern.
- **옵저버 패턴** → Observer Pattern.
- **어댑터 패턴** → Adapter Pattern.
- **퍼사드 패턴** → Facade Pattern.
- **데코레이터 패턴** → Decorator Pattern.
- **프록시 패턴** → Proxy Pattern.
- **팩토리 메서드** → Factory Method.
- **추상 팩토리** → Abstract Factory.
- **빌더** → Builder.
- **프로토타입** → Prototype.
- **싱글턴** → Singleton.
- **커맨드** → Command.
- **템플릿 메서드** → Template Method.
- **이터레이터** → Iterator.

---

# 2. 소프트웨어 개발 — Software Development

## Data Structure / Algorithm

- **자료구조** → Data Structure.
- **스택** → Stack → LIFO.
- **큐** → Queue → FIFO.
- **트리** → Tree.
- **그래프** → Graph.
- **이진 탐색 트리** → Binary Search Tree.
- **힙** → Heap.
- **해시** → Hash.
- **충돌** → Collision.
- **선형 조사법** → Linear Probing.
- **너비 우선 탐색** → Breadth-First Search, BFS.
- **깊이 우선 탐색** → Depth-First Search, DFS.
- **이진 탐색** → Binary Search.
- **시간 복잡도** → Time Complexity.
- **공간 복잡도** → Space Complexity.

---

## Testing

- **단위 테스트** → Unit Test.
- **통합 테스트** → Integration Test.
- **시스템 테스트** → System Test.
- **인수 테스트** → Acceptance Test.
- **회귀 테스트** → Regression Test.
- **재시험** → Retest.
- **블랙박스 테스트** → Black-box Testing.
- **화이트박스 테스트** → White-box Testing.
- **동등 분할** → Equivalence Partitioning.
- **경계값 분석** → Boundary Value Analysis.
- **문장 커버리지** → Statement Coverage.
- **분기 커버리지** → Branch Coverage.
- **경로 커버리지** → Path Coverage.
- **스텁** → Stub.
- **드라이버** → Driver.
- **알파 테스트** → Alpha Test.
- **베타 테스트** → Beta Test.
- **순환 복잡도** → Cyclomatic Complexity.

### Dấu hiệu

`상위 모듈부터` + lower chưa có → Stub.

`하위 모듈부터` + caller chưa có → Driver.

---

## Configuration / Packaging

- **형상관리** → Configuration Management.
- **버전 관리** → Version Control.
- **베이스라인** → Baseline.
- **빌드** → Build.
- **패키징** → Packaging.
- **배포** → Deployment/Distribution tùy context.
- **릴리스** → Release.
- **무결성** → Integrity.

---

# 3. 데이터베이스 구축 — Database Construction

## Relational Model

- **릴레이션** → Relation.
- **튜플** → Tuple → row.
- **속성** → Attribute → column.
- **도메인** → Domain.
- **슈퍼키** → Super Key.
- **후보키** → Candidate Key.
- **기본키** → Primary Key.
- **대체키** → Alternate Key.
- **외래키** → Foreign Key.
- **개체 무결성** → Entity Integrity.
- **참조 무결성** → Referential Integrity.
- **도메인 무결성** → Domain Integrity.

---

## Relational Algebra

- **셀렉션/선택** → Selection → chọn row.
- **프로젝션/투영** → Projection → chọn column.
- **조인** → Join.
- **디비전/나눗셈** → Division.
- **합집합** → Union.
- **교집합** → Intersection.
- **차집합** → Difference.

---

## Dependency / Normalization

- **함수 종속** → Functional Dependency.
- **완전 함수 종속** → Full Functional Dependency.
- **부분 함수 종속** → Partial Functional Dependency.
- **이행적 함수 종속** → Transitive Functional Dependency.
- **정규화** → Normalization.
- **제1정규형** → First Normal Form, 1NF.
- **제2정규형** → 2NF.
- **제3정규형** → 3NF.
- **BCNF** → Boyce-Codd Normal Form.
- **이상 현상** → Anomaly.
- **삽입 이상** → Insertion Anomaly.
- **삭제 이상** → Deletion Anomaly.
- **갱신 이상** → Update Anomaly.

---

## Physical DB / Index

- **인덱스** → Index.
- **선택도** → Selectivity.
- **카디널리티** → Cardinality.
- **클러스터링** → Clustering.
- **파티셔닝** → Partitioning.
- **비정규화** → Denormalization.
- **B+ 트리** → B+Tree.
- **해시 인덱스** → Hash Index.

---

## Transaction / Concurrency

- **트랜잭션** → Transaction.
- **원자성** → Atomicity.
- **일관성** → Consistency.
- **고립성/격리성** → Isolation.
- **영속성** → Durability.
- **잠금** → Lock.
- **교착상태** → Deadlock.
- **직렬 가능성** → Serializability.
- **직렬 스케줄** → Serial Schedule.
- **선행 그래프** → Precedence Graph.
- **더티 리드** → Dirty Read.
- **반복 불가능 읽기** → Non-repeatable Read.
- **팬텀 리드** → Phantom Read.
- **회복** → Recovery.
- **로그** → Log.
- **체크포인트** → Checkpoint.
- **Undo** → 실행 취소/롤백 복구.
- **Redo** → 재실행 복구.

---

# 4. 프로그래밍 언어 활용 — Programming Language Application

## OS

- **프로세스** → Process.
- **스레드** → Thread.
- **동시성** → Concurrency.
- **병렬성** → Parallelism.
- **경쟁 상태** → Race Condition.
- **임계 구역** → Critical Section.
- **상호 배제** → Mutual Exclusion.
- **뮤텍스** → Mutex.
- **세마포어** → Semaphore.
- **교착상태** → Deadlock.
- **기아 상태** → Starvation.
- **문맥 교환** → Context Switch.
- **선점형** → Preemptive.
- **비선점형** → Non-preemptive.

Scheduling:

- **선입선처리** → FCFS.
- **최단 작업 우선** → SJF.
- **최단 잔여 시간 우선** → SRTF.
- **라운드 로빈** → Round Robin.
- **우선순위 스케줄링** → Priority Scheduling.
- **에이징** → Aging.
- **응답률 우선** → HRN.

Metrics:

- **대기 시간** → Waiting Time.
- **반환 시간** → Turnaround Time.
- **응답 시간** → Response Time.

---

## Memory

- **페이징** → Paging.
- **세그먼테이션** → Segmentation.
- **페이지** → Page.
- **프레임** → Frame.
- **페이지 폴트** → Page Fault.
- **페이지 교체** → Page Replacement.
- **스래싱** → Thrashing.
- **작업 집합** → Working Set.
- **내부 단편화** → Internal Fragmentation.
- **외부 단편화** → External Fragmentation.
- **가상 메모리** → Virtual Memory.

Replacement:

- **FIFO** → First-In First-Out.
- **LRU** → Least Recently Used.
- **LFU** → Least Frequently Used.
- **최적 교체** → Optimal Replacement.

---

## Network

- **물리 계층** → Physical Layer.
- **데이터 링크 계층** → Data Link Layer.
- **네트워크 계층** → Network Layer.
- **전송 계층** → Transport Layer.
- **세션 계층** → Session Layer.
- **표현 계층** → Presentation Layer.
- **응용 계층** → Application Layer.

- **라우팅** → Routing.
- **라우터** → Router.
- **스위치** → Switch.
- **서브넷** → Subnet.
- **서브넷 마스크** → Subnet Mask.
- **네트워크 주소** → Network Address.
- **브로드캐스트 주소** → Broadcast Address.
- **기본 게이트웨이** → Default Gateway.
- **최장 접두어 일치** → Longest Prefix Match.
- **도메인 이름 시스템** → DNS.
- **동적 호스트 설정 프로토콜** → DHCP.
- **주소 결정 프로토콜** → ARP.

---

## Language Terms

C:

- **포인터** → Pointer.
- **역참조** → Dereference.
- **주소 연산자** → Address operator.
- **구조체** → struct.
- **공용체** → union.
- **재귀** → Recursion.

Java:

- **상속** → Inheritance.
- **다형성** → Polymorphism.
- **추상 클래스** → Abstract Class.
- **인터페이스** → Interface.
- **예외** → Exception.
- **동적 바인딩** → Dynamic Binding/Dispatch.

Python:

- **가변 객체** → Mutable Object.
- **불변 객체** → Immutable Object.
- **슬라이싱** → Slicing.
- **참조/별칭** → Reference/Alias.

---

# 5. 정보시스템 구축 관리 — Information System Construction Management

## Methodology / Project

- **폭포수 모델** → Waterfall Model.
- **애자일** → Agile.
- **반복적 개발** → Iterative Development.
- **점진적 개발** → Incremental Development.
- **위험** → Risk.
- **이슈** → Issue.
- **임계 경로** → Critical Path.
- **여유 시간** → Slack/Float.
- **PERT** → Program Evaluation and Review Technique.
- **CPM** → Critical Path Method.

---

## Infrastructure / Availability

- **가용성** → Availability.
- **고가용성** → High Availability, HA.
- **이중화** → Redundancy.
- **복제** → Replication.
- **백업** → Backup.
- **장애 조치** → Failover.
- **재해 복구** → Disaster Recovery, DR.
- **복구 시간 목표** → Recovery Time Objective, RTO.
- **복구 시점 목표** → Recovery Point Objective, RPO.
- **장애 지점** → Failure Point.
- **단일 장애점** → Single Point of Failure, SPOF.
- **수직 확장** → Vertical Scaling.
- **수평 확장** → Horizontal Scaling.

Storage:

- **미러링** → Mirroring.
- **스트라이핑** → Striping.
- **패리티** → Parity.
- **RAID** → Redundant Array of Independent Disks.

Cloud:

- **서비스형 인프라** → IaaS.
- **서비스형 플랫폼** → PaaS.
- **서비스형 소프트웨어** → SaaS.
- **가상 머신** → Virtual Machine, VM.
- **컨테이너** → Container.

---

## Security

- **인증** → Authentication.
- **인가/권한 부여** → Authorization.
- **기밀성** → Confidentiality.
- **무결성** → Integrity.
- **가용성** → Availability.
- **암호화** → Encryption.
- **복호화** → Decryption.
- **해시** → Hash.
- **전자서명/디지털 서명** → Digital Signature.
- **대칭키 암호** → Symmetric Cryptography.
- **공개키/비대칭키 암호** → Public-key/Asymmetric Cryptography.
- **최소 권한** → Least Privilege.
- **취약점** → Vulnerability.
- **위협** → Threat.
- **위험** → Risk.
- **보안 통제** → Security Control.

Attack/control:

- **SQL 삽입** → SQL Injection.
- **사이트 간 스크립팅** → Cross-Site Scripting, XSS.
- **사이트 간 요청 위조** → Cross-Site Request Forgery, CSRF.
- **서비스 거부** → Denial of Service, DoS.
- **분산 서비스 거부** → Distributed DoS, DDoS.
- **방화벽** → Firewall.
- **웹 애플리케이션 방화벽** → Web Application Firewall, WAF.
- **침입 탐지 시스템** → IDS.
- **침입 방지 시스템** → IPS.
- **가상 사설망** → VPN.
- **전송 계층 보안** → TLS.

---

# 6. Korean wording patterns trong câu hỏi

## “가장 적절한 것”

→ “cái phù hợp nhất”. Có thể nhiều đáp án đúng một phần; chọn đáp án khớp **scope + wording** nhất.

## “옳지 않은 것”

→ chọn câu **không đúng**. Đây là nguồn careless error lớn; đánh dấu NOT trước khi đọc options.

## “해당하지 않는 것”

→ “không thuộc nhóm/không áp dụng”. Trước hết xác định category đang hỏi.

## “주된 목적”

→ hỏi **primary purpose**, không phải side effect.

## “가장 직접적인”

→ ưu tiên control/mechanism xử lý root cause trực tiếp hơn defense phụ.

## “보장하는”

→ từ mạnh. Một mechanism chỉ “giúp” không nhất thiết “guarantee”. Cẩn thận các option tuyệt đối như 항상, 반드시, 완전히.

## “일반적으로”

→ hỏi behavior/convention thường gặp, không phải exception hiếm.

## “~에 대한 설명으로 옳은 것”

→ cần map exact definition, đừng chọn statement đúng nhưng thuộc concept hàng xóm.

---

# 7. Closed-book term drill

Không nhìn phần trên, tự dịch và giải thích mechanism của 30 từ sau:

```text
추적성
응집도
결합도
스탬프 결합도
다형성
실체화
순환 복잡도
회귀 테스트
베이스라인
후보키
부분 함수 종속
이행적 함수 종속
선택도
직렬 가능성
반복 불가능 읽기
체크포인트
임계 구역
상호 배제
기아 상태
반환 시간
페이지 폴트
스래싱
최장 접두어 일치
임계 경로
이중화
장애 조치
복구 시간 목표
복구 시점 목표
최소 권한
침입 방지 시스템
```

Một term chỉ tính là “biết” khi có thể nói đủ ba tầng:

```text
Korean term → English concept → mechanism/ranh giới
```

Ví dụ không đủ: `스래싱 = thrashing`.

Ví dụ đạt: `스래싱 = thrashing = hệ thống dành quá nhiều thời gian paging vì working set/frame pressure, khiến useful CPU work giảm mạnh`.