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

Ví dụ:

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

`getRowStatus(rowIndex)` cho phép kiểm tra trạng thái hiện tại.

Đây là một state machine. Một row không chỉ chứa data; nó còn chứa lịch sử thay đổi đủ để hệ thống biết row nào cần insert/update/delete khi save.

Ví dụ:

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

Điều này giải thích bug kiểu:

“UI chỉ còn 9 dòng nhưng `getAllJSON()` thấy 10.”

Câu hỏi đúng là API đang trả **visible rows**, **all rows**, hay **rows bao gồm delete state**. Khi export, validate hoặc count, phải chọn semantics phù hợp.

## 6. Data mutation cần phân biệt insert/remove/delete

Một framework data model thường phân biệt:

**insert** — tạo row mới và đánh dấu state mới.

**update** — sửa row hiện có.

**delete** — đánh dấu row để server biết cần xóa.

**remove** — có thể loại row khỏi client model mà không mang semantic delete tương tự, tùy API.

Do tên API giữa generation/build có thể khác hoặc có option khác nhau, hãy tra reference đúng build trước khi chọn. Điều quan trọng là reasoning: **bạn muốn thay UI list, thay client model, hay phát sinh một delete operation cần server commit?**

## 7. LinkedDataList: derived view, không nhất thiết là dữ liệu mới

Nếu một màn hình cần filter/sort một DataList, tạo bản copy thủ công bằng loop thường làm mất row identity và status relationship. LinkedDataList tồn tại để biểu diễn một view dẫn xuất.

Mental model tương tự database view:

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

Một flow cơ bản:

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

Một Submission thường cần biết dữ liệu nào gửi đi và response đi vào object nào.

**Reference** biểu diễn client data được serialize thành request.

**Target** biểu diễn client model nhận response.

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

Sai mental model:

```javascript
$p.executeSubmission(sbmSearchUser);
console.log(dlUser.getRowCount()); // giả định response đã về
```

Đúng mental model:

```text
executeSubmission()
→ request scheduled/sent
→ current JS handler tiếp tục và kết thúc
→ sau đó response về
→ submitdone / callback chạy
```

Nếu code cần dùng response, đặt nó ở lifecycle callback tương ứng hoặc trong function được callback gọi.

## 11. Success HTTP không đồng nghĩa success nghiệp vụ

Server có thể trả HTTP 200 nhưng payload báo business failure, ví dụ duplicate key, validation fail hoặc insufficient business permission.

Do đó cần phân biệt ít nhất ba lớp result:

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

Production flow phải nghĩ đến timeout, 401/403, 500, network loss, malformed payload, duplicate click và server business failure.

Nếu UI set loading state trước request:

```javascript
scwin.isSaving = true;
btnSave.setDisabled(true);
```

thì **mọi terminal path** phải reset state. Nếu chỉ reset ở success, user có thể bị kẹt nút Save sau error.

## 13. Race condition giữa các search request

Một case phổ biến:

1. User search keyword `A`.
2. Request A chậm.
3. User đổi keyword thành `B` và search.
4. Request B nhanh, result B hiển thị.
5. Request A về sau và ghi đè result bằng A.

UI cuối cùng không phản ánh điều kiện hiện tại.

Giải pháp tùy framework/build và API: abort request cũ, disable new search khi request đang chạy, hoặc attach request identity và bỏ response stale.

WebSquare cung cấp mechanism abort cho Submission ở một số dòng API. Nhưng first principle vẫn là: **asynchronous response không đảm bảo về đúng thứ tự user intent**.

## 14. Query flow và Save flow nên tách

Search/query thường có đặc tính:

```text
read-only
có thể retry
có thể cancel
response thay toàn bộ result list
```

Save có đặc tính:

```text
mutation
cần validation
cần duplicate protection
có thể cần optimistic/pessimistic concurrency handling
phải xử lý partial/business failure cẩn thận
```

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

Sau save, có hai chiến lược chính.

**Re-query** lấy lại dữ liệu canonical từ server. Đơn giản và an toàn khi server có trigger/default/normalization.

**Local commit/reset** giữ data hiện tại rồi reset row state. Nhanh hơn nhưng dễ lệch nếu server biến đổi dữ liệu.

