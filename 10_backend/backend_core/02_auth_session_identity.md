# 02. Auth, session và identity

## Tách ba câu hỏi

1. **Authentication**: request chứng minh là ai bằng credential nào?
2. **Identity**: hệ thống biểu diễn subject, tenant, role và assurance ra sao?
3. **Authorization**: subject đó được phép làm hành động nào trên resource nào?

`401` thường nói credential thiếu/không hợp lệ; `403` nói identity đã biết
nhưng không có quyền. Không suy ra quyền từ một field do client gửi lên. Server
phải lấy subject từ session/token đã verify rồi kiểm tra ownership/tenant ở
domain boundary.

## Session và token

Cookie session lưu một định danh ngẫu nhiên, state nằm server-side; cần expiry,
rotation, revoke và cookie flags (`Secure`, `HttpOnly`, `SameSite`). Access token
stateless giảm lookup nhưng revoke khó hơn; refresh token nên ngắn phạm vi, xoay
vòng và phát hiện reuse. Không log secret, token đầy đủ hoặc password.

CSRF là vấn đề của credential tự động gửi (đặc biệt cookie), không phải lý do để
bỏ authorization. CORS cũng không phải authentication. Password phải được hash
bằng password KDF phù hợp và reset flow cần token một lần, expiry ngắn.

## Authorization model

RBAC hữu ích cho role coarse-grained; ownership, tenant isolation và policy theo
attribute cần kiểm tra ở use case. Kiểm tra ở UI chỉ là trải nghiệm. Mọi đường
đi (HTTP, job, admin script, event consumer) phải gọi cùng policy/invariant.

## Failure modes

- session fixation sau login nếu không rotate session ID;
- token hết hạn giữa request và retry;
- cache response của user này cho user khác;
- chỉ kiểm tra `tenant_id` ở query chính nhưng quên query phụ;
- logout chỉ xóa UI nhưng refresh token vẫn còn hiệu lực.

Security internals và threat model thuộc [Computer Science Security](../../computer_science/07_security_reliability/README.md); chapter này tập trung vào boundary ứng dụng.

## Đào sâu: identity propagation

Identity không chỉ là `user_id`. Một request thường mang subject, tenant, auth
method, assurance level, session age, scopes và actor-on-behalf-of. Context này
phải được truyền qua use case và job có chủ ý; không serialize toàn bộ HTTP
request vào queue rồi coi đó là authorization.

Job chạy sau khi user logout hoặc role bị thu hồi cần policy rõ ràng: snapshot
authorization tại thời điểm enqueue, just-in-time authorization tại worker, hoặc
hybrid với scope snapshot và kiểm tra tenant/kill switch hiện tại. Lựa chọn này
phải nằm trong contract vì nó quyết định rủi ro và UX.

Rotation tạo credential mới khi login, đổi đặc quyền hoặc refresh. Revocation cần
source of truth dùng được cho nhiều instance; không dựa vào process memory. Clock
skew và retry có thể làm refresh token bị dùng hai lần, nên cần detect reuse và
policy revoke token family.

## Bài tập suy luận

Phân tích endpoint tải file: user có role lúc tạo signed URL nhưng bị revoke trước
lúc download. Quyết định URL expiry, authorization tại issuance và storage, audit
event, cache policy và cách ngăn URL bị chia sẻ ngoài tenant.

## Privacy và vòng đời dữ liệu identity

Identity data có lifecycle: collect tối thiểu → dùng theo purpose → retain trong
thời hạn → archive/delete → chứng minh đã xóa hoặc đã anonymize. Audit log cần
đủ để điều tra nhưng không nên sao chép password, access token, full cookie,
payment secret hay payload nhạy cảm. Redaction phải xảy ra trước khi log/trace
serialize; hash/pseudonymize chỉ có ý nghĩa nếu secret mapping được bảo vệ.

Deletion không đơn giản là xóa row chính: session, refresh-token family, cache,
search index, export, backup và event replay đều có retention policy riêng. Ghi
rõ SLA và eventual deletion state, tránh hứa “xóa ngay lập tức” khi bản sao còn
tồn tại hợp pháp. Authorization của admin/support cũng cần actor, reason, scope
và audit trail; không dùng quyền vận hành như bypass không ghi dấu.
