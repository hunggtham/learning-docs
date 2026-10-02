# Độ sâu (depth / 깊이) Lab 08 — Kotlin + Android phiên bản (version / 버전) tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션) và Upgrade Forensics

> **Mạch đọc:** [README](./README.md) là owner của **Độ sâu (depth / 깊이) Lab 08 — Kotlin + Android phiên bản (version / 버전) tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션) và Upgrade Forensics**; đặt lab sau version evolution và trước build/release forensics. Từ **1. phiên bản (version / 버전) không phải một con số — nó là tập hợp các đặc tả hợp đồng (contract / 계약)** nối source/API/compiler/K2/bytecode/runtime/toolchain và consumer evidence, rồi điều tra thay đổi theo đồ thị contract thay vì chỉ nhìn số version.

Tệp (file / 파일) `05_kotlin_android_version_evolution.md` trả lời câu hỏi **Kotlin và Android đã tiến hóa như thế nào theo thời gian**. độ sâu (depth / 깊이) Lab này đi thêm một tầng: **vì sao một thay đổi phiên bản (version / 버전) có thể làm bản dựng (build / 빌드), nhị phân (binary / 이진), generated mã (code / 코드) hoặc hành vi thời gian chạy (runtime behavior / 런타임 동작) hỏng dù mã nguồn (source code / 소스 코드) gần như không đổi**.

Mục tiêu không phải học thuộc tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬). Mục tiêu là nhìn một Android dự án (project / 프로젝트) như một **đồ thị đặc tả hợp đồng (contract / 계약) theo phiên bản (version / 버전)** và biết cách điều tra khi một nút (node / 노드) trong đồ thị thay đổi.

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

Song song với đó là bản dựng (build / 빌드) đồ thị (graph / 그래프):

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

Khi upgrade, lỗi thường xuất hiện ở **ranh giới (boundary / 경계) giữa hai nút (node / 노드)**, không nằm đơn giản trong một con số phiên bản (version / 버전).

---

## 1. phiên bản (version / 버전) không phải một con số — nó là tập hợp các đặc tả hợp đồng (contract / 계약)

Một dự án (project / 프로젝트) có thể đồng thời có:

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

Nếu không phân biệt các đặc tả hợp đồng (contract / 계약) này, nhà phát triển (developer / 개발자) thường gỡ lỗi (debug / 디버그) theo kiểu:

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

# 2. bản phát hành (release / 릴리스) channel cũng là một phần của tính tương thích (compatibility / 호환성)

Không phải phiên bản (version / 버전) nào có số lớn hơn cũng có cùng mức guarantee.

Ta cần phân biệt:

```text
EAP / Early Access
Beta / Preview
RC / Release Candidate
Stable
Deprecated
Removed
```

Một dự án (project / 프로젝트) môi trường vận hành (production / 운영 환경) dùng Stable surface có upgrade rủi ro (risk / 위험) khác hoàn toàn một dự án (project / 프로젝트) phụ thuộc nhiều vào:

```text
-X compiler flags
experimental language feature
unstable compiler plugin API
preview Android behavior
alpha Jetpack library
internal annotation processor contract
```

Do đó trước upgrade cần inventory không chỉ phiên bản (version / 버전) mà cả **stability mức (level / 수준)** của tính năng (feature / 기능) đang dùng.

Một codebase có thể ở Kotlin Stable nhưng vẫn có upgrade rủi ro (risk / 위험) cao vì trình biên dịch (compiler / 컴파일러) plugin hoặc thư viện (library / 라이브러리) đang Alpha.

---

# 3. Kotlin bản phát hành (release / 릴리스) phiên bản (version / 버전), `languageVersion` và `apiVersion` tạo ba đặc tả hợp đồng (contract / 계약) khác nhau

Giả sử trình biên dịch (compiler / 컴파일러) là Kotlin 2.4 nhưng thư viện (library / 라이브러리) muốn giữ bên tiêu thụ (consumer / 소비자) tính tương thích (compatibility / 호환성) thấp hơn.

```kotlin
kotlin {
    compilerOptions {
        languageVersion.set(KotlinVersion.KOTLIN_2_4)
        apiVersion.set(KotlinVersion.KOTLIN_2_1)
    }
}
```

Mô hình tư duy (mental model / 사고 모델):

```text
compiler version
= compiler implementation đang chạy

languageVersion
= syntax/semantic language được phép dùng

apiVersion
= stdlib API tối đa source được phép gọi
```

`apiVersion` không được cao hơn `languageVersion`.

Điểm sâu hơn là: **giảm `apiVersion` không tự động biến mọi sản phẩm tạo ra (artifact / 산출물) thành tương thích với bên tiêu thụ (consumer / 소비자) cũ**.

Nó chỉ giúp tránh gọi stdlib API quá mới. nhị phân (binary / 이진) siêu dữ liệu (metadata / 메타데이터), JVM mục tiêu (target / 대상), trình biên dịch (compiler / 컴파일러) plugin đầu ra (output / 출력) và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) vẫn có thể yêu cầu toolchain mới hơn.

---

# 4. Kotlin siêu dữ liệu (metadata / 메타데이터) — tính tương thích (compatibility / 호환성) tầng (layer / 계층) thường bị bỏ qua

Kotlin/JVM sản phẩm tạo ra (artifact / 산출물) không chỉ chứa JVM bytecode. Kotlin trình biên dịch (compiler / 컴파일러) còn ghi **Kotlin siêu dữ liệu (metadata / 메타데이터)** để trình biên dịch (compiler / 컴파일러) khác hiểu những ngữ nghĩa (semantic / 의미적) mà bytecode Java thuần không diễn đạt đầy đủ.

Siêu dữ liệu (metadata / 메타데이터) có thể chứa thông tin về:

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

Vì vậy một JAR/AAR có thể nhìn bằng JVM như “lớp (class / 클래스) hợp lệ”, nhưng Kotlin trình biên dịch (compiler / 컴파일러) bên tiêu thụ (consumer / 소비자) vẫn từ chối vì siêu dữ liệu (metadata / 메타데이터) phiên bản (version / 버전) quá mới hoặc pre-release.

Đây là lý do lỗi kiểu:

```text
Module was compiled with an incompatible version of Kotlin
The binary version of its metadata is ...
Expected version is ...
```

không nên được xử lý bằng cách ngẫu nhiên thêm trình biên dịch (compiler / 컴파일러) flag cho qua.

Câu hỏi đúng là:

```text
producer dùng compiler nào?
consumer dùng compiler nào?
metadata version nào được producer ghi ra?
consumer compiler có support không?
```

---

> **Chuyển mạch:** Version là tập contract, không chỉ bytecode; “chạy được” chưa chứng minh metadata, ABI, target hoặc compiler-plugin compatibility, nên toolchain evidence phải được truy vết riêng.

## 4.1 Vì sao “bytecode chạy được” chưa đủ?

Java trình biên dịch (compiler / 컴파일러) có thể nhìn bytecode theo một đặc tả hợp đồng (contract / 계약) khác Kotlin trình biên dịch (compiler / 컴파일러).

Ví dụ thư viện (library / 라이브러리) Kotlin API công khai (public API / 공개 API) sử dụng:

```kotlin
suspend fun load(): Result<User>
```

Bytecode JVM cuối cùng không giữ nguyên cú pháp (syntax / 문법) `suspend` như nguồn (source / 소스). Kotlin siêu dữ liệu (metadata / 메타데이터) giúp trình biên dịch (compiler / 컴파일러) bên tiêu thụ (consumer / 소비자) tái dựng Kotlin-level API.

Do đó tính tương thích (compatibility / 호환성) Kotlin thư viện (library / 라이브러리) phải xét ít nhất:

```text
JVM bytecode compatibility
+
Kotlin metadata compatibility
+
stdlib/API compatibility
```

---

# 5. Pre-release trình biên dịch (compiler / 컴파일러) sản phẩm tạo ra (artifact / 산출물) có rủi ro riêng

Một thư viện (library / 라이브러리) bản dựng (build / 빌드) bằng trình biên dịch (compiler / 컴파일러) EAP/RC có thể tạo sản phẩm tạo ra (artifact / 산출물) mà stable bên tiêu thụ (consumer / 소비자) không đọc như sản phẩm tạo ra (artifact / 산출물) stable thông thường.

Vì vậy môi trường vận hành (production / 운영 환경) thư viện (library / 라이브러리) không nên publish sản phẩm tạo ra (artifact / 산출물) pre-release vào channel stable chỉ vì cục bộ (local / 로컬) app compile thành công.

Nên tách:

```text
internal experiment repository
pre-release coordinates
stable production coordinates
```

Nếu organization có nhiều app bên tiêu thụ (consumer / 소비자), một sản phẩm tạo ra (artifact / 산출물) pre-release có thể làm cả phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) bị kéo sang toolchain thử nghiệm.

---

# 6. JVM mục tiêu (target / 대상) mismatch — lỗi phiên bản (version / 버전) nhìn giống bản dựng (build / 빌드) cấu hình (config / 설정) nhưng là sản phẩm tạo ra (artifact / 산출물) đặc tả hợp đồng (contract / 계약)

Kotlin và Java cùng compile vào JVM bytecode nhưng có thể bị cấu hình mục tiêu (target / 대상) khác nhau.

Ví dụ:

```text
compileJava targetCompatibility = 17
compileKotlin jvmTarget = 1.8
```

Hoặc ngược lại.

Kotlin Gradle Plugin có kiểm tra hợp lệ (validation / 검증) giữa Kotlin `jvmTarget` và Java mục tiêu (target / 대상). Với Gradle hiện đại, mismatch thường có thể làm bản dựng (build / 빌드) thất bại (fail / 실패).

Mô hình tư duy (mental model / 사고 모델):

```text
JDK chạy Gradle
!= Java source level
!= Java target level
!= Kotlin jvmTarget
```

Dùng JDK 21 để chạy Gradle không có nghĩa đầu ra (output / 출력) bytecode tự động phải mục tiêu (target / 대상) JVM 21.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 08 — Kotlin + Android phiên bản (version / 버전) tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션) và Upgrade Forensics**, **6.1 Toolchain giúp gì?** tiếp nhận điểm tựa từ **4.1 Vì sao “bytecode chạy được” chưa đủ?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9.1 BOM không “cài Compose” cho dự án (project / 프로젝트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.1 Toolchain giúp gì?

Java/Kotlin toolchain giúp bản dựng (build / 빌드) reproducible hơn vì nhà phát triển (developer / 개발자) machine không tự quyết định trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) mức (level / 수준).

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

# 7. Android làm JVM tính tương thích (compatibility / 호환성) phức tạp thêm một tầng

Android không chạy JVM desktop theo cách thông thường. nguồn (source / 소스) Java/Kotlin đi qua chuỗi xử lý (pipeline / 파이프라인):

```text
Java/Kotlin source
→ JVM class files
→ D8/R8
→ DEX
→ ART
```

Vì vậy một Java/Kotlin ngôn ngữ (language / 언어) tính năng (feature / 기능) có thể được dùng trên Android thấp hơn nhờ:

```text
desugaring
core library desugaring
Jetpack compatibility abstraction
```

Do đó không được suy luận đơn giản:

```text
“JVM 17 feature → Android device phải có Java 17 runtime.”
```

Android bản dựng (build / 빌드) toolchain có thể transform một phần tính năng (feature / 기능) trước khi sản phẩm tạo ra (artifact / 산출물) tới thiết bị (device / 장치).

---

# 8. trình biên dịch (compiler / 컴파일러) plugin là nơi phiên bản (version / 버전) upgrade dễ vỡ nhất

Trình biên dịch (compiler / 컴파일러) plugin chạy sâu trong compilation chuỗi xử lý (pipeline / 파이프라인). Nó phụ thuộc trình biên dịch (compiler / 컴파일러) internals nhiều hơn thư viện (library / 라이브러리) thời gian chạy (runtime / 런타임) thông thường.

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

Upgrade Kotlin nhưng giữ trình biên dịch (compiler / 컴파일러) plugin quá cũ có thể gây:

```text
compiler crash
unresolved generated symbol
IR lowering error
metadata mismatch
incremental compilation bug
release-only generated-code issue
```

Vì vậy di chuyển (migration / 마이그레이션) Kotlin môi trường vận hành (production / 운영 환경) phải xem trình biên dịch (compiler / 컴파일러) plugin như **lockstep ranh giới (boundary / 경계)**, không phải phụ thuộc (dependency / 의존성) thời gian chạy (runtime / 런타임) bình thường.

---

# 9. Compose trình biên dịch (compiler / 컴파일러): trước và sau Kotlin 2.0 là hai generation khác nhau

Trước Kotlin 2.0:

```text
Kotlin version
↕ compatibility map
Compose compiler version
```

