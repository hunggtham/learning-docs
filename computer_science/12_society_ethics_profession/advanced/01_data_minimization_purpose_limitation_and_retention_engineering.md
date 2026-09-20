# Data minimization, purpose limitation và retention engineering

Privacy engineering không chỉ là policy document. Một hệ thống thật sự bảo vệ dữ liệu phải biến nguyên tắc như **data minimization**, **purpose limitation** và **retention** thành architecture, schema, access control và deletion workflow có thể kiểm chứng.

## Data minimization

Data minimization hỏi: để cung cấp capability này, hệ thống thực sự cần thu thập và giữ những fields nào? “Có thể hữu ích sau này” tạo data liability: breach impact lớn hơn, authorization phức tạp hơn và deletion khó hơn.

Minimization nên diễn ra từ input boundary. Nếu field không cần thiết, tốt hơn không thu thập thay vì thu thập rồi hứa không dùng.

## Purpose limitation

Cùng một dữ liệu có thể phù hợp cho mục đích A nhưng không mặc nhiên phù hợp cho B. Engineering cần gắn data flow với declared purpose và authorization context thay vì coi mọi internal data là tài nguyên dùng tự do.

Điều này ảnh hưởng event bus, analytics lake và feature engineering: copy data sang hệ thống khác tạo thêm processing purpose và retention boundary cần quản lý.

## Retention là lifecycle

“Giữ 90 ngày” nghe đơn giản nhưng data có thể tồn tại trong primary DB, replica, cache, search index, object storage, log, backup và derived dataset. Retention engineering cần inventory các copies và định nghĩa deletion semantics cho từng layer.

Một row bị delete khỏi primary không có nghĩa mọi derived copy biến mất ngay.

## TTL và scheduled deletion

TTL ở storage layer hữu ích nhưng phải hiểu guarantee: deletion có diễn ra đúng thời điểm hay eventual? Backup immutable có policy expiry riêng không? Search index có nhận delete event không?

Retention SLO có thể định nghĩa khoảng thời gian tối đa từ eligibility tới deletion hoàn tất ở các active systems.

## Logs là nguồn rò rỉ phổ biến

Application có thể cẩn thận với database nhưng vô tình log token, email, request body hoặc identifier nhạy cảm. Log thường được replicate sang nhiều observability systems và có retention dài.

Structured logging nên có allowlist/redaction policy; “log tất cả rồi filter sau” tạo blast radius lớn.

## Derived data

Nếu raw data bị xóa, aggregate/model feature có cần xóa không phụ thuộc khả năng liên kết lại cá nhân và policy/legal context. Engineering cần lineage để biết artifact nào được tạo từ nguồn nào thay vì tranh luận sau sự cố mà không có evidence.

## Access control theo purpose

RBAC chỉ nói role nào truy cập resource; hệ thống phức tạp có thể cần attribute/context để giới hạn theo tenant, workflow hoặc approved purpose. Nhưng policy càng tinh vi càng cần auditability và test, nếu không configuration complexity tự tạo security gap.

## Deletion workflow phải idempotent

User deletion thường đi qua nhiều services. Retry là bình thường; vì vậy delete handlers cần idempotent và có trạng thái theo dõi completion. Failure ở một downstream không nên làm toàn workflow im lặng thành công.

Audit record có thể cần chứng minh deletion process đã chạy mà không giữ lại chính payload đáng lẽ phải xóa.

## Privacy và reliability liên hệ nhau

Một deletion queue backlog là privacy incident tiềm năng. Retention job thất bại cần alert/SLO giống production pipeline khác. Privacy control chỉ tồn tại trên giấy nếu không có monitoring và owner.

## Mental model

> Privacy principle phải trở thành data lifecycle có thể vận hành: collect ít hơn, bind usage với purpose, biết mọi copy ở đâu, đặt retention, propagate deletion và đo failure. Privacy engineering là system design + governance + observability, không phải checkbox cuối dự án.