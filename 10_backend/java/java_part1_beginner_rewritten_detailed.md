# Java cốt lõi (core / 핵심) — Part 1: Beginner — Rewritten Detailed

> **Mạch đọc:** [README](../README.md) là owner của **Java cốt lõi (core / 핵심) — Part 1: Beginner — Rewritten Detailed**; dùng README để giữ Part 1 ở nền tảng trước Intermediate. Từ **Học Java từ số 0 theo cách hiểu bản chất, không học thuộc cú pháp** nối qua execution/object model, types, control flow, OOP, collections, exceptions và I/O, rồi quay về canonical path để xác định API/spec owner của từng câu hỏi.

## Học Java từ số 0 theo cách hiểu bản chất, không học thuộc cú pháp

> Đây là Part 1 trong lộ trình **Beginner → Intermediate → cấp cao (senior / 시니어) → Master Supplement**. Tài liệu này được viết cho người mới học Java hoặc đã từng dùng Java nhưng chưa có mô hình tư duy (mental model / 사고 모델) chắc chắn. Mỗi chủ đề được giải thích theo hướng: vấn đề đang tồn tại là gì, Java giải quyết nó bằng cơ chế nào, cú pháp thể hiện cơ chế đó ra sao, ví dụ thực tế nên viết như thế nào, và vì sao một số cách viết tuy chạy được nhưng không nên trở thành thói quen.
>
> Các “cấp cao (senior / 시니어) ghi chú (note / 노트)”, “lối viết quen dùng của ngôn ngữ (language idiom / 언어 관용구)”, “mẫu lập trình (programming pattern / 프로그래밍 패턴)” và “mẫu thiết kế (design pattern / 디자인 패턴)” không được tách thành checklist riêng sau mỗi mục. Khi một mẫu (pattern / 패턴) thực sự quan trọng, nó sẽ được giải thích ngay trong nội dung để bạn hiểu nó như một phần tự nhiên của Java chứ không phải một danh sách thuật ngữ cần học thuộc.

> **Chuyển mạch:** Sau khi dựng mental model Java từ execution và object, **Cách đọc bộ Java chuẩn gốc (canonical / 정본)** chỉ ra API/spec nào là owner cho từng câu hỏi. Handoff này giữ Part 1 ở nền tảng ngôn ngữ thay vì lấn sang framework.

## Cách đọc bộ Java chuẩn gốc (canonical / 정본)

Đây là tệp (file / 파일) đầu tiên trong bốn ghi chú (note / 노트) chuẩn gốc (canonical / 정본) của Java thư viện kiến thức (knowledge library / 지식 라이브러리). Hãy đọc theo thứ tự **Beginner → Intermediate → cấp cao (senior / 시니어) → Master Supplement** thay vì nhảy thẳng vào JVM hoặc tính đồng thời (concurrency / 동시성). Beginner xây hệ kiểu (type system / 타입 시스템), mô hình đối tượng (object model / 객체 모델), collections, exception và I/O; Intermediate mở generics, tính đồng thời (concurrency / 동시성), JDBC, reflection và JVM; cấp cao (senior / 시니어) chuyển sang môi trường vận hành (production / 운영 환경) tính đúng đắn (correctness / 정확성), profiling và hiệu năng (performance / 성능); Master chỉ bổ sung low-level/thời gian chạy (runtime / 런타임)/library-author topics chưa phù hợp với ba phần trước.

Sau khi hoàn thành tệp (file / 파일) này, tiếp tục tại [Java Part 2 — Intermediate](./java_part2_intermediate_rewritten_detailed.md).

---

# 1. Trước khi viết mã (code / 코드): Java thực sự chạy như thế nào?

Khi bạn viết một tệp (file / 파일) `Hello.java`, CPU không hiểu trực tiếp mã nguồn (source code / 소스 코드) Java. mã nguồn (source code / 소스 코드) trước hết được trình biên dịch (compiler / 컴파일러) `javac` biên dịch thành **bytecode** nằm trong tệp (file / 파일) `.class`. Bytecode không gắn chặt với một loại CPU cụ thể như x86 hay ARM. Nó là instruction format dành cho JVM, tức Java Virtual Machine. Khi ứng dụng (application / 애플리케이션) chạy, JVM tải (load / 로드) các lớp (class / 클래스), verify bytecode, quản lý bộ nhớ (memory / 메모리), thực thi bytecode bằng trình thông dịch (interpreter / 인터프리터) và có thể compile những đoạn mã (code / 코드) nóng thành mã máy bản địa (native machine code / 네이티브 기계어) bằng Trình biên dịch JIT (JIT compiler / JIT 컴파일러).

Có thể hình dung luồng (flow / 흐름) đơn giản như sau:

```text
Hello.java
    ↓ javac
Hello.class
    ↓ JVM
bytecode được load / verify / execute
    ↓
native instructions trên máy thật
```

Đây là nguyên nhân Java nổi tiếng với ý tưởng “ghi (write / 쓰기) once, run anywhere”. Thực tế chính xác hơn là cùng bytecode có thể chạy trên nhiều nền tảng (platform / 플랫폼) miễn nền tảng (platform / 플랫폼) đó có JVM tương thích. Bạn vẫn có thể gặp khác biệt về filesystem, timezone, charset, bản địa (native / 네이티브) thư viện (library / 라이브러리) hoặc OS hành vi (behavior / 동작), vì vậy portable không có nghĩa mọi môi trường hoàn toàn giống nhau.

Ba khái niệm rất thường bị trộn là JDK, JRE và JVM. JVM là máy ảo thực thi bytecode. JRE theo cách gọi truyền thống là môi trường cần để chạy Java ứng dụng (application / 애플리케이션), gồm JVM và tiêu chuẩn (standard / 표준) thời gian chạy (runtime / 런타임) libraries. JDK là bộ công cụ phát triển, chứa trình biên dịch (compiler / 컴파일러), thời gian chạy (runtime / 런타임) và các tools như `javac`, `jar`, `javadoc`, `jcmd`, `jshell`. Với Java hiện đại, cách đóng gói thời gian chạy (runtime / 런타임) đã thay đổi và khái niệm “cài một JRE riêng như thời Java 8” không còn là mô hình tư duy (mental model / 사고 모델) tốt nhất, nhưng ba khái niệm trên vẫn giúp bạn hiểu kiến trúc.

Khi gặp lỗi “mã (code / 코드) compile trên máy tôi nhưng máy chủ (server / 서버) không chạy”, hãy phân biệt compile-time và thời gian chạy (runtime / 런타임). Ví dụ bạn compile lớp (class / 클래스) bằng JDK mới rồi deploy lên JVM cũ, máy chủ (server / 서버) có thể báo `UnsupportedClassVersionError`. Đây không phải lỗi lô-gic nghiệp vụ (business logic / 비즈니스 로직); thời gian chạy (runtime / 런타임) đơn giản không hiểu class-file phiên bản (version / 버전) mới.

---

# 2. Cài JDK và kiểm tra môi trường

Sau khi cài JDK, hai lệnh đầu tiên nên biết là:

```bash
java --version
javac --version
```

`java` dùng để chạy ứng dụng (application / 애플리케이션). `javac` dùng để compile nguồn (source / 소스). Nếu hai lệnh cho phiên bản (version / 버전) khác nhau hoặc shell đang dùng một JDK khác IDE, bạn có thể gặp bug rất khó hiểu. Trong môi trường làm việc thực tế, đừng chỉ tin IDE đang hiển thị “Java 21”; hãy kiểm tra bản dựng (build / 빌드) công cụ (tool / 도구), `JAVA_HOME`, thời gian chạy (runtime / 런타임) command và CI cũng dùng phiên bản (version / 버전) nào.

Compile một tệp (file / 파일) đơn giản:

```bash
javac Hello.java
```

Run:

```bash
java Hello
```

Nếu gói (package / 패키지) được dùng, classpath và folder cấu trúc (structure / 구조) bắt đầu có ý nghĩa. Phần nạp lớp (class loading / 클래스 로딩) sâu hơn sẽ học ở Intermediate và cấp cao (senior / 시니어); ở Beginner bạn chỉ cần hiểu rằng JVM phải tìm được `.class` đúng theo fully qualified lớp (class / 클래스) name.

---

# 3. Cấu trúc một chương trình Java

Một tệp (file / 파일):

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

`package` xác định không gian tên (namespace / 네임스페이스) của lớp (class / 클래스). `import` cho phép viết short lớp (class / 클래스) name thay vì full name. lớp (class / 클래스) `HelloApplication` chứa phương thức (method / 메서드) `main`, là entry điểm (point / 지점) truyền thống cho một Java ứng dụng (application / 애플리케이션).

Gói (package / 패키지) không chỉ dùng để “xếp folder cho đẹp”. Nó giúp tránh name collision và còn ảnh hưởng kiểm soát truy cập (access control / 접근 제어). Một lớp (class / 클래스) package-private có thể được các lớp (class / 클래스) cùng gói (package / 패키지) dùng nhưng không công khai (public / 공개) ra toàn ứng dụng (application / 애플리케이션). Khi dự án (project / 프로젝트) lớn, gói (package / 패키지) ranh giới (boundary / 경계) trở thành một công cụ kiến trúc.