Chọn dựa trên contract, không theo thói quen.

## 16. Dirty check

Trước khi save, nên biết có row thay đổi hay không. Có thể duyệt row status hoặc dùng API hỗ trợ của build.

Ví dụ reasoning thủ công:

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

Một Grid 10.000 row nhưng user chỉ sửa 2 row. Validate mọi cell mọi row trước save có thể lãng phí và tạo UX kém.

Nếu business rule cho phép, chỉ validate row state `C`/`U` và các row `D` cần delete constraint.

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

Performance tốt hơn và semantics rõ hơn.

## 18. Server contract phải explicit

Client không nên gửi “mọi thứ có trong DataList” rồi để server đoán. Hãy định nghĩa rõ:

```text
field nào required
field nào writable
field nào server-owned
row status encode ra sao
null/empty semantics
number/date format
error payload shape
```

Nếu client gửi cả field không được phép sửa, server vẫn phải whitelist/validate. Không tin payload chỉ vì nó do WebSquare tạo.

## 19. Empty string, null và undefined

Enterprise bug rất hay nằm ở semantic rỗng.

```text
""        = người dùng để trống?
null      = không có giá trị?
undefined = field không được gửi?
```

JavaScript, serializer, WebSquare DataCollection và server binding framework có thể xử lý khác nhau. Với update API, `field absent` và `field: null` thường mang ý nghĩa khác.

Đừng normalize tất cả về `""` chỉ để “dễ”. Contract phải quyết định.

## 20. Date và number không nên đi qua UI format mơ hồ

Một số component có display/edit format. Data gửi server nên có canonical representation.

Ví dụ date:

```text
UI: 2026/09/22
model: 20260922
hoặc ISO contract: 2026-09-22
```

Chọn một representation ổn định ở API boundary. Đừng parse locale-formatted string ở server nếu có thể tránh.

## 21. Submission so với AJAX thấp hơn

WebSquare cũng có AJAX utility cho trường hợp cần control request/response ở mức thấp hơn. Nhưng đừng dùng AJAX chỉ vì quen `fetch`/jQuery.

Submission có lợi khi flow phù hợp DataCollection mapping, framework lifecycle và convention của project. AJAX phù hợp khi request không khớp model đó, cần raw payload/stream/special header hoặc integration đặc biệt.

Decision nên dựa vào abstraction fit, không dựa vào sở thích cá nhân.

## 22. Workflow và orchestration

Nếu nhiều Submission phụ thuộc thứ tự, project có thể dùng workflow hoặc orchestration bằng script.

Ví dụ dependency:

```text
loadCodeList
   ↓
loadUserDetail
   ↓
loadPermission
```

Sai pattern là fire cả ba cùng lúc rồi dùng `setTimeout` để hy vọng thứ tự.

Nếu request độc lập, chạy song song có thể nhanh hơn. Nếu có dependency, encode dependency explicit.

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

Nếu Network tab cho thấy response mất 3 giây, tối ưu Grid không giải quyết chính. Nếu response 50 ms nhưng UI freeze 2 giây với 50.000 row, vấn đề nằm client rendering/data processing.

Evidence trước optimization.

## 24. Security boundary

DataCollection nằm trong browser memory. User có DevTools có thể đọc/sửa client state. Vì vậy:

```text
DataMap/DataList ≠ trusted storage
rowStatus ≠ authorization proof
hidden column ≠ secret
readOnly field ≠ immutable business data
```

Server phải xác thực identity, authorization, ownership và invariant trước khi commit.

## 25. Debugging Submission theo pipeline

Khi Save thất bại:

```text
1. Handler Save có chạy?
2. Validation có pass?
3. DataCollection trước submit chứa gì?
4. Submission reference trỏ đúng object?
5. Request payload thực tế trong Network là gì?
6. HTTP status/header/body là gì?
7. Server business result là gì?
8. Target mapping sau response ra sao?
9. submitdone/error callback nào chạy?
10. UI có bị callback khác ghi đè không?
```

Đi theo thứ tự này tốt hơn việc thêm `alert()` ngẫu nhiên.

## 26. Kết nối

DataCollection và Submission trở nên phức tạp hơn khi page được chia thành nhiều frame/scope. Tiếp theo đọc [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md).
