# Case Study: Streaming Analytics với dữ liệu lớn
**Streaming Analytics Case Study / 스트리밍 분석 사례**

Streaming analytics xử lý chuỗi sự kiện đến liên tục thay vì một tập dữ liệu tĩnh đã biết trước. Ví dụ: log hệ thống, clickstream, giao dịch, packet mạng, metric observability hoặc sự kiện IoT.

Khó khăn cốt lõi là:

```text
dòng dữ liệu có thể không kết thúc
không thể giữ mọi sự kiện trong RAM
cần kết quả gần thời gian thực
có thể chấp nhận xấp xỉ cho một số truy vấn
state phải gộp được giữa nhiều worker
```

Case study này nối Hash Table, Heap, Count-Min Sketch, HyperLogLog, Reservoir Sampling, Sliding Window và distributed merge thành một pipeline thực tế.

## 1. Những truy vấn điển hình

Một hệ thống telemetry có thể cần:

```text
bao nhiêu user phân biệt trong 5 phút gần nhất?
endpoint nào xuất hiện nhiều nhất?
request nào có latency cao nhất?
phân phối latency p50/p95/p99 là gì?
service nào tăng error rate đột biến?
```

Không phải mọi truy vấn đều cần cùng mức chính xác.

Ví dụ số billing có thể cần chính xác; cardinality dashboard có thể chấp nhận sai số 1–2%; heavy hitter detection thường chỉ cần tìm đúng nhóm lớn nhất.

## 2. Exact state bằng Hash Map

Baseline cho tần suất:

```text
key -> count
```

Hash Map cho update kỳ vọng `O(1)`.

Nhưng nếu cardinality của key lên hàng trăm triệu, memory tăng tuyến tính theo số key phân biệt. Đây là điểm hệ thống phải quyết định:

```text
state chính xác còn vừa bộ nhớ không?
```

Nếu không, cần approximation hoặc partitioning.

## 3. Top-K với Hash Map + Heap

Nếu vẫn giữ count chính xác, Top-K có thể được lấy bằng min-heap kích thước `K`:

```text
scan counts
push candidate
nếu heap.size > K -> pop nhỏ nhất
```

Chi phí:

\[
O(n\log K)
\]

với `n` là số key phân biệt.

Nếu cần Top-K liên tục sau mỗi event, cập nhật heap trực tiếp phức tạp hơn vì priority thay đổi. Có thể dùng indexed heap hoặc lazy entries.

## 4. Count-Min Sketch khi không thể giữ mọi key

CMS giữ ma trận bộ đếm nhỏ và nhiều hàm băm. Mỗi event cập nhật một ô ở mỗi hàng.

Ước lượng:

```text
estimate(key) = min(counters corresponding to key)
```

Trong mô hình cập nhật không âm, CMS không đánh giá thấp số đếm thật; va chạm chỉ làm tăng ước lượng.

Memory phụ thuộc `ε`, `δ`, không phụ thuộc trực tiếp số key phân biệt.

Đây là lý do CMS phù hợp telemetry có keyspace rất lớn.

## 5. CMS không tự tìm được key nổi bật

Sketch biết “key X khoảng bao nhiêu” nếu ta hỏi X, nhưng không lưu danh sách tất cả key.

Muốn heavy hitters cần thêm candidate set:

```text
CMS + heap/set ứng viên
```

hoặc dùng thuật toán như Misra–Gries/Space-Saving.

Đây là ví dụ quan trọng:

> Query by known key và discovery of unknown key là hai loại bài toán khác nhau.

## 6. Space-Saving cho heavy hitters

Space-Saving giữ một số lượng counter hữu hạn cho các candidate lớn.

Khi key mới không có counter và mọi slot đã dùng, nó thay candidate có count nhỏ nhất rồi cập nhật sai số tương ứng.

Với distribution lệch mạnh kiểu Zipf, nó có thể theo dõi heavy hitters rất hiệu quả.

Một pipeline thực tế có thể dùng:

```text
Space-Saving -> candidate discovery
exact backend -> verify candidate
```

## 7. HyperLogLog cho distinct count

Muốn đếm số user phân biệt chính xác cần Hash Set:

```text
user_id -> membership
```

