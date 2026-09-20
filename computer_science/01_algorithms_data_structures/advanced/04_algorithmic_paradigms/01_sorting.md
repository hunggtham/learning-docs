# Sắp xếp
**Sorting / 정렬**

Sắp xếp tạo ra một **bất biến thứ tự** trên dữ liệu. Giá trị của sorting không chỉ là “làm dữ liệu đẹp hơn”. Một khi dữ liệu có thứ tự, nhiều bài toán khác trở nên rẻ hơn: binary search, two pointers, merge, deduplication, interval processing, ranking, range scan, external processing và database operations.

Vì vậy câu hỏi đúng không phải “sort nào nhanh nhất?”, mà là:

> Ta cần thứ tự nào, comparator có semantics gì, stability có quan trọng không, dữ liệu nằm trong RAM hay storage ngoài, key có cấu trúc đặc biệt không, input có gần sorted không, và sau sorting ta sẽ làm gì tiếp?

## Specification của sorting

Một sorting algorithm đúng phải thỏa ít nhất hai điều:

```text
1. output có thứ tự theo comparator
2. output là một hoán vị của input
```

Điều thứ hai là **bất biến bảo toàn (conservation invariant)**. Một implementation có thể tạo output tăng dần nhưng làm mất hoặc nhân đôi phần tử; khi đó vẫn sai.

Nếu sort record, specification còn có thể gồm stability, null handling, secondary key hoặc tie-breaking.

## Comparator định nghĩa thế giới thứ tự

Sorting không tự biết “nhỏ hơn” nghĩa gì. Comparator là một phần của specification.

Một comparator tốt phải nhất quán với một thứ tự hợp lệ, đặc biệt cần tính bắc cầu:

```text
a < b và b < c  =>  a < c
```

Comparator không bắc cầu có thể làm sort, TreeMap hoặc PriorityQueue hành xử khó dự đoán.

Trong Java, tránh:

```java
(a, b) -> a - b
```

vì phép trừ có thể overflow. Dùng:

```java
Integer.compare(a, b)
Comparator.comparingInt(Node::score)
```

Trong C:

```c
int cmp_int(const void *pa, const void *pb) {
    int a = *(const int *)pa;
    int b = *(const int *)pb;
    return (a > b) - (a < b);
}
```

Trong JavaScript, numeric sort cần comparator rõ:

```js
arr.sort((a, b) => a - b);
```

## Total order và partial order

Không phải mọi domain tự nhiên đều có total order.

Ví dụ task có hai tiêu chí `(cost, quality)` có thể có hai phần tử không cái nào “tốt hơn toàn diện”. Đây là **partial order**.

Nếu muốn sort toàn bộ, ta phải chọn một total order bổ sung, ví dụ:

```text
cost tăng dần
nếu cost bằng nhau thì quality giảm dần
nếu vẫn bằng nhau thì id tăng dần
```

Việc thêm tie-breaker không chỉ để tránh comparator trả 0; nó xác định semantics của output.

## Stable sorting

**Sắp xếp ổn định (stable sorting / 안정 정렬)** giữ thứ tự tương đối của các phần tử có key bằng nhau.

Nếu dữ liệu ban đầu đã sort theo `name`, sau đó stable-sort theo `department`, trong mỗi department thứ tự `name` cũ vẫn được giữ.

Stability quan trọng khi:

```text
sort nhiều khóa qua nhiều lượt
muốn bảo toàn thứ tự đến ban đầu
record có cùng business key nhưng khác metadata
pipeline dựa vào thứ tự trước đó
```

Stable không phải tính chất “tốt hơn chung”; nó là một yêu cầu semantics có chi phí implementation nhất định.

## In-place và out-of-place

Một thuật toán in-place thường dùng rất ít memory phụ trợ. Merge Sort trên array cổ điển dùng buffer `O(n)`. Heap Sort có thể dùng `O(1)` auxiliary memory. Quicksort thường partition tại chỗ nhưng còn recursion stack.

Khi dữ liệu cực lớn, memory footprint có thể quan trọng ngang runtime.

