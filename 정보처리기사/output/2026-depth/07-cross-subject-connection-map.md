# 정보처리기사 필기 2026 — Cross-Subject liên kết (connection / 연결) Map

> tệp (file / 파일) này dùng sau 5 deep-dive. Mục tiêu không phải học thêm một “môn thứ sáu”, mà nối các khái niệm đang nằm rời rạc giữa 5 môn thành một mô hình hệ thống thống nhất. Khi đề đổi cách diễn đạt, chính các liên kết này giúp suy ra đáp án thay vì phụ thuộc vào việc nhớ đúng một câu định nghĩa.
>
> Thuật ngữ quan trọng giữ tiếng Hàn, kèm English và nghĩa Việt khi cần. Các scenario và câu hỏi trong tệp (file / 파일) đều được viết mới.

---

## 0. Một hệ thống thật không chia thành 5 môn

Trong đề thi, kiến thức được chia thành 소프트웨어 설계, 소프트웨어 개발, 데이터베이스 구축, 프로그래밍 언어 활용 và 정보시스템 구축 관리. Trong hệ thống thật, năm vùng này xảy ra đồng thời.

Một yêu cầu “người dùng có thể thanh toán đơn hàng trong dưới hai giây và không bị tính tiền hai lần” bắt đầu ở **요구사항 — yêu cầu (requirement / 요구사항)**, đi qua **애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)**, trở thành mã (code / 코드) và kiểm thử (test / 테스트) trong **소프트웨어 개발**, lưu trạng thái bằng giao dịch (transaction / 트랜잭션) trong **데이터베이스**, chạy trên tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드), mạng (network / 네트워크) và máy chủ (server / 서버) trong **응용 SW 기초 기술**, rồi cần logging, triển khai (deployment / 배포), bảo mật (security / 보안), availability và khôi phục (recovery / 복구) trong **정보시스템 구축 관리**.

Nếu chỉ học theo từng môn, ta có thể biết tất cả các từ nhưng vẫn không biết chúng ghép với nhau thế nào. Vì vậy tệp (file / 파일) này dùng một câu hỏi xuyên suốt:

> “Khái niệm này nằm ở đâu trong vòng đời yêu cầu (request / 요청) và nó bảo vệ điều gì?”

---

# 1. Từ 요구사항 đến 테스트 — Requirements ↔ Testing

## 1.1 yêu cầu (requirement / 요구사항) không kết thúc ở tài liệu đặc tả

Functional yêu cầu (requirement / 요구사항) — 기능 요구사항 — nói hệ thống phải làm gì. Non-functional yêu cầu (requirement / 요구사항) — 비기능 요구사항 — nói hệ thống phải đạt chất lượng hoặc ràng buộc (constraint / 제약조건) nào.

Nhưng yêu cầu (requirement / 요구사항) chỉ có giá trị khi nó có thể được **검증 — xác minh (verification / 확인)/kiểm tra hợp lệ (validation / 검증)**. Vì vậy yêu cầu (requirement / 요구사항) và kiểm thử (test / 테스트) có quan hệ traceability.

Ví dụ:

```text
R1: 사용자 로그인 가능
    User can log in

R2: 로그인 응답은 95% 요청에서 500ms 이하
    95% login requests finish within 500 ms

R3: 5회 연속 실패 시 계정 잠금
    Lock account after 5 consecutive failures
```

R1 dẫn tới functional kiểm thử (test / 테스트). R2 dẫn tới hiệu năng (performance / 성능) kiểm thử (test / 테스트) với percentile/response-time criterion. R3 dẫn tới bảo mật (security / 보안)/business-rule kiểm thử (test / 테스트), đồng thời liên quan trạng thái (state / 상태) management và tính đồng thời (concurrency / 동시성).

### Liên kết (connection / 연결) cần nhớ

```text
Requirement
    ↓
Acceptance criterion
    ↓
Design decision
    ↓
Implementation
    ↓
Test case
    ↓
Operational metric
```

Nếu đề hỏi “thay đổi yêu cầu (requirement / 요구사항) nhưng trường hợp kiểm thử (test case / 테스트 케이스) không được cập nhật”, vấn đề không chỉ là kiểm thử (test / 테스트). Đó là đứt **추적성 — traceability** giữa yêu cầu (requirement / 요구사항) và xác minh (verification / 확인) sản phẩm tạo ra (artifact / 산출물).

## 1.2 xác minh (verification / 확인) vs kiểm tra hợp lệ (validation / 검증) nối Môn 1 và Môn 2

Xác minh (verification / 확인) hỏi: sản phẩm có được xây đúng theo specification không?

Kiểm tra hợp lệ (validation / 검증) hỏi: specification/sản phẩm có thực sự giải quyết nhu cầu stakeholder không?

Một đơn vị (unit / 단위) kiểm thử (test / 테스트) có thể verify mã (code / 코드) đúng spec nhưng không chứng minh spec đúng nhu cầu người dùng. Ngược lại, người dùng (user / 사용자) acceptance kiểm thử (test / 테스트) có thể phát hiện hệ thống “đúng tài liệu nhưng sai nhu cầu”.

