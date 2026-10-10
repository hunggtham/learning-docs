# Cấu trúc dữ liệu xác suất cho dữ liệu lớn

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Cấu trúc dữ liệu xác suất cho dữ liệu lớn**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Khi nào approximation đáng giá?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Ba loại guarantee cần phân biệt** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối probabilistic data structures với sketch, hash và error bound, để tiết kiệm bộ nhớ mà vẫn định lượng sai số.

**Probabilistic dữ liệu (data / 데이터) Structures / 확률적 자료구조**

Khi dữ liệu quá lớn để lưu chính xác từng phần tử, yêu cầu thực tế đôi khi cũng không cần câu trả lời tuyệt đối chính xác. Nếu hệ thống chấp nhận một **mô hình sai số (error model)** rõ ràng, ta có thể đánh đổi một phần độ chính xác để lấy bộ nhớ nhỏ hơn rất nhiều, thông lượng (throughput / 처리량) cao hơn và khả năng gộp dữ liệu giữa nhiều nút (node / 노드) tốt hơn.

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

Các tải công việc (workload / 워크로드) điển hình:

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

**lỗi (error / 오류) ngân sách (budget / 예산) phải đi từ nghiệp vụ (business / 비즈니스) yêu cầu (requirement / 요구사항) xuống cấu trúc dữ liệu, không phải ngược lại.**

Approximation chỉ đáng giá khi ta nói rõ guarantee nào được giữ và sai số chấp nhận được. Bloom filter là ví dụ đầu tiên: nó đổi bộ nhớ lấy một câu trả lời membership có thể có false positive.

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

Ví dụ Bloom Filter có one-sided membership lỗi (error / 오류). HyperLogLog ước lượng cardinality với sai số tương đối thống kê. Count-Min Sketch cho additive over-estimation trong mô hình chuẩn.

Bloom filter dùng nhiều hash để set bit khi insert; query chỉ có thể phủ định membership khi một bit bị thiếu, không thể khẳng định tuyệt đối khi tất cả đều bật. Xác suất false positive cần được tính từ số bit, số hash và số phần tử.

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

Truy vấn (query / 쿼리):

```text
nếu có bit bằng 0 -> chắc chắn không có
nếu tất cả bằng 1 -> có thể có
```

Trong mô hình chuẩn chỉ chèn, Bloom Filter có **false positive** nhưng không có **false negative**.

False positive xảy ra khi các bit cần kiểm tra đã bị các phần tử khác set, còn false negative không xảy ra nếu không có deletion sai. Từ công thức đó, ta chọn số bit `m` và số hash `k` theo ngân sách bộ nhớ và error target.

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

Tăng `m` giảm va chạm bit, còn `k` quá nhỏ hoặc quá lớn đều làm false-positive rate xấu đi; có một điểm gần tối ưu theo `m/n`. Khi triển khai nhiều vị trí, double hashing tạo các offset từ hai hàm cơ sở mà không cần lưu k hàm độc lập.

## Chọn k và m

Với `m,n` cố định, số băm (hash / 해시) gần tối ưu:

\[
k\approx\frac mn\ln2
\]

Nếu muốn false-positive tỷ lệ (rate / 비율) `p`, số bit xấp xỉ:

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

Double hashing cần hằng số bước không suy biến và phải giữ cùng quy tắc cho insert/query. Dù xác suất được kiểm soát, Bloom filter chỉ là prefilter: hit vẫn cần kiểm tra nguồn dữ liệu chính xác.

## Double hashing để sinh nhiều vị trí

Thực tế không nhất thiết tính `k` băm (hash / 해시) hoàn toàn độc lập và đắt tiền. Có thể dùng hai băm (hash / 해시) cơ sở rồi sinh:

\[
h_i(x)=h_1(x)+i\cdot h_2(x)
\]

modulo kích thước bảng dưới một construction phù hợp.

Mục tiêu là giảm CPU chi phí (cost / 비용) trong khi vẫn có phân bố đủ tốt cho guarantee thực tế.

Prefilter giúp loại nhanh phần lớn miss nhưng không được dùng như bằng chứng cuối cùng, nhất là trong security hoặc billing. Khi cần deletion, counting Bloom filter thay bit bằng counter để theo dõi số lần set.

## Bloom Filter chỉ là prefilter

Bloom Filter không lưu key nên không thể liệt kê lại tập phần tử.

Chuỗi xử lý (pipeline / 파이프라인) điển hình:

```text
query key
  ↓
Bloom Filter
  ↓ chắc chắn không có -> tránh I/O
  ↓ có thể có
exact index / database / SSTable
```

False positive chỉ làm phát sinh thêm một chính xác (exact / 정확한) lookup. Không có false negative giúp ta không bỏ sót entry thật.

Đây là lý do Bloom Filter đặc biệt phù hợp làm tầng lọc trước lưu trữ (storage / 저장소) đắt.

Counting filter cho phép giảm counter khi xóa, nhưng counter có thể overflow và footprint lớn hơn bit filter. Khi số phần tử tăng vượt dự báo, scalable Bloom filter mở thêm các tầng thay vì phá vỡ toàn bộ ngân sách error.

