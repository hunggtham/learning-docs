# Cây tìm kiếm cân bằng
**Balanced Search Trees / 균형 탐색 트리**

Cây tìm kiếm nhị phân chỉ thật sự hữu ích khi chiều cao được kiểm soát. Với cùng một tập khóa, một BST có thể thấp gần `log n`, nhưng cũng có thể suy thoái thành chuỗi dài gần `n` nếu thứ tự chèn xấu.

Mọi thao tác cơ bản thực chất có chi phí theo chiều cao:

\[
search, insert, delete = O(h)
\]

Vì vậy **cây tìm kiếm cân bằng** thêm một bất biến về hình dạng để bảo đảm:

\[
h = O(\log n)
\]

Ta trả thêm chi phí sửa cấu trúc khi cập nhật để đổi lấy cận tìm kiếm ổn định.

## 1. Hai lớp bất biến khác nhau

Balanced BST duy trì đồng thời:

```text
BST invariant      -> thứ tự khóa
balance invariant  -> chiều cao/hình dạng được kiểm soát
```

Rotation tồn tại vì nó có thể sửa lớp thứ hai mà không phá lớp thứ nhất.

Điểm này rất quan trọng: balancing không làm cây “sorted hơn”; nó chỉ ngăn đường tìm kiếm dài quá mức.

## 2. Rotation bảo toàn thứ tự thế nào?

Right rotation:

```text
        y                     x
       / \                   / \
      x   C      --->        A   y
     / \                       / \
    A   B                     B   C
```

Trước và sau rotation, inorder sequence đều là:

```text
A < x < B < y < C
```

Rotation chỉ đổi quan hệ cha–con cục bộ. Chính vì inorder order không đổi nên BST invariant được giữ.

Nếu node có metadata như `height`, `size`, `maxEnd`, `sum`, metadata phải được cập nhật đúng thứ tự sau rotation.

## 3. Metadata Update Order

Sau right rotation ở `y`:

```text
y trở thành con của x
```

Nên recompute `y` trước, rồi `x`, vì metadata mới của `x` phụ thuộc metadata mới của `y`.

Pattern tổng quát:

> Khi relink tree, cập nhật metadata từ dưới lên theo topology mới.

Sai thứ tự có thể tạo cây đúng về BST nhưng sai về augmentation.

## 4. AVL Tree

AVL giữ balance factor:

\[
BF(u)=height(left(u))-height(right(u))
\]

và yêu cầu:

\[
BF(u)\in\{-1,0,1\}
\]

ở mọi node.

Đây là một invariant cân bằng khá chặt.

## 5. Vì sao AVL có chiều cao logarithmic?

Gọi `N(h)` là số node ít nhất của AVL height `h`.

Để đạt height `h` với ít node nhất nhưng vẫn hợp lệ, hai subtree phải có height `h-1` và `h-2`:

\[
N(h)=1+N(h-1)+N(h-2)
\]

Recurrence này tăng cùng cấp với Fibonacci, tức tăng theo hàm mũ của `h`.

Do đó đảo lại:

\[
h=O(\log n)
\]

Đây là bản chất của bảo đảm chiều cao AVL.

## 6. Bốn case AVL thực chất là hai hình dạng

Sau insert, một node có thể lệch trái hoặc lệch phải.

Nếu đường đi nặng cùng hướng:

```text
LL -> rotate right
RR -> rotate left
```

Nếu zig-zag:

```text
LR -> rotate left ở child, rồi rotate right
RL -> rotate right ở child, rồi rotate left
```

Không nên học bốn case như bốn mẹo. Hãy nhìn hình dạng:

> zig-zag cần biến thành straight line trước, sau đó một rotation chính sửa được imbalance.

## 7. AVL Insert

Quy trình:

1. insert như BST;
2. đi ngược path;
3. recompute height;
4. tính balance factor;
5. rotate nếu vi phạm;
6. tiếp tục cập nhật metadata cần thiết.

Insertion chỉ ảnh hưởng các tổ tiên của vị trí chèn.

## 8. AVL Delete khó hơn Insert

Delete có thể làm height subtree giảm. Sau khi sửa một imbalance, height của subtree mới vẫn có thể thấp hơn trước, tiếp tục làm ancestor cao hơn mất cân bằng.

Vì vậy delete thường phải tiếp tục kiểm tra tới root.

