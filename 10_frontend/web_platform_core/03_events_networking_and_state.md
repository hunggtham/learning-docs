# Events, networking và state ownership

Frontend behavior thường là kết quả của hai luồng cùng lúc: user intent đi qua
event system và resource/response đi qua network. Sai lầm phổ biến là coi
callback đến sau là intent mới nhất hoặc coi request hoàn tất đồng nghĩa UI
được phép commit.

## Event semantics

Một event có capture, target và bubble phase; default action có thể chạy sau
dispatch nếu không bị ngăn. Keyboard, pointer, focus và input có semantics
khác nhau; delegation phải giữ target, currentTarget, focus order và keyboard
behavior. Framework event abstraction chỉ là lớp dispatch thêm, không xóa
capture/bubble hoặc native default action.

## Request và stale result

Mỗi request cần identity, owner, deadline và cancellation policy. Khi người dùng
đổi filter hoặc rời màn hình, request cũ có thể vẫn trả về; `AbortController`
giúp dừng work hỗ trợ abort nhưng không thay thế generation check ở nơi commit.
Một state transition an toàn thường kiểm tra `operationId`, session/context và
component/page lifetime trước khi ghi state.

Retry, cache và optimistic update phải nêu rõ side effect, idempotency và
rollback/reconciliation. HTTP status hoặc schema validation là contract với
backend, không phải authorization của client.

## Chọn source of truth

Giữ server state, form draft, URL state, local cache và derived presentation
ở boundaries khác nhau. Nếu hai owner cùng ghi một field, race không biến mất
bằng cách thêm một state library; cần invariant, ordering và conflict policy.

Chi tiết JS async nằm ở [JavaScript intermediate](../javascript/javascript_intermediate.md),
API contract ở [Backend Core](../../10_backend/backend_core/README.md), còn
React/WebSquare chỉ mô tả cách họ tổ chức ownership trong framework.
