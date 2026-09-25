# Request → Pixel → Interaction Trace — một màn hình web thực sự chạy như thế nào?

Một lỗi frontend thường được mô tả bằng câu rất ngắn: “page load chậm”, “React render sai”, “CSS bị lag”, “API trả rồi nhưng màn hình chưa update”, hoặc “production khác local”. Các câu này mô tả **triệu chứng**, chưa mô tả cơ chế.

Case này lấy một màn hình giả định đủ quen thuộc để nối toàn bộ domain:

```text
/users
```

Màn hình có:

- header và navigation;
- stylesheet chính;
- JavaScript bundle;
- danh sách user tải từ `/api/users`;
- ô filter;
- nút mở modal detail;
- avatar image;
- loading state và error state.

Không quan trọng app viết bằng vanilla JavaScript, React hay WebSquare. Mục tiêu là truy được cùng một chuỗi first principles:

```text
URL
→ request
→ response bytes
→ parser
→ DOM / CSSOM
→ style
→ layout
→ paint
→ composite
→ event
→ JavaScript scheduling
→ state transition
→ network request
→ stale/cancel/error handling
→ next render
→ deployed artifact evidence
```

Case này không thay các chapter HTML, CSS hay JavaScript. Nó kiểm tra xem các chapter đó có nối thành một mental model hay chưa.

---

# 1. Bắt đầu bằng câu hỏi đúng: browser đang chạy cái gì?

Giả sử người dùng nhập:

```text
https://example.com/users
```

Sai lầm phổ biến là bắt đầu reasoning ngay từ component `UsersPage`.

Nhưng component chưa tồn tại ở thời điểm browser bắt đầu navigation.

Câu hỏi đầu tiên phải là:

```text
Browser nhận URL nào?
URL đó resolve tới origin nào?
Document request nào được gửi?
Response nào tạo ra document hiện tại?
Artifact nào browser thực sự tải?
```

Điều này đặc biệt quan trọng khi production dùng CDN, reverse proxy, service worker, cache hoặc frontend build có hashed filename.

Source file trong Git không phải thứ browser chạy trực tiếp.

Ta cần tách:

```text
Source code
→ build graph
→ generated artifact
→ deployed artifact
→ cached artifact
→ resource browser actually executes
```

Nếu không tách được năm lớp này, câu “code đã deploy rồi” chưa phải evidence.

---

# 2. Navigation không giống `fetch`

Document navigation tới `/users` và JavaScript gọi:

```js
fetch('/api/users')
```

đều dùng network, nhưng semantic khác nhau.

Navigation có thể tạo hoặc thay document. Nó kích hoạt document loading, parsing và lifecycle liên quan page.

`fetch()` chỉ là một request do script khởi tạo trong document hiện tại. Nó không tự tạo DOM mới, không tự render dữ liệu và không tự thay state của framework.

Mental model:

```text
Navigation response
→ bytes that can become a Document

API response
→ bytes/data delivered to JavaScript
→ application decides what state changes
→ rendering may happen afterward
```

Đây là lý do “API đã trả 200” không đồng nghĩa “UI phải hiện ngay”. Giữa response và pixel còn nhiều bước.

---

# 3. Document response: status code chưa đủ

Giả sử document request trả `200 OK`.

Ta vẫn phải hỏi:

```text
Content-Type là gì?
encoding là gì?
cache policy là gì?
CSP/security headers là gì?
HTML body thực tế là version nào?
```

Một status `200` chỉ nói request thành công theo HTTP contract ở một mức nào đó. Nó không chứng minh:

- response là artifact đúng version;
- HTML tham chiếu bundle đúng;
- CDN không trả file cũ;
- script không bị CSP chặn;
- stylesheet không 404;
- hydration/runtime không fail sau đó.

Debug production vì vậy phải trace **resource graph**, không dừng ở document request.

---

# 4. Browser nhận bytes, không nhận DOM