Đây là khác biệt quan trọng giữa:

```text
insert -> height có thể tăng
remove -> height có thể giảm dây chuyền
```

## 9. Red-Black Tree

Red-Black Tree không theo dõi chênh lệch height trực tiếp. Nó dùng màu để encode một ràng buộc cân bằng mềm hơn.

Các invariant phổ biến:

1. mỗi node đỏ hoặc đen;
2. root đen;
3. null leaf được xem là đen;
4. node đỏ không có child đỏ;
5. mọi path từ một node tới null leaf có cùng số node đen.

Số node đen trên path được gọi là **black height**.

## 10. Vì sao Red-Black cũng logarithmic?

Vì không có hai node đỏ liên tiếp, trên một root-to-leaf path số node đỏ không vượt số node đen đáng kể.

Mọi path có cùng black height, nên path dài nhất không quá khoảng hai lần path ngắn nhất theo số level liên quan.

Từ đó suy ra:

\[
h=O(\log n)
\]

Red-Black cho phép hình dạng “lỏng” hơn AVL nhưng vẫn đủ giữ logarithmic bound.

## 11. Red-Black Insert

Node mới thường được tô đỏ để không làm tăng black height ngay lập tức.

Vấn đề chỉ xuất hiện nếu parent cũng đỏ.

Hai hướng repair chính:

### Uncle đỏ

Recolor parent và uncle thành đen, grandparent thành đỏ, rồi tiếp tục kiểm tra grandparent.

### Uncle đen/null

Dùng rotation + recolor để loại red-red violation tại chỗ.

Mô hình tư duy:

> insertion repair bảo vệ đồng thời “không red-red” và “black height không đổi không hợp lệ”.

## 12. Red-Black Delete

Xóa node đen có thể làm một nhánh thiếu một đơn vị black height.

Nhiều tài liệu dùng khái niệm **double black** để mô hình hóa thiếu hụt này.

Các case sibling đỏ/đen và child đỏ/đen thực chất là những cách:

```text
chuyển thiếu hụt black lên trên
hoặc
phân phối lại black bằng rotation/recolor
```

Nếu chỉ học case mà không hiểu black-height deficit, implementation rất khó nhớ và debug.

## 13. AVL vs Red-Black

AVL cân bằng chặt hơn nên thường có chiều cao thấp hơn một chút. Red-Black cho phép nhiều shape hơn, thường cần ít rotation hơn trong update-heavy workload.

Một cách định hướng:

```text
lookup-heavy / latency lookup quan trọng   -> AVL có thể hấp dẫn
ordered map/set tổng quát                  -> Red-Black rất phổ biến
external-memory                            -> B/B+Tree phù hợp hơn
concurrent ordered structure               -> có thể cân nhắc Skip List hoặc tree chuyên dụng
```

Không nên coi đây là luật tuyệt đối. Cache locality, allocator, comparator cost và implementation quality đều ảnh hưởng thực tế.

## 14. Treap: Balance bằng Random Priority

Treap giữ:

```text
BST order theo key
heap order theo random priority
```

Nếu priorities độc lập ngẫu nhiên, expected height là `O(log n)`.

Treap cho thấy balance không nhất thiết đến từ deterministic metadata như height hoặc color. Randomness cũng có thể tạo expected balance.

## 15. Split và Merge trong Treap

Treap đặc biệt mạnh vì `split` và `merge` rất tự nhiên.

`split(root,key)` chia thành:

```text
L: keys < key
R: keys >= key
```

`merge(L,R)` yêu cầu mọi key của `L` nhỏ hơn mọi key của `R`, rồi dùng heap priority để chọn root.

Nhiều sequence/data-structure operations có thể xây từ split/merge thay vì viết insert/delete riêng.

## 16. Implicit Treap

Nếu không lưu key explicit mà coi inorder position là index logic, subtree size cho phép tìm phần tử thứ `k`.

Khi đó Treap có thể biểu diễn sequence động với:

```text
split theo position
merge sequences
insert/delete interval
reverse interval bằng lazy flag
range aggregate nếu augment
```

Đây là cầu nối giữa balanced tree và dynamic array/rope.

## 17. Splay Tree

Splay Tree không giữ balance invariant cứng. Sau access, node được đưa lên root bằng zig, zig-zig, zig-zag rotations.

Một thao tác có thể `O(n)`, nhưng amortized `O(log n)`.

