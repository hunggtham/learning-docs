# Kotlin + Android Master ghi chú (note / 노트) — Beginner

> **Mạch đọc:** Đặt **Kotlin + Android Master ghi chú (note / 노트) — Beginner** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Mục lục** sang **1.1 Kotlin/JVM, Kotlin Multiplatform và Kotlin/bản địa (native / 네이티브)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> Mục tiêu: học từ gần như số 0 để có thể đọc, viết và chạy một ứng dụng Android cơ bản bằng Kotlin. Tài liệu ưu tiên Kotlin hiện đại và Jetpack Compose, đồng thời vẫn giải thích XML/View hệ thống (system / 시스템) để bạn hiểu mã (code / 코드) Android cũ.
>
> Baseline phiên bản khi biên soạn: Kotlin 2.4.x; Android Studio Quail 4 / 2026.1.4 Patch 1 stable. Khi gặp API theo thế hệ khác nhau, tài liệu dùng bốn nhãn: `Modern preferred` cho hướng ưu tiên khi viết mã (code / 코드) mới; `Supported legacy/coexistence` cho API cũ hơn nhưng vẫn hợp lệ và phổ biến trong môi trường vận hành (production / 운영 환경); `Deprecated` cho API đã có hướng rời bỏ chính thức; `Historical` cho API chủ yếu cần biết để đọc dự án (project / 프로젝트) rất cũ. **Cũ không đồng nghĩa sai** và **mới không tự động tốt hơn trong mọi codebase**.

## Mục lục

1. Kotlin là gì và Kotlin nằm ở đâu trong Android
2. Cài Android Studio và tạo dự án (project / 프로젝트) Android đầu tiên
3. Cấu trúc dự án (project / 프로젝트) Gradle
4. Cú pháp Kotlin nền tảng
5. Kiểu dữ liệu, null-safety và kiểu (type / 타입) suy luận (inference / 추론)
6. Toán tử và biểu thức
7. Điều khiển luồng: if, when, vòng lặp (loop / 루프)
8. hàm (function / 함수)
9. lớp (class / 클래스) và đối tượng (object / 객체)
10. Constructor, thuộc tính (property / 속성), getter/setter
11. Inheritance, giao diện (interface / 인터페이스) và abstract lớp (class / 클래스)
12. dữ liệu (data / 데이터) lớp (class / 클래스), enum lớp (class / 클래스), sealed lớp (class / 클래스) nhập môn
13. Collection cơ bản
14. Lambda và higher-order hàm (function / 함수) nhập môn
15. Exception và kết quả (result / 결과) nhập môn
16. Android thành phần (component / 컴포넌트) căn bản
17. Jetpack Compose căn bản
18. XML/View hệ thống (system / 시스템) căn bản
19. trạng thái (state / 상태), sự kiện (event / 이벤트) và vòng đời (lifecycle / 생명주기) nhập môn
20. điều hướng (navigation / 내비게이션) nhập môn
21. tài nguyên (resource / 자원), manifest và permission
22. gỡ lỗi (debug / 디버그), Logcat và lỗi thường gặp
23. Mini dự án (project / 프로젝트) tổng hợp
24. Checklist Beginner

---

# 1. Kotlin là gì và Kotlin nằm ở đâu trong Android

Kotlin là ngôn ngữ lập trình hiện đại do JetBrains phát triển. Trên Android, Kotlin không phải là “Android khung phần mềm (framework / 프레임워크)” mà là ngôn ngữ dùng để viết mã chạy trên Android thời gian chạy (runtime / 런타임) thông qua toolchain của Android. Điều này cần được phân biệt rõ: Kotlin cung cấp cú pháp (syntax / 문법), hệ kiểu (type system / 타입 시스템), hàm (function / 함수), coroutine, collection và nhiều lớp trừu tượng (abstraction / 추상화) ở cấp ngôn ngữ; Android SDK cung cấp Activity, dịch vụ (service / 서비스), ngữ cảnh (context / 맥락), Intent, View, vòng đời (lifecycle / 생명주기) và các API thiết bị; Jetpack cung cấp những thư viện cấp cao như ViewModel, Room, điều hướng (navigation / 내비게이션), WorkManager, Compose.

Một ứng dụng Android Kotlin hiện đại thường có ba lớp công nghệ đan xen: Kotlin ngôn ngữ (language / 언어) ở lớp cú pháp và lô-gic (logic / 논리); Android/Jetpack ở lớp khung phần mềm (framework / 프레임워크); Gradle/Android Gradle Plugin ở lớp bản dựng (build / 빌드). Khi gặp lỗi, xác định lỗi thuộc lớp nào sẽ giúp gỡ lỗi (debug / 디버그) nhanh hơn. Ví dụ `NullPointerException` có thể liên quan lô-gic (logic / 논리) Kotlin hoặc Java interop; `ActivityNotFoundException` thuộc Android khung phần mềm (framework / 프레임워크); `Unresolved reference` thường thuộc trình biên dịch (compiler / 컴파일러)/phụ thuộc (dependency / 의존성)/bản dựng (build / 빌드) cấu hình (configuration / 구성).

Kotlin tương thích rất tốt với Java. Một dự án (project / 프로젝트) Android có thể có tệp (file / 파일) `.kt` và `.java` cùng lúc. Kotlin gọi Java API trực tiếp, và Java cũng có thể gọi Kotlin nếu signature phù hợp. Điều này đặc biệt quan trọng vì phần lớn Android khung phần mềm (framework / 프레임워크) ban đầu được viết bằng Java và nhiều codebase enterprise vẫn còn Java.

## 1.1 Kotlin/JVM, Kotlin Multiplatform và Kotlin/bản địa (native / 네이티브)

Trong Android truyền thống, mã Kotlin chủ yếu biên dịch cho JVM bytecode rồi được Android bản dựng (build / 빌드) công cụ (tool / 도구) chuyển thành DEX để ART chạy. Ngoài Kotlin/JVM, Kotlin còn có Kotlin/JS, Kotlin/bản địa (native / 네이티브), Kotlin/Wasm và Kotlin Multiplatform. Tuy nhiên khi mới học Android, không nên trộn KMP vào quá sớm. Hãy nắm chắc Kotlin/JVM + Android trước; KMP phù hợp hơn khi đã hiểu mô-đun (module / 모듈), phụ thuộc (dependency / 의존성), coroutine, serialization và nền tảng (platform / 플랫폼) ranh giới (boundary / 경계).

# 2. Cài Android Studio và tạo dự án (project / 프로젝트) đầu tiên

