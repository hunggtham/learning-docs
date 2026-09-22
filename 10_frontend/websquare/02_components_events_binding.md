# 02 — Components, Events & Data Binding

## 1. Component API là contract, DOM chỉ là implementation detail

Trong WebSquare, component là abstraction mà engine expose cho application code. Một Input, SelectBox, Button, GridView hay WFrame có property, event và method riêng. Khi framework cung cấp `getValue()`, `setValue()`, `setReadOnly()`, `validate()` hoặc binding API, đó mới là contract mà code nên dựa vào.

Ví dụ với Input:

```javascript
var userId = inputUserId.getValue();
inputUserId.setValue("A1024");
inputUserId.setReadOnly(true);
```

Cách này khác với việc tìm DOM bên trong component rồi gán `.value`. Khi gọi public API, engine có cơ hội đồng bộ internal state, format, validation và binding. Khi sửa DOM trực tiếp, bạn có thể chỉ đổi phần hiển thị.

Một senior note quan trọng là: **public API là semantic boundary**. Nếu một yêu cầu có thể giải quyết bằng public API, ưu tiên nó. Chỉ xuống DOM khi thật sự cần và phải coi đó là dependency có upgrade risk.

## 2. Giá trị thật và giá trị hiển thị không phải lúc nào cũng giống nhau

Input có thể áp dụng format ngày, số, tiền tệ hoặc mask. Khi đó người dùng nhìn thấy một chuỗi đã format nhưng framework có thể giữ actual value khác.

Ví dụ một ngày có thể được hiển thị như `2026/09/22` nhưng actual value là `20260922`. Vì vậy khi debug dữ liệu gửi server, hãy phân biệt:

```text
raw/actual value
        ≠
display value
        ≠
text nằm trong một DOM node cụ thể
```

Nếu API có `getValue()` và một API khác trả display-formatted value, hãy chọn theo contract dữ liệu. Server thường nên nhận normalized value, không phải chuỗi trình bày cho người dùng.

## 3. Event handler nên là boundary adapter

Một event handler tốt thường rất ngắn:

```javascript
scwin.btnSearch_onclick = function () {
    scwin.searchUsers();
};
```

Sau đó orchestration nằm ở function có tên theo nghiệp vụ:

```javascript
scwin.searchUsers = function () {
    if (!scwin.validateSearch()) {
        return;
    }

    $p.executeSubmission(sbmSearchUser);
};
```

Pattern này có ba lợi ích. Thứ nhất, UI event không chứa toàn bộ nghiệp vụ. Thứ hai, function có thể được gọi lại từ keyboard shortcut, popup callback hoặc test harness. Thứ ba, stack trace và log có tên có ý nghĩa.

Anti-pattern là:

```javascript
scwin.btnSearch_onclick = function () {
    // 150 dòng validate
    // sửa nhiều component
    // build request
    // gọi submission
    // mở popup
    // update grid
};
```

Khi một event handler trở thành nơi mọi thứ xảy ra, coupling giữa UI và business flow tăng rất nhanh.

## 4. Event trước và sau thay đổi có semantics khác nhau

Nhiều component/data object có event dạng “before change” và “after change”. Đây không chỉ là khác tên. Event trước thay đổi thường cho phép kiểm tra hoặc chặn mutation; event sau thay đổi phù hợp để phản ứng sau khi state đã đổi.

Ví dụ với DataList, một `onbeforecelldatachange` có thể return `false` để từ chối thay đổi. Mental model là:

```text
user proposes change
        │
        ▼
before-change event
        │
        ├─ false → reject
        │
        └─ allow
             │
             ▼
        model mutation
             │
             ▼
        after-change event
```

Nếu validation cần ngăn dữ liệu invalid vào model, before-event thường phù hợp hơn. Nếu logic cần tính lại tổng sau khi value đã được commit, after-event phù hợp hơn.

## 5. Binding: nối UI với model

Binding là cơ chế làm cho component đọc/ghi dữ liệu qua DataCollection thay vì mỗi component giữ một bản sao dữ liệu độc lập.

Ví dụ Input có thể bind với một key trong DataMap. Public API của Input cho phép đặt reference dạng:

```javascript
inputName.setRef("data:dmUser.name");
```

Mental model:

```text
Input component
      ⇅
binding contract
      ⇅
DataMap key
```

Nếu GridView bind với DataList, GridView là view còn DataList là data model. Đây là distinction rất quan trọng. Khi cần sửa business data, ưu tiên reasoning trên DataList; khi cần đổi cách hiển thị, ưu tiên GridView.

## 6. Source of truth và duplicated state

