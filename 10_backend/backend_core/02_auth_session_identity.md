# 02. Auth, session và định danh (identity / 식별자)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **02. Auth, session và định danh (identity / 식별자)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tách ba câu hỏi** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **Session và đơn vị từ (token / 토큰)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối auth, session và identity, để phân biệt người dùng là ai, phiên nào đang hoạt động và quyền nào được cấp.

## Tách ba câu hỏi

1. **Authentication**: yêu cầu (request / 요청) chứng minh là ai bằng credential nào?
2. **định danh (identity / 식별자)**: hệ thống biểu diễn subject, tenant, role và assurance ra sao?
3. **Authorization**: subject đó được phép làm hành động nào trên tài nguyên (resource / 자원) nào?

`401` thường nói credential thiếu/không hợp lệ; `403` nói định danh (identity / 식별자) đã biết
nhưng không có quyền. Không suy ra quyền từ một trường dữ liệu (field / 필드) do máy khách (client / 클라이언트) gửi lên. máy chủ (server / 서버)
phải lấy subject từ session/đơn vị từ (token / 토큰) đã verify rồi kiểm tra quyền sở hữu (ownership / 소유권)/tenant ở
lĩnh vực (domain / 도메인) ranh giới (boundary / 경계).

> **Chuyển mạch:** Ba câu hỏi authentication, identity và authorization tách credential khỏi quyền; **Session và token** cho thấy credential được lưu, xoay vòng và thu hồi như thế nào trước khi kiểm tra policy.

## Session và đơn vị từ (token / 토큰)

Cookie session lưu một định danh ngẫu nhiên, trạng thái (state / 상태) nằm server-side; cần expiry,
rotation, revoke và cookie flags (`Secure`, `HttpOnly`, `SameSite`). truy cập (access / 접근) đơn vị từ (token / 토큰)
stateless giảm lookup nhưng revoke khó hơn; refresh đơn vị từ (token / 토큰) nên ngắn phạm vi, xoay
vòng và phát hiện reuse. Không log secret, đơn vị từ (token / 토큰) đầy đủ hoặc password.

CSRF là vấn đề của credential tự động gửi (đặc biệt cookie), không phải lý do để
bỏ authorization. CORS cũng không phải authentication. Password phải được băm (hash / 해시)
bằng password KDF phù hợp và reset luồng (flow / 흐름) cần đơn vị từ (token / 토큰) một lần, expiry ngắn.

> **Chuyển mạch:** Session/token chỉ chứng minh credential và context; **Authorization model** quyết định subject được làm gì trên resource nào, kể cả qua job hoặc admin path.

## Authorization mô hình (model / 모델)

RBAC hữu ích cho role coarse-grained; quyền sở hữu (ownership / 소유권), tenant isolation và chính sách (policy / 정책) theo
attribute cần kiểm tra ở use trường hợp (case / 사례). Kiểm tra ở UI chỉ là trải nghiệm. Mọi đường
đi (HTTP, job, admin script, event consumer) phải gọi cùng chính sách (policy / 정책)/bất biến (invariant / 불변식).

> **Chuyển mạch:** Khi policy đã được xác định, các failure mode cho thấy ranh giới bị phá ở session fixation, cache key, tenant query hoặc stale token; phần identity propagation theo dõi context qua các boundary đó.

## Thất bại (failure / 실패) modes

- session fixation sau login nếu không rotate session ID;
- đơn vị từ (token / 토큰) hết hạn giữa yêu cầu (request / 요청) và thử lại (retry / 재시도);
- bộ nhớ đệm (cache / 캐시) phản hồi (response / 응답) của người dùng (user / 사용자) này cho người dùng (user / 사용자) khác;
- chỉ kiểm tra `tenant_id` ở truy vấn (query / 쿼리) chính nhưng quên truy vấn (query / 쿼리) phụ;
- logout chỉ xóa UI nhưng refresh đơn vị từ (token / 토큰) vẫn còn hiệu lực.

Bảo mật (security / 보안) internals và threat mô hình (model / 모델) thuộc [Computer Science Security](../../computer_science/07_security_reliability/README.md); chapter này tập trung vào ranh giới (boundary / 경계) ứng dụng.

> **Chuyển mạch:** Identity propagation biến các failure mode thành câu hỏi vận hành: actor, tenant, assurance và scope nào còn đúng khi request trở thành job; bài tập tiếp theo dùng một signed URL để kiểm tra lựa chọn đó.

