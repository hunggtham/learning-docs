# Balanced Search Trees
**Cây tìm kiếm cân bằng (Balanced Search Tree / 균형 탐색 트리)**

Binary Search Tree chỉ có lợi nếu chiều cao của cây nhỏ. Một BST có thể chứa đúng cùng tập key nhưng có shape hoàn toàn khác nhau: nếu insert theo thứ tự gần ngẫu nhiên, cây có thể khá thấp; nếu insert `1,2,3,4,5,...`, cây có thể suy thoái thành gần như linked list. Vì vậy operation tưởng như `O(log n)` thực chất chỉ có bound theo chiều cao `h`:

\[
search, insert, delete = O(h)
\]

Nếu `h = n`, ta mất toàn bộ lợi thế của tree search. **Balanced search tree (균형 탐색 트리)** giải quyết vấn đề này bằng cách thêm một invariant hình dạng. Ta trả một ít maintenance cost khi insert/delete để đảm bảo `h = O(log n)` trong dài hạn.

## Mental Model

> Balancing không làm BST “sorted hơn”. BST order invariant đã đủ để nói left < node < right. Balancing chỉ kiểm soát **shape** để số bước từ root tới leaf không tăng tuyến tính.

Có hai lớp invariant khác nhau:

```text
BST invariant     -> quyết định key nằm bên trái hay bên phải
balance invariant -> quyết định tree có được phép nghiêng quá mức hay không
```

Rotation tồn tại vì nó sửa lớp thứ hai mà không phá lớp thứ nhất.

## Rotation thực sự bảo toàn điều gì?

Xét một right rotation:

```text
        y                     x
       / \                   / \
      x   C      --->        A   y
     / \                       / \
    A   B                     B   C
```

Trước rotation, inorder sequence là:

```text
A < x < B < y < C
```

Sau rotation, sequence vẫn y hệt. Nghĩa là rotation thay đổi quan hệ parent-child cục bộ nhưng **không thay đổi sorted order** của các key. Đây là lý do rotation có thể sửa height mà không cần rebuild toàn subtree.

Nếu mỗi node còn metadata như `height`, `size`, `maxEnd`, metadata phải được recompute theo đúng thứ tự sau rotation. Tree có thể vẫn là BST nhưng query augmentation sẽ sai nếu metadata cũ còn tồn tại.

## AVL Tree: cân bằng bằng height

**AVL Tree (AVL 트리)** giữ balance factor:

\[
BF(u)=height(left(u))-height(right(u))
\]

và yêu cầu:

\[
BF(u) \in \{-1,0,1\}
\]

cho mọi node. Đây là một invariant chặt: hai subtree của bất kỳ node nào không được lệch nhau quá một level.

### Tại sao invariant này cho `O(log n)` height?

Hãy hỏi ngược: với height `h`, cây AVL ít node nhất có bao nhiêu node? Để vẫn đạt height `h` nhưng dùng ít node nhất, một subtree phải có height `h-1`, subtree còn lại nhỏ nhất có thể mà vẫn hợp lệ là `h-2`.

Do đó:

\[
N(h)=1+N(h-1)+N(h-2)
\]

Recurrence này tăng giống Fibonacci, tức số node tăng theo exponential của height. Đảo lại quan hệ đó, height chỉ tăng logarithmic theo `n`:

\[
h=O(\log n)
\]

Đây là bản chất proof; không cần học thuộc một hằng số cụ thể để hiểu vì sao AVL không thể cao tuyến tính.

## AVL insertion: bốn case chỉ là hai loại lệch

Insert trước tiên giống BST thường. Sau đó chỉ các ancestor trên search path mới có thể đổi height. Ta đi ngược lên, recompute height và tìm node đầu tiên vi phạm `|BF| <= 1`.

Các tên LL, RR, LR, RL chỉ mô tả hướng path làm mất cân bằng:

```text
LL -> right rotation
RR -> left rotation
LR -> left rotation ở left child, sau đó right rotation
RL -> right rotation ở right child, sau đó left rotation
```

Không nên học đây như bốn mẹo rời rạc. Hãy nhìn shape: nếu subtree nặng nằm “cùng hướng” với parent, một rotation đơn đủ; nếu path zig-zag, cần rotation ở child trước để biến nó về cùng hướng.

### Java skeleton

```java
final class Node {
    int key;
    int height = 1;
    Node left, right;

    Node(int key) {
        this.key = key;
    }
}

static int h(Node x) {
    return x == null ? 0 : x.height;
}

static void pull(Node x) {
    x.height = 1 + Math.max(h(x.left), h(x.right));
}

static Node rotateRight(Node y) {
    Node x = y.left;
    Node b = x.right;

    x.right = y;
    y.left = b;

    pull(y);
    pull(x);
    return x;
}
```

