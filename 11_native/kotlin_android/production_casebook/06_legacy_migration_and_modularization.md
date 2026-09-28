# Trường hợp (case / 사례) 06 — Legacy Android di chuyển (migration / 마이그레이션) và Modularization

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 06 — Legacy Android di chuyển (migration / 마이그레이션) và Modularization** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Đầu tiên phải inventory, không mã (code / 코드) ngay** sang **2. Phân biệt legacy, deprecated và simply-not-fashionable**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Nhiều Android nhà phát triển (developer / 개발자) không bắt đầu từ một greenfield Compose dự án (project / 프로젝트). Họ bước vào codebase có XML, Fragment, custom View, callback, RxJava, LiveData, AsyncTask-era utility, singleton dịch vụ (service / 서비스) locator, Java lớp (class / 클래스), `startActivityForResult`, dùng chung (shared / 공유) mutable trạng thái (state / 상태) và Gradle script tích lũy qua nhiều năm. Nếu approach là “rewrite toàn bộ sang Compose/Clean kiến trúc (architecture / 아키텍처)”, rủi ro (risk / 위험) thường tăng mạnh: nghiệp vụ (business / 비즈니스) regression, bản phát hành (release / 릴리스) freeze, merge xung đột (conflict / 충돌), mất kiến thức (knowledge / 지식) và kéo dài di chuyển (migration / 마이그레이션) vô hạn.

Chương này trình bày cách migrate theo **strangler mẫu (pattern / 패턴)**: tạo ranh giới (boundary / 경계) mới, chuyển từng vertical slice, giữ interoperability rõ ràng và xóa legacy khi replacement đã chứng minh môi trường vận hành (production / 운영 환경).

## 1. Đầu tiên phải inventory, không mã (code / 코드) ngay

Trước di chuyển (migration / 마이그레이션), lập bản đồ:

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

Đồng thời tìm rủi ro (risk / 위험) hotspot: payment/auth, thiết bị (device / 장치) tích hợp (integration / 통합), deep link, tệp (file / 파일) upload, WebView, cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션), push notification.

Một màn hình 2.000 dòng nhưng ít người dùng (user / 사용자) có thể rủi ro (risk / 위험) thấp hơn một utility 50 dòng dùng ở mọi payment luồng (flow / 흐름).

## 2. Phân biệt legacy, deprecated và simply-not-fashionable

XML/View không phải “sai”. Fragment cũng không mặc định cần xóa. Một API cũ nhưng stable có thể tiếp tục hợp lý trong mô-đun (module / 모듈) maintenance.

Chỉ migrate khi có mục tiêu: giảm bug/vòng đời (lifecycle / 생명주기) độ phức tạp (complexity / 복잡도), unify ngăn xếp (stack / 스택), improve testability, remove unsupported phụ thuộc (dependency / 의존성), speed tính năng (feature / 기능) delivery hoặc satisfy nền tảng (platform / 플랫폼) yêu cầu (requirement / 요구사항).

Di chuyển (migration / 마이그레이션) không có nghiệp vụ (business / 비즈니스)/kỹ thuật (engineering / 엔지니어링) kết quả (outcome / 결과) rõ ràng dễ biến thành rewrite vì sở thích.

## 3. Establish seam trước khi replace hiện thực (implementation / 구현)

Nếu Fragment gọi trực tiếp Retrofit, SQLite helper và analytics, trước tiên tạo repository/use-case ranh giới (boundary / 경계) mà UI cũ vẫn dùng được.

```kotlin
interface UserRepository {
    fun observeUser(id: String): Flow<User>
    suspend fun updateProfile(command: UpdateProfileCommand)
}
```

Sau khi seam ổn định, hiện thực (implementation / 구현) có thể migrate mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스) mà UI không cần đổi cùng lúc.

Đây là nguyên tắc quan trọng: **decouple first, modernize second**.

## 4. Java ↔ Kotlin di chuyển (migration / 마이그레이션)

Kotlin interoperates Java tốt nhưng có trường hợp biên (edge case / 경계 사례).

Java nền tảng (platform / 플랫폼) kiểu (type / 타입) không biết nullability chính xác. Annotate Java API (`@Nullable`, `@NonNull`) nếu có thể để Kotlin trình biên dịch (compiler / 컴파일러) giúp bạn.

