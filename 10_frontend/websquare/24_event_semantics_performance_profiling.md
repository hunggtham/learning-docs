# 24 — Event Semantics, Reentrancy & Performance Profiling

WebSquare screen thường trông “event-driven”: user click, component phát event, handler sửa DataCollection, binding cập nhật UI, Submission chạy, callback lại sửa model. Khi project nhỏ, chuỗi này có vẻ tuyến tính. Khi project lớn, một mutation có thể kích hoạt nhiều event/binding/render path và timing trở thành nguyên nhân của bug hoặc performance regression.

Chapter này xây mental model để phân biệt **user event, framework event, model event, render effect và async continuation**, sau đó đo performance theo evidence thay vì tối ưu bằng cảm giác.

---

## 1. Event không phải business intent

Một click có thể đại diện business intent “Save”, nhưng click event chỉ là một input signal.

```text
DOM/browser interaction
→ WebSquare component event
→ page handler
→ validation
→ model mutation
→ Submission
→ server result
→ model update
→ render
```

Business intent nằm ở orchestration layer, không nằm trong raw event object.

Điều này quan trọng vì cùng một intent có thể đến từ keyboard shortcut, button, menu hoặc native bridge. Nếu business logic gắn chặt vào `btnSave_onclick`, reuse/testability giảm.

Pattern tốt hơn:

```javascript
scwin.btnSave_onclick = function () {
    scwin.requestSave();
};

scwin.requestSave = function () {
    // validate → snapshot → execute command
};
```

Handler chuyển signal thành command; command mới sở hữu workflow.

---

## 2. User-driven change và programmatic change có thể khác semantics

Một số WebSquare component phân biệt event do user interaction với value thay đổi bằng script. Official guide của một số component mô tả `onviewchange` chỉ phát khi user thay đổi view, không nhất thiết khi script set value.

Vì vậy không được giả định:

```text
setValue(x)
→ luôn phát cùng event như user chọn x
```

Nếu business rule phụ thuộc event tự phát sau programmatic mutation, code dễ break khi component/build khác behavior.

Rule tốt hơn:

```text
programmatic command
→ gọi explicit domain/page function cần thiết
```

Event nên quan sát interaction, không nên là hidden control-flow bus.

---

## 3. Event ordering là contract version-sensitive

Grid editing là ví dụ rõ. SP5 release notes có property `viewChangeAfterEdit` liên quan thứ tự `onviewchange` và `onafteredit` ở các build tương ứng.

Bài học không phải nhớ một default. Bài học là:

```text
event A exists
+ event B exists
≠ ordering luôn bất biến
```

Nếu correctness phụ thuộc A luôn trước B, hãy:

1. kiểm tra exact build/config;
2. viết regression test cho ordering;
3. tốt hơn nữa, giảm dependency vào implicit ordering bằng explicit state transition.

Upgrade engine có thể thay behavior dù source page không đổi.

---

## 4. Reentrancy: handler có thể kích hoạt chính hệ thống event nó đang xử lý

Ví dụ conceptual:

```text
onchange
→ normalize value
→ setValue(normalized)
→ onchange?
```

Tùy component/API, có thể không phát lại, phát event khác, hoặc trigger binding/render path. Nếu handler không idempotent, reentrancy tạo loop hoặc duplicate work.

Một normalization function tốt nên thỏa:

```text
normalize(normalize(x)) = normalize(x)
```

Tức idempotent về giá trị.

Nếu cần guard:

```javascript
if (scwin.isNormalizing) return;
scwin.isNormalizing = true;
try {
    // mutation
} finally {
    scwin.isNormalizing = false;
}
```

Guard là safety net; design tốt hơn là tách pure normalization khỏi event wiring.

---

## 5. Event storm và amplification

Một user action có thể sửa 1 DataMap field. Binding update 5 component. Mỗi component có formatter/validator/event. Một handler lại sửa 10 DataList row.

Work amplification:

```text
1 user action
→ N model mutations
→ N × M binding/render callbacks
→ formatter/expression calls
```

Performance issue không nằm ở “JavaScript chậm” chung chung mà ở amplification factor.

Khi profiling, đếm:

```text
bao nhiêu handler chạy?
bao nhiêu row/cell mutation?
bao nhiêu formatter/expression call?
bao nhiêu render/update?
```

---

## 6. Binding là convenience nhưng vẫn có cost

Binding giúp model là source of truth, nhưng mỗi bound component cần synchronization work.

Nếu code làm:

```text
for 10.000 rows:
  setCellData(...)
```

và mỗi mutation tạo event/render work, tổng cost khác hoàn toàn bulk set một snapshot rồi render một lần.

Exact bulk API tùy DataList/build; mental model là:

```text
mutation granularity
× observer count
× render cost
```

Cần tối ưu dominant multiplication, không chỉ micro-optimize callback syntax.

---

## 7. Đừng dùng DOM trực tiếp để “tối ưu” WebSquare component

SP5 best-practice guide cảnh báo việc trực tiếp điều khiển DOM/browser event của component WebSquare và khuyến nghị dùng framework abstraction. Lý do không chỉ style.

Engine có thể giữ state ngoài DOM. Nếu developer sửa DOM trực tiếp:

```text
DOM display
≠ component state
≠ DataCollection state
```

UI có thể trông nhanh/đúng tạm thời nhưng lần render sau engine ghi đè, accessibility/focus bị phá hoặc cleanup không biết reference mới.

Performance optimization không được phá ownership model.

---

## 8. Event handler budget

Một event chạy trên browser main thread. Nếu handler làm 80 ms synchronous work, input/render khác phải chờ.

Mental model:

```text
input latency
= queue wait
+ handler synchronous work
+ framework/model propagation
+ render/layout/paint
```

Không cần một con số “chuẩn” cho mọi screen. Cần đo interaction quan trọng và giữ long task khỏi critical path.

Heavy transformation có thể được chuyển khỏi hot event, precompute, cache hoặc server-side tùy ownership.

---

## 9. Formatter và expression là hot path tiềm ẩn

Grid formatter/expression nhìn nhỏ vì function ngắn. Nhưng nếu gọi cho hàng nghìn cell, complexity nhân lên.

Ví dụ:

```text
5.000 rows × 20 columns = 100.000 cell evaluations
```

Nếu mỗi formatter lại scan một DataList 5.000 row:

```text
100.000 × O(5.000)
```

thì bottleneck là algorithmic amplification.

Senior note: formatter nên gần pure, cheap và tránh network/global lookup. Lookup map nên được chuẩn bị trước nếu cần.

---

## 10. Sort/filter/group làm thay đổi cả cost lẫn identity

Sort/filter không chỉ đổi vị trí row. Nó có thể:

```text
recompute view
invalidate cached index
rerun formatter
rerender visible region
change selection/focus mapping
```

Vì vậy performance test Grid phải bao gồm interaction thật: sort, filter, edit, scroll, select, không chỉ đo initial load.

Chapter 13 giải thích identity; chapter này thêm cost model.

---

## 11. Performance budget theo stage

Đừng đo “screen mất 3 giây”. Chia:

```text
T_total
= T_resource
+ T_engine/page init
+ T_submission
+ T_server/network
+ T_parse/map
+ T_model mutation
+ T_render
+ T_post-render
```

Với interaction:

```text
T_interaction
= T_event queue
+ T_handler
+ T_model propagation
+ T_render/layout/paint
```

Khi stage rõ, optimization mới có target.

---

## 12. WebSquare performance instrumentation

Một số SP5 build cung cấp performance instrumentation và `WebSquare.util.setPerformanceUse(...)`; release notes cũng mô tả engine performance mark/measure có screen URL detail ở các build tương ứng.

Đây là evidence bổ sung, không thay browser profiler.

Kết hợp:

```text
WebSquare performance marks
+ Chrome Performance trace
+ Network timing
+ server correlation timing
+ custom business marks
```

để nối framework stage với browser/server stage.

Exact API/output phải kiểm tra engine build.

---

## 13. Custom mark phải đo business stage, không chỉ function

Tên mark hữu ích:

```text
employeeSearch:intent
employeeSearch:request-start
employeeSearch:response
employeeSearch:model-ready
employeeSearch:grid-ready
```

Tên ít hữu ích:

```text
fn1-start
fn1-end
```

Production question là “user chờ ở stage nào?”, không phải “function nào có tên fn1”.

---

## 14. Network timing phải tách server khỏi client

DevTools thấy request 1.5 s nhưng không tự nói server xử lý 1.5 s.

Có thể gồm:

```text
queue/stalled
connection/TLS
request upload
server wait
response download
client parse/mapping
```

Correlation ID + server timing giúp phân biệt.

Nếu response về 200 ms nhưng Grid usable sau 2 s, backend không phải dominant term.

---

## 15. Payload size là performance architecture

Một Grid chỉ hiển thị 30 row nhưng endpoint trả 50.000 row. Tối ưu formatter 20% không giải quyết network/memory/render architecture.

Các lựa chọn:

```text
server paging
server filtering
projection ít column hơn
lazy/detail fetch
chunk loading
```

SP5 có DataList/large-data capability thay đổi theo build, nhưng first principle vẫn là **không vận chuyển state client không cần sở hữu**.

---

## 16. Chunk loading không miễn phí consistency

