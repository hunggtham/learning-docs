# Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**. Route đi từ Gradle/AGP/Kotlin plugin → settings/root/module graph → source sets, manifest/resources và dependency variants → tasks, generated code, R8 và signing → CI/local parity, để build model giải thích lỗi release và flavor.

Android dự án (project / 프로젝트) không chỉ là tập mã nguồn (source code / 소스 코드) Kotlin rồi bấm Run. Trước khi một dòng Kotlin trở thành APK/AAB, hệ thống dựng (build system / 빌드 시스템) phải quyết định nguồn (source / 소스) set nào được lấy, manifest nào được merge, tài nguyên (resource / 자원) nào thắng khi trùng tên, phụ thuộc (dependency / 의존성) nào xuất hiện trong từng variant, trình biên dịch (compiler / 컴파일러)/plugin nào chạy, generated mã (code / 코드) nào được tạo, R8 có shrink/optimize hay không, sản phẩm tạo ra (artifact / 산출물) nào được ký và cuối cùng tác vụ (task / 작업) đồ thị (graph / 그래프) nào thực sự cần chạy. Khi dự án (project / 프로젝트) nhỏ, Android Studio che phần lớn độ phức tạp (complexity / 복잡도) này. Khi dự án (project / 프로젝트) lớn, không hiểu bản dựng (build / 빌드) mô hình (model / 모델) sẽ dẫn đến các bug kiểu “gỡ lỗi (debug / 디버그) chạy nhưng bản phát hành (release / 릴리스) crash”, “flavor A có permission mà flavor B không có”, “CI bản dựng (build / 빌드) khác cục bộ (local / 로컬)”, hoặc “thay một tệp (file / 파일) nhưng Gradle rebuild nửa repository”.

Mục tiêu chapter này là tạo mô hình tư duy (mental model / 사고 모델) để đọc và thiết kế bản dựng (build / 빌드), không phải thuộc mọi thuộc tính (property / 속성) của AGP DSL.

## 1. Ba lớp phải phân biệt: Gradle, Android Gradle Plugin và Kotlin plugin

**Gradle** là general bản dựng (build / 빌드) engine. Nó quản lý dự án (project / 프로젝트), plugin, tác vụ (task / 작업) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성) resolution, bộ nhớ đệm (cache / 캐시), cấu hình (configuration / 구성) phase và thực thi (execution / 실행) phase. Gradle không tự hiểu Activity, AndroidManifest hay tài nguyên (resource / 자원) Android.

**Android Gradle Plugin — AGP** bổ sung Android-specific mô hình (model / 모델) vào Gradle. Nó hiểu `android {}`, `compileSdk`, `defaultConfig`, bản dựng (build / 빌드) types, sản phẩm (product / 제품) flavors, nguồn (source / 소스) sets, manifest merger, Android resources, D8/R8, signing, APK/AAB packaging và kiểm thử (test / 테스트) variants.

**Kotlin Gradle Plugin** chịu trách nhiệm Kotlin compilation, trình biên dịch (compiler / 컴파일러) options và phần Kotlin-specific toolchain. Compose trình biên dịch (compiler / 컴파일러), KSP và các trình biên dịch (compiler / 컴파일러) plugin khác lại là những lớp riêng gắn vào chuỗi xử lý (pipeline / 파이프라인) này.

Khi bản dựng (build / 빌드) thất bại (fail / 실패), trước tiên cần xác định thất bại (failure / 실패) thuộc lớp nào. phụ thuộc (dependency / 의존성) resolution lỗi (error / 오류) khác AGP variant cấu hình (configuration / 구성) lỗi (error / 오류); Kotlin trình biên dịch (compiler / 컴파일러) lỗi (error / 오류) khác R8 missing-class lỗi (error / 오류). Gom mọi lỗi thành “Gradle lỗi” khiến gỡ lỗi (debug / 디버그) chậm hơn nhiều.

> **Chuyển mạch:** Gradle, AGP và Kotlin plugin tạo ba lớp tooling; settings/root/module build scopes tiếp theo giải thích vì sao `compileSdk`, `minSdk` và `targetSdk` có semantics khác nhau.

## 2. Settings, gốc (root / 루트) bản dựng (build / 빌드) và mô-đun (module / 모듈) bản dựng (build / 빌드) có vai trò khác nhau

`settings.gradle.kts` xác định dự án (project / 프로젝트) đồ thị (graph / 그래프) ở cấp repository: mô-đun (module / 모듈) nào được include, plugin/phụ thuộc (dependency / 의존성) repository nào được dùng, phiên bản (version / 버전) danh mục (catalog / 카탈로그) nào được import và đôi khi composite bản dựng (build / 빌드)/build-logic nào được gắn vào.

