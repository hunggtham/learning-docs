# Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**. Route đi từ các trục version → Kotlin/compiler/Gradle/AGP/JDK/SDK/Jetpack → timeline và compatibility → project migration, targetSdk và Play policy → kiểm tra toolchain, để lỗi phiên bản được chẩn đoán theo dependency thật.

Phiên bản (version / 버전) trong Kotlin + Android phức tạp hơn việc nhìn một con số như `2.4.20`. Một dự án (project / 프로젝트) Android thực tế có nhiều trục phiên bản (version / 버전) độc lập nhưng liên quan với nhau: phiên bản (version / 버전) của ngôn ngữ Kotlin, Kotlin trình biên dịch (compiler / 컴파일러), Kotlin Gradle Plugin, Compose trình biên dịch (compiler / 컴파일러), Android Gradle Plugin, Gradle, JDK, `jvmTarget`, Android SDK, Jetpack libraries và chính sách (policy / 정책) của Google Play.

Nếu chỉ nhớ “dự án (project / 프로젝트) đang dùng Kotlin 2.4” mà không hiểu các trục này, rất dễ gặp lỗi kiểu trình biên dịch (compiler / 컴파일러) plugin không tương thích, AGP không hỗ trợ API mức (level / 수준) mới, thư viện (library / 라이브러리) compile được nhưng bên tiêu thụ (consumer / 소비자) cũ không dùng được, hoặc app chạy tốt trên Android cũ nhưng đổi hành vi (behavior / 동작) sau khi tăng `targetSdk`.

Tệp (file / 파일) này được viết như **phiên bản (version / 버전) map + di chuyển (migration / 마이그레이션) guide**, tương tự cách học phiên bản (version / 버전) evolution của Java, JavaScript/ECMAScript hoặc Swift: không chỉ hỏi phiên bản nào mới hơn, mà phải hiểu **mỗi thế hệ đã thay đổi mô hình tư duy (mental model / 사고 모델) nào, mã (code / 코드) cũ trông ra sao, mã (code / 코드) mới nên viết như thế nào, và khi upgrade phải kiểm tra những ranh giới (boundary / 경계) nào**.

---

## 1. Trước hết phải phân biệt các loại phiên bản (version / 버전)

### 1.1 Kotlin bản phát hành (release / 릴리스) phiên bản (version / 버전)

Ví dụ:

```text
1.9.25
2.0.21
2.1.20
2.2.21
2.3.20
2.4.20
```

Đây là phiên bản (version / 버전) của Kotlin toolchain/bản phát hành (release / 릴리스) line. Nó ảnh hưởng trình biên dịch (compiler / 컴파일러), thư viện chuẩn (standard library / 표준 라이브러리), Kotlin Gradle Plugin và các ngôn ngữ (language / 언어)/tooling tính năng (feature / 기능) đi kèm.

Tại thời điểm snapshot của bộ tài liệu này, stable line hiện tại là:

```text
Kotlin 2.4.20
Released: 2026-09-07
Release line: 2.4
```

Kotlin 2.4 được JetBrains liệt kê với hỗ trợ (support / 지원) cửa sổ (window / 윈도우) tới cuối năm 2027. Con số này là snapshot, không phải phiên bản (version / 버전) phải giữ cố định mãi mãi.

---

### 1.2 `languageVersion`

`languageVersion` quyết định **bộ quy tắc ngôn ngữ** mà trình biên dịch (compiler / 컴파일러) cho phép mã nguồn (source code / 소스 코드) sử dụng.

Ví dụ conceptually:

```kotlin
kotlin {
    compilerOptions {
        languageVersion.set(KotlinVersion.KOTLIN_2_4)
    }
}
```

Một trình biên dịch (compiler / 컴파일러) mới có thể đôi khi compile mã (code / 코드) theo ngôn ngữ (language / 언어) mức (level / 수준) cũ để hỗ trợ di chuyển (migration / 마이그레이션)/thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성).

Điểm quan trọng:

```text
compiler version != language version bắt buộc phải giống tuyệt đối
```

Trình biên dịch (compiler / 컴파일러) 2.x có thể hỗ trợ một số ngôn ngữ (language / 언어)/API phiên bản (version / 버전) cũ, nhưng hỗ trợ (support / 지원) cửa sổ (window / 윈도우) không vô hạn. Ví dụ từ Kotlin 2.2, ngôn ngữ (language / 언어) phiên bản (version / 버전) 1.6 và 1.7 không còn được trình biên dịch (compiler / 컴파일러) hỗ trợ nữa.

---

### 1.3 `apiVersion`

`apiVersion` giới hạn phiên bản (version / 버전) của Kotlin thư viện chuẩn (standard library / 표준 라이브러리) API mà mã nguồn (source code / 소스 코드) được phép gọi.

Mô hình tư duy (mental model / 사고 모델):

```text
languageVersion
= cú pháp và semantic nào được phép viết

apiVersion
= API stdlib tới version nào được phép dùng
```

Điều này hữu ích cho thư viện (library / 라이브러리) author muốn compile bằng trình biên dịch (compiler / 컴파일러) mới nhưng vẫn tránh vô tình sử dụng API quá mới so với bên tiêu thụ (consumer / 소비자) mục tiêu (target / 대상).

---

### 1.4 `jvmTarget`

`jvmTarget` quyết định bytecode JVM đầu ra (output / 출력) được tạo cho JVM mức (level / 수준) nào.

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

Chúng liên quan nhưng là các đặc tả hợp đồng (contract / 계약) khác nhau.

---

### 1.5 JDK toolchain

JDK toolchain là Java trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) toolchain dùng trong bản dựng (build / 빌드).

Ví dụ:

```kotlin
kotlin {
    jvmToolchain(17)
}
```

Android Gradle Plugin cũng có yêu cầu JDK riêng theo phiên bản (version / 버전). Vì vậy upgrade AGP có thể buộc dự án (project / 프로젝트) nâng JDK dù nguồn (source / 소스) Kotlin không thay đổi.

---

### 1.6 Kotlin Gradle Plugin — KGP

Plugin thường xuất hiện dạng:

```kotlin
plugins {
    id("org.jetbrains.kotlin.android") version "2.4.20"
}
```

KGP nối Gradle với Kotlin trình biên dịch (compiler / 컴파일러)/toolchain.

Khi nói “upgrade Kotlin trong Android dự án (project / 프로젝트)”, trên thực tế thường đang thay đổi phiên bản (version / 버전) KGP trong bản dựng (build / 빌드) cấu hình (configuration / 구성).

---

### 1.7 Android Gradle Plugin — AGP

AGP không phải Kotlin plugin.

```text
KGP
= Gradle ↔ Kotlin

AGP
= Gradle ↔ Android build model
```

AGP quyết định cách Android mô-đun (module / 모듈) được bản dựng (build / 빌드), tài nguyên (resource / 자원)/manifest merge, variant, packaging, D8/R8, SDK hỗ trợ (support / 지원) và nhiều hành vi (behavior / 동작) bản dựng (build / 빌드) khác.

Vì vậy:

```text
Kotlin 2.4.20
không đồng nghĩa
AGP phải là 2.4.20
```

Chúng có bản phát hành (release / 릴리스) cadence khác nhau.

Snapshot đang dùng trong thư viện (library / 라이브러리):

```text
Kotlin: 2.4.20
AGP baseline: 9.4.1
```

---

### 1.8 Gradle phiên bản (version / 버전)

Gradle là hệ thống dựng (build system / 빌드 시스템) bên dưới.

Ta có chuỗi phụ thuộc (dependency / 의존성):

```text
Gradle
   ↑
AGP / KGP
   ↑
Android/Kotlin modules
```

Một KGP hoặc AGP mới có minimum/maximum Gradle tính tương thích (compatibility / 호환성) riêng.

Kotlin 2.4.20 hỗ trợ chính thức Gradle 7.6.3 tới 9.7.0; dùng phiên bản (version / 버전) khác có thể vẫn chạy nhưng không nằm trong fully supported phạm vi (range / 범위).

