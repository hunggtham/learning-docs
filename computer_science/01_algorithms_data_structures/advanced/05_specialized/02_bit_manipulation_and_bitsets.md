# thao tác bit và Bitsets

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **thao tác bit và Bitsets**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình tư duy** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **Các phép cơ bản** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Thao tác bit và tập bit (Bit Manipulation & Bitsets / 비트 연산과 비트셋)**

thao tác bit khai thác cách biểu diễn (representation / 표현) nhị phân của integer để biểu diễn flags, subsets, masks và trạng thái gọn. Nó thường được dạy như một danh sách tricks (`x & -x`, `x & (x-1)`, XOR...), nhưng cách học đó dễ quên và dễ dùng sai.

Cách hiểu bền hơn là:

> Bitwise thao tác là các phép toán trên **nhiều boolean positions cùng lúc**. Mỗi bit là một biến nhị phân; integer chỉ là bộ chứa (container / 컨테이너) đóng gói chúng.

## Mô hình tư duy

Nếu ta có `k` boolean flags:

```text
f0, f1, f2, ..., fk-1
```

thay vì lưu từng boolean riêng, ta có thể encode:

\[
mask = \sum_{i=0}^{k-1} f_i 2^i
\]

Bit `i = 1` nghĩa flag `i` đang bật.

Hardware có thể AND/OR/XOR cả machine word trong một instruction, nên tập bit (bitset) tạo **song song ở mức từ máy** tự nhiên.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Các phép cơ bản** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **AND, OR, XOR như set các thao tác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các phép cơ bản

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
&   AND
|   OR
^   XOR
~   NOT
<<  left shift
>>  right shift
```

Với mặt nạ bit `1 << k`:

### Kiểm tra bit

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
if (x & (1u << k)) {
    // bit k đang bật
}
```

### Set bit

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
x |= (1u << k);
```

### Clear bit

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
x &= ~(1u << k);
```

### Toggle bit

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```c
x ^= (1u << k);
```

Điểm quan trọng là kiểu (type / 타입)/width. `1 << k` dùng kiểu (type / 타입) của literal `1`; nếu cần shift tới bit cao của 64-bit giá trị trong C/Java, dùng literal phù hợp như `1ULL << k` hoặc `1L << k`.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **AND, OR, XOR như set các thao tác** tiếp nhận điểm tựa từ **Các phép cơ bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **XOR algebra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AND, OR, XOR như set các thao tác

Nếu mỗi bit đại diện một phần tử trong universe nhỏ:

```text
A & B -> intersection
A | B -> union
A ^ B -> symmetric difference
A & ~B -> A \ B
```

Đây là lý do bitsets rất mạnh cho đồ thị/set các thuật toán: một machine word có thể xử lý 64 memberships cùng lúc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **XOR algebra** tiếp nhận điểm tựa từ **AND, OR, XOR như set các thao tác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Two's Complement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## XOR algebra

XOR có các tính chất:

\[
x \oplus x = 0
\]

\[
x \oplus 0 = x
\]

\[
x \oplus y = y \oplus x
\]

và có tính kết hợp (associative).

Nếu mọi number xuất hiện đúng hai lần trừ một number xuất hiện một lần:

```text
x ^ x = 0
```

làm các pairs triệt tiêu, để lại unique giá trị.

Điều này không phải magic trick; các ràng buộc của bài toán (problem / 문제) khớp chính xác algebra của XOR.

Nếu có ba lần, hoặc nhiều unique các giá trị, cùng trick không còn đủ thông tin.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Two's Complement** tiếp nhận điểm tựa từ **XOR algebra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Least Significant Set Bit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Two's Complement

Signed integers thường dùng **two's complement (2의 보수)** cách biểu diễn.

Trong fixed width:

\[
-x = \sim x + 1
\]

Đây là cơ sở của nhiều bit identities, nhưng ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) vẫn phải được tôn trọng.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **Least Significant Set Bit** tiếp nhận điểm tựa từ **Two's Complement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xóa bit 1 thấp nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

cây Fenwick (Fenwick Tree) dùng giá trị này làm khối (block / 블록) kích thước (size / 크기).

