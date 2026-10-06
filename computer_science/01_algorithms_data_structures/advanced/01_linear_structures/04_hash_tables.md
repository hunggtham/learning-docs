# Bảng băm

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Bảng băm**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Hàm băm và ánh xạ vào bảng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Collision là điều chắc chắn có thể xảy ra** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối hash tables với bucket, collision, load factor và lookup, để cấu trúc ánh xạ được đánh giá theo workload.

**bảng băm (hash table / 해시 테이블) / 해시 테이블**

Bảng băm giải một câu hỏi rất phổ biến: **từ một khóa, làm sao đi gần trực tiếp tới vùng lưu trữ liên quan thay vì quét toàn bộ tập dữ liệu?** Đây là một trong những cấu trúc được dùng rộng nhất trong phần mềm: bộ nhớ đệm (cache / 캐시), symbol bảng (table / 테이블), deduplication, grouping, cơ sở dữ liệu (database / 데이터베이스) băm (hash / 해시) phép nối (join / 조인), memoization, routing siêu dữ liệu (metadata / 메타데이터), frequency counting và theo dõi trạng thái đã thăm.

Ý tưởng cốt lõi là:

> bảng băm (hash table / 해시 테이블) dùng hàm băm để biến không gian khóa rất lớn thành một không gian vị trí nhỏ hơn, chấp nhận collision là tất yếu và dùng một chính sách xử lý collision để bảo toàn tính đúng đắn.

Điểm cần hiểu sâu là `O(1)` của bảng băm (hash table / 해시 테이블) không phải phép thuật. Nó dựa trên nhiều lớp giả định: chất lượng băm (hash / 해시), hệ số tải, chính sách collision, phân bố đầu vào (input / 입력), cách quản lý deletion, bộ nhớ và đôi khi cả threat mô hình (model / 모델).

## Hàm băm và ánh xạ vào bảng

Một mô hình đơn giản:

\[
chỉ mục (index / 인덱스)=h(key)\bmod m
\]

trong đó `m` là số bucket hoặc slot.

Nếu `m` là lũy thừa của hai, hiện thực (implementation / 구현) có thể dùng bitmask:

```text
index = hash & (m - 1)
```

Cách này nhanh nhưng làm chất lượng các bit thấp của băm (hash / 해시) trở nên đặc biệt quan trọng. Nếu khóa có mẫu (pattern / 패턴) mạnh ở các bit thấp mà không được trộn tốt, nhiều khóa có thể dồn vào cùng vùng.

Một băm (hash / 해시) hàm (function / 함수) phù hợp cho bảng băm thường cần:

```text
xác định trong phạm vi sử dụng cần thiết
nhanh
phân tán khóa đủ đều với workload thực tế
khó bị input pattern phá nếu môi trường có input đối kháng
```

Mục tiêu không phải “không collision”; điều đó bất khả thi khi miền khóa lớn hơn bảng.

> **Nối mạch:** **Collision là điều chắc chắn có thể xảy ra** nối từ **Hàm băm và ánh xạ vào bảng** sang **Khóa có thể thay đổi là một lỗi thiết kế nguy hiểm**, vì cơ chế trước tạo đầu vào cho bước sau.

## Collision là điều chắc chắn có thể xảy ra

Theo pigeonhole principle, nếu số khóa khả dĩ lớn hơn số bucket, hai khóa khác nhau có thể cùng ánh xạ tới một vị trí.

Do đó bảng băm (hash table / 해시 테이블) đúng phải có hai tầng:

```text
hash -> tìm vùng ứng viên
key equality -> xác nhận đúng khóa
```

Không bao giờ được dùng “băm (hash / 해시) bằng nhau” như bằng chứng hai khóa bằng nhau.

Trong Java:

```text
a.equals(b) == true  =>  a.hashCode() == b.hashCode()
```

Chiều ngược lại không bắt buộc.

> **Nối mạch:** **Khóa có thể thay đổi là một lỗi thiết kế nguy hiểm** nối từ **Collision là điều chắc chắn có thể xảy ra** sang **Hai họ xử lý collision chính**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khóa có thể thay đổi là một lỗi thiết kế nguy hiểm

Nếu một đối tượng (object / 객체) được dùng làm khóa rồi các trường tham gia `equals/hashCode` bị sửa, entry vẫn nằm ở vị trí được chọn theo băm (hash / 해시) cũ nhưng lookup sau đó tính băm (hash / 해시) mới.

