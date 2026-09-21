# Lũy thừa, căn và logarithm: multiplicative structure và inverse scales

Lũy thừa (power / 거듭제곱), căn (root / 근) và logarithm (로그) không phải ba chủ đề tách rời. Chúng là ba cách đọc cùng một relationship:

```math
b^x=y.
```

Nếu biết `b` và `x`, ta tính `y`: đó là exponentiation. Nếu biết `x` và `y`, ta hỏi giá trị base-like phù hợp: đó dẫn tới roots. Nếu biết `b` và `y`, ta hỏi exponent cần thiết: đó là logarithm.

Điểm sâu hơn là cả ba thuộc **multiplicative structure**. Chúng mô tả systems nơi scale thay đổi bằng factors, không phải fixed differences.

## 1. Từ repeated addition đến repeated multiplication

Multiplication có thể được xem như repeated addition trong integer setting:

```math
5\cdot3=5+5+5.
```

Exponentiation tiếp tục pattern bằng repeated multiplication:

```math
b^n=\underbrace{b\cdot b\cdots b}_{n\text{ factors}}.
```

Nếu `b>1`, repeated multiplication tạo growth nhanh hơn linear growth vì mỗi step scale toàn bộ quantity hiện tại.

Ví dụ doubling:

```text
1, 2, 4, 8, 16, 32, ...
```

sau `n` doublings:

```math
2^n.
```

Đây là structure phía sau compound interest, population models, binary trees và many divide/multiply processes.

## 2. Vì sao exponent laws tồn tại?

Với positive integers:

```math
b^m b^n
```

chỉ là product có tổng cộng `m+n` factors `b`, nên

```math
b^m b^n=b^{m+n}.
```

Tương tự,

```math
(b^m)^n=b^{mn}
```

vì ta lặp một product có `m` factors tổng cộng `n` lần.

Các exponent laws không nên được học như bảng rules; chúng đến từ counting multiplicative factors.

## 3. Tại sao exponent 0 bằng 1?

Ta muốn law

```math
\frac{b^m}{b^n}=b^{m-n}
```

vẫn nhất quán khi `m=n`.

Left side:

```math
\frac{b^n}{b^n}=1,
```

nên ta cần

```math
b^0=1,\qquad b\ne0.
```

Đây là consistency extension: definition của exponent được mở rộng để giữ algebraic structure.

## 4. Negative exponents là inverse scaling

Muốn law

```math
b^m b^n=b^{m+n}
```

vẫn đúng với `n=-m`, ta cần

```math
b^m b^{-m}=b^0=1.
```

Do đó

```math
b^{-m}=\frac1{b^m}.
```

Negative exponent không nghĩa “negative multiplication”; nó nghĩa multiplicative inverse.

Ví dụ:

```math
10^{-3}=\frac1{1000}=0.001.
```

Scientific notation dựa trực tiếp trên idea này.

## 5. Fractional exponents và roots

Ta muốn

```math
(b^{1/n})^n=b.
```

Do exponent multiplication law, điều này gợi ý

```math
b^{1/n}=\sqrt[n]{b}
```

trong domain phù hợp.

Do đó

```math
b^{m/n}=\sqrt[n]{b^m}.
```

Với real numbers, domain cần cẩn thận: even root của negative real không tồn tại trong `\mathbb R`, nhưng tồn tại trong complex numbers.

Fractional exponents vì vậy nối number systems với exponent laws.

## 6. Exponential function khác polynomial growth như thế nào?

So sánh

```math
x^3
```

và

```math
2^x.
```

Trong polynomial, variable nằm ở base. Trong exponential, variable nằm ở exponent.

Khi `x` lớn, exponential với base `>1` cuối cùng vượt mọi fixed-degree polynomial. Đây là lý do exponential-time algorithms trở nên infeasible cực nhanh.

Ví dụ:

```math
2^{100}\approx1.27\times10^{30}.
```

Không có micro-optimization thông thường nào cứu được việc enumerate tất cả `2^100` possibilities.

## 7. Logarithm là inverse của exponential

Definition:

```math
\log_b y=x
\iff
b^x=y,
```

với real logarithm yêu cầu

```math
b>0,\qquad b\ne1,\qquad y>0.
```

Logarithm trả lời câu hỏi:

> Cần bao nhiêu multiplicative steps ở base `b` để đi từ scale 1 tới scale `y`?

Ví dụ:

```math
\log_2 8=3
```

vì ba doublings đưa 1 thành 8.

## 8. Vì sao log biến product thành sum?

Giả sử

```math
x=b^m,\qquad y=b^n.
```

Khi đó

```math
xy=b^{m+n}.
```

Lấy log base `b`:

```math
\log_b(xy)=m+n
```

và vì

```math
m=\log_bx,\qquad n=\log_by,
```

nên

```math
\log_b(xy)=\log_bx+\log_by.
```

Log law xuất phát trực tiếp từ exponent law. Product trở thành sum vì logarithm đo exponent depth.

Tương tự:

```math
\log_b(x^k)=k\log_bx.
```

## 9. Change of base: vì sao base chỉ thay scale

Từ

```math
b^x=y
```

lấy natural log:

```math
x\ln b=\ln y,
```

nên

```math
\log_b y=\frac{\ln y}{\ln b}.
```

Các log bases khác nhau chỉ khác nhau bởi constant scale factor. Đây là lý do trong Big-O,

```math
\log_2 n
```

và

```math
\ln n
```

cùng asymptotic order.

