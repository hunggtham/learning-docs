# Java Core — Part 2: Intermediate — Rewritten Detailed
## Từ “biết viết Java” sang “hiểu contract, concurrency, runtime và boundary”

> Part 2 giả định bạn đã hoàn thành Part 1 và đã có thể tự viết một chương trình Java nhỏ bằng OOP, collections, Stream, Optional, `java.time`, file I/O và exceptions. Mục tiêu ở đây là nâng cách suy nghĩ từ “API nào làm được việc này?” thành “contract của API này là gì, object này thuộc về ai, thread nào được phép thay đổi state, resource tồn tại bao lâu, và lỗi nào có thể xảy ra ở runtime dù compiler vẫn cho qua?”.
>
> Các ghi chú kiểu Senior, idiom và pattern không được tách thành mục riêng sau mỗi chương. Khi một tư duy nâng cao cần thiết, nó được giải thích ngay trong nội dung cùng ví dụ để bạn học như một phần tự nhiên của Java.

---

# 1. Intermediate Java nghĩa là bắt đầu học theo contract

Ở Beginner, bạn học `List.add`, `Map.get`, `Stream.map`, `Optional.orElseThrow`. Ở Intermediate, điều quan trọng hơn là contract phía sau chúng. `HashMap` có yêu cầu gì với `equals()` và `hashCode()`? `Comparator` phải thỏa tính chất nào để `TreeSet` không hành xử kỳ lạ? `Stream` có lazy hay eager? `volatile` đảm bảo visibility nhưng không đảm bảo atomicity nghĩa là gì? `ExecutorService.shutdown()` khác `shutdownNow()` ra sao? Một JDBC `Connection` thuộc sở hữu của ai và khi nào được close?

Java có rất nhiều API; bạn không thể master bằng cách thuộc toàn bộ methods. Bạn phải học mental model và contract để có thể dự đoán behavior khi gặp API mới.

---

# 2. Generics không chỉ để bỏ cast

Beginner nhìn:

```java
List<String>
```

và hiểu list chỉ chứa String.

Intermediate cần hiểu generic type system giúp compiler kiểm tra **mối quan hệ type**, nhưng generic types trong Java phần lớn là invariant.

Ví dụ:

```java
List<Integer> integers =
    List.of(1, 2, 3);
```

Dù `Integer` là subtype của `Number`, điều này không hợp lệ:

```java
List<Number> numbers = integers;
```

Nếu cho phép, bạn có thể:

```java
numbers.add(3.14);
```

và `integers` bỗng chứa `Double`, phá type safety.

Vì vậy:

```text
Integer <: Number
```

không suy ra:

```text
List<Integer> <: List<Number>
```

Đây là invariance.

---

# 3. Wildcard `? extends T`

Nếu method chỉ **đọc** values như `T`, bạn có thể dùng upper-bounded wildcard.

```java
double sum(
        List<? extends Number> values) {

    double total = 0;

    for (Number value : values) {
        total += value.doubleValue();
    }

    return total;
}
```

Method này nhận:

```text
List<Integer>
List<Long>
List<Double>
```

vì mỗi element có thể đọc như `Number`.

Nhưng bạn không thể an toàn add `Integer` vào `List<? extends Number>` vì list thật có thể là `List<Double>`.

Mental model: `extends` làm producer flexible. Bạn biết lấy ra được `T`, nhưng không biết exact subtype để add.

---

# 4. Wildcard `? super T`

Nếu method cần **ghi** T vào collection:

```java
void addDefaults(
        List<? super Integer> target) {

    target.add(0);
    target.add(1);
}
```

`target` có thể là:

```text
List<Integer>
List<Number>
List<Object>
```

Bạn có thể add Integer vì tất cả những list đó đều chứa được Integer.

Khi đọc ra, static type an toàn nhất thường chỉ là `Object`.

Từ hai ý trên sinh ra mnemonic **PECS**: Producer Extends, Consumer Super. Đừng học thuộc câu đó nếu chưa hiểu variance; nó chỉ là cách nhớ contract đã giải thích.

---

# 5. Type parameter bounds

Generic method:

```java
static <T extends Comparable<T>>
T max(T a, T b) {
    return a.compareTo(b) >= 0
            ? a
            : b;
}
```

`T extends Comparable<T>` nói type T phải implement contract so sánh với chính T.

Multiple bounds:

```java
<T extends Closeable
        & Comparable<T>>
```

Nếu có class bound, nó phải đứng trước interface bounds.

Generic constraints giúp encode requirement ở compile time, thay vì runtime `instanceof` checks.

---

# 6. Type Erasure

Java generics được triển khai chủ yếu qua type erasure. Sau compile, runtime thường không giữ full generic type arguments theo cách bạn tưởng.

Ví dụ:

```java
List<String>
List<Integer>
```

đều là `List` ở nhiều runtime contexts.

Do đó:

```java
if (obj instanceof List<String>) {
}
```

không được phép.

Bạn chỉ có thể:

```java
if (obj instanceof List<?>) {
}
```

Type erasure giải thích vì sao không tạo được:

```java
new T[10]
```

và vì sao reflection generic metadata có giới hạn/phức tạp.

---

# 7. Raw Types và vì sao nguy hiểm

Legacy:

```java
List values = new ArrayList();
```

Raw type bypass generic checks.

```java
values.add("hello");
values.add(123);
```

Sau đó:

```java
List<String> strings = values;
```

có unchecked warning và runtime `ClassCastException` có thể xảy ra xa nơi bug được tạo.

Đừng suppress unchecked warnings cả package. Nếu phải interop với legacy/raw API, hãy cô lập cast ở một boundary nhỏ, validate dữ liệu rồi expose typed API cho phần còn lại.

---

# 8. Heap Pollution và `@SafeVarargs`

Generic varargs có thể tạo array representation không reified đầy đủ.

```java
static <T> void process(
        List<T>... lists) {
}
```

Compiler có thể cảnh báo heap pollution.

`@SafeVarargs` chỉ nên dùng khi implementation thực sự không làm unsafe operations với varargs array. Annotation này là lời hứa của programmer với compiler, không phải công cụ tắt warning tùy tiện.

---

# 9. Collections phải chọn theo semantics trước Big-O

Big-O cần biết nhưng không đủ. `ArrayList` và `LinkedList` có theoretical differences, nhưng CPU cache locality, allocation, traversal pattern và workload thật làm `ArrayList` thường tốt hơn trong application code.

Nếu cần indexed/read-heavy ordered sequence, bắt đầu bằng `ArrayList`.

Nếu cần uniqueness, dùng `Set`.

Nếu cần lookup bằng key, dùng `Map`.

Nếu cần priority order, dùng `PriorityQueue`.

Nếu cần FIFO/LIFO queue, `ArrayDeque` thường là lựa chọn tốt.

