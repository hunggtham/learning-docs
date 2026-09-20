# Kotlin + Android Version Evolution — từ Kotlin 1.x đến 2.4 và cách đọc project cũ/mới

Version trong Kotlin + Android phức tạp hơn việc nhìn một con số như `2.4.20`. Một project Android thực tế có nhiều trục version độc lập nhưng liên quan với nhau: version của ngôn ngữ Kotlin, Kotlin compiler, Kotlin Gradle Plugin, Compose compiler, Android Gradle Plugin, Gradle, JDK, `jvmTarget`, Android SDK, Jetpack libraries và policy của Google Play.

Nếu chỉ nhớ “project đang dùng Kotlin 2.4” mà không hiểu các trục này, rất dễ gặp lỗi kiểu compiler plugin không tương thích, AGP không hỗ trợ API level mới, library compile được nhưng consumer cũ không dùng được, hoặc app chạy tốt trên Android cũ nhưng đổi behavior sau khi tăng `targetSdk`.

File này được viết như **version map + migration guide**, tương tự cách học version evolution của Java, JavaScript/ECMAScript hoặc Swift: không chỉ hỏi phiên bản nào mới hơn, mà phải hiểu **mỗi thế hệ đã thay đổi mental model nào, code cũ trông ra sao, code mới nên viết như thế nào, và khi upgrade phải kiểm tra những boundary nào**.

---

## 1. Trước hết phải phân biệt các loại version

### 1.1 Kotlin release version

Ví dụ:

```text
1.9.25
2.0.21
2.1.20
2.2.21
2.3.20
2.4.20
```

Đây là version của Kotlin toolchain/release line. Nó ảnh hưởng compiler, standard library, Kotlin Gradle Plugin và các language/tooling feature đi kèm.

Tại thời điểm snapshot của bộ tài liệu này, stable line hiện tại là:

```text
Kotlin 2.4.20
Released: 2026-09-07
Release line: 2.4
```

Kotlin 2.4 được JetBrains liệt kê với support window tới cuối năm 2027. Con số này là snapshot, không phải version phải giữ cố định mãi mãi.

---

### 1.2 `languageVersion`

`languageVersion` quyết định **bộ quy tắc ngôn ngữ** mà compiler cho phép source code sử dụng.

Ví dụ conceptually:

```kotlin
kotlin {
    compilerOptions {
        languageVersion.set(KotlinVersion.KOTLIN_2_4)
    }
}
```

Một compiler mới có thể đôi khi compile code theo language level cũ để hỗ trợ migration/library compatibility.

Điểm quan trọng:

```text
compiler version != language version bắt buộc phải giống tuyệt đối
```

Compiler 2.x có thể hỗ trợ một số language/API version cũ, nhưng support window không vô hạn. Ví dụ từ Kotlin 2.2, language version 1.6 và 1.7 không còn được compiler hỗ trợ nữa.

---

### 1.3 `apiVersion`

`apiVersion` giới hạn version của Kotlin standard library API mà source code được phép gọi.

Mental model:

```text
languageVersion
= cú pháp và semantic nào được phép viết

apiVersion
= API stdlib tới version nào được phép dùng
```

Điều này hữu ích cho library author muốn compile bằng compiler mới nhưng vẫn tránh vô tình sử dụng API quá mới so với consumer target.

---

### 1.4 `jvmTarget`

`jvmTarget` quyết định bytecode JVM output được tạo cho JVM level nào.

Ví dụ:

```kotlin
import org.jetbrains.kotlin.gradle.dsl.JvmTarget

kotlin {
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_17)
    }
}
```

Không được nhầm:

```text
Kotlin version
JDK chạy Gradle
Java source compatibility
Java target compatibility
Kotlin jvmTarget
Android minSdk
```

đều là cùng một thứ.

Chúng liên quan nhưng là các contract khác nhau.

---

### 1.5 JDK toolchain

JDK toolchain là Java compiler/runtime toolchain dùng trong build.

Ví dụ:

```kotlin
kotlin {
    jvmToolchain(17)
}
```

Android Gradle Plugin cũng có yêu cầu JDK riêng theo version. Vì vậy upgrade AGP có thể buộc project nâng JDK dù source Kotlin không thay đổi.

---

### 1.6 Kotlin Gradle Plugin — KGP

Plugin thường xuất hiện dạng:

```kotlin
plugins {
    id("org.jetbrains.kotlin.android") version "2.4.20"
}
```

KGP nối Gradle với Kotlin compiler/toolchain.

Khi nói “upgrade Kotlin trong Android project”, trên thực tế thường đang thay đổi version KGP trong build configuration.

---

### 1.7 Android Gradle Plugin — AGP

AGP không phải Kotlin plugin.

```text
KGP
= Gradle ↔ Kotlin

AGP
= Gradle ↔ Android build model
```

AGP quyết định cách Android module được build, resource/manifest merge, variant, packaging, D8/R8, SDK support và nhiều behavior build khác.

Vì vậy:

```text
Kotlin 2.4.20
không đồng nghĩa
AGP phải là 2.4.20
```

Chúng có release cadence khác nhau.

Snapshot đang dùng trong library:

```text
Kotlin: 2.4.20
AGP baseline: 9.4.1
```

---

### 1.8 Gradle version

Gradle là build system bên dưới.

Ta có chuỗi dependency:

```text
Gradle
   ↑
AGP / KGP
   ↑
Android/Kotlin modules
```

