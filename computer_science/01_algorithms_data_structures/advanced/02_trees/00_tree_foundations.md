# Nền tảng Tree
**Cây (Tree / 트리)**

Tree là một trong những abstraction quan trọng nhất của Computer Science vì nó biểu diễn **quan hệ phân cấp (hierarchical relationship / 계층 관계)**. Filesystem, DOM, AST, organization chart, category hierarchy, database index, routing structure và decision process đều có thể được nhìn như tree. Điểm quan trọng không phải là hình vẽ “một node ở trên, nhiều node ở dưới”, mà là việc tree tạo ra một cấu trúc trong đó mỗi phần của toàn bộ lại có thể được xem như một tree nhỏ hơn.

Một rooted tree có **root / 루트**, mỗi node khác root có đúng một parent, có thể có nhiều children, và không chứa cycle. Nếu tree có `n` nodes thì luôn có `n-1` edges. Tính chất này không phải một dữ kiện để học thuộc; nó xuất phát từ việc mỗi node trừ root cần đúng một edge nối lên parent. Chỉ riêng invariant đó đã giúp ta phân biệt tree với general graph, nơi một node có thể có nhiều đường quay lại hoặc nhiều parent-like relationships.

## Tree như một recursive object

Tree có định nghĩa đệ quy rất tự nhiên:

```text
Một tree = root + zero or more subtrees
```

Trong binary tree, mỗi node có tối đa hai subtrees: left và right. Vì subtree vẫn là tree, recursion khớp trực tiếp với structure vật lý. Đây là lý do traversal, height, subtree size, tree DP và nhiều thuật toán khác có recursive formulation rất sạch.

Ví dụ height:

```java
int height(TreeNode node) {
    if (node == null) return 0;
    return 1 + Math.max(height(node.left), height(node.right));
}
```

Correctness có thể nhìn bằng **structural induction / 구조적 귀납법**. Base case: empty tree có height 0. Inductive step: giả sử height của left và right subtree đúng; height của parent chỉ cần lấy lớn nhất trong hai subtree rồi cộng một level. Tư duy này quan trọng hơn chính đoạn code vì rất nhiều proof trên tree có cùng shape.

## Depth, height và size

**Depth / 깊이** của node thường là số edges từ root tới node. **Height / 높이** của node là độ dài đường đi dài nhất từ node xuống một leaf. **Subtree size / 서브트리 크기** là số node nằm trong subtree gốc tại node đó.

Ba khái niệm này phục vụ ba loại reasoning khác nhau. Depth liên quan ancestor distance, BFS level và LCA. Height liên quan worst-case cost của BST, recursion depth và balancing. Subtree size có thể dùng cho rank, order statistics, rerooting hoặc divide-by-subtree reasoning.

Nếu một binary tree có height `h`, số node tối đa là xấp xỉ:

\[
2^{h+1}-1
\]

với convention root ở depth 0. Ngược lại, một complete hoặc balanced tree có height logarithmic theo số node. Đây là lý do rất nhiều tree algorithms đạt `O(log n)` chỉ khi shape được kiểm soát.

## Full, complete, perfect và balanced

Các từ này dễ bị dùng lẫn nhưng mô tả những invariant khác nhau.

**Full binary tree**: mỗi node có 0 hoặc 2 children. Nó không nói gì về depth của leaves.

**Complete binary tree**: mọi level trừ level cuối đầy đủ; level cuối được lấp từ trái sang phải. Binary heap dựa vào property này để lưu tree trong array không cần pointers.

**Perfect binary tree**: mọi internal node có đúng hai children và mọi leaves nằm ở cùng depth.

**Balanced tree**: height được giữ trong một bound đủ tốt, thường logarithmic. AVL và Red-Black Tree dùng invariant khác nhau để đạt mục tiêu đó.

Điểm cần nhớ là structure property chỉ có ý nghĩa khi biết operation nào cần tối ưu. Heap cần complete shape; BST cần order; AVL cần balance; B+Tree cần high fan-out và occupancy.

## Traversal như một cách định nghĩa thứ tự xử lý

Binary tree có ba DFS orders kinh điển:

```text
Preorder:  root -> left -> right
Inorder:   left -> root -> right
Postorder: left -> right -> root
```

Chúng không chỉ khác nhau ở thứ tự in màn hình.

Preorder phù hợp khi parent phải được xử lý trước children, ví dụ serialize structure hoặc propagate state xuống dưới.

Postorder phù hợp khi parent phụ thuộc kết quả children, ví dụ tính subtree size, height, expression evaluation hoặc delete/free subtree.

Inorder đặc biệt quan trọng với BST vì nó trả keys theo sorted order.

Level-order dùng BFS/queue và xử lý theo depth. Nó phù hợp với shortest number-of-edges reasoning, level aggregation hoặc tree serialization theo breadth.

## Recursive stack đang lưu gì?

Một recursive traversal nhìn đơn giản vì call stack lưu hộ chúng ta trạng thái chưa hoàn thành. Với inorder, khi đi sâu xuống left child, stack đang ghi nhớ những ancestors cần quay lại visit sau khi left subtree xong.

Iterative inorder làm explicit cùng state đó:

```java
Deque<TreeNode> stack = new ArrayDeque<>();
TreeNode cur = root;

while (cur != null || !stack.isEmpty()) {
    while (cur != null) {
        stack.push(cur);
        cur = cur.left;
    }

    cur = stack.pop();
    visit(cur);
    cur = cur.right;
}
```

Hiểu iterative traversal giúp thấy recursion không phải “phép màu”; nó chỉ là một data structure stack được runtime quản lý.

## Tree representation trong C, Java và JavaScript

C thường biểu diễn node bằng pointer:

```c
typedef struct TreeNode {
    int value;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;
```

Ở đây tree correctness còn phụ thuộc lifetime: node phải sống đủ lâu, không double-free và không để dangling pointer.

Java dùng references và garbage collection. Logical structure giống pointer graph nhưng memory reclamation khác. JavaScript cũng dùng reference semantics, nhưng object shape/JIT/GC có thể khiến node-heavy tree có overhead khác hẳn array-based structure.

Một insight quan trọng: **tree topology logic** và **memory layout vật lý** không giống nhau. Hai tree cùng shape có thể có performance khác nếu một tree dùng contiguous arrays còn tree kia là hàng triệu objects rải rác trong heap.

## Parent pointer có cần không?

Nhiều tree chỉ lưu children, vì parent có thể được truyền qua recursion. Nhưng nếu workload cần predecessor/successor, upward navigation hoặc frequent ancestor queries, parent pointer có thể hữu ích.

Trade-off là mỗi node tốn thêm memory và mọi rotation/relink phải update parent pointer đúng. Không nên thêm metadata chỉ vì “có thể cần”; mỗi field là một invariant cần bảo trì.

## Euler tour và flattening

Một DFS có thể ghi `tin[u]` khi đi vào node và `tout[u]` khi rời node. Nếu đánh index theo entry order, toàn bộ subtree của `u` thường trở thành một đoạn liên tục:

```text
subtree(u) = [tin[u], tout[u]]
```

Đây là một bridge rất mạnh từ tree sang array/range-query structures.

Ví dụ một bài yêu cầu:

```text
update value của một node
query tổng toàn subtree
```

Ta có thể flatten tree bằng DFS, rồi dùng Fenwick Tree hoặc Segment Tree trên interval tương ứng. Tree problem được biến thành range problem mà vẫn giữ semantics subtree.

## Lowest Common Ancestor

**Lowest Common Ancestor (LCA / 최소 공통 조상)** của hai node là deepest node làm ancestor của cả hai.

Naive approach có thể đưa cả hai node lên parent từng bước. Với nhiều queries, ta preprocess **binary lifting / 이진 리프팅**:

```text
up[k][v] = ancestor của v cách 2^k bước
```

Một jump `2^k` có thể được tổ hợp từ hai jump `2^(k-1)`. Preprocess khoảng `O(n log n)`, query thường `O(log n)`.

Tại sao powers of two lại xuất hiện? Vì mọi số nguyên distance có thể phân rã theo binary representation. Đây cùng mental model với sparse table và exponentiation by squaring: precompute các block có kích thước tăng gấp đôi để ghép nhanh một khoảng lớn.

