# 03 — DataCollection & Submission

## 1. Tách dữ liệu khỏi component

Một trong những ý tưởng quan trọng nhất của WebSquare là không bắt mọi component tự giữ business data. Framework cung cấp **DataCollection**, một nhóm object dữ liệu được tạo trong browser memory để màn hình dùng chung.

Ba loại thường gặp là:

`DataMap` — dữ liệu dạng một record hoặc key/value.

`DataList` — dữ liệu nhiều dòng, gần với table/list.

`LinkedDataList` — một view dẫn xuất từ DataList, thường dùng cho filter/sort mà không cần coi kết quả đó là một business dataset hoàn toàn mới.

Mental model:

```text
server data
    ↓
DataCollection
    ↓
binding / script
    ↓
components
```

Nếu component chỉ là view, code nghiệp vụ nên ưu tiên thao tác model thay vì cố đọc từng cell UI để dựng lại dữ liệu.

## 2. DataMap: record có schema

Một `DataMap` thường có key definition và value tương ứng. Nó phù hợp cho điều kiện tìm kiếm, form chi tiết hoặc request parameter dạng một object.

Ví dụ conceptual:

```text
dmSearch
 ├─ userId
 ├─ userName
 ├─ fromDate
 └─ toDate
```

Nếu các Input bind vào `dmSearch`, flow tìm kiếm trở nên dễ hiểu:

```text
User nhập điều kiện
→ dmSearch thay đổi
→ sbmSearch tham chiếu dmSearch
→ request được gửi
```

Điểm mạnh không chỉ là code ngắn hơn. Nó tạo một boundary rõ giữa UI state và request state.

## 3. DataList: table model phía client

`DataList` giữ nhiều row và cung cấp API như `getRowCount()`, `getCellData(rowIndex, colId)`, `getRowJSON(rowIndex)` và `getAllJSON(...)`.

```javascript
var count = dlUser.getRowCount();

for (var i = 0; i < count; i++) {
    var id = dlUser.getCellData(i, "USER_ID");
    console.log(id);
}
```

Nhưng DataList không nên bị hiểu đơn giản là JavaScript Array. Nó còn giữ metadata và row state phục vụ binding, CRUD và Submission.

## 4. Row status là một mini state machine

DataList có thể theo dõi trạng thái của từng row. Trong WebSquare5 SP5, các status thường gặp gồm:

```text
R = read / unchanged
U = updated
C = created / inserted
D = deleted
V = inserted rồi deleted
```

`getRowStatus(rowIndex)` cho phép kiểm tra trạng thái hiện tại. Một row không chỉ chứa data; nó còn chứa lịch sử thay đổi đủ để hệ thống biết row nào cần insert/update/delete khi save.

```javascript
for (var i = 0; i < dlUser.getRowCount(); i++) {
    var status = dlUser.getRowStatus(i);

    if (status !== "R") {
        console.log("changed row", i, status);
    }
}
```

Senior note: đừng tự tạo thêm cột `STATUS` chỉ để duplicate row status framework nếu không có business reason. Nếu server contract cần một status field explicit thì mapping có thể cần, nhưng phải phân biệt business status với client row state.

## 5. Delete không phải lúc nào cũng biến mất ngay

Trong CRUD grid, một row bị delete có thể được đánh dấu `D` nhưng vẫn tồn tại trong model để Submission biết phải gửi delete instruction. GridView có option để ẩn row đã delete, nhưng model vẫn có thể giữ nó.

Điều này giải thích bug kiểu “UI chỉ còn 9 dòng nhưng API DataList vẫn thấy 10”. Câu hỏi đúng là API đang trả **visible rows**, **all rows**, hay **rows bao gồm delete state**. Khi export, validate hoặc count, phải chọn semantics phù hợp.

## 6. Data mutation cần phân biệt insert/remove/delete

Một framework data model thường phân biệt insert để tạo row mới và đánh dấu state mới, update để sửa row hiện có, delete để đánh dấu row cho server commit, còn remove có thể chỉ loại row khỏi client model mà không mang cùng semantic delete, tùy API/build.

Do tên API giữa generation/build có thể khác hoặc có option khác nhau, hãy tra reference đúng build trước khi chọn. Điều quan trọng là reasoning: **bạn muốn thay UI list, thay client model, hay phát sinh một delete operation cần server commit?**

## 7. LinkedDataList: derived view, không nhất thiết là dữ liệu mới

Nếu một màn hình cần filter/sort một DataList, tạo bản copy thủ công bằng loop thường làm mất row identity và status relationship. LinkedDataList tồn tại để biểu diễn một view dẫn xuất.

