# Case 02 — Authentication, Session, Token Refresh và Network Security

Authentication trong app Android thường bị dạy như một màn hình login rồi lưu token vào đâu đó. Production thực tế phức tạp hơn nhiều vì authentication chỉ trả lời **user là ai**, còn authorization trả lời **user được phép làm gì**; session còn phải sống qua process restart; token có expiry; nhiều request có thể cùng nhận `401`; refresh có thể thất bại; user có thể logout giữa lúc request đang chạy; và toàn bộ client vẫn là môi trường có thể bị inspect, modify hoặc chạy trên thiết bị không đáng tin tuyệt đối.

Chương này xây một mental model từ sign-in đến logout, đồng thời chỉ rõ phần nào thuộc app, phần nào bắt buộc phải được enforced ở backend.

## 1. Authentication, authorization và session là ba khái niệm khác nhau

**Authentication** xác minh identity. Password, passkey, Sign in with Google hoặc enterprise identity provider đều là các cách authentication.

**Authorization** là policy quyết định identity đó được làm gì. App có thể ẩn nút admin theo role để UX tốt hơn, nhưng backend vẫn phải enforce authorization. Một APK có thể bị patch nên client-side role check không phải security boundary.

**Session** là trạng thái cho phép nhiều request liên tiếp chứng minh identity mà không bắt user đăng nhập lại mỗi lần. Với token-based system, session thường liên quan access token, refresh token hoặc một credential/session handle tương đương.

## 2. Client không phải nơi giữ “bí mật tuyệt đối”

Một mobile app được phân phối cho user. Code, resource và runtime có thể bị reverse-engineer. Vì vậy không embed server secret, private signing secret, master API key hoặc logic “nếu app giấu được thì backend sẽ tin”.

Android Keystore hữu ích để bảo vệ key material và làm extraction khó hơn, nhưng nó không biến client thành HSM mà server có thể tin vô điều kiện. Integrity/attestation cũng là risk signal để backend tăng confidence, không thay thế authentication và authorization.

## 3. Modern sign-in boundary

Với credential UX hiện đại, app nên ưu tiên platform/Jetpack abstraction như **Credential Manager** thay vì tự xây password picker riêng cho mọi cơ chế. Credential Manager thống nhất password, passkey và federated sign-in flow; tuy nhiên nó chỉ là phần đầu của login.

Một flow điển hình:

```text
User chooses credential/passkey/federated account
        ↓
Credential Manager returns credential/assertion
        ↓
App sends assertion to backend over HTTPS
        ↓
Backend verifies provider/assertion
        ↓
Backend creates application session
        ↓
App receives short-lived access credential + session/refresh mechanism
```

Không nên chỉ parse identity token ở client rồi coi user là authenticated cho protected backend data. Backend phải verify token/assertion và tạo session của chính hệ thống.

## 4. Session repository là source of truth cho trạng thái login

Đừng để mỗi screen tự đọc SharedPreferences và đoán login state. Một `SessionRepository` nên sở hữu contract rõ ràng.

```kotlin
interface SessionRepository {
    val session: StateFlow<SessionState>

    suspend fun signIn(request: SignInRequest): Result<Unit>
    suspend fun refreshIfNeeded(): Result<Unit>
    suspend fun signOut()
}

sealed interface SessionState {
    data object Unknown : SessionState
    data object SignedOut : SessionState
    data class SignedIn(
        val userId: String,
        val expiresAtEpochMillis: Long
    ) : SessionState
}
```

`Unknown` hữu ích khi app mới khởi động và đang restore session. Nếu chỉ có Boolean `isLoggedIn`, UI dễ flash login screen trong vài millisecond trước khi persistent state được đọc.

## 5. Không expose raw token cho UI

ViewModel không cần access token string. UI càng không cần. Token nên ở data/security boundary thấp nhất có thể.

Một network authentication component có thể hỏi session storage để attach credential:

```kotlin
class AuthHeaderProvider(
    private val tokenStore: TokenStore
) {
    suspend fun currentAccessToken(): String? = tokenStore.readAccessToken()
}
```

Retrofit/OkHttp interceptor có thể attach header, nhưng refresh strategy phải cẩn thận để tránh deadlock hoặc refresh storm.

## 6. Access token ngắn hạn và refresh token

Access token nên có lifetime ngắn hơn refresh credential vì nó được gửi thường xuyên. Refresh credential mạnh hơn và cần được bảo vệ tốt hơn.

Một model đơn giản:

```kotlin
data class TokenBundle(
    val accessToken: String,
    val accessTokenExpiresAt: Instant,
    val refreshToken: String?
)
```

Không nên log object này, kể cả ở debug build nếu log có thể được upload. `toString()` mặc định của data class có thể vô tình in secret; với type nhạy cảm, cân nhắc custom representation hoặc wrapper không expose value.

## 7. Refresh trước expiry hay sau 401?

Có hai chiến lược chính và thường dùng kết hợp.

**Proactive refresh** kiểm tra expiry trước request. Nó giảm số request bị 401 nhưng phụ thuộc clock và metadata expiry.

**Reactive refresh** thử request, nhận 401 rồi refresh. Nó đơn giản về semantics nhưng nếu 20 request đồng thời cùng hết hạn, cả 20 có thể trigger refresh.

Production thường dùng proactive khi token gần hết hạn, đồng thời vẫn xử lý 401 vì server có thể revoke token trước expiry.

## 8. Single-flight refresh: tránh 20 refresh request cùng lúc

Đây là bug rất phổ biến. Giả sử app mở home screen và gửi 10 API call cùng lúc. Access token đã expired, cả 10 nhận 401. Nếu mỗi request tự refresh, server nhận 10 refresh request; refresh token rotation có thể khiến 9 request sau fail và session bị logout sai.

Một giải pháp là serialize refresh bằng `Mutex` và kiểm tra lại token sau khi lock:

```kotlin
class TokenRefresher(
    private val store: TokenStore,
    private val api: AuthApi,
    private val mutex: Mutex = Mutex()
) {
    suspend fun freshAccessToken(staleToken: String?): String? = mutex.withLock {
        val current = store.readAccessToken()

        if (current != null && current != staleToken && !current.isExpired()) {
            return current.value
        }

        val refreshToken = store.readRefreshToken() ?: return null
        val response = api.refresh(refreshToken)
        store.save(response.toTokenBundle())
        response.accessToken
    }
}
```

Check `current != staleToken` rất quan trọng: request thứ hai đợi mutex, đến lượt nó thì request thứ nhất có thể đã refresh xong. Không cần refresh lần nữa.

## 9. Token refresh không được recurse vô hạn

Nếu auth endpoint dùng cùng interceptor và request refresh cũng nhận 401, ta có thể tạo loop. Hãy đánh dấu endpoint không cần attach auth hoặc dùng client riêng cho refresh.

Ngoài ra cần giới hạn retry. Một request protected chỉ nên retry theo policy rõ ràng; không phải “401 thì cứ refresh mãi”.

## 10. Logout là một transaction về security state

Logout không chỉ là clear access token rồi navigate login. Cần quyết định:

- refresh/session credential nào phải revoke ở server;
- local database user-specific có phải clear không;
- pending WorkManager job có thể tiếp tục không;
- notification channel/data cache có chứa thông tin user không;
- WebSocket/SSE connection phải close không;
- background sync đang dùng credential cũ xử lý thế nào;
- app có nhiều account hay chỉ một account.

Một sequence hợp lý:

```text
mark session as signing out
→ stop/deny new authenticated operations
→ best-effort revoke server session
→ cancel user-bound background work
→ clear token/credential storage
→ clear or namespace user data
→ publish SignedOut
→ navigate/reset back stack
```

Nếu revoke network fail vì offline, local logout vẫn phải có thể hoàn thành. Backend session sẽ expire hoặc có thể được revoke lần sau tùy threat model.

