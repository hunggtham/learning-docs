# Đa thức và phân tích nhân tử: structure, roots và approximation

Đa thức (polynomial / 다항식) thường được gặp đầu tiên như biểu thức

```math
P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,
```

nhưng cách nhìn hữu ích hơn là: polynomial là một class functions có **algebraic structure rất giàu nhưng vẫn dễ tính toán**. Chúng cộng, nhân, đạo hàm, tích phân và approximate tốt; roots của chúng encode geometry; factorization làm lộ structure ẩn; còn trong numerical methods và computer algebra, representation của polynomial ảnh hưởng trực tiếp tới stability và cost.

## 1. Polynomial là gì và vì sao nó đặc biệt?

Một polynomial một biến có finite sum của nonnegative integer powers:

```math
P(x)=\sum_{k=0}^n a_kx^k.
```

Bậc (degree / 차수) là largest `k` sao cho `a_k\ne0`.

Ví dụ

```math
P(x)=3x^4-2x+1
```

có degree 4.

Polynomial đặc biệt vì nhiều operations giữ ta ở cùng family:

- tổng hai polynomials vẫn là polynomial;
- product vẫn là polynomial;
- derivative vẫn là polynomial;
- antiderivative cũng là polynomial cộng constant.

Closure này làm polynomial trở thành “working language” tự nhiên của algebra và calculus.

## 2. Leading term và large-scale behavior

Với

```math
P(x)=a_nx^n+\cdots+a_0,
```

khi `|x|` rất lớn, term `a_nx^n` thường dominate lower-order terms.

Do đó end behavior phụ thuộc mạnh vào degree parity và sign của `a_n`.

Nếu `n` chẵn, hai ends đi cùng direction. Nếu `n` lẻ, hai ends đi opposite directions.

Đây là first asymptotic reasoning: không cần biết mọi coefficient để biết large-scale shape.

## 3. Roots là nơi polynomial mất output

Root/zero `r` thỏa

```math
P(r)=0.
```

Graphically, đó là nơi graph gặp x-axis. Algebraically, root liên hệ trực tiếp với factor.

Factor theorem:

```math
P(r)=0
\iff
(x-r)\mid P(x).
```

Tại sao?

Polynomial division cho

```math
P(x)=(x-r)Q(x)+R,
```

vì divisor degree 1 nên remainder là constant. Thay `x=r`:

```math
P(r)=R.
```

Vì thế `P(r)=0` khi và chỉ khi remainder bằng 0, tức `(x-r)` là exact factor.

Factor theorem không phải mẹo; nó là special case của polynomial division.

## 4. Zero-product property biến factors thành roots

Nếu

```math
P(x)=(x-2)(x-3),
```

thì solving

```math
P(x)=0
```

trở thành

```math
(x-2)(x-3)=0.
```

Trong real/complex numbers, product bằng zero khi ít nhất một factor bằng zero, nên

```math
x=2\quad\text{hoặc}\quad x=3.
```

Factorization là powerful vì nó đổi một global expression thành local conditions trên factors.

## 5. Multiplicity nói gì về local geometry?

Nếu

```math
P(x)=(x-r)^mQ(x),\qquad Q(r)\ne0,
```

thì `r` có multiplicity `m`.

Nếu `m` odd, sign thường đổi khi đi qua `r`, nên graph cross x-axis.

Nếu `m` even, sign thường giữ nguyên, nên graph touch rồi turn.

Ví dụ:

```math
P(x)=(x-1)^2(x+2).
```

Root `x=1` multiplicity 2, root `x=-2` multiplicity 1.

Calculus giải thích sâu hơn: high multiplicity đồng nghĩa nhiều derivatives đầu tiên cũng vanish tại root.

## 6. Cùng polynomial, nhiều representations

Một trong những bài học quan trọng nhất của algebra là **representation choice matters**.

### Expanded form

```math
ax^2+bx+c
```

làm coefficients và algebraic combination rõ.

### Factored form

```math
a(x-r_1)(x-r_2)
```

làm roots và sign structure rõ.

### Vertex form

```math
a(x-h)^2+k
```

làm extremum và geometry rõ.

Cùng một object nhưng mỗi form trả lời một loại câu hỏi khác nhau. Đây là pattern lặp lại trong linear algebra, Fourier analysis và numerical computing: đổi basis/representation để làm structure trở nên nhìn thấy được.

## 7. Completing the square là representation change

Với quadratic

```math
x^2+6x+5,
```

ta thêm và bớt `9`:

```math
x^2+6x+9-9+5
```

```math
=(x+3)^2-4.
```

Expanded form giúp đọc coefficients; vertex form ngay lập tức cho vertex `(-3,-4)`.

Operation này cũng là nền của quadratic formula và Gaussian expressions trong probability.

## 8. Polynomial division và remainder theorem

Giống integer division,

```math
P(x)=D(x)Q(x)+R(x),
```

với

```math
\deg R<\deg D.
```

Khi `D(x)=x-r`, remainder là constant và bằng `P(r)`.

Điều này nối evaluation với divisibility.

Trong computer algebra, polynomial division là primitive operation phía sau gcd algorithms, symbolic simplification và factorization methods.

## 9. Fundamental Theorem of Algebra: vì sao complex numbers đủ?

Fundamental Theorem of Algebra nói rằng mọi nonconstant polynomial degree `n` với complex coefficients có exactly `n` complex roots counting multiplicity.

Nói trực giác: complex numbers tạo một number system đủ lớn để polynomial equations không cần mở rộng thêm một class numbers mới chỉ để tìm roots.

