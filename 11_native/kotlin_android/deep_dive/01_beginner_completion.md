# Kotlin + Android Beginner — Completion Deep Dive

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Kotlin + Android Beginner — Completion Deep Dive**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. Bắt đầu ở **Kotlin + Android Beginner — Completion Deep Dive** để mở đối tượng chính của file và câu hỏi cần theo dõi, rồi dùng kết luận đó khi quay về lộ trình rộng hơn.

> tệp (file / 파일) này bổ sung cho [`../01_kotlin_beginner.md`](../01_kotlin_beginner.md). Mục tiêu là lấp các khoảng trống thường khiến người mới đọc dự án (project / 프로젝트) thật phải tra cứu thêm: gói (package / 패키지)/import, equality, number conversion, phạm vi (range / 범위)/array, collection transformation, nested/inner lớp (class / 클래스), precondition, đối tượng (object / 객체) định danh (identity / 식별자), ngữ cảnh (context / 맥락)/Intent/Uri, Compose bố cục (layout / 레이아웃) và testing căn bản.

# 1. gói (package / 패키지), import, tệp (file / 파일) và naming convention

Một tệp (file / 파일) Kotlin thường bắt đầu bằng `package`, sau đó là các `import`. gói (package / 패키지) không chỉ là cách “xếp folder”; trên JVM nó là một phần của fully-qualified name và ảnh hưởng cách lớp (class / 클래스)/hàm (function / 함수) được tham chiếu. Android dự án (project / 프로젝트) thường tổ chức gói (package / 패키지) theo tính năng (feature / 기능) hoặc tầng (layer / 계층), nhưng gói (package / 패키지) name không bắt buộc phải trùng tuyệt đối với đường dẫn folder. Dù trình biên dịch (compiler / 컴파일러) cho phép, giữ chúng tương ứng giúp IDE điều hướng (navigation / 내비게이션) và việc đọc mã (code / 코드) dễ hơn.

```kotlin
package com.example.notes.feature.editor

import androidx.compose.runtime.Composable
import com.example.notes.domain.Note
```

Kotlin hỗ trợ top-level hàm (function / 함수)/thuộc tính (property / 속성), vì vậy không cần tạo lớp (class / 클래스) `Utils` chỉ để chứa helper. Nếu hai import trùng tên, có thể dùng alias.

```kotlin
import java.time.Duration as JavaDuration
import kotlin.time.Duration as KotlinDuration
```

Naming convention phổ biến là `PascalCase` cho lớp (class / 클래스)/giao diện (interface / 인터페이스)/đối tượng (object / 객체), `camelCase` cho hàm (function / 함수)/thuộc tính (property / 속성)/cục bộ (local / 로컬) variable, và constant compile-time dùng `UPPER_SNAKE_CASE`. Tên tốt nên mô tả ý nghĩa nghiệp vụ hơn là hiện thực (implementation / 구현). `userRepository` tốt hơn `repo1`; `loadActiveOrders()` tốt hơn `getData()`.

# 2. Number conversion, equality, phạm vi (range / 범위), progression và Array

Kotlin không tự động mở rộng kiểu số theo mọi tình huống như một số ngôn ngữ khác. Khi cần chuyển kiểu, dùng conversion rõ ràng như `toLong()`, `toDouble()`. Điều này tránh nhiều implicit conversion khó đoán.

```kotlin
val count: Int = 10
val total: Long = count.toLong()
```

Hai toán tử equality rất dễ nhầm. `==` gọi structural equality, về bản chất tương đương kiểm tra `equals`; `===` kiểm tra hai tham chiếu (reference / 참조) có trỏ cùng đối tượng (object / 객체) hay không. Trong nghiệp vụ (business / 비즈니스) mã (code / 코드), `==` là thứ cần dùng phần lớn thời gian.

```kotlin
data class User(val id: Long)

val a = User(1)
val b = User(1)
println(a == b)   // true
println(a === b)  // false
```

Phạm vi (range / 범위) và progression xuất hiện thường xuyên trong vòng lặp (loop / 루프) và kiểm tra hợp lệ (validation / 검증). `1..5` gồm cả 5; `1 until 5` không gồm 5; `5 downTo 1` đi giảm; `step` thay bước nhảy.

```kotlin
for (i in 0 until items.size) { }
for (i in 10 downTo 0 step 2) { }
```

