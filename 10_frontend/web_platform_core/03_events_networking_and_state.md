# Events, networking và quyền sở hữu trạng thái (state ownership / 상태 소유권)

> **Mạch đọc:** Đặt **Events, networking và quyền sở hữu trạng thái (state ownership / 상태 소유권)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론)** sang **yêu cầu (request / 요청) và stale kết quả (result / 결과)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Frontend hành vi (behavior / 동작) thường là kết quả của hai luồng cùng lúc: người dùng (user / 사용자) intent đi qua
sự kiện (event / 이벤트) hệ thống (system / 시스템) và tài nguyên (resource / 자원)/phản hồi (response / 응답) đi qua mạng (network / 네트워크). Sai lầm phổ biến là coi
callback đến sau là intent mới nhất hoặc coi yêu cầu (request / 요청) hoàn tất đồng nghĩa UI
được phép lần ghi nhận (commit / 커밋).

## Sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론)

Một sự kiện (event / 이벤트) có capture, mục tiêu (target / 대상) và bubble phase; default hành động (action / 동작) có thể chạy sau
dispatch nếu không bị ngăn. Keyboard, pointer, focus và đầu vào (input / 입력) có ngữ nghĩa (semantics / 의미론)
khác nhau; delegation phải giữ mục tiêu (target / 대상), currentTarget, focus thứ tự (order / 순서) và keyboard
hành vi (behavior / 동작). khung phần mềm (framework / 프레임워크) sự kiện (event / 이벤트) lớp trừu tượng (abstraction / 추상화) chỉ là lớp dispatch thêm, không xóa
capture/bubble hoặc bản địa (native / 네이티브) default hành động (action / 동작).


> **Chuyển mạch:** Từ **sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론)**, ta sang **yêu cầu (request / 요청) và stale kết quả (result / 결과)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Yêu cầu (request / 요청) và stale kết quả (result / 결과)

Mỗi yêu cầu (request / 요청) cần định danh (identity / 식별자), đơn vị sở hữu (owner / 오너), deadline và cancellation chính sách (policy / 정책). Khi người dùng
đổi filter hoặc rời màn hình, yêu cầu (request / 요청) cũ có thể vẫn trả về; `AbortController`
giúp dừng công việc (work / 작업) hỗ trợ abort nhưng không thay thế generation check ở nơi lần ghi nhận (commit / 커밋).
Một chuyển tiếp trạng thái (state transition / 상태 전이) an toàn thường kiểm tra `operationId`, session/ngữ cảnh (context / 맥락) và
thành phần (component / 컴포넌트)/page thời gian tồn tại (lifetime / 수명) trước khi ghi trạng thái (state / 상태).

Thử lại (retry / 재시도), bộ nhớ đệm (cache / 캐시) và optimistic cập nhật (update / 업데이트) phải nêu rõ side tác động (effect / 효과), idempotency và
quay lui (rollback / 롤백)/reconciliation. HTTP status hoặc lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) là đặc tả hợp đồng (contract / 계약) với
backend, không phải authorization của máy khách (client / 클라이언트).


> **Chuyển mạch:** Từ **yêu cầu (request / 요청) và stale kết quả (result / 결과)**, ta sang **Chọn nguồn chuẩn (source of truth / 정본)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chọn nguồn chuẩn (source of truth / 정본)

Giữ máy chủ (server / 서버) trạng thái (state / 상태), form draft, URL trạng thái (state / 상태), cục bộ (local / 로컬) bộ nhớ đệm (cache / 캐시) và derived presentation
ở boundaries khác nhau. Nếu hai đơn vị sở hữu (owner / 오너) cùng ghi một trường dữ liệu (field / 필드), race không biến mất
bằng cách thêm một trạng thái (state / 상태) thư viện (library / 라이브러리); cần bất biến (invariant / 불변식), thứ tự (ordering / 순서) và xung đột (conflict / 충돌) chính sách (policy / 정책).

Chi tiết JS async nằm ở [JavaScript intermediate](../javascript/javascript_intermediate.md),
Đặc tả API (API contract / API 계약) ở [Backend Core](../../10_backend/backend_core/README.md), còn
React/WebSquare chỉ mô tả cách họ tổ chức quyền sở hữu (ownership / 소유권) trong khung phần mềm (framework / 프레임워크).

> **Bàn giao:** Sau **Chọn nguồn chuẩn (source of truth / 정본)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 web platform model](./00_web_platform_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
