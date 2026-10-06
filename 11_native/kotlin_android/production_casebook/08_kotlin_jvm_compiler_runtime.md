# Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**. Route đi từ source → K2 frontend/backend → generated code, bytecode và JVM/Android runtime → erasure, boxing, suspend state machine, R8/KSP/KAPT → ABI/metadata debugging, để abstraction leak được truy tìm theo pipeline.

Kotlin giúp Android mã (code / 코드) ngắn và an toàn hơn Java, nhưng môi trường vận hành (production / 운영 환경) bug khó thường nằm dưới lớp trừu tượng (abstraction / 추상화): generic bị kiểu (type / 타입) erasure, giá trị (value / 값) lớp (class / 클래스) bị boxing, `suspend` thành máy trạng thái (state machine / 상태 머신), lambda capture giữ đối tượng (object / 객체) lâu hơn dự kiến, reflection bị R8 strip siêu dữ liệu (metadata / 메타데이터), annotation đặt sai use-site mục tiêu (target / 대상), KSP/KAPT sinh mã (code / 코드) khác phiên bản (version / 버전), hoặc một thư viện (library / 라이브러리) đổi công khai (public / 공개) ABI dù nguồn (source / 소스) nhìn gần giống.

Không cần đọc bytecode mỗi ngày. Mục tiêu chương này là biết **khi nào lớp trừu tượng (abstraction / 추상화) leak** và có mô hình tư duy (mental model / 사고 모델) đủ để gỡ lỗi (debug / 디버그).

## 1. Kotlin trên Android không chạy “trực tiếp” như nguồn (source / 소스)

Luồng (flow / 흐름) khái quát:

```text
Kotlin source
→ Kotlin compiler frontend/analysis (K2)
→ JVM bytecode / compiler-generated structures
→ D8/R8 transform, desugar, shrink, optimize
→ DEX
→ Android Runtime (ART)
```

Compose, serialization, Parcelize, DI/mã (code / 코드) generation hoặc KSP processor có thể thêm generated mã (code / 코드)/trình biên dịch (compiler / 컴파일러) transformation trong chuỗi xử lý (pipeline / 파이프라인).

Vì vậy bug bản dựng (build / 빌드)/thời gian chạy (runtime / 런타임) đôi khi không thể hiểu chỉ từ `.kt` nguồn (source / 소스).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **1. Kotlin trên Android không chạy “trực tiếp” như nguồn (source / 소스)** đặt vấn đề; **2. K2 là trình biên dịch (compiler / 컴파일러) frontend, không phải “Kotlin 2 cú pháp (syntax / 문법)” đơn thuần** đối chiếu bằng chứng, rồi **3. Kotlin siêu dữ liệu (metadata / 메타데이터)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. K2 là trình biên dịch (compiler / 컴파일러) frontend, không phải “Kotlin 2 cú pháp (syntax / 문법)” đơn thuần

Kotlin 2.x chuyển trình biên dịch (compiler / 컴파일러) frontend sang K2. Điều nhà phát triển (developer / 개발자) cần quan tâm là ecosystem tính tương thích (compatibility / 호환성): Kotlin phiên bản (version / 버전), AGP, Compose trình biên dịch (compiler / 컴파일러) tích hợp (integration / 통합), serialization plugin, KSP, annotation processor và thư viện (library / 라이브러리) siêu dữ liệu (metadata / 메타데이터) phải tương thích.

Khi upgrade Kotlin, hãy coi đó là toolchain di chuyển (migration / 마이그레이션):

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

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **2. K2 là trình biên dịch (compiler / 컴파일러) frontend, không phải “Kotlin 2 cú pháp (syntax / 문법)” đơn thuần** đặt vấn đề; **3. Kotlin siêu dữ liệu (metadata / 메타데이터)** đối chiếu bằng chứng, rồi **4. suspend không tạo luồng thực thi (thread / 스레드)** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. Kotlin siêu dữ liệu (metadata / 메타데이터)

Kotlin lớp (class / 클래스) trên JVM mang siêu dữ liệu (metadata / 메타데이터) để tooling/trình biên dịch (compiler / 컴파일러) hiểu tính năng (feature / 기능) Kotlin mà Java bytecode thuần không biểu diễn đầy đủ. Reflection/thư viện (library / 라이브러리) tooling có thể đọc siêu dữ liệu (metadata / 메타데이터).

R8/proguard hoặc shading nếu xử lý sai siêu dữ liệu (metadata / 메타데이터)/annotation có thể làm reflection khung phần mềm (framework / 프레임워크) thất bại (fail / 실패). Đây là lý do keep quy tắc (rule / 규칙) phải dựa vào cơ chế thư viện (library / 라이브러리) thật chứ không bản sao (copy / 복사) một quy tắc (rule / 규칙) toàn cục (global / 전역).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **3. Kotlin siêu dữ liệu (metadata / 메타데이터)** đặt vấn đề; **4. suspend không tạo luồng thực thi (thread / 스레드)** đối chiếu bằng chứng, rồi **5. Suspend không làm blocking code thành non-blocking** mở rộng hệ quả hoặc giới hạn liên quan.

## 4. `suspend` không tạo luồng thực thi (thread / 스레드)

Một `suspend fun` được trình biên dịch (compiler / 컴파일러) biến thành dạng continuation/máy trạng thái (state machine / 상태 머신). Nó có thể pause và resume mà không khối (block / 블록) luồng thực thi (thread / 스레드), nếu hiện thực (implementation / 구현) gọi API suspending/non-blocking đúng.

Conceptual transformation:

```kotlin
suspend fun load(): Result {
    val a = apiA()
    val b = apiB(a)
    return combine(a, b)
}
```

Trình biên dịch (compiler / 컴파일러) cần lưu cục bộ (local / 로컬) trạng thái (state / 상태) giữa suspension điểm (point / 지점), gần giống một máy trạng thái (state machine / 상태 머신):