Server gửi HTML text/bytes. DOM chưa tồn tại sẵn trong response.

Ví dụ response:

```html
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="/assets/app.abc123.css">
    <script type="module" src="/assets/app.def456.js"></script>
  </head>
  <body>
    <main id="app"></main>
  </body>
</html>
```

Browser phải parse source này thành tree.

Mental model:

```text
HTML source
≠ DOM tree
```

Parser có rules riêng, có thể repair markup, insert implied nodes hoặc xử lý các content mode khác nhau.

Vì vậy khi DOM nhìn khác source, đừng lập tức kết luận framework sửa HTML. Có thể chính HTML parser đã tạo tree khác source text.

---

# 5. Parser gặp resource: loading và parsing bắt đầu đan xen

Trong khi parse HTML, browser phát hiện resource như stylesheet, script, image, font.

Document loading không phải:

```text
download full HTML
→ parse all HTML
→ download CSS
→ download JS
→ render
```

Nhiều việc overlap.

Một mental timeline đơn giản hơn:

```text
HTML bytes arrive
→ parser advances
→ discover CSS / JS / image
→ initiate dependent requests
→ continue or pause according to resource semantics
```

Chi tiết blocking phụ thuộc resource type và cách khai báo, nên không nên học một rule đơn giản kiểu “mọi script block parser”.

Điểm cần giữ là **resource discovery time ảnh hưởng critical path**.

Nếu một stylesheet quan trọng chỉ được phát hiện sau khi JavaScript chạy rồi inject link, browser không thể tải nó trước khi có discovery đó.

---

# 6. DOM và CSSOM là hai cấu trúc khác nhau

HTML tạo DOM.

CSS được parse thành cấu trúc rule/style information thường được reasoning dưới mental model CSSOM.

Ta có thể hình dung:

```text
DOM
+
CSS rules / cascade inputs
→ computed style
```

Nhưng đừng biến nó thành công thức quá cơ học. Style resolution còn phụ thuộc:

- origin;
- cascade layer;
- importance;
- specificity;
- scope/proximity;
- inheritance;
- source order;
- environment như viewport/media/container state.

Do đó lỗi “CSS class có trong DOM nhưng không có style mong muốn” là câu hỏi cascade trước khi là câu hỏi framework.

---

# 7. Style không phải layout

Sau khi browser biết style liên quan, nó còn phải xác định geometry.

Ví dụ:

```css
.user-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

CSS declaration không chứa trực tiếp pixel position cuối của từng card.

Layout phải giải quyết constraint từ:

- available size;
- intrinsic size;
- formatting context;
- font metrics;
- content;
- replaced elements;
- min/max constraints;
- scrollbars;
- viewport/container size.

Vì vậy:

```text
computed style
≠ final geometry
```

Một image load muộn có thể thay intrinsic size và kéo theo layout mới nếu dimension không được reserve.

Một web font load cũng có thể thay text metrics và geometry.

---

# 8. Layout không phải paint

Biết một box ở đâu chưa có nghĩa pixel đã xuất hiện trên màn hình.

Layout trả lời gần với:

```text
box nào ở đâu, kích thước bao nhiêu?
```

Paint trả lời gần với:

```text
box/text/border/background/shadow nào cần được vẽ theo thứ tự nào?
```

Compositing lại liên quan cách các painted results/layers được kết hợp để tạo frame cuối.

Đừng học pipeline như ba API public mà browser bắt buộc implement y hệt nhau. Đây là mental model để reasoning performance.

Điều quan trọng:

```text
style work
layout work
paint work
composite work
```

không có cùng cost và không bị invalidate bởi cùng loại thay đổi.

---

# 9. “Transform chạy trên GPU” không phải kết luận performance

Một câu rất hay gặp:

> Dùng `transform` nhanh vì GPU.

Đây là shortcut nguy hiểm.

Ngay cả khi một animation có thể tránh layout/paint trong một implementation cụ thể, tổng performance còn phụ thuộc:

- layer creation/promotion;
- texture memory;
- rasterization;
- upload/composite cost;
- size của layer;
- số lượng layer;
- main-thread scripting;
- concurrent work khác;
- device/browser/runtime state.

Do đó production reasoning phải là:

```text
Hypothesis
→ record trace
→ identify actual work
→ change one variable
→ record again
```

chứ không phải:

```text
CSS property name
→ assume cost
```

Lab kế tiếp sẽ biến nguyên tắc này thành workflow đo.

---

# 10. JavaScript bundle tải xong chưa có nghĩa app sẵn sàng

Giả sử `/assets/app.def456.js` download xong.

Browser vẫn có thể cần:

- parse JavaScript;
- compile/prepare execution;
- resolve/import module graph;
- execute initialization;
- register listeners;
- create application state;
- mount/hydrate framework tree;
- schedule additional work.

Vì vậy network waterfall chỉ là một lớp của startup.

Nếu bundle download nhanh nhưng main thread bận execute vài trăm millisecond, user vẫn có thể cảm thấy app chưa interactive.

Ta cần phân biệt:

```text
Resource download time
vs
Main-thread execution time
vs
Rendering work
vs
Interaction latency
```

---

# 11. Initial application state có owner

Giả sử runtime tạo state:

```js
{
  users: [],
  loading: true,
  error: null,
  filter: '',
  selectedUserId: null
}
```

Không nên chỉ hỏi state “nằm trong React hay store nào”.

Hỏi sâu hơn:

```text
Ai sở hữu state này?
Lifetime bằng document, page, component hay request?
State nào canonical?
State nào derived?
State nào chỉ là UI affordance?
```

Ví dụ filtered list nên thường là derived từ:

```text
users + filter
```

Nếu app lưu riêng cả `users`, `filter`, `filteredUsers`, ta đã tạo khả năng hai nguồn dữ liệu lệch nhau.

Rule tổng quát:

```text
Derived state không nên trở thành source of truth mới nếu có thể tính đáng tin từ canonical state.
```

---

# 12. API request bắt đầu: cần gắn identity cho operation

App gọi `/api/users`.

Naive model:

```text
request
→ response
→ setUsers(response)
```

Production model phải nghĩ thêm:

```text
operation identity
owner
lifetime
cancellation
stale-result policy
error policy
retry policy
```

Ví dụ user đổi filter không nhất thiết cần request mới nếu filter client-side. Nhưng nếu search server-side:

```text
query=a
→ request A
query=ab
→ request B
```

Nếu B trả trước A:

```text
B response
→ UI shows "ab"
A response arrives later
→ naive code overwrites with stale "a"
```

Đây không phải network bug. Đây là **ordering + ownership bug**.

Invariant cần là:

```text
Only result belonging to current intent may update current state.
```

Implementation có thể dùng abort/cancellation, request ID, sequence number hoặc library abstraction. Nhưng invariant mới là kiến thức canonical.

---

# 13. Promise completion không đồng nghĩa pixel cập nhật ngay lập tức

Giả sử response về và Promise continuation chạy:

```js
state.users = data
state.loading = false
```

Người mới dễ nghĩ:

```text
set state
→ pixel đổi tức thì
```

Thực tế state mutation/update có thể làm framework schedule rendering work. Browser còn phải đi qua phần cần thiết của style/layout/paint/composite trước khi frame mới xuất hiện.

Tùy framework và scheduling model, nhiều state update có thể được batch hoặc deferred.

Mental model nên là:

```text
Data becomes available
→ application state transition
→ rendering work becomes eligible/scheduled
→ DOM/style consequences
→ browser rendering work
→ frame presented
```

Không nên debug timing bằng cách chỉ thêm `setTimeout(..., 0)` cho tới khi “hết lỗi”.

---

# 14. Event loop: phải trace ordering, không học slogan

Giả sử user gõ vào filter input.

Có thể có:

```text
input event
→ handler
→ state update
→ Promise/microtask continuation
→ framework scheduling
→ render opportunity
→ paint
```

Nhưng timeline thực tế còn phụ thuộc work đang chờ, framework, browser và code.

Điều cần học là cách hỏi:

```text
Callback nào đang chạy?
Nó được enqueue từ đâu?
Có microtask nào tiếp tục trước khi browser có cơ hội render?
Có long task nào đang giữ main thread không?
```

Một microtask chain quá dài có thể trì hoãn rendering dù mỗi Promise callback riêng lẻ nhìn nhỏ.

Do đó `async` không đồng nghĩa “không block UI”. JavaScript continuation vẫn có thể chạy trên main thread và tiêu tốn budget.

---

# 15. Filter 10.000 rows: bottleneck nằm ở đâu?

Giả sử filter list gồm 10.000 user.

Triệu chứng: gõ một ký tự bị lag.

Có ít nhất bốn họ nguyên nhân khác nhau:

```text
A. computation
filter/sort quá nặng