`import` không bản sao (copy / 복사) mã (code / 코드) và cũng không làm lớp (class / 클래스) “được tải (load / 로드) sẵn”. Nó chủ yếu là compile-time cú pháp (syntax / 문법) để trình biên dịch (compiler / 컴파일러) biết `LocalDate` bạn viết đang nói tới kiểu (type / 타입) nào. Static import:

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

Static import hợp khi symbol có nghĩa rõ trong ngữ cảnh (context / 맥락), ví dụ assertions trong tests hoặc một vài utility methods. Nếu dùng quá nhiều, người đọc khó biết phương thức (method / 메서드) đến từ lớp (class / 클래스) nào.

---

# 4. `main()` và ý nghĩa của từng phần

Phương thức (method / 메서드) truyền thống:

```java
public static void main(String[] args) {
}
```

`public` cho phép launcher truy cập. `static` nghĩa phương thức (method / 메서드) thuộc lớp (class / 클래스), không cần tạo đối tượng (object / 객체) của lớp (class / 클래스) trước. `void` nghĩa không return giá trị (value / 값). `String[] args` chứa command-line arguments.

Ví dụ:

```bash
java Hello Alice
```

thì:

```java
args[0]
```

là `"Alice"`.

Bạn không cần biến mọi lô-gic (logic / 논리) thành `static` chỉ vì `main` là static. Một ứng dụng (application / 애플리케이션) có thể dùng `main` chỉ để bootstrap đối tượng (object / 객체) đồ thị (graph / 그래프) rồi chuyển điều khiển (control / 제어) sang normal objects. Đây là thói quen quan trọng trước khi học Spring: `main` không nên là nơi chứa toàn bộ ứng dụng (application / 애플리케이션).

---

# 5. Variable là gì?

Variable là một tên gắn với một vùng dữ liệu theo kiểu (type / 타입) nhất định.

```java
int age = 27;
```

Ở đây `int` là kiểu (type / 타입), `age` là variable name, `27` là giá trị (value / 값) ban đầu.

Bạn có thể khai báo rồi gán sau:

```java
int age;
age = 27;
```

nhưng cục bộ (local / 로컬) variable phải được definite assignment trước khi đọc. trình biên dịch (compiler / 컴파일러) ngăn bạn dùng cục bộ (local / 로컬) variable chưa được gán một cách chắc chắn.

Trường dữ liệu (field / 필드) của đối tượng (object / 객체) lại có default values như `0`, `false`, `null`, nhưng không nên dựa vào default một cách mơ hồ nếu trường dữ liệu (field / 필드) là phần quan trọng của bất biến (invariant / 불변식). Constructor nên thiết lập đối tượng (object / 객체) thành trạng thái hợp lệ ngay từ lúc tạo.

---

# 6. thành phần nguyên thủy (primitive / 기본 요소) types và tham chiếu (reference / 참조) types

Java có tám thành phần nguyên thủy (primitive / 기본 요소) types: `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`.

Trong ứng dụng (application / 애플리케이션) thông thường, integer thường dùng `int`; `long` khi phạm vi (range / 범위) lớn hoặc ID/timestamp-like numeric values cần lớn hơn. `float` và `double` dùng floating-point nhị phân (binary / 이진) arithmetic, rất phù hợp cho khoa học/đồ họa/nhiều phép tính gần đúng nhưng không nên tự động dùng cho tiền.

Ví dụ:

```java
double price = 0.1 + 0.2;
System.out.println(price);
```

có thể in ra một số không chính xác theo decimal intuition vì nhị phân (binary / 이진) floating điểm (point / 지점) không biểu diễn chính xác mọi decimal fraction. Tiền thường dùng `BigDecimal`, sẽ học sau.

`char` là một UTF-16 mã (code / 코드) đơn vị (unit / 단위), không phải luôn một “ký tự Unicode hoàn chỉnh” theo cách người dùng nhìn thấy. Unicode sâu hơn sẽ nằm ở Intermediate/Master.

Tham chiếu (reference / 참조) kiểu (type / 타입) gồm lớp (class / 클래스), giao diện (interface / 인터페이스), array, enum, bản ghi (record / 레코드) và nhiều loại đối tượng (object / 객체) khác.

```java
String name = "Kim";
User user = new User(...);
```

Variable tham chiếu (reference / 참조) không chứa toàn bộ đối tượng (object / 객체) theo mô hình tư duy (mental model / 사고 모델) đơn giản; nó chứa tham chiếu (reference / 참조) tới đối tượng (object / 객체). Vì vậy hai variables có thể trỏ tới cùng đối tượng (object / 객체).

```java
User a = user;
User b = user;
```

Thay đổi mutable trạng thái (state / 상태) qua `a` có thể được nhìn thấy qua `b` vì cả hai tham chiếu (reference / 참조) cùng trỏ tới một đối tượng (object / 객체).

---

# 7. `null` là gì?

Tham chiếu (reference / 참조) variable có thể có giá trị `null`, nghĩa là hiện không trỏ tới đối tượng (object / 객체) nào.

```java
User user = null;
```

Gọi:

```java
user.name();
```

sẽ gây `NullPointerException`.

Điểm quan trọng là `null` không phải đối tượng (object / 객체). Nó là special tham chiếu (reference / 참조) giá trị (value / 값). Nhiều bug Java đến từ đặc tả hợp đồng (contract / 계약) không rõ: phương thức (method / 메서드) này có thể return null không? parameter này có chấp nhận null không?

Nếu null không hợp lệ, thất bại (fail / 실패) sớm:

```java
public UserService(UserRepository repository) {
    this.repository =
        Objects.requireNonNull(repository);
}
```

Cách này làm lỗi xảy ra ngay tại ranh giới (boundary / 경계) nơi bất biến (invariant / 불변식) bị vi phạm, thay vì vài phút sau ở một phương thức (method / 메서드) xa hơn.

Một ứng dụng (application / 애플리케이션) tốt không nhất thiết “không bao giờ dùng null”, nhưng null chính sách (policy / 정책) phải rõ. Collection phương thức (method / 메서드) thường nên return empty collection thay vì null nếu “không có phần tử” là kết quả hợp lệ.

---

# 8. `final` và tư duy immutable

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
final int maxRetry = 3;
```

Sau assignment, variable không thể được assign lại.

Với tham chiếu (reference / 참조):

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

vì `final` khóa tham chiếu (reference / 참조) variable, không tự làm đối tượng (object / 객체) immutable.

Dù vậy `final` rất hữu ích. Khi phụ thuộc (dependency / 의존성) trường dữ liệu (field / 필드):

```java
private final UserRepository repository;
```

người đọc biết tham chiếu (reference / 참조) không bị đổi sau construction. Càng ít reassignment và mutable trạng thái (state / 상태), mã (code / 코드) càng dễ reason, nhất là khi tính đồng thời (concurrency / 동시성) xuất hiện.

Một thói quen tốt là để constructor thiết lập required fields và giữ chúng `final` khi có thể. Đây là nền của immutable đối tượng (object / 객체) và constructor injection.

---

# 9. `var` từ Java 10

Java 10 hỗ trợ cục bộ (local / 로컬) variable kiểu (type / 타입) suy luận (inference / 추론):

```java
var users =
    new ArrayList<User>();
```

Trình biên dịch (compiler / 컴파일러) vẫn biết chính xác (exact / 정확한) static kiểu (type / 타입). Java không trở thành dynamically typed ngôn ngữ (language / 언어).

`var` chỉ dùng cho cục bộ (local / 로컬) variables trong những ngữ cảnh (context / 맥락) cho phép; không dùng thay trường dữ liệu (field / 필드) kiểu (type / 타입) hoặc phương thức (method / 메서드) return kiểu (type / 타입).

Nó tốt khi right-hand side nói kiểu (type / 타입) rõ:

```java
var formatter =
    DateTimeFormatter.ISO_LOCAL_DATE;
```

Nó kém rõ khi:

```java
var result = process();
```

và không ai biết `process()` trả gì nếu không nhảy tới definition.

Do đó hãy dùng `var` để giảm noise, không để che ngữ nghĩa (semantic / 의미적) kiểu (type / 타입).

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

nếu vế trái true, `loadFallback()` không chạy. Nếu phương thức (method / 메서드) bên phải có side tác động (effect / 효과), short-circuit có thể làm luồng (flow / 흐름) khó đọc. Tránh nhét nghiệp vụ (business / 비즈니스) side tác động (effect / 효과) vào boolean expressions phức tạp.

---

# 11. `==` khác `equals()` như thế nào?

Với primitives, `==` so sánh giá trị (value / 값):

```java
int a = 10;
int b = 10;