Một KGP hoặc AGP mới có minimum/maximum Gradle compatibility riêng.

Kotlin 2.4.20 hỗ trợ chính thức Gradle 7.6.3 tới 9.7.0; dùng version khác có thể vẫn chạy nhưng không nằm trong fully supported range.

---

### 1.9 Android `minSdk`, `compileSdk`, `targetSdk`

Đây là ba version axis khác hẳn Kotlin.

```kotlin
android {
    compileSdk = 37

    defaultConfig {
        minSdk = 26
        targetSdk = 37
    }
}
```

Ý nghĩa:

```text
minSdk
= Android thấp nhất app cho phép cài/chạy

compileSdk
= Android API surface dùng để compile

targetSdk
= app tuyên bố đã thích nghi với behavior contract của Android version nào
```

Một app có thể:

```text
minSdk = 26
compileSdk = 37
targetSdk = 36
```

và đây là cấu hình hoàn toàn có nghĩa.

---

## 2. Timeline tổng quan Kotlin

Bảng dưới không cố liệt kê mọi bug-fix release. Nó tập trung vào những release làm thay đổi cách đọc hoặc viết code.

| Thế hệ | Thời gian | Ý nghĩa chính |
|---|---:|---|
| Kotlin 1.0 | 2016 | Ngôn ngữ JVM stable; nền móng Kotlin hiện đại |
| Kotlin 1.1 | 2017 | Coroutine xuất hiện ở experimental stage; ecosystem Android tăng mạnh |
| Kotlin 1.2 | 2017 | Multiplatform bắt đầu hình thành rõ hơn |
| Kotlin 1.3 | 2018 | Coroutine trở thành language feature stable; multiplatform/tooling trưởng thành hơn |
| Kotlin 1.4 | 2020 | Compiler/type inference/build backend bắt đầu chuyển thế hệ |
| Kotlin 1.5 | 2021 | JVM IR backend mặc định, sealed interface, value class, JVM record support |
| Kotlin 1.6 | 2021 | `when` exhaustiveness và coroutine-related language semantics được siết chặt |
| Kotlin 1.7 | 2022 | K2 Alpha, builder inference và definitely-non-null types stable |
| Kotlin 1.8 | 2022–2023 | JVM baseline cũ được dọn dẹp; stdlib JVM target chuyển hẳn sang 1.8 |
| Kotlin 1.9 | 2023–2024 | K2 Beta, `data object`, enum `entries`, KMP stable ở 1.9.20 |
| Kotlin 2.0 | 2024 | K2 compiler Stable; Compose compiler chuyển vào Kotlin repository |
| Kotlin 2.1 | 2024–2025 | K2 ecosystem/tooling trưởng thành; preview nhiều language feature mới |
| Kotlin 2.2 | 2025 | Nhiều feature mới stable; migration Gradle DSL mạnh hơn sang `compilerOptions` |
| Kotlin 2.3 | 2025–2026 | Tiếp tục stabilize language; explicit backing field xuất hiện experimental |
| Kotlin 2.4 | 2026 | Context parameters và explicit backing fields stable; Java 26 support và toolchain mới |

---

# 3. Kotlin 1.0 — nền tảng stable đầu tiên

Kotlin/JVM 1.0 đặt nền móng cho phần lớn syntax người dùng vẫn thấy ngày nay:

```kotlin
val
var
fun
class
object
data class
when
extension function
nullable type T?
?.
?:
```

Một điểm đáng chú ý của Kotlin là phần lớn syntax nền tảng này không bị thay đổi triệt để khi lên 2.x. Kotlin tiến hóa theo hướng compatibility tương đối mạnh thay vì liên tục viết lại language core.

Vì vậy project Kotlin rất cũ vẫn có thể trông “quen” với developer Kotlin hiện tại.

Điều thay đổi mạnh hơn qua các version thường nằm ở:

```text
compiler backend
inference
coroutine semantics
JVM interop
Gradle DSL
plugin architecture
multiplatform
Compose compiler
stdlib APIs
deprecation cycle
```

---

# 4. Kotlin 1.1–1.2 — coroutine experimental và multiplatform sơ khai

Kotlin 1.1 là thời kỳ coroutine bắt đầu xuất hiện nhưng chưa có ecosystem ổn định như hiện nay.

Nếu đọc code rất cũ, có thể gặp coroutine API hoặc experimental annotation khác xa code hiện đại.

Không nên copy nguyên tutorial Kotlin 1.1/1.2 về coroutine vào project hiện tại.

Mental model cần giữ là:

```text
language coroutine support
+
kotlinx.coroutines library
```

là hai layer khác nhau.

Compiler hiểu `suspend`, state machine và coroutine language semantics; library cung cấp `CoroutineScope`, `Dispatchers`, `launch`, `async`, Flow và structured-concurrency abstractions.

---

# 5. Kotlin 1.3 — coroutine trở thành nền tảng thực tế

Kotlin 1.3 là một mốc lớn vì coroutine chuyển sang giai đoạn stable đủ để ecosystem sử dụng rộng rãi.

Từ đây Android gradually chuyển từ callback-heavy code:

```kotlin
api.load(object : Callback {
    override fun onSuccess(value: Data) { ... }
    override fun onError(error: Throwable) { ... }
})
```

sang suspend-style:

```kotlin
suspend fun load(): Data
```

và structured concurrency hiện đại.