```text
source DataList
     │
     ├─ filter
     └─ sort
     │
     ▼
LinkedDataList
```

Không nên mặc định coi LinkedDataList là một source of truth độc lập. Hãy hiểu relation của nó với source trước khi update/save.

## 8. Submission là communication description, không phải business transaction

WebSquare `Submission` mô tả client-server communication: action/endpoint, request reference, response target, mode và callback lifecycle.

```text
dmSearch
   │ reference
   ▼
sbmSearch
   │ HTTP
   ▼
server
   │ response
   ▼
dlUser target
   │ binding
   ▼
GridView
```

Submission giúp chuẩn hóa serialization và mapping nhưng nó không tự biến nhiều HTTP call thành một database transaction. Transaction thật nằm ở server.

## 9. Reference và Target là contract dữ liệu

**Reference** biểu diễn client data được serialize thành request. **Target** biểu diễn client model nhận response.

Nếu request chạy thành công nhưng Grid rỗng, hãy tách pipeline:

```text
HTTP response có data?
        ↓
response mapping có đúng path/schema?
        ↓
Target DataList có data?
        ↓
GridView có bind đúng DataList?
```

Đừng nhảy thẳng từ “Network 200” sang “Grid bug”.

## 10. Execute Submission và async reasoning

Một cách thường gặp để chạy Submission là:

```javascript
$p.executeSubmission(sbmSearchUser);
```

Nếu mode là asynchronous, dòng tiếp theo không chờ response.

```javascript
$p.executeSubmission(sbmSearchUser);
console.log(dlUser.getRowCount()); // không được giả định response đã về
```

Mental model đúng:

```text
executeSubmission()
→ request scheduled/sent
→ current JS handler tiếp tục và kết thúc
→ response về sau
→ submitdone hoặc submiterror chạy
```

Nếu code cần dùng response, đặt nó ở lifecycle callback tương ứng hoặc trong function được callback gọi.

## 11. Success HTTP không đồng nghĩa success nghiệp vụ

Server có thể trả HTTP 200 nhưng payload báo business failure, ví dụ duplicate key, validation fail hoặc insufficient business permission.

Cần phân biệt ít nhất ba lớp result:

```text
transport result
HTTP/network có thành công không?

protocol/application result
payload có đúng schema không?

business result
operation có được chấp nhận không?
```

Một handler `submitdone` không nên mặc định hiển thị “Save success” chỉ vì transport không lỗi. Nó phải đọc business result contract.

## 12. Error path phải là first-class path

Nhiều màn hình chỉ viết happy path:

```javascript
scwin.sbmSave_submitdone = function () {
    alert("Saved");
};
```

Production flow phải nghĩ đến timeout, 401/403, 500, network loss, malformed payload, duplicate click và server business failure. Nếu UI set loading state trước request thì mọi terminal path phải reset state. Nếu chỉ reset ở success, user có thể bị kẹt nút Save sau error.

## 13. Race condition giữa các search request

Một case phổ biến là request A được gửi trước nhưng chậm, request B được gửi sau nhưng nhanh. B hiển thị trước, rồi A về sau và ghi đè result. UI cuối cùng không còn phản ánh user intent mới nhất.

Giải pháp tùy framework/build và API: abort request cũ, disable new search khi request đang chạy, hoặc attach request identity và bỏ response stale. WebSquare có mechanism abort Submission ở các API/build tương ứng, nhưng first principle vẫn là: **asynchronous response không đảm bảo về đúng thứ tự user intent**.

## 14. Query flow và Save flow nên tách

Search/query thường read-only, dễ retry/cancel và response thường thay result list. Save là mutation, cần validation, duplicate protection, concurrency handling và xử lý partial/business failure cẩn thận.

Đừng dùng cùng một helper mơ hồ cho mọi Submission nếu nó che mất semantics này.

## 15. CRUD screen pattern

Một flow enterprise điển hình:

```text
Search
  ↓
dlUser = server result, rowStatus R
  ↓
User edits Grid
  ↓
rowStatus U/C/D
  ↓
Validate changed rows
  ↓
Save Submission
  ↓
server transaction
  ↓
success
  ↓
re-query hoặc normalize client state
```

Sau save, **re-query** lấy lại dữ liệu canonical từ server và an toàn khi server có trigger/default/normalization. **Local commit/reset** giữ data hiện tại rồi reset row state, nhanh hơn nhưng dễ lệch nếu server biến đổi dữ liệu. Chọn dựa trên contract, không theo thói quen.

## 16. Dirty check

Trước khi save, nên biết có row thay đổi hay không. Có thể duyệt row status hoặc dùng API hỗ trợ của build.