Gốc (root / 루트) `build.gradle.kts` ngày nay nên nhẹ. Nó thường khai báo plugin versions bằng `apply false`, hoặc rất ít cross-project cấu hình (configuration / 구성). Nhét mọi cấu hình (configuration / 구성) vào gốc (root / 루트) bản dựng (build / 빌드) tệp (file / 파일) tạo hidden coupling và làm cấu hình (configuration / 구성) phase khó tối ưu.

Mỗi mô-đun (module / 모듈) có `build.gradle.kts` riêng. Android ứng dụng (application / 애플리케이션) mô-đun (module / 모듈) thường dùng `com.android.application`; reusable Android thư viện (library / 라이브러리) dùng `com.android.library`; pure Kotlin mô-đun (module / 모듈) có thể chỉ dùng Kotlin/JVM; động (dynamic / 동적) tính năng (feature / 기능) dùng plugin riêng. Plugin quyết định mô-đun (module / 모듈) mô hình (model / 모델) và tác vụ (task / 작업) đồ thị (graph / 그래프) nào tồn tại.

Một ranh giới mô-đun (module boundary / 모듈 경계) tốt vì thế không chỉ là gói (package / 패키지) organization. Nó là **bản dựng (build / 빌드) ranh giới (boundary / 경계)**: phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), compilation đơn vị (unit / 단위), API công khai (public API / 공개 API) surface và bộ nhớ đệm (cache / 캐시) ranh giới (boundary / 경계).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **3. compileSdk, minSdk, targetSdk không phải ba cách viết cùng một phiên bản (version / 버전)** tiếp nhận điểm tựa từ **2. Settings, gốc (root / 루트) bản dựng (build / 빌드) và mô-đun (module / 모듈) bản dựng (build / 빌드) có vai trò khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. bản dựng (build / 빌드) kiểu (type / 타입) giải quyết môi trường (environment / 환경)/bản dựng (build / 빌드) hành vi (behavior / 동작), sản phẩm (product / 제품) flavor giải quyết sản phẩm (product / 제품) dimension** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. `compileSdk`, `minSdk`, `targetSdk` không phải ba cách viết cùng một phiên bản (version / 버전)

`compileSdk` quyết định bộ Android API mà mã nguồn (source code / 소스 코드) được phép compile against. Tăng `compileSdk` cho phép gọi API mới nhưng tự nó không nói app sẽ chạy trên phiên bản (version / 버전) nào.

`minSdk` là OS thấp nhất app hỗ trợ. Nếu `minSdk = 26`, app không được cài trên API thấp hơn 26. Mọi mã (code / 코드) gọi API mới hơn minSdk phải được guard hoặc được thư viện (library / 라이브러리)/desugaring lớp trừu tượng (abstraction / 추상화) xử lý phù hợp.

`targetSdk` là lời tuyên bố app đã được kiểm thử theo hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약) của Android phiên bản (version / 버전) tương ứng. Nhiều breaking hành vi (behavior / 동작) changes chỉ bật khi app tăng mục tiêu (target / 대상) SDK. Vì vậy tăng mục tiêu (target / 대상) SDK là di chuyển (migration / 마이그레이션) dự án (project / 프로젝트), không nên xem như sửa một con số để upload Play Console.

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

