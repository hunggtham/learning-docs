# Case 20 — Android Library và SDK Authoring: AAR, Public API, Binary Compatibility và Publishing

Viết code bên trong một app và viết một Android library/SDK cho app khác sử dụng là hai bài toán khác nhau. Trong app, team có thể refactor đồng thời mọi call site. Trong library, public class, resource, manifest component, ProGuard rule, initialization behavior và transitive dependency đều trở thành contract với consumer mà bạn không kiểm soát.

Chapter này xây mental model để thiết kế reusable Android library/SDK ổn định, nhỏ, test được và không ép consumer hiểu implementation detail.

## 1. Android Library khác pure Kotlin/JVM library

Pure Kotlin/JVM library chủ yếu publish bytecode/JAR và metadata. Android library có thể cần Android resources, manifest, native library, consumer ProGuard rules, lint checks và Android-specific APIs, nên thường được build thành **AAR — Android Archive**.

AAR có thể chứa:

```text
classes.jar
AndroidManifest.xml
res/
assets/
jni/
consumer-rules
R.txt/public resources metadata
```

Không phải AAR nào cũng có mọi thành phần.

Nếu library không cần Android framework/resource, pure Kotlin/JVM module thường đơn giản và reusable hơn.

## 2. Public API surface là sản phẩm

Mọi `public` declaration có thể trở thành compatibility obligation. Đừng để implementation class public chỉ vì default visibility tiện.

Kotlin default là `public`, nên library author phải chủ động dùng `internal`/`private`.

```kotlin
public interface PaymentClient {
    suspend fun pay(request: PaymentRequest): PaymentResult
}

internal class DefaultPaymentClient(...) : PaymentClient { ... }
```

Public API nhỏ giúp evolve implementation mà không phá consumer.

## 3. Source compatibility và binary compatibility

**Source compatibility**: consumer source cũ recompile với library mới vẫn compile.

**Binary compatibility**: app/library consumer đã compile trước đó vẫn link/run với binary mới mà không cần recompile.

Một change có thể source-compatible nhưng binary-incompatible hoặc ngược lại.

Ví dụ đổi method signature/default parameter/inline implementation/interface shape có thể có ABI implication khác trực giác source code.

Library production cần API/ABI validation, không chỉ compile sample app.

## 4. Kotlin default parameters và Java consumer

Kotlin:

```kotlin
fun connect(timeoutMs: Long = 5_000)
```

Kotlin caller dùng default parameter tự nhiên. Java caller không thấy overload giống Kotlin trừ khi dùng `@JvmOverloads` hoặc explicit overload.

Library cho mixed Java/Kotlin ecosystem phải review Java ergonomics:

```kotlin
@JvmOverloads
fun connect(timeoutMs: Long = 5_000, retry: Int = 1)
```

Không thêm `@JvmOverloads` máy móc; nó tăng public methods/ABI surface.

## 5. `@JvmStatic`, `@JvmField`, `@JvmName` là interoperability tools

Companion/object API có thể awkward từ Java. Annotation JVM giúp shape bytecode/API:

```kotlin
class Sdk private constructor() {
    companion object {
        @JvmStatic
        fun initialize(context: Context) { ... }
    }
}
```

`@JvmName` giúp tránh signature clash hoặc cung cấp Java-friendly name. Mọi annotation này nên được xem là ABI decision.

## 6. Avoid exposing implementation dependency types

Nếu public API trả Retrofit `Response`, OkHttp type, Room entity hay coroutine internal type không cần thiết, consumer bị coupled vào dependency/version của SDK.

Bad:

```kotlin
fun fetch(): retrofit2.Response<UserDto>
```

Better:

```kotlin
suspend fun fetchUser(): UserResult
```

Expose standard/library-owned domain types. Điều này giảm transitive dependency conflict và cho phép đổi implementation.

## 7. `api` vs `implementation` trong library

Nếu public API expose type từ dependency, Gradle có thể cần `api`. Nếu dependency chỉ implementation detail, dùng `implementation`.

Overuse `api` làm dependency graph consumer phình và tăng ABI coupling.

Goal không phải “không có transitive dependency”, mà là public contract deliberate.

## 8. AAR resource là global-ish namespace concern

Resource name trong dependencies được merge vào app resource graph. Library nên prefix resource để giảm collision:

```text
sdk_payment_button
sdk_payment_error_title
sdk_payment_theme_overlay
```

Không đặt generic `button_primary` trong public library.

Nếu resource không intended for consumer override/use, giảm public exposure theo capability build tools/version hỗ trợ.

## 9. Theme/style contract

Custom View/Compose component library cần document theme expectation. Không assume consumer dùng cùng Material theme/version.

