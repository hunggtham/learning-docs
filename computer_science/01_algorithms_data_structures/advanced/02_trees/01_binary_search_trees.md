# Binary Search Tree
**Cây tìm kiếm nhị phân (Binary Search Tree, BST / 이진 탐색 트리)**

Binary Search Tree thêm một **order invariant / 정렬 불변식** lên binary tree để việc search không cần duyệt toàn bộ structure. Với mỗi node `x`, một formulation phổ biến là:

```text
mọi key trong left subtree  < x.key
mọi key trong right subtree > x.key
```

Nếu domain cho phép duplicate keys, policy phải được định nghĩa ngay từ đầu: reject duplicate, lưu count/value-list trong node, hoặc cho equal key đi về một phía theo rule cố định. BST đúng không chỉ vì từng node trông hợp lý; nó đúng vì **mọi subtree** đều thỏa cùng invariant.

## Từ binary search trên array tới BST

Sorted array cho binary search `O(log n)` vì midpoint comparison loại nửa candidates. Nhưng insert vào giữa array cần dịch chuyển nhiều elements, thường `O(n)`.

BST giữ sorted order dưới dạng links thay vì vị trí contiguous cố định. Search vẫn loại một subtree sau mỗi comparison; insert/delete có thể relink local nodes thay vì shift toàn bộ suffix.

Trade-off là performance giờ phụ thuộc **height `h`**:

```text
search   O(h)
insert   O(h)
delete   O(h)
```

Nếu tree balanced, `h = O(log n)`. Nếu tree thoái hóa thành chain, `h = O(n)`.

Đây là insight trung tâm: BST không bảo đảm logarithmic time chỉ nhờ order invariant. Muốn worst-case logarithmic còn cần balancing strategy.

## Search như một proof bằng loại trừ

Tại node `x`:

```text
target < x.key  -> right subtree chắc chắn không chứa target
target > x.key  -> left subtree chắc chắn không chứa target
target = x.key  -> tìm thấy
```

Mỗi bước search hợp lệ vì BST invariant cho phép **chứng minh cả một subtree không thể chứa answer**.

Iterative C version:

```c
TreeNode *bst_search(TreeNode *root, int key) {
    while (root != NULL) {
        if (key == root->key) return root;
        root = key < root->key ? root->left : root->right;
    }
    return NULL;
}
```

Nếu insert/delete từng phá invariant dù chỉ một node, code trên vẫn compile và chạy nhưng proof “bỏ subtree này là an toàn” không còn đúng.

## Insert

Insert trước hết là search tới vị trí null nơi key phải nằm.

```java
TreeNode insert(TreeNode root, int key) {
    if (root == null) return new TreeNode(key);

    if (key < root.key) {
        root.left = insert(root.left, key);
    } else if (key > root.key) {
        root.right = insert(root.right, key);
    }

    return root;
}
```

Correctness đến từ việc vị trí insert được xác định bởi cùng comparisons như search. Nếu ta dừng ở null trong left branch của node `x`, mọi ancestor constraints đã chứng minh key thuộc chính interval đó.

Một cách nhìn hữu ích là mỗi node chia numeric/order space thành các interval nhỏ hơn. Search path không chỉ đi qua nodes; nó liên tục thu hẹp interval hợp lệ của key.

## Duplicate policy không phải chi tiết nhỏ

Ba policy phổ biến:

```text
1. reject duplicate
2. node lưu key + count/list values
3. equal key luôn đi một side theo rule cố định
```

Policy số 2 thường sạch hơn nếu key đại diện identity còn nhiều records chia sẻ key. Policy số 3 vẫn có thể đúng nhưng range/search/delete phải dùng cùng rule.

Trong production map/set abstraction, key equality còn liên quan comparator contract. Nếu comparator cho rằng hai keys bằng nhau (`compare(a,b)==0`) thì ordered set/map thường coi chúng là cùng vị trí order, dù object identity khác.

## Minimum, maximum, successor, predecessor

Minimum của BST nằm bằng cách đi left liên tục; maximum tương tự với right.

Successor của node `x` là key nhỏ nhất lớn hơn `x.key`.

Nếu `x` có right subtree, successor là minimum của right subtree.

Nếu không có right subtree, ta đi lên ancestors cho tới ancestor đầu tiên mà `x` nằm trong left subtree của ancestor đó.

Predecessor đối xứng.