Con số trên chỉ là ví dụ cấu trúc. dự án (project / 프로젝트) thật phải dùng tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬) và chính sách (policy / 정책) hiện hành thay vì bản sao (copy / 복사) cứng từ tài liệu học.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **4. bản dựng (build / 빌드) kiểu (type / 타입) giải quyết môi trường (environment / 환경)/bản dựng (build / 빌드) hành vi (behavior / 동작), sản phẩm (product / 제품) flavor giải quyết sản phẩm (product / 제품) dimension** tiếp nhận điểm tựa từ **3. compileSdk, minSdk, targetSdk không phải ba cách viết cùng một phiên bản (version / 버전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. nguồn (source / 소스) set precedence là nguyên nhân của rất nhiều “mystery hành vi (behavior / 동작)”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. bản dựng (build / 빌드) kiểu (type / 타입) giải quyết môi trường (environment / 환경)/bản dựng (build / 빌드) hành vi (behavior / 동작), sản phẩm (product / 제품) flavor giải quyết sản phẩm (product / 제품) dimension

Bản dựng (build / 빌드) kiểu (type / 타입) thường biểu diễn cách sản phẩm tạo ra (artifact / 산출물) được bản dựng (build / 빌드): `debug`, `release`, đôi khi `benchmark` hoặc `staging`. Nó điều khiển các concern như debuggable, minification, signing, suffix, tài nguyên (resource / 자원) giá trị (value / 값) và tối ưu hóa (optimization / 최적화).

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

Sản phẩm (product / 제품) flavor biểu diễn một dimension của sản phẩm. Ví dụ `demo/full`, `internal/public`, hoặc brand/region. Khi có nhiều dimension, cần khai báo `flavorDimensions` rõ ràng.

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

Bản dựng (build / 빌드) variant là cross-product của những lựa chọn đó, ví dụ `demoKrDebug` hoặc `fullGlobalRelease`. Nếu số dimension tăng không kiểm soát, variant explosion sẽ làm IDE sync, CI ma trận (matrix / 행렬) và phụ thuộc (dependency / 의존성) maintenance phức tạp nhanh chóng.

Cấp cao (senior / 시니어) quy tắc (rule / 규칙): chỉ tạo flavor khi khác biệt thực sự là build-time sản phẩm (product / 제품) dimension. cờ tính năng (feature flag / 기능 플래그) thời gian chạy (runtime / 런타임) không nên biến thành flavor chỉ vì “có hai trạng thái”.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **4. bản dựng (build / 빌드) kiểu (type / 타입) giải quyết môi trường (environment / 환경)/bản dựng (build / 빌드) hành vi (behavior / 동작), sản phẩm (product / 제품) flavor giải quyết sản phẩm (product / 제품) dimension** nêu điều cần giải thích; **5. nguồn (source / 소스) set precedence là nguyên nhân của rất nhiều “mystery hành vi (behavior / 동작)”** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. Manifest Merger là build-time composition hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. nguồn (source / 소스) set precedence là nguyên nhân của rất nhiều “mystery hành vi (behavior / 동작)”

Android bản dựng (build / 빌드) có thể lấy nguồn (source / 소스)/tài nguyên (resource / 자원)/manifest từ nhiều nguồn (source / 소스) set. Với một variant kiểu `demoDebug`, Gradle có thể xem `src/demoDebug/`, `src/debug/`, `src/demo/`, rồi `src/main/` theo precedence tương ứng.

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

Tài nguyên (resource / 자원) có cùng tên có thể bị override theo precedence. Manifest cũng được merge theo quy tắc (rule / 규칙) tương tự. Nhưng Kotlin/Java lớp (class / 클래스) trùng fully-qualified name trong hai nguồn (source / 소스) set cùng tham gia variant thường gây duplicate-class lỗi (error / 오류) chứ không phải override như tài nguyên (resource / 자원).

Nguồn (source / 소스) sets rất hữu ích cho fake endpoint, debug-only screen, brand tài nguyên (resource / 자원) hoặc kiểm thử (test / 테스트) hiện thực (implementation / 구현), nhưng lạm dụng sẽ tạo đường đi mã (code path / 코드 경로) khó nhìn thấy bằng tìm kiếm (search / 검색) thông thường.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **5. nguồn (source / 소스) set precedence là nguyên nhân của rất nhiều “mystery hành vi (behavior / 동작)”** nêu điều cần giải thích; **6. Manifest Merger là build-time composition hệ thống (system / 시스템)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. BuildConfig, resValue, manifest placeholder và secret** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Manifest Merger là build-time composition hệ thống (system / 시스템)

Manifest cuối cùng của app không nhất thiết giống `src/main/AndroidManifest.xml`. Nó có thể được merge từ app manifest, bản dựng (build / 빌드) kiểu (type / 타입), flavor và manifests của dependencies.

Điều này giải thích tại sao một SDK có thể thêm permission/provider/dịch vụ (service / 서비스) vào app dù bạn không viết chúng trong main manifest.

Khi có xung đột (conflict / 충돌), dùng Manifest Merger report thay vì đoán. Các `tools:` marker như `tools:replace`, `tools:remove`, `tools:node` có thể giải quyết merge xung đột (conflict / 충돌), nhưng phải hiểu hậu quả bảo mật (security / 보안)/thời gian chạy (runtime / 런타임) của việc override siêu dữ liệu (metadata / 메타데이터) từ phụ thuộc (dependency / 의존성).

Một `android:exported`, provider authority hoặc permission sai trong manifest merged sản phẩm tạo ra (artifact / 산출물) có thể trở thành môi trường vận hành (production / 운영 환경) vulnerability dù nguồn (source / 소스) manifest nhìn có vẻ đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **7. BuildConfig, resValue, manifest placeholder và secret** tiếp nhận điểm tựa từ **6. Manifest Merger là build-time composition hệ thống (system / 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. phụ thuộc (dependency / 의존성) configurations biểu diễn visibility và classpath** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. `BuildConfig`, `resValue`, manifest placeholder và secret

Build-time values có nhiều cơ chế. `buildConfigField` tạo constant trong generated `BuildConfig`; `resValue` tạo Android tài nguyên (resource / 자원); manifest placeholders thay đơn vị từ (token / 토큰) lúc merge manifest.

Không cơ chế nào biến giá trị (value / 값) thành secret. Bất kỳ secret nào ship trong APK/AAB đều có thể bị trích xuất. API key có restriction vẫn có thể tồn tại trong app nếu dịch vụ (service / 서비스) thiết kế cho client-side key, nhưng credential có quyền backend không được nhúng vào bản dựng (build / 빌드) cấu hình (config / 설정).

```kotlin
buildTypes {
    debug {
        buildConfigField("String", "API_BASE_URL", "\"https://staging.example.com\"")
    }
}
```

Bản dựng (build / 빌드) cấu hình (config / 설정) là cấu hình (configuration / 구성) phân phối (distribution / 분포), không phải secure vault.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **7. BuildConfig, resValue, manifest placeholder và secret** xác định đầu vào; **8. phụ thuộc (dependency / 의존성) configurations biểu diễn visibility và classpath** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **9. phiên bản (version / 버전) danh mục (catalog / 카탈로그) giúp centralize coordinates nhưng không thay phụ thuộc (dependency / 의존성) quản trị (governance / 거버넌스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. phụ thuộc (dependency / 의존성) configurations biểu diễn visibility và classpath

`implementation` nói phụ thuộc (dependency / 의존성) cần để compile mô-đun (module / 모듈) hiện tại nhưng không được expose như công khai (public / 공개) transitive API cho bên tiêu thụ (consumer / 소비자).

`api` trong thư viện (library / 라이브러리) mô-đun (module / 모듈) expose phụ thuộc (dependency / 의존성) qua API công khai (public API / 공개 API) surface. Dùng `api` quá nhiều tăng coupling và recompilation cascade.

`compileOnly` cần khi compile nhưng không gói (package / 패키지) thời gian chạy (runtime / 런타임) hiện thực (implementation / 구현). `runtimeOnly` ngược lại: thời gian chạy (runtime / 런타임) cần nhưng compile mã (code / 코드) không trực tiếp tham chiếu (reference / 참조). kiểm thử (test / 테스트) nguồn (source / 소스) sets có `testImplementation`, `androidTestImplementation`, v.v.

Một heuristic tốt là mặc định `implementation`, chỉ dùng `api` khi API công khai (public API / 공개 API) của mô-đun (module / 모듈) thật sự để lộ kiểu (type / 타입) của phụ thuộc (dependency / 의존성) đó.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **8. phụ thuộc (dependency / 의존성) configurations biểu diễn visibility và classpath** xác định đầu vào; **9. phiên bản (version / 버전) danh mục (catalog / 카탈로그) giúp centralize coordinates nhưng không thay phụ thuộc (dependency / 의존성) quản trị (governance / 거버넌스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **10. Convention plugin tốt hơn copy-paste Gradle khối (block / 블록)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. phiên bản (version / 버전) danh mục (catalog / 카탈로그) giúp centralize coordinates nhưng không thay phụ thuộc (dependency / 의존성) quản trị (governance / 거버넌스)

`libs.versions.toml` giúp định danh phụ thuộc (dependency / 의존성)/plugin bằng alias nhất quán.

```toml
[versions]
kotlin = "..."
coroutines = "..."

[libraries]
coroutines-core = { module = "org.jetbrains.kotlinx:kotlinx-coroutines-core", version.ref = "coroutines" }

[plugins]
android-application = { id = "com.android.application", version = "..." }
```

Phiên bản (version / 버전) danh mục (catalog / 카탈로그) không tự đảm bảo tính tương thích (compatibility / 호환성), license, vulnerability hay reproducibility. Những concern đó cần phụ thuộc (dependency / 의존성) locking, xác minh (verification / 확인), SBOM/vulnerability scanning và upgrade chính sách (policy / 정책) riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **10. Convention plugin tốt hơn copy-paste Gradle khối (block / 블록)** tiếp nhận điểm tựa từ **9. phiên bản (version / 버전) danh mục (catalog / 카탈로그) giúp centralize coordinates nhưng không thay phụ thuộc (dependency / 의존성) quản trị (governance / 거버넌스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Gradle cấu hình (configuration / 구성) phase và thực thi (execution / 실행) phase** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Convention plugin tốt hơn copy-paste Gradle khối (block / 블록)

Khi nhiều mô-đun (module / 모듈) lặp cùng compile options, lint, Compose cấu hình (config / 설정) hoặc kiểm thử (test / 테스트) dependencies, copy-paste khiến cấu hình (configuration / 구성) drift. **Convention plugin** gom chính sách (policy / 정책) bản dựng (build / 빌드) thành mã (code / 코드)/plugin dùng lại.

Thay vì mỗi mô-đun (module / 모듈) tự viết 50 dòng:

```kotlin
plugins {
    id("company.android.library")
}
```

Convention plugin có thể áp AGP/Kotlin plugin, configure không gian tên (namespace / 네임스페이스) chính sách (policy / 정책), Java toolchain, trình biên dịch (compiler / 컴파일러) options, lint, Compose, kiểm thử (test / 테스트) defaults và dùng chung (common / 공통) dependencies.

Điểm quan trọng là convention plugin chứa **convention**, không chứa mọi business-specific phụ thuộc (dependency / 의존성). Nếu plugin trở thành một toàn cục (global / 전역) god đối tượng (object / 객체), mọi mô-đun (module / 모듈) lại coupled theo cách khác.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **11. Gradle cấu hình (configuration / 구성) phase và thực thi (execution / 실행) phase** tiếp nhận điểm tựa từ **10. Convention plugin tốt hơn copy-paste Gradle khối (block / 블록)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Incremental bản dựng (build / 빌드) phụ thuộc đầu vào (input / 입력)/đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Gradle cấu hình (configuration / 구성) phase và thực thi (execution / 실행) phase

Gradle trước tiên cấu hình (configuration / 구성) dự án (project / 프로젝트) và tạo tác vụ (task / 작업) đồ thị (graph / 그래프), sau đó mới execute những tác vụ (task / 작업) cần thiết. cấu hình (configuration / 구성) quá nặng làm mọi command chậm, kể cả tác vụ (task / 작업) nhỏ.

Các mẫu (pattern / 패턴) như eager tác vụ (task / 작업) creation, đọc tệp (file / 파일)/mạng (network / 네트워크) trong cấu hình (configuration / 구성), `afterEvaluate` tùy tiện hoặc toàn cục (global / 전역) cross-project mutation làm bản dựng (build / 빌드) khó bộ nhớ đệm (cache / 캐시) và khó parallelize.

Cấu hình (configuration / 구성) bộ nhớ đệm (cache / 캐시) cố tái sử dụng kết quả cấu hình (configuration / 구성) giữa các bản dựng (build / 빌드) khi plugin/tác vụ (task / 작업) compatible. bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시) tái sử dụng tác vụ (task / 작업) đầu ra (output / 출력) khi đầu vào (input / 입력) fingerprint giống. Hai bộ nhớ đệm (cache / 캐시) giải quyết hai phase khác nhau.

Cấp cao (senior / 시니어) gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) hiệu năng (performance / 성능) nên bắt đầu bằng đo lường (measurement / 측정): Gradle bản dựng (build / 빌드) Scan/profile, tác vụ (task / 작업) timing, bộ nhớ đệm (cache / 캐시) hit/miss, đường găng (critical path / 임계 경로), annotation/mã (code / 코드) generation chi phí (cost / 비용). Không tối ưu chỉ vì thấy “nhiều mô-đun (module / 모듈)”.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **12. Incremental bản dựng (build / 빌드) phụ thuộc đầu vào (input / 입력)/đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **11. Gradle cấu hình (configuration / 구성) phase và thực thi (execution / 실행) phase** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Toolchain và JVM mục tiêu (target / 대상) phải được hiểu là tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Incremental bản dựng (build / 빌드) phụ thuộc đầu vào (input / 입력)/đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약)

Một tác vụ (task / 작업) cacheable/incremental cần khai báo đầu vào (input / 입력)/đầu ra (output / 출력) chính xác. Plugin custom hoặc codegen đọc tệp (file / 파일) ngoài mô hình (model / 모델) có thể khiến bản dựng (build / 빌드) không reproducible hoặc bộ nhớ đệm (cache / 캐시) trả kết quả sai.

KSP thường được chọn thay KAPT trong ecosystem hiện đại khi processor hỗ trợ (support / 지원), một phần vì mã (code / 코드) generation mô hình (model / 모델) phù hợp Kotlin hơn và có thể giảm overhead so với Java annotation-processing chuỗi xử lý (pipeline / 파이프라인). Tuy nhiên di chuyển (migration / 마이그레이션) phải dựa processor thực tế; không phải mọi KAPT processor đều có replacement KSP tương đương.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **13. Toolchain và JVM mục tiêu (target / 대상) phải được hiểu là tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **12. Incremental bản dựng (build / 빌드) phụ thuộc đầu vào (input / 입력)/đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Android Components / Variant API dành cho plugin và bản dựng (build / 빌드) lô-gic (logic / 논리) nâng cao** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Toolchain và JVM mục tiêu (target / 대상) phải được hiểu là tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약)

JDK chạy Gradle/AGP, Java/Kotlin ngôn ngữ (language / 언어) mức (level / 수준) và bytecode/JVM mục tiêu (target / 대상) là các khái niệm khác nhau. dự án (project / 프로젝트) có thể dùng một JDK để chạy bản dựng (build / 빌드) nhưng compile nguồn (source / 소스) với mục tiêu (target / 대상) khác.

Java toolchain giúp bản dựng (build / 빌드) thống nhất giữa cục bộ (local / 로컬) và CI:

```kotlin
kotlin {
    jvmToolchain(17)
}
```

Con số cần theo tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬) của Kotlin/AGP/dự án (project / 프로젝트). Không nên upgrade JDK, Gradle, AGP, Kotlin và Compose trình biên dịch (compiler / 컴파일러) cùng lúc mà không có kiểm thử (test / 테스트) ma trận (matrix / 행렬) vì khi thất bại (fail / 실패) rất khó xác định tầng (layer / 계층) gây regression.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **14. Android Components / Variant API dành cho plugin và bản dựng (build / 빌드) lô-gic (logic / 논리) nâng cao** tiếp nhận điểm tựa từ **13. Toolchain và JVM mục tiêu (target / 대상) phải được hiểu là tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. tài nguyên (resource / 자원) processing, D8, R8 và packaging chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Android Components / Variant API dành cho plugin và bản dựng (build / 빌드) lô-gic (logic / 논리) nâng cao