## Counting Bloom Filter

Bloom Filter chuẩn khó delete vì một bit có thể thuộc nhiều key.

Counting Bloom Filter thay bit bằng counter nhỏ:

```text
insert -> increment
remove -> decrement
```

Delete chỉ an toàn nếu ứng dụng (application / 애플리케이션) biết chính xác key thật sự tồn tại. Nếu decrement nhầm, counter có thể xuống 0 dù key khác vẫn dựa trên vị trí đó, tạo false negative.

Counter còn làm bộ nhớ (memory / 메모리) tăng và cần xử lý saturation/overflow.

Scalable Bloom filter thêm filter mới theo growth policy và phối hợp query qua các tầng, nên cần tính error budget tổng. Stable Bloom filter chọn ngẫu nhiên counter để giảm nhằm giữ cửa sổ thông tin gần đây với bộ nhớ cố định.

## Scalable Bloom Filter

Nếu stream tăng không biết trước, filter cố định sẽ bão hòa.

Một hướng là thêm filter mới khi filter hiện tại đạt ngưỡng tải. truy vấn (query / 쿼리) kiểm tra qua các lớp.

Điều này cho phép sức chứa (capacity / 용량) tăng dần nhưng:

```text
query cost tăng theo số layer
error budget phải phân bổ giữa layers
memory tăng theo thời gian
```

Không nên gọi mọi biến thể là “Bloom Filter” rồi giả định cùng một guarantee.

Stable filter phù hợp membership gần đây nhưng có thể tạo false negative do cơ chế aging, nên guarantee khác Bloom filter cổ điển. Cuckoo filter lưu fingerprint trong bucket và hỗ trợ deletion tự nhiên hơn.

## Stable Bloom Filter

Với stream không giới hạn nhưng chỉ muốn membership gần đây, có thể chủ động làm “quên” thông tin cũ.

Stable Bloom Filter duy trì kích thước bounded bằng cách giảm/xóa một số counter/bit theo chính sách (policy / 정책).

Đổi lại, false negative có thể xuất hiện cho dữ liệu cũ.

Đây là ví dụ lỗi (error / 오류) mô hình (model / 모델) thay đổi trực tiếp khi thêm yêu cầu bounded-memory trên stream vô hạn.

Cuckoo filter di chuyển fingerprint giữa các bucket khi insert, và insertion có thể thất bại khi bảng gần đầy hoặc chuỗi kick quá dài. XOR filter xây tĩnh theo ba vị trí và thường tối ưu lookup read-only, nhưng không linh hoạt như cuckoo khi cập nhật.

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

XOR filter giải membership bằng XOR các fingerprint tại vị trí được hash và cần construction thành công trước khi publish. Nếu câu hỏi chuyển từ membership sang tần suất theo luồng, Count-Min Sketch dùng các counter theo nhiều hàng hash.

## XOR Filter

XOR Filter thường phù hợp với **tập tĩnh**: xây cấu trúc (structure / 구조) một lần rồi truy vấn (query / 쿼리) nhiều lần.

Nó có thể rất gọn và truy vấn (query / 쿼리) nhanh, nhưng cập nhật (update / 업데이트) động không tự nhiên như Bloom/Cuckoo Filter.

Bài học:

> Static tải công việc (workload / 워크로드) và động (dynamic / 동적) tải công việc (workload / 워크로드) dẫn tới cấu trúc xác suất khác nhau.

Count-Min Sketch cập nhật một counter trong mỗi row cho mỗi key và lấy các counter tương ứng khi query. Việc lấy minimum biến mọi overcount do collision thành một upper bound, thay vì chọn một hàng bất kỳ.

## Count-Min Sketch

Count-Min Sketch ước lượng frequency.

Có `d` hàng, mỗi hàng rộng `w`, mỗi hàng dùng băm (hash / 해시) riêng.

Cập nhật (update / 업데이트) key `x` thêm `c`:

```text
counter[r][h_r(x)] += c
```

Truy vấn (query / 쿼리):

```text
estimate(x) = min(counter[r][h_r(x)])
```

Trong mô hình cập nhật (update / 업데이트) không âm, collision chỉ cộng noise dương, nên estimate không nhỏ hơn count thật.

Mỗi counter của CMS không nhỏ hơn tần suất thật vì update chỉ tăng theo hash collision; minimum do đó vẫn là upper bound và thường gần giá trị thật nhất. Chiều rộng và số hàng chuyển bound đó thành các tham số `ε` và `δ`.

## Vì sao lấy minimum?

Mỗi hàng có thể xem như:

\[
estimate_r(x)=trueCount(x)+noise_r
\]

với `noise_r>=0`.

Lấy minimum chọn hàng ít bị collision noise nhất.

Lấy average sẽ cộng ảnh hưởng của các hàng nhiễu nhiều hơn và không giữ one-sided interpretation tương tự.

`ε` kiểm soát sai số tương đối còn `δ` kiểm soát xác suất guarantee thất bại; chúng quyết định chiều rộng và số hàng cần cấp phát. Conservative update giảm overcount bằng cách chỉ tăng những counter nhỏ nhất trong các vị trí của key.

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

