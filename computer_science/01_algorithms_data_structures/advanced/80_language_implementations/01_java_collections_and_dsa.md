# Java Collections nhìn dưới góc DSA
**Java Collections & Data Structure Selection / Java Collections와 자료구조 선택**

Java Collections Framework cung cấp các lớp trừu tượng an toàn và tiện dụng hơn việc tự quản con trỏ, nhưng lớp trừu tượng không làm độ phức tạp biến mất. Khi chọn `List`, `Map`, `Set`, `Queue` hay `Deque`, ta vẫn đang chọn một cấu trúc dữ liệu với bất biến, bố trí bộ nhớ và đặc tính hiệu năng cụ thể.

Học DSA trong Java nên có hai lớp: hiểu cấu trúc dữ liệu/thuật toán ở mức khái niệm, sau đó biết collection nào của JDK hiện thực ngữ nghĩa đó và phải trả chi phí gì.

## Interface trước cách triển khai

Các interface như `List`, `Set`, `Map`, `Queue`, `Deque`, `NavigableMap` và `NavigableSet` mô tả hợp đồng hành vi. Các lớp như `ArrayList`, `LinkedList`, `HashMap`, `HashSet`, `TreeMap`, `TreeSet`, `ArrayDeque` và `PriorityQueue` cung cấp cách triển khai cụ thể.

```java
List<Integer> xs = new ArrayList<>();
Map<String, User> users = new HashMap<>();
Deque<Task> q = new ArrayDeque<>();
```

Mã ở cấp API nên phụ thuộc interface khi hợp lý, nhưng mã nhạy về hiệu năng vẫn phải biết concrete type bên dưới.

## ArrayList là lựa chọn mặc định mạnh cho List

`ArrayList` dựa trên mảng có thể thay đổi kích thước.

```text
get/set theo chỉ số      O(1)
thêm cuối                O(1) khấu hao
chèn/xóa ở giữa          O(n)
contains                 O(n)
```

Nó thường có tính cục bộ bộ nhớ tốt hơn danh sách mỗi nút một object và có ít chi phí phụ trên mỗi phần tử. Ngay cả khi bài toán có chèn/xóa, `ArrayList` vẫn thường phù hợp nếu thao tác chủ yếu ở cuối hoặc dữ liệu không quá lớn.

## LinkedList không tự động nhanh hơn khi chèn/xóa

Chèn hoặc xóa tại một nút đã biết có thể `O(1)`, nhưng `list.add(i, x)` phải tìm tới vị trí `i` trước và thường mất `O(n)`. Ngoài ra, mỗi nút là một object riêng, làm tăng cấp phát, lần theo reference và áp lực GC.

Vì vậy câu “LinkedList chèn O(1)” chỉ đúng khi đã có vị trí nút và bỏ qua các chi phí khác.

## ArrayDeque cho stack, queue và deque

```java
Deque<Integer> dq = new ArrayDeque<>();
dq.push(10);
int x = dq.pop();
dq.offerLast(20);
int y = dq.pollFirst();
```

`ArrayDeque` thường là lựa chọn mặc định tốt hơn `LinkedList` cho stack/queue và tốt hơn lớp `Stack` cũ. `java.util.Stack` kế thừa `Vector` và mang theo thiết kế đồng bộ hóa kiểu cũ; mã hiện đại thường dùng `Deque`.

## HashMap và hợp đồng equals/hashCode

`HashMap` cho tra cứu, chèn và xóa kỳ vọng gần `O(1)`, nhưng không duy trì thứ tự đã sắp xếp. Tính đúng đắn của khóa phụ thuộc hợp đồng:

```text
nếu a.equals(b) == true
thì a.hashCode() == b.hashCode()
```

Chiều ngược lại không bắt buộc: cùng hash không có nghĩa hai object bằng nhau.

### Không nên dùng khóa có thể thay đổi

Nếu trường tham gia `equals/hashCode` thay đổi sau khi khóa đã được chèn, `HashMap` không tự di chuyển entry sang bucket mới.

```java
record Key(int userId, int productId) {}
```

Record bất biến theo thành phần rất phù hợp cho khóa trạng thái tổng hợp trong DSA.

### Va chạm và hệ số tải

