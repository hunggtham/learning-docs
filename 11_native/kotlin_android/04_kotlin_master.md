# Kotlin + Android Master Note — Master / Production Engineering Supplement

> Mục tiêu: đưa người học từ mức Senior lên mức có thể reasoning về compiler, runtime, lifecycle, concurrency, API compatibility, production architecture, build/release và migration qua nhiều thế hệ Kotlin/Android. File này là canonical Master note; các `deep_dive/`, `production_casebook/` và `depth_labs/` chỉ mở rộng những boundary khó, không thay thế learning flow của file này.

## Mục lục

1. Version model: Kotlin 1.x → 2.x và Android toolchain
2. K2 compiler và language evolution
3. Kotlin/JVM bytecode awareness
4. Value classes và allocation model
5. Context parameters và feature maturity
6. Advanced generics và type erasure
7. Functional error modeling
8. Concurrency architecture
9. Locks, atomics và thread safety
10. Flow architecture ở hệ thống lớn
11. Compose architecture ở scale lớn
12. Design system
13. Adaptive UI, window size và foldables
14. Accessibility và internationalization
15. Startup architecture
16. Baseline Profiles và Macrobenchmark
17. Observability
18. Resilience engineering
19. Large-scale modularization
20. Convention plugins và build-logic
21. API/module compatibility
22. Library publishing
23. Kotlin Multiplatform awareness
24. Native/JNI interoperability awareness
25. Android platform boundaries
26. Privacy, security, compliance
27. Release engineering
28. Testing architecture cấp tổ chức
29. Technical debt và migration strategy
30. Master-level architectural heuristics
31. Kotlin/Android keyword & API index
32. Version matrix và cách đọc project Android hiện đại
33. Compiler plugin và generated code
34. Source/binary/behavioral compatibility
35. Architecture ở codebase lớn
36. Performance engineering
37. Reliability engineering
38. Security engineering
39. Release, rollout và rollback
40. Modern vs legacy Android
41. Production-ready checklist

---

# 1. Version model: Kotlin 1.x → Kotlin 2.x và Android toolchain

<!-- merge: preserve both canonical variants -->
Kotlin/Android không có một “version của project”. Một project production là giao điểm của nhiều version axis. Nếu chỉ nhìn `kotlin = "2.4.20"` rồi kết luận project mới hay cũ, ta bỏ qua phần lớn compatibility contract thực tế.

Bốn tầng version cần tách riêng trong đầu:

```text
Tầng 1 — Language/compiler
Kotlin release
languageVersion
apiVersion
K1/K2 compiler
compiler plugins

Tầng 2 — JVM/toolchain
JDK chạy Gradle
Java source/target compatibility
Kotlin jvmTarget
bytecode level

Tầng 3 — Android build/platform
Gradle
Android Gradle Plugin (AGP)
compileSdk
minSdk
targetSdk
D8/R8
APK/AAB packaging

Tầng 4 — Ecosystem
Compose compiler plugin
Compose BOM / Jetpack libraries
KSP/kapt processors
Room/Hilt/serialization/plugin versions
NDK/native dependencies
Google Play policy
```

Các tầng này liên quan nhưng không đồng nhất. `Kotlin 2.4.20`, `AGP 9.4.1`, `compileSdk 37`, `targetSdk 36` và `Compose BOM 2026.09.00` hoàn toàn có thể cùng tồn tại vì chúng mô tả các contract khác nhau.

## 1.1 Kotlin version không đồng nghĩa language version

Compiler mới có thể hỗ trợ source language level cũ trong một khoảng thời gian. Vì vậy cần phân biệt:

```text
Kotlin compiler version
= compiler/toolchain đang chạy

languageVersion
= syntax + language semantics source được phép dùng

apiVersion
= mức Kotlin standard-library API source được phép gọi
```

Đối với application, thường ba mức này đi khá gần nhau. Đối với library, chúng có thể được pin bảo thủ hơn để không vô tình nâng minimum consumer requirement.

Ví dụ mental model:

```kotlin
kotlin {
    compilerOptions {
        languageVersion.set(KotlinVersion.KOTLIN_2_4)
        apiVersion.set(KotlinVersion.KOTLIN_2_4)
        jvmTarget.set(JvmTarget.JVM_17)
<!-- merge: preserve both canonical variants -->
Kotlin có tính tương thích source khá tốt, vì vậy một project Kotlin 1.x cũ vẫn có thể trông quen thuộc khi đọc bằng Kotlin 2.x. Điều thay đổi mạnh qua thời gian thường không phải `val`, `fun`, class hay null-safety, mà là **compiler frontend/backend, coroutine ecosystem, generated code, compiler plugin, Gradle DSL, JVM target, Compose compiler và Android platform contract**. Đây là lý do chỉ nhìn `kotlinVersion` rồi kết luận project “cũ” hay “mới” là quá đơn giản.

Canonical mental model cần tách ít nhất các trục sau:

```text
Kotlin release / Kotlin compiler
languageVersion
apiVersion
Kotlin Gradle Plugin hoặc Kotlin support của AGP
compiler plugins: Compose / serialization / Parcelize / custom plugin
KSP / kapt processors
JDK chạy build
Java source/target compatibility
Kotlin jvmTarget
Gradle Wrapper
Android Gradle Plugin
minSdk
compileSdk
targetSdk
Android OS thực tế trên device
Jetpack/library versions
```

Các con số này liên quan nhau nhưng **không phải một version duy nhất**. `jvmTarget = 17` không có nghĩa `minSdk = 17`; `compileSdk = 37` không bắt app chỉ chạy Android 17; Kotlin `2.4.20` cũng không có nghĩa AGP phải có cùng số version.

## 1.1 Bản đồ evolution theo era

Thay vì học thuộc mọi release, hãy nhớ các giai đoạn làm thay đổi cách lập trình và cách đọc codebase.

### Era 1 — Kotlin 1.0 → 1.2: ngôn ngữ JVM ổn định, Android còn Java/XML-heavy

Kotlin 1.0 đặt nền cho syntax cốt lõi hiện vẫn dùng. Kotlin 1.1 bắt đầu coroutine ở trạng thái experimental; Kotlin Multiplatform còn sơ khai. Code Android thời kỳ này thường là XML + Activity/Fragment + callback, đôi khi có RxJava, và build script còn nhiều cấu hình Gradle/Android kiểu cũ.

Điều cần học khi đọc code era này không phải “rewrite ngay”, mà là nhận diện historical context: callback không tự động sai; XML/Fragment không tự động sai; rủi ro thật sự nằm ở API deprecated, lifecycle handling, thread ownership và platform behavior đã đổi.

### Era 2 — Kotlin 1.3 → 1.4: coroutine trở thành practical foundation

Từ Kotlin 1.3, coroutine trở thành nền tảng đủ ổn định để Android ecosystem chuyển dần từ callback/Rx-only sang `suspend`, structured concurrency và về sau là Flow. Kotlin 1.4 đồng thời mở đường cho compiler IR mới.

Mental shift của era này là:

```text
callback ownership thủ công
→ structured asynchronous work

