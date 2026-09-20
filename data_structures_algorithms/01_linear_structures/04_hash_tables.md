# Bảng băm
**Hash Table / 해시 테이블**

Hash table giải bài toán: từ key, làm sao “nhảy” gần tới vị trí lưu trữ mà không scan toàn bộ collection?

## Hash function

**Hàm băm (Hash Function / 해시 함수)** ánh xạ key sang integer. Bucket index thường được suy ra từ hash và table capacity.

\[
index=h(key)\bmod m
\]

Hash function cho hash table cần nhanh và phân phối key đủ đều.

## Collision là tất yếu

Nếu key space lớn hơn số buckets, hai keys có thể cùng bucket. Đây là **hash collision / 해시 충돌**. Collision không phải bug; data structure phải có strategy xử lý.

**Separate chaining** để mỗi bucket chứa nhiều entries. **Open addressing** giữ mọi entry trong array chính và probe vị trí khác khi collision.

## Load factor

\[
\alpha=\frac{n}{m}
\]

Load factor cao làm collisions tăng. Khi vượt threshold, table thường resize và rehash. Resize đắt nhưng hiếm, nên insert có thể amortized expected `O(1)`.

## Equality contract

Trong Java, nếu `a.equals(b)` là `true`, `a.hashCode()` bắt buộc bằng `b.hashCode()`. Chiều ngược lại không cần đúng vì collision được phép.

Mutable key nguy hiểm: nếu field tham gia hash/equality đổi sau khi insert, lookup có thể không tìm lại được entry theo semantics mong muốn.

## Java và JavaScript

```java
Map<String, Integer> counts = new HashMap<>();
counts.merge("apple", 1, Integer::sum);
```

```js
const m = new Map();
m.set('apple', 3);
console.log(m.get('apple'));
```

Trong JavaScript, `Map` thường phù hợp hơn plain object cho general key-value collection vì object có prototype/property semantics riêng.

## HashSet

Set chỉ quan tâm membership. Nếu cần detect duplicate, hash set có thể giảm từ `O(n²)` kiểu “mỗi phần tử lại scan các phần tử trước” xuống expected `O(n)` tổng.

## Hash table và balanced tree

Hash table phù hợp exact lookup. Balanced tree phù hợp khi cần order operations như minimum, predecessor/successor hoặc range query.

## Mental Model

> Hash table dùng hash để dự đoán vùng nhỏ nơi key phải nằm, rồi chỉ xử lý collision cục bộ.

Nó đánh đổi ordering tự nhiên để lấy expected constant-time equality lookup.

## Chaining và open addressing nhìn từ locality

Separate chaining đơn giản về logic nhưng node allocations làm locality kém. Open addressing giữ entries trong một table contiguous nên thường cache-friendly hơn, nhưng deletion và resize phức tạp hơn.

Với linear probing, cluster có thể hình thành: một vùng occupied dài làm future probes dài hơn. Robin Hood hashing giảm variance của probe length bằng cách cho entry “đi xa home bucket hơn” có quyền chiếm vị trí của entry chưa đi xa bằng.

Không cần thuộc mọi biến thể, nhưng cần hiểu một nguyên tắc: collision policy quyết định cả **correctness invariant lẫn memory behavior**.

## Tombstone trong open addressing

Nếu delete một slot bằng cách biến nó thành empty hoàn toàn, search có thể dừng quá sớm và không tìm thấy key nằm sau collision chain. Vì vậy thường cần state thứ ba:

```text
EMPTY
OCCUPIED
DELETED (tombstone)
```

Search được phép đi qua tombstone nhưng có thể dừng ở EMPTY. Insert có thể reuse tombstone.

## Resize và rehash không thể chỉ memcpy

Khi `m` thay đổi, bucket index:

\[
h(key) \bmod m
\]

cũng thay đổi. Vì thế resize hash table thường phải reinsert/rehash entries; copy raw buckets sang array lớn hơn là sai.

## Hashing compound keys

Một key như `(userId, productId)` cần combine hashes. Java record có thể cung cấp generated equality/hash code phù hợp; C cần định nghĩa rõ byte/field semantics; JavaScript có thể dùng nested `Map`, string canonicalization hoặc custom representation tùy domain.

Không nên serialize key bằng concatenation mơ hồ như:

```text
"12" + "34" == "1" + "234"
```

nếu không có separator/length encoding chắc chắn.

## Hash table và database hash join

Hash join xây hash table từ relation nhỏ theo join key, sau đó scan relation còn lại và probe table. Mental model giống hệt in-memory hash lookup, nhưng cost model thêm memory budget, partitioning và I/O.

Đây là một connection trực tiếp giữa DSA và SQL execution engine.