Tuy nhiên khi duyệt collection, ưu tiên `for (item in items)` nếu không thật sự cần chỉ mục (index / 인덱스). Khi cần cả chỉ mục (index / 인덱스) và giá trị (value / 값), `withIndex()` thường rõ hơn truy cập `items[i]`.

`Array<T>` là bộ chứa (container / 컨테이너) có kích thước cố định sau khi tạo; phần tử bên trong vẫn có thể thay đổi. Với thành phần nguyên thủy (primitive / 기본 요소) có các kiểu (type / 타입) chuyên biệt như `IntArray`, `LongArray`, `ByteArray` để tránh boxing không cần thiết.

```kotlin
val names = arrayOf("A", "B", "C")
val scores = IntArray(3) { index -> index * 10 }
```

# 3. Collection operations cần nắm trước khi sang Intermediate

Kotlin thư viện chuẩn (standard library / 표준 라이브러리) mạnh ở việc biến đổi collection. Cần hiểu ý nghĩa dữ liệu của từng operator thay vì học thuộc tên. `map` biến mỗi phần tử thành một phần tử mới; `filter` giữ phần tử thỏa điều kiện; `mapNotNull` vừa transform vừa loại kết quả null; `associateBy` tạo map theo key; `groupBy` gom nhiều phần tử cùng key; `zip` ghép hai chuỗi (sequence / 시퀀스) theo vị trí; `fold` tích lũy từ initial giá trị (value / 값).

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

`map` không sửa danh sách (list / 목록) gốc; nó tạo collection mới. `MutableList` mới cho phép mutation tại chỗ. Khi trạng thái (state / 상태) được quan sát bởi Compose hoặc luồng (flow / 흐름), tạo giá trị (value / 값) mới thường dễ suy luận hơn mutation âm thầm.

`fold` đặc biệt quan trọng vì nhiều thao tác (operation / 연산) có thể nhìn như một dạng accumulation.

```kotlin
val total = listOf(10, 20, 30).fold(0) { acc, value ->
    acc + value
}
```

Không nên biến mọi lô-gic (logic / 논리) thành chuỗi (chain / 사슬) dài hàng chục operator. Nếu chuỗi (chain / 사슬) cần nhiều comment để giải thích, tách thành named hàm (function / 함수) hoặc dùng vòng lặp (loop / 루프) rõ ràng có thể tốt hơn.

# 4. Nested lớp (class / 클래스), inner lớp (class / 클래스), đối tượng (object / 객체) expression và typealias

Lớp (class / 클래스) khai báo bên trong lớp (class / 클래스) khác mặc định là **nested lớp (class / 클래스)** và không giữ tham chiếu (reference / 참조) tới instance bên ngoài. Chỉ khi thêm `inner`, instance bên trong mới có thể truy cập member của outer đối tượng (object / 객체).

```kotlin
class Screen {
    private val title = "Home"

    inner class Listener {
        fun printTitle() = println(title)
    }
}
```

`inner` tạo coupling và giữ tham chiếu (reference / 참조) tới outer đối tượng (object / 객체), vì vậy trên Android cần cẩn thận với vòng đời (lifecycle / 생명주기). Một callback sống lâu hơn Activity nhưng giữ `inner` tham chiếu (reference / 참조) tới Activity có thể góp phần gây bộ nhớ (memory / 메모리) leak.

Đối tượng (object / 객체) expression tạo anonymous đối tượng (object / 객체), tương tự anonymous lớp (class / 클래스) nhưng gọn hơn.

```kotlin
val listener = object : View.OnClickListener {
    override fun onClick(v: View?) {
        println("clicked")
    }
}
```

`typealias` chỉ tạo tên thay thế ở nguồn (source / 소스) mức (level / 수준), không tạo kiểu (type / 타입) mới. Nó hữu ích khi hàm (function / 함수) kiểu (type / 타입) dài hoặc generic kiểu (type / 타입) khó đọc.

```kotlin
typealias UserClick = (User) -> Unit
```

Nếu cần lĩnh vực (domain / 도메인) kiểu (type / 타입) thực sự khác biệt để trình biên dịch (compiler / 컴파일러) ngăn trộn lẫn dữ liệu, `value class` ở mức (level / 수준) Master phù hợp hơn `typealias`.

# 5. Preconditions: `require`, `check`, `error`, `TODO`

