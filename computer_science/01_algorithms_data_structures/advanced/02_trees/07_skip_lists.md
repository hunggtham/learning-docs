# Skip List
**스킵 리스트 / Skip List**

Skip List là cấu trúc set/map có thứ tự, cung cấp tìm kiếm/chèn/xóa với chi phí kỳ vọng `O(log n)` nhưng không dùng phép xoay như AVL hoặc Red-Black Tree. Thay vào đó, nó duy trì nhiều tầng danh sách liên kết với mật độ giảm dần và dùng tính ngẫu nhiên để tạo các “làn đường nhanh”.

Skip List quan trọng không chỉ vì nó là một alternative cho balanced BST. Nó minh họa một tư tưởng lớn hơn:

> Ta có thể đạt tìm kiếm logarit bằng một **phân cấp nhiều độ phân giải** của cùng một dãy đã sắp xếp, trong đó tầng cao bỏ qua nhiều phần tử còn tầng thấp giữ đầy đủ thứ tự.

## Từ sorted danh sách liên kết tới express lanes

Một danh sách liên kết đơn đã sắp xếp vẫn tìm kiếm `O(n)` vì chỉ có thể đi qua từng nút.

Nếu tạo tầng 1 chứa khoảng một nửa các nút, tầng 2 khoảng một phần tư, tầng 3 khoảng một phần tám, search có thể nhảy xa ở các tầng cao rồi refine dần.

```text
L3: 1 ------------------------- 20
L2: 1 -------- 9 -------------- 20
L1: 1 --- 4 -- 9 ---- 15 ------ 20
L0: 1 2 3 4 5  9 10  15 18 19 20
```

Tìm kiếm bắt đầu ở tầng cao nhất. Nếu khóa của nút kế tiếp vẫn nhỏ hơn đích thì đi sang phải; nếu nút kế tiếp vượt đích hoặc là `null` thì đi xuống một tầng.

mẫu này giống tìm kiếm nhị phân ở tinh thần “coarse-to-fine”, nhưng cách biểu diễn (representation) là linked hierarchy thay vì contiguous mảng.

## nút cách biểu diễn

Một nút thường giữ:

```text
key
value
forward[0..height-1]
```

Sentinel head có maximum configured tầng.

C sketch:

```c
typedef struct SkipNode {
    int key;
    int level;
    struct SkipNode **next;
} SkipNode;
```

Trong hệ thống thực tế, cách triển khai có thể cấp phát nút + forward các con trỏ trong một block để giảm các lần cấp phát/indirection.

## Search bất biến (invariant)

Tại mỗi tầng, ta duy trì rằng `cur.key < target` và `cur` là nút xa nhất đã biết ở tầng đó mà chưa vượt đích.

Khi `cur.next[level].key < target`, ta có thể đi sang phải an toàn. Khi nút kế tiếp có khóa `>=` đích, không còn nút nào ở xa hơn trên cùng tầng nhưng nằm trước nút đó cần xét, vì vậy ta đi xuống tầng dưới.

JavaScript:

```js
function find(head, maxLevel, key) {
  let cur = head;

  for (let level = maxLevel; level >= 0; level--) {
    while (cur.next[level] && cur.next[level].key < key) {
      cur = cur.next[level];
    }
  }

  cur = cur.next[0];
  return cur && cur.key === key ? cur : null;
}
```

tính đúng đắn cuối cùng đến từ tầng 0 chứa toàn bộ sorted sequence.

## ngẫu nhiên chiều cao

Khi insert nút, chọn chiều cao ngẫu nhiên. Một scheme phổ biến: bắt đầu tầng 0, mỗi lần coin flip success với xác suất `p` thì promote thêm một tầng.

xác suất nút đạt ít nhất tầng `k` xấp xỉ:

\[
p^k
\]

Với `p=1/2`, kỳ vọng các nút ở tầng `k`:

\[
n\left(\frac12\right)^k
\]

tầng cao nhất đáng kể khi quantity gần 1:

\[
n/2^k\approx1
\Rightarrow k\approx\log_2 n
\]

Đây là nguồn gốc kỳ vọng logarithmic chiều cao.

## kỳ vọng search chi phí intuition

Ở tầng cao, các nút thưa nên ta nhảy khoảng lớn. Khi descend, ta chỉ cần đi một số kỳ vọng constant steps ngang trước khi lại gặp promoted nút phù hợp.

Có khoảng `O(log n)` các tầng và kỳ vọng horizontal work mỗi tầng bounded, nên kỳ vọng search `O(log n)`.

Đây là kỳ vọng analysis; một ngẫu nhiên outcome cực xấu vẫn có thể xảy ra.