Ngoài Big-O, còn phải xét:

```text
peak memory
allocation count
cache locality
object movement
GC pressure
```

## Cận dưới của comparison sorting

Nếu thuật toán chỉ học thông tin qua pairwise comparison, `n` phần tử phân biệt có `n!` thứ tự khả dĩ.

Decision tree cần ít nhất `n!` lá. Mỗi comparison nhị phân tạo tối đa hai nhánh, nên chiều cao ít nhất:

\[
\log_2(n!)=\Omega(n\log n)
\]

Do đó general comparison sorting không thể có worst-case `O(n)`.

Counting Sort hoặc Radix Sort không mâu thuẫn với kết quả này vì chúng khai thác representation của key, không chỉ comparison.

## Insertion Sort

Insertion Sort duy trì invariant:

> Trước vòng `i`, prefix `a[0..i)` đã sorted và chứa đúng các phần tử ban đầu của prefix đó.

Mỗi bước lấy `a[i]` và chèn vào đúng vị trí trong prefix.

Worst-case:

\[
\Theta(n^2)
\]

nhưng trên dữ liệu gần sorted, số lần shift nhỏ.

## Inversion và tính adaptive

Một **inversion** là cặp `(i,j)` sao cho:

```text
i < j nhưng a[i] > a[j]
```

Insertion Sort thực hiện lượng công việc liên quan trực tiếp số inversion. Nếu input gần sorted, inversion ít và runtime có thể gần tuyến tính.

Đây là ví dụ complexity phụ thuộc không chỉ `n` mà còn **độ mất trật tự của input**.

Một thuật toán gọi là **adaptive** nếu nó tận dụng structure như “đã gần sorted”.

## Selection Sort

Selection Sort tìm phần tử nhỏ nhất còn lại rồi đổi vào vị trí tiếp theo.

Số comparison gần như luôn:

\[
\frac{n(n-1)}2
\]

nên `Θ(n²)` kể cả input đã sorted.

Điểm đáng chú ý là số swap chỉ `O(n)`. Trong môi trường write rất đắt, đặc tính này từng có ý nghĩa. Nhưng với software thông thường, quadratic comparisons làm Selection Sort ít hấp dẫn.

## Bubble Sort

Bubble Sort swap các cặp adjacent bị đảo thứ tự.

Giá trị học thuật chính của nó là giúp hiểu:

```text
local repair
inversion
loop invariant
early termination
```

Trong production, nó hiếm khi là lựa chọn tốt.

Biết nhiều tên sorting algorithm không quan trọng bằng hiểu lý do một thuật toán phù hợp với một workload cụ thể.

## Merge Sort

Merge Sort chia array, sort hai nửa rồi merge.

\[
T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)
\]

Merge invariant:

> Prefix output luôn chứa đúng những phần tử nhỏ nhất đã được lấy từ hai input sorted và prefix đó đã có thứ tự.

Một stable merge chọn phần tử bên trái trước khi hai key bằng nhau.

## Vì sao merge là primitive mạnh?

Nếu hai run đã sorted, merge chỉ cần hai con trỏ tiến một chiều.

Điều này xuất hiện trong:

```text
Merge Sort
external sorting
LSM compaction
merge join
k-way merge
stream processing
```

Sorting biến nhiều so sánh rời rạc thành một lần quét tuyến tính có cấu trúc.

## Merge Sort trên linked list

Linked List không có random access rẻ nhưng split bằng slow/fast pointers và merge chỉ cần nối lại links.

Vì vậy Merge Sort thường phù hợp Linked List hơn Quicksort.

Data representation ảnh hưởng algorithm choice.

## Quicksort

Quicksort chọn pivot, partition rồi recurse.

Với pivot tốt hoặc randomized pivot, expected runtime thường:

\[
O(n\log n)
\]

Worst-case khi partition liên tục cực lệch:

\[
O(n^2)
\]

Quicksort thường nhanh thực tế trên array vì partition quét dữ liệu contiguous và có locality tốt.

