# Trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) và vòng đời (lifecycle / 생명주기)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) và vòng đời (lifecycle / 생명주기)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Host môi trường (environment / 환경)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Vòng lặp sự kiện (event loop / 이벤트 루프) và rendering opportunity** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối browser runtime với lifecycle, event loop và rendering, để theo dõi một thao tác người dùng đến lúc giao diện cập nhật.

JavaScript ngôn ngữ (language / 언어) là một phần của trình duyệt (browser / 브라우저) ứng dụng (application / 애플리케이션), không phải toàn bộ
trình duyệt (browser / 브라우저). ECMAScript cung cấp thực thi (execution / 실행) ngữ nghĩa (semantics / 의미론); trình duyệt (browser / 브라우저) cung cấp realm,
`Window`, `Document`, vòng lặp sự kiện (event loop / 이벤트 루프), timers, networking, lưu trữ (storage / 저장소), rendering và
bảo mật (security / 보안) chính sách (policy / 정책).

## Host môi trường (environment / 환경)

Một document có toàn cục (global / 전역) đối tượng (object / 객체), browsing ngữ cảnh (context / 맥락), origin và vòng đời (lifecycle / 생명주기) riêng.
điều hướng (navigation / 내비게이션) có thể thay document nhưng không nhất thiết thay tab; iframe có
ngữ cảnh (context / 맥락)/origin riêng; Web Worker có toàn cục (global / 전역) phạm vi (scope / 범위) khác và không có DOM. Vì vậy
`window`, `document`, mô-đun (module / 모듈) trạng thái (state / 상태), bộ nhớ đệm (cache / 캐시) và khung phần mềm (framework / 프레임워크) gốc (root / 루트) không đồng nhất về
định danh (identity / 식별자) hoặc thời gian tồn tại (lifetime / 수명).

Khi một screen bị dispose, mọi listener, timer, subscription, yêu cầu (request / 요청) và worker
liên quan phải có đường cleanup. Giữ một closure sống lâu hơn document có thể
giữ DOM subtree và dữ liệu (data / 데이터) trong bộ nhớ (memory / 메모리) dù người dùng không còn nhìn thấy nó.

Host environment cung cấp task queue, timing và rendering opportunity; event loop quyết định callback và frame, còn lifecycle contract kiểm tra boundary khi document hoặc page đổi trạng thái.

## Vòng lặp sự kiện (event loop / 이벤트 루프) và rendering opportunity

JavaScript chạy tác vụ (task / 작업) trên thực thi (execution / 실행) ngăn xếp (stack / 스택). Promise continuation chạy trong
microtask checkpoint; timers, đầu vào (input / 입력) và mạng (network / 네트워크) callback đi vào tác vụ (task / 작업) queues theo
host scheduling. trình duyệt (browser / 브라우저) chỉ có thể kết xuất (render / 렌더링) giữa những thời điểm phù hợp, vì
microtask hoặc synchronous công việc (work / 작업) quá dài có thể trì hoãn paint dù lô-gic (logic / 논리) “đã
xong”. `requestAnimationFrame` diễn đạt ý định chạy gần frame kế tiếp nhưng
không phải cam kết frame luôn được tạo.

Đừng dùng thứ tự gọi API làm bằng chứng về thứ tự observable. Hãy ghi timeline
với tác vụ (task / 작업), microtask, kết xuất (render / 렌더링) opportunity, mạng (network / 네트워크) phản hồi (response / 응답) và người dùng (user / 사용자) intent. Đây
là cách phát hiện reentrancy, stale cập nhật (update / 업데이트) và long tác vụ (task / 작업).

Event loop và rendering opportunity tạo các mốc execution có thể quan sát; lifecycle contract dùng chúng để định nghĩa cleanup, visibility và cancellation, tránh giữ state quá thời gian sống.

## Vòng đời (lifecycle / 생명주기) đặc tả hợp đồng (contract / 계약)

Mỗi thao tác (operation / 연산) nên có `created → active → settled/cancelled → disposed` trạng thái (state / 상태).
Cleanup phải idempotent: gọi hai lần không tạo side tác động (effect / 효과) thứ hai. Khi ngữ cảnh (context / 맥락)
đổi (navigation, logout, component unmount, WebSquare scope destroy), thao tác (operation / 연산)
phải bị cancel hoặc bị vô hiệu hóa bằng generation/quyền sở hữu (ownership / 소유권) check trước khi
lần ghi nhận (commit / 커밋) trạng thái (state / 상태).

Chi tiết ngôn ngữ (language / 언어) nằm ở [JavaScript track](../javascript/javascript_beginner_rebuilt.md);
chi tiết page/phạm vi (scope / 범위) nằm ở [WebSquare runtime](../websquare/01_platform_runtime_page_model.md).

> **Bàn giao:** Sau **Vòng đời (lifecycle / 생명주기) đặc tả hợp đồng (contract / 계약)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
