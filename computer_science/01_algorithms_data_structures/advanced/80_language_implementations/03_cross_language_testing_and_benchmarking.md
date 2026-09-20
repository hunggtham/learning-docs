# Testing và Benchmarking DSA trên C, Java, JavaScript
**Data Structure & Algorithm Testing / 자료구조·알고리즘 테스트와 벤치마킹**

Một implementation DSA đáng tin cậy cần trả lời ba câu hỏi khác nhau:

```text
Algorithm có đúng về mặt lý thuyết không?
Implementation có bug không?
Chi phí thực tế trên runtime/hardware có đúng với kỳ vọng không?
```

**Proof**, **testing** và **benchmarking** giải ba lớp vấn đề khác nhau. Proof cho correctness/growth model. Test cố tìm counterexample của code thật. Benchmark đo latency, throughput, memory và scaling trong môi trường cụ thể. Trộn ba mục tiêu này thường dẫn tới kết luận sai: benchmark không chứng minh correctness, và vài unit tests không chứng minh Big-O.

## 1. Specification trước Test

Trước khi viết test, phải xác định contract:

```text
input hợp lệ là gì?
output chính xác là gì?
mutation có được phép không?
ordering/tie-breaking thế nào?
error behavior ra sao?
complexity expectation nào là requirement?
```

Ví dụ `topK(items, k)` có thể trả unordered set, stable sorted list hoặc arbitrary tie order. Nếu specification mơ hồ, test “fail” có thể chỉ là hai bên hiểu contract khác nhau.

## 2. Test public behavior và internal invariant là hai lớp khác nhau

Queue phải FIFO dù implement bằng linked list hay ring buffer. Public behavior tests nên không phụ thuộc representation.

Custom heap/tree/hash table còn cần invariant tests:

```text
heap parent <= children
BST inorder sorted
AVL/RB balance/color properties
hash-table size == occupied count
DSU parent forest valid
segment-tree parent aggregate = combine(children)
```

Behavior tests bảo vệ abstraction; invariant tests bắt corruption sớm hơn.

## 3. Assertions như executable specification

Trong debug/test build, structure có thể có:

```java
assert size >= 0 && size <= capacity;
```

hoặc validator:

```text
validateHeap()
validateBST()
validateFreeList()
```

Assertions không thay input validation ở public boundary. Chúng dùng để phát hiện **programmer assumption** bị phá.

Một invariant scan `O(n)` sau mỗi mutation là quá đắt cho production nhưng hoàn toàn hợp lý trong randomized tests.

## 4. Unit Tests: deterministic edge cases

Unit tests nên cover smallest boundaries trước:

```text
empty
one element
two elements
full capacity
first resize
last removal
duplicate keys
negative/large values
max/min index
```

Bugs DSA thường nằm ở transitions:

```text
empty -> one
one -> empty
capacity -> capacity+1
root rotation
head/tail removal
component merge
```

Đừng chỉ test “normal middle state”.

## 5. Differential Testing

Chạy implementation đang test và một reference implementation đơn giản trên cùng input.

Examples:

```text
custom heap       vs sorted array
segment tree      vs raw loop
Dijkstra          vs Floyd-Warshall trên graph nhỏ
Kruskal           vs Prim
custom hash set   vs linear/sorted reference
Quickselect       vs full sort
```

Oracle không cần nhanh. Input nhỏ + oracle đơn giản thường đáng tin hơn một optimized oracle phức tạp.

## 6. Property-Based Testing

Thay vì hard-code output, test properties phải luôn đúng.

Sort:

```text
output nondecreasing
multiset(output) == multiset(input)
```

MST:

```text
V-1 edges
connected
acyclic
cost == reference cost
```

Lower bound:

```text
all indices < answer violate predicate
answer/after satisfy predicate
```

Data structure:

```text
sequence public operations equivalent reference model
```

Properties gần mathematical specification hơn example tests.

## 7. Metamorphic Testing

Khi khó có oracle, biến đổi input theo relation đã biết.

Ví dụ:

```text
rename graph vertices -> mapped result tương đương
add constant c vào mọi sort key -> order không đổi
add isolated graph vertex -> old pair distances không đổi
permute input of a set algorithm -> set output không đổi
scale all positive MST weights by c -> chosen MST edge ordering structurally tương ứng nếu ties không đổi
```

