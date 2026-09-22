# 04 — Scope, WFrame, Popup & SPA

## 1. Vì sao WebSquare cần Scope?

Một enterprise application hiếm khi chỉ có một page độc lập. Nó có shell, menu, tab, popup, content frame và nhiều màn hình có thể mở đồng thời. Nếu mọi component ID và function đều sống ở global namespace, hai page cùng có `input1` hoặc `scwin.search` sẽ collision.

WebSquare giải quyết bằng **Scope (유효 범위 / phạm vi hiệu lực)**. Mỗi page được load trong cấu trúc WFrame có thể có một scope riêng. Component và script của page đó được resolve trong scope tương ứng.

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

Điều này giống module instance hơn là một object global duy nhất. Khi debugging ở console, đừng hỏi “`scwin` có function này không?” trước khi xác định expression đang resolve scope nào.

## 3. `$p` là page-aware utility

WebSquare cho phép dùng `$p` như utility gắn với scope hiện tại. Điều này giải quyết vấn đề context: cùng một lệnh `parent()` từ hai page con khác nhau phải trả về hai parent khác nhau.

Các API quan trọng về reasoning gồm:

```javascript
$p.parent();
$p.top();
$p.main();
```

Ngoài ra WFrame/TabControl có `getWindow()` để lấy Scope object của content tương ứng. Đừng học các API này như synonym; chúng biểu diễn quan hệ khác nhau trong page graph.

## 4. `parent()`: đi một boundary lên

`$p.parent()` trả scope của page cha theo frame relationship.

```javascript
$p.parent().scwin.refreshList();
```

Cách này tốt hơn truy cập thẳng component parent:

```javascript
$p.parent().grdUser.setCellData(...); // coupling cao
```

Parent function là contract. Parent component ID là implementation detail. Nếu code có chain `parent().parent().parent()`, đó là design smell vì page đang biết quá nhiều về nesting topology.

## 5. `top()` và `main()` không phải lúc nào cũng đồng nghĩa

Không nên chọn `top()` chỉ vì “nó chắc tìm được”. Đi thẳng lên top làm page con phụ thuộc application shell và khó reuse.

Rule reasoning:

```text
Nếu cần parent trực tiếp → parent()
Nếu cần content của frame/tab cụ thể → getWindow() trên owner component
Nếu cần app shell thật sự → main()/top() sau khi hiểu topology và scopeInherit
```

Điểm đặc biệt quan trọng là behavior của `$p.main()` có thể thay đổi theo `scopeInherit`. Vì vậy không thể định nghĩa `main()` chỉ bằng một câu “luôn trả main page” rồi áp dụng cho mọi WFrame.

## 6. `getWindow()`: tìm đúng scope thay vì đoán đường đi

WFrame có `getWindow()` trả Scope object của page đang nằm trong WFrame. TabControl cũng có `getWindow(tabId/tabIndex)` cho tab tương ứng ở các build hỗ trợ.

Conceptual example:

```javascript
var detailScope = wframeDetail.getWindow();
detailScope.scwin.loadUser(userId);
```

Mental model là **owner component → current child Scope**. Khi content dynamic, object này gắn với instance hiện tại chứ không phải tên page vĩnh viễn.

## 7. Strict boundary và lý do nên tránh implicit cross-scope lookup

Nếu runtime/config cho phép component ở scope khác được tìm thấy implicit, code có thể “vô tình chạy” đến khi page khác có cùng ID hoặc topology đổi. Boundary rõ làm dependency lộ sớm hơn.

Tư duy tương tự strict mode/type checking: hạn chế tiện lợi mơ hồ để đổi lấy predictability.

## 8. WFrame là composition primitive, không chỉ iframe đẹp hơn

WFrame cho phép load page source vào một vùng của page và kết hợp với Scope. Nó giải quyết composition, isolation và navigation/reuse. `src` hoặc `setSrc()` thay content mà không cần reload toàn WebSquare engine.

Do đó WFrame là architecture boundary, không chỉ layout component.

## 9. `setSrc()` và lifecycle

