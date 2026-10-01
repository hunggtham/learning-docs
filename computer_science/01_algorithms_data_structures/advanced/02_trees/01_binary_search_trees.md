# cây tìm kiếm nhị phân

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **cây tìm kiếm nhị phân**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ tìm kiếm nhị phân trên mảng tới BST** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Tìm kiếm (search / 검색) như một chứng minh bằng loại trừ** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Cây tìm kiếm nhị phân (Binary Search Tree, BST / 이진 탐색 트리)**

cây tìm kiếm nhị phân thêm một **bất biến thứ tự / 정렬 불변식** lên cây nhị phân để việc tìm kiếm (search / 검색) không cần duyệt toàn bộ cấu trúc (structure / 구조). Với mỗi nút `x`, một formulation phổ biến là:

```text
mọi key trong left subtree  < x.key
mọi key trong right subtree > x.key
```

Nếu miền bài toán cho phép khóa trùng, chính sách phải được định nghĩa ngay từ đầu: từ chối khóa trùng, lưu số lần xuất hiện/danh sách giá trị trong nút, hoặc luôn đưa khóa bằng nhau về một phía theo quy tắc cố định. BST đúng không chỉ vì từng nút trông hợp lý; nó đúng vì **mọi cây con** đều thỏa cùng bất biến (invariant / 불변식).

## Từ tìm kiếm nhị phân trên mảng tới BST

mảng đã sắp xếp cho tìm kiếm nhị phân `O(log n)` vì midpoint phép so sánh loại nửa các ứng viên. Nhưng insert vào giữa mảng cần dịch chuyển nhiều các phần tử, thường `O(n)`.

BST giữ thứ tự đã sắp xếp bằng các liên kết thay vì vị trí liên tiếp cố định. Mỗi phép so sánh khi tìm kiếm vẫn loại bỏ được một cây con; thao tác chèn/xóa có thể nối lại cục bộ các nút thay vì dịch toàn bộ phần đuôi dữ liệu.

Sự đánh đổi (trade-off / 트레이드오프) là hiệu năng giờ phụ thuộc **chiều cao `h`**:

```text
search   O(h)
insert   O(h)
delete   O(h)
```

Nếu cây balanced, `h = O(log n)`. Nếu cây thoái hóa thành chuỗi (chain / 사슬), `h = O(n)`.

Đây là insight trung tâm: BST không bảo đảm logarithmic thời gian (time / 시간) chỉ nhờ bất biến thứ tự. Muốn trường hợp xấu nhất logarithmic còn cần balancing chiến lược (strategy / 전략).

> **Chuyển mạch:** Trong **cây tìm kiếm nhị phân**, **Tìm kiếm (search / 검색) như một chứng minh bằng loại trừ** tiếp nhận điểm tựa từ **Từ tìm kiếm nhị phân trên mảng tới BST** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Insert** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm (search / 검색) như một chứng minh bằng loại trừ

Tại nút `x`:

```text
target < x.key  -> right subtree chắc chắn không chứa target
target > x.key  -> left subtree chắc chắn không chứa target
target = x.key  -> tìm thấy
```

Mỗi bước tìm kiếm (search / 검색) hợp lệ vì BST bất biến cho phép **chứng minh cả một cây con không thể chứa answer**.

Iterative C phiên bản (version / 버전):

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

> **Chuyển mạch:** Ở chặng này của **cây tìm kiếm nhị phân**, **Insert** tiếp nhận điểm tựa từ **Tìm kiếm (search / 검색) như một chứng minh bằng loại trừ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **phần tử trùng chính sách không phải chi tiết nhỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Một cách nhìn hữu ích là mỗi nút chia numeric/thứ tự (order / 순서) không gian (space / 공간) thành các interval nhỏ hơn. đường tìm kiếm không chỉ đi qua các nút; nó liên tục thu hẹp interval hợp lệ của khóa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây tìm kiếm nhị phân**, **phần tử trùng chính sách không phải chi tiết nhỏ** tiếp nhận điểm tựa từ **Insert** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Minimum, maximum, successor, predecessor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## phần tử trùng chính sách không phải chi tiết nhỏ

Ba chính sách phổ biến:

```text
1. reject duplicate
2. node lưu key + count/list values
3. equal key luôn đi một side theo rule cố định
```

Chính sách thứ hai thường rõ ràng hơn nếu khóa đại diện cho định danh còn nhiều bản ghi có thể chia sẻ cùng khóa. Chính sách thứ ba vẫn có thể đúng, nhưng truy vấn khoảng, tìm kiếm và xóa phải tuân thủ cùng một quy tắc.

Trong hệ thống thực tế map/set sự trừu tượng (abstraction), khóa equality còn liên quan hợp đồng bộ so sánh. Nếu comparator cho rằng hai các khóa bằng nhau (`compare(a,b)==0`) thì ordered set/map thường coi chúng là cùng vị trí thứ tự (order / 순서), dù định danh đối tượng khác.

