# API/schema compatibility và evolutionary design

Một API production hiếm khi có thời điểm tất cả producers và consumers upgrade cùng lúc. Trong rolling deployment, mobile app, external integration hoặc event stream, nhiều versions phải cùng tồn tại. Vì vậy compatibility không phải polish; nó là điều kiện để hệ thống **evolve without coordinated stop-the-world upgrade**.

## Compatibility có hướng

**Backward compatibility** thường nghĩa consumer mới vẫn hiểu data/request cũ hoặc API mới không phá client cũ, tùy context. **Forward compatibility** nói thành phần cũ có thể chịu được data từ version mới ở mức thiết kế cho phép.

Vì thuật ngữ dễ gây nhầm, engineering document nên viết rõ producer version nào nói chuyện với consumer version nào thay vì chỉ ghi “backward compatible”.

## Additive change thường an toàn hơn destructive change

Thêm optional field thường dễ tương thích hơn rename/remove field. Nhưng “optional” phải có semantic default rõ. Nếu consumer cũ bỏ qua field mới nhưng field đó thay đổi meaning của request, wire format vẫn parse được nhưng business compatibility đã hỏng.

Compatibility có ít nhất ba tầng: **syntactic**, **semantic**, **operational**.

## Tolerant reader có giới hạn

Consumer nên bỏ qua unknown fields khi protocol cho phép để producer có thể mở rộng. Nhưng quá tolerant với malformed/ambiguous data có thể che bug hoặc security issue.

Robustness không có nghĩa accept mọi thứ; contract phải xác định extension points nào được phép và invariant nào phải reject.

## Enum là một compatibility trap

Producer thêm enum value mới có thể làm consumer cũ crash nếu code giả định exhaustive set cố định. Với public/event contracts, consumer cần strategy cho unknown value: map `UNKNOWN`, preserve raw value hoặc fail theo policy có chủ đích.

Compiler exhaustiveness rất hữu ích trong code nội bộ nhưng boundary evolving cần thiết kế riêng.

## Database schema evolution

Rename column trực tiếp có thể phá old application instances trong rolling deploy. Pattern an toàn hơn thường là **expand → migrate → contract**: thêm representation mới tương thích, deploy code có thể đọc/ghi theo transition, backfill data, chuyển traffic, rồi chỉ xóa field cũ khi không còn consumer.

Mỗi bước phải rollback được trong phạm vi hợp lý. Migration schema và application deployment là một protocol nhiều version.

## Event schema khó hơn request/response

Event có thể được lưu và replay nhiều tháng sau. Consumer mới có thể đọc event rất cũ; consumer cũ có thể vẫn chạy khi producer mới publish. Schema registry/versioning giúp quản lý structure nhưng không tự đảm bảo semantic compatibility.

Nếu field `amount` đổi từ gross sang net mà vẫn cùng tên/type, schema checker có thể không phát hiện breaking semantic change.

## Consumer-driven contract

Provider không phải lúc nào biết consumer phụ thuộc vào behavior nào. Contract testing có thể capture expectations quan trọng từ consumers và chạy chúng trước khi provider release.

Tuy nhiên test không thay thế version policy. Nếu hàng trăm consumer contracts encode accidental behavior, provider có thể bị đóng băng. Contract cần tập trung vào supported behavior.

## Versioning endpoint không giải quyết mọi thứ

`/v1` và `/v2` cho phép breaking change rõ ràng nhưng tạo cost duy trì hai systems. Nếu mọi thay đổi nhỏ đều tạo version mới, migration debt tăng nhanh. Additive evolution trong cùng major version thường rẻ hơn; major version dành cho semantic break thực sự.

## Deprecation là lifecycle

Một field/API không biến mất chỉ vì documentation ghi deprecated. Cần telemetry biết consumer nào còn dùng, communication, deadline, migration path và enforcement. Unknown consumers là lý do observability tại boundary rất quan trọng.

## Mental model

> API evolution là distributed migration qua thời gian. Một change an toàn phải xét old/new producer × old/new consumer, không chỉ compile version hiện tại. Expand trước, migrate usage, quan sát, rồi contract. Compatibility tốt giảm nhu cầu coordinated release và làm architecture có khả năng thay đổi lâu dài.