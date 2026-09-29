# 정보처리기사 필기 2026 — Coverage kiểm tra (audit / 감사) & Closed-Book Recall

> tệp (file / 파일) này là lớp **kiểm tra (audit / 감사) cuối**. Nó không dạy lại toàn bộ lý thuyết; nó kiểm tra xem 21 vùng kiến thức lớn đã thật sự được hiểu hay mới chỉ “đã đọc”. Mỗi mục có ba tiêu chuẩn: **Explain**, **Distinguish**, **Solve**.

---

## Cách chấm

Mỗi chapter tự đánh dấu:

```text
E = Explain: giải thích được bản chất không nhìn tài liệu
D = Distinguish: phân biệt được các khái niệm gần nhau
S = Solve: làm được scenario/code/SQL/tính liên quan
```

Chỉ khi `E+D+S` đều đạt mới coi chapter là closed-book ready.

---

# Môn 1 — 소프트웨어 설계

## 1. 요구사항 확인 — Requirements Confirmation

### Explain

Giải thích được vì sao yêu cầu (requirement / 요구사항) kỹ thuật (engineering / 엔지니어링) không phải chỉ “ghi lại yêu cầu”, mà gồm elicitation, phân tích (analysis / 분석), specification và kiểm tra hợp lệ (validation / 검증). Giải thích được functional yêu cầu (requirement / 요구사항), non-functional yêu cầu (requirement / 요구사항), feasibility và traceability.

### Distinguish

Phải phân biệt được:

- functional vs non-functional;
- xác minh (verification / 확인) vs kiểm tra hợp lệ (validation / 검증);
- DFD vs flowchart;
- dữ liệu (data / 데이터) Dictionary vs Mini-specification;
- stakeholder need vs hiện thực (implementation / 구현) detail;
- structural UML vs behavioral UML.

### Solve

Không nhìn tài liệu, tự phân loại 10 yêu cầu (requirement / 요구사항) tự đặt; với mỗi yêu cầu (requirement / 요구사항) chỉ ra kiểm thử (test / 테스트)/acceptance criterion phù hợp. Từ một scenario đơn giản, chọn đúng Use trường hợp (case / 사례), chuỗi (sequence / 시퀀스), Activity hoặc trạng thái (state / 상태) Diagram theo câu hỏi cần trả lời.

---

## 2. 화면 설계 — UI thiết kế (design / 설계)

### Explain

Giải thích wireframe, mockup, prototype, storyboard khác nhau về mục tiêu và fidelity. Giải thích usability không chỉ là “đẹp”, mà liên quan effectiveness, learnability, intuitiveness, consistency, phản hồi (feedback / 피드백) và khả năng tiếp cận (accessibility / 접근성) tùy taxonomy.

### Distinguish

Phải phân biệt được:

- CLI / GUI / NUI;
- wireframe / mockup / prototype / storyboard;
- usability vs khả năng tiếp cận (accessibility / 접근성);
- visual thiết kế (design / 설계) vs tương tác (interaction / 상호작용) luồng (flow / 흐름).

### Solve

Cho một yêu cầu “cần kiểm thử (test / 테스트) luồng (flow / 흐름) đăng ký trước khi mã (code / 코드) backend”, chọn sản phẩm tạo ra (artifact / 산출물) phù hợp và giải thích vì sao.

---

## 3. 애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)

### Explain

Giải thích mô-đun (module / 모듈) independence qua cohesion/coupling. Giải thích OOP, SOLID và mẫu thiết kế (design pattern / 디자인 패턴) như cơ chế quản lý variation/phụ thuộc (dependency / 의존성), không phải danh sách từ khóa.

### Distinguish

Phải phân biệt được:

- Functional/Sequential/Communicational/Procedural/Temporal/Logical/Coincidental cohesion;
- Content/dùng chung (common / 공통)/bên ngoài (external / 외부)/điều khiển (control / 제어)/Stamp/dữ liệu (data / 데이터) coupling;
- overloading vs overriding;
- composition vs aggregation;
- chiến lược (strategy / 전략) vs trạng thái (state / 상태);
- Adapter vs Facade;
- Decorator vs Proxy;
- Factory phương thức (method / 메서드) vs Abstract Factory;
- inheritance vs delegation/composition.

