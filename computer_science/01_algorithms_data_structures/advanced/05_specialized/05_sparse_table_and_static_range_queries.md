# bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Power-of-two decomposition** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Tại sao các lũy thừa của hai?** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**스파스 테이블과 정적 구간 질의**

bảng thưa là một cấu trúc (structure / 구조) dành cho khối lượng công việc rất cụ thể: **dữ liệu tĩnh (static data / 정적 데이터)** nhưng có rất nhiều các truy vấn khoảng. Nếu mảng không cập nhật, ta có thể trả nhiều tiền xử lý và bộ nhớ hơn để truy vấn sau đó cực nhanh.

Đây là cùng sự đánh đổi (trade-off / 트레이드오프) quen thuộc của DSA:

```text
ít mutation
+ nhiều repeated queries
→ preprocess mạnh
```

Sparse bảng (table / 테이블) đặc biệt mạnh với các phép toán như cực tiểu, cực đại và GCD, cho phép trả lời truy vấn trong `O(1)` sau tiền xử lý `O(n log n)`.

## Power-of-two decomposition

bảng thưa lưu aggregate của mọi interval có length là lũy thừa của hai:

```text
st[k][i] = aggregate của đoạn bắt đầu tại i, length 2^k
```

Cơ sở (base / 기반):

```text
st[0][i] = a[i]
```

Chuyển tiếp (transition / 전이):

\[
st[k][i] = kết hợp(st[k-1][i], st[k-1][i + 2^{k-1}])
\]

Vì một khoảng có độ dài `2^k` có thể chia thành hai nửa, mỗi nửa dài `2^(k-1)`.

Construction cần khoảng:

\[
O(n\log n)
\]

Thời gian (time / 시간) và bộ nhớ.

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Tại sao các lũy thừa của hai?** tiếp nhận điểm tựa từ **Power-of-two decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java construction cho RMQ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tại sao các lũy thừa của hai?

Mọi positive length có logarithmic cách biểu diễn (representation / 표현) theo các lũy thừa của hai. Precompute intervals tăng gấp đôi giúp ta reuse kết quả nhỏ để tạo khối (block / 블록) lớn.

Ý tưởng này xuất hiện nhiều nơi:

```text
binary lifting ancestors
exponentiation by squaring
segment-tree levels
sparse table
```

các lũy thừa của hai không phải magic; chúng tạo hierarchy có số các tầng logarithmic.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Java construction cho RMQ** tiếp nhận điểm tựa từ **Tại sao các lũy thừa của hai?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **O(1) RMQ nhờ idempotence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java construction cho RMQ

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```java
final class SparseMin {
    private final int[][] st;
    private final int[] log2;

    SparseMin(int[] a) {
        int n = a.length;

        log2 = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            log2[i] = log2[i / 2] + 1;
        }

        int levels = n == 0 ? 0 : log2[n] + 1;
        st = new int[levels][n];

        if (n == 0) return;

        System.arraycopy(a, 0, st[0], 0, n);

        for (int k = 1; k < levels; k++) {
            int len = 1 << k;
            int half = len >> 1;

            for (int i = 0; i + len <= n; i++) {
                st[k][i] = Math.min(
                    st[k - 1][i],
                    st[k - 1][i + half]
                );
            }
        }
    }

    int min(int l, int r) { // inclusive
        int len = r - l + 1;
        int k = log2[len];
        return Math.min(
            st[k][l],
            st[k][r - (1 << k) + 1]
        );
    }
}
```

Precompute `floor(log2(x))` tránh logarit dấu phẩy động trong truy vấn và làm ngữ nghĩa (semantics / 의미론) integer rõ ràng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **O(1) RMQ nhờ idempotence** tiếp nhận điểm tựa từ **Java construction cho RMQ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Associative chưa đủ cho classic O(1) trick** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## O(1) RMQ nhờ idempotence

Cho phạm vi (range / 범위) `[L,R]`, đặt:

\[
k = \lfloor \log_2(R-L+1) \rfloor
\]

Ta chọn hai blocks length `2^k`:

```text
[L ........ L+2^k-1]
        [R-2^k+1 ........ R]
```

Hai blocks có thể overlap. Với `min`:

\[
\min(x,x)=x
\]

nên việc một phần tử xuất hiện ở cả hai blocks không thay kết quả.

