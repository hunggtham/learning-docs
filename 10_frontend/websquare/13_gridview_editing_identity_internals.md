# 13 — GridView Editing, Identity & View Internals

Chapter 05 đã xây mental model `DataList = model`, `GridView = view + interaction`. Chapter này đi sâu hơn vào phần thường gây bug ở project thật: một cell đang edit chưa chắc đã commit vào model, index nhìn thấy chưa chắc là identity thật, sort/filter/group làm thay đổi view topology, selection không phải business state, và một thao tác tưởng là “sửa một ô” có thể kích hoạt nhiều event, binding và redraw.

Mục tiêu không phải thuộc mọi property GridView. Mục tiêu là có thể nhìn một bug Grid và trả lời chính xác: **giá trị hiện nằm ở editor, Grid view hay DataList; row nào đang được nói tới; event nào đã chạy; mutation đã commit chưa; và operation tiếp theo đang dùng identity nào**.

## 1. Một cell có nhiều trạng thái hơn giá trị bạn nhìn thấy

Khi user đang gõ trong một cell editable, có thể tồn tại đồng thời ba representation:

```text
editor value đang nhập
        ↓ commit/edit lifecycle
GridView cell state
        ↓ binding/data propagation
DataList canonical client value
```

Trong nhiều tình huống ba giá trị nhanh chóng đồng bộ nên developer tưởng chúng luôn là một. Nhưng ở boundary như Enter/Tab, click sang row khác, validation fail, Save được click khi editor còn active hoặc script đổi value, timing trở nên quan trọng.

Vì vậy câu hỏi “Grid đang hiển thị gì?” khác với “DataList sẽ serialize gì nếu Submission chạy ngay bây giờ?”. Save flow production phải đảm bảo edit hiện tại đã đi qua lifecycle mà project mong đợi trước khi đọc model.

## 2. Edit lifecycle là state transition, không chỉ một event

Một interaction điển hình có thể reasoning như sau:

```text
focus cell
→ enter edit mode
→ user changes editor value
→ before-change validation
→ model mutation accepted/rejected
→ row/cell status update
→ after-edit/view-change events
→ formatter/render refresh
```

Exact event name và thứ tự phụ thuộc engine build, input type và Grid configuration. SP5 từng bổ sung `viewChangeAfterEdit` để điều khiển quan hệ thứ tự giữa `onviewchange` và `onafteredit`; điều này là bằng chứng rằng event ordering là runtime contract có version, không phải thứ nên đoán từ tên event.

Senior rule: nếu business logic phụ thuộc “event A chắc chắn chạy trước event B”, hãy kiểm chứng bằng reference/release note đúng engine build và viết regression test cho assumption đó.

## 3. Before-change event phù hợp để bảo vệ invariant cục bộ

DataList có lifecycle trước cell mutation, ví dụ `onbeforecelldatachange` trong SP5. Handler có thể từ chối thay đổi trong các scenario được hỗ trợ.

```javascript
scwin.dlOrder_onbeforecelldatachange = function (info) {
    if (info.colID === "QTY" && Number(info.newValue) < 0) {
        return false;
    }
};
```

Đây là nơi tốt cho invariant rẻ, synchronous và hoàn toàn dựa vào client state hiện có. Nó không phải nơi tốt để gọi server rồi chờ kết quả như một synchronous validator.

Nếu validation cần API, hãy tách thành workflow rõ: cho phép edit vào model, đánh dấu trạng thái cần kiểm tra, chạy async validation, rồi quyết định UX khi result về. Cố biến network thành before-change synchronous path thường làm UI khó reasoning.

## 4. Row position là interaction cursor, không phải identity

`rowPosition` trả lời “row nào đang active trong model/view context hiện tại”. Nó hữu ích cho thao tác ngay tại thời điểm event, nhưng không phải khóa bền vững.

Một business entity cần identity như:

```text
EMPLOYEE_ID
ORDER_ID
ACCOUNT_NO + EFFECTIVE_DATE
```

Nếu callback async giữ `rowIndex = 7`, rồi user sort/filter/insert trước khi response về, row 7 có thể đã là entity khác.

Pattern an toàn hơn:

```javascript
var row = dlOrder.getRowPosition();
var orderId = dlOrder.getCellData(row, "ORDER_ID");

scwin.validateOrderAsync(orderId);
```

