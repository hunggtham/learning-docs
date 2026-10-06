# 02 — Components, Events & dữ liệu (data / 데이터) Binding

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **02 — Components, Events & dữ liệu (data / 데이터) Binding**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. thành phần (component / 컴포넌트) API là đặc tả hợp đồng (contract / 계약), DOM chỉ là hiện thực (implementation / 구현) detail** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Giá trị thật và giá trị hiển thị không phải lúc nào cũng giống nhau** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối component, event và binding, để theo dõi dữ liệu đi từ thao tác người dùng qua model đến render và side effect.

## 1. thành phần (component / 컴포넌트) API là đặc tả hợp đồng (contract / 계약), DOM chỉ là hiện thực (implementation / 구현) detail

Trong WebSquare, thành phần (component / 컴포넌트) là lớp trừu tượng (abstraction / 추상화) mà engine expose cho ứng dụng (application / 애플리케이션) mã (code / 코드). Một đầu vào (input / 입력), SelectBox, Button, GridView hay WFrame có thuộc tính (property / 속성), sự kiện (event / 이벤트) và phương thức (method / 메서드) riêng. Khi khung phần mềm (framework / 프레임워크) cung cấp `getValue()`, `setValue()`, `setReadOnly()`, `validate()` hoặc binding API, đó mới là đặc tả hợp đồng (contract / 계약) mà mã (code / 코드) nên dựa vào.

Ví dụ với đầu vào (input / 입력):

```javascript
var userId = inputUserId.getValue();
inputUserId.setValue("A1024");
inputUserId.setReadOnly(true);
```

Cách này khác với việc tìm DOM bên trong thành phần (component / 컴포넌트) rồi gán `.value`. Khi gọi API công khai (public API / 공개 API), engine có cơ hội đồng bộ trạng thái nội bộ (internal state / 내부 상태), format, kiểm tra hợp lệ (validation / 검증) và binding. Khi sửa DOM trực tiếp, bạn có thể chỉ đổi phần hiển thị.

Một cấp cao (senior / 시니어) ghi chú (note / 노트) quan trọng là: **API công khai (public API / 공개 API) là ngữ nghĩa (semantic / 의미적) ranh giới (boundary / 경계)**. Nếu một yêu cầu có thể giải quyết bằng API công khai (public API / 공개 API), ưu tiên nó. Chỉ xuống DOM khi thật sự cần và phải coi đó là phụ thuộc (dependency / 의존성) có upgrade rủi ro (risk / 위험).

> **Nối mạch:** Component API là contract còn DOM là implementation detail; giá trị display/value làm lộ nơi hai lớp có thể khác nhau. Event handler tiếp theo làm adapter tường minh giữa UI event và domain action.

## 2. Giá trị thật và giá trị hiển thị không phải lúc nào cũng giống nhau

Đầu vào (input / 입력) có thể áp dụng format ngày, số, tiền tệ hoặc mask. Khi đó người dùng nhìn thấy một chuỗi đã format nhưng khung phần mềm (framework / 프레임워크) có thể giữ actual giá trị (value / 값) khác.

Ví dụ một ngày có thể được hiển thị như `2026/09/22` nhưng actual giá trị (value / 값) là `20260922`. Vì vậy khi gỡ lỗi (debug / 디버그) dữ liệu gửi máy chủ (server / 서버), hãy phân biệt:

```text
raw/actual value
        ≠
display value
        ≠
text nằm trong một DOM node cụ thể
```

Nếu API có `getValue()` và một API khác trả display-formatted giá trị (value / 값), hãy chọn theo đặc tả hợp đồng (contract / 계약) dữ liệu. máy chủ (server / 서버) thường nên nhận normalized giá trị (value / 값), không phải chuỗi trình bày cho người dùng.

