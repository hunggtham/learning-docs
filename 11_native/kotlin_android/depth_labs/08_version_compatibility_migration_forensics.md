# Depth Lab 08 — Kotlin + Android Version Compatibility, Migration và Upgrade Forensics

File `05_kotlin_android_version_evolution.md` trả lời câu hỏi **Kotlin và Android đã tiến hóa như thế nào theo thời gian**. Depth Lab này đi thêm một tầng: **vì sao một thay đổi version có thể làm build, binary, generated code hoặc runtime behavior hỏng dù source code gần như không đổi**.

Mục tiêu không phải học thuộc compatibility matrix. Mục tiêu là nhìn một Android project như một **đồ thị contract theo version** và biết cách điều tra khi một node trong đồ thị thay đổi.

```text
Kotlin source
   ↓
Kotlin language/API level
   ↓
Kotlin compiler / K2
   ↓
compiler plugins + KSP/kapt
   ↓
JVM bytecode / Kotlin metadata / generated source
   ↓
D8 / R8 / Android packaging
   ↓
APK / AAB
   ↓
Android runtime + OS behavior
```

Song song với đó là build graph:

```text
JDK
 ↓
Gradle
 ↓
AGP ───────── Android SDK / build tools
 ↓
variants / resources / manifest / D8 / R8

KGP ───────── Kotlin compiler
 ↓
Kotlin source + compiler plugins
```

Khi upgrade, lỗi thường xuất hiện ở **boundary giữa hai node**, không nằm đơn giản trong một con số version.

---

## 1. Version không phải một con số — nó là tập hợp các contract

Một project có thể đồng thời có:

```text
Kotlin          2.4.20
languageVersion 2.4
apiVersion      2.1
jvmTarget       17
JDK toolchain   17
Gradle          9.x
AGP             9.4.x
compileSdk      37
targetSdk       36
minSdk          26
Compose BOM     2026.09.00
```

Không có mâu thuẫn ở đây. Mỗi con số trả lời một câu hỏi khác.

Nếu không phân biệt các contract này, developer thường debug theo kiểu:

```text
“Sau khi update Kotlin app lỗi → Kotlin có bug.”
```

Cách suy luận tốt hơn là:

```text
version nào đổi?
contract nào đổi?
artifact nào được sinh khác?
consumer/runtime nào quan sát artifact đó?
```

---

# 2. Release channel cũng là một phần của compatibility

Không phải version nào có số lớn hơn cũng có cùng mức guarantee.

Ta cần phân biệt:

```text
EAP / Early Access
Beta / Preview
RC / Release Candidate
Stable
Deprecated
Removed
```

Một project production dùng Stable surface có upgrade risk khác hoàn toàn một project phụ thuộc nhiều vào:

```text
-X compiler flags
experimental language feature
unstable compiler plugin API
preview Android behavior
alpha Jetpack library
internal annotation processor contract
```

Do đó trước upgrade cần inventory không chỉ version mà cả **stability level** của feature đang dùng.

Một codebase có thể ở Kotlin Stable nhưng vẫn có upgrade risk cao vì compiler plugin hoặc library đang Alpha.

---

# 3. Kotlin release version, `languageVersion` và `apiVersion` tạo ba contract khác nhau

Giả sử compiler là Kotlin 2.4 nhưng library muốn giữ consumer compatibility thấp hơn.

```kotlin
kotlin {
    compilerOptions {
        languageVersion.set(KotlinVersion.KOTLIN_2_4)
        apiVersion.set(KotlinVersion.KOTLIN_2_1)
    }
}
```

Mental model:

```text
compiler version
= compiler implementation đang chạy

languageVersion
= syntax/semantic language được phép dùng

apiVersion
= stdlib API tối đa source được phép gọi
```

`apiVersion` không được cao hơn `languageVersion`.

Điểm sâu hơn là: **giảm `apiVersion` không tự động biến mọi artifact thành tương thích với consumer cũ**.

Nó chỉ giúp tránh gọi stdlib API quá mới. Binary metadata, JVM target, compiler plugin output và dependency graph vẫn có thể yêu cầu toolchain mới hơn.

---

# 4. Kotlin metadata — compatibility layer thường bị bỏ qua

Kotlin/JVM artifact không chỉ chứa JVM bytecode. Kotlin compiler còn ghi **Kotlin metadata** để compiler khác hiểu những semantic mà bytecode Java thuần không diễn đạt đầy đủ.

Metadata có thể chứa thông tin về:

```text
nullability
property
extension
suspend function
inline/value class
sealed hierarchy
function default parameters
Kotlin-specific type information
```

Vì vậy một JAR/AAR có thể nhìn bằng JVM như “class hợp lệ”, nhưng Kotlin compiler consumer vẫn từ chối vì metadata version quá mới hoặc pre-release.

Đây là lý do lỗi kiểu:

```text
Module was compiled with an incompatible version of Kotlin
The binary version of its metadata is ...
Expected version is ...
```

không nên được xử lý bằng cách ngẫu nhiên thêm compiler flag cho qua.

Câu hỏi đúng là:

```text
producer dùng compiler nào?
consumer dùng compiler nào?
metadata version nào được producer ghi ra?
consumer compiler có support không?
```

---

## 4.1 Vì sao “bytecode chạy được” chưa đủ?

Java compiler có thể nhìn bytecode theo một contract khác Kotlin compiler.

Ví dụ library Kotlin public API sử dụng:

```kotlin
suspend fun load(): Result<User>
```

Bytecode JVM cuối cùng không giữ nguyên syntax `suspend` như source. Kotlin metadata giúp compiler consumer tái dựng Kotlin-level API.

Do đó compatibility Kotlin library phải xét ít nhất:

```text
JVM bytecode compatibility
+
Kotlin metadata compatibility
+
stdlib/API compatibility
```

---

# 5. Pre-release compiler artifact có rủi ro riêng

Một library build bằng compiler EAP/RC có thể tạo artifact mà stable consumer không đọc như artifact stable thông thường.

Vì vậy production library không nên publish artifact pre-release vào channel stable chỉ vì local app compile thành công.

Nên tách:

```text
internal experiment repository
pre-release coordinates
stable production coordinates
```

Nếu organization có nhiều app consumer, một artifact pre-release có thể làm cả dependency graph bị kéo sang toolchain thử nghiệm.

---

# 6. JVM target mismatch — lỗi version nhìn giống build config nhưng là artifact contract

Kotlin và Java cùng compile vào JVM bytecode nhưng có thể bị cấu hình target khác nhau.

Ví dụ:

```text
compileJava targetCompatibility = 17
compileKotlin jvmTarget = 1.8
```

Hoặc ngược lại.

Kotlin Gradle Plugin có validation giữa Kotlin `jvmTarget` và Java target. Với Gradle hiện đại, mismatch thường có thể làm build fail.

Mental model:

```text
JDK chạy Gradle
!= Java source level
!= Java target level
!= Kotlin jvmTarget
```

Dùng JDK 21 để chạy Gradle không có nghĩa output bytecode tự động phải target JVM 21.

---

## 6.1 Toolchain giúp gì?

Java/Kotlin toolchain giúp build reproducible hơn vì developer machine không tự quyết định compiler/runtime level.

Ví dụ:

```kotlin
kotlin {
    jvmToolchain(17)
}

kotlin {
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_17)
    }
}
```

Nhưng toolchain và `jvmTarget` vẫn không cùng một khái niệm.

```text
toolchain
= compiler/JDK environment

jvmTarget
= bytecode target contract
```

---

# 7. Android làm JVM compatibility phức tạp thêm một tầng

Android không chạy JVM desktop theo cách thông thường. Source Java/Kotlin đi qua pipeline:

```text
Java/Kotlin source
→ JVM class files
→ D8/R8
→ DEX
→ ART
```

Vì vậy một Java/Kotlin language feature có thể được dùng trên Android thấp hơn nhờ:

```text
desugaring
core library desugaring
Jetpack compatibility abstraction
```

Do đó không được suy luận đơn giản:

```text
“JVM 17 feature → Android device phải có Java 17 runtime.”
```

Android build toolchain có thể transform một phần feature trước khi artifact tới device.

---

# 8. Compiler plugin là nơi version upgrade dễ vỡ nhất

Compiler plugin chạy sâu trong compilation pipeline. Nó phụ thuộc compiler internals nhiều hơn library runtime thông thường.

Ví dụ ecosystem có thể gồm:

```text
Compose compiler
kotlinx.serialization plugin
Parcelize
all-open
no-arg
KSP
kapt
custom compiler plugin
```

Upgrade Kotlin nhưng giữ compiler plugin quá cũ có thể gây:

```text
compiler crash
unresolved generated symbol
IR lowering error
metadata mismatch
incremental compilation bug
release-only generated-code issue
```

Vì vậy migration Kotlin production phải xem compiler plugin như **lockstep boundary**, không phải dependency runtime bình thường.

---

# 9. Compose compiler: trước và sau Kotlin 2.0 là hai generation khác nhau

Trước Kotlin 2.0:

```text
Kotlin version
↕ compatibility map
Compose compiler version
```

Developer phải chọn Compose compiler tương thích với Kotlin compiler.

Từ Kotlin 2.0:

```text
Kotlin compiler
+
org.jetbrains.kotlin.plugin.compose
```

Compose compiler được phát hành cùng Kotlin và plugin dùng cùng version Kotlin.

Ví dụ:

```toml
[versions]
kotlin = "2.4.20"

[plugins]
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
compose-compiler = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
```

Điểm quan trọng:

```text
Compose compiler version
!= Compose UI library version
```

Compose UI libraries vẫn được quản lý theo release/BOM riêng.