Khi response về, resolve entity bằng business key hoặc request identity thay vì tin index cũ.

## 5. View index và model index phải được phân biệt bằng tên biến

Trong Grid có sort/filter/group/paging, từ `index` một mình là quá mơ hồ. Code review nên yêu cầu tên thể hiện semantic:

```text
viewRowIndex
modelRowIndex
realRowIndex
pageRowIndex
selectedViewIndex
```

Tên API exact để convert giữa các loại index phụ thuộc Grid/DataList build và feature đang dùng. Điều quan trọng hơn là không truyền một integer qua nhiều function mà mất metadata “integer này thuộc coordinate system nào”.

Đây giống bài toán coordinate system trong graphics: cùng số `5` nhưng `x=5` ở local coordinate không đồng nghĩa `x=5` ở world coordinate.

## 6. Sort thay đổi order, không thay business identity

Khi user sort theo `USER_NAME`, vị trí row đổi nhưng `USER_ID` không đổi. Nếu application giữ selection bằng business key, nó có thể tái xác định entity. Nếu giữ bằng index, selection logic có thể silently chuyển sang row khác.

Mental model:

```text
model entities: A B C
sort by name:  C A B

identity A vẫn là A
position của A đã đổi
```

Bất kỳ logic dài-lived nào liên quan save result, popup result, async validation hoặc cross-page communication nên ưu tiên identity hơn position.

## 7. Filter tạo một view con, không xóa source data

Filter thường làm một số row không còn visible nhưng source DataList vẫn có thể chứa chúng. Vì vậy:

```text
visible row count
≠ source row count
≠ changed row count
≠ server total count
```

Một nút “Save all changes” thường phải quan tâm changed rows trong model, kể cả row hiện bị filter ẩn. Một nút “Export current view” có thể lại cần visible rows. Hai operation có semantics khác nhau dù cùng nhìn một Grid.

Trước khi dùng count/index API, viết câu tiếng Việt trước: “Tôi muốn đếm/tác động tập row nào?”. Sau đó mới chọn API.

## 8. Grouping tạo presentation hierarchy, không tự tạo domain hierarchy

Grid grouping có thể hiển thị row theo phòng ban, trạng thái hoặc category. Group header/subtotal là presentation structure. Đừng mặc định chúng là business entity mới trong DataList.

Nếu server cần hierarchy thật, contract phải biểu diễn hierarchy rõ. Nếu chỉ Grid group theo `DEPT_CD`, save vẫn nên dựa source row identity/status chứ không dựa group header position.

## 9. Selection, check và focus là ba loại interaction state khác nhau

Một Grid có thể có focused cell, current row, selected rows và checkbox selection. Chúng phục vụ UX khác nhau.

```text
focus → keyboard/edit cursor
current row → active record context
selection → user chọn một hoặc nhiều row
check column → có thể chỉ là UI selection hoặc business field
```

Bug phổ biến là dùng checkbox UI để persist `SELECTED_YN` dù business không hề có khái niệm selected. Ngược lại, nếu checkbox thật sự là field nghiệp vụ như `APPROVED_YN`, nó phải nằm trong DataList và tham gia validation/save như data.

## 10. Programmatic change và user change không nhất thiết phát cùng event

Một số component/event chỉ phát khi user interaction xảy ra, trong khi `setCellData()` hoặc binding update bằng script có thể đi đường khác. Vì vậy business invariant quan trọng không nên chỉ sống trong handler “user changed cell”.

Ví dụ total phải luôn đúng sau cả Excel upload, API load, bulk script update và user edit. Nếu total logic chỉ nằm ở `onviewchange`, các path khác có thể bypass.

Tốt hơn là có function domain rõ:

```javascript
scwin.recalculateTotal = function () {
    // đọc canonical DataList và tính lại
};
```

Các event/path cần thiết gọi function đó, hoặc server trả canonical total nếu đó là owner phù hợp.

## 11. Bulk mutation cần một transaction-like client boundary

Giả sử user chọn 2.000 row và bấm “Set ACTIVE=Y”. Nếu mỗi `setCellData()` kích hoạt formatter, summary, validation và redraw toàn Grid, chi phí có thể tăng rất lớn.

Reasoning đúng:

```text
begin bulk intent
→ mutate model rows
→ suppress/defer expensive derived work nếu build hỗ trợ
→ recalculate derived state một lần
→ redraw/refresh một lần
→ validate result
```

