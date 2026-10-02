# 정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **요구사항 — yêu cầu (requirement / 요구사항)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **구조적 분석 — Structured phân tích (analysis / 분석)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Korean terms với requirements và structured analysis, để thuật ngữ Hàn–Việt đi cùng khái niệm sở hữu.

> Mục tiêu: khi gặp thuật ngữ tiếng Hàn trong đề, phải map ngay được sang **English concept → nghĩa Việt → cơ chế (mechanism / 메커니즘)**, không dừng ở dịch từ. tệp (file / 파일) này chỉ giữ các thuật ngữ có giá trị phân biệt cao hoặc dễ gây nhầm.

---

# 1. 소프트웨어 설계 — Software thiết kế (design / 설계)

## 요구사항 — yêu cầu (requirement / 요구사항)

**요구사항** → yêu cầu (requirement / 요구사항) → yêu cầu hệ thống.

- **기능 요구사항** → Functional yêu cầu (requirement / 요구사항) → hệ thống phải làm gì.
- **비기능 요구사항** → Non-functional yêu cầu (requirement / 요구사항) → chất lượng/ràng buộc phải đạt.
- **요구사항 도출** → yêu cầu (requirement / 요구사항) Elicitation → khai thác yêu cầu từ stakeholder/nguồn (source / 소스).
- **요구사항 분석** → phân tích yêu cầu (requirement analysis / 요구사항 분석) → xử lý xung đột (conflict / 충돌), phụ thuộc (dependency / 의존성), feasibility, priority.
- **요구사항 명세** → yêu cầu (requirement / 요구사항) Specification → đặc tả yêu cầu rõ, testable.
- **요구사항 확인/검증** → yêu cầu (requirement / 요구사항) kiểm tra hợp lệ (validation / 검증)/xác minh (verification / 확인) tùy ngữ cảnh giáo trình → kiểm tính đúng/đủ/phù hợp.
- **추적성** → Traceability → liên kết yêu cầu (requirement / 요구사항) với nguồn (source / 소스)/thiết kế (design / 설계)/mã (code / 코드)/kiểm thử (test / 테스트).

### Dấu hiệu

`추적`, `영향 분석`, `요구사항 변경` thường kéo về traceability/thay đổi (change / 변경) impact.

---

> **Chuyển mạch:** Trong **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **구조적 분석 — Structured phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **요구사항 — yêu cầu (requirement / 요구사항)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **UML** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 구조적 분석 — Structured phân tích (analysis / 분석)

- **자료 흐름도** → luồng dữ liệu (data flow / 데이터 흐름) Diagram, DFD → sơ đồ luồng dữ liệu.
- **자료 사전** → dữ liệu (data / 데이터) Dictionary → từ điển dữ liệu.
- **소단위 명세서** → Mini-specification → đặc tả lô-gic (logic / 논리) tiến trình (process / 프로세스) chi tiết.
- **프로세스** → tiến trình (process / 프로세스) → biến đổi đầu vào (input / 입력) dữ liệu (data / 데이터) thành đầu ra (output / 출력) dữ liệu (data / 데이터) trong DFD.
- **자료 저장소** → dữ liệu (data / 데이터) Store → nơi lưu dữ liệu.
- **단말/외부 개체** → bên ngoài (external / 외부) thực thể (entity / 엔터티) → nguồn/đích ngoài hệ thống (system / 시스템) ranh giới (boundary / 경계).

---

> **Chuyển mạch:** Ở chặng này của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **UML** tiếp nhận điểm tựa từ **구조적 분석 — Structured phân tích (analysis / 분석)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô-đun (module / 모듈) thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## UML

- **유스케이스 다이어그램** → Use trường hợp (case / 사례) Diagram.
- **클래스 다이어그램** → lớp (class / 클래스) Diagram.
- **객체 다이어그램** → đối tượng (object / 객체) Diagram.
- **순차 다이어그램** → chuỗi (sequence / 시퀀스) Diagram.
- **활동 다이어그램** → Activity Diagram.
- **상태 다이어그램** → trạng thái (state / 상태) Diagram.
- **컴포넌트 다이어그램** → thành phần (component / 컴포넌트) Diagram.
- **배치 다이어그램** → triển khai (deployment / 배포) Diagram.
- **일반화** → Generalization.
- **연관** → Association.
- **집합** → Aggregation.
- **합성** → Composition.
- **의존** → phụ thuộc (dependency / 의존성).
- **실체화** → Realization.

