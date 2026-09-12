# Java Core — Part 1: Beginner — Rewritten Detailed
## Học Java từ số 0 theo cách hiểu bản chất, không học thuộc cú pháp

> Đây là Part 1 trong lộ trình **Beginner → Intermediate → Senior → Master Supplement**. Tài liệu này được viết cho người mới học Java hoặc đã từng dùng Java nhưng chưa có mental model chắc chắn. Mỗi chủ đề được giải thích theo hướng: vấn đề đang tồn tại là gì, Java giải quyết nó bằng cơ chế nào, cú pháp thể hiện cơ chế đó ra sao, ví dụ thực tế nên viết như thế nào, và vì sao một số cách viết tuy chạy được nhưng không nên trở thành thói quen.
>
> Các “Senior Note”, “Language Idiom”, “Programming Pattern” và “Design Pattern” không được tách thành checklist riêng sau mỗi mục. Khi một pattern thực sự quan trọng, nó sẽ được giải thích ngay trong nội dung để bạn hiểu nó như một phần tự nhiên của Java chứ không phải một danh sách thuật ngữ cần học thuộc.

---

# 1. Trước khi viết code: Java thực sự chạy như thế nào?

Khi bạn viết một file `Hello.java`, CPU không hiểu trực tiếp source code Java. Source code trước hết được compiler `javac` biên dịch thành **bytecode** nằm trong file `.class`. Bytecode không gắn chặt với một loại CPU cụ thể như x86 hay ARM. Nó là instruction format dành cho JVM, tức Java Virtual Machine. Khi application chạy, JVM load các class, verify bytecode, quản lý memory, thực thi bytecode bằng interpreter và có thể compile những đoạn code nóng thành native machine code bằng JIT compiler.

Có thể hình dung flow đơn giản như sau:

```text
Hello.java
    ↓ javac
Hello.class
    ↓ JVM
bytecode được load / verify / execute
    ↓
native instructions trên máy thật
```

Đây là nguyên nhân Java nổi tiếng với ý tưởng “write once, run anywhere”. Thực tế chính xác hơn là cùng bytecode có thể chạy trên nhiều platform miễn platform đó có JVM tương thích. Bạn vẫn có thể gặp khác biệt về filesystem, timezone, charset, native library hoặc OS behavior, vì vậy portable không có nghĩa mọi môi trường hoàn toàn giống nhau.

Ba khái niệm rất thường bị trộn là JDK, JRE và JVM. JVM là máy ảo thực thi bytecode. JRE theo cách gọi truyền thống là môi trường cần để chạy Java application, gồm JVM và standard runtime libraries. JDK là bộ công cụ phát triển, chứa compiler, runtime và các tools như `javac`, `jar`, `javadoc`, `jcmd`, `jshell`. Với Java hiện đại, cách đóng gói runtime đã thay đổi và khái niệm “cài một JRE riêng như thời Java 8” không còn là mental model tốt nhất, nhưng ba khái niệm trên vẫn giúp bạn hiểu kiến trúc.

Khi gặp lỗi “code compile trên máy tôi nhưng server không chạy”, hãy phân biệt compile-time và runtime. Ví dụ bạn compile class bằng JDK mới rồi deploy lên JVM cũ, server có thể báo `UnsupportedClassVersionError`. Đây không phải lỗi business logic; runtime đơn giản không hiểu class-file version mới.

---

# 2. Cài JDK và kiểm tra môi trường

Sau khi cài JDK, hai lệnh đầu tiên nên biết là:

```bash
java --version
javac --version
```

`java` dùng để chạy application. `javac` dùng để compile source. Nếu hai lệnh cho version khác nhau hoặc shell đang dùng một JDK khác IDE, bạn có thể gặp bug rất khó hiểu. Trong môi trường làm việc thực tế, đừng chỉ tin IDE đang hiển thị “Java 21”; hãy kiểm tra build tool, `JAVA_HOME`, runtime command và CI cũng dùng version nào.

Compile một file đơn giản:

```bash
javac Hello.java
```

Run:

```bash
java Hello
```

Nếu package được dùng, classpath và folder structure bắt đầu có ý nghĩa. Phần class loading sâu hơn sẽ học ở Intermediate và Senior; ở Beginner bạn chỉ cần hiểu rằng JVM phải tìm được `.class` đúng theo fully qualified class name.

---

# 3. Cấu trúc một chương trình Java

Một file:

```java
package com.example.hello;

import java.time.LocalDate;

public class HelloApplication {

    public static void main(String[] args) {
        LocalDate today = LocalDate.now();
        System.out.println(today);
    }
}
```

`package` xác định namespace của class. `import` cho phép viết short class name thay vì full name. Class `HelloApplication` chứa method `main`, là entry point truyền thống cho một Java application.

Package không chỉ dùng để “xếp folder cho đẹp”. Nó giúp tránh name collision và còn ảnh hưởng access control. Một class package-private có thể được các class cùng package dùng nhưng không public ra toàn application. Khi project lớn, package boundary trở thành một công cụ kiến trúc.

`import` không copy code và cũng không làm class “được load sẵn”. Nó chủ yếu là compile-time syntax để compiler biết `LocalDate` bạn viết đang nói tới type nào. Static import:

```java
import static java.util.Objects.requireNonNull;
```

cho phép:

```java
this.name = requireNonNull(name);
```

thay vì:

```java
this.name = Objects.requireNonNull(name);
```

Static import hợp khi symbol có nghĩa rõ trong context, ví dụ assertions trong tests hoặc một vài utility methods. Nếu dùng quá nhiều, người đọc khó biết method đến từ class nào.

---

# 4. `main()` và ý nghĩa của từng phần

Method truyền thống:

```java
public static void main(String[] args) {
}
```

`public` cho phép launcher truy cập. `static` nghĩa method thuộc class, không cần tạo object của class trước. `void` nghĩa không return value. `String[] args` chứa command-line arguments.

Ví dụ:

```bash
java Hello Alice
```

thì:

```java
args[0]
```

là `"Alice"`.

Bạn không cần biến mọi logic thành `static` chỉ vì `main` là static. Một application có thể dùng `main` chỉ để bootstrap object graph rồi chuyển control sang normal objects. Đây là thói quen quan trọng trước khi học Spring: `main` không nên là nơi chứa toàn bộ application.

---

# 5. Variable là gì?

Variable là một tên gắn với một vùng dữ liệu theo type nhất định.

```java
int age = 27;
```

Ở đây `int` là type, `age` là variable name, `27` là value ban đầu.

Bạn có thể khai báo rồi gán sau:

```java
int age;
age = 27;
```

nhưng local variable phải được definite assignment trước khi đọc. Compiler ngăn bạn dùng local variable chưa được gán một cách chắc chắn.

Field của object lại có default values như `0`, `false`, `null`, nhưng không nên dựa vào default một cách mơ hồ nếu field là phần quan trọng của invariant. Constructor nên thiết lập object thành trạng thái hợp lệ ngay từ lúc tạo.

---

# 6. Primitive types và reference types

Java có tám primitive types: `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`.

