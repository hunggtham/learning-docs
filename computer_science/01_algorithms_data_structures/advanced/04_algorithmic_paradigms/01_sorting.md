# Sắp xếp

> **Mạch đọc:** Đọc **Sắp xếp** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Specification của sorting** sang **Comparator định nghĩa thế giới thứ tự**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

**Sorting / 정렬**

Sắp xếp tạo ra một **bất biến thứ tự** trên dữ liệu. Giá trị của sorting không chỉ là “làm dữ liệu đẹp hơn”. Một khi dữ liệu có thứ tự, nhiều bài toán khác trở nên rẻ hơn: tìm kiếm nhị phân (binary search / 이진 탐색), two pointers, merge, deduplication, interval processing, ranking, phạm vi (range / 범위) scan, bên ngoài (external / 외부) processing và cơ sở dữ liệu (database / 데이터베이스) operations.

Vì vậy câu hỏi đúng không phải “sort nào nhanh nhất?”, mà là:

> Ta cần thứ tự nào, comparator có ngữ nghĩa (semantics / 의미론) gì, stability có quan trọng không, dữ liệu nằm trong RAM hay lưu trữ (storage / 저장소) ngoài, key có cấu trúc đặc biệt không, đầu vào (input / 입력) có gần sorted không, và sau sorting ta sẽ làm gì tiếp?

## Specification của sorting

Một sorting thuật toán (algorithm / 알고리즘) đúng phải thỏa ít nhất hai điều:

```text
1. output có thứ tự theo comparator
2. output là một hoán vị của input
```

Điều thứ hai là **bất biến bảo toàn (conservation invariant)**. Một hiện thực (implementation / 구현) có thể tạo đầu ra (output / 출력) tăng dần nhưng làm mất hoặc nhân đôi phần tử; khi đó vẫn sai.

Nếu sort bản ghi (record / 레코드), specification còn có thể gồm stability, null handling, secondary key hoặc tie-breaking.

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

## Total thứ tự (order / 순서) và partial thứ tự (order / 순서)

Không phải mọi lĩnh vực (domain / 도메인) tự nhiên đều có total thứ tự (order / 순서).

Ví dụ tác vụ (task / 작업) có hai tiêu chí `(cost, quality)` có thể có hai phần tử không cái nào “tốt hơn toàn diện”. Đây là **partial thứ tự (order / 순서)**.

Nếu muốn sort toàn bộ, ta phải chọn một total thứ tự (order / 순서) bổ sung, ví dụ:

```text
cost tăng dần
nếu cost bằng nhau thì quality giảm dần
nếu vẫn bằng nhau thì id tăng dần
```

Việc thêm tie-breaker không chỉ để tránh comparator trả 0; nó xác định ngữ nghĩa (semantics / 의미론) của đầu ra (output / 출력).

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

Stable không phải tính chất “tốt hơn chung”; nó là một yêu cầu ngữ nghĩa (semantics / 의미론) có chi phí hiện thực (implementation / 구현) nhất định.

## In-place và out-of-place

Một thuật toán in-place thường dùng rất ít bộ nhớ (memory / 메모리) phụ trợ. Merge Sort trên array cổ điển dùng buffer `O(n)`. vùng nhớ động (heap / 힙) Sort có thể dùng `O(1)` auxiliary bộ nhớ (memory / 메모리). Quicksort thường partition tại chỗ nhưng còn recursion ngăn xếp (stack / 스택).

Khi dữ liệu cực lớn, bộ nhớ (memory / 메모리) footprint có thể quan trọng ngang thời gian chạy (runtime / 런타임).

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

Cây quyết định (decision tree / 의사결정 트리) cần ít nhất `n!` lá. Mỗi comparison nhị phân tạo tối đa hai nhánh, nên chiều cao ít nhất:

\[
\log_2(n!)=\Omega(n\log n)
\]

Do đó general comparison sorting không thể có worst-case `O(n)`.