Android Studio là IDE chính thức của Android. Bản stable hiện tại trong baseline này là Android Studio Quail 4 (2026.1.4 Patch 1). Một bản Android Studio bao gồm editor dựa trên IntelliJ nền tảng (platform / 플랫폼), Gradle tích hợp (integration / 통합), Android SDK Manager, thiết bị (device / 장치) Manager, emulator, profiler, bố cục (layout / 레이아웃) Inspector, Logcat, debugger và Compose tooling.

Sau khi cài Android Studio, mở `SDK Manager` để kiểm tra Android SDK nền tảng (platform / 플랫폼) và bản dựng (build / 빌드) Tools. Trong `Device Manager`, có thể tạo Android Virtual thiết bị (device / 장치). Emulator phù hợp cho phần lớn việc học; thiết bị thật cần bật `Developer options` và `USB debugging`.

Khi tạo dự án (project / 프로젝트) mới, template `Empty Activity` hiện đại thường dùng Jetpack Compose. gói (package / 패키지) name nên theo reverse-domain convention như `com.example.myapp`. `Minimum SDK` quyết định phiên bản Android thấp nhất app hỗ trợ. `Compile SDK` là API mức (level / 수준) trình biên dịch (compiler / 컴파일러) dùng để compile; `Target SDK` cho Android biết ứng dụng đã được thiết kế/kiểm thử (test / 테스트) theo hành vi của API mức (level / 수준) nào; `Min SDK` là giới hạn thấp nhất có thể cài.

Không nên hiểu sai rằng tăng `compileSdk` sẽ khiến app chỉ chạy trên Android mới. Khả năng cài phụ thuộc chủ yếu vào `minSdk`; còn API mới phải được guard nếu có thể chạy trên OS thấp hơn.

# 3. Cấu trúc dự án (project / 프로젝트) và Gradle

Một dự án (project / 프로젝트) Android thường có gốc (root / 루트) dự án (project / 프로젝트) và một hoặc nhiều mô-đun (module / 모듈). mô-đun (module / 모듈) ứng dụng thường tên là `app`.

```text
project/
├─ settings.gradle.kts
├─ build.gradle.kts
├─ gradle.properties
├─ gradle/libs.versions.toml
└─ app/
   ├─ build.gradle.kts
   └─ src/
      ├─ main/
      │  ├─ AndroidManifest.xml
      │  ├─ java/ hoặc kotlin/
      │  └─ res/
      ├─ test/
      └─ androidTest/
```

Tệp (file / 파일) có hậu tố `.kts` dùng Kotlin DSL. `settings.gradle.kts` khai báo mô-đun (module / 모듈) và repository cấp dự án (project / 프로젝트). `app/build.gradle.kts` khai báo plugin Android/Kotlin, không gian tên (namespace / 네임스페이스), SDK versions, bản dựng (build / 빌드) types và dependencies.

Ví dụ rút gọn:

```kotlin
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = "com.example.myapp"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.example.myapp"
        minSdk = 24
        targetSdk = 36
        versionCode = 1
        versionName = "1.0"
    }
}
```

Phiên bản (version / 버전) danh mục (catalog / 카탈로그) trong `gradle/libs.versions.toml` giúp gom phiên bản (version / 버전) phụ thuộc (dependency / 의존성). dự án (project / 프로젝트) cũ có thể khai báo trực tiếp `implementation("group:artifact:version")`; đây không sai về bản chất nhưng khó quản lý hơn ở dự án (project / 프로젝트) lớn.

# 4. Cú pháp Kotlin nền tảng

Tệp (file / 파일) Kotlin có thể chứa gói (package / 패키지) declaration, import, lớp (class / 클래스), hàm (function / 함수) và top-level thuộc tính (property / 속성)/hàm (function / 함수). Kotlin không bắt buộc mọi hàm (function / 함수) phải nằm trong lớp (class / 클래스) như Java.

```kotlin
package com.example.demo

fun main() {
    println("Hello Kotlin")
}
```

Dấu chấm phẩy thường không cần. Kotlin coi nhiều cấu trúc là expression, nghĩa là chúng có thể trả về giá trị.

## 4.1 `val` và `var`

`val` là tham chiếu (reference / 참조) chỉ được gán một lần; `var` là tham chiếu (reference / 참조) có thể gán lại.

```kotlin
val name = "Minh"
var age = 20
age = 21
```

`val` không có nghĩa đối tượng (object / 객체) bên trong bất biến tuyệt đối. Nếu `val list = mutableListOf(1, 2)`, bạn không thể gán `list = ...` nhưng vẫn có thể `list.add(3)`. Đây là khác biệt giữa tham chiếu (reference / 참조) immutability và đối tượng (object / 객체) immutability.

Quy ước môi trường vận hành (production / 운영 환경) là ưu tiên `val`, chỉ dùng `var` khi thực sự cần mutation.

## 4.2 kiểu (type / 타입) suy luận (inference / 추론)

Trình biên dịch (compiler / 컴파일러) thường tự suy ra kiểu:

```kotlin
val count = 10        // Int
val price = 12.5      // Double
val title = "Kotlin" // String
```

Có thể ghi rõ kiểu khi Đặc tả API (API contract / API 계약) cần dễ đọc:

```kotlin
val userId: Long = 100L
```

# 5. Kiểu dữ liệu và null-safety

Các kiểu số quen thuộc gồm `Byte`, `Short`, `Int`, `Long`, `Float`, `Double`; ngoài ra có `Boolean`, `Char`, `String`. Kotlin không có thành phần nguyên thủy (primitive / 기본 요소) kiểu (type / 타입) theo cách Java biểu diễn trong nguồn (source / 소스); trình biên dịch (compiler / 컴파일러) tối ưu thành thành phần nguyên thủy (primitive / 기본 요소)/JVM wrapper tùy ngữ cảnh.

```kotlin
val i: Int = 10
val l: Long = 10L
val f: Float = 1.5f
val d: Double = 1.5
val ok: Boolean = true
val c: Char = 'A'
val s: String = "Hello"
```

## 5.1 String template

```kotlin
val name = "Lan"
val age = 25
println("Name: $name, next year: ${age + 1}")
```

## 5.2 Nullable kiểu (type / 타입)

Kotlin tách `String` và `String?`. `String` không được nhận `null`; `String?` có thể nhận null.

```kotlin
var nickname: String? = null
```

