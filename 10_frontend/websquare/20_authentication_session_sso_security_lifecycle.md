# 20 — Authentication, Session, SSO & Security Lifecycle

Một màn hình WebSquare có thể chạy đúng về UI, DataList và Submission nhưng vẫn sai ở cấp hệ thống nếu developer không phân biệt **identity**, **authentication**, **session**, **authorization** và **screen state**. Đây là một trong những nguồn bug khó nhất ở ứng dụng enterprise vì browser thường giữ page instance rất lâu, trong khi session phía server có lifetime khác.

Chapter này không biến WebSquare thành security framework. Authentication và authorization thật sự thuộc server/identity platform. Mục tiêu ở đây là hiểu **client lifecycle phải phản ứng thế nào khi security state thay đổi**, đặc biệt trong SPA, multi-tab, popup, hybrid app và Submission đang chạy.

> Mental model chính: `UI state != authentication state != authorization state != server session state`.

## 1. Bốn khái niệm phải tách riêng

**Identity** trả lời “người dùng hoặc service principal này là ai?”.

**Authentication** trả lời “hệ thống đã xác minh identity bằng cơ chế nào?”.

**Session** là trạng thái liên tục cho phép nhiều request thuộc cùng một authenticated interaction. Session có thể dựa trên server-side session cookie, token hoặc kiến trúc khác.

**Authorization** trả lời “identity hiện tại được phép thực hiện operation nào trên resource nào?”.

Một menu bị ẩn chỉ là presentation. Một button disabled chỉ là UX. Một DataMap chứa `role=ADMIN` chỉ là client state. Không thứ nào trong số đó thay thế server authorization.

## 2. Security state machine thay vì boolean `isLogin`

Trong app lớn, `isLogin = true/false` quá nghèo thông tin. Một model thực tế hơn:

```text
UNKNOWN
→ AUTHENTICATING
→ AUTHENTICATED
→ ACTIVE
→ EXPIRING
→ EXPIRED
→ REAUTHENTICATING
→ LOGGED_OUT
```

Có thể thêm `LOCKED`, `MFA_REQUIRED`, `PASSWORD_CHANGE_REQUIRED` hoặc `TERMS_REQUIRED` tùy hệ thống.

Điểm quan trọng là mỗi state cho phép một tập action khác nhau. `AUTHENTICATED` chưa chắc đã đồng nghĩa application shell và permission data đã ready. `EXPIRED` không có nghĩa page instance tự biến mất. `REAUTHENTICATING` không nên để Save tiếp tục như chưa có gì xảy ra.

## 3. Session lifetime và page lifetime là hai đồng hồ khác nhau

SPA WebSquare có thể giữ shell nhiều giờ. Session server có thể timeout sau 30 phút inactivity. Tab browser có thể sleep rồi resume. Laptop có thể suspend. Hybrid WebView có thể background rồi quay lại sau vài giờ.

Do đó:

```text
page lifetime      ───────────────────────────────>
server session     ───────────────X
pending UI state   ───────────────────────────────>
```

Sau điểm `X`, DataList và Grid vẫn còn trong browser nhưng server không còn coi request là authenticated.

Đây là lý do không được suy luận “màn hình vẫn mở nên session còn sống”.

## 4. Session expiration phải là application-level event

Nếu mỗi Submission tự xử lý session expiration bằng một alert khác nhau, application sẽ nhanh chóng hỗn loạn.

Một kiến trúc tốt thường có common communication layer nhận diện auth failure và phát một event/transition thống nhất:

```text
Submission response
→ classify transport/business/auth error
→ AUTH_EXPIRED event
→ block new protected commands
→ preserve/discard working state theo policy
→ redirect/re-authenticate
→ restore/reload theo contract
```

Không nên để 20 page cùng lúc mở 20 login popup khi session hết hạn.

## 5. 401, 403 và business error không giống nhau

Một convention phổ biến:

```text
401 / unauthenticated
→ credential/session không còn hợp lệ

403 / forbidden
→ identity hợp lệ nhưng không có quyền

409 / conflict
→ version/concurrency conflict

422 hoặc business envelope
→ validation/business rule failure
```

Exact HTTP contract phụ thuộc backend, nhưng frontend phải phân loại được ý nghĩa. Nếu mọi lỗi đều hiện “System Error”, người dùng không biết cần login lại, sửa dữ liệu hay liên hệ support.

