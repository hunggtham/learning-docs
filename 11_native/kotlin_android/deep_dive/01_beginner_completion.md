# Kotlin + Android Beginner — Completion Deep Dive

> File này bổ sung cho [`../01_kotlin_beginner.md`](../01_kotlin_beginner.md). Mục tiêu là lấp các khoảng trống thường khiến người mới đọc project thật phải tra cứu thêm: package/import, equality, number conversion, range/array, collection transformation, nested/inner class, precondition, object identity, Context/Intent/Uri, Compose layout và testing căn bản.

# 1. Package, import, file và naming convention

Một file Kotlin thường bắt đầu bằng `package`, sau đó là các `import`. Package không chỉ là cách “xếp folder”; trên JVM nó là một phần của fully-qualified name và ảnh hưởng cách class/function được tham chiếu. Android project thường tổ chức package theo feature hoặc layer, nhưng package name không bắt buộc phải trùng tuyệt đối với đường dẫn folder. Dù compiler cho phép, giữ chúng tương ứng giúp IDE navigation và việc đọc code dễ hơn.

```kotlin
package com.example.notes.feature.editor

import androidx.compose.runtime.Composable
import com.example.notes.domain.Note
```

Kotlin hỗ trợ top-level function/property, vì vậy không cần tạo class `Utils` chỉ để chứa helper. Nếu hai import trùng tên, có thể dùng alias.

```kotlin
import java.time.Duration as JavaDuration
import kotlin.time.Duration as KotlinDuration
```

Naming convention phổ biến là `PascalCase` cho class/interface/object, `camelCase` cho function/property/local variable, và constant compile-time dùng `UPPER_SNAKE_CASE`. Tên tốt nên mô tả ý nghĩa nghiệp vụ hơn là implementation. `userRepository` tốt hơn `repo1`; `loadActiveOrders()` tốt hơn `getData()`.

# 2. Number conversion, equality, range, progression và Array

Kotlin không tự động mở rộng kiểu số theo mọi tình huống như một số ngôn ngữ khác. Khi cần chuyển kiểu, dùng conversion rõ ràng như `toLong()`, `toDouble()`. Điều này tránh nhiều implicit conversion khó đoán.

```kotlin
val count: Int = 10
val total: Long = count.toLong()
```

Hai toán tử equality rất dễ nhầm. `==` gọi structural equality, về bản chất tương đương kiểm tra `equals`; `===` kiểm tra hai reference có trỏ cùng object hay không. Trong business code, `==` là thứ cần dùng phần lớn thời gian.

```kotlin
data class User(val id: Long)

val a = User(1)
val b = User(1)
println(a == b)   // true
println(a === b)  // false
```

Range và progression xuất hiện thường xuyên trong loop và validation. `1..5` gồm cả 5; `1 until 5` không gồm 5; `5 downTo 1` đi giảm; `step` thay bước nhảy.

```kotlin
for (i in 0 until items.size) { }
for (i in 10 downTo 0 step 2) { }
```

Tuy nhiên khi duyệt collection, ưu tiên `for (item in items)` nếu không thật sự cần index. Khi cần cả index và value, `withIndex()` thường rõ hơn truy cập `items[i]`.

`Array<T>` là container có kích thước cố định sau khi tạo; phần tử bên trong vẫn có thể thay đổi. Với primitive có các type chuyên biệt như `IntArray`, `LongArray`, `ByteArray` để tránh boxing không cần thiết.

```kotlin
val names = arrayOf("A", "B", "C")
val scores = IntArray(3) { index -> index * 10 }
```

# 3. Collection operations cần nắm trước khi sang Intermediate

Kotlin Standard Library mạnh ở việc biến đổi collection. Cần hiểu ý nghĩa dữ liệu của từng operator thay vì học thuộc tên. `map` biến mỗi phần tử thành một phần tử mới; `filter` giữ phần tử thỏa điều kiện; `mapNotNull` vừa transform vừa loại kết quả null; `associateBy` tạo map theo key; `groupBy` gom nhiều phần tử cùng key; `zip` ghép hai sequence theo vị trí; `fold` tích lũy từ initial value.