compiler backend cũ
→ IR-oriented compiler architecture
```

### Era 3 — Kotlin 1.5 → 1.8: JVM IR mặc định và dọn baseline cũ

Kotlin 1.5 đưa JVM IR backend thành mặc định và làm các model như sealed interface/value class trở nên thực dụng hơn. 1.8 dọn các JVM baseline cũ. Đây là thời kỳ project Android bắt đầu có Flow, Room, WorkManager, ViewModel, nhưng XML/Fragment vẫn rất phổ biến và Compose mới dần trưởng thành.

Khi maintain era này, cần nhìn generated bytecode, kapt processors, R8 và Java interop cẩn thận vì source có thể không đổi nhiều nhưng compiler/backend đã thay đổi đáng kể.

### Era 4 — Kotlin 1.9: cầu nối cuối giữa K1 và K2

Kotlin 1.9 là thế hệ rất quan trọng với codebase enterprise vì nó vừa chứa nhiều syntax hiện đại (`data object`, enum `entries`, open-ended range) vừa là giai đoạn K2 tiến tới Beta. Nhiều project production đang migrate từ 1.9 lên 2.x, vì vậy đây là “legacy gần” chứ không phải historical code xa xưa.

### Era 5 — Kotlin 2.0: K2 Stable và Compose compiler nhập vào Kotlin

Kotlin 2.0 là mốc thay đổi compiler generation. K2 trở thành compiler frontend chính. Đồng thời Compose compiler được chuyển vào Kotlin repository và có Gradle plugin `org.jetbrains.kotlin.plugin.compose`, dùng cùng version Kotlin.

Trước Kotlin 2.0, project Compose có thể chứa:

```kotlin
android {
    composeOptions {
        kotlinCompilerExtensionVersion = "..."
<!-- end merged variant -->
    }
}
```

<!-- merge: preserve both canonical variants -->
`jvmTarget` lại là contract khác: nó mô tả bytecode JVM output, không phải Kotlin language feature set.

## 1.2 Kotlin 1.x → 2.x: thay đổi lớn nhất nằm ở compiler generation

Phần lớn syntax Kotlin nền tảng từ 1.x vẫn quen thuộc ở 2.x. Mốc lớn là Kotlin 2.0 khi K2 trở thành compiler frontend production mặc định. Do đó migration 1.x → 2.x thường không phải “rewrite Kotlin”, mà là kiểm tra những boundary phụ thuộc compiler:

```text
Kotlin source
→ type inference / diagnostics
→ compiler plugins
→ KSP/kapt processors
→ generated code
→ Kotlin metadata
→ JVM bytecode
→ D8/R8
→ APK/AAB
```

Source có thể không đổi nhưng build vẫn vỡ vì processor hoặc plugin chưa tương thích.

## 1.3 Compose compiler: dấu mốc trước và sau Kotlin 2.0

Project Compose cũ thường có Compose compiler version mapping riêng với Kotlin. Từ Kotlin 2.0+, Compose compiler được tích hợp vào Kotlin repository và modern setup dùng plugin `org.jetbrains.kotlin.plugin.compose` cùng version Kotlin.

Điều này không có nghĩa Compose UI libraries dùng cùng version Kotlin. Phải tách:

```text
Kotlin / Compose compiler plugin
!=
Compose UI runtime/foundation/material versions
```

Compose BOM alignment chỉ quản lý nhóm Compose libraries; BOM không thay thế compatibility của Kotlin, AGP, JDK hay compileSdk.

## 1.4 Android version có bốn câu hỏi khác nhau

```text
minSdk
= Android thấp nhất app hỗ trợ runtime

compileSdk
= Android API surface dùng để compile

targetSdk
= behavior contract mới mà app tuyên bố đã thích nghi

