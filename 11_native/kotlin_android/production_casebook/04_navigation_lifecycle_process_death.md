# Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bốn loại thời gian tồn tại (lifetime / 수명) cần phân biệt** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. remember không phải persistence** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Điều hướng (navigation / 내비게이션) thường được học như `navController.navigate("detail/123")`, còn vòng đời (lifecycle / 생명주기) được học riêng như một sơ đồ `onCreate` → `onStart` → `onResume`. Trong môi trường vận hành (production / 운영 환경), hai chủ đề này gắn chặt: một destination có thời gian tồn tại (lifetime / 수명) riêng, back ngăn xếp (stack / 스택) có thể được restore, app có thể mở từ deep link khi tiến trình (process / 프로세스) chưa tồn tại, cấu hình (configuration / 구성) thay đổi (change / 변경) không giống tiến trình (process / 프로세스) death, và trạng thái (state / 상태) của screen cần được phân loại để biết cái gì nằm trong `remember`, `rememberSaveable`, `ViewModel`, `SavedStateHandle` hay persistent lưu trữ (storage / 저장소).

## 1. Bốn loại thời gian tồn tại (lifetime / 수명) cần phân biệt

Một mô hình tư duy (mental model / 사고 모델) hữu ích là chia trạng thái (state / 상태) theo thời gian sống.

**Recomposition thời gian tồn tại (lifetime / 수명)**: biến chỉ cần tồn tại qua recomposition trong cùng composition. Dùng `remember`.

**cấu hình (configuration / 구성)/recreation thời gian tồn tại (lifetime / 수명)**: trạng thái (state / 상태) UI nhỏ cần giữ khi Activity recreate, như tab/filter/văn bản (text / 텍스트) draft nhỏ. `rememberSaveable` hoặc `SavedStateHandle` phù hợp tùy đơn vị sở hữu (owner / 오너).

**điều hướng (navigation / 내비게이션) destination thời gian tồn tại (lifetime / 수명)**: trạng thái (state / 상태) thuộc một screen khi destination còn trên back ngăn xếp (stack / 스택). ViewModel scoped theo điều hướng (navigation / 내비게이션) entry thường phù hợp.

**tiến trình (process / 프로세스)/persistent thời gian tồn tại (lifetime / 수명)**: dữ liệu (data / 데이터) cần khôi phục sau tiến trình (process / 프로세스) chết lâu hoặc app restart. Dữ liệu lớn/quan trọng phải từ Room/DataStore/máy chủ (server / 서버), không trông chờ Bundle.

Phân loại đúng thời gian tồn tại (lifetime / 수명) quan trọng hơn thuộc tên API.

> **Chuyển mạch:** Mỗi lifetime có persistence guarantee khác nhau; `remember` chỉ giữ composition state, còn ViewModel qua configuration change nhưng không đảm bảo process-death recovery.