```kotlin
val users = listOf(
    UserDto(1, "An"),
    UserDto(2, null),
    UserDto(3, "Binh")
)

val names = users.mapNotNull { it.name }
val byId = users.associateBy { it.id }
val byHasName = users.groupBy { it.name != null }
```

`map` không sửa list gốc; nó tạo collection mới. `MutableList` mới cho phép mutation tại chỗ. Khi state được quan sát bởi Compose hoặc Flow, tạo value mới thường dễ suy luận hơn mutation âm thầm.

`fold` đặc biệt quan trọng vì nhiều operation có thể nhìn như một dạng accumulation.

```kotlin
val total = listOf(10, 20, 30).fold(0) { acc, value ->
    acc + value
}
```

Không nên biến mọi logic thành chain dài hàng chục operator. Nếu chain cần nhiều comment để giải thích, tách thành named function hoặc dùng loop rõ ràng có thể tốt hơn.

# 4. Nested class, inner class, object expression và typealias

Class khai báo bên trong class khác mặc định là **nested class** và không giữ reference tới instance bên ngoài. Chỉ khi thêm `inner`, instance bên trong mới có thể truy cập member của outer object.

```kotlin
class Screen {
    private val title = "Home"

    inner class Listener {
        fun printTitle() = println(title)
    }
}
```

`inner` tạo coupling và giữ reference tới outer object, vì vậy trên Android cần cẩn thận với lifecycle. Một callback sống lâu hơn Activity nhưng giữ `inner` reference tới Activity có thể góp phần gây memory leak.

Object expression tạo anonymous object, tương tự anonymous class nhưng gọn hơn.

```kotlin
val listener = object : View.OnClickListener {
    override fun onClick(v: View?) {
        println("clicked")
    }
}
```

`typealias` chỉ tạo tên thay thế ở source level, không tạo type mới. Nó hữu ích khi function type dài hoặc generic type khó đọc.

```kotlin
typealias UserClick = (User) -> Unit
```

Nếu cần domain type thực sự khác biệt để compiler ngăn trộn lẫn dữ liệu, `value class` ở level Master phù hợp hơn `typealias`.

# 5. Preconditions: `require`, `check`, `error`, `TODO`

Không phải mọi lỗi đều nên biểu diễn bằng nullable. Nếu caller vi phạm điều kiện đầu vào, `require` giúp encode precondition. Nếu state nội bộ của object không hợp lệ, `check` diễn đạt invariant. `error` luôn ném `IllegalStateException`; `TODO` hữu ích trong code đang phát triển nhưng không nên lọt vào production path.

```kotlin
fun setAge(age: Int) {
    require(age >= 0) { "age must be non-negative" }
}

fun submit() {
    check(items.isNotEmpty()) { "cannot submit empty order" }
}
```

Precondition tốt làm contract rõ hơn, nhưng đừng dùng exception như control flow cho tình huống nghiệp vụ bình thường. Ví dụ “username đã tồn tại” là domain result có thể dự kiến, không nên được mô hình như bug invariant.

# 6. Data class sâu hơn: equality, `copy`, hashCode và shallow copy

Data class tự sinh `equals`, `hashCode`, `toString`, `componentN` và `copy` dựa trên property nằm trong primary constructor. Điều này khiến data class rất phù hợp cho immutable state và model dữ liệu.

```kotlin
data class Profile(
    val name: String,
    val tags: List<String>
)

val old = Profile("An", listOf("android"))
val updated = old.copy(name = "Binh")
```

`copy` là **shallow copy**. Nếu một property chứa mutable object, object con vẫn có thể được chia sẻ giữa bản cũ và bản mới. Vì vậy immutable collection/value giúp state dễ reasoning hơn.