Khi maintain project Kotlin đời 1.3, cần để ý:

- coroutine library version có thể rất cũ;
- Android Architecture Components khi đó thường dùng LiveData nhiều hơn Flow;
- XML/Fragment là UI architecture chính;
- Jetpack Compose chưa phải production UI stack.

---

# 6. Kotlin 1.4 — giai đoạn chuyển compiler backend

Kotlin 1.4 không chỉ thêm syntax. Đây là thời kỳ compiler architecture bắt đầu chuyển mạnh sang IR — Intermediate Representation.

IR giúp Kotlin có architecture compiler thống nhất hơn giữa JVM, JS, Native và về sau là nền tảng quan trọng cho compiler plugin như Compose.

Kotlin 1.4.30 đưa JVM IR backend lên Beta.

Đây là ví dụ quan trọng cho cách đọc version history:

```text
user-visible syntax chỉ thay đổi ít
nhưng generated bytecode/compiler plugin behavior có thể thay đổi lớn
```

Vì vậy migration Kotlin không chỉ cần compile source code; với project có serialization/reflection/compiler plugin/R8 cần test runtime behavior.

---

# 7. Kotlin 1.5 — JVM IR mặc định và modern type modeling

Kotlin 1.5 là một release rất quan trọng đối với Android/JVM.

## 7.1 JVM IR backend trở thành mặc định

Trước 1.5, JVM compiler dùng backend cũ theo default.

Từ Kotlin 1.5, IR backend trở thành stable/default.

Điều này ảnh hưởng tới:

- bytecode shape;
- field ordering;
- compiler plugin integration;
- incremental build;
- reflection/serialization edge case;
- R8/proguard behavior trong một số project legacy.

---

## 7.2 Sealed interface

Modern Kotlin có thể viết:

```kotlin
sealed interface UiState

data object Loading : UiState

data class Content(val items: List<Item>) : UiState

data class Error(val message: String) : UiState
```

`sealed interface` stable từ Kotlin 1.5.

Project cũ có thể dùng `sealed class` ở những nơi hiện nay interface phù hợp hơn.

---

## 7.3 Value class

```kotlin
@JvmInline
value class UserId(val value: String)
```

Value class cho phép tạo strong domain type mà nhiều trường hợp không cần allocation wrapper thông thường.

Code rất cũ có thể gọi chúng là **inline class**.

Mental migration:

```text
inline class   → legacy naming
value class    → modern naming
```

---

## 7.4 JVM records

Kotlin 1.5 bổ sung interop với Java record:

```kotlin
@JvmRecord
data class Point(val x: Int, val y: Int)
```

Điều này quan trọng khi Kotlin library phải expose model cho Java ecosystem.

---

# 8. Kotlin 1.6 — exhaustive `when` và stricter correctness

Kotlin 1.6 bắt đầu siết nhiều semantic rule mà code cũ từng được phép bỏ qua.

Ví dụ với sealed hierarchy:

```kotlin
sealed interface Result

data object Success : Result
data object Failure : Result
```

Modern code nên viết exhaustive `when`:

```kotlin
when (result) {
    Success -> showSuccess()
    Failure -> showFailure()
}
```

Compiler dần chuyển những trường hợp non-exhaustive từ warning sang error qua release cycle.

Đây là pattern thường gặp trong Kotlin evolution:

```text
allow
→ warning
→ stronger warning/progressive error
→ compile error
```

Do đó khi upgrade nhiều version một lúc, warnings của version cũ không nên bị xem nhẹ.

---

# 9. Kotlin 1.7 — K2 xuất hiện

Kotlin 1.7.0 đưa K2 compiler ra Alpha cho JVM.

K2 không chỉ là “compiler nhanh hơn”. Mục tiêu lớn hơn là:

```text
một compiler frontend mới
→ architecture nhất quán hơn
→ type analysis tốt hơn
→ compiler-extension API tốt hơn
→ dễ phát triển language feature mới hơn
→ unify platform behavior tốt hơn
```

Tại 1.7, K2 chưa phù hợp cho production Android thông thường vì compiler plugin support còn hạn chế.

Cùng thời kỳ này, các feature như:

- builder inference;
- definitely non-null types;
- opt-in requirements

được stabilize.

Definitely non-null type đặc biệt quan trọng khi làm generic Java interop:

```kotlin
T & Any
```

Nó biểu diễn generic `T` nhưng bắt buộc non-null ở boundary cần thiết.

---

# 10. Kotlin 1.8 — bỏ legacy JVM baseline

Kotlin 1.8 là mốc dễ thấy khi maintain build cũ.

Standard library chuyển sang JVM target 1.8 và không còn giữ baseline JVM 1.6/1.7.

Các artifact riêng:

```text
kotlin-stdlib-jdk7
kotlin-stdlib-jdk8
```

không còn cần khai báo như trước vì functionality đã được nhập vào `kotlin-stdlib`.

Nếu thấy build cũ có:

```kotlin
implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8:...")
```

hãy hiểu đó thường là dấu hiệu project đến từ thế hệ cũ, không phải template nên tiếp tục copy.

---

# 11. Kotlin 1.9 — bridge giữa K1 và K2

Kotlin 1.9 là thế hệ cuối rất phổ biến trước Kotlin 2.x.

Nhiều production Android codebase hiện nay vẫn có lịch sử từ 1.9.

## 11.1 `Enum.entries`

Legacy:

```kotlin
Color.values()
```

Modern:

```kotlin
Color.entries
```

`entries` stable ở Kotlin 1.9 và tránh tạo array mới như `values()` trong nhiều trường hợp.

---

## 11.2 `data object`

Legacy sealed state thường viết:

```kotlin
object Loading : UiState
```

Modern Kotlin có thể dùng:

```kotlin
data object Loading : UiState
```

`data object` tạo behavior `toString`/`equals`/`hashCode` đối xứng hơn với `data class` trong sealed hierarchy.

---

## 11.3 Open-ended range

```kotlin
0..<size
```

trở thành syntax rõ ràng cho range loại trừ upper bound.

So với:

```kotlin
0 until size
```

cả hai đều có thể gặp trong codebase.

---

## 11.4 K2 Beta

K2 tiến từ Alpha sang Beta trong thế hệ 1.9.

Điều này báo hiệu Kotlin 2.0 sắp đổi compiler frontend mặc định.

---

## 11.5 Kotlin Multiplatform stable

Kotlin 1.9.20 là mốc quan trọng khi Kotlin Multiplatform được JetBrains công bố Stable.

Điều này không có nghĩa mọi target/library/interoperability feature KMP đều stable; cần phân biệt stability của **platform/product** với từng feature cụ thể.

---

# 12. Kotlin 2.0 — mốc chuyển thế hệ

Kotlin 2.0.0 phát hành ngày 2024-05-21 và đánh dấu K2 compiler Stable.

Đây là mốc lớn nhất kể từ Kotlin 1.0 nếu nhìn từ compiler architecture.

---

## 12.1 K2 trở thành compiler chính

K2 cải thiện:

- frontend architecture;
- analysis;
- type inference consistency;
- compiler performance;
- compiler-plugin foundation;
- multiplatform compiler consistency.

Nhưng migration 1.9 → 2.0 không nên được xem là chỉ đổi số version.

Cần test:

```text
source compatibility
compiler plugin compatibility
KSP/kapt
Compose compiler
serialization
generated code
R8/minification
binary compatibility của internal libraries
```

---

## 12.2 Compose compiler chuyển vào Kotlin repository

Đây là thay đổi cực kỳ quan trọng với Android.

### Trước Kotlin 2.0

Compose compiler có release/version mapping riêng với Kotlin compiler.

Developer phải kiểm tra compatibility map:

```text
Kotlin version
↔ Compose compiler extension version
```

Config cũ có thể trông như:

```kotlin
android {
    composeOptions {
        kotlinCompilerExtensionVersion = "..."
    }
}
```

### Từ Kotlin 2.0+

Compose compiler nằm cùng Kotlin repository và có Gradle plugin riêng:

```kotlin
plugins {
    id("org.jetbrains.kotlin.android") version "2.4.20"
    id("org.jetbrains.kotlin.plugin.compose") version "2.4.20"
}
```

Mental model mới:

```text
Kotlin 2.x
↔ Compose compiler plugin cùng Kotlin version
```

Jetpack Compose libraries vẫn có version/BOM riêng.

Do đó phải phân biệt:

```text
Compose compiler version
!=
Compose UI library version
```

---

# 13. Kotlin 2.1 — K2 ecosystem trưởng thành

Kotlin 2.1 tiếp tục hoàn thiện K2 và giới thiệu preview cho nhiều language feature mới.

Ví dụ:

- guard condition trong `when`;
- non-local `break`/`continue`;
- multi-dollar string interpolation.

Ví dụ guard condition:

```kotlin
when (user) {
    is User.Admin if user.enabled -> showAdmin()
    is User.Admin -> showDisabledAdmin()
    else -> showNormalUser()
}
```

Ở thời điểm 2.1 đây là preview; các feature sau đó được stabilize ở release sau.

Bài học quan trọng:

```text
thấy syntax trong blog release
không đồng nghĩa feature đã Stable
```

Luôn kiểm tra status:

```text
Experimental
Alpha
Beta
Preview
Stable
Deprecated
```

---

## 13.1 kapt và K2

Kotlin 2.1.20 đưa K2 implementation của kapt thành mặc định.

Tuy vậy với Android project hiện đại, nếu annotation processor hỗ trợ KSP thì thường nên đánh giá migration:

```text
kapt → KSP
```

Không phải vì kapt lập tức “không dùng được”, mà vì KSP thường tích hợp tốt hơn với Kotlin symbol model và build performance.

---

# 14. Kotlin 2.2 — modern compiler DSL và dọn legacy language levels

Kotlin 2.2 tiếp tục ổn định các feature từ 2.1.

Một số thay đổi đáng nhớ khi đọc Gradle script:

## 14.1 `kotlinOptions {}` chuyển sang `compilerOptions {}`

Legacy:

```kotlin
tasks.withType<KotlinCompile>().configureEach {
    kotlinOptions {
        jvmTarget = "17"
        freeCompilerArgs += "-X..."
    }
}
```

Modern:

```kotlin
kotlin {
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_17)
    }
}
```

Trong Kotlin 2.2, DSL `kotlinOptions {}` cũ đã bị nâng deprecation level mạnh và nên migrate sang `compilerOptions {}`.

---

## 14.2 Không giữ language level quá cũ vô hạn

Từ Kotlin 2.2, compiler không còn hỗ trợ `language-version=1.6` và `1.7`.

Điều này quan trọng cho enterprise codebase:

```text
compiler mới
không thể mãi đóng băng source ở language mode cực cũ
```