### Solve

Nhìn một phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) mô-đun (module / 모듈) và chỉ ra fan-in/fan-out. Nhìn scenario và chọn mẫu (pattern / 패턴) theo force. Nhìn mã (code / 코드) OOP và xác định polymorphism/encapsulation/vi phạm principle.

---

## 4. 인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계)

### Explain

Giải thích giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약) gồm dữ liệu (data / 데이터), giao thức (protocol / 프로토콜), lỗi (error / 오류) ngữ nghĩa (semantics / 의미론), chuỗi (sequence / 시퀀스) và tính tương thích (compatibility / 호환성). Giải thích point-to-point, EAI/ESB và lý do tích hợp (integration / 통합) độ phức tạp (complexity / 복잡도) tăng.

### Distinguish

Phải phân biệt được:

- synchronous vs asynchronous tương tác (interaction / 상호작용);
- yêu cầu (request / 요청) kiểm tra hợp lệ (validation / 검증) vs nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증);
- vận chuyển (transport / 전송) thất bại (failure / 실패) vs ứng dụng (application / 애플리케이션) lỗi (error / 오류);
- thử lại (retry / 재시도) vs idempotency;
- dữ liệu (data / 데이터) transformation vs routing.

### Solve

Thiết kế retry-safe cho một payment API; chỉ ra đâu cần idempotency key, giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) và lỗi (error / 오류) ánh xạ (mapping / 매핑).

---

# Môn 2 — 소프트웨어 개발

## 5. 데이터 입출력 구현 — dữ liệu (data / 데이터) I/O hiện thực (implementation / 구현)

### Explain

Giải thích abstract dữ liệu (data / 데이터) kiểu (type / 타입), ngăn xếp (stack / 스택), hàng đợi (queue / 큐), cây (tree / 트리), đồ thị (graph / 그래프), bảng băm (hash table / 해시 테이블) và thuật toán (algorithm / 알고리즘) độ phức tạp (complexity / 복잡도). Giải thích tại sao cấu trúc dữ liệu (data structure / 자료구조) quyết định thao tác (operation / 연산) chi phí (cost / 비용).

### Distinguish

Phải phân biệt được:

- ngăn xếp (stack / 스택) vs hàng đợi (queue / 큐);
- cây (tree / 트리) vs đồ thị (graph / 그래프);
- BFS vs DFS;
- BST vs vùng nhớ động (heap / 힙);
- tuyến tính (linear / 선형) tìm kiếm (search / 검색) vs tìm kiếm nhị phân (binary search / 이진 탐색);
- collision resolution strategies;
- thời gian (time / 시간) độ phức tạp (complexity / 복잡도) vs actual elapsed thời gian (time / 시간).

### Solve

Dấu vết (trace / 추적) postfix expression, BFS/DFS, tìm kiếm nhị phân (binary search / 이진 탐색), băm (hash / 해시) insertion và ít nhất một sorting tiến trình (process / 프로세스).

---

## 6. 통합 구현 — tích hợp (integration / 통합) hiện thực (implementation / 구현)

### Explain

Giải thích dữ liệu (data / 데이터)/giao diện (interface / 인터페이스) tích hợp (integration / 통합) từ ánh xạ (mapping / 매핑), transformation, kiểm tra hợp lệ (validation / 검증) tới lỗi (error / 오류) handling. Hiểu rằng tích hợp (integration / 통합) bài toán (problem / 문제) có lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) và operational dimensions.

### Distinguish

Phân biệt:

- lược đồ (schema / 스키마) mismatch vs vận chuyển (transport / 전송) thất bại (failure / 실패);
- batch tích hợp (integration / 통합) vs real-time tích hợp (integration / 통합);
- adapter/connector vs lô-gic nghiệp vụ (business logic / 비즈니스 로직);
- dữ liệu (data / 데이터) ánh xạ (mapping / 매핑) vs dữ liệu (data / 데이터) cleansing.