## 2. `remember` không phải persistence
Phần này nối mạch Android vừa học với “2. `remember` không phải persistence”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
var expanded by remember { mutableStateOf(false) }
```

Giá trị tồn tại qua recomposition nhưng mất nếu composable rời composition hoặc tiến trình (process / 프로세스)/activity recreate tùy cấu trúc.

`rememberSaveable` dùng saved instance trạng thái (state / 상태) cho kiểu (type / 타입) saveable:

```kotlin
var query by rememberSaveable { mutableStateOf("") }
```

Không nên save đối tượng (object / 객체) lớn, bitmap, cơ sở dữ liệu (database / 데이터베이스) kết quả (result / 결과) hoặc secret vào saved trạng thái (state / 상태) chỉ để “khỏi tải (load / 로드) lại”. Bundle có kích thước (size / 크기) limit và tiến trình (process / 프로세스) restore cần lightweight key/trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **2. remember không phải persistence** xác định đầu vào; **3. ViewModel sống qua cấu hình (configuration / 구성) thay đổi (change / 변경), không bảo đảm qua tiến trình (process / 프로세스) death** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. điều hướng (navigation / 내비게이션) argument nên là định danh (identity / 식별자), không phải đối tượng (object / 객체) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. ViewModel sống qua cấu hình (configuration / 구성) thay đổi (change / 변경), không bảo đảm qua tiến trình (process / 프로세스) death

Đây là nhầm lẫn rất phổ biến. ViewModel được giữ khi cấu hình (configuration / 구성) thay đổi (change / 변경) nhưng tiến trình (process / 프로세스) bị hệ điều hành kill thì bộ nhớ (memory / 메모리) biến mất.

Vì vậy:

```kotlin
class DetailViewModel(
    savedStateHandle: SavedStateHandle,
    repository: ArticleRepository
) : ViewModel() {
    private val articleId: String = checkNotNull(savedStateHandle["articleId"])
    val article = repository.observeArticle(articleId)
}
```

ViewModel chỉ cần giữ **key** đủ để reconstruct trạng thái (state / 상태) từ repository. Không cần persist toàn bộ Article đối tượng (object / 객체) trong SavedStateHandle.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **3. ViewModel sống qua cấu hình (configuration / 구성) thay đổi (change / 변경), không bảo đảm qua tiến trình (process / 프로세스) death** xác định đầu vào; **4. điều hướng (navigation / 내비게이션) argument nên là định danh (identity / 식별자), không phải đối tượng (object / 객체) đồ thị (graph / 그래프)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. Type-safe tuyến (route / 경로) với điều hướng (navigation / 내비게이션) Compose** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. điều hướng (navigation / 내비게이션) argument nên là định danh (identity / 식별자), không phải đối tượng (object / 객체) đồ thị (graph / 그래프)

Đừng pass một lĩnh vực (domain / 도메인) đối tượng (object / 객체) lớn qua tuyến (route / 경로). Pass ID hoặc minimal thành phần nguyên thủy (primitive / 기본 요소)/serializable argument rồi tải (load / 로드) từ nguồn chuẩn (source of truth / 정본).

Lợi ích:

- deep link có thể tạo destination chỉ từ URL;
- tiến trình (process / 프로세스) restore không cần serialize đối tượng (object / 객체) lớn;
- detail luôn đọc latest nguồn chuẩn (source of truth / 정본);
- tuyến (route / 경로) đặc tả hợp đồng (contract / 계약) ổn định hơn mô hình (model / 모델) nội bộ.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **5. Type-safe tuyến (route / 경로) với điều hướng (navigation / 내비게이션) Compose** tiếp nhận điểm tựa từ **4. điều hướng (navigation / 내비게이션) argument nên là định danh (identity / 식별자), không phải đối tượng (object / 객체) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Route-level composable và screen-level composable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Type-safe tuyến (route / 경로) với điều hướng (navigation / 내비게이션) Compose

Điều hướng (navigation / 내비게이션) Compose hiện hỗ trợ type-safe tuyến (route / 경로) dựa trên Kotlin serialization. mô hình tư duy (mental model / 사고 모델):

```kotlin
@Serializable
data object Home