### Dấu hiệu

`시간 순서`, `메시지` → chuỗi (sequence / 시퀀스).

`상태 변화`, `이벤트` → trạng thái (state / 상태).

`노드`, `배치` → triển khai (deployment / 배포).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Mô-đun (module / 모듈) thiết kế (design / 설계)** tiếp nhận điểm tựa từ **UML** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **OOP / mẫu thiết kế (design pattern / 디자인 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô-đun (module / 모듈) thiết kế (design / 설계)

- **응집도** → Cohesion → mức gắn kết bên trong mô-đun (module / 모듈).
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
- **공통 결합도** → dùng chung (common / 공통) Coupling.
- **외부 결합도** → bên ngoài (external / 외부) Coupling.
- **제어 결합도** → điều khiển (control / 제어) Coupling.
- **스탬프 결합도** → Stamp Coupling.
- **자료 결합도** → dữ liệu (data / 데이터) Coupling.

### Trật tự thi hay hỏi

Cohesion: càng functional càng mạnh/tốt.

Coupling: càng dữ liệu (data / 데이터) càng yếu/tốt trong bộ classic.

---

> **Chuyển mạch:** Trong **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **OOP / mẫu thiết kế (design pattern / 디자인 패턴)** tiếp nhận điểm tựa từ **Mô-đun (module / 모듈) thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấu trúc dữ liệu (data structure / 자료구조) / thuật toán (algorithm / 알고리즘)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OOP / mẫu thiết kế (design pattern / 디자인 패턴)

- **캡슐화** → Encapsulation → đóng gói/kiểm soát trạng thái (state / 상태).
- **상속** → Inheritance → kế thừa.
- **다형성** → Polymorphism → đa hình.
- **추상화** → lớp trừu tượng (abstraction / 추상화) → trừu tượng hóa.
- **오버로딩** → Overloading.
- **오버라이딩** → Overriding.

Mẫu (pattern / 패턴) terms:

- **전략 패턴** → chiến lược (strategy / 전략) mẫu (pattern / 패턴).
- **상태 패턴** → trạng thái (state / 상태) mẫu (pattern / 패턴).
- **옵저버 패턴** → Observer mẫu (pattern / 패턴).
- **어댑터 패턴** → Adapter mẫu (pattern / 패턴).
- **퍼사드 패턴** → Facade mẫu (pattern / 패턴).
- **데코레이터 패턴** → Decorator mẫu (pattern / 패턴).
- **프록시 패턴** → Proxy mẫu (pattern / 패턴).
- **팩토리 메서드** → Factory phương thức (method / 메서드).
- **추상 팩토리** → Abstract Factory.
- **빌더** → Builder.
- **프로토타입** → Prototype.
- **싱글턴** → Singleton.
- **커맨드** → Command.
- **템플릿 메서드** → Template phương thức (method / 메서드).
- **이터레이터** → Iterator.

---

# 2. 소프트웨어 개발 — Software Development

> **Chuyển mạch:** Ở chặng này của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **OOP / mẫu thiết kế (design pattern / 디자인 패턴)** nêu điều cần giải thích; **Cấu trúc dữ liệu (data structure / 자료구조) / thuật toán (algorithm / 알고리즘)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấu trúc dữ liệu (data structure / 자료구조) / thuật toán (algorithm / 알고리즘)

- **자료구조** → cấu trúc dữ liệu (data structure / 자료구조).
- **스택** → ngăn xếp (stack / 스택) → LIFO.
- **큐** → hàng đợi (queue / 큐) → FIFO.
- **트리** → cây (tree / 트리).
- **그래프** → đồ thị (graph / 그래프).
- **이진 탐색 트리** → tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리).
- **힙** → vùng nhớ động (heap / 힙).
- **해시** → băm (hash / 해시).
- **충돌** → Collision.
- **선형 조사법** → tuyến tính (linear / 선형) Probing.
- **너비 우선 탐색** → Breadth-First tìm kiếm (search / 검색), BFS.
- **깊이 우선 탐색** → Depth-First tìm kiếm (search / 검색), DFS.
- **이진 탐색** → tìm kiếm nhị phân (binary search / 이진 탐색).
- **시간 복잡도** → thời gian (time / 시간) độ phức tạp (complexity / 복잡도).
- **공간 복잡도** → không gian (space / 공간) độ phức tạp (complexity / 복잡도).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Cấu trúc dữ liệu (data structure / 자료구조) / thuật toán (algorithm / 알고리즘)** nêu điều cần giải thích; **Testing** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Cấu hình (configuration / 구성) / Packaging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Testing