B. framework reconciliation/render
quá nhiều component work

C. DOM mutation + style/layout
quá nhiều node hoặc geometry invalidation

D. paint/composite
visual effect/layer/raster cost lớn
```

Không thể nhìn lag rồi kết luận ngay “React render quá nhiều”.

Quy trình đúng:

```text
record interaction
→ find long work
→ split scripting vs rendering
→ inspect call stack / invalidation
→ count affected nodes/work
→ form hypothesis
```

Nếu computation chiếm 80 ms nhưng layout chỉ 2 ms, CSS không phải target đầu tiên.

Nếu JavaScript chỉ 4 ms nhưng layout 70 ms trên hàng nghìn node, memoization component không giải quyết core problem.

---

# 16. DOM size là multiplier chứ không phải tội lỗi tuyệt đối

“DOM lớn chậm” là một heuristic, không phải định luật đủ để debug.

DOM lớn có thể tăng cost cho:

- selector/style calculation;
- layout;
- accessibility tree;
- memory;
- event/listener architecture;
- mutation/update scope.

Nhưng cost thực tế còn phụ thuộc structure và operation.

Virtualization có giá trị khi UI chỉ cần render subset visible, nhưng virtualization cũng tạo complexity:

- scroll measurement;
- focus/accessibility;
- dynamic row height;
- selection;
- keyboard navigation;
- state preservation.

Optimization phải gắn với bottleneck thật, không phải checklist trend.

---

# 17. Modal: visual layer và interaction layer phải thống nhất

User bấm một card và mở detail modal.

Nếu chỉ nhìn pixel, modal có thể “đúng”. Nhưng public behavior còn gồm:

- focus chuyển vào modal hợp lý;
- background không nhận interaction ngoài ý muốn;
- keyboard navigation;
- accessible name/role;
- Escape/close behavior;
- focus restoration sau close;
- scroll behavior;
- portal/layer ownership;
- async detail request cancellation nếu modal đóng sớm.

Đây là ví dụ vì sao accessibility không phải phần trang trí cuối pipeline.

Semantics và focus là correctness của interaction model.

---

# 18. Portal không phá DOM rules

React portal hoặc framework popup abstraction có thể render node ra vị trí DOM khác logical component parent.

Điều này tạo hai tree cần phân biệt:

```text
Logical application/component tree
vs
Physical DOM tree
```

Event, CSS inheritance, stacking context, focus và accessibility có thể phụ thuộc tree/boundary khác nhau.

Khi debug modal, phải biết mình đang reasoning tree nào.

Nói “modal là child của UsersPage” có thể đúng trong component model nhưng sai nếu dùng để suy luận CSS containing block hoặc DOM ancestry.

---

# 19. Stacking context: `z-index: 999999` không phải universal fix

Modal nằm sau header.

Naive fix:

```css
z-index: 999999;
```

Nhưng `z-index` được interpret trong stacking context. Nếu ancestor tạo stacking context khác, tăng số trong context con không nhất thiết vượt sibling context bên ngoài.

Debug phải hỏi:

```text
Node nào tạo stacking context?
Modal physical DOM nằm ở đâu?
Containing/stacking ancestry là gì?
```

Đây là ví dụ điển hình của việc framework tree không thay CSS rendering rules.

---

# 20. Image loading và layout stability

Avatar xuất hiện sau.

Nếu image không reserve space, load hoàn tất có thể đổi layout.

Nếu user chuẩn bị click nút nhưng content dịch chuyển, đây không chỉ là “visual annoyance”; nó thay interaction target position.

Mental model:

```text
resource timing
→ intrinsic size becomes known
→ geometry may invalidate
→ new layout
→ repaint/composite as needed
```

Giải pháp tốt thường bắt đầu từ contract kích thước/aspect ratio, không phải JavaScript đo rồi sửa sau mỗi load nếu không cần.

---

# 21. Font là resource có thể thay geometry

Font load không chỉ đổi “style chữ”.

Font metrics có thể đổi:

- line break;
- line height;
- element width/height;
- downstream layout.

Vì vậy font strategy là giao điểm giữa network, typography, layout và visual stability.

Nếu production font CDN chậm còn local dùng installed font, layout bug có thể chỉ xuất hiện production dù CSS source giống nhau.

---

# 22. API error: error state không phải `console.error`

Giả sử `/api/users` trả 500.

Application contract cần quyết định:

```text
loading kết thúc khi nào?
error nào public cho user?
retry có safe không?
partial data có giữ không?
telemetry ghi gì?
request ID/correlation nào giúp backend trace?
```

`console.error(error)` không phải error handling hoàn chỉnh.

Frontend cũng không nên tự suy rằng retry mọi request là tốt. Một GET idempotent có đặc tính khác mutation có side effect.

Boundary với Backend phải giữ semantic của operation.

---

# 23. `401` và `403`: UI không phải authorization engine

Nếu API trả auth error, frontend có thể:

- redirect login;
- refresh session theo contract;
- hide/disable capability;
- hiển thị message.

Nhưng frontend không quyết định security truth cuối cùng.

Rule:

```text
UI capability hint
≠ server authorization
```

Button bị ẩn không bảo vệ API.

Client validation giúp UX và giảm request sai, nhưng không thay server-side authorization/validation.

---

# 24. CORS bug không phải “backend API chết”

Nếu browser chặn cross-origin access, có thể server thực tế vẫn trả response ở network level.

CORS là browser security policy quanh việc script có được đọc/use response cross-origin theo contract hay không.

Debug cần phân biệt:

```text
DNS/connect failure
HTTP failure
CORS policy failure
application parsing failure
state/render failure
```

Gộp tất cả thành “API lỗi” làm mất boundary.

---

# 25. Cache: version cũ có thể tồn tại đúng theo policy

Production bug:

> Tôi đã deploy JS mới nhưng user vẫn chạy code cũ.

Đừng bắt đầu bằng “clear cache thử”. Trước hết cần biết caching model:

```text
HTML cache policy
hashed asset cache policy
CDN cache
browser HTTP cache
service worker/cache storage nếu có
runtime config cache
```

Một pattern phổ biến là HTML có policy cho phép cập nhật nhanh, còn hashed immutable assets cache dài. Khi HTML mới trỏ hash mới, graph chuyển version.

Nếu HTML cũ bị cache sai, nó vẫn có thể tiếp tục trỏ bundle cũ hoàn toàn hợp logic.

Do đó artifact identity phải quan sát được.

---

# 26. Service worker tạo thêm một network owner

Nếu app có service worker, request path có thể không đơn giản là:

```text
browser → network
```

Mà có thể là:

```text
page
→ service worker fetch handling
→ cache and/or network
→ response
```

Production debugging phải hỏi service worker version nào đang control page.

Nếu không, DevTools Network nhìn thấy một response nhưng ta có thể hiểu sai nguồn thực tế của nó.

---

# 27. Source map: source dễ đọc không phải code browser execute

Production stack trace có thể map về TypeScript/JSX/source thông qua source map.

Điều đó hữu ích, nhưng mental model phải giữ:

```text
Mapped source location
≠ bytes executed directly by runtime
```

Build transform có thể thay module, syntax, chunking, minification và code path.

Khi bug chỉ xảy ra production, cần giữ cả hai view:

- source view để reasoning logic;
- generated artifact view để reasoning runtime/build issue.

---

# 28. Build-time config và runtime config khác nhau

Ví dụ:

```text
API_BASE_URL
FEATURE_FLAG
BUILD_ID
```

Một giá trị có thể được bake vào bundle lúc build hoặc được tải runtime.

Hai mô hình có operational consequence khác nhau.

Nếu build-time:

```text
config change
→ rebuild artifact
```

Nếu runtime:

```text
same artifact
+ different runtime config
```

Khi production sai endpoint, cần biết config ownership trước khi sửa code.

---

# 29. Một trace đúng phải có nhiều clock/timeline liên quan

Đừng chỉ giữ một screenshot waterfall.

Case này nên được trace trên ít nhất các lớp:

```text
Navigation/network timeline
Main-thread task timeline
Rendering timeline
Application state timeline
User-intent timeline
Deployment/artifact timeline
```

Ví dụ:

```text
T0 user navigates
T1 HTML response starts
T2 CSS discovered
T3 JS discovered
T4 first DOM content exists
T5 JS initialization starts
T6 API request starts
T7 initial frame shown
T8 API response arrives
T9 state update scheduled
T10 layout/paint
T11 user types filter
T12 filter computation
T13 next frame
```

Các timestamp cụ thể tùy run. Giá trị của diagram là buộc ta nói rõ **causal ordering**.

---

# 30. Worked failure A — API nhanh nhưng màn hình chậm

Observation:

```text
/api/users response: 80 ms
UI list visible: 900 ms later
```

Naive conclusion:

> React chậm.

Audit flow:

1. Xác định response complete time.
2. Xem Promise continuation chạy lúc nào.
3. Tìm long task giữa response và next paint.
4. Tách scripting/style/layout/paint.
5. Kiểm tra số node được tạo.
6. Kiểm tra synchronous transform/sort/avatar processing.
7. Kiểm tra framework profiler nếu framework work là phần lớn cost.

Có thể cuối cùng nguyên nhân là:

```text
response
→ synchronous sort/group 250 ms
→ create 10k rows
→ style/layout 300 ms
→ paint 120 ms
```

Trong case này “API nhanh” đúng, nhưng chưa nói bottleneck nằm ở framework reconciliation hay browser rendering.

---

# 31. Worked failure B — local đúng, production sai CSS

Observation:

```text
local modal correct
production modal under header
```

Hypotheses hợp lý hơn random z-index:

```text
CSS build order khác?
chunk bị thiếu?
minifier/build transform thay output?
production-only class/content detection bỏ rule?
runtime portal target khác?
feature flag tạo ancestor stacking context khác?
old cached stylesheet?
```

Evidence cần:

- computed style;
- matched rule/source;
- actual loaded stylesheet hash;
- DOM ancestry;
- stacking context;
- build ID.

Chỉ so source SCSS chưa đủ.

---

# 32. Worked failure C — kết quả search quay ngược

Timeline:

```text
T0 query="a"  → request A
T1 query="ab" → request B
T2 B returns   → state="ab results"
T3 A returns   → state="a results"
```

Network hoạt động đúng. Backend có thể cũng đúng.

Bug là application không encode current-intent invariant.

Fix không phải “delay search thêm 500 ms” như một luật universal.

Debounce có thể giảm request nhưng không tự giải quyết mọi stale ordering nếu requests vẫn overlap.

Need:

```text
operation identity + cancellation/stale-result guard
```

---

# 33. Worked failure D — click lag nhưng animation vẫn mượt

Có thể compositor animation tiếp tục chạy tương đối mượt trong khi main thread bị long task, nên user thấy một phần UI chuyển động nhưng click handler phản hồi chậm.

Bài học:

```text
visual motion quality
≠ main-thread responsiveness
```

Một metric/symptom không đại diện toàn bộ responsiveness.

Cần record interaction và main-thread work.

---

# 34. Worked failure E — scroll jank chỉ khi mở DevTools hoặc máy yếu

Performance phụ thuộc environment.

Một profile phải ghi ít nhất:

```text
browser/version
hardware class
viewport
network condition nếu relevant
data size
feature flags
build ID
profile method
```

Không cần giả lập chính xác mọi user, nhưng không được báo kết quả benchmark mà thiếu execution context.

---

# 35. Framework-specific reasoning chỉ bắt đầu sau platform evidence

Nếu app dùng React, ta có thể tiếp tục hỏi:

```text
component nào render?
state/props identity nào thay?
memo boundary có hợp lý không?
effect có duplicate work không?
hydration/concurrency có liên quan không?
```

Nếu dùng WebSquare:

```text
scope/page lifecycle nào?
DataCollection/Submission state nào?
Grid rendering/formatter có amplify work không?
WFrame ownership/lifetime nào?
```

Nhưng trước đó vẫn cần platform trace:

```text
network
DOM
style/layout/paint
main-thread tasks
```

Framework profiler không thay browser profiler; browser profiler cũng không giải thích hết framework logical ownership. Hai lớp bổ sung nhau.

---

# 36. Từ symptom tới hypothesis

Khi gặp lỗi, đừng nhảy từ symptom thẳng sang fix.

Dùng chain:

```text
Symptom
→ observation
→ boundary
→ hypothesis
→ expected evidence
→ measurement
→ conclusion
→ smallest corrective change
→ re-measure
```

Ví dụ:

```text
Symptom: typing lag
Observation: 120 ms long task per keystroke
Boundary: JavaScript + rendering
Hypothesis: full list sort + rerender 10k rows
Expected evidence: sort stack + node/layout growth
Measurement: trace/profile
Change: pre-index + virtualization
Re-measure: interaction + memory + accessibility regression
```

Điểm quan trọng là fix phải nối với evidence.

---

# 37. Failure matrix cho màn hình `/users`

Không cần ghi nhớ bảng. Hãy dùng nó như pattern reasoning:

| Symptom | Có thể nằm ở | Evidence đầu tiên |
|---|---|---|
| Blank page | document/script/runtime/security | document + console + loaded artifact |
| Unstyled page | CSS discovery/cache/build/cascade | stylesheet request + matched rules |
| Layout shift | image/font/dynamic content geometry | timeline + element geometry |
| API data không hiện | async/state/render | network + state transition + task trace |
| Typing lag | compute/framework/DOM/layout/paint | interaction trace |
| Modal sau header | stacking context/portal/output CSS | DOM + computed style + stacking ancestry |
| User cũ hiện sau search mới | stale async ordering | request + intent timeline |
| Production khác local | build/config/cache/version | build ID + resource hashes + config |

Một symptom có nhiều candidate. Evidence dùng để loại dần, không phải intuition chọn ngay một nguyên nhân.

---

# 38. Artifact identity phải là một phần observability

Một production frontend tốt nên có cách xác định version đang chạy.

Ví dụ conceptual:

```text
commit SHA
build ID
deploy ID
bundle hash
runtime config version
```

Không nhất thiết expose mọi thứ công khai cho end user, nhưng engineering telemetry/debug info phải cho phép trả lời:

> User gặp lỗi này đang chạy artifact nào?

Nếu không, rollback và incident correlation trở nên mơ hồ.

---

# 39. Performance budget phải map tới user work

Không nên dùng một budget chỉ vì tool có metric đó.

Hãy map:

```text
startup
→ document/resource critical path
→ initialization
→ first useful content

