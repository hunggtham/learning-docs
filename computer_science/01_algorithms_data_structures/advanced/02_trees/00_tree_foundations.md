# Nền tảng Tree
**Cây (Tree / 트리)**

Tree mô hình hóa quan hệ phân cấp: filesystem, DOM, organization chart, AST, index, decision structure. Một rooted tree có root, parent, child, sibling và leaf. Với tree connected, acyclic có `n` nodes, số edges là `n-1`.

## Depth và height

**Depth / 깊이** của node thường là số edges từ root đến node. **Height / 높이** của node là độ dài đường đi dài nhất từ node xuống leaf. Height của toàn tree ảnh hưởng trực tiếp cost của nhiều operations.

## Traversal

Binary tree có ba DFS orders cơ bản:

```text
Preorder:  root -> left -> right
Inorder:   left -> root -> right
Postorder: left -> right -> root
```

Level-order dùng BFS/queue.

C representation:

```c
typedef struct TreeNode {
    int value;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;
```

Java và JavaScript dùng object references tương tự về mặt logical structure.

## Recursion tự nhiên với tree

Tree có recursive definition: subtree của tree cũng là tree. Height:

```java
int height(TreeNode n) {
    if (n == null) return 0;
    return 1 + Math.max(height(n.left), height(n.right));
}
```

Correctness đến từ structural induction: nếu height của children đúng, công thức tại parent đúng.

## Mental Model

> Tree biến một structure lớn thành các substructures cùng loại. Vì vậy recursion và tree thường khớp nhau tự nhiên.

Xem tiếp: [BST](./01_binary_search_trees.md), [Heaps](./03_heaps.md), [Tries](./04_tries.md).

## Full, complete, perfect và balanced không phải một khái niệm

**Full binary tree**: mỗi node có 0 hoặc 2 children.

**Complete binary tree**: mọi level trừ cuối đầy, level cuối được lấp từ trái sang phải. Heap cần property này.

**Perfect binary tree**: mọi internal node có 2 children và mọi leaves cùng depth.

**Balanced tree**: height được giữ trong bound logarithmic hoặc local balance constraint tùy loại.

Những từ này thường bị dùng lẫn, nhưng mỗi property phục vụ reasoning khác nhau.

## Iterative traversals

Preorder dễ mô phỏng bằng stack: pop node, visit, push right rồi left để left được xử lý trước.

Inorder cần đi xuống left chain, stack lưu ancestors đang chờ visit. Postorder khó hơn vì node chỉ được visit sau cả children; có thể dùng two-stack hoặc stack + lastVisited state.

Hiểu iterative traversal giúp thấy recursion thực chất đang lưu continuation/ancestor state nào trên call stack.

## Euler tour của tree

Nếu ghi lại thời điểm enter/exit node trong DFS, subtree của `u` thường ánh xạ thành một contiguous interval trong DFS order. Đây là bridge rất mạnh từ tree sang array/range-query structures.

Ví dụ nếu `tin[u]` là entry time và `tout[u]` là cuối subtree, mọi descendants của `u` nằm trong interval `[tin[u], tout[u]]`. Ta có thể dùng Fenwick/segment tree để query/update subtree sau khi “flatten” tree.

## Lowest Common Ancestor connection

LCA của hai nodes là deepest node làm ancestor của cả hai. Naive climb có thể chậm; binary lifting preprocess `2^k` ancestors để jump theo powers of two, biến query thành `O(log n)`.

Đây là một ví dụ khác nơi logarithm xuất hiện vì mỗi jump đại diện distance tăng gấp đôi.

## Trees là graphs có thêm invariant

Mọi tree là graph connected acyclic. Vì unique simple path giữa hai nodes, nhiều graph problems trở nên dễ hơn: không cần visited khi DFS có parent rõ ràng; DP có dependency tự nhiên; edge removal luôn tách tree thành hai components.
