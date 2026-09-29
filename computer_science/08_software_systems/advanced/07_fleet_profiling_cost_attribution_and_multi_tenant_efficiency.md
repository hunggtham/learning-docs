# Fleet profiling, chi phí (cost / 비용) attribution và multi-tenant efficiency

> **Mạch đọc:** Đặt **Fleet profiling, chi phí (cost / 비용) attribution và multi-tenant efficiency** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Trung bình fleet có thể che thất bại (failure / 실패) cục bộ (local / 로컬)** sang **2. Fleet heterogeneity làm benchmark đơn lẻ mất đại diện**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Đọc trước [Capacity planning, utilization knee và admission control](./01_capacity_planning_utilization_knee_and_admission_control.md) và [Queueing, tail latency, backpressure](./00_queueing_tail_latency_and_backpressure.md). Chapter này mở rộng từ một dịch vụ (service / 서비스) instance sang một **fleet**: hàng trăm hoặc hàng nghìn processes/VMs/containers/accelerators chạy nhiều versions, regions, hardware types và tenants.

Ở quy mô này, câu hỏi không còn chỉ là “CPU có cao không?” mà là:

> tài nguyên (resource / 자원) nào đang tạo useful kết quả (outcome / 결과), tài nguyên (resource / 자원) nào là headroom cần thiết, tài nguyên (resource / 자원) nào bị lãng phí vì skew/fragmentation, và chi phí (cost / 비용) được tạo bởi tải công việc (workload / 워크로드)/tenant/phiên bản (version / 버전) nào?

Mô hình tư duy (mental model / 사고 모델):

```text
user/business demand
→ request/work unit
→ distributed critical path
→ resource consumption across fleet
→ useful outcome / SLO
→ cost attribution
→ capacity / placement / architecture decision
```

## 1. Trung bình fleet có thể che thất bại (failure / 실패) cục bộ (local / 로컬)

Giả sử average CPU toàn fleet là 45%. Điều đó không nói được một availability zone có instances ở 95%, một shard đang nóng hoặc một hardware cohort đang throttling.

Aggregation càng lớn càng dễ che skew. Do đó môi trường vận hành (production / 운영 환경) phân tích (analysis / 분석) cần giữ dimensions có nhân quả (causal / 인과적) giá trị (value / 값) như region, zone, phiên bản (version / 버전), instance kiểu (type / 타입), shard, tenant, endpoint và tải công việc (workload / 워크로드) lớp (class / 클래스).

Nhưng dimensions quá nhiều tạo cardinality explosion. khả năng quan sát (observability / 관측 가능성) thiết kế (design / 설계) là sự đánh đổi (trade-off / 트레이드오프) giữa diagnosability và chi phí (cost / 비용).

## 2. Fleet heterogeneity làm benchmark đơn lẻ mất đại diện

Cùng dịch vụ (service / 서비스) nhị phân (binary / 이진) có thể chạy trên CPU generations khác nhau, NUMA topology khác nhau, bộ nhớ (memory / 메모리) bandwidth khác nhau hoặc cloud instance noisy-neighbor khác nhau.

Một p50 benchmark trên lab machine không đại diện cho môi trường vận hành (production / 운영 환경) phân phối (distribution / 분포). Cần compare cohorts và normalize theo useful công việc (work / 작업).

Ví dụ chỉ số (metric / 지표) tốt hơn “requests/sec/host” có thể là:

```text
successful requests under SLO / vCPU-second
```

hoặc với batch:

```text
records processed correctly / dollar
```

## 3. chi phí (cost / 비용) per useful kết quả (outcome / 결과) tốt hơn raw tài nguyên (resource / 자원) chi phí (cost / 비용)

Một instance rẻ hơn 20% nhưng làm p99 vượt SLO và tạo retries có thể đắt hơn tổng thể.

Useful-outcome chi phí (cost / 비용) phải tính cả unsuccessful công việc (work / 작업):

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

Mục tiêu không phải minimize từng line item mà minimize chi phí (cost / 비용) với bất biến (invariant / 불변식) SLO/tính đúng đắn (correctness / 정확성)/bảo mật (security / 보안) vẫn giữ.

## 4. Headroom không phải waste mặc định

Nếu traffic burst nhanh hơn autoscaler, fleet cần spare sức chứa (capacity / 용량) để hấp thụ shock. Nếu failover một zone yêu cầu các zone còn lại gánh traffic, headroom là insurance cho thất bại (failure / 실패) mô hình (model / 모델).

Do đó utilization mục tiêu (target / 대상) phải gắn với khôi phục (recovery / 복구) yêu cầu (requirement / 요구사항):

```text
steady-state utilization
+ expected burst
+ failure reserve
< utilization knee
```

Chạy 95% mọi lúc có thể nhìn “efficient” nhưng làm hệ thống (system / 시스템) brittle.

