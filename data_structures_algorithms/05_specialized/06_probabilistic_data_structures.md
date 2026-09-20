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
