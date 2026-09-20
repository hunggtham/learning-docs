# Augmented Trees, Order Statistics và Interval Trees  
**증강 트리, 순서 통계 트리, 구간 트리**

Một balanced BST có thể trở thành nhiều cấu trúc mạnh hơn nếu mỗi node lưu thêm metadata có thể cập nhật cục bộ từ children. Đây gọi là augmentation.

## Order-statistics tree

Mỗi node lưu:

```text
size = 1 + size(left) + size(right)
```

Muốn tìm k-th smallest, nhìn `leftSize`.

Nếu `k == leftSize + 1`, node hiện tại là answer. Nếu nhỏ hơn, đi left. Nếu lớn hơn, đi right với rank đã trừ phần left + node.

Balanced height cho query `O(log n)`.

Rank của key cũng tương tự: mỗi lần đi right, cộng số nodes chắc chắn nhỏ hơn từ left subtree + current node.

## Metadata và rotations

Sau AVL/Red-Black rotation, nodes đổi children; metadata phải recompute theo bottom-up order. Nếu quên update size/max-end, tree vẫn giữ sorted order nhưng augmented queries sai — một ví dụ multi-invariant structure.

## Interval tree

Lưu intervals theo start key, và mỗi node thêm:

```text
maxEnd = maximum end trong subtree
```

Khi tìm interval overlap query `[L,R]`, nếu left subtree có `maxEnd < L`, ta biết toàn bộ left subtree kết thúc trước query và có thể prune.

Metadata biến một BST bình thường thành spatial query structure.

## General augmentation principle

Nếu metadata `M(node)` có thể tính từ:

```text
node local data
M(left)
M(right)
```

trong `O(1)`, balanced BST update thường vẫn `O(log n)` vì chỉ `O(log n)` ancestors/rotated nodes cần sửa.

Đây là design pattern quan trọng hơn việc nhớ một structure cụ thể.

## Mental Model

> Augmentation là lưu **summary của subtree** để một query có thể loại cả subtree mà không inspect từng node.

## Ví dụ: k-th smallest bằng subtree size

Giả sử mỗi node có `size`. Với rank `k` tính từ 1:

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

Ta không cần inorder traversal toàn tree. `leftSize` cho biết có chính xác bao nhiêu keys nhỏ hơn current key trong subtree hiện tại. Trên balanced tree, mỗi bước đi xuống một level nên query `O(log n)`.

Rank query làm chiều ngược lại: khi đi right, toàn bộ left subtree và current node chắc chắn nhỏ hơn target, nên cộng `leftSize + 1`.

## Interval overlap không chỉ là “range query”

Hai intervals `[a,b]` và `[c,d]` overlap theo closed-interval semantics khi:

\[
a \le d \land c \le b
\]

Nếu domain dùng half-open interval `[a,b)`, điều kiện boundary khác. Data structure chỉ đúng khi semantics interval được xác định trước.

Interval tree thường order nodes theo `start`. Metadata `maxEnd` giúp prune: nếu `left.maxEnd < query.start`, không interval nào ở left có thể chạm query.

## Augmentation và prefix/range structures

Augmented BST và Segment Tree đều lưu summary, nhưng solve mutation models khác nhau. Segment tree có coordinate/range hierarchy gần cố định; augmented BST giữ dynamic ordered keys. Nếu keys insert/delete động và cần rank/predecessor, augmented balanced BST tự nhiên hơn. Nếu index domain ổn định và cần range aggregate mạnh, segment tree thường đơn giản hơn.

## Một nguyên tắc thiết kế tổng quát

Khi muốn thêm query mới vào tree, hãy hỏi:

> “Có summary nào của một subtree giúp tôi quyết định bỏ qua toàn subtree đó không?”

Nếu summary có thể combine từ children trong `O(1)`, augmentation thường giữ update `O(log n)` trên balanced tree. Nếu summary cần nhìn toàn subtree mỗi lần rotation/update, lợi thế biến mất.

## Common failure: cập nhật metadata không đúng thứ tự

Sau rotation, phải recompute node thấp hơn trước rồi node mới ở trên. Nếu tính parent bằng metadata child cũ, BST ordering vẫn đúng nhưng rank/interval query sai âm thầm.

Vì vậy augmented tree nên có một hàm duy nhất kiểu:

```text
pull(node)
```

để tái tính mọi metadata từ local data và children sau mỗi structural change.

## Mental Model mở rộng

> Balanced tree quyết định **đi đâu** bằng key order. Augmentation thêm đủ summary để quyết định **có cần đi vào subtree đó không** hoặc **subtree đó đóng góp bao nhiêu vào câu trả lời**.
