# Bit Manipulation và Bitsets
**Thao tác bit và tập bit (Bit Manipulation & Bitsets / 비트 연산과 비트셋)**

Bit manipulation khai thác representation nhị phân của integer để biểu diễn flags, subsets, masks và trạng thái compact. Nó thường được dạy như một danh sách tricks (`x & -x`, `x & (x-1)`, XOR...), nhưng cách học đó dễ quên và dễ dùng sai.

Cách hiểu bền hơn là:

> Bitwise operation là các phép toán trên **nhiều boolean positions cùng lúc**. Mỗi bit là một biến nhị phân; integer chỉ là container đóng gói chúng.

## Mental Model

Nếu ta có `k` boolean flags:

```text
f0, f1, f2, ..., fk-1
```

thay vì lưu từng boolean riêng, ta có thể encode:

\[
mask = \sum_{i=0}^{k-1} f_i 2^i
\]

Bit `i = 1` nghĩa flag `i` đang bật.

Hardware có thể AND/OR/XOR cả machine word trong một instruction, nên bitset tạo **word-level parallelism** tự nhiên.

## Các phép cơ bản

```text
&   AND
|   OR
^   XOR
~   NOT
<<  left shift
>>  right shift
```

Với bit mask `1 << k`:

### Kiểm tra bit

```c
if (x & (1u << k)) {
    // bit k đang bật
}
```

### Set bit

```c
x |= (1u << k);
```

### Clear bit

```c
x &= ~(1u << k);
```

### Toggle bit

```c
x ^= (1u << k);
```

Điểm quan trọng là type/width. `1 << k` dùng type của literal `1`; nếu cần shift tới bit cao của 64-bit value trong C/Java, dùng literal phù hợp như `1ULL << k` hoặc `1L << k`.

## AND, OR, XOR như set operations

Nếu mỗi bit đại diện một element trong universe nhỏ:

```text
A & B -> intersection
A | B -> union
A ^ B -> symmetric difference
A & ~B -> A \ B
```

Đây là lý do bitsets rất mạnh cho graph/set algorithms: một machine word có thể xử lý 64 memberships cùng lúc.

## XOR algebra

XOR có properties:

\[
x \oplus x = 0
\]

\[
x \oplus 0 = x
\]

\[
x \oplus y = y \oplus x
\]

và associative.

Nếu mọi number xuất hiện đúng hai lần trừ một number xuất hiện một lần:

```text
x ^ x = 0
```

làm các pairs triệt tiêu, để lại unique value.

Điều này không phải magic trick; constraints của problem khớp chính xác algebra của XOR.

Nếu có ba lần, hoặc nhiều unique values, cùng trick không còn đủ information.

## Two's Complement

Signed integers thường dùng **two's complement (2의 보수)** representation.

Trong fixed width:

\[
-x = \sim x + 1
\]

Đây là cơ sở của nhiều bit identities, nhưng language semantics vẫn phải được tôn trọng.

## Least Significant Set Bit

Expression:

```text
x & -x
```

isolate bit 1 thấp nhất.

Ví dụ:

```text
x    = 1011000₂
-x   = 0101000₂  (conceptual low bits)
AND  = 0001000₂
```

Fenwick tree dùng value này làm block size.

Mental reason: `-x` giữ bit 1 thấp nhất của `x` và đảo pattern phía trên theo two's-complement carry, nên AND chỉ còn bit đó.

## Xóa bit 1 thấp nhất

```text
x & (x - 1)
```

clear least significant set bit.

Tại sao? Trừ 1 biến lowest `1` thành `0` và các zeros thấp hơn thành `1`; AND với original x xóa đúng lowest set bit.

Brian Kernighan popcount:

```c
int count = 0;
while (x) {
    x &= x - 1;
    count++;
}
```

Số iterations bằng số set bits, không phải bit width.

Trong production, ưu tiên compiler/library intrinsic như `Integer.bitCount`, `Long.bitCount`, `std::popcount` nếu available vì có thể map tới hardware POPCNT.

## Kiểm tra power of two

Positive integer `x` là power of two nếu chỉ có một set bit:

```text
x > 0 && (x & (x - 1)) == 0
```

Phải có `x > 0`; zero cũng thỏa expression thứ hai nhưng không phải power of two.

Đây là ví dụ constraints nhỏ làm bit trick đúng hay sai.

## Bitmask subset representation

Với `n` nhỏ, mask từ `0` tới `2^n - 1` biểu diễn mọi subset.

Bit `i` bật nghĩa item `i` được chọn.

