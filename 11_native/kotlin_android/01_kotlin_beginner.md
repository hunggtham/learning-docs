# Kotlin + Android Master Note — Beginner

> Mục tiêu: học từ gần như số 0 để có thể đọc, viết và chạy một ứng dụng Android cơ bản bằng Kotlin. Tài liệu ưu tiên Kotlin hiện đại và Jetpack Compose, đồng thời vẫn giải thích XML/View system để bạn hiểu code Android cũ.
>
> Baseline phiên bản khi biên soạn: Kotlin 2.4.x; Android Studio Quail 4 / 2026.1.4 Patch 1 stable. Khi gặp API cũ, tài liệu sẽ đánh dấu rõ `Legacy`, `Deprecated` hoặc `Historical`.

## Mục lục

1. Kotlin là gì và Kotlin nằm ở đâu trong Android
2. Cài Android Studio và tạo project Android đầu tiên
3. Cấu trúc project Gradle
4. Cú pháp Kotlin nền tảng
5. Kiểu dữ liệu, null-safety và type inference
6. Toán tử và biểu thức
7. Điều khiển luồng: if, when, loop
8. Function
9. Class và object
10. Constructor, property, getter/setter
11. Inheritance, interface và abstract class
12. Data class, enum class, sealed class nhập môn
13. Collection cơ bản
14. Lambda và higher-order function nhập môn
15. Exception và Result nhập môn
16. Android component căn bản
17. Jetpack Compose căn bản
18. XML/View system căn bản
19. State, event và lifecycle nhập môn
20. Navigation nhập môn
21. Resource, manifest và permission
22. Debug, Logcat và lỗi thường gặp
23. Mini project tổng hợp
24. Checklist Beginner

---

# 1. Kotlin là gì và Kotlin nằm ở đâu trong Android

Kotlin là ngôn ngữ lập trình hiện đại do JetBrains phát triển. Trên Android, Kotlin không phải là “Android framework” mà là ngôn ngữ dùng để viết mã chạy trên Android Runtime thông qua toolchain của Android. Điều này cần được phân biệt rõ: Kotlin cung cấp syntax, type system, function, coroutine, collection và nhiều abstraction ở cấp ngôn ngữ; Android SDK cung cấp Activity, Service, Context, Intent, View, lifecycle và các API thiết bị; Jetpack cung cấp những thư viện cấp cao như ViewModel, Room, Navigation, WorkManager, Compose.

Một ứng dụng Android Kotlin hiện đại thường có ba lớp công nghệ đan xen: Kotlin language ở lớp cú pháp và logic; Android/Jetpack ở lớp framework; Gradle/Android Gradle Plugin ở lớp build. Khi gặp lỗi, xác định lỗi thuộc lớp nào sẽ giúp debug nhanh hơn. Ví dụ `NullPointerException` có thể liên quan logic Kotlin hoặc Java interop; `ActivityNotFoundException` thuộc Android framework; `Unresolved reference` thường thuộc compiler/dependency/build configuration.

Kotlin tương thích rất tốt với Java. Một project Android có thể có file `.kt` và `.java` cùng lúc. Kotlin gọi Java API trực tiếp, và Java cũng có thể gọi Kotlin nếu signature phù hợp. Điều này đặc biệt quan trọng vì phần lớn Android framework ban đầu được viết bằng Java và nhiều codebase enterprise vẫn còn Java.

## 1.1 Kotlin/JVM, Kotlin Multiplatform và Kotlin/Native

Trong Android truyền thống, mã Kotlin chủ yếu biên dịch cho JVM bytecode rồi được Android build tool chuyển thành DEX để ART chạy. Ngoài Kotlin/JVM, Kotlin còn có Kotlin/JS, Kotlin/Native, Kotlin/Wasm và Kotlin Multiplatform. Tuy nhiên khi mới học Android, không nên trộn KMP vào quá sớm. Hãy nắm chắc Kotlin/JVM + Android trước; KMP phù hợp hơn khi đã hiểu module, dependency, coroutine, serialization và platform boundary.

