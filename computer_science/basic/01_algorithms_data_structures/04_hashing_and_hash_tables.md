# Hashing và hash table

Ta muốn map key như `userId` sang value mà không scan toàn bộ collection. Nếu key nằm trong universe lớn, direct-address table quá tốn memory. Hashing giải quyết bằng cách dùng một function nén key thành một integer/bucket index nhỏ hơn.

## Hash function đang làm gì?

Hash function (해시 함수) ánh xạ input có kích thước tùy ý vào fixed-size value. Với hash table, ta thường lấy hash code rồi map vào bucket range.

Vì number of possible keys lớn hơn buckets, collision (충돌) là tất yếu theo pigeonhole principle. Mục tiêu không phải tránh collision hoàn toàn mà phân bố keys đủ đều và xử lý collision đúng.

Một hash table đúng cần equality contract phù hợp: nếu `a == b` thì hashes phải tương thích để lookup tìm cùng location. Trong Java, đây là lý do `equals()` và `hashCode()` phải nhất quán.

## Separate chaining và open addressing

Separate chaining mỗi bucket chứa collection entries, như linked list hoặc tree. Lookup hash tới bucket rồi search trong bucket.

Open addressing giữ entries ngay trong table; collision trigger probing như linear/quadratic probing hoặc double hashing. Empty/deleted markers trở thành phần quan trọng của invariant.

Open addressing thường có locality tốt nhưng performance suy giảm nhanh khi table quá đầy. Chaining linh hoạt load hơn nhưng thêm pointer/object overhead.

## Load factor

Load factor `α = n/m`, với n entries và m buckets/slots. Khi α tăng, collision/probe length tăng. Dynamic hash table resize khi vượt threshold, rehash entries vào table lớn hơn.

Resize là operation O(n), nhưng nếu growth geometric, insert có thể amortized O(1), tương tự dynamic array.

## Expected O(1) dựa trên assumptions

Hash table thường được mô tả lookup expected O(1), nhưng guarantee này phụ thuộc hash distribution và load factor. Nếu mọi keys collide, lookup có thể O(n). Một attacker có thể cố tạo collision patterns nếu hash function predictable, tạo hash-flooding DoS; runtime/framework có thể randomize seed hoặc treeify buckets để giảm risk.

## Hash table khác cryptographic hash

Data-structure hash ưu tiên speed và distribution. Cryptographic hash cần thêm properties như preimage resistance, second-preimage resistance và collision resistance. Dùng `hashCode()` để lưu password là sai category.

Xem [Cryptography foundations](../07_security_reliability/01_cryptography_foundations.md).

## Mutable key hazard

Nếu key được insert rồi fields tham gia hash/equality bị mutate, hash có thể đổi. Entry vẫn nằm bucket cũ nhưng lookup tính bucket mới, khiến “key tồn tại mà tìm không thấy”. Vì vậy keys nên immutable theo equality/hash identity trong thời gian nằm trong map/set.

## Hash set như map đặc biệt

Set membership có thể implement bằng hash table chỉ lưu keys hoặc map keys tới dummy value. Từ abstraction perspective, HashSet và HashMap chia sẻ cơ chế distribution/collision nhưng expose contract khác.

## Consistent hashing

Trong distributed systems, simple `hash(key) mod N` remap rất nhiều keys khi N thay đổi. Consistent hashing đặt nodes và keys trên hash ring để thêm/bớt node chỉ di chuyển một phần keyspace. Đây là ví dụ cùng mental model hashing được nâng từ in-memory structure lên partition placement.

## Bloom filter: probabilistic membership

Bloom filter dùng nhiều hash functions và bit array. Nó có thể nói “definitely not present” hoặc “possibly present”, chấp nhận false positives nhưng không false negatives nếu không có deletion biến thể. Database/storage system dùng Bloom filter để tránh expensive I/O cho keys chắc chắn không tồn tại.

Đây là time-space-accuracy trade-off: một ít memory giảm nhiều lookups nhưng không lưu actual values.

## Mental Model

> Hash table đổi **ordered structure** lấy **direct probabilistic placement**. Nhanh vì hash đưa ta gần vị trí cần tìm; collision policy và load factor quyết định phần việc còn lại.

## Common Misconceptions

**“Hash không collision nếu function tốt.”** Collision là toán học tất yếu khi domain lớn hơn output space.

**“O(1) nghĩa guaranteed.”** Thường là expected/amortized dưới assumptions; worst-case có thể khác.

**“Hashing và encryption giống nhau vì đều biến dữ liệu.”** Hash là one-way digest; encryption thiết kế reversible với key. Data-structure hash còn có mục tiêu khác cryptographic hash.

## Kết nối

Hashing liên quan [database hash indexes](../05_data_databases/03_indexes_and_query_execution.md), [password/MAC hashing](../07_security_reliability/01_cryptography_foundations.md), [distributed partitioning](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) và [cache key design](../08_software_systems/02_performance_capacity_and_scalability.md).
