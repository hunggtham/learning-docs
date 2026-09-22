# 14 — Application Shell, Navigation & Multi-Screen State

WebSquare enterprise application thường không phải tập hợp các XML page độc lập. Phía trên các screen nghiệp vụ còn có **application shell**: menu, header, tab/window container, permission context, global message/loading layer, navigation history và cơ chế mở/đóng/reuse screen.

Chapter 04 đã giải thích Scope/WFrame ở mức page composition. Chapter này đi lên một tầng architecture: **khi hàng chục hoặc hàng trăm screen cùng sống trong một shell, ai sở hữu navigation state, page instance được định danh thế nào, khi nào reuse tab, khi nào tạo instance mới, và state nào được phép global?**

## 1. Shell là runtime host, không phải “page cha biết mọi thứ”

Mental model tốt:

```text
Application Shell
├─ authentication/session context
├─ menu/navigation registry
├─ tab/window host
├─ common message/loading service
└─ screen instances
   ├─ customer-list scope
   ├─ customer-detail scope
   └─ order-list scope
```

Shell cung cấp capability chung. Screen nghiệp vụ giữ business state của chính nó. Nếu shell biết ID của mọi Grid/Input trong mọi screen, architecture đã đảo ngược dependency.

Shell nên biết **screen contract**, không biết **screen internals**.

## 2. Screen definition khác screen instance

`/ui/order/list.xml` là screen definition/source. Khi mở nó hai lần với hai parameter khác nhau, có thể có hai instance.

```text
screen definition: order/list.xml

instance A: order/list.xml?customer=C001
instance B: order/list.xml?customer=C999
```

Trong WFrame/Scope architecture, mỗi instance có thể có `scwin`, DataCollection, current row, pending Submission và unsaved state riêng.

Nếu navigation registry chỉ key theo source path, instance B có thể vô tình activate A. Vì vậy cần quyết định identity policy của screen.

## 3. Navigation identity là product rule

Một menu “Employee Management” có thể chỉ cho phép một tab duy nhất. Một màn hình “Order Detail” có thể cho phép nhiều order mở song song.

Do đó tab/window key nên phản ánh intent:

```text
single-instance screen
key = MENU_EMPLOYEE

multi-instance detail
key = ORDER_DETAIL:ORD-1001
key = ORDER_DETAIL:ORD-1002
```

Không có một key strategy đúng cho mọi screen. Nhưng strategy phải explicit để tránh duplicate tab hoặc reuse nhầm state.

## 4. `openAction`/reuse policy phải khớp identity policy

TabControl/WindowContainer có option để quyết định behavior khi target đã tồn tại tùy API/build. Đừng chọn “exist/reuse” chỉ vì muốn tránh mở nhiều tab.

Reuse chỉ đúng nếu existing instance đại diện cùng logical task. Nếu user mở detail của entity khác mà app chỉ focus tab cũ không reload parameter, UI sẽ hiển thị entity sai.

Reasoning trước khi mở:

```text
logical key đã tồn tại?
→ có: activate hay refresh/reparameterize?
→ không: create instance mới
```

## 5. TabControl và WindowContainer là host có lifecycle

SP5 hỗ trợ `wframe` frame mode cho TabControl/WindowContainer để screen có Scope riêng. WindowContainer còn phục vụ MDI-style window hierarchy. Đây không chỉ là layout choice; nó quyết định isolation, `getWindow()` semantics và cleanup boundary.

Khi tạo tab/window bằng `src`, screen cần thời gian load. Shell không được giả định `addTab()`/`createWindow()` return là business screen đã data-ready.

```text
container created
→ WFrame source load
→ Scope/object ready
→ render ready
→ screen init
→ initial Submission
→ business data ready
```

Nếu shell cần gọi screen sau load, hãy dùng ready contract phù hợp thay vì timer.

## 6. `dataObject` là navigation input contract

Khi shell mở screen, parameter nên là plain data:

```javascript
var dataObject = {
    type: "json",
    name: "pageParam",
    data: {
        orderId: "ORD-1001",
        mode: "EDIT"
    }
};
```

Screen đọc bằng `$p.getParameter()` theo contract của build.

Parameter nên mô tả **ý định mở screen**, không truyền component instance hoặc mutable object của parent. Điều này cho phép cùng screen được host bởi TabControl, WindowContainer hoặc popup mà không biết topology cụ thể.

## 7. Navigation command tốt hơn direct container manipulation rải rác

Nếu mọi screen tự gọi `mainTab.addTab(...)` với option khác nhau, navigation policy bị phân tán.

Một common navigation service có thể expose capability:

```javascript
appNav.openScreen({
    screenId: "ORDER_DETAIL",
    instanceKey: orderId,
    params: { orderId: orderId }
});
```

Bên trong service mới quyết định container, tab ID, title, duplicate policy và telemetry.

Điểm quan trọng là common service không được biết `grdOrder` hoặc `dmSearch` của screen. Nó quản navigation, không quản business UI.