Các operation này là lý do ordered map/tree mạnh hơn hash table. Hash table biết “key này có không?”, nhưng không tự nhiên biết “key gần nhất nhỏ hơn X là gì?”.

## Delete là operation khó nhất của BST cơ bản

Delete có ba case.

### Case 1 — leaf

Không có child, chỉ cần bỏ link từ parent.

### Case 2 — một child

Thay node bằng child duy nhất. Vì toàn subtree child đã thỏa order range của node cũ, relink này giữ invariant.

### Case 3 — hai children

Ta không thể đơn giản đưa một child lên nếu vẫn muốn giữ cả hai subtrees. Strategy phổ biến là thay node bằng **inorder successor** — minimum của right subtree — rồi xóa successor ở vị trí cũ.

Tại sao successor an toàn?

- nó lớn hơn mọi key trong left subtree vì nó nằm trong right subtree của node cũ;
- nó là phần tử nhỏ nhất bên phải, nên sau khi lên vị trí node cũ, các key còn lại trong right subtree vẫn không nhỏ hơn nó;
- successor không có left child, nên delete lần hai giảm về case đơn giản hơn.

Có thể dùng predecessor đối xứng.

## Delete bằng transplant

Trong implementation có parent pointers, một helper `transplant(u, v)` thay subtree rooted at `u` bằng subtree rooted at `v`. Đây là abstraction giúp tách “relink parent-child” khỏi logic chọn successor.

Pseudo-flow:

```text
if left == null:
    transplant(node, right)
else if right == null:
    transplant(node, left)
else:
    s = minimum(right)
    nếu s không phải direct right child:
        transplant(s, s.right)
        s.right = node.right
    transplant(node, s)
    s.left = node.left
```

Cách này làm rõ invariant hơn code gán pointer ad-hoc ở nhiều chỗ.

## Inorder traversal và sorted order

Inorder traversal:

```text
left -> root -> right
```

trả keys theo sorted order vì mọi key bên trái nhỏ hơn root và mọi key bên phải lớn hơn root, recursively.

Đây là một theorem đơn giản nhưng cực quan trọng: local invariant ở từng node đủ để suy ra global sorted order của toàn tree.

## Range query

Muốn lấy keys trong `[L, R]`, không cần scan cả tree.

```text
nếu node.key > L: left subtree có thể chứa answer
nếu L <= node.key <= R: output node
nếu node.key < R: right subtree có thể chứa answer
```

Trong balanced BST, complexity gần:

\[
O(\log n + k)
\]

với `k` là số kết quả output. Đây là **output-sensitive complexity**: nếu query cần trả hàng triệu records, không structure nào tránh được cost tương ứng với số output.

## BST shape phụ thuộc insertion order

Insert:

```text
1, 2, 3, 4, 5
```

vào raw BST tạo chain:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
```

Search giờ là linear. Random insertion order thường cho expected height tốt hơn, nhưng đó không phải worst-case guarantee.

AVL, Red-Black Tree, Treap hoặc randomized skip-list-like approaches tồn tại vì ta cần kiểm soát shape, không chỉ order.

## BST vs sorted array

BST và sorted array cùng khai thác total order nhưng tối ưu workload khác nhau.

Sorted array:

```text
lookup        O(log n)
sequential scan rất cache-friendly
insert middle O(n)
low memory overhead
```

Balanced BST:

```text
lookup        O(log n)
insert/delete O(log n)
predecessor/successor tự nhiên
node overhead + pointer chasing
```

Nếu workload static và đọc nhiều, sorted array có thể tốt hơn tree dù Big-O lookup giống nhau. Đây là ví dụ cho thấy locality và mutation pattern quan trọng ngang asymptotic complexity.

## BST vs HashMap

HashMap thường cho expected `O(1)` equality lookup, nhưng không duy trì order.

Balanced BST cho `O(log n)` nhưng hỗ trợ:

```text
min/max
floor/ceiling
predecessor/successor
range iteration
ordered traversal
```

Câu hỏi đúng không phải “HashMap nhanh hơn TreeMap đúng không?” mà là “workload có cần order semantics không?”.

## Parent pointer, iterator và ordered traversal

Nếu node có parent pointer, successor/predecessor có thể tìm bằng upward navigation. Điều này giúp iterator không cần stack lớn nếu tree structure ổn định.

Nhưng parent pointer tạo thêm invariant: rotation, delete và transplant đều phải update nó chính xác. Nếu một field không cần cho API/workload, đừng thêm chỉ vì “có vẻ tiện”.

## Augmented BST

BST node có thể lưu thêm metadata nếu metadata recompute được từ children.

Ví dụ:

```text
subtreeSize
subtreeSum
maxEndpoint
min/max key
```

Nếu update metadata trên path thay đổi, ta có thể hỗ trợ order statistics hoặc interval queries.

Một order-statistics tree với `size` trả k-th smallest bằng cách nhìn size của left subtree:

```text
leftSize = size(left)

