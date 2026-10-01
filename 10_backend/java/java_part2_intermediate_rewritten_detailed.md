# Java cốt lõi (core / 핵심) — Part 2: Intermediate — Rewritten Detailed

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Java cốt lõi (core / 핵심) — Part 2: Intermediate — Rewritten Detailed**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ “biết viết Java” sang “hiểu đặc tả hợp đồng (contract / 계약), tính đồng thời (concurrency / 동시성), thời gian chạy (runtime / 런타임) và ranh giới (boundary / 경계)”** làm rõ cặp khái niệm dễ lẫn và giới hạn của cách giải thích; sau đó sang **Vị trí của Part 2 trong mạch học (learning flow / 학습 흐름)** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Từ “biết viết Java” sang “hiểu đặc tả hợp đồng (contract / 계약), tính đồng thời (concurrency / 동시성), thời gian chạy (runtime / 런타임) và ranh giới (boundary / 경계)”

> Part 2 giả định bạn đã hoàn thành Part 1 và đã có thể tự viết một chương trình Java nhỏ bằng OOP, collections, Stream, Optional, `java.time`, tệp (file / 파일) I/O và exceptions. Mục tiêu ở đây là nâng cách suy nghĩ từ “API nào làm được việc này?” thành “đặc tả hợp đồng (contract / 계약) của API này là gì, đối tượng (object / 객체) này thuộc về ai, luồng thực thi (thread / 스레드) nào được phép thay đổi trạng thái (state / 상태), tài nguyên (resource / 자원) tồn tại bao lâu, và lỗi nào có thể xảy ra ở thời gian chạy (runtime / 런타임) dù trình biên dịch (compiler / 컴파일러) vẫn cho qua?”.
>
> Các ghi chú kiểu cấp cao (senior / 시니어), idiom và mẫu (pattern / 패턴) không được tách thành mục riêng sau mỗi chương. Khi một tư duy nâng cao cần thiết, nó được giải thích ngay trong nội dung cùng ví dụ để bạn học như một phần tự nhiên của Java.

> **Chuyển mạch:** Trong **Java cốt lõi (core / 핵심) — Part 2: Intermediate — Rewritten Detailed**, **Từ “biết viết Java” sang “hiểu đặc tả hợp đồng (contract / 계약), tính đồng thời (concurrency / 동시성), thời gian chạy (runtime / 런타임) và ranh giới (boundary / 경계)”** đã nêu tiêu chí phân biệt, còn **Vị trí của Part 2 trong mạch học (learning flow / 학습 흐름)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Thread: đối tượng (object / 객체) Java và thực thi (execution / 실행) ngữ cảnh (context / 맥락) khác nhau thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vị trí của Part 2 trong mạch học (learning flow / 학습 흐름)

Part 2 nối trực tiếp từ [Java Part 1 — Beginner](./java_part1_beginner_rewritten_detailed.md). Ở đây bạn không học lại cú pháp (syntax / 문법); bạn bắt đầu giải thích được đặc tả hợp đồng (contract / 계약) của collections/generics, vòng đời (lifecycle / 생명주기) của luồng thực thi (thread / 스레드)/tài nguyên (resource / 자원), bộ nhớ (memory / 메모리) visibility, JDBC giao dịch (transaction / 트랜잭션), reflection, nạp lớp (class loading / 클래스 로딩) và JVM. Sau khi hoàn thành Part 2, tiếp tục [Java Part 3 — Senior](./java_part3_senior_rewritten_detailed.md).

---

# 1. Intermediate Java nghĩa là bắt đầu học theo đặc tả hợp đồng (contract / 계약)

Ở Beginner, bạn học `List.add`, `Map.get`, `Stream.map`, `Optional.orElseThrow`. Ở Intermediate, điều quan trọng hơn là đặc tả hợp đồng (contract / 계약) phía sau chúng. `HashMap` có yêu cầu gì với `equals()` và `hashCode()`? `Comparator` phải thỏa tính chất nào để `TreeSet` không hành xử kỳ lạ? `Stream` có lazy hay eager? `volatile` đảm bảo visibility nhưng không đảm bảo atomicity nghĩa là gì? `ExecutorService.shutdown()` khác `shutdownNow()` ra sao? Một JDBC `Connection` thuộc sở hữu của ai và khi nào được close?

Java có rất nhiều API; bạn không thể master bằng cách thuộc toàn bộ methods. Bạn phải học mô hình tư duy (mental model / 사고 모델) và đặc tả hợp đồng (contract / 계약) để có thể dự đoán hành vi (behavior / 동작) khi gặp API mới.

---

# 2. Generics không chỉ để bỏ cast

Beginner nhìn:

```java
List<String>
```

và hiểu danh sách (list / 목록) chỉ chứa String.

Intermediate cần hiểu generic hệ kiểu (type system / 타입 시스템) giúp trình biên dịch (compiler / 컴파일러) kiểm tra **mối quan hệ kiểu (type / 타입)**, nhưng generic types trong Java phần lớn là bất biến (invariant / 불변식).

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

và `integers` bỗng chứa `Double`, phá kiểu (type / 타입) an toàn (safety / 안전).

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

Nếu phương thức (method / 메서드) chỉ **đọc** values như `T`, bạn có thể dùng upper-bounded wildcard.

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

Phương thức (method / 메서드) này nhận:

```text
List<Integer>
List<Long>
List<Double>
```

vì mỗi element có thể đọc như `Number`.

Nhưng bạn không thể an toàn add `Integer` vào `List<? extends Number>` vì danh sách (list / 목록) thật có thể là `List<Double>`.

Mô hình tư duy (mental model / 사고 모델): `extends` làm producer flexible. Bạn biết lấy ra được `T`, nhưng không biết chính xác (exact / 정확한) subtype để add.

---

# 4. Wildcard `? super T`

Nếu phương thức (method / 메서드) cần **ghi** T vào collection:

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

Bạn có thể add Integer vì tất cả những danh sách (list / 목록) đó đều chứa được Integer.

Khi đọc ra, static kiểu (type / 타입) an toàn nhất thường chỉ là `Object`.

Từ hai ý trên sinh ra mnemonic **PECS**: Producer Extends, bên tiêu thụ (consumer / 소비자) Super. Đừng học thuộc câu đó nếu chưa hiểu variance; nó chỉ là cách nhớ đặc tả hợp đồng (contract / 계약) đã giải thích.

---

# 5. kiểu (type / 타입) parameter bounds

Generic phương thức (method / 메서드):

```java
static <T extends Comparable<T>>
T max(T a, T b) {
    return a.compareTo(b) >= 0
            ? a
            : b;
}
```

`T extends Comparable<T>` nói kiểu (type / 타입) T phải implement đặc tả hợp đồng (contract / 계약) so sánh với chính T.

Multiple bounds:

```java
<T extends Closeable
        & Comparable<T>>
```

Nếu có lớp (class / 클래스) bound, nó phải đứng trước giao diện (interface / 인터페이스) bounds.

Generic các ràng buộc (constraints / 제약조건들) giúp encode yêu cầu (requirement / 요구사항) ở compile thời gian (time / 시간), thay vì thời gian chạy (runtime / 런타임) `instanceof` checks.

---

# 6. kiểu (type / 타입) Erasure

Java generics được triển khai chủ yếu qua kiểu (type / 타입) erasure. Sau compile, thời gian chạy (runtime / 런타임) thường không giữ full generic kiểu (type / 타입) arguments theo cách bạn tưởng.

Ví dụ:

```java
List<String>
List<Integer>
```

đều là `List` ở nhiều thời gian chạy (runtime / 런타임) contexts.

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

Kiểu (type / 타입) erasure giải thích vì sao không tạo được:

```java
new T[10]
```

và vì sao reflection generic siêu dữ liệu (metadata / 메타데이터) có giới hạn/phức tạp.

---

# 7. Raw Types và vì sao nguy hiểm

Legacy:

```java
List values = new ArrayList();
```

Raw kiểu (type / 타입) bypass generic checks.

```java
values.add("hello");
values.add(123);
```

Sau đó:

```java
List<String> strings = values;
```

có unchecked warning và thời gian chạy (runtime / 런타임) `ClassCastException` có thể xảy ra xa nơi bug được tạo.

Đừng suppress unchecked warnings cả gói (package / 패키지). Nếu phải interop với legacy/raw API, hãy cô lập cast ở một ranh giới (boundary / 경계) nhỏ, validate dữ liệu rồi expose typed API cho phần còn lại.

---

# 8. vùng nhớ động (heap / 힙) Pollution và `@SafeVarargs`

Generic varargs có thể tạo array biểu diễn (representation / 표현) không reified đầy đủ.

```java
static <T> void process(
        List<T>... lists) {
}
```

Trình biên dịch (compiler / 컴파일러) có thể cảnh báo vùng nhớ động (heap / 힙) pollution.

`@SafeVarargs` chỉ nên dùng khi hiện thực (implementation / 구현) thực sự không làm unsafe operations với varargs array. Annotation này là lời hứa của programmer với trình biên dịch (compiler / 컴파일러), không phải công cụ tắt warning tùy tiện.

---

# 9. Collections phải chọn theo ngữ nghĩa (semantics / 의미론) trước Big-O

Big-O cần biết nhưng không đủ. `ArrayList` và `LinkedList` có theoretical differences, nhưng CPU bộ nhớ đệm (cache / 캐시) locality, allocation, traversal mẫu (pattern / 패턴) và tải công việc (workload / 워크로드) thật làm `ArrayList` thường tốt hơn trong ứng dụng (application / 애플리케이션) mã (code / 코드).

Nếu cần indexed/read-heavy ordered chuỗi (sequence / 시퀀스), bắt đầu bằng `ArrayList`.

Nếu cần uniqueness, dùng `Set`.

Nếu cần lookup bằng key, dùng `Map`.

Nếu cần priority thứ tự (order / 순서), dùng `PriorityQueue`.

Nếu cần FIFO/LIFO hàng đợi (queue / 큐), `ArrayDeque` thường là lựa chọn tốt.