a == b // true
```

Với references, `==` kiểm tra hai references có trỏ tới cùng đối tượng (object / 객체) định danh (identity / 식별자) hay không.

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

Khi kiểu (type / 타입) của bạn biểu diễn giá trị (value / 값) như `Money`, `UserId`, `Email`, `equals()` và `hashCode()` phải phản ánh giá trị (value / 값) ngữ nghĩa (semantics / 의미론). Nếu đối tượng (object / 객체) được dùng làm `HashMap` key hoặc `HashSet` element, đặc tả hợp đồng (contract / 계약) của hai methods này cực kỳ quan trọng. Intermediate sẽ đi sâu.

---

# 12. Casting và conversion

Widening thành phần nguyên thủy (primitive / 기본 요소) conversion thường an toàn hơn:

```java
int x = 10;
long y = x;
```

Narrowing cần tường minh (explicit / 명시적) cast:

```java
long value = 1000L;
int x = (int) value;
```

Nếu giá trị (value / 값) vượt phạm vi (range / 범위), dữ liệu có thể bị mất.

Đối tượng (object / 객체) casting:

```java
Animal animal = new Dog();
Dog dog = (Dog) animal;
```

cast hợp lệ vì thời gian chạy (runtime / 런타임) đối tượng (object / 객체) thật là `Dog`.

Sai:

```java
Animal animal = new Cat();
Dog dog = (Dog) animal;
```

gây `ClassCastException`.

Hiện đại (modern / 현대적) mẫu (pattern / 패턴) matching:

```java
if (animal instanceof Dog dog) {
    dog.bark();
}
```

tránh separate cast và làm kiểu (type / 타입) narrowing rõ hơn.

Khi mã (code / 코드) có rất nhiều `instanceof` + casts theo kiểu (type / 타입), hãy xem hierarchy có thiếu polymorphism hay closed-type modeling không. Java 17 sealed classes và Java 21 mẫu (pattern / 패턴) switch sẽ giúp một số trường hợp (case / 사례).

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

Nested mã (code / 코드):

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

Guard clause làm invalid cases kết thúc sớm và giữ happy đường dẫn (path / 경로) phẳng. Đây không phải quy tắc (rule / 규칙) tuyệt đối; nếu có hai branch đối xứng, `if/else` có thể rõ hơn. Nhưng với kiểm tra hợp lệ (validation / 검증)/permission chuỗi xử lý (pipeline / 파이프라인), guard clause thường rất hiệu quả.

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

Hiện đại (modern / 현대적) switch expression từ Java 14:

```java
String label =
    switch (status) {
        case NEW -> "New";
        case DONE -> "Done";
        case CANCELLED -> "Cancelled";
    };
```

Không cần `break`, và trình biên dịch (compiler / 컴파일러) có thể check exhaustiveness khi kiểu (type / 타입) hữu hạn phù hợp.

Với enum hoặc sealed hierarchy, switch expression làm data-oriented branch lô-gic (logic / 논리) rõ. Tuy nhiên không phải mọi nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작) nên biến thành giant switch. Nếu mỗi trường hợp (case / 사례) có hành vi (behavior / 동작) phức tạp và kiểu (type / 타입) có polymorphic responsibility thật, chiến lược (strategy / 전략)/trạng thái (state / 상태)/polymorphism có thể phù hợp hơn.

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

Nếu không cần chỉ mục (index / 인덱스), enhanced for thường rõ hơn.

`while` hợp khi số lần lặp chưa biết trước:

```java
while (queue.hasNext()) {
    process(queue.next());
}
```

`do-while` đảm bảo body chạy ít nhất một lần.

`break` dừng vòng lặp (loop / 루프), `continue` bỏ phần còn lại của iteration hiện tại.

Đừng biến vòng lặp (loop / 루프) thành nơi có 100 dòng lô-gic (logic / 논리). Nếu iteration có nhiều nghiệp vụ (business / 비즈니스) steps, extract phương thức (method / 메서드):

```java
for (Order order : orders) {
    processOrder(order);
}
```

Không phải vì phương thức (method / 메서드) ngắn luôn tốt, mà vì vòng lặp (loop / 루프) nói rõ “lặp qua orders”, còn phương thức (method / 메서드) nói rõ “tiến trình (process / 프로세스) một thứ tự (order / 순서)”.

---

# 16. Methods và đặc tả hợp đồng (contract / 계약)

Phương thức (method / 메서드):

```java
public Money calculateTotal(
        List<OrderItem> items) {
    ...
}
```

Phương thức (method / 메서드) signature là một đặc tả hợp đồng (contract / 계약): đầu vào (input / 입력) kiểu (type / 타입) gì, đầu ra (output / 출력) kiểu (type / 타입) gì, truy cập (access / 접근) mức (level / 수준) nào, phương thức (method / 메서드) name nói hành vi (behavior / 동작) nào.

Parameter là pass-by-value, kể cả tham chiếu (reference / 참조). Java luôn bản sao (copy / 복사) **giá trị (value / 값) của variable** vào parameter.

```java
void reassign(User user) {
    user = new User(...);
}
```

không đổi tham chiếu (reference / 참조) của caller.

Nhưng:

```java
void rename(User user) {
    user.setName("A");
}
```

có thể mutate cùng đối tượng (object / 객체) mà caller đang giữ.

Đây là lý do câu “Java pass đối tượng (object / 객체) by tham chiếu (reference / 참조)” là không chính xác. Java pass-by-value; với đối tượng (object / 객체), giá trị (value / 값) được bản sao (copy / 복사) là tham chiếu (reference / 참조) giá trị (value / 값).

---

# 17. phương thức (method / 메서드) Overloading

Overloading nghĩa cùng phương thức (method / 메서드) name nhưng khác parameter danh sách (list / 목록):

```java
void send(String message)
void send(String message, int priority)
```

Trình biên dịch (compiler / 컴파일러) chọn overload ở compile thời gian (time / 시간) dựa trên static types và conversion rules.

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

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
void log(String... messages) {
}
```

Caller:

```java
log("A", "B", "C");
```

Trong phương thức (method / 메서드), `messages` gần như array.

Varargs nên ở cuối parameter danh sách (list / 목록) và dùng khi số arguments thực sự variable. Đừng thay `List<T>` bằng varargs cho dữ liệu (data / 데이터) đã tồn tại dạng collection.

Generic varargs có type-erasure/heap-pollution concerns; Intermediate sẽ giải thích `@SafeVarargs`.

---

# 19. Arrays

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

```java
int[] numbers = {1, 2, 3};
```

Array có fixed length.

```java
numbers.length
```

Chỉ mục (index / 인덱스) từ `0` đến `length - 1`. Sai chỉ mục (index / 인덱스) gây `ArrayIndexOutOfBoundsException`.

Array biết thời gian chạy (runtime / 런타임) thành phần (component / 컴포넌트) kiểu (type / 타입) và có covariance:

```java
String[] strings = new String[2];
Object[] objects = strings;
```

nhưng:

```java
objects[0] = Integer.valueOf(1);
```

gây `ArrayStoreException`. Generics lại bất biến (invariant / 불변식) theo cách khác. Đây là một trong các lý do collections generic thường dễ dùng hơn arrays trong ứng dụng (application / 애플리케이션) mã (code / 코드).

`Arrays` utility:

```java
Arrays.sort(numbers);
Arrays.asList(...);
Arrays.copyOf(...);
```

Cẩn thận `Arrays.asList(array)` tạo fixed-size danh sách (list / 목록) view trên array; không giống `new ArrayList<>()`.

---

# 20. String và tính immutable

`String` immutable. Sau khi đối tượng (object / 객체) String được tạo, nội dung logical của nó không đổi.

```java
String name = "Kim";
name.toUpperCase();
```

không sửa `name`.

Phải:

```java
name = name.toUpperCase();
```

Immutability giúp String an toàn hơn khi share, bộ nhớ đệm (cache / 캐시), dùng làm key và tối ưu nội bộ.

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

`isBlank()` và `strip()` có ngữ nghĩa (semantics / 의미론) Unicode-aware hơn `trim()` trong một số khía cạnh và có từ Java 11.

Văn bản (text / 텍스트) khối (block / 블록) từ Java 15:

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

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

```java
String full = first + " " + last;
```

cho vài concatenations hoàn toàn ổn. trình biên dịch (compiler / 컴파일러)/JVM có optimizations.

Nhưng vòng lặp (loop / 루프):

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

Tuy nhiên đừng micro-optimize mọi `+`. Chỉ dùng builder khi xây văn bản (text / 텍스트) lặp/phức tạp hoặc clarity phù hợp.

---

# 22. Normalize đầu vào (input / 입력) at ranh giới (boundary / 경계)

Người dùng (user / 사용자) đầu vào (input / 입력) có thể có whitespace/trường hợp (case / 사례) variations.

Bad:

```java
if (email.trim().toLowerCase().equals(...)) {
}
```

rải khắp mã (code / 코드).

Better:

```java
String normalizedEmail =
    normalizeEmail(rawEmail);
```

rồi cốt lõi (core / 핵심) dùng normalized form.

Cách này là một mẫu lập trình (programming pattern / 프로그래밍 패턴) quan trọng: **normalize/parse đầu vào (input / 입력) ở ranh giới (boundary / 경계)**, thay vì validate lặp lại ở mọi nơi. Sau này lĩnh vực (domain / 도메인) giá trị (value / 값) đối tượng (object / 객체) như `Email` có thể encapsulate quy tắc (rule / 규칙) này.

---

# 23. Wrapper Classes và Autoboxing

Thành phần nguyên thủy (primitive / 기본 요소) wrappers:

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

Trình biên dịch (compiler / 컴파일러) box thành phần nguyên thủy (primitive / 기본 요소) thành đối tượng (object / 객체).

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

Collection generic không nhận thành phần nguyên thủy (primitive / 기본 요소) trực tiếp:

```java
List<Integer>
```

nên boxing có thể tạo allocation/hiệu năng (performance / 성능) chi phí (cost / 비용) ở hot paths. Beginner chưa cần tối ưu, nhưng cần biết ngữ nghĩa (semantic / 의미적).

Parsing:

```java
int age =
    Integer.parseInt("27");
```

invalid văn bản (text / 텍스트) gây `NumberFormatException`.

---

# 24. Classes và Objects

Lớp (class / 클래스) mô tả trạng thái (state / 상태) + hành vi (behavior / 동작).

```java
public class BankAccount {
    private BigDecimal balance;

    public void deposit(BigDecimal amount) {
        ...
    }
}
```

Đối tượng (object / 객체) là instance cụ thể:

```java
BankAccount account =
    new BankAccount();
```

OOP tốt không phải chỉ gom fields + getters/setters. Một đối tượng (object / 객체) nên bảo vệ bất biến (invariant / 불변식).

Bad:

```java
account.setBalance(
    new BigDecimal("-999"));
```

Better:

```java
account.withdraw(amount);
```

và phương thức (method / 메서드) kiểm tra không cho balance invalid.

Đây là tư duy “tell đối tượng (object / 객체) what to do” thay vì lấy toàn bộ trạng thái (state / 상태) ra ngoài rồi tự xử lý.

---

# 25. Constructor

Constructor tạo đối tượng (object / 객체) ở trạng thái ban đầu.

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

Nếu `name`/`email` là required, đối tượng (object / 객체) không nên có default constructor rồi chờ setter.

Constructor establishes validity là một thói quen rất mạnh. Nó làm impossible trạng thái (state / 상태) khó tồn tại.

Constructor overloading:

```java
public User(String name) {
    this(name, null);
}
```

phải dùng cẩn thận nếu null làm đối tượng (object / 객체) không hợp lệ.

---

# 26. `this` và `super`

`this` nói đối tượng (object / 객체) hiện tại.

```java
this.name = name;
```

`this(...)` gọi constructor khác trong cùng lớp (class / 클래스) và phải là statement đầu tiên.

`super(...)` gọi constructor superclass và cũng phải ở đầu constructor theo rules tương ứng.

`super.method()` gọi hiện thực (implementation / 구현) của parent khi override.

Các từ khóa (keyword / 키워드) này quan trọng nhưng không nên dùng inheritance phức tạp chỉ vì Java hỗ trợ.

---

# 27. Encapsulation và truy cập (access / 접근) Modifiers

`private` giới hạn trong lớp (class / 클래스). Package-private không viết modifier và cho cùng gói (package / 패키지) truy cập (access / 접근). `protected` liên quan subclass và gói (package / 패키지) ngữ nghĩa (semantics / 의미론). `public` expose rộng nhất.

Default nên là visibility hẹp nhất hợp lý. Nếu một helper chỉ cần trong gói (package / 패키지), không cần công khai (public / 공개).

API công khai (public API / 공개 API) khó thay đổi hơn vì nhiều mã (code / 코드) có thể phụ thuộc. Đây là lý do “minimize công khai (public / 공개) surface” là một principle quan trọng từ thư viện (library / 라이브러리) tới ứng dụng (application / 애플리케이션) modules.

Encapsulation không chỉ là “fields private rồi generate getters/setters”. Nếu mọi trạng thái (state / 상태) vẫn được set tùy ý, bất biến (invariant / 불변식) chưa thực sự được encapsulate.

---

# 28. `static`

Static member thuộc lớp (class / 클래스) hơn là một instance.

```java
public static final int MAX_RETRY = 3;
```

Static utility phương thức (method / 메서드):

```java
public static boolean isBlank(String value) {
}
```

Static trạng thái (state / 상태) mutable:

```java
public static List<User> users =
        new ArrayList<>();
```

là toàn cục (global / 전역) mutable trạng thái (state / 상태) và dễ tạo kiểm thử (test / 테스트)/tính đồng thời (concurrency / 동시성) coupling.

Static không xấu. Constants, pure utilities và factory methods rất hữu ích. Điều cần tránh là dùng static toàn cục (global / 전역) mutable trạng thái (state / 상태) như hidden phụ thuộc (dependency / 의존성).

---

# 29. Inheritance

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
class Dog extends Animal {
}
```

Inheritance biểu diễn is-a relationship và reuse polymorphic hành vi (behavior / 동작).

Override:

```java
@Override
public String sound() {
    return "woof";
}
```

Inheritance dễ bị lạm dụng để reuse mã (code / 코드). Nếu `ReportService extends BaseService extends LoggingService...`, hierarchy cứng và fragile.

Thường composition rõ hơn:

```java
class ReportService {
    private final Formatter formatter;
}
```

“Favor composition over inheritance” là heuristic, không luật tuyệt đối. Inheritance tốt khi hierarchy thực sự ổn định và substitutability đúng.

---

# 30. Polymorphism

Giao diện (interface / 인터페이스):

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

Phương thức (method / 메서드) dispatch chọn hiện thực (implementation / 구현) thời gian chạy (runtime / 런타임).

Đây là nền của chiến lược (strategy / 전략) mẫu (pattern / 패턴): caller phụ thuộc hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약), hiện thực (implementation / 구현) có thể thay.

Spring phụ thuộc (dependency / 의존성) Injection sau này tận dụng đúng kiểu lớp trừu tượng (abstraction / 추상화) này.

---

# 31. Interfaces

Giao diện (interface / 인터페이스) khai báo đặc tả hợp đồng (contract / 계약):

```java
public interface UserRepository {
    Optional<User> findById(UserId id);
}
```

Lớp (class / 클래스):

```java
public final class JdbcUserRepository
        implements UserRepository {
}
```

Java 8 thêm default/static methods trong giao diện (interface / 인터페이스); Java 9 thêm private giao diện (interface / 인터페이스) methods để share hiện thực (implementation / 구현) giữa default methods.

Đừng tạo giao diện (interface / 인터페이스) cho mọi lớp (class / 클래스) chỉ vì “best practice”. giao diện (interface / 인터페이스) hữu ích khi có lớp trừu tượng (abstraction / 추상화) thật: nhiều implementations, kiểm thử (test / 테스트) seam, bên ngoài (external / 외부) ranh giới (boundary / 경계) hoặc stable công khai (public / 공개) đặc tả hợp đồng (contract / 계약).

Một lớp (class / 클래스) nội bộ (internal / 내부) duy nhất không cần giao diện (interface / 인터페이스) giả tạo nếu không có reason.

---

# 32. Abstract Classes

Abstract lớp (class / 클래스) cho trạng thái dùng chung (shared state / 공유 상태)/hành vi (behavior / 동작) + abstract methods.

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

Đây gần Template phương thức (method / 메서드) mẫu (pattern / 패턴): superclass define thuật toán (algorithm / 알고리즘) skeleton, subclass customize steps.

So với giao diện (interface / 인터페이스), abstract lớp (class / 클래스) có instance trạng thái (state / 상태)/constructors và single inheritance restriction.

Nếu customization cần linh hoạt, composition/chiến lược (strategy / 전략) thường dễ thay hơn.

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

Đừng persist ordinal mặc định nếu nghiệp vụ (business / 비즈니스)/lưu trữ (storage / 저장소) đặc tả hợp đồng (contract / 계약) cần stable values; reorder enum có thể phá dữ liệu. Stable mã (code / 코드)/string thường an toàn hơn.

---

# 34. Records từ Java 16

Bản ghi (record / 레코드) phù hợp cho data-centric immutable-ish carriers.

```java
public record UserResponse(
        long id,
        String name,
        String email) {
}
```

Trình biên dịch (compiler / 컴파일러) tạo accessors, constructor, `equals`, `hashCode`, `toString` theo bản ghi (record / 레코드) components.

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

Bản ghi (record / 레코드) shallowly immutable: tham chiếu (reference / 참조) fields không thể reassigned, nhưng đối tượng (object / 객체) bên trong có thể mutable.

```java
record Config(List<String> rules) {
}
```

Nếu `rules` mutable, caller vẫn có thể mutate danh sách (list / 목록). Use `List.copyOf` nếu cần quyền sở hữu (ownership / 소유권) snapshot.

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

Sealed hierarchy nói set implementations được kiểm soát. Khi kết hợp mẫu (pattern / 패턴) switch Java 21, trình biên dịch (compiler / 컴파일러) có thể reason exhaustiveness.

Nó phù hợp cho finite alternatives, nhưng không nên seal extension điểm (point / 지점) mà third-party/plugin cần mở rộng.

---

# 36. `Object` methods

Mọi lớp (class / 클래스) tham chiếu (reference / 참조) kiểu (type / 타입) cuối cùng liên hệ `Object`.

Methods quan trọng: `equals`, `hashCode`, `toString`, `getClass`.

Override `toString()` để log/gỡ lỗi (debug / 디버그) hữu ích nhưng không expose secrets.

Nếu override `equals`, phải override `hashCode` consistent. Hash-based collections dựa đặc tả hợp đồng (contract / 계약) này. Intermediate sẽ đi sâu mutable-key trap và băm (hash / 해시) ngữ nghĩa (semantics / 의미론).

---

# 37. Exceptions: lỗi (error / 오류) luồng (flow / 흐름) trong Java

Exception là đối tượng (object / 객체) biểu diễn abnormal điều kiện (condition / 조건).

Checked exceptions phải được catch hoặc declare:

```java
void load()
        throws IOException {
}
```

Unchecked exceptions extend `RuntimeException`; trình biên dịch (compiler / 컴파일러) không bắt caller declare.

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

vì bạn mất tín hiệu (signal / 신호) và nguyên nhân gốc (root cause / 근본 원인).

Catch exception khi bạn có thể recover, translate, add ngữ cảnh (context / 맥락) hoặc terminate ở quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계).

---

# 38. Checked vs Unchecked: đừng học thành “checked tốt/xấu”

Checked exception phù hợp khi caller realistically được kỳ vọng xử lý/recover theo đặc tả hợp đồng (contract / 계약). Unchecked phù hợp cho programming errors, invalid states và nhiều hạ tầng (infrastructure / 인프라) failures nơi forcing every tầng (layer / 계층) catch/declare không thêm giá trị (value / 값).

Không có quy tắc (rule / 규칙) “backend luôn dùng RuntimeException”. Điều quan trọng là exception taxonomy và ranh giới (boundary / 경계).

Ví dụ repository có thể catch vendor SQL exception và translate thành ứng dụng (application / 애플리케이션) data-access exception có cause giữ nguyên.

```java
throw new DataAccessFailure(
    "Cannot load user " + id,
    e);