AGP có variant-oriented API để đọc hoặc biến đổi sản phẩm tạo ra (artifact / 산출물)/tác vụ (task / 작업) cấu hình (configuration / 구성) theo variant mà không dựa nội bộ (internal / 내부) API không ổn định. Đây là hướng đúng khi viết plugin bản dựng (build / 빌드) hoặc instrumentation lô-gic (logic / 논리) tùy variant.

Anti-pattern phổ biến là script truy cập tác vụ (task / 작업) name bằng string, `afterEvaluate`, hoặc nội bộ (internal / 내부) AGP classes. Cách này thường vỡ khi upgrade AGP.

Nếu custom bản dựng (build / 빌드) lô-gic (logic / 논리) cần biết variant, hãy ưu tiên công khai (public / 공개) AGP Variant API và sản phẩm tạo ra (artifact / 산출물) API của phiên bản (version / 버전) đang dùng.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **14. Android Components / Variant API dành cho plugin và bản dựng (build / 빌드) lô-gic (logic / 논리) nâng cao** nêu điều cần giải thích; **15. tài nguyên (resource / 자원) processing, D8, R8 và packaging chuỗi xử lý (pipeline / 파이프라인)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. bên tiêu thụ (consumer / 소비자) ProGuard rules của thư viện (library / 라이브러리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. tài nguyên (resource / 자원) processing, D8, R8 và packaging chuỗi xử lý (pipeline / 파이프라인)

Một mô hình tư duy (mental model / 사고 모델) đơn giản:

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

Chuỗi xử lý (pipeline / 파이프라인) thật chi tiết hơn, nhưng mô hình (model / 모델) này giúp xác định lỗi nằm ở compile, bytecode transform, shrinker hay packaging.

Gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) thường ít tối ưu hóa (optimization / 최적화) hơn nên reflection bug hoặc missing keep quy tắc (rule / 규칙) chỉ xuất hiện ở bản phát hành (release / 릴리스). Vì vậy “gỡ lỗi (debug / 디버그) app chạy” không chứng minh bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **15. tài nguyên (resource / 자원) processing, D8, R8 và packaging chuỗi xử lý (pipeline / 파이프라인)** nêu điều cần giải thích; **16. bên tiêu thụ (consumer / 소비자) ProGuard rules của thư viện (library / 라이브러리)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. Signing cấu hình (config / 설정) và bản dựng (build / 빌드) credentials** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. bên tiêu thụ (consumer / 소비자) ProGuard rules của thư viện (library / 라이브러리)

