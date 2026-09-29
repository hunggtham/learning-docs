# Backend — kiểm toán phạm vi và độ sâu

> **Mạch đọc:** Đọc tệp này sau [`README.md`](./README.md). `README.md` cho biết đường học của Backend; audit này trả lời câu hỏi khác: **những cơ chế nào Backend phải sở hữu, phần nào phải bàn giao sang Computer Science/Linux/DevOps, và khoảng trống nào đáng đào sâu tiếp theo?** Đơn vị sở hữu khái niệm chuẩn gốc (canonical owner / 정본 소유자) của Backend là [`backend_core/`](./backend_core/README.md); Java, Spring và Python là các nhánh hiện thực (implementation track / 구현 트랙).

**Ngày rà soát:** 2026-09-29.

## 1. Phạm vi sở hữu

`10_backend/` sở hữu lớp kỹ thuật ứng dụng phía máy chủ (backend application engineering / 백엔드 애플리케이션 엔지니어링): vòng đời yêu cầu (request lifecycle / 요청 수명주기), hợp đồng API (API contract / API 계약), định danh và phiên (identity/session / 신원·세션), cách ứng dụng dùng lưu trữ và giao dịch (persistence/transaction / 영속성·트랜잭션), bộ nhớ đệm (cache / 캐시), xử lý bất đồng bộ (asynchronous processing / 비동기 처리), thử lại và tính lũy đẳng (retry/idempotency / 재시도·멱등성), kiểm thử (testing / 테스트), khả năng quan sát (observability / 관측 가능성), ranh giới mô-đun/dịch vụ và các nhánh ngôn ngữ/khung phần mềm.

Backend không nên tự viết lại cơ chế sâu đã có đơn vị sở hữu khác. Nội tại cơ sở dữ liệu thuộc [Computer Science Databases](../computer_science/05_data_databases/README.md); mạng và hệ phân tán thuộc [Networks & Distributed Systems](../computer_science/06_networks_distributed_systems/README.md); nền tảng bảo mật/độ tin cậy thuộc [Security & Reliability](../computer_science/07_security_reliability/README.md); trạng thái máy chủ và thời gian chạy thuộc [Linux](../linux/README.md); triển khai, SRE và nền tảng vận hành thuộc [DevOps / Platform Engineering](../devops_platform_engineering/README.md).

Ranh giới này quan trọng vì cùng một lỗi có thể xuất hiện ở nhiều lớp. Ví dụ “request timeout” có thể bắt nguồn từ pool kết nối của ứng dụng, bộ lập lịch CPU, hàng đợi downstream hoặc transaction chưa hoàn tất. Backend cần giải thích **hợp đồng và hậu quả ở lớp ứng dụng**, rồi bàn giao cơ chế thấp hơn sang đúng owner thay vì copy lại toàn bộ internals.

## 2. Phần hiện đã mạnh

Mạch học hiện tại đi theo trạng thái và tác động phụ thay vì đi theo API của framework:

```text
vòng đời request
→ ngữ nghĩa HTTP/API
→ identity/session
→ persistence/transaction
→ cache/invalidation
→ job/message bất đồng bộ
→ timeout/retry/idempotency
→ test/contract
→ observability/debugging
→ module/service boundary
→ production case
```

Đây là một xương sống tốt vì người học có thể theo cùng một câu hỏi xuyên suốt: **trạng thái nào thay đổi, bất biến nào phải giữ, failure có thể xuất hiện ở đâu và bằng chứng nào giúp phân biệt nguyên nhân?** [`backend_core/`](./backend_core/README.md) đã có audit chi tiết riêng, nên audit cấp root không lặp lại từng chapter mà tập trung vào tính nhất quán giữa `backend_core`, Java, Spring và Python.

Việc tách Java, Spring và Python cũng đang đúng hướng. Java/Python giải thích ngữ nghĩa ngôn ngữ và runtime; Spring giải thích cách một framework hiện thực các invariant Backend. Điều này ngăn lỗi cấu trúc phổ biến như đồng nhất “Spring = Backend”.

## 3. Bất biến khi thêm hoặc sửa nội dung

Một chapter Backend có giá trị khi người đọc trả lời được: hợp đồng nào được cung cấp; trạng thái nào thay đổi; điểm bền vững (durable boundary / 영속 경계) nằm ở đâu; failure nào có thể xảy ra độc lập; thao tác nào có thể retry/replay; retry có thể lặp side effect hay không; telemetry nào phân biệt các giả thuyết; và thay đổi phiên bản có giữ tương thích khi rollout hay rollback hay không.

Vì vậy, lời giải kiểu “dùng annotation/API X” là chưa đủ. API chỉ là cơ chế hiện thực. Nếu bỏ tên Spring/FastAPI/vendor mà phần giải thích vẫn đúng, nội dung có khả năng đang ở đúng lớp khái niệm. Nếu toàn bộ giải thích sụp đổ khi bỏ tên sản phẩm, nội dung đó nên nằm trong nhánh implementation tương ứng.

## 4. Ranh giới dễ nhầm

### ORM không phải nội tại cơ sở dữ liệu