Trong application thông thường, integer thường dùng `int`; `long` khi range lớn hoặc ID/timestamp-like numeric values cần lớn hơn. `float` và `double` dùng floating-point binary arithmetic, rất phù hợp cho khoa học/đồ họa/nhiều phép tính gần đúng nhưng không nên tự động dùng cho tiền.

Ví dụ:

```java
double price = 0.1 + 0.2;
System.out.println(price);
```

có thể in ra một số không chính xác theo decimal intuition vì binary floating point không biểu diễn chính xác mọi decimal fraction. Tiền thường dùng `BigDecimal`, sẽ học sau.

`char` là một UTF-16 code unit, không phải luôn một “ký tự Unicode hoàn chỉnh” theo cách người dùng nhìn thấy. Unicode sâu hơn sẽ nằm ở Intermediate/Master.

Reference type gồm class, interface, array, enum, record và nhiều loại object khác.

```java
String name = "Kim";
User user = new User(...);
```

Variable reference không chứa toàn bộ object theo mental model đơn giản; nó chứa reference tới object. Vì vậy hai variables có thể trỏ tới cùng object.

```java
User a = user;
User b = user;
```

Thay đổi mutable state qua `a` có thể được nhìn thấy qua `b` vì cả hai reference cùng trỏ tới một object.

---

# 7. `null` là gì?

Reference variable có thể có giá trị `null`, nghĩa là hiện không trỏ tới object nào.

```java
User user = null;
```

Gọi:

```java
user.name();
```

sẽ gây `NullPointerException`.

Điểm quan trọng là `null` không phải object. Nó là special reference value. Nhiều bug Java đến từ contract không rõ: method này có thể return null không? parameter này có chấp nhận null không?

Nếu null không hợp lệ, fail sớm:

```java
public UserService(UserRepository repository) {
    this.repository =
        Objects.requireNonNull(repository);
}
```

Cách này làm lỗi xảy ra ngay tại boundary nơi invariant bị vi phạm, thay vì vài phút sau ở một method xa hơn.

Một application tốt không nhất thiết “không bao giờ dùng null”, nhưng null policy phải rõ. Collection method thường nên return empty collection thay vì null nếu “không có phần tử” là kết quả hợp lệ.

---

# 8. `final` và tư duy immutable

```java
final int maxRetry = 3;
```

Sau assignment, variable không thể được assign lại.

Với reference:

```java
final List<String> names =
        new ArrayList<>();
```

bạn không thể:

```java
names = anotherList;
```

nhưng vẫn có thể:

```java
names.add("Kim");
```

vì `final` khóa reference variable, không tự làm object immutable.

Dù vậy `final` rất hữu ích. Khi dependency field:

```java
private final UserRepository repository;
```

người đọc biết reference không bị đổi sau construction. Càng ít reassignment và mutable state, code càng dễ reason, nhất là khi concurrency xuất hiện.

Một thói quen tốt là để constructor thiết lập required fields và giữ chúng `final` khi có thể. Đây là nền của immutable object và constructor injection.

---

# 9. `var` từ Java 10

Java 10 hỗ trợ local variable type inference:

```java
var users =
    new ArrayList<User>();
```

Compiler vẫn biết exact static type. Java không trở thành dynamically typed language.

`var` chỉ dùng cho local variables trong những context cho phép; không dùng thay field type hoặc method return type.

Nó tốt khi right-hand side nói type rõ:

```java
var formatter =
    DateTimeFormatter.ISO_LOCAL_DATE;
```

Nó kém rõ khi:

```java
var result = process();
```

và không ai biết `process()` trả gì nếu không nhảy tới definition.

Do đó hãy dùng `var` để giảm noise, không để che semantic type.

---

# 10. Operators và thứ tự đánh giá

Arithmetic:

```java
+ - * / %
```

Comparison:

```java
== != > >= < <=
```

Logical:

```java
&& || !
```

Assignment:

```java
= += -= *= /=
```

Một điểm rất quan trọng là short-circuit evaluation.

```java
if (user != null && user.isActive()) {
}
```

Nếu `user == null`, vế phải không được evaluate, vì kết quả `&&` đã chắc chắn false. Đây là cách viết null guard hợp lệ.

Tương tự:

```java
if (cached != null || loadFallback()) {
}
```

nếu vế trái true, `loadFallback()` không chạy. Nếu method bên phải có side effect, short-circuit có thể làm flow khó đọc. Tránh nhét business side effect vào boolean expressions phức tạp.

---

# 11. `==` khác `equals()` như thế nào?

Với primitives, `==` so sánh value:

```java
int a = 10;
int b = 10;

a == b // true
```

Với references, `==` kiểm tra hai references có trỏ tới cùng object identity hay không.

```java
String a = new String("hello");
String b = new String("hello");

a == b       // false thường
a.equals(b)  // true
```

Đây là lý do so sánh `String` bằng `==` là lỗi kinh điển.

Null-safe equality:

```java
Objects.equals(a, b);
```

sẽ xử lý null.

Khi type của bạn biểu diễn value như `Money`, `UserId`, `Email`, `equals()` và `hashCode()` phải phản ánh value semantics. Nếu object được dùng làm `HashMap` key hoặc `HashSet` element, contract của hai methods này cực kỳ quan trọng. Intermediate sẽ đi sâu.

---

# 12. Casting và conversion

Widening primitive conversion thường an toàn hơn:

```java
int x = 10;
long y = x;
```

Narrowing cần explicit cast:

```java
long value = 1000L;
int x = (int) value;
```

Nếu value vượt range, dữ liệu có thể bị mất.

Object casting:

```java
Animal animal = new Dog();
Dog dog = (Dog) animal;
```

cast hợp lệ vì runtime object thật là `Dog`.

Sai:

```java
Animal animal = new Cat();
Dog dog = (Dog) animal;
```

gây `ClassCastException`.

Modern pattern matching:

```java
if (animal instanceof Dog dog) {
    dog.bark();
}
```

tránh separate cast và làm type narrowing rõ hơn.

Khi code có rất nhiều `instanceof` + casts theo type, hãy xem hierarchy có thiếu polymorphism hay closed-type modeling không. Java 17 sealed classes và Java 21 pattern switch sẽ giúp một số case.

---

# 13. `if`, `else` và Guard Clause

Basic:

```java
if (age >= 18) {
    allow();
} else {
    reject();
}
```

Nested code:

```java
if (user != null) {
    if (user.isActive()) {
        if (user.hasPermission()) {
            process(user);
        }
    }
}
```

khó đọc hơn guard clauses:

```java
if (user == null) {
    return;
}

if (!user.isActive()) {
    return;
}

if (!user.hasPermission()) {
    return;
}

process(user);
```

Guard clause làm invalid cases kết thúc sớm và giữ happy path phẳng. Đây không phải rule tuyệt đối; nếu có hai branch đối xứng, `if/else` có thể rõ hơn. Nhưng với validation/permission pipeline, guard clause thường rất hiệu quả.

---

# 14. `switch`: từ statement cũ đến expression hiện đại

Classic switch:

```java
switch (status) {
    case NEW:
        handleNew();
        break;
    case DONE:
        handleDone();
        break;
    default:
        handleOther();
}
```

Nếu quên `break`, fall-through có thể xảy ra. Có lúc fall-through chủ ý nhưng dễ bug.

Modern switch expression từ Java 14:

```java
String label =
    switch (status) {
        case NEW -> "New";
        case DONE -> "Done";
        case CANCELLED -> "Cancelled";
    };
```

Không cần `break`, và compiler có thể check exhaustiveness khi type hữu hạn phù hợp.

Với enum hoặc sealed hierarchy, switch expression làm data-oriented branch logic rõ. Tuy nhiên không phải mọi business behavior nên biến thành giant switch. Nếu mỗi case có behavior phức tạp và type có polymorphic responsibility thật, Strategy/State/polymorphism có thể phù hợp hơn.

---

# 15. Loops và chọn cấu trúc lặp

Classic for:

```java
for (int i = 0; i < users.size(); i++) {
    User user = users.get(i);
}
```

Enhanced for:

```java
for (User user : users) {
}
```

Nếu không cần index, enhanced for thường rõ hơn.

`while` hợp khi số lần lặp chưa biết trước:

```java
while (queue.hasNext()) {
    process(queue.next());
}
```

`do-while` đảm bảo body chạy ít nhất một lần.

`break` dừng loop, `continue` bỏ phần còn lại của iteration hiện tại.

Đừng biến loop thành nơi có 100 dòng logic. Nếu iteration có nhiều business steps, extract method:

```java
for (Order order : orders) {
    processOrder(order);
}
```

Không phải vì method ngắn luôn tốt, mà vì loop nói rõ “lặp qua orders”, còn method nói rõ “process một order”.

---

# 16. Methods và contract

Method:

```java
public Money calculateTotal(
        List<OrderItem> items) {
    ...
}
```

Method signature là một contract: input type gì, output type gì, access level nào, method name nói behavior nào.

Parameter là pass-by-value, kể cả reference. Java luôn copy **value của variable** vào parameter.

```java
void reassign(User user) {
    user = new User(...);
}
```

không đổi reference của caller.

Nhưng:

```java
void rename(User user) {
    user.setName("A");
}
```

có thể mutate cùng object mà caller đang giữ.

Đây là lý do câu “Java pass object by reference” là không chính xác. Java pass-by-value; với object, value được copy là reference value.

---

# 17. Method Overloading

Overloading nghĩa cùng method name nhưng khác parameter list:

```java
void send(String message)
void send(String message, int priority)
```

Compiler chọn overload ở compile time dựa trên static types và conversion rules.

Đừng tạo nhiều overload kết hợp boxing/varargs quá mơ hồ:

```java
process(int x)
process(Integer x)
process(int... values)
```

API có thể trở thành puzzle.

Một overload tốt thường đại diện convenient default:

```java
connect(host)
```

delegate:

```java
connect(host, DEFAULT_TIMEOUT)
```

---

# 18. Varargs

```java
void log(String... messages) {
}
```

Caller:

```java
log("A", "B", "C");
```

Trong method, `messages` gần như array.

Varargs nên ở cuối parameter list và dùng khi số arguments thực sự variable. Đừng thay `List<T>` bằng varargs cho data đã tồn tại dạng collection.

Generic varargs có type-erasure/heap-pollution concerns; Intermediate sẽ giải thích `@SafeVarargs`.

---

# 19. Arrays

```java
int[] numbers = {1, 2, 3};
```

Array có fixed length.

```java
numbers.length
```

Index từ `0` đến `length - 1`. Sai index gây `ArrayIndexOutOfBoundsException`.

Array biết runtime component type và có covariance:

```java
String[] strings = new String[2];
Object[] objects = strings;
```

nhưng:

```java
objects[0] = Integer.valueOf(1);
```

gây `ArrayStoreException`. Generics lại invariant theo cách khác. Đây là một trong các lý do collections generic thường dễ dùng hơn arrays trong application code.

`Arrays` utility:

```java
Arrays.sort(numbers);
Arrays.asList(...);
Arrays.copyOf(...);
```

Cẩn thận `Arrays.asList(array)` tạo fixed-size list view trên array; không giống `new ArrayList<>()`.

---

# 20. String và tính immutable

`String` immutable. Sau khi object String được tạo, nội dung logical của nó không đổi.

```java
String name = "Kim";
name.toUpperCase();
```

không sửa `name`.

Phải:

```java
name = name.toUpperCase();
```

Immutability giúp String an toàn hơn khi share, cache, dùng làm key và tối ưu nội bộ.

Các methods thường dùng:

```java
text.length()
text.isEmpty()
text.isBlank()
text.contains("x")
text.startsWith("A")
text.endsWith(".json")
text.substring(1, 4)
text.replace("a", "b")
text.split(",")
text.strip()
```

`isBlank()` và `strip()` có semantics Unicode-aware hơn `trim()` trong một số khía cạnh và có từ Java 11.

Text block từ Java 15:

```java
String sql = """
    select id, name
    from users
    where active = true
    """;
```

rất hữu ích cho SQL/JSON snippets.

---

# 21. String concatenation và StringBuilder

```java
String full = first + " " + last;
```

cho vài concatenations hoàn toàn ổn. Compiler/JVM có optimizations.

Nhưng loop:

```java
String result = "";

for (String value : values) {
    result += value;
}
```

có thể tạo nhiều intermediate strings.

Dùng:

```java
StringBuilder builder =
        new StringBuilder();

for (String value : values) {
    builder.append(value);
}

String result = builder.toString();
```

Tuy nhiên đừng micro-optimize mọi `+`. Chỉ dùng builder khi xây text lặp/phức tạp hoặc clarity phù hợp.

---

# 22. Normalize Input at Boundary

User input có thể có whitespace/case variations.

Bad:

```java
if (email.trim().toLowerCase().equals(...)) {
}
```

rải khắp code.

Better:

```java
String normalizedEmail =
    normalizeEmail(rawEmail);
```

rồi core dùng normalized form.

Cách này là một programming pattern quan trọng: **normalize/parse input ở boundary**, thay vì validate lặp lại ở mọi nơi. Sau này domain value object như `Email` có thể encapsulate rule này.

---

# 23. Wrapper Classes và Autoboxing

Primitive wrappers:

```text
int → Integer
long → Long
double → Double
boolean → Boolean
```

Autoboxing:

```java
Integer value = 10;
```

compiler box primitive thành object.

Unboxing:

```java
int x = value;
```

Nguy hiểm:

```java
Integer value = null;
int x = value;
```

gây NPE trong unboxing.

Collection generic không nhận primitive trực tiếp:

```java
List<Integer>
```

nên boxing có thể tạo allocation/performance cost ở hot paths. Beginner chưa cần tối ưu, nhưng cần biết semantic.

Parsing:

```java
int age =
    Integer.parseInt("27");
```

invalid text gây `NumberFormatException`.

---

# 24. Classes và Objects

Class mô tả state + behavior.