## 6. Submission interceptor/common handler

WebSquare SP5 cho phép cấu hình và handler quanh Submission; exact API/property phải kiểm tra theo engine build. Về architecture, mục tiêu là có một boundary chung:

```javascript
scwin.handleCommunicationError = function(error) {
    var type = appErrorClassifier.classify(error);

    if (type === "AUTH_EXPIRED") {
        authCoordinator.expire();
        return;
    }

    if (type === "FORBIDDEN") {
        permissionCoordinator.showDenied();
        return;
    }

    errorPresenter.show(error);
};
```

Tên API ở trên là project abstraction, không phải WebSquare built-in API. Điều quan trọng là **classification và orchestration không bị copy vào từng screen**.

## 7. Không retry mù request sau login

Giả sử Save request timeout vì session expired. User login lại. Có nên tự động gửi lại Save?

Không thể trả lời chỉ từ frontend.

Nếu operation có side effect và request cũ có thể đã commit trước khi auth layer trả lỗi, retry mù có thể duplicate. Chapter 15 đã giải thích idempotency; security lifecycle phải nối với contract đó.

Safe retry cần biết:

```text
operation read-only hay mutating?
idempotency key có không?
server có commit trước failure không?
request body còn hợp lệ sau re-auth không?
entity version có thay đổi không?
```

Read query thường dễ retry hơn Save/Approve/Transfer.

## 8. Working state khi session hết hạn

Một screen edit có thể chứa 20 phút thay đổi chưa save. Khi session expire, có ba policy thường gặp:

**Discard** — phù hợp dữ liệu nhạy cảm hoặc workflow yêu cầu reload.

**Preserve locally in memory** — sau login lại có thể cho user review và save nếu server version còn phù hợp.

**Persist draft** — chỉ dùng nếu security/privacy cho phép và có thiết kế rõ; không tự ý lưu PII vào localStorage.

Policy phải được quyết định theo domain, không phải developer tự chọn trong từng page.

## 9. SSO không loại bỏ session lifecycle

Single Sign-On (SSO / 통합 인증) chỉ làm nhiều application dùng chung identity provider hoặc authentication flow. Nó không có nghĩa mỗi application session tồn tại mãi.

Có thể có:

```text
Identity Provider session = active
Application session = expired
```

Khi app redirect/re-authenticate, IdP có thể xác nhận user mà không hỏi password lại. Với user cảm giác như “tự login lại”, nhưng application vẫn phải xử lý pending request và working state đúng.

## 10. OIDC/OAuth2 và SAML: hiểu boundary, không nhét protocol vào page

Enterprise SSO thường gặp OpenID Connect/OAuth 2.0 hoặc SAML. WebSquare page không nên tự implement cryptography, token validation hoặc protocol exchange.

Page cần biết contract ở mức:

```text
auth state
current principal summary
permission/capability
session expiry/re-auth event
logout command
```

Token signature validation, authorization code exchange, refresh token policy, SAML assertion validation và key rotation thuộc auth/backend/infrastructure layer.

## 11. Cookie-based session và CSRF

Nếu browser tự gửi session cookie, một request thay đổi dữ liệu có thể cần CSRF protection tùy kiến trúc. UI không thể “chống CSRF” chỉ bằng hidden button.

Mental model:

```text
browser credential automatically attached
+ attacker-controlled cross-site request
= cần server-side CSRF defense phù hợp
```

Frontend có thể tham gia bằng CSRF token/header contract, nhưng server phải verify. Exact mechanism phụ thuộc security stack.

## 12. `HttpOnly`, `Secure`, `SameSite` và vì sao page không nên đọc session secret

Session cookie nhạy cảm thường nên được bảo vệ bằng browser cookie attributes phù hợp. Nếu credential được thiết kế `HttpOnly`, JavaScript không đọc được nó — đó là feature bảo mật, không phải limitation cần workaround.

Không copy session/token secret vào DataMap chỉ để “dễ dùng”. DataCollection có thể bị inspect, log hoặc serialize nhầm qua Submission.

## 13. Authorization phải theo capability/resource

Anti-pattern:

```javascript
if (dmUser.get("role") === "ADMIN") {
    btnApprove.show();
}
```

