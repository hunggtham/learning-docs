# 06 — Distributed processing: partition, shuffle, skew và spill

Distributed processing không chỉ là chạy cùng một function trên nhiều máy. Hệ thống phải chia input, di chuyển dữ liệu giữa worker, giữ ordering/aggregation semantics và phục hồi khi một phần computation thất bại.

## 1. Execution graph

Một job thường có các stage nối bằng boundary:

```text
read → map/filter → repartition → join/aggregate → write
```

Operation giữ record ở cùng partition thường rẻ hơn operation cần đưa các record cùng key về một nơi. Boundary đó thường là shuffle. Khi review một job, hãy đánh dấu byte đi qua network, không chỉ số dòng trong code.

## 2. Partition

Partition là đơn vị phân phối work và thường là đơn vị failure/retry. Key tốt cần đủ phân tán, ổn định và phù hợp với operation downstream. Partition theo một key có cardinality thấp tạo hotspot; partition theo key quá ngẫu nhiên làm mất locality và tăng shuffle.

Partition count phải tương xứng với input size, worker parallelism và overhead scheduling. Quá ít partition tạo task dài; quá nhiều tạo task nhỏ, metadata và scheduling overhead.

## 3. Shuffle

Shuffle xảy ra khi record phải đi tới partition mới theo key/range. Chi phí gồm serialize, network transfer, buffer, disk spill và merge. Join, group-by và global sort thường là shuffle boundary.

Một query có ít output vẫn có thể shuffle nhiều TB. Predicate pushdown trước shuffle, pre-aggregation và projection sớm giảm byte di chuyển. Không được đo performance chỉ bằng output size.

## 4. Skew

Skew là khi phân phối key không đều: một customer lớn, một ngày lỗi, hoặc `null` gom phần lớn record vào một partition. Dấu hiệu là phần lớn task hoàn tất nhưng một vài task kéo dài, memory cao và spill lớn.

Các hướng xử lý tùy semantics:

- lọc hoặc xử lý `null`/heavy hitter riêng;
- pre-aggregate trước join;
- salting key rồi aggregate lại;
- broadcast phía nhỏ khi thật sự phù hợp;
- thay đổi partition strategy hoặc giới hạn input theo time slice.

Tăng worker không chữa được một key vẫn phải đi vào một partition duy nhất.

## 5. Spill và memory pressure

Khi hash table, sort buffer hoặc aggregation state vượt memory, engine spill intermediate data xuống disk. Spill bảo vệ correctness nhưng tăng I/O, serialization và merge pass. Spill cao có thể là triệu chứng của skew, partition quá lớn, projection dư thừa hoặc concurrency quá cao.

Đừng chỉ tăng memory. Hãy phân biệt:

```text
input bytes → post-filter bytes → shuffle bytes → spill bytes → output bytes
```

Mỗi bước có bottleneck khác nhau và cần evidence riêng.

## 6. Join semantics

Hash join thường cần build side vừa memory; sort-merge join cần sort và có thể spill; broadcast join giảm shuffle nhưng tạo pressure trên mọi worker. Chọn algorithm phải dựa trên cardinality, distribution, null semantics, freshness và failure behavior.

Nếu duplicate key ở một phía là hợp lệ, join output có thể tăng theo tích cardinality. Query “chạy được” không chứng minh join đúng business.

## 7. Fault recovery

Worker failure buộc engine retry task hoặc stage. Nếu source và sink có side effect ngoài transaction, retry có thể duplicate. Intermediate data cần được tái tạo hoặc lưu với lifecycle rõ ràng. Output commit chỉ nên public sau khi toàn bộ partition cần thiết đã hoàn tất và reconcile đạt.

## 8. Performance review loop

1. Xác định grain và predicate cần thiết.
2. Đo input, filtered, shuffle, spill, output bytes.
3. Kiểm tra task duration distribution, không chỉ average.
4. Tìm heavy hitter/skew key.
5. Kiểm tra memory, disk, network và concurrency saturation.
6. Thay đổi một boundary, chạy lại cùng input/version và so sánh correctness trước cost.

Đọc tiếp: [03 — Storage và layout](../03_storage_and_formats.md), [07 — Streaming systems](../07_streaming_systems/README.md), [12 — Cost, performance và capacity](../12_cost_performance_capacity/README.md).