```java
public class BankAccount {
    private BigDecimal balance;

    public void deposit(BigDecimal amount) {
        ...
    }
}
```

Object là instance cụ thể:

```java
BankAccount account =
    new BankAccount();
```

OOP tốt không phải chỉ gom fields + getters/setters. Một object nên bảo vệ invariant.

Bad:

```java
account.setBalance(
    new BigDecimal("-999"));
```

Better:

```java
account.withdraw(amount);
```

và method kiểm tra không cho balance invalid.

Đây là tư duy “tell object what to do” thay vì lấy toàn bộ state ra ngoài rồi tự xử lý.

---

# 25. Constructor

Constructor tạo object ở trạng thái ban đầu.

```java
public User(
        String name,
        String email) {
    this.name =
        Objects.requireNonNull(name);
    this.email =
        Objects.requireNonNull(email);
}
```

Nếu `name`/`email` là required, object không nên có default constructor rồi chờ setter.

Constructor establishes validity là một thói quen rất mạnh. Nó làm impossible state khó tồn tại.

Constructor overloading:

```java
public User(String name) {
    this(name, null);
}
```

phải dùng cẩn thận nếu null làm object không hợp lệ.

---

# 26. `this` và `super`

`this` nói object hiện tại.

```java
this.name = name;
```

`this(...)` gọi constructor khác trong cùng class và phải là statement đầu tiên.

`super(...)` gọi constructor superclass và cũng phải ở đầu constructor theo rules tương ứng.

`super.method()` gọi implementation của parent khi override.

Các keyword này quan trọng nhưng không nên dùng inheritance phức tạp chỉ vì Java hỗ trợ.

---

# 27. Encapsulation và Access Modifiers

`private` giới hạn trong class. Package-private không viết modifier và cho cùng package access. `protected` liên quan subclass và package semantics. `public` expose rộng nhất.

Default nên là visibility hẹp nhất hợp lý. Nếu một helper chỉ cần trong package, không cần public.

Public API khó thay đổi hơn vì nhiều code có thể phụ thuộc. Đây là lý do “minimize public surface” là một principle quan trọng từ library tới application modules.

Encapsulation không chỉ là “fields private rồi generate getters/setters”. Nếu mọi state vẫn được set tùy ý, invariant chưa thực sự được encapsulate.

---

# 28. `static`

Static member thuộc class hơn là một instance.

```java
public static final int MAX_RETRY = 3;
```

Static utility method:

```java
public static boolean isBlank(String value) {
}
```

Static state mutable:

```java
public static List<User> users =
        new ArrayList<>();
```

là global mutable state và dễ tạo test/concurrency coupling.

Static không xấu. Constants, pure utilities và factory methods rất hữu ích. Điều cần tránh là dùng static global mutable state như hidden dependency.

---

# 29. Inheritance

```java
class Dog extends Animal {
}
```

Inheritance biểu diễn is-a relationship và reuse polymorphic behavior.

Override:

```java
@Override
public String sound() {
    return "woof";
}
```

Inheritance dễ bị lạm dụng để reuse code. Nếu `ReportService extends BaseService extends LoggingService...`, hierarchy cứng và fragile.

Thường composition rõ hơn:

```java
class ReportService {
    private final Formatter formatter;
}
```

“Favor composition over inheritance” là heuristic, không luật tuyệt đối. Inheritance tốt khi hierarchy thực sự ổn định và substitutability đúng.

---

# 30. Polymorphism

Interface:

```java
interface PaymentGateway {
    PaymentResult pay(Money amount);
}
```

Implementations:

```java
class CardGateway
        implements PaymentGateway {
}
```

```java
class BankGateway
        implements PaymentGateway {
}
```

Caller:

```java
PaymentGateway gateway =
    new CardGateway();

gateway.pay(amount);
```

Method dispatch chọn implementation runtime.

Đây là nền của Strategy Pattern: caller phụ thuộc behavior contract, implementation có thể thay.

Spring Dependency Injection sau này tận dụng đúng kiểu abstraction này.

---

# 31. Interfaces

Interface khai báo contract:

```java
public interface UserRepository {
    Optional<User> findById(UserId id);
}
```

Class:

```java
public final class JdbcUserRepository
        implements UserRepository {
}
```

Java 8 thêm default/static methods trong interface; Java 9 thêm private interface methods để share implementation giữa default methods.

Đừng tạo interface cho mọi class chỉ vì “best practice”. Interface hữu ích khi có abstraction thật: nhiều implementations, test seam, external boundary hoặc stable public contract.

Một class internal duy nhất không cần interface giả tạo nếu không có reason.

---

# 32. Abstract Classes

Abstract class cho shared state/behavior + abstract methods.

```java
abstract class Report {
    public final void generate() {
        load();
        render();
        save();
    }

    protected abstract void render();
}
```

Đây gần Template Method Pattern: superclass define algorithm skeleton, subclass customize steps.

So với interface, abstract class có instance state/constructors và single inheritance restriction.

Nếu customization cần linh hoạt, composition/Strategy thường dễ thay hơn.

---

# 33. Enum

Bad:

```java
String status = "DONE";
```

typo `"DNOE"` compile vẫn qua.

Enum:

```java
enum OrderStatus {
    NEW,
    PAID,
    SHIPPED,
    CANCELLED
}
```

Type-safe hơn.

Enum có fields/methods:

```java
enum PaymentType {
    CARD("C"),
    BANK("B");

    private final String code;

    PaymentType(String code) {
        this.code = code;
    }

    public String code() {
        return code;
    }
}
```

Đừng persist ordinal mặc định nếu business/storage contract cần stable values; reorder enum có thể phá dữ liệu. Stable code/string thường an toàn hơn.

---

# 34. Records từ Java 16

Record phù hợp cho data-centric immutable-ish carriers.

```java
public record UserResponse(
        long id,
        String name,
        String email) {
}
```

Compiler tạo accessors, constructor, `equals`, `hashCode`, `toString` theo record components.

Compact constructor:

```java
public record Money(
        BigDecimal amount,
        Currency currency) {

    public Money {
        Objects.requireNonNull(amount);
        Objects.requireNonNull(currency);
    }
}
```

Record shallowly immutable: reference fields không thể reassigned, nhưng object bên trong có thể mutable.

```java
record Config(List<String> rules) {
}
```

Nếu `rules` mutable, caller vẫn có thể mutate list. Use `List.copyOf` nếu cần ownership snapshot.

---

# 35. Sealed Classes awareness

Java 17 finalizes sealed classes.

```java
sealed interface PaymentResult
    permits Success, Rejected {
}
```

```java
record Success(String id)
        implements PaymentResult {
}
```

```java
record Rejected(String reason)
        implements PaymentResult {
}
```

Sealed hierarchy nói set implementations được kiểm soát. Khi kết hợp pattern switch Java 21, compiler có thể reason exhaustiveness.

Nó phù hợp cho finite alternatives, nhưng không nên seal extension point mà third-party/plugin cần mở rộng.

---

# 36. `Object` methods

Mọi class reference type cuối cùng liên hệ `Object`.

Methods quan trọng: `equals`, `hashCode`, `toString`, `getClass`.