Load data theo chunk giảm peak latency/memory nhưng tạo state:

```text
loaded range
pending range
failed range
sort/filter version
query version
```

Nếu user đổi filter giữa chunk 2 và 3, chunk cũ không được append vào query mới.

Cần query/version identity giống stale Submission guard.

Performance optimization tạo thêm lifecycle; lifecycle mới cần correctness model.

---

## 17. DataList metadata và large-data memory

SP5 release notes mới có optimization giảm rowStatus/cellStatus array element không cần thiết khi set large data. Điều này nhắc rằng DataList không chỉ chứa business values.

Memory model gần hơn:

```text
business cell values
+ row metadata
+ cell metadata
+ binding observers
+ Grid/render structures
+ formatter/cache objects
```

Do đó “JSON chỉ 10 MB” không có nghĩa heap tăng 10 MB.

---

## 18. Dynamic Submission có lifecycle cost

Official performance guide khuyến nghị khai báo Submission cần thiết ở business screen và cảnh báo dynamic creation phải kiểm tra duplicate ID.

Dynamic Submission có use case, nhưng tạo mọi request bằng generic factory có thể làm:

```text
ownership khó thấy
workflow linkage khó đọc
duplicate ID/lifetime khó kiểm soát
profiling/log identity kém ổn định
```

Performance và maintainability gặp nhau ở đây: static/declarative object khi phù hợp làm execution graph dễ quan sát hơn.

---

## 19. Debounce, throttle và coalescing giải quyết ba vấn đề khác nhau

Search-as-you-type có thể cần debounce: chỉ chạy sau khi user ngừng gõ một khoảng.

Scroll/resize có thể cần throttle: giới hạn tần suất xử lý.

Nhiều model mutation có thể cần coalescing/batching: gom update thành một logical commit.

Không dùng ba thuật ngữ như nhau.

Quan trọng hơn, debounce không thay stale-result guard. Request cũ vẫn có thể về sau request mới.

---

## 20. Repeated listener registration là correctness + performance bug

Page/tab mở nhiều lần và mỗi `onload` add listener vào global target nhưng không remove:

```text
open #1 → 1 handler
open #2 → 2 handlers
open #10 → 10 handlers
```

Một click chạy logic 10 lần. User thấy “app càng dùng càng chậm”.

Đây là lifetime leak, không phải chỉ memory leak.

Test:

```text
open → interact → close × 30
```

đo handler invocation count, heap và pending timers/listeners.

---

## 21. Timer loop phải có owner

`setInterval` polling trong page nhưng page close không clear:

```text
closed screen
→ timer alive
→ Submission alive
→ callback closure giữ scope
```

Hậu quả gồm network load, memory retention và stale mutation.

Timer cần owner/lifetime contract:

```text
create on active
pause on hidden/background nếu phù hợp
dispose on close
```

Chapter 21 mở rộng điều này cho polling/real-time connection.

---

## 22. Spinner và process message có thể che latency nhưng không sửa latency

Process message tốt cho UX khi operation thật sự cần chờ. Nhưng “thêm loading” không phải performance fix.

Nếu interaction 150 ms, spinner có thể gây visual flicker. Nếu 8 s, cần stage timing và cancellation/retry policy.

UX feedback và system performance là hai trục liên quan nhưng khác nhau.

---

## 23. Performance test phải giữ production-like shape

Test 100 row rồi production 30.000 row không cho evidence hữu ích.

Dataset cần đại diện:

```text
row count
column count
text length
formatter complexity
editability
selection/accessibility mode
sort/filter pattern
```

Accessibility có thể thay rendering configuration ở Grid build tương ứng, vì vậy benchmark phải dùng mode production thật.

---

## 24. Measure warm và cold path riêng

Cold path có thể gồm:

```text
resource load
W-Pack/module load
component creation
first formatter/cache initialization
first network/TLS
```

Warm path có thể reuse cache/object.

Nếu chỉ benchmark lần thứ 10, startup regression bị bỏ qua. Nếu chỉ benchmark cold load, interaction thường ngày bị che.

---

## 25. Performance regression guard

Không cần mọi metric thành hard threshold. Nhưng critical path nên có baseline:

```text
screen ready
search usable
Grid render after response
Save round-trip
heap after repeated open/close
number of requests
payload size
```

Khi engine upgrade hoặc component config đổi, compare baseline trước/sau.

Performance regression test đặc biệt quan trọng vì source business code có thể không đổi nhưng engine/render behavior đổi.

---

## 26. Case study — `onchange` làm Search chạy hai lần

Một common handler normalize code rồi programmatically update component. Một event path khác cũng gọi Search.

User thay một field nhưng hai Submission chạy.

Debug bằng:

```text
event trace
handler invocation count
requestId
stack/call path
```