## Tree DP

Tree không có cycle nên khi fix parent, các child subtrees độc lập về cấu trúc. Điều này tạo điều kiện lý tưởng cho dynamic programming.

Ví dụ maximum independent set trên tree:

```text
dp[u][0] = best trong subtree u khi không chọn u
dp[u][1] = best trong subtree u khi chọn u
```

Nếu chọn `u`, children không được chọn. Nếu không chọn `u`, mỗi child có thể chọn state tốt hơn của nó.

State ở đây không phải “vì bài tree thì phải có dp[u]”. State tồn tại vì future của subtree chỉ cần biết một bit thông tin từ parent: parent có đang cấm chọn node này hay không.

## Rerooting

Một số bài cần answer cho mọi node nếu node đó được coi là root. Tính lại DFS từ từng root là `O(n^2)`. Rerooting DP reuse information giữa parent và child để đạt gần `O(n)`.

Mental model là:

```text
pass 1: tính contribution từ children lên parent
pass 2: truyền contribution từ phần còn lại của tree xuống child
```

Điều này là ví dụ rất đẹp cho việc reuse giữa hai states chỉ khác root position một edge.

## Tree là graph có invariant mạnh hơn

Mọi tree là một connected acyclic graph. Vì có đúng một simple path giữa hai nodes, nhiều graph problems trở nên đơn giản hơn.

Trong DFS tree có parent rõ ràng, ta không cần generic visited set nếu input thật sự được đảm bảo là tree. Xóa một edge luôn tách tree thành đúng hai components. Không có cycle nên dependency giữa parent-child tự nhiên là DAG.

Chính vì tree có structure chặt hơn graph tổng quát, ta có thể làm nhiều optimization mà general graph không cho phép.

## Common misconceptions

Một binary tree không tự động là BST. “Binary” chỉ nói tối đa hai children; BST thêm order invariant.

Một complete tree không đồng nghĩa balanced BST. Complete shape rất mạnh về layout nhưng không đảm bảo search-by-key semantics.

Height `O(log n)` không tự xuất hiện chỉ vì node có hai children. Một binary tree có thể là chain dài `n`.

Recursion không phải lúc nào cũng an toàn. Input tree rất sâu có thể overflow call stack trong C, Java hoặc JavaScript; iterative traversal cần được cân nhắc khi depth không bị bound.

## Testing tree implementations

Test một tree không nên chỉ kiểm tra output cuối. Hãy kiểm tra structural invariants sau mỗi sequence operations:

```text
node count có đúng không?
parent/child links có đối xứng không nếu có parent pointer?
traversal có visit mỗi node đúng một lần không?
subtree metadata có bằng recomputation từ children không?
```

Randomized operation sequences cộng với invariant validation thường bắt bug rotation/relink tốt hơn vài hand-written examples.

## Mental Model

> Tree là cách biến một structure lớn thành những substructures cùng loại, có quan hệ parent-child rõ ràng. Sức mạnh của tree đến từ việc mỗi node tạo ra một **boundary**: thông tin nào nằm trong subtree này, thông tin nào nằm ngoài, và operation nào có thể được giải bằng cách kết hợp kết quả của children.

Khi gặp tree problem, hãy hỏi:

```text
Thông tin nào cần truyền từ parent xuống?
Thông tin nào cần tổng hợp từ children lên?
Subtree có thể flatten thành interval không?
Có cần jump ancestor theo powers of two không?
Height có được guarantee logarithmic không?
Representation pointer-based hay contiguous ảnh hưởng gì tới performance?
```

Từ các câu hỏi đó, BST, AVL/Red-Black Tree, Heap, Trie, Segment Tree, LCA, Tree DP và B-Tree trở thành các specialization khác nhau của cùng một mental model.

Xem tiếp: [BST](./01_binary_search_trees.md), [Balanced Search Trees](./02_balanced_search_trees.md), [Heap](./03_heaps.md), [Trie](./04_tries.md), [B/B+Tree](./05_b_trees_and_external_memory.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md).