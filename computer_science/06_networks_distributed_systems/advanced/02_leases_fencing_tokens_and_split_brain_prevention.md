# Leases, fencing tokens và split-brain prevention

Distributed lock hoặc “primary ownership” khó hơn local mutex vì client có thể pause, mất network rồi quay lại sau khi hệ thống đã trao quyền cho client khác. Nếu old owner vẫn ghi được, ta có **stale owner** và có thể corrupt state. Leases và fencing giải quyết hai phần khác nhau của vấn đề.

## Lock ownership không nên dựa vào niềm tin local

Giả sử worker A lấy lock xử lý file. Sau đó A pause 60 giây vì GC. Lock service cho rằng A timeout và cấp lock cho B. B xử lý xong. A tỉnh lại và tiếp tục write vì trong memory nó vẫn “tin” mình giữ lock.

Nếu storage chấp nhận write của A, lock timeout đã không bảo vệ correctness.

Đây là failure mode kinh điển của distributed lock không có fencing.

## Lease

Lease là quyền có thời hạn. Holder chỉ được coi có authority trước expiry theo protocol.

Lease giúp system tự thu hồi ownership khi holder mất liên lạc. Nhưng clock uncertainty, pause và delayed messages khiến holder không thể chỉ nhìn local clock rồi tuyệt đối tin quyền còn hiệu lực.

Lease protocol cần assumptions về clock drift/network delay hoặc authority central kiểm tra validity.

## Fencing token

Mỗi lần quyền được cấp, coordinator phát token đơn điệu tăng:

```text
A gets token 41
lease expires
B gets token 42
```

Storage/resource server nhớ token lớn nhất đã chấp nhận. Nếu A quay lại gửi write với 41 sau khi B đã dùng 42, storage reject 41.

Fencing biến stale-owner problem thành monotonic ordering check ở nơi side effect xảy ra.

## Vì sao fencing mạnh hơn “check lock trước write”

A có thể check lock và thấy valid, rồi pause trước write. Trong pause, lease hết và B nhận quyền mới. Khi A tiếp tục, check cũ đã stale.

Đây là TOCTOU — time-of-check to time-of-use.

Nếu write mang fencing token và resource server validate atomically, stale client không thể bypass chỉ vì check xảy ra trước pause.

## Token cần được enforce ở resource

Nếu lock service phát token nhưng database/file service không kiểm tra token, fencing chỉ là metadata trang trí.

Safety boundary phải đặt ở system thực hiện side effect: storage, state machine hoặc API owner của data.

## Leader lease

Consensus-based system có thể dùng lease để leader phục vụ read nhanh mà không quorum mỗi read, nếu đảm bảo không leader khác hợp lệ đồng thời trong interval.

Điều này thường cần clock bounds hoặc quorum interaction cẩn thận. Nếu assumptions clock sai, stale leader có thể serve stale/unsafe result.

Lease optimization luôn phải nêu rõ timing assumption.

## Split-brain

Split-brain xảy ra khi nhiều actors cùng tin mình có quyền primary/write.

Failure detector có thể gây split-brain nếu mỗi partition tự promote local node. Prevention cần một authority rule mà hai sides không cùng thỏa, thường quorum majority hoặc external fencing device/token service.

Trong cluster 3 nodes, partition 2-1 cho phép side 2 giữ majority và side 1 phải ngừng writes. Availability bị hy sinh ở minority để giữ single-writer safety.

## Epoch/term như fencing concept

Consensus protocols dùng term/epoch tăng dần. Message từ old leader term thấp có thể bị reject.

Đây là cùng mental model với fencing token, nhưng integrated vào replicated state machine protocol.

Epoch giúp phân biệt “message cũ đến muộn” với current authority.

## Database primary failover

Một standby được promote nhưng old primary chưa thật sự chết, chỉ mất network với control plane. Nếu clients hoặc storage path vẫn gửi write tới old primary, divergence xảy ra.

Production failover cần đảm bảo old primary bị **fenced**: revoke storage access, change epoch/quorum authority, disable network path hoặc mechanism tương đương.

“Promote new primary” chỉ là nửa đầu của failover; “old primary cannot write” mới hoàn tất safety.

## Distributed job ownership

Scheduler có thể phát fencing token per job attempt. Output sink chỉ accept attempt token mới nhất.

Nếu old worker chậm hoàn thành sau retry worker mới, sink reject stale result thay vì overwrite new result.

Pattern này hữu ích cho batch, workflow engine và exactly-once-like processing.

## Mental Model

> Lease trả lời **quyền có hiệu lực trong khoảng nào**; fencing token trả lời **làm sao resource từ chối owner cũ dù nó quay lại**. Split-brain prevention cần authority được enforce tại side-effect boundary.

## Common Misconceptions

**“Distributed lock timeout là đủ.”** Stale holder có thể tiếp tục sau pause nếu downstream không fence.

**“Clock đồng bộ bằng NTP nên lease tuyệt đối an toàn.”** Clock vẫn có drift/step và process pause; protocol phải dựa assumption rõ.

**“Failover xong khi standby thành primary.”** Old primary phải mất khả năng mutate state.

## Kết nối

Đọc trước [Failure detectors và membership](./01_failure_detectors_membership_and_gossip.md). Chapter consensus tiếp theo sẽ cho thấy term/epoch, quorum và log authority tạo fencing semantics ở cấp protocol.