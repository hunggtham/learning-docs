# Case 08 — Kotlin/JVM, K2 Compiler, Generated Code và Runtime Internals

Kotlin giúp Android code ngắn và an toàn hơn Java, nhưng production bug khó thường nằm dưới abstraction: generic bị type erasure, value class bị boxing, `suspend` thành state machine, lambda capture giữ object lâu hơn dự kiến, reflection bị R8 strip metadata, annotation đặt sai use-site target, KSP/KAPT sinh code khác version, hoặc một library đổi public ABI dù source nhìn gần giống.

Không cần đọc bytecode mỗi ngày. Mục tiêu chương này là biết **khi nào abstraction leak** và có mental model đủ để debug.

## 1. Kotlin trên Android không chạy “trực tiếp” như source

Flow khái quát:

```text
Kotlin source
→ Kotlin compiler frontend/analysis (K2)
→ JVM bytecode / compiler-generated structures
→ D8/R8 transform, desugar, shrink, optimize
→ DEX
→ Android Runtime (ART)
```

Compose, serialization, Parcelize, DI/code generation hoặc KSP processor có thể thêm generated code/compiler transformation trong pipeline.

Vì vậy bug build/runtime đôi khi không thể hiểu chỉ từ `.kt` source.

## 2. K2 là compiler frontend, không phải “Kotlin 2 syntax” đơn thuần

Kotlin 2.x chuyển compiler frontend sang K2. Điều developer cần quan tâm là ecosystem compatibility: Kotlin version, AGP, Compose compiler integration, serialization plugin, KSP, annotation processor và library metadata phải tương thích.

Khi upgrade Kotlin, hãy coi đó là toolchain migration:

```text
Kotlin
AGP
Gradle
JDK
Compose/compiler plugin
KSP/KAPT processors
serialization/other compiler plugins
```

Không chỉ đổi `kotlin("android") version ...` rồi assume mọi plugin tự tương thích.

## 3. Kotlin metadata

Kotlin class trên JVM mang metadata để tooling/compiler hiểu feature Kotlin mà Java bytecode thuần không biểu diễn đầy đủ. Reflection/library tooling có thể đọc metadata.

R8/proguard hoặc shading nếu xử lý sai metadata/annotation có thể làm reflection framework fail. Đây là lý do keep rule phải dựa vào cơ chế library thật chứ không copy một rule global.

## 4. `suspend` không tạo thread

Một `suspend fun` được compiler biến thành dạng continuation/state machine. Nó có thể pause và resume mà không block thread, nếu implementation gọi API suspending/non-blocking đúng.

Conceptual transformation:

```kotlin
suspend fun load(): Result {
    val a = apiA()
    val b = apiB(a)
    return combine(a, b)
}
```

Compiler cần lưu local state giữa suspension point, gần giống một state machine:

```text
state 0 -> call apiA -> suspend
resume -> state 1 -> call apiB -> suspend
resume -> state 2 -> combine -> return
```

Điều này giải thích tại sao stack trace coroutine có hình dạng khác synchronous call và tại sao local variable cần survive suspension.

## 5. Suspend không làm blocking code thành non-blocking

```kotlin
suspend fun bad() {
    Thread.sleep(5_000)
}
```

Function có keyword `suspend` nhưng vẫn block thread 5 giây. Blocking I/O/CPU work vẫn cần dispatcher/executor phù hợp.

`suspend` mô tả khả năng suspension trong call chain, không tự quyết định thread.

## 6. Coroutine context và thread local

Coroutine có thể resume trên thread khác. Code dựa raw `ThreadLocal` có thể sai nếu không bridge bằng `asContextElement` hoặc mechanism phù hợp.

Security/request tracing context nên được propagate có chủ ý. Đừng assume thread identity là coroutine identity.

## 7. `inline` thực sự làm gì?

Higher-order function tạo lambda object/call overhead trong một số trường hợp. `inline` cho phép compiler inline function body/lambda ở call site, đồng thời mở khả năng `reified` type parameter và non-local return.

```kotlin
inline fun <reified T> Json.decode(value: String): T = ...
```

`reified` hoạt động vì call site biết concrete type khi inline. Generic function bình thường chịu type erasure trên JVM.

## 8. Không inline mọi function

Inline làm bytecode ở call site lớn hơn. Public inline function còn có compatibility implication vì implementation được copy vào consumer khi compile.

