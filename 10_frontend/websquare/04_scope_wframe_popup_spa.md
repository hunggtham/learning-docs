# 04 — Scope, WFrame, Popup & SPA

## 1. Vì sao WebSquare cần Scope?

Một enterprise application hiếm khi chỉ có một page độc lập. Nó có shell, menu, tab, popup, content frame và nhiều màn hình có thể mở đồng thời. Nếu mọi component ID và function đều sống ở global namespace, hai page cùng có `input1` hoặc `scwin.search` sẽ collision.

WebSquare giải quyết bằng **Scope (유효 범위 / phạm vi hiệu lực)**. Mỗi page được load trong cấu trúc WFrame có thể có một scope riêng. Component và script của page đó được resolve trong scope tương ứng.

Mental model:

```text
main page scope
├─ wframeA scope
│  ├─ inputName
│  └─ scwin.search
└─ wframeB scope
   ├─ inputName
   └─ scwin.search
```

Hai `inputName` có cùng logical ID nhưng không phải cùng object.

## 2. `scwin` không phải global singleton của toàn app

Trong project dùng Scope, `scwin` là scope variable của **page hiện tại**. Hai WFrame khác nhau có hai `scwin` khác nhau dù code source đều dùng tên `scwin`.

Điều này giống module instance hơn là một object global duy nhất.

Khi debugging ở console, đừng hỏi “`scwin` có function này không?” trước khi xác định console expression đang resolve scope nào.

## 3. `$p` là page-aware utility

WebSquare cho phép dùng `$p` như shortcut của utility gắn với scope hiện tại. Điều này giải quyết vấn đề context: cùng một lệnh `parent()` từ hai page con khác nhau phải trả về hai parent khác nhau.

Các API quan trọng về reasoning gồm:

```javascript
$p.parent();
$p.top();
$p.main();
$p.getWindow(...);
```

Đừng học chúng như bốn synonym. Chúng biểu diễn bốn quan hệ navigation khác nhau trong page graph.

## 4. `parent()`: đi một boundary lên

`$p.parent()` trả scope của page cha theo frame relationship.

Ví dụ page con muốn gọi public function của parent:

```javascript
$p.parent().scwin.refreshList();
```

Cách này tốt hơn truy cập thẳng component parent:

```javascript
$p.parent().grdUser.setCellData(...); // coupling cao
```

Parent function là contract. Parent component ID là implementation detail.

Nếu code có:

```javascript
$p.parent().$p.parent().$p.parent()...
```

đó là design smell. Page đang biết quá nhiều về nesting topology. Một layout refactor có thể phá toàn bộ chain.

## 5. `top()` và `main()` khác nhau vì app có thể có nhiều boundary

`$p.top()` nhắm tới scope cấp cao nhất theo WebSquare navigation semantics. `$p.main()` nhắm tới main scope trong phạm vi page/frame hiện tại và có thể khác `top()` khi có IFrame hoặc container boundary.

Không nên chọn `top()` chỉ vì “nó chắc tìm được”. Đi thẳng lên top làm page con phụ thuộc application shell và khó reuse.

Rule:

```text
Nếu cần parent trực tiếp → parent()
Nếu cần page cụ thể → getWindow()/container API
Nếu cần app shell thật sự → main()/top() sau khi hiểu topology
```

## 6. `getWindow()`: tìm đúng scope thay vì đoán đường đi

WFrame và container API cho phép lấy window/scope chứa page cụ thể. Khi biết identity của frame, resolve trực tiếp thường rõ hơn chain `parent().parent()`.

Conceptual example:

```javascript
var detailScope = $p.getWindow("detailFrame");
detailScope.scwin.loadUser(userId);
```

Signature thực tế có thể phụ thuộc component/build, nên kiểm tra API reference của object đang dùng. Mental model không đổi: **resolve target scope bằng identity rõ ràng**.

## 7. Strict mode và lý do nên tránh implicit cross-scope lookup

Nếu runtime cho phép component ở scope khác được tìm thấy một cách implicit, code có thể “vô tình chạy” đến khi page khác có cùng ID hoặc topology đổi.

Strict Scope configuration làm dependency lộ rõ hơn. Đây là lợi ích architecture: lỗi xuất hiện sớm thay vì silently resolve nhầm object.

Tư duy tương tự strict mode/type checking: hạn chế tiện lợi mơ hồ để đổi lấy predictability.

## 8. WFrame là composition primitive, không chỉ iframe đẹp hơn

WFrame cho phép load page source vào một vùng của page và kết hợp với Scope. Trong các dòng WebSquare mới hơn SP3, WFrame là primitive quan trọng cho SPA-style composition thay cho cách cũ dựa nhiều vào IFrame.

WFrame giải quyết ba vấn đề:

**composition** — nhúng page con vào shell/page cha.

**isolation** — page con có Scope riêng.

**navigation/reuse** — thay `src` để chuyển content mà không cần reload toàn engine.

Do đó WFrame là architecture boundary, không chỉ là layout component.

## 9. `setSrc()` và lifecycle

Khi gọi:

```javascript
wframeDetail.setSrc("/user/detail.xml", options);
```

page mới không xuất hiện đồng bộ như gán một object local. Engine phải load artifact, tạo scope, component, binding và chạy lifecycle.

Sai pattern:

```javascript
wframeDetail.setSrc("/user/detail.xml");
var value = wframeDetail.getWindow().inputUserId.getValue();
```

Nếu page chưa load xong, object chưa tồn tại.

Đúng approach là dùng event/callback load contract phù hợp với component/build.

## 10. Parameter passing bằng `dataObject`

WebSquare hỗ trợ truyền data object khi tạo WFrame/popup. Dữ liệu có thể được nhận bằng `$p.getParameter(...)`.

Conceptual example:

```javascript
var dataObject = {
    type: "json",
    name: "userParam",
    data: {
        userId: "U1001",
        mode: "EDIT"
    }
};

wframeDetail.setSrc("/user/detail.xml", {
    dataObject: dataObject
});
```

Page con:

```javascript
var param = $p.getParameter("userParam");
console.log(param.userId);
```

Điểm quan trọng: parameter object là **boundary data**, nên ưu tiên JSON-serializable data đơn giản.

## 11. Clone semantics và giới hạn serialization

Trong WFrame parameter model, data có thể được copy qua `JSON.stringify`/`JSON.parse` semantics. Hệ quả:

Function không serialize như data bình thường.

Circular reference không serialize được.

Object đặc biệt như `window`, DOM node, component instance không phải payload tốt.

Prototype/class identity có thể mất.

Vì vậy parameter contract nên gồm primitive, array và plain object.

```text
Tốt: { userId, mode, filters }
Xấu: { window, gridInstance, callbackFunction, circularObject }
```

## 12. Callback bằng string/eval là legacy smell

Một số codebase truyền tên callback dưới dạng string rồi page con `eval` hoặc resolve ngược parent. Pattern này tồn tại trong enterprise legacy nhưng có rủi ro security, refactorability và static reasoning.

Nếu project convention bắt buộc dùng, giới hạn input callback vào allowlist nội bộ, không eval string từ server/user. Nếu có thể refactor, ưu tiên explicit parent API hoặc event/message contract.

## 13. Popup là một boundary tương tự page con

`$p.openPopup()` có thể mở page với options và parameter. Hãy coi popup như một module có input/output contract.

Parent mở popup:

```javascript
var options = {
    id: "userDetailPopup",
    modal: true,
    width: "720px",
    height: "560px",
    dataObject: {
        type: "json",
        name: "param",
        data: {
            userId: selectedUserId
        }
    }
};

$p.openPopup("/user/detail.xml", options);
```

Popup không nên tự mò khắp parent để lấy 20 component. Nhận input cần thiết qua parameter sẽ giảm coupling.

## 14. Popup result contract

Một popup chọn user có thể trả:

```javascript
{
    userId: "U1001",
    userName: "Kim"
}
```

Parent nhận result và tự quyết định update model nào. Đây là contract tốt hơn popup gọi thẳng:

```javascript
$p.parent().dmSearch.setJSON(...);
$p.parent().inputName.setValue(...);
$p.parent().grdUser...;
```

Rule: **popup nên trả kết quả, không nên điều khiển internals của parent nếu không cần**.

## 15. TabControl và WindowContainer cũng tạo page topology

Tab/Window container thường chứa nhiều page. Khi mỗi tab là WFrame/Scope, cùng một screen có thể tồn tại nhiều instance.

Điều này làm global mutable state nguy hiểm. Nếu `window.currentUserId` được dùng chung cho mọi tab, tab B có thể ghi đè tab A.

Scope-local state trong `scwin` hoặc DataCollection của page instance an toàn hơn.

## 16. SPA trong WebSquare

Single Page Application (SPA / 단일 페이지 애플리케이션) ở đây không nhất thiết giống React Router. Ý tưởng chính là **engine shell được giữ lại**, còn content page được thay trong frame/body để tránh reload toàn engine.

WebSquare đời cũ có thể dùng IFrame và pooling/reuse phức tạp hơn. Dòng SP3+ hỗ trợ WFrame/Scope để navigation đơn giản hơn.

Mental model:

```text
websquare engine shell stays alive
        │
        ├─ menu state
        ├─ common resources
        └─ current WFrame content changes
```

## 17. SPA tạo lifetime dài hơn — memory leak trở nên quan trọng

Trong multi-page full reload, browser giải phóng phần lớn page state khi navigation. Trong SPA, shell có thể sống hàng giờ. Nếu page đăng ký timer, global event listener hoặc giữ reference sang object đã đóng mà không cleanup, memory tăng dần.

Các nguồn leak thường gặp:

```text
setInterval không clear
window/document listener không unbind
cache global giữ page scope
closure giữ large DataList
popup/frame đóng nhưng reference vẫn tồn tại
```

Performance chapter sẽ đi sâu hơn.

## 18. Scope inheritance là convenience có trade-off

Một số WFrame configuration cho phép scope con inherit component/API từ parent theo mức khác nhau. Điều này có thể giúp migration code cũ nhưng làm boundary mờ.

