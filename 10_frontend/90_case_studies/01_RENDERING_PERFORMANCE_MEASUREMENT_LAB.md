# Rendering Performance Measurement Lab — đo style, layout, paint và composite thay vì đoán

Frontend performance rất dễ bị biến thành folklore:

```text
transform = nhanh
box-shadow = chậm
React render = xấu
DOM lớn = luôn chậm
GPU = tốt
will-change = tối ưu
```

Một số câu có thể đúng trong một context cụ thể, nhưng không câu nào đủ để thay measurement.

Lab này tập trung vào một nguyên tắc:

```text
Không tối ưu rendering bằng tên property.
Tối ưu bằng trace của work thực tế.
```

Mục tiêu không phải học thuộc internals của một browser engine cụ thể. Mục tiêu là xây workflow có thể lặp lại:

```text
Symptom
→ reproducible scenario
→ baseline
→ trace
→ classify work
→ identify invalidation / owner
→ hypothesis
→ one change
→ re-measure
→ regression guard
```

---

# 1. Performance là câu hỏi về critical path

Một page có thể làm rất nhiều work nhưng user chỉ bị block bởi phần nằm trên critical path của intent hiện tại.

Ví dụ user click “Open detail”. Ta quan tâm:

```text
input
→ event dispatch
→ application handler
→ state transition
→ DOM/style consequences
→ layout/paint/composite if needed
→ next useful frame
```

Nếu đồng thời background analytics chạy 20 ms sau frame, nó vẫn là cost đáng quan tâm nhưng không nhất thiết là nguyên nhân chính của click latency đó.

Do đó trước khi profile phải xác định:

```text
User action nào?
Expected visible result nào?
Start và end của interaction ở đâu?
```

Không có scope này, trace dễ biến thành một ảnh đầy màu nhưng không có câu hỏi.

---

# 2. Chọn scenario có thể tái tạo

Không profile một page bằng cách “click thử vài thứ”.

Định nghĩa scenario:

```text
Dataset: 5.000 rows
Viewport: desktop 1440×900
State: page đã load, cache warm
Action: gõ một ký tự vào filter
Expected result: list cập nhật và input vẫn responsive
Runs: ít nhất vài lần cùng điều kiện
```

Hoặc:

```text
State: modal đóng
Action: click Open Detail
Expected result: overlay + dialog visible, focus moved inside
```

Scenario phải đủ cụ thể để before/after có thể so.

---

# 3. Ghi environment trước khi ghi metric

Performance result không có context thì rất khó tái tạo.

Ghi:

```text
browser + version
OS
device/hardware class
viewport/device scale nếu relevant
build ID / commit
feature flags
data volume
network/cache condition
CPU/network throttling nếu có
```

Không cần mọi benchmark phải lab-grade. Nhưng cần đủ context để biết hai run có đang so cùng một hệ thống hay không.

---

# 4. Warm cache và cold cache là hai câu hỏi khác nhau

Cold load có thể bị chi phối bởi network/resource startup.

Warm interaction có thể bị chi phối bởi JavaScript/rendering.

Đừng gộp:

```text
page load performance
interaction performance
```

thành một con số “frontend speed”.

Nếu mục tiêu là rendering khi filter rows, warm page trước rồi đo interaction. Nếu mục tiêu là first navigation, cold/warm cache phải được ghi rõ.

---

# 5. Baseline trước optimization

Trước khi sửa code, ghi baseline.

Ví dụ:

```text
Interaction duration: 140 ms
Scripting: 72 ms
Style: 18 ms
Layout: 31 ms
Paint/composite-related work: 12 ms
Other: 7 ms
Affected DOM nodes: ~5.000
```

Các con số chỉ là ví dụ. Tool/browser có thể nhóm work khác nhau.

Điểm quan trọng là decomposition.

Nếu không có baseline, sau optimization ta chỉ biết “cảm giác nhanh hơn”.

---

# 6. Scripting, style, layout, paint và composite là categories, không phải blame labels

Khi thấy layout lớn, đừng kết luận CSS team sai.

Layout có thể bị kích hoạt bởi JavaScript mutation.

Khi thấy scripting lớn, đừng kết luận framework sai.

Scripting có thể là app business transform hoặc third-party code.

Reasoning phải nối:

```text
Who caused invalidation?
What work became necessary?
How large was affected scope?
```

