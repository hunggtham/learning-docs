# Augmented Trees, Order Statistics và Interval Trees
**증강 트리, 순서 통계 트리, 구간 트리**

Một balanced search tree đã hỗ trợ search/insert/delete theo key trong `O(log n)`. **Augmentation / 증강** biến nó thành một family structures mạnh hơn bằng cách lưu thêm metadata ở mỗi node — metadata đủ nhỏ để cập nhật cục bộ nhưng đủ giàu để trả lời query mới mà không phải scan toàn subtree.

Idea quan trọng nhất không phải thuộc “Order Statistic Tree” hay “Interval Tree”, mà là design pattern:

> Nếu một query trên subtree có thể được tóm tắt bằng một summary nhỏ, và summary của parent có thể tính từ local data + summaries của children trong `O(1)`, ta thường có thể thêm capability đó vào balanced BST mà vẫn giữ update `O(log n)`.

## Augmentation là thêm invariant thứ hai

BST bình thường giữ ordering invariant. Augmented BST giữ thêm metadata invariant.

Ví dụ subtree size:

\[
size(u)=1+size(left(u))+size(right(u))
\]

Tree có thể vẫn sorted hoàn hảo nhưng rank query sai nếu `size` stale. Vì vậy augmented structure là **multi-invariant structure**.

Một helper function kiểu `pull(node)` nên là source of truth:

```java
void pull(Node x) {
    if (x == null) return;
    x.size = 1 + size(x.left) + size(x.right);
}
```

Nếu có nhiều metadata:

```text
size
subtreeSum
maxEnd
minKey
...
```

`pull` recompute tất cả từ children/current node.

## Metadata phải có tính local-composability

Augmentation phù hợp nhất khi:

\[
M(u)=F(data(u),M(left),M(right))
\]

với `F` `O(1)`.

Ví dụ:

```text
size = 1 + left.size + right.size
sum = value + left.sum + right.sum
max = max(value, left.max, right.max)
maxEnd = max(interval.end, left.maxEnd, right.maxEnd)
```

Nếu update metadata cần scan toàn subtree, mỗi tree update có thể mất `O(n)` và lợi ích của balanced tree biến mất.

## Order-statistics tree

**Order statistics / 순서 통계** là các query về vị trí trong sorted order: k-th smallest, rank của key, số keys nhỏ hơn `x`, percentile, median dynamic.

Mỗi node lưu `size`.

### k-th smallest

Giả sử rank bắt đầu từ 1. Tại node `u`, đặt:

```text
leftSize = size(u.left)
```

Nếu `k == leftSize + 1`, `u` là answer. Nếu `k <= leftSize`, answer nằm left. Nếu lớn hơn, đi right và giảm:

\[
k \leftarrow k-(leftSize+1)
\]

Java:

```java
Node kth(Node root, int k) {
    Node cur = root;

    while (cur != null) {
        int leftSize = cur.left == null ? 0 : cur.left.size;

        if (k == leftSize + 1) return cur;
        if (k <= leftSize) {
            cur = cur.left;
        } else {
            k -= leftSize + 1;
            cur = cur.right;
        }
    }

    return null;
}
```

Trên balanced tree, mỗi bước xuống một level nên query `O(log n)`.

## Rank của key

Rank hỏi có bao nhiêu keys nhỏ hơn target, hoặc target đứng thứ mấy.

Khi đi right từ node `u`, toàn bộ left subtree và `u` chắc chắn nhỏ hơn target, nên cộng:

```text
size(left) + 1
```

Nếu duplicates được phép, semantics phải rõ: rank đầu tiên, rank cuối, count-less-than hay count-less-or-equal. Duplicate policy ảnh hưởng formula và node metadata.

## Dynamic median

Nếu tree hỗ trợ insert/delete + k-th, median của `n` values là rank khoảng `(n+1)/2` hoặc average hai middle ranks tùy definition.

Balanced order-statistics tree vì thế là một cách làm dynamic median trong `O(log n)` update/query. Alternative phổ biến là two-heaps nếu chỉ cần median, nhưng tree hỗ trợ thêm arbitrary rank/range queries.

Đây là example data structure selection theo query set.

## Weighted order statistics

Metadata không nhất thiết là node count. Nếu mỗi key có frequency/weight `w`, lưu subtree weight:

\[
W(u)=w(u)+W(left)+W(right)
\]

Ta có thể tìm weighted percentile bằng cách compare target cumulative weight với `leftWeight`.

Use case: histogram compressed by distinct value, sampling theo weight, frequency table ordered.

## Subtree aggregate

Một BST ordered theo key có thể lưu subtree sum/min/max và trả một số prefix/range aggregates.

Ví dụ `sumLessThan(x)`:

- nếu `x <= key(u)`, đi left;
- nếu `x > key(u)`, toàn bộ left subtree + node contribute, rồi đi right.

Với subtree sum metadata, prefix sum query `O(log n)` trên balanced tree.

Range sum `[L,R]` có thể lấy từ hai prefix sums nếu semantics cho phép:

\[
sum(\le R)-sum(<L)
\]

Augmented BST ở đây giống Fenwick/segment tree về summary, nhưng hỗ trợ dynamic sparse ordered keys tự nhiên hơn.

## Interval tree

Interval tree lưu intervals thường ordered theo start coordinate và augment mỗi node với:

```text
maxEnd = maximum end trong subtree
```

Hai closed intervals `[a,b]` và `[c,d]` overlap khi:

\[
a\le d \land c\le b
\]

Nếu domain dùng half-open `[a,b)`, condition là:

\[
a<d \land c<b
\]

Boundary semantics phải được định nghĩa trước.

## Interval search và pruning

Giả sử query `[L,R]`. Nếu left child tồn tại và:

```text
left.maxEnd >= L
```

left subtree **có thể** chứa overlap nên search left. Nếu `left.maxEnd < L`, mọi interval trong left kết thúc trước query start, nên prune toàn subtree.

`maxEnd` không trả answer trực tiếp; nó trả enough information để biết subtree có đáng khám phá hay không.

Đây là augmentation pattern điển hình.

## Reporting all overlaps

Tìm một overlapping interval và báo tất cả overlaps là hai problems khác nhau.

Nếu output có `k` intervals, bất kỳ algorithm nào cũng cần ít nhất `Ω(k)` để emit results. Với balanced interval tree, cost có thể gần `O(log n + k)` trong favorable design/queries nhưng phụ thuộc exact variant.

Output-sensitive complexity là mental model quan trọng: không thể kỳ vọng `O(log n)` khi phải trả hàng triệu matches.

## Interval tree vs segment tree

Tên dễ gây nhầm.

**Interval Tree** thường là BST-like structure lưu dynamic intervals và prune bằng metadata như `maxEnd`.

**Segment Tree** thường tổ chức coordinate domain/ranges theo fixed hierarchy và phù hợp range aggregates/updates.

Nếu keys/intervals insert-delete động và cần ordered operations, interval tree tự nhiên. Nếu coordinate range ổn định/compress được và cần aggregate mạnh, segment tree có thể tốt hơn.

## Interval tree vs sweep line

Nếu tất cả intervals known offline và query là global event như “maximum overlap”, sweep line + sorting thường đơn giản hơn.

Nếu queries/updates online, dynamic interval structure có lợi.

Static/offline vs dynamic/online là một dimension quan trọng của structure choice.

## Rotation và metadata update order

Xét right rotation:

```text
        y                  x
       / \                / \
      x   C      ->       A   y
     / \                    / \
    A   B                  B   C
```

Sau rotation, metadata của `y` phải được recompute trước metadata của `x`, vì `x` mới phụ thuộc `y` ở child.

Pseudo:

```text
rotateRight(y):
    x = y.left
    B = x.right

    x.right = y
    y.left = B

    pull(y)
    pull(x)
    return x
```

Sai thứ tự có thể giữ BST sorted nhưng làm summaries sai âm thầm.

## Red-Black/AVL augmentation

Balanced-tree implementation đã có rotations/recolor/height maintenance. Augmentation nên gắn vào mọi structural mutation point.

Rule tổng quát:

```text
mọi nơi children của node thay đổi -> metadata node có thể stale
mọi rotation -> pull nodes theo bottom-up dependency
mọi insert/delete -> ancestors trên modified path cần update
```

Nếu code có quá nhiều places update metadata thủ công, bug risk cao. Centralize mutation helpers khi có thể.

## Augmentation theorem intuition

