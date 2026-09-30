# 정보처리기사 필기 2026 — Advanced Scenario Labs

> Đây là lớp luyện **lập luận (reasoning / 추론) nhiều bước**. Mỗi scenario được thiết kế để có nhiều khái niệm đúng cùng xuất hiện, nhưng bạn phải xác định **primary concept**, **cơ chế (mechanism / 메커니즘)**, **sự đánh đổi (trade-off / 트레이드오프)** và **bẫy wording**. Không xem phần phân tích trước khi tự trả lời.

---

# Môn 1 — 소프트웨어 설계

## Lab 1 — yêu cầu (requirement / 요구사항) đúng nhưng sản phẩm vẫn thất bại

### Scenario

Stakeholder yêu cầu “hệ thống cho phép xuất báo cáo PDF”. nhóm (team / 팀) viết spec đúng câu đó, mã (code / 코드) đúng spec, kiểm thử (test / 테스트) pass. Sau bản phát hành (release / 릴리스), người dùng nói họ thực ra cần CSV để import vào ERP; PDF gần như vô dụng.

### Tự trả lời

1. xác minh (verification / 확인) có pass không?
2. kiểm tra hợp lệ (validation / 검증) có pass không?
3. Sai ở phase nào của yêu cầu (requirement / 요구사항) kỹ thuật (engineering / 엔지니어링)?
4. Traceability có tự giải quyết vấn đề này không?

### Phân tích

Xác minh (verification / 확인) có thể pass vì hiện thực (implementation / 구현) đúng spec. kiểm tra hợp lệ (validation / 검증) thất bại (fail / 실패) vì spec không phản ánh need thật.

Traceability chỉ giúp lần theo yêu cầu (requirement / 요구사항) → thiết kế (design / 설계) → mã (code / 코드) → kiểm thử (test / 테스트); nếu yêu cầu (requirement / 요구사항) gốc sai thì traceability vẫn có thể hoàn hảo nhưng dẫn tới sai mục tiêu.

Nguyên nhân gốc (root cause / 근본 원인) gần yêu cầu (requirement / 요구사항) elicitation/phân tích (analysis / 분석)/kiểm tra hợp lệ (validation / 검증) hơn là coding.

### Bẫy

Đừng chọn “đơn vị (unit / 단위) kiểm thử (test / 테스트) thiếu” chỉ vì sản phẩm không hữu ích. Đây là **right sản phẩm (product / 제품) vs sản phẩm (product / 제품) built right**.

---

## Lab 2 — mô-đun (module / 모듈) phụ thuộc (dependency / 의존성) nhìn tưởng sạch nhưng vẫn coupling cao

### Scenario

`OrderService` chỉ gọi một phương thức (method / 메서드) duy nhất:

```text
LegacyFacade.process(order, mode, retryFlag, regionCode, dbShard, debugFlag)
```

Nhóm (team / 팀) nói fan-out chỉ bằng 1 nên coupling thấp.

### Tự trả lời

1. Fan-out thấp có chứng minh coupling thấp không?
2. Những parameter nào có thể cho thấy điều khiển (control / 제어)/bên ngoài (external / 외부) coupling?
3. Facade có tự động làm kiến trúc tốt không?

### Phân tích

Fan-out chỉ đo số phụ thuộc (dependency / 의존성) trực tiếp, không đo chất lượng phụ thuộc (dependency / 의존성).

`mode`, `retryFlag`, `debugFlag` có thể là điều khiển (control / 제어) coupling nếu caller điều khiển hành vi (behavior / 동작) nội bộ của callee.

`regionCode`, `dbShard` có thể leak hạ tầng (infrastructure / 인프라) concern lên nghiệp vụ (business / 비즈니스) tầng (layer / 계층).

Facade giảm số entry points nhưng có thể trở thành “god facade” nếu giao diện (interface / 인터페이스) gom quá nhiều điều khiển (control / 제어) detail.

### Insight

Chỉ số (metric / 지표) structural không thay ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석).

---

## Lab 3 — chiến lược (strategy / 전략) hay trạng thái (state / 상태)?

