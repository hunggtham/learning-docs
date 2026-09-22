# 05 — GridView, CRUD & Enterprise Screen Patterns

## 1. GridView là view; DataList mới là dữ liệu nghiệp vụ phía client

GridView là một trong những component quan trọng nhất của WebSquare vì nhiều ứng dụng doanh nghiệp xoay quanh bảng tra cứu, chỉnh sửa hàng loạt và CRUD. Tuy nhiên mental model sai phổ biến nhất là coi GridView như “database trên màn hình”.

Nếu GridView bind với `dlUser`, hãy nghĩ:

```text
DataList = model
GridView = view + interaction layer
```

DataList giữ row, column value và row status. GridView chịu trách nhiệm hiển thị, selection, edit UI, formatting, sort/filter/display behavior và các event liên quan interaction.

Khi cần gửi dữ liệu server, dirty check hoặc phân tích state, ưu tiên model. Khi cần thay cách trình bày, ưu tiên GridView.

## 2. Search screen điển hình

Một màn hình tìm kiếm enterprise thường có flow:

```text
Search condition Inputs
        ⇅ binding
dmSearch
        │ reference
        ▼
sbmSearch
        │
        ▼
server query
        │
        ▼
dlUser target
        ⇅ binding
GridView
```

Flow này tốt vì mỗi layer có trách nhiệm rõ. Nếu GridView rỗng, bạn có thể inspect `dlUser`. Nếu `dlUser` rỗng, inspect Submission response. Nếu response rỗng, inspect server query.

## 3. Row identity quan trọng hơn row index

Row index là vị trí hiện tại trong list, không phải identity business ổn định. Sort, filter, insert, delete hoặc paging có thể làm index thay đổi.

Sai pattern:

```javascript
scwin.selectedRowIndex = 5;
// vài thao tác sau
var id = dlUser.getCellData(scwin.selectedRowIndex, "USER_ID");
```

Nếu list đã sort hoặc filter, row 5 có thể là user khác.

Tốt hơn là giữ business key khi cần reference dài hơn một event:

```javascript
var row = dlUser.getRowPosition();
scwin.selectedUserId = dlUser.getCellData(row, "USER_ID");
```

Sau đó nếu cần, tìm lại row bằng key theo API phù hợp.

## 4. CRUD row status và ý nghĩa thật

Grid edit làm DataList row chuyển state. Một lifecycle thường là:

```text
server result → R
user edit → U
insert new row → C
delete existing row → D
insert rồi delete → V
```

Đây là thông tin quan trọng để save chỉ phần thay đổi.

```javascript
var count = dlUser.getRowCount();
for (var i = 0; i < count; i++) {
    var status = dlUser.getRowStatus(i);
    if (status !== "R") {
        console.log(i, status, dlUser.getRowJSON(i));
    }
}
```

Đừng reset row status chỉ để UI “trông sạch” trước khi server commit. Bạn sẽ mất evidence về unsaved changes.

## 5. Insert row nên khởi tạo default có chủ đích

Khi user thêm row mới, đừng để mỗi cell tự có default rời rạc nếu chúng đại diện một business object.

```javascript
scwin.addUser = function () {
    var rowIndex = dlUser.insertRow();

    dlUser.setCellData(rowIndex, "ACTIVE_YN", "Y");
    dlUser.setCellData(rowIndex, "COUNTRY_CD", "KR");
};
```

Tên API có thể khác theo generation/build, nhưng pattern là: **create row → initialize domain defaults → move focus/selection**.

Nếu default đến server/config, tránh hard-code rải rác nhiều screen.

## 6. Delete và remove khác business meaning

Khi xóa row đã tồn tại trên server, client thường cần giữ delete intent để save. Nếu chỉ remove row khỏi DataList mà không giữ status/delete payload, server không biết phải xóa gì.

Ngược lại, row mới `C` chưa từng tồn tại server nếu user bỏ đi có thể chỉ cần remove client-side.

Vì vậy trước khi chọn API, xác định state transition:

```text
existing row → marked delete → server DELETE
new unsaved row → discard locally
```

## 7. GridView có thể ẩn row deleted nhưng DataList vẫn giữ

Property như `hideDeletedRow` cho phép UI không hiển thị row `D`. Đây là presentation choice, không phải model deletion.

Hệ quả: count trên Grid và count trên DataList có thể khác semantics. Khi hiển thị “총 10건”, hãy quyết định đang đếm visible records, server records hay all client rows including deleted.

## 8. Cell value và display value

Một cell có thể hiển thị label nhưng lưu code.

```text
model value: "01"
display value: "서울"
```

Hoặc date/number format tương tự Input. Khi build payload hoặc compare business data, dùng model value. Khi export “những gì user nhìn thấy”, display value có thể phù hợp hơn.

Đừng compare display string nếu business rule dựa code.

## 9. Validation theo row state

Một Grid 5.000 row nhưng chỉ 3 row thay đổi. Validation hiệu quả nên tập trung changed rows.

