# 09. Modular monolith và services

## Boundary trước topology

Modular monolith và microservices đều cần module boundary rõ: ownership của
state, public command/query, invariant và dependency direction. Tách process
không tự tạo modularity; nó chỉ thêm network, deployment, versioning, tracing,
failure và data consistency cost.

Một module tốt có API nhỏ, dữ liệu được sở hữu rõ, invariant không cần truy cập
trực tiếp bảng của module khác, và dependency đi theo hướng có chủ ý. Shared
utility chỉ chứa primitive ổn định; đừng biến nó thành shared domain model làm
mọi module coupling.

## Khi nào tách service

Tách khi có boundary business/ownership thật, scaling hoặc availability profile
khác, cadence/deployment độc lập, hoặc security/isolation bắt buộc. Không tách
chỉ vì package dài hay vì muốn “microservice-ready”. Trước khi tách, đo coupling,
transaction crossing, data access và operational readiness.

## Migration path

1. Đặt module API và cấm truy cập chéo trực tiếp.
2. Thêm contract test, audit dependency và ownership.
3. Tách read model/event hoặc strangler flow nếu cần.
4. Chuyển persistence ownership, rồi mới chuyển process.
5. Đo latency, retry, consistency và chi phí vận hành sau mỗi bước.

Remote call không thể giả định như function call: phải có timeout, retry policy,
idempotency, versioned contract và fallback. Distributed transaction nên được
thay bằng local transaction + event/state machine khi invariant cho phép.

Architecture fundamentals và distributed trade-off thuộc [Computer Science](../../computer_science/README.md); chapter này giữ quyết định topology ở application level.

## Đào sâu: dependency fitness

Boundary cần được kiểm tra liên tục bằng các chỉ số: dependency đi ngược hướng,
transaction đọc bảng module khác, consumer ngoài owner, deploy cần release đồng
thời, và latency/failure rate của cross-module call. Architecture test giúp cấm
import sai, nhưng review ownership của schema, event và on-call mới phát hiện
boundary giả.

Khi service B cần dữ liệu của A, chọn rõ: synchronous query (coupling latency),
replicated read model (eventual consistency), hoặc API composition (coupling
contract). Không cho B đọc thẳng database A “tạm thời” mà không có expiry plan;
đường tắt này thường trở thành transaction xuyên service không thể tách.

## Bài tập suy luận

Lập migration plan tách `Billing` khỏi monolith: invariant local, transaction
crossing, event/outbox, dual-read/dual-write risk, rollback signal và điều kiện
dừng. Nếu không thể mô tả rollback, boundary chưa sẵn sàng.
