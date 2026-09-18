# Số và các hệ số

Số (Number / 수) không chỉ là ký hiệu để đếm. Mỗi lần toán học gặp một loại bài toán mà hệ số hiện tại không giải được một cách đóng kín, con người mở rộng khái niệm số. Natural numbers đủ để đếm, nhưng không đủ cho `3-5`. Integers giải subtraction, nhưng không đủ cho `1/2`. Rational numbers giải division giữa integers khác 0, nhưng không chứa `√2`. Real numbers lấp những “gaps” đó, còn complex numbers cho phép giải phương trình như `x^2+1=0` và mô tả rotation/oscillation rất tự nhiên.

## Natural numbers

Số tự nhiên (Natural numbers / 자연수) dùng cho counting. Tùy convention:

```math
\mathbb N=\{0,1,2,3,\ldots\}
```

hoặc bắt đầu từ 1. Vì textbooks khác nhau, luôn kiểm tra convention.

Addition và multiplication của naturals là closed:

```math
3+5=8\in\mathbb N
```

```math
3\times5=15\in\mathbb N.
```

Nhưng subtraction không closed:

```math
3-5=-2\notin\mathbb N.
```

Vấn đề đó thúc đẩy integers.

## Integers

Số nguyên (Integers / 정수):

```math
\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\}.
```

Integers thêm notion direction quanh zero. Điều này hữu ích cho balance/debt, nhiệt độ trên dưới mốc, coordinate và displacement.

Addition, subtraction, multiplication closed trên integers, nhưng division không:

```math
1/2\notin\mathbb Z.
```

## Rational numbers

Số hữu tỉ (Rational numbers / 유리수) là numbers viết được dưới dạng

```math
\frac pq
```

với integers `p,q` và `q≠0`.

Decimal hữu hạn như `0.125` là rational vì

```math
0.125=\frac{125}{1000}=\frac18.
```

Repeating decimal cũng rational. Ví dụ

```math
x=0.333\ldots
```

thì

```math
10x=3.333\ldots
```

trừ hai phương trình:

```math
9x=3
\Rightarrow x=\frac13.
```

## Irrational numbers

Số vô tỉ (Irrational numbers / 무리수) không thể biểu diễn thành ratio của two integers. `√2`, `π`, `e` là examples nổi tiếng.

Irrational không có nghĩa “không thể xấp xỉ bằng phân số”. Thực tế rational numbers có thể approximate reals tùy ý gần. Điều bị cấm là equality exact với một fraction hữu hạn integers.

## Real numbers

Số thực (Real numbers / 실수)

```math
\mathbb R
```

có thể hình dung như mọi points trên continuous number line.

Một property sâu là completeness: certain bounded sets/sequences có limits nằm trong `R`. Đây là nền để calculus hoạt động. Rational numbers alone có “holes”; sequence rationals có thể tiến tới `√2`, nhưng `√2` không nằm trong `Q`.

## Absolute value và distance

Giá trị tuyệt đối (Absolute value / 절댓값)

```math
|x|
```

đo distance từ `x` tới zero trên number line.

Do đó

```math
|a-b|
```

là distance giữa `a` và `b`.

Đây là bridge từ arithmetic sang geometry và sau đó vector norm.

Triangle inequality:

```math
|a+b|\le|a|+|b|.
```

Trực giác: đi trực tiếp không dài hơn đi vòng qua hai legs.

## Complex numbers

Số phức (Complex numbers / 복소수) có dạng

```math
z=a+bi
```

với

```math
i^2=-1.
```

Ban đầu `i` xuất hiện để giải equations không có real roots. Nhưng complex numbers còn biểu diễn 2D rotations và waves cực kỳ tự nhiên.

Trên complex plane, `a` là horizontal coordinate và `b` là vertical coordinate.

Magnitude:

```math
|z|=\sqrt{a^2+b^2}
```

chính là Pythagorean distance tới origin.

Euler relation

```math
e^{i\theta}=\cos\theta+i\sin\theta
```

nối exponential với rotation. Vì vậy complex numbers xuất hiện trong signal processing, Fourier transform, control systems và quantum mechanics.

## Base systems

Hệ cơ số (Numeral system / 기수법) quyết định weights của digit positions.

Decimal base 10:

```text
372 = 3×10² + 7×10¹ + 2×10⁰
```

Binary base 2:

```text
1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 11₁₀
```

Hexadecimal base 16 dùng digits `0–9,A–F` và compact hơn binary:

```text
FF₁₆ = 255₁₀
```

Trong computing, base 2 không được dùng vì “máy tính thích số 0 và 1” một cách bí ẩn; physical digital circuits dễ thiết kế với hai stable state ranges và Boolean logic xây trên hai states đó.

## Positional representation

General base `b`:

```math
(d_nd_{n-1}\ldots d_0)_b
=
\sum_{k=0}^n d_kb^k.
```

Fractional positions dùng negative powers:

```math
0.101_2
=
1\cdot2^{-1}+0\cdot2^{-2}+1\cdot2^{-3}
=
\frac12+\frac18
=0.625.
```

## Floating point và hữu hạn bit

Không phải mọi real number có finite binary representation. `0.1₁₀` trở thành repeating expansion trong binary, giống `1/3` repeating trong decimal.

IEEE floating-point lưu approximation thông qua sign, exponent và significand. Vì representation finite, arithmetic có rounding.

Do đó comparison kiểu

```text
x == 0.3
```

sau một chuỗi floating calculations có thể unreliable. Numerical code thường compare tolerance:

```text
abs(x - 0.3) < epsilon
```

nhưng lựa chọn epsilon cần phụ thuộc scale/problem chứ không phải constant magic cho mọi trường hợp.

## Overflow

Fixed-width integer có finite range. Signed 32-bit integer thường có range:

```math
-2^{31}\le x\le2^{31}-1.
```

Nếu computation vượt range, behavior phụ thuộc language/runtime: wraparound, exception, undefined behavior hoặc arbitrary precision alternative.

Toán học integers là unbounded abstraction; computer integer representation là finite engineering object. Phân biệt hai layer này rất quan trọng.

## Order và density

Rational và real numbers đều dense theo nghĩa giữa hai numbers khác nhau luôn có number khác. Ví dụ giữa `a<b`, midpoint

```math
\frac{a+b}{2}
```

nằm giữa chúng.

Nhưng reals có completeness mà rationals không có. Đây là điểm calculus sẽ dùng khi nói limits.

## Mental Model

> Các hệ số là những lần mở rộng “vũ trụ số” để các operations và limits ta cần có chỗ tồn tại: counting dẫn tới natural, subtraction dẫn tới integer, division dẫn tới rational, limits dẫn tới real, algebra/rotation dẫn tới complex.

## Common Misconceptions

Irrational không nghĩa random. Complex không nghĩa “không thật” hay vô dụng. Binary number không khác bản chất quantity; nó chỉ là representation khác. Floating-point number trong máy tính không phải một real number với infinite precision.
