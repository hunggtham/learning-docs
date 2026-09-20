# Sorting
**Sắp xếp (Sorting / 정렬)**

Sorting tạo một **order invariant** trên dữ liệu. Giá trị của sorting không chỉ là “làm output đẹp”. Order là một dạng preprocessing làm nhiều thao tác phía sau rẻ hơn: binary search, two pointers, merging, deduplication, interval processing, rank/select, range scan và external data processing.

Vì vậy câu hỏi đúng không chỉ là “thuật toán sort nào nhanh nhất?”, mà là:

> Ta cần loại order nào, comparator semantics gì, stability có quan trọng không, dữ liệu nằm trong RAM hay external storage, key có structure đặc biệt không, và sau sorting sẽ làm những operations gì?

## Sorting như một phép biến đổi specification

Một sorting algorithm phải thỏa ít nhất hai properties:

1. output ordered theo comparator;
2. output là một permutation/multiset-preserving transformation của input.

Chỉ kiểm tra “array tăng dần” chưa đủ. Một bug có thể làm mất hoặc duplicate elements nhưng output vẫn sorted.

Correctness proof thường cần cả **order invariant** và **conservation invariant**.

## Comparator định nghĩa order

Sorting không tự biết “nhỏ hơn” nghĩa gì. Comparator là một phần của specification.

Một comparator hợp lệ nên có ordering consistent, đặc biệt transitivity:

```text
if a < b and b < c, then a < c
```

Nếu comparator không transitive, sorting library không thể tạo một total order coherent.

Java comparator subtract trực tiếp có thể overflow:

```java
(a, b) -> a - b // risky
```

nên dùng:

```java
Integer.compare(a, b)
```

C:

```c
int cmp_int(const void *pa, const void *pb) {
    int a = *(const int *)pa;
    int b = *(const int *)pb;
    return (a > b) - (a < b);
}
```

JavaScript numeric sorting cần comparator:

```js
arr.sort((a, b) => a - b);
```

vì default sort dùng string-conversion semantics.

## Stable sort

**Stable sort / 안정 정렬** giữ relative order của equal keys.

Giả sử records đã sorted theo `name`, sau đó stable-sort theo `department`. Trong mỗi department, name order cũ được giữ. Stability vì thế giúp compose sort keys theo passes.

Nếu sorting object records theo primary key nhưng muốn ties giữ input arrival order, stability là semantic requirement, không chỉ một performance property.

## In-place, out-of-place và auxiliary memory

Một algorithm “in-place” thường dùng `O(1)` hoặc `O(log n)` auxiliary memory tùy definition/recursion stack. Merge sort array classic cần auxiliary buffer `O(n)`. Heap sort có thể `O(1)` auxiliary. Quicksort thường in-place partition nhưng recursion stack có expected `O(log n)` và worst deeper nếu không controlled.

Memory requirement quan trọng khi arrays rất lớn hoặc runtime object-heavy.

## Comparison sorting lower bound

Nếu algorithm chỉ thu information bằng pairwise comparisons, input có `n!` possible permutations. Decision tree cần ít nhất `n!` leaves.

Một binary comparison cho tối đa hai outcomes, nên height cần:

\[
\log_2(n!)
\]

Stirling approximation cho:

\[
\log(n!)=\Theta(n\log n)
\]

Vì vậy general comparison sorting có worst-case lower bound:

\[
\Omega(n\log n)
\]

Điều này không nói counting/radix sort bất khả thi; chúng dùng additional information về key representation, không chỉ comparisons.

## Insertion Sort

Insertion Sort duy trì sorted prefix.

Invariant:

> Trước iteration `i`, `a[0..i)` sorted và chứa đúng các phần tử ban đầu của prefix đó.

Ta lấy `a[i]`, shift các elements lớn hơn sang phải và đặt key vào đúng vị trí.

Worst-case reverse-sorted input:

\[
1+2+\cdots+(n-1)=\Theta(n^2)
\]

