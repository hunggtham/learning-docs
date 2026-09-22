# 11 — Testing, Testability & Regression Engineering

WebSquare application thường được kiểm thử bằng cách mở màn hình, nhập dữ liệu rồi quan sát kết quả. Cách đó cần thiết nhưng không đủ cho một hệ thống enterprise lớn. Khi số page, WFrame, Submission, UDC và Grid tăng lên, kiểm thử thủ công không còn trả lời được câu hỏi quan trọng nhất: **thay đổi này đã phá contract nào, ở layer nào, và bằng chứng nào cho thấy behavior vẫn đúng?**

Chapter này không cố ép WebSquare vào một testing framework cụ thể. Mental model quan trọng hơn tool: tách business reasoning khỏi framework side effect, xác định observable contract, kiểm soát async/lifecycle và xây regression suite theo risk. Playwright, Selenium hay một runner nội bộ chỉ là phương tiện thực thi những contract đó.

> Prerequisite: [03 — DataCollection & Submission](03_data_collection_submission.md), [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md), [08 — Reusable Architecture](08_reusable_architecture_udc_common_modules.md) và [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md).

## 1. Test không phải là “click được”

Một màn hình có thể click được nhưng vẫn sai business state. Search button có thể gửi request nhưng gửi condition cũ. Save có thể hiện success message nhưng server đã reject một phần dữ liệu. Popup có thể mở được nhưng giữ listener sau khi đóng. Grid có thể hiển thị đúng 20 row đầu nhưng selected row identity bị sai sau sort.

Vì vậy một test tốt phải phát biểu **invariant có thể quan sát**. Ví dụ:

```text
Khi user sửa NAME của row có USER_ID=U100
→ canonical DataList row U100 mang value mới
→ row status chuyển sang trạng thái changed phù hợp
→ Save gửi đúng business identity và field được phép sửa
→ success response làm model trở về trạng thái sau-save theo contract
```

Test không nên chỉ phát biểu “click Save rồi thấy popup thành công”. UI message là một observation, không phải toàn bộ correctness.

## 2. Testing portfolio theo boundary

Không có một loại test nào phù hợp cho mọi failure mode. WebSquare screen nên được kiểm thử ở nhiều boundary khác nhau.

**Logic test** kiểm tra function gần thuần như normalize input, build request object, validate cross-field rule, map server error và quyết định enable/disable action. Đây là test rẻ, nhanh và dễ chạy nhiều case.

**Page orchestration test** kiểm tra `scwin` function điều phối DataCollection, Submission và state transition. Mục tiêu không phải giả lập toàn bộ browser mà là chứng minh page logic gọi đúng dependency và xử lý đúng result.

**Component/UDC contract test** kiểm tra public property, method và event. Consumer không cần biết internal Input/Grid/DataMap của UDC.

**Integration test** chạy page với WebSquare Engine thật hoặc environment gần thật để kiểm tra Scope, binding, lifecycle, WFrame, Submission mapping và rendering integration.

**End-to-end test** đi qua browser, HTTP và backend để chứng minh critical user journey. Nó có giá trị cao nhưng chậm và dễ flaky hơn, nên không dùng để thay tất cả test tầng dưới.

Mental model là:

```text
pure logic
→ page/component contract
→ WebSquare integration
→ browser + server journey
```

Càng xuống dưới càng gần production nhưng chi phí setup, runtime và diagnosis càng lớn.

## 3. Testability bắt đầu từ architecture

Nếu một handler 300 dòng vừa đọc component, validate, build payload, gọi Submission, format message, mở popup và sửa global state, test sẽ khó vì behavior không có seam rõ.

Một cấu trúc dễ test hơn:

```javascript
scwin.normalizeSearchCondition = function (raw) {
    return {
        userId: String(raw.userId || "").trim(),
        activeOnly: raw.activeOnly === true
    };
};

scwin.validateSearchCondition = function (condition) {
    if (condition.userId.length > 30) {
        return { ok: false, code: "USER_ID_TOO_LONG" };
    }
    return { ok: true };
};

scwin.search = function () {
    var condition = scwin.normalizeSearchCondition({
        userId: dmSearch.get("USER_ID"),
        activeOnly: dmSearch.get("ACTIVE_ONLY")
    });

    var result = scwin.validateSearchCondition(condition);
    if (!result.ok) {
        scwin.showValidationError(result);
        return;
    }

    scwin.executeSearch(condition);
};
```