> **Nối mạch:** Ở chặng này của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **2. Giá trị thật và giá trị hiển thị không phải lúc nào cũng giống nhau** đặt tiêu chí; **3. sự kiện (event / 이벤트) handler nên là ranh giới (boundary / 경계) adapter** dùng tiêu chí đó để kiểm tra ranh giới, rồi **4. sự kiện (event / 이벤트) trước và sau thay đổi có ngữ nghĩa (semantics / 의미론) khác nhau** mở rộng hệ quả.

## 3. sự kiện (event / 이벤트) handler nên là ranh giới (boundary / 경계) adapter

Một sự kiện (event / 이벤트) handler tốt thường rất ngắn:

```javascript
scwin.btnSearch_onclick = function () {
    scwin.searchUsers();
};
```

Sau đó orchestration nằm ở hàm (function / 함수) có tên theo nghiệp vụ:

```javascript
scwin.searchUsers = function () {
    if (!scwin.validateSearch()) {
        return;
    }

    $p.executeSubmission(sbmSearchUser);
};
```

Mẫu (pattern / 패턴) này có ba lợi ích. Thứ nhất, UI sự kiện (event / 이벤트) không chứa toàn bộ nghiệp vụ. Thứ hai, hàm (function / 함수) có thể được gọi lại từ keyboard shortcut, popup callback hoặc kiểm thử (test / 테스트) harness. Thứ ba, dấu vết ngăn xếp (stack trace / 스택 트레이스) và log có tên có ý nghĩa.

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

Khi một sự kiện (event / 이벤트) handler trở thành nơi mọi thứ xảy ra, coupling giữa UI và nghiệp vụ (business / 비즈니스) luồng (flow / 흐름) tăng rất nhanh.

> **Nối mạch:** Đặt trong câu hỏi lớn của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **3. sự kiện (event / 이벤트) handler nên là ranh giới (boundary / 경계) adapter** đặt tiêu chí; **4. sự kiện (event / 이벤트) trước và sau thay đổi có ngữ nghĩa (semantics / 의미론) khác nhau** dùng tiêu chí đó để kiểm tra ranh giới, rồi **5. Binding: nối UI với mô hình (model / 모델)** mở rộng hệ quả.

## 4. sự kiện (event / 이벤트) trước và sau thay đổi có ngữ nghĩa (semantics / 의미론) khác nhau

Nhiều thành phần (component / 컴포넌트)/dữ liệu (data / 데이터) đối tượng (object / 객체) có sự kiện (event / 이벤트) dạng “before thay đổi (change / 변경)” và “after thay đổi (change / 변경)”. Đây không chỉ là khác tên. sự kiện (event / 이벤트) trước thay đổi thường cho phép kiểm tra hoặc chặn mutation; sự kiện (event / 이벤트) sau thay đổi phù hợp để phản ứng sau khi trạng thái (state / 상태) đã đổi.

Ví dụ với DataList, một `onbeforecelldatachange` có thể return `false` để từ chối thay đổi. mô hình tư duy (mental model / 사고 모델) là:

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

Nếu kiểm tra hợp lệ (validation / 검증) cần ngăn dữ liệu invalid vào mô hình (model / 모델), before-event thường phù hợp hơn. Nếu lô-gic (logic / 논리) cần tính lại tổng sau khi giá trị (value / 값) đã được lần ghi nhận (commit / 커밋), after-event phù hợp hơn.

> **Nối mạch:** Event semantics xác định thời điểm trước/sau change; binding tiếp theo nối UI với model, nên source of truth phải được chọn để tránh duplicated state.

## 5. Binding: nối UI với mô hình (model / 모델)

Binding là cơ chế làm cho thành phần (component / 컴포넌트) đọc/ghi dữ liệu qua DataCollection thay vì mỗi thành phần (component / 컴포넌트) giữ một bản sao dữ liệu độc lập.

Ví dụ đầu vào (input / 입력) có thể bind với một key trong DataMap. API công khai (public API / 공개 API) của đầu vào (input / 입력) cho phép đặt tham chiếu (reference / 참조) dạng:

```javascript
inputName.setRef("data:dmUser.name");
```

Mô hình tư duy (mental model / 사고 모델):

```text
Input component
      ⇅
binding contract
      ⇅
DataMap key
```

Nếu GridView bind với DataList, GridView là view còn DataList là mô hình dữ liệu (data model / 데이터 모델). Đây là distinction rất quan trọng. Khi cần sửa nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터), ưu tiên lập luận (reasoning / 추론) trên DataList; khi cần đổi cách hiển thị, ưu tiên GridView.

> **Nối mạch:** Ở chặng này của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **5. Binding: nối UI với mô hình (model / 모델)** đặt vấn đề; **6. nguồn chuẩn (source of truth / 정본) và duplicated trạng thái (state / 상태)** đối chiếu bằng chứng, rồi **7. kiểm tra hợp lệ (validation / 검증) có nhiều tầng** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. nguồn chuẩn (source of truth / 정본) và duplicated trạng thái (state / 상태)

Giả sử màn hình có:

```text
inputUserId
hiddenUserId
scwin.selectedUserId
dmUser.userId
```

Nếu cả bốn đều giữ cùng một giá trị, hệ thống đang có bốn nguồn chuẩn (source of truth / 정본) giả. Một handler cập nhật (update / 업데이트) ba chỗ nhưng quên chỗ thứ tư là đủ tạo bug.

Mẫu (pattern / 패턴) tốt hơn là chọn một mô hình (model / 모델) chính, ví dụ `dmUser.userId`, rồi để đầu vào (input / 입력) bind vào mô hình (model / 모델). `scwin` chỉ giữ trạng thái (state / 상태) không thuộc nghiệp vụ (business / 비즈니스) mô hình (model / 모델), ví dụ `isSaving`, `currentMode` hoặc bộ nhớ đệm (cache / 캐시) tạm cho orchestration.

Một quy tắc (rule / 규칙) thực dụng:

```text
Dữ liệu cần submit / bind / track thay đổi → DataCollection
UI presentation state → component
Transient orchestration state → scwin
Persistent business truth → server
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **6. nguồn chuẩn (source of truth / 정본) và duplicated trạng thái (state / 상태)** đặt vấn đề; **7. kiểm tra hợp lệ (validation / 검증) có nhiều tầng** đối chiếu bằng chứng, rồi **8. readOnly, disabled, hidden không đồng nghĩa authorization** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. kiểm tra hợp lệ (validation / 검증) có nhiều tầng

Kiểm tra hợp lệ (validation / 검증) phía máy khách (client / 클라이언트) giúp UX tốt hơn nhưng không tạo ranh giới bảo mật (security boundary / 보안 경계). Có thể chia kiểm tra hợp lệ (validation / 검증) thành bốn tầng.

**Input-format kiểm tra hợp lệ (validation / 검증)** kiểm tra ký tự, độ dài, mẫu (pattern / 패턴), date/number format.

**Cross-field kiểm tra hợp lệ (validation / 검증)** kiểm tra quan hệ giữa nhiều đầu vào (input / 입력), ví dụ `startDate <= endDate`.

**lĩnh vực (domain / 도메인) kiểm tra hợp lệ (validation / 검증)** kiểm tra nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙), ví dụ amount không vượt hạn mức.

**máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증)** là tầng bắt buộc cho dữ liệu không đáng tin cậy và quy tắc (rule / 규칙) liên quan authorization/giao dịch (transaction / 트랜잭션).

WebSquare thành phần (component / 컴포넌트) có kiểm tra hợp lệ (validation / 검증) API và thuộc tính (property / 속성) hỗ trợ nhiều trường hợp (case / 사례) UI. Tuy nhiên đừng biến máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) thành nơi duy nhất bảo vệ nghiệp vụ.

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

Máy chủ (server / 서버) vẫn phải validate đầu vào (input / 입력) thật sự nhận được.

> **Nối mạch:** Validation nhiều tầng bảo vệ input nhưng không cấp quyền; `readOnly`/`disabled`/`hidden` chỉ là UI hints, vì vậy naming tiếp theo phải làm rõ contract và ownership.

## 8. `readOnly`, `disabled`, `hidden` không đồng nghĩa authorization

Một trường dữ liệu (field / 필드) `readOnly` chỉ ngăn người dùng (user / 사용자) sửa qua UI thông thường. `disabled` chỉ thay tương tác (interaction / 상호작용) của thành phần (component / 컴포넌트). `hidden` chỉ làm nó không hiển thị.

Không giá trị nào trong ba thứ trên chứng minh người dùng (user / 사용자) không thể gửi yêu cầu (request / 요청) khác bằng DevTools hoặc HTTP máy khách (client / 클라이언트). Authorization phải ở máy chủ (server / 서버).

Mô hình tư duy (mental model / 사고 모델):

```text
UI restriction = trải nghiệm và guardrail
Server authorization = security control
```

Đây là nguyên tắc web bảo mật (security / 보안) chung, không riêng WebSquare.

> **Nối mạch:** Ở chặng này của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **9. Naming là một phần của maintainability** nối từ **8. readOnly, disabled, hidden không đồng nghĩa authorization** sang **10. thành phần (component / 컴포넌트) chuyển tiếp trạng thái (state transition / 상태 전이) thay vì imperative chaos**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Naming là một phần của maintainability

Enterprise screen có thể có hàng chục thành phần (component / 컴포넌트). ID kiểu `input1`, `input2`, `grid1`, `submission1` khiến mã (code / 코드) khó đọc.

Một convention dễ lập luận (reasoning / 추론) hơn:

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

Tên nên cho biết **loại đối tượng (object / 객체) + vai trò nghiệp vụ**. Khi dấu vết ngăn xếp (stack trace / 스택 트레이스) hoặc log chỉ có ID, tên tốt giúp giảm ngữ cảnh (context / 맥락) switching.

> **Nối mạch:** Đặt trong câu hỏi lớn của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **10. thành phần (component / 컴포넌트) chuyển tiếp trạng thái (state transition / 상태 전이) thay vì imperative chaos** nối từ **9. Naming là một phần của maintainability** sang **11. vòng lặp sự kiện (event loop / 이벤트 루프) và duplicate click**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. thành phần (component / 컴포넌트) chuyển tiếp trạng thái (state transition / 상태 전이) thay vì imperative chaos

Một màn hình thường có chế độ (mode / 모드) như `VIEW`, `CREATE`, `EDIT`, `SAVING`. Anti-pattern là rải `setReadOnly`, `show`, `hide`, `setDisabled` khắp nhiều handler.

Tốt hơn là gom chuyển tiếp trạng thái (state transition / 상태 전이):

```javascript
scwin.setMode = function (mode) {
    scwin.currentMode = mode;

    var editable = mode === "CREATE" || mode === "EDIT";
    inputUserName.setReadOnly(!editable);
    btnSave.setDisabled(!editable);
};
```

Giá trị thực sự ở đây không phải hàm (function / 함수) nhỏ hơn, mà là **UI trở thành máy trạng thái (state machine / 상태 머신) có tên**. Khi bug xảy ra, bạn hỏi “page đang ở chế độ (mode / 모드) nào?” thay vì “handler nào vừa thay thuộc tính (property / 속성) gì?”.

> **Nối mạch:** Trong **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **11. vòng lặp sự kiện (event loop / 이벤트 루프) và duplicate click** nối từ **10. thành phần (component / 컴포넌트) chuyển tiếp trạng thái (state transition / 상태 전이) thay vì imperative chaos** sang **12. Programmatic thay đổi (change / 변경) và người dùng (user / 사용자) thay đổi (change / 변경) có thể phát sự kiện (event / 이벤트) khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. vòng lặp sự kiện (event loop / 이벤트 루프) và duplicate click

Nếu người dùng (user / 사용자) bấm Save hai lần nhanh, hai Submission có thể được tạo trước khi phản hồi (response / 응답) đầu tiên về. Đây là race điều kiện (condition / 조건) ở cấp UI/mạng (network / 네트워크).

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

Môi trường vận hành (production / 운영 환경) mã (code / 코드) còn cần reset flag ở lỗi (error / 오류) đường dẫn (path / 경로). Với thao tác (operation / 연산) không idempotent, máy chủ (server / 서버) cũng phải có protection phù hợp; máy khách (client / 클라이언트) guard chỉ giảm duplicate tương tác (interaction / 상호작용), không thể là guarantee duy nhất.

> **Nối mạch:** Ở chặng này của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **12. Programmatic thay đổi (change / 변경) và người dùng (user / 사용자) thay đổi (change / 변경) có thể phát sự kiện (event / 이벤트) khác nhau** nối từ **11. vòng lặp sự kiện (event loop / 이벤트 루프) và duplicate click** sang **13. Binding vòng lặp (loop / 루프) và side tác động (effect / 효과) cascade**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Programmatic thay đổi (change / 변경) và người dùng (user / 사용자) thay đổi (change / 변경) có thể phát sự kiện (event / 이벤트) khác nhau

Khung phần mềm (framework / 프레임워크) UI thường phân biệt thay đổi do người dùng (user / 사용자) thao tác và thay đổi bằng API. Ví dụ trong dòng WebSquare mới, `setValue()` có thể kích hoạt một số sự kiện (event / 이벤트) nhưng không kích hoạt sự kiện (event / 이벤트) dành riêng cho view/người dùng (user / 사용자) tương tác (interaction / 상호작용).

Do đó đừng dựa vào giả định “setValue chắc chắn giống người dùng (user / 사용자) gõ”. Nếu lô-gic (logic / 논리) phụ thuộc sự kiện (event / 이벤트) cụ thể, kiểm tra API tham chiếu (reference / 참조) của đúng thành phần (component / 컴포넌트)/bản dựng (build / 빌드).

Một mẫu (pattern / 패턴) an toàn hơn là đưa nghiệp vụ (business / 비즈니스) reaction vào hàm (function / 함수) rõ ràng:

```javascript
scwin.applyCustomer = function (customer) {
    inputCustomerId.setValue(customer.id);
    inputCustomerName.setValue(customer.name);
    scwin.refreshCustomerDependentState();
};
```

Thay vì hy vọng chuỗi sự kiện (event / 이벤트) side tác động (effect / 효과) tự chạy đúng khi set nhiều trường dữ liệu (field / 필드).

> **Nối mạch:** Đặt trong câu hỏi lớn của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **13. Binding vòng lặp (loop / 루프) và side tác động (effect / 효과) cascade** nối từ **12. Programmatic thay đổi (change / 변경) và người dùng (user / 사용자) thay đổi (change / 변경) có thể phát sự kiện (event / 이벤트) khác nhau** sang **14. thành phần (component / 컴포넌트) coupling giữa page**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Binding vòng lặp (loop / 루프) và side tác động (effect / 효과) cascade

Nếu A thay đổi (change / 변경) cập nhật B, B thay đổi (change / 변경) cập nhật C, C thay đổi (change / 변경) lại cập nhật A, bạn đã tạo vòng phản hồi (feedback loop / 피드백 루프). khung phần mềm (framework / 프레임워크) có thể suppress một số sự kiện (event / 이벤트) nhưng không nên dựa vào hành vi (behavior / 동작) ngầm.

Hãy thiết kế phụ thuộc (dependency / 의존성) một chiều nếu có thể:

```text
source model
   ↓
