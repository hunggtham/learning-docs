# Case 06 — Legacy Android Migration và Modularization

Nhiều Android developer không bắt đầu từ một greenfield Compose project. Họ bước vào codebase có XML, Fragment, custom View, callback, RxJava, LiveData, AsyncTask-era utility, singleton service locator, Java class, `startActivityForResult`, shared mutable state và Gradle script tích lũy qua nhiều năm. Nếu approach là “rewrite toàn bộ sang Compose/Clean Architecture”, risk thường tăng mạnh: business regression, release freeze, merge conflict, mất knowledge và kéo dài migration vô hạn.

Chương này trình bày cách migrate theo **strangler pattern**: tạo boundary mới, chuyển từng vertical slice, giữ interoperability rõ ràng và xóa legacy khi replacement đã chứng minh production.

## 1. Đầu tiên phải inventory, không code ngay

Trước migration, lập bản đồ:

```text
entry points
→ Activity/Fragment graph
→ shared ViewModel/singleton/global state
→ data sources
→ network stack
→ persistence
→ background work
→ analytics/security dependencies
→ test coverage
```

Đồng thời tìm risk hotspot: payment/auth, device integration, deep link, file upload, WebView, database migration, push notification.

Một màn hình 2.000 dòng nhưng ít user có thể risk thấp hơn một utility 50 dòng dùng ở mọi payment flow.

## 2. Phân biệt legacy, deprecated và simply-not-fashionable

XML/View không phải “sai”. Fragment cũng không mặc định cần xóa. Một API cũ nhưng stable có thể tiếp tục hợp lý trong module maintenance.

Chỉ migrate khi có mục tiêu: giảm bug/lifecycle complexity, unify stack, improve testability, remove unsupported dependency, speed feature delivery hoặc satisfy platform requirement.

Migration không có business/engineering outcome rõ ràng dễ biến thành rewrite vì sở thích.

## 3. Establish seam trước khi replace implementation

Nếu Fragment gọi trực tiếp Retrofit, SQLite helper và analytics, trước tiên tạo repository/use-case boundary mà UI cũ vẫn dùng được.

```kotlin
interface UserRepository {
    fun observeUser(id: String): Flow<User>
    suspend fun updateProfile(command: UpdateProfileCommand)
}
```

Sau khi seam ổn định, implementation có thể migrate network/database mà UI không cần đổi cùng lúc.

Đây là nguyên tắc quan trọng: **decouple first, modernize second**.

## 4. Java ↔ Kotlin migration

Kotlin interoperates Java tốt nhưng có edge case.

Java platform type không biết nullability chính xác. Annotate Java API (`@Nullable`, `@NonNull`) nếu có thể để Kotlin compiler giúp bạn.

Java bean getter/setter có thể xuất hiện như Kotlin property. SAM interface có lambda interop. Checked exception không được Kotlin enforce. Wildcard/generic variance có thể cần `@JvmSuppressWildcards` hoặc API design cẩn thận.

Không convert 500 file Java bằng tool rồi gọi là migration hoàn tất. Chọn boundary, chạy test và refactor idiomatic Kotlin dần.

## 5. Callback → suspend

Legacy API:

```kotlin
interface Callback<T> {
    fun onSuccess(value: T)
    fun onError(error: Throwable)
}
```

Có thể bridge one-shot callback bằng `suspendCancellableCoroutine`:

```kotlin
suspend fun LegacyApi.awaitUser(id: String): User =
    suspendCancellableCoroutine { continuation ->
        val call = getUser(id, object : Callback<User> {
            override fun onSuccess(value: User) {
                if (continuation.isActive) continuation.resume(value)
            }

            override fun onError(error: Throwable) {
                if (continuation.isActive) continuation.resumeWithException(error)
            }
        })

        continuation.invokeOnCancellation {
            call.cancel()
        }
    }
```

Cancellation bridge rất quan trọng. Nếu coroutine cancel mà underlying request vẫn chạy và giữ callback/UI reference, migration chỉ đổi syntax chứ chưa sửa lifecycle.

