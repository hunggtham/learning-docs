# Adaptive truy vấn (query / 쿼리) thực thi (execution / 실행), thời gian chạy (runtime / 런타임) filters, skew và re-optimization

> **Mạch đọc:** Đặt **Adaptive truy vấn (query / 쿼리) thực thi (execution / 실행), thời gian chạy (runtime / 런타임) filters, skew và re-optimization** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Vì sao optimizer không thể biết mọi thứ trước thực thi (execution / 실행)** sang **2. Adaptation ranh giới (boundary / 경계)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Cost-based optimizer phải chọn plan **trước khi** truy vấn (query / 쿼리) thực sự chạy, trong khi nhiều thông tin quan trọng chỉ xuất hiện **sau khi thực thi (execution / 실행) bắt đầu**: cardinality thực, skew thực, selectivity của predicate, bộ nhớ (memory / 메모리) pressure, partition kích thước (size / 크기) và mạng (network / 네트워크) transfer. Nếu estimate sai lớn, một plan hợp lý trên giấy có thể trở thành bottleneck môi trường vận hành (production / 운영 환경).

Adaptive truy vấn (query / 쿼리) thực thi (execution / 실행) (AQE) là nhóm kỹ thuật cho phép engine dùng bằng chứng (evidence / 증거) thời gian chạy (runtime / 런타임) để điều chỉnh thực thi (execution / 실행) mà vẫn giữ truy vấn (query / 쿼리) ngữ nghĩa (semantics / 의미론).

Mô hình tư duy (mental model / 사고 모델):

```text
logical query
→ compile-time statistics
→ initial physical plan
→ runtime cardinality / distribution evidence
→ adaptive decision
→ revised stage/operator strategy
→ same logical result
```

Bất biến (invariant / 불변식) quan trọng nhất là: **thực thi (execution / 실행) chiến lược (strategy / 전략) có thể đổi, nhưng ngữ nghĩa (semantics / 의미론) của truy vấn (query / 쿼리) không được đổi**.

## 1. Vì sao optimizer không thể biết mọi thứ trước thực thi (execution / 실행)

Statistics chỉ là mô hình (model / 모델) của dữ liệu (data / 데이터). Histogram có thể cũ, correlation giữa columns có thể bị bỏ qua, parameter giá trị (value / 값) có thể khác phân phối (distribution / 분포) trung bình và intermediate kết quả (result / 결과) phụ thuộc nhiều predicate/phép nối (join / 조인) liên tiếp.

Một lỗi cardinality nhỏ ở đầu plan có thể khuếch đại. Nếu optimizer nghĩ phép nối (join / 조인) tạo 10 nghìn rows nhưng thực tế là 100 triệu, quyết định broadcast, phép nối (join / 조인) thứ tự (order / 순서), bộ nhớ (memory / 메모리) grant và parallelism có thể sai đồng thời.

Vì vậy compile-time tối ưu hóa (optimization / 최적화) luôn có epistemic limit: nó ra quyết định dưới bất định (uncertainty / 불확실성).

## 2. Adaptation ranh giới (boundary / 경계)

Không phải engine muốn đổi plan ở bất kỳ instruction nào cũng được. Re-optimization thường cần **safe ranh giới (boundary / 경계)**: materialized stage, exchange ranh giới (boundary / 경계) hoặc điểm mà intermediate kết quả (result / 결과) đã có định danh (identity / 식별자) rõ.

Tại ranh giới (boundary / 경계) đó, engine biết kích thước (size / 크기)/phân phối (distribution / 분포) thực của đầu ra (output / 출력) trước và có thể chọn chiến lược (strategy / 전략) cho stage sau.

```text
stage A chạy
→ materialized/shuffle output
→ runtime stats
→ chọn lại stage B
```

Nếu đổi giữa chừng mà trạng thái (state / 상태) của operator cũ đã có side tác động (effect / 효과) hoặc partial aggregation phức tạp, tính đúng đắn (correctness / 정확성) trở nên khó chứng minh hơn.

## 3. thời gian chạy (runtime / 런타임) cardinality

Cardinality thời gian chạy (runtime / 런타임) là bằng chứng (evidence / 증거) mạnh nhất để kiểm tra optimizer giả định (assumption / 가정). Nó cho phép engine phát hiện:

- filter selectivity khác estimate;
- phép nối (join / 조인) đầu ra (output / 출력) lớn/nhỏ bất ngờ;
- partition skew;
- broadcast side vượt threshold;
- bộ nhớ (memory / 메모리) footprint sắp vượt ngân sách (budget / 예산).

Nhưng thời gian chạy (runtime / 런타임) stats cũng có chi phí (cost / 비용). Muốn biết chính xác mọi intermediate cardinality có thể cần materialization hoặc synchronization. Adaptive engine phải cân bằng thông tin (information / 정보) giá trị (value / 값) với overhead.

## 4. Broadcast phép nối (join / 조인) có thể đổi thành partitioned phép nối (join / 조인)

Giả sử optimizer tin dimension bảng (table / 테이블) sau filter chỉ còn 20 MB nên chọn broadcast. thời gian chạy (runtime / 런타임) phát hiện nó là 2 GB. Tiếp tục broadcast có thể bản sao (copy / 복사) 2 GB tới nhiều worker, gây mạng (network / 네트워크)/bộ nhớ (memory / 메모리) explosion.

Adaptive quyết định (decision / 결정) có thể chuyển sang repartition/băm (hash / 해시) phép nối (join / 조인). Đây không chỉ là “đổi thuật toán (algorithm / 알고리즘)”; nó thay tài nguyên (resource / 자원) topology:

```text
broadcast:
one-side replication → nhiều memory copy, ít shuffle phía còn lại

partitioned:
both sides partition by key → shuffle lớn hơn nhưng memory phân tán
```

Threshold tốt phụ thuộc worker count, mạng (network / 네트워크), available bộ nhớ (memory / 메모리) và concurrent tải công việc (workload / 워크로드).

## 5. thời gian chạy (runtime / 런타임) filters

Trong phép nối (join / 조인), bản dựng (build / 빌드) side có thể tạo compact membership cấu trúc (structure / 구조) hoặc giá trị (value / 값) phạm vi (range / 범위) rồi đẩy ngược filter về scan của probe side. Mục tiêu là loại dữ liệu (data / 데이터) sớm trước khi tốn I/O, decode, shuffle và phép nối (join / 조인) công việc (work / 작업).

Lập luận (reasoning / 추론) đường dẫn (path / 경로):

```text
build-side keys
→ runtime filter
→ push toward scan
→ skip impossible rows/segments
→ reduce downstream work
```

Bloom-like filter thường chấp nhận false positive: một số row không match vẫn đi qua và bị loại ở phép nối (join / 조인). Nhưng false negative không được phép nếu filter dùng để loại row trong chính xác (exact / 정확한) truy vấn (query / 쿼리); nếu bỏ nhầm key thật, kết quả (result / 결과) sai.

Thời gian chạy (runtime / 런타임) filter vì thế có cùng an toàn (safety / 안전) bất biến (invariant / 불변식) với pruning siêu dữ liệu (metadata / 메타데이터) trong [columnar storage](./08_columnar_storage_encoding_pruning_and_vectorized_scans.md).

## 6. Filter arrival thời gian (time / 시간)

Một thời gian chạy (runtime / 런타임) filter chỉ hữu ích nếu tới đủ sớm. Nếu probe scan đã đọc 90% bảng (table / 테이블) trước khi filter được tạo, benefit nhỏ dù filter rất selective.

Đây tạo scheduling phụ thuộc (dependency / 의존성) giữa bản dựng (build / 빌드) side và probe side. Engine có thể chờ filter, chạy speculative, hoặc đặt hết thời gian chờ (timeout / 타임아웃). Chờ quá lâu làm mất parallelism; không chờ làm mất pruning opportunity.

Adaptive hệ thống (system / 시스템) phải lập luận (reasoning / 추론) cả **giá trị (value / 값) of thông tin (information / 정보)** lẫn **chi phí (cost / 비용) of waiting**.

## 7. dữ liệu (data / 데이터) skew

Băm (hash / 해시) partitioning giả định key phân phối (distribution / 분포) đủ đều. Hot key có thể đưa phần lớn rows vào một partition:

```text
99 workers xong sớm
1 worker giữ hot partition
→ stage completion chờ straggler
```

Average partition kích thước (size / 크기) che mất vấn đề. bằng chứng (evidence / 증거) phải nhìn phân phối (distribution / 분포), max/p99 partition kích thước (size / 크기) và tác vụ (task / 작업) duration.