Collection kiểu (type / 타입) nên nói intent của lĩnh vực (domain / 도메인). Nếu nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) là “không duplicate SKU”, `Set<Sku>` encode intent tốt hơn `List<Sku>` + manual duplicate tìm kiếm (search / 검색).

---

# 10. `ArrayList.remove()` overload trap

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

```java
List<Integer> values =
    new ArrayList<>(
        List.of(10, 20, 30));

values.remove(1);
```

xóa element chỉ mục (index / 인덱스) 1, tức `20`.

Muốn xóa giá trị (value / 값) 1:

```java
values.remove(
    Integer.valueOf(1));
```

Đây là ví dụ overloading + autoboxing có thể gây ambiguity về ý nghĩa. Khi API có overloaded thành phần nguyên thủy (primitive / 기본 요소)/đối tượng (object / 객체) forms, đọc signature chứ đừng đoán.

---

# 11. `HashSet` và equality đặc tả hợp đồng (contract / 계약)

`HashSet` dùng hash-based cấu trúc (structure / 구조). Khi add đối tượng (object / 객체), băm (hash / 해시) mã (code / 코드) giúp chọn bucket; equality xác nhận đối tượng (object / 객체) đã tồn tại chưa.

Nếu hai objects bằng nhau theo `equals`, chúng bắt buộc phải có cùng `hashCode`.

Sai đặc tả hợp đồng (contract / 계약) có thể làm:

```text
set contains duplicate logical values
contains() trả false
remove() không tìm thấy object
```

Đây không phải “HashSet bug”; cấu trúc (structure / 구조) dựa vào đặc tả hợp đồng (contract / 계약) của key.

---

# 12. Mutable keys là lỗi nguy hiểm

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

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

Băm (hash / 해시) mã (code / 코드) thay đổi nhưng entry vẫn nằm ở bucket cũ.

```java
map.get(key)
```

có thể thất bại (fail / 실패).

Map keys nên thường immutable theo fields dùng trong equality/băm (hash / 해시). Đây là một lý do giá trị (value / 값) objects và records rất hữu ích.

---

# 13. `LinkedHashMap`, `TreeMap`, `EnumMap`

`LinkedHashMap` preserve insertion thứ tự (order / 순서) và có access-order chế độ (mode / 모드), hữu ích cho cache-like structures nhỏ.

`TreeMap` giữ keys sorted dựa comparator, hỗ trợ phạm vi (range / 범위)/điều hướng (navigation / 내비게이션) operations.

`EnumMap` chuyên cho enum keys, thường compact và fast hơn generic `HashMap<Enum,...>`.

Nếu key lĩnh vực (domain / 도메인) là enum:

```java
EnumMap<PaymentType, Handler>
```

thể hiện intent rất rõ.

---

# 14. Map như chỉ mục (index / 인덱스)

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

“chỉ mục (index / 인덱스) once, truy vấn (query / 쿼리) many” là một mẫu lập trình (programming pattern / 프로그래밍 패턴) thường xuyên xuất hiện từ in-memory collections tới cơ sở dữ liệu (database / 데이터베이스) indexes.

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

Ánh xạ (mapping / 매핑) hàm (function / 함수) nên đơn giản, nhanh và không gây side tác động (effect / 효과) phức tạp, đặc biệt với concurrent maps. Nó có thể được gọi trong synchronization/atomic mechanics tùy hiện thực (implementation / 구현).

Không dùng `computeIfAbsent` để gọi remote API chậm mà không hiểu tính đồng thời (concurrency / 동시성) consequences.

---

# 16. `equals()` và `hashCode()` là đặc tả hợp đồng (contract / 계약) hệ thống

Giá trị (value / 값) đối tượng (object / 객체):

```java
public record UserId(long value) {
    public UserId {
        if (value <= 0) {
            throw new IllegalArgumentException();
        }
    }
}
```

Bản ghi (record / 레코드) tự cung cấp value-based equality.

Nếu custom lớp (class / 클래스):

```java
final class Money {
    private final BigDecimal amount;
    private final Currency currency;
}
```

bạn phải quyết định equality ngữ nghĩa (semantics / 의미론). `BigDecimal.equals` xem quy mô (scale / 규모), nên `10.0` và `10.00` không equal. Nếu lĩnh vực (domain / 도메인) muốn numeric equality bất kể quy mô (scale / 규모), normalize amount lúc construction hoặc custom equality carefully.

Equality không chỉ để kiểm thử (test / 테스트). Nó ảnh hưởng maps, sets, caches, ORM entities và deduplication.

---

# 17. `Comparable` vs `Comparator`

`Comparable<T>` định nghĩa natural thứ tự (order / 순서) của kiểu (type / 타입).

```java
class Version
        implements Comparable<Version> {
}
```

`Comparator<T>` định nghĩa bên ngoài (external / 외부) thứ tự (ordering / 순서) chiến lược (strategy / 전략).

```java
Comparator<User> byName =
    Comparator.comparing(User::name);
```

Một kiểu (type / 타입) thường chỉ có một natural thứ tự (order / 순서) hợp lý nhưng có thể có nhiều comparators.

Comparator phải consistent enough với thứ tự (ordering / 순서) đặc tả hợp đồng (contract / 계약): antisymmetry/transitivity và hành vi (behavior / 동작) ổn định. Comparator inconsistent có thể làm `TreeSet` tưởng hai objects “trùng” nếu compare trả 0 dù `equals` false.

Đây là lý do sorting đặc tả hợp đồng (contract / 계약) không chỉ là “return negative/zero/positive”.

---

# 18. Immutable, Unmodifiable và Defensive bản sao (copy / 복사) khác nhau

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

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

`List.copyOf(original)` tạo unmodifiable snapshot về cấu trúc (structure / 구조) tại thời điểm bản sao (copy / 복사).

Nếu lớp (class / 클래스) cần own collection trạng thái (state / 상태):

```java
this.roles =
    List.copyOf(roles);
```

rõ hơn giữ bên ngoài (external / 외부) mutable danh sách (list / 목록).

Nhưng nếu elements mutable, shallow bản sao (copy / 복사) không deep-copy elements. quyền sở hữu (ownership / 소유권) phải reason toàn đối tượng (object / 객체) đồ thị (graph / 그래프).

---

# 19. Stream là lazy chuỗi xử lý (pipeline / 파이프라인)

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

```java
Stream<User> stream =
    users.stream()
         .filter(user -> {
             System.out.println(
                 "filter " + user.id());
             return user.active();
         });
```

Chưa có terminal thao tác (operation / 연산), filter có thể chưa chạy.

Khi:

```java
long count = stream.count();
```

Chuỗi xử lý (pipeline / 파이프라인) mới evaluate.

Laziness cho phép tối ưu hóa (optimization / 최적화) và short-circuit.

```java
users.stream()
     .filter(...)
     .findFirst();
```

có thể dừng khi tìm thấy first match.

Không dựa vào stream chuỗi xử lý (pipeline / 파이프라인) để thực hiện side tác động (effect / 효과) thứ tự (order / 순서) phức tạp nếu ngữ nghĩa (semantics / 의미론) quan trọng.

---

# 20. `flatMap`

Nếu:

```java
List<Order> orders
```

mỗi thứ tự (order / 순서) có:

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

`flatMap` rất quan trọng khi composition trả bộ chứa (container / 컨테이너)/ngữ cảnh (context / 맥락) cùng loại.

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

Collectors giúp biến stream thành aggregated dữ liệu (data / 데이터) structures.

---

# 22. `toMap` duplicate key trap

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
users.stream()
     .collect(
         Collectors.toMap(
             User::email,
             Function.identity()
         ));
```

Nếu duplicate email, collector throw `IllegalStateException`.

Bạn phải quyết định nghiệp vụ (business / 비즈니스) chính sách (policy / 정책):

```java
Collectors.toMap(
    User::email,
    Function.identity(),
    (first, second) -> first
)
```

Nhưng silent “first wins” chỉ đúng nếu lĩnh vực (domain / 도메인) cho phép. Duplicate key thường có thể là data-quality bug nên fail-fast tốt hơn.

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

`reduce` kết hợp elements thành một giá trị (value / 값).

Accumulator phải associative nếu muốn parallel ngữ nghĩa (semantics / 의미론) đúng.

Dùng specialized collectors/methods khi dễ đọc hơn. Không biến mọi aggregation thành abstract reduce nếu `sum()`/`count()`/collector thể hiện intent rõ hơn.

---

# 24. thành phần nguyên thủy (primitive / 기본 요소) Streams

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

```java
int totalAge =
    users.stream()
         .mapToInt(User::age)
         .sum();
```

`IntStream`, `LongStream`, `DoubleStream` giảm boxing và có operations như `sum`, `average`.

Hot data-processing mã (code / 코드) có thể benefit, nhưng clarity trước. Đừng dùng thành phần nguyên thủy (primitive / 기본 요소) streams chỉ vì sợ boxing trong small nghiệp vụ (business / 비즈니스) đường dẫn (path / 경로) chưa profile.

---

# 25. Parallel Stream

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

```java
users.parallelStream()
```

không tự động nhanh hơn.

Parallel công việc (work / 작업) có overhead split/merge/scheduling và thường dùng dùng chung (common / 공통) `ForkJoinPool`. Nếu thao tác (operation / 연산) blocking HTTP/DB, bạn có thể làm dùng chung (common / 공통) pool starvation hoặc uncontrolled fan-out.

Chỉ parallelize khi tải công việc (workload / 워크로드) CPU-bound/splittable, dataset đủ lớn và benchmark chứng minh.

Trong máy chủ (server / 서버) ứng dụng (application / 애플리케이션), tường minh (explicit / 명시적) executor/tính đồng thời (concurrency / 동시성) limit thường dễ kiểm soát hơn parallel stream.

---

# 26. Optional nâng cao

`Optional` nên thường là return kiểu (type / 타입) để nói “kết quả (result / 결과) có thể không tồn tại”.

Bad style:

```java
void process(
    Optional<User> user)