Device OS
= platform thật đang chạy app
```

Một app có thể compile với API 37, target 36 và vẫn chạy trên API 26 nếu dependencies và code path cho phép. `targetSdk` mới đặc biệt nguy hiểm nếu bị xem như “chỉ đổi một số”: nó có thể bật behavior change về permission, background execution, foreground service, storage, window/edge-to-edge, notification hoặc networking.

## 1.5 Upgrade là dependency graph, không phải sửa version string

Một chuỗi upgrade có thể là:

```text
Compose/Jetpack mới
→ cần compileSdk mới
→ cần AGP mới
→ AGP cần Gradle/JDK mới
→ Kotlin plugin/processor cần version tương thích
→ release variant cần R8 rules mới
```

Vì vậy production upgrade nên theo thứ tự có kiểm soát:

```text
1. chụp baseline version fingerprint
2. đọc release notes + compatibility guide
3. đổi một axis hoặc một nhóm tightly-coupled axis
4. clean build tất cả variants
5. chạy unit/integration/instrumented tests
6. build release + minified artifact
7. benchmark nếu compiler/runtime path đổi đáng kể
8. rollout có telemetry và rollback plan
```

Không nên cùng một PR nâng Kotlin, AGP, targetSdk, Compose, đổi architecture và migrate database nếu không có lý do bắt buộc.

## 1.6 Cách đọc project theo generation

Một project có Kotlin 2.x nhưng vẫn XML/Fragment/RxJava có thể là codebase modern toolchain nhưng legacy UI/reactive stack. Một project Kotlin 1.9 có architecture sạch và test tốt vẫn có thể production-quality. Version chỉ giúp xác định **migration context**, không tự động đánh giá chất lượng kiến trúc.

Khi mở project lạ, hãy fingerprint:

```text
Gradle wrapper
AGP
Kotlin/KGP
JDK
languageVersion/apiVersion/jvmTarget
KSP hay kapt
Compose compiler setup
minSdk/compileSdk/targetSdk
UI stack: XML/View hay Compose
state stack: LiveData/RxJava hay Flow/StateFlow
background work: Service/Alarm/WorkManager
storage: SharedPreferences/DataStore/Room
```

Sau đó mới quyết định phần nào thật sự cần migrate.

# 2. K2 compiler và language evolution

K2 không phải “Kotlin 2 syntax”. Đây là compiler frontend thế hệ mới dựa trên FIR (Front-end Intermediate Representation), được thiết kế để unify analysis, cải thiện compiler/IDE architecture và làm language evolution bền vững hơn.

Một migration sang K2 cần quan tâm ba lớp:

```text
Source semantics
Compiler diagnostics/inference
Plugin/generated-code ecosystem
```

Một số source từng compile nhờ corner-case inference ở K1 có thể bị diagnostics khác ở K2. Đây không nhất thiết là regression; đôi khi compiler mới siết behavior vốn ambiguous. Vì vậy khi migration cần phân biệt:

```text
source bug bị compiler mới phát hiện
vs
compiler/plugin incompatibility
vs
behavioral regression của application
```

## 2.1 Feature maturity quan trọng hơn “feature xuất hiện ở version nào”

Language feature thường đi qua:

```text
Experimental / Preview
→ Beta
→ Stable
→ Deprecated
→ Error/Removal
```

Không nên thấy feature trong release blog rồi đưa ngay vào public API. Với library/public SDK, maturity level là compatibility contract. Experimental feature có thể đổi syntax, metadata hoặc generated representation ở release sau.

## 2.2 Context parameters và explicit backing fields

Ở line 2.4, context parameters và explicit backing fields đã tiến tới Stable. Điều này làm source expressiveness mạnh hơn nhưng không tạo nghĩa vụ migrate toàn bộ code cũ.

Ví dụ context parameter:

```kotlin
context(logger: Logger)
fun save(user: User) {
    logger.info("save ${user.id}")
}
```

Đây không tự động thay constructor injection/Hilt. Android dependency thường mang lifecycle, scope và disposal semantics; lexical context không giải quyết ownership đó.

Explicit backing field có thể giảm boilerplate của mutable-inside/read-only-outside, nhưng `_state` + public `StateFlow` vẫn dễ hiểu và tương thích rộng. Chọn syntax mới khi nó cải thiện API/readability thật, không phải vì version mới tồn tại.

## 2.3 Compiler options là một phần của source contract

Modern Kotlin Gradle DSL ưu tiên `compilerOptions {}` thay `kotlinOptions {}` cũ. Compiler flags, progressive mode và opt-in API cần được xem như codebase policy. Một `-X...` flag experimental đặt ở root build có thể ảnh hưởng hàng chục module và làm migration khó hơn nhiều năm sau.

Nguyên tắc Master-level:

```text
stable feature mặc định
experimental feature phải có owner + lý do + exit strategy
compiler flag phải được document
public API không nên vô tình phụ thuộc unstable behavior
```
<!-- merge: preserve both canonical variants -->
và phải đối chiếu compatibility map giữa Kotlin và Compose compiler.

Từ Kotlin 2.x, mental model hiện đại là:

```text
Kotlin version
↕ cùng release train
Compose compiler plugin version

Compose UI libraries/BOM
= release train khác
```

Không được nhầm Compose compiler với Compose UI BOM.

### Era 6 — Kotlin 2.1 → 2.4: K2 ecosystem trở thành mặc định

Các release 2.1–2.4 không chỉ thêm syntax. Chúng dọn Gradle DSL cũ, mở rộng K2 plugin ecosystem, ổn định language feature mới và thay đổi generated-code/tooling behavior. `compilerOptions {}` là hướng hiện đại thay cho `kotlinOptions {}`; nhiều feature đi qua Experimental/Beta trước khi Stable nên project production phải quản lý opt-in thay vì copy syntax mới từ blog release.

Từ Kotlin 2.4 trở đi, K2 không còn là “mode mới có thể đơn giản quay về frontend cũ” như một số release chuyển tiếp trước đó. Vì vậy migration debt bị trì hoãn quá lâu sẽ khó xử lý hơn so với nâng đều theo release line.

File [`05_kotlin_android_version_evolution.md`](05_kotlin_android_version_evolution.md) chứa timeline chi tiết; Master note này giữ các mental shift bắt buộc phải hiểu ngay trong canonical learning path.

## 1.2 Android toolchain cũng có evolution riêng

Android không evolve theo version Kotlin. Một project hiện đại có thể dùng Kotlin mới nhưng vẫn support OS cũ, miễn `minSdk` và dependency cho phép.

Ba Android SDK axis quan trọng:

```text
minSdk
= OS thấp nhất app hỗ trợ

compileSdk
= API surface dùng lúc compile

targetSdk
= behavior contract Android mà app tuyên bố đã thích nghi
```

Do đó migration `targetSdk` là **platform behavior migration**, còn migration Kotlin là **language/compiler/toolchain migration**. Hai việc có thể xảy ra cùng quý nhưng nên tách reasoning, commit và test matrix nếu codebase lớn.

Tại baseline của bộ note này, Android Studio stable là Quail 4 / 2026.1.4 Patch 1 và patch này đi cùng AGP 9.4.1. Với AGP 9.x, Android build model cũng đã tiến thêm một bước quan trọng: Kotlin support được tích hợp sâu hơn vào AGP, nên project hiện đại có thể không còn cấu hình Kotlin Android plugin giống template cũ. Vì vậy khi đọc build script, **không được dùng việc có/không có một plugin ID làm bằng chứng duy nhất cho generation của project**.

Production team nên pin Gradle wrapper, toolchain và dependency version để build reproducible thay vì phụ thuộc IDE cá nhân.

## 1.3 Modern, transitional và legacy không phải nhãn chất lượng

Khi đọc code, phân loại API theo bốn trạng thái sẽ hữu ích hơn gọi chung là “cũ”:

```text
Historical
= cần biết để đọc project rất cũ; không dùng cho code mới