Adaptive mitigation có thể split skewed partition, replicate small-side dữ liệu (data / 데이터) cho subpartitions, salt hot key hoặc chọn chiến lược (strategy / 전략) khác. Nhưng mỗi kỹ thuật phải giữ phép nối (join / 조인) ngữ nghĩa (semantics / 의미론); salting tùy tiện có thể duplicate hoặc mất match.

## 8. Coalescing small partitions

Ngược lại với skew là quá nhiều partition nhỏ. Scheduling overhead, siêu dữ liệu (metadata / 메타데이터) và tiny mạng (network / 네트워크) transfer có thể chiếm phần lớn chi phí (cost / 비용).

Thời gian chạy (runtime / 런타임) kích thước (size / 크기) bằng chứng (evidence / 증거) cho phép coalesce nhiều partition nhỏ thành ít tác vụ (task / 작업) hơn. Nhưng coalesce quá mạnh giảm parallelism và tạo tác vụ (task / 작업) dài. Mục tiêu không phải ít partition nhất mà là công việc (work / 작업) granularity phù hợp cluster và tail hành vi (behavior / 동작).

## 9. bộ nhớ (memory / 메모리) grant và spill

Optimizer có thể cấp bộ nhớ (memory / 메모리) dựa estimate. Underestimate làm bảng băm (hash table / 해시 테이블)/sort spill xuống disk; overestimate giữ bộ nhớ (memory / 메모리) thừa và giảm tính đồng thời (concurrency / 동시성) toàn cluster.

Adaptive thực thi (execution / 실행) có thể điều chỉnh partitioning hoặc chiến lược (strategy / 전략) khi thấy bộ nhớ (memory / 메모리) footprint thực. Tuy nhiên bộ nhớ (memory / 메모리) đã dùng không thể luôn “thu hồi miễn phí”; một số operator phải spill hoặc restart stage.

Spill là **phase thay đổi (change / 변경)** quan trọng:

```text
working set fits memory
→ in-memory throughput

working set exceeds memory
→ disk/network spill
→ latency tăng phi tuyến
```

Do đó thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) nên ghi bytes spilled, spill count, merge passes và per-stage bộ nhớ (memory / 메모리) peak.

## 10. Re-optimization và sunk chi phí (cost / 비용)

Đổi plan có chi phí (cost / 비용). Nếu stage đã chạy 95%, restart bằng plan tốt hơn có thể tệ hơn hoàn thành plan hiện tại. Adaptive controller phải xét **remaining chi phí (cost / 비용)**, không chỉ so plan lý tưởng từ đầu.

Đây giống quyết định (decision / 결정) under sunk chi phí (cost / 비용):

```text
cost tiếp tục plan hiện tại
vs
cost dừng + chuyển + chạy plan mới
```

Re-optimization trigger quá nhạy có thể oscillate hoặc làm thực thi (execution / 실행) khó dự đoán.

## 11. Parameter-sensitive hành vi (behavior / 동작)

Cùng SQL văn bản (text / 텍스트) nhưng parameter khác có thể cần plan khác. truy vấn (query / 쿼리) lấy một customer cụ thể khác truy vấn (query / 쿼리) lấy toàn bộ region. Nếu bộ nhớ đệm (cache / 캐시) một plan cho mọi parameter, một thực thi (execution / 실행) đầu tiên có thể “đóng băng” giả định (assumption / 가정) không phù hợp các thực thi (execution / 실행) sau.

Adaptive thực thi (execution / 실행) giảm một phần rủi ro (risk / 위험) bằng thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거), nhưng compile-time plan caching và thời gian chạy (runtime / 런타임) adaptation là hai tầng (layer / 계층) khác nhau. Cần quan sát cả estimated/actual cardinality và parameter cohort.

## 12. phân tán (distributed / 분산) thực thi (execution / 실행) và mạng (network / 네트워크)

Trong analytical engine phân tán, exchange/shuffle là ranh giới (boundary / 경계) vừa về dữ liệu (data / 데이터) vừa về mạng (network / 네트워크). Adaptive partition count ảnh hưởng liên kết (connection / 연결) count, buffer, serialization và congestion.

Một plan giảm CPU nhưng tăng shuffle có thể tệ khi mạng (network / 네트워크) saturated. Ngược lại, broadcast tránh repartition nhưng nhân bản bytes theo worker count.