Java bean getter/setter có thể xuất hiện như Kotlin thuộc tính (property / 속성). SAM giao diện (interface / 인터페이스) có lambda interop. Checked exception không được Kotlin enforce. Wildcard/generic variance có thể cần `@JvmSuppressWildcards` hoặc API thiết kế (design / 설계) cẩn thận.

Không convert 500 tệp (file / 파일) Java bằng công cụ (tool / 도구) rồi gọi là di chuyển (migration / 마이그레이션) hoàn tất. Chọn ranh giới (boundary / 경계), chạy kiểm thử (test / 테스트) và refactor idiomatic Kotlin dần.

## 5. Callback → suspend

Legacy API:

```kotlin
interface Callback<T> {
    fun onSuccess(value: T)
    fun onError(error: Throwable)
}
```

Có thể cầu nối (bridge / 브리지) one-shot callback bằng `suspendCancellableCoroutine`:

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

Cancellation cầu nối (bridge / 브리지) rất quan trọng. Nếu coroutine cancel mà underlying yêu cầu (request / 요청) vẫn chạy và giữ callback/UI tham chiếu (reference / 참조), di chuyển (migration / 마이그레이션) chỉ đổi cú pháp (syntax / 문법) chứ chưa sửa vòng đời (lifecycle / 생명주기).

## 6. Listener/stream → callbackFlow

Listener nhiều sự kiện (event / 이벤트) phù hợp với `callbackFlow`:

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

Luôn có cleanup. `callbackFlow` không tự biết cách unregister listener của thư viện (library / 라이브러리).

## 7. LiveData → luồng (flow / 흐름) không cần big-bang

ViewModel cũ có thể expose LiveData cho XML Fragment. dữ liệu (data / 데이터) tầng (layer / 계층) mới có thể dùng luồng (flow / 흐름) rồi adapt ở ranh giới (boundary / 경계).

```kotlin
val usersLiveData = repository.observeUsers().asLiveData()
```

Ngược lại có thể cầu nối (bridge / 브리지) LiveData thành luồng (flow / 흐름) nếu cần. Mục tiêu là move nguồn chuẩn (source of truth / 정본) dần, không force toàn bộ app đổi cùng PR.

Khi Compose screen thay Fragment, có thể dùng StateFlow trực tiếp với lifecycle-aware collection.

## 8. RxJava → Coroutine/luồng (flow / 흐름)

Nếu codebase RxJava lớn, đừng replace operator-by-operator một cách máy móc. Rx có ngữ nghĩa (semantics / 의미론) scheduler/backpressure/disposal riêng.

Chọn mô-đun (module / 모듈)/tính năng (feature / 기능) ranh giới (boundary / 경계). cầu nối (bridge / 브리지) Single/Maybe/Observable sang suspend/luồng (flow / 흐름) bằng official/interoperability adapter phù hợp, rồi giữ một side làm đơn vị sở hữu (owner / 오너).

Tránh chuỗi (chain / 사슬) kiểu Rx → LiveData → luồng (flow / 흐름) → StateFlow chỉ để nối khung phần mềm (framework / 프레임워크); mỗi cầu nối (bridge / 브리지) thêm ngữ nghĩa (semantics / 의미론) và gỡ lỗi (debug / 디버그) độ phức tạp (complexity / 복잡도).

## 9. XML Fragment → Compose từng screen

Có hai hướng cầu nối (bridge / 브리지) phổ biến.

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

Interoperability là di chuyển (migration / 마이그레이션) công cụ (tool / 도구), không nên trở thành permanent nesting 5 tầng nếu không có lý do.

## 10. Fragment vòng đời (lifecycle / 생명주기) vs Compose vòng đời (lifecycle / 생명주기)

Khi Compose nằm trong Fragment, composition disposal chiến lược (strategy / 전략) phải phù hợp View vòng đời (lifecycle / 생명주기). Nếu composition sống lâu hơn Fragment View, có thể giữ tham chiếu (reference / 참조)/leak.

Đừng assume “Compose tự xử lý vòng đời (lifecycle / 생명주기)”. Host ranh giới (boundary / 경계) vẫn cần đúng đơn vị sở hữu (owner / 오너).