Tên API suspend/redraw cụ thể phụ thuộc build. Đừng copy một private engine trick từ project khác. Hãy tìm public API/config của Grid/DataList đang dùng và đo trước/sau bằng Performance trace.

## 12. Formatter là pure projection càng nhiều càng tốt

Formatter tốt nhận value/context và trả representation. Nó không nên âm thầm mutate DataList, gọi Submission hoặc query DOM lớn.

```text
model value
→ formatter
→ display text/style
```

Nếu formatter có side effect, redraw có thể vô tình chạy business logic nhiều lần. Đây là loại bug rất khó thấy vì cùng một user action có thể dẫn đến nhiều render pass.

Senior note: render callback phải được xem như hot path. Một function 0.1 ms chạy 100.000 lần vẫn thành 10 giây CPU.

## 13. Expression, subtotal và summary có computational budget

Grid hỗ trợ expression, subtotal/footer và nhiều dạng derived display. Chúng hữu ích nhưng mỗi derived value đều có cost và invalidation rule.

Nếu một cell thay đổi khiến toàn bộ summary scan lại 50.000 row, rồi bulk update 5.000 cell, complexity có thể bùng nổ. Khi performance giảm, đo số lần function chạy và dataset size trước khi tối ưu micro-code.

Một số calculation nên chuyển server nếu nó thuộc business truth hoặc cần full dataset mà browser chỉ có một page.

## 14. Infinite scroll không biến full payload thành nhỏ

Grid có thể render tuần tự hoặc hỗ trợ large-data display tốt hơn, nhưng phải tách ba vấn đề:

```text
network volume
client model volume
rendered DOM/view volume
```

Virtual/infinite rendering chủ yếu giảm view/DOM cost. Nếu server vẫn gửi 500.000 row một lần, network, JSON parse và DataList memory vẫn tồn tại.

Nếu dataset lớn thật, server-side paging/query thường là architecture boundary quan trọng hơn Grid rendering option.

## 15. Server paging làm selection xuyên trang trở thành domain problem

Nếu browser chỉ giữ page 3 gồm 20 row, “Select all 100.000 records” không thể chỉ là tick 20 checkbox hiện có.

Cần contract rõ:

```text
select current page
select loaded rows
select all rows matching last executed query
```

Trường hợp cuối thường nên gửi query snapshot + exclusion/inclusion keys cho server thay vì materialize 100.000 identity trong browser.

Đây là ví dụ điển hình cho việc UI wording phải khớp data ownership.

## 16. Save trong khi editor còn active phải có policy rõ

Một failure mode thực tế:

```text
user gõ giá trị mới
→ chưa rời cell
→ click Save
→ payload vẫn chứa giá trị trước edit
```

Không nên chữa bằng `setTimeout(100)` vì đó chỉ là timing guess. Hãy xác định public Grid/edit API hoặc lifecycle convention của project để commit/finish current edit trước khi serialize. Sau đó regression test bằng cách click Save trực tiếp khi editor còn active.

Nếu build tự commit trước click handler thì test sẽ chứng minh behavior đó; nếu không, application phải explicit.

## 17. Navigation khi cell invalid cần phân biệt “không cho rời cell” và “không cho save”

Blocking row/cell navigation cho mọi invalid value có thể làm UX bị trap. Một số rule nên ngăn mutation ngay; một số rule nên cho user tiếp tục nhập rồi validate ở Save.

Decision dựa vào loại invariant:

```text
syntactic impossible value → có thể reject sớm
required field → có thể đánh dấu lỗi và cho di chuyển
cross-row uniqueness → thường validate dataset/save
server-owned rule → validate server
```

Đừng biến mọi validation thành before-navigation block.

## 18. Error mapping phải sống qua sort/filter

Server trả `rowIndex=12` là fragile nếu user có thể sort/filter trong lúc request pending. Tốt hơn trả business identity + field/code.

```json
{
  "entityKey": "ORD-2026-00123",
  "field": "AMOUNT",
  "code": "LIMIT_EXCEEDED"
}
```

Client resolve row hiện tại bằng key rồi focus/highlight nếu row visible. Nếu row bị filter ẩn, UX có thể hiển thị summary “1 lỗi nằm ngoài filter hiện tại” thay vì silently bỏ lỗi.

## 19. Excel import là một bulk edit pipeline