Null-safety là một trong các điểm khác Kotlin với Java. Tuy nhiên Kotlin không loại bỏ hoàn toàn NPE, vì NPE vẫn có thể xuất hiện từ `!!`, Java interop, initialization bug hoặc khung phần mềm (framework / 프레임워크).

### Safe lời gọi (call / 호출) `?.`

```kotlin
val length = nickname?.length
```

Nếu `nickname == null`, biểu thức trả `null` thay vì crash.

### Elvis operator `?:`

```kotlin
val displayName = nickname ?: "Guest"
```

### Not-null assertion `!!`

```kotlin
val length = nickname!!.length
```

`!!` nói với trình biên dịch (compiler / 컴파일러) “tôi chắc chắn giá trị không null”. Nếu bạn sai, app crash. Trong môi trường vận hành (production / 운영 환경), `!!` nên hiếm và chỉ dùng khi bất biến (invariant / 불변식) thực sự được đảm bảo hoặc trong kiểm thử (test / 테스트)/prototype.

### Safe cast `as?`

```kotlin
val text = value as? String
```

Nếu cast không hợp lệ, kết quả là null thay vì `ClassCastException`.

## 5.3 Smart cast

```kotlin
fun printLength(value: Any) {
    if (value is String) {
        println(value.length)
    }
}
```

Sau khi kiểm tra `is String`, trình biên dịch (compiler / 컴파일러) hiểu `value` là `String` trong nhánh đó nếu điều kiện smart-cast được đảm bảo.

# 6. Toán tử và biểu thức

Kotlin có toán tử số học `+ - * / %`, so sánh `< <= > >=`, equality `== !=`, tham chiếu (reference / 참조) equality `=== !==`, boolean `&& || !`, phạm vi (range / 범위) `..`, `until`, `in`, `!in`.

`==` gọi ngữ nghĩa (semantic / 의미적) equality tương đương `equals`; `===` kiểm tra hai tham chiếu (reference / 참조) có trỏ cùng đối tượng (object / 객체) không.

```kotlin
val a = String(charArrayOf('h', 'i'))
val b = String(charArrayOf('h', 'i'))
println(a == b)   // true
println(a === b)  // thường false
```

Kotlin không hỗ trợ implicit numeric widening như Java. `Int` không tự trở thành `Long` trong mọi phép gán.

```kotlin
val x: Int = 10
val y: Long = x.toLong()
```

# 7. Điều khiển luồng

## 7.1 `if` là expression

```kotlin
val max = if (a > b) a else b
```

Kotlin không có ternary operator `condition ? a : b` vì `if` đã là expression.

## 7.2 `when`

`when` thay thế nhiều use trường hợp (case / 사례) của `switch` và mạnh hơn `switch` truyền thống.

```kotlin
val label = when (score) {
    in 90..100 -> "A"
    in 80..89 -> "B"
    else -> "Other"
}
```

Có thể match kiểu (type / 타입):

```kotlin
fun describe(x: Any) = when (x) {
    is String -> "String length=${x.length}"
    is Int -> "Int"
    else -> "Unknown"
}
```

## 7.3 vòng lặp (loop / 루프)

```kotlin
for (i in 0 until 5) println(i)
for (i in 5 downTo 1) println(i)
for (i in 0..10 step 2) println(i)
```

`0..5` bao gồm 5; `0 until 5` không bao gồm 5. Đây là lỗi off-by-one rất thường gặp.

`while` và `do-while` hoạt động giống các ngôn ngữ C-family.

# 8. hàm (function / 함수)

```kotlin
fun add(a: Int, b: Int): Int {
    return a + b
}
```

Expression body:

```kotlin
fun add(a: Int, b: Int) = a + b
```

## 8.1 Default argument và named argument

```kotlin
fun greet(name: String, prefix: String = "Hello") = "$prefix $name"

greet("Minh")
greet(name = "Minh", prefix = "Hi")
```

Cách này giảm nhu cầu overload nhiều phương thức (method / 메서드) như Java.

## 8.2 `Unit`, `Nothing`

`Unit` tương đương ý nghĩa “không trả dữ liệu có ích”, gần với `void` nhưng là một kiểu (type / 타입) thực tế.

`Nothing` biểu diễn hàm (function / 함수) không bao giờ return bình thường, ví dụ luôn throw exception.

```kotlin
fun fail(message: String): Nothing = throw IllegalStateException(message)
```

## 8.3 Vararg

```kotlin
fun sum(vararg values: Int): Int = values.sum()
```

Dùng spread operator `*` để truyền array vào vararg:

```kotlin
val arr = intArrayOf(1, 2, 3)
sum(*arr)
```

# 9. lớp (class / 클래스) và đối tượng (object / 객체)

```kotlin
class User(val name: String, var age: Int)

val user = User("Minh", 25)
println(user.name)
user.age++
```

Primary constructor nằm ngay sau tên lớp (class / 클래스). Nếu cần lô-gic (logic / 논리) khởi tạo, dùng `init`.

```kotlin
class User(val name: String) {
    init {
        require(name.isNotBlank())
    }
}
```

## 9.1 Secondary constructor

```kotlin
class Person(val name: String) {
    var age: Int = 0

    constructor(name: String, age: Int) : this(name) {
        this.age = age
    }
}
```

Trong Kotlin hiện đại, secondary constructor ít cần hơn vì default arguments, factory functions và named arguments thường rõ hơn.

# 10. thuộc tính (property / 속성), getter/setter và backing trường dữ liệu (field / 필드)

Thuộc tính (property / 속성) Kotlin không đơn giản chỉ là công khai (public / 공개) trường dữ liệu (field / 필드). Nó có getter/setter ngữ nghĩa (semantics / 의미론).

```kotlin
class Temperature {
    var celsius: Double = 0.0
        set(value) {
            field = value.coerceAtLeast(-273.15)
        }
}
```

`field` là backing trường dữ liệu (field / 필드) đặc biệt chỉ tồn tại trong accessor khi trình biên dịch (compiler / 컴파일러) tạo backing trường dữ liệu (field / 필드).

Computed thuộc tính (property / 속성):

```kotlin
val Temperature.fahrenheit: Double
    get() = celsius * 9 / 5 + 32
```

# 11. Inheritance, giao diện (interface / 인터페이스) và abstract lớp (class / 클래스)

Lớp (class / 클래스) Kotlin mặc định là `final`. Muốn kế thừa phải dùng `open`.

```kotlin
open class Animal {
    open fun sound() = "..."
}

class Dog : Animal() {
    override fun sound() = "Woof"
}
```