## 11. View Binding thay Kotlin synthetic

Kotlin Android Extensions synthetic view truy cập (access / 접근) từng phổ biến nhưng đã bị loại. Legacy dự án (project / 프로젝트) nên migrate sang View Binding hoặc Compose.

View Binding tham chiếu (reference / 참조) trong Fragment phải clear ở `onDestroyView` nếu binding giữ View cây (tree / 트리):

```kotlin
private var _binding: FragmentProfileBinding? = null
private val binding get() = _binding!!

override fun onDestroyView() {
    super.onDestroyView()
    _binding = null
}
```

Đây là vòng đời (lifecycle / 생명주기) issue, không chỉ cú pháp (syntax / 문법) replacement.

## 12. `startActivityForResult` → Activity kết quả (result / 결과) API

Legacy requestCode/onActivityResult dễ collision và phân tán handling. Activity kết quả (result / 결과) API register đặc tả hợp đồng (contract / 계약) theo vòng đời (lifecycle / 생명주기).

Di chuyển (migration / 마이그레이션) nên centralize kết quả (result / 결과) ngữ nghĩa (semantics / 의미론) ở screen ranh giới (boundary / 경계) và kiểm thử (test / 테스트) tiến trình (process / 프로세스) recreation/permission cases.

## 13. SharedPreferences → DataStore

Đừng migrate bằng cách đổi từng `getString` sang DataStore lời gọi (call / 호출) ở UI. Tạo SettingsRepository trước:

```kotlin
interface SettingsRepository {
    val theme: Flow<ThemeMode>
    suspend fun setTheme(mode: ThemeMode)
}
```

UI chỉ biết repository đặc tả hợp đồng (contract / 계약). Backend hiện thực (implementation / 구현) có thể dùng SharedPreferences trước rồi đổi DataStore sau.

Dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) từ SharedPreferences sang DataStore phải idempotent và preserve key ngữ nghĩa (semantics / 의미론).

## 14. SQLiteOpenHelper → Room

Nếu legacy cơ sở dữ liệu (database / 데이터베이스) quan trọng, di chuyển (migration / 마이그레이션) cần lược đồ (schema / 스키마) inventory và tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트). Không `fallbackToDestructiveMigration` chỉ để app mở được.

Có thể đưa Room quản lý cơ sở dữ liệu (database / 데이터베이스) hiện có nếu lược đồ (schema / 스키마) ánh xạ (mapping / 매핑) phù hợp hoặc viết di chuyển (migration / 마이그레이션) bản sao (copy / 복사) dữ liệu. kiểm thử (test / 테스트) bằng cơ sở dữ liệu (database / 데이터베이스) snapshot từ môi trường vận hành (production / 운영 환경) lược đồ (schema / 스키마) cũ.

## 15. AsyncTask/luồng thực thi (thread / 스레드)/Handler → coroutine hoặc WorkManager

Không đổi mọi background công việc (work / 작업) thành `viewModelScope.launch`.

- công việc (work / 작업) gắn screen: vòng đời (lifecycle / 생명주기) coroutine;
- thao tác (operation / 연산) app-level ngắn: ứng dụng (application / 애플리케이션) phạm vi (scope / 범위) có đơn vị sở hữu (owner / 오너) rõ;
- durable deferred công việc (work / 작업) qua tiến trình (process / 프로세스) death: WorkManager;
- user-visible ongoing công việc (work / 작업): foreground dịch vụ (service / 서비스)/công việc (work / 작업) theo nền tảng (platform / 플랫폼) chính sách (policy / 정책);
- chính xác (exact / 정확한) alarm chỉ khi ngữ nghĩa (semantics / 의미론) thật sự chính xác (exact / 정확한).

Di chuyển (migration / 마이그레이션) phải chọn thời gian tồn tại (lifetime / 수명) đúng, không chỉ chọn API mới.

## 16. dịch vụ (service / 서비스) locator → DI

Legacy singleton:

```kotlin
object ServiceLocator {
    val api = Retrofit.Builder()...
    val repository = UserRepositoryImpl(api)
}
```