```

thường làm caller phải wrap giá trị (value / 값) vô ích.

Trường dữ liệu (field / 필드) Optional cũng có khung phần mềm (framework / 프레임워크)/serialization concerns.

`orElseGet` lazy như Part 1.

Java 9 thêm `ifPresentOrElse`, `or`, `stream`; Java 11 thêm `isEmpty`.

Optional chuỗi xử lý (pipeline / 파이프라인):

```java
String email =
    repository.findById(id)
              .filter(User::active)
              .map(User::email)
              .orElseThrow(...);
```

Nếu chuỗi (chain / 사슬) trở nên khó gỡ lỗi (debug / 디버그), tường minh (explicit / 명시적) branching có thể rõ hơn.

---

# 27. Exception thiết kế (design / 설계)

Exception should carry ngữ nghĩa (semantics / 의미론) and cause.

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

Catch nơi bạn có thể add giá trị (value / 값). Nếu tầng (layer / 계층) chỉ catch để log `"error"` rồi rethrow, top tầng (layer / 계층) sẽ log lại và tạo duplicate ngăn xếp (stack / 스택) traces.

---

# 28. Exception Translation at Boundaries

Cơ sở dữ liệu (database / 데이터베이스) tầng (layer / 계층) có vendor exception. ứng dụng (application / 애플리케이션) tầng (layer / 계층) cần data-access ngữ nghĩa (semantics / 의미론). HTTP tầng (layer / 계층) cần status/lỗi (error / 오류) đặc tả hợp đồng (contract / 계약).

Luồng (flow / 흐름):

```text
SQLException
→ UserRepositoryException
→ application decision
→ HTTP 503/500 or domain response
```

Không expose raw SQL exception cho REST máy khách (client / 클라이언트).

Đây là ranh giới (boundary / 경계) translation mẫu (pattern / 패턴) và là nền cho Spring's exception translation sau này.

---

# 29. Try-with-resources và suppressed exceptions

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
try (Resource a = openA();
     Resource b = openB()) {
    use(a, b);
}
```

Resources close reverse thứ tự (order / 순서).

Nếu body throw `PrimaryException` và `close()` throw `CloseException`, Java giữ primary và attach close exception:

```java
e.getSuppressed()
```

Điều này tránh losing nguyên nhân gốc (root cause / 근본 원인).

Khi gỡ lỗi (debug / 디버그) I/O, kiểm tra suppressed exceptions nếu close thất bại (failure / 실패) có ý nghĩa.

---

# 30. `java.time`: Instant, Offset, Zone

`Instant` là điểm (point / 지점) trên UTC timeline.

`OffsetDateTime` có date/thời gian (time / 시간) + fixed UTC offset.

`ZonedDateTime` có zone region + rules, ví dụ `Asia/Seoul`.

Store sự kiện (event / 이벤트) timestamp:

```java
Instant createdAt;
```

Display:

```java
createdAt.atZone(
    ZoneId.of("Asia/Seoul"));
```

Không lưu “2026-11-01 01:30” rồi assume worldwide meaning. cục bộ (local / 로컬) thời gian (time / 시간) có thể ambiguous trong DST zones.

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

có thể khác cục bộ (local / 로컬) wall thời gian (time / 시간).

Nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) phải nói “ngày lịch” hay “elapsed 24 hours”.

Korea hiện không DST nhưng toàn cục (global / 전역) ứng dụng (application / 애플리케이션) vẫn gặp.

---

# 32. Inject `Clock` cho deterministic thời gian (time / 시간)

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

Kiểm thử (test / 테스트):

```java
Clock fixed =
    Clock.fixed(
        Instant.parse(
            "2026-01-01T00:00:00Z"),
        ZoneOffset.UTC);
```

Phụ thuộc (dependency / 의존성) injection cho nondeterminism là plain Java mẫu thiết kế (design pattern / 디자인 패턴), sau này Spring chỉ giúp wiring.

---

# 33. BigDecimal quy mô (scale / 규모) và rounding chính sách (policy / 정책)

Division:

```java
new BigDecimal("10")
    .divide(
        new BigDecimal("3"));
```

có thể throw `ArithmeticException` nếu decimal expansion non-terminating.

Specify quy mô (scale / 규모)/rounding:

```java
amount.divide(
    divisor,
    2,
    RoundingMode.HALF_UP);
```

Nhưng “2, HALF_UP” không phải universal money quy tắc (rule / 규칙). Currency/tax/sản phẩm (product / 제품) có chính sách (policy / 정책) riêng.

Put rounding chính sách (policy / 정책) trong lĩnh vực (domain / 도메인) dịch vụ (service / 서비스)/giá trị (value / 값) đối tượng (object / 객체).

---

# 34. `Path`/`Files` và large tệp (file / 파일) chiến lược (strategy / 전략)

`Files.readAllBytes` hoặc `readString` tải (load / 로드) toàn tệp (file / 파일) vào bộ nhớ (memory / 메모리).

10 KB okay. 10 GB không.

Large dữ liệu (data / 데이터) nên stream:

```java
try (Stream<String> lines =
         Files.lines(
             path,
             StandardCharsets.UTF_8)) {

    lines.forEach(...);
}
```

`Files.list`/`Files.walk` cũng trả streams gắn tài nguyên (resource / 자원); dùng try-with-resources.

Resource-returning Stream là một đặc tả hợp đồng (contract / 계약) quan trọng vì nó khác in-memory stream.

---

# 35. ByteBuffer mô hình tư duy (mental model / 사고 모델)

`ByteBuffer` có:

```text
capacity
position
limit
```

Bạn ghi (write / 쓰기) dữ liệu (data / 데이터):

```java
buffer.put(bytes);
```

Sau đó `flip()` chuyển buffer từ ghi (write / 쓰기) chế độ (mode / 모드) sang read chế độ (mode / 모드) bằng cách set limit=hiện tại (current / 현재) position rồi position=0.

`clear()` chuẩn bị ghi lại toàn buffer, không zero bộ nhớ (memory / 메모리).

`compact()` giữ unread bytes rồi chuẩn bị ghi thêm.

Nếu không hiểu position/limit, NIO mã (code / 코드) rất dễ bug.

---

# 36. Channels

`FileChannel` đọc/ghi qua buffers và hỗ trợ random truy cập (access / 접근), transfer, ánh xạ (mapping / 매핑).

NIO không đồng nghĩa “luôn non-blocking”. FileChannel operations có thể khối (block / 블록). Non-blocking selector mô hình (model / 모델) chủ yếu liên quan socket channels.

Cấp cao (senior / 시니어) sẽ đi sâu direct buffers/mmap/zero-copy-like operations.

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

Regex `\d+` trong nguồn (source / 소스):

```java
"\\d+"
```

Precompile repeated mẫu (pattern / 패턴).

Cẩn thận catastrophic backtracking với untrusted đầu vào (input / 입력); regex có thể thành hiệu năng (performance / 성능)/bảo mật (security / 보안) issue.

---

# 38. tính đồng thời (concurrency / 동시성) bắt đầu từ dùng chung (shared / 공유) mutable trạng thái (state / 상태)

Race điều kiện (condition / 조건) không phải chỉ “hai threads cùng chạy”. Nó xảy ra khi tính đúng đắn (correctness / 정확성) phụ thuộc timing interleavings không được synchronize.

```java
count++;
```

conceptually là:

```text
read count
add 1
write count
```

Hai threads có thể cùng read 10 và cùng ghi (write / 쓰기) 11, mất một increment.

Thread-safe thiết kế (design / 설계) bắt đầu bằng việc giảm dùng chung (shared / 공유) mutable trạng thái (state / 상태). Immutable dữ liệu (data / 데이터) và luồng thực thi (thread / 스레드) confinement thường đơn giản hơn locks.

---

> **Chuyển mạch:** Part 2 bắt đầu từ nền tảng object và chuyển sang concurrency/runtime. Câu hỏi về **Thread: đối tượng Java và execution context khác nhau thế nào?** là cầu nối để đọc các phần sau về memory visibility, coordination và failure.

## `Thread`: đối tượng (object / 객체) Java và thực thi (execution / 실행) ngữ cảnh (context / 맥락) khác nhau thế nào?

Trước khi học `synchronized`, executor hay virtual luồng thực thi (thread / 스레드), cần hiểu `Thread` ở mức trực tiếp. Một `Thread` đối tượng (object / 객체) biểu diễn một luồng thực thi có vòng đời (lifecycle / 생명주기). Tạo đối tượng (object / 객체) chưa làm mã (code / 코드) chạy song song:

```java
Thread thread =
    new Thread(() -> doWork());
```

Chỉ khi gọi `thread.start()` JVM mới tạo/schedule thực thi (execution / 실행) mới và luồng thực thi (thread / 스레드) đó sau đó thực thi `run()`. Nếu gọi trực tiếp `thread.run()`, đó chỉ là một phương thức (method / 메서드) lời gọi (call / 호출) bình thường trên **luồng thực thi (thread / 스레드) hiện tại**; không có tính đồng thời (concurrency / 동시성) mới.

Bạn có thể chờ luồng thực thi (thread / 스레드) khác hoàn thành bằng `join()`. `join()` không chỉ “đợi cho xong”; việc luồng thực thi (thread / 스레드) kết thúc rồi luồng thực thi (thread / 스레드) khác phép nối (join / 조인) thành công còn tạo happens-before relationship, nên các effects trước khi luồng thực thi (thread / 스레드) kết thúc được luồng thực thi (thread / 스레드) phép nối (join / 조인) quan sát theo Java bộ nhớ (memory / 메모리) mô hình (model / 모델).

