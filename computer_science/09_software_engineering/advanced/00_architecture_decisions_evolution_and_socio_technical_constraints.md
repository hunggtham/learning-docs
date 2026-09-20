# Architecture decisions, evolution và socio-technical constraints

Advanced software architecture không phải thuộc nhiều pattern hơn. Nó là khả năng chọn boundary và trade-off phù hợp với **rate of change, failure domain, ownership, data consistency, deployment topology và organizational communication**.

## Architecture là tập constraints trên thay đổi

Một architecture tốt làm một số changes dễ và một số changes khó có chủ đích. Module boundary tốt cho phép team thay implementation bên trong mà không buộc consumers hiểu chi tiết. Boundary xấu làm một thay đổi nhỏ lan qua nhiều services/repos/deployments.

Vì vậy khi đánh giá architecture, đừng chỉ nhìn diagram hiện tại; hãy hỏi những change scenarios thường xảy ra và chi phí coordination của chúng.

## Quality attributes tạo trade-off thật

Latency, availability, consistency, security, operability, modifiability và cost thường xung đột. “Microservices scalable hơn” là statement quá thô. Tách service có thể scale độc lập, nhưng thêm network failure, serialization, observability, deployment coordination và distributed data consistency.

Architecture decision cần nêu attribute ưu tiên, workload assumption và consequence. Nếu không, pattern trở thành fashion.

## Reversibility quyết định mức đầu tư decision

Một decision dễ đảo ngược nên được thử nhanh. Decision khó đảo ngược như partition key, public API contract, identity model hoặc data ownership cần nhiều evidence hơn.

ADR (Architecture Decision Record) hữu ích khi ghi context, decision, alternatives, consequences và conditions có thể làm decision cần xem lại. ADR không phải tài liệu để chứng minh người cũ “đúng”; nó lưu reasoning để người sau hiểu constraint lịch sử.

## Conway's Law là coupling giữa software và communication

Nếu hai teams phải thay cùng component liên tục nhưng ownership tách rời, coordination cost sẽ trở thành kiến trúc thực tế. Ngược lại, service boundaries không khớp business capability có thể tạo chatty calls và cross-team transactions.

Socio-technical design nhìn code graph và communication graph cùng lúc. “Đúng” về kỹ thuật nhưng không phù hợp ownership model có thể không bền.

## Shared database là một boundary rất mạnh

Hai services có API riêng nhưng cùng sửa tables của nhau chưa thực sự có data autonomy. Schema change trở thành distributed coordination. Tuy nhiên tách database chỉ để đạt purity cũng có cost: duplicated data, asynchronous consistency và operational overhead.

Boundary nên dựa invariants và ownership. Nếu hai concepts phải commit atomic cùng nhau rất thường xuyên, việc tách chúng thành services có thể đang cắt sai aggregate/business boundary.

## Migration quan trọng hơn target diagram

Production architecture hiếm khi “rewrite một lần”. Senior engineering cần đường chuyển trạng thái an toàn:

```text
old system
→ introduce compatibility seam
→ dual-read/dual-write hoặc replicate có kiểm soát
→ verify equivalence
→ shift traffic
→ remove old path
```

Patterns như strangler fig và branch-by-abstraction giảm big-bang risk. Nhưng dual-write tự thân nguy hiểm nếu không có reconciliation/idempotency; migration cần observability và rollback story.

## Coupling có nhiều dạng

Compile-time dependency chỉ là một loại. Runtime sync dependency, shared schema, shared deployment, shared queue, shared cache key convention và shared operational runbook đều tạo coupling.

Một system có nhiều repos vẫn có thể tightly coupled nếu release phải đồng bộ. Một monolith có thể modular tốt nếu boundaries được enforce và teams deploy cùng artifact mà không phải coordinate mọi code change.

## Architecture review nên dùng scenarios

Thay vì hỏi “có dùng clean architecture không?”, dùng scenario: traffic tăng 10x; một region mất; schema cần thêm field; team A deploy mà team B chưa deploy; downstream chậm 30 giây; credential bị compromise; rollback sau migration.

Scenario ép architecture reveal assumptions và failure modes.

## Mental Model

> Architecture là **thiết kế cost-of-change và failure boundaries dưới constraints kỹ thuật + tổ chức**. Pattern chỉ là vocabulary; decision quality đến từ context, evidence, reversibility và migration path.

## Kết nối

Ôn [software architecture foundation](../../basic/09_software_engineering/01_software_architecture_and_design_reasoning.md), [system decomposition](../../basic/08_software_systems/07_system_decomposition_services_and_boundaries.md) và [distributed consistency](../../basic/06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md).