```text
state 0 -> call apiA -> suspend
resume -> state 1 -> call apiB -> suspend
resume -> state 2 -> combine -> return
```

Điều này giải thích tại sao dấu vết ngăn xếp (stack trace / 스택 트레이스) coroutine có hình dạng khác synchronous lời gọi (call / 호출) và tại sao cục bộ (local / 로컬) variable cần survive suspension.

> **Nối mạch:** `suspend` không tạo thread và không biến blocking call thành non-blocking; coroutine context tiếp theo chọn dispatcher/thread nơi work thực sự chạy.

## 5. Suspend không làm blocking code thành non-blocking
Phần này nối mạch Android vừa học với “5. Suspend không làm blocking code thành non-blocking”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
suspend fun bad() {
    Thread.sleep(5_000)
}
```

Hàm (function / 함수) có từ khóa (keyword / 키워드) `suspend` nhưng vẫn khối (block / 블록) luồng thực thi (thread / 스레드) 5 giây. Blocking I/O/CPU công việc (work / 작업) vẫn cần dispatcher/executor phù hợp.

`suspend` mô tả khả năng suspension trong lời gọi (call / 호출) chuỗi (chain / 사슬), không tự quyết định luồng thực thi (thread / 스레드).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **6. Coroutine ngữ cảnh (context / 맥락) và luồng thực thi (thread / 스레드) cục bộ (local / 로컬)** nối từ **5. Suspend không làm blocking code thành non-blocking** sang **7. inline thực sự làm gì?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Coroutine ngữ cảnh (context / 맥락) và luồng thực thi (thread / 스레드) cục bộ (local / 로컬)

Coroutine có thể resume trên luồng thực thi (thread / 스레드) khác. mã (code / 코드) dựa raw `ThreadLocal` có thể sai nếu không cầu nối (bridge / 브리지) bằng `asContextElement` hoặc cơ chế (mechanism / 메커니즘) phù hợp.

Bảo mật (security / 보안)/yêu cầu (request / 요청) tracing ngữ cảnh (context / 맥락) nên được propagate có chủ ý. Đừng assume luồng thực thi (thread / 스레드) định danh (identity / 식별자) là coroutine định danh (identity / 식별자).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **7. inline thực sự làm gì?** nối từ **6. Coroutine ngữ cảnh (context / 맥락) và luồng thực thi (thread / 스레드) cục bộ (local / 로컬)** sang **8. Không inline mọi hàm (function / 함수)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. `inline` thực sự làm gì?

Higher-order hàm (function / 함수) tạo lambda đối tượng (object / 객체)/lời gọi (call / 호출) overhead trong một số trường hợp. `inline` cho phép trình biên dịch (compiler / 컴파일러) inline hàm (function / 함수) body/lambda ở lời gọi (call / 호출) site, đồng thời mở khả năng `reified` kiểu (type / 타입) parameter và non-local return.

```kotlin
inline fun <reified T> Json.decode(value: String): T = ...
```

`reified` hoạt động vì lời gọi (call / 호출) site biết concrete kiểu (type / 타입) khi inline. Generic hàm (function / 함수) bình thường chịu kiểu (type / 타입) erasure trên JVM.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **8. Không inline mọi hàm (function / 함수)** nối từ **7. inline thực sự làm gì?** sang **9. noinline và crossinline**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Không inline mọi hàm (function / 함수)

Inline làm bytecode ở lời gọi (call / 호출) site lớn hơn. công khai (public / 공개) inline hàm (function / 함수) còn có tính tương thích (compatibility / 호환성) implication vì hiện thực (implementation / 구현) được bản sao (copy / 복사) vào bên tiêu thụ (consumer / 소비자) khi compile.

Dùng inline chủ yếu cho HOF hot/idiomatic, reified yêu cầu (requirement / 요구사항) hoặc API thiết kế (design / 설계) rõ; không thêm `inline` như hiệu năng (performance / 성능) decoration.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **9. noinline và crossinline** nối từ **8. Không inline mọi hàm (function / 함수)** sang **10. Generic kiểu (type / 타입) erasure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. `noinline` và `crossinline`

Trong inline hàm (function / 함수), lambda parameter mặc định có thể inline.

`noinline` giữ lambda như đối tượng (object / 객체), cần khi lưu/truyền lambda như giá trị (value / 값).

`crossinline` ngăn non-local return khi lambda sẽ chạy ở ngữ cảnh (context / 맥락) không cho phép return khỏi caller.

```kotlin
inline fun execute(crossinline block: () -> Unit) {
    executor.execute { block() }
}
```

Nếu không hiểu non-local return, mã (code / 코드) inline callback có thể gây compile lỗi (error / 오류) khó hiểu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **10. Generic kiểu (type / 타입) erasure** nối từ **9. noinline và crossinline** sang **11. Variance ở nguồn (source / 소스) vs JVM wildcard**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Generic kiểu (type / 타입) erasure

Trên JVM:

```kotlin
fun <T> isListOf(value: Any): Boolean {
    // không thể runtime check đầy đủ List<T>
}
```

Thời gian chạy (runtime / 런타임) thường chỉ biết `List`, không biết element `T`. `reified` giúp một số check tại inline lời gọi (call / 호출) site nhưng nested generic vẫn có giới hạn.

Serialization/reflection khung phần mềm (framework / 프레임워크) cần kiểu (type / 타입) đơn vị từ (token / 토큰), generated serializer hoặc siêu dữ liệu (metadata / 메타데이터) để giữ kiểu (type / 타입) thông tin (information / 정보).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **10. Generic kiểu (type / 타입) erasure** đặt vấn đề; **11. Variance ở nguồn (source / 소스) vs JVM wildcard** đối chiếu bằng chứng, rồi **12. nền tảng (platform / 플랫폼) kiểu (type / 타입)** mở rộng hệ quả hoặc giới hạn liên quan.

## 11. Variance ở nguồn (source / 소스) vs JVM wildcard

Kotlin `out T`/`in T` biểu diễn variance ở hệ kiểu (type system / 타입 시스템). Khi expose API cho Java, wildcard signature có thể khác mong muốn.

`@JvmSuppressWildcards` và `@JvmWildcard` đôi lúc cần để điều chỉnh Java-facing signature, nhưng đừng dùng nếu không inspect API thực tế.

Thư viện (library / 라이브러리)/API công khai (public API / 공개 API) nên kiểm thử (test / 테스트) Java interoperability nếu bên tiêu thụ (consumer / 소비자) có Java.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **11. Variance ở nguồn (source / 소스) vs JVM wildcard** đặt vấn đề; **12. nền tảng (platform / 플랫폼) kiểu (type / 타입)** đối chiếu bằng chứng, rồi **13. lateinit thời gian chạy (runtime / 런타임) check** mở rộng hệ quả hoặc giới hạn liên quan.

## 12. nền tảng (platform / 플랫폼) kiểu (type / 타입)

Java API không annotate nullability có thể thành `String!` trong Kotlin. trình biên dịch (compiler / 컴파일러) cho phép xử lý như nullable hoặc non-null, nên NPE vẫn có thể xảy ra.

Ranh giới (boundary / 경계) Java legacy nên annotate nullability hoặc normalize giá trị (value / 값) ngay khi vào Kotlin tầng (layer / 계층).

```kotlin
val name: String = requireNotNull(javaApi.name) {
    "Legacy API returned null name"
}
```

Crash ở ranh giới (boundary / 경계) có message rõ hơn crash xa downstream.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **13. lateinit thời gian chạy (runtime / 런타임) check** nối từ **12. nền tảng (platform / 플랫폼) kiểu (type / 타입)** sang **14. lazy**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. `lateinit` thời gian chạy (runtime / 런타임) check

`lateinit var` bỏ nullable cú pháp (syntax / 문법) nhưng không bảo đảm thuộc tính (property / 속성) đã init. Read trước init ném `UninitializedPropertyAccessException`.

Dùng khi vòng đời (lifecycle / 생명주기)/khung phần mềm (framework / 프레임워크) thực sự init sau construction; không dùng để né constructor injection.

Trong Fragment View Binding, `lateinit`/nullable backing trường dữ liệu (field / 필드) phải theo View vòng đời (lifecycle / 생명주기), không Activity/Fragment đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **14. lazy** nối từ **13. lateinit thời gian chạy (runtime / 런타임) check** sang **15. dữ liệu (data / 데이터) lớp (class / 클래스) generation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. `lazy`

`lazy` mặc định có synchronization ngữ nghĩa (semantics / 의미론) phù hợp multi-thread. Có các chế độ (mode / 모드) khác (`SYNCHRONIZED`, `PUBLICATION`, `NONE`) với sự đánh đổi (trade-off / 트레이드오프).

Android main-thread-only đối tượng (object / 객체) có thể dùng chế độ (mode / 모드) phù hợp nếu chắc chắn truy cập (access / 접근) single-thread, nhưng tối ưu hóa (optimization / 최적화) này hiếm khi là bottleneck. Ưu tiên tính đúng đắn (correctness / 정확성).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **14. lazy** đặt vấn đề; **15. dữ liệu (data / 데이터) lớp (class / 클래스) generation** đối chiếu bằng chứng, rồi **16. object và singleton initialization** mở rộng hệ quả hoặc giới hạn liên quan.

## 15. dữ liệu (data / 데이터) lớp (class / 클래스) generation

Trình biên dịch (compiler / 컴파일러) generate `equals`, `hashCode`, `toString`, `componentN`, `copy` cho primary constructor properties.

`copy()` là shallow bản sao (copy / 복사):

```kotlin
data class State(val items: MutableList<String>)

