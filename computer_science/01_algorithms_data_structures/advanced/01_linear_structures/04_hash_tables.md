# Bảng băm
**Hash Table / 해시 테이블**

Bảng băm giải một câu hỏi rất phổ biến: **từ một khóa, làm sao đi gần trực tiếp tới vùng lưu trữ liên quan thay vì quét toàn bộ tập dữ liệu?** Đây là một trong những cấu trúc được dùng rộng nhất trong phần mềm: cache, symbol table, deduplication, grouping, database hash join, memoization, routing metadata, frequency counting và theo dõi trạng thái đã thăm.

Ý tưởng cốt lõi là:

> Hash Table dùng hàm băm để biến không gian khóa rất lớn thành một không gian vị trí nhỏ hơn, chấp nhận collision là tất yếu và dùng một chính sách xử lý collision để bảo toàn tính đúng đắn.

Điểm cần hiểu sâu là `O(1)` của Hash Table không phải phép thuật. Nó dựa trên nhiều lớp giả định: chất lượng hash, hệ số tải, chính sách collision, phân bố input, cách quản lý deletion, bộ nhớ và đôi khi cả threat model.

## Hàm băm và ánh xạ vào bảng

Một mô hình đơn giản:

\[
index=h(key)\bmod m
\]

trong đó `m` là số bucket hoặc slot.

Nếu `m` là lũy thừa của hai, implementation có thể dùng bitmask:

```text
index = hash & (m - 1)
```

Cách này nhanh nhưng làm chất lượng các bit thấp của hash trở nên đặc biệt quan trọng. Nếu khóa có pattern mạnh ở các bit thấp mà không được trộn tốt, nhiều khóa có thể dồn vào cùng vùng.

Một hash function phù hợp cho bảng băm thường cần:

```text
xác định trong phạm vi sử dụng cần thiết
nhanh
phân tán khóa đủ đều với workload thực tế
khó bị input pattern phá nếu môi trường có input đối kháng
```

Mục tiêu không phải “không collision”; điều đó bất khả thi khi miền khóa lớn hơn bảng.

## Collision là điều chắc chắn có thể xảy ra

Theo pigeonhole principle, nếu số khóa khả dĩ lớn hơn số bucket, hai khóa khác nhau có thể cùng ánh xạ tới một vị trí.

Do đó Hash Table đúng phải có hai tầng:

```text
hash -> tìm vùng ứng viên
key equality -> xác nhận đúng khóa
```

Không bao giờ được dùng “hash bằng nhau” như bằng chứng hai khóa bằng nhau.

Trong Java:

```text
a.equals(b) == true  =>  a.hashCode() == b.hashCode()
```

Chiều ngược lại không bắt buộc.

## Khóa có thể thay đổi là một lỗi thiết kế nguy hiểm

Nếu một object được dùng làm khóa rồi các trường tham gia `equals/hashCode` bị sửa, entry vẫn nằm ở vị trí được chọn theo hash cũ nhưng lookup sau đó tính hash mới.

Kết quả là khóa có thể trở thành “mất tích” về logic dù entry vẫn chiếm bộ nhớ.

Trong Java, compound key bất biến như record thường an toàn hơn:

```java
record UserProductKey(long userId, long productId) {}
```

Trong C hoặc JavaScript, cũng phải tự định nghĩa rõ canonical representation của khóa.

## Hai họ xử lý collision chính

Hai chiến lược lớn là:

```text
separate chaining
open addressing
```

Chúng cùng cung cấp dictionary semantics nhưng có mô hình bộ nhớ rất khác.

## Separate chaining

Mỗi bucket trỏ tới một collection các entry có cùng bucket index.

```text
bucket[0] -> entry -> entry
bucket[1] -> null
bucket[2] -> entry
```

Lookup:

```text
1. tính hash
2. chọn bucket
3. duyệt các entry trong bucket
4. so key equality
```

Deletion khá đơn giản vì chỉ cần gỡ entry khỏi bucket chain.

Ưu điểm:

```text
load factor có thể vượt 1
xóa đơn giản
resize policy linh hoạt
```

Nhược điểm của chaining kiểu linked nodes:

```text
nhiều cấp phát nhỏ
pointer chasing
locality kém
object/header overhead
```