## Partition là trung tâm của Quicksort

Điều khó nhất trong Quicksort không phải recursion mà là contract của partition.

### Lomuto

Một invariant có thể là:

```text
[left..i]      <= pivot
[i+1..j-1]     > pivot
[j..right-1]   chưa xử lý
```

Sau khi quét xong, pivot được đặt vào vị trí biên đúng.

### Hoare

Hoare partition dùng hai con trỏ đi từ hai phía, tìm phần tử ở sai phía rồi swap.

Nó thường ít swap hơn nhưng contract về vị trí trả về khác Lomuto.

Một lỗi phổ biến là lấy partition code của một scheme nhưng dùng recursion boundary của scheme khác.

## Three-way partition

Nếu nhiều duplicate, two-way partition có thể làm việc thừa.

Dutch National Flag giữ:

```text
< pivot | == pivot | unknown | > pivot
```

Sau partition chỉ recurse hai vùng `<` và `>`.

Nếu toàn bộ array bằng nhau, three-way partition có thể xử lý gần tuyến tính thay vì tạo nhiều recursive call vô ích.

## Pivot selection

Chọn đầu/cuối cố định có thể tệ trên input sorted hoặc adversarial.

Các chiến lược:

```text
random pivot
median-of-three
sample nhiều phần tử
```

Randomization không làm worst-case biến mất về toán học, nhưng làm fixed adversarial input khó ép partition xấu nếu random source đủ tốt.

## Stack depth của Quicksort

Nếu recurse vô điều kiện cả hai phía, partition lệch có thể tạo recursion sâu `O(n)`.

Một kỹ thuật là recurse phía nhỏ hơn và lặp phía lớn hơn. Khi đó recursion stack có thể bị chặn `O(log n)` theo kích thước phía nhỏ, dù tổng runtime vẫn phụ thuộc partition quality.

Đây là ví dụ tối ưu stack mà không thay semantics của partition.

## Heap Sort

Heap Sort:

```text
build max-heap
swap root với phần tử cuối
reduce heap size
sift-down
lặp lại
```

Worst-case:

\[
O(n\log n)
\]

với auxiliary memory nhỏ.

Trade-off là locality và branch behavior thường không tốt bằng các hybrid sort hiện đại trên array.

Heap Sort không stable theo implementation thông thường.

## Vì sao build-heap là O(n)?

Một upper bound thô `n * O(log n)` cho `O(n log n)`, nhưng quá lỏng.

Phần lớn node gần lá và chỉ sift xuống rất ít. Tổng chi phí theo chiều cao:

\[
\sum_{h\ge0}\frac{n}{2^{h+1}}O(h)=O(n)
\]

Đây là ví dụ quan trọng: không thể luôn lấy “số phần tử × worst cost của một phần tử” để có tight bound.

## Introsort

Introsort kết hợp:

```text
Quicksort cho tốc độ thực tế tốt
Heap Sort làm fallback khi recursion quá sâu
Insertion Sort cho partition rất nhỏ
```

Mục tiêu là giữ ưu điểm average/locality của Quicksort nhưng bảo vệ worst-case `O(n log n)`.

Đây là triết lý phổ biến trong library algorithm: **hybrid hóa theo vùng input mà mỗi thuật toán mạnh nhất**.

## Timsort: tận dụng run có sẵn

Timsort phát hiện các **run** đã sorted hoặc gần sorted rồi merge chúng theo policy có kiểm soát.

Nó đặc biệt hiệu quả với dữ liệu thực tế thường đã có cấu trúc, ví dụ timestamp gần thứ tự hoặc list được chỉnh sửa nhẹ từ trạng thái đã sorted.

Timsort cho thấy một sorting library tốt không nhất thiết giả định input là random; nó có thể khai thác pre-existing order.

## Counting Sort

Nếu key integer nằm trong miền nhỏ `[0,k)`, ta có thể đếm tần suất:

```text
count[key]++
```

Runtime:

\[
O(n+k)
\]

Đây không phải comparison sort.

