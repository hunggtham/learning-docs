# Idempotency kiến trúc (architecture / 아키텍처) và deduplication at quy mô (scale / 규모)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Idempotency architecture và deduplication at scale**. Route đi từ retry ambiguity → idempotency key/operation identity → dedup store/retention → side-effect ordering → partitioning and failure, để “effectively once” có boundary đo được.

Phân tán (distributed / 분산) yêu cầu (request / 요청) có thể hết thời gian chờ (timeout / 타임아웃) dù máy chủ (server / 서버) đã thực hiện side tác động (effect / 효과). máy khách (client / 클라이언트) không biết nên thử lại (retry / 재시도) hay không. **Idempotency** giải quyết ambiguity bằng cách làm nhiều lần cùng logical thao tác (operation / 연산) có observable kết quả (result / 결과) tương đương một lần.

## Thử lại (retry / 재시도) tạo ambiguity

Máy khách (client / 클라이언트) gửi payment yêu cầu (request / 요청), máy chủ (server / 서버) lần ghi nhận (commit / 커밋) rồi phản hồi (response / 응답) bị mất. Nếu máy khách (client / 클라이언트) thử lại (retry / 재시도) như yêu cầu (request / 요청) mới, charge có thể xảy ra hai lần. Nếu không thử lại (retry / 재시도), người dùng (user / 사용자) có thể nghĩ payment thất bại dù đã thành công.

Mạng (network / 네트워크) không thể luôn nói cho máy khách (client / 클라이언트) giao dịch (transaction / 트랜잭션) đã lần ghi nhận (commit / 커밋) hay chưa. giao thức (protocol / 프로토콜) phải encode logical định danh (identity / 식별자) của thao tác (operation / 연산).

> **Nối mạch:** **Idempotency key** nối từ **Thử lại (retry / 재시도) tạo ambiguity** sang **Cơ sở dữ liệu (database / 데이터베이스) uniqueness**, vì cơ chế trước tạo đầu vào cho bước sau.

## Idempotency key

Máy khách (client / 클라이언트) tạo key ổn định cho một logical hành động (action / 동작). máy chủ (server / 서버) lưu ánh xạ (mapping / 매핑) key → kết quả (outcome / 결과)/trạng thái (state / 상태). thử lại (retry / 재시도) cùng key trả lại kết quả (result / 결과) cũ hoặc tiếp tục máy trạng thái (state machine / 상태 머신) thay vì tạo side tác động (effect / 효과) mới.

Key phải có phạm vi (scope / 범위) rõ: per account/endpoint? TTL bao lâu? Payload khác nhưng reuse cùng key xử lý thế nào? Những chi tiết này là part of Đặc tả API (API contract / API 계약).

> **Nối mạch:** **Idempotency key** đặt vấn đề; **Cơ sở dữ liệu (database / 데이터베이스) uniqueness** kiểm tra bằng chứng, rồi **Inbox/outbox** mở rộng hệ quả.

## Cơ sở dữ liệu (database / 데이터베이스) uniqueness

Unique ràng buộc (constraint / 제약조건) thường là dedup ranh giới (boundary / 경계) mạnh. `INSERT ... ON CONFLICT` hoặc giao dịch (transaction / 트랜잭션) kiểm tra idempotency bản ghi (record / 레코드) có thể atomically gắn nghiệp vụ (business / 비즈니스) ghi (write / 쓰기) với key.

Check-then-insert ngoài giao dịch (transaction / 트랜잭션) dễ race khi hai retries đến đồng thời.

> **Nối mạch:** **Cơ sở dữ liệu (database / 데이터베이스) uniqueness** đặt vấn đề; **Inbox/outbox** kiểm tra bằng chứng, rồi **Dedup cửa sổ (window / 윈도우)** mở rộng hệ quả.

## Inbox/outbox

Message bên tiêu thụ (consumer / 소비자) có thể ghi message ID vào inbox/dedup bảng (table / 테이블) cùng giao dịch (transaction / 트랜잭션) với nghiệp vụ (business / 비즈니스) cập nhật (update / 업데이트). Producer dùng transactional outbox để nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) và event-to-publish được lần ghi nhận (commit / 커밋) cùng cục bộ (local / 로컬) DB giao dịch (transaction / 트랜잭션).

Relay có thể publish duplicate, nhưng bên tiêu thụ (consumer / 소비자) idempotency xử lý. Đây là cách đạt reliable tác động (effect / 효과) mà không cần phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) cho mọi thành phần (component / 컴포넌트).

> **Nối mạch:** **Dedup cửa sổ (window / 윈도우)** nối từ **Inbox/outbox** sang **Natural idempotency**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dedup cửa sổ (window / 윈도우)

Giữ mọi idempotency key vĩnh viễn không quy mô (scale / 규모). TTL giới hạn lưu trữ (storage / 저장소) nhưng thử lại (retry / 재시도) sau TTL có thể duplicate. cửa sổ (window / 윈도우) phải dựa trên nghiệp vụ (business / 비즈니스) rủi ro (risk / 위험) và maximum thử lại (retry / 재시도)/replay horizon.

Payment có thể cần retention dài hơn analytics sự kiện (event / 이벤트).

> **Nối mạch:** **Natural idempotency** nối từ **Dedup cửa sổ (window / 윈도우)** sang **Exactly-once tác động (effect / 효과)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Natural idempotency

`SET status='ACTIVE'` thường idempotent hơn `increment balance by 10`. Thiết kế API theo desired final trạng thái (state / 상태) đôi khi giảm dedup burden.

Nhưng conditional transitions vẫn cần tính đồng thời (concurrency / 동시성) điều khiển (control / 제어): “activate subscription phiên bản (version / 버전) 7” có thể dùng phiên bản (version / 버전)/precondition để tránh stale ghi (write / 쓰기).

> **Nối mạch:** **Exactly-once tác động (effect / 효과)** nối từ **Natural idempotency** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Exactly-once tác động (effect / 효과)

Vận chuyển (transport / 전송) có thể deliver at-least-once; ứng dụng (application / 애플리케이션) vẫn tạo exactly-once-like nghiệp vụ (business / 비즈니스) tác động (effect / 효과) bằng stable định danh (identity / 식별자) + atomic dedup + idempotent side tác động (effect / 효과). bên ngoài (external / 외부) các hệ thống (systems / 시스템들) không hỗ trợ idempotency làm end-to-end guarantee yếu đi.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Exactly-once tác động (effect / 효과)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy (mental model / 사고 모델)

> Idempotency không ngăn duplicate delivery; nó ngăn duplicate delivery trở thành duplicate nghiệp vụ (business / 비즈니스) tác động (effect / 효과). Stable thao tác (operation / 연산) định danh (identity / 식별자) và atomic dedup ranh giới (boundary / 경계) là cốt lõi, còn thử lại (retry / 재시도) chỉ là vận chuyển (transport / 전송) hành vi (behavior / 동작).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
