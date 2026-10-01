# Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bài toán ban đầu: độ trễ (latency / 지연 시간), availability và consistency cùng chịu physics** đưa mô hình vào một trường hợp đủ cụ thể để quan sát; sau đó sang **2. bất biến (invariant / 불변식) đầu tiên: chỉ một authority hợp lệ được phép quyết định lịch sử (history / 이력) cần single-writer** để chuyển câu hỏi ấy thành điều kiện phải giữ. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Khi các bản sao nằm ở nhiều vùng địa lý, tốc độ ánh sáng, topology mạng và failure-domain trở thành một phần của consistency mô hình (model / 모델). Không giao thức (protocol / 프로토콜) nào biến một round trip Seoul–Virginia thành bộ nhớ (memory / 메모리) truy cập (access / 접근) cục bộ. kiến trúc (architecture / 아키텍처) phải quyết định **bất biến (invariant / 불변식) nào xứng đáng trả coordination chi phí (cost / 비용) xuyên vùng** và bất biến (invariant / 불변식) nào có thể giữ cục bộ rồi reconcile sau.

Mô hình tư duy (mental model / 사고 모델) của chương này là: **multi-region replication phân phối authority và lịch sử (history / 이력) qua khoảng cách. tính đúng đắn (correctness / 정확성) phụ thuộc vào ai có quyền accept ghi (write / 쓰기), replica nào có lịch sử (history / 이력) đủ mới để serve/read/promote, và failover có ngăn old authority tiếp tục ghi hay không.**

## 1. Bài toán ban đầu: độ trễ (latency / 지연 시간), availability và consistency cùng chịu physics

Một synchronous coordination round qua nhiều regions có độ trễ (latency / 지연 시간) floor theo mạng (network / 네트워크) propagation + processing. Nếu ghi (write / 쓰기) phải chờ remote quorum, user-facing độ trễ (latency / 지연 시간) chứa ít nhất một phần remote RTT và remote hàng đợi (queue / 큐)/lưu trữ (storage / 저장소) chi phí (cost / 비용).

Tối ưu software có thể giảm overhead nhưng không bỏ khoảng cách vật lý. Vì vậy region placement là **ngữ nghĩa (semantic / 의미적)/sức chứa (capacity / 용량) quyết định (decision / 결정)**, không chỉ triển khai (deployment / 배포) preference.

> **Chuyển mạch:** Multi-region phải đánh đổi latency, availability và consistency dưới cùng physics; single-writer giữ authority cho history, còn replication state cần được mô tả theo mức lag/conflict thay vì chỉ đồng bộ/chưa đồng bộ.

## 2. bất biến (invariant / 불변식) đầu tiên: chỉ một authority hợp lệ được phép quyết định lịch sử (history / 이력) cần single-writer

Với single-leader hệ thống (system / 시스템), bất biến (invariant / 불변식) thường là:

> Tại một epoch/term có thẩm quyền, chỉ leader hợp lệ được phép accept writes tạo authoritative lịch sử (history / 이력).

Mạng (network / 네트워크) partition làm hai nodes đều “không nghe thấy nhau”; nó không chứng minh nút (node / 노드) bên kia chết. Failover vì vậy phải dựa vào consensus/lease/fencing/epoch cơ chế (mechanism / 메커니즘) chứ không chỉ health-check hết thời gian chờ (timeout / 타임아웃).

Nếu primary cũ vẫn ghi sau khi new primary được promoted, split-brain có thể tạo two divergent histories mà async replication không tự hòa giải được.

