# Case 15 — Gradle, Android Gradle Plugin và Build Variant Model

Android project không chỉ là tập source code Kotlin rồi bấm Run. Trước khi một dòng Kotlin trở thành APK/AAB, build system phải quyết định source set nào được lấy, manifest nào được merge, resource nào thắng khi trùng tên, dependency nào xuất hiện trong từng variant, compiler/plugin nào chạy, generated code nào được tạo, R8 có shrink/optimize hay không, artifact nào được ký và cuối cùng task graph nào thực sự cần chạy. Khi project nhỏ, Android Studio che phần lớn complexity này. Khi project lớn, không hiểu build model sẽ dẫn đến các bug kiểu “debug chạy nhưng release crash”, “flavor A có permission mà flavor B không có”, “CI build khác local”, hoặc “thay một file nhưng Gradle rebuild nửa repository”.

Mục tiêu chapter này là tạo mental model để đọc và thiết kế build, không phải thuộc mọi property của AGP DSL.

## 1. Ba lớp phải phân biệt: Gradle, Android Gradle Plugin và Kotlin plugin

**Gradle** là general build engine. Nó quản lý project, plugin, task graph, dependency resolution, cache, configuration phase và execution phase. Gradle không tự hiểu Activity, AndroidManifest hay resource Android.

**Android Gradle Plugin — AGP** bổ sung Android-specific model vào Gradle. Nó hiểu `android {}`, `compileSdk`, `defaultConfig`, build types, product flavors, source sets, manifest merger, Android resources, D8/R8, signing, APK/AAB packaging và test variants.

**Kotlin Gradle Plugin** chịu trách nhiệm Kotlin compilation, compiler options và phần Kotlin-specific toolchain. Compose compiler, KSP và các compiler plugin khác lại là những lớp riêng gắn vào pipeline này.

Khi build fail, trước tiên cần xác định failure thuộc lớp nào. Dependency resolution error khác AGP variant configuration error; Kotlin compiler error khác R8 missing-class error. Gom mọi lỗi thành “Gradle lỗi” khiến debug chậm hơn nhiều.

## 2. Settings, root build và module build có vai trò khác nhau

`settings.gradle.kts` xác định project graph ở cấp repository: module nào được include, plugin/dependency repository nào được dùng, version catalog nào được import và đôi khi composite build/build-logic nào được gắn vào.

Root `build.gradle.kts` ngày nay nên nhẹ. Nó thường khai báo plugin versions bằng `apply false`, hoặc rất ít cross-project configuration. Nhét mọi configuration vào root build file tạo hidden coupling và làm configuration phase khó tối ưu.

Mỗi module có `build.gradle.kts` riêng. Android application module thường dùng `com.android.application`; reusable Android library dùng `com.android.library`; pure Kotlin module có thể chỉ dùng Kotlin/JVM; dynamic feature dùng plugin riêng. Plugin quyết định module model và task graph nào tồn tại.

Một module boundary tốt vì thế không chỉ là package organization. Nó là **build boundary**: dependency graph, compilation unit, public API surface và cache boundary.

## 3. `compileSdk`, `minSdk`, `targetSdk` không phải ba cách viết cùng một version

`compileSdk` quyết định bộ Android API mà source code được phép compile against. Tăng `compileSdk` cho phép gọi API mới nhưng tự nó không nói app sẽ chạy trên version nào.

`minSdk` là OS thấp nhất app hỗ trợ. Nếu `minSdk = 26`, app không được cài trên API thấp hơn 26. Mọi code gọi API mới hơn minSdk phải được guard hoặc được library/desugaring abstraction xử lý phù hợp.

`targetSdk` là lời tuyên bố app đã được kiểm thử theo behavior contract của Android version tương ứng. Nhiều breaking behavior changes chỉ bật khi app tăng target SDK. Vì vậy tăng target SDK là migration project, không nên xem như sửa một con số để upload Play Console.

```kotlin
android {
    namespace = "com.example.app"
    compileSdk = 37

    defaultConfig {
        applicationId = "com.example.app"
        minSdk = 26
        targetSdk = 37
        versionCode = 120
        versionName = "3.4.0"
    }
}
```

Con số trên chỉ là ví dụ cấu trúc. Project thật phải dùng compatibility matrix và policy hiện hành thay vì copy cứng từ tài liệu học.

## 4. Build type giải quyết environment/build behavior, product flavor giải quyết product dimension

Build type thường biểu diễn cách artifact được build: `debug`, `release`, đôi khi `benchmark` hoặc `staging`. Nó điều khiển các concern như debuggable, minification, signing, suffix, resource value và optimization.

