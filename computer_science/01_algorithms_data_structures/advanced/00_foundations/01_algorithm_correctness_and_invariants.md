# Tính đúng đắn và bất biến của thuật toán
**Algorithm Correctness & Invariants / 알고리즘 정확성과 불변식**

Một thuật toán nhanh nhưng sai không có giá trị. Test chỉ cho thấy chương trình đúng trên những input đã chạy; nó không tự chứng minh rằng algorithm đúng cho mọi input hợp lệ. Trong DSA, một phần quan trọng của kỹ năng không phải chỉ viết code chạy được, mà là xây được **lập luận về tính đúng đắn (correctness reasoning / 정확성 추론)**: giả định gì trước khi chạy, điều gì luôn đúng trong quá trình chạy, vì sao algorithm tiến tới termination, và tại sao trạng thái cuối buộc phải thỏa yêu cầu.

Correctness không nhất thiết đồng nghĩa với một proof hình thức dài. Trong thực tế, việc xác định đúng invariant thường đủ để biến một đoạn code “khó tin” thành một chuỗi reasoning kiểm tra được.

## Specification: trước khi chứng minh phải biết đang chứng minh điều gì

Một algorithm chỉ có thể được gọi là đúng so với một **specification / 명세** cụ thể. Specification thường gồm input domain, precondition, output semantics và postcondition.

Ví dụ binary search có precondition quan trọng: array được sorted theo comparator mà algorithm sử dụng. Postcondition có thể là: nếu target tồn tại thì trả một index chứa target; nếu không tồn tại thì trả `-1`. Nếu API muốn “first occurrence”, postcondition phải mạnh hơn và algorithm cũng khác.

Điều này cho thấy một lỗi phổ biến: cùng tên “binary search” nhưng specification khác nhau có thể yêu cầu invariant khác nhau.

## Precondition và postcondition

**Điều kiện trước (Precondition / 사전 조건)** là điều phải đúng trước khi algorithm bắt đầu. **Điều kiện sau (Postcondition / 사후 조건)** là điều algorithm cam kết khi kết thúc bình thường.

Ví dụ `merge(left, right)` có precondition rằng hai input ranges đã sorted. Postcondition là output chứa đúng multiset phần tử của hai inputs và sorted theo comparator. Nếu input chưa sorted, function không “chậm hơn”; cơ sở correctness của merge bị phá.

Trong production API, precondition cần được quyết định rõ: validate và reject invalid input, dùng assertion cho programmer error, hay xem invalid input là undefined behavior. Cách xử lý phụ thuộc layer của system.

## Partial correctness và termination

Một distinction hữu ích là **partial correctness** và **total correctness**.

Partial correctness nói: nếu algorithm kết thúc, result đúng. Total correctness thêm yêu cầu algorithm thật sự phải kết thúc với mọi input hợp lệ.

Ví dụ một loop có thể duy trì invariant đúng nhưng không bao giờ giảm search space vì update boundary sai; nó partial-correct theo một reasoning hời hợt nhưng không total-correct. Vì vậy proof loop thường cần hai phần: invariant + **variant/ranking function** tiến đơn điệu về termination.

Binary search chẳng hạn có candidate interval length `hi - lo + 1`. Mỗi iteration không return phải giảm interval này, nên loop không thể chạy vô hạn.

## Loop invariant: cách biến vòng lặp thành proof có cấu trúc

**Bất biến vòng lặp (Loop Invariant / 루프 불변식)** là một mệnh đề đúng tại một điểm xác định của mọi iteration.

Một proof loop thường có ba bước:

```text
Initialization: invariant đúng trước iteration đầu tiên.
Maintenance: nếu invariant đúng trước iteration, body giữ nó đúng cho iteration kế.
Termination: khi loop dừng, invariant + điều kiện dừng suy ra postcondition.
```

Với binary search trên `[lo, hi]`, invariant có thể là:

> Nếu target tồn tại trong array, mọi vị trí còn khả năng chứa target nằm trong `[lo, hi]`.

Nếu `a[mid] < target`, sorted order chứng minh mọi index `<= mid` không thể là answer; cập nhật `lo = mid + 1` giữ invariant. Khi `lo > hi`, candidate set rỗng, nên target không tồn tại.

```c
int binary_search(const int *a, int n, int target) {
    int lo = 0, hi = n - 1;

    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;

        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }

    return -1;
}
```

## Invariant không phải comment mô tả code

