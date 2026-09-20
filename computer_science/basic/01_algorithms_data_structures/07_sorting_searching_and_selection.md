# Sorting, searching và selection

Sorting (정렬 / sắp xếp) tưởng như bài tập cơ bản nhưng nó phơi bày nhiều idea: comparison model, divide-and-conquer, stability, locality, lower bound và trade-off giữa CPU với memory. Searching và selection tiếp tục cùng câu hỏi: ta khai thác structure nào của data để tránh work không cần thiết?

## Linear search và binary search

Nếu data không có ordering/index, tìm key thường phải scan `O(n)`. Binary search khai thác sorted order để bỏ nửa search interval mỗi comparison, `O(log n)`.

Binary search dễ viết sai vì boundary semantics. Half-open interval `[lo, hi)` thường giúp invariant rõ: candidate positions luôn nằm trong interval, size là `hi-lo`. Midpoint nên tính tránh overflow ở languages fixed integer, ví dụ `lo + (hi-lo)/2`.

Binary search không chỉ tìm exact key. Lower bound/upper bound tìm first position thỏa predicate monotonic. Pattern này áp dụng cho “minimum capacity đủ”, “earliest time condition true” nếu predicate chuyển false→true một lần.

## Stable sort

Stable sorting giữ relative order của elements có equal key. Nếu đã sort employees theo name rồi stable sort theo department, within department name order được giữ. Stability là semantic property, không thể nhìn chỉ Big O.

## Insertion sort

Insertion sort xây sorted prefix, chèn từng element đúng vị trí. Worst O(n²), nhưng simple, in-place và nhanh với arrays nhỏ hoặc nearly sorted. Hybrid production sorts thường dùng insertion sort cho tiny partitions vì constants/cache tốt.

## Merge sort

Merge sort chia đôi, sort hai halves, merge. Time Θ(n log n), dễ stable, nhưng array implementation thường cần extra O(n) memory. Linked list merge sort có thể tận dụng pointer rewiring.

Nó minh họa divide-and-conquer rõ và có predictable worst-case.

## Quicksort

Quicksort partition quanh pivot rồi recursively sort partitions. Average/expected O(n log n), worst O(n²), nhưng in-place variants và locality tốt làm nó rất nhanh thực tế. Random pivot hoặc robust pivot strategy giảm nguy cơ bad partitions.

Three-way partition hữu ích khi nhiều duplicates.

## Heapsort

Heapsort build heap O(n), rồi repeatedly extract max/min, total O(n log n), in-place và worst-case bounded, nhưng locality/constant thường kém quicksort. Nó cho thấy theoretical guarantees không quyết định toàn bộ engineering choice.

## Comparison lower bound

Trong comparison model, sorting n distinct elements cần Ω(n log n) comparisons worst-case. Decision tree có ít nhất n! leaves cho permutations; binary comparison tree height ít nhất log₂(n!) = Θ(n log n).

Counting/radix sort vượt bound bằng cách không chỉ dùng pairwise comparisons; chúng khai thác key representation/range.

## Selection

Selection hỏi k-th smallest mà không cần full sorting. Quickselect expected O(n) partition tương tự quicksort nhưng chỉ recurse một side. Median-of-medians cho worst-case O(n) nhưng constants lớn.

Nếu chỉ cần top-k streaming, heap size k cho O(n log k) có thể phù hợp hơn sorting toàn bộ O(n log n).

## External sorting

Khi data lớn hơn RAM, I/O dominates. External merge sort tạo sorted runs vừa memory rồi multi-way merge từ disk. Đây là lý do database query engine có algorithms khác khi sort spills to disk.

## Mental Model

> Sorting/searching performance đến từ **structure đã có** và **guarantee cần giữ**. Hỏi data có sorted không, key domain gì, có cần stability/in-place/worst-case không, và data có fit memory không.

## Common Misconceptions

**“Quicksort luôn O(n log n).”** Expected/average dưới pivot assumptions; worst-case O(n²).

**“Binary search chỉ dùng để tìm number trong sorted array.”** Nó áp dụng cho bất kỳ monotonic predicate trên ordered search space.

**“Sort O(n log n) là tối ưu tuyệt đối.”** Chỉ là lower bound trong comparison model.

## Kết nối

Sorting dựa [complexity](./01_complexity_and_asymptotic_analysis.md), [algorithm strategies](./08_algorithmic_strategies.md) và [memory locality](./02_memory_models_and_data_layout.md); database có [sort/merge/hash query plans](../05_data_databases/03_indexes_and_query_execution.md) nơi data size và I/O thay cost model.