Metamorphic tests rất hữu ích cho graph, optimization và randomized algorithms.

## 8. Model-Based Testing cho mutable structures

Tạo một simple model state và random operation sequence:

```text
insert
remove
contains
peek
update
```

Sau mỗi operation:

```text
compare return value
compare logical contents
validate invariants
```

Ví dụ custom deque so với standard library list/deque. Model-based testing đặc biệt mạnh cho data structure bug chỉ xuất hiện sau sequence dài.

## 9. Stateful fuzzing

Fuzzer không chỉ sinh input một lần, mà sinh sequence operations phụ thuộc state:

```text
push 5
push 2
pop
push 9
remove index 0
...
```

Nó có thể tìm bug resize, stale pointer, metadata drift hoặc deletion corner case mà unit tests độc lập không thấy.

Log seed + operation trace để reproduce.

## 10. Shrinking/minimization

Một random sequence 100.000 operations fail không hữu ích bằng 7 operations tối thiểu gây bug.

Shrinking cố loại operations/giảm values mà failure vẫn giữ. Property-testing frameworks có support; nếu tự viết, có thể dùng delta-debugging style:

```text
thử bỏ nửa trace
nếu vẫn fail -> giữ phiên bản nhỏ hơn
lặp
```

Minimal counterexample thường làm invariant bug trở nên hiển nhiên.

## 11. Random generator phải biết failure modes

Uniform random numbers chưa đủ.

Sorting:

```text
sorted
reverse
nearly sorted
all equal
duplicate-heavy
organ-pipe patterns
```

Hash table:

```text
collision-heavy patterns
insert/delete churn
load-factor thresholds
resize boundaries
```

Graph:

```text
path
star
cycle
DAG
clique
disconnected
parallel edges
self-loops
```

Generator tốt sinh **structured adversarial cases**, không chỉ noise.

## 12. Deterministic seeds

Mọi randomized test/algorithm benchmark nên có seed configurable. Failure report cần:

```text
seed
input size
parameters
runtime/version
operation trace hoặc generated case
```

Không reproduce được failure nghĩa là debugging cost tăng rất mạnh.

## 13. Test randomized algorithms mà không làm test flaky

Không nên assert “Quickselect luôn dùng < X comparisons” cho một random run. Thay vào đó:

```text
assert correctness cho mọi run
fix seed cho regression case
statistical test performance/probability riêng nếu cần
```

Probabilistic structures cần statistical validation trên nhiều trials với tolerance/confidence, không assert exact false-positive rate trên một small sample.

## 14. Test probabilistic data structures

Bloom Filter:

```text
no false negative cho inserted items theo standard model
false-positive rate nằm gần expected trên sufficiently large independent sample
```

HyperLogLog:

```text
relative error distribution qua nhiều random datasets
merge result tương thích single-pass result trong tolerance
```

Count-Min Sketch:

```text
estimate >= true count trong non-negative model
error statistics phù hợp parameterization
```

Test statistical guarantee khác test deterministic equality.

## 15. Mutation testing

Một cách đánh giá chất lượng test suite là cố tình inject bug nhỏ:

```text
< thành <=
quên size--
đảo comparator
skip low update
sai boundary +1
```

Nếu tests vẫn pass, suite đang thiếu sensitivity ở behavior đó.

Mutation testing không phải DSA-specific nhưng cực hữu ích vì nhiều bugs là one-line invariant violations.

## 16. Benchmark khác Test ở mục tiêu

Test hỏi đúng/sai. Benchmark hỏi cost.

Benchmark hot path không nên chạy validator nặng bên trong timing loop. Setup/input generation cần tách ra nếu không thuộc workload cần đo.

Ví dụ benchmark `HashMap.get` thì populate map trước timing, trừ khi question thật sự là build+lookup pipeline.

## 17. Benchmark nhiều scale, không một `n`

Đo `n` theo geometric progression:

```text
1K, 2K, 4K, 8K, ...
```

Quan sát ratio:

```text
n doubled, time ~2x -> linear signal
~4x                  -> quadratic signal
slightly >2x         -> n log n / memory effects
```