---

# 2. UML, OOP và mẫu thiết kế (design pattern / 디자인 패턴) không phải ba thế giới khác nhau

## 2.1 lớp (class / 클래스) Diagram là mô hình, OOP là cơ chế thời gian chạy (runtime / 런타임)

Lớp (class / 클래스) Diagram — 클래스 다이어그램 — mô tả lớp (class / 클래스), attribute, thao tác (operation / 연산) và relationship. Encapsulation, inheritance, polymorphism là các cơ chế mà hiện thực (implementation / 구현) có thể dùng để hiện thực mô hình đó.

Một mũi tên generalization trong UML không tự động nói mã (code / 코드) sẽ “tốt”. Nếu hierarchy vi phạm Liskov Substitution Principle — LSP — 리스코프 치환 원칙, mô hình vẫn vẽ được nhưng thiết kế yếu.

## 2.2 mẫu (pattern / 패턴) là lời giải cho force lặp lại

Mẫu (pattern / 패턴) không phải từ khóa (keyword / 키워드) để ghép tên. Hãy nối mẫu (pattern / 패턴) với loại variation mà hệ thống cần hấp thụ.

Chiến lược (strategy / 전략) — 전략 패턴 — variation của thuật toán (algorithm / 알고리즘).
trạng thái (state / 상태) — 상태 패턴 — variation của hành vi (behavior / 동작) theo trạng thái nội bộ (internal state / 내부 상태).
Observer — 옵저버 패턴 — one-to-many notification khi trạng thái (state / 상태) thay đổi.
Adapter — 어댑터 패턴 — giao diện (interface / 인터페이스) không tương thích.
Facade — 퍼사드 패턴 — subsystem phức tạp cần mặt tiền đơn giản.
Decorator — 데코레이터 패턴 — thêm hành vi (behavior / 동작) động quanh đối tượng (object / 객체) mà không đổi lớp (class / 클래스) gốc.

### Câu hỏi suy luận

Nếu hai lớp (class / 클래스) “nhìn giống nhau” trong UML nhưng một lớp (class / 클래스) được chọn dựa trên nghiệp vụ (business / 비즈니스) chính sách (policy / 정책) còn một lớp (class / 클래스) được chọn vì đối tượng (object / 객체) đang ở trạng thái `PAID/SHIPPED/CANCELLED`, hai trường hợp có thể dùng chiến lược (strategy / 전략) và trạng thái (state / 상태) khác nhau dù sơ đồ lớp (class / 클래스) có cấu trúc gần giống.

---

# 3. giao diện (interface / 인터페이스) thiết kế (design / 설계) ↔ tích hợp (integration / 통합) ↔ mạng (network / 네트워크)

## 3.1 Đặc tả API (API contract / API 계약) không dừng ở JSON

인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계) — xác định dữ liệu, giao thức (protocol / 프로토콜), lỗi (error / 오류) handling, chuỗi (sequence / 시퀀스) và đặc tả hợp đồng (contract / 계약) giữa hai thành phần. Khi triển khai, đặc tả hợp đồng (contract / 계약) đó đi qua mạng (network / 네트워크) thật.

Ví dụ API:

```http
POST /payments
Idempotency-Key: abc-123
Content-Type: application/json
```

JSON lược đồ (schema / 스키마) thuộc đặc tả hợp đồng (contract / 계약). HTTP phương thức (method / 메서드)/status thuộc ứng dụng (application / 애플리케이션) giao thức (protocol / 프로토콜). TCP chịu trách nhiệm reliable byte stream. IP chịu trách nhiệm packet forwarding. Ethernet/Wi-Fi xử lý cục bộ (local / 로컬) link.

Đây là lý do OSI/TCP-IP ở Môn 4 liên quan trực tiếp giao diện (interface / 인터페이스) hiện thực (implementation / 구현) ở Môn 1–2.

## 3.2 hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도) và duplicate side tác động (effect / 효과)

Nếu máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) sau khi máy chủ (server / 서버) đã charge card nhưng trước khi phản hồi (response / 응답) quay lại, máy khách (client / 클라이언트) có thể thử lại (retry / 재시도). Nếu endpoint không idempotent, cùng một nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) có thể chạy hai lần.

Vì vậy:

```text
Network uncertainty
    ↓
Retry
    ↓
Duplicate request risk
    ↓
Idempotency design
    ↓
DB uniqueness / transaction
```

Một câu hỏi về “중복 처리 방지 — duplicate processing prevention” có thể đòi suy nghĩ đồng thời về giao diện (interface / 인터페이스), máy chủ (server / 서버) lô-gic (logic / 논리) và cơ sở dữ liệu (database / 데이터베이스) ràng buộc (constraint / 제약조건).

## 3.3 EAI/ESB và coupling

Point-to-point tích hợp (integration / 통합) tăng nhanh số liên kết (connection / 연결) khi số hệ thống (system / 시스템) tăng. EAI/ESB cố gắng tập trung hoặc chuẩn hóa mediation, routing và transformation.