Upgrade strategy nên thường xuyên nâng từng bước thay vì nhảy 5–7 năm một lần.

---

# 15. Kotlin 2.3 — stabilization và explicit backing field

Kotlin 2.3 tiếp tục ổn định feature mới và giới thiệu **explicit backing field** ở trạng thái experimental.

Pattern cũ:

```kotlin
private val _state = MutableStateFlow<State>(State.Loading)
val state: StateFlow<State> = _state
```

Explicit backing field model:

```kotlin
val state: StateFlow<State>
    field = MutableStateFlow(State.Loading)
```

Trong private scope, compiler có thể hiểu backing field có implementation type cụ thể hơn.

Điểm quan trọng khi đọc version history:

```text
2.3 introduced/experimented
2.4 stabilized
```

không nên viết tài liệu như thể feature đã Stable ngay từ ngày đầu xuất hiện.

---

# 16. Kotlin 2.4 — baseline hiện tại của bộ note

Kotlin 2.4 là baseline chính của library tại thời điểm tháng 9/2026.

Stable release dùng trong tài liệu:

```text
Kotlin 2.4.20
```

Các điểm nổi bật của 2.4 generation:

- context parameters trở thành Stable;
- explicit backing fields trở thành Stable;
- annotation use-site target được cải thiện;
- Java 26 support trên Kotlin/JVM;
- compiler/tooling/Gradle integration tiếp tục hiện đại hóa;
- Kotlin/Native, JS, Wasm và build-tools API tiếp tục tiến hóa.

---

## 16.1 Context parameters

Context parameters giúp truyền dependency/context theo lexical context mà không buộc đưa mọi thứ thành parameter trực tiếp hoặc global singleton.

Ví dụ conceptual:

```kotlin
context(logger: Logger)
fun saveUser(user: User) {
    logger.info("saving ${user.id}")
}
```

Đây không phải lý do để thay toàn bộ constructor injection/Hilt.

Nên xem context parameters như một language mechanism mới cho những API phù hợp, đặc biệt DSL/library/domain context; lifecycle-heavy Android dependencies vẫn cần ownership rõ ràng.

---

## 16.2 Explicit backing field stable

Modern code có thể giảm boilerplate trong một số API dạng mutable-inside/read-only-outside.

Tuy nhiên đừng migrate mọi `_state` chỉ vì syntax mới tồn tại. Cần cân nhắc:

- readability của team;
- minimum Kotlin version của module/library consumer;
- Java interop;
- public API compatibility;
- mức quen thuộc của developer.

---

## 16.3 `when` compilation qua `invokedynamic`

Kotlin 2.4.20 ổn định thêm compiler optimization cho một số `when` trên JVM 21+ bằng `invokedynamic`.

Đây là ví dụ về feature version mà source code gần như không đổi nhưng generated bytecode/runtime strategy đổi.

Senior developer cần nhớ:

```text
same source
!=
same bytecode
```

đặc biệt khi profiling, reflection, instrumentation hoặc binary tooling tham gia.

---

# 17. K1 vs K2 — bảng so sánh mental model

| Khía cạnh | K1 compiler | K2 compiler |
|---|---|---|
| Thế hệ | Kotlin 1.x truyền thống | Compiler frontend thế hệ mới |
| Production mặc định | Trước Kotlin 2.0 | Kotlin 2.0+ |
| Mục tiêu | Compiler architecture ban đầu | Unified/faster/extensible architecture |
| Analysis | Frontend cũ | FIR-based frontend |
| Language feature development | Chậm/phức tạp hơn | Thiết kế để tiến hóa dễ hơn |
| Compiler plugin ecosystem | Mature legacy ecosystem | Modern ecosystem đang là mặc định |
| Compose compiler | Tách release mapping | Tích hợp Kotlin repository từ 2.0 |
| kapt | K1 implementation truyền thống | K2 implementation được đưa thành default ở 2.1.20 |

Không nên nói K1 là “compiler sai” và K2 là “compiler đúng”. K1 là compiler đã vận hành Kotlin ecosystem nhiều năm; K2 là thế hệ kế tiếp nhằm giải quyết scale/evolution/tooling limitation.

---

# 18. Compose version evolution dành cho Android developer

Compose có ít nhất ba version concern khác nhau.

## 18.1 Compose compiler

```text
< Kotlin 2.0
Compose compiler có compatibility mapping riêng

>= Kotlin 2.0
Compose compiler plugin dùng cùng version với Kotlin
```

Modern:

```kotlin
plugins {
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.compose.compiler)
}
```

`libs.versions.toml`:

```toml
[versions]
kotlin = "2.4.20"

[plugins]
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
compose-compiler = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
```

---

## 18.2 Compose UI libraries

Compose UI runtime/foundation/material libraries không dùng Kotlin version number.

Nên quản lý qua BOM:

```kotlin
val composeBom = platform("androidx.compose:compose-bom:2026.09.00")
implementation(composeBom)
androidTestImplementation(composeBom)
```

Mental model:

```text
Kotlin 2.4.20
Compose compiler 2.4.20
Compose BOM 2026.09.00
```

ba con số này có thể đồng thời tồn tại và không mâu thuẫn.

---

## 18.3 Compose và `compileSdk`

Compose libraries mới dần yêu cầu Android API compile level mới hơn.

Ví dụ các thế hệ Compose mới có thể yêu cầu `compileSdk 37` và AGP 9+.