### Solve

Cho hai lược đồ (schema / 스키마) khác nhau, tự viết ánh xạ (mapping / 매핑) quy tắc (rule / 규칙) và kiểm tra hợp lệ (validation / 검증) quy tắc (rule / 규칙); chỉ ra cách xử lý missing/invalid trường dữ liệu (field / 필드).

---

## 7. 제품 소프트웨어 패키징 — sản phẩm (product / 제품) Software Packaging

### Explain

Giải thích packaging, bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물), phụ thuộc (dependency / 의존성), manual, phiên bản (version / 버전) và cấu hình (configuration / 구성) item. Hiểu DRM/license và phân phối (distribution / 분포) integrity ở mức khái niệm.

### Distinguish

Phân biệt:

- phiên bản (version / 버전) điều khiển (control / 제어) vs cấu hình (configuration / 구성) management;
- hiện vật bản dựng (build artifact / 빌드 산출물) vs nguồn (source / 소스);
- checksum/integrity vs authentication/authorization;
- backup sản phẩm tạo ra (artifact / 산출물) vs bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물).

### Solve

Từ nguồn (source / 소스) tới deployable gói (package / 패키지), liệt kê siêu dữ liệu (metadata / 메타데이터)/phụ thuộc (dependency / 의존성)/cấu hình (config / 설정)/manual cần quản lý và cách verify gói (package / 패키지) không bị corrupt.

---

## 8. 애플리케이션 테스트 관리 — ứng dụng (application / 애플리케이션) kiểm thử (test / 테스트) Management

### Explain

Giải thích kiểm thử (test / 테스트) mức (level / 수준), black-box, white-box, regression, tích hợp (integration / 통합) và acceptance. Hiểu kiểm thử (test / 테스트) oracle, coverage và defect vòng đời (lifecycle / 생명주기) ở mức cơ chế.

### Distinguish

Phân biệt:

- đơn vị (unit / 단위)/tích hợp (integration / 통합)/hệ thống (system / 시스템)/acceptance;
- black-box/white-box;
- equivalence partition/ranh giới (boundary / 경계) giá trị (value / 값);
- statement/branch/đường dẫn (path / 경로) coverage;
- stub/driver;
- xác minh (verification / 확인)/kiểm tra hợp lệ (validation / 검증);
- alpha/beta;
- regression/retest.

### Solve

Tính Cyclomatic độ phức tạp (complexity / 복잡도), chọn black-box cases ở ranh giới (boundary / 경계), thiết kế top-down/bottom-up tích hợp (integration / 통합) setup.

---

## 9. 인터페이스 구현 — giao diện (interface / 인터페이스) hiện thực (implementation / 구현)

### Explain

Giải thích đặc tả hợp đồng (contract / 계약) hiện thực (implementation / 구현), serialization, kiểm tra hợp lệ (validation / 검증), lỗi (error / 오류) handling, logging và interoperability.

### Distinguish

Phân biệt:

- cú pháp (syntax / 문법)/lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) vs ngữ nghĩa (semantic / 의미적)/nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증);
- hết thời gian chờ (timeout / 타임아웃) vs ứng dụng (application / 애플리케이션) rejection;
- retryable vs non-retryable lỗi (error / 오류);
- serialization lỗi (error / 오류) vs dữ liệu (data / 데이터) integrity lỗi (error / 오류).

### Solve

Cho API payload và lỗi (error / 오류) ma trận (matrix / 행렬), xác định nơi validate và phản hồi (response / 응답) category phù hợp.

---

# Môn 3 — 데이터베이스 구축

## 10. 논리 데이터베이스 설계 — Logical cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)

### Explain

Giải thích relational mô hình (model / 모델), key, functional phụ thuộc (dependency / 의존성), normalization và integrity các ràng buộc (constraints / 제약조건들).

### Distinguish

Phân biệt:

- super key / candidate key / primary key / alternate key / foreign key;
- selection / projection / phép nối (join / 조인) / division;
- partial / transitive phụ thuộc (dependency / 의존성);
- 1NF / 2NF / 3NF / BCNF;
- thực thể (entity / 엔터티) integrity / referential integrity / lĩnh vực (domain / 도메인) integrity.

### Solve

Tính attribute closure, tìm candidate key, normalize một quan hệ (relation / 관계) tới ít nhất 3NF/BCNF khi phù hợp và kiểm lossless lập luận (reasoning / 추론) cơ bản.

---

## 11. 물리 데이터베이스 설계 — vật lý (physical / 물리적) cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)

### Explain

Giải thích chỉ mục (index / 인덱스), lưu trữ (storage / 저장소), partition, clustering/organization và denormalization như vật lý (physical / 물리적) decisions dựa trên tải công việc (workload / 워크로드).

### Distinguish

Phân biệt:

- logical lược đồ (schema / 스키마) vs vật lý (physical / 물리적) thiết kế (design / 설계);
- B+cây (tree / 트리) vs băm (hash / 해시) cho equality/phạm vi (range / 범위);
- normalization vs denormalization;
- selectivity vs cardinality;
- clustered concept vs secondary chỉ mục (index / 인덱스) theo DBMS-specific hiện thực (implementation / 구현).

### Solve

Nhìn truy vấn (query / 쿼리) mẫu (pattern / 패턴) và đề xuất chỉ mục (index / 인덱스) key thứ tự (order / 순서) có lý do; giải thích ghi (write / 쓰기) chi phí (cost / 비용) và cases chỉ mục (index / 인덱스) không được dùng hiệu quả.

---

## 12. SQL 활용 — SQL Utilization

### Explain

Giải thích logical truy vấn (query / 쿼리) processing: FROM/phép nối (join / 조인) → WHERE → GROUP BY → HAVING → SELECT → thứ tự (order / 순서) BY như mô hình tư duy (mental model / 사고 모델).

### Distinguish

Phân biệt:

- WHERE vs HAVING;
- INNER vs LEFT/RIGHT/FULL OUTER phép nối (join / 조인);
- `COUNT(*)` vs `COUNT(column)`;
- subquery vs phép nối (join / 조인) theo ngữ nghĩa (semantics / 의미론);
- NULL vs empty string/giá trị (value / 값) 0;
- UNION vs UNION ALL.

### Solve

Tự viết truy vấn (query / 쿼리) có phép nối (join / 조인) + aggregate + HAVING; dự đoán kết quả (result / 결과) khi có NULL và unmatched rows.

---

## 13. SQL 응용 — SQL ứng dụng (application / 애플리케이션)

### Explain

Giải thích giao dịch (transaction / 트랜잭션), ACID, tính đồng thời (concurrency / 동시성) anomaly, locking/isolation và khôi phục (recovery / 복구).

### Distinguish

Phân biệt:

- dirty read / non-repeatable read / phantom;
- dùng chung (shared / 공유)/exclusive khóa (lock / 잠금) concept;
- deadlock vs starvation;
- serial schedule vs serializable schedule;
- undo vs redo;
- checkpoint vs backup.

### Solve

Vẽ precedence đồ thị (graph / 그래프) cho schedule; xác định conflict-serializability; nhận diện anomaly từ timeline; lập luận (reasoning / 추론) khóa (lock / 잠금) thứ tự (ordering / 순서)/deadlock.

---

## 14. 데이터 전환 — dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션)/Conversion

### Explain

Giải thích extract, transform, tải (load / 로드)/migrate, kiểm tra hợp lệ (validation / 검증), reconciliation và cutover. Hiểu di chuyển (migration / 마이그레이션) là tính đúng đắn (correctness / 정확성) + operational chuyển tiếp (transition / 전이) bài toán (problem / 문제).

### Distinguish

Phân biệt:

- lược đồ (schema / 스키마) ánh xạ (mapping / 매핑) vs dữ liệu (data / 데이터) cleansing;
- di chuyển (migration / 마이그레이션) vs replication;
- kiểm tra hợp lệ (validation / 검증) vs reconciliation;
- full cutover vs staged/parallel chiến lược (strategy / 전략).