Deprecated
= compiler/platform đã chỉ hướng rời bỏ; cần migration plan

Supported legacy / coexistence
= vẫn hợp lệ, đặc biệt trong codebase đang chuyển đổi

Modern preferred
= hướng được ưu tiên cho code mới trong baseline hiện tại
```

Ví dụ XML, Fragment, RecyclerView, LiveData và RxJava có thể vẫn được support và phù hợp với codebase cụ thể. Ngược lại `AsyncTask` hoặc synthetic view access là ví dụ rõ hơn của API/workflow nên rời bỏ. Senior engineer không rewrite chỉ vì “có API mới”; phải chứng minh migration giảm risk, maintenance cost, build cost hoặc platform incompatibility.

## 1.4 Upgrade là compatibility graph, không phải sửa version string

Một upgrade Kotlin/Android nên đi qua các bước:

```text
1. Chụp baseline version graph
2. Đọc compatibility + breaking/deprecation notes
3. Thay một axis chính mỗi lần nếu có thể
4. Build mọi variant quan trọng, đặc biệt release/minified
5. Verify generated code và compiler plugin
6. Test migration/rollback/persisted data
7. Benchmark nếu compiler/runtime/build path thay đổi
8. Rollout có observability
```

Nếu build hỏng sau upgrade, hãy hỏi theo graph:

```text
source semantic thay đổi?
compiler/K2 thay đổi?
plugin/processor không tương thích?
JVM target lệch Java/Kotlin?
AGP/Gradle/JDK không nằm trong supported matrix?
R8 chỉ lỗi ở release?
targetSdk làm behavior runtime đổi?
transitive dependency kéo minimum requirement mới?
```

Đó là version engineering ở mức Master: tìm contract nào bị phá thay vì thử đổi số version ngẫu nhiên tới khi build xanh.

# 2. K2 compiler và language evolution

K2 không phải Kotlin “version ngôn ngữ mới” tách biệt; nó là compiler frontend thế hệ mới. Source Kotlin 2.x vẫn dựa trên phần lớn core syntax quen thuộc, nhưng cách compiler phân tích type, resolve symbol, expose extension point cho compiler plugin và báo lỗi đã được thiết kế lại.

## 2.1 Vì sao K2 tồn tại

K1 đã vận hành Kotlin ecosystem nhiều năm nhưng architecture frontend cũ làm việc phát triển language feature, IDE analysis và multiplatform consistency ngày càng tốn chi phí. K2 dựa trên FIR (Front-end Intermediate Representation) nhằm tạo một nền tảng thống nhất hơn cho compiler và tooling.

Mental model:

```text
K1
= frontend lịch sử đã rất mature

K2
= frontend mới để Kotlin tiếp tục scale về language/tooling/platform
```

Không nên diễn giải thành “K1 sai, K2 đúng”. Migration compiler generation luôn có compatibility edge case.

## 2.2 K2 có thể làm code cũ fail dù syntax nhìn hợp lệ

Compiler mới có thể siết semantic mà compiler cũ từng chấp nhận hoặc resolve khác ở edge case. Ví dụ nhóm thay đổi thường gặp gồm Java/Kotlin property resolution, nullability ở Java interop, generic accessibility, initialization rule và overload resolution.

Do đó migration 1.9 → 2.x không được xác nhận chỉ bằng việc `assembleDebug` thành công. Cần chạy:

```text
all source sets
unit tests
lint/static analysis
instrumented tests cần thiết
release/minified build
KSP/kapt generated code
serialization/Parcelize/Compose compiler path
```

## 2.3 Compiler plugin là một phần của compatibility contract

Android project hiện đại hiếm khi chỉ có Kotlin compiler thuần. Compose, serialization, Parcelize, all-open/no-arg ở một số stack, custom compiler plugin và symbol processor đều phụ thuộc compiler/tooling contract.

Từ Kotlin 2.0, Compose compiler đi cùng Kotlin release train, làm giảm một compatibility axis so với thời kỳ phải tra Kotlin ↔ Compose compiler map. Tuy nhiên Compose UI libraries vẫn có version riêng; KSP processor và các plugin khác vẫn cần compatibility riêng.

Nếu lỗi chỉ xuất hiện sau upgrade Kotlin mà handwritten source nhìn bình thường, kiểm tra plugin/generated-code boundary trước khi kết luận business logic hỏng.

## 2.4 `languageVersion` không đồng nghĩa compiler version

Compiler version xác định binary/toolchain đang chạy; `languageVersion` xác định language semantics được source opt vào; `apiVersion` giới hạn Kotlin standard-library API được phép gọi.

Ví dụ conceptual:

```kotlin
kotlin {
    compilerOptions {
        languageVersion.set(KotlinVersion.KOTLIN_2_4)
        apiVersion.set(KotlinVersion.KOTLIN_2_4)
    }
}
```

Đây là ba contract khác nhau. Compiler mới có thể hỗ trợ một số language level cũ trong migration window, nhưng support không tồn tại vô hạn. Không dùng `languageVersion` như chiến lược “đóng băng vĩnh viễn” để tránh xử lý technical debt.

## 2.5 `jvmTarget`, JDK và Android runtime cũng là ba lớp khác nhau

```text
JDK toolchain
= compiler/runtime Java dùng trong build

jvmTarget
= bytecode JVM level Kotlin/Java muốn sinh