Mental reason: `-x` giữ bit 1 thấp nhất của `x` và đảo mẫu phía trên theo two's-complement carry, nên AND chỉ còn bit đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **Xóa bit 1 thấp nhất** tiếp nhận điểm tựa từ **Least Significant Set Bit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm tra lũy thừa của hai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xóa bit 1 thấp nhất

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

Số iterations bằng số set bits, không phải độ rộng bit.

Trong hệ thống thực tế, ưu tiên trình biên dịch/thư viện (library / 라이브러리) intrinsic như `Integer.bitCount`, `Long.bitCount`, `std::popcount` nếu available vì có thể map tới hardware POPCNT.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Kiểm tra lũy thừa của hai** tiếp nhận điểm tựa từ **Xóa bit 1 thấp nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bitmask subset cách biểu diễn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm tra lũy thừa của hai

Positive integer `x` là lũy thừa của hai nếu chỉ có một set bit:

```text
x > 0 && (x & (x - 1)) == 0
```

Phải có `x > 0`; zero cũng thỏa expression thứ hai nhưng không phải lũy thừa của hai.

Đây là ví dụ các ràng buộc nhỏ làm bit trick đúng hay sai.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **Bitmask subset cách biểu diễn** tiếp nhận điểm tựa từ **Kiểm tra lũy thừa của hai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Enumerating submasks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bitmask subset cách biểu diễn

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

Bitmask không biến exponential bài toán (problem / 문제) thành polynomial. Nó chỉ encode trạng thái (state / 상태) gọn và làm membership thao tác rẻ.

Nếu cần enumerate `2^n` subsets, đầu ra/không gian tìm kiếm vẫn exponential.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **Enumerating submasks** tiếp nhận điểm tựa từ **Bitmask subset cách biểu diễn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao tổng (mask, submask) pairs là 3^n?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Enumerating submasks

Muốn iterate mọi non-empty submask của `mask`:

```c
for (unsigned sub = mask; sub; sub = (sub - 1) & mask) {
    // use sub
}
```

`sub - 1` thay đổi suffix bits; AND với original `mask` ép kết quả chỉ chứa các bit được phép.

mẫu này đi qua submasks theo descending numeric thứ tự (order / 순서).

Muốn include rỗng submask, xử lý `0` riêng hoặc dùng vòng lặp (loop / 루프) có break rõ ràng để tránh unsigned tràn dưới vòng lặp (loop / 루프).

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Vì sao tổng (mask, submask) pairs là 3^n?** tiếp nhận điểm tựa từ **Enumerating submasks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Superset enumeration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Đây là lý do vòng lặp lồng nhau over masks and submasks thường `O(3^n)`, không phải `O(4^n)` nếu cấu trúc (structure / 구조) đúng.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **Superset enumeration** tiếp nhận điểm tựa từ **Vì sao tổng (mask, submask) pairs là 3^n?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gray mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Superset enumeration

Nếu mặt nạ toàn miền có `n` bit và cần liệt kê các siêu tập của `mask`, có thể liệt kê các mặt nạ con của phần bù rồi OR trở lại, hoặc dùng vòng lặp biến đổi phù hợp với bài toán.

Mô hình tư duy tốt hơn memorizing cú pháp (syntax / 문법) là: tách **các bit bắt buộc cố định** và **các bit tự do**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **Gray mã (code / 코드)** tiếp nhận điểm tựa từ **Superset enumeration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bitmask quy hoạch động (dynamic programming)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gray mã (code / 코드)

**Gray mã (code / 코드)** sắp `2^n` bit các mẫu sao cho hai consecutive các giá trị khác đúng một bit.

Binary-reflected Gray mã (code / 코드):

\[
g(i)=i\oplus(i>>1)
\]

