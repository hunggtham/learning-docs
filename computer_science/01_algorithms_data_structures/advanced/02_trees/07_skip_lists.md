# Skip List
**스킵 리스트 / Skip List**

Skip List là một ordered-set/map structure cung cấp expected `O(log n)` search/insert/delete nhưng không dùng rotations như AVL/Red-Black Tree. Thay vào đó, nó duy trì nhiều linked-list levels với mật độ giảm dần và dùng randomness để tạo các “express lanes”.

Skip List quan trọng không chỉ vì nó là một alternative cho balanced BST. Nó minh họa một tư tưởng lớn hơn:

> Ta có thể đạt search logarithmic bằng một **hierarchy nhiều độ phân giải** của cùng sorted sequence, trong đó tầng cao bỏ qua nhiều phần tử và tầng thấp giữ exact order.

## Từ sorted linked list tới express lanes

Một sorted singly linked list search `O(n)` vì chỉ có thể đi từng node.

Nếu tạo level 1 chứa khoảng một nửa nodes, level 2 khoảng một phần tư, level 3 khoảng một phần tám, search có thể nhảy xa ở levels cao rồi refine dần.

```text
L3: 1 ------------------------- 20
L2: 1 -------- 9 -------------- 20
L1: 1 --- 4 -- 9 ---- 15 ------ 20
L0: 1 2 3 4 5  9 10  15 18 19 20
```

Search bắt đầu ở highest level. Nếu next key vẫn nhỏ hơn target thì đi right. Nếu next vượt target hoặc null thì đi xuống một level.

Pattern này giống binary search ở tinh thần “coarse-to-fine”, nhưng representation là linked hierarchy thay vì contiguous array.

## Node representation

Một node thường giữ:

```text
key
value
forward[0..height-1]
```

Sentinel head có maximum configured level.

C sketch:

```c
typedef struct SkipNode {
    int key;
    int level;
    struct SkipNode **next;
} SkipNode;
```

Production implementation có thể allocate node + forward pointers trong một block để giảm allocations/indirection.

## Search invariant

Tại mỗi level, ta duy trì rằng `cur.key < target` và `cur` là node xa nhất đã biết ở level đó mà chưa vượt target.

Khi `cur.next[level].key < target`, đi right an toàn. Khi next >= target, không node nào xa hơn ở cùng level nhưng trước next cần xét, nên descend.

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

Correctness cuối cùng đến từ level 0 chứa toàn bộ sorted sequence.

## Random height

Khi insert node, chọn height random. Một scheme phổ biến: bắt đầu level 0, mỗi lần coin flip success với probability `p` thì promote thêm một level.

Probability node đạt ít nhất level `k` xấp xỉ:

\[
p^k
\]

Với `p=1/2`, expected nodes ở level `k`:

\[
n\left(\frac12\right)^k
\]

Level cao nhất đáng kể khi quantity gần 1:

\[
n/2^k\approx1
\Rightarrow k\approx\log_2 n
\]

Đây là nguồn gốc expected logarithmic height.

## Expected search cost intuition

Ở level cao, nodes thưa nên ta nhảy khoảng lớn. Khi descend, ta chỉ cần đi một số expected constant steps ngang trước khi lại gặp promoted node phù hợp.

Có khoảng `O(log n)` levels và expected horizontal work mỗi level bounded, nên expected search `O(log n)`.

Đây là expected analysis; một random outcome cực xấu vẫn có thể xảy ra.

## Insert và predecessor path

Search cho insert cần lưu predecessor ở mỗi level:

```text
update[level] = node cuối cùng có key < newKey tại level đó
```

Sau khi randomize new node height:

```text
new.next[level] = update[level].next[level]
update[level].next[level] = new
```

cho mọi level node tham gia.

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

Nếu key tồn tại, map semantics có thể update value hoặc reject duplicate tùy contract.

## Delete

Delete search cùng predecessor path. Nếu target ở level 0, với mỗi level:

```text
nếu update[level].next[level] == target:
    update[level].next[level] = target.next[level]
```

Sau đó có thể giảm current maximum level nếu top levels trở thành empty.

Deletion local hơn tree rotations, một lý do skip list attractive trong some concurrent designs.

## Duplicate policy

Ordered set có thể reject duplicate key. Ordered multiset có thể lưu count hoặc cho nhiều nodes equal keys với tie-breaking rule. Map update existing value.

Search/insert/delete/range iteration phải dùng cùng comparator semantics. Nếu duplicate handling không rõ, lower-bound/rank operations dễ sai.

## Comparator contract

Skip list dựa trên total order giống BST. Comparator phải consistent và transitive.

Nếu comparator coi hai domain-distinct keys equal (`compare(a,b)==0`), structure sẽ treat chúng cùng order position theo API design.

Floating-point NaN, case-insensitive strings, locale order hoặc composite keys cần semantics rõ ràng.

## Lower bound và range scan

Search có thể trả first node `>= key`, tức lower bound.

Sau khi tìm start expected `O(log n)`, range scan đi level 0 sequentially:

```text
O(log n + k)
```

với `k` outputs.

Đây là ordered-map capability tương tự balanced tree.

## Predecessor và successor

Successor dễ: node tiếp theo ở level 0.

Predecessor có thể lấy từ search path (`update[0]`). Nếu API cần bidirectional iteration hiệu quả, node có thể giữ backward pointer level 0 hoặc maintain doubly-linked base level, đổi thêm memory/update cost.

## Indexed Skip List

Một skip list có thể được augment bằng **span/width** trên mỗi forward pointer: số level-0 nodes pointer đó bỏ qua.

Then search theo rank có thể trừ spans giống order-statistics tree dùng subtree sizes.

Example conceptual entry:

```text
next[level]
span[level]
```

Muốn tìm k-th item, đi right nếu span không vượt rank target; nếu vượt thì descend.

Expected `O(log n)` rank/select.

Đây là connection trực tiếp với [Augmented Trees](./06_augmented_trees_and_order_statistics.md): cả hai lưu summary để skip một region và biết region đóng góp bao nhiêu.

## Weighted spans

Span không nhất thiết count nodes. Có thể lưu cumulative weight, score hoặc byte length để navigate theo weighted position trong specialized structures.

Mental model là forward edge mang summary của segment mà edge bỏ qua.

## Skip List vs balanced BST

Cả hai hỗ trợ ordered dictionary operations expected/deterministic logarithmic theo variant.

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

Không có universal winner. Runtime memory layout, concurrency, implementation complexity và latency guarantees quyết định.

## Expected vs worst-case guarantee

Skip List expected `O(log n)` không phải deterministic worst-case. Trong extreme random outcome, nhiều nodes có thể ở level 0 và search gần linear.

Production code thường set maximum level để bound metadata và use good random generation.

Nếu hard worst-case latency là requirement, deterministic balanced tree có argument mạnh hơn.

## Probability parameter `p`

`p` điều khiển trade-off:

- `p` lớn -> nhiều promoted nodes, nhiều memory/pointers, ít horizontal steps;
- `p` nhỏ -> ít memory, nhiều horizontal movement.

`p=1/2` phổ biến vì đơn giản, nhưng other values có thể được chọn theo cache/memory trade-off.

Expected number of forward pointers per node liên quan geometric distribution và xấp xỉ constant:

\[
1+p+p^2+\cdots = \frac1{1-p}
\]

với indexing convention thích hợp.

Với `p=1/2`, expected pointer count là small constant, dù một số nodes cao hơn nhiều.

## Random level generation bằng bits

Nếu `p=1/2`, random height có thể lấy từ số consecutive coin successes hoặc bit patterns. Low-level code có thể dùng count-trailing/leading-zero style trên random bits.

Nhưng random-number quality và bias phải phù hợp. Optimization bit trick không đáng nếu làm distribution sai.

## Deterministic skip structures