---

## 9.1 BOM không “cài Compose” cho project

BOM chỉ quản lý tập version tương thích cho Compose libraries.

Ví dụ:

```kotlin
implementation(platform("androidx.compose:compose-bom:2026.09.00"))
implementation("androidx.compose.ui:ui")
implementation("androidx.compose.material3:material3")
```

BOM không tự thêm `ui`, `material3` hay compiler plugin.

Đây là một failure mode phổ biến khi developer hiểu BOM như dependency bundle thay vì **version alignment contract**.

---

## 9.2 Artifact build bằng Compose compiler cũ vẫn có thể ảnh hưởng app mới

Một app dùng compiler mới nhưng dependency được build bằng compiler version có bug vẫn có thể mang behavior bất lợi vào composition/runtime.

Đây là ví dụ quan trọng:

```text
application toolchain mới
không đồng nghĩa
mọi binary dependency đã được rebuild bằng toolchain mới
```

Khi điều tra recomposition bất thường, cần nhìn cả producer version của dependency chứ không chỉ app root build file.

---

# 10. KSP và kapt không chỉ là “hai cách generate code”

`kapt` làm việc qua Java annotation processing model. KSP làm việc trên Kotlin symbol model.

Khi nâng Kotlin version, generated-code ecosystem cần được kiểm tra theo processor:

```text
Room
Hilt/Dagger
Moshi
AutoService
Glide
custom processor
```

Không được migrate toàn bộ:

```text
kapt → KSP
```

chỉ vì KSP mới hơn. Processor phải thực sự hỗ trợ KSP và behavior generated code cần test lại.

---

## 10.1 Generated code là một API boundary

Nhiều team xem generated source như implementation detail. Điều này chỉ đúng một phần.

Nếu handwritten code compile dựa vào generated symbol, thì generator output chính là contract của build.

Upgrade compiler/processor có thể đổi:

```text
tên class generated
nullability annotation
visibility
constructor signature
incremental processing behavior
ordering
error diagnostic
```

Vì vậy test upgrade phải compile clean build, không chỉ incremental build từ cache cũ.

---

# 11. Clean build và incremental build có thể cho hai kết quả khác nhau

Incremental compilation giữ cache của compilation trước.

Một migration có thể “pass local” vì cache cũ che lỗi generated code hoặc stale artifact.

Do đó validation nên có cả:

```text
incremental developer build
+
clean CI build
+
release/minified build
```

Nếu chỉ chạy `assembleDebug` trên máy đã build nhiều lần, confidence rất thấp.

---

# 12. Source compatibility, binary compatibility và behavioral compatibility phải tách riêng

Giả sử library đổi:

```kotlin
fun load(id: String): User
```

thành:

```kotlin
fun load(id: String, refresh: Boolean = false): User
```

Source consumer compile lại có thể vẫn gọi:

```kotlin
load("42")
```

nhưng binary consumer cũ không nhất thiết tương thích như bạn nghĩ nếu bytecode/public ABI thay đổi.

Do đó library migration phải hỏi ba câu khác nhau:

```text
source cũ compile lại được không?
binary cũ chạy với library mới được không?
behavior cũ có còn đúng không?
```

---

# 13. Default parameter là source convenience nhưng có binary implication

Kotlin default parameter thường sinh synthetic helper như `$default` ở JVM level.

Thay đổi default value:

```kotlin
fun connect(timeoutMs: Long = 5_000)
```

thành:

```kotlin
fun connect(timeoutMs: Long = 10_000)
```

có thể không làm source API nhìn khác nhiều, nhưng behavior consumer sau recompile có thể đổi.

Đây là **behavioral compatibility change**.

Với public SDK, default value là một phần contract cần document và test.

---

# 14. `inline` làm implementation leak sang consumer artifact

Inline function đặc biệt vì body có thể được copy vào call site của consumer khi compile.

```kotlin
inline fun <reified T> decode(json: String): T = ...
```

Nếu implementation thay đổi trong library version mới, consumer binary cũ có thể vẫn chứa logic inline cũ cho tới khi recompile.

Mental model:

```text
non-inline library function
→ logic chủ yếu sống trong library binary

inline public function
→ một phần logic có thể sống trong consumer binary
```

Đây là lý do public inline API cần compatibility discipline cao hơn tưởng tượng.

---

# 15. `const val` cũng có thể bị inline vào consumer

Ví dụ:

```kotlin
const val API_VERSION = 3
```

Consumer compile có thể embed giá trị này.

Sau khi library đổi:

```kotlin
const val API_VERSION = 4
```

consumer binary cũ có thể vẫn dùng `3` cho tới khi recompile.

Vì vậy public constant thay đổi không phải lúc nào cũng giống đọc field runtime.

---

# 16. Value class và ABI evolution cần cẩn thận

Value class có representation/boxing rules phụ thuộc context.

