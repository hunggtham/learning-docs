# 정보처리기사 필기 2026 — Full Mock #2: Hard chế độ (mode / 모드) 100

> **100 câu tự viết mới, 20 câu/môn.** Mock #2 cố ý dùng wording gần nhau, scenario nhiều tầng (layer / 계층) và distractor “đúng nhưng không đúng nhất”. Không mở answer key trước khi hoàn thành toàn bộ 100 câu.
>
> Chấm như đề thật: mỗi môn 20 câu; mô phỏng 과락 nếu dưới 8/20 ở bất kỳ môn nào. Sau khi chấm, dùng `14-error-remediation-map.md` thay vì chỉ ghi đáp án.

---

# 제1과목 — 소프트웨어 설계

## Q1
Hai yêu cầu (requirement / 요구사항) sau cùng tồn tại:

```text
R1: User session hết hạn sau 30 phút không hoạt động.
R2: User session phải tồn tại tối thiểu 8 giờ bất kể hoạt động.
```

Vấn đề chính là:

A. Ambiguity
B. Inconsistency
C. Incompleteness
D. Untraceability

## Q2
yêu cầu (requirement / 요구사항) “tìm kiếm (search / 검색) phải nhanh” có vấn đề chính nào trước tiên?

A. Không functional
B. Không measurable/verifiable đủ rõ
C. Không thể implement bằng cơ sở dữ liệu (database / 데이터베이스)
D. Không thể dấu vết (trace / 추적)

## Q3
Context-level DFD có đầu vào (input / 입력) `Order` và đầu ra (output / 출력) `Receipt`. Khi phân rã tiến trình (process / 프로세스), mức (level / 수준) con tạo thêm bên ngoài (external / 외부) đầu ra (output / 출력) `CreditScore` nhưng mức (level / 수준) trên không có. Khái niệm cần kiểm tra là:

A. Encapsulation
B. DFD balancing
C. Polymorphism
D. Fan-in

## Q4
Muốn biểu diễn một đối tượng (object / 객체) `Order` chuyển `CREATED → PAID → SHIPPED` theo sự kiện (event / 이벤트). Diagram phù hợp nhất:

A. Activity
B. máy trạng thái (state machine / 상태 머신)
C. triển khai (deployment / 배포)
D. thành phần (component / 컴포넌트)

## Q5
Use trường hợp (case / 사례) `Checkout` luôn gọi `Validate Cart`; `Apply Coupon` chỉ xảy ra khi có coupon. Quan hệ phù hợp nhất:

A. Checkout extend Validate Cart; Apply Coupon include Checkout
B. Checkout include Validate Cart; Apply Coupon extend Checkout
C. Cả hai đều generalization
D. Cả hai đều composition

## Q6
Một lớp (class / 클래스) `ReportService` vừa truy vấn (query / 쿼리) DB, format PDF, gửi email, ghi kiểm tra (audit / 감사) và upload S3. Principle bị đe dọa trực tiếp nhất:

A. LSP
B. SRP
C. ISP
D. OCP

## Q7
Một giao diện (interface / 인터페이스) có 25 phương thức (method / 메서드); máy khách (client / 클라이언트) A chỉ cần 2 phương thức (method / 메서드) nhưng buộc implement/depend toàn bộ. Principle phù hợp nhất:

A. ISP
B. LSP
C. SRP
D. Singleton

## Q8
Subclass `Square` kế thừa `Rectangle`, nhưng setter width/height của cơ sở (base / 기반) lớp (class / 클래스) làm mã (code / 코드) máy khách (client / 클라이언트) phá giả định (assumption / 가정) khi dùng Square. Principle được nhắc tới rõ nhất:

A. DIP
B. LSP
C. ISP
D. SRP

## Q9
mô-đun (module / 모듈) A truyền cả `CustomerRecord` cho B, trong khi B chỉ dùng `customerId`. Đây là:

A. dữ liệu (data / 데이터) coupling
B. Stamp coupling
C. điều khiển (control / 제어) coupling
D. dùng chung (common / 공통) coupling

## Q10
Hai mô-đun (module / 모듈) cùng phụ thuộc vào một định dạng tệp (file / 파일) bên ngoài cố định. Đây gần nhất với:

A. bên ngoài (external / 외부) coupling
B. dùng chung (common / 공통) coupling
C. Content coupling
D. dữ liệu (data / 데이터) coupling

## Q11
mẫu (pattern / 패턴) nào phù hợp nhất khi hành vi (behavior / 동작) thay đổi theo **nội bộ (internal / 내부) vòng đời (lifecycle / 생명주기) trạng thái (state / 상태)** của đối tượng (object / 객체)?

A. chiến lược (strategy / 전략)
B. trạng thái (state / 상태)
C. Adapter
D. Facade

## Q12
mẫu (pattern / 패턴) nào phù hợp khi cần thay đổi thuật toán (algorithm / 알고리즘) tính phí theo thị trường (market / 시장)/channel mà caller dùng cùng giao diện (interface / 인터페이스)?