Giao diện (interface / 인터페이스) mô tả đặc tả hợp đồng (contract / 계약) và có thể chứa default hiện thực (implementation / 구현).

```kotlin
interface Clickable {
    fun click()
    fun description() = "Clickable"
}
```

Abstract lớp (class / 클래스) phù hợp khi muốn chia sẻ trạng thái (state / 상태)/constructor/partial hiện thực (implementation / 구현) giữa các subclass có quan hệ chặt. giao diện (interface / 인터페이스) phù hợp cho năng lực (capability / 역량) hoặc đặc tả hợp đồng (contract / 계약) và hỗ trợ multiple inheritance of kiểu (type / 타입).

# 12. dữ liệu (data / 데이터) lớp (class / 클래스), enum lớp (class / 클래스) và sealed lớp (class / 클래스)

## 12.1 dữ liệu (data / 데이터) lớp (class / 클래스)

```kotlin
data class User(
    val id: Long,
    val name: String
)
```

Trình biên dịch (compiler / 컴파일러) sinh `equals`, `hashCode`, `toString`, `componentN`, `copy` dựa chủ yếu trên properties trong primary constructor.

```kotlin
val u2 = u1.copy(name = "Lan")
```

Dữ liệu (data / 데이터) lớp (class / 클래스) rất phù hợp cho DTO, UI mô hình (model / 모델), trạng thái (state / 상태) đối tượng (object / 객체) nhỏ. Không nên mặc định dùng dữ liệu (data / 데이터) lớp (class / 클래스) cho thực thể (entity / 엔터티) giàu hành vi (behavior / 동작) nếu định danh (identity / 식별자)/vòng đời (lifecycle / 생명주기) quan trọng.

## 12.2 Enum

```kotlin
enum class Role { ADMIN, USER, GUEST }
```

Enum phù hợp tập giá trị cố định cùng kiểu (type / 타입).

## 12.3 Sealed lớp (class / 클래스)/giao diện (interface / 인터페이스)

```kotlin
sealed interface UiState {
    data object Loading : UiState
    data class Success(val items: List<String>) : UiState
    data class Error(val message: String) : UiState
}
```

Sealed hierarchy rất hữu ích khi mô hình (model / 모델) một tập trạng thái đóng. `when` có thể exhaustive mà không cần `else` nếu đã cover toàn bộ subtype.

# 13. Collection cơ bản

Kotlin phân biệt giao diện (interface / 인터페이스) read-only (`List`, `Set`, `Map`) với mutable (`MutableList`, `MutableSet`, `MutableMap`). Read-only không đồng nghĩa deep immutable; nó chỉ không expose API mutation qua tham chiếu (reference / 참조) đó.

```kotlin
val names = listOf("A", "B")
val mutable = mutableListOf("A", "B")
mutable.add("C")
```

Các thao tác (operation / 연산) thường dùng:

```kotlin
val numbers = listOf(1, 2, 3, 4)
val doubled = numbers.map { it * 2 }
val evens = numbers.filter { it % 2 == 0 }
val first = numbers.firstOrNull()
val total = numbers.sum()
```

`map` biến đổi từng phần tử; `filter` giữ phần tử thỏa điều kiện; `flatMap` vừa transform vừa flatten; `associateBy` tạo map theo key; `groupBy` gom nhiều phần tử theo key.

# 14. Lambda và higher-order hàm (function / 함수)

Lambda là hàm (function / 함수) literal.

```kotlin
val square: (Int) -> Int = { x -> x * x }
```

Higher-order hàm (function / 함수) nhận hoặc trả hàm (function / 함수).

```kotlin
fun calculate(a: Int, b: Int, op: (Int, Int) -> Int): Int = op(a, b)

calculate(2, 3) { x, y -> x + y }
```

Nếu lambda là tham số cuối, có thể dùng trailing lambda. Đây là idiom quan trọng tạo DSL-like API trong Kotlin và Compose.

# 15. Exception và kết quả (result / 결과) nhập môn

Kotlin không có checked exception. `try` cũng là expression.

```kotlin
val number = try {
    text.toInt()
} catch (e: NumberFormatException) {
    0
}
```

Có thể dùng `runCatching`:

```kotlin
val result = runCatching { riskyOperation() }
result.onSuccess { println(it) }
      .onFailure { println(it.message) }
```

`Result` tiện cho ranh giới (boundary / 경계) đơn giản nhưng không nên dùng vô thức thay cho lĩnh vực (domain / 도메인) lỗi (error / 오류) mô hình (model / 모델). Ở mức (level / 수준) cao hơn sẽ học sealed lỗi (error / 오류) và exception chiến lược (strategy / 전략).

# 16. Android thành phần (component / 컴포넌트) căn bản

Bốn thành phần (component / 컴포넌트) kinh điển của Android là Activity, dịch vụ (service / 서비스), BroadcastReceiver và ContentProvider. Trong app hiện đại, Activity thường là entry điểm (point / 지점) chứa Compose cây (tree / 트리) hoặc Fragment host. dịch vụ (service / 서비스) dành cho công việc cần thành phần (component / 컴포넌트) dịch vụ (service / 서비스) ngữ nghĩa (semantics / 의미론); BroadcastReceiver nhận broadcast; ContentProvider expose/share dữ liệu (data / 데이터) qua URI đặc tả hợp đồng (contract / 계약).

`Context` là handle tới môi trường Android, dùng để truy cập resources, hệ thống (system / 시스템) services, start Activity và nhiều khung phần mềm (framework / 프레임워크) API. Không được giữ `Activity Context` trong singleton lâu dài vì có thể gây bộ nhớ (memory / 메모리) leak. Nếu đối tượng (object / 객체) sống toàn app, thường dùng `applicationContext` nếu API cho phép.

`Intent` mô tả một hành động muốn Android thực hiện.

```kotlin
val intent = Intent(this, DetailActivity::class.java)
startActivity(intent)
```

Implicit Intent:

```kotlin
val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://example.com"))
startActivity(intent)
```

# 17. Jetpack Compose căn bản