Do đó upgrade Compose đôi khi kéo theo:

```text
Compose libraries
→ compileSdk
→ AGP
→ Gradle/JDK
```

chứ không chỉ đổi BOM.

---

# 19. Android API version evolution — không gắn trực tiếp với Kotlin

Kotlin version và Android OS version độc lập.

Ví dụ Kotlin 2.4 có thể build app chạy trên Android API cũ nếu `minSdk` và library dependencies cho phép.

Một app Android modern cần reasoning trên ma trận:

```text
Kotlin/KGP version
× AGP version
× Gradle version
× JDK version
× compileSdk
× targetSdk
× minSdk
× Android OS thực tế
× Jetpack library versions
```

Vì vậy lỗi “sau khi update Kotlin app crash trên Android X” không thể kết luận nguyên nhân là Kotlin chỉ từ tên version; cần xác định chính xác trục nào đã đổi.

---

# 20. Legacy → Modern map

Bảng này rất hữu ích khi đọc code Android/Kotlin cũ.

| Legacy / thế hệ cũ | Modern direction | Ghi chú |
|---|---|---|
| Java-only Android | Kotlin-first Android | Java vẫn được support và interop quan trọng |
| Kotlin Android Extensions synthetic view | View Binding / Compose | Synthetic bị loại khỏi modern workflow |
| `findViewById` everywhere | View Binding / Compose | `findViewById` vẫn hợp lệ ở View code |
| XML-only UI | Compose + XML interop | XML không “sai”; nhiều app production vẫn dùng |
| `AsyncTask` | Coroutine / WorkManager tùy lifetime | `AsyncTask` deprecated |
| callback pyramid | `suspend`, Flow | Callback vẫn cần ở platform boundary |
| LiveData everywhere | StateFlow/Flow cho modern data/state | LiveData vẫn supported |
| SharedPreferences cho structured settings | DataStore | SharedPreferences chưa biến mất |
| `startActivityForResult` | Activity Result API | Modern lifecycle-aware contract |
| manual service cho durable deferred work | WorkManager | Service vẫn đúng với use case khác |
| RxJava-heavy Android | Coroutine/Flow phổ biến hơn | RxJava vẫn tồn tại trong legacy/large codebase |
| `kapt` everywhere | KSP khi processor hỗ trợ | kapt vẫn dùng được cho tool chưa migrate |
| `kotlinOptions {}` | `compilerOptions {}` | Modern KGP DSL |
| Compose compiler compatibility map | Kotlin Compose compiler plugin cùng version | Kotlin 2.0+ |
| K1 compiler | K2 compiler | K2 stable/default từ Kotlin 2.0 |
| `Color.values()` | `Color.entries` | `values()` vẫn tồn tại |
| `object Loading` trong sealed state | `data object Loading` khi phù hợp | Không bắt buộc đổi mọi object |
| backing property `_state` + public `state` | explicit backing field có thể dùng | Stable từ 2.4, không phải migration bắt buộc |

---

# 21. Code cũ không đồng nghĩa code sai

Đây là nguyên tắc quan trọng nhất khi học version.

Ví dụ:

```kotlin
LiveData
Fragment
RecyclerView
View Binding
SharedPreferences
RxJava
kapt
XML layout
```

không tự động trở thành anti-pattern chỉ vì có API mới hơn.

Cần phân loại thành bốn nhóm:

```text
1. Deprecated và nên migrate
2. Supported nhưng có replacement hiện đại hơn
3. Vẫn là API phù hợp cho use case cụ thể
4. Historical API chỉ cần biết để đọc legacy code
```

Senior engineer không rewrite code chỉ vì version number mới hơn. Migration cần mua được giá trị cụ thể như:

- giảm bug;
- tăng maintainability;
- giảm build time;
- support platform requirement mới;
- security/compliance;
- performance;
- loại dependency deprecated;
- đơn giản hóa architecture.

---

# 22. Upgrade Kotlin: không nhảy version một cách mù quáng

Một upgrade Kotlin production nên theo pipeline.

## Bước 1 — chụp baseline

Trước upgrade ghi lại:

```text
Kotlin/KGP
AGP
Gradle
JDK
Compose compiler
Compose BOM
KSP/kapt processors
serialization plugin
Room/Hilt compiler
compileSdk
targetSdk
minSdk
```

Nếu không có baseline, khi build hỏng sẽ không biết dependency axis nào đã thay đổi.

---

## Bước 2 — đọc compatibility/release notes

Không chỉ đọc “What's New”.

Cần đọc cả:

```text
breaking changes
deprecations
compatibility guide
Gradle support
AGP support
compiler plugin support
JVM target changes
```

---

## Bước 3 — upgrade compiler/toolchain trước khi đổi source style

Tránh cùng một PR vừa:

```text
upgrade Kotlin
+ migrate Compose
+ đổi architecture
+ refactor package
+ đổi targetSdk
```

Nếu lỗi xảy ra, quá nhiều biến thay đổi đồng thời.

Tách migration theo axis giúp forensic debugging dễ hơn.

---

## Bước 4 — compile tất cả variants

Không chỉ compile `debug`.

Cần đặc biệt test:

```text
release
minified release
product flavors
benchmark/profile variants
instrumented tests
consumer sample nếu là library
```

Rất nhiều R8/compiler plugin issue chỉ xuất hiện ở release.

---

## Bước 5 — test generated-code boundary

