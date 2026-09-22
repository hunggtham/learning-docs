# 07 — Legacy, Modern Evolution & Migration

## 1. Vì sao migration knowledge quan trọng với WebSquare

WebSquare thường xuất hiện trong hệ thống enterprise sống nhiều năm. Một project có thể chứa page được viết ở nhiều thời kỳ, common module đã tích lũy workaround cũ, API mới và cũ cùng tồn tại, và engine upgrade diễn ra chậm hơn application code.

Vì vậy “code mới nhất” không đủ. Developer cần đọc được cả code legacy và biết **behavior nào là historical constraint, behavior nào vẫn là invariant, và behavior nào chỉ còn vì chưa refactor**.

## 2. Đừng migrate syntax trước mental model

Một migration an toàn không bắt đầu bằng search/replace `$w` thành `$p` hay IFrame thành WFrame. Trước tiên phải hiểu page topology, state ownership và communication path hiện tại.

Với mỗi screen, lập bản đồ:

```text
entry page
frame/container tree
global variables
DataCollection
Submission
popup contract
cross-page calls
common utility dependency
browser-specific workaround
```

Sau đó mới quyết định refactor boundary.

## 3. Global-style page và Scope-style page

Code cũ có thể dựa mạnh vào global ID/function. Điều này chạy khi mỗi page độc lập hoặc IFrame tách global context.

Scope-style architecture đặt page behavior vào `scwin`, dùng WFrame Scope để tránh collision và `$p` cho page-aware utility.

Migration không chỉ là đổi tên function:

```text
global function
→ page-local function

global component lookup
→ scope-local component lookup

implicit cross-page dependency
→ explicit parent/window contract
```

Nếu chỉ thêm `scwin.` nhưng vẫn giữ global state và `top.someComponent`, isolation chưa thật sự đạt được.

## 4. `$w` và `$p`

Trong Scope model, `$p` được dùng như page-aware mapping cho utility vốn liên quan `$w`. Code legacy có thể còn `$w.*` ở global context.

Không nên blindly replace mọi `$w` bằng `$p`. Cần xác định function đó đang chạy ở page Scope nào và utility đó có page-relative semantics hay không.

Migration checklist:

```text
Call có cần current page context?
Code có chạy trong common global module?
Target object có nằm trong child/parent Scope?
Build hiện tại document API nào?
```

## 5. IFrame SPA → WFrame SPA

Các WebSquare đời cũ có thể dùng IFrame để isolate page và tái sử dụng engine/frame bằng mechanism như `spaInitCount`/`spaAuto`. Từ các dòng SP3+, WFrame + Scope cho phép SPA composition đơn giản hơn.

IFrame tạo browser context tương đối độc lập; WFrame Scope vẫn sống trong cùng broader runtime. Vì vậy migration ảnh hưởng:

```text
global variable isolation
window/top/parent semantics
CSS/resource sharing
memory lifecycle
cross-frame call
DOM access
```

Không thay IFrame bằng WFrame rồi giả định `window.parent` behavior giống hệt.

## 6. `window.parent` → WebSquare scope navigation

Legacy code có thể:

```javascript
window.parent.someFunction();
```

Trong WFrame Scope architecture, explicit WebSquare relation như `$p.parent()` phù hợp hơn vì nó hiểu page scope, không chỉ browser window hierarchy.

Migration tốt:

```javascript
$p.parent().scwin.someFunction();
```

Nhưng bước tiếp theo nên là giảm coupling bằng public parent function contract, không chỉ thay navigation primitive.

## 7. Inline DOM manipulation → component API

Code cũ thường chứa jQuery selector hoặc raw DOM vì component API thời đó thiếu feature hoặc team quen web development cũ.

Khi engine mới đã có public API, ưu tiên migrate về component contract.

Ví dụ:

```text
$('#someInternalInput').val(x)
→ inputComponent.setValue(x)
```

Không phải vì jQuery “xấu”, mà vì component API giữ framework state/binding/lifecycle đúng hơn và bền hơn khi renderer đổi.

## 8. jQuery support là compatibility, không nên là default mới

WebSquare có jQuery support ở nhiều dòng. Với code mới, nếu WebSquare API hoặc modern browser API đủ, không cần thêm jQuery chỉ vì project legacy có sẵn.

Tuy nhiên không nên xóa jQuery hàng loạt nếu plugin/common library phụ thuộc. Migration theo usage graph và test behavior.

## 9. Callback string và `eval`

Legacy popup/common module có thể truyền callback string:

```javascript
{
    callback: "$p.parent().scwin.onSelected"
}
```

rồi `eval` ở child.

Migration target tốt hơn:

```text
input data contract
→ child operation
→ result data contract
→ parent handler
```

Nếu platform API chỉ cho string ở một điểm, ít nhất giới hạn callback vào internal allowlist và tách nó khỏi arbitrary external data.