Một implementation hiện đại có thể dùng bucket nhỏ dạng mảng hoặc layout gọn thay vì linked list cổ điển.

## Hệ số tải

Định nghĩa:

\[
\alpha=\frac nm
\]

với `n` là số entry và `m` là số bucket/slot.

Load factor càng cao thì bộ nhớ càng tiết kiệm nhưng collision/probing thường càng đắt.

Với chaining, `α` có thể lớn hơn 1. Với open addressing, bảng cần slot trống để probing kết thúc hiệu quả nên `α` tiến gần 1 thường làm hiệu năng giảm mạnh.

Do đó capacity planning là sự đánh đổi giữa memory và probe cost.

## Resize và rehash

Khi capacity đổi, bucket index thường đổi theo:

\[
h(key)\bmod m_{old}\neq h(key)\bmod m_{new}
\]

Vì vậy resize thường cần **rehash/reinsert** các entry vào bảng mới.

Resize có thể tốn `O(n)`, nhưng nếu capacity tăng theo cấp số nhân thì tổng chi phí trên chuỗi nhiều insert thường được phân tích khấu hao thành expected `O(1)` mỗi insert dưới giả định hash phù hợp.

### Vì sao tăng từng 1 là tệ?

Nếu bảng gần đầy và mỗi lần chỉ tăng capacity rất ít, ta có thể rehash gần toàn bộ bảng quá thường xuyên. Tăng theo tỷ lệ giúp số lần resize chỉ logarithmic theo số entry.

## Incremental rehashing

Rehash toàn bộ bảng trong một operation có thể tạo latency spike.

Một số hệ thống chọn **incremental rehashing**:

```text
giữ old table + new table
di chuyển một lượng nhỏ bucket/entry ở mỗi operation
lookup tạm thời có thể phải kiểm tra cả hai bảng
khi migrate xong thì bỏ bảng cũ
```

Tổng công việc không nhất thiết giảm, nhưng chi phí được dàn ra để cải thiện tail latency.

Đây là ví dụ rõ ràng của trade-off throughput–latency.

## Open addressing

Open addressing giữ entry trực tiếp trong array table. Khi home slot đã occupied, thuật toán thử các slot khác theo **probe sequence**.

### Linear probing

\[
index_i=(h(key)+i)\bmod m
\]

Rất đơn giản và có locality tốt vì các slot gần nhau trong bộ nhớ.

### Quadratic probing

Probe offset tăng theo hàm bậc hai nhằm giảm một số dạng clustering.

### Double hashing

Dùng hash thứ hai để tạo stride:

\[
index_i=(h_1(key)+i\cdot h_2(key))\bmod m
\]

Thiết kế phải bảo đảm stride cho phép đi qua đủ không gian slot theo capacity đã chọn.

## Vì sao open addressing có thể rất nhanh trên máy thật?

Entry nằm gần nhau trong một mảng, nên CPU có thể tận dụng cache line và prefetch tốt hơn chaining bằng pointer.

Do đó hai cấu trúc cùng expected `O(1)` có thể khác đáng kể về tốc độ thực tế vì **data movement** chứ không phải Big-O.

Đây là một bài học tổng quát: độ phức tạp tiệm cận không thay thế phân tích layout bộ nhớ.

## Primary clustering

Linear probing có thể tạo các cụm slot occupied liên tiếp.

Khi một key hash vào giữa cụm, nó phải đi qua cụm và thường được đặt ở cuối. Cụm dài hơn lại thu hút nhiều collision hơn.

Đây là **primary clustering**.

Ngay cả hash function khá tốt vẫn không loại hoàn toàn hiện tượng này vì probing rule tự tạo phụ thuộc giữa các vị trí.

## Deletion và tombstone

Open addressing không thể luôn biến slot vừa xóa thành `EMPTY`.

Ví dụ:

```text
A home = 3, nằm slot 3
B home = 3, collision nên nằm slot 4
xóa A
```

Nếu slot 3 trở thành `EMPTY`, lookup B bắt đầu từ 3 có thể dừng quá sớm và kết luận sai rằng B không tồn tại.

Vì vậy thường cần:

```text
EMPTY
OCCUPIED
DELETED / TOMBSTONE
```

Lookup đi qua tombstone. Insert có thể tái sử dụng tombstone.