Dùng inline chủ yếu cho HOF hot/idiomatic, reified requirement hoặc API design rõ; không thêm `inline` như performance decoration.

## 9. `noinline` và `crossinline`

Trong inline function, lambda parameter mặc định có thể inline.

`noinline` giữ lambda như object, cần khi lưu/truyền lambda như value.

`crossinline` ngăn non-local return khi lambda sẽ chạy ở context không cho phép return khỏi caller.

```kotlin
inline fun execute(crossinline block: () -> Unit) {
    executor.execute { block() }
}
```

Nếu không hiểu non-local return, code inline callback có thể gây compile error khó hiểu.

## 10. Generic type erasure

Trên JVM:

```kotlin
fun <T> isListOf(value: Any): Boolean {
    // không thể runtime check đầy đủ List<T>
}
```

Runtime thường chỉ biết `List`, không biết element `T`. `reified` giúp một số check tại inline call site nhưng nested generic vẫn có giới hạn.

Serialization/reflection framework cần type token, generated serializer hoặc metadata để giữ type information.

## 11. Variance ở source vs JVM wildcard

Kotlin `out T`/`in T` biểu diễn variance ở type system. Khi expose API cho Java, wildcard signature có thể khác mong muốn.

`@JvmSuppressWildcards` và `@JvmWildcard` đôi lúc cần để điều chỉnh Java-facing signature, nhưng đừng dùng nếu không inspect API thực tế.

Library/public API nên test Java interoperability nếu consumer có Java.

## 12. Platform type

Java API không annotate nullability có thể thành `String!` trong Kotlin. Compiler cho phép xử lý như nullable hoặc non-null, nên NPE vẫn có thể xảy ra.

Boundary Java legacy nên annotate nullability hoặc normalize value ngay khi vào Kotlin layer.

```kotlin
val name: String = requireNotNull(javaApi.name) {
    "Legacy API returned null name"
}
```

Crash ở boundary có message rõ hơn crash xa downstream.

## 13. `lateinit` runtime check

`lateinit var` bỏ nullable syntax nhưng không bảo đảm property đã init. Read trước init ném `UninitializedPropertyAccessException`.

Dùng khi lifecycle/framework thực sự init sau construction; không dùng để né constructor injection.

Trong Fragment View Binding, `lateinit`/nullable backing field phải theo View lifecycle, không Activity/Fragment object lifetime.

## 14. `lazy`

`lazy` mặc định có synchronization semantics phù hợp multi-thread. Có các mode khác (`SYNCHRONIZED`, `PUBLICATION`, `NONE`) với trade-off.

Android main-thread-only object có thể dùng mode phù hợp nếu chắc chắn access single-thread, nhưng optimization này hiếm khi là bottleneck. Ưu tiên correctness.

## 15. Data class generation

Compiler generate `equals`, `hashCode`, `toString`, `componentN`, `copy` cho primary constructor properties.

`copy()` là shallow copy:

```kotlin
data class State(val items: MutableList<String>)

val a = State(mutableListOf("A"))
val b = a.copy()
b.items += "B"
// a.items cũng thấy B vì cùng list reference
```

Immutable state cần immutable nested value hoặc defensive copy.

## 16. `object` và singleton initialization

Kotlin `object` tạo singleton semantics theo runtime/classloader. Nó tiện cho stateless utility, nhưng global mutable state trong object gây hidden dependency/test contamination.

Android process death reset singleton memory. Đừng dùng object làm persistence/session source of truth nếu state cần restore.

## 17. Companion object và Java API

Companion member không phải static JVM method theo đúng nghĩa mặc định. `@JvmStatic` có thể generate static bridge cho Java-friendly API.

```kotlin
class Parser {
    companion object {
        @JvmStatic
        fun create(): Parser = Parser()
    }
}
```

Chỉ dùng khi Java interop/API yêu cầu.

## 18. Top-level function

Top-level Kotlin function compile thành static method trong generated file class trên JVM. `@file:JvmName` có thể control Java-visible class name.

Đây là lý do top-level pure utility hoàn toàn idiomatic; không cần tạo `Utils` object chỉ để chứa static-like function.

## 19. Extension function là static dispatch

Extension không thực sự thêm virtual method vào class.

```kotlin
fun Animal.sound() = "animal"
fun Dog.sound() = "dog"
```