Backend có thể giải thích cách dùng transaction, hậu quả của isolation, N+1, connection pool và migration contract. Cấu trúc B-tree, WAL, cách MVCC được hiện thực hoặc consensus phân tán thuộc Computer Science Databases. Backend chỉ kéo những cơ chế đó vào khi cần làm prerequisite ngắn để giải thích hậu quả ở ứng dụng.

### Messaging không đồng nghĩa với học lại distributed systems

Backend sở hữu ngữ nghĩa ứng dụng như consumer side effect, duplicate delivery, poison message, retry policy, idempotency và outbox. Thuật toán consensus hoặc protocol của broker không cần lặp lại ở đây.

### Observability là bằng chứng, không phải cú pháp logging

Cấu hình logger có thể là ví dụ. Câu hỏi chuẩn gốc là: bằng chứng nào nối request với operation, dependency, durable transition và failed side effect? Nếu log nhiều nhưng không trả lời được các câu hỏi này, hệ thống chưa thật sự quan sát được.

### Service boundary không phải checklist microservices

Một service mới phải có lý do như ownership, failure isolation, compliance, scaling độc lập hoặc deployment boundary. Câu “microservices scale tốt hơn” không đủ để biện minh cho việc chia hệ thống.

## 5. Khoảng trống ưu tiên

### P1 — So sánh cùng một invariant giữa các nhánh

Hiện mỗi track đã mạnh riêng lẻ nhưng còn thiếu một tuyến so sánh ngắn:

```text
backend invariant
→ hệ quả ở Java/runtime
→ cơ chế hiện thực trong Spring
→ hệ quả ở Python/runtime/framework
→ cách test và quan sát
```

Giá trị của tuyến này là giúp người học thấy framework khác nhau nhưng vấn đề nền giống nhau; nó không nên trở thành ba tutorial trùng lặp.

### P1 — Migration dữ liệu và trạng thái mixed-version

Cần tăng độ sâu về expand/contract migration, backward/forward compatibility, dual-read/dual-write, old/new version chạy đồng thời và rollback sau thay đổi schema/event contract. Đây là vùng dễ gây lỗi vì migration không chỉ là “chạy SQL”; nó là một giai đoạn mà nhiều phiên bản code cùng tương tác với một trạng thái đang chuyển đổi.

### P1 — Ngân sách phụ thuộc và sức chứa

Cần nối rõ:

```text
SLO của request
→ timeout budget
→ connection/thread/event-loop pool
→ downstream concurrency
→ queue depth/age
→ backpressure
→ overload behavior
```

Backend sở hữu phần ngân sách và hợp đồng ứng dụng; Linux/DevOps sở hữu cơ chế host/platform sâu hơn.

### P2 — Đường bằng chứng của authentication/authorization

Các chapter identity/session nên nối rõ hơn từ credential tới quyền hiệu lực (effective authority / 유효 권한), propagation qua job/service và audit evidence. Lý thuyết threat model vẫn bàn giao sang Computer Science Security.

### P2 — Từ vựng recovery thống nhất

Cần chuẩn hóa khác biệt giữa **thử lại (retry / 재시도)**, **phát lại (replay / 재생)**, **đối soát (reconciliation / 대조)**, **bù trừ (compensation / 보상)**, **khôi phục dữ liệu (restore / 복원)** và **quay lui phiên bản (rollback / 롤백)**. Mỗi production case phải nói rõ đang dùng cơ chế nào, vì chúng giải quyết các failure khác nhau.

### P2 — Hợp đồng với hệ thống bên ngoài

Webhook/API/payment-like side effect cần được học như một hệ thống có duplicate delivery, callback authenticity, provider timeout, eventual reconciliation, rate limit và bằng chứng phục vụ recovery/tranh chấp. Đây là lớp mà “HTTP 200/500” thường không đủ để suy ra business outcome.

## 6. Quy trình review

Khi một PR thay đổi đáng kể Backend, đọc theo thứ tự:

```text
owner
→ contract/invariant
→ state + durable boundary
→ failure semantics
→ retry/recovery
→ telemetry/evidence
→ compatibility khi thay đổi
→ cách framework/ngôn ngữ hiện thực
→ internal links
```

Nếu chapter chỉ thêm API mới mà không làm rõ invariant, failure hoặc evidence, thay đổi đó chưa tăng chiều sâu của thư viện.

## 7. Kết luận và bàn giao

Cấu trúc root, `backend_core` và việc tách Java/Spring/Python hiện **mạnh**. Khoảng trống có giá trị cao nhất không phải thêm framework khác mà là: so sánh invariant giữa các track, reasoning cho migration/mixed-version, capacity budget và vocabulary recovery.

Sau audit này, nếu muốn đào sâu failure xuyên nhiều lớp, đọc tiếp [`devops_platform_engineering/10_production_practice/01_request_storage_queue_failure_and_recovery_case.md`](../devops_platform_engineering/10_production_practice/01_request_storage_queue_failure_and_recovery_case.md). Tuyến đó dùng đúng các invariant Backend ở đây rồi mở rộng sang database, queue và recovery ở production.