- **단위 테스트** → đơn vị (unit / 단위) kiểm thử (test / 테스트).
- **통합 테스트** → kiểm thử tích hợp (integration test / 통합 테스트).
- **시스템 테스트** → hệ thống (system / 시스템) kiểm thử (test / 테스트).
- **인수 테스트** → Acceptance kiểm thử (test / 테스트).
- **회귀 테스트** → Regression kiểm thử (test / 테스트).
- **재시험** → Retest.
- **블랙박스 테스트** → Black-box Testing.
- **화이트박스 테스트** → White-box Testing.
- **동등 분할** → Equivalence Partitioning.
- **경계값 분석** → ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석).
- **문장 커버리지** → Statement Coverage.
- **분기 커버리지** → Branch Coverage.
- **경로 커버리지** → đường dẫn (path / 경로) Coverage.
- **스텁** → Stub.
- **드라이버** → Driver.
- **알파 테스트** → Alpha kiểm thử (test / 테스트).
- **베타 테스트** → Beta kiểm thử (test / 테스트).
- **순환 복잡도** → Cyclomatic độ phức tạp (complexity / 복잡도).

### Dấu hiệu

`상위 모듈부터` + lower chưa có → Stub.

`하위 모듈부터` + caller chưa có → Driver.

---

> **Chuyển mạch:** Trong **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Cấu hình (configuration / 구성) / Packaging** tiếp nhận điểm tựa từ **Testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Relational mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấu hình (configuration / 구성) / Packaging

- **형상관리** → cấu hình (configuration / 구성) Management.
- **버전 관리** → phiên bản (version / 버전) điều khiển (control / 제어).
- **베이스라인** → Baseline.
- **빌드** → bản dựng (build / 빌드).
- **패키징** → Packaging.
- **배포** → triển khai (deployment / 배포)/phân phối (distribution / 분포) tùy ngữ cảnh (context / 맥락).
- **릴리스** → bản phát hành (release / 릴리스).
- **무결성** → Integrity.

---

# 3. 데이터베이스 구축 — cơ sở dữ liệu (database / 데이터베이스) Construction

> **Chuyển mạch:** Ở chặng này của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Relational mô hình (model / 모델)** tiếp nhận điểm tựa từ **Cấu hình (configuration / 구성) / Packaging** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Relational Algebra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Relational mô hình (model / 모델)

- **릴레이션** → quan hệ (relation / 관계).
- **튜플** → Tuple → row.
- **속성** → Attribute → column.
- **도메인** → lĩnh vực (domain / 도메인).
- **슈퍼키** → Super Key.
- **후보키** → Candidate Key.
- **기본키** → Primary Key.
- **대체키** → Alternate Key.
- **외래키** → Foreign Key.
- **개체 무결성** → thực thể (entity / 엔터티) Integrity.
- **참조 무결성** → Referential Integrity.
- **도메인 무결성** → lĩnh vực (domain / 도메인) Integrity.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Relational Algebra** tiếp nhận điểm tựa từ **Relational mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phụ thuộc (dependency / 의존성) / Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Relational Algebra

- **셀렉션/선택** → Selection → chọn row.
- **프로젝션/투영** → Projection → chọn column.
- **조인** → phép nối (join / 조인).
- **디비전/나눗셈** → Division.
- **합집합** → Union.
- **교집합** → Intersection.
- **차집합** → Difference.

---

> **Chuyển mạch:** Trong **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Phụ thuộc (dependency / 의존성) / Normalization** tiếp nhận điểm tựa từ **Relational Algebra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vật lý (physical / 물리적) DB / chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phụ thuộc (dependency / 의존성) / Normalization

- **함수 종속** → Functional phụ thuộc (dependency / 의존성).
- **완전 함수 종속** → Full Functional phụ thuộc (dependency / 의존성).
- **부분 함수 종속** → Partial Functional phụ thuộc (dependency / 의존성).
- **이행적 함수 종속** → Transitive Functional phụ thuộc (dependency / 의존성).
- **정규화** → Normalization.
- **제1정규형** → First Normal Form, 1NF.
- **제2정규형** → 2NF.
- **제3정규형** → 3NF.
- **BCNF** → Boyce-Codd Normal Form.
- **이상 현상** → Anomaly.
- **삽입 이상** → Insertion Anomaly.
- **삭제 이상** → Deletion Anomaly.
- **갱신 이상** → cập nhật (update / 업데이트) Anomaly.