Ví dụ:

```kotlin
@JvmInline
value class UserId(val raw: String)
```

Đổi underlying type:

```kotlin
String → Long
```

không phải refactor vô hại. Nó ảnh hưởng:

```text
mangled JVM signature
boxing
serialization
reflection
binary consumer
Java interop
```

Nếu type nằm trong public API, hãy coi underlying representation là compatibility concern.

---

# 17. Enum evolution không phải lúc nào cũng backward-safe

Thêm enum constant mới có thể làm code consumer cũ sai assumption.

Ví dụ consumer:

```kotlin
when (status) {
    Status.NEW -> ...
    Status.DONE -> ...
}
```

Nếu enum từ remote/server hoặc library evolve thêm constant, behavior runtime/deserialization có thể thay đổi.

Với wire format hoặc SDK contract, nên thiết kế unknown value strategy thay vì giả định enum đóng vĩnh viễn.

---

# 18. Sealed hierarchy cũng có compatibility semantics

Sealed type giúp exhaustive `when` trong cùng compilation context.

Nhưng library public sealed hierarchy evolve phức tạp hơn internal app hierarchy.

Thêm subtype mới có thể buộc source consumer recompile và xử lý branch mới.

Nếu ecosystem yêu cầu third-party extension hoặc open-ended evolution, sealed có thể không phải contract phù hợp.

Version design phải bắt đầu từ evolution requirement, không chỉ từ syntax tiện lợi.

---

# 19. Serialization schema là version contract độc lập với Kotlin version

Một project upgrade Kotlin có thể đồng thời upgrade serialization plugin/library.

Điều cần bảo vệ không chỉ là compile thành công mà là dữ liệu cũ vẫn đọc được.

Ví dụ persisted JSON/Proto/Room blob có thể sống qua nhiều app version.

Cần test:

```text
old writer → new reader
new writer → rollback old reader nếu rollback được hỗ trợ
unknown field
missing field
default value change
enum evolution
renamed field
```

Compiler upgrade không được che mất schema migration risk.

---

# 20. Android version axis: `minSdk`, `compileSdk`, `targetSdk` không thể gộp

```text
minSdk
= install/runtime floor

compileSdk
= API surface compiler nhìn thấy

targetSdk
= behavior contract app opt-in
```

Upgrade `compileSdk` có thể cần để dùng library mới mà chưa bắt buộc app đổi mọi runtime behavior.

Upgrade `targetSdk` mới là bước kích hoạt nhiều target-gated behavior changes.

Do đó migration an toàn thường tách:

```text
1. compileSdk/toolchain readiness
2. app chạy trên OS mới với target cũ
3. targetSdk migration
4. behavior regression test
```

---

# 21. `targetSdk` migration là semantic migration, không chỉ build migration

Tăng target có thể đổi behavior về:

```text
permission
foreground service
background execution
notification
storage
implicit intent
exported component
window/edge-to-edge
local network access
```

Build xanh không chứng minh app đã thích nghi đúng.

Đây là điểm khác với nhiều language upgrade: targetSdk thay đổi **runtime policy contract của OS**.

---

# 22. Android SDK Extensions làm “API availability” không còn chỉ là API level

Một số Android capability có thể được cập nhật qua modular system component.

Vì vậy future-proof code đôi khi cần xét:

```text
Build.VERSION.SDK_INT
+
SDK extension version
```

Mental model quan trọng:

```text
OS API level
không phải lúc nào cũng là toàn bộ platform capability version
```

Đây là lý do compatibility engineering cần đọc docs của API cụ thể thay vì chỉ so `SDK_INT` máy móc.

---

# 23. AGP upgrade kéo theo Gradle và JDK vì build toolchain là một graph

Một AGP release thường có supported range cho:

```text
Gradle
JDK
Android SDK/build tools
Android Studio
```

Do đó lỗi sau AGP upgrade thường không nằm trong Android source.

Ví dụ chain:

```text
muốn compileSdk mới
→ cần AGP mới
→ AGP mới cần Gradle mới
→ Gradle/AGP mới cần JDK mới
```

Nếu upgrade tất cả trong một commit khổng lồ, forensic rất khó.

---

# 24. Upgrade order nên theo dependency direction

Một chiến lược thực tế:

```text
1. xác nhận JDK/toolchain
2. nâng Gradle wrapper nếu cần
3. nâng AGP
4. xác nhận compileSdk/build tools
5. nâng Kotlin/KGP
6. nâng compiler plugins/KSP/kapt processors
7. nâng Compose compiler setup
8. nâng Compose/Jetpack runtime libraries
9. cuối cùng mới đổi source style/refactor
```

Thứ tự cụ thể có thể khác theo compatibility matrix, nhưng nguyên tắc là **không đổi nhiều independent axes hơn cần thiết trong cùng một bước**.

---

# 25. Version Catalog chỉ centralize version, không chứng minh compatibility