Chi phí (cost / 비용) mô hình (model / 모델) thời gian chạy (runtime / 런타임) cần hiểu tài nguyên (resource / 자원) đang scarce ở thời điểm đó; “cheapest plan” không cố định nếu cluster pressure thay đổi.

## 13. thất bại (failure / 실패) modes

**Late adaptation:** phát hiện estimate sai khi phần lớn expensive công việc (work / 작업) đã xảy ra.

**Thrashing:** controller đổi chiến lược (strategy / 전략) quá thường xuyên do threshold/noise.

**Skew hidden by averages:** tổng bytes bình thường nhưng một partition quyết định tail.

**thời gian chạy (runtime / 런타임) filter too late:** filter đúng nhưng arrival sau scan nên gần như vô ích.

**Unsafe pruning:** filter hiện thực (implementation / 구현) tạo false negative làm sai kết quả (result / 결과).

**Spill cascade:** nhiều truy vấn (query / 쿼리) đồng thời vượt bộ nhớ (memory / 메모리), cùng spill và làm lưu trữ (storage / 저장소) saturated.

**Adaptive herd:** nhiều truy vấn (query / 쿼리) cùng thấy cluster trạng thái (state / 상태) rồi đồng thời chọn chiến lược (strategy / 전략) giống nhau, tạo bottleneck mới.

## 14. bằng chứng vận hành (production evidence / 운영 증거)

Thực thi (execution / 실행) plan phải được đọc cùng thời gian chạy (runtime / 런타임) counters:

```text
estimated rows vs actual rows
rows/bytes per operator
partition-size distribution
broadcast/shuffle bytes
runtime-filter build time, arrival time, selectivity
memory peak / grant
spill bytes và spill passes
task duration distribution
stage retry/replan count
CPU, disk và network saturation
```

Một plan diagram không có actual cardinality chỉ cho biết optimizer đã tin gì, chưa cho biết thời gian chạy (runtime / 런타임) đã xảy ra gì.

## 15. Worked lập luận (reasoning / 추론) trường hợp (case / 사례)

Giả sử dashboard truy vấn (query / 쿼리) bình thường 8 giây bỗng thành 90 giây sau khi dữ liệu (data / 데이터) tăng.

Plan cho thấy optimizer chọn broadcast phép nối (join / 조인). Estimated bản dựng (build / 빌드) side 40 MB, actual 1.8 GB. Worker bộ nhớ (memory / 메모리) tăng, một số spill; mạng (network / 네트워크) outbound tăng mạnh. thời gian chạy (runtime / 런타임) filter chỉ xuất hiện sau khi probe scan gần hoàn tất.

Lập luận (reasoning / 추론) chuỗi (chain / 사슬):

```text
stale/correlated statistics
→ underestimate build cardinality
→ broadcast decision sai
→ replicated memory/network pressure
→ spill
→ runtime filter tới muộn
→ tail latency tăng mạnh
```

Fix có thể nằm ở statistics, plan chính sách (policy / 정책), adaptive broadcast threshold hoặc stage scheduling. Tăng machine bộ nhớ (memory / 메모리) chỉ che symptom nếu estimator tiếp tục sai.

## 16. liên kết (connection / 연결) với các chapter khác

Đọc chapter này sau [cost-based optimizer](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md), [join/vectorized execution](./06_join_algorithms_vectorized_execution_and_late_materialization.md) và [columnar storage](./08_columnar_storage_encoding_pruning_and_vectorized_scans.md).

Ở tầng hệ thống, adaptive thực thi (execution / 실행) nối với [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và [fleet profiling/cost attribution](../../08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md).

Mô hình tư duy (mental model / 사고 모델) cuối cùng:

```text
optimizer = decision under incomplete information
runtime = evidence
adaptive execution = controlled revision at safe boundary
correctness invariant = logical result không đổi
performance goal = tránh catastrophic mismatch giữa estimate và reality
```

Đây là bước chuyển từ “optimizer chọn plan tốt” sang hiểu cơ sở dữ liệu (database / 데이터베이스) như một **phản hồi (feedback / 피드백) hệ thống (system / 시스템)** quan sát thực thi (execution / 실행) và sửa giả định (assumption / 가정) khi đủ bằng chứng (evidence / 증거).

> **Bàn giao:** Sau **16. liên kết (connection / 연결) với các chapter khác**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mvcc visibility wal and recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
