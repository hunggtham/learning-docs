# cây tìm kiếm nhị phân
**Cây tìm kiếm nhị phân (Binary Search Tree, BST / 이진 탐색 트리)**

cây tìm kiếm nhị phân thêm một **bất biến thứ tự / 정렬 불변식** lên cây nhị phân để việc search không cần duyệt toàn bộ structure. Với mỗi nút `x`, một formulation phổ biến là:

```text
mọi key trong left subtree  < x.key
mọi key trong right subtree > x.key
```

Nếu miền bài toán cho phép khóa trùng, chính sách phải được định nghĩa ngay từ đầu: từ chối khóa trùng, lưu số lần xuất hiện/danh sách giá trị trong nút, hoặc luôn đưa khóa bằng nhau về một phía theo quy tắc cố định. BST đúng không chỉ vì từng nút trông hợp lý; nó đúng vì **mọi cây con** đều thỏa cùng bất biến (invariant).

## Từ tìm kiếm nhị phân trên mảng tới BST

mảng đã sắp xếp cho tìm kiếm nhị phân `O(log n)` vì midpoint phép so sánh loại nửa các ứng viên. Nhưng insert vào giữa mảng cần dịch chuyển nhiều các phần tử, thường `O(n)`.

BST giữ thứ tự đã sắp xếp bằng các liên kết thay vì vị trí liên tiếp cố định. Mỗi phép so sánh khi tìm kiếm vẫn loại bỏ được một cây con; thao tác chèn/xóa có thể nối lại cục bộ các nút thay vì dịch toàn bộ phần đuôi dữ liệu.

sự đánh đổi (trade-off) là hiệu năng giờ phụ thuộc **chiều cao `h`**:

```text
search   O(h)
insert   O(h)
delete   O(h)
```

Nếu cây balanced, `h = O(log n)`. Nếu cây thoái hóa thành chain, `h = O(n)`.

Đây là insight trung tâm: BST không bảo đảm logarithmic time chỉ nhờ bất biến thứ tự. Muốn trường hợp xấu nhất logarithmic còn cần balancing strategy.

## Search như một chứng minh bằng loại trừ

Tại nút `x`:

```text
target < x.key  -> right subtree chắc chắn không chứa target
target > x.key  -> left subtree chắc chắn không chứa target
target = x.key  -> tìm thấy
```

Mỗi bước search hợp lệ vì BST bất biến cho phép **chứng minh cả một cây con không thể chứa answer**.

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

Nếu thao tác chèn/xóa phá bất biến dù chỉ tại một nút, mã vẫn có thể biên dịch và chạy nhưng lập luận “bỏ qua cây con này là an toàn” không còn đúng.

## Insert

Thao tác chèn trước hết tìm tới vị trí `null` nơi khóa phải nằm.

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

Tính đúng đắn đến từ việc vị trí chèn được xác định bằng cùng các phép so sánh như khi tìm kiếm. Nếu ta dừng ở `null` trong nhánh trái của nút `x`, các ràng buộc từ mọi tổ tiên đã chứng minh khóa thuộc đúng khoảng giá trị đó.

Một cách nhìn hữu ích là mỗi nút chia numeric/order space thành các interval nhỏ hơn. đường tìm kiếm không chỉ đi qua các nút; nó liên tục thu hẹp interval hợp lệ của khóa.

## phần tử trùng chính sách không phải chi tiết nhỏ

Ba chính sách phổ biến:

```text
1. reject duplicate
2. node lưu key + count/list values
3. equal key luôn đi một side theo rule cố định
```

Chính sách thứ hai thường rõ ràng hơn nếu khóa đại diện cho định danh còn nhiều bản ghi có thể chia sẻ cùng khóa. Chính sách thứ ba vẫn có thể đúng, nhưng truy vấn khoảng, tìm kiếm và xóa phải tuân thủ cùng một quy tắc.

Trong hệ thống thực tế map/set sự trừu tượng (abstraction), khóa equality còn liên quan hợp đồng bộ so sánh. Nếu comparator cho rằng hai các khóa bằng nhau (`compare(a,b)==0`) thì ordered set/map thường coi chúng là cùng vị trí order, dù định danh đối tượng khác.

## Minimum, maximum, successor, predecessor

Phần tử nhỏ nhất của BST được tìm bằng cách đi liên tục sang trái; phần tử lớn nhất tương tự bằng cách đi sang phải.

Successor của nút `x` là khóa nhỏ nhất lớn hơn `x.key`.

Nếu `x` có right cây con, successor là minimum của right cây con.

Nếu không có right cây con, ta đi lên ancestors cho tới tổ tiên đầu tiên mà `x` nằm trong left cây con của tổ tiên đó.