Khi gọi:

```javascript
wframeDetail.setSrc("/user/detail.xml", options);
```

page mới không xuất hiện đồng bộ như gán một object local. Engine phải resolve/load artifact, tạo Scope/component/binding và chạy lifecycle.

Sai pattern:

```javascript
wframeDetail.setSrc("/user/detail.xml");
var value = wframeDetail.getWindow().inputUserId.getValue();
```

Nếu page chưa ready, object chưa tồn tại. Dùng event/callback lifecycle phù hợp với component/build thay vì delay bằng `setTimeout(500)`.

## 10. Parameter passing bằng `dataObject`

WebSquare hỗ trợ `dataObject` khi tạo WFrame, popup, tab hoặc WindowContainer. Page nhận dữ liệu bằng `$p.getParameter(...)`.

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

Điểm quan trọng: parameter là **boundary data**, không phải đường tắt để chia sẻ toàn bộ object graph của page cha.

## 11. Boundary data nên là plain data

Function, DOM node, component instance, `window` và object graph có circular/reference semantics phức tạp là payload kém cho frame boundary. Chúng làm ownership và lifetime mơ hồ, đồng thời có thể giữ reference sang page đã đóng.

Guide SP5 còn cảnh báo khi gọi function qua Frame không nên gán trực tiếp object không phải String/JSON-like boundary object sang Frame khác theo cách tạo reference lâu dài, vì một số browser có thể phát sinh memory leak. Ý nghĩa architecture rộng hơn là: **truyền giá trị, không chia sẻ internals**.

```text
Tốt: { userId, mode, filters }
Xấu: { gridInstance, window, childScope, callbackClosure }
```

## 12. Callback bằng string/eval là legacy smell

Một số codebase truyền tên callback dưới dạng string rồi page con `eval` hoặc resolve ngược parent. Pattern này có rủi ro security, refactorability và static reasoning.

Nếu project convention bắt buộc dùng, giới hạn callback vào allowlist nội bộ, không eval string từ server/user. Nếu có thể refactor, ưu tiên explicit parent API hoặc event/result contract.

## 13. Popup là một boundary tương tự page con

`$p.openPopup()` có thể mở page với options và parameter. Hãy coi popup như một module có input/output contract.

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

Parent nhận result và tự quyết định update model nào. Rule: **popup nên trả kết quả, không nên điều khiển internals của parent nếu không cần**.

## 15. Chọn popup type theo boundary thật

SP5 guide phân biệt `wframePopup`, `iframePopup` và `browserPopup`, trong đó `wframePopup` được khuyến nghị cho phần lớn màn hình WebSquare vì hỗ trợ Scope và nằm trong runtime composition của application.

`iframePopup` hợp lý hơn khi cần isolation của IFrame, ví dụ tích hợp external domain/solution. `browserPopup` tạo native browser window/process boundary và chỉ nên dùng khi requirement thực sự cần cửa sổ riêng.

Đừng chọn IFrame/browser popup chỉ vì code legacy đã quen `window.parent` hoặc vì nó “dễ tách”. Isolation mạnh hơn cũng kéo theo communication, lifecycle, security và debugging cost lớn hơn.

## 16. TabControl và WindowContainer cũng tạo page topology

Tab/Window container thường chứa nhiều page. Khi mỗi tab/window là WFrame/Scope, cùng một screen có thể tồn tại nhiều instance.

Điều này làm global mutable state nguy hiểm. Nếu `window.currentUserId` được dùng chung cho mọi tab, tab B có thể ghi đè tab A. Scope-local state trong `scwin` hoặc DataCollection của page instance an toàn hơn.

## 17. SPA trong WebSquare

Single Page Application (SPA / 단일 페이지 애플리케이션) ở đây không nhất thiết giống React Router. Ý tưởng chính là **engine shell được giữ lại**, còn content page được thay trong frame/container để tránh reload toàn engine.

```text
websquare engine shell stays alive
        │
        ├─ menu/common state
        ├─ shared resources
        └─ WFrame/tab/window content changes
```

