# Java Core — Part 1: Beginner

> Lộ trình tổng thể: **Beginner → Intermediate → Senior**  
> File này chỉ tập trung vào **Beginner**, nhưng mỗi chủ đề đều có các ghi chú giúp nhìn trước cách senior suy nghĩ.

---

## Cách đọc tài liệu này

Mỗi chủ đề được trình bày theo cùng một cấu trúc:

1. **Khái niệm** — thứ cần hiểu trước khi nhớ cú pháp.
2. **Syntax / API** — câu lệnh, method, option cần biết.
3. **Ví dụ thực tế** — ví dụ ngắn, ưu tiên backend/business code.
4. **Language Idioms** — cách viết “đúng chất Java”, thường gặp trong codebase tốt.
5. **Coding / Programming Patterns** — mẫu tổ chức logic ở mức code.
6. **Design Patterns** — liên hệ với pattern lớn hơn khi phù hợp.
7. **Senior Notes** — các quyết định, trade-off, bug production và thói quen của senior.

### Mức ưu tiên

- **P0 — Must know:** dùng gần như hằng ngày.
- **P1 — Very common:** gặp thường xuyên trong dự án.
- **P2 — Important:** không dùng mọi ngày nhưng phải hiểu.
- **P3 — Awareness:** biết tồn tại để đọc code và học tiếp.

### Version notation

- **Java 8**: baseline cực kỳ quan trọng trong enterprise.
- **Java 11**: LTS, thêm một số API tiện dụng.
- **Java 17**: LTS, rất phổ biến trong Spring hiện đại.
- **Java 21**: LTS, thêm nhiều syntax/API mới đáng học.

---

# 0. Mental Model: Java chạy như thế nào? — P0

Java source code không chạy trực tiếp như script.

Flow cơ bản:

```text
.java source
   ↓ javac
.class bytecode
   ↓ JVM
machine code / interpreted + JIT compiled code
```

Ví dụ:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello Java");
    }
}
```

Compile:

```bash
javac Main.java
```

Run:

```bash
java Main
```

`javac` tạo `Main.class` chứa **bytecode**. JVM đọc bytecode và thực thi.

## JDK, JRE, JVM

### JVM — Java Virtual Machine

JVM chịu trách nhiệm:

- load `.class`
- verify bytecode
- quản lý memory
- garbage collection
- JIT compilation
- execute bytecode

### JRE — Java Runtime Environment

Khái niệm runtime để chạy Java. Trong Java hiện đại, cách phân phối JDK/JRE đã thay đổi so với thời Java cũ, nhưng về mặt học thuật vẫn cần phân biệt runtime với bộ công cụ phát triển.

### JDK — Java Development Kit

Bao gồm JVM + compiler + tooling:

```text
java
javac
jar
javadoc
jcmd
jstack
jmap
...
```

## Language Idiom

Java developer thường không compile từng file thủ công trong dự án thực tế. Maven/Gradle sẽ quản lý compile, dependency, test, packaging.

Tuy nhiên vẫn phải hiểu:

```bash
javac
java
jar
```

vì nó giải thích bản chất build/runtime.

## Programming Pattern

Tách khái niệm:

```text
source code ≠ compiled artifact ≠ running process
```

Điều này cực kỳ quan trọng khi debug lỗi kiểu:

- code đã sửa nhưng server vẫn chạy `.jar` cũ
- compile bằng JDK 21 nhưng runtime chỉ có Java 17
- dependency tồn tại lúc compile nhưng thiếu lúc runtime

## Senior Notes

Senior không chỉ hỏi “code đúng không?”, mà còn hỏi:

```text
Code được compile bằng version nào?
Runtime đang dùng JVM nào?
Classpath/module path là gì?
Artifact nào thực sự được deploy?
```

Một bug Java production rất thường không nằm ở syntax mà nằm ở **environment/build/runtime mismatch**.

---

# 1. Cấu trúc chương trình Java — P0

Java tổ chức code qua:

```text
package
import
class/interface/enum/record
field
constructor
method
```

Ví dụ:

```java
package com.example.user;

import java.util.List;

public class UserService {

    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    public List<String> getUserNames() {
        return repository.findNames();
    }
}
```

## `package`

```java
package com.example.user;
```

Package dùng để:

- namespace
- tổ chức source code
- kiểm soát access ở package level

Convention phổ biến:

```text
com.company.project.feature
```

Ví dụ:

```text
com.mycompany.payment
com.mycompany.payment.service
com.mycompany.payment.repository
```

## `import`

```java
import java.util.List;
```

Cho phép dùng:

```java
List<String>
```

thay vì:

```java
java.util.List<String>
```

Wildcard:

```java
import java.util.*;
```

hợp lệ nhưng nhiều codebase tránh vì giảm độ rõ ràng.

Static import:

```java
import static java.lang.Math.PI;
import static java.lang.Math.max;
```

Sau đó:

```java
double x = PI;
int result = max(10, 20);
```

### Khi nào static import hợp lý?

Thường dùng trong test:

```java
assertEquals(expected, actual);
```

thay vì:

```java
Assertions.assertEquals(expected, actual);
```

## Language Idiom

Tên package:

```text
lowercase
```

Tên class:

```text
PascalCase
```

Tên variable/method:

```text
camelCase
```

Constant:

```text
UPPER_SNAKE_CASE
```

## Senior Notes

Đừng xem package chỉ như folder. Package là một phần của **boundary design**.

Ví dụ codebase tốt thường tránh:

```text
controller/
service/
repository/
```

cho toàn bộ hệ thống nếu project lớn, vì mọi business feature bị trộn vào nhau.

Thường tốt hơn:

```text
user/
    UserController
    UserService
    UserRepository

payment/
    PaymentController
    PaymentService
    PaymentRepository
```

Đây là bước đầu dẫn đến tư duy **package by feature**.

---

# 2. `main()` — Entry Point — P0

Java application truyền thống bắt đầu từ:

```java
public static void main(String[] args)
```

Giải thích:

```java
public
```

JVM cần truy cập method.

```java
static
```

JVM gọi method mà không cần tạo object `Main`.

```java
void
```

Không trả return value.

```java
String[] args
```

Danh sách command-line arguments.

Ví dụ:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

Run:

```bash
java Main production
```

Output:

```text
production
```

## Senior Notes

Trong Spring Boot bạn thường thấy:

```java
public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
}
```

Spring không thay thế Java entry point. Nó **bootstrap framework từ Java main()**.

---

# 3. Variables và Data Types — P0

Java là **statically typed language**.

```java
int age = 27;
String name = "Kim";
```

Compiler biết type từ compile time.

---

## 3.1 Primitive Types

Java có 8 primitive types.

```text
byte
short
int
long
float
double
char
boolean
```

### Integer

```java
byte small = 100;
short count = 20000;
int age = 27;
long population = 8_000_000_000L;
```

Literal `long` thường thêm `L`:

```java
long value = 10L;
```

### Floating point

```java
float rate = 1.5F;
double price = 19.99;
```

`double` là mặc định cho decimal literal.

### boolean

```java
boolean active = true;
boolean deleted = false;
```

### char

```java
char grade = 'A';
```

`char` dùng single quote.

String dùng double quote:

```java
String grade = "A";
```

---

## 3.2 Reference Types

Ví dụ:

```java
String name = "Alice";
User user = new User();
List<String> names = new ArrayList<>();
```

Variable chứa **reference tới object**, không phải object được nhét trực tiếp vào variable theo mental model đơn giản.

---

## 3.3 `var` — Java 10+

```java
var name = "Alice";
var count = 10;
var users = new ArrayList<User>();
```

Compiler vẫn suy luận type tại compile time.

`var` không biến Java thành dynamically typed language.

Sai:

```java
var value;
```

Compiler không biết type.

Sai:

```java
var value = null;
```

Không có type để infer.

### Language Idiom

Dùng `var` khi type đã quá rõ:

```java
var user = userRepository.findById(id);
```

Không nên dùng khi làm mất thông tin quan trọng:

```java
var result = service.execute();
```

nếu `result` là một type domain quan trọng mà người đọc cần thấy ngay.

### Senior Notes

`var` là công cụ giảm noise, không phải mục tiêu “viết code ngắn nhất”.

Rule thực tế:

> Nếu bỏ explicit type làm code khó đọc hơn, đừng dùng `var`.

---

# 4. Declaration, Assignment, `final` — P0

Declaration:

```java
int age;
```

Assignment:

```java
age = 27;
```

Initialization:

```java
int age = 27;
```

## `final`

```java
final int age = 27;
```

Không thể reassign:

```java
age = 28; // compile error
```

Với reference:

```java
final List<String> names = new ArrayList<>();
```

Không thể:

```java
names = new ArrayList<>();
```

nhưng vẫn có thể:

```java
names.add("Alice");
```

Vì `final` khóa **reference**, không tự động làm object immutable.

## Language Idiom

Ưu tiên object không thay đổi state nếu không cần.

```java
final User user = findUser();
```

Nhiều team không bắt buộc `final` cho local variable vì IDE/compiler đã giúp khá nhiều, nhưng với field dependency thì rất phổ biến:

```java
private final UserRepository repository;
```

## Programming Pattern — Prefer Immutability

Thay vì liên tục mutate:

```java
user.setName("A");
user.setAge(20);
```

thiết kế domain có thể hướng tới object bất biến hơn.

Đây sẽ là tư duy quan trọng khi học:

- thread safety
- functional programming
- record
- event-driven systems

## Senior Notes

`final` không đồng nghĩa immutable.

```java
final List<String> list
```

vẫn mutable.

Muốn immutable cần kiểm soát object/state thực sự.

---

# 5. Operators — P0

## Arithmetic

```java
+
-
*
/
%
```

Ví dụ:

```java
int total = 10 + 5;
int remainder = 10 % 3;
```

## Assignment

```java
=
+=
-=
*=
/=
%=
```

Ví dụ:

```java
count += 1;
```

## Increment / decrement

```java
count++;
count--;
```

Prefix:

```java
++count;
```

Postfix:

```java
count++;
```

Khác biệt chỉ quan trọng khi expression sử dụng value cùng lúc.

```java
int a = 1;
int b = a++;
```

Sau đó:

```text
a = 2
b = 1
```

## Comparison

```java
==
!=
>
<
>=
<=
```

## Logical

```java
&&
||
!
```

Ví dụ:

```java
if (age >= 18 && active) {
    ...
}
```

## Short-circuit evaluation

```java
user != null && user.isActive()
```

Nếu `user != null` là false, Java không gọi:

```java
user.isActive()
```

Do đó tránh `NullPointerException`.

## Ternary operator

```java
condition ? valueIfTrue : valueIfFalse
```

Ví dụ:

```java
String status = active ? "ACTIVE" : "INACTIVE";
```

### Language Idiom

Ternary tốt cho expression đơn giản.

Không nên biến nó thành nested puzzle:

```java
String status = a ? b ? "X" : "Y" : c ? "Z" : "W";
```

### Senior Notes

Ưu tiên readability hơn số dòng code.

Senior thường tránh “clever code”. Code production phải tối ưu cho **người đọc tiếp theo**, không phải cho người viết hiện tại.

---

# 6. `==` vs `equals()` — P0

Đây là một trong những chủ đề quan trọng nhất cho beginner.

Primitive:

```java
int a = 10;
int b = 10;