Giả sử màn hình có:

```text
inputUserId
hiddenUserId
scwin.selectedUserId
dmUser.userId
```

Nếu cả bốn đều giữ cùng một giá trị, hệ thống đang có bốn source of truth giả. Một handler update ba chỗ nhưng quên chỗ thứ tư là đủ tạo bug.

Pattern tốt hơn là chọn một model chính, ví dụ `dmUser.userId`, rồi để Input bind vào model. `scwin` chỉ giữ state không thuộc business model, ví dụ `isSaving`, `currentMode` hoặc cache tạm cho orchestration.

Một rule thực dụng:

```text
Dữ liệu cần submit / bind / track thay đổi → DataCollection
UI presentation state → component
Transient orchestration state → scwin
Persistent business truth → server
```

## 7. Validation có nhiều tầng

Validation phía client giúp UX tốt hơn nhưng không tạo security boundary. Có thể chia validation thành bốn tầng.

**Input-format validation** kiểm tra ký tự, độ dài, pattern, date/number format.

**Cross-field validation** kiểm tra quan hệ giữa nhiều input, ví dụ `startDate <= endDate`.

**Domain validation** kiểm tra business rule, ví dụ amount không vượt hạn mức.

**Server validation** là tầng bắt buộc cho dữ liệu không đáng tin cậy và rule liên quan authorization/transaction.

WebSquare component có validation API và property hỗ trợ nhiều case UI. Tuy nhiên đừng biến client validation thành nơi duy nhất bảo vệ nghiệp vụ.

Ví dụ:

```javascript
scwin.validateSearch = function () {
    var keyword = inputKeyword.getValue().trim();

    if (keyword.length === 1) {
        // show user-facing message
        return false;
    }

    return true;
};
```

Server vẫn phải validate input thật sự nhận được.

## 8. `readOnly`, `disabled`, `hidden` không đồng nghĩa authorization

Một field `readOnly` chỉ ngăn user sửa qua UI thông thường. `disabled` chỉ thay interaction của component. `hidden` chỉ làm nó không hiển thị.

Không giá trị nào trong ba thứ trên chứng minh user không thể gửi request khác bằng DevTools hoặc HTTP client. Authorization phải ở server.

Mental model:

```text
UI restriction = trải nghiệm và guardrail
Server authorization = security control
```

Đây là nguyên tắc web security chung, không riêng WebSquare.

## 9. Naming là một phần của maintainability

Enterprise screen có thể có hàng chục component. ID kiểu `input1`, `input2`, `grid1`, `submission1` khiến code khó đọc.

Một convention dễ reasoning hơn:

```text
inputUserId
inputUserName
btnSearch
grUser      hoặc grdUser
dmSearch
dmDetail
dlUser
sbmSearchUser
sbmSaveUser
```

Tên nên cho biết **loại object + vai trò nghiệp vụ**. Khi stack trace hoặc log chỉ có ID, tên tốt giúp giảm context switching.

## 10. Component state transition thay vì imperative chaos

Một màn hình thường có mode như `VIEW`, `CREATE`, `EDIT`, `SAVING`. Anti-pattern là rải `setReadOnly`, `show`, `hide`, `setDisabled` khắp nhiều handler.

Tốt hơn là gom state transition:

```javascript
scwin.setMode = function (mode) {
    scwin.currentMode = mode;

    var editable = mode === "CREATE" || mode === "EDIT";
    inputUserName.setReadOnly(!editable);
    btnSave.setDisabled(!editable);
};
```

Giá trị thực sự ở đây không phải function nhỏ hơn, mà là **UI trở thành state machine có tên**. Khi bug xảy ra, bạn hỏi “page đang ở mode nào?” thay vì “handler nào vừa thay property gì?”.

## 11. Event loop và duplicate click

Nếu user bấm Save hai lần nhanh, hai Submission có thể được tạo trước khi response đầu tiên về. Đây là race condition ở cấp UI/network.

Một guard đơn giản:

```javascript
scwin.save = function () {
    if (scwin.isSaving) {
        return;
    }

    scwin.isSaving = true;
    btnSave.setDisabled(true);
    $p.executeSubmission(sbmSaveUser);
};

scwin.sbmSaveUser_submitdone = function () {
    scwin.isSaving = false;
    btnSave.setDisabled(false);
};
```

Production code còn cần reset flag ở error path. Với operation không idempotent, server cũng phải có protection phù hợp; client guard chỉ giảm duplicate interaction, không thể là guarantee duy nhất.

## 12. Programmatic change và user change có thể phát event khác nhau