## 18. SPA tạo lifetime dài hơn — memory leak trở nên quan trọng

Trong full reload, browser giải phóng phần lớn page state khi navigation. Trong SPA, shell có thể sống hàng giờ. Nếu page đăng ký timer, global event listener hoặc giữ reference sang object đã đóng mà không cleanup, memory tăng dần.

```text
setInterval không clear
window/document listener không unbind
cache global giữ page scope
closure giữ large DataList
popup/frame đóng nhưng reference vẫn tồn tại
```

## 19. `scopeInherit`: phải hiểu theo hai trục độc lập

SP5 định nghĩa `scopeInherit` không chỉ bằng câu “child inherit parent”. Có hai câu hỏi độc lập:

```text
A. Child có tự động resolve object/component của parent như local không?
B. $p.main() từ child trỏ về parent WFrame area hay top page?
```

Với các option phổ biến:

| `scopeInherit` | Tự động tham chiếu object parent | `$p.main()` |
|---|---|---|
| `none` | Không | top page |
| `api` | Không | parent WFrame area |
| `component` | Có | top page |
| `all` | Có | parent WFrame area |

`none` là default trong guide SP5. Bảng này quan trọng vì `api` và `component` cố ý tách hai trục. Nếu chỉ nhớ “all = inherit, none = không” thì bạn chưa hiểu feature.

## 20. `recursive` là evolution mới và không nên giả định mọi engine có

Release note SP5 engine 2026 bổ sung `scopeInherit="recursive"`. Option này cho phép tự động tham chiếu object qua các ancestor WFrame cũng cấu hình `recursive`, trong khi `$p.main()` vẫn đi về top page. `all` và `recursive` vì vậy không phải synonym.

Consequence production: một codebase chạy trên engine trước feature này không thể dùng `recursive` chỉ vì Studio/documentation mới có. Đây là ví dụ điển hình của nguyên tắc **engine build > tên generation**.

Khi upgrade, regression test phải có nested topology thật:

```text
Shell
└─ WFrame A
   └─ WFrame B
      └─ WFrame C
```

và xác nhận object resolution cùng `$p.main()` ở từng level.

## 21. Scope inheritance là convenience có trade-off

`scopeInherit="all"` hoặc `recursive` có thể giảm code navigation nhưng cũng làm dependency ẩn. Child gọi `inputParent` như local object thì source file không cho người đọc biết object đó thuộc parent.

Với code mới, ưu tiên explicit page contract. Dùng inheritance khi project có reason rõ như migration, common shell convention hoặc composition pattern được kiểm soát; đừng dùng để “chữa” mọi lỗi object-not-found.

## 22. `scopeInherit` không chỉ thuộc WFrame tĩnh

Các SP5 build mới đưa cùng mental model inheritance vào WFrame popup, TabControl contents và WindowContainer WFrame. Vì vậy topology có thể đổi behavior tùy **cách page được host**.

Một screen chạy đúng trong WFrame thường nhưng fail khi mở trong popup/tab có thể không phải bug của screen logic; host options có thể tạo Scope relationship khác.

Đây là lý do test reusable screen ở nhiều host topology thay vì chỉ test một đường navigation.

## 23. Lifecycle ordering giữa parent và child

Một parent page có thể load WFrame; child lại load DataCollection/Submission; parent muốn gọi child sau khi sẵn sàng. Đây là distributed lifecycle trong cùng browser.

```text
parent script parsed
≠ parent rendered
≠ child source requested
≠ child scope ready
≠ child UI ready
≠ child data ready
```

Nếu parent cần child “ready with data”, hãy định nghĩa ready contract ở đúng mức, không chỉ frame-load nếu data load còn asynchronous.

## 24. `onpageload` chỉ chứng minh page lifecycle đã đến một mốc

SP5 guide mô tả `scwin.onpageload` là event chạy sau page loading. Điều đó hữu ích nhưng không có nghĩa mọi business data async đã sẵn sàng. Nếu `onpageload` tự execute Submission, callback của Submission vẫn là một readiness stage khác.