`libs.versions.toml` giúp nhìn graph dễ hơn:

```toml
[versions]
kotlin = "2.4.20"
agp = "9.4.1"
compose-bom = "2026.09.00"
```

Nhưng file đẹp không đảm bảo matrix hợp lệ.

Version Catalog không tự biết:

```text
AGP có support Gradle này không
KSP có support Kotlin này không
processor có support KSP2 không
Compose library có yêu cầu compileSdk cao hơn không
```

Nó là declaration layer, không phải compatibility solver hoàn chỉnh.

---

# 26. BOM cũng chỉ giải một phần dependency graph

BOM hữu ích để align family libraries.

Nhưng BOM thường không quản lý mọi dependency xung quanh family đó.

Ví dụ Compose BOM không quản lý:

```text
Kotlin compiler
AGP
Gradle
JDK
Room
Hilt
Retrofit
KSP
```

Do đó dependency governance cần nhiều lớp:

```text
Version Catalog
+BOM
+dependency constraints
+compatibility docs
+CI build/test matrix
```

---

# 27. Transitive dependency có thể âm thầm nâng floor của project

Một library upgrade có thể kéo transitive dependency mới yêu cầu:

```text
compileSdk cao hơn
minSdk cao hơn
newer Kotlin metadata
newer Java bytecode
newer desugaring support
```

Vì vậy khi dependency update làm build hỏng, đừng chỉ nhìn direct dependency declaration.

Cần inspect resolved graph.

Trong Gradle, tư duy đúng là:

```text
declared dependency
→ dependency constraints
→ variant selection
→ resolved graph
→ artifact thực tế
```

---

# 28. Dependency conflict không nên giải bằng “force latest” trước khi hiểu graph

Ép latest version có thể build được nhưng tạo runtime incompatibility.

Trước khi dùng force/resolutionStrategy, cần biết:

```text
ai yêu cầu version cũ?
ai yêu cầu version mới?
API/ABI có tương thích không?
variant nào được chọn?
consumer rule nào đi kèm artifact?
```

Một build hết warning không đồng nghĩa runtime graph đúng.

---

# 29. Migration scenario A — Kotlin 1.9 + Compose compiler cũ → Kotlin 2.x

Đây là migration rất phổ biến.

Legacy mental model:

```text
Kotlin 1.9.x
+
Compose compiler 1.5.x tương thích theo map
```

Modern mental model:

```text
Kotlin 2.x
+
org.jetbrains.kotlin.plugin.compose cùng Kotlin version
```

Checklist:

```text
1. nâng Kotlin/KGP
2. áp dụng Compose compiler Gradle plugin
3. bỏ config compiler extension cũ nếu không còn cần
4. kiểm tra compiler options mới
5. clean build toàn bộ modules
6. rebuild dependency nội bộ nếu cần
7. chạy Compose UI tests
8. benchmark recomposition/hot screen nếu app lớn
```

Không nên cùng lúc rewrite XML → Compose trong migration này. Hai việc độc lập.

---

# 30. Migration scenario B — `kotlinOptions {}` → `compilerOptions {}`

Legacy:

```kotlin
android {
    kotlinOptions {
        jvmTarget = "17"
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

Điểm cần kiểm tra không chỉ syntax DSL.

Trong multi-module project, option có thể được set ở nhiều level:

```text
extension level
target level
compilation task level
convention plugin
third-party Gradle plugin
```

Lower level có thể override higher level.

Khi migration xong mà behavior khác, inspect **effective compiler args**, không chỉ đọc root build script.

---

# 31. Migration scenario C — kapt → KSP

Một migration an toàn nên đi processor-by-processor.

Ví dụ:

```text
Room supports KSP → migrate Room first
custom processor chưa support → giữ kapt
```

Project có thể tạm thời dùng cả hai.

Điều cần đo:

```text
clean build time
incremental build time
generated source parity
error diagnostics
release/minified build
IDE indexing
```

Mục tiêu không phải “100% KSP” bằng mọi giá. Mục tiêu là giảm build cost mà không đổi behavior.

---

# 32. Migration scenario D — nâng targetSdk nhưng giữ Kotlin ổn định

Nếu product có risk cao, đây thường là chiến lược tốt:

```text
Kotlin/KGP giữ nguyên
AGP/compileSdk đủ mới
nâng targetSdk
fix platform behavior
run device matrix
release
```

Sau khi target migration ổn định mới thực hiện Kotlin/compiler upgrade riêng.

Tách release train giúp postmortem rõ hơn nếu crash tăng.

---

# 33. Migration scenario E — nâng Kotlin nhưng giữ targetSdk ổn định

Ngược lại:

```text
Kotlin/KGP
compiler plugins
KSP/kapt processors
Compose compiler setup
```

được nâng trong khi Android behavior contract giữ nguyên.

Khi regression xuất hiện, phạm vi nghi ngờ nhỏ hơn:

```text
compiler
generated code
bytecode
metadata
build plugin
```

thay vì permission/background-policy của OS.

---

# 34. Library upgrade strategy khác application upgrade strategy

Application thường compile lại toàn bộ source cùng một toolchain.

Library phải hỗ trợ consumer nằm ngoài quyền kiểm soát.

Do đó library cần explicit support matrix:

```text
minimum Kotlin version
minimum JVM target
minimum Android API
minimum compileSdk expectation
Java interoperability
binary compatibility policy
SemVer policy
```

Nếu không document, consumer sẽ tự suy luận từ build failure.

---

# 35. Public library không nên vô tình nâng Kotlin floor

Giả sử library build bằng compiler mới và dùng stdlib API mới trong public inline function.

Consumer dùng Kotlin cũ có thể gặp vấn đề dù public method name gần như không đổi.

Vì vậy library author cần test **old supported consumer project** thật, không chỉ test module trong mono-repo bằng cùng root toolchain.

---

# 36. Consumer matrix nên là executable test, không phải README text

Một SDK production có thể có fixture projects:

```text
consumer-old-kotlin/
consumer-current-kotlin/
consumer-java/
consumer-minified/
consumer-compose/
```

CI build các consumer này sau mỗi release candidate.

Như vậy support matrix trở thành testable contract.

---

# 37. R8/ProGuard làm version compatibility có thêm một chiều

Debug build có thể chạy, release minified build crash vì:

```text
reflection target bị rename
serializer metadata bị strip
JNI method/name lookup bị obfuscate
consumer keep rule thiếu
SDK update thay internal class graph
```

Vì vậy upgrade library/compiler plugin phải test release artifact thật.

Không được xem R8 là “bước cuối tối ưu size”. Nó là một transformation stage có thể làm lộ contract ẩn.

---

# 38. Native `.so` dependency có version contract riêng

Android app có NDK/native library cần xét:

```text
ABI
NDK level
C++ runtime
symbol visibility
page-size compatibility
native API level
JNI contract
```

Kotlin/AGP upgrade có thể kéo packaging behavior mới dù native source không đổi.

Do đó binary inventory nên bao gồm cả `.so`, không chỉ Maven dependencies.

---

# 39. Build cache có thể làm forensic sai nếu không kiểm soát

Một regression sau upgrade đôi khi chỉ xuất hiện ở clean environment.

Forensic sequence nên có:

```text
1. reproduce incremental build
2. clean local build
3. CI clean build
4. optionally disable/rebuild relevant cache
5. compare generated artifacts
```

Không nên xóa toàn bộ cache ngay từ đầu rồi mất bằng chứng về incremental-only bug.

---

# 40. Effective configuration quan trọng hơn declaration

Project lớn có thể set Kotlin/Android option qua:

```text
root plugin
convention plugin
module build script
buildSrc
included build
third-party Gradle plugin
CI property
```

Do đó file `build.gradle.kts` của module không nhất thiết phản ánh effective value cuối.

Khi debug hãy hỏi:

```text
compiler args thực tế là gì?
variant nào đang build?
resolved dependency nào thực tế được chọn?
manifest cuối cùng là gì?
R8 rules cuối cùng là gì?
```

---

# 41. Version forensic: bắt đầu từ artifact, không bắt đầu từ phỏng đoán

Giả sử release mới crash nhưng debug không crash.

Thay vì nói:

```text
“R8 chắc lỗi.”
```

hãy tạo evidence chain:

```text
release variant nào?
APK/AAB hash nào?
mapping file nào?
Kotlin/AGP version nào build artifact đó?
resolved dependency graph nào?
manifest merged ra sao?
class nào bị optimize/rename?
stacktrace đã deobfuscate chưa?
```

Forensic engineering nghĩa là truy từ artifact về configuration, không từ cảm giác về tool.

---

# 42. Lỗi metadata mismatch — playbook điều tra

Khi gặp lỗi Kotlin metadata incompatible:

```text
1. tìm dependency nào chứa artifact lỗi
2. xác định producer Kotlin version
3. xác định consumer compiler version
4. xem dependency direct hay transitive
5. kiểm tra artifact có pre-release không
6. nâng consumer compiler hoặc hạ dependency theo support matrix
7. không dùng skip metadata check như fix mặc định
```

Compiler flag bỏ check chỉ nên là diagnostic/temporary escape hatch khi hiểu rõ consequence.

---

# 43. Lỗi JVM target mismatch — playbook điều tra

```text
1. xem Java targetCompatibility
2. xem Kotlin jvmTarget effective
3. xem JDK/toolchain đang chạy
4. xem convention plugin có override không
5. align toolchain/targets
6. clean build
```

Đừng sửa bằng cách disable validation trước khi hiểu mismatch.

Validation đang bảo vệ artifact consistency.

---

# 44. Lỗi “works on debug, fails on release” sau upgrade

Suspect list theo thứ tự evidence:

```text
R8/keep rules
resource shrinking
BuildConfig/variant values
signing/configuration
reflection
serialization
JNI
consumer ProGuard rules
release-only dependency
optimization-sensitive race
```

Compiler upgrade có thể chỉ là trigger làm contract ẩn lộ ra, không nhất thiết là root cause.

---

# 45. Lỗi “works on one device, fails on another” sau target upgrade

Cần tách:

```text
OS API level
OEM
WebView version
Google Play system component
SDK extension
permission state
hardware capability
```

TargetSdk chỉ là một axis.

Device matrix phải được ghi vào reproduction report.

---

# 46. Lỗi “only CI fails” sau toolchain upgrade

Thường kiểm tra:

```text
CI JDK version
Gradle daemon/runtime
environment variable
network/cache
case-sensitive filesystem
path length
repository credentials
architecture x64/arm64
Gradle configuration cache
```

Nếu local dùng Android Studio bundled JDK nhưng CI dùng system JDK khác, cùng source không có nghĩa cùng build environment.

---

# 47. Lỗi “only local fails” sau upgrade

Suspect:

```text
old Gradle daemon
stale IDE cache
local.properties
custom JDK
Android SDK package thiếu
proxy/repository cache
old generated source
```

Nhưng không nên bắt đầu bằng “Invalidate Caches” như nghi thức.

Trước hết capture environment để biết sự khác nhau giữa local và CI.

---

# 48. Upgrade PR nên chứa một version fingerprint machine-readable

Ví dụ trong PR description hoặc artifact report:

```text
Before:
Kotlin 1.9.x
AGP 8.x
Gradle 8.x
JDK 17
Compose compiler 1.5.x
compileSdk 35
targetSdk 34