Owner của **cause** và owner của **work category** có thể khác nhau.

---

# 7. Style invalidation

Một DOM/class/state change có thể làm browser phải tính lại style cho một scope nào đó.

Ví dụ:

```js
document.body.classList.add('dark')
```

Nếu theme selector ảnh hưởng phần lớn tree, style work có thể rộng.

Nhưng không nên nói:

> đổi class body luôn chậm.

Cost phụ thuộc:

- selector graph;
- số affected nodes;
- implementation;
- current state;
- follow-up layout/paint.

Trace mới trả lời scenario cụ thể.

---

# 8. Layout invalidation

Layout work xảy ra khi geometry cần được xác định lại.

Các thay đổi liên quan size/flow có thể kéo theo layout, nhưng scope không phải lúc nào cũng toàn document.

Câu hỏi đúng:

```text
Geometry nào đổi?
Ancestor/descendant/sibling nào phụ thuộc geometry đó?
Formatting context nào bị ảnh hưởng?
```

Một component được isolate tốt có thể giới hạn propagation tốt hơn một tree có dependency rộng.

---

# 9. Forced synchronous layout là ordering problem

Pattern kinh điển:

```js
el.style.width = '200px';
const width = el.offsetWidth;
```

Code vừa mutation có khả năng invalidate layout, sau đó ngay lập tức đọc geometry cần giá trị cập nhật.

Browser có thể buộc phải resolve pending layout trước khi trả kết quả read.

Đây không đơn giản là:

```text
offsetWidth = slow
```

Vấn đề là **read/write ordering**.

Một read riêng lẻ khi layout already clean có thể rẻ hơn nhiều.

Mental model:

```text
write that invalidates geometry
→ geometry read before normal rendering opportunity
→ synchronous layout may be forced
```

---

# 10. Layout thrashing

Xấu hơn là xen kẽ read/write trong loop:

```js
for (const item of items) {
  item.style.width = computeWidth(item);
  total += item.offsetWidth;
}
```

Potential pattern:

```text
write
→ force layout
→ write
→ force layout
→ ...
```

Một strategy tốt hơn có thể batch reads rồi writes nếu semantic cho phép.

Nhưng đừng refactor chỉ vì thấy pattern. Profile để xác nhận layout thực sự đáng kể trong scenario.

---

# 11. Paint cost phụ thuộc vùng và visual complexity

Paint không phải binary “property A paint, property B không paint”.

Cost còn phụ thuộc:

- area bị invalidate;
- number of elements;
- clipping;
- effects;
- text;
- images;
- scrolling;
- raster scale.

Một effect đắt trên full-screen layer khác hoàn toàn cùng effect trên icon 20×20.

Do đó khi audit paint, hỏi:

```text
What region repainted?
Why?
How often?
How large/complex?
```

---

# 12. Composite không miễn phí

Nếu browser có thể composite một layer mà không repaint content, điều đó có thể hữu ích.

Nhưng layers có cost:

- memory;
- management;
- raster surfaces;
- transfer/upload depending on architecture;
- composition complexity.

Nếu promote hàng nghìn element “để GPU chạy”, ta có thể đổi một bottleneck sang bottleneck khác.

Vì vậy:

```text
more layers
≠ automatically faster
```

---

# 13. `will-change` là hint, không phải turbo button

`will-change` có thể cho browser biết một property có khả năng thay đổi, giúp chuẩn bị optimization trong một số case.

Nhưng giữ nó rộng/lâu trên nhiều node có thể tăng resource cost.

Workflow đúng:

```text
measured bottleneck
→ specific animation/update
→ test whether will-change improves trace
→ remove if no evidence / avoid global blanket use
```

Không thêm `will-change: transform` vào mọi component như default reset.

---

# 14. Animation lab A — `top/left` và `transform`

Tạo một box di chuyển 300 px trong 500 ms.

Version A thay `left`.

Version B dùng `transform: translateX(...)`.

Không bắt đầu bằng kết luận B thắng.

Record:

```text
main-thread work
style/layout
paint
composite/layer behavior
frame consistency
memory/layers if observable
```

Trong nhiều environment, transform animation có thể tránh layout tốt hơn. Nhưng lab chỉ đạt khi người học có thể **show evidence**, không chỉ lặp câu này.

Sau đó tăng:

```text
1 box
→ 100 boxes
→ 2.000 boxes
```

