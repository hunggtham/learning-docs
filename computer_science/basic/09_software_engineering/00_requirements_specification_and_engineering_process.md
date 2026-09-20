# Requirements, specification và software engineering process

Software Engineering (kỹ nghệ phần mềm / 소프트웨어 공학) bắt đầu trước khi code xuất hiện. Nếu ta xây đúng thứ đã được mô tả nhưng thứ đó không giải quyết problem thực, system vẫn thất bại. Vì vậy requirements engineering nghiên cứu cách biến nhu cầu mơ hồ của stakeholders thành behavior, constraints và acceptance criteria đủ rõ để design, implement và verify.

## Problem trước solution

Một requirement tốt không bắt đầu bằng framework hay database. Nó mô tả actor nào cần đạt goal nào, trong context nào, với constraints nào.

“Làm màn hình nhanh hơn” mơ hồ. “95% requests hoàn thành dưới 300 ms với 500 concurrent users trên workload X” có thể đo và kiểm chứng.

Điểm cốt lõi là chuyển adjective mơ hồ thành observable property khi có thể.

## Functional và non-functional requirements

Functional requirement mô tả system phải làm gì: đăng nhập, chuyển tiền, tìm kiếm, export report.

Non-functional requirement mô tả quality/constraint: latency, availability, security, compliance, maintainability, portability, data retention.

Nhưng boundary không tuyệt đối. “Không cho user khác đọc hồ sơ” vừa là security property vừa là functional authorization rule. Điều quan trọng là requirement có thể trace tới design/test.

## Stakeholder và conflicting goals

Product muốn feature nhanh; security muốn stricter controls; operations muốn simplicity; finance muốn giảm infrastructure cost; user muốn ít friction.

Engineering không loại bỏ conflict mà làm trade-off explicit. Một architecture decision nên nói requirement nào ưu tiên và cost nào chấp nhận.

## Specification

Specification (đặc tả / 명세) mô tả expected behavior ở mức đủ precise. Nó có thể là prose, API contract, state machine, schema, sequence diagram, invariant hoặc formal model.

Specification không nhất thiết dài. Quan trọng là loại bỏ ambiguity ở những nơi failure cost cao.

Ví dụ payment API cần định nghĩa idempotency, currency precision, timeout semantics và duplicate request behavior; không chỉ request/response fields.

## Use case và user story

Use case mô tả interaction flow giữa actor và system, gồm main path và alternate/error paths. User story kiểu “As a..., I want..., so that...” hữu ích cho conversation nhưng không thay acceptance criteria.

Một user story quá ngắn dễ biến thành placeholder thay vì requirement. Engineering cần bổ sung edge cases, permissions, data lifecycle và failure behavior.

## Acceptance criteria

Acceptance criteria biến intent thành testable conditions. Với password reset, cần không chỉ happy path mà token expiry, single-use, rate limit, account enumeration và logged-in session behavior.

Acceptance tests không chứng minh toàn system đúng, nhưng tạo contract giữa product intent và implementation.

## Requirements volatility

Requirements thay đổi vì market, regulation và learning. Quy trình tốt không giả vờ đóng băng mọi thứ; nó quản lý change impact.

Architecture nên giữ stable core invariants trong khi cho phép volatile parts thay đổi. Đây là lý do abstraction/module boundaries quan trọng.

## Traceability

Traceability nối requirement → design decision → implementation → test → monitoring. Trong safety/regulatory domains, traceability rất quan trọng để chứng minh control nào đáp ứng requirement nào.

Trong product development bình thường, traceability lightweight vẫn hữu ích khi incident xảy ra: “behavior này là bug hay intended?”

## Waterfall, iterative và agile

Waterfall-style phase separation phù hợp khi requirements ổn định và change cost cao, nhưng dễ feedback muộn. Iterative/agile processes giảm batch size của learning bằng cách deliver/validate thường xuyên.

Agile không có nghĩa không design, không document hay thay đổi vô hạn. Nó nhấn mạnh short feedback loops và adaptation.

## Risk-driven development

Không phải task nào cũng nên làm theo business priority đơn thuần. Technical uncertainty cao có thể cần spike/prototype sớm. Security/performance bottleneck có thể cần validate trước khi UI hoàn thiện.

Risk-driven planning xử lý unknowns trước khi chúng trở thành late surprise.

## Common Misconceptions

**“Requirements là việc của PM/BA, developer chỉ code.”** Developer cần hiểu constraints để phát hiện ambiguity/impossible assumptions.

**“Agile nghĩa là không cần specification.”** Chỉ đổi granularity/timing; critical contracts vẫn cần precise.

**“User nói gì thì requirement là vậy.”** User mô tả pain/goal; solution và hidden constraints cần investigation.

## Mental Model

> Requirements engineering là quá trình biến intent thành falsifiable contracts đủ rõ để design và verify, đồng thời chấp nhận rằng understanding sẽ thay đổi qua feedback.

## Kết nối

Đọc [abstraction/API contracts](../08_software_systems/00_abstraction_modularity_interfaces_and_apis.md), [software architecture](./01_software_architecture_and_design_reasoning.md) và [testing strategy](./02_testing_quality_and_verification_strategy.md).