# Failure detectors, membership và gossip protocols

Trong một process đơn lẻ, crash thường rõ ràng: process biến mất. Trong distributed system, node A không nhận response từ node B không đủ để kết luận B đã chết. B có thể crash, network có thể partition, packet có thể mất, B có thể pause vì GC hoặc A có thể đang quá tải. **Failure detection** vì thế là reasoning dưới uncertainty.

## Timeout là một giả định về thời gian

Khi đặt timeout 2 giây, hệ thống không chứng minh peer đã chết sau 2 giây. Nó tuyên bố: “nếu chưa có response sau khoảng này, ta sẽ hành động như thể peer không còn usable cho mục tiêu hiện tại”.

Timeout quá ngắn tăng false suspicion; quá dài làm failover chậm. Giá trị đúng phụ thuộc latency distribution, workload, network và hậu quả của false positive.

## Perfect failure detector khó đạt trong asynchronous system

Trong model hoàn toàn asynchronous, không có upper bound chắc chắn cho message delay hoặc process pause. Một node chậm không thể phân biệt hoàn hảo với node chết chỉ bằng việc chờ.

Distributed algorithms vì thế thường dựa trên failure detector có property yếu hơn hoặc giả định partial synchrony: sau một thời điểm nào đó, timing trở nên đủ ổn định để protocol tiến triển.

## Heartbeat và suspicion

Heartbeat định kỳ cung cấp evidence peer còn hoạt động. Nhưng “không thấy heartbeat” chỉ tạo **suspicion**, không phải sự thật tuyệt đối. Hệ thống trưởng thành thường có intermediate state: alive → suspect → failed/dead, thay vì flip ngay từ healthy sang dead.

Accrual failure detector thậm chí có thể tính suspicion score dựa trên lịch sử inter-arrival time thay vì fixed threshold cứng.

## Membership là distributed state

Cluster cần biết node nào thuộc group, incarnation/version nào hiện tại và thay đổi nào mới hơn. Nếu node rời rồi quay lại cùng identifier mà không có generation/incarnation, message cũ có thể làm state mới bị ghi đè.

Membership protocol vì thế thường gắn monotonic incarnation/version để phân biệt “node A trước restart” và “node A sau restart”.

## Gossip lan truyền information theo xác suất

Trong **gossip protocol (가십 프로토콜)**, mỗi node định kỳ trao đổi state với một số peer. Information lan ra theo nhiều vòng giống epidemic dissemination.

Gossip tránh coordinator trung tâm và scale tốt vì mỗi node chỉ giao tiếp với subset nhỏ. Đổi lại convergence không tức thời; trong một khoảng thời gian, các node có thể có membership view khác nhau.

## Anti-entropy và reconciliation

Gossip không nhất thiết gửi toàn bộ state mỗi lần. Node có thể trao digest/version rồi chỉ đồng bộ phần khác biệt. Anti-entropy giúp state cuối cùng hội tụ dù message bị mất hoặc node tạm thời disconnected.

Thiết kế phải có rule merge rõ ràng: version, timestamp, vector metadata hoặc domain-specific conflict resolution. “Gửi state cho nhau” không tự tạo consistency.

## Failure detector tác động tới consensus

Consensus safety không nên phụ thuộc vào việc failure detector đoán luôn đúng; false suspicion không được phép khiến hai leaders cùng commit conflicting history. Nhưng liveness thường cần timing assumption để cuối cùng chọn được leader ổn định.

Đây là phân biệt quan trọng: **safety** phải giữ ngay cả khi network xấu; **liveness** có thể tạm dừng cho tới khi communication đủ tốt.

## Operational example

Nếu Kubernetes-like control plane đánh dấu node unavailable quá nhanh khi có network jitter, workload có thể bị reschedule dù node cũ vẫn chạy. Nếu fencing không đủ mạnh, hai nơi có thể cùng tin mình đang phục vụ cùng resource. Failure detection vì thế phải đi cùng lease/fencing, không chỉ heartbeat.

## Mental model

> Failure detector không trả lời “peer có thật sự chết không?”; nó cung cấp một mức suspicion đủ để protocol ra quyết định. Membership là replicated state có version; gossip là cơ chế dissemination eventual. Correctness đến từ việc thiết kế hệ thống chịu được false suspicion, stale view và delayed message.