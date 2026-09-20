# Large-scale refactoring, strangler migration và branch-by-abstraction

Refactoring nhỏ có thể hoàn thành trong một commit. Migration lớn kéo dài tuần/tháng phải coexist với production traffic, nhiều teams và releases. Vấn đề chính chuyển từ “code mới tốt hơn” sang “làm sao thay hệ thống mà luôn giữ một trạng thái deployable”.

## Big-bang rewrite

Rewrite toàn bộ hấp dẫn vì tránh legacy constraints, nhưng trong thời gian dài old system vẫn thay đổi. New system phải đuổi theo moving target, feedback production đến muộn và cutover có blast radius lớn.

Rewrite đôi khi hợp lý, nhưng cần chứng minh boundary đủ cô lập và migration risk chấp nhận được.

## Strangler pattern

**Strangler migration** đặt facade/routing boundary trước old system rồi chuyển từng capability sang implementation mới. Old và new coexist; traffic được migrate dần.

Điểm khó là chọn seam. Nếu data ownership vẫn shared hỗn loạn, code đã tách nhưng coupling chưa thực sự giảm.

## Branch by abstraction

Thay vì long-lived Git branch, tạo abstraction trong mainline để old/new implementations cùng compile. Sau đó migrate callers, switch implementation bằng config/feature flag rồi xóa old path.

Technique này giảm merge divergence và cho phép incremental integration.

## Expand-contract

Khi thay API/schema, trước tiên **expand** để cả old/new clients hoạt động; migrate traffic/data; cuối cùng **contract** xóa compatibility path.

Ví dụ rename DB column an toàn thường thêm column mới, dual-read/write hoặc backfill, migrate readers rồi mới drop old column. Rename trực tiếp là một-step change nhưng distributed deployment hiếm khi atomic.

## Dual write và shadow traffic

Dual write giúp so sánh systems nhưng tạo consistency problem nếu một write thành công và một thất bại. Outbox/change-data-capture thường đáng tin hơn naive dual-write.

Shadow traffic gửi copy request sang new path nhưng không dùng response để user, giúp đo compatibility/performance trước cutover. Cần tránh duplicate side effects.

## Migration invariant

Mỗi phase phải định nghĩa invariant: source of truth là đâu, rollback có thể quay về không, data format nào cả hai versions hiểu, metric nào xác nhận correctness.

Không có invariant, migration trở thành chuỗi manual steps khó phục hồi.

## Reversibility

Feature flag chỉ giúp rollback nếu data/schema changes còn backward compatible. Một migration destructive có thể làm binary rollback vô dụng.

Deployment safety vì vậy phải reasoning code + data + protocol cùng lúc.

## Mental Model

> Large-scale refactoring là thiết kế chuỗi trạng thái trung gian an toàn. Đích cuối quan trọng, nhưng engineering difficulty nằm ở mọi bước giữa old và new phải deployable, observable và có đường phục hồi.