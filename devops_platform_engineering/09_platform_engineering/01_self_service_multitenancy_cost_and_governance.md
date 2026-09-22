# Self-service, multi-tenancy, governance và FinOps

## 1. Self-service là delegated control có boundary

Self-service không nghĩa ai cũng có admin. Nó nghĩa user có thể hoàn thành common task trong một permission envelope đã thiết kế: tạo service, database plan, secret binding hoặc environment mà không chờ operator thao tác.

Platform nhận intent mức cao, validate policy, thực hiện provisioning bằng automation identity và trả status. Đây là delegated control.

## 2. API cần thể hiện intent

Nếu developer muốn “một internal HTTP service” nhưng phải khai VPC ID, subnet, security group, node selector và IAM ARN, platform đang expose implementation.

Intent-level API giảm coupling. Platform có thể đổi underlying implementation mà consumer contract ít thay hơn.

Tuy nhiên intent phải đủ rõ cho reliability/cost. User vẫn có thể cần chọn tier, region, data classification, expected traffic hoặc RPO/RTO.

## 3. Multi-tenancy là shared resource + isolation contract

Nhiều team có thể dùng chung cluster, CI runner, registry hoặc observability backend. Multi-tenancy tiết kiệm và chuẩn hóa nhưng tạo noisy neighbor/security risk.

Isolation có nhiều chiều: identity/RBAC, network, compute quota, storage, secret, observability data và billing attribution. Namespace chỉ giải một phần.

## 4. Quota là product feature

Quota ngăn một tenant tiêu hết shared capacity, nhưng quota quá thấp tạo support ticket. Platform cần default theo workload class và cách request increase có reason/approval tự động phù hợp.

Quota usage phải visible cho tenant trước khi chạm limit. Error “quota exceeded” chỉ khi deploy là feedback quá muộn.

## 5. Resource fairness và noisy neighbor

Shared cluster có thể gặp CPU, memory, I/O, network hoặc API-server contention. Request/limit, priority, rate limit và dedicated pool là các công cụ.

Không phải tenant nào cũng cần isolation vật lý. Chọn boundary dựa trên risk/compliance/performance. Dedicated cluster per team có isolation nhưng tăng cost/operational surface.

## 6. Environment strategy

Dev/staging/prod có thể tách account/project/cluster hoặc chia namespace tùy risk. Production thường cần stronger boundary. Nhưng càng nhiều environment giống hệt production càng tốn cost và drift risk.

Mục tiêu của pre-production là tạo confidence cho change, không phải sao chép mọi thứ vô điều kiện. Ephemeral environment có thể phù hợp feature/integration test; long-lived staging phù hợp shared dependency test.

## 7. Governance bằng metadata

Mọi resource nên có owner, environment, service/product, cost center/team, data classification và lifecycle/expiry khi phù hợp. Metadata cho phép policy, cost allocation và cleanup.

Nếu resource không có owner, incident/security/cost question đều khó. Platform nên inject/require metadata thay vì mong user nhớ tag bằng tay.

## 8. FinOps là feedback loop về cost

Cloud bill chỉ hữu ích khi cost được gắn với owner và driver. “Team A tốn 20 triệu” chưa đủ; cần biết compute idle, data egress, database tier, log ingestion hay storage retention nào gây cost.

FinOps không phải chỉ cắt chi phí. Nó tối ưu trade-off cost–reliability–performance–velocity. Giảm replica làm bill thấp nhưng vi phạm SLO không phải optimization.

## 9. Unit economics kỹ thuật

Metric cost trên request, tenant, build minute, GB processed hoặc active user giúp thấy efficiency khi scale. Tổng bill tăng có thể là hợp lý nếu business volume tăng nhanh hơn.

Platform có thể cung cấp cost estimate trước provisioning và actual cost sau sử dụng để close loop.

## 10. Rightsizing có evidence

CPU request lớn hơn nhiều usage có thể là waste, nhưng p99/peak và failover headroom quan trọng. Rightsizing nên dùng historical distribution, SLO, startup time và autoscaling delay.

Tự động giảm resource ngay theo average có thể tạo incident. Recommendation nên có confidence và staged application.

## 11. Cleanup và ephemeral resource

Preview environment, temporary database và old image tạo cost/leak. Resource tạm nên có TTL/owner mặc định. Cleanup automation phải bảo vệ production bằng classification và explicit retention policy.

“Không ai biết resource này là gì nên không dám xóa” là dấu hiệu metadata/lifecycle design yếu.

## 12. Policy hierarchy

Organization có global policy; platform có default; team có config trong allowed range; workload có runtime state. Conflict resolution phải rõ.

Nếu central policy thay đổi breaking behavior, rollout cần staged/canary. Policy cũng là production code.

## 13. Developer autonomy và guardrail

Autonomy tốt không phải cho mọi người toàn quyền, mà là cho quyền quyết định gần context trong boundary an toàn. Platform encode common constraint; team quyết định business-specific choice.

Khi exception cần nhiều lần, có thể golden path đang thiếu use case chứ không phải user “không tuân thủ”. Platform product discovery phải học từ exception.

## 14. Senior note: shared platform cần economics và reliability cùng lúc

Multi-tenancy tăng utilization nhưng blast radius tăng. Dedicated resource giảm coupling nhưng cost/toil tăng. Quyết định tenancy phải xem workload criticality, compliance, scaling pattern và team maturity.

Không có topology “chuẩn cho mọi công ty”. Có contract rõ và evidence để điều chỉnh mới là maturity.