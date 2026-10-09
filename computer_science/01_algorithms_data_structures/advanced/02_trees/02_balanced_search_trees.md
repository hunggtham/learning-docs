# Cây tìm kiếm cân bằng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Cây tìm kiếm cân bằng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Hai lớp bất biến khác nhau** xác định điều kiện hoặc ranh giới mà các cơ chế sau phải tôn trọng; sau đó sang **2. Rotation bảo toàn thứ tự thế nào?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối balanced search trees với rotations, height và ordered operations, để giữ tìm kiếm nhanh sau cập nhật.

**Balanced tìm kiếm (search / 검색) Trees / 균형 탐색 트리**

Cây tìm kiếm nhị phân chỉ thật sự hữu ích khi chiều cao được kiểm soát. Với cùng một tập khóa, một BST có thể thấp gần `log n`, nhưng cũng có thể suy thoái thành chuỗi dài gần `n` nếu thứ tự chèn xấu.

Mọi thao tác cơ bản thực chất có chi phí theo chiều cao:

\[
tìm kiếm (search / 검색), insert, delete = O(h)
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

> **Mối nối:** Cân bằng chiều cao chỉ có giá trị khi rotation vẫn giữ thứ tự khóa. Sau khi chứng minh điều đó, phần kế tiếp theo dõi metadata phải cập nhật thế nào để cả hai bất biến cùng tồn tại.

## 2. Rotation bảo toàn thứ tự thế nào?

Right rotation:

```text
        y                     x
       / \                   / \
      x   C      --->        A   y
     / \                       / \
    A   B                     B   C
```

Trước và sau rotation, inorder chuỗi (sequence / 시퀀스) đều là:

```text
A < x < B < y < C
```

Rotation chỉ đổi quan hệ cha–con cục bộ. Chính vì inorder thứ tự (order / 순서) không đổi nên BST bất biến (invariant / 불변식) được giữ.

Nếu nút (node / 노드) có siêu dữ liệu (metadata / 메타데이터) như `height`, `size`, `maxEnd`, `sum`, siêu dữ liệu (metadata / 메타데이터) phải được cập nhật đúng thứ tự sau rotation.

> **Mối nối:** Rotation đã giữ được thứ tự, nhưng height, color hoặc size không tự cập nhật theo nó. AVL là ví dụ đầu tiên cho thấy metadata địa phương có thể tạo ra bảo đảm chiều cao toàn cục.

## 3. siêu dữ liệu (metadata / 메타데이터) cập nhật (update / 업데이트) thứ tự (order / 순서)

Sau right rotation ở `y`:

```text
y trở thành con của x
```

Nên recompute `y` trước, rồi `x`, vì siêu dữ liệu (metadata / 메타데이터) mới của `x` phụ thuộc siêu dữ liệu (metadata / 메타데이터) mới của `y`.

Mẫu (pattern / 패턴) tổng quát:

> Khi relink cây (tree / 트리), cập nhật siêu dữ liệu (metadata / 메타데이터) từ dưới lên theo topology mới.

Sai thứ tự có thể tạo cây đúng về BST nhưng sai về augmentation.

> **Mối nối:** AVL đặt quy tắc cập nhật balance factor vào một cấu trúc cụ thể. Để đánh giá quy tắc ấy, ta cần chứng minh vì sao giới hạn chênh lệch chiều cao dẫn đến chiều cao logarithmic.

## 4. AVL cây (tree / 트리)

AVL giữ balance factor:

\[
BF(u)=height(left(u))-height(right(u))
\]

và yêu cầu:

\[
BF(u)\in\{-1,0,1\}
\]

ở mọi nút (node / 노드).

Đây là một bất biến (invariant / 불변식) cân bằng khá chặt.

> **Mối nối:** Cận logarithmic của AVL đến từ truy hồi về cây nhỏ nhất ở mỗi chiều cao. Khi cập nhật làm mất cân bằng, bốn tên trường hợp thực ra quy về hai hình dạng lệch và phép sửa tương ứng.

## 5. Vì sao AVL có chiều cao logarithmic?

Gọi `N(h)` là số nút (node / 노드) ít nhất của AVL height `h`.

Để đạt height `h` với ít nút (node / 노드) nhất nhưng vẫn hợp lệ, hai subtree phải có height `h-1` và `h-2`:

\[
N(h)=1+N(h-1)+N(h-2)
\]

Recurrence này tăng cùng cấp với Fibonacci, tức tăng theo hàm mũ của `h`.

Do đó đảo lại:

\[
h=O(\log n)
\]

Đây là bản chất của bảo đảm chiều cao AVL.

> **Mối nối:** Phân loại hình dạng cho biết rotation nào khôi phục balance mà vẫn giữ thứ tự. AVL Insert là nơi áp dụng trực tiếp quyết định đó trên đường từ nút mới về gốc.

## 6. Bốn trường hợp (case / 사례) AVL thực chất là hai hình dạng

Sau insert, một nút (node / 노드) có thể lệch trái hoặc lệch phải.

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

Không nên học bốn trường hợp (case / 사례) như bốn mẹo. Hãy nhìn hình dạng:

> zig-zag cần biến thành straight line trước, sau đó một rotation chính sửa được imbalance.

> **Mối nối:** Insert chỉ làm tăng chiều cao trên một đường đi nên có thể sửa từ dưới lên theo các trường hợp đã biết. Delete có thể làm giảm chiều cao ở nhiều tổ tiên liên tiếp, vì vậy cần một phân tích riêng.

## 7. AVL Insert

Quy trình:

1. insert như BST;
2. đi ngược đường dẫn (path / 경로);
3. recompute height;
4. tính balance factor;
5. rotate nếu vi phạm;
6. tiếp tục cập nhật siêu dữ liệu (metadata / 메타데이터) cần thiết.

Insertion chỉ ảnh hưởng các tổ tiên của vị trí chèn.

> **Mối nối:** AVL Delete cho thấy bảo đảm chặt về chiều cao kéo theo nhiều cập nhật sau một lần xóa. Red-Black tree chọn bất biến khác để thường giảm số lần sửa, đổi một phần độ chặt lấy thao tác thực tế đơn giản hơn.

## 8. AVL Delete khó hơn Insert

Delete có thể làm height subtree giảm. Sau khi sửa một imbalance, height của subtree mới vẫn có thể thấp hơn trước, tiếp tục làm ancestor cao hơn mất cân bằng.

Vì vậy delete thường phải tiếp tục kiểm tra tới gốc (root / 루트).

Đây là khác biệt quan trọng giữa:

```text
insert -> height có thể tăng
remove -> height có thể giảm dây chuyền
```

> **Mối nối:** Red-Black mã hóa trạng thái cân bằng bằng màu trên nút và lá giả. Để tin vào cấu trúc này, ta cần thấy các bất biến màu giới hạn số nút trên mọi đường gốc–lá.

## 9. Red-Black cây (tree / 트리)

Red-Black cây (tree / 트리) không theo dõi chênh lệch height trực tiếp. Nó dùng màu để encode một ràng buộc cân bằng mềm hơn.

Các bất biến (invariant / 불변식) phổ biến:

1. mỗi nút (node / 노드) đỏ hoặc đen;
2. gốc (root / 루트) đen;
3. null leaf được xem là đen;
4. nút (node / 노드) đỏ không có child đỏ;
5. mọi đường dẫn (path / 경로) từ một nút (node / 노드) tới null leaf có cùng số nút (node / 노드) đen.

Số nút (node / 노드) đen trên đường dẫn (path / 경로) được gọi là **black height**.

> **Mối nối:** Bất biến Red-Black giới hạn chiều cao bằng cách ràng buộc black-height, dù không cân bằng chặt như AVL. Insert tiếp theo sửa vi phạm màu bằng các trường hợp cục bộ và rotation.

## 10. Vì sao Red-Black cũng logarithmic?

Vì không có hai nút (node / 노드) đỏ liên tiếp, trên một root-to-leaf đường dẫn (path / 경로) số nút (node / 노드) đỏ không vượt số nút (node / 노드) đen đáng kể.

Mọi đường dẫn (path / 경로) có cùng black height, nên đường dẫn (path / 경로) dài nhất không quá khoảng hai lần đường dẫn (path / 경로) ngắn nhất theo số mức (level / 수준) liên quan.

Từ đó suy ra:

\[
h=O(\log n)
\]

Red-Black cho phép hình dạng “lỏng” hơn AVL nhưng vẫn đủ giữ logarithmic bound.

> **Mối nối:** Insert tạo vi phạm chủ yếu khi hai nút đỏ đứng cạnh nhau, nên các trường hợp sửa có thể truyền lên theo màu của cha và chú. Delete khó hơn vì nó có thể làm mất một đơn vị black-height.

## 11. Red-Black Insert

Nút (node / 노드) mới thường được tô đỏ để không làm tăng black height ngay lập tức.

Vấn đề chỉ xuất hiện nếu parent cũng đỏ.

Hai hướng repair chính:

### Uncle đỏ

Recolor parent và uncle thành đen, grandparent thành đỏ, rồi tiếp tục kiểm tra grandparent.

### Uncle đen/null

Dùng rotation + recolor để loại red-red violation tại chỗ.

Mô hình tư duy:

> insertion repair bảo vệ đồng thời “không red-red” và “black height không đổi không hợp lệ”.

> **Mối nối:** Red-Black Delete phải xử lý trạng thái “thiếu đen” và khôi phục cân bằng qua anh em, nên nhiều nhánh hơn Insert. Hai cấu trúc lúc này có đủ khác biệt để so sánh theo workload thay vì chỉ theo cận Big-O.

## 12. Red-Black Delete

Xóa nút (node / 노드) đen có thể làm một nhánh thiếu một đơn vị black height.

Nhiều tài liệu dùng khái niệm **double black** để mô hình hóa thiếu hụt này.

Các trường hợp (case / 사례) sibling đỏ/đen và child đỏ/đen thực chất là những cách:

```text
chuyển thiếu hụt black lên trên
hoặc
phân phối lại black bằng rotation/recolor
```

Nếu chỉ học trường hợp (case / 사례) mà không hiểu black-height deficit, hiện thực (implementation / 구현) rất khó nhớ và gỡ lỗi (debug / 디버그).

> **Mối nối:** AVL thường giữ chiều cao chặt hơn, còn Red-Black thường giảm chi phí sửa; lựa chọn phụ thuộc tỷ lệ đọc, ghi và locality. Treap đưa ra một hướng khác: dùng priority ngẫu nhiên để đạt cân bằng kỳ vọng.

## 13. AVL vs Red-Black

AVL cân bằng chặt hơn nên thường có chiều cao thấp hơn một chút. Red-Black cho phép nhiều shape hơn, thường cần ít rotation hơn trong update-heavy tải công việc (workload / 워크로드).

Một cách định hướng:

```text
lookup-heavy / latency lookup quan trọng   -> AVL có thể hấp dẫn
ordered map/set tổng quát                  -> Red-Black rất phổ biến
external-memory                            -> B/B+Tree phù hợp hơn
concurrent ordered structure               -> có thể cân nhắc Skip List hoặc tree chuyên dụng
```

Không nên coi đây là luật tuyệt đối. bộ nhớ đệm (cache / 캐시) locality, allocator, comparator chi phí (cost / 비용) và hiện thực (implementation / 구현) chất lượng (quality / 품질) đều ảnh hưởng thực tế.

> **Mối nối:** Treap giữ thứ tự theo key và heap theo priority, nhờ vậy không cần lưu balance factor hay màu. Hai bất biến này cũng cho phép xây thao tác split và merge như những phép toán cơ bản.

## 14. Treap: Balance bằng Random Priority

Treap giữ:

```text
BST order theo key
heap order theo random priority
```

Nếu priorities độc lập ngẫu nhiên, expected height là `O(log n)`.

Treap cho thấy balance không nhất thiết đến từ deterministic siêu dữ liệu (metadata / 메타데이터) như height hoặc color. Randomness cũng có thể tạo expected balance.

> **Mối nối:** Split cắt theo key, merge ghép hai cây có miền khóa tách biệt; cả hai đều tái lập heap priority bằng đệ quy. Nếu thay key bằng vị trí inorder, cùng cơ chế đó trở thành implicit treap cho mảng động.

## 15. Split và Merge trong Treap

Treap đặc biệt mạnh vì `split` và `merge` rất tự nhiên.

`split(root,key)` chia thành:

```text
L: keys < key
R: keys >= key
```

`merge(L,R)` yêu cầu mọi key của `L` nhỏ hơn mọi key của `R`, rồi dùng vùng nhớ động (heap / 힙) priority để chọn gốc (root / 루트).

Nhiều chuỗi (sequence / 시퀀스)/data-structure operations có thể xây từ split/merge thay vì viết insert/delete riêng.

> **Mối nối:** Implicit Treap dùng subtree size để định vị phần tử theo vị trí và lazy tag để cập nhật đoạn. Splay tree cũng thích nghi theo truy cập, nhưng dựa vào việc đưa nút vừa dùng lên gốc thay vì priority ngẫu nhiên.

## 16. Implicit Treap

Nếu không lưu key tường minh (explicit / 명시적) mà coi inorder position là chỉ mục (index / 인덱스) lô-gic (logic / 논리), subtree kích thước (size / 크기) cho phép tìm phần tử thứ `k`.

Khi đó Treap có thể biểu diễn chuỗi (sequence / 시퀀스) động với:

```text
split theo position
merge sequences
insert/delete interval
reverse interval bằng lazy flag
range aggregate nếu augment
```

Đây là cầu nối giữa balanced cây (tree / 트리) và động (dynamic / 동적) array/rope.

> **Mối nối:** Splay không giữ bất biến cân bằng cứng; bảo đảm amortized xuất hiện từ chuỗi truy cập và các rotation zig-zig/zig-zag. Weight-balanced tree quay lại một tiêu chí tường minh hơn: tỷ lệ kích thước các cây con.

## 17. Splay cây (tree / 트리)

Splay cây (tree / 트리) không giữ balance bất biến (invariant / 불변식) cứng. Sau truy cập (access / 접근), nút (node / 노드) được đưa lên gốc (root / 루트) bằng zig, zig-zig, zig-zag rotations.

Một thao tác có thể `O(n)`, nhưng amortized `O(log n)`.

Điểm thú vị là cấu trúc (structure / 구조) tự thích nghi: item được truy cập gần đây hoặc thường xuyên có xu hướng gần gốc (root / 루트).

Splay cây (tree / 트리) minh họa sự đánh đổi (trade-off / 트레이드오프) giữa worst-case per thao tác (operation / 연산) và adaptive locality.

> **Mối nối:** Weight-balanced tree dùng size để kiểm soát chiều cao thay vì height hoặc color. Scapegoat tree đẩy ý tưởng này xa hơn: chỉ rebuild khi một đường đi cho thấy bất biến kích thước đã lệch quá xa.

## 18. Weight-Balanced cây (tree / 트리)

Có thể cân bằng dựa trên subtree kích thước (size / 크기) thay vì height/color.

Ví dụ yêu cầu hai subtree không quá lệch theo tỷ lệ. Khi vi phạm, rotate/rebuild.

Ý tưởng quan trọng:

> “Balanced” không chỉ có một định nghĩa; miễn bất biến (invariant / 불변식) đủ mạnh để bound height hoặc expected chi phí (cost / 비용).

> **Mối nối:** Scapegoat trả chi phí rebuild theo đợt để tránh metadata cân bằng ở mọi nút. Trong bộ nhớ ngoài, mô hình chi phí lại bị chi phối bởi page I/O, nên B-Tree cần nhiều khóa trong một nút.

## 19. Scapegoat cây (tree / 트리)

Scapegoat cây (tree / 트리) tránh lưu balance siêu dữ liệu (metadata / 메타데이터) ở mọi nút (node / 노드). Khi insertion làm cây (tree / 트리) quá cao, tìm một ancestor “scapegoat” có subtree mất cân bằng rồi rebuild toàn subtree đó thành cây cân bằng.

Một cập nhật (update / 업데이트) riêng có thể đắt, nhưng amortized bound tốt.

Đây là ví dụ khác của deamortized-vs-amortized thiết kế (design / 설계) không gian (space / 공간).

> **Mối nối:** B-Tree giảm số lần đọc trang bằng cách tăng hệ số phân nhánh và giữ các nút trong giới hạn lấp đầy. Cấu trúc này vẫn cung cấp ordered map, với các năng lực vượt quá tra cứu khóa đơn thuần.

## 20. B-Tree là Balanced tìm kiếm (search / 검색) cây (tree / 트리) cho Page I/O

B-Tree/B+cây (tree / 트리) cũng cân bằng, nhưng nút (node / 노드) có nhiều child.

Mục tiêu không chỉ giảm số comparison mà giảm số page truy cập (access / 접근).

Balanced nhị phân (binary / 이진) cây (tree / 트리) height `O(log_2 n)`; B-Tree với fanout `B` có height gần:

\[
O(\log_B n)
\]

Balanced-tree thiết kế (design / 설계) phải khớp chi phí (cost / 비용) mô hình (model / 모델) của lưu trữ (storage / 저장소) medium.

> **Mối nối:** Ordered map không chỉ tìm một khóa; nó còn cung cấp min/max, predecessor, range và thứ tự duyệt. Khi nhiều bản ghi có cùng khóa, từng năng lực ấy phụ thuộc vào chính sách duplicate rõ ràng.

## 21. Ordered Map năng lực (capability / 역량)

Balanced BST hỗ trợ tự nhiên:

```text
minimum / maximum
floor / ceiling
predecessor / successor
lower_bound / upper_bound
range iteration
```

Bảng băm (hash table / 해시 테이블) không giữ toàn cục (global / 전역) thứ tự (order / 순서) nên không hỗ trợ các truy vấn (query / 쿼리) này tự nhiên.

Đây là khác biệt năng lực (capability / 역량), không chỉ độ phức tạp (complexity / 복잡도).

> **Mối nối:** Duplicate có thể được lưu thành nhiều nút, gom vào bucket, hoặc tách bằng một tie-breaker; mỗi lựa chọn thay đổi iterator và delete. Comparator phải mô tả chính sách ấy thành một hợp đồng nhất quán.

## 22. Duplicate Keys

Phải xác định chính sách (policy / 정책):

```text
reject duplicate
count frequency trong node
lưu multiset entries
augment bằng tie-break unique id
```

Nếu comparator trả `0`, ordered map thường xem hai key là cùng thứ tự (ordering / 순서) position.

Comparator ngữ nghĩa (semantics / 의미론) là một phần của định danh (identity / 식별자) trong cây (tree / 트리).

> **Mối nối:** Comparator không chỉ quyết định thứ tự hiển thị; nó quyết định đường đi và định danh logic của phần tử. Khi hợp đồng này ổn định, mỗi nút có thể mang summary để mở rộng năng lực của cây.

## 23. Comparator đặc tả hợp đồng (contract / 계약)

Comparator cần ít nhất tính nhất quán và bắc cầu.

Nếu:

```text
a < b
b < c
nhưng c < a
```

Tìm kiếm (search / 검색) đường dẫn (path / 경로) không còn có nghĩa toán học.

Một rotation hoàn hảo cũng không cứu được cây (tree / 트리) có comparator không tạo thứ tự (ordering / 순서) hợp lệ.

> **Mối nối:** Augmentation lưu một hàm tổng hợp của cây con và phải được tính lại sau insert, delete hoặc rotation. Subtree size là trường hợp nền tảng, từ đó order statistics trả lời rank và phần tử thứ k.

## 24. Augmentation

Balanced cây (tree / 트리) là khung phần mềm (framework / 프레임워크) rất mạnh khi mỗi nút (node / 노드) lưu summary từ subtree.

Ví dụ:

```text
size
sum
maxEnd
min/max
custom aggregate
```

Nếu summary được tính từ child trong `O(1)`, rotation chỉ cần recompute vài nút (node / 노드) cục bộ nên asymptotic cập nhật (update / 업데이트) thường vẫn `O(log n)`.

> **Mối nối:** Với subtree size, mỗi bước đi có thể bỏ qua toàn bộ một cây con để tìm rank hoặc phần tử thứ k. Interval tree dùng cùng nguyên tắc summary, nhưng lưu `maxEnd` để loại bỏ những nhánh không thể giao.

## 25. thứ tự (order / 순서) Statistics

Lưu:

\[
kích thước (size / 크기)(u)=1+kích thước (size / 크기)(left)+kích thước (size / 크기)(right)
\]

cho phép:

```text
select(k) -> phần tử nhỏ thứ k
rank(x)   -> số key nhỏ hơn x
```

mỗi truy vấn (query / 쿼리) `O(log n)` trên balanced cây (tree / 트리).

Đây là ví dụ augmentation biến ordered set thành order-statistic cây (tree / 트리).

> **Mối nối:** Interval tree phải bảo trì đồng thời bất biến cân bằng và summary `maxEnd`; một rotation đúng hình dạng nhưng sai summary vẫn cho kết quả sai. Persistent balanced tree giải quyết một chiều khác: giữ lại các summary của phiên bản cũ bằng chia sẻ cấu trúc.

## 26. Interval cây (tree / 트리)

Nếu nút (node / 노드) keyed theo interval start và lưu `maxEnd` của subtree, có thể prune subtree không thể giao truy vấn (query / 쿼리) interval.

Balanced bất biến (invariant / 불변식) giữ height; augmentation giữ summary phục vụ overlap truy vấn (query / 쿼리).

Hai lớp bất biến hoạt động độc lập nhưng phải cùng được bảo trì sau rotation.

> **Mối nối:** Persistent update chỉ sao chép đường đi nên các phiên bản dùng chung những cây con bất biến; mọi metadata trên đường đó cũng phải được tính lại. Iterator trong cấu trúc mutable lại cần parent pointer và quy tắc invalidation rõ ràng.

## 27. Persistent Balanced cây (tree / 트리)

Với immutable/persistent cây (tree / 트리), cập nhật (update / 업데이트) chỉ sao chép các nút (node / 노드) trên tìm kiếm (search / 검색) đường dẫn (path / 경로) và chia sẻ subtree không đổi.

Nếu cây (tree / 트리) height `O(log n)`, một cập nhật (update / 업데이트) tạo `O(log n)` nút (node / 노드) mới.

Persistent Red-Black/AVL/Treap có thể hỗ trợ snapshot/versioning hiệu quả.

> **Mối nối:** Parent pointer làm ordered iterator tiện hơn nhưng tăng số liên kết phải cập nhật sau rotation. Khi số nút lớn, chi phí pointer chasing và layout bộ nhớ có thể quan trọng không kém số phép so sánh.

## 28. Parent Pointer và Iterator

Nếu cần iterator predecessor/successor nhanh, parent pointer có thể hữu ích.

Nhưng mỗi rotation phải cập nhật parent pointer đúng.

Nếu iterator giữ raw nút (node / 노드) tham chiếu (reference / 참조), delete/rotation/vô hiệu hóa (invalidation / 무효화) ngữ nghĩa (semantics / 의미론) phải được định nghĩa rõ.

> **Mối nối:** Node-based tree thường trả giá bằng cache locality để đổi lấy cập nhật linh hoạt; mảng hoặc layout phẳng có thể đảo ngược đánh đổi đó. Khi nhiều luồng cùng chạm các node và rotation, bài toán concurrent balanced tree trở nên khó hơn nữa.

## 29. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃)

Node-based trees có pointer chasing và đối tượng (object / 객체) overhead.

Với dữ liệu nhỏ/tĩnh, sorted array có thể nhanh hơn cây (tree / 트리) dù insert/delete tệ hơn, vì:

```text
contiguous memory
fewer allocations
better cache locality
```

Balanced cây (tree / 트리) đáng giá khi mutation/thứ tự (order / 순서) queries thực sự cần.

> **Mối nối:** Rotation thay đổi nhiều liên kết cùng lúc, nên khóa tinh vi dễ gây deadlock và lock-free tree cần memory reclamation chặt chẽ. Optimistic read giảm contention bằng cách đọc trước rồi xác thực rằng cấu trúc chưa đổi.

## 30. Concurrent Balanced Trees

Concurrent cây (tree / 트리) khó hơn băm (hash / 해시) Map hoặc Skip danh sách (list / 목록) vì rotation thay đổi nhiều pointer liên quan.

Fine-grained locking phải xác định khóa (lock / 잠금) thứ tự (order / 순서) để tránh deadlock. Lock-free cây (tree / 트리) cần linearization, bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) và reclamation rất phức tạp.