`Thread.sleep(...)` chỉ tạm dừng luồng thực thi (thread / 스레드) hiện tại; nó không nhả monitor khóa (lock / 잠금) đang giữ và không phải thành phần nguyên thủy (primitive / 기본 요소) để chờ một điều kiện (condition / 조건). Nếu kiểm thử (test / 테스트) hoặc môi trường vận hành (production / 운영 환경) mã (code / 코드) dùng `sleep(100)` để “đợi tác vụ (task / 작업) chắc chạy xong”, thiết kế (design / 설계) đang phụ thuộc timing. Hãy dùng `join`, latch, `Future` hoặc điều kiện (condition / 조건) phù hợp.

Nền tảng (platform / 플랫폼) luồng thực thi (thread / 스레드) có các trạng thái như `NEW`, `RUNNABLE`, `BLOCKED`, `WAITING`, `TIMED_WAITING`, `TERMINATED`. Trong môi trường vận hành (production / 운영 환경) luồng thực thi (thread / 스레드) dump, trạng thái (state / 상태) chỉ là đầu mối: một worker WAITING trên hàng đợi (queue / 큐) có thể hoàn toàn bình thường, còn hàng trăm threads BLOCKED trên cùng monitor mới là tín hiệu contention cần điều tra.

Daemon luồng thực thi (thread / 스레드) không giữ JVM sống khi tất cả non-daemon threads đã kết thúc. Background công việc (work / 작업) quan trọng không nên dựa vào giả định “daemon luồng thực thi (thread / 스레드) sẽ còn kịp flush”. Durability phải đến từ tường minh (explicit / 명시적) persistence và vòng đời (lifecycle / 생명주기).

Trong ứng dụng (application / 애플리케이션) môi trường vận hành (production / 운영 환경), bạn hiếm khi tự tạo một nền tảng (platform / 플랫폼) `Thread` cho từng tác vụ (task / 작업); `ExecutorService` quản lý vòng đời (lifecycle / 생명주기) và sức chứa (capacity / 용량) tốt hơn. Java 21 Virtual Threads lại làm thread-per-task style khả thi với chi phí (cost / 비용) mô hình (model / 모델) khác. Nhưng hiểu `Thread` vẫn bắt buộc để đọc dấu vết ngăn xếp (stack trace / 스택 트레이스), luồng thực thi (thread / 스레드) dump, interruption và khung phần mềm (framework / 프레임워크) thực thi (execution / 실행).

---

# 39. Visibility

Luồng thực thi (thread / 스레드) A:

```java
running = false;
```

Luồng thực thi (thread / 스레드) B:

```java
while (running) {
}
```

Nếu không synchronization/volatile, Java bộ nhớ (memory / 메모리) mô hình (model / 모델) không guarantee B thấy cập nhật (update / 업데이트) timely như bạn tưởng.

CPU caches/trình biên dịch (compiler / 컴파일러)/JIT reorder/optimize trong boundaries được phép.

Tính đồng thời (concurrency / 동시성) tính đúng đắn (correctness / 정확성) phải reason bằng happens-before, không bằng “RAM chắc cập nhật (update / 업데이트) rồi”.

---

# 40. Happens-before ở mức (level / 수준) Intermediate

Happens-before là relationship đảm bảo visibility/thứ tự (ordering / 순서) giữa actions.

Các mechanisms tạo happens-before gồm synchronized khóa (lock / 잠금)/unlock, volatile ghi (write / 쓰기)/read, luồng thực thi (thread / 스레드) start/phép nối (join / 조인) và tính đồng thời (concurrency / 동시성) utilities theo đặc tả hợp đồng (contract / 계약).

Nếu hành động (action / 동작) A happens-before B, effects của A được B thấy theo JMM guarantee phù hợp.

Đây là nền để cấp cao (senior / 시니어) học safe publication/final fields/VarHandle.

---

# 41. `synchronized`

Phương thức (method / 메서드):

```java
synchronized void increment() {
    count++;
}
```

Khối (block / 블록):

```java
synchronized (lock) {
    ...
}
```

`synchronized` cung cấp mutual exclusion và bộ nhớ (memory / 메모리) visibility.

Khóa (lock / 잠금) đối tượng (object / 객체) phải stable/private nếu có thể.

Bad:

```java
synchronized (publicList) {
}
```

Bên ngoài (external / 외부) mã (code / 코드) cũng có thể khóa (lock / 잠금) same đối tượng (object / 객체), gây hidden coupling/deadlock.

Trọng yếu (critical / 중요) section nên chỉ chứa trạng thái (state / 상태) operations cần bảo vệ. Đừng giữ khóa (lock / 잠금) trong remote HTTP lời gọi (call / 호출).

---

# 42. `volatile`

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
private volatile boolean running = true;
```

Volatile thích hợp cho simple visibility/trạng thái (state / 상태) flag.

Nhưng:

```java
volatile int count;
count++;
```

vẫn không atomic.

Compound bất biến (invariant / 불변식):

```text
balance >= 0
debit + ledger update
```

không được bảo vệ bởi volatile đơn lẻ.

Volatile không phải “lightweight synchronized replacement”; nó giải đặc tả hợp đồng (contract / 계약) khác.

---

# 43. Atomic Classes

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

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

Nếu bất biến (invariant / 불변식) liên quan hai fields:

```text
available + reserved = total
```

hai `AtomicInteger` không tự tạo atomic giao dịch (transaction / 트랜잭션) giữa chúng.

Need khóa (lock / 잠금)/immutable trạng thái (state / 상태)/CAS trạng thái (state / 상태) đối tượng (object / 객체) thiết kế (design / 설계).

---

# 44. `LongAdder`

High-contention counter:

```java
LongAdder adder =
    new LongAdder();

adder.increment();
```

nó phân tán contention qua cells rồi sum.

Tốt cho metrics-style counters hơn chính xác (exact / 정확한) synchronization điểm (point / 지점).

`sum()` không necessarily linearizable snapshot như `AtomicLong.get()` trong mọi concurrent timing.

Chọn ngữ nghĩa (semantics / 의미론) trước thông lượng (throughput / 처리량).

---

# 45. `ReentrantLock`

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
lock.lock();

try {
    ...
} finally {
    lock.unlock();
}
```

Bắt buộc unlock trong finally.

`ReentrantLock` hữu ích khi cần `tryLock`, interruptible khóa (lock / 잠금) acquisition, multiple Conditions hoặc fairness chính sách (policy / 정책).

Nếu chỉ cần simple mutual exclusion, `synchronized` thường dễ đọc và ít bug hơn.

---

# 46. `Condition`

`Condition` tương tự wait/notify lớp trừu tượng (abstraction / 추상화) gắn với khóa (lock / 잠금).

```java
Condition notEmpty =
    lock.newCondition();
```

Wait phải trong vòng lặp (loop / 루프):

```java
while (queue.isEmpty()) {
    notEmpty.await();
}
```

vì spurious wakeup và điều kiện (condition / 조건) có thể đổi trước khi luồng thực thi (thread / 스레드) reacquire khóa (lock / 잠금).

High-level `BlockingQueue` thường tốt hơn tự implement producer/bên tiêu thụ (consumer / 소비자) điều kiện (condition / 조건) lô-gic (logic / 논리).

---

# 47. ExecutorService

Không tạo luồng thực thi (thread / 스레드) tùy tiện:

```java
new Thread(task).start();
```

cho mỗi job trong máy chủ (server / 서버).

Executor tách tác vụ (task / 작업) submission khỏi luồng thực thi (thread / 스레드) management.

```java
ExecutorService executor =
    Executors.newFixedThreadPool(8);

executor.submit(task);
```

Sau đó vòng đời (lifecycle / 생명주기):

```java
executor.shutdown();
```

Ứng dụng (application / 애플리케이션)/thành phần (component / 컴포넌트) sở hữu executor phải close/shutdown nó.

---

# 48. ThreadPoolExecutor thực sự có ba phần chính

Luồng thực thi (thread / 스레드) pool hành vi (behavior / 동작) không chỉ là “max threads”.

Nó có:

```text
workers
queue
rejection policy
```

Khi tasks đến nhanh hơn xử lý, hàng đợi (queue / 큐) hành vi (behavior / 동작) quyết định độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리).

Unbounded hàng đợi (queue / 큐) có thể làm bộ nhớ (memory / 메모리) grow thay vì reject.

Bounded hàng đợi (queue / 큐) + rejection chính sách (policy / 정책) làm overload tường minh (explicit / 명시적).

Sức chứa (capacity / 용량) là tính đúng đắn (correctness / 정확성) thuộc tính (property / 속성) trong môi trường vận hành (production / 운영 환경).

---

# 49. Rejection Policies

`AbortPolicy` throw rejection exception.

`CallerRunsPolicy` cho submitting luồng thực thi (thread / 스레드) chạy tác vụ (task / 작업), tạo natural slowdown/backpressure trong một số kiến trúc (architecture / 아키텍처).

Discard policies bỏ tác vụ (task / 작업), chỉ đúng khi dữ liệu (data / 데이터) mất mát (loss / 손실) acceptable.

Không chọn chính sách (policy / 정책) mà không biết nghiệp vụ (business / 비즈니스) consequence của rejected tác vụ (task / 작업).

---

# 50. Future

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
Future<Result> future =
    executor.submit(
        () -> compute());

Result result =
    future.get();
```

`get()` khối (block / 블록) indefinitely nếu không hết thời gian chờ (timeout / 타임아웃).

Better:

```java
future.get(
    2,
    TimeUnit.SECONDS);
```

Waiting chính sách (policy / 정책) phải tường minh (explicit / 명시적) ở bên ngoài (external / 외부)/slow operations.

Cancellation:

```java
future.cancel(true);
```

yêu cầu cooperative interruption; không guarantee tác vụ (task / 작업) chết ngay.

---

# 51. Interruption

Luồng thực thi (thread / 스레드) interruption là cooperative cancellation tín hiệu (signal / 신호).

Bad:

```java
catch (InterruptedException e) {
    // ignore
}
```

Bạn mất tín hiệu (signal / 신호).

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

`ConcurrentHashMap` cho concurrent truy cập (access / 접근) với atomic compound methods.

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

Ánh xạ (mapping / 매핑) hàm (function / 함수) phải tránh long blocking/reentrant updates phức tạp.

Concurrent collection iterator thường weakly consistent, không giống fail-fast normal collection iterator.

---

# 53. CopyOnWriteArrayList

Mỗi ghi (write / 쓰기) tạo bản sao (copy / 복사) array mới.

Excellent khi:

```text
reads rất nhiều
writes cực ít
lists nhỏ/moderate
```

Ví dụ listener registry.

Tệ nếu write-heavy/large danh sách (list / 목록).

Tính đồng thời (concurrency / 동시성) collection name không tự nghĩa “better danh sách (list / 목록)”.

---

# 54. BlockingQueue và Producer/bên tiêu thụ (consumer / 소비자)

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
BlockingQueue<Job> queue =
    new ArrayBlockingQueue<>(1000);
```