Điểm thú vị là structure tự thích nghi: item được truy cập gần đây hoặc thường xuyên có xu hướng gần root.

Splay Tree minh họa trade-off giữa worst-case per operation và adaptive locality.

## 18. Weight-Balanced Tree

Có thể cân bằng dựa trên subtree size thay vì height/color.

Ví dụ yêu cầu hai subtree không quá lệch theo tỷ lệ. Khi vi phạm, rotate/rebuild.

Ý tưởng quan trọng:

> “Balanced” không chỉ có một định nghĩa; miễn invariant đủ mạnh để bound height hoặc expected cost.

## 19. Scapegoat Tree

Scapegoat Tree tránh lưu balance metadata ở mọi node. Khi insertion làm tree quá cao, tìm một ancestor “scapegoat” có subtree mất cân bằng rồi rebuild toàn subtree đó thành cây cân bằng.

Một update riêng có thể đắt, nhưng amortized bound tốt.

Đây là ví dụ khác của deamortized-vs-amortized design space.

## 20. B-Tree là Balanced Search Tree cho Page I/O

B-Tree/B+Tree cũng cân bằng, nhưng node có nhiều child.

Mục tiêu không chỉ giảm số comparison mà giảm số page access.

Balanced binary tree height `O(log_2 n)`; B-Tree với fanout `B` có height gần:

\[
O(\log_B n)
\]

Balanced-tree design phải khớp cost model của storage medium.

## 21. Ordered Map Capability

Balanced BST hỗ trợ tự nhiên:

```text
minimum / maximum
floor / ceiling
predecessor / successor
lower_bound / upper_bound
range iteration
```

Hash Table không giữ global order nên không hỗ trợ các query này tự nhiên.

Đây là khác biệt capability, không chỉ complexity.

## 22. Duplicate Keys

Phải xác định policy:

```text
reject duplicate
count frequency trong node
lưu multiset entries
augment bằng tie-break unique id
```

Nếu comparator trả `0`, ordered map thường xem hai key là cùng ordering position.

Comparator semantics là một phần của identity trong tree.

## 23. Comparator Contract

Comparator cần ít nhất tính nhất quán và bắc cầu.

Nếu:

```text
a < b
b < c
nhưng c < a
```

search path không còn có nghĩa toán học.

Một rotation hoàn hảo cũng không cứu được tree có comparator không tạo ordering hợp lệ.

## 24. Augmentation

Balanced Tree là framework rất mạnh khi mỗi node lưu summary từ subtree.

Ví dụ:

```text
size
sum
maxEnd
min/max
custom aggregate
```

Nếu summary được tính từ child trong `O(1)`, rotation chỉ cần recompute vài node cục bộ nên asymptotic update thường vẫn `O(log n)`.

## 25. Order Statistics

Lưu:

\[
size(u)=1+size(left)+size(right)
\]

cho phép:

```text
select(k) -> phần tử nhỏ thứ k
rank(x)   -> số key nhỏ hơn x
```

mỗi query `O(log n)` trên balanced tree.

Đây là ví dụ augmentation biến ordered set thành order-statistic tree.

## 26. Interval Tree

Nếu node keyed theo interval start và lưu `maxEnd` của subtree, có thể prune subtree không thể giao query interval.

Balanced invariant giữ height; augmentation giữ summary phục vụ overlap query.

Hai lớp bất biến hoạt động độc lập nhưng phải cùng được bảo trì sau rotation.

## 27. Persistent Balanced Tree

Với immutable/persistent tree, update chỉ sao chép các node trên search path và chia sẻ subtree không đổi.

Nếu tree height `O(log n)`, một update tạo `O(log n)` node mới.

Persistent Red-Black/AVL/Treap có thể hỗ trợ snapshot/versioning hiệu quả.

## 28. Parent Pointer và Iterator

Nếu cần iterator predecessor/successor nhanh, parent pointer có thể hữu ích.

Nhưng mỗi rotation phải cập nhật parent pointer đúng.

Nếu iterator giữ raw node reference, delete/rotation/invalidation semantics phải được định nghĩa rõ.

## 29. Memory Layout

Node-based trees có pointer chasing và object overhead.

Với dữ liệu nhỏ/tĩnh, sorted array có thể nhanh hơn tree dù insert/delete tệ hơn, vì:

```text
contiguous memory
fewer allocations
better cache locality
```

Balanced Tree đáng giá khi mutation/order queries thực sự cần.

## 30. Concurrent Balanced Trees

Concurrent tree khó hơn Hash Map hoặc Skip List vì rotation thay đổi nhiều pointer liên quan.

Fine-grained locking phải xác định lock order để tránh deadlock. Lock-free tree cần linearization, memory ordering và reclamation rất phức tạp.

Đây là lý do concurrent ordered maps đôi khi dùng Skip List: expected `O(log n)` nhưng update topology cục bộ theo level có thể thuận lợi hơn.

## 31. Optimistic Read

Một số implementation cho reader đọc mà không khóa toàn tree, rồi validate version/stamp để phát hiện writer đã thay đổi cấu trúc.

Mẫu này đánh đổi retry để giảm contention read-heavy.

Data structure concurrency không chỉ chọn lock hay no-lock; có cả optimistic validation và copy-on-write.

## 32. Bulk Build

Nếu đã có sorted keys, xây balanced BST không cần insert từng phần tử.

Chọn middle làm root đệ quy tạo tree height tối ưu gần nhất trong `O(n)`.

Nếu dùng insert lặp, dù mỗi insert `O(log n)`, total `O(n log n)`.

Static/batch workload thường cho phép construction tốt hơn online workload.

## 33. Join-Based Balanced Trees

Một góc nhìn nâng cao là xây các operation từ `split` và `join`.

Nếu có primitive:

```text
split(T, key)
join(L, key, R)
```

thì union/intersection/difference của ordered sets có thể được xây đệ quy hiệu quả.

Cách nhìn này đặc biệt hữu ích trong functional/persistent trees.

## 34. Set Union giữa hai Trees

Nếu một set nhỏ hơn nhiều set kia, không nhất thiết insert từng key đơn giản.

Split/join algorithms có thể tận dụng cấu trúc của cả hai tree và đạt complexity phụ thuộc kích thước tương đối tốt hơn trong một số mô hình.

Đây là ví dụ operation set cao cấp có thể ảnh hưởng lựa chọn tree family.

## 35. Tree Validator

BST validator phải kiểm tra global range, không chỉ parent-child.

AVL validator:

```text
BST order
stored height đúng
|BF| <= 1
```

Red-Black validator:

```text
BST order
root black
no red-red
mọi root-to-null path cùng black height
```

Augmented tree còn phải kiểm tra metadata.

Validator sau random operations rất đáng giá khi tự implement.

## 36. Differential Testing

Có thể so custom tree với standard ordered map/set:

```text
insert/delete/contains
min/max
floor/ceiling
range iteration
```

Sau mỗi operation, kiểm tra inorder output và invariants.

Rotation bugs thường chỉ lộ sau sequence dài, nên stateful random testing rất hữu ích.

## 37. Những hiểu lầm phổ biến

“BST luôn `O(log n)`” — sai nếu không có balance guarantee.

“AVL luôn nhanh hơn Red-Black” — sai; workload và update cost khác nhau.

“Rotation chỉ đổi hình vẽ” — sai; metadata/parent/iterator semantics phải được bảo trì.

“Balanced Tree tốt hơn sorted array vì insert nhanh” — chưa chắc nếu dữ liệu gần tĩnh và locality quan trọng.

“Red-Black color chỉ là implementation trick” — màu là encoding của invariant giúp chứng minh height bound.

## Mô hình tư duy

> Balanced Search Tree trả một **chi phí bảo trì cục bộ sau update** để mua một **cận toàn cục cho chiều cao**.

AVL dùng height difference, Red-Black dùng black-height + màu, Treap dùng random priority, Splay dùng amortized self-adjustment, B-Tree dùng multiway occupancy phù hợp page I/O.

Khi chọn hoặc triển khai balanced tree, hãy hỏi: **cần deterministic hay expected guarantee, read/write ratio ra sao, có cần augmentation/persistence/split-merge không, memory locality có quan trọng không, và liệu sorted array hoặc Skip List đã phù hợp hơn chưa?**

Xem thêm: [Binary Search Trees](./01_binary_search_trees.md), [Augmented Trees](./06_augmented_trees_and_order_statistics.md), [Skip Lists](./07_skip_lists.md), [B/B+Tree](./05_b_trees_and_external_memory.md).