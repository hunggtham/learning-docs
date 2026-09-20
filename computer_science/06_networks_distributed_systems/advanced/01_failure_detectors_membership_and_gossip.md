# Failure detectors, membership và gossip protocols

Trong distributed system, node không thể trực tiếp biết “node kia đã chết”. Nó chỉ biết **message/reply chưa đến trong một khoảng thời gian**. Network delay, GC pause, CPU saturation, packet loss và process crash đều có thể tạo cùng observation. Vì vậy failure detection là bài toán suy luận dưới uncertainty.

## Timeout chỉ tạo suspicion

Nếu A ping B và sau 1 giây không có reply, A có thể suspect B. Nhưng B có thể vẫn sống, chỉ chậm hoặc network partition.

Timeout ngắn phát hiện nhanh nhưng false positive nhiều. Timeout dài giảm false positive nhưng failover chậm.

Không có threshold hoàn hảo nếu network delay không có upper bound chắc chắn.

## Perfect failure detector là abstraction mạnh

Theory distributed systems mô tả failure detectors theo properties như completeness và accuracy.

Perfect detector lý tưởng cuối cùng phát hiện mọi process crash và không nghi nhầm process đúng. Trong asynchronous network thuần, guarantee này không thực tế vì “rất chậm” không phân biệt được với “đã chết”.

Production systems vì vậy dùng eventually-accurate assumptions, heartbeats và adaptive timeout.

## Membership là state machine riêng

Cluster cần biết tập members: joining, alive, suspect, leaving, dead.

Membership không chỉ là một list IP. Nó cần version/epoch/incarnation để phân biệt old information với node restart.

Nếu node B restart với cùng address nhưng incarnation mới, gossip cũ nói “B dead” không được phép giết membership mới.

## Heartbeat

Node gửi heartbeat định kỳ hoặc peers chủ động probe nhau. Missing heartbeats tạo suspicion.

Central coordinator đơn giản nhưng thành bottleneck/single dependency. All-to-all heartbeat scale `O(n^2)` messages. Large clusters thường dùng subset probing + gossip.

## Gossip

Mỗi round, node trao đổi membership/state với một số peers ngẫu nhiên. Information lan truyền epidemic-style.

Gossip có ưu điểm decentralized, robust và message cost per node thấp hơn broadcast toàn cluster. Đổi lại, convergence không instant và state tạm thời không đồng nhất.

Một node có thể biết failure trước node khác; protocol sử dụng membership phải chịu được điều đó.

## SWIM intuition

Family protocol như SWIM tách failure detection và information dissemination. Node probe target; nếu direct ping fail, có thể nhờ một số peers indirect ping để phân biệt local path issue.

Sau suspicion, status được piggyback qua gossip.

Chi tiết implementation khác nhau, nhưng mental model quan trọng là **randomized probing + suspicion + epidemic dissemination**.

## False positive nguy hiểm hơn tưởng tượng

Nếu suspect lập tức trigger leader election, shard reassignment và data replication, một network hiccup nhỏ có thể tạo “recovery storm”.

Membership layer cần hysteresis/suspicion period và downstream control plane cần rate limit remediation.

Failure detector không nên tự động biến uncertainty thành destructive action quá sớm.

## Partition

Hai halves của cluster có thể cùng nghĩ phía kia dead. Nếu cả hai tiếp tục nhận writes như primary, split-brain xảy ra.

Membership/failure detector không tự giải split-brain. Cần quorum, consensus, lease/fencing hoặc external authority để quyết định ai có quyền mutate shared state.

Đây là lý do “health check fail” không tương đương “safe to promote standby”.

## Phi accrual detector

Thay vì binary timeout cố định, detector có thể tính suspicion level dựa distribution heartbeat intervals. Phi accrual trả continuous score biểu diễn observation hiện tại bất thường mức nào so history.

Điều này thích ứng latency variation tốt hơn fixed timeout trong một số systems, nhưng vẫn không biến uncertainty thành certainty.

## Clock và timer assumptions

Failure detection dùng local timeouts nên phụ thuộc timer scheduling và process pauses. Long GC stop-the-world có thể làm node khỏe bị peers suspect.

Production tuning phải xem GC, CPU starvation, event-loop stalls và network tail latency cùng nhau.

## Membership change và state ownership

Khi member set đổi, shard ownership hoặc replica placement có thể phải rebalance. Nếu membership flaps, data movement liên tục tạo load lớn.

Do đó stable membership và controlled reconfiguration là prerequisite cho storage cluster khỏe.

## Mental Model

> Failure detector không nói “ai chết”; nó cung cấp **suspicion signal dưới timing assumptions**. Membership biến signals đó thành versioned cluster view; safety-critical ownership phải dựa thêm quorum/consensus/fencing.

## Common Misconceptions

**“Ping timeout = node chết.”** Chỉ là một observation không có reply đúng hạn.

**“Gossip cho mọi node state giống nhau ngay.”** Gossip converges dần và chấp nhận temporary inconsistency.

**“Detect failure là đủ để failover an toàn.”** Failover mutation authority cần fencing/quorum để tránh split-brain.

## Kết nối

Tiếp theo đọc [Leases, fencing tokens và split-brain prevention](./02_leases_fencing_tokens_and_split_brain_prevention.md). Sau đó consensus internals giải thích cách cluster đồng ý durable log/state transitions.