# Testing và Benchmarking DSA trên C, Java, JavaScript
**Data Structure & Algorithm Testing / 자료구조·알고리즘 테스트와 벤치마킹**

Một implementation DSA không nên được đánh giá chỉ bằng vài example input cho output đúng. Ta cần tách ba câu hỏi khác nhau: **algorithm có đúng về mặt lý thuyết không**, **implementation có bug không**, và **chi phí thực tế trên runtime/hardware có đúng với kỳ vọng không**. Proof, testing và benchmarking trả lời ba câu hỏi này theo ba cách khác nhau.

Proof có thể cho biết một thuật toán đúng với mọi input thỏa assumptions. Test không chứng minh được điều đó, nhưng rất giỏi tìm implementation bug. Benchmark lại không kiểm tra correctness; nó đo latency, throughput, allocation, memory và scaling trong môi trường thực tế.

## 1. Test theo invariant, không chỉ test output cuối

Một cấu trúc dữ liệu có thể bị corrupt từ sớm nhưng chỉ cho output sai sau nhiều operation. Nếu chỉ kiểm tra kết quả cuối, bug rất khó khoanh vùng. Vì vậy nên kiểm tra **invariant / 불변식** sau mỗi mutation quan trọng.

Với min-heap lưu trong array, invariant là với mọi node `i`, giá trị tại parent không lớn hơn children. Sau random sequence của `push`, `pop`, `decreaseKey` hoặc heapify, ta có thể scan toàn heap để xác nhận invariant.

Với BST, inorder traversal phải có thứ tự. Nếu tree có metadata như `size`, `height` hoặc `maxEnd`, metadata phải khớp với structure thật. Balanced tree còn cần balance invariant tương ứng.

Với DSU, mọi node trong cùng component phải có cùng representative. Nếu dùng union-by-rank/size, metadata root phải consistent với partition.

Invariant test thường đắt hơn production operation, nhưng test không cần tối ưu giống production. Mục tiêu là phát hiện corruption càng gần nơi nó xảy ra càng tốt.

## 2. Test abstract behavior tách khỏi representation

Một queue phải đáp ứng FIFO semantics bất kể implement bằng circular buffer hay linked list. Một set phải đảm bảo uniqueness và membership semantics bất kể dùng hash table hay tree.

Do đó test tốt nên có hai lớp. Lớp đầu kiểm tra **public behavior**: sequence operation cho output nào. Lớp thứ hai, nếu implementation custom, kiểm tra **internal invariant**.

Cách tách này rất hữu ích khi refactor representation. Nếu đổi custom queue từ linked list sang ring buffer, behavior tests phải vẫn giữ nguyên; chỉ invariant tests thay đổi.

## 3. Differential testing: dùng implementation đơn giản làm oracle

**Differential testing / 차등 테스트** nghĩa là chạy cùng input trên implementation đang kiểm thử và một implementation tham chiếu đáng tin cậy, rồi so kết quả.

Reference không cần nhanh. Thậm chí càng đơn giản càng tốt vì code đơn giản thường dễ tin hơn.

Custom heap JavaScript có thể được so với array rồi `sort((a,b)=>a-b)` sau mỗi operation trên input nhỏ. Segment Tree có thể so với raw array update và loop range sum. Shortest path implementation có thể so với Floyd–Warshall trên graph nhỏ. Custom hash set C có thể so với sorted array hoặc simple linear scan model.

Điểm mạnh của phương pháp này là ta không cần tự đoán expected output cho hàng nghìn random cases; oracle sinh expected behavior tự động.

## 4. Property-based thinking

Ngoài expected output cụ thể, nhiều thuật toán có **property** phải luôn đúng.

Sort output cần nondecreasing theo comparator và phải giữ nguyên multiset của input. Chỉ kiểm tra sorted là chưa đủ, vì implementation lỗi có thể làm mất hoặc nhân đôi phần tử.

Binary search nếu trả về index phải đảm bảo value tại index thỏa predicate; nếu tìm lower bound, mọi phần tử trước index phải không thỏa và phần tử tại/after boundary phải thỏa theo semantics.

Shortest path distances sau khi kết thúc phải thỏa relaxation condition `dist[v] <= dist[u] + w(u,v)` cho mọi edge reachable trong assumptions phù hợp. Parent chain phải tạo path có cost bằng reported distance.

MST phải có `V-1` edges nếu graph connected, không cycle, và tổng weight có thể đối chiếu giữa Kruskal và Prim trên random graphs nhỏ.

Property tests giúp test specification ở mức toán học thay vì phụ thuộc vài sample cụ thể.

## 5. Metamorphic testing khi không có oracle tốt