## 6. Listener/stream → callbackFlow

Listener nhiều event phù hợp với `callbackFlow`:

```kotlin
fun LocationClient.locations(): Flow<Location> = callbackFlow {
    val listener = object : LocationListener {
        override fun onLocation(location: Location) {
            trySend(location)
        }
    }

    register(listener)
    awaitClose { unregister(listener) }
}
```

Luôn có cleanup. `callbackFlow` không tự biết cách unregister listener của library.

## 7. LiveData → Flow không cần big-bang

ViewModel cũ có thể expose LiveData cho XML Fragment. Data layer mới có thể dùng Flow rồi adapt ở boundary.

```kotlin
val usersLiveData = repository.observeUsers().asLiveData()
```

Ngược lại có thể bridge LiveData thành Flow nếu cần. Mục tiêu là move source of truth dần, không force toàn bộ app đổi cùng PR.

Khi Compose screen thay Fragment, có thể dùng StateFlow trực tiếp với lifecycle-aware collection.

## 8. RxJava → Coroutine/Flow

Nếu codebase RxJava lớn, đừng replace operator-by-operator một cách máy móc. Rx có semantics scheduler/backpressure/disposal riêng.

Chọn module/feature boundary. Bridge Single/Maybe/Observable sang suspend/Flow bằng official/interoperability adapter phù hợp, rồi giữ một side làm owner.

Tránh chain kiểu Rx → LiveData → Flow → StateFlow chỉ để nối framework; mỗi bridge thêm semantics và debug complexity.

## 9. XML Fragment → Compose từng screen

Có hai hướng bridge phổ biến.

Fragment/View app có thể host Compose qua `ComposeView`:

```kotlin
class ProfileFragment : Fragment(R.layout.fragment_profile_host) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        view.findViewById<ComposeView>(R.id.composeView).setContent {
            ProfileRoute(...)
        }
    }
}
```

Compose app có thể host legacy View bằng `AndroidView`:

```kotlin
AndroidView(
    factory = { context -> LegacyChartView(context) },
    update = { chart -> chart.submit(data) }
)
```

Interoperability là migration tool, không nên trở thành permanent nesting 5 tầng nếu không có lý do.

## 10. Fragment lifecycle vs Compose lifecycle

Khi Compose nằm trong Fragment, composition disposal strategy phải phù hợp View lifecycle. Nếu composition sống lâu hơn Fragment View, có thể giữ reference/leak.

Đừng assume “Compose tự xử lý lifecycle”. Host boundary vẫn cần đúng owner.

## 11. View Binding thay Kotlin synthetic

Kotlin Android Extensions synthetic view access từng phổ biến nhưng đã bị loại. Legacy project nên migrate sang View Binding hoặc Compose.

View Binding reference trong Fragment phải clear ở `onDestroyView` nếu binding giữ View tree:

```kotlin
private var _binding: FragmentProfileBinding? = null
private val binding get() = _binding!!

override fun onDestroyView() {
    super.onDestroyView()
    _binding = null
}
```

Đây là lifecycle issue, không chỉ syntax replacement.

## 12. `startActivityForResult` → Activity Result API

Legacy requestCode/onActivityResult dễ collision và phân tán handling. Activity Result API register contract theo lifecycle.

Migration nên centralize result semantics ở screen boundary và test process recreation/permission cases.

## 13. SharedPreferences → DataStore

Đừng migrate bằng cách đổi từng `getString` sang DataStore call ở UI. Tạo SettingsRepository trước:

```kotlin
interface SettingsRepository {
    val theme: Flow<ThemeMode>
    suspend fun setTheme(mode: ThemeMode)
}
```

UI chỉ biết repository contract. Backend implementation có thể dùng SharedPreferences trước rồi đổi DataStore sau.

Data migration từ SharedPreferences sang DataStore phải idempotent và preserve key semantics.

## 14. SQLiteOpenHelper → Room

Nếu legacy database quan trọng, migration cần schema inventory và compatibility test. Không `fallbackToDestructiveMigration` chỉ để app mở được.