```javascript
scwin.hasChangedRows = function () {
    var count = dlUser.getRowCount();

    for (var i = 0; i < count; i++) {
        if (dlUser.getRowStatus(i) !== "R") {
            return true;
        }
    }

    return false;
};
```

Nhưng cần hiểu semantics của deleted row và filtered view. Nếu `getRowCount()` không bao gồm một loại row trong configuration cụ thể, dirty check có thể sai. Kiểm tra API reference/build khi implementation cần production guarantee.

## 17. Validate changed rows, không nhất thiết validate toàn bộ dataset

Một Grid 10.000 row nhưng user chỉ sửa 2 row. Validate mọi cell mọi row trước save có thể lãng phí và tạo UX kém. Nếu business rule cho phép, chỉ validate row state `C`/`U` và các row `D` cần delete constraint.

```javascript
scwin.validateChanges = function () {
    var count = dlUser.getRowCount();

    for (var i = 0; i < count; i++) {
        var status = dlUser.getRowStatus(i);

        if (status === "C" || status === "U") {
            if (!scwin.validateUserRow(i)) {
                return false;
            }
        }
    }

    return true;
};
```

## 18. Server contract phải explicit

Client không nên gửi “mọi thứ có trong DataList” rồi để server đoán. Contract cần xác định field required/writable/server-owned, row status encode ra sao, null/empty semantics, number/date format và error payload shape.

Nếu client gửi cả field không được phép sửa, server vẫn phải whitelist/validate. Không tin payload chỉ vì nó do WebSquare tạo.

## 19. Empty string, null và undefined

Enterprise bug rất hay nằm ở semantic rỗng.

```text
""        = giá trị rỗng?
null      = không có giá trị?
undefined = field không tồn tại/không được gửi?
```

JavaScript, serializer, WebSquare DataCollection và server binding framework có thể xử lý khác nhau. Với update API, `field absent` và `field: null` thường mang ý nghĩa khác. Đừng normalize tất cả về `""` chỉ để “dễ”. Contract phải quyết định.

## 20. Date và number không nên đi qua UI format mơ hồ

Một số component có display/edit format. Data gửi server nên có canonical representation.

```text
UI: 2026/09/22
model: 20260922
hoặc API contract: 2026-09-22
```

Chọn một representation ổn định ở API boundary. Đừng parse locale-formatted string ở server nếu có thể tránh.

## 21. Submission so với AJAX thấp hơn

WebSquare cũng có AJAX utility cho trường hợp cần control request/response ở mức thấp hơn. Nhưng đừng dùng AJAX chỉ vì quen `fetch`/jQuery.

Submission có lợi khi flow phù hợp DataCollection mapping, framework lifecycle và convention của project. AJAX phù hợp khi request không khớp model đó, cần raw payload/stream/special header hoặc integration đặc biệt. Decision nên dựa vào abstraction fit, không dựa vào sở thích cá nhân.

## 22. Workflow và orchestration

Nếu nhiều Submission phụ thuộc thứ tự, project có thể dùng workflow hoặc orchestration bằng script.

```text
loadCodeList
   ↓
loadUserDetail
   ↓
loadPermission
```

Sai pattern là fire cả ba cùng lúc rồi dùng `setTimeout` để hy vọng thứ tự. Nếu request độc lập, chạy song song có thể nhanh hơn. Nếu có dependency, encode dependency explicit.

## 23. Performance: payload trước, Grid sau

Khi màn hình chậm, tách latency:

```text
T_total = request_wait
        + response_transfer
        + parse/mapping
        + DataCollection update
        + Grid rendering
        + script side effects
```

Nếu Network cho thấy response mất 3 giây, tối ưu Grid không giải quyết chính. Nếu response 50 ms nhưng UI freeze 2 giây với 50.000 row, vấn đề nằm client rendering/data processing. Evidence trước optimization.

## 24. Security boundary

DataCollection nằm trong browser memory. User có DevTools có thể đọc/sửa client state.

```text
DataMap/DataList ≠ trusted storage
rowStatus ≠ authorization proof
hidden column ≠ secret
readOnly field ≠ immutable business data
```

Server phải xác thực identity, authorization, ownership và invariant trước khi commit.

## 25. Debugging Submission theo pipeline

Khi Save thất bại, kiểm tra theo pipeline: handler Save có chạy, validation có pass, DataCollection trước submit chứa gì, reference trỏ đúng object không, request payload thực tế là gì, HTTP status/header/body là gì, business result là gì, target mapping sau response ra sao, callback nào chạy và cuối cùng có callback khác ghi đè UI không.