Android thư viện (library / 라이브러리) có thể cần cung cấp `consumerProguardFiles` để quy tắc (rule / 규칙) cần thiết được merge vào app bên tiêu thụ (consumer / 소비자) khi R8 chạy.

Thư viện (library / 라이브러리) author không nên bắt app bên tiêu thụ (consumer / 소비자) đoán reflection/JNI quy tắc (rule / 규칙) bên trong SDK. Ngược lại, keep quy tắc (rule / 규칙) quá rộng như giữ toàn bộ gói (package / 패키지) làm giảm lợi ích shrinker cho mọi app dùng thư viện (library / 라이브러리).

Quy tắc (rule / 규칙) tốt phải càng hẹp càng tốt và đi cùng kiểm thử (test / 테스트) minified bên tiêu thụ (consumer / 소비자) sản phẩm tạo ra (artifact / 산출물).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **17. Signing cấu hình (config / 설정) và bản dựng (build / 빌드) credentials** tiếp nhận điểm tựa từ **16. bên tiêu thụ (consumer / 소비자) ProGuard rules của thư viện (library / 라이브러리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Reproducible bản dựng (build / 빌드) và supply-chain thinking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Signing cấu hình (config / 설정) và bản dựng (build / 빌드) credentials

Gỡ lỗi (debug / 디버그) signing key có thể generated/cục bộ (local / 로컬). bản phát hành (release / 릴리스) signing key là môi trường vận hành (production / 운영 환경) định danh (identity / 식별자) và cần được quản lý như credential quan trọng. Không lần ghi nhận (commit / 커밋) keystore/password vào Git.

CI nên lấy signing material từ secret manager/secure môi trường (environment / 환경), hạn chế quyền truy cập và kiểm tra (audit / 감사) usage. Nếu dùng Play App Signing, vẫn cần hiểu upload key khác app signing key về vai trò và khôi phục (recovery / 복구) tiến trình (process / 프로세스).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **18. Reproducible bản dựng (build / 빌드) và supply-chain thinking** tiếp nhận điểm tựa từ **17. Signing cấu hình (config / 설정) và bản dựng (build / 빌드) credentials** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. bản dựng (build / 빌드) hiệu năng (performance / 성능): tránh cả hai cực đoan** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Reproducible bản dựng (build / 빌드) và supply-chain thinking

Hai bản dựng (build / 빌드) từ cùng lần ghi nhận (commit / 커밋) ideally phải cho hành vi (behavior / 동작) tương đương và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) có thể giải thích được. động (dynamic / 동적) versions kiểu `1.+`, repository không kiểm soát, plugin tải sản phẩm tạo ra (artifact / 산출물) bất định hoặc script phụ thuộc mạng (network / 네트워크) mutable đều làm reproducibility kém.

