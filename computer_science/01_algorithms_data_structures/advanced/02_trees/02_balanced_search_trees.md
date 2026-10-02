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

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **2. Rotation bảo toàn thứ tự thế nào?** tiếp nhận điểm tựa từ **1. Hai lớp bất biến khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. siêu dữ liệu (metadata / 메타데이터) cập nhật (update / 업데이트) thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **2. Rotation bảo toàn thứ tự thế nào?** nêu điều cần giải thích; **3. siêu dữ liệu (metadata / 메타데이터) cập nhật (update / 업데이트) thứ tự (order / 순서)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. AVL cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. siêu dữ liệu (metadata / 메타데이터) cập nhật (update / 업데이트) thứ tự (order / 순서)

Sau right rotation ở `y`:

```text
y trở thành con của x
```

Nên recompute `y` trước, rồi `x`, vì siêu dữ liệu (metadata / 메타데이터) mới của `x` phụ thuộc siêu dữ liệu (metadata / 메타데이터) mới của `y`.

Mẫu (pattern / 패턴) tổng quát:

> Khi relink cây (tree / 트리), cập nhật siêu dữ liệu (metadata / 메타데이터) từ dưới lên theo topology mới.

Sai thứ tự có thể tạo cây đúng về BST nhưng sai về augmentation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **3. siêu dữ liệu (metadata / 메타데이터) cập nhật (update / 업데이트) thứ tự (order / 순서)** nêu điều cần giải thích; **4. AVL cây (tree / 트리)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. Vì sao AVL có chiều cao logarithmic?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **5. Vì sao AVL có chiều cao logarithmic?** tiếp nhận điểm tựa từ **4. AVL cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Bốn trường hợp (case / 사례) AVL thực chất là hai hình dạng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **5. Vì sao AVL có chiều cao logarithmic?** cho ta quy tắc; **6. Bốn trường hợp (case / 사례) AVL thực chất là hai hình dạng** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. AVL Insert** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **6. Bốn trường hợp (case / 사례) AVL thực chất là hai hình dạng** cho ta quy tắc; **7. AVL Insert** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **8. AVL Delete khó hơn Insert** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. AVL Insert

Quy trình:

1. insert như BST;
2. đi ngược đường dẫn (path / 경로);
3. recompute height;
4. tính balance factor;
5. rotate nếu vi phạm;
6. tiếp tục cập nhật siêu dữ liệu (metadata / 메타데이터) cần thiết.

Insertion chỉ ảnh hưởng các tổ tiên của vị trí chèn.

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **8. AVL Delete khó hơn Insert** tiếp nhận điểm tựa từ **7. AVL Insert** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Red-Black cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. AVL Delete khó hơn Insert

Delete có thể làm height subtree giảm. Sau khi sửa một imbalance, height của subtree mới vẫn có thể thấp hơn trước, tiếp tục làm ancestor cao hơn mất cân bằng.

Vì vậy delete thường phải tiếp tục kiểm tra tới gốc (root / 루트).

Đây là khác biệt quan trọng giữa:

```text
insert -> height có thể tăng
remove -> height có thể giảm dây chuyền
```

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **9. Red-Black cây (tree / 트리)** tiếp nhận điểm tựa từ **8. AVL Delete khó hơn Insert** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Vì sao Red-Black cũng logarithmic?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Red-Black cây (tree / 트리)

Red-Black cây (tree / 트리) không theo dõi chênh lệch height trực tiếp. Nó dùng màu để encode một ràng buộc cân bằng mềm hơn.

Các bất biến (invariant / 불변식) phổ biến:

1. mỗi nút (node / 노드) đỏ hoặc đen;
2. gốc (root / 루트) đen;
3. null leaf được xem là đen;
4. nút (node / 노드) đỏ không có child đỏ;
5. mọi đường dẫn (path / 경로) từ một nút (node / 노드) tới null leaf có cùng số nút (node / 노드) đen.

Số nút (node / 노드) đen trên đường dẫn (path / 경로) được gọi là **black height**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **10. Vì sao Red-Black cũng logarithmic?** tiếp nhận điểm tựa từ **9. Red-Black cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Red-Black Insert** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Vì sao Red-Black cũng logarithmic?

Vì không có hai nút (node / 노드) đỏ liên tiếp, trên một root-to-leaf đường dẫn (path / 경로) số nút (node / 노드) đỏ không vượt số nút (node / 노드) đen đáng kể.

Mọi đường dẫn (path / 경로) có cùng black height, nên đường dẫn (path / 경로) dài nhất không quá khoảng hai lần đường dẫn (path / 경로) ngắn nhất theo số mức (level / 수준) liên quan.

Từ đó suy ra:

\[
h=O(\log n)
\]