# 2. Cài Android Studio và tạo project đầu tiên

Android Studio là IDE chính thức của Android. Bản stable hiện tại trong baseline này là Android Studio Quail 4 (2026.1.4 Patch 1). Một bản Android Studio bao gồm editor dựa trên IntelliJ Platform, Gradle integration, Android SDK Manager, Device Manager, emulator, profiler, Layout Inspector, Logcat, debugger và Compose tooling.

Sau khi cài Android Studio, mở `SDK Manager` để kiểm tra Android SDK Platform và Build Tools. Trong `Device Manager`, có thể tạo Android Virtual Device. Emulator phù hợp cho phần lớn việc học; thiết bị thật cần bật `Developer options` và `USB debugging`.

Khi tạo project mới, template `Empty Activity` hiện đại thường dùng Jetpack Compose. Package name nên theo reverse-domain convention như `com.example.myapp`. `Minimum SDK` quyết định phiên bản Android thấp nhất app hỗ trợ. `Compile SDK` là API level compiler dùng để compile; `Target SDK` cho Android biết ứng dụng đã được thiết kế/test theo hành vi của API level nào; `Min SDK` là giới hạn thấp nhất có thể cài.

Không nên hiểu sai rằng tăng `compileSdk` sẽ khiến app chỉ chạy trên Android mới. Khả năng cài phụ thuộc chủ yếu vào `minSdk`; còn API mới phải được guard nếu có thể chạy trên OS thấp hơn.

# 3. Cấu trúc project và Gradle

Một project Android thường có root project và một hoặc nhiều module. Module ứng dụng thường tên là `app`.

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

File có hậu tố `.kts` dùng Kotlin DSL. `settings.gradle.kts` khai báo module và repository cấp project. `app/build.gradle.kts` khai báo plugin Android/Kotlin, namespace, SDK versions, build types và dependencies.

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

Version Catalog trong `gradle/libs.versions.toml` giúp gom version dependency. Project cũ có thể khai báo trực tiếp `implementation("group:artifact:version")`; đây không sai về bản chất nhưng khó quản lý hơn ở project lớn.

# 4. Cú pháp Kotlin nền tảng

File Kotlin có thể chứa package declaration, import, class, function và top-level property/function. Kotlin không bắt buộc mọi function phải nằm trong class như Java.

```kotlin
package com.example.demo

fun main() {
    println("Hello Kotlin")
}
```

Dấu chấm phẩy thường không cần. Kotlin coi nhiều cấu trúc là expression, nghĩa là chúng có thể trả về giá trị.

## 4.1 `val` và `var`

`val` là reference chỉ được gán một lần; `var` là reference có thể gán lại.

```kotlin
val name = "Minh"
var age = 20
age = 21
```

`val` không có nghĩa object bên trong bất biến tuyệt đối. Nếu `val list = mutableListOf(1, 2)`, bạn không thể gán `list = ...` nhưng vẫn có thể `list.add(3)`. Đây là khác biệt giữa reference immutability và object immutability.

Quy ước production là ưu tiên `val`, chỉ dùng `var` khi thực sự cần mutation.

## 4.2 Type inference

Compiler thường tự suy ra kiểu:

```kotlin
val count = 10        // Int
val price = 12.5      // Double
val title = "Kotlin" // String
```

Có thể ghi rõ kiểu khi API contract cần dễ đọc:

```kotlin
val userId: Long = 100L
```

# 5. Kiểu dữ liệu và null-safety

Các kiểu số quen thuộc gồm `Byte`, `Short`, `Int`, `Long`, `Float`, `Double`; ngoài ra có `Boolean`, `Char`, `String`. Kotlin không có primitive type theo cách Java biểu diễn trong source; compiler tối ưu thành primitive/JVM wrapper tùy ngữ cảnh.

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

## 5.2 Nullable type