Nhà phát triển (developer / 개발자) phải chọn Compose trình biên dịch (compiler / 컴파일러) tương thích với Kotlin trình biên dịch (compiler / 컴파일러).

Từ Kotlin 2.0:

```text
Kotlin compiler
+
org.jetbrains.kotlin.plugin.compose
```

Compose trình biên dịch (compiler / 컴파일러) được phát hành cùng Kotlin và plugin dùng cùng phiên bản (version / 버전) Kotlin.

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

Compose UI libraries vẫn được quản lý theo bản phát hành (release / 릴리스)/BOM riêng.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 08 — Kotlin + Android phiên bản (version / 버전) tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션) và Upgrade Forensics**, **9.1 BOM không “cài Compose” cho dự án (project / 프로젝트)** tiếp nhận điểm tựa từ **6.1 Toolchain giúp gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9.2 sản phẩm tạo ra (artifact / 산출물) bản dựng (build / 빌드) bằng Compose trình biên dịch (compiler / 컴파일러) cũ vẫn có thể ảnh hưởng app mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9.1 BOM không “cài Compose” cho dự án (project / 프로젝트)

BOM chỉ quản lý tập phiên bản (version / 버전) tương thích cho Compose libraries.

Ví dụ:

```kotlin
implementation(platform("androidx.compose:compose-bom:2026.09.00"))
implementation("androidx.compose.ui:ui")
implementation("androidx.compose.material3:material3")
```

BOM không tự thêm `ui`, `material3` hay trình biên dịch (compiler / 컴파일러) plugin.

Đây là một dạng thất bại (failure mode / 실패 모드) phổ biến khi nhà phát triển (developer / 개발자) hiểu BOM như phụ thuộc (dependency / 의존성) bundle thay vì **phiên bản (version / 버전) alignment đặc tả hợp đồng (contract / 계약)**.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 08 — Kotlin + Android phiên bản (version / 버전) tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션) và Upgrade Forensics**, **9.2 sản phẩm tạo ra (artifact / 산출물) bản dựng (build / 빌드) bằng Compose trình biên dịch (compiler / 컴파일러) cũ vẫn có thể ảnh hưởng app mới** tiếp nhận điểm tựa từ **9.1 BOM không “cài Compose” cho dự án (project / 프로젝트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10.1 Generated mã (code / 코드) là một API ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9.2 sản phẩm tạo ra (artifact / 산출물) bản dựng (build / 빌드) bằng Compose trình biên dịch (compiler / 컴파일러) cũ vẫn có thể ảnh hưởng app mới

Một app dùng trình biên dịch (compiler / 컴파일러) mới nhưng phụ thuộc (dependency / 의존성) được bản dựng (build / 빌드) bằng trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전) có bug vẫn có thể mang hành vi (behavior / 동작) bất lợi vào composition/thời gian chạy (runtime / 런타임).

Đây là ví dụ quan trọng:

```text
application toolchain mới
không đồng nghĩa
mọi binary dependency đã được rebuild bằng toolchain mới
```

Khi điều tra recomposition bất thường, cần nhìn cả producer phiên bản (version / 버전) của phụ thuộc (dependency / 의존성) chứ không chỉ app gốc (root / 루트) bản dựng (build / 빌드) tệp (file / 파일).

---

# 10. KSP và kapt không chỉ là “hai cách generate mã (code / 코드)”

`kapt` làm việc qua Java annotation processing mô hình (model / 모델). KSP làm việc trên Kotlin symbol mô hình (model / 모델).

Khi nâng Kotlin phiên bản (version / 버전), generated-code ecosystem cần được kiểm tra theo processor:

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

chỉ vì KSP mới hơn. Processor phải thực sự hỗ trợ KSP và hành vi (behavior / 동작) generated mã (code / 코드) cần kiểm thử (test / 테스트) lại.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 08 — Kotlin + Android phiên bản (version / 버전) tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션) và Upgrade Forensics**, **9.2 sản phẩm tạo ra (artifact / 산출물) bản dựng (build / 빌드) bằng Compose trình biên dịch (compiler / 컴파일러) cũ vẫn có thể ảnh hưởng app mới** đã nêu tiêu chí phân biệt, còn **10.1 Generated mã (code / 코드) là một API ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 10.1 Generated mã (code / 코드) là một API ranh giới (boundary / 경계)

Nhiều nhóm (team / 팀) xem generated nguồn (source / 소스) như hiện thực (implementation / 구현) detail. Điều này chỉ đúng một phần.

Nếu handwritten mã (code / 코드) compile dựa vào generated symbol, thì generator đầu ra (output / 출력) chính là đặc tả hợp đồng (contract / 계약) của bản dựng (build / 빌드).

Upgrade trình biên dịch (compiler / 컴파일러)/processor có thể đổi:

```text
tên class generated
nullability annotation
visibility
constructor signature
incremental processing behavior
ordering
error diagnostic
```

Vì vậy kiểm thử (test / 테스트) upgrade phải compile clean bản dựng (build / 빌드), không chỉ incremental bản dựng (build / 빌드) từ bộ nhớ đệm (cache / 캐시) cũ.

---

# 11. Clean bản dựng (build / 빌드) và incremental bản dựng (build / 빌드) có thể cho hai kết quả khác nhau

Incremental compilation giữ bộ nhớ đệm (cache / 캐시) của compilation trước.

Một di chuyển (migration / 마이그레이션) có thể “pass cục bộ (local / 로컬)” vì bộ nhớ đệm (cache / 캐시) cũ che lỗi generated mã (code / 코드) hoặc stale sản phẩm tạo ra (artifact / 산출물).

Do đó kiểm tra hợp lệ (validation / 검증) nên có cả:

```text
incremental developer build
+
clean CI build
+
release/minified build
```

Nếu chỉ chạy `assembleDebug` trên máy đã bản dựng (build / 빌드) nhiều lần, confidence rất thấp.

---

# 12. nguồn (source / 소스) tính tương thích (compatibility / 호환성), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và behavioral tính tương thích (compatibility / 호환성) phải tách riêng

Giả sử thư viện (library / 라이브러리) đổi:

```kotlin
fun load(id: String): User
```

thành:

```kotlin
fun load(id: String, refresh: Boolean = false): User
```

Nguồn (source / 소스) bên tiêu thụ (consumer / 소비자) compile lại có thể vẫn gọi:

```kotlin
load("42")
```