Đây không phải proof Big-O, nhưng giúp phát hiện accidental complexity regression.

## 18. Input shape là một benchmark dimension

Quicksort performance phụ thuộc pivot/input. Hash table phụ thuộc key distribution. Graph algorithm phụ thuộc density. DP phụ thuộc reachable-state density.

Benchmark table nên có dimensions:

```text
size
shape/distribution
operation mix
read/write ratio
warm/cold cache
```

Một single random-uniform dataset không đại diện mọi workload.

## 19. Throughput vs Latency

Throughput:

```text
operations/second
```

Latency:

```text
time per operation/request
```

Batch algorithm có throughput tốt nhưng p99 latency xấu do occasional resize/GC. Amortized `O(1)` không bảo đảm per-operation constant latency.

Production benchmark nên đo distribution:

```text
p50
p95
p99
max
```

nếu tail quan trọng.

## 20. Warm vs Cold Cache

Benchmark array scan lặp lại cùng buffer có thể đo warm-cache performance, khác first-pass/cold-cache workload.

Search index production có dataset lớn hơn LLC, nên microbenchmark fit-cache có thể misleading.

Cần biết câu hỏi:

```text
steady hot loop?
first access?
working set > cache?
```

## 21. C: compiler optimization

Benchmark C ở `-O0` không đại diện production optimized build. Cần record flags, compiler version và target architecture.

Compiler có thể loại computation nếu result không observable. Benchmark phải consume result hoặc dùng harness phù hợp.

Undefined behavior làm mọi performance conclusion vô nghĩa: optimizer được phép giả định UB không xảy ra.

## 22. C: allocator là một phần workload

Linked structure `malloc` mỗi node đang benchmark cả allocator. Điều này đúng nếu production cũng allocate như vậy.

Nếu muốn isolate traversal, preallocate nodes. Nếu muốn compare arena vs malloc, allocation phải nằm trong measured workload.

Không có “benchmark thuần data structure” tách khỏi representation nếu allocation chính là phần implementation.

## 23. C: sanitizers và benchmark tách riêng

AddressSanitizer/UBSan rất tốt cho correctness nhưng tăng overhead mạnh. Không dùng sanitized build để kết luận production performance.

Quy trình:

```text
sanitized tests/fuzzing
optimized benchmark build riêng
```

Correctness trước, performance sau.

## 24. Java: JIT warm-up

Java code có tiered compilation/JIT. Run đầu đo startup/interpreter/compilation nhiều hơn steady-state.

Framework như JMH xử lý:

```text
warmup iterations
measurement iterations
forks
blackholes
state scopes
```

Tự viết `System.nanoTime()` loop rất dễ dính dead-code elimination, constant folding hoặc insufficient warmup.

## 25. Java: GC và allocation rate

Hai algorithms cùng latency trung bình có thể khác allocation rate. High allocation làm GC hoạt động nhiều và tail latency thay đổi.

Đo:

```text
bytes/op
allocations/op
GC count/time
peak/live heap
```

nếu structure object-heavy.

Primitive arrays vs boxed objects là một khác biệt lớn trong DSA benchmark Java.

## 26. Java: escape analysis và scalar replacement

JIT có thể eliminate allocation ngắn-lived nếu object không escape. Microbenchmark artificial có thể được optimize khác production nơi object escape qua collection/API.

Benchmark cần mimic lifecycle thật; không nên suy từ toy microbenchmark sang full service quá xa.

## 27. JavaScript: JIT tiering và shapes

JavaScript engine tối ưu dựa runtime feedback. Mixed types, changing object shapes, sparse arrays hoặc polymorphic access có thể deoptimize hot code.

Benchmark nên giữ data shape realistic. Một benchmark chỉ numbers packed array không đại diện workload thực tế có mixed objects.

## 28. JavaScript: event loop và async noise

Nếu đo pure DSA trong Node/browser, tách network/file timers/GC scheduling càng nhiều càng tốt.

`async` không làm algorithm CPU-bound nhanh hơn; nó thay scheduling. Benchmark algorithm nên tránh trộn event-loop waiting trừ khi đó chính là workload.

## 29. JavaScript: `performance.now`/timing granularity