trong đó `N` là tổng mass cập nhật (update / 업데이트) trong mô hình chuẩn.

Trực giác:

```text
width lớn -> ít collision hơn -> giảm độ lớn error
depth lớn -> có nhiều cơ hội có ít nhất một hàng sạch -> tăng confidence
```

Conservative update thường giảm bias do collision nhưng làm logic cập nhật phụ thuộc toàn bộ counter candidates và vẫn giữ upper-bound semantics. CMS trả lời frequency của key đã biết, không tự lưu danh sách định danh heavy hitter; cần cấu trúc theo dõi candidate riêng.

## Conservative cập nhật (update / 업데이트)

Thay vì tăng tất cả counter, một biến thể chỉ tăng những counter đang bằng estimate tối thiểu.

Mục tiêu là tránh đẩy những counter đã bị noise cao lên thêm nữa.

Thực tế có thể giảm over-estimation, nhưng phải phân biệt guarantee của biến thể với theorem của CMS chuẩn.

Misra–Gries lưu một số candidate và giảm đồng loạt khi bảng đầy, nên có bound rõ cho các item có tần suất lớn. Nó phù hợp với mô hình cập nhật chỉ tăng, nhưng không tự giải quyết mọi truy vấn frequency như CMS.

## CMS không tự tìm ra heavy hitter định danh (identity / 식별자)

CMS trả frequency estimate khi đã biết key.

Nếu muốn hỏi:

> “Key nào xuất hiện nhiều nhất?”

thì cần thêm candidate cấu trúc (structure / 구조), ví dụ vùng nhớ động (heap / 힙)/set hoặc thuật toán heavy-hitter chuyên dụng như Misra–Gries/Space-Saving.

Một sketch không lưu định danh (identity / 식별자) đầy đủ nên không thể tự “sinh ra” mọi key đã thấy.

Misra–Gries dùng decrement toàn bộ counters để loại bỏ mass của các item không thể là heavy hitter. Space-Saving thay bước đó bằng việc thay candidate ít đếm nhất và điều chỉnh estimate để tận dụng không gian hiệu quả hơn.

## Misra–Gries

Misra–Gries giữ tối đa `k-1` candidate counters để tìm frequent items.

Ý tưởng:

```text
nếu key đã có -> tăng counter
nếu còn slot -> thêm key
nếu hết slot và key mới -> giảm mọi counter, xóa counter về 0
```

Nó bảo đảm các item có frequency đủ lớn không bị bỏ mất khỏi candidate set theo threshold tương ứng.

Đây là một cách khác CMS: thay vì estimate mọi key đã biết, nó tập trung giữ định danh (identity / 식별자) của một tập candidate nhỏ.

Space-Saving thường giữ estimate và error của candidate để xếp hạng heavy hitter với bộ nhớ cố định. Nếu stream có update âm hoặc delete, cần turnstile-compatible sketch thay vì giả định counters chỉ tăng.

## Space-Saving

Space-Saving là một heavy-hitter thuật toán (algorithm / 알고리즘) khác, thường giữ `k` counters và khi key mới không có slot, thay thế item có count nhỏ nhất.

Nó phù hợp stream analytics khi mục tiêu chính là top frequent items.

Điểm quan trọng là chọn cấu trúc (structure / 구조) theo loại truy vấn (query / 쿼리):

```text
point frequency query -> CMS
heavy hitter identity -> Misra–Gries / Space-Saving / hybrid
```

Turnstile model cho phép increment và decrement, nên cần linear sketch hoặc signed counters với guarantee tương ứng; thuật toán dương-only có thể mất tính đúng. HyperLogLog chuyển sang bài toán ước lượng số distinct.

## Cập nhật (update / 업데이트) âm và turnstile mô hình (model / 모델)

CMS guarantee chuẩn thường giả định non-negative updates.

Nếu stream cho phép increment và decrement, phải xác định mô hình (model / 모델):

```text
strict turnstile  -> frequency thực luôn không âm
general turnstile -> intermediate/final value có thể âm
```

Một theorem cho insertion-only stream không thể áp dụng nguyên trạng cho general turnstile.

**lỗi (error / 오류) guarantee luôn gắn với cập nhật (update / 업데이트) mô hình (model / 모델).**

HLL hash mỗi item thành vị trí register và rank của phần suffix zero; các rank lớn cung cấp tín hiệu về cardinality. Register chỉ cần lưu rank lớn nhất quan sát được, nên footprint nhỏ và merge được.

## HyperLogLog

HyperLogLog ước lượng **số phần tử phân biệt (cardinality)**.

Ý tưởng nền tảng: nếu băm (hash / 해시) bit giống random, việc nhìn thấy một băm (hash / 해시) có nhiều zero liên tiếp ở đầu là sự kiện hiếm. Mức cực đại của “độ hiếm” này chứa thông tin về số distinct items đã quan sát.

HLL chia băm (hash / 해시) không gian (space / 공간) thành nhiều register để giảm variance thay vì chỉ giữ một maximum toàn cục.

Mỗi register đại diện cho một bucket của hash space và ghi maximum rank đã thấy; estimator kết hợp tất cả register thay vì một quan sát đơn. Nhiều register làm giảm variance nhờ averaging nhưng tiêu tốn memory.