```javascript
scwin.validateChangedRows = function () {
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

Nếu rule liên quan uniqueness toàn dataset, vẫn có thể cần scan nhiều row. Optimize theo semantics, không theo công thức “chỉ changed rows”.

## 10. Cross-row invariant

Một số rule không thuộc riêng một cell:

```text
không trùng USER_ID
chỉ một row được PRIMARY=Y
sum(weight) = 100
fromDate <= toDate trong mọi row
```

Những rule này nên có function tên rõ:

```javascript
scwin.validatePrimaryRow = function () { ... };
scwin.validateDuplicateUserId = function () { ... };
```

Không nhét logic vào `onchange` của từng cell nếu rule cần toàn dataset, vì nó dễ bị bypass khi data load bằng API.

## 11. Before-change event để chặn invalid transition

DataList có event trước cell change cho phép trả `false` để từ chối mutation trong một số build.

Conceptual:

```javascript
scwin.dlUser_onbeforecelldatachange = function (info) {
    if (info.colID === "AGE" && Number(info.newValue) < 0) {
        return false;
    }
};
```

Đây phù hợp cho local invariant rẻ và rõ. Rule cần server data hoặc async check không nên block theo cách giả định synchronous.

## 12. Selection state không nên bị nhầm với data state

Grid có current row, selected rows, checked rows hoặc focus cell. Đây là interaction state, không phải business state.

Nếu user tick checkbox để chọn row gửi batch operation, hãy phân biệt:

```text
selection checkbox do UI quản lý
vs.
BUSINESS_SELECTED_YN field thực sự cần persist
```

Không nên persist UI selection chỉ vì nó tiện.

## 13. Search lại sau save hay update local?

Sau save thành công, lựa chọn thường là:

**Re-query**: server trả canonical state bằng query mới.

**Local update**: giữ DataList, update server-generated field rồi reset dirty state.

Re-query phù hợp khi server có sequence, timestamp, calculated field, trigger hoặc normalization. Local update phù hợp khi latency quan trọng và server contract trả đầy đủ canonical result.

Không có lựa chọn luôn đúng. Hãy cân correctness, latency và complexity.

## 14. Optimistic locking

Nếu hai user cùng sửa một row, row status phía client không giải quyết conflict. Server cần concurrency control, ví dụ version column hoặc last-updated timestamp.

Client gửi:

```text
USER_ID = U1001
VERSION = 7
new NAME = ...
```

Server update với condition `VERSION = 7`. Nếu affected rows = 0, có thể đã bị người khác sửa.

WebSquare chỉ là nơi transport/display conflict; invariant concurrency thuộc server/database.

## 15. Paging: client-side và server-side khác nhau

Nếu server trả 20 row mỗi page, Grid chỉ biết page hiện tại. Sort/filter client-side chỉ áp dụng dataset hiện có trừ khi framework/pattern trigger server query.

Nếu business yêu cầu sort toàn bộ 1 triệu row, server phải tham gia.

Mental model:

```text
client paging → full dataset ở browser, view chia page
server paging → browser chỉ có một slice
```

Đừng viết logic “đếm toàn bộ” dựa trên `getRowCount()` nếu server paging đang bật.

## 16. Large dataset và rendering budget

GridView hỗ trợ nhiều tính năng cho dữ liệu lớn, nhưng không có component nào miễn phí. Cost có thể đến từ:

```text
JSON parse
DataList creation
binding propagation
cell formatting
renderer creation
layout/reflow
custom event per cell
DOM nodes
```

Trước khi tối ưu, đo:

```text
response size
request duration
DataList row count
time từ response đến UI usable
main-thread long tasks
memory before/after load
```

Nếu 50 MB JSON được trả về, virtual scroll không làm network và parse cost biến mất.

## 17. N+1 Submission ở từng row là anti-pattern

Một màn hình load 100 row rồi gọi thêm một Submission cho mỗi row tạo N+1 network problem.

```text
1 query list
+ 100 query detail
= 101 request
```

Nếu server có thể join/batch, ưu tiên batch contract. Nếu detail thật sự lazy, chỉ load khi user mở row cần thiết.

## 18. Custom formatting không nên chứa heavy business logic

Cell formatter/render callback có thể chạy rất nhiều lần. Nếu nó parse JSON lớn, gọi synchronous utility nặng hoặc query DOM, scrolling sẽ lag.

Formatter nên gần pure function:

```text
input value → display representation
```

Business computation nên chuẩn bị trước ở model/server nếu phức tạp.

## 19. Excel upload/download là data boundary nguy hiểm

WebSquare hỗ trợ Grid/Excel integration ở nhiều build. Đây là feature tiện nhưng upload Excel đưa một khối dữ liệu không đáng tin vào client/server.

Phải nghĩ đến:

```text
file size limit
column mapping
formula/cell type
invalid date/number
duplicate row
malicious content
server validation
transaction size
partial failure reporting
```

Upload thành Grid không đồng nghĩa data hợp lệ để persist.

## 20. Batch save và partial failure

Giả sử 100 row được save. Server có hai strategy:

**all-or-nothing transaction**: một row lỗi thì rollback tất cả.

**partial success**: row hợp lệ commit, row lỗi trả error riêng.

Client UX phải phù hợp. Với partial success, DataList cần biết row nào đã commit và row nào còn dirty/error. Đây là protocol design, không chỉ Grid event.

## 21. Error mapping về row/cell

Server validation tốt nên trả stable identifier, ví dụ business key và field name, thay vì chỉ row index.

```json
{
  "errors": [
    {
      "userId": "U1001",
      "field": "EMAIL",
      "code": "INVALID_EMAIL"
    }
  ]
}
```

Row index trên client có thể thay đổi do sort/filter. Business key giúp map error ổn định hơn.

## 22. Query condition state

Một bug UX phổ biến: user search A, sửa điều kiện thành B nhưng chưa search, rồi export Grid. Export nên dùng data result A, nhưng title/filter label lại đọc current input B.

Có thể tách:

```text
editing search condition
last executed search condition
current result dataset
```

Nếu report/export cần biết query đã chạy, snapshot condition khi execute Submission.

## 23. UI mode: QUERY / EDIT / SAVE

Màn hình CRUD phức tạp nên explicit mode.

```javascript
scwin.setMode = function (mode) {
    scwin.mode = mode;

    var editing = mode === "EDIT" || mode === "CREATE";
    btnSave.setDisabled(!editing);
    btnAdd.setDisabled(mode === "SAVING");
};
```

Mode giúp thống nhất enable/readOnly state của nhiều component thay vì rải property mutation khắp handlers.

## 24. Unsaved-change guard

Trước khi chuyển tab/page hoặc đóng popup, nếu DataList còn dirty, application nên quyết định có prompt user không.

Dirty check phải dựa model state, không dựa “user đã click Edit”. User có thể click Edit nhưng không thay gì, hoặc data có thể bị script thay dù user không click Edit.

## 25. Grid event storm

Một bulk update có thể trigger rất nhiều event. Nếu mỗi event tính lại summary toàn dataset, complexity có thể từ O(n) thành O(n²).

Ví dụ 10.000 cell changes × scan 10.000 rows là 100 triệu operation.

Khi bulk update, xem build có cơ chế suspend event/redraw hay không; nếu không, thiết kế function tổng hợp để chỉ recalculate một lần sau batch.

## 26. Readability của grid code

Thay vì magic string rải rác:

```javascript
dlUser.getCellData(i, "USR_NM");
dlUser.getCellData(i, "USR_STS_CD");
```

Project có thể dùng constant mapping nếu convention cho phép:

```javascript
var USER_COL = {
    ID: "USER_ID",
    NAME: "USER_NAME",
    STATUS: "STATUS_CD"
};
```

Tuy nhiên đừng abstraction quá mức khiến dev phải nhảy 5 file mới biết column ID. Mục tiêu là giảm typo và giữ domain vocabulary rõ.

## 27. Example: search-edit-save hoàn chỉnh

```javascript
scwin.btnSearch_onclick = function () {
    scwin.search();
};