Extension được resolve theo compile-time receiver type, không polymorphic virtual dispatch. Nếu behavior cần override, dùng member/interface.

## 20. Sequence vs Collection

```kotlin
items.map(...).filter(...).take(10)
```

Collection chain có thể tạo intermediate collection. `asSequence()` xử lý lazy element-by-element và hữu ích khi chain dài/data lớn/early termination.

Nhưng Sequence có iterator/lambda overhead và không luôn nhanh hơn cho list nhỏ. Benchmark hot path thay vì cargo-cult `asSequence()`.

## 21. Boxing primitive

Kotlin `Int` thường map JVM primitive `int` khi có thể, nhưng generic/nullable có thể box thành `Integer`.

```kotlin
val a: Int = 1       // có thể primitive
val b: Int? = 1      // boxed
val list: List<Int>  // elements boxed trên JVM
```

Trong UI/business code bình thường không đáng lo. Trong loop cực nóng/large numeric data, allocation/boxing có thể hiện trên profiler.

## 22. Value class và boxing

```kotlin
@JvmInline
value class UserId(val value: String)
```

Value class thường tránh allocation wrapper trong nhiều context, nhưng có thể box khi nullable, generic, interface/polymorphic boundary hoặc runtime cần object.

Đừng hứa “zero allocation”. Dùng value class trước hết cho type safety/domain modeling; performance là secondary và cần đo.

## 23. Lambda capture

```kotlin
fun screen(activity: Activity): () -> Unit = {
    activity.finish()
}
```

Lambda capture giữ reference `activity`. Nếu lambda được singleton/store lâu hơn Activity, leak.

Coroutine/callback leak investigation nên inspect capture chain, không chỉ class field rõ ràng.

## 24. Anonymous object và inner class

`inner class` giữ reference tới outer instance. Nested class không giữ implicit outer reference.

Listener anonymous object có thể capture outer Activity/Fragment. Registration lifetime sai dễ leak.

## 25. Annotation use-site target

Kotlin property có thể tương ứng field/getter/setter/constructor parameter. Annotation framework đôi khi cần target cụ thể:

```kotlin
@get:JsonIgnore
val internalValue: String

@field:Inject
lateinit var dependency: Dependency
```

Nếu annotation “không có tác dụng”, inspect framework đọc field, getter hay parameter nào.

## 26. Reflection vs generated code

Reflection linh hoạt nhưng có runtime cost và R8/metadata complexity. Generated code chuyển nhiều lỗi sang compile time và shrink-friendly hơn trong nhiều framework.

Room, modern DI/codegen, Kotlin serialization thường tận dụng generated/compiled knowledge thay vì reflection thuần.

Không vì thế reflection luôn xấu; chỉ cần biết runtime contract và keep requirement.

## 27. KAPT

KAPT bridge Java annotation processing vào Kotlin bằng stub generation. Nó từng là nền tảng của nhiều library nhưng có build cost đáng kể.

Migration khỏi KAPT chỉ nên làm khi processor/library hỗ trợ alternative ổn định. Một project có thể coexist KAPT và KSP trong giai đoạn migration.

## 28. KSP

KSP (Kotlin Symbol Processing) cung cấp symbol model gần Kotlin hơn và thường hiệu quả hơn KAPT cho processor hỗ trợ.

KSP processor tạo source/resource trong build. Generated output phải là deterministic function của source/config nếu muốn cache/reproducible build tốt.

KSP version phải tương thích Kotlin compiler line phù hợp; upgrade Kotlin cần kiểm tra processor ecosystem.

## 29. Compiler plugin

Serialization và Compose có compiler integration. Compiler plugin có quyền transform/augment compilation mạnh hơn annotation processor.

Do đó plugin version mismatch có thể gây compile/runtime issue sâu. Toolchain matrix cần được review như một unit.

## 30. Compose compiler/runtime mental model

Composable function không phải ordinary function đơn giản. Compiler thêm machinery để runtime theo dõi composition group, parameter/state read và skipping/recomposition.

Bạn không cần đọc generated bytecode hằng ngày, nhưng khi optimize cần hiểu:

- state read quyết định invalidation scope;
- stable/immutable input giúp skipping trong context phù hợp;
- key/identity ảnh hưởng state association;
- composition, layout, draw là phase khác nhau.