After:
Kotlin 2.4.20
AGP 9.4.x
Gradle 9.x
JDK 17/required toolchain
Compose plugin 2.4.20
compileSdk 37
targetSdk unchanged
```

Mục đích là giúp reviewer thấy **axis nào đổi và axis nào cố ý không đổi**.

---

# 49. CI gate cho version migration

Một upgrade production nên có gate tối thiểu:

```text
clean compile
unit tests
integration tests
release/minified assemble
instrumented smoke tests
consumer build nếu library
dependency vulnerability/license check nếu organization yêu cầu
baseline performance check nếu compiler/runtime-sensitive
```

Không phải project nào cũng cần matrix khổng lồ. Nhưng gate phải cover boundary có risk thật.

---

# 50. Performance regression sau compiler upgrade cần evidence

Compiler mới có thể thay:

```text
inlining
bytecode shape
allocation
Compose stability inference
generated code
R8 optimization opportunity
```

Nếu app performance-critical, so sánh:

```text
startup
frame time
allocation/memory
APK size
critical benchmark
```

Không kết luận tốt/xấu chỉ từ release note “compiler nhanh hơn”. Build performance và runtime performance là hai chuyện khác nhau.

---

# 51. Build performance cũng phải được đo clean và incremental riêng

```text
clean build
!= incremental build
!= configuration time
!= test execution time
```

Upgrade KGP/KSP/AGP có thể cải thiện một loại nhưng làm loại khác chậm hơn.

Benchmark build phải ghi rõ scenario.

---

# 52. Version support policy cần được viết ra trước khi khủng hoảng

Team nên quyết định:

```text
Kotlin release line được support bao lâu?
bao lâu review targetSdk?
bao lâu review AGP?
JDK baseline là gì?
alpha/beta dependency có được phép production không?
compiler flag experimental nào được phép?
```

Nếu không có policy, upgrade thường chỉ xảy ra khi Google Play deadline hoặc dependency bắt buộc team phải nhảy nhiều generation cùng lúc.

---

# 53. “Latest everything” không phải version strategy

Luôn latest có lợi ích:

```text
security fix
support window dài
API/tooling mới
ít migration debt tích lũy
```

Nhưng production còn có:

```text
plugin lag
regression risk
release train
certification/device testing
vendor SDK compatibility
```

Strategy tốt là **stay reasonably current inside supported windows**, không phải chạy theo version trong ngày đầu bằng mọi giá.

---

# 54. Version debt là technical debt có thể đo được

Có thể track:

```text
Kotlin major/minor lag
AGP lag
Gradle lag
targetSdk lag
unsupported dependencies
number of deprecated APIs
number of experimental compiler flags
number of kapt-only processors
```

Version debt lớn làm mỗi migration sau đắt hơn vì nhiều boundary đổi cùng lúc.

---

# 55. Risk score cho một upgrade

Một cách review định tính:

```text
Risk = Scope × Compatibility Distance × Runtime Exposure × Rollback Difficulty
```

Ví dụ:

```text
Kotlin patch release trong same line
→ compatibility distance thấp

Kotlin 1.9 → 2.4 + K1 → K2 + Compose compiler migration
→ compatibility distance cao

