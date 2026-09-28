# 정보처리기사 필기 2026 — Full Mock Exam 100 Questions

> **Đề tự viết mới, không sao chép 기출.** Cấu trúc mô phỏng đúng tỷ lệ chính thức: 5 môn × 20 câu = 100 câu. Mục tiêu là kiểm tra coverage, discrimination và procedural lập luận (reasoning / 추론) sau khi hoàn thành Master Guide + 5 deep-dive + workbook.
>
> Làm toàn bộ câu hỏi trước khi mở phần đáp án. Với 20 câu mỗi môn, mỗi câu tương đương 5 điểm trong môn đó. Để mô phỏng điều kiện đỗ: mỗi môn cần ít nhất 8/20 câu đúng và tổng thể cần ít nhất 60/100 câu đúng.

---

# 제1과목 — 소프트웨어 설계 — Software thiết kế (design / 설계)

## Q1

Yêu cầu (requirement / 요구사항) nào là **non-functional yêu cầu (requirement / 요구사항) — 비기능 요구사항** rõ nhất?

A. người dùng (user / 사용자) có thể đổi mật khẩu
B. Admin có thể khóa tài khoản
C. 95% yêu cầu (request / 요청) phải trả lời trong 500 ms
D. người dùng (user / 사용자) có thể tải invoice

## Q2

Câu hỏi “Are we building the right sản phẩm (product / 제품)?” gắn gần nhất với:

A. xác minh (verification / 확인)
B. kiểm tra hợp lệ (validation / 검증)
C. Compilation
D. Refactoring

## Q3

Trong DFD — luồng dữ liệu (data flow / 데이터 흐름) Diagram — thành phần nào biểu diễn nơi dữ liệu được lưu giữ?

A. tiến trình (process / 프로세스)
B. dữ liệu (data / 데이터) Store
C. bên ngoài (external / 외부) thực thể (entity / 엔터티)
D. luồng dữ liệu (data flow / 데이터 흐름)

## Q4

Muốn biểu diễn thứ tự message giữa `Controller`, `Service`, `Repository` theo thời gian, diagram phù hợp nhất là:

A. chuỗi (sequence / 시퀀스) Diagram
B. lớp (class / 클래스) Diagram
C. triển khai (deployment / 배포) Diagram
D. gói (package / 패키지) Diagram

## Q5

`Order` chứa `OrderLine`; `OrderLine` không có vòng đời (lifecycle / 생명주기) độc lập và bị hủy khi `Order` bị hủy. Quan hệ UML phù hợp nhất:

A. Aggregation
B. Composition
C. phụ thuộc (dependency / 의존성)
D. Realization

## Q6

Mục tiêu thiết kế mô-đun (module / 모듈) tốt thường là:

A. Low cohesion, high coupling
B. High cohesion, high coupling
C. High cohesion, low coupling
D. Low cohesion, low coupling

## Q7

Mô-đun (module / 모듈) A chỉ truyền đúng `customerId` mà mô-đun (module / 모듈) B cần thông qua parameter. Đây gần nhất với:

A. Content Coupling
B. dùng chung (common / 공통) Coupling
C. điều khiển (control / 제어) Coupling
D. dữ liệu (data / 데이터) Coupling

## Q8

Mô-đun (module / 모듈) A truyền toàn bộ đối tượng (object / 객체) `Customer` cho B dù B chỉ dùng `customerId`. Đây gần nhất với:

A. Stamp Coupling
B. dữ liệu (data / 데이터) Coupling
C. Content Coupling
D. dùng chung (common / 공통) Coupling

## Q9

SOLID principle nào nhấn mạnh “một lớp (class / 클래스)/mô-đun (module / 모듈) nên có một lý do chính để thay đổi”?

A. SRP
B. OCP
C. LSP
D. DIP

## Q10

`PaymentService` nhận một giao diện (interface / 인터페이스) `PaymentGateway` qua constructor thay vì trực tiếp `new ConcreteKakaoClient()`. Thiết kế này hỗ trợ rõ nhất principle nào?

A. ISP
B. DIP
C. LSP
D. SRP

## Q11

Hệ thống cần thay đổi thuật toán tính discount tại thời gian chạy (runtime / 런타임) mà máy khách (client / 클라이언트) dùng cùng một giao diện (interface / 인터페이스). mẫu (pattern / 패턴) phù hợp nhất:

A. chiến lược (strategy / 전략)
B. trạng thái (state / 상태)
C. Observer
D. Prototype

## Q12

Một thư viện cũ có giao diện (interface / 인터페이스) `legacyPay()`, hệ thống mới mong đợi giao diện (interface / 인터페이스) `pay()`. mẫu (pattern / 패턴) phù hợp nhất để chuyển đổi giao diện (interface / 인터페이스):

A. Facade
B. Adapter
C. Singleton
D. Builder

## Q13

Máy khách (client / 클라이언트) cần một API đơn giản ở trước một subsystem phức tạp gồm nhiều lớp (class / 클래스). mẫu (pattern / 패턴) phù hợp nhất:

A. Facade
B. Proxy
C. Flyweight
D. Command

## Q14

Một đối tượng (object / 객체) thay đổi trạng thái và cần thông báo cho nhiều subscriber mà không hard-code từng subscriber. mẫu (pattern / 패턴) phù hợp nhất:

A. Template phương thức (method / 메서드)
B. Observer
C. Factory phương thức (method / 메서드)
D. Memento

## Q15

Sản phẩm tạo ra (artifact / 산출물) nào tập trung chủ yếu vào bố cục/cấu trúc màn hình, thường trước khi có tương tác hoàn chỉnh?

A. Wireframe
B. kiểm thử tải (load test / 부하 테스트)
C. triển khai (deployment / 배포) Diagram
D. dữ liệu (data / 데이터) Dictionary

## Q16

Trong Scrum, sản phẩm tạo ra (artifact / 산출물) chứa công việc được chọn cho Sprint cùng plan để đạt Sprint Goal là:

A. sản phẩm (product / 제품) Backlog
B. Sprint Backlog
C. Increment
D. sản phẩm (product / 제품) Vision

## Q17

Practice nào gắn mạnh với XP — Extreme Programming?

