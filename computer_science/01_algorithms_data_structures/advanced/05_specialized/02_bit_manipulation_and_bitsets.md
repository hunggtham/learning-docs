# Bit Manipulation và Bitsets
**비트 연산과 비트셋**

Bit manipulation khai thác binary representation để biểu diễn flags, subsets và trạng thái compact.

## Operations

```text
&  AND
|  OR
^  XOR
~  NOT
<< left shift
>> right shift
```

Kiểm tra bit `k`: `x & (1 << k)`. Set: `x | (1 << k)`. Clear: `x & ~(1 << k)`. Toggle: `x ^ (1 << k)`.

## Bitmask subset

Với `n` items nhỏ, một integer mask biểu diễn subset: bit `k=1` nghĩa item `k` được chọn. Tổng subsets là `2^n`, nên bitmask không làm exponential state biến mất; nó chỉ biểu diễn state gọn và cho operations nhanh.

## Least significant set bit

Trong two's complement:

```text
x & -x
```

lấy bit 1 thấp nhất. Fenwick tree dùng trực tiếp property này để nhảy theo binary blocks.

## XOR

`x ^ x = 0`, `x ^ 0 = x`. Nếu mọi số xuất hiện đúng hai lần trừ một số xuất hiện một lần, XOR toàn bộ trả số lẻ đó. Đây không phải “magic”; nó đúng vì constraints khớp algebra của XOR.

## Bitset

Bitset biểu diễn nhiều boolean flags bằng machine words, tiết kiệm memory và cho phép batch AND/OR/XOR. Java có `BitSet`. JavaScript bitwise operators thường có 32-bit integer semantics; với masks lớn phải cẩn thận và cân nhắc `BigInt` hoặc typed representations.

## Mental Model

> Bitmask biến nhiều boolean state thành một số, để hardware có thể xử lý nhiều flags qua vài bitwise operations.

## Two's complement và `-x`

Trong two's complement fixed-width arithmetic, `-x = ~x + 1`. Vì vậy `x & -x` giữ lại bit 1 thấp nhất và xóa các bit khác. Fenwick tree dùng giá trị này như kích thước block phụ trách.

## Enumerating subsets

Với mask có `n` bits:

```c
for (int mask = 0; mask < (1 << n); ++mask) {
    // subset encoded by mask
}
```

Để enumerate submasks của một mask:

```c
for (int sub = mask; sub; sub = (sub - 1) & mask) {
    // every non-empty submask
}
```

Pattern này đi qua đúng các submasks vì subtraction thay đổi suffix bits rồi AND ép kết quả nằm trong mask.

Tổng số `(mask, submask)` pairs qua mọi masks là `3^n`, vì mỗi bit có ba trạng thái: không ở mask, ở mask nhưng không ở sub, ở cả sub.

## Popcount

Đếm set bits dùng hardware intrinsic/library khi có. Brian Kernighan loop:

```c
while (x) {
    x &= x - 1;
    count++;
}
```

mỗi iteration xóa set bit thấp nhất, nên chạy theo số set bits.

## Bitset acceleration

Nếu một set có universe vài nghìn items, AND/OR của bitsets xử lý 64 memberships mỗi machine word. Graph reachability approximations, subset constraints và DP boolean có thể được tăng tốc lớn nhờ word-level parallelism.

## Signed shift caveats

C signed shifting có rules/undefined or implementation-defined corners tùy operation/value; Java có `>>` arithmetic và `>>>` logical right shift. JavaScript bitwise operations coerce về 32-bit. Code portable phải biết semantics ngôn ngữ chứ không chỉ toán bit abstract.