### Scenario

Một shipping calculator có ba thuật toán (algorithm / 알고리즘): `Normal`, `Express`, `International`. người dùng (user / 사용자) hoặc chính sách (policy / 정책) engine chọn thuật toán (algorithm / 알고리즘) khi tạo shipment.

Một thứ tự (order / 순서) khác có hành vi (behavior / 동작) thay đổi theo vòng đời (lifecycle / 생명주기) `CREATED → PAID → SHIPPED → DELIVERED`.

### Tự trả lời

Mẫu (pattern / 패턴) nào phù hợp từng trường hợp (case / 사례)? Vì sao lớp (class / 클래스) diagram có thể trông giống nhau?

### Phân tích

Shipping algorithms → chiến lược (strategy / 전략): chính sách (policy / 정책)/thuật toán (algorithm / 알고리즘) interchangeable.

Thứ tự (order / 순서) vòng đời (lifecycle / 생명주기) → trạng thái (state / 상태): hành vi (behavior / 동작) thay đổi theo trạng thái nội bộ (internal state / 내부 상태) chuyển tiếp (transition / 전이).

Cả hai có thể dùng giao diện (interface / 인터페이스) + concrete implementations, nên không thể chọn mẫu (pattern / 패턴) chỉ từ shape lớp (class / 클래스) diagram.

---

## Lab 4 — Adapter hay Facade hay Anti-corruption tầng (layer / 계층)?

### Scenario

Hệ thống mới dùng `Customer(id, name, email)`. Legacy CRM trả `CUST_NO`, `NM`, `MAIL_ADDR`, nhiều trường dữ liệu (field / 필드) khác và ngữ nghĩa (semantics / 의미론) khác đôi chút.

### Tự trả lời

1. Nếu chỉ đổi phương thức (method / 메서드)/giao diện (interface / 인터페이스) shape, mẫu (pattern / 패턴) nào gần nhất?
2. Nếu cần translate cả mô hình (model / 모델)/ngữ nghĩa (semantics / 의미론) để lĩnh vực (domain / 도메인) mới không bị legacy mô hình (model / 모델) “nhiễm”, vấn đề sâu hơn là gì?
3. Facade có phải đáp án tốt nhất nếu câu hỏi nhấn “incompatible giao diện (interface / 인터페이스)” không?

### Phân tích

Nếu chỉ giao diện (interface / 인터페이스) mismatch → Adapter.

Nếu cần cô lập mô hình ngữ nghĩa (semantic model / 의미 모델) legacy khỏi lĩnh vực (domain / 도메인) mới, tư duy gần anti-corruption tầng (layer / 계층)/lĩnh vực (domain / 도메인) ranh giới (boundary / 경계) hơn, dù thuật ngữ này có thể ngoài trọng tâm đề.

Nếu đề nhấn subsystem độ phức tạp (complexity / 복잡도) → Facade. Nếu nhấn mismatch → Adapter.

---

## Lab 5 — Retry-safe giao diện (interface / 인터페이스)

### Scenario

Máy khách (client / 클라이언트) gửi `POST /payments`, máy chủ (server / 서버) charge thành công nhưng phản hồi (response / 응답) bị mất. máy khách (client / 클라이언트) thử lại (retry / 재시도).

### Tự trả lời

1. hết thời gian chờ (timeout / 타임아웃) có chứng minh máy chủ (server / 서버) chưa xử lý không?
2. Idempotency key nên thuộc yêu cầu (request / 요청) định danh (identity / 식별자) hay session định danh (identity / 식별자)?
3. Unique ràng buộc (constraint / 제약조건) có thể đóng vai trò gì?
4. giao dịch (transaction / 트랜잭션) cần bao quanh những gì?

### Phân tích

Hết thời gian chờ (timeout / 타임아웃) chỉ nói máy khách (client / 클라이언트) không nhận phản hồi (response / 응답) trong thời gian chờ; máy chủ (server / 서버) có thể đã lần ghi nhận (commit / 커밋).

Idempotency key nên đại diện logical thao tác (operation / 연산). máy chủ (server / 서버) cần bảo đảm cùng key không tạo duplicate side tác động (effect / 효과).

