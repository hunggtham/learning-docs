# Consensus internals: log replication, reconfiguration và snapshots

Distributed system cần consensus khi nhiều nodes phải thống nhất một sequence quyết định dù message delay, node crash và network partition. Consensus không làm network đáng tin; nó xây protocol để một quorum đủ lớn có thể duy trì một lịch sử quyết định duy nhất.

## State machine replication

Một cách nhìn phổ biến là mọi replicas chạy cùng deterministic state machine. Nếu chúng apply cùng commands theo cùng order, state sẽ giống nhau. Vấn đề consensus trở thành thống nhất ordered log.

Leader-based protocols như Raft làm model này dễ quan sát: leader nhận commands, replicate log entries và chỉ commit khi điều kiện quorum được đáp ứng.

## Term và leadership

Leadership không phải quyền vĩnh viễn. Term/epoch tăng theo elections. Message từ leader cũ có term thấp bị reject, giúp phân biệt authority mới với stale authority.

Connection với fencing token rất trực tiếp: monotonic epoch biến “ai là leader?” thành một ordering có thể kiểm tra.

## Quorum intersection

Majority quorums có property mọi hai majorities giao nhau ít nhất một node. Intersection giúp committed history không biến mất khỏi mọi participant của election sau.

Safety đến từ overlap + voting/log rules, không phải vì “đa số luôn đúng” theo nghĩa xã hội.

## Commit và apply

Entry được append local chưa phải committed. Leader replicate entry; khi protocol xác định entry an toàn theo quorum rules, commit index tiến lên. State machine chỉ apply committed entries theo order.

Client acknowledgement cần gắn với durability/commit contract. Ack quá sớm có thể báo success cho write chưa đủ replicated.

## Network partition

Partition có thể tạo nhóm minority vẫn chạy nhưng không thể commit writes cần quorum. Đây là deliberate availability trade-off để giữ single history.

Một node “alive” không đồng nghĩa có authority. Failure detector chỉ cung cấp suspicion; consensus rules quyết định ai được phép commit.

## Membership change

Thay cluster members nguy hiểm nếu chuyển trực tiếp từ quorum set A sang B mà hai quorums không overlap đủ. Protocol dùng joint consensus hoặc staged reconfiguration để giữ intersection trong transition.

Operational action “remove node/add node” vì vậy là consensus state change, không chỉ config file edit.

## Snapshot và log compaction

Log tăng mãi là không thực tế. Replica có thể snapshot state tại index đã apply rồi bỏ prefix log cũ. Node quá chậm có thể nhận snapshot thay vì replay hàng triệu entries.

Snapshot phải gắn với exact log index/term để state và log suffix không lệch nhau.

## Linearizable read

Read từ leader tưởng đơn giản nhưng stale leader có thể chưa biết mình mất quorum. Linearizable read cần mechanism xác nhận authority/current commit state, ví dụ quorum round hoặc lease với assumptions phù hợp.

## Mental Model

> Consensus là protocol quản lý một lịch sử có authority. Quorum intersection bảo vệ safety; terms phân biệt leadership qua thời gian; log replication truyền quyết định; snapshots nén history mà không được làm mất điểm nối với log.