# Trường hợp (case / 사례) Study: Streaming Analytics với dữ liệu lớn

> **Mạch đọc:** Đọc **trường hợp (case / 사례) Study: Streaming Analytics với dữ liệu lớn** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Những truy vấn điển hình** sang **2. chính xác (exact / 정확한) trạng thái (state / 상태) bằng băm (hash / 해시) Map**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

**Streaming Analytics trường hợp (case / 사례) Study / 스트리밍 분석 사례**

Streaming analytics xử lý chuỗi sự kiện đến liên tục thay vì một tập dữ liệu tĩnh đã biết trước. Ví dụ: log hệ thống, clickstream, giao dịch, packet mạng, chỉ số (metric / 지표) khả năng quan sát (observability / 관측 가능성) hoặc sự kiện IoT.

Khó khăn cốt lõi là:

```text
dòng dữ liệu có thể không kết thúc
không thể giữ mọi sự kiện trong RAM
cần kết quả gần thời gian thực
có thể chấp nhận xấp xỉ cho một số truy vấn
state phải gộp được giữa nhiều worker
```

Trường hợp (case / 사례) study này nối bảng băm (hash table / 해시 테이블), vùng nhớ động (heap / 힙), Count-Min Sketch, HyperLogLog, Reservoir Sampling, Sliding cửa sổ (window / 윈도우) và phân tán (distributed / 분산) merge thành một chuỗi xử lý (pipeline / 파이프라인) thực tế.

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

## 2. chính xác (exact / 정확한) trạng thái (state / 상태) bằng băm (hash / 해시) Map

Baseline cho tần suất:

```text
key -> count
```

Băm (hash / 해시) Map cho cập nhật (update / 업데이트) kỳ vọng `O(1)`.

Nhưng nếu cardinality của key lên hàng trăm triệu, bộ nhớ (memory / 메모리) tăng tuyến tính theo số key phân biệt. Đây là điểm hệ thống phải quyết định:

```text
state chính xác còn vừa bộ nhớ không?
```

Nếu không, cần approximation hoặc partitioning.

## 3. Top-K với băm (hash / 해시) Map + vùng nhớ động (heap / 힙)

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

Nếu cần Top-K liên tục sau mỗi sự kiện (event / 이벤트), cập nhật vùng nhớ động (heap / 힙) trực tiếp phức tạp hơn vì priority thay đổi. Có thể dùng indexed vùng nhớ động (heap / 힙) hoặc lazy entries.

## 4. Count-Min Sketch khi không thể giữ mọi key

CMS giữ ma trận bộ đếm nhỏ và nhiều hàm băm. Mỗi sự kiện (event / 이벤트) cập nhật một ô ở mỗi hàng.

Ước lượng:

```text
estimate(key) = min(counters corresponding to key)
```

Trong mô hình cập nhật không âm, CMS không đánh giá thấp số đếm thật; va chạm chỉ làm tăng ước lượng.

Bộ nhớ (memory / 메모리) phụ thuộc `ε`, `δ`, không phụ thuộc trực tiếp số key phân biệt.

Đây là lý do CMS phù hợp telemetry có keyspace rất lớn.

## 5. CMS không tự tìm được key nổi bật

Sketch biết “key X khoảng bao nhiêu” nếu ta hỏi X, nhưng không lưu danh sách tất cả key.

Muốn heavy hitters cần thêm candidate set:

```text
CMS + heap/set ứng viên
```

hoặc dùng thuật toán như Misra–Gries/Space-Saving.

Đây là ví dụ quan trọng:

> truy vấn (query / 쿼리) by known key và discovery of unknown key là hai loại bài toán khác nhau.

## 6. Space-Saving cho heavy hitters

Space-Saving giữ một số lượng counter hữu hạn cho các candidate lớn.

Khi key mới không có counter và mọi slot đã dùng, nó thay candidate có count nhỏ nhất rồi cập nhật sai số tương ứng.

Với phân phối (distribution / 분포) lệch mạnh kiểu Zipf, nó có thể theo dõi heavy hitters rất hiệu quả.

Một chuỗi xử lý (pipeline / 파이프라인) thực tế có thể dùng:

```text
Space-Saving -> candidate discovery
exact backend -> verify candidate
```

## 7. HyperLogLog cho distinct count

Muốn đếm số người dùng (user / 사용자) phân biệt chính xác cần băm (hash / 해시) Set:

```text
user_id -> membership
```

Bộ nhớ (memory / 메모리) tăng theo cardinality.

HyperLogLog giữ thống kê trên băm (hash / 해시) và dùng rất ít bộ nhớ (memory / 메모리) so với băm (hash / 해시) Set.

Các worker có thể merge HLL bằng phép `max` theo từng register, nên rất phù hợp phân tán (distributed / 분산) aggregation.

## 8. Mergeability là tính chất hệ thống quan trọng

