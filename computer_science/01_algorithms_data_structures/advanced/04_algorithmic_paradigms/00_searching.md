# Searching
**Tìm kiếm (Searching / 탐색)**

Searching là quá trình thu hẹp **candidate space / 후보 공간** cho tới khi xác định được target, boundary hoặc chứng minh answer không tồn tại. Điểm phân biệt giữa các search algorithms không phải syntax loop mà là **information nào cho phép loại một vùng candidates**.

Nếu không có structure hỗ trợ, linear scan có thể là optimal practical choice. Nếu dữ liệu sorted, comparison cho phép loại nửa space. Nếu có hash index, identity lookup gần-direct. Nếu state space là graph, BFS/DFS/Dijkstra tổ chức frontier khác nhau. Nếu answer space có monotonic predicate, binary search có thể hoạt động ngay cả khi không tồn tại một array cụ thể.

Mental model quan trọng nhất là:

> Search nhanh khi mỗi observation loại được một vùng candidates lớn mà không bỏ mất answer.

## Linear search và lower bound trực giác

Nếu array không sorted, không có hash/index và ta cần tìm một arbitrary value, worst case có thể phải xem mọi phần tử.

```c
int linear_search(const int *a, int n, int target) {
    for (int i = 0; i < n; ++i) {
        if (a[i] == target) return i;
    }
    return -1;
}
```

Worst-case `O(n)`.

Không nên coi linear search là “thuật toán kém”. Nếu dataset nhỏ, chỉ search một lần hoặc preprocessing/indexing đắt hơn query, linear scan có thể là lựa chọn tốt nhất.

Ví dụ với 20 elements, build hash table rồi lookup một lần thường không có giá trị thực tế.

## Binary search cần monotonic information

Binary search hoạt động vì sorted order tạo một predicate monotonic.

Ví dụ tìm target trong sorted ascending array:

```text
values < target | maybe target | values > target
```

Midpoint comparison cho phép chứng minh một nửa candidates không thể chứa target.

```java
int binarySearch(int[] a, int target) {
    int lo = 0, hi = a.length - 1;

    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;

        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }

    return -1;
}
```

`lo + (hi-lo)/2` tránh overflow mà `(lo+hi)/2` có thể gây trong fixed-width integer domain.

## Loop invariant quan trọng hơn template

Một binary search đúng nên có invariant rõ ràng.

Ví dụ lower-bound dùng half-open interval `[lo, hi)`:

```java
int lowerBound(int[] a, int target) {
    int lo = 0, hi = a.length;

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;

        if (a[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    return lo;
}
```

Invariant có thể viết:

```text
mọi index < lo có value < target
mọi index >= hi có value >= target
answer boundary nằm trong [lo, hi]
```

Khi `lo == hi`, candidate interval co lại thành boundary answer.

Nếu hiểu invariant này, ta không cần học thuộc hàng chục template first/last occurrence khác nhau.

## Lower bound và upper bound

**Lower bound** là vị trí đầu tiên có value `>= target`.

**Upper bound** là vị trí đầu tiên có value `> target`.

Với sorted array, số lần target xuất hiện là:

```text
upperBound(target) - lowerBound(target)
```

Nếu target không tồn tại, lower bound vẫn có ý nghĩa: đó là insertion position để giữ order.

Đây là lý do APIs kiểu `lower_bound` mạnh hơn function chỉ trả `found/not found`.

## First true / last false abstraction

Rất nhiều binary-search problems có thể chuẩn hóa về sequence:

```text
F F F F T T T T
```

Ta tìm:

```text
first T
hoặc last F
```

Trước khi code, viết predicate orientation ra giấy:

```text
P(x) = ?
P có monotonic không?
Ta cần first true hay last true?
```

Đây là cách giảm mạnh off-by-one bugs.

## Binary search on answer

Binary search không cần sorted array. Nó cần **ordered solution space + monotonic feasibility predicate**.

Ví dụ tìm ship capacity nhỏ nhất để vận chuyển packages trong `D` ngày.

```text
P(C) = có thể ship trong <= D ngày với capacity C không?
```

Nếu capacity `C` khả thi thì mọi capacity lớn hơn cũng khả thi:

```text
F F F T T T
```

Ta tìm first true.

Complexity:

```text
O(cost(P) * log(answer range))
```

Điểm quan trọng là feasibility check phải đủ nhanh và monotonic thật sự.

## Cách chứng minh predicate monotonic

Đừng chỉ nhìn problem và “cảm giác binary search được”. Hãy chứng minh:

```text
P(x) true -> P(y) true với mọi y >= x
```

hoặc orientation ngược lại.