## Insert và predecessor đường đi

Khi tìm vị trí chèn, cần lưu nút liền trước ở mỗi tầng:

```text
update[level] = node cuối cùng có key < newKey tại level đó
```

Sau khi randomize new nút chiều cao:

```text
new.next[level] = update[level].next[level]
update[level].next[level] = new
```

cho mọi tầng nút tham gia.

Pseudo:

```java
Node[] update = new Node[MAX_LEVEL];
Node cur = head;

for (int level = currentMax; level >= 0; level--) {
    while (cur.next[level] != null && cur.next[level].key < key) {
        cur = cur.next[level];
    }
    update[level] = cur;
}
```

Nếu khóa tồn tại, map ngữ nghĩa (semantics) có thể cập nhật giá trị hoặc reject phần tử trùng tùy contract.

## Delete

Khi xóa, ta tìm cùng đường đi và lưu các nút liền trước. Nếu đích tồn tại ở tầng 0, với mỗi tầng:

```text
nếu update[level].next[level] == target:
    update[level].next[level] = target.next[level]
```

Sau đó có thể giảm hiện tại maximum tầng nếu top các tầng trở thành rỗng.

Thao tác xóa của **Skip List** mang tính cục bộ hơn các phép xoay cây; đây là một lý do cấu trúc này hấp dẫn trong một số thiết kế xử lý đồng thời.

## phần tử trùng chính sách

Ordered set có thể reject phần tử trùng khóa. Ordered multiset có thể lưu count hoặc cho nhiều các nút equal các khóa với quy tắc phân xử khi bằng nhau quy tắc. Map cập nhật existing giá trị.

Tìm kiếm, chèn, xóa và duyệt theo khoảng phải dùng cùng ngữ nghĩa bộ so sánh. Nếu cách xử lý phần tử trùng không rõ ràng, các thao tác cận dưới hoặc truy vấn hạng rất dễ sai.

## hợp đồng bộ so sánh

Skip list dựa trên thứ tự toàn phần giống BST. Comparator phải consistent và transitive.

Nếu bộ so sánh xem hai khóa khác nhau về mặt nghiệp vụ là bằng nhau (`compare(a,b)==0`), cấu trúc sẽ coi chúng nằm ở cùng một vị trí thứ tự theo hợp đồng API.

Floating-point NaN, case-insensitive strings, locale order hoặc composite các khóa cần ngữ nghĩa rõ ràng.

## cận dưới và quét theo khoảng

Tìm kiếm có thể trả nút đầu tiên có khóa `>= key`, tức cận dưới.

Sau khi tìm start kỳ vọng `O(log n)`, quét theo khoảng đi tầng 0 sequentially:

```text
O(log n + k)
```

với `k` các đầu ra.

Đây là ordered-map capability tương tự balanced cây.

## Predecessor và successor

Successor dễ: nút tiếp theo ở tầng 0.

Predecessor có thể lấy từ đường tìm kiếm (`update[0]`). Nếu API cần bidirectional iteration hiệu quả, nút có thể giữ backward con trỏ tầng 0 hoặc maintain doubly-linked base tầng, đổi thêm bộ nhớ/cập nhật chi phí.

## Indexed Skip List

Skip List có thể được tăng cường bằng **độ dài nhảy (span/width)** trên mỗi con trỏ tiến: số nút ở tầng 0 mà con trỏ đó bỏ qua.

Sau đó, tìm kiếm theo hạng có thể trừ dần các độ dài nhảy (span), tương tự cây thống kê thứ tự sử dụng kích thước cây con.

Example conceptual mục:

```text
next[level]
span[level]
```

Muốn tìm k-th item, đi right nếu span không vượt rank đích; nếu vượt thì descend.

kỳ vọng `O(log n)` rank/select.

Đây là connection trực tiếp với [Augmented Trees](./06_augmented_trees_and_order_statistics.md): cả hai lưu dữ liệu tóm lược để skip một region và biết region đóng góp bao nhiêu.

## Weighted spans

Span không nhất thiết chỉ đếm số nút. Nó có thể lưu trọng số tích lũy, điểm số hoặc số byte để điều hướng theo vị trí có trọng số trong các cấu trúc chuyên biệt.

Mô hình tư duy là forward cạnh mang dữ liệu tóm lược của segment mà cạnh bỏ qua.

## Skip List vs balanced BST

Cả hai hỗ trợ từ điển có thứ tự các thao tác kỳ vọng/xác định logarithmic theo variant.

Balanced BST:

```text
deterministic balance invariant
rotations/recoloring
usually fewer forward pointers per node
hard worst-case bounds
```