Một statement kiểu “array đang được xử lý” không phải invariant hữu ích. Invariant tốt phải đủ mạnh để chứng minh postcondition và đủ đơn giản để chứng minh maintenance.

Ví dụ insertion sort có invariant mạnh:

> Trước iteration `i`, prefix `a[0..i)` đã sorted và chứa đúng multiset phần tử ban đầu của prefix đó.

Chỉ nói “prefix sorted” chưa đủ để chứng minh algorithm không làm mất/nhân đôi phần tử. Correctness thường cần cả order property và conservation property.

## Conservation invariant: dữ liệu không được tự biến mất

Nhiều algorithms mutate structure, vì vậy ngoài order/shape invariant còn cần một invariant về membership hoặc quantity.

Sorting cần output là permutation của input. Heap operation cần giữ cùng set entries trừ phần tử được insert/delete. Graph traversal cần mỗi discovered state correspond đúng một reachable state. Memory allocator cần tổng các blocks free/allocated khớp arena state.

Đây là lý do validator tốt thường kiểm tra nhiều dimensions thay vì một property duy nhất.

## Recursion và structural induction

Recursive algorithm tự nhiên được chứng minh bằng **quy nạp (Induction / 수학적 귀납법)**.

Với merge sort:

**Base case:** array length 0 hoặc 1 đã sorted.

**Inductive hypothesis:** recursive calls sort đúng các subarrays nhỏ hơn.

**Inductive step:** nếu hai halves sorted đúng và `merge` tạo một sorted permutation của hai halves, toàn array sorted đúng.

Tree algorithm còn tự nhiên hơn vì tree được định nghĩa đệ quy. Nếu một function tính subtree size:

\[
size(u)=1+size(left(u))+size(right(u))
\]

correctness đến từ structural induction: null/leaf đúng ở base, rồi combine đúng ở parent nếu children đúng.

## Recursive contract phải đủ rõ

Một cách debug recursion tốt là viết contract cho function thay vì mô phỏng toàn call tree.

Ví dụ:

```text
solve(state) trả optimum achievable từ chính state này trở đi,
không thay đổi global state ngoài vùng được contract cho phép.
```

Sau đó recursive caller được quyền tin contract của subcall. Đây là cách induction xuất hiện trong engineering practice.

## Strong induction

Có những recurrence phụ thuộc nhiều kích thước nhỏ hơn chứ không chỉ `n-1`. Khi đó **strong induction / 강한 귀납법** tự nhiên hơn: giả sử statement đúng cho mọi size nhỏ hơn `n`, rồi chứng minh cho `n`.

Dynamic Programming proofs thường có dạng này vì state hiện tại có thể phụ thuộc nhiều predecessor states.

## Exchange argument trong greedy algorithms

Greedy algorithm khóa local choice và không quay lại. Vì vậy proof cần chứng minh choice đó **safe**.

Một pattern phổ biến là exchange argument: lấy một optimal solution `O` chưa dùng greedy choice `g`, rồi chỉ ra có thể thay một phần của `O` bằng `g` mà không làm objective tệ hơn và không phá feasibility. Khi đó tồn tại optimal solution chứa `g`; ta recurse trên phần còn lại.

Interval scheduling là ví dụ điển hình. Chọn interval finish sớm nhất để lại nhiều timeline nhất cho future. Nếu một optimal solution bắt đầu bằng interval finish muộn hơn, thay interval đầu bằng greedy interval vẫn không làm mất các intervals phía sau.

Greedy correctness nằm ở argument này, không nằm ở trực giác “chọn cái tốt nhất trước”.

## Cut property và safe edge

Một số graph algorithms dùng proof dạng cut. Trong MST, nếu một edge nhẹ nhất crossing một cut phù hợp, cut property chứng minh edge đó là safe cho một MST. Kruskal và Prim khác cách sinh cut/frontier nhưng cùng dựa trên structural fact này.

Proof pattern quan trọng hơn việc nhớ tên theorem: xác định boundary giữa “đã quyết định” và “chưa quyết định”, rồi chứng minh một local choice crossing boundary không thể làm mất global optimum.

## Contradiction: giả sử điều sai xảy ra

**Proof by contradiction / 귀류법** hữu ích khi algorithm finalizes một choice.

Dijkstra là ví dụ. Với non-negative edges, khi vertex `u` có tentative distance nhỏ nhất được lấy ra, giả sử tồn tại một path ngắn hơn chưa biết tới `u`. Trên path đó phải có transition từ finalized region sang unfinalized region; non-negative weights dẫn tới một candidate distance không thể lớn hơn `dist[u]`, mâu thuẫn với việc `u` là minimum candidate chưa xử lý.