A. trạng thái (state / 상태)
B. chiến lược (strategy / 전략)
C. Observer
D. Composite

## Q13
Một subsystem có 8 dịch vụ (service / 서비스) phức tạp; máy khách (client / 클라이언트) chỉ cần một entry điểm (point / 지점) đơn giản. mẫu (pattern / 패턴):

A. Adapter
B. Facade
C. Decorator
D. Prototype

## Q14
Một wrapper thêm logging và caching quanh dịch vụ (service / 서비스) mà giữ cùng giao diện (interface / 인터페이스). mẫu (pattern / 패턴) gần nhất:

A. Decorator
B. Builder
C. trạng thái (state / 상태)
D. Memento

## Q15
Diagram nào trả lời tốt nhất câu hỏi “sản phẩm tạo ra (artifact / 산출물) nào deploy trên nút (node / 노드) nào?”

A. thành phần (component / 컴포넌트)
B. triển khai (deployment / 배포)
C. lớp (class / 클래스)
D. chuỗi (sequence / 시퀀스)

## Q16
Traceability giúp trực tiếp nhất cho:

A. Tăng CPU clock
B. Impact phân tích (analysis / 분석) và kiểm coverage từ yêu cầu (requirement / 요구사항) tới kiểm thử (test / 테스트)
C. Chọn subnet mask
D. Mã hóa tệp (file / 파일)

## Q17
Một payment yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) sau khi máy chủ (server / 서버) đã lần ghi nhận (commit / 커밋). máy khách (client / 클라이언트) thử lại (retry / 재시도) cùng logical yêu cầu (request / 요청). thuộc tính (property / 속성) cần thiết nhất ở giao diện (interface / 인터페이스)/nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) là:

A. Inheritance
B. Idempotency
C. Compression
D. Aggregation

## Q18
Thay trường dữ liệu (field / 필드) API từ optional thành required mà không versioning có rủi ro chính:

A. vật lý (physical / 물리적) fragmentation
B. Backward tính tương thích (compatibility / 호환성) break
C. CPU starvation
D. Deadlock

## Q19
Point-to-point tích hợp (integration / 통합) giữa N các hệ thống (systems / 시스템들) tăng vấn đề gì khi N lớn?

A. phụ thuộc (dependency / 의존성)/liên kết (connection / 연결) độ phức tạp (complexity / 복잡도)
B. Không thể dùng HTTP
C. Không thể thử lại (retry / 재시도)
D. Không có dữ liệu (data / 데이터) format

## Q20
Một kiến trúc (architecture / 아키텍처) style chia xử lý thành nhiều stage độc lập, đầu ra (output / 출력) stage trước thành đầu vào (input / 입력) stage sau. Gần nhất:

A. Repository
B. Pipe-and-Filter
C. MVC
D. Client-Server

---

# 제2과목 — 소프트웨어 개발

## Q21
ngăn xếp (stack / 스택) là:

A. hiện thực (implementation / 구현) duy nhất bằng array
B. ADT có thể implement bằng nhiều cấu trúc (structure / 구조)
C. Luôn FIFO
D. Luôn cây (tree / 트리)

## Q22
Một max-heap bảo đảm điều gì?

A. Mọi nút (node / 노드) trái nhỏ hơn mọi nút (node / 노드) phải
B. Parent không nhỏ hơn child theo vùng nhớ động (heap / 힙) thuộc tính (property / 속성)
C. Inorder traversal luôn sorted
D. tìm kiếm (search / 검색) arbitrary key luôn O(log n)

## Q23
đồ thị (graph / 그래프) có 1 triệu vertices nhưng chỉ 2 triệu edges. biểu diễn (representation / 표현) thường tiết kiệm bộ nhớ (memory / 메모리) hơn:

A. Adjacency ma trận (matrix / 행렬)
B. Adjacency danh sách (list / 목록)
C. Full bảng (table / 테이블) V×V bắt buộc
D. ngăn xếp (stack / 스택)

## Q24
Muốn shortest đường dẫn (path / 경로) theo số cạnh trong đồ thị (graph / 그래프) unweighted:

A. DFS
B. BFS
C. Prim
D. Kruskal

## Q25
Mục tiêu của Minimum Spanning cây (tree / 트리) là:

A. Tối thiểu distance từ nguồn (source / 소스) tới mọi nút (node / 노드)
B. Nối tất cả vertices với tổng edge weight nhỏ nhất mà không cycle
C. Tìm strongly connected components
D. Sort vertices

## Q26
Sort ổn định nghĩa là:

A. Không dùng bộ nhớ (memory / 메모리) phụ
B. Luôn O(n log n)
C. Giữ relative thứ tự (order / 순서) của records có key bằng nhau
D. Không bao giờ swap

## Q27
băm (hash / 해시) collision là:

A. Cùng logical key xuất hiện hai lần
B. Hai key khác nhau map tới cùng bucket/chỉ mục (index / 인덱스)
C. bảng (table / 테이블) đầy hoàn toàn
D. băm (hash / 해시) hàm (function / 함수) trả negative

## Q28
Trong tuyến tính (linear / 선형) probing, xóa một item bằng cách đặt slot thành “never used” có thể phá:

A. Probe chuỗi (chain / 사슬)
B. cây (tree / 트리) balance
C. ngăn xếp (stack / 스택) pointer
D. TCP chuỗi (sequence / 시퀀스)

## Q29
rà soát (review / 검토) mã nguồn (source code / 소스 코드) mà không execute là:

A. động (dynamic / 동적) testing
B. Static testing
C. tải (load / 로드) testing
D. Beta testing

## Q30
Human hiểu sai yêu cầu (requirement / 요구사항) và viết sai điều kiện (condition / 조건). Sai điều kiện (condition / 조건) trong mã (code / 코드) là:

A. thất bại (failure / 실패) observable
B. Defect/Fault
C. mạng (network / 네트워크) độ trễ (latency / 지연 시간)
D. khôi phục (recovery / 복구) điểm (point / 지점)

## Q31
Một bộ kiểm thử (test suite / 테스트 스위트) đạt 100% statement coverage. Kết luận an toàn nhất:

A. Mọi branch đã chạy cả true và false
B. Mọi đường dẫn (path / 경로) đã kiểm thử (test / 테스트)
C. Không thể suy ra branch/đường dẫn (path / 경로) coverage đầy đủ
D. Không còn bug

## Q32
Black-box technique nào tập trung ngay cạnh giới hạn hợp lệ/không hợp lệ?

A. Branch Coverage
B. ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석)
C. đường dẫn (path / 경로) Coverage
D. Statement Coverage

## Q33
Top-down tích hợp (integration / 통합) khi mô-đun (module / 모듈) con chưa có dùng:

A. Driver
B. Stub
C. Proxy bắt buộc
D. bảng băm (hash table / 해시 테이블)

## Q34
Bottom-up tích hợp (integration / 통합) khi caller phía trên chưa có dùng:

A. Stub
B. Driver
C. Semaphore
D. Mock DB bắt buộc

## Q35
Sau bug fix, chạy kiểm thử (test / 테스트) cụ thể chứng minh bug đã hết gọi gần nhất là:

A. Retest/confirmation kiểm thử (test / 테스트)
B. Regression-only
C. Alpha kiểm thử (test / 테스트)
D. Static kiểm thử (test / 테스트)

## Q36
Chạy broader existing suite để xem bug fix có phá chức năng khác là:

A. Regression kiểm thử (test / 테스트)
B. đơn vị (unit / 단위) compile
C. Acceptance-only
D. Mutation-only

## Q37
sản phẩm tạo ra (artifact / 산출물) nào có thể là cấu hình (configuration / 구성) item?

A. Chỉ mã nguồn (source code / 소스 코드)
B. nguồn (source / 소스), cấu hình (config / 설정), lược đồ (schema / 스키마), bản dựng (build / 빌드) script, kiểm thử (test / 테스트) sản phẩm tạo ra (artifact / 산출물), manual
C. Chỉ nhị phân (binary / 이진)
D. Chỉ README

## Q38
bản dựng (build / 빌드) khác bản phát hành (release / 릴리스) ở đâu?

A. bản dựng (build / 빌드) tạo sản phẩm tạo ra (artifact / 산출물); bản phát hành (release / 릴리스) là tiến trình (process / 프로세스)/quyết định (decision / 결정) đưa phiên bản (version / 버전) xác định ra môi trường (environment / 환경)/người dùng (user / 사용자)
B. Hai từ đồng nghĩa
C. bản phát hành (release / 릴리스) chỉ compile nguồn (source / 소스)
D. bản dựng (build / 빌드) luôn môi trường vận hành (production / 운영 환경)

## Q39
Checksum trên gói (package / 패키지) chủ yếu kiểm:

A. Authorization
B. Integrity/thay đổi (change / 변경)/corruption
C. CPU speed
D. nghiệp vụ (business / 비즈니스) role

## Q40
Một giao diện (interface / 인터페이스) môi trường vận hành (production / 운영 환경) có hết thời gian chờ (timeout / 타임아웃) tăng nhưng lỗi (error / 오류) tỷ lệ (rate / 비율) thấp. chỉ số (metric / 지표) quan trọng để phát hiện issue này là:

A. độ trễ (latency / 지연 시간)/response-time phân phối (distribution / 분포)
B. Chỉ success count
C. Chỉ phiên bản (version / 버전) number
D. Chỉ line count nguồn (source / 소스)

---

# 제3과목 — 데이터베이스 구축

## Q41
Trong relational terminology cơ bản, degree là:

A. Số rows
B. Số attributes
C. Số indexes
D. Số foreign keys

## Q42
Candidate key là:

A. Bất kỳ superkey nào
B. Minimal superkey
C. Luôn surrogate key
D. Luôn single-column