A. Pair Programming
B. Big thiết kế (design / 설계) Up Front bắt buộc
C. Không bao giờ refactor
D. Chỉ kiểm thử (test / 테스트) sau bản phát hành (release / 릴리스)

## Q18

Máy khách (client / 클라이언트) thử lại (retry / 재시도) cùng một payment yêu cầu (request / 요청) sau hết thời gian chờ (timeout / 타임아웃). thiết kế (design / 설계) concept nào trực tiếp giúp tránh thực hiện cùng side tác động (effect / 효과) nhiều lần khi cùng yêu cầu (request / 요청) định danh (identity / 식별자) được gửi lại?

A. Idempotency
B. Inheritance
C. Compression
D. Pagination

## Q19

Điểm yếu chính của point-to-point tích hợp (integration / 통합) khi số lượng hệ thống tăng mạnh là:

A. Không dùng được JSON
B. Số liên kết (connection / 연결)/phụ thuộc (dependency / 의존성) tăng khó quản lý
C. Không thể dùng cơ sở dữ liệu (database / 데이터베이스)
D. Không thể có authentication

## Q20

UML diagram nào phù hợp nhất để biểu diễn software sản phẩm tạo ra (artifact / 산출물)/thành phần (component / 컴포넌트) được triển khai trên nút (node / 노드)/máy chủ (server / 서버) nào?

A. Activity Diagram
B. triển khai (deployment / 배포) Diagram
C. trạng thái (state / 상태) Diagram
D. Use trường hợp (case / 사례) Diagram

---

# 제2과목 — 소프트웨어 개발 — Software Development

## Q21

Cấu trúc dữ liệu (data structure / 자료구조) nào hoạt động theo LIFO?

A. hàng đợi (queue / 큐)
B. ngăn xếp (stack / 스택)
C. vùng nhớ động (heap / 힙)
D. đồ thị (graph / 그래프)

## Q22

Cấu trúc dữ liệu (data structure / 자료구조) nào hoạt động theo FIFO trong mô hình cơ bản?

A. ngăn xếp (stack / 스택)
B. hàng đợi (queue / 큐)
C. tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리)
D. băm (hash / 해시) hàm (function / 함수)

## Q23

Traversal nào của BST với key phân biệt cho kết quả theo thứ tự tăng dần?

A. Preorder
B. Inorder
C. Postorder
D. Level-order

## Q24

Trong đồ thị (graph / 그래프) không trọng số, thuật toán nền tảng tìm shortest đường dẫn (path / 경로) theo số cạnh từ một nguồn (source / 소스) là:

A. BFS
B. DFS
C. Prim
D. Kruskal

## Q25

Worst-case thời gian (time / 시간) độ phức tạp (complexity / 복잡도) điển hình của Quick Sort là:

A. O(1)
B. O(log n)
C. O(n log n)
D. O(n²)

## Q26

Merge Sort có worst-case thời gian (time / 시간) độ phức tạp (complexity / 복잡도) điển hình là:

A. O(n²)
B. O(n log n)
C. O(log n)
D. O(1)

## Q27

Tuyến tính (linear / 선형) Probing trong bảng băm (hash table / 해시 테이블) dễ gây:

A. Primary Clustering
B. Dirty Read
C. Dead mã (code / 코드)
D. ngăn xếp (stack / 스택) Overflow bắt buộc

## Q28

Trong Top-down tích hợp (integration / 통합) Testing, mô-đun (module / 모듈) cấp dưới chưa sẵn sàng thường được thay bằng:

A. Driver
B. Stub
C. trình biên dịch (compiler / 컴파일러)
D. Proxy máy chủ (server / 서버)

## Q29

Trong Bottom-up tích hợp (integration / 통합) Testing, thành phần (component / 컴포넌트) gọi phía trên chưa sẵn sàng thường được thay bằng:

A. Driver
B. Stub
C. Semaphore
D. chỉ mục (index / 인덱스)

## Q30

Technique nào thuộc Black-box Testing?

A. Statement Coverage
B. Branch Coverage
C. ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석)
D. đường dẫn (path / 경로) Coverage

## Q31

Chỉ số (metric / 지표) nào kiểm tra các branch/quyết định (decision / 결정) outcomes trong white-box testing?

A. ranh giới (boundary / 경계) Coverage
B. Branch Coverage
C. Equivalence Partitioning
D. Usability Coverage

## Q32

Control-flow đồ thị (graph / 그래프) có `E=12`, `N=10`, một connected thành phần (component / 컴포넌트). Cyclomatic độ phức tạp (complexity / 복잡도) là:

A. 2
B. 3
C. 4
D. 12

## Q33

Sau khi sửa bug trong mô-đun (module / 모듈) thanh toán, nhóm (team / 팀) chạy lại các kiểm thử (test / 테스트) cũ để bảo đảm chức năng trước đó không bị phá. Đây là:

A. Regression Testing
B. Smoke-free Testing
C. Mutation bắt buộc
D. Acceptance only

## Q34

Testing do một nhóm người dùng bên ngoài tổ chức thực hiện trước bản phát hành (release / 릴리스) rộng rãi thường gần nhất với:

A. Alpha Testing
B. Beta Testing
C. đơn vị (unit / 단위) Testing
D. Static phân tích (analysis / 분석)

## Q35

Baseline trong cấu hình (configuration / 구성) Management gần nhất với:

A. Một mốc cấu hình đã được xác lập/kiểm soát, thay đổi qua procedure
B. Bất kỳ tệp (file / 파일) tạm nào chưa lần ghi nhận (commit / 커밋)
C. Password mặc định
D. CPU scheduling hàng đợi (queue / 큐)

## Q36

Phiên bản (version / 버전) điều khiển (control / 제어) giúp giải quyết trực tiếp nhất vấn đề nào?

A. Theo dõi lịch sử thay đổi nguồn (source / 소스)/sản phẩm tạo ra (artifact / 산출물) và phối hợp phiên bản
B. Tăng RAM vật lý
C. Mã hóa toàn bộ mạng (network / 네트워크) traffic
D. Thay thế cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션)

## Q37

Mục đích của software packaging gần nhất với:

A. Chuẩn bị software, phụ thuộc (dependency / 의존성), siêu dữ liệu (metadata / 메타데이터)/manual cần thiết để phân phối/cài đặt
B. Chỉ nén nguồn (source / 소스) thành ZIP bất kể triển khai (deployment / 배포)
C. Thay thế mọi kiểm thử (test / 테스트)
D. Xóa phiên bản (version / 버전) thông tin (information / 정보)