> **Chuyển mạch:** Ở chặng này của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **3. Replication trạng thái (state / 상태) không phải nhị phân (binary / 이진) “đồng bộ/chưa đồng bộ”** tiếp nhận điểm tựa từ **2. bất biến (invariant / 불변식) đầu tiên: chỉ một authority hợp lệ được phép quyết định lịch sử (history / 이력) cần single-writer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Synchronous replication đổi thất bại (failure / 실패) mô hình (model / 모델) và đường găng (critical path / 임계 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Replication trạng thái (state / 상태) không phải nhị phân (binary / 이진) “đồng bộ/chưa đồng bộ”

Một log entry/ghi (write / 쓰기) có thể đi qua:

```text
created at leader
→ appended locally
→ persisted locally
→ sent
→ received by replica
→ persisted remotely
→ acknowledged by quorum/rule
→ applied to replica state
→ visible to replica reads
```

Các các hệ thống (systems / 시스템들) đặt acknowledgement/read ranh giới (boundary / 경계) ở vị trí khác nhau. Do đó cần hỏi cụ thể:

```text
ack sau receive hay persist?
quorum nào phải ack?
read replica serve theo received, applied hay committed frontier?
promotion cần frontier nào?
```

Số replicas tự nó không trả lời durability/consistency.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **3. Replication trạng thái (state / 상태) không phải nhị phân (binary / 이진) “đồng bộ/chưa đồng bộ”** xác định đầu vào; **4. Synchronous replication đổi thất bại (failure / 실패) mô hình (model / 모델) và đường găng (critical path / 임계 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. Asynchronous replication tạo thất bại (failure / 실패) cửa sổ (window / 윈도우) có chủ đích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Synchronous replication đổi thất bại (failure / 실패) mô hình (model / 모델) và đường găng (critical path / 임계 경로)

Nếu máy khách (client / 클라이언트) chỉ nhận success sau remote quorum persistence, RPO trước một số nút (node / 노드) failures có thể nhỏ hơn. Đổi lại remote mạng (network / 네트워크)/lưu trữ (storage / 저장소) nằm trên đường găng (critical path / 임계 경로).

Một follower chậm có thể kéo p99 nếu quorum chính sách (policy / 정책) cần nó; giao thức (protocol / 프로토콜) có thể chọn quorum subset, nhưng lựa chọn đó phải vẫn giữ intersection/authority bất biến (invariant / 불변식).

Câu hỏi không phải “sync có an toàn hơn async” chung chung. Câu hỏi là **acknowledgement này hứa survive thất bại (failure / 실패) set nào?**

> **Chuyển mạch:** Trong **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **4. Synchronous replication đổi thất bại (failure / 실패) mô hình (model / 모델) và đường găng (critical path / 임계 경로)** xác định đầu vào; **5. Asynchronous replication tạo thất bại (failure / 실패) cửa sổ (window / 윈도우) có chủ đích** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. Read consistency phải được thiết kế riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Asynchronous replication tạo thất bại (failure / 실패) cửa sổ (window / 윈도우) có chủ đích

Leader có thể ack cục bộ (local / 로컬) durable ghi (write / 쓰기) rồi ship log sau. Foreground độ trễ (latency / 지연 시간) thấp hơn nhưng failover trước replication có thể mất acknowledged writes tùy đặc tả hợp đồng (contract / 계약).

Cửa sổ (window / 윈도우) này phải được diễn đạt bằng **mục tiêu điểm khôi phục (Recovery Point Objective, RPO)** và measured replication lag, không bằng câu “thường chỉ vài ms”. Tail lag trong sự cố (incident / 인시던트) mới là thứ quyết định data-loss cửa sổ (window / 윈도우).

> **Chuyển mạch:** Ở chặng này của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **6. Read consistency phải được thiết kế riêng** tiếp nhận điểm tựa từ **5. Asynchronous replication tạo thất bại (failure / 실패) cửa sổ (window / 윈도우) có chủ đích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Replica lag là một distance trong lịch sử (history / 이력), không chỉ seconds** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Read consistency phải được thiết kế riêng

Read replica giảm độ trễ (latency / 지연 시간) và offload leader, nhưng có thể stale. Các guarantees có strength khác nhau:

```text
eventual read
monotonic reads
read-your-writes
causal/session consistency
linearizable/leader/quorum-style read
```

Nếu người dùng (user / 사용자) vừa cập nhật (update / 업데이트) profile ở region A rồi yêu cầu (request / 요청) chuyển sang replica B chưa apply ghi (write / 쓰기), người dùng (user / 사용자) có thể thấy old trạng thái (state / 상태).

Read-your-writes có thể dùng session/phiên bản (version / 버전) đơn vị từ (token / 토큰), sticky routing, wait-until-replica-frontier, hoặc tuyến (route / 경로) tới authority đủ mới. cơ chế (mechanism / 메커니즘) khác nhau nhưng bất biến (invariant / 불변식) là:

> Read phải được serve từ replica có lịch sử (history / 이력) frontier đáp ứng consistency đặc tả hợp đồng (contract / 계약) của yêu cầu (request / 요청).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **7. Replica lag là một distance trong lịch sử (history / 이력), không chỉ seconds** tiếp nhận điểm tựa từ **6. Read consistency phải được thiết kế riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Failover là chuyển authority, không chỉ đổi DNS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Replica lag là một distance trong lịch sử (history / 이력), không chỉ seconds

Time-based lag dễ hiểu nhưng có thể gây nhầm khi clocks/skew hoặc ghi (write / 쓰기) tỷ lệ (rate / 비율) biến động. Một replica 2 seconds behind trong burst 100k writes khác 2 seconds behind lúc idle.

Useful bằng chứng (evidence / 증거) gồm log/LSN/offset/lần ghi nhận (commit / 커밋)/applied positions và hàng đợi (queue / 큐)/backlog. mô hình tư duy (mental model / 사고 모델) là đo **lịch sử (history / 이력) distance + ứng dụng (application / 애플리케이션) delay + mạng (network / 네트워크) delay**, không chỉ một wall-clock number.

> **Chuyển mạch:** Trong **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **8. Failover là chuyển authority, không chỉ đổi DNS** tiếp nhận điểm tựa từ **7. Replica lag là một distance trong lịch sử (history / 이력), không chỉ seconds** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Failover candidate mới nhất chưa chắc tự động là candidate an toàn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Failover là chuyển authority, không chỉ đổi DNS

Một safe failover cần giải nhiều trạng thái (state / 상태) transitions:

```text
xác định old authority không còn quyền ghi
→ chọn candidate có history đủ hợp lệ
→ assign new epoch/term/fencing token
→ promote
→ redirect clients/control plane
→ invalidate/drain stale connections/routes
→ verify read/write invariants
```

DNS/TTL chỉ là traffic steering. Nó không giải authority. liên kết (connection / 연결) pools và clients có thể giữ old endpoint lâu hơn DNS thay đổi (change / 변경).

Đọc [leases, fencing tokens và split-brain prevention](./02_leases_fencing_tokens_and_split_brain_prevention.md).

> **Chuyển mạch:** Ở chặng này của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **9. Failover candidate mới nhất chưa chắc tự động là candidate an toàn** tiếp nhận điểm tựa từ **8. Failover là chuyển authority, không chỉ đổi DNS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Failback còn khó hơn failover nếu histories đã đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Failover candidate mới nhất chưa chắc tự động là candidate an toàn

Một replica có nhiều bytes nhất nhưng bytes đó chưa chắc thuộc committed authoritative lịch sử (history / 이력) nếu giao thức (protocol / 프로토콜) chưa xác nhận. Consensus hệ thống (system / 시스템) cần term/commit-index-like authority rules; primary-replica hệ thống (system / 시스템) cần promotion quy tắc (rule / 규칙) rõ.

Bất biến (invariant / 불변식) là **new leader không được invent lịch sử (history / 이력) trái với lần ghi nhận (commit / 커밋) đặc tả hợp đồng (contract / 계약) đã hứa cho clients**.

Đây là lý do “bản sao (copy / 복사) nhiều dữ liệu (data / 데이터) nhất rồi promote” không phải generic failover thuật toán (algorithm / 알고리즘).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **10. Failback còn khó hơn failover nếu histories đã đổi** tiếp nhận điểm tựa từ **9. Failover candidate mới nhất chưa chắc tự động là candidate an toàn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Multi-leader chuyển bài toán (problem / 문제) từ authority sang xung đột (conflict / 충돌) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Failback còn khó hơn failover nếu histories đã đổi

Sau khi region cũ hồi phục, không nên đơn giản bật ghi (write / 쓰기) lại. Nó có thể chứa stale/divergent trạng thái (state / 상태).

Safe failback thường cần:

```text
rejoin as follower/non-authoritative
→ catch up / snapshot / repair
→ prove frontier consistency
→ only then consider authority transfer
```

Operational runbook phải coi failback là giao thức (protocol / 프로토콜) chuyển tiếp (transition / 전이), không phải reverse DNS edit.

> **Chuyển mạch:** Trong **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **11. Multi-leader chuyển bài toán (problem / 문제) từ authority sang xung đột (conflict / 충돌) ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **10. Failback còn khó hơn failover nếu histories đã đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. CRDT giải một lớp xung đột (conflict / 충돌) nhưng không xóa nghiệp vụ (business / 비즈니스) các ràng buộc (constraints / 제약조건들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Multi-leader chuyển bài toán (problem / 문제) từ authority sang xung đột (conflict / 충돌) ngữ nghĩa (semantics / 의미론)

Cho phép mỗi region accept cục bộ (local / 로컬) writes giảm ghi (write / 쓰기) độ trễ (latency / 지연 시간) và tăng autonomy, nhưng concurrent writes có thể xung đột.

Một last-write-wins quy tắc (rule / 규칙) dựa timestamp có thể làm mất nghiệp vụ (business / 비즈니스) intent và phụ thuộc clock các giả định (assumptions / 가정들). Unique username, inventory decrement, quota và account balance thường có invariants không thể reconcile chỉ bằng chọn “latest giá trị (value / 값)”.

Cần phân loại trạng thái (state / 상태):

```text
commutative/mergeable
conflict-tolerant
requires single authority or coordination
```

Toàn cục (global / 전역) coordination chỉ nên đặt tại invariants thật sự không thể tách/merge an toàn.

> **Chuyển mạch:** Ở chặng này của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **12. CRDT giải một lớp xung đột (conflict / 충돌) nhưng không xóa nghiệp vụ (business / 비즈니스) các ràng buộc (constraints / 제약조건들)** tiếp nhận điểm tựa từ **11. Multi-leader chuyển bài toán (problem / 문제) từ authority sang xung đột (conflict / 충돌) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Geo-partitioning giữ coordination gần quyền sở hữu (ownership / 소유권) tự nhiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. CRDT giải một lớp xung đột (conflict / 충돌) nhưng không xóa nghiệp vụ (business / 비즈니스) các ràng buộc (constraints / 제약조건들)

CRDT cho phép merge trạng thái (state / 상태) với algebraic properties cụ thể mà không cần total thứ tự (order / 순서) cho mọi thao tác (operation / 연산). Nhưng nếu nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) là “không bán quá 100 vé toàn cầu”, merge-friendly counter không tự tạo sức chứa (capacity / 용량) reservation toàn cục (global / 전역) an toàn.

Đọc [CRDT, causal consistency và conflict resolution](./04_crdts_causal_consistency_and_conflict_resolution.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **13. Geo-partitioning giữ coordination gần quyền sở hữu (ownership / 소유권) tự nhiên** tiếp nhận điểm tựa từ **12. CRDT giải một lớp xung đột (conflict / 충돌) nhưng không xóa nghiệp vụ (business / 비즈니스) các ràng buộc (constraints / 제약조건들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Hotspot và skew phá giả định (assumption / 가정) “traffic phân bố đều”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Geo-partitioning giữ coordination gần quyền sở hữu (ownership / 소유권) tự nhiên

Nếu users/dữ liệu (data / 데이터) có “home region”, partition by quyền sở hữu (ownership / 소유권) có thể giữ đa số writes cục bộ (local / 로컬) và chỉ coordinate cross-region khi nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) thật sự vượt ranh giới (boundary / 경계).

Ví dụ:

```text
customer profile owned by home region
regional inventory owned locally
analytics replicated globally asynchronously
```

Ranh giới (boundary / 경계) tốt giảm toàn cục (global / 전역) coordination volume. ranh giới (boundary / 경계) xấu tạo cross-region phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) cho mọi yêu cầu (request / 요청).

> **Chuyển mạch:** Trong **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **14. Hotspot và skew phá giả định (assumption / 가정) “traffic phân bố đều”** tiếp nhận điểm tựa từ **13. Geo-partitioning giữ coordination gần quyền sở hữu (ownership / 소유권) tự nhiên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. thất bại (failure / 실패) domains phải độc lập thật sự** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Hotspot và skew phá giả định (assumption / 가정) “traffic phân bố đều”

Geo sharding theo user-id có thể trông cân bằng trên paper nhưng tenant lớn, sự kiện (event / 이벤트) viral hoặc region traffic peak tạo skew.

Một shard/leader nóng có thể saturate CPU/mạng (network / 네트워크)/lưu trữ (storage / 저장소) trong khi fleet average thấp. Multi-region sức chứa (capacity / 용량) planning cần nhìn per-shard/per-tenant frontier, không chỉ aggregate regional utilization.

> **Chuyển mạch:** Ở chặng này của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **15. thất bại (failure / 실패) domains phải độc lập thật sự** tiếp nhận điểm tựa từ **14. Hotspot và skew phá giả định (assumption / 가정) “traffic phân bố đều”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Active-active không đồng nghĩa zero downtime** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. thất bại (failure / 실패) domains phải độc lập thật sự

Ba replicas không tương đương ba independent copies nếu cùng rack, power lĩnh vực (domain / 도메인), mạng (network / 네트워크) điều khiển (control / 제어) plane, credential gốc (root / 루트), lưu trữ (storage / 저장소) backend hoặc triển khai (deployment / 배포) bug.

Availability lập luận (reasoning / 추론) cần map:

```text
hardware failure domain
network failure domain
region/provider/control-plane dependency
software rollout/config dependency
security/identity dependency
```

Correlated thất bại (failure / 실패) thường phá kiến trúc (architecture / 아키텍처) mà “N regions” marketing diagram không thể hiện.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **16. Active-active không đồng nghĩa zero downtime** tiếp nhận điểm tựa từ **15. thất bại (failure / 실패) domains phải độc lập thật sự** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Cross-region hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도) có thể khuếch đại outage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Active-active không đồng nghĩa zero downtime

Active-active regions vẫn có dùng chung (shared / 공유) dependencies: toàn cục (global / 전역) định danh (identity / 식별자) issuer, lược đồ (schema / 스키마) registry, KMS gốc (root / 루트), DNS/điều khiển (control / 제어) plane, replication channel hoặc dùng chung (common / 공통) nhị phân (binary / 이진)/cấu hình (config / 설정).

Một bad deploy hoặc bảo mật (security / 보안) chính sách (policy / 정책) rollout có thể thất bại (fail / 실패) tất cả regions cùng lúc. Geographic redundancy chỉ bảo vệ thất bại (failure / 실패) modes thực sự independent với nó.

> **Chuyển mạch:** Trong **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **17. Cross-region hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도) có thể khuếch đại outage** tiếp nhận điểm tựa từ **16. Active-active không đồng nghĩa zero downtime** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Consistency chính sách (policy / 정책) cũng là sức chứa (capacity / 용량) chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Cross-region hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도) có thể khuếch đại outage