Một principle kinh điển: nếu attribute của node có thể tính trong `O(1)` từ node + children attributes, balanced BST thường có thể maintain attribute mà không đổi asymptotic update complexity.

Tại sao? Insert/delete/rotation chỉ ảnh hưởng `O(log n)` nodes trên search/rebalance path, và mỗi node recompute `O(1)`.

Tổng vẫn:

\[
O(\log n)
\]

Đây là một design theorem thực dụng, không chỉ một structure riêng.

## Multiple augmentations

Một node có thể lưu nhiều summaries cùng lúc:

```text
size
sum
maxEnd
minimumTimestamp
custom aggregate
```

Nếu tất cả `pull` constant-time, asymptotic update vẫn `O(log n)`, nhưng constants, memory/node và cache locality tăng.

Đừng augment “cho tiện” mọi possible metric; metadata nên được biện minh bởi query workload.

## Augmented treap / skip list

Augmentation không giới hạn AVL/Red-Black. Treap node có thể lưu subtree size/sum. Skip list có thể thêm span/width ở mỗi forward pointer để hỗ trợ rank/select.

Concept sâu là **hierarchical ordered structure + local summaries**, không phải loại balancing cụ thể.

## Indexed skip list connection

Skip list thông thường search key expected `O(log n)`. Nếu mỗi forward pointer lưu số level-0 nodes mà nó skip, ta có thể navigate theo rank.

Đây chính là order-statistics augmentation trên skip-list hierarchy.

Xem thêm [Skip Lists](./07_skip_lists.md).

## Rope và sequence trees

Balanced trees có thể represent sequence thay vì sorted set. Node lưu subtree length/size, cho split/concatenate/index-by-position.

Rope text structure lưu chunks và weights để index/edit large strings. Implicit treap dùng subtree size làm “key by position” thay explicit key.

Augmentation vì thế mở rộng tree từ dictionary sang dynamic sequence structure.

## Implicit treap

Trong implicit treap, inorder position của node được suy ra từ subtree sizes. Split theo rank và merge theo random priority cho phép range sequence operations.

Nếu thêm lazy tags như reverse/add, structure bắt đầu gần segment tree nhưng trên dynamic sequence.

Đây là bridge giữa balanced tree, augmentation và lazy propagation.

## Lazy metadata/tagging

Một số augmented sequence trees lưu pending operation cho entire subtree, giống lazy segment tree. Ví dụ reverse flag hoán đổi left/right khi pushed.

Khi có lazy tags, invariant phức tạp hơn:

```text
stored summary phải phản ánh logical subtree hiện tại
children có thể chưa materialize pending update
trước khi descend cần push tag đúng
```

Đây là advanced version của “metadata invariant”.

## Range tree và multidimensional thinking

Nếu cần queries nhiều dimensions, có thể augment mỗi node bằng một secondary structure. Ví dụ 2D range tree order theo `x`, mỗi node lưu sorted structure theo `y` cho subtree.

Query nhanh hơn nhưng memory/build complexity tăng lớn.

Lesson: augmentation có thể recursive, nhưng mỗi extra dimension thường trả cost đáng kể.

## Geometry use cases

Interval/augmented trees xuất hiện trong:

```text
calendar conflict detection
memory-region overlap
compiler live ranges
collision broad phase
genomic interval queries
reservation windows
network address ranges
```

Exact structure phụ thuộc update frequency, dimensionality, output size và coordinate model.

## Database connection

Database ordered index có thể giữ statistics/summaries ở pages hoặc side structures. Order-statistics-like metadata có thể hỗ trợ counts/rank select trong specialized indexes.

Spatial indexes như R-tree dùng bounding rectangles thay vì BST key order, nhưng concept pruning bằng subtree summary tương tự: summary cho biết branch có khả năng intersect query không.

Augmentation là một pattern rộng của indexing.

## OS allocator connection

Memory allocators có thể dùng balanced trees keyed theo size/address và augment metadata để tìm suitable blocks hoặc track maximum free block trong subtree.

Query “subtree này có block đủ lớn không?” chính là summary-guided pruning.

## Maintaining counts with duplicates

Nếu many equal keys, một node có thể lưu `count` thay vì tạo node riêng mỗi duplicate.

Then:

\[
size(u)=count(u)+size(left)+size(right)
\]

k-th/rank formulas phải dùng `count` range thay vì exactly one current rank.

Duplicate policy là part of abstraction, không phải implementation afterthought.

## Deletion là nơi metadata bugs dễ xuất hiện

Insert thường đi một path và attach leaf. Delete có thể swap/copy successor value, remove another node, rebalance nhiều levels.

Nếu metadata gắn với key-specific local data, việc copy key/value mà quên copy/recompute associated local fields có thể sai.

Một strategy an toàn là structural deletion rõ ràng + bottom-up `pull` theo actual changed nodes, không patch metadata ad hoc.

## Persistence

Path-copying persistent BST tạo new nodes trên root-to-update path và reuse unchanged subtrees. Augmented metadata rất phù hợp vì mỗi copied node recompute summary từ children.

Mỗi version root có riêng logical state; subtree sharing tiết kiệm memory. Update `O(log n)` new nodes trên balanced tree.

Use case: versioned indexes, undo, time-travel queries và functional data structures.

## Concurrency

Augmentation làm concurrent update khó hơn vì một key mutation có thể require metadata changes trên ancestor path. Lock granularity, rotations và reader consistency phải được thiết kế cùng nhau.

Một reader nhìn tree giữa structural update và metadata update có thể thấy sorted order hợp lệ nhưng summary inconsistent.

Concurrent augmented tree cần atomicity protocol rõ, không chỉ lock node vừa insert.

## Validation

`validate(node)` nên recompute expected metadata recursively và compare stored values.

Ví dụ:

```java
int validateSize(Node u) {
    if (u == null) return 0;

    int left = validateSize(u.left);
    int right = validateSize(u.right);
    int expected = 1 + left + right;

    if (u.size != expected) throw new AssertionError();
    return expected;
}
```

Interval tree validator tương tự recompute `maxEnd`.

Trong debug tests, validator sau random insert/delete/rotation sequence rất hiệu quả.

## Differential testing

Order-statistics tree có thể test against sorted `ArrayList` nhỏ:

```text
random insert/delete
sort reference list
compare kth/rank/count
```

Interval queries có thể compare với brute-force scan all intervals.

Property-based/random testing đặc biệt hữu ích vì metadata bugs thường chỉ xuất hiện sau mutation sequence dài.

## Common failure modes

- BST ordering đúng nhưng metadata stale;
- update metadata sai thứ tự sau rotation;
- duplicate policy không nhất quán với `size`;
- interval boundary closed/half-open không rõ;
- `maxEnd` dùng wrong sentinel cho null;
- integer overflow trong subtree sum/count;
- lazy tag không push trước khi descend;
- copy successor key nhưng quên local metadata;
- assume output-heavy query vẫn `O(log n)` dù phải emit `k` results.

## Choosing augmentation vs separate structure

Không phải query nào cũng nên nhét vào một tree.

Nếu cần dynamic ordered keys + rank + range sum, augmented tree hợp lý. Nếu coordinate domain dense và only prefix sums, Fenwick đơn giản hơn. Nếu range updates mạnh, segment tree tự nhiên hơn. Nếu exact key lookup dominates, hash map + separate ordered structure đôi khi tốt hơn.

Augmentation trả cost bằng node size, implementation complexity và mutation burden. Chỉ thêm summary khi query benefit thực sự đáng.

## Mental Model

> Augmentation là biến mỗi subtree thành một “module có summary”. Key order cho biết đi trái hay phải; metadata cho biết subtree đóng góp bao nhiêu hoặc có thể bỏ qua hoàn toàn không. Nếu summary của parent tính được cục bộ từ children, ta có thể thêm query power mà không phá logarithmic update của balanced tree.

Khi muốn thêm query mới vào tree, hãy hỏi: **summary nhỏ nhất nào đủ để quyết định query mà không nhìn mọi node? Summary đó có combine từ children trong `O(1)` không? Và mọi structural mutation có một nơi rõ ràng để recompute nó không?**

Xem tiếp: [BST](./01_binary_search_trees.md), [Balanced Search Trees](./02_balanced_search_trees.md), [Skip Lists](./07_skip_lists.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md) và [Intervals & Sweep Line](../04_algorithmic_paradigms/08_intervals_and_sweep_line.md).