Fix không phải disable request thứ hai ngẫu nhiên; cần một command owner duy nhất cho Search.

---

## 27. Case study — Grid 2.000 row chậm sau thêm formatter

Formatter mới lookup label bằng cách scan code DataList cho từng cell.

```text
rows 2.000
× columns 8
× code rows 500
```

Hàng triệu comparison phát sinh.

Fix:

```text
prepare codeMap once
→ O(1)-like lookup per cell
```

hoặc bind/lookup mechanism phù hợp của framework.

Evidence phải cho thấy formatter hot path giảm, không chỉ cảm giác “nhanh hơn”.

---

## 28. Case study — Engine upgrade làm edit behavior đổi

Sau upgrade, validation chạy trước/after event khác với assumption cũ do property/default/event ordering thay đổi.

Source page không đổi nhưng behavior đổi.

Root cause graph:

```text
engine build
→ event semantics
→ handler assumption
→ business behavior
```

Regression suite cần capture event ordering quan trọng và compatibility matrix phải coi event semantics là upgrade surface.

---

## 29. Case study — Search nhanh nhưng screen vẫn treo

Network 300 ms. DataList mapping 100 ms. Grid render 2.4 s.

Team tối ưu SQL từ 180 ms xuống 120 ms, user gần như không cảm nhận.

Dominant term là render.

Performance budget buộc team sửa đúng layer: row count, column complexity, formatter, render strategy hoặc paging.

---

## 30. Profiling playbook

Khi screen chậm:

```text
1. Xác định user-visible interval.
2. Gắn intent/request/build/screen identity.
3. Đo Network và server timing.
4. Đo response parse/model mapping.
5. Record browser Performance trace.
6. Tìm long task/hot handler/formatter.
7. Đếm mutation/render amplification.
8. Kiểm tra payload/dataset shape.
9. Kiểm tra repeated listener/timer/request.
10. Thay đổi một dominant factor.
11. Đo lại cùng dataset/build/config.
12. Tạo regression guard.
```

Không bắt đầu bằng việc rewrite function dài nhất nếu chưa có evidence nó nằm trên critical path.

---

## 31. Event architecture review checklist

```text
Event này là user signal hay business command?
Programmatic mutation có dựa vào implicit event không?
Ordering giữa event có build-dependent không?
Handler có thể re-enter không?
Handler có idempotent không?
Một intent có tạo duplicate command không?
Model mutation có amplification lớn không?
Formatter/expression có chạy trong hot path không?
Listener/timer có owner và cleanup không?
Async callback có stale-intent guard không?
```

---

## 32. Performance review checklist

```text
User-visible budget được chia stage chưa?
Dominant term là network/server/model/render ở đâu?
Payload có lớn hơn state UI cần không?
Grid dataset production shape là bao nhiêu?
Có server paging/filtering phù hợp không?
Bulk mutation có đang thành hàng nghìn fine-grained mutation không?
Code lookup có complexity ẩn trong formatter không?
Cold/warm path đã đo riêng chưa?
Engine/build/config identity có được ghi lại không?
Repeated lifecycle có tăng heap/listener/request count không?
Optimization đã được đo lại bằng cùng scenario chưa?
```

---

## 33. Master synthesis

Event-driven WebSquare app có thể nhìn như graph:

```text
Signal graph
browser/user/native
→ component event
→ command

State graph
command
→ DataCollection mutation
→ binding
→ render

Async graph
command
→ Submission/workflow
→ continuation
→ state convergence

Cost graph
handler
→ observers
→ formatter/expression
→ render/layout/paint
```

Bug correctness thường đến từ graph crossing sai identity hoặc ordering. Bug performance thường đến từ amplification giữa các graph.

Ở mức Master, developer không hỏi “event nào chạy?” một cách cô lập. Họ hỏi:

```text
signal nào đại diện intent nào,
command owner là ai,
state transition nào xảy ra,
observer nào bị kích hoạt,
ordering nào là contract,
work được khuếch đại bao nhiêu lần,
và evidence nào chứng minh critical path.
```

Đó là khác biệt giữa biết event API và hiểu runtime behavior.

---

## 34. Nguồn kiểm chứng theo build

Exact event semantics, Grid event ordering, performance instrumentation và component rendering behavior phải đối chiếu WebSquare5 SP5 Development Guide/API Reference/Release Notes đúng engine build. Các release note liên quan `viewChangeAfterEdit`, engine performance mark/measure, `WebSquare.util.setPerformanceUse`, DataList large-data memory optimization và performance best-practice là nguồn đặc biệt hữu ích.

Không copy private API từ một build sang canonical code. Dùng public API và regression evidence để bảo vệ behavior cần thiết.