# Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Augmentation là thêm bất biến (invariant / 불변식) thứ hai** xác định điều kiện hoặc ranh giới mà các cơ chế sau phải tôn trọng; sau đó sang **siêu dữ liệu phải có tính local-composability** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**증강 트리, 순서 통계 트리, 구간 트리**

Một cây tìm kiếm cân bằng đã hỗ trợ tìm kiếm/chèn/xóa theo khóa trong `O(log n)`. **Tăng cường siêu dữ liệu (metadata / 메타데이터)** biến nó thành một họ cấu trúc mạnh hơn bằng cách lưu thêm thông tin tại mỗi nút — đủ nhỏ để cập nhật cục bộ nhưng đủ giàu để trả lời truy vấn mới mà không phải quét toàn cây con.

Idea quan trọng nhất không phải thuộc “thống kê thứ tự cây” hay “Interval cây”, mà là thiết kế (design / 설계) mẫu:

> Nếu một truy vấn trên cây con có thể được tóm tắt bằng một dữ liệu tóm lược nhỏ, và dữ liệu tóm lược của nút cha có thể tính từ cục bộ dữ liệu (data / 데이터) + summaries của các nút con trong `O(1)`, ta thường có thể thêm năng lực (capability / 역량) đó vào balanced BST mà vẫn giữ cập nhật `O(log n)`.

## Augmentation là thêm bất biến (invariant / 불변식) thứ hai

BST bình thường giữ thứ tự (ordering / 순서) bất biến. Augmented BST giữ thêm siêu dữ liệu bất biến.

Ví dụ kích thước cây con:

\[
kích thước (size / 크기)(u)=1+kích thước (size / 크기)(left(u))+kích thước (size / 크기)(right(u))
\]

cây có thể vẫn sorted hoàn hảo nhưng rank truy vấn sai nếu `size` stale. Vì vậy augmented cấu trúc (structure / 구조) là **multi-bất biến cấu trúc (structure / 구조)**.

Một helper hàm kiểu `pull(node)` nên là nguồn of truth:

```java
void pull(Node x) {
    if (x == null) return;
    x.size = 1 + size(x.left) + size(x.right);
}
```

Nếu có nhiều siêu dữ liệu:

```text
size
subtreeSum
maxEnd
minKey
...
```

`pull` recompute tất cả từ các nút con/hiện tại nút.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Augmentation là thêm bất biến (invariant / 불변식) thứ hai** nêu điều cần giải thích; **siêu dữ liệu phải có tính local-composability** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Order-statistics cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## siêu dữ liệu phải có tính local-composability

Augmentation phù hợp nhất khi:

\[
M(u)=F(data(u),M(left),M(right))
\]

với `F` `O(1)`.

Ví dụ:

```text
size = 1 + left.size + right.size
sum = value + left.sum + right.sum
max = max(value, left.max, right.max)
maxEnd = max(interval.end, left.maxEnd, right.maxEnd)
```

Nếu cập nhật siêu dữ liệu cần quét toàn cây con, mỗi cây cập nhật có thể mất `O(n)` và lợi ích của balanced cây biến mất.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **siêu dữ liệu phải có tính local-composability** nêu điều cần giải thích; **Order-statistics cây** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Rank của khóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Order-statistics cây

**thứ tự (order / 순서) thống kê / 순서 통계** là các truy vấn về vị trí trong thứ tự đã sắp xếp: phần tử nhỏ thứ k, rank của khóa, số các khóa nhỏ hơn `x`, percentile, median động.

Mỗi nút lưu `size`.

### phần tử nhỏ thứ k

Giả sử rank bắt đầu từ 1. Tại nút `u`, đặt:

```text
leftSize = size(u.left)
```

Nếu `k == leftSize + 1`, `u` là answer. Nếu `k <= leftSize`, answer nằm left. Nếu lớn hơn, đi right và giảm:

\[
k \leftarrow k-(leftSize+1)
\]

Java:

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

Trên balanced cây, mỗi bước xuống một tầng nên truy vấn `O(log n)`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Rank của khóa** tiếp nhận điểm tựa từ **Order-statistics cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **động median** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rank của khóa