@Serializable
data class ArticleDetail(val articleId: String)
```

Đồ thị (graph / 그래프):

```kotlin
NavHost(
    navController = navController,
    startDestination = Home
) {
    composable<Home> {
        HomeRoute(
            onOpenArticle = { id ->
                navController.navigate(ArticleDetail(id))
            }
        )
    }

    composable<ArticleDetail> { backStackEntry ->
        val route = backStackEntry.toRoute<ArticleDetail>()
        ArticleDetailRoute(articleId = route.articleId)
    }
}
```

Type-safe tuyến (route / 경로) giảm string parsing và mismatch argument, nhưng vẫn cần thiết kế (design / 설계) điều hướng (navigation / 내비게이션) đặc tả hợp đồng (contract / 계약) tốt.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **6. Route-level composable và screen-level composable** tiếp nhận điểm tựa từ **5. Type-safe tuyến (route / 경로) với điều hướng (navigation / 내비게이션) Compose** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. điều hướng (navigation / 내비게이션) không phải toàn cục (global / 전역) sự kiện (event / 이벤트) bus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Route-level composable và screen-level composable

Tuyến (route / 경로) nên kết nối điều hướng (navigation / 내비게이션)/ViewModel; Screen nên tập trung kết xuất (render / 렌더링).

```kotlin
@Composable
fun ArticleDetailRoute(
    articleId: String,
    viewModel: ArticleDetailViewModel,
    onBack: () -> Unit
) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()

    ArticleDetailScreen(
        state = state,
        onBack = onBack,
        onRetry = viewModel::retry
    )
}
```

Điều này tránh composable con giữ `NavController` khắp nơi và giúp kiểm thử (test / 테스트) pure UI dễ hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **7. điều hướng (navigation / 내비게이션) không phải toàn cục (global / 전역) sự kiện (event / 이벤트) bus** tiếp nhận điểm tựa từ **6. Route-level composable và screen-level composable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Back ngăn xếp (stack / 스택) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. điều hướng (navigation / 내비게이션) không phải toàn cục (global / 전역) sự kiện (event / 이벤트) bus

Một anti-pattern là đặt `NavController` vào singleton hoặc repository. dữ liệu (data / 데이터) tầng (layer / 계층) không nên biết người dùng (user / 사용자) đang ở screen nào.

Điều hướng (navigation / 내비게이션) quyết định (decision / 결정) thường thuộc UI coordination. lĩnh vực (domain / 도메인) có thể trả kết quả (result / 결과)/trạng thái (state / 상태) như `PaymentCompleted(orderId)`, còn tuyến (route / 경로)/UI quyết định navigate tới receipt.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **8. Back ngăn xếp (stack / 스택) ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **7. điều hướng (navigation / 내비게이션) không phải toàn cục (global / 전역) sự kiện (event / 이벤트) bus** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Multiple tabs và trạng thái (state / 상태) restoration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Back ngăn xếp (stack / 스택) ngữ nghĩa (semantics / 의미론)

Hiểu `popBackStack`, `popUpTo`, inclusive, `launchSingleTop`, `restoreState` quan trọng hơn memorize snippet.

Ví dụ sau login, bạn thường không muốn Back quay lại login:

```kotlin
navController.navigate(Home) {
    popUpTo<Login> { inclusive = true }
}
```

Sau logout, protected back ngăn xếp (stack / 스택) cần được reset tương tự. Nhưng dữ liệu (data / 데이터) bảo mật (security / 보안) không được dựa vào việc xóa back ngăn xếp (stack / 스택); protected repository/backend vẫn phải kiểm tra session.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **9. Multiple tabs và trạng thái (state / 상태) restoration** tiếp nhận điểm tựa từ **8. Back ngăn xếp (stack / 스택) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Deep link là bên ngoài (external / 외부) đầu vào (input / 입력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Multiple tabs và trạng thái (state / 상태) restoration

Bottom điều hướng (navigation / 내비게이션) thường muốn mỗi tab giữ back ngăn xếp (stack / 스택) riêng. Nếu mỗi lần đổi tab bạn tạo đồ thị (graph / 그래프) mới hoặc navigate vô hạn, back ngăn xếp (stack / 스택) có thể phình.

Mẫu (pattern / 패턴) thường dùng `launchSingleTop`, `restoreState` và `popUpTo` start destination với `saveState` để preserve tab trạng thái (state / 상태). Quan trọng là kiểm thử (test / 테스트) hành vi (behavior / 동작): đổi tab, drill detail, đổi tab khác, quay lại phải ở đúng vị trí sản phẩm (product / 제품) mong muốn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **10. Deep link là bên ngoài (external / 외부) đầu vào (input / 입력)** tiếp nhận điểm tựa từ **9. Multiple tabs và trạng thái (state / 상태) restoration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. App Link và custom scheme** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Deep link là bên ngoài (external / 외부) đầu vào (input / 입력)

Deep link có thể đến từ trình duyệt (browser / 브라우저), notification, email hoặc app khác. Vì vậy tuyến (route / 경로) argument là **untrusted đầu vào (input / 입력)**.

Không được giả định `articleId` hợp lệ chỉ vì tuyến (route / 경로) type-safe. Validate ID, check authorization, handle thực thể (entity / 엔터티) không tồn tại và session chưa login.

```text
external URI
→ parse + validate
→ resolve app route
→ auth/authorization gate
→ load data
→ render or safe error
```

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **11. App Link và custom scheme** tiếp nhận điểm tựa từ **10. Deep link là bên ngoài (external / 외부) đầu vào (input / 입력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Authentication-gated deep link** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. App Link và custom scheme

Custom scheme như `myapp://article/123` dễ đăng ký nhưng app khác cũng có thể claim scheme.