## 5. Bin packing có thể tăng efficiency và tăng blast radius cùng lúc

Packing nhiều workloads lên cùng hosts giảm idle fragmentation. Nhưng co-location tạo dùng chung (shared / 공유) miền lỗi (failure domain / 장애 도메인) và noisy-neighbor rủi ro (risk / 위험).

Một scheduler tối ưu chi phí (cost / 비용) cần cân CPU, bộ nhớ (memory / 메모리), I/O, mạng (network / 네트워크), NUMA/accelerator locality và anti-affinity. Packing chỉ theo CPU yêu cầu (request / 요청) dễ tạo memory-bandwidth hoặc I/O hotspot.

## 6. Requested resources và actual demand là hai phân phối (distribution / 분포) khác nhau

Containers thường khai báo requests/limits. Nếu yêu cầu (request / 요청) quá cao, scheduler để trống sức chứa (capacity / 용량) dù tải công việc (workload / 워크로드) không dùng. Nếu yêu cầu (request / 요청) quá thấp, nút (node / 노드) overcommit và pressure bất ngờ.

Rightsizing không nên lấy peak một ngày rồi set cứng. Cần phân phối (distribution / 분포) theo thời gian (time / 시간), SLO sensitivity và burst hành vi (behavior / 동작).

Bộ nhớ (memory / 메모리) khác CPU: CPU có thể throttle, còn bộ nhớ (memory / 메모리) exhaustion có thể OOM/evict. Vì vậy overcommit ngữ nghĩa (semantics / 의미론) khác nhau theo tài nguyên (resource / 자원).

## 7. Noisy neighbor là multi-resource contention

Hai tenants có thể không cạnh tranh CPU nhưng vẫn tranh LLC, bộ nhớ (memory / 메모리) bandwidth, disk hàng đợi (queue / 큐), NIC, liên kết (connection / 연결) pool hoặc downstream quota.

Symptoms thường là tail độ trễ (latency / 지연 시간) tăng theo co-location mẫu (pattern / 패턴) chứ không theo yêu cầu (request / 요청) tỷ lệ (rate / 비율) riêng của victim.

Bằng chứng (evidence / 증거) cần correlation giữa placement và lower-layer contention, không chỉ ứng dụng (application / 애플리케이션) metrics.

## 8. Multi-tenant fairness cần định nghĩa công việc (work / 작업) đơn vị (unit / 단위)

Fairness theo yêu cầu (request / 요청) count có thể sai nếu requests chi phí (cost / 비용) khác nhau 100×. Fairness theo CPU thời gian (time / 시간) có thể bỏ qua bộ nhớ (memory / 메모리)/mạng (network / 네트워크) pressure.

Hệ thống có thể dùng weighted quotas, tính đồng thời (concurrency / 동시성) limits, đơn vị từ (token / 토큰) buckets hoặc dominant-resource style accounting tùy bất biến (invariant / 불변식).

Câu hỏi trước thuật toán (algorithm / 알고리즘) là: **tenant đang được chia công bằng theo thứ gì?**

## 9. chi phí (cost / 비용) attribution trong dùng chung (shared / 공유) hệ thống (system / 시스템) không hoàn toàn “đo trực tiếp” được

Một cơ sở dữ liệu (database / 데이터베이스) cluster dùng chung có fixed baseline, dùng chung (shared / 공유) bộ nhớ đệm (cache / 캐시) và background compaction. Không thể luôn gán chính xác từng byte RAM cho một tenant.

Attribution thường cần mô hình (model / 모델):

```text
fixed shared cost
+ directly metered cost
+ allocated shared cost
```

Allocation key có thể là CPU thời gian (time / 시간), lưu trữ (storage / 저장소) bytes, yêu cầu (request / 요청) weight, rows scanned hoặc nghiệp vụ (business / 비즈니스) đơn vị (unit / 단위). Đây là accounting mô hình (model / 모델); cần công khai giả định (assumption / 가정) để tránh biến estimate thành “fact”.

## 10. Chargeback và showback tạo behavioral phản hồi (feedback / 피드백)

**Showback** hiển thị chi phí (cost / 비용) theo nhóm (team / 팀)/tenant nhưng không billing trực tiếp. **Chargeback** đưa chi phí (cost / 비용) vào ngân sách (budget / 예산)/accounting.

Hai cơ chế có thể thay đổi hành vi (behavior / 동작), đôi khi theo hướng xấu nếu chỉ số (metric / 지표) dễ game. Ví dụ nhóm (team / 팀) giảm logs quan trọng chỉ để giảm bill khả năng quan sát (observability / 관측 가능성).

Chi phí (cost / 비용) chỉ số (metric / 지표) vì vậy cần guardrail về độ tin cậy (reliability / 신뢰성)/bảo mật (security / 보안).