Quan sát scaling. Một optimization ở scale 1 có thể có trade-off khác ở scale lớn.

---

# 15. Animation lab B — visual effect lớn

Tạo card lớn có shadow/filter và animate.

Thử:

- animate geometry;
- animate opacity;
- animate transform;
- thay size vùng effect.

Mục tiêu không phải lập bảng universal property cost.

Mục tiêu là thấy:

```text
same property family
× different area/count/device
→ different total cost
```

Performance là property của workload, không chỉ syntax.

---

# 16. List lab — 100, 1.000, 10.000 rows

Render cùng component với dataset tăng dần.

Ghi:

```text
DOM node count
initial render time
filter interaction
style/layout time
memory trend
scroll behavior
```

Sau đó test một số intervention:

```text
reduce rendered columns
avoid expensive synchronous transform
virtualize visible rows
memoize only proven repeated computation
change DOM structure
```

Không apply tất cả cùng lúc. Mỗi run chỉ nên thay đủ ít để attribution còn rõ.

---

# 17. Framework render và browser rendering phải tách

Trong React, “render” thường được dùng cho framework render/reconciliation.

Browser rendering lại có style/layout/paint/composite.

Hai từ giống nhau nhưng khác layer.

Có thể có case:

```text
React render nhiều
but DOM output nearly unchanged
→ browser layout small
```

Hoặc:

```text
React work nhỏ
but one DOM mutation invalidates large layout
→ browser rendering large
```

Vì vậy report phải nói rõ:

```text
framework render/reconciliation
vs
browser rendering pipeline
```

---

# 18. Measure commit/output, không chỉ function calls

Một component function chạy 20 lần chưa tự nói user bị chậm bao nhiêu.

Cần biết:

- mỗi run làm work gì;
- output có thay không;
- commit/mutation nào xảy ra;
- browser work sau commit là gì.

Count là signal, không phải verdict.

---

# 19. Memoization có cost và semantic risk

Memoization có thể tránh computation/render work lặp lại, nhưng cũng có:

- memory;
- comparison cost;
- dependency complexity;
- stale value bug nếu dependency model sai;
- cognitive cost.

Do đó:

```text
profile → find repeat expensive work → memoize candidate → remeasure
```

thay vì:

```text
component → memo everywhere
```

---

# 20. Event handler latency và rendering latency khác nhau

Một input handler có thể chạy 5 ms nhưng frame xuất hiện 80 ms sau vì rendering work.

Ngược lại handler có thể chạy 70 ms nhưng DOM change nhỏ.

Trace interaction phải giữ cả hai.

Một useful decomposition:

```text
input delay
processing time
presentation delay
```

Tên cụ thể trong metric/tool có thể khác theo platform, nhưng mental model giúp không đổ mọi latency cho handler.

---

# 21. Long task: boundary hữu ích nhưng không phải root cause

Nếu main thread bị một task dài, user input có thể phải chờ.

Nhưng “long task” chỉ nói container work dài.

Bên trong có thể là:

- application JavaScript;
- JSON transform;
- framework rendering;
- style/layout forced synchronously;
- third-party code;
- logging/instrumentation.

Drill down call stack/timeline để tìm owner.

---

# 22. Microtask starvation

Code có thể không có một synchronous loop lớn nhưng vẫn chain Promise/microtask liên tục.

Nếu microtasks tiếp tục tạo microtask mới, browser có thể bị trì hoãn trước rendering opportunity hoặc other task.

Lab nhỏ:

```js
function spin() {
  Promise.resolve().then(spin);
}
spin();
```

Không chạy vô hạn trong production. Đây chỉ là conceptual warning rằng:

```text
Promise-based
≠ automatically cooperative with rendering
```

Scheduling semantics quan trọng.

---

# 23. `requestAnimationFrame` không sửa algorithm nặng

`requestAnimationFrame` giúp schedule callback quanh rendering cycle, hữu ích cho visual updates.

Nhưng nếu callback làm 80 ms computation:

```text
rAF
→ 80 ms work
→ missed frames
```

API đúng không cứu workload quá lớn.

Nếu computation có thể split/offload, cần reasoning riêng về scheduling/worker/data transfer.

---

# 24. Worker không phải miễn phí

Web Worker có thể đưa CPU work khỏi main thread, nhưng có cost:

- message serialization/structured clone;
- transfer;
- worker startup;
- duplicated state/coordination;
- architecture complexity.

Dùng worker khi workload và latency justify, không phải vì “multithreading luôn nhanh hơn”.

Measure end-to-end:

```text
main thread freed
vs
communication overhead
vs
total latency
```

---

# 25. Scroll performance

Scroll jank có thể liên quan:

- main-thread event work;
- layout during scroll;
- large paint area;
- sticky/fixed effects;
- image decode/raster;
- huge DOM;
- third-party listeners.

Đừng chỉ search code `scroll` listener.

Record scroll session và xem work thực tế.

Nếu listener không xuất hiện đáng kể mà paint dominates, tối ưu listener không giải quyết vấn đề.

---

# 26. Resize performance

Resize là stress test tốt cho responsive layout.

Một layout có thể ổn khi static nhưng resize gây:

```text
repeated JS measurement
+
DOM write
+
forced layout
```

Nếu code resize handler tự đo/mutate liên tục, framework/CSS responsive features có thể bị vô hiệu hóa bởi application loop.

Trace để biết bottleneck ở CSS layout hay JS measurement pattern.

---

# 27. Image decode và raster là phần user-visible pipeline

Image request complete không nhất thiết pixel đã sẵn sàng ngay.

Browser còn cần decode/raster/process tùy format/path.

Với gallery lớn, network có thể nhanh nhưng image processing + memory vẫn gây jank.

Optimization có thể gồm:

- đúng resolution;
- lazy loading phù hợp;
- reserve dimensions;
- avoid decoding huge source chỉ để display thumbnail;
- reduce simultaneous heavy work.

Nhưng lại phải đo workload cụ thể.

---

# 28. Font performance

Font ảnh hưởng cả network lẫn layout.

Lab:

1. record page với fallback only;
2. record web font;
3. quan sát font request;
4. quan sát text/layout shift nếu có;
5. kiểm tra font size/weight subsets và usage.

Mục tiêu là thấy font decision không chỉ là design choice.

---

# 29. Hidden work

Một element invisible với user chưa chắc không tạo cost.

Tùy cách hide:

- nó có thể không participate layout;
- có thể vẫn giữ subtree/state/listeners;
- có thể vẫn được framework update;
- có thể giữ media/resource.

Không suy từ “không thấy trên màn hình” rằng work bằng 0.

Measure component/application behavior.

---

# 30. CSS selector folklore

Modern engines có nhiều optimization; selector syntax đơn lẻ hiếm khi là nơi nên bắt đầu nếu không có evidence.

Nếu style recalculation lớn, inspect:

- affected node count;
- invalidation source;
- selector/cascade structure;
- DOM scope;
- frequency.

Không dành hàng giờ đổi `.parent .child` thành `.child` nếu trace cho thấy 90% cost là JavaScript computation.

---

# 31. Containment và isolation

CSS/platform có các cơ chế giúp giới hạn scope layout/rendering trong một số scenario.

Nhưng containment thay semantic/layout behavior và cần hiểu contract.

Không thêm chỉ vì benchmark nhỏ đẹp hơn.

Kiểm tra:

```text
layout correctness
size behavior
overflow
accessibility
sticky/positioning interaction
```

Optimization không được phá invariant.

---

# 32. Performance fix có thể tạo accessibility regression

Virtualization hoặc custom scrolling có thể cải thiện frame time nhưng phá:

- keyboard navigation;
- screen-reader traversal;
- find-in-page;
- focus restoration;
- semantic table/list structure.

Do đó before/after không chỉ là timing.

Regression matrix phải gồm public behavior.

---

# 33. Performance fix có thể tạo correctness regression

Debounce search giúp giảm work nhưng thay semantics.

Nếu user type rồi immediately submit, pending debounced state có được commit đúng không?

Nếu filter là accessibility-critical feedback, delay có hợp lý không?

Optimization không được được đánh giá riêng khỏi behavior contract.

---

# 34. Performance fix có thể chuyển cost sang server/network

Client-side filter 100k records chậm.

Ta chuyển sang server search.

Client nhẹ hơn, nhưng system có thêm:

- request latency;
- server load;
- cancellation/stale race;
- pagination;
- cache;
- offline/error behavior.

Đây có thể vẫn là kiến trúc tốt, nhưng phải đánh giá end-to-end chứ không tuyên bố “frontend nhanh hơn” rồi dừng.