val a = State(mutableListOf("A"))
val b = a.copy()
b.items += "B"
// a.items cũng thấy B vì cùng list reference
```

Immutable trạng thái (state / 상태) cần immutable nested giá trị (value / 값) hoặc defensive bản sao (copy / 복사).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **15. dữ liệu (data / 데이터) lớp (class / 클래스) generation** đặt vấn đề; **16. object và singleton initialization** đối chiếu bằng chứng, rồi **17. Companion đối tượng (object / 객체) và Java API** mở rộng hệ quả hoặc giới hạn liên quan.

## 16. `object` và singleton initialization

Kotlin `object` tạo singleton ngữ nghĩa (semantics / 의미론) theo thời gian chạy (runtime / 런타임)/classloader. Nó tiện cho stateless utility, nhưng toàn cục (global / 전역) mutable trạng thái (state / 상태) trong đối tượng (object / 객체) gây hidden phụ thuộc (dependency / 의존성)/kiểm thử (test / 테스트) contamination.

Android tiến trình (process / 프로세스) death reset singleton bộ nhớ (memory / 메모리). Đừng dùng đối tượng (object / 객체) làm persistence/session nguồn chuẩn (source of truth / 정본) nếu trạng thái (state / 상태) cần restore.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **17. Companion đối tượng (object / 객체) và Java API** nối từ **16. object và singleton initialization** sang **18. Top-level hàm (function / 함수)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Companion đối tượng (object / 객체) và Java API

Companion member không phải static JVM phương thức (method / 메서드) theo đúng nghĩa mặc định. `@JvmStatic` có thể generate static cầu nối (bridge / 브리지) cho Java-friendly API.

```kotlin
class Parser {
    companion object {
        @JvmStatic
        fun create(): Parser = Parser()
    }
}
```

Chỉ dùng khi Java interop/API yêu cầu.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **18. Top-level hàm (function / 함수)** nối từ **17. Companion đối tượng (object / 객체) và Java API** sang **19. Extension hàm (function / 함수) là static dispatch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Top-level hàm (function / 함수)

Top-level Kotlin hàm (function / 함수) compile thành static phương thức (method / 메서드) trong generated tệp (file / 파일) lớp (class / 클래스) trên JVM. `@file:JvmName` có thể điều khiển (control / 제어) Java-visible lớp (class / 클래스) name.

Đây là lý do top-level pure utility hoàn toàn idiomatic; không cần tạo `Utils` đối tượng (object / 객체) chỉ để chứa static-like hàm (function / 함수).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **19. Extension hàm (function / 함수) là static dispatch** nối từ **18. Top-level hàm (function / 함수)** sang **20. Sequence vs Collection**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Extension hàm (function / 함수) là static dispatch

Extension không thực sự thêm virtual phương thức (method / 메서드) vào lớp (class / 클래스).

```kotlin
fun Animal.sound() = "animal"
fun Dog.sound() = "dog"
```

Extension được resolve theo compile-time receiver kiểu (type / 타입), không polymorphic virtual dispatch. Nếu hành vi (behavior / 동작) cần override, dùng member/giao diện (interface / 인터페이스).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **20. Sequence vs Collection** nối từ **19. Extension hàm (function / 함수) là static dispatch** sang **21. Boxing thành phần nguyên thủy (primitive / 기본 요소)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Sequence vs Collection
Phần này nối mạch Android vừa học với “20. Sequence vs Collection”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
items.map(...).filter(...).take(10)
```