---

> **Chuyển mạch:** Ở chặng này của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Vật lý (physical / 물리적) DB / chỉ mục (index / 인덱스)** tiếp nhận điểm tựa từ **Phụ thuộc (dependency / 의존성) / Normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giao dịch (transaction / 트랜잭션) / tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vật lý (physical / 물리적) DB / chỉ mục (index / 인덱스)

- **인덱스** → chỉ mục (index / 인덱스).
- **선택도** → Selectivity.
- **카디널리티** → Cardinality.
- **클러스터링** → Clustering.
- **파티셔닝** → Partitioning.
- **비정규화** → Denormalization.
- **B+ 트리** → B+cây (tree / 트리).
- **해시 인덱스** → băm (hash / 해시) chỉ mục (index / 인덱스).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Giao dịch (transaction / 트랜잭션) / tính đồng thời (concurrency / 동시성)** tiếp nhận điểm tựa từ **Vật lý (physical / 물리적) DB / chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **OS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giao dịch (transaction / 트랜잭션) / tính đồng thời (concurrency / 동시성)

- **트랜잭션** → giao dịch (transaction / 트랜잭션).
- **원자성** → Atomicity.
- **일관성** → Consistency.
- **고립성/격리성** → Isolation.
- **영속성** → Durability.
- **잠금** → khóa (lock / 잠금).
- **교착상태** → Deadlock.
- **직렬 가능성** → Serializability.
- **직렬 스케줄** → Serial Schedule.
- **선행 그래프** → Precedence đồ thị (graph / 그래프).
- **더티 리드** → Dirty Read.
- **반복 불가능 읽기** → Non-repeatable Read.
- **팬텀 리드** → Phantom Read.
- **회복** → khôi phục (recovery / 복구).
- **로그** → Log.
- **체크포인트** → Checkpoint.
- **Undo** → 실행 취소/롤백 복구.
- **Redo** → 재실행 복구.

---

# 4. 프로그래밍 언어 활용 — Programming ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)

