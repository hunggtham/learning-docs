# Backend cốt lõi (core / 핵심)

> **Mạch đọc:** Đọc **Backend cốt lõi (core / 핵심)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **mạch học (learning flow / 학습 흐름)** sang **Chapters**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Backend cốt lõi (core / 핵심) là lớp kiến thức chung đứng trước Java, Spring và Python. Nó mô tả
backend như một hệ thống nhận yêu cầu (request / 요청), đọc/ghi trạng thái (state / 상태), phát side tác động (effect / 효과) và trả
đặc tả hợp đồng (contract / 계약) có thể quan sát được. Mục tiêu là tạo một đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) cho những
quyết định backend không thuộc riêng một ngôn ngữ hay khung phần mềm (framework / 프레임워크).

## Mạch học (learning flow / 학습 흐름)
Phần “Mạch học (learning flow / 학습 흐름)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
request lifecycle
  → HTTP semantics
  → identity/session
  → persistence and transaction
  → cache and invalidation
  → jobs and messaging
  → timeout/retry/idempotency
  → tests and contracts
  → observability and debugging
  → modular monolith and service boundaries
  → production case studies
```


> **Chuyển mạch:** Từ **mạch học (learning flow / 학습 흐름)**, ta sang **Chapters** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chapters

1. [Backend request lifecycle](./00_backend_request_lifecycle.md)
2. [HTTP API semantics](./01_http_api_semantics.md)
3. [Auth, session và identity](./02_auth_session_identity.md)
4. [Persistence, transaction và ORM](./03_persistence_transactions_orm.md)
5. [Caching và invalidation](./04_caching_and_invalidation.md)
6. [Async jobs và messaging](./05_async_jobs_messaging.md)
7. [Timeout, retry và idempotency](./06_timeout_retry_idempotency.md)
8. [Testing, contract và integration](./07_testing_contract_integration.md)
9. [Observability và debugging](./08_observability_and_debugging.md)
10. [Modular monolith và services](./09_modular_monolith_services.md)
11. [Production backend case studies](./10_production_backend_case_studies.md)

12. [Coverage audit và backlog](./COVERAGE_AUDIT.md)

Mỗi chapter tách rõ **đặc tả hợp đồng (contract / 계약)**, **cơ chế (mechanism / 메커니즘)**, **dạng thất bại (failure mode / 실패 모드)** và **bằng chứng (evidence / 증거)**.
Đây là lớp lập luận (reasoning / 추론) để áp dụng vào khung phần mềm (framework / 프레임워크); không phải danh sách API cần học
thuộc lòng.

`COVERAGE_AUDIT.md` là nơi ghi ranh giới (boundary / 경계), đơn vị sở hữu (owner / 오너) và các chủ đề cố ý không lặp lại
từ Khoa học máy tính (computer science / 컴퓨터 과학). Khi thêm chapter mới, cập nhật kiểm tra (audit / 감사) trước để tránh biến
Backend cốt lõi (core / 핵심) thành một bản sao của cơ sở dữ liệu (database / 데이터베이스), mạng (network / 네트워크) hoặc khung phần mềm (framework / 프레임워크) thư viện (library / 라이브러리).


> **Chuyển mạch:** Từ **Chapters**, ta sang **Đường đọc nâng cao** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đường đọc nâng cao

Sau vòng đọc đầu tiên, hãy đọc lại theo các trục xuyên chapter thay vì chỉ đi
theo số thứ tự:

1. **tính đúng đắn (correctness / 정확성):** định danh (identity / 식별자) → giao dịch (transaction / 트랜잭션) → idempotency → đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트).
2. **độ trễ (latency / 지연 시간):** yêu cầu (request / 요청) ngân sách (budget / 예산) → bộ nhớ đệm (cache / 캐시) → hàng đợi (queue / 큐) → phụ thuộc (dependency / 의존성) hết thời gian chờ (timeout / 타임아웃) → dấu vết (trace / 추적).
3. **Durability:** lần ghi nhận (commit / 커밋) → outbox → thử lại (retry / 재시도) → replay → kiểm tra (audit / 감사) bằng chứng (evidence / 증거).
4. **thay đổi (change / 변경) an toàn (safety / 안전):** API tính tương thích (compatibility / 호환성) → expand/đặc tả hợp đồng (contract / 계약) di chuyển (migration / 마이그레이션) → rollout →
   quay lui (rollback / 롤백) và mixed-version hành vi (behavior / 동작).
5. **quy mô (scale / 규모):** hot key → pool saturation → backpressure → hàng đợi (queue / 큐) age → sức chứa (capacity / 용량)
   limit.

Mỗi trục nên kết thúc bằng một thiết kế (design / 설계) ghi chú (note / 노트) ngắn: nêu bất biến (invariant / 불변식), thất bại (failure / 실패) ngân sách (budget / 예산),
khả năng quan sát (observability / 관측 가능성) tín hiệu (signal / 신호) và cách kiểm thử (test / 테스트). Nếu một quyết định chỉ được giải thích bằng
tên khung phần mềm (framework / 프레임워크) hoặc sản phẩm (product / 제품), hãy quay lại chapter tương ứng và viết lại ở mức
đặc tả hợp đồng (contract / 계약).

> **Bàn giao:** Sau **Đường đọc nâng cao**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 backend request lifecycle](./00_backend_request_lifecycle.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