## 10. Base `e` xuất hiện từ continuous change

Natural exponential

```math
e^x
```

đặc biệt vì

```math
\frac{d}{dx}e^x=e^x.
```

Nếu quantity có instantaneous growth rate proportional với chính nó,

```math
\frac{dA}{dt}=kA,
```

solution có dạng

```math
A(t)=A_0e^{kt}.
```

Do đó `e` không chỉ là một constant lạ. Nó là base tự nhiên khi multiplicative change xảy ra continuously.

## 11. Compound growth và solving time-to-target

Nếu growth mỗi period là `r`,

```math
A_n=A_0(1+r)^n.
```

Muốn tìm `n` để đạt target `A`:

```math
A=A_0(1+r)^n.
```

Chia cho `A_0`:

```math
\frac A{A_0}=(1+r)^n.
```

Lấy log:

```math
n=\frac{\ln(A/A_0)}{\ln(1+r)}.
```

Unknown nằm trong exponent nên logarithm là inverse operation tự nhiên.

### Worked example

Một khoản đầu tư tăng 8% mỗi năm. Cần bao lâu để tăng gấp đôi?

```math
2=(1.08)^n.
```

Suy ra

```math
n=\frac{\ln2}{\ln1.08}\approx9.0.
```

Đây là nguồn gốc định lượng của Rule of 72 approximation.

## 12. Half-life và exponential decay

Nếu quantity giảm theo

```math
A(t)=A_0e^{-kt},
```

half-life `T_{1/2}` thỏa

```math
\frac{A_0}{2}=A_0e^{-kT_{1/2}}.
```

Do đó

```math
T_{1/2}=\frac{\ln2}{k}.
```

Cùng algebra áp dụng cho radioactive decay, pharmacokinetics, capacitor discharge và nhiều relaxation processes.

## 13. `O(log n)` đến từ repeated shrinking

Nếu mỗi step giảm problem size bởi factor `b>1`:

```math
n,\frac nb,\frac n{b^2},\ldots
```

sau `k` steps còn khoảng 1:

```math
\frac{n}{b^k}\approx1.
```

Suy ra

```math
k\approx\log_b n.
```

Binary search là example điển hình. `O(log n)` không có nghĩa code phải gọi một `log()` function; logarithm xuất hiện từ **number of multiplicative reductions**.

## 14. Log scales trong measurement

Khi values trải nhiều orders of magnitude, linear scale có thể khó đọc. Logarithmic scales chuyển ratios thành differences.

### Decibel

Với power ratio:

```math
L=10\log_{10}\left(\frac{P}{P_0}\right)\text{ dB}.
```

Một factor `10` về power tương ứng +10 dB.

### pH

```math
pH=-\log_{10}[H^+].
```

Concentration tăng factor 10 làm pH giảm 1.

Log scales rất hữu ích, nhưng interpretation phải giữ relation với original multiplicative scale.

## 15. Information theory: surprise là logarithmic

Information content thường được viết

```math
I(x)=-\log_2P(x).
```

Nếu hai independent events có probabilities multiply,

```math
P(A\cap B)=P(A)P(B),
```

thì information adds:

```math
I(A,B)=I(A)+I(B).
```

Logarithm là function tự nhiên vì nó biến multiplicative probability structure thành additive information.

## 16. Numerical computing: tại sao dùng log-probability?

Trong statistics/AI, likelihood của many independent observations thường là product:

```math
L(\theta)=\prod_i p(x_i\mid\theta).
```

Product của nhiều số nhỏ có thể underflow floating point. Lấy log:

```math
\log L(\theta)=\sum_i\log p(x_i\mid\theta).
```

Ta vừa biến product thành sum, vừa cải thiện numerical behavior.

Đây là example rõ của algebraic identity trở thành engineering technique.

## 17. Common failure modes

### `\log(a+b)` không phân phối qua addition

Không có rule

```math
\log(a+b)=\log a+\log b.
```

Log laws đến từ multiplication/exponent structure, không phải arbitrary algebraic simplification.

### Root và exponent có domain subtleties

Ví dụ

```math
\sqrt{x^2}=|x|,
```

không phải luôn `x`. Square root convention trả nonnegative principal root trong real numbers.

### Exponential model không thể dùng vô hạn

Một system có finite resources thường không thể grow exponential mãi. Logistic models hoặc saturation mechanisms có thể cần thiết.

## Applications và connections

**Computer Science:** binary search, tree height, exponential state spaces, logarithmic data structures.

**Physics:** radioactive decay, oscillation envelopes, thermodynamics/statistical mechanics scales.

**AI:** log-likelihood, cross-entropy, softmax stabilization, exponential families.

**Finance:** compound returns, discounting, continuously compounded rates, time-to-target calculations.

## Mental Model

> Powers describe multiplicative accumulation. Roots undo a known power. Logarithms measure multiplicative depth. Whenever a system changes by ratios, factors, repeated halving/doubling or compounding, exponentials and logarithms are the natural language.

## Common Misconceptions

**Exponent rules là arbitrary formulas.** Không; chúng encode how multiplicative factors combine.

**Negative exponent là negative value.** Không; nó means reciprocal scaling.

**Logarithm chỉ dùng để solve equations.** Không; nó là coordinate system tự nhiên cho multiplicative processes và information.

**`O(log n)` nghĩa “rất nhanh” trong mọi setting.** Không; nó mô tả asymptotic scaling trong một cost model. Constants, memory access và I/O vẫn matter.