Kết quả là khóa có thể trở thành “mất tích” về lô-gic (logic / 논리) dù entry vẫn chiếm bộ nhớ.

Trong Java, compound key bất biến như bản ghi (record / 레코드) thường an toàn hơn:

```java
record UserProductKey(long userId, long productId) {}
```

Trong C hoặc JavaScript, cũng phải tự định nghĩa rõ chuẩn gốc (canonical / 정본) biểu diễn (representation / 표현) của khóa.

> **Nối mạch:** **Hai họ xử lý collision chính** nối từ **Khóa có thể thay đổi là một lỗi thiết kế nguy hiểm** sang **Separate chaining**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hai họ xử lý collision chính

Hai chiến lược lớn là:

```text
separate chaining
open addressing
```

Chúng cùng cung cấp dictionary ngữ nghĩa (semantics / 의미론) nhưng có mô hình bộ nhớ rất khác.

> **Nối mạch:** **Separate chaining** nối từ **Hai họ xử lý collision chính** sang **Hệ số tải**, vì cơ chế trước tạo đầu vào cho bước sau.

## Separate chaining

Mỗi bucket trỏ tới một collection các entry có cùng bucket chỉ mục (index / 인덱스).

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

Deletion khá đơn giản vì chỉ cần gỡ entry khỏi bucket chuỗi (chain / 사슬).

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

Một hiện thực (implementation / 구현) hiện đại có thể dùng bucket nhỏ dạng mảng hoặc bố cục (layout / 레이아웃) gọn thay vì linked danh sách (list / 목록) cổ điển.

> **Nối mạch:** **Hệ số tải** nối từ **Separate chaining** sang **Resize và rehash**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hệ số tải

Định nghĩa:

\[
\alpha=\frac nm
\]

với `n` là số entry và `m` là số bucket/slot.

Tải (load / 로드) factor càng cao thì bộ nhớ càng tiết kiệm nhưng collision/probing thường càng đắt.

Với chaining, `α` có thể lớn hơn 1. Với open addressing, bảng cần slot trống để probing kết thúc hiệu quả nên `α` tiến gần 1 thường làm hiệu năng giảm mạnh.

Do đó sức chứa (capacity / 용량) planning là sự đánh đổi giữa bộ nhớ (memory / 메모리) và probe chi phí (cost / 비용).

> **Nối mạch:** **Resize và rehash** nối từ **Hệ số tải** sang **Incremental rehashing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Resize và rehash

Khi sức chứa (capacity / 용량) đổi, bucket chỉ mục (index / 인덱스) thường đổi theo:

\[
h(key)\bmod m_{old}\neq h(key)\bmod m_{new}
\]

Vì vậy resize thường cần **rehash/reinsert** các entry vào bảng mới.

Resize có thể tốn `O(n)`, nhưng nếu sức chứa (capacity / 용량) tăng theo cấp số nhân thì tổng chi phí trên chuỗi nhiều insert thường được phân tích khấu hao thành expected `O(1)` mỗi insert dưới giả định băm (hash / 해시) phù hợp.

### Vì sao tăng từng 1 là tệ?

Nếu bảng gần đầy và mỗi lần chỉ tăng sức chứa (capacity / 용량) rất ít, ta có thể rehash gần toàn bộ bảng quá thường xuyên. Tăng theo tỷ lệ giúp số lần resize chỉ logarithmic theo số entry.

> **Nối mạch:** **Incremental rehashing** nối từ **Resize và rehash** sang **Open addressing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Incremental rehashing

Rehash toàn bộ bảng trong một thao tác (operation / 연산) có thể tạo độ trễ (latency / 지연 시간) spike.

Một số hệ thống chọn **incremental rehashing**:

```text
giữ old table + new table
di chuyển một lượng nhỏ bucket/entry ở mỗi operation
lookup tạm thời có thể phải kiểm tra cả hai bảng
khi migrate xong thì bỏ bảng cũ
```

Tổng công việc không nhất thiết giảm, nhưng chi phí được dàn ra để cải thiện tail độ trễ (latency / 지연 시간).

Đây là ví dụ rõ ràng của sự đánh đổi (trade-off / 트레이드오프) thông lượng (throughput / 처리량)–độ trễ (latency / 지연 시간).