Memory tăng theo cardinality.

HyperLogLog giữ thống kê trên hash và dùng rất ít memory so với Hash Set.

Các worker có thể merge HLL bằng phép `max` theo từng register, nên rất phù hợp distributed aggregation.

## 8. Mergeability là tính chất hệ thống quan trọng

Trong distributed stream processing, mỗi partition xử lý một phần dữ liệu:

```text
partition 1 -> sketch A
partition 2 -> sketch B
partition 3 -> sketch C
```

Nếu sketch có phép merge kết hợp:

```text
merge(merge(A,B),C) = merge(A,merge(B,C))
```

coordinator có thể dùng tree reduction song song.

Đây là lý do HLL/CMS/bottom-k hấp dẫn hơn nhiều cấu trúc exact không dễ merge ở quy mô lớn.

## 9. Time Window làm state khó hơn

“Distinct count từ đầu hệ thống” dễ hơn “distinct count 5 phút gần nhất”.

Nếu sketch chỉ tăng đơn điệu, nó không tự quên event cũ.

Các cách phổ biến:

```text
bucket theo thời gian
ring of sketches
exponential histogram
sliding-window sketch chuyên dụng
```

Ví dụ giữ 60 HLL cho 60 phút gần nhất rồi merge các bucket cần thiết.

Đổi lại, boundary của window và memory tăng theo số bucket.

## 10. Tumbling, Sliding và Session Window

**Tumbling Window** chia thời gian thành các đoạn không chồng lấp.

**Sliding Window** có thể chồng lấp và cập nhật thường xuyên.

**Session Window** kết thúc khi user không hoạt động trong một khoảng timeout.

Session window cần state theo key và timeout management; thường dùng timer queue/heap hoặc timer wheel.

Cùng gọi là “window”, nhưng state machine rất khác nhau.

## 11. Event Time và Processing Time

Streaming thực có event đến trễ hoặc ngoài thứ tự.

```text
event time      -> thời gian sự kiện thực xảy ra
processing time -> thời gian hệ thống xử lý
```

Nếu dùng event time, phải quyết định chờ bao lâu cho event trễ. Watermark là một cách biểu diễn tiến độ thời gian logic.

Đây không còn là DSA thuần nhưng state/window structure phải phù hợp semantics thời gian.

## 12. Reservoir Sampling

Nếu muốn giữ một mẫu đại diện `k` event từ stream chưa biết trước độ dài, Reservoir Sampling dùng bộ nhớ `O(k)`.

Nó tránh thiên lệch về event đầu hoặc cuối và rất hữu ích cho debug, inspection hoặc offline analysis.

Sampling là cách giảm dữ liệu trong khi cố giữ phân phối đại diện.

## 13. Quantile Sketch

Latency percentile không thể tính chỉ bằng average. Muốn p99 chính xác có thể cần giữ/sort lượng dữ liệu lớn.

Các sketch quantile như KLL/t-digest (tùy domain) nén phân phối để ước lượng percentile với bộ nhớ giới hạn.

Điểm cần hiểu là:

```text
mean -> aggregate đơn giản
quantile -> cần thông tin về distribution
```

Do đó state phức tạp hơn một counter.

## 14. Histogram

Một histogram cố định chia miền giá trị thành bucket:

```text
0–10 ms
10–50 ms
50–100 ms
...
```

Memory nhỏ và merge rất dễ, nhưng precision phụ thuộc boundary.

Nếu distribution thay đổi mạnh, bucket cố định có thể mất chi tiết ở vùng quan trọng.

Đây là trade-off giữa simplicity, mergeability và precision.

## 15. Approximate vs Exact Pipeline

Một kiến trúc mạnh thường dùng hai tầng:

```text
approximate path:
    rẻ, rộng, liên tục

exact path:
    đắt hơn, chỉ chạy cho candidate quan trọng
```

Ví dụ:

```text
CMS phát hiện endpoint có vẻ nóng
→ thêm vào exact counter map
→ nếu vượt threshold thì alert
```

Approximation giúp giảm search space, không nhất thiết thay thế kết quả chính xác cuối cùng.

## 16. Partitioning theo key

Để state cùng key nằm một worker, hệ thống có thể dùng:

```text
partition = hash(key) mod N
```

Hashing cân bằng tương đối nhưng khi số partition thay đổi sẽ remap nhiều key. Consistent/rendezvous hashing có thể giảm lượng state di chuyển trong một số kiến trúc.

Stateful streaming vì vậy nối trực tiếp với hashing phân tán.

## 17. Hot Key

Nếu một key chiếm 30% lưu lượng, hash partitioning vẫn không cân bằng vì toàn bộ key đó đi cùng một worker.

Các chiến lược gồm:

```text
salting key
local partial aggregation
hierarchical combine
special-case hot keys
```

Ví dụ split `celebrity_user` thành nhiều subkey rồi merge count ở tầng sau.

Đây là vấn đề distribution, không phải lỗi của hash function.

## 18. Backpressure

Nếu downstream xử lý chậm hơn upstream, queue tăng mãi.

Cần chính sách:

```text
block producer
drop samples
spill to disk
scale consumers
reduce fidelity
```

Queue capacity là một phần của reliability contract.

Streaming analytics vì vậy kết nối trực tiếp với scheduler/backpressure, không chỉ sketch.

## 19. Exactly-once, At-least-once và duplicate

Nếu event có thể được xử lý lại sau retry, counter đơn giản có thể đếm trùng.

Cần xác định semantics:

```text
at-most-once
at-least-once
exactly-once theo phạm vi hệ thống
```

Dedup có thể cần event ID + Hash Set/TTL index, nhưng state dedup cũng tốn memory.

Approximate duplicate filters như Bloom Filter có thể tạo false positive, vì vậy không phải domain nào cũng chấp nhận được.

## 20. Snapshot và Recovery

State phải được checkpoint:

```text
Hash Map state
sketch registers
window buckets
timers
```

Nếu snapshot không nhất quán với input offset, recovery có thể mất hoặc đếm lại event.

Một cấu trúc đúng trong RAM chưa đủ; distributed state cần protocol persistence tương ứng.

## 21. Monitoring chính sketch

Approximate structure cũng cần observability:

```text
Bloom saturation
CMS collision/error trend
HLL version/precision
counter overflow
merge compatibility
bucket age
```

Nếu dữ liệu tăng gấp 100 lần so với assumption ban đầu, error guarantee có thể không còn phù hợp.

## 22. Testing

Dùng exact model trên dữ liệu nhỏ để đối chiếu:

```text
Hash Map exact counts
Hash Set exact cardinality
full sorted values cho percentile
```

Với sketch, kiểm tra distribution sai số qua nhiều seed/dataset thay vì một lần chạy.

Cần thử:

```text
uniform distribution
Zipf/heavy-tail
hot key
sudden traffic spike
late event
duplicate/retry
window boundary
```

## 23. Benchmark

Đo đồng thời:

```text
events/second
bytes of state
update latency
merge cost
checkpoint size
error distribution
p95/p99 processing latency
```

Không nên chỉ đo CPU throughput mà bỏ qua state growth và recovery cost.

## 24. Kiến trúc khái niệm

```text
Event Stream
   ↓
Partition by key
   ↓
Local exact/approximate state
   ├─ Hash Map
   ├─ Count-Min Sketch
   ├─ HyperLogLog
   ├─ Quantile Sketch
   └─ Reservoir Sample
   ↓
Window / Watermark
   ↓
Merge / Reduce
   ↓
Top-K / Alert / Dashboard
```

## Mô hình tư duy

> Streaming analytics là bài toán **quản lý state dưới giới hạn tài nguyên**. Exact structure giữ chi tiết nhưng state tăng theo dữ liệu; sketch chủ động nén thông tin và đổi lại sai số có kiểm soát. Window thêm chiều thời gian, partitioning thêm chiều phân tán, còn backpressure quyết định hệ thống phản ứng thế nào khi tốc độ đến vượt khả năng xử lý.

Xem thêm: [Hash Tables](../01_linear_structures/04_hash_tables.md), [Priority Queues](../01_linear_structures/03_queues_deques_and_priority_queues.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Two Pointers & Sliding Window](../04_algorithmic_paradigms/07_two_pointers_sliding_window_prefix_difference.md).