`normalizeSearchCondition()` và `validateSearchCondition()` có thể được kiểm tra mà không cần Grid hay network. `search()` giữ vai trò orchestration. Đây không phải “viết code để test”; đây là tách responsibility để reasoning tốt hơn, và testability là hệ quả.

## 4. Không mock WebSquare ở mọi nơi

Mock quá ít làm test chậm và khó cô lập. Mock quá nhiều làm test chứng minh behavior của mock chứ không chứng minh WebSquare integration.

Quy tắc hữu ích là mock **boundary mà test không nhằm kiểm tra**.

Nếu đang test validator, không cần engine thật.

Nếu đang test Submission target mapping, phải có integration đủ thật để mapping chạy.

Nếu đang test WFrame lifecycle, fake `$p` quá nhiều sẽ che đúng bug cần tìm.

Nếu đang test business response mapping, backend thật có thể được thay bằng deterministic test endpoint hoặc network stub, nhưng response shape phải giống contract production.

Senior note: mock phải bảo toàn semantics quan trọng của boundary. Một fake Submission gọi callback synchronously có thể làm test xanh trong khi production callback asynchronous và có race condition.

## 5. Fixture cho DataMap và DataList

DataCollection là nơi rất phù hợp để tạo fixture có chủ đích. Đừng dùng một dump production khổng lồ cho mọi test. Fixture nên nhỏ nhưng chứa case có ý nghĩa.

Ví dụ một DataList test có thể cần:

```text
U100 — row bình thường
U101 — row có null/empty field
U102 — row sẽ bị update
U103 — row sẽ bị delete
```

Sau operation, assert theo **business key** thay vì row index. Sort/filter có thể đổi index nhưng không đổi identity.

Nếu test CRUD, cần quan sát cả value lẫn row status. Chỉ assert `NAME === "Kim"` có thể bỏ sót việc row vẫn ở status không phù hợp để Save serialize.

## 6. Row status là một state machine cần test transition

CRUD test nên xem row status như state machine, không như ký tự bí mật.

Ví dụ các transition cần kiểm chứng tùy contract/build:

```text
loaded row
→ edit
→ changed row

new row
→ edit
→ still new/insert candidate

loaded row
→ delete
→ deletion candidate retained/marked theo model semantics

save success
→ refreshed/committed state theo application policy
```

Không hard-code assumption về ký tự status nếu project wrapper đã abstract nó. Test business transition mà application dựa vào, rồi kiểm tra exact API/status theo engine build.

## 7. Submission test phải kiểm tra bốn lớp

Một Submission regression thường có bốn lớp correctness:

```text
request trigger
→ request serialization
→ response classification
→ target/state update
```

Test chỉ thấy HTTP 200 mới chứng minh transport. Một test đầy đủ hơn cần xác nhận condition đúng được serialize, error response không đi vào success flow, target DataCollection nhận đúng shape và stale response không overwrite intent mới.

Nếu save mutation có duplicate protection, test double-click hoặc repeated trigger phải chứng minh chỉ một logical operation được commit hoặc server idempotency xử lý đúng.

## 8. Async test không dùng sleep làm synchronization chính

Đây là anti-pattern phổ biến:

```javascript
clickSearch();
await sleep(1000);
expect(gridRowCount()).toBe(10);
```

Test này giả định network/render hoàn tất trong một giây. Máy CI chậm hơn sẽ flaky; máy nhanh hơn thì lãng phí thời gian.

Hãy chờ một observable condition:

```text
request cụ thể hoàn thành
DataList đạt expected state
page phát ready signal
loading indicator biến mất sau đúng operation
business result xuất hiện
```

`waitForTimeout` chỉ nên dùng khi chính timing là thứ đang test, không phải cách che thiếu lifecycle contract.

## 9. Test latest-intent và race condition

Search-as-you-type hoặc user đổi condition nhanh tạo scenario:

```text
request A gửi trước
request B gửi sau
response B về trước
response A về sau
```

Expected behavior thường là UI giữ result của intent B. Regression test nên cố tình đảo response order. Nếu chỉ test network trả theo thứ tự gửi, race bug sẽ không bao giờ xuất hiện trong CI nhưng vẫn xảy ra production.

Tương tự, test navigation race:

```text
page A gửi request
user đóng tab A
page B mở
response A về
```

Response cũ không được mutate state của page đã disposed hoặc page mới không liên quan.

## 10. WFrame và Scope test cần kiểm tra topology

Một page chạy standalone có thể pass nhưng fail khi nằm trong WFrame tầng hai. Vì vậy critical reusable page nên có ít nhất một test trong topology thật.

Cần kiểm chứng:

```text
component ID giống nhau ở hai Scope không collision
child nhận đúng parameter
child chỉ gọi public parent contract nếu contract cho phép
popup result quay đúng caller
close/reopen tạo instance sạch
setSrc/navigation không gọi child trước readiness phù hợp
```

Nếu code chỉ pass khi page là direct child của main frame, test nested topology sẽ lộ hidden dependency vào `parent().parent()`.

## 11. UDC test theo public contract

UDC tốt có thể test như một black box tương đối.

Ví dụ `EmployeePicker` có contract:

```text
property: departmentId
method: setValue(employee)
method: getValue()
event: onChange(employee)
```

Test không nên query internal `inputEmployeeName` trừ khi đang test implementation riêng. Consumer regression phải chứng minh property được áp dụng, method giữ invariant và event trả payload đúng schema.

Khi refactor internal layout từ Input + Button sang AutoComplete, contract test vẫn giữ nguyên. Đây là lợi ích trực tiếp của abstraction boundary.

## 12. End-to-end selector phải bền với rendering internals

WebSquare có thể biến đổi physical DOM ID theo Scope/rendering. Test E2E phụ thuộc selector dài kiểu:

```text
#mf_wframe1_udc1_input1_input
```

sẽ dễ vỡ khi layout thay đổi dù behavior không đổi.

Ưu tiên selector dựa trên contract ổn định: logical test hook được project quy ước, accessible name/label, role, hoặc wrapper test API. Không dựa vào private engine DOM structure nếu không bắt buộc.

Nếu cần thêm `data-*` hook cho automation, hook phải semantic và ổn định, ví dụ `data-testid="employee-search-submit"`, không phải `div-17-child-2`.

## 13. Accessibility test là functional test

Keyboard navigation, focus return sau popup, label association và error announcement không phải cosmetic detail.

Một regression scenario nên thử:

```text
Tab qua form theo thứ tự nghiệp vụ
mở popup bằng keyboard
focus chuyển vào popup
đóng popup
focus quay về trigger hợp lý
validation error có thể được nhận biết không chỉ bằng màu
```

Automation có thể hỗ trợ một phần, nhưng keyboard-only exploratory test và screen-reader verification vẫn cần cho flow quan trọng.

## 14. Internationalization test cần thay đổi dữ liệu, không chỉ locale flag

Một screen “đã hỗ trợ English” chưa được chứng minh chỉ vì locale switch hoạt động.

Test nên dùng text dài, missing key, ký tự đa byte, date/number format và label có độ dài khác nhau. Korean, Vietnamese và English tạo pressure layout khác nhau.

Fixture i18n nên có ít nhất:

```text
short label
long translated label
missing key
special character
number/date locale case
```

Mục tiêu là tìm assumption “text luôn ngắn như Korean hiện tại”.

## 15. Validation test theo boundary

Client validation có ba nhóm test khác nhau.

Input interaction test chứng minh component cho phép/chặn character theo UX rule.

Semantic validation test chứng minh business condition như `startDate <= endDate`.

Server validation integration test chứng minh payload không hợp lệ vẫn bị reject dù client guard bị bypass.

Nếu chỉ test client, bạn chưa test trust boundary. Nếu chỉ test server, UX regression có thể vẫn xảy ra.

## 16. Security negative test

Critical screen nên có negative test cho assumption bảo mật thường gặp:

```text
hidden field bị sửa bằng request manipulation
readOnly field bị gửi giá trị khác
role thấp gọi save endpoint trực tiếp
HTML-like input quay lại Grid/Output
file upload sai loại/kích thước
Excel/CSV cell có formula-like prefix
```

Kết quả đúng phải đến từ server policy và safe rendering, không từ việc button bị ẩn.

## 17. Performance regression test cần budget

Không cần biến mọi test thành benchmark. Chọn flow có risk cao như initial shell, search Grid lớn, open popup, switch tab và repeated navigation.