> **Nối mạch:** **Open addressing** nối từ **Incremental rehashing** sang **Vì sao open addressing có thể rất nhanh trên máy thật?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Open addressing

Open addressing giữ entry trực tiếp trong array bảng (table / 테이블). Khi home slot đã occupied, thuật toán thử các slot khác theo **probe chuỗi (sequence / 시퀀스)**.

### Tuyến tính (linear / 선형) probing

\[
index_i=(h(key)+i)\bmod m
\]

Rất đơn giản và có locality tốt vì các slot gần nhau trong bộ nhớ.

### Quadratic probing

Probe offset tăng theo hàm bậc hai nhằm giảm một số dạng clustering.

### Double hashing

Dùng băm (hash / 해시) thứ hai để tạo stride:

\[
index_i=(h_1(key)+i\cdot h_2(key))\bmod m
\]

Thiết kế phải bảo đảm stride cho phép đi qua đủ không gian slot theo sức chứa (capacity / 용량) đã chọn.

> **Nối mạch:** **Vì sao open addressing có thể rất nhanh trên máy thật?** nối từ **Open addressing** sang **Primary clustering**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao open addressing có thể rất nhanh trên máy thật?

Entry nằm gần nhau trong một mảng, nên CPU có thể tận dụng bộ nhớ đệm (cache / 캐시) line và prefetch tốt hơn chaining bằng pointer.

Do đó hai cấu trúc cùng expected `O(1)` có thể khác đáng kể về tốc độ thực tế vì **dữ liệu (data / 데이터) movement** chứ không phải Big-O.

Đây là một bài học tổng quát: độ phức tạp tiệm cận không thay thế phân tích bố cục (layout / 레이아웃) bộ nhớ.

> **Nối mạch:** **Primary clustering** nối từ **Vì sao open addressing có thể rất nhanh trên máy thật?** sang **Deletion và tombstone**, vì cơ chế trước tạo đầu vào cho bước sau.

## Primary clustering

Tuyến tính (linear / 선형) probing có thể tạo các cụm slot occupied liên tiếp.

Khi một key băm (hash / 해시) vào giữa cụm, nó phải đi qua cụm và thường được đặt ở cuối. Cụm dài hơn lại thu hút nhiều collision hơn.

Đây là **primary clustering**.

Ngay cả băm (hash / 해시) hàm (function / 함수) khá tốt vẫn không loại hoàn toàn hiện tượng này vì probing quy tắc (rule / 규칙) tự tạo phụ thuộc giữa các vị trí.

> **Nối mạch:** **Deletion và tombstone** nối từ **Primary clustering** sang **Backward-shift deletion**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** **Backward-shift deletion** nối từ **Deletion và tombstone** sang **Khoảng cách probe như một đại lượng trạng thái**, vì cơ chế trước tạo đầu vào cho bước sau.

## Backward-shift deletion

Một số scheme, đặc biệt các biến thể tuyến tính (linear / 선형) probing, có thể dịch một số entry sau điểm xóa về phía trước để bảo toàn reachability của probe chuỗi (sequence / 시퀀스) mà không giữ tombstone lâu dài.

Điểm quan trọng không phải nhớ thuật toán xóa cụ thể, mà là:

> deletion phải được chứng minh dựa trên bất biến (invariant / 불변식) của probe chuỗi (sequence / 시퀀스).

Không thể tự ý “dọn slot cho đẹp” nếu việc đó làm lookup mất đường tới key khác.

> **Nối mạch:** **Khoảng cách probe như một đại lượng trạng thái** nối từ **Backward-shift deletion** sang **Robin Hood hashing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khoảng cách probe như một đại lượng trạng thái

Với open addressing, ngoài băm (hash / 해시) và key còn có một đại lượng quan trọng: entry đã đi xa bao nhiêu slot từ home position.

Probe distance ảnh hưởng:

```text
latency lookup
variance giữa các key
quyết định swap trong Robin Hood hashing
quy tắc dừng lookup ở một số scheme
```

Nhìn probe distance như siêu dữ liệu (metadata / 메타데이터) giúp hiểu các thiết kế hiện đại hơn.

> **Nối mạch:** **Robin Hood hashing** nối từ **Khoảng cách probe như một đại lượng trạng thái** sang **Cuckoo hashing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Robin Hood hashing