Môi trường vận hành (production / 운영 환경) bản dựng (build / 빌드) quản trị (governance / 거버넌스) nên theo dõi:

- nguồn (source / 소스) lần ghi nhận (commit / 커밋);
- toolchain versions;
- resolved phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프);
- signing định danh (identity / 식별자);
- bản dựng (build / 빌드) flags/variant;
- generated SBOM nếu tổ chức yêu cầu;
- sản phẩm tạo ra (artifact / 산출물) checksum;
- ánh xạ (mapping / 매핑) tệp (file / 파일) của R8;
- provenance từ CI.

Mục tiêu không phải bureaucracy mà là khả năng trả lời “nhị phân (binary / 이진) đang chạy ngoài môi trường vận hành (production / 운영 환경) được bản dựng (build / 빌드) từ cái gì?”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **19. bản dựng (build / 빌드) hiệu năng (performance / 성능): tránh cả hai cực đoan** tiếp nhận điểm tựa từ **18. Reproducible bản dựng (build / 빌드) và supply-chain thinking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. CI ma trận (matrix / 행렬) theo variant phải có chủ đích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. bản dựng (build / 빌드) hiệu năng (performance / 성능): tránh cả hai cực đoan

Một monolith mô-đun (module / 모듈) có thể compile chậm và mọi thay đổi invalidate quá nhiều mã (code / 코드). Nhưng hàng trăm mô-đun (module / 모듈) micro-granular cũng làm cấu hình (configuration / 구성)/phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) phức tạp.