Remote lời gọi (call / 호출) có RTT cao và variability lớn hơn. hết thời gian chờ (timeout / 타임아웃) quá sát normal tail tạo false hết thời gian chờ (timeout / 타임아웃); máy khách (client / 클라이언트) thử lại (retry / 재시도) sang region khác có thể duplicate công việc (work / 작업) và tăng tải (load / 로드) đúng lúc failover.

Nhân quả (causal / 인과적) vòng lặp (loop / 루프):

```text
region latency ↑
→ timeout ↑
→ retry/failover traffic ↑
→ alternate region queue ↑
→ its latency ↑
→ more retries
→ cascading regional failure
```

Failover sức chứa (capacity / 용량) phải tính **redirected demand**, không chỉ normal cục bộ (local / 로컬) traffic.

Đọc [end-to-end request và retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

> **Chuyển mạch:** Ở chặng này của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **18. Consistency chính sách (policy / 정책) cũng là sức chứa (capacity / 용량) chính sách (policy / 정책)** tiếp nhận điểm tựa từ **17. Cross-region hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도) có thể khuếch đại outage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. dữ liệu (data / 데이터) residency và ranh giới bảo mật (security boundary / 보안 경계) đi cùng replication topology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Consistency chính sách (policy / 정책) cũng là sức chứa (capacity / 용량) chính sách (policy / 정책)