Đây là lý do concurrent ordered maps đôi khi dùng Skip danh sách (list / 목록): expected `O(log n)` nhưng cập nhật (update / 업데이트) topology cục bộ theo mức (level / 수준) có thể thuận lợi hơn.

> **Mối nối:** Optimistic read chấp nhận retry để đổi lấy đường đọc không khóa, miễn việc kiểm tra phiên bản đủ mạnh. Nếu dữ liệu đã có sẵn theo thứ tự, bulk build lại đổi hướng tối ưu: xây toàn cây một lần thay vì cập nhật từng nút.

## 31. Optimistic Read

Một số hiện thực (implementation / 구현) cho reader đọc mà không khóa toàn cây (tree / 트리), rồi validate phiên bản (version / 버전)/stamp để phát hiện writer đã thay đổi cấu trúc.

Mẫu này đánh đổi thử lại (retry / 재시도) để giảm contention read-heavy.

Cấu trúc dữ liệu (data structure / 자료구조) tính đồng thời (concurrency / 동시성) không chỉ chọn khóa (lock / 잠금) hay no-lock; có cả optimistic kiểm tra hợp lệ (validation / 검증) và sao chép khi ghi (copy-on-write / 쓰기 시 복사).

> **Mối nối:** Từ sorted keys, chọn phần tử giữa làm gốc rồi dựng đệ quy đạt `O(n)`, tốt hơn nhiều lần insert `O(n log n)`. Các phép split/join tiếp theo mở rộng tinh thần xây theo cấu trúc thay vì theo từng thao tác đơn.