## 11. User-bound local data phải có namespace hoặc cleanup policy

Một lỗi nghiêm trọng là user A logout, user B login và nhìn thấy cached data của A. Có hai chiến lược phổ biến.

Cách đơn giản: clear user-specific database/table khi logout.

Cách mạnh hơn cho multi-account: mọi row quan trọng có `accountId`, query luôn scope theo account và switch source of truth theo active session. Complexity cao hơn nhưng hỗ trợ account switching tốt hơn.

## 12. Secret storage: DataStore không tự động là secure vault

DataStore phù hợp persistence config/session metadata nhưng không mặc định mã hóa secret. Nếu threat model yêu cầu bảo vệ token khi at-rest, cần thiết kế storage sử dụng cryptographic key bảo vệ bởi Android Keystore hoặc solution phù hợp.

Không hard-code encryption key trong source. Nếu key để decrypt cũng nằm plaintext ngay cạnh ciphertext thì encryption không mua được security thực tế.

Cũng cần nhớ: một thiết bị compromised/rooted có threat model khác. Mục tiêu mobile security thường là giảm exposure và tăng chi phí attack, không hứa “secret không bao giờ bị lấy”.

## 13. Biometrics không phải backend authorization

`BiometricPrompt` có thể dùng để xác nhận user presence trước thao tác nhạy cảm hoặc unlock một key local. Nó không có nghĩa backend tự động biết request được user vừa scan fingerprint.

Nếu operation tài chính cần step-up authentication, protocol phải được thiết kế end-to-end: backend tạo challenge, client thực hiện approved auth ceremony, backend verify proof/challenge phù hợp. Một Boolean `biometricPassed=true` từ client không được coi là trusted evidence.

## 14. Network Security Config và HTTPS

Production app phải dùng secure transport. Không tạo `TrustManager` chấp nhận mọi certificate để “fix SSL”. Debug environment nếu cần custom CA phải được giới hạn debug configuration.

Network Security Config có thể cấu hình trust anchor/cleartext policy theo environment. Cleartext HTTP nên bị disable trừ use case có lý do rõ ràng.

Certificate pinning có trade-off vận hành lớn. Pin sai hoặc certificate rotate ngoài dự kiến có thể brick network cho toàn bộ installed app cho tới khi user update. Chỉ dùng khi threat model justify và phải có backup pins/rotation plan.

## 15. Interceptor, authenticator và coroutine boundary

Với OkHttp, interceptor phù hợp thêm header/logging/policy request. `Authenticator` có thể xử lý challenge như 401, nhưng implementation phải tránh blocking/coroutine mismatch và duplicate refresh.

Nếu auth refresh API là suspend trong Retrofit nhưng authenticator chạy synchronous contract, đừng tùy tiện `runBlocking` trên thread không hiểu rõ. Có thể thiết kế synchronous token refresh client riêng, hoặc centralize request stack theo cách không gây deadlock. Điều quan trọng là hiểu execution model của library thay vì chỉ copy snippet.

## 16. Error model của authentication

Sign-in cần phân biệt ít nhất invalid credential, canceled flow, network unavailable, rate limited, account disabled, provider error và unknown error. Không nên convert tất cả thành `false`.

```kotlin
sealed interface AuthError {
    data object InvalidCredential : AuthError
    data object UserCanceled : AuthError
    data object Offline : AuthError
    data class RateLimited(val retryAfter: Duration?) : AuthError
    data object AccountDisabled : AuthError
    data class ProviderFailure(val code: String?) : AuthError
    data class Unknown(val cause: Throwable) : AuthError
}
```

UI có thể xử lý canceled flow im lặng, invalid credential bằng field message, offline bằng retry UI, và account disabled bằng support path.

## 17. Request retry phải dựa trên idempotency

GET thường có thể retry an toàn hơn POST mutation, nhưng HTTP method không phải toàn bộ câu chuyện. Payment create request nếu retry mù có thể charge hai lần. Backend nên hỗ trợ idempotency key cho operation cần exactly-once business effect ở mức protocol.