```

Giữ cause giúp môi trường vận hành (production / 운영 환경) debugging.

---

# 39. `finally` và Try-with-resources

Tài nguyên (resource / 자원) như tệp (file / 파일)/socket/cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) cần close.

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

Hiện đại (modern / 현대적):

```java
try (InputStream in =
         Files.newInputStream(path)) {
    ...
}
```

Try-with-resources gọi `close()` tự động cho `AutoCloseable`.

Nếu body throw và `close()` cũng throw, exception từ close có thể thành suppressed exception, không làm mất primary exception.

Tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) phải rõ. phương thức (method / 메서드) nhận stream từ caller thường không nên tự close nếu đặc tả hợp đồng (contract / 계약) nói caller sở hữu nó.

---

# 40. Collections khung phần mềm (framework / 프레임워크): tại sao có nhiều loại collection?

Không có một collection “tốt nhất”.

`List` biểu diễn ordered chuỗi (sequence / 시퀀스), cho phép duplicates.

`Set` biểu diễn uniqueness.

`Map` biểu diễn key → giá trị (value / 값) lookup.

`Queue`/`Deque` biểu diễn processing thứ tự (order / 순서).

Chọn kiểu (type / 타입) theo ngữ nghĩa (semantics / 의미론) trước hiệu năng (performance / 성능).

Nếu lĩnh vực (domain / 도메인) nói “mỗi email chỉ xuất hiện một lần”, `Set<Email>` có thể encode ràng buộc (constraint / 제약조건) tốt hơn `List<Email>` + manual duplicate checks.

---

# 41. `ArrayList`

Default danh sách (list / 목록) hiện thực (implementation / 구현) cho phần lớn ứng dụng (application / 애플리케이션) use cases.

```java
List<String> names =
    new ArrayList<>();

names.add("Kim");
names.add("Lee");
```

Fast random truy cập (access / 접근) theo chỉ mục (index / 인덱스) và append thường hiệu quả.

Insert/remove giữa danh sách (list / 목록) có thể shift elements.

Đừng chọn `LinkedList` chỉ vì thấy O(1) insertion trên textbook. Real workloads còn bộ nhớ đệm (cache / 캐시) locality, traversal và việc tìm nút (node / 노드). `ArrayList` thường là default tốt cho general-purpose danh sách (list / 목록).

---

# 42. `Set`

`HashSet` cho uniqueness với hash-based lookup.

```java
Set<String> emails =
    new HashSet<>();

emails.add("a@example.com");
emails.add("a@example.com");
```

Kích thước (size / 크기) vẫn 1.

`LinkedHashSet` preserve insertion thứ tự (order / 순서). `TreeSet` sorted theo natural/comparator thứ tự (order / 순서).

Set tính đúng đắn (correctness / 정확성) phụ thuộc `equals/hashCode` hoặc thứ tự (ordering / 순서) comparator. Mutable element fields dùng trong equality/băm (hash / 해시) có thể phá lookup.

---

# 43. `Map`

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
Map<Long, User> users =
    new HashMap<>();
```

Dùng chung (common / 공통):

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

Nó diễn đạt grouping/indexing mẫu (pattern / 패턴) rõ hơn manual check-then-put.

`merge` tốt cho counting:

```java
counts.merge(word, 1, Integer::sum);
```

Đây là ví dụ Java API chứa patterns mà bạn nên nhận ra, không chỉ thuộc phương thức (method / 메서드) names.

---

# 44. `HashMap`, `LinkedHashMap`, `TreeMap`

`HashMap` là default general-purpose map khi không cần thứ tự (ordering / 순서).

`LinkedHashMap` giữ insertion thứ tự (order / 순서) hoặc có thể dùng access-order cho LRU-like lô-gic (logic / 논리).

`TreeMap` giữ sorted keys dựa comparator/natural thứ tự (order / 순서) với tree-based độ phức tạp (complexity / 복잡도).

Đừng chọn `TreeMap` chỉ vì “sorted đẹp”; sorting có chi phí (cost / 비용). Chọn khi sorted điều hướng (navigation / 내비게이션)/phạm vi (range / 범위) ngữ nghĩa (semantics / 의미론) thực sự cần.

---

# 45. Immutable collection factory methods từ Java 9

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

```java
List<String> names =
    List.of("Kim", "Lee");

Set<String> roles =
    Set.of("USER", "ADMIN");

Map<String, Integer> limits =
    Map.of("A", 10, "B", 20);
```

Các factory này tạo unmodifiable collections và reject `null`.

Nếu nhận mutable danh sách (list / 목록) từ caller mà muốn quyền sở hữu (ownership / 소유권) snapshot:

```java
this.roles =
    List.copyOf(roles);
```

Điều này tốt hơn giữ bên ngoài (external / 외부) mutable tham chiếu (reference / 참조).

Unmodifiable view và immutable snapshot khác nhau. `Collections.unmodifiableList(original)` ngăn mutate qua view nhưng nếu `original` bị mutate, view vẫn đổi. `List.copyOf(original)` tạo snapshot-style collection independent theo structural trạng thái (state / 상태) tại thời điểm bản sao (copy / 복사).

---

# 46. Generics: kiểu (type / 타입) an toàn (safety / 안전) trước khi thời gian chạy (runtime / 런타임)

Without generics:

```java
List values = new ArrayList();
values.add("hello");
values.add(123);
```

Trình biên dịch (compiler / 컴파일러) không bảo vệ.

With generics:

```java
List<String> values =
    new ArrayList<>();

values.add("hello");
// values.add(123); compile error
```

Generic kiểu (type / 타입) parameter cho reusable type-safe abstractions.

```java
class Box<T> {
    private T value;

    T get() {
        return value;
    }
}
```

Generic phương thức (method / 메서드):

```java
static <T> T first(List<T> values) {
    return values.get(0);
}
```

Beginner chỉ cần hiểu `T` là compile-time kiểu (type / 타입) parameter. kiểu (type / 타입) erasure, wildcard variance và PECS sẽ sang Intermediate.

---

# 47. Diamond Operator

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
Map<String, List<User>> users =
    new HashMap<String, List<User>>();
```

có thể viết:

```java
Map<String, List<User>> users =
    new HashMap<>();
```

Trình biên dịch (compiler / 컴파일러) infer kiểu (type / 타입) arguments từ left side/ngữ cảnh (context / 맥락).

Đây là giảm noise, không thay static typing.

---

# 48. Lambdas từ Java 8

Functional giao diện (interface / 인터페이스) có đúng một abstract phương thức (method / 메서드).

```java
@FunctionalInterface
interface DiscountPolicy {
    BigDecimal apply(BigDecimal price);
}
```

Hiện thực (implementation / 구현) anonymous lớp (class / 클래스):

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

Lambda giúp hành vi (behavior / 동작) trở thành giá trị (value / 값) truyền vào phương thức (method / 메서드), rất hợp với chiến lược (strategy / 전략).

---

# 49. tiêu chuẩn (standard / 표준) Functional Interfaces

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

`Consumer<T>` nhận T và không return useful giá trị (value / 값).

```java
Consumer<String> printer =
    System.out::println;
```

`Supplier<T>` không nhận đầu vào (input / 입력) và tạo T.

```java
Supplier<UUID> idGenerator =
    UUID::randomUUID;
```

Khi lambda phức tạp nhiều lines/conditions, named phương thức (method / 메서드) hoặc named chiến lược (strategy / 전략) lớp (class / 클래스) có thể rõ hơn.

---

# 50. phương thức (method / 메서드) References

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
users.stream()
    .map(User::name)
```

tương đương gần ý nghĩa:

```java
users.stream()
    .map(user -> user.name())
```

Phương thức (method / 메서드) tham chiếu (reference / 참조) tốt khi mục tiêu (target / 대상) phương thức (method / 메서드) name diễn đạt rõ. Nếu phải đoán receiver/overload, lambda tường minh (explicit / 명시적) có thể dễ đọc hơn.