Android Runtime / minSdk
= runtime platform thực tế trên device
```

Android toolchain có desugaring/D8 nên relationship không giống chạy JVM server trực tiếp. Dù vậy Java compile target và Kotlin `jvmTarget` lệch nhau vẫn có thể tạo compatibility validation/error trong build. Hãy cấu hình toolchain có chủ đích, không để IDE máy này và CI máy khác tự chọn JDK khác nhau.

## 2.6 Language evolution phải đọc theo stability lifecycle

Một feature thường đi qua:

```text
Experimental / preview
→ Beta
→ Stable
→ có thể deprecate sau nhiều release
```

Project production nên hỏi:

```text
feature có nằm trong public API không?
consumer minimum Kotlin version là gì?
opt-in có được isolate không?
rollback sẽ thế nào nếu syntax/ABI chưa ổn định?
team có thật sự mua được lợi ích gì?
```

Context parameters hay explicit backing fields là ví dụ feature mới đáng biết, nhưng không phải lý do để mass-refactor code chỉ vì compiler mới hỗ trợ.

## 2.7 K2 migration forensic checklist

Khi migration K1-era codebase sang K2, theo thứ tự:

```text
1. Inventory Kotlin/KGP + AGP/Gradle/JDK
2. Inventory compiler plugins, KSP/kapt processors, freeCompilerArgs
3. Đọc Kotlin compatibility/K2 migration notes cho version đích
4. Upgrade toolchain trước, giữ behavior refactor tối thiểu
5. Build clean + incremental để bắt cache/generated-code issue
6. Build release/minified, không chỉ debug
7. So sánh warnings/errors mới và sửa semantic issue có chủ đích
8. Chạy regression test ở Java interop/reflection/serialization boundary
9. Verify performance/build time nếu compiler change lớn
10. Chỉ sau khi baseline ổn mới áp dụng syntax/style mới
```

Tách **toolchain migration** khỏi **style modernization** giúp rollback và root-cause analysis rõ hơn nhiều.

Senior/master developer nên đọc changelog theo release line vì feature có thể bị gate bởi `languageVersion`/`apiVersion`, compiler plugin có compatibility window riêng và generated bytecode có thể đổi dù source nhìn giống nhau.
<!-- end merged variant -->

# 3. Kotlin/JVM bytecode awareness

Kotlin source có thể generate JVM representation khác điều source “trông như”. Default arguments tạo synthetic bridge/bitmask; suspend function thành continuation state machine; lambdas có thể dùng `invokedynamic` hoặc generated class tùy target/toolchain; companion/object có runtime representation; delegation và annotations tạo metadata/bridge code.

Không tối ưu bytecode bằng trực giác. Chỉ inspect khi profiler, binary size, Java interop hoặc compatibility issue đưa ra bằng chứng. Senior/Master workflow là source → generated bytecode/metadata → D8/R8 → runtime behavior, không dừng ở decompiled pseudo-Java.

Public `inline`, default parameter, `const val`, value class và JVM name cần đặc biệt thận trọng ở library vì implementation/signature có thể leak sang consumer binary.

# 4. Value classes và allocation model

`@JvmInline value class` tạo type safety mà có thể tránh wrapper allocation trong nhiều call path:

```kotlin
@JvmInline
value class UserId(val value: Long)
```

Nhưng “value class = zero allocation” là mental model sai. Boxing có thể xảy ra khi nullable, generic, interface, reflection hoặc Java boundary tham gia. Đối với public SDK, thay underlying representation hoặc signature còn là compatibility decision.

Dùng value class khi domain semantics mạnh hơn raw primitive và profiling không cho thấy downside đáng kể; không dùng chỉ như micro-optimization.

# 5. Context parameters và feature maturity

Master-level learning không yêu cầu thuộc mọi feature mới. Điều quan trọng là biết feature maturity, compiler requirement, Java interop và public-API implication.

Trước khi dùng feature ngôn ngữ mới trong code production, hỏi:

```text
feature Stable chưa?
minimum Kotlin version nào?
consumer/library có bị nâng floor không?
Java caller nhìn API ra sao?
KSP/compiler plugin/tooling đã hiểu chưa?
team có đọc/debug được không?
```

# 6. Advanced generics và type erasure

JVM generic chủ yếu bị type erasure. `List<String>` và `List<Int>` không giữ đầy đủ type parameter runtime như source thể hiện. `reified` giúp inline call site truy cập type trong một số trường hợp nhưng không “xóa” type erasure khỏi JVM.

Serialization, DI và reflection thường cần generated schema, type token hoặc metadata bổ sung. Public generic API cần để ý wildcard/JVM interop, variance và binary signature.

# 7. Functional error modeling

Exception phù hợp exceptional failure và framework/Java integration. Domain error đôi khi rõ hơn bằng sealed type:

```kotlin
sealed interface LoginError {
    data object InvalidCredential : LoginError
    data object NetworkUnavailable : LoginError
    data class Unknown(val cause: Throwable) : LoginError
}
```

Không biến mọi function thành `Result`/Either theo nghi thức. Boundary cần contract rõ: method nào throw, method nào trả domain error, cancellation có được propagate không, retry decision nằm ở đâu.

# 8. Concurrency architecture

Concurrency production không phải chọn `Dispatchers.IO` rồi kết thúc. Cần xác định:

```text
owner của scope
lifetime của work
structured parent/child relation
parallelism budget
shared-state policy
cancellation semantics
ordering requirement
backpressure
retry/replay semantics
```

Một repository tự tạo `CoroutineScope(SupervisorJob() + Dispatchers.IO)` có nghĩa repository đang sở hữu lifetime độc lập; phải có lý do và shutdown/test strategy. Nếu work chỉ thuộc request/screen, structured scope của caller thường đúng hơn.

## 8.1 Race condition tồn tại dù chỉ dùng coroutine

Coroutine có thể interleave ở suspension point. Đoạn read-modify-write vẫn race nếu nhiều coroutine cùng chạy:

```kotlin
val old = state.value
val next = old.copy(count = old.count + 1)
state.value = next
```

Nếu invariant yêu cầu atomicity, dùng API atomic phù hợp, `Mutex`, actor/state owner single-threaded hoặc database transaction. Chọn primitive theo invariant, không theo thói quen.

## 8.2 Cancellation là control flow

`CancellationException` không phải business failure. Generic `catch (Throwable)` rồi convert thành `Error` có thể phá structured cancellation. Cleanup bắt buộc có thể dùng `finally`; `NonCancellable` chỉ nên bọc đoạn cleanup nhỏ thật sự cần hoàn tất, không biến toàn operation thành uncancellable.

# 9. Locks, atomics và thread safety

`Mutex` suspend thay vì block thread:

```kotlin
private val mutex = Mutex()

