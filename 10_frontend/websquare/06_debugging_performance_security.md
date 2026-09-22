# 06 — Debugging, Performance, Security & Production

## 1. Production reasoning bắt đầu bằng evidence

WebSquare screen có nhiều lớp abstraction, vì vậy debug bằng cách thêm `alert()` ngẫu nhiên rất nhanh đạt giới hạn. Một incident nên được phân tích như pipeline có evidence:

```text
user action
→ event handler
→ page state/DataCollection
→ Submission/request
→ server
→ response
→ target mapping
→ component rendering
```

Mỗi mũi tên là một boundary có thể đo hoặc inspect. Khi biết boundary nào sai, search space giảm mạnh.

## 2. DevTools là công cụ chính, không phải last resort

Browser DevTools vẫn là nền tảng dù framework dùng nhiều abstraction.

**Console** dùng để inspect `scwin`, component object, DataMap/DataList và exception.

**Sources** dùng breakpoint, call stack, scope variable và source map nếu project có.

**Network** xác nhận request URL, timing, payload, header, status, response body và duplicate request.

**Performance** xác định long task, scripting/layout/rendering cost.

**Memory** giúp tìm detached object, heap growth và reference leak.

Framework Studio debugger hữu ích, nhưng production evidence trong browser mới phản ánh môi trường thật.

## 3. Debug theo binary search trên pipeline

Ví dụ “Search không ra kết quả”. Đừng đọc toàn bộ code trước.

Bước 1: Network có request không?

Nếu **không**, lỗi nằm trước network: event, validation, Scope hoặc Submission execution.

Nếu **có**, response có data không?

Nếu **không**, xem server/request condition.

Nếu **có**, DataList target có data không?

Nếu **không**, mapping/target issue.

Nếu **có**, Grid có bind đúng không?

Cách chia đôi pipeline nhanh hơn debug theo file.

## 4. Scope debugging

Khi thấy element trên màn hình nhưng không biết object thuộc frame nào, resolve Scope trước. Một số SP5 build có debug utility như:

```javascript
$p.debug.getScope($0);
$p.debug.getFrame($0);
```

`$0` là DOM element đang được chọn trong DevTools Elements.

Mental workflow:

```text
visual element
→ DOM element
→ WebSquare frame/scope
→ component object
→ scwin/DataCollection
```

Đây là cách đặc biệt hữu ích trong TabControl/WindowContainer nhiều tầng.

## 5. Log có context, không log chuỗi vô nghĩa

Sai:

```javascript
console.log("here1");
console.log("here2");
```

Tốt hơn:

```javascript
console.log("[user-search] execute", {
    condition: dmSearch.getJSON ? dmSearch.getJSON() : null,
    requestId: scwin.requestId
});
```

Trong production, tránh log PII, token, password hoặc full response nhạy cảm. Logging phải vừa đủ để correlation nhưng không biến console/log server thành data leak.

## 6. Correlation ID

Nếu một user action đi qua browser → API gateway → application server → DB, correlation ID giúp nối log.

```text
browser request id
→ HTTP header
→ server log
→ downstream log
```

Client có thể generate/request ID theo convention của hệ thống, nhưng security/tracing architecture phải thống nhất server-side. Đừng tự phát minh header nếu gateway đã cung cấp trace ID.

## 7. Submission timing

Khi màn hình chậm, đo các đoạn riêng:

```text
T_click_to_request
T_network_wait
T_response_download
T_mapping
T_render
```

Nếu request bắt đầu 800 ms sau click, client script/validation đang chậm.

Nếu waiting 4 s, server/network là nghi phạm chính.

Nếu response về nhanh nhưng UI freeze 2 s, DataCollection/Grid rendering là trọng tâm.

## 8. Performance budget thay vì “cảm giác chậm”

Định nghĩa budget theo screen quan trọng, ví dụ:

```text
search click → request start < 100 ms
API p95 < 1 s
response → interactive grid < 500 ms
main-thread task < 50 ms khi có thể
```

Con số thực tế phụ thuộc hệ thống. Điểm quan trọng là có measurement target. Không có budget, team chỉ tranh luận bằng cảm giác.

## 9. Grid rendering cost

Grid lớn có thể chậm vì:

```text
quá nhiều row trả về
cell formatter nặng
nhiều merged cell/style dynamic
per-cell event
DOM/layout cost
repeated redraw
summary calculation lặp
```

Optimization tốt thường bắt đầu ở data volume và algorithm trước khi micro-optimize từng API.

## 10. Tránh synchronous heavy loop trong event handler

JavaScript chạy trên main thread cho phần lớn UI work. Nếu click handler scan hàng trăm nghìn cell synchronously, browser không thể paint/respond trong lúc đó.

Ví dụ O(n²):

```javascript
for (var i = 0; i < count; i++) {
    for (var j = 0; j < count; j++) {
        // duplicate search
    }
}
```

