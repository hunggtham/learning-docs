# Fleet profiling, cost attribution và multi-tenant efficiency

Đọc trước [Capacity planning, utilization knee và admission control](./01_capacity_planning_utilization_knee_and_admission_control.md) và [Queueing, tail latency, backpressure](./00_queueing_tail_latency_and_backpressure.md). Chapter này mở rộng từ một service instance sang một **fleet**: hàng trăm hoặc hàng nghìn processes/VMs/containers/accelerators chạy nhiều versions, regions, hardware types và tenants.

Ở quy mô này, câu hỏi không còn chỉ là “CPU có cao không?” mà là:

> Resource nào đang tạo useful outcome, resource nào là headroom cần thiết, resource nào bị lãng phí vì skew/fragmentation, và cost được tạo bởi workload/tenant/version nào?

Mental model:

```text
user/business demand
→ request/work unit
→ distributed critical path
→ resource consumption across fleet
→ useful outcome / SLO
→ cost attribution
→ capacity / placement / architecture decision
```

## 1. Trung bình fleet có thể che failure local

Giả sử average CPU toàn fleet là 45%. Điều đó không nói được một availability zone có instances ở 95%, một shard đang nóng hoặc một hardware cohort đang throttling.

Aggregation càng lớn càng dễ che skew. Do đó production analysis cần giữ dimensions có causal value như region, zone, version, instance type, shard, tenant, endpoint và workload class.

Nhưng dimensions quá nhiều tạo cardinality explosion. Observability design là trade-off giữa diagnosability và cost.

## 2. Fleet heterogeneity làm benchmark đơn lẻ mất đại diện

Cùng service binary có thể chạy trên CPU generations khác nhau, NUMA topology khác nhau, memory bandwidth khác nhau hoặc cloud instance noisy-neighbor khác nhau.

Một p50 benchmark trên lab machine không đại diện cho production distribution. Cần compare cohorts và normalize theo useful work.

Ví dụ metric tốt hơn “requests/sec/host” có thể là:

```text
successful requests under SLO / vCPU-second
```

hoặc với batch:

```text
records processed correctly / dollar
```

## 3. Cost per useful outcome tốt hơn raw resource cost

Một instance rẻ hơn 20% nhưng làm p99 vượt SLO và tạo retries có thể đắt hơn tổng thể.

Useful-outcome cost phải tính cả unsuccessful work:

```text
compute
+ memory
+ storage I/O
+ network egress
+ retries
+ replication
+ observability
+ idle headroom needed for reliability
```

Mục tiêu không phải minimize từng line item mà minimize cost với invariant SLO/correctness/security vẫn giữ.

## 4. Headroom không phải waste mặc định

Nếu traffic burst nhanh hơn autoscaler, fleet cần spare capacity để hấp thụ shock. Nếu failover một zone yêu cầu các zone còn lại gánh traffic, headroom là insurance cho failure model.

Do đó utilization target phải gắn với recovery requirement:

```text
steady-state utilization
+ expected burst
+ failure reserve
< utilization knee
```

Chạy 95% mọi lúc có thể nhìn “efficient” nhưng làm system brittle.

## 5. Bin packing có thể tăng efficiency và tăng blast radius cùng lúc

Packing nhiều workloads lên cùng hosts giảm idle fragmentation. Nhưng co-location tạo shared failure domain và noisy-neighbor risk.

Một scheduler tối ưu cost cần cân CPU, memory, I/O, network, NUMA/accelerator locality và anti-affinity. Packing chỉ theo CPU request dễ tạo memory-bandwidth hoặc I/O hotspot.

## 6. Requested resources và actual demand là hai distribution khác nhau

Containers thường khai báo requests/limits. Nếu request quá cao, scheduler để trống capacity dù workload không dùng. Nếu request quá thấp, node overcommit và pressure bất ngờ.

Rightsizing không nên lấy peak một ngày rồi set cứng. Cần distribution theo time, SLO sensitivity và burst behavior.

Memory khác CPU: CPU có thể throttle, còn memory exhaustion có thể OOM/evict. Vì vậy overcommit semantics khác nhau theo resource.