nâng targetSdk + background policy
→ runtime exposure cao

DB schema + targetSdk + compiler cùng release
→ rollback difficulty cao
```

Công thức không cần số tuyệt đối; nó ép team suy nghĩ về dimension thật của risk.

---

# 56. Rollback strategy phải xét backward compatibility của data

Nếu release mới migrate Room schema hoặc persisted data rồi rollback app binary, binary cũ có đọc data mới được không?

Version upgrade có thể nhìn là build concern nhưng rollback lại chạm storage contract.

Do đó release plan phải hỏi:

```text
app cũ đọc DB mới được không?
feature flag có disable behavior không?
server contract có backward-compatible không?
remote config có cứu được không?
```

---

# 57. Server/API version cũng tham gia mobile compatibility

Mobile app không update đồng thời với backend consumer khác.

Nếu app mới yêu cầu API mới ngay khi release, rollout chậm có thể tạo mixed-version population.

Cần design:

```text
old app + new server
new app + old-compatible server behavior
```

Version engineering mobile luôn có yếu tố distributed-system compatibility.

---

# 58. Feature flag là công cụ migration, không phải substitute cho compatibility

Feature flag có thể giảm blast radius của behavior mới.

Nhưng không cứu được:

```text
app không khởi động vì metadata mismatch
binary link error
manifest invalid
DB schema unreadable trước khi flag load
```

Flag chỉ hiệu quả sau khi app đủ healthy để đọc flag.

---

# 59. Release artifact phải trace được về toolchain

Một production APK/AAB nên trace được về:

```text
git commit
Kotlin/KGP
AGP
Gradle
JDK
compileSdk/targetSdk
resolved dependencies
mapping file
native symbols
build type/flavor
```

Khi crash xuất hiện, traceability rút ngắn forensic đáng kể.

---

# 60. Current baseline của bộ tài liệu

Tại snapshot tháng 9/2026:

```text
Kotlin: 2.4.20
K2: default compiler generation
Compose compiler: plugin cùng Kotlin version
Compose BOM: 2026.09.00
Android Studio: Quail 4 / 2026.1.4 Patch 1
AGP baseline: 9.4.1
Android platform reference: API 37
```

Kotlin 2.4 release line bắt đầu ngày 2026-06-03 và support window chính thức tới cuối năm 2027; 2.4.20 phát hành ngày 2026-09-07.

Snapshot này phải được review khi toolchain thay đổi.

---

# 61. Checklist forensic khi upgrade thất bại

Thay vì thử random version, đi theo thứ tự:

```text
1. Xác định symptom: configuration / compile / link / package / install / runtime.
2. Ghi version fingerprint before/after.
3. Xác định node nào thực sự đổi.
4. Xác định boundary nào quan sát change đó.
5. Reproduce bằng clean build.
6. Kiểm tra generated code/artifact nếu compile khác.
7. Kiểm tra resolved dependency graph.
8. Kiểm tra effective compiler/AGP options.
9. Kiểm tra release/minified variant.
10. Kiểm tra old/new consumer nếu là library.
11. Kiểm tra device/OS/target behavior nếu runtime-only.
12. Chỉ sau đó mới chọn upgrade/downgrade/workaround.
```

---

# 62. Checklist review version PR

Reviewer nên hỏi:

```text
Version nào đổi?
Tại sao phải đổi?
Support window cũ còn bao lâu?
Compatibility guide đã đọc chưa?
Compiler plugins nào bị ảnh hưởng?
Generated code nào bị ảnh hưởng?
JVM target/toolchain có align không?
Compose compiler setup có đúng generation không?
Dependency transitive floor có đổi không?
compileSdk/targetSdk có đổi cùng lúc không?
release/minified build đã test chưa?
consumer compatibility đã test chưa?
performance-critical path đã benchmark chưa?
rollback có an toàn không?
artifact có traceability không?
```

Nếu PR không trả lời được, upgrade vẫn đang ở mức “đổi version string”.

---

# 63. Mental model cuối cùng

Khi nhìn một version change, đừng hỏi đầu tiên:

```text
“Version mới có gì hay?”
```

Hãy hỏi:

```text
Producer nào thay đổi?
Artifact nào thay đổi?
Metadata/ABI/schema nào thay đổi?
Consumer nào phải hiểu artifact đó?
Runtime nào thực thi behavior đó?
Rollback path nào còn hợp lệ?
Evidence nào chứng minh migration thành công?
```

Version engineering tốt là khả năng giữ **source, binary, metadata, generated code, Android behavior, persisted data và release artifact** cùng tiến hóa mà không làm hệ thống mất khả năng build, chạy, rollback hoặc được debug.

Đó là điểm mà kiến thức version vượt khỏi “biết Kotlin 2.4 mới hơn Kotlin 1.9” và trở thành **compatibility engineering** thực sự.