Producer:

```java
queue.put(job);
```

Bên tiêu thụ (consumer / 소비자):

```java
Job job = queue.take();
```

Bounded hàng đợi (queue / 큐) tạo backpressure: nếu full, producer phải wait/thất bại (fail / 실패) theo chosen thao tác (operation / 연산).

Đây là môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴) rất quan trọng. hàng đợi (queue / 큐) vô hạn chỉ chuyển overload thành bộ nhớ (memory / 메모리)/độ trễ (latency / 지연 시간).

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

Dependent async kết quả (result / 결과):

```java
future.thenCompose(
    user ->
      loadOrdersAsync(user.id()));
```

`thenApply` giống `map`; `thenCompose` giống `flatMap`.

---

# 56. Combine independent futures

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

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

Fan-out independent I/O có thể giảm độ trễ (latency / 지연 시간), nhưng cũng tăng downstream tải (load / 로드).

Nếu một yêu cầu (request / 요청) fan-out 100 calls và hệ thống (system / 시스템) nhận 1000 requests, bạn tạo 100.000 downstream calls. Parallelism phải bounded.

---

# 57. CompletableFuture thực thi (execution / 실행) ngữ cảnh (context / 맥락)

Async methods không chỉ khác suffix.

`thenApply` có thể chạy trên completion luồng thực thi (thread / 스레드)/caller ngữ cảnh (context / 맥락).

`thenApplyAsync` sử dụng executor/default async facility.

Nếu không truyền executor, dùng chung (common / 공통) pool có thể được dùng.

Máy chủ (server / 서버) mã (code / 코드) nên biết executor nào sở hữu tải công việc (workload / 워크로드).

Hidden dùng chung (common / 공통) pool là hidden sức chứa (capacity / 용량).

---

# 58. CompletableFuture errors

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
future.exceptionally(
    error -> fallback);
```

`handle` nhận cả giá trị (value / 값)/lỗi (error / 오류).

`whenComplete` quan sát side tác động (effect / 효과) nhưng không nhất thiết recover.

Lỗi (error / 오류) topology trong async đồ thị (graph / 그래프) dễ phức tạp. Preserve cause và define hết thời gian chờ (timeout / 타임아웃)/cancellation.

`join()` wrap checked completion failures thành unchecked `CompletionException`; `get()` dùng checked `ExecutionException`.

---

# 59. Virtual Threads Java 21

Virtual luồng thực thi (thread / 스레드) là lightweight Java luồng thực thi (thread / 스레드) managed bởi JVM, phù hợp thread-per-task blocking style.

```java
try (var executor =
         Executors
            .newVirtualThreadPerTaskExecutor()) {

    Future<Result> result =
        executor.submit(
            this::blockingCall);
}
```

Không pool virtual threads để “tiết kiệm threads”; chúng đã lightweight. Giới hạn tính đồng thời (concurrency / 동시성) tại scarce tài nguyên (resource / 자원) như DB/remote dịch vụ (service / 서비스) bằng pool/semaphore.

Virtual threads tăng scalability của blocking tính đồng thời (concurrency / 동시성), không làm CPU calculation nhanh hơn.

---

# 60. JDBC mô hình tư duy (mental model / 사고 모델)

JDBC layers:

```text
Driver
→ Connection
→ PreparedStatement
→ ResultSet
```

Truy vấn (query / 쿼리):

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

Try-with-resources làm quyền sở hữu (ownership / 소유권) rõ.

---

# 61. PreparedStatement

PreparedStatement giúp parameter binding đúng kiểu (type / 타입) và tránh SQL injection nếu bạn không concatenate untrusted values vào SQL cú pháp (syntax / 문법).

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

`executeQuery()` cho tập kết quả (result set / 결과 집합) truy vấn (query / 쿼리).

`executeUpdate()` thường cho INSERT/cập nhật (update / 업데이트)/DELETE và trả affected count.

`execute()` generic hơn khi kết quả (result / 결과) kiểu (type / 타입) chưa chắc.

Generated keys có thể yêu cầu (request / 요청) qua appropriate statement options.

Không dùng API chỉ vì “nó chạy”; chọn phương thức (method / 메서드) thể hiện expected SQL ngữ nghĩa (semantics / 의미론).

---

# 63. JDBC Transactions

Default liên kết (connection / 연결) thường auto-commit true.

Manual giao dịch (transaction / 트랜잭션):

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

Giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải phản ánh nghiệp vụ (business / 비즈니스) atomic thao tác (operation / 연산), không chỉ một repository phương thức (method / 메서드).

Liên kết (connection / 연결) phải được dùng nhất quán trong đơn vị (unit / 단위) of công việc (work / 작업); mở liên kết (connection / 연결) mới trong mỗi helper có thể phá atomicity.

---

# 64. JDBC Isolation và Savepoints

Liên kết (connection / 연결) cho phép set giao dịch (transaction / 트랜잭션) isolation theo constants.

Actual hành vi (behavior / 동작) phụ thuộc DB.

Savepoint:

```java
Savepoint sp =
    connection.setSavepoint();
```

Quay lui (rollback / 롤백) partial:

```java
connection.rollback(sp);
```

Useful cho nested-like cục bộ (local / 로컬) khôi phục (recovery / 복구) nhưng độ phức tạp (complexity / 복잡도) tăng. Đừng dùng savepoints nếu full giao dịch (transaction / 트랜잭션) quay lui (rollback / 롤백) là nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작) đúng.

---

# 65. JDBC Batch

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
statement.addBatch();
...
int[] counts =
    statement.executeBatch();
```

Batch giảm round trips cho many similar DML.

Nhưng huge batch có bộ nhớ (memory / 메모리)/giao dịch (transaction / 트랜잭션)/log chi phí (cost / 비용). Chunk kích thước (size / 크기) cần measure.

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

Mục tiêu (target / 대상) giới hạn nơi dùng.

Thời gian chạy (runtime / 런타임) annotation chỉ tồn tại để reflection/khung phần mềm (framework / 프레임워크) đọc; tự nó không execute mã (code / 코드).

Compile-time annotation processor là topic sâu hơn.

---

# 67. Reflection

Get lớp (class / 클래스):

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

Reflection giảm compile-time kiểu (type / 타입) an toàn (safety / 안전), có truy cập (access / 접근)/mô-đun (module / 모듈) considerations và thời gian chạy (runtime / 런타임) thất bại (failure / 실패) modes.

Nó hợp ở hạ tầng (infrastructure / 인프라)/khung phần mềm (framework / 프레임워크) ranh giới (boundary / 경계) như serialization/DI/testing tools, không nên là default nghiệp vụ (business / 비즈니스) dispatch.

---

# 68. động (dynamic / 동적) Proxy

JDK động (dynamic / 동적) proxy tạo đối tượng (object / 객체) implement interfaces và intercept phương thức (method / 메서드) calls.

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

Đây là Proxy mẫu (pattern / 패턴) và là cầu nối (bridge / 브리지) rất quan trọng trước Spring AOP.

Caller tưởng đang gọi hiện thực (implementation / 구현) đặc tả hợp đồng (contract / 계약), nhưng proxy chạy lô-gic (logic / 논리) trước/sau.

---

# 69. Classpath và nạp lớp (class loading / 클래스 로딩)

Classpath là nơi thời gian chạy (runtime / 런타임)/trình biên dịch (compiler / 컴파일러) tìm classes/resources.

Dùng chung (common / 공통) errors:

`ClassNotFoundException` thường khi mã (code / 코드) cố tải (load / 로드) lớp (class / 클래스) theo name nhưng loader không tìm thấy.

`NoClassDefFoundError` có thể xảy ra khi lớp (class / 클래스) cần thiết không thể tải (load / 로드)/initialize dù compile trước đó có lớp (class / 클래스).

`NoSuchMethodError` thường do nhị phân (binary / 이진) phụ thuộc (dependency / 의존성) mismatch: compile với thư viện (library / 라이브러리) phiên bản (version / 버전) có phương thức (method / 메서드), thời gian chạy (runtime / 런타임) tải (load / 로드) phiên bản (version / 버전) không có.

Khi gặp linkage lỗi (error / 오류), inspect actual phụ thuộc (dependency / 의존성) cây (tree / 트리)/sản phẩm tạo ra (artifact / 산출물), không chỉ nguồn (source / 소스).

---

# 70. ClassLoader định danh (identity / 식별자)

Ở mức Intermediate, nhớ rằng lớp (class / 클래스) định danh (identity / 식별자) không chỉ name; defining classloader cũng matter.

Hai `com.example.Plugin` loaded bởi different classloaders có thể được xem như distinct thời gian chạy (runtime / 런타임) types.

Plugin containers/app servers dùng custom loaders và có classloader leaks/casting surprises. cấp cao (senior / 시니어) sẽ đi sâu.

---

# 71. JPMS mô-đun (module / 모듈) hệ thống (system / 시스템)

Java 9 mô-đun (module / 모듈) descriptor:

```java
module com.example.app {
    requires java.sql;

    exports com.example.api;

    opens com.example.model
        to some.framework;
}
```

`exports` cho compile/thời gian chạy (runtime / 런타임) truy cập (access / 접근) công khai (public / 공개) types.

`opens` cho deep reflection truy cập (access / 접근).

