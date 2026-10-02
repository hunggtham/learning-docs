# Consensus internals: log replication, reconfiguration và snapshots

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Consensus internals: log replication, reconfiguration và snapshots**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. máy trạng thái (state machine / 상태 머신) replication biến consensus thành bài toán thứ tự (ordering / 순서)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Term/epoch biến authority thành một thứ có thứ tự (ordering / 순서)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối consensus với log replication, reconfiguration và snapshots, để state machine giữ cùng lịch sử qua thay đổi topology.

Hệ thống phân tán (distributed system / 분산 시스템) cần consensus khi nhiều nodes phải thống nhất một chuỗi (sequence / 시퀀스) quyết định dù message delay, nút (node / 노드) crash và mạng (network / 네트워크) partition. Consensus không làm mạng (network / 네트워크) đáng tin; nó giữ một bất biến (invariant / 불변식) mạnh hơn trên nền communication không đáng tin: **không có hai histories đã lần ghi nhận (commit / 커밋) mâu thuẫn cùng được coi là authoritative trong cùng giao thức (protocol / 프로토콜) lịch sử (history / 이력).**

Ở mức advanced, cần tách **an toàn (safety / 안전)** khỏi **liveness**. an toàn (safety / 안전) hỏi “điều sai có thể xảy ra không?”; liveness hỏi “hệ thống có tiếp tục tiến triển không?”. mạng (network / 네트워크) partition có thể làm liveness dừng có chủ đích để an toàn (safety / 안전) còn giữ.

## 1. máy trạng thái (state machine / 상태 머신) replication biến consensus thành bài toán thứ tự (ordering / 순서)

Nếu replicas chạy cùng deterministic máy trạng thái (state machine / 상태 머신) và apply cùng commands theo cùng thứ tự (order / 순서), trạng thái (state / 상태) của chúng có thể hội tụ giống nhau.

Do đó vấn đề trở thành thống nhất một ordered log:

```text
command 1
command 2
command 3
...
```

Leader-based giao thức (protocol / 프로토콜) như Raft làm mô hình (model / 모델) này rõ: leader đề xuất entries, replicas ghi entries, quorum quy tắc (rule / 규칙) quyết định entry nào đủ an toàn để lần ghi nhận (commit / 커밋), rồi máy trạng thái (state machine / 상태 머신) apply committed entries theo thứ tự (order / 순서).

Bất biến (invariant / 불변식) quan trọng không phải “mọi replica luôn giống nhau tức thì”. Replica có thể lag. bất biến (invariant / 불변식) là **lịch sử (history / 이력) đã lần ghi nhận (commit / 커밋) không được bị thay bằng lịch sử (history / 이력) mâu thuẫn sau election/failover hợp lệ.**