Nhưng quá nhiều tombstone làm probe dài lên, vì vậy bảng có thể cần rebuild ngay cả khi số phần tử sống không lớn.

## Backward-shift deletion

Một số scheme, đặc biệt các biến thể linear probing, có thể dịch một số entry sau điểm xóa về phía trước để bảo toàn reachability của probe sequence mà không giữ tombstone lâu dài.

Điểm quan trọng không phải nhớ thuật toán xóa cụ thể, mà là:

> deletion phải được chứng minh dựa trên invariant của probe sequence.

Không thể tự ý “dọn slot cho đẹp” nếu việc đó làm lookup mất đường tới key khác.

## Khoảng cách probe như một đại lượng trạng thái

Với open addressing, ngoài hash và key còn có một đại lượng quan trọng: entry đã đi xa bao nhiêu slot từ home position.

Probe distance ảnh hưởng:

```text
latency lookup
variance giữa các key
quyết định swap trong Robin Hood hashing
quy tắc dừng lookup ở một số scheme
```

Nhìn probe distance như metadata giúp hiểu các thiết kế hiện đại hơn.

## Robin Hood hashing

Ý tưởng Robin Hood là “lấy của người may mắn gần nhà để giúp người xui phải đi xa”.

Khi entry mới có probe distance lớn hơn entry đang chiếm slot, hai entry có thể đổi chỗ. Mục tiêu là giảm variance của probe length và tránh một số key có đường dò quá dài.

Trade-off:

```text
lookup thường ổn định hơn
insert phức tạp hơn
metadata/deletion cần cẩn thận hơn
```

Đây là ví dụ một cấu trúc tối ưu không chỉ mean cost mà còn phân phối cost.

## Cuckoo hashing

Cuckoo hashing cho mỗi key một số vị trí khả dĩ, ví dụ hai hash function:

```text
slot1 = h1(key)
slot2 = h2(key)
```

Nếu cả hai bị chiếm, insert có thể “đá” một entry hiện tại sang vị trí thay thế của nó và tiếp tục chuỗi di chuyển.

Lookup rất hấp dẫn vì chỉ phải kiểm tra một số vị trí cố định nhỏ.

Nhưng insertion có thể tạo cycle; khi đó cần rehash hoặc resize.

Cuckoo hashing cho thấy một trade-off khác: lookup đơn giản hơn đổi lại insertion khó dự đoán hơn.

## SwissTable-style design: bài học về metadata và vectorization

Các hash table hiệu năng cao hiện đại thường tách metadata nhỏ của slot khỏi payload và quét một nhóm metadata cùng lúc để lọc nhanh candidate.

Một control byte có thể mã hóa trạng thái slot và một fingerprint ngắn của hash. CPU có thể so sánh nhiều control byte song song trước khi chạm vào key thật.

Điều đáng học không phải một implementation cụ thể, mà là nguyên lý:

> Cùng ADT và cùng expected Big-O vẫn có thể khác nhau rất lớn nhờ layout metadata, cache locality, branch behavior và SIMD.

## Hash mixing

Nếu capacity là lũy thừa của hai, chỉ một số bit của hash quyết định bucket. Nếu key pattern làm các bit đó kém phân tán, collision tăng mạnh.

Ví dụ ID luôn là bội số của `1024` có nhiều bit thấp bằng 0. Một mapping dùng trực tiếp bit thấp mà không mix có thể tạo distribution xấu.

Do đó implementation thường có bước trộn để khuếch tán thông tin từ toàn bộ key/hash vào các bit dùng cho index.

## Universal hashing: trực giác lý thuyết

Universal hashing chọn ngẫu nhiên một hash function từ một family được thiết kế sao cho với hai key khác nhau, xác suất collision bị chặn.

Ý tưởng quan trọng là: nếu attacker hoặc input không biết chính xác hash function được chọn, một fixed set key khó ép toàn bộ collision theo cùng cách.

Universal hashing giúp nối randomization với expected dictionary performance.

## Hash flooding và input đối kháng

Nếu người dùng kiểm soát key và biết cách tạo nhiều collision, Hash Table có thể suy thoái nghiêm trọng và trở thành vector denial-of-service.

Các biện pháp có thể gồm:

```text
hash seed ngẫu nhiên
hash tốt hơn
bucket treeification
thay đổi implementation khi collision quá lớn
rate limiting ở tầng hệ thống
```