Một thiết kế (design / 설계) mạnh là lưu yêu cầu (request / 요청) định danh (identity / 식별자) + kết quả (result / 결과) trong cùng giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) với side tác động (effect / 효과) hoặc dùng bất biến (invariant / 불변식) tương đương. Unique ràng buộc (constraint / 제약조건) giúp concurrent duplicate requests không cùng “thắng”.

---

# Môn 2 — 소프트웨어 개발

## Lab 6 — Chọn cấu trúc dữ liệu (data structure / 자료구조) từ thao tác (operation / 연산) mẫu (pattern / 패턴)

### Scenario

Một dịch vụ (service / 서비스) cần:

- insert sự kiện (event / 이벤트) liên tục;
- luôn lấy sự kiện (event / 이벤트) có priority nhỏ nhất;
- không cần iterate toàn bộ theo sorted thứ tự (order / 순서);
- không cần arbitrary lookup theo key.

### Tự trả lời

Chọn BST, bảng băm (hash table / 해시 테이블), hàng đợi (queue / 큐) hay min-heap?

### Phân tích

Min-heap phù hợp vì thao tác (operation / 연산) trọng tâm là insert + extract-min.

BST cũng có thể hỗ trợ min, nhưng vùng nhớ động (heap / 힙) trực tiếp tối ưu cho priority hàng đợi (queue / 큐) lớp trừu tượng (abstraction / 추상화). bảng băm (hash table / 해시 테이블) không giữ thứ tự (ordering / 순서); FIFO hàng đợi (queue / 큐) không xét priority.

### Bẫy

Đừng chọn cấu trúc (structure / 구조) chỉ vì nó “nhanh” tổng quát. Chọn theo thao tác (operation / 연산) mix.

---

## Lab 7 — tìm kiếm nhị phân (binary search / 이진 탐색) sai dù mã (code / 코드) nhìn đúng

### Scenario

Nhóm (team / 팀) dùng tìm kiếm nhị phân (binary search / 이진 탐색) trên array `[8, 3, 12, 1, 20]` và đôi khi không tìm thấy giá trị (value / 값) tồn tại.

### Phân tích

Tìm kiếm nhị phân (binary search / 이진 탐색) dựa bất biến (invariant / 불변식) rằng tìm kiếm (search / 검색) không gian (space / 공간) được ordered theo comparator tương thích. Không có thứ tự (ordering / 순서), bước loại bỏ nửa tìm kiếm (search / 검색) không gian (space / 공간) không hợp lệ.

Nguyên nhân gốc (root cause / 근본 원인) không phải off-by-one trước tiên mà là violated precondition.

---

## Lab 8 — Coverage cao nhưng bug vẫn lọt

### Scenario

Một hàm (function / 함수) có 100% statement coverage nhưng điều kiện (condition / 조건) `a && b` chỉ được kiểm thử (test / 테스트) với `(true,true)` và `(false,false)`.

### Tự trả lời

1. 100% statement coverage chứng minh điều gì?
2. Nó có chứng minh mọi branch/điều kiện (condition / 조건) combination đã kiểm thử (test / 테스트) không?
3. kiểm thử (test / 테스트) nào nên thêm?

### Phân tích

Statement coverage chỉ chứng minh mỗi statement đã execute ít nhất một lần.

Cần xét branch/điều kiện (condition / 조건) coverage tùy mục tiêu. Cases `(true,false)` và `(false,true)` có thể phơi lộ lô-gic (logic / 논리) bug bị statement coverage bỏ qua.

---

## Lab 9 — Regression hay Retest?

### Scenario

Bug: discount mã (code / 코드) `SAVE10` không áp dụng cho thứ tự (order / 순서) trên 100,000 won. Dev sửa bug.

Nhóm (team / 팀) chạy:

- kiểm thử (test / 테스트) đúng trường hợp (case / 사례) `SAVE10 + 150,000`;
- kiểm thử (test / 테스트) các mã (code / 코드) khác;
- kiểm thử (test / 테스트) checkout không discount;
- kiểm thử (test / 테스트) refund sau checkout.