Client có thể tạo stable idempotency key cho một logical operation và reuse key khi retry:

```kotlin
data class PendingPayment(
    val localOperationId: UUID,
    val idempotencyKey: String,
    val payload: PaymentPayload
)
```

Network retry policy phải biết operation semantics, không phải một global interceptor retry mọi 5xx.

## 18. Session state và navigation

Root navigation thường phụ thuộc session state:

```text
Unknown -> splash/restoring
SignedOut -> auth graph
SignedIn -> main graph
```

Khi logout, reset back stack để Back không quay về authenticated screen. Tuy nhiên protected screen vẫn không nên dựa vào navigation để bảo vệ data; repository/backend authorization mới là boundary thật.

Process recreation có thể khôi phục back stack cũ. Vì vậy screen protected phải react với `SessionState` hiện tại, không giả định “đã vào đây nghĩa là chắc chắn signed in”.

## 19. Credential Manager và account lifecycle

Credential Manager giúp thống nhất password/passkey/federated sign-in experience, nhưng app vẫn cần xử lý account lifecycle riêng: linking account, re-authentication cho operation nhạy cảm, logout, account deletion và server-side session revoke.

Sign in with Google cho authentication profile không đồng nghĩa app có authorization truy cập Google Drive/Gmail. Authorization resource của Google là flow riêng với scope riêng. Đây là ví dụ điển hình của khác biệt authentication và authorization.

## 20. Observability nhưng không leak credential

Auth cần telemetry vì failure thường khó debug, nhưng log phải redact secret.

Nên log event như:

```text
auth_sign_in_started provider=passkey

auth_sign_in_failed category=network

token_refresh_started reason=near_expiry

token_refresh_failed category=invalid_grant

session_signed_out source=user_action
```

Không log access token, refresh token, password, authorization header hoặc credential assertion raw. Với crash reporting, kiểm tra breadcrumb/request logger có tự động capture header/body nhạy cảm không.

## 21. Test những gì?

Unit test session state machine: restore thành công/thất bại, token gần expiry, refresh fail, logout. Test single-flight refresh với nhiều coroutine đồng thời để đảm bảo chỉ một call refresh thực sự xảy ra. Test request retry không lặp mutation ngoài policy. Integration test database cleanup khi switch account. UI test root navigation khi session đổi.

Một test quan trọng:

```kotlin
@Test
fun concurrent_401_only_refreshes_once() = runTest {
    // Arrange stale token and 10 callers.
    // Make refresh fake count invocations.
    // Launch callers concurrently.
    // Assert refresh count == 1 and all callers receive new token.
}
```

## 22. Threat-model checklist

Trước khi ship auth, hãy trả lời bằng văn bản:

Ai là attacker? Token theft qua log, malware/local extraction, MITM, modified APK, credential stuffing hay stolen device? Asset cần bảo vệ là gì? Server có revoke session không? Access token sống bao lâu? Refresh rotation thế nào? App có thể detect account/session invalidation server-side không? Local data sau logout xử lý ra sao? Backup có vô tình chứa credential không? Deep link có thể đưa user vào protected action mà không revalidate không?

Nếu không biết threat model, rất dễ dùng kỹ thuật “security-looking” nhưng không bảo vệ đúng asset.

## 23. Senior notes

Không viết token refresh ở từng repository. Nó là cross-cutting infrastructure với concurrency semantics rõ ràng. Không expose token lên ViewModel. Không tin role/claim chỉ vì UI parse được. Không log auth header. Không retry mutation mù. Không dùng biometric như server authorization. Không nghĩ obfuscation là secret storage.

Một session architecture tốt cho phép kể flow rất rõ: **credential ceremony → backend verification → application session → token storage boundary → authenticated request → refresh single-flight → observable session state → deterministic logout**. Mỗi bước có owner, failure model và test riêng.