Kotlin tách `String` và `String?`. `String` không được nhận `null`; `String?` có thể nhận null.

```kotlin
var nickname: String? = null
```

Null-safety là một trong các điểm khác Kotlin với Java. Tuy nhiên Kotlin không loại bỏ hoàn toàn NPE, vì NPE vẫn có thể xuất hiện từ `!!`, Java interop, initialization bug hoặc framework.

### Safe call `?.`

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

`!!` nói với compiler “tôi chắc chắn giá trị không null”. Nếu bạn sai, app crash. Trong production, `!!` nên hiếm và chỉ dùng khi invariant thực sự được đảm bảo hoặc trong test/prototype.

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

Sau khi kiểm tra `is String`, compiler hiểu `value` là `String` trong nhánh đó nếu điều kiện smart-cast được đảm bảo.

# 6. Toán tử và biểu thức

Kotlin có toán tử số học `+ - * / %`, so sánh `< <= > >=`, equality `== !=`, reference equality `=== !==`, boolean `&& || !`, range `..`, `until`, `in`, `!in`.

`==` gọi semantic equality tương đương `equals`; `===` kiểm tra hai reference có trỏ cùng object không.

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

`when` thay thế nhiều use case của `switch` và mạnh hơn `switch` truyền thống.

```kotlin
val label = when (score) {
    in 90..100 -> "A"
    in 80..89 -> "B"
    else -> "Other"
}
```

Có thể match type:

```kotlin
fun describe(x: Any) = when (x) {
    is String -> "String length=${x.length}"
    is Int -> "Int"
    else -> "Unknown"
}
```

## 7.3 Loop

```kotlin
for (i in 0 until 5) println(i)
for (i in 5 downTo 1) println(i)
for (i in 0..10 step 2) println(i)
```

`0..5` bao gồm 5; `0 until 5` không bao gồm 5. Đây là lỗi off-by-one rất thường gặp.

`while` và `do-while` hoạt động giống các ngôn ngữ C-family.

# 8. Function

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

Cách này giảm nhu cầu overload nhiều method như Java.

## 8.2 `Unit`, `Nothing`

`Unit` tương đương ý nghĩa “không trả dữ liệu có ích”, gần với `void` nhưng là một type thực tế.

`Nothing` biểu diễn function không bao giờ return bình thường, ví dụ luôn throw exception.

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

# 9. Class và object

```kotlin
class User(val name: String, var age: Int)

val user = User("Minh", 25)
println(user.name)
user.age++
```

Primary constructor nằm ngay sau tên class. Nếu cần logic khởi tạo, dùng `init`.

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

# 10. Property, getter/setter và backing field

Property Kotlin không đơn giản chỉ là public field. Nó có getter/setter semantics.

```kotlin
class Temperature {
    var celsius: Double = 0.0
        set(value) {
            field = value.coerceAtLeast(-273.15)
        }
}
```

`field` là backing field đặc biệt chỉ tồn tại trong accessor khi compiler tạo backing field.

Computed property:

```kotlin
val Temperature.fahrenheit: Double
    get() = celsius * 9 / 5 + 32
```

# 11. Inheritance, interface và abstract class

Class Kotlin mặc định là `final`. Muốn kế thừa phải dùng `open`.

```kotlin
open class Animal {
    open fun sound() = "..."
}

class Dog : Animal() {
    override fun sound() = "Woof"
}
```

Interface mô tả contract và có thể chứa default implementation.

```kotlin
interface Clickable {
    fun click()
    fun description() = "Clickable"
}
```

Abstract class phù hợp khi muốn chia sẻ state/constructor/partial implementation giữa các subclass có quan hệ chặt. Interface phù hợp cho capability hoặc contract và hỗ trợ multiple inheritance of type.

# 12. Data class, enum class và sealed class

## 12.1 Data class

```kotlin
data class User(
    val id: Long,
    val name: String
)
```

Compiler sinh `equals`, `hashCode`, `toString`, `componentN`, `copy` dựa chủ yếu trên properties trong primary constructor.