## 32. Bulk bản dựng (build / 빌드)

Nếu đã có sorted keys, xây balanced BST không cần insert từng phần tử.

Chọn middle làm gốc (root / 루트) đệ quy tạo cây (tree / 트리) height tối ưu gần nhất trong `O(n)`.

Nếu dùng insert lặp, dù mỗi insert `O(log n)`, total `O(n log n)`.

Static/batch tải công việc (workload / 워크로드) thường cho phép construction tốt hơn online tải công việc (workload / 워크로드).

> **Mối nối:** Join-based tree coi split và join là nguyên tử xây dựng, rồi dùng chúng để tạo thao tác giàu hơn. Set union giữa hai cây tận dụng chính các phép đó để tránh chèn tuần tự khi kích thước hai tập rất khác nhau.

## 33. Join-Based Balanced Trees

Một góc nhìn nâng cao là xây các thao tác (operation / 연산) từ `split` và `join`.

Nếu có thành phần nguyên thủy (primitive / 기본 요소):

```text
split(T, key)
join(L, key, R)
```

thì union/intersection/difference của ordered sets có thể được xây đệ quy hiệu quả.

Cách nhìn này đặc biệt hữu ích trong functional/persistent trees.

> **Mối nối:** Union, intersection và difference phải giữ cả thứ tự lẫn metadata cân bằng; hiệu quả phụ thuộc tỷ lệ kích thước giữa hai cây. Validator là lớp bảo hiểm để phát hiện bất biến bị hỏng sau những thao tác phức tạp đó.