## 7. Noisy neighbor là multi-resource contention

Hai tenants có thể không cạnh tranh CPU nhưng vẫn tranh LLC, memory bandwidth, disk queue, NIC, connection pool hoặc downstream quota.

Symptoms thường là tail latency tăng theo co-location pattern chứ không theo request rate riêng của victim.

Evidence cần correlation giữa placement và lower-layer contention, không chỉ application metrics.

## 8. Multi-tenant fairness cần định nghĩa work unit

Fairness theo request count có thể sai nếu requests cost khác nhau 100×. Fairness theo CPU time có thể bỏ qua memory/network pressure.

Hệ thống có thể dùng weighted quotas, concurrency limits, token buckets hoặc dominant-resource style accounting tùy invariant.

Câu hỏi trước algorithm là: **tenant đang được chia công bằng theo thứ gì?**

## 9. Cost attribution trong shared system không hoàn toàn “đo trực tiếp” được

Một database cluster dùng chung có fixed baseline, shared cache và background compaction. Không thể luôn gán chính xác từng byte RAM cho một tenant.

Attribution thường cần model:

```text
fixed shared cost
+ directly metered cost
+ allocated shared cost
```

Allocation key có thể là CPU time, storage bytes, request weight, rows scanned hoặc business unit. Đây là accounting model; cần công khai assumption để tránh biến estimate thành “fact”.

## 10. Chargeback và showback tạo behavioral feedback

**Showback** hiển thị cost theo team/tenant nhưng không billing trực tiếp. **Chargeback** đưa cost vào budget/accounting.

Hai cơ chế có thể thay đổi behavior, đôi khi theo hướng xấu nếu metric dễ game. Ví dụ team giảm logs quan trọng chỉ để giảm bill observability.

Cost metric vì vậy cần guardrail về reliability/security.

## 11. Distributed tracing không phải fleet profiler hoàn chỉnh

Trace cho biết critical path của sampled requests. Continuous profiling cho biết CPU/stack behavior theo thời gian. Metrics cho biết aggregate rates/queues. Logs cung cấp discrete events.

Mỗi signal có blind spots. Fleet diagnosis thường cần kết hợp:

```text
trace: request đi đâu?
profile: CPU làm gì?
metric: pressure/rate thay đổi ra sao?
log/event: state transition nào xảy ra?
```

## 12. Sampling có thể bias dữ liệu cost/performance

Nếu trace sampling chỉ random 1%, rare slow requests có thể bị thiếu. Tail-based sampling giữ slow/error traces tốt hơn nhưng tốn buffer và có selection bias cho workload analysis.

Profiler sampling interval cũng ảnh hưởng visibility của short-lived functions.

Evidence pipeline phải biết sampling policy, không coi sampled distribution như full population mặc định.

## 13. Version/cohort comparison là công cụ mạnh nhất khi rollout

Khi version mới rollout 10%, compare cost/SLO theo cùng workload cohort giúp phân biệt code regression với traffic seasonality.

Cần normalize theo request mix và hardware. Nếu version mới vô tình chạy chủ yếu trên hardware nhanh hơn, raw latency comparison đánh lừa.

Useful experiment design:

```text
same region
same hardware class
similar request mix
old vs new version
→ compare service time / allocation / downstream calls / success under SLO
```

## 14. Tail latency ở fleet level thường đến từ minority cohort

p99 global có thể do một zone, shard, dependency pool hoặc tenant cực nhỏ. Average profile của toàn fleet pha loãng signal.

Một workflow tốt là:

```text
SLO tail cohort
→ identify dimensions correlated with tail
→ narrow to hosts/processes
→ on/off-CPU profile
→ lower-layer evidence
```

Không profile toàn fleet rồi hy vọng hot stack tự lộ rõ.

## 15. Cost regression có thể không đi cùng latency regression

Version mới có cùng latency nhưng allocate gấp đôi, tăng GC frequency và yêu cầu nhiều hosts để giữ headroom. Nếu chỉ monitor SLO, regression kinh tế bị bỏ sót.