```kotlin
android {
    buildTypes {
        debug {
            applicationIdSuffix = ".debug"
            versionNameSuffix = "-debug"
        }
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

Product flavor biểu diễn một dimension của sản phẩm. Ví dụ `demo/full`, `internal/public`, hoặc brand/region. Khi có nhiều dimension, cần khai báo `flavorDimensions` rõ ràng.

```kotlin
android {
    flavorDimensions += listOf("tier", "region")

    productFlavors {
        create("demo") {
            dimension = "tier"
            applicationIdSuffix = ".demo"
        }
        create("full") {
            dimension = "tier"
        }
        create("global") {
            dimension = "region"
        }
        create("kr") {
            dimension = "region"
        }
    }
}
```

Build variant là cross-product của những lựa chọn đó, ví dụ `demoKrDebug` hoặc `fullGlobalRelease`. Nếu số dimension tăng không kiểm soát, variant explosion sẽ làm IDE sync, CI matrix và dependency maintenance phức tạp nhanh chóng.

Senior rule: chỉ tạo flavor khi khác biệt thực sự là build-time product dimension. Feature flag runtime không nên biến thành flavor chỉ vì “có hai trạng thái”.

## 5. Source set precedence là nguyên nhân của rất nhiều “mystery behavior”

Android build có thể lấy source/resource/manifest từ nhiều source set. Với một variant kiểu `demoDebug`, Gradle có thể xem `src/demoDebug/`, `src/debug/`, `src/demo/`, rồi `src/main/` theo precedence tương ứng.

Ví dụ:

```text
app/
└── src/
    ├── main/
    │   ├── kotlin/
    │   ├── res/
    │   └── AndroidManifest.xml
    ├── debug/
    │   ├── kotlin/
    │   └── res/
    ├── demo/
    │   └── res/
    └── demoDebug/
        └── res/
```

Resource có cùng tên có thể bị override theo precedence. Manifest cũng được merge theo rule tương tự. Nhưng Kotlin/Java class trùng fully-qualified name trong hai source set cùng tham gia variant thường gây duplicate-class error chứ không phải override như resource.

Source sets rất hữu ích cho fake endpoint, debug-only screen, brand resource hoặc test implementation, nhưng lạm dụng sẽ tạo code path khó nhìn thấy bằng search thông thường.

## 6. Manifest Merger là build-time composition system

Manifest cuối cùng của app không nhất thiết giống `src/main/AndroidManifest.xml`. Nó có thể được merge từ app manifest, build type, flavor và manifests của dependencies.

Điều này giải thích tại sao một SDK có thể thêm permission/provider/service vào app dù bạn không viết chúng trong main manifest.

Khi có conflict, dùng Manifest Merger report thay vì đoán. Các `tools:` marker như `tools:replace`, `tools:remove`, `tools:node` có thể giải quyết merge conflict, nhưng phải hiểu hậu quả security/runtime của việc override metadata từ dependency.

Một `android:exported`, provider authority hoặc permission sai trong manifest merged artifact có thể trở thành production vulnerability dù source manifest nhìn có vẻ đúng.

## 7. `BuildConfig`, `resValue`, manifest placeholder và secret

Build-time values có nhiều cơ chế. `buildConfigField` tạo constant trong generated `BuildConfig`; `resValue` tạo Android resource; manifest placeholders thay token lúc merge manifest.

Không cơ chế nào biến value thành secret. Bất kỳ secret nào ship trong APK/AAB đều có thể bị trích xuất. API key có restriction vẫn có thể tồn tại trong app nếu service thiết kế cho client-side key, nhưng credential có quyền backend không được nhúng vào build config.

```kotlin
buildTypes {
    debug {
        buildConfigField("String", "API_BASE_URL", "\"https://staging.example.com\"")
    }
}
```

Build config là configuration distribution, không phải secure vault.

## 8. Dependency configurations biểu diễn visibility và classpath

`implementation` nói dependency cần để compile module hiện tại nhưng không được expose như public transitive API cho consumer.

`api` trong library module expose dependency qua public API surface. Dùng `api` quá nhiều tăng coupling và recompilation cascade.

`compileOnly` cần khi compile nhưng không package runtime implementation. `runtimeOnly` ngược lại: runtime cần nhưng compile code không trực tiếp reference. Test source sets có `testImplementation`, `androidTestImplementation`, v.v.

Một heuristic tốt là mặc định `implementation`, chỉ dùng `api` khi public API của module thật sự để lộ type của dependency đó.

## 9. Version catalog giúp centralize coordinates nhưng không thay dependency governance

`libs.versions.toml` giúp định danh dependency/plugin bằng alias nhất quán.

```toml
[versions]
kotlin = "..."
coroutines = "..."