Điều này có thể dùng cho presentation, nhưng server vẫn phải authorize `APPROVE_ORDER` trên order cụ thể.

Frontend architecture tốt hơn khi dùng capability:

```text
canSearchEmployee
canEditEmployee
canApproveOrder
canExportPersonalData
```

Capability dễ map vào UI hơn role name, và giảm coupling với mô hình role phía server.

## 14. Permission snapshot có thể stale

Permission có thể thay đổi trong khi user đang mở app. Vì vậy client permission chỉ là snapshot phục vụ UX.

Nếu admin thu hồi quyền, request tiếp theo vẫn phải bị server reject dù button hiện tại còn visible.

Khi nhận forbidden response, frontend nên reconcile UI hoặc refresh permission snapshot thay vì kết luận “backend bug vì button đang hiện”.

## 15. Multi-tab browser và logout propagation

User có thể mở nhiều browser tab cùng application.

Tab A logout nhưng Tab B vẫn giữ DataList và UI cũ. Request tiếp theo ở Tab B phải fail theo server state.

Có thể dùng browser coordination mechanism phù hợp để cải thiện UX, nhưng correctness không được phụ thuộc vào việc event logout luôn truyền được giữa tab.

Invariant:

```text
server authorization/session = canonical
cross-tab notification = UX optimization
```

## 16. App shell phải sở hữu auth coordination

Trong WebSquare SPA, shell thường là nơi hợp lý để sở hữu:

```text
auth state
principal summary
permission snapshot
session-expiry dialog
reauth flow
logout flow
cross-screen notification
```

Child screen không nên tự redirect browser hoặc destroy shell theo cách riêng.

Điều này nối trực tiếp với [14 — Application Shell](14_application_shell_navigation_state.md).

## 17. Popup và nested WFrame khi auth state đổi

Nếu session expire khi popup đang mở:

```text
popup owner
→ auth coordinator
→ popup command blocked
→ reauth
→ owner quyết định reload/close/resume
```

Không nên để popup tự login rồi parent vẫn ở auth state cũ.

Security state là cross-screen concern, nhưng UI working state vẫn có owner riêng.

## 18. Hybrid/WebView authentication

Hybrid app tạo thêm ít nhất ba security state:

```text
native app auth state
WebView/browser auth state
backend session/token state
```

Chúng có thể lệch nhau sau background/resume, app upgrade hoặc deep link.

Không truyền long-lived secret qua bridge message nếu không cần. Native secure storage, WebView cookie store và backend token/session policy phải có ownership rõ.

Chapter [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md) giải thích bridge lifecycle; chapter này bổ sung auth reconciliation.

## 19. Deep link vào protected screen

Deep link không được bypass shell security flow.

```text
deep link received
→ parse route
→ auth readiness
→ permission check
→ load screen
→ load business data
```

Nếu chưa authenticated, giữ **navigation intent** chứ không nhất thiết giữ toàn bộ screen instance.

Sau re-auth, shell có thể resume intent nếu policy cho phép.

## 20. Step-up authentication

Một số operation nhạy cảm như transfer, approve, export PII có thể yêu cầu authentication mạnh hơn session thông thường.

Frontend nên model step-up như state transition:

```text
ACTIVE
→ STEP_UP_REQUIRED
→ STEP_UP_IN_PROGRESS
→ ACTIVE_WITH_ASSURANCE
→ execute command
```

Không hard-code “nếu amount > X thì mở OTP popup” rải rác trong screen. Rule trigger nên đến từ domain/security contract.

## 21. Logout là destructive lifecycle event

Logout không chỉ là gọi endpoint rồi redirect.

Cần xác định:

```text
pending Submission xử lý thế nào?
unsaved DataList có xóa không?
file upload staging có cleanup không?
native bridge operation có cancel không?
local/session storage nào cần clear?
app shell cache nào cần reset?
telemetry context nào phải rotate?
```

Sau logout, object cũ không được vô tình dùng lại dưới identity mới.

## 22. Identity switch là case nguy hiểm

Máy dùng chung có thể logout user A rồi login user B trong cùng browser runtime.

Nếu global DataMap/cache giữ dữ liệu A, user B có thể nhìn thấy stale sensitive data.

Invariant quan trọng:

```text
principal change
→ invalidate principal-scoped client state
```