Collection type nên nói intent của domain. Nếu business invariant là “không duplicate SKU”, `Set<Sku>` encode intent tốt hơn `List<Sku>` + manual duplicate search.

---

# 10. `ArrayList.remove()` overload trap

```java
List<Integer> values =
    new ArrayList<>(
        List.of(10, 20, 30));

values.remove(1);
```

xóa element index 1, tức `20`.

Muốn xóa value 1:

```java
values.remove(
    Integer.valueOf(1));
```

Đây là ví dụ overloading + autoboxing có thể gây ambiguity về ý nghĩa. Khi API có overloaded primitive/object forms, đọc signature chứ đừng đoán.

---

# 11. `HashSet` và equality contract

`HashSet` dùng hash-based structure. Khi add object, hash code giúp chọn bucket; equality xác nhận object đã tồn tại chưa.

Nếu hai objects bằng nhau theo `equals`, chúng bắt buộc phải có cùng `hashCode`.

Sai contract có thể làm:

```text
set contains duplicate logical values
contains() trả false
remove() không tìm thấy object
```

Đây không phải “HashSet bug”; structure dựa vào contract của key.

---

# 12. Mutable keys là lỗi nguy hiểm

```java
final class UserKey {
    String email;

    // equals/hashCode use email
}
```

Add vào map:

```java
UserKey key =
    new UserKey("a@example.com");

map.put(key, user);
```

Sau đó mutate:

```java
key.email =
    "b@example.com";
```

Hash code thay đổi nhưng entry vẫn nằm ở bucket cũ.

```java
map.get(key)
```

có thể fail.

Map keys nên thường immutable theo fields dùng trong equality/hash. Đây là một lý do value objects và records rất hữu ích.

---

# 13. `LinkedHashMap`, `TreeMap`, `EnumMap`

`LinkedHashMap` preserve insertion order và có access-order mode, hữu ích cho cache-like structures nhỏ.

`TreeMap` giữ keys sorted dựa comparator, hỗ trợ range/navigation operations.

`EnumMap` chuyên cho enum keys, thường compact và fast hơn generic `HashMap<Enum,...>`.

Nếu key domain là enum:

```java
EnumMap<PaymentType, Handler>
```

thể hiện intent rất rõ.

---

# 14. Map như Index

Giả sử bạn có 100.000 users và lặp nhiều lần để tìm theo ID.

Bad:

```java
for each lookup:
    scan list
```

Better:

```java
Map<UserId, User> index =
    users.stream()
         .collect(
            Collectors.toMap(
                User::id,
                Function.identity()
            ));
```

Sau đó lookup O(1)-average.

“Index once, query many” là một programming pattern thường xuyên xuất hiện từ in-memory collections tới database indexes.

---

# 15. `computeIfAbsent` đúng cách

Grouping:

```java
Map<String, List<User>> byTeam =
    new HashMap<>();

for (User user : users) {
    byTeam.computeIfAbsent(
            user.team(),
            key -> new ArrayList<>())
        .add(user);
}
```

Mapping function nên đơn giản, nhanh và không gây side effect phức tạp, đặc biệt với concurrent maps. Nó có thể được gọi trong synchronization/atomic mechanics tùy implementation.

Không dùng `computeIfAbsent` để gọi remote API chậm mà không hiểu concurrency consequences.

---

# 16. `equals()` và `hashCode()` là contract hệ thống

Value object:

```java
public record UserId(long value) {
    public UserId {
        if (value <= 0) {
            throw new IllegalArgumentException();
        }
    }
}
```

Record tự cung cấp value-based equality.

Nếu custom class:

```java
final class Money {
    private final BigDecimal amount;
    private final Currency currency;
}
```

bạn phải quyết định equality semantics. `BigDecimal.equals` xem scale, nên `10.0` và `10.00` không equal. Nếu domain muốn numeric equality bất kể scale, normalize amount lúc construction hoặc custom equality carefully.

Equality không chỉ để test. Nó ảnh hưởng maps, sets, caches, ORM entities và deduplication.

---

# 17. `Comparable` vs `Comparator`

`Comparable<T>` định nghĩa natural order của type.

```java
class Version
        implements Comparable<Version> {
}
```

`Comparator<T>` định nghĩa external ordering strategy.

```java
Comparator<User> byName =
    Comparator.comparing(User::name);
```

Một type thường chỉ có một natural order hợp lý nhưng có thể có nhiều comparators.

Comparator phải consistent enough với ordering contract: antisymmetry/transitivity và behavior ổn định. Comparator inconsistent có thể làm `TreeSet` tưởng hai objects “trùng” nếu compare trả 0 dù `equals` false.

Đây là lý do sorting contract không chỉ là “return negative/zero/positive”.

---

# 18. Immutable, Unmodifiable và Defensive Copy khác nhau

```java
List<String> original =
    new ArrayList<>();

List<String> view =
    Collections.unmodifiableList(
        original);
```

Không thể mutate qua `view`, nhưng:

```java
original.add("A");
```

thì `view` nhìn thấy `"A"`.

`List.copyOf(original)` tạo unmodifiable snapshot về structure tại thời điểm copy.

Nếu class cần own collection state:

```java
this.roles =
    List.copyOf(roles);
```

rõ hơn giữ external mutable list.

Nhưng nếu elements mutable, shallow copy không deep-copy elements. Ownership phải reason toàn object graph.

---

# 19. Stream là lazy pipeline

```java
Stream<User> stream =
    users.stream()
         .filter(user -> {
             System.out.println(
                 "filter " + user.id());
             return user.active();
         });
```

Chưa có terminal operation, filter có thể chưa chạy.

Khi:

```java
long count = stream.count();
```

pipeline mới evaluate.

Laziness cho phép optimization và short-circuit.

```java
users.stream()
     .filter(...)
     .findFirst();
```

có thể dừng khi tìm thấy first match.

Không dựa vào stream pipeline để thực hiện side effect order phức tạp nếu semantics quan trọng.

---

# 20. `flatMap`

Nếu:

```java
List<Order> orders
```

mỗi order có:

```java
List<OrderItem> items
```

Muốn một flat stream items:

```java
List<OrderItem> items =
    orders.stream()
          .flatMap(
              order ->
                order.items().stream())
          .toList();
```

`map` sẽ tạo `Stream<List<OrderItem>>`; `flatMap` flatten nested streams.

Optional:

```java
Optional<Address> address =
    userRepository.findById(id)
        .flatMap(User::shippingAddress);
```

`flatMap` rất quan trọng khi composition trả container/context cùng loại.

---

# 21. Collectors nâng cao

Group:

```java
Map<String, List<User>> byTeam =
    users.stream()
         .collect(
            Collectors.groupingBy(
                User::team));
```

Count:

```java
Map<String, Long> counts =
    users.stream()
         .collect(
            Collectors.groupingBy(
                User::team,
                Collectors.counting()
            ));
```

Partition boolean:

```java
Map<Boolean, List<User>> split =
    users.stream()
         .collect(
            Collectors.partitioningBy(
                User::active));
```

Collectors giúp biến stream thành aggregated data structures.

---

# 22. `toMap` duplicate key trap

```java
users.stream()
     .collect(
         Collectors.toMap(
             User::email,
             Function.identity()
         ));
```

Nếu duplicate email, collector throw `IllegalStateException`.

Bạn phải quyết định business policy:

```java
Collectors.toMap(
    User::email,
    Function.identity(),
    (first, second) -> first
)
```

Nhưng silent “first wins” chỉ đúng nếu domain cho phép. Duplicate key thường có thể là data-quality bug nên fail-fast tốt hơn.

---

# 23. `reduce`

Sum:

```java
int total =
    numbers.stream()
           .reduce(
               0,
               Integer::sum);
```

`reduce` kết hợp elements thành một value.

Accumulator phải associative nếu muốn parallel semantics đúng.

Dùng specialized collectors/methods khi dễ đọc hơn. Không biến mọi aggregation thành abstract reduce nếu `sum()`/`count()`/collector thể hiện intent rõ hơn.

---

# 24. Primitive Streams

```java
int totalAge =
    users.stream()
         .mapToInt(User::age)
         .sum();
```

`IntStream`, `LongStream`, `DoubleStream` giảm boxing và có operations như `sum`, `average`.

Hot data-processing code có thể benefit, nhưng clarity trước. Đừng dùng primitive streams chỉ vì sợ boxing trong small business path chưa profile.

---

# 25. Parallel Stream

```java
users.parallelStream()
```

không tự động nhanh hơn.

Parallel work có overhead split/merge/scheduling và thường dùng common `ForkJoinPool`. Nếu operation blocking HTTP/DB, bạn có thể làm common pool starvation hoặc uncontrolled fan-out.

Chỉ parallelize khi workload CPU-bound/splittable, dataset đủ lớn và benchmark chứng minh.

Trong server application, explicit executor/concurrency limit thường dễ kiểm soát hơn parallel stream.

---

# 26. Optional nâng cao

`Optional` nên thường là return type để nói “result có thể không tồn tại”.

Bad style:

```java
void process(
    Optional<User> user)
```

thường làm caller phải wrap value vô ích.

Field Optional cũng có framework/serialization concerns.

`orElseGet` lazy như Part 1.

Java 9 thêm `ifPresentOrElse`, `or`, `stream`; Java 11 thêm `isEmpty`.

Optional pipeline:

```java
String email =
    repository.findById(id)
              .filter(User::active)
              .map(User::email)
              .orElseThrow(...);
```

Nếu chain trở nên khó debug, explicit branching có thể rõ hơn.

---

# 27. Exception Design

Exception should carry semantics and cause.

Bad:

```java
catch (SQLException e) {
    throw new RuntimeException(
        "failed");
}
```

Better:

```java
catch (SQLException e) {
    throw new UserDataAccessException(
        "Failed to load user " + id,
        e);
}
```

Original cause preserved.

Catch nơi bạn có thể add value. Nếu layer chỉ catch để log `"error"` rồi rethrow, top layer sẽ log lại và tạo duplicate stack traces.

---

# 28. Exception Translation at Boundaries

Database layer có vendor exception. Application layer cần data-access semantics. HTTP layer cần status/error contract.

Flow:

```text
SQLException
→ UserRepositoryException
→ application decision
→ HTTP 503/500 or domain response
```

Không expose raw SQL exception cho REST client.

Đây là boundary translation pattern và là nền cho Spring's exception translation sau này.

---

# 29. Try-with-resources và suppressed exceptions

```java
try (Resource a = openA();
     Resource b = openB()) {
    use(a, b);
}
```

Resources close reverse order.

Nếu body throw `PrimaryException` và `close()` throw `CloseException`, Java giữ primary và attach close exception:

```java
e.getSuppressed()
```

Điều này tránh losing root cause.

Khi debug I/O, kiểm tra suppressed exceptions nếu close failure có ý nghĩa.

---

# 30. `java.time`: Instant, Offset, Zone

`Instant` là point trên UTC timeline.

`OffsetDateTime` có date/time + fixed UTC offset.

`ZonedDateTime` có zone region + rules, ví dụ `Asia/Seoul`.

Store event timestamp:

```java
Instant createdAt;
```

Display:

```java
createdAt.atZone(
    ZoneId.of("Asia/Seoul"));
```

Không lưu “2026-11-01 01:30” rồi assume worldwide meaning. Local time có thể ambiguous trong DST zones.

---

# 31. DST và calendar bugs

Một ngày calendar không luôn 24 hours ở zones có daylight-saving transitions.

```java
zoned.plusDays(1)
```

và:

```java
zoned.plusHours(24)
```

có thể khác local wall time.

Business rule phải nói “ngày lịch” hay “elapsed 24 hours”.

Korea hiện không DST nhưng global application vẫn gặp.

---

# 32. Inject `Clock` cho deterministic time

Bad testability:

```java
Instant now =
    Instant.now();
```

Better:

```java
final class TokenService {
    private final Clock clock;

    TokenService(Clock clock) {
        this.clock = clock;
    }

    boolean expired(Token token) {
        return token.expiresAt()
            .isBefore(
                Instant.now(clock));
    }
}
```

Test:

```java
Clock fixed =
    Clock.fixed(
        Instant.parse(
            "2026-01-01T00:00:00Z"),
        ZoneOffset.UTC);
```

Dependency injection cho nondeterminism là plain Java design pattern, sau này Spring chỉ giúp wiring.

---

# 33. BigDecimal scale và rounding policy

Division:

```java
new BigDecimal("10")
    .divide(
        new BigDecimal("3"));
```

có thể throw `ArithmeticException` nếu decimal expansion non-terminating.

Specify scale/rounding:

```java
amount.divide(
    divisor,
    2,
    RoundingMode.HALF_UP);
```

Nhưng “2, HALF_UP” không phải universal money rule. Currency/tax/product có policy riêng.

Put rounding policy trong domain service/value object.

---

# 34. `Path`/`Files` và large file strategy

`Files.readAllBytes` hoặc `readString` load toàn file vào memory.

10 KB okay. 10 GB không.

Large data nên stream:

```java
try (Stream<String> lines =
         Files.lines(
             path,
             StandardCharsets.UTF_8)) {

    lines.forEach(...);
}
```

`Files.list`/`Files.walk` cũng trả streams gắn resource; dùng try-with-resources.

Resource-returning Stream là một contract quan trọng vì nó khác in-memory stream.

---

# 35. ByteBuffer mental model