## Register của HLL

Một phần băm (hash / 해시) chọn register. Phần còn lại xác định `rho`, thường là vị trí bit 1 đầu tiên hoặc số leading zeros theo convention.

Register lưu maximum `rho` từng thấy.

Nếu stream có nhiều distinct values, khả năng quan sát các mẫu (pattern / 패턴) hiếm hơn tăng, làm register lớn hơn.

Final estimator kết hợp nhiều register qua một dạng harmonic mean có correction constants.

Nhiều register giúp các bucket độc lập hơn và làm ước lượng ổn định hơn theo căn bậc hai số register. Nhưng estimator cơ bản có bias ở cardinality nhỏ và saturation ở miền rất lớn, nên cần correction theo range.

## Vì sao cần nhiều register?

Chỉ một maximum có variance rất lớn: một băm (hash / 해시) cực hiếm có thể làm estimate nhảy mạnh.

Chia dữ liệu vào nhiều bucket độc lập gần đúng rồi aggregate giúp giảm variance.

Số register `m` lớn hơn thường làm relative tiêu chuẩn (standard / 표준) lỗi (error / 오류) giảm cỡ:

\[
O(1/\sqrt m)
\]

Trong HLL kinh điển, hằng số thường được nhắc khoảng `1.04/√m` dưới mô hình lý tưởng.

Điều cần nhớ: tăng bộ nhớ (memory / 메모리) theo số register để giảm lỗi (error / 오류) theo căn bậc hai.

Small-range correction dùng số register zero để nhận diện khi quan sát còn thưa; large-range correction bù saturation hoặc giới hạn miền hash. Sau khi estimator ổn định, khả năng merge register theo phép max là một guarantee triển khai quan trọng.

## Small-range và large-range correction

Estimator thuần có độ lệch (bias / 편향) ở một số miền cardinality.

Hiện thực (implementation / 구현) HLL thực tế thường dùng correction cho:

```text
cardinality nhỏ -> nhiều register còn 0
cardinality rất lớn -> hash space saturation effects
```

Do đó không nên tự implement HLL môi trường vận hành (production / 운영 환경) chỉ từ một công thức rút gọn nếu accuracy quan trọng.

HLL merge bằng cách lấy maximum tương ứng của từng register, nhưng chỉ hợp lệ khi các sketch dùng cùng hash, precision và encoding. MinHash cũng dựa vào phép gộp trạng thái để ước lượng độ tương đồng giữa tập.

## Mergeability của HLL

Nếu hai HLL dùng cùng parameters/băm (hash / 해시) scheme, có thể merge register-wise bằng maximum:

```text
R_merged[i] = max(R_a[i], R_b[i])
```

Đây là lý do HLL rất phù hợp phân tán (distributed / 분산) analytics.

Ta có thể tính sketch trên nhiều shard rồi merge mà không gửi raw IDs.

**Mergeability là một tính năng (feature / 기능) hệ thống cực kỳ quan trọng của probabilistic summary.**

MinHash giữ các giá trị hash nhỏ nhất của các shingle, và xác suất hai signature trùng nhau xấp xỉ Jaccard similarity. LSH chia signature thành bands để biến tương đồng thành candidate retrieval với false-positive/negative trade-off.

## MinHash

MinHash ước lượng **Jaccard similarity** giữa hai tập:

\[
J(A,B)=\frac{|A\cap B|}{|A\cup B|}
\]

Với một băm (hash / 해시)/permutation ngẫu nhiên phù hợp, xác suất phần tử có băm (hash / 해시) nhỏ nhất của hai tập giống nhau bằng Jaccard similarity.

Lặp nhiều băm (hash / 해시)/signature components tạo estimator ổn định hơn.

Ứng dụng:

```text
near-duplicate documents
similar sets
recommendation candidate generation
web-page deduplication
```

MinHash cung cấp signature compact, còn LSH chỉ là lớp truy hồi candidate và vẫn cần bước similarity chính xác nếu false match đắt. Khi cần lấy mẫu stream không biết trước độ dài, reservoir sampling giải quyết bài toán khác bằng invariant xác suất.

## MinHash và LSH

MinHash signature có thể được dùng cùng **Locality-Sensitive Hashing (LSH)** để tìm candidate pair tương tự mà không so mọi cặp.

LSH không “tính similarity chính xác”; nó tăng xác suất các đối tượng (object / 객체) giống nhau rơi vào cùng bucket.

Chuỗi xử lý (pipeline / 파이프라인):

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

Reservoir sampling giữ đúng K item trong một stream chưa biết chiều dài bằng cách thay thế với xác suất phụ thuộc vị trí hiện tại. Tính đồng đều không phải trực giác may rủi; nó đến từ invariant mỗi item đã thấy có cùng xác suất nằm trong reservoir.

## Reservoir Sampling

Nếu stream dài không biết trước và muốn mẫu (sample / 표본) `k` phần tử đồng đều, không thể giữ toàn bộ rồi random sau.

Reservoir Sampling giữ `k` item đầu, sau đó với item thứ `i` chọn nó với xác suất phù hợp và nếu được chọn thì thay một vị trí ngẫu nhiên trong reservoir.

