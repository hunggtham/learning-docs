# Caching consistency, invalidation và stampede ở quy mô lớn

Cache giảm latency và load bằng cách giữ bản sao gần consumer. Nhưng ngay khi có nhiều bản sao, hệ thống phải trả lời: **bản nào mới nhất, khi nào stale được chấp nhận, ai invalidates và điều gì xảy ra khi cache miss đồng loạt?** “Cache cho nhanh” thực chất là một consistency protocol thu nhỏ.

## Cache là replicated state

Database có value `V2`, cache vẫn giữ `V1`. Đây không phải anomaly lạ; nó là trạng thái tự nhiên nếu cache refresh/invalidation chưa xảy ra.

Vì vậy trước khi thêm cache cần định nghĩa freshness contract:

```text
strongly fresh?
stale tối đa 5s?
stale-while-revalidate được?
read-your-writes cần không?
```

Không có contract, team sẽ tranh luận bug bằng cảm giác.

## Cache-aside

Application đọc cache; miss thì đọc DB rồi populate cache. Write thường update DB rồi invalidate cache.

Pattern đơn giản nhưng race tồn tại:

```text
Reader miss cache -> đọc DB V1
Writer ghi DB V2 -> invalidate cache
Reader sau đó set cache V1
```

Cache bị resurrect stale value. TTL cuối cùng sửa nhưng window stale có thể dài.

Mitigation có thể dùng version, write-through, delayed invalidation hoặc ordering mechanisms tùy requirement.

## Write-through và write-behind

Write-through cập nhật cache trong write path, giảm stale reads nhưng tăng coupling/latency.

Write-behind ghi cache trước rồi flush backend async, throughput tốt nhưng durability/failure semantics phức tạp hơn nhiều.

Một cache pattern không thể đánh giá chỉ bằng hit rate; phải tính write consistency và failure recovery.

## TTL

TTL là cơ chế đơn giản để bounded staleness và cleanup. Nhưng expiry đồng loạt của hot keys có thể gây burst backend.

Thêm random jitter vào TTL giúp spread expirations.

TTL dài tăng hit rate nhưng stale lâu; TTL ngắn tăng backend load. Đây là explicit trade-off consistency–capacity.

## Cache stampede

Hot key hết hạn, hàng nghìn requests cùng miss và cùng query DB. Cache vốn được thêm để bảo vệ DB lại biến thành synchronized thundering herd.

Mitigations:

```text
single-flight/request coalescing
probabilistic early refresh
stale-while-revalidate
lock per hot key
distributed refresh ownership
```

Mục tiêu là chỉ một số nhỏ requests làm expensive regeneration.

## Negative caching

Cache “not found” giúp ngăn repeated miss với keys không tồn tại hoặc attack probing. Nhưng nếu object vừa được tạo, negative entry có thể che object tới TTL.

Negative TTL thường cần ngắn hơn và phải phù hợp creation semantics.

## Multi-layer cache

Browser/CDN/service local cache/distributed cache/DB buffer pool có thể cùng tồn tại.

Invalidation phải đi qua nhiều layers. Fix cache Redis nhưng CDN vẫn stale có thể khiến debugging khó.

Cần biết authoritative source và headers/version keys ở từng boundary.

## Versioned key

Thay vì mutate `user:123`, key có thể chứa version/hash như `profile:123:v42`. New version không conflict old; old entries tự expire.

Pattern này đơn giản hóa invalidation khi version dễ xác định, đổi lại key churn/memory footprint tăng.

## Read-your-writes

User vừa update profile rồi ngay lập tức GET có thể đọc stale cache. Nếu UX yêu cầu read-your-writes, write path có thể update/invalidate cache đồng bộ hoặc response/session tạm bypass cache.

Global strong consistency cho mọi user có thể quá đắt; session-scoped guarantee thường đủ.

## Distributed cache partitioning

Consistent hashing/sharding phân keys giữa cache nodes. Node failure remap subset keys và tạo miss burst vào backend.

Failover capacity phải tính **cache cold-start**. Backend chịu steady-state 5% misses có thể không chịu 60% misses sau cache cluster event.

Cache availability và origin capacity liên kết chặt.

## Hot key

Một key cực nóng có thể bão hòa một shard dù total cluster capacity còn nhiều. Replicate hot value, client-side caching hoặc request coalescing có thể cần.

Average QPS per shard che mất skew distribution.

## Cache correctness và authorization

Cache key thiếu tenant/user/locale/permission dimension có thể trả data của người khác. Đây là security bug chứ không chỉ stale bug.

Key derivation phải bao gồm mọi input có thể thay đổi semantic response, hoặc response phải được thiết kế share-safe.

## Mental Model

> Cache là **một replica có policy freshness và eviction**. Mọi cache design cần trả lời authority, staleness, invalidation ordering, miss burst và key correctness.

## Common Misconceptions

**“TTL giải quyết invalidation.”** TTL chỉ bounded stale window; race và user-facing consistency vẫn cần reasoning.

**“Hit rate 99% nghĩa cache tốt.”** 1% miss có thể rơi đúng hot/expensive keys; tail/origin load mới quyết định.

**“Cache chỉ ảnh hưởng performance.”** Cache key sai có thể gây data leak và correctness bugs.

## Kết nối

Chapter này nối distributed consistency với software system capacity. Database buffer pool cũng là cache nhưng nằm dưới transaction/storage semantics; CDN cache thêm HTTP validation/ETag semantics ở network layer.