Ý tưởng Robin Hood là “lấy của người may mắn gần nhà để giúp người xui phải đi xa”.

Khi entry mới có probe distance lớn hơn entry đang chiếm slot, hai entry có thể đổi chỗ. Mục tiêu là giảm variance của probe length và tránh một số key có đường dò quá dài.

Sự đánh đổi (trade-off / 트레이드오프):

```text
lookup thường ổn định hơn
insert phức tạp hơn
metadata/deletion cần cẩn thận hơn
```

Đây là ví dụ một cấu trúc tối ưu không chỉ mean chi phí (cost / 비용) mà còn phân phối chi phí (cost / 비용).

> **Nối mạch:** **Cuckoo hashing** nối từ **Robin Hood hashing** sang **SwissTable-style thiết kế (design / 설계): bài học về siêu dữ liệu (metadata / 메타데이터) và vectorization**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cuckoo hashing

Cuckoo hashing cho mỗi key một số vị trí khả dĩ, ví dụ hai băm (hash / 해시) hàm (function / 함수):

```text
slot1 = h1(key)
slot2 = h2(key)
```

Nếu cả hai bị chiếm, insert có thể “đá” một entry hiện tại sang vị trí thay thế của nó và tiếp tục chuỗi di chuyển.

Lookup rất hấp dẫn vì chỉ phải kiểm tra một số vị trí cố định nhỏ.

Nhưng insertion có thể tạo cycle; khi đó cần rehash hoặc resize.

Cuckoo hashing cho thấy một sự đánh đổi (trade-off / 트레이드오프) khác: lookup đơn giản hơn đổi lại insertion khó dự đoán hơn.

> **Nối mạch:** **Cuckoo hashing** đặt vấn đề; **SwissTable-style thiết kế (design / 설계): bài học về siêu dữ liệu (metadata / 메타데이터) và vectorization** kiểm tra bằng chứng, rồi **Băm (hash / 해시) mixing** mở rộng hệ quả.

## SwissTable-style thiết kế (design / 설계): bài học về siêu dữ liệu (metadata / 메타데이터) và vectorization

Các bảng băm (hash table / 해시 테이블) hiệu năng cao hiện đại thường tách siêu dữ liệu (metadata / 메타데이터) nhỏ của slot khỏi payload và quét một nhóm siêu dữ liệu (metadata / 메타데이터) cùng lúc để lọc nhanh candidate.

Một điều khiển (control / 제어) byte có thể mã hóa trạng thái slot và một fingerprint ngắn của băm (hash / 해시). CPU có thể so sánh nhiều điều khiển (control / 제어) byte song song trước khi chạm vào key thật.

Điều đáng học không phải một hiện thực (implementation / 구현) cụ thể, mà là nguyên lý:

> Cùng ADT và cùng expected Big-O vẫn có thể khác nhau rất lớn nhờ bố cục (layout / 레이아웃) siêu dữ liệu (metadata / 메타데이터), bộ nhớ đệm (cache / 캐시) locality, branch hành vi (behavior / 동작) và SIMD.

> **Nối mạch:** **SwissTable-style thiết kế (design / 설계): bài học về siêu dữ liệu (metadata / 메타데이터) và vectorization** đặt vấn đề; **Băm (hash / 해시) mixing** kiểm tra bằng chứng, rồi **Universal hashing: trực giác lý thuyết** mở rộng hệ quả.

## Băm (hash / 해시) mixing

Nếu sức chứa (capacity / 용량) là lũy thừa của hai, chỉ một số bit của băm (hash / 해시) quyết định bucket. Nếu key mẫu (pattern / 패턴) làm các bit đó kém phân tán, collision tăng mạnh.

Ví dụ ID luôn là bội số của `1024` có nhiều bit thấp bằng 0. Một ánh xạ (mapping / 매핑) dùng trực tiếp bit thấp mà không mix có thể tạo phân phối (distribution / 분포) xấu.

Do đó hiện thực (implementation / 구현) thường có bước trộn để khuếch tán thông tin từ toàn bộ key/băm (hash / 해시) vào các bit dùng cho chỉ mục (index / 인덱스).

> **Nối mạch:** **Universal hashing: trực giác lý thuyết** nối từ **Băm (hash / 해시) mixing** sang **Băm (hash / 해시) flooding và đầu vào (input / 입력) đối kháng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Universal hashing: trực giác lý thuyết