System.out.println(a == b); // true
```

Với object, `==` so sánh reference identity:

```java
String a = new String("hello");
String b = new String("hello");

System.out.println(a == b);      // false
System.out.println(a.equals(b)); // true
```

`equals()` thường dùng để so sánh logical value.

## Null-safe equality

Thay vì:

```java
user.getStatus().equals("ACTIVE")
```

có nguy cơ status null.

Có thể viết:

```java
"ACTIVE".equals(user.getStatus())
```

Hoặc:

```java
Objects.equals(a, b)
```

Ví dụ:

```java
Objects.equals(user1, user2);
```

`Objects.equals` xử lý null an toàn.

## Language Idiom

String/enum/domain object thường dùng `equals()` cho equality semantics.

## Programming Pattern — Value Semantics

Khi object đại diện một value:

```text
Money
Email
Coordinate
UserId
```

hai object có cùng dữ liệu thường nên được coi là equal.

Đó là nền tảng của **Value Object**.

## Design Pattern / DDD Connection — Value Object

Ví dụ:

```java
final class Money {
    private final BigDecimal amount;
    private final Currency currency;
}
```

Equality thường dựa vào `amount + currency`, không phải memory address.

## Senior Notes

Nếu override `equals()`, gần như luôn phải xem xét `hashCode()` cùng lúc.

Sai contract này có thể tạo bug rất khó hiểu trong:

```java
HashMap
HashSet
```

Phần này sẽ học kỹ hơn ở Intermediate.

---

# 7. Type Conversion / Casting — P0

## Widening conversion

Tự động:

```java
int x = 10;
long y = x;
```

## Narrowing conversion

Cần cast:

```java
double price = 19.99;
int value = (int) price;
```

Kết quả:

```text
19
```

Không rounding, chỉ mất phần decimal.

## Object casting

```java
Animal animal = new Dog();
Dog dog = (Dog) animal;
```

Sai runtime type:

```java
Animal animal = new Cat();
Dog dog = (Dog) animal;
```

→ `ClassCastException`.

## `instanceof`

```java
if (animal instanceof Dog) {
    Dog dog = (Dog) animal;
}
```

Java 16+ pattern matching:

```java
if (animal instanceof Dog dog) {
    dog.bark();
}
```

## Language Idiom

Java 16+ ưu tiên:

```java
if (obj instanceof User user) {
    ...
}
```

thay vì cast thủ công lặp lại.

## Senior Notes

Nếu code có quá nhiều:

```java
instanceof
```

và casting, có thể object model đang sai.

Polymorphism thường tốt hơn:

```java
payment.pay();
```

thay vì:

```java
if (payment instanceof CardPayment) ...
else if (payment instanceof BankPayment) ...
```

Đây là bridge sang **Strategy Pattern / Polymorphism**.

---

# 8. `if`, `else if`, `else` — P0

Syntax:

```java
if (condition) {
    ...
} else if (otherCondition) {
    ...
} else {
    ...
}
```

Ví dụ:

```java
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else {
    grade = "C";
}
```

## Guard Clause

Code beginner thường:

```java
if (user != null) {
    if (user.isActive()) {
        if (user.hasPermission()) {
            process(user);
        }
    }
}
```

Code dễ đọc hơn:

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

## Programming Pattern — Guard Clause

Guard clause giảm nesting và đưa invalid cases ra trước.

Đây là pattern rất thường gặp trong production Java.

## Senior Notes

Một method có nesting sâu 4–5 level thường là dấu hiệu cần refactor.

Senior thường tối ưu **control-flow clarity** trước khi tối ưu số dòng.

---

# 9. `switch` — P0/P1

Classic switch:

```java
switch (status) {
    case "READY":
        start();
        break;
    case "STOPPED":
        stop();
        break;
    default:
        handleUnknown();
}
```

## Fall-through

Nếu quên `break`:

```java
case "A":
    actionA();
case "B":
    actionB();
```

case A sẽ chạy tiếp action B.

Đây là nguồn bug phổ biến ở classic switch.

## Switch expression — Java 14+

```java
String message = switch (status) {
    case "READY" -> "Start";
    case "STOPPED" -> "Stop";
    default -> "Unknown";
};
```

Nhiều statements:

```java
int fee = switch (level) {
    case PREMIUM -> 0;
    case NORMAL -> 1000;
    default -> {
        log.warn("Unknown level");
        yield 2000;
    }
};
```

`yield` trả value khỏi block của switch expression.

## Language Idiom

Java 17/21 codebase thường ưu tiên arrow-style switch khi có thể.

## Senior Notes

Nếu switch tăng lên hàng chục case và mỗi case chứa business logic phức tạp, cân nhắc polymorphism/Strategy thay vì tiếp tục mở rộng switch.

---

# 10. Loops — P0

## `for`

```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

Phù hợp khi cần index.

## Enhanced for

```java
for (String name : names) {
    System.out.println(name);
}
```

Thường dùng khi chỉ cần từng element.

## `while`

```java
while (running) {
    process();
}
```

## `do-while`

```java
do {
    readInput();
} while (!valid);
```

Khác biệt: body chạy ít nhất một lần.

## `break`

```java
for (User user : users) {
    if (user.isAdmin()) {
        break;
    }
}
```

## `continue`

```java
for (User user : users) {
    if (!user.isActive()) {
        continue;
    }

    process(user);
}
```

## Language Idiom

Enhanced for thường rõ ràng hơn index loop nếu không cần index.

## Programming Pattern — Filter Early

Thay vì:

```java
for (User user : users) {
    if (user.isActive()) {
        process(user);
    }
}
```

Guard style:

```java
for (User user : users) {
    if (!user.isActive()) {
        continue;
    }

    process(user);
}
```

Đặc biệt hữu ích khi body phức tạp.

## Senior Notes

Đừng tự động thay mọi loop bằng Stream.

Loop thường tốt hơn khi:

- flow imperative phức tạp
- có `break`
- nhiều side effects
- cần debug từng step

Stream tốt khi pipeline transformation rõ ràng.

Senior chọn abstraction phù hợp, không theo trend.

---

# 11. Methods — P0

Syntax:

```java
accessModifier returnType methodName(parameters) {
    ...
}
```

Ví dụ:

```java
public int add(int a, int b) {
    return a + b;
}
```

## Parameter

```java
public User findUser(long id)
```

`id` là parameter.

Khi gọi:

```java
findUser(10L);
```

`10L` là argument.

## `return`

```java
return value;
```

Với `void`:

```java
public void validate(User user) {
    if (user == null) {
        return;
    }
}
```

## Method overloading

```java
void print(String value)
void print(int value)
void print(String value, int count)
```

Cùng tên, khác parameter list.

Không thể overload chỉ bằng return type.

Sai:

```java
int getValue()
String getValue()
```

## Varargs

```java
public int sum(int... values) {
    int total = 0;
    for (int value : values) {
        total += value;
    }
    return total;
}
```

Call:

```java
sum(1, 2, 3);
```

Bên trong `values` gần giống `int[]`.

## Language Idiom — Small Focused Methods

Method tốt thường làm một nhiệm vụ rõ ràng.

Thay vì:

```java
processUserAndSaveAndSendEmailAndLog(...)
```

nên tách:

```java
validateUser();
saveUser();
sendWelcomeEmail();
```

## Programming Pattern — Extract Method

Đây là một trong những refactoring quan trọng nhất.

Before:

```java
if (user.getName() == null || user.getName().isBlank()) {
    throw new IllegalArgumentException();
}
```

After:

```java
validateName(user);
```

## Senior Notes

Tên method nên mô tả **intent**, không mô tả implementation.

Tốt:

```java
calculateDiscount()
```

Kém hơn:

```java
loopProductsAndSubtractPrice()
```

Implementation có thể thay đổi; business intent thường ổn định hơn.

---

# 12. Java Pass-by-Value — P0

Java **luôn pass-by-value**.

Primitive:

```java
void change(int x) {
    x = 100;
}

int value = 10;
change(value);
```

`value` vẫn là `10`.

Với object, value được copy là **reference value**.

```java
void changeName(User user) {
    user.setName("New");
}
```

Object gốc bị thay đổi vì copied reference vẫn trỏ tới cùng object.

Nhưng:

```java
void replace(User user) {
    user = new User();
}
```

không thay reference của caller.

## Senior Notes

Nhiều bug và tranh luận Java bắt nguồn từ việc gọi sai “pass-by-reference”.

Mental model chính xác:

```text
Java passes copies of values.
For object variables, that value is a reference.
```

---

# 13. Arrays — P0

Declaration:

```java
int[] numbers;
```

Create:

```java
numbers = new int[3];
```

Combined:

```java
int[] numbers = new int[3];
```

Literal:

```java
int[] numbers = {10, 20, 30};
```

Access:

```java
numbers[0]
```

Length:

```java
numbers.length
```

Không phải method:

```java
numbers.length // đúng
numbers.length() // sai
```

## Common exception

```java
numbers[3]
```

với length 3 → `ArrayIndexOutOfBoundsException`.

## Utility methods

```java
Arrays.sort(numbers);
Arrays.toString(numbers);
Arrays.copyOf(numbers, newLength);
Arrays.equals(a, b);
```

## Arrays vs List

Array:

- fixed size
- primitive-friendly
- low-level hơn

List:

- dynamic size
- API phong phú hơn
- phổ biến hơn trong business code

## Senior Notes

Trong backend business code, `List<T>` thường linh hoạt hơn array.

Array vẫn quan trọng khi:

- performance-sensitive code
- byte buffers
- library API
- low-level processing

---

# 14. String — P0

`String` là một trong các class được dùng nhiều nhất Java.

```java
String name = "Alice";
```

## String immutable

```java
String value = "hello";
value.toUpperCase();
```

`value` vẫn là:

```text
hello
```

Phải assign:

```java
value = value.toUpperCase();
```

## Common methods

### `length()`

```java
name.length()
```

### `isEmpty()`

```java
name.isEmpty()
```

Chỉ kiểm tra length == 0.

### `isBlank()` — Java 11+

```java
"   ".isBlank() // true
```

### `trim()`

```java
" hello ".trim()
```

### `strip()` — Java 11+

Unicode-aware hơn `trim()`.

```java
value.strip()
```

### `contains()`

```java
text.contains("error")
```

### `startsWith()` / `endsWith()`

```java
fileName.endsWith(".csv")
```

### `substring()`

```java
String value = "ABCDEFG";
value.substring(0, 3); // ABC
```

Start inclusive, end exclusive.

### `replace()`

```java
"a-b-c".replace("-", "/")
```

### `split()`

```java
"A,B,C".split(",")
```

Lưu ý `split()` nhận **regex**.

Ví dụ dấu `.` phải escape regex:

```java
"a.b.c".split("\\.")
```

### `String.join()`

```java
String.join(",", "A", "B", "C")
```

### `formatted()` — Java 15+

```java
"Hello %s".formatted(name)
```

## Concatenation

```java
String fullName = firstName + " " + lastName;
```

Trong loop lớn, không nên nối String liên tục.

Dùng `StringBuilder`:

```java
StringBuilder sb = new StringBuilder();

for (String item : items) {
    sb.append(item).append(',');
}

String result = sb.toString();
```

## Language Idiom

Check blank input:

```java
if (name == null || name.isBlank()) {
    ...
}
```

Java 11+.

## Programming Pattern — Normalize Input at Boundary

Ví dụ:

```java
String normalizedEmail = email.strip().toLowerCase(Locale.ROOT);
```

Normalize ở boundary giúp business logic phía sau đơn giản hơn.

## Senior Notes

Tránh:

```java
password == "1234"
```

Dùng:

```java
password.equals("1234")
```

Ngoài ra, string manipulation có thể là hotspot performance nếu chạy trên lượng dữ liệu lớn; nhưng đừng tối ưu sớm nếu chưa đo.

---

# 15. Wrapper Classes và Autoboxing — P0/P1

Primitive có wrapper tương ứng:

```text
int     → Integer
long    → Long
double  → Double
boolean → Boolean
char    → Character
```

Ví dụ:

```java
Integer age = 27;
```

## Autoboxing

```java
Integer value = 10;
```

Compiler chuyển primitive `int` thành `Integer`.

## Unboxing

```java
Integer value = 10;
int x = value;
```

## Null trap

```java
Integer value = null;
int x = value;
```

→ `NullPointerException` khi unboxing.

## Parsing

```java
int age = Integer.parseInt("27");
long id = Long.parseLong("100");
double value = Double.parseDouble("1.25");
```

## Convert to String

```java
String.valueOf(123)
Integer.toString(123)
```

## Senior Notes

Dùng primitive nếu value **không được null** và không cần generic container.

Dùng wrapper khi:

- generic type (`List<Integer>`)
- nullable state thực sự có ý nghĩa
- framework/API yêu cầu object

Trong database mapping, `Integer null` và `int 0` có semantics khác nhau.

---

# 16. Classes và Objects — P0

Class là blueprint.

```java
public class User {
    String name;
    int age;
}
```

Object:

```java
User user = new User();
```

Fields:

```java
user.name = "Alice";
user.age = 27;
```

Nhưng direct public field thường không phải thiết kế tốt.

---

# 17. Constructors — P0

Constructor khởi tạo object.

```java
public class User {
    private String name;

    public User(String name) {
        this.name = name;
    }
}
```

Create:

```java
User user = new User("Alice");
```

## `this`

```java
this.name = name;
```

`this.name` = field.

`name` = parameter.

## Constructor overloading

```java
public User(String name) {
    this(name, 0);
}

public User(String name, int age) {
    this.name = name;
    this.age = age;
}
```

`this(...)` gọi constructor khác trong cùng class.

## Language Idiom

Đảm bảo object hợp lệ ngay từ constructor khi phù hợp.

```java
public User(String name) {
    if (name == null || name.isBlank()) {
        throw new IllegalArgumentException("name is required");
    }

    this.name = name;
}
```

## Programming Pattern — Constructor Injection

```java
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

Đây chính là nền tảng của **Dependency Injection** trong Spring.

## Design Pattern — Dependency Injection

Class không tự tạo dependency:

Không tốt:

```java
private UserRepository repository = new OracleUserRepository();
```

Tốt hơn:

```java
public UserService(UserRepository repository) {
    this.repository = repository;
}
```

Object bên ngoài quyết định implementation.

## Senior Notes

Constructor nên giúp tạo **valid object**, không nên chứa I/O nặng như:

- query DB
- HTTP call
- đọc file lớn

Constructor có side effect lớn làm code khó test và khó kiểm soát lifecycle.

---

# 18. Encapsulation và Access Modifiers — P0

Các access modifiers:

```text
public
protected
package-private
private
```

## `private`

Chỉ trong class.

```java
private String password;
```

## package-private

Không viết modifier:

```java
String internalValue;
```

Chỉ trong cùng package.

## `protected`

Cùng package + subclass.

## `public`

Accessible rộng nhất.

## Encapsulation

Không phải cứ field private + getter/setter là encapsulation tốt.

Ví dụ yếu:

```java
public void setBalance(BigDecimal balance) {
    this.balance = balance;
}
```

Caller có thể set số âm tùy ý.

Tốt hơn:

```java
public void withdraw(BigDecimal amount) {
    if (amount.signum() <= 0) {
        throw new IllegalArgumentException();
    }

    if (balance.compareTo(amount) < 0) {
        throw new IllegalStateException("Insufficient balance");
    }

    balance = balance.subtract(amount);
}
```

Object bảo vệ invariant của chính nó.

## Language Idiom

Expose behavior thay vì expose toàn bộ state.

## Programming Pattern — Tell, Don't Ask

Thay vì:

```java
if (account.getBalance().compareTo(amount) >= 0) {
    account.setBalance(account.getBalance().subtract(amount));
}
```

nên:

```java
account.withdraw(amount);
```

## Senior Notes

Encapsulation là kiểm soát **invariants + state transitions**, không chỉ là modifier.

Đây là tư duy quan trọng khi chuyển từ CRUD code sang domain-oriented code.

---

# 19. `static` — P0

Static member thuộc class thay vì object instance.

```java
public class MathUtils {
    public static int add(int a, int b) {
        return a + b;
    }
}
```

Call:

```java
MathUtils.add(1, 2);
```

## Static field

```java
public static final int MAX_SIZE = 100;
```

## Static block

```java
static {
    System.out.println("Class initialized");
}
```

Dùng khi class initialization cần logic, nhưng trong business code hiện đại thường nên hạn chế logic phức tạp ở static initializer.

## Language Idiom — Utility Class

```java
public final class StringUtils {

    private StringUtils() {
    }

    public static boolean isBlank(String value) {
        return value == null || value.isBlank();
    }
}
```

Private constructor ngăn tạo instance.

## Senior Notes

Static utility tốt cho function stateless nhỏ.

Nhưng quá nhiều static business logic làm giảm:

- testability
- substitutability
- dependency injection

Không nên biến toàn bộ application thành collection của static methods.

---

# 20. Inheritance — P0/P1

```java
class Animal {
    void speak() {
        System.out.println("...");
    }
}