Ví dụ minimum capacity, more capacity không thể làm schedule khó hơn nên monotonic.

Nhưng nếu parameter ảnh hưởng objective theo non-monotonic way, binary search sẽ sai dù code template hoàn hảo.

## Search trên integer answer range

Giả sử answer thuộc `[L, R]` inclusive và tìm minimum feasible.

Một robust half-open formulation là search `[L, R+1)` với upper sentinel chắc chắn feasible, hoặc dùng inclusive bounds cẩn thận.

Nếu `R+1` có overflow risk, cần representation khác.

Trong production code, boundary domain quan trọng không kém algorithm idea.

## Binary search trên real numbers

Nếu answer continuous, exact equality hiếm có ý nghĩa vì floating-point.

Ta có hai stopping strategies:

```text
fixed iterations
hoặc hi - lo <= epsilon
```

Fixed iterations thường predictable hơn. Với `double`, khoảng 60–100 iterations thường vượt quá precision cần thiết cho nhiều tasks.

Nhưng correctness phải định nghĩa error tolerance theo domain. `1e-9` không tự động phù hợp với mọi scale.

## Floating-point monotonic caveat

Mathematical predicate có thể monotonic nhưng floating-point implementation gần threshold có rounding noise.

Nếu predicate dựa vào accumulated floating-point sums, hãy xem xét numerical stability thay vì giả định exact monotonic sequence ở machine level.

## Exponential search khi chưa biết upper bound

Nếu answer position không có known finite upper bound, ta có thể grow bound theo powers of two:

```text
1, 2, 4, 8, 16, ...
```

cho tới khi predicate true hoặc vượt target, sau đó binary search interval vừa tìm được.

Cost logarithmic theo answer magnitude.

Pattern này hữu ích cho:

```text
unbounded sorted stream/API
unknown array length abstraction
first failure position trong infinite-like domain
```

## Ternary search không phải binary search phiên bản “chia ba nhanh hơn”

Ternary search thường dùng trên **unimodal function** — tăng rồi giảm hoặc giảm rồi tăng — để tìm cực trị.

Nó không thay binary search trên sorted/monotonic predicate. Chia ba không tự động giảm complexity tốt hơn về constant/logic; property của function quyết định algorithm.

## Interpolation search

Nếu sorted numeric values phân bố gần uniform, interpolation search estimate position từ value thay vì midpoint.

Expected performance có thể tốt trên distribution lý tưởng, nhưng worst-case có thể `O(n)`. Nó nhắc rằng search strategy có thể khai thác distribution ngoài order.

Trong general-purpose code, binary search predictable hơn.

## Hash lookup

Hash table dùng hash function để map key vào bucket/index structure.

Expected lookup thường `O(1)` nhưng phụ thuộc collision handling và hash distribution.

Hash search không giữ order, nên các query như:

```text
floor/ceiling
range
predecessor/successor
```

không tự nhiên.

BST/TreeMap chậm hơn asymptotically cho equality lookup nhưng cung cấp ordered search semantics.

## Tree search

BST search loại subtree dựa trên order invariant. Complexity `O(h)` chứ không tự động `O(log n)`.

Balanced BST giữ `h = O(log n)`.

B/B+Tree mở rộng cùng idea cho external memory bằng fan-out lớn.

Searching vì thế nối trực tiếp với representation.

## Trie search

Trie không compare toàn key theo total order. Nó consume key từng symbol/prefix.

Lookup length `L` thường khoảng `O(L)` dưới child lookup assumptions.

Trie phù hợp khi internal structure của key — prefix — có semantics quan trọng.

## Graph search

BFS, DFS, Dijkstra, A* đều là searching trên state graph.

Khác nhau ở frontier policy:

```text
DFS       -> stack
BFS       -> FIFO queue
Dijkstra  -> min priority by distance
A*        -> min priority by g + heuristic
```

Đây là một unified mental model rất mạnh: search algorithm = state space + frontier order + visited/best-known policy.

## State-space search và duplicate detection

Trong puzzles/backtracking, cùng logical state có thể được reach qua nhiều histories.

Nếu future possibilities từ state giống nhau, ta nên canonicalize state và tránh expand lại.

Đây chính là relation giữa search, graph visited và DP memoization.

## Branch and bound

Optimization search có thể giữ best-known solution và lower/upper bound cho partial states. Nếu branch không thể beat incumbent, prune.

Đây không phải binary search; nó là search-tree pruning dựa trên objective bound.

Common pattern:

```text
if optimistic_bound(state) >= best:
    prune
```

cho minimization.

## A* search

A* dùng:

\[
f(n)=g(n)+h(n)
\]

trong đó `g` là cost đã đi, `h` là heuristic estimate remaining cost.

