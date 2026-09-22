# 18 — Hybrid App, WebView & Native Bridge

## 1. Hybrid WebSquare không chỉ là website đặt trong app

Một hybrid application (ứng dụng lai / 하이브리드 앱) thường dùng native shell để chứa WebView, còn phần lớn UI/business screen chạy bằng WebSquare/JavaScript. Nhưng khi cần camera, biometrics, push notification, file system, app-to-app launch hoặc secure storage, JavaScript phải đi qua native capability.

Mental model:

```text
WebSquare page
    ↓
JavaScript runtime
    ↓
WebView boundary
    ↓
native bridge / Cordova-style plugin / app-defined plugin
    ↓
iOS / Android capability
```

Đây là một distributed boundary nằm trong cùng thiết bị. Hai bên có lifecycle, error model và security model khác nhau.

## 2. Browser capability và native capability phải được tách

Một screen có thể chạy trong desktop Chrome, mobile browser và hybrid WebView. Không nên giả định mọi môi trường có cùng API.

Ví dụ conceptual:

```javascript
if (isHybridRuntime()) {
    return nativeCamera.capture();
}
return webCameraFallback();
```

Điểm quan trọng không phải tên helper. Điều quan trọng là capability detection phải nằm ở một abstraction boundary thay vì rải `if (Android)`/`if (iPhone)` trong từng screen.

## 3. `WebSquare.hybridApp` là environment signal, không phải architecture

Tài liệu WebSquare có những flow dùng `WebSquare.hybridApp` để phân biệt browser với hybrid runtime, ví dụ file download trên mobile. Signal này hữu ích để chọn code path.

Nhưng production architecture vẫn nên có adapter:

```text
screen
  ↓
platformService.download(...)
  ├─ browser adapter
  └─ hybrid adapter
```

Screen không nên biết Cordova path, Android intent hay iOS temporary directory.

## 4. Native bridge là RPC cục bộ

Khi JavaScript gọi plugin native, hãy reasoning như remote procedure call (RPC), dù hai bên ở cùng process/app.

```text
JS creates request
→ serialize arguments
→ bridge dispatch
→ native executes
→ native serializes result/error
→ JS callback/promise resumes
```

Từ mental model này suy ra ngay các vấn đề: serialization, timeout, duplicate callback, lifecycle cancellation, version mismatch và error translation.

## 5. Không truyền object runtime qua bridge

Component instance, DOM node, `scwin`, DataList object hay function không phải payload bridge tốt.

Bridge contract nên dùng primitive/plain data:

```javascript
{
    requestId: "REQ-123",
    documentType: "ID_CARD",
    options: {
        allowGallery: false,
        quality: 0.85
    }
}
```

Native trả về data contract:

```javascript
{
    requestId: "REQ-123",
    status: "SUCCESS",
    fileToken: "..."
}
```

Không để native biết GridView ID hoặc WebSquare scope topology.

## 6. Callback contract phải có exactly-once semantics ở mức ứng dụng

Một plugin bug có thể callback hai lần, hoặc callback success sau khi screen đã đóng. Screen code không nên mutate state vô điều kiện.

Có thể guard bằng request state:

```text
PENDING
  ├─ SUCCESS → terminal
  ├─ ERROR   → terminal
  └─ CANCEL  → terminal
```

Sau terminal state, callback cùng request ID phải bị ignore hoặc log anomaly.

## 7. Page lifetime và native operation lifetime khác nhau

User mở eKYC camera từ page A, rồi app background hoặc user đóng tab/page. Native camera có thể vẫn đang chạy.

Khi native callback về, page scope cũ có thể đã bị destroy.

Sai assumption:

```text
operation started by page A
→ page A chắc chắn còn tồn tại khi operation kết thúc
```

Đúng reasoning:

```text
operation lifetime độc lập
→ callback phải kiểm tra owner/session/page validity
```

Đây là stale callback problem tương tự stale Submission response, nhưng crossing native boundary.

## 8. App background/foreground là lifecycle event thật

Browser desktop thường giữ page active tương đối ổn định. Mobile OS có thể pause WebView, reclaim memory hoặc kill process khi background.

Vì vậy state quan trọng không nên chỉ tồn tại trong một closure.