Với `k=1`, item thứ `i` được chọn với xác suất `1/i`.

Ở bước thứ `i`, mỗi item cũ có xác suất sống sót đúng bằng xác suất item mới được chọn và không đẩy nó ra; induction giữ invariant đồng đều qua toàn stream. Nếu item có trọng số khác nhau, ta cần weighted reservoir thay cho uniform sampling.

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

Đây là ví dụ đẹp của induction/xác suất (probability / 확률) proof cho streaming thuật toán (algorithm / 알고리즘).

Weighted reservoir biến trọng số thành key hoặc priority ngẫu nhiên, rồi giữ K item có priority tốt nhất; cần chứng minh phân phối mục tiêu chứ không chỉ nhân xác suất tùy ý. Quantile sketch cũng tóm tắt stream, nhưng mục tiêu là truy vấn thứ hạng thay vì giữ sample cụ thể.

## Weighted Reservoir Sampling

Nếu item có trọng số và không muốn mẫu (sample / 표본) uniform, có các biến thể weighted sampling.

Điểm cần xác định trước:

```text
sample probability tỷ lệ trọng số?
with replacement hay without replacement?
trọng số có thay đổi theo thời gian không?
```

Sampling ngữ nghĩa (semantics / 의미론) phải là một phần specification.

Quantile sketch lưu một summary có thứ tự và guarantee rank/error để trả median, percentile hoặc threshold mà không giữ toàn bộ stream. p99 nằm ở tail nhạy cảm, nên một sketch tối ưu trung tâm có thể không đủ chính xác ở đuôi.

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

Các sketch khác nhau có lỗi (error / 오류) mô hình (model / 모델) khác nhau, ví dụ rank lỗi (error / 오류) hoặc relative lỗi (error / 오류) ở tail. Khi chọn thư viện (library / 라이브러리), phải đọc guarantee cụ thể chứ không chỉ tên “quantile sketch”.

p99 có thể bị chi phối bởi ít quan sát cực lớn, và sai số rank nhỏ chưa chắc tạo sai số value nhỏ ở tail. Vì vậy phải chọn sketch theo phân phối, query và khả năng merge, không chỉ theo một con số memory.

## Tại sao p99 cần sketch chuyên biệt?

Mean độ trễ (latency / 지연 시간) có thể nhỏ trong khi tail rất xấu. Muốn theo dõi p99 trên hàng tỷ yêu cầu (request / 요청) mà không lưu toàn bộ mẫu (sample / 표본), chính xác (exact / 정확한) sorting không thực tế.

Một quantile sketch đổi một lượng lỗi (error / 오류) có kiểm soát lấy bộ nhớ (memory / 메모리) bounded.

Đây là ví dụ sản phẩm (product / 제품) yêu cầu (requirement / 요구사항) trực tiếp dẫn tới approximate cấu trúc (structure / 구조).

Mergeability phải được thiết kế cùng estimator: merge hai summary phải tương đương với chạy summary trên union stream trong giới hạn guarantee. Nhìn phép merge như một operation kết hợp giúp kiểm tra tính đúng qua monoid perspective.

## Mergeability là dimension thiết kế riêng

Trong hệ thống phân tán (distributed system / 분산 시스템), có hai cách:

```text
ship raw data về một nơi rồi tính
hoặc
compute summary tại shard rồi merge summaries
```

Nếu sketch merge được, mạng (network / 네트워크) chi phí (cost / 비용) giảm cực mạnh.

Các cấu trúc như HLL và nhiều frequency/quantile sketch được thiết kế với merge thao tác (operation / 연산) rõ ràng.

Một summary nhỏ nhưng không merge được có thể kém hữu ích trong phân tán (distributed / 분산) chuỗi xử lý (pipeline / 파이프라인).

Một sketch merge tốt có identity cho stream rỗng và operation associative đủ gần với phép hợp nhất dữ liệu; nếu không, thứ tự merge trong hệ phân tán sẽ làm kết quả trôi. Các guarantee đó vẫn phụ thuộc giả định về hash independence.

## Monoid perspective của sketch merge

Nếu summary có merge associative và định danh (identity / 식별자):

```text
merge(merge(A,B),C) = merge(A,merge(B,C))
```

thì ta có thể aggregate theo cây (tree / 트리), shard hoặc batch bất kỳ.

Đây là lý do các sketch merge-friendly rất hợp MapReduce/stream processing.

Algebraic properties không chỉ là lý thuyết; chúng quyết định khả năng quy mô (scale / 규모) hệ thống.

Hash family cần đủ độc lập hoặc đủ gần với giả định của phân tích; dùng hash yếu hoặc seed không đổi sai cách có thể tạo bias. Với input adversarial, collision có thể bị cố ý điều khiển nên seed và nguồn entropy trở thành một phần của thiết kế.

## Băm (hash / 해시) independence các giả định (assumptions / 가정들)

Nhiều proof giả định băm (hash / 해시) hàm (function / 함수) có mức independence hoặc uniformity nhất định.

Băm (hash / 해시) hiện thực (implementation / 구현) thực tế chỉ xấp xỉ mô hình lý tưởng.