```kotlin
val u2 = u1.copy(name = "Lan")
```

Data class rất phù hợp cho DTO, UI model, state object nhỏ. Không nên mặc định dùng data class cho entity giàu behavior nếu identity/lifecycle quan trọng.

## 12.2 Enum

```kotlin
enum class Role { ADMIN, USER, GUEST }
```

Enum phù hợp tập giá trị cố định cùng type.

## 12.3 Sealed class/interface

```kotlin
sealed interface UiState {
    data object Loading : UiState
    data class Success(val items: List<String>) : UiState
    data class Error(val message: String) : UiState
}
```

Sealed hierarchy rất hữu ích khi model một tập trạng thái đóng. `when` có thể exhaustive mà không cần `else` nếu đã cover toàn bộ subtype.

# 13. Collection cơ bản

Kotlin phân biệt interface read-only (`List`, `Set`, `Map`) với mutable (`MutableList`, `MutableSet`, `MutableMap`). Read-only không đồng nghĩa deep immutable; nó chỉ không expose API mutation qua reference đó.

```kotlin
val names = listOf("A", "B")
val mutable = mutableListOf("A", "B")
mutable.add("C")
```

Các operation thường dùng:

```kotlin
val numbers = listOf(1, 2, 3, 4)
val doubled = numbers.map { it * 2 }
val evens = numbers.filter { it % 2 == 0 }
val first = numbers.firstOrNull()
val total = numbers.sum()
```

`map` biến đổi từng phần tử; `filter` giữ phần tử thỏa điều kiện; `flatMap` vừa transform vừa flatten; `associateBy` tạo map theo key; `groupBy` gom nhiều phần tử theo key.

# 14. Lambda và higher-order function

Lambda là function literal.

```kotlin
val square: (Int) -> Int = { x -> x * x }
```

Higher-order function nhận hoặc trả function.

```kotlin
fun calculate(a: Int, b: Int, op: (Int, Int) -> Int): Int = op(a, b)

calculate(2, 3) { x, y -> x + y }
```

Nếu lambda là tham số cuối, có thể dùng trailing lambda. Đây là idiom quan trọng tạo DSL-like API trong Kotlin và Compose.

# 15. Exception và Result nhập môn

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

`Result` tiện cho boundary đơn giản nhưng không nên dùng vô thức thay cho domain error model. Ở level cao hơn sẽ học sealed error và exception strategy.

# 16. Android component căn bản

Bốn component kinh điển của Android là Activity, Service, BroadcastReceiver và ContentProvider. Trong app hiện đại, Activity thường là entry point chứa Compose tree hoặc Fragment host. Service dành cho công việc cần component service semantics; BroadcastReceiver nhận broadcast; ContentProvider expose/share data qua URI contract.

`Context` là handle tới môi trường Android, dùng để truy cập resources, system services, start Activity và nhiều framework API. Không được giữ `Activity Context` trong singleton lâu dài vì có thể gây memory leak. Nếu object sống toàn app, thường dùng `applicationContext` nếu API cho phép.

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