Collection chuỗi (chain / 사슬) có thể tạo intermediate collection. `asSequence()` xử lý lazy element-by-element và hữu ích khi chuỗi (chain / 사슬) dài/dữ liệu (data / 데이터) lớn/early termination.

Nhưng chuỗi (sequence / 시퀀스) có iterator/lambda overhead và không luôn nhanh hơn cho danh sách (list / 목록) nhỏ. Benchmark đường xử lý nóng (hot path / 핫 패스) thay vì cargo-cult `asSequence()`.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **21. Boxing thành phần nguyên thủy (primitive / 기본 요소)** nối từ **20. Sequence vs Collection** sang **22. Value class và boxing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Boxing thành phần nguyên thủy (primitive / 기본 요소)

Kotlin `Int` thường map JVM thành phần nguyên thủy (primitive / 기본 요소) `int` khi có thể, nhưng generic/nullable có thể box thành `Integer`.

```kotlin
val a: Int = 1       // có thể primitive
val b: Int? = 1      // boxed
val list: List<Int>  // elements boxed trên JVM
```

Trong UI/nghiệp vụ (business / 비즈니스) mã (code / 코드) bình thường không đáng lo. Trong vòng lặp (loop / 루프) cực nóng/large numeric dữ liệu (data / 데이터), allocation/boxing có thể hiện trên profiler.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **22. Value class và boxing** nối từ **21. Boxing thành phần nguyên thủy (primitive / 기본 요소)** sang **23. Lambda capture**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Value class và boxing
Phần này nối mạch Android vừa học với “22. Value class và boxing”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
@JvmInline
value class UserId(val value: String)
```

Giá trị (value / 값) lớp (class / 클래스) thường tránh allocation wrapper trong nhiều ngữ cảnh (context / 맥락), nhưng có thể box khi nullable, generic, giao diện (interface / 인터페이스)/polymorphic ranh giới (boundary / 경계) hoặc thời gian chạy (runtime / 런타임) cần đối tượng (object / 객체).

Đừng hứa “zero allocation”. Dùng giá trị (value / 값) lớp (class / 클래스) trước hết cho kiểu (type / 타입) an toàn (safety / 안전)/lĩnh vực (domain / 도메인) modeling; hiệu năng (performance / 성능) là secondary và cần đo.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **23. Lambda capture** nối từ **22. Value class và boxing** sang **24. Anonymous đối tượng (object / 객체) và inner lớp (class / 클래스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Lambda capture
Phần này nối mạch Android vừa học với “23. Lambda capture”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
fun screen(activity: Activity): () -> Unit = {
    activity.finish()
}
```

Lambda capture giữ tham chiếu (reference / 참조) `activity`. Nếu lambda được singleton/store lâu hơn Activity, leak.

Coroutine/callback leak investigation nên inspect capture chuỗi (chain / 사슬), không chỉ lớp (class / 클래스) trường dữ liệu (field / 필드) rõ ràng.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **24. Anonymous đối tượng (object / 객체) và inner lớp (class / 클래스)** nối từ **23. Lambda capture** sang **25. Annotation use-site mục tiêu (target / 대상)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Anonymous đối tượng (object / 객체) và inner lớp (class / 클래스)

`inner class` giữ tham chiếu (reference / 참조) tới outer instance. Nested lớp (class / 클래스) không giữ implicit outer tham chiếu (reference / 참조).

Listener anonymous đối tượng (object / 객체) có thể capture outer Activity/Fragment. Registration thời gian tồn tại (lifetime / 수명) sai dễ leak.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **25. Annotation use-site mục tiêu (target / 대상)** nối từ **24. Anonymous đối tượng (object / 객체) và inner lớp (class / 클래스)** sang **26. Reflection vs generated mã (code / 코드)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Annotation use-site mục tiêu (target / 대상)

Kotlin thuộc tính (property / 속성) có thể tương ứng trường dữ liệu (field / 필드)/getter/setter/constructor parameter. Annotation khung phần mềm (framework / 프레임워크) đôi khi cần mục tiêu (target / 대상) cụ thể:

```kotlin
@get:JsonIgnore
val internalValue: String

@field:Inject
lateinit var dependency: Dependency
```

Nếu annotation “không có tác dụng”, inspect khung phần mềm (framework / 프레임워크) đọc trường dữ liệu (field / 필드), getter hay parameter nào.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **26. Reflection vs generated mã (code / 코드)** nối từ **25. Annotation use-site mục tiêu (target / 대상)** sang **27. KAPT**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Reflection vs generated mã (code / 코드)

