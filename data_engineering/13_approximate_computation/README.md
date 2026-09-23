# 13 — Approximate computation và error bounds

Approximate computation là cách đổi một phần exactness lấy latency, memory hoặc cost có giới hạn. Nó chỉ đúng khi error được định nghĩa, đo được và phù hợp với quyết định của consumer.

## 1. Exact không phải lúc nào cũng là mục tiêu tối ưu

`COUNT(DISTINCT user_id)` trên hàng tỷ row có thể cần state lớn hoặc shuffle lớn. Một estimate nhanh với sai số ±1% có thể đủ cho capacity planning nhưng không đủ cho billing. Contract phải nêu rõ metric này là estimate hay source of truth.

## 2. Sketch phải merge được

Trong distributed system, mỗi worker tạo partial sketch rồi merge:

```text
input → local sketch_1 ... sketch_n → merge → estimate + bound
```

Merge operation cần associative/commutative để retry và partition order không thay đổi kết quả ngoài bound. Sketch state phải có version, parameter và hash function ổn định; đổi chúng giữa run làm estimate không comparable.

## 3. Cardinality và quantile

Distinct sketch như HyperLogLog lưu register thay vì mọi identity. Sai số phụ thuộc số register, bias correction và hash distribution. Quantile sketch phải phân biệt rank error với value error: ±1% percentile rank không đồng nghĩa giá trị nằm trong ±1%.

Không dùng average của percentile từ từng partition để suy ra percentile toàn cục. Cần merge sketch hoặc giữ weighted distribution phù hợp.

## 4. Sampling

Random sample đơn giản nhưng dễ bias nếu sampling theo partition, tenant hoặc thời gian. Stratified sampling bảo vệ nhóm nhỏ nhưng cần allocation và weight đúng. Mọi estimate phải lưu sampling frame, seed, rate và confidence interval.

## 5. Error contract

Một approximate metric cần metadata:

```text
estimate + error definition + confidence/bound
→ method/version + input scope + freshness
```

Không ghi một số estimate vào cột `count` như thể exact. Serving layer nên hiển thị uncertainty khi quyết định có thể bị ảnh hưởng bởi bound.

## 6. Failure và evidence

- hash collision hoặc input distribution bất thường;
- sketch version đổi làm số liệu nhảy;
- merge thiếu một partition nhưng job vẫn xanh;
- sample bỏ sót heavy hitter;
- estimate bị cache lâu hơn freshness contract.

Evidence cần có exact sample đối chiếu, error distribution theo segment, canary run, sketch metadata và reconciliation khi có thể.

## 7. Khi nào không được approximate

Billing, entitlement, compliance count, deletion audit và financial ledger thường cần exact hoặc quy trình correction rõ. Approximation có thể dùng cho monitoring/triage nhưng không được âm thầm thay source of truth.

Đọc tiếp: [06 — Distributed processing](../06_distributed_processing/README.md), [10 — Serving](../10_serving_semantic_layer/README.md), [12 — Cost](../12_cost_performance_capacity/README.md).
