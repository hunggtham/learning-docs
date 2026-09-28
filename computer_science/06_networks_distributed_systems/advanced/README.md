# Mạng & Hệ thống phân tán nâng cao

> **Mạch đọc:** Đọc **Mạng & Hệ thống phân tán nâng cao** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **chuẩn gốc (canonical / 정본) chapters** sang **mô hình tư duy (mental models / 사고 모델들) cần đạt**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Phần nâng cao không mở chapter chỉ để bao phủ tên công nghệ. Chapter mới chỉ được thêm khi topic có bất biến (invariant / 불변식), máy trạng thái (state machine / 상태 머신) và thất bại (failure / 실패) mô hình (model / 모델) độc lập đủ để trở thành phụ thuộc (dependency / 의존성) cho nhiều phần khác.

## Chuẩn gốc (canonical / 정본) chapters

1. [Giao dịch phân tán, exactly-once và failure semantics](./00_distributed_transactions_exactly_once_and_failure_semantics.md)
2. [Failure detector, membership và gossip protocol](./01_failure_detectors_membership_and_gossip.md)
3. [Lease, fencing token và phòng tránh split-brain](./02_leases_fencing_tokens_and_split_brain_prevention.md)
4. [Consensus internals: log replication, reconfiguration và snapshot](./03_consensus_log_replication_reconfiguration_and_snapshots.md)
5. [CRDT, causal consistency và conflict resolution](./04_crdts_causal_consistency_and_conflict_resolution.md)
6. [Multi-region replication và các đánh đổi geo-distributed](./05_multi_region_replication_and_geo_distributed_tradeoffs.md)
7. [Thời gian, đồng hồ, thứ tự và quan hệ nhân quả](./06_time_clocks_ordering_and_causality.md)
8. [BGP, routing policy, convergence và route security](./07_bgp_routing_policy_convergence_and_route_security.md)


> **Chuyển mạch:** Từ **chuẩn gốc (canonical / 정본) chapters**, ta sang **mô hình tư duy (mental models / 사고 모델들) cần đạt** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental models / 사고 모델들) cần đạt

Khi đọc hết nhánh học (track / 트랙) này, người đọc cần phân biệt rõ crash với partition, liveness với an toàn (safety / 안전), suspicion với authority, replication với durability, wall-clock thứ tự (order / 순서) với nhân quả (causal / 인과적) thứ tự (order / 순서), thử lại (retry / 재시도) với exactly-once illusion và control-plane reachability với data-plane forwarding.

Mỗi giao thức (protocol / 프로토콜) phải được đọc theo cùng một khung:

```text
vấn đề ban đầu
→ invariant cần giữ
→ mechanism giữ invariant
→ failure/partition làm assumption nào mất hiệu lực
→ performance pressure đổi behavior ra sao
→ evidence nào chứng minh state hiện tại
```


> **Chuyển mạch:** Từ **mô hình tư duy (mental models / 사고 모델들) cần đạt**, ta sang **mạng (network / 네트워크) đường dẫn (path / 경로) vẫn thuộc Khoa học máy tính (computer science / 컴퓨터 과학)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mạng (network / 네트워크) đường dẫn (path / 경로) vẫn thuộc Khoa học máy tính (computer science / 컴퓨터 과학)

DNS, TCP/QUIC, TLS, proxy/bộ cân bằng tải (load balancer / 로드 밸런서), liên kết (connection / 연결) pooling và mạng (network / 네트워크) tail độ trễ (latency / 지연 시간) vẫn thuộc conceptual ranh giới (boundary / 경계) của `computer_science/`. Foundation nằm tại [`basic/06_networks_distributed_systems`](../../basic/06_networks_distributed_systems/), còn lập luận (reasoning / 추론) môi trường vận hành (production / 운영 환경) end-to-end được nối tại [request path: DNS → TCP/TLS → proxy → runtime → DB](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

BGP được nâng thành chapter advanced riêng vì nó có control-plane máy trạng thái (state machine / 상태 머신), inter-domain chính sách (policy / 정책), convergence, tuyến (route / 경로) leak/hijack và RIB→FIB ranh giới (boundary / 경계) độc lập. Chapter không biến thành vendor command danh mục (catalog / 카탈로그); trọng tâm là advertisement → chính sách (policy / 정책) → selected tuyến (route / 경로) → forwarding → bằng chứng (evidence / 증거).


> **Chuyển mạch:** Từ **mạng (network / 네트워크) đường dẫn (path / 경로) vẫn thuộc Khoa học máy tính (computer science / 컴퓨터 과학)**, ta sang **bằng chứng vận hành (production evidence / 운영 증거)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bằng chứng vận hành (production evidence / 운영 증거)

Mạng (network / 네트워크)/phân tán (distributed / 분산) debugging cần phối hợp packet/liên kết (connection / 연결) bằng chứng (evidence / 증거) với phân tán (distributed / 분산) trạng thái (state / 상태): DNS resolution, liên kết (connection / 연결) establishment, retransmission/congestion signals, proxy/LB hàng đợi (queue / 큐), yêu cầu (request / 요청) attempts, BGP advertisement/withdrawal, RIB/FIB trạng thái (state / 상태), leader term/epoch, quorum membership, replica positions, clock bất định (uncertainty / 불확실성) và dấu vết (trace / 추적) causality.

Một hết thời gian chờ (timeout / 타임아웃) không tự chứng minh nút (node / 노드) đã chết; một BGP session `Established` không chứng minh ứng dụng (application / 애플리케이션) reachability; một nút (node / 노드) `alive` không chứng minh nó còn authority; một replicated entry không tự chứng minh client-visible lần ghi nhận (commit / 커밋). Đây là các distinction cốt lõi của nhánh học (track / 트랙).

> **Bàn giao:** Sau **bằng chứng vận hành (production evidence / 운영 증거)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 distributed transactions exactly once and failure semantics](./00_distributed_transactions_exactly_once_and_failure_semantics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
