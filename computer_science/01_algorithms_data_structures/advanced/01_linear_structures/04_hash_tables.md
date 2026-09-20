# Bảng băm
**Hash Table / 해시 테이블**

Hash table giải bài toán: từ một key, làm sao đi gần trực tiếp tới vùng lưu trữ của key thay vì quét toàn bộ collection? Nó là một trong những structures được dùng nhiều nhất trong software vì equality lookup, membership và grouping xuất hiện khắp nơi: cache, symbol table, deduplication, join, routing metadata, compiler tables, counting và graph state tracking.

Mental model cơ bản là:

> Hash table dùng một hàm băm để nén key space rất lớn thành một table nhỏ hơn, chấp nhận collision là tất yếu và dùng collision policy để giữ correctness.

## Hash function và bucket mapping

**Hash function / 해시 함수** ánh xạ key sang integer-like hash value. Bucket index sau đó được suy ra từ hash và capacity.

Một mô hình đơn giản:

\[
index = h(key) \bmod m
\]

Trong implementation thực tế, capacity có thể là power of two và index dùng mask thay vì modulo. Khi đó hash mixing phải đảm bảo low bits đủ tốt, nếu không distribution sẽ tệ.

Hash function cho in-memory table cần nhanh, deterministic trong lifetime cần thiết và phân phối keys đủ đều dưới workload dự kiến. “Hash tốt” không chỉ là không collision — điều đó bất khả thi khi key space lớn hơn table — mà là collision distribution không tạo clusters xấu quá thường xuyên.

## Collision là toán học, không phải bug

Theo pigeonhole principle, nếu số possible keys lớn hơn số buckets, collision chắc chắn có thể xảy ra. Vì thế correctness không được dựa trên assumption “hash khác nhau cho mọi key”.

Hai chiến lược lớn:

```text
separate chaining
open addressing
```

Chaining cho mỗi bucket chứa một collection entries. Open addressing giữ entries trực tiếp trong table và probe vị trí khác khi home slot occupied.

## Equality và hash là hai tầng khác nhau

Hash giúp tìm candidate region; equality quyết định key có thật sự bằng nhau không.

Trong Java contract:

```text
a.equals(b) == true  =>  a.hashCode() == b.hashCode()
```

Chiều ngược lại không cần đúng vì collision hợp lệ.

Một implementation chỉ so hash mà không compare key có thể trả false equality khi collision. Đây là lỗi correctness nghiêm trọng.

## Hash code stability và mutable keys

Nếu key được insert rồi field dùng trong hash/equality bị thay đổi, entry vẫn nằm ở bucket/probe path cũ nhưng future lookup tính hash mới.

Ví dụ Java object mutable làm `HashMap` key có thể trở thành “mất tích” logic dù entry vẫn chiếm memory.

Vì vậy keys nên immutable theo identity fields, hoặc ít nhất không mutate các fields tham gia `equals/hashCode` trong khi key đang nằm trong table.

Java `record` thường thuận tiện cho compound immutable keys.

## Separate chaining

Chaining có thể hình dung:

```text
bucket[0] -> entry -> entry
bucket[1] -> null
bucket[2] -> entry
...
```

Expected chain length liên quan load factor nếu hashing đều. Chaining xử lý deletion đơn giản: remove entry khỏi chain.

Nhược điểm lớn của classic pointer-linked chaining là memory locality kém và allocation overhead. Modern implementations có thể dùng compact arrays, small vectors hoặc treeification cho buckets lớn tùy runtime/library.

## Load factor

Load factor:

\[
\alpha = \frac{n}{m}
\]

trong đó `n` entries và `m` buckets/slots.

Với chaining, `α` có thể > 1 nhưng chains dài hơn. Với open addressing, table phải có empty slots; `α` tiến gần 1 làm probe length tăng mạnh.

Load factor threshold là trade-off giữa memory overhead và lookup/insert cost.

## Resize và rehash

Khi capacity thay đổi, mapping bucket thường thay đổi:

\[
h(key)\bmod m_{old} \neq h(key)\bmod m_{new}
\]

vì vậy không thể chỉ `memcpy` table sang vùng lớn hơn và giữ nguyên slot semantics. Entries phải được redistribute theo capacity mới, dù một số implementation power-of-two có thể optimize transfer dựa trên một hash bit mới.

Resize thường `O(n)` nhưng xảy ra thưa, cho insert amortized expected `O(1)` dưới assumptions phù hợp.

## Incremental rehashing

Rehash toàn table một lần có thể tạo latency spike lớn. Systems latency-sensitive đôi khi dùng **incremental rehashing**: giữ old + new table tạm thời và migrate một số buckets mỗi operation.