class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("Woof");
    }
}
```

## `extends`

```java
class Dog extends Animal
```

Java class chỉ extends một class trực tiếp.

## `super`

Call parent constructor:

```java
public Dog(String name) {
    super(name);
}
```

Call parent method:

```java
super.speak();
```

## Method overriding

```java
@Override
public void speak() {
    ...
}
```

`@Override` nên luôn dùng khi override vì compiler sẽ kiểm tra.

## Language Idiom

Ưu tiên annotation:

```java
@Override
```

thay vì chỉ dựa vào signature.

## Programming Pattern — Favor Composition over Inheritance

Inheritance dễ bị lạm dụng.

Thay vì:

```java
class CsvReportService extends FileService
```

có thể tốt hơn:

```java
class CsvReportService {
    private final FileStorage storage;
}
```

## Design Pattern Connection — Template Method

Inheritance có thể hữu ích khi parent định nghĩa algorithm skeleton và subclass override step.

Tuy nhiên pattern này cần dùng có chủ ý, không phải default.

## Senior Notes

Câu hỏi trước khi `extends`:

> Subclass có thực sự là một specialization có thể thay parent theo Liskov Substitution Principle không?

Nếu chỉ muốn reuse code, composition thường an toàn hơn.

---

# 21. Polymorphism — P0

```java
Animal animal = new Dog();
animal.speak();
```

Runtime gọi implementation của `Dog`.

Đây là dynamic dispatch.

Ví dụ business:

```java
interface PaymentMethod {
    void pay(BigDecimal amount);
}
```

```java
class CardPayment implements PaymentMethod {
    @Override
    public void pay(BigDecimal amount) {
        ...
    }
}
```

```java
class BankTransferPayment implements PaymentMethod {
    @Override
    public void pay(BigDecimal amount) {
        ...
    }
}
```

Service:

```java
public void checkout(PaymentMethod paymentMethod) {
    paymentMethod.pay(totalAmount);
}
```

Service không cần biết implementation cụ thể.

## Design Pattern — Strategy

Đây chính là Strategy Pattern ở dạng đơn giản.

```java
interface DiscountStrategy {
    BigDecimal apply(BigDecimal price);
}
```

Mỗi strategy implement khác nhau.

## Senior Notes

Polymorphism giúp loại bỏ chuỗi:

```java
if type == A
else if type == B
else if type == C
```

nhưng đừng tạo interface cho mọi class chỉ vì “best practice”. Abstraction có cost. Chỉ tạo abstraction khi có **variation point** thật sự.

---

# 22. Interfaces — P0

```java
public interface UserRepository {
    User findById(long id);
}
```

Implementation:

```java
public class JdbcUserRepository implements UserRepository {
    @Override
    public User findById(long id) {
        ...
    }
}
```

## Multiple interfaces

```java
class Service implements Runnable, AutoCloseable {
    ...
}
```

## Default method — Java 8

```java
interface Logger {
    default void info(String message) {
        System.out.println(message);
    }
}
```

## Static method in interface

```java
interface Validator {
    static boolean valid(String value) {
        return value != null;
    }
}
```

## Private interface methods — Java 9+

Có thể dùng để reuse logic giữa default methods.

## Language Idiom — Program to an Interface

Field:

```java
private final List<String> names = new ArrayList<>();
```

Type declaration là:

```java
List<String>
```

không phải:

```java
ArrayList<String>
```

Điều này giảm coupling với implementation.

## Design Patterns

Interface là nền tảng của nhiều pattern:

- Strategy
- Adapter
- Decorator
- Proxy
- Repository
- Factory abstraction

## Senior Notes

Interface tốt mô tả **capability/contract**, không chỉ copy toàn bộ methods của implementation.

Tên interface kiểu:

```text
UserManagerImplInterface
```

thường là dấu hiệu thiết kế kém.

---

# 23. Abstract Classes — P1

```java
abstract class ReportGenerator {

    public final void generate() {
        loadData();
        render();
    }

    protected abstract void loadData();

    protected abstract void render();
}
```

Subclass:

```java
class CsvReportGenerator extends ReportGenerator {
    ...
}
```

## Abstract class vs interface

Interface phù hợp khi cần contract/capability.

Abstract class phù hợp khi cần:

- shared state
- protected helper logic
- partial implementation

## Design Pattern — Template Method

Ví dụ trên là Template Method:

```java
generate()
```

định nghĩa skeleton, subclass cung cấp từng step.

## Senior Notes

Nếu abstract hierarchy bắt đầu có quá nhiều level:

```text
BaseService
AbstractService
CommonService
GenericService
...
```

hãy kiểm tra lại. Deep inheritance hierarchy rất khó maintain.

---

# 24. Enum — P0/P1

Không nên dùng raw string cho fixed domain values nếu enum phù hợp.

Kém:

```java
String status = "ACTIVE";
```

Tốt hơn:

```java
enum UserStatus {
    ACTIVE,
    INACTIVE,
    SUSPENDED
}
```

Use:

```java
UserStatus status = UserStatus.ACTIVE;
```

## Enum có field/method

```java
enum OrderStatus {
    CREATED(false),
    PAID(false),
    CANCELLED(true),
    COMPLETED(true);

    private final boolean finalState;

    OrderStatus(boolean finalState) {
        this.finalState = finalState;
    }

    public boolean isFinalState() {
        return finalState;
    }
}
```

## `values()`

```java
OrderStatus.values()
```

## `valueOf()`

```java
OrderStatus.valueOf("PAID")
```

Sai value → `IllegalArgumentException`.

## Language Idiom

Đưa behavior liên quan trực tiếp vào enum nếu logic nhỏ và ổn định.

## Programming Pattern — Replace Magic Strings with Enum

Thay:

```java
if ("ACTIVE".equals(status))
```

bằng:

```java
if (status == UserStatus.ACTIVE)
```

Với enum, dùng `==` là hợp lệ và phổ biến.

## Design Pattern Connection — State

Enum có thể là bước đầu của state handling. Khi state behavior trở nên phức tạp, có thể tiến tới State Pattern.

## Senior Notes

Đừng serialize/persist `enum.ordinal()` vào DB nếu schema cần ổn định. Thay đổi order enum có thể phá data semantics.

Ưu tiên explicit code/string representation.

---

# 25. Records — Java 16+ — P1

Record phù hợp cho data carrier.

```java
public record UserResponse(
    long id,
    String name,
    String email
) {}
```

Compiler tự sinh nhiều boilerplate:

- constructor
- accessor
- `equals()`
- `hashCode()`
- `toString()`

Use:

```java
UserResponse user = new UserResponse(1L, "Alice", "a@example.com");

user.id();
user.name();
```

Không dùng getter kiểu JavaBean:

```java
user.getName()
```

mặc định record accessor là:

```java
user.name()
```

## Compact constructor

```java
public record UserRequest(String name) {
    public UserRequest {
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("name required");
        }
    }
}
```

## Language Idiom

Record rất hợp cho:

- DTO
- API response/request model
- value-like data
- immutable data carriers

## Senior Notes

Record không phải “entity replacement” tự động.

Đừng dùng record chỉ vì ít boilerplate nếu object cần lifecycle/mutable identity phức tạp.

---

# 26. Exceptions — P0

Exception biểu diễn abnormal flow.

```java
try {
    process();
} catch (Exception e) {
    handle(e);
}
```

## Checked Exception

Subclass của `Exception` nhưng không phải `RuntimeException`.

Ví dụ:

```java
IOException
SQLException
```

Compiler bắt buộc handle hoặc declare.

```java
public void read() throws IOException {
    ...
}
```

## Unchecked Exception

Subclass của `RuntimeException`.

Ví dụ:

```java
NullPointerException
IllegalArgumentException
IllegalStateException
```

Không bắt buộc declare.

## `throw`

```java
throw new IllegalArgumentException("Invalid age");
```

## `throws`

```java
public void readFile() throws IOException
```

Khai báo method có thể propagate exception.

## `finally`

```java
try {
    ...
} finally {
    cleanup();
}
```

`finally` thường chạy bất kể success/failure.

## Try-with-resources — Java 7+

```java
try (BufferedReader reader = Files.newBufferedReader(path)) {
    return reader.readLine();
}
```

Resource implement `AutoCloseable` sẽ được close tự động.

## Language Idiom — Fail Fast

Validate sớm:

```java
if (id <= 0) {
    throw new IllegalArgumentException("id must be positive");
}
```

## Programming Pattern — Exception Translation

Low-level:

```java
SQLException
```

có thể được translate thành domain/application exception:

```java
throw new UserPersistenceException("Failed to save user", e);
```

Framework như Spring làm rất nhiều exception translation.

## Senior Notes

Không catch `Exception` chỉ để nuốt lỗi:

```java
try {
    process();
} catch (Exception e) {
}
```

Đây là anti-pattern rất nguy hiểm.

Cũng tránh:

```java
catch (Exception e) {
    return null;
}
```

vì mất root cause.

Exception nên có:

- meaningful type
- useful message
- preserved cause

```java
throw new MyException("context", e);
```

---

# 27. Null và `NullPointerException` — P0

```java
User user = null;
user.getName();
```

→ `NullPointerException`.

## `Objects.requireNonNull`

```java
this.repository = Objects.requireNonNull(repository);
```

Có message:

```java
Objects.requireNonNull(repository, "repository must not be null");
```

## Null check

```java
if (user == null) {
    return;
}
```

## Language Idiom

Nếu method không cho phép null, fail fast.

Nếu null là valid business state, document/represent rõ ràng.

## Senior Notes

Một codebase có rất nhiều null thường khó reason.

Các chiến lược giảm null:

- constructor validation
- empty collection thay vì null list
- Optional ở return boundary phù hợp
- value objects
- non-null conventions

Ví dụ tốt:

```java
return Collections.emptyList();
```

thay vì:

```java
return null;
```

cho method trả danh sách.

---

# 28. Collections Framework — P0

Collections là phần quan trọng nhất của `java.util` đối với business code.

Mental model:

```text
Collection
├── List
├── Set
└── Queue

Map  // riêng, không extends Collection
```

---

## 28.1 `List`

Ordered collection, cho phép duplicate.

```java
List<String> names = new ArrayList<>();
```

Common methods:

```java
names.add("Alice");
names.get(0);
names.set(0, "Bob");
names.remove("Alice");
names.size();
names.isEmpty();
names.contains("Bob");
```

### `ArrayList`

Default choice cho đa số List business use case.

```java
List<User> users = new ArrayList<>();
```

Tốt cho:

- random access
- append
- iteration

### `LinkedList`

Có API List/Deque, nhưng không phải default replacement cho ArrayList.

Trong application code thông thường, `ArrayList` thường là default tốt hơn.

## Language Idiom

Declare interface:

```java
List<String> names = new ArrayList<>();
```

không phải:

```java
ArrayList<String> names = new ArrayList<>();
```

## Senior Notes

Đừng chọn collection theo tên nghe “nhanh”. Chọn theo access pattern.

---

## 28.2 `Set`

Không cho duplicate theo equality semantics.

```java
Set<String> emails = new HashSet<>();
```

Methods:

```java
add
remove
contains
size
isEmpty
```

### `HashSet`

Default Set khi không cần ordering.

### `LinkedHashSet`

Giữ insertion order.

### `TreeSet`

Sorted set.

## Programming Pattern — De-duplication

```java
Set<String> uniqueEmails = new HashSet<>(emails);
```

## Senior Notes

Set uniqueness phụ thuộc `equals/hashCode`.

Nếu domain object implement sai equality, Set sẽ hoạt động “sai” theo business expectation.

---

## 28.3 `Map`

Key-value structure.

```java
Map<Long, User> userById = new HashMap<>();
```

### `put()`

```java
userById.put(user.getId(), user);
```

### `get()`

```java
User user = userById.get(id);
```

Không có key thường trả `null`.

### `getOrDefault()`

```java
int count = counts.getOrDefault(key, 0);
```

### `containsKey()`

```java
if (userById.containsKey(id)) {
    ...
}
```

### `putIfAbsent()`

```java
map.putIfAbsent(key, value);
```

### `computeIfAbsent()`

Rất quan trọng:

```java
Map<String, List<User>> usersByTeam = new HashMap<>();