Đi theo thứ tự này tốt hơn việc thêm `alert()` ngẫu nhiên.

## 26. `submitdone` và `submiterror`: hiểu đúng transport boundary

Tài liệu SP5 định nghĩa `submitdone(e)` chạy khi response status code nằm trong vùng thành công, còn `submiterror(e)` chạy khi status nhỏ hơn 200 hoặc từ 300 trở lên. Điều này tạo một boundary rất cụ thể: hai callback này trước hết phản ánh **HTTP/Submission transport outcome**, không phải business outcome.

Event object của `submitdone` có các dữ liệu như `responseStatusCode`, `responseHeaders`, `responseText`, `responseBody` và, khi response `Content-Type` chứa JSON, `responseJSON`. Vì vậy code production không cần parse cùng một response theo ba cách ngẫu nhiên. Hãy chọn representation dựa trên media type và contract.

```javascript
scwin.sbmSave_submitdone = function (e) {
    var result = e.responseJSON;

    if (!result || result.success !== true) {
        scwin.showBusinessError(result);
        return;
    }

    scwin.afterSave(result);
};
```

Ví dụ trên chỉ là contract minh họa; key `success` không phải chuẩn WebSquare. Điểm cần nhớ là WebSquare quyết định transport callback, còn application quyết định business success.

`submiterror(e)` cũng có `requestBody` và `responseText` ở SP5. Đây là evidence hữu ích khi debug nhưng có thể chứa PII hoặc credential-like data. Không dump toàn bộ event vào production log chỉ vì nó tiện.

## 27. Async là default reasoning; sync là compatibility debt

SP5 Development Guide khuyến nghị Submission bất đồng bộ (asynchronous / 비동기) và có configuration cảnh báo khi dùng synchronous mode. Lý do không chỉ là style: synchronous network work khóa execution/UI path, làm browser kém responsive và khiến control flow phụ thuộc một behavior mà platform web hiện đại tránh.

Khi gặp project legacy dùng sync Submission, đừng đổi toàn bộ sang async bằng search-replace. Sync code thường vô tình dựa vào invariant:

```text
executeSubmission()
→ response đã map xong
→ dòng kế tiếp đọc target
```

Khi chuyển async, invariant đó biến mất. Migration phải tìm mọi read-after-submit, state transition, popup close, navigation và error path phụ thuộc timing cũ rồi chuyển chúng vào callback/orchestration explicit.

## 28. `getAllJSON()` không chỉ là “convert DataList thành Array”

SP5 cho phép `getAllJSON()` trả toàn bộ DataList và có option liên quan row-status data. Điều này củng cố mental model rằng DataList gồm **business cells + framework metadata**, không phải chỉ một array object.

Khi API server chỉ cần business data, đừng vô thức gửi metadata. Khi save contract cần change semantics, đừng vô thức bỏ metadata rồi tự đoán lại change bằng cách compare object. Hãy chọn API theo ý nghĩa dữ liệu cần lấy.

Các API như `getInsertedJSON()`, `getUpdatedJSON()`, `getModifiedJSON()` và `getOnlyDeletedJSON()` tồn tại ở các SP5 build tương ứng để lấy tập thay đổi theo semantic rõ hơn. Chúng hữu ích khi save changed rows, nhưng exact option và treatment của null/status phải được đối chiếu build đang chạy.

Mental model:

```text
getAllJSON       → snapshot rộng
getInsertedJSON  → rows mới
getUpdatedJSON   → rows đã sửa
getModifiedJSON  → change set theo contract API
getOnlyDeletedJSON → delete set
```

Đừng chọn API vì tên “có vẻ đúng”; kiểm tra xem deleted row, rowStatus và null conversion được trả như thế nào trong build thật.

## 29. Filtered index và real index là hai coordinate system

Khi DataList/LinkedDataList bị filter, vị trí người dùng thấy có thể khác index thật của source. SP5 có API như `getFilteredRowIndex(realRowIndex)` để ánh xạ index thật sang vị trí sau filter.

Đây không phải detail nhỏ. Nếu code giữ `selectedIndex = 5`, sau filter/sort thì “5” có thể chỉ là **tọa độ của view**, không còn là identity của business row.

```text
business key = identity ổn định
real row index = vị trí trong source model
filtered/view index = vị trí trong projection hiện tại
```

Senior code ưu tiên business key cho operation sống lâu hơn một interaction tức thời. Index chỉ nên được giữ ngắn hạn trong đúng coordinate system của nó.

## 30. Null handling đã trở thành một phần version-sensitive của DataList

