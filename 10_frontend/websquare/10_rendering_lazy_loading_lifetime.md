# 10 — Rendering, Lazy Loading & Resource Lifetime

WebSquare screen có thể “load xong” theo nhiều nghĩa khác nhau. Source đã tải chưa? Script đã eval chưa? Scope đã tạo chưa? DataCollection đã tồn tại chưa? Component object đã được tạo chưa? DOM đã render chưa? `onpageload` đã chạy chưa? Submission đầu tiên đã hoàn thành chưa?

Nếu gom tất cả thành một từ “loaded”, code dễ tạo race condition và performance regression. Chapter này xây mental model chi tiết cho **load → instantiate → render → activate → data-ready → unload**, đặc biệt với WFrame, TabControl, preload, SPA và screen sống lâu.

## 1. Một page có nhiều mốc sẵn sàng

Hãy tách tối thiểu các trạng thái sau:

```text
source available
→ script evaluated
→ scope/data objects created
→ UI component objects created
→ DOM/render complete
→ page lifecycle callback executed
→ initial async data ready
```

Tùy component/config/build, một số bước có thể gần nhau hoặc được tối ưu khác đi. Nhưng distinction vẫn quan trọng.

Một object tồn tại không đồng nghĩa UI của nó đã render. Một page render xong không đồng nghĩa dữ liệu nghiệp vụ đã load xong.

## 2. `onpageload` không có nghĩa toàn business state đã ready

Pattern phổ biến:

```javascript
scwin.onpageload = function () {
    scwin.search();
};
```

Nếu `search()` bắt đầu Submission async, `onpageload` có thể return trước khi response về.

Do đó parent không nên suy:

```text
child onpageload đã chạy
⇒ child data đã sẵn sàng
```

Nếu parent cần “child ready with initial data”, child nên có explicit readiness contract ở sau Submission success.

## 3. WFrame tạo distributed lifecycle trong cùng browser

Một shell page có thể chứa WFrame A; A chứa TabControl; một tab chứa WFrame B; B gọi Submission. Mỗi layer có lifecycle riêng.

Source order không mô tả runtime ordering.

```text
shell ready
├─ A source loading
│  ├─ A scope ready
│  └─ tab selected
│     └─ B source loading
│        ├─ B rendered
│        └─ B data request pending
```

Khi bug chỉ xuất hiện “đôi lúc”, hãy vẽ timeline này trước khi thêm `setTimeout`.

## 4. `setTimeout` không phải lifecycle API

Anti-pattern:

```javascript
wframe1.setSrc("detail.xml");
setTimeout(function () {
    wframe1.getWindow().scwin.initDetail();
}, 500);
```

500 ms chỉ là phỏng đoán dựa trên máy/network hiện tại. Ở production hoặc cache miss, load có thể lâu hơn; trên máy nhanh, code chỉ chậm vô ích.

Đúng hướng là dùng event/callback/readiness contract mà component/build hỗ trợ.

## 5. Load, preload và render là ba chi phí khác nhau

Một page có thể tải source/script trước nhưng chưa render UI. Điều này tạo ba nhóm cost:

```text
network/resource load
JavaScript parse/eval/object creation
DOM/layout/paint/render
```

Tối ưu phải biết bottleneck nằm ở nhóm nào.

Nếu Network chậm, lazy render không sửa bandwidth. Nếu DOM quá lớn, preload source không giải quyết render cost.

## 6. TabControl `alwaysDraw`

Official SP5 guide giải thích `alwaysDraw` quyết định nội dung tab có được render tất cả ngay ban đầu hay chỉ render khi tab được chọn.

Mental model:

```text
alwaysDraw=true
→ startup cost cao hơn
→ child UI sẵn sàng sớm hơn

alwaysDraw=false
→ startup nhẹ hơn
→ first-open cost chuyển sang thời điểm user chọn tab
```

Không có giá trị “luôn đúng”. Quyết định phụ thuộc số tab, component complexity, initial data và interaction probability.

## 7. `frameMode="wframe"` và lazy page content

Với tab content dùng WFrame và `alwaysDraw=false`, page của tab chưa chọn có thể chưa được tải/render cho đến khi user mở tab.

Hệ quả architecture:

```text
Không được gọi component trong tab chưa activate như thể nó đã tồn tại.
Không nên load data cho tab user có thể không bao giờ mở.
Không nên đặt business dependency bắt buộc vào side effect của tab lazy chưa chạy.
```

Nếu main page cần dữ liệu chung, dữ liệu đó không nên được khởi tạo tình cờ trong một tab optional.

## 8. `frameMode="wframePreload"` tạo trạng thái trung gian rất quan trọng