HashMap không phải direct addressing. Chất lượng hash, hệ số tải và chi phí `equals` đều ảnh hưởng hiệu năng. Resize là thao tác đắt nhưng được phân bổ trên nhiều lần `put`.

Nếu biết trước số lượng phần tử lớn, đặt dung lượng ban đầu hợp lý có thể giảm số lần resize. Không nên phụ thuộc vào các ngưỡng nội bộ không được bảo đảm giữa các phiên bản JDK.

## HashSet

`HashSet` phù hợp cho:

```text
visited
membership
deduplication
```

Nếu cần thứ tự, `floor`, `ceiling` hoặc truy vấn khoảng, cần cấu trúc có thứ tự như `TreeSet`.

## TreeMap và TreeSet

`TreeMap` và `TreeSet` cung cấp ánh xạ/tập có thứ tự, thường với các thao tác chính `O(log n)`:

```java
NavigableMap<Integer, String> map = new TreeMap<>();
map.floorEntry(x);
map.ceilingEntry(x);
map.subMap(l, true, r, false);
```

Comparator phải nhất quán và có tính bắc cầu. Tránh:

```java
(a, b) -> a.priority - b.priority
```

vì phép trừ có thể tràn số. Nên dùng:

```java
Comparator.comparingInt(Node::priority)
Integer.compare(a, b)
```

Nếu comparator trả `0`, `TreeMap`/`TreeSet` xem hai khóa nằm cùng vị trí thứ tự, dù `equals` có thể cho kết quả khác. Đây là khác biệt quan trọng với HashMap.

## PriorityQueue

`PriorityQueue` là heap:

```text
peek     O(1)
offer    O(log n)
poll     O(log n)
```

Một mẫu Dijkstra phổ biến là chèn trạng thái khoảng cách mới thay vì decrease-key, rồi bỏ qua entry cũ khi lấy ra.

```java
record State(int node, long dist) {}
PriorityQueue<State> pq =
    new PriorityQueue<>(Comparator.comparingLong(State::dist));
```

Không sửa trường dùng để so sánh của object đang nằm trong queue rồi kỳ vọng heap tự sắp xếp lại. Hãy chèn một trạng thái mới hoặc dùng indexed heap chuyên dụng.

## Mảng primitive thường tốt hơn collection đóng hộp trong DSA

```java
int[] parent;
long[] dist;
boolean[] seen;
```

thường gọn và nhanh hơn `List<Integer>`, `List<Long>` hoặc `List<Boolean>` khi kích thước đã biết.

Autoboxing làm cú pháp tiện hơn nhưng tạo thêm object/reference và có thể tăng áp lực GC. Unboxing `null` còn gây `NullPointerException`.

## Biểu diễn đồ thị

Dạng dễ đọc:

```java
record Edge(int to, int weight) {}
List<List<Edge>> g;
```

Với hàng triệu cạnh, object overhead có thể đáng kể. Khi đó có thể chuyển sang mảng primitive hoặc CSR:

```text
int[] offsets
int[] to
long[] weight
```

Nên bắt đầu từ biểu diễn rõ ràng rồi tối ưu khi profiling cho thấy bộ nhớ hoặc GC thực sự là nút thắt.

## Record và tính bất biến

Record rất hợp cho trạng thái hàng đợi ưu tiên, khóa map tổng hợp, cạnh và tọa độ:

```java
record Cell(int r, int c, int mask) {}
```

Tuy nhiên, record chỉ làm các reference thành phần không thể được gán lại. Nếu thành phần là một `List` có thể thay đổi thì nội dung bên trong vẫn mutable. Khóa băm cần mức bất biến đủ sâu để `equals/hashCode` không thay đổi trong thời gian khóa nằm trong map.

## computeIfAbsent, merge và miền khóa

```java
Map<String, List<String>> g = new HashMap<>();
g.computeIfAbsent(u, k -> new ArrayList<>()).add(v);

freq.merge(x, 1, Integer::sum);
```

Các API này rất tiện cho map thưa. Nhưng nếu khóa là số nguyên dày đặc `0..n-1`, mảng thường đơn giản và rẻ hơn:

```java
int[] count = new int[n];
```

Miền khóa quyết định cấu trúc phù hợp. HashMap không phải lựa chọn mặc định cho mọi bài toán ánh xạ.

## EnumMap, EnumSet và BitSet