> **Chuyển mạch:** Trong **cây tìm kiếm nhị phân**, **Minimum, maximum, successor, predecessor** tiếp nhận điểm tựa từ **phần tử trùng chính sách không phải chi tiết nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Delete là thao tác khó nhất của BST cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Minimum, maximum, successor, predecessor

Phần tử nhỏ nhất của BST được tìm bằng cách đi liên tục sang trái; phần tử lớn nhất tương tự bằng cách đi sang phải.

Successor của nút `x` là khóa nhỏ nhất lớn hơn `x.key`.

Nếu `x` có right cây con, successor là minimum của right cây con.

Nếu không có right cây con, ta đi lên ancestors cho tới tổ tiên đầu tiên mà `x` nằm trong left cây con của tổ tiên đó.

Predecessor đối xứng.

Các thao tác này là lý do ordered map/cây mạnh hơn bảng băm (hash table / 해시 테이블). bảng băm biết “khóa này có không?”, nhưng không tự nhiên biết “khóa gần nhất nhỏ hơn X là gì?”.

> **Chuyển mạch:** Ở chặng này của **cây tìm kiếm nhị phân**, **Delete là thao tác khó nhất của BST cơ bản** tiếp nhận điểm tựa từ **Minimum, maximum, successor, predecessor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Delete bằng transplant** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Delete là thao tác khó nhất của BST cơ bản

Delete có ba trường hợp (case / 사례).

### Trường hợp (case / 사례) 1 — nút lá

Không có nút con, chỉ cần bỏ link từ nút cha.

### Trường hợp (case / 사례) 2 — một nút con

Ta thay nút bằng nút con duy nhất của nó. Vì toàn bộ cây con đó đã thỏa khoảng thứ tự của nút cũ, việc nối lại liên kết vẫn giữ bất biến.

### Trường hợp (case / 사례) 3 — hai các nút con

Ta không thể đơn giản đưa một nút con lên nếu vẫn muốn giữ cả hai các cây con. chiến lược (strategy / 전략) phổ biến là thay nút bằng **inorder successor** — minimum của right cây con — rồi xóa successor ở vị trí cũ.

Tại sao successor an toàn?

- nó lớn hơn mọi khóa trong left cây con vì nó nằm trong right cây con của nút cũ;
- nó là phần tử nhỏ nhất bên phải, nên sau khi lên vị trí nút cũ, các khóa còn lại trong right cây con vẫn không nhỏ hơn nó;
- successor không có left nút con, nên delete lần hai giảm về trường hợp (case / 사례) đơn giản hơn.

Có thể dùng predecessor đối xứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây tìm kiếm nhị phân**, **Delete bằng transplant** tiếp nhận điểm tựa từ **Delete là thao tác khó nhất của BST cơ bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Inorder traversal và thứ tự đã sắp xếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Delete bằng transplant

Trong cách triển khai có các con trỏ tới nút cha, một helper `transplant(u, v)` thay cây con rooted at `u` bằng cây con rooted at `v`. Đây là sự trừu tượng giúp tách “relink parent-child” khỏi lô-gic (logic / 논리) chọn successor.

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

Cách này làm rõ bất biến hơn mã (code / 코드) gán con trỏ ad-hoc ở nhiều chỗ.

> **Chuyển mạch:** Trong **cây tìm kiếm nhị phân**, **Inorder traversal và thứ tự đã sắp xếp** tiếp nhận điểm tựa từ **Delete bằng transplant** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **truy vấn khoảng (range query)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inorder traversal và thứ tự đã sắp xếp

Inorder traversal:

```text
left -> root -> right
```

trả các khóa theo thứ tự đã sắp xếp vì mọi khóa bên trái nhỏ hơn nút gốc và mọi khóa bên phải lớn hơn nút gốc, recursively.

Đây là một theorem đơn giản nhưng cực quan trọng: cục bộ bất biến ở từng nút đủ để suy ra toàn cục thứ tự đã sắp xếp của toàn cây.

> **Chuyển mạch:** Ở chặng này của **cây tìm kiếm nhị phân**, **truy vấn khoảng (range query)** tiếp nhận điểm tựa từ **Inorder traversal và thứ tự đã sắp xếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BST shape phụ thuộc thứ tự chèn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## truy vấn khoảng (range query)

Muốn lấy các khóa trong `[L, R]`, không cần quét cả cây.

```text
nếu node.key > L: left subtree có thể chứa answer
nếu L <= node.key <= R: output node
nếu node.key < R: right subtree có thể chứa answer
```

Trong balanced BST, độ phức tạp (complexity / 복잡도) gần:

\[
O(\log n + k)
\]