Loại proof này giúp hiểu chính xác vì sao negative edges phá Dijkstra.

## Proof bằng extremal/counterexample reasoning

Khi nghi một rule greedy sai, cách mạnh là tìm **smallest counterexample**. Ví dụ coin system `[1,3,4]`, amount `6`: greedy chọn `4+1+1`, trong khi optimum `3+3`.

Counterexample không chỉ dùng để bác bỏ theorem; nó giúp xác định assumption còn thiếu. Trong trường hợp này, canonical coin structure không đúng cho mọi coin systems.

Một workflow thực tế là brute-force small inputs để tìm counterexample cho conjecture trước khi đầu tư vào proof dài.

## Correctness của binary-search-on-answer

Binary search on answer có hai proof layers.

Thứ nhất, phải chứng minh predicate `P(x)` monotonic, ví dụ:

```text
F F F F T T T
```

Thứ hai, phải chứng minh boundary invariant của implementation để tìm first true hoặc last false.

Nếu predicate không thật sự monotonic, binary search có thể chạy hoàn hảo nhưng trả answer vô nghĩa. Vì vậy proof algorithm phụ thuộc proof của model/predicate.

## Correctness của graph traversal

BFS shortest-path proof dựa trên layer invariant: trước khi dequeue một node ở distance `d+1`, mọi node reachable trong `<=d` edges đã được discovered. Lần đầu discover node vì thế cho shortest unweighted distance.

DFS không có shortest-layer property nhưng có stack/nesting property. Discovery/finish intervals giúp reasoning về ancestor relations, cycle detection, SCC và articulation structures.

“BFS và DFS đều visit mọi node” là đúng nhưng chưa đủ; correctness của application phụ thuộc frontier-order property riêng của từng traversal.

## Correctness của data-structure operations

Không chỉ algorithms một-shot mới cần proof. Data structure là sequence operations, nên mỗi operation phải **preserve representation invariant**.

Heap insertion proof:

1. append ở cuối giữ complete-tree shape;
2. chỉ heap-order trên ancestor path có thể bị phá;
3. sift-up sửa mỗi local violation;
4. khi dừng, toàn tree lại thỏa heap invariant.

AVL rotation proof cần đồng thời giữ BST inorder order và cập nhật balance/height metadata. Augmented tree còn phải giữ subtree summaries. Một structure càng nhiều metadata thì số invariants phải bảo vệ càng nhiều.

## Representation invariant và abstraction function

Một cách nhìn từ software verification là tách:

**Representation invariant**: internal bytes/nodes/pointers phải có shape hợp lệ.

**Abstraction function**: internal representation tương ứng abstract value nào.

Ví dụ hash set internal table có tombstones, spare slots và buckets, nhưng abstract value chỉ là tập keys đang present. Correctness của `contains(k)` được chứng minh từ probe invariant và mapping giữa internal slots với abstract set.

Mental model này rất hữu ích khi implementation phức tạp hơn ADT nhiều.

## Assertions như executable invariants

Invariant có thể chuyển thành checks trong debug/test builds:

```java
assert size >= 0 && size <= capacity;
```

```c
assert(heap_is_valid(h));
```

```js
if (debug && !isSorted(run)) throw new Error('run invariant broken');
```

Assertions không thay validation cho untrusted input. Chúng dùng để phát hiện programmer assumptions bị phá càng gần source càng tốt.

## Validator cho data structure

Với structures phức tạp, viết `validate()` thường đáng giá.

BST validator kiểm tra global key bounds chứ không chỉ parent-child comparisons. Red-Black Tree validator kiểm tra color constraints và black height. Heap validator kiểm tra parent/children order. Hash table validator kiểm tra slot states/counts. DSU validator có thể kiểm tra parent indices và size metadata ở roots.

Sau mỗi random mutation trong test, gọi validator giúp bắt bug structural sớm.

## Differential testing và oracle nhỏ

Khi proof implementation khó, có thể dùng một implementation chậm nhưng rõ ràng làm **oracle** trên small input.

Ví dụ test range structure bằng cách so kết quả với brute-force scan. Test shortest path bằng Floyd-Warshall trên graph nhỏ. Test Top-K bằng full sort. Test randomized structure bằng một `TreeMap`/sorted list reference model.

Differential testing không thay proof algorithmic, nhưng rất mạnh để kiểm tra code thực thi proof đó.