Có thể migrate bằng constructor injection từng lớp (class / 클래스). Hilt/Koin/Dagger chỉ automate đồ thị (graph / 그래프) sau khi phụ thuộc (dependency / 의존성) ranh giới (boundary / 경계) sạch.

Một chiến lược là giữ ServiceLocator ở composition gốc (root / 루트), nhưng nội bộ (internal / 내부) tính năng (feature / 기능) nhận phụ thuộc (dependency / 의존성) qua constructor. Sau đó thay gốc (root / 루트) bằng DI khung phần mềm (framework / 프레임워크) mà tính năng (feature / 기능) mã (code / 코드) ít đổi.

## 17. God Activity/God Fragment

Một Activity 5.000 dòng thường chứa điều hướng (navigation / 내비게이션), API, permissions, dialog, analytics, trạng thái (state / 상태), adapter, lô-gic nghiệp vụ (business logic / 비즈니스 로직).

Không nên tách thành 20 helper lớp (class / 클래스) ngẫu nhiên. Tách theo quyền sở hữu (ownership / 소유권):

```text
UI rendering/event
screen state holder
business operation
repository/data source
navigation coordinator
platform integration
```

Mỗi extraction nên có kiểm thử (test / 테스트) hoặc hành vi (behavior / 동작) proof.

## 18. toàn cục (global / 전역) sự kiện (event / 이벤트) bus

EventBus/Rx subject singleton thường tạo hidden phụ thuộc (dependency / 의존성). di chuyển (migration / 마이그레이션) nên tìm sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론).

- durable dữ liệu (data / 데이터) thay đổi (change / 변경) → repository/nguồn chuẩn (source of truth / 정본);
- UI trạng thái (state / 상태) → ViewModel;
- cross-feature điều hướng (navigation / 내비게이션) → tường minh (explicit / 명시적) navigator/coordinator đặc tả hợp đồng (contract / 계약);
- analytics → analytics giao diện (interface / 인터페이스);
- app-level session → SessionRepository observable trạng thái (state / 상태).

Đừng replace EventBus bằng một toàn cục (global / 전역) SharedFlow rồi giữ nguyên vấn đề.

## 19. Multi-module di chuyển (migration / 마이그레이션)

Không chia mô-đun (module / 모듈) theo mọi gói (package / 패키지) trong ngày đầu. Trước tiên đo phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và bản dựng (build / 빌드) bottleneck.

Một thứ tự thực tế:

```text
extract stable core:model/common contracts
→ isolate database/network implementation
→ extract one feature vertical slice
→ define feature API/impl boundary nếu cần
→ measure build/test ownership benefit
→ repeat
```

Nếu mô-đun (module / 모듈) hóa không giảm coupling/bản dựng (build / 빌드)/quyền sở hữu (ownership / 소유권) bài toán (problem / 문제), nó chỉ chuyển độ phức tạp (complexity / 복잡도) sang Gradle.

## 20. tính năng (feature / 기능) API và hiện thực (implementation / 구현)

Tính năng (feature / 기능) lớn có thể expose đặc tả hợp đồng (contract / 계약) nhỏ:

```kotlin
interface ProfileEntryPoint {
    fun route(userId: String): ProfileRoute
}
```

Các mô-đun (module / 모듈) khác không import nội bộ (internal / 내부) ViewModel/Repository của Profile. Điều này giảm accidental coupling và giúp tính năng (feature / 기능) refactor độc lập.

## 21. phụ thuộc (dependency / 의존성) cycle

Mô-đun (module / 모듈) đồ thị (graph / 그래프) cycle là dấu hiệu ranh giới (boundary / 경계) sai. Đừng giải bằng mô-đun (module / 모듈) `common` chứa mọi thứ.

Nếu A và B cần kiểu (type / 타입) chung, extract lớp trừu tượng (abstraction / 추상화)/mô hình (model / 모델) thật sự dùng chung (shared / 공유). Nếu A gọi B và B callback A vì workflow, có thể cần coordinator ở tầng (layer / 계층) trên.

## 22. thiết kế (design / 설계) hệ thống (system / 시스템) extraction

Compose di chuyển (migration / 마이그레이션) thường tạo thành phần (component / 컴포넌트) duplicate. Khi mẫu (pattern / 패턴) ổn định, extract thiết kế (design / 설계) hệ thống (system / 시스템): typography, color/đơn vị từ (token / 토큰), spacing, reusable thành phần (component / 컴포넌트).