`uses`/`provides` hỗ trợ dịch vụ (service / 서비스) Provider giao diện (interface / 인터페이스).

Không phải mọi Spring/backend app cần JPMS, nhưng mô-đun (module / 모듈) encapsulation giải thích một số reflection truy cập (access / 접근) errors hiện đại (modern / 현대적) Java.

---

# 72. ServiceLoader và SPI

Giao diện (interface / 인터페이스):

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

Đây là bản địa (native / 네이티브) Java plugin cơ chế (mechanism / 메커니즘).

Plugin discovery là chiến lược (strategy / 전략) + provider registry.

Spring DI có hệ thống riêng phong phú hơn, nhưng SPI giúp hiểu khung phần mềm (framework / 프레임워크) extension kiến trúc (architecture / 아키텍처).

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

# 74. tiêu chuẩn (standard / 표준) HTTP máy khách (client / 클라이언트) Java 11

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

```java
HttpClient client =
    HttpClient.newBuilder()
        .connectTimeout(
            Duration.ofSeconds(2))
        .build();
```

Yêu cầu (request / 요청):

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

Connect hết thời gian chờ (timeout / 타임아웃) và yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) là distinct layers.

Reuse HttpClient where appropriate; liên kết (connection / 연결) pooling/tài nguyên (resource / 자원) setup benefit.

---

# 75. ngân sách thời gian chờ (timeout budget / 타임아웃 예산)

Nếu incoming thao tác (operation / 연산) ngân sách (budget / 예산) 2 seconds, downstream calls không nên mỗi cái hết thời gian chờ (timeout / 타임아웃) 5 seconds.

Ngân sách (budget / 예산) thinking:

```text
total deadline
→ remaining time
→ child operation timeout
```

Intermediate chỉ cần hình thành nguyên tắc này. cấp cao (senior / 시니어) sẽ đi vào deadline propagation/thử lại (retry / 재시도).

---

# 76. hiện đại (modern / 현대적) Java 14–17

Switch expressions Java 14 giúp expression-style branching.

Văn bản (text / 텍스트) blocks Java 15 giúp multiline SQL/JSON.

Records Java 16 cho dữ liệu (data / 데이터)/giá trị (value / 값) carriers.

Mẫu (pattern / 패턴) matching for `instanceof` Java 16 giảm cast boilerplate.

Sealed classes Java 17 giới hạn subtype set.

Đây không chỉ cú pháp (syntax / 문법) sugar; chúng làm dữ liệu (data / 데이터) modeling rõ và trình biên dịch (compiler / 컴파일러) có thêm thông tin.

---

# 77. mẫu (pattern / 패턴) Matching for Switch Java 21

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

Trình biên dịch (compiler / 컴파일러) check exhaustiveness.

Guard with `when` trong mẫu (pattern / 패턴) switch:

```java
case Success s
    when s.id() > 100 -> ...
```

Dùng khi quyết định (decision / 결정) là data-oriented closed variants. Nếu mỗi subtype có hành vi (behavior / 동작) tự nhiên, polymorphic phương thức (method / 메서드) có thể tốt hơn.

---

# 78. bản ghi (record / 레코드) Patterns Java 21

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

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

Mẫu (pattern / 패턴) matching giúp parse/branch dữ liệu (data / 데이터) structures, nhưng đừng biến lĩnh vực (domain / 도메인) thành massive switch nếu object-oriented hành vi (behavior / 동작) rõ hơn.

---

# 79. Sequenced Collections Java 21

Interfaces như `SequencedCollection`, `SequencedSet`, `SequencedMap` thống nhất truy cập (access / 접근) first/last/reversed ngữ nghĩa (semantics / 의미론) cho ordered collections.

Ví dụ concept:

```java
collection.getFirst();
collection.getLast();
collection.reversed();
```

Trước Java 21, mỗi collection có APIs khác nhau hoặc cần chỉ mục (index / 인덱스)/iterator hacks.

---

# 80. UUID, Base64, Random và SecureRandom

UUID:

```java
UUID id =
    UUID.randomUUID();
```

thích hợp identifiers không cần centralized chuỗi (sequence / 시퀀스) trong nhiều contexts, nhưng lưu trữ (storage / 저장소)/indexing trade-offs tồn tại.

Base64 là encoding, không encryption.

```java
String encoded =
    Base64.getEncoder()
          .encodeToString(bytes);
```

`Random`/`ThreadLocalRandom` cho non-security randomness.

`SecureRandom` cho cryptographic randomness.

Không dùng `Random` tạo reset đơn vị từ (token / 토큰)/session secret.

---

# 81. Locale, Currency, ResourceBundle

Locale-sensitive formatting phải tường minh (explicit / 명시적).

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

Không assume máy chủ (server / 서버) default locale/timezone; bộ chứa (container / 컨테이너)/máy chủ (server / 서버) có thể khác cục bộ (local / 로컬) laptop.

---

# 82. Charset

Bytes không tự là văn bản (text / 텍스트). Cần encoding.

```java
String text =
    Files.readString(
        path,
        StandardCharsets.UTF_8);
```

Nếu ghi (write / 쓰기) UTF-8 nhưng read EUC-KR, mojibake xuất hiện.

Make charset part of đặc tả hợp đồng (contract / 계약).

Nền tảng (platform / 플랫폼) default charset thay đổi qua Java generations/environments; tường minh (explicit / 명시적) UTF-8 safest khi giao thức (protocol / 프로토콜)/tệp (file / 파일) đặc tả hợp đồng (contract / 계약) định nghĩa UTF-8.

---

# 83. bản địa (native / 네이티브) Java Serialization awareness

`Serializable` cho built-in đối tượng (object / 객체) serialization.

Nhưng bản địa (native / 네이티브) Java serialization có tight lớp (class / 클래스) coupling và historical bảo mật (security / 보안) risks.

Bạn cần biết để maintain legacy các hệ thống (systems / 시스템들), không nên chọn làm default new API/message format.

Use JSON/CBOR/Protobuf/etc theo ecosystem requirements thay vì `ObjectOutputStream` chỉ vì built-in.

---

# 84. bảo mật (security / 보안) API awareness

Băm (hash / 해시):

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

Nhưng cryptography là giao thức (protocol / 프로토콜) thiết kế (design / 설계), không chỉ gọi API.

Không tự invent encryption scheme.

Password hashing không dùng raw SHA-256; cần adaptive password băm (hash / 해시) libraries/algorithms theo bảo mật (security / 보안) chính sách (policy / 정책).

Cấp cao (senior / 시니어)/Master sẽ đi sâu.

---

# 85. API thiết kế (design / 설계): Strong Types

Bad:

```java
transfer(
    long from,
    long to,
    BigDecimal amount,
    String currency);
```

Better lĩnh vực (domain / 도메인) concepts:

```java
transfer(
    AccountId from,
    AccountId to,
    Money amount);
```

Strong types làm illegal argument mix khó compile.

Thành phần nguyên thủy (primitive / 기본 요소) obsession là khi lĩnh vực (domain / 도메인) concepts bị biểu diễn bằng raw primitives/strings quá lâu.

---

# 86. Command/truy vấn (query / 쿼리) Separation mindset

Phương thức (method / 메서드):

```java
User activate(User user)
```

vừa mutate trạng thái (state / 상태) vừa return dữ liệu (data / 데이터) có thể okay, nhưng API khó hiểu nếu truy vấn (query / 쿼리) methods có hidden side effects.

Tư duy CQS nói command thay trạng thái (state / 상태) và truy vấn (query / 쿼리) đọc trạng thái (state / 상태) nên thường dễ phân biệt.

Không phải luật cấm methods vừa return kết quả (result / 결과) sau mutation; mục tiêu là side effects tường minh (explicit / 명시적).

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

Bạn thêm hành vi (behavior / 동작) bằng wrapping thay vì subclass deep hierarchy.

Java I/O và many khung phần mềm (framework / 프레임워크) proxies use this structural idea.

---

# 88. Factory và Static Factory

Static factory names:

```java
UserId.of(value)
Money.zero(currency)
Duration.ofSeconds(2)
List.of(...)
```

có thể communicate ngữ nghĩa (semantics / 의미론) tốt hơn overloaded constructors.

Factory có thể choose subtype/bộ nhớ đệm (cache / 캐시)/reuse.

Không tạo separate factory lớp (class / 클래스) nếu static factory đủ rõ.

---

# 89. Builder

Builder phù hợp cấu hình (config / 설정) đối tượng (object / 객체) có many optional fields.

Nhưng Java records + named static factory có thể đủ cho small dữ liệu (data / 데이터) structures.

Mẫu (pattern / 패턴) là phản hồi (response / 응답) to constructor readability/optional combinations, không phải yêu cầu (requirement / 요구사항) cho every lĩnh vực (domain / 도메인) thực thể (entity / 엔터티).

---

# 90. Template phương thức (method / 메서드) vs chiến lược (strategy / 전략)

Template phương thức (method / 메서드) dùng inheritance để cố định thuật toán (algorithm / 알고리즘) skeleton.

Chiến lược (strategy / 전략) dùng composition để inject hành vi (behavior / 동작).

Nếu subclass hierarchy stable, template phương thức (method / 메서드) okay.

Nếu cần combine hành vi (behavior / 동작)/thời gian chạy (runtime / 런타임) replace/testing, chiến lược (strategy / 전략) thường flexible.

Biết sự đánh đổi (trade-off / 트레이드오프) quan trọng hơn “composition always”.

---

# 91. Adapter

Adapter chuyển bên ngoài (external / 외부) giao diện (interface / 인터페이스) sang nội bộ (internal / 내부) đặc tả hợp đồng (contract / 계약).

```java
final class VendorPaymentAdapter
        implements PaymentGateway {

    private final VendorSdk sdk;
}
```

Vendor exception/types dừng ở adapter.

Đây là anti-corruption ranh giới (boundary / 경계) và sẽ rất quan trọng trong Spring HTTP/JPA integrations.

---