Trong phân tán (distributed / 분산) stream processing, mỗi partition xử lý một phần dữ liệu:

```text
partition 1 -> sketch A
partition 2 -> sketch B
partition 3 -> sketch C
```

Nếu sketch có phép merge kết hợp:

```text
merge(merge(A,B),C) = merge(A,merge(B,C))
```

coordinator có thể dùng cây (tree / 트리) reduction song song.

Đây là lý do HLL/CMS/bottom-k hấp dẫn hơn nhiều cấu trúc chính xác (exact / 정확한) không dễ merge ở quy mô lớn.

## 9. thời gian (time / 시간) cửa sổ (window / 윈도우) làm trạng thái (state / 상태) khó hơn

“Distinct count từ đầu hệ thống” dễ hơn “distinct count 5 phút gần nhất”.

Nếu sketch chỉ tăng đơn điệu, nó không tự quên sự kiện (event / 이벤트) cũ.

Các cách phổ biến:

```text
bucket theo thời gian
ring of sketches
exponential histogram
sliding-window sketch chuyên dụng
```

Ví dụ giữ 60 HLL cho 60 phút gần nhất rồi merge các bucket cần thiết.

Đổi lại, ranh giới (boundary / 경계) của cửa sổ (window / 윈도우) và bộ nhớ (memory / 메모리) tăng theo số bucket.

## 10. Tumbling, Sliding và Session cửa sổ (window / 윈도우)

**Tumbling cửa sổ (window / 윈도우)** chia thời gian thành các đoạn không chồng lấp.

**Sliding cửa sổ (window / 윈도우)** có thể chồng lấp và cập nhật thường xuyên.

**Session cửa sổ (window / 윈도우)** kết thúc khi người dùng (user / 사용자) không hoạt động trong một khoảng hết thời gian chờ (timeout / 타임아웃).

Session cửa sổ (window / 윈도우) cần trạng thái (state / 상태) theo key và hết thời gian chờ (timeout / 타임아웃) management; thường dùng timer hàng đợi (queue / 큐)/vùng nhớ động (heap / 힙) hoặc timer wheel.

Cùng gọi là “cửa sổ (window / 윈도우)”, nhưng máy trạng thái (state machine / 상태 머신) rất khác nhau.

## 11. sự kiện (event / 이벤트) thời gian (time / 시간) và Processing thời gian (time / 시간)

Streaming thực có sự kiện (event / 이벤트) đến trễ hoặc ngoài thứ tự.

```text
event time      -> thời gian sự kiện thực xảy ra
processing time -> thời gian hệ thống xử lý
```

Nếu dùng sự kiện (event / 이벤트) thời gian (time / 시간), phải quyết định chờ bao lâu cho sự kiện (event / 이벤트) trễ. Watermark là một cách biểu diễn tiến độ thời gian lô-gic (logic / 논리).

Đây không còn là DSA thuần nhưng trạng thái (state / 상태)/cửa sổ (window / 윈도우) cấu trúc (structure / 구조) phải phù hợp ngữ nghĩa (semantics / 의미론) thời gian.

## 12. Reservoir Sampling

Nếu muốn giữ một mẫu đại diện `k` sự kiện (event / 이벤트) từ stream chưa biết trước độ dài, Reservoir Sampling dùng bộ nhớ `O(k)`.

Nó tránh thiên lệch về sự kiện (event / 이벤트) đầu hoặc cuối và rất hữu ích cho gỡ lỗi (debug / 디버그), inspection hoặc offline phân tích (analysis / 분석).

Sampling là cách giảm dữ liệu trong khi cố giữ phân phối đại diện.

## 13. Quantile Sketch

Độ trễ (latency / 지연 시간) percentile không thể tính chỉ bằng average. Muốn p99 chính xác có thể cần giữ/sort lượng dữ liệu lớn.

Các sketch quantile như KLL/t-digest (tùy domain) nén phân phối để ước lượng percentile với bộ nhớ giới hạn.

Điểm cần hiểu là:

```text
mean -> aggregate đơn giản
quantile -> cần thông tin về distribution
```

Do đó trạng thái (state / 상태) phức tạp hơn một counter.

## 14. Histogram

Một histogram cố định chia miền giá trị thành bucket:

```text
0–10 ms
10–50 ms
50–100 ms
...
```

Bộ nhớ (memory / 메모리) nhỏ và merge rất dễ, nhưng precision phụ thuộc ranh giới (boundary / 경계).

Nếu phân phối (distribution / 분포) thay đổi mạnh, bucket cố định có thể mất chi tiết ở vùng quan trọng.

Đây là sự đánh đổi (trade-off / 트레이드오프) giữa simplicity, mergeability và precision.

## 15. Approximate vs chính xác (exact / 정확한) chuỗi xử lý (pipeline / 파이프라인)

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

Approximation giúp giảm tìm kiếm (search / 검색) không gian (space / 공간), không nhất thiết thay thế kết quả chính xác cuối cùng.

