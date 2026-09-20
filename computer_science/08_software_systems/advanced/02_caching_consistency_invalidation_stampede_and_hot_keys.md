# Caching consistency, invalidation, stampede và hot keys

Cache đổi storage/compute lấy latency thấp hơn, nhưng đồng thời tạo một bản sao state mới. Ngay khi có hai nơi giữ cùng logical data, câu hỏi consistency xuất hiện: bản nào authoritative, cache stale bao lâu được chấp nhận, update thất bại giữa chừng thì sao, và điều gì xảy ra khi hàng nghìn request cùng miss.

## Cache là policy, không chỉ data structure

Một cache design phải định nghĩa ít nhất: key, value, source of truth, admission, eviction, TTL, invalidation và behavior khi cache unavailable. `Map<K,V>` chỉ là cơ chế lưu; semantics nằm ở policy.

## Cache-aside

Trong **cache-aside**, application đọc cache; miss thì đọc database rồi populate cache. Write thường update database và invalidate/update cache.

Pattern này đơn giản nhưng có race. Reader có thể đọc old DB value, writer update DB + invalidate cache, rồi reader cũ ghi old value trở lại cache. TTL cuối cùng sửa stale state nhưng trong cửa sổ đó client thấy dữ liệu cũ.

Correctness cần dựa trên business tolerance: stale vài giây có thể ổn với product catalog nhưng không ổn với authorization decision hoặc account balance.

## Write-through và write-behind

Write-through cập nhật cache và backing store theo path đồng bộ, giúp read cache mới hơn nhưng tăng write latency/coupling. Write-behind buffer write rồi flush sau, tăng throughput nhưng tạo durability/order complexity.

Không có strategy “tốt nhất”; mỗi strategy chuyển cost giữa consistency, latency và failure handling.

## TTL là bounded staleness thô

TTL không đảm bảo data fresh; nó chỉ giới hạn khoảng thời gian entry tồn tại trước khi cần refresh theo clock/policy. TTL dài tăng hit rate nhưng stale lâu; TTL ngắn tăng load lên source.

Jitter TTL giúp tránh hàng loạt keys cùng expire một thời điểm.

## Cache stampede

Nếu một hot key hết hạn, hàng nghìn requests có thể cùng miss và cùng query database. Đây là **cache stampede/thundering herd**.

Single-flight/request coalescing cho một worker refresh trong khi others chờ hoặc dùng stale value. Stale-while-revalidate cho phép phục vụ value cũ trong khoảng ngắn trong khi background refresh. Cả hai biến “N miss → N backend calls” thành gần “N miss → 1 refresh”.

## Hot key

Một key cực phổ biến có thể saturate một cache shard dù tổng cluster còn capacity. Consistent hashing phân phối keys nhưng không thể chia một key duy nhất nếu mỗi key chỉ thuộc một shard.

Giải pháp có thể gồm local near-cache, replication hot key, request coalescing hoặc thay đổi key/data model. Đây là ví dụ average load che giấu skew.

## Negative caching

Nếu request liên tục hỏi một object không tồn tại, không cache “not found” sẽ gây repeated database lookup. **Negative cache** lưu absence trong TTL ngắn.

Nhưng nếu object vừa được tạo, negative entry có thể làm client tiếp tục thấy 404. Vì vậy invalidation/TTL cho absence cũng cần business semantics.

## Versioned key

Thay vì mutate cùng key, một số system dùng version trong cache key. Update tạo version mới; old entries tự hết hạn. Cách này giảm invalidation race nhưng cần nơi authoritative để biết current version và tăng memory footprint.

## Cache failure

Cache down có thể làm database nhận toàn bộ traffic vốn được cache hấp thụ. Nếu backend chỉ được provision cho miss rate 5%, cache outage có thể trở thành database outage.

Resilience design phải có circuit breaker, rate limit, fallback hoặc degraded mode. Cache không nên là “optional optimization” trên sơ đồ nhưng lại là hard dependency ẩn trong capacity model.

## Mental model

> Cache là replicated, disposable state với policy freshness. Mọi optimization hit-rate đều phải đi cùng reasoning về stale data, invalidation race, stampede, skew và backend capacity khi cache biến mất. Câu hỏi đầu tiên không phải “dùng Redis hay local cache?” mà là “staleness nào business chấp nhận và source of truth nằm ở đâu?”