Rank hỏi có bao nhiêu các khóa nhỏ hơn đích, hoặc đích đứng thứ mấy.

Khi đi right từ nút `u`, toàn bộ left cây con và `u` chắc chắn nhỏ hơn đích, nên cộng:

```text
size(left) + 1
```

Nếu cho phép phần tử trùng, ngữ nghĩa phải rõ: hạng đầu tiên, hạng cuối cùng, số phần tử nhỏ hơn hay số phần tử nhỏ hơn hoặc bằng. Chính sách xử lý phần tử trùng ảnh hưởng trực tiếp tới công thức và siêu dữ liệu (metadata / 메타데이터) ở nút.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **động median** tiếp nhận điểm tựa từ **Rank của khóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weighted thứ tự (order / 순서) thống kê** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## động median

Nếu cây hỗ trợ chèn/xóa và truy vấn phần tử thứ k, trung vị của `n` giá trị là hạng khoảng `(n+1)/2` hoặc trung bình của hai hạng giữa tùy định nghĩa.

Balanced order-statistics cây vì thế là một cách làm động median trong `O(log n)` cập nhật/truy vấn. Alternative phổ biến là two-heaps nếu chỉ cần median, nhưng cây hỗ trợ thêm arbitrary rank/các truy vấn khoảng (range queries).

Đây là example cấu trúc dữ liệu selection theo truy vấn set.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Weighted thứ tự (order / 순서) thống kê** tiếp nhận điểm tựa từ **động median** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cây con aggregate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weighted thứ tự (order / 순서) thống kê

siêu dữ liệu không nhất thiết là nút count. Nếu mỗi khóa có tần suất/trọng số `w`, lưu cây con trọng số:

\[
W(u)=w(u)+W(left)+W(right)
\]

Ta có thể tìm weighted percentile bằng cách so sánh đích cumulative trọng số với `leftWeight`.

Trường hợp sử dụng: histogram compressed by distinct giá trị, sampling theo trọng số, tần suất bảng (table / 테이블) ordered.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **cây con aggregate** tiếp nhận điểm tựa từ **Weighted thứ tự (order / 순서) thống kê** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interval cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây con aggregate

Một BST có thứ tự theo khóa có thể lưu tổng, cực tiểu hoặc cực đại của từng cây con để trả lời một số phép tổng hợp theo tiền tố hoặc theo khoảng.

Ví dụ `sumLessThan(x)`:

- nếu `x <= key(u)`, đi left;
- nếu `x > key(u)`, toàn bộ left cây con + nút contribute, rồi đi right.

Với cây con sum siêu dữ liệu, tổng tiền tố truy vấn `O(log n)` trên balanced cây.

Phạm vi (range / 범위) sum `[L,R]` có thể lấy từ hai prefix sums nếu ngữ nghĩa cho phép:

\[
sum(\le R)-sum(<L)
\]

Augmented BST ở đây giống Fenwick/cây đoạn (Segment Tree) về dữ liệu tóm lược, nhưng hỗ trợ động sparse ordered các khóa tự nhiên hơn.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Interval cây** tiếp nhận điểm tựa từ **cây con aggregate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interval tìm kiếm (search / 검색) và pruning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interval cây

Interval cây lưu intervals thường ordered theo tọa độ bắt đầu và augment mỗi nút với:

```text
maxEnd = maximum end trong subtree
```

Hai closed intervals `[a,b]` và `[c,d]` overlap khi:

\[
a\le d \land c\le b
\]

Nếu lĩnh vực (domain / 도메인) dùng half-open `[a,b)`, điều kiện là:

\[
a<d \land c<b
\]

ranh giới ngữ nghĩa phải được định nghĩa trước.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Interval tìm kiếm (search / 검색) và pruning** tiếp nhận điểm tựa từ **Interval cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reporting all overlaps** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interval tìm kiếm (search / 검색) và pruning

Giả sử truy vấn `[L,R]`. Nếu left nút con tồn tại và:

```text
left.maxEnd >= L
```

Cây con trái **có thể** chứa khoảng giao nhau nên cần tiếp tục tìm bên trái. Nếu `left.maxEnd < L`, mọi khoảng trong cây con trái đều kết thúc trước điểm bắt đầu truy vấn, vì vậy có thể cắt tỉa toàn bộ cây con đó.