Override `toString()` để log/debug hữu ích nhưng không expose secrets.

Nếu override `equals`, phải override `hashCode` consistent. Hash-based collections dựa contract này. Intermediate sẽ đi sâu mutable-key trap và hash semantics.

---

# 37. Exceptions: error flow trong Java

Exception là object biểu diễn abnormal condition.

Checked exceptions phải được catch hoặc declare:

```java
void load()
        throws IOException {
}
```

Unchecked exceptions extend `RuntimeException`; compiler không bắt caller declare.

Throw:

```java
throw new IllegalArgumentException(
    "amount must be positive");
```

Catching:

```java
try {
    load();
} catch (IOException e) {
    ...
}
```

Đừng catch rồi bỏ:

```java
catch (Exception e) {
}
```

vì bạn mất signal và root cause.

Catch exception khi bạn có thể recover, translate, add context hoặc terminate ở ownership boundary.

---

# 38. Checked vs Unchecked: đừng học thành “checked tốt/xấu”

Checked exception phù hợp khi caller realistically được kỳ vọng xử lý/recover theo contract. Unchecked phù hợp cho programming errors, invalid states và nhiều infrastructure failures nơi forcing every layer catch/declare không thêm value.

Không có rule “backend luôn dùng RuntimeException”. Điều quan trọng là exception taxonomy và boundary.

Ví dụ repository có thể catch vendor SQL exception và translate thành application data-access exception có cause giữ nguyên.

```java
throw new DataAccessFailure(
    "Cannot load user " + id,
    e);
```

Giữ cause giúp production debugging.

---

# 39. `finally` và Try-with-resources

Resource như file/socket/database connection cần close.

Classic:

```java
InputStream in = null;

try {
    in = Files.newInputStream(path);
    ...
} finally {
    if (in != null) {
        in.close();
    }
}
```

Modern:

```java
try (InputStream in =
         Files.newInputStream(path)) {
    ...
}
```

Try-with-resources gọi `close()` tự động cho `AutoCloseable`.

Nếu body throw và `close()` cũng throw, exception từ close có thể thành suppressed exception, không làm mất primary exception.

Resource ownership phải rõ. Method nhận stream từ caller thường không nên tự close nếu contract nói caller sở hữu nó.

---

# 40. Collections Framework: tại sao có nhiều loại collection?

Không có một collection “tốt nhất”.

`List` biểu diễn ordered sequence, cho phép duplicates.

`Set` biểu diễn uniqueness.

`Map` biểu diễn key → value lookup.

`Queue`/`Deque` biểu diễn processing order.

Chọn type theo semantics trước performance.

Nếu domain nói “mỗi email chỉ xuất hiện một lần”, `Set<Email>` có thể encode constraint tốt hơn `List<Email>` + manual duplicate checks.

---

# 41. `ArrayList`

Default list implementation cho phần lớn application use cases.

```java
List<String> names =
    new ArrayList<>();

names.add("Kim");
names.add("Lee");
```

Fast random access theo index và append thường hiệu quả.

Insert/remove giữa list có thể shift elements.

Đừng chọn `LinkedList` chỉ vì thấy O(1) insertion trên textbook. Real workloads còn cache locality, traversal và việc tìm node. `ArrayList` thường là default tốt cho general-purpose list.

---

# 42. `Set`

`HashSet` cho uniqueness với hash-based lookup.

```java
Set<String> emails =
    new HashSet<>();

emails.add("a@example.com");
emails.add("a@example.com");
```

size vẫn 1.

`LinkedHashSet` preserve insertion order. `TreeSet` sorted theo natural/comparator order.

Set correctness phụ thuộc `equals/hashCode` hoặc ordering comparator. Mutable element fields dùng trong equality/hash có thể phá lookup.

---

# 43. `Map`

```java
Map<Long, User> users =
    new HashMap<>();
```

Common:

```java
users.put(id, user);
users.get(id);
users.getOrDefault(id, fallback);
users.containsKey(id);
users.putIfAbsent(id, user);
```

`computeIfAbsent` cực hữu ích:

```java
groups.computeIfAbsent(
        department,
        key -> new ArrayList<>()
    )
    .add(user);
```

Nó diễn đạt grouping/indexing pattern rõ hơn manual check-then-put.

`merge` tốt cho counting:

```java
counts.merge(word, 1, Integer::sum);
```

Đây là ví dụ Java API chứa patterns mà bạn nên nhận ra, không chỉ thuộc method names.

---

# 44. `HashMap`, `LinkedHashMap`, `TreeMap`

`HashMap` là default general-purpose map khi không cần ordering.

`LinkedHashMap` giữ insertion order hoặc có thể dùng access-order cho LRU-like logic.

`TreeMap` giữ sorted keys dựa comparator/natural order với tree-based complexity.

Đừng chọn `TreeMap` chỉ vì “sorted đẹp”; sorting có cost. Chọn khi sorted navigation/range semantics thực sự cần.

---

# 45. Immutable collection factory methods từ Java 9

```java
List<String> names =
    List.of("Kim", "Lee");

Set<String> roles =
    Set.of("USER", "ADMIN");

Map<String, Integer> limits =
    Map.of("A", 10, "B", 20);
```

Các factory này tạo unmodifiable collections và reject `null`.

Nếu nhận mutable list từ caller mà muốn ownership snapshot:

```java
this.roles =
    List.copyOf(roles);
```

Điều này tốt hơn giữ external mutable reference.

Unmodifiable view và immutable snapshot khác nhau. `Collections.unmodifiableList(original)` ngăn mutate qua view nhưng nếu `original` bị mutate, view vẫn đổi. `List.copyOf(original)` tạo snapshot-style collection independent theo structural state tại thời điểm copy.

---

# 46. Generics: type safety trước khi runtime

Without generics:

```java
List values = new ArrayList();
values.add("hello");
values.add(123);
```

compiler không bảo vệ.

With generics:

```java
List<String> values =
    new ArrayList<>();

values.add("hello");
// values.add(123); compile error
```

Generic type parameter cho reusable type-safe abstractions.

```java
class Box<T> {
    private T value;

    T get() {
        return value;
    }
}
```

Generic method:

```java
static <T> T first(List<T> values) {
    return values.get(0);
}
```

Beginner chỉ cần hiểu `T` là compile-time type parameter. Type erasure, wildcard variance và PECS sẽ sang Intermediate.

---

# 47. Diamond Operator

```java
Map<String, List<User>> users =
    new HashMap<String, List<User>>();
```

có thể viết:

```java
Map<String, List<User>> users =
    new HashMap<>();
```

Compiler infer type arguments từ left side/context.

Đây là giảm noise, không thay static typing.

---

# 48. Lambdas từ Java 8

Functional interface có đúng một abstract method.

```java
@FunctionalInterface
interface DiscountPolicy {
    BigDecimal apply(BigDecimal price);
}
```

Implementation anonymous class:

```java
DiscountPolicy policy =
    new DiscountPolicy() {
        @Override
        public BigDecimal apply(
                BigDecimal price) {
            return price.multiply(
                new BigDecimal("0.9"));
        }
    };
```