## Q38

Chỉ số (metric / 지표) nào đo số yêu cầu (request / 요청)/giao dịch (transaction / 트랜잭션) được xử lý trong một đơn vị thời gian?

A. thông lượng (throughput / 처리량)
B. phản hồi (response / 응답) thời gian (time / 시간)
C. độ trễ (latency / 지연 시간) percentile duy nhất
D. Defect Density

## Q39

Nếu giao diện (interface / 인터페이스) nhận JSON và cần kiểm tra trường dữ liệu (field / 필드) bắt buộc, kiểu (type / 타입) và format trước khi lô-gic nghiệp vụ (business logic / 비즈니스 로직) chạy, đây gần nhất với:

A. giao diện (interface / 인터페이스)/dữ liệu (data / 데이터) kiểm tra hợp lệ (validation / 검증)
B. CPU Scheduling
C. Deadlock khôi phục (recovery / 복구)
D. RAID Rebuild

## Q40

Checksum/băm (hash / 해시) dùng trong quá trình phân phối gói (package / 패키지) chủ yếu giúp phát hiện:

A. gói (package / 패키지) bị thay đổi/corrupt so với giá trị mong đợi
B. người dùng (user / 사용자) có quyền nghiệp vụ (business / 비즈니스) nào
C. CPU nào chạy tiến trình (process / 프로세스)
D. giao dịch (transaction / 트랜잭션) isolation mức (level / 수준)

---

# 제3과목 — 데이터베이스 구축 — cơ sở dữ liệu (database / 데이터베이스) Construction

## Q41

Một Super Key trở thành Candidate Key khi có thêm tính chất:

A. Minimality
B. Luôn có hai column
C. Luôn là foreign key
D. Luôn là numeric

## Q42

Relational Algebra thao tác (operation / 연산) dùng để chọn các row thỏa predicate là:

A. Projection
B. Selection
C. Division
D. Rename

## Q43

Thao tác (operation / 연산) dùng để lấy một số attribute/column trong relational algebra là:

A. Selection
B. Projection
C. Union
D. phép nối (join / 조인)

## Q44

Quan hệ (relation / 관계) có key `(StudentId, CourseId)` và `StudentName` chỉ phụ thuộc `StudentId`. Đây là:

A. Partial phụ thuộc (dependency / 의존성)
B. Transitive phụ thuộc (dependency / 의존성)
C. Multivalued phụ thuộc (dependency / 의존성)
D. phép nối (join / 조인) phụ thuộc (dependency / 의존성)

## Q45

`EmpId → DeptId` và `DeptId → DeptName`; `EmpId` là key. `DeptName` phụ thuộc vào key qua `DeptId`. Đây là:

A. Partial phụ thuộc (dependency / 의존성)
B. Transitive phụ thuộc (dependency / 의존성)
C. Trivial phụ thuộc (dependency / 의존성)
D. No phụ thuộc (dependency / 의존성)

## Q46

BCNF yêu cầu với mọi non-trivial FD `X → Y`:

A. X phải là superkey
B. Y phải là foreign key
C. X phải có đúng một attribute
D. Y không được là prime attribute

## Q47

Chỉ mục (index / 인덱스) cấu trúc (structure / 구조) nào tự nhiên phù hợp với equality + phạm vi (range / 범위) truy vấn (query / 쿼리) vì giữ thứ tự (ordering / 순서) theo key?

A. B+cây (tree / 트리)
B. Hash-only cấu trúc (structure / 구조)
C. ngăn xếp (stack / 스택)
D. FIFO hàng đợi (queue / 큐)

## Q48

Thêm quá nhiều chỉ mục (index / 인덱스) vào bảng (table / 테이블) write-heavy có sự đánh đổi (trade-off / 트레이드오프) phổ biến nào?

A. Insert/cập nhật (update / 업데이트)/Delete tốn thêm chi phí duy trì chỉ mục (index / 인덱스)
B. Mọi SELECT chắc chắn chậm hơn
C. giao dịch (transaction / 트랜잭션) không còn ACID
D. Foreign key tự biến mất

## Q49

Cơ sở dữ liệu (database / 데이터베이스) View gần nhất với:

A. Một virtual quan hệ (relation / 관계)/truy vấn (query / 쿼리) lớp trừu tượng (abstraction / 추상화) dựa trên underlying dữ liệu (data / 데이터)
B. Một vật lý (physical / 물리적) disk bắt buộc
C. Một CPU register
D. Một mạng (network / 네트워크) tuyến (route / 경로)

## Q50

Statement nào là DDL điển hình?

A. CREATE bảng (table / 테이블)
B. SELECT
C. lần ghi nhận (commit / 커밋)
D. GRANT

## Q51

Muốn lọc group có `SUM(amount) > 1000` sau `GROUP BY customer_id`, clause phù hợp là:

A. WHERE
B. HAVING
C. FROM
D. DISTINCT

## Q52

Trong `LEFT JOIN`, row bên trái không có match bên phải sẽ:

A. Bị loại luôn
B. Vẫn được giữ, columns bên phải thường là NULL
C. Tạo exception bắt buộc
D. Biến thành INNER phép nối (join / 조인)

## Q53

Ràng buộc (constraint / 제약조건) nào bảo đảm giá trị foreign key tham chiếu phù hợp tới key được phép ở quan hệ (relation / 관계) cha, theo referential integrity?

A. FOREIGN KEY
B. CHECKSUM
C. INDEX-only
D. VIEW-only

## Q54

ACID thuộc tính (property / 속성) nào bảo đảm một giao dịch (transaction / 트랜잭션) hoặc hoàn thành toàn bộ hoặc không để lại một phần thay đổi đã lần ghi nhận (commit / 커밋)?

A. Atomicity
B. Consistency
C. Isolation
D. Durability

## Q55

T1 đọc một row hai lần. Giữa hai lần, T2 cập nhật (update / 업데이트) row đó và lần ghi nhận (commit / 커밋), nên T1 thấy hai giá trị khác nhau. Đây là:

A. Dirty Read
B. Non-repeatable Read
C. Phantom Read
D. Deadlock

## Q56