`maxEnd` không trả answer trực tiếp; nó trả enough thông tin để biết cây con có đáng khám phá hay không.

Đây là augmentation mẫu điển hình.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Reporting all overlaps** tiếp nhận điểm tựa từ **Interval tìm kiếm (search / 검색) và pruning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interval cây vs cây đoạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reporting all overlaps

Tìm một overlapping interval và báo tất cả overlaps là hai problems khác nhau.

Nếu đầu ra có `k` intervals, bất kỳ thuật toán nào cũng cần ít nhất `Ω(k)` để emit các kết quả. Với balanced interval cây, chi phí có thể gần `O(log n + k)` trong favorable thiết kế (design / 설계)/các truy vấn nhưng phụ thuộc chính xác variant.

nhạy theo kích thước đầu ra độ phức tạp (complexity / 복잡도) là mental mô hình quan trọng: không thể kỳ vọng `O(log n)` khi phải trả hàng triệu matches.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Interval cây vs cây đoạn** tiếp nhận điểm tựa từ **Reporting all overlaps** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interval cây vs đường quét** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interval cây vs cây đoạn

Tên dễ gây nhầm.

**Interval cây** thường là BST-like cấu trúc (structure / 구조) lưu động intervals và prune bằng siêu dữ liệu như `maxEnd`.

**cây đoạn** thường tổ chức coordinate lĩnh vực (domain / 도메인)/ranges theo fixed hierarchy và phù hợp phạm vi (range / 범위) aggregates/các cập nhật.

Nếu khóa hoặc khoảng được chèn/xóa động và cần thao tác có thứ tự, Interval cây (tree / 트리) là lựa chọn tự nhiên. Nếu miền tọa độ ổn định hoặc có thể nén và cần tổng hợp mạnh theo khoảng, Segment cây (tree / 트리) có thể phù hợp hơn.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Interval cây vs đường quét** tiếp nhận điểm tựa từ **Interval cây vs cây đoạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rotation và siêu dữ liệu cập nhật thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interval cây vs đường quét

Nếu tất cả khoảng đã biết ngoại tuyến và truy vấn mang tính toàn cục như “số khoảng chồng lấn lớn nhất”, đường quét kết hợp sắp xếp thường đơn giản hơn.

Nếu các truy vấn/các cập nhật trực tuyến, động interval cấu trúc (structure / 구조) có lợi.

tĩnh/ngoại tuyến vs động/trực tuyến là một dimension quan trọng của cấu trúc (structure / 구조) choice.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Interval cây vs đường quét** nêu điều cần giải thích; **Rotation và siêu dữ liệu cập nhật thứ tự (order / 순서)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Red-Black/AVL augmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rotation và siêu dữ liệu cập nhật thứ tự (order / 순서)

Xét right rotation:

```text
        y                  x
       / \                / \
      x   C      ->       A   y
     / \                    / \
    A   B                  B   C
```

Sau rotation, siêu dữ liệu của `y` phải được recompute trước siêu dữ liệu của `x`, vì `x` mới phụ thuộc `y` ở nút con.

Pseudo:

```text
rotateRight(y):
    x = y.left
    B = x.right

    x.right = y
    y.left = B

    pull(y)
    pull(x)
    return x
```

Sai thứ tự có thể giữ BST sorted nhưng làm summaries sai âm thầm.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Rotation và siêu dữ liệu cập nhật thứ tự (order / 순서)** nêu điều cần giải thích; **Red-Black/AVL augmentation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Augmentation theorem intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Red-Black/AVL augmentation

Balanced-tree cách triển khai đã có rotations/recolor/chiều cao maintenance. Augmentation nên gắn vào mọi structural sự thay đổi dữ liệu điểm (point / 지점).

quy tắc tổng quát:

```text
mọi nơi children của node thay đổi -> metadata node có thể stale
mọi rotation -> pull nodes theo bottom-up dependency
mọi insert/delete -> ancestors trên modified path cần update
```