## 16. Partitioning theo key

Để trạng thái (state / 상태) cùng key nằm một worker, hệ thống có thể dùng:

```text
partition = hash(key) mod N
```

Hashing cân bằng tương đối nhưng khi số partition thay đổi sẽ remap nhiều key. Consistent/rendezvous hashing có thể giảm lượng trạng thái (state / 상태) di chuyển trong một số kiến trúc.

Stateful streaming vì vậy nối trực tiếp với hashing phân tán.

## 17. Hot Key

Nếu một key chiếm 30% lưu lượng, băm (hash / 해시) partitioning vẫn không cân bằng vì toàn bộ key đó đi cùng một worker.

Các chiến lược gồm:

```text
salting key
local partial aggregation
hierarchical combine
special-case hot keys
```

Ví dụ split `celebrity_user` thành nhiều subkey rồi merge count ở tầng sau.

Đây là vấn đề phân phối (distribution / 분포), không phải lỗi của băm (hash / 해시) hàm (function / 함수).

## 18. Backpressure

Nếu downstream xử lý chậm hơn upstream, hàng đợi (queue / 큐) tăng mãi.

Cần chính sách:

```text
block producer
drop samples
spill to disk
scale consumers
reduce fidelity
```

Hàng đợi (queue / 큐) sức chứa (capacity / 용량) là một phần của độ tin cậy (reliability / 신뢰성) đặc tả hợp đồng (contract / 계약).

Streaming analytics vì vậy kết nối trực tiếp với scheduler/backpressure, không chỉ sketch.

## 19. Exactly-once, At-least-once và duplicate

Nếu sự kiện (event / 이벤트) có thể được xử lý lại sau thử lại (retry / 재시도), counter đơn giản có thể đếm trùng.

Cần xác định ngữ nghĩa (semantics / 의미론):

```text
at-most-once
at-least-once
exactly-once theo phạm vi hệ thống
```

Dedup có thể cần sự kiện (event / 이벤트) ID + băm (hash / 해시) Set/TTL chỉ mục (index / 인덱스), nhưng trạng thái (state / 상태) dedup cũng tốn bộ nhớ (memory / 메모리).

Approximate duplicate filters như Bloom Filter có thể tạo false positive, vì vậy không phải lĩnh vực (domain / 도메인) nào cũng chấp nhận được.

## 20. Snapshot và khôi phục (recovery / 복구)

Trạng thái (state / 상태) phải được checkpoint:

```text
Hash Map state
sketch registers
window buckets
timers
```

Nếu snapshot không nhất quán với đầu vào (input / 입력) offset, khôi phục (recovery / 복구) có thể mất hoặc đếm lại sự kiện (event / 이벤트).

Một cấu trúc đúng trong RAM chưa đủ; phân tán (distributed / 분산) trạng thái (state / 상태) cần giao thức (protocol / 프로토콜) persistence tương ứng.

## 21. Monitoring chính sketch

Approximate cấu trúc (structure / 구조) cũng cần khả năng quan sát (observability / 관측 가능성):

```text
Bloom saturation
CMS collision/error trend
HLL version/precision
counter overflow
merge compatibility
bucket age
```

Nếu dữ liệu tăng gấp 100 lần so với giả định (assumption / 가정) ban đầu, lỗi (error / 오류) guarantee có thể không còn phù hợp.

## 22. Testing

Dùng chính xác (exact / 정확한) mô hình (model / 모델) trên dữ liệu nhỏ để đối chiếu:

```text
Hash Map exact counts
Hash Set exact cardinality
full sorted values cho percentile
```

Với sketch, kiểm tra phân phối (distribution / 분포) sai số qua nhiều seed/dataset thay vì một lần chạy.

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

Không nên chỉ đo CPU thông lượng (throughput / 처리량) mà bỏ qua trạng thái (state / 상태) growth và khôi phục (recovery / 복구) chi phí (cost / 비용).

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

> Streaming analytics là bài toán **quản lý trạng thái (state / 상태) dưới giới hạn tài nguyên**. chính xác (exact / 정확한) cấu trúc (structure / 구조) giữ chi tiết nhưng trạng thái (state / 상태) tăng theo dữ liệu; sketch chủ động nén thông tin và đổi lại sai số có kiểm soát. cửa sổ (window / 윈도우) thêm chiều thời gian, partitioning thêm chiều phân tán, còn backpressure quyết định hệ thống phản ứng thế nào khi tốc độ đến vượt khả năng xử lý.

Xem thêm: [Hash Tables](../01_linear_structures/04_hash_tables.md), [Priority Queues](../01_linear_structures/03_queues_deques_and_priority_queues.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Two Pointers & Sliding Window](../04_algorithmic_paradigms/07_two_pointers_sliding_window_prefix_difference.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 choose the right data structure](./00_choose_the_right_data_structure.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