Hash-based collection như `HashSet`/`HashMap` phụ thuộc `equals` và `hashCode`. Tránh dùng mutable property tham gia equality làm key rồi thay đổi nó sau khi object đã được đưa vào hash map/set, vì lookup có thể trở nên sai.

# 7. `Context`, `Application`, `Activity` và lifetime

`Context` là gateway tới tài nguyên và dịch vụ Android, nhưng các subclass có lifetime khác nhau. `Application` context sống gần bằng process; `Activity` context gắn với màn hình và theme. Một object singleton giữ Activity context có thể giữ cả Activity sau khi màn hình bị destroy và gây leak.

Khi API cần tạo UI/dialog hoặc dùng theme của màn hình, Activity context thường đúng. Khi dependency sống lâu như database singleton chỉ cần application service/resource không phụ thuộc theme, application context phù hợp hơn.

Không nên “fix leak” bằng cách thay mọi context thành `applicationContext`. Context đúng phải xuất phát từ lifetime và capability cần dùng.

# 8. Intent, Bundle, Uri và boundary dữ liệu giữa Android component

`Intent` mô tả hành động cần thực hiện. Explicit intent chỉ rõ component đích; implicit intent mô tả action/data để system tìm component phù hợp. Dữ liệu nhỏ có thể đi qua extras/Bundle, nhưng không nên truyền object graph lớn qua Binder transaction.

```kotlin
val intent = Intent(context, DetailActivity::class.java)
    .putExtra("note_id", noteId)
startActivity(intent)
```

`Uri` là kiểu quan trọng khi làm việc với file picker, content provider, deep link và web URL. Không nên giả định `Uri` luôn là file path. `content://` có thể đại diện dữ liệu qua `ContentResolver`; quyền truy cập có thể tạm thời theo grant của system.

# 9. Compose layout và `Modifier`: thứ tự modifier có ý nghĩa

`Modifier` không phải “bag option” không có thứ tự. Mỗi modifier wrap hoặc transform node theo thứ tự chain, vì vậy `padding().background()` có thể khác `background().padding()` về vùng được tô và hit target.

```kotlin
Text(
    text = "Save",
    modifier = Modifier
        .padding(16.dp)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { onSave() }
        .padding(12.dp)
)
```

Trong layout, `Row`, `Column`, `Box`, `LazyColumn` là primitive quan trọng. Compose đo child theo constraint từ parent, child trả size rồi parent đặt vị trí. Khi layout “bí ẩn”, hãy nghĩ theo constraint/measurement thay vì chỉ thử thêm modifier ngẫu nhiên.

# 10. Test căn bản: local unit test và instrumented test

Android project thường có `src/test` cho local JVM test và `src/androidTest` cho test cần Android runtime/device/emulator. Logic Kotlin thuần nên được tách đủ tốt để test nhanh ở JVM. Instrumented test dành cho integration với Android framework, UI, database thực hoặc behavior chỉ tồn tại trên thiết bị.

```kotlin
class PriceCalculatorTest {
    @Test
    fun total_is_sum_of_items() {
        val result = PriceCalculator().total(listOf(10, 20))
        assertEquals(30, result)
    }
}
```

Đừng đợi đến Intermediate mới nghĩ về testability. Ngay từ Beginner, function thuần nhận input và trả output đã dễ test hơn function tự đọc global state, gọi network và sửa UI cùng lúc.

# 11. Checklist hoàn thiện Beginner

Sau phần này, bạn nên giải thích được package/import, structural/reference equality, range/array, các collection operator phổ biến, nested/inner class, object expression, `typealias`, precondition, data class equality/copy, sự khác nhau giữa Activity/Application context, Intent/Bundle/Uri và local/instrumented test. Khi các khái niệm này đã rõ, việc chuyển sang coroutine, Flow và architecture ở Intermediate sẽ ít tạo cảm giác “framework magic” hơn.