usersByTeam
    .computeIfAbsent(teamName, k -> new ArrayList<>())
    .add(user);
```

Thay cho:

```java
if (!usersByTeam.containsKey(teamName)) {
    usersByTeam.put(teamName, new ArrayList<>());
}
usersByTeam.get(teamName).add(user);
```

### `merge()`

Đếm:

```java
Map<String, Integer> counts = new HashMap<>();

counts.merge(word, 1, Integer::sum);
```

### Iterate

Tốt nhất khi cần key + value:

```java
for (Map.Entry<Long, User> entry : userById.entrySet()) {
    Long id = entry.getKey();
    User user = entry.getValue();
}
```

## Language Idiom

`computeIfAbsent()` và `merge()` là idioms rất hữu ích cho grouping/counting.

## Programming Patterns

### Indexing Pattern

Chuyển list thành map để lookup nhanh:

```java
Map<Long, User> byId = new HashMap<>();
for (User user : users) {
    byId.put(user.getId(), user);
}
```

### Grouping Pattern

```java
Map<String, List<User>> byTeam = new HashMap<>();
```

## Senior Notes

Đừng gọi nhiều lần:

```java
map.get(key)
```

nếu có thể lưu local variable cho clarity.

Và đừng dùng mutable object làm HashMap key nếu equality/hash có thể thay đổi sau insertion.

---

# 29. Collection Factory Methods — Java 9+ — P0/P1

```java
List.of("A", "B", "C")
Set.of("A", "B")
Map.of("A", 1, "B", 2)
```

Các collection này không cho structural modification.

```java
List<String> names = List.of("A", "B");
names.add("C"); // UnsupportedOperationException
```

## Copy factory

```java
List.copyOf(existingList)
Set.copyOf(existingSet)
Map.copyOf(existingMap)
```

## Language Idiom

Dùng immutable factory cho constants/input không cần mutate:

```java
private static final Set<String> SUPPORTED_TYPES =
    Set.of("PDF", "CSV", "TXT");
```

## Senior Notes

Immutable collection giúp giảm accidental mutation và làm ownership rõ hơn.

Nhưng `List.of(...)` không biến các object bên trong thành immutable.

---

# 30. Generics — Beginner Core — P0

Không generics:

```java
List list = new ArrayList();
list.add("hello");
list.add(123);
```

Phải cast và dễ lỗi runtime.

Generics:

```java
List<String> names = new ArrayList<>();
```

Compiler đảm bảo element type.

## Generic class

```java
class Box<T> {
    private T value;

    public T get() {
        return value;
    }

    public void set(T value) {
        this.value = value;
    }
}
```

Use:

```java
Box<String> box = new Box<>();
```

## Generic method

```java
public static <T> T first(List<T> values) {
    return values.get(0);
}
```

## Diamond operator

```java
new ArrayList<>()
```

không cần:

```java
new ArrayList<String>()
```

## Wildcards — awareness

```java
List<?> values
```

Upper bound:

```java
List<? extends Number>
```

Lower bound:

```java
List<? super Integer>
```

Chi tiết PECS nên để Intermediate, nhưng beginner cần nhận biết syntax.

## Senior Notes

Generics chuyển nhiều lỗi từ runtime sang compile time.

Nếu code đang dùng raw type:

```java
List list
Map map
```

đó thường là legacy hoặc code chưa type-safe.

---

# 31. `Object` methods — P0/P1

Mọi class Java trực tiếp/gián tiếp kế thừa `Object`.

Các methods quan trọng:

```java
toString()
equals(Object)
hashCode()
getClass()
```

## `toString()`

Dùng để representation/debug/logging.

```java
@Override
public String toString() {
    return "User{id=" + id + ", name='" + name + "'}";
}
```

## `equals()` / `hashCode()`

Nếu logical equality quan trọng, cần implement đúng contract.

## Senior Notes

Không đưa secret vào `toString()`:

```text
password
access token
secret key
PII không cần thiết
```

Log leakage là security issue thật.

---

# 32. Lambdas — Java 8 — P0/P1

Lambda biểu diễn function-like behavior cho functional interface.

```java
(a, b) -> a + b
```

Ví dụ:

```java
List<String> names = List.of("Bob", "Alice");

names.forEach(name -> System.out.println(name));
```

## Syntax variants

Một parameter:

```java
name -> name.length()
```

Nhiều parameter:

```java
(a, b) -> a + b
```

Block:

```java
value -> {
    log(value);
    return value.length();
}
```

## Functional Interface

Interface có một abstract method.

```java
@FunctionalInterface
interface Calculator {
    int calculate(int a, int b);
}
```

Use:

```java
Calculator add = (a, b) -> a + b;
```

## Standard functional interfaces

### `Predicate<T>`

```java
T -> boolean
```

```java
Predicate<User> active = user -> user.isActive();
```

### `Function<T, R>`

```java
T -> R
```

```java
Function<User, String> getName = user -> user.getName();
```

### `Consumer<T>`

```java
T -> void
```

```java
Consumer<String> print = value -> System.out.println(value);
```

### `Supplier<T>`

```java
() -> T
```

```java
Supplier<User> createUser = () -> new User();
```

## Language Idiom — Method Reference

Lambda:

```java
name -> System.out.println(name)
```

Method reference:

```java
System.out::println
```

Lambda:

```java
user -> user.getName()
```

Method reference:

```java
User::getName
```

## Design Pattern — Strategy with Lambda

```java
Comparator<User> comparator =
    (a, b) -> a.getName().compareTo(b.getName());
```

Lambda giúp Strategy nhỏ không cần tạo class riêng.

## Senior Notes

Lambda tốt khi behavior ngắn và rõ.

Nếu lambda dài 20–30 dòng, hãy extract thành named method/class.

---

# 33. Stream API — Beginner Core — P0/P1

Stream xử lý data theo pipeline.

```text
source
  ↓
intermediate operations
  ↓
terminal operation
```

Ví dụ:

```java
List<String> activeNames = users.stream()
    .filter(User::isActive)
    .map(User::getName)
    .toList();
```

`toList()` có từ Java 16.

Java 8:

```java
.collect(Collectors.toList())
```

## `stream()`

```java
users.stream()
```

Tạo stream từ collection.

## `filter()`

```java
.filter(user -> user.isActive())
```

Giữ lại element thỏa predicate.

## `map()`

```java
.map(User::getName)
```

Transform `User → String`.

## `sorted()`

```java
.sorted()
```

Custom:

```java
.sorted(Comparator.comparing(User::getName))
```

## `distinct()`

```java
.distinct()
```

Dựa vào equality.

## `limit()`

```java
.limit(10)
```

## `skip()`

```java
.skip(10)
```

## Terminal operations

### `forEach()`

```java
.forEach(System.out::println)
```

### `count()`

```java
long count = users.stream()
    .filter(User::isActive)
    .count();
```

### `findFirst()`

```java
Optional<User> first = users.stream().findFirst();
```

### `anyMatch()`

```java
boolean hasAdmin = users.stream()
    .anyMatch(User::isAdmin);
```

### `allMatch()`

```java
boolean allActive = users.stream()
    .allMatch(User::isActive);
```

### `noneMatch()`

```java
boolean noBlocked = users.stream()
    .noneMatch(User::isBlocked);
```

### `collect()`

Java 8:

```java
List<String> names = users.stream()
    .map(User::getName)
    .collect(Collectors.toList());
```

Java 16+:

```java
List<String> names = users.stream()
    .map(User::getName)
    .toList();
```

## Language Idiom — Transformation Pipeline

```java
users.stream()
    .filter(User::isActive)
    .map(User::getEmail)
    .filter(Objects::nonNull)
    .distinct()
    .toList();
```

Đọc gần như business sentence.

## Programming Pattern — Filter → Map → Collect

Đây là pipeline cực kỳ phổ biến:

```text
lọc dữ liệu
→ biến đổi
→ gom kết quả
```

## Senior Notes

Tránh side effect trong Stream nếu không cần:

```java
users.stream()
    .map(user -> {
        database.save(user); // suspicious
        return user;
    })
```

Stream mạnh nhất khi transformation gần với pure functions.

Không dùng `parallelStream()` chỉ vì nghĩ nó sẽ nhanh hơn. Parallelism có overhead và correctness concerns.

---

# 34. Optional — Java 8 — P1

Optional biểu diễn “có thể có value hoặc không”.

```java
Optional<User> findById(long id)
```

## `Optional.of()`

Không chấp nhận null.

```java
Optional.of(user)
```

## `Optional.ofNullable()`

```java
Optional.ofNullable(user)
```

Cho phép null input.

## `Optional.empty()`

```java
Optional.empty()
```

## `isPresent()`

```java
if (user.isPresent()) {
    ...
}
```

## `ifPresent()`

```java
user.ifPresent(this::process);
```

## `orElse()`

```java
User result = optional.orElse(defaultUser);
```

Default expression được evaluate ngay.

## `orElseGet()`

```java
User result = optional.orElseGet(this::createDefaultUser);
```

Lazy supplier.

## `orElseThrow()`

```java
User user = repository.findById(id)
    .orElseThrow(() -> new UserNotFoundException(id));