với `k` là số kết quả đầu ra. Đây là **nhạy theo kích thước đầu ra độ phức tạp (complexity / 복잡도)**: nếu truy vấn cần trả hàng triệu records, không cấu trúc (structure / 구조) nào tránh được chi phí tương ứng với số đầu ra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây tìm kiếm nhị phân**, **BST shape phụ thuộc thứ tự chèn** tiếp nhận điểm tựa từ **truy vấn khoảng (range query)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BST vs mảng đã sắp xếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BST shape phụ thuộc thứ tự chèn

Insert:

```text
1, 2, 3, 4, 5
```

vào raw BST tạo chuỗi (chain / 사슬):

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

Tìm kiếm (search / 검색) giờ là tuyến tính (linear / 선형). ngẫu nhiên thứ tự chèn thường cho kỳ vọng chiều cao tốt hơn, nhưng đó không phải trường hợp xấu nhất bảo đảm.

AVL, cây đỏ-đen (Red-Black Tree), Treap hoặc các cấu trúc ngẫu nhiên kiểu Skip danh sách (list / 목록) tồn tại vì ta cần kiểm soát cả hình dạng cây, không chỉ thứ tự khóa.

> **Chuyển mạch:** Trong **cây tìm kiếm nhị phân**, **BST vs mảng đã sắp xếp** tiếp nhận điểm tựa từ **BST shape phụ thuộc thứ tự chèn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BST vs HashMap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Nếu khối lượng công việc tĩnh và đọc nhiều, mảng đã sắp xếp có thể tốt hơn cây dù Big-O tra cứu giống nhau. Đây là ví dụ cho thấy tính cục bộ (locality) và sự thay đổi dữ liệu mẫu quan trọng ngang asymptotic độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Ở chặng này của **cây tìm kiếm nhị phân**, **BST vs HashMap** tiếp nhận điểm tựa từ **BST vs mảng đã sắp xếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **nút cha con trỏ, iterator và ordered traversal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Câu hỏi đúng không phải “HashMap nhanh hơn TreeMap đúng không?” mà là “khối lượng công việc có cần thứ tự (order / 순서) ngữ nghĩa (semantics / 의미론) không?”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây tìm kiếm nhị phân**, **nút cha con trỏ, iterator và ordered traversal** tiếp nhận điểm tựa từ **BST vs HashMap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Augmented BST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## nút cha con trỏ, iterator và ordered traversal

Nếu nút có nút cha con trỏ, successor/predecessor có thể tìm bằng upward điều hướng (navigation / 내비게이션). Điều này giúp iterator không cần ngăn xếp (stack / 스택) lớn nếu cây cấu trúc (structure / 구조) ổn định.

Nhưng nút cha con trỏ tạo thêm bất biến: rotation, delete và transplant đều phải cập nhật nó chính xác. Nếu một trường không cần cho API/khối lượng công việc, đừng thêm chỉ vì “có vẻ tiện”.

> **Chuyển mạch:** Trong **cây tìm kiếm nhị phân**, **Augmented BST** tiếp nhận điểm tựa từ **nút cha con trỏ, iterator và ordered traversal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BST như một quyết định (decision / 결정) cây của các phép so sánh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Augmented BST

BST nút có thể lưu thêm siêu dữ liệu nếu siêu dữ liệu recompute được từ các nút con.

Ví dụ:

```text
subtreeSize
subtreeSum
maxEndpoint
min/max key
```

Nếu cập nhật siêu dữ liệu trên đường đi thay đổi, ta có thể hỗ trợ thứ tự (order / 순서) thống kê hoặc interval các truy vấn.

Một cây thống kê thứ tự (order-statistics tree) có trường `size` có thể trả phần tử nhỏ thứ k bằng cách xét kích thước cây con trái:

```text
leftSize = size(left)

k == leftSize + 1 -> current node
k <= leftSize     -> go left
k > leftSize + 1  -> go right với k giảm
```

Raw BST có thể làm được, nhưng muốn bảo đảm `O(log n)` vẫn cần balance.

> **Chuyển mạch:** Ở chặng này của **cây tìm kiếm nhị phân**, **Augmented BST** đã nêu tiêu chí phân biệt, còn **BST như một quyết định (decision / 결정) cây của các phép so sánh** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Comparator và thứ tự toàn phần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BST như một quyết định (decision / 결정) cây của các phép so sánh

Mỗi đường tìm kiếm là một chuỗi (sequence / 시퀀스) các phép so sánh. chiều cao chính là số các phép so sánh trường hợp xấu nhất theo cây shape.

Điều này nối BST với thông tin lý thuyết (theory / 이론): cây càng lệch, một số các khóa cần nhiều các phép so sánh. Self-balancing cây đang trả maintenance chi phí trong cập nhật để giữ quyết định (decision / 결정) cây không quá sâu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây tìm kiếm nhị phân**, **BST như một quyết định (decision / 결정) cây của các phép so sánh** đã nêu tiêu chí phân biệt, còn **Comparator và thứ tự toàn phần** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Persistent BST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Comparator và thứ tự toàn phần