Operation quá nhanh cần batch nhiều iterations để vượt timer resolution/noise. Nhưng batching quá nhiều có thể thay JIT/GC regime.

Nên đo nhiều repetitions, discard warm-up và xem distribution thay vì một run.

## 30. Cross-language benchmark: định nghĩa câu hỏi trước

So C/Java/JS có thể mang hai mục tiêu khác:

**Algorithmic comparison**: nên giữ cùng language/runtime để giảm nhiễu.

**Production stack comparison**: runtime overhead, GC/JIT chính là một phần answer.

Không nên từ một microbenchmark conclude “language X nhanh hơn language Y nói chung”. Kết luận hợp lệ phải gắn với:

```text
workload
implementation
runtime version
hardware
compiler flags
memory limits
```

## 31. Fairness không đồng nghĩa code giống hệt

Một implementation idiomatic Java dùng `int[]`, JavaScript dùng TypedArray, C dùng flat array có thể công bằng hơn ép cả ba dùng object-heavy structure giống syntax.

Câu hỏi là compare **best reasonable implementation cùng semantics**, hay compare **same high-level structure**? Hai nghiên cứu khác nhau.

Benchmark report phải nói rõ.

## 32. Correctness parity trước performance parity

Trước cross-language timing, cần verify outputs equivalent. Nếu C uses 64-bit integer còn JS Number mất precision, hai implementation không còn cùng problem semantics.

Nếu Java comparator stable tie rule khác JS version, output contract khác.

Đừng benchmark hai programs giải hơi khác problem rồi gọi đó là language comparison.

## 33. Numeric semantics

C signed overflow có UB trong nhiều trường hợp. Java integer overflow wrap theo two's complement semantics. JavaScript Number là IEEE-754 double với safe integer limit.

Algorithm count/path sum phải dùng representation tương đương hoặc document semantic differences.

BigInt JavaScript làm arithmetic cost khác Number; Java `BigInteger` cũng khác primitive long.

## 34. Memory footprint cross-language

Một node có:

```text
C: struct fields + allocator metadata/alignment
Java: object header + references + GC metadata effects
JS: engine object shape/property storage
```

So “1 million nodes” chỉ bằng logical count không đủ. Đo resident/live memory thực tế.

Arrays/TypedArrays/primitive arrays thường cho cross-language footprint gần nhau hơn object graph.

## 35. CPU profiling

Khi benchmark bất ngờ, profiler giúp phân biệt:

```text
algorithm work
comparator
allocation
GC
hash function
cache misses
runtime helper
```

Tối ưu không có profile thường dễ tập trung sai chỗ.

## 36. Hardware counters

Trong native/perf-oriented environment, counters như:

```text
cycles
instructions
cache misses
branch misses
```

có thể giải thích vì sao hai `O(n)` implementation khác nhau.

Array vs linked list là ví dụ: instruction count và cache miss profile thường khác mạnh.

## 37. Memory benchmark

Space `O(n)` chưa đủ. Constants matter.

Đo:

```text
peak RSS
live heap
allocation rate
bytes per element
spare capacity
fragmentation
```

Hash table có spare buckets; tree có pointer/object overhead; graph adjacency objects có thể tốn nhiều hơn CSR arrays.

## 38. End-to-end benchmark

Microbenchmark heap `poll()` nhanh hơn 20% chưa chắc cải thiện service nếu heap chỉ chiếm 1% request time.

Architecture decision cần end-to-end benchmark gần production:

```text
serialization
database/network
allocation
algorithm
caching
contention
```

Profile trước khi tối ưu.

## 39. Concurrency benchmark

Sequential cost không dự đoán concurrent throughput.

Cần vary:

```text
thread count
read/write ratio
key contention
NUMA/core placement
critical section size
```

Concurrent map có thể scale tốt với dispersed keys nhưng collapse khi mọi threads update cùng key/cache line.

Report throughput vs threads, không chỉ “8-thread result”.

## 40. False sharing và cache-line contention

Hai counters logic khác nhau nhưng cùng cache line có thể làm threads ping-pong cache ownership.

Benchmark concurrent arrays/queues nên cân nhắc padding/alignment nếu result bất thường.

Đây là hardware effect nằm ngoài sequential Big-O nhưng rất thật.