Jetpack Compose là UI toolkit declarative và là hướng ưu tiên cho UI mới trong baseline hiện tại. Thay vì tạo View rồi mutation từng thuộc tính, bạn mô tả UI như hàm (function / 함수) của trạng thái (state / 상태). Khi trạng thái (state / 상태) thay đổi, Compose chạy recomposition ở phần cần thiết.

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Hello $name")
}
```

`@Composable` không đơn thuần là annotation trang trí. trình biên dịch (compiler / 컴파일러) Compose plugin biến đổi hàm (function / 함수) để thời gian chạy (runtime / 런타임) có thể theo dõi composition, trạng thái (state / 상태) read và recomposition.

## 17.1 bố cục (layout / 레이아웃) cơ bản

```kotlin
@Composable
fun Profile() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text("Title")
        Spacer(Modifier.height(8.dp))
        Button(onClick = { /* event */ }) {
            Text("Save")
        }
    }
}
```

`Row` xếp ngang, `Column` xếp dọc, `Box` chồng/position child, `LazyColumn` kết xuất (render / 렌더링) danh sách lazy.

`Modifier` là chuỗi decorator-like để mô tả bố cục (layout / 레이아웃), đầu vào (input / 입력), ngữ nghĩa (semantics / 의미론), drawing. Thứ tự modifier có thể thay đổi kết quả.

```kotlin
Modifier
    .padding(16.dp)
    .background(Color.Red)
```

khác với:

```kotlin
Modifier
    .background(Color.Red)
    .padding(16.dp)
```

Vì modifier được áp dụng theo chuỗi (chain / 사슬) và mỗi nút (node / 노드) có thể wrap nút (node / 노드) tiếp theo.

# 18. XML/View hệ thống (system / 시스템) căn bản

XML + View/ViewGroup hiện là **Supported legacy/coexistence**, không phải “API sai”. Hệ thống này vẫn rất phổ biến trong môi trường vận hành (production / 운영 환경) và còn phù hợp khi maintain màn hình cũ, dùng widget/View-only SDK hoặc migrate từng phần. Với tính năng (feature / 기능) UI mới trong ngăn xếp (stack / 스택) hiện đại, Compose thường là hướng ưu tiên; nhưng việc rewrite một màn hình View đang ổn chỉ để “hiện đại (modern / 현대적)” không tự động tạo giá trị.

```xml
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/titleText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello" />
</LinearLayout>
```

Trong Activity cũ hoặc View-based Activity:

```kotlin
setContentView(R.layout.activity_main)
val title = findViewById<TextView>(R.id.titleText)
```

`findViewById` **vẫn được hỗ trợ (support / 지원)**. Nó không phải deprecated; chỉ là View Binding thường giảm cast/lookup boilerplate và an toàn hơn cho mã (code / 코드) View mới.

```kotlin
private lateinit var binding: ActivityMainBinding

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    binding = ActivityMainBinding.inflate(layoutInflater)
    setContentView(binding.root)
    binding.titleText.text = "Hello"
}
```

Kotlin Android Extensions synthetic view truy cập (access / 접근) (`kotlinx.android.synthetic`) thuộc nhóm **Historical/removed workflow** và không nên học như cách triển khai mới.

Một codebase có Compose + Fragment/XML cùng tồn tại không phải “di chuyển (migration / 마이그레이션) thất bại”. Đây thường là trạng thái chuyển đổi hợp lý. Compose có `AndroidView` để host View; View hierarchy có thể host Compose qua `ComposeView`. Interop ranh giới (boundary / 경계) sẽ được học sâu hơn ở Intermediate/cấp cao (senior / 시니어).

# 19. trạng thái (state / 상태), sự kiện (event / 이벤트) và vòng đời (lifecycle / 생명주기) nhập môn

Trong Compose, cục bộ (local / 로컬) trạng thái (state / 상태) thường dùng `remember` và `mutableStateOf`.

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableIntStateOf(0) }

    Button(onClick = { count++ }) {
        Text("Count: $count")
    }
}
```

`remember` giữ giá trị qua recomposition, nhưng không tự sống qua Activity recreation. Nếu cần lưu UI trạng thái (state / 상태) nhỏ qua cấu hình (configuration / 구성)/tiến trình (process / 프로세스) recreation có giới hạn, dùng `rememberSaveable` khi kiểu (type / 타입) có thể save.

Trạng thái (state / 상태) hoisting là đưa trạng thái (state / 상태) lên caller để composable dễ kiểm thử (test / 테스트) và reusable:

```kotlin
@Composable
fun Counter(
    count: Int,
    onIncrement: () -> Unit
) {
    Button(onClick = onIncrement) {
        Text("Count: $count")
    }
}
```

Android vòng đời (lifecycle / 생명주기) kinh điển của Activity gồm `onCreate`, `onStart`, `onResume`, `onPause`, `onStop`, `onDestroy`. Không nên hiểu vòng đời (lifecycle / 생명주기) như “mỗi lần đóng app chắc chắn sẽ gọi onDestroy”; tiến trình (process / 프로세스) có thể bị OS kill mà không có callback cuối cùng theo cách bạn kỳ vọng.

# 20. điều hướng (navigation / 내비게이션) nhập môn

Điều hướng (navigation / 내비게이션) Compose giúp định nghĩa destination và chuyển màn hình.

```kotlin
NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(...) }
    composable("detail/{id}") { backStackEntry ->
        val id = backStackEntry.arguments?.getString("id")
        DetailScreen(id)
    }
}
```

Tuyến (route / 경로) string là cách rất phổ biến trong dự án (project / 프로젝트) Compose cũ và vẫn có thể hoạt động tốt. Với dự án (project / 프로젝트) mới và điều hướng (navigation / 내비게이션) phiên bản (version / 버전) hỗ trợ, type-safe tuyến (route / 경로) API là hướng ưu tiên vì giảm stringly-typed argument/tuyến (route / 경로) lỗi (error / 오류). Đây là ví dụ điển hình của **Supported legacy/coexistence → hiện đại (modern / 현대적) preferred**, không phải “cũ = lỗi”.

# 21. tài nguyên (resource / 자원), Manifest và permission

Resources nằm trong `res/`: `drawable`, `mipmap`, `values`, `font`, `xml`, `raw`... String nên đặt trong `res/values/strings.xml` để hỗ trợ localization.

```xml
<string name="welcome">Welcome</string>
```

AndroidManifest khai báo thành phần (component / 컴포넌트), permission và app siêu dữ liệu (metadata / 메타데이터).

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

Một số permission là normal và được grant tự động; dangerous permission còn cần thời gian chạy (runtime / 런타임) permission luồng (flow / 흐름) trên phiên bản Android phù hợp.

# 22. gỡ lỗi (debug / 디버그), Logcat và lỗi thường gặp

Dùng breakpoint khi cần quan sát trạng thái (state / 상태) chính xác; dùng Logcat khi cần dấu vết (trace / 추적) vòng đời (lifecycle / 생명주기), mạng (network / 네트워크), sự kiện (event / 이벤트) hoặc crash. Tránh log đơn vị từ (token / 토큰)/password/PII trong môi trường vận hành (production / 운영 환경).

