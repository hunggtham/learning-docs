# Caching consistency, invalidation, stampede và hot keys

Cache giảm latency và load bằng cách giữ bản sao state gần consumer hơn. Nhưng ngay khi có thêm một bản sao, hệ thống phải trả lời: **source of truth ở đâu, stale bao lâu được chấp nhận, update/invalidation được ordering thế nào, và backend sống sót ra sao khi cache đồng loạt miss hoặc biến mất.**

Một cache vì thế không chỉ là data structure; nó là một **replication protocol có eviction policy**.

## 1. Invariant đầu tiên: phải biết authoritative state nằm ở đâu

Nếu database có `V2` nhưng cache còn `V1`, đó không tự động là bug. Nó chỉ là bug nếu freshness contract nói reader phải thấy `V2` ở thời điểm đó.

Trước khi thêm cache, cần định nghĩa contract như:

```text
strongly fresh?
bounded stale tối đa N giây?
read-your-writes cần không?
stale-while-revalidate được không?
cache failure có bypass về origin không?
```

Không có contract, team chỉ tranh luận “stale thế này có chấp nhận được không?” sau incident.

## 2. Cache-aside đơn giản nhưng có race ordering

Trong cache-aside, reader miss cache → đọc DB → populate cache. Writer thường update DB rồi invalidate/update cache.

Race điển hình:

```text
Reader miss cache → đọc DB V1
Writer ghi DB V2 → invalidate cache
Reader cũ set cache V1
```

Stale value bị resurrect. TTL cuối cùng có thể sửa nhưng window stale vẫn tồn tại.

Mitigation có thể là versioned value/key, delayed/double invalidation, write-through hoặc ordering token tùy requirement. Không có strategy universal.

## 3. TTL là freshness bound thô, không phải consistency proof

TTL chỉ định entry được reuse trong bao lâu trước refresh/expiry. TTL dài tăng hit rate nhưng stale lâu; TTL ngắn tăng origin load.

Nếu hàng nghìn keys cùng TTL và cùng populate lúc deploy, expiry đồng loạt tạo traffic spike. Jitter TTL giúp phân tán expiry.

TTL giải cleanup và bounded staleness thô, nhưng không giải read-your-writes hay race ordering tự động.

## 4. Write-through và write-behind đổi failure semantics

Write-through đặt cache trong write path; read freshness tốt hơn nhưng write latency/coupling tăng.

Write-behind ghi cache/buffer rồi flush source async; throughput có thể tốt nhưng durability, ordering và recovery trở nên khó hơn. Khi cache node chết trước flush, logical write có thể mất nếu cache đang đóng vai trò queue bền mà thực tế không durable.

Do đó cache pattern phải được đánh giá cùng durability contract, không chỉ hit rate.

## 5. Multi-layer cache làm invalidation path dài hơn

Browser, CDN, reverse proxy, service-local cache, distributed cache và DB buffer pool có thể cùng giữ state.

```text
origin DB
→ distributed cache
→ service local cache
→ CDN/proxy
→ browser
```

Fix Redis invalidation không giúp nếu CDN vẫn giữ stale response. Debugging cần biết key/version/header semantics ở từng layer.

Cache càng nhiều tầng, consistency contract càng cần rõ về nơi nào được phép stale bao lâu.

## 6. Read-your-writes là guarantee riêng

User vừa update profile rồi GET ngay có thể đọc cache cũ. Global strong consistency có thể quá đắt, nhưng session-scoped read-your-writes đôi khi đủ.

Write path có thể update/invalidate đồng bộ, response trả version token, hoặc subsequent read tạm bypass stale layer.

Điểm quan trọng là guarantee phải được thiết kế, không xuất hiện tự nhiên từ TTL.

## 7. Cache stampede là synchronized miss failure

Hot key hết hạn và hàng nghìn requests cùng miss có thể cùng gọi origin. Cache được thêm để giảm load nhưng lại biến thành trigger cho thundering herd.

Mitigation gồm:

```text
single-flight/request coalescing
stale-while-revalidate
probabilistic early refresh
per-key refresh ownership
bounded regeneration concurrency
```

Invariant performance cần là: một miss wave không được biến thành N expensive origin calls nếu regeneration có thể share.

## 8. Hot key là skew problem, không phải average-capacity problem

Consistent hashing phân keys giữa shards nhưng không chia được một key duy nhất nếu mỗi key chỉ có một owner shard.

