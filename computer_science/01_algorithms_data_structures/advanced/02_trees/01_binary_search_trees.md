# Binary Search Tree
**Cây tìm kiếm nhị phân (Binary Search Tree, BST / 이진 탐색 트리)**

BST đưa order vào tree. Invariant thường là:

```text
mọi key ở left subtree  < node.key
mọi key ở right subtree > node.key
```

Duplicate cần policy rõ ràng: count, lưu list values hoặc quy định một phía.

## Search

Tại node `x`, nếu target nhỏ hơn `x.key`, chỉ left subtree có thể chứa target; nếu lớn hơn thì chỉ right subtree. Complexity là `O(h)` với `h` là height.

Nếu tree balanced, `h≈log n`. Nếu insert keys theo thứ tự tăng vào BST không tự cân bằng, tree có thể thành chain với `h=n`, khiến search `O(n)`.

## Insert

```java
TreeNode insert(TreeNode root, int key) {
    if (root == null) return new TreeNode(key);
    if (key < root.value) root.left = insert(root.left, key);
    else if (key > root.value) root.right = insert(root.right, key);
    return root;
}
```

## Delete

Leaf có thể bỏ trực tiếp. Node một child được thay bằng child. Node hai children thường thay key bằng **inorder successor** — phần tử nhỏ nhất ở right subtree — rồi delete successor đó.

Successor giữ order vì nó là key nhỏ nhất vẫn lớn hơn node hiện tại.

## Inorder traversal

Với BST, inorder trả keys theo sorted order. Đây là điều hash table không cung cấp tự nhiên.

## Mental Model

> BST là binary search được “đóng băng” thành pointer structure để dữ liệu có thể insert/delete động.

Sorted array cho search `O(log n)` nhưng insert giữa `O(n)`. Balanced BST cố gắng giữ search/insert/delete ở `O(log n)` bằng việc duy trì shape.

## Search/insert iterative trong C

```c
TreeNode *search(TreeNode *root, int key) {
    while (root != NULL) {
        if (key == root->key) return root;
        root = key < root->key ? root->left : root->right;
    }
    return NULL;
}
```

Code ngắn vì BST invariant loại cả subtree sau mỗi comparison. Nếu invariant không được duy trì sau insert/delete, function vẫn compile nhưng logic loại subtree không còn hợp lệ.

## Successor và predecessor

Nếu node có right subtree, successor là minimum của right subtree. Nếu không, successor là ancestor gần nhất mà node nằm trong left subtree của ancestor đó.

Operation này cho phép ordered iteration mà không cần sort lại keys.

## Duplicate policy

Một BST API phải định nghĩa duplicate keys. Ba strategies phổ biến:

```text
reject duplicate
store count/value list trong node
cho equal key sang một side theo rule cố định
```

Nếu policy không nhất quán giữa insert/search/delete, correctness bị phá.

## BST shape phụ thuộc insertion order

Insert sorted data `1,2,3,...` vào unbalanced BST tạo chain. Random insertion thường cho expected logarithmic height nhưng không phải deterministic guarantee. Đây là lý do production ordered maps dùng self-balancing tree hoặc randomized structures thay vì raw BST.

## Range query

BST có thể prune. Muốn in keys trong `[L,R]`:

- nếu node.key > L, left subtree có thể chứa answer;
- nếu key trong range, output;
- nếu node.key < R, right subtree có thể chứa answer.

Ta không cần visit subtrees được chứng minh nằm hoàn toàn ngoài range. Complexity gần `O(h+k)` với `k` output size trong balanced tree.

## Mental model mở rộng

> BST biến một global sorted order thành local invariant tại mỗi node. Chính local rule đủ để suy ra search, successor, range traversal và ordered iteration.