---

# 51. Stream API

Stream là chuỗi xử lý (pipeline / 파이프라인) xử lý dữ liệu (data / 데이터), không phải collection lưu dữ liệu (data / 데이터).

```java
List<String> activeNames =
    users.stream()
         .filter(User::isActive)
         .map(User::name)
         .sorted()
         .toList();
```

Luồng (flow / 흐름):

```text
source
→ filter
→ transform
→ order
→ terminal result
```

Intermediate operations như `filter`, `map`, `sorted` thường lazy; terminal thao tác (operation / 연산) như `toList`, `count`, `findFirst` kích hoạt evaluation.

Stream single-use. Sau terminal thao tác (operation / 연산), không reuse cùng stream.

---

# 52. Khi nào Stream dễ đọc?

Transformation chuỗi xử lý (pipeline / 파이프라인):

```java
users.stream()
     .filter(User::isActive)
     .map(User::email)
     .toList();
```

rất rõ.

Nếu lô-gic (logic / 논리) có nhiều side effects, nested lỗi (error / 오류) handling và trạng thái (state / 상태) mutations, vòng lặp (loop / 루프) có thể rõ hơn.

Đừng viết stream chỉ để chứng minh “Java hiện đại”. Chọn biểu diễn (representation / 표현) giúp người đọc thấy intent.

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

Đây là declarative dữ liệu (data / 데이터) transformation.

---

# 54. Terminal operations

`forEach` thực hiện hành động (action / 동작):

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

Optional biểu diễn “có giá trị (value / 값) hoặc không” một cách tường minh (explicit / 명시적) trong return kiểu (type / 타입).

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

`Optional.of(null)` throw NPE; dùng `ofNullable` nếu giá trị (value / 값) có thể null.

Optional hữu ích cho return ngữ nghĩa (semantics / 의미론). Không cần dùng `Optional` cho mọi trường dữ liệu (field / 필드)/parameter.

---

# 56. `orElse` vs `orElseGet`

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
optional.orElse(
    expensiveFallback());
```

`expensiveFallback()` được evaluate trước khi `orElse` được gọi, kể cả Optional có giá trị (value / 값).

```java
optional.orElseGet(
    this::expensiveFallback);
```

supplier chỉ chạy khi empty.

Đây là ví dụ API laziness ảnh hưởng hiệu năng (performance / 성능)/side tác động (effect / 효과).

---

# 57. Sorting: Comparable và Comparator ở mức Beginner

Natural thứ tự (order / 순서):

```java
class User
        implements Comparable<User> {
    ...
}
```

Nhưng một lĩnh vực (domain / 도메인) kiểu (type / 타입) có thể có nhiều sort orders, nên `Comparator` thường linh hoạt.

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

# 58. Date/thời gian (time / 시간) API

Legacy `Date`/`Calendar` có many thiết kế (design / 설계) problems. Java 8 `java.time` nên là default.

`LocalDate` là ngày không timezone:

```java
LocalDate birthday =
    LocalDate.of(2000, 7, 26);
```

`LocalTime` là giờ trong ngày không date/zone.

`LocalDateTime` là date+thời gian (time / 시간) nhưng vẫn không timezone/offset.

`Instant` là timestamp trên UTC timeline.

`ZonedDateTime` kết hợp cục bộ (local / 로컬) date-time với time-zone rules.

Nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) “store chính xác (exact / 정확한) sự kiện (event / 이벤트) thời gian (time / 시간)” thường dùng `Instant`. Display theo Seoul dùng `ZoneId.of("Asia/Seoul")`.

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

“30 days” và “1 month” không phải luôn cùng nghĩa. Calendar arithmetic và elapsed thời gian (time / 시간) là hai lĩnh vực (domain / 도메인) khác nhau.

---

# 60. DateTimeFormatter

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
DateTimeFormatter formatter =
    DateTimeFormatter.ofPattern(
        "yyyy-MM-dd");

String text =
    date.format(formatter);
```

Prefer tiêu chuẩn (standard / 표준) ISO format khi Đặc tả API (API contract / API 계약) không cần custom.

Parse/format ở ranh giới (boundary / 경계); cốt lõi (core / 핵심) nên giữ typed date/thời gian (time / 시간).

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

BigDecimal immutable, nên phải giữ kết quả (result / 결과).

Comparison:

```java
a.compareTo(b) == 0
```

thường phù hợp numeric equality hơn `equals`, vì `equals` còn xem quy mô (scale / 규모):

```text
1.0 != 1.00 theo equals
```

Chính sách (policy / 정책) rounding nên nằm ở lĩnh vực (domain / 도메인) kiểu (type / 타입)/dịch vụ (service / 서비스), không rải `setScale(... HALF_UP)` khắp mã (code / 코드).

---

# 62. tệp (file / 파일) I/O với đường dẫn (path / 경로) và Files

Hiện đại (modern / 현대적) API:

```java
Path path =
    Path.of("data", "users.txt");
```

Không tự concatenate:

```java
"data/" + filename
```

vì đường dẫn (path / 경로) separator/nền tảng (platform / 플랫폼)/bảo mật (security / 보안) concerns.

Read văn bản (text / 텍스트) Java 11+:

```java
String content =
    Files.readString(
        path,
        StandardCharsets.UTF_8);
```

Ghi (write / 쓰기):

```java
Files.writeString(
    path,
    content,
    StandardCharsets.UTF_8);
```

Bản sao (copy / 복사):

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

Always make charset tường minh (explicit / 명시적) when tệp (file / 파일) đặc tả hợp đồng (contract / 계약) matters.

---

# 63. Streams trong I/O: InputStream, Reader, Buffered layers

`InputStream` xử lý bytes.

`Reader` xử lý characters.

Nếu đọc văn bản (text / 텍스트) từ byte stream, cần charset.

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

Buffered wrappers giảm calls xuống underlying tài nguyên (resource / 자원).

Decorator mẫu (pattern / 패턴) xuất hiện ở Java I/O: bạn wrap một stream để thêm hành vi (behavior / 동작).

```text
FileInputStream
→ BufferedInputStream
→ DataInputStream
```

Đừng học tên mẫu (pattern / 패턴) trước luồng (flow / 흐름); hãy nhìn việc mỗi tầng (layer / 계층) bọc tầng (layer / 계층) dưới và bổ sung năng lực (capability / 역량).

---

# 64. Annotations

Annotation là siêu dữ liệu (metadata / 메타데이터).

```java
@Override
public String toString() {
}
```

`@Override` giúp trình biên dịch (compiler / 컴파일러) verify phương thức (method / 메서드) thật sự override.

`@Deprecated` báo API cũ.

`@SuppressWarnings` tắt trình biên dịch (compiler / 컴파일러) warning có chủ đích.

Custom:

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Audited {
}
```

Annotation tự nó không chạy hành vi (behavior / 동작). Một trình biên dịch (compiler / 컴파일러), annotation processor, khung phần mềm (framework / 프레임워크) hoặc reflection mã (code / 코드) phải đọc nó.

Đây là kiến thức cực quan trọng trước Spring: `@Transactional` không phải giao dịch (transaction / 트랜잭션) engine; Spring hạ tầng (infrastructure / 인프라) đọc siêu dữ liệu (metadata / 메타데이터) rồi tạo hành vi (behavior / 동작).

---

# 65. Immutability và Defensive bản sao (copy / 복사)

Immutable đối tượng (object / 객체) không thay logical trạng thái (state / 상태) sau construction.

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

caller còn giữ mutable danh sách (list / 목록) và có thể thay trạng thái (state / 상태) đối tượng (object / 객체) từ bên ngoài.

Defensive bản sao (copy / 복사) ở quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계) giúp đối tượng (object / 객체) kiểm soát trạng thái (state / 상태).

Immutability giảm synchronization surface trong tính đồng thời (concurrency / 동시성) và làm caching/equality dễ hơn.

---

# 66. Basic lỗi (error / 오류) Handling kiến trúc (architecture / 아키텍처)

Không phải mọi lỗi (error / 오류) giống nhau.

Invalid đầu vào (input / 입력):

```java
throw new IllegalArgumentException(...);
```

Nghiệp vụ (business / 비즈니스) absence:

```java
UserNotFoundException
```

Hạ tầng (infrastructure / 인프라):

```java
DataAccessException-like
```

Programming bug:

```text
NullPointerException
IllegalStateException
```

Ranh giới (boundary / 경계) như HTTP/CLI có thể translate exceptions thành phản hồi (response / 응답)/exit mã (code / 코드).

Đừng catch tất cả ở mọi tầng (layer / 계층) rồi log + rethrow; bạn sẽ có duplicate logs và mất quyền sở hữu (ownership / 소유권).

---

# 67. Basic API thiết kế (design / 설계)

Prefer ngữ nghĩa (semantic / 의미적) kiểu (type / 타입):

```java
UserId
```

over passing unrelated `long` values nếu lĩnh vực (domain / 도메인) đủ phức tạp.

Prefer empty danh sách (list / 목록):

```java
return List.of();
```

over null khi “không có items” là normal.

Phương thức (method / 메서드) name phải mô tả intent:

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

khó đọc. Có thể dùng options đối tượng (object / 객체)/enum/named methods khi flags tăng.

---

# 68. chiến lược (strategy / 전략) mẫu (pattern / 패턴) trong Java thực tế

Đặc tả hợp đồng (contract / 계약):

```java
interface DiscountPolicy {
    Money discount(Order order);
}
```

Hiện thực (implementation / 구현):

```java
final class VipDiscountPolicy
        implements DiscountPolicy {
}
```

Caller không cần `if` theo hiện thực (implementation / 구현).

Lambda có thể implement chiến lược (strategy / 전략) nếu hành vi (behavior / 동작) nhỏ:

```java
DiscountPolicy none =
    order -> Money.zero();