Nếu mã (code / 코드) có quá nhiều places cập nhật siêu dữ liệu thủ công, bug rủi ro (risk / 위험) cao. Centralize sự thay đổi dữ liệu helpers khi có thể.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Augmentation theorem intuition** tiếp nhận điểm tựa từ **Red-Black/AVL augmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multiple augmentations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Augmentation theorem intuition

Một principle kinh điển: nếu attribute của nút có thể tính trong `O(1)` từ nút + các nút con attributes, balanced BST thường có thể maintain attribute mà không đổi asymptotic cập nhật độ phức tạp (complexity / 복잡도).

Lý do là chèn/xóa/xoay chỉ ảnh hưởng `O(log n)` nút trên đường tìm kiếm và tái cân bằng, còn siêu dữ liệu (metadata / 메타데이터) của mỗi nút có thể tính lại trong `O(1)`.

Tổng vẫn:

\[
O(\log n)
\]

Đây là một thiết kế (design / 설계) theorem thực dụng, không chỉ một cấu trúc (structure / 구조) riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Multiple augmentations** tiếp nhận điểm tựa từ **Augmentation theorem intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Augmented treap / skip danh sách (list / 목록)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multiple augmentations

Một nút có thể lưu nhiều summaries cùng lúc:

```text
size
sum
maxEnd
minimumTimestamp
custom aggregate
```

Nếu tất cả `pull` constant-time, asymptotic cập nhật vẫn `O(log n)`, nhưng constants, bộ nhớ/nút và tính cục bộ bộ nhớ đệm tăng.

Đừng augment “cho tiện” mọi possible chỉ số (metric / 지표); siêu dữ liệu nên được biện minh bởi truy vấn khối lượng công việc.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Augmented treap / skip danh sách (list / 목록)** tiếp nhận điểm tựa từ **Multiple augmentations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Indexed skip danh sách (list / 목록) liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Augmented treap / skip danh sách (list / 목록)

Tăng cường siêu dữ liệu (metadata / 메타데이터) không chỉ áp dụng cho AVL hoặc Red-Black cây (tree / 트리). Nút Treap có thể lưu kích thước cây con hoặc tổng; Skip danh sách (list / 목록) có thể thêm độ dài nhảy (**span/width**) ở mỗi con trỏ tiến để hỗ trợ truy vấn hạng và chọn phần tử.

Concept sâu là **hierarchical ordered cấu trúc (structure / 구조) + cục bộ summaries**, không phải loại balancing cụ thể.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, sau nội dung của **Augmented treap / skip danh sách (list / 목록)**, **Indexed skip danh sách (list / 목록) liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Rope và chuỗi (sequence / 시퀀스) các cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Indexed skip danh sách (list / 목록) liên kết (connection / 연결)

Skip danh sách (list / 목록) thông thường tìm khóa với chi phí kỳ vọng `O(log n)`. Nếu mỗi con trỏ tiến lưu số nút tầng 0 mà nó bỏ qua, ta có thể điều hướng theo hạng.

Đây chính là cách tăng cường thống kê thứ tự trên phân cấp của Skip danh sách (list / 목록).