Lambda:

```java
DiscountPolicy policy =
    price -> price.multiply(
        new BigDecimal("0.9"));
```

Lambda giúp behavior trở thành value truyền vào method, rất hợp với Strategy.

---

# 49. Standard Functional Interfaces

`Predicate<T>` nhận T và trả boolean.

```java
Predicate<User> active =
    User::isActive;
```

`Function<T,R>` biến T thành R.

```java
Function<User, String> toName =
    User::name;
```

`Consumer<T>` nhận T và không return useful value.

```java
Consumer<String> printer =
    System.out::println;
```

`Supplier<T>` không nhận input và tạo T.

```java
Supplier<UUID> idGenerator =
    UUID::randomUUID;
```

Khi lambda phức tạp nhiều lines/conditions, named method hoặc named strategy class có thể rõ hơn.

---

# 50. Method References

```java
users.stream()
    .map(User::name)
```

tương đương gần ý nghĩa:

```java
users.stream()
    .map(user -> user.name())
```

Method reference tốt khi target method name diễn đạt rõ. Nếu phải đoán receiver/overload, lambda explicit có thể dễ đọc hơn.

---

# 51. Stream API

Stream là pipeline xử lý data, không phải collection lưu data.

```java
List<String> activeNames =
    users.stream()
         .filter(User::isActive)
         .map(User::name)
         .sorted()
         .toList();
```

Flow:

```text
source
→ filter
→ transform
→ order
→ terminal result
```

Intermediate operations như `filter`, `map`, `sorted` thường lazy; terminal operation như `toList`, `count`, `findFirst` kích hoạt evaluation.

Stream single-use. Sau terminal operation, không reuse cùng stream.

---

# 52. Khi nào Stream dễ đọc?

Transformation pipeline:

```java
users.stream()
     .filter(User::isActive)
     .map(User::email)
     .toList();
```

rất rõ.

Nếu logic có nhiều side effects, nested error handling và state mutations, loop có thể rõ hơn.

Đừng viết stream chỉ để chứng minh “Java hiện đại”. Chọn representation giúp người đọc thấy intent.

---

# 53. `filter`, `map`, `distinct`, `sorted`, `limit`, `skip`

`filter` giữ elements thỏa predicate.

`map` transform mỗi element.

`distinct` remove duplicates dựa equality.

`sorted` sort.

`limit(n)` lấy tối đa n.

`skip(n)` bỏ n đầu.

Ví dụ:

```java
List<String> topEmails =
    users.stream()
         .filter(User::isActive)
         .map(User::email)
         .distinct()
         .sorted()
         .limit(10)
         .toList();
```

Đây là declarative data transformation.

---

# 54. Terminal operations

`forEach` thực hiện action:

```java
users.forEach(
    System.out::println);
```

`count` đếm.

`findFirst` trả `Optional<T>`.

`anyMatch`, `allMatch`, `noneMatch` short-circuit.

```java
boolean hasAdmin =
    users.stream()
         .anyMatch(User::isAdmin);
```

`collect` và collectors mạnh hơn sẽ học Intermediate.

---

# 55. Optional

Optional biểu diễn “có value hoặc không” một cách explicit trong return type.

```java
Optional<User> findById(long id);
```

Caller:

```java
User user =
    repository.findById(id)
              .orElseThrow(
                  () ->
                    new UserNotFoundException(id));
```

Create:

```java
Optional.of(value);
Optional.ofNullable(value);
Optional.empty();
```

`Optional.of(null)` throw NPE; dùng `ofNullable` nếu value có thể null.

Optional hữu ích cho return semantics. Không cần dùng `Optional` cho mọi field/parameter.

---

# 56. `orElse` vs `orElseGet`

```java
optional.orElse(
    expensiveFallback());
```

`expensiveFallback()` được evaluate trước khi `orElse` được gọi, kể cả Optional có value.

```java
optional.orElseGet(
    this::expensiveFallback);
```

supplier chỉ chạy khi empty.

Đây là ví dụ API laziness ảnh hưởng performance/side effect.

---

# 57. Sorting: Comparable và Comparator ở mức Beginner

Natural order:

```java
class User
        implements Comparable<User> {
    ...
}
```

Nhưng một domain type có thể có nhiều sort orders, nên `Comparator` thường linh hoạt.

```java
Comparator<User> byName =
    Comparator.comparing(User::name);

Comparator<User> byAgeDesc =
    Comparator.comparingInt(User::age)
              .reversed();
```

Combine:

```java
Comparator<User> comparator =
    Comparator.comparing(User::department)
              .thenComparing(User::name);
```

Không comparator bằng subtraction:

```java
(a, b) -> a.age() - b.age()
```

vì overflow có thể xảy ra. Dùng `Integer.compare`/`comparingInt`.

---

# 58. Date/Time API

Legacy `Date`/`Calendar` có many design problems. Java 8 `java.time` nên là default.

`LocalDate` là ngày không timezone:

```java
LocalDate birthday =
    LocalDate.of(2000, 7, 26);
```

`LocalTime` là giờ trong ngày không date/zone.

`LocalDateTime` là date+time nhưng vẫn không timezone/offset.

`Instant` là timestamp trên UTC timeline.

`ZonedDateTime` kết hợp local date-time với time-zone rules.

Business rule “store exact event time” thường dùng `Instant`. Display theo Seoul dùng `ZoneId.of("Asia/Seoul")`.

```java
ZonedDateTime seoul =
    instant.atZone(
        ZoneId.of("Asia/Seoul"));
```

Intermediate sẽ đi sâu DST/offset.

---

# 59. `Duration` và `Period`

`Duration` đo time-based amount như seconds/nanos.

```java
Duration timeout =
    Duration.ofSeconds(2);
```

`Period` đo date-based years/months/days.

```java
Period oneMonth =
    Period.ofMonths(1);
```

“30 days” và “1 month” không phải luôn cùng nghĩa. Calendar arithmetic và elapsed time là hai domain khác nhau.

---

# 60. DateTimeFormatter

```java
DateTimeFormatter formatter =
    DateTimeFormatter.ofPattern(
        "yyyy-MM-dd");

String text =
    date.format(formatter);
```

Prefer standard ISO format khi API contract không cần custom.

Parse/format ở boundary; core nên giữ typed date/time.

---

# 61. BigDecimal cho Money

Bad:

```java
BigDecimal amount =
    new BigDecimal(0.1);
```

`0.1` đã là imprecise double trước khi constructor nhận.

Use:

```java
new BigDecimal("0.1")
```

hoặc:

```java
BigDecimal.valueOf(0.1);
```

Operations:

```java
amount.add(other);
amount.subtract(other);
amount.multiply(rate);
amount.divide(divisor, scale, roundingMode);
```

BigDecimal immutable, nên phải giữ result.

Comparison:

```java
a.compareTo(b) == 0
```

thường phù hợp numeric equality hơn `equals`, vì `equals` còn xem scale:

```text
1.0 != 1.00 theo equals
```