nhưng nhị phân (binary / 이진) bên tiêu thụ (consumer / 소비자) cũ không nhất thiết tương thích như bạn nghĩ nếu bytecode/công khai (public / 공개) ABI thay đổi.

Do đó thư viện (library / 라이브러리) di chuyển (migration / 마이그레이션) phải hỏi ba câu khác nhau:

```text
source cũ compile lại được không?
binary cũ chạy với library mới được không?
behavior cũ có còn đúng không?
```

---

# 13. Default parameter là nguồn (source / 소스) convenience nhưng có nhị phân (binary / 이진) implication

Kotlin default parameter thường sinh synthetic helper như `$default` ở JVM mức (level / 수준).

Thay đổi default giá trị (value / 값):

```kotlin
fun connect(timeoutMs: Long = 5_000)
```

thành:

```kotlin
fun connect(timeoutMs: Long = 10_000)
```

có thể không làm nguồn (source / 소스) API nhìn khác nhiều, nhưng hành vi (behavior / 동작) bên tiêu thụ (consumer / 소비자) sau recompile có thể đổi.

Đây là **behavioral tính tương thích (compatibility / 호환성) thay đổi (change / 변경)**.

Với công khai (public / 공개) SDK, default giá trị (value / 값) là một phần đặc tả hợp đồng (contract / 계약) cần document và kiểm thử (test / 테스트).

---

# 14. `inline` làm hiện thực (implementation / 구현) leak sang bên tiêu thụ (consumer / 소비자) sản phẩm tạo ra (artifact / 산출물)

Inline hàm (function / 함수) đặc biệt vì body có thể được bản sao (copy / 복사) vào lời gọi (call / 호출) site của bên tiêu thụ (consumer / 소비자) khi compile.

```kotlin
inline fun <reified T> decode(json: String): T = ...
```

Nếu hiện thực (implementation / 구현) thay đổi trong thư viện (library / 라이브러리) phiên bản (version / 버전) mới, bên tiêu thụ (consumer / 소비자) nhị phân (binary / 이진) cũ có thể vẫn chứa lô-gic (logic / 논리) inline cũ cho tới khi recompile.

Mô hình tư duy (mental model / 사고 모델):

```text
non-inline library function
→ logic chủ yếu sống trong library binary

inline public function
→ một phần logic có thể sống trong consumer binary
```

Đây là lý do công khai (public / 공개) inline API cần tính tương thích (compatibility / 호환성) discipline cao hơn tưởng tượng.

---

# 15. `const val` cũng có thể bị inline vào bên tiêu thụ (consumer / 소비자)

Ví dụ:

```kotlin
const val API_VERSION = 3
```

Bên tiêu thụ (consumer / 소비자) compile có thể embed giá trị này.

Sau khi thư viện (library / 라이브러리) đổi:

```kotlin
const val API_VERSION = 4
```

Bên tiêu thụ (consumer / 소비자) nhị phân (binary / 이진) cũ có thể vẫn dùng `3` cho tới khi recompile.

Vì vậy công khai (public / 공개) constant thay đổi không phải lúc nào cũng giống đọc trường dữ liệu (field / 필드) thời gian chạy (runtime / 런타임).

---

# 16. giá trị (value / 값) lớp (class / 클래스) và ABI evolution cần cẩn thận

Giá trị (value / 값) lớp (class / 클래스) có biểu diễn (representation / 표현)/boxing rules phụ thuộc ngữ cảnh (context / 맥락).

Ví dụ:

```kotlin
@JvmInline
value class UserId(val raw: String)
```

Đổi underlying kiểu (type / 타입):

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

Nếu kiểu (type / 타입) nằm trong API công khai (public API / 공개 API), hãy coi underlying biểu diễn (representation / 표현) là tính tương thích (compatibility / 호환성) concern.

---

# 17. Enum evolution không phải lúc nào cũng backward-safe

Thêm enum constant mới có thể làm mã (code / 코드) bên tiêu thụ (consumer / 소비자) cũ sai giả định (assumption / 가정).

Ví dụ bên tiêu thụ (consumer / 소비자):

```kotlin
when (status) {
    Status.NEW -> ...
    Status.DONE -> ...
}
```

Nếu enum từ remote/máy chủ (server / 서버) hoặc thư viện (library / 라이브러리) evolve thêm constant, hành vi (behavior / 동작) thời gian chạy (runtime / 런타임)/deserialization có thể thay đổi.

Với wire format hoặc SDK đặc tả hợp đồng (contract / 계약), nên thiết kế unknown giá trị (value / 값) chiến lược (strategy / 전략) thay vì giả định enum đóng vĩnh viễn.

---

# 18. Sealed hierarchy cũng có tính tương thích (compatibility / 호환성) ngữ nghĩa (semantics / 의미론)

Sealed kiểu (type / 타입) giúp exhaustive `when` trong cùng compilation ngữ cảnh (context / 맥락).

Nhưng thư viện (library / 라이브러리) công khai (public / 공개) sealed hierarchy evolve phức tạp hơn nội bộ (internal / 내부) app hierarchy.

Thêm subtype mới có thể buộc nguồn (source / 소스) bên tiêu thụ (consumer / 소비자) recompile và xử lý branch mới.

Nếu ecosystem yêu cầu third-party extension hoặc open-ended evolution, sealed có thể không phải đặc tả hợp đồng (contract / 계약) phù hợp.

Phiên bản (version / 버전) thiết kế (design / 설계) phải bắt đầu từ evolution yêu cầu (requirement / 요구사항), không chỉ từ cú pháp (syntax / 문법) tiện lợi.

---

# 19. Serialization lược đồ (schema / 스키마) là phiên bản (version / 버전) đặc tả hợp đồng (contract / 계약) độc lập với Kotlin phiên bản (version / 버전)

Một dự án (project / 프로젝트) upgrade Kotlin có thể đồng thời upgrade serialization plugin/thư viện (library / 라이브러리).

Điều cần bảo vệ không chỉ là compile thành công mà là dữ liệu cũ vẫn đọc được.

Ví dụ persisted JSON/Proto/Room blob có thể sống qua nhiều app phiên bản (version / 버전).

Cần kiểm thử (test / 테스트):

```text
old writer → new reader
new writer → rollback old reader nếu rollback được hỗ trợ
unknown field
missing field
default value change
enum evolution
renamed field
```

Trình biên dịch (compiler / 컴파일러) upgrade không được che mất lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) rủi ro (risk / 위험).

---