Predecessor đối xứng.

Các thao tác này là lý do ordered map/cây mạnh hơn bảng băm (Hash Table). bảng băm biết “khóa này có không?”, nhưng không tự nhiên biết “khóa gần nhất nhỏ hơn X là gì?”.

## Delete là thao tác khó nhất của BST cơ bản

Delete có ba case.

### Case 1 — nút lá

Không có nút con, chỉ cần bỏ link từ nút cha.

### Case 2 — một nút con

Ta thay nút bằng nút con duy nhất của nó. Vì toàn bộ cây con đó đã thỏa khoảng thứ tự của nút cũ, việc nối lại liên kết vẫn giữ bất biến.

### Case 3 — hai các nút con

Ta không thể đơn giản đưa một nút con lên nếu vẫn muốn giữ cả hai các cây con. Strategy phổ biến là thay nút bằng **inorder successor** — minimum của right cây con — rồi xóa successor ở vị trí cũ.

Tại sao successor an toàn?

- nó lớn hơn mọi khóa trong left cây con vì nó nằm trong right cây con của nút cũ;
- nó là phần tử nhỏ nhất bên phải, nên sau khi lên vị trí nút cũ, các khóa còn lại trong right cây con vẫn không nhỏ hơn nó;
- successor không có left nút con, nên delete lần hai giảm về case đơn giản hơn.

Có thể dùng predecessor đối xứng.

## Delete bằng transplant

Trong cách triển khai có các con trỏ tới nút cha, một helper `transplant(u, v)` thay cây con rooted at `u` bằng cây con rooted at `v`. Đây là sự trừu tượng giúp tách “relink parent-child” khỏi logic chọn successor.

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

Cách này làm rõ bất biến hơn code gán con trỏ ad-hoc ở nhiều chỗ.

## Inorder traversal và thứ tự đã sắp xếp

Inorder traversal:

```text
left -> root -> right
```

trả các khóa theo thứ tự đã sắp xếp vì mọi khóa bên trái nhỏ hơn nút gốc và mọi khóa bên phải lớn hơn nút gốc, recursively.

Đây là một theorem đơn giản nhưng cực quan trọng: cục bộ bất biến ở từng nút đủ để suy ra toàn cục thứ tự đã sắp xếp của toàn cây.

## truy vấn khoảng (range query)

Muốn lấy các khóa trong `[L, R]`, không cần quét cả cây.

```text
nếu node.key > L: left subtree có thể chứa answer
nếu L <= node.key <= R: output node
nếu node.key < R: right subtree có thể chứa answer
```

Trong balanced BST, complexity gần:

\[
O(\log n + k)
\]

với `k` là số kết quả đầu ra. Đây là **nhạy theo kích thước đầu ra complexity**: nếu truy vấn cần trả hàng triệu records, không structure nào tránh được chi phí tương ứng với số đầu ra.

## BST shape phụ thuộc thứ tự chèn

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

Search giờ là linear. ngẫu nhiên thứ tự chèn thường cho kỳ vọng chiều cao tốt hơn, nhưng đó không phải trường hợp xấu nhất bảo đảm.

AVL, cây đỏ-đen (Red-Black Tree), Treap hoặc các cấu trúc ngẫu nhiên kiểu Skip List tồn tại vì ta cần kiểm soát cả hình dạng cây, không chỉ thứ tự khóa.

## BST vs mảng đã sắp xếp

BST và mảng đã sắp xếp cùng khai thác thứ tự toàn phần nhưng tối ưu khối lượng công việc khác nhau.

mảng đã sắp xếp:

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

Nếu khối lượng công việc tĩnh và đọc nhiều, mảng đã sắp xếp có thể tốt hơn cây dù Big-O tra cứu giống nhau. Đây là ví dụ cho thấy tính cục bộ (locality) và sự thay đổi dữ liệu mẫu quan trọng ngang asymptotic complexity.

## BST vs HashMap

`HashMap` thường cho phép tra cứu theo quan hệ bằng nhau với chi phí kỳ vọng `O(1)`, nhưng không duy trì thứ tự.

Balanced BST cho `O(log n)` nhưng hỗ trợ:

```text
min/max
floor/ceiling
predecessor/successor
range iteration
ordered traversal
```

Câu hỏi đúng không phải “HashMap nhanh hơn TreeMap đúng không?” mà là “khối lượng công việc có cần order ngữ nghĩa (semantics) không?”.

## nút cha con trỏ, iterator và ordered traversal

Nếu nút có nút cha con trỏ, successor/predecessor có thể tìm bằng upward navigation. Điều này giúp iterator không cần stack lớn nếu cây structure ổn định.

