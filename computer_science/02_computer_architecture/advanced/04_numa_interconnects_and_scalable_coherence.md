# NUMA, interconnects và scalable coherence

Khi một máy có nhiều cores và nhiều memory controllers, giả định “RAM có cùng latency ở mọi nơi” bắt đầu sai. **NUMA — Non-Uniform Memory Access (비균일 메모리 접근)** mô tả hệ thống trong đó access tới memory gần core hiện tại rẻ hơn access phải đi qua interconnect tới node/socket khác.

## Vì sao UMA không scale mãi

Nếu mọi core chia sẻ một memory bus duy nhất, số core tăng làm bandwidth contention và coherence traffic tăng. Server nhiều socket vì thế phân bố memory controllers theo node. Mỗi CPU socket có local memory channels, đồng thời có interconnect để truy cập remote memory và trao đổi coherence messages.

Latency remote không chỉ thêm vài nanosecond cố định. Nó còn cạnh tranh interconnect bandwidth và có thể thay đổi theo topology, queueing và traffic từ core khác.

## First-touch và memory placement

OS thường cấp physical page theo **first-touch policy**: page được đặt gần NUMA node của thread chạm vào nó lần đầu. Nếu một thread khởi tạo toàn bộ array rồi worker ở socket khác xử lý, data có thể bị đặt lệch node dù workload sau đó song song.

Điều này giải thích vì sao initialization strategy ảnh hưởng performance. Parallel initialization đôi khi quan trọng không vì CPU cost mà vì nó quyết định physical placement.

## Thread affinity

Scheduler có thể migrate thread giữa cores để cân bằng CPU load. Nhưng migration làm cache nóng trở thành lạnh và có thể biến local memory thành remote memory. **CPU affinity** hoặc NUMA-aware scheduling cố giữ computation gần data khi lợi ích locality lớn hơn lợi ích load balancing.

Không nên pin mọi thread một cách máy móc. Pinning sai có thể tạo imbalance hoặc ngăn scheduler phản ứng với workload biến động.

## Interconnect và coherence directory

Snooping đơn giản yêu cầu broadcast coherence request tới nhiều participants, khó scale khi core count tăng. Directory-based coherence lưu metadata về nơi line đang được cache để gửi invalidation/query có mục tiêu hơn.

Directory cũng có cost: metadata, lookup latency và traffic khi line được chia sẻ rộng. Một hot writable cache line giữa nhiều sockets có thể “ping-pong” qua interconnect và trở thành bottleneck nghiêm trọng.

## False sharing ở cấp NUMA

False sharing trong một socket đã đắt; qua socket còn đắt hơn. Hai threads cập nhật hai counters khác nhau nhưng cùng cache line có thể khiến ownership của line di chuyển liên tục giữa NUMA nodes.

Padding/alignment có thể giúp trong hot counters, nhưng tăng memory footprint. Quyết định cần dựa trên measurement thay vì áp dụng mọi nơi.

## Database và JVM

Database buffer pool lớn, JVM heap lớn hoặc in-memory analytics đều có thể trải trên nhiều NUMA nodes. Nếu allocator, GC thread và application thread không NUMA-aware, latency có thể tăng dù tổng RAM còn dư.

GC concurrent/parallel cũng tương tác với topology: collector threads quét object ở remote node tạo bandwidth traffic. Một số runtime và allocator cung cấp NUMA-aware policy để cải thiện locality.

## Scale-up và scale-out

NUMA cho thấy scale-up server không phải một “máy lớn đồng nhất”; bên trong nó đã có đặc tính distributed ở mức nhỏ: locality, topology, remote access và coordination cost. Đây là connection quan trọng sang distributed systems.

Scale-out qua network có latency lớn hơn nhiều, nhưng mental model tương tự: đặt computation gần data, giảm shared mutable state và tránh communication không cần thiết.

## Mental Model

> NUMA biến vị trí thành một phần của performance model. Memory không chỉ có dung lượng; mỗi byte còn có topology. Khi hệ thống lớn lên, câu hỏi “data ở đâu so với computation?” trở thành câu hỏi kiến trúc.