Reflection linh hoạt nhưng có thời gian chạy (runtime / 런타임) chi phí (cost / 비용) và R8/siêu dữ liệu (metadata / 메타데이터) độ phức tạp (complexity / 복잡도). Generated mã (code / 코드) chuyển nhiều lỗi sang compile thời gian (time / 시간) và shrink-friendly hơn trong nhiều khung phần mềm (framework / 프레임워크).

Room, hiện đại (modern / 현대적) DI/codegen, Kotlin serialization thường tận dụng generated/compiled kiến thức (knowledge / 지식) thay vì reflection thuần.

Không vì thế reflection luôn xấu; chỉ cần biết thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약) và keep yêu cầu (requirement / 요구사항).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **27. KAPT** nối từ **26. Reflection vs generated mã (code / 코드)** sang **28. KSP**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. KAPT

KAPT cầu nối (bridge / 브리지) Java annotation processing vào Kotlin bằng stub generation. Nó từng là nền tảng của nhiều thư viện (library / 라이브러리) nhưng có bản dựng (build / 빌드) chi phí (cost / 비용) đáng kể.

Di chuyển (migration / 마이그레이션) khỏi KAPT chỉ nên làm khi processor/thư viện (library / 라이브러리) hỗ trợ alternative ổn định. Một dự án (project / 프로젝트) có thể coexist KAPT và KSP trong giai đoạn di chuyển (migration / 마이그레이션).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **28. KSP** nối từ **27. KAPT** sang **29. trình biên dịch (compiler / 컴파일러) plugin**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. KSP

KSP (Kotlin Symbol Processing) cung cấp symbol mô hình (model / 모델) gần Kotlin hơn và thường hiệu quả hơn KAPT cho processor hỗ trợ.

KSP processor tạo nguồn (source / 소스)/tài nguyên (resource / 자원) trong bản dựng (build / 빌드). Generated đầu ra (output / 출력) phải là deterministic hàm (function / 함수) của nguồn (source / 소스)/cấu hình (config / 설정) nếu muốn bộ nhớ đệm (cache / 캐시)/reproducible bản dựng (build / 빌드) tốt.

KSP phiên bản (version / 버전) phải tương thích Kotlin trình biên dịch (compiler / 컴파일러) line phù hợp; upgrade Kotlin cần kiểm tra processor ecosystem.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **29. trình biên dịch (compiler / 컴파일러) plugin** nối từ **28. KSP** sang **30. Compose trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. trình biên dịch (compiler / 컴파일러) plugin

Serialization và Compose có trình biên dịch (compiler / 컴파일러) tích hợp (integration / 통합). trình biên dịch (compiler / 컴파일러) plugin có quyền transform/augment compilation mạnh hơn annotation processor.

Do đó plugin phiên bản (version / 버전) mismatch có thể gây compile/thời gian chạy (runtime / 런타임) issue sâu. Toolchain ma trận (matrix / 행렬) cần được rà soát (review / 검토) như một đơn vị (unit / 단위).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **30. Compose trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **29. trình biên dịch (compiler / 컴파일러) plugin** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **31. Stability không đồng nghĩa val** mở rộng hệ quả hoặc giới hạn liên quan.

## 30. Compose trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) mô hình tư duy (mental model / 사고 모델)

Composable hàm (function / 함수) không phải ordinary hàm (function / 함수) đơn giản. trình biên dịch (compiler / 컴파일러) thêm machinery để thời gian chạy (runtime / 런타임) theo dõi composition group, parameter/trạng thái (state / 상태) read và skipping/recomposition.

Bạn không cần đọc generated bytecode hằng ngày, nhưng khi optimize cần hiểu:

- trạng thái (state / 상태) read quyết định vô hiệu hóa (invalidation / 무효화) phạm vi (scope / 범위);
- stable/immutable đầu vào (input / 입력) giúp skipping trong ngữ cảnh (context / 맥락) phù hợp;
- key/định danh (identity / 식별자) ảnh hưởng trạng thái (state / 상태) association;
- composition, bố cục (layout / 레이아웃), draw là phase khác nhau.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **31. Stability không đồng nghĩa val** tổng hợp từ **30. Compose trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **32. @Immutable/@Stable không phải hiệu năng (performance / 성능) magic** mở rộng hệ quả hoặc giới hạn liên quan.

## 31. Stability không đồng nghĩa `val`

Một lớp (class / 클래스) có toàn `val` nhưng chứa mutable danh sách (list / 목록) vẫn có mutation hidden.

```kotlin
data class UiModel(
    val items: MutableList<Item>
)
```

Compose/trạng thái (state / 상태) lập luận (reasoning / 추론) cần ngữ nghĩa (semantic / 의미적) immutability, không chỉ cú pháp (syntax / 문법) `val`.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **32. @Immutable/@Stable không phải hiệu năng (performance / 성능) magic** nối từ **31. Stability không đồng nghĩa val** sang **33. Bytecode inspection**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. `@Immutable`/`@Stable` không phải hiệu năng (performance / 성능) magic

Annotation stability là đặc tả hợp đồng (contract / 계약) bạn hứa với Compose thời gian chạy (runtime / 런타임)/trình biên dịch (compiler / 컴파일러). Annotate sai có thể khiến UI không cập nhật (update / 업데이트) đúng hoặc làm lập luận (reasoning / 추론) sai.

Chỉ annotate khi kiểu (type / 타입) thực sự thỏa đặc tả hợp đồng (contract / 계약); đừng dùng để silence hiệu năng (performance / 성능) warning mà không hiểu mutation ngữ nghĩa (semantics / 의미론).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **33. Bytecode inspection** nối từ **32. @Immutable/@Stable không phải hiệu năng (performance / 성능) magic** sang **34. Default argument và Java**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Bytecode inspection

Android Studio/Kotlin tooling có thể decompile bytecode để hiểu:

- thuộc tính (property / 속성) getter/setter;
- default argument synthetic phương thức (method / 메서드);
- suspend máy trạng thái (state machine / 상태 머신);
- inline kết quả (result / 결과);
- companion/static cầu nối (bridge / 브리지);
- boxing.

