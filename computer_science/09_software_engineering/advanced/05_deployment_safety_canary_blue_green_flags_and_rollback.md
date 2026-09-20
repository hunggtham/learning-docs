# Deployment safety: canary, blue-green, feature flags và rollback limits

Deploy không chỉ là copy artifact. Nó thay đổi một running socio-technical system có traffic, persistent data và dependencies đang ở nhiều versions. Deployment strategy tốt giảm blast radius và tăng khả năng phát hiện sai trước khi toàn bộ users bị ảnh hưởng.

## Rolling deployment

Instances được thay dần giúp giữ capacity nhưng old/new versions coexist. API, message và database schema phải tương thích trong overlap window.

Nếu version N+1 chỉ hiểu data mà N không hiểu, rollback hoặc mixed fleet có thể fail dù deploy tool hoạt động đúng.

## Blue-green

Blue-green duy trì hai environments và switch traffic. Rollback routing nhanh nếu state/data compatible. Cost infrastructure cao hơn và database thường vẫn shared, nên không phải mọi thay đổi rollback tức thì.

## Canary

Canary gửi phần nhỏ traffic tới version mới, quan sát error/latency/business metrics rồi tăng dần. Canary giảm blast radius nhưng chỉ hữu ích nếu sample traffic đại diện và metrics nhạy với failure cần phát hiện.

1% traffic có thể không chạm rare workflow hoặc tenant đặc biệt.

## Feature flags

Flag tách code deployment khỏi feature exposure. Team có thể deploy dormant code rồi enable theo cohort.

Nhưng flags tạo state space: old/new paths cùng tồn tại, combinations có thể tương tác. Flags cần owner, expiry và cleanup; nếu không chúng trở thành permanent complexity.

## Rollback không phải time machine

Binary rollback không undo database migration, external email đã gửi, money movement hoặc event đã publish. Sau destructive data change, old binary có thể không chạy được.

Vì vậy migration cần forward/backward compatibility và đôi khi **roll-forward** an toàn hơn rollback.

## Health và readiness

Process start thành công chưa nghĩa sẵn sàng nhận traffic. Readiness nên phản ánh initialization cần thiết, nhưng nếu phụ thuộc mọi downstream service, transient dependency có thể làm toàn fleet rút khỏi load balancer cùng lúc.

Health check cũng là control-loop design.

## Automated guardrails

Deployment controller có thể pause/rollback khi SLO burn, error rate hoặc key business invariant vượt threshold. Guardrail cần chống noisy metric và delayed signal.

Manual approval không thay thế observability; người duyệt cũng cần evidence.

## Deployment và schema

Expand-contract pattern giúp old/new binaries cùng hoạt động. Add nullable field/index online, backfill có throttling, migrate reads/writes, rồi mới enforce/drop.

Database change thường là phần ít reversible nhất của deploy.

## Mental Model

> Safe deployment là controlled exposure dưới uncertainty. Canary giảm blast radius, flags tách activation, blue-green giảm switch cost, nhưng rollback chỉ tồn tại khi code, data và protocols còn backward compatible.