Đo cùng một scenario với dataset kiểm soát:

```text
click → request start
request end → DataList ready
DataList ready → interactive render
heap sau N vòng open/close
request count sau N vòng navigation
```

Regression test có giá trị khi environment đủ ổn định và threshold có ý nghĩa. Một threshold 500 ms trên CI noisy có thể tạo false alarm; trend hoặc relative comparison đôi khi phù hợp hơn absolute number.

## 18. Memory regression cần repeated lifecycle

Leak hiếm khi lộ sau một lần mở page.

Scenario tốt hơn:

```text
warm up
record baseline
open popup/tab
perform representative action
close
lặp 20–50 lần
force/await GC nếu test environment cho phép
so heap/listener/request behavior
```

Không chỉ nhìn heap tổng. Tìm retained Scope/component/listener hoặc duplicate network effect. Chapter [10](10_rendering_lazy_loading_lifetime.md) giải thích lifetime model phía sau test này.

## 19. Test data phải có ownership

E2E test dùng chung một account và một record mutable rất dễ flaky. Test A đổi record, Test B giả định record cũ.

Có ba chiến lược thường dùng:

```text
immutable reference fixture
per-test generated data
reset/cleanup transaction theo suite
```

Chọn theo backend architecture. Điều quan trọng là test biết ai tạo dữ liệu, ai được sửa và ai cleanup.

Đừng để CI phụ thuộc “database UAT hiện đang có USER_ID=TEST01”. Đó không phải fixture; đó là environmental accident.

## 20. Environment parity và deterministic config

Một test pass local nhưng fail UAT có thể do engine build, config, context root, locale, browser hoặc cache khác nhau.

Regression report nên ghi ít nhất:

```text
WebSquare engine build
browser/version
application build/artifact id
config profile
backend environment
test data version hoặc seed
```

Đây là provenance của evidence. Không có provenance, screenshot “pass” khó tái hiện.

## 21. Contract test cho response schema

Frontend thường fail không phải vì UI code đổi mà vì backend response shape đổi.

Nếu page kỳ vọng:

```json
{
  "users": [
    { "userId": "U100", "name": "Kim" }
  ]
}
```

thì contract test cần bắt các thay đổi như `userId` thành `user_id`, `users` thành `data`, hoặc nullability thay đổi.

TypeScript có thể giúp model contract nếu project dùng TypeScript, nhưng runtime response vẫn cần validation/contract evidence. Với JavaScript WebSquare, schema fixture và integration test càng quan trọng.

## 22. Error path phải được test như first-class behavior

Happy path thường được test nhiều nhất, trong khi production incident nằm ở timeout, 401/403, 500, malformed payload và partial business failure.

Một screen quan trọng nên fault-inject:

```text
network timeout
HTTP error
business error với HTTP 200
malformed/missing field
slow response
response out of order
session expiration
```

Sau mỗi lỗi, assert cả UI state: loading indicator có tắt không, button có được enable lại không, DataList cũ có bị xóa sai không, user có thể retry không.

## 23. Test debug menu và runtime evidence trong exploratory testing

WebSquare5 SP5 có debug context menu cho log, DataCollection, event và Submission ở các configuration tương ứng. Khi exploratory test phát hiện lỗi, dùng các view này cùng Browser DevTools để capture state trước khi refresh.

Một bug report tốt không chỉ có “Search không chạy”. Nó có thể ghi:

```text
handler đã fire
Submission object tồn tại
Network không có request
DataMap condition = {...}
engine build = ...
console exception = ...
```

Như vậy developer bắt đầu từ boundary đã khoanh vùng thay vì tái hiện mù.

## 24. CI pipeline: fail càng sớm càng rẻ

Một pipeline hợp lý thường đi từ kiểm tra rẻ đến đắt:

```text
syntax/static checks
→ pure logic tests
→ build/W-Pack validation
→ component/page integration
→ critical E2E smoke
→ broader regression
→ performance/security suites theo lịch hoặc release gate
```

W-Pack có stand-alone module phục vụ CI/server-side batch conversion trong SP5, vì vậy build artifact không nhất thiết phụ thuộc thao tác thủ công trong Studio. Chapter [12](12_build_config_deployment.md) đi sâu source-to-artifact pipeline.

## 25. Smoke test sau deploy