Nếu heuristic admissible/consistent theo assumptions thích hợp, A* vẫn optimal nhưng explore ít states hơn Dijkstra trong nhiều spatial problems.

Heuristic là extra information giúp loại/deprioritize candidates — cùng bản chất với mọi search optimization.

## Search index trong database

Database table scan là linear search ở storage scale.

B+Tree index, hash index, inverted index đều là preprocessing structures để giảm candidate rows/documents.

Index build/update có cost, vì vậy search speed luôn được mua bằng storage + maintenance.

Mental model này giúp nối interview DSA với production systems.

## Inverted index

Search engine text retrieval không scan every document cho mỗi query. Nó xây mapping:

```text
term -> sorted postings list of document IDs
```

Query AND intersect postings lists, thường bằng two pointers/skip information.

Đây là một search index được thiết kế theo workload: query theo term membership.

## Information theory intuition

Nếu cần phân biệt `n` sorted positions bằng binary comparisons, mỗi comparison có khoảng hai outcomes và cung cấp cỡ một bit information.

Để distinguish `n` possibilities cần khoảng:

\[
\log_2 n
\]

bits.

Đây là intuition cho logarithmic comparison lower scale của binary search.

Không phải proof lower bound đầy đủ cho mọi model, nhưng giúp hiểu vì sao `O(log n)` là tự nhiên.

## Preprocessing vs query time

Một dataset static với triệu queries đáng để build index/preprocess.

Một dataset chỉ query một lần có thể không đáng.

Ví dụ:

```text
sort once O(n log n) + q binary searches O(q log n)
```

so với:

```text
q linear scans O(qn)
```

Break-even phụ thuộc `q`, n và constants.

Searching design vì thế cần nhìn **lifecycle workload**, không chỉ một query cô lập.

## Common binary-search bugs

### Midpoint update không shrink interval

Nếu branch dùng `lo = mid` trong interval nơi `mid == lo`, loop có thể infinite. Phải prove interval strictly shrinks.

### Wrong first/last orientation

Code tìm first true nhưng predicate thật là true-then-false.

### Closed vs half-open trộn lẫn

`hi = n-1` nhưng loop/updates viết như `[lo,hi)` tạo off-by-one.

### Predicate không monotonic

Đây là bug conceptual, không phải syntax.

### Overflow

`(lo+hi)/2`, `R+1` hoặc feasibility arithmetic có thể overflow.

## Testing binary search bằng properties

Thay vì chỉ vài examples, test:

```text
empty array
one element
target < min
target > max
all values equal
duplicates nhiều
target tại first/last index
```

Với lower bound, property:

```text
for all i < ans: a[i] < target
for all i >= ans: a[i] >= target
```

Property-based test này mạnh hơn checking one expected index.

## Search và cache locality

Binary search trên array có `O(log n)` comparisons nhưng access pattern nhảy. Tree search cũng pointer-chasing.

For small arrays, linear scan có thể cạnh tranh nhờ contiguous memory, vectorization và branch predictability.

Asymptotic model không bỏ qua hardware effects.

## Galloping search trong merge/intersection

Khi intersect sorted lists có size rất lệch, thay vì advance one-by-one trên list lớn, exponential/galloping jumps rồi binary search có thể tốt hơn.

Search techniques thường compose với nhau; không phải mỗi problem chỉ dùng một named algorithm.

## Search as elimination

Một cách debug design:

```text
Candidate set ban đầu là gì?
Mỗi observation loại candidates nào?
Tại sao loại chúng là safe?
Candidate set có strictly shrink không?
Stopping condition chứng minh điều gì?
```

Nếu không trả lời được, search logic có thể đang dựa vào intuition chưa được proof.

## Mental Model

> Searching là khoa học của **candidate elimination**. Data order, hash index, prefix structure, graph distance, heuristic hay monotonic predicate đều là information dùng để loại hoặc deprioritize candidates. Algorithm tốt không chỉ “tìm nhanh”; nó giải thích rõ vì sao những candidates bị bỏ chắc chắn không thể là answer.

Khi gặp một search problem, hãy hỏi:

```text
Candidate space là gì?
Có order/monotonicity không?
Có thể preprocess/index không?
Search một lần hay rất nhiều lần?
State graph có duplicate states không?
Frontier cần FIFO/LIFO/priority/heuristic?
Need exact answer hay approximate acceptable?
```

Xem thêm: [BST](../02_trees/01_binary_search_trees.md), [BFS/DFS](../03_graphs/01_graph_traversal_bfs_dfs.md), [Shortest Paths](../03_graphs/02_shortest_paths.md), [Trie](../02_trees/04_tries.md).