Nhưng nearly sorted input có ít inversions nên insertion sort rất nhanh. Với small arrays, low overhead và cache locality tốt làm nó thường được dùng bên trong hybrid sorts.

## Inversions và adaptive behavior

Một **inversion** là pair `(i,j)` với `i<j` nhưng `a[i]>a[j]`.

Insertion sort runtime liên quan số inversions vì mỗi shift sửa một inversion. Nếu data gần sorted, inversions ít, runtime gần linear.

Đây là ví dụ algorithm complexity phụ thuộc **input disorder measure**, không chỉ `n`.

## Selection Sort

Selection Sort chọn minimum còn lại và swap vào vị trí tiếp theo. Comparisons luôn khoảng `n(n-1)/2`, nên `Theta(n^2)` ngay cả input sorted.

Điểm mạnh là số swaps nhỏ `O(n)`, nên historically có ý nghĩa khi writes rất đắt so với comparisons. Trong general software, nó ít được chọn vì quadratic comparisons.

## Bubble Sort — giá trị chủ yếu là invariant teaching

Bubble Sort swap adjacent inverted pairs. Nó giúp học invariant và inversion reduction, nhưng hiếm khi là production choice.

Điều quan trọng là không biến “biết nhiều sorting algorithms” thành mục tiêu tự thân; cần hiểu trade-off khiến một algorithm phù hợp hay không.

## Merge Sort

Merge Sort chia array, sort hai nửa, rồi merge.

Recurrence:

\[
T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)
\]

Merge invariant có thể là:

> Output prefix luôn chứa đúng những phần tử nhỏ nhất đã consumed từ hai sorted inputs và tự nó sorted.

Stable merge chọn từ left run trước khi equal key xuất hiện ở right run.

## Why merge is powerful

Nếu hai runs đã sorted, merge chỉ cần tiến pointers một chiều. Đây là lý do merge xuất hiện trong external sort, linked-list sorting, LSM compaction và multiway data pipelines.

Sortedness biến global compare-all problem thành linear stream combination.

## Merge Sort trên linked list

Linked list không có random access để binary partition bằng index rẻ, nhưng có thể split bằng slow/fast pointers. Merge hai sorted lists chỉ rewires links và không cần auxiliary array lớn.

Vì thế Merge Sort thường phù hợp linked list hơn Quicksort.

Data representation ảnh hưởng sorting choice.

## Quicksort

Quicksort chọn pivot, partition thành regions rồi recurse.

Average/expected behavior với good/randomized pivots:

\[
O(n\log n)
\]

Worst case repeated `0` vs `n-1` splits:

\[
O(n^2)
\]

Quicksort thường cache-friendly vì partition scan contiguous array và ít auxiliary memory.

## Lomuto partition invariant

Một possible invariant:

```text
[left .. i]      <= pivot
[i+1 .. j-1]     > pivot
[j .. right-1]   chưa xử lý
```

Mỗi iteration move one element từ unknown region sang correct side. Khi done, pivot đặt boundary.

Correctness là partition invariant + induction trên subarrays.

## Hoare partition

Hoare scheme dùng pointers từ hai phía, tìm misplaced elements rồi swap. Nó thường làm fewer swaps và có different boundary semantics.

Không được copy recursion boundaries của Lomuto sang Hoare máy móc; partition contract khác nhau.

Một common source bug là hiểu visual idea nhưng không define exact postcondition của partition function.

## Three-way partition

Nếu nhiều duplicates, two-way partition có thể tạo recursive work lớn trên equal values.

Dutch National Flag partition giữ:

```text
< pivot | == pivot | unknown | > pivot
```

Sau partition chỉ recurse `<` và `>` regions. Duplicate-heavy workload cải thiện mạnh.

## Pivot selection

Always-first/last pivot dễ bị sorted/adversarial input phá. Alternatives:

```text
random pivot
median-of-three
sampling
```

Randomization biến fixed adversarial input thành expected good partitions dưới randomness assumptions.

Security/adversarial context cần cân nhắc attacker có influence randomness không.

## Quicksort stack depth

Ngay cả average runtime tốt, recursion depth có thể overflow nếu partitions xấu.