Nhưng thêm middleware không tự động tạo low coupling. Nếu mọi bên tiêu thụ (consumer / 소비자) phụ thuộc chặt vào một lược đồ (schema / 스키마) duy nhất và thay lược đồ (schema / 스키마) gây vỡ toàn bộ, logical coupling vẫn cao.

---

# 4. Logical mô hình dữ liệu (data model / 데이터 모델) ↔ vật lý (physical / 물리적) DB ↔ SQL ↔ giao dịch (transaction / 트랜잭션)

## 4.1 Normalization giải quyết anomaly, không giải quyết mọi hiệu năng (performance / 성능) bài toán (problem / 문제)

정규화 — normalization — dùng functional phụ thuộc (dependency / 의존성) để giảm redundancy và cập nhật (update / 업데이트) anomaly. 물리 설계 — vật lý (physical / 물리적) thiết kế (design / 설계) — chọn chỉ mục (index / 인덱스), partition, lưu trữ (storage / 저장소), denormalization có kiểm soát để đáp ứng tải công việc (workload / 워크로드).

Do đó:

```text
Logical correctness ≠ Physical performance
```

Một lược đồ (schema / 스키마) có thể ở 3NF/BCNF nhưng truy vấn (query / 쿼리) chậm vì thiếu chỉ mục (index / 인덱스) hoặc truy cập (access / 접근) mẫu (pattern / 패턴) không phù hợp. Một lược đồ (schema / 스키마) denormalized có thể nhanh hơn cho read nhưng tăng consistency burden.

## 4.2 chỉ mục (index / 인덱스) nối SQL với cấu trúc dữ liệu (data structure / 자료구조)

B+cây (tree / 트리) chỉ mục (index / 인덱스) hoạt động tốt với equality và phạm vi (range / 범위) vì key có thứ tự. băm (hash / 해시) chỉ mục (index / 인덱스) tự nhiên cho equality lookup nhưng không hỗ trợ phạm vi (range / 범위) theo thứ tự (ordering / 순서) như B+cây (tree / 트리).

Đây là liên kết (connection / 연결) giữa:

- 자료구조 — cấu trúc dữ liệu (data structure / 자료구조) ở Môn 2;
- 물리 데이터베이스 설계 — vật lý (physical / 물리적) DB ở Môn 3;
- truy vấn (query / 쿼리) hiệu năng (performance / 성능) trong hệ thống (system / 시스템) management.

## 4.3 giao dịch (transaction / 트랜잭션) nối nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) với tính đồng thời (concurrency / 동시성)

ACID không phải bốn từ riêng lẻ. Nó bảo vệ bất biến (invariant / 불변식) khi nhiều thao tác (operation / 연산) cùng diễn ra hoặc hệ thống crash.

Ví dụ chuyển 100 từ A sang B:

```text
A = A - 100
B = B + 100
```

Atomicity bảo đảm không chỉ một nửa được lần ghi nhận (commit / 커밋). Consistency nói giao dịch (transaction / 트랜잭션) hợp lệ phải đưa DB từ trạng thái thỏa bất biến (invariant / 불변식) sang trạng thái thỏa bất biến (invariant / 불변식). Isolation kiểm soát interference giữa concurrent giao dịch (transaction / 트랜잭션). Durability bảo đảm committed kết quả (result / 결과) sống qua crash theo cơ chế persistence/khôi phục (recovery / 복구).

Locking, MVCC, log, checkpoint và khôi phục (recovery / 복구) là hiện thực (implementation / 구현) mechanisms hỗ trợ các thuộc tính (property / 속성) đó.

---

# 5. thuật toán (algorithm / 알고리즘)/cấu trúc dữ liệu (data structure / 자료구조) ↔ hiệu năng (performance / 성능)

## 5.1 Big-O không bằng thời gian chạy thực tế

복잡도 — độ phức tạp (complexity / 복잡도) — mô tả tốc độ tăng tài nguyên (resource / 자원) theo đầu vào (input / 입력) kích thước (size / 크기). Nó không nói chính xác một yêu cầu (request / 요청) mất bao nhiêu millisecond.

Hai thuật toán (algorithm / 알고리즘) đều O(n log n) có thể khác constant factor, bộ nhớ (memory / 메모리) locality và hành vi (behavior / 동작) trên đầu vào (input / 입력) cụ thể.

### Liên kết (connection / 연결)

```text
Algorithmic complexity
+ data structure
+ input distribution
+ I/O
+ cache/memory
+ concurrency
= observed performance
```

Nếu đề cho một vấn đề lookup nhiều lần, chọn cấu trúc dữ liệu (data structure / 자료구조) đúng thường quan trọng hơn micro-optimization cú pháp (syntax / 문법).

## 5.2 hàng đợi (queue / 큐) xuất hiện ở nhiều môn

Hàng đợi (queue / 큐) — 큐 — FIFO cấu trúc (structure / 구조) ở Môn 2. Nhưng cùng lớp trừu tượng (abstraction / 추상화) xuất hiện trong:

- tiến trình (process / 프로세스) scheduling;
- message hàng đợi (queue / 큐);
- mạng (network / 네트워크) buffer;
- job hàng đợi (queue / 큐);
- producer/bên tiêu thụ (consumer / 소비자).

Cần phân biệt lớp trừu tượng (abstraction / 추상화) “hàng đợi (queue / 큐)” với chính sách (policy / 정책) cụ thể. Round Robin dùng ready hàng đợi (queue / 큐) nhưng scheduling chính sách (policy / 정책) không đơn giản bằng “FIFO thuần”.

---

# 6. máy chủ (server / 서버) Program ↔ tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) ↔ Synchronization

## 6.1 yêu cầu (request / 요청) tính đồng thời (concurrency / 동시성) cuối cùng trở thành shared-state bài toán (problem / 문제)

Máy chủ (server / 서버) nhận nhiều yêu cầu (request / 요청) cùng lúc. Tùy kiến trúc (architecture / 아키텍처), yêu cầu (request / 요청) có thể được xử lý bởi tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), vòng lặp sự kiện (event loop / 이벤트 루프) hoặc worker pool.

Nếu hai đơn vị thực thi (execution unit / 실행 유닛) cùng cập nhật trạng thái dùng chung (shared state / 공유 상태) mà không có synchronization phù hợp, race điều kiện (condition / 조건) — 경쟁 상태 — có thể xuất hiện.

Ví dụ:

```text
stock = 1
T1 reads stock = 1
T2 reads stock = 1
T1 writes stock = 0
T2 writes stock = 0
```

Hai thứ tự (order / 순서) đều nghĩ đã mua thành công dù chỉ có một item.

Ở ứng dụng (application / 애플리케이션) tầng (layer / 계층), có thể dùng khóa (lock / 잠금). Ở cơ sở dữ liệu (database / 데이터베이스) tầng (layer / 계층), có thể dùng giao dịch (transaction / 트랜잭션)/row khóa (lock / 잠금)/optimistic tính đồng thời (concurrency / 동시성). Chọn tầng (layer / 계층) phụ thuộc bất biến (invariant / 불변식) và hệ thống (system / 시스템) ranh giới (boundary / 경계).

## 6.2 Mutex, Semaphore và DB khóa (lock / 잠금) có họ hàng nhưng không đồng nhất

Mutex — 상호배제 — thường biểu diễn quyền sở hữu (ownership / 소유권) của trọng yếu (critical / 중요) section. Semaphore — 세마포어 — counter cho phép một số lượng permit. cơ sở dữ liệu (database / 데이터베이스) khóa (lock / 잠금) bảo vệ dữ liệu (data / 데이터) item/phạm vi (range / 범위) theo giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론).

Không nên suy rằng “đều là khóa (lock / 잠금) nên giống nhau”. Chúng giải quyết tính đồng thời (concurrency / 동시성) ở các lớp trừu tượng (abstraction / 추상화) mức (level / 수준) khác nhau.

---

# 7. Virtual bộ nhớ (memory / 메모리) ↔ ứng dụng (application / 애플리케이션) hành vi (behavior / 동작)

Page fault — 페이지 폴트 — xảy ra khi referenced page chưa ở vật lý (physical / 물리적) bộ nhớ (memory / 메모리). Page replacement chính sách (policy / 정책) quyết định page nào bị thay khi cần frame.

Ứng dụng (application / 애플리케이션) có poor locality có thể gây nhiều page fault. Vì vậy locality không chỉ là khái niệm OS; bố cục (layout / 레이아웃) dữ liệu (data / 데이터) và truy cập (access / 접근) mẫu (pattern / 패턴) ở mã (code / 코드) ảnh hưởng hành vi (behavior / 동작) của bộ nhớ (memory / 메모리) hierarchy.

Working set quá lớn so với available bộ nhớ (memory / 메모리) có thể dẫn tới thrashing — 스래싱 — hệ thống tốn phần lớn thời gian paging thay vì làm công việc hữu ích.

---

# 8. DB tính đồng thời (concurrency / 동시성) ↔ OS tính đồng thời (concurrency / 동시성): giống câu hỏi, khác đơn vị bảo vệ

Cả OS synchronization và DB giao dịch (transaction / 트랜잭션) đều hỏi:

> “Hai hoạt động cùng lúc có thể làm trạng thái (state / 상태) trở nên sai không?”

Nhưng đơn vị (unit / 단위) khác nhau.

OS có tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드), bộ nhớ (memory / 메모리), trọng yếu (critical / 중요) section.
DB có giao dịch (transaction / 트랜잭션), row/page/phạm vi (range / 범위), isolation mức (level / 수준).

Deadlock có thể tồn tại ở cả hai: mỗi bên giữ tài nguyên (resource / 자원) mà bên kia cần. Cách phát hiện/giải quyết có thể dùng wait-for đồ thị (graph / 그래프), hết thời gian chờ (timeout / 타임아웃), prevention hoặc victim selection, nhưng ngữ nghĩa (semantics / 의미론) cụ thể khác nhau.

