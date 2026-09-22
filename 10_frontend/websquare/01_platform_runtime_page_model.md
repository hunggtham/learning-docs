# 01 — Platform, Runtime & Page Model

## 1. WebSquare không phải là “JavaScript có thêm vài API”

Cách dễ hiểu sai nhất là nhìn một file WebSquare, thấy JavaScript trong `<script>` rồi kết luận rằng đây chỉ là một trang web bình thường có thêm thư viện component. Cách nhìn đó bỏ qua phần quan trọng nhất: WebSquare cung cấp một **runtime quản lý page** (page runtime / 페이지 런타임). Runtime này tạo component object, quản lý page lifecycle, binding, data model, communication object, frame/scope và rendering abstraction.

JavaScript vẫn là JavaScript. Closure, `this`, event loop, Promise, exception, object reference và garbage collection vẫn tuân theo runtime của browser. Nhưng object mà code thao tác thường không phải DOM node trực tiếp. `input1`, `gridView1`, `dataList1` hay `submission1` là object do WebSquare Engine quản lý. Điều này tạo ra hai tầng semantics chồng lên nhau: semantics của JavaScript và semantics của framework.

Nếu một bug nằm ở closure hoặc async ordering, học thêm API WebSquare không giải quyết được. Ngược lại, nếu bug do page đang ở WFrame khác Scope, chỉ biết JavaScript thuần cũng chưa đủ. Senior developer phải xác định đúng tầng trước khi sửa.

## 2. Từ source đến runtime: XML → W-Pack → Engine → browser

WebSquare Studio cho phép author màn hình dưới dạng XML. XML mô tả component tree, DataCollection, Submission, workflow và script. Trong WebSquare5 SP5, W-Pack có thể chuyển page XML thành JavaScript đặt trong `_wpack_`. Browser gọi page theo URL, nhưng engine có thể thực sự tải artifact JavaScript đã được build để render nhanh hơn.

Mental model nên là:

```text
page.xml
   │
   ├─ component declaration
   ├─ dataCollection
   ├─ submission
   └─ script
   │
   ▼
W-Pack / build transformation
   │
   ▼
page JavaScript artifact
   │
   ▼
WebSquare Engine
   │
   ├─ create component objects
   ├─ create page/scope objects
   ├─ connect bindings
   ├─ install event handlers
   └─ render DOM
   │
   ▼
Browser
```

Điều này giải thích một hiện tượng thường làm người mới bối rối: source file họ sửa là XML nhưng stack trace, Network tab hoặc runtime object lại cho thấy JavaScript. Đó không phải hai ứng dụng khác nhau. XML là authoring representation; JavaScript mới là representation thuận tiện cho runtime.

Đọc thêm nền XML tại [XML Beginner](../xml/xml_01_beginner_detailed.md). Library này không lặp lại namespace, element tree hay well-formed XML.

## 3. Studio và Engine giải quyết hai nhiệm vụ khác nhau

WebSquare Studio là môi trường phát triển (development environment / 개발 환경). Nó cung cấp design view, source view, palette, property editor, preview, debug support và tooling để tạo page.

WebSquare Engine là runtime chạy ứng dụng. Engine đọc hoặc tải artifact của page, dựng component, điều phối lifecycle và cho phép API WebSquare hoạt động trong browser.

Việc tách hai khái niệm này giúp tránh một lỗi reasoning phổ biến: “Studio hiển thị đúng” không đồng nghĩa “runtime production chắc chắn đúng”. Studio có thể dùng cấu hình local, resource path, engine build hoặc mock khác với môi trường tích hợp. Khi lỗi chỉ xảy ra trên server, hãy kiểm tra runtime evidence chứ không suy từ màn hình Design.

## 4. Page WebSquare gồm những lớp gì?

Một page thường có thể hình dung thành bốn vùng logic.

Phần **UI declaration** mô tả component như Input, Button, GridView, Group, WFrame. Đây là cấu trúc hiển thị và interaction surface.