# 92. Command mẫu (pattern / 패턴) với Functional Interfaces

Command đối tượng (object / 객체)/lambda biểu diễn thao tác (operation / 연산) như dữ liệu (data / 데이터)/hành vi (behavior / 동작) giá trị (value / 값).

```java
Runnable task =
    () -> processOrder(id);
```

Executors nhận commands.

Complex command có thể là lớp (class / 클래스) chứa parameters + execute hành vi (behavior / 동작).

Patterns trong hiện đại (modern / 현대적) Java thường được biểu diễn nhẹ hơn nhờ lambdas/records.

---

# 93. JVM bộ nhớ (memory / 메모리): ngăn xếp (stack / 스택), vùng nhớ động (heap / 힙), Metaspace, bản địa (native / 네이티브)

Mỗi luồng thực thi (thread / 스레드) có ngăn xếp (stack / 스택) chứa frames/cục bộ (local / 로컬) thực thi (execution / 실행) trạng thái (state / 상태).

Vùng nhớ vùng nhớ động (heap / 힙) chứa most objects/arrays managed by GC.

Metaspace chứa lớp (class / 클래스) siêu dữ liệu (metadata / 메타데이터) ngoài vùng nhớ động (heap / 힙).

Direct buffers/bản địa (native / 네이티브) libraries/luồng thực thi (thread / 스레드) stacks dùng bản địa (native / 네이티브) bộ nhớ (memory / 메모리) ngoài Java vùng nhớ động (heap / 힙).

Do đó:

```text
-Xmx = 2G
```

không nghĩa tiến trình (process / 프로세스) RSS tối đa 2G.

Máy chủ (server / 서버)/bộ chứa (container / 컨테이너) bộ nhớ (memory / 메모리) planning phải chừa bản địa (native / 네이티브) headroom.

---

# 94. Garbage Collection awareness

GC tìm objects còn reachable từ roots như luồng thực thi (thread / 스레드) stacks/static/JNI references và reclaim unreachable objects.

Java bộ nhớ (memory / 메모리) leak vẫn có thể xảy ra khi đối tượng (object / 객체) không còn business-useful nhưng vẫn reachable, ví dụ static danh sách (list / 목록)/bộ nhớ đệm (cache / 캐시)/hàng đợi (queue / 큐)/listener.

Đầu tiên fix retention/quyền sở hữu (ownership / 소유권); đừng đổi collector để chữa logical leak.

Dùng chung (common / 공통) collectors hiện đại gồm G1, ZGC, Parallel, Serial; selection/tuning sang cấp cao (senior / 시니어).

---

# 95. JIT và Warm-up

JVM ban đầu interpret/compile progressively. Hot methods được JIT optimize dựa thời gian chạy (runtime / 런타임) profile.

Benchmark:

```java
long start =
    System.nanoTime();
doWork();
long elapsed =
    System.nanoTime() - start;
```

một lần không đủ kết luận vì warm-up, dead-code elimination, GC, CPU scaling và profiling.

Use JMH mindset/công cụ (tool / 도구) cho microbenchmark quan trọng.

Cấp cao (senior / 시니어) sẽ đi sâu inlining/deoptimization/escape phân tích (analysis / 분석).

---

# 96. `javac --release`

Nếu develop bằng JDK 25 nhưng mục tiêu (target / 대상) Java 17:

```bash
javac --release 17 ...
```

giúp trình biên dịch (compiler / 컴파일러) enforce Java 17 ngôn ngữ (language / 언어)/API nền tảng (platform / 플랫폼) baseline.

Chỉ `-source 17 -target 17` historically không luôn ngăn mã (code / 코드) gọi APIs mới có trong hiện tại (current / 현재) JDK.

Bản dựng (build / 빌드) tools thường expose equivalent bản phát hành (release / 릴리스) cấu hình (configuration / 구성).

---

# 97. JVM Options cơ bản

Vùng nhớ vùng nhớ động (heap / 힙):

```bash
-Xms512m
-Xmx2g
```

Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택):

```bash
-Xss1m
```

Hệ thống (system / 시스템) thuộc tính (property / 속성):

```bash
-Dapp.env=prod
```

GC logging hiện đại (modern / 현대적):

```bash
-Xlog:gc*
```

Vùng nhớ vùng nhớ động (heap / 힙) dump on OOM:

```bash
-XX:+HeapDumpOnOutOfMemoryError
```

Không bản sao (copy / 복사) môi trường vận hành (production / 운영 환경) flags từ random blog. JVM defaults thay đổi theo phiên bản (version / 버전)/hardware/bộ chứa (container / 컨테이너).

---

# 98. `jcmd`, `jstack`, `jmap`, `jstat`

Find Java tiến trình (process / 프로세스):

```bash
jcmd
```

Luồng thực thi (thread / 스레드) dump:

```bash
jcmd <pid> Thread.print
```

JFR start/dump và GC/lớp (class / 클래스) info cũng qua `jcmd`.

`jstack` cho luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) legacy/dùng chung (common / 공통) usage.

`jmap` có heap-related operations.

`jstat` xem JVM stats sampling.

Hiện đại (modern / 현대적) môi trường vận hành (production / 운영 환경) habit: ưu tiên diagnostic tools dựa bằng chứng (evidence / 증거) thay vì restart trước khi collect dữ liệu (data / 데이터).

---

# 99. Java Flight Recorder awareness

JFR là built-in low-overhead sự kiện (event / 이벤트) recording/profiling facility.

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

tùy settings/phiên bản (version / 버전).

Cấp cao (senior / 시니어) sẽ dùng JFR như primary môi trường vận hành (production / 운영 환경) diagnostic công cụ (tool / 도구).

Intermediate chỉ cần biết Java có khả năng quan sát (observability / 관측 가능성) sâu hơn logs.

---

# 100. Logging awareness

Java cốt lõi (core / 핵심) có `java.util.logging`, nhưng ứng dụng (application / 애플리케이션) ecosystems thường dùng lớp trừu tượng (abstraction / 추상화)/facade như SLF4J sau này.

Cốt lõi (core / 핵심) principle: log ngữ cảnh (context / 맥락), not secrets.

```text
orderId
requestId
operation
duration
error category
```

Không log password/đơn vị từ (token / 토큰).

Không concatenate huge strings nếu log disabled.

Logging không thay metrics/traces/profiles.

---

# 101. mã (code / 코드) Smells ở Intermediate

Thành phần nguyên thủy (primitive / 기본 요소) obsession xuất hiện khi `String` đại diện Email, Currency, Status, UserId khắp nơi.

Boolean parameter explosion:

```java
process(true, false, true)
```

khó đọc.

Tính năng (feature / 기능) envy khi lớp (class / 클래스) lấy hàng loạt getters của đối tượng (object / 객체) khác rồi làm lô-gic (logic / 논리) lẽ ra thuộc đối tượng (object / 객체) kia.

Shotgun surgery khi một nghiệp vụ (business / 비즈니스) thay đổi (change / 변경) cần sửa 20 classes vì concept bị phân tán.

Hidden side tác động (effect / 효과) khi phương thức (method / 메서드) tên `findUser()` lại cập nhật (update / 업데이트) DB/bộ nhớ đệm (cache / 캐시)/mạng (network / 네트워크).

Recognize smell là để investigate thiết kế (design / 설계) pressure, không phải auto-refactor mọi trường hợp (case / 사례).

---

# 102. lỗi (error / 오류) Handling mẫu (pattern / 패턴) trong Backend

Không thử lại (retry / 재시도) programming bug.

Không thử lại (retry / 재시도) kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류).

Transient mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스) errors có thể thử lại (retry / 재시도) nếu thao tác (operation / 연산) idempotent và bounded.

Preserve cause.

Translate at boundaries.

Log once at quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계).

Những rules này chuẩn bị cho resilience/Spring exception kiến trúc (architecture / 아키텍처).

---

# 103. phụ thuộc (dependency / 의존성) Direction trước Spring

Ứng dụng (application / 애플리케이션) dịch vụ (service / 서비스):

```java
final class PlaceOrderService {
    private final OrderRepository repository;
    private final PaymentGateway payment;
}
```

Interfaces/ports thuộc cốt lõi (core / 핵심)/ứng dụng (application / 애플리케이션).

JDBC/HTTP implementations depend inward:

```text
JdbcOrderRepository
→ implements OrderRepository

HttpPaymentGateway
→ implements PaymentGateway
```

Spring sau này chỉ wire implementations.

Nếu bạn hiểu phụ thuộc (dependency / 의존성) Inversion bằng plain Java, Spring DI sẽ không còn là magic.

---

# 104. gói (package / 패키지) Visibility như kiến trúc (architecture / 아키텍처) công cụ (tool / 도구)

Không công khai (public / 공개) mọi hiện thực (implementation / 구현).

```java
final class JdbcUserMapper {
}
```

package-private nếu chỉ repository gói (package / 패키지) cần.

Công khai (public / 공개) surface nhỏ giảm accidental coupling.

Gói (package / 패키지) by tính năng (feature / 기능) giúp nội bộ (internal / 내부) classes gần nhau và visibility hữu dụng hơn.

---

# 105. Testing Mindset trước khung phần mềm (framework / 프레임워크)

Pure dịch vụ (service / 서비스) với injected dependencies kiểm thử (test / 테스트) dễ.

Thời gian (time / 시간) dùng `Clock`.

IDs dùng `Supplier<UUID>` hoặc generator giao diện (interface / 인터페이스).

Bên ngoài (external / 외부) gateway fake/mock.

Không cần Mockito/Spring để hiểu testability. khung phần mềm (framework / 프레임워크) tools chỉ automate seams mà thiết kế (design / 설계) đã tạo.

---

# 106. Legacy Java bạn sẽ gặp trong enterprise và cách hiện đại hóa mà không phá hệ thống