Khi interop/hiệu năng (performance / 성능) bug khó, inspect generated biểu diễn (representation / 표현) thường nhanh hơn đoán.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **34. Default argument và Java** nối từ **33. Bytecode inspection** sang **35. Checked exception**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Default argument và Java

Kotlin default parameter thuận tiện nhưng Java caller không tự thấy overload tương đương. `@JvmOverloads` generate overload trong trường hợp (case / 사례) phù hợp.

```kotlin
class Client @JvmOverloads constructor(
    val timeout: Long = 5_000,
    val retries: Int = 2
)
```

Không generate hàng loạt overload nếu API Java không cần.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **35. Checked exception** nối từ **34. Default argument và Java** sang **36. Nothing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Checked exception

Kotlin không enforce checked exception. Nếu Kotlin API được Java gọi và cần khai báo throws, `@Throws` giúp generate signature.

```kotlin
@Throws(IOException::class)
fun read(): Data = ...
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **36. Nothing** nối từ **35. Checked exception** sang **37. Unit vs Java void**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. `Nothing`

`Nothing` là kiểu (type / 타입) không có giá trị (value / 값), dùng cho hàm (function / 함수) không return bình thường:

```kotlin
fun fail(message: String): Nothing = error(message)
```

Nó giúp kiểu (type / 타입) suy luận (inference / 추론) hiểu branch throw không cần produce giá trị (value / 값).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **37. Unit vs Java void** nối từ **36. Nothing** sang **38. Equality và generated equals**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. `Unit` vs Java `void`

`Unit` là kiểu (type / 타입) có single giá trị (value / 값) `Unit`; Java `void` là absence return. Interop/trình biên dịch (compiler / 컴파일러) có ánh xạ (mapping / 매핑) riêng. Higher-order hàm (function / 함수) `() -> Unit` là đối tượng (object / 객체)/hàm (function / 함수) kiểu (type / 타입) nhận kết quả (result / 결과) đơn vị (unit / 단위), khác khái niệm một phương thức (method / 메서드) void đơn thuần.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **38. Equality và generated equals** nối từ **37. Unit vs Java void** sang **39. Hash-based collection bất biến (invariant / 불변식)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Equality và generated `equals`

`==` gọi structural equality (`equals`), `===` kiểm tra tham chiếu (reference / 참조) định danh (identity / 식별자).

Dữ liệu (data / 데이터) lớp (class / 클래스) generated equals dùng primary constructor thuộc tính (property / 속성) equality. Với array, `Array.equals` ngữ nghĩa (semantics / 의미론) khác content equality kỳ vọng; dùng `contentEquals`/`contentDeepEquals` khi cần.

Lĩnh vực (domain / 도메인) kiểu (type / 타입) chứa array cần custom equality nếu content ngữ nghĩa (semantics / 의미론) quan trọng.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **39. Hash-based collection bất biến (invariant / 불변식)** nối từ **38. Equality và generated equals** sang **40. JVM bộ nhớ (memory / 메모리) mô hình (model / 모델) và luồng thực thi (thread / 스레드) an toàn (safety / 안전)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. Hash-based collection bất biến (invariant / 불변식)

Nếu đối tượng (object / 객체) dùng key trong HashMap/HashSet, fields tham gia `equals/hashCode` không nên mutate theo cách làm băm (hash / 해시) thay đổi khi đối tượng (object / 객체) đang trong set/map.

Immutable dữ liệu (data / 데이터) lớp (class / 클래스) key an toàn hơn mutable thực thể (entity / 엔터티) đối tượng (object / 객체).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **40. JVM bộ nhớ (memory / 메모리) mô hình (model / 모델) và luồng thực thi (thread / 스레드) an toàn (safety / 안전)** nối từ **39. Hash-based collection bất biến (invariant / 불변식)** sang **41. volatile, atomic và Mutex**, vì cơ chế trước tạo đầu vào cho bước sau.

## 40. JVM bộ nhớ (memory / 메모리) mô hình (model / 모델) và luồng thực thi (thread / 스레드) an toàn (safety / 안전)

`val` chỉ ngăn reassignment tham chiếu (reference / 참조), không tự làm đối tượng (object / 객체) thread-safe. MutableList trong val vẫn mutable.

Dùng chung (shared / 공유) mutable trạng thái (state / 상태) giữa coroutine trên nhiều dispatcher cần confinement, Mutex, atomic thành phần nguyên thủy (primitive / 기본 요소) hoặc immutable chuyển tiếp trạng thái (state transition / 상태 전이) phù hợp.

Coroutine không loại bỏ dữ liệu (data / 데이터) race nếu mã (code / 코드) chạy concurrent thật.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **41. volatile, atomic và Mutex** nối từ **40. JVM bộ nhớ (memory / 메모리) mô hình (model / 모델) và luồng thực thi (thread / 스레드) an toàn (safety / 안전)** sang **42. Exception và cancellation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. `volatile`, atomic và Mutex

`@Volatile` giúp visibility của một trường dữ liệu (field / 필드), không biến multi-step thao tác (operation / 연산) thành atomic.

```kotlin
@Volatile var count = 0
count++ // read-modify-write, không atomic
```

Dùng AtomicInteger/atomic thành phần nguyên thủy (primitive / 기본 요소) cho thao tác (operation / 연산) đơn giản; Mutex cho trọng yếu (critical / 중요) section suspending; single-thread confinement/trạng thái (state / 상태) reducer khi phù hợp.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **42. Exception và cancellation** nối từ **41. volatile, atomic và Mutex** sang **43. kết quả (result / 결과) và exception API thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. Exception và cancellation

`CancellationException` là điều khiển (control / 제어) tín hiệu (signal / 신호) của coroutine. Broad catch:

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

Hoặc cấu trúc (structure / 구조) catch cụ thể hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **43. kết quả (result / 결과) và exception API thiết kế (design / 설계)** nối từ **42. Exception và cancellation** sang **44. nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 43. kết quả (result / 결과) và exception API thiết kế (design / 설계)

Kotlin `Result<T>` hữu ích ở một số ranh giới (boundary / 경계) nhưng không phải universal lĩnh vực (domain / 도메인) lỗi (error / 오류) mô hình (model / 모델). lĩnh vực (domain / 도메인) có nhiều lỗi (error / 오류) typed rõ ràng có thể dùng sealed kết quả (result / 결과).

Công khai (public / 공개) Java-facing API với Kotlin kết quả (result / 결과) cần cân nhắc interop. API thiết kế (design / 설계) phải xét bên tiêu thụ (consumer / 소비자).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **44. nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)** nối từ **43. kết quả (result / 결과) và exception API thiết kế (design / 설계)** sang **45. công khai (public / 공개) inline API tính tương thích (compatibility / 호환성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 44. nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)

Thư viện (library / 라이브러리)/mô-đun (module / 모듈) API đổi source-compatible chưa chắc binary-compatible với bên tiêu thụ (consumer / 소비자) đã compile trước.

Thay phương thức (method / 메서드) signature, remove lớp (class / 클래스), đổi JVM name hoặc inline/công khai (public / 공개) ABI có thể gây `NoSuchMethodError`/`NoClassDefFoundError` nếu sản phẩm tạo ra (artifact / 산출물) mix phiên bản (version / 버전).

Nội bộ (internal / 내부) app monorepo thường rebuild cùng lúc nên rủi ro (risk / 위험) thấp hơn published thư viện (library / 라이브러리)/động (dynamic / 동적) mô-đun (module / 모듈) ecosystem.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **45. công khai (public / 공개) inline API tính tương thích (compatibility / 호환성)** nối từ **44. nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)** sang **46. R8 shrinking**, vì cơ chế trước tạo đầu vào cho bước sau.

## 45. công khai (public / 공개) inline API tính tương thích (compatibility / 호환성)

Bên tiêu thụ (consumer / 소비자) compile body inline vào bytecode của họ. Vì vậy hành vi (behavior / 동작) cũ có thể nằm trong bên tiêu thụ (consumer / 소비자) cho tới khi recompile, và nội bộ (internal / 내부) symbol referenced bởi công khai (public / 공개) inline cần visibility rules (`@PublishedApi` khi phù hợp).

Thư viện (library / 라이브러리) author cần hiểu điều này trước khi expose nhiều inline hiện thực (implementation / 구현) detail.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **46. R8 shrinking** nối từ **45. công khai (public / 공개) inline API tính tương thích (compatibility / 호환성)** sang **47. ánh xạ (mapping / 매핑) và crash**, vì cơ chế trước tạo đầu vào cho bước sau.

## 46. R8 shrinking

R8 phân tích reachability và có thể remove/rename/optimize mã (code / 코드). Reflection/JNI/resource-by-name làm static phân tích (analysis / 분석) khó.

Keep quy tắc (rule / 규칙) nên là minimum đặc tả hợp đồng (contract / 계약):

```text
keep exactly reflected members
keep required annotation/metadata
consumer rule đi cùng library
```

Không disable shrink để tránh gỡ lỗi (debug / 디버그) một issue.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **47. ánh xạ (mapping / 매핑) và crash** nối từ **46. R8 shrinking** sang **48. D8/desugaring**, vì cơ chế trước tạo đầu vào cho bước sau.

## 47. ánh xạ (mapping / 매핑) và crash

Obfuscated dấu vết ngăn xếp (stack trace / 스택 트레이스) môi trường vận hành (production / 운영 환경) cần ánh xạ (mapping / 매핑) tệp (file / 파일) đúng bản dựng (build / 빌드). ánh xạ (mapping / 매핑) là sản phẩm tạo ra (artifact / 산출물) của bản phát hành (release / 릴리스), không được overwrite/mất.

Bản dựng (build / 빌드) ID/versionCode phải liên kết ánh xạ (mapping / 매핑) để symbolicate sự cố (incident / 인시던트) sau nhiều tháng.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **48. D8/desugaring** nối từ **47. ánh xạ (mapping / 매핑) và crash** sang **49. API mức (level / 수준) check vẫn cần**, vì cơ chế trước tạo đầu vào cho bước sau.

## 48. D8/desugaring

Android thiết bị (device / 장치) API cũ không có mọi Java ngôn ngữ (language / 언어)/thư viện (library / 라이브러리) tính năng (feature / 기능) mới. Desugaring transform một số bytecode/API để hỗ trợ mục tiêu (target / 대상) thấp hơn.

Khi dùng Java thời gian (time / 시간)/API mới trên minSdk cũ, cốt lõi (core / 핵심) thư viện (library / 라이브러리) desugaring có thể liên quan. Đừng assume compileSdk cao nghĩa mọi thời gian chạy (runtime / 런타임) thiết bị (device / 장치) có API đó bản địa (native / 네이티브).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **49. API mức (level / 수준) check vẫn cần** nối từ **48. D8/desugaring** sang **50. phương thức (method / 메서드) count và phụ thuộc (dependency / 의존성) chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 49. API mức (level / 수준) check vẫn cần

Compile-time symbol availability khác thời gian chạy (runtime / 런타임) availability.

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.X) {
    // API mới
}
```

