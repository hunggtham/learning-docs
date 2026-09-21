# Cấu trúc dữ liệu xác suất cho dữ liệu lớn
**Probabilistic Data Structures / 확률적 자료구조**

Khi dữ liệu quá lớn để lưu chính xác từng phần tử, yêu cầu thực tế đôi khi cũng không cần câu trả lời tuyệt đối chính xác. Nếu hệ thống chấp nhận một **mô hình sai số (error model)** rõ ràng, ta có thể đánh đổi một phần độ chính xác để lấy bộ nhớ nhỏ hơn rất nhiều, throughput cao hơn và khả năng gộp dữ liệu giữa nhiều node tốt hơn.

Cấu trúc dữ liệu xác suất không phải “bản kém chính xác” của cấu trúc thông thường. Một thiết kế tốt phải nói rõ:

```text
truy vấn nào được hỗ trợ
loại sai số nào có thể xảy ra
loại sai số nào được bảo đảm không xảy ra
xác suất hoặc biên độ sai số phụ thuộc tham số nào
có hỗ trợ merge không
có hỗ trợ delete/update không
hash/randomness assumptions là gì
```

Mô hình tư duy trung tâm:

> Cấu trúc xác suất chủ động nén nhiều lịch sử dữ liệu khác nhau vào cùng một trạng thái tóm lược, rồi mô tả định lượng lượng thông tin bị mất.

## Khi nào approximation đáng giá?

Các workload điển hình:

```text
membership prefilter trước disk/database lookup
ước lượng số user distinct
frequency estimation trong event stream
heavy-hitter detection
sampling stream dài không biết trước độ dài
telemetry và network analytics
phân tán aggregation giữa nhiều machine
```

Nếu kết quả quyết định trực tiếp kế toán, authorization hoặc giao dịch tài chính, approximation có thể không phù hợp.

**Error budget phải đi từ business requirement xuống cấu trúc dữ liệu, không phải ngược lại.**

## Ba loại guarantee cần phân biệt

Một cấu trúc xác suất có thể có:

```text
one-sided error   -> chỉ sai theo một hướng
bounded additive error
bounded relative error
probability of failure δ
expected error
high-probability guarantee
```

Hai cấu trúc cùng “sai số 1%” có thể mang nghĩa hoàn toàn khác nhau.

Ví dụ Bloom Filter có one-sided membership error. HyperLogLog ước lượng cardinality với sai số tương đối thống kê. Count-Min Sketch cho additive over-estimation trong mô hình chuẩn.

## Bloom Filter

Bloom Filter trả lời gần đúng câu hỏi membership.

Nó dùng:

```text
m bit
k hash positions cho mỗi key
```

Insert:

```text
set tất cả k bit thành 1
```

Query:

```text
nếu có bit bằng 0 -> chắc chắn không có
nếu tất cả bằng 1 -> có thể có
```

Trong mô hình chuẩn chỉ chèn, Bloom Filter có **false positive** nhưng không có **false negative**.

## Xác suất false positive

Sau `n` phần tử, có khoảng `kn` lần đặt bit.

Xác suất một bit vẫn là 0:

\[
\left(1-\frac1m\right)^{kn}\approx e^{-kn/m}
\]

Xác suất bit là 1:

\[
1-e^{-kn/m}
\]

Một key chưa chèn bị false positive khi cả `k` vị trí đều đã 1:

\[
p\approx\left(1-e^{-kn/m}\right)^k
\]

Điều này cho thấy Bloom Filter không có một “accuracy cố định” độc lập số phần tử. Khi `n` tăng mà `m` không đổi, filter dần bão hòa.

## Chọn k và m

Với `m,n` cố định, số hash gần tối ưu:

\[
k\approx\frac mn\ln2
\]

Nếu muốn false-positive rate `p`, số bit xấp xỉ:

\[
m\approx-\frac{n\ln p}{(\ln2)^2}
\]

Số bit trên mỗi phần tử:

\[
\frac mn\approx-\frac{\ln p}{(\ln2)^2}
\]

Điều cần hiểu là Bloom Filter phải được sizing từ:

```text
expected cardinality
false-positive target
memory budget
CPU/hash budget
```

## Double hashing để sinh nhiều vị trí

Thực tế không nhất thiết tính `k` hash hoàn toàn độc lập và đắt tiền. Có thể dùng hai hash cơ sở rồi sinh:

\[
h_i(x)=h_1(x)+i\cdot h_2(x)
\]

modulo kích thước bảng dưới một construction phù hợp.

Mục tiêu là giảm CPU cost trong khi vẫn có phân bố đủ tốt cho guarantee thực tế.

## Bloom Filter chỉ là prefilter

Bloom Filter không lưu key nên không thể liệt kê lại tập phần tử.

Pipeline điển hình:

```text
query key
  ↓
Bloom Filter
  ↓ chắc chắn không có -> tránh I/O
  ↓ có thể có
exact index / database / SSTable
```

False positive chỉ làm phát sinh thêm một exact lookup. Không có false negative giúp ta không bỏ sót entry thật.

Đây là lý do Bloom Filter đặc biệt phù hợp làm tầng lọc trước storage đắt.

## Counting Bloom Filter

Bloom Filter chuẩn khó delete vì một bit có thể thuộc nhiều key.

Counting Bloom Filter thay bit bằng counter nhỏ:

```text
insert -> increment
remove -> decrement
```

Delete chỉ an toàn nếu application biết chính xác key thật sự tồn tại. Nếu decrement nhầm, counter có thể xuống 0 dù key khác vẫn dựa trên vị trí đó, tạo false negative.

Counter còn làm memory tăng và cần xử lý saturation/overflow.

## Scalable Bloom Filter

Nếu stream tăng không biết trước, filter cố định sẽ bão hòa.

Một hướng là thêm filter mới khi filter hiện tại đạt ngưỡng tải. Query kiểm tra qua các lớp.

Điều này cho phép capacity tăng dần nhưng:

```text
query cost tăng theo số layer
error budget phải phân bổ giữa layers
memory tăng theo thời gian
```

Không nên gọi mọi biến thể là “Bloom Filter” rồi giả định cùng một guarantee.

## Stable Bloom Filter

Với stream không giới hạn nhưng chỉ muốn membership gần đây, có thể chủ động làm “quên” thông tin cũ.

Stable Bloom Filter duy trì kích thước bounded bằng cách giảm/xóa một số counter/bit theo policy.

Đổi lại, false negative có thể xuất hiện cho dữ liệu cũ.

Đây là ví dụ error model thay đổi trực tiếp khi thêm yêu cầu bounded-memory trên stream vô hạn.

## Cuckoo Filter

Cuckoo Filter lưu fingerprint ngắn thay vì chỉ bit.

Mỗi fingerprint có một vài bucket khả dĩ. Insert có thể di chuyển fingerprint hiện tại giống Cuckoo Hashing.

Ưu điểm thường thấy:

```text
membership nhanh
delete tự nhiên hơn Bloom Filter
memory cạnh tranh tốt ở một số false-positive target
```

Nhược điểm:

```text
build/insert phức tạp hơn
có thể cần relocation chain
capacity/load factor có giới hạn thực tế
```

False positive xảy ra do fingerprint collision.

## XOR Filter

XOR Filter thường phù hợp với **tập tĩnh**: xây structure một lần rồi query nhiều lần.

Nó có thể rất gọn và query nhanh, nhưng update động không tự nhiên như Bloom/Cuckoo Filter.

Bài học:

> Static workload và dynamic workload dẫn tới cấu trúc xác suất khác nhau.

## Count-Min Sketch

Count-Min Sketch ước lượng frequency.

Có `d` hàng, mỗi hàng rộng `w`, mỗi hàng dùng hash riêng.

Update key `x` thêm `c`:

```text
counter[r][h_r(x)] += c
```

Query:

```text
estimate(x) = min(counter[r][h_r(x)])
```

Trong mô hình update không âm, collision chỉ cộng noise dương, nên estimate không nhỏ hơn count thật.

## Vì sao lấy minimum?

Mỗi hàng có thể xem như:

\[
estimate_r(x)=trueCount(x)+noise_r
\]

với `noise_r>=0`.

Lấy minimum chọn hàng ít bị collision noise nhất.

Lấy average sẽ cộng ảnh hưởng của các hàng nhiễu nhiều hơn và không giữ one-sided interpretation tương tự.

## Tham số ε và δ

Một dạng guarantee kinh điển:

```text
width  O(1/ε)
depth  O(log(1/δ))
```

để với xác suất cao:

\[
estimate(x)\le trueCount(x)+\varepsilon N
\]

trong đó `N` là tổng mass update trong mô hình chuẩn.