---

### 1.9 Android `minSdk`, `compileSdk`, `targetSdk`

Đây là ba phiên bản (version / 버전) axis khác hẳn Kotlin.

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

> **Nối mạch:** Phân biệt release, language/API version và toolchain trước khi đọc timeline; JVM IR mặc định tiếp theo là một consequence cần gắn với compiler generation cụ thể.

## 2. Timeline tổng quan Kotlin

Bảng dưới không cố liệt kê mọi bug-fix bản phát hành (release / 릴리스). Nó tập trung vào những bản phát hành (release / 릴리스) làm thay đổi cách đọc hoặc viết mã (code / 코드).

| Thế hệ | Thời gian | Ý nghĩa chính |
|---|---:|---|
| Kotlin 1.0 | 2016 | Ngôn ngữ JVM stable; nền móng Kotlin hiện đại |
| Kotlin 1.1 | 2017 | Coroutine xuất hiện ở experimental stage; ecosystem Android tăng mạnh |
| Kotlin 1.2 | 2017 | Multiplatform bắt đầu hình thành rõ hơn |
| Kotlin 1.3 | 2018 | Coroutine trở thành ngôn ngữ (language / 언어) tính năng (feature / 기능) stable; multiplatform/tooling trưởng thành hơn |
| Kotlin 1.4 | 2020 | trình biên dịch (compiler / 컴파일러)/kiểu (type / 타입) suy luận (inference / 추론)/bản dựng (build / 빌드) backend bắt đầu chuyển thế hệ |
| Kotlin 1.5 | 2021 | JVM IR backend mặc định, sealed giao diện (interface / 인터페이스), giá trị (value / 값) lớp (class / 클래스), JVM bản ghi (record / 레코드) hỗ trợ (support / 지원) |
| Kotlin 1.6 | 2021 | `when` exhaustiveness và coroutine-related ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) được siết chặt |
| Kotlin 1.7 | 2022 | K2 Alpha, builder suy luận (inference / 추론) và definitely-non-null types stable |
| Kotlin 1.8 | 2022–2023 | JVM baseline cũ được dọn dẹp; stdlib JVM mục tiêu (target / 대상) chuyển hẳn sang 1.8 |
| Kotlin 1.9 | 2023–2024 | K2 Beta, `data object`, enum `entries`, KMP stable ở 1.9.20 |
| Kotlin 2.0 | 2024 | K2 trình biên dịch (compiler / 컴파일러) Stable; Compose trình biên dịch (compiler / 컴파일러) chuyển vào Kotlin repository |
| Kotlin 2.1 | 2024–2025 | K2 ecosystem/tooling trưởng thành; preview nhiều ngôn ngữ (language / 언어) tính năng (feature / 기능) mới |
| Kotlin 2.2 | 2025 | Nhiều tính năng (feature / 기능) mới stable; di chuyển (migration / 마이그레이션) Gradle DSL mạnh hơn sang `compilerOptions` |
| Kotlin 2.3 | 2025–2026 | Tiếp tục stabilize ngôn ngữ (language / 언어); tường minh (explicit / 명시적) backing trường dữ liệu (field / 필드) xuất hiện experimental |
| Kotlin 2.4 | 2026 | ngữ cảnh (context / 맥락) parameters và tường minh (explicit / 명시적) backing fields stable; Java 26 hỗ trợ (support / 지원) và toolchain mới |

---

# 3. Kotlin 1.0 — nền tảng stable đầu tiên

Kotlin/JVM 1.0 đặt nền móng cho phần lớn cú pháp (syntax / 문법) người dùng vẫn thấy ngày nay:

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

Một điểm đáng chú ý của Kotlin là phần lớn cú pháp (syntax / 문법) nền tảng này không bị thay đổi triệt để khi lên 2.x. Kotlin tiến hóa theo hướng tính tương thích (compatibility / 호환성) tương đối mạnh thay vì liên tục viết lại ngôn ngữ (language / 언어) cốt lõi (core / 핵심).

Vì vậy dự án (project / 프로젝트) Kotlin rất cũ vẫn có thể trông “quen” với nhà phát triển (developer / 개발자) Kotlin hiện tại.

Điều thay đổi mạnh hơn qua các phiên bản (version / 버전) thường nằm ở:

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

Nếu đọc mã (code / 코드) rất cũ, có thể gặp coroutine API hoặc experimental annotation khác xa mã (code / 코드) hiện đại.

Không nên bản sao (copy / 복사) nguyên tutorial Kotlin 1.1/1.2 về coroutine vào dự án (project / 프로젝트) hiện tại.

Mô hình tư duy (mental model / 사고 모델) cần giữ là:

```text
language coroutine support
+
kotlinx.coroutines library
```

là hai tầng (layer / 계층) khác nhau.

Trình biên dịch (compiler / 컴파일러) hiểu `suspend`, máy trạng thái (state machine / 상태 머신) và coroutine ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론); thư viện (library / 라이브러리) cung cấp `CoroutineScope`, `Dispatchers`, `launch`, `async`, luồng (flow / 흐름) và structured-concurrency abstractions.

---

# 5. Kotlin 1.3 — coroutine trở thành nền tảng thực tế

Kotlin 1.3 là một mốc lớn vì coroutine chuyển sang giai đoạn stable đủ để ecosystem sử dụng rộng rãi.

Từ đây Android gradually chuyển từ callback-heavy mã (code / 코드):

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

và structured tính đồng thời (concurrency / 동시성) hiện đại.

Khi maintain dự án (project / 프로젝트) Kotlin đời 1.3, cần để ý:

- coroutine thư viện (library / 라이브러리) phiên bản (version / 버전) có thể rất cũ;
- Android kiến trúc (architecture / 아키텍처) Components khi đó thường dùng LiveData nhiều hơn luồng (flow / 흐름);
- XML/Fragment là UI kiến trúc (architecture / 아키텍처) chính;
- Jetpack Compose chưa phải môi trường vận hành (production / 운영 환경) UI ngăn xếp (stack / 스택).

---

# 6. Kotlin 1.4 — giai đoạn chuyển trình biên dịch (compiler / 컴파일러) backend

Kotlin 1.4 không chỉ thêm cú pháp (syntax / 문법). Đây là thời kỳ trình biên dịch (compiler / 컴파일러) kiến trúc (architecture / 아키텍처) bắt đầu chuyển mạnh sang IR — Intermediate biểu diễn (representation / 표현).

IR giúp Kotlin có kiến trúc (architecture / 아키텍처) trình biên dịch (compiler / 컴파일러) thống nhất hơn giữa JVM, JS, bản địa (native / 네이티브) và về sau là nền tảng quan trọng cho trình biên dịch (compiler / 컴파일러) plugin như Compose.

Kotlin 1.4.30 đưa JVM IR backend lên Beta.

Đây là ví dụ quan trọng cho cách đọc phiên bản (version / 버전) lịch sử (history / 이력):

```text
user-visible syntax chỉ thay đổi ít
nhưng generated bytecode/compiler plugin behavior có thể thay đổi lớn
```

Vì vậy di chuyển (migration / 마이그레이션) Kotlin không chỉ cần compile mã nguồn (source code / 소스 코드); với dự án (project / 프로젝트) có serialization/reflection/trình biên dịch (compiler / 컴파일러) plugin/R8 cần kiểm thử (test / 테스트) hành vi thời gian chạy (runtime behavior / 런타임 동작).

---

# 7. Kotlin 1.5 — JVM IR mặc định và hiện đại (modern / 현대적) kiểu (type / 타입) modeling