Nếu child có thể gọi parent component như local object, developer dễ quên dependency thật nằm ở đâu. Với code mới, ưu tiên explicit boundary trừ khi project architecture có convention rõ.

## 19. Lifecycle ordering giữa parent và child

Một parent page có thể load WFrame; child lại load DataCollection/Submission; parent muốn gọi child sau khi sẵn sàng. Đây là distributed lifecycle trong cùng browser.

Đừng suy bằng source order.

```text
parent script parsed
≠ parent rendered
≠ child source requested
≠ child scope ready
≠ child data loaded
```

Nếu parent cần child “ready with data”, hãy định nghĩa ready contract ở đúng mức, không chỉ frame-load nếu data load còn asynchronous.

## 20. Dynamic page instance và stale reference

Giả sử:

```javascript
var detail = $p.getWindow("detailFrame");
```

Sau đó `detailFrame.setSrc()` chuyển sang page khác. Biến `detail` cũ có thể trỏ object/scope không còn đại diện current page.

Nếu topology dynamic, resolve scope gần thời điểm sử dụng thay vì cache vô thời hạn.

## 21. Cross-scope call là synchronous hay asynchronous?

Nếu hai scope đã tồn tại trong cùng JavaScript runtime và bạn gọi trực tiếp function, call bản thân nó thường synchronous như JavaScript bình thường.

Nhưng function bên kia có thể bắt đầu Submission hoặc load WFrame async. Đừng nhầm “function call synchronous” với “business operation synchronous”.

```javascript
$p.parent().scwin.refresh();
// refresh() có thể chỉ schedule network call rồi return ngay
```

## 22. Error handling qua frame boundary

Nếu child gọi parent function và parent throw exception, exception có thể bubble như JavaScript call bình thường tùy call path. Nhưng network/lifecycle error xảy ra sau đó không thể catch bằng outer `try/catch` quanh function call.

Sai:

```javascript
try {
    $p.parent().scwin.save();
} catch (e) {
    // không bắt được lỗi HTTP xảy ra 2 giây sau
}
```

Async failure phải được xử lý ở callback/promise/event tương ứng.

## 23. Debug Scope bằng DOM element

WebSquare cung cấp debug utility để tìm Scope/Frame từ DOM element ở một số SP5 build, ví dụ `$p.debug.getScope($0)` hoặc `$p.debug.getFrame($0)` khi dùng browser DevTools.

Đây là công cụ rất hữu ích khi nhìn một component trên màn hình nhưng không biết nó thuộc WFrame nào.

Workflow:

```text
Inspect element
→ $0
→ resolve WebSquare scope/frame
→ inspect scwin/component/DataCollection trong đúng scope
```

Đừng đoán bằng tên DOM id.

## 24. Anti-pattern: singleton common object biết mọi screen

Một số project tạo `com`/`gcm` global utility rồi dần biến nó thành object biết ID và behavior của mọi page. Common utility hợp lý cho logging, message, date formatting, submission wrapper hoặc auth context. Nhưng nếu nó có function `setUserGridOnScreenA()` và `openScreenBAndModifyScreenC()`, common layer đã trở thành god object.

Common module nên phụ thuộc vào abstraction ổn định; screen-specific logic ở screen/domain module.

## 25. Anti-pattern: dùng `top()` để “chữa” lỗi scope

Khi component local không tìm thấy, developer có thể thử `$p.top().someComponent`. Nếu chạy, bug tạm biến mất nhưng dependency bị đẩy lên app shell.

Trước khi dùng `top()`, trả lời:

```text
Object này thực sự thuộc page nào?
Tại sao current page cần nó?
Có public function/data contract thay cho component access không?
```

## 26. Thiết kế page contract như function contract

Hãy coi một page con như function:

```text
Input: parameter/dataObject
Internal state: scwin + DataCollection
Output: callback/result/event
Side effects: Submission / navigation
```

Một page contract tốt giúp screen reuse được ở tab, popup hoặc WFrame khác mà không phụ thuộc parent structure cụ thể.

## 27. Ví dụ: Search → Detail popup → Refresh

Flow tốt:

```text
List page
  │ selected userId
  ▼
open Detail popup(userId)
  │
  ▼
Detail page loads user
  │ user edits + saves
  ▼
popup returns { changed: true, userId }
  │
  ▼
List page decides to re-query
```

Popup không cần biết GridView của parent tên gì. Parent không cần biết internal component của popup.

## 28. Production checklist cho Scope architecture

Trước khi merge screen mới, kiểm tra:

```text
Page có truy cập component ngoài scope trực tiếp không?
Có chain parent().parent() dài không?
Parameter có chứa object không serialize được không?
Có global mutable state dùng chung giữa nhiều page instance không?
Frame load có race với code gọi child không?
Popup có input/output contract rõ không?
SPA page có cleanup timer/listener/resource không?
```

## 29. Kết nối

Sau khi hiểu Scope, bạn có thể reasoning GridView/CRUD trong screen lớn mà không nhầm data model và page instance. Tiếp theo: [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md).