Red-Black cho phép hình dạng “lỏng” hơn AVL nhưng vẫn đủ giữ logarithmic bound.

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **11. Red-Black Insert** tiếp nhận điểm tựa từ **10. Vì sao Red-Black cũng logarithmic?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Red-Black Delete** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **12. Red-Black Delete** tiếp nhận điểm tựa từ **11. Red-Black Insert** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. AVL vs Red-Black** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **13. AVL vs Red-Black** tiếp nhận điểm tựa từ **12. Red-Black Delete** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Treap: Balance bằng Random Priority** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **14. Treap: Balance bằng Random Priority** tiếp nhận điểm tựa từ **13. AVL vs Red-Black** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Split và Merge trong Treap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Treap: Balance bằng Random Priority

Treap giữ:

```text
BST order theo key
heap order theo random priority
```

Nếu priorities độc lập ngẫu nhiên, expected height là `O(log n)`.

Treap cho thấy balance không nhất thiết đến từ deterministic siêu dữ liệu (metadata / 메타데이터) như height hoặc color. Randomness cũng có thể tạo expected balance.

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **15. Split và Merge trong Treap** tiếp nhận điểm tựa từ **14. Treap: Balance bằng Random Priority** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Implicit Treap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Split và Merge trong Treap

Treap đặc biệt mạnh vì `split` và `merge` rất tự nhiên.

`split(root,key)` chia thành:

```text
L: keys < key
R: keys >= key
```

`merge(L,R)` yêu cầu mọi key của `L` nhỏ hơn mọi key của `R`, rồi dùng vùng nhớ động (heap / 힙) priority để chọn gốc (root / 루트).

Nhiều chuỗi (sequence / 시퀀스)/data-structure operations có thể xây từ split/merge thay vì viết insert/delete riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **16. Implicit Treap** tiếp nhận điểm tựa từ **15. Split và Merge trong Treap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Splay cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **17. Splay cây (tree / 트리)** tiếp nhận điểm tựa từ **16. Implicit Treap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Weight-Balanced cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Splay cây (tree / 트리)

Splay cây (tree / 트리) không giữ balance bất biến (invariant / 불변식) cứng. Sau truy cập (access / 접근), nút (node / 노드) được đưa lên gốc (root / 루트) bằng zig, zig-zig, zig-zag rotations.

Một thao tác có thể `O(n)`, nhưng amortized `O(log n)`.

Điểm thú vị là cấu trúc (structure / 구조) tự thích nghi: item được truy cập gần đây hoặc thường xuyên có xu hướng gần gốc (root / 루트).

Splay cây (tree / 트리) minh họa sự đánh đổi (trade-off / 트레이드오프) giữa worst-case per thao tác (operation / 연산) và adaptive locality.

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **18. Weight-Balanced cây (tree / 트리)** tiếp nhận điểm tựa từ **17. Splay cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Scapegoat cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Weight-Balanced cây (tree / 트리)

Có thể cân bằng dựa trên subtree kích thước (size / 크기) thay vì height/color.

Ví dụ yêu cầu hai subtree không quá lệch theo tỷ lệ. Khi vi phạm, rotate/rebuild.

Ý tưởng quan trọng:

> “Balanced” không chỉ có một định nghĩa; miễn bất biến (invariant / 불변식) đủ mạnh để bound height hoặc expected chi phí (cost / 비용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **19. Scapegoat cây (tree / 트리)** tiếp nhận điểm tựa từ **18. Weight-Balanced cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. B-Tree là Balanced tìm kiếm (search / 검색) cây (tree / 트리) cho Page I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Scapegoat cây (tree / 트리)

Scapegoat cây (tree / 트리) tránh lưu balance siêu dữ liệu (metadata / 메타데이터) ở mọi nút (node / 노드). Khi insertion làm cây (tree / 트리) quá cao, tìm một ancestor “scapegoat” có subtree mất cân bằng rồi rebuild toàn subtree đó thành cây cân bằng.

Một cập nhật (update / 업데이트) riêng có thể đắt, nhưng amortized bound tốt.

Đây là ví dụ khác của deamortized-vs-amortized thiết kế (design / 설계) không gian (space / 공간).

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **20. B-Tree là Balanced tìm kiếm (search / 검색) cây (tree / 트리) cho Page I/O** tiếp nhận điểm tựa từ **19. Scapegoat cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Ordered Map năng lực (capability / 역량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. B-Tree là Balanced tìm kiếm (search / 검색) cây (tree / 트리) cho Page I/O

B-Tree/B+cây (tree / 트리) cũng cân bằng, nhưng nút (node / 노드) có nhiều child.

Mục tiêu không chỉ giảm số comparison mà giảm số page truy cập (access / 접근).

Balanced nhị phân (binary / 이진) cây (tree / 트리) height `O(log_2 n)`; B-Tree với fanout `B` có height gần:

\[
O(\log_B n)
\]

Balanced-tree thiết kế (design / 설계) phải khớp chi phí (cost / 비용) mô hình (model / 모델) của lưu trữ (storage / 저장소) medium.

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **21. Ordered Map năng lực (capability / 역량)** tiếp nhận điểm tựa từ **20. B-Tree là Balanced tìm kiếm (search / 검색) cây (tree / 트리) cho Page I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Duplicate Keys** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **22. Duplicate Keys** tiếp nhận điểm tựa từ **21. Ordered Map năng lực (capability / 역량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Comparator đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **23. Comparator đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **22. Duplicate Keys** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Augmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **24. Augmentation** tiếp nhận điểm tựa từ **23. Comparator đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. thứ tự (order / 순서) Statistics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **25. thứ tự (order / 순서) Statistics** tiếp nhận điểm tựa từ **24. Augmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Interval cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **26. Interval cây (tree / 트리)** tiếp nhận điểm tựa từ **25. thứ tự (order / 순서) Statistics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Persistent Balanced cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Interval cây (tree / 트리)

Nếu nút (node / 노드) keyed theo interval start và lưu `maxEnd` của subtree, có thể prune subtree không thể giao truy vấn (query / 쿼리) interval.

Balanced bất biến (invariant / 불변식) giữ height; augmentation giữ summary phục vụ overlap truy vấn (query / 쿼리).

Hai lớp bất biến hoạt động độc lập nhưng phải cùng được bảo trì sau rotation.

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **27. Persistent Balanced cây (tree / 트리)** tiếp nhận điểm tựa từ **26. Interval cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Parent Pointer và Iterator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Persistent Balanced cây (tree / 트리)

Với immutable/persistent cây (tree / 트리), cập nhật (update / 업데이트) chỉ sao chép các nút (node / 노드) trên tìm kiếm (search / 검색) đường dẫn (path / 경로) và chia sẻ subtree không đổi.

Nếu cây (tree / 트리) height `O(log n)`, một cập nhật (update / 업데이트) tạo `O(log n)` nút (node / 노드) mới.

Persistent Red-Black/AVL/Treap có thể hỗ trợ snapshot/versioning hiệu quả.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **28. Parent Pointer và Iterator** tiếp nhận điểm tựa từ **27. Persistent Balanced cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Parent Pointer và Iterator

Nếu cần iterator predecessor/successor nhanh, parent pointer có thể hữu ích.

Nhưng mỗi rotation phải cập nhật parent pointer đúng.

Nếu iterator giữ raw nút (node / 노드) tham chiếu (reference / 참조), delete/rotation/vô hiệu hóa (invalidation / 무효화) ngữ nghĩa (semantics / 의미론) phải được định nghĩa rõ.

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **29. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃)** tiếp nhận điểm tựa từ **28. Parent Pointer và Iterator** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Concurrent Balanced Trees** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃)

Node-based trees có pointer chasing và đối tượng (object / 객체) overhead.

Với dữ liệu nhỏ/tĩnh, sorted array có thể nhanh hơn cây (tree / 트리) dù insert/delete tệ hơn, vì:

```text
contiguous memory
fewer allocations
better cache locality
```

Balanced cây (tree / 트리) đáng giá khi mutation/thứ tự (order / 순서) queries thực sự cần.

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **30. Concurrent Balanced Trees** tiếp nhận điểm tựa từ **29. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Optimistic Read** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Concurrent Balanced Trees

Concurrent cây (tree / 트리) khó hơn băm (hash / 해시) Map hoặc Skip danh sách (list / 목록) vì rotation thay đổi nhiều pointer liên quan.

Fine-grained locking phải xác định khóa (lock / 잠금) thứ tự (order / 순서) để tránh deadlock. Lock-free cây (tree / 트리) cần linearization, bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) và reclamation rất phức tạp.