Kotlin 1.5 là một bản phát hành (release / 릴리스) rất quan trọng đối với Android/JVM.

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **7.1 JVM IR backend trở thành mặc định** nối từ **2. Timeline tổng quan Kotlin** sang **7.2 Sealed giao diện (interface / 인터페이스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.1 JVM IR backend trở thành mặc định

Trước 1.5, JVM trình biên dịch (compiler / 컴파일러) dùng backend cũ theo default.

Từ Kotlin 1.5, IR backend trở thành stable/default.

Điều này ảnh hưởng tới:

- bytecode shape;
- trường dữ liệu (field / 필드) thứ tự (ordering / 순서);
- trình biên dịch (compiler / 컴파일러) plugin tích hợp (integration / 통합);
- incremental bản dựng (build / 빌드);
- reflection/serialization trường hợp biên (edge case / 경계 사례);
- R8/proguard hành vi (behavior / 동작) trong một số dự án (project / 프로젝트) legacy.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **7.2 Sealed giao diện (interface / 인터페이스)** nối từ **7.1 JVM IR backend trở thành mặc định** sang **7.3 giá trị (value / 값) lớp (class / 클래스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.2 Sealed giao diện (interface / 인터페이스)

Hiện đại (modern / 현대적) Kotlin có thể viết:

```kotlin
sealed interface UiState

data object Loading : UiState

data class Content(val items: List<Item>) : UiState

data class Error(val message: String) : UiState
```

`sealed interface` stable từ Kotlin 1.5.

Dự án (project / 프로젝트) cũ có thể dùng `sealed class` ở những nơi hiện nay giao diện (interface / 인터페이스) phù hợp hơn.

---

> **Nối mạch:** Trong **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **7.3 giá trị (value / 값) lớp (class / 클래스)** nối từ **7.2 Sealed giao diện (interface / 인터페이스)** sang **7.4 JVM records**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.3 giá trị (value / 값) lớp (class / 클래스)

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```kotlin
@JvmInline
value class UserId(val value: String)
```

Giá trị (value / 값) lớp (class / 클래스) cho phép tạo strong lĩnh vực (domain / 도메인) kiểu (type / 타입) mà nhiều trường hợp không cần allocation wrapper thông thường.

Mã (code / 코드) rất cũ có thể gọi chúng là **inline lớp (class / 클래스)**.

Mental di chuyển (migration / 마이그레이션):

```text
inline class   → legacy naming
value class    → modern naming
```

---

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **7.4 JVM records** nối từ **7.3 giá trị (value / 값) lớp (class / 클래스)** sang **11.1 Enum.entries**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.4 JVM records

Kotlin 1.5 bổ sung interop với Java bản ghi (record / 레코드):

```kotlin
@JvmRecord
data class Point(val x: Int, val y: Int)
```

Điều này quan trọng khi Kotlin thư viện (library / 라이브러리) phải expose mô hình (model / 모델) cho Java ecosystem.

---

# 8. Kotlin 1.6 — exhaustive `when` và stricter tính đúng đắn (correctness / 정확성)

Kotlin 1.6 bắt đầu siết nhiều ngữ nghĩa (semantic / 의미적) quy tắc (rule / 규칙) mà mã (code / 코드) cũ từng được phép bỏ qua.

Ví dụ với sealed hierarchy:

```kotlin
sealed interface Result

data object Success : Result
data object Failure : Result
```

Hiện đại (modern / 현대적) mã (code / 코드) nên viết exhaustive `when`:

```kotlin
when (result) {
    Success -> showSuccess()
    Failure -> showFailure()
}
```

Trình biên dịch (compiler / 컴파일러) dần chuyển những trường hợp non-exhaustive từ warning sang lỗi (error / 오류) qua bản phát hành (release / 릴리스) cycle.

Đây là mẫu (pattern / 패턴) thường gặp trong Kotlin evolution:

```text
allow
→ warning
→ stronger warning/progressive error
→ compile error
```

Do đó khi upgrade nhiều phiên bản (version / 버전) một lúc, warnings của phiên bản (version / 버전) cũ không nên bị xem nhẹ.

---

# 9. Kotlin 1.7 — K2 xuất hiện

Kotlin 1.7.0 đưa K2 trình biên dịch (compiler / 컴파일러) ra Alpha cho JVM.

K2 không chỉ là “trình biên dịch (compiler / 컴파일러) nhanh hơn”. Mục tiêu lớn hơn là:

```text
một compiler frontend mới
→ architecture nhất quán hơn
→ type analysis tốt hơn
→ compiler-extension API tốt hơn
→ dễ phát triển language feature mới hơn
→ unify platform behavior tốt hơn
```

Tại 1.7, K2 chưa phù hợp cho môi trường vận hành (production / 운영 환경) Android thông thường vì trình biên dịch (compiler / 컴파일러) plugin hỗ trợ (support / 지원) còn hạn chế.

Cùng thời kỳ này, các tính năng (feature / 기능) như:

- builder suy luận (inference / 추론);
- definitely non-null types;
- opt-in requirements

được stabilize.

Definitely non-null kiểu (type / 타입) đặc biệt quan trọng khi làm generic Java interop:

```kotlin
T & Any
```

Nó biểu diễn generic `T` nhưng bắt buộc non-null ở ranh giới (boundary / 경계) cần thiết.

---

# 10. Kotlin 1.8 — bỏ legacy JVM baseline

Kotlin 1.8 là mốc dễ thấy khi maintain bản dựng (build / 빌드) cũ.

Thư viện chuẩn (standard library / 표준 라이브러리) chuyển sang JVM mục tiêu (target / 대상) 1.8 và không còn giữ baseline JVM 1.6/1.7.

Các sản phẩm tạo ra (artifact / 산출물) riêng:

```text
kotlin-stdlib-jdk7
kotlin-stdlib-jdk8
```

không còn cần khai báo như trước vì functionality đã được nhập vào `kotlin-stdlib`.

Nếu thấy bản dựng (build / 빌드) cũ có:

```kotlin
implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8:...")
```

hãy hiểu đó thường là dấu hiệu dự án (project / 프로젝트) đến từ thế hệ cũ, không phải template nên tiếp tục bản sao (copy / 복사).

---

# 11. Kotlin 1.9 — cầu nối (bridge / 브리지) giữa K1 và K2

Kotlin 1.9 là thế hệ cuối rất phổ biến trước Kotlin 2.x.

Nhiều môi trường vận hành (production / 운영 환경) Android codebase hiện nay vẫn có lịch sử từ 1.9.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **11.1 Enum.entries** nối từ **7.4 JVM records** sang **11.2 data object**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11.1 `Enum.entries`

Legacy:

```kotlin
Color.values()
```

Hiện đại (modern / 현대적):

```kotlin
Color.entries
```

`entries` stable ở Kotlin 1.9 và tránh tạo array mới như `values()` trong nhiều trường hợp.

---

> **Nối mạch:** Trong **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **11.2 data object** nối từ **11.1 Enum.entries** sang **11.3 Open-ended phạm vi (range / 범위)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11.2 `data object`

Legacy sealed trạng thái (state / 상태) thường viết:

```kotlin
object Loading : UiState
```

Hiện đại (modern / 현대적) Kotlin có thể dùng:

```kotlin
data object Loading : UiState
```

`data object` tạo hành vi (behavior / 동작) `toString`/`equals`/`hashCode` đối xứng hơn với `data class` trong sealed hierarchy.

---

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **11.3 Open-ended phạm vi (range / 범위)** nối từ **11.2 data object** sang **11.4 K2 Beta**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11.3 Open-ended phạm vi (range / 범위)

Mục này biến quy tắc collection thành hành vi có thể quan sát. Hãy đối chiếu kiểu dữ liệu, thứ tự duyệt, mutation và kết quả cuối để biết lựa chọn API nào giữ đúng contract của bài toán.

```kotlin
0..<size
```

trở thành cú pháp (syntax / 문법) rõ ràng cho phạm vi (range / 범위) loại trừ upper bound.

So với:

```kotlin
0 until size
```

cả hai đều có thể gặp trong codebase.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **11.4 K2 Beta** nối từ **11.3 Open-ended phạm vi (range / 범위)** sang **11.5 Kotlin Multiplatform stable**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11.4 K2 Beta

K2 tiến từ Alpha sang Beta trong thế hệ 1.9.

Điều này báo hiệu Kotlin 2.0 sắp đổi trình biên dịch (compiler / 컴파일러) frontend mặc định.

---

> **Nối mạch:** Trong **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **11.5 Kotlin Multiplatform stable** nối từ **11.4 K2 Beta** sang **12.1 K2 trở thành trình biên dịch (compiler / 컴파일러) chính**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11.5 Kotlin Multiplatform stable

Kotlin 1.9.20 là mốc quan trọng khi Kotlin Multiplatform được JetBrains công bố Stable.

Điều này không có nghĩa mọi mục tiêu (target / 대상)/thư viện (library / 라이브러리)/interoperability tính năng (feature / 기능) KMP đều stable; cần phân biệt stability của **nền tảng (platform / 플랫폼)/sản phẩm (product / 제품)** với từng tính năng (feature / 기능) cụ thể.

---

# 12. Kotlin 2.0 — mốc chuyển thế hệ

Kotlin 2.0.0 phát hành ngày 2024-05-21 và đánh dấu K2 trình biên dịch (compiler / 컴파일러) Stable.

Đây là mốc lớn nhất kể từ Kotlin 1.0 nếu nhìn từ trình biên dịch (compiler / 컴파일러) kiến trúc (architecture / 아키텍처).

---

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **12.1 K2 trở thành trình biên dịch (compiler / 컴파일러) chính** nối từ **11.5 Kotlin Multiplatform stable** sang **12.2 Compose trình biên dịch (compiler / 컴파일러) chuyển vào Kotlin repository**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12.1 K2 trở thành trình biên dịch (compiler / 컴파일러) chính

K2 cải thiện:

- frontend kiến trúc (architecture / 아키텍처);
- phân tích (analysis / 분석);
- kiểu (type / 타입) suy luận (inference / 추론) consistency;
- trình biên dịch (compiler / 컴파일러) hiệu năng (performance / 성능);
- compiler-plugin foundation;
- multiplatform trình biên dịch (compiler / 컴파일러) consistency.

Nhưng di chuyển (migration / 마이그레이션) 1.9 → 2.0 không nên được xem là chỉ đổi số phiên bản (version / 버전).

Cần kiểm thử (test / 테스트):

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **12.2 Compose trình biên dịch (compiler / 컴파일러) chuyển vào Kotlin repository** nối từ **12.1 K2 trở thành trình biên dịch (compiler / 컴파일러) chính** sang **13.1 kapt và K2**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12.2 Compose trình biên dịch (compiler / 컴파일러) chuyển vào Kotlin repository

Đây là thay đổi cực kỳ quan trọng với Android.

### Trước Kotlin 2.0

Compose trình biên dịch (compiler / 컴파일러) có bản phát hành (release / 릴리스)/phiên bản (version / 버전) ánh xạ (mapping / 매핑) riêng với Kotlin trình biên dịch (compiler / 컴파일러).

Nhà phát triển (developer / 개발자) phải kiểm tra tính tương thích (compatibility / 호환성) map:

```text
Kotlin version
↔ Compose compiler extension version
```

Cấu hình (config / 설정) cũ có thể trông như:

```kotlin
android {
    composeOptions {
        kotlinCompilerExtensionVersion = "..."
    }
}
```

### Từ Kotlin 2.0+

Compose trình biên dịch (compiler / 컴파일러) nằm cùng Kotlin repository và có Gradle plugin riêng:

```kotlin
plugins {
    id("org.jetbrains.kotlin.android") version "2.4.20"
    id("org.jetbrains.kotlin.plugin.compose") version "2.4.20"
}
```

Mô hình tư duy (mental model / 사고 모델) mới:

```text
Kotlin 2.x
↔ Compose compiler plugin cùng Kotlin version
```

Jetpack Compose libraries vẫn có phiên bản (version / 버전)/BOM riêng.

Do đó phải phân biệt:

```text
Compose compiler version
!=
Compose UI library version
```

---

# 13. Kotlin 2.1 — K2 ecosystem trưởng thành

Kotlin 2.1 tiếp tục hoàn thiện K2 và giới thiệu preview cho nhiều ngôn ngữ (language / 언어) tính năng (feature / 기능) mới.

Ví dụ:

- guard điều kiện (condition / 조건) trong `when`;
- non-local `break`/`continue`;
- multi-dollar string interpolation.

Ví dụ guard điều kiện (condition / 조건):

```kotlin
when (user) {
    is User.Admin if user.enabled -> showAdmin()
    is User.Admin -> showDisabledAdmin()
    else -> showNormalUser()
}
```

Ở thời điểm 2.1 đây là preview; các tính năng (feature / 기능) sau đó được stabilize ở bản phát hành (release / 릴리스) sau.

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

> **Nối mạch:** Trong **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **13.1 kapt và K2** nối từ **12.2 Compose trình biên dịch (compiler / 컴파일러) chuyển vào Kotlin repository** sang **14.1 kotlinOptions {} chuyển sang compilerOptions {}**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13.1 kapt và K2

Kotlin 2.1.20 đưa K2 hiện thực (implementation / 구현) của kapt thành mặc định.

Tuy vậy với Android dự án (project / 프로젝트) hiện đại, nếu annotation processor hỗ trợ KSP thì thường nên đánh giá di chuyển (migration / 마이그레이션):

```text
kapt → KSP
```

Không phải vì kapt lập tức “không dùng được”, mà vì KSP thường tích hợp tốt hơn với Kotlin symbol mô hình (model / 모델) và bản dựng (build / 빌드) hiệu năng (performance / 성능).

---

# 14. Kotlin 2.2 — hiện đại (modern / 현대적) trình biên dịch (compiler / 컴파일러) DSL và dọn legacy ngôn ngữ (language / 언어) levels

Kotlin 2.2 tiếp tục ổn định các tính năng (feature / 기능) từ 2.1.

Một số thay đổi đáng nhớ khi đọc Gradle script:

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **14.1 kotlinOptions {} chuyển sang compilerOptions {}** nối từ **13.1 kapt và K2** sang **14.2 Không giữ ngôn ngữ (language / 언어) mức (level / 수준) quá cũ vô hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Hiện đại (modern / 현대적):

```kotlin
kotlin {
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_17)
    }
}
```

Trong Kotlin 2.2, DSL `kotlinOptions {}` cũ đã bị nâng deprecation mức (level / 수준) mạnh và nên migrate sang `compilerOptions {}`.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **14.2 Không giữ ngôn ngữ (language / 언어) mức (level / 수준) quá cũ vô hạn** nối từ **14.1 kotlinOptions {} chuyển sang compilerOptions {}** sang **16.1 ngữ cảnh (context / 맥락) parameters**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14.2 Không giữ ngôn ngữ (language / 언어) mức (level / 수준) quá cũ vô hạn

Từ Kotlin 2.2, trình biên dịch (compiler / 컴파일러) không còn hỗ trợ `language-version=1.6` và `1.7`.

Điều này quan trọng cho enterprise codebase:

```text
compiler mới
không thể mãi đóng băng source ở language mode cực cũ
```

Upgrade chiến lược (strategy / 전략) nên thường xuyên nâng từng bước thay vì nhảy 5–7 năm một lần.

---

# 15. Kotlin 2.3 — stabilization và tường minh (explicit / 명시적) backing trường dữ liệu (field / 필드)

Kotlin 2.3 tiếp tục ổn định tính năng (feature / 기능) mới và giới thiệu **tường minh (explicit / 명시적) backing trường dữ liệu (field / 필드)** ở trạng thái experimental.

Mẫu (pattern / 패턴) cũ:

```kotlin
private val _state = MutableStateFlow<State>(State.Loading)
val state: StateFlow<State> = _state
```

Tường minh (explicit / 명시적) backing trường dữ liệu (field / 필드) mô hình (model / 모델):

```kotlin
val state: StateFlow<State>
    field = MutableStateFlow(State.Loading)
```

Trong private phạm vi (scope / 범위), trình biên dịch (compiler / 컴파일러) có thể hiểu backing trường dữ liệu (field / 필드) có hiện thực (implementation / 구현) kiểu (type / 타입) cụ thể hơn.

Điểm quan trọng khi đọc phiên bản (version / 버전) lịch sử (history / 이력):

```text
2.3 introduced/experimented
2.4 stabilized
```

không nên viết tài liệu như thể tính năng (feature / 기능) đã Stable ngay từ ngày đầu xuất hiện.

---

# 16. Kotlin 2.4 — baseline hiện tại của bộ ghi chú (note / 노트)

Kotlin 2.4 là baseline chính của thư viện (library / 라이브러리) tại thời điểm tháng 9/2026.

Stable bản phát hành (release / 릴리스) dùng trong tài liệu:

```text
Kotlin 2.4.20
```

Các điểm nổi bật của 2.4 generation:

- ngữ cảnh (context / 맥락) parameters trở thành Stable;
- tường minh (explicit / 명시적) backing fields trở thành Stable;
- annotation use-site mục tiêu (target / 대상) được cải thiện;
- Java 26 hỗ trợ (support / 지원) trên Kotlin/JVM;
- trình biên dịch (compiler / 컴파일러)/tooling/Gradle tích hợp (integration / 통합) tiếp tục hiện đại hóa;
- Kotlin/bản địa (native / 네이티브), JS, Wasm và build-tools API tiếp tục tiến hóa.

---

> **Nối mạch:** Trong **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **16.1 ngữ cảnh (context / 맥락) parameters** nối từ **14.2 Không giữ ngôn ngữ (language / 언어) mức (level / 수준) quá cũ vô hạn** sang **16.2 tường minh (explicit / 명시적) backing trường dữ liệu (field / 필드) stable**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16.1 ngữ cảnh (context / 맥락) parameters

Ngữ cảnh (context / 맥락) parameters giúp truyền phụ thuộc (dependency / 의존성)/ngữ cảnh (context / 맥락) theo lexical ngữ cảnh (context / 맥락) mà không buộc đưa mọi thứ thành parameter trực tiếp hoặc toàn cục (global / 전역) singleton.

Ví dụ conceptual:

```kotlin
context(logger: Logger)
fun saveUser(user: User) {
    logger.info("saving ${user.id}")
}
```

Đây không phải lý do để thay toàn bộ constructor injection/Hilt.

Nên xem ngữ cảnh (context / 맥락) parameters như một ngôn ngữ (language / 언어) cơ chế (mechanism / 메커니즘) mới cho những API phù hợp, đặc biệt DSL/thư viện (library / 라이브러리)/lĩnh vực (domain / 도메인) ngữ cảnh (context / 맥락); lifecycle-heavy Android dependencies vẫn cần quyền sở hữu (ownership / 소유권) rõ ràng.

---

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **16.1 ngữ cảnh (context / 맥락) parameters** đặt vấn đề; **16.2 tường minh (explicit / 명시적) backing trường dữ liệu (field / 필드) stable** đối chiếu bằng chứng, rồi **16.3 when compilation qua invokedynamic** mở rộng hệ quả hoặc giới hạn liên quan.

## 16.2 tường minh (explicit / 명시적) backing trường dữ liệu (field / 필드) stable

Hiện đại (modern / 현대적) mã (code / 코드) có thể giảm boilerplate trong một số API dạng mutable-inside/read-only-outside.

Tuy nhiên đừng migrate mọi `_state` chỉ vì cú pháp (syntax / 문법) mới tồn tại. Cần cân nhắc:

- readability của nhóm (team / 팀);
- minimum Kotlin phiên bản (version / 버전) của mô-đun (module / 모듈)/thư viện (library / 라이브러리) bên tiêu thụ (consumer / 소비자);
- Java interop;
- API công khai (public API / 공개 API) tính tương thích (compatibility / 호환성);
- mức quen thuộc của nhà phát triển (developer / 개발자).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **16.2 tường minh (explicit / 명시적) backing trường dữ liệu (field / 필드) stable** đặt vấn đề; **16.3 when compilation qua invokedynamic** đối chiếu bằng chứng, rồi **18.1 Compose trình biên dịch (compiler / 컴파일러)** mở rộng hệ quả hoặc giới hạn liên quan.

## 16.3 `when` compilation qua `invokedynamic`

Kotlin 2.4.20 ổn định thêm trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화) cho một số `when` trên JVM 21+ bằng `invokedynamic`.

Đây là ví dụ về tính năng (feature / 기능) phiên bản (version / 버전) mà mã nguồn (source code / 소스 코드) gần như không đổi nhưng generated bytecode/thời gian chạy (runtime / 런타임) chiến lược (strategy / 전략) đổi.

Cấp cao (senior / 시니어) nhà phát triển (developer / 개발자) cần nhớ:

```text
same source
!=
same bytecode
```

đặc biệt khi profiling, reflection, instrumentation hoặc nhị phân (binary / 이진) tooling tham gia.

---

# 17. K1 vs K2 — bảng so sánh mental model
Phần này nối mạch Android vừa học với “17. K1 vs K2 — bảng so sánh mental model”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Khía cạnh | K1 trình biên dịch (compiler / 컴파일러) | K2 trình biên dịch (compiler / 컴파일러) |
|---|---|---|
| Thế hệ | Kotlin 1.x truyền thống | trình biên dịch (compiler / 컴파일러) frontend thế hệ mới |
| môi trường vận hành (production / 운영 환경) mặc định | Trước Kotlin 2.0 | Kotlin 2.0+ |
| Mục tiêu | trình biên dịch (compiler / 컴파일러) kiến trúc (architecture / 아키텍처) ban đầu | Unified/faster/extensible kiến trúc (architecture / 아키텍처) |
| phân tích (analysis / 분석) | Frontend cũ | FIR-based frontend |
| ngôn ngữ (language / 언어) tính năng (feature / 기능) development | Chậm/phức tạp hơn | Thiết kế để tiến hóa dễ hơn |
| trình biên dịch (compiler / 컴파일러) plugin ecosystem | Mature legacy ecosystem | hiện đại (modern / 현대적) ecosystem đang là mặc định |
| Compose trình biên dịch (compiler / 컴파일러) | Tách bản phát hành (release / 릴리스) ánh xạ (mapping / 매핑) | Tích hợp Kotlin repository từ 2.0 |
| kapt | K1 hiện thực (implementation / 구현) truyền thống | K2 hiện thực (implementation / 구현) được đưa thành default ở 2.1.20 |

Không nên nói K1 là “trình biên dịch (compiler / 컴파일러) sai” và K2 là “trình biên dịch (compiler / 컴파일러) đúng”. K1 là trình biên dịch (compiler / 컴파일러) đã vận hành Kotlin ecosystem nhiều năm; K2 là thế hệ kế tiếp nhằm giải quyết quy mô (scale / 규모)/evolution/tooling limitation.

---

# 18. Compose phiên bản (version / 버전) evolution dành cho Android nhà phát triển (developer / 개발자)

Compose có ít nhất ba phiên bản (version / 버전) concern khác nhau.

> **Nối mạch:** Trong **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **18.1 Compose trình biên dịch (compiler / 컴파일러)** nối từ **16.3 when compilation qua invokedynamic** sang **18.2 Compose UI libraries**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18.1 Compose trình biên dịch (compiler / 컴파일러)

Khối minh họa dưới đây đặt Compose compiler vào ma trận version và plugin. Hãy xác định dependency nào phải lockstep, dependency nào chỉ là compatibility mapping và bằng chứng build nào xác nhận kết luận.

```text
< Kotlin 2.0
Compose compiler có compatibility mapping riêng

>= Kotlin 2.0
Compose compiler plugin dùng cùng version với Kotlin
```

Hiện đại (modern / 현대적):

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

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **18.2 Compose UI libraries** nối từ **18.1 Compose trình biên dịch (compiler / 컴파일러)** sang **18.3 Compose và compileSdk**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18.2 Compose UI libraries

Compose UI thời gian chạy (runtime / 런타임)/foundation/material libraries không dùng Kotlin phiên bản (version / 버전) number.

Nên quản lý qua BOM:

```kotlin
val composeBom = platform("androidx.compose:compose-bom:2026.09.00")
implementation(composeBom)
androidTestImplementation(composeBom)
```

Mô hình tư duy (mental model / 사고 모델):

```text
Kotlin 2.4.20
Compose compiler 2.4.20
Compose BOM 2026.09.00
```

ba con số này có thể đồng thời tồn tại và không mâu thuẫn.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **18.3 Compose và compileSdk** nối từ **18.2 Compose UI libraries** sang **Bước 1 — chụp baseline**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18.3 Compose và `compileSdk`

Compose libraries mới dần yêu cầu Android API compile mức (level / 수준) mới hơn.

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

# 19. Android API phiên bản (version / 버전) evolution — không gắn trực tiếp với Kotlin

Kotlin phiên bản (version / 버전) và Android OS phiên bản (version / 버전) độc lập.

Ví dụ Kotlin 2.4 có thể bản dựng (build / 빌드) app chạy trên Android API cũ nếu `minSdk` và thư viện (library / 라이브러리) dependencies cho phép.

Một app Android hiện đại (modern / 현대적) cần lập luận (reasoning / 추론) trên ma trận:

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

Vì vậy lỗi “sau khi cập nhật (update / 업데이트) Kotlin app crash trên Android X” không thể kết luận nguyên nhân là Kotlin chỉ từ tên phiên bản (version / 버전); cần xác định chính xác trục nào đã đổi.

---

# 20. Legacy → hiện đại (modern / 현대적) map

Bảng này rất hữu ích khi đọc mã (code / 코드) Android/Kotlin cũ.

| Legacy / thế hệ cũ | hiện đại (modern / 현대적) direction | Ghi chú |
|---|---|---|
| Java-only Android | Kotlin-first Android | Java vẫn được hỗ trợ (support / 지원) và interop quan trọng |
| Kotlin Android Extensions synthetic view | View Binding / Compose | Synthetic bị loại khỏi hiện đại (modern / 현대적) workflow |
| `findViewById` everywhere | View Binding / Compose | `findViewById` vẫn hợp lệ ở View mã (code / 코드) |
| XML-only UI | Compose + XML interop | XML không “sai”; nhiều app môi trường vận hành (production / 운영 환경) vẫn dùng |
| `AsyncTask` | Coroutine / WorkManager tùy thời gian tồn tại (lifetime / 수명) | `AsyncTask` deprecated |
| callback pyramid | `suspend`, luồng (flow / 흐름) | Callback vẫn cần ở nền tảng (platform / 플랫폼) ranh giới (boundary / 경계) |
| LiveData everywhere | StateFlow/luồng (flow / 흐름) cho hiện đại (modern / 현대적) dữ liệu (data / 데이터)/trạng thái (state / 상태) | LiveData vẫn supported |
| SharedPreferences cho structured settings | DataStore | SharedPreferences chưa biến mất |
| `startActivityForResult` | Activity kết quả (result / 결과) API | hiện đại (modern / 현대적) lifecycle-aware đặc tả hợp đồng (contract / 계약) |
| manual dịch vụ (service / 서비스) cho durable deferred công việc (work / 작업) | WorkManager | dịch vụ (service / 서비스) vẫn đúng với use trường hợp (case / 사례) khác |
| RxJava-heavy Android | Coroutine/luồng (flow / 흐름) phổ biến hơn | RxJava vẫn tồn tại trong legacy/large codebase |
| `kapt` everywhere | KSP khi processor hỗ trợ | kapt vẫn dùng được cho công cụ (tool / 도구) chưa migrate |
| `kotlinOptions {}` | `compilerOptions {}` | hiện đại (modern / 현대적) KGP DSL |
| Compose trình biên dịch (compiler / 컴파일러) tính tương thích (compatibility / 호환성) map | Kotlin Compose trình biên dịch (compiler / 컴파일러) plugin cùng phiên bản (version / 버전) | Kotlin 2.0+ |
| K1 trình biên dịch (compiler / 컴파일러) | K2 trình biên dịch (compiler / 컴파일러) | K2 stable/default từ Kotlin 2.0 |
| `Color.values()` | `Color.entries` | `values()` vẫn tồn tại |
| `object Loading` trong sealed trạng thái (state / 상태) | `data object Loading` khi phù hợp | Không bắt buộc đổi mọi đối tượng (object / 객체) |
| backing thuộc tính (property / 속성) `_state` + công khai (public / 공개) `state` | tường minh (explicit / 명시적) backing trường dữ liệu (field / 필드) có thể dùng | Stable từ 2.4, không phải di chuyển (migration / 마이그레이션) bắt buộc |

---

# 21. mã (code / 코드) cũ không đồng nghĩa mã (code / 코드) sai

Đây là nguyên tắc quan trọng nhất khi học phiên bản (version / 버전).

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

Cấp cao (senior / 시니어) engineer không rewrite mã (code / 코드) chỉ vì phiên bản (version / 버전) number mới hơn. di chuyển (migration / 마이그레이션) cần mua được giá trị cụ thể như:

- giảm bug;
- tăng maintainability;
- giảm bản dựng (build / 빌드) thời gian (time / 시간);
- hỗ trợ (support / 지원) nền tảng (platform / 플랫폼) yêu cầu (requirement / 요구사항) mới;
- bảo mật (security / 보안)/compliance;
- hiệu năng (performance / 성능);
- loại phụ thuộc (dependency / 의존성) deprecated;
- đơn giản hóa kiến trúc (architecture / 아키텍처).

---

# 22. Upgrade Kotlin: không nhảy phiên bản (version / 버전) một cách mù quáng

Một upgrade Kotlin môi trường vận hành (production / 운영 환경) nên theo chuỗi xử lý (pipeline / 파이프라인).

> **Nối mạch:** Trong **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **Bước 1 — chụp baseline** nối từ **18.3 Compose và compileSdk** sang **Bước 2 — đọc tính tương thích (compatibility / 호환성)/bản phát hành (release / 릴리스) notes**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Nếu không có baseline, khi bản dựng (build / 빌드) hỏng sẽ không biết phụ thuộc (dependency / 의존성) axis nào đã thay đổi.

---

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **Bước 2 — đọc tính tương thích (compatibility / 호환성)/bản phát hành (release / 릴리스) notes** nối từ **Bước 1 — chụp baseline** sang **Bước 3 — upgrade trình biên dịch (compiler / 컴파일러)/toolchain trước khi đổi nguồn (source / 소스) style**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bước 2 — đọc tính tương thích (compatibility / 호환성)/bản phát hành (release / 릴리스) notes

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **Bước 2 — đọc tính tương thích (compatibility / 호환성)/bản phát hành (release / 릴리스) notes** đặt vấn đề; **Bước 3 — upgrade trình biên dịch (compiler / 컴파일러)/toolchain trước khi đổi nguồn (source / 소스) style** đối chiếu bằng chứng, rồi **Bước 4 — compile tất cả variants** mở rộng hệ quả hoặc giới hạn liên quan.

## Bước 3 — upgrade trình biên dịch (compiler / 컴파일러)/toolchain trước khi đổi nguồn (source / 소스) style

Tránh cùng một PR vừa:

```text
upgrade Kotlin
+ migrate Compose
+ đổi architecture
+ refactor package
+ đổi targetSdk
```

Nếu lỗi xảy ra, quá nhiều biến thay đổi đồng thời.

Tách di chuyển (migration / 마이그레이션) theo axis giúp forensic debugging dễ hơn.

---

> **Nối mạch:** Trong **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **Bước 3 — upgrade trình biên dịch (compiler / 컴파일러)/toolchain trước khi đổi nguồn (source / 소스) style** đặt vấn đề; **Bước 4 — compile tất cả variants** đối chiếu bằng chứng, rồi **Bước 5 — kiểm thử (test / 테스트) generated-code ranh giới (boundary / 경계)** mở rộng hệ quả hoặc giới hạn liên quan.

## Bước 4 — compile tất cả variants

Không chỉ compile `debug`.

Cần đặc biệt kiểm thử (test / 테스트):

```text
release
minified release
product flavors
benchmark/profile variants
instrumented tests
consumer sample nếu là library
```

Rất nhiều R8/trình biên dịch (compiler / 컴파일러) plugin issue chỉ xuất hiện ở bản phát hành (release / 릴리스).

---

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **Bước 4 — compile tất cả variants** đặt tiêu chí; **Bước 5 — kiểm thử (test / 테스트) generated-code ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Bước 6 — kiểm thử (test / 테스트) nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) nếu publish thư viện (library / 라이브러리)** mở rộng hệ quả.