# 20. Android version axis: `minSdk`, `compileSdk`, `targetSdk` không thể gộp
Phần này nối mạch Android vừa học với “20. Android version axis: `minSdk`, `compileSdk`, `targetSdk` không thể gộp”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```text
minSdk
= install/runtime floor

compileSdk
= API surface compiler nhìn thấy

targetSdk
= behavior contract app opt-in
```

Upgrade `compileSdk` có thể cần để dùng thư viện (library / 라이브러리) mới mà chưa bắt buộc app đổi mọi hành vi thời gian chạy (runtime behavior / 런타임 동작).

Upgrade `targetSdk` mới là bước kích hoạt nhiều target-gated hành vi (behavior / 동작) changes.

Do đó di chuyển (migration / 마이그레이션) an toàn thường tách:

```text
1. compileSdk/toolchain readiness
2. app chạy trên OS mới với target cũ
3. targetSdk migration
4. behavior regression test
```

---

# 21. `targetSdk` di chuyển (migration / 마이그레이션) là ngữ nghĩa (semantic / 의미적) di chuyển (migration / 마이그레이션), không chỉ bản dựng (build / 빌드) di chuyển (migration / 마이그레이션)

Tăng mục tiêu (target / 대상) có thể đổi hành vi (behavior / 동작) về:

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

Bản dựng (build / 빌드) xanh không chứng minh app đã thích nghi đúng.

Đây là điểm khác với nhiều ngôn ngữ (language / 언어) upgrade: targetSdk thay đổi **thời gian chạy (runtime / 런타임) chính sách (policy / 정책) đặc tả hợp đồng (contract / 계약) của OS**.

---

# 22. Android SDK Extensions làm “API availability” không còn chỉ là API mức (level / 수준)

Một số Android năng lực (capability / 역량) có thể được cập nhật qua modular hệ thống (system / 시스템) thành phần (component / 컴포넌트).

Vì vậy future-proof mã (code / 코드) đôi khi cần xét:

```text
Build.VERSION.SDK_INT
+
SDK extension version
```

Mô hình tư duy (mental model / 사고 모델) quan trọng:

```text
OS API level
không phải lúc nào cũng là toàn bộ platform capability version
```

Đây là lý do tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링) cần đọc docs của API cụ thể thay vì chỉ so `SDK_INT` máy móc.

---

# 23. AGP upgrade kéo theo Gradle và JDK vì bản dựng (build / 빌드) toolchain là một đồ thị (graph / 그래프)

Một AGP bản phát hành (release / 릴리스) thường có supported phạm vi (range / 범위) cho:

```text
Gradle
JDK
Android SDK/build tools
Android Studio
```

Do đó lỗi sau AGP upgrade thường không nằm trong Android nguồn (source / 소스).

Ví dụ chuỗi (chain / 사슬):

```text
muốn compileSdk mới
→ cần AGP mới
→ AGP mới cần Gradle mới
→ Gradle/AGP mới cần JDK mới
```

Nếu upgrade tất cả trong một lần ghi nhận (commit / 커밋) khổng lồ, forensic rất khó.

---

# 24. Upgrade thứ tự (order / 순서) nên theo phụ thuộc (dependency / 의존성) direction

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

Thứ tự cụ thể có thể khác theo tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬), nhưng nguyên tắc là **không đổi nhiều independent axes hơn cần thiết trong cùng một bước**.

---

# 25. phiên bản (version / 버전) danh mục (catalog / 카탈로그) chỉ centralize phiên bản (version / 버전), không chứng minh tính tương thích (compatibility / 호환성)

`libs.versions.toml` giúp nhìn đồ thị (graph / 그래프) dễ hơn:

```toml
[versions]
kotlin = "2.4.20"
agp = "9.4.1"
compose-bom = "2026.09.00"
```

Nhưng tệp (file / 파일) đẹp không đảm bảo ma trận (matrix / 행렬) hợp lệ.

Phiên bản (version / 버전) danh mục (catalog / 카탈로그) không tự biết:

```text
AGP có support Gradle này không
KSP có support Kotlin này không
processor có support KSP2 không
Compose library có yêu cầu compileSdk cao hơn không
```

Nó là declaration tầng (layer / 계층), không phải tính tương thích (compatibility / 호환성) solver hoàn chỉnh.

---

# 26. BOM cũng chỉ giải một phần phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)

BOM hữu ích để align family libraries.

Nhưng BOM thường không quản lý mọi phụ thuộc (dependency / 의존성) xung quanh family đó.

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

Do đó phụ thuộc (dependency / 의존성) quản trị (governance / 거버넌스) cần nhiều lớp:

```text
Version Catalog
+BOM
+dependency constraints
+compatibility docs
+CI build/test matrix
```

---

# 27. Transitive phụ thuộc (dependency / 의존성) có thể âm thầm nâng floor của dự án (project / 프로젝트)

Một thư viện (library / 라이브러리) upgrade có thể kéo transitive phụ thuộc (dependency / 의존성) mới yêu cầu:

```text
compileSdk cao hơn
minSdk cao hơn
newer Kotlin metadata
newer Java bytecode
newer desugaring support
```

Vì vậy khi phụ thuộc (dependency / 의존성) cập nhật (update / 업데이트) làm bản dựng (build / 빌드) hỏng, đừng chỉ nhìn direct phụ thuộc (dependency / 의존성) declaration.

Cần inspect resolved đồ thị (graph / 그래프).

Trong Gradle, tư duy đúng là:

```text
declared dependency
→ dependency constraints
→ variant selection
→ resolved graph
→ artifact thực tế
```

---

# 28. phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) không nên giải bằng “force latest” trước khi hiểu đồ thị (graph / 그래프)

Ép latest phiên bản (version / 버전) có thể bản dựng (build / 빌드) được nhưng tạo thời gian chạy (runtime / 런타임) incompatibility.

Trước khi dùng force/resolutionStrategy, cần biết:

```text
ai yêu cầu version cũ?
ai yêu cầu version mới?
API/ABI có tương thích không?
variant nào được chọn?
consumer rule nào đi kèm artifact?
```

Một bản dựng (build / 빌드) hết warning không đồng nghĩa thời gian chạy (runtime / 런타임) đồ thị (graph / 그래프) đúng.

---

# 29. di chuyển (migration / 마이그레이션) scenario A — Kotlin 1.9 + Compose trình biên dịch (compiler / 컴파일러) cũ → Kotlin 2.x

Đây là di chuyển (migration / 마이그레이션) rất phổ biến.