Khi phân tích security-sensitive code, phải tách:

```text
normal workload
random workload
adversarial workload
```

Expected `O(1)` luôn đi kèm assumption.

## Hash table hash và cryptographic hash không cùng mục tiêu

SHA-256 được thiết kế cho các thuộc tính mật mã mạnh. Hash function cho in-memory table thường ưu tiên tốc độ, phân phối và khả năng chống pattern đủ cho threat model cụ thể.

Dùng cryptographic hash cho mọi map có thể quá đắt. Ngược lại, dùng một hash cực nhanh nhưng dễ bị crafted collision có thể không phù hợp với public-facing server.

“Hash” là một họ ý tưởng, không phải một loại hàm duy nhất.

## Compound key

Khóa `(userId, productId)` phải có equality/hash theo cặp.

Không nên ghép chuỗi mơ hồ:

```text
"12" + "34" = "1234"
"1"  + "234" = "1234"
```

Có thể dùng tuple/record, encoding có delimiter/length rõ hoặc nested map.

Java:

```java
record Key(long userId, long productId) {}
```

JavaScript có một khác biệt quan trọng: object dùng làm key trong `Map` được so theo identity. Hai object literal có cùng field không tự động là cùng key:

```js
const a = {x: 1};
const b = {x: 1};
console.log(a === b); // false
```

Nếu cần value semantics, phải canonicalize hoặc encode key.

## Hash Table và memoization

Memoization thường dùng map:

```text
state -> computed answer
```

Điều này chỉ đúng nếu key chứa đầy đủ state ảnh hưởng tới kết quả.

Nếu memo key bỏ một dimension quan trọng, cache có thể trả lời của state khác. Đây là lỗi mô hình hóa, không phải lỗi Hash Table.

Nếu key chứa quá nhiều dữ liệu lịch sử không cần thiết, số entry có thể bùng nổ.

Hash Table vì vậy nằm trực tiếp trên ranh giới giữa state modeling và storage.

## Hash Table và graph visited set

Trong implicit graph có state phức tạp, Hash Set thường lưu các state đã thăm.

Tính đúng đắn phụ thuộc canonical state representation:

```text
hai trạng thái logic giống nhau phải encode thành key bằng nhau
hai trạng thái logic khác nhau không được vô tình encode thành cùng một key nếu equality dựa trên encoding
```

Ví dụ một board puzzle có thể encode thành string, bitmask hoặc packed integer tùy kích thước.

## Grouping và frequency counting

Một pattern rất phổ biến:

```text
key -> count
key -> list of values
key -> aggregate
```

Ví dụ:

```java
freq.merge(x, 1, Integer::sum);
```

Nhưng nếu key là số nguyên dày đặc trong `[0, n)`, array thường gọn và nhanh hơn Hash Map:

```java
int[] freq = new int[n];
```

Hash Table phù hợp khi miền khóa lớn, thưa hoặc không ánh xạ tự nhiên vào một đoạn chỉ số nhỏ.

## Hash Join trong cơ sở dữ liệu

Một equi-join có thể xây Hash Table trên phía nhỏ hơn:

```text
build phase: key -> rows
probe phase: đọc bảng còn lại và tra key
```

Nếu bảng build vừa RAM và hash distribution tốt, đây là cách join rất mạnh.

Nhưng range join hoặc ordered query không phù hợp trực tiếp vì Hash Table không lưu thứ tự.

Đây là ví dụ semantics của cấu trúc quyết định loại operator nó hỗ trợ tốt.

## Khi Hash Table không phải lựa chọn phù hợp

Không nên chọn Hash Table chỉ vì lookup expected `O(1)`.

Nếu cần:

```text
ordered iteration
min/max liên tục
floor/ceiling
range query
prefix query
stable deterministic traversal order
worst-case guarantee mạnh
```

thì balanced tree, sorted array, Trie hoặc cấu trúc khác có thể phù hợp hơn.

Một Hash Table mạnh ở equality lookup nhưng cố tình không duy trì nhiều thông tin khác.

## Iteration order là một phần của contract

Một số map implementation giữ insertion order, một số không bảo đảm order, một số có order phụ thuộc layout nội bộ.

Nếu business logic hoặc test vô tình dựa vào iteration order không được contract bảo đảm, resize hoặc thay runtime có thể làm hành vi thay đổi.