Một BST tổng quát không nhất thiết dùng integer `<`. Nó dựa trên comparator.

Comparator cần có hành vi nhất quán với thứ tự toàn phần:

```text
antisymmetry
transitivity
consistency
```

Nếu comparator bất nhất, cây có thể đưa cùng khóa về các directions mâu thuẫn và tìm kiếm (search / 검색) không còn reliable.

Trong Java:

```java
Comparator<User> byId = Comparator.comparingLong(User::id);
```

Tránh comparator kiểu `a.id - b.id` nếu tràn số có thể xảy ra.

> **Chuyển mạch:** Trong **cây tìm kiếm nhị phân**, **Persistent BST** tiếp nhận điểm tựa từ **Comparator và thứ tự toàn phần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính đồng thời (concurrency / 동시성) ghi chú (note / 노트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Persistent BST

Nếu cấu trúc (structure / 구조) bất biến sau khi tạo hoặc cần phiên bản (version / 버전) lịch sử, cập nhật có thể **path-copy** chỉ các nút trên đường tìm kiếm và reuse phần còn lại.

Với balanced persistent cây, một cập nhật tạo `O(log n)` các nút mới thay vì bản sao (copy / 복사) cả cây. Đây là chia sẻ cấu trúc — rất quan trọng trong lập trình hàm, versioned dữ liệu (data / 데이터) và persistent trạng thái (state / 상태) các hệ thống.

> **Chuyển mạch:** Ở chặng này của **cây tìm kiếm nhị phân**, **Tính đồng thời (concurrency / 동시성) ghi chú (note / 노트)** tiếp nhận điểm tựa từ **Persistent BST** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đồng thời (concurrency / 동시성) ghi chú (note / 노트)

BST sự thay đổi dữ liệu có thể thay nhiều links và rotations. Concurrent ordered maps vì thế cần synchronization chiến lược (strategy / 전략) phức tạp hơn đơn giản đặt mutex quanh một variable.

Trong hệ thống thực tế, concurrent các cây có thể dùng coarse-grained khóa (lock / 잠금), fine-grained khóa (lock / 잠금), optimistic techniques hoặc completely different structures. DSA bất biến vẫn là nền tảng, nhưng tính đồng thời (concurrency / 동시성) thêm một lớp bất biến về atomicity/visibility.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây tìm kiếm nhị phân**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **Tính đồng thời (concurrency / 동시성) ghi chú (note / 노트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kiểm thử BST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

“BST tìm kiếm (search / 검색) luôn O(log n)” là sai với unbalanced BST.

“cây nhị phân” không đồng nghĩa BST.

“Inorder luôn sorted” chỉ đúng khi bất biến thứ tự thật sự được duy trì.

“Delete nút hai các nút con chỉ cần bản sao (copy / 복사) successor khóa” có thể chưa đủ nếu nút chứa giá trị, siêu dữ liệu hoặc định danh (identity / 식별자) ngữ nghĩa phức tạp; phải chuyển đúng bản ghi (record / 레코드)/các trường theo hợp đồng API.

“ngẫu nhiên BST thường tốt” không thay thế xác định bảo đảm nếu đầu vào có thể đối kháng.

> **Chuyển mạch:** Trong **cây tìm kiếm nhị phân**, **kiểm thử BST** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kiểm thử BST

Ngoài kiểm tra kết quả tìm kiếm, hãy xác minh bất biến sau các chuỗi chèn/xóa ngẫu nhiên:

```text
inorder strictly/non-strictly sorted theo duplicate policy
node count đúng
mọi subtree key nằm trong allowed range
parent pointers đúng nếu có
metadata == recomputation từ children
```

Một bộ xác minh mạnh dùng phạm vi (range / 범위) các ràng buộc:

```text
validate(node, low, high)
```

thay vì chỉ check `left < node < right`, vì violation có thể nằm sâu hơn một tầng.

> **Chuyển mạch:** Ở chặng này của **cây tìm kiếm nhị phân**, **Mô hình tư duy** gom các mảnh từ **kiểm thử BST** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> BST biến **toàn cục thứ tự đã sắp xếp** thành **cục bộ branching quy tắc**. Mỗi phép so sánh không chỉ chọn nút con; nó loại cả một interval các khóa. tìm kiếm (search / 검색) nhanh khi cây chiều cao thấp. cập nhật mạnh vì cấu trúc (structure / 구조) động, nhưng chính sự thay đổi dữ liệu tạo rủi ro shape lệch nên balancing trở thành bước tiến tự nhiên tiếp theo.

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

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