Đây là security reason để tránh global mutable cache không có owner.

## 23. Error taxonomy cho auth lifecycle

Nên phân biệt ít nhất:

```text
AUTH_REQUIRED
SESSION_EXPIRED
TOKEN_INVALID
FORBIDDEN
STEP_UP_REQUIRED
ACCOUNT_LOCKED
AUTH_SERVICE_UNAVAILABLE
CSRF_REJECTED
```

User message có thể đơn giản hơn, nhưng telemetry và orchestration cần category đủ chính xác.

## 24. Observability không được log credential

Correlation ID, principal surrogate ID và permission decision có thể hữu ích, nhưng password, raw token, session cookie, OTP và secret không được log.

PII cũng phải được mask theo policy.

Chapter [19 — Observability](19_observability_incident_response.md) phải được áp dụng cùng security classification.

## 25. Testing matrix

Auth regression suite nên có:

```text
session expire khi idle
session expire trong Search
session expire trong Save
reauth thành công
reauth fail
403 sau permission revoke
logout ở tab khác
principal A → logout → principal B
protected deep link khi chưa login
step-up success/failure
hybrid background → session expire → resume
```

Với Save, phải test cả case server đã commit nhưng client nhận auth/network failure để kiểm chứng idempotency/reconciliation.

## 26. Failure mode: redirect loop

Flow:

```text
app → auth redirect → app
app chưa nhận diện auth-ready
→ auth redirect lần nữa
```

Root cause thường là readiness hoặc callback state bị nhầm, không phải “SSO chậm”.

Log cần có navigation intent, auth transition và correlation ID.

## 27. Failure mode: 20 popup login cùng lúc

Nhiều Submission fail đồng thời và mỗi handler tự mở login.

Fix bằng single-flight reauthentication coordinator:

```text
first auth failure → start reauth
other failures → join/wait
reauth success/fail → broadcast one result
```

Đây là concurrency problem ở client architecture.

## 28. Failure mode: user B thấy dữ liệu user A

Nguyên nhân có thể là shell cache/DataList global không clear khi principal change.

Fix không phải chỉ refresh Grid; phải xác định toàn bộ state có scope theo principal và invalidate đúng boundary.

## 29. Failure mode: Save tự chạy lại sau login và tạo duplicate

Root cause là frontend coi auth recovery như retry transport thông thường.

Fix bằng operation classification + idempotency contract + explicit user reconciliation cho mutating request không chắc kết quả.

## 30. Master checklist

Trước khi coi auth integration là production-ready, phải trả lời được:

```text
Ai sở hữu auth state trong SPA?
Server session/token lifetime bao lâu?
Client nhận diện expiration bằng contract nào?
401/403/business error được phân loại ở đâu?
Reauth có single-flight không?
Mutating request có auto-retry không, vì sao?
Unsaved state xử lý thế nào khi expire?
Principal switch invalidates state nào?
Permission UI có được coi là authorization không?
Deep link đi qua auth readiness chưa?
Hybrid native/WebView auth reconcile thế nào?
Log có vô tình chứa credential/PII không?
```

## 31. Connection map

Submission lifecycle và error classification: [03 — DataCollection & Submission](03_data_collection_submission.md).

Security trust boundary: [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).

Testing: [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md).

Application shell: [14 — Application Shell, Navigation & Multi-Screen State](14_application_shell_navigation_state.md).

Idempotency/concurrency: [15 — Backend Contract, Transaction & Concurrency](15_backend_contract_transaction_concurrency.md).

Hybrid auth: [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md).

Incident evidence: [19 — Observability, Logging & Incident Response](19_observability_incident_response.md).

## 32. Kết luận

Security lifecycle trong WebSquare không phải là “có login page”. Nó là bài toán đồng bộ nhiều lifetime và trust boundary:

```text
Principal
→ Authentication
→ Session
→ Permission snapshot
→ Screen capability
→ Submission
→ Server authorization
→ Result
→ Security-state reconciliation
```

Master-level developer không tin client state chỉ vì UI đang hiển thị hợp lệ. Họ luôn hỏi **security truth nằm ở đâu, state có thể stale khi nào, operation có thể được retry an toàn không, principal change invalidates những gì và evidence nào chứng minh security transition đã xảy ra đúng**.