Nếu `k` lớn hơn rất nhiều `n`, memory/time khởi tạo bảng đếm có thể làm nó không phù hợp.

Counting Sort mạnh khi **miền khóa nhỏ và dày đặc**.

## Stable Counting Sort

Muốn dùng Counting Sort làm bước con của Radix Sort, cần thường giữ stability.

Ta chuyển count thành cumulative positions rồi đặt phần tử theo thứ tự thích hợp.

Điều này cho thấy stability có thể trở thành dependency correctness của một thuật toán khác, không chỉ preference đầu ra.

## Radix Sort

Radix Sort xử lý key theo từng digit/chunk.

**LSD Radix Sort** từ digit thấp lên cao yêu cầu sort ở mỗi digit phải stable để thứ tự của các digit đã xử lý trước không bị phá.

Nếu có `d` digit và mỗi pass `O(n+k)`:

\[
O(d(n+k))
\]

Khi `d` nhỏ cố định, có thể gần tuyến tính theo `n`.

Nhưng cost thật còn phụ thuộc representation, base, cache và memory bandwidth.

## MSD Radix Sort

MSD xử lý digit quan trọng nhất trước rồi recursively chia nhóm.

Nó có thể phù hợp string/prefix-like data và cho phép dừng sớm khi prefix đủ phân biệt.

LSD và MSD có semantics/implementation trade-off khác nhau; không nên xem Radix Sort như một công thức duy nhất.

## Bucket Sort

Bucket Sort phân phần tử vào các bucket theo range rồi sort từng bucket.

Hiệu quả phụ thuộc distribution. Nếu dữ liệu phân bố đều và bucket balance tốt, runtime có thể rất tốt. Nếu toàn bộ rơi vào một bucket, lợi ích biến mất.

Đây là ví dụ average-case dựa mạnh vào input distribution.

## External Sorting

Khi dữ liệu lớn hơn RAM, mô hình chi phí thay đổi. I/O theo block quan trọng hơn CPU comparison.

External Merge Sort thường:

```text
1. đọc một chunk vừa RAM
2. sort trong RAM
3. ghi thành sorted run
4. k-way merge các run
```

Mục tiêu là tối đa sequential I/O và giảm số pass trên storage.

Một thuật toán `O(n log n)` trong RAM model chưa đủ để đánh giá external workload.

## K-way merge

Nếu có `k` sorted runs, dùng min-heap chứa phần tử đầu hiện tại của mỗi run:

```text
extract min
đưa phần tử tiếp theo từ run tương ứng vào heap
```

Runtime:

\[
O(N\log k)
\]

với `N` tổng số phần tử.

Trong external sorting, `k` còn bị giới hạn bởi buffer memory và số stream I/O có thể quản lý hiệu quả.

## Merge Join

Nếu hai bảng đã sorted theo join key, equi-join có thể quét hai phía theo thứ tự.

Sort ban đầu tốn chi phí, nhưng nếu cùng thứ tự đó được tái sử dụng cho nhiều operator, chi phí tiền xử lý có thể được amortize.

Đây là ví dụ sorting như materialized structure cho pipeline sau.

## Partial sorting và Top-K

Nếu chỉ cần `k` phần tử nhỏ nhất/lớn nhất, sort toàn bộ `n` phần tử có thể thừa.

Các lựa chọn:

```text
heap size k            O(n log k)
Quickselect            expected O(n)
partial sort library   tùy implementation
counting/bucket        nếu key domain phù hợp
```

Mục tiêu output ảnh hưởng thuật toán. Không nên sort toàn bộ chỉ vì dữ liệu “cần lấy top”.

## Quickselect

Quickselect dùng partition như Quicksort nhưng chỉ recurse phía chứa rank cần tìm.

Expected runtime với pivot phù hợp:

\[
O(n)
\]

Worst-case vẫn `O(n²)` nếu partition liên tục tệ.

Đây là ví dụ cùng primitive partition nhưng objective khác làm recursion tree thay đổi hoàn toàn.

## Deterministic selection

