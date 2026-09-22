# 08 — Reusable Architecture, UDC & Common Modules

WebSquare enterprise project thường không thất bại vì thiếu một API để set value. Nó thất bại khi hàng trăm màn hình cùng giải quyết một vấn đề theo hàng trăm cách khác nhau: mỗi màn hình tự tạo popup, tự validate, tự format date, tự dựng search condition, tự gọi Submission, tự xử lý Grid và tự truy cập page khác. Vì vậy abstraction và reusable architecture là phần bắt buộc nếu muốn đọc hoặc duy trì codebase lớn.

Chapter này không dạy “cách tạo UDC” theo kiểu thao tác Studio. Mục tiêu là hiểu **khi nào một thứ nên trở thành UDC, common function, page template, layout, snippet hay page riêng**, public contract của abstraction nên có hình dạng nào, và failure mode nào xuất hiện khi tái sử dụng sai boundary.

## 1. Bài toán thật sự của reuse

Reuse không có nghĩa là càng gom nhiều code vào common càng tốt. Hai đoạn code giống nhau về chữ chưa chắc đại diện cùng một concept. Ngược lại, hai màn hình nhìn khác nhau có thể cùng tuân theo một invariant và nên dùng chung abstraction.

Ví dụ ba màn hình đều có nút tìm nhân viên. Nếu chỉ giống nhau ở việc mở popup nhưng mỗi nghiệp vụ dùng popup khác nhau, ép chúng vào một helper khổng lồ có thể làm coupling tăng. Nhưng nếu cả ba thực sự cùng cần contract:

```text
input: employeeId?, departmentId?, selectableStatus
output: { employeeId, employeeName, departmentId }
```

thì đây là một reusable business interaction hợp lý.

Mental model quan trọng là:

```text
reuse tốt = shared invariant + stable contract
reuse xấu = shared syntax + hidden branching
```

Một helper có 12 boolean flag thường là dấu hiệu nhiều concept khác nhau đã bị ép vào cùng function.

## 2. Các mức abstraction nên phân biệt

Trong WebSquare project, có nhiều mechanism tái sử dụng nhưng chúng giải quyết vấn đề khác nhau.

**Common JavaScript module** phù hợp cho logic không cần sở hữu UI lifecycle, chẳng hạn normalize dữ liệu, format domain value, tạo request metadata hoặc kiểm tra một rule thuần.

**Snippet** phù hợp cho scaffolding hoặc pattern code lặp khi tạo source, nhưng không tạo runtime abstraction. Sau khi chèn snippet, các bản sao có thể tiến hóa riêng.

**Page template/layout template** chuẩn hóa cấu trúc màn hình ban đầu. Nó giúp consistency khi tạo page nhưng không đồng nghĩa mọi instance dùng chung runtime object.

**WFrame/page composition** phù hợp khi một khu vực UI có lifecycle, DataCollection và behavior riêng, cần được load như một page boundary.

**UDC (User Defined Component / 사용자 정의 컴포넌트)** phù hợp khi muốn tạo một UI component có public property, method và event riêng, xuất hiện như một component có contract rõ trong Studio/runtime.

Không nên chọn mechanism dựa trên câu hỏi “cái nào tiện nhất lúc này”. Hãy hỏi object mới cần sở hữu điều gì: source template, pure logic, UI state, lifecycle hay component contract.

## 3. UDC là component contract, không phải một file include đẹp hơn

Official WebSquare5 guide cho phép UDC khai báo property, method và event; property được đọc qua `$p.getOptions()` và UDC có thể được đưa vào Palette. Điều này cho thấy UDC nên được hiểu như một **component type do project định nghĩa**, không chỉ là một đoạn XML tái sử dụng.

Nếu một UDC `EmployeeSearch` có property:

```text
requiredDepartment
allowInactive
placeholder
```

method:

```text
getSelectedEmployee()
clear()
openSearch()
```

và event:

```text
onemployeechange
onsearchopen
```

thì page sử dụng nó không cần biết bên trong UDC dùng Input, Trigger, Popup hay DataMap nào.

Đây là nguyên lý đóng gói (encapsulation / 캡슐화): **consumer phụ thuộc public contract, không phụ thuộc internal component ID**.

## 4. Public property phải là cấu hình, không phải remote control

Property tốt mô tả trạng thái cấu hình tương đối ổn định:

```text
mode="readonly"
required="true"
maxResult="20"
```

Property xấu thường bắt consumer truyền quá nhiều implementation detail:

```text
innerInputId="..."
innerButtonId="..."
parentGridId="..."
parentDataListId="..."
```

Nếu một UDC cần biết ID component bên ngoài để hoạt động, boundary đã bị đảo ngược. Component reusable đang điều khiển consumer thay vì cung cấp capability cho consumer.

Thay vào đó, expose event/result và để page cha quyết định cập nhật model nào.

## 5. Method là command trên abstraction

Một method public nên diễn đạt hành vi theo domain/component capability:

```javascript
employeePicker.clear();
employeePicker.openSearch();
var employee = employeePicker.getSelectedEmployee();
```

Không nên expose method chỉ để mirror toàn bộ internals:

```javascript
employeePicker.getInnerInput().setValue(...);
employeePicker.getInternalDataMap().set(...);
```

Nếu consumer thường xuyên phải chui vào internals, abstraction không thực sự đóng gói gì cả.

Senior note: public API nhỏ thường tốt hơn public API lớn. Mỗi API public là compatibility promise mà project phải giữ khi UDC được refactor.

## 6. Event đảo chiều dependency

Component reusable không nên biết consumer sẽ làm gì sau khi user chọn dữ liệu. Nó phát event và cung cấp payload.

Conceptual flow:

```text
UDC internal interaction
→ UDC validates internal state
→ UDC emits onemployeechange(payload)
→ consumer decides business consequence
```

Consumer có thể update DataMap, refresh Grid hay không làm gì thêm. UDC không cần biết.

Đây là inversion of control ở cấp UI. Nó giảm coupling mạnh hơn việc UDC gọi `$p.parent().scwin.someFunction()` bằng tên cố định.

## 7. `$p.getOptions()` và initialization timing

UDC property thường được đưa vào component options. Khi đọc option, cần phân biệt **construction-time configuration** với **runtime mutable state**.

Nếu một property được dùng để quyết định cấu trúc component khi khởi tạo, thay đổi nó sau render có thể không tự tái cấu hình internals trừ khi UDC tự cung cấp setter tương ứng.

Do đó contract nên nói rõ:

```text
Property nào chỉ đọc khi init?
Property nào có setter runtime?
Setter thay đổi model, style hay re-render?
```

Nếu không có distinction này, consumer dễ tưởng mọi property là reactive configuration.

## 8. UDC state ownership

Một UDC có thể có state nội bộ, nhưng phải xác định state nào thuộc UDC và state nào thuộc page.

Ví dụ employee picker có thể sở hữu:

```text
popup opened?
current display label
internal validation message
```

Page nên sở hữu business state chính:

```text
employeeId used in search condition
selected employee used for save
```

Nếu UDC giữ một copy employee object và page cũng giữ một copy trong DataMap, hai nguồn sự thật có thể drift. Khi có binding hoặc setter, nên thiết kế một chiều dữ liệu rõ ràng.

## 9. Controlled và uncontrolled mental model

Dù WebSquare không dùng thuật ngữ React, distinction này vẫn hữu ích.

Một component **self-owned** giữ value nội bộ và consumer hỏi value khi cần.

Một component **model-bound** lấy canonical value từ DataCollection/binding và interaction cập nhật model.

Cả hai đều có thể hợp lệ. Vấn đề xuất hiện khi trộn hai model mà không có precedence rule.

Ví dụ UDC vừa bind `dmForm.employeeId`, vừa giữ `scwin.selectedEmployeeId`, lại còn cho parent set trực tiếp Input value. Đây là ba source of truth.

## 10. Common module nên thuần khi có thể

Common function càng ít phụ thuộc Scope/component càng dễ test và reuse.

Tốt:

```javascript
common.normalizePhone = function (value) {
    return String(value || "").replace(/[^0-9]/g, "");
};
```

Coupling cao:

```javascript
common.normalizePhone = function () {
    inputPhone.setValue(inputPhone.getValue().replace(...));
};
```

Function thứ hai chỉ chạy nếu đúng page có đúng ID và đúng scope context.

Rule thực tế:

```text
Nếu logic có thể nhận value và trả value → giữ pure.
Nếu cần thao tác page → để page orchestration gọi pure function rồi update component/model.
```

## 11. Common object không nên trở thành service locator toàn ứng dụng