Universal hashing chọn ngẫu nhiên một băm (hash / 해시) hàm (function / 함수) từ một family được thiết kế sao cho với hai key khác nhau, xác suất collision bị chặn.

Ý tưởng quan trọng là: nếu attacker hoặc đầu vào (input / 입력) không biết chính xác băm (hash / 해시) hàm (function / 함수) được chọn, một fixed set key khó ép toàn bộ collision theo cùng cách.

Universal hashing giúp nối randomization với expected dictionary hiệu năng (performance / 성능).

> **Nối mạch:** **Băm (hash / 해시) flooding và đầu vào (input / 입력) đối kháng** nối từ **Universal hashing: trực giác lý thuyết** sang **Bảng băm (hash table / 해시 테이블) băm (hash / 해시) và cryptographic băm (hash / 해시) không cùng mục tiêu**, vì cơ chế trước tạo đầu vào cho bước sau.

## Băm (hash / 해시) flooding và đầu vào (input / 입력) đối kháng

Nếu người dùng kiểm soát key và biết cách tạo nhiều collision, bảng băm (hash table / 해시 테이블) có thể suy thoái nghiêm trọng và trở thành véc-tơ (vector / 벡터) denial-of-service.

Các biện pháp có thể gồm:

```text
hash seed ngẫu nhiên
hash tốt hơn
bucket treeification
thay đổi implementation khi collision quá lớn
rate limiting ở tầng hệ thống
```

Khi phân tích security-sensitive mã (code / 코드), phải tách:

```text
normal workload
random workload
adversarial workload
```

Expected `O(1)` luôn đi kèm giả định (assumption / 가정).

> **Nối mạch:** **Bảng băm (hash table / 해시 테이블) băm (hash / 해시) và cryptographic băm (hash / 해시) không cùng mục tiêu** nối từ **Băm (hash / 해시) flooding và đầu vào (input / 입력) đối kháng** sang **Compound key**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bảng băm (hash table / 해시 테이블) băm (hash / 해시) và cryptographic băm (hash / 해시) không cùng mục tiêu

SHA-256 được thiết kế cho các thuộc tính mật mã mạnh. băm (hash / 해시) hàm (function / 함수) cho in-memory bảng (table / 테이블) thường ưu tiên tốc độ, phân phối và khả năng chống mẫu (pattern / 패턴) đủ cho threat mô hình (model / 모델) cụ thể.

Dùng cryptographic băm (hash / 해시) cho mọi map có thể quá đắt. Ngược lại, dùng một băm (hash / 해시) cực nhanh nhưng dễ bị crafted collision có thể không phù hợp với public-facing máy chủ (server / 서버).

“băm (hash / 해시)” là một họ ý tưởng, không phải một loại hàm duy nhất.

> **Nối mạch:** **Compound key** nối từ **Bảng băm (hash table / 해시 테이블) băm (hash / 해시) và cryptographic băm (hash / 해시) không cùng mục tiêu** sang **Bảng băm (hash table / 해시 테이블) và memoization**, vì cơ chế trước tạo đầu vào cho bước sau.

## Compound key

Khóa `(userId, productId)` phải có equality/băm (hash / 해시) theo cặp.

Không nên ghép chuỗi mơ hồ:

```text
"12" + "34" = "1234"
"1"  + "234" = "1234"
```

Có thể dùng tuple/bản ghi (record / 레코드), encoding có delimiter/length rõ hoặc nested map.

Java:

```java
record Key(long userId, long productId) {}
```

JavaScript có một khác biệt quan trọng: đối tượng (object / 객체) dùng làm key trong `Map` được so theo định danh (identity / 식별자). Hai đối tượng (object / 객체) literal có cùng trường dữ liệu (field / 필드) không tự động là cùng key:

```js
const a = {x: 1};
const b = {x: 1};
console.log(a === b); // false
```

Nếu cần giá trị (value / 값) ngữ nghĩa (semantics / 의미론), phải canonicalize hoặc encode key.

> **Nối mạch:** **Bảng băm (hash table / 해시 테이블) và memoization** nối từ **Compound key** sang **Bảng băm (hash table / 해시 테이블) và đồ thị (graph / 그래프) visited set**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bảng băm (hash table / 해시 테이블) và memoization

Memoization thường dùng map:

```text
state -> computed answer
```