Nhưng nút cha con trỏ tạo thêm bất biến: rotation, delete và transplant đều phải cập nhật nó chính xác. Nếu một trường không cần cho API/khối lượng công việc, đừng thêm chỉ vì “có vẻ tiện”.

## Augmented BST

BST nút có thể lưu thêm siêu dữ liệu nếu siêu dữ liệu recompute được từ các nút con.

Ví dụ:

```text
subtreeSize
subtreeSum
maxEndpoint
min/max key
```

Nếu cập nhật siêu dữ liệu trên đường đi thay đổi, ta có thể hỗ trợ order thống kê hoặc interval các truy vấn.

Một cây thống kê thứ tự (order-statistics tree) có trường `size` có thể trả phần tử nhỏ thứ k bằng cách xét kích thước cây con trái:

```text
leftSize = size(left)

k == leftSize + 1 -> current node
k <= leftSize     -> go left
k > leftSize + 1  -> go right với k giảm
```

Raw BST có thể làm được, nhưng muốn bảo đảm `O(log n)` vẫn cần balance.

## BST như một decision cây của các phép so sánh

Mỗi đường tìm kiếm là một sequence các phép so sánh. chiều cao chính là số các phép so sánh trường hợp xấu nhất theo cây shape.

Điều này nối BST với thông tin theory: cây càng lệch, một số các khóa cần nhiều các phép so sánh. Self-balancing cây đang trả maintenance chi phí trong cập nhật để giữ decision cây không quá sâu.

## Comparator và thứ tự toàn phần

Một BST tổng quát không nhất thiết dùng integer `<`. Nó dựa trên comparator.

Comparator cần có hành vi nhất quán với thứ tự toàn phần:

```text
antisymmetry
transitivity
consistency
```

Nếu comparator bất nhất, cây có thể đưa cùng khóa về các directions mâu thuẫn và search không còn reliable.

Trong Java:

```java
Comparator<User> byId = Comparator.comparingLong(User::id);
```

Tránh comparator kiểu `a.id - b.id` nếu tràn số có thể xảy ra.

## Persistent BST

Nếu structure bất biến sau khi tạo hoặc cần version lịch sử, cập nhật có thể **path-copy** chỉ các nút trên đường tìm kiếm và reuse phần còn lại.

Với balanced persistent cây, một cập nhật tạo `O(log n)` các nút mới thay vì copy cả cây. Đây là chia sẻ cấu trúc — rất quan trọng trong lập trình hàm, versioned data và persistent trạng thái (state) các hệ thống.

## Concurrency note

BST sự thay đổi dữ liệu có thể thay nhiều links và rotations. Concurrent ordered maps vì thế cần synchronization strategy phức tạp hơn đơn giản đặt mutex quanh một variable.

Trong hệ thống thực tế, concurrent các cây có thể dùng coarse-grained lock, fine-grained lock, optimistic techniques hoặc completely different structures. DSA bất biến vẫn là nền tảng, nhưng concurrency thêm một lớp bất biến về atomicity/visibility.

## Những hiểu lầm phổ biến

“BST search luôn O(log n)” là sai với unbalanced BST.

“cây nhị phân” không đồng nghĩa BST.

“Inorder luôn sorted” chỉ đúng khi bất biến thứ tự thật sự được duy trì.

“Delete nút hai các nút con chỉ cần copy successor khóa” có thể chưa đủ nếu nút chứa giá trị, siêu dữ liệu hoặc identity ngữ nghĩa phức tạp; phải chuyển đúng record/các trường theo hợp đồng API.

“ngẫu nhiên BST thường tốt” không thay thế xác định bảo đảm nếu đầu vào có thể đối kháng.

## kiểm thử BST

Ngoài kiểm tra kết quả tìm kiếm, hãy xác minh bất biến sau các chuỗi chèn/xóa ngẫu nhiên:

```text
inorder strictly/non-strictly sorted theo duplicate policy
node count đúng
mọi subtree key nằm trong allowed range
parent pointers đúng nếu có
metadata == recomputation từ children
```

Một bộ xác minh mạnh dùng range các ràng buộc:

```text
validate(node, low, high)
```

thay vì chỉ check `left < node < right`, vì violation có thể nằm sâu hơn một tầng.

## Mô hình tư duy

> BST biến **toàn cục thứ tự đã sắp xếp** thành **cục bộ branching quy tắc**. Mỗi phép so sánh không chỉ chọn nút con; nó loại cả một interval các khóa. Search nhanh khi cây chiều cao thấp. cập nhật mạnh vì structure động, nhưng chính sự thay đổi dữ liệu tạo rủi ro shape lệch nên balancing trở thành bước tiến tự nhiên tiếp theo.

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