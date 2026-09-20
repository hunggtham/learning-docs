# Idempotency architecture và deduplication at scale

Distributed request có thể timeout dù server đã thực hiện side effect. Client không biết nên retry hay không. **Idempotency** giải quyết ambiguity bằng cách làm nhiều lần cùng logical operation có observable result tương đương một lần.

## Retry tạo ambiguity

Client gửi payment request, server commit rồi response bị mất. Nếu client retry như request mới, charge có thể xảy ra hai lần. Nếu không retry, user có thể nghĩ payment thất bại dù đã thành công.

Network không thể luôn nói cho client transaction đã commit hay chưa. Protocol phải encode logical identity của operation.

## Idempotency key

Client tạo key ổn định cho một logical action. Server lưu mapping key → outcome/state. Retry cùng key trả lại result cũ hoặc tiếp tục state machine thay vì tạo side effect mới.

Key phải có scope rõ: per account/endpoint? TTL bao lâu? Payload khác nhưng reuse cùng key xử lý thế nào? Những chi tiết này là part of API contract.

## Database uniqueness

Unique constraint thường là dedup boundary mạnh. `INSERT ... ON CONFLICT` hoặc transaction kiểm tra idempotency record có thể atomically gắn business write với key.

Check-then-insert ngoài transaction dễ race khi hai retries đến đồng thời.

## Inbox/outbox

Message consumer có thể ghi message ID vào inbox/dedup table cùng transaction với business update. Producer dùng transactional outbox để business state và event-to-publish được commit cùng local DB transaction.

Relay có thể publish duplicate, nhưng consumer idempotency xử lý. Đây là cách đạt reliable effect mà không cần distributed transaction cho mọi component.

## Dedup window

Giữ mọi idempotency key vĩnh viễn không scale. TTL giới hạn storage nhưng retry sau TTL có thể duplicate. Window phải dựa trên business risk và maximum retry/replay horizon.

Payment có thể cần retention dài hơn analytics event.

## Natural idempotency

`SET status='ACTIVE'` thường idempotent hơn `increment balance by 10`. Thiết kế API theo desired final state đôi khi giảm dedup burden.

Nhưng conditional transitions vẫn cần concurrency control: “activate subscription version 7” có thể dùng version/precondition để tránh stale write.

## Exactly-once effect

Transport có thể deliver at-least-once; application vẫn tạo exactly-once-like business effect bằng stable identity + atomic dedup + idempotent side effect. External systems không hỗ trợ idempotency làm end-to-end guarantee yếu đi.

## Mental Model

> Idempotency không ngăn duplicate delivery; nó ngăn duplicate delivery trở thành duplicate business effect. Stable operation identity và atomic dedup boundary là cốt lõi, còn retry chỉ là transport behavior.