Lookup trong transition có thể phải check cả hai tables. Implementation phức tạp hơn nhưng tail latency tốt hơn.

Đây là ví dụ khác của trade-off throughput vs latency smoothness.

## Open addressing

Open addressing giữ entries trong array chính. Khi home slot occupied, algorithm probe vị trí tiếp theo theo một sequence.

Linear probing:

\[
index_i=(h(key)+i)\bmod m
\]

Quadratic probing thay step tuyến tính bằng quadratic expression. Double hashing dùng second hash để sinh stride.

Correctness cần đảm bảo probe sequence có thể tìm được entry nếu nó tồn tại và insert có thể tìm empty slot khi table chưa quá đầy theo design.

## Why locality makes open addressing attractive

Entries contiguous hơn chaining, giảm pointer chasing và tận dụng cache tốt. Với workloads memory-bound, open addressing có thể rất mạnh dù theoretical expected complexity cùng `O(1)`.

Nhưng deletion, high load factor và clustering khó hơn.

## Primary clustering trong linear probing

Linear probing có thể tạo contiguous occupied runs. Khi collision rơi vào run, entry mới nối dài run; run dài lại thu hút thêm collisions.

Đây gọi là **primary clustering**.

Hash distribution tốt không loại hoàn toàn phenomenon vì probing policy tự tạo dependency giữa positions.

## Tombstone và deletion

Nếu search qua occupied slots và dừng tại first truly empty slot, deletion không được biến một middle slot thành EMPTY ngay.

Ví dụ:

```text
home(A)=3
A ở slot 3
B collision -> slot 4
xóa A
```

Nếu slot 3 trở thành EMPTY, lookup B từ home 3 sẽ dừng quá sớm.

Vì vậy open addressing thường có states:

```text
EMPTY
OCCUPIED
DELETED / TOMBSTONE
```

Search đi qua tombstone; insert có thể reuse tombstone. Quá nhiều tombstones làm probe dài nên table có thể cần rebuild.

## Backward-shift deletion

Một số probing schemes có thể tránh permanent tombstones bằng cách shift subsequent entries backward sau deletion trong những điều kiện nhất định. Điều này giữ probe invariants nhưng implementation tinh tế hơn.

Không có một deletion strategy tốt cho mọi probing scheme; phải xuất phát từ probe invariant.

## Robin Hood hashing

Robin Hood hashing theo dõi khoảng cách mỗi entry đã đi từ home slot. Khi new entry đã “đi xa” hơn resident entry, chúng có thể swap để giảm variance probe distances.

Idea là phân phối bất công ít hơn: entry rất unlucky được ưu tiên hơn entry còn gần home.

Kết quả thường cải thiện predictability của lookup probe length, dù implementation deletion/metadata phức tạp hơn.

## Swiss-table style intuition

Modern high-performance hash tables thường dùng groups control bytes/fingerprints để scan nhiều candidate slots cùng lúc với SIMD-friendly operations, thay vì textbook “một slot một lần”.

Điều đáng học không phải một specific implementation version, mà là principle:

> Same ADT và same expected Big-O có thể khác nhau rất lớn vì metadata layout, branch behavior và vectorized candidate filtering.

## Hash mixing và poor input patterns

Nếu capacity power-of-two và keys có low bits correlated, direct masking có thể cluster badly. Hash function/mixing cần spread entropy sang bits dùng cho index.

Ví dụ integer ids multiples of 1024 đi vào table size power-of-two có thể có low bits giống nhau nếu không mix.

Một quality hash table implementation không giả định key raw bits đã uniform.

## Universal hashing intuition

Universal hashing chọn hash function ngẫu nhiên từ một family sao cho xác suất collision của hai distinct keys được bounded.

Mục tiêu lý thuyết là giảm khả năng một fixed adversarial key set ép collisions xấu khi hash choice random/hidden.

Không cần implement universal hashing thường xuyên, nhưng nó giải thích mối liên hệ giữa randomization và expected dictionary performance.

## Hash flooding và security

Nếu attacker kiểm soát input keys và có thể tạo nhiều collisions, expected `O(1)` lookup có thể suy thoái mạnh và trở thành denial-of-service vector.

Runtime/framework có thể dùng randomized seeds, better hashing, bucket treeification hoặc other defenses. Security-sensitive system cần phân biệt “random-looking normal workload” và **adversarial workload**.

Expected complexity luôn gắn với assumptions.

## Cryptographic hash không mặc định là hash-table hash

SHA-family hashes có security properties mạnh nhưng thường đắt hơn nhu cầu in-memory map. Hash table thường cần fast non-cryptographic distribution, trừ khi threat model yêu cầu chống crafted collisions theo cách cụ thể.

“Hash” là family concept; cryptographic hash và table hash có goals khác nhau.

