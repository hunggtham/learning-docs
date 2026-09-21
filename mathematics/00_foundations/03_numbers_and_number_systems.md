# Số và các hệ số: mở rộng universe để phép toán có nơi tồn tại

Số (number / 수) không phải một collection ký hiệu rời rạc. Mỗi hệ số xuất hiện vì hệ trước đó không còn đủ để giữ một số operation hoặc limit quan trọng.

Ta có thể nhìn lịch sử mở rộng như một dependency chain:

```text
đếm
→ số tự nhiên
→ cần phép trừ
→ số nguyên
→ cần phép chia
→ số hữu tỉ
→ cần giới hạn không bị “rơi ra ngoài”
→ số thực
→ cần nghiệm cho polynomial như x²+1=0
→ số phức
```

Mental model này hữu ích hơn học `N ⊂ Z ⊂ Q ⊂ R ⊂ C` như một chuỗi ký hiệu cần nhớ.

## 1. Một number system được chọn theo operations ta cần

Một set số có thể **closed** dưới một operation: thực hiện operation trên members vẫn cho result nằm trong set.

Natural numbers closed dưới addition và multiplication:

```math
3+5=8\in\mathbb N
```

```math
3\cdot5=15\in\mathbb N.
```

Nhưng không closed dưới subtraction:

```math
3-5=-2\notin\mathbb N.
```

Điểm này giải thích vì sao negative numbers không phải “phần phụ kỳ lạ”; chúng hoàn tất một operation mà counting numbers chưa giữ được.

## 2. Natural numbers: arithmetic của counting

Số tự nhiên (natural numbers / 자연수) thường được viết

```math
\mathbb N=\{0,1,2,3,\ldots\}
```

hoặc bắt đầu từ 1 tùy convention.

Natural numbers model count của discrete objects. Với `n` objects, addition mô tả combining collections, multiplication mô tả repeated groups.

Peano-style viewpoint còn cho thấy arithmetic có thể được xây từ successor operation, nhưng scope hiện tại không cần formal axiomatization đầy đủ. Điều quan trọng là hiểu natural numbers mang **discrete order + arithmetic structure**.

## 3. Integers: thêm direction quanh zero

Số nguyên (integers / 정수):

```math
\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\}.
```

Integers làm subtraction closed:

```math
3-5=-2\in\mathbb Z.
```

Negative number nên được hiểu như direction/opposite trong additive structure, không chỉ là “debt number”.

Mỗi integer `a` có additive inverse `-a` sao cho

```math
a+(-a)=0.
```

Đây là bridge đầu tiên tới group-like algebraic thinking: operation có identity và inverse.

Integers vẫn không closed dưới division:

```math
1/2\notin\mathbb Z.
```

## 4. Rational numbers: hoàn tất phép chia giữa integers

Số hữu tỉ (rational numbers / 유리수) có dạng

```math
\frac pq,
\qquad p,q\in\mathbb Z,
\qquad q\ne0.
```

Mỗi rational có nhiều representations:

```math
\frac12=\frac24=\frac{50}{100}.
```

Vì vậy rational number về structural sense là **equivalence class của fractions**, không phải một particular pair numerator/denominator.

Two fractions

```math
\frac ab,\qquad\frac cd
```

represent cùng rational khi

```math
ad=bc
```

với denominators nonzero.

Đây là connection giữa number systems và equivalence relations.

## 5. Decimal expansion và rationality

Finite decimal luôn rational:

```math
0.125=\frac{125}{1000}=\frac18.
```

Repeating decimal cũng rational. Với

```math
x=0.333\ldots,
```

nhân 10:

```math
10x=3.333\ldots
```

trừ:

```math
9x=3
```

nên

```math
x=\frac13.
```

General fact: real number có eventually repeating decimal expansion iff nó rational.

Điều này cho thấy representation bằng digits chứa information về algebraic nature của number.

## 6. Irrational numbers: rational line có “holes” đối với limits

Số vô tỉ (irrational numbers / 무리수) không thể biểu diễn thành ratio của two integers.

`√2` là classic example. Proof by contradiction cho thấy giả sử

```math
\sqrt2=\frac ab
```

