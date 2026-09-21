# Depth Lab 07 — SDK Authoring, Native Boundary, API Evolution và Consumer Safety

Khi viết application code, team kiểm soát hầu hết call site. Khi viết Android library hoặc SDK, code của bạn chạy bên trong process của **người khác**, dưới build system, dependency graph, lifecycle, shrinker và release cadence của **người khác**. Vì vậy SDK authoring đòi hỏi discipline cao hơn: public API phải ổn định, dependency không được gây xung đột, initialization không được làm chậm app host, native code không được phá ABI, và failure không được kéo cả process consumer xuống theo.

Depth Lab này đào sâu cách thiết kế library/SDK như một long-lived contract.

---

## 1. Public API là contract, không chỉ là `public` keyword

Một type public trong bytecode có thể trở thành dependency của hàng trăm consumer.

Sau khi release:

```kotlin
class Client(
    val config: Config
)
```

consumer có thể compile trực tiếp against constructor và property đó.

Nếu version sau đổi:

```kotlin
class Client internal constructor(...)
```

source/binary compatibility có thể vỡ.

Public surface phải nhỏ và có chủ ý ngay từ đầu.

---

## 2. Source compatibility và binary compatibility khác nhau

Source compatibility hỏi:

```text
consumer source cũ compile lại với library mới được không?
```

Binary compatibility hỏi:

```text
consumer APK/module đã compile trước đó có chạy với binary library mới không?
```

Một thay đổi có thể source-compatible nhưng binary-incompatible hoặc ngược lại.

SDK production cần hiểu cả hai nếu consumer có dynamic/plugin/multi-module distribution hoặc dependency resolution phức tạp.

---

## 3. Kotlin default argument có ABI implications

Ví dụ:

```kotlin
fun login(
    username: String,
    timeoutMs: Long = 5_000
)
```

Kotlin compiler sinh helper/default machinery.

Java consumer không tự thấy default parameter như Kotlin.

Nếu SDK cần Java-friendly API, cân nhắc overload explicit hoặc `@JvmOverloads` có chủ ý.

Đừng assume Kotlin ergonomics tự động map tốt sang Java ABI.

---

## 4. `@JvmName`, `@JvmField`, `@JvmStatic` thay đổi Java surface

Kotlin source đẹp có thể tạo Java call site khó dùng.

Library public API nên review từ cả Kotlin và Java nếu support Java consumer.

Ví dụ companion factory:

```kotlin
class Client private constructor(...) {
    companion object {
        @JvmStatic
        fun create(config: Config): Client = ...
    }
}
```

Java consumer:

```java
Client.create(config);
```

API ergonomics là part của compatibility contract.

---

## 5. Nullability annotation là contract với Java consumer

Kotlin type:

```kotlin
fun token(): String?
```

rõ nullability.

Java boundary có thể mất một phần type-safety nếu annotation metadata không được preserve/understood.

SDK nên tránh ambiguous platform type trong public API.

---

## 6. Expose interface, hide implementation khi implementation có change axis lớn

Ví dụ:

```kotlin
interface AnalyticsClient {
    fun track(event: Event)
}
```

Implementation network/storage có thể thay đổi mà consumer không biết.

Nhưng đừng tạo interface cho mọi data class vô cớ. Abstraction cần bảo vệ một change axis cụ thể.

---

## 7. Public model nên độc lập internal transport model

Không expose Retrofit/Moshi/Room-specific type trong API nếu không muốn consumer phụ thuộc implementation.

Bad:

```kotlin
fun events(): Flow<List<EventEntity>>
```

nếu `EventEntity` là Room entity nội bộ.

Better:

```kotlin
fun events(): Flow<List<Event>>
```

Internal schema có thể migrate mà public contract ổn định.

---

## 8. Dependency leakage mở rộng compatibility surface

Nếu public method trả type từ third-party library:

```kotlin
fun client(): okhttp3.OkHttpClient
```

SDK đã biến OkHttp version/API thành part của public contract.

Consumer có thể buộc dependency version theo SDK hoặc gặp conflict.

Expose third-party type chỉ khi đó là intentional integration surface.

---

## 9. `api` dependency có thể leak transitive surface

Library dùng Gradle `api(...)` khiến consumer compile thấy dependency đó.

`implementation(...)` giữ dependency private hơn.

Chọn `api` khi public ABI thực sự cần, không vì build fix nhanh.

---

## 10. Dependency conflict là consumer safety problem

SDK A cần library X v1, app cần X v2.

Nếu binary incompatible, runtime có thể crash:

```text
NoSuchMethodError
ClassNotFoundException
VerifyError
```

SDK nên giảm dependency footprint, tránh pin version cứng không cần thiết và test với representative consumer graph.

---

## 11. Shading/relocation đôi khi cần nhưng có cost

Nếu SDK buộc dùng dependency dễ conflict, có thể relocate package bằng shading.

Nhưng shading:

- tăng artifact size,
- complicate license/security updates,
- có thể break reflection/resource loading.

Dùng khi conflict risk thật, không mặc định.

---

## 12. Android resource cũng là public surface

AAR có thể đóng góp:

```text
layout
drawable
string
style
attr
```

Resource name collision với app/SDK khác có thể xảy ra.

Prefix resource:

```text
my_sdk_*
```

là practice hữu ích cho library lớn.

---

## 13. Manifest contribution phải tối thiểu

SDK auto-add:

```text
permission
service
receiver
provider
metadata
```

làm app host chịu behavior mà có thể không nhận ra.

Mỗi manifest entry nên trả lời:

```text
vì sao cần?
exported không?
permission guard?
startup cost?
consumer disable/override được không?
```

---

## 14. Auto-initialization là consumer startup debt

SDK dùng ContentProvider để auto-init rất tiện nhưng chạy trên startup path consumer.

Nếu initialization nặng, mọi app tích hợp đều trả latency cost.

Ưu tiên lazy/on-demand khi feature không cần trước first interaction.

Nếu auto-init cần thiết, keep work tối thiểu.

---

## 15. SDK không được assume Activity tồn tại

Library có thể được gọi từ:

```text
Service
Receiver
Worker
Application
headless process
```

Nếu API core yêu cầu Activity context cho mọi operation, coupling quá mạnh.

Phân biệt:

```text
application-scoped capability
vs
UI-scoped capability
```

UI flow mới nhận Activity/Fragment khi thật sự cần.

---

## 16. Context lifetime phải rõ

Không giữ Activity context trong singleton.

Nếu SDK client sống application lifetime, giữ `applicationContext` khi phù hợp.

Nếu cần Activity cho permission/UI, nhận ephemeral reference ở method boundary và không cache lâu dài.

---

## 17. Threading contract phải document

Consumer cần biết callback chạy thread nào.

API mơ hồ:

```kotlin
client.fetch { result -> ... }
```

callback có thể background hoặc main tùy implementation.

Better contract:

```text
callbacks delivered on main thread
```

hoặc expose suspend API và để caller quyết định context khi hợp lý.

---

## 18. Suspend API nên main-safe

SDK public suspend function không nên yêu cầu consumer nhớ chuyển IO nếu underlying work blocking.

```kotlin
suspend fun loadConfig(): Config =
    withContext(ioDispatcher) {
        blockingStore.read()
    }
```

Threading detail nằm trong SDK.

---

## 19. Callback cancellation cần explicit handle

Nếu SDK expose callback API:

```kotlin
fun fetch(callback: Callback): RequestHandle
```

consumer cần cách cancel khi lifecycle kết thúc.

Không có cancel path dễ tạo stale callback/leak.

---

## 20. Flow API cần define hot/cold semantics

Public SDK method:

```kotlin
fun events(): Flow<Event>
```

consumer cần biết:

```text
mỗi collector tạo connection riêng?
replay không?
buffer policy?
start/stop resource khi nào?
```

Flow type không tự document resource semantics.

---

## 21. Exception type public trở thành API contract

Nếu SDK throw internal Retrofit exception trực tiếp, consumer có thể bắt `HttpException` và phụ thuộc implementation.

Tốt hơn map sang SDK-defined error model nếu cần stable contract.

```kotlin
sealed interface SdkError {
    data object NetworkUnavailable : SdkError
    data class Server(val code: Int) : SdkError
    data object Unauthorized : SdkError
}
```

---

## 22. Error contract phải phân biệt retryable/permanent

Consumer cần biết có retry được không.

SDK có thể expose metadata:

```kotlin
data class Failure(
    val kind: FailureKind,
    val retryAfter: Duration? = null
)
```

Đừng bắt consumer reverse-engineer message string.

---

## 23. Logging trong SDK phải respect host privacy

Không log:

```text
token
full request body
PII
password
```

SDK debug logging nên opt-in và redact.

Consumer có privacy/compliance requirement riêng; SDK không được âm thầm thu thập vượt contract.

---

## 24. Telemetry SDK phải có backpressure/storage policy

Analytics event queue có thể tăng khi offline.

SDK cần policy:

```text
max queue size
retention
batch size
retry
sampling
disk limit
```