tính chất:

\[
f(x,x)=x
\]

được gọi là **idempotence / 멱등성**.

Min, max và GCD là các examples quan trọng.

Do đó truy vấn chỉ kết hợp hai precomputed các giá trị → `O(1)`.

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Associative chưa đủ cho classic O(1) trick** tiếp nhận điểm tựa từ **O(1) RMQ nhờ idempotence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bảng thưa cho GCD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Associative chưa đủ cho classic O(1) trick

Sum có tính kết hợp (associative):

\[
(a+b)+c=a+(b+c)
\]

nhưng không lũy đẳng (idempotent):

\[
x+x\ne x
\]

Nếu hai blocks overlap, phần overlap bị double-count.

Vì vậy classic bảng thưa two-overlap truy vấn không hoạt động cho sum.

Đây là distinction cần hiểu rõ:

```text
associative -> dễ combine partition không overlap
idempotent  -> cho phép overlap mà result không đổi
```

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **bảng thưa cho GCD** tiếp nhận điểm tựa từ **Associative chưa đủ cho classic O(1) trick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bảng thưa cho AND/OR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bảng thưa cho GCD

GCD lũy đẳng (idempotent):

\[
\gcd(x,x)=x
\]

nên truy vấn phạm vi (range / 범위) GCD cũng `O(1)` bằng hai blocks overlap.

Điều này hữu ích trong number-theory phạm vi (range / 범위) problems.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **bảng thưa cho AND/OR** tiếp nhận điểm tựa từ **bảng thưa cho GCD** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Non-overlapping decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bảng thưa cho AND/OR

Bitwise AND và OR cũng lũy đẳng (idempotent):

```text
x & x = x
x | x = x
```

nên có thể dùng same RMQ-style truy vấn technique.

Bitwise XOR không lũy đẳng (idempotent) vì:

```text
x ^ x = 0
```

nên overlap trick không đúng.

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Non-overlapping decomposition** tiếp nhận điểm tựa từ **bảng thưa cho AND/OR** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Disjoint bảng thưa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Non-overlapping decomposition

Ngay cả với có tính kết hợp (associative) non-lũy đẳng (idempotent) thao tác, ordinary bảng thưa blocks vẫn có thể decompose phạm vi (range / 범위) thành `O(log n)` disjoint power-of-two blocks.

Ví dụ sum:

```text
length 13 = 8 + 4 + 1
```

truy vấn `O(log n)`.

Nhưng với tĩnh sum, tổng tiền tố cho `O(1)` và bộ nhớ `O(n)` nên bảng thưa thường không phải lựa chọn tốt.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Disjoint bảng thưa** tiếp nhận điểm tựa từ **Non-overlapping decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bảng thưa vs tổng tiền tố** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Disjoint bảng thưa

**Disjoint bảng thưa (DST)** hỗ trợ `O(1)` truy vấn khoảng (range query) cho nhiều có tính kết hợp (associative) các thao tác, kể cả sum.

Mô hình tư duy khác classic bảng thưa.

Ở mỗi tầng, mảng được chia thành blocks. Quanh midpoint của mỗi khối (block / 블록), preprocess:

```text
suffix aggregates bên trái midpoint
prefix aggregates bên phải midpoint
```

Với truy vấn `[L,R]`, tìm highest bit nơi `L` và `R` khác nhau. tầng đó xác định một midpoint nằm giữa hai endpoints. Answer kết hợp:

```text
suffix(L -> midpoint-1)
+ prefix(midpoint -> R)
```

Hai phần disjoint nên không cần idempotence.

tiền xử lý vẫn khoảng `O(n log n)`, truy vấn `O(1)`.

DST phức tạp hơn và constants lớn hơn; dùng khi tĩnh có tính kết hợp (associative) các truy vấn thật sự cần extreme truy vấn speed.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **bảng thưa vs tổng tiền tố** tiếp nhận điểm tựa từ **Disjoint bảng thưa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bảng thưa vs cây đoạn (Segment Tree)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bảng thưa vs tổng tiền tố

tĩnh sum:

```text
Prefix Sum:
preprocess O(n)
query O(1)
memory O(n)
```

bảng thưa không thắng.

tĩnh min/max/GCD:

```text
Prefix Sum không áp dụng
Sparse Table:
preprocess O(n log n)
query O(1)
```

