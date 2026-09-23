# 04. Caching và invalidation

Cache là một bản sao có thời hạn, không phải source of truth. Thiết kế cache bắt
đầu bằng câu hỏi: dữ liệu nào được phép stale, trong bao lâu, ai sở hữu key, và
failure khi cache mất là gì.

## Pattern

- **Cache-aside**: đọc cache, miss thì đọc source rồi populate; dễ áp dụng nhưng
  có stampede và cửa sổ stale.
- **Write-through**: ghi qua cache và source theo một flow; đơn giản cho reader
  nhưng cần xử lý partial failure.
- **Write-behind**: cache nhận ghi trước; chỉ dùng khi chấp nhận durability
  bất đồng bộ và có queue/recovery rõ ràng.
- **Refresh-ahead**: làm mới trước expiry cho hot key; cần giới hạn chi phí.

TTL là safety net, không phải invalidation strategy. Khi mutation thành công,
invalidate các key liên quan hoặc dùng versioned key. Invalidation phải bao phủ
mọi representation: detail, list, aggregate và permission-sensitive view.

## Stampede và consistency

Dùng single-flight/lease, jitter TTL, stale-while-revalidate hoặc giới hạn
concurrency để tránh hàng nghìn request cùng rebuild một key. Không cache dữ liệu
phụ thuộc identity bằng key thiếu tenant/user. Nếu consistency quan trọng hơn
latency, đọc source sau write hoặc đính kèm version để client phát hiện stale.

## Chỉ số cần theo dõi

Hit ratio một mình không đủ: theo dõi stale-read rate, eviction, size, latency,
origin load, error/fallback và hot-key skew. Cache outage phải degrade có chủ ý
(slower origin, partial response hoặc fail fast), không tạo retry storm.

## Đào sâu: consistency budget

Đặt một `staleness budget` cho từng loại dữ liệu thay vì nói cache “nhanh hơn”.
Profile công khai có thể chấp nhận stale 60 giây; quyền truy cập không được đọc
cache quá cũ sau revoke. Budget quyết định TTL, invalidation, read-after-write
path và alert threshold.

Key design là một phần của schema. Key phải chứa mọi dimension làm thay đổi
representation (tenant, locale, permission scope, version). Namespace và version
giúp đổi serialization mà không phải scan/xóa toàn bộ cache. Khi invalidation
không chắc chắn, versioned key + TTL ngắn an toàn hơn một lệnh delete tưởng đã
bao phủ tất cả variant.

Ba failure pattern cần tách: **stampede** (rebuild đồng thời, dùng lease),
**avalanche** (nhiều key hết hạn cùng lúc, dùng jitter), và **penetration** (key
không tồn tại bị hỏi liên tục, dùng negative cache TTL ngắn). Test cả cache
outage và origin error trong lúc refresh để không ghi đè giá trị tốt bằng error.