```kotlin
Log.d("MainActivity", "onCreate")
Log.e("Network", "Request failed", throwable)
```

Lỗi Beginner thường gặp gồm: dùng `!!` để “cho trình biên dịch (compiler / 컴파일러) im”, hiểu sai `val` là immutable đối tượng (object / 객체), chạy mạng (network / 네트워크) trên main luồng thực thi (thread / 스레드), quên vòng đời (lifecycle / 생명주기), giữ Activity ngữ cảnh (context / 맥락) trong singleton, dùng danh sách (list / 목록) chỉ mục (index / 인덱스) không kiểm tra, hiểu `0..size` thay vì `0 until size`, mutation trạng thái (state / 상태) Compose không observable, và nhét toàn bộ lô-gic (logic / 논리) vào Activity/Composable.

# 23. Mini dự án (project / 프로젝트) tổng hợp: Todo đơn giản

Mục tiêu mini dự án (project / 프로젝트) là tạo app Todo với một màn hình nhập tác vụ (task / 작업) và danh sách tác vụ (task / 작업). Phiên bản Beginner chưa cần cơ sở dữ liệu (database / 데이터베이스); dùng trạng thái (state / 상태) trong bộ nhớ (memory / 메모리).

```kotlin
@Composable
fun TodoScreen() {
    var input by remember { mutableStateOf("") }
    var items by remember { mutableStateOf(listOf<String>()) }

    Column(Modifier.padding(16.dp)) {
        OutlinedTextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Task") }
        )

        Button(
            onClick = {
                val text = input.trim()
                if (text.isNotEmpty()) {
                    items = items + text
                    input = ""
                }
            }
        ) {
            Text("Add")
        }

        LazyColumn {
            items(items) { item ->
                Text(item)
            }
        }
    }
}
```

Điểm cần hiểu không phải chỉ là mã (code / 코드) chạy được. `input` là trạng thái (state / 상태) cục bộ (local / 로컬); `items = items + text` tạo danh sách (list / 목록) mới nên `mutableStateOf` nhận tham chiếu (reference / 참조) mới và Compose dễ thấy thay đổi; UI chỉ là hàm (function / 함수) của trạng thái (state / 상태); callback `onClick` là sự kiện (event / 이벤트) đưa hệ thống từ trạng thái (state / 상태) cũ sang trạng thái (state / 상태) mới.

Ở Intermediate, dự án (project / 프로젝트) này sẽ được nâng cấp thành ViewModel + StateFlow + Room + điều hướng (navigation / 내비게이션) + repository.

# 24. Checklist Beginner

Sau mức (level / 수준) này, bạn nên tự giải thích được sự khác nhau giữa Kotlin ngôn ngữ (language / 언어), Android SDK và Jetpack; hiểu Gradle mô-đun (module / 모듈)/phụ thuộc (dependency / 의존성) cơ bản; dùng `val`, `var`, nullable kiểu (type / 타입), safe lời gọi (call / 호출), Elvis, `when`, vòng lặp (loop / 루프), hàm (function / 함수), lớp (class / 클래스), inheritance, giao diện (interface / 인터페이스), dữ liệu (data / 데이터) lớp (class / 클래스), sealed lớp (class / 클래스) và collection; viết lambda; hiểu Activity/ngữ cảnh (context / 맥락)/Intent; tạo Compose UI; hiểu trạng thái (state / 상태)/recomposition ở mức cơ bản; đọc được XML/View Binding mã (code / 코드); hiểu tài nguyên (resource / 자원)/manifest/permission; chạy debugger và đọc Logcat.

Bạn cũng phải phân biệt được ba câu hoàn toàn khác nhau:

```text
API này cũ hơn
API này deprecated
API này không còn nên dùng cho code mới
```

Một API có thể “cũ” nhưng vẫn được hỗ trợ (support / 지원) và đúng với ngữ cảnh (context / 맥락) hiện tại. Nếu chưa phân biệt được điều này, rất dễ biến modernization thành rewrite không cần thiết.

Nếu còn thấy `?.`, `?:`, `let`, lambda, `@Composable`, `remember`, `Modifier`, `Context`, `Intent`, `ViewModel` là những từ “ma thuật” chưa giải thích được bằng lời của mình, chưa nên chuyển nhanh sang các kiến trúc (architecture / 아키텍처) phức tạp.

---

## Phiên bản (version / 버전) & Legacy Notes — cách đọc API cũ và mới

Kotlin hiện đại sử dụng K2 trình biên dịch (compiler / 컴파일러) line và Kotlin 2.x, nhưng Android dự án (project / 프로젝트) tồn tại qua nhiều thế hệ. Beginner cần học cách **phân loại** thay vì học một bảng “cũ → mới” rồi thay thế máy móc.

### Nhóm 1 — hiện đại (modern / 현대적) preferred cho mã (code / 코드) mới

Trong baseline hiện tại, các hướng thường được ưu tiên gồm Compose cho UI mới; Activity kết quả (result / 결과) APIs cho kết quả (result / 결과)/permission đặc tả hợp đồng (contract / 계약); coroutine cho asynchronous lô-gic (logic / 논리) có thời gian tồn tại (lifetime / 수명) rõ; ViewModel cho screen-level trạng thái (state / 상태) holder; WorkManager cho durable deferred công việc (work / 작업); DataStore cho nhiều use trường hợp (case / 사례) settings mới; type-safe điều hướng (navigation / 내비게이션) khi điều hướng (navigation / 내비게이션) ngăn xếp (stack / 스택) hỗ trợ.

Những lựa chọn này vẫn phải đúng với yêu cầu (requirement / 요구사항). Coroutine không thay WorkManager; WorkManager không thay foreground dịch vụ (service / 서비스); DataStore không thay cơ sở dữ liệu (database / 데이터베이스); Compose không làm vòng đời (lifecycle / 생명주기) tự biến mất.

### Nhóm 2 — Supported legacy / coexistence

Các API như XML/View, Fragment, RecyclerView, View Binding, LiveData, SharedPreferences và RxJava vẫn có thể xuất hiện hợp lệ trong môi trường vận hành (production / 운영 환경). Chúng không cần rewrite chỉ vì tutorial mới dùng ngăn xếp (stack / 스택) khác.

Ví dụ:

```text
XML/View
→ vẫn đúng khi maintain màn hình View hoặc SDK chỉ expose View

LiveData
→ vẫn hoạt động tốt với lifecycle-aware observer trong codebase hiện hữu

SharedPreferences
→ vẫn usable cho một số key-value đơn giản; DataStore là hướng hiện đại hơn cho nhiều case mới

RxJava
→ vẫn có thể là nền tảng async ổn định của codebase lớn; migration sang Flow nên incremental
```

### Nhóm 3 — Deprecated: cần di chuyển (migration / 마이그레이션) plan

`AsyncTask` và `startActivityForResult`/`onActivityResult` là ví dụ dễ gặp. Deprecated không có nghĩa app lập tức ngừng chạy; nó có nghĩa nền tảng (platform / 플랫폼)/thư viện (library / 라이브러리) đã chỉ hướng khác và technical debt sẽ tăng nếu tiếp tục mở rộng mã (code / 코드) mới dựa trên API đó.

Đặc biệt, không có replacement one-to-one cho mọi API:

```text
AsyncTask
→ coroutine nếu work gắn với scope/lifecycle
→ WorkManager nếu work cần durable/deferred execution

Service
→ không tự động đổi thành WorkManager
→ service vẫn đúng khi requirement thật sự là service semantics
```

### Nhóm 4 — Historical/removed workflow

`kotlinx.android.synthetic` là ví dụ cần biết để đọc nguồn (source / 소스) cũ nhưng không nên dùng cho mã (code / 코드) mới. Tutorial cũ có thể vẫn chứa import synthetic; khi gặp chúng, cần hiểu đó là dấu vết generation của dự án (project / 프로젝트) thay vì bản sao (copy / 복사) vào template hiện đại.

### Beginner di chuyển (migration / 마이그레이션) quy tắc (rule / 규칙)

Trước khi thay API, luôn hỏi:

```text
API hiện tại có deprecated không?
replacement giải quyết cùng lifetime/contract không?
test nào giữ behavior cũ?
migration có thể làm incremental không?
code cũ và mới cần coexist trong bao lâu?
```

Nếu chưa trả lời được các câu này, “đổi sang API mới” chưa phải một di chuyển (migration / 마이그레이션) plan.

---

# 25. Các modifier và cấu trúc Kotlin thường gặp nhưng dễ bỏ sót

Sau khi đã hiểu lớp (class / 클래스), hàm (function / 함수) và thuộc tính (property / 속성), cần làm quen với nhóm **modifier** vì chúng xuất hiện dày đặc trong mã (code / 코드) Android thực tế. `public` là mặc định; `private` giới hạn trong lớp (class / 클래스)/tệp (file / 파일) tương ứng; `protected` dành cho lớp (class / 클래스) con; `internal` giới hạn theo Kotlin mô-đun (module / 모듈). `internal` rất hữu ích khi xây mô-đun (module / 모듈) Android vì nó cho phép hiện thực (implementation / 구현) được chia sẻ bên trong mô-đun (module / 모듈) nhưng không trở thành API công khai (public API / 공개 API) cho mô-đun (module / 모듈) khác.

```kotlin
internal class TokenParser {
    private fun normalize(raw: String): String = raw.trim()
}
```

`const val` khác `val` thông thường ở chỗ nó là compile-time constant và chỉ dùng được cho thành phần nguyên thủy (primitive / 기본 요소)/String ở top-level, đối tượng (object / 객체) hoặc companion đối tượng (object / 객체). Nó phù hợp cho constant thực sự như key cố định, nhưng không dùng cho giá trị phải tính lúc thời gian chạy (runtime / 런타임).

```kotlin
const val API_VERSION = "v1"
```

`lateinit var` cho phép trì hoãn khởi tạo một non-null mutable thuộc tính (property / 속성). Nó thường xuất hiện trong Android View Binding hoặc kiểm thử (test / 테스트) setup cũ, nhưng nếu đọc trước khi được gán sẽ ném `UninitializedPropertyAccessException`. Vì vậy `lateinit` không phải null-safety “miễn phí”; nó chỉ chuyển bất biến (invariant / 불변식) từ compile thời gian (time / 시간) sang thời gian chạy (runtime / 런타임).

```kotlin
private lateinit var binding: ActivityMainBinding
```

`lazy` thì khác: nó thường đi cùng `val` và tính giá trị ở lần truy cập đầu tiên. Đây là lazy initialization chứ không phải “biến chưa khởi tạo”.

```kotlin
val database by lazy { createDatabase() }
```

Kotlin còn hỗ trợ destructuring qua `componentN()`; dữ liệu (data / 데이터) lớp (class / 클래스) tự sinh các thành phần (component / 컴포넌트) tương ứng. Cú pháp này tiện khi pair hoặc đối tượng (object / 객체) nhỏ, nhưng nếu destructure quá nhiều trường dữ liệu (field / 필드) thì mã (code / 코드) khó hiểu hơn gọi tên thuộc tính (property / 속성) trực tiếp.

```kotlin
val (name, age) = User("An", 28)
```

# 26. Android Studio workflow: từ mã nguồn (source code / 소스 코드) đến APK/AAB

Khi bấm **Run**, Android Studio không “chạy tệp (file / 파일) Kotlin trực tiếp”. IDE gọi Gradle; Android Gradle Plugin chọn bản dựng (build / 빌드) variant, compile Kotlin/Java, xử lý tài nguyên (resource / 자원) và manifest, tạo DEX, đóng gói sản phẩm tạo ra (artifact / 산출물), ký bản gỡ lỗi (debug / 디버그) rồi cài lên emulator hoặc thiết bị. Hiểu chuỗi xử lý (pipeline / 파이프라인) này giúp phân biệt lỗi trình biên dịch (compiler / 컴파일러), lỗi tài nguyên (resource / 자원), lỗi manifest merge, lỗi phụ thuộc (dependency / 의존성) và lỗi thời gian chạy (runtime / 런타임).

Các thao tác thường dùng trong Android Studio gồm **Sync dự án (project / 프로젝트) with Gradle Files** khi bản dựng (build / 빌드) script hoặc phụ thuộc (dependency / 의존성) thay đổi; **bản dựng (build / 빌드) > Make dự án (project / 프로젝트)** để compile; **Run** để bản dựng (build / 빌드) và deploy; **gỡ lỗi (debug / 디버그)** để attach debugger; **Logcat** để xem log thời gian chạy (runtime / 런타임); **App Inspection** cho cơ sở dữ liệu (database / 데이터베이스)/mạng (network / 네트워크) tùy tooling; **Profiler** và **bố cục (layout / 레이아웃) Inspector** để điều tra hiệu năng (performance / 성능)/UI. `Clean Project` không nên trở thành phản xạ mỗi khi lỗi vì nó xóa bộ nhớ đệm (cache / 캐시) bản dựng (build / 빌드) hữu ích; trước tiên cần đọc lỗi và xác định tác vụ (task / 작업) nào thất bại.

