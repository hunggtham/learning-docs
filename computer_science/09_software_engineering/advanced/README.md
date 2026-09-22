# Advanced Software Engineering

Track này tập trung vào cách thay đổi production system dưới uncertainty mà không cần big-bang coordination. Không thêm chapter chỉ để bao phủ methodology hoặc metric mới; ưu tiên đào sâu decision boundary, compatibility, migration, verification và evidence.

## Canonical chapters

1. [Architecture decisions, evolution và socio-technical constraints](./00_architecture_decisions_evolution_and_socio_technical_constraints.md)
2. [Modular monolith vs services: boundary economics và migration](./01_modular_monolith_vs_services_boundary_economics.md)
3. [API/schema compatibility và evolutionary design](./02_api_schema_compatibility_and_evolutionary_design.md)
4. [Large-scale refactoring, strangler migration và branch-by-abstraction](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md)
5. [Test architecture: contract, mutation, property-based và production verification](./04_test_architecture_contract_mutation_property_and_production_verification.md)
6. [Deployment safety: canary, blue-green, feature flags và rollback limits](./05_deployment_safety_canary_blue_green_flags_and_rollback.md)

## Mental models cần đạt

Mỗi thay đổi phải được reasoning như một state transition có overlap window:

```text
old world
→ mixed versions / partial rollout
→ migration state
→ new world
```

Invariant quan trọng là system vẫn tương thích và quan sát được trong toàn bộ transition, không chỉ ở trạng thái cuối.

Architecture decision cần chỉ ra quality attribute/trade-off nào được tối ưu, assumption nào đang dựa vào và evidence nào sẽ cho biết decision không còn phù hợp. Deployment strategy phải nói rõ blast radius, rollback limit, irreversible side effect và guardrail nào quyết định tiếp tục hay dừng rollout.

## System Design và Software Engineering giao nhau ở changeability

System Design nằm ở `08_software_systems` và các domain runtime/network/database; Software Engineering sở hữu câu hỏi **làm sao thay đổi design đó an toàn theo thời gian**.

Vì vậy zero-downtime database migration, incident learning, technical debt, team ownership và architecture governance được hấp thụ vào các canonical chapter theo perspective evolution/decision, thay vì mở thành file riêng chỉ để tăng coverage.

## Production evidence

Một thay đổi production phải để lại evidence đủ để kiểm tra hypothesis: deployment version/cohort, error và latency percentile, SLO burn, compatibility failures, schema/data migration progress, rollback feasibility, test signal và business invariant.

Metric chỉ có giá trị khi gắn với decision. DORA-style signal, test coverage hay deployment frequency không được dùng như proxy tuyệt đối cho engineering quality nếu không hiểu mechanism phía sau.

## Quy tắc mở rộng

Ưu tiên rewrite chapter hiện có khi gap thuộc architecture boundary, compatibility, migration, verification hoặc deployment safety. Chỉ thêm conceptual unit mới khi có invariant/failure mode độc lập mà sáu chapter canonical không thể chứa tự nhiên.