Trực giác:

```text
width lớn -> ít collision hơn -> giảm độ lớn error
depth lớn -> có nhiều cơ hội có ít nhất một hàng sạch -> tăng confidence
```

## Conservative update

Thay vì tăng tất cả counter, một biến thể chỉ tăng những counter đang bằng estimate tối thiểu.

Mục tiêu là tránh đẩy những counter đã bị noise cao lên thêm nữa.

Thực tế có thể giảm over-estimation, nhưng phải phân biệt guarantee của biến thể với theorem của CMS chuẩn.

## CMS không tự tìm ra heavy hitter identity

CMS trả frequency estimate khi đã biết key.

Nếu muốn hỏi:

> “Key nào xuất hiện nhiều nhất?”

thì cần thêm candidate structure, ví dụ heap/set hoặc thuật toán heavy-hitter chuyên dụng như Misra–Gries/Space-Saving.

Một sketch không lưu identity đầy đủ nên không thể tự “sinh ra” mọi key đã thấy.

## Misra–Gries

Misra–Gries giữ tối đa `k-1` candidate counters để tìm frequent items.

Ý tưởng:

```text
nếu key đã có -> tăng counter
nếu còn slot -> thêm key
nếu hết slot và key mới -> giảm mọi counter, xóa counter về 0
```

Nó bảo đảm các item có frequency đủ lớn không bị bỏ mất khỏi candidate set theo threshold tương ứng.

Đây là một cách khác CMS: thay vì estimate mọi key đã biết, nó tập trung giữ identity của một tập candidate nhỏ.

## Space-Saving

Space-Saving là một heavy-hitter algorithm khác, thường giữ `k` counters và khi key mới không có slot, thay thế item có count nhỏ nhất.

Nó phù hợp stream analytics khi mục tiêu chính là top frequent items.

Điểm quan trọng là chọn structure theo loại query:

```text
point frequency query -> CMS
heavy hitter identity -> Misra–Gries / Space-Saving / hybrid
```

## Update âm và turnstile model

CMS guarantee chuẩn thường giả định non-negative updates.

Nếu stream cho phép increment và decrement, phải xác định model:

```text
strict turnstile  -> frequency thực luôn không âm
general turnstile -> intermediate/final value có thể âm
```

Một theorem cho insertion-only stream không thể áp dụng nguyên trạng cho general turnstile.

**Error guarantee luôn gắn với update model.**

## HyperLogLog

HyperLogLog ước lượng **số phần tử phân biệt (cardinality)**.

Ý tưởng nền tảng: nếu hash bit giống random, việc nhìn thấy một hash có nhiều zero liên tiếp ở đầu là sự kiện hiếm. Mức cực đại của “độ hiếm” này chứa thông tin về số distinct items đã quan sát.

HLL chia hash space thành nhiều register để giảm variance thay vì chỉ giữ một maximum toàn cục.

## Register của HLL

Một phần hash chọn register. Phần còn lại xác định `rho`, thường là vị trí bit 1 đầu tiên hoặc số leading zeros theo convention.

Register lưu maximum `rho` từng thấy.

Nếu stream có nhiều distinct values, khả năng quan sát các pattern hiếm hơn tăng, làm register lớn hơn.

Final estimator kết hợp nhiều register qua một dạng harmonic mean có correction constants.

## Vì sao cần nhiều register?

Chỉ một maximum có variance rất lớn: một hash cực hiếm có thể làm estimate nhảy mạnh.

Chia dữ liệu vào nhiều bucket độc lập gần đúng rồi aggregate giúp giảm variance.

Số register `m` lớn hơn thường làm relative standard error giảm cỡ:

\[
O(1/\sqrt m)
\]

Trong HLL kinh điển, hằng số thường được nhắc khoảng `1.04/√m` dưới mô hình lý tưởng.

Điều cần nhớ: tăng memory theo số register để giảm error theo căn bậc hai.

## Small-range và large-range correction

Estimator thuần có bias ở một số miền cardinality.

Implementation HLL thực tế thường dùng correction cho:

```text
cardinality nhỏ -> nhiều register còn 0
cardinality rất lớn -> hash space saturation effects
```

Do đó không nên tự implement HLL production chỉ từ một công thức rút gọn nếu accuracy quan trọng.

## Mergeability của HLL

Nếu hai HLL dùng cùng parameters/hash scheme, có thể merge register-wise bằng maximum:

```text
R_merged[i] = max(R_a[i], R_b[i])
```

Đây là lý do HLL rất phù hợp distributed analytics.

Ta có thể tính sketch trên nhiều shard rồi merge mà không gửi raw IDs.

**Mergeability là một feature hệ thống cực kỳ quan trọng của probabilistic summary.**

## MinHash

MinHash ước lượng **Jaccard similarity** giữa hai tập:

\[
J(A,B)=\frac{|A\cap B|}{|A\cup B|}
\]

Với một hash/permutation ngẫu nhiên phù hợp, xác suất phần tử có hash nhỏ nhất của hai tập giống nhau bằng Jaccard similarity.

Lặp nhiều hash/signature components tạo estimator ổn định hơn.

Ứng dụng:

```text
near-duplicate documents
similar sets
recommendation candidate generation
web-page deduplication
```

## MinHash và LSH

MinHash signature có thể được dùng cùng **Locality-Sensitive Hashing (LSH)** để tìm candidate pair tương tự mà không so mọi cặp.

LSH không “tính similarity chính xác”; nó tăng xác suất các object giống nhau rơi vào cùng bucket.

Pipeline:

```text
raw sets
  ↓
MinHash signatures
  ↓
LSH candidate buckets
  ↓
exact/expensive similarity trên candidate
```

Đây là cùng triết lý với Bloom Filter: approximation dùng để giảm không gian candidate trước bước chính xác đắt hơn.

## Reservoir Sampling

Nếu stream dài không biết trước và muốn sample `k` phần tử đồng đều, không thể giữ toàn bộ rồi random sau.

Reservoir Sampling giữ `k` item đầu, sau đó với item thứ `i` chọn nó với xác suất phù hợp và nếu được chọn thì thay một vị trí ngẫu nhiên trong reservoir.

Với `k=1`, item thứ `i` được chọn với xác suất `1/i`.

## Vì sao Reservoir Sampling đồng đều?

Xét một item ở vị trí `j`.

Khi item `j` được xử lý, xác suất vào reservoir kích thước `k` là:

\[
\frac{k}{j}
\]

Sau đó ở mỗi bước `i>j`, xác suất nó không bị thay thế là:

\[
1-\frac1i
\]

Tích các xác suất sống sót tới cuối tạo xác suất cuối cùng:

\[
\frac{k}{n}
\]

cho mọi item.

Đây là ví dụ đẹp của induction/probability proof cho streaming algorithm.

## Weighted Reservoir Sampling

Nếu item có trọng số và không muốn sample uniform, có các biến thể weighted sampling.

Điểm cần xác định trước:

```text
sample probability tỷ lệ trọng số?
with replacement hay without replacement?
trọng số có thay đổi theo thời gian không?
```

Sampling semantics phải là một phần specification.

## Quantile sketch

Một lớp cấu trúc khác ước lượng median/percentile/quantile trên stream.

Thay vì lưu mọi giá trị rồi sort, sketch giữ summary nhỏ hơn.

Ứng dụng:

```text
p50/p95/p99 latency
telemetry
monitoring
large-scale analytics
```

Các sketch khác nhau có error model khác nhau, ví dụ rank error hoặc relative error ở tail. Khi chọn library, phải đọc guarantee cụ thể chứ không chỉ tên “quantile sketch”.

## Tại sao p99 cần sketch chuyên biệt?

Mean latency có thể nhỏ trong khi tail rất xấu. Muốn theo dõi p99 trên hàng tỷ request mà không lưu toàn bộ sample, exact sorting không thực tế.

Một quantile sketch đổi một lượng error có kiểm soát lấy memory bounded.

Đây là ví dụ product requirement trực tiếp dẫn tới approximate structure.

## Mergeability là dimension thiết kế riêng

Trong distributed system, có hai cách:

```text
ship raw data về một nơi rồi tính
hoặc
compute summary tại shard rồi merge summaries
```

Nếu sketch merge được, network cost giảm cực mạnh.

Các cấu trúc như HLL và nhiều frequency/quantile sketch được thiết kế với merge operation rõ ràng.

Một summary nhỏ nhưng không merge được có thể kém hữu ích trong distributed pipeline.

## Monoid perspective của sketch merge

Nếu summary có merge associative và identity:

```text
merge(merge(A,B),C) = merge(A,merge(B,C))
```

thì ta có thể aggregate theo tree, shard hoặc batch bất kỳ.