Hữu ích khi chuyển trạng thái mà chỉ muốn một bit thay đổi mỗi bước, hardware encoders, combinatorial generation và một số DP/enumeration optimizations.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Bitmask quy hoạch động (dynamic programming)** tiếp nhận điểm tựa từ **Gray mã (code / 코드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SOS DP / Subset DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bitmask quy hoạch động (dynamic programming)

Nếu trạng thái phụ thuộc subset nhỏ `n`, DP có thể dùng:

```text
dp[mask]
```

Ví dụ Traveling Salesman chính xác DP:

```text
dp[mask][v] = minimum cost đi qua set mask và kết thúc tại v
```

trạng thái count:

\[
O(2^n n)
\]

Transitions có thể đưa total tới `O(2^n n^2)`.

Bitmask làm trạng thái định danh (identity / 식별자) gọn; nó không loại exponential dependence vào `n`.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **SOS DP / Subset DP** tiếp nhận điểm tựa từ **Bitmask quy hoạch động (dynamic programming)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **tập bit là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SOS DP / Subset DP

Nhiều problems cần tổng hàm trên mọi submask:

\[
g[mask] = \sum_{sub \subseteq mask} f[sub]
\]

Cách đơn giản duyệt mọi cặp mặt nạ–mặt nạ con có độ phức tạp `O(3^n)`. **Sum Over Subsets DP (SOS DP)** có thể giảm độ phức tạp bằng cách tái sử dụng các tổng trung gian:

\[
O(n2^n)
\]

bằng cách lần lượt cho phép từng bit đóng góp.

Đây là một example mạnh nơi nhị phân (binary / 이진) cách biểu diễn định nghĩa dimensions của DP trạng thái.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **tập bit là gì?** tiếp nhận điểm tựa từ **SOS DP / Subset DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java tập bit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tập bit là gì?

Nếu universe có nhiều hơn machine-word bits, dùng mảng of words:

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

Set các thao tác chạy word-by-word.

Nếu universe có 6400 các phần tử, intersection cần khoảng 100 64-bit AND các thao tác thay vì kiểm 6400 booleans riêng lẻ.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Java tập bit** tiếp nhận điểm tựa từ **tập bit là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **JavaScript bitwise operators chỉ 32-bit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java tập bit

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

`BitSet` tự quản word mảng và có methods `and`, `or`, `xor`, `nextSetBit`, `cardinality`.

Nếu cần tập cờ dày đặc có kích thước cố định, `BitSet` thường tiết kiệm bộ nhớ hơn `HashSet<Integer>` rất nhiều.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **JavaScript bitwise operators chỉ 32-bit** tiếp nhận điểm tựa từ **Java tập bit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BigInt bitmasks trong JavaScript** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## JavaScript bitwise operators chỉ 32-bit

Đây là pitfall rất quan trọng.

JavaScript `Number` là số dấu phẩy động độ chính xác kép, nhưng các toán tử bit truyền thống chuyển toán hạng sang số nguyên có dấu 32 bit.

```js
1 << 31
```

Các phép toán này sử dụng ngữ nghĩa số nguyên có dấu 32 bit; số lượng bit dịch cũng được lấy modulo 32 theo quy tắc của toán tử.

Không thể dùng toán tử bit trên `Number` cho các mặt nạ 53 bit tùy ý như thể chúng là số nguyên 64 bit.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **BigInt bitmasks trong JavaScript** tiếp nhận điểm tựa từ **JavaScript bitwise operators chỉ 32-bit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java shift ngữ nghĩa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

BigInt phù hợp mask lớn nhưng hiệu năng/mô hình chi phí khác typed-array bitsets.

Nếu universe hàng nghìn bits và các thao tác bulk, `Uint32Array`/custom word tập bit có thể thực dụng hơn một giant BigInt tùy engine/khối lượng công việc.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Java shift ngữ nghĩa** tiếp nhận điểm tựa từ **BigInt bitmasks trong JavaScript** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **C shift caveats** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java shift ngữ nghĩa

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

Shift khoảng cách của `int` chỉ dùng low 5 bits; của `long` dùng low 6 bits. Vì vậy shift >= width không có ngữ nghĩa giống toán học naïve.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **C shift caveats** tiếp nhận điểm tựa từ **Java shift ngữ nghĩa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Endianness không phải bit numbering trong integer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## C shift caveats

Dịch bit trên giá trị có dấu trong C có nhiều trường hợp biên (corner cases). Dịch trái làm vượt miền số có dấu có thể dẫn tới hành vi không xác định; dịch phải một giá trị âm từng có những chi tiết phụ thuộc cách triển khai tùy chuẩn và phiên bản.

Khi thao tác các bit thô, unsigned integer types thường an toàn hơn:

```c
uint32_t
uint64_t
```

và constants nên có unsigned/wide suffix phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **Endianness không phải bit numbering trong integer** tiếp nhận điểm tựa từ **C shift caveats** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Signed vs Unsigned Interpretation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Endianness không phải bit numbering trong integer

Bit các thao tác trên integer giá trị thường độc lập với bộ nhớ endianness. `x & 1` kiểm least significant bit của numeric giá trị dù byte được lưu little-endian hay big-endian.

Endianness trở nên quan trọng khi serialize/interpret multi-byte bộ nhớ cách biểu diễn, mạng giao thức (protocol / 프로토콜) hoặc cast byte các mảng.

Đừng trộn “bit thấp” với “byte nằm ở address thấp”.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Signed vs Unsigned Interpretation** tiếp nhận điểm tựa từ **Endianness không phải bit numbering trong integer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bitboard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Signed vs Unsigned Interpretation

Cùng bit mẫu có thể được diễn giải khác:

```text
11111111₂
```

là 255 nếu unsigned 8-bit, -1 nếu signed two's complement 8-bit.

Bitwise transform làm việc trên mẫu; phép so sánh/arithmetic sau đó phụ thuộc signedness.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **Bitboard** tiếp nhận điểm tựa từ **Signed vs Unsigned Interpretation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **đồ thị bằng Bitsets** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bitboard

Bàn cờ nhỏ có thể mã hóa toàn bộ trạng thái bằng bit. Chess engines dùng **bàn cờ dạng bit**: một 64-bit integer cho positions của một loại piece/occupancy.

Move generation có thể dùng shifts, masks và AND để tính nhiều squares đồng thời.

Đây là example song song ở mức từ máy rất thực tế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **đồ thị bằng Bitsets** tiếp nhận điểm tựa từ **Bitboard** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **tập bit DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## đồ thị bằng Bitsets

đồ thị dày nhỏ có thể lưu adjacency row như tập bit.

Phổ biến các đỉnh kề của `u` và `v`:

```text
adj[u] & adj[v]
```

Đếm tam giác hoặc các phép toán liên quan tới bao đóng bắc cầu có thể tận dụng thao tác trên cả từ máy của phần cứng.

Bài toán khả đạt Boolean kiểu Floyd–Warshall có thể được tối ưu bằng bitset: nếu `i` reaches `k`, OR row `k` vào row `i`, giảm constant factor mạnh so với per-vertex boolean loops.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **tập bit DP** tiếp nhận điểm tựa từ **đồ thị bằng Bitsets** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bộ lọc Bloom liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tập bit DP

Kinh điển subset-sum boolean DP:

```text
possible sums
```

có thể encode bằng tập bit `bits`, trong đó bit `s` nghĩa sum `s` có thể tới.

Với item trọng số `w`:

```text
bits |= bits << w
```

Một shift+OR xử lý nhiều các trạng thái cùng lúc.

Trong languages/libraries hỗ trợ (support / 지원) efficient arbitrary tập bit shift, điều này có thể tăng tốc rất lớn so với các vòng lặp lồng nhau.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, sau nội dung của **tập bit DP**, **bộ lọc Bloom liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Flags và Permissions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## bộ lọc Bloom liên kết (connection / 연결)

bộ lọc Bloom cũng là bit mảng, nhưng ngữ nghĩa khác chính xác tập bit membership. Multiple các hàm băm map các khóa vào bit positions; truy vấn có các dương tính giả.

tập bit ở đây là lưu trữ thành phần nguyên thủy (primitive / 기본 요소), còn bộ lọc Bloom là cấu trúc dữ liệu xác suất xây trên nó.

Xem [Probabilistic Data Structures](./06_probabilistic_data_structures.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **Flags và Permissions** tiếp nhận điểm tựa từ **bộ lọc Bloom liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bit packing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Nếu trường là enum flags trong giao thức (protocol / 프로토콜)/cơ sở dữ liệu, cần document bit assignments ổn định để tính tương thích (compatibility / 호환성) không bị phá.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Bit packing** tiếp nhận điểm tựa từ **Flags và Permissions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mask tạo từ k các bit thấp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bit packing

Nhiều số nguyên nhỏ có thể được đóng gói trong một từ máy bằng phép dịch bit và mặt nạ.

Ví dụ RGB 8-bit channels:

```text
0xRRGGBB
```

Extract green:

```c
(g >> 8) & 0xFF
```

Packing giảm bộ nhớ/bandwidth nhưng tăng độ phức tạp (complexity / 복잡도) và coupling vào bit bố trí. Trong hệ thống thực tế, serialization còn phải định nghĩa endianness/versioning.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **Mask tạo từ k các bit thấp** tiếp nhận điểm tựa từ **Bit packing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rotate vs Shift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mask tạo từ `k` các bit thấp

Nếu muốn mask có `k` bits thấp bằng 1:

```text
(1 << k) - 1
```

Tuy nhiên cần cẩn thận khi `k` bằng đúng độ rộng từ máy, vì dịch bit một lượng bằng độ rộng kiểu dữ liệu có ngữ nghĩa nguy hiểm hoặc khác nhau giữa các ngôn ngữ.

Với độ rộng cố định types, special-case full width hoặc dùng thư viện (library / 라이브러리) helper.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **Rotate vs Shift** tiếp nhận điểm tựa từ **Mask tạo từ k các bit thấp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Finding Highest/Lowest Set Bit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rotate vs Shift

Phép dịch đẩy các bit ra ngoài và điền bit 0 hoặc bit dấu; phép xoay đưa các bit bị đẩy ra quay lại đầu bên kia.

Cryptographic/băm (hash / 해시) các thuật toán thường dùng rotate (`rotl`, `rotr`) vì muốn mix bits mà không mất thông tin.

C++20 có `std::rotl`/`std::rotr`; Java có `Integer.rotateLeft/Right` và `Long.rotateLeft/Right`.

Đừng implement rotate bằng shifts mà quên width/signedness các trường hợp biên (edge cases).

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Finding Highest/Lowest Set Bit** tiếp nhận điểm tựa từ **Rotate vs Shift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Next lũy thừa của hai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Finding Highest/Lowest Set Bit

các thao tác như đếm số bit 0 đầu (CLZ), đếm số bit 0 cuối (CTZ) và bit length thường có hardware intrinsics.

Examples:

```java
Integer.numberOfLeadingZeros(x)
Integer.numberOfTrailingZeros(x)
Integer.highestOneBit(x)
```

các ứng dụng:

```text
log2 floor
next power-of-two allocation
binary lifting
Fenwick/segment internals
bitset scanning
```

Nếu thư viện có intrinsic phù hợp, nên dùng nó thay cho vòng lặp viết tay khi điều đó cải thiện độ rõ ràng hoặc hiệu năng.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **Next lũy thừa của hai** tiếp nhận điểm tựa từ **Finding Highest/Lowest Set Bit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bit Hacks không nên thay clarity vô điều kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Next lũy thừa của hai

động các bộ đệm, băm (hash / 해시) tables hoặc segment các cây đôi khi round sức chứa (capacity / 용량) lên lũy thừa của hai.

Một approach conceptually:

```text
n > 0
next = 1 << ceil(log2(n))
```

Bit-smearing tricks tồn tại, nhưng thư viện (library / 라이브러리) bit-length các hàm thường rõ và an toàn hơn.

Power-of-two sức chứa (capacity / 용량) cho phép chỉ số modulo bằng mask:

```text
index & (capacity - 1)
```

chỉ khi sức chứa (capacity / 용량) thực sự là lũy thừa của hai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **Bit Hacks không nên thay clarity vô điều kiện** tiếp nhận điểm tựa từ **Next lũy thừa của hai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo mật (security / 보안) considerations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bit Hacks không nên thay clarity vô điều kiện

Hiện đại compilers tối ưu nhiều các mẫu. Một obscure trick không tự động nhanh hơn clear mã (code / 코드)/thư viện (library / 라이브러리) intrinsic.

Ví dụ manual popcount hack có thể chậm hơn hardware intrinsic và khó rà soát (review / 검토).

Use bit trick khi nó:

```text
encode mathematical property rõ
reduce asymptotic/state complexity
map tốt tới library/hardware
```

không phải để mã (code / 코드) trông “low-level”.

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Bảo mật (security / 보안) considerations** tiếp nhận điểm tựa từ **Bit Hacks không nên thay clarity vô điều kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo mật (security / 보안) considerations

Mã thao tác bit xuất hiện nhiều trong mật mã, bộ phân tích cú pháp và giao thức. Tuy nhiên các mẹo bit tự viết cho mật mã rất dễ tạo kênh rò rỉ phụ hoặc lỗi lô-gic (logic / 논리).

Constant-time programming là chuyên biệt bảo mật (security / 보안) discipline; branchless bit các thao tác không tự động làm mã (code / 코드) constant-time vì trình biên dịch/môi trường chạy (runtime)/bộ nhớ hành vi còn ảnh hưởng.

Không nên tự thiết kế cryptographic thành phần nguyên thủy (primitive / 기본 요소) chỉ vì hiểu bitwise operators.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **Bảo mật (security / 보안) considerations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kiểm thử Bit mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“Bitmask luôn O(1).”** Chỉ khi trạng thái fit trong fixed number machine words. Arbitrary-size tập bit thao tác là `O(number of words)`.

**“Bitwise trong JavaScript dùng toàn bộ 53-bit integer precision.”** Không; Number bitwise operators dùng 32-bit coercion.

**“`x & -x` luôn an toàn cho mọi kiểu (type / 타입).”** Cần hiểu signed width và ngôn ngữ (language / 언어) tràn số ngữ nghĩa.

**“Bit DP làm exponential bài toán (problem / 문제) thành fast polynomial.”** trạng thái count vẫn `2^n`; bitmask chỉ làm cách biểu diễn gọn.

**“Shift giống multiply/divide cho mọi signed giá trị.”** Rounding, tràn số và sign-fill có thể khác arithmetic expectation.

**“tập bit = bộ lọc Bloom.”** tập bit thường chính xác flags; bộ lọc Bloom thêm hashing và probabilistic các dương tính giả.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **thao tác bit và Bitsets**, **kiểm thử Bit mã (code / 코드)** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi nào thao tác bit thật sự đáng dùng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kiểm thử Bit mã (code / 코드)

Bit bugs thường nằm ở các ranh giới:

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

tính chất tests hữu ích:

```text
set rồi clear bit -> original value
x ^ x == 0
popcount(x) == number of enumerated set bits
submask loop chỉ sinh subsets của mask và không duplicate
bitset AND tương đương set intersection reference
```

> **Chuyển mạch:** Trong **thao tác bit và Bitsets**, **Khi nào thao tác bit thật sự đáng dùng?** tiếp nhận điểm tựa từ **kiểm thử Bit mã (code / 코드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy mở rộng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi nào thao tác bit thật sự đáng dùng?

Bit cách biểu diễn đặc biệt mạnh khi:

```text
universe nhỏ hoặc vừa và dense
state là nhiều boolean flags
subset identity cần hash/index nhanh
word-level batch operations hữu ích
memory bandwidth quan trọng
```

Nếu lĩnh vực (domain / 도메인) các khóa sparse, huge hoặc động labels, `HashSet`, sorted set hoặc bitmap nén có thể phù hợp hơn.

Roaring Bitmap, chẳng hạn, chia miền giá trị thành các khối và chọn cách biểu diễn dày hoặc thưa theo lực lượng cục bộ. Đây là một ví dụ thực tế vượt khỏi lựa chọn đơn giản “bitset hay set” bằng một cấu trúc lai.

> **Chuyển mạch:** Ở chặng này của **thao tác bit và Bitsets**, **Mô hình tư duy mở rộng** gom các mảnh từ **Khi nào thao tác bit thật sự đáng dùng?** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy mở rộng

> thao tác bit không phải collection của mẹo nhị phân. Nó là **dữ liệu (data / 데이터) cách biểu diễn thiết kế (design / 설계)**: khi trạng thái thật sự là boolean véc-tơ (vector / 벡터), nhị phân (binary / 이진) integer/tập bit cho phép bộ nhớ gọn, algebra rõ và hardware xử lý nhiều flags cùng lúc.

Khi dùng bit trick, luôn hỏi ba điều: chứng minh identity đến từ đâu, integer width/signedness của language là gì, và trạng thái có thực sự fit mô hình dense boolean vector không. Nếu ba câu này rõ, bitwise code trở thành công cụ có hệ thống thay vì magic.

> **Bàn giao:** Sau **Mô hình tư duy mở rộng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