Không phải mọi lỗi đều nên biểu diễn bằng nullable. Nếu caller vi phạm điều kiện đầu vào, `require` giúp encode precondition. Nếu trạng thái (state / 상태) nội bộ của đối tượng (object / 객체) không hợp lệ, `check` diễn đạt bất biến (invariant / 불변식). `error` luôn ném `IllegalStateException`; `TODO` hữu ích trong mã (code / 코드) đang phát triển nhưng không nên lọt vào môi trường vận hành (production / 운영 환경) đường dẫn (path / 경로).

```kotlin
fun setAge(age: Int) {
    require(age >= 0) { "age must be non-negative" }
}

fun submit() {
    check(items.isNotEmpty()) { "cannot submit empty order" }
}
```

Precondition tốt làm đặc tả hợp đồng (contract / 계약) rõ hơn, nhưng đừng dùng exception như điều khiển (control / 제어) luồng (flow / 흐름) cho tình huống nghiệp vụ bình thường. Ví dụ “username đã tồn tại” là lĩnh vực (domain / 도메인) kết quả (result / 결과) có thể dự kiến, không nên được mô hình như bug bất biến (invariant / 불변식).

# 6. dữ liệu (data / 데이터) lớp (class / 클래스) sâu hơn: equality, `copy`, hashCode và shallow bản sao (copy / 복사)

Dữ liệu (data / 데이터) lớp (class / 클래스) tự sinh `equals`, `hashCode`, `toString`, `componentN` và `copy` dựa trên thuộc tính (property / 속성) nằm trong primary constructor. Điều này khiến dữ liệu (data / 데이터) lớp (class / 클래스) rất phù hợp cho immutable trạng thái (state / 상태) và mô hình (model / 모델) dữ liệu.

```kotlin
data class Profile(
    val name: String,
    val tags: List<String>
)

val old = Profile("An", listOf("android"))
val updated = old.copy(name = "Binh")
```

`copy` là **shallow bản sao (copy / 복사)**. Nếu một thuộc tính (property / 속성) chứa mutable đối tượng (object / 객체), đối tượng (object / 객체) con vẫn có thể được chia sẻ giữa bản cũ và bản mới. Vì vậy immutable collection/giá trị (value / 값) giúp trạng thái (state / 상태) dễ lập luận (reasoning / 추론) hơn.

Hash-based collection như `HashSet`/`HashMap` phụ thuộc `equals` và `hashCode`. Tránh dùng mutable thuộc tính (property / 속성) tham gia equality làm key rồi thay đổi nó sau khi đối tượng (object / 객체) đã được đưa vào băm (hash / 해시) map/set, vì lookup có thể trở nên sai.

# 7. `Context`, `Application`, `Activity` và thời gian tồn tại (lifetime / 수명)

`Context` là gateway tới tài nguyên và dịch vụ Android, nhưng các subclass có thời gian tồn tại (lifetime / 수명) khác nhau. `Application` ngữ cảnh (context / 맥락) sống gần bằng tiến trình (process / 프로세스); `Activity` ngữ cảnh (context / 맥락) gắn với màn hình và theme. Một đối tượng (object / 객체) singleton giữ Activity ngữ cảnh (context / 맥락) có thể giữ cả Activity sau khi màn hình bị destroy và gây leak.

Khi API cần tạo UI/dialog hoặc dùng theme của màn hình, Activity ngữ cảnh (context / 맥락) thường đúng. Khi phụ thuộc (dependency / 의존성) sống lâu như cơ sở dữ liệu (database / 데이터베이스) singleton chỉ cần ứng dụng (application / 애플리케이션) dịch vụ (service / 서비스)/tài nguyên (resource / 자원) không phụ thuộc theme, ứng dụng (application / 애플리케이션) ngữ cảnh (context / 맥락) phù hợp hơn.

Không nên “fix leak” bằng cách thay mọi ngữ cảnh (context / 맥락) thành `applicationContext`. ngữ cảnh (context / 맥락) đúng phải xuất phát từ thời gian tồn tại (lifetime / 수명) và năng lực (capability / 역량) cần dùng.

# 8. Intent, Bundle, Uri và ranh giới (boundary / 경계) dữ liệu giữa Android thành phần (component / 컴포넌트)

`Intent` mô tả hành động cần thực hiện. tường minh (explicit / 명시적) intent chỉ rõ thành phần (component / 컴포넌트) đích; implicit intent mô tả hành động (action / 동작)/dữ liệu (data / 데이터) để hệ thống (system / 시스템) tìm thành phần (component / 컴포넌트) phù hợp. Dữ liệu nhỏ có thể đi qua extras/Bundle, nhưng không nên truyền đối tượng (object / 객체) đồ thị (graph / 그래프) lớn qua Binder giao dịch (transaction / 트랜잭션).