ở lowest terms dẫn tới `a,b` đều chẵn, contradiction.

Irrational không nghĩa “không approximate được”. Rational numbers dense trong reals: có thể approximate `√2`, `π`, `e` tùy ý chính xác.

Vấn đề là approximation không bằng exact membership.

## 7. Real numbers và completeness

Số thực (real numbers / 실수) thường được visualized như mọi points trên continuous number line.

Nhưng property quan trọng nhất cho calculus là **completeness**.

Intuition: nếu một process rational approximations đang hội tụ về một location “đáng lẽ phải có”, real-number system không để location đó bị thiếu.

Một formulation quan trọng là least-upper-bound property: mọi nonempty subset của `R` bị chặn trên có supremum trong `R`.

Một formulation khác dùng Cauchy sequences: sequence các real numbers mà terms trở nên arbitrarily close với nhau phải converge tới một real number.

Rationals không complete. Có rational Cauchy sequences converge về `√2`, nhưng `√2∉Q`.

Đây là reason Real Analysis dành nhiều thời gian cho completeness: limits, derivatives, integrals dựa vào việc limiting objects không biến mất khỏi number system.

## 8. Absolute value: từ sign tới metric

Giá trị tuyệt đối (absolute value / 절댓값)

```math
|x|
```

đo distance từ `x` tới zero.

Khoảng cách giữa `a,b`:

```math
|a-b|.
```

Triangle inequality:

```math
|a+b|\le|a|+|b|.
```

Không nên nhìn đây chỉ là inequality để biến đổi. Nó nói path trực tiếp không dài hơn đi qua intermediate decomposition.

Pattern này mở rộng tới vector norms:

```math
\|u+v\|\le\|u\|+\|v\|.
```

Vì vậy absolute value là first example của norm/metric structure.

## 9. Order: cái mà complex numbers sẽ không giữ nguyên theo cùng cách

Real numbers có total order:

```math
x<y,\quad x=y,\quad x>y
```

với exactly one case true.

Order tương thích với addition và positive multiplication.

Nhiều inequalities dựa trên structure này.

Complex numbers không có natural total order tương thích với field operations theo cách reals có. Vì vậy khi mở rộng number system, ta gain solutions/rotation structure nhưng không giữ mọi property cũ.

Đây là lesson tổng quát: extension thường giải quyết một limitation nhưng đổi set of structures available.

## 10. Complex numbers: closure cho polynomial equations và rotation

Số phức (complex numbers / 복소수):

```math
z=a+bi,
\qquad i^2=-1.
```

Ban đầu `i` giúp equation

```math
x^2+1=0
```

có solutions `±i`.

Nhưng complex numbers mạnh hơn vai trò “chứa square root của -1”.

Trên complex plane, `a` và `b` là two coordinates. Magnitude:

```math
|z|=\sqrt{a^2+b^2}.
```

Polar form:

```math
z=re^{i\theta}.
```

Euler relation:

```math
e^{i\theta}=\cos\theta+i\sin\theta.
```

Multiplication của complex numbers cộng angles và nhân magnitudes. Vì vậy multiplication tự encode rotation + scaling.

Đây là reason complex numbers xuất hiện tự nhiên trong Fourier analysis, wave models, AC circuits và control systems.

## 11. Fundamental Theorem of Algebra: vì sao C là một natural endpoint cho polynomial roots

Một polynomial nonconstant với complex coefficients có ít nhất một complex root. Từ đó polynomial degree `n` factor thành `n` linear factors khi multiplicity được count.

Conceptually, `C` là algebraically closed: polynomial equations không buộc ta tiếp tục mở rộng theo cùng kiểu như `R` phải mở sang `C` cho `x²+1=0`.

Không cần proof theorem này ở chapter foundations; proof cần complex analysis/algebra sâu hơn. Nhưng theorem giải thích vị trí đặc biệt của complex numbers trong algebra.

## 12. Numeral system không phải number system

Cần phân biệt:

**Number system**: mathematical objects như integers/reals.

**Numeral system**: cách viết cùng quantity bằng digits và base.

`11₁₀`, `1011₂`, `B₁₆` represent cùng integer.