Có thể đưa Room quản lý database hiện có nếu schema mapping phù hợp hoặc viết migration copy dữ liệu. Test bằng database snapshot từ production schema cũ.

## 15. AsyncTask/Thread/Handler → coroutine hoặc WorkManager

Không đổi mọi background work thành `viewModelScope.launch`.

- work gắn screen: lifecycle coroutine;
- operation app-level ngắn: application scope có owner rõ;
- durable deferred work qua process death: WorkManager;
- user-visible ongoing work: foreground service/work theo platform policy;
- exact alarm chỉ khi semantics thật sự exact.

Migration phải chọn lifetime đúng, không chỉ chọn API mới.

## 16. Service locator → DI

Legacy singleton:

```kotlin
object ServiceLocator {
    val api = Retrofit.Builder()...
    val repository = UserRepositoryImpl(api)
}
```

Có thể migrate bằng constructor injection từng class. Hilt/Koin/Dagger chỉ automate graph sau khi dependency boundary sạch.

Một chiến lược là giữ ServiceLocator ở composition root, nhưng internal feature nhận dependency qua constructor. Sau đó thay root bằng DI framework mà feature code ít đổi.

## 17. God Activity/God Fragment

Một Activity 5.000 dòng thường chứa navigation, API, permissions, dialog, analytics, state, adapter, business logic.

Không nên tách thành 20 helper class ngẫu nhiên. Tách theo ownership:

```text
UI rendering/event
screen state holder
business operation
repository/data source
navigation coordinator
platform integration
```

Mỗi extraction nên có test hoặc behavior proof.

## 18. Global event bus

EventBus/Rx subject singleton thường tạo hidden dependency. Migration nên tìm event semantics.

- durable data change → repository/source of truth;
- UI state → ViewModel;
- cross-feature navigation → explicit navigator/coordinator contract;
- analytics → analytics interface;
- app-level session → SessionRepository observable state.

Đừng replace EventBus bằng một global SharedFlow rồi giữ nguyên vấn đề.

## 19. Multi-module migration

Không chia module theo mọi package trong ngày đầu. Trước tiên đo dependency graph và build bottleneck.

Một thứ tự thực tế:

```text
extract stable core:model/common contracts
→ isolate database/network implementation
→ extract one feature vertical slice
→ define feature API/impl boundary nếu cần
→ measure build/test ownership benefit
→ repeat
```

Nếu module hóa không giảm coupling/build/ownership problem, nó chỉ chuyển complexity sang Gradle.

## 20. Feature API và implementation

Feature lớn có thể expose contract nhỏ:

```kotlin
interface ProfileEntryPoint {
    fun route(userId: String): ProfileRoute
}
```

Các module khác không import internal ViewModel/Repository của Profile. Điều này giảm accidental coupling và giúp feature refactor độc lập.

## 21. Dependency cycle

Module graph cycle là dấu hiệu boundary sai. Đừng giải bằng module `common` chứa mọi thứ.

Nếu A và B cần type chung, extract abstraction/model thật sự shared. Nếu A gọi B và B callback A vì workflow, có thể cần coordinator ở layer trên.

## 22. Design system extraction

Compose migration thường tạo component duplicate. Khi pattern ổn định, extract design system: typography, color/token, spacing, reusable component.

Không abstract component quá sớm. Nếu hai button “trông giống” nhưng semantics/behavior khác, ép chung API khổng lồ có thể tệ hơn duplicate nhỏ.

## 23. Navigation migration

XML Navigation Component + Fragment có thể coexist với Compose. Bạn có thể migrate screen content trước, navigation graph sau.

Nếu đổi navigation và UI cùng PR cho feature critical, rollback/debug khó hơn. Separate migration axis giảm risk.

## 24. Backend compatibility trong migration

Client migration không được assume backend dừng hỗ trợ version cũ. Mobile rollout chậm; nhiều version coexist.

Nếu new app đổi request schema, backend cần compatibility window. Nếu database/local pending payload đổi, new version phải đọc pending operation cũ.