Không nên nhầm “order hiện tại quan sát được” với “order được API cam kết”.

## Memory footprint

Space complexity `O(n)` chưa nói đủ.

Chaining có bucket array + node/object overhead. Open addressing cần slot trống theo load factor. Metadata, hash cache, alignment và tombstone đều tiêu tốn memory.

Với hàng chục triệu entry, vài byte trên mỗi entry có thể biến thành hàng trăm MB.

Do đó benchmark Hash Table lớn nên đo cả:

```text
bytes per entry
load factor
peak memory trong resize
allocation count
cache miss behavior
```

## Concurrency

Hash Table single-thread không tự trở thành thread-safe khi thêm một mutex quanh vài đoạn code tùy ý.

Resize đặc biệt nhạy vì thay toàn bộ table layout.

Concurrent Hash Map cần xác định:

```text
operation nào atomic
iterator có snapshot hay weak consistency
compute-if-absent có thể chạy function bao nhiêu lần theo contract
resize phối hợp ra sao
```

Một operation compound kiểu:

```text
if absent then insert
```

phải dùng primitive atomic phù hợp nếu muốn tránh race.

## Persistency và crash consistency

Nếu Hash Table nằm trong file hoặc persistent memory, ngoài logical invariant còn có crash invariant.

Một resize đang làm dở mà process chết không được để table không thể phục hồi. Điều này có thể cần write-ahead logging, copy-on-write hoặc metadata versioning.

Đây là ví dụ cùng ADT nhưng storage medium làm correctness model thay đổi hoàn toàn.

## Kiểm thử Hash Table

Ngoài test chức năng, nên kiểm tra invariant dưới chuỗi thao tác ngẫu nhiên.

```text
put/get/remove so với reference map
insert nhiều key collision có chủ đích
delete rồi reinsert
resize nhiều lần
all keys vẫn lookup được sau resize
size đúng
không có duplicate logical key
```

Với open addressing, cần test đặc biệt cho tombstone và wrap-around probe.

Property mạnh:

> Với mọi key đang được lưu, bắt đầu probe từ home position theo đúng rule phải tìm tới key trước khi gặp một slot thật sự EMPTY cho phép kết luận “không tồn tại”.

## Benchmark Hash Table đúng cách

Không benchmark chỉ trên random integer đẹp.

Nên thử:

```text
uniform random keys
sequential keys
keys có pattern bit
read-heavy
write-heavy
mixed get/put/remove
high load factor
large table vượt cache
miss-heavy workload
collision-heavy workload hợp lệ
```

Kết quả còn phụ thuộc allocator, GC, key size, equality cost và CPU cache.

## Những hiểu lầm phổ biến

“Hash Table lookup luôn O(1)” — chỉ đúng theo expected/amortized model dưới assumptions phù hợp.

“Hash collision là lỗi của hash function” — sai; collision là không thể tránh hoàn toàn.

“Hash bằng nhau nghĩa key bằng nhau” — sai.

“Xóa slot open addressing bằng cách đặt EMPTY là đủ” — có thể phá probe chain.

“Load factor càng gần 1 càng tiết kiệm và tốt” — thường làm probe cost tăng mạnh.

“Cryptographic hash luôn tốt hơn” — mục tiêu và chi phí khác nhau.

“HashMap luôn tốt hơn array vì O(1)” — array với dense integer key có direct indexing, ít overhead và locality tốt hơn.

## Mô hình tư duy

> Hash Table không loại bỏ tìm kiếm; nó **dùng hash để thu hẹp mạnh vùng phải tìm**, rồi dùng equality và collision policy để bảo toàn correctness.

Khi đánh giá một bảng băm, hãy hỏi: **hash có phù hợp workload không, key equality có ổn định không, collision được xử lý ra sao, load factor bao nhiêu, deletion giữ probe invariant thế nào, resize ảnh hưởng latency ra sao, layout có thân thiện cache không, và input có thể mang tính đối kháng không?**

Xem tiếp: [Arrays & Dynamic Arrays](./00_arrays_and_dynamic_arrays.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Java Collections](../80_language_implementations/01_java_collections_and_dsa.md) và [C Implementation Patterns](../80_language_implementations/00_c_dsa_implementation_patterns.md).