Một technique: recurse smaller partition trước và loop trên larger partition, giúp stack depth `O(log n)` even with some unbalanced patterns while total work behavior remains based on partitions.

Hybrid introsort còn switch algorithm khi recursion depth vượt threshold.

## Heap Sort

Heap Sort build max-heap `O(n)`, rồi repeatedly swap root với last element và sift-down reduced heap.

Total:

\[
O(n\log n)
\]

worst-case deterministic, auxiliary `O(1)` array implementation.

Trade-off: poor locality/branch patterns hơn some quicksort variants và không stable.

## Build heap is O(n), không phải O(n log n)

Bottom-up heapify gọi sift-down cho internal nodes. Phần lớn nodes ở gần leaves nên travel distance nhỏ.

Tổng work theo heights là linear. Đây là một classic case nơi multiply “n nodes * log n worst per node” tạo bound đúng nhưng quá lỏng.

## Introsort

Introsort bắt đầu Quicksort để tận dụng locality/average speed, theo dõi recursion depth, và nếu depth quá lớn switch sang Heap Sort để giữ worst-case `O(n log n)`. Small partitions thường dùng Insertion Sort.

Đây là production design pattern:

> Combine algorithms có strengths ở different regimes thay vì dùng textbook algorithm thuần túy.

## Timsort

Timsort khai thác existing sorted **runs** trong real-world data. Nó detect ascending/descending runs, normalize, rồi merge theo policies nhằm giữ efficiency.

Timsort adaptive theo presortedness. Một dataset đã gần sorted có thể được xử lý nhanh hơn general random order.

Java object sorting và Python sorting historically use Timsort-family implementations, nhưng exact implementation/version details nên xem runtime docs/source khi cần.

## Counting Sort

Nếu keys là integers trong bounded range `[0,k)`, ta có thể count frequencies:

```text
count[x] = số lần key x xuất hiện
```

Time:

\[
O(n+k)
\]

Memory:

\[
O(k)
\]

Nếu `k` gần `n`, rất tốt. Nếu `k` hàng tỷ nhưng chỉ có vài nghìn items, memory/time scan range không hợp lý.

Counting Sort thắng comparison lower bound vì dùng key-as-index information.

## Stable Counting Sort

Nếu cần stable output records, dùng prefix cumulative counts để xác định output positions. Khi iterate input đúng direction theo construction, equal keys giữ relative order.

Stable counting sort là building block cho LSD Radix Sort.

## Radix Sort

Radix Sort xử lý key theo digits/chunks. LSD (least-significant digit first) cần mỗi pass stable để order của digits đã xử lý không bị phá.

Với `d` digits và per-pass range `k`:

\[
O(d(n+k))
\]

Performance phụ thuộc digit width/radix, memory bandwidth và key representation.

## MSD radix và trie connection

MSD Radix Sort partition theo most-significant digit trước rồi recurse buckets. Conceptually gần trie: prefix digits quyết định branch.

String sorting có thể khai thác common prefixes để tránh re-compare toàn strings.

## Sorting strings không giống sorting integers

Comparator string có thể inspect nhiều characters. Nếu average common prefix dài, “`O(n log n)` comparisons” chưa nói tổng character work.

Locale/collation, Unicode normalization và case folding còn làm comparator đắt/phức tạp hơn byte lexicographic compare.

Cost model phải tính comparator cost khi significant.

## Key extraction và decorate-sort-undecorate

Nếu comparator phải compute expensive derived key nhiều lần, có thể precompute key once:

```text
(record, sortKey)
```

sort theo `sortKey`, rồi discard decoration.

Python-style “key function” APIs conceptually làm điều này. Đây là preprocessing để giảm repeated comparator work.

## Multi-key sorting

Nếu comparator order theo `(department, salary, id)`, có thể compare tuple trực tiếp. Stable multi-pass sorting cũng possible: sort least-significant key trước, rồi stable sort more significant key.

Tuple comparator thường straightforward hơn nếu all keys available.

## External Sorting