> **Chuyển mạch:** Trong **Consensus internals: log replication, reconfiguration và snapshots**, **2. Term/epoch biến authority thành một thứ có thứ tự (ordering / 순서)** tiếp nhận điểm tựa từ **1. máy trạng thái (state machine / 상태 머신) replication biến consensus thành bài toán thứ tự (ordering / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Quorum intersection là cốt lõi (core / 핵심) an toàn (safety / 안전) argument** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Term/epoch biến authority thành một thứ có thứ tự (ordering / 순서)

Leadership không phải quyền vĩnh viễn. Term/epoch tăng qua elections. Message từ leader cũ có epoch thấp bị xem là stale.

Điều này giải quyết một thất bại (failure / 실패) phổ biến: tiến trình (process / 프로세스) cũ bị pause/mạng (network / 네트워크) partition, sau đó sống lại và vẫn tin mình là leader.

Term một mình chưa đủ; downstream side effects ngoài consensus log có thể vẫn bị old leader thực hiện. Khi cần bảo vệ bên ngoài (external / 외부) tài nguyên (resource / 자원), **fencing đơn vị từ (token / 토큰)** hoặc monotonic epoch phải được tài nguyên (resource / 자원) đó kiểm tra.

Đọc cùng [Leases, fencing tokens và split-brain prevention](./02_leases_fencing_tokens_and_split_brain_prevention.md).

> **Chuyển mạch:** Ở chặng này của **Consensus internals: log replication, reconfiguration và snapshots**, **3. Quorum intersection là cốt lõi (core / 핵심) an toàn (safety / 안전) argument** tiếp nhận điểm tựa từ **2. Term/epoch biến authority thành một thứ có thứ tự (ordering / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Append cục bộ (local / 로컬), replicate, lần ghi nhận (commit / 커밋) và apply là bốn mốc khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Quorum intersection là cốt lõi (core / 핵심) an toàn (safety / 안전) argument

Majority quorums có thuộc tính (property / 속성) mọi hai majorities giao nhau ít nhất một nút (node / 노드). Intersection giúp election/lần ghi nhận (commit / 커밋) rules mang thông tin committed lịch sử (history / 이력) sang future authority set.

An toàn (safety / 안전) không đến từ ý tưởng “đa số luôn đúng”. Nó đến từ **set intersection + giao thức (protocol / 프로토콜) rules về nút (node / 노드) nào được vote/accept lịch sử (history / 이력) nào**.

Nếu cấu hình membership thay đổi sai làm old/new quorum không còn overlap cần thiết, hệ thống (system / 시스템) có thể tạo split-brain lịch sử (history / 이력) dù mỗi phía đều thấy mình có “đa số” trong cấu hình (config / 설정) riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Consensus internals: log replication, reconfiguration và snapshots**, **4. Append cục bộ (local / 로컬), replicate, lần ghi nhận (commit / 커밋) và apply là bốn mốc khác nhau** tiếp nhận điểm tựa từ **3. Quorum intersection là cốt lõi (core / 핵심) an toàn (safety / 안전) argument** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. an toàn (safety / 안전) và durability giao nhau tại acknowledgement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Append cục bộ (local / 로컬), replicate, lần ghi nhận (commit / 커밋) và apply là bốn mốc khác nhau

Một log entry có thể ở nhiều trạng thái:

```text
accepted by leader
→ appended locally
→ replicated to followers
→ satisfies commit rule
→ applied to state machine
→ observed by client/read path
```

Trộn các mốc này dẫn tới acknowledgement bug. Nếu API hứa ghi (write / 쓰기) survive leader mất mát (loss / 손실), leader không được ack chỉ vì cục bộ (local / 로컬) append đã xong.

Lần ghi nhận (commit / 커밋) đặc tả hợp đồng (contract / 계약) còn phụ thuộc cục bộ (local / 로컬) durability: follower “có entry” nhưng chỉ ở volatile bộ nhớ (memory / 메모리) có thể không đủ cho thất bại (failure / 실패) mô hình (model / 모델) mạnh hơn.

> **Chuyển mạch:** Trong **Consensus internals: log replication, reconfiguration và snapshots**, **5. an toàn (safety / 안전) và durability giao nhau tại acknowledgement** tiếp nhận điểm tựa từ **4. Append cục bộ (local / 로컬), replicate, lần ghi nhận (commit / 커밋) và apply là bốn mốc khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. mạng (network / 네트워크) partition: nút (node / 노드) alive không có nghĩa nút (node / 노드) có authority** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. an toàn (safety / 안전) và durability giao nhau tại acknowledgement

Consensus thường được dạy ở mạng (network / 네트워크)/giao thức (protocol / 프로토콜) tầng (layer / 계층); durability thường được dạy ở lưu trữ (storage / 저장소) tầng (layer / 계층). môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) phải nối cả hai.

Một committed entry theo quorum lô-gic (logic / 논리) chỉ survive power/tiến trình (process / 프로세스) failures như đặc tả hợp đồng (contract / 계약) hứa nếu replicas giữ log theo persistence rules tương ứng.

Chuỗi nhân quả (causal chain / 인과 사슬):

```text
client write
→ leader log append
→ follower replication
→ local durable state theo policy
→ quorum commit
→ client ack
```

Nếu ack xảy ra trước durability/quorum điều kiện (condition / 조건) cần thiết, consistency giao thức (protocol / 프로토콜) có thể đúng trên giấy nhưng sản phẩm (product / 제품) durability guarantee vẫn sai.

Xem [đường durability xuyên tầng](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Chuyển mạch:** Ở chặng này của **Consensus internals: log replication, reconfiguration và snapshots**, **6. mạng (network / 네트워크) partition: nút (node / 노드) alive không có nghĩa nút (node / 노드) có authority** tiếp nhận điểm tựa từ **5. an toàn (safety / 안전) và durability giao nhau tại acknowledgement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Election hết thời gian chờ (timeout / 타임아웃) là liveness tuning, không phải tính đúng đắn (correctness / 정확성) proof duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. mạng (network / 네트워크) partition: nút (node / 노드) alive không có nghĩa nút (node / 노드) có authority

Một minority partition có thể có processes hoàn toàn khỏe, CPU thấp và disk bình thường nhưng không được lần ghi nhận (commit / 커밋) writes nếu giao thức (protocol / 프로토콜) cần quorum.

Đây là deliberate availability sự đánh đổi (trade-off / 트레이드오프) để bảo vệ single authoritative lịch sử (history / 이력).

Thất bại (failure / 실패) detector chỉ nói “tôi nghi nút (node / 노드) kia không reachable/healthy”. Consensus rules mới quyết định ai có quyền lần ghi nhận (commit / 커밋).

Không được biến suspicion thành authority bằng hết thời gian chờ (timeout / 타임아웃) đơn giản.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Consensus internals: log replication, reconfiguration và snapshots**, **7. Election hết thời gian chờ (timeout / 타임아웃) là liveness tuning, không phải tính đúng đắn (correctness / 정확성) proof duy nhất** tiếp nhận điểm tựa từ **6. mạng (network / 네트워크) partition: nút (node / 노드) alive không có nghĩa nút (node / 노드) có authority** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Log matching và leader completeness giữ lịch sử (history / 이력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Election hết thời gian chờ (timeout / 타임아웃) là liveness tuning, không phải tính đúng đắn (correctness / 정확성) proof duy nhất

Hết thời gian chờ (timeout / 타임아웃) quá ngắn có thể gây election churn khi mạng (network / 네트워크) jitter/GC pause; quá dài làm failover chậm.

Hết thời gian chờ (timeout / 타임아웃) tuning chủ yếu ảnh hưởng liveness và operational hành vi (behavior / 동작). an toàn (safety / 안전) phải đến từ term/voting/log rules, không dựa vào giả định (assumption / 가정) “hai leaders chắc không overlap vì hết thời gian chờ (timeout / 타임아웃)”.

Đây là mẫu (pattern / 패턴) quan trọng trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들): **clock/timing có thể giúp progress nhưng an toàn (safety / 안전) nên dựa vào bất biến (invariant / 불변식) giao thức (protocol / 프로토콜) khi có thể.**

> **Chuyển mạch:** Trong **Consensus internals: log replication, reconfiguration và snapshots**, **8. Log matching và leader completeness giữ lịch sử (history / 이력)** tiếp nhận điểm tựa từ **7. Election hết thời gian chờ (timeout / 타임아웃) là liveness tuning, không phải tính đúng đắn (correctness / 정확성) proof duy nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. lần ghi nhận (commit / 커밋) chỉ mục (index / 인덱스) và apply chỉ mục (index / 인덱스) không nên bị trộn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Log matching và leader completeness giữ lịch sử (history / 이력)

Leader-based consensus thường cần rules để đảm bảo candidate thiếu committed lịch sử (history / 이력) không trở thành authority rồi ghi đè lịch sử (history / 이력) đó.

Intuition cần giữ:

```text
future leader phải mang đủ committed prefix
followers không được chấp nhận arbitrary conflicting suffix
```

Xung đột (conflict / 충돌) repair được phép thay speculative/uncommitted suffix, nhưng committed prefix phải được bảo toàn theo giao thức (protocol / 프로토콜).

Đây là nơi “replication là bản sao (copy / 복사) log” trở thành state-machine giao thức (protocol / 프로토콜) thực sự.

> **Chuyển mạch:** Ở chặng này của **Consensus internals: log replication, reconfiguration và snapshots**, **9. lần ghi nhận (commit / 커밋) chỉ mục (index / 인덱스) và apply chỉ mục (index / 인덱스) không nên bị trộn** tiếp nhận điểm tựa từ **8. Log matching và leader completeness giữ lịch sử (history / 이력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Linearizable read cần chứng minh authority hiện tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. lần ghi nhận (commit / 커밋) chỉ mục (index / 인덱스) và apply chỉ mục (index / 인덱스) không nên bị trộn

Entry có thể committed nhưng máy trạng thái (state machine / 상태 머신) chưa apply kịp. Replica lag có thể đến từ mạng (network / 네트워크) replication hoặc apply thông lượng (throughput / 처리량).

Nếu read đường dẫn (path / 경로) trả trạng thái (state / 상태) tại apply chỉ mục (index / 인덱스) cũ nhưng caller tưởng đang đọc committed-latest, consistency guarantee bị yếu hơn mong đợi.

Khả năng quan sát (observability / 관측 가능성) nên phân biệt:

```text
match/replication position
commit position
applied position
```

Một replica “caught up log” chưa chắc “caught up ứng dụng (application / 애플리케이션) trạng thái (state / 상태)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Consensus internals: log replication, reconfiguration và snapshots**, **10. Linearizable read cần chứng minh authority hiện tại** tiếp nhận điểm tựa từ **9. lần ghi nhận (commit / 커밋) chỉ mục (index / 인덱스) và apply chỉ mục (index / 인덱스) không nên bị trộn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Reconfiguration là consensus trên chính membership** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Linearizable read cần chứng minh authority hiện tại

Read từ leader tưởng miễn phí vì không append log mới. Nhưng stale leader bị partition có thể chưa biết mình đã mất quorum.

Linearizable read cần cơ chế (mechanism / 메커니즘) xác nhận leader vẫn có authority/hiện tại (current / 현재) lần ghi nhận (commit / 커밋) trạng thái (state / 상태), ví dụ quorum confirmation/read-index style giao thức (protocol / 프로토콜) hoặc lease dưới timing các giả định (assumptions / 가정들) đủ mạnh.

Nếu sản phẩm (product / 제품) chỉ cần stale/eventual read, có thể chọn đường dẫn (path / 경로) rẻ hơn. Consistency guarantee phải là thiết kế (design / 설계) đầu vào (input / 입력), không phải label gắn sau hiện thực (implementation / 구현).

> **Chuyển mạch:** Trong **Consensus internals: log replication, reconfiguration và snapshots**, **11. Reconfiguration là consensus trên chính membership** tiếp nhận điểm tựa từ **10. Linearizable read cần chứng minh authority hiện tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Snapshot và log compaction phải giữ điểm nối với lịch sử (history / 이력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Reconfiguration là consensus trên chính membership

Thêm/bớt nút (node / 노드) không chỉ sửa tệp cấu hình (config file / 구성 파일). Membership quyết định quorum set, nên thay membership là thay an toàn (safety / 안전) ranh giới (boundary / 경계).

Giao thức (protocol / 프로토콜) thường dùng joint/staged cấu hình (configuration / 구성) để old và new sets overlap trong chuyển tiếp (transition / 전이).

Dạng thất bại (failure mode / 실패 모드) nguy hiểm:

```text
old config A có quorum riêng
new config B có quorum riêng
A và B không overlap đủ
→ hai groups đều có thể nghĩ mình authoritative
```

Operational tooling phải coi membership thay đổi (change / 변경) là state-machine thao tác (operation / 연산) có guardrail.

> **Chuyển mạch:** Ở chặng này của **Consensus internals: log replication, reconfiguration và snapshots**, **12. Snapshot và log compaction phải giữ điểm nối với lịch sử (history / 이력)** tiếp nhận điểm tựa từ **11. Reconfiguration là consensus trên chính membership** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Lagging replica và backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Snapshot và log compaction phải giữ điểm nối với lịch sử (history / 이력)

Log tăng vô hạn là không thực tế. Replica có thể snapshot trạng thái (state / 상태) tại một committed/applied chỉ mục (index / 인덱스) rồi bỏ prefix log cũ.

Snapshot phải gắn chính xác với chỉ mục (index / 인덱스)/term hoặc equivalent siêu dữ liệu (metadata / 메타데이터) để nút (node / 노드) biết suffix nào tiếp tục từ trạng thái (state / 상태) đó.

Dạng thất bại (failure mode / 실패 모드) gồm snapshot quá cũ, partial snapshot install, trạng thái (state / 상태) không đồng bộ với log suffix hoặc compaction xóa lịch sử (history / 이력) còn cần cho lagging replica/khôi phục (recovery / 복구).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Consensus internals: log replication, reconfiguration và snapshots**, **13. Lagging replica và backpressure** tiếp nhận điểm tựa từ **12. Snapshot và log compaction phải giữ điểm nối với lịch sử (history / 이력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. hiệu năng (performance / 성능) pressure thay đổi hành vi (behavior / 동작) ở đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Lagging replica và backpressure

Replica chậm có thể giữ WAL/log retention lâu, chiếm disk và tăng leader bộ nhớ (memory / 메모리)/mạng (network / 네트워크) pressure. Nếu leader chờ mọi replica, một nút (node / 노드) chậm có thể kéo độ trễ (latency / 지연 시간) toàn cluster; nếu chỉ chờ quorum, nút (node / 노드) đó có thể tụt xa rồi cần snapshot.

Đây là sự đánh đổi (trade-off / 트레이드오프) giữa foreground độ trễ (latency / 지연 시간) và khôi phục (recovery / 복구)/catch-up chi phí (cost / 비용).

Consensus tầng (layer / 계층) vì thế cần retention chính sách (policy / 정책), snapshot chính sách (policy / 정책) và monitoring cho lag phân phối (distribution / 분포), không chỉ “quorum còn đủ”.

> **Chuyển mạch:** Trong **Consensus internals: log replication, reconfiguration và snapshots**, **14. hiệu năng (performance / 성능) pressure thay đổi hành vi (behavior / 동작) ở đâu?** tiếp nhận điểm tựa từ **13. Lagging replica và backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. thất bại (failure / 실패) modes cần lập luận (reasoning / 추론) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. hiệu năng (performance / 성능) pressure thay đổi hành vi (behavior / 동작) ở đâu?

Consensus ghi (write / 쓰기) độ trễ (latency / 지연 시간) thường gồm:

```text
leader queue
+ local append/persistence
+ network RTT tới quorum
+ follower queue/persistence
+ commit propagation/apply
```

Khi cluster gần sức chứa (capacity / 용량), queueing có thể lớn hơn mạng (network / 네트워크) RTT. Cross-region quorum làm tail nhạy với slowest required member. Large log entry tăng serialization/mạng (network / 네트워크)/lưu trữ (storage / 저장소) pressure.

Batching/group lần ghi nhận (commit / 커밋) cải thiện thông lượng (throughput / 처리량) nhưng có thể thêm độ trễ (latency / 지연 시간) nhỏ để gom công việc (work / 작업). bất biến (invariant / 불변식) lần ghi nhận (commit / 커밋) không được yếu đi chỉ vì batching.

> **Chuyển mạch:** Ở chặng này của **Consensus internals: log replication, reconfiguration và snapshots**, **15. thất bại (failure / 실패) modes cần lập luận (reasoning / 추론) riêng** tiếp nhận điểm tựa từ **14. hiệu năng (performance / 성능) pressure thay đổi hành vi (behavior / 동작) ở đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. thất bại (failure / 실패) modes cần lập luận (reasoning / 추론) riêng

```text
leader churn do timeout/jitter
split-brain authority nếu membership/fencing sai
stale read từ old leader
replica apply lag
log growth vì lagging follower
snapshot install failure
ack quá sớm trước quorum/durability condition
external side effect từ stale leader thiếu fencing
```

Không nên gom mọi symptom thành “consensus unstable”. Mỗi thất bại (failure / 실패) vi phạm hoặc làm pressure một bất biến (invariant / 불변식) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Consensus internals: log replication, reconfiguration và snapshots**, **15. thất bại (failure / 실패) modes cần lập luận (reasoning / 추론) riêng** nêu điều cần giải thích; **16. bằng chứng vận hành (production evidence / 운영 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) tốt phải reconstruct giao thức (protocol / 프로토콜) trạng thái (state / 상태):

```text
current term/epoch và leader identity
membership/config version
per-replica match/commit/applied positions
replication lag theo bytes/time
quorum health và election frequency
append/fsync latency
network RTT/loss giữa members
snapshot create/install state
rejected stale-term/fencing events
client retry/timeout rate
```

Log statement “became leader” đơn lẻ không đủ. sự cố (incident / 인시던트) cần timeline election → quorum → lần ghi nhận (commit / 커밋) positions → máy khách (client / 클라이언트) acknowledgements.

> **Chuyển mạch:** Trong **Consensus internals: log replication, reconfiguration và snapshots**, **16. bằng chứng vận hành (production evidence / 운영 증거)** nêu điều cần giải thích; **17. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?

Nếu lần ghi nhận (commit / 커밋) p99 tăng, nguyên nhân có thể là lưu trữ (storage / 저장소) flush hoặc mạng (network / 네트워크) hàng đợi (queue / 큐), không phải election lô-gic (logic / 논리). Nếu leader churn khi GC pause, thời gian chạy (runtime / 런타임) stop-the-world hành vi (behavior / 동작) có thể quyết định liveness. Nếu stale leader vẫn làm bên ngoài (external / 외부) ghi (write / 쓰기), tài nguyên (resource / 자원) fencing ranh giới (boundary / 경계) mới là nơi tính đúng đắn (correctness / 정확성) phải được enforce.

Consensus thuật toán (algorithm / 알고리즘) là lớp trừu tượng (abstraction / 추상화) trung tâm nhưng môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작) phụ thuộc OS/thời gian chạy (runtime / 런타임)/mạng (network / 네트워크)/lưu trữ (storage / 저장소) dưới nó.

> **Chuyển mạch:** Ở chặng này của **Consensus internals: log replication, reconfiguration và snapshots**, **18. Mô hình tư duy** gom các mảnh từ **17. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Mô hình tư duy

> Consensus quản lý **một lịch sử (history / 이력) có authority dưới partial thất bại (failure / 실패)**. Quorum intersection + voting/log rules giữ an toàn (safety / 안전); term/epoch phân biệt authority qua thời gian; durability nối committed lịch sử (history / 이력) với lưu trữ (storage / 저장소); reconfiguration giữ quorum overlap; snapshots nén lịch sử (history / 이력) mà không được mất điểm nối; bằng chứng vận hành (production evidence / 운영 증거) phải chỉ ra term, quorum và log positions chứ không chỉ nút (node / 노드) health.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Consensus internals: log replication, reconfiguration và snapshots**, **Kết nối** gom các mảnh từ **18. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [Failure detectors và membership](./01_failure_detectors_membership_and_gossip.md), [Leases/fencing](./02_leases_fencing_tokens_and_split_brain_prevention.md), [Time/causality](./06_time_clocks_ordering_and_causality.md), [Distributed transactions](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md) và [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Giữ lại quorum intersection, term/epoch authority, commit-vs-apply, membership overlap và snapshot boundary trước khi đọc tiếp. Sang [Time, clocks and causality](./06_time_clocks_ordering_and_causality.md) để kiểm tra ordering assumptions, hoặc [Distributed transactions](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md) khi log authority phải phục vụ workflow nghiệp vụ; quay về [README](./README.md) để xác nhận owner.