`ByteBuffer` có:

```text
capacity
position
limit
```

Bạn write data:

```java
buffer.put(bytes);
```

Sau đó `flip()` chuyển buffer từ write mode sang read mode bằng cách set limit=current position rồi position=0.

`clear()` chuẩn bị ghi lại toàn buffer, không zero memory.

`compact()` giữ unread bytes rồi chuẩn bị ghi thêm.

Nếu không hiểu position/limit, NIO code rất dễ bug.

---

# 36. Channels

`FileChannel` đọc/ghi qua buffers và hỗ trợ random access, transfer, mapping.

NIO không đồng nghĩa “luôn non-blocking”. FileChannel operations có thể block. Non-blocking selector model chủ yếu liên quan socket channels.

Senior sẽ đi sâu direct buffers/mmap/zero-copy-like operations.

---

# 37. Regex

Compile:

```java
Pattern EMAIL =
    Pattern.compile(...);
```

Match entire:

```java
matcher.matches()
```

Find substring:

```java
matcher.find()
```

Groups:

```java
matcher.group(1)
```

Java string escaping means regex backslash phải double escape.

Regex `\d+` trong source:

```java
"\\d+"
```

Precompile repeated pattern.

Cẩn thận catastrophic backtracking với untrusted input; regex có thể thành performance/security issue.

---

# 38. Concurrency bắt đầu từ shared mutable state

Race condition không phải chỉ “hai threads cùng chạy”. Nó xảy ra khi correctness phụ thuộc timing interleavings không được synchronize.

```java
count++;
```

conceptually là:

```text
read count
add 1
write count
```

Hai threads có thể cùng read 10 và cùng write 11, mất một increment.

Thread-safe design bắt đầu bằng việc giảm shared mutable state. Immutable data và thread confinement thường đơn giản hơn locks.

---

# 39. Visibility

Thread A:

```java
running = false;
```

Thread B:

```java
while (running) {
}
```

Nếu không synchronization/volatile, Java Memory Model không guarantee B thấy update timely như bạn tưởng.

CPU caches/compiler/JIT reorder/optimize trong boundaries được phép.

Concurrency correctness phải reason bằng happens-before, không bằng “RAM chắc update rồi”.

---

# 40. Happens-before ở level Intermediate

Happens-before là relationship đảm bảo visibility/ordering giữa actions.

Các mechanisms tạo happens-before gồm synchronized lock/unlock, volatile write/read, thread start/join và concurrency utilities theo contract.

Nếu action A happens-before B, effects của A được B thấy theo JMM guarantee phù hợp.

Đây là nền để Senior học safe publication/final fields/VarHandle.

---

# 41. `synchronized`

Method:

```java
synchronized void increment() {
    count++;
}
```

Block:

```java
synchronized (lock) {
    ...
}
```

`synchronized` cung cấp mutual exclusion và memory visibility.

Lock object phải stable/private nếu có thể.

Bad:

```java
synchronized (publicList) {
}
```

external code cũng có thể lock same object, gây hidden coupling/deadlock.

Critical section nên chỉ chứa state operations cần bảo vệ. Đừng giữ lock trong remote HTTP call.

---

# 42. `volatile`

```java
private volatile boolean running = true;
```

Volatile thích hợp cho simple visibility/state flag.

Nhưng:

```java
volatile int count;
count++;
```

vẫn không atomic.

Compound invariant:

```text
balance >= 0
debit + ledger update
```

không được bảo vệ bởi volatile đơn lẻ.

Volatile không phải “lightweight synchronized replacement”; nó giải contract khác.

---

# 43. Atomic Classes

```java
AtomicInteger counter =
    new AtomicInteger();

counter.incrementAndGet();
```

CAS-based methods:

```java
compareAndSet(expected, update)
updateAndGet(fn)
getAndIncrement()
```

Atomic classes phù hợp single-variable atomic transitions.

Nếu invariant liên quan hai fields:

```text
available + reserved = total
```

hai `AtomicInteger` không tự tạo atomic transaction giữa chúng.

Need lock/immutable state/CAS state object design.

---

# 44. `LongAdder`

High-contention counter:

```java
LongAdder adder =
    new LongAdder();

adder.increment();
```

nó phân tán contention qua cells rồi sum.

Tốt cho metrics-style counters hơn exact synchronization point.

`sum()` không necessarily linearizable snapshot như `AtomicLong.get()` trong mọi concurrent timing.

Chọn semantics trước throughput.

---

# 45. `ReentrantLock`

```java
lock.lock();

try {
    ...
} finally {
    lock.unlock();
}
```

Bắt buộc unlock trong finally.

`ReentrantLock` hữu ích khi cần `tryLock`, interruptible lock acquisition, multiple Conditions hoặc fairness policy.

Nếu chỉ cần simple mutual exclusion, `synchronized` thường dễ đọc và ít bug hơn.

---

# 46. `Condition`

`Condition` tương tự wait/notify abstraction gắn với Lock.

```java
Condition notEmpty =
    lock.newCondition();
```

Wait phải trong loop:

```java
while (queue.isEmpty()) {
    notEmpty.await();
}
```

vì spurious wakeup và condition có thể đổi trước khi thread reacquire lock.

High-level `BlockingQueue` thường tốt hơn tự implement producer/consumer condition logic.

---

# 47. ExecutorService

Không tạo thread tùy tiện:

```java
new Thread(task).start();
```

cho mỗi job trong server.

Executor tách task submission khỏi thread management.

```java
ExecutorService executor =
    Executors.newFixedThreadPool(8);

executor.submit(task);
```

Sau đó lifecycle:

```java
executor.shutdown();
```

Application/component sở hữu executor phải close/shutdown nó.

---

# 48. ThreadPoolExecutor thực sự có ba phần chính

Thread pool behavior không chỉ là “max threads”.

Nó có:

```text
workers
queue
rejection policy
```

Khi tasks đến nhanh hơn xử lý, queue behavior quyết định latency/memory.

Unbounded queue có thể làm memory grow thay vì reject.

Bounded queue + rejection policy làm overload explicit.

Capacity là correctness property trong production.

---

# 49. Rejection Policies

`AbortPolicy` throw rejection exception.

`CallerRunsPolicy` cho submitting thread chạy task, tạo natural slowdown/backpressure trong một số architecture.

Discard policies bỏ task, chỉ đúng khi data loss acceptable.

Không chọn policy mà không biết business consequence của rejected task.

---

# 50. Future

```java
Future<Result> future =
    executor.submit(
        () -> compute());

Result result =
    future.get();
```

`get()` block indefinitely nếu không timeout.

Better:

```java
future.get(
    2,
    TimeUnit.SECONDS);
```

Waiting policy phải explicit ở external/slow operations.

Cancellation:

```java
future.cancel(true);
```