Mô-đun (module / 모듈) hóa vì ranh giới (boundary / 경계) có giá trị: quyền sở hữu (ownership / 소유권), parallel công việc (work / 작업), API isolation, testability, bản dựng (build / 빌드) isolation hoặc tính năng (feature / 기능) delivery. Không mô-đun (module / 모듈) hóa chỉ để số mô-đun (module / 모듈) lớn.

Những hướng tối ưu thường có impact thực tế hơn micro-tweak:

- giảm `api` surface;
- tránh annotation processor nặng không cần thiết;
- bật/correct bộ nhớ đệm (cache / 캐시);
- dùng convention plugin;
- bỏ cấu hình (configuration / 구성) side tác động (effect / 효과);
- tránh generated mã (code / 코드) invalidating quá rộng;
- tách tính năng (feature / 기능) có churn độc lập;
- profile CI đường găng (critical path / 임계 경로).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **20. CI ma trận (matrix / 행렬) theo variant phải có chủ đích** tiếp nhận điểm tựa từ **19. bản dựng (build / 빌드) hiệu năng (performance / 성능): tránh cả hai cực đoan** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Các lỗi thường gặp và cách suy luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. CI ma trận (matrix / 행렬) theo variant phải có chủ đích

Nếu dự án (project / 프로젝트) có 20 variants, kiểm thử (test / 테스트) toàn bộ ở mọi lần ghi nhận (commit / 커밋) có thể quá đắt. Nhưng chỉ kiểm thử (test / 테스트) `debug` cũng không đủ.

Một chiến lược thường hợp lý:

- PR: compile/lint/đơn vị (unit / 단위) kiểm thử (test / 테스트) representative variants;
- main/nightly: mở rộng variant/thiết bị (device / 장치) ma trận (matrix / 행렬);
- bản phát hành (release / 릴리스): bản dựng (build / 빌드) đúng môi trường vận hành (production / 운영 환경) variant, minified, signed-like chuỗi xử lý (pipeline / 파이프라인), instrumentation/trọng yếu (critical / 중요) smoke kiểm thử (test / 테스트);
- flavor có hành vi (behavior / 동작) riêng phải có kiểm thử (test / 테스트) riêng, không chỉ rely dùng chung (common / 공통) gỡ lỗi (debug / 디버그).