## 11. phân tán (distributed / 분산) tracing không phải fleet profiler hoàn chỉnh

Dấu vết (trace / 추적) cho biết đường găng (critical path / 임계 경로) của sampled requests. Continuous profiling cho biết CPU/ngăn xếp (stack / 스택) hành vi (behavior / 동작) theo thời gian. Metrics cho biết aggregate rates/queues. Logs cung cấp discrete events.

Mỗi tín hiệu (signal / 신호) có blind spots. Fleet diagnosis thường cần kết hợp:

```text
trace: request đi đâu?
profile: CPU làm gì?
metric: pressure/rate thay đổi ra sao?
log/event: state transition nào xảy ra?
```

## 12. Sampling có thể độ lệch (bias / 편향) dữ liệu chi phí (cost / 비용)/hiệu năng (performance / 성능)

Nếu dấu vết (trace / 추적) sampling chỉ random 1%, rare slow requests có thể bị thiếu. Tail-based sampling giữ slow/lỗi (error / 오류) traces tốt hơn nhưng tốn buffer và có selection độ lệch (bias / 편향) cho tải công việc (workload / 워크로드) phân tích (analysis / 분석).

Profiler sampling interval cũng ảnh hưởng visibility của short-lived functions.

Bằng chứng (evidence / 증거) chuỗi xử lý (pipeline / 파이프라인) phải biết sampling chính sách (policy / 정책), không coi sampled phân phối (distribution / 분포) như full population mặc định.

## 13. phiên bản (version / 버전)/cohort comparison là công cụ mạnh nhất khi rollout

Khi phiên bản (version / 버전) mới rollout 10%, compare chi phí (cost / 비용)/SLO theo cùng tải công việc (workload / 워크로드) cohort giúp phân biệt mã (code / 코드) regression với traffic seasonality.

Cần normalize theo yêu cầu (request / 요청) mix và hardware. Nếu phiên bản (version / 버전) mới vô tình chạy chủ yếu trên hardware nhanh hơn, raw độ trễ (latency / 지연 시간) comparison đánh lừa.

Useful experiment thiết kế (design / 설계):

```text
same region
same hardware class
similar request mix
old vs new version
→ compare service time / allocation / downstream calls / success under SLO
```

## 14. Tail độ trễ (latency / 지연 시간) ở fleet mức (level / 수준) thường đến từ minority cohort

p99 toàn cục (global / 전역) có thể do một zone, shard, phụ thuộc (dependency / 의존성) pool hoặc tenant cực nhỏ. Average profile của toàn fleet pha loãng tín hiệu (signal / 신호).

Một workflow tốt là:

```text
SLO tail cohort
→ identify dimensions correlated with tail
→ narrow to hosts/processes
→ on/off-CPU profile
→ lower-layer evidence
```

Không profile toàn fleet rồi hy vọng hot ngăn xếp (stack / 스택) tự lộ rõ.

## 15. chi phí (cost / 비용) regression có thể không đi cùng độ trễ (latency / 지연 시간) regression

Phiên bản (version / 버전) mới có cùng độ trễ (latency / 지연 시간) nhưng allocate gấp đôi, tăng GC frequency và yêu cầu nhiều hosts để giữ headroom. Nếu chỉ monitor SLO, regression kinh tế bị bỏ sót.

Ngược lại phiên bản (version / 버전) dùng thêm CPU nhưng giảm lưu trữ (storage / 저장소)/mạng (network / 네트워크) chi phí (cost / 비용) nhiều hơn có thể tốt tổng thể.

Hiệu năng (performance / 성능) và chi phí (cost / 비용) phải được đọc theo kết quả (outcome / 결과), không theo một tài nguyên (resource / 자원) riêng.

## 16. Autoscaling là phản hồi (feedback / 피드백) controller nên có oscillation rủi ro (risk / 위험)

Nếu scaler nhìn chỉ số (metric / 지표) trễ, scale-out chậm, cooldown sai hoặc tải công việc (workload / 워크로드) burst theo period gần phản hồi (response / 응답) thời gian (time / 시간) của controller, fleet có thể oscillate:

```text
load ↑
→ queue ↑
→ scale-out
→ load already dropped
→ overcapacity
→ scale-in
→ next burst hits reduced fleet
```

Scaling chính sách (policy / 정책) cần xét đo lường (measurement / 측정) lag, provisioning thời gian (time / 시간) và hàng đợi (queue / 큐) dynamics. Đọc cùng chapter sức chứa (capacity / 용량)/admission thay vì coi autoscaling là magic elasticity.

## 17. Scale-to-zero đổi chi phí (cost / 비용) lấy cold-start tail