## 8. Global state phải nhỏ và có owner rõ

Một số state hợp lý ở shell/session level:

```text
current authenticated user identity
locale/theme
menu/permission snapshot
feature/config flags phù hợp client
navigation registry
correlation/session metadata không nhạy cảm
```

State không nên global tùy tiện:

```text
current selected customer của một tab
search condition của một screen
Grid row index
popup temporary form
pending Save flag của một page
```

Global mutable state làm nhiều instance ghi đè nhau và kéo lifetime object dài hơn cần thiết.

## 9. Permission menu khác authorization

Shell thường ẩn menu user không có quyền. Đây là UX/navigation filtering, không phải security boundary.

```text
menu permission → user có thấy/mở screen dễ dàng không
server authorization → request có được phép thực thi không
```

User có thể gọi endpoint trực tiếp hoặc sửa client state. Server vẫn phải enforce permission.

Menu cache cũng cần invalidation policy nếu quyền có thể thay đổi trong session.

## 10. Unsaved-change guard thuộc navigation protocol

Nếu user đóng tab đang có dirty DataList, screen biết “tôi có unsaved change”, còn shell biết “user đang yêu cầu close/navigation”. Hai bên cần contract.

Pattern tốt:

```text
shell asks screen: canClose?
screen checks dirty state
→ yes: close
→ no/confirm required: prompt/decision
```

Pattern xấu là shell tự inspect mọi `dl*` object của child. Điều đó couple shell vào implementation screen.

Screen có thể expose public function:

```javascript
scwin.canClose = function () {
    return !scwin.hasUnsavedChanges();
};
```

Exact invocation qua scope/container phụ thuộc topology, nhưng ownership rõ: screen đánh giá business state, shell điều phối navigation.

## 11. Close không đồng nghĩa object đã garbage-collected

Khi tab/window đóng, UI biến mất nhưng memory chỉ được giải phóng khi không còn reference reachable.

Nếu shell giữ registry:

```javascript
scwin.openScreens[screenKey] = childScope;
```

mà không remove entry khi close, child scope có thể bị giữ sống. Registry nên giữ metadata/identity tối thiểu hoặc cleanup reference đúng lifecycle.

Đây là connection trực tiếp với chapter 10 về resource lifetime.

## 12. Reuse tab và refresh state phải có contract

Giả sử tab Order List đã mở. User từ menu khác yêu cầu mở lại với filter mới.

Có ba policy khác nhau:

```text
activate only
activate + refresh with new params
close old + create new instance
```

Không nên ngầm chọn một. Nếu refresh, screen cần public capability như `applyNavigation(params)` thay vì shell set trực tiếp `dmSearch` và click button hộ.

```javascript
scwin.applyNavigation = function (params) {
    scwin.setSearchCondition(params);
    scwin.search();
};
```

## 13. Back/forward history cần định nghĩa semantic

SPA shell giữ engine sống nên browser history không tự động hiểu mọi tab switch là navigation meaningful. Legacy IFrame còn có history riêng.

Trước khi thêm back button, xác định:

```text
browser Back quay route/screen nào?
tab switch có push history không?
popup có history không?
filter/search có history không?
```

Không cố map mọi UI state vào URL/history. Chỉ state cần deep-link/recovery/share mới nên có navigation representation ổn định.

## 14. Deep link cần tách route identity và runtime instance

Một deep link có thể biểu diễn:

```text
screen = ORDER_DETAIL
orderId = ORD-1001
```

Khi app boot, shell resolve permission, load screen definition, tạo instance rồi truyền parameter. URL không nên chứa physical WFrame ID sinh ngẫu nhiên hay Grid row index.

Stable route dùng business/navigation identity; runtime ID chỉ là implementation detail.

## 15. Menu metadata không nên trở thành god configuration

Enterprise app thường có menu table chứa screen URL, title, permission, icon, open mode. Metadata hữu ích nhưng nếu nhét mọi behavior business vào menu config, debugging trở nên khó.

Menu metadata nên trả lời navigation concern. Screen behavior vẫn thuộc screen/domain code.

```text
menu config: screenId, src, title, single/multi-instance
screen code: validation, DataCollection, Submission, CRUD
```

## 16. Loading indicator cần đúng boundary

Một global spinner cho mọi request có thể tạo UX khó hiểu: background refresh ở tab A làm block tab B. Ngược lại, spinner chỉ trong Grid có thể không đủ cho operation khóa toàn screen.

Chọn loading scope theo operation ownership:

```text
component-level
screen/WFrame-level
application-level
```

TabControl/WindowContainer có mechanism hiển thị process message trong frame ở các configuration tương ứng. Hãy dùng boundary phù hợp thay vì một global boolean duy nhất.

## 17. Concurrent tabs làm race condition rõ hơn

Hai tab cùng gọi endpoint không nhất thiết có vấn đề. Vấn đề xảy ra khi chúng chia sẻ mutable client state hoặc server operation không hỗ trợ concurrency.

Ví dụ:

```text
Tab A edit customer C001
Tab B cũng edit C001
```

Client Scope isolation giữ hai form riêng, nhưng server vẫn cần optimistic locking/version. WFrame isolation không giải quyết database concurrency.

## 18. Cross-screen communication nên qua intent/event, không qua internals

Case: Detail popup save xong, List tab cần refresh.

Contract tốt:

```text
Detail emits/returns { type: "ORDER_CHANGED", orderId }
List decides whether/how to refresh
```

Contract xấu:

```text
Detail finds top tab
→ finds list frame
→ finds grdOrder
→ mutates row 7
```

Contract tốt giữ ownership và cho List quyết định re-query hay local patch.

## 19. Broadcast event cũng có trade-off

Event bus/global publish-subscribe giảm direct reference nhưng có thể tạo hidden dependency nếu dùng quá mức.

Nếu `ORDER_CHANGED` có 12 subscriber, một Save có thể trigger nhiều request ngoài dự kiến. Event contract cần naming, payload schema, ownership và unsubscribe lifecycle.

Đừng thay `parent().parent()` coupling bằng “magic global event” coupling khó trace hơn.

## 20. Screen registry nên lưu metadata hơn object graph

Registry hữu ích:

```text
screenKey
containerId/tabId
screenId/src
business instance key
title
openedAt
```

Cẩn thận khi lưu direct scope/component reference dài hạn. Nếu container recreate WFrame bằng `setSrc()`, cached reference có thể stale và giữ old object sống.

Resolve scope gần thời điểm sử dụng qua container/public API khi topology dynamic.

## 21. Adaptive frame và responsive responsibility

SP5 có `adaptiveFrame` trong TabControl/WindowContainer scenario để adaptive layout có thể dựa kích thước frame thay vì browser. Điều này quan trọng khi một screen sống trong window nhỏ hơn viewport.

Mental model:

```text
browser viewport size
≠ tab/window content size
```

Responsive logic cần biết boundary nào quyết định layout. Đừng hard-code `window.innerWidth` nếu screen thực tế phải thích ứng theo container.

## 22. Application shell cũng cần observability

Metrics/log hữu ích:

```text
screen open duration
screen ready duration
open screen count
close count
duplicate-open prevention
navigation failure
unsaved-close cancellation
per-screen memory/request growth
```

Khi user nói “mở càng nhiều tab càng chậm”, cần evidence shell-level chứ không chỉ profile một screen riêng lẻ.

## 23. Shell failure-mode matrix

```text
Mở menu nhưng tab cũ hiện data khác
→ instance key/reuse policy sai

Đóng tab rồi request vẫn chạy
→ child lifetime/cleanup chưa kết thúc

Mở cùng screen hai lần state đè nhau
→ global mutable state hoặc Scope boundary sai

Tab mới đôi lúc gọi function không tồn tại
→ object/render/data readiness race

Back button đi qua lịch sử lạ
→ browser/IFrame/SPA history semantics chưa định nghĩa

Mở 30 tab memory tăng không giảm
→ registry/listener/timer/reference leak
```

Mỗi triệu chứng nên được debug bằng topology + lifetime evidence trước khi sửa ngẫu nhiên.

## 24. Case study: menu → multi-tab detail → save → refresh

Giả sử app có Order List và cho mở nhiều Order Detail.

Shell nhận command `openScreen(ORDER_DETAIL, ORD-1001)`. Navigation key là `ORDER_DETAIL:ORD-1001`. Nếu chưa tồn tại, shell tạo WFrame tab và truyền `{orderId}`. Nếu đã tồn tại, shell activate tab đó.

Detail page giữ DataMap/DataList và Submission trong Scope riêng. Save gửi version để server kiểm tra concurrency. Khi thành công, detail trả/publish một domain event nhỏ `{type:"ORDER_CHANGED", orderId:"ORD-1001"}`. List page nếu đang mở có thể đánh dấu stale hoặc re-query theo policy. Shell không chạm Grid của List.

Khi user đóng Detail còn dirty, shell gọi public `canClose()` của instance. Nếu được đóng, registry xóa metadata/reference và page cleanup timer/listener. Đây là một flow hoàn chỉnh trong đó navigation, business state, server concurrency và lifetime có owner khác nhau nhưng contract nối chúng rõ.

## 25. Master rule cho multi-screen WebSquare

Hãy giữ bốn identity riêng:

```text
screen definition identity
screen instance identity
business entity identity
runtime frame/scope identity
```

Nhiều bug enterprise xuất hiện vì bốn identity này bị trộn thành một string hoặc một row index.

Khi architecture rõ, shell có thể thay TabControl bằng WindowContainer hoặc đổi navigation policy mà business screen ít bị ảnh hưởng.

## 26. Kết nối

Application shell điều phối screen, nhưng mọi mutation cuối cùng vẫn đi qua server contract và transaction boundary. Tiếp theo đọc [15 — Backend Contract, Transaction & Concurrency Integration](15_backend_contract_transaction_concurrency.md).
