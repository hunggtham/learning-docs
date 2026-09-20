# Sorting
**Sắp xếp (Sorting / 정렬)**

Sorting tạo order invariant. Giá trị của nó không chỉ là output đẹp: sorted data hỗ trợ binary search, two pointers, merging, deduplication và range processing.

## Lower bound của comparison sorting

Nếu algorithm chỉ thu information bằng comparisons, nó phải phân biệt `n!` permutations. Decision tree cần height ít nhất:

\[
\log_2(n!)=\Omega(n\log n)
\]

Vì vậy comparison sort tổng quát không thể có worst-case asymptotic tốt hơn `n log n`.

## Insertion sort

Duy trì sorted prefix rồi chèn phần tử hiện tại. Worst `O(n²)`, nhưng gần `O(n)` với nearly-sorted input. Nó rất hiệu quả trên arrays nhỏ nên thường xuất hiện trong hybrid sorts.

## Merge sort

Chia đôi, sort hai nửa, merge. Recurrence:

\[
T(n)=2T(n/2)+O(n)=O(n\log n)
\]

Stable nếu merge giữ relative order của equal keys. Array implementation phổ biến cần auxiliary `O(n)` memory.

## Quicksort

Chọn pivot, partition, recurse. Average `O(n log n)`, worst `O(n²)` nếu partitions liên tục lệch. Randomized pivot giảm khả năng input cố định phá algorithm. Quicksort thường cache-friendly và có thể in-place hơn merge sort.

## Heap sort

Build heap `O(n)`, sau đó extract extreme `n` lần, tổng `O(n log n)`. Auxiliary memory có thể `O(1)` với array heap, nhưng không stable theo implementation thông thường.

## Stability

**Stable sort / 안정 정렬** giữ relative order của elements có equal key. Stability quan trọng khi compose nhiều sort keys hoặc record đã có secondary order.

## Non-comparison sorting

Counting sort tận dụng key range nhỏ để đạt `O(n+k)`. Radix sort xử lý digits/chunks qua nhiều passes. Chúng không vi phạm comparison lower bound vì sử dụng structure của keys chứ không chỉ comparisons.

## C, Java, JavaScript pitfalls

C `qsort` không nên được giả định stable. Java sorting API có implementation khác nhau cho primitives/objects tùy JDK. JavaScript:

```js
arr.sort((a,b) => a-b);
```

phải dùng numeric comparator khi sort numbers; default sort dựa trên string conversion semantics.

## Mental Model

> Sorting là khoản đầu tư tạo order để nhiều thao tác phía sau rẻ hơn. Nếu chỉ cần minimum một lần, scan `O(n)` tốt hơn sort `O(n log n)`; nếu chỉ cần top-k, heap có thể hợp hơn.

## Partition của quicksort — Hoare và Lomuto

Partition không phải một operation duy nhất. Lomuto scheme thường dễ dạy, chọn pivot ở cuối và duy trì vùng `<= pivot`; Hoare scheme dùng hai pointers tiến từ hai đầu và thường làm ít swaps hơn.

Điều cần giữ là partition invariant. Ví dụ Lomuto có thể duy trì:

```text
[left .. i]      <= pivot
[i+1 .. j-1]     > pivot
[j .. right-1]   chưa xét
```

Sau mỗi iteration, một phần tử từ vùng chưa xét được đưa vào đúng side. Khi kết thúc, đặt pivot vào boundary.

Quicksort correctness đến từ invariant này + induction trên hai subarrays, không phải từ việc “pivot chia mảng”.

## Three-way partition và nhiều duplicates

Nếu data có rất nhiều keys bằng nhau, two-way partition có thể recurse vô ích trên vùng equal. Dutch National Flag partition chia thành:

```text
< pivot | == pivot | > pivot
```

và chỉ recurse hai vùng ngoài. Đây là cải tiến quan trọng cho duplicate-heavy datasets.

## Introsort và hybrid sorting

Production sorting library hiếm khi dùng một textbook algorithm thuần túy. Introsort bắt đầu bằng quicksort nhưng nếu recursion depth quá lớn thì chuyển sang heapsort để bảo đảm worst-case `O(n log n)`, và có thể dùng insertion sort cho partitions nhỏ.

Mental model: algorithms có strengths ở các regimes khác nhau; hybrid algorithm chọn regime thích hợp thay vì trung thành với một algorithm.

## Timsort idea

Dữ liệu đời thực thường có existing ordered runs. Timsort phát hiện runs, mở rộng/merge chúng thông minh và khai thác presortedness. Java object sorting và nhiều ecosystems từng sử dụng/biến thể Timsort tùy API/version.

Ý tưởng đáng học là **adaptive algorithm**: complexity/performance có thể phụ thuộc structure của input ngoài chỉ `n`.

## Counting sort derivation

Nếu keys là integers trong `[0,k)`, thay vì so sánh pairs, ta đếm frequency:

```text
count[x] = số lần key x xuất hiện
```

Sau đó reconstruct order. Time `O(n+k)`, memory `O(k)`.

Nếu `k` lớn hơn rất nhiều `n`, cost memory/time trên range làm counting sort không còn hợp lý. Vì vậy non-comparison sort không “luôn nhanh hơn”.

## Radix sort

Radix sort xử lý key theo digits/chunks. Nếu mỗi pass dùng stable sort theo một digit, LSD radix giữ order của digits đã xử lý trước.

Với `d` digits và alphabet/radix `k`, cost thường gần:

\[
O(d(n+k))
\]

Đây không vi phạm `Omega(n log n)` lower bound của comparison sort vì algorithm khai thác representation của keys.

## External sorting

Khi data không fit RAM, sorting problem đổi cost model. External merge sort:

1. đọc chunks fit memory, sort mỗi chunk thành run;
2. ghi runs ra disk;
3. k-way merge bằng heap/buffer.

Mục tiêu giảm số sequential I/O passes. Đây nối Sorting với [B-Tree & External Memory](../02_trees/05_b_trees_and_external_memory.md).

## Comparator correctness

Comparator phải nhất quán. Java comparator vi phạm transitivity có thể làm sorting behave không xác định theo contract hoặc throw trong một số implementations. Trong C `qsort`, comparator kiểu `return a-b` có thể overflow; nên so sánh bằng relational branches.

```c
int cmp_int(const void *pa, const void *pb) {
    int a = *(const int *)pa;
    int b = *(const int *)pb;
    return (a > b) - (a < b);
}
```

JavaScript numeric sort cần:

```js
arr.sort((a, b) => a - b);
```

vì default sort dựa trên string conversion semantics.

## Mental Model mở rộng

> Sorting algorithm là cách thu thập đủ thông tin về relative order với chi phí thấp nhất trong model cho phép. Comparison sorts học order qua comparisons; counting/radix sorts khai thác structure bên trong key; external sorts tối ưu data movement giữa memory levels.