Điểm quan trọng trong code không phải tên function mà là thứ tự `pull`: node thấp hơn sau rotation phải được cập nhật trước node mới ở trên.

## AVL deletion khó hơn insertion ở đâu?

Insert chỉ tăng height trên một path và thường việc sửa node mất cân bằng đầu tiên đủ để khôi phục structure phía trên. Delete có thể làm subtree thấp đi; sau một rotation, height của subtree mới vẫn có thể giảm tiếp và gây imbalance ở ancestor cao hơn. Vì vậy deletion thường phải tiếp tục kiểm tra toàn path lên root.

Đây là một ví dụ tốt cho việc cùng invariant nhưng mutation khác nhau tạo repair logic khác nhau.

## Red-Black Tree: encode balance bằng màu

**Red-Black Tree (레드-블랙 트리)** không giữ chênh lệch height trực tiếp. Thay vào đó nó gắn color metadata vào node và duy trì các invariant thường được phát biểu như:

1. mỗi node là red hoặc black;
2. root là black;
3. null leaves/sentinels được xem là black;
4. red node không có red child;
5. mọi path từ một node tới descendant null leaves có cùng số black nodes.

Từ các property này suy ra không có root-to-leaf path nào dài hơn khoảng gấp đôi path ngắn nhất. Do đó:

\[
h = O(\log n)
\]

Red-Black cho phép cây “lỏng” hơn AVL. Đổi lại, insert/delete thường cần ít rotation nghiêm ngặt hơn và phù hợp tốt với ordered map/set general-purpose.

## Tại sao red node không được có red child?

Nếu cho phép chuỗi red dài tùy ý, black-height có thể vẫn giữ nhưng physical height có thể phình lớn. Rule “không red-red” giới hạn số red node giữa các black node. Vì mọi root-to-leaf path có cùng black count và red chỉ có thể xen kẽ, longest path bị bound theo black-height.

Màu ở đây không có ý nghĩa semantic; nó là một cách compact để encode structural constraint.

## Red-Black insertion: điều gì đang được sửa?

Khi insert một node mới, thường node mới được tô red để không thay đổi black-height ngay lập tức. Vấn đề chỉ phát sinh nếu parent cũng red. Khi đó repair logic dựa vào color của uncle:

- nếu uncle red, recolor parent + uncle thành black và grandparent thành red, sau đó tiếp tục kiểm tra cao hơn;
- nếu uncle black/null, rotations + recolor sửa local red-red violation.

Điểm cần hiểu là repair không “tìm một shape đẹp”. Nó cố khôi phục chính xác hai thứ: không red-red và black-height consistency.

## Red-Black deletion vì sao nổi tiếng khó?

Delete một black node có thể làm một path mất một đơn vị black-height. Nhiều textbook mô tả trạng thái này bằng khái niệm “double black”. Các case sibling-red, sibling-black-with-black-children, sibling-with-red-near/far-child đều là cách phân phối lại black-height qua recolor/rotation.

Nếu chỉ nhớ case mà không giữ mental model “một path đang thiếu black count”, code rất dễ sai.

Trong production, nếu không thật sự cần tự implement balanced tree, dùng standard library thường an toàn hơn. Tự implement nên chủ yếu để hiểu invariant hoặc khi cần augmentation đặc biệt.

## AVL hay Red-Black?

AVL cân bằng chặt hơn, nên lookup có thể có constant factor tốt hơn vì height thấp hơn. Red-Black cho phép nhiều shape hơn, thường giảm rebalancing pressure ở workload update-heavy.

Không nên biến điều này thành luật tuyệt đối. Performance thật còn phụ thuộc allocator, cache locality, branch prediction, key comparison cost và implementation quality.

Một cách reasoning tốt hơn là:

```text
read-heavy, lookup latency quan trọng -> AVL có thể hấp dẫn
mixed read/write general ordered map -> Red-Black thường phổ biến
external-memory/page I/O dominant -> B/B+Tree phù hợp hơn
concurrent ordered structure -> có thể cần skip list / specialized tree
```

## Ordered Map khác Hash Map ở capability, không chỉ Big-O

Hash table tối ưu exact identity lookup. Balanced BST duy trì total order nên hỗ trợ các operation như:

```text
minimum / maximum
predecessor / successor
floor(key) / ceiling(key)
range iteration
rank / k-th nếu được augment
```

Trong Java, `TreeMap`/`TreeSet` cung cấp `NavigableMap`/`NavigableSet` semantics. `HashMap` không thể trả `floorKey()` một cách tự nhiên vì nó không duy trì order invariant.

Nếu requirement là “lookup exact key nhanh nhất”, hash map thường phù hợp. Nếu requirement là “lookup + order query”, balanced tree giải một bài toán rộng hơn.

## Duplicate keys và comparator contract