---

# 9. mạng (network / 네트워크) ↔ bảo mật (security / 보안)

## 9.1 bảo mật (security / 보안) điều khiển (control / 제어) nằm trên nhiều tầng (layer / 계층)

Firewall — 방화벽 — kiểm soát traffic theo quy tắc (rule / 규칙). IDS phát hiện suspicious activity. IPS có thể khối (block / 블록) inline. TLS cung cấp cryptographic protection cho vận chuyển (transport / 전송)/ứng dụng (application / 애플리케이션) communication. VPN tạo protected tunnel. WAF tập trung HTTP/web ứng dụng (application / 애플리케이션) traffic.

Không hỏi “công cụ nào mạnh nhất”; hỏi **threat ở tầng (layer / 계층) nào và điều khiển (control / 제어) quan sát được gì**.

Ví dụ SQL Injection không được giải quyết tận gốc bằng firewall L3/L4. Secure coding với parameterized truy vấn (query / 쿼리) xử lý nguyên nhân tại ứng dụng (application / 애플리케이션)/DB ranh giới (boundary / 경계); WAF có thể là additional defense.

## 9.2 Authentication, Authorization, Encryption

인증 — authentication — xác minh ai.
인가/권한부여 — authorization — người đó được làm gì.
암호화 — encryption — bảo vệ confidentiality của dữ liệu (data / 데이터).

TLS có thể bảo vệ channel nhưng không tự quyết định người dùng (user / 사용자) có quyền xóa bản ghi (record / 레코드) hay không.

---

# 10. Availability ↔ Redundancy ↔ Disaster khôi phục (recovery / 복구)

Availability — 가용성 — khả năng dịch vụ (service / 서비스) sẵn sàng khi cần. Redundancy — 이중화/중복성 — thêm thành phần (component / 컴포넌트)/đường dẫn (path / 경로) dự phòng để giảm single điểm (point / 지점) of thất bại (failure / 실패). Backup — 백업 — bản sao dữ liệu (data / 데이터) để phục hồi. Disaster khôi phục (recovery / 복구) — 재해복구 — năng lực (capability / 역량) khôi phục dịch vụ (service / 서비스)/dữ liệu (data / 데이터) sau sự cố lớn.

RTO — khôi phục (recovery / 복구) thời gian (time / 시간) mục tiêu (objective / 목표) — thời gian gián đoạn tối đa mục tiêu.
RPO — khôi phục (recovery / 복구) điểm (point / 지점) mục tiêu (objective / 목표) — mức mất dữ liệu tính theo thời gian mà tổ chức chấp nhận.

Một RAID array không thay thế backup. Một backup mỗi ngày không tự đảm bảo RPO 5 phút. Multi-AZ redundancy không tự động thay thế disaster khôi phục (recovery / 복구) nếu cùng loại miền lỗi (failure domain / 장애 도메인) vẫn có thể phá hủy toàn hệ thống.

---

# 11. Secure SDLC nối Môn 1, 2 và 5

Bảo mật (security / 보안) không chỉ nằm ở cuối dự án (project / 프로젝트).

```text
Requirements: xác định security requirement
Design: threat modeling, trust boundary, least privilege
Implementation: secure coding
Testing: SAST/DAST, penetration testing, abuse cases
Deployment: secrets/config/network hardening
Operation: logging, monitoring, patching, incident response
```

Nếu chỉ “scan sau khi mã (code / 코드) xong”, nhiều flaw kiến trúc không thể sửa rẻ như khi phát hiện ở thiết kế (design / 설계) stage.

### Example

Yêu cầu (requirement / 요구사항): chỉ đơn vị sở hữu (owner / 오너) được xem invoice.
thiết kế (design / 설계): object-level authorization check.
hiện thực (implementation / 구현): máy chủ (server / 서버) lấy đơn vị sở hữu (owner / 오너) từ authenticated định danh (identity / 식별자), không tin `userId` do máy khách (client / 클라이언트) tự gửi.
kiểm thử (test / 테스트): thử IDOR/BOLA bằng cách đổi invoice ID.
thao tác (operation / 연산): kiểm tra (audit / 감사) truy cập (access / 접근) bất thường.

---

# 12. dự án (project / 프로젝트) Management ↔ cấu hình (configuration / 구성) ↔ thay đổi (change / 변경)

Một thay đổi (change / 변경) yêu cầu (request / 요청) không chỉ đổi mã (code / 코드). Nó có thể đổi yêu cầu (requirement / 요구사항), lược đồ (schema / 스키마), API, kiểm thử (test / 테스트), triển khai (deployment / 배포) gói (package / 패키지), manual và operational procedure.

Cấu hình (configuration / 구성) Management — 형상관리 — quản lý phiên bản (version / 버전)/baseline/thay đổi (change / 변경) của cấu hình (configuration / 구성) items. phiên bản (version / 버전) điều khiển (control / 제어) là một phần quan trọng nhưng không đồng nghĩa toàn bộ cấu hình (configuration / 구성) management.