Xem thêm [Skip Lists](./07_skip_lists.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Indexed skip danh sách (list / 목록) liên kết (connection / 연결)** xác định đầu vào; **Rope và chuỗi (sequence / 시퀀스) các cây** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **treap ngầm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rope và chuỗi (sequence / 시퀀스) các cây

Cây cân bằng cũng có thể biểu diễn một dãy thay vì một tập hợp đã sắp xếp. Mỗi nút lưu độ dài hoặc kích thước cây con, nhờ đó hỗ trợ tách, nối và lập chỉ mục theo vị trí.

Cấu trúc Rope lưu văn bản theo các khối cùng trọng số để hỗ trợ lập chỉ mục và chỉnh sửa chuỗi lớn. Treap ngầm dùng kích thước cây con để suy ra “khóa theo vị trí” thay vì lưu khóa tường minh.

Augmentation vì thế mở rộng cây từ dictionary sang động chuỗi (sequence / 시퀀스) cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Rope và chuỗi (sequence / 시퀀스) các cây** xác định đầu vào; **treap ngầm** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Lazy siêu dữ liệu/tagging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## treap ngầm

Trong treap ngầm, vị trí theo thứ tự inorder của nút được suy ra từ kích thước cây con. Tách theo hạng và gộp theo độ ưu tiên ngẫu nhiên cho phép thực hiện các thao tác trên một khoảng của dãy.

Nếu thêm lazy tags như reverse/add, cấu trúc (structure / 구조) bắt đầu gần cây đoạn nhưng trên động chuỗi (sequence / 시퀀스).

Đây là cầu nối (bridge / 브리지) giữa balanced cây, augmentation và lazy propagation.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **treap ngầm** nêu điều cần giải thích; **Lazy siêu dữ liệu/tagging** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phạm vi (range / 범위) cây và multidimensional thinking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lazy siêu dữ liệu/tagging

Một số cây dãy có tăng cường siêu dữ liệu (metadata / 메타데이터) lưu thao tác đang chờ cho cả cây con, tương tự cơ chế lazy của cây đoạn. Ví dụ, một cờ đảo ngược có thể hoán đổi cây con trái/phải khi cờ được đẩy xuống.

Khi có lazy tags, bất biến phức tạp hơn:

```text
stored summary phải phản ánh logical subtree hiện tại
children có thể chưa materialize pending update
trước khi descend cần push tag đúng
```

Đây là advanced phiên bản (version / 버전) của “siêu dữ liệu bất biến”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Lazy siêu dữ liệu/tagging** nêu điều cần giải thích; **Phạm vi (range / 범위) cây và multidimensional thinking** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hình học (geometry / 기하학) use cases** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phạm vi (range / 범위) cây và multidimensional thinking

Nếu cần truy vấn nhiều chiều, có thể tăng cường mỗi nút bằng một cấu trúc phụ. Ví dụ, một cây truy vấn khoảng 2D có thể sắp theo `x`, còn mỗi nút lưu một cấu trúc đã sắp theo `y` cho cây con của nó.

truy vấn nhanh hơn nhưng bộ nhớ/xây dựng độ phức tạp (complexity / 복잡도) tăng lớn.

Lesson: augmentation có thể recursive, nhưng mỗi extra dimension thường trả chi phí đáng kể.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Phạm vi (range / 범위) cây và multidimensional thinking** cho ta quy tắc; **Hình học (geometry / 기하학) use cases** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **cơ sở dữ liệu liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hình học (geometry / 기하학) use cases

Interval/augmented các cây xuất hiện trong:

```text
calendar conflict detection
memory-region overlap
compiler live ranges
collision broad phase
genomic interval queries
reservation windows
network address ranges
```

chính xác cấu trúc (structure / 구조) phụ thuộc cập nhật tần suất, dimensionality, kích thước đầu ra và coordinate mô hình.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Hình học (geometry / 기하학) use cases** cho ta quy tắc; **cơ sở dữ liệu liên kết (connection / 연결)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **OS bộ cấp phát liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cơ sở dữ liệu liên kết (connection / 연결)

Chỉ mục có thứ tự trong cơ sở dữ liệu có thể giữ thống kê hoặc dữ liệu tóm lược ở trang hay cấu trúc phụ. siêu dữ liệu (metadata / 메타데이터) kiểu thống kê thứ tự có thể hỗ trợ đếm, truy vấn hạng hoặc chọn phần tử trong các chỉ mục chuyên biệt.

Chỉ mục không gian như R-tree dùng các hình chữ nhật bao thay vì thứ tự khóa BST, nhưng ý tưởng cắt tỉa bằng dữ liệu tóm lược của cây con tương tự: thông tin tóm lược cho biết một nhánh có khả năng giao với truy vấn hay không.

Augmentation là một mẫu rộng của lập chỉ mục.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **cơ sở dữ liệu liên kết (connection / 연결)** nêu điều cần giải thích; **OS bộ cấp phát liên kết (connection / 연결)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Maintaining counts with các phần tử trùng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OS bộ cấp phát liên kết (connection / 연결)

Bộ cấp phát bộ nhớ có thể dùng cây cân bằng được lập khóa theo kích thước hoặc địa chỉ, đồng thời tăng cường siêu dữ liệu (metadata / 메타데이터) để tìm khối phù hợp hoặc theo dõi khối trống lớn nhất trong cây con.

truy vấn “cây con này có khối (block / 블록) đủ lớn không?” chính là summary-guided pruning.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Maintaining counts with các phần tử trùng** tiếp nhận điểm tựa từ **OS bộ cấp phát liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deletion là nơi siêu dữ liệu bugs dễ xuất hiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Maintaining counts with các phần tử trùng

Nếu many equal các khóa, một nút có thể lưu `count` thay vì tạo nút riêng mỗi phần tử trùng.

Then:

\[
kích thước (size / 크기)(u)=count(u)+kích thước (size / 크기)(left)+kích thước (size / 크기)(right)
\]

Các công thức tìm phần tử thứ k hoặc hạng phải sử dụng phạm vi `count` khi một khóa có thể xuất hiện nhiều lần, thay vì giả định mỗi khóa chỉ đóng góp đúng một vị trí.

phần tử trùng chính sách là part of sự trừu tượng (abstraction), không phải cách triển khai afterthought.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Maintaining counts with các phần tử trùng** nêu điều cần giải thích; **Deletion là nơi siêu dữ liệu bugs dễ xuất hiện** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Persistence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deletion là nơi siêu dữ liệu bugs dễ xuất hiện

Chèn thường đi theo một đường rồi gắn nút lá mới. Xóa có thể đổi/sao chép giá trị của phần tử kế tiếp, loại bỏ một nút khác và tái cân bằng qua nhiều tầng.

Nếu siêu dữ liệu gắn với key-specific cục bộ dữ liệu (data / 데이터), việc bản sao (copy / 복사) khóa/giá trị mà quên bản sao (copy / 복사)/recompute associated cục bộ các trường có thể sai.

Một chiến lược (strategy / 전략) an toàn là structural deletion rõ ràng + bottom-up `pull` theo actual changed các nút, không patch siêu dữ liệu ad hoc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Deletion là nơi siêu dữ liệu bugs dễ xuất hiện** nêu điều cần giải thích; **Persistence** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Persistence

Path-copying persistent BST tạo new các nút trên root-to-update đường đi và reuse unchanged các cây con. Augmented siêu dữ liệu rất phù hợp vì mỗi copied nút recompute dữ liệu tóm lược từ các nút con.

Mỗi phiên bản (version / 버전) nút gốc có riêng lô-gic (logic / 논리) trạng thái (state / 상태); cây con sharing tiết kiệm bộ nhớ. cập nhật `O(log n)` new các nút trên balanced cây.

Trường hợp sử dụng: các chỉ mục có phiên bản, undo, time-travel các truy vấn và functional các cấu trúc dữ liệu.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Tính đồng thời (concurrency / 동시성)** tiếp nhận điểm tựa từ **Persistence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **xác minh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đồng thời (concurrency / 동시성)

Augmentation làm concurrent cập nhật khó hơn vì một khóa sự thay đổi dữ liệu có thể require siêu dữ liệu changes trên tổ tiên đường đi. khóa (lock / 잠금) granularity, rotations và reader consistency phải được thiết kế cùng nhau.

Một reader nhìn cây giữa structural cập nhật và siêu dữ liệu cập nhật có thể thấy thứ tự đã sắp xếp hợp lệ nhưng dữ liệu tóm lược inconsistent.

Concurrent augmented cây cần atomicity giao thức (protocol / 프로토콜) rõ, không chỉ khóa (lock / 잠금) nút vừa insert.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **xác minh** tiếp nhận điểm tựa từ **Tính đồng thời (concurrency / 동시성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differential kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## xác minh

`validate(node)` nên recompute kỳ vọng siêu dữ liệu recursively và so sánh stored các giá trị.

Ví dụ:

```java
int validateSize(Node u) {
    if (u == null) return 0;

    int left = validateSize(u.left);
    int right = validateSize(u.right);
    int expected = 1 + left + right;

    if (u.size != expected) throw new AssertionError();
    return expected;
}
```

Interval cây bộ xác minh tương tự recompute `maxEnd`.

Trong kiểm thử gỡ lỗi, việc chạy bộ xác minh bất biến sau các chuỗi chèn, xóa và xoay ngẫu nhiên rất hiệu quả.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Differential kiểm thử** tiếp nhận điểm tựa từ **xác minh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phổ biến các dạng lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differential kiểm thử

Có thể kiểm thử cây thống kê thứ tự bằng cách đối chiếu với một `ArrayList` nhỏ đã sắp xếp:

```text
random insert/delete
sort reference list
compare kth/rank/count
```

Interval các truy vấn có thể so sánh với brute-force quét all intervals.

Property-based/ngẫu nhiên kiểm thử đặc biệt hữu ích vì siêu dữ liệu bugs thường chỉ xuất hiện sau sự thay đổi dữ liệu chuỗi (sequence / 시퀀스) dài.

> **Chuyển mạch:** Trong **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Phổ biến các dạng lỗi** tiếp nhận điểm tựa từ **Differential kiểm thử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Choosing augmentation vs separate cấu trúc (structure / 구조)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phổ biến các dạng lỗi

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- BST ordering đúng nhưng siêu dữ liệu stale;
- cập nhật siêu dữ liệu sai thứ tự sau rotation;
- phần tử trùng chính sách không nhất quán với `size`;
- interval ranh giới closed/half-open không rõ;
- `maxEnd` dùng wrong giá trị canh gác (sentinel) cho null;
- tràn số nguyên (integer overflow) trong cây con sum/count;
- lazy tag không push trước khi descend;
- bản sao (copy / 복사) successor khóa nhưng quên cục bộ siêu dữ liệu;
- assume output-heavy truy vấn vẫn `O(log n)` dù phải emit `k` các kết quả.

> **Chuyển mạch:** Ở chặng này của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Choosing augmentation vs separate cấu trúc (structure / 구조)** tiếp nhận điểm tựa từ **Phổ biến các dạng lỗi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Choosing augmentation vs separate cấu trúc (structure / 구조)

Không phải truy vấn nào cũng nên nhét vào một cây.

Nếu cần khóa có thứ tự cập nhật động cùng truy vấn hạng và tổng theo khoảng, cây tăng cường là hợp lý. Nếu miền tọa độ dày đặc và chỉ cần tổng tiền tố, Fenwick cây (tree / 트리) đơn giản hơn. Nếu cần cập nhật mạnh theo khoảng, Segment cây (tree / 트리) tự nhiên hơn. Nếu tra cứu chính xác theo khóa chiếm ưu thế, đôi khi bảng băm kết hợp một cấu trúc có thứ tự riêng sẽ tốt hơn.

Augmentation trả chi phí bằng nút kích thước (size / 크기), cách triển khai độ phức tạp (complexity / 복잡도) và sự thay đổi dữ liệu burden. Chỉ thêm dữ liệu tóm lược khi truy vấn benefit thực sự đáng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Augmented các cây, thứ tự (order / 순서) thống kê và Interval các cây**, **Mô hình tư duy** gom các mảnh từ **Choosing augmentation vs separate cấu trúc (structure / 구조)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Augmentation là biến mỗi cây con thành một “mô-đun (module / 모듈) có dữ liệu tóm lược”. khóa thứ tự (order / 순서) cho biết đi trái hay phải; siêu dữ liệu cho biết cây con đóng góp bao nhiêu hoặc có thể bỏ qua hoàn toàn không. Nếu dữ liệu tóm lược của nút cha tính được cục bộ từ các nút con, ta có thể thêm truy vấn power mà không phá logarithmic cập nhật của balanced cây.

Khi muốn thêm truy vấn mới vào cây, hãy hỏi: **dữ liệu tóm lược nhỏ nhất nào đủ để quyết định truy vấn mà không nhìn mọi nút? dữ liệu tóm lược đó có kết hợp từ các nút con trong `O(1)` không? Và mọi structural sự thay đổi dữ liệu có một nơi rõ ràng để recompute nó không?**

Xem tiếp: [BST](./01_binary_search_trees.md), [Balanced Search Trees](./02_balanced_search_trees.md), [Skip Lists](./07_skip_lists.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md) và [Intervals & Sweep Line](../04_algorithmic_paradigms/08_intervals_and_sweep_line.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