T1 chạy cùng một predicate truy vấn (query / 쿼리) hai lần; lần hai xuất hiện thêm row mới do T2 insert và lần ghi nhận (commit / 커밋). Đây gần nhất với:

A. Phantom Read
B. Lost cập nhật (update / 업데이트)
C. ngăn xếp (stack / 스택) Overflow
D. Paging

## Q57

Trong precedence đồ thị (graph / 그래프) của một schedule, nếu có cycle thì schedule đó:

A. Chắc chắn conflict-serializable
B. Không conflict-serializable
C. Luôn read-only
D. Luôn deadlock

## Q58

Write-ahead logging — WAL — về ý tưởng yêu cầu điều gì trước khi dữ liệu (data / 데이터) page chứa thay đổi được ghi durable theo khôi phục (recovery / 복구) giao thức (protocol / 프로토콜)?

A. Relevant log bản ghi (record / 레코드) phải được ghi theo quy tắc (rule / 규칙) WAL trước
B. Xóa toàn bộ log
C. Tắt giao dịch (transaction / 트랜잭션)
D. Reboot máy chủ (server / 서버)

## Q59

Sau dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션), bước nào quan trọng để phát hiện mất hoặc biến đổi sai dữ liệu?

A. kiểm tra hợp lệ (validation / 검증)/Reconciliation
B. Chỉ đổi tên tệp (file / 파일)
C. Chỉ tăng CPU
D. Chỉ thêm CSS

## Q60

`COUNT(column)` khác `COUNT(*)` ở điểm quan trọng nào?

A. `COUNT(column)` không đếm NULL của column đó
B. `COUNT(*)` luôn trả 0
C. `COUNT(column)` chỉ dùng với primary key
D. Hai cái luôn giống nhau trong mọi truy vấn (query / 쿼리)

---

# 제4과목 — 프로그래밍 언어 활용 — Programming ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)

## Q61

Điểm khác biệt cơ bản thường gặp giữa tiến trình (process / 프로세스) và luồng thực thi (thread / 스레드) là:

A. luồng thực thi (thread / 스레드) trong cùng tiến trình (process / 프로세스) thường chia sẻ address không gian (space / 공간)/resources nhiều hơn
B. tiến trình (process / 프로세스) luôn chia sẻ toàn bộ bộ nhớ (memory / 메모리) với tiến trình (process / 프로세스) khác
C. luồng thực thi (thread / 스레드) không bao giờ được schedule
D. tiến trình (process / 프로세스) không có trạng thái (state / 상태)

## Q62

Semaphore khác mutex ở điểm khái quát nào?

A. Semaphore có thể biểu diễn nhiều permit bằng counter
B. Mutex luôn có counter 100
C. Semaphore chỉ dùng cho cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스)
D. Hai khái niệm hoàn toàn không liên quan synchronization

## Q63

Impose một thứ tự toàn cục khi acquire tài nguyên (resource / 자원) và buộc mọi tiến trình (process / 프로세스) tuân theo thứ tự đó nhắm phá Coffman điều kiện (condition / 조건) nào?

A. Mutual Exclusion
B. Hold and Wait
C. Circular Wait
D. No Preemption

## Q64

Ba tiến trình (process / 프로세스) cùng arrive thời gian (time / 시간) 0: P1=5, P2=3, P3=2. FCFS theo thứ tự P1→P2→P3. Average waiting thời gian (time / 시간) là:

A. 2.33
B. 4.33
C. 5.00
D. 7.67

## Q65

Cùng ba tiến trình (process / 프로세스) P1=5, P2=3, P3=2, tất cả arrive thời gian (time / 시간) 0. Non-preemptive SJF thứ tự (order / 순서) là:

A. P1→P2→P3
B. P3→P2→P1
C. P2→P1→P3
D. P3→P1→P2

## Q66

Trong Round Robin, giảm thời gian (time / 시간) quantum quá nhỏ thường dẫn tới sự đánh đổi (trade-off / 트레이드오프) nào?

A. Context-switch overhead tăng
B. Không còn preemption
C. Mọi tiến trình (process / 프로세스) chạy đến hết burst
D. Không cần ready hàng đợi (queue / 큐)

## Q67

Page Fault xảy ra khi:

A. tiến trình (process / 프로세스) tham chiếu page chưa hiện diện trong vật lý (physical / 물리적) bộ nhớ (memory / 메모리) và OS phải xử lý
B. CPU instruction luôn sai cú pháp (syntax / 문법)
C. DNS không resolve được
D. SQL không có GROUP BY

## Q68

LRU page replacement chọn victim theo:

A. Page ít được dùng gần đây nhất
B. Page có địa chỉ nhỏ nhất bắt buộc
C. Page vào frame đầu tiên bất kể usage
D. Page random theo chuẩn

## Q69

Thrashing gần nhất với tình trạng:

A. Hệ thống dành quá nhiều thời gian paging do working set không phù hợp bộ nhớ (memory / 메모리)
B. CPU không có instruction set
C. cơ sở dữ liệu (database / 데이터베이스) không có primary key
D. mạng (network / 네트워크) chỉ dùng UDP

## Q70

Trong mô hình TCP/IP/OSI, TCP thuộc tầng (layer / 계층) gần nhất với:

A. vận chuyển (transport / 전송)
B. mạng (network / 네트워크)
C. dữ liệu (data / 데이터) Link
D. vật lý (physical / 물리적)

## Q71

So với UDP, TCP cung cấp rõ nhất:

A. Connection-oriented reliable ordered byte stream
B. Broadcast bắt buộc
C. Không có cổng (port / 포트)
D. Không có congestion điều khiển (control / 제어) concept

## Q72

Một subnet IPv4 `/27` có bao nhiêu địa chỉ usable theo cách tính truyền thống mạng (network / 네트워크)/broadcast?

A. 14
B. 30
C. 32
D. 62

## Q73

Routing bảng (table / 테이블) có các tuyến (route / 경로) `/8`, `/16`, `/24` cùng match destination. Router theo longest-prefix match sẽ chọn:

A. /8
B. /16
C. /24
D. Chọn random

## Q74

DNS chủ yếu dùng để:

A. Phân giải tên miền và các bản ghi (record / 레코드) liên quan sang thông tin như IP theo bản ghi (record / 레코드) kiểu (type / 타입)
B. Mã hóa disk
C. Lập lịch CPU
D. Normalize cơ sở dữ liệu (database / 데이터베이스)