yêu cầu cooperative interruption; không guarantee task chết ngay.

---

# 51. Interruption

Thread interruption là cooperative cancellation signal.

Bad:

```java
catch (InterruptedException e) {
    // ignore
}
```

Bạn mất signal.

Nếu không handle:

```java
catch (InterruptedException e) {
    Thread.currentThread()
          .interrupt();

    throw new RuntimeException(e);
}
```

hoặc propagate checked exception tùy API.

Preserve interruption là thói quen cực quan trọng trong executors/shutdown.

---

# 52. ConcurrentHashMap

`ConcurrentHashMap` cho concurrent access với atomic compound methods.

Bad check-then-act:

```java
if (!map.containsKey(key)) {
    map.put(key, create());
}
```

Race.

Better:

```java
map.computeIfAbsent(
    key,
    this::create);
```

Mapping function phải tránh long blocking/reentrant updates phức tạp.

Concurrent collection iterator thường weakly consistent, không giống fail-fast normal collection iterator.

---

# 53. CopyOnWriteArrayList

Mỗi write tạo copy array mới.

Excellent khi:

```text
reads rất nhiều
writes cực ít
lists nhỏ/moderate
```

Ví dụ listener registry.

Tệ nếu write-heavy/large list.

Concurrency collection name không tự nghĩa “better list”.

---

# 54. BlockingQueue và Producer/Consumer

```java
BlockingQueue<Job> queue =
    new ArrayBlockingQueue<>(1000);
```

Producer:

```java
queue.put(job);
```

Consumer:

```java
Job job = queue.take();
```

Bounded queue tạo backpressure: nếu full, producer phải wait/fail theo chosen operation.

Đây là production pattern rất quan trọng. Queue vô hạn chỉ chuyển overload thành memory/latency.

---

# 55. CompletableFuture

Create:

```java
CompletableFuture<User> future =
    CompletableFuture.supplyAsync(
        this::loadUser,
        executor);
```

Transform:

```java
future.thenApply(
    User::name);
```

Dependent async result:

```java
future.thenCompose(
    user ->
      loadOrdersAsync(user.id()));
```

`thenApply` giống `map`; `thenCompose` giống `flatMap`.

---

# 56. Combine independent futures

```java
CompletableFuture<User> user =
    loadUser();

CompletableFuture<List<Order>> orders =
    loadOrders();

CompletableFuture<Response> response =
    user.thenCombine(
        orders,
        Response::new);
```

Fan-out independent I/O có thể giảm latency, nhưng cũng tăng downstream load.

Nếu một request fan-out 100 calls và system nhận 1000 requests, bạn tạo 100.000 downstream calls. Parallelism phải bounded.

---

# 57. CompletableFuture execution context

Async methods không chỉ khác suffix.

`thenApply` có thể chạy trên completion thread/caller context.

`thenApplyAsync` sử dụng executor/default async facility.

Nếu không truyền executor, common pool có thể được dùng.

Server code nên biết executor nào sở hữu workload.

Hidden common pool là hidden capacity.

---

# 58. CompletableFuture errors

```java
future.exceptionally(
    error -> fallback);
```

`handle` nhận cả value/error.

`whenComplete` quan sát side effect nhưng không nhất thiết recover.

Error topology trong async graph dễ phức tạp. Preserve cause và define timeout/cancellation.

`join()` wrap checked completion failures thành unchecked `CompletionException`; `get()` dùng checked `ExecutionException`.

---

# 59. Virtual Threads Java 21

Virtual thread là lightweight Java thread managed bởi JVM, phù hợp thread-per-task blocking style.

```java
try (var executor =
         Executors
            .newVirtualThreadPerTaskExecutor()) {

    Future<Result> result =
        executor.submit(
            this::blockingCall);
}
```

Không pool virtual threads để “tiết kiệm threads”; chúng đã lightweight. Giới hạn concurrency tại scarce resource như DB/remote service bằng pool/semaphore.

Virtual threads tăng scalability của blocking concurrency, không làm CPU calculation nhanh hơn.

---

# 60. JDBC mental model

JDBC layers:

```text
Driver
→ Connection
→ PreparedStatement
→ ResultSet
```

Query:

```java
try (Connection connection =
         dataSource.getConnection();

     PreparedStatement statement =
         connection.prepareStatement(
             """
             select id, name
             from users
             where id = ?
             """)) {

    statement.setLong(1, id);

    try (ResultSet rs =
             statement.executeQuery()) {

        if (rs.next()) {
            ...
        }
    }
}
```

Try-with-resources làm ownership rõ.

---

# 61. PreparedStatement

PreparedStatement giúp parameter binding đúng type và tránh SQL injection nếu bạn không concatenate untrusted values vào SQL syntax.

Bad:

```java
"select * from users where name='"
    + userInput + "'"
```

Better:

```sql
where name = ?
```

và `setString`.

PreparedStatement còn có plan/reuse benefits tùy DB/driver.

---

# 62. JDBC execute methods

`executeQuery()` cho result set query.

`executeUpdate()` thường cho INSERT/UPDATE/DELETE và trả affected count.

`execute()` generic hơn khi result type chưa chắc.

Generated keys có thể request qua appropriate statement options.

Không dùng API chỉ vì “nó chạy”; chọn method thể hiện expected SQL semantics.

---

# 63. JDBC Transactions

Default connection thường auto-commit true.

Manual transaction:

```java
connection.setAutoCommit(false);

try {
    debit(connection);
    credit(connection);
    connection.commit();
} catch (Exception e) {
    connection.rollback();
    throw e;
}
```

Transaction boundary phải phản ánh business atomic operation, không chỉ một repository method.

Connection phải được dùng nhất quán trong unit of work; mở connection mới trong mỗi helper có thể phá atomicity.

---

# 64. JDBC Isolation và Savepoints

Connection cho phép set transaction isolation theo constants.

Actual behavior phụ thuộc DB.

Savepoint:

```java
Savepoint sp =
    connection.setSavepoint();
```

Rollback partial:

```java
connection.rollback(sp);
```

Useful cho nested-like local recovery nhưng complexity tăng. Đừng dùng savepoints nếu full transaction rollback là business behavior đúng.

---

# 65. JDBC Batch

```java
statement.addBatch();
...
int[] counts =
    statement.executeBatch();
```

Batch giảm round trips cho many similar DML.

Nhưng huge batch có memory/transaction/log cost. Chunk size cần measure.

DB driver có settings ảnh hưởng real batching.

---

# 66. Annotations nâng cao

Custom annotation:

```java
@Retention(
    RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Audited {
    String value() default "";
}
```

Retention:

```text
SOURCE
CLASS
RUNTIME
```

Target giới hạn nơi dùng.

Runtime annotation chỉ tồn tại để reflection/framework đọc; tự nó không execute code.