## Bước 5 — kiểm thử (test / 테스트) generated-code ranh giới (boundary / 경계)

Kiểm tra:

- Room;
- Hilt/Dagger;
- KSP;
- kapt;
- kotlinx.serialization;
- Compose trình biên dịch (compiler / 컴파일러);
- Parcelize;
- custom trình biên dịch (compiler / 컴파일러) plugins.

Trình biên dịch (compiler / 컴파일러) upgrade có thể làm lỗi xuất hiện ở generated mã (code / 코드) trước khi handwritten nguồn (source / 소스) có vấn đề.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **Bước 5 — kiểm thử (test / 테스트) generated-code ranh giới (boundary / 경계)** đặt tiêu chí; **Bước 6 — kiểm thử (test / 테스트) nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) nếu publish thư viện (library / 라이브러리)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Dự án (project / 프로젝트) rất cũ** mở rộng hệ quả.

## Bước 6 — kiểm thử (test / 테스트) nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) nếu publish thư viện (library / 라이브러리)

Thư viện (library / 라이브러리) author phải quan tâm:

```text
source compatibility
binary compatibility
behavioral compatibility
```

App nội bộ compile lại toàn bộ nguồn (source / 소스) có thể không thấy lỗi mà nhị phân (binary / 이진) bên tiêu thụ (consumer / 소비자) cũ sẽ gặp.