```c
for (unsigned mask = 0; mask < (1u << n); ++mask) {
    for (int i = 0; i < n; ++i) {
        if (mask & (1u << i)) {
            // item i belongs to subset
        }
    }
}
```

Bitmask không biến exponential problem thành polynomial. Nó chỉ encode state gọn và làm membership operation rẻ.

Nếu cần enumerate `2^n` subsets, output/search space vẫn exponential.

## Enumerating submasks

Muốn iterate mọi non-empty submask của `mask`:

```c
for (unsigned sub = mask; sub; sub = (sub - 1) & mask) {
    // use sub
}
```

`sub - 1` thay đổi suffix bits; AND với original `mask` ép result chỉ chứa allowed bits.

Pattern này đi qua submasks theo descending numeric order.

Muốn include empty submask, xử lý `0` riêng hoặc dùng loop có break rõ ràng để tránh unsigned underflow loop.

## Vì sao tổng `(mask, submask)` pairs là `3^n`?

Xét mỗi bit độc lập. Một bit có ba trạng thái:

```text
không thuộc mask
thuộc mask nhưng không thuộc submask
thuộc cả mask và submask
```

Vậy tổng combinations:

\[
3^n
\]

Đây là lý do nested loop over masks and submasks thường `O(3^n)`, không phải `O(4^n)` nếu structure đúng.

## Superset enumeration

Nếu universe mask có `n` bits và cần enumerate supersets của `mask`, có thể enumerate submasks của complement rồi OR lại, hoặc dùng transformed loops tùy problem.

Mental model tốt hơn memorizing syntax là: tách **fixed required bits** và **free bits**.

## Gray Code

**Gray code (그레이 코드)** sắp `2^n` bit patterns sao cho hai consecutive values khác đúng một bit.

Binary-reflected Gray code:

\[
g(i)=i\oplus(i>>1)
\]

Useful khi chuyển state mà chỉ muốn một bit thay đổi mỗi bước, hardware encoders, combinatorial generation và một số DP/enumeration optimizations.

## Bitmask Dynamic Programming

Nếu state phụ thuộc subset nhỏ `n`, DP có thể dùng:

```text
dp[mask]
```

Ví dụ Traveling Salesman exact DP:

```text
dp[mask][v] = minimum cost đi qua set mask và kết thúc tại v
```

State count:

\[
O(2^n n)
\]

Transitions có thể đưa total tới `O(2^n n^2)`.

Bitmask làm state identity compact; nó không loại exponential dependence vào `n`.

## SOS DP / Subset DP

Nhiều problems cần tổng function trên mọi submask:

\[
g[mask] = \sum_{sub \subseteq mask} f[sub]
\]

Naive iterate all mask-submask pairs `O(3^n)`. **Sum Over Subsets DP (SOS DP)** có thể làm:

\[
O(n2^n)
\]

bằng cách lần lượt cho phép từng bit đóng góp.

Đây là một example mạnh nơi binary representation định nghĩa dimensions của DP state.

## Bitset là gì?

Nếu universe có nhiều hơn machine-word bits, dùng array of words:

```text
word 0 -> bits 0..63
word 1 -> bits 64..127
...
```

Membership:

```text
word = index / 64
bit  = index % 64
```

Set operations chạy word-by-word.

Nếu universe có 6400 elements, intersection cần khoảng 100 64-bit AND operations thay vì kiểm 6400 booleans riêng lẻ.

## Java BitSet

Java cung cấp `java.util.BitSet`:

```java
BitSet a = new BitSet();
a.set(3);
a.set(100);

BitSet b = new BitSet();
b.set(100);
b.set(200);

a.and(b);
```

`BitSet` tự quản word array và có methods `and`, `or`, `xor`, `nextSetBit`, `cardinality`.

Nếu cần fixed-size dense flags, `BitSet` thường memory-efficient hơn `HashSet<Integer>` rất nhiều.

## JavaScript bitwise operators chỉ 32-bit

Đây là pitfall rất quan trọng.

JavaScript `Number` là floating-point double, nhưng bitwise operators truyền thống convert operand sang signed 32-bit integer.

```js
1 << 31
```

có signed 32-bit semantics; shift count cũng modulo 32 theo operator rules.

Không thể dùng Number bitwise operators cho arbitrary 53-bit masks như thể chúng là 64-bit integers.

## BigInt bitmasks trong JavaScript

`BigInt` có bitwise operators riêng:

```js
let mask = 0n;
mask |= 1n << 60n;
```

Nhưng không được mix `Number` và `BigInt` trực tiếp:

```js
1n + 1 // TypeError
```

BigInt phù hợp mask lớn nhưng performance/cost model khác typed-array bitsets.