## Compound keys

Key `(userId, productId)` cần equality/hash theo tuple semantics.

Không nên canonicalize bằng concatenation mơ hồ:

```text
"12" + "34" -> "1234"
"1" + "234" -> "1234"
```

Có thể dùng tuple/record, length-delimited encoding, nested map hoặc a proper combine function.

Java:

```java
record Key(long userId, long productId) {}
```

JavaScript object keys trong `Map` dùng identity, nên hai object literals fields giống nhau vẫn khác keys. Có thể dùng canonical string, nested `Map`, integer packing nếu range cho phép hoặc explicit interning.

C cần define hash/equality cùng field semantics và ownership rõ ràng.

## Integer key packing

Nếu two fields có bounded bit-width, có thể pack vào một integer:

```text
key = (x << bitsY) | y
```

nhưng phải chứng minh ranges không overlap/overflow. Java signed shifting, C integer promotions và JavaScript 32-bit bitwise semantics có thể làm implementation khác mathematical intent.

Representation trick chỉ đúng khi numeric model được kiểm soát.

## Hash set và membership

HashSet thường là hash map chỉ cần keys hoặc map key tới dummy marker.

Deduplication:

```java
Set<String> seen = new HashSet<>();
for (String x : values) {
    if (!seen.add(x)) {
        // duplicate
    }
}
```

Expected total `O(n)` thay vì nested scan `O(n^2)` dưới normal hashing assumptions.

## Frequency map

Counting là pattern rất phổ biến:

```java
Map<String, Integer> freq = new HashMap<>();
for (String x : values) {
    freq.merge(x, 1, Integer::sum);
}
```

Nhưng nếu key cardinality rất lớn, memory của exact map có thể dominate. Khi only approximate frequencies cần thiết, Count-Min Sketch là alternative specialized structure.

## Hash table vs balanced tree

Hash table mạnh ở exact equality lookup expected `O(1)`.

Balanced tree mạnh ở ordered operations:

```text
min/max
predecessor/successor
floor/ceiling
range scan
ordered iteration
```

Tree update thường deterministic `O(log n)`. Hash table không giữ global order tự nhiên.

Nếu workload cần cả exact lookup và order, có thể maintain two structures hoặc dùng one ordered structure tùy trade-off.

## Hash table vs direct addressing

Nếu key domain nhỏ, dense và bounded, direct array indexing có thể tốt hơn hashing.

Ví dụ keys integers `[0, 9999]`:

```text
value[key]
```

không collision, no hash computation, predictable locality. Cost là memory proportional to universe size `U` thay vì number of actual entries `n`.

Hash table hữu ích khi universe lớn/sparse.

## Perfect hashing

Nếu key set static và known trước, perfect hashing có thể xây collision-free mapping cho exactly set đó. Minimal perfect hash còn cố dùng near-minimal slot count.

Build phức tạp hơn nhưng lookup rất compact/fast cho static dictionaries, compiler keyword tables, asset indexes hoặc large read-only datasets.

Đây là example rằng “static vs dynamic” thay đổi structure possibilities.

## Caching và memoization

Memoization table map state -> computed result. Correctness phụ thuộc key state chứa **đủ future-relevant information**.

Nếu key thiếu một variable ảnh hưởng result, cache collision về semantics xảy ra ngay cả khi hash implementation hoàn hảo: two distinct logical states bị coi là same key.

Đây là modeling bug, không phải hash collision.

## Graph visited state

BFS/DFS thường dùng hash set khi state space sparse/implicit. Nếu node ids dense `[0,n)`, boolean array/bitset thường nhanh và compact hơn.

Chọn HashSet chỉ vì “visited thường dùng set” có thể bỏ lỡ better representation.

## Database hash join

Hash join xây hash table từ relation nhỏ theo join key, sau đó scan relation lớn và probe matching entries.

Nếu build side không fit memory, engine có thể partition data theo hash và process partitions, chuyển problem thành external-memory hash join.

Mental model giống in-memory table nhưng cost model thêm I/O, memory budget và skew.

## Hash aggregation

SQL:

```sql
SELECT department_id, COUNT(*)
FROM employee
GROUP BY department_id;
```

có thể dùng hash aggregation: key là group value, entry giữ aggregate state. Nếu groups quá nhiều cho memory, engine phải spill/partition hoặc dùng sort-based aggregation.

Data structure choice xuất hiện trực tiếp trong query plan.

## Consistent hashing trong distributed systems

Consistent hashing không phải internal hash-table collision scheme. Nó map keys/nodes vào a ring-like hash space để khi cluster membership thay đổi, chỉ subset keys cần remap.

Use case là partitioning/sharding/cache distribution, không phải dictionary lookup inside one process.