## Q43
Một bảng (table / 테이블) dùng surrogate `id`, nhưng email phải unique theo nghiệp vụ (business / 비즈니스). Cần:

A. Không cần ràng buộc (constraint / 제약조건) email vì đã có id
B. Unique ràng buộc (constraint / 제약조건)/nghiệp vụ (business / 비즈니스) candidate-key enforcement cho email nếu yêu cầu (requirement / 요구사항) yêu cầu
C. Bỏ primary key
D. Chuyển email thành chỉ mục (index / 인덱스) không unique là đủ

## Q44
FD `{A,B} → A` là:

A. Partial
B. Trivial
C. Transitive
D. Multivalued

## Q45
quan hệ (relation / 관계) có candidate key `(A,B)`, và `A → C`, C non-prime. Vi phạm rõ nhất:

A. 1NF
B. 2NF
C. BCNF nhưng không 2NF
D. Không normalization issue

## Q46
3NF formal cho FD `X → A` chấp nhận nếu:

A. X là superkey hoặc A là prime attribute, ngoài trivial điều kiện (condition / 조건)
B. X luôn single attribute
C. A phải foreign key
D. quan hệ (relation / 관계) có chỉ mục (index / 인덱스)

## Q47
BCNF mạnh hơn 3NF chủ yếu vì:

A. Mọi determinant của non-trivial FD phải là superkey
B. Cấm foreign key
C. Cấm composite key
D. Cấm NULL

## Q48
Lossless decomposition bảo đảm:

A. truy vấn (query / 쿼리) luôn nhanh hơn
B. phép nối (join / 조인) lại không tạo/mất thông tin (information / 정보) sai theo phụ thuộc (dependency / 의존성) các giả định (assumptions / 가정들)
C. Không cần indexes
D. Không có deadlock

## Q49
phụ thuộc (dependency / 의존성) preservation quan tâm:

A. Có enforce các FD từ quan hệ (relation / 관계) con mà không cần phép nối (join / 조인) phức tạp không
B. Disk sức chứa (capacity / 용량)
C. TCP retransmission
D. Backup retention

## Q50
chỉ mục (index / 인덱스) `(customer_id, created_at)` hữu ích tự nhiên cho truy vấn (query / 쿼리) equality theo customer + phạm vi (range / 범위)/thứ tự (order / 순서) theo thời gian (time / 시간) vì:

A. B+cây (tree / 트리) key thứ tự (ordering / 순서) có thể thu hẹp prefix rồi scan ordered phạm vi (range / 범위)
B. băm (hash / 해시) luôn hỗ trợ phạm vi (range / 범위) tốt hơn
C. chỉ mục (index / 인덱스) bỏ qua equality
D. Normalization tự tạo chỉ mục (index / 인덱스)

## Q51
Một boolean column phân bố gần 50/50 thường có:

A. Selectivity rất cao như unique key
B. Selectivity tương đối thấp
C. Cardinality bằng số rows luôn
D. Không thể chỉ mục (index / 인덱스)

## Q52
`WHERE YEAR(created_at)=2026` trên indexed `created_at` có thể kém sargable hơn phạm vi (range / 범위) predicate vì:

A. hàm (function / 함수) trên column có thể cản chỉ mục (index / 인덱스) phạm vi (range / 범위) seek tùy DBMS
B. YEAR luôn cú pháp (syntax / 문법) lỗi (error / 오류)
C. chỉ mục (index / 인덱스) không dùng với date
D. phạm vi (range / 범위) truy vấn (query / 쿼리) không tồn tại

## Q53
SQL kiểm NULL đúng cách:

A. `col = NULL`
B. `col IS NULL`
C. `col == NULL`
D. `NULL(col)`

## Q54
`COUNT(col)` khác `COUNT(*)` vì:

A. `COUNT(col)` bỏ qua NULL
B. `COUNT(*)` bỏ qua mọi NULL row
C. Hai cái luôn giống
D. COUNT chỉ dùng numeric

## Q55
UNION ALL khác UNION:

A. UNION ALL giữ duplicate; UNION loại duplicate
B. UNION ALL chỉ numeric
C. UNION luôn nhanh hơn
D. UNION ALL sort bắt buộc

## Q56
T2 đọc uncommitted giá trị (value / 값) từ T1; T1 abort khiến T2 phải quay lui (rollback / 롤백). Đây liên quan:

A. Cascading quay lui (rollback / 롤백)
B. Phantom only
C. vùng nhớ động (heap / 힙) overflow
D. NAT

## Q57
Basic Two-Phase Locking có phases:

A. Read/ghi (write / 쓰기)
B. Growing acquire locks rồi Shrinking bản phát hành (release / 릴리스) locks
C. lần ghi nhận (commit / 커밋)/quay lui (rollback / 롤백) only
D. Encode/Decode

## Q58
Precedence đồ thị (graph / 그래프) có cycle. Kết luận:

A. Conflict-serializable
B. Không conflict-serializable
C. Chắc chắn deadlock thời gian chạy (runtime / 런타임)
D. Chắc chắn recoverable

## Q59
Checkpoint khác backup vì:

A. Checkpoint hỗ trợ khôi phục (recovery / 복구) coordination/log scan; backup là bản sao (copy / 복사) dữ liệu (data / 데이터) để restore
B. Checkpoint luôn offsite
C. Backup nằm trong RAM
D. Hai cái đồng nghĩa

## Q60
di chuyển (migration / 마이그레이션) chỉ so row count là chưa đủ vì có thể vẫn sai:

A. giá trị (value / 값) precision, encoding, referential integrity, aggregates, nghiệp vụ (business / 비즈니스) invariants
B. Chỉ CSS
C. Chỉ CPU mô hình (model / 모델)
D. Chỉ DNS TTL

---

# 제4과목 — 프로그래밍 언어 활용

## Q61
Static typing đồng nghĩa tuyệt đối với compiled ngôn ngữ (language / 언어)?

A. Có
B. Không; typing discipline và mô hình thực thi (execution model / 실행 모델) là dimensions khác nhau
C. Chỉ với Java
D. Chỉ với C

## Q62
phạm vi (scope / 범위) khác thời gian tồn tại (lifetime / 수명) vì:

A. phạm vi (scope / 범위) là visibility trong nguồn (source / 소스); thời gian tồn tại (lifetime / 수명) là thời gian đối tượng (object / 객체)/lưu trữ (storage / 저장소) tồn tại thời gian chạy (runtime / 런타임)
B. Hai cái giống nhau
C. thời gian tồn tại (lifetime / 수명) chỉ compile-time
D. phạm vi (scope / 범위) chỉ vùng nhớ động (heap / 힙)

## Q63
Trong C, `int **pp` là:

A. Int giá trị (value / 값)
B. Pointer tới pointer tới int
C. Array 2 chiều bắt buộc
D. hàm (function / 함수) pointer

## Q64
Trong C hàm (function / 함수) parameter `int a[]`, `sizeof(a)` thường cho:

A. Total original array kích thước (size / 크기)
B. Pointer kích thước (size / 크기) do parameter adjustment
C. 0
D. Compile lỗi (error / 오류) luôn

## Q65
Union khác struct chủ yếu ở:

A. Members share lưu trữ (storage / 저장소)
B. Không có kiểu (type / 타입)
C. Không thể chứa int
D. Luôn lớn hơn tổng members

## Q66
Java instance phương thức (method / 메서드) overridden được chọn chủ yếu theo:

A. thời gian chạy (runtime / 런타임) đối tượng (object / 객체) kiểu (type / 타입)
B. Chỉ tham chiếu (reference / 참조) variable name
C. Return kiểu (type / 타입)
D. tệp (file / 파일) name

## Q67
Java static phương thức (method / 메서드) khi subclass định nghĩa cùng signature:

A. động (dynamic / 동적) overriding giống instance phương thức (method / 메서드) hoàn toàn
B. phương thức (method / 메서드) hiding/resolution khác động (dynamic / 동적) instance dispatch
C. Compile lỗi (error / 오류) luôn
D. Không thể có static

## Q68
Với đối tượng (object / 객체) references Java, `==` thường kiểm:

A. Logical equality do `.equals()`
B. tham chiếu (reference / 참조) định danh (identity / 식별자)
C. băm (hash / 해시) mã (code / 코드) equality bắt buộc
D. String content luôn

## Q69
Python shallow bản sao (copy / 복사) của nested danh sách (list / 목록):

A. bản sao (copy / 복사) recursively mọi nested đối tượng (object / 객체)
B. Outer bộ chứa (container / 컨테이너) mới nhưng nested objects có thể vẫn dùng chung (shared / 공유)
C. Không tạo đối tượng (object / 객체) mới
D. Chuyển thành tuple

## Q70
Python mutable default argument có thể giữ trạng thái (state / 상태) giữa calls vì:

A. Default được evaluate khi hàm (function / 함수) definition executed
B. Python reset tiến trình (process / 프로세스) mỗi lời gọi (call / 호출)
C. danh sách (list / 목록) immutable
D. `def` không tạo đối tượng (object / 객체)

## Q71
SJF tại thời điểm t chỉ được chọn trong:

A. Mọi tiến trình (process / 프로세스) kể cả chưa arrive
B. Ready processes đã arrive
C. Terminated processes
D. I/O devices

## Q72
phản hồi (response / 응답) thời gian (time / 시간) là:

A. Completion - arrival
B. First CPU run - arrival
C. Total ready waiting
D. Burst - arrival

## Q73
Aging dùng để giảm:

A. Starvation
B. Deadlock cycle bắt buộc
C. Page kích thước (size / 크기)
D. IP fragmentation

## Q74
TLB miss có nghĩa:

A. Chắc chắn page fault
B. Translation không ở TLB; page vẫn có thể resident
C. Disk hỏng
D. tiến trình (process / 프로세스) deadlock

## Q75
Thrashing xảy ra khi:

A. Useful công việc (work / 작업) bị áp đảo bởi paging activity
B. CPU không có bộ nhớ đệm (cache / 캐시)
C. DNS thất bại (fail / 실패)
D. DB normalize

## Q76
Private IPv4 nào đúng?

A. 172.0.0.0/8 toàn bộ
B. 172.16.0.0/12
C. 169.0.0.0/8 toàn bộ
D. 11.0.0.0/8

## Q77
Host `192.168.1.70/26` thuộc mạng (network / 네트워크):

A. 192.168.1.0
B. 192.168.1.64
C. 192.168.1.128
D. 192.168.1.192

## Q78
Default gateway dùng khi:

A. Destination nằm ngoài cục bộ (local / 로컬) subnet và cần router forward
B. Resolve lĩnh vực (domain / 도메인)
C. Encrypt packet
D. Detect SQL injection

## Q79
TCP luồng (flow / 흐름) điều khiển (control / 제어) chủ yếu bảo vệ:

A. Receiver khỏi sender gửi quá nhanh
B. Toàn Internet khỏi routing vòng lặp (loop / 루프)
C. Password lưu trữ (storage / 저장소)
D. DNS authority

## Q80
Three-way handshake của TCP không cung cấp trực tiếp:

A. liên kết (connection / 연결) trạng thái (state / 상태) establishment
B. chuỗi (sequence / 시퀀스) synchronization
C. Encryption/confidentiality
D. Connection-oriented setup

---

# 제5과목 — 정보시스템 구축 관리

## Q81
rủi ro (risk / 위험) khác issue ở điểm:

A. rủi ro (risk / 위험) chưa chắc xảy ra; issue đã xảy ra/cần xử lý
B. Issue luôn positive
C. rủi ro (risk / 위험) không có impact
D. Hai cái giống nhau

## Q82
Trong CPM, forward pass chủ yếu tính:

A. Earliest start/finish
B. Latest start/finish
C. Password băm (hash / 해시)
D. Subnet phạm vi (range / 범위)

## Q83
Một non-critical activity có float 3 ngày. Delay 2 ngày, mọi giả định (assumption / 가정) khác giữ nguyên. Kết luận hợp lý nhất:

A. dự án (project / 프로젝트) chắc chắn delay 2 ngày
B. Có thể chưa ảnh hưởng final finish nếu vẫn trong float
C. đường găng (critical path / 임계 경로) biến mất
D. Không cần theo dõi nữa

## Q84
Vertical scaling là:

A. Thêm nodes
B. Tăng tài nguyên (resource / 자원) của một nút (node / 노드)
C. Chia subnet
D. Add backup site

## Q85
tải (load / 로드) balancing khác failover vì:

A. tải (load / 로드) balancing phân phối công việc (work / 작업); failover chuyển sang healthy/standby khi thất bại (failure / 실패)
B. Hai cái đồng nghĩa
C. Failover chỉ DB
D. tải (load / 로드) balancing chỉ lưu trữ (storage / 저장소)

## Q86
Synchronous replication sự đánh đổi (trade-off / 트레이드오프) điển hình:

A. Giảm data-loss cửa sổ (window / 윈도우) nhưng tăng độ trễ (latency / 지연 시간)/coupling với replica health
B. Không cần mạng (network / 네트워크)
C. RPO luôn vô hạn
D. Không có consistency

## Q87
Differential backup thường chứa:

A. Changes từ last full backup
B. Changes từ immediate previous backup bất kể kiểu (type / 타입)
C. Toàn disk bắt buộc
D. Chỉ siêu dữ liệu (metadata / 메타데이터)

## Q88
Hot site so với cold site thường:

A. khôi phục (recovery / 복구) nhanh hơn nhưng chi phí (cost / 비용) cao hơn
B. khôi phục (recovery / 복구) chậm hơn và rẻ hơn luôn
C. Không có equipment
D. Không có dữ liệu (data / 데이터) chiến lược (strategy / 전략)

## Q89
RPO 5 phút nghĩa:

A. dịch vụ (service / 서비스) phải phục hồi trong 5 phút
B. Mục tiêu mức mất dữ liệu theo thời gian tối đa khoảng 5 phút
C. Backup chạy 5 phút
D. MTTR 5 phút

## Q90
MTTR giảm thường giúp:

A. Availability tăng, các yếu tố khác giữ nguyên
B. Availability giảm
C. RPO tăng bắt buộc
D. CPU clock giảm

## Q91
Trong IaaS, customer thường còn trách nhiệm nhiều hơn SaaS về:

A. OS/middleware/ứng dụng (application / 애플리케이션) cấu hình (configuration / 구성)
B. vật lý (physical / 물리적) datacenter hoàn toàn
C. Provider staff
D. Internet backbone toàn cầu

## Q92
ảnh bộ chứa (container image / 컨테이너 이미지) là:

A. thời gian chạy (runtime / 런타임) tiến trình (process / 프로세스) instance duy nhất
B. Packaged template/layers dùng để tạo containers
C. Hypervisor
D. DNS zone

## Q93
Base64 là:

A. Encryption
B. Encoding
C. băm (hash / 해시)
D. Signature

## Q94
Password salt chủ yếu giúp:

A. Chống precomputed băm (hash / 해시)/rainbow attacks và làm cùng password không ra cùng stored băm (hash / 해시) mẫu (pattern / 패턴)
B. Mã hóa reversible password
C. Thay password chính sách (policy / 정책)
D. Tạo digital signature

## Q95
MAC khác digital signature vì MAC:

A. Dùng dùng chung (shared / 공유) secret giữa parties
B. Luôn dùng công khai (public / 공개)/private key
C. Không kiểm integrity
D. Chỉ dùng cho cơ sở dữ liệu (database / 데이터베이스)

## Q96
RBAC cấp quyền bằng cách:

A. Gắn permissions với roles rồi assign users vào roles
B. Mỗi packet có ACL
C. Mọi người dùng (user / 사용자) admin
D. Chỉ dùng encryption

## Q97
Least privilege khác Separation of Duties vì:

A. Một cái giảm mức quyền; một cái chia trọng yếu (critical / 중요) responsibility qua nhiều principals/roles
B. Hai cái giống nhau
C. SoD chỉ firewall
D. Least privilege chỉ password

## Q98
Stateful firewall khác stateless filter vì:

A. Theo dõi liên kết (connection / 연결)/session trạng thái (state / 상태)
B. Luôn decrypt TLS
C. Luôn là WAF
D. Không có rules

## Q99
Vulnerability scan khác penetration kiểm thử (test / 테스트) ở chỗ:

A. Scan thường tìm known weaknesses tự động hơn; pentest cố exploit/chaining để chứng minh impact trong phạm vi (scope / 범위)
B. Pentest không cần authorization
C. Scan luôn sửa bug
D. Hai cái giống nhau

## Q100
sự cố (incident / 인시던트) phản hồi (response / 응답) sau containment thường cần tiếp tục với:

A. Eradication và khôi phục (recovery / 복구), rồi lessons learned
B. Xóa logs
C. Tắt backup
D. Bỏ root-cause phân tích (analysis / 분석)

---

# Answer Key

```text
1 B   2 B   3 B   4 B   5 B
6 B   7 A   8 B   9 B  10 A
11 B 12 B 13 B 14 A 15 B
16 B 17 B 18 B 19 A 20 B

21 B 22 B 23 B 24 B 25 B
26 C 27 B 28 A 29 B 30 B
31 C 32 B 33 B 34 B 35 A
36 A 37 B 38 A 39 B 40 A

41 B 42 B 43 B 44 B 45 B
46 A 47 A 48 B 49 A 50 A
51 B 52 A 53 B 54 A 55 A
56 A 57 B 58 B 59 A 60 A

61 B 62 A 63 B 64 B 65 A
66 A 67 B 68 B 69 B 70 A
71 B 72 B 73 A 74 B 75 A
76 B 77 B 78 A 79 A 80 C

81 A 82 A 83 B 84 B 85 A
86 A 87 A 88 A 89 B 90 A
91 A 92 B 93 B 94 A 95 A
96 A 97 A 98 A 99 A 100 A
```

---

# High-value rationales

## Q1
Hai yêu cầu (requirement / 요구사항) cho cùng session thời gian tồn tại (lifetime / 수명) nhưng đưa ràng buộc (constraint / 제약조건) mâu thuẫn. Đây là **inconsistency**, không phải ambiguity.

## Q3
DFD decomposition phải bảo toàn logical bên ngoài (external / 외부) đầu vào (input / 입력)/đầu ra (output / 출력) của parent tiến trình (process / 프로세스). Đây là **balancing**.

## Q5
`include` cho hành vi (behavior / 동작) được reuse như phần bắt buộc; `extend` cho hành vi (behavior / 동작) tùy điều kiện/extension điểm (point / 지점).

## Q8
LSP hỏi subtype có thay thế cơ sở (base / 기반) kiểu (type / 타입) mà không phá expectation/đặc tả hợp đồng (contract / 계약) không.

## Q10
bên ngoài (external / 외부) coupling liên quan bên ngoài (external / 외부) format/giao thức (protocol / 프로토콜)/thiết bị (device / 장치) giao diện (interface / 인터페이스) chung; dùng chung (common / 공통) coupling là dùng chung (shared / 공유) toàn cục (global / 전역) dữ liệu (data / 데이터).

## Q17
hết thời gian chờ (timeout / 타임아웃) làm máy khách (client / 클라이언트) không biết kết quả (outcome / 결과) cuối cùng; idempotency bảo repeated same logical thao tác (operation / 연산) không nhân side tác động (effect / 효과).