Phân loại state:

```text
ephemeral UI state → có thể mất
recoverable workflow state → cần persist/checkpoint
security-sensitive secret → dùng storage phù hợp, không localStorage tùy tiện
```

Một eKYC flow 5 bước cần biết sau resume user đang ở bước nào và server đã ghi nhận gì.

## 9. Native permission là state machine

Camera/location/storage permission không phải boolean cố định. Có thể là:

```text
not requested
allowed
rejected
rejected permanently / don't ask again
restricted by policy
```

UI phải map từng state sang action phù hợp. Nếu permission bị deny vĩnh viễn, gọi request lại vô hạn chỉ tạo UX loop; có thể cần hướng user tới system settings.

## 10. Permission success không đồng nghĩa operation success

Camera permission được cấp nhưng camera có thể unavailable, user cancel, device storage full hoặc native SDK fail.

Tách:

```text
permission result
capability availability
operation result
business result
```

Không collapse tất cả thành `false`.

## 11. Deep link là external input

Một hybrid app có thể được mở bằng custom scheme hoặc universal/app link.

Ví dụ conceptual:

```text
myapp://ekyc/result?token=...
```

Deep-link payload là untrusted input giống URL từ web. Không dùng nó trực tiếp để quyết định privileged action.

Server-side token validation, expiry, nonce/state correlation và allowlisted route là những control thường cần.

## 12. Deep link routing và WebSquare navigation

Native shell nhận deep link trước, sau đó cần route vào WebSquare page/screen. Có hai timing case:

```text
app already running
→ WebView/page shell ready
→ dispatch route immediately

cold start
→ native receives link
→ WebView chưa ready
→ store pending route
→ engine/shell ready
→ dispatch route
```

Nếu không có pending-route state, deep link cold start sẽ thỉnh thoảng “mất”.

## 13. Native → Web callback phải đi qua một gateway

Đừng để native layer gọi ngẫu nhiên `scwin.someFunction()` của screen hiện tại bằng string.

Tốt hơn:

```text
native event
→ bridge gateway
→ validate event envelope
→ route by event type/requestId
→ application service
→ current page reacts
```

Gateway làm versioning, logging và security dễ hơn.

## 14. Event envelope

Một event contract tốt có thể gồm:

```javascript
{
    version: 1,
    type: "EKYC_COMPLETED",
    requestId: "REQ-123",
    timestamp: 1780000000000,
    payload: {
        sessionId: "..."
    }
}
```

`type` cho routing, `version` cho compatibility, `requestId` cho correlation. Payload chỉ chứa data cần thiết.

## 15. Bridge versioning

Web bundle và native app không phải lúc nào deploy cùng lúc. User có thể chạy native app version cũ nhưng tải WebSquare resource mới từ server.

Đây là compatibility problem quan trọng:

```text
Web vNext expects nativePlugin.fooV2()
Native app old only has fooV1()
→ runtime failure
```

Cần capability/version handshake.

```text
web asks native capabilities
→ native returns appVersion + pluginVersion/features
→ web selects compatible path
```

Đừng chỉ check user agent.

## 16. Backward compatibility matrix

Một release nên biết các cặp được support:

```text
web build A ↔ app 5.2+
web build B ↔ app 5.4+
```

Nếu web deploy độc lập, server/CDN có thể cần serve compatible bundle theo app version hoặc web phải degrade gracefully.

Hybrid production failure rất hay xuất hiện khi team web và mobile release theo cadence khác nhau.

## 17. Authentication trong WebView

Hybrid app có thể dùng cookie session, access token hoặc native-managed credential. Dù cơ chế nào, boundary phải rõ:

```text
native auth state
↕
WebView auth state
↕
backend session/token state
```

Nếu native refresh token nhưng WebView vẫn giữ cookie/token cũ, user có thể thấy app “đã login” nhưng WebSquare request nhận 401.

Auth synchronization phải là explicit protocol.

## 18. Không nhét long-lived secret vào JavaScript global

WebView JavaScript có thể bị inspect/debug ở môi trường development và chịu XSS risk như web. Long-lived refresh token/private credential không nên được đặt vào `window`, `scwin` hoặc DataCollection nếu native secure storage có thể giữ chúng.