---

# 23. Upgrade `targetSdk` là di chuyển (migration / 마이그레이션) khác với upgrade Kotlin

Không nên gộp hai việc này trong mô hình tư duy (mental model / 사고 모델).

```text
Upgrade Kotlin
= language/compiler/toolchain migration

Upgrade targetSdk
= Android platform behavior-contract migration
```

Nếu cùng bản phát hành (release / 릴리스) train phải thực hiện cả hai, nên tách lần ghi nhận (commit / 커밋)/kiểm thử (test / 테스트) ma trận (matrix / 행렬) rõ ràng.

Ví dụ mục tiêu (target / 대상) SDK mới có thể thay đổi:

- permission hành vi (behavior / 동작);
- background thực thi (execution / 실행);
- foreground dịch vụ (service / 서비스) chính sách (policy / 정책);
- notification;
- lưu trữ (storage / 저장소);
- implicit intent/exported hành vi (behavior / 동작);
- cục bộ (local / 로컬) truy cập mạng (network access / 네트워크 접근);
- edge-to-edge/cửa sổ (window / 윈도우) hành vi (behavior / 동작).

Không có liên hệ trực tiếp với việc K2 compile nguồn (source / 소스) như thế nào.

---

# 24. phiên bản (version / 버전) danh mục (catalog / 카탈로그) — nơi quản lý phiên bản (version / 버전) hiện đại (modern / 현대적) Android dự án (project / 프로젝트)

