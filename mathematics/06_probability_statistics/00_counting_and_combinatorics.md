# Đếm và tổ hợp

Tổ hợp (Combinatorics / 조합론) nghiên cứu cách đếm configurations mà không cần liệt kê từng case. Đây là nền của probability rời rạc, algorithm analysis và search spaces.

## Rule of product

Nếu một process có `m` choices ở bước đầu và với mỗi choice có `n` choices ở bước sau, total combinations:

```math
mn
```

Ví dụ mã gồm 3 decimal digits có

```math
10^3=1000
```

strings nếu leading zero được phép. Mỗi position là một independent choice trong counting sense.

## Rule of sum

Nếu hai sets cases rời nhau có sizes `m` và `n`, total cases `m+n`. Nếu overlap, phải tránh double-counting bằng inclusion-exclusion.

## Permutations

Sắp xếp `n` distinct objects:

```math
n!=n(n-1)\cdots2\cdot1
```

vì position đầu có `n` choices, kế `n-1`, v.v.

Chọn và sắp `k` objects từ `n`:

```math
P(n,k)=\frac{n!}{(n-k)!}
```

Order matters.

## Combinations

Nếu chỉ chọn subset size `k` và order không matter, mỗi subset bị đếm `k!` lần trong permutations, nên

```math
\binom nk=\frac{n!}{k!(n-k)!}
```

Đây là binomial coefficient.

## Binomial theorem

```math
(a+b)^n=\sum_{k=0}^n\binom nk a^{n-k}b^k
```

Coefficient `C(n,k)` xuất hiện vì để tạo term có `k` copies của `b`, ta chọn `k` trong `n` factors `(a+b)` để lấy `b`.

## Combinations with repetition

Số nonnegative integer solutions của

```math
x_1+\cdots+x_k=n
```

là

```math
\binom{n+k-1}{k-1}
```

stars-and-bars interpretation: `n` identical items và `k-1` separators.

## Inclusion-exclusion

Với hai sets:

```math
|A\cup B|=|A|+|B|-|A\cap B|
```

vì intersection bị cộng hai lần. Với nhiều sets, signs alternate theo overlaps higher order.

## Pigeonhole principle

Nếu `n+1` objects được đặt vào `n` boxes, ít nhất một box chứa ≥2 objects. Principle nghe hiển nhiên nhưng proof existence rất mạnh.

Trong hashing, nếu key space lớn hơn bucket count, collisions là unavoidable bất kể hash function thiết kế tốt đến đâu.

## Search-space growth

Mỗi binary decision thêm factor 2. `n` independent yes/no choices tạo `2^n` subsets. Vì vậy brute-force subset optimization nhanh chóng infeasible.

Traveling Salesman naive route permutations tăng roughly factorial, còn lớn hơn exponential đơn giản.

## Mental Model

> Combinatorics biến “bao nhiêu cấu hình có thể xảy ra?” thành decomposition của choices. Product rule dùng khi decisions nối tiếp; combinations bỏ order; inclusion-exclusion sửa double counting; growth rate của count thường báo trước computational difficulty.

## Common Misconceptions

Permutation và combination khác nhau ở việc order có tạo configuration mới hay không. Independence trong probability không đồng nghĩa “các choices nhìn khác nhau”; counting product rule cần structure phù hợp. Factorial growth vượt polynomial rất nhanh.

## Worked Example: birthday collision

Nếu có `n` người và giả sử 365 birthdays equally likely, independent, bỏ leap day, dễ hơn tính probability **không ai trùng** trước:

```math
P(\text{no collision})
=1\cdot\frac{364}{365}\cdot\frac{363}{365}\cdots
\frac{365-n+1}{365}
```

nên

```math
P(\text{at least one collision})
=1-P(\text{no collision})
```

Với 23 người, probability collision đã trên khoảng 50%. Trực giác thường đánh giá thấp vì number pairs tăng theo

```math
\binom n2=\frac{n(n-1)}2
```

chứ không chỉ tăng theo n.

## Combinatorics và probability

Khi outcomes equally likely, probability trở thành favorable count / total count. Nhưng combinatorics chỉ cho counts; assumption equally likely phải đến từ probability model. Chọn “đếm được bao nhiêu” không tự động cho “khả năng bao nhiêu”.