Jetpack Compose là UI toolkit declarative. Thay vì tạo View rồi mutation từng thuộc tính, bạn mô tả UI như function của state. Khi state thay đổi, Compose chạy recomposition ở phần cần thiết.

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Hello $name")
}
```

`@Composable` không đơn thuần là annotation trang trí. Compiler Compose plugin biến đổi function để runtime có thể theo dõi composition, state read và recomposition.

## 17.1 Layout cơ bản

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

`Row` xếp ngang, `Column` xếp dọc, `Box` chồng/position child, `LazyColumn` render danh sách lazy.

`Modifier` là chuỗi decorator-like để mô tả layout, input, semantics, drawing. Thứ tự modifier có thể thay đổi kết quả.

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

Vì modifier được áp dụng theo chain và mỗi node có thể wrap node tiếp theo.

# 18. XML/View system căn bản

Trước Compose, Android UI chủ yếu dùng XML layout với `View`/`ViewGroup`. Hệ thống này vẫn rất phổ biến trong codebase cũ.

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

Trong Activity cũ:

```kotlin
setContentView(R.layout.activity_main)
val title = findViewById<TextView>(R.id.titleText)
```

`findViewById` vẫn dùng được nhưng View Binding an toàn và dễ maintain hơn.

```kotlin
private lateinit var binding: ActivityMainBinding

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    binding = ActivityMainBinding.inflate(layoutInflater)
    setContentView(binding.root)
    binding.titleText.text = "Hello"
}
```

Kotlin Android Extensions synthetic view access (`kotlinx.android.synthetic`) là cách cũ và đã bị loại bỏ; không nên học như cách triển khai mới.

# 19. State, event và lifecycle nhập môn

Trong Compose, local state thường dùng `remember` và `mutableStateOf`.

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableIntStateOf(0) }

    Button(onClick = { count++ }) {
        Text("Count: $count")
    }
}
```

`remember` giữ giá trị qua recomposition, nhưng không tự sống qua Activity recreation. Nếu cần lưu UI state nhỏ qua configuration/process recreation có giới hạn, dùng `rememberSaveable` khi type có thể save.

State hoisting là đưa state lên caller để composable dễ test và reusable:

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

Android lifecycle kinh điển của Activity gồm `onCreate`, `onStart`, `onResume`, `onPause`, `onStop`, `onDestroy`. Không nên hiểu lifecycle như “mỗi lần đóng app chắc chắn sẽ gọi onDestroy”; process có thể bị OS kill mà không có callback cuối cùng theo cách bạn kỳ vọng.

# 20. Navigation nhập môn

Navigation Compose giúp định nghĩa destination và chuyển màn hình.

```kotlin
NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(...) }
    composable("detail/{id}") { backStackEntry ->
        val id = backStackEntry.arguments?.getString("id")
        DetailScreen(id)
    }
}
```

Ở project mới nên ưu tiên type-safe navigation API nếu version Navigation đang dùng hỗ trợ và codebase thống nhất. Route string vẫn rất phổ biến trong code cũ.

# 21. Resource, Manifest và permission

Resources nằm trong `res/`: `drawable`, `mipmap`, `values`, `font`, `xml`, `raw`... String nên đặt trong `res/values/strings.xml` để hỗ trợ localization.

```xml
<string name="welcome">Welcome</string>
```

AndroidManifest khai báo component, permission và app metadata.

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

Một số permission là normal và được grant tự động; dangerous permission còn cần runtime permission flow trên phiên bản Android phù hợp.

# 22. Debug, Logcat và lỗi thường gặp

Dùng breakpoint khi cần quan sát state chính xác; dùng Logcat khi cần trace lifecycle, network, event hoặc crash. Tránh log token/password/PII trong production.

```kotlin
Log.d("MainActivity", "onCreate")
Log.e("Network", "Request failed", throwable)
```

Lỗi Beginner thường gặp gồm: dùng `!!` để “cho compiler im”, hiểu sai `val` là immutable object, chạy network trên main thread, quên lifecycle, giữ Activity Context trong singleton, dùng list index không kiểm tra, hiểu `0..size` thay vì `0 until size`, mutation state Compose không observable, và nhét toàn bộ logic vào Activity/Composable.

# 23. Mini project tổng hợp: Todo đơn giản

Mục tiêu mini project là tạo app Todo với một màn hình nhập task và danh sách task. Phiên bản Beginner chưa cần database; dùng state trong memory.

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

Điểm cần hiểu không phải chỉ là code chạy được. `input` là state local; `items = items + text` tạo list mới nên `mutableStateOf` nhận reference mới và Compose dễ thấy thay đổi; UI chỉ là function của state; callback `onClick` là event đưa hệ thống từ state cũ sang state mới.

Ở Intermediate, project này sẽ được nâng cấp thành ViewModel + StateFlow + Room + Navigation + repository.