Nếu khóa là enum, `EnumMap` và `EnumSet` khai thác miền khóa hữu hạn hiệu quả hơn cấu trúc hash tổng quát.

`BitSet` nén nhiều cờ Boolean và hỗ trợ AND/OR/XOR trên nhiều bit mỗi từ máy. Nó hữu ích cho tập membership lớn, bitset DP, giao/hợp tập và một số tối ưu reachability.

## Sắp xếp và tìm kiếm nhị phân

`Arrays.sort` có overload cho primitive và object với đặc tính triển khai khác nhau. Nếu tính ổn định là một phần của hợp đồng, cần đọc tài liệu của đúng API/JDK thay vì suy ra từ tên phương thức.

`Arrays.binarySearch` trả một vị trí khớp nếu tìm thấy; nếu không, giá trị âm mã hóa insertion point. Nó không phải API lower-bound/upper-bound cho phần tử trùng. Nếu cần lần xuất hiện đầu tiên/cuối cùng, nên tự cài binary search theo bất biến tương ứng.

Tìm kiếm nhị phân còn cần truy cập ngẫu nhiên hiệu quả. Áp dụng nó lên `LinkedList` không tự biến truy cập theo chỉ số thành `O(1)`.

## View, sao chép và bí danh dữ liệu

`subList` thường là view dựa trên list gốc. Thay đổi cấu trúc nền có thể ảnh hưởng hoặc làm view mất hiệu lực theo hợp đồng của API.

Nếu cần snapshot độc lập:

```java
new ArrayList<>(list.subList(l, r))
```

Tương tự, `Collections.unmodifiable*` tạo view không cho sửa qua wrapper nhưng không làm các object bên trong bất biến sâu.

## Iterator fail-fast không phải cơ chế đồng bộ hóa

Nhiều collection cố phát hiện thay đổi cấu trúc trong lúc duyệt và có thể ném `ConcurrentModificationException`. Đây là cơ chế phát hiện lỗi kiểu best-effort, không phải bảo đảm an toàn luồng.

Không dùng exception này như một primitive đồng bộ hóa.

## ConcurrentHashMap

`ConcurrentHashMap` được chọn vì cần ngữ nghĩa truy cập đồng thời, không phải vì nó là “HashMap nhanh hơn”. Các thao tác nhiều bước như “kiểm tra rồi chèn” phải dùng API nguyên tử phù hợp như `putIfAbsent`, `compute` hoặc `merge` nếu muốn tránh race.

## BlockingQueue và backpressure

Trong mô hình producer–consumer, `BlockingQueue` kết hợp cấu trúc queue với ngữ nghĩa đồng bộ hóa. Queue có giới hạn còn biểu diễn **áp lực ngược (backpressure)**: producer có thể phải chờ khi queue đầy.

Đây là ví dụ một cấu trúc dữ liệu chuyển trực tiếp thành cơ chế điều tiết của hệ thống.

## CopyOnWrite collections

Copy-on-write phù hợp với tải đọc rất nhiều và ghi rất hiếm. Mỗi lần ghi phải sao chép vùng lưu trữ, vì vậy tải ghi cao sẽ rất đắt.

“Thread-safe” không đủ để chọn collection; tỷ lệ đọc/ghi và ngữ nghĩa snapshot mới là yếu tố quyết định.

## IdentityHashMap và WeakHashMap

`IdentityHashMap` dùng định danh reference (`==`) thay vì `equals`. Nó phù hợp với một số thuật toán theo dõi object identity, serialization hoặc đồ thị object, nhưng không thay thế HashMap thông thường.

`WeakHashMap` có ngữ nghĩa vòng đời đặc biệt: entry có thể biến mất khi khóa không còn được tham chiếu mạnh. Nó không phải cache eviction policy tổng quát; muốn dùng đúng phải hiểu GC reachability.

## GC không loại bỏ rò rỉ logic

Nếu map, list, listener hoặc cache giữ reference mãi, object vẫn reachable và GC không thể thu hồi. Một memoization cache không giới hạn có thể làm heap tăng liên tục dù không tồn tại lỗi `malloc/free`.

Trong Java, quản lý vòng đời chủ yếu là quản lý reachability.