Đây là lý do các sketch merge-friendly rất hợp MapReduce/stream processing.

Algebraic properties không chỉ là lý thuyết; chúng quyết định khả năng scale hệ thống.

## Hash independence assumptions

Nhiều proof giả định hash function có mức independence hoặc uniformity nhất định.

Hash implementation thực tế chỉ xấp xỉ mô hình lý tưởng.

Nếu key có pattern xấu, attacker-controlled input hoặc hash quality kém, error thực tế có thể lệch khỏi model.

Vì vậy production sketch nên dùng hash function/library đã được đánh giá phù hợp thay vì tự nghĩ một mixing function đơn giản.

## Adversarial input

Một cấu trúc xác suất được chứng minh dưới random-hash assumption có thể không an toàn trước attacker biết seed hoặc điều khiển key.

Threat model cần hỏi:

```text
attacker có biết hash seed không?
attacker có quan sát output để adapt input không?
sai số chỉ ảnh hưởng analytics hay ảnh hưởng security decision?
```

Một sketch phù hợp telemetry nội bộ chưa chắc phù hợp access control.

## Deletion không phải feature miễn phí

Bloom Filter chuẩn không delete an toàn. CMS với decrement thay đổi update model. HLL không thể “trừ” một distinct item đơn giản vì register chỉ giữ maxima.

Muốn delete có thể cần:

```text
counting variant
windowed/time-decay structure
rebuild định kỳ
partition theo epoch
exact side structure
```

Một summary nén mạnh thường mất thông tin cần để đảo ngược update.

## Sliding window và time decay

Streaming system thường quan tâm “5 phút gần nhất”, không phải toàn bộ lịch sử.

Có thể dùng:

```text
epoch buckets
ring of sketches
exponential decay
window-specific algorithms
```

Ví dụ giữ HLL theo từng minute rồi merge vài bucket gần nhất. Trade-off là boundary error và memory tăng theo số epoch.

Time semantics là một dimension khác ngoài value semantics.

## Cardinality của union và intersection

HLL merge rất tự nhiên cho union.

Intersection không trực tiếp bằng register-wise operation tương tự. Có thể dùng inclusion–exclusion từ estimates:

\[
|A\cap B|=|A|+|B|-|A\cup B|
\]

nhưng error của nhiều estimate cộng/trừ có thể làm kết quả kém ổn định, đặc biệt khi intersection nhỏ.

MinHash thường phù hợp hơn nếu mục tiêu chính là similarity/intersection ratio.

Chọn sketch theo query, không chỉ theo loại dữ liệu.

## Error propagation

Nếu một pipeline dùng nhiều approximate stages, error có thể tích lũy hoặc tương tác.

Ví dụ:

```text
approx frequency -> chọn candidate -> approx cardinality
```

Không nên giả định mỗi stage “1% error” nghĩa toàn pipeline vẫn “1%”.

Cần hiểu error direction, independence và cách downstream operation khuếch đại sai số.

## Memory budget trước, error sau — hay ngược lại?

Có hai cách thiết kế:

```text
business cho error target -> tính memory cần
hệ thống cho memory budget -> tính error đạt được
```

Ví dụ Bloom Filter cho phép chuyển giữa `n`, `p`, `m` tương đối trực tiếp.

Việc ghi rõ phương trình sizing biến design từ “chọn đại 10 MB” thành một quyết định có thể review.

## Serialization và compatibility

Sketch thường được lưu hoặc truyền qua network. Format phải chứa đủ metadata:

```text
version
hash seed/scheme
number of registers/counters
precision parameters
endianness nếu liên quan
```

Hai HLL khác precision hoặc hash scheme không thể merge tùy tiện.

Versioning của sketch format là một phần của distributed correctness.

## Determinism và reproducibility

Randomized structure có thể cần seed cố định cho test/reproducibility.

Nhưng production security có thể lại cần seed bí mật/ngẫu nhiên.

Không có seed policy duy nhất đúng. Nó phụ thuộc mục tiêu:

```text
test repeatability
cross-node merge compatibility
adversarial resistance
```

## Concurrency

Counter array hoặc register updates từ nhiều thread có thể race.

Tùy structure, có thể dùng:

```text
thread-local sketch rồi merge
atomic counters
sharded sketch
lock quanh batch update
```

Thread-local + merge thường hấp dẫn nếu merge operation rẻ và associative.