cấu trúc dữ liệu phải match algebra của thao tác.

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **bảng thưa vs cây đoạn (Segment Tree)** tiếp nhận điểm tựa từ **bảng thưa vs tổng tiền tố** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bảng thưa vs cây Fenwick (Fenwick Tree)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bảng thưa vs cây đoạn (Segment Tree)

cây đoạn:

```text
preprocess O(n)
query O(log n)
point update O(log n)
range update có thể hỗ trợ lazy
```

bảng thưa:

```text
preprocess O(n log n)
query O(1) với idempotent op
updates rất không phù hợp
```

Nếu có sự thay đổi dữ liệu, cây đoạn thường là choice tự nhiên hơn.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **bảng thưa vs cây Fenwick (Fenwick Tree)** tiếp nhận điểm tựa từ **bảng thưa vs cây đoạn (Segment Tree)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao cập nhật đắt?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bảng thưa vs cây Fenwick (Fenwick Tree)

cây Fenwick tối ưu prefix-like group các thao tác và điểm (point / 지점) các cập nhật:

```text
update O(log n)
prefix/range sum O(log n)
memory O(n)
```

bảng thưa tối ưu tĩnh lũy đẳng (idempotent) các truy vấn.

Hai structures giải khối lượng công việc khác nhau; không nên chọn theo “cái nào advanced hơn”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Vì sao cập nhật đắt?** tiếp nhận điểm tựa từ **bảng thưa vs cây Fenwick (Fenwick Tree)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bộ nhớ bố trí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao cập nhật đắt?

Một cập nhật điểm `a[p]` ảnh hưởng mọi precomputed khối (block / 블록) chứa `p`.

Ở tầng `k`, có thể có nhiều các vị trí bắt đầu `i` sao cho interval `[i,i+2^k)` chứa `p`. Tổng số affected bảng (table / 테이블) các mục không chỉ `O(log n)`.

bảng thưa intentionally các phần tử trùng thông tin để truy vấn nhanh. sự thay đổi dữ liệu phá nhiều copies đó.

Đây là sự đánh đổi giữa **redundant tiền xử lý** và cập nhật chi phí.

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **bộ nhớ bố trí** tiếp nhận điểm tựa từ **Vì sao cập nhật đắt?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bộ nhớ estimation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bộ nhớ bố trí

`st[k][i]` bố trí level-major như Java `int[][]` làm mỗi tầng contiguous lô-gic (logic / 논리) mảng.

truy vấn đọc hai cells cùng tầng. Construction quét sequentially.

Trong C có thể cấp phát flat bộ đệm:

```c
st[k * n + i]
```

để giảm cấp phát overhead.

Java object-per-row overhead thường chấp nhận được, nhưng dataset rất lớn cần estimate bộ nhớ.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **bộ nhớ estimation** tiếp nhận điểm tựa từ **bộ nhớ bố trí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Precomputing logs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bộ nhớ estimation

Với `n = 1,000,000`, các tầng khoảng 20.

Nếu mỗi cell `int` 4 byte:

```text
~20,000,000 ints
~80 MB raw numeric data
```

chưa tính mảng headers/các tham chiếu.

Nếu dùng `long`, raw dữ liệu (data / 데이터) khoảng 160 MB.

