# Lũy thừa, căn và logarithm

Lũy thừa, căn và logarithm là ba cách nhìn cùng một relationship. Nếu

```math
b^x=y
```

thì `b^x` hỏi output khi biết base/exponent, căn hỏi base-like quantity trong trường hợp exponent biết, còn logarithm hỏi exponent cần thiết để đi từ base tới output.

## Exponential operation

Với integer positive `n`:

```math
b^n=b\cdot b\cdots b.
```

Repeated multiplication tạo exponential growth khi factor lớn hơn 1.

Ví dụ doubling:

```text
1,2,4,8,16,32,...
```

sau `n` doublings:

```math
2^n.
```

## Logarithm là inverse của exponentiation

Logarithm (Logarithm / 로그) được định nghĩa:

```math
\log_b y=x
\iff
b^x=y.
```

Ví dụ:

```math
\log_2 8=3
```

vì

```math
2^3=8.
```

Mental question là “phải multiply by base bao nhiêu lần trên exponential scale để đạt y?”.

## Log laws

Từ

```math
b^m b^n=b^{m+n}
```

lấy log cho:

```math
\log_b(xy)=\log_b x+\log_b y.
```

Product biến thành sum. Đây là lý do logarithm từng cực kỳ quan trọng cho manual computation và vẫn quan trọng trong numerical probability: product của rất nhiều small probabilities có thể underflow, nên ta cộng log-probabilities.

Tương tự:

```math
\log_b(x^k)=k\log_bx.
```

## Natural logarithm

Natural log

```math
\ln x=\log_e x
```

với

```math
e\approx2.71828.
```

Base `e` không được chọn tùy ý. Function `e^x` có property derivative bằng chính nó:

```math
\frac{d}{dx}e^x=e^x.
```

Vì vậy `e` là base tự nhiên cho continuous growth, differential equations và calculus.

## Compound growth

Nếu growth rate mỗi period là `r`:

```math
A_n=A_0(1+r)^n.
```

Muốn biết cần bao nhiêu periods để đạt target `A`:

```math
A=A_0(1+r)^n
```

chia `A_0`:

```math
\frac A{A_0}=(1+r)^n
```

lấy logarithm:

```math
n=\frac{\ln(A/A_0)}{\ln(1+r)}.
```

Logarithm xuất hiện vì unknown nằm trong exponent.

## Binary search và O(log n)

Binary search mỗi bước loại khoảng một nửa search space. Sau `k` bước, size còn approximately

```math
\frac{n}{2^k}.
```

Muốn còn 1:

```math
\frac{n}{2^k}=1
```

nên

```math
2^k=n
```

và

```math
k=\log_2 n.
```

Vì vậy `O(log n)` không phải label phải học thuộc; nó mô tả số lần có thể chia problem size theo constant factor trước khi xuống size 1.

Nếu `n≈1,000,000`, vì

```math
2^{20}\approx1,048,576,
```

binary search cần khoảng 20 halvings.

## Decibel và multiplicative scale

Decibel dùng logarithmic representation của ratio. Với power ratio:

```math
L=10\log_{10}\left(\frac{P}{P_0}\right)\,dB.
```

Log scale hữu ích khi ratios trải nhiều orders of magnitude và khi multiplicative changes cần chuyển thành additive differences.

## pH

pH:

```math
pH=-\log_{10}[H^+].
```

Nếu hydrogen ion concentration tăng factor 10, pH giảm 1. Log compresses concentration range và biến multiplicative factor thành additive scale.

## Information theory

Information content của event probability `p` thường measured:

```math
I=-\log_2p.
```

Nếu independent probabilities multiply, information amounts add vì log product thành sum. Rare event có smaller `p`, vì vậy larger information/surprise.

## Mental Model

> Exponential mô tả repeated multiplication. Logarithm đo “multiplicative depth” — cần bao nhiêu exponential steps để đạt một scale. Vì vậy log xuất hiện bất cứ nơi nào problem co/giãn theo factors thay vì fixed differences.

## Common Misconceptions

`log(a+b)` không bằng `log a + log b`; log law áp dụng product. `log_b x` yêu cầu base thích hợp (`b>0,b≠1`) và với real logarithm `x>0`. `O(log n)` không đơn giản nghĩa “nhanh”; nó mô tả scaling asymptotic và constant factors vẫn có thể quan trọng trong actual system.