Có deterministic variants dùng promotion rules thay randomness, nhưng complexity/maintenance semantics khác textbook Skip List.

Điểm học chính: multi-level linked indexing không bắt buộc probabilistic về bản chất; randomness là một cách rẻ để đạt distribution tốt expected.

## Redis-like composition intuition

Sorted-set systems thường cần both exact member lookup và ordered-by-score operations. Một design natural là combine:

```text
hash map: member -> metadata/node
ordered structure: score -> sequence
```

Skip list historically xuất hiện trong production ordered-set implementations vì range scan và local updates tốt.

Lesson quan trọng hơn specific product/version là **composition**: một structure không nhất thiết phục vụ mọi query class.

## Skip list và LSM/memtable

Some storage engines use skip-list-like ordered memtables: writes vào in-memory ordered structure, range scan sorted, rồi flush thành immutable sorted files.

Skip list phù hợp vì insert dynamic + ordered iteration. Alternative có thể là balanced tree, concurrent tree hoặc other structures.

Đây là connection giữa DSA và database/storage-engine write path.

## Memory locality

Classic skip list pointer-rich hơn array/B-tree page layout. Search nhảy qua heap objects có thể gây cache misses.

Nếu implementation allocates nodes/forward arrays compactly hoặc uses arena, locality cải thiện. Nhưng generally B-tree-like high-fanout structures tốt hơn external memory/cache page behavior.

Big-O logarithmic không kể pointer-chasing cost.

## Memory overhead

Mỗi node có base fields + variable forward pointers. Expected pointer count constant nhưng overhead/node có thể lớn so với compact sorted array.

Nếu dataset static/read-heavy, sorted array + binary search có thể memory-efficient và cache-friendly hơn rất nhiều.

Skip List mạnh khi cần dynamic updates + order.

## Concurrency motivation

Rotations trong balanced tree thay đổi local topology theo patterns khá intricate. Skip list insert/delete chủ yếu CAS/splice forward pointers ở levels, nên có structure thuận lợi cho lock-free/concurrent algorithms.

Tuy nhiên “thuận lợi hơn” không có nghĩa dễ.

Concurrent Skip List phải xử lý:

```text
node đang insert dở ở vài levels
node logically deleted nhưng chưa unlinked hết
reader đồng thời traverse
ABA/memory reclamation
ordering của atomic writes
```

Correctness cần linearization point rõ.

## Logical deletion và physical unlink

Concurrent designs thường tách:

```text
logical delete: mark node không còn thuộc abstract set
physical delete: unlink pointers để cleanup
```

Operation có thể linearize tại mark, còn cleanup giúp future traversal nhưng không thay abstract semantics.

Pattern này phổ biến trong lock-free structures.

## Memory reclamation

Ngay cả sau khi node unlinked, reader khác có thể vẫn giữ pointer. Free ngay có thể use-after-free.

Techniques gồm hazard pointers, epoch-based reclamation, reference counting hoặc GC-managed runtime.

Trong Java, GC loại một class memory-reclamation bugs nhưng atomic ordering/visibility vẫn cần correctness.

## Java ConcurrentSkipListMap

Java cung cấp `ConcurrentSkipListMap`/`ConcurrentSkipListSet` cho sorted concurrent operations. Điểm đáng học là API semantics: ordered navigation + concurrency, không phải xem nó như “TreeMap nhưng nhanh hơn”.

Trade-off memory/constants và concurrent workload phải được profile.

## Persistent Skip List?

Path-copying tree tự nhiên hơn persistence vì branch path rõ. Skip list có multiple forward links crossing many nodes; persistence có thể thực hiện nhưng structural sharing/update complexity không đẹp bằng some tree structures.

Nếu versioning là requirement chính, persistent balanced/functional tree thường natural hơn.

## Skip graph và distributed variants

Multi-level random linking idea có relatives trong distributed overlay/search structures. Exact protocols khác Skip List in-memory, nhưng hierarchy + probabilistic routing intuition liên quan.

Điều này cho thấy design pattern “sparse express links” có thể scale beyond one process.