```

Chiến lược (strategy / 전략) là “thay hành vi (behavior / 동작) bằng composition”, không phải “cứ có giao diện (interface / 인터페이스) là chiến lược (strategy / 전략)”.

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

Factory có lợi khi construction cần kiểm tra hợp lệ (validation / 검증), caching, subtype selection hoặc tên có meaning.

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

Builder phù hợp đối tượng (object / 객체) có nhiều optional cấu hình (config / 설정); không cần builder cho bản ghi (record / 레코드) 2 fields.

---

# 71. Repository mẫu (pattern / 패턴) awareness

Nghiệp vụ (business / 비즈니스) mã (code / 코드):

```java
interface UserRepository {
    Optional<User> findById(UserId id);
    void save(User user);
}
```

Hạ tầng (infrastructure / 인프라) hiện thực (implementation / 구현) có thể JDBC, tệp (file / 파일) hoặc bộ nhớ (memory / 메모리).

Repository giúp cốt lõi (core / 핵심) không phụ thuộc lưu trữ (storage / 저장소) detail và tạo kiểm thử (test / 테스트) seam.

Spring dữ liệu (data / 데이터) JPA sau này generate repository hiện thực (implementation / 구현), nhưng mẫu (pattern / 패턴) tồn tại trước Spring.

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

đừng chỉ đọc exception lớp (class / 클래스). Đọc dấu vết ngăn xếp (stack trace / 스택 트레이스) từ top exception + cause chuỗi (chain / 사슬) và tìm **first frame thuộc mã (code / 코드) của bạn** gần lỗi.

Workflow tốt:

```text
reproduce
→ minimize/isolate
→ inspect actual values
→ form hypothesis
→ change one thing
→ verify
```

Không sửa nhiều lines cùng lúc rồi không biết thay đổi (change / 변경) nào giải quyết.

---

# 73. Basic CLI và JAR

Compile đầu ra (output / 출력):

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

Danh sách (list / 목록):

```bash
jar --list \
    --file app.jar
```

Cấp cao (senior / 시니어) habit bắt đầu từ Beginner: khi thời gian chạy (runtime / 런타임) khác cục bộ (local / 로컬), inspect actual sản phẩm tạo ra (artifact / 산출물)/phiên bản (version / 버전) thay vì chỉ inspect nguồn (source / 소스).

---

# 74. Java 8 → 11 → 17 → 21: phiên bản (version / 버전) thay đổi cách lập trình như thế nào?

Nếu chỉ học phiên bản (version / 버전) bằng danh sách “bản phát hành (release / 릴리스) X thêm tính năng (feature / 기능) Y”, bạn rất nhanh quên. Cách hữu ích hơn là nhìn bốn generation như bốn lần **thay đổi phong cách viết và vận hành Java**.

**Java 8** là mốc đưa functional style thực dụng vào Java ứng dụng (application / 애플리케이션) mã (code / 코드). Lambda, phương thức (method / 메서드) tham chiếu (reference / 참조) và Stream không chỉ rút ngắn cú pháp; chúng biến *hành vi (behavior / 동작)* thành thứ có thể truyền vào API. Trước Java 8, một `Comparator`, callback hoặc `Runnable` thường được viết bằng anonymous lớp (class / 클래스) dài:

```java
Collections.sort(users,
    new Comparator<User>() {
        @Override
        public int compare(User a, User b) {
            return a.name().compareTo(b.name());
        }
    });
```

Java 8 cho phép diễn đạt intent trực tiếp hơn:

```java
users.sort(
    Comparator.comparing(User::name));
```

Stream API tiếp tục ý tưởng này cho dữ liệu (data / 데이터) transformation, còn `java.time` thay đổi cách xử lý thời gian từ `Date`/`Calendar` mutable và dễ sai sang những kiểu (type / 타입) có ngữ nghĩa (semantic / 의미적) rõ như `LocalDate`, `Instant`, `Duration`. Vì rất nhiều enterprise mã (code / 코드) từng baseline Java 8 trong thời gian dài, bạn phải đọc được cả anonymous classes, `Date`/`Calendar` lẫn mã (code / 코드) hiện đại tương đương.

**Java 11** nên được hiểu như mốc Java hiện đại đầu tiên sau quá trình modular hóa JDK. Ở ứng dụng (application / 애플리케이션) mã (code / 코드) có các API nhỏ nhưng hữu ích như `String.isBlank()`, `strip()`, `lines()`, `Files.readString()` và tiêu chuẩn (standard / 표준) `HttpClient`. Quan trọng hơn với enterprise di chuyển (migration / 마이그레이션) là một số Java EE/CORBA modules như JAXB/JAX-WS không còn được bundle trong JDK. Một dự án (project / 프로젝트) Java 8 từng compile chỉ vì JAXB “có sẵn trong JDK” có thể thất bại (fail / 실패) khi lên 11 cho tới khi bản dựng (build / 빌드) khai báo phụ thuộc (dependency / 의존성) rõ. Từ đây bạn phải phân biệt **Java SE nền tảng (platform / 플랫폼)** với khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) dependencies của ứng dụng (application / 애플리케이션).

**Java 17** làm lĩnh vực (domain / 도메인) modeling và nền tảng (platform / 플랫폼) encapsulation mạnh hơn. Records giúp dữ liệu (data / 데이터) carrier/value-like objects giảm boilerplate; sealed classes giúp mô hình một tập subtype đóng; mẫu (pattern / 패턴) matching cho `instanceof` giảm cast ceremony. Quan trọng hơn ở môi trường vận hành (production / 운영 환경) di chuyển (migration / 마이그레이션), JDK internals bị strong encapsulation theo default mạnh hơn trước. khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) cũ dùng deep reflection vào private internals của `java.*` có thể gặp `InaccessibleObjectException`, vì vậy mã (code / 코드) bền vững hơn phải dựa supported API thay vì nội bộ (internal / 내부) hiện thực (implementation / 구현).

Trước records, một dữ liệu (data / 데이터) carrier có thể cần constructor, accessors và equality boilerplate. Với Java 17, intent có thể được biểu diễn rõ hơn:

```java
record UserSummary(
    long id,
    String name) {
}
```

Ý nghĩa không chỉ là “bản ghi (record / 레코드) ngắn hơn lớp (class / 클래스)”, mà là ngôn ngữ (language / 언어) có một cách biểu diễn rõ ràng kiểu (type / 타입) chủ yếu được định nghĩa bởi dữ liệu của nó.

**Java 21** thay đổi hai hướng lớn. Hướng thứ nhất là data-oriented programming: bản ghi (record / 레코드) patterns và mẫu (pattern / 패턴) matching for `switch` làm closed/sealed mô hình (model / 모델) dễ destructure và xử lý exhaustive hơn. Hướng thứ hai là tính đồng thời (concurrency / 동시성): Virtual Threads được final. Với nhiều I/O-bound máy chủ (server / 서버) workloads, bạn có thể giữ imperative blocking style mà quy mô (scale / 규모) số concurrent tasks cao hơn thay vì buộc ứng dụng (application / 애플리케이션) chuyển sang callback/reactive style chỉ để tiết kiệm OS threads.

```java
try (var executor =
        Executors.newVirtualThreadPerTaskExecutor()) {
    Future<Response> future =
        executor.submit(this::callRemoteService);
    return future.get();
}
```

Virtual luồng thực thi (thread / 스레드) không làm cơ sở dữ liệu (database / 데이터베이스), CPU hay bên ngoài (external / 외부) API nhanh hơn. Nó thay **chi phí (cost / 비용) mô hình (model / 모델) của luồng thực thi (thread / 스레드)**, không thay sức chứa (capacity / 용량) của downstream tài nguyên (resource / 자원). Phần Intermediate và cấp cao (senior / 시니어) sẽ mở kỹ điểm này.

Các bản phát hành (release / 릴리스) 9, 10, 14, 15 và 16 vẫn quan trọng vì collection factories, `var`, switch expressions, văn bản (text / 텍스트) blocks, records và mẫu (pattern / 패턴) matching đã hình thành Java hiện đại. Tuy nhiên hãy học chúng theo **vấn đề chúng loại bỏ** thay vì nhớ chronology. LTS cũng không có nghĩa tính năng (feature / 기능) “tốt hơn”; nó chủ yếu phản ánh hỗ trợ (support / 지원) cadence phù hợp long-lived môi trường vận hành (production / 운영 환경).

---

# 75. gói (package / 패키지) by tính năng (feature / 기능) và cấu trúc dự án (project structure / 프로젝트 구조)

Technical-layer-only:

```text
controller/
service/
repository/
model/
```

đơn giản khi dự án (project / 프로젝트) nhỏ.

Tính năng (feature / 기능) cấu trúc (structure / 구조):

```text
user/
order/
payment/
```

giúp mã (code / 코드) cùng nghiệp vụ (business / 비즈니스) năng lực (capability / 역량) nằm gần nhau.

Trong mỗi tính năng (feature / 기능) bạn có thể giữ classes package-private để hạn chế accidental phụ thuộc (dependency / 의존성).

Bạn chưa cần DDD/mô-đun (module / 모듈) kiến trúc (architecture / 아키텍처) ở Beginner. Chỉ cần hình thành thói quen: gói (package / 패키지) cấu trúc (structure / 구조) phải giúp phụ thuộc (dependency / 의존성) dễ hiểu, không phải chỉ giúp IDE nhìn đẹp.

---

# 76. Testing Mindset

Mã (code / 코드):

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

Kiểm thử (test / 테스트) có thể inject deterministic `Clock.fixed(...)` và fake chính sách (policy / 정책).

Nếu phương thức (method / 메서드) gọi trực tiếp:

```java
Instant.now()
```

và `new RealPaymentGateway()`, hành vi (behavior / 동작) khó điều khiển (control / 제어) hơn.

Phụ thuộc (dependency / 의존성) Injection không phải mẫu (pattern / 패턴) riêng của Spring. Nó là plain Java thiết kế (design / 설계) để testability và decoupling tốt.

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

Tốt hơn nữa nếu finite nghiệp vụ (business / 비즈니스) statuses:

```java
OrderStatus.DONE
```

Enum loại typo và centralize lĩnh vực (domain / 도메인) states.

---

# 78. Anti-pattern: Return null collection

Bad:

```java
List<User> findUsers() {
    return null;
}
```

caller phải null-check trước vòng lặp (loop / 루프).

Better:

```java
return List.of();
```

“không có kết quả (result / 결과)” là empty chuỗi (sequence / 시퀀스), không phải absence của collection đối tượng (object / 객체).

---

# 79. Anti-pattern: `double` cho Money

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
double total = 0.1 + 0.2;
```