Trong Gradle, `debug` và `release` là hai bản dựng (build / 빌드) kiểu (type / 타입) quen thuộc. Bản gỡ lỗi (debug / 디버그) thường debuggable và dùng gỡ lỗi (debug / 디버그) signing key; bản bản phát hành (release / 릴리스) thường bật tối ưu hóa (optimization / 최적화)/shrinking theo cấu hình và phải dùng signing key phù hợp để phát hành. APK là gói (package / 패키지) cài đặt trực tiếp; Android App Bundle (`.aab`) là format phát hành lên Google Play để Play tạo APK tối ưu cho từng thiết bị.

# 27. Activity kết quả (result / 결과) API và thời gian chạy (runtime / 런타임) permission theo cách hiện đại

Mã (code / 코드) Android cũ thường dùng `startActivityForResult()` và `onActivityResult()`. Cách hiện đại là đăng ký **Activity kết quả (result / 결과) đặc tả hợp đồng (contract / 계약)**. Điểm quan trọng không chỉ là cú pháp (syntax / 문법) mới; đặc tả hợp đồng (contract / 계약) giúp tách kiểu đầu vào (input / 입력)/đầu ra (output / 출력) và tích hợp vòng đời (lifecycle / 생명주기) tốt hơn.

```kotlin
private val pickImage = registerForActivityResult(
    ActivityResultContracts.GetContent()
) { uri ->
    if (uri != null) {
        // sử dụng Uri
    }
}

fun openPicker() {
    pickImage.launch("image/*")
}
```

Thời gian chạy (runtime / 런타임) permission cũng dùng đặc tả hợp đồng (contract / 계약) tương tự. Không được yêu cầu permission chỉ vì manifest đã khai báo. Với permission thuộc nhóm thời gian chạy (runtime / 런타임), ứng dụng phải kiểm tra trạng thái, giải thích khi cần, yêu cầu (request / 요청), rồi xử lý cả trường hợp người dùng từ chối.

```kotlin
private val requestCamera = registerForActivityResult(
    ActivityResultContracts.RequestPermission()
) { granted ->
    if (granted) openCamera()
}
```

Permission hành vi (behavior / 동작) thay đổi theo Android phiên bản (version / 버전). Vì thế mã (code / 코드) môi trường vận hành (production / 운영 환경) cần kiểm tra API mức (level / 수준) và tài liệu nền tảng (platform / 플랫폼) thay vì bản sao (copy / 복사) một snippet cũ rồi giả định nó đúng trên mọi phiên bản.

# 28. tài nguyên (resource / 자원) qualifier, cấu hình (configuration / 구성) và vì sao không hard-code UI

Android tài nguyên (resource / 자원) hệ thống (system / 시스템) tồn tại để một logical tài nguyên (resource / 자원) có thể có nhiều biến thể. Ví dụ `values/strings.xml` chứa string mặc định, `values-ko/` có tiếng Hàn, `values-vi/` có tiếng Việt; drawable/bố cục (layout / 레이아웃) có thể có biến thể theo density, orientation, screen kích thước (size / 크기) hoặc night chế độ (mode / 모드). khung phần mềm (framework / 프레임워크) chọn tài nguyên (resource / 자원) phù hợp với cấu hình (configuration / 구성) thiết bị.

Do đó văn bản (text / 텍스트) hiển thị cho người dùng không nên hard-code trong Kotlin nếu cần localization. Kích thước UI không nên suy nghĩ theo điểm ảnh (pixel / 픽셀) thuần túy; Android dùng `dp` cho kích thước bố cục (layout / 레이아웃) và `sp` cho văn bản (text / 텍스트) để tôn trọng density và font quy mô (scale / 규모). Trong Compose, các lớp trừu tượng (abstraction / 추상화) như `dp`, `sp`, `stringResource()` và theme tiếp tục phản ánh cùng triết lý tài nguyên (resource / 자원)/cấu hình (configuration / 구성) này.

Cấu hình (configuration / 구성) thay đổi (change / 변경) có thể recreate Activity. Nếu trạng thái (state / 상태) chỉ nằm trong trường dữ liệu (field / 필드) của Activity, nó có thể biến mất. trạng thái (state / 상태) UI ngắn hạn có thể dùng `rememberSaveable`; trạng thái (state / 상태) lô-gic (logic / 논리) thường thuộc ViewModel; dữ liệu cần sống qua tiến trình (process / 프로세스) death phải có cơ chế saved trạng thái (state / 상태) hoặc persistence phù hợp. Đây là nền tảng để hiểu sâu hơn ở Intermediate và cấp cao (senior / 시니어).

# 29. Bản đồ tư duy sau Beginner

Sau mức (level / 수준) này, một luồng (flow / 흐름) Android cơ bản nên được hình dung như sau: Gradle bản dựng (build / 빌드) dự án (project / 프로젝트); Android hệ thống (system / 시스템) tạo thành phần (component / 컴포넌트) theo manifest/intent; Activity hoặc Fragment sở hữu vòng đời (lifecycle / 생명주기); UI có thể là Compose hoặc View; UI đọc trạng thái (state / 상태) và phát sự kiện (event / 이벤트); Kotlin cung cấp hệ kiểu (type system / 타입 시스템) và lô-gic (logic / 논리); tài nguyên (resource / 자원) hệ thống (system / 시스템) cung cấp văn bản (text / 텍스트)/ảnh (image / 이미지)/cấu hình (configuration / 구성); permission và nền tảng (platform / 플랫폼) API tạo ranh giới (boundary / 경계) với hệ điều hành. Khi gỡ lỗi (debug / 디버그), hãy xác định lỗi nằm ở bản dựng (build / 빌드) thời gian (time / 시간), thành phần (component / 컴포넌트) vòng đời (lifecycle / 생명주기), trạng thái (state / 상태), tài nguyên (resource / 자원), permission hay lô-gic nghiệp vụ (business logic / 비즈니스 로직) trước khi sửa mã (code / 코드).

> **Bàn giao:** Sau **Beginner di chuyển (migration / 마이그레이션) quy tắc (rule / 규칙)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [02 kotlin intermediate](./02_kotlin_intermediate.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