Điều này chỉ đúng nếu key chứa đầy đủ trạng thái (state / 상태) ảnh hưởng tới kết quả.

Nếu memo key bỏ một dimension quan trọng, bộ nhớ đệm (cache / 캐시) có thể trả lời của trạng thái (state / 상태) khác. Đây là lỗi mô hình hóa, không phải lỗi bảng băm (hash table / 해시 테이블).

Nếu key chứa quá nhiều dữ liệu lịch sử không cần thiết, số entry có thể bùng nổ.

Bảng băm (hash table / 해시 테이블) vì vậy nằm trực tiếp trên ranh giới giữa trạng thái (state / 상태) modeling và lưu trữ (storage / 저장소).

> **Nối mạch:** **Bảng băm (hash table / 해시 테이블) và đồ thị (graph / 그래프) visited set** nối từ **Bảng băm (hash table / 해시 테이블) và memoization** sang **Grouping và frequency counting**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bảng băm (hash table / 해시 테이블) và đồ thị (graph / 그래프) visited set

Trong implicit đồ thị (graph / 그래프) có trạng thái (state / 상태) phức tạp, băm (hash / 해시) Set thường lưu các trạng thái (state / 상태) đã thăm.

Tính đúng đắn phụ thuộc chuẩn gốc (canonical / 정본) trạng thái (state / 상태) biểu diễn (representation / 표현):

```text
hai trạng thái logic giống nhau phải encode thành key bằng nhau
hai trạng thái logic khác nhau không được vô tình encode thành cùng một key nếu equality dựa trên encoding
```

Ví dụ một board puzzle có thể encode thành string, bitmask hoặc packed integer tùy kích thước.

> **Nối mạch:** **Grouping và frequency counting** nối từ **Bảng băm (hash table / 해시 테이블) và đồ thị (graph / 그래프) visited set** sang **Băm (hash / 해시) phép nối (join / 조인) trong cơ sở dữ liệu**, vì cơ chế trước tạo đầu vào cho bước sau.

## Grouping và frequency counting

Một mẫu (pattern / 패턴) rất phổ biến:

```text
key -> count
key -> list of values
key -> aggregate
```

Ví dụ:

```java
freq.merge(x, 1, Integer::sum);
```

Nhưng nếu key là số nguyên dày đặc trong `[0, n)`, array thường gọn và nhanh hơn băm (hash / 해시) Map:

```java
int[] freq = new int[n];
```

Bảng băm (hash table / 해시 테이블) phù hợp khi miền khóa lớn, thưa hoặc không ánh xạ tự nhiên vào một đoạn chỉ số nhỏ.

> **Nối mạch:** **Grouping và frequency counting** đặt vấn đề; **Băm (hash / 해시) phép nối (join / 조인) trong cơ sở dữ liệu** kiểm tra bằng chứng, rồi **Khi bảng băm (hash table / 해시 테이블) không phải lựa chọn phù hợp** mở rộng hệ quả.

## Băm (hash / 해시) phép nối (join / 조인) trong cơ sở dữ liệu

Một equi-join có thể xây bảng băm (hash table / 해시 테이블) trên phía nhỏ hơn:

```text
build phase: key -> rows
probe phase: đọc bảng còn lại và tra key
```

Nếu bảng bản dựng (build / 빌드) vừa RAM và băm (hash / 해시) phân phối (distribution / 분포) tốt, đây là cách phép nối (join / 조인) rất mạnh.

Nhưng phạm vi (range / 범위) phép nối (join / 조인) hoặc ordered truy vấn (query / 쿼리) không phù hợp trực tiếp vì bảng băm (hash table / 해시 테이블) không lưu thứ tự.

Đây là ví dụ ngữ nghĩa (semantics / 의미론) của cấu trúc quyết định loại operator nó hỗ trợ tốt.

> **Nối mạch:** **Băm (hash / 해시) phép nối (join / 조인) trong cơ sở dữ liệu** đặt vấn đề; **Khi bảng băm (hash table / 해시 테이블) không phải lựa chọn phù hợp** kiểm tra bằng chứng, rồi **Iteration thứ tự (order / 순서) là một phần của đặc tả hợp đồng (contract / 계약)** mở rộng hệ quả.

## Khi bảng băm (hash table / 해시 테이블) không phải lựa chọn phù hợp

Không nên chọn bảng băm (hash table / 해시 테이블) chỉ vì lookup expected `O(1)`.

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