k == leftSize + 1 -> current node
k <= leftSize     -> go left
k > leftSize + 1  -> go right với k giảm
```

Raw BST có thể làm được, nhưng muốn guarantee `O(log n)` vẫn cần balance.

## BST như một decision tree của comparisons

Mỗi search path là một sequence comparisons. Height chính là số comparisons worst-case theo tree shape.

Điều này nối BST với information theory: tree càng lệch, một số keys cần nhiều comparisons. Self-balancing tree đang trả maintenance cost trong update để giữ decision tree không quá sâu.

## Comparator và total order

Một BST tổng quát không nhất thiết dùng integer `<`. Nó dựa trên comparator.

Comparator cần có behavior nhất quán với total order:

```text
antisymmetry
transitivity
consistency
```

Nếu comparator bất nhất, tree có thể đưa cùng key về các directions mâu thuẫn và search không còn reliable.

Trong Java:

```java
Comparator<User> byId = Comparator.comparingLong(User::id);
```

Tránh comparator kiểu `a.id - b.id` nếu overflow có thể xảy ra.

## Persistent BST

Nếu structure immutable hoặc cần version history, update có thể **path-copy** chỉ các nodes trên search path và reuse phần còn lại.

Với balanced persistent tree, một update tạo `O(log n)` nodes mới thay vì copy cả tree. Đây là structural sharing — rất quan trọng trong functional programming, versioned data và persistent state systems.

## Concurrency note

BST mutation có thể thay nhiều links và rotations. Concurrent ordered maps vì thế cần synchronization strategy phức tạp hơn đơn giản đặt mutex quanh một variable.

Production concurrent trees có thể dùng coarse-grained lock, fine-grained lock, optimistic techniques hoặc completely different structures. DSA invariant vẫn là nền tảng, nhưng concurrency thêm một lớp invariant về atomicity/visibility.

## Common misconceptions

“BST search luôn O(log n)” là sai với unbalanced BST.

“Binary tree” không đồng nghĩa BST.

“Inorder luôn sorted” chỉ đúng khi order invariant thật sự được duy trì.

“Delete node hai children chỉ cần copy successor key” có thể chưa đủ nếu node chứa value, metadata hoặc identity semantics phức tạp; phải chuyển đúng record/fields theo API contract.

“Random BST thường tốt” không thay thế deterministic guarantee nếu input có thể adversarial.

## Testing BST

Ngoài test search output, hãy validate invariant sau random insert/delete:

```text
inorder strictly/non-strictly sorted theo duplicate policy
node count đúng
mọi subtree key nằm trong allowed range
parent pointers đúng nếu có
metadata == recomputation từ children
```

Một validator mạnh dùng range constraints:

```text
validate(node, low, high)
```

thay vì chỉ check `left < node < right`, vì violation có thể nằm sâu hơn một level.

## Mental Model

> BST biến **global sorted order** thành **local branching rule**. Mỗi comparison không chỉ chọn child; nó loại cả một interval keys. Search nhanh khi tree height thấp. Update mạnh vì structure động, nhưng chính mutation tạo rủi ro shape lệch nên balancing trở thành bước tiến tự nhiên tiếp theo.

Khi thiết kế hoặc dùng BST, hãy hỏi:

```text
Có cần order semantics hay chỉ exact lookup?
Height có guarantee không?
Duplicate key được định nghĩa thế nào?
Comparator có total-order contract đúng không?
Có cần predecessor/successor/range query không?
Metadata augmentation nào đáng trả maintenance cost?
Pointer/reference locality có ảnh hưởng workload thật không?
```

Xem tiếp: [Balanced Search Trees](./02_balanced_search_trees.md), [Augmented Trees](./06_augmented_trees_and_order_statistics.md), [B/B+Tree](./05_b_trees_and_external_memory.md).