## Q22
vùng nhớ động (heap / 힙) chỉ bảo đảm parent-child vùng nhớ động (heap / 힙) thuộc tính (property / 속성), không full thứ tự (ordering / 순서) như BST.

## Q25
MST tối ưu tổng weight để connect all vertices, khác shortest đường dẫn (path / 경로) từ nguồn (source / 소스).

## Q31
Statement coverage không chứng minh mọi branch kết quả (outcome / 결과)/đường dẫn (path / 경로) được exercise.

## Q35–36
Retest xác nhận defect cụ thể đã sửa; regression kiểm side effects trên hành vi (behavior / 동작) khác.

## Q43
Surrogate primary key không tự enforce nghiệp vụ (business / 비즈니스) uniqueness của candidate key tự nhiên.

## Q46
3NF formal cho phép determinant là superkey **hoặc** dependent attribute là prime, ngoài trivial phụ thuộc (dependency / 의존성).

## Q48–49
Lossless bảo toàn thông tin (information / 정보) khi phép nối (join / 조인) lại; phụ thuộc (dependency / 의존성) preservation bảo toàn khả năng enforce dependencies ở relations con.

## Q52
Sargability nối cách viết predicate với khả năng optimizer dùng truy cập (access / 접근) đường dẫn (path / 경로)/chỉ mục (index / 인덱스) hiệu quả.

## Q56
Dirty phụ thuộc (dependency / 의존성) có thể gây cascading quay lui (rollback / 롤백) nếu reader phụ thuộc giao dịch (transaction / 트랜잭션) chưa lần ghi nhận (commit / 커밋).

## Q61
Static/động (dynamic / 동적) typing và compiled/interpreted/JIT là dimensions khác nhau.

## Q67
Static phương thức (method / 메서드) không dùng thời gian chạy (runtime / 런타임) polymorphic dispatch giống overridden instance phương thức (method / 메서드).

## Q74
TLB miss chỉ là translation trượt bộ nhớ đệm (cache miss / 캐시 미스); bảng trang (page table / 페이지 테이블) có thể map tới resident frame nên không page fault.

## Q77
`/26` khối (block / 블록) kích thước (size / 크기) 64: ranges 0–63, 64–127, ...; 70 thuộc mạng (network / 네트워크) `.64`.

## Q79
TCP luồng (flow / 흐름) điều khiển (control / 제어) bảo vệ receiver; congestion điều khiển (control / 제어) phản ứng trạng thái mạng (network / 네트워크) đường dẫn (path / 경로).

## Q83
Float/slack cho phép một mức delay không đổi dự án (project / 프로젝트) finish, nếu các giả định (assumptions / 가정들)/mạng (network / 네트워크) không đổi.

## Q86
Sync replication trade RPO/dữ liệu (data / 데이터) durability against ghi (write / 쓰기) độ trễ (latency / 지연 시간) và dependence vào replica/mạng (network / 네트워크) availability.

## Q89
RPO là data-loss mục tiêu (objective / 목표); RTO là dịch vụ (service / 서비스) recovery-time mục tiêu (objective / 목표).

## Q93
Encoding không cung cấp confidentiality. Base64 chỉ thay biểu diễn (representation / 표현).

## Q95
MAC dựa dùng chung (shared / 공유) secret; digital signature dùng asymmetric key và có trust/non-repudiation ngữ nghĩa (semantics / 의미론) khác.

## Q97
Least privilege hỏi “bao nhiêu quyền”; SoD hỏi “một người có được làm toàn bộ trọng yếu (critical / 중요) luồng (flow / 흐름) không”.

---

# Score interpretation

| Môn | Correct / 20 | hành động (action / 동작) |
|---|---:|---|
| 1 | ___ | nếu < 12: quay `01`, `11`, `12`, `15` |
| 2 | ___ | nếu < 12: quay `02`, `08`, `11`, `15` |
| 3 | ___ | nếu < 12: quay `03`, `08`, `11`, `15` |
| 4 | ___ | nếu < 12: quay `04`, `08`, `13`, `15` |
| 5 | ___ | nếu < 12: quay `05`, `11`, `12`, `15` |

Ngưỡng 8/20 ở đây chỉ mô phỏng 과락 40 điểm. Mục tiêu học nên cao hơn: **ít nhất 14/20 mỗi môn ở mock tự viết**, vì đề thật có thể dùng wording và phân phối (distribution / 분포) khác.

## Lỗi (error / 오류) kiểm tra (audit / 감사) bắt buộc

Mỗi câu sai phải ghi:

```text
Q__
Subject:
Error code: COV / CON / PRO / LAY / TERM / READ / CAL / MEM
Why my choice looked plausible:
Why correct answer fits wording better:
Source file to revisit:
Transfer question I can now answer:
```

Không làm lại ngay cùng câu để “nhớ đáp án”. Sau remediation, hãy tự tạo một scenario mới cùng cơ chế (mechanism / 메커니즘) nhưng đổi nouns/numbers.