Nếu SDK render UI, cân nhắc:

- theme overlay;
- colors/typography configurable;
- dark mode;
- dynamic color behavior;
- accessibility/font scale;
- localization;
- edge-to-edge/insets.

UI SDK là public visual contract, không chỉ code API.

## 10. Compose library compatibility

Compose library public API có thêm concern compiler/runtime/library version. Avoid exposing unstable/experimental API không có policy rõ.

Public composable nên follow state hoisting:

```kotlin
@Composable
fun PaymentButton(
    state: PaymentButtonState,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
)
```

`Modifier` thường để cuối/default giúp composition idiom. Không hardcode navigation/ViewModel/global singleton bên trong reusable UI component.

## 11. Manifest của library được merge vào consumer app

Library có thể khai báo provider/service/receiver/permission. Đây là powerful side effect.

SDK author phải:

- minimal manifest footprint;
- `android:exported` explicit/correct;
- unique authorities bằng `${applicationId}` placeholder khi phù hợp;
- avoid broad permission nếu feature optional;
- document component behavior.

Consumer phải có khả năng override/remove component khi architecture cho phép.

## 12. Auto-initialization là convenience có startup cost

SDK thường dùng ContentProvider/AndroidX Startup để auto-init. Điều này giảm setup nhưng thêm work vào cold start của mọi app consumer.

Chỉ auto-init phần thật sự cần và rất nhẹ. Heavy SDK nên explicit initialize hoặc lazy feature init.

Cung cấp opt-out nếu auto-init có meaningful cost.

## 13. `Context` ownership trong SDK

Long-lived SDK object không giữ Activity context nếu không cần. Dùng application context cho process-lifetime service.

Nếu API cần Activity để launch UI/permission, chỉ giữ reference trong operation scope hoặc weak/lifecycle-aware contract.

Memory leak trong SDK ảnh hưởng mọi app consumer và khó debug vì stack crossing library boundary.

## 14. Threading contract phải được document

API callback có chạy main thread không? Method có thread-safe không? Có thể call concurrent không?

Kotlin coroutine API thường rõ hơn callback, nhưng vẫn cần main-safety contract.

```kotlin
interface AnalyticsSdk {
    /** Main-safe; may be called from any thread. */
    fun track(event: Event)
}
```

Nếu consumer phải tự biết “method này không được main thread” mà docs không nói, SDK contract chưa đủ.

## 15. Coroutine API và scope ownership

Library `suspend` function nên caller-owned: work bị cancel khi caller scope cancel, trừ khi operation semantics thật sự durable.

Không launch `GlobalScope` để thoát cancellation.

Nếu SDK cần process-long work, expose explicit lifecycle or use appropriate durable Android primitive; document behavior.

## 16. Flow public API

`Flow<T>` hợp lý cho stream. Cần document hot/cold behavior và replay semantics.

Expose mutable stream ra ngoài là nguy hiểm:

```kotlin
private val _state = MutableStateFlow(...)
val state: StateFlow<State> = _state.asStateFlow()
```

Consumer quan sát, SDK sở hữu mutation.

## 17. Error model public API

Không để mọi failure thành raw `Exception` implementation-specific.

Library có thể dùng sealed result/error:

```kotlin
sealed interface PaymentError {
    data object NetworkUnavailable : PaymentError
    data object Cancelled : PaymentError
    data class Declined(val code: String?) : PaymentError
    data class Internal(val cause: Throwable?) : PaymentError
}
```

Nhưng public error taxonomy phải stable. Đừng expose internal server code như permanent enum nếu backend có thể thêm value.

## 18. Cancellation không phải error bình thường

Coroutine library không nên catch `Throwable` rồi biến `CancellationException` thành SDK error. Propagate cancellation đúng structured concurrency.

```kotlin
catch (e: CancellationException) {
    throw e
}
```

Nếu API có explicit user cancellation result khác coroutine cancellation, document distinction.

## 19. Consumer ProGuard/R8 rules

Library dùng reflection/JNI/serialization có thể cần keep rules khi consumer app minify.

Đưa rule bắt buộc vào `consumerProguardFiles`, không yêu cầu mọi consumer copy docs thủ công.

```kotlin
android {
    defaultConfig {
        consumerProguardFiles("consumer-rules.pro")
    }
}
```

Rule phải minimal. `-keep class com.sdk.** { *; }` có thể vô hiệu hóa optimization lớn của consumer.

## 20. Test minified consumer app

Library debug unit tests không phát hiện R8 issue. Tạo sample/fixture app build `release` minified để test SDK packaged như consumer thật.

CI nên ít nhất build/install smoke test minified artifact cho library có reflection/JNI.

## 21. Native library trong AAR