Nếu universe hàng nghìn bits và operations bulk, `Uint32Array`/custom word bitset có thể thực dụng hơn một giant BigInt tùy engine/workload.

## Java shift semantics

Java có:

```text
>>   arithmetic right shift: fill sign bit
>>>  logical right shift: fill zero
```

Ví dụ negative integer:

```java
int x = -8;
System.out.println(x >> 1);  // vẫn negative
System.out.println(x >>> 1); // large positive
```

Shift distance của `int` chỉ dùng low 5 bits; của `long` dùng low 6 bits. Vì vậy shift >= width không có semantics giống toán học naïve.

## C shift caveats

C bit shifting signed values có nhiều corner cases. Left shift làm overflow signed range có thể dẫn tới undefined behavior; right shift negative signed value historically có implementation-defined aspects theo standard/version context.

Khi thao tác raw bits, unsigned integer types thường an toàn hơn:

```c
uint32_t
uint64_t
```

và constants nên có unsigned/wide suffix phù hợp.

## Endianness không phải bit numbering trong integer

Bit operations trên integer value thường độc lập với memory endianness. `x & 1` kiểm least significant bit của numeric value dù bytes được lưu little-endian hay big-endian.

Endianness trở nên quan trọng khi serialize/interpret multi-byte memory representation, network protocol hoặc cast byte arrays.

Đừng trộn “bit thấp” với “byte nằm ở address thấp”.

## Signed vs Unsigned Interpretation

Cùng bit pattern có thể được diễn giải khác:

```text
11111111₂
```

là 255 nếu unsigned 8-bit, -1 nếu signed two's complement 8-bit.

Bitwise transform làm việc trên pattern; comparison/arithmetic sau đó phụ thuộc signedness.

## Bitboard

Board game nhỏ có thể encode whole board bằng bits. Chess engines dùng **bitboards**: một 64-bit integer cho positions của một loại piece/occupancy.

Move generation có thể dùng shifts, masks và AND để tính nhiều squares đồng thời.

Đây là example word-level parallelism rất thực tế.

## Graph bằng Bitsets

Dense graph nhỏ có thể lưu adjacency row như bitset.

Common neighbors của `u` và `v`:

```text
adj[u] & adj[v]
```

Triangle counting hoặc transitive operations có thể tận dụng hardware word operations.

Floyd-Warshall boolean reachability có thể optimize bằng bitsets: nếu `i` reaches `k`, OR row `k` vào row `i`, giảm constant factor mạnh so với per-vertex boolean loops.

## Bitset DP

Classic subset-sum boolean DP:

```text
possible sums
```

có thể encode bằng bitset `bits`, trong đó bit `s` nghĩa sum `s` reachable.

Với item weight `w`:

```text
bits |= bits << w
```

Một shift+OR xử lý nhiều states cùng lúc.

Trong languages/libraries support efficient arbitrary bitset shift, điều này có thể tăng tốc rất lớn so với nested loops.

## Bloom Filter connection

Bloom filter cũng là bit array, nhưng semantics khác exact bitset membership. Multiple hash functions map keys vào bit positions; query có false positives.

Bitset ở đây là storage primitive, còn Bloom filter là probabilistic data structure xây trên nó.

Xem [Probabilistic Data Structures](./06_probabilistic_data_structures.md).

## Flags và Permissions

Permissions thường encode bit flags:

```text
READ    = 001
WRITE   = 010
EXECUTE = 100
```

Combination:

```text
READ | WRITE = 011
```

Check:

```text
(mask & WRITE) != 0
```

Nếu field là enum flags trong protocol/database, cần document bit assignments ổn định để compatibility không bị phá.

## Bit packing

Nhiều small integers có thể pack trong một word bằng shift + mask.

Ví dụ RGB 8-bit channels:

```text
0xRRGGBB
```

Extract green:

```c
(g >> 8) & 0xFF
```

Packing giảm memory/bandwidth nhưng tăng complexity và coupling vào bit layout. Production serialization còn phải định nghĩa endianness/versioning.

## Mask tạo từ `k` low bits

Nếu muốn mask có `k` bits thấp bằng 1:

```text
(1 << k) - 1
```

nhưng cần cẩn thận khi `k` bằng word width vì shifting by width có semantics nguy hiểm/khác language.

Với fixed-width types, special-case full width hoặc dùng library helper.

## Rotate vs Shift

Shift đẩy bits ra ngoài và fill zeros/sign bits. Rotate chuyển bits bị đẩy ra quay lại đầu kia.

Cryptographic/hash algorithms thường dùng rotate (`rotl`, `rotr`) vì muốn mix bits mà không mất information.