---

# 35. Production-like data quan trọng hơn toy data

Một table 20 rows không reveal bottleneck của table 20.000 rows.

Performance test cần data distribution gần use case:

```text
row count
text length
image count
column count
nested components
error/empty/loading states
```

Không cần copy dữ liệu nhạy cảm; synthetic dataset có cùng shape/distribution là đủ tốt hơn toy demo.

---

# 36. Tail latency

Average interaction 30 ms nhưng thỉnh thoảng 250 ms vẫn gây vấn đề.

Do đó đừng chỉ report mean.

Có thể xem distribution:

```text
median
p75
p95/p99 khi sample đủ
worst observed with context
```

Không cần dùng percentile nếu sample quá nhỏ để có ý nghĩa. Nhưng principle là performance có distribution.

---

# 37. Run-to-run variance

Garbage collection, background process, cache, JIT/runtime state và OS scheduling có thể làm run khác nhau.

Đừng kết luận từ một run:

```text
Before 102 ms
After 98 ms
→ 4% faster!
```

Nếu variance tự nhiên ±15 ms, kết luận đó không đáng tin.

Lặp run và nhìn effect size so với noise.

---

# 38. Synthetic lab và field telemetry trả lời câu hỏi khác nhau

Local trace giúp causal debugging sâu.

Field telemetry/RUM giúp biết user population thực gặp gì.

Mental model:

```text
Lab profiling
→ Why does this scenario cost what it costs?

Field telemetry
→ How often, for whom, on what devices/network, does this problem happen?
```

Một lab fix tốt nên sau đó được monitor field nếu app có telemetry.

---

# 39. Third-party scripts

Analytics, chat widget, tag manager hoặc ad/monitoring SDK có thể chiếm main thread/network.

Không loại chúng khỏi trace chỉ vì “không phải code team mình”.

User trả cost của toàn page.

Nếu third-party là bottleneck, mitigation có thể là:

- defer/lazy load;
- reduce provider count;
- conditional load;
- isolate;
- renegotiate requirement.

Architecture includes external dependencies.

---

# 40. Memory và GC

Rendering performance không chỉ frame timing.

Nếu component/list leak memory:

```text
navigation count ↑
→ retained objects ↑
→ GC pressure ↑
→ long pauses / eventual crash
```

Lab dài hơn có thể repeat open/close modal hoặc route navigation nhiều lần, sau đó inspect retention trend.

Một fast first run không chứng minh runtime stable sau hai giờ sử dụng.

---

# 41. Modal leak experiment

Scenario:

```text
open modal
close modal
repeat 100 times
```

Track:

- detached DOM nodes nếu observable;
- retained listeners/subscriptions;
- object count/memory trend;
- network/subscription duplication;
- later interaction latency.

Nếu memory tăng không quay lại ngay, chưa chắc leak vì GC timing. Cần inspect retention/reference path thay vì chỉ nhìn một memory number.

---

# 42. Large table experiment

Tạo three versions:

```text
A. render all rows
B. paginate
C. virtualize
```

So:

```text
startup
filter/update
scroll
memory
a11y/keyboard
complexity
```

Không có winner universal.

Pagination thay information architecture. Virtualization giữ continuous list feel nhưng tăng implementation complexity. Render all có thể hoàn toàn đủ cho 200 rows.

Optimization phải phù hợp scale thực tế.

---

# 43. Layout shift experiment

Tạo card với image không có reserved size.

Record.

Sau đó thêm width/height/aspect-ratio contract phù hợp.

Record lại.

Quan sát:

```text
geometry stability
layout work
user target movement
```

Bài này nối performance với correctness/UX mà không cần framework.

---

# 44. Stacking/overlay experiment

Tạo modal trong ancestor có transform/stacking context.

Thử tăng z-index rồi quan sát vì sao không vượt context ngoài.

Sau đó thay physical DOM placement/stacking architecture phù hợp.

Đây không phải performance lab trực tiếp, nhưng nó dạy nguyên tắc chung:

```text
đừng tối ưu hoặc sửa dựa trên property folklore;
trace tree/boundary thực tế.
```

---

# 45. Build artifact experiment

Profile local dev build và production build.

Không giả định production luôn nhanh hơn.

So:

```text
bundle graph
source maps/debug overhead
minification/tree shaking
runtime flags
code splitting
cache
initialization work
```

Nếu production-specific bug/perf regression xuất hiện, cần artifact-level evidence.

---

# 46. One-change rule

Khi benchmark, tránh commit cùng lúc:

```text
virtualization
+ memoization
+ CSS rewrite
+ API pagination
+ image lazy-load
```

Nếu result tốt hơn, không biết phần nào tạo effect.

Thực tế engineering đôi khi phải bundle fixes, nhưng learning/research phase nên cô lập variable càng nhiều càng tốt.

---

# 47. Performance report template

Mỗi experiment nên có:

```text
Question
Scenario
Environment
Build/artifact
Baseline
Trace observation
Hypothesis
Change
After measurement
Variance / uncertainty
Correctness regression check
Accessibility regression check
Conclusion
Next action
```

Không report chỉ:

```text
Before: slow
After: fast
```

---

# 48. Ví dụ report ngắn

```text
Question:
Why does filtering 5k rows exceed the interaction budget?

Baseline:
Median ~145 ms across 8 local runs.
Main cost: 68–75 ms JS filter/sort, 35–42 ms layout.

Hypothesis:
Repeated full sort and rendering all rows dominate.

Change 1:
Precompute normalized searchable field.

After:
JS cost reduced ~25 ms; layout unchanged.

Change 2:
Virtualize visible rows.

After:
Layout and paint reduced materially; keyboard/a11y behavior retested.

Conclusion:
Two independent bottlenecks existed: compute and rendered-node scale.
Memoization alone would not have solved layout cost.
```

Con số chỉ minh họa format, không phải threshold universal.

---

# 49. Performance budget phải có owner

Nếu team đặt budget:

```text
filter interaction < X
bundle < Y
layout work < Z
```

phải có owner và measurement path.

Một budget không được đo trong CI/telemetry/profile routine sẽ nhanh chóng thành documentation stale.

Nếu automation không ổn định, ít nhất cần checklist release/profile rõ.

---

# 50. Không tối ưu khi không có user problem hoặc system risk

Performance engineering có opportunity cost.

Không phải mọi 5 ms đều cần tối ưu.

Prioritize theo:

```text
user impact
frequency
scale
resource cost
business criticality
regression risk
```

Độ sâu không có nghĩa micro-optimize mọi function. Độ sâu là biết **khi nào optimization có bằng chứng đủ mạnh để đáng làm**.

---

# 51. Exit gate

Lab được xem là hoàn thành khi người học có thể đưa ra statement kiểu:

```text
"Interaction lag không đến từ network. Trong 10 run production-like,
main-thread work sau input có median khoảng N ms. Phần lớn đến từ X;
Y gây layout invalidation cho khoảng M nodes. Sau thay đổi Z,
category X giảm rõ so với run variance, trong khi keyboard/focus contract
vẫn pass."
```

thay vì:

```text
"Dùng transform vì GPU nhanh hơn."
```

Hoặc:

```text
"React render nhiều nên thêm memo."
```

Không có trace/evidence thì chưa đạt gate.

---

# 52. Bài tập cuối

Chọn một page thật và tạo hai trace:

## Trace A — interaction

Ví dụ filter/search/open modal.

Bắt buộc tách:

```text
input/event
scripting
style
layout
paint/composite
next useful frame
```

## Trace B — load/update

Ví dụ navigation hoặc API data update.

Bắt buộc tách:

```text
network/resource
parse/execute
state transition
DOM changes
rendering work
artifact/build identity
```

Sau đó chọn **một** bottleneck có evidence mạnh nhất, sửa và remeasure.

Cuối cùng ghi một đoạn post-mortem:

```text
What did I initially assume?
What did the trace actually show?
Which boundary was the real owner?
What regression guard should remain?
```

Nếu câu trả lời ban đầu và evidence khác nhau, đó không phải thất bại. Đó chính là lý do performance profiling tồn tại.

## Cross-link

- [Request → Pixel → Interaction Trace](./00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md)
- [`../COVERAGE_AUDIT.md`](../COVERAGE_AUDIT.md)
- CSS Master/Supplement cho cascade, layout, paint/composite reasoning.
- JavaScript Senior/Master cho event loop, long task, worker, performance và artifact boundary.
- React/WebSquare profiling chapter khi cần map browser evidence sang framework-specific ownership.