Phần **DataCollection** mô tả dữ liệu client-side. `DataMap` phù hợp với một bản ghi hoặc một nhóm key/value; `DataList` phù hợp với nhiều dòng; `LinkedDataList` cung cấp view đã filter/sort từ DataList.

Phần **Submission** mô tả giao tiếp với server: endpoint, request reference, response target và lifecycle của request.

Phần **script** chứa page behavior. Trong page theo Scope model hiện đại, function thường nằm dưới `scwin`.

Một ví dụ rút gọn có dạng tư duy như sau:

```xml
<xf:model>
    <w2:dataCollection>
        <!-- dmSearch, dlResult ... -->
    </w2:dataCollection>
    <!-- sbmSearch ... -->
</xf:model>

<script type="text/javascript" lazy="false">
    scwin.btnSearch_onclick = function () {
        scwin.search();
    };
</script>

<!-- UI components -->
```

Đừng học thuộc markup này như template. Điều quan trọng là hiểu dependency: **UI event → page function → client data model → Submission → server → response target → bound UI**.

## 5. Component object khác DOM element

Giả sử page có Input ID `inputName`. Code có thể gọi:

```javascript
inputName.setValue("Kim");
var value = inputName.getValue();
```

`inputName` ở đây là component API object do WebSquare expose, không nên mặc định coi nó là raw DOM `<input>`. Component có thể có format, validation, binding, event mediation và internal markup riêng. Một component nhìn như một input đơn giản có thể render thành nhiều DOM node hoặc thay đổi cấu trúc giữa engine build.

Hệ quả là code production nên ưu tiên **component API** thay vì đi xuyên vào DOM nội bộ bằng selector. DOM hacking có ba rủi ro:

Thứ nhất, bạn có thể thay đổi phần hiển thị nhưng không thay đổi framework state. UI nhìn đúng nhưng `getValue()` hoặc Submission vẫn lấy dữ liệu cũ.

Thứ hai, internal DOM structure không phải public contract. Engine update có thể thay class hoặc nesting.

Thứ ba, event được framework quản lý có thể không chạy nếu bạn sửa DOM theo đường tắt.

Chỉ nên thao tác DOM trực tiếp khi public API không đáp ứng yêu cầu và bạn đã xác nhận contract, test regression và upgrade risk.

## 6. ID không chỉ là chuỗi để query DOM

Trong WebSquare, ID là cách runtime định danh component trong Scope. Khi Scope/WFrame được dùng, engine có thể thay đổi ID vật lý ở DOM để tránh collision, trong khi script vẫn truy cập bằng logical ID đã khai báo.

Do đó một CSS rule dựa vào raw `#id` có thể dễ vỡ hơn class-based styling trong môi trường WFrame. Nếu cùng một page được mở hai lần ở hai frame, logical component ID có thể giống nhau nhưng mỗi Scope vẫn tách biệt.

Đây là lý do phải tách ba khái niệm:

```text
logical component ID
        ≠
physical DOM id
        ≠
page Scope identity
```

Nếu không phân biệt ba lớp này, developer rất dễ gặp bug “console tìm thấy hai id”, “CSS không ăn trong popup”, hoặc “gọi component cùng tên nhưng ra màn hình khác”.

## 7. `scwin`: namespace của page behavior

Trong Scope-based page, WebSquare thường dùng `scwin` làm Scope variable. Thay vì tạo function global:

```javascript
function search() {
    // ...
}
```

page viết:

```javascript
scwin.search = function () {
    // ...
};
```

Về mặt reasoning, `scwin` giống một namespace đại diện cho behavior của page hiện tại. Nó giảm collision giữa nhiều page cùng được mount trong một shell hoặc WFrame structure.

Một pattern tốt:

```javascript
scwin.btnSearch_onclick = function () {
    scwin.search();
};

scwin.search = function () {
    if (!scwin.validateSearchCondition()) {
        return;
    }

    $p.executeSubmission(sbmSearch);
};

scwin.validateSearchCondition = function () {
    return inputKeyword.getValue().trim().length >= 2;
};
```

Handler chỉ đóng vai trò adapter từ UI event sang page behavior. Validation và orchestration có tên riêng, có thể đọc và test reasoning dễ hơn.

Anti-pattern thường thấy là dồn hàng trăm dòng vào `onclick`, vừa đọc giá trị, sửa 10 component, duyệt grid, gọi nhiều submission và xử lý popup. Code kiểu đó biến event thành một “god function”.

## 8. `$p`: utility hiểu page Scope

WebSquare có họ utility trước đây thường gắn với `$w`; trong Scope model, các utility page-aware được expose qua `$p`. Mental model thực dụng là: `$p` đại diện cho các WebSquare operation cần biết **page hiện tại đang ở Scope nào**.

Ví dụ:

```javascript
$p.executeSubmission(sbmSearch);
$p.openPopup("/user/detail.xml", options);
var parentScope = $p.parent();
var topScope = $p.top();
```

Điểm quan trọng không phải nhớ `$p` có bao nhiêu method. Điểm quan trọng là khi một utility cần resolve component/page relative to current Scope, `$p` giúp framework giữ context đó.

Chapter [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md) sẽ đào sâu `$p.parent()`, `$p.main()`, `$p.top()`, `$p.getWindow()` và failure mode khi đi sai Scope.

## 9. Page lifecycle: code không chạy trong vacuum

Một page phải trải qua load, script initialization, component creation/render, data binding và page events. WebSquare có các cấu hình liên quan đến thứ tự script như `scriptPrecedence`, `postDrawMode` và JavaScript `lazy` behavior. Chính vì vậy code chạy “sớm quá” có thể không nhìn thấy component, còn code chạy “muộn quá” có thể gây flash hoặc duplicate request.

Đừng giải quyết lifecycle bug bằng `setTimeout(..., 100)` trừ khi timeout chính là business requirement. Timeout chỉ che race condition. Câu hỏi đúng là:

```text
Object này được tạo ở lifecycle phase nào?
Code của tôi chạy ở phase nào?
Có event/callback chính thức nào biểu diễn readiness không?
```

Nếu cần delay vì page con chưa load, hãy dùng event/load contract của WFrame/Tab/Popup tương ứng thay vì đoán thời gian.

## 10. Event trong WebSquare vẫn dựa trên event-driven programming

Button click, input change, DataList cell change, Submission done hay WFrame load đều là event. Framework đăng ký callback và gọi nó khi điều kiện xảy ra.

Mental model từ JavaScript vẫn áp dụng:

```text
user action/network result
        │
        ▼
event emitted
        │
        ▼
handler runs on JS execution context
        │
        ├─ read state
        ├─ mutate framework state
        ├─ schedule async work
        └─ return
```

Nếu handler gọi Submission asynchronous, handler không “đứng chờ” server. Response callback chạy sau. Vì vậy đoạn code đặt ngay sau `executeSubmission()` không được giả định rằng response đã có.

Đây là cùng một vấn đề async ordering được giải thích sâu ở [JavaScript Intermediate](../javascript/javascript_intermediate.md), chỉ khác object phát event là WebSquare runtime.

## 11. State nằm ở đâu?

Một màn hình enterprise có thể có ít nhất bốn loại state:

**Component state**: value, selected index, disabled/readOnly, visible state của UI component.

**DataCollection state**: dữ liệu business phía client, ví dụ search condition, danh sách user, row status.

**Page state**: biến trong `scwin`, flag loading, current mode, temporary context.

**Server state**: database, session, workflow status thật.

Bug thường xuất hiện khi một giá trị tồn tại ở nhiều nơi nhưng không có source of truth rõ ràng. Ví dụ developer giữ `selectedUserId` trong `scwin`, đồng thời trong hidden Input và trong DataMap. Ba bản sao có thể lệch nhau.