Legacy mô hình tư duy (mental model / 사고 모델):

```text
Kotlin 1.9.x
+
Compose compiler 1.5.x tương thích theo map
```

Hiện đại (modern / 현대적) mô hình tư duy (mental model / 사고 모델):

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

Không nên cùng lúc rewrite XML → Compose trong di chuyển (migration / 마이그레이션) này. Hai việc độc lập.

---

# 30. di chuyển (migration / 마이그레이션) scenario B — `kotlinOptions {}` → `compilerOptions {}`

Legacy:

```kotlin
android {
    kotlinOptions {
        jvmTarget = "17"
    }
}
```

Hiện đại (modern / 현대적):

```kotlin
kotlin {
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_17)
    }
}
```

Điểm cần kiểm tra không chỉ cú pháp (syntax / 문법) DSL.

Trong multi-module dự án (project / 프로젝트), option có thể được set ở nhiều mức (level / 수준):

```text
extension level
target level
compilation task level
convention plugin
third-party Gradle plugin
```

Lower mức (level / 수준) có thể override higher mức (level / 수준).

Khi di chuyển (migration / 마이그레이션) xong mà hành vi (behavior / 동작) khác, inspect **effective trình biên dịch (compiler / 컴파일러) args**, không chỉ đọc gốc (root / 루트) bản dựng (build / 빌드) script.

---

# 31. di chuyển (migration / 마이그레이션) scenario C — kapt → KSP

Một di chuyển (migration / 마이그레이션) an toàn nên đi processor-by-processor.

Ví dụ:

```text
Room supports KSP → migrate Room first
custom processor chưa support → giữ kapt
```

Dự án (project / 프로젝트) có thể tạm thời dùng cả hai.

Điều cần đo:

```text
clean build time
incremental build time
generated source parity
error diagnostics
release/minified build
IDE indexing
```

Mục tiêu không phải “100% KSP” bằng mọi giá. Mục tiêu là giảm bản dựng (build / 빌드) chi phí (cost / 비용) mà không đổi hành vi (behavior / 동작).

---

# 32. di chuyển (migration / 마이그레이션) scenario D — nâng targetSdk nhưng giữ Kotlin ổn định

Nếu sản phẩm (product / 제품) có rủi ro (risk / 위험) cao, đây thường là chiến lược tốt:

```text
Kotlin/KGP giữ nguyên
AGP/compileSdk đủ mới
nâng targetSdk
fix platform behavior
run device matrix
release
```

Sau khi mục tiêu (target / 대상) di chuyển (migration / 마이그레이션) ổn định mới thực hiện Kotlin/trình biên dịch (compiler / 컴파일러) upgrade riêng.

Tách bản phát hành (release / 릴리스) train giúp postmortem rõ hơn nếu crash tăng.

---

# 33. di chuyển (migration / 마이그레이션) scenario E — nâng Kotlin nhưng giữ targetSdk ổn định

Ngược lại:

```text
Kotlin/KGP
compiler plugins
KSP/kapt processors
Compose compiler setup
```

được nâng trong khi Android hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약) giữ nguyên.

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

# 34. thư viện (library / 라이브러리) upgrade chiến lược (strategy / 전략) khác ứng dụng (application / 애플리케이션) upgrade chiến lược (strategy / 전략)

Ứng dụng (application / 애플리케이션) thường compile lại toàn bộ nguồn (source / 소스) cùng một toolchain.

Thư viện (library / 라이브러리) phải hỗ trợ bên tiêu thụ (consumer / 소비자) nằm ngoài quyền kiểm soát.

Do đó thư viện (library / 라이브러리) cần tường minh (explicit / 명시적) hỗ trợ (support / 지원) ma trận (matrix / 행렬):

```text
minimum Kotlin version
minimum JVM target
minimum Android API
minimum compileSdk expectation
Java interoperability
binary compatibility policy
SemVer policy
```

Nếu không document, bên tiêu thụ (consumer / 소비자) sẽ tự suy luận từ bản dựng (build / 빌드) thất bại (failure / 실패).

---

# 35. công khai (public / 공개) thư viện (library / 라이브러리) không nên vô tình nâng Kotlin floor

Giả sử thư viện (library / 라이브러리) bản dựng (build / 빌드) bằng trình biên dịch (compiler / 컴파일러) mới và dùng stdlib API mới trong công khai (public / 공개) inline hàm (function / 함수).

Bên tiêu thụ (consumer / 소비자) dùng Kotlin cũ có thể gặp vấn đề dù công khai (public / 공개) phương thức (method / 메서드) name gần như không đổi.

Vì vậy thư viện (library / 라이브러리) author cần kiểm thử (test / 테스트) **old supported bên tiêu thụ (consumer / 소비자) dự án (project / 프로젝트)** thật, không chỉ kiểm thử (test / 테스트) mô-đun (module / 모듈) trong mono-repo bằng cùng gốc (root / 루트) toolchain.

---

# 36. bên tiêu thụ (consumer / 소비자) ma trận (matrix / 행렬) nên là executable kiểm thử (test / 테스트), không phải README văn bản (text / 텍스트)

Một SDK môi trường vận hành (production / 운영 환경) có thể có fixture projects:

```text
consumer-old-kotlin/
consumer-current-kotlin/
consumer-java/
consumer-minified/
consumer-compose/
```

CI bản dựng (build / 빌드) các bên tiêu thụ (consumer / 소비자) này sau mỗi bản phát hành (release / 릴리스) candidate.

Như vậy hỗ trợ (support / 지원) ma trận (matrix / 행렬) trở thành testable đặc tả hợp đồng (contract / 계약).

---

# 37. R8/ProGuard làm phiên bản (version / 버전) tính tương thích (compatibility / 호환성) có thêm một chiều

Gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) có thể chạy, bản phát hành (release / 릴리스) minified bản dựng (build / 빌드) crash vì:

```text
reflection target bị rename
serializer metadata bị strip
JNI method/name lookup bị obfuscate
consumer keep rule thiếu
SDK update thay internal class graph
```

Vì vậy upgrade thư viện (library / 라이브러리)/trình biên dịch (compiler / 컴파일러) plugin phải kiểm thử (test / 테스트) bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) thật.

Không được xem R8 là “bước cuối tối ưu kích thước (size / 크기)”. Nó là một transformation stage có thể làm lộ đặc tả hợp đồng (contract / 계약) ẩn.

---