Representation thay đổi, object không đổi.

Đây là cùng mental model đã gặp ở coordinate systems và basis changes.

## 13. Positional notation

Trong base `b`:

```math
(d_nd_{n-1}\ldots d_0)_b
=
\sum_{k=0}^{n}d_kb^k.
```

Fractional digits dùng negative powers:

```math
0.101_2
=
2^{-1}+2^{-3}
=0.625_{10}.
```

Binary base 2 phù hợp digital representation vì hardware dễ distinguish two stable state ranges. Nhưng binary không biến quantity thành “loại số khác”.

## 14. Finite representation: khi mathematics gặp machine limits

Mathematical integer là unbounded abstraction. Machine integer có fixed or managed representation.

Signed 32-bit range thường:

```math
-2^{31}\le x\le2^{31}-1.
```

Overflow semantics phụ thuộc language/runtime.

Mathematical real có infinite precision abstraction; floating point chỉ represent finite subset.

IEEE-style floating point roughly:

```math
(-1)^s\times m\times2^e.
```

Do finite significand, operation được rounded.

## 15. Vì sao 0.1 thường không exact trong binary

Decimal `0.1` tương tự `1/10`.

Một rational có finite base-`b` expansion chỉ khi denominator sau reduction có prime factors nằm trong base.

Base 10 có prime factors 2 và 5, nên `1/10` finite decimal.

Base 2 chỉ có factor 2; denominator 10 còn factor 5, nên expansion binary repeats.

Vì vậy error không phải bug của floating point; nó là consequence của finite positional representation.

## 16. Equality trong numerical computing

Sau floating operations, exact comparison có thể fail:

```text
0.1 + 0.2 == 0.3
```

không luôn true trong binary floating arithmetic.

Nhưng solution cũng không phải dùng một `epsilon` magic cho mọi scale.

Absolute tolerance thích hợp gần zero; relative tolerance hữu ích ở different magnitudes. Numerical comparison phải match problem scale và error model.

## 17. Density và cardinality: hai notions “có nhiều số” khác nhau

Rationals và reals đều dense: giữa hai numbers khác nhau luôn có number khác.

Nhưng cardinality khác. `Q` countable; `R` uncountable.

Do đó “dense” không đồng nghĩa “có cùng size theo set theory”.

Đây là một trong những điểm làm infinite sets khác finite intuition.

## 18. Number systems và algebraic structures

Integers dưới addition tạo group; rationals/reals/complex numbers với addition/multiplication tạo fields.

Không cần học abstract algebra trước để dùng numbers, nhưng viewpoint này giải thích vì sao rules algebra giống nhau trên `Q`, `R`, `C`: chúng share field axioms.

Khi một operation không valid trong structure — ví dụ division by zero — không có symbolic trick nào cứu được.

## 19. Physics, AI và Finance connections

Physics dùng real numbers cho continuous measurements và complex numbers cho oscillatory state representations.

AI dùng floating-point approximations của real-valued linear algebra; precision format (`FP32`, `FP16`, etc.) ảnh hưởng stability và performance.

Finance dùng decimals/currency representations nơi binary floating point có thể không phù hợp cho exact monetary accounting; fixed-point/decimal arithmetic thường phù hợp hơn cho ledger semantics.

Điểm chung là **mathematical number domain** và **machine representation** phải được chọn riêng.

## Mental Model

> Một number system là một universe được mở rộng để giữ những operations hoặc limits ta cần. Natural numbers giữ counting; integers thêm additive inverse; rationals thêm division; reals thêm completeness; complex numbers thêm algebraic closure cho polynomial roots và geometry của rotation. Còn binary/decimal/floating-point chỉ là representations hữu hạn của những objects đó trong một computational model.

## Common Misconceptions

Irrational không nghĩa random. Dense không nghĩa uncountable. Complex không phải “fake numbers”; chúng là extension nhất quán với rich geometry. Decimal/binary là representation, không phải different quantities. Mathematical real numbers không giống floating-point numbers. Dùng tolerance không có nghĩa mọi approximate equality đều hợp lệ; tolerance phải xuất phát từ scale và error model.