## 31. Stability không đồng nghĩa `val`

Một class có toàn `val` nhưng chứa mutable list vẫn có mutation hidden.

```kotlin
data class UiModel(
    val items: MutableList<Item>
)
```

Compose/state reasoning cần semantic immutability, không chỉ syntax `val`.

## 32. `@Immutable`/`@Stable` không phải performance magic

Annotation stability là contract bạn hứa với Compose runtime/compiler. Annotate sai có thể khiến UI không update đúng hoặc làm reasoning sai.

Chỉ annotate khi type thực sự thỏa contract; đừng dùng để silence performance warning mà không hiểu mutation semantics.

## 33. Bytecode inspection

Android Studio/Kotlin tooling có thể decompile bytecode để hiểu:

- property getter/setter;
- default argument synthetic method;
- suspend state machine;
- inline result;
- companion/static bridge;
- boxing.

Khi interop/performance bug khó, inspect generated representation thường nhanh hơn đoán.

## 34. Default argument và Java

Kotlin default parameter thuận tiện nhưng Java caller không tự thấy overload tương đương. `@JvmOverloads` generate overload trong case phù hợp.

```kotlin
class Client @JvmOverloads constructor(
    val timeout: Long = 5_000,
    val retries: Int = 2
)
```

Không generate hàng loạt overload nếu API Java không cần.

## 35. Checked exception

Kotlin không enforce checked exception. Nếu Kotlin API được Java gọi và cần khai báo throws, `@Throws` giúp generate signature.

```kotlin
@Throws(IOException::class)
fun read(): Data = ...
```

## 36. `Nothing`

`Nothing` là type không có value, dùng cho function không return bình thường:

```kotlin
fun fail(message: String): Nothing = error(message)
```

Nó giúp type inference hiểu branch throw không cần produce value.

## 37. `Unit` vs Java `void`

`Unit` là type có single value `Unit`; Java `void` là absence return. Interop/compiler có mapping riêng. Higher-order function `() -> Unit` là object/function type nhận result Unit, khác khái niệm một method void đơn thuần.

## 38. Equality và generated `equals`

`==` gọi structural equality (`equals`), `===` kiểm tra reference identity.

Data class generated equals dùng primary constructor property equality. Với array, `Array.equals` semantics khác content equality kỳ vọng; dùng `contentEquals`/`contentDeepEquals` khi cần.

Domain type chứa array cần custom equality nếu content semantics quan trọng.

## 39. Hash-based collection invariant

Nếu object dùng key trong HashMap/HashSet, fields tham gia `equals/hashCode` không nên mutate theo cách làm hash thay đổi khi object đang trong set/map.

Immutable data class key an toàn hơn mutable entity object.

## 40. JVM memory model và thread safety

`val` chỉ ngăn reassignment reference, không tự làm object thread-safe. MutableList trong val vẫn mutable.

Shared mutable state giữa coroutine trên nhiều dispatcher cần confinement, Mutex, atomic primitive hoặc immutable state transition phù hợp.

Coroutine không loại bỏ data race nếu code chạy concurrent thật.

## 41. `volatile`, atomic và Mutex

`@Volatile` giúp visibility của một field, không biến multi-step operation thành atomic.

```kotlin
@Volatile var count = 0
count++ // read-modify-write, không atomic
```

Dùng AtomicInteger/atomic primitive cho operation đơn giản; Mutex cho critical section suspending; single-thread confinement/state reducer khi phù hợp.

## 42. Exception và cancellation

`CancellationException` là control signal của coroutine. Broad catch:

```kotlin
try {
    work()
} catch (e: Exception) {
    // nguy hiểm: có thể nuốt cancellation
}
```

Nếu catch generic, rethrow cancellation:

```kotlin
catch (e: CancellationException) {
    throw e
}
```

Hoặc structure catch cụ thể hơn.

## 43. Result và exception API design

Kotlin `Result<T>` hữu ích ở một số boundary nhưng không phải universal domain error model. Domain có nhiều error typed rõ ràng có thể dùng sealed result.

Public Java-facing API với Kotlin Result cần cân nhắc interop. API design phải xét consumer.

## 44. Binary compatibility

Library/module API đổi source-compatible chưa chắc binary-compatible với consumer đã compile trước.

Thay method signature, remove class, đổi JVM name hoặc inline/public ABI có thể gây `NoSuchMethodError`/`NoClassDefFoundError` nếu artifact mix version.

