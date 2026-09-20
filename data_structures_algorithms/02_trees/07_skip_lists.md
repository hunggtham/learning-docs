# Skip List  
**스킵 리스트**

Skip list cung cấp ordered-set/map operations expected `O(log n)` nhưng dùng linked lists nhiều tầng và randomness thay vì rotations.

## Từ linked list tới express lanes

Một sorted linked list search `O(n)` vì chỉ đi từng node. Nếu thêm một tầng chứa khoảng một nửa nodes, ta có thể nhảy xa hơn; tầng trên nữa chứa khoảng một phần tư, tiếp tục như vậy.

```text
L2: 1 -------- 9 -------- 20
L1: 1 --- 4 -- 9 --- 15 - 20
L0: 1 2 3 4 5  9 10 15 18 20
```

Search đi right khi next <= target; nếu không, đi xuống level. Đây giống binary-search spirit nhưng trên linked representation.

## Random level

Khi insert, node được promote lên tầng cao hơn với probability, thường gần 1/2 mỗi level. Expected số nodes giảm exponentially theo level, tạo expected logarithmic height/search.

Không có deterministic balance rotations; randomness giữ distribution tốt trong expectation.

## Insert/delete

Search lưu `update[level]`: node trước insertion position ở mỗi tầng. Tạo node với random height rồi splice links ở các tầng nó tham gia.

Delete dùng cùng predecessor path và unlink node ở mọi level.

## So với balanced BST

Skip list implementation thường đơn giản hơn rotations và dễ hỗ trợ certain concurrent designs. Balanced tree cho deterministic worst-case logarithmic guarantees; skip list cho expected guarantees và pointer-rich representation.

Redis sorted sets historically use skip-list-like structure kết hợp hash map trong một số implementations/versions, minh họa composition theo workload.

## Mental Model

> Skip list tạo **nhiều độ phân giải của cùng sorted sequence**. Tầng cao bỏ qua nhiều nodes; tầng thấp hoàn thiện search chính xác.

## Vì sao số tầng chỉ logarithmic trong expectation?

Nếu probability promote là `p = 1/2`, khoảng một nửa nodes lên level 1, một phần tư lên level 2, một phần tám lên level 3.

Expected node count ở level `k` xấp xỉ:

\[
n \left(\frac12\right)^k
\]

Level cao nhất đáng kể xuất hiện khi quantity này gần 1:

\[
n/2^k \approx 1
\Rightarrow k \approx \log_2 n
\]

Đây là nguồn gốc expected logarithmic search height.

## Search algorithm

Ta bắt đầu ở level cao nhất. Nếu `next.key < target`, đi right; nếu next đã vượt target hoặc null, đi xuống một level. Mỗi level cung cấp “express lane” có độ thưa khác nhau.

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

Node thật thường cần `next[]` có length bằng level của chính node; sentinel head giữ max level.

## Insert từ predecessor path

Trong khi search, lưu node cuối cùng nhỏ hơn key ở từng level vào `update[level]`. Sau đó randomize height của node mới và nối:

```text
new.next[level] = update[level].next[level]
update[level].next[level] = new
```

Delete thực hiện rewiring ngược lại ở mọi level mà node tham gia.

Điều này cho thấy skip list vẫn là linked structure; randomness chỉ quyết định những “đường cao tốc” nào tồn tại.

## Deterministic worst case và adversarial randomness

Expected `O(log n)` không phải deterministic worst case. Một sequence random cực xấu về lý thuyết có thể tạo structure kém. Production implementation cần nguồn randomness đủ phù hợp và có thể giới hạn maximum level.

Nếu hệ thống cần hard worst-case latency guarantee, balanced BST có deterministic bound rõ hơn.

## Concurrency connection

Skip list hấp dẫn trong concurrent ordered structures vì update chủ yếu là local pointer changes theo nhiều levels, tránh complex rotations lan qua vài nodes như balanced tree. Concurrent correctness vẫn rất khó vì memory reclamation, ABA-like hazards và atomic ordering; “skip list dễ concurrent hơn” không có nghĩa lock-free implementation đơn giản.

## Ordered operations

Giống balanced BST, skip list hỗ trợ lower-bound/range scan tự nhiên: search điểm bắt đầu expected `O(log n)`, rồi đi level 0 tuần tự qua `k` outputs, tổng expected `O(log n + k)`.

## Mental Model mở rộng

> Balanced BST ép shape tốt bằng invariant deterministic. Skip list để randomness tạo một hierarchy thống kê của cùng sorted sequence. Hai structure giải cùng ordered-search problem bằng hai triết lý maintenance khác nhau.