### Chuỗi (chain / 사슬)

```text
Change request
→ impact analysis
→ approval/prioritization
→ requirement/design update
→ code + DB/API change
→ test update
→ version/baseline
→ release/deploy
→ monitoring/rollback plan
```

Nếu một câu hỏi hỏi “mã (code / 코드) đúng nhưng môi trường vận hành (production / 운영 환경) dùng nhầm sản phẩm tạo ra (artifact / 산출물)”, đây có thể là bản phát hành (release / 릴리스)/cấu hình (configuration / 구성) management bài toán (problem / 문제), không phải coding thuật toán (algorithm / 알고리즘) bài toán (problem / 문제).

---

# 13. Tám scenario liên môn

## Scenario 1 — Duplicate Payment

### Tình huống

Mobile app gọi payment API. máy chủ (server / 서버) charge thành công nhưng phản hồi (response / 응답) bị mất do mạng (network / 네트워크) interruption. App thử lại (retry / 재시도) và người dùng (user / 사용자) bị charge hai lần.

### Phân tích

Mạng (network / 네트워크) không thể bảo đảm máy khách (client / 클라이언트) luôn biết yêu cầu (request / 요청) trước đã hoàn thành. Vì vậy giao diện (interface / 인터페이스) cần idempotency ngữ nghĩa (semantics / 의미론). máy chủ (server / 서버) có thể lưu `Idempotency-Key` với kết quả (result / 결과) trong giao dịch (transaction / 트랜잭션) hoặc enforce unique ràng buộc (constraint / 제약조건) theo nghiệp vụ (business / 비즈니스) thao tác (operation / 연산).

### Kiến thức nối

인터페이스 설계 → TCP/mạng (network / 네트워크) bất định (uncertainty / 불확실성) → máy chủ (server / 서버) hiện thực (implementation / 구현) → giao dịch (transaction / 트랜잭션)/unique ràng buộc (constraint / 제약조건) → testing thử lại (retry / 재시도) scenario.

### Tự trả lời

1. Tại sao “TCP reliable” vẫn không loại bỏ duplicate nghiệp vụ (business / 비즈니스) thao tác (operation / 연산)?
2. Idempotency khác giao dịch (transaction / 트랜잭션) atomicity ở đâu?
3. Nếu key được lưu ngoài giao dịch (transaction / 트랜잭션) charge thì race nào vẫn có thể xảy ra?

---

## Scenario 2 — Overselling Stock

Hai yêu cầu (request / 요청) cùng mua item cuối cùng.

Ứng dụng (application / 애플리케이션) check `stock > 0`, sau đó cập nhật (update / 업데이트). Nếu check và cập nhật (update / 업데이트) không nằm trong concurrency-control ranh giới (boundary / 경계) phù hợp, lost cập nhật (update / 업데이트) hoặc overselling có thể xảy ra.

Các phương án có thể gồm pessimistic khóa (lock / 잠금), atomic conditional cập nhật (update / 업데이트), serializable giao dịch (transaction / 트랜잭션), optimistic phiên bản (version / 버전) check. Không có một answer duy nhất cho mọi kiến trúc (architecture / 아키텍처); đề thường cho ràng buộc (constraint / 제약조건) để chọn.

### Tự trả lời

- `SELECT stock` rồi `UPDATE stock = stock - 1` tách rời có race gì?
- Atomic SQL `UPDATE ... WHERE stock > 0` thay đổi trọng yếu (critical / 중요) section như thế nào?
- Mutex trong một máy chủ (server / 서버) instance có đủ khi chạy 10 instances không?

---

## Scenario 3 — Slow tìm kiếm (search / 검색) API

Bảng (table / 테이블) có 30 triệu row. truy vấn (query / 쿼리):

```sql
SELECT id, created_at, total
FROM orders
WHERE customer_id = ?
  AND created_at >= ?
ORDER BY created_at DESC
LIMIT 20;
```

Đây không chỉ là SQL cú pháp (syntax / 문법). Cần xét chỉ mục (index / 인덱스) key thứ tự (order / 순서), selectivity, B+cây (tree / 트리) phạm vi (range / 범위) scan, sort avoidance, cardinality và truy cập (access / 접근) mẫu (pattern / 패턴).

Composite chỉ mục (index / 인덱스) `(customer_id, created_at)` có thể phù hợp vì equality trên customer rồi phạm vi (range / 범위)/thứ tự (order / 순서) trên created thời gian (time / 시간). Nhưng quyết định cuối cùng phụ thuộc DBMS và tải công việc (workload / 워크로드).

### Tự trả lời

- Tại sao băm (hash / 해시) chỉ mục (index / 인덱스) không tự nhiên cho phần phạm vi (range / 범위)/thứ tự (order / 순서)?
- Normalization có giải quyết truy vấn (query / 쿼리) chậm này không?
- Vì sao chỉ mục (index / 인덱스) quá nhiều lại làm ghi (write / 쓰기) đắt hơn?

