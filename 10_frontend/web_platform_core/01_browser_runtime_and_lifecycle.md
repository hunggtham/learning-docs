# Browser runtime và lifecycle

JavaScript language là một phần của browser application, không phải toàn bộ
browser. ECMAScript cung cấp execution semantics; browser cung cấp realm,
`Window`, `Document`, event loop, timers, networking, storage, rendering và
security policy.

## Host environment

Một document có global object, browsing context, origin và lifecycle riêng.
Navigation có thể thay document nhưng không nhất thiết thay tab; iframe có
context/origin riêng; Web Worker có global scope khác và không có DOM. Vì vậy
`window`, `document`, module state, cache và framework root không đồng nhất về
identity hoặc lifetime.

Khi một screen bị dispose, mọi listener, timer, subscription, request và worker
liên quan phải có đường cleanup. Giữ một closure sống lâu hơn document có thể
giữ DOM subtree và data trong memory dù người dùng không còn nhìn thấy nó.

## Event loop và rendering opportunity

JavaScript chạy task trên execution stack. Promise continuation chạy trong
microtask checkpoint; timers, input và network callback đi vào task queues theo
host scheduling. Browser chỉ có thể render giữa những thời điểm phù hợp, vì
microtask hoặc synchronous work quá dài có thể trì hoãn paint dù logic “đã
xong”. `requestAnimationFrame` diễn đạt ý định chạy gần frame kế tiếp nhưng
không phải cam kết frame luôn được tạo.

Đừng dùng thứ tự gọi API làm bằng chứng về thứ tự observable. Hãy ghi timeline
với task, microtask, render opportunity, network response và user intent. Đây
là cách phát hiện reentrancy, stale update và long task.

## Lifecycle contract

Mỗi operation nên có `created → active → settled/cancelled → disposed` state.
Cleanup phải idempotent: gọi hai lần không tạo side effect thứ hai. Khi context
đổi (navigation, logout, component unmount, WebSquare scope destroy), operation
phải bị cancel hoặc bị vô hiệu hóa bằng generation/ownership check trước khi
commit state.

Chi tiết language nằm ở [JavaScript track](../javascript/javascript_beginner_rebuilt.md);
chi tiết page/scope nằm ở [WebSquare runtime](../websquare/01_platform_runtime_page_model.md).