suspend fun update() = mutex.withLock {
    // critical section nhỏ, không chứa network call nếu không cần
}
```

Atomic phù hợp state nhỏ/operation lock-free đơn giản. Actor/single-owner phù hợp khi nhiều event cần ordering. Thread confinement phù hợp khi subsystem có execution context rõ. Không dùng lock lớn quanh I/O chậm vì dễ tạo convoy/starvation.

# 10. Flow architecture ở hệ thống lớn

Flow phù hợp dữ liệu thay đổi theo thời gian; one-shot command vẫn thường là `suspend fun`. Khi graph Flow lớn, cần kiểm soát cold/hot semantics, sharing scope, replay và backpressure.

`stateIn`/`shareIn` không chỉ là optimization. Chúng thay đổi lifetime của upstream. Nếu scope sống application-level, network/database subscription có thể sống lâu hơn UI tưởng. `SharingStarted.WhileSubscribed(...)` phải được chọn dựa trên reconnect cost và stale-state semantics.

Backpressure operator có nghĩa nghiệp vụ khác nhau:

```text
buffer
= cho producer chạy trước consumer trong giới hạn buffer

conflate
= bỏ intermediate state, giữ mới nhất

collectLatest
= cancel xử lý cũ khi value mới tới

flatMapLatest
= cancel sub-flow cũ khi key mới tới
```

`conflate` hợp progress/state mới nhất, nhưng có thể sai với payment/event/audit stream nơi mỗi item đều có ý nghĩa.

## 10.1 StateFlow không phải event bus

`StateFlow` có current value và replay state cho collector mới. One-off event như “show copied toast” có semantics khác durable state như “payment succeeded”. Đừng ép mọi thứ vào `SharedFlow`/Channel; trước hết quyết định event có được phép mất khi collector inactive hay phải reconstruct từ state.

# 11. Compose architecture ở scale lớn

Compose tốt không chỉ là `@Composable`. Cần hiểu ba tầng:

```text
State model
→ Composition / identity / effects
→ Layout / draw / input / semantics
```

Route-level composable có thể nối ViewModel/navigation/lifecycle; content composable nhận immutable state + callbacks:

```kotlin
@Composable
fun HomeRoute(viewModel: HomeViewModel = hiltViewModel()) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    HomeScreen(state = state, onAction = viewModel::onAction)
}
```

`HomeScreen` không nên biết repository hoặc DI graph. Điều này làm preview, screenshot test và semantics test đơn giản hơn.

## 11.1 Recomposition không đồng nghĩa redraw toàn màn hình

Compose ghi nhận state reads và invalidates scope/phases liên quan. Performance issue cần xác định state nào thay đổi và state được đọc ở composition, layout hay draw phase. Không sửa bằng cách thêm `remember` bừa.

Stable identity rất quan trọng với lazy content:

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        Row(item)
    }
}
```

Key không phải chỉ để performance; nó gắn logical identity với composition state. Key sai có thể khiến local remembered state “đi theo vị trí” thay vì entity.

## 11.2 Effect API phải khớp lifetime

`LaunchedEffect(key)` restart theo key; `DisposableEffect` dành cho register/unregister resource; `rememberUpdatedState` giữ callback/value mới mà không restart effect; `SideEffect` sync ra object bên ngoài sau successful composition.

Một effect cần sống sau khi screen biến mất không thuộc UI composition lifecycle và nên được đẩy về owner khác như ViewModel/repository/WorkManager tùy semantics.

# 12. Design system

Design system production gồm color/typography/spacing/shape tokens, semantic component, interaction state, accessibility, theming và migration policy. Component API nên semantic hơn là expose vô hạn flag kỹ thuật.

# 13. Adaptive UI

Android chạy trên phone, tablet, foldable, desktop-like window và multi-window. Không hardcode theo orientation. Layout nên dựa available window/capability và giữ navigation/state continuity khi window đổi.

# 14. Accessibility và internationalization

Accessibility là correctness: semantics, focus order, touch target, dynamic font scale, contrast và TalkBack behavior cần được thiết kế từ đầu. Internationalization cần resource/plural/locale-aware formatting thay vì nối string theo English grammar.

# 15. Startup architecture

Cold start chịu ảnh hưởng `Application`, ContentProvider auto-init, DI graph, class loading, disk I/O, DB open/migration và first-frame Compose work. Mỗi eager initializer là một phần critical path.

Lazy initialization chỉ tốt nếu không dời latency thành jank ở first interaction. Dùng Perfetto/Macrobenchmark để xác định critical path thực, không đo bằng log thủ công rồi kết luận.

# 16. Baseline Profiles và Macrobenchmark

Baseline Profile giúp ART precompile hot paths quan trọng. Macrobenchmark đo startup/scroll/interaction ở package-level; microbenchmark đo primitive nhỏ. Baseline Profile không sửa algorithm xấu, blocking I/O hoặc layout/recomposition sai.

# 17. Observability

Production app cần crash/ANR reporting, structured logging, performance metrics và domain telemetry có privacy guard. Log phải trả lời “failure xảy ra ở đâu và với version/artifact/config nào” mà không leak PII/token.

Telemetry schema cũng là API. Nếu rename event/field tùy tiện, dashboard và alert mất continuity. Release version, build fingerprint, experiment/feature flag và correlation ID nên đủ để khoanh vùng regression.

# 18. Resilience engineering

Mobile luôn có partial failure: timeout sau server commit, process death giữa write và UI update, token expire đồng thời ở nhiều request, retry sau reconnect, duplicate tap, stale cache và backend rollout không đồng bộ.

Retry phải dựa idempotency. Một request timeout không nói server chưa xử lý. Với mutation quan trọng, client/server cần operation ID hoặc idempotency key để replay an toàn.

Graceful degradation nghĩa định nghĩa trước feature nào vẫn hoạt động khi dependency fail, không phải catch mọi exception rồi hiện “Something went wrong”.

# 19. Large-scale modularization

Module boundary tốt giới hạn vùng ảnh hưởng của thay đổi, enforce dependency direction và phản ánh ownership. Tránh `core:common` thành god-module. Interface chỉ đáng tồn tại khi tạo contract/decoupling/test seam thật, không phải vì mỗi class “phải có interface”.

# 20. Convention plugins và build-logic

Convention plugin giúp gom cấu hình repeated ở multi-module project. Nhưng build-logic là production code: cần versioning, test, configuration-cache awareness và tránh hidden I/O trong configuration phase.