Policy rounding nên nằm ở domain type/service, không rải `setScale(... HALF_UP)` khắp code.

---

# 62. File I/O với Path và Files

Modern API:

```java
Path path =
    Path.of("data", "users.txt");
```

Không tự concatenate:

```java
"data/" + filename
```

vì path separator/platform/security concerns.

Read text Java 11+:

```java
String content =
    Files.readString(
        path,
        StandardCharsets.UTF_8);
```

Write:

```java
Files.writeString(
    path,
    content,
    StandardCharsets.UTF_8);
```

Copy:

```java
Files.copy(
    source,
    target,
    StandardCopyOption.REPLACE_EXISTING);
```

Create directory:

```java
Files.createDirectories(path);
```

Always make charset explicit when file contract matters.

---

# 63. Streams trong I/O: InputStream, Reader, Buffered layers

`InputStream` xử lý bytes.

`Reader` xử lý characters.

Nếu đọc text từ byte stream, cần charset.

```java
try (BufferedReader reader =
         Files.newBufferedReader(
             path,
             StandardCharsets.UTF_8)) {

    String line;

    while ((line = reader.readLine())
            != null) {
        ...
    }
}
```

Buffered wrappers giảm calls xuống underlying resource.

Decorator Pattern xuất hiện ở Java I/O: bạn wrap một stream để thêm behavior.

```text
FileInputStream
→ BufferedInputStream
→ DataInputStream
```

Đừng học tên pattern trước flow; hãy nhìn việc mỗi layer bọc layer dưới và bổ sung capability.

---

# 64. Annotations

Annotation là metadata.

```java
@Override
public String toString() {
}
```

`@Override` giúp compiler verify method thật sự override.

`@Deprecated` báo API cũ.

`@SuppressWarnings` tắt compiler warning có chủ đích.

Custom:

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Audited {
}
```

Annotation tự nó không chạy behavior. Một compiler, annotation processor, framework hoặc reflection code phải đọc nó.

Đây là kiến thức cực quan trọng trước Spring: `@Transactional` không phải transaction engine; Spring infrastructure đọc metadata rồi tạo behavior.

---

# 65. Immutability và Defensive Copy

Immutable object không thay logical state sau construction.

```java
public final class UserProfile {
    private final List<String> roles;

    public UserProfile(
            List<String> roles) {
        this.roles =
            List.copyOf(roles);
    }

    public List<String> roles() {
        return roles;
    }
}
```

Nếu chỉ:

```java
this.roles = roles;
```

caller còn giữ mutable list và có thể thay state object từ bên ngoài.

Defensive copy ở ownership boundary giúp object kiểm soát state.

Immutability giảm synchronization surface trong concurrency và làm caching/equality dễ hơn.

---

# 66. Basic Error Handling Architecture

Không phải mọi error giống nhau.

Invalid input:

```java
throw new IllegalArgumentException(...);
```

Business absence:

```java
UserNotFoundException
```

Infrastructure:

```java
DataAccessException-like
```

Programming bug:

```text
NullPointerException
IllegalStateException
```

Boundary như HTTP/CLI có thể translate exceptions thành response/exit code.

Đừng catch tất cả ở mọi layer rồi log + rethrow; bạn sẽ có duplicate logs và mất ownership.

---

# 67. Basic API Design

Prefer semantic type:

```java
UserId
```

over passing unrelated `long` values nếu domain đủ phức tạp.

Prefer empty list:

```java
return List.of();
```

over null khi “không có items” là normal.

Method name phải mô tả intent:

```java
activateUser()
```

rõ hơn:

```java
process()
```

Boolean parameters:

```java
send(user, true, false)
```

khó đọc. Có thể dùng options object/enum/named methods khi flags tăng.

---

# 68. Strategy Pattern trong Java thực tế

Contract:

```java
interface DiscountPolicy {
    Money discount(Order order);
}
```

Implementation:

```java
final class VipDiscountPolicy
        implements DiscountPolicy {
}
```

Caller không cần `if` theo implementation.

Lambda có thể implement strategy nếu behavior nhỏ:

```java
DiscountPolicy none =
    order -> Money.zero();
```

Strategy là “thay behavior bằng composition”, không phải “cứ có interface là Strategy”.

---

# 69. Factory

Static factory:

```java
public static UserId of(long value) {
    if (value <= 0) {
        throw new IllegalArgumentException();
    }

    return new UserId(value);
}
```

Factory có lợi khi construction cần validation, caching, subtype selection hoặc tên có meaning.

```java
Money.zero(currency)
```

có thể rõ hơn constructor với magic values.

---

# 70. Builder

Constructor:

```java
new HttpRequestConfig(
    host,
    port,
    timeout,
    retry,
    proxy,
    headers,
    ssl);
```

nhiều optional parameters khó đọc.

Builder:

```java
HttpRequestConfig config =
    HttpRequestConfig.builder()
        .host(host)
        .timeout(timeout)
        .retry(3)
        .build();
```

Builder phù hợp object có nhiều optional config; không cần builder cho record 2 fields.

---

# 71. Repository Pattern awareness

Business code:

```java
interface UserRepository {
    Optional<User> findById(UserId id);
    void save(User user);
}
```

Infrastructure implementation có thể JDBC, file hoặc memory.

Repository giúp core không phụ thuộc storage detail và tạo test seam.

Spring Data JPA sau này generate repository implementation, nhưng pattern tồn tại trước Spring.

---

# 72. Debugging Mindset

Khi gặp:

```text
NullPointerException
IndexOutOfBoundsException
IllegalArgumentException
ClassCastException
NumberFormatException
IOException
```

đừng chỉ đọc exception class. Đọc stack trace từ top exception + cause chain và tìm **first frame thuộc code của bạn** gần lỗi.

Workflow tốt:

```text
reproduce
→ minimize/isolate
→ inspect actual values
→ form hypothesis
→ change one thing
→ verify
```

Không sửa nhiều lines cùng lúc rồi không biết change nào giải quyết.

---

# 73. Basic CLI và JAR

Compile output:

```bash
javac -d out \
  src/com/example/Main.java
```

Run classpath:

```bash
java -cp out \
  com.example.Main
```

Create JAR:

```bash
jar --create \
    --file app.jar \
    -C out .
```

List:

```bash
jar --list \
    --file app.jar
