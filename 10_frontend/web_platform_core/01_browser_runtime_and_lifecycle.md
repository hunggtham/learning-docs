# Trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) và vòng đời (lifecycle / 생명주기)

> **Mạch đọc:** Đặt **trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) và vòng đời (lifecycle / 생명주기)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Host môi trường (environment / 환경)** sang **vòng lặp sự kiện (event loop / 이벤트 루프) và rendering opportunity**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

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


> **Chuyển mạch:** Từ **Host môi trường (environment / 환경)**, ta sang **vòng lặp sự kiện (event loop / 이벤트 루프) và rendering opportunity** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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


> **Chuyển mạch:** Từ **vòng lặp sự kiện (event loop / 이벤트 루프) và rendering opportunity**, ta sang **vòng đời (lifecycle / 생명주기) đặc tả hợp đồng (contract / 계약)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Vòng đời (lifecycle / 생명주기) đặc tả hợp đồng (contract / 계약)

Mỗi thao tác (operation / 연산) nên có `created → active → settled/cancelled → disposed` trạng thái (state / 상태).
Cleanup phải idempotent: gọi hai lần không tạo side tác động (effect / 효과) thứ hai. Khi ngữ cảnh (context / 맥락)
đổi (navigation, logout, component unmount, WebSquare scope destroy), thao tác (operation / 연산)
phải bị cancel hoặc bị vô hiệu hóa bằng generation/quyền sở hữu (ownership / 소유권) check trước khi
lần ghi nhận (commit / 커밋) trạng thái (state / 상태).

Chi tiết ngôn ngữ (language / 언어) nằm ở [JavaScript track](../javascript/javascript_beginner_rebuilt.md);
chi tiết page/phạm vi (scope / 범위) nằm ở [WebSquare runtime](../websquare/01_platform_runtime_page_model.md).

> **Bàn giao:** Sau **vòng đời (lifecycle / 생명주기) đặc tả hợp đồng (contract / 계약)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 web platform model](./00_web_platform_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