Compile-time annotation processor là topic sâu hơn.

---

# 67. Reflection

Get class:

```java
Class<?> type =
    User.class;
```

Inspect:

```java
type.getDeclaredMethods();
type.getDeclaredFields();
type.getDeclaredConstructors();
```

Invoke:

```java
Method method =
    type.getDeclaredMethod(
        "name");

Object result =
    method.invoke(user);
```

Reflection giảm compile-time type safety, có access/module considerations và runtime failure modes.

Nó hợp ở infrastructure/framework boundary như serialization/DI/testing tools, không nên là default business dispatch.

---

# 68. Dynamic Proxy

JDK dynamic proxy tạo object implement interfaces và intercept method calls.

```java
PaymentGateway proxy =
    (PaymentGateway)
    Proxy.newProxyInstance(
        loader,
        new Class<?>[] {
            PaymentGateway.class
        },
        (p, method, args) -> {
            before();
            Object result =
                method.invoke(
                    target,
                    args);
            after();
            return result;
        });
```

Đây là Proxy Pattern và là bridge rất quan trọng trước Spring AOP.

Caller tưởng đang gọi implementation contract, nhưng proxy chạy logic trước/sau.

---

# 69. Classpath và Class Loading

Classpath là nơi runtime/compiler tìm classes/resources.

Common errors:

`ClassNotFoundException` thường khi code cố load class theo name nhưng loader không tìm thấy.

`NoClassDefFoundError` có thể xảy ra khi class cần thiết không thể load/initialize dù compile trước đó có class.

`NoSuchMethodError` thường do binary dependency mismatch: compile với library version có method, runtime load version không có.

Khi gặp linkage error, inspect actual dependency tree/artifact, không chỉ source.

---

# 70. ClassLoader identity

Ở mức Intermediate, nhớ rằng class identity không chỉ name; defining classloader cũng matter.

Hai `com.example.Plugin` loaded bởi different classloaders có thể được xem như distinct runtime types.

Plugin containers/app servers dùng custom loaders và có classloader leaks/casting surprises. Senior sẽ đi sâu.

---

# 71. JPMS Module System

Java 9 module descriptor:

```java
module com.example.app {
    requires java.sql;

    exports com.example.api;

    opens com.example.model
        to some.framework;
}
```

`exports` cho compile/runtime access public types.

`opens` cho deep reflection access.

`uses`/`provides` hỗ trợ Service Provider Interface.

Không phải mọi Spring/backend app cần JPMS, nhưng module encapsulation giải thích một số reflection access errors modern Java.

---

# 72. ServiceLoader và SPI

Interface:

```java
public interface Parser {
    Document parse(String input);
}
```

Providers có thể được discover:

```java
ServiceLoader<Parser> loader =
    ServiceLoader.load(Parser.class);
```

Đây là native Java plugin mechanism.

Plugin discovery là Strategy + provider registry.

Spring DI có hệ thống riêng phong phú hơn, nhưng SPI giúp hiểu framework extension architecture.

---

# 73. Java 11 APIs cần biết

String:

```java
text.isBlank();
text.lines();
text.strip();
text.repeat(3);
```

Files:

```java
Files.readString(path);
Files.writeString(path, text);
```

Optional:

```java
optional.isEmpty();
```

Lambda parameter `var` Java 11:

```java
(var x, var y) -> x + y
```

chủ yếu hữu ích khi cần annotations trên lambda params.

---

# 74. Standard HTTP Client Java 11

```java
HttpClient client =
    HttpClient.newBuilder()
        .connectTimeout(
            Duration.ofSeconds(2))
        .build();
```

Request:

```java
HttpRequest request =
    HttpRequest.newBuilder()
        .uri(
            URI.create(
                "https://example.com"))
        .timeout(
            Duration.ofSeconds(3))
        .GET()
        .build();
```

Sync:

```java
HttpResponse<String> response =
    client.send(
        request,
        HttpResponse.BodyHandlers
                    .ofString());
```

Async:

```java
client.sendAsync(
    request,
    BodyHandlers.ofString());
```

Connect timeout và request timeout là distinct layers.

Reuse HttpClient where appropriate; connection pooling/resource setup benefit.

---

# 75. Timeout Budget

Nếu incoming operation budget 2 seconds, downstream calls không nên mỗi cái timeout 5 seconds.

Budget thinking:

```text
total deadline
→ remaining time
→ child operation timeout
```

Intermediate chỉ cần hình thành nguyên tắc này. Senior sẽ đi vào deadline propagation/retry.

---

# 76. Modern Java 14–17

Switch expressions Java 14 giúp expression-style branching.

Text blocks Java 15 giúp multiline SQL/JSON.

Records Java 16 cho data/value carriers.

Pattern matching for `instanceof` Java 16 giảm cast boilerplate.

Sealed classes Java 17 giới hạn subtype set.

Đây không chỉ syntax sugar; chúng làm data modeling rõ và compiler có thêm thông tin.

---

# 77. Pattern Matching for Switch Java 21

Sealed hierarchy:

```java
sealed interface Result
    permits Success, Failure {
}
```

Switch:

```java
String message =
    switch (result) {
        case Success s ->
            "ok " + s.id();

        case Failure f ->
            "error " + f.reason();
    };
```

Compiler check exhaustiveness.

Guard with `when` trong pattern switch:

```java
case Success s
    when s.id() > 100 -> ...
```

Dùng khi decision là data-oriented closed variants. Nếu mỗi subtype có behavior tự nhiên, polymorphic method có thể tốt hơn.

---

# 78. Record Patterns Java 21

```java
record Point(int x, int y) {
}
```

Deconstruct:

```java
if (obj instanceof
        Point(int x, int y)) {
    ...
}
```

Nested records cho data-oriented matching.

Pattern matching giúp parse/branch data structures, nhưng đừng biến domain thành massive switch nếu object-oriented behavior rõ hơn.

---

# 79. Sequenced Collections Java 21

Interfaces như `SequencedCollection`, `SequencedSet`, `SequencedMap` thống nhất access first/last/reversed semantics cho ordered collections.

Ví dụ concept:

```java
collection.getFirst();
collection.getLast();
collection.reversed();
```

Trước Java 21, mỗi collection có APIs khác nhau hoặc cần index/iterator hacks.

---

# 80. UUID, Base64, Random và SecureRandom

UUID:

```java
UUID id =
    UUID.randomUUID();
```

thích hợp identifiers không cần centralized sequence trong nhiều contexts, nhưng storage/indexing trade-offs tồn tại.

Base64 là encoding, không encryption.

```java
String encoded =
    Base64.getEncoder()
          .encodeToString(bytes);
```

`Random`/`ThreadLocalRandom` cho non-security randomness.

`SecureRandom` cho cryptographic randomness.

Không dùng `Random` tạo reset token/session secret.

