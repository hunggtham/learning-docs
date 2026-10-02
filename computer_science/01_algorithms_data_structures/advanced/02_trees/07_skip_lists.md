# Skip danh sách (list / 목록)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Skip danh sách (list / 목록)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ sorted danh sách liên kết tới express lanes** chỉ đường quay lại owner và tài liệu chuẩn khi cần đào sâu; sau đó sang **nút cách biểu diễn** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối skip lists với probabilistic levels, search và update, để đạt tốc độ cây bằng cấu trúc xác suất.

**스킵 리스트 / Skip danh sách (list / 목록)**

Skip danh sách (list / 목록) là cấu trúc set/map có thứ tự, cung cấp tìm kiếm/chèn/xóa với chi phí kỳ vọng `O(log n)` nhưng không dùng phép xoay như AVL hoặc Red-Black cây (tree / 트리). Thay vào đó, nó duy trì nhiều tầng danh sách liên kết với mật độ giảm dần và dùng tính ngẫu nhiên để tạo các “làn đường nhanh”.

Skip danh sách (list / 목록) quan trọng không chỉ vì nó là một alternative cho balanced BST. Nó minh họa một tư tưởng lớn hơn:

> Ta có thể đạt tìm kiếm logarit bằng một **phân cấp nhiều độ phân giải** của cùng một dãy đã sắp xếp, trong đó tầng cao bỏ qua nhiều phần tử còn tầng thấp giữ đầy đủ thứ tự.

## Từ sorted danh sách liên kết tới express lanes

Một danh sách liên kết đơn đã sắp xếp vẫn tìm kiếm `O(n)` vì chỉ có thể đi qua từng nút.

Nếu tạo tầng 1 chứa khoảng một nửa các nút, tầng 2 khoảng một phần tư, tầng 3 khoảng một phần tám, tìm kiếm (search / 검색) có thể nhảy xa ở các tầng cao rồi refine dần.

```text
L3: 1 ------------------------- 20
L2: 1 -------- 9 -------------- 20
L1: 1 --- 4 -- 9 ---- 15 ------ 20
L0: 1 2 3 4 5  9 10  15 18 19 20
```

Tìm kiếm bắt đầu ở tầng cao nhất. Nếu khóa của nút kế tiếp vẫn nhỏ hơn đích thì đi sang phải; nếu nút kế tiếp vượt đích hoặc là `null` thì đi xuống một tầng.

mẫu này giống tìm kiếm nhị phân ở tinh thần “coarse-to-fine”, nhưng cách biểu diễn (representation / 표현) là linked hierarchy thay vì contiguous mảng.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **nút cách biểu diễn** tiếp nhận điểm tựa từ **Từ sorted danh sách liên kết tới express lanes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tìm kiếm (search / 검색) bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## nút cách biểu diễn

Một nút thường giữ:

```text
key
value
forward[0..height-1]
```

Sentinel head có maximum configured tầng.

C sketch:

```c
typedef struct SkipNode {
    int key;
    int level;
    struct SkipNode **next;
} SkipNode;
```

Trong hệ thống thực tế, cách triển khai có thể cấp phát nút + forward các con trỏ trong một khối (block / 블록) để giảm các lần cấp phát/indirection.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **Tìm kiếm (search / 검색) bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **nút cách biểu diễn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ngẫu nhiên chiều cao** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm (search / 검색) bất biến (invariant / 불변식)

Tại mỗi tầng, ta duy trì rằng `cur.key < target` và `cur` là nút xa nhất đã biết ở tầng đó mà chưa vượt đích.

Khi `cur.next[level].key < target`, ta có thể đi sang phải an toàn. Khi nút kế tiếp có khóa `>=` đích, không còn nút nào ở xa hơn trên cùng tầng nhưng nằm trước nút đó cần xét, vì vậy ta đi xuống tầng dưới.

JavaScript:

```js
function find(head, maxLevel, key) {
  let cur = head;

  for (let level = maxLevel; level >= 0; level--) {
    while (cur.next[level] && cur.next[level].key < key) {
      cur = cur.next[level];
    }
  }

  cur = cur.next[0];
  return cur && cur.key === key ? cur : null;
}
```

tính đúng đắn cuối cùng đến từ tầng 0 chứa toàn bộ sorted chuỗi (sequence / 시퀀스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **ngẫu nhiên chiều cao** tiếp nhận điểm tựa từ **Tìm kiếm (search / 검색) bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kỳ vọng tìm kiếm (search / 검색) chi phí intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ngẫu nhiên chiều cao

Khi insert nút, chọn chiều cao ngẫu nhiên. Một scheme phổ biến: bắt đầu tầng 0, mỗi lần coin flip success với xác suất `p` thì promote thêm một tầng.

xác suất nút đạt ít nhất tầng `k` xấp xỉ:

\[
p^k
\]

Với `p=1/2`, kỳ vọng các nút ở tầng `k`:

\[
n\left(\frac12\right)^k
\]

tầng cao nhất đáng kể khi quantity gần 1:

\[
n/2^k\approx1
\Rightarrow k\approx\log_2 n
\]

Đây là nguồn gốc kỳ vọng logarithmic chiều cao.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **kỳ vọng tìm kiếm (search / 검색) chi phí intuition** tiếp nhận điểm tựa từ **ngẫu nhiên chiều cao** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Insert và predecessor đường đi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kỳ vọng tìm kiếm (search / 검색) chi phí intuition

Ở tầng cao, các nút thưa nên ta nhảy khoảng lớn. Khi descend, ta chỉ cần đi một số kỳ vọng constant steps ngang trước khi lại gặp promoted nút phù hợp.

Có khoảng `O(log n)` các tầng và kỳ vọng horizontal công việc (work / 작업) mỗi tầng bounded, nên kỳ vọng tìm kiếm (search / 검색) `O(log n)`.

Đây là kỳ vọng phân tích (analysis / 분석); một ngẫu nhiên kết quả (outcome / 결과) cực xấu vẫn có thể xảy ra.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **Insert và predecessor đường đi** tiếp nhận điểm tựa từ **kỳ vọng tìm kiếm (search / 검색) chi phí intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Delete** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Insert và predecessor đường đi

Khi tìm vị trí chèn, cần lưu nút liền trước ở mỗi tầng:

```text
update[level] = node cuối cùng có key < newKey tại level đó
```

Sau khi randomize new nút chiều cao:

```text
new.next[level] = update[level].next[level]
update[level].next[level] = new
```

cho mọi tầng nút tham gia.

Pseudo:

```java
Node[] update = new Node[MAX_LEVEL];
Node cur = head;

for (int level = currentMax; level >= 0; level--) {
    while (cur.next[level] != null && cur.next[level].key < key) {
        cur = cur.next[level];
    }
    update[level] = cur;
}
```

Nếu khóa tồn tại, map ngữ nghĩa (semantics / 의미론) có thể cập nhật giá trị hoặc reject phần tử trùng tùy đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **Delete** tiếp nhận điểm tựa từ **Insert và predecessor đường đi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **phần tử trùng chính sách** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Delete

Khi xóa, ta tìm cùng đường đi và lưu các nút liền trước. Nếu đích tồn tại ở tầng 0, với mỗi tầng:

```text
nếu update[level].next[level] == target:
    update[level].next[level] = target.next[level]
```

Sau đó có thể giảm hiện tại maximum tầng nếu top các tầng trở thành rỗng.

Thao tác xóa của **Skip danh sách (list / 목록)** mang tính cục bộ hơn các phép xoay cây; đây là một lý do cấu trúc này hấp dẫn trong một số thiết kế xử lý đồng thời.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **phần tử trùng chính sách** tiếp nhận điểm tựa từ **Delete** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **hợp đồng bộ so sánh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## phần tử trùng chính sách

Ordered set có thể reject phần tử trùng khóa. Ordered multiset có thể lưu count hoặc cho nhiều các nút equal các khóa với quy tắc phân xử khi bằng nhau quy tắc. Map cập nhật existing giá trị.

Tìm kiếm, chèn, xóa và duyệt theo khoảng phải dùng cùng ngữ nghĩa bộ so sánh. Nếu cách xử lý phần tử trùng không rõ ràng, các thao tác cận dưới hoặc truy vấn hạng rất dễ sai.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **phần tử trùng chính sách** đã nêu tiêu chí phân biệt, còn **hợp đồng bộ so sánh** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **cận dưới và quét theo khoảng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## hợp đồng bộ so sánh

Skip danh sách (list / 목록) dựa trên thứ tự toàn phần giống BST. Comparator phải consistent và transitive.

Nếu bộ so sánh xem hai khóa khác nhau về mặt nghiệp vụ là bằng nhau (`compare(a,b)==0`), cấu trúc sẽ coi chúng nằm ở cùng một vị trí thứ tự theo hợp đồng API.

Floating-point NaN, case-insensitive strings, locale thứ tự (order / 순서) hoặc composite các khóa cần ngữ nghĩa rõ ràng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **hợp đồng bộ so sánh** đã nêu tiêu chí phân biệt, còn **cận dưới và quét theo khoảng** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Predecessor và successor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cận dưới và quét theo khoảng

Tìm kiếm có thể trả nút đầu tiên có khóa `>= key`, tức cận dưới.

Sau khi tìm start kỳ vọng `O(log n)`, quét theo khoảng đi tầng 0 sequentially:

```text
O(log n + k)
```

với `k` các đầu ra.

Đây là ordered-map năng lực (capability / 역량) tương tự balanced cây.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **Predecessor và successor** tiếp nhận điểm tựa từ **cận dưới và quét theo khoảng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Indexed Skip danh sách (list / 목록)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Predecessor và successor

Successor dễ: nút tiếp theo ở tầng 0.

Predecessor có thể lấy từ đường tìm kiếm (`update[0]`). Nếu API cần bidirectional iteration hiệu quả, nút có thể giữ backward con trỏ tầng 0 hoặc maintain doubly-linked cơ sở (base / 기반) tầng, đổi thêm bộ nhớ/cập nhật chi phí.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **Indexed Skip danh sách (list / 목록)** tiếp nhận điểm tựa từ **Predecessor và successor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weighted spans** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Indexed Skip danh sách (list / 목록)

Skip danh sách (list / 목록) có thể được tăng cường bằng **độ dài nhảy (span/width)** trên mỗi con trỏ tiến: số nút ở tầng 0 mà con trỏ đó bỏ qua.

Sau đó, tìm kiếm theo hạng có thể trừ dần các độ dài nhảy (span), tương tự cây thống kê thứ tự sử dụng kích thước cây con.

Example conceptual mục:

```text
next[level]
span[level]
```

Muốn tìm k-th item, đi right nếu span không vượt rank đích; nếu vượt thì descend.

kỳ vọng `O(log n)` rank/select.

Đây là liên kết (connection / 연결) trực tiếp với [Augmented Trees](./06_augmented_trees_and_order_statistics.md): cả hai lưu dữ liệu tóm lược để skip một region và biết region đóng góp bao nhiêu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **Weighted spans** tiếp nhận điểm tựa từ **Indexed Skip danh sách (list / 목록)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Skip danh sách (list / 목록) vs balanced BST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weighted spans

Span không nhất thiết chỉ đếm số nút. Nó có thể lưu trọng số tích lũy, điểm số hoặc số byte để điều hướng theo vị trí có trọng số trong các cấu trúc chuyên biệt.

Mô hình tư duy là forward cạnh mang dữ liệu tóm lược của segment mà cạnh bỏ qua.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **Skip danh sách (list / 목록) vs balanced BST** tiếp nhận điểm tựa từ **Weighted spans** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kỳ vọng vs trường hợp xấu nhất bảo đảm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Skip danh sách (list / 목록) vs balanced BST

Cả hai hỗ trợ từ điển có thứ tự các thao tác kỳ vọng/xác định logarithmic theo variant.

Balanced BST:

```text
deterministic balance invariant
rotations/recoloring
usually fewer forward pointers per node
hard worst-case bounds
```

Skip danh sách (list / 목록):

```text
randomized height
simple local splice logic
expected logarithmic bounds
more pointer slots / probabilistic shape
```

Không có universal winner. môi trường chạy (runtime) bộ nhớ bố trí, tính đồng thời (concurrency / 동시성), cách triển khai độ phức tạp (complexity / 복잡도) và độ trễ (latency / 지연 시간) các bảo đảm quyết định.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **kỳ vọng vs trường hợp xấu nhất bảo đảm** tiếp nhận điểm tựa từ **Skip danh sách (list / 목록) vs balanced BST** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **xác suất parameter p** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kỳ vọng vs trường hợp xấu nhất bảo đảm

Chi phí kỳ vọng `O(log n)` của Skip danh sách (list / 목록) không phải bảo đảm xác định cho trường hợp xấu nhất. Trong kết quả ngẫu nhiên cực đoan, nhiều nút có thể chỉ ở tầng 0 và quá trình tìm kiếm gần tuyến tính.

mã dùng trong hệ thống thực tế thường set maximum tầng để bound siêu dữ liệu và use good ngẫu nhiên generation.

Nếu hard trường hợp xấu nhất độ trễ là yêu cầu, xác định balanced cây có argument mạnh hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **xác suất parameter p** tiếp nhận điểm tựa từ **kỳ vọng vs trường hợp xấu nhất bảo đảm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ngẫu nhiên tầng generation bằng bits** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## xác suất parameter `p`

`p` điều khiển sự đánh đổi (trade-off / 트레이드오프):

- `p` lớn -> nhiều promoted các nút, nhiều bộ nhớ/các con trỏ, ít horizontal steps;
- `p` nhỏ -> ít bộ nhớ, nhiều horizontal movement.

`p=1/2` phổ biến vì đơn giản, nhưng other các giá trị có thể được chọn theo bộ nhớ đệm/bộ nhớ sự đánh đổi.

kỳ vọng number of forward các con trỏ per nút liên quan geometric phân phối và xấp xỉ constant:

\[
1+p+p^2+\cdots = \frac1{1-p}
\]

với lập chỉ mục convention thích hợp.

Với `p=1/2`, số con trỏ kỳ vọng trên mỗi nút là một hằng số nhỏ, dù một số nút có thể cao hơn nhiều.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **ngẫu nhiên tầng generation bằng bits** tiếp nhận điểm tựa từ **xác suất parameter p** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **xác định skip structures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ngẫu nhiên tầng generation bằng bits

Nếu `p=1/2`, ngẫu nhiên chiều cao có thể lấy từ số consecutive coin successes hoặc bit các mẫu. Low-level mã (code / 코드) có thể dùng count-trailing/leading-zero style trên ngẫu nhiên bits.

Nhưng random-number chất lượng (quality / 품질) và độ lệch (bias / 편향) phải phù hợp. tối ưu hóa (optimization / 최적화) bit trick không đáng nếu làm phân phối sai.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **xác định skip structures** tiếp nhận điểm tựa từ **ngẫu nhiên tầng generation bằng bits** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Redis-like composition intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## xác định skip structures

Có các biến thể xác định sử dụng quy tắc nâng tầng thay cho tính ngẫu nhiên, nhưng độ phức tạp và đặc điểm bảo trì khác với Skip danh sách (list / 목록) trong mô hình kinh điển.

Điểm học chính: multi-level linked lập chỉ mục không bắt buộc probabilistic về bản chất; randomness là một cách rẻ để đạt phân phối tốt kỳ vọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **Redis-like composition intuition** tiếp nhận điểm tựa từ **xác định skip structures** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Skip danh sách (list / 목록) và LSM/memtable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Redis-like composition intuition

Sorted-set các hệ thống thường cần both chính xác member tra cứu và ordered-by-score các thao tác. Một thiết kế (design / 설계) natural là kết hợp:

```text
hash map: member -> metadata/node
ordered structure: score -> sequence
```

Skip danh sách (list / 목록) historically xuất hiện trong hệ thống thực tế ordered-set các cách triển khai vì quét theo khoảng và cục bộ các cập nhật tốt.

Bài học quan trọng hơn specific sản phẩm (product / 제품)/phiên bản (version / 버전) là **composition**: một cấu trúc (structure / 구조) không nhất thiết phục vụ mọi truy vấn lớp (class / 클래스).

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **Skip danh sách (list / 목록) và LSM/memtable** tiếp nhận điểm tựa từ **Redis-like composition intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bộ nhớ tính cục bộ (locality)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Skip danh sách (list / 목록) và LSM/memtable

Một số bộ máy lưu trữ dùng memtable có thứ tự kiểu Skip danh sách (list / 목록): các lần ghi đi vào cấu trúc có thứ tự trong bộ nhớ, hỗ trợ quét khoảng đã sắp xếp, rồi được ghi xuống thành các tệp bất biến đã sắp xếp.

Skip danh sách (list / 목록) phù hợp khi cần chèn động cùng khả năng duyệt theo thứ tự. Các lựa chọn thay thế có thể là cây cân bằng, cây hỗ trợ xử lý đồng thời hoặc những cấu trúc có thứ tự khác.

Đây là liên kết (connection / 연결) giữa DSA và cơ sở dữ liệu/storage-engine ghi (write / 쓰기) đường đi.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **bộ nhớ tính cục bộ (locality)** tiếp nhận điểm tựa từ **Skip danh sách (list / 목록) và LSM/memtable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bộ nhớ overhead** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bộ nhớ tính cục bộ (locality)

Skip danh sách (list / 목록) kinh điển dùng nhiều con trỏ hơn bố trí mảng hoặc trang B-tree. Tìm kiếm phải nhảy giữa các đối tượng trên vùng nhớ động (heap / 힙) nên có thể gây nhiều lần trượt bộ nhớ đệm.

Nếu cách triển khai allocates các nút/forward các mảng compactly hoặc uses arena, tính cục bộ cải thiện. Nhưng generally B-tree-like high-fanout structures tốt hơn bên ngoài bộ nhớ/bộ nhớ đệm page hành vi.

Big-O logarithmic không kể pointer-chasing chi phí.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **bộ nhớ overhead** tiếp nhận điểm tựa từ **bộ nhớ tính cục bộ (locality)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính đồng thời (concurrency / 동시성) motivation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bộ nhớ overhead

Mỗi nút có cơ sở (base / 기반) các trường + variable forward các con trỏ. kỳ vọng con trỏ count constant nhưng overhead/nút có thể lớn so với gọn mảng đã sắp xếp.

Nếu dataset tĩnh/read-heavy, mảng đã sắp xếp + tìm kiếm nhị phân có thể memory-efficient và thân thiện với bộ nhớ đệm hơn rất nhiều.

Skip danh sách (list / 목록) mạnh khi cần cập nhật động đồng thời duy trì thứ tự.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **Tính đồng thời (concurrency / 동시성) motivation** tiếp nhận điểm tựa từ **bộ nhớ overhead** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lô-gic (logic / 논리) deletion và vật lý unlink** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đồng thời (concurrency / 동시성) motivation

Các phép xoay trong cây cân bằng làm thay đổi cấu trúc liên kết cục bộ theo những mẫu tương đối phức tạp. Chèn/xóa trong skip danh sách (list / 목록) chủ yếu dùng CAS hoặc nối lại các con trỏ tiến ở từng tầng, vì vậy cấu trúc này thuận lợi cho một số thuật toán không khóa (lock-free) hoặc xử lý đồng thời.

Tuy nhiên “thuận lợi hơn” không có nghĩa dễ.

Concurrent Skip danh sách (list / 목록) phải xử lý:

```text
node đang insert dở ở vài levels
node logically deleted nhưng chưa unlinked hết
reader đồng thời traverse
ABA/memory reclamation
ordering của atomic writes
```

tính đúng đắn cần linearization điểm (point / 지점) rõ.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **Lô-gic (logic / 논리) deletion và vật lý unlink** tiếp nhận điểm tựa từ **Tính đồng thời (concurrency / 동시성) motivation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **thu hồi bộ nhớ (memory reclamation)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lô-gic (logic / 논리) deletion và vật lý unlink

Concurrent designs thường tách:

```text
logical delete: mark node không còn thuộc abstract set
physical delete: unlink pointers để cleanup
```

thao tác có thể linearize tại mark, còn cleanup giúp tương lai traversal nhưng không thay trừu tượng ngữ nghĩa.

mẫu này phổ biến trong không khóa structures.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **thu hồi bộ nhớ (memory reclamation)** tiếp nhận điểm tựa từ **Lô-gic (logic / 논리) deletion và vật lý unlink** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java ConcurrentSkipListMap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## thu hồi bộ nhớ (memory reclamation)

Ngay cả sau khi một nút đã bị tháo khỏi cấu trúc, luồng đọc khác vẫn có thể đang giữ con trỏ tới nó. Giải phóng ngay có thể dẫn đến lỗi truy cập bộ nhớ sau khi giải phóng (use-after-free).

Techniques gồm con trỏ nguy hiểm, epoch-based reclamation, tham chiếu counting hoặc GC-môi trường chạy có quản lý.

Trong Java, GC loại bỏ một nhóm lỗi liên quan đến thu hồi bộ nhớ, nhưng thứ tự nguyên tử và khả năng nhìn thấy dữ liệu giữa các luồng vẫn phải được xử lý đúng.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **Java ConcurrentSkipListMap** tiếp nhận điểm tựa từ **thu hồi bộ nhớ (memory reclamation)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Persistent Skip danh sách (list / 목록)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java ConcurrentSkipListMap

Java cung cấp `ConcurrentSkipListMap` và `ConcurrentSkipListSet` cho các thao tác có thứ tự trong môi trường đồng thời. Điều quan trọng là hiểu ngữ nghĩa API: vừa điều hướng theo thứ tự vừa hỗ trợ xử lý đồng thời, chứ không nên xem chúng đơn giản là “TreeMap nhưng nhanh hơn”.

sự đánh đổi bộ nhớ/constants và concurrent khối lượng công việc phải được profile.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **Persistent Skip danh sách (list / 목록)?** tiếp nhận điểm tựa từ **Java ConcurrentSkipListMap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Skip đồ thị và phân tán (distributed / 분산) variants** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Persistent Skip danh sách (list / 목록)?

Sao chép theo đường đi trên cây tự nhiên hơn cho tính bền vững (persistence) vì đường nhánh rõ ràng. Skip danh sách (list / 목록) có nhiều con trỏ tiến cắt qua nhiều nút; vẫn có thể làm cấu trúc bền vững nhưng việc chia sẻ cấu trúc và cập nhật thường phức tạp hơn một số loại cây.

Nếu versioning là yêu cầu chính, persistent balanced/functional cây thường natural hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **Skip đồ thị và phân tán (distributed / 분산) variants** tiếp nhận điểm tựa từ **Persistent Skip danh sách (list / 목록)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **dạng lỗi: off-by-one tầng conventions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Skip đồ thị và phân tán (distributed / 분산) variants

Ý tưởng liên kết ngẫu nhiên nhiều tầng có họ hàng với các cấu trúc phủ và tìm kiếm phân tán. Giao thức cụ thể khác Skip danh sách (list / 목록) trong bộ nhớ, nhưng trực giác về phân cấp và định tuyến xác suất có liên hệ.

Điều này cho thấy thiết kế (design / 설계) mẫu “sparse các liên kết nhảy nhanh” có thể quy mô (scale / 규모) beyond one xử lý.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **dạng lỗi: off-by-one tầng conventions** tiếp nhận điểm tựa từ **Skip đồ thị và phân tán (distributed / 분산) variants** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng lỗi: độ dài mảng con trỏ tiến của nút** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## dạng lỗi: off-by-one tầng conventions

Một triển khai có thể gọi tầng cơ sở là 0; khi đó “chiều cao tối đa `h`” có thể nghĩa là các tầng `0..h`, hoặc “số tầng `h`” có thể nghĩa là `0..h-1`. Cần thống nhất quy ước.

Mix conventions dễ gây mảng out-of-bounds hoặc miss top-level link.

Nên define rõ:

```text
height = number of levels in node
valid levels = 0 .. height-1
```

hoặc một convention khác nhưng consistent.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **Dạng lỗi: độ dài mảng con trỏ tiến của nút** tiếp nhận điểm tựa từ **dạng lỗi: off-by-one tầng conventions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **dạng lỗi: ngẫu nhiên seed/kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng lỗi: độ dài mảng con trỏ tiến của nút

Khi traversal ở tầng `L`, hiện tại nút phải có con trỏ ô `L`. Chuẩn thiết kế (design / 설계) đảm bảo chỉ các nút hiện có at that tầng được traversal, giá trị canh gác (sentinel) has max các tầng.

Mã trong ngôn ngữ động có thể che giấu một số lỗi cấu trúc; mã kiểu tĩnh hoặc mức thấp có thể gặp lỗi nghiêm trọng nếu truy cập vượt mảng con trỏ tiến đã được cấp phát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **dạng lỗi: ngẫu nhiên seed/kiểm thử** tiếp nhận điểm tựa từ **Dạng lỗi: độ dài mảng con trỏ tiến của nút** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **xác minh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## dạng lỗi: ngẫu nhiên seed/kiểm thử

ngẫu nhiên shape làm bug khó reproduce. Tests nên cho phép xác định seed hoặc inject bộ sinh tầng ngẫu nhiên.

Sau đó failing chuỗi (sequence / 시퀀스) có thể replay chính xác cấu trúc (structure / 구조).

Trong hệ thống thực tế, tính ngẫu nhiên khi chạy và tính ngẫu nhiên có thể tái lập trong kiểm thử là hai mối quan tâm khác nhau.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **xác minh** tiếp nhận điểm tựa từ **dạng lỗi: ngẫu nhiên seed/kiểm thử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differential kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## xác minh

Validator có thể kiểm tra:

```text
level 0 sorted strictly/non-strictly theo duplicate policy
every higher-level node cũng tồn tại level 0
each level sorted
forward link level không đi tới node có insufficient height
currentMaxLevel khớp top non-empty level
size/count đúng
```

Skip danh sách (list / 목록) có chỉ mục còn phải tính lại các span theo khoảng cách ở tầng cơ sở.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **Differential kiểm thử** tiếp nhận điểm tựa từ **xác minh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Benchmarking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differential kiểm thử

tham chiếu có thể là `TreeMap`, mảng đã sắp xếp/danh sách (list / 목록) hoặc multiset cách triển khai.

ngẫu nhiên chuỗi thao tác:

```text
insert
remove
contains
lowerBound
range scan
rank/select nếu augmented
```

so các kết quả với tham chiếu after every batch.

Randomization của cấu trúc (structure / 구조) không ảnh hưởng trừu tượng ngữ nghĩa, nên differential kiểm thử rất phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **Benchmarking** tiếp nhận điểm tựa từ **Differential kiểm thử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi nào nên cân nhắc Skip danh sách (list / 목록)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Benchmarking

Benchmark Skip danh sách (list / 목록) vs cây phải tách khối lượng công việc:

```text
random lookup
sequential range scan
insert-heavy
mixed read/write
concurrent contention
memory footprint
```

A single phép đo hiệu năng vi mô “100k gets” không nói hết sự đánh đổi.

Dataset kích thước (size / 크기) so với CPU bộ nhớ đệm cũng có thể đổi kết quả đáng kể.

> **Chuyển mạch:** Trong **Skip danh sách (list / 목록)**, **Khi nào nên cân nhắc Skip danh sách (list / 목록)** tiếp nhận điểm tựa từ **Benchmarking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi nào nên cân nhắc Skip danh sách (list / 목록)

Nên cân nhắc Skip danh sách (list / 목록) khi cần ánh xạ hoặc tập hợp có thứ tự và cập nhật động, cần duyệt theo khoảng, muốn tránh độ phức tạp của phép xoay cây, hoặc khi thiết kế đồng thời hưởng lợi từ việc nối lại con trỏ mang tính cục bộ.

Nếu tập dữ liệu tĩnh, mảng đã sắp xếp thường đơn giản và có tính cục bộ tốt. Nếu bài toán theo mô hình bộ nhớ ngoài hoặc theo trang, B+cây (tree / 트리) mạnh hơn. Nếu chỉ cần tra cứu chính xác theo quan hệ bằng nhau, bảng băm thường phù hợp. Nếu bắt buộc có cận xác định cho trường hợp xấu nhất, cây cân bằng xác định rõ ràng hơn.

> **Chuyển mạch:** Ở chặng này của **Skip danh sách (list / 목록)**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **Khi nào nên cân nhắc Skip danh sách (list / 목록)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

“Skip danh sách (list / 목록) là danh sách liên kết nên tìm kiếm tuyến tính” là sai vì cấu trúc phân tầng làm thay đổi đường tìm kiếm kỳ vọng.

“kỳ vọng `O(log n)` nghĩa mỗi thao tác chắc chắn logarithmic” sai.

“tính đồng thời (concurrency / 동시성) dễ hơn cây nghĩa cách triển khai không khóa đơn giản” sai; reclamation và atomic giao thức (protocol / 프로토콜) vẫn phức tạp.

“ngẫu nhiên promotion càng nhiều càng nhanh” sai vì bộ nhớ/bộ nhớ đệm overhead tăng và có phương án tối ưu sự đánh đổi.

“Skip danh sách (list / 목록) chỉ là academic cấu trúc (structure / 구조)” sai; ordered concurrent/lập chỉ mục khối lượng công việc đã dùng variants trong real các hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Skip danh sách (list / 목록)**, **Mô hình tư duy** gom các mảnh từ **Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Skip danh sách (list / 목록) không cân bằng cây; nó điều chỉnh **mật độ các liên kết nhảy nhanh** bằng tính ngẫu nhiên. Tầng 0 giữ đầy đủ dữ liệu, các tầng cao là những chỉ mục thưa của cùng dãy đã sắp xếp. Tìm kiếm đi từ độ phân giải thô xuống độ phân giải mịn, còn chèn/xóa chỉ nối lại những liên kết mà nút tham gia.

Khi đánh giá Skip danh sách (list / 목록), hãy hỏi: **kỳ vọng bảo đảm có đủ không, quét theo khoảng có quan trọng không, bộ nhớ/con trỏ tính cục bộ thế nào, tính đồng thời (concurrency / 동시성) có cần không, và comparator/phần tử trùng ngữ nghĩa có rõ không?**

Xem tiếp: [Linked Lists](../01_linear_structures/01_linked_lists.md), [Balanced Search Trees](./02_balanced_search_trees.md), [Augmented Trees](./06_augmented_trees_and_order_statistics.md), [B-Tree & External Memory](./05_b_trees_and_external_memory.md) và [Amortized & Randomized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