```

## `map()`

```java
Optional<String> name = optionalUser.map(User::getName);
```

## `filter()`

```java
optionalUser.filter(User::isActive)
```

## Language Idiom

Repository lookup:

```java
return repository.findById(id)
    .orElseThrow(() -> new UserNotFoundException(id));
```

rất phổ biến trong Spring application code.

## Senior Notes

Optional thường tốt ở **return type**.

Không mặc định dùng Optional cho:

- field
- method parameter
- DTO properties

trừ khi framework/design có lý do rõ ràng.

Cũng tránh:

```java
optional.get()
```

nếu chưa kiểm tra present. `orElseThrow`, `map`, `ifPresent` thường thể hiện intent tốt hơn.

---

# 35. Sorting và Comparator — P0/P1

Natural ordering qua `Comparable`.

```java
class User implements Comparable<User> {
    @Override
    public int compareTo(User other) {
        return this.name.compareTo(other.name);
    }
}
```

Nhưng business code thường dùng `Comparator` linh hoạt hơn.

```java
users.sort(Comparator.comparing(User::getName));
```

Descending:

```java
users.sort(
    Comparator.comparing(User::getName).reversed()
);
```

Multiple fields:

```java
Comparator<User> comparator =
    Comparator.comparing(User::getDepartment)
        .thenComparing(User::getName);
```

Null handling:

```java
Comparator.comparing(
    User::getName,
    Comparator.nullsLast(String::compareTo)
)
```

## Language Idiom

```java
Comparator.comparing(...)
    .thenComparing(...)
```

là idiom nên nhớ thay vì tự viết comparator dài.

## Design Pattern — Strategy

Comparator chính là một Strategy cho ordering.

## Senior Notes

Sorting large collections có cost. Nếu data đến từ DB, đôi khi nên sort ở SQL thay vì load toàn bộ rồi sort trong Java — tùy use case và pagination semantics.

---

# 36. Date/Time API — `java.time` — P0

Java 8 giới thiệu modern Date/Time API.

Tránh ưu tiên legacy:

```text
java.util.Date
java.util.Calendar
SimpleDateFormat
```

cho code mới nếu không bị API cũ bắt buộc.

## `LocalDate`

Date không timezone/time.

```java
LocalDate today = LocalDate.now();
LocalDate birthday = LocalDate.of(2000, 7, 26);
```

## `LocalTime`

```java
LocalTime now = LocalTime.now();
```

## `LocalDateTime`

```java
LocalDateTime now = LocalDateTime.now();
```

Không mang timezone.

## `Instant`

Machine timestamp UTC-oriented.

```java
Instant now = Instant.now();
```

## `ZonedDateTime`

Có timezone.

```java
ZonedDateTime seoul = ZonedDateTime.now(
    ZoneId.of("Asia/Seoul")
);
```

## Add/subtract

```java
date.plusDays(1)
date.minusMonths(1)
```

Immutable: method trả object mới.

## Compare

```java
date1.isBefore(date2)
date1.isAfter(date2)
date1.isEqual(date2)
```

## Formatting

```java
DateTimeFormatter formatter =
    DateTimeFormatter.ofPattern("yyyy-MM-dd");

String value = date.format(formatter);
```

Parse:

```java
LocalDate date = LocalDate.parse("2026-09-07");
```

Custom:

```java
LocalDate.parse("07/09/2026", formatter);
```

## Duration vs Period

`Duration`: time-based.

```java
Duration.between(start, end)
```

`Period`: date-based.

```java
Period.between(date1, date2)
```

## Language Idiom

Dùng `Instant` cho timestamp kỹ thuật/event time khi phù hợp.

Dùng `LocalDate` cho business date không cần timezone.

## Senior Notes

`LocalDateTime` không mang timezone. Đây là nguồn bug rất phổ biến khi hệ thống chạy nhiều region.

Phải phân biệt:

```text
business local date/time
vs
absolute point in time
```

---

# 37. BigDecimal — P0 cho backend/business

Không dùng `double` cho money nếu cần decimal precision nghiêm túc.

```java
double value = 0.1 + 0.2;
```

Floating-point không đảm bảo decimal representation chính xác theo cách con người thường kỳ vọng.

Dùng:

```java
BigDecimal amount = new BigDecimal("19.99");
```

Tránh:

```java
new BigDecimal(0.1)
```

Ưu tiên:

```java
new BigDecimal("0.1")
```

hoặc:

```java
BigDecimal.valueOf(0.1)
```

## Operations

```java
amount.add(other)
amount.subtract(other)
amount.multiply(other)
amount.divide(other)
```

BigDecimal immutable.

Sai:

```java
amount.add(other);
```

rồi nghĩ `amount` đã đổi.

Đúng:

```java
amount = amount.add(other);
```

## Comparison

Không dùng `>`.

```java
amount.compareTo(other)
```

Kết quả:

```text
< 0
= 0
> 0
```

Ví dụ:

```java
if (amount.compareTo(BigDecimal.ZERO) > 0) {
    ...
}
```

## Scale / rounding

```java
amount.setScale(2, RoundingMode.HALF_UP)
```

## Senior Notes

`equals()` của BigDecimal xét cả scale:

```java
new BigDecimal("1.0").equals(new BigDecimal("1.00"))
```

có thể false.

Trong business numeric comparison thường cần cân nhắc:

```java
compareTo() == 0
```

rather than `equals()`.

---

# 38. File I/O — Beginner — P1

Modern API ưu tiên `java.nio.file`.

## `Path`

```java
Path path = Path.of("data/users.txt");
```

`Path.of` Java 11+.

Java 8:

```java
Paths.get("data/users.txt")
```

## Check existence

```java
Files.exists(path)
Files.notExists(path)
```

## Read String — Java 11+

```java
String content = Files.readString(path);
```

## Write String — Java 11+

```java
Files.writeString(path, content);
```

## Read lines

```java
List<String> lines = Files.readAllLines(path);
```

## Copy

```java
Files.copy(source, target);
```

Replace:

```java
Files.copy(
    source,
    target,
    StandardCopyOption.REPLACE_EXISTING
);
```

## Move

```java
Files.move(source, target);
```

## Delete

```java
Files.delete(path);
```

Nếu không tồn tại → exception.

```java
Files.deleteIfExists(path);
```

## Create directories

```java
Files.createDirectories(path);
```

Tạo cả parent directories cần thiết.

## Language Idiom — try-with-resources

Stream lines:

```java
try (Stream<String> lines = Files.lines(path)) {
    lines.forEach(System.out::println);
}
```

## Senior Notes

`readAllLines()` / `readString()` load toàn bộ file vào memory.

File lớn cần streaming.

Đây là điểm quan trọng về memory profile.

---

# 39. Input/Output Streams — P1

Byte streams:

```text
InputStream
OutputStream
```

Character streams:

```text
Reader
Writer
```

## Byte example

```java
try (InputStream in = Files.newInputStream(path)) {
    byte[] buffer = new byte[8192];
    int read;

    while ((read = in.read(buffer)) != -1) {
        ...
    }
}
```

## BufferedReader

```java
try (BufferedReader reader = Files.newBufferedReader(path)) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
}
```

## Language Idiom

Always close closeable resources bằng try-with-resources nếu ownership thuộc method hiện tại.

## Design Pattern — Decorator

Java I/O classic API là ví dụ nổi tiếng của Decorator:

```java
new BufferedInputStream(
    new FileInputStream(file)
)
```

Wrapper bổ sung behavior lên stream khác.

## Senior Notes

Cần hiểu resource ownership:

> Ai mở resource thì ai chịu trách nhiệm close?

Sai ownership dễ gây connection/file descriptor leak.

---

# 40. Packages, Access và Project Structure — P1

Một beginner nên quen cấu trúc:

```text
src/
  main/
    java/
      com/example/app/
        Application.java
        user/
          User.java
          UserService.java
```

Maven sau này thường là:

```text
src/main/java
src/main/resources
src/test/java
```

## Senior Note — Package by Feature

Feature-oriented:

```text
user/
payment/
order/
```

thường scale tốt hơn giant technical layers nếu domain lớn.

---

# 41. Annotations — Beginner Awareness — P1

Annotation thêm metadata.

```java
@Override
```

```java
@Deprecated
```

```java
@SuppressWarnings("unchecked")
```

## `@Override`

Compiler check override correctness.

## `@Deprecated`

API không còn được khuyến nghị.

## `@SuppressWarnings`

Chặn warning cụ thể, nhưng không dùng để “tắt warning cho sạch”.

## Custom annotation

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Audited {
}
```

Beginner chỉ cần nhận biết. Reflection/framework processing học sâu hơn ở Intermediate/Senior.

## Senior Notes

Spring dùng annotation rất mạnh:

```text
@Component
@Service
@Repository
@Transactional
@GetMapping
```

Nhưng annotation bản thân không “có phép thuật”; framework dùng reflection/proxy/scanning để đọc metadata và thực thi behavior.

---

# 42. Immutability — P1

Object immutable không thay state sau khi tạo.

Ví dụ:

```java
public final class UserId {
    private final long value;

    public UserId(long value) {
        if (value <= 0) {
            throw new IllegalArgumentException();
        }
        this.value = value;
    }

    public long value() {
        return value;
    }
}
```

## Why useful?

- dễ reason
- ít side effect
- thread-safe hơn theo bản chất
- làm key/value object tốt

## Language Idiom

Immutable-by-default là mindset tốt khi không cần mutation.

## Design Pattern / DDD — Value Object

Object như:

```text
Money
UserId
Email
Address
```

thường phù hợp value object và immutability.

## Senior Notes

Immutable object vẫn có thể chứa mutable member:

```java
private final List<String> roles;
```

Nếu constructor giữ reference trực tiếp:

```java
this.roles = roles;
```

caller vẫn mutate được.

Defensive copy:

```java
this.roles = List.copyOf(roles);
```

---

# 43. Defensive Copy — P1

Problem:

```java
public class User {
    private final List<String> roles;

    public User(List<String> roles) {
        this.roles = roles;
    }
}
```

Caller:

```java
List<String> roles = new ArrayList<>();
User user = new User(roles);

roles.add("ADMIN");
```

State của `user` bị thay đổi gián tiếp.

Better:

```java
this.roles = List.copyOf(roles);
```

Getter:

```java
public List<String> getRoles() {
    return roles;
}
```

safe hơn nếu roles đã immutable.

## Programming Pattern — Defensive Copy

Copy mutable input/output tại object boundary để bảo vệ ownership.

## Senior Notes

Đây là một chi tiết nhỏ nhưng rất quan trọng trong API design và concurrent systems.

---

# 44. Basic Error Handling Pattern — P0/P1

Một flow backend điển hình:

```java
public User getUser(long id) {
    if (id <= 0) {
        throw new IllegalArgumentException("invalid id");
    }

    return repository.findById(id)
        .orElseThrow(() -> new UserNotFoundException(id));
}
```

Các lớp lỗi khác nhau:

```text
invalid input
not found
business rule violation
infrastructure failure
programming bug
```

## Programming Pattern — Separate Error Categories

Đừng biến tất cả thành:

```java
throw new Exception("error");
```

Type cụ thể giúp caller/framework xử lý đúng.

## Senior Notes

Exception taxonomy tốt giúp:

- HTTP mapping
- logging severity
- retry decision
- transaction rollback
- alerting

Spring sẽ làm rõ hơn chủ đề này.

---

# 45. Basic API Design — P1

Method API tốt nên:

- tên rõ nghĩa
- parameter tối thiểu cần thiết
- return type có semantics rõ
- predictable null behavior
- validate input

Kém:

```java
Object process(Object a, Object b, int type)
```

Tốt hơn:

```java
PaymentResult processPayment(
    PaymentRequest request,
    PaymentMethod method
)
```

## Language Idiom — Strong Types

Thay raw primitive/string có thể cân nhắc type domain.

Raw:

```java
void transfer(String from, String to, BigDecimal amount)
```

Domain-oriented:

```java
void transfer(
    AccountId from,
    AccountId to,
    Money amount
)
```

## Senior Notes

“Make invalid states unrepresentable” là mục tiêu tốt, dù không phải lúc nào Java cũng đạt tuyệt đối.

Strong types giảm class bug do parameter bị đảo hoặc string sai format.

---

# 46. Basic Design Patterns Beginner Nên Nhận Biết

Mục tiêu beginner **không phải thuộc lòng GoF**, mà nhận biết pattern đang tự nhiên xuất hiện trong Java.

---

## 46.1 Strategy Pattern — P0/P1

Khi một behavior có nhiều implementation.

```java
interface DiscountStrategy {
    BigDecimal calculate(BigDecimal amount);
}
```

```java
class VipDiscount implements DiscountStrategy {
    public BigDecimal calculate(BigDecimal amount) {
        return amount.multiply(new BigDecimal("0.9"));
    }
}
```

Service:

```java
class PriceService {
    private final DiscountStrategy strategy;

    PriceService(DiscountStrategy strategy) {
        this.strategy = strategy;
    }
}
```

### Senior Note

Đừng tạo Strategy nếu chỉ có một behavior cố định và không có variation point thật.

---

## 46.2 Factory — P1

Centralize object creation.

```java
public class PaymentFactory {

    public PaymentMethod create(PaymentType type) {
        return switch (type) {
            case CARD -> new CardPayment();
            case BANK -> new BankPayment();
        };
    }
}
```

### Khi hữu ích

Object creation phụ thuộc type/configuration và caller không nên biết implementation.

### Senior Note

Spring container chính là một object factory/container cực mạnh ở cấp framework.

---

## 46.3 Builder — P1

Hữu ích khi object có nhiều optional fields.

```java
User user = User.builder()
    .name("Alice")
    .email("a@example.com")
    .age(27)
    .build();
```

Java không có built-in builder syntax; thường tự code hoặc library sinh.

### Senior Note

Builder tốt cho complex construction nhưng có thể overkill với record/constructor chỉ 2–3 field.

---

## 46.4 Iterator — P1

Enhanced for dựa trên iteration abstraction.

```java
for (User user : users) {
    ...
}
```

Underlying concept:

```java
Iterator<User> iterator = users.iterator();
```

### Senior Note

Hiểu Iterator giúp hiểu Collections và fail-fast behavior sau này.

---

## 46.5 Decorator — P2 Beginner Awareness

Ví dụ Java I/O:

```java
BufferedInputStream
    → wraps InputStream
```

Decorator thêm behavior mà không thay interface chính.

Spring Security/filter chains cũng sẽ có nhiều concept gần kiểu composition/decorator chain.

---

## 46.6 Repository Pattern — P1

Không phải GoF classic nhưng cực quan trọng trong backend.

```java
interface UserRepository {
    Optional<User> findById(long id);
    void save(User user);
}
```

Business service không cần biết DB details.

### Senior Note

Repository abstraction không đồng nghĩa mỗi table phải có một repository máy móc. Repository nên phản ánh aggregate/domain access boundary phù hợp.

---

# 47. Common Java Language Idioms Beginner Nên Thuộc

## Idiom 1 — Interface on the left

```java
List<String> list = new ArrayList<>();
Map<String, User> map = new HashMap<>();
```

---

## Idiom 2 — Guard clauses

```java
if (request == null) {
    throw new IllegalArgumentException();
}
```

---

## Idiom 3 — Try-with-resources

```java
try (InputStream in = ...) {
    ...
}
```

---

## Idiom 4 — `Objects.equals`

```java
Objects.equals(a, b)
```

---

## Idiom 5 — `Objects.requireNonNull`

```java
this.repository = Objects.requireNonNull(repository);
```

---

## Idiom 6 — Collection empty instead of null

```java
return List.of();
```

thay vì:

```java
return null;
```

---

## Idiom 7 — Enum instead of magic strings

```java
OrderStatus.PAID
```

---

## Idiom 8 — `Comparator.comparing`

```java
users.sort(Comparator.comparing(User::getName));
```

---

## Idiom 9 — `computeIfAbsent`

```java
map.computeIfAbsent(key, k -> new ArrayList<>()).add(value);
```

---

## Idiom 10 — Stream filter/map pipeline

```java
users.stream()
    .filter(User::isActive)
    .map(User::getName)
    .toList();
```

---

## Idiom 11 — `Optional.orElseThrow`

```java
repository.findById(id)
    .orElseThrow(() -> new UserNotFoundException(id));
```

---

## Idiom 12 — Constructor injection

```java
public Service(Repository repository) {
    this.repository = repository;
}
```

---

# 48. Coding / Programming Patterns Beginner Nên Luyện

## 48.1 Guard Clause

```text
invalid case → return/throw early
happy path → giữ thẳng và dễ đọc
```

---

## 48.2 Extract Method

Large method → chia theo meaningful intent.

---

## 48.3 Normalize at Boundary

```java
email = email.strip().toLowerCase(Locale.ROOT);
```

---

## 48.4 Validate Early

```java
if (amount.signum() <= 0) {
    throw ...;
}
```

---

## 48.5 Prefer Immutable Data

Dữ liệu không cần đổi → không cho đổi.

---

## 48.6 Defensive Copy

Mutable collection/object đi qua boundary → cân nhắc copy.

---

## 48.7 Map for Lookup

Nếu code liên tục scan list để tìm theo id:

```java
for (...) {
    if (user.getId() == id) ...
}
```

nhiều lần, cân nhắc build:

```java
Map<Long, User>
```

---

## 48.8 Set for Uniqueness

Không tự viết logic duplicate bằng nested loop nếu Set mô hình hóa đúng requirement.

---

## 48.9 Separate Transformation from Side Effects

Transformation:

```java
map/filter
```

Side effects:

```text
DB write
HTTP call
file write
logging
```

Cố giữ ranh giới rõ khi có thể.

---

# 49. Common Beginner Anti-patterns

## 49.1 So sánh String bằng `==`

Sai:

```java
status == "ACTIVE"
```

Đúng:

```java
"ACTIVE".equals(status)
```

---

## 49.2 Catch exception rồi bỏ qua

```java
catch (Exception e) {
}
```

Không làm vậy.

---

## 49.3 Return null cho collection

Tránh:

```java
return null;
```

Ưu tiên:

```java
return List.of();
```

---

## 49.4 Dùng `double` cho money

Dùng `BigDecimal` khi precision decimal quan trọng.

---

## 49.5 Getter/setter cho mọi field mà không có invariant

Object trở thành data bag và business rule nằm rải rác ngoài object.

---

## 49.6 Giant method

```java
process()
```

500 dòng → gần như chắc chắn nên refactor.

---

## 49.7 Giant `if/else` theo type

Có thể cần polymorphism/Strategy.

---

## 49.8 Dùng implementation type ở mọi nơi

```java
ArrayList<User>
```

thay vì:

```java
List<User>
```

khi caller chỉ cần List contract.

---

## 49.9 Mutable static global state

```java
public static List<User> users = new ArrayList<>();
```

rất dễ tạo race condition, hidden coupling, test contamination.

---

## 49.10 Overengineering

Không phải mọi class cần:

```text
interface
factory
builder
strategy
abstract base class
```

Chỉ tạo abstraction khi complexity/variation thực sự cần.

---

# 50. Java Version Delta Beginner Cần Nắm

Đây không phải toàn bộ feature history; chỉ là các thay đổi beginner nên biết.

---

## Java 8

Cực kỳ quan trọng:

```text
Lambda
Stream API
Optional
java.time
Default methods in interface
Method references
```

Nếu làm enterprise Java, Java 8 concepts vẫn là nền tảng bắt buộc.

---

## Java 9

Beginner awareness:

```text
List.of / Set.of / Map.of
private interface methods
module system
```

Module system để Intermediate.

---

## Java 10

```java
var
```

local variable type inference.

---

## Java 11

Các API rất thực dụng:

```java
String.isBlank()
String.strip()
String.lines()
String.repeat()
Files.readString()
Files.writeString()
```