scwin.search = function () {
    if (scwin.hasUnsavedChanges()) {
        // confirm trước khi mất changes nếu UX yêu cầu
    }

    scwin.lastSearchCondition = dmSearch.getJSON();
    $p.executeSubmission(sbmSearchUser);
};

scwin.btnAdd_onclick = function () {
    scwin.addUser();
};

scwin.btnSave_onclick = function () {
    scwin.saveUsers();
};

scwin.saveUsers = function () {
    if (!scwin.hasUnsavedChanges()) {
        return;
    }

    if (!scwin.validateChangedRows()) {
        return;
    }

    if (scwin.isSaving) {
        return;
    }

    scwin.isSaving = true;
    $p.executeSubmission(sbmSaveUser);
};
```

Tên API DataMap như `getJSON()` phải được đối chiếu build nếu dùng thực tế; ví dụ này nhấn mạnh orchestration structure hơn là reference API tuyệt đối.

## 28. Senior code-review checklist

Khi review Grid screen, hỏi:

“Code đang thao tác model hay DOM/Grid internals?”

“Row index có bị giữ quá lâu thay vì business key?”

“Delete semantics có đúng với server operation không?”

“Dirty check dựa row state thật hay flag thủ công?”

“Validation có scan toàn bộ grid không cần thiết?”

“Có N+1 Submission không?”

“Server paging nhưng code lại giả định full dataset không?”

“Batch save có protocol partial failure rõ không?”

“Sau save client lấy canonical state từ đâu?”

## 29. Kết nối

Một Grid screen đúng logic vẫn có thể chậm, leak memory hoặc tạo security issue. Tiếp theo: [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).