---

# 81. Locale, Currency, ResourceBundle

Locale-sensitive formatting phải explicit.

```java
NumberFormat format =
    NumberFormat.getCurrencyInstance(
        Locale.KOREA);
```

Currency:

```java
Currency.getInstance("KRW");
```

ResourceBundle cho localized resources.

Không assume server default locale/timezone; container/server có thể khác local laptop.

---

# 82. Charset

Bytes không tự là text. Cần encoding.

```java
String text =
    Files.readString(
        path,
        StandardCharsets.UTF_8);
```

Nếu write UTF-8 nhưng read EUC-KR, mojibake xuất hiện.

Make charset part of contract.

Platform default charset thay đổi qua Java generations/environments; explicit UTF-8 safest khi protocol/file contract định nghĩa UTF-8.

---

# 83. Native Java Serialization awareness

`Serializable` cho built-in object serialization.

Nhưng native Java serialization có tight class coupling và historical security risks.

Bạn cần biết để maintain legacy systems, không nên chọn làm default new API/message format.

Use JSON/CBOR/Protobuf/etc theo ecosystem requirements thay vì `ObjectOutputStream` chỉ vì built-in.

---

# 84. Security API awareness

Hash:

```java
MessageDigest.getInstance(
    "SHA-256");
```

MAC:

```java
Mac.getInstance(
    "HmacSHA256");
```

Encryption:

```java
Cipher.getInstance(...);
```

Nhưng cryptography là protocol design, không chỉ gọi API.

Không tự invent encryption scheme.

Password hashing không dùng raw SHA-256; cần adaptive password hash libraries/algorithms theo security policy.

Senior/Master sẽ đi sâu.

---

# 85. API Design: Strong Types

Bad:

```java
transfer(
    long from,
    long to,
    BigDecimal amount,
    String currency);
```

Better domain concepts:

```java
transfer(
    AccountId from,
    AccountId to,
    Money amount);
```

Strong types làm illegal argument mix khó compile.

Primitive obsession là khi domain concepts bị biểu diễn bằng raw primitives/strings quá lâu.

---

# 86. Command/Query Separation mindset

Method:

```java
User activate(User user)
```

vừa mutate state vừa return data có thể okay, nhưng API khó hiểu nếu query methods có hidden side effects.

Tư duy CQS nói command thay state và query đọc state nên thường dễ phân biệt.

Không phải luật cấm methods vừa return result sau mutation; mục tiêu là side effects explicit.

---

# 87. Composition over Inheritance

Decorator-style composition:

```java
interface MessageSender {
    void send(Message message);
}
```

```java
final class LoggingSender
        implements MessageSender {

    private final MessageSender delegate;

    public void send(Message message) {
        log(message);
        delegate.send(message);
    }
}
```

Bạn thêm behavior bằng wrapping thay vì subclass deep hierarchy.

Java I/O và many framework proxies use this structural idea.

---

# 88. Factory và Static Factory

Static factory names:

```java
UserId.of(value)
Money.zero(currency)
Duration.ofSeconds(2)
List.of(...)
```

có thể communicate semantics tốt hơn overloaded constructors.

Factory có thể choose subtype/cache/reuse.

Không tạo separate factory class nếu static factory đủ rõ.

---

# 89. Builder

Builder phù hợp config object có many optional fields.

Nhưng Java records + named static factory có thể đủ cho small data structures.

Pattern là response to constructor readability/optional combinations, không phải requirement cho every domain entity.

---

# 90. Template Method vs Strategy

Template Method dùng inheritance để cố định algorithm skeleton.

Strategy dùng composition để inject behavior.

Nếu subclass hierarchy stable, template method okay.

Nếu cần combine behavior/runtime replace/testing, Strategy thường flexible.

Biết trade-off quan trọng hơn “composition always”.

---

# 91. Adapter

Adapter chuyển external interface sang internal contract.

```java
final class VendorPaymentAdapter
        implements PaymentGateway {

    private final VendorSdk sdk;
}
```

Vendor exception/types dừng ở adapter.

Đây là anti-corruption boundary và sẽ rất quan trọng trong Spring HTTP/JPA integrations.

---

# 92. Command Pattern với Functional Interfaces

Command object/lambda biểu diễn operation như data/behavior value.

```java
Runnable task =
    () -> processOrder(id);
```

Executors nhận commands.

Complex command có thể là class chứa parameters + execute behavior.

Patterns trong modern Java thường được biểu diễn nhẹ hơn nhờ lambdas/records.

---

# 93. JVM Memory: Stack, Heap, Metaspace, Native

Mỗi thread có stack chứa frames/local execution state.

Heap chứa most objects/arrays managed by GC.

Metaspace chứa class metadata ngoài heap.

Direct buffers/native libraries/thread stacks dùng native memory ngoài Java heap.

Do đó:

```text
-Xmx = 2G
```

không nghĩa process RSS tối đa 2G.

Server/container memory planning phải chừa native headroom.

---

# 94. Garbage Collection awareness

GC tìm objects còn reachable từ roots như thread stacks/static/JNI references và reclaim unreachable objects.

Java memory leak vẫn có thể xảy ra khi object không còn business-useful nhưng vẫn reachable, ví dụ static list/cache/queue/listener.

Đầu tiên fix retention/ownership; đừng đổi collector để chữa logical leak.

Common collectors hiện đại gồm G1, ZGC, Parallel, Serial; selection/tuning sang Senior.

---

# 95. JIT và Warm-up

JVM ban đầu interpret/compile progressively. Hot methods được JIT optimize dựa runtime profile.

Benchmark:

```java
long start =
    System.nanoTime();
doWork();
long elapsed =
    System.nanoTime() - start;
```

một lần không đủ kết luận vì warm-up, dead-code elimination, GC, CPU scaling và profiling.

Use JMH mindset/tool cho microbenchmark quan trọng.

Senior sẽ đi sâu inlining/deoptimization/escape analysis.

---

# 96. `javac --release`

Nếu develop bằng JDK 25 nhưng target Java 17:

```bash
javac --release 17 ...
```

giúp compiler enforce Java 17 language/API platform baseline.

Chỉ `-source 17 -target 17` historically không luôn ngăn code gọi APIs mới có trong current JDK.

Build tools thường expose equivalent release configuration.

---

# 97. JVM Options cơ bản

Heap:

```bash
-Xms512m
-Xmx2g
```

Thread stack:

```bash
-Xss1m
```

System property:

```bash
-Dapp.env=prod
```

GC logging modern:

```bash
-Xlog:gc*
```

Heap dump on OOM:

```bash
-XX:+HeapDumpOnOutOfMemoryError
```

Không copy production flags từ random blog. JVM defaults thay đổi theo version/hardware/container.

---

# 98. `jcmd`, `jstack`, `jmap`, `jstat`