Cùng chữ “hash” nhưng abstraction khác.

## Rendezvous hashing

Highest Random Weight / rendezvous hashing assign key tới node có score hash cao nhất. Nó cũng giảm remapping khi nodes thay đổi và đôi khi simpler than ring management.

Điểm học được là hashing có thể dùng để **partition responsibility**, không chỉ chọn array bucket.

## Bloom Filter connection

Hash table lưu exact keys; Bloom Filter chỉ lưu bit evidence từ multiple hashes và cho approximate membership với false positives.

Một storage engine có thể đặt Bloom Filter trước expensive SSTable/disk lookup: nếu filter chắc chắn “không”, bỏ I/O; nếu “có thể”, mới check exact structure.

Đây là composition exact + probabilistic structures.

## Resizing policy và latency

Doubling capacity giảm số lần resize nhưng tạo big copy/rehash events. Smaller growth factor dùng memory sát hơn nhưng resize thường xuyên.

Real system có thể pre-size map nếu biết approximate cardinality để tránh repeated resizing.

Java `HashMap` constructor capacity/loading semantics cần hiểu nếu tuning; JavaScript `Map` thường không expose capacity directly.

## Iteration order

Không nên giả định hash map iteration sorted. Một số languages/runtimes define insertion order for specific map types; điều đó là API contract riêng, không phải property chung của hash table theory.

Nếu correctness phụ thuộc iteration order, hãy chọn abstraction có contract rõ ràng thay vì dựa vào implementation accident.

## Concurrency

Concurrent hash table cần synchronization finer-grained hơn global lock nếu throughput cao. Techniques có thể gồm striped locks, lock-free reads, CAS, bucket-level coordination và resizing protocols.

Correctness phải giữ mapping semantics trong khi table shape thay đổi. Concurrent resize là một trong những phần khó hơn textbook map rất nhiều.

Trong Java, `ConcurrentHashMap` cung cấp concurrent semantics khác `HashMap`; không được coi chỉ là drop-in “faster thread-safe map”. Compound operations vẫn cần dùng atomic APIs phù hợp như `compute` thay vì external check-then-act nếu cần atomicity.

## Memory model

Một hash entry object-heavy có overhead lớn: object header, key/value references, bucket nodes, allocator metadata. Open-addressing primitive table có thể compact hơn nhiều.

Big-O đều `O(n)` nhưng actual bytes/key khác lớn. Với millions entries, representation memory có thể quyết định architecture.

## Cache behavior

Chaining pointer chase làm cache misses; open addressing scans nearby slots, có thể tận dụng cache lines/prefetch. Nhưng high load factor tăng probes.

Hash table performance thường memory-bound hơn arithmetic-bound, nên locality và table size quan trọng.

## Common failure modes

- key equality/hash không consistent;
- mutable key sau insert;
- delete open-addressing slot thành EMPTY sai invariant;
- resize raw-copy buckets mà không rehash;
- load factor quá cao;
- poor hash mixing với patterned keys;
- assume iteration order không được contract;
- adversarial collision/hash flooding;
- use object identity trong JavaScript khi cần value equality;
- dùng hash table cho range/order query vốn không phù hợp.

## Testing strategy

Hash table nên được differential-test với reference map/set từ standard library hoặc simple sorted structure trên random operation sequences.

Các cases cần test mạnh:

```text
many collisions cố ý
resize nhiều lần
insert-delete-reinsert
tombstone reuse
duplicate key update
empty table
capacity boundaries
keys có same hash nhưng not equal
```

Validator có thể kiểm tra `size` khớp occupied entries, every occupied key searchable theo probe invariant và no duplicate logical keys.

Với custom hash function, statistical distribution tests có thể phát hiện obvious clustering, nhưng không thay formal/security evaluation.

## Mental Model

> Hash table đổi global order lấy khả năng dùng hash để nhảy tới một vùng nhỏ nơi key có thể nằm. Performance tốt đến từ ba lớp cùng lúc: hash phân phối đủ tốt, collision policy giữ probe/chain ngắn, và representation tận dụng memory/cache tốt. Correctness vẫn phải dựa trên equality thật, không bao giờ chỉ dựa vào hash.

Khi chọn hash table, hãy hỏi: **query có thật sự là equality lookup không, key semantics có ổn định không, workload có adversarial không, cardinality/memory bao nhiêu, có cần order/range không, và expected guarantee có đủ cho latency requirement không?**

Xem tiếp: [Arrays](./00_arrays_and_dynamic_arrays.md), [Balanced Search Trees](../02_trees/02_balanced_search_trees.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md) và [DSA in Databases & Systems](../90_connections/01_dsa_in_databases_networks_and_systems.md).