Nếu key có mẫu (pattern / 패턴) xấu, attacker-controlled đầu vào (input / 입력) hoặc băm (hash / 해시) chất lượng (quality / 품질) kém, lỗi (error / 오류) thực tế có thể lệch khỏi mô hình (model / 모델).

Vì vậy môi trường vận hành (production / 운영 환경) sketch nên dùng băm (hash / 해시) hàm (function / 함수)/thư viện (library / 라이브러리) đã được đánh giá phù hợp thay vì tự nghĩ một mixing hàm (function / 함수) đơn giản.

Adversarial input có thể làm Bloom collision, sketch overcount hoặc LSH candidate set lệch khỏi phân phối kỳ vọng; cần keyed hash, randomized seed hoặc mitigation ở lớp nguồn. Deletion lại đặt một giới hạn khác: nhiều cấu trúc không thể hoàn tác chỉ bằng cách trừ một bit.

## Adversarial đầu vào (input / 입력)

Một cấu trúc xác suất được chứng minh dưới random-hash giả định (assumption / 가정) có thể không an toàn trước attacker biết seed hoặc điều khiển key.

Threat mô hình (model / 모델) cần hỏi:

```text
attacker có biết hash seed không?
attacker có quan sát output để adapt input không?
sai số chỉ ảnh hưởng analytics hay ảnh hưởng security decision?
```

Một sketch phù hợp telemetry nội bộ chưa chắc phù hợp kiểm soát truy cập (access control / 접근 제어).

Bloom filter thường không hỗ trợ delete vì không biết bit thuộc về item nào; counting hoặc generation filters đổi memory/guarantee để có aging. Sliding window và time decay cung cấp semantics “gần đây” thay vì giả vờ xóa chính xác khỏi summary.

## Deletion không phải tính năng (feature / 기능) miễn phí

Bloom Filter chuẩn không delete an toàn. CMS với decrement thay đổi cập nhật (update / 업데이트) mô hình (model / 모델). HLL không thể “trừ” một distinct item đơn giản vì register chỉ giữ maxima.

Muốn delete có thể cần:

```text
counting variant
windowed/time-decay structure
rebuild định kỳ
partition theo epoch
exact side structure
```

Một summary nén mạnh thường mất thông tin cần để đảo ngược cập nhật (update / 업데이트).

Sliding window có thể chia bucket theo thời gian rồi hết hạn cả bucket, còn decay giảm ảnh hưởng dần theo tuổi; mỗi cách cho error và latency khác nhau. Khi có nhiều tập, các signature cardinality có thể ước lượng union/intersection nhưng phải giữ tương quan hash nhất quán.

## Sliding cửa sổ (window / 윈도우) và thời gian (time / 시간) decay

Streaming hệ thống (system / 시스템) thường quan tâm “5 phút gần nhất”, không phải toàn bộ lịch sử.

Có thể dùng:

```text
epoch buckets
ring of sketches
exponential decay
window-specific algorithms
```

Ví dụ giữ HLL theo từng minute rồi merge vài bucket gần nhất. sự đánh đổi (trade-off / 트레이드오프) là ranh giới (boundary / 경계) lỗi (error / 오류) và bộ nhớ (memory / 메모리) tăng theo số epoch.

Thời gian (time / 시간) ngữ nghĩa (semantics / 의미론) là một dimension khác ngoài giá trị (value / 값) ngữ nghĩa (semantics / 의미론).

HLL union merge được bằng register-wise max; intersection thường suy ra từ inclusion–exclusion nên sai số có thể khuếch đại khi các số gần nhau. Vì vậy cần theo dõi error propagation thay vì cộng các error bound một cách máy móc.

## Cardinality của union và intersection

HLL merge rất tự nhiên cho union.

Intersection không trực tiếp bằng register-wise thao tác (operation / 연산) tương tự. Có thể dùng inclusion–exclusion từ estimates:

\[
|A\cap B|=|A|+|B|-|A\cup B|
\]

nhưng lỗi (error / 오류) của nhiều estimate cộng/trừ có thể làm kết quả kém ổn định, đặc biệt khi intersection nhỏ.

MinHash thường phù hợp hơn nếu mục tiêu chính là similarity/intersection ratio.

Chọn sketch theo truy vấn (query / 쿼리), không chỉ theo loại dữ liệu.

Khi kết hợp nhiều sketch hoặc nhiều phép biến đổi, bias, variance và correlation có thể truyền qua nhau không tuyến tính. Chọn memory budget trước hay error target trước là quyết định workload; cần ghi lại cả hai cùng assumption.

## Lan truyền lỗi (error propagation / 오류 전파)

Nếu một chuỗi xử lý (pipeline / 파이프라인) dùng nhiều approximate stages, lỗi (error / 오류) có thể tích lũy hoặc tương tác.

Ví dụ:

```text
approx frequency -> chọn candidate -> approx cardinality
```

Không nên giả định mỗi stage “1% lỗi (error / 오류)” nghĩa toàn chuỗi xử lý (pipeline / 파이프라인) vẫn “1%”.

Cần hiểu lỗi (error / 오류) direction, independence và cách downstream thao tác (operation / 연산) khuếch đại sai số.