[libraries]
coroutines-core = { module = "org.jetbrains.kotlinx:kotlinx-coroutines-core", version.ref = "coroutines" }

[plugins]
android-application = { id = "com.android.application", version = "..." }
```

Version catalog không tự đảm bảo compatibility, license, vulnerability hay reproducibility. Những concern đó cần dependency locking, verification, SBOM/vulnerability scanning và upgrade policy riêng.

## 10. Convention plugin tốt hơn copy-paste Gradle block

Khi nhiều module lặp cùng compile options, lint, Compose config hoặc test dependencies, copy-paste khiến configuration drift. **Convention plugin** gom policy build thành code/plugin dùng lại.

Thay vì mỗi module tự viết 50 dòng:

```kotlin
plugins {
    id("company.android.library")
}
```

Convention plugin có thể áp AGP/Kotlin plugin, configure namespace policy, Java toolchain, compiler options, lint, Compose, test defaults và common dependencies.

Điểm quan trọng là convention plugin chứa **convention**, không chứa mọi business-specific dependency. Nếu plugin trở thành một global god object, mọi module lại coupled theo cách khác.

## 11. Gradle configuration phase và execution phase

Gradle trước tiên configuration project và tạo task graph, sau đó mới execute những task cần thiết. Configuration quá nặng làm mọi command chậm, kể cả task nhỏ.

Các pattern như eager task creation, đọc file/network trong configuration, `afterEvaluate` tùy tiện hoặc global cross-project mutation làm build khó cache và khó parallelize.

Configuration Cache cố tái sử dụng kết quả configuration giữa các build khi plugin/task compatible. Build Cache tái sử dụng task output khi input fingerprint giống. Hai cache giải quyết hai phase khác nhau.

Senior debug build performance nên bắt đầu bằng measurement: Gradle Build Scan/profile, task timing, cache hit/miss, critical path, annotation/code generation cost. Không tối ưu chỉ vì thấy “nhiều module”.

## 12. Incremental build phụ thuộc input/output contract

Một task cacheable/incremental cần khai báo input/output chính xác. Plugin custom hoặc codegen đọc file ngoài model có thể khiến build không reproducible hoặc cache trả kết quả sai.

KSP thường được chọn thay KAPT trong ecosystem hiện đại khi processor support, một phần vì code generation model phù hợp Kotlin hơn và có thể giảm overhead so với Java annotation-processing pipeline. Tuy nhiên migration phải dựa processor thực tế; không phải mọi KAPT processor đều có replacement KSP tương đương.

## 13. Toolchain và JVM target phải được hiểu là compatibility contract

JDK chạy Gradle/AGP, Java/Kotlin language level và bytecode/JVM target là các khái niệm khác nhau. Project có thể dùng một JDK để chạy build nhưng compile source với target khác.

Java toolchain giúp build thống nhất giữa local và CI:

```kotlin
kotlin {
    jvmToolchain(17)
}
```

Con số cần theo compatibility matrix của Kotlin/AGP/project. Không nên upgrade JDK, Gradle, AGP, Kotlin và Compose compiler cùng lúc mà không có test matrix vì khi fail rất khó xác định layer gây regression.

## 14. Android Components / Variant API dành cho plugin và build logic nâng cao

AGP có variant-oriented API để đọc hoặc biến đổi artifact/task configuration theo variant mà không dựa internal API không ổn định. Đây là hướng đúng khi viết plugin build hoặc instrumentation logic tùy variant.

Anti-pattern phổ biến là script truy cập task name bằng string, `afterEvaluate`, hoặc internal AGP classes. Cách này thường vỡ khi upgrade AGP.

Nếu custom build logic cần biết variant, hãy ưu tiên public AGP Variant API và artifact API của version đang dùng.

## 15. Resource processing, D8, R8 và packaging pipeline

Một mental model đơn giản:

```text
Kotlin/Java source
→ compile/generated code
→ JVM bytecode
→ desugaring/D8
→ DEX

resources + manifest
→ merge/process/package

release optimization
→ R8 shrink/optimize/obfuscate