Median-of-medians cho selection worst-case `O(n)` bằng cách chọn pivot bảo đảm partition không quá tệ.

Nó quan trọng về lý thuyết vì chứng minh selection tuyến tính worst-case là có thể, dù constant factor khiến implementation thực tế thường ưu tiên randomized/select hybrid.

## Stable vs unstable: cách tạo stability bổ sung

Nếu thuật toán không stable nhưng cần semantics stable, có thể decorate key bằng original index:

```text
(key, originalIndex)
```

rồi sort theo tuple.

Trade-off là thêm memory/key comparison cost.

Đây là kỹ thuật chung: khi structure không giữ một property, ta có thể mã hóa property đó vào key.

## Sorting object lớn và indirect sorting

Nếu record rất lớn, swap/copy object trực tiếp có thể đắt.

Có thể sort:

```text
array of pointers/references
array of indices
small key records
```

rồi dùng thứ tự đó để truy cập payload lớn.

Indirect sorting giảm data movement nhưng tăng pointer chasing.

Again, representation quyết định hiệu năng.

## Cache locality

Merge Sort quét tuyến tính nhưng cần buffer. Quicksort partition quét contiguous region. Heap Sort truy cập các vị trí theo cây và thường locality kém hơn.

Trên data lớn, memory bandwidth và cache miss có thể quyết định nhiều hơn số comparison thuần túy.

Hai thuật toán cùng `O(n log n)` không nhất thiết chạy gần nhau.

## Branch prediction

Comparator và partition tạo nhiều branch phụ thuộc dữ liệu.

Data distribution có thể làm branch predictor hoạt động tốt hoặc tệ. Một số high-performance sorting implementation dùng branchless techniques hoặc vectorized partition ở mức thấp.

Điểm cần học: Big-O không mô tả branch/memory behavior.

## Parallel Sorting

Sorting có thể song song hóa bằng:

```text
chia data thành chunks
sort chunks song song
merge song song hoặc nhiều tầng
```

Parallel speedup bị giới hạn bởi:

```text
memory bandwidth
load balance
merge overhead
thread scheduling
NUMA locality
```

Sort nhỏ không đáng tạo thread.

## Distributed Sorting

Ở quy mô cluster, một pattern là range/hash partition data giữa worker rồi local sort.

Nếu cần global total order, partition boundaries phải bảo đảm mọi key ở partition trước nhỏ hơn mọi key ở partition sau.

Data skew có thể làm một worker nhận quá nhiều record, tạo hotspot. Sampling splitter hoặc dynamic partitioning được dùng để giảm skew.

Sorting ở đây trở thành bài toán cả algorithm lẫn data distribution.

## Strings và Unicode

Sorting string không chỉ là `O(n log n)` theo số phần tử. Mỗi comparison có thể phải đọc nhiều ký tự chung ở prefix.

Nếu string dài và có prefix chung, comparison cost đáng kể.

Unicode còn đặt câu hỏi:

```text
sort theo code unit?
code point?
locale/collation rule?
case-insensitive?
normalized form nào?
```

“Alphabetical order” trong business software là một specification phức tạp hơn numeric comparator.

## Floating-point và NaN

Floating-point có `NaN`, `-0`, infinities và rounding semantics.

Comparator phải xác định order rõ cho các giá trị này nếu chúng có thể xuất hiện. Một comparator không nhất quán với NaN có thể phá total order.

Library thường đã có contract cụ thể; custom comparator cần theo đúng semantics mong muốn.

## Sorting và database index

B+Tree index duy trì thứ tự incrementally để tránh sort lại toàn bộ mỗi query. Có thể xem index như “trả chi phí cập nhật để materialize sorted access path”.

Nếu workload chủ yếu đọc theo range, ordered index rất có giá trị. Nếu workload chỉ exact lookup, Hash Index có thể hợp hơn.

Sorting và indexing là hai cách khác nhau để trả trước chi phí cho tương lai.

## Sorting network

Sorting network là chuỗi comparator cố định, không phụ thuộc dữ liệu.

