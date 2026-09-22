# Adaptive query execution, runtime filters, skew và re-optimization

Cost-based optimizer phải chọn plan **trước khi** query thực sự chạy, trong khi nhiều thông tin quan trọng chỉ xuất hiện **sau khi execution bắt đầu**: cardinality thực, skew thực, selectivity của predicate, memory pressure, partition size và network transfer. Nếu estimate sai lớn, một plan hợp lý trên giấy có thể trở thành bottleneck production.

Adaptive query execution (AQE) là nhóm kỹ thuật cho phép engine dùng evidence runtime để điều chỉnh execution mà vẫn giữ query semantics.

Mental model:

```text
logical query
→ compile-time statistics
→ initial physical plan
→ runtime cardinality / distribution evidence
→ adaptive decision
→ revised stage/operator strategy
→ same logical result
```

Invariant quan trọng nhất là: **execution strategy có thể đổi, nhưng semantics của query không được đổi**.

## 1. Vì sao optimizer không thể biết mọi thứ trước execution

Statistics chỉ là model của data. Histogram có thể cũ, correlation giữa columns có thể bị bỏ qua, parameter value có thể khác distribution trung bình và intermediate result phụ thuộc nhiều predicate/join liên tiếp.

Một lỗi cardinality nhỏ ở đầu plan có thể khuếch đại. Nếu optimizer nghĩ join tạo 10 nghìn rows nhưng thực tế là 100 triệu, quyết định broadcast, join order, memory grant và parallelism có thể sai đồng thời.

Vì vậy compile-time optimization luôn có epistemic limit: nó ra quyết định dưới uncertainty.

## 2. Adaptation boundary

Không phải engine muốn đổi plan ở bất kỳ instruction nào cũng được. Re-optimization thường cần **safe boundary**: materialized stage, exchange boundary hoặc điểm mà intermediate result đã có identity rõ.

Tại boundary đó, engine biết size/distribution thực của output trước và có thể chọn strategy cho stage sau.

```text
stage A chạy
→ materialized/shuffle output
→ runtime stats
→ chọn lại stage B
```

Nếu đổi giữa chừng mà state của operator cũ đã có side effect hoặc partial aggregation phức tạp, correctness trở nên khó chứng minh hơn.

## 3. Runtime cardinality

Cardinality runtime là evidence mạnh nhất để kiểm tra optimizer assumption. Nó cho phép engine phát hiện:

- filter selectivity khác estimate;
- join output lớn/nhỏ bất ngờ;
- partition skew;
- broadcast side vượt threshold;
- memory footprint sắp vượt budget.

Nhưng runtime stats cũng có cost. Muốn biết chính xác mọi intermediate cardinality có thể cần materialization hoặc synchronization. Adaptive engine phải cân bằng information value với overhead.

## 4. Broadcast join có thể đổi thành partitioned join

Giả sử optimizer tin dimension table sau filter chỉ còn 20 MB nên chọn broadcast. Runtime phát hiện nó là 2 GB. Tiếp tục broadcast có thể copy 2 GB tới nhiều worker, gây network/memory explosion.

Adaptive decision có thể chuyển sang repartition/hash join. Đây không chỉ là “đổi algorithm”; nó thay resource topology:

```text
broadcast:
one-side replication → nhiều memory copy, ít shuffle phía còn lại

partitioned:
both sides partition by key → shuffle lớn hơn nhưng memory phân tán
```

Threshold tốt phụ thuộc worker count, network, available memory và concurrent workload.

## 5. Runtime filters

Trong join, build side có thể tạo compact membership structure hoặc value range rồi đẩy ngược filter về scan của probe side. Mục tiêu là loại data sớm trước khi tốn I/O, decode, shuffle và join work.

Reasoning path:

```text
build-side keys
→ runtime filter
→ push toward scan
→ skip impossible rows/segments
→ reduce downstream work
```

Bloom-like filter thường chấp nhận false positive: một số row không match vẫn đi qua và bị loại ở join. Nhưng false negative không được phép nếu filter dùng để loại row trong exact query; nếu bỏ nhầm key thật, result sai.

Runtime filter vì thế có cùng safety invariant với pruning metadata trong [columnar storage](./08_columnar_storage_encoding_pruning_and_vectorized_scans.md).

## 6. Filter arrival time

Một runtime filter chỉ hữu ích nếu tới đủ sớm. Nếu probe scan đã đọc 90% table trước khi filter được tạo, benefit nhỏ dù filter rất selective.

Đây tạo scheduling dependency giữa build side và probe side. Engine có thể chờ filter, chạy speculative, hoặc đặt timeout. Chờ quá lâu làm mất parallelism; không chờ làm mất pruning opportunity.

Adaptive system phải reasoning cả **value of information** lẫn **cost of waiting**.

## 7. Data skew

Hash partitioning giả định key distribution đủ đều. Hot key có thể đưa phần lớn rows vào một partition:

```text
99 workers xong sớm
1 worker giữ hot partition
→ stage completion chờ straggler
```

Average partition size che mất vấn đề. Evidence phải nhìn distribution, max/p99 partition size và task duration.

Adaptive mitigation có thể split skewed partition, replicate small-side data cho subpartitions, salt hot key hoặc chọn strategy khác. Nhưng mỗi kỹ thuật phải giữ join semantics; salting tùy tiện có thể duplicate hoặc mất match.

## 8. Coalescing small partitions