Đây là lý do bảng thưa không “free” chỉ vì truy vấn nhanh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Precomputing logs** tiếp nhận điểm tựa từ **bộ nhớ estimation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **rỗng mảng và không hợp lệ phạm vi (range / 범위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Precomputing logs

`log2[len]` mảng tốn `O(n)` thêm bộ nhớ.

Alternative có thể dùng integer bit thao tác:

Java:

```java
int k = 31 - Integer.numberOfLeadingZeros(len);
```

JavaScript:

```js
const k = 31 - Math.clz32(len);
```

nhưng `Math.clz32` có 32-bit ngữ nghĩa. Với very large lengths, cách biểu diễn khác cần cân nhắc.

Choice là readability vs small bộ nhớ saving/môi trường chạy (runtime) detail.

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **rỗng mảng và không hợp lệ phạm vi (range / 범위)** tiếp nhận điểm tựa từ **Precomputing logs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Inclusive vs half-open intervals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## rỗng mảng và không hợp lệ phạm vi (range / 범위)

Trong hệ thống thực tế, API phải định nghĩa:

```text
n = 0 xử lý thế nào?
L > R thì sao?
range out of bounds?
```

Competitive-programming cách triển khai thường assume hợp lệ đầu vào; reusable thư viện (library / 라이브러리) không nên.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Inclusive vs half-open intervals** tiếp nhận điểm tựa từ **rỗng mảng và không hợp lệ phạm vi (range / 범위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RMQ — Truy vấn cực tiểu trên khoảng (Range Minimum Query)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inclusive vs half-open intervals

bảng thưa examples thường dùng inclusive `[L,R]`, nhưng các hệ thống/codebase có thể prefer half-open `[L,R)`.

Half-open length:

```text
len = R - L
```

và right khối (block / 블록) starts at:

```text
R - 2^k
```

Hãy chọn một convention và giữ nhất quán. Mixing interval ngữ nghĩa là nguồn off-by-one phổ biến.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **RMQ — Truy vấn cực tiểu trên khoảng (Range Minimum Query)** tiếp nhận điểm tựa từ **Inclusive vs half-open intervals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RMQ và LCA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RMQ — Truy vấn cực tiểu trên khoảng (Range Minimum Query)

RMQ là một foundational bài toán (problem / 문제):

```text
query(L,R) = minimum value/index trên interval
```

bảng thưa cho tĩnh RMQ `O(1)` sau `O(n log n)` preprocess.

Nhưng RMQ còn có deeper các thuật toán đạt tuyến tính (linear / 선형) tiền xử lý + O(1) truy vấn bằng Cartesian cây/LCA reductions. Đây là chủ đề lý thuyết nâng cao hơn.

bảng thưa nổi bật vì cách triển khai đơn giản và constants practical.

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **RMQ và LCA** tiếp nhận điểm tựa từ **RMQ — Truy vấn cực tiểu trên khoảng (Range Minimum Query)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cartesian cây liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RMQ và LCA

Lowest Phổ biến tổ tiên trên tĩnh cây có thể reduce thành RMQ.

DFS Euler tour ghi chuỗi (sequence / 시퀀스) các nút và depths:

```text
node:  A B D B E B A C ...
depth: 0 1 2 1 2 1 0 1 ...
```

LCA của `u,v` là nút có minimum độ sâu giữa lần xuất hiện phù hợp của chúng trong Euler tour interval.

chuỗi xử lý:

```text
Tree
→ Euler tour
→ depth array
→ RMQ
→ Sparse Table
→ O(1) LCA query
```

Đây là example tuyệt đẹp của bài toán (problem / 문제) phép biến đổi.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, sau nội dung của **RMQ và LCA**, **Cartesian cây liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **tĩnh lũy đẳng (idempotent) truy vấn như semilattice intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cartesian cây liên kết (connection / 연결)

Cartesian cây (tree / 트리) của mảng duy trì tính chất vùng nhớ động (heap / 힙) theo giá trị và thứ tự inorder theo các chỉ số ban đầu.

RMQ giữa hai vị trí có liên hệ với LCA của hai nút tương ứng trong Cartesian cây (tree / 트리).

Vì vậy RMQ, Cartesian cây và LCA có equivalence sâu về cấu trúc (structure / 구조).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **tĩnh lũy đẳng (idempotent) truy vấn như semilattice intuition** tiếp nhận điểm tựa từ **Cartesian cây liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2D bảng thưa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tĩnh lũy đẳng (idempotent) truy vấn như semilattice intuition

Min/max/GCD có algebraic các tính chất phù hợp: có tính kết hợp (associative) + lũy đẳng (idempotent).

Không cần học lattice lý thuyết (theory / 이론) để dùng cấu trúc (structure / 구조), nhưng biết algebra giúp chọn cấu trúc dữ liệu đúng hơn:

```text
operation properties
→ decomposition strategy
→ query structure
```

Đây là tư duy tổng quát có ích cho cây đoạn monoid, Fenwick group-like prefix difference và bảng thưa idempotence.

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **2D bảng thưa** tiếp nhận điểm tựa từ **tĩnh lũy đẳng (idempotent) truy vấn như semilattice intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bảng thưa trên strings/các đối tượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2D bảng thưa

Với truy vấn cực tiểu 2D trên dữ liệu tĩnh, Sparse bảng (table / 테이블) có thể được mở rộng theo hai chiều:

```text
st[kx][ky][x][y]
```

bộ nhớ/tiền xử lý tăng mạnh khoảng `O(nm log n log m)`.

truy vấn rectangle có thể kết hợp bốn blocks nếu thao tác lũy đẳng (idempotent).

Practical only khi dimensions vừa phải và truy vấn volume rất lớn.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **bảng thưa trên strings/các đối tượng** tiếp nhận điểm tựa từ **2D bảng thưa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **quy tắc phân xử khi bằng nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bảng thưa trên strings/các đối tượng

Cấu trúc (structure / 구조) không bắt buộc numeric nếu kết hợp thao tác xác định và bảng (table / 테이블) lưu trữ feasible.

Ví dụ có thể lưu chỉ số của phần tử nhỏ nhất theo một bộ so sánh tùy biến thay vì lưu trực tiếp giá trị. Cách này hữu ích khi cần trả về vị trí ban đầu.

Store chỉ mục (index / 인덱스):

```text
st[k][i] = index của best element trong block
```

kết hợp compares `a[idx1]` và `a[idx2]`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **quy tắc phân xử khi bằng nhau** tiếp nhận điểm tựa từ **bảng thưa trên strings/các đối tượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ngoại tuyến các truy vấn vs bảng thưa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## quy tắc phân xử khi bằng nhau

Nếu truy vấn cực tiểu trên khoảng cần trả chỉ số sớm nhất khi nhiều giá trị bằng nhau, bộ so sánh phải định nghĩa rõ quy tắc phân xử:

```text
smaller value wins
if equal, smaller index wins
```

Tie ngữ nghĩa phải được encoded trong `combine`. Otherwise giá trị đúng nhưng chỉ mục (index / 인덱스) kết quả có thể không đúng specification.

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **ngoại tuyến các truy vấn vs bảng thưa** tiếp nhận điểm tựa từ **quy tắc phân xử khi bằng nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mo's thuật toán khác gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ngoại tuyến các truy vấn vs bảng thưa

Nếu tất cả các truy vấn biết trước, có thể có ngoại tuyến các thuật toán khác mạnh hơn.

Ví dụ tĩnh RMQ ngoại tuyến có Tarjan LCA-like reductions hoặc Mo's thuật toán cho truy vấn classes khác.

bảng thưa phù hợp khi muốn trực tuyến truy vấn sau one-time preprocess và dữ liệu (data / 데이터) tĩnh.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Mo's thuật toán khác gì?** tiếp nhận điểm tựa từ **ngoại tuyến các truy vấn vs bảng thưa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **truy vấn volume và break-even** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mo's thuật toán khác gì?

Mo's thuật toán reorder ngoại tuyến các truy vấn khoảng để minimize ranh giới movement. Nó hữu ích khi:

```text
add/remove element khỏi current range rẻ
operation không có simple prefix/segment structure
```

Độ phức tạp (complexity / 복잡도) thường khoảng `O((n+q)sqrt(n))` style tùy variant.

bảng thưa là preprocessing-based trực tuyến O(1) cho thao tác lớp (class / 클래스) hẹp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **truy vấn volume và break-even** tiếp nhận điểm tựa từ **Mo's thuật toán khác gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bộ nhớ đệm hành vi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## truy vấn volume và break-even

bảng thưa preprocess `O(n log n)` chỉ đáng giá nếu q lớn hoặc độ trễ (latency / 지연 시간) per truy vấn rất quan trọng.

Nếu chỉ vài RMQ các truy vấn, cây đoạn hoặc even quét có thể đủ tùy n.

DSA choice nên nhìn total vòng đời (lifecycle / 생명주기) chi phí:

\[
preprocess + q\times truy vấn + các cập nhật\times cập nhật
\]

không chỉ fastest truy vấn độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **bộ nhớ đệm hành vi** tiếp nhận điểm tựa từ **truy vấn volume và break-even** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **JavaScript cách triển khai caveat** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bộ nhớ đệm hành vi

truy vấn classic bảng thưa đọc hai positions. Rất ít bộ nhớ accesses, tốt cho độ trễ nhưng bảng (table / 테이블) lớn có thể vượt bộ nhớ đệm.

tiền xử lý quét các tầng sequentially, khá thân thiện với bộ nhớ đệm.

cây đoạn truy vấn chạm logarithmic các nút có mẫu nhảy hơn.

Actual hiệu năng phụ thuộc n và phân cấp bộ nhớ.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **JavaScript cách triển khai caveat** tiếp nhận điểm tựa từ **bộ nhớ đệm hành vi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **C cách triển khai caveat** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## JavaScript cách triển khai caveat

Một `Array<Array<number>>` rất tiện nhưng bộ nhớ overhead có thể lớn. Typed các mảng:

```js
const st = Array.from({length: levels}, () => new Int32Array(n));
```

gọn hơn nếu miền giá trị số fit 32-bit.

Nếu các giá trị vượt phạm vi (range / 범위), `Float64Array` hoặc BigInt cách biểu diễn cần cân nhắc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **C cách triển khai caveat** tiếp nhận điểm tựa từ **JavaScript cách triển khai caveat** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## C cách triển khai caveat

Nếu `1 << k` dùng `int` có dấu, phép dịch lớn có thể gây tràn hoặc rơi vào trường hợp hành vi không xác định tùy ngữ cảnh. Nên dùng kiểu không dấu hoặc kiểu kích thước phù hợp và bảo đảm `k` nằm trong độ rộng kiểu dữ liệu.

cấp phát bộ nhớ `levels * n * sizeof(T)` cũng cần tràn số check cho general-purpose thư viện (library / 라이브러리).

> **Chuyển mạch:** Trong **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **C cách triển khai caveat** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

“bảng thưa dùng cho mọi truy vấn khoảng” — sai; strength chính là tĩnh dữ liệu (data / 데이터) và thao tác các tính chất phù hợp.

“Chỉ cần tính kết hợp là đủ để truy vấn `O(1)`” — sai với phương pháp các khối chồng lấn kinh điển; tính lũy đẳng mới cho phép hai khối truy vấn chồng lên nhau.

“cập nhật chỉ sửa O(log n) cells vì có log các tầng” — sai; một điểm (point / 지점) thuộc nhiều intervals ở each tầng.

“bảng thưa luôn tốt hơn cây đoạn vì O(1)” — bỏ qua tiền xử lý, bộ nhớ và sự thay đổi dữ liệu.

“Sum dùng hai khối (block / 블록) như min” — sai vì overlap double-count.

> **Chuyển mạch:** Ở chặng này của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **kiểm thử** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kiểm thử

ngẫu nhiên hóa differential kiểm thử (test / 테스트) rất đơn giản:

```text
generate random array nhỏ
build sparse table
for random L,R:
    expected = scan range
    actual = sparse query
    compare
```

Kiểm thử (test / 테스트) đặc biệt:

```text
length 1
range toàn array
power-of-two length
length ngay trên power-of-two
all values equal
duplicates/ties
negative values
```

Nếu lưu chỉ mục (index / 인덱스), kiểm thử (test / 테스트) quy tắc phân xử khi bằng nhau separately.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **bảng thưa (Sparse Table) và tĩnh các truy vấn khoảng (range queries)**, **Mô hình tư duy** gom các mảnh từ **kiểm thử** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> bảng thưa là **memoization cho mọi interval power-of-two của dữ liệu tĩnh**. Với lũy đẳng (idempotent) thao tác, một arbitrary phạm vi (range / 범위) được cover bởi hai possibly-các khối chồng lấn nên truy vấn chỉ cần hai bảng (table / 테이블) reads. truy vấn cực nhanh được mua bằng redundant tiền xử lý và bộ nhớ, vì vậy cấu trúc (structure / 구조) này chỉ hợp khối lượng công việc ít/no các cập nhật và nhiều lặp lại các truy vấn.

Khi gặp range-truy vấn bài toán (problem / 문제), hãy hỏi:

```text
Data có update không?
Operation associative không?
Operation idempotent không?
Query volume lớn tới mức nào?
Prefix Sum/Fenwick/Segment Tree đơn giản hơn không?
Memory O(n log n) có acceptable không?
Need online hay offline queries?
```

Xem thêm: [Range Queries — Fenwick & Segment Tree](./01_range_queries_fenwick_segment_tree.md), [Tree Foundations — LCA](../02_trees/00_tree_foundations.md), [Bit Manipulation](./02_bit_manipulation_and_bitsets.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