Không abstract thành phần (component / 컴포넌트) quá sớm. Nếu hai button “trông giống” nhưng ngữ nghĩa (semantics / 의미론)/hành vi (behavior / 동작) khác, ép chung API khổng lồ có thể tệ hơn duplicate nhỏ.

## 23. điều hướng (navigation / 내비게이션) di chuyển (migration / 마이그레이션)

XML điều hướng (navigation / 내비게이션) thành phần (component / 컴포넌트) + Fragment có thể coexist với Compose. Bạn có thể migrate screen content trước, điều hướng (navigation / 내비게이션) đồ thị (graph / 그래프) sau.

Nếu đổi điều hướng (navigation / 내비게이션) và UI cùng PR cho tính năng (feature / 기능) trọng yếu (critical / 중요), quay lui (rollback / 롤백)/gỡ lỗi (debug / 디버그) khó hơn. Separate di chuyển (migration / 마이그레이션) axis giảm rủi ro (risk / 위험).

## 24. Backend tính tương thích (compatibility / 호환성) trong di chuyển (migration / 마이그레이션)

Máy khách (client / 클라이언트) di chuyển (migration / 마이그레이션) không được assume backend dừng hỗ trợ phiên bản (version / 버전) cũ. Mobile rollout chậm; nhiều phiên bản (version / 버전) coexist.

Nếu new app đổi yêu cầu (request / 요청) lược đồ (schema / 스키마), backend cần tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우). Nếu cơ sở dữ liệu (database / 데이터베이스)/cục bộ (local / 로컬) pending payload đổi, new phiên bản (version / 버전) phải đọc pending thao tác (operation / 연산) cũ.

## 25. Branch-by-abstraction

Khi replace hiện thực (implementation / 구현) lớn, tạo lớp trừu tượng (abstraction / 추상화) rồi cho old/new hiện thực (implementation / 구현) coexist dưới flag.

```kotlin
interface SearchEngine {
    suspend fun search(query: String): List<Result>
}
```

OldSearchEngine và NewSearchEngine có thể A/B/nội bộ (internal / 내부) switch. Khi new ổn định, xóa old hiện thực (implementation / 구현) và flag.

Điều này an toàn hơn branch kéo dài vài tháng với big-bang merge.

## 26. Strangler mẫu (pattern / 패턴) cho tính năng (feature / 기능)

Một tính năng (feature / 기능) legacy có thể được migrate vertical slice:

```text
new entry route
→ new ViewModel/UDF
→ repository boundary dùng data legacy adapter
→ new Compose UI
```

Sau đó dữ liệu (data / 데이터) tầng (layer / 계층) được migrate riêng. Hoặc ngược lại: modernize repository trước nhưng UI legacy vẫn dùng adapter.

Chọn direction theo nơi rủi ro (risk / 위험)/chi phí (cost / 비용) cao nhất.

## 27. kiểm thử (test / 테스트) trước khi refactor hành vi (behavior / 동작)

Legacy mã (code / 코드) thường thiếu kiểm thử (test / 테스트). Trước extraction, thêm characterization kiểm thử (test / 테스트): kiểm thử (test / 테스트) hiện tại (current / 현재) hành vi (behavior / 동작) kể cả hành vi (behavior / 동작) hơi kỳ.

Sau đó refactor cấu trúc (structure / 구조) mà kiểm thử (test / 테스트) vẫn pass. Khi muốn sửa nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작), làm thay đổi (change / 변경) riêng với yêu cầu (requirement / 요구사항) rõ.

Refactor và hành vi (behavior / 동작) thay đổi (change / 변경) cùng lúc làm khó biết regression đến từ đâu.

## 28. khả năng quan sát (observability / 관측 가능성) trong di chuyển (migration / 마이그레이션)

Đặt chỉ số (metric / 지표) so sánh old/new:

- crash/ANR;
- screen tải (load / 로드) độ trễ (latency / 지연 시간);
- API thất bại (failure / 실패);
- conversion/nghiệp vụ (business / 비즈니스) sự kiện (event / 이벤트);
- sync thất bại (failure / 실패);
- bộ nhớ (memory / 메모리)/jank.

