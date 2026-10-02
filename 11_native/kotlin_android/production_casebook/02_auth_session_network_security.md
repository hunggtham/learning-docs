# Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**. Route đi từ authentication/authorization/session → client trust boundary → token storage/expiry → concurrent refresh, logout và process restart → transport/backend enforcement, để security model nối với lifecycle thực.

Authentication trong app Android thường bị dạy như một màn hình login rồi lưu đơn vị từ (token / 토큰) vào đâu đó. môi trường vận hành (production / 운영 환경) thực tế phức tạp hơn nhiều vì authentication chỉ trả lời **người dùng (user / 사용자) là ai**, còn authorization trả lời **người dùng (user / 사용자) được phép làm gì**; session còn phải sống qua tiến trình (process / 프로세스) restart; đơn vị từ (token / 토큰) có expiry; nhiều yêu cầu (request / 요청) có thể cùng nhận `401`; refresh có thể thất bại; người dùng (user / 사용자) có thể logout giữa lúc yêu cầu (request / 요청) đang chạy; và toàn bộ máy khách (client / 클라이언트) vẫn là môi trường có thể bị inspect, modify hoặc chạy trên thiết bị không đáng tin tuyệt đối.

Chương này xây một mô hình tư duy (mental model / 사고 모델) từ sign-in đến logout, đồng thời chỉ rõ phần nào thuộc app, phần nào bắt buộc phải được enforced ở backend.

## 1. Authentication, authorization và session là ba khái niệm khác nhau

**Authentication** xác minh định danh (identity / 식별자). Password, passkey, Sign in with Google hoặc enterprise định danh (identity / 식별자) provider đều là các cách authentication.

**Authorization** là chính sách (policy / 정책) quyết định định danh (identity / 식별자) đó được làm gì. App có thể ẩn nút admin theo role để UX tốt hơn, nhưng backend vẫn phải enforce authorization. Một APK có thể bị patch nên client-side role check không phải ranh giới bảo mật (security boundary / 보안 경계).

**Session** là trạng thái cho phép nhiều yêu cầu (request / 요청) liên tiếp chứng minh định danh (identity / 식별자) mà không bắt người dùng (user / 사용자) đăng nhập lại mỗi lần. Với token-based hệ thống (system / 시스템), session thường liên quan truy cập (access / 접근) đơn vị từ (token / 토큰), refresh đơn vị từ (token / 토큰) hoặc một credential/session handle tương đương.

> **Chuyển mạch:** Authentication, authorization và session có lifecycle khác nhau; client không giữ absolute secret, nên modern sign-in phải đặt trust boundary và token handling rõ.

## 2. máy khách (client / 클라이언트) không phải nơi giữ “bí mật tuyệt đối”

Một mobile app được phân phối cho người dùng (user / 사용자). mã (code / 코드), tài nguyên (resource / 자원) và thời gian chạy (runtime / 런타임) có thể bị reverse-engineer. Vì vậy không embed máy chủ (server / 서버) secret, private signing secret, master API key hoặc lô-gic (logic / 논리) “nếu app giấu được thì backend sẽ tin”.

Android Keystore hữu ích để bảo vệ key material và làm extraction khó hơn, nhưng nó không biến máy khách (client / 클라이언트) thành HSM mà máy chủ (server / 서버) có thể tin vô điều kiện. Integrity/attestation cũng là rủi ro (risk / 위험) tín hiệu (signal / 신호) để backend tăng confidence, không thay thế authentication và authorization.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **2. máy khách (client / 클라이언트) không phải nơi giữ “bí mật tuyệt đối”** đã nêu tiêu chí phân biệt, còn **3. hiện đại (modern / 현대적) sign-in ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **4. Session repository là nguồn chuẩn (source of truth / 정본) cho trạng thái login** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. hiện đại (modern / 현대적) sign-in ranh giới (boundary / 경계)

Với credential UX hiện đại, app nên ưu tiên nền tảng (platform / 플랫폼)/Jetpack lớp trừu tượng (abstraction / 추상화) như **Credential Manager** thay vì tự xây password picker riêng cho mọi cơ chế. Credential Manager thống nhất password, passkey và federated sign-in luồng (flow / 흐름); tuy nhiên nó chỉ là phần đầu của login.

