# Cross-domain Connections — lĩnh vực (domain / 도메인) Hub

> **Mạch đọc:** [README thư viện Khoa học máy tính](../README.md) là owner cấp domain; file này là hub điều phối các tuyến kết nối và trỏ về chapter sở hữu cơ chế chi tiết. Mỗi route bắt đầu từ một câu hỏi xuyên tầng, không thay thế tài liệu canonical của từng lĩnh vực.

Các tuyến nền hiện nằm trực tiếp trong thư mục này:

1. [Từ source code tới CPU](./00_source_code_to_cpu.md) — nối source, compiler/runtime, OS, architecture và execution.
2. [Từ browser tới database request](./01_browser_to_database_request.md) — nối browser, network, backend và database trên một request path.
3. [Vòng đời dữ liệu qua memory, disk và network](./02_data_lifecycle_memory_disk_network.md) — theo data qua representation, storage và transport boundary.
4. [Các trade-off xuyên tầng](./03_cross_cutting_tradeoffs.md) — latency, throughput, consistency, availability, complexity và cost.
5. [Abstraction layers và leaky abstractions](./04_abstraction_layers_and_leaky_abstractions.md) — hiểu khi abstraction che chi tiết hữu ích và khi failure buộc phải đi xuống layer dưới.

Phần [`advanced/`](./advanced/README.md) dùng các lĩnh vực đã học để lập luận về sự cố môi trường vận hành end-to-end: độ trễ, tính đúng đắn, bảo mật, consistency, bão hòa tài nguyên và debugging qua nhiều lớp trừu tượng.

## Cách dùng connection route

Connection route không thay thế chapter gốc. Khi một route nhắc tới scheduler, transaction, authorization, secret rotation, model evaluation hay data lineage, hãy dùng link trong route để quay về canonical owner nếu cần mechanism sâu hơn. Mục tiêu của thư mục này là luyện **composition reasoning**: cùng một failure hoặc quyết định có thể đi qua nhiều layer nhưng mỗi concept vẫn có một owner rõ ràng.

Có thể chọn route theo câu hỏi:

```text
"Request này đi qua những layer nào?"
→ browser → database

"Control bảo mật này chứng minh hiệu lực bằng gì?"
→ threat model → control → evidence
```

## Handoff sang domain owner

- Cần database internals sâu hơn → [Data & Databases](../05_data_databases/README.md).
- Cần pipeline/warehouse/semantic layer sâu hơn → quay về owner dữ liệu được README domain chỉ định.
- Cần AI module/evaluation/MLOps sâu hơn → [Artificial Intelligence](../02_artificial_intelligence/README.md).
- Cần production incident/recovery reasoning → [DevOps / Platform Engineering](../../devops_platform_engineering/README.md).

> **Bàn giao:** Chọn tuyến theo câu hỏi thực tế: request đi qua những lớp nào thì bắt đầu với [browser → database](./01_browser_to_database_request.md); dữ liệu thay đổi thế nào qua storage và network thì đọc [data lifecycle](./02_data_lifecycle_memory_disk_network.md); cần tìm trade-off hệ thống thì đọc [cross-cutting trade-offs](./03_cross_cutting_tradeoffs.md). Khi cần cơ chế sâu hơn, quay về README domain và owner được liên kết trong từng tuyến.