CI ma trận (matrix / 행렬) phải phản ánh rủi ro (risk / 위험) chứ không phản ánh số variant một cách máy móc.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **21. Các lỗi thường gặp và cách suy luận** tiếp nhận điểm tựa từ **20. CI ma trận (matrix / 행렬) theo variant phải có chủ đích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. cấp cao (senior / 시니어) checklist cho build-system thay đổi (change / 변경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Các lỗi thường gặp và cách suy luận

### Gỡ lỗi (debug / 디버그) chạy, bản phát hành (release / 릴리스) crash

Kiểm tra R8 keep rules, reflection/serialization, JNI symbol, release-only cấu hình (config / 설정), signing/mạng (network / 네트워크) bảo mật (security / 보안) cấu hình (config / 설정), tài nguyên (resource / 자원) shrinking và đường đi mã (code path / 코드 경로) bản dựng (build / 빌드) kiểu (type / 타입).

### Một flavor có tài nguyên (resource / 자원) sai

Kiểm tra source-set precedence, flavor dimension thứ tự (order / 순서) và tài nguyên (resource / 자원) merger đầu ra (output / 출력).

### Permission “tự nhiên xuất hiện” trong manifest

Mở merged manifest và tìm manifest từ phụ thuộc (dependency / 의존성) nào thêm permission/thành phần (component / 컴포넌트).

### Cục bộ (local / 로컬) bản dựng (build / 빌드) được, CI thất bại (fail / 실패)

Kiểm tra JDK/toolchain, phụ thuộc (dependency / 의존성) repository, case-sensitive filesystem, uncommitted generated/cục bộ (local / 로컬) tệp (file / 파일), môi trường (environment / 환경) variable và cached trạng thái (state / 상태).

### Bản dựng (build / 빌드) chậm sau khi thêm processor/plugin

Đo tác vụ (task / 작업) đồ thị (graph / 그래프), processor thời gian (time / 시간) và cacheability trước khi refactor cấu trúc dự án (project structure / 프로젝트 구조).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, **22. cấp cao (senior / 시니어) checklist cho build-system thay đổi (change / 변경)** tiếp nhận điểm tựa từ **21. Các lỗi thường gặp và cách suy luận** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Official references** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. cấp cao (senior / 시니어) checklist cho build-system thay đổi (change / 변경)

Khi rà soát (review / 검토) thay đổi bản dựng (build / 빌드), hãy hỏi: thay đổi áp dụng variant nào; có thay manifest/tài nguyên (resource / 자원) precedence không; công khai (public / 공개) phụ thuộc (dependency / 의존성) surface có tăng không; có ảnh hưởng bản phát hành (release / 릴리스)/minified sản phẩm tạo ra (artifact / 산출물) không; có làm cấu hình (configuration / 구성) bộ nhớ đệm (cache / 캐시) mất hiệu lực không; CI có bản dựng (build / 빌드) đúng variant mới không; secret/signing có bị đưa vào nguồn (source / 소스) không; và quay lui (rollback / 롤백) toolchain có còn khả thi nếu upgrade thất bại (fail / 실패) không.

Hệ thống dựng (build system / 빌드 시스템) là môi trường vận hành (production / 운영 환경) mã (code / 코드). Một lỗi bản dựng (build / 빌드) cấu hình (configuration / 구성) có thể không xuất hiện trong đơn vị (unit / 단위) kiểm thử (test / 테스트) nhưng vẫn thay permission, signing, tài nguyên (resource / 자원), shrinker hoặc sản phẩm tạo ra (artifact / 산출물) được ship tới hàng triệu thiết bị (device / 장치).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 15 — Gradle, Android Gradle Plugin và bản dựng (build / 빌드) Variant mô hình (model / 모델)**, sau nội dung của **22. cấp cao (senior / 시니어) checklist cho build-system thay đổi (change / 변경)**, **23. Official references** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 23. Official references
Phần này nối mạch Android vừa học với “23. Official references”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

- Android bản dựng (build / 빌드) overview: https://nhà phát triển (developer / 개발자).android.com/bản dựng (build / 빌드)
- bản dựng (build / 빌드) variants and nguồn (source / 소스) sets: https://nhà phát triển (developer / 개발자).android.com/bản dựng (build / 빌드)/build-variants
- Gradle tips: https://nhà phát triển (developer / 개발자).android.com/bản dựng (build / 빌드)/gradle-tips
- Android Gradle Plugin APIs: https://nhà phát triển (developer / 개발자).android.com/tham chiếu (reference / 참조)/tools/gradle-api

Đọc reference theo version AGP đang dùng; không giả định DSL/internal behavior của một version cũ vẫn đúng với version mới.

> **Bàn giao:** Sau **23. Official references**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