```kotlin
val intent = Intent(context, DetailActivity::class.java)
    .putExtra("note_id", noteId)
startActivity(intent)
```

`Uri` là kiểu quan trọng khi làm việc với tệp (file / 파일) picker, content provider, deep link và web URL. Không nên giả định `Uri` luôn là tệp (file / 파일) đường dẫn (path / 경로). `content://` có thể đại diện dữ liệu qua `ContentResolver`; quyền truy cập có thể tạm thời theo grant của hệ thống (system / 시스템).

# 9. Compose bố cục (layout / 레이아웃) và `Modifier`: thứ tự modifier có ý nghĩa

`Modifier` không phải “bag option” không có thứ tự. Mỗi modifier wrap hoặc transform nút (node / 노드) theo thứ tự chuỗi (chain / 사슬), vì vậy `padding().background()` có thể khác `background().padding()` về vùng được tô và hit mục tiêu (target / 대상).

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

Trong bố cục (layout / 레이아웃), `Row`, `Column`, `Box`, `LazyColumn` là thành phần nguyên thủy (primitive / 기본 요소) quan trọng. Compose đo child theo ràng buộc (constraint / 제약조건) từ parent, child trả kích thước (size / 크기) rồi parent đặt vị trí. Khi bố cục (layout / 레이아웃) “bí ẩn”, hãy nghĩ theo ràng buộc (constraint / 제약조건)/đo lường (measurement / 측정) thay vì chỉ thử thêm modifier ngẫu nhiên.

# 10. kiểm thử (test / 테스트) căn bản: cục bộ (local / 로컬) đơn vị (unit / 단위) kiểm thử (test / 테스트) và instrumented kiểm thử (test / 테스트)

Android dự án (project / 프로젝트) thường có `src/test` cho cục bộ (local / 로컬) JVM kiểm thử (test / 테스트) và `src/androidTest` cho kiểm thử (test / 테스트) cần Android thời gian chạy (runtime / 런타임)/thiết bị (device / 장치)/emulator. lô-gic (logic / 논리) Kotlin thuần nên được tách đủ tốt để kiểm thử (test / 테스트) nhanh ở JVM. Instrumented kiểm thử (test / 테스트) dành cho tích hợp (integration / 통합) với Android khung phần mềm (framework / 프레임워크), UI, cơ sở dữ liệu (database / 데이터베이스) thực hoặc hành vi (behavior / 동작) chỉ tồn tại trên thiết bị.

```kotlin
class PriceCalculatorTest {
    @Test
    fun total_is_sum_of_items() {
        val result = PriceCalculator().total(listOf(10, 20))
        assertEquals(30, result)
    }
}
```

Đừng đợi đến Intermediate mới nghĩ về testability. Ngay từ Beginner, hàm (function / 함수) thuần nhận đầu vào (input / 입력) và trả đầu ra (output / 출력) đã dễ kiểm thử (test / 테스트) hơn hàm (function / 함수) tự đọc toàn cục (global / 전역) trạng thái (state / 상태), gọi mạng (network / 네트워크) và sửa UI cùng lúc.

# 11. Checklist hoàn thiện Beginner

Sau phần này, bạn nên giải thích được gói (package / 패키지)/import, structural/tham chiếu (reference / 참조) equality, phạm vi (range / 범위)/array, các collection operator phổ biến, nested/inner lớp (class / 클래스), đối tượng (object / 객체) expression, `typealias`, precondition, dữ liệu (data / 데이터) lớp (class / 클래스) equality/bản sao (copy / 복사), sự khác nhau giữa Activity/ứng dụng (application / 애플리케이션) ngữ cảnh (context / 맥락), Intent/Bundle/Uri và cục bộ (local / 로컬)/instrumented kiểm thử (test / 테스트). Khi các khái niệm này đã rõ, việc chuyển sang coroutine, luồng (flow / 흐름) và kiến trúc (architecture / 아키텍처) ở Intermediate sẽ ít tạo cảm giác “phép màu của khung phần mềm (framework magic / 프레임워크 마법)” hơn.

> **Bàn giao:** Sau **Kotlin + Android Beginner — Completion Deep Dive**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