## Q75

ARP trong IPv4 LAN truyền thống dùng để:

A. Ánh xạ IPv4 address tới link-layer MAC address trong cục bộ (local / 로컬) mạng (network / 네트워크) ngữ cảnh (context / 맥락)
B. Tìm SQL chỉ mục (index / 인덱스)
C. Tính đường găng (critical path / 임계 경로)
D. băm (hash / 해시) password

## Q76

C mã (code / 코드):

```c
int a[] = {10,20,30,40};
int *p = a + 1;
printf("%d", *(p + 2));
```

Đầu ra (output / 출력) là:

A. 10
B. 20
C. 30
D. 40

## Q77

C mã (code / 코드):

```c
int x = 3;
int y = x++;
```

Ngay sau đó:

A. x=3, y=4
B. x=4, y=3
C. x=4, y=4
D. x=3, y=3

## Q78

Java:

```java
A x = new B();
x.f();
```

Nếu `B` override instance phương thức (method / 메서드) `f()` của `A`, phương thức (method / 메서드) body nào thường được gọi qua động (dynamic / 동적) dispatch?

A. Luôn A
B. B
C. Không phương thức (method / 메서드) nào
D. Compile lỗi (error / 오류) chỉ vì tham chiếu (reference / 참조) kiểu (type / 타입) A

## Q79

Trong Java, overloading thường được phân biệt bằng:

A. Parameter danh sách (list / 목록)/signature khác phù hợp quy tắc (rule / 규칙) ngôn ngữ
B. Chỉ khác return kiểu (type / 타입)
C. Chỉ khác tên lớp (class / 클래스)
D. Chỉ khác comment

## Q80

Python:

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

Đầu ra (output / 출력) là:

A. `[1, 2]`
B. `[1, 2, 3]`
C. `[3]`
D. lỗi (error / 오류) bắt buộc

---

# 제5과목 — 정보시스템 구축 관리 — thông tin (information / 정보) hệ thống (system / 시스템) Construction Management

## Q81

Đặc điểm nào gần nhất với Waterfall mô hình (model / 모델) truyền thống?

A. Các phase theo trình tự tương đối rõ, thay đổi (change / 변경) muộn thường tốn kém
B. Không có yêu cầu (requirement / 요구사항)
C. Không có kiểm thử (test / 테스트)
D. Luôn deploy mỗi ngày

## Q82

PERT expected thời gian (time / 시간) với O=4, M=7, P=16 là:

A. 7
B. 8
C. 9
D. 16

## Q83

Dự án (project / 프로젝트) có đường dẫn (path / 경로) A tổng 12 ngày và đường dẫn (path / 경로) B tổng 9 ngày, không có ràng buộc (constraint / 제약조건) khác. đường găng (critical path / 임계 경로) là:

A. đường dẫn (path / 경로) B
B. đường dẫn (path / 경로) A
C. Cả hai luôn trọng yếu (critical / 중요)
D. Không đường dẫn (path / 경로) nào

## Q84

4 disk × 2 TB chạy RAID 5. Usable sức chứa (capacity / 용량) theo mô hình parity một disk tương đương là:

A. 2 TB
B. 4 TB
C. 6 TB
D. 8 TB

## Q85

RAID 1 chủ yếu dùng:

A. Mirroring
B. Striping không redundancy
C. phân tán (distributed / 분산) dual parity
D. DNS replication

## Q86

Nghiệp vụ (business / 비즈니스) nói “dịch vụ (service / 서비스) phải phục hồi trong 30 phút”. Đây mô tả:

A. RPO
B. RTO
C. MTU
D. TTL DNS

## Q87

Nghiệp vụ (business / 비즈니스) nói “chấp nhận mất tối đa 5 phút dữ liệu”. Đây mô tả:

A. RTO
B. RPO
C. CPU quantum
D. Fan-out

## Q88

Phát biểu nào đúng nhất?

A. RAID hoàn toàn thay thế backup
B. Backup, replication và RAID bảo vệ các thất bại (failure / 실패) modes khác nhau
C. Có RAID thì ransomware không thể phá dữ liệu (data / 데이터)
D. Có backup thì không cần restore kiểm thử (test / 테스트)

## Q89

Trong cloud dịch vụ (service / 서비스) mô hình (model / 모델), IaaS cung cấp gần nhất:

A. Compute/mạng (network / 네트워크)/lưu trữ (storage / 저장소) hạ tầng (infrastructure / 인프라) mà customer quản lý nhiều phần software ngăn xếp (stack / 스택) hơn SaaS
B. Chỉ một ứng dụng hoàn chỉnh không quản lý OS nào
C. Chỉ mã nguồn (source code / 소스 코드) repository
D. Chỉ password manager

## Q90

Bộ chứa (container / 컨테이너) khác full VM điển hình ở điểm:

A. bộ chứa (container / 컨테이너) thường chia sẻ host kernel thay vì mỗi instance có guest OS/kernel riêng như VM truyền thống
B. bộ chứa (container / 컨테이너) không cần isolation
C. VM không thể chạy ứng dụng (application / 애플리케이션)
D. bộ chứa (container / 컨테이너) luôn mạnh hơn VM về bảo mật (security / 보안)

## Q91

Firewall gần nhất với nhiệm vụ:

A. Kiểm soát mạng (network / 네트워크) traffic theo chính sách (policy / 정책)/quy tắc (rule / 규칙)
B. Normalize quan hệ (relation / 관계)
C. Compile Java
D. Tính PERT

## Q92

IDS và IPS khác nhau khái quát ở điểm:

A. IDS thiên về detection/alert; IPS có thể nằm inline để khối (block / 블록)/prevent
B. IDS là cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스); IPS là SQL clause
C. IPS không liên quan mạng (network / 네트워크)/bảo mật (security / 보안)
D. Hai cái luôn giống hệt triển khai (deployment / 배포)

## Q93

Authentication và Authorization khác nhau ở đâu?

A. Authentication xác minh định danh (identity / 식별자); Authorization quyết định quyền hành động
B. Authentication quyết định quyền; Authorization chỉ băm (hash / 해시) password
C. Hai khái niệm đồng nghĩa hoàn toàn
D. Authorization chỉ dùng cho mạng (network / 네트워크) routing