Web layer nên nhận capability/token có lifetime và scope tối thiểu cần thiết.

## 19. XSS trong hybrid có thể nguy hiểm hơn web thường

Nếu injected JavaScript có quyền gọi native bridge mạnh, XSS có thể trở thành native capability abuse.

Ví dụ bridge cung cấp:

```text
readFile(path)
openExternalApp(...)
getDeviceId()
```

thì attacker script có thể gọi chúng nếu bridge không kiểm soát origin/caller/action.

Bridge phải expose API tối thiểu, validate argument và áp dụng authorization/policy ở native side khi cần.

## 20. Bridge allowlist thay vì generic `execute(command, args)`

Một generic bridge cho phép string command bất kỳ rất linh hoạt nhưng khó audit.

Prefer contract rõ:

```text
camera.capture
file.download
biometric.authenticate
app.openSettings
```

thay vì:

```text
native.execute("some arbitrary class/method", args)
```

Surface nhỏ hơn giúp giảm attack surface và migration risk.

## 21. File download trên hybrid

Tài liệu WebSquare có ví dụ mobile download dùng Cordova `FileTransfer`, chọn directory khác nhau giữa iOS và Android rồi mở file bằng native/system target.

Đừng copy path literal từ sample vào production mà không kiểm tra plugin/platform version. Filesystem permission model thay đổi theo Android/iOS version.

Abstraction nên là:

```javascript
platformService.downloadFile({ url, fileName, mimeType })
```

và native adapter chịu trách nhiệm path/permission/open behavior.

## 22. Popup/browser launch trong hybrid

`window.open()` trong WebView có thể không giống desktop browser. Target `_blank`, `_system`, embedded browser plugin hoặc OS browser có semantics khác nhau tùy shell/plugin.

Trước khi dùng, quyết định intent:

```text
mở nội bộ trong WebView?
mở browser ngoài app?
mở native app khác?
```

Rồi map intent sang platform adapter.

## 23. External app launch và fallback

Nếu cần mở banking/eKYC/identity app khác:

```text
check capability / attempt launch
        ↓
success → wait for callback/deep link
        ↓
fail → store/app-store/web fallback
```

Không giả định app đích đã cài.

Callback phải correlate với request/session ban đầu để tránh nhận result của flow cũ.

## 24. eKYC như một distributed workflow

Một eKYC flow có thể đi qua:

```text
WebSquare screen
→ native camera/SDK
→ vendor SDK/server
→ app callback
→ WebSquare
→ project backend
```

Không layer nào một mình sở hữu toàn bộ transaction.

Cần workflow state explicit:

```text
CREATED
CAPTURE_STARTED
CAPTURE_COMPLETED
SUBMITTED
VERIFIED
REJECTED
EXPIRED
```

UI chỉ render workflow state; không nên suy trạng thái chỉ từ việc popup/camera đã đóng.

## 25. Request ID xuyên các layer

Một request ID duy nhất giúp trace:

```text
WebSquare log
native log
vendor callback
backend log
```

Nếu mỗi layer tự sinh ID mà không map, incident “camera thành công nhưng UI không update” sẽ rất khó điều tra.

## 26. Offline và flaky network

Hybrid app thường chạy trên cellular network. Network có thể chuyển Wi-Fi ↔ LTE, mất vài giây hoặc app background giữa request.

Read operation có thể retry với backoff nếu idempotent. Mutation phải có idempotency semantics.

Native operation success nhưng server submit fail là một state riêng; đừng bắt user chụp lại ảnh nếu artifact/session vẫn còn hợp lệ.

## 27. Retry phải dựa trên operation semantics

```text
GET status → thường retry được
upload chunk → có thể retry nếu protocol hỗ trợ
create payment → cần idempotency key
launch camera → retry nghĩa là user action mới, không auto-loop
```

Một helper `retryAll()` cho mọi bridge/network call là anti-pattern.

## 28. Timeout budget

Một flow qua nhiều layer cần timeout budget:

```text
Web UI timeout
native plugin timeout
vendor SDK timeout
backend timeout
```

Nếu UI timeout 10s nhưng native SDK hợp lệ mất 30s, UI sẽ báo fail trong khi operation vẫn tiếp tục.