Official guide mô tả `wframePreload` có thể tải script và tạo object trước khi tab được render. DataCollection và `scwin` có thể truy cập được, nhưng code đụng trực tiếp UI component có thể lỗi vì component chưa render hoàn chỉnh; `onpageload` của tab chưa nhất thiết chạy ở preload stage.

Đây là ví dụ hoàn hảo cho distinction:

```text
object-ready ≠ render-ready
```

Nếu function có thể được gọi ở preload stage, function đó nên tách pure/data logic khỏi UI manipulation.

## 9. Thiết kế function theo readiness requirement

Thay vì một `init()` làm mọi thứ:

```javascript
scwin.init = function () {
    dmSearch.set(...);
    inputName.setValue(...);
    grid1.redraw();
    scwin.search();
};
```

có thể tách:

```javascript
scwin.initModel = function () {
    // chỉ cần data objects
};

scwin.initView = function () {
    // cần component đã render
};

scwin.loadInitialData = function () {
    // async boundary
};
```

Tên function biểu diễn prerequisite, giảm việc gọi sai lifecycle stage.

## 10. Lazy loading thay đổi vị trí latency, không xóa latency

Nếu một tab nặng mất 800 ms để load/render, lazy loading có thể làm initial page nhanh hơn nhưng user chịu 800 ms khi mở tab lần đầu.

Vì vậy cần quyết định UX:

```text
startup latency hay first-use latency quan trọng hơn?
user có khả năng mở tab này bao nhiêu?
resource có thể preload khi browser idle không?
```

Không nên gọi mọi lazy strategy là “performance improvement” nếu chỉ di chuyển cost đến interaction critical path.

## 11. Preload là speculation

Preload có lợi khi xác suất user dùng resource cao và cost network đáng kể. Nó lãng phí khi preload nhiều tab user không dùng.

Mental model:

```text
expected benefit ≈ probability of use × saved latency - preload cost
```

Không cần tính chính xác bằng công thức; chỉ cần reasoning theo xác suất và cost thay vì bật preload mặc định.

## 12. Rendering cost tăng theo số object/DOM

Grid, repeated component, nested WFrame và complex UDC tạo object/DOM lớn. Official performance guide nhấn mạnh số cell/DOM object, đặc biệt Grid hiển thị nhiều row, ảnh hưởng memory và rendering time.

Khi screen lag, đo:

```text
row count
visible DOM count
render duration
script duration
heap retained size
```

Đừng chỉ đo HTTP response.

## 13. Grid virtual/native và visibility

Grid renderer có thể tối ưu bằng chỉ render phần visible hoặc dùng mode khác tùy build/property. Trade-off thường là:

```text
ít DOM → memory/render tốt hơn
nhưng lifecycle/scroll/render behavior phức tạp hơn
```

Code không nên dựa vào giả định mọi row luôn tồn tại thành DOM node. Hãy thao tác bằng DataList/Grid public API.

## 14. Accessibility có thể tăng render footprint

Một số accessibility mode cần nhiều semantic DOM hơn. Nếu đồng thời cấu hình `visibleRowNum="all"` với hàng nghìn row, cost có thể tăng đáng kể.

Fix đúng không phải mặc định tắt accessibility; hãy giảm dataset/render footprint và đo.

Xem [09 — Forms, Validation, Internationalization & Accessibility](09_forms_validation_i18n_accessibility.md).

## 15. Scope giúp cleanup nhưng không cứu được reference global

Official performance guidance khuyến nghị đặt function/value business screen vào object/scope thay vì top-level global để engine có thể dọn khi screen unload.

Nhưng nếu một global cache giữ reference tới child scope:

```javascript
window.lastDetailScope = $p.getWindow("detailFrame");
```

thì page unload không đảm bảo object graph được garbage collect vì vẫn còn reachable từ global root.

Garbage collection tuân theo reachability, không theo ý định developer.

## 16. Resource lifetime phải có owner

Bất kỳ resource nào sống qua thời gian đều cần owner:

```text
timer
interval
event listener
observer
cached scope
pending request
large DataList
popup/window reference
```

Hỏi hai câu:

```text
Ai tạo nó?
Ai giải phóng/hủy nó?
```

Nếu câu thứ hai không có đáp án, leak risk cao.

## 17. Timer leak trong SPA

Ví dụ:

```javascript
scwin.timer = setInterval(scwin.refresh, 30000);
```

Nếu page đóng mà interval không clear, callback vẫn có thể giữ `scwin`, DataCollection và closure reachable.

Cleanup:

```javascript
clearInterval(scwin.timer);
scwin.timer = null;
```

Tên lifecycle callback unload cụ thể phải kiểm tra theo project/build. Mental model là cleanup cùng ownership boundary.

## 18. Event listener leak

Listener gắn trực tiếp lên object sống lâu như `window`/`document` đặc biệt nguy hiểm.