Ngược lại với skew là quá nhiều partition nhỏ. Scheduling overhead, metadata và tiny network transfer có thể chiếm phần lớn cost.

Runtime size evidence cho phép coalesce nhiều partition nhỏ thành ít task hơn. Nhưng coalesce quá mạnh giảm parallelism và tạo task dài. Mục tiêu không phải ít partition nhất mà là work granularity phù hợp cluster và tail behavior.

## 9. Memory grant và spill

Optimizer có thể cấp memory dựa estimate. Underestimate làm hash table/sort spill xuống disk; overestimate giữ memory thừa và giảm concurrency toàn cluster.

Adaptive execution có thể điều chỉnh partitioning hoặc strategy khi thấy memory footprint thực. Tuy nhiên memory đã dùng không thể luôn “thu hồi miễn phí”; một số operator phải spill hoặc restart stage.

Spill là **phase change** quan trọng:

```text
working set fits memory
→ in-memory throughput

working set exceeds memory
→ disk/network spill
→ latency tăng phi tuyến
```

Do đó runtime evidence nên ghi bytes spilled, spill count, merge passes và per-stage memory peak.

## 10. Re-optimization và sunk cost

Đổi plan có cost. Nếu stage đã chạy 95%, restart bằng plan tốt hơn có thể tệ hơn hoàn thành plan hiện tại. Adaptive controller phải xét **remaining cost**, không chỉ so plan lý tưởng từ đầu.

Đây giống decision under sunk cost:

```text
cost tiếp tục plan hiện tại
vs
cost dừng + chuyển + chạy plan mới
```

Re-optimization trigger quá nhạy có thể oscillate hoặc làm execution khó dự đoán.

## 11. Parameter-sensitive behavior

Cùng SQL text nhưng parameter khác có thể cần plan khác. Query lấy một customer cụ thể khác query lấy toàn bộ region. Nếu cache một plan cho mọi parameter, một execution đầu tiên có thể “đóng băng” assumption không phù hợp các execution sau.

Adaptive execution giảm một phần risk bằng runtime evidence, nhưng compile-time plan caching và runtime adaptation là hai layer khác nhau. Cần quan sát cả estimated/actual cardinality và parameter cohort.

## 12. Distributed execution và network

Trong analytical engine phân tán, exchange/shuffle là boundary vừa về data vừa về network. Adaptive partition count ảnh hưởng connection count, buffer, serialization và congestion.

Một plan giảm CPU nhưng tăng shuffle có thể tệ khi network saturated. Ngược lại, broadcast tránh repartition nhưng nhân bản bytes theo worker count.

Cost model runtime cần hiểu resource đang scarce ở thời điểm đó; “cheapest plan” không cố định nếu cluster pressure thay đổi.

## 13. Failure modes

**Late adaptation:** phát hiện estimate sai khi phần lớn expensive work đã xảy ra.

**Thrashing:** controller đổi strategy quá thường xuyên do threshold/noise.

**Skew hidden by averages:** tổng bytes bình thường nhưng một partition quyết định tail.

**Runtime filter too late:** filter đúng nhưng arrival sau scan nên gần như vô ích.

**Unsafe pruning:** filter implementation tạo false negative làm sai result.

**Spill cascade:** nhiều query đồng thời vượt memory, cùng spill và làm storage saturated.

**Adaptive herd:** nhiều query cùng thấy cluster state rồi đồng thời chọn strategy giống nhau, tạo bottleneck mới.

## 14. Production evidence

Execution plan phải được đọc cùng runtime counters:

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

Một plan diagram không có actual cardinality chỉ cho biết optimizer đã tin gì, chưa cho biết runtime đã xảy ra gì.

## 15. Worked reasoning case

Giả sử dashboard query bình thường 8 giây bỗng thành 90 giây sau khi data tăng.

Plan cho thấy optimizer chọn broadcast join. Estimated build side 40 MB, actual 1.8 GB. Worker memory tăng, một số spill; network outbound tăng mạnh. Runtime filter chỉ xuất hiện sau khi probe scan gần hoàn tất.

Reasoning chain:

```text
stale/correlated statistics
→ underestimate build cardinality
→ broadcast decision sai
→ replicated memory/network pressure
→ spill
→ runtime filter tới muộn
→ tail latency tăng mạnh
```

Fix có thể nằm ở statistics, plan policy, adaptive broadcast threshold hoặc stage scheduling. Tăng machine memory chỉ che symptom nếu estimator tiếp tục sai.

## 16. Connection với các chapter khác

Đọc chapter này sau [cost-based optimizer](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md), [join/vectorized execution](./06_join_algorithms_vectorized_execution_and_late_materialization.md) và [columnar storage](./08_columnar_storage_encoding_pruning_and_vectorized_scans.md).

Ở tầng hệ thống, adaptive execution nối với [queueing/backpressure](../../08_software_systems/advanced/00_queueing_backpressure_and_overload_control.md) và [fleet profiling/cost attribution](../../08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md).

Mental model cuối cùng:

```text
optimizer = decision under incomplete information
runtime = evidence
adaptive execution = controlled revision at safe boundary
correctness invariant = logical result không đổi
performance goal = tránh catastrophic mismatch giữa estimate và reality
```

Đây là bước chuyển từ “optimizer chọn plan tốt” sang hiểu database như một **feedback system** quan sát execution và sửa assumption khi đủ evidence.