Dùng Set/Map có thể đổi thành gần O(n):

```javascript
var seen = new Set();
for (var i = 0; i < count; i++) {
    var id = dlUser.getCellData(i, "USER_ID");
    if (seen.has(id)) {
        return false;
    }
    seen.add(id);
}
```

Kiến thức complexity nằm ở Computer Science canonical docs; WebSquare không thay đổi Big-O.

## 11. Debounce và search-as-you-type

Nếu Input change mỗi ký tự đều gọi Submission, user gõ 10 ký tự tạo 10 request. Debounce có thể hợp lý cho autocomplete/search suggestion.

Nhưng debounce không thay abort/stale-response protection. Request cũ có thể vẫn về sau request mới.

Tách hai vấn đề:

```text
debounce → giảm số request
cancellation/request identity → bảo vệ ordering
```

## 12. Cache có invalidation cost

Common code đôi khi cache code list, menu hoặc reference data để giảm request. Cache chỉ đúng khi biết lifetime và invalidation.

```text
static code list trong session → cache tốt
user permission có thể đổi → cần refresh policy
transaction data → thường không cache global tùy tiện
```

Cache global trong SPA sống lâu; stale state có thể kéo dài hàng giờ.

## 13. Memory leak trong SPA

Dấu hiệu:

```text
mở/đóng cùng screen 20 lần → heap tăng liên tục
handler cũ vẫn chạy
request duplicate tăng sau mỗi navigation
```

Nguồn phổ biến:

```text
window/document event listener không remove
timer không clear
global array giữ scope/component
closure giữ DataList lớn
third-party widget không destroy
```

Test leak bằng repeatable navigation scenario và heap snapshot, không bằng một lần mở page.

## 14. Timer lifecycle

Nếu page dùng timer:

```javascript
scwin.timerId = setInterval(function () {
    scwin.refreshStatus();
}, 30000);
```

phải xác định cleanup khi page đóng/chuyển. Nếu WebSquare cung cấp timer utility gắn lifecycle, ưu tiên contract đó; nếu dùng browser timer, tự quản cleanup rõ.

Timer orphan tạo duplicate request và giữ reference vào page.

## 15. XSS: escape output nhưng hiểu context

Cross-site scripting (XSS / 크로스 사이트 스크립팅) xảy ra khi dữ liệu không đáng tin được interpret như code/markup.

Một Input/Grid property có `escape` option ở một số component/build, nhưng đừng coi một property là lá chắn toàn cục. Escape phải đúng context:

```text
HTML text
HTML attribute
JavaScript string
URL
CSS
```

Không dùng `innerHTML`/HTML-rendering mode cho user-controlled data trừ khi sanitize bằng cơ chế được phê duyệt.

## 16. `eval` và dynamic function execution

Legacy WebSquare pattern đôi khi truyền callback name dạng string và `eval`. `eval` làm code khó audit và mở injection risk nếu string chịu ảnh hưởng từ external input.

Rule:

```text
Không eval dữ liệu từ user/server.
Nếu legacy callback bắt buộc, dùng allowlist function name nội bộ.
Ưu tiên direct function contract khi có thể.
```

## 17. Client-side hidden/readOnly không bảo vệ dữ liệu

Một field role `ADMIN` bị hidden vẫn có thể bị sửa bằng DevTools nếu request trust client payload.

Server phải whitelist writable fields:

```text
client sends USER_ID, NAME, ROLE
server knows caller may edit NAME only
→ ignore/reject ROLE change
```

Authorization không được delegate cho WebSquare UI.

## 18. CSRF, session và authentication

WebSquare Submission vẫn là HTTP request. Nếu app dùng cookie session, Cross-Site Request Forgery (CSRF / 사이트 간 요청 위조) vẫn là threat tùy architecture.

Protection có thể gồm same-site cookie, CSRF token, origin checks hoặc framework security mechanism. Implementation thuộc server/security stack, không phải “WebSquare tự lo”.

## 19. Sensitive data trong DataCollection

DataCollection ở browser có thể inspect. Không đưa secret server-side, private key, database credential hoặc access control rule nhạy cảm vào client model.

Token/session data nếu buộc phải ở client phải theo security architecture của hệ thống. `hidden=true` không làm secret.

## 20. File upload

File upload cần kiểm tra server-side:

```text
size
extension và MIME
magic bytes/content
malware policy
storage path
filename normalization
authorization
```

Client validation chỉ để UX. Filename do user cung cấp không được dùng trực tiếp làm server path.

## 21. Excel injection

Nếu export dữ liệu user-controlled sang Excel/CSV, cell bắt đầu bằng `=`, `+`, `-`, `@` có thể được spreadsheet interpret như formula tùy format/application.

Nếu hệ thống xuất file cho user khác mở, cần xem xét formula injection policy. Đây là security boundary thường bị bỏ qua ở enterprise grid export.