Strong remote read/ghi (write / 쓰기) yêu cầu coordination/mạng (network / 네트워크)/lưu trữ (storage / 저장소) trên đường găng (critical path / 임계 경로). Stale-local read giảm chi phí (cost / 비용) nhưng đổi ngữ nghĩa (semantics / 의미론). Session consistency ở giữa cần đơn vị từ (token / 토큰)/frontier tracking.

Hệ thống (system / 시스템) thiết kế (design / 설계) nên phân loại operations theo bất biến (invariant / 불변식):

```text
must be globally current
must read own write
can tolerate seconds stale
can reconcile asynchronously
```

Sau đó mới chọn replication/read đường dẫn (path / 경로). Chọn “strong consistency toàn bộ” hoặc “eventual toàn bộ” trước khi phân loại tải công việc (workload / 워크로드) thường tạo chi phí (cost / 비용) hoặc tính đúng đắn (correctness / 정확성) bài toán (problem / 문제) không cần thiết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **18. Consistency chính sách (policy / 정책) cũng là sức chứa (capacity / 용량) chính sách (policy / 정책)** đã nêu tiêu chí phân biệt, còn **19. dữ liệu (data / 데이터) residency và ranh giới bảo mật (security boundary / 보안 경계) đi cùng replication topology** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **20. bằng chứng vận hành (production evidence / 운영 증거) phải reconstruct authority + lịch sử (history / 이력) timeline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. dữ liệu (data / 데이터) residency và ranh giới bảo mật (security boundary / 보안 경계) đi cùng replication topology