# 38. bản địa (native / 네이티브) `.so` phụ thuộc (dependency / 의존성) có phiên bản (version / 버전) đặc tả hợp đồng (contract / 계약) riêng

Android app có NDK/bản địa (native / 네이티브) thư viện (library / 라이브러리) cần xét:

```text
ABI
NDK level
C++ runtime
symbol visibility
page-size compatibility
native API level
JNI contract
```

Kotlin/AGP upgrade có thể kéo packaging hành vi (behavior / 동작) mới dù bản địa (native / 네이티브) nguồn (source / 소스) không đổi.

Do đó nhị phân (binary / 이진) inventory nên bao gồm cả `.so`, không chỉ Maven dependencies.

---

# 39. bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시) có thể làm forensic sai nếu không kiểm soát

Một regression sau upgrade đôi khi chỉ xuất hiện ở clean môi trường (environment / 환경).

Forensic chuỗi (sequence / 시퀀스) nên có:

```text
1. reproduce incremental build
2. clean local build
3. CI clean build
4. optionally disable/rebuild relevant cache
5. compare generated artifacts
```

Không nên xóa toàn bộ bộ nhớ đệm (cache / 캐시) ngay từ đầu rồi mất bằng chứng về incremental-only bug.

---

# 40. Effective cấu hình (configuration / 구성) quan trọng hơn declaration

Dự án (project / 프로젝트) lớn có thể set Kotlin/Android option qua:

```text
root plugin
convention plugin
module build script
buildSrc
included build
third-party Gradle plugin
CI property
```

Do đó tệp (file / 파일) `build.gradle.kts` của mô-đun (module / 모듈) không nhất thiết phản ánh effective giá trị (value / 값) cuối.

Khi gỡ lỗi (debug / 디버그) hãy hỏi:

```text
compiler args thực tế là gì?
variant nào đang build?
resolved dependency nào thực tế được chọn?
manifest cuối cùng là gì?
R8 rules cuối cùng là gì?
```

---

# 41. phiên bản (version / 버전) forensic: bắt đầu từ sản phẩm tạo ra (artifact / 산출물), không bắt đầu từ phỏng đoán

Giả sử bản phát hành (release / 릴리스) mới crash nhưng gỡ lỗi (debug / 디버그) không crash.

Thay vì nói:

```text
“R8 chắc lỗi.”
```

hãy tạo bằng chứng (evidence / 증거) chuỗi (chain / 사슬):

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

Forensic kỹ thuật (engineering / 엔지니어링) nghĩa là truy từ sản phẩm tạo ra (artifact / 산출물) về cấu hình (configuration / 구성), không từ cảm giác về công cụ (tool / 도구).

---

# 42. Lỗi siêu dữ liệu (metadata / 메타데이터) mismatch — playbook điều tra

Khi gặp lỗi Kotlin siêu dữ liệu (metadata / 메타데이터) incompatible:

```text
1. tìm dependency nào chứa artifact lỗi
2. xác định producer Kotlin version
3. xác định consumer compiler version
4. xem dependency direct hay transitive
5. kiểm tra artifact có pre-release không
6. nâng consumer compiler hoặc hạ dependency theo support matrix
7. không dùng skip metadata check như fix mặc định
```

Trình biên dịch (compiler / 컴파일러) flag bỏ check chỉ nên là diagnostic/temporary escape hatch khi hiểu rõ consequence.

---

# 43. Lỗi JVM target mismatch — playbook điều tra
Phần này nối mạch Android vừa học với “43. Lỗi JVM target mismatch — playbook điều tra”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```text
1. xem Java targetCompatibility
2. xem Kotlin jvmTarget effective
3. xem JDK/toolchain đang chạy
4. xem convention plugin có override không
5. align toolchain/targets
6. clean build
```

Đừng sửa bằng cách disable kiểm tra hợp lệ (validation / 검증) trước khi hiểu mismatch.

Kiểm tra hợp lệ (validation / 검증) đang bảo vệ sản phẩm tạo ra (artifact / 산출물) consistency.

---

# 44. Lỗi “works on gỡ lỗi (debug / 디버그), fails on bản phát hành (release / 릴리스)” sau upgrade

Suspect danh sách (list / 목록) theo thứ tự bằng chứng (evidence / 증거):

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

Trình biên dịch (compiler / 컴파일러) upgrade có thể chỉ là trigger làm đặc tả hợp đồng (contract / 계약) ẩn lộ ra, không nhất thiết là nguyên nhân gốc (root cause / 근본 원인).

---

# 45. Lỗi “works on one thiết bị (device / 장치), fails on another” sau mục tiêu (target / 대상) upgrade

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

Thiết bị (device / 장치) ma trận (matrix / 행렬) phải được ghi vào reproduction report.

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

Nếu cục bộ (local / 로컬) dùng Android Studio bundled JDK nhưng CI dùng hệ thống (system / 시스템) JDK khác, cùng nguồn (source / 소스) không có nghĩa cùng bản dựng (build / 빌드) môi trường (environment / 환경).

---

# 47. Lỗi “only cục bộ (local / 로컬) fails” sau upgrade

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

Trước hết capture môi trường (environment / 환경) để biết sự khác nhau giữa cục bộ (local / 로컬) và CI.

---

# 48. Upgrade PR nên chứa một phiên bản (version / 버전) fingerprint machine-readable

Ví dụ trong PR description hoặc sản phẩm tạo ra (artifact / 산출물) report:

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

# 49. CI gate cho phiên bản (version / 버전) di chuyển (migration / 마이그레이션)

Một upgrade môi trường vận hành (production / 운영 환경) nên có gate tối thiểu:

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

Không phải dự án (project / 프로젝트) nào cũng cần ma trận (matrix / 행렬) khổng lồ. Nhưng gate phải cover ranh giới (boundary / 경계) có rủi ro (risk / 위험) thật.

---

# 50. hiệu năng (performance / 성능) regression sau trình biên dịch (compiler / 컴파일러) upgrade cần bằng chứng (evidence / 증거)

Trình biên dịch (compiler / 컴파일러) mới có thể thay:

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

Không kết luận tốt/xấu chỉ từ bản phát hành (release / 릴리스) ghi chú (note / 노트) “trình biên dịch (compiler / 컴파일러) nhanh hơn”. bản dựng (build / 빌드) hiệu năng (performance / 성능) và thời gian chạy (runtime / 런타임) hiệu năng (performance / 성능) là hai chuyện khác nhau.

---