Có những bài khó tạo expected output trực tiếp. Khi đó có thể dùng **metamorphic relation**: biến đổi input theo cách mà quan hệ giữa outputs phải biết trước.

Nếu cộng cùng constant `c` vào mọi phần tử rồi sort, relative order theo numeric comparison không đổi. Nếu rename vertex IDs của graph bằng một permutation, shortest-path distance structure phải tương đương sau khi map ngược IDs. Nếu thêm một isolated vertex vào graph, shortest paths giữa các vertex cũ không nên thay đổi.

Metamorphic testing đặc biệt hữu ích cho graph algorithms, randomized algorithms và optimization problems.

## 6. Random generation phải tạo được input “xấu”

Random uniform đơn giản thường không đủ. Một hash-table test cần duplicate-heavy keys, repeated insert/delete, keys có pattern và capacity boundary. Tree test cần ascending input, descending input, duplicate policy và sequences gây nhiều rotations. Graph test cần sparse, dense, disconnected, DAG, cyclic, path-like, star-like và multi-component graphs.

Sorting cần random, sorted, reverse-sorted, nearly sorted, all-equal và duplicate-heavy arrays. Interval algorithms cần equal endpoints và nhiều ties. DP cần smallest state, maximum state và states không reachable.

Một generator tốt phản ánh cấu trúc failure mode chứ không chỉ “sinh số ngẫu nhiên”.

## 7. Reproducibility: seed là một phần của bug report

Random test chỉ hữu ích nếu failure có thể chạy lại. Vì vậy nên log random seed, input size và operation sequence tối thiểu.

Khi một random test fail, mục tiêu tiếp theo là **shrinking**: giảm input xuống case nhỏ nhất vẫn fail. Một sequence 50.000 operations có thể rút còn 7 operations làm lộ bug rotation hoặc stale metadata. Property-testing frameworks tự động làm một phần việc này, nhưng mental model vẫn hữu ích nếu viết test thủ công.

## 8. Benchmark khác test ở mục tiêu

Test hỏi “đúng hay sai?”. Benchmark hỏi “tốn bao nhiêu?”. Vì thế benchmark phải tránh đưa correctness assertions nặng vào hot path đo, nếu không ta đo cả test logic.

Benchmark nên có warm-up, nhiều repetitions, measure distribution thay vì một con số duy nhất, và tách setup khỏi timed region khi setup không thuộc operation cần đo.

Ví dụ muốn benchmark lookup HashMap, đừng tính cả thời gian generate keys và populate map vào mỗi lookup measurement trừ khi workload thực tế đúng là build-and-query cùng lúc.

## 9. Không benchmark chỉ một kích thước n

Một measurement tại `n = 100000` không cho biết growth behavior. Nên đo nhiều `n`, ví dụ tăng theo powers of two, rồi quan sát runtime ratio.

Nếu `n` nhân đôi và runtime gần nhân bốn, có tín hiệu quadratic trong regime đó. Nếu runtime gần nhân đôi, có thể gần linear. Nếu tăng hơi hơn gấp đôi, có thể `n log n` hoặc bị memory effects.

Đây không phải proof complexity. Cache, GC, JIT, branch prediction và allocation có thể làm curve méo. Nhưng growth trend rất hữu ích để phát hiện implementation vô tình biến `O(n)` thành `O(n^2)`.

## 10. C: compiler, allocation và undefined behavior

Benchmark C phụ thuộc mạnh vào compiler flags như optimization level và target architecture. Code debug `-O0` không nên được dùng để kết luận performance production.

Phải ngăn compiler tối ưu bỏ toàn bộ computation nếu result không observable. Allocation strategy cũng phải được kiểm soát: benchmark linked list với `malloc` mỗi node đang đo cả allocator; điều đó có thể đúng nếu production cũng như vậy, nhưng phải biết mình đang đo gì.

Undefined behavior làm mọi benchmark mất ý nghĩa. Out-of-bounds, signed overflow trong trường hợp UB hoặc use-after-free có thể khiến optimizer tạo code bất ngờ. Correctness phải được đảm bảo trước performance.

## 11. Java: JIT, warm-up, GC và boxing

Java code ban đầu chạy qua interpreter/tiered compilation rồi mới đạt optimized JIT state. Microbenchmark chạy một lần rất dễ đo startup thay vì steady-state.

JIT còn có thể dead-code eliminate computation nếu result không được consume đúng cách. Đây là lý do các framework như JMH tồn tại: chúng xử lý warm-up, forks, blackholes và nhiều benchmark trap phổ biến.

GC cũng ảnh hưởng latency. Hai implementations có cùng Big-O nhưng một bên tạo object tạm thời rất nhiều có thể tạo allocation pressure và pause khác biệt. Boxing `int` thành `Integer` trong collections cũng là cost thực tế.

## 12. JavaScript: JIT tiering, hidden representation và event-loop context

JavaScript engine cũng tối ưu code theo runtime feedback. Object shape thay đổi, mixed types hoặc polymorphic access có thể ảnh hưởng optimization. Vì vậy một microbenchmark quá nhỏ hoặc không giống production có thể đánh giá sai.

`Array`, `Map`, object và TypedArray có behavior khác nhau. Ví dụ queue implement bằng `shift()` có thể mang cost khác head-index queue. Nhưng benchmark phải đủ lớn và đúng pattern để thấy difference đáng kể.

Nếu benchmark chạy trong browser hoặc Node.js, cần tách I/O/event-loop effects khỏi pure algorithm timing khi mục tiêu là đo core DSA.

## 13. Cross-language benchmark phải định nghĩa “công bằng”

So C, Java và JavaScript không đơn giản là chạy cùng source logic rồi so milliseconds. Runtime model khác nhau: startup, JIT, GC, integer representation, collection implementation và memory allocator đều khác.

Cần xác định câu hỏi. Nếu hỏi “thuật toán nào scale tốt hơn”, nên so cùng language/runtime để giảm nhiễu. Nếu hỏi “implementation production của workload X trên C/Java/JS có throughput nào”, thì runtime overhead chính là một phần câu trả lời và không nên loại bỏ.

Không nên dùng microbenchmark cross-language để kết luận ngôn ngữ A “nhanh hơn” ngôn ngữ B nói chung. Benchmark chỉ có ý nghĩa trong workload, environment và implementation cụ thể.

## 14. Latency distribution quan trọng hơn average đơn lẻ

Trong system workload, average latency có thể che p95/p99 rất xấu. GC pause, resize hash table hoặc occasional rebalancing có thể tạo tail latency.

Data structure có amortized `O(1)` vẫn có individual operation đắt hơn. Dynamic array resize là ví dụ. Nếu hệ thống real-time nhạy với worst-case latency, amortized complexity chưa chắc đủ; có thể cần incremental resizing hoặc structure có deterministic bound.

## 15. Memory benchmark và peak usage

Một algorithm nhanh nhưng dùng memory vượt limit vẫn thất bại. Nên đo peak memory, allocation rate và resident set khi relevant.

Adjacency matrix và adjacency list cùng biểu diễn graph nhưng memory profile rất khác. Hash table thường giữ spare capacity để giảm collision/load factor. Tree node có pointer/object overhead. Primitive arrays có locality tốt hơn boxed collections.

Space complexity `O(n)` chỉ nói tốc độ tăng trưởng; production cần cả constant factor.

## 16. Benchmark end-to-end khi quyết định architecture

Microbenchmark giúp hiểu primitive operation nhưng không thay thế end-to-end benchmark. Một database-like workflow có thể bottleneck ở serialization, disk hoặc network chứ không phải tree lookup. Tối ưu heap operation 20% không có ý nghĩa nếu nó chỉ chiếm 1% total latency.

Nên profile trước khi tối ưu. Nếu profile cho thấy hotspot ở comparator, allocation hoặc cache misses, lúc đó data structure change mới có evidence.

## 17. Một quy trình test và benchmark thực dụng

Trước hết chứng minh hoặc ít nhất viết rõ invariant/correctness argument. Sau đó xây deterministic unit tests cho boundary cases. Tiếp theo thêm random/differential tests với oracle nhỏ. Khi correctness ổn định, mới benchmark nhiều input shapes và nhiều scales.

Cuối cùng, nếu quyết định dùng structure trong production, benchmark workload gần thực tế và profile memory/allocation. Nếu kết quả khác kỳ vọng Big-O, đừng vội phủ nhận lý thuyết; hãy kiểm tra constants, runtime, representation và benchmark methodology.

## Mental Model

> **Proof** trả lời “vì sao algorithm đúng và tăng trưởng thế nào”. **Tests** cố tìm counterexample trong implementation. **Benchmark** đo chi phí thật của implementation trên workload và runtime cụ thể.

Ba lớp này bổ sung cho nhau. Một DSA implementation đáng tin cậy cần correctness reasoning trước, testing mạnh ở giữa, và performance measurement có phương pháp ở cuối.

Xem thêm: [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [C Implementation Patterns](./00_c_dsa_implementation_patterns.md), [Java Collections & DSA](./01_java_collections_and_dsa.md), [JavaScript Runtime Patterns](./02_javascript_dsa_runtime_patterns.md).