## Q94

Cryptographic băm (hash / 해시) hàm (function / 함수) chủ yếu tạo:

A. Fixed-size digest từ đầu vào (input / 입력), dùng cho integrity-related purposes tùy giao thức (protocol / 프로토콜)
B. Reversible ciphertext bằng cùng key bắt buộc
C. IP tuyến (route / 경로)
D. CPU schedule

## Q95

Digital signature chủ yếu hỗ trợ combination nào?

A. Authenticity/integrity và non-repudiation theo scheme/ngữ cảnh (context / 맥락) phù hợp
B. Compression
C. cơ sở dữ liệu (database / 데이터베이스) normalization
D. tải (load / 로드) balancing

## Q96

Mitigation trực tiếp nhất cho SQL Injection trong ứng dụng (application / 애플리케이션) mã (code / 코드) là:

A. Parameterized truy vấn (query / 쿼리) / Prepared Statement
B. Chỉ đổi cổng (port / 포트) cơ sở dữ liệu (database / 데이터베이스)
C. Chỉ nén phản hồi (response / 응답)
D. Chỉ thêm CSS kiểm tra hợp lệ (validation / 검증) phía máy khách (client / 클라이언트)

## Q97

Mitigation quan trọng cho Stored/Reflected XSS khi kết xuất (render / 렌더링) untrusted dữ liệu (data / 데이터) là:

A. Context-appropriate đầu ra (output / 출력) encoding/escaping
B. RAID 1
C. CPU affinity
D. B+cây (tree / 트리) chỉ mục (index / 인덱스)

## Q98

Principle of Least Privilege — 최소 권한 원칙 — nghĩa là:

A. Cấp tối thiểu quyền cần thiết cho tác vụ (task / 작업), trong phạm vi/thời gian phù hợp
B. Mọi người dùng (user / 사용자) đều admin
C. Tắt logging
D. Không cần authorization

## Q99

Cấu hình (configuration / 구성) Management — 형상관리 — rộng hơn phiên bản (version / 버전) điều khiển (control / 제어) vì nó còn bao gồm:

A. Identification/baseline/thay đổi (change / 변경)/status/kiểm tra (audit / 감사) của cấu hình (configuration / 구성) items và release-related điều khiển (control / 제어)
B. Chỉ cú pháp (syntax / 문법) highlighting
C. Chỉ CPU scheduling
D. Chỉ DNS bộ nhớ đệm (cache / 캐시)

## Q100

Rủi ro (risk / 위험) có xác suất (probability / 확률) thấp nhưng impact cực lớn. Cách đánh giá đúng nhất là:

A. Bỏ qua vì xác suất (probability / 확률) thấp
B. Xem xét cả likelihood và impact, cùng exposure/ngữ cảnh (context / 맥락) và mitigation
C. Chỉ nhìn impact, không cần xác suất (probability / 확률)
D. Chỉ nhìn số lượng nhà phát triển (developer / 개발자)

---

# Answer Key + Rationales

## Môn 1

**Q1 — C.** hiệu năng (performance / 성능) threshold là chất lượng (quality / 품질) ràng buộc (constraint / 제약조건), không phải nghiệp vụ (business / 비즈니스) hàm (function / 함수) chính.
**Q2 — B.** kiểm tra hợp lệ (validation / 검증) hỏi sản phẩm/spec có đúng nhu cầu thực không; xác minh (verification / 확인) hỏi có xây đúng spec không.
**Q3 — B.** dữ liệu (data / 데이터) Store biểu diễn nơi dữ liệu được giữ trong DFD.
**Q4 — A.** chuỗi (sequence / 시퀀스) Diagram tập trung thứ tự (order / 순서) của messages theo thời gian.
**Q5 — B.** Composition biểu diễn whole-part quyền sở hữu (ownership / 소유권)/vòng đời (lifecycle / 생명주기) mạnh.
**Q6 — C.** mô-đun (module / 모듈) independence thường hướng tới high cohesion, low coupling.
**Q7 — D.** Chỉ truyền đúng dữ liệu cần dùng qua parameter là dữ liệu (data / 데이터) Coupling.
**Q8 — A.** Truyền whole bản ghi (record / 레코드)/đối tượng (object / 객체) nhưng chỉ dùng một phần là Stamp Coupling.
**Q9 — A.** SRP = Single Responsibility Principle.
**Q10 — B.** High-level dịch vụ (service / 서비스) phụ thuộc lớp trừu tượng (abstraction / 추상화) `PaymentGateway`, phù hợp DIP.
**Q11 — A.** chiến lược (strategy / 전략) encapsulates interchangeable algorithms/policies.
**Q12 — B.** Adapter chuyển giao diện (interface / 인터페이스) hiện có sang giao diện (interface / 인터페이스) máy khách (client / 클라이언트) mong đợi.
**Q13 — A.** Facade cung cấp mặt tiền đơn giản cho subsystem phức tạp.
**Q14 — B.** Observer phù hợp one-to-many notification.
**Q15 — A.** Wireframe tập trung bố cục (layout / 레이아웃)/cấu trúc (structure / 구조) hơn visual polish hoặc tương tác (interaction / 상호작용) hoàn chỉnh.
**Q16 — B.** Sprint Backlog chứa selected công việc (work / 작업) và plan để đạt Sprint Goal.
**Q17 — A.** Pair Programming là practice tiêu biểu của XP.
**Q18 — A.** Idempotency giúp same logical yêu cầu (request / 요청) không lặp side tác động (effect / 효과) ngoài ý muốn.
**Q19 — B.** Số liên kết (connection / 연결)/phụ thuộc (dependency / 의존성) tăng nhanh khiến point-to-point khó maintain.
**Q20 — B.** triển khai (deployment / 배포) Diagram biểu diễn ánh xạ (mapping / 매핑) sản phẩm tạo ra (artifact / 산출물)/thành phần (component / 컴포넌트) lên triển khai (deployment / 배포) nodes.

**Môn 1 score:** `___ / 20` → `___ / 100`.

---

## Môn 2