Một key cực nóng có thể saturate shard dù cluster trung bình còn rảnh. Giải pháp có thể dùng near-cache, replication của hot value, request coalescing hoặc thay đổi data model.

Average QPS/shard che mất distribution skew. Production evidence cần per-key/per-shard tail.

## 9. Negative caching cũng có consistency cost

Lưu `not found` giúp ngăn repeated lookup cho object không tồn tại hoặc attack probing. Nhưng object vừa được tạo có thể bị che bởi negative entry cho tới TTL.

Negative TTL thường cần ngắn hơn và creation path có thể cần invalidation. Absence cũng là state cần version/freshness policy.

## 10. Versioned key giảm invalidation race bằng immutable naming

Thay vì mutate `profile:123`, system có thể dùng `profile:123:v42`. Update tạo version mới; old key tự expire.

Điều này biến invalidation thành pointer/version update, giảm một số race. Đổi lại key churn/memory footprint tăng và vẫn cần nơi authoritative để biết current version.

Versioned key là ví dụ đổi mutable-state coordination lấy immutable-state indirection.

## 11. Cache key correctness là security invariant

Nếu response semantic phụ thuộc tenant, user, locale, permission hoặc feature state nhưng cache key thiếu dimension tương ứng, system có thể trả data của principal khác.

Đây là data leak, không chỉ stale bug.

Invariant cần là:

> Mọi input ảnh hưởng tới authorization/semantic response phải được phản ánh trong cache partition/key hoặc response phải thật sự share-safe.

Caching vì vậy giao trực tiếp với security boundary.

## 12. Cache outage có thể làm origin collapse

Nếu backend được provision với steady-state miss rate 5%, cache outage/cold start có thể đưa 100% traffic về origin. Một dependency được gọi là “optional optimization” trên architecture diagram có thể là hard capacity dependency trong thực tế.

Failure chain:

```text
cache node/cluster fail
→ miss rate tăng
→ DB/origin queue tăng
→ latency + timeout tăng
→ retry tăng
→ origin overload
```

Resilience cần rate limit, circuit breaker, stale/degraded fallback hoặc origin headroom phù hợp.

## 13. Cache node failure và remapping tạo cold-start burst

Distributed cache partition bằng consistent hashing giảm lượng keys phải remap khi node thay đổi, nhưng remapped keys vẫn cold. Cache cluster event có thể tạo miss burst không đồng đều theo shard/key popularity.

Capacity test cần simulate cold cache, không chỉ benchmark steady-state warm cache.

## 14. Performance pressure và eviction interaction

Khi working set lớn hơn cache capacity, churn/eviction tăng. Hit rate có thể giảm dần hoặc collapse nếu access pattern không phù hợp replacement policy.

Large entries giảm effective key capacity. Hot/cold mix, TTL và admission policy có thể quyết định cache pollution.

Một hit-rate aggregate 99% chưa đủ nếu 1% misses chính là những keys đắt nhất.

## 15. Production evidence

Cần quan sát:

```text
hit/miss rate theo key class/shard
origin QPS do misses
stale/version mismatch events nếu đo được
refresh/coalescing contention
expiry rate
per-key hotness/skew
cache memory/eviction rate
cold-start behavior
backend latency khi cache degraded
```

Trace nên cho biết request hit layer nào, miss ở đâu và có regeneration/retry hay không.

## 16. Lower abstraction nào quyết định behavior?

Nếu stale do propagation race, ordering/version protocol quyết định. Nếu p99 tăng vì hot shard, partition/key distribution quyết định. Nếu cache outage kéo DB chết, origin capacity/backpressure quyết định. Nếu data leak qua cache, authorization/key derivation boundary quyết định.

“Redis chậm” thường chỉ là symptom-level label.

## 17. Mô hình tư duy

> Cache là **replicated, disposable state với freshness và eviction policy**. Mọi cache design phải reasoning authority, staleness, invalidation ordering, miss amplification, key correctness và origin capacity khi cache biến mất. Tối ưu hit rate mà không giữ các invariant đó chỉ dời failure sang một layer khó quan sát hơn.

## Kết nối

Đọc cùng [Capacity/admission control](./01_capacity_planning_utilization_knee_and_admission_control.md), [Load balancing và locality](./03_load_balancing_connection_pools_and_locality.md), [Distributed consistency](../../06_networks_distributed_systems/advanced/04_crdts_causal_consistency_and_conflict_resolution.md), [Authorization foundation](../../basic/07_security_reliability/02_identity_authentication_and_authorization.md) và [End-to-end overload path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).