Enterprise codebase thường bắt đầu bằng `gcm`, `com`, `common` nhỏ rồi dần thành object chứa mọi thứ:

```text
popup
submission
session
permission
format
DOM
Grid
business code
component lookup
navigation
```

Khi đó mọi page phụ thuộc common global object và common object phụ thuộc mọi page convention. Đây là circular architecture.

Nên chia theo capability ổn định, chẳng hạn:

```text
formatting
navigation contract
submission helper
message/notification
permission adapter
```

nhưng vẫn tránh helper che mất WebSquare semantics. Ví dụ wrapper Submission không nên nuốt hết error để caller chỉ nhận `true/false`; caller cần đủ evidence để xử lý business failure.

## 12. Wrapper API phải giữ semantics quan trọng

Giả sử project tạo:

```javascript
common.submit("sbmSave");
```

Nếu wrapper này tự disable button, tự hiện loading, tự retry, tự show success message và tự refresh page, developer không còn biết side effect thực tế.

Wrapper tốt thường chuẩn hóa phần boilerplate nhưng vẫn expose lifecycle rõ:

```text
before request
success transport
business result
error
finally
cancel
```

Abstraction không được đổi một protocol nhiều trạng thái thành một boolean nghèo thông tin.

## 13. Dynamic component creation

WebSquare hỗ trợ tạo component/UDC động bằng API như `$p.dynamicCreate()` ở các build tương ứng. Dynamic UI hợp lý khi số lượng hoặc loại component thực sự phụ thuộc runtime data.

Không nên dùng dynamic creation chỉ để né XML authoring. Dynamic component tăng yêu cầu quản lý:

```text
unique ID
scope ownership
event registration
binding
cleanup
render cost
```

Nếu một cấu trúc UI luôn tồn tại, declarative XML thường dễ inspect và maintain hơn.

## 14. Generator và repeated UI

Generator phù hợp khi cần lặp một UI structure theo collection. Mental model khác GridView: GridView là specialized tabular interaction; Generator là repeated component composition linh hoạt hơn.

Khi lựa chọn, hỏi:

```text
Dữ liệu có bản chất bảng không?
Có cần sorting/editing/cell semantics không?
Hay mỗi item là một card/form complex?
```

Nếu ép mọi repeated UI vào Grid chỉ vì quen Grid API, UX và rendering architecture có thể trở nên méo mó.

## 15. Dynamic event registration và cleanup

Event được khai báo trong page XML thường gắn với lifecycle component. Event đăng ký động bằng code cần có ownership rõ.

Nếu page tạo event trên `window`, `document` hoặc object sống lâu hơn page, unload page không nhất thiết tự hiểu callback nào do business code đăng ký.

Do đó bất kỳ dynamic subscription nào cũng nên trả lời được:

```text
Ai đăng ký?
Ai sở hữu listener?
Khi nào unregister?
Nếu page mở 20 lần thì listener có thành 20 bản không?
```

Đây là điểm giao giữa reusable architecture và memory leak.

## 16. Page template không phải runtime inheritance

Template giúp tạo nhiều page với cấu trúc ban đầu giống nhau, nhưng sau khi sinh source, mỗi page là source riêng. Nếu muốn thay đổi behavior dùng chung ở runtime, sửa template cũ không tự sửa các page đã sinh.

Vì vậy hãy tách:

```text
creation-time consistency → template/snippet
runtime shared behavior → common module/UDC/component contract
```

Không hiểu distinction này thường dẫn đến câu hỏi “tại sao tôi sửa template mà màn hình cũ không đổi?”.

## 17. WFrame reuse và UDC reuse khác nhau

WFrame page thường là một **screen/module boundary**: có DataCollection, Submission, lifecycle, navigation context.

UDC thường là **component boundary**: một capability UI nhỏ hơn với property/method/event contract.

Nếu một UDC chứa cả search page, 8 Submission, business permission và routing, có thể abstraction đã quá lớn. Ngược lại nếu một reusable screen được nhét vào UDC chỉ để gọi vài method, navigation/lifecycle trở nên khó reasoning.

## 18. Cross-scope dependency injection bằng data, không bằng object internals

Khi một reusable page cần context, truyền plain data hoặc public service contract hẹp tốt hơn truyền component instance.

Tốt:

```text
{ userId, mode, permissions }
```

Rủi ro:

```text
{ parentGrid, parentDataList, parentWindow, callbackThatTouchesEverything }
```

Plain data làm boundary dễ serialize, log, test và replay.

## 19. Versioning reusable component

Một UDC dùng ở 200 page là internal platform API. Thay đổi nhỏ cũng có blast radius lớn.

Trước khi đổi public property/method/event, phân loại:

```text
backward-compatible addition
behavioral change
contract break
visual-only change
performance change
```

Nếu buộc breaking change, migration nên có search strategy và regression set rõ. Đừng đổi method semantic nhưng giữ nguyên tên khiến old consumer chạy mà sai âm thầm.

## 20. Anti-pattern: abstraction chỉ chuyển tên API

Wrapper như:

```javascript
common.setValue = function(component, value) {
    component.setValue(value);
};
```

không tạo mental model mới, không chuẩn hóa invariant, không giảm coupling. Nó chỉ thêm một indirection.

Abstraction có giá trị khi nó đóng gói policy hoặc invariant, ví dụ:

```text
normalize domain value
apply permission consistently
serialize a standard request envelope
open popup with stable result contract
```

## 21. Testing strategy cho reusable layer

Pure common logic có thể test độc lập khỏi WebSquare runtime nếu project toolchain cho phép.

UDC cần contract tests theo behavior:

```text
property input → initial state
user action → emitted event payload
method call → observable component state
invalid input → validation behavior
open/close repeatedly → no duplicated listener/timer
```

Không nên test UDC chỉ bằng DOM snapshot. Public behavior mới là compatibility surface.

## 22. Production evidence khi reusable abstraction lỗi

Khi một shared UDC lỗi ở 30 màn hình, sửa nhanh trực tiếp UDC có thể có blast radius cực lớn. Trước hết cần phân biệt:

```text
UDC internal defect?
consumer dùng sai contract?
engine build behavior khác?
CSS/theme override?
shared config drift?
```

Evidence nên gồm page instance, UDC version/source hash, engine build, option payload, emitted event và reproduction tối thiểu.

## 23. Case study: EmployeePicker

Giả sử nhiều màn hình cần chọn nhân viên. Thiết kế tốt có thể như sau.

UDC nhận property `allowInactive` và `requiredDepartment`. Nội bộ nó có Input hiển thị tên, hidden/model state giữ `employeeId`, Trigger mở popup và validation message. Popup nhận filter bằng plain data. Khi user chọn, UDC cập nhật state và phát `onemployeechange` với payload `{employeeId, employeeName, departmentId}`.

Page consumer bind result cần thiết vào `dmForm` trong handler event. Page không biết ID Input nội bộ của UDC; UDC không biết `dmForm` của page.

Nếu sau này UI đổi từ popup sang autocomplete server-side, consumer contract có thể giữ nguyên. Đó là dấu hiệu abstraction boundary tốt.

## 24. Checklist reasoning trước khi tạo common abstraction

Trước khi tạo helper/UDC mới, hãy trả lời:

```text
Shared invariant là gì?
Owner của state là ai?
Public input/output là gì?
Lifecycle bắt đầu/kết thúc ở đâu?
Consumer có cần biết internal ID không?
Có hidden dependency vào parent/top scope không?
Có thể log/test contract độc lập không?
Breaking change sẽ ảnh hưởng bao nhiêu consumer?
```

Nếu chưa trả lời được, abstraction có thể đang được tạo quá sớm.

## 25. Connection với các chapter khác

Scope và WFrame boundary được giải thích ở [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md). Data contract và Submission nằm ở [03 — DataCollection & Submission](03_data_collection_submission.md). Memory leak do dynamic listener và long-lived SPA được đào sâu ở [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).

JavaScript closure/module semantics không lặp lại ở đây; xem [JavaScript Intermediate](../javascript/javascript_intermediate.md) và [JavaScript Senior](../javascript/javascript_senior.md).

## Nguồn chính thức nên đối chiếu

WebSquare5 SP5 Development Guide — UDC 생성: `https://docs1.inswave.com/sp5_user_guide/0825289df4df8d45`

WebSquare5 SP5 Development Guide — 화면 그리기 / resource types: `https://docs1.inswave.com/sp5_user_guide/740ba8f1ef906f13`

API và behavior cụ thể của `$p.dynamicCreate()`, Generator, property/method/event phải được kiểm tra theo engine build project đang chạy.