Skip List:

```text
randomized height
simple local splice logic
expected logarithmic bounds
more pointer slots / probabilistic shape
```

Không có universal winner. môi trường chạy (runtime) bộ nhớ bố trí, concurrency, cách triển khai complexity và độ trễ (latency) các bảo đảm quyết định.

## kỳ vọng vs trường hợp xấu nhất bảo đảm

Chi phí kỳ vọng `O(log n)` của Skip List không phải bảo đảm xác định cho trường hợp xấu nhất. Trong kết quả ngẫu nhiên cực đoan, nhiều nút có thể chỉ ở tầng 0 và quá trình tìm kiếm gần tuyến tính.

mã dùng trong hệ thống thực tế thường set maximum tầng để bound siêu dữ liệu và use good ngẫu nhiên generation.

Nếu hard trường hợp xấu nhất độ trễ là yêu cầu, xác định balanced cây có argument mạnh hơn.

## xác suất parameter `p`

`p` điều khiển sự đánh đổi (trade-off):

- `p` lớn -> nhiều promoted các nút, nhiều bộ nhớ/các con trỏ, ít horizontal steps;
- `p` nhỏ -> ít bộ nhớ, nhiều horizontal movement.

`p=1/2` phổ biến vì đơn giản, nhưng other các giá trị có thể được chọn theo bộ nhớ đệm/bộ nhớ sự đánh đổi.

kỳ vọng number of forward các con trỏ per nút liên quan geometric phân phối và xấp xỉ constant:

\[
1+p+p^2+\cdots = \frac1{1-p}
\]

với lập chỉ mục convention thích hợp.

Với `p=1/2`, số con trỏ kỳ vọng trên mỗi nút là một hằng số nhỏ, dù một số nút có thể cao hơn nhiều.

## ngẫu nhiên tầng generation bằng bits

Nếu `p=1/2`, ngẫu nhiên chiều cao có thể lấy từ số consecutive coin successes hoặc bit các mẫu. Low-level code có thể dùng count-trailing/leading-zero style trên ngẫu nhiên bits.

Nhưng random-number quality và bias phải phù hợp. Optimization bit trick không đáng nếu làm phân phối sai.

## xác định skip structures

Có các biến thể xác định sử dụng quy tắc nâng tầng thay cho tính ngẫu nhiên, nhưng độ phức tạp và đặc điểm bảo trì khác với Skip List trong mô hình kinh điển.

Điểm học chính: multi-level linked lập chỉ mục không bắt buộc probabilistic về bản chất; randomness là một cách rẻ để đạt phân phối tốt kỳ vọng.

## Redis-like composition intuition

Sorted-set các hệ thống thường cần both chính xác member tra cứu và ordered-by-score các thao tác. Một design natural là kết hợp:

```text
hash map: member -> metadata/node
ordered structure: score -> sequence
```

Skip list historically xuất hiện trong hệ thống thực tế ordered-set các cách triển khai vì quét theo khoảng và cục bộ các cập nhật tốt.

Bài học quan trọng hơn specific product/version là **composition**: một structure không nhất thiết phục vụ mọi truy vấn class.

## Skip list và LSM/memtable

Một số bộ máy lưu trữ dùng memtable có thứ tự kiểu Skip List: các lần ghi đi vào cấu trúc có thứ tự trong bộ nhớ, hỗ trợ quét khoảng đã sắp xếp, rồi được ghi xuống thành các tệp bất biến đã sắp xếp.

Skip list phù hợp khi cần chèn động cùng khả năng duyệt theo thứ tự. Các lựa chọn thay thế có thể là cây cân bằng, cây hỗ trợ xử lý đồng thời hoặc những cấu trúc có thứ tự khác.

Đây là connection giữa DSA và cơ sở dữ liệu/storage-engine write đường đi.

## bộ nhớ tính cục bộ (locality)

Skip List kinh điển dùng nhiều con trỏ hơn bố trí mảng hoặc trang B-tree. Tìm kiếm phải nhảy giữa các đối tượng trên heap nên có thể gây nhiều lần trượt bộ nhớ đệm.

Nếu cách triển khai allocates các nút/forward các mảng compactly hoặc uses arena, tính cục bộ cải thiện. Nhưng generally B-tree-like high-fanout structures tốt hơn bên ngoài bộ nhớ/bộ nhớ đệm page hành vi.

Big-O logarithmic không kể pointer-chasing chi phí.

## bộ nhớ overhead

Mỗi nút có base các trường + variable forward các con trỏ. kỳ vọng con trỏ count constant nhưng overhead/nút có thể lớn so với gọn mảng đã sắp xếp.