## 22. Error message không nên leak internals

Server stack trace, SQL, table name, filesystem path không nên hiện nguyên cho end user.

Client có thể log correlation ID và hiển thị message phù hợp:

```text
“처리 중 오류가 발생했습니다. 문의 시 오류번호 ABC-123을 알려 주세요.”
```

Developer tra server log bằng ID.

## 23. Retry chỉ an toàn khi hiểu idempotency

Search GET-like operation thường retry dễ hơn Save mutation.

Nếu retry Save sau timeout, request đầu có thể đã commit nhưng response mất. Request thứ hai có thể duplicate transaction.

Với operation quan trọng, server nên có idempotency strategy hoặc transaction key phù hợp. Client không tự động retry mutation một cách mù quáng.

## 24. Timeout là product decision

Timeout quá ngắn tạo false failure; quá dài làm user treo. Chọn dựa endpoint SLO và UX. Khi timeout, UI phải cho biết operation state và khả năng retry.

Nếu state server không chắc chắn, message “save failed” có thể sai; có thể cần “không xác định kết quả, hãy kiểm tra lại”.

## 25. Config và environment drift

WebSquare project có client/server config, resource path và engine setting. Local, UAT và production có thể khác.

Một bug chỉ có production nên audit:

```text
engine build
config.xml/client config
server config
context root
resource cache/CDN
browser support
security header
reverse proxy path
```

Không giả định source code giống nhau thì runtime behavior giống nhau.

## 26. Cache busting và stale artifact

W-Pack tạo JavaScript artifact. Nếu deploy XML/source mới nhưng browser/CDN vẫn giữ JS artifact cũ, user có thể chạy code khác source bạn đang đọc.

Khi bug “máy tôi sửa rồi nhưng user vẫn thấy cũ”, kiểm tra:

```text
artifact thực deploy
response cache headers
service worker nếu có
CDN/proxy cache
browser cache
versioned resource URL
```

## 27. Source map và minification

Production artifact có thể minify/obfuscate. Source map giúp stack trace quay về source dễ hơn nhưng có security/deployment trade-off. Có thể giữ source map private cho observability thay vì public nếu policy yêu cầu.

Đừng debug production minified stack bằng cách đoán nếu build pipeline có thể cung cấp mapping.

## 28. Browser compatibility

WebSquare engine hỗ trợ browser matrix theo version. Project legacy có thể còn IE-specific code; modern deployment thường evergreen browser.

Đừng giữ polyfill/workaround chỉ vì “WebSquare cũ từng cần”. Xác định browser support policy hiện tại rồi loại dead compatibility code có kiểm soát.

## 29. Accessibility

Enterprise app vẫn cần accessibility (접근성 / khả năng tiếp cận). Grid, form, popup và keyboard flow phải dùng semantic label/tab order/focus management phù hợp.

Component property hỗ trợ accessibility nhưng application logic vẫn phải đảm bảo:

```text
focus sau popup mở/đóng
keyboard navigation
error announcement
label association
contrast
no keyboard trap
```

## 30. Observability của page quan trọng

Một screen critical có thể instrument:

```text
screen load duration
search request latency
save success/failure rate
client exception count
large result size
popup load error
```

Không cần log mọi click. Chọn signal giúp vận hành.

## 31. Incident example: Save bị duplicate ngẫu nhiên

Triệu chứng: database đôi lúc có hai record.

Đi theo evidence:

1. Network trace cho thấy hai request giống nhau cách nhau 80 ms.
2. Click handler log cũng chạy hai lần.
3. Button chưa disable cho đến sau một async validation callback.
4. User double-click tạo hai flow song song.

Client fix: set in-flight guard ngay khi operation bắt đầu.

Server fix: unique constraint/idempotency/transaction invariant để duplicate không thể commit nếu business không cho phép.

Bài học: client fix UX, server fix correctness.

## 32. Incident example: Screen càng dùng lâu càng chậm

Evidence:

1. Fresh reload: 1 request mỗi 30 s.
2. Sau 10 lần mở/đóng tab: 10 request mỗi 30 s.
3. Heap snapshot giữ 10 scope instance cũ.
4. Mỗi page start `setInterval` nhưng không clear.

Fix nằm ở lifecycle cleanup, không ở API server.

## 33. Production readiness checklist

Trước release screen quan trọng:

```text
No duplicate submission on double click
All error paths restore UI state
Authorization enforced server-side
Sensitive data not logged
Large dataset tested
SPA open/close leak tested
Network failure tested
Slow server tested
Popup/frame race tested
Browser matrix tested
Accessibility basics checked
Cache/deploy artifact verified
```

## 34. Kết nối

Production code thường sống lâu qua nhiều WebSquare generation. Chapter cuối giúp đọc và migrate code cũ mà không phá semantics: [07 — Legacy, Modern Evolution & Migration](07_legacy_modern_migration.md).