không phù hợp chính xác (exact / 정확한) decimal monetary ngữ nghĩa (semantics / 의미론).

Use `BigDecimal` + currency + rounding chính sách (policy / 정책).

Một lĩnh vực (domain / 도메인) `Money` giá trị (value / 값) đối tượng (object / 객체) có thể encapsulate cả ba để tránh mã (code / 코드) rải rounding.

---

# 80. Anti-pattern: Giant phương thức (method / 메서드)

Một phương thức (method / 메서드) 300 lines thường chứa nhiều levels of lớp trừu tượng (abstraction / 추상화).

Không phải cứ >20 lines là xấu. Nhưng nếu phương thức (method / 메서드) vừa parse đầu vào (input / 입력), truy vấn (query / 쿼리) DB, calculate, format email và ghi (write / 쓰기) tệp (file / 파일), responsibility đang trộn.

Extract methods/classes theo meaningful hành vi (behavior / 동작), không theo arbitrary line count.

---

# 81. Anti-pattern: Mutable Static toàn cục (global / 전역) trạng thái (state / 상태)

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
public static Map<String, User>
    USERS = new HashMap<>();
```

làm trạng thái (state / 상태) toàn cục (global / 전역), thread-safety khó, tests ảnh hưởng nhau và vòng đời (lifecycle / 생명주기) mơ hồ.

Prefer tường minh (explicit / 명시적) đơn vị sở hữu (owner / 오너) đối tượng (object / 객체)/dịch vụ (service / 서비스)/repository.

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

cho một hàm (function / 함수) 5 lines.

Mẫu (pattern / 패턴) là phản hồi (response / 응답) tới lực thiết kế, không phải checklist cần nhét vào dự án (project / 프로젝트).

Mã (code / 코드) trực tiếp, rõ và dễ thay trước. lớp trừu tượng (abstraction / 추상화) khi variation/coupling thực sự xuất hiện.

---

# 83. Beginner dự án (project / 프로젝트) đề xuất

Hãy viết plain Java `Order Processing CLI`.

Lĩnh vực (domain / 도메인) gồm `Order`, `OrderItem`, `Money`, `OrderStatus`, `CustomerId`.

Đầu vào (input / 입력) đọc từ tệp (file / 파일) CSV hoặc console, parse thành typed objects. kiểm tra hợp lệ (validation / 검증) phải xảy ra ở ranh giới (boundary / 경계). Repository ban đầu in-memory. Pricing dùng `DiscountPolicy` chiến lược (strategy / 전략). đầu ra (output / 출력) ghi kết quả (result / 결과) tệp (file / 파일) bằng `Files`.

Dùng collections, streams ở nơi phù hợp, exceptions có taxonomy cơ bản, `Clock` inject nếu cần thời gian (time / 시간), `BigDecimal` cho money và `java.time` cho timestamps.

Sau đó viết tests cho lĩnh vực (domain / 도메인)/dịch vụ (service / 서비스) mà không khung phần mềm (framework / 프레임워크).

Dự án (project / 프로젝트) này là cầu nối (bridge / 브리지) rất tốt trước JDBC/tính đồng thời (concurrency / 동시성)/Spring.

---

# 84. Beginner → Intermediate Gate

Trước khi sang Part 2, bạn phải có thể tự giải thích Java nguồn (source / 소스) được compile/run ra sao, thành phần nguyên thủy (primitive / 기본 요소)/tham chiếu (reference / 참조)/null khác nhau, Java pass-by-value nghĩa gì, `==` và `equals` khác gì, constructor/encapsulation/inheritance/polymorphism/interfaces dùng để giải quyết bài toán (problem / 문제) nào và tại sao composition thường linh hoạt.

Bạn phải chọn được `List`, `Set`, `Map`; biết `HashMap`/`ArrayList` là default use cases nào; dùng generics, lambda, Stream chuỗi xử lý (pipeline / 파이프라인), Optional, Comparator, `java.time`, `BigDecimal`, `Path`/`Files` và try-with-resources.

Bạn phải hiểu rằng annotations là siêu dữ liệu (metadata / 메타데이터), immutability và defensive bản sao (copy / 복사) liên quan quyền sở hữu (ownership / 소유권), exceptions cần preserve cause và resources phải có vòng đời (lifecycle / 생명주기) rõ.

Quan trọng nhất, bạn phải nhìn mã (code / 코드) không chỉ như cú pháp mà như **đặc tả hợp đồng (contract / 계약) + quyền sở hữu (ownership / 소유권) + trạng thái (state / 상태) + hành vi (behavior / 동작)**.

---

# 85. Điều cố ý chưa đào sâu

Part 1 chưa đào sâu wildcard/PECS/kiểu (type / 타입) erasure, Stream collectors nâng cao, Java bộ nhớ (memory / 메모리) mô hình (model / 모델), locks, executors, CompletableFuture, JDBC giao dịch (transaction / 트랜잭션) internals, reflection/proxy/nạp lớp (class loading / 클래스 로딩), JVM bộ nhớ (memory / 메모리)/GC/JIT và môi trường vận hành (production / 운영 환경) diagnostics. Những phần đó thuộc Intermediate.

Senior-level thời gian chạy (runtime / 런타임) như bytecode/JIT deoptimization, safe publication, tranh chấp khóa (lock contention / 잠금 경합), GC tuning, JFR, virtual-thread môi trường vận hành (production / 운영 환경) mô hình (model / 모델), phân tán (distributed / 분산) consistency và kiến trúc (architecture / 아키텍처) sẽ ở Part 3.

Master Supplement sẽ bổ sung low-level areas như VarHandle, AQS, luồng (flow / 흐름), Spliterator/Gatherers, FFM, class-file API, agents/instrumentation và Java 22–26 evolution.

---

# 86. Kết luận Part 1

Nếu chỉ nhớ cú pháp (syntax / 문법), bạn có thể viết mã (code / 코드) chạy. Nếu hiểu kiểu (type / 타입) contracts, quyền sở hữu (ownership / 소유권), mutability, exceptions, resources và lớp trừu tượng (abstraction / 추상화), bạn bắt đầu viết Java có thể maintain.

Mô hình tư duy (mental model / 사고 모델) cuối Part 1 nên là:

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

Khi ba luồng (flow / 흐름) này trở thành tự nhiên, Part 2 mới thực sự có ý nghĩa, vì tính đồng thời (concurrency / 동시성), reflection, JDBC và JVM đều xây trên nền đó.

---

# References for version-sensitive topics

Oracle Java SE hỗ trợ (support / 지원) Roadmap:
https://www.oracle.com/java/technologies/java-se-support-roadmap.html

Oracle JDK 25 bản phát hành (release / 릴리스) notes:
https://www.oracle.com/java/technologies/javase/25all-relnotes.html

Oracle JDK 26 bản phát hành (release / 릴리스) notes:
https://www.oracle.com/java/technologies/javase/26all-relnotes.html

Oracle Java ngôn ngữ (language / 언어) documentation:
https://docs.oracle.com/en/java/javase/

> **Bàn giao:** Sau **Cách đọc bộ Java chuẩn gốc (canonical / 정본)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