Serverless hoặc batch workers có thể về zero khi idle. chi phí (cost / 비용) baseline giảm nhưng first yêu cầu (request / 요청) trả cold-start chi phí (cost / 비용): ảnh (image / 이미지) tải (load / 로드), thời gian chạy (runtime / 런타임) init, JIT, liên kết (connection / 연결) warmup, trượt bộ nhớ đệm (cache miss / 캐시 미스).

Nếu SLO không chấp nhận cold start, phải giữ warm sức chứa (capacity / 용량) hoặc prewarm dựa forecast.

Efficiency là sự đánh đổi (trade-off / 트레이드오프) trạng thái (state / 상태), không phải một con số.

## 18. Accelerator/GPU utilization cần nhìn bộ nhớ (memory / 메모리) và hàng đợi (queue / 큐) chứ không chỉ compute %

AI/graphics/HPC tải công việc (workload / 워크로드) có thể bottleneck ở HBM bandwidth, host-device transfer, batch formation hoặc kernel launch overhead.

Accelerator “utilization cao” chưa chắc useful tokens/samples cao nếu queueing hoặc bộ nhớ (memory / 메모리) stalls dominate.

Chi phí (cost / 비용) per đơn vị từ (token / 토큰)/mẫu (sample / 표본) dưới độ trễ (latency / 지연 시간) mục tiêu (target / 대상) là chỉ số (metric / 지표) gần kết quả (outcome / 결과) hơn thiết bị (device / 장치) utilization đơn lẻ.

## 19. Carbon/năng lượng (energy / 에너지) có thể là dimension nhưng không nên thay SLO/bảo mật (security / 보안)

Năng lượng (energy / 에너지) per useful yêu cầu (request / 요청) có thể quan trọng ở fleet lớn. DVFS, hardware generation và region năng lượng (energy / 에너지) mix ảnh hưởng. Tuy nhiên tối ưu hóa (optimization / 최적화) năng lượng không được làm mất availability reserve hoặc data-residency ràng buộc (constraint / 제약조건).

Đây là thêm một tài nguyên (resource / 자원)/economic dimension, không phải mục tiêu tuyệt đối.

## 20. Worked example: CPU thấp nhưng fleet vẫn cần scale-out

Một API fleet CPU chỉ 35%, nhưng p99 tăng. dấu vết (trace / 추적) cho thấy phần lớn yêu cầu (request / 요청) chờ DB liên kết (connection / 연결) pool. Pool active chạm max; DB downstream gần saturation.

Scale-out API tạo thêm pools, có thể làm DB overload nặng hơn. CPU headroom ở tier A không có ý nghĩa nếu bottleneck ở dùng chung (shared / 공유) tier B.

Correct hành động (action / 동작) có thể là admission limit, truy vấn (query / 쿼리) tối ưu hóa (optimization / 최적화) hoặc DB sức chứa (capacity / 용량)—not “thêm app instances”.

## 21. Worked example: tenant scan làm tăng bill toàn cluster

Một analytical tenant chạy truy vấn (query / 쿼리) scan rất rộng. CPU cluster tăng vừa phải nhưng object-storage read và mạng (network / 네트워크) shuffle tăng mạnh; bộ nhớ đệm (cache / 캐시) bị evict, làm tenants khác đọc chậm hơn.

Attribution cần bytes scanned/shuffled và bộ nhớ đệm (cache / 캐시) impact, không chỉ yêu cầu (request / 요청) count. Quota có thể dựa scan bytes/tính đồng thời (concurrency / 동시성); chargeback/showback làm chi phí (cost / 비용) visible. Nhưng truy vấn (query / 쿼리) optimizer/pruning mới là fix giảm useful-work waste.

## 22. bằng chứng vận hành (production evidence / 운영 증거)

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

Sau đó drill down thay vì export mọi dimension vào một chỉ số (metric / 지표) cardinality vô hạn.

## 23. Kết nối sang các chapter khác

Fleet profiling nối với [capacity planning](./01_capacity_planning_utilization_knee_and_admission_control.md), [load balancing/locality](./03_load_balancing_connection_pools_and_locality.md), [multi-region tradeoffs](../../06_networks_distributed_systems/advanced/05_multi_region_replication_and_geo_distributed_tradeoffs.md), [deployment canary](../../09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md) và [debugging xuyên layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

Mô hình tư duy (mental model / 사고 모델) cuối cùng: **fleet efficiency là tối ưu chi phí (cost / 비용) của useful kết quả (outcome / 결과) dưới SLO/thất bại (failure / 실패)/bảo mật (security / 보안) các ràng buộc (constraints / 제약조건들), không phải ép mọi tài nguyên (resource / 자원) lên 100% utilization.**

> **Bàn giao:** Sau **23. Kết nối sang các chapter khác**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 queueing tail latency and backpressure](./00_queueing_tail_latency_and_backpressure.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