Legacy Java không đồng nghĩa “mã (code / 코드) xấu”. Nhiều hệ thống quan trọng được viết đúng với các ràng buộc (constraints / 제약조건들) của Java 6/7/8 và khung phần mềm (framework / 프레임워크) thời đó. Kỹ năng cần có là **đọc mô hình tư duy (mental model / 사고 모델) cũ, nhận ra replacement hiện đại, rồi migrate có kiểm soát** thay vì rewrite theo style mới chỉ vì nhìn đẹp hơn.

Trong mã (code / 코드) Java 8 hoặc cũ hơn, bạn sẽ gặp anonymous classes ở những nơi mã (code / 코드) mới dùng lambda. Đổi sang lambda có thể giảm noise, nhưng đừng biến callback nhiều trạng thái (state / 상태)/lô-gic (logic / 논리) thành lambda 30 dòng chỉ để “modernize”. Named lớp (class / 클래스) đôi khi vẫn dễ đọc hơn.

Bạn cũng sẽ gặp `Date`, `Calendar` và `SimpleDateFormat`. `SimpleDateFormat` mutable và không thread-safe; static dùng chung (shared / 공유) formatter trong máy chủ (server / 서버) có thể race. mã (code / 코드) mới nên dùng `java.time` và immutable `DateTimeFormatter`. Khi migrate, phải xác định ngữ nghĩa (semantic / 의미적) trước: `Date` cũ đang đại diện chính xác (exact / 정확한) instant, cục bộ (local / 로컬) nghiệp vụ (business / 비즈니스) date hay chỉ timestamp DB? Chuyển bừa sang `LocalDateTime` có thể làm mất timezone meaning.

Legacy collections có `Vector`, `Hashtable` và `Stack`. Chúng không “không dùng được”, nhưng synchronization ngữ nghĩa (semantics / 의미론) và API thiết kế (design / 설계) thường không phải lựa chọn tốt cho mã (code / 코드) mới. `ArrayList`, `HashMap`/`ConcurrentHashMap`, `ArrayDeque` thường rõ hơn tùy yêu cầu (requirement / 요구사항). Không thay `Hashtable` bằng `HashMap` chỉ vì mới hơn nếu old mã (code / 코드) thật sự dựa concurrent truy cập (access / 접근); trước tiên phải xác định compound atomicity và quyền sở hữu (ownership / 소유권).

I/O legacy thường dùng `File`, `FileInputStream`, `FileReader` với nền tảng (platform / 플랫폼) default charset. hiện đại (modern / 현대적) mã (code / 코드) nên ưu tiên `Path`/`Files` và charset tường minh (explicit / 명시적). tính đồng thời (concurrency / 동시성) legacy có thể tạo raw `Thread`, dùng `wait/notify`, `Timer/TimerTask` hoặc synchronized collections; hiện đại (modern / 현대적) executors, `BlockingQueue`, scheduled executors và atomics thường dễ reason hơn, nhưng di chuyển (migration / 마이그레이션) phải preserve giao thức (protocol / 프로토콜) chứ không chỉ replace API names.

JDK 8 → 11 di chuyển (migration / 마이그레이션) có một nhóm lỗi không nằm trong nguồn (source / 소스) style: JAXB/JAX-WS và Java EE/CORBA modules từng đi kèm JDK đã bị loại khỏi JDK 11. mã (code / 코드) cũ có thể compile/run trên JDK 8 rồi báo missing lớp (class / 클래스) trên 11 cho tới khi dependencies được khai báo rõ trong bản dựng (build / 빌드).

JDK 17 tạo tính tương thích (compatibility / 호환성) ranh giới (boundary / 경계) khác: strong encapsulation của JDK internals mạnh hơn. thư viện (library / 라이브러리) cũ dùng reflection vào private fields của `java.*` có thể thất bại (fail / 실패). `--add-opens` có thể là temporary di chuyển (migration / 마이그레이션) cầu nối (bridge / 브리지), nhưng long-term fix là cập nhật (update / 업데이트) thư viện (library / 라이브러리) hoặc chuyển sang supported API.

Khi lên Java 21, Virtual Threads không có nghĩa phải rewrite executor kiến trúc (architecture / 아키텍처) ngay. Trước hết đo tải công việc (workload / 워크로드): bottleneck là blocking nền tảng (platform / 플랫폼) threads hay DB pool/CPU? Virtual luồng thực thi (thread / 스레드) giảm chi phí (cost / 비용) chờ của Java threads, nhưng pool 30 cơ sở dữ liệu (database / 데이터베이스) connections vẫn chỉ có 30 connections.

Cách migrate an toàn là tách **nền tảng (platform / 플랫폼) upgrade** khỏi **nguồn (source / 소스) modernization** khi có thể: chạy tests trên JDK mới, sửa dependencies/removed APIs, xử lý illegal reflection, đo GC/bộ nhớ (memory / 메모리)/độ trễ (latency / 지연 시간) baseline, rồi refactor từng vùng với tests. Hai mục tiêu có rủi ro (risk / 위험) profile khác nhau.

---

# 107. phiên bản (version / 버전) tính tương thích (compatibility / 호환성)

Có ba axes:

```text
source syntax
class-file target
runtime/platform APIs
```

Bạn có thể viết cú pháp (syntax / 문법) Java 17 nhưng gọi Java 25 API nếu bản dựng (build / 빌드) cấu hình (config / 설정) không enforce bản phát hành (release / 릴리스) correctly.

Thời gian chạy (runtime / 런타임) old sẽ thất bại (fail / 실패).

Dependencies cũng có minimum Java phiên bản (version / 버전).

Upgrade JDK phải kiểm thử (test / 테스트) libraries/bản dựng (build / 빌드) tools/thời gian chạy (runtime / 런타임), không chỉ trình biên dịch (compiler / 컴파일러).

---

# 108. Intermediate dự án (project / 프로젝트): thứ tự (order / 순서) Processing dịch vụ (service / 서비스) cốt lõi (core / 핵심)

Viết plain Java ứng dụng (application / 애플리케이션) xử lý orders với `Order`, `Money`, `OrderStatus`, `CustomerId`, repository giao diện (interface / 인터페이스) và JDBC hiện thực (implementation / 구현).

Dùng Flyway-like SQL scripts manually if needed, nhưng mục tiêu là JDBC giao dịch (transaction / 트랜잭션) đúng.

Thêm bên ngoài (external / 외부) HTTP máy khách (client / 클라이언트) Java 11 để gọi fake payment API với hết thời gian chờ (timeout / 타임아웃).

Thêm executor/CompletableFuture để tải (load / 로드) two independent datasets concurrently, sau đó giới hạn tính đồng thời (concurrency / 동시성).

Dùng JFR/jcmd để quan sát luồng thực thi (thread / 스레드)/vùng nhớ động (heap / 힙).

Viết reflection-based simple annotation scanner nhỏ để hiểu siêu dữ liệu (metadata / 메타데이터)/proxy trước Spring.

Dự án (project / 프로젝트) này là cầu nối (bridge / 브리지) trực tiếp sang cấp cao (senior / 시니어) và Spring.

---

# 109. Intermediate → cấp cao (senior / 시니어) Gate

Bạn sẵn sàng sang cấp cao (senior / 시니어) khi có thể giải thích invariance, PECS, kiểu (type / 타입) erasure và unsafe raw types; chọn collection dựa ngữ nghĩa (semantics / 의미론); hiểu equals/hashCode/comparator contracts; phân biệt immutable snapshot và unmodifiable view; giải thích Stream laziness, flatMap, collectors và parallel-stream risks.

Bạn phải reason tính đồng thời (concurrency / 동시성) bằng race/visibility/atomicity/happens-before; biết khi nào synchronized, volatile, atomic, locks, executors, blocking queues, CompletableFuture và virtual threads phù hợp.

Bạn phải viết JDBC tài nguyên (resource / 자원) vòng đời (lifecycle / 생명주기)/giao dịch (transaction / 트랜잭션) đúng, hiểu reflection/động (dynamic / 동적) proxy/classpath/classloader errors và đọc hiện đại (modern / 현대적) Java 11–21 features.

Bạn phải biết JVM bộ nhớ (memory / 메모리) không chỉ vùng nhớ động (heap / 힙), GC không chữa logical leak, JIT cần warm-up và JFR/jcmd tồn tại để gỡ lỗi (debug / 디버그) bằng bằng chứng (evidence / 증거).

Ở mức (level / 수준) này, “mã (code / 코드) chạy” chưa đủ. Bạn cần biết **vì sao nó đúng dưới nhiều inputs, threads, environments và failures**.

---

# 110. Điều để sang cấp cao (senior / 시니어)

Cấp cao (senior / 시니어) sẽ đào sâu bytecode, ngăn xếp (stack / 스택) frames, JIT inlining/deoptimization, escape phân tích (analysis / 분석), nạp lớp (class loading / 클래스 로딩) định danh (identity / 식별자)/initialization, Java bộ nhớ (memory / 메모리) mô hình (model / 모델) formal hơn, safe publication, deadlocks/contention, CAS/ABA, advanced concurrent collections, executor saturation, CompletableFuture thất bại (failure / 실패) topology, virtual-thread môi trường vận hành (production / 운영 환경) trade-offs, GC roots/leaks, G1/ZGC, bản địa (native / 네이티브) bộ nhớ (memory / 메모리), JFR sự cố (incident / 인시던트) workflow, hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링), NIO/direct buffers, remote-call resilience, MethodHandle, JDBC pool/isolation, bảo mật (security / 보안), API tính tương thích (compatibility / 호환성), kiến trúc (architecture / 아키텍처) và distributed-system patterns.

---

# References for version-sensitive topics

Oracle Java SE hỗ trợ (support / 지원) Roadmap:
https://www.oracle.com/java/technologies/java-se-support-roadmap.html

Oracle Java API:
https://docs.oracle.com/en/java/javase/

OpenJDK JEP chỉ mục (index / 인덱스):
https://openjdk.org/jeps/0

> **Bàn giao:** Sau **Thread: đối tượng (object / 객체) Java và thực thi (execution / 실행) ngữ cảnh (context / 맥락) khác nhau thế nào?**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