Nếu AAR chứa `.so`, SDK author chịu thêm ABI/page-size/symbol concern của Case 17.

Consumer không nên bất ngờ với 30 MB native binaries. Document size và ABI support.

Native symbols/debug package cần release management tương ứng nếu SDK support crash analysis.

## 22. Lint checks như executable documentation

Nếu SDK có usage rule mà compiler không encode được, custom Android Lint có thể bắt sai usage ở consumer build.

Ví dụ:

- API cần manifest declaration;
- method không được gọi trong main thread;
- annotation pair phải dùng cùng nhau;
- deprecated migration path.

Lint tốt giúp chuyển docs thành early feedback. Nhưng custom lint cũng là artifact/versioned API phải test với toolchain consumer.

## 23. Annotations và opt-in

`@RequiresApi`, `@IntDef` legacy Java interop, Kotlin `@RequiresOptIn`, nullability annotations và threading annotations có thể tăng contract clarity.

Experimental API nên rõ:

```kotlin
@RequiresOptIn
annotation class ExperimentalSdkApi
```

Không gọi API “experimental” nhưng vẫn hứa binary compatibility như stable API.

## 24. SemVer chỉ hữu ích khi compatibility policy rõ

Semantic Versioning thường hiểu:

- major: breaking change;
- minor: backward-compatible feature;
- patch: backward-compatible fix.

Nhưng “breaking” phải định nghĩa source, binary, behavior, resource và data compatibility.

Android SDK có thể giữ binary API nhưng đổi manifest behavior làm app consumer break. Đó vẫn là breaking change về product contract.

## 25. Behavioral compatibility

Method signature không đổi nhưng semantics đổi từ “retry 1 lần” sang “retry vô hạn” có thể phá app.

SDK release notes phải ghi behavior changes, thread changes, permission changes, startup changes và dependency changes—không chỉ API diff.

## 26. Binary compatibility validation

Kotlin/Java ecosystem có tools để dump/check public ABI. Team nên integrate API dump/check vào CI cho published libraries.

Workflow:

```text
change library
→ generate API/ABI dump
→ diff against baseline
→ deliberate approve breaking/additive change
```

Không review public ABI bằng mắt trong 500-file PR.

## 27. Inline function compatibility

Public `inline` function đưa implementation vào caller bytecode khi compile. Thay implementation/library version có semantics khác non-inline method.

Public inline API cần đặc biệt cẩn thận với references tới internal implementation; Kotlin có `@PublishedApi` cho specific use case nhưng nó cũng mở compatibility commitment.

Đừng inline public API chỉ vì micro performance nếu không cần.

## 28. Data class trong public API

Public `data class` tiện nhưng auto-generated `copy/componentN` và constructor shape trở thành API. Thêm property vào primary constructor có thể source/binary implications.

Đối với long-lived SDK model cần evolve, builder/interface/regular class hoặc optional extension fields có thể linh hoạt hơn tùy use case.

## 29. Enum evolution

Consumer `when` exhaustive trên enum có thể break assumptions khi library thêm enum constant. Network/server-open domain càng không nên expose closed enum nếu future values có thể xuất hiện.

Sealed hierarchy cũng là closed-world contract. Chọn closed/open model có chủ ý.

## 30. Parcelable/Serializable public model

Nếu SDK model đi qua Bundle/Intent/process recreation, serialized shape trở thành compatibility concern.

Không dùng Java Serializable mặc định cho durable storage/versioned protocol. Parcelable phù hợp Android IPC/state ngắn hạn nhưng không phải stable persistence format.

Durable data cần explicit schema/versioning.

## 31. Resource ID không phải stable external protocol

Không persist raw `R.id`/resource integer qua app versions/server. IDs có thể thay khi rebuild/resource graph thay đổi.

Public SDK API nên dùng semantic identifiers/string/domain type.

## 32. Dependency conflict và BOM

SDK kéo nhiều libraries có thể conflict consumer versions. Giảm dependency footprint và tránh pin constraints quá chặt nếu không cần.

Nếu publish family nhiều artifacts, BOM/platform có thể giúp align versions. Nhưng BOM không giải runtime incompatibility nếu modules thật sự không compatible.

## 33. Shading/relocation

Một số JVM libraries shade dependency để tránh conflict, nhưng Android/R8/resource/native environment làm technique phức tạp. Chỉ dùng khi hiểu license/size/reflection consequences.

Tốt hơn thường là giảm dependency hoặc expose compatibility range hợp lý.

## 34. Publishing repository

Library có thể publish Maven artifact gồm group/artifact/version, POM/module metadata và AAR/JAR.

Internal SDK có thể dùng private Maven repository. Public SDK có thể publish central repository phù hợp.