`advancedExcelUpload()` có thể đưa nhiều row vào Grid, nhưng về architecture nó là một import pipeline:

```text
untrusted file
→ parse/convert
→ column mapping
→ client model
→ validation
→ preview/error report
→ server validation
→ transaction/partial result
```

Không nên coi “Excel đã hiện đúng trong Grid” là “dữ liệu đã an toàn để save”. Type conversion, trim, date format, duplicate key và hidden formula/content đều cần policy.

## 20. Excel export phải định nghĩa value semantics

Grid có thể hiển thị code label khác model value. `advancedExcelDownload()` hỗ trợ nhiều option liên quan value/label, style, data format, row limit và callback tùy build.

Trước khi cấu hình, quyết định report contract:

```text
Excel dùng code hay label?
Export source dataset hay current grouped/filtered view?
Date là text hay Excel date?
Có export hidden/sensitive column không?
Max row/cell là bao nhiêu?
```

Security review phải bao gồm việc người dùng có thể export dữ liệu mà UI chỉ “ẩn” nhưng DataList vẫn chứa.

## 21. Accessibility thay đổi interaction assumptions

Grid accessibility mode có thể thay đổi embedded input, focus movement, keyboard behavior và rendering footprint. Vì vậy test Grid chỉ bằng mouse là chưa đủ.

Regression scenario nên có:

```text
Tab/Shift+Tab
arrow navigation
enter/escape edit
screen-reader relevant label/title
error focus
popup return focus
```

Performance optimization không được mặc định tắt accessibility để giảm DOM. Hãy giảm data/render cost trước.

## 22. Grid debugging theo bốn coordinate

Khi một cell “sai”, ghi lại bốn thứ:

```text
business key của row
model index / view index hiện tại
column ID
value ở editor / Grid / DataList
```

Sau đó mới xem event trace. Cách này loại bỏ phần lớn nhầm lẫn do chỉ log `rowIndex=3`.

Một debug record tốt có thể như:

```javascript
console.log("[order-grid] edit", {
    orderId: orderId,
    viewRowIndex: viewRowIndex,
    columnId: info.colID,
    oldValue: info.oldValue,
    newValue: info.newValue
});
```

Không log dữ liệu nhạy cảm nếu production policy không cho phép.

## 23. Master invariant cho Grid screen

Một Grid screen production nên giữ các invariant sau:

```text
Business identity không phụ thuộc view index.
Submission serialize canonical model, không đọc DOM.
Unsaved change không bị mất khi sort/filter/navigation ngoài ý muốn.
Async result không apply vào entity khác vì index stale.
Bulk operation không tạo event/redraw storm không kiểm soát.
Export/import có contract riêng, không chỉ “copy Grid”.
Accessibility và keyboard path được test như interaction chính thức.
```

Nếu một design vi phạm một invariant, hãy ghi rõ lý do và regression test cho exception đó.

## 24. Case study: chỉnh giá hàng loạt

Giả sử màn hình có 20.000 sản phẩm, server paging 100 row/page. User filter category A, chọn 40 row trên page hiện tại, tăng giá 5%, rồi Save.

Đầu tiên, selection phải được snapshot bằng `PRODUCT_ID`, không bằng row index. Tiếp theo, bulk mutation cập nhật DataList hiện có và đánh dấu row dirty. Derived display như margin có thể recalculate một lần sau batch. Save gửi changed entities cùng version để optimistic locking. Server trả success/error theo `PRODUCT_ID`. Client map error về row hiện tại bằng key; nếu user đã sort trong lúc request pending, index mới vẫn không làm sai identity.

Nếu product ở page khác không được load, operation không được tự hiểu là “tất cả category A”. Nếu product requirement muốn “tăng 5% toàn bộ kết quả filter”, đó phải là server-side bulk command dựa trên query snapshot, không phải loop Grid.

Case này gom nhiều nguyên tắc thành một câu: **Grid chỉ là cửa sổ tương tác lên một tập dữ liệu có identity và ownership rõ; đừng biến vị trí hiển thị thành business truth.**

## 25. Kết nối

Chapter này mở rộng [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md) bằng editing/view internals. Khi Grid được đặt trong app shell nhiều tab/window, identity của **page instance** cũng quan trọng như identity của row. Tiếp theo đọc [14 — Application Shell, Navigation & Multi-Screen State](14_application_shell_navigation_state.md).