**Q21 — B.** ngăn xếp (stack / 스택) là LIFO.
**Q22 — B.** hàng đợi (queue / 큐) cơ bản là FIFO.
**Q23 — B.** Inorder traversal của BST distinct keys cho sorted thứ tự (order / 순서).
**Q24 — A.** BFS khám phá theo tầng (layer / 계층) nên cho shortest đường dẫn (path / 경로) theo số edge trong unweighted đồ thị (graph / 그래프).
**Q25 — D.** Quick Sort worst trường hợp (case / 사례) điển hình O(n²).
**Q26 — B.** Merge Sort worst-case O(n log n).
**Q27 — A.** tuyến tính (linear / 선형) probing dễ tạo primary clustering.
**Q28 — B.** Top-down dùng stub thay mô-đun (module / 모듈) con chưa có.
**Q29 — A.** Bottom-up dùng driver mô phỏng caller phía trên.
**Q30 — C.** ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석) là black-box technique.
**Q31 — B.** Branch Coverage đo các quyết định (decision / 결정) kết quả (outcome / 결과)/branches.
**Q32 — C.** `12 - 10 + 2 = 4`.
**Q33 — A.** Regression kiểm thử (test / 테스트) kiểm tra thay đổi không phá hành vi (behavior / 동작) trước đó.
**Q34 — B.** Beta thường do bên ngoài (external / 외부) users trong môi trường gần thực tế hơn alpha.
**Q35 — A.** Baseline là cấu hình/mốc đã được formally established và controlled.
**Q36 — A.** phiên bản (version / 버전) điều khiển (control / 제어) quản lý lịch sử, branch/phiên bản (version / 버전) và collaboration trên artifacts.
**Q37 — A.** Packaging chuẩn bị sản phẩm tạo ra (artifact / 산출물)/phụ thuộc (dependency / 의존성)/siêu dữ liệu (metadata / 메타데이터)/manual cần cho phân phối (distribution / 분포)/install.
**Q38 — A.** thông lượng (throughput / 처리량) = công việc (work / 작업) completed per thời gian (time / 시간) đơn vị (unit / 단위).
**Q39 — A.** Kiểm tra lược đồ (schema / 스키마)/kiểu (type / 타입)/required fields là giao diện (interface / 인터페이스)/dữ liệu (data / 데이터) kiểm tra hợp lệ (validation / 검증).
**Q40 — A.** Checksum/băm (hash / 해시) giúp phát hiện gói (package / 패키지) khác expected content; authentication/authorization là vấn đề khác.

**Môn 2 score:** `___ / 20` → `___ / 100`.

---

## Môn 3

**Q41 — A.** Candidate key = minimal superkey.
**Q42 — B.** Selection chọn rows theo predicate.
**Q43 — B.** Projection chọn attributes/columns.
**Q44 — A.** Non-key attribute phụ thuộc một phần composite key là partial phụ thuộc (dependency / 의존성).
**Q45 — B.** Key → non-key → non-key tạo transitive phụ thuộc (dependency / 의존성).
**Q46 — A.** BCNF yêu cầu determinant của mọi non-trivial FD là superkey.
**Q47 — A.** B+cây (tree / 트리) giữ thứ tự (ordering / 순서) và hỗ trợ phạm vi (range / 범위) scan tự nhiên.
**Q48 — A.** chỉ mục (index / 인덱스) phải được cập nhật khi writes thay đổi indexed keys/rows.
**Q49 — A.** View là truy vấn (query / 쿼리) lớp trừu tượng (abstraction / 추상화)/virtual quan hệ (relation / 관계), trừ materialized-view variant có lưu trữ (storage / 저장소) riêng.
**Q50 — A.** `CREATE TABLE` là DDL. `SELECT` là truy vấn (query / 쿼리)/DML-style, `COMMIT` TCL, `GRANT` DCL theo phân loại truyền thống.
**Q51 — B.** HAVING lọc group sau aggregate.
**Q52 — B.** LEFT phép nối (join / 조인) giữ rows phía trái và fill NULL cho unmatched right side.
**Q53 — A.** FOREIGN KEY enforce referential ràng buộc (constraint / 제약조건) theo DBMS quy tắc (rule / 규칙).
**Q54 — A.** Atomicity = all-or-nothing giao dịch (transaction / 트랜잭션) tác động (effect / 효과).
**Q55 — B.** Cùng row đọc hai lần ra giá trị khác do committed cập nhật (update / 업데이트) là non-repeatable read.
**Q56 — A.** Predicate kết quả (result / 결과) có thêm/mất row do insert/delete concurrent là phantom.
**Q57 — B.** Cycle trong precedence đồ thị (graph / 그래프) nghĩa không conflict-serializable.
**Q58 — A.** WAL yêu cầu log bản ghi (record / 레코드) tương ứng được forced theo quy tắc (rule / 규칙) trước dữ liệu (data / 데이터) page cần thiết cho khôi phục (recovery / 복구).
**Q59 — A.** di chuyển (migration / 마이그레이션) phải có kiểm tra hợp lệ (validation / 검증)/reconciliation về count, ràng buộc (constraint / 제약조건), sampled/full checks tùy criticality.
**Q60 — A.** `COUNT(column)` bỏ qua NULL; `COUNT(*)` đếm rows.

**Môn 3 score:** `___ / 20` → `___ / 100`.

---

## Môn 4