# 24. Checklist Beginner

Sau level này, bạn nên tự giải thích được sự khác nhau giữa Kotlin language, Android SDK và Jetpack; hiểu Gradle module/dependency cơ bản; dùng `val`, `var`, nullable type, safe call, Elvis, `when`, loop, function, class, inheritance, interface, data class, sealed class và collection; viết lambda; hiểu Activity/Context/Intent; tạo Compose UI; hiểu state/recomposition ở mức cơ bản; đọc được XML/View Binding code; hiểu resource/manifest/permission; chạy debugger và đọc Logcat.

Nếu còn thấy `?.`, `?:`, `let`, lambda, `@Composable`, `remember`, `Modifier`, `Context`, `Intent`, `ViewModel` là những từ “ma thuật” chưa giải thích được bằng lời của mình, chưa nên chuyển nhanh sang các architecture phức tạp.

---

## Version & Legacy Notes

Kotlin hiện đại sử dụng K2 compiler line và Kotlin 2.x. Code Kotlin 1.x phần lớn vẫn đọc được, nhưng plugin/compiler/build configuration có khác biệt. Với Android UI, Compose là hướng hiện đại, còn XML/View system vẫn rất quan trọng trong codebase hiện hữu. `kotlinx.android.synthetic` là legacy đã bị loại bỏ; `AsyncTask` là deprecated từ lâu; `startActivityForResult`/`onActivityResult` đã được thay thế bằng Activity Result APIs trong code mới. Các phần này sẽ được giải thích sâu hơn ở level sau.

---

# 25. Các modifier và cấu trúc Kotlin thường gặp nhưng dễ bỏ sót

Sau khi đã hiểu class, function và property, cần làm quen với nhóm **modifier** vì chúng xuất hiện dày đặc trong code Android thực tế. `public` là mặc định; `private` giới hạn trong class/file tương ứng; `protected` dành cho class con; `internal` giới hạn theo Kotlin module. `internal` rất hữu ích khi xây module Android vì nó cho phép implementation được chia sẻ bên trong module nhưng không trở thành public API cho module khác.

```kotlin
internal class TokenParser {
    private fun normalize(raw: String): String = raw.trim()
}
```

`const val` khác `val` thông thường ở chỗ nó là compile-time constant và chỉ dùng được cho primitive/String ở top-level, object hoặc companion object. Nó phù hợp cho constant thực sự như key cố định, nhưng không dùng cho giá trị phải tính lúc runtime.

```kotlin
const val API_VERSION = "v1"
```

`lateinit var` cho phép trì hoãn khởi tạo một non-null mutable property. Nó thường xuất hiện trong Android View Binding hoặc test setup cũ, nhưng nếu đọc trước khi được gán sẽ ném `UninitializedPropertyAccessException`. Vì vậy `lateinit` không phải null-safety “miễn phí”; nó chỉ chuyển invariant từ compile time sang runtime.

```kotlin
private lateinit var binding: ActivityMainBinding
```

`lazy` thì khác: nó thường đi cùng `val` và tính giá trị ở lần truy cập đầu tiên. Đây là lazy initialization chứ không phải “biến chưa khởi tạo”.

```kotlin
val database by lazy { createDatabase() }
```

Kotlin còn hỗ trợ destructuring qua `componentN()`; data class tự sinh các component tương ứng. Cú pháp này tiện khi pair hoặc object nhỏ, nhưng nếu destructure quá nhiều field thì code khó hiểu hơn gọi tên property trực tiếp.

```kotlin
val (name, age) = User("An", 28)
```

# 26. Android Studio workflow: từ source code đến APK/AAB

Khi bấm **Run**, Android Studio không “chạy file Kotlin trực tiếp”. IDE gọi Gradle; Android Gradle Plugin chọn build variant, compile Kotlin/Java, xử lý resource và manifest, tạo DEX, đóng gói artifact, ký bản debug rồi cài lên emulator hoặc thiết bị. Hiểu pipeline này giúp phân biệt lỗi compiler, lỗi resource, lỗi manifest merge, lỗi dependency và lỗi runtime.