Ví dụ

```math
x^2+1=0
```

không có real root nhưng có

```math
x=\pm i.
```

Vì vậy complex numbers không phải appendage kỳ lạ; chúng hoàn thiện algebra của polynomial roots.

## 10. Vieta relations: roots và coefficients nói cùng một story

Nếu

```math
ax^2+bx+c=a(x-r_1)(x-r_2),
```

khai triển:

```math
ax^2-a(r_1+r_2)x+ar_1r_2.
```

So coefficients:

```math
r_1+r_2=-\frac ba,
```

```math
r_1r_2=\frac ca.
```

Vieta's formulas cho thấy coefficients và roots chỉ là hai coordinate systems khác nhau của cùng polynomial structure.

## 11. Worked example: chọn representation đúng

Xét

```math
P(x)=x^2-6x+8.
```

Muốn tìm roots, factorization phù hợp:

```math
P(x)=(x-2)(x-4).
```

Roots: `2,4`.

Muốn tìm vertex, complete square:

```math
P(x)=(x-3)^2-1.
```

Vertex: `(3,-1)`.

Muốn evaluate tại many `x`, expanded/Horner representation có thể thuận tiện hơn.

Không có form “tốt nhất” tuyệt đối; form tốt phụ thuộc question.

## 12. Polynomial interpolation: fit data bằng polynomial có giới hạn gì?

Qua `n+1` points có distinct x-values, tồn tại unique polynomial degree at most `n` đi qua tất cả points.

Điều này nghe rất mạnh, nhưng exact interpolation không đồng nghĩa good model.

High-degree global polynomial có thể oscillate mạnh giữa sample points — Runge phenomenon. Data noise cũng có thể khiến exact fit overfit.

Vì vậy numerical work thường dùng splines, low-degree local approximation hoặc regularized fitting thay vì “degree càng cao càng tốt”.

## 13. Taylor polynomial: polynomial như local language của smooth functions

Nếu `f` smooth quanh `a`, Taylor expansion bắt đầu:

```math
f(x)
\approx
f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2+\cdots.
```

Coefficient được chọn để polynomial match derivatives của `f` tại `a`.

Đây là lý do polynomial xuất hiện khắp calculus và numerical methods: gần một point, nhiều smooth functions behave như polynomial đến một order nhất định.

Ví dụ quanh `0`:

```math
\sin x\approx x-\frac{x^3}{3!}+\frac{x^5}{5!}.
```

## 14. Horner's method: algebraic form trở thành algorithm

Thay vì evaluate

```math
P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0
```

bằng cách tính từng power riêng, viết nested:

```math
P(x)=(((a_nx+a_{n-1})x+a_{n-2})x+\cdots)+a_0.
```

Horner's method dùng `O(n)` multiplications/additions và giảm intermediate work.

Ví dụ

```math
2x^3-3x^2+4x-5
```

thành

```math
((2x-3)x+4)x-5.
```

Đây là một connection trực tiếp giữa symbolic representation và computational efficiency.

## 15. Numerical conditioning của roots

Không phải mọi root đều numerically stable. Small perturbations coefficients có thể gây large changes roots, đặc biệt với multiple hoặc clustered roots.

Điều này quan trọng vì symbolic identity và numerical computation là hai tầng khác nhau. Một exact polynomial theorem không guarantee floating-point root-finding sẽ easy.

Companion matrices còn cho phép chuyển polynomial-root problem thành eigenvalue problem, nối algebra với linear algebra.

## 16. Polynomials trong signals, control và approximation

Transfer functions thường có numerator/denominator polynomials. Roots của denominator là poles, liên quan stability của dynamic system.

Characteristic polynomial

```math
\det(A-\lambda I)
```

có roots là eigenvalues. Vì vậy polynomial factorization kết nối trực tiếp với dynamics, control và linear algebra.

## 17. Failure modes khi factorization

### Không phải polynomial nào cũng factor đẹp trên integers

Ví dụ

```math
x^2-2
```

không factor thành linear factors với rational coefficients, nhưng factor trên reals:

```math
(x-\sqrt2)(x+\sqrt2).
```

### Repeated roots dễ bị bỏ sót nếu chỉ nhìn sign change

Even multiplicity roots có thể touch axis mà không đổi sign.

### Exact symbolic factorization và numerical factorization khác nhau

Trong high degree hoặc floating coefficients, “factor” có thể nhạy với noise và tolerance.

## Applications và connections

**Computer Science:** Horner evaluation, symbolic algebra, polynomial hashing và coding theory.

**Physics:** characteristic equations, local approximations và perturbation models.

**AI:** polynomial features, kernel approximations và Taylor-based analysis.

**Finance:** local approximations của pricing/risk functions và polynomial regression, nhưng high-degree fits cần cảnh giác overfitting.

## Mental Model

> Polynomial là một object có nhiều representations. Expanded coefficients, factors, roots, vertex form và Taylor form không phải các chủ đề riêng; chúng là những “camera angles” khác nhau. Algebra mạnh lên khi ta biết đổi representation để structure cần thiết trở nên nhìn thấy được.

## Common Misconceptions

**Factorization chỉ là technique để solve quadratics.** Không; nó bộc lộ root, multiplicity và structural decomposition.

**Degree cao luôn fit tốt hơn.** Không; interpolation có thể oscillate và overfit.

**Root là property tách khỏi number system.** Không; factorization phụ thuộc coefficient/domain field đang dùng.

**Polynomial evaluation chỉ là thay số.** Trong computation, representation như Horner form ảnh hưởng cost và numerical behavior.