AndroidX tính tương thích (compatibility / 호환성) wrapper thường nên được ưu tiên khi nó abstract hành vi (behavior / 동작) chính xác.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **50. phương thức (method / 메서드) count và phụ thuộc (dependency / 의존성) chi phí (cost / 비용)** nối từ **49. API mức (level / 수준) check vẫn cần** sang **51. Allocation profiler và vùng nhớ động (heap / 힙)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 50. phương thức (method / 메서드) count và phụ thuộc (dependency / 의존성) chi phí (cost / 비용)

MultiDex ít còn là daily issue như thời cũ ở nhiều dự án (project / 프로젝트) hiện đại, nhưng phụ thuộc (dependency / 의존성) vẫn có chi phí (cost / 비용): phương thức (method / 메서드)/mã (code / 코드) kích thước (size / 크기), startup initializer, transitive phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) và bảo mật (security / 보안) surface.

Rà soát (review / 검토) phụ thuộc (dependency / 의존성) không chỉ theo “thêm một dòng Gradle”.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **51. Allocation profiler và vùng nhớ động (heap / 힙)** nối từ **50. phương thức (method / 메서드) count và phụ thuộc (dependency / 의존성) chi phí (cost / 비용)** sang **52. Benchmark JVM vs Android**, vì cơ chế trước tạo đầu vào cho bước sau.