Framework UI thường phân biệt thay đổi do user thao tác và thay đổi bằng API. Ví dụ trong dòng WebSquare mới, `setValue()` có thể kích hoạt một số event nhưng không kích hoạt event dành riêng cho view/user interaction.

Do đó đừng dựa vào giả định “setValue chắc chắn giống user gõ”. Nếu logic phụ thuộc event cụ thể, kiểm tra API reference của đúng component/build.

Một pattern an toàn hơn là đưa business reaction vào function rõ ràng:

```javascript
scwin.applyCustomer = function (customer) {
    inputCustomerId.setValue(customer.id);
    inputCustomerName.setValue(customer.name);
    scwin.refreshCustomerDependentState();
};
```

Thay vì hy vọng chuỗi event side effect tự chạy đúng khi set nhiều field.

## 13. Binding loop và side effect cascade

Nếu A change cập nhật B, B change cập nhật C, C change lại cập nhật A, bạn đã tạo feedback loop. Framework có thể suppress một số event nhưng không nên dựa vào behavior ngầm.

Hãy thiết kế dependency một chiều nếu có thể:

```text
source model
   ↓
derived calculation
   ↓
UI rendering
```

Nếu bắt buộc two-way binding, side effect không nên quay lại write source mà không có guard.

## 14. Component coupling giữa page

Một page con gọi trực tiếp component của page cha:

```javascript
$p.parent().inputMainStatus.setValue("DONE");
```

Cách này chạy nhưng coupling cao. Page con biết ID và implementation của cha. Nếu cha đổi layout/component, page con hỏng.

Tốt hơn là expose function ở boundary:

```javascript
// parent
scwin.setStatus = function (status) {
    inputMainStatus.setValue(status);
};

// child
$p.parent().scwin.setStatus("DONE");
```

Tốt hơn nữa trong flow phức tạp là truyền callback contract hoặc data/result contract rõ ràng. Chapter Scope sẽ nói kỹ hơn.

## 15. CSS và component internals

Khi Scope/WFrame được dùng, engine có thể biến đổi DOM ID. Vì vậy CSS dựa class thường bền hơn CSS dựa physical ID. Ngoài ra component có thể render nested structure, nên selector quá sâu như:

```css
#someGeneratedId > div > span > input { ... }
```

rất fragile.

Ưu tiên semantic class do application kiểm soát. Nếu cần style vùng internal component, ghi rõ đây là dependency vào renderer version và có visual regression test sau engine upgrade.

## 16. Event delegation không phải lúc nào cũng cần tự viết

Trong JavaScript thuần, event delegation thường giúp xử lý nhiều node động. Trong WebSquare, component framework đã quản lý event layer cho nhiều UI object. Đừng tự thêm một global DOM listener chỉ vì quen pattern từ vanilla JS nếu component event đã cung cấp contract tốt hơn.

Mỗi layer listener bổ sung có thể gây double handling, khó trace stopPropagation và bypass Scope semantics.

## 17. Data binding và GridView: preview cho chapter sau

Khi DataList bind với GridView, bạn có thể đọc dữ liệu từ DataList:

```javascript
var count = dlUser.getRowCount();
var userId = dlUser.getCellData(0, "USER_ID");
var row = dlUser.getRowJSON(0);
```

Điều quan trọng là GridView không phải business data store. Nếu Grid chỉ là view của `dlUser`, code save nên reasoning trên `dlUser` và row status của nó.

## 18. Debugging checklist cho component/event/binding

Khi UI không phản ứng đúng, đi theo pipeline:

```text
1. Component có tồn tại đúng Scope không?
2. Event có fire không?
3. Handler nào chạy?
4. Handler đọc actual value nào?
5. Component có binding không?
6. Model sau event có thay đổi không?
7. Side effect nào chạy tiếp?
8. Có event thứ hai ghi đè state không?
```

Đặt breakpoint ở handler, inspect component API value và DataCollection value cùng lúc. Đừng chỉ nhìn UI.

## 19. Senior review questions

Khi review một màn hình, hãy hỏi:

“State này có bị giữ ở nhiều object không?”

“Handler có quá nhiều trách nhiệm không?”

“Code có đang query DOM internal thay vì component API không?”

“Validation này thuộc UX hay security?”

“Programmatic set có đang phụ thuộc side-effect event không rõ ràng không?”

“Page con có phụ thuộc ID của page cha quá nhiều không?”

Nếu trả lời được những câu này, bạn đang review architecture chứ không chỉ syntax.

## 20. Kết nối

Tiếp theo: [03 — DataCollection & Submission](03_data_collection_submission.md), nơi state model được nối với server communication và row-state semantics.