Find Java process:

```bash
jcmd
```

Thread dump:

```bash
jcmd <pid> Thread.print
```

JFR start/dump và GC/class info cũng qua `jcmd`.

`jstack` cho thread stack legacy/common usage.

`jmap` có heap-related operations.

`jstat` xem JVM stats sampling.

Modern production habit: ưu tiên diagnostic tools dựa evidence thay vì restart trước khi collect data.

---

# 99. Java Flight Recorder awareness

JFR là built-in low-overhead event recording/profiling facility.

Có thể capture:

```text
CPU samples
allocation
GC
locks
threads
I/O
exceptions
```

tùy settings/version.

Senior sẽ dùng JFR như primary production diagnostic tool.

Intermediate chỉ cần biết Java có observability sâu hơn logs.

---

# 100. Logging awareness

Java Core có `java.util.logging`, nhưng application ecosystems thường dùng abstraction/facade như SLF4J sau này.

Core principle: log context, not secrets.

```text
orderId
requestId
operation
duration
error category
```

Không log password/token.

Không concatenate huge strings nếu log disabled.

Logging không thay metrics/traces/profiles.

---

# 101. Code Smells ở Intermediate

Primitive obsession xuất hiện khi `String` đại diện Email, Currency, Status, UserId khắp nơi.

Boolean parameter explosion:

```java
process(true, false, true)
```

khó đọc.

Feature envy khi class lấy hàng loạt getters của object khác rồi làm logic lẽ ra thuộc object kia.

Shotgun surgery khi một business change cần sửa 20 classes vì concept bị phân tán.

Hidden side effect khi method tên `findUser()` lại update DB/cache/network.

Recognize smell là để investigate design pressure, không phải auto-refactor mọi case.

---

# 102. Error Handling Pattern trong Backend

Không retry programming bug.

Không retry validation error.

Transient network/database errors có thể retry nếu operation idempotent và bounded.

Preserve cause.

Translate at boundaries.

Log once at ownership boundary.

Những rules này chuẩn bị cho resilience/Spring exception architecture.

---

# 103. Dependency Direction trước Spring

Application service:

```java
final class PlaceOrderService {
    private final OrderRepository repository;
    private final PaymentGateway payment;
}
```

Interfaces/ports thuộc core/application.

JDBC/HTTP implementations depend inward:

```text
JdbcOrderRepository
→ implements OrderRepository

HttpPaymentGateway
→ implements PaymentGateway
```

Spring sau này chỉ wire implementations.

Nếu bạn hiểu Dependency Inversion bằng plain Java, Spring DI sẽ không còn là magic.

---

# 104. Package Visibility như Architecture Tool

Không public mọi implementation.

```java
final class JdbcUserMapper {
}
```

package-private nếu chỉ repository package cần.

Public surface nhỏ giảm accidental coupling.

Package by feature giúp internal classes gần nhau và visibility hữu dụng hơn.

---

# 105. Testing Mindset trước Framework

Pure service với injected dependencies test dễ.

Time dùng `Clock`.

IDs dùng `Supplier<UUID>` hoặc generator interface.

External gateway fake/mock.

Không cần Mockito/Spring để hiểu testability. Framework tools chỉ automate seams mà design đã tạo.

---

# 106. Legacy APIs cần nhận biết

`Date`, `Calendar`, `SimpleDateFormat` vẫn có trong legacy; prefer `java.time`.

`Vector`, `Hashtable`, `Stack` thường legacy; modern alternatives `ArrayList`, `HashMap`/concurrent maps, `ArrayDeque`.

`StringBuffer` synchronized; `StringBuilder` thường default single-threaded local building.

Native serialization cần caution.

Bạn phải đọc legacy code nhưng không copy legacy APIs vào code mới chỉ vì quen.

---

# 107. Version Compatibility

Có ba axes:

```text
source syntax
class-file target
runtime/platform APIs
```

Bạn có thể viết syntax Java 17 nhưng gọi Java 25 API nếu build config không enforce release correctly.

Runtime old sẽ fail.

Dependencies cũng có minimum Java version.

Upgrade JDK phải test libraries/build tools/runtime, không chỉ compiler.

---

# 108. Intermediate Project: Order Processing Service Core

Viết plain Java application xử lý orders với `Order`, `Money`, `OrderStatus`, `CustomerId`, repository interface và JDBC implementation.

Dùng Flyway-like SQL scripts manually if needed, nhưng mục tiêu là JDBC transaction đúng.

Thêm external HTTP Client Java 11 để gọi fake payment API với timeout.

Thêm executor/CompletableFuture để load two independent datasets concurrently, sau đó giới hạn concurrency.

Dùng JFR/jcmd để quan sát thread/heap.

Viết reflection-based simple annotation scanner nhỏ để hiểu metadata/proxy trước Spring.

Project này là bridge trực tiếp sang Senior và Spring.

---

# 109. Intermediate → Senior Gate

Bạn sẵn sàng sang Senior khi có thể giải thích invariance, PECS, type erasure và unsafe raw types; chọn collection dựa semantics; hiểu equals/hashCode/comparator contracts; phân biệt immutable snapshot và unmodifiable view; giải thích Stream laziness, flatMap, collectors và parallel-stream risks.

Bạn phải reason concurrency bằng race/visibility/atomicity/happens-before; biết khi nào synchronized, volatile, atomic, locks, executors, blocking queues, CompletableFuture và virtual threads phù hợp.

Bạn phải viết JDBC resource lifecycle/transaction đúng, hiểu reflection/dynamic proxy/classpath/classloader errors và đọc modern Java 11–21 features.

Bạn phải biết JVM memory không chỉ heap, GC không chữa logical leak, JIT cần warm-up và JFR/jcmd tồn tại để debug bằng evidence.

Ở level này, “code chạy” chưa đủ. Bạn cần biết **vì sao nó đúng dưới nhiều inputs, threads, environments và failures**.

---

# 110. Điều để sang Senior

Senior sẽ đào sâu bytecode, stack frames, JIT inlining/deoptimization, escape analysis, class loading identity/initialization, Java Memory Model formal hơn, safe publication, deadlocks/contention, CAS/ABA, advanced concurrent collections, executor saturation, CompletableFuture failure topology, virtual-thread production trade-offs, GC roots/leaks, G1/ZGC, native memory, JFR incident workflow, performance engineering, NIO/direct buffers, remote-call resilience, MethodHandle, JDBC pool/isolation, security, API compatibility, architecture và distributed-system patterns.

---

# References for version-sensitive topics

Oracle Java SE Support Roadmap:
https://www.oracle.com/java/technologies/java-se-support-roadmap.html

Oracle Java API:
https://docs.oracle.com/en/java/javase/

OpenJDK JEP index:
https://openjdk.org/jeps/0