---

## Scenario 4 — Login dịch vụ (service / 서비스) bị tấn công brute force

Yêu cầu (requirement / 요구사항) cần tỷ lệ (rate / 비율) limit/lockout. thiết kế (design / 설계) phải tránh cho attacker khóa account người khác quá dễ. hiện thực (implementation / 구현) cần secure password hashing, constant-time comparison ở chỗ phù hợp, session/đơn vị từ (token / 토큰) handling. mạng (network / 네트워크) cần TLS. Monitoring cần phát hiện mẫu (pattern / 패턴) bất thường.

### Tự trả lời

- Authentication khác authorization ở đâu trong scenario này?
- TLS giải quyết phần nào và không giải quyết phần nào?
- Account lockout có thể tạo denial-of-service véc-tơ (vector / 벡터) như thế nào?

---

## Scenario 5 — Batch Job ăn hết bộ nhớ (memory / 메모리)

Job đọc toàn bộ tệp (file / 파일) 10 GB vào danh sách (list / 목록) trước khi tiến trình (process / 프로세스). vùng nhớ động (heap / 힙) tăng, GC/paging tăng và host có thể thrash.

Giải pháp kiến trúc có thể là streaming/chunking. Đây là liên kết (connection / 연결) giữa thuật toán (algorithm / 알고리즘)/cấu trúc dữ liệu (data structure / 자료구조), bộ nhớ (memory / 메모리) management và ứng dụng (application / 애플리케이션) hiệu năng (performance / 성능).

### Tự trả lời

- Big-O không gian (space / 공간) của cách tải (load / 로드) toàn bộ là gì theo đầu vào (input / 입력) kích thước (size / 크기)?
- Streaming thay đổi peak bộ nhớ (memory / 메모리) ra sao?
- Page replacement chính sách (policy / 정책) có cứu được một working set vượt xa RAM không?

---

## Scenario 6 — Đặc tả API (API contract / API 계약) thay đổi làm nhiều hệ thống lỗi

Provider rename trường dữ liệu (field / 필드) `customerId` thành `userId`. Nhiều bên tiêu thụ (consumer / 소비자) thất bại (fail / 실패).

Đây là giao diện (interface / 인터페이스) tính tương thích (compatibility / 호환성), versioning và coupling bài toán (problem / 문제). tích hợp (integration / 통합) kiến trúc (architecture / 아키텍처) có thể giảm direct phụ thuộc (dependency / 의존성), nhưng lược đồ (schema / 스키마) evolution vẫn cần tính tương thích (compatibility / 호환성) chiến lược (strategy / 전략), bên tiêu thụ (consumer / 소비자) testing và thay đổi (change / 변경) management.

### Tự trả lời

- Adapter có thể dùng ở đâu?
- phiên bản (version / 버전) điều khiển (control / 제어) có đủ để ngăn breaking thay đổi (change / 변경) môi trường vận hành (production / 운영 환경) không?
- đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) nối yêu cầu (requirement / 요구사항)/giao diện (interface / 인터페이스) với kiểm thử (test / 테스트) như thế nào?

---

## Scenario 7 — cơ sở dữ liệu (database / 데이터베이스) primary chết

Nếu hệ thống có replica nhưng failover mất 20 phút, availability có thể vẫn không đạt SLO. Nếu replica async lag 30 giây, failover có thể mất recent dữ liệu (data / 데이터).

RTO liên quan thời gian phục hồi. RPO liên quan mức dữ liệu (data / 데이터) mất mát (loss / 손실). Redundancy, replication, backup và DR phải được thiết kế theo mục tiêu (objective / 목표), không phải chỉ “có nhiều máy chủ (server / 서버)”.

### Tự trả lời

- Async replication ảnh hưởng RPO thế nào?
- Backup hàng đêm có thể đáp ứng RPO 5 phút không?
- RAID bảo vệ loại thất bại (failure / 실패) nào và không bảo vệ loại nào?

---

## Scenario 8 — Deadlock trong thứ tự (order / 순서) processing

Giao dịch (transaction / 트랜잭션) T1 khóa (lock / 잠금) `order` rồi `inventory`; T2 khóa (lock / 잠금) `inventory` rồi `order`. Hai bên chờ nhau.

Đây là circular wait. Có thể giảm bằng consistent khóa (lock / 잠금) thứ tự (ordering / 순서), hết thời gian chờ (timeout / 타임아웃)/deadlock detection hoặc giao dịch (transaction / 트랜잭션) redesign.

### Tự trả lời

- Vì sao “khóa (lock / 잠금) nhiều hơn” không đồng nghĩa an toàn hơn?
- Deadlock khác starvation ở đâu?
- Consistent tài nguyên (resource / 자원) thứ tự (ordering / 순서) phá điều kiện nào của deadlock?

---

# 14. liên kết (connection / 연결) ma trận (matrix / 행렬) để tự kiểm tra