“mã (code / 코드) mới đẹp hơn” không đủ nếu môi trường vận hành (production / 운영 환경) chỉ số (metric / 지표) xấu hơn.

## 29. cờ tính năng (feature flag / 기능 플래그) rollout

New Compose screen có thể rollout 5% nội bộ (internal / 내부)/beta/môi trường vận hành (production / 운영 환경) cohort. Nếu chỉ số (metric / 지표) ổn, tăng dần. Nếu lỗi, disable flag mà không cần emergency nhị phân (binary / 이진) bản phát hành (release / 릴리스) tùy kiến trúc (architecture / 아키텍처).

Flag cần cleanup sau di chuyển (migration / 마이그레이션).

## 30. Definition of done của di chuyển (migration / 마이그레이션)

Di chuyển (migration / 마이그레이션) chưa xong khi mã (code / 코드) mới được thêm. Nó xong khi:

- traffic/người dùng (user / 사용자) luồng (flow / 흐름) đã sang hiện thực (implementation / 구현) mới;
- chỉ số (metric / 지표) ổn;
- fallback không cần nữa;
- old mã (code / 코드)/phụ thuộc (dependency / 의존성)/adapter được xóa;
- kiểm thử (test / 테스트)/document cập nhật;
- flag được remove;
- quyền sở hữu (ownership / 소유권) mới rõ.

Nếu old/new sống mãi song song, maintenance chi phí (cost / 비용) tăng gấp đôi.

## 31. Anti-pattern: rewrite toàn bộ

Rewrite hấp dẫn vì mã (code / 코드) mới sạch trên whiteboard. Nhưng nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) ẩn trong legacy mã (code / 코드) thường chỉ lộ khi môi trường vận hành (production / 운영 환경) trường hợp biên (edge case / 경계 사례) xảy ra.

Incremental di chuyển (migration / 마이그레이션) giữ vòng phản hồi (feedback loop / 피드백 루프) và cho phép ship giá trị (value / 값) trong khi modernize. Big-bang chỉ hợp lý khi hệ thống (system / 시스템) nhỏ, hành vi (behavior / 동작) hiểu đầy đủ và rewrite chi phí (cost / 비용)/rủi ro (risk / 위험) thực sự thấp.

## 32. Anti-pattern: kiến trúc (architecture / 아키텍처) astronaut

Một legacy app đơn mô-đun (module / 모듈) không tự động cần 50 Gradle modules, 200 use trường hợp (case / 사례) và custom MVI khung phần mềm (framework / 프레임워크). Mục tiêu là giảm độ phức tạp (complexity / 복잡도) tổng, không đổi loại độ phức tạp (complexity / 복잡도).

Đo compile thời gian (time / 시간), quyền sở hữu (ownership / 소유권) xung đột (conflict / 충돌), kiểm thử (test / 테스트) isolation và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) trước/sau.

## 33. di chuyển (migration / 마이그레이션) roadmap mẫu

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

Roadmap phải thay đổi theo dự án (project / 프로젝트); đây là lập luận (reasoning / 추론) template, không phải mandatory thứ tự (order / 순서).

## 34. cấp cao (senior / 시니어) notes

Legacy di chuyển (migration / 마이그레이션) là rủi ro (risk / 위험) management. Người cấp cao (senior / 시니어) không chỉ biết API mới; họ biết **cách thay hệ thống đang chạy mà không làm mất nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작)**.

Mỗi di chuyển (migration / 마이그레이션) step nên nhỏ đủ để rà soát (review / 검토), kiểm thử (test / 테스트), rollout và quay lui (rollback / 롤백). Tạo seam trước, cầu nối (bridge / 브리지) thời gian tồn tại (lifetime / 수명)/cancellation đúng, đo môi trường vận hành (production / 운영 환경) chỉ số (metric / 지표), và xóa cầu nối (bridge / 브리지) khi hoàn tất. Interop là công cụ tạm thời; ranh giới (boundary / 경계) rõ ràng mới là tài sản lâu dài.

> **Bàn giao:** Sau **34. cấp cao (senior / 시니어) notes**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture end to end](./01_architecture_end_to_end.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