```javascript
window.addEventListener("resize", scwin.onResize);
```

Page đóng nhưng `window` vẫn sống. Nếu không remove listener, function reference giữ page state.

Ưu tiên event API/component lifecycle của WebSquare khi có thể; nếu tự đăng ký browser event, tự unregister.

## 19. Pending Submission khi page đóng

Một request có thể còn đang chạy khi user đổi tab/đóng popup. Khi response về, callback có thể cố update page không còn active.

Có ba strategy tùy business:

```text
abort request nếu không còn giá trị
ignore stale result bằng token/version
apply result vào shared owner nếu owner vẫn sống
```

Không nên để callback mù quáng chạm component cũ.

## 20. Request generation/token

Một pattern chống stale response:

```javascript
scwin.searchVersion = 0;

scwin.search = function () {
    scwin.searchVersion += 1;
    var myVersion = scwin.searchVersion;
    // execute request; trong callback chỉ apply nếu myVersion còn current
};
```

Với Submission object cụ thể, implementation callback cần phù hợp API project. Mental model là **result chỉ hợp lệ với generation đã tạo nó**.

## 21. Debounce và latest-intent

Autocomplete/search-as-you-type có thể phát nhiều request. Nếu request cũ về sau request mới, UI có thể hiển thị kết quả cũ.

Hai layer giải quyết khác nhau:

```text
debounce → giảm số request
latest-intent guard → ngăn stale response ghi đè state mới
```

Chỉ debounce không loại bỏ race hoàn toàn.

## 22. Lazy script và execution ordering

WebSquare/WFrame config có các option liên quan lazy script, sync mode và scope. Official WFrame guide lưu ý một số cấu hình `mode="sync"`, `scope="true"` để bảo đảm behavior/execution order trong multi-WFrame architecture của các generation tương ứng.

Không copy config từ project khác mà không hiểu build. Một config từng là workaround ở SP cũ có thể không còn là recommendation hiện tại.

## 23. `scriptLoading.merge` và observability

Client config có option liên quan cách script WFrame/PageInherit được eval/merge. Các optimization kiểu merge có thể thay đổi stack trace/source visibility và timing.

Khi debug issue chỉ production xảy ra, hãy so sánh config dev/prod trước khi kết luận source code khác.

## 24. W-Pack và cache tạo nhiều artifact identity

Có thể tồn tại:

```text
XML source trong repository
W-Pack generated JS
artifact trong deploy package
browser/CDN cached artifact
runtime object hiện tại
```

Nếu developer sửa XML nhưng browser vẫn chạy JS cũ, nhìn source repo không đủ chứng minh runtime code.

Debug production phải xác định artifact thật được tải qua Network/source map/hash/build metadata.

## 25. Page reload không đồng nghĩa engine reload

Trong SPA, thay WFrame `src` có thể tạo page instance mới trong cùng engine shell. Global engine/common state vẫn còn.

Do đó bug “reload page con là hết” có thể khác “reload browser là hết”. Đây là clue quan trọng:

```text
Nếu browser reload mới fix → nghi global/common/cache/lifetime state.
Nếu đổi page con fix → nghi page-local state.
```

## 26. Tab caching và stale state

Một tab đã mở có thể được giữ lại thay vì destroy/recreate tùy container/config. Khi user quay lại, `onpageload` có thể không chạy lại như developer tưởng.

Nên phân biệt:

```text
first creation
activation
refresh
re-entry
close/destroy
```

Nếu business cần refresh mỗi lần active, gắn vào activation contract, không dựa vào creation callback.

## 27. Warm cache che performance problem

Development thường test lần thứ hai khi browser đã cache script và API data nhỏ. User first visit có cold cache.

Performance test nên có:

```text
cold load
warm load
slow network simulation khi phù hợp
realistic row count
repeated navigation 20–50 lần
```

Một screen chỉ nhanh ở warm cache chưa đủ production-ready.

## 28. Memory test cần lặp lifecycle

Heap snapshot một lần khó chứng minh leak. Test tốt:

```text
baseline heap
open screen
perform representative actions
close screen
force/allow GC khi tooling hỗ trợ
repeat N lần
compare retained objects
```

Nếu retained scope/listener/count tăng gần tuyến tính theo lần mở, hypothesis leak mạnh hơn.

## 29. Performance budget theo screen

Thay vì “màn hình phải nhanh”, đặt budget có thể đo:

```text
initial payload
first interactive time
search response + render
maximum practical row count
heap growth after 30 navigation cycles
```

Con số cụ thể phụ thuộc product/device/network. Giá trị của budget là tạo regression signal.

## 30. Không optimize bằng private engine API

Official performance guide khuyến nghị dùng public component API/event. API nhìn thấy trong DevTools nhưng không có trong docs có thể thay đổi giữa build.