## 34. Set Union giữa hai Trees

Nếu một set nhỏ hơn nhiều set kia, không nhất thiết insert từng key đơn giản.

Split/phép nối (join / 조인) algorithms có thể tận dụng cấu trúc của cả hai cây (tree / 트리) và đạt độ phức tạp (complexity / 복잡도) phụ thuộc kích thước tương đối tốt hơn trong một số mô hình.

Đây là ví dụ thao tác (operation / 연산) set cao cấp có thể ảnh hưởng lựa chọn cây (tree / 트리) family.

> **Mối nối:** Validator phải kiểm tra miền khóa toàn cục, chiều cao, màu hoặc balance factor, parent pointer và mọi summary được augment. Differential testing bổ sung một đối chứng độc lập để bắt lỗi mà validator cục bộ có thể bỏ sót.

## 35. cây (tree / 트리) Validator

BST validator phải kiểm tra toàn cục (global / 전역) phạm vi (range / 범위), không chỉ parent-child.

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

Augmented cây (tree / 트리) còn phải kiểm tra siêu dữ liệu (metadata / 메타데이터).

Validator sau random operations rất đáng giá khi tự implement.

> **Mối nối:** So sánh với ordered map chuẩn sau mỗi thao tác và chạy chuỗi random dài giúp lộ lỗi rotation, delete hoặc iterator. Kết quả kiểm thử cũng làm rõ những hiểu lầm phổ biến về “balanced” và cận hiệu năng.