derived calculation
   ↓
UI rendering
```

Nếu bắt buộc two-way binding, side tác động (effect / 효과) không nên quay lại ghi (write / 쓰기) nguồn (source / 소스) mà không có guard.

> **Nối mạch:** Trong **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **14. thành phần (component / 컴포넌트) coupling giữa page** nối từ **13. Binding vòng lặp (loop / 루프) và side tác động (effect / 효과) cascade** sang **15. CSS và thành phần (component / 컴포넌트) internals**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. thành phần (component / 컴포넌트) coupling giữa page

Một page con gọi trực tiếp thành phần (component / 컴포넌트) của page cha:

```javascript
$p.parent().inputMainStatus.setValue("DONE");
```

Cách này chạy nhưng coupling cao. Page con biết ID và hiện thực (implementation / 구현) của cha. Nếu cha đổi bố cục (layout / 레이아웃)/thành phần (component / 컴포넌트), page con hỏng.

Tốt hơn là expose hàm (function / 함수) ở ranh giới (boundary / 경계):

```javascript
// parent
scwin.setStatus = function (status) {
    inputMainStatus.setValue(status);
};

// child
$p.parent().scwin.setStatus("DONE");
```

Tốt hơn nữa trong luồng (flow / 흐름) phức tạp là truyền callback đặc tả hợp đồng (contract / 계약) hoặc dữ liệu (data / 데이터)/kết quả (result / 결과) đặc tả hợp đồng (contract / 계약) rõ ràng. Chapter phạm vi (scope / 범위) sẽ nói kỹ hơn.

> **Nối mạch:** Ở chặng này của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **15. CSS và thành phần (component / 컴포넌트) internals** nối từ **14. thành phần (component / 컴포넌트) coupling giữa page** sang **16. sự kiện (event / 이벤트) delegation không phải lúc nào cũng cần tự viết**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. CSS và thành phần (component / 컴포넌트) internals

Khi phạm vi (scope / 범위)/WFrame được dùng, engine có thể biến đổi DOM ID. Vì vậy CSS dựa lớp (class / 클래스) thường bền hơn CSS dựa vật lý (physical / 물리적) ID. Ngoài ra thành phần (component / 컴포넌트) có thể kết xuất (render / 렌더링) nested cấu trúc (structure / 구조), nên selector quá sâu như:

```css
#someGeneratedId > div > span > input { ... }
```

rất fragile.

Ưu tiên ngữ nghĩa (semantic / 의미적) lớp (class / 클래스) do ứng dụng (application / 애플리케이션) kiểm soát. Nếu cần style vùng nội bộ (internal / 내부) thành phần (component / 컴포넌트), ghi rõ đây là phụ thuộc (dependency / 의존성) vào renderer phiên bản (version / 버전) và có visual regression kiểm thử (test / 테스트) sau engine upgrade.

> **Nối mạch:** Đặt trong câu hỏi lớn của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **16. sự kiện (event / 이벤트) delegation không phải lúc nào cũng cần tự viết** nối từ **15. CSS và thành phần (component / 컴포넌트) internals** sang **17. dữ liệu (data / 데이터) binding và GridView: preview cho chapter sau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. sự kiện (event / 이벤트) delegation không phải lúc nào cũng cần tự viết

Trong JavaScript thuần, sự kiện (event / 이벤트) delegation thường giúp xử lý nhiều nút (node / 노드) động. Trong WebSquare, thành phần (component / 컴포넌트) khung phần mềm (framework / 프레임워크) đã quản lý sự kiện (event / 이벤트) tầng (layer / 계층) cho nhiều UI đối tượng (object / 객체). Đừng tự thêm một toàn cục (global / 전역) DOM listener chỉ vì quen mẫu (pattern / 패턴) từ vanilla JS nếu thành phần (component / 컴포넌트) sự kiện (event / 이벤트) đã cung cấp đặc tả hợp đồng (contract / 계약) tốt hơn.

Mỗi tầng (layer / 계층) listener bổ sung có thể gây double handling, khó dấu vết (trace / 추적) stopPropagation và bypass phạm vi (scope / 범위) ngữ nghĩa (semantics / 의미론).

> **Nối mạch:** Trong **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **16. sự kiện (event / 이벤트) delegation không phải lúc nào cũng cần tự viết** đặt vấn đề; **17. dữ liệu (data / 데이터) binding và GridView: preview cho chapter sau** đối chiếu bằng chứng, rồi **18. Debugging checklist cho thành phần (component / 컴포넌트)/sự kiện (event / 이벤트)/binding** mở rộng hệ quả hoặc giới hạn liên quan.

## 17. dữ liệu (data / 데이터) binding và GridView: preview cho chapter sau

Khi DataList bind với GridView, bạn có thể đọc dữ liệu từ DataList:

```javascript
var count = dlUser.getRowCount();
var userId = dlUser.getCellData(0, "USER_ID");
var row = dlUser.getRowJSON(0);
```

Điều quan trọng là GridView không phải nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) store. Nếu Grid chỉ là view của `dlUser`, mã (code / 코드) save nên lập luận (reasoning / 추론) trên `dlUser` và row status của nó.

> **Nối mạch:** Ở chặng này của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **17. dữ liệu (data / 데이터) binding và GridView: preview cho chapter sau** đặt vấn đề; **18. Debugging checklist cho thành phần (component / 컴포넌트)/sự kiện (event / 이벤트)/binding** đối chiếu bằng chứng, rồi **19. cấp cao (senior / 시니어) rà soát (review / 검토) questions** mở rộng hệ quả hoặc giới hạn liên quan.

## 18. Debugging checklist cho thành phần (component / 컴포넌트)/sự kiện (event / 이벤트)/binding

Khi UI không phản ứng đúng, đi theo chuỗi xử lý (pipeline / 파이프라인):

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

Đặt breakpoint ở handler, inspect thành phần (component / 컴포넌트) API giá trị (value / 값) và DataCollection giá trị (value / 값) cùng lúc. Đừng chỉ nhìn UI.

> **Nối mạch:** Đặt trong câu hỏi lớn của **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **19. cấp cao (senior / 시니어) rà soát (review / 검토) questions** nối từ **18. Debugging checklist cho thành phần (component / 컴포넌트)/sự kiện (event / 이벤트)/binding** sang **20. Kết nối**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. cấp cao (senior / 시니어) rà soát (review / 검토) questions

Khi rà soát (review / 검토) một màn hình, hãy hỏi:

“trạng thái (state / 상태) này có bị giữ ở nhiều đối tượng (object / 객체) không?”

“Handler có quá nhiều trách nhiệm không?”

“mã (code / 코드) có đang truy vấn (query / 쿼리) DOM nội bộ (internal / 내부) thay vì thành phần (component / 컴포넌트) API không?”

“kiểm tra hợp lệ (validation / 검증) này thuộc UX hay bảo mật (security / 보안)?”

“Programmatic set có đang phụ thuộc side-effect sự kiện (event / 이벤트) không rõ ràng không?”

“Page con có phụ thuộc ID của page cha quá nhiều không?”

Nếu trả lời được những câu này, bạn đang rà soát (review / 검토) kiến trúc (architecture / 아키텍처) chứ không chỉ cú pháp (syntax / 문법).

> **Nối mạch:** Trong **02 — Components, Events & dữ liệu (data / 데이터) Binding**, **20. Kết nối** nối từ **19. cấp cao (senior / 시니어) rà soát (review / 검토) questions** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 20. Kết nối

Tiếp theo: [03 — DataCollection & Submission](03_data_collection_submission.md), nơi trạng thái (state / 상태) mô hình (model / 모델) được nối với máy chủ (server / 서버) communication và row-state ngữ nghĩa (semantics / 의미론).

> **Bàn giao:** Sau **20. Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