Internal app monorepo thường rebuild cùng lúc nên risk thấp hơn published library/dynamic module ecosystem.

## 45. Public inline API compatibility

Consumer compile body inline vào bytecode của họ. Vì vậy behavior cũ có thể nằm trong consumer cho tới khi recompile, và internal symbol referenced bởi public inline cần visibility rules (`@PublishedApi` khi phù hợp).

Library author cần hiểu điều này trước khi expose nhiều inline implementation detail.

## 46. R8 shrinking

R8 phân tích reachability và có thể remove/rename/optimize code. Reflection/JNI/resource-by-name làm static analysis khó.

Keep rule nên là minimum contract:

```text
keep exactly reflected members
keep required annotation/metadata
consumer rule đi cùng library
```

Không disable shrink để tránh debug một issue.

## 47. Mapping và crash

Obfuscated stack trace production cần mapping file đúng build. Mapping là artifact của release, không được overwrite/mất.

Build ID/versionCode phải liên kết mapping để symbolicate incident sau nhiều tháng.

## 48. D8/desugaring

Android device API cũ không có mọi Java language/library feature mới. Desugaring transform một số bytecode/API để hỗ trợ target thấp hơn.

Khi dùng Java time/API mới trên minSdk cũ, core library desugaring có thể liên quan. Đừng assume compileSdk cao nghĩa mọi runtime device có API đó native.

## 49. API level check vẫn cần

Compile-time symbol availability khác runtime availability.

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.X) {
    // API mới
}
```

AndroidX compatibility wrapper thường nên được ưu tiên khi nó abstract behavior chính xác.

## 50. Method count và dependency cost

MultiDex ít còn là daily issue như thời cũ ở nhiều project hiện đại, nhưng dependency vẫn có cost: method/code size, startup initializer, transitive dependency, resource và security surface.

Review dependency không chỉ theo “thêm một dòng Gradle”.

## 51. Allocation profiler và heap

Nếu profiler thấy allocation spike, trace source trước. Có thể là JSON parsing, bitmap, list transform, string format, lambda capture hoặc recomposition object creation.

Đừng rewrite idiomatic Kotlin sang imperative code chỉ dựa trên giả định “functional chậm”. Measure representative workload.

## 52. Benchmark JVM vs Android

Microbenchmark trên desktop JVM không phản ánh ART/device hoàn toàn. AndroidX Benchmark chạy môi trường Android phù hợp hơn cho hot code cần đo.

Macrobenchmark dùng cho user journey; Microbenchmark cho function/component hot path.

## 53. Build scan/profile

Slow Gradle build cần profile configuration vs task execution, annotation processing/code generation, non-cacheable task, dependency resolution.

Không giải slow build chỉ bằng tăng heap. Root cause có thể là module graph, KAPT processor hoặc task luôn out-of-date.

## 54. Generated source ownership

Không edit generated source bằng tay. Fix input/processor/template.

Generated folder thường không commit trừ tool explicitly yêu cầu; CI phải tạo lại được. Nếu generated artifact cần review/API tracking, thiết kế workflow rõ.

## 55. Senior debugging workflow

Khi gặp bug “Kotlin magic”, dùng thứ tự:

```text
reproduce minimal
→ xác định source-level semantics
→ inspect Java/JVM signature hoặc generated source
→ inspect bytecode/decompiled form khi cần
→ kiểm tra R8/consumer rules/build variant
→ profile/trace runtime nếu performance/lifetime
→ thêm regression test ở boundary
```

Đừng nhảy thẳng vào decompile nếu source-level bug đã đủ giải thích.

## 56. Master takeaway

Kotlin abstraction tốt cho productivity, nhưng senior/master cần biết abstraction được thực hiện thế nào ở những điểm ảnh hưởng correctness, performance và compatibility.

Hãy nhớ các leak point chính: **type erasure, boxing, generated code, coroutine state machine, capture/lifetime, annotation target, Java interop, compiler/plugin compatibility, reflection/R8 và binary ABI**.

Bạn không cần tối ưu theo bytecode mỗi ngày. Bạn cần khả năng hạ xuống tầng bytecode/runtime khi evidence cho thấy vấn đề nằm ở đó, rồi quay lại thiết kế source-level đơn giản nhất có thể.