> **Chuyển mạch:** Trong **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **OS** tiếp nhận điểm tựa từ **Giao dịch (transaction / 트랜잭션) / tính đồng thời (concurrency / 동시성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OS

- **프로세스** → tiến trình (process / 프로세스).
- **스레드** → luồng thực thi (thread / 스레드).
- **동시성** → tính đồng thời (concurrency / 동시성).
- **병렬성** → Parallelism.
- **경쟁 상태** → Race điều kiện (condition / 조건).
- **임계 구역** → trọng yếu (critical / 중요) Section.
- **상호 배제** → Mutual Exclusion.
- **뮤텍스** → Mutex.
- **세마포어** → Semaphore.
- **교착상태** → Deadlock.
- **기아 상태** → Starvation.
- **문맥 교환** → ngữ cảnh (context / 맥락) Switch.
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

- **대기 시간** → Waiting thời gian (time / 시간).
- **반환 시간** → Turnaround thời gian (time / 시간).
- **응답 시간** → phản hồi (response / 응답) thời gian (time / 시간).

---

> **Chuyển mạch:** Ở chặng này của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **OS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mạng (network / 네트워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리)

- **페이징** → Paging.
- **세그먼테이션** → Segmentation.
- **페이지** → Page.
- **프레임** → Frame.
- **페이지 폴트** → Page Fault.
- **페이지 교체** → Page Replacement.
- **스래싱** → Thrashing.
- **작업 집합** → Working Set.
- **내부 단편화** → nội bộ (internal / 내부) Fragmentation.
- **외부 단편화** → bên ngoài (external / 외부) Fragmentation.
- **가상 메모리** → Virtual bộ nhớ (memory / 메모리).

Replacement:

- **FIFO** → First-In First-Out.
- **LRU** → Least Recently Used.
- **LFU** → Least Frequently Used.
- **최적 교체** → Optimal Replacement.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Mạng (network / 네트워크)** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngôn ngữ (language / 언어) Terms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mạng (network / 네트워크)

- **물리 계층** → vật lý (physical / 물리적) tầng (layer / 계층).
- **데이터 링크 계층** → dữ liệu (data / 데이터) Link tầng (layer / 계층).
- **네트워크 계층** → mạng (network / 네트워크) tầng (layer / 계층).
- **전송 계층** → tầng vận chuyển (transport layer / 전송 계층).
- **세션 계층** → Session tầng (layer / 계층).
- **표현 계층** → Presentation tầng (layer / 계층).
- **응용 계층** → ứng dụng (application / 애플리케이션) tầng (layer / 계층).

- **라우팅** → Routing.
- **라우터** → Router.
- **스위치** → Switch.
- **서브넷** → Subnet.
- **서브넷 마스크** → Subnet Mask.
- **네트워크 주소** → mạng (network / 네트워크) Address.
- **브로드캐스트 주소** → Broadcast Address.
- **기본 게이트웨이** → Default Gateway.
- **최장 접두어 일치** → Longest Prefix Match.
- **도메인 이름 시스템** → DNS.
- **동적 호스트 설정 프로토콜** → DHCP.
- **주소 결정 프로토콜** → ARP.

---

> **Chuyển mạch:** Trong **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Ngôn ngữ (language / 언어) Terms** tiếp nhận điểm tựa từ **Mạng (network / 네트워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Methodology / dự án (project / 프로젝트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngôn ngữ (language / 언어) Terms

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
- **추상 클래스** → Abstract lớp (class / 클래스).
- **인터페이스** → giao diện (interface / 인터페이스).
- **예외** → Exception.
- **동적 바인딩** → động (dynamic / 동적) Binding/Dispatch.

Python:

- **가변 객체** → Mutable đối tượng (object / 객체).
- **불변 객체** → Immutable đối tượng (object / 객체).
- **슬라이싱** → Slicing.
- **참조/별칭** → tham chiếu (reference / 참조)/Alias.

---

# 5. 정보시스템 구축 관리 — thông tin (information / 정보) hệ thống (system / 시스템) Construction Management

> **Chuyển mạch:** Ở chặng này của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Methodology / dự án (project / 프로젝트)** tiếp nhận điểm tựa từ **Ngôn ngữ (language / 언어) Terms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hạ tầng (infrastructure / 인프라) / Availability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Methodology / dự án (project / 프로젝트)

- **폭포수 모델** → Waterfall mô hình (model / 모델).
- **애자일** → Agile.
- **반복적 개발** → Iterative Development.
- **점진적 개발** → Incremental Development.
- **위험** → rủi ro (risk / 위험).
- **이슈** → Issue.
- **임계 경로** → đường găng (critical path / 임계 경로).
- **여유 시간** → Slack/Float.
- **PERT** → Program Evaluation and rà soát (review / 검토) Technique.
- **CPM** → đường găng (critical path / 임계 경로) phương thức (method / 메서드).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Methodology / dự án (project / 프로젝트)** cho ta quy tắc; **Hạ tầng (infrastructure / 인프라) / Availability** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Bảo mật (security / 보안)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hạ tầng (infrastructure / 인프라) / Availability

- **가용성** → Availability.
- **고가용성** → High Availability, HA.
- **이중화** → Redundancy.
- **복제** → Replication.
- **백업** → Backup.
- **장애 조치** → Failover.
- **재해 복구** → Disaster khôi phục (recovery / 복구), DR.
- **복구 시간 목표** → khôi phục (recovery / 복구) thời gian (time / 시간) mục tiêu (objective / 목표), RTO.
- **복구 시점 목표** → khôi phục (recovery / 복구) điểm (point / 지점) mục tiêu (objective / 목표), RPO.
- **장애 지점** → thất bại (failure / 실패) điểm (point / 지점).
- **단일 장애점** → Single điểm (point / 지점) of thất bại (failure / 실패), SPOF.
- **수직 확장** → Vertical Scaling.
- **수평 확장** → Horizontal Scaling.

Lưu trữ (storage / 저장소):

- **미러링** → Mirroring.
- **스트라이핑** → Striping.
- **패리티** → Parity.
- **RAID** → Redundant Array of Independent Disks.

Cloud:

- **서비스형 인프라** → IaaS.
- **서비스형 플랫폼** → PaaS.
- **서비스형 소프트웨어** → SaaS.
- **가상 머신** → Virtual Machine, VM.
- **컨테이너** → bộ chứa (container / 컨테이너).

---

> **Chuyển mạch:** Trong **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **Hạ tầng (infrastructure / 인프라) / Availability** cho ta quy tắc; **Bảo mật (security / 보안)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **“가장 적절한 것”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo mật (security / 보안)

- **인증** → Authentication.
- **인가/권한 부여** → Authorization.
- **기밀성** → Confidentiality.
- **무결성** → Integrity.
- **가용성** → Availability.
- **암호화** → Encryption.
- **복호화** → Decryption.
- **해시** → băm (hash / 해시).
- **전자서명/디지털 서명** → Digital Signature.
- **대칭키 암호** → Symmetric Cryptography.
- **공개키/비대칭키 암호** → Public-key/Asymmetric Cryptography.
- **최소 권한** → Least Privilege.
- **취약점** → Vulnerability.
- **위협** → Threat.
- **위험** → rủi ro (risk / 위험).
- **보안 통제** → bảo mật (security / 보안) điều khiển (control / 제어).

Attack/điều khiển (control / 제어):

- **SQL 삽입** → SQL Injection.
- **사이트 간 스크립팅** → Cross-Site Scripting, XSS.
- **사이트 간 요청 위조** → Cross-Site yêu cầu (request / 요청) Forgery, CSRF.
- **서비스 거부** → Denial of dịch vụ (service / 서비스), DoS.
- **분산 서비스 거부** → phân tán (distributed / 분산) DoS, DDoS.
- **방화벽** → Firewall.
- **웹 애플리케이션 방화벽** → Web ứng dụng (application / 애플리케이션) Firewall, WAF.
- **침입 탐지 시스템** → IDS.
- **침입 방지 시스템** → IPS.
- **가상 사설망** → VPN.
- **전송 계층 보안** → TLS.

---

# 6. Korean wording patterns trong câu hỏi

> **Chuyển mạch:** Ở chặng này của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **“가장 적절한 것”** tiếp nhận điểm tựa từ **Bảo mật (security / 보안)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **“옳지 않은 것”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## “가장 적절한 것”

→ “cái phù hợp nhất”. Có thể nhiều đáp án đúng một phần; chọn đáp án khớp **phạm vi (scope / 범위) + wording** nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **“옳지 않은 것”** tiếp nhận điểm tựa từ **“가장 적절한 것”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **“해당하지 않는 것”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## “옳지 않은 것”

→ chọn câu **không đúng**. Đây là nguồn careless lỗi (error / 오류) lớn; đánh dấu NOT trước khi đọc options.

> **Chuyển mạch:** Trong **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **“해당하지 않는 것”** tiếp nhận điểm tựa từ **“옳지 않은 것”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **“주된 목적”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## “해당하지 않는 것”

→ “không thuộc nhóm/không áp dụng”. Trước hết xác định category đang hỏi.

> **Chuyển mạch:** Ở chặng này của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **“주된 목적”** tiếp nhận điểm tựa từ **“해당하지 않는 것”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **“가장 직접적인”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## “주된 목적”

→ hỏi **primary purpose**, không phải side tác động (effect / 효과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **“가장 직접적인”** tiếp nhận điểm tựa từ **“주된 목적”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **“보장하는”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## “가장 직접적인”

→ ưu tiên điều khiển (control / 제어)/cơ chế (mechanism / 메커니즘) xử lý nguyên nhân gốc (root cause / 근본 원인) trực tiếp hơn defense phụ.

> **Chuyển mạch:** Trong **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **“보장하는”** tiếp nhận điểm tựa từ **“가장 직접적인”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **“일반적으로”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## “보장하는”

→ từ mạnh. Một cơ chế (mechanism / 메커니즘) chỉ “giúp” không nhất thiết “guarantee”. Cẩn thận các option tuyệt đối như 항상, 반드시, 완전히.

> **Chuyển mạch:** Ở chặng này của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **“일반적으로”** tiếp nhận điểm tựa từ **“보장하는”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **“에 대한 설명으로 옳은 것”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## “일반적으로”

→ hỏi hành vi (behavior / 동작)/convention thường gặp, không phải exception hiếm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Korean Term cầu nối (bridge / 브리지)**, **“에 대한 설명으로 옳은 것”** tiếp nhận điểm tựa từ **“일반적으로”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## “~에 대한 설명으로 옳은 것”

→ cần map chính xác (exact / 정확한) definition, đừng chọn statement đúng nhưng thuộc concept hàng xóm.

---

# 7. Closed-book term drill

Không nhìn phần trên, tự dịch và giải thích cơ chế (mechanism / 메커니즘) của 30 từ sau:

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

> **Bàn giao:** Sau **“에 대한 설명으로 옳은 것”**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