# 51. Build performance cũng phải được đo clean và incremental riêng
Phần này nối mạch Android vừa học với “51. Build performance cũng phải được đo clean và incremental riêng”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```text
clean build
!= incremental build
!= configuration time
!= test execution time
```

Upgrade KGP/KSP/AGP có thể cải thiện một loại nhưng làm loại khác chậm hơn.

Benchmark bản dựng (build / 빌드) phải ghi rõ scenario.

---

# 52. phiên bản (version / 버전) hỗ trợ (support / 지원) chính sách (policy / 정책) cần được viết ra trước khi khủng hoảng

Nhóm (team / 팀) nên quyết định:

```text
Kotlin release line được support bao lâu?
bao lâu review targetSdk?
bao lâu review AGP?
JDK baseline là gì?
alpha/beta dependency có được phép production không?
compiler flag experimental nào được phép?
```

Nếu không có chính sách (policy / 정책), upgrade thường chỉ xảy ra khi Google Play deadline hoặc phụ thuộc (dependency / 의존성) bắt buộc nhóm (team / 팀) phải nhảy nhiều generation cùng lúc.

---

# 53. “Latest everything” không phải phiên bản (version / 버전) chiến lược (strategy / 전략)

Luôn latest có lợi ích:

```text
security fix
support window dài
API/tooling mới
ít migration debt tích lũy
```

Nhưng môi trường vận hành (production / 운영 환경) còn có:

```text
plugin lag
regression risk
release train
certification/device testing
vendor SDK compatibility
```

Chiến lược (strategy / 전략) tốt là **stay reasonably hiện tại (current / 현재) inside supported windows**, không phải chạy theo phiên bản (version / 버전) trong ngày đầu bằng mọi giá.

---

# 54. phiên bản (version / 버전) debt là technical debt có thể đo được

Có thể nhánh học (track / 트랙):

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

Phiên bản (version / 버전) debt lớn làm mỗi di chuyển (migration / 마이그레이션) sau đắt hơn vì nhiều ranh giới (boundary / 경계) đổi cùng lúc.

---

# 55. rủi ro (risk / 위험) score cho một upgrade

Một cách rà soát (review / 검토) định tính:

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

Công thức không cần số tuyệt đối; nó ép nhóm (team / 팀) suy nghĩ về dimension thật của rủi ro (risk / 위험).

---

# 56. chiến lược quay lui (rollback strategy / 롤백 전략) phải xét backward tính tương thích (compatibility / 호환성) của dữ liệu (data / 데이터)

Nếu bản phát hành (release / 릴리스) mới migrate Room lược đồ (schema / 스키마) hoặc persisted dữ liệu (data / 데이터) rồi quay lui (rollback / 롤백) app nhị phân (binary / 이진), nhị phân (binary / 이진) cũ có đọc dữ liệu (data / 데이터) mới được không?

Phiên bản (version / 버전) upgrade có thể nhìn là bản dựng (build / 빌드) concern nhưng quay lui (rollback / 롤백) lại chạm lưu trữ (storage / 저장소) đặc tả hợp đồng (contract / 계약).

Do đó bản phát hành (release / 릴리스) plan phải hỏi:

```text
app cũ đọc DB mới được không?
feature flag có disable behavior không?
server contract có backward-compatible không?
remote config có cứu được không?
```

---

# 57. máy chủ (server / 서버)/API phiên bản (version / 버전) cũng tham gia mobile tính tương thích (compatibility / 호환성)

Mobile app không cập nhật (update / 업데이트) đồng thời với backend bên tiêu thụ (consumer / 소비자) khác.

Nếu app mới yêu cầu API mới ngay khi bản phát hành (release / 릴리스), rollout chậm có thể tạo mixed-version population.

Cần thiết kế (design / 설계):

```text
old app + new server
new app + old-compatible server behavior
```

Phiên bản (version / 버전) kỹ thuật (engineering / 엔지니어링) mobile luôn có yếu tố distributed-system tính tương thích (compatibility / 호환성).

---

# 58. cờ tính năng (feature flag / 기능 플래그) là công cụ di chuyển (migration / 마이그레이션), không phải substitute cho tính tương thích (compatibility / 호환성)

Cờ tính năng (feature flag / 기능 플래그) có thể giảm blast radius của hành vi (behavior / 동작) mới.

Nhưng không cứu được:

```text
app không khởi động vì metadata mismatch
binary link error
manifest invalid
DB schema unreadable trước khi flag load
```

Flag chỉ hiệu quả sau khi app đủ healthy để đọc flag.

---

# 59. bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) phải dấu vết (trace / 추적) được về toolchain

Một môi trường vận hành (production / 운영 환경) APK/AAB nên dấu vết (trace / 추적) được về:

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

# 60. hiện tại (current / 현재) baseline của bộ tài liệu

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

Kotlin 2.4 bản phát hành (release / 릴리스) line bắt đầu ngày 2026-06-03 và hỗ trợ (support / 지원) cửa sổ (window / 윈도우) chính thức tới cuối năm 2027; 2.4.20 phát hành ngày 2026-09-07.

Snapshot này phải được rà soát (review / 검토) khi toolchain thay đổi.

---

# 61. Checklist forensic khi upgrade thất bại

Thay vì thử random phiên bản (version / 버전), đi theo thứ tự:

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

# 62. Checklist rà soát (review / 검토) phiên bản (version / 버전) PR

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

Nếu PR không trả lời được, upgrade vẫn đang ở mức “đổi phiên bản (version / 버전) string”.

---

# 63. mô hình tư duy (mental model / 사고 모델) cuối cùng

Khi nhìn một phiên bản (version / 버전) thay đổi (change / 변경), đừng hỏi đầu tiên:

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

Phiên bản (version / 버전) kỹ thuật (engineering / 엔지니어링) tốt là khả năng giữ **nguồn (source / 소스), nhị phân (binary / 이진), siêu dữ liệu (metadata / 메타데이터), generated mã (code / 코드), Android hành vi (behavior / 동작), persisted dữ liệu (data / 데이터) và bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물)** cùng tiến hóa mà không làm hệ thống mất khả năng bản dựng (build / 빌드), chạy, quay lui (rollback / 롤백) hoặc được gỡ lỗi (debug / 디버그).

Đó là điểm mà kiến thức version vượt khỏi “biết Kotlin 2.4 mới hơn Kotlin 1.9” và trở thành **compatibility engineering** thực sự.

> **Bàn giao:** Sau **10.1 Generated mã (code / 코드) là một API ranh giới (boundary / 경계)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