Deploy thành công không đồng nghĩa application usable. Smoke test nên đi qua một số contract có khả năng phát hiện config/artifact lỗi nhanh:

```text
shell load
login/session nếu thuộc scope test
một WFrame child load
một Submission GET/query
một Grid render
một popup open/close
một static/common resource từ _wpack_
```

Nếu release có migration lớn, thêm flow đặc thù như UDC, Excel hoặc multilingual resource.

## 26. Regression suite theo risk, không theo số màn hình

Không cần một E2E test đầy đủ cho mọi page nếu nhiều page chỉ lặp cùng pattern. Ưu tiên theo:

```text
business criticality
change frequency
complexity/lifecycle risk
historical defect density
shared component blast radius
security/data sensitivity
```

Một UDC dùng ở 80 screen có thể đáng được test sâu hơn một page độc lập ít dùng.

## 27. Flaky test là defect của test system

Một test fail ngẫu nhiên làm team mất niềm tin. Đừng chỉ retry đến xanh.

Root cause thường là:

```text
sleep-based synchronization
shared mutable test data
selector phụ thuộc DOM internals
network/environment không kiểm soát
animation/render timing
test order dependency
cleanup thiếu
```

Retry có thể dùng để thu thập evidence tạm thời, nhưng không được biến nondeterminism thành “pass”.

## 28. Anti-pattern: assert implementation detail

Ví dụ test rằng `scwin.tempFlag === 2` trong khi business contract chỉ cần Save button disabled. Refactor nội bộ sẽ làm test vỡ dù behavior đúng.

Test nên bám vào public contract hoặc invariant. Implementation-level test chỉ hợp lý khi implementation đó chính là thứ cần bảo vệ, ví dụ row-status transition hoặc serialization adapter.

## 29. Anti-pattern: một E2E khổng lồ cho cả ngày làm việc

Một script login → search → edit → popup → export → logout dài hàng trăm bước có diagnosis kém. Step 87 fail không biết root cause nằm ở state từ step nào.

Tách journey theo bounded capability, nhưng giữ một số end-to-end critical path ngắn để chứng minh integration xuyên hệ thống.

## 30. Practical test matrix cho màn hình CRUD

Một màn hình query/edit/save nên có regression matrix tối thiểu theo reasoning sau.

**Search** phải chứng minh condition mapping, empty result, large result, server error và stale-response ordering.

**Edit** phải chứng minh canonical DataList thay đổi, row identity ổn định sau sort/filter và validation không duplicate giữa handler.

**Save** phải chứng minh changed rows được gửi đúng, double-click không tạo duplicate logical transaction, business error giữ UI recoverable và success state được refresh/commit đúng policy.

**Popup** phải chứng minh parameter/result contract, focus return và repeated open/close không leak.

**Lifecycle** phải chứng minh close/navigate khi request pending không gây stale mutation.

Đây là matrix theo failure mode, không phải checklist API.

## 31. Senior note: testability là chỉ báo coupling

Nếu muốn test một rule nhỏ nhưng phải boot toàn bộ app shell, mở ba WFrame và kết nối server thật, rule đó đang nằm quá sâu trong framework coupling.

Nếu muốn test một UDC nhưng phải biết năm internal component ID, public contract của UDC chưa đủ rõ.

Nếu muốn test page B nhưng phải tạo global state từ page A, hai page đang có hidden coupling.

Testing vì vậy không chỉ bắt bug. Nó cho feedback về architecture.

## 32. Mental model cuối chapter

Một regression strategy tốt có thể tóm tắt:

```text
business invariant
→ observable contract
→ smallest useful test boundary
→ deterministic fixture
→ controlled async/lifecycle
→ production-like integration ở nơi cần
→ evidence khi fail
```

Khi test fail, câu hỏi đầu tiên không phải “retry có pass không?”. Hãy hỏi contract nào vừa bị phá, evidence nằm ở layer nào và test có đang quan sát đúng source of truth không.

## Nguồn đối chiếu

WebSquare5 SP5 Development Guide mô tả debug context menu, DataCollection/Submission inspection, W-Pack và lifecycle behavior. Stand-alone W-Pack được tài liệu chính thức mô tả như cơ chế có thể tích hợp CI/server batch build. Testing framework cụ thể không phải canonical WebSquare API; hãy chọn theo browser/toolchain của project và giữ test dựa trên public WebSquare/application contract thay vì private engine DOM.