DEX + resources + native libs
→ APK/AAB artifact
```

Pipeline thật chi tiết hơn, nhưng model này giúp xác định lỗi nằm ở compile, bytecode transform, shrinker hay packaging.

Debug build thường ít optimization hơn nên reflection bug hoặc missing keep rule chỉ xuất hiện ở release. Vì vậy “debug app chạy” không chứng minh release artifact đúng.

## 16. Consumer ProGuard rules của library

Android library có thể cần cung cấp `consumerProguardFiles` để rule cần thiết được merge vào app consumer khi R8 chạy.

Library author không nên bắt app consumer đoán reflection/JNI rule bên trong SDK. Ngược lại, keep rule quá rộng như giữ toàn bộ package làm giảm lợi ích shrinker cho mọi app dùng library.

Rule tốt phải càng hẹp càng tốt và đi cùng test minified consumer artifact.

## 17. Signing config và build credentials

Debug signing key có thể generated/local. Release signing key là production identity và cần được quản lý như credential quan trọng. Không commit keystore/password vào Git.

CI nên lấy signing material từ secret manager/secure environment, hạn chế quyền truy cập và audit usage. Nếu dùng Play App Signing, vẫn cần hiểu upload key khác app signing key về vai trò và recovery process.

## 18. Reproducible build và supply-chain thinking

Hai build từ cùng commit ideally phải cho behavior tương đương và dependency graph có thể giải thích được. Dynamic versions kiểu `1.+`, repository không kiểm soát, plugin tải artifact bất định hoặc script phụ thuộc network mutable đều làm reproducibility kém.

Production build governance nên theo dõi:

- source commit;
- toolchain versions;
- resolved dependency graph;
- signing identity;
- build flags/variant;
- generated SBOM nếu tổ chức yêu cầu;
- artifact checksum;
- mapping file của R8;
- provenance từ CI.

Mục tiêu không phải bureaucracy mà là khả năng trả lời “binary đang chạy ngoài production được build từ cái gì?”.

## 19. Build performance: tránh cả hai cực đoan

Một monolith module có thể compile chậm và mọi thay đổi invalidate quá nhiều code. Nhưng hàng trăm module micro-granular cũng làm configuration/dependency graph phức tạp.

Module hóa vì boundary có giá trị: ownership, parallel work, API isolation, testability, build isolation hoặc feature delivery. Không module hóa chỉ để số module lớn.

Những hướng tối ưu thường có impact thực tế hơn micro-tweak:

- giảm `api` surface;
- tránh annotation processor nặng không cần thiết;
- bật/correct cache;
- dùng convention plugin;
- bỏ configuration side effect;
- tránh generated code invalidating quá rộng;
- tách feature có churn độc lập;
- profile CI critical path.

## 20. CI matrix theo variant phải có chủ đích

Nếu project có 20 variants, test toàn bộ ở mọi commit có thể quá đắt. Nhưng chỉ test `debug` cũng không đủ.

Một chiến lược thường hợp lý:

- PR: compile/lint/unit test representative variants;
- main/nightly: mở rộng variant/device matrix;
- release: build đúng production variant, minified, signed-like pipeline, instrumentation/critical smoke test;
- flavor có behavior riêng phải có test riêng, không chỉ rely common debug.

CI matrix phải phản ánh risk chứ không phản ánh số variant một cách máy móc.

## 21. Các lỗi thường gặp và cách suy luận

### Debug chạy, release crash

Kiểm tra R8 keep rules, reflection/serialization, JNI symbol, release-only config, signing/network security config, resource shrinking và code path build type.

### Một flavor có resource sai

Kiểm tra source-set precedence, flavor dimension order và resource merger output.

### Permission “tự nhiên xuất hiện” trong manifest

Mở merged manifest và tìm manifest từ dependency nào thêm permission/component.

### Local build được, CI fail

Kiểm tra JDK/toolchain, dependency repository, case-sensitive filesystem, uncommitted generated/local file, environment variable và cached state.

### Build chậm sau khi thêm processor/plugin

Đo task graph, processor time và cacheability trước khi refactor project structure.

## 22. Senior checklist cho build-system change

Khi review thay đổi build, hãy hỏi: thay đổi áp dụng variant nào; có thay manifest/resource precedence không; public dependency surface có tăng không; có ảnh hưởng release/minified artifact không; có làm configuration cache mất hiệu lực không; CI có build đúng variant mới không; secret/signing có bị đưa vào source không; và rollback toolchain có còn khả thi nếu upgrade fail không.

Build system là production code. Một lỗi build configuration có thể không xuất hiện trong unit test nhưng vẫn thay permission, signing, resource, shrinker hoặc artifact được ship tới hàng triệu device.

## 23. Official references

- Android build overview: https://developer.android.com/build
- Build variants and source sets: https://developer.android.com/build/build-variants
- Gradle tips: https://developer.android.com/build/gradle-tips
- Android Gradle Plugin APIs: https://developer.android.com/reference/tools/gradle-api

Đọc reference theo version AGP đang dùng; không giả định DSL/internal behavior của một version cũ vẫn đúng với version mới.