Không có lựa chọn phổ quát: nếu SLO đặt error trước, ta suy ra memory và throughput; nếu giới hạn memory cứng, ta báo error envelope thực tế. Một sketch đã triển khai còn phải serialize seed, precision, layout và version để merge tương thích.

## Bộ nhớ (memory / 메모리) ngân sách (budget / 예산) trước, lỗi (error / 오류) sau — hay ngược lại?

Có hai cách thiết kế:

```text
business cho error target -> tính memory cần
hệ thống cho memory budget -> tính error đạt được
```

Ví dụ Bloom Filter cho phép chuyển giữa `n`, `p`, `m` tương đối trực tiếp.

Việc ghi rõ phương trình sizing biến thiết kế (design / 설계) từ “chọn đại 10 MB” thành một quyết định có thể rà soát (review / 검토).

Serialization phải bảo toàn các tham số ảnh hưởng semantics, không chỉ các counter hiện tại; khác hash seed hoặc endian có thể làm hai sketch không merge được. Determinism và reproducibility giúp phân biệt thay đổi thuật toán với dao động ngẫu nhiên.

## Serialization và tính tương thích (compatibility / 호환성)

Sketch thường được lưu hoặc truyền qua mạng (network / 네트워크). Format phải chứa đủ siêu dữ liệu (metadata / 메타데이터):

```text
version
hash seed/scheme
number of registers/counters
precision parameters
endianness nếu liên quan
```

Hai HLL khác precision hoặc băm (hash / 해시) scheme không thể merge tùy tiện.

Versioning của sketch format là một phần của phân tán (distributed / 분산) tính đúng đắn (correctness / 정확성).

Reproducible experiment cần seed, input order, version và configuration được ghi rõ; deterministic không đồng nghĩa chính xác nếu estimator có bias. Khi update từ nhiều worker, concurrency lại có thể làm mất update hoặc phá invariant nếu merge không atomic.

## Determinism và reproducibility

Randomized cấu trúc (structure / 구조) có thể cần seed cố định cho kiểm thử (test / 테스트)/reproducibility.

Nhưng môi trường vận hành (production / 운영 환경) bảo mật (security / 보안) có thể lại cần seed bí mật/ngẫu nhiên.

Không có seed chính sách (policy / 정책) duy nhất đúng. Nó phụ thuộc mục tiêu:

```text
test repeatability
cross-node merge compatibility
adversarial resistance
```

Concurrent sketch có thể dùng thread-local summaries rồi merge, hoặc atomic update với contention cao; lựa chọn phụ thuộc write rate và mergeability. Layout và cache locality quyết định throughput thực tế của các counter/register này.

## Tính đồng thời (concurrency / 동시성)

Counter array hoặc register updates từ nhiều luồng thực thi (thread / 스레드) có thể race.

Tùy cấu trúc (structure / 구조), có thể dùng:

```text
thread-local sketch rồi merge
atomic counters
sharded sketch
lock quanh batch update
```

Thread-local + merge thường hấp dẫn nếu merge thao tác (operation / 연산) rẻ và associative.

Đây là một ví dụ algebraic merge giúp thiết kế concurrent kiến trúc (architecture / 아키텍처) đơn giản hơn.

Packed counters, contiguous registers và batch update thường tận dụng cache tốt hơn các node pointer-rich, nhưng có thể tăng chi phí merge hoặc false sharing. Approximation tiếp theo cần phân biệt có random error hay chỉ là heuristic/deterministic bound.

## Bộ nhớ đệm (cache / 캐시) locality

Sketch thường dùng array nhỏ và contiguous, nên có locality tốt hơn băm (hash / 해시) Map lưu hàng triệu key.

Một trong những lý do sketch nhanh không chỉ là ít thao tác (operation / 연산) về lý thuyết mà còn vì working set nhỏ hơn và vừa bộ nhớ đệm (cache / 캐시) hơn.

Approximation đôi khi mua cả bộ nhớ (memory / 메모리) lẫn CPU efficiency qua bộ nhớ đệm (cache / 캐시).

Một cấu trúc có thể xấp xỉ do sampling, hash randomness, quantization hoặc do heuristic nén nhưng không có guarantee xác suất. Vì vậy chọn data structure phải bắt đầu từ query, update model, error semantics và operational constraints.

## Không phải approximation nào cũng probabilistic

Có deterministic approximate algorithms. Ngược lại, randomized thuật toán (algorithm / 알고리즘) có thể luôn chính xác (exact / 정확한).

Do đó phải tách:

```text
randomness source
output accuracy
runtime randomness
probability of failure
```

Không nên dùng “probabilistic” như một từ thay thế chung cho “không chính xác”.

Membership, frequency, cardinality, similarity, quantile và sampling có invariant khác nhau, nên Bloom filter không thay CMS và HLL không thay quantile sketch. Sau khi chọn cấu trúc, test phải kiểm tra đúng guarantee thay vì chỉ so một vài output.