Java 11 cũng có standard HTTP Client, học sâu ở Intermediate.

---

## Java 14

Switch expression trở thành standard:

```java
var text = switch (status) {
    case ACTIVE -> "active";
    default -> "other";
};
```

---

## Java 15

Text blocks:

```java
String json = """
    {
      "name": "Alice"
    }
    """;
```

Rất hữu ích cho:

- JSON
- SQL
- HTML snippets
- test data

---

## Java 16

### Record

```java
record UserDto(long id, String name) {}
```

### Pattern matching for `instanceof`

```java
if (obj instanceof User user) {
    ...
}
```

### Stream `.toList()`

```java
stream.toList()
```

---

## Java 17

### Sealed classes

Beginner chỉ cần nhận biết:

```java
sealed interface Payment
    permits CardPayment, BankPayment {
}
```

Kiểm soát class nào được implement/extend.

Học sâu ở Intermediate.

---

## Java 21

### Pattern matching for switch

```java
String describe(Object obj) {
    return switch (obj) {
        case String s -> "String: " + s;
        case Integer i -> "Integer: " + i;
        case null -> "null";
        default -> "Other";
    };
}
```

### Record patterns

```java
record Point(int x, int y) {}
```

Pattern destructuring dùng trong advanced pattern matching.

### Virtual Threads

```java
Thread.startVirtualThread(() -> task());
```

Đây là feature quan trọng nhưng concurrency semantics cần học ở Intermediate/Senior, không nên học bằng cách copy API mà chưa hiểu thread/blocking.

---

# 51. Basic CLI / JDK Commands — P1

## Check version

```bash
java -version
javac -version
```

## Compile

```bash
javac Main.java
```

## Output directory

```bash
javac -d out Main.java
```

`-d` chỉ định directory chứa compiled class files.

## Run

```bash
java Main
```

Nếu class ở output folder:

```bash
java -cp out Main
```

## Classpath

```bash
-cp
-classpath
```

Ví dụ:

```bash
java -cp "libs/*:out" Main
```

Windows separator thường là `;` thay vì `:`.

## Create JAR

```bash
jar --create --file app.jar -C out .
```

Short form legacy:

```bash
jar cf app.jar -C out .
```

## List JAR contents

```bash
jar tf app.jar
```

## Senior Notes

Thực tế Maven/Gradle sẽ quản lý nhiều phần này, nhưng classpath vẫn là mental model quan trọng để hiểu:

```text
ClassNotFoundException
NoClassDefFoundError
dependency conflict
```

---

# 52. Beginner Debugging Mindset — P0/P1

Khi lỗi, đừng chỉ đọc dòng cuối.

Ví dụ stack trace:

```text
Exception in thread "main" java.lang.NullPointerException
    at UserService.getName(UserService.java:42)
    at Main.main(Main.java:10)
```

Bắt đầu từ:

```text
exception type
message
first application frame
call chain
```

## Common exceptions beginner phải nhận biết

```text
NullPointerException
IllegalArgumentException
IllegalStateException
IndexOutOfBoundsException
NumberFormatException
ClassCastException
UnsupportedOperationException
IOException
```

## Programming Pattern — Reproduce → Isolate → Verify

1. reproduce lỗi ổn định
2. isolate input/path gây lỗi
3. inspect state
4. fix root cause
5. verify bằng test/reproduction

## Senior Notes

Đừng sửa exception bằng cách thêm null check ngẫu nhiên nếu chưa hiểu vì sao null xuất hiện.

Fix symptom khác fix root cause.

---

# 53. Beginner Testing Mindset — P1

Trước Spring/JUnit sâu, phải hiểu một unit dễ test thường có:

- input rõ
- output rõ
- dependency rõ
- side effect giới hạn

Ví dụ pure-ish method:

```java
public BigDecimal calculateDiscount(
    BigDecimal amount,
    BigDecimal rate
) {
    return amount.multiply(rate);
}
```

Dễ test hơn method tự:

```text
query DB
read clock
call HTTP
write file
```

trong cùng một block.

## Programming Pattern — Dependency Injection for Testability

```java
class UserService {
    private final UserRepository repository;

    UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

Test có thể truyền fake/mock implementation.

## Senior Notes

Testability thường là side effect của design tốt, không phải “thêm test framework vào code xấu”.

---

# 54. Beginner Clean Code Checklist

Trước khi coi một đoạn Java beginner là “ổn”, kiểm tra:

- [ ] Tên class/method/variable mô tả intent?
- [ ] Có magic string/magic number nên thay constant/enum không?
- [ ] Có nested if quá sâu không?
- [ ] Có String `==` không?
- [ ] Có collection return null không?
- [ ] Có exception bị swallow không?
- [ ] Có method quá dài không?
- [ ] Có dependency `new` cứng trong business service không?
- [ ] Có dùng implementation type thay interface không cần thiết không?
- [ ] Có mutable global static state không?
- [ ] Money có dùng `double` không?
- [ ] Date/time có semantics timezone rõ không?
- [ ] File/resource có được close bằng try-with-resources không?
- [ ] Mutable collection có ownership rõ không?
- [ ] `equals/hashCode` có liên quan Set/Map key không?
- [ ] Stream có side effect khó hiểu không?

---

# 55. Beginner → Intermediate Gate

Trước khi chuyển sang **Part 2 — Intermediate**, nên có khả năng tự giải thích và code được các nội dung sau.

## Java language

- [ ] class/object
- [ ] primitive/reference
- [ ] `final`
- [ ] `static`
- [ ] method/overload
- [ ] constructor
- [ ] encapsulation
- [ ] inheritance
- [ ] polymorphism
- [ ] interface
- [ ] abstract class
- [ ] enum
- [ ] record basics
- [ ] exception
- [ ] generics basics
- [ ] lambda

## Collections

- [ ] `ArrayList`
- [ ] `HashSet`
- [ ] `HashMap`
- [ ] khi nào chọn List/Set/Map
- [ ] `computeIfAbsent`
- [ ] `merge`
- [ ] immutable collection factories

## Functional Java

- [ ] Predicate
- [ ] Function
- [ ] Consumer
- [ ] Supplier
- [ ] Stream filter/map/sorted/collect
- [ ] Optional basics

## Data handling

- [ ] String
- [ ] BigDecimal
- [ ] LocalDate / LocalDateTime / Instant
- [ ] Path / Files
- [ ] try-with-resources

## Coding mindset

- [ ] guard clause
- [ ] extract method
- [ ] fail fast
- [ ] defensive copy
- [ ] immutability
- [ ] constructor injection
- [ ] program to interface

## Patterns nhận biết được

- [ ] Strategy
- [ ] Factory
- [ ] Builder
- [ ] Repository
- [ ] Iterator
- [ ] Decorator concept
- [ ] Template Method concept

---

# 56. Những gì cố ý để sang Intermediate

Không nên nhồi tất cả Java vào Beginner. Các phần sau sẽ được học kỹ ở **Part 2 — Intermediate**:

```text
Generics nâng cao: PECS, bounded type params, type erasure
Collections internals và complexity sâu
HashMap internals
equals/hashCode contract sâu
Stream collectors nâng cao
flatMap/reduce/groupingBy/partitioningBy
Spliterator
Concurrency fundamentals
Thread lifecycle
synchronized / volatile
locks / atomics
ExecutorService
CompletableFuture
Virtual Threads
JDBC
transaction
HTTP Client
Reflection
custom annotations processing
dynamic proxy
class loading
serialization
regex nâng cao
NIO channels/buffers
modules
sealed hierarchy
pattern matching nâng cao
SOLID sâu
GoF patterns có hệ thống
unit/integration testing
Maven/Gradle
logging
```

Sau Intermediate mới chuyển sang **Part 3 — Senior**, tập trung vào:

```text
JVM internals
memory model
GC
performance
profiling
concurrency correctness
API design
architecture
DDD boundaries
advanced patterns
failure handling
observability
production debugging
security basics
compatibility/versioning
modern Java trade-offs
```

---

# 57. Beginner Learning Order Đề Xuất

Không cần học theo đúng số chapter trong file. Có thể học theo 6 phase sau.

## Phase 1 — Java Syntax

```text
variables
primitive/reference
operators
if/switch
loops
methods
arrays
String
```

## Phase 2 — OOP

```text
class/object
constructor
encapsulation
static
inheritance
polymorphism
interface
abstract class
enum
record
```

## Phase 3 — Everyday Standard Library

```text
List
Set
Map
Objects
Comparator
BigDecimal
java.time
```

## Phase 4 — Modern Java

```text
lambda
functional interfaces
Stream
Optional
method references
```

## Phase 5 — Boundaries

```text
exceptions
files
I/O
null handling
immutability
defensive copy
```

## Phase 6 — Senior Thinking Introduced Early

```text
guard clause
extract method
constructor injection
program to interface
Strategy
Factory
Repository
Builder
composition over inheritance
fail fast
```

---

# Final Beginner Mental Model

Sau Beginner, Java không nên còn được nhìn như “một danh sách câu lệnh”.

Mental model cần chuyển thành:

```text
Syntax
  ↓
Types
  ↓
Objects + Contracts
  ↓
Collections + Data Transformation
  ↓
Boundaries + Errors
  ↓
Patterns
  ↓
Maintainable Application Code
```

Và một senior không chỉ hỏi:

```text
Câu lệnh nào chạy được?
```

mà còn hỏi:

```text
API này biểu đạt intent tốt chưa?
State ownership nằm ở đâu?
Object có giữ invariant không?
Null semantics có rõ không?
Data structure có đúng access pattern không?
Side effect có bị giấu không?
Dependency có bị hard-code không?
Abstraction này thực sự cần thiết không?
Code này 6 tháng nữa người khác có đọc được không?
```

Đó là lý do từ Beginner đã cần học song song:

```text
Language Idioms
    ↓
Coding / Programming Patterns
    ↓
Design Patterns
    ↓
Senior Engineering Notes
```

thay vì đợi đến khi “học xong syntax” mới bắt đầu học cách thiết kế code.
