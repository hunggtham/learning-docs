# Data governance, bias và algorithmic impact

Data pipeline không chỉ là technical ETL. Dataset đại diện cho decisions về measurement, inclusion, labels, access và retention. Những decisions đó ảnh hưởng model/report/automation downstream, nên governance là part of system correctness.

## Data provenance

Provenance trả lời data đến từ đâu, transform qua steps nào, version nào và ai chịu ownership. Không có provenance, khi metric sai rất khó truy root cause.

Lineage tools biến pipeline dependencies thành graph để impact analysis khi schema/source thay đổi.

## Measurement bias

Ta thường không observe concept trực tiếp mà đo proxy. “Productivity” có thể proxy bằng tickets closed; “creditworthiness” bằng historical repayment; “engagement” bằng clicks.

Proxy mismatch tạo bias ngay trước algorithm.

## Sampling bias

Dataset chỉ phản ánh population được quan sát. Nếu training data thiếu rural users hoặc devices cũ, model may generalize kém cho nhóm đó.

Random split không sửa representation gap nếu underlying dataset đã biased.

## Label bias

Labels do humans/institutions tạo có inconsistency và historical policy. Arrest records không bằng crime ground truth; customer support escalation không bằng objective severity.

ML có thể reproduce institutional bias encoded trong labels.

## Feedback loops

Prediction ảnh hưởng environment, tạo data mới rồi reinforce model. Nếu predictive policing gửi nhiều patrol tới khu A, phát hiện nhiều incidents ở A và data sau càng “chứng minh” A risky.

Closed-loop systems cần evaluate causal/behavioral effects, không chỉ offline accuracy.

## Fairness metrics

Group fairness metrics formalize different goals: parity of positive rates, equalized error rates, calibration... Chúng có thể conflict khi base rates khác.

Không có metric “fairness universal”. Selection là normative decision cần domain/stakeholder analysis.

## Governance controls

Useful controls gồm data classification, access policy, retention, quality checks, schema contracts, lineage, stewardship và deletion workflows.

Governance không nên chỉ là document; policy cần map thành technical enforcement/monitoring.

## Right to deletion và derived data

Xóa source record không luôn đơn giản nếu data đã copy vào cache, backup, analytics và model training artifacts. System architecture cần know data propagation.

Legal obligations vary jurisdiction, nhưng engineering principle là deletion/retention must be designed, not improvised.

## Algorithmic impact assessment

Trước high-impact automation, assessment có thể hỏi affected populations, failure modes, contestability, human oversight, monitoring và redress.

Goal là discover risks before irreversible deployment, tương tự threat modeling cho security.

## Common Misconceptions

**“Data là objective facts.”** Measurement/collection luôn có context và missingness.

**“Remove protected attribute thì model không biased.”** Proxies/correlated features vẫn encode group information.

**“Fairness metric giải ethics.”** Metric làm trade-off explicit nhưng không quyết normative priority thay con người.

## Mental Model

> Data system là measurement system. Mỗi field là claim về world; governance giữ provenance, purpose và quality của claims đó xuyên lifecycle.

## Kết nối

Đọc [AI evaluation](../10_ai_foundations/04_ai_evaluation_data_and_responsibility.md), [database data models](../05_data_databases/00_data_models_and_database_systems.md), [privacy/ethics](./00_computing_ethics_privacy_and_professional_responsibility.md) và [data lifecycle](../90_connections/02_data_lifecycle_memory_disk_network.md).