Một luồng (flow / 흐름) điển hình:

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

Không nên chỉ parse định danh (identity / 식별자) đơn vị từ (token / 토큰) ở máy khách (client / 클라이언트) rồi coi người dùng (user / 사용자) là authenticated cho protected backend dữ liệu (data / 데이터). Backend phải verify đơn vị từ (token / 토큰)/assertion và tạo session của chính hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **3. hiện đại (modern / 현대적) sign-in ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **4. Session repository là nguồn chuẩn (source of truth / 정본) cho trạng thái login** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **5. Không expose raw đơn vị từ (token / 토큰) cho UI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Session repository là nguồn chuẩn (source of truth / 정본) cho trạng thái login

Đừng để mỗi screen tự đọc SharedPreferences và đoán login trạng thái (state / 상태). Một `SessionRepository` nên sở hữu đặc tả hợp đồng (contract / 계약) rõ ràng.

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

`Unknown` hữu ích khi app mới khởi động và đang restore session. Nếu chỉ có Boolean `isLoggedIn`, UI dễ flash login screen trong vài millisecond trước khi persistent trạng thái (state / 상태) được đọc.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **4. Session repository là nguồn chuẩn (source of truth / 정본) cho trạng thái login** nêu điều cần giải thích; **5. Không expose raw đơn vị từ (token / 토큰) cho UI** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. truy cập (access / 접근) đơn vị từ (token / 토큰) ngắn hạn và refresh đơn vị từ (token / 토큰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Không expose raw đơn vị từ (token / 토큰) cho UI

ViewModel không cần truy cập (access / 접근) đơn vị từ (token / 토큰) string. UI càng không cần. đơn vị từ (token / 토큰) nên ở dữ liệu (data / 데이터)/ranh giới bảo mật (security boundary / 보안 경계) thấp nhất có thể.

Một mạng (network / 네트워크) authentication thành phần (component / 컴포넌트) có thể hỏi session lưu trữ (storage / 저장소) để attach credential:

```kotlin
class AuthHeaderProvider(
    private val tokenStore: TokenStore
) {
    suspend fun currentAccessToken(): String? = tokenStore.readAccessToken()
}
```

Retrofit/OkHttp interceptor có thể attach header, nhưng refresh chiến lược (strategy / 전략) phải cẩn thận để tránh deadlock hoặc refresh storm.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **6. truy cập (access / 접근) đơn vị từ (token / 토큰) ngắn hạn và refresh đơn vị từ (token / 토큰)** tiếp nhận điểm tựa từ **5. Không expose raw đơn vị từ (token / 토큰) cho UI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Refresh trước expiry hay sau 401?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. truy cập (access / 접근) đơn vị từ (token / 토큰) ngắn hạn và refresh đơn vị từ (token / 토큰)

Truy cập (access / 접근) đơn vị từ (token / 토큰) nên có thời gian tồn tại (lifetime / 수명) ngắn hơn refresh credential vì nó được gửi thường xuyên. Refresh credential mạnh hơn và cần được bảo vệ tốt hơn.

Một mô hình (model / 모델) đơn giản:

```kotlin
data class TokenBundle(
    val accessToken: String,
    val accessTokenExpiresAt: Instant,
    val refreshToken: String?
)
```

Không nên log đối tượng (object / 객체) này, kể cả ở gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) nếu log có thể được upload. `toString()` mặc định của dữ liệu (data / 데이터) lớp (class / 클래스) có thể vô tình in secret; với kiểu (type / 타입) nhạy cảm, cân nhắc custom biểu diễn (representation / 표현) hoặc wrapper không expose giá trị (value / 값).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **7. Refresh trước expiry hay sau 401?** tiếp nhận điểm tựa từ **6. truy cập (access / 접근) đơn vị từ (token / 토큰) ngắn hạn và refresh đơn vị từ (token / 토큰)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Single-flight refresh: tránh 20 refresh yêu cầu (request / 요청) cùng lúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Refresh trước expiry hay sau 401?

Có hai chiến lược chính và thường dùng kết hợp.