```

Senior habit bắt đầu từ Beginner: khi runtime khác local, inspect actual artifact/version thay vì chỉ inspect source.

---

# 74. Java Version Roadmap cần nhận biết

Java 8 là mốc rất lớn với lambdas, Stream API, Optional và `java.time`.

Java 9 thêm module system, collection factory methods và API improvements.

Java 10 thêm local `var`.

Java 11 là LTS và thêm nhiều String/Files APIs, standard HTTP Client và lambda parameter `var`.

Java 14 finalizes switch expressions.

Java 15 finalizes text blocks.

Java 16 finalizes records và pattern matching cho `instanceof`; Stream có `toList()` từ generation này.

Java 17 là LTS và finalizes sealed classes.

Java 21 là LTS, finalizes record patterns, pattern matching for switch và Virtual Threads.

Java 25 là LTS mới hơn và nên được xem là modern production target khi ecosystem của bạn hỗ trợ. Java 26 là non-LTS release hiện tại vào thời điểm tài liệu được cập nhật. Part Master Supplement sẽ cover feature delta 22–26 sâu hơn.

LTS không có nghĩa “feature tốt hơn”; nó nghĩa vendor/support cadence phù hợp long-lived production.

---

# 75. Package by Feature và Project Structure

Technical-layer-only:

```text
controller/
service/
repository/
model/
```

đơn giản khi project nhỏ.

Feature structure:

```text
user/
order/
payment/
```

giúp code cùng business capability nằm gần nhau.

Trong mỗi feature bạn có thể giữ classes package-private để hạn chế accidental dependency.

Bạn chưa cần DDD/module architecture ở Beginner. Chỉ cần hình thành thói quen: package structure phải giúp dependency dễ hiểu, không phải chỉ giúp IDE nhìn đẹp.

---

# 76. Testing Mindset

Code:

```java
class PriceService {
    private final Clock clock;
    private final DiscountPolicy policy;

    PriceService(
            Clock clock,
            DiscountPolicy policy) {
        this.clock = clock;
        this.policy = policy;
    }
}
```

test có thể inject deterministic `Clock.fixed(...)` và fake policy.

Nếu method gọi trực tiếp:

```java
Instant.now()
```

và `new RealPaymentGateway()`, behavior khó control hơn.

Dependency Injection không phải pattern riêng của Spring. Nó là plain Java design để testability và decoupling tốt.

---

# 77. Anti-pattern: String equality bằng `==`

Sai:

```java
if (status == "DONE") {
}
```

Đúng:

```java
if ("DONE".equals(status)) {
}
```

hoặc:

```java
Objects.equals(status, "DONE");
```

Tốt hơn nữa nếu finite business statuses:

```java
OrderStatus.DONE
```

Enum loại typo và centralize domain states.

---

# 78. Anti-pattern: Return null collection

Bad:

```java
List<User> findUsers() {
    return null;
}
```

caller phải null-check trước loop.

Better:

```java
return List.of();
```

“không có result” là empty sequence, không phải absence của collection object.

---

# 79. Anti-pattern: `double` cho Money

```java
double total = 0.1 + 0.2;
```

không phù hợp exact decimal monetary semantics.

Use `BigDecimal` + currency + rounding policy.

Một domain `Money` value object có thể encapsulate cả ba để tránh code rải rounding.

---

# 80. Anti-pattern: Giant method

Một method 300 lines thường chứa nhiều levels of abstraction.

Không phải cứ >20 lines là xấu. Nhưng nếu method vừa parse input, query DB, calculate, format email và write file, responsibility đang trộn.

Extract methods/classes theo meaningful behavior, không theo arbitrary line count.

---

# 81. Anti-pattern: Mutable Static Global State

```java
public static Map<String, User>
    USERS = new HashMap<>();
```

làm state global, thread-safety khó, tests ảnh hưởng nhau và lifecycle mơ hồ.

Prefer explicit owner object/service/repository.

---

# 82. Anti-pattern: Overengineering

Người mới biết patterns dễ tạo:

```text
AbstractFactoryFactory
Strategy interface
Builder
Adapter
Decorator
```

cho một function 5 lines.

Pattern là response tới lực thiết kế, không phải checklist cần nhét vào project.

Code trực tiếp, rõ và dễ thay trước. Abstraction khi variation/coupling thực sự xuất hiện.

---

# 83. Beginner Project đề xuất

Hãy viết plain Java `Order Processing CLI`.

Domain gồm `Order`, `OrderItem`, `Money`, `OrderStatus`, `CustomerId`.

Input đọc từ file CSV hoặc console, parse thành typed objects. Validation phải xảy ra ở boundary. Repository ban đầu in-memory. Pricing dùng `DiscountPolicy` strategy. Output ghi result file bằng `Files`.

Dùng collections, streams ở nơi phù hợp, exceptions có taxonomy cơ bản, `Clock` inject nếu cần time, `BigDecimal` cho money và `java.time` cho timestamps.

Sau đó viết tests cho domain/service mà không framework.

Project này là bridge rất tốt trước JDBC/concurrency/Spring.

---

# 84. Beginner → Intermediate Gate

Trước khi sang Part 2, bạn phải có thể tự giải thích Java source được compile/run ra sao, primitive/reference/null khác nhau, Java pass-by-value nghĩa gì, `==` và `equals` khác gì, constructor/encapsulation/inheritance/polymorphism/interfaces dùng để giải quyết problem nào và tại sao composition thường linh hoạt.

Bạn phải chọn được `List`, `Set`, `Map`; biết `HashMap`/`ArrayList` là default use cases nào; dùng generics, lambda, Stream pipeline, Optional, Comparator, `java.time`, `BigDecimal`, `Path`/`Files` và try-with-resources.

Bạn phải hiểu rằng annotations là metadata, immutability và defensive copy liên quan ownership, exceptions cần preserve cause và resources phải có lifecycle rõ.

Quan trọng nhất, bạn phải nhìn code không chỉ như cú pháp mà như **contract + ownership + state + behavior**.

---

# 85. Điều cố ý chưa đào sâu

Part 1 chưa đào sâu wildcard/PECS/type erasure, Stream collectors nâng cao, Java Memory Model, locks, executors, CompletableFuture, JDBC transaction internals, reflection/proxy/class loading, JVM memory/GC/JIT và production diagnostics. Những phần đó thuộc Intermediate.

Senior-level runtime như bytecode/JIT deoptimization, safe publication, lock contention, GC tuning, JFR, virtual-thread production model, distributed consistency và architecture sẽ ở Part 3.

Master Supplement sẽ bổ sung low-level areas như VarHandle, AQS, Flow, Spliterator/Gatherers, FFM, class-file API, agents/instrumentation và Java 22–26 evolution.

---

# 86. Kết luận Part 1

Nếu chỉ nhớ syntax, bạn có thể viết code chạy. Nếu hiểu type contracts, ownership, mutability, exceptions, resources và abstraction, bạn bắt đầu viết Java có thể maintain.

Mental model cuối Part 1 nên là:

```text
Source code
→ Compiler
→ Bytecode
→ JVM

Input
→ Parse / Validate
→ Typed Objects
→ Business Behavior
→ Repository / I/O
→ Output

Object
→ valid constructor
→ controlled state
→ clear methods
→ explicit dependencies
```

Khi ba flow này trở thành tự nhiên, Part 2 mới thực sự có ý nghĩa, vì concurrency, reflection, JDBC và JVM đều xây trên nền đó.

---

# References for version-sensitive topics

Oracle Java SE Support Roadmap:
https://www.oracle.com/java/technologies/java-se-support-roadmap.html

Oracle JDK 25 release notes:
https://www.oracle.com/java/technologies/javase/25all-relnotes.html

Oracle JDK 26 release notes:
https://www.oracle.com/java/technologies/javase/26all-relnotes.html

Oracle Java language documentation:
https://docs.oracle.com/en/java/javase/