## 51. Allocation profiler và vùng nhớ động (heap / 힙)

Nếu profiler thấy allocation spike, dấu vết (trace / 추적) nguồn (source / 소스) trước. Có thể là JSON parsing, bitmap, danh sách (list / 목록) transform, string format, lambda capture hoặc recomposition đối tượng (object / 객체) creation.

Đừng rewrite idiomatic Kotlin sang imperative mã (code / 코드) chỉ dựa trên giả định “functional chậm”. Measure representative tải công việc (workload / 워크로드).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **52. Benchmark JVM vs Android** nối từ **51. Allocation profiler và vùng nhớ động (heap / 힙)** sang **53. bản dựng (build / 빌드) scan/profile**, vì cơ chế trước tạo đầu vào cho bước sau.

## 52. Benchmark JVM vs Android

Microbenchmark trên desktop JVM không phản ánh ART/thiết bị (device / 장치) hoàn toàn. AndroidX Benchmark chạy môi trường Android phù hợp hơn cho hot mã (code / 코드) cần đo.

Macrobenchmark dùng cho người dùng (user / 사용자) journey; Microbenchmark cho hàm (function / 함수)/thành phần (component / 컴포넌트) đường xử lý nóng (hot path / 핫 패스).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **53. bản dựng (build / 빌드) scan/profile** nối từ **52. Benchmark JVM vs Android** sang **54. Generated nguồn (source / 소스) quyền sở hữu (ownership / 소유권)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 53. bản dựng (build / 빌드) scan/profile

Slow Gradle bản dựng (build / 빌드) cần profile cấu hình (configuration / 구성) vs tác vụ (task / 작업) thực thi (execution / 실행), annotation processing/mã (code / 코드) generation, non-cacheable tác vụ (task / 작업), phụ thuộc (dependency / 의존성) resolution.

Không giải slow bản dựng (build / 빌드) chỉ bằng tăng vùng nhớ động (heap / 힙). nguyên nhân gốc (root cause / 근본 원인) có thể là mô-đun (module / 모듈) đồ thị (graph / 그래프), KAPT processor hoặc tác vụ (task / 작업) luôn out-of-date.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **53. bản dựng (build / 빌드) scan/profile** đặt vấn đề; **54. Generated nguồn (source / 소스) quyền sở hữu (ownership / 소유권)** đối chiếu bằng chứng, rồi **55. cấp cao (senior / 시니어) debugging workflow** mở rộng hệ quả hoặc giới hạn liên quan.

## 54. Generated nguồn (source / 소스) quyền sở hữu (ownership / 소유권)

Không edit generated nguồn (source / 소스) bằng tay. Fix đầu vào (input / 입력)/processor/template.

Generated folder thường không lần ghi nhận (commit / 커밋) trừ công cụ (tool / 도구) explicitly yêu cầu; CI phải tạo lại được. Nếu generated sản phẩm tạo ra (artifact / 산출물) cần rà soát (review / 검토)/API tracking, thiết kế workflow rõ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **54. Generated nguồn (source / 소스) quyền sở hữu (ownership / 소유권)** đặt vấn đề; **55. cấp cao (senior / 시니어) debugging workflow** đối chiếu bằng chứng, rồi **56. Master takeaway** mở rộng hệ quả hoặc giới hạn liên quan.

## 55. cấp cao (senior / 시니어) debugging workflow

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

Đừng nhảy thẳng vào decompile nếu tầng mã nguồn (source-level / 소스 수준) bug đã đủ giải thích.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 08 — Kotlin/JVM, K2 trình biên dịch (compiler / 컴파일러), Generated mã (code / 코드) và thời gian chạy (runtime / 런타임) Internals**, **55. cấp cao (senior / 시니어) debugging workflow** xác định đầu vào; **56. Master takeaway** giải thích bước vận hành tạo ra kết quả kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 56. Master takeaway

Kotlin lớp trừu tượng (abstraction / 추상화) tốt cho productivity, nhưng cấp cao (senior / 시니어)/master cần biết lớp trừu tượng (abstraction / 추상화) được thực hiện thế nào ở những điểm ảnh hưởng tính đúng đắn (correctness / 정확성), hiệu năng (performance / 성능) và tính tương thích (compatibility / 호환성).

Hãy nhớ các leak điểm (point / 지점) chính: **kiểu (type / 타입) erasure, boxing, generated mã (code / 코드), coroutine máy trạng thái (state machine / 상태 머신), capture/thời gian tồn tại (lifetime / 수명), annotation mục tiêu (target / 대상), Java interop, trình biên dịch (compiler / 컴파일러)/plugin tính tương thích (compatibility / 호환성), reflection/R8 và nhị phân (binary / 이진) ABI**.

Bạn không cần tối ưu theo bytecode mỗi ngày. Bạn cần khả năng hạ xuống tầng bytecode/thời gian chạy (runtime / 런타임) khi bằng chứng (evidence / 증거) cho thấy vấn đề nằm ở đó, rồi quay lại thiết kế tầng mã nguồn (source-level / 소스 수준) đơn giản nhất có thể.

> **Bàn giao:** Sau **56. Master takeaway**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