### Solve

Thiết kế checklist di chuyển (migration / 마이그레이션) có row counts, các ràng buộc (constraints / 제약조건들), sampled/nghiệp vụ (business / 비즈니스) reconciliation, quay lui (rollback / 롤백)/cutover criteria.

---

# Môn 4 — 프로그래밍 언어 활용

## 15. 서버 프로그램 구현 — máy chủ (server / 서버) Program hiện thực (implementation / 구현)

### Explain

Giải thích vòng đời yêu cầu (request lifecycle / 요청 생명주기), tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드), trạng thái dùng chung (shared state / 공유 상태), synchronization và máy chủ (server / 서버) tính đồng thời (concurrency / 동시성).

### Distinguish

Phân biệt:

- tiến trình (process / 프로세스) vs luồng thực thi (thread / 스레드);
- tính đồng thời (concurrency / 동시성) vs parallelism;
- race điều kiện (condition / 조건) vs deadlock;
- mutex vs semaphore;
- blocking vs non-blocking ở mức khái niệm.

### Solve

Nhìn mã (code / 코드) increment dùng chung (shared / 공유) counter và chỉ ra race; chọn synchronization ranh giới (boundary / 경계) hợp lý trong single-process và multi-instance hệ thống (system / 시스템).

---

## 16. 프로그래밍 언어 활용 — Programming ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)

### Explain

Hiểu evaluation/trạng thái (state / 상태) thay đổi (change / 변경) trong C, Java, Python thay vì học đầu ra (output / 출력) mẫu (pattern / 패턴) máy móc.

### Distinguish

Phân biệt:

- C pointer vs pointed giá trị (value / 값);
- pre-increment vs post-increment;
- Java overloading vs overriding;
- tham chiếu (reference / 참조) kiểu (type / 타입) vs thời gian chạy (runtime / 런타임) đối tượng (object / 객체);
- Python mutable vs immutable đối tượng (object / 객체);
- alias vs bản sao (copy / 복사).

### Solve

Dấu vết (trace / 추적) mã (code / 코드) C pointer/array, Java động (dynamic / 동적) dispatch và Python alias/mutation từng line bằng bảng variable trạng thái (state / 상태).

---

## 17. 응용 SW 기초 기술 활용 — OS / mạng (network / 네트워크) / Basic hạ tầng (infrastructure / 인프라)

### Explain

Giải thích CPU scheduling, deadlock, virtual bộ nhớ (memory / 메모리), page replacement, TCP/IP, subnetting và routing.

### Distinguish

Phân biệt:

- FCFS / SJF / Round Robin;
- waiting / turnaround / phản hồi (response / 응답) thời gian (time / 시간);
- FIFO / LRU page replacement;
- page fault vs thrashing;
- TCP vs UDP;
- IP address / subnet / gateway / DNS;
- mạng (network / 네트워크) prefix vs host bits;
- shortest đường dẫn (path / 경로) concept vs longest-prefix routing match.

### Solve

Tính scheduling timeline, page faults, subnet mạng (network / 네트워크)/broadcast/usable phạm vi (range / 범위) và longest-prefix tuyến (route / 경로).

---

# Môn 5 — 정보시스템 구축 관리

## 18. 소프트웨어 개발 방법론 활용 — Software Development Methodology

### Explain

Giải thích vòng đời (lifecycle / 생명주기)/methodology, estimation, schedule/rủi ro (risk / 위험)/thay đổi (change / 변경). Hiểu rằng Agile/Waterfall là cách tổ chức phản hồi (feedback / 피드백)/thay đổi (change / 변경) khác nhau chứ không phải “mới vs cũ” đơn giản.

### Distinguish

Phân biệt:

- Waterfall vs iterative/agile;
- dự án (project / 프로젝트) activity duration vs đường dẫn (path / 경로) duration;
- đường găng (critical path / 임계 경로) vs non-critical đường dẫn (path / 경로);
- estimate vs commitment;
- rủi ro (risk / 위험) vs issue.