**Proactive refresh** kiểm tra expiry trước yêu cầu (request / 요청). Nó giảm số yêu cầu (request / 요청) bị 401 nhưng phụ thuộc clock và siêu dữ liệu (metadata / 메타데이터) expiry.

**Reactive refresh** thử yêu cầu (request / 요청), nhận 401 rồi refresh. Nó đơn giản về ngữ nghĩa (semantics / 의미론) nhưng nếu 20 yêu cầu (request / 요청) đồng thời cùng hết hạn, cả 20 có thể trigger refresh.

Môi trường vận hành (production / 운영 환경) thường dùng proactive khi đơn vị từ (token / 토큰) gần hết hạn, đồng thời vẫn xử lý 401 vì máy chủ (server / 서버) có thể revoke đơn vị từ (token / 토큰) trước expiry.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **8. Single-flight refresh: tránh 20 refresh yêu cầu (request / 요청) cùng lúc** tiếp nhận điểm tựa từ **7. Refresh trước expiry hay sau 401?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. đơn vị từ (token / 토큰) refresh không được recurse vô hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Single-flight refresh: tránh 20 refresh yêu cầu (request / 요청) cùng lúc

Đây là bug rất phổ biến. Giả sử app mở home screen và gửi 10 API lời gọi (call / 호출) cùng lúc. truy cập (access / 접근) đơn vị từ (token / 토큰) đã expired, cả 10 nhận 401. Nếu mỗi yêu cầu (request / 요청) tự refresh, máy chủ (server / 서버) nhận 10 refresh yêu cầu (request / 요청); refresh đơn vị từ (token / 토큰) rotation có thể khiến 9 yêu cầu (request / 요청) sau thất bại (fail / 실패) và session bị logout sai.

Một giải pháp là serialize refresh bằng `Mutex` và kiểm tra lại đơn vị từ (token / 토큰) sau khi khóa (lock / 잠금):

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

Check `current != staleToken` rất quan trọng: yêu cầu (request / 요청) thứ hai đợi mutex, đến lượt nó thì yêu cầu (request / 요청) thứ nhất có thể đã refresh xong. Không cần refresh lần nữa.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **9. đơn vị từ (token / 토큰) refresh không được recurse vô hạn** tiếp nhận điểm tựa từ **8. Single-flight refresh: tránh 20 refresh yêu cầu (request / 요청) cùng lúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Logout là một giao dịch (transaction / 트랜잭션) về bảo mật (security / 보안) trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. đơn vị từ (token / 토큰) refresh không được recurse vô hạn

Nếu auth endpoint dùng cùng interceptor và yêu cầu (request / 요청) refresh cũng nhận 401, ta có thể tạo vòng lặp (loop / 루프). Hãy đánh dấu endpoint không cần attach auth hoặc dùng máy khách (client / 클라이언트) riêng cho refresh.

Ngoài ra cần giới hạn thử lại (retry / 재시도). Một yêu cầu (request / 요청) protected chỉ nên thử lại (retry / 재시도) theo chính sách (policy / 정책) rõ ràng; không phải “401 thì cứ refresh mãi”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **10. Logout là một giao dịch (transaction / 트랜잭션) về bảo mật (security / 보안) trạng thái (state / 상태)** tiếp nhận điểm tựa từ **9. đơn vị từ (token / 토큰) refresh không được recurse vô hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. User-bound cục bộ (local / 로컬) dữ liệu (data / 데이터) phải có không gian tên (namespace / 네임스페이스) hoặc cleanup chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Logout là một giao dịch (transaction / 트랜잭션) về bảo mật (security / 보안) trạng thái (state / 상태)

Logout không chỉ là clear truy cập (access / 접근) đơn vị từ (token / 토큰) rồi navigate login. Cần quyết định:

- refresh/session credential nào phải revoke ở máy chủ (server / 서버);
- cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스) user-specific có phải clear không;
- pending WorkManager job có thể tiếp tục không;
- notification channel/dữ liệu (data / 데이터) bộ nhớ đệm (cache / 캐시) có chứa thông tin người dùng (user / 사용자) không;
- WebSocket/SSE liên kết (connection / 연결) phải close không;
- background sync đang dùng credential cũ xử lý thế nào;
- app có nhiều account hay chỉ một account.