C++20 có `std::rotl`/`std::rotr`; Java có `Integer.rotateLeft/Right` và `Long.rotateLeft/Right`.

Đừng implement rotate bằng shifts mà quên width/signedness edge cases.

## Finding Highest/Lowest Set Bit

Operations như count-leading-zeros (CLZ), count-trailing-zeros (CTZ) và bit length thường có hardware intrinsics.

Examples:

```java
Integer.numberOfLeadingZeros(x)
Integer.numberOfTrailingZeros(x)
Integer.highestOneBit(x)
```

Applications:

```text
log2 floor
next power-of-two allocation
binary lifting
Fenwick/segment internals
bitset scanning
```

Nếu library có intrinsic, dùng nó thay manual loop khi clarity/performance phù hợp.

## Next power of two

Dynamic buffers, hash tables hoặc segment trees đôi khi round capacity lên power of two.

Một approach conceptually:

```text
n > 0
next = 1 << ceil(log2(n))
```

Bit-smearing tricks tồn tại, nhưng library bit-length functions thường rõ và an toàn hơn.

Power-of-two capacity cho phép modulo index bằng mask:

```text
index & (capacity - 1)
```

chỉ khi capacity thực sự là power of two.

## Bit Hacks không nên thay clarity vô điều kiện

Modern compilers tối ưu nhiều patterns. Một obscure trick không tự động nhanh hơn clear code/library intrinsic.

Ví dụ manual popcount hack có thể chậm hơn hardware intrinsic và khó review.

Use bit trick khi nó:

```text
encode mathematical property rõ
reduce asymptotic/state complexity
map tốt tới library/hardware
```

không phải để code trông “low-level”.

## Security considerations

Bitwise code xuất hiện nhiều trong crypto, parsers và protocols. Nhưng custom crypto bit tricks rất dễ tạo side channels hoặc logic bugs.

Constant-time programming là specialized security discipline; branchless bit operations không tự động làm code constant-time vì compiler/runtime/memory behavior còn ảnh hưởng.

Không nên tự thiết kế cryptographic primitive chỉ vì hiểu bitwise operators.

## Common misconceptions

**“Bitmask luôn O(1).”** Chỉ khi state fit trong fixed number machine words. Arbitrary-size bitset operation là `O(number of words)`.

**“Bitwise trong JavaScript dùng toàn bộ 53-bit integer precision.”** Không; Number bitwise operators dùng 32-bit coercion.

**“`x & -x` luôn an toàn cho mọi type.”** Cần hiểu signed width và language overflow semantics.

**“Bit DP làm exponential problem thành fast polynomial.”** State count vẫn `2^n`; bitmask chỉ làm representation compact.

**“Shift giống multiply/divide cho mọi signed value.”** Rounding, overflow và sign-fill có thể khác arithmetic expectation.

**“Bitset = Bloom filter.”** Bitset thường exact flags; Bloom filter thêm hashing và probabilistic false positives.

## Testing Bit Code

Bit bugs thường nằm ở boundaries:

```text
bit 0
highest bit
all-zero mask
all-one mask
negative signed values
shift by 0
shift near/at word width
n = 31/32/63/64
JavaScript >31 bit cases
BigInt/Number conversion
```

Property tests hữu ích:

```text
set rồi clear bit -> original value
x ^ x == 0
popcount(x) == number of enumerated set bits
submask loop chỉ sinh subsets của mask và không duplicate
bitset AND tương đương set intersection reference
```

## Khi nào bit manipulation thật sự đáng dùng?

Bit representation đặc biệt mạnh khi:

```text
universe nhỏ hoặc vừa và dense
state là nhiều boolean flags
subset identity cần hash/index nhanh
word-level batch operations hữu ích
memory bandwidth quan trọng
```

Nếu domain keys sparse, huge hoặc dynamic labels, `HashSet`, sorted set hoặc compressed bitmap có thể phù hợp hơn.

Roaring Bitmap chẳng hạn chia universe thành chunks và chọn representation dense/sparse theo local cardinality; đây là production example vượt qua “plain bitset vs set” bằng hybrid structure.

## Mental Model mở rộng

> Bit manipulation không phải collection của mẹo nhị phân. Nó là **data representation design**: khi state thật sự là boolean vector, binary integer/bitset cho phép memory compact, algebra rõ và hardware xử lý nhiều flags cùng lúc.

Khi dùng bit trick, luôn hỏi ba điều: proof identity đến từ đâu, integer width/signedness của language là gì, và state có thực sự fit model dense boolean vector không. Nếu ba câu này rõ, bitwise code trở thành công cụ có hệ thống thay vì magic.