Dữ liệu (data / 데이터) nào được replicate sang region nào là cả hiệu năng (performance / 성능), privacy, compliance và blast-radius quyết định (decision / 결정). Logs, backups, caches và tìm kiếm (search / 검색) indexes cũng là replicas theo nghĩa quản trị (governance / 거버넌스) dù ứng dụng (application / 애플리케이션) kiến trúc (architecture / 아키텍처) không gọi chúng như vậy.

Định danh (identity / 식별자)/KMS topology cần phù hợp: region có thể autonomous khi mạng (network / 네트워크) partition hay mọi decrypt/auth thao tác (operation / 연산) vẫn phụ thuộc điều khiển (control / 제어) plane toàn cục (global / 전역)?

> **Chuyển mạch:** Trong **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **19. dữ liệu (data / 데이터) residency và ranh giới bảo mật (security boundary / 보안 경계) đi cùng replication topology** đã nêu tiêu chí phân biệt, còn **20. bằng chứng vận hành (production evidence / 운영 증거) phải reconstruct authority + lịch sử (history / 이력) timeline** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **21. thất bại (failure / 실패) testing phải bao gồm partial thất bại (failure / 실패), không chỉ kill tiến trình (process / 프로세스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. bằng chứng vận hành (production evidence / 운영 증거) phải reconstruct authority + lịch sử (history / 이력) timeline

Bằng chứng (evidence / 증거) hữu ích:

```text
Replication:
- leader/term/epoch
- commit/durable/applied frontier per replica
- send/receive/apply lag
- snapshot/catch-up state

Network:
- inter-region RTT/loss/retransmission
- bandwidth/queue saturation

Storage:
- WAL/log flush latency per region
- replica persistence latency

Traffic:
- read/write routing by region
- failover/retry rate
- redirected load and queue wait

Correctness:
- stale-read/session-token violations
- conflict/repair events
- fencing/promotion history
```

Một “replication lag = 0” chỉ số (metric / 지표) không chứng minh no split-brain; một leader election log không chứng minh replica lưu trữ (storage / 저장소) healthy. Cần nối authority và dữ liệu (data / 데이터) frontier.

> **Chuyển mạch:** Ở chặng này của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **20. bằng chứng vận hành (production evidence / 운영 증거) phải reconstruct authority + lịch sử (history / 이력) timeline** nêu điều cần giải thích; **21. thất bại (failure / 실패) testing phải bao gồm partial thất bại (failure / 실패), không chỉ kill tiến trình (process / 프로세스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **22. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. thất bại (failure / 실패) testing phải bao gồm partial thất bại (failure / 실패), không chỉ kill tiến trình (process / 프로세스)

Kiểm thử (test / 테스트) đáng giá:

```text
partition leader khỏi subset replicas
inject asymmetric packet loss/latency
slow one replica storage
expire lease/fencing boundary
fail leader với outstanding acknowledged/unacknowledged writes
route reads tới lagging replica
promote rồi rejoin old leader
simulate capacity after full-region traffic shift
```

Sau kiểm thử (test / 테스트), kiểm tra data-loss cửa sổ (window / 윈도우) đúng đặc tả hợp đồng (contract / 계약), no dual authority, session/read consistency đúng chính sách (policy / 정책) và old leader không thể mutate trạng thái (state / 상태) sau fencing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **21. thất bại (failure / 실패) testing phải bao gồm partial thất bại (failure / 실패), không chỉ kill tiến trình (process / 프로세스)** xác định đầu vào; **22. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **23. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?

Nếu người dùng (user / 사용자) đọc stale dữ liệu (data / 데이터), consistency/read-routing frontier quyết định hành vi (behavior / 동작). Nếu failover mất dữ liệu (data / 데이터), ack/replication/persistence quy tắc (rule / 규칙) mới là trọng tâm. Nếu outage lan sang region khỏe, sức chứa (capacity / 용량)/thử lại (retry / 재시도) phản hồi (feedback / 피드백) có thể là gốc (root / 루트) cơ chế (mechanism / 메커니즘). Nếu two primaries cùng ghi, authority/fencing giao thức (protocol / 프로토콜) là bất biến (invariant / 불변식) bị phá.

> **Chuyển mạch:** Trong **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **23. Mô hình tư duy** gom các mảnh từ **22. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Mô hình tư duy

> Multi-region replication là bài toán **phân phối authority, lịch sử (history / 이력) và sức chứa (capacity / 용량) qua khoảng cách**. Synchronous coordination trả độ trễ (latency / 지연 시간) để làm lần ghi nhận (commit / 커밋) frontier mạnh hơn; asynchronous replication đổi độ trễ (latency / 지연 시간) lấy thất bại (failure / 실패) cửa sổ (window / 윈도우); replica reads đổi freshness lấy locality; failover là chuyển authority được fencing, không phải chỉ đổi tuyến (route / 경로). **toàn cục (global / 전역) coordination chỉ nên đặt ở bất biến (invariant / 불변식) cần nó, còn bằng chứng vận hành (production evidence / 운영 증거) phải theo dõi cả authority frontier lẫn dữ liệu (data / 데이터) frontier.**

> **Chuyển mạch:** Ở chặng này của **Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý**, **Kết nối** gom các mảnh từ **23. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Ôn [distributed consistency foundation](../../basic/06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [replication/consensus foundation](../../basic/06_networks_distributed_systems/05_replication_partitioning_and_consensus.md), đọc [failure detectors](./01_failure_detectors_membership_and_gossip.md), [leases/fencing](./02_leases_fencing_tokens_and_split_brain_prevention.md), [consensus internals](./03_consensus_log_replication_reconfiguration_and_snapshots.md), [time/causality](./06_time_clocks_ordering_and_causality.md), [MVCC/WAL](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