## 36. Differential Testing

Có thể so custom cây (tree / 트리) với tiêu chuẩn (standard / 표준) ordered map/set:

```text
insert/delete/contains
min/max
floor/ceiling
range iteration
```

Sau mỗi thao tác (operation / 연산), kiểm tra inorder đầu ra (output / 출력) và invariants.

Rotation bugs thường chỉ lộ sau chuỗi (sequence / 시퀀스) dài, nên stateful random testing rất hữu ích.

> **Mối nối:** Không có cây cân bằng nào miễn phí: AVL, Red-Black, Treap và B-Tree giữ những bất biến khác nhau cho những mô hình chi phí khác nhau. Phần mô hình tư duy gom các đánh đổi ấy thành cách chọn cấu trúc theo workload.

## 37. Những hiểu lầm phổ biến

“BST luôn `O(log n)`” — sai nếu không có balance guarantee.

“AVL luôn nhanh hơn Red-Black” — sai; tải công việc (workload / 워크로드) và cập nhật (update / 업데이트) chi phí (cost / 비용) khác nhau.

“Rotation chỉ đổi hình vẽ” — sai; siêu dữ liệu (metadata / 메타데이터)/parent/iterator ngữ nghĩa (semantics / 의미론) phải được bảo trì.

“Balanced cây (tree / 트리) tốt hơn sorted array vì insert nhanh” — chưa chắc nếu dữ liệu gần tĩnh và locality quan trọng.