Một dự án (project / 프로젝트) hiện đại thường centralize phiên bản (version / 버전) trong `libs.versions.toml`.

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

Ưu điểm không chỉ là “đỡ viết lặp”. Nó tạo một điểm rà soát (review / 검토) rõ ràng cho toolchain phiên bản (version / 버전).

Tuy nhiên phiên bản (version / 버전) danh mục (catalog / 카탈로그) không tự giải quyết tính tương thích (compatibility / 호환성). Nó chỉ centralize declaration.

---

# 25. phiên bản (version / 버전) tính tương thích (compatibility / 호환성) không nên đoán từ số lớn/nhỏ

Ví dụ sai:

```text
Kotlin 2.4 nên AGP cũng phải 2.4
```

Hoặc:

```text
Compose BOM 2026.09 phải dùng Kotlin 2026.09
```

Các dự án (project / 프로젝트) có nhiều independent bản phát hành (release / 릴리스) train.

Luôn kiểm tra official tính tương thích (compatibility / 호환성)/documentation của từng ranh giới (boundary / 경계):

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

# 26. Progressive chế độ (mode / 모드)

Kotlin hỗ trợ progressive chế độ (mode / 모드) để áp dụng một số ngôn ngữ (language / 언어) fix/deprecation hành vi (behavior / 동작) sớm hơn.