Android App Links dùng HTTPS lĩnh vực (domain / 도메인) association để hệ thống có thể verify quyền sở hữu (ownership / 소유권). Với link công khai (public / 공개) từ web, App Link thường tạo trust mô hình (model / 모델) tốt hơn.

Dù verified link, đầu vào (input / 입력) đường dẫn (path / 경로)/truy vấn (query / 쿼리) vẫn cần kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **12. Authentication-gated deep link** tiếp nhận điểm tựa từ **11. App Link và custom scheme** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Notification điều hướng (navigation / 내비게이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Authentication-gated deep link

Một trường hợp (case / 사례) điển hình: người dùng (user / 사용자) mở link `/orders/123`, nhưng chưa login.

Sai mẫu (pattern / 패턴): bỏ link và chuyển login; sau login người dùng (user / 사용자) mất ngữ cảnh (context / 맥락).

Tốt hơn:

```text
Deep link arrives
→ parse target destination
→ session SignedOut
→ store small pending navigation intent
→ login
→ validate target against current account
→ navigate to target
```

Pending mục tiêu (target / 대상) phải minimal và safe. Không persist secret hoặc raw unvalidated payload tùy tiện.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **13. Notification điều hướng (navigation / 내비게이션)** tiếp nhận điểm tựa từ **12. Authentication-gated deep link** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. cấu hình (configuration / 구성) thay đổi (change / 변경) khác tiến trình (process / 프로세스) death** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Notification điều hướng (navigation / 내비게이션)

Notification tap cũng là deep entry. PendingIntent flags, unique yêu cầu (request / 요청) mã (code / 코드) và tác vụ (task / 작업)/back-stack hành vi (behavior / 동작) cần được thiết kế.

Nếu notification dẫn đến message detail, app có thể đang:

- chưa chạy;
- background với existing tác vụ (task / 작업);
- foreground ở chính message đó;
- signed out;
- người dùng (user / 사용자) đã switch account.

Tuyến (route / 경로) handler phải idempotent và account-aware.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **13. Notification điều hướng (navigation / 내비게이션)** xác định đầu vào; **14. cấu hình (configuration / 구성) thay đổi (change / 변경) khác tiến trình (process / 프로세스) death** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **15. Cách kiểm thử (test / 테스트) tiến trình (process / 프로세스) recreation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. cấu hình (configuration / 구성) thay đổi (change / 변경) khác tiến trình (process / 프로세스) death

Cấu hình (configuration / 구성) thay đổi (change / 변경) tạo Activity instance mới trong cùng tiến trình (process / 프로세스). ViewModel thường được giữ.

Tiến trình (process / 프로세스) death xóa bộ nhớ (memory / 메모리). Khi người dùng (user / 사용자) quay lại từ recent apps, Android có thể recreate tác vụ (task / 작업)/back ngăn xếp (stack / 스택) từ saved trạng thái (state / 상태). ViewModel mới được tạo. Nếu ViewModel giả định một in-memory singleton còn dữ liệu (data / 데이터) thì bug xuất hiện.

Kiểm thử (test / 테스트) tiến trình (process / 프로세스) death riêng, không coi rotation là đủ.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **14. cấu hình (configuration / 구성) thay đổi (change / 변경) khác tiến trình (process / 프로세스) death** xác định đầu vào; **15. Cách kiểm thử (test / 테스트) tiến trình (process / 프로세스) recreation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. SavedStateHandle không phải cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Cách kiểm thử (test / 테스트) tiến trình (process / 프로세스) recreation

Trong manual kiểm thử (test / 테스트), có thể dùng nhà phát triển (developer / 개발자) Options / “Don’t keep activities” cho một số vòng đời (lifecycle / 생명주기) issue, nhưng nó không hoàn toàn mô phỏng tiến trình (process / 프로세스) death.

Một kỹ thuật thực tế là background app rồi dùng ADB kill tiến trình (process / 프로세스) hoặc Android Studio tooling phù hợp, sau đó restore tác vụ (task / 작업). Mục tiêu kiểm thử (test / 테스트):

- destination restore đúng;
- tuyến (route / 경로) argument đủ để reload;
- unsaved transient trạng thái (state / 상태) hành vi (behavior / 동작) đúng;
- repository reconnect dữ liệu (data / 데이터) nguồn (source / 소스);
- session restore trước protected screen.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, cơ chế trong **15. Cách kiểm thử (test / 테스트) tiến trình (process / 프로세스) recreation** cần được kiểm chứng bằng dấu vết cụ thể; **16. SavedStateHandle không phải cơ sở dữ liệu (database / 데이터베이스)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **17. Lifecycle-aware luồng (flow / 흐름) collection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. SavedStateHandle không phải cơ sở dữ liệu (database / 데이터베이스)

`SavedStateHandle` hợp với ID, filter, draft nhỏ, step number. Dữ liệu user-created quan trọng chưa gửi máy chủ (server / 서버) không nên chỉ dựa vào saved trạng thái (state / 상태).

Ví dụ form dài có thể autosave draft vào cục bộ (local / 로컬) DB nếu mất dữ liệu là unacceptable.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **16. SavedStateHandle không phải cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **17. Lifecycle-aware luồng (flow / 흐름) collection** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. LaunchedEffect và lifecycle của effect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Lifecycle-aware luồng (flow / 흐름) collection

Compose UI nên collect observable trạng thái (state / 상태) theo vòng đời (lifecycle / 생명주기) để không giữ unnecessary collection khi screen không active.

```kotlin
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

Ở View hệ thống (system / 시스템) có `repeatOnLifecycle`:

```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { render(it) }
    }
}
```

Không dùng `launchWhenStarted` như một cargo-cult nếu ngữ nghĩa (semantics / 의미론) suspension/tài nguyên (resource / 자원) upstream không phù hợp. Hiểu vòng đời (lifecycle / 생명주기) của producer/collector mới quan trọng.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **17. Lifecycle-aware luồng (flow / 흐름) collection** xác định đầu vào; **18. LaunchedEffect và lifecycle của effect** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **19. DisposableEffect cho registration có cleanup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. `LaunchedEffect` và lifecycle của effect
Phần này nối mạch Android vừa học với “18. `LaunchedEffect` và lifecycle của effect”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
LaunchedEffect(articleId) {
    viewModel.load(articleId)
}
```