## 10. Synchronous Submission

Legacy code có thể dùng synchronous request vì dễ reasoning theo source order. Synchronous XHR-style communication block UI thread và không phù hợp web hiện đại.

Migration sang asynchronous đòi hỏi đổi control flow:

Legacy mental model:

```javascript
execute();
useResult();
```

Async model:

```text
execute
→ return
→ response callback
→ useResult
```

Không thể chỉ đổi `mode="asynchronous"` mà giữ code phía sau như cũ.

## 11. Common utility wrapper và abstraction debt

Project lâu năm thường có wrapper như:

```text
gfn_search
gfn_save
gfn_popup
gfn_message
gfn_grid...
```

Wrapper tốt khi chuẩn hóa logging, auth header, common error handling hoặc UX convention. Wrapper xấu khi che quá nhiều parameter, tự sửa DataCollection hoặc chứa exception cho từng screen.

Audit wrapper bằng câu hỏi:

```text
Nó giảm duplication thật hay chỉ đổi tên API?
Nó giữ abstraction ổn định không?
Nó có hidden side effect không?
Có hàng chục flag boolean không?
Screen mới có buộc hiểu internal wrapper mới dùng được không?
```

## 12. Magic config và historical workaround

Một config có thể tồn tại vì bug engine 8 năm trước. Trước khi giữ hoặc xóa, tìm evidence:

```text
comment/issue history
release note
engine build hiện tại
reproduction test
```

Không xóa workaround chỉ vì không hiểu. Cũng không giữ vĩnh viễn chỉ vì “hệ thống đang chạy”.

## 13. Engine build là dependency cần version control

WebSquare API docs được phát hành theo engine build. Một production issue có thể chỉ xuất hiện ở build cụ thể.

Repository/app documentation nên ghi:

```text
engine generation
SP/build version
Studio version nếu liên quan
known browser matrix
important config toggles
```

Đây là dependency inventory giống Java version hoặc Spring Boot version.

## 14. Release note phải đi cùng upgrade test

Khi upgrade engine:

```text
1. đọc release note từ current → target
2. liệt kê deprecated/changed behavior
3. chạy smoke test core screens
4. chạy regression cho Grid, popup, WFrame, Submission
5. đo performance/memory
6. test browser matrix
7. so sánh console warning/error
```

Upgrade UI engine không nên được coi là “thay vài JAR rồi xong”.

## 15. W-Pack artifact và deployment migration

Khi build pipeline thay đổi W-Pack/minify/obfuscation, cần verify:

```text
source → artifact mapping
cache busting
source map
resource path/context root
incremental build
CI packaging
rollback artifact
```

Một migration source thành công nhưng artifact stale vẫn thất bại production.

## 16. CSS migration

Renderer/version mới có thể thay internal DOM/class. CSS selector dựa sâu vào internal markup dễ vỡ.

Trước engine upgrade, search:

```text
#generated-id
very deep selectors
engine-internal class name
!important workaround
browser-specific hacks
```

Ưu tiên application-owned class và visual regression test.

## 17. Browser modernization

Project WebSquare lâu năm có thể chứa:

```text
IE branch
ActiveX integration
document.all
attachEvent
old polyfill
vendor CSS prefix workaround
```

Nếu browser policy đã bỏ IE, những branch này trở thành maintenance cost. Nhưng xóa theo test coverage, không theo cảm giác.

## 18. Security modernization

Legacy enterprise code thường cần audit:

```text
eval
innerHTML
unescaped server message
URL parameter injection
weak popup origin assumption
client-side authorization
old upload endpoint
sensitive console log
```

Engine upgrade không tự sửa application security pattern.

## 19. Data contract migration

Khi backend đổi XML → JSON hoặc field schema, tránh làm mỗi screen tự convert thủ công.

Tạo compatibility boundary ở data/service layer nếu project architecture cho phép. Mục tiêu là screen reasoning vẫn trên canonical domain model.

```text
legacy response
→ adapter
→ canonical DataCollection shape
→ screen
```

Adapter tạm phải có kế hoạch remove; nếu không, compatibility layer trở thành permanent complexity.

## 20. WebSquare5 SP5 và dòng 6.0/WebSquare AI

Tài liệu chính thức năm 2026 có cả WebSquare5 SP5 và API 6.0. Dòng 6.0 vẫn giữ nhiều concept quen thuộc như component object, `getValue/setValue`, DataMap và network utility, nhưng có API/reference generation riêng.

Không nên diễn giải “6.0” như chỉ đổi tên SP5. Khi project thực sự migrate, hãy diff API/property/event của các component critical bằng official reference đúng build.

Mental model trong library này được giữ ở mức bền hơn version:

```text
page/component abstraction
data model
scope
communication
frame composition
browser/runtime boundary
```