thì balanced cây (tree / 트리), sorted array, Trie hoặc cấu trúc khác có thể phù hợp hơn.

Một bảng băm (hash table / 해시 테이블) mạnh ở equality lookup nhưng cố tình không duy trì nhiều thông tin khác.

> **Nối mạch:** **Iteration thứ tự (order / 순서) là một phần của đặc tả hợp đồng (contract / 계약)** nối từ **Khi bảng băm (hash table / 해시 테이블) không phải lựa chọn phù hợp** sang **Bộ nhớ (memory / 메모리) footprint**, vì cơ chế trước tạo đầu vào cho bước sau.

## Iteration thứ tự (order / 순서) là một phần của đặc tả hợp đồng (contract / 계약)

Một số map hiện thực (implementation / 구현) giữ insertion thứ tự (order / 순서), một số không bảo đảm thứ tự (order / 순서), một số có thứ tự (order / 순서) phụ thuộc bố cục (layout / 레이아웃) nội bộ.

Nếu lô-gic nghiệp vụ (business logic / 비즈니스 로직) hoặc kiểm thử (test / 테스트) vô tình dựa vào iteration thứ tự (order / 순서) không được đặc tả hợp đồng (contract / 계약) bảo đảm, resize hoặc thay thời gian chạy (runtime / 런타임) có thể làm hành vi thay đổi.

Không nên nhầm “thứ tự (order / 순서) hiện tại quan sát được” với “thứ tự (order / 순서) được API cam kết”.

