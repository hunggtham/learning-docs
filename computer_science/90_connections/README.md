# Cross-domain Connections — lĩnh vực (domain / 도메인) Hub

> **Mạch đọc:** Đọc **Cross-domain Connections — lĩnh vực (domain / 도메인) Hub** như lớp nối các canonical owner của Khoa học máy tính (computer science / 컴퓨터 과학), không như một thư viện thứ hai. Mỗi route bắt đầu từ một câu hỏi xuyên tầng rồi trỏ ngược về chapter sở hữu cơ chế chi tiết.

Các tuyến nền hiện nằm trực tiếp trong thư mục này:

1. [Từ source code tới CPU](./00_source_code_to_cpu.md) — nối source, compiler/runtime, OS, architecture và execution.
2. [Từ browser tới database request](./01_browser_to_database_request.md) — nối browser, network, backend và database trên một request path.
3. [Vòng đời dữ liệu qua memory, disk và network](./02_data_lifecycle_memory_disk_network.md) — theo data qua representation, storage và transport boundary.
4. [Các trade-off xuyên tầng](./03_cross_cutting_tradeoffs.md) — latency, throughput, consistency, availability, complexity và cost.
5. [Abstraction layers và leaky abstractions](./04_abstraction_layers_and_leaky_abstractions.md) — hiểu khi abstraction che chi tiết hữu ích và khi failure buộc phải đi xuống layer dưới.
6. [Từ threat model tới control và evidence](./05_threat_model_to_control_and_evidence.md) — nối asset/threat/trust boundary với identity, authorization, secrets, data handling, telemetry, audit evidence và response.
7. [Từ query → transaction → pipeline → analytical serving](./06_query_transaction_pipeline_and_analytical_serving.md) — theo một business fact từ OLTP commit/WAL/CDC qua transformation, warehouse, semantic layer, dashboard và reconciliation.
8. [Từ AI data → evaluation → provenance → production evidence](./07_ai_data_evaluation_provenance_and_production_evidence.md) — nối data/label lineage, experiment/evaluation, artifact/config versioning, deployment, drift, delayed outcome và retraining decision.

Phần [`advanced/`](./advanced/README.md) dùng các lĩnh vực (domain / 도메인) đã học để lập luận (reasoning / 추론) về sự cố môi trường vận hành (production incident / 운영 환경 인시던트) end-to-end: độ trễ (latency / 지연 시간), tính đúng đắn (correctness / 정확성), bảo mật (security / 보안), consistency, tài nguyên (resource / 자원) saturation và debugging qua nhiều lớp trừu tượng (abstraction layer / 추상화 계층).

## Cách dùng connection route

Connection route không thay thế chapter gốc. Khi một route nhắc tới scheduler, transaction, authorization, secret rotation, model evaluation hay data lineage, hãy dùng link trong route để quay về canonical owner nếu cần mechanism sâu hơn. Mục tiêu của thư mục này là luyện **composition reasoning**: cùng một failure hoặc quyết định có thể đi qua nhiều layer nhưng mỗi concept vẫn có một owner rõ ràng.

Có thể chọn route theo câu hỏi:

```text
"Request này đi qua những layer nào?"
→ browser → database

"Business fact này thành dashboard metric như thế nào?"
→ query → transaction → pipeline → analytical serving

"Model tốt trong notebook có thực sự đáng deploy không?"
→ AI data → evaluation → provenance → production evidence

"Control bảo mật này chứng minh hiệu lực bằng gì?"
→ threat model → control → evidence
```

> **Bàn giao:** Nếu muốn luyện đường đi của một request bình thường, bắt đầu với [browser → database](./01_browser_to_database_request.md). Nếu muốn luyện correctness của dữ liệu sau nhiều lần sao chép/biến đổi, đọc [query → transaction → pipeline → analytical serving](./06_query_transaction_pipeline_and_analytical_serving.md). Nếu muốn luyện lifecycle của một AI release, đọc [AI data → evaluation → provenance → production evidence](./07_ai_data_evaluation_provenance_and_production_evidence.md).