Các concept này giúp đọc cả code cũ và mới, dù API chi tiết thay đổi.

## 21. Strangler migration cho screen lớn

Một screen 5.000 dòng không nên rewrite một lần nếu không có test mạnh. Có thể migration dần:

```text
1. thêm observability/test
2. tách handler lớn thành function có tên
3. gom DataCollection contract
4. giảm direct parent component access
5. thay DOM hack bằng component API
6. chuyển async flow
7. bật stricter Scope/config
8. nâng engine
```

Mỗi bước giảm risk và tạo checkpoint rollback.

## 22. Characterization test trước refactor

Với legacy code khó hiểu, test behavior hiện tại trước khi sửa:

```text
Given condition A
When click Search
Then request payload X
And grid result Y
```

Đây là characterization test: ghi lại behavior thật, kể cả implementation xấu. Sau refactor, giữ business behavior trừ phần bug chủ đích sửa.

## 23. Migration anti-pattern: rewrite vì “code cũ xấu”

Full rewrite thường đánh mất hidden business rules nằm trong handler, common util và server contract.

Trước rewrite, inventory rule:

```text
validation
format
permission
special customer case
batch semantics
error handling
popup callback
legacy browser requirement
```

Nếu không liệt kê được, bạn chưa hiểu đủ để rewrite an toàn.

## 24. Migration anti-pattern: preserve mọi behavior vì sợ

Ngược lại, giữ tất cả historical behavior cũng nguy hiểm. Một workaround cho IE8 không nên dictate architecture năm 2026.

Phân loại:

```text
business invariant → preserve
platform constraint còn tồn tại → preserve
obsolete workaround → remove có test
accidental bug → fix có requirement
```

## 25. API inventory cho critical screen

Trước upgrade, lập bảng:

| Area | API/property đang dùng | Risk |
|---|---|---|
| Scope | `$p.parent`, `getWindow` | topology/lifecycle |
| Input | `getValue`, `setValue`, format | event/format behavior |
| DataList | row status, insert/delete, JSON | CRUD semantics |
| Submission | mode, ref/target, callbacks | async/network |
| GridView | edit, filter, Excel | rendering/performance |
| Popup/WFrame | dataObject, setSrc | serialization/lifecycle |

Sau đó tra đúng target build.

## 26. Deprecation strategy

Khi API deprecated:

```text
Không xóa ngay nếu production còn dùng.
Đánh dấu usage.
Xác định replacement và semantic difference.
Migrate screen nhỏ trước.
Đo regression.
Sau khi usage = 0 mới remove compatibility wrapper.
```

Deprecation không đồng nghĩa broken ngay, nhưng là debt có deadline.

## 27. Code review khi có cả legacy và modern style

Reviewer không nên yêu cầu mọi file cũ chuyển modern style trong PR feature nhỏ. Scope change quá lớn tăng regression risk.

Thay vào đó:

```text
không thêm legacy pattern mới
refactor phần chạm vào nếu đủ test
ghi debt có boundary rõ
migrate theo module/screen
```

## 28. Checklist đọc một file WebSquare lạ

Khi mở một page chưa từng thấy:

```text
1. Page nằm trong frame nào?
2. Có Scope/scwin không?
3. DataMap/DataList nào là source of truth?
4. Submission nào query/save?
5. Grid bind model nào?
6. Event entry point là gì?
7. Cross-page dependency ở đâu?
8. Common util nào có side effect?
9. API nào legacy/version-sensitive?
10. Có DOM/jQuery hack không?
```

Trả lời mười câu này trước khi sửa sâu.

## 29. Checklist migration production

```text
Engine/build target được ghi rõ
Release notes reviewed
Config diff reviewed
Critical API inventory done
Async behavior tested
Scope/frame navigation tested
Grid CRUD regression done
Popup parameter/result tested
Large data performance measured
Memory leak soak test done
Security regression reviewed
Cache/W-Pack deployment verified
Rollback plan available
```

## 30. Kết thúc track

Sau bảy chapter, mục tiêu không phải là bạn nhớ mọi property của mọi component. API reference tồn tại cho việc đó. Mục tiêu là bạn có một mental model đủ mạnh để mở một screen WebSquare lạ và trả lời:

```text
Page được tạo và chạy thế nào?
State nằm ở đâu?
Scope nào sở hữu object?
Event nào kích hoạt flow?
Data đi qua DataCollection/Submission ra sao?
Grid đang hiển thị model nào?
Failure có thể nằm ở boundary nào?
Evidence nào kiểm chứng giả thuyết?
Code này là modern contract hay legacy workaround?
```

Hãy dùng [Glossary & Coverage Audit](GLOSSARY_AND_COVERAGE.md) để tự kiểm tra coverage và quay lại chapter còn yếu.