Một private method nhanh hơn 20% hôm nay có thể tạo upgrade blocker ngày mai.

Tối ưu bền vững ưu tiên:

```text
ít data hơn
ít render hơn
đúng lifecycle
ít duplicate work
public API
```

trước micro-hack internals.

## 31. Render storm do event/binding chain

Một user action có thể:

```text
set model
→ binding update component
→ onchange handler
→ handler set model khác
→ Grid refresh
→ computed state update
```

Nếu handler viết thiếu guard, event chain có thể lặp hoặc redraw nhiều lần.

Khi profile thấy scripting/render spike, vẽ causal chain của state mutation thay vì tối ưu từng function độc lập.

## 32. Batch mutation khi API hỗ trợ

Nếu cần update nhiều row/cell, gọi update + redraw mỗi iteration có thể tốn hơn batch change rồi redraw/refresh một lần. API cụ thể phụ thuộc DataList/Grid build.

Mental model:

```text
N mutations × N render notifications
```

thường đắt hơn:

```text
N model mutations + 1 render synchronization
```

Nhưng không dùng undocumented suspend-render hack; kiểm tra public API.

## 33. Hidden UI vẫn có thể có cost

`display:none` hoặc tab chưa visible không nhất thiết nghĩa component chưa được instantiate hoặc data không load. Cost phụ thuộc lifecycle/render strategy.

Đừng tối ưu bằng cách “ẩn” 20 Grid rồi nghĩ startup nhẹ đi. Đo Network, object creation và DOM.

## 34. Case study: dashboard 12 tab

Giả sử dashboard có 12 tab, mỗi tab một WFrame và 3 Grid. Với `alwaysDraw=true`, startup có thể tải/render mọi tab và phát hàng chục request. User thường chỉ dùng 2–3 tab.

Một architecture tốt hơn có thể:

```text
render tab đầu
lazy load tab khác
preload một tab có xác suất sử dụng cao nếu network latency đáng kể
load tab-specific data khi activation lần đầu
cache data có TTL nếu business cho phép
cleanup listener/timer khi tab destroy
```

Nhưng nếu tab B cung cấp data bắt buộc cho header chung, data đó phải chuyển lên owner chung thay vì trông chờ tab B lazy chạy.

## 35. Case study: child object tồn tại nhưng method lỗi

Với preload, `scwin` child có thể tồn tại. Parent gọi `child.scwin.calculate()` thành công nếu function chỉ dùng DataMap. Sau đó refactor function thêm `grid1.redraw()` và bắt đầu lỗi trước khi tab render.

Root cause không phải “Grid API flaky”. Contract của function đã thay đổi từ data-ready sang render-ready nhưng caller không biết.

Fix tốt là tách function hoặc encode readiness requirement rõ.

## 36. Lifecycle state machine nên nghĩ thế nào

Một screen phức tạp có thể reasoning như state machine:

```text
CREATED
→ MODEL_READY
→ VIEW_READY
→ ACTIVE
→ DATA_LOADING
→ READY
→ CLOSING
→ DISPOSED
```

Không nhất thiết implement enum thật. Nhưng khi bug timing xảy ra, xác định operation hợp lệ ở state nào giúp tìm lỗi nhanh hơn.

## 37. Production debugging order

Khi “tab đôi lúc trắng”, kiểm tra theo thứ tự:

```text
content source đã request chưa?
HTTP/resource load có success không?
script exception có xảy ra không?
scope/window có tồn tại không?
component đã render chưa?
onpageload/activation có chạy không?
initial Submission có pending/fail không?
CSS/layout có làm nội dung invisible không?
```

Mỗi bước có evidence khác nhau. Không bắt đầu bằng random `redraw()`.

## 38. Connection với chapter khác

Scope/WFrame topology: [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md).

Grid rendering và large dataset: [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md).

Memory/performance evidence: [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).

Reusable UDC/dynamic component ownership: [08 — Reusable Architecture, UDC & Common Modules](08_reusable_architecture_udc_common_modules.md).

## Nguồn chính thức nên đối chiếu

WebSquare5 SP5 — TabControl tab content rendering guide: `https://docs1.inswave.com/sp5_user_guide/e0b2630fe498ead7`

WebSquare5 SP5 — Performance guide: `https://docs1.inswave.com/sp5_user_guide/5f4b3b7ceca5e65b`

WebSquare5 SP5 — WFrame/Scope guide: `https://docs1.inswave.com/sp5_user_guide/4b5b013547991bdf`

WebSquare5 SP5 — client.config.xml: `https://docs1.inswave.com/sp5_user_guide/db5edae0d31101bd`

Các behavior lifecycle/config cụ thể phải được xác minh theo exact engine build của project.