# Load balancing algorithms, connection pools và locality

Load balancer không đơn giản là “chia request đều”. Mục tiêu thực tế là phân phối work sao cho resources không bị hotspot, giữ latency ổn định và tận dụng locality mà không tạo coupling quá mạnh.

## Round robin và weighted round robin

Round robin phù hợp khi requests có cost gần nhau và backends tương đương. Nếu instance sizes khác nhau, weighted round robin phản ánh capacity tương đối.

Nhưng số request không bằng amount of work. Một report query 5 giây và health check 2 ms đều chỉ là một request.

## Least connections và least outstanding

Least-connections dùng active connections như proxy cho load. Với HTTP/2 multiplexing hoặc connection pooling, connection count có thể không phản ánh concurrent requests.

Least-outstanding-requests gần work hơn nhưng vẫn không biết request cost tương lai. Adaptive algorithms có thể dùng observed latency/load.

## Power of two choices

Chọn ngẫu nhiên hai backends rồi gửi tới backend nhẹ hơn tạo load balance rất tốt với overhead thấp trong nhiều mô hình. Insight là một chút state/comparison đã giảm hotspot mạnh so với pure random.

## Connection pool

Mỗi request mở TCP/TLS/database connection mới rất đắt. Pool amortize handshake và giới hạn concurrency downstream.

Pool size không nên “càng lớn càng tốt”. Pool lớn có thể đẩy database vượt capacity; pool nhỏ quá tạo queue ở application. Pool là admission-control boundary trá hình.

## Queue ở đâu?

Nếu request phải chờ, queue có thể nằm ở load balancer, app pool, thread pool hoặc database. Nhiều queues nối tiếp làm tail latency khó nhìn và timeout budget bị tiêu âm thầm.

Tốt hơn là có bounded queue rõ ràng gần resource bottleneck và reject/load-shed sớm khi capacity cạn.

## Locality

Cache locality, zone locality và data shard locality có thể làm một backend “gần” request hơn. Consistent hashing hoặc locality-aware routing giảm cache misses và cross-zone traffic.

Nhưng locality quá cứng tạo hotspot khi một key/user quá nóng. Hệ thống cần escape path để rebalance.

## Sticky session

Session affinity đơn giản hóa in-memory session nhưng làm failover/rebalancing khó và giảm elasticity. External/shared session state hoặc stateless token có trade-off khác về consistency/security.

## Health checking

Backend trả TCP 200/health endpoint không nghĩa đủ khỏe để nhận thêm load. Overloaded node có thể vẫn “healthy”. Passive latency/error signals và outlier detection giúp routing phản ánh runtime condition.

## Mental Model

> Load balancing là control loop giữa demand và heterogeneous capacity. Routing algorithm, pool và locality cùng quyết định nơi queue hình thành. Mục tiêu không phải request count đẹp mà là giữ từng bottleneck trong safe operating region.