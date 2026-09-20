# Caching, load balancing và CDNs

Khi system lớn lên, hai câu hỏi lặp lại: làm sao tránh lặp lại work/data transfer đắt, và làm sao phân phối work qua nhiều resources? Caching trả lời câu đầu; load balancing trả lời câu hai; CDN kết hợp cả hai theo geography/network topology.

## Cache là bản sao có điều kiện

Cache giữ copy của data/computation gần nơi sử dụng hơn hoặc trên medium nhanh hơn. Nhưng copy tạo consistency problem: source thay đổi thì cache stale.

Mỗi cache design phải trả lời key, value, eviction, freshness và invalidation. “Thêm Redis” không trả lời các câu đó.

## Cache-aside

Application đọc cache trước; miss thì đọc source, ghi cache rồi trả. Write thường update source và invalidate cache.

Race có thể xảy ra: request A miss, request B update source + invalidate, rồi A ghi old value trở lại cache. Solutions phụ thuộc versioning, short TTL hoặc coordinated write strategy.

## TTL và staleness budget

Time-to-live đặt upper bound thực dụng cho freshness nhưng không đảm bảo exact invalidation moment. Short TTL tăng source load; long TTL tăng stale window.

Business requirement nên nói “stale tối đa bao lâu chấp nhận được” thay vì “cache phải luôn mới”.

## Eviction

Cache capacity hữu hạn nên cần eviction policy như LRU, LFU, CLOCK hoặc adaptive variants. Workload scan có thể phá LRU; skewed popularity làm LFU hữu ích hơn.

Eviction policy là online algorithm vì không biết future accesses.

## Cache stampede

Khi hot key hết hạn, hàng nghìn requests cùng miss và cùng hit backend. Single-flight/request coalescing, jittered TTL và stale-while-revalidate là mitigations.

Đây là ví dụ synchronization problem ở system level.

## Load balancing

Load balancer chọn backend cho request. Strategies gồm round robin, least connections, weighted variants, consistent hashing hoặc locality-aware routing.

Nếu backends heterogeneous hoặc requests cost khác nhau, simple round robin có thể tạo imbalance.

Health check phải phân biệt process alive với service capable of useful work. Một server overloaded có thể technically return health 200 nhưng không nên nhận thêm load.

## Layer 4 và Layer 7

L4 load balancer route theo transport connection/IP/port. L7 hiểu HTTP-level data như host/path/header để route richer policy.

L7 flexibility có CPU/parsing/TLS overhead và larger attack surface.

## Consistent hashing

Hashing key lên ring/space giúp remap fraction nhỏ keys khi nodes add/remove, hữu ích cho caches/shards.

Virtual nodes cải thiện balance. Tuy nhiên consistent hashing không tự xử lý hot keys hoặc heterogeneous capacity nếu không weighting.

## CDN

Content Delivery Network đặt edge caches gần users/network peering points. Static assets rất phù hợp; dynamic content có thể use edge compute, origin shielding hoặc cacheable APIs.

Cache key phải bao gồm dimensions làm response khác nhau. Bỏ `Accept-Encoding`, auth state hoặc locale khỏi key có thể trả sai data; include quá nhiều dimensions lại phá hit rate.

## Common Misconceptions

**“Cache luôn làm nhanh hơn.”** Cold miss, serialization, network hop và invalidation complexity có thể khiến cache không đáng cho cheap data.

**“Load balancer giải scaling.”** Backend bottleneck chung như database vẫn có thể choke toàn system.

**“CDN chỉ là mirror static files.”** Modern CDNs còn TLS termination, routing, DDoS absorption và edge computation, nhưng core mental model vẫn là placement/caching gần client.

## Mental Model

> Caching đổi freshness/complexity lấy latency/load; load balancing đổi single-resource simplicity lấy coordination. Cả hai chỉ đúng khi key, health và failure semantics rõ.

## Kết nối

Xem [online algorithms](../01_algorithms_data_structures/10_randomized_approximation_and_online_algorithms.md), [performance/capacity](./02_performance_capacity_and_scalability.md), [Internet routing](../06_networks_distributed_systems/07_routing_protocols_and_the_internet.md) và [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md).