### Phân tích

Trường hợp (case / 사례) đầu là retest trực tiếp defect.

Các kiểm thử (test / 테스트) còn lại là regression để xem fix có phá hành vi (behavior / 동작) liên quan không.

Một kiểm thử (test / 테스트) session có thể chứa cả hai loại.

---

## Lab 10 — gói (package / 패키지) integrity nhưng nguồn (source / 소스) không đáng tin

### Scenario

Một installer tải về có SHA-256 đúng với băm (hash / 해시) đăng trên cùng website vừa bị compromise.

### Tự trả lời

Băm (hash / 해시) check đã bảo vệ điều gì? Điều gì vẫn thiếu?

### Phân tích

Băm (hash / 해시) giúp phát hiện mismatch giữa tệp (file / 파일) và expected digest, nhưng nếu attacker kiểm soát cả tệp (file / 파일) và digest thì authenticity không được đảm bảo.

Digital signature/trusted phân phối (distribution / 분포) chuỗi (chain / 사슬) giải bài định danh (identity / 식별자)/authenticity tốt hơn.

### Insight

Integrity check chỉ mạnh bằng trust nguồn (source / 소스) của expected giá trị (value / 값).

---

# Môn 3 — 데이터베이스 구축

## Lab 11 — Candidate key không nhìn từ FD bằng mắt

### Scenario

Quan hệ (relation / 관계):

```text
R(A,B,C,D,E)
```

FDs:

```text
A → B
B → C
CD → E
E → D
```

### Tự làm

Tìm một candidate key.

### Gợi ý

`A+ = {A,B,C}` chưa có D/E.

Thử `AD+`:

```text
A → B → C
C,D → E
```

Vậy `AD+ = {A,B,C,D,E}`.

Có bỏ A được không? `D+` không ra A/B/C.

Có bỏ D được không? `A+` không ra D/E.

`AD` là candidate key.

Nhưng vì `E → D`, thử `AE`:

A → B → C và E → D → từ C,D suy E vốn đã có.

`AE` cũng là candidate key.

### Insight

Một quan hệ (relation / 관계) có thể có nhiều candidate keys. Đừng dừng ở superkey đầu tiên.

---

## Lab 12 — 3NF nhưng chưa BCNF

### Scenario

Quan hệ (relation / 관계) `R(Student, Course, Instructor)` với FDs:

```text
(Student, Course) → Instructor
Instructor → Course
```

Candidate keys gồm `(Student, Course)` và `(Student, Instructor)`.

### Tự trả lời

`Instructor → Course` vi phạm BCNF không? 3NF thì sao?

### Phân tích

`Instructor` không phải superkey → vi phạm BCNF.

Nhưng `Course` là prime attribute vì nằm trong candidate key `(Student, Course)`, nên FD này có thể vẫn thỏa 3NF theo formal điều kiện (condition / 조건).

### Insight

Đây là kiểu trường hợp (case / 사례) cho thấy 3NF và BCNF không đồng nghĩa.

---

## Lab 13 — chỉ mục (index / 인덱스) đúng cột nhưng sai thứ tự

### Scenario

Truy vấn (query / 쿼리) chính:

```sql
SELECT id, created_at
FROM orders
WHERE customer_id = ?
  AND created_at >= ?
ORDER BY created_at DESC
LIMIT 20;
```

Hai chỉ mục (index / 인덱스):

```text
I1(created_at, customer_id)
I2(customer_id, created_at)
```

### Tự trả lời

Chỉ mục (index / 인덱스) nào thường tự nhiên hơn và vì sao?

### Phân tích

`I2(customer_id, created_at)` thường phù hợp hơn vì equality trên `customer_id` tạo một ordered phạm vi (range / 범위) nhỏ theo `created_at`.

`I1` bắt đầu bằng thời gian (time / 시간), có thể phải scan nhiều customer trong thời gian (time / 시간) phạm vi (range / 범위) rồi filter.