Một tree implementation phải quyết định duplicates được xử lý thế nào: reject, count frequency, lưu multiset node hay đặt duplicate theo một rule ổn định. Nếu comparator cho rằng hai object bằng nhau (`compare(a,b)==0`) nhưng equality semantics của application lại khác, ordered map có thể xem chúng như cùng key.

Trong Java, comparator phải tạo ordering nhất quán, đặc biệt cần transitive:

```text
a < b và b < c  =>  a < c
```

Comparator sai có thể làm search path không còn meaningful dù rotation code hoàn hảo.

## Augmentation: balanced tree như một framework

Một balanced tree mạnh hơn nhiều khi mỗi node lưu metadata tổng hợp từ subtree. Ví dụ:

```text
size(node) = 1 + size(left) + size(right)
```

cho phép tìm k-th smallest hoặc rank trong `O(log n)`.

Interval tree có thể lưu:

```text
maxEnd(node) = max(interval.end, maxEnd(left), maxEnd(right))
```

để prune whole subtrees khi tìm overlap.

Nguyên tắc tổng quát là nếu metadata có thể recompute trong `O(1)` từ node + children, thì insert/delete vẫn `O(log n)` vì chỉ `O(log n)` ancestors và một số node rotation cần `pull()` lại.

Xem thêm [Augmented Trees](./06_augmented_trees_and_order_statistics.md).

## Memory locality: một giới hạn của pointer trees

Big-O không nói hết performance. Mỗi tree node thường là một object/allocation riêng, có pointers/references và metadata. Traversal root-to-leaf có thể jump qua nhiều cache lines.

Array-based binary search trên sorted array có cùng `O(log n)` lookup nhưng locality tốt hơn và overhead memory thấp hơn; đổi lại insert/delete giữa array là đắt. Vì vậy static ordered data thường không cần balanced tree.

Đây là một trade-off kinh điển:

```text
sorted array -> read/search tốt, mutation giữa sequence đắt
balanced BST -> dynamic ordered mutation O(log n), locality kém hơn
```

## Connection với B-Tree và external memory

AVL/Red-Black giả định cost chính là số bước qua node trong RAM. Khi mỗi node access có thể tương ứng disk/page I/O, binary branching trở nên quá hẹp. B-Tree/B+Tree tăng branching factor để mỗi page chứa nhiều keys, giảm tree height và I/O count.

Nói cách khác, “balance” luôn phải gắn với cost model. RAM tree tối ưu pointer-depth; database index tối ưu page-depth.

## Common misconceptions

**“Balanced” nghĩa là hai subtree phải có cùng size.** Không đúng. AVL bound theo height difference; Red-Black dùng color/black-height. Hai subtree có thể khác số node đáng kể mà tree vẫn hợp lệ.

**Rotation làm thay đổi sorted order.** Không. Rotation được thiết kế chính vì nó bảo toàn inorder order.

**TreeMap luôn chậm hơn HashMap nên không nên dùng.** Sai cách đặt vấn đề. `TreeMap` cung cấp ordered operations mà `HashMap` không cung cấp.

**Một BST có random-looking input thì chắc chắn `O(log n)`.** Không có deterministic guarantee. Nếu cần guaranteed logarithmic height, phải dùng structure có balancing invariant hoặc randomized structure với expected guarantee.

**Biết bốn case AVL là đã hiểu balanced tree.** Chưa. Quan trọng hơn là hiểu invariant nào bị phá, rotation bảo toàn cái gì, và tại sao repair khôi phục bound `O(log n)`.

## Khi nào nên tự implement?

Trong học thuật và interview, tự implement giúp hiểu invariant. Trong production, ưu tiên standard library trừ khi có requirement đặc biệt như custom allocator, intrusive node, lock-free concurrency, augmented metadata hoặc domain-specific ordering.

Nếu tự implement, test không nên chỉ kiểm output. Sau random sequences insert/delete, hãy kiểm toàn bộ structural invariant:

```text
BST inorder sorted
AVL: |BF| <= 1 và stored height đúng
Red-Black: không red-red và black-height bằng nhau
metadata augmentation recompute đúng
node count / parent pointers nhất quán
```

Property/invariant testing thường phát hiện bug rotation/delete nhanh hơn các example nhỏ.

## Mental Model mở rộng

> Balanced search tree là một **dynamic ordered index**. BST order cho biết đi hướng nào; balance invariant giữ số bước nhỏ; rotation sửa shape mà không phá order; augmentation thêm capability mới mà vẫn giữ logarithmic path length.

Khi chọn structure, hãy hỏi không chỉ “lookup có nhanh không?” mà còn: dữ liệu có mutate không, có cần order/range/predecessor không, cost model là RAM hay page I/O, và metadata nào cần duy trì cùng key order.