Đây là một ví dụ algebraic merge giúp thiết kế concurrent architecture đơn giản hơn.

## Cache locality

Sketch thường dùng array nhỏ và contiguous, nên có locality tốt hơn Hash Map lưu hàng triệu key.

Một trong những lý do sketch nhanh không chỉ là ít operation về lý thuyết mà còn vì working set nhỏ hơn và vừa cache hơn.

Approximation đôi khi mua cả memory lẫn CPU efficiency qua cache.

## Không phải approximation nào cũng probabilistic

Có deterministic approximate algorithms. Ngược lại, randomized algorithm có thể luôn exact.

Do đó phải tách:

```text
randomness source
output accuracy
runtime randomness
probability of failure
```

Không nên dùng “probabilistic” như một từ thay thế chung cho “không chính xác”.

## Chọn cấu trúc theo câu hỏi

| Câu hỏi | Cấu trúc thường đáng cân nhắc |
|---|---|
| Key có thể đã tồn tại? | Bloom/Cuckoo/XOR Filter |
| Frequency của key đã biết? | Count-Min Sketch |
| Heavy hitters là ai? | Misra–Gries / Space-Saving / CMS + candidates |
| Bao nhiêu giá trị distinct? | HyperLogLog |
| Hai tập giống nhau bao nhiêu? | MinHash |
| Lấy mẫu stream đều | Reservoir Sampling |
| Percentile/quantile | Quantile sketch phù hợp |

Bảng này chỉ là điểm khởi đầu; update/delete/merge/error model mới quyết định cuối cùng.

## Kiểm thử cấu trúc xác suất

Testing phải kiểm tra cả correctness logic lẫn statistical behavior.

Bloom Filter:

```text
mọi key đã insert phải query true trong mô hình chuẩn
đo false-positive rate trên tập key độc lập lớn
```

CMS:

```text
estimate không thấp hơn true count trong insertion-only model
đo error distribution trên workload khác nhau
```

HLL:

```text
chạy nhiều trial với cardinality đã biết
đo relative error distribution
```

Không nên kiểm thử probability bằng 10 sample rồi kết luận guarantee đúng.

## Differential và simulation testing

Có thể so sketch với exact structure trên dataset nhỏ/vừa:

```text
HashSet -> exact cardinality
HashMap -> exact frequency
full list -> exact sample distribution
```

Sau đó chạy nhiều seed/workload để quan sát bias, variance và tail error.

Đây là cách nối theory với implementation thực tế.

## Những hiểu lầm phổ biến

“Bloom Filter nói true nghĩa key tồn tại” — sai; chỉ là “có thể tồn tại”.

“Bloom Filter delete một key bằng cách clear các bit của nó” — có thể tạo false negative cho key khác.

“CMS biết heavy hitter là ai” — nó chỉ estimate key được hỏi, trừ khi ghép candidate mechanism.

“HLL có thể xóa một user khỏi cardinality bằng cách undo hash” — không đơn giản vì register giữ max history.

“Sketch nhỏ thì accuracy cố định” — error phụ thuộc parameters và workload size.

“Expected/statistical guarantee vẫn đúng với mọi adversarial hash input” — không nếu assumptions bị phá.

“Merge hai sketch cùng loại luôn hợp lệ” — sai nếu precision/hash/version khác nhau.

## Mô hình tư duy

> Probabilistic data structure là một **hợp đồng nén thông tin**. Ta chủ động bỏ khả năng phân biệt một số trạng thái để đổi lấy memory/throughput/mergeability, nhưng phải mô tả chính xác cái giá bằng error model.

Khi chọn sketch, hãy hỏi: **truy vấn thật sự là membership, frequency, heavy hitter, cardinality, similarity hay quantile; error được phép theo hướng nào; memory bao nhiêu; update có delete không; cần merge giữa shard không; hash assumptions có phù hợp threat model không; và downstream system sẽ dùng estimate như thế nào?**

Xem tiếp: [Hash Tables](../01_linear_structures/04_hash_tables.md), [Amortized, Randomized & Probabilistic Thinking](./03_amortized_randomized_and_probabilistic_thinking.md), [Mathematical Toolkit](../00_foundations/04_mathematical_toolkit_for_dsa.md), [Bit Manipulation](./02_bit_manipulation_and_bitsets.md) và [DSA in Databases, Networks & Systems](../90_connections/01_dsa_in_databases_networks_and_systems.md).