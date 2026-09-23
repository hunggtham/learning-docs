# 01. HTTP API semantics

## API là contract

API contract gồm resource representation, method, status code, headers, error
shape, pagination, versioning và compatibility policy. URL đẹp không cứu được
contract mơ hồ: client cần biết request nào có side effect, có thể retry hay
không, và response nào là authoritative.

| Ý định | Semantics cần làm rõ |
|---|---|
| đọc collection | filter, sort, cursor/page, empty result |
| tạo resource | `POST`, validation error, location/id trả về |
| thay thế một resource | `PUT` thường idempotent, representation đầy đủ |
| chỉnh một phần | `PATCH`, merge/operation semantics |
| xóa | `DELETE`, hard/soft delete, repeated request |
| xử lý async | `202`, job status và terminal state |

`200`, `201`, `202`, `204`, `400`, `401`, `403`, `404`, `409`, `412`, `422`,
`429` và `5xx` không phải các nhãn tùy ý. Chúng giúp client quyết định hiển
thị, retry, sửa input hoặc báo incident. Error response nên có code ổn định,
message dành cho người đọc, field path (nếu validation) và request ID.

## Idempotency và concurrency

Method idempotent không đồng nghĩa request không có side effect; nó nghĩa là gửi
lại cùng request có cùng hiệu ứng cuối cùng. Với tạo thanh toán hoặc lệnh quan
trọng, dùng `Idempotency-Key` được lưu cùng kết quả và request fingerprint.
`ETag`/`If-Match` hoặc version number giúp phát hiện lost update thay vì âm thầm
ghi đè thay đổi của client khác.

## Compatibility

Thêm field thường tương thích hơn đổi nghĩa field. Không đổi kiểu dữ liệu, enum
hay nullability mà không có migration plan. Version theo contract và capability,
không tạo version mới chỉ vì implementation refactor. Pagination nên ổn định
dưới concurrent writes; cursor thường ít gây duplicate/skip hơn offset ở bảng
lớn.

## Checklist review

- Client có biết success, validation failure, auth failure và conflict khác nhau?
- Request timeout và rate limit có được phản ánh bằng header/contract không?
- Retry cùng request có tạo duplicate không?
- Schema có backward/forward compatibility và deprecation window không?

## Đào sâu: semantic compatibility

Compatibility không chỉ là JSON vẫn parse được. Một thay đổi có thể phá client
qua bốn lớp: syntactic (field/type/header), semantic (nghĩa của `null` hoặc
enum), temporal (thứ tự event/cursor) và operational (latency, rate limit,
retry behavior). API review nên ghi compatibility matrix cho producer/consumer
version cũ–mới.

`ETag` là version của representation, không nhất thiết là hash nội dung. Flow an
toàn cho update là: client đọc representation + ETag, gửi `If-Match`, server chỉ
ghi nếu version còn khớp, rồi trả ETag mới. `412 Precondition Failed` nói
precondition không đúng; `409 Conflict` thường dành cho conflict domain. Chọn
một convention và ghi vào contract.

## Bài tập suy luận

Thiết kế contract cho `POST /exports` chạy 10 phút: response đầu, job status,
cancel, duplicate `Idempotency-Key`, permission change giữa chừng và retention
của kết quả. Nếu client mất mạng ngay sau `201`, nó tìm lại resource bằng gì?

## Security và traffic policy ở API boundary

Rate limit là contract giữa caller và server, không chỉ là một con số trong
gateway. Ghi rõ scope (IP, subject, tenant, route), algorithm/window, response
`429`, `Retry-After`, burst và hành vi khi counter store lỗi. Giới hạn ở nhiều
layer có thể cộng dồn ngoài dự kiến; cần một owner chính và metric cho rejected
request, remaining quota và limiter latency.

CORS chỉ quyết định browser có cho JavaScript đọc response hay không; nó không
thay thế authentication/authorization. `Origin`, allowed methods/headers,
credentials và preflight cache phải được policy hóa. Security headers và body
size/content-type validation nên được áp dụng trước parser/business logic; error
response không được phản hồi secret, stack trace, SQL hoặc dữ liệu của resource
khác để “giúp debug”.

Validation nên phân biệt malformed request, field constraint và domain conflict.
Dùng error code ổn định + field path; message có thể thay đổi và không được trở
thành nguồn suy luận về sự tồn tại của user/resource nhạy cảm.