Không để analytics chiếm disk vô hạn hoặc retry làm hao pin.

---

## 25. SDK phải degrade gracefully khi host misconfigure

Ví dụ API key thiếu.

Bad:

```text
crash Application startup
```

Better tùy criticality:

```text
return initialization error
log actionable diagnostic
disable feature safely
```

Library không nên kéo cả app host crash nếu feature optional.

---

## 26. Native code làm failure boundary nguy hiểm hơn

Kotlin exception thường có thể catch.

Native SIGSEGV có thể kill toàn process.

JNI/NDK boundary cần validation chặt hơn:

```text
null
array length
buffer capacity
pointer lifetime
thread attachment
exception pending
```

---

## 27. JNI local/global reference lifetime khác nhau

Local reference thường chỉ valid trong native call/frame.

Nếu giữ Java object qua call, cần global reference phù hợp và delete khi xong.

Giữ local ref lâu có thể use-after-lifetime; quên delete global ref gây leak.

---

## 28. `JNIEnv*` gắn với thread

Không cache `JNIEnv*` từ thread A rồi dùng trên thread B.

Native thread cần attach JVM để lấy environment hợp lệ, rồi detach khi lifecycle yêu cầu.

Thread ownership là core JNI invariant.

---

## 29. Java exception từ JNI phải check

Nếu native gọi Java method và Java throw, JNI có pending exception.

Tiếp tục gọi API khác khi exception pending có thể gây behavior khó đoán.

Native bridge nên check/propagate/clear theo contract đúng.

---

## 30. Native buffer ownership phải explicit

Nếu Kotlin truyền `ByteBuffer` direct sang native, hỏi:

```text
ai giữ memory?
native có giữ pointer sau call không?
GC có move/free backing memory không?
write/read concurrency?
```

Boundary docs phải nói rõ lifetime.

---

## 31. ABI split ảnh hưởng distribution và testing

Native `.so` build theo ABI:

```text
arm64-v8a
armeabi-v7a
x86_64
```

Nếu một ABI thiếu library hoặc behavior khác, app có thể chỉ crash trên nhóm device đó.

CI/release test cần representative ABI.

---

## 32. Native symbolication là production requirement

Crash address:

```text
#00 pc 00000000001234 libfoo.so
```

không hữu ích nếu không có symbol mapping/build artifact tương ứng.

Release pipeline phải archive/upload native symbols theo version/build id.

---

## 33. Sanitizer hữu ích để bắt memory bug trước production

Address/UndefinedBehavior sanitizer hoặc tooling tương ứng giúp bắt:

```text
use-after-free
buffer overflow
undefined behavior
```

Native memory bug hiếm nhưng blast radius lớn.

---

## 34. 16 KB page-size compatibility là native packaging/runtime concern

Modern Android device ecosystem có thể dùng page size khác 4 KB.

Native library build/link alignment phải compatible.

Nếu SDK ship prebuilt `.so`, SDK author chịu trách nhiệm kiểm tra binary của mình, không đẩy risk cho consumer app.

---

## 35. Native code nên được dùng khi lợi ích rõ

Lý do hợp lý:

```text
reuse C/C++ engine
media/codec
high-performance numerical/native library
platform low-level integration
```

Không dùng NDK chỉ để “nhanh hơn” mà chưa benchmark.

JNI crossing cũng có overhead và complexity.

---

## 36. JNI boundary nên coarse-grained

Bad:

```text
Kotlin gọi native cho từng pixel/từng item nhỏ
```

Crossing hàng triệu lần tạo overhead.

Better:

```text
pass batch/buffer
native xử lý chunk lớn
return aggregated result
```

Optimize boundary frequency trước micro-optimize function body.

---

## 37. Public native ABI và internal native ABI khác nhau

Nếu SDK expose C API cho third party, ABI stability trở thành contract dài hạn.

Nếu native chỉ internal sau JNI, có thể refactor tự do hơn miễn Java/Kotlin API ổn định.

Giữ native implementation private nếu không cần external ABI.

---

## 38. Deprecation nên có migration path

Bad:

```kotlin
@Deprecated("Old")
fun oldApi()
```

Better:

```kotlin
@Deprecated(
    message = "Use track(Event) instead",
    replaceWith = ReplaceWith("track(Event(name, properties))")
)
fun log(name: String, properties: Map<String, Any>)
```

Docs cần giải thích semantic difference nếu migration không 1:1.

---

## 39. Removal cần release policy

Public API không nên deprecated hôm nay, remove ngày mai nếu SDK có broad consumer base.

Policy ví dụ:

```text
deprecate in minor
keep ít nhất N release cycles
remove in major
publish migration guide
```

SemVer chỉ hữu ích khi team thực sự tôn trọng compatibility policy.

---

## 40. Behavioral compatibility quan trọng không kém signature

Method signature không đổi nhưng behavior thay:

```text
callback trước chạy main, giờ chạy background
retry count từ 1 thành 5
timeout từ 5s thành 60s
auto-init bắt đầu network call
```

Consumer có thể vỡ dù binary compatibility pass.

Release note phải cover behavior contract.

---

## 41. Performance regression của SDK là externalized cost

SDK thêm 100ms startup nghĩa là mọi host app trả cost đó.

SDK nên benchmark:

```text
initialization time
memory overhead
thread count
network usage
artifact size
```

Consumer-centric performance là part của quality.

---

## 42. SDK size budget cần track transitive cost

AAR 100 KB nhưng kéo dependency 5 MB vẫn làm consumer artifact lớn.

Measure final consumer impact, không chỉ file AAR.

---

## 43. Custom Lint giúp encode integration rule

Nếu SDK yêu cầu:

```text
API chỉ gọi từ main thread
manifest config bắt buộc
permission usage pattern
forbidden deprecated API
```

custom Lint có thể phát hiện sớm ở consumer build.

Compiler/build-time feedback tốt hơn runtime crash.

---

## 44. SDK sample app phải là real consumer

Đừng để sample module access internal project implementation đặc biệt.

Sample nên consume published/local Maven artifact gần giống external consumer.

Như vậy detect:

```text
missing consumer rules
missing transitive dependency
resource/manifest issue
Java/Kotlin API ergonomics
```

---

## 45. Compatibility test nên compile old consumer against new SDK

Lưu sample consumer/API dump từ version trước.

CI new SDK có thể chạy:

```text
binary API diff
source compile test
release minified app test
Java consumer test
Kotlin consumer test
```

Đây là contract regression suite.

---

## 46. API dump giúp review accidental public surface

Tool/API dump cho thấy public declarations thay đổi trong PR.

Reviewer có thể hỏi:

```text
API mới này thật sự cần public?
nullable contract đúng chưa?
third-party type leak không?
```

Public API review nên explicit như database migration review.

---

## 47. Consumer-driven compatibility matrix

SDK test matrix nên gồm:

```text
min supported Android API
latest Android API
representative AGP/Kotlin ranges nếu support
R8 on/off
Java/Kotlin consumer
common dependency version combinations
major OEM/device nếu hardware feature
```

Không thể support “mọi version”; support range phải document.

---

## 48. Security update có thể buộc compatibility trade-off

Nếu dependency có vulnerability nghiêm trọng, SDK có thể cần upgrade breaking dependency.

Policy cần cân bằng:

```text
consumer safety
compatibility
migration urgency
```

Security patch không nên bị trì hoãn vô hạn chỉ để tránh major version.

---

## 49. Release artifact provenance cho SDK

Mỗi published artifact nên map được về:

```text
git commit
CI run
source tag
toolchain
dependency lock
signing/provenance metadata
```

Nếu Maven artifact bị incident, team phải reproduce và audit được.

---

## 50. SDK reliability checklist

| Câu hỏi | Ý nghĩa |
|---|---|
| Public surface tối thiểu chưa? | giảm compatibility burden |
| Third-party type có leak không? | dependency coupling |
| Java consumer dùng dễ không? | interop contract |
| Callback/thread semantics document chưa? | concurrency safety |
| Initialization có nằm startup path không? | host performance |
| Consumer R8 rules đủ chưa? | release safety |
| Manifest entry/exported/security đúng chưa? | host security |
| Native symbols archived chưa? | crash forensic |
| ABI/page-size test chưa? | native compatibility |
| Old consumer compile/run được không? | API evolution |
| Behavioral change có release note không? | semantic compatibility |
| Artifact reproducible/auditable không? | supply-chain/release |

---

## 51. Kết luận

Một SDK tốt không chỉ “có API dễ gọi”. Nó phải là một dependency tử tế trong ecosystem của consumer.

Mental model:

```text
small public contract
-> stable source/binary behavior
-> minimal dependency leakage
-> explicit lifetime/thread/error semantics
-> release-safe R8/resources/manifest
-> safe native boundary
-> measurable host impact
-> controlled deprecation/migration
-> reproducible artifact
```

Application code có thể sửa theo cadence của chính team. SDK code phải sống cùng cadence của nhiều consumer, vì vậy mỗi public decision đều có chi phí dài hạn.