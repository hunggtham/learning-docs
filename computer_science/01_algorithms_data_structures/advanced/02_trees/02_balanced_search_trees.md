# Balanced Search Trees
**Cây tìm kiếm cân bằng (Balanced Search Tree / 균형 탐색 트리)**

BST chỉ nhanh nếu height nhỏ. Balanced search tree thêm invariant để ngăn structure suy thoái thành linked list.

## Rotation

Rotation thay đổi local shape mà không phá inorder order.

```text
        y              x
       / \            / \
      x   C   ->     A   y
     / \                / \
    A   B              B   C
```

Inorder trước/sau đều là `A, x, B, y, C`.

## AVL Tree

AVL giữ balance factor:

\[
BF=height(left)-height(right)
\]

và yêu cầu `BF` nằm trong `{-1,0,1}`. Cân bằng chặt giúp lookup rất tốt nhưng updates có thể cần rotations thường hơn.

## Red-Black Tree

Red-Black Tree dùng color invariants để bound height ở `O(log n)`. Java `TreeMap` và `TreeSet` dùng red-black tree. Nó thường cân bằng lỏng hơn AVL nhưng update thuận lợi.

## B-Tree và B+Tree

Storage/database có cost model khác RAM. Disk/page access đắt hơn comparison, nên tree node chứa nhiều keys/children để giảm height và số I/O. B+Tree thường giữ records ở leaves và internal nodes chủ yếu routing; leaves có thể linked để range scan nhanh.

Đây là ví dụ quan trọng: data structure tốt phải khớp phần cứng và workload.

## HashMap hay TreeMap?

Hash map phù hợp exact lookup expected `O(1)`. Tree map thích hợp nếu cần keys sorted, `floor`, `ceiling`, min/max, predecessor/successor hoặc range.

## Mental Model

> Balancing là trả maintenance cost nhỏ sau mỗi update để ngăn future searches trở nên đắt.

## AVL insertion từ invariant

Sau insert như BST bình thường, chỉ các ancestors trên search path có thể đổi height. Ta đi ngược lên và kiểm tra balance factor.

Bốn shape kinh điển không phải bốn mẹo rời rạc. Chúng là hai kiểu imbalance — left-heavy hoặc right-heavy — kết hợp hướng của child path.

```text
LL -> right rotation
RR -> left rotation
LR -> left rotation ở child, rồi right rotation
RL -> right rotation ở child, rồi left rotation
```

Rotation sửa shape nhưng giữ inorder sequence, vì vậy giữ BST order invariant.

## Red-Black invariants và giới hạn height

Một formulation phổ biến dùng các property như root/leaf sentinel màu đen, red node không có red child, và mọi path từ node tới descendant null leaves có cùng số black nodes. Từ đó suy ra longest path không quá khoảng gấp đôi shortest path; height là `O(log n)`.

Điểm quan trọng không phải học từng case recolor. Cần hiểu rằng color là **metadata dùng để encode một bound lỏng hơn về balance**, đổi lại update ít rigid hơn AVL.

## Ordered map như một abstraction mạnh hơn exact lookup

Với balanced BST, ta có thể hỗ trợ:

```text
floor(key)
ceiling(key)
lower(key)
higher(key)
subMap(L, R)
```

Đây là các operation không tự nhiên với hash table. Trong Java, `NavigableMap` biểu diễn abstraction này rất rõ.

## Augmentation

Ta có thể thêm metadata vào mỗi node nếu metadata có thể recompute từ children. Ví dụ `subtreeSize` cho phép trả lời k-th smallest và rank query trong `O(log n)` trên balanced tree.

Nếu mỗi rotation/update đều recompute metadata đúng, augmentation không phá asymptotic update cost.

Mental model này mở đường cho order-statistics tree và interval tree.