Do đó nên đặt tên state rõ:

```text
pageReady
referenceDataReady
businessDataReady
interactiveReady
```

thay vì một boolean `loaded` dùng cho mọi thứ.

## 25. Dynamic page instance và stale reference

Giả sử:

```javascript
var detail = wframeDetail.getWindow();
```

Sau đó `wframeDetail.setSrc()` chuyển sang page khác. Biến `detail` cũ có thể trỏ Scope không còn đại diện current page.

Nếu topology dynamic, resolve Scope gần thời điểm sử dụng thay vì cache vô thời hạn. Nếu buộc cache, cache phải có invalidation theo lifecycle.

## 26. Cross-scope call là synchronous hay asynchronous?

Nếu hai Scope đã tồn tại trong cùng JavaScript runtime và bạn gọi trực tiếp function, call bản thân nó thường synchronous như JavaScript bình thường. Nhưng function bên kia có thể bắt đầu Submission hoặc frame load async.

```javascript
$p.parent().scwin.refresh();
// refresh() có thể chỉ schedule network call rồi return ngay
```

Đừng nhầm “function call synchronous” với “business operation synchronous”.

## 27. Error handling qua frame boundary

Nếu child gọi parent function và parent throw exception ngay, exception có thể bubble theo JavaScript call path. Nhưng network/lifecycle error xảy ra sau đó không thể catch bằng outer `try/catch` quanh function call.

Async failure phải được xử lý ở callback/event tương ứng.

## 28. Debug Scope bằng DOM element

SP5 có debug utility như `$p.debug.getScope($0)` và `$p.debug.getFrame($0)` ở các build tương ứng. Đây là công cụ hữu ích khi nhìn một element nhưng không biết nó thuộc WFrame nào.

```text
Inspect element
→ $0
→ resolve WebSquare scope/frame
→ inspect scwin/component/DataCollection trong đúng scope
```

Đừng đoán bằng physical DOM id.

## 29. Anti-pattern: singleton common object biết mọi screen

Một số project tạo `com`/`gcm` global utility rồi dần biến nó thành object biết ID và behavior của mọi page. Common utility hợp lý cho logging, message, date formatting, submission wrapper hoặc auth context. Nhưng screen-specific logic không nên chảy hết vào global god object.

Common module nên phụ thuộc abstraction ổn định; screen/domain logic ở screen/domain module.

## 30. Anti-pattern: dùng `top()` để “chữa” lỗi scope

Khi component local không tìm thấy, developer có thể thử `$p.top().someComponent`. Nếu chạy, bug tạm biến mất nhưng dependency bị đẩy lên app shell.

Trước khi dùng `top()`, trả lời object thực sự thuộc page nào, vì sao current page cần nó và có public function/data contract thay cho component access không.

## 31. Thiết kế page contract như function contract

Hãy coi một page con như function:

```text
Input: parameter/dataObject
Internal state: scwin + DataCollection
Output: result/event/public API
Side effects: Submission / navigation
Lifetime: create → ready stages → dispose
```

Một page contract tốt giúp screen reuse được ở tab, popup hoặc WFrame khác mà không phụ thuộc parent structure cụ thể.

## 32. Ví dụ: Search → Detail popup → Refresh

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

## 33. Production checklist cho Scope architecture

Trước khi merge screen mới, kiểm tra page có truy cập component ngoài scope trực tiếp không; có chain parent dài không; `scopeInherit` có làm dependency ẩn không; host popup/tab/window có cùng topology assumption không; parameter có chứa object/reference khó quản lifetime không; global mutable state có bị dùng chung giữa nhiều instance không; frame load có race với code gọi child không; và SPA page có cleanup timer/listener/resource không.

## 34. Kết nối

Sau khi hiểu Scope, bạn có thể reasoning GridView/CRUD trong screen lớn mà không nhầm data model và page instance. Tiếp theo: [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md).

Để hiểu object-ready/render-ready/preload sâu hơn, đọc [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md). Để regression-test nested WFrame, popup và host topology, đọc [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md).