Một chuỗi (sequence / 시퀀스) hợp lý:

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

Nếu revoke mạng (network / 네트워크) thất bại (fail / 실패) vì offline, cục bộ (local / 로컬) logout vẫn phải có thể hoàn thành. Backend session sẽ expire hoặc có thể được revoke lần sau tùy threat mô hình (model / 모델).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **10. Logout là một giao dịch (transaction / 트랜잭션) về bảo mật (security / 보안) trạng thái (state / 상태)** nêu điều cần giải thích; **11. User-bound cục bộ (local / 로컬) dữ liệu (data / 데이터) phải có không gian tên (namespace / 네임스페이스) hoặc cleanup chính sách (policy / 정책)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. Secret lưu trữ (storage / 저장소): DataStore không tự động là secure vault** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. User-bound cục bộ (local / 로컬) dữ liệu (data / 데이터) phải có không gian tên (namespace / 네임스페이스) hoặc cleanup chính sách (policy / 정책)

Một lỗi nghiêm trọng là người dùng (user / 사용자) A logout, người dùng (user / 사용자) B login và nhìn thấy cached dữ liệu (data / 데이터) của A. Có hai chiến lược phổ biến.

Cách đơn giản: clear user-specific cơ sở dữ liệu (database / 데이터베이스)/bảng (table / 테이블) khi logout.

Cách mạnh hơn cho multi-account: mọi row quan trọng có `accountId`, truy vấn (query / 쿼리) luôn phạm vi (scope / 범위) theo account và switch nguồn chuẩn (source of truth / 정본) theo active session. độ phức tạp (complexity / 복잡도) cao hơn nhưng hỗ trợ account switching tốt hơn.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **11. User-bound cục bộ (local / 로컬) dữ liệu (data / 데이터) phải có không gian tên (namespace / 네임스페이스) hoặc cleanup chính sách (policy / 정책)** nêu điều cần giải thích; **12. Secret lưu trữ (storage / 저장소): DataStore không tự động là secure vault** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. Biometrics không phải backend authorization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Secret lưu trữ (storage / 저장소): DataStore không tự động là secure vault

DataStore phù hợp persistence cấu hình (config / 설정)/session siêu dữ liệu (metadata / 메타데이터) nhưng không mặc định mã hóa secret. Nếu threat mô hình (model / 모델) yêu cầu bảo vệ đơn vị từ (token / 토큰) khi at-rest, cần thiết kế lưu trữ (storage / 저장소) sử dụng cryptographic key bảo vệ bởi Android Keystore hoặc solution phù hợp.

Không hard-code encryption key trong nguồn (source / 소스). Nếu key để decrypt cũng nằm plaintext ngay cạnh ciphertext thì encryption không mua được bảo mật (security / 보안) thực tế.

Cũng cần nhớ: một thiết bị compromised/rooted có threat mô hình (model / 모델) khác. Mục tiêu mobile bảo mật (security / 보안) thường là giảm exposure và tăng chi phí attack, không hứa “secret không bao giờ bị lấy”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **13. Biometrics không phải backend authorization** tiếp nhận điểm tựa từ **12. Secret lưu trữ (storage / 저장소): DataStore không tự động là secure vault** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. mạng (network / 네트워크) bảo mật (security / 보안) cấu hình (config / 설정) và HTTPS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Biometrics không phải backend authorization

`BiometricPrompt` có thể dùng để xác nhận người dùng (user / 사용자) presence trước thao tác nhạy cảm hoặc unlock một key cục bộ (local / 로컬). Nó không có nghĩa backend tự động biết yêu cầu (request / 요청) được người dùng (user / 사용자) vừa scan fingerprint.

Nếu thao tác (operation / 연산) tài chính cần step-up authentication, giao thức (protocol / 프로토콜) phải được thiết kế end-to-end: backend tạo challenge, máy khách (client / 클라이언트) thực hiện approved auth ceremony, backend verify proof/challenge phù hợp. Một Boolean `biometricPassed=true` từ máy khách (client / 클라이언트) không được coi là trusted bằng chứng (evidence / 증거).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **14. mạng (network / 네트워크) bảo mật (security / 보안) cấu hình (config / 설정) và HTTPS** tiếp nhận điểm tựa từ **13. Biometrics không phải backend authorization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Interceptor, authenticator và coroutine ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. mạng (network / 네트워크) bảo mật (security / 보안) cấu hình (config / 설정) và HTTPS