Nếu dataset tĩnh/read-heavy, mảng đã sắp xếp + tìm kiếm nhị phân có thể memory-efficient và thân thiện với bộ nhớ đệm hơn rất nhiều.

Skip List mạnh khi cần cập nhật động đồng thời duy trì thứ tự.

## Concurrency motivation

Các phép xoay trong cây cân bằng làm thay đổi cấu trúc liên kết cục bộ theo những mẫu tương đối phức tạp. Chèn/xóa trong skip list chủ yếu dùng CAS hoặc nối lại các con trỏ tiến ở từng tầng, vì vậy cấu trúc này thuận lợi cho một số thuật toán không khóa (lock-free) hoặc xử lý đồng thời.

Tuy nhiên “thuận lợi hơn” không có nghĩa dễ.

Concurrent Skip List phải xử lý:

```text
node đang insert dở ở vài levels
node logically deleted nhưng chưa unlinked hết
reader đồng thời traverse
ABA/memory reclamation
ordering của atomic writes
```

tính đúng đắn cần linearization point rõ.

## logic deletion và vật lý unlink

Concurrent designs thường tách:

```text
logical delete: mark node không còn thuộc abstract set
physical delete: unlink pointers để cleanup
```

thao tác có thể linearize tại mark, còn cleanup giúp tương lai traversal nhưng không thay trừu tượng ngữ nghĩa.

mẫu này phổ biến trong không khóa structures.

## thu hồi bộ nhớ (memory reclamation)

Ngay cả sau khi một nút đã bị tháo khỏi cấu trúc, luồng đọc khác vẫn có thể đang giữ con trỏ tới nó. Giải phóng ngay có thể dẫn đến lỗi truy cập bộ nhớ sau khi giải phóng (use-after-free).

Techniques gồm con trỏ nguy hiểm, epoch-based reclamation, tham chiếu counting hoặc GC-môi trường chạy có quản lý.

Trong Java, GC loại bỏ một nhóm lỗi liên quan đến thu hồi bộ nhớ, nhưng thứ tự nguyên tử và khả năng nhìn thấy dữ liệu giữa các luồng vẫn phải được xử lý đúng.

## Java ConcurrentSkipListMap

Java cung cấp `ConcurrentSkipListMap` và `ConcurrentSkipListSet` cho các thao tác có thứ tự trong môi trường đồng thời. Điều quan trọng là hiểu ngữ nghĩa API: vừa điều hướng theo thứ tự vừa hỗ trợ xử lý đồng thời, chứ không nên xem chúng đơn giản là “TreeMap nhưng nhanh hơn”.

sự đánh đổi bộ nhớ/constants và concurrent khối lượng công việc phải được profile.

## Persistent Skip List?

Sao chép theo đường đi trên cây tự nhiên hơn cho tính bền vững (persistence) vì đường nhánh rõ ràng. Skip List có nhiều con trỏ tiến cắt qua nhiều nút; vẫn có thể làm cấu trúc bền vững nhưng việc chia sẻ cấu trúc và cập nhật thường phức tạp hơn một số loại cây.

Nếu versioning là yêu cầu chính, persistent balanced/functional cây thường natural hơn.

## Skip đồ thị và distributed variants

Ý tưởng liên kết ngẫu nhiên nhiều tầng có họ hàng với các cấu trúc phủ và tìm kiếm phân tán. Giao thức cụ thể khác Skip List trong bộ nhớ, nhưng trực giác về phân cấp và định tuyến xác suất có liên hệ.

Điều này cho thấy design mẫu “sparse các liên kết nhảy nhanh” có thể scale beyond one xử lý.

## dạng lỗi: off-by-one tầng conventions

Một triển khai có thể gọi tầng cơ sở là 0; khi đó “chiều cao tối đa `h`” có thể nghĩa là các tầng `0..h`, hoặc “số tầng `h`” có thể nghĩa là `0..h-1`. Cần thống nhất quy ước.

Mix conventions dễ gây mảng out-of-bounds hoặc miss top-level link.

Nên define rõ:

```text
height = number of levels in node
valid levels = 0 .. height-1
```

hoặc một convention khác nhưng consistent.

## Dạng lỗi: độ dài mảng con trỏ tiến của nút

Khi traversal ở tầng `L`, hiện tại nút phải có con trỏ ô `L`. Chuẩn design đảm bảo chỉ các nút hiện có at that tầng được traversal, giá trị canh gác (sentinel) has max các tầng.

Mã trong ngôn ngữ động có thể che giấu một số lỗi cấu trúc; mã kiểu tĩnh hoặc mức thấp có thể gặp lỗi nghiêm trọng nếu truy cập vượt mảng con trỏ tiến đã được cấp phát.