interaction
→ input event
→ JavaScript work
→ rendering work
→ next presented frame

list update
→ data size
→ computation
→ DOM/framework work
→ layout/paint
```

Metric là proxy cho user experience và system work; không phải mục tiêu độc lập.

---

# 40. Một end-to-end trace hoàn chỉnh nên trả lời được gì?

Sau case này, người đọc phải có thể chọn một màn hình thật và trả lời:

```text
1. Document nào tạo page?
2. Resource graph nào tạo CSS/JS/font/image?
3. Artifact/version nào đang chạy?
4. Parser tạo DOM nào?
5. CSS nào thắng cascade và tại sao?
6. Geometry phụ thuộc constraint nào?
7. Thay đổi nào invalidate style/layout/paint?
8. Main thread đang làm work gì khi user chờ?
9. Event/Promise/request ordering là gì?
10. State canonical nằm ở đâu?
11. Async operation nào có identity/lifetime nào?
12. Accessibility contract nào phải giữ?
13. Security/trust boundary ở đâu?
14. Backend/DevOps domain sở hữu phần nào?
15. Evidence nào xác nhận hypothesis?
```

Nếu trả lời được 15 câu này, framework trở thành một lớp có thể reasoning chứ không còn là magic.

---

# 41. Bài thực hành bắt buộc

Chọn một page trong project thật.

Không bắt đầu bằng sửa code. Trước tiên tạo file trace với structure:

```text
A. User intent
B. URL/document request
C. dependent resource graph
D. DOM/CSS owner map
E. main-thread timeline
F. application state transitions
G. async operations and stale-result rules
H. rendering evidence
I. accessibility interaction contract
J. build/deploy artifact identity
K. top three failure hypotheses
L. measurement needed to distinguish them
```

Sau đó cố ý tạo một regression, ví dụ:

- bỏ image dimension;
- render gấp 10 lần rows;
- thêm synchronous sort nặng;
- tạo stale request race;
- thêm ancestor stacking context;
- deploy HTML cache policy không phù hợp trong environment test.

Quan sát trace thay đổi ở đâu.

Đây là cách biến mental model thành debugging skill.

---

# 42. Exit gate

Case hoàn thành khi người học không còn nói các câu quá rộng như:

```text
"Frontend chậm"
"React lỗi"
"CSS lag"
"API chưa load"
```

mà có thể chuyển chúng thành statement có boundary và evidence:

```text
"Input event bắt đầu lúc T0; handler tạo một 96 ms main-thread task,
trong đó 61 ms là synchronous filtering và 24 ms là style/layout trên
8.400 row nodes. Network không nằm trên interaction critical path."
```

hoặc:

```text
"Production document đang tải app.OLDHASH.js từ cached HTML version cũ;
source branch đã mới nhưng browser không chạy artifact mới."
```

Depth của Frontend nằm ở khả năng chuyển symptom thành causal trace như vậy.

## Cross-link

Đọc song song:

- [`../README.md`](../README.md) để giữ domain map;
- [`../COVERAGE_AUDIT.md`](../COVERAGE_AUDIT.md) để biết owner và remaining gaps;
- JavaScript Senior/Master cho event loop, networking, performance và deployment boundary;
- CSS Master cho rendering/cascade/layout evidence;
- HTML Master cho parser, semantics, resource loading và accessibility;
- React/WebSquare track khi cần map platform trace sang framework ownership.

Tiếp theo làm [Rendering Performance Measurement Lab](./01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md) để biến phần style/layout/paint/composite thành quy trình đo lặp lại được.