| Nếu gặp khái niệm này | Hãy nối ngay sang |
|---|---|
| 요구사항 / yêu cầu (requirement / 요구사항) | acceptance criteria, kiểm thử (test / 테스트), traceability, thay đổi (change / 변경) management |
| UML / kiến trúc (architecture / 아키텍처) | OOP, patterns, mô-đun (module / 모듈) coupling, giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약) |
| giao diện (interface / 인터페이스)/API | giao thức (protocol / 프로토콜), hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도), idempotency, bảo mật (security / 보안), tích hợp (integration / 통합) |
| cấu trúc dữ liệu (data structure / 자료구조) | thuật toán (algorithm / 알고리즘) độ phức tạp (complexity / 복잡도), chỉ mục (index / 인덱스), scheduler/buffer usage |
| Normalization | phụ thuộc (dependency / 의존성), anomaly, vật lý (physical / 물리적) thiết kế (design / 설계), truy vấn (query / 쿼리) tải công việc (workload / 워크로드) |
| SQL | chỉ mục (index / 인덱스), giao dịch (transaction / 트랜잭션), locking, authorization |
| tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) | scheduling, synchronization, máy chủ (server / 서버) tính đồng thời (concurrency / 동시성) |
| Virtual bộ nhớ (memory / 메모리) | locality, page fault, ứng dụng (application / 애플리케이션) bộ nhớ (memory / 메모리) hành vi (behavior / 동작) |
| mạng (network / 네트워크) | giao diện (interface / 인터페이스) vận chuyển (transport / 전송), routing, firewall, TLS, availability |
| bảo mật (security / 보안) | yêu cầu (requirement / 요구사항), thiết kế (design / 설계), mã (code / 코드), kiểm thử (test / 테스트), thao tác (operation / 연산) |
| RAID/Replication | availability, miền lỗi (failure domain / 장애 도메인), RTO/RPO, backup |
| SCM/cấu hình (configuration / 구성) | thay đổi (change / 변경), hiện vật bản dựng (build artifact / 빌드 산출물), bản phát hành (release / 릴리스), quay lui (rollback / 롤백) |

---

# 15. Closed-book tích hợp (integration / 통합) drill

Không nhìn tài liệu, hãy giải thích liên tục một yêu cầu (request / 요청) `POST /orders` từ lúc yêu cầu (requirement / 요구사항) được viết đến lúc môi trường vận hành (production / 운영 환경) phục hồi sau thất bại (failure / 실패). Câu trả lời đạt yêu cầu khi tự nối được ít nhất các điểm sau mà không biến thành danh sách từ khóa rời rạc:

1. functional/non-functional yêu cầu (requirement / 요구사항);
2. UML/thành phần (component / 컴포넌트)/giao diện (interface / 인터페이스) thiết kế (design / 설계);
3. mô-đun (module / 모듈) responsibility và coupling;
4. kiểm tra hợp lệ (validation / 검증)/đầu vào (input / 입력) handling;
5. máy chủ (server / 서버) tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) thực thi (execution / 실행);
6. thuật toán (algorithm / 알고리즘)/cấu trúc dữ liệu (data structure / 자료구조) chính;
7. SQL và chỉ mục (index / 인덱스);
8. giao dịch (transaction / 트랜잭션)/isolation/tính đồng thời (concurrency / 동시성);
9. TCP/IP và mạng (network / 네트워크) đường dẫn (path / 경로);
10. authentication/authorization/TLS;
11. logging/monitoring;
12. triển khai (deployment / 배포)/cấu hình (configuration / 구성)/phiên bản (version / 버전);
13. redundancy/backup;
14. RTO/RPO và khôi phục (recovery / 복구).

Nếu bị đứng ở bất kỳ chuyển tiếp (transition / 전이) nào, quay lại deep-dive của hai môn nằm hai bên chuyển tiếp (transition / 전이) đó. Đây là dấu hiệu của **liên kết (connection / 연결) gap**, khác với việc hoàn toàn chưa biết một concept.

---

# 16. Definition of Done

Tệp (file / 파일) này chỉ hoàn thành khi bạn có thể làm ba việc.

**End-to-end lập luận (reasoning / 추론):** nhìn một scenario và theo yêu cầu (request / 요청)/dữ liệu (data / 데이터) xuyên qua thiết kế (design / 설계) → mã (code / 코드) → DB → OS/mạng (network / 네트워크) → thao tác (operation / 연산)/bảo mật (security / 보안).

**ranh giới (boundary / 경계) lập luận (reasoning / 추론):** biết cùng một vấn đề như tính đồng thời (concurrency / 동시성), availability hoặc kiểm tra hợp lệ (validation / 검증) được xử lý khác nhau ở các lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층) nào.

**sự đánh đổi (trade-off / 트레이드오프) lập luận (reasoning / 추론):** không trả lời bằng khẩu hiệu “càng nhiều chỉ mục (index / 인덱스) càng tốt”, “normalize luôn tốt”, “RAID là backup”, “TLS là đủ bảo mật”, mà chỉ ra benefit, chi phí (cost / 비용) và phạm vi bảo vệ.