Concept:

```text
normal mode
= ưu tiên migration compatibility

progressive mode
= opt-in sớm vào correction/change mới
```

Thư viện (library / 라이브러리)/ứng dụng (application / 애플리케이션) nhóm (team / 팀) có thể dùng progressive chế độ (mode / 모드) để phát hiện technical debt sớm hơn, nhưng cần kiểm thử (test / 테스트) trình biên dịch (compiler / 컴파일러)/plugin tính tương thích (compatibility / 호환성).

Không bật chỉ vì “hiện đại (modern / 현대적) hơn”. Nó là chính sách (policy / 정책) quyết định (decision / 결정) của codebase.

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

Phiên bản (version / 버전) di chuyển (migration / 마이그레이션) phải inventory experimental API vì chúng có tính tương thích (compatibility / 호환성) guarantee thấp hơn Stable API.

Nếu dự án (project / 프로젝트) dùng nhiều:

```text
-X...
experimental annotations
internal compiler flag
unstable plugin API
```

thì upgrade rủi ro (risk / 위험) cao hơn dự án (project / 프로젝트) chỉ dùng stable surface.

---

# 28. phiên bản (version / 버전) chiến lược (strategy / 전략) cho Android ứng dụng (application / 애플리케이션)

Ứng dụng (application / 애플리케이션) có lợi thế là thường compile toàn bộ mã (code / 코드) cùng một toolchain.

Recommended chiến lược (strategy / 전략):

```text
1. Theo dõi stable Kotlin line
2. Không trì hoãn nhiều major generations
3. Upgrade compiler plugins cùng compatibility window
4. Giữ AGP/Gradle/JDK trong supported matrix
5. Compile release/minified variant trong CI
6. Tách Kotlin upgrade khỏi targetSdk migration khi có thể
7. Benchmark nếu compiler/generated-code/runtime behavior thay đổi đáng kể
```

Không cần chạy phiên bản (version / 버전) mới trong ngày đầu bản phát hành (release / 릴리스) nếu sản phẩm (product / 제품) rủi ro (risk / 위험) cao. Nhưng cũng không nên ở lại bản phát hành (release / 릴리스) line quá cũ tới khi cả trình biên dịch (compiler / 컴파일러), AGP và dependencies cùng hết hỗ trợ (support / 지원).

---

# 29. phiên bản (version / 버전) chiến lược (strategy / 전략) cho Android/Kotlin thư viện (library / 라이브러리)

Thư viện (library / 라이브러리) cần conservative hơn ứng dụng (application / 애플리케이션) vì bên tiêu thụ (consumer / 소비자) có thể dùng toolchain khác.

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

Một thư viện (library / 라이브러리) nâng ngôn ngữ (language / 언어)/API phiên bản (version / 버전) có thể vô tình loại bên tiêu thụ (consumer / 소비자) cũ dù API công khai (public API / 공개 API) nhìn không thay đổi.

Do đó trước publish nên kiểm thử (test / 테스트) ma trận (matrix / 행렬) ít nhất:

```text
old supported consumer
current consumer
minified consumer
Java consumer nếu public API hỗ trợ Java
```

---