Tác động (effect / 효과) restart khi key thay đổi và cancel khi rời composition. Nhưng nếu `load` là screen initialization, thường ViewModel init/repository stream có ngữ nghĩa (semantics / 의미론) ổn định hơn. Tránh dùng `LaunchedEffect(Unit)` để biến Composable thành imperative controller cho mọi thứ.

Tác động (effect / 효과) phù hợp khi cần side tác động (effect / 효과) gắn với composition/key, ví dụ scroll, analytics screen exposure, focus hoặc collect one-off UI tác động (effect / 효과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **18. LaunchedEffect và lifecycle của effect** xác định đầu vào; **19. DisposableEffect cho registration có cleanup** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **20. rememberUpdatedState khi callback thay đổi nhưng tác động (effect / 효과) không nên restart** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. `DisposableEffect` cho registration có cleanup

Khi cầu nối (bridge / 브리지) listener API:

```kotlin
DisposableEffect(owner) {
    val observer = LifecycleEventObserver { _, event ->
        // react
    }
    owner.lifecycle.addObserver(observer)

    onDispose {
        owner.lifecycle.removeObserver(observer)
    }
}
```

Registration và cleanup phải cùng ranh giới (boundary / 경계) để tránh leak.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **20. rememberUpdatedState khi callback thay đổi nhưng tác động (effect / 효과) không nên restart** tiếp nhận điểm tựa từ **19. DisposableEffect cho registration có cleanup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. điều hướng (navigation / 내비게이션) kết quả (result / 결과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. `rememberUpdatedState` khi callback thay đổi nhưng tác động (effect / 효과) không nên restart

Một long-lived tác động (effect / 효과) có thể cần callback mới nhất mà không restart timer/listener:

```kotlin
val latestOnTimeout by rememberUpdatedState(onTimeout)

LaunchedEffect(Unit) {
    delay(5_000)
    latestOnTimeout()
}
```

Đây là ví dụ Compose tác động (effect / 효과) ngữ nghĩa (semantics / 의미론) không thể hiểu chỉ bằng “API này dùng khi nào” mà phải hiểu thời gian tồn tại (lifetime / 수명)/key.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **21. điều hướng (navigation / 내비게이션) kết quả (result / 결과)** tiếp nhận điểm tựa từ **20. rememberUpdatedState khi callback thay đổi nhưng tác động (effect / 효과) không nên restart** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. dùng chung (shared / 공유) ViewModel phạm vi (scope / 범위) phải có lý do** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. điều hướng (navigation / 내비게이션) kết quả (result / 결과)

Screen B edit item rồi quay về A. Có nhiều lựa chọn:

- cơ sở dữ liệu (database / 데이터베이스) là nguồn chuẩn (source of truth / 정본): B cập nhật (update / 업데이트) repository; A đang observe nên tự nhận cập nhật (update / 업데이트);
- small one-off kết quả (result / 결과): SavedStateHandle của previous entry;
- dùng chung (shared / 공유) scoped ViewModel nếu hai destination thực sự share workflow trạng thái (state / 상태).

Nếu dữ liệu (data / 데이터) đã nằm trong repository, truyền đối tượng (object / 객체) quay lại thường tạo duplicate trạng thái (state / 상태) không cần thiết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **22. dùng chung (shared / 공유) ViewModel phạm vi (scope / 범위) phải có lý do** tiếp nhận điểm tựa từ **21. điều hướng (navigation / 내비게이션) kết quả (result / 결과)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Nested đồ thị (graph / 그래프) là ranh giới (boundary / 경계) workflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. dùng chung (shared / 공유) ViewModel phạm vi (scope / 범위) phải có lý do

Checkout nhiều bước có thể dùng ViewModel scoped theo điều hướng (navigation / 내비게이션) đồ thị (graph / 그래프) để giữ workflow trạng thái (state / 상태). Nhưng toàn cục (global / 전역) Activity-scoped ViewModel cho mọi screen dễ biến thành god trạng thái (state / 상태) holder và leak coupling.

Phạm vi (scope / 범위) trạng thái (state / 상태) theo nhỏ nhất thời gian tồn tại (lifetime / 수명) đáp ứng yêu cầu (requirement / 요구사항).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **22. dùng chung (shared / 공유) ViewModel phạm vi (scope / 범위) phải có lý do** đã nêu tiêu chí phân biệt, còn **23. Nested đồ thị (graph / 그래프) là ranh giới (boundary / 경계) workflow** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **24. Adaptive điều hướng (navigation / 내비게이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Nested đồ thị (graph / 그래프) là ranh giới (boundary / 경계) workflow

Auth đồ thị (graph / 그래프), onboarding đồ thị (graph / 그래프), checkout đồ thị (graph / 그래프) có thể là nested đồ thị (graph / 그래프). Nó giúp phạm vi (scope / 범위) ViewModel và back-stack chính sách (policy / 정책) theo workflow.

Nested đồ thị (graph / 그래프) không nên chỉ dùng để làm tệp (file / 파일) điều hướng (navigation / 내비게이션) “đẹp”; nó có ý nghĩa khi destination share vòng đời (lifecycle / 생명주기)/luồng (flow / 흐름).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **23. Nested đồ thị (graph / 그래프) là ranh giới (boundary / 경계) workflow** đã nêu tiêu chí phân biệt, còn **24. Adaptive điều hướng (navigation / 내비게이션)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **25. Foldable và cửa sổ (window / 윈도우) kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Adaptive điều hướng (navigation / 내비게이션)

Phone có thể dùng bottom điều hướng (navigation / 내비게이션), tablet có điều hướng (navigation / 내비게이션) rail hoặc list-detail pane. kiến trúc (architecture / 아키텍처) tốt không encode nghiệp vụ (business / 비즈니스) điều hướng (navigation / 내비게이션) trực tiếp vào widget cụ thể.

Một selection như `selectedArticleId` có thể ở trạng thái (state / 상태) holder; compact bố cục (layout / 레이아웃) navigate detail destination, expanded bố cục (layout / 레이아웃) hiển thị detail pane cùng screen. Cùng một trạng thái (state / 상태), presentation/điều hướng (navigation / 내비게이션) khác theo cửa sổ (window / 윈도우) kích thước (size / 크기).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **25. Foldable và cửa sổ (window / 윈도우) kích thước (size / 크기)** tiếp nhận điểm tựa từ **24. Adaptive điều hướng (navigation / 내비게이션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. khả năng tiếp cận (accessibility / 접근성) và điều hướng (navigation / 내비게이션) focus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Foldable và cửa sổ (window / 윈도우) kích thước (size / 크기)

Không hard-code “tablet nếu width > X dp” rải rác. Dùng adaptive/cửa sổ (window / 윈도우) APIs và centralize bố cục (layout / 레이아웃) chính sách (policy / 정책). Khi posture/cửa sổ (window / 윈도우) thay đổi thời gian chạy (runtime / 런타임), trạng thái (state / 상태) phải giữ đúng thực thể (entity / 엔터티) selection.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **26. khả năng tiếp cận (accessibility / 접근성) và điều hướng (navigation / 내비게이션) focus** tiếp nhận điểm tựa từ **25. Foldable và cửa sổ (window / 윈도우) kích thước (size / 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Unsaved form và back** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. khả năng tiếp cận (accessibility / 접근성) và điều hướng (navigation / 내비게이션) focus

Sau điều hướng (navigation / 내비게이션), screen reader focus nên có hành vi hợp lý. Dialog/bottom sheet phải có ngữ nghĩa (semantic / 의미적) role và focus management đúng. Back gesture/hệ thống (system / 시스템) back không chỉ là technical callback; nó là UX đặc tả hợp đồng (contract / 계약).

Predictive back và chuyển tiếp (transition / 전이) hiện đại yêu cầu điều hướng (navigation / 내비게이션) ngăn xếp (stack / 스택) có ngữ nghĩa (semantics / 의미론) đúng, không override Back tùy tiện để chống người dùng (user / 사용자) rời screen. Nếu có unsaved changes, mô hình (model / 모델) tường minh (explicit / 명시적) confirmation trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **27. Unsaved form và back** tiếp nhận điểm tựa từ **26. khả năng tiếp cận (accessibility / 접근성) và điều hướng (navigation / 내비게이션) focus** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. điều hướng (navigation / 내비게이션) kiểm thử (test / 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Unsaved form và back

Không nên khối (block / 블록) back bằng một toàn cục (global / 전역) flag khó hiểu. Form trạng thái (state / 상태) biết nó dirty hay không:

```kotlin
data class EditUiState(
    val draft: Draft,
    val original: Draft,
    val showDiscardDialog: Boolean = false
) {
    val isDirty: Boolean get() = draft != original
}
```

Back sự kiện (event / 이벤트) nếu dirty thì show confirm. Nếu tiến trình (process / 프로세스) death, nếu draft quan trọng thì persist draft; dialog trạng thái (state / 상태) có thể không cần persist tùy UX.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **28. điều hướng (navigation / 내비게이션) kiểm thử (test / 테스트)** tiếp nhận điểm tựa từ **27. Unsaved form và back** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. cấp cao (senior / 시니어) notes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. điều hướng (navigation / 내비게이션) kiểm thử (test / 테스트)

Kiểm thử (test / 테스트) ở nhiều tầng.

Pure ViewModel kiểm thử (test / 테스트): session/payment trạng thái (state / 상태) dẫn đến điều hướng (navigation / 내비게이션) tín hiệu (signal / 신호)/trạng thái (state / 상태) đúng.

Điều hướng (navigation / 내비게이션) kiểm thử tích hợp (integration test / 통합 테스트): tuyến (route / 경로) parse, đồ thị (graph / 그래프) hành động (action / 동작), back ngăn xếp (stack / 스택).

Compose UI kiểm thử (test / 테스트): click element và assert destination ngữ nghĩa (semantics / 의미론).

Deep link kiểm thử (test / 테스트): invalid ID, signed-out người dùng (user / 사용자), missing thực thể (entity / 엔터티), multiple entry trạng thái (state / 상태).

Tiến trình (process / 프로세스) recreation kiểm thử (test / 테스트): restored entry tải (load / 로드) được từ ID.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 04 — điều hướng (navigation / 내비게이션), Deep Link, vòng đời (lifecycle / 생명주기) và tiến trình (process / 프로세스) Death**, **29. cấp cao (senior / 시니어) notes** tiếp nhận điểm tựa từ **28. điều hướng (navigation / 내비게이션) kiểm thử (test / 테스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 29. cấp cao (senior / 시니어) notes

Điều hướng (navigation / 내비게이션) bug thường là quyền sở hữu trạng thái (state ownership / 상태 소유권) bug disguised. Nếu tuyến (route / 경로) phải mang đối tượng (object / 객체) lớn để screen hoạt động, source-of-truth ranh giới (boundary / 경계) có thể sai. Nếu tiến trình (process / 프로세스) death làm app crash, restoration đặc tả hợp đồng (contract / 계약) chưa đủ. Nếu logout rồi Back xem được protected dữ liệu (data / 데이터), session/dữ liệu (data / 데이터) ranh giới (boundary / 경계) có vấn đề. Nếu deep link bypass kiểm tra hợp lệ (validation / 검증), bên ngoài (external / 외부) đầu vào (input / 입력) ranh giới (boundary / 경계) sai.

Hãy thiết kế destination như một hàm (function / 함수) nhận **minimal stable định danh (identity / 식별자) + hiện tại (current / 현재) ứng dụng (application / 애플리케이션) trạng thái (state / 상태)** và có khả năng reconstruct UI. Khi làm được điều đó, điều hướng (navigation / 내비게이션), deep link, adaptive bố cục (layout / 레이아웃) và tiến trình (process / 프로세스) restoration đều đơn giản hơn.

> **Bàn giao:** Sau **29. cấp cao (senior / 시니어) notes**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