## 25. Branch-by-abstraction

Khi replace implementation lớn, tạo abstraction rồi cho old/new implementation coexist dưới flag.

```kotlin
interface SearchEngine {
    suspend fun search(query: String): List<Result>
}
```

OldSearchEngine và NewSearchEngine có thể A/B/internal switch. Khi new ổn định, xóa old implementation và flag.

Điều này an toàn hơn branch kéo dài vài tháng với big-bang merge.

## 26. Strangler pattern cho feature

Một feature legacy có thể được migrate vertical slice:

```text
new entry route
→ new ViewModel/UDF
→ repository boundary dùng data legacy adapter
→ new Compose UI
```

Sau đó data layer được migrate riêng. Hoặc ngược lại: modernize repository trước nhưng UI legacy vẫn dùng adapter.

Chọn direction theo nơi risk/cost cao nhất.

## 27. Test trước khi refactor behavior

Legacy code thường thiếu test. Trước extraction, thêm characterization test: test current behavior kể cả behavior hơi kỳ.

Sau đó refactor structure mà test vẫn pass. Khi muốn sửa business behavior, làm change riêng với requirement rõ.

Refactor và behavior change cùng lúc làm khó biết regression đến từ đâu.

## 28. Observability trong migration

Đặt metric so sánh old/new:

- crash/ANR;
- screen load latency;
- API failure;
- conversion/business event;
- sync failure;
- memory/jank.

“Code mới đẹp hơn” không đủ nếu production metric xấu hơn.

## 29. Feature flag rollout

New Compose screen có thể rollout 5% internal/beta/production cohort. Nếu metric ổn, tăng dần. Nếu lỗi, disable flag mà không cần emergency binary release tùy architecture.

Flag cần cleanup sau migration.

## 30. Definition of done của migration

Migration chưa xong khi code mới được thêm. Nó xong khi:

- traffic/user flow đã sang implementation mới;
- metric ổn;
- fallback không cần nữa;
- old code/dependency/adapter được xóa;
- test/document cập nhật;
- flag được remove;
- ownership mới rõ.

Nếu old/new sống mãi song song, maintenance cost tăng gấp đôi.

## 31. Anti-pattern: rewrite toàn bộ

Rewrite hấp dẫn vì code mới sạch trên whiteboard. Nhưng business rule ẩn trong legacy code thường chỉ lộ khi production edge case xảy ra.

Incremental migration giữ feedback loop và cho phép ship value trong khi modernize. Big-bang chỉ hợp lý khi system nhỏ, behavior hiểu đầy đủ và rewrite cost/risk thực sự thấp.

## 32. Anti-pattern: architecture astronaut

Một legacy app đơn module không tự động cần 50 Gradle modules, 200 use case và custom MVI framework. Mục tiêu là giảm complexity tổng, không đổi loại complexity.

Đo compile time, ownership conflict, test isolation và dependency graph trước/sau.

## 33. Migration roadmap mẫu

```text
Phase 0: inventory + metrics + critical characterization tests
Phase 1: repository/session/error contracts
Phase 2: coroutine/Flow boundary around legacy async APIs
Phase 3: migrate one non-critical vertical feature to Compose
Phase 4: standardize design system/navigation conventions
Phase 5: Room/DataStore/background modernization
Phase 6: extract modules where measurable value exists
Phase 7: migrate critical feature with staged rollout
Phase 8: delete adapters/old dependencies/flags
```

Roadmap phải thay đổi theo project; đây là reasoning template, không phải mandatory order.

## 34. Senior notes

Legacy migration là risk management. Người senior không chỉ biết API mới; họ biết **cách thay hệ thống đang chạy mà không làm mất business behavior**.

Mỗi migration step nên nhỏ đủ để review, test, rollout và rollback. Tạo seam trước, bridge lifetime/cancellation đúng, đo production metric, và xóa bridge khi hoàn tất. Interop là công cụ tạm thời; boundary rõ ràng mới là tài sản lâu dài.
