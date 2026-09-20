# Probabilistic Data Structures cho dữ liệu lớn  
**확률적 자료구조**

Khi data stream quá lớn để lưu toàn bộ, đôi khi requirement thực sự không cần exact answer. Nếu chấp nhận một error model rõ ràng, ta có thể giảm memory từ tỷ lệ với số items xuống rất nhỏ.

## Bloom Filter

Bloom filter trả lời approximate membership. Nó không lưu keys, chỉ lưu bit pattern tạo bởi hashes.

Nếu query thấy một required bit bằng 0, key chắc chắn chưa được insert theo standard no-deletion model. Nếu tất cả bits đều 1, key **có thể** tồn tại.

False positive probability xấp xỉ phụ thuộc `m` bits, `n` inserted items và `k` hashes. Với parameter hợp lý, memory trên item thấp hơn hash set nhiều.

Use case: tránh expensive database/disk lookup cho keys chắc chắn không tồn tại, cache admission, distributed storage membership filters.

## Count-Min Sketch

Count-Min Sketch ước lượng frequency. Nó có nhiều rows hash tables; mỗi update increment một cell mỗi row. Query lấy minimum counters tương ứng.

Collision chỉ làm count tăng quá thật, nên estimate có one-sided error theo standard model. Memory không phụ thuộc số distinct keys trực tiếp, mà phụ thuộc desired error/confidence.

Use case: heavy hitters, telemetry, network traffic.

## HyperLogLog

Distinct count exact cần set mọi unique item, memory có thể rất lớn. HyperLogLog ước lượng cardinality từ statistical property của hash bit patterns, đặc biệt position của leading zeros.

Nó đạt relative error nhỏ với fixed compact registers, rất phù hợp “có khoảng bao nhiêu unique users?” ở quy mô lớn.

## Reservoir sampling

Nếu stream length không biết trước và muốn sample `k` items uniformly, reservoir sampling giữ `k` samples. Khi item thứ `i` tới, nó được chọn vào reservoir với probability `k/i`, thay ngẫu nhiên một existing item nếu được chọn.

Không cần lưu stream hoặc biết total length trước.

## Khi nào approximate structure là sai lựa chọn?

Các nghiệp vụ cần kết quả membership/accounting tuyệt đối chính xác không phù hợp với false-positive hoặc estimation. Approximation chỉ hợp lý khi product/system requirement định lượng được error budget.

## Mental Model

> Probabilistic data structure nén thông tin bằng cách **từ bỏ khả năng tái tạo exact set/count**, nhưng giữ đủ statistical signal để trả lời một query class với error guarantee rõ ràng.

## Bloom Filter: error đến từ đâu?

Sau `n` inserts, mỗi insert set `k` positions trong `m` bits. Dưới hashing assumptions thông thường, xác suất một bit vẫn 0 xấp xỉ:

\[
\left(1-\frac1m\right)^{kn}
\approx e^{-kn/m}
\]

Vì vậy xác suất một bit là 1 xấp xỉ:

\[
1-e^{-kn/m}
\]

Một query key chưa từng insert bị false positive nếu cả `k` positions của nó đều đã thành 1:

\[
p \approx \left(1-e^{-kn/m}\right)^k
\]

Công thức cho thấy không có `k` càng lớn càng tốt; nhiều hash functions vừa set nhiều bits hơn vừa làm query tốn hơn. Với `m,n` cố định có một vùng `k` tối ưu.

## Count-Min Sketch: width và depth

Count-Min Sketch có `d` hash rows, mỗi row width `w`. Collision làm estimate tăng, không giảm theo standard non-negative frequency model. Tăng width giảm collision/error magnitude; tăng depth giảm probability tất cả rows đều bị collision xấu.

Query lấy minimum vì mỗi counter là true count cộng collision noise; minimum cố tìm row ít nhiễu nhất.

Nó phù hợp cho question “item này xuất hiện khoảng bao nhiêu lần?”, không phù hợp khi cần exact accounting.

## HyperLogLog intuition

Nếu hash outputs uniform, thấy một hash bắt đầu bằng rất nhiều zero liên tiếp là event hiếm. Quan sát maximum/aggregate pattern của leading-zero counts cung cấp signal về số distinct values đã xuất hiện.

HyperLogLog chia hash space thành registers để giảm variance và dùng harmonic-style aggregation cùng bias corrections trong implementations thực tế.

Điểm quan trọng: nó không “đếm users rồi nén”; nó giữ **statistical evidence** đủ để ước lượng cardinality.

## Reservoir sampling vì sao uniform?

Với reservoir size 1, item thứ `i` thay sample hiện tại với probability `1/i`. Một item xuất hiện ở position `j` được chọn lúc `j` với probability `1/j`, rồi phải sống sót qua các bước `j+1...n`.

Xác suất sống sót telescopes:

\[
\frac1j
\cdot\frac{j}{j+1}
\cdot\frac{j+1}{j+2}
\cdots
\frac{n-1}{n}
=
\frac1n
\]

nên mọi item có xác suất bằng nhau ở cuối stream. Reservoir size `k` là generalization của reasoning đó.

## Mergeability trong distributed systems

Một lý do sketches hữu ích là nhiều loại có thể merge. Các workers xử lý partitions riêng rồi combine summaries thay vì gửi raw events. HyperLogLog registers có thể combine bằng max theo register; Count-Min Sketch tables cùng parameters có thể cộng counters.

Bloom filters cùng size/hash scheme có thể OR để biểu diễn union membership approximation.

Mergeability biến data structure thành primitive cho distributed aggregation.

## Hash quality là assumption, không phải chi tiết

Nếu input distribution tương quan xấu với hash function, theoretical error model có thể không giữ. Production systems cần hash functions/seeds phù hợp và parameterization dựa trên expected cardinality/error budget.

## Mental Model mở rộng

> Exact structure cố giữ đủ information để phân biệt mọi trường hợp cần thiết. Probabilistic structure chủ động **nén nhiều histories thành cùng internal state**, sau đó mô tả xác suất sai do sự nén đó gây ra.