“Red-Black color chỉ là hiện thực (implementation / 구현) trick” — màu là encoding của bất biến (invariant / 불변식) giúp chứng minh height bound.

> **Mối nối:** Hãy chọn cây bằng ba câu hỏi: cần thứ tự nào, cập nhật nào chiếm ưu thế, và chi phí vật lý nằm trong RAM hay page I/O? Câu trả lời quyết định bất biến cân bằng, metadata và kiểu kiểm thử cần giữ.

## Mô hình tư duy

> Balanced tìm kiếm (search / 검색) cây (tree / 트리) trả một **chi phí bảo trì cục bộ sau cập nhật (update / 업데이트)** để mua một **cận toàn cục cho chiều cao**.

AVL dùng height difference, Red-Black dùng black-height + màu, Treap dùng random priority, Splay dùng amortized self-adjustment, B-Tree dùng multiway occupancy phù hợp page I/O.

Khi chọn hoặc triển khai balanced cây (tree / 트리), hãy hỏi: **cần deterministic hay expected guarantee, read/ghi (write / 쓰기) ratio ra sao, có cần augmentation/persistence/split-merge không, bộ nhớ (memory / 메모리) locality có quan trọng không, và liệu sorted array hoặc Skip danh sách (list / 목록) đã phù hợp hơn chưa?**

Xem thêm: [Binary Search Trees](./01_binary_search_trees.md), [Augmented Trees](./06_augmented_trees_and_order_statistics.md), [Skip Lists](./07_skip_lists.md), [B/B+Tree](./05_b_trees_and_external_memory.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