### Solve

Tính PERT expected thời gian (time / 시간), đường găng (critical path / 임계 경로) đơn giản và impact khi activity trọng yếu (critical / 중요) delay.

---

## 19. IT 프로젝트 정보시스템 구축관리 — IT dự án (project / 프로젝트) / hạ tầng (infrastructure / 인프라) Construction Management

### Explain

Giải thích compute/lưu trữ (storage / 저장소)/mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스)/cloud hạ tầng (infrastructure / 인프라), redundancy, sức chứa (capacity / 용량) và miền lỗi (failure domain / 장애 도메인).

### Distinguish

Phân biệt:

- RAID 0/1/5/6;
- redundancy vs backup;
- replication vs backup;
- vertical vs horizontal scaling;
- IaaS/PaaS/SaaS;
- VM vs bộ chứa (container / 컨테이너);
- high availability vs disaster khôi phục (recovery / 복구);
- RTO vs RPO.

### Solve

Tính RAID usable sức chứa (capacity / 용량), chọn kiến trúc (architecture / 아키텍처) theo RTO/RPO scenario và chỉ ra single điểm (point / 지점) of thất bại (failure / 실패).

---

## 20. 소프트웨어 개발 보안 구축 — Software Development bảo mật (security / 보안)

### Explain

Giải thích secure SDLC, đầu vào (input / 입력) handling, authentication, authorization, secrets và dùng chung (common / 공통) ứng dụng (application / 애플리케이션) vulnerabilities.

### Distinguish

Phân biệt:

- authentication vs authorization;
- SQL Injection vs XSS;
- parameterized truy vấn (query / 쿼리) vs escaping;
- hashing vs encryption;
- symmetric vs asymmetric encryption;
- confidentiality/integrity/authenticity;
- threat/vulnerability/rủi ro (risk / 위험)/điều khiển (control / 제어).

### Solve

Cho attack scenario, chọn root-cause mitigation và defense-in-depth controls; giải thích vì sao điều khiển (control / 제어) ở sai tầng (layer / 계층) không xử lý nguyên nhân.

---

## 21. 시스템 보안 구축 — hệ thống (system / 시스템) bảo mật (security / 보안) Construction

### Explain

Giải thích mạng (network / 네트워크)/hệ thống (system / 시스템) bảo mật (security / 보안) controls, firewall, IDS/IPS, VPN/TLS, kiểm soát truy cập (access control / 접근 제어), logging/monitoring, patching và sự cố (incident / 인시던트)/khôi phục (recovery / 복구).

### Distinguish

Phân biệt:

- firewall vs WAF;
- IDS vs IPS;
- TLS vs VPN;
- detection vs prevention;
- preventive/detective/corrective điều khiển (control / 제어);
- availability cơ chế (mechanism / 메커니즘) vs bảo mật (security / 보안) monitoring.

### Solve

Với một kiến trúc (architecture / 아키텍처) có Internet → LB → Web → App → DB, đặt trust ranh giới (boundary / 경계) và đề xuất controls theo tầng (layer / 계층) mà không biến thành “gắn firewall ở mọi nơi”.

---

# Cross-Chapter Recall — 30 câu không nhìn tài liệu