Môi trường vận hành (production / 운영 환경) app phải dùng secure vận chuyển (transport / 전송). Không tạo `TrustManager` chấp nhận mọi certificate để “fix SSL”. gỡ lỗi (debug / 디버그) môi trường (environment / 환경) nếu cần custom CA phải được giới hạn gỡ lỗi (debug / 디버그) cấu hình (configuration / 구성).

Mạng (network / 네트워크) bảo mật (security / 보안) cấu hình (config / 설정) có thể cấu hình trust anchor/cleartext chính sách (policy / 정책) theo môi trường (environment / 환경). Cleartext HTTP nên bị disable trừ use trường hợp (case / 사례) có lý do rõ ràng.

Certificate pinning có sự đánh đổi (trade-off / 트레이드오프) vận hành lớn. Pin sai hoặc certificate rotate ngoài dự kiến có thể brick mạng (network / 네트워크) cho toàn bộ installed app cho tới khi người dùng (user / 사용자) cập nhật (update / 업데이트). Chỉ dùng khi threat mô hình (model / 모델) justify và phải có backup pins/rotation plan.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **14. mạng (network / 네트워크) bảo mật (security / 보안) cấu hình (config / 설정) và HTTPS** đã nêu tiêu chí phân biệt, còn **15. Interceptor, authenticator và coroutine ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **16. lỗi (error / 오류) mô hình (model / 모델) của authentication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Interceptor, authenticator và coroutine ranh giới (boundary / 경계)

Với OkHttp, interceptor phù hợp thêm header/logging/chính sách (policy / 정책) yêu cầu (request / 요청). `Authenticator` có thể xử lý challenge như 401, nhưng hiện thực (implementation / 구현) phải tránh blocking/coroutine mismatch và duplicate refresh.

Nếu auth refresh API là suspend trong Retrofit nhưng authenticator chạy synchronous đặc tả hợp đồng (contract / 계약), đừng tùy tiện `runBlocking` trên luồng thực thi (thread / 스레드) không hiểu rõ. Có thể thiết kế synchronous đơn vị từ (token / 토큰) refresh máy khách (client / 클라이언트) riêng, hoặc centralize yêu cầu (request / 요청) ngăn xếp (stack / 스택) theo cách không gây deadlock. Điều quan trọng là hiểu mô hình thực thi (execution model / 실행 모델) của thư viện (library / 라이브러리) thay vì chỉ bản sao (copy / 복사) snippet.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **15. Interceptor, authenticator và coroutine ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **16. lỗi (error / 오류) mô hình (model / 모델) của authentication** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **17. yêu cầu (request / 요청) thử lại (retry / 재시도) phải dựa trên idempotency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. lỗi (error / 오류) mô hình (model / 모델) của authentication

Sign-in cần phân biệt ít nhất invalid credential, canceled luồng (flow / 흐름), mạng (network / 네트워크) unavailable, tỷ lệ (rate / 비율) limited, account disabled, provider lỗi (error / 오류) và unknown lỗi (error / 오류). Không nên convert tất cả thành `false`.

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