Các thao tác thường dùng trong Android Studio gồm **Sync Project with Gradle Files** khi build script hoặc dependency thay đổi; **Build > Make Project** để compile; **Run** để build và deploy; **Debug** để attach debugger; **Logcat** để xem log runtime; **App Inspection** cho database/network tùy tooling; **Profiler** và **Layout Inspector** để điều tra performance/UI. `Clean Project` không nên trở thành phản xạ mỗi khi lỗi vì nó xóa cache build hữu ích; trước tiên cần đọc lỗi và xác định task nào thất bại.

Trong Gradle, `debug` và `release` là hai build type quen thuộc. Bản debug thường debuggable và dùng debug signing key; bản release thường bật optimization/shrinking theo cấu hình và phải dùng signing key phù hợp để phát hành. APK là package cài đặt trực tiếp; Android App Bundle (`.aab`) là format phát hành lên Google Play để Play tạo APK tối ưu cho từng thiết bị.

# 27. Activity Result API và runtime permission theo cách hiện đại

Code Android cũ thường dùng `startActivityForResult()` và `onActivityResult()`. Cách hiện đại là đăng ký **Activity Result Contract**. Điểm quan trọng không chỉ là syntax mới; contract giúp tách kiểu input/output và tích hợp lifecycle tốt hơn.

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

Runtime permission cũng dùng contract tương tự. Không được yêu cầu permission chỉ vì manifest đã khai báo. Với permission thuộc nhóm runtime, ứng dụng phải kiểm tra trạng thái, giải thích khi cần, request, rồi xử lý cả trường hợp người dùng từ chối.

```kotlin
private val requestCamera = registerForActivityResult(
    ActivityResultContracts.RequestPermission()
) { granted ->
    if (granted) openCamera()
}
```

Permission behavior thay đổi theo Android version. Vì thế code production cần kiểm tra API level và tài liệu platform thay vì copy một snippet cũ rồi giả định nó đúng trên mọi phiên bản.

# 28. Resource qualifier, configuration và vì sao không hard-code UI

Android resource system tồn tại để một logical resource có thể có nhiều biến thể. Ví dụ `values/strings.xml` chứa string mặc định, `values-ko/` có tiếng Hàn, `values-vi/` có tiếng Việt; drawable/layout có thể có biến thể theo density, orientation, screen size hoặc night mode. Framework chọn resource phù hợp với configuration thiết bị.

Do đó text hiển thị cho người dùng không nên hard-code trong Kotlin nếu cần localization. Kích thước UI không nên suy nghĩ theo pixel thuần túy; Android dùng `dp` cho kích thước layout và `sp` cho text để tôn trọng density và font scale. Trong Compose, các abstraction như `dp`, `sp`, `stringResource()` và theme tiếp tục phản ánh cùng triết lý resource/configuration này.

Configuration change có thể recreate Activity. Nếu state chỉ nằm trong field của Activity, nó có thể biến mất. State UI ngắn hạn có thể dùng `rememberSaveable`; state logic thường thuộc ViewModel; dữ liệu cần sống qua process death phải có cơ chế saved state hoặc persistence phù hợp. Đây là nền tảng để hiểu sâu hơn ở Intermediate và Senior.

# 29. Bản đồ tư duy sau Beginner

Sau level này, một flow Android cơ bản nên được hình dung như sau: Gradle build project; Android system tạo component theo manifest/intent; Activity hoặc Fragment sở hữu lifecycle; UI có thể là Compose hoặc View; UI đọc state và phát event; Kotlin cung cấp type system và logic; resource system cung cấp text/image/configuration; permission và platform API tạo boundary với hệ điều hành. Khi debug, hãy xác định lỗi nằm ở build time, component lifecycle, state, resource, permission hay business logic trước khi sửa code.