## dạng lỗi: ngẫu nhiên seed/kiểm thử

ngẫu nhiên shape làm bug khó reproduce. Tests nên cho phép xác định seed hoặc inject bộ sinh tầng ngẫu nhiên.

Sau đó failing sequence có thể replay chính xác structure.

Trong hệ thống thực tế, tính ngẫu nhiên khi chạy và tính ngẫu nhiên có thể tái lập trong kiểm thử là hai mối quan tâm khác nhau.

## xác minh

Validator có thể kiểm tra:

```text
level 0 sorted strictly/non-strictly theo duplicate policy
every higher-level node cũng tồn tại level 0
each level sorted
forward link level không đi tới node có insufficient height
currentMaxLevel khớp top non-empty level
size/count đúng
```

Skip list có chỉ mục còn phải tính lại các span theo khoảng cách ở tầng cơ sở.

## Differential kiểm thử

tham chiếu có thể là `TreeMap`, mảng đã sắp xếp/list hoặc multiset cách triển khai.

ngẫu nhiên chuỗi thao tác:

```text
insert
remove
contains
lowerBound
range scan
rank/select nếu augmented
```

so các kết quả với tham chiếu after every batch.

Randomization của structure không ảnh hưởng trừu tượng ngữ nghĩa, nên differential kiểm thử rất phù hợp.

## Benchmarking

Benchmark Skip List vs cây phải tách khối lượng công việc:

```text
random lookup
sequential range scan
insert-heavy
mixed read/write
concurrent contention
memory footprint
```

A single phép đo hiệu năng vi mô “100k gets” không nói hết sự đánh đổi.

Dataset size so với CPU bộ nhớ đệm cũng có thể đổi kết quả đáng kể.

## Khi nào nên cân nhắc Skip List

Nên cân nhắc Skip List khi cần ánh xạ hoặc tập hợp có thứ tự và cập nhật động, cần duyệt theo khoảng, muốn tránh độ phức tạp của phép xoay cây, hoặc khi thiết kế đồng thời hưởng lợi từ việc nối lại con trỏ mang tính cục bộ.

Nếu tập dữ liệu tĩnh, mảng đã sắp xếp thường đơn giản và có tính cục bộ tốt. Nếu bài toán theo mô hình bộ nhớ ngoài hoặc theo trang, B+Tree mạnh hơn. Nếu chỉ cần tra cứu chính xác theo quan hệ bằng nhau, bảng băm thường phù hợp. Nếu bắt buộc có cận xác định cho trường hợp xấu nhất, cây cân bằng xác định rõ ràng hơn.

## Những hiểu lầm phổ biến

“Skip List là danh sách liên kết nên tìm kiếm tuyến tính” là sai vì cấu trúc phân tầng làm thay đổi đường tìm kiếm kỳ vọng.

“kỳ vọng `O(log n)` nghĩa mỗi thao tác chắc chắn logarithmic” sai.

“Concurrency dễ hơn cây nghĩa cách triển khai không khóa đơn giản” sai; reclamation và atomic protocol vẫn phức tạp.

“ngẫu nhiên promotion càng nhiều càng nhanh” sai vì bộ nhớ/bộ nhớ đệm overhead tăng và có phương án tối ưu sự đánh đổi.

“Skip List chỉ là academic structure” sai; ordered concurrent/lập chỉ mục khối lượng công việc đã dùng variants trong real các hệ thống.

## Mô hình tư duy

> Skip List không cân bằng cây; nó điều chỉnh **mật độ các liên kết nhảy nhanh** bằng tính ngẫu nhiên. Tầng 0 giữ đầy đủ dữ liệu, các tầng cao là những chỉ mục thưa của cùng dãy đã sắp xếp. Tìm kiếm đi từ độ phân giải thô xuống độ phân giải mịn, còn chèn/xóa chỉ nối lại những liên kết mà nút tham gia.

Khi đánh giá Skip List, hãy hỏi: **kỳ vọng bảo đảm có đủ không, quét theo khoảng có quan trọng không, bộ nhớ/con trỏ tính cục bộ thế nào, concurrency có cần không, và comparator/phần tử trùng ngữ nghĩa có rõ không?**

Xem tiếp: [Linked Lists](../01_linear_structures/01_linked_lists.md), [Balanced Search Trees](./02_balanced_search_trees.md), [Augmented Trees](./06_augmented_trees_and_order_statistics.md), [B-Tree & External Memory](./05_b_trees_and_external_memory.md) và [Amortized & Randomized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md).
