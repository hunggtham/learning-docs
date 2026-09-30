# 10 — Production Practice

Phần này là lớp thực hành của DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링). Các chapter trước giải thích runtime, delivery, container, infrastructure, Kubernetes, GitOps, observability, security và platform contracts theo từng concern. Ở đây, người đọc phải nối chúng lại khi symptom đi qua nhiều layer.

## Mạch đọc

1. [Production troubleshooting: từ symptom tới evidence xuyên tầng](./00_production_troubleshooting_and_change_failure_patterns.md) — phương pháp giảm không gian giả thuyết, phân biệt correlation với causation, đọc golden signals và chọn recovery action có expected effect rõ.
2. [Request → storage → queue → failure → recovery](./01_request_storage_queue_failure_and_recovery_case.md) — worked case đi qua HTTP request, connection pool, database commit, outbox, queue, consumer, external side effect và backlog recovery.

## Cách dùng

Chapter `00` dạy phương pháp. Chapter `01` buộc áp dụng phương pháp đó vào một hệ thống nơi transport outcome, durable state và business outcome có thể khác nhau. Khi gặp một mechanism cần đào sâu, quay về canonical owner thay vì giữ toàn bộ chi tiết trong production-practice layer.

Các owner được dùng nhiều nhất trong case hiện tại:

- [Backend timeout, retry và idempotency](../../10_backend/backend_core/06_timeout_retry_idempotency.md)
- [Observability và evidence-driven debugging](../07_observability_sre/00_observability_telemetry_and_evidence_driven_debugging.md)
- [Incident, resilience và disaster recovery](../07_observability_sre/02_incidents_resilience_backup_and_disaster_recovery.md)
- [Computer Science databases](../../computer_science/05_data_databases/README.md)
- [Data Engineering](../../data_engineering/README.md)

> **Bàn giao:** Sau khi đọc case `01`, người đọc nên có thể vẽ timeline của một operation, đánh dấu durable boundary, unknown outcome, retry/replay path và evidence cần thu trước khi chọn mitigation.