Kiểm tra:

- Room;
- Hilt/Dagger;
- KSP;
- kapt;
- kotlinx.serialization;
- Compose compiler;
- Parcelize;
- custom compiler plugins.

Compiler upgrade có thể làm lỗi xuất hiện ở generated code trước khi handwritten source có vấn đề.

---

## Bước 6 — test binary compatibility nếu publish library

Library author phải quan tâm:

```text
source compatibility
binary compatibility
behavioral compatibility
```

App nội bộ compile lại toàn bộ source có thể không thấy lỗi mà binary consumer cũ sẽ gặp.

---

# 23. Upgrade `targetSdk` là migration khác với upgrade Kotlin

Không nên gộp hai việc này trong mental model.

```text
Upgrade Kotlin
= language/compiler/toolchain migration

Upgrade targetSdk
= Android platform behavior-contract migration
```

Nếu cùng release train phải thực hiện cả hai, nên tách commit/test matrix rõ ràng.

Ví dụ target SDK mới có thể thay đổi:

- permission behavior;
- background execution;
- foreground service policy;
- notification;
- storage;
- implicit intent/exported behavior;
- local network access;
- edge-to-edge/window behavior.

Không có liên hệ trực tiếp với việc K2 compile source như thế nào.

---

# 24. Version Catalog — nơi quản lý version modern Android project

Một project hiện đại thường centralize version trong `libs.versions.toml`.

Ví dụ:

```toml
[versions]
kotlin = "2.4.20"
agp = "9.4.1"
compose-bom = "2026.09.00"

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
compose-compiler = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
```

Ưu điểm không chỉ là “đỡ viết lặp”. Nó tạo một điểm review rõ ràng cho toolchain version.

Tuy nhiên Version Catalog không tự giải quyết compatibility. Nó chỉ centralize declaration.

---

# 25. Version compatibility không nên đoán từ số lớn/nhỏ

Ví dụ sai:

```text
Kotlin 2.4 nên AGP cũng phải 2.4
```

Hoặc:

```text
Compose BOM 2026.09 phải dùng Kotlin 2026.09
```

Các project có nhiều independent release train.

Luôn kiểm tra official compatibility/documentation của từng boundary:

```text
Kotlin ↔ Gradle
Kotlin ↔ compiler plugins
AGP ↔ Gradle
AGP ↔ JDK
AGP ↔ compileSdk
Compose libraries ↔ compileSdk
KSP ↔ Kotlin
```

---

# 26. Progressive mode

Kotlin hỗ trợ progressive mode để áp dụng một số language fix/deprecation behavior sớm hơn.

Concept:

```text
normal mode
= ưu tiên migration compatibility

progressive mode
= opt-in sớm vào correction/change mới
```

Library/application team có thể dùng progressive mode để phát hiện technical debt sớm hơn, nhưng cần test compiler/plugin compatibility.

Không bật chỉ vì “modern hơn”. Nó là policy decision của codebase.

---

# 27. Experimental API và opt-in

Kotlin ecosystem dùng opt-in khá nhiều.

Ví dụ concept:

```kotlin
@OptIn(ExperimentalStdlibApi::class)
fun useExperimentalFeature() {
    // ...
}
```

Version migration phải inventory experimental API vì chúng có compatibility guarantee thấp hơn Stable API.

Nếu project dùng nhiều:

```text
-X...
experimental annotations
internal compiler flag
unstable plugin API
```

thì upgrade risk cao hơn project chỉ dùng stable surface.

---

# 28. Version strategy cho Android application

Application có lợi thế là thường compile toàn bộ code cùng một toolchain.

Recommended strategy:

```text
1. Theo dõi stable Kotlin line
2. Không trì hoãn nhiều major generations
3. Upgrade compiler plugins cùng compatibility window
4. Giữ AGP/Gradle/JDK trong supported matrix
5. Compile release/minified variant trong CI
6. Tách Kotlin upgrade khỏi targetSdk migration khi có thể
7. Benchmark nếu compiler/generated-code/runtime behavior thay đổi đáng kể
```

Không cần chạy version mới trong ngày đầu release nếu product risk cao. Nhưng cũng không nên ở lại release line quá cũ tới khi cả compiler, AGP và dependencies cùng hết support.

---

# 29. Version strategy cho Android/Kotlin library

Library cần conservative hơn application vì consumer có thể dùng toolchain khác.

Cần quyết định rõ:

```text
minimum Kotlin consumer version
minimum Android API
minimum/expected compileSdk
JVM target
binary compatibility policy
SemVer policy
experimental API policy
```

Một library nâng language/API version có thể vô tình loại consumer cũ dù public API nhìn không thay đổi.

Do đó trước publish nên test matrix ít nhất:

```text
old supported consumer
current consumer
minified consumer
Java consumer nếu public API hỗ trợ Java
```

---

# 30. Current baseline — September 2026

Snapshot dùng để đọc repository này:

| Thành phần | Baseline |
|---|---|
| Kotlin | `2.4.20` |
| Kotlin compiler generation | K2 |
| Compose compiler | Kotlin Compose compiler plugin cùng Kotlin version |
| Compose BOM | `2026.09.00` |
| Android Studio | Quail 4 / `2026.1.4 Patch 1` |
| Android Gradle Plugin | `9.4.1` |
| Android platform reference | Android 17 / API 37 |
| Google Play ordinary app target requirement | API 36+ từ 2026-08-31 |