# 21. API/module compatibility

Public API phải nghĩ theo ba lớp:

```text
source compatibility
binary compatibility
behavioral compatibility
```

Giữ signature chưa chắc giữ behavior. Thay caching/threading/cancellation semantics có thể phá caller dù compile vẫn xanh. Kotlin metadata, default args, public inline, JVM name và generic signature có thể ảnh hưởng binary consumer.

# 22. Library publishing

Android/Kotlin library cần AAR/POM metadata, dependency exposure policy, consumer R8 rules, minSdk/JVM target, public API docs, sample consumer và compatibility matrix. `api` vs `implementation` là public classpath contract chứ không chỉ build optimization.

# 23. Kotlin Multiplatform awareness

KMP giúp share code giữa platform nhưng không tự động làm platform boundary biến mất. Share concern ổn định như domain/data khi hợp lý; giữ platform-specific lifecycle/UI/hardware ở platform layer. `expect/actual` là công cụ, không phải mục tiêu tăng “% shared code”.

# 24. JNI / native interoperability awareness

JNI/NDK tạo boundary về memory ownership, thread affinity, ABI, page size, symbolication và crash diagnostics. Dùng khi có native dependency hoặc performance/platform requirement đã chứng minh; đừng chuyển code sang C++ theo trực giác “native nhanh hơn”.

# 25. Android platform boundaries

Binder IPC có transaction/serialization cost. Bundle/Parcelable không nên chứa object graph lớn. Exported component, deep link, ContentProvider URI, PendingIntent và Binder input là untrusted boundary; validate như network input.

# 26. Privacy, security, compliance

Permission theo least privilege. Authorization nghiệp vụ nằm server-side; client chỉ là UX/risk signal. Keystore bảo vệ key material tốt hơn file plaintext nhưng không biến compromised device thành trusted environment.

Log, clipboard, screenshot, backup, WebView, notification và analytics đều có thể leak sensitive data. Security review phải cover data lifecycle, không chỉ crypto API.

# 27. Release engineering

Release pipeline production tối thiểu cần formatting/static analysis, unit/integration tests, lint, release/minified build, signing, mapping/symbol upload, artifact provenance, staged rollout và rollback/kill-switch strategy.

`versionCode` là monotonically increasing distribution identity; `versionName` là user-facing label. Nhưng để debug production cần thêm artifact identity: Git commit, build config, dependency lock, mapping file và server/feature-flag context.

Release-only failure thường tới từ R8, resource shrinking, different manifest/resource merge, signing, build config hoặc production backend—not từ source path debug. Vì vậy CI phải build/test artifact gần production nhất.

# 28. Testing architecture cấp tổ chức

Test strategy dựa risk, không dựa tỷ lệ unit/UI cố định. Pure logic test nhanh; database/network contract test kiểm tra boundary; instrumentation/Compose UI test kiểm tra platform semantics; Macrobenchmark kiểm tra performance contract. Flaky test là defect engineering vì nó phá tín hiệu CI.

# 29. Technical debt và migration strategy

Migration lớn nên dùng strangler/branch-by-abstraction: tạo path mới cạnh path cũ, chuyển dần traffic, đo regression, rồi xóa legacy. Mỗi migration cần exit criteria, telemetry, fallback, owner và deadline xóa compatibility layer.

# 30. Master-level architectural heuristics

Một hệ thống tốt thường có dependency một chiều, state owner rõ, source of truth rõ, side effect ở boundary có owner, concurrency structured, public API nhỏ, error semantics nhất quán, persistence phù hợp lifetime, build reproducible, security boundary rõ và migration có kế hoạch.

Pattern như MVVM/MVI/Clean Architecture chỉ là công cụ. Nếu không giải thích được invariant, lifetime, failure và compatibility, tên pattern không chứng minh kiến trúc tốt.

# 31. Kotlin/Android keyword & API index

Các keyword cần nhận diện: `package`, `import`, `class`, `interface`, `fun`, `object`, `val`, `var`, `typealias`, `this`, `super`, `as`, `is`, `in`, `when`, `if`, `else`, `for`, `while`, `try`, `catch`, `finally`, `throw`, `return`, `break`, `continue`, `sealed`, `data`, `enum`, `annotation`, `companion`, `inner`, `open`, `final`, `abstract`, `override`, `private`, `protected`, `internal`, `public`, `lateinit`, `const`, `tailrec`, `operator`, `infix`, `inline`, `noinline`, `crossinline`, `reified`, `suspend`, `external`, `expect`, `actual`, `out`, `vararg`, `where`, `by` và các contextual/use-site keywords theo language version.

Standard library families cần quen: string conversion/search, collection transformation/aggregation, null/error helpers, scope functions và sequence. Coroutine families cần nhận diện: `launch`, `async`, `coroutineScope`, `supervisorScope`, `withContext`, `delay`, `yield`, `ensureActive`, timeout, `Mutex`, Channel, Flow, StateFlow và SharedFlow.

Android families cần nhận diện: Application/Activity/Fragment/Service/Receiver/Provider; Lifecycle/ViewModel/SavedStateHandle; Compose state/effect/layout APIs; Room/DataStore/WorkManager; Navigation; testing/performance APIs.

# 32. Version matrix và cách đọc một project Android hiện đại

Baseline tài liệu này dùng Kotlin **2.4.20**, K2, Android Studio Quail 4 / 2026.1.4 Patch 1, AGP **9.4.1**, Android 17 / API 37 và Compose BOM snapshot 2026.09.00. Các số này là documentation snapshot, không phải constant kiến trúc.

Khi version thay đổi, không chỉ hỏi “latest là gì?” mà hỏi:

```text
node nào đổi?
contract nào đổi?
consumer nào bị ảnh hưởng?
artifact nào khác?
runtime behavior nào được bật?
rollback có còn tương thích dữ liệu không?
```

# 33. Compiler plugin và generated code như một phần của kiến trúc

Compose compiler plugin transform composable function; serialization/Parcelize/compiler plugin và KSP/kapt processors sinh code/metadata. Generated code ảnh hưởng compile time, API visibility, runtime startup và debugging.