Nguyên tắc production: chọn source of truth theo mục đích. Dữ liệu cần submit nên sống trong DataCollection phù hợp. UI component nên phản ánh model qua binding khi có thể. Biến `scwin` phù hợp cho transient orchestration state, không nên biến thành một database thu nhỏ.

## 12. Binding thay đổi cách reasoning

Nếu Input được bind với DataMap, gọi `inputName.setValue(...)` có thể dẫn đến model update theo binding contract, và model update cũng có thể phản ánh ngược ra UI. Vì vậy khi debug, không chỉ nhìn component.

Hãy hỏi:

```text
Input này có bind DataMap không?
Grid này bind DataList nào?
Thay đổi đang xảy ra ở UI, model hay cả hai?
Event nào được phát khi binding cập nhật?
```

Chapter 02 đi sâu vấn đề này.

## 13. Error taxonomy: phân loại trước khi sửa

Một lỗi “bấm Search không ra dữ liệu” có thể thuộc nhiều nhóm hoàn toàn khác nhau:

```text
UI event không fire
→ handler sai tên / disabled / overlay

handler fire nhưng validation return
→ page logic

Submission không chạy
→ object/scope/config

request đi nhưng 4xx/5xx
→ endpoint/auth/server

response 200 nhưng target rỗng
→ response schema/mapping

DataList có data nhưng Grid rỗng
→ binding/grid rendering/filter
```

Chẩn đoán tốt là đi theo pipeline và thu evidence ở từng boundary, không sửa ngẫu nhiên từng API.

## 14. Senior note: abstraction leak là bình thường, nhưng phải biết lúc nào xảy ra

Framework cố che DOM, AJAX, serialization và frame management để developer làm việc ở mức abstraction cao hơn. Nhưng abstraction không bao giờ kín hoàn toàn. Khi có performance issue, security issue hay browser-specific bug, bạn phải đi xuống tầng thấp hơn.

Một senior WebSquare developer cần di chuyển được giữa ba mức:

```text
business screen
↕
WebSquare abstraction
↕
JavaScript / browser / HTTP / DOM
```

Chỉ biết tầng trên thì debug khó. Chỉ biết tầng dưới thì dễ chống lại framework và tạo code fragile. Kỹ năng quan trọng là biết **khi nào nên ở trong public abstraction, khi nào cần quan sát internals, và khi nào tuyệt đối không phụ thuộc internals**.

## 15. Bài tập reasoning

Giả sử một page có `inputName`, `dmUser`, `sbmSaveUser` và nút Save. `inputName` bind với `dmUser.name`. Khi người dùng nhập tên và bấm Save, server đôi lúc nhận tên cũ.

Đừng sửa ngay. Hãy xây giả thuyết theo thứ tự:

1. Giá trị hiển thị của Input có khác actual value do format/commit timing không?
2. Binding có commit trước event click không?
3. Submission reference lấy từ đúng DataMap không?
4. Có code khác ghi đè `dmUser.name` trước submit không?
5. Có duplicate/racing submission không?
6. Request payload trong Network tab thực tế chứa giá trị nào?

Bước 6 rất quan trọng. Nếu payload đã đúng mà server vẫn lưu sai, lỗi không còn nằm ở WebSquare UI. Nếu payload sai, tiếp tục truy ngược model và event ordering. Đây là cách debug theo evidence thay vì theo cảm giác.

## 16. Kết nối sang chapter tiếp theo

Sau chapter này, bạn nên giải thích được vì sao XML chỉ là authoring source, vì sao component object không nên đồng nhất với DOM, `scwin` giải quyết collision gì, `$p` cần Scope context ra sao, và tại sao state duplication là nguồn bug lớn.

Tiếp theo: [02 — Components, Events & Data Binding](02_components_events_binding.md).
