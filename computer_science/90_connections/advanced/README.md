# Kết nối xuyên tầng nâng cao

Các chapter ở đây không lặp lại domain content. Chúng bắt đầu từ một thuộc tính end-to-end hoặc symptom production rồi đi xuyên các abstraction để trả lời: invariant nào bị vi phạm, lower layer nào quyết định behavior, và evidence nào đủ để chứng minh causal path.

## Canonical connection paths

1. [Gỡ lỗi xuyên abstraction layers](./00_debugging_across_abstraction_layers.md)
2. [Request path: DNS → TCP/TLS → proxy/load balancer → runtime → DB/storage](./01_end_to_end_latency_browser_edge_service_db_storage.md)
3. [Correctness path: CPU cache → memory ordering → language memory model → concurrency bug](./02_correctness_path_language_os_cpu_memory_ordering.md)
4. [Durability path: application transaction → MVCC/WAL → filesystem → storage → replication](./03_durability_path_application_commit_wal_filesystem_device.md)

## Connections đã được hấp thụ vào bốn path hiện có

Không tạo chapter riêng chỉ để có thêm tên connection.

**Retry → timeout → overload → queue → backpressure → cascading failure** nằm trong request/latency path, vì đây là một feedback loop làm thay đổi arrival rate và service time trên cùng causal graph.

**Identity → authorization → secret → TLS → service boundary → incident containment** nằm trong debugging path, vì đây là authority path cần được reconstruct khi failure hoặc compromise lan qua nhiều service boundaries.

**CPU cache → memory ordering → language memory model → concurrency bug** là correctness path và phải luôn phân biệt physical visibility với language-level happens-before.

**Application transaction → MVCC/WAL → filesystem → storage → replication** là durability path và phải phân biệt visibility, local persistence, quorum commit và backup/recovery.

## Cách dùng khi debug production

Bắt đầu từ property người dùng quan sát được: sai dữ liệu, mất dữ liệu, timeout, duplicate side effect, auth failure hoặc latency tail. Sau đó:

```text
1. Viết invariant bị nghi vi phạm.
2. Dựng timeline/causal graph.
3. Xác định boundary có queue, ownership, authority hoặc representation change.
4. Thu evidence ở tầng hiện tại.
5. Chỉ đi xuống lower layer khi contract hiện tại không giải thích được symptom.
6. Quay lại abstraction sở hữu invariant để đặt fix.
```

Không mặc định nguyên nhân ở layer thấp nhất. CPU/cache/kernel chỉ nên xuất hiện khi evidence cho thấy chúng thực sự quyết định behavior.

## Production evidence

Cross-layer evidence phải nối được nhiều loại signal: trace/span, queue/pool wait, runtime pause, scheduler pressure, DB wait/plan/WAL, network connection/retransmission, certificate/policy identity, storage flush/queue, quorum/replica position và hardware counters khi cần.

Một dashboard đơn lẻ thường chỉ cho symptom. Mục tiêu là xây **causal model có confidence**, dùng nhiều independent signals để phân biệt correlation với mechanism.

## Quy tắc mở rộng

Nếu connection mới có thể được hấp thụ như một section sâu hơn trong bốn canonical path hiện tại, không tạo chapter mới. Chỉ thêm file khi có một end-to-end invariant độc lập, một failure propagation pattern khác bản chất và đủ nội dung để tạo mental model mới.