Một root reference có thể giữ toàn bộ cây hoặc đồ thị sống. Chu trình object tự thân không gây leak với tracing GC nếu toàn bộ chu trình không còn reachable từ roots.

## Độ sâu đệ quy

Java không bảo đảm tối ưu lời gọi đuôi. DFS trên cây lệch hoặc đồ thị dạng đường có thể gây `StackOverflowError`.

Khi độ sâu có thể lớn, dùng `ArrayDeque` làm stack tường minh. Không nên dùng `StackOverflowError` như luồng điều khiển bình thường của thuật toán.

## long, overflow và BigInteger

Khoảng cách đồ thị, prefix sum và số đếm có thể vượt `int`; khi đó dùng `long`. Nhưng `long` vẫn có thể tràn.

```java
static final long INF = Long.MAX_VALUE / 4;
```

Dùng sentinel có khoảng an toàn và chỉ cộng từ trạng thái reachable giúp giảm rủi ro overflow.

Nếu bài toán thực sự cần số nguyên vượt 64 bit, `BigInteger` cung cấp độ chính xác tùy ý nhưng phải trả chi phí object và số học lớn hơn.

## Generic và type erasure

Java generics cung cấp an toàn kiểu ở mức mã nguồn nhưng không nhận primitive làm type argument, vì vậy không có `List<int>`. Đây là một nguyên nhân autoboxing xuất hiện trong collection chuẩn.

Khi profiling chứng minh boxing là nút thắt, có thể dùng mảng primitive hoặc thư viện collection primitive chuyên dụng.

## Cấu trúc DSA tùy biến vẫn thường dùng mảng

Ngay trong Java hướng đối tượng, Segment Tree, heap hoặc DSU thường hiệu quả nhất với mảng primitive:

```java
long[] tree = new long[4 * n];
int[] heap = new int[n];
int[] position = new int[n];
```

Không cần biến mọi nút thành class. Cách biểu diễn phải phục vụ tải công việc chứ không phục vụ thẩm mỹ OOP.

## Streams và độ phức tạp

`stream.sorted()`, `stream.distinct()` hoặc `groupingBy()` vẫn thực hiện công việc thuật toán và xây dựng cấu trúc dữ liệu. Lớp API khai báo không làm chi phí biến mất.

Trong đường chạy nóng, vòng lặp truyền thống thường cho quyền kiểm soát rõ hơn về boxing, cấp phát và dừng sớm. Streams có thể rất dễ đọc ở các phép biến đổi không nhạy về hiệu năng; quyết định nên dựa trên profiling thay vì định kiến.

Parallel streams cũng không tự làm thuật toán mở rộng tuyến tính theo số lõi. Chi phí chia/gộp, tranh chấp và phụ thuộc dữ liệu có thể làm song song hóa không hiệu quả.

## String và Unicode

Java `String` dùng UTF-16; `length()` và `charAt()` làm việc theo code unit, không phải luôn theo Unicode code point hoặc ký tự người dùng nhìn thấy.

Nếu thuật toán cần code point, có thể dùng:

```java
s.codePoints()
```

Nhưng việc chuyển và lưu code point có chi phí riêng. Trước khi viết thuật toán chuỗi, phải xác định đơn vị ký tự của miền bài toán.

`String` là bất biến. Khi xây chuỗi qua nhiều bước, `StringBuilder` thường là bộ đệm thay đổi được phù hợp hơn việc tạo chuỗi trung gian lặp lại.

## Bộ nhớ thực tế và object header

Một object Java còn có header, alignment và reference; số byte chính xác phụ thuộc cấu hình JVM. Vì vậy hàng triệu `Node` có thể lớn hơn nhiều so với tổng kích thước các trường logic.

Các cách biểu diễn phẳng bằng mảng thường giảm đáng kể chi phí này.

JIT có thể loại bỏ một số cấp phát thông qua escape analysis hoặc scalar replacement, nhưng không nên thiết kế dựa trên giả định rằng một tối ưu cụ thể chắc chắn xảy ra.

## JMH và profiling

Microbenchmark Java rất dễ sai do warmup JIT, dead-code elimination và constant folding. JMH cung cấp cơ chế warmup, measurement, fork và blackhole phù hợp hơn một vòng `System.nanoTime()` tự viết.

