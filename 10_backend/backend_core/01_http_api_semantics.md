# 01. HTTP API ngữ nghĩa (semantics / 의미론)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **01. HTTP API ngữ nghĩa (semantics / 의미론)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **API là đặc tả hợp đồng (contract / 계약)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Idempotency và tính đồng thời (concurrency / 동시성)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối HTTP API semantics với resource, method, status và error contract, để client và server cùng hiểu một request như thế nào.

## API là đặc tả hợp đồng (contract / 계약)

Đặc tả API (API contract / API 계약) gồm tài nguyên (resource / 자원) biểu diễn (representation / 표현), phương thức (method / 메서드), status mã (code / 코드), headers, lỗi (error / 오류)
shape, pagination, versioning và tính tương thích (compatibility / 호환성) chính sách (policy / 정책). URL đẹp không cứu được
đặc tả hợp đồng (contract / 계약) mơ hồ: máy khách (client / 클라이언트) cần biết yêu cầu (request / 요청) nào có side tác động (effect / 효과), có thể thử lại (retry / 재시도) hay
không, và phản hồi (response / 응답) nào là authoritative.

| Ý định | ngữ nghĩa (semantics / 의미론) cần làm rõ |
|---|---|
| đọc collection | filter, sort, cursor/page, empty kết quả (result / 결과) |
| tạo tài nguyên (resource / 자원) | `POST`, kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류), location/id trả về |
| thay thế một tài nguyên (resource / 자원) | `PUT` thường idempotent, biểu diễn (representation / 표현) đầy đủ |
| chỉnh một phần | `PATCH`, merge/thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론) |
| xóa | `DELETE`, hard/soft delete, repeated yêu cầu (request / 요청) |
| xử lý async | `202`, job status và terminal trạng thái (state / 상태) |

`200`, `201`, `202`, `204`, `400`, `401`, `403`, `404`, `409`, `412`, `422`,
`429` và `5xx` không phải các nhãn tùy ý. Chúng giúp máy khách (client / 클라이언트) quyết định hiển
thị, thử lại (retry / 재시도), sửa đầu vào (input / 입력) hoặc báo sự cố (incident / 인시던트). lỗi (error / 오류) phản hồi (response / 응답) nên có mã (code / 코드) ổn định,
message dành cho người đọc, trường dữ liệu (field / 필드) đường dẫn (path / 경로) (nếu validation) và yêu cầu (request / 요청) ID.

> **Chuyển mạch:** API contract chỉ có giá trị khi retry và concurrent request không tạo side effect ngoài invariant; **Idempotency và concurrency** chuyển contract đó thành điều kiện có thể kiểm tra.

## Idempotency và tính đồng thời (concurrency / 동시성)

Phương thức (method / 메서드) idempotent không đồng nghĩa yêu cầu (request / 요청) không có side tác động (effect / 효과); nó nghĩa là gửi
lại cùng yêu cầu (request / 요청) có cùng hiệu ứng cuối cùng. Với tạo thanh toán hoặc lệnh quan
trọng, dùng `Idempotency-Key` được lưu cùng kết quả và yêu cầu (request / 요청) fingerprint.
`ETag`/`If-Match` hoặc phiên bản (version / 버전) number giúp phát hiện lost cập nhật (update / 업데이트) thay vì âm thầm
ghi đè thay đổi của máy khách (client / 클라이언트) khác.

> **Chuyển mạch:** Khi idempotency và concurrency đã rõ, compatibility trả lời câu hỏi thay đổi contract mà client cũ vẫn có thể hiểu đến đâu; checklist sau đó biến câu hỏi thành bước review cụ thể.

## Tính tương thích (compatibility / 호환성)

Thêm trường dữ liệu (field / 필드) thường tương thích hơn đổi nghĩa trường dữ liệu (field / 필드). Không đổi kiểu dữ liệu, enum
hay nullability mà không có di chuyển (migration / 마이그레이션) plan. phiên bản (version / 버전) theo đặc tả hợp đồng (contract / 계약) và năng lực (capability / 역량),
không tạo phiên bản (version / 버전) mới chỉ vì hiện thực (implementation / 구현) refactor. Pagination nên ổn định
dưới concurrent writes; cursor thường ít gây duplicate/skip hơn offset ở bảng
lớn.

> **Chuyển mạch:** Checklist rà soát các status, method, representation và failure contract; phần đào sâu compatibility giải thích vì sao một thay đổi nhỏ có thể phá client hoặc cache.

## Checklist rà soát (review / 검토)

- máy khách (client / 클라이언트) có biết success, kiểm tra hợp lệ (validation / 검증) thất bại (failure / 실패), auth thất bại (failure / 실패) và xung đột (conflict / 충돌) khác nhau?
- yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) và tỷ lệ (rate / 비율) limit có được phản ánh bằng header/đặc tả hợp đồng (contract / 계약) không?
- thử lại (retry / 재시도) cùng yêu cầu (request / 요청) có tạo duplicate không?
- lược đồ (schema / 스키마) có backward/forward tính tương thích (compatibility / 호환성) và deprecation cửa sổ (window / 윈도우) không?