UI có thể xử lý canceled luồng (flow / 흐름) im lặng, invalid credential bằng trường dữ liệu (field / 필드) message, offline bằng thử lại (retry / 재시도) UI, và account disabled bằng hỗ trợ (support / 지원) đường dẫn (path / 경로).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **17. yêu cầu (request / 요청) thử lại (retry / 재시도) phải dựa trên idempotency** tiếp nhận điểm tựa từ **16. lỗi (error / 오류) mô hình (model / 모델) của authentication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Session trạng thái (state / 상태) và điều hướng (navigation / 내비게이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. yêu cầu (request / 요청) thử lại (retry / 재시도) phải dựa trên idempotency

GET thường có thể thử lại (retry / 재시도) an toàn hơn POST mutation, nhưng HTTP phương thức (method / 메서드) không phải toàn bộ câu chuyện. Payment create yêu cầu (request / 요청) nếu thử lại (retry / 재시도) mù có thể charge hai lần. Backend nên hỗ trợ idempotency key cho thao tác (operation / 연산) cần exactly-once nghiệp vụ (business / 비즈니스) tác động (effect / 효과) ở mức giao thức (protocol / 프로토콜).

Máy khách (client / 클라이언트) có thể tạo stable idempotency key cho một logical thao tác (operation / 연산) và reuse key khi thử lại (retry / 재시도):

```kotlin
data class PendingPayment(
    val localOperationId: UUID,
    val idempotencyKey: String,
    val payload: PaymentPayload
)
```

Mạng (network / 네트워크) thử lại (retry / 재시도) chính sách (policy / 정책) phải biết thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론), không phải một toàn cục (global / 전역) interceptor thử lại (retry / 재시도) mọi 5xx.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **18. Session trạng thái (state / 상태) và điều hướng (navigation / 내비게이션)** tiếp nhận điểm tựa từ **17. yêu cầu (request / 요청) thử lại (retry / 재시도) phải dựa trên idempotency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Credential Manager và account vòng đời (lifecycle / 생명주기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Session trạng thái (state / 상태) và điều hướng (navigation / 내비게이션)

Gốc (root / 루트) điều hướng (navigation / 내비게이션) thường phụ thuộc session trạng thái (state / 상태):

```text
Unknown -> splash/restoring
SignedOut -> auth graph
SignedIn -> main graph
```

Khi logout, reset back ngăn xếp (stack / 스택) để Back không quay về authenticated screen. Tuy nhiên protected screen vẫn không nên dựa vào điều hướng (navigation / 내비게이션) để bảo vệ dữ liệu (data / 데이터); repository/backend authorization mới là ranh giới (boundary / 경계) thật.

Tiến trình (process / 프로세스) recreation có thể khôi phục back ngăn xếp (stack / 스택) cũ. Vì vậy screen protected phải react với `SessionState` hiện tại, không giả định “đã vào đây nghĩa là chắc chắn signed in”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **18. Session trạng thái (state / 상태) và điều hướng (navigation / 내비게이션)** xác định đầu vào; **19. Credential Manager và account vòng đời (lifecycle / 생명주기)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **20. khả năng quan sát (observability / 관측 가능성) nhưng không leak credential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Credential Manager và account vòng đời (lifecycle / 생명주기)

Credential Manager giúp thống nhất password/passkey/federated sign-in experience, nhưng app vẫn cần xử lý account vòng đời (lifecycle / 생명주기) riêng: linking account, re-authentication cho thao tác (operation / 연산) nhạy cảm, logout, account deletion và server-side session revoke.

Sign in with Google cho authentication profile không đồng nghĩa app có authorization truy cập Google Drive/Gmail. Authorization tài nguyên (resource / 자원) của Google là luồng (flow / 흐름) riêng với phạm vi (scope / 범위) riêng. Đây là ví dụ điển hình của khác biệt authentication và authorization.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **19. Credential Manager và account vòng đời (lifecycle / 생명주기)** xác định đầu vào; **20. khả năng quan sát (observability / 관측 가능성) nhưng không leak credential** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **21. kiểm thử (test / 테스트) những gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. khả năng quan sát (observability / 관측 가능성) nhưng không leak credential

Auth cần telemetry vì thất bại (failure / 실패) thường khó gỡ lỗi (debug / 디버그), nhưng log phải redact secret.

Nên log sự kiện (event / 이벤트) như:

```text
auth_sign_in_started provider=passkey

auth_sign_in_failed category=network

token_refresh_started reason=near_expiry

token_refresh_failed category=invalid_grant

session_signed_out source=user_action
```

Không log truy cập (access / 접근) đơn vị từ (token / 토큰), refresh đơn vị từ (token / 토큰), password, authorization header hoặc credential assertion raw. Với crash reporting, kiểm tra breadcrumb/yêu cầu (request / 요청) logger có tự động capture header/body nhạy cảm không.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **21. kiểm thử (test / 테스트) những gì?** tiếp nhận điểm tựa từ **20. khả năng quan sát (observability / 관측 가능성) nhưng không leak credential** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Threat-model checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. kiểm thử (test / 테스트) những gì?

Đơn vị (unit / 단위) kiểm thử (test / 테스트) session máy trạng thái (state machine / 상태 머신): restore thành công/thất bại, đơn vị từ (token / 토큰) gần expiry, refresh thất bại (fail / 실패), logout. kiểm thử (test / 테스트) single-flight refresh với nhiều coroutine đồng thời để đảm bảo chỉ một lời gọi (call / 호출) refresh thực sự xảy ra. kiểm thử (test / 테스트) yêu cầu (request / 요청) thử lại (retry / 재시도) không lặp mutation ngoài chính sách (policy / 정책). kiểm thử tích hợp (integration test / 통합 테스트) cơ sở dữ liệu (database / 데이터베이스) cleanup khi switch account. UI kiểm thử (test / 테스트) gốc (root / 루트) điều hướng (navigation / 내비게이션) khi session đổi.

Một kiểm thử (test / 테스트) quan trọng:

```kotlin
@Test
fun concurrent_401_only_refreshes_once() = runTest {
    // Arrange stale token and 10 callers.
    // Make refresh fake count invocations.
    // Launch callers concurrently.
    // Assert refresh count == 1 and all callers receive new token.
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **22. Threat-model checklist** tiếp nhận điểm tựa từ **21. kiểm thử (test / 테스트) những gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. cấp cao (senior / 시니어) notes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Threat-model checklist

Trước khi ship auth, hãy trả lời bằng văn bản:

Ai là attacker? đơn vị từ (token / 토큰) theft qua log, malware/cục bộ (local / 로컬) extraction, MITM, modified APK, credential stuffing hay stolen thiết bị (device / 장치)? Asset cần bảo vệ là gì? máy chủ (server / 서버) có revoke session không? truy cập (access / 접근) đơn vị từ (token / 토큰) sống bao lâu? Refresh rotation thế nào? App có thể detect account/session vô hiệu hóa (invalidation / 무효화) server-side không? cục bộ (local / 로컬) dữ liệu (data / 데이터) sau logout xử lý ra sao? Backup có vô tình chứa credential không? Deep link có thể đưa người dùng (user / 사용자) vào protected hành động (action / 동작) mà không revalidate không?

Nếu không biết threat mô hình (model / 모델), rất dễ dùng kỹ thuật “security-looking” nhưng không bảo vệ đúng asset.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 02 — Authentication, Session, đơn vị từ (token / 토큰) Refresh và mạng (network / 네트워크) bảo mật (security / 보안)**, **23. cấp cao (senior / 시니어) notes** tiếp nhận điểm tựa từ **22. Threat-model checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 23. cấp cao (senior / 시니어) notes

Không viết đơn vị từ (token / 토큰) refresh ở từng repository. Nó là cross-cutting hạ tầng (infrastructure / 인프라) với tính đồng thời (concurrency / 동시성) ngữ nghĩa (semantics / 의미론) rõ ràng. Không expose đơn vị từ (token / 토큰) lên ViewModel. Không tin role/claim chỉ vì UI parse được. Không log auth header. Không thử lại (retry / 재시도) mutation mù. Không dùng biometric như máy chủ (server / 서버) authorization. Không nghĩ obfuscation là secret lưu trữ (storage / 저장소).

Một session kiến trúc (architecture / 아키텍처) tốt cho phép kể luồng (flow / 흐름) rất rõ: **credential ceremony → backend xác minh (verification / 확인) → ứng dụng (application / 애플리케이션) session → đơn vị từ (token / 토큰) lưu trữ (storage / 저장소) ranh giới (boundary / 경계) → authenticated yêu cầu (request / 요청) → refresh single-flight → observable session trạng thái (state / 상태) → deterministic logout**. Mỗi bước có đơn vị sở hữu (owner / 오너), thất bại (failure / 실패) mô hình (model / 모델) và kiểm thử (test / 테스트) riêng.

> **Bàn giao:** Sau **23. cấp cao (senior / 시니어) notes**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