## 41. Benchmark statistical hygiene

Đừng chỉ lấy một average. Nên có:

```text
multiple forks/processes
many samples
median/percentiles
confidence interval nếu cần
outlier explanation
```

OS scheduler, thermal throttling, background tasks, CPU frequency scaling tạo noise.

Không cần biến mọi benchmark thành nghiên cứu khoa học, nhưng phải đủ discipline để không tự lừa mình.

## 42. Regression Benchmark

Benchmark hữu ích nhất khi chạy lặp qua commits/releases với threshold hợp lý.

Ví dụ:

```text
heap push throughput không giảm >10%
peak memory graph parser không tăng >15%
```

Nhưng threshold cần allowance cho noise. Microbenchmark quá flaky làm CI mất giá trị.

## 43. Complexity regression tests

Có thể tạo performance test theo scale ratio hơn là absolute milliseconds.

Ví dụ algorithm expected near linear:

```text
time(2n) / time(n)
```

không nên liên tục gần 4 trên large stable regime.

Đây không proof complexity, nhưng bắt accidental nested loop hoặc hidden copy regression.

## 44. Benchmark adversarial inputs

Ngoài average workload, test cases xấu:

```text
hash collision attack
quicksort pathological ordering
very deep tree/graph
huge duplicates
max capacity resize
```

Nếu API public hoặc latency-sensitive, worst-case behavior có thể là security/reliability concern.

## 45. Reproducible benchmark report

Một result đáng tin nên ghi:

```text
CPU/cores
RAM
OS
compiler/runtime version
flags
GC mode nếu relevant
commit SHA
input generator + seed
warmup/measurement config
```

Không có metadata, result vài tháng sau gần như không audit được.

## 46. Một workflow hoàn chỉnh

**Bước 1 — Specification:** viết contract và assumptions.

**Bước 2 — Proof/Reasoning:** invariant, correctness, complexity.

**Bước 3 — Deterministic Tests:** boundaries và known cases.

**Bước 4 — Differential/Property Tests:** random small cases + oracle.

**Bước 5 — Fuzz/Adversarial:** long operation sequences, malformed shapes.

**Bước 6 — Sanitizers/Runtime checks:** memory/UB ở C, assertions, race tools nếu relevant.

**Bước 7 — Microbenchmark:** isolate primitive operation.

**Bước 8 — Profile:** tìm hotspot thật.

**Bước 9 — End-to-end benchmark:** workload gần production.

**Bước 10 — Regression automation:** giữ performance/correctness qua thay đổi.

## 47. Ví dụ: custom Priority Queue cross-language

Giả sử implement binary heap ở C/Java/JS.

Correctness tests:

```text
random push/pop vs sorted reference
heap invariant after each mutation
duplicates
overflow/tie comparator
```

Benchmark dimensions:

```text
n
push:pop ratio
primitive vs object payload
already ordered/random scores
```

C:

```text
allocator strategy
struct layout
compiler flags
```

Java:

```text
boxing vs primitive custom arrays
JIT warmup
GC allocation
```

JS:

```text
Number vs BigInt
Array vs TypedArray
object tuple allocation
JIT shape stability
```

Đây mới là so sánh có ý nghĩa; chỉ chạy một heap of 1000 items một lần không đủ.

## 48. Common benchmark mistakes

```text
benchmark debug build
đo setup cùng hot operation ngoài ý muốn
không warm up JIT
compiler loại dead code
sample quá ngắn
chỉ một input size
không kiểm tra result correctness
so semantics numeric khác nhau
kết luận từ average duy nhất
microbenchmark rồi suy ra whole application
```

## Mental Model

> **Proof** giải thích vì sao algorithm đúng và growth ra sao. **Testing** cố phá implementation. **Benchmarking** đo cost thật dưới một workload và runtime cụ thể.

Ba lớp này phải nối với nhau nhưng không thay thế nhau. Một DSA implementation tốt là nơi mathematical contract, executable tests và empirical performance đều kể cùng một câu chuyện.

Xem thêm: [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [C Implementation](./00_c_dsa_implementation_patterns.md), [Java Collections](./01_java_collections_and_dsa.md), [JavaScript Runtime](./02_javascript_dsa_runtime_patterns.md).