Khi nâng Kotlin mà lỗi nằm trong Room/Hilt/serialization/Compose generated path, kiểm tra plugin/processor compatibility trước khi sửa business source. Clean build giúp loại stale generated artifacts; CI clean environment là tín hiệu quan trọng nếu local incremental build khác behavior.

# 34. Source compatibility, binary compatibility và behavioral compatibility

Một thay đổi có thể source-compatible nhưng binary-incompatible hoặc compile được nhưng behavior khác. Public default argument, inline function, const, value class, enum/sealed evolution và JVM signature đều cần review đặc biệt với library.

Behavioral compatibility thường bị bỏ qua: repository giữ nguyên signature nhưng đổi từ cache-first sang network-first có thể làm UX, latency và offline behavior thay đổi. Contract phải document threading, cancellation, ordering, nullability, retry và idempotency khi chúng quan trọng.

# 35. Architecture ở codebase lớn: dependency graph quan trọng hơn tên pattern

Architecture tốt giới hạn blast radius, làm dependency direction rõ và cho phép subsystem evolve độc lập ở mức hợp lý. Use case/interface/module không có giá trị nếu chỉ thêm ceremony. Mỗi abstraction cần trả lời nó đang cô lập volatility, ownership hay policy nào.

# 36. Performance engineering: hypothesis → measurement → change → verification

Bắt đầu từ user-facing metric như startup, frame time, time-to-content, memory, network latency, battery hoặc artifact size. Thu trace/profile trên device đại diện, tạo hypothesis, thay đổi một yếu tố và đo lại.

Nhìn percentile, không chỉ average. Một UI average 10 ms nhưng thường xuyên có frame 100 ms vẫn jank. Baseline Profile/Macrobenchmark/Perfetto là công cụ đo; chúng không thay design đúng.

# 37. Reliability engineering trên mobile

Mobile app sống cùng process death, network transition, duplicate delivery, server/client version skew và partial failure. Production design phải định nghĩa idempotency, retry policy, local persistence, conflict, reconstruction và observability trước khi bug xảy ra.

Offline-first không có nghĩa mọi app phải có distributed sync engine. Nó nghĩa requirement offline được model rõ. Nếu chỉ cần cached read, đừng xây durable mutation queue không cần thiết.

# 38. Security engineering: xem APK là môi trường không đáng tin

Attacker có thể inspect/decompile/hook client. Không lưu server secret dài hạn trong APK rồi kỳ vọng R8 bảo vệ. Backend phải authorize. Client chỉ giữ credential/session với lifetime và secure-storage strategy phù hợp.

External Intent/URI/WebView/native input đều là untrusted input. Native parser còn có memory-safety risk riêng.

# 39. Release, rollout và rollback như một phần của feature design

Staged rollout giảm blast radius chỉ khi telemetry đủ phát hiện regression. Feature flag giúp kill behavior nhưng tạo thêm state space; mỗi flag phải có owner và cleanup date.

Rollback binary không đủ nếu DB schema, serialized data hoặc backend protocol đã migrate theo hướng không tương thích. Release design cần backward/forward compatibility window cho dữ liệu quan trọng.

# 40. Modern vs legacy Android — phân loại thay vì phán xét

Không nên gắn `legacy = sai`, `modern = đúng`. Hãy phân loại:

```text
Deprecated / unsafe
→ cần migration có kế hoạch

Supported nhưng có replacement hiện đại
→ migrate khi benefit > cost

Still-valid API cho use case cụ thể
→ giữ nếu contract phù hợp

Historical API
→ học để đọc code cũ, không dùng cho code mới
```

Ví dụ phổ biến:

| Thế hệ cũ | Hướng modern | Ghi chú |
|---|---|---|
| Java-heavy Android | Kotlin-first | Java interop vẫn quan trọng |
| Kotlin synthetic views | View Binding / Compose | synthetic không còn là modern workflow |
| `findViewById` | View Binding / Compose | vẫn hợp lệ trong View code |
| XML/Fragment | Compose hoặc hybrid | XML/Fragment vẫn supported |
| `AsyncTask` | coroutine / WorkManager theo lifetime | không thay bằng coroutine một cách máy móc |
| callback pyramid | suspend / Flow | callback vẫn tồn tại ở platform boundary |
| LiveData everywhere | Flow/StateFlow ở modern stack | LiveData vẫn usable/interop tốt |
| SharedPreferences | DataStore cho structured settings | không phải mọi key-value đều buộc migrate tức thì |
| `startActivityForResult` | Activity Result API | lifecycle-aware contract tốt hơn |
| manual Service cho deferred work | WorkManager | Service vẫn đúng cho ongoing user-visible work |
| RxJava-heavy | coroutine/Flow phổ biến hơn | RxJava codebase không tự động sai |
| kapt | KSP khi processor hỗ trợ | migrate per-processor |
| `kotlinOptions {}` | `compilerOptions {}` | modern Kotlin Gradle DSL |
| Compose compiler mapping riêng | Compose compiler plugin cùng Kotlin | Kotlin 2.0+ |
| K1 | K2 | K2 là compiler generation mặc định mới |

Migration tốt giữ behavior trước rồi thay implementation. Characterization test, adapter boundary và incremental rollout quan trọng hơn “rewrite sạch”.

# 41. Master checklist trước khi gọi hệ thống production-ready

Một hệ thống Kotlin/Android mature phải trả lời được:

```text
Version/toolchain contract là gì?
Source of truth ở đâu?
Owner của state/coroutine/resource là ai?
Điều gì sống qua recomposition/configuration/process death?
Race/order/idempotency được kiểm soát thế nào?
Flow/event semantics có bị mất hoặc replay sai không?
Compose effect có đúng lifetime không?
Network/database migration có rollback-compatible không?
Security boundary nào nhận untrusted input?
Metric/log nào chứng minh behavior production?
Release artifact nào đang chạy trên device?
R8/signing/variant có được test không?
Feature lỗi thì rollback/disable bằng cách nào?
Legacy path bao giờ được xóa?
```

Mastery không phải nhớ toàn bộ Android SDK. Nó là khả năng hạ một vấn đề từ UI xuống state/lifecycle, từ coroutine xuống ordering/cancellation, từ Kotlin source xuống compiler/bytecode, từ Gradle xuống artifact, và từ bug production xuống invariant + evidence thay vì đoán.