Đây là **documentation snapshot**, không phải hardcoded architecture rule.

---

# 31. Checklist khi gặp một project Kotlin/Android lạ

Trước khi đọc code sâu, hãy xác định version fingerprint.

### Build system

```text
Gradle wrapper version?
AGP version?
KGP/Kotlin version?
JDK/toolchain?
Groovy DSL hay Kotlin DSL?
Version Catalog có không?
```

### Kotlin

```text
K1 hay K2 generation?
languageVersion/apiVersion?
jvmTarget?
kapt hay KSP?
Compose compiler setup kiểu cũ hay Kotlin 2.x plugin?
```

### Android

```text
minSdk?
compileSdk?
targetSdk?
View/XML hay Compose?
Fragment-heavy hay single-activity Compose?
```

### Architecture generation

```text
callbacks / AsyncTask?
RxJava?
LiveData?
coroutine/Flow?
Room?
DataStore?
WorkManager?
```

Chỉ cần fingerprint này đã giúp ước lượng project thuộc thế hệ nào và migration debt nằm ở đâu.

---

# 32. Cách đọc nhanh code theo generation

## Project rất cũ

Dấu hiệu:

```text
Java nhiều
Kotlin 1.3/1.4
XML + Fragment
synthetic view access
callback/RxJava
LiveData
SharedPreferences
kapt-heavy
old Gradle DSL
```

Không được rewrite ngay. Trước hết xác định test coverage và behavior contract.

---

## Project transitional

Dấu hiệu:

```text
Kotlin 1.8/1.9
Flow + LiveData cùng tồn tại
XML + Compose coexist
kapt + KSP coexist
ViewModel modern nhưng navigation cũ
```

Đây là trạng thái rất phổ biến ở production.

Migration nên incremental.

---

## Project modern

Dấu hiệu thường gặp:

```text
Kotlin 2.x / K2
compilerOptions DSL
Compose compiler plugin
Compose BOM
Flow/StateFlow
Room/DataStore
KSP nếu ecosystem hỗ trợ
Activity Result API
WorkManager
modern AGP/Gradle/JDK toolchain
```

Nhưng “modern stack” vẫn không bảo đảm architecture tốt. State ownership, lifetime, consistency, testing và release discipline vẫn quyết định chất lượng.

---

# 33. Version timeline nên được dùng như thế nào khi học

Không cần học thuộc ngày release.

Điều nên nhớ là **các mốc chuyển mental model**:

```text
1.3 → coroutine trở thành nền tảng practical
1.5 → JVM IR + sealed interface/value class
1.7 → K2 bắt đầu xuất hiện
1.8 → dọn JVM legacy baseline
1.9 → cầu nối cuối K1/K2, KMP stable
2.0 → K2 Stable + Compose compiler nhập vào Kotlin
2.1 → K2 ecosystem mở rộng
2.2 → compilerOptions DSL / dọn language levels cũ
2.3 → language stabilization mới
2.4 → context parameters + explicit backing fields Stable
```

Đối với Android:

```text
Java/XML era
→ Kotlin-first
→ Architecture Components
→ coroutine/Flow
→ Compose
→ K2 / Kotlin 2.x
→ modern build/distribution/runtime engineering
```

Version history có giá trị vì nó giải thích **vì sao codebase cũ có hình dạng hiện tại**, không phải để đánh giá code cũ bằng tiêu chuẩn hiện đại mà không xét bối cảnh.

---

# 34. Senior Notes — version là một dependency graph

Ở mức Senior/Master, đừng nhìn version thành một list:

```text
Kotlin 2.4.20
AGP 9.4.1
Gradle X
```

Hãy nhìn chúng thành dependency graph:

```text
JDK
 ↓
Gradle
 ↓
AGP ───── Android SDK / build tools
 ↓
Android variants → D8/R8 → APK/AAB

KGP ───── Kotlin compiler/K2
 ↓
Kotlin source
 ↓
compiler plugins: Compose / serialization / Parcelize / KSP-kapt ecosystem

Jetpack libraries ───── compileSdk requirements
 ↓
runtime behavior on Android OS
```

Một version change ở node trên có thể cascade xuống nhiều node khác.

Đó là lý do upgrade production cần:

```text
compatibility matrix
+ isolated change
+ full variant build
+ migration tests
+ performance evidence
+ rollout observability
```

chứ không phải chỉ sửa version string tới khi Gradle hết báo đỏ.

---

# 35. Nguồn chính thức nên kiểm tra khi update file này

Khi version thay đổi, ưu tiên các nguồn chính thức sau:

- Kotlin release process: `https://kotlinlang.org/docs/releases.html`
- Kotlin What's New: `https://kotlinlang.org/docs/whatsnew24.html` và các release tương ứng
- Kotlin compatibility guides: `https://kotlinlang.org/docs/compatibility-guides.html`
- Kotlin language features/proposals: `https://kotlinlang.org/docs/kotlin-language-features-and-proposals.html`
- Compose compiler migration: `https://kotlinlang.org/docs/compose-compiler-migration-guide.html`
- Android Compose compiler setup: `https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler`
- Android Gradle Plugin release notes và API support: Android Developers
- Android behavior changes theo OS/target SDK: Android Developers

Mỗi lần baseline trong README thay đổi, file version evolution này cũng nên được review để tránh tình trạng README nói toolchain mới nhưng migration guide vẫn dừng ở thế hệ cũ.
