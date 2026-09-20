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