## Chọn cấu trúc theo câu hỏi

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Câu hỏi | Cấu trúc thường đáng cân nhắc |
|---|---|
| Key có thể đã tồn tại? | Bloom/Cuckoo/XOR Filter |
| Frequency của key đã biết? | Count-Min Sketch |
| Heavy hitters là ai? | Misra–Gries / Space-Saving / CMS + candidates |
| Bao nhiêu giá trị distinct? | HyperLogLog |
| Hai tập giống nhau bao nhiêu? | MinHash |
| Lấy mẫu stream đều | Reservoir Sampling |
| Percentile/quantile | Quantile sketch phù hợp |

Bảng này chỉ là điểm khởi đầu; cập nhật (update / 업데이트)/delete/merge/lỗi (error / 오류) mô hình (model / 모델) mới quyết định cuối cùng.

Test sketch cần đo bias, variance, false-positive rate, rank error, merge behavior và saturation trên nhiều phân phối. Differential testing đối chiếu với oracle chính xác; simulation testing kiểm tra envelope qua nhiều seed và stream.

## Kiểm thử cấu trúc xác suất

Testing phải kiểm tra cả tính đúng đắn (correctness / 정확성) lô-gic (logic / 논리) lẫn statistical hành vi (behavior / 동작).

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

Không nên kiểm thử xác suất (probability / 확률) bằng 10 mẫu (sample / 표본) rồi kết luận guarantee đúng.

Differential test cho biết implementation lệch oracle ở đâu, còn simulation cho biết tần suất lệch có phù hợp guarantee qua nhiều workload không. Các hiểu lầm còn lại thường biến bound xác suất thành lời hứa tuyệt đối.

## Differential và simulation testing

Có thể so sketch với chính xác (exact / 정확한) cấu trúc (structure / 구조) trên dataset nhỏ/vừa:

```text
HashSet -> exact cardinality
HashMap -> exact frequency
full list -> exact sample distribution
```

Sau đó chạy nhiều seed/tải công việc (workload / 워크로드) để quan sát độ lệch (bias / 편향), variance và tail lỗi (error / 오류).

Đây là cách nối lý thuyết (theory / 이론) với hiện thực (implementation / 구현) thực tế.

False positive không phải false negative, merge không phải cộng state tùy tiện, và `ε/δ` không phải một độ chính xác cố định cho mọi input. Mô hình tư duy cuối bài gom guarantee, resource budget và operational evidence vào cùng một quy trình.

## Những hiểu lầm phổ biến

“Bloom Filter nói true nghĩa key tồn tại” — sai; chỉ là “có thể tồn tại”.

“Bloom Filter delete một key bằng cách clear các bit của nó” — có thể tạo false negative cho key khác.

“CMS biết heavy hitter là ai” — nó chỉ estimate key được hỏi, trừ khi ghép candidate cơ chế (mechanism / 메커니즘).

“HLL có thể xóa một người dùng (user / 사용자) khỏi cardinality bằng cách undo băm (hash / 해시)” — không đơn giản vì register giữ max lịch sử (history / 이력).

“Sketch nhỏ thì accuracy cố định” — lỗi (error / 오류) phụ thuộc parameters và tải công việc (workload / 워크로드) kích thước (size / 크기).

“Expected/statistical guarantee vẫn đúng với mọi adversarial băm (hash / 해시) đầu vào (input / 입력)” — không nếu các giả định (assumptions / 가정들) bị phá.

“Merge hai sketch cùng loại luôn hợp lệ” — sai nếu precision/băm (hash / 해시)/phiên bản (version / 버전) khác nhau.

Mô hình tư duy là: xác định câu hỏi, chọn invariant và guarantee, tính error/memory budget, kiểm tra merge và adversarial behavior, rồi đo lại trên workload thật. Các liên kết cuối bài giúp đối chiếu từng họ cấu trúc với bài toán streaming tương ứng.

## Mô hình tư duy

> Probabilistic cấu trúc dữ liệu (data structure / 자료구조) là một **hợp đồng nén thông tin**. Ta chủ động bỏ khả năng phân biệt một số trạng thái để đổi lấy bộ nhớ (memory / 메모리)/thông lượng (throughput / 처리량)/mergeability, nhưng phải mô tả chính xác cái giá bằng lỗi (error / 오류) mô hình (model / 모델).

Khi chọn sketch, hãy hỏi: **truy vấn thật sự là membership, frequency, heavy hitter, cardinality, similarity hay quantile; lỗi (error / 오류) được phép theo hướng nào; bộ nhớ (memory / 메모리) bao nhiêu; cập nhật (update / 업데이트) có delete không; cần merge giữa shard không; băm (hash / 해시) các giả định (assumptions / 가정들) có phù hợp threat mô hình (model / 모델) không; và downstream hệ thống (system / 시스템) sẽ dùng estimate như thế nào?**

Xem tiếp: [Hash Tables](../01_linear_structures/04_hash_tables.md), [Amortized, Randomized & Probabilistic Thinking](./03_amortized_randomized_and_probabilistic_thinking.md), [Mathematical Toolkit](../00_foundations/04_mathematical_toolkit_for_dsa.md), [Bit Manipulation](./02_bit_manipulation_and_bitsets.md) và [DSA in Databases, Networks & Systems](../90_connections/01_dsa_in_databases_networks_and_systems.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