Ngược lại version dùng thêm CPU nhưng giảm storage/network cost nhiều hơn có thể tốt tổng thể.

Performance và cost phải được đọc theo outcome, không theo một resource riêng.

## 16. Autoscaling là feedback controller nên có oscillation risk

Nếu scaler nhìn metric trễ, scale-out chậm, cooldown sai hoặc workload burst theo period gần response time của controller, fleet có thể oscillate:

```text
load ↑
→ queue ↑
→ scale-out
→ load already dropped
→ overcapacity
→ scale-in
→ next burst hits reduced fleet
```

Scaling policy cần xét measurement lag, provisioning time và queue dynamics. Đọc cùng chapter capacity/admission thay vì coi autoscaling là magic elasticity.

## 17. Scale-to-zero đổi cost lấy cold-start tail

Serverless hoặc batch workers có thể về zero khi idle. Cost baseline giảm nhưng first request trả cold-start cost: image load, runtime init, JIT, connection warmup, cache miss.

Nếu SLO không chấp nhận cold start, phải giữ warm capacity hoặc prewarm dựa forecast.

Efficiency là trade-off state, không phải một con số.

## 18. Accelerator/GPU utilization cần nhìn memory và queue chứ không chỉ compute %

AI/graphics/HPC workload có thể bottleneck ở HBM bandwidth, host-device transfer, batch formation hoặc kernel launch overhead.

Accelerator “utilization cao” chưa chắc useful tokens/samples cao nếu queueing hoặc memory stalls dominate.

Cost per token/sample dưới latency target là metric gần outcome hơn device utilization đơn lẻ.

## 19. Carbon/energy có thể là dimension nhưng không nên thay SLO/security

Energy per useful request có thể quan trọng ở fleet lớn. DVFS, hardware generation và region energy mix ảnh hưởng. Tuy nhiên optimization năng lượng không được làm mất availability reserve hoặc data-residency constraint.

Đây là thêm một resource/economic dimension, không phải mục tiêu tuyệt đối.

## 20. Worked example: CPU thấp nhưng fleet vẫn cần scale-out

Một API fleet CPU chỉ 35%, nhưng p99 tăng. Trace cho thấy phần lớn request chờ DB connection pool. Pool active chạm max; DB downstream gần saturation.

Scale-out API tạo thêm pools, có thể làm DB overload nặng hơn. CPU headroom ở tier A không có ý nghĩa nếu bottleneck ở shared tier B.

Correct action có thể là admission limit, query optimization hoặc DB capacity—not “thêm app instances”.

## 21. Worked example: tenant scan làm tăng bill toàn cluster

Một analytical tenant chạy query scan rất rộng. CPU cluster tăng vừa phải nhưng object-storage read và network shuffle tăng mạnh; cache bị evict, làm tenants khác đọc chậm hơn.

Attribution cần bytes scanned/shuffled và cache impact, không chỉ request count. Quota có thể dựa scan bytes/concurrency; chargeback/showback làm cost visible. Nhưng query optimizer/pruning mới là fix giảm useful-work waste.

## 22. Production evidence

Một fleet-level investigation nên giữ các dimensions:

```text
service/version/region/zone
hardware/instance type
host/node
shard/partition
endpoint/workload class
tenant
resource pressure
queue/wait
success + SLO outcome
cost unit
```

Sau đó drill down thay vì export mọi dimension vào một metric cardinality vô hạn.

## 23. Kết nối sang các chapter khác

Fleet profiling nối với [capacity planning](./01_capacity_planning_utilization_knee_and_admission_control.md), [load balancing/locality](./03_load_balancing_connection_pools_and_locality.md), [multi-region tradeoffs](../../06_networks_distributed_systems/advanced/05_multi_region_replication_and_geo_distributed_tradeoffs.md), [deployment canary](../../09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md) và [debugging xuyên layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

Mental model cuối cùng: **fleet efficiency là tối ưu cost của useful outcome dưới SLO/failure/security constraints, không phải ép mọi resource lên 100% utilization.**