Các SP5 engine mới bổ sung `nullYN` ở column và `nullYNType` ở DataList cho các API trả JSON. Với column được đánh dấu phù hợp, empty data có thể được giữ theo default behavior, bị exclude khỏi object hoặc được trả thành `null`, tùy configuration/build.

Điều này có consequence lớn với PATCH/update contract:

```text
{ name: "" }   ≠   { name: null }   ≠   { }
```

Nếu backend hiểu ba payload trên khác nhau, một thay đổi engine/config ở DataList có thể thay business behavior dù handler JavaScript không đổi. Vì vậy regression test serialization phải kiểm tra payload thật, không chỉ kiểm tra value hiển thị trên Grid.

## 31. Data type coercion cũng là contract, không phải convenience vô hại

SP5 các build gần đây có behavior/config như `preserveType` hoặc `keepDataType` để xử lý việc string được set vào column khai báo `dataType="number"` và các type khác. Đây là dấu hiệu quan trọng: type của DataList có thể tham gia coercion khi data đi vào model.

Giả sử server trả:

```json
{ "ACCOUNT_NO": "00123" }
```

Nếu column bị model như number và coercion biến nó thành `123`, leading zero đã mất trước khi Submission tiếp theo chạy. Vấn đề không nằm ở Grid formatter mà ở **domain modeling**: account number nhìn giống số nhưng bản chất là identifier, vì vậy nên là string.

Quy tắc first-principles: chọn DataList `dataType` theo ý nghĩa domain và phép toán hợp lệ, không theo hình dạng ký tự.

## 32. Row status và cell status có memory cost thật

Release note SP5 2025 ghi nhận tối ưu internal arrays liên quan `rowStatus` và `cellStatus` để giảm memory khi set lượng dữ liệu lớn. Điều này xác nhận một điều mà developer thường quên: change tracking có footprint, đặc biệt với DataList lớn.

Nếu màn hình load 50.000 × 30 cells chỉ để read-only report, hãy hỏi liệu client có thực sự cần toàn bộ dataset và full editing/change tracking hay không. Pagination, server aggregation, read-only projection hoặc lazy data strategy thường có leverage lớn hơn micro-optimize loop JavaScript.

Performance reasoning nên đi từ:

```text
number of rows × number of columns
→ metadata/change tracking
→ mapping/coercion
→ Grid rendering
→ formatter/event cost
```

chứ không chỉ nhìn DOM row count.

## 33. Workflow không phải Promise chain “cổ điển” cần thay bằng tay

WebSquare có `xf:workflow` để mô tả thứ tự `submit`/`submitDone` khi nhiều Submission cần phối hợp; guide SP5 khuyến nghị workflow chủ yếu cho communication kiểu Select. Ý nghĩa kiến trúc là dependency được khai báo thay vì giấu trong timer hoặc callback lồng sâu.

Tuy vậy workflow không tự giải quyết business transaction, rollback hay distributed consistency. Nếu `loadA → loadB → loadC` chỉ là query dependency, workflow có thể phù hợp. Nếu `saveA → saveB` phải atomic ở database, giải pháp đúng thường là một server-side transaction boundary, không phải hai client Submission nối nhau rồi hy vọng cả hai cùng thành công.

## 34. Submission serialization phải được regression-test như public contract

Một màn hình có thể nhìn hoàn toàn đúng nhưng payload thay đổi sau engine upgrade, config change hoặc DataList schema edit. Vì vậy với flow quan trọng, test nên cố định các case:

```text
empty string
null
field absent
number-like identifier
created row
updated row
deleted row
filtered dataset
server 2xx business failure
server 4xx/5xx
stale async response
```

Evidence cuối cùng là request body trong Network hoặc test harness, không phải screenshot UI. Đây là điểm nối trực tiếp sang [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md).

## 35. Checklist reasoning trước khi sửa Submission bug

Trước khi sửa code, trả lời được các câu sau: source of truth hiện nằm ở DataMap/DataList nào; row đang ở state gì; index đang dùng là source index hay filtered/view index; serializer có chuyển null/type không; request nào là latest user intent; callback đang phản ánh transport hay business result; response target có replace/merge state nào; và sau success client sẽ re-query hay tự commit local state.

Nếu một câu chưa trả lời được, fix bằng thêm `if` thường chỉ che symptom.

## 36. Kết nối

DataCollection và Submission trở nên phức tạp hơn khi page được chia thành nhiều frame/scope. Tiếp theo đọc [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md).

Khi cần kiểm thử payload, race, row-state và engine upgrade, đọc [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md). Khi behavior chỉ khác giữa local/UAT/production, đối chiếu thêm [12 — Build, Configuration, Deployment & Environment Reasoning](12_build_config_deployment.md).