> **Nối mạch:** **Bộ nhớ (memory / 메모리) footprint** nối từ **Iteration thứ tự (order / 순서) là một phần của đặc tả hợp đồng (contract / 계약)** sang **Tính đồng thời (concurrency / 동시성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bộ nhớ (memory / 메모리) footprint

Không gian (space / 공간) độ phức tạp (complexity / 복잡도) `O(n)` chưa nói đủ.

Chaining có bucket array + nút (node / 노드)/đối tượng (object / 객체) overhead. Open addressing cần slot trống theo tải (load / 로드) factor. siêu dữ liệu (metadata / 메타데이터), băm (hash / 해시) bộ nhớ đệm (cache / 캐시), alignment và tombstone đều tiêu tốn bộ nhớ (memory / 메모리).

Với hàng chục triệu entry, vài byte trên mỗi entry có thể biến thành hàng trăm MB.

Do đó benchmark bảng băm (hash table / 해시 테이블) lớn nên đo cả:

```text
bytes per entry
load factor
peak memory trong resize
allocation count
cache miss behavior
```

> **Nối mạch:** **Tính đồng thời (concurrency / 동시성)** nối từ **Bộ nhớ (memory / 메모리) footprint** sang **Persistency và crash consistency**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tính đồng thời (concurrency / 동시성)

Bảng băm (hash table / 해시 테이블) single-thread không tự trở thành thread-safe khi thêm một mutex quanh vài đoạn mã (code / 코드) tùy ý.

Resize đặc biệt nhạy vì thay toàn bộ bảng (table / 테이블) bố cục (layout / 레이아웃).

Concurrent băm (hash / 해시) Map cần xác định:

```text
operation nào atomic
iterator có snapshot hay weak consistency
compute-if-absent có thể chạy function bao nhiêu lần theo contract
resize phối hợp ra sao
```

Một thao tác (operation / 연산) compound kiểu:

```text
if absent then insert
```

phải dùng thành phần nguyên thủy (primitive / 기본 요소) atomic phù hợp nếu muốn tránh race.

> **Nối mạch:** **Persistency và crash consistency** nối từ **Tính đồng thời (concurrency / 동시성)** sang **Kiểm thử bảng băm (hash table / 해시 테이블)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Persistency và crash consistency

Nếu bảng băm (hash table / 해시 테이블) nằm trong tệp (file / 파일) hoặc persistent bộ nhớ (memory / 메모리), ngoài logical bất biến (invariant / 불변식) còn có crash bất biến (invariant / 불변식).

Một resize đang làm dở mà tiến trình (process / 프로세스) chết không được để bảng (table / 테이블) không thể phục hồi. Điều này có thể cần write-ahead logging, sao chép khi ghi (copy-on-write / 쓰기 시 복사) hoặc siêu dữ liệu (metadata / 메타데이터) versioning.

Đây là ví dụ cùng ADT nhưng lưu trữ (storage / 저장소) medium làm tính đúng đắn (correctness / 정확성) mô hình (model / 모델) thay đổi hoàn toàn.

> **Nối mạch:** **Kiểm thử bảng băm (hash table / 해시 테이블)** nối từ **Persistency và crash consistency** sang **Benchmark bảng băm (hash table / 해시 테이블) đúng cách**, vì cơ chế trước tạo đầu vào cho bước sau.

## Kiểm thử bảng băm (hash table / 해시 테이블)

Ngoài kiểm thử (test / 테스트) chức năng, nên kiểm tra bất biến (invariant / 불변식) dưới chuỗi thao tác ngẫu nhiên.

```text
put/get/remove so với reference map
insert nhiều key collision có chủ đích
delete rồi reinsert
resize nhiều lần
all keys vẫn lookup được sau resize
size đúng
không có duplicate logical key
```

Với open addressing, cần kiểm thử (test / 테스트) đặc biệt cho tombstone và wrap-around probe.

Thuộc tính (property / 속성) mạnh:

> Với mọi key đang được lưu, bắt đầu probe từ home position theo đúng quy tắc (rule / 규칙) phải tìm tới key trước khi gặp một slot thật sự EMPTY cho phép kết luận “không tồn tại”.

> **Nối mạch:** **Benchmark bảng băm (hash table / 해시 테이블) đúng cách** nối từ **Kiểm thử bảng băm (hash table / 해시 테이블)** sang **Những hiểu lầm phổ biến**, vì cơ chế trước tạo đầu vào cho bước sau.

## Benchmark bảng băm (hash table / 해시 테이블) đúng cách

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

Kết quả còn phụ thuộc allocator, GC, key kích thước (size / 크기), equality chi phí (cost / 비용) và CPU bộ nhớ đệm (cache / 캐시).

> **Nối mạch:** **Những hiểu lầm phổ biến** nối từ **Benchmark bảng băm (hash table / 해시 테이블) đúng cách** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Những hiểu lầm phổ biến

“bảng băm (hash table / 해시 테이블) lookup luôn O(1)” — chỉ đúng theo expected/amortized mô hình (model / 모델) dưới các giả định (assumptions / 가정들) phù hợp.

“băm (hash / 해시) collision là lỗi của băm (hash / 해시) hàm (function / 함수)” — sai; collision là không thể tránh hoàn toàn.

“băm (hash / 해시) bằng nhau nghĩa key bằng nhau” — sai.

“Xóa slot open addressing bằng cách đặt EMPTY là đủ” — có thể phá probe chuỗi (chain / 사슬).

“tải (load / 로드) factor càng gần 1 càng tiết kiệm và tốt” — thường làm probe chi phí (cost / 비용) tăng mạnh.

“Cryptographic băm (hash / 해시) luôn tốt hơn” — mục tiêu và chi phí khác nhau.

“HashMap luôn tốt hơn array vì O(1)” — array với dense integer key có direct indexing, ít overhead và locality tốt hơn.

> **Nối mạch:** **Bảng băm**, **Mô hình tư duy** tổng hợp từ **Những hiểu lầm phổ biến**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy

> bảng băm (hash table / 해시 테이블) không loại bỏ tìm kiếm; nó **dùng băm (hash / 해시) để thu hẹp mạnh vùng phải tìm**, rồi dùng equality và collision chính sách (policy / 정책) để bảo toàn tính đúng đắn (correctness / 정확성).

Khi đánh giá một bảng băm, hãy hỏi: **băm (hash / 해시) có phù hợp tải công việc (workload / 워크로드) không, key equality có ổn định không, collision được xử lý ra sao, tải (load / 로드) factor bao nhiêu, deletion giữ probe bất biến (invariant / 불변식) thế nào, resize ảnh hưởng độ trễ (latency / 지연 시간) ra sao, bố cục (layout / 레이아웃) có thân thiện bộ nhớ đệm (cache / 캐시) không, và đầu vào (input / 입력) có thể mang tính đối kháng không?**

Xem tiếp: [Arrays & Dynamic Arrays](./00_arrays_and_dynamic_arrays.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Java Collections](../80_language_implementations/01_java_collections_and_dsa.md) và [C Implementation Patterns](../80_language_implementations/00_c_dsa_implementation_patterns.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