**Q61 — A.** Threads cùng tiến trình (process / 프로세스) thường share address không gian (space / 공간)/resources nhiều hơn independent processes.
**Q62 — A.** Semaphore có counter/permits; mutex thường mô hình quyền sở hữu (ownership / 소유권)/exclusion một trọng yếu (critical / 중요) section.
**Q63 — C.** tài nguyên (resource / 자원) thứ tự (ordering / 순서) phá circular wait.
**Q64 — B.** Waiting: 0,5,8 → average `13/3 ≈ 4.33`.
**Q65 — B.** SJF chọn burst ngắn: P3(2) → P2(3) → P1(5).
**Q66 — A.** Quantum quá nhỏ tăng scheduling/context-switch overhead.
**Q67 — A.** Page fault khi referenced page không resident và OS phải bring/resolve ánh xạ (mapping / 매핑).
**Q68 — A.** LRU thay page least recently used.
**Q69 — A.** Thrashing = paging activity quá mức, useful công việc (work / 작업) giảm mạnh.
**Q70 — A.** TCP là transport-layer giao thức (protocol / 프로토콜).
**Q71 — A.** TCP cung cấp connection-oriented reliable ordered byte stream.
**Q72 — B.** `/27` còn 5 host bits → 32 addresses, usable truyền thống 30.
**Q73 — C.** Longest-prefix match chọn tuyến (route / 경로) cụ thể nhất `/24`.
**Q74 — A.** DNS phân giải names/records, không phải routing/scheduling.
**Q75 — A.** ARP dùng trong IPv4 local-link address resolution.
**Q76 — D.** `p=a+1` trỏ 20; `p+2` trỏ chỉ mục (index / 인덱스) 3 = 40.
**Q77 — B.** Post-increment trả old giá trị (value / 값) cho assignment rồi tăng x: y=3, x=4.
**Q78 — B.** Overridden instance phương thức (method / 메서드) dispatch theo thời gian chạy (runtime / 런타임) đối tượng (object / 객체) B.
**Q79 — A.** Overloading dựa trên khác parameter signature; chỉ khác return kiểu (type / 타입) không đủ.
**Q80 — B.** `a` và `b` alias cùng mutable danh sách (list / 목록), append qua b làm a thấy `[1,2,3]`.

**Môn 4 score:** `___ / 20` → `___ / 100`.

---

## Môn 5

**Q81 — A.** Waterfall truyền thống có phase thứ tự (ordering / 순서) rõ; thay đổi (change / 변경) late thường có rework chi phí (cost / 비용) cao.
**Q82 — B.** `(4 + 4×7 + 16)/6 = 48/6 = 8`.
**Q83 — B.** đường dẫn (path / 경로) dài 12 quyết định duration trong mạng (network / 네트워크) đơn giản này.
**Q84 — C.** RAID5 usable `(4-1)×2 = 6 TB`.
**Q85 — A.** RAID1 là mirroring.
**Q86 — B.** RTO = mục tiêu (objective / 목표) cho thời gian phục hồi dịch vụ (service / 서비스).
**Q87 — B.** RPO = mục tiêu (objective / 목표) cho mức dữ liệu (data / 데이터) mất mát (loss / 손실) theo thời gian.
**Q88 — B.** RAID, replication và backup giải quyết thất bại (failure / 실패) modes khác nhau và không thay thế hoàn toàn nhau.
**Q89 — A.** IaaS cung cấp hạ tầng (infrastructure / 인프라) primitives; customer kiểm soát nhiều tầng (layer / 계층) phía trên hơn SaaS.
**Q90 — A.** Containers thường share host kernel; VMs truyền thống có guest OS/kernel riêng.
**Q91 — A.** Firewall enforce mạng (network / 네트워크) traffic chính sách (policy / 정책).
**Q92 — A.** IDS thiên detection/alert; IPS thường inline/prevent/khối (block / 블록) tùy triển khai (deployment / 배포).
**Q93 — A.** Authentication = who are you; Authorization = what may you do.
**Q94 — A.** băm (hash / 해시) tạo digest fixed-size; không phải reversible encryption.
**Q95 — A.** Digital signatures hỗ trợ integrity/authenticity và non-repudiation các giả định (assumptions / 가정들) theo scheme/ngữ cảnh (context / 맥락).
**Q96 — A.** Parameterized truy vấn (query / 쿼리) tách mã (code / 코드)/SQL cấu trúc (structure / 구조) khỏi untrusted values, mitigation cốt lõi cho SQL injection.
**Q97 — A.** đầu ra (output / 출력) encoding theo ngữ cảnh (context / 맥락) là defense cốt lõi khi kết xuất (render / 렌더링) untrusted content; CSP có thể là tầng (layer / 계층) bổ sung.
**Q98 — A.** Least privilege cấp đúng mức quyền cần thiết, không mặc định admin.
**Q99 — A.** cấu hình (configuration / 구성) Management bao gồm identification, baseline, thay đổi (change / 변경)/status accounting, kiểm tra (audit / 감사)/bản phát hành (release / 릴리스) điều khiển (control / 제어); VCS chỉ là một phần tooling/tiến trình (process / 프로세스).
**Q100 — B.** rủi ro (risk / 위험) assessment phải xét likelihood + impact + ngữ cảnh (context / 맥락)/exposure/controls; low xác suất (probability / 확률) không tự động nghĩa bỏ qua.

**Môn 5 score:** `___ / 20` → `___ / 100`.

---

# Score Sheet

| Môn | Correct / 20 | Score / 100 | ≥ 40? |
|---|---:|---:|---|
| 소프트웨어 설계 | ___ | ___ | ___ |
| 소프트웨어 개발 | ___ | ___ | ___ |
| 데이터베이스 구축 | ___ | ___ | ___ |
| 프로그래밍 언어 활용 | ___ | ___ | ___ |
| 정보시스템 구축 관리 | ___ | ___ | ___ |

```text
Total correct = _____ / 100
Average score = _____ / 100
```

Trong mô hình này, vì năm môn có cùng 20 câu và cùng weight, `60/100` total correct tương ứng average 60, **nhưng vẫn phải đồng thời đạt tối thiểu 8/20 ở từng môn**.

---

# Lỗi (error / 오류) kiểm tra (audit / 감사)

Với mỗi câu sai, ghi một mã duy nhất đầu tiên:

```text
COV = coverage hole
CON = confusion pair
PRO = procedural error
TERM = Korean/English term recognition
READ = careless reading
```

Sau đó ghi concept gốc phải sửa. Ví dụ:

```text
Q55 — CON — non-repeatable read vs phantom read
Q64 — PRO — FCFS waiting-time timeline
Q72 — PRO — /27 host-bit calculation
Q96 — COV — parameterized query
```

Không học lại nguyên 100 câu. Học lại **cơ chế tạo ra lỗi**.

---

# Definition of Done

Mock này chưa “xong” khi chỉ đạt 60 câu đúng một lần. Xong khi:

1. không môn nào dưới 8/20;
2. mọi câu procedural sai đều có thể làm lại bằng bước trung gian;
3. mọi confusion pair sai đều giải thích được ranh giới bằng lời của mình;
4. mọi term-recognition lỗi (error / 오류) đều nhận ra cả Korean + English concept;
5. khi làm lại sau một khoảng cách, không còn phụ thuộc vào việc nhớ vị trí đáp án A/B/C/D.