1. yêu cầu (requirement / 요구사항) “phản hồi (response / 응답) < 1s” sẽ nối sang kiểm thử (test / 테스트) kiểu (type / 타입) và operational chỉ số (metric / 지표) nào?
2. Vì sao chuỗi (sequence / 시퀀스) Diagram và Activity Diagram có thể cùng mô tả một nghiệp vụ nhưng trả lời câu hỏi khác nhau?
3. Stamp Coupling khác dữ liệu (data / 데이터) Coupling ở ranh giới (boundary / 경계) nào?
4. chiến lược (strategy / 전략) khác trạng thái (state / 상태) ở nguồn quyết định hành vi (behavior / 동작) nào?
5. thử lại (retry / 재시도) vì hết thời gian chờ (timeout / 타임아웃) có thể tạo duplicate nghiệp vụ (business / 비즈니스) side tác động (effect / 효과) thế nào?
6. Tại sao BFS tìm shortest đường dẫn (path / 경로) unweighted nhưng DFS không bảo đảm?
7. Vì sao tìm kiếm nhị phân (binary search / 이진 탐색) cần thứ tự (ordering / 순서)?
8. tuyến tính (linear / 선형) Probing tạo primary clustering bằng cơ chế nào?
9. Branch Coverage khác ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석) ở góc nhìn nội bộ (internal / 내부)/bên ngoài (external / 외부) thế nào?
10. Vì sao checksum không thay thế digital signature/authentication?
11. Tại sao candidate key phải minimal?
12. Tại sao 2NF chủ yếu trở nên đáng chú ý khi candidate key composite?
13. B+cây (tree / 트리) hỗ trợ phạm vi (range / 범위) tốt hơn băm (hash / 해시) bằng cơ chế nào?
14. `WHERE` và `HAVING` xảy ra ở logical phase nào?
15. `COUNT(*)` và `COUNT(col)` khác nhau khi NULL thế nào?
16. Non-repeatable read khác phantom read ở đơn vị (unit / 단위) thay đổi nào?
17. Cycle trong precedence đồ thị (graph / 그래프) chứng minh điều gì?
18. Race điều kiện (condition / 조건) ở ứng dụng (application / 애플리케이션) khác lost cập nhật (update / 업데이트) ở DB thế nào và giống nhau ở bản chất nào?
19. Quantum quá nhỏ trong Round Robin có chi phí (cost / 비용) gì?
20. FIFO và LRU chọn victim theo thông tin (information / 정보) nào?
21. `/27` để lại bao nhiêu host bit?
22. Longest-prefix match vì sao chọn tuyến (route / 경로) cụ thể nhất?
23. Java overriding khác overloading về dispatch thế nào?
24. Python alias của mutable danh sách (list / 목록) gây tác động (effect / 효과) gì?
25. đường găng (critical path / 임계 경로) quyết định dự án (project / 프로젝트) duration trong mô hình (model / 모델) thế nào?
26. RAID5 và backup bảo vệ các dạng thất bại (failure mode / 실패 모드) khác nhau ra sao?
27. RTO và RPO trả lời hai câu hỏi khác nhau nào?
28. TLS bảo vệ channel nhưng không thay authorization ra sao?
29. SQL Injection và XSS có nguyên nhân gốc (root cause / 근본 원인)/mitigation khác nhau thế nào?
30. cấu hình (configuration / 구성) Management rộng hơn Git phiên bản (version / 버전) điều khiển (control / 제어) ở đâu?

---

# 과락 방지 — Fail-Safe kiểm tra (audit / 감사)

Vì mỗi môn có ngưỡng riêng, không được coi tổng điểm cao ở một môn có thể “bù” hoàn toàn cho môn yếu. Trước khi làm mock cuối, mỗi môn cần có tối thiểu:

```text
Môn 1: E+D+S cho 4/4 chapter
Môn 2: E+D+S cho 5/5 chapter
Môn 3: E+D+S cho 5/5 chapter
Môn 4: E+D+S cho 3/3 chapter
Môn 5: E+D+S cho 4/4 chapter
```

Nếu một chapter thiếu `S`, ưu tiên Procedural Workbook. Nếu thiếu `D`, quay lại confusion pairs trong deep-dive. Nếu thiếu `E`, quay lại explanation gốc trong Master Guide/deep-dive và tự nói lại bằng lời của mình.

---

# Definition of Done

Bạn có thể coi toàn bộ nhánh học (track / 트랙) 2026 đạt coverage khi:

- 21 chapter đều có E+D+S;
- 30 cross-chapter recall questions trả lời được mà không mở tài liệu;
- Procedural Workbook không còn dạng bài “biết lý thuyết nhưng không làm được”;
- Full Mock không có môn dưới 8/20;
- mọi câu sai được truy ngược về một concept/procedure cụ thể và sửa ở tệp (file / 파일) nguồn, không chỉ học đáp án.