# 30. hiện tại (current / 현재) baseline — September 2026

Snapshot dùng để đọc repository này:

| Thành phần | Baseline |
|---|---|
| Kotlin | `2.4.20` |
| Kotlin trình biên dịch (compiler / 컴파일러) generation | K2 |
| Compose trình biên dịch (compiler / 컴파일러) | Kotlin Compose trình biên dịch (compiler / 컴파일러) plugin cùng Kotlin phiên bản (version / 버전) |
| Compose BOM | `2026.09.00` |
| Android Studio | Quail 4 / `2026.1.4 Patch 1` |
| Android Gradle Plugin | `9.4.1` |
| Android nền tảng (platform / 플랫폼) tham chiếu (reference / 참조) | Android 17 / API 37 |
| Google Play ordinary app mục tiêu (target / 대상) yêu cầu (requirement / 요구사항) | API 36+ từ 2026-08-31 |

Đây là **documentation snapshot**, không phải hardcoded kiến trúc (architecture / 아키텍처) quy tắc (rule / 규칙).

---

# 31. Checklist khi gặp một dự án (project / 프로젝트) Kotlin/Android lạ

Trước khi đọc mã (code / 코드) sâu, hãy xác định phiên bản (version / 버전) fingerprint.

### Hệ thống dựng (build system / 빌드 시스템)

Khối minh họa dưới đây là fingerprint để nhận diện thế hệ project. Hãy đọc từng dấu hiệu như một câu hỏi chẩn đoán trước khi chọn hướng migration.

```text
Gradle wrapper version?
AGP version?
KGP/Kotlin version?
JDK/toolchain?
Groovy DSL hay Kotlin DSL?
Version Catalog có không?
```

### Kotlin

Khối minh họa dưới đây là fingerprint của Kotlin compiler/toolchain. Hãy dùng nó để phân biệt K1/K2, API level và cách Compose compiler được gắn vào build.

```text
K1 hay K2 generation?
languageVersion/apiVersion?
jvmTarget?
kapt hay KSP?
Compose compiler setup kiểu cũ hay Kotlin 2.x plugin?
```

### Android

Khối minh họa dưới đây là fingerprint của Android platform. Hãy tách minSdk, compileSdk, targetSdk và framework behavior trước khi kết luận project tương thích tới đâu.

```text
minSdk?
compileSdk?
targetSdk?
View/XML hay Compose?
Fragment-heavy hay single-activity Compose?
```

### Kiến trúc (architecture / 아키텍처) generation

Khối minh họa dưới đây gom các dấu hiệu architecture generation để đọc project cũ. Hãy dùng chúng để chọn seam migration và giữ nguyên phần chưa cần đổi.

```text
callbacks / AsyncTask?
RxJava?
LiveData?
coroutine/Flow?
Room?
DataStore?
WorkManager?
```

Chỉ cần fingerprint này đã giúp ước lượng dự án (project / 프로젝트) thuộc thế hệ nào và di chuyển (migration / 마이그레이션) debt nằm ở đâu.

---

# 32. Cách đọc nhanh mã (code / 코드) theo generation

> **Nối mạch:** Trong **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **Dự án (project / 프로젝트) rất cũ** nối từ **Bước 6 — kiểm thử (test / 테스트) nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) nếu publish thư viện (library / 라이브러리)** sang **Dự án (project / 프로젝트) transitional**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dự án (project / 프로젝트) rất cũ

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

Không được rewrite ngay. Trước hết xác định kiểm thử (test / 테스트) coverage và hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약).

---

> **Nối mạch:** Ở chặng này của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **Dự án (project / 프로젝트) transitional** nối từ **Dự án (project / 프로젝트) rất cũ** sang **Dự án (project / 프로젝트) hiện đại (modern / 현대적)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dự án (project / 프로젝트) transitional

Dấu hiệu:

```text
Kotlin 1.8/1.9
Flow + LiveData cùng tồn tại
XML + Compose coexist
kapt + KSP coexist
ViewModel modern nhưng navigation cũ
```

Đây là trạng thái rất phổ biến ở môi trường vận hành (production / 운영 환경).

Di chuyển (migration / 마이그레이션) nên incremental.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android phiên bản (version / 버전) Evolution — từ Kotlin 1.x đến 2.4 và cách đọc dự án (project / 프로젝트) cũ/mới**, **Dự án (project / 프로젝트) hiện đại (modern / 현대적)** nối từ **Dự án (project / 프로젝트) transitional** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dự án (project / 프로젝트) hiện đại (modern / 현대적)

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

Nhưng “hiện đại (modern / 현대적) ngăn xếp (stack / 스택)” vẫn không bảo đảm kiến trúc (architecture / 아키텍처) tốt. quyền sở hữu trạng thái (state ownership / 상태 소유권), thời gian tồn tại (lifetime / 수명), consistency, testing và bản phát hành (release / 릴리스) discipline vẫn quyết định chất lượng.

---

# 33. phiên bản (version / 버전) timeline nên được dùng như thế nào khi học

Không cần học thuộc ngày bản phát hành (release / 릴리스).

Điều nên nhớ là **các mốc chuyển mô hình tư duy (mental model / 사고 모델)**:

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

Phiên bản (version / 버전) lịch sử (history / 이력) có giá trị vì nó giải thích **vì sao codebase cũ có hình dạng hiện tại**, không phải để đánh giá mã (code / 코드) cũ bằng tiêu chuẩn hiện đại mà không xét bối cảnh.

---

# 34. cấp cao (senior / 시니어) Notes — phiên bản (version / 버전) là một phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)

Ở mức cấp cao (senior / 시니어)/Master, đừng nhìn phiên bản (version / 버전) thành một danh sách (list / 목록):

```text
Kotlin 2.4.20
AGP 9.4.1
Gradle X
```

Hãy nhìn chúng thành phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프):

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

Một phiên bản (version / 버전) thay đổi (change / 변경) ở nút (node / 노드) trên có thể cascade xuống nhiều nút (node / 노드) khác.

Đó là lý do upgrade môi trường vận hành (production / 운영 환경) cần:

```text
compatibility matrix
+ isolated change
+ full variant build
+ migration tests
+ performance evidence
+ rollout observability
```

chứ không phải chỉ sửa phiên bản (version / 버전) string tới khi Gradle hết báo đỏ.

---

# 35. Nguồn chính thức nên kiểm tra khi cập nhật (update / 업데이트) tệp (file / 파일) này

Khi phiên bản (version / 버전) thay đổi, ưu tiên các nguồn chính thức sau:

- Kotlin quy trình phát hành (release process / 릴리스 프로세스): `https://kotlinlang.org/docs/releases.html`
- Kotlin What's New: `https://kotlinlang.org/docs/whatsnew24.html` và các bản phát hành (release / 릴리스) tương ứng
- Kotlin tính tương thích (compatibility / 호환성) guides: `https://kotlinlang.org/docs/compatibility-guides.html`
- Kotlin ngôn ngữ (language / 언어) features/proposals: `https://kotlinlang.org/docs/kotlin-language-features-and-proposals.html`
- Compose trình biên dịch (compiler / 컴파일러) di chuyển (migration / 마이그레이션): `https://kotlinlang.org/docs/compose-compiler-migration-guide.html`
- Android Compose trình biên dịch (compiler / 컴파일러) setup: `https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler`
- Android Gradle Plugin bản phát hành (release / 릴리스) notes và API hỗ trợ (support / 지원): Android Developers
- Android hành vi (behavior / 동작) changes theo OS/mục tiêu (target / 대상) SDK: Android Developers

Mỗi lần baseline trong README thay đổi, tệp (file / 파일) phiên bản (version / 버전) evolution này cũng nên được rà soát (review / 검토) để tránh tình trạng README nói toolchain mới nhưng di chuyển (migration / 마이그레이션) guide vẫn dừng ở thế hệ cũ.

> **Bàn giao:** Sau **Dự án (project / 프로젝트) hiện đại (modern / 현대적)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