## Đào sâu: định danh (identity / 식별자) propagation

Định danh (identity / 식별자) không chỉ là `user_id`. Một yêu cầu (request / 요청) thường mang subject, tenant, auth
phương thức (method / 메서드), assurance mức (level / 수준), session age, scopes và actor-on-behalf-of. ngữ cảnh (context / 맥락) này
phải được truyền qua use trường hợp (case / 사례) và job có chủ ý; không serialize toàn bộ HTTP
yêu cầu (request / 요청) vào hàng đợi (queue / 큐) rồi coi đó là authorization.

Job chạy sau khi người dùng (user / 사용자) logout hoặc role bị thu hồi cần chính sách (policy / 정책) rõ ràng: snapshot
authorization tại thời điểm enqueue, just-in-time authorization tại worker, hoặc
hybrid với phạm vi (scope / 범위) snapshot và kiểm tra tenant/kill switch hiện tại. Lựa chọn này
phải nằm trong đặc tả hợp đồng (contract / 계약) vì nó quyết định rủi ro và UX.

Rotation tạo credential mới khi login, đổi đặc quyền hoặc refresh. Revocation cần
nguồn chuẩn (source of truth / 정본) dùng được cho nhiều instance; không dựa vào tiến trình (process / 프로세스) bộ nhớ (memory / 메모리). Clock
skew và thử lại (retry / 재시도) có thể làm refresh đơn vị từ (token / 토큰) bị dùng hai lần, nên cần detect reuse và
chính sách (policy / 정책) revoke đơn vị từ (token / 토큰) family.

> **Chuyển mạch:** Bài tập signed URL buộc phân biệt authorization lúc cấp quyền với lúc sử dụng; **Privacy và vòng đời dữ liệu identity** mở rộng cùng ranh giới sang retention, deletion và audit trail.

## Bài tập suy luận

Phân tích endpoint tải tệp (file / 파일): người dùng (user / 사용자) có role lúc tạo signed URL nhưng bị revoke trước
lúc download. Quyết định URL expiry, authorization tại issuance và lưu trữ (storage / 저장소), kiểm tra (audit / 감사)
sự kiện (event / 이벤트), bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책) và cách ngăn URL bị chia sẻ ngoài tenant.

> **Chuyển mạch:** Quyết định authorization phải đi cùng lifecycle của credential và dữ liệu; phần privacy kiểm tra bản sao, backup, cache và log có còn giữ quyền truy cập sau deletion hay không.

## Privacy và vòng đời dữ liệu định danh (identity / 식별자)

Định danh (identity / 식별자) dữ liệu (data / 데이터) có vòng đời (lifecycle / 생명주기): collect tối thiểu → dùng theo purpose → retain trong
thời hạn → archive/delete → chứng minh đã xóa hoặc đã anonymize. nhật ký kiểm tra (audit log / 감사 로그) cần
đủ để điều tra nhưng không nên sao chép password, truy cập (access / 접근) đơn vị từ (token / 토큰), full cookie,
payment secret hay payload nhạy cảm. Redaction phải xảy ra trước khi log/dấu vết (trace / 추적)
serialize; băm (hash / 해시)/pseudonymize chỉ có ý nghĩa nếu secret ánh xạ (mapping / 매핑) được bảo vệ.

Deletion không đơn giản là xóa row chính: session, refresh-token family, bộ nhớ đệm (cache / 캐시),
tìm kiếm (search / 검색) chỉ mục (index / 인덱스), export, backup và sự kiện (event / 이벤트) replay đều có retention chính sách (policy / 정책) riêng. Ghi
rõ SLA và eventual deletion trạng thái (state / 상태), tránh hứa “xóa ngay lập tức” khi bản sao còn
tồn tại hợp pháp. Authorization của admin/hỗ trợ (support / 지원) cũng cần actor, reason, phạm vi (scope / 범위)
và kiểm tra (audit / 감사) trail; không dùng quyền vận hành như bypass không ghi dấu.

> **Bàn giao:** Sau **Privacy và vòng đời dữ liệu identity**, giữ lại nguyên tắc least privilege, propagation có chủ ý và deletion có bằng chứng; quay về [Backend cốt lõi README](./README.md) để nối sang persistence hoặc observability.