Khi data không fit RAM, CPU comparisons không còn primary cost. External Merge Sort:

1. đọc chunk vừa memory;
2. sort chunk thành run;
3. ghi run ra storage;
4. k-way merge runs với buffers + heap.

Mục tiêu giảm random I/O và số passes.

Nếu merge fan-in `k` lớn, cần buffers cho each run nhưng giảm merge levels. Đây là external-memory trade-off.

## Replacement selection intuition

External sorting có techniques tạo initial runs dài hơn memory bằng heap/replacement selection, tùy input distribution. Dù advanced, principle đáng nhớ là streaming + priority structure có thể kéo dài sorted runs trước merge phase.

## Sorting trong database

Database sort có thể phục vụ:

```text
ORDER BY
GROUP BY
merge join
window functions
DISTINCT
index build
```

Nếu memory đủ, in-memory sort. Nếu không, engine spill runs và external merge.

Execution engine phải cân nhắc memory grant, row width, comparator cost và parallelism.

## Sort-Merge Join

Nếu two relations sorted theo join key, merge join scan cả hai gần tuyến tính theo total rows plus output.

Nếu inputs chưa sorted, sort cost có thể được amortize nếu sorted order reused cho other operations hoặc existing indexes already provide order.

DSA choice xuất hiện ở query optimizer level.

## Parallel sorting

Data có thể partition thành chunks, sort concurrently, rồi merge. Scalability phụ thuộc memory bandwidth, merge cost và thread coordination.

Comparison sort không tự speed up linear với cores vì shared memory/cache bandwidth có thể become bottleneck.

## GPU/vectorized sorting

Sorting networks, radix-based approaches và block algorithms có thể tận dụng SIMD/GPU. Model khác branch-heavy scalar quicksort.

Điểm học được: hardware execution model có thể thay algorithmic constants và preferred structure dù asymptotic theory không đổi.

## Sorting networks

Sorting network là fixed sequence compare-exchange independent of data. Bitonic sort là example.

Work có thể nhiều hơn optimal comparison sort, nhưng fixed structure phù hợp parallel hardware/secure computation nơi data-dependent branches/accesses undesirable.

## Partial sorting

Nếu chỉ cần smallest `k`, full sort `O(n log n)` có thể unnecessary.

Alternatives:

```text
heap: O(n log k)
quickselect: expected O(n)
partial_sort/library specialized
```

Nếu cần median một lần, selection problem khác sorting problem.

Xem [Selection & Top-K](./06_selection_and_top_k.md).

## Nearly sorted streams và k-sorted arrays

Nếu mỗi element cách final position tối đa `k`, min-heap size `k+1` sort trong:

\[
O(n\log k)
\]

Constraint structure cho algorithm tốt hơn general sorting.

## Online sorting vs maintaining order

Nếu data updates liên tục và queries cần sorted order sau mỗi update, re-sort toàn collection mỗi lần thường sai abstraction. Balanced tree, skip list hoặc B-tree maintains order incrementally.

Sorting phù hợp batch/static transformation; ordered data structure phù hợp dynamic workload.

## Stability and object identity

Stable sorting equal keys preserves relative sequence, nhưng nếu comparator defines many values equal unintentionally, result may look surprising. Comparator equality is ordering semantics, not necessarily object `equals`.

Java `TreeSet`/sorting comparator consistency concepts connect here.

## Floating-point ordering

NaN breaks ordinary intuition: comparisons with NaN are false in IEEE semantics. Language/library comparators may define total-order policies differently.

If sorting floating data, use API's explicit comparison methods/policies rather than ad-hoc `<`/`>` assumptions when NaN matters.

## Null handling

Production comparator needs define null placement or forbid null. Java comparators can compose `nullsFirst/nullsLast`. JavaScript arrays may contain `undefined`/holes with runtime-specific sort behavior.

Domain specification should decide semantics before algorithm.

## In-place stable sorting is hard

Stable + comparison-based + worst-case `O(n log n)` + strict `O(1)` extra space simultaneously is much harder than textbook merge sort. Production libraries choose practical trade-offs rather than maximize every property.