Publishing pipeline phải immutable: không overwrite binary của cùng version. Nếu `1.2.3` hôm nay khác `1.2.3` ngày mai, reproducibility consumer vỡ.

## 35. Sources và documentation artifacts

Publish source/Javadoc/Dokka artifacts giúp debugging/IDE navigation. Public API docs phải đi cùng release version.

Docs website “latest” không đủ khi consumer đang pin old version. Giữ versioned migration/release notes.

## 36. Sample app là integration test và documentation

Một sample app tốt chứng minh:

- install SDK;
- manifest/config setup;
- common flow;
- error/cancel;
- process recreation;
- release minification;
- Java consumer nếu support.

Sample phải build trong CI để tránh docs drift.

## 37. Test matrix cho SDK

SDK test không chỉ unit test internal code. Cần:

1. pure unit tests;
2. Android instrumentation nếu framework interaction;
3. minSdk + latest representative;
4. Java/Kotlin consumer compile;
5. minified release consumer;
6. process/lifecycle tests nếu SDK UI/system component;
7. network failure/cancellation;
8. upgrade from previous SDK version in sample app khi state durable;
9. ABI/native matrix nếu `.so`;
10. compile against supported AGP/Kotlin range nếu officially promised.

## 38. Backward compatibility window của SDK

Không nên hứa support “mọi Kotlin/AGP version”. Define tested support range.

Kotlin metadata/compiler plugin changes có thể ảnh hưởng consumer compile. Android library resource/manifest behavior cũng phụ thuộc AGP.

Release notes phải nêu minimum compileSdk/minSdk/JDK/AGP nếu thay đổi.

## 39. SDK initialization API design

Nếu cần explicit init:

```kotlin
Sdk.initialize(
    context = applicationContext,
    config = SdkConfig(...)
)
```

Define:

- gọi nhiều lần idempotent không;
- thread nào được gọi;
- init async hay sync;
- lỗi config trả thế nào;
- process nào init;
- init trước use API nếu quên thì behavior gì.

Không để `lateinit global` crash ngẫu nhiên mà không contract.

## 40. Multi-process SDK

Nếu SDK có provider/service process riêng, state không shared như singleton memory. DataStore/Room/shared file access cần multi-process correctness riêng.

Tránh multi-process nếu không required. SDK consumer thường không muốn thêm process chỉ để library tiện.

## 41. Privacy và data collection contract

SDK analytics/ads/auth có thể thu data thay app. Consumer cần biết để khai Data Safety/privacy policy.

SDK nên document:

- data fields collected;
- purpose;
- retention/upload;
- opt-out/config;
- permissions;
- network domains;
- identifiers.

Privacy side effect là public contract ngang API signature.

## 42. Security surface của SDK

Review exported components, WebView bridge, PendingIntent mutability, file URI/provider, certificate/TLS, token storage và native parser.

Consumer app inherit attack surface library. Vì vậy security patch cadence và vulnerability disclosure process quan trọng với SDK public.

## 43. Deprecation và migration

Không xóa public API ngay. Deprecate với replacement/migration message:

```kotlin
@Deprecated(
    message = "Use authenticate(request) instead",
    replaceWith = ReplaceWith("authenticate(request)")
)
fun login(...)
```

Nếu replacement không mechanical, link migration guide.

Deprecation window tùy policy; quan trọng là consumer có thời gian và clear path.

## 44. Feature flag trong SDK

Remote flag nội bộ SDK có thể thay behavior consumer ngoài version upgrade, gây khó reproduce. Nếu dùng, flag cần observability/versioning và không được silently break contract.

Critical behavior nên consumer-configurable hoặc release-versioned thay vì hidden server switch không document.

## 45. Senior review checklist cho library release

Trước publish:

- public API diff đã review chưa;
- binary compatibility check pass;
- minSdk/compile/toolchain requirement đổi không;
- transitive dependencies đổi gì;
- manifest/resource/permission footprint đổi không;
- consumer R8 rules tested chưa;
- release minified sample chạy chưa;
- Java interoperability ổn chưa;
- privacy/security behavior đổi không;
- migration/release note đủ chưa;
- artifact immutable/provenance trace được không.

## 46. Official references

- Android library modules: https://developer.android.com/studio/projects/android-library
- Publish your library: https://developer.android.com/build/publish-library
- Build variants: https://developer.android.com/build/build-variants
- R8: https://developer.android.com/topic/performance/app-optimization
- Android Lint: https://developer.android.com/studio/write/lint

Library authoring là compatibility engineering dài hạn. API đẹp ở version 1.0 nhưng không có evolution strategy sẽ trở thành technical debt cho cả SDK team và mọi consumer.