> **Chuyển mạch:** Phần compatibility đặt quy tắc vào các thay đổi representation và version; bài tập suy luận dùng các quy tắc đó để phân biệt breaking change với thay đổi tương thích.

## Đào sâu: ngữ nghĩa (semantic / 의미적) tính tương thích (compatibility / 호환성)

Tính tương thích (compatibility / 호환성) không chỉ là JSON vẫn parse được. Một thay đổi có thể phá máy khách (client / 클라이언트)
qua bốn lớp: syntactic (field/type/header), ngữ nghĩa (semantic / 의미적) (nghĩa của `null` hoặc
enum), temporal (thứ tự event/cursor) và operational (latency, rate limit,
retry behavior). API rà soát (review / 검토) nên ghi tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬) cho producer/bên tiêu thụ (consumer / 소비자)
phiên bản (version / 버전) cũ–mới.

`ETag` là phiên bản (version / 버전) của biểu diễn (representation / 표현), không nhất thiết là băm (hash / 해시) nội dung. luồng (flow / 흐름) an
toàn cho cập nhật (update / 업데이트) là: máy khách (client / 클라이언트) đọc biểu diễn (representation / 표현) + ETag, gửi `If-Match`, máy chủ (server / 서버) chỉ
ghi nếu phiên bản (version / 버전) còn khớp, rồi trả ETag mới. `412 Precondition Failed` nói
precondition không đúng; `409 Conflict` thường dành cho xung đột (conflict / 충돌) lĩnh vực (domain / 도메인). Chọn
một convention và ghi vào đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Bài tập suy luận buộc người học theo dõi contract qua một request cụ thể; phần security và traffic policy mở rộng cùng contract sang authorization, rate limit và trust boundary.

## Bài tập suy luận

Thiết kế đặc tả hợp đồng (contract / 계약) cho `POST /exports` chạy 10 phút: phản hồi (response / 응답) đầu, job status,
cancel, duplicate `Idempotency-Key`, permission thay đổi (change / 변경) giữa chừng và retention
của kết quả. Nếu máy khách (client / 클라이언트) mất mạng ngay sau `201`, nó tìm lại tài nguyên (resource / 자원) bằng gì?

> **Chuyển mạch:** API semantics chỉ hoàn chỉnh khi request hợp lệ được gắn với principal và policy đúng; đây là điểm bàn giao sang security, không phải một checklist API riêng biệt.

## Bảo mật (security / 보안) và traffic chính sách (policy / 정책) ở API ranh giới (boundary / 경계)

Tỷ lệ (rate / 비율) limit là đặc tả hợp đồng (contract / 계약) giữa caller và máy chủ (server / 서버), không chỉ là một con số trong
gateway. Ghi rõ phạm vi (scope / 범위) (IP, subject, tenant, route), thuật toán (algorithm / 알고리즘)/cửa sổ (window / 윈도우), phản hồi (response / 응답)
`429`, `Retry-After`, burst và hành vi khi counter store lỗi. Giới hạn ở nhiều
tầng (layer / 계층) có thể cộng dồn ngoài dự kiến; cần một đơn vị sở hữu (owner / 오너) chính và chỉ số (metric / 지표) cho rejected
yêu cầu (request / 요청), remaining quota và limiter độ trễ (latency / 지연 시간).

CORS chỉ quyết định trình duyệt (browser / 브라우저) có cho JavaScript đọc phản hồi (response / 응답) hay không; nó không
thay thế authentication/authorization. `Origin`, allowed methods/headers,
credentials và preflight bộ nhớ đệm (cache / 캐시) phải được chính sách (policy / 정책) hóa. bảo mật (security / 보안) headers và body
kích thước (size / 크기)/content-type kiểm tra hợp lệ (validation / 검증) nên được áp dụng trước parser/lô-gic nghiệp vụ (business logic / 비즈니스 로직); lỗi (error / 오류)
phản hồi (response / 응답) không được phản hồi secret, dấu vết ngăn xếp (stack trace / 스택 트레이스), SQL hoặc dữ liệu của tài nguyên (resource / 자원)
khác để “giúp gỡ lỗi (debug / 디버그)”.

Kiểm tra hợp lệ (validation / 검증) nên phân biệt malformed yêu cầu (request / 요청), trường dữ liệu (field / 필드) ràng buộc (constraint / 제약조건) và lĩnh vực (domain / 도메인) xung đột (conflict / 충돌).
Dùng lỗi (error / 오류) mã (code / 코드) ổn định + trường dữ liệu (field / 필드) đường dẫn (path / 경로); message có thể thay đổi và không được trở
thành nguồn suy luận về sự tồn tại của người dùng (user / 사용자)/tài nguyên (resource / 자원) nhạy cảm.

> **Bàn giao:** Sau phần security và traffic policy, giữ lại contract, idempotency và compatibility boundary; quay về [Backend cốt lõi README](./README.md) để nối sang persistence hoặc caching.