Đây là lý do concurrent ordered maps đôi khi dùng Skip danh sách (list / 목록): expected `O(log n)` nhưng cập nhật (update / 업데이트) topology cục bộ theo mức (level / 수준) có thể thuận lợi hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **31. Optimistic Read** tiếp nhận điểm tựa từ **30. Concurrent Balanced Trees** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Bulk bản dựng (build / 빌드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Optimistic Read

Một số hiện thực (implementation / 구현) cho reader đọc mà không khóa toàn cây (tree / 트리), rồi validate phiên bản (version / 버전)/stamp để phát hiện writer đã thay đổi cấu trúc.

Mẫu này đánh đổi thử lại (retry / 재시도) để giảm contention read-heavy.

Cấu trúc dữ liệu (data structure / 자료구조) tính đồng thời (concurrency / 동시성) không chỉ chọn khóa (lock / 잠금) hay no-lock; có cả optimistic kiểm tra hợp lệ (validation / 검증) và sao chép khi ghi (copy-on-write / 쓰기 시 복사).

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **32. Bulk bản dựng (build / 빌드)** tiếp nhận điểm tựa từ **31. Optimistic Read** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Join-Based Balanced Trees** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Bulk bản dựng (build / 빌드)

Nếu đã có sorted keys, xây balanced BST không cần insert từng phần tử.

Chọn middle làm gốc (root / 루트) đệ quy tạo cây (tree / 트리) height tối ưu gần nhất trong `O(n)`.

Nếu dùng insert lặp, dù mỗi insert `O(log n)`, total `O(n log n)`.

Static/batch tải công việc (workload / 워크로드) thường cho phép construction tốt hơn online tải công việc (workload / 워크로드).

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **33. Join-Based Balanced Trees** tiếp nhận điểm tựa từ **32. Bulk bản dựng (build / 빌드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Set Union giữa hai Trees** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Join-Based Balanced Trees

Một góc nhìn nâng cao là xây các thao tác (operation / 연산) từ `split` và `join`.

Nếu có thành phần nguyên thủy (primitive / 기본 요소):

```text
split(T, key)
join(L, key, R)
```

thì union/intersection/difference của ordered sets có thể được xây đệ quy hiệu quả.

Cách nhìn này đặc biệt hữu ích trong functional/persistent trees.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **34. Set Union giữa hai Trees** tiếp nhận điểm tựa từ **33. Join-Based Balanced Trees** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. cây (tree / 트리) Validator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Set Union giữa hai Trees

Nếu một set nhỏ hơn nhiều set kia, không nhất thiết insert từng key đơn giản.

Split/phép nối (join / 조인) algorithms có thể tận dụng cấu trúc của cả hai cây (tree / 트리) và đạt độ phức tạp (complexity / 복잡도) phụ thuộc kích thước tương đối tốt hơn trong một số mô hình.

Đây là ví dụ thao tác (operation / 연산) set cao cấp có thể ảnh hưởng lựa chọn cây (tree / 트리) family.

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **35. cây (tree / 트리) Validator** tiếp nhận điểm tựa từ **34. Set Union giữa hai Trees** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Differential Testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Cây tìm kiếm cân bằng**, **36. Differential Testing** tiếp nhận điểm tựa từ **35. cây (tree / 트리) Validator** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây tìm kiếm cân bằng**, **37. Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **36. Differential Testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Những hiểu lầm phổ biến

“BST luôn `O(log n)`” — sai nếu không có balance guarantee.

“AVL luôn nhanh hơn Red-Black” — sai; tải công việc (workload / 워크로드) và cập nhật (update / 업데이트) chi phí (cost / 비용) khác nhau.

“Rotation chỉ đổi hình vẽ” — sai; siêu dữ liệu (metadata / 메타데이터)/parent/iterator ngữ nghĩa (semantics / 의미론) phải được bảo trì.

“Balanced cây (tree / 트리) tốt hơn sorted array vì insert nhanh” — chưa chắc nếu dữ liệu gần tĩnh và locality quan trọng.

“Red-Black color chỉ là hiện thực (implementation / 구현) trick” — màu là encoding của bất biến (invariant / 불변식) giúp chứng minh height bound.

> **Chuyển mạch:** Trong **Cây tìm kiếm cân bằng**, **Mô hình tư duy** gom các mảnh từ **37. Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Balanced tìm kiếm (search / 검색) cây (tree / 트리) trả một **chi phí bảo trì cục bộ sau cập nhật (update / 업데이트)** để mua một **cận toàn cục cho chiều cao**.

AVL dùng height difference, Red-Black dùng black-height + màu, Treap dùng random priority, Splay dùng amortized self-adjustment, B-Tree dùng multiway occupancy phù hợp page I/O.

Khi chọn hoặc triển khai balanced cây (tree / 트리), hãy hỏi: **cần deterministic hay expected guarantee, read/ghi (write / 쓰기) ratio ra sao, có cần augmentation/persistence/split-merge không, bộ nhớ (memory / 메모리) locality có quan trọng không, và liệu sorted array hoặc Skip danh sách (list / 목록) đã phù hợp hơn chưa?**

Xem thêm: [Binary Search Trees](./01_binary_search_trees.md), [Augmented Trees](./06_augmented_trees_and_order_statistics.md), [Skip Lists](./07_skip_lists.md), [B/B+Tree](./05_b_trees_and_external_memory.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