## Property-based testing

Thay vì viết vài examples cố định, generate nhiều operation sequences và kiểm tra properties:

```text
insert rồi contains phải true
sort output phải ordered và cùng multiset input
union(a,b) khiến find(a)==find(b)
heap poll sequence phải nondecreasing
```

Đây là cách biến specification thành test generator.

## Fuzzing và adversarial cases

Random input tốt nhưng không đủ. Nên thêm boundary/adversarial cases: empty, single element, duplicates, already sorted, reverse sorted, all equal, deep chain, maximum values, overflow boundaries, negative values, disconnected graph, parallel edges, self-loops.

Một proof đúng dưới preconditions rõ ràng sẽ giúp biết adversarial case nào hợp lệ và case nào phải reject.

## Integer overflow cũng là correctness

Một recurrence có thể đúng toán học nhưng implementation sai vì finite-width arithmetic.

Ví dụ:

```java
long candidate = dist[u] + weight;
```

nếu `dist[u]` dùng sentinel gần `Long.MAX_VALUE`, addition có thể overflow. C signed overflow còn có undefined-behavior implications. JavaScript `Number` mất integer precision sau `2^53-1`.

Correctness proof của code phải sử dụng arithmetic model thực tế, không chỉ integer toán học vô hạn.

## Floating-point correctness

Các thuật toán numeric hoặc geometry cần cẩn thận vì equality/ordering trên floating point có rounding. Predicate tưởng monotonic trên real numbers có thể noisy ở machine representation. Comparator không nhất quán vì epsilon tùy tiện có thể phá sorting/tree contracts.

Khi DSA dùng floating values làm keys hoặc boundaries, numeric semantics là một phần của specification.

## Concurrency: invariant có thể bị phá giữa hai dòng code

Một operation single-thread đúng chưa chắc thread-safe. Ví dụ check-then-act:

```text
if key absent:
    insert key
```

có thể race giữa hai threads. Concurrent correctness thường dùng concept **linearizability / 선형화 가능성**: mỗi operation phải trông như xảy ra atomically tại một điểm giữa invocation và response.

Lock-free structures còn cần memory-ordering và reclamation reasoning. Đây là lớp correctness vượt khỏi DSA cơ bản nhưng cùng nguyên lý: xác định invariant và chứng minh mọi interleaving hợp lệ giữ nó.

## Proof sketch nên đi cùng code review

Trong code review của algorithm phức tạp, một proof sketch ngắn thường có giá trị hơn comment mô tả từng dòng.

Ví dụ:

```text
Invariant: deque chứa các candidate indices còn trong window,
values giảm dần từ front tới back.
Khi thêm index i, pop back mọi value <= a[i] vì chúng không bao giờ
có thể thắng i ở future window. Pop front nếu index expired.
Front luôn là max hiện tại.
```

Đoạn reasoning này giải thích *tại sao* code monotonic deque đúng và giúp reviewer nhận ra mutation nào phá invariant.

## Common misconceptions

“Pass tất cả sample tests” không phải proof.

“Invariant đúng lúc kết thúc” chưa đủ; phải đúng sau initialization và được maintenance ở mọi iteration.

“Recursion có base case” chưa chứng minh termination nếu recursive arguments không tiến gần base case.

“Greedy có vẻ hợp lý” không phải exchange proof.

“Data structure vẫn trả đúng vài queries” không chứng minh metadata/invariant chưa âm thầm hỏng.

## Mental Model

> Correctness là chuỗi lập luận: specification nói ta phải đạt gì; precondition nói ta được giả định gì; invariant nói điều gì luôn được bảo vệ; progress argument nói vì sao algorithm sẽ kết thúc; termination state + invariant suy ra postcondition.

Khi một algorithm khó hiểu, đừng đọc code line-by-line trước. Hãy hỏi: **candidate set hiện tại là gì, invariant nào đang giữ, mỗi mutation loại bỏ hoặc bảo toàn điều gì, và tại sao khi dừng không còn trường hợp nào chưa xét?**

Xem tiếp: [Problem Modeling](./00_dsa_as_problem_modeling.md), [Complexity Analysis](./02_complexity_analysis.md), [Mathematical Toolkit](./04_mathematical_toolkit_for_dsa.md), [Greedy Algorithms](../04_algorithmic_paradigms/04_greedy_algorithms.md) và [Problem Solving Workflow](../90_connections/02_problem_solving_workflow.md).