This is a useful reminder: algorithm properties can conflict.

## Cache locality

Array quicksort/insertion/merge variants scan contiguous memory. Heap Sort jumps parent/child indices, often worse cache behavior. Pointer-based sorts can be dominated by memory latency.

Same `O(n log n)` can have substantially different real performance.

## Branch prediction

Partition comparisons on random data can be branch-unpredictable. Branchless/vectorized techniques may improve performance for primitive keys.

Again, asymptotic complexity does not capture CPU microarchitecture.

## Comparator cost

If compare itself is expensive `C`, total time more accurately includes:

\[
O(C\cdot n\log n)
\]

for comparison sort. Avoid repeated parsing/network lookup/complex normalization inside comparator.

Comparators should generally be pure and cheap.

## Sorting and immutability

In-place sort mutates input. API must define whether mutation is acceptable. JavaScript `Array.sort()` mutates array; if functional semantics needed, copy first or use immutable APIs where available.

Copy adds `O(n)` memory/time and can matter for large data.

## Correctness testing

A strong sorting test checks:

```text
ordered output
same multiset as input
stability when promised
comparator consistency assumptions
```

Differential testing can compare custom algorithm with standard library sort on random arrays, including duplicates, extremes, already-sorted/reverse-sorted and patterned inputs.

## Adversarial cases

Quicksort needs test sorted/reverse/all-equal if pivot policy deterministic. Counting Sort needs range extremes. Integer comparator tests need `MIN_VALUE/MAX_VALUE` to expose subtraction overflow.

External sort needs empty runs, duplicate-heavy boundaries and partial final buffers.

## Benchmarking sorting fairly

Benchmark must separate:

```text
random primitives
nearly sorted data
many duplicates
large records + key comparator
strings with common prefixes
input larger than cache
```

One random-int benchmark does not establish universal winner.

Also decide whether benchmark includes allocation/copy/key extraction.

## Common misconceptions

“Quicksort is always fastest” — false; workload/runtime matter.

“Stable means sorted correctly” — stability is additional tie-order property.

“Counting Sort is `O(n)`” — only if key range term is controlled; actual `O(n+k)`.

“`n log n` lower bound means no linear sorting” — only comparison model.

“Heap Sort build phase is `n log n`” — bottom-up heap construction is `O(n)`.

“Sorted data should always stay in array” — dynamic update workload may need ordered structure.

## Choosing a sorting approach

A useful reasoning path:

```text
Need full ordering or only min/top-k/select?
Keys arbitrary comparison-only or bounded integers/digits?
Need stable order?
Need deterministic worst-case bound?
Memory constraints?
Data nearly sorted / duplicate-heavy?
Data fits memory?
Comparator expensive?
```

Then choose algorithm/library accordingly.

In most application code, use high-quality standard library sort unless domain constraints justify custom implementation. Learning textbook algorithms is để hiểu invariants/trade-offs và biết khi library behavior matters, không phải để reimplement sorting everywhere.

## Mental Model

> Sorting là quá trình trả một khoản cost để biến relation “unordered” thành một global order có thể khai thác về sau. Comparison sorts học order qua pairwise comparisons; radix/counting khai thác structure của keys; external sorts tối ưu data movement giữa memory levels; adaptive/hybrid sorts khai thác input structure và strengths của nhiều algorithms.

Khi chọn sorting strategy, hãy hỏi: **ta thực sự cần bao nhiêu order, comparator cho biết bao nhiêu information, input có structure đặc biệt gì, và cost quan trọng nằm ở comparisons, data movement, memory hay I/O?**

Xem tiếp: [Searching](./00_searching.md), [Divide and Conquer](./03_divide_and_conquer.md), [Selection & Top-K](./06_selection_and_top_k.md), [Heap](../02_trees/03_heaps.md), [B-Tree & External Memory](../02_trees/05_b_trees_and_external_memory.md) và [Mathematical Toolkit](../00_foundations/04_mathematical_toolkit_for_dsa.md).