Timeout phải phản ánh ownership: timeout có cancel operation thật không, hay chỉ ngừng chờ?

## 29. Cancellation contract

User bấm Cancel trong UI. Có ba khả năng:

```text
cancel chỉ UI waiting
cancel native operation
cancel cả server/vendor session
```

Contract phải explicit. Nếu native không cancel được, mark request abandoned và ignore late callback.

## 30. WebView cache và stale resource

Native app upgrade nhưng WebView cache vẫn giữ JS/W-Pack cũ, hoặc ngược lại. Hybrid incident vì vậy phải record cả:

```text
native app version
OS version
WebView version
WebSquare engine build
web artifact/build ID
config version
```

Chỉ hỏi “app version bao nhiêu?” là chưa đủ.

## 31. Remote debugging và production privacy

Development có thể bật WebView remote debugging, console và WebSquare debug facilities. Production phải cân bằng observability với exposure.

Không log access token, citizen ID, raw eKYC image, biometric result chi tiết hoặc full deep-link secret.

Debug build và production build cần policy khác nhau.

## 32. Crash vs JavaScript error

Hybrid có ít nhất ba failure domain:

```text
JavaScript/WebSquare error
WebView/process error
native app/plugin crash
```

JavaScript `try/catch` không bắt native crash. Native crash reporter không tự chứa WebSquare state trước crash.

Incident correlation cần telemetry ở cả hai phía.

## 33. Testing matrix

Hybrid feature không thể chỉ test Chrome desktop.

Minimum reasoning matrix:

```text
Android + supported WebView
Android permission denied/allowed
Android background/resume

iOS + supported WKWebView
iOS permission denied/allowed
iOS background/resume

old supported app + new web
new app + current web
slow/offline network
cold-start deep link
warm deep link
```

Không nhất thiết mọi commit chạy toàn matrix, nhưng release risk phải được cover có chủ đích.

## 34. Contract test cho bridge

Bridge adapter có thể được test bằng fake native implementation:

```javascript
var fakeBridge = {
    capture: function (request) {
        return Promise.resolve({
            requestId: request.requestId,
            status: "SUCCESS",
            fileToken: "TEST_TOKEN"
        });
    }
};
```

Mục tiêu là test WebSquare workflow mà không cần camera thật. Native team test contract tương tự ở phía native.

## 35. Production checklist

Trước khi release hybrid feature, trả lời được:

```text
Bridge contract version là gì?
Old app có gọi được web mới không?
Operation có requestId không?
Late callback xử lý thế nào?
Page đóng trước callback thì sao?
Permission denied/permanent denied thì sao?
App background giữa flow thì sao?
Deep link cold start có mất không?
Native capability có allowlist không?
Sensitive data có đi vào JS/log không?
Có test old app/new web compatibility không?
```

## 36. Senior pattern: platform service

Screen nên phụ thuộc vào intent-level API:

```javascript
platformService.captureIdentityDocument(options)
platformService.downloadFile(file)
platformService.openExternalVerification(session)
platformService.authenticateBiometric(options)
```

Bên dưới mới quyết định browser, Cordova, Android hoặc iOS implementation.

Nhờ vậy business screen không biến thành collection của platform `if/else`.

## 37. Kết nối

Hybrid chapter dựa trên [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md) để hiểu page lifetime, [10 — Rendering, Lazy Loading & Lifetime](10_rendering_lazy_loading_lifetime.md) để hiểu resource lifetime, [15 — Backend Contract, Transaction & Concurrency](15_backend_contract_transaction_concurrency.md) để hiểu distributed workflow và [17 — File/Excel Pipeline](17_file_excel_upload_download_pipeline.md) cho mobile download.

Cách trace incident xuyên WebSquare/native/backend được tiếp tục ở [19 — Observability & Incident Response](19_observability_incident_response.md).

## 38. Mastery checkpoint

Bạn đã master phần hybrid khi không còn nghĩ “gọi plugin rồi callback”. Bạn phải nhìn thấy một RPC boundary có version, serialization, lifecycle, permission, security, compatibility và failure semantics; đồng thời thiết kế WebSquare screen sao cho browser và native implementation có thể thay đổi mà business workflow vẫn giữ invariant.