## Failure mode: off-by-one level conventions

Một implementation có thể gọi base level là 0, maximum height `h` nghĩa levels `0..h`, hoặc height count `h` nghĩa `0..h-1`.

Mix conventions dễ gây array out-of-bounds hoặc miss top-level link.

Nên define rõ:

```text
height = number of levels in node
valid levels = 0 .. height-1
```

hoặc một convention khác nhưng consistent.

## Failure mode: node forward-array length

Khi traversal ở level `L`, current node phải có pointer slot `L`. Standard design đảm bảo chỉ nodes present at that level được traversal, sentinel has max levels.

Dynamic language code dễ hide structural mistakes; typed/low-level code có thể crash nếu access beyond allocated forward array.

## Failure mode: random seed/testing

Random shape làm bug khó reproduce. Tests nên cho phép deterministic seed hoặc inject random-level generator.

Then failing sequence có thể replay exact structure.

Production randomness và deterministic test randomness là hai concerns khác nhau.

## Validation

Validator có thể kiểm tra:

```text
level 0 sorted strictly/non-strictly theo duplicate policy
every higher-level node cũng tồn tại level 0
each level sorted
forward link level không đi tới node có insufficient height
currentMaxLevel khớp top non-empty level
size/count đúng
```

Indexed skip list còn phải recompute spans theo base-level distances.

## Differential testing

Reference có thể là `TreeMap`, sorted array/list hoặc multiset implementation.

Random operation sequence:

```text
insert
remove
contains
lowerBound
range scan
rank/select nếu augmented
```

so results với reference after every batch.

Randomization của structure không ảnh hưởng abstract semantics, nên differential testing rất phù hợp.

## Benchmarking

Benchmark Skip List vs tree phải tách workloads:

```text
random lookup
sequential range scan
insert-heavy
mixed read/write
concurrent contention
memory footprint
```

A single microbenchmark “100k gets” không nói hết trade-off.

Dataset size so với CPU cache cũng có thể đổi result đáng kể.

## When Skip List is a good mental candidate

Skip List đáng nghĩ tới khi cần dynamic ordered map/set, range iteration, implementation muốn tránh rotation complexity hoặc concurrency design hưởng lợi từ local pointer splicing.

Nếu dataset static, sorted array thường đơn giản và locality tốt. Nếu external-memory/page-oriented, B+Tree mạnh hơn. Nếu exact equality only, hash table thường phù hợp. Nếu hard worst-case bound bắt buộc, deterministic balanced tree rõ hơn.

## Common misconceptions

“Skip List là linked list nên search linear” sai vì hierarchy thay đổi search path expected.

“Expected `O(log n)` nghĩa mỗi operation chắc chắn logarithmic” sai.

“Concurrency dễ hơn tree nghĩa implementation lock-free đơn giản” sai; reclamation và atomic protocol vẫn phức tạp.

“Random promotion càng nhiều càng nhanh” sai vì memory/cache overhead tăng và có optimum trade-off.

“Skip List chỉ là academic structure” sai; ordered concurrent/indexing workloads đã dùng variants trong real systems.

## Mental Model

> Skip List không cân bằng tree; nó cân bằng **mật độ các express links** bằng randomness. Level 0 giữ truth đầy đủ, levels cao là indexes thưa của cùng sorted sequence. Search đi từ coarse resolution xuống fine resolution, còn insert/delete chỉ splice những links mà node tham gia.

Khi đánh giá Skip List, hãy hỏi: **expected guarantee có đủ không, range scan có quan trọng không, memory/pointer locality thế nào, concurrency có cần không, và comparator/duplicate semantics có rõ không?**

Xem tiếp: [Linked Lists](../01_linear_structures/01_linked_lists.md), [Balanced Search Trees](./02_balanced_search_trees.md), [Augmented Trees](./06_augmented_trees_and_order_statistics.md), [B-Tree & External Memory](./05_b_trees_and_external_memory.md) và [Amortized & Randomized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md).