Các công cụ như JFR, async-profiler, JMC hoặc profiler tương đương giúp quan sát CPU hotspot, allocation hotspot, GC pressure và lock contention.

Tối ưu collection nên dựa trên dữ liệu đo.

## Áp lực GC

Thuật toán đồ thị hoặc PriorityQueue có thể tạo rất nhiều object sống ngắn. GC thường xử lý object ngắn hạn tốt, nhưng tốc độ cấp phát quá cao vẫn có thể ảnh hưởng throughput và tail latency.

Các lựa chọn thay thế gồm mảng primitive hoặc cách biểu diễn gọn hơn. Object pooling không phải lúc nào cũng tốt trong JVM hiện đại; phải đo trước khi áp dụng.

## Immutability và persistent structures

Collection chuẩn của JDK chủ yếu là mutable. Cấu trúc immutable/persistent có thể hữu ích cho snapshot, versioning và chia sẻ trạng thái an toàn hơn.

Persistent tree có thể sao chép chỉ đường cập nhật rồi chia sẻ các nhánh không đổi. Đổi lại, nó tạo thêm object và có mô hình chi phí khác collection mutable.

## Bảng chọn nhanh

| Nhu cầu | Lựa chọn thường phù hợp |
|---|---|
| Truy cập ngẫu nhiên theo chỉ số | `ArrayList` / array |
| Stack, queue, deque | `ArrayDeque` |
| Tra cứu khóa chính xác | `HashMap` / `HashSet` |
| Tra cứu có thứ tự hoặc theo khoảng | `TreeMap` / `TreeSet` |
| Lấy min/max lặp lại | `PriorityQueue` |
| Khóa số nguyên dày đặc | array / `BitSet` |
| Ánh xạ cần truy cập đồng thời | `ConcurrentHashMap` sau khi xác định ngữ nghĩa |
| Producer–consumer có chờ | `BlockingQueue` |

Bảng chỉ là điểm bắt đầu; tải công việc thực tế và profiling mới quyết định cuối cùng.

## Kiểm thử cấu trúc DSA tự cài đặt

Có thể dùng collection JDK làm mô hình tham chiếu:

```text
heap tự cài đặt      -> so chuỗi pop với danh sách đã sắp xếp
BST tự cài đặt       -> so tập/thứ tự với TreeSet hoặc TreeMap
Hash Map tự cài đặt  -> so thao tác ngẫu nhiên với HashMap
```

Ngoài đầu ra, vẫn nên kiểm tra bất biến sau các chuỗi thao tác ngẫu nhiên.

`assert` có thể bị tắt ở runtime, vì vậy kiểm thử tự động nên dùng JUnit hoặc framework property-based testing phù hợp thay vì phụ thuộc ngầm vào Java assertions.

## Những hiểu lầm phổ biến

“Java Collections tự chọn cách triển khai tối ưu” — sai; người gọi vẫn chọn concrete type.

“LinkedList chèn/xóa O(1) nên tốt hơn ArrayList” — thiếu chi phí tìm vị trí, cấp phát và locality.

“ConcurrentHashMap là HashMap nhanh hơn” — sai; nó cung cấp ngữ nghĩa đồng thời và phải trả chi phí phối hợp.

“Thay đổi priority của object trong PriorityQueue thì heap tự cập nhật” — sai.

“Có GC thì không thể rò rỉ bộ nhớ” — sai nếu reference vẫn reachable.

“Streams làm thuật toán nhanh hơn về Big-O” — sai; lớp trừu tượng không thay đổi lượng công việc cơ bản.

“TreeMap xác định khóa trùng giống HashMap” — sai; comparator/natural ordering có ngữ nghĩa khác `equals/hashCode`.

## Mô hình tư duy

> Java Collections là các **hợp đồng DSA được đóng gói trong framework**. Chúng giảm lượng mã phải tự viết nhưng không loại bỏ trách nhiệm chọn đúng cách biểu diễn.

Khi chọn collection, hãy hỏi: **thao tác nào chiếm ưu thế, cần thứ tự hay chỉ membership, khóa có bất biến không, mảng primitive có đủ không, object overhead có đáng kể không, có thật sự cần concurrency không, và view/iterator/reference có thể mất hiệu lực khi nào?**

Xem thêm: [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Cross-language Testing](./03_cross_language_testing_and_benchmarking.md).