Counting Sort hoặc Radix Sort không mâu thuẫn với kết quả này vì chúng khai thác biểu diễn (representation / 표현) của key, không chỉ comparison.

## Insertion Sort

Insertion Sort duy trì bất biến (invariant / 불변식):

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

Insertion Sort thực hiện lượng công việc liên quan trực tiếp số inversion. Nếu đầu vào (input / 입력) gần sorted, inversion ít và thời gian chạy (runtime / 런타임) có thể gần tuyến tính.

Đây là ví dụ độ phức tạp (complexity / 복잡도) phụ thuộc không chỉ `n` mà còn **độ mất trật tự của đầu vào (input / 입력)**.

Một thuật toán gọi là **adaptive** nếu nó tận dụng cấu trúc (structure / 구조) như “đã gần sorted”.

## Selection Sort

Selection Sort tìm phần tử nhỏ nhất còn lại rồi đổi vào vị trí tiếp theo.

Số comparison gần như luôn:

\[
\frac{n(n-1)}2
\]

nên `Θ(n²)` kể cả đầu vào (input / 입력) đã sorted.

Điểm đáng chú ý là số swap chỉ `O(n)`. Trong môi trường ghi (write / 쓰기) rất đắt, đặc tính này từng có ý nghĩa. Nhưng với software thông thường, quadratic comparisons làm Selection Sort ít hấp dẫn.

## Bubble Sort

Bubble Sort swap các cặp adjacent bị đảo thứ tự.

Giá trị học thuật chính của nó là giúp hiểu:

```text
local repair
inversion
loop invariant
early termination
```

Trong môi trường vận hành (production / 운영 환경), nó hiếm khi là lựa chọn tốt.

Biết nhiều tên sorting thuật toán (algorithm / 알고리즘) không quan trọng bằng hiểu lý do một thuật toán phù hợp với một tải công việc (workload / 워크로드) cụ thể.

## Merge Sort

Merge Sort chia array, sort hai nửa rồi merge.

\[
T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)
\]

Merge bất biến (invariant / 불변식):

> Prefix đầu ra (output / 출력) luôn chứa đúng những phần tử nhỏ nhất đã được lấy từ hai đầu vào (input / 입력) sorted và prefix đó đã có thứ tự.

Một stable merge chọn phần tử bên trái trước khi hai key bằng nhau.

## Vì sao merge là thành phần nguyên thủy (primitive / 기본 요소) mạnh?

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

## Merge Sort trên linked danh sách (list / 목록)

Linked danh sách (list / 목록) không có random truy cập (access / 접근) rẻ nhưng split bằng slow/fast pointers và merge chỉ cần nối lại links.

Vì vậy Merge Sort thường phù hợp Linked danh sách (list / 목록) hơn Quicksort.

Dữ liệu (data / 데이터) biểu diễn (representation / 표현) ảnh hưởng thuật toán (algorithm / 알고리즘) choice.

## Quicksort

Quicksort chọn pivot, partition rồi recurse.

Với pivot tốt hoặc randomized pivot, expected thời gian chạy (runtime / 런타임) thường:

\[
O(n\log n)
\]

Worst-case khi partition liên tục cực lệch:

\[
O(n^2)
\]

Quicksort thường nhanh thực tế trên array vì partition quét dữ liệu contiguous và có locality tốt.

## Partition là trung tâm của Quicksort

Điều khó nhất trong Quicksort không phải recursion mà là đặc tả hợp đồng (contract / 계약) của partition.

### Lomuto

Một bất biến (invariant / 불변식) có thể là:

```text
[left..i]      <= pivot
[i+1..j-1]     > pivot
[j..right-1]   chưa xử lý
```

Sau khi quét xong, pivot được đặt vào vị trí biên đúng.

### Hoare

Hoare partition dùng hai con trỏ đi từ hai phía, tìm phần tử ở sai phía rồi swap.

Nó thường ít swap hơn nhưng đặc tả hợp đồng (contract / 계약) về vị trí trả về khác Lomuto.

Một lỗi phổ biến là lấy partition mã (code / 코드) của một scheme nhưng dùng recursion ranh giới (boundary / 경계) của scheme khác.

## Three-way partition

Nếu nhiều duplicate, two-way partition có thể làm việc thừa.

Dutch National Flag giữ:

```text
< pivot | == pivot | unknown | > pivot
```

Sau partition chỉ recurse hai vùng `<` và `>`.

Nếu toàn bộ array bằng nhau, three-way partition có thể xử lý gần tuyến tính thay vì tạo nhiều recursive lời gọi (call / 호출) vô ích.

## Pivot selection

Chọn đầu/cuối cố định có thể tệ trên đầu vào (input / 입력) sorted hoặc adversarial.

Các chiến lược:

```text
random pivot
median-of-three
sample nhiều phần tử
```

Randomization không làm worst-case biến mất về toán học, nhưng làm fixed adversarial đầu vào (input / 입력) khó ép partition xấu nếu random nguồn (source / 소스) đủ tốt.

## Ngăn xếp (stack / 스택) độ sâu (depth / 깊이) của Quicksort

Nếu recurse vô điều kiện cả hai phía, partition lệch có thể tạo recursion sâu `O(n)`.

Một kỹ thuật là recurse phía nhỏ hơn và lặp phía lớn hơn. Khi đó recursion ngăn xếp (stack / 스택) có thể bị chặn `O(log n)` theo kích thước phía nhỏ, dù tổng thời gian chạy (runtime / 런타임) vẫn phụ thuộc partition chất lượng (quality / 품질).

Đây là ví dụ tối ưu ngăn xếp (stack / 스택) mà không thay ngữ nghĩa (semantics / 의미론) của partition.

## Vùng nhớ vùng nhớ động (heap / 힙) Sort

Vùng nhớ vùng nhớ động (heap / 힙) Sort:

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

với auxiliary bộ nhớ (memory / 메모리) nhỏ.

Sự đánh đổi (trade-off / 트레이드오프) là locality và branch hành vi (behavior / 동작) thường không tốt bằng các hybrid sort hiện đại trên array.

Vùng nhớ vùng nhớ động (heap / 힙) Sort không stable theo hiện thực (implementation / 구현) thông thường.

## Vì sao build-heap là O(n)?

Một upper bound thô `n * O(log n)` cho `O(n log n)`, nhưng quá lỏng.

Phần lớn nút (node / 노드) gần lá và chỉ sift xuống rất ít. Tổng chi phí theo chiều cao:

\[
\sum_{h\ge0}\frac{n}{2^{h+1}}O(h)=O(n)
\]

Đây là ví dụ quan trọng: không thể luôn lấy “số phần tử × worst chi phí (cost / 비용) của một phần tử” để có tight bound.

## Introsort

Introsort kết hợp:

```text
Quicksort cho tốc độ thực tế tốt
Heap Sort làm fallback khi recursion quá sâu
Insertion Sort cho partition rất nhỏ
```

Mục tiêu là giữ ưu điểm average/locality của Quicksort nhưng bảo vệ worst-case `O(n log n)`.

Đây là triết lý phổ biến trong thư viện (library / 라이브러리) thuật toán (algorithm / 알고리즘): **hybrid hóa theo vùng đầu vào (input / 입력) mà mỗi thuật toán mạnh nhất**.

## Timsort: tận dụng run có sẵn

Timsort phát hiện các **run** đã sorted hoặc gần sorted rồi merge chúng theo chính sách (policy / 정책) có kiểm soát.

Nó đặc biệt hiệu quả với dữ liệu thực tế thường đã có cấu trúc, ví dụ timestamp gần thứ tự hoặc danh sách (list / 목록) được chỉnh sửa nhẹ từ trạng thái đã sorted.

Timsort cho thấy một sorting thư viện (library / 라이브러리) tốt không nhất thiết giả định đầu vào (input / 입력) là random; nó có thể khai thác pre-existing thứ tự (order / 순서).

## Counting Sort

Nếu key integer nằm trong miền nhỏ `[0,k)`, ta có thể đếm tần suất:

```text
count[key]++
```

Thời gian chạy (runtime / 런타임):

\[
O(n+k)
\]

Đây không phải comparison sort.

Nếu `k` lớn hơn rất nhiều `n`, bộ nhớ (memory / 메모리)/thời gian (time / 시간) khởi tạo bảng đếm có thể làm nó không phù hợp.

Counting Sort mạnh khi **miền khóa nhỏ và dày đặc**.

## Stable Counting Sort

Muốn dùng Counting Sort làm bước con của Radix Sort, cần thường giữ stability.

Ta chuyển count thành cumulative positions rồi đặt phần tử theo thứ tự thích hợp.

Điều này cho thấy stability có thể trở thành phụ thuộc (dependency / 의존성) tính đúng đắn (correctness / 정확성) của một thuật toán khác, không chỉ preference đầu ra.

## Radix Sort

Radix Sort xử lý key theo từng digit/chunk.

**LSD Radix Sort** từ digit thấp lên cao yêu cầu sort ở mỗi digit phải stable để thứ tự của các digit đã xử lý trước không bị phá.

Nếu có `d` digit và mỗi pass `O(n+k)`:

\[
O(d(n+k))
\]

Khi `d` nhỏ cố định, có thể gần tuyến tính theo `n`.

Nhưng chi phí (cost / 비용) thật còn phụ thuộc biểu diễn (representation / 표현), cơ sở (base / 기반), bộ nhớ đệm (cache / 캐시) và bộ nhớ (memory / 메모리) bandwidth.

## MSD Radix Sort

MSD xử lý digit quan trọng nhất trước rồi recursively chia nhóm.

Nó có thể phù hợp string/prefix-like dữ liệu (data / 데이터) và cho phép dừng sớm khi prefix đủ phân biệt.

LSD và MSD có ngữ nghĩa (semantics / 의미론)/hiện thực (implementation / 구현) sự đánh đổi (trade-off / 트레이드오프) khác nhau; không nên xem Radix Sort như một công thức duy nhất.

## Bucket Sort

Bucket Sort phân phần tử vào các bucket theo phạm vi (range / 범위) rồi sort từng bucket.

Hiệu quả phụ thuộc phân phối (distribution / 분포). Nếu dữ liệu phân bố đều và bucket balance tốt, thời gian chạy (runtime / 런타임) có thể rất tốt. Nếu toàn bộ rơi vào một bucket, lợi ích biến mất.

Đây là ví dụ average-case dựa mạnh vào đầu vào (input / 입력) phân phối (distribution / 분포).

## Bên ngoài (external / 외부) Sorting

Khi dữ liệu lớn hơn RAM, mô hình chi phí thay đổi. I/O theo khối (block / 블록) quan trọng hơn CPU comparison.

Bên ngoài (external / 외부) Merge Sort thường:

```text
1. đọc một chunk vừa RAM
2. sort trong RAM
3. ghi thành sorted run
4. k-way merge các run
```

Mục tiêu là tối đa sequential I/O và giảm số pass trên lưu trữ (storage / 저장소).

Một thuật toán `O(n log n)` trong RAM mô hình (model / 모델) chưa đủ để đánh giá bên ngoài (external / 외부) tải công việc (workload / 워크로드).

## K-way merge

Nếu có `k` sorted runs, dùng min-heap chứa phần tử đầu hiện tại của mỗi run:

```text
extract min
đưa phần tử tiếp theo từ run tương ứng vào heap
```

Thời gian chạy (runtime / 런타임):

\[
O(N\log k)
\]

với `N` tổng số phần tử.

Trong bên ngoài (external / 외부) sorting, `k` còn bị giới hạn bởi buffer bộ nhớ (memory / 메모리) và số stream I/O có thể quản lý hiệu quả.

## Merge phép nối (join / 조인)

Nếu hai bảng đã sorted theo phép nối (join / 조인) key, equi-join có thể quét hai phía theo thứ tự.

Sort ban đầu tốn chi phí, nhưng nếu cùng thứ tự đó được tái sử dụng cho nhiều operator, chi phí tiền xử lý có thể được amortize.

Đây là ví dụ sorting như materialized cấu trúc (structure / 구조) cho chuỗi xử lý (pipeline / 파이프라인) sau.

## Partial sorting và Top-K

Nếu chỉ cần `k` phần tử nhỏ nhất/lớn nhất, sort toàn bộ `n` phần tử có thể thừa.

Các lựa chọn:

```text
heap size k            O(n log k)
Quickselect            expected O(n)
partial sort library   tùy implementation
counting/bucket        nếu key domain phù hợp
```

Mục tiêu đầu ra (output / 출력) ảnh hưởng thuật toán. Không nên sort toàn bộ chỉ vì dữ liệu “cần lấy top”.

## Quickselect

Quickselect dùng partition như Quicksort nhưng chỉ recurse phía chứa rank cần tìm.

Expected thời gian chạy (runtime / 런타임) với pivot phù hợp:

\[
O(n)
\]

Worst-case vẫn `O(n²)` nếu partition liên tục tệ.

Đây là ví dụ cùng thành phần nguyên thủy (primitive / 기본 요소) partition nhưng mục tiêu (objective / 목표) khác làm recursion cây (tree / 트리) thay đổi hoàn toàn.

## Deterministic selection

Median-of-medians cho selection worst-case `O(n)` bằng cách chọn pivot bảo đảm partition không quá tệ.

Nó quan trọng về lý thuyết vì chứng minh selection tuyến tính worst-case là có thể, dù constant factor khiến hiện thực (implementation / 구현) thực tế thường ưu tiên randomized/select hybrid.

## Stable vs unstable: cách tạo stability bổ sung

Nếu thuật toán không stable nhưng cần ngữ nghĩa (semantics / 의미론) stable, có thể decorate key bằng original chỉ mục (index / 인덱스):

```text
(key, originalIndex)
```

rồi sort theo tuple.

Sự đánh đổi (trade-off / 트레이드오프) là thêm bộ nhớ (memory / 메모리)/key comparison chi phí (cost / 비용).

Đây là kỹ thuật chung: khi cấu trúc (structure / 구조) không giữ một thuộc tính (property / 속성), ta có thể mã hóa thuộc tính (property / 속성) đó vào key.

## Sorting đối tượng (object / 객체) lớn và indirect sorting

Nếu bản ghi (record / 레코드) rất lớn, swap/bản sao (copy / 복사) đối tượng (object / 객체) trực tiếp có thể đắt.

Có thể sort:

```text
array of pointers/references
array of indices
small key records
```

rồi dùng thứ tự đó để truy cập payload lớn.

Indirect sorting giảm dữ liệu (data / 데이터) movement nhưng tăng pointer chasing.

Again, biểu diễn (representation / 표현) quyết định hiệu năng.

## Bộ nhớ đệm (cache / 캐시) locality

Merge Sort quét tuyến tính nhưng cần buffer. Quicksort partition quét contiguous region. vùng nhớ động (heap / 힙) Sort truy cập các vị trí theo cây và thường locality kém hơn.

Trên dữ liệu (data / 데이터) lớn, bộ nhớ (memory / 메모리) bandwidth và trượt bộ nhớ đệm (cache miss / 캐시 미스) có thể quyết định nhiều hơn số comparison thuần túy.

Hai thuật toán cùng `O(n log n)` không nhất thiết chạy gần nhau.

## Branch prediction

Comparator và partition tạo nhiều branch phụ thuộc dữ liệu.

Dữ liệu (data / 데이터) phân phối (distribution / 분포) có thể làm branch predictor hoạt động tốt hoặc tệ. Một số high-performance sorting hiện thực (implementation / 구현) dùng branchless techniques hoặc vectorized partition ở mức thấp.

Điểm cần học: Big-O không mô tả branch/bộ nhớ (memory / 메모리) hành vi (behavior / 동작).

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

Sort nhỏ không đáng tạo luồng thực thi (thread / 스레드).

## Phân tán (distributed / 분산) Sorting

Ở quy mô cluster, một mẫu (pattern / 패턴) là phạm vi (range / 범위)/băm (hash / 해시) partition dữ liệu (data / 데이터) giữa worker rồi cục bộ (local / 로컬) sort.

Nếu cần toàn cục (global / 전역) total thứ tự (order / 순서), partition boundaries phải bảo đảm mọi key ở partition trước nhỏ hơn mọi key ở partition sau.

Dữ liệu (data / 데이터) skew có thể làm một worker nhận quá nhiều bản ghi (record / 레코드), tạo hotspot. Sampling splitter hoặc động (dynamic / 동적) partitioning được dùng để giảm skew.

Sorting ở đây trở thành bài toán cả thuật toán (algorithm / 알고리즘) lẫn dữ liệu (data / 데이터) phân phối (distribution / 분포).

## Strings và Unicode

Sorting string không chỉ là `O(n log n)` theo số phần tử. Mỗi comparison có thể phải đọc nhiều ký tự chung ở prefix.

Nếu string dài và có prefix chung, comparison chi phí (cost / 비용) đáng kể.

Unicode còn đặt câu hỏi:

```text
sort theo code unit?
code point?
locale/collation rule?
case-insensitive?
normalized form nào?
```

“Alphabetical thứ tự (order / 순서)” trong nghiệp vụ (business / 비즈니스) software là một specification phức tạp hơn numeric comparator.

## Floating-point và NaN

Floating-point có `NaN`, `-0`, infinities và rounding ngữ nghĩa (semantics / 의미론).

Comparator phải xác định thứ tự (order / 순서) rõ cho các giá trị này nếu chúng có thể xuất hiện. Một comparator không nhất quán với NaN có thể phá total thứ tự (order / 순서).

Thư viện (library / 라이브러리) thường đã có đặc tả hợp đồng (contract / 계약) cụ thể; custom comparator cần theo đúng ngữ nghĩa (semantics / 의미론) mong muốn.

## Sorting và cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스)

B+cây (tree / 트리) chỉ mục (index / 인덱스) duy trì thứ tự incrementally để tránh sort lại toàn bộ mỗi truy vấn (query / 쿼리). Có thể xem chỉ mục (index / 인덱스) như “trả chi phí cập nhật để materialize sorted truy cập (access / 접근) đường dẫn (path / 경로)”.

Nếu tải công việc (workload / 워크로드) chủ yếu đọc theo phạm vi (range / 범위), ordered chỉ mục (index / 인덱스) rất có giá trị. Nếu tải công việc (workload / 워크로드) chỉ chính xác (exact / 정확한) lookup, băm (hash / 해시) chỉ mục (index / 인덱스) có thể hợp hơn.

Sorting và indexing là hai cách khác nhau để trả trước chi phí cho tương lai.

## Sorting mạng (network / 네트워크)

Sorting mạng (network / 네트워크) là chuỗi comparator cố định, không phụ thuộc dữ liệu.

Nó quan trọng trong hardware, SIMD hoặc secure computation vì điều khiển (control / 제어) luồng (flow / 흐름) cố định có thể giảm branch và data-dependent hành vi (behavior / 동작).

Bitonic Sort là ví dụ nổi tiếng.

Dù comparison count thường lớn hơn thuật toán (algorithm / 알고리즘) tốt trên CPU tuần tự, cấu trúc song song và deterministic có thể làm nó phù hợp môi trường đặc biệt.

## Oblivious sorting

Trong một số bảo mật (security / 보안) ngữ cảnh (context / 맥락), không chỉ đầu ra (output / 출력) đúng mà mẫu (pattern / 패턴) truy cập bộ nhớ cũng không được tiết lộ nhiều về dữ liệu.

**Oblivious algorithms** dùng truy cập (access / 접근) mẫu (pattern / 패턴) ít phụ thuộc đầu vào (input / 입력) hơn.

Đây là ví dụ tính đúng đắn (correctness / 정확성)/bảo mật (security / 보안) specification mở rộng vượt ra ngoài “mảng đã sorted”.

## Kiểm thử sorting

Không chỉ kiểm thử (test / 테스트) “đầu ra (output / 출력) tăng dần”. Cần ít nhất:

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

Quicksort cần kiểm thử (test / 테스트) kỹ partition boundaries và duplicate.

## Benchmark sorting

Một benchmark có ý nghĩa cần mô tả phân phối (distribution / 분포) đầu vào (input / 입력):

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

Một “winner” trên random integers có thể không phải lựa chọn tốt nhất cho tải công việc (workload / 워크로드) thật.

## Chọn thuật toán theo tải công việc (workload / 워크로드)

Một bảng định hướng:

| Tình huống | Lựa chọn thường đáng cân nhắc |
|---|---|
| dữ liệu (data / 데이터) nhỏ hoặc gần sorted | Insertion Sort / hybrid |
| General in-memory array | thư viện (library / 라이브러리) hybrid sort |
| Cần stable | stable Merge/Timsort-style |
| Cần worst-case comparison bound, ít bộ nhớ (memory / 메모리) | vùng nhớ động (heap / 힙) Sort / Introsort fallback |
| Nhiều duplicate | three-way partition / adaptive stable sort |
| Integer key miền nhỏ | Counting Sort |
| Fixed-width integer/string chunks | Radix Sort |
| Dữ liệu vượt RAM | bên ngoài (external / 외부) Merge Sort |
| Chỉ cần Top-K | vùng nhớ động (heap / 힙) / selection |
| Linked danh sách (list / 목록) | Merge Sort thường tự nhiên |

Bảng này không thay profiling và Đặc tả API (API contract / API 계약).

## Những hiểu lầm phổ biến

“Quicksort luôn nhanh nhất” — sai; tải công việc (workload / 워크로드) và hiện thực (implementation / 구현) quyết định.

“`O(n log n)` nào cũng gần nhau” — sai vì locality, branch, allocation và stability khác nhau.

“Stable chỉ là tính chất phụ” — có thể là một phần tính đúng đắn (correctness / 정확성) của multi-key sorting.

“Counting Sort phá cận dưới `n log n`” — cận dưới đó chỉ áp dụng comparison sorting.

“Sort toàn bộ luôn cần nếu muốn Top-K” — sai.

“thư viện (library / 라이브러리) sort dùng một thuật toán duy nhất” — nhiều thư viện dùng hybrid chiến lược (strategy / 전략) tùy kiểu dữ liệu, kích thước và thời gian chạy (runtime / 런타임).

## Mô hình tư duy

> Sorting là quá trình trả một chi phí để xây dựng **trật tự có thể tái sử dụng**. Chọn sorting thuật toán (algorithm / 알고리즘) là chọn cách cân bằng comparison, dữ liệu (data / 데이터) movement, bộ nhớ (memory / 메모리), stability, đầu vào (input / 입력) cấu trúc (structure / 구조) và môi trường lưu trữ.

Khi cần sort, hãy hỏi: **comparator có total thứ tự (order / 순서) đúng không, stability có phải yêu cầu (requirement / 요구사항) không, đầu vào (input / 입력) có cấu trúc (structure / 구조) nào tận dụng được không, có thật sự cần sort toàn bộ không, key lĩnh vực (domain / 도메인) có cho phép non-comparison sort không, và bottleneck là CPU comparison hay dữ liệu (data / 데이터) movement/I/O?**

Xem tiếp: [Searching](./00_searching.md), [Divide and Conquer](./03_divide_and_conquer.md), [Selection & Top-K](./06_selection_and_top_k.md), [Intervals & Sweep Line](./08_intervals_and_sweep_line.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md) và [Cross-language Testing](../80_language_implementations/03_cross_language_testing_and_benchmarking.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 searching](./00_searching.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