DBMS optimizer/cardinality có thể làm quyết định cụ thể khác, nhưng đây là lập luận (reasoning / 추론) access-pattern cơ bản.

---

## Lab 14 — LEFT phép nối (join / 조인) bị biến thành INNER phép nối (join / 조인) ngoài ý muốn

### Scenario
Phần “Scenario” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```sql
SELECT c.id, o.id
FROM customer c
LEFT JOIN orders o
  ON o.customer_id = c.id
WHERE o.status = 'PAID';
```

Nhóm (team / 팀) kỳ vọng customer chưa có thứ tự (order / 순서) vẫn xuất hiện.

### Phân tích

Unmatched row có `o.status = NULL`. `WHERE o.status='PAID'` loại row đó, nên ngữ nghĩa (semantics / 의미론) gần INNER phép nối (join / 조인) cho điều kiện (condition / 조건) này.

Nếu mục tiêu là giữ mọi customer và chỉ match paid orders:

```sql
LEFT JOIN orders o
  ON o.customer_id = c.id
 AND o.status = 'PAID'
```

### Insight

Vị trí predicate ảnh hưởng outer phép nối (join / 조인) ngữ nghĩa (semantics / 의미론).

---

## Lab 15 — Lost cập nhật (update / 업데이트) và optimistic tính đồng thời (concurrency / 동시성)

### Scenario

Row:

```text
account(id=1, balance=100, version=7)
```

T1 và T2 cùng đọc balance 100, phiên bản (version / 버전) 7.

T1 muốn -20; T2 muốn -30.

### Tự thiết kế

Dùng optimistic versioning để tránh lost cập nhật (update / 업데이트).

### Phân tích
Phần “Phân tích” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```sql
UPDATE account
SET balance = 80,
    version = 8
WHERE id = 1
  AND version = 7;
```

T1 cập nhật (update / 업데이트) 1 row.

T2 sau đó:

```sql
UPDATE account
SET balance = 70,
    version = 8
WHERE id = 1
  AND version = 7;
```

Cập nhật (update / 업데이트) 0 row → phát hiện concurrent modification, phải thử lại (retry / 재시도)/recompute trên trạng thái (state / 상태) mới.

### Insight

Optimistic locking không “khóa” row trước; nó detect xung đột (conflict / 충돌) khi ghi (write / 쓰기) bằng phiên bản (version / 버전)/bất biến (invariant / 불변식).

---

# Môn 4 — 프로그래밍 언어 활용

## Lab 16 — Mutex đúng nhưng môi trường vận hành (production / 운영 환경) vẫn race

### Scenario

Một app có toàn cục (global / 전역) in-memory counter và dùng mutex. Single instance kiểm thử (test / 테스트) luôn đúng. môi trường vận hành (production / 운영 환경) chạy 8 instances sau bộ cân bằng tải (load balancer / 로드 밸런서) và counter sai.

### Tự trả lời

Mutex đã bảo vệ gì? Vì sao chưa đủ?

### Phân tích

Mutex chỉ synchronize threads/tiến trình (process / 프로세스) phạm vi (scope / 범위) mà thành phần nguyên thủy (primitive / 기본 요소) đó chia sẻ được. 8 instances có bộ nhớ (memory / 메모리) riêng nên mỗi instance có mutex riêng.

Nếu bất biến (invariant / 불변식) toàn cục (global / 전역) giữa instances, cần dùng chung (shared / 공유) coordination/trạng thái (state / 상태) cơ chế (mechanism / 메커니즘) ở tầng (layer / 계층) phù hợp: DB atomic cập nhật (update / 업데이트)/giao dịch (transaction / 트랜잭션), phân tán (distributed / 분산) khóa (lock / 잠금) khi thật cần, hoặc redesign.

### Insight

Đúng cơ chế (mechanism / 메커니즘) ở sai phạm vi (scope / 범위) vẫn sai bất biến (invariant / 불변식).

---

## Lab 17 — Round Robin quantum sự đánh đổi (trade-off / 트레이드오프)

### Scenario

Quantum giảm từ 50 ms xuống 1 ms.

### Tự trả lời

Phản hồi (response / 응답) thời gian (time / 시간) và overhead có xu hướng gì?

### Phân tích

Quantum nhỏ thường cải thiện responsiveness/fairness ngắn hạn nhưng tăng context-switch overhead.

Nếu quantum quá lớn, Round Robin tiến gần FCFS cho CPU-bound jobs.

Không có quantum tối ưu universal; phụ thuộc tải công việc (workload / 워크로드) và switch chi phí (cost / 비용).

---

## Lab 18 — FIFO vs LRU khác victim nhưng fault count bằng nhau

### Scenario

Tham chiếu (reference / 참조) string ngắn cho cùng số page faults ở FIFO và LRU.

### Tự trả lời

Có kết luận hai thuật toán (algorithm / 알고리즘) tương đương không?

### Phân tích

Không. Same kết quả (result / 결과) trên một dấu vết (trace / 추적) không chứng minh same chính sách (policy / 정책). FIFO dùng insertion age; LRU dùng recency of truy cập (access / 접근).

Cần nhìn cơ chế (mechanism / 메커니즘), không chỉ count ở một mẫu (sample / 표본).

---

## Lab 19 — TCP reliable nhưng API vẫn duplicate

### Scenario

TCP bảo đảm bytes ordered/retransmitted trong một liên kết (connection / 연결). Tại sao payment API vẫn cần idempotency?

### Phân tích

Độ tin cậy (reliability / 신뢰성) vận chuyển (transport / 전송) không giải ambiguity application-level khi liên kết (connection / 연결) mất sau máy chủ (server / 서버) lần ghi nhận (commit / 커밋) nhưng trước khi máy khách (client / 클라이언트) biết kết quả (result / 결과). máy khách (client / 클라이언트) mở yêu cầu (request / 요청) mới/thử lại (retry / 재시도) → logical thao tác (operation / 연산) có thể lặp.

TCP giải byte delivery ngữ nghĩa (semantics / 의미론); idempotency giải nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론).

---

## Lab 20 — Java tham chiếu (reference / 참조) kiểu (type / 타입) vs thời gian chạy (runtime / 런타임) kiểu (type / 타입)

### Scenario
Phần “Scenario” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```java
class A {
    void f() { System.out.print("A"); }
    void onlyA() {}
}
class B extends A {
    @Override void f() { System.out.print("B"); }
    void onlyB() {}
}
A x = new B();
```

### Tự trả lời

1. `x.f()` gọi gì?
2. `x.onlyB()` compile được không?
3. Vì sao?

### Phân tích

`x.f()` → `B.f()` qua động (dynamic / 동적) dispatch.

`x.onlyB()` không accessible qua static/tham chiếu (reference / 참조) kiểu (type / 타입) `A` nếu không cast/typing khác.

Compile-time member availability và thời gian chạy (runtime / 런타임) overriding là hai stage lập luận (reasoning / 추론) khác nhau.

---

# Môn 5 — 정보시스템 구축 관리

## Lab 21 — RPO tốt nhưng RTO tệ

### Scenario

DB sync replication gần như zero dữ liệu (data / 데이터) mất mát (loss / 손실). Primary thất bại (fail / 실패), nhưng failover manual cần 3 giờ.

Nghiệp vụ (business / 비즈니스) yêu cầu (requirement / 요구사항):

```text
RPO <= 1 minute
RTO <= 15 minutes
```

### Phân tích

RPO có thể đạt, RTO thất bại (fail / 실패).

Replication freshness không tự giải khôi phục (recovery / 복구) orchestration.

Need automated failover, tested runbook, phụ thuộc (dependency / 의존성) khôi phục (recovery / 복구) và operational readiness tùy kiến trúc (architecture / 아키텍처).

---

## Lab 22 — Backup đầy đủ nhưng restore không được

### Scenario

Nhóm (team / 팀) backup mỗi giờ nhưng chưa bao giờ restore kiểm thử (test / 테스트). Khi sự cố (incident / 인시던트) xảy ra, tệp (file / 파일) backup corrupt từ 3 tuần trước.

### Tự trả lời

Backup chính sách (policy / 정책) đã thiếu dimension nào?

### Phân tích

Backup không hoàn thành khi “job success”. Cần restore xác minh (verification / 확인), integrity monitoring, retention, isolation và khôi phục (recovery / 복구) drill.

Availability/khôi phục (recovery / 복구) là end-to-end năng lực (capability / 역량).

---

## Lab 23 — RAID 5 không cứu ransomware

### Scenario

Máy chủ (server / 서버) dùng RAID 5. Ransomware encrypt filesystem hợp lệ qua OS.

### Phân tích

RAID parity bảo vệ một số vật lý (physical / 물리적) disk failures, không bảo vệ logical overwrite/encryption. Mọi disk trong array sẽ chứa encrypted blocks hợp lệ.

Need backup/versioning/isolation/bảo mật (security / 보안) controls khác.

---

## Lab 24 — Authentication đúng, authorization sai

### Scenario

Người dùng (user / 사용자) đăng nhập hợp lệ. API:

```http
GET /invoice/12345
```

Máy chủ (server / 서버) kiểm đơn vị từ (token / 토큰) valid nhưng không kiểm invoice 12345 thuộc người dùng (user / 사용자) nào. người dùng (user / 사용자) đổi ID và đọc invoice người khác.

### Phân tích

Authentication pass; object-level authorization thất bại (fail / 실패).

TLS cũng không giải nguyên nhân gốc (root cause / 근본 원인) vì attacker là người dùng (user / 사용자) hợp lệ trong protected channel.

Đây là lý do phải phân định danh (identity / 식별자) xác minh (verification / 확인) khỏi permission quyết định (decision / 결정).

---

## Lab 25 — Defense in độ sâu (depth / 깊이) nhưng nguyên nhân gốc (root cause / 근본 원인) vẫn tồn tại

### Scenario

App dùng WAF và firewall nhưng truy vấn (query / 쿼리) xây bằng string concat:

```text
"SELECT * FROM users WHERE name='" + input + "'"
```

### Tự trả lời

WAF có làm mã (code / 코드) an toàn không? gốc (root / 루트) điều khiển (control / 제어) là gì?

### Phân tích

WAF có thể khối (block / 블록) một số mẫu (pattern / 패턴) nhưng bypass/false positive/encoding variation vẫn tồn tại.

Gốc (root / 루트) điều khiển (control / 제어) là parameterized truy vấn (query / 쿼리)/prepared statement để dữ liệu (data / 데이터) không thay đổi SQL cấu trúc (structure / 구조).

Defense in độ sâu (depth / 깊이) tốt, nhưng perimeter điều khiển (control / 제어) không thay mã (code / 코드) tính đúng đắn (correctness / 정확성).

---

# Cross-subject mega labs

## Mega Lab A — Checkout endpoint

### Scenario

Yêu cầu (requirement / 요구사항):

```text
User đặt order.
Không oversell.
Không charge hai lần.
95% request < 2s.
System chịu mất một app instance mà không gián đoạn đáng kể.
```

### Hãy nối 5 môn

**Môn 1:** functional/non-functional yêu cầu (requirement / 요구사항), chuỗi (sequence / 시퀀스)/giao diện (interface / 인터페이스) thiết kế (design / 설계), idempotency đặc tả hợp đồng (contract / 계약).

**Môn 2:** kiểm thử (test / 테스트) ranh giới (boundary / 경계), regression, kiểm thử tích hợp (integration test / 통합 테스트) cho thử lại (retry / 재시도)/concurrent thứ tự (order / 순서).

**Môn 3:** giao dịch (transaction / 트랜잭션), atomic stock cập nhật (update / 업데이트), unique key, chỉ mục (index / 인덱스).

**Môn 4:** concurrent requests, tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드), TCP hết thời gian chờ (timeout / 타임아웃) ambiguity.

**Môn 5:** tải (load / 로드) balancing, HA, authentication/authorization, monitoring/khôi phục (recovery / 복구).

### Câu hỏi sâu

1. Mutex cục bộ (local / 로컬) có đủ cho stock không?
2. Unique idempotency key và giao dịch (transaction / 트랜잭션) phải phối hợp thế nào?
3. chỉ mục (index / 인덱스) nào hỗ trợ lookup yêu cầu (request / 요청) định danh (identity / 식별자)?
4. hiệu năng (performance / 성능) yêu cầu (requirement / 요구사항) phải biến thành kiểm thử (test / 테스트)/chỉ số (metric / 지표) gì?
5. Nếu app instance chết sau DB lần ghi nhận (commit / 커밋) nhưng trước phản hồi (response / 응답), máy khách (client / 클라이언트) hành vi (behavior / 동작) phải thế nào?

---

## Mega Lab B — Reporting hệ thống (system / 시스템) chậm

### Scenario

Report truy vấn (query / 쿼리) phép nối (join / 조인) 8 bảng normalized, chạy 45 giây. nhóm (team / 팀) đề xuất:

- denormalize mọi bảng (table / 테이블);
- thêm chỉ mục (index / 인덱스) vào mọi column;
- tăng RAM;
- bộ nhớ đệm (cache / 캐시) report 24 giờ.

### Tư duy đúng

Không chọn solution trước khi phân tích truy cập (access / 접근) mẫu (pattern / 패턴) và bottleneck.

Cần:

1. xác định yêu cầu (requirement / 요구사항) về freshness/độ trễ (latency / 지연 시간);
2. xem thực thi (execution / 실행) plan/cardinality/chỉ mục (index / 인덱스);
3. phân biệt OLTP vs analytics tải công việc (workload / 워크로드);
4. cân nhắc summary/materialized cấu trúc (structure / 구조);
5. hiểu consistency chi phí (cost / 비용) của bộ nhớ đệm (cache / 캐시)/denormalization;
6. đo thay vì đoán.

### Bẫy

Mọi proposed solution đều có thể hợp lý trong một ngữ cảnh (context / 맥락), nhưng không cái nào universal.

---

## Mega Lab C — sự cố (incident / 인시던트) sau triển khai (deployment / 배포)

### Scenario

Phiên bản (version / 버전) mới deploy 10:00. 10:05 lỗi (error / 오류) tỷ lệ (rate / 비율) tăng mạnh. DB CPU bình thường, app CPU tăng 95%, GC liên tục. quay lui (rollback / 롤백) sản phẩm tạo ra (artifact / 산출물) lại bị nhầm phiên bản (version / 버전).

### Nối kiến thức
Phần “Nối kiến thức” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- cấu hình (configuration / 구성) management/bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물);
- ứng dụng (application / 애플리케이션) bộ nhớ (memory / 메모리) hành vi (behavior / 동작);
- khả năng quan sát (observability / 관측 가능성);
- quay lui (rollback / 롤백) plan;
- phiên bản (version / 버전) identification/baseline;
- kiểm tra hợp lệ (validation / 검증) sau deploy.

### Gốc (root / 루트) học tập (learning / 학습)

Một sự cố (incident / 인시던트) môi trường vận hành (production / 운영 환경) có thể bắt đầu là mã (code / 코드)/hiệu năng (performance / 성능) issue nhưng khôi phục (recovery / 복구) thất bại vì cấu hình (configuration / 구성) management.

---

# Cách tự chấm scenario

Mỗi lab chấm 0–4:

```text
0 = không biết bắt đầu
1 = nhớ keyword nhưng không giải thích mechanism
2 = chọn đúng concept nhưng reasoning thiếu layer/scope
3 = giải đúng mechanism + phân biệt distractor
4 = giải đúng + nêu trade-off + liên kết sang môn khác
```

Mục tiêu trước full mock:

```text
25 labs cơ bản: trung bình >= 3
3 mega labs: mỗi lab >= 3
không có lab nào = 0
```

Nếu score 1 vì nhầm hai concept, quay lại `11-high-risk-confusion-atlas.md`.

Nếu score 1–2 vì không làm được calculation/dấu vết (trace / 추적), quay lại `08-procedural-workbook.md`.

Nếu score thấp vì không hiểu concept gốc, quay lại deep-dive môn tương ứng.