Nó quan trọng trong hardware, SIMD hoặc secure computation vì control flow cố định có thể giảm branch và data-dependent behavior.

Bitonic Sort là ví dụ nổi tiếng.

Dù comparison count thường lớn hơn algorithm tốt trên CPU tuần tự, cấu trúc song song và deterministic có thể làm nó phù hợp môi trường đặc biệt.

## Oblivious sorting

Trong một số security context, không chỉ output đúng mà pattern truy cập bộ nhớ cũng không được tiết lộ nhiều về dữ liệu.

**Oblivious algorithms** dùng access pattern ít phụ thuộc input hơn.

Đây là ví dụ correctness/security specification mở rộng vượt ra ngoài “mảng đã sorted”.

## Kiểm thử sorting

Không chỉ test “output tăng dần”. Cần ít nhất:

```text
ordered(output)
multiset(output) == multiset(input)
```

Nếu cần stable:

```text
các phần tử bằng key giữ relative order cũ
```

Nên thử:

```text
rỗng
1 phần tử
đã sorted
reverse sorted
tất cả bằng nhau
nhiều duplicate
random
nearly sorted
sawtooth pattern
extreme numeric values
```

Quicksort cần test kỹ partition boundaries và duplicate.

## Benchmark sorting

Một benchmark có ý nghĩa cần mô tả distribution input:

```text
uniform random
sorted
reverse sorted
few unique keys
nearly sorted
many duplicates
large records
strings with long common prefix
```

Và đo thêm:

```text
allocation
peak memory
cache behavior nếu có thể
comparison count
write count
```

Một “winner” trên random integers có thể không phải lựa chọn tốt nhất cho workload thật.

## Chọn thuật toán theo workload

Một bảng định hướng:

| Tình huống | Lựa chọn thường đáng cân nhắc |
|---|---|
| Data nhỏ hoặc gần sorted | Insertion Sort / hybrid |
| General in-memory array | library hybrid sort |
| Cần stable | stable Merge/Timsort-style |
| Cần worst-case comparison bound, ít memory | Heap Sort / Introsort fallback |
| Nhiều duplicate | three-way partition / adaptive stable sort |
| Integer key miền nhỏ | Counting Sort |
| Fixed-width integer/string chunks | Radix Sort |
| Dữ liệu vượt RAM | External Merge Sort |
| Chỉ cần Top-K | heap / selection |
| Linked List | Merge Sort thường tự nhiên |

Bảng này không thay profiling và API contract.

## Những hiểu lầm phổ biến

“Quicksort luôn nhanh nhất” — sai; workload và implementation quyết định.

“`O(n log n)` nào cũng gần nhau” — sai vì locality, branch, allocation và stability khác nhau.

“Stable chỉ là tính chất phụ” — có thể là một phần correctness của multi-key sorting.

“Counting Sort phá cận dưới `n log n`” — cận dưới đó chỉ áp dụng comparison sorting.

“Sort toàn bộ luôn cần nếu muốn Top-K” — sai.

“Library sort dùng một thuật toán duy nhất” — nhiều thư viện dùng hybrid strategy tùy kiểu dữ liệu, kích thước và runtime.

## Mô hình tư duy

> Sorting là quá trình trả một chi phí để xây dựng **trật tự có thể tái sử dụng**. Chọn sorting algorithm là chọn cách cân bằng comparison, data movement, memory, stability, input structure và môi trường lưu trữ.

Khi cần sort, hãy hỏi: **comparator có total order đúng không, stability có phải requirement không, input có structure nào tận dụng được không, có thật sự cần sort toàn bộ không, key domain có cho phép non-comparison sort không, và bottleneck là CPU comparison hay data movement/I/O?**

Xem tiếp: [Searching](./00_searching.md), [Divide and Conquer](./03_divide_and_conquer.md), [Selection & Top-K](./06_selection_and_top_k.md), [Intervals & Sweep Line](./08_intervals_and_sweep_line.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md) và [Cross-language Testing](../80_language_implementations/03_cross_language_testing_and_benchmarking.md).