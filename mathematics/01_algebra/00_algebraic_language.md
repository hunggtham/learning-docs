# Ngôn ngữ đại số: biểu diễn cấu trúc bằng ký hiệu

Đại số (algebra / 대수학) bắt đầu khi ta ngừng giải từng bài toán bằng số cụ thể và chuyển sang reasoning trên **structure**. Ký hiệu cho phép ta giữ một quantity chưa biết, một parameter có thể thay đổi, hoặc một pattern áp dụng cho cả family problems.

Ví dụ thay vì xử lý riêng “3 hộp, mỗi hộp 5 món”, “3 hộp, mỗi hộp 8 món”, ta viết

```math
3x.
```

Ký hiệu `x` không làm bài toán trừu tượng vô ích; nó loại chi tiết không cần thiết để giữ relationship cần reasoning.

## 1. Variable có nhiều vai trò

Biến (variable / 변수) không đồng nghĩa “ẩn số”.

Trong

```math
x+3=10,
```

`x` là unknown cần solve.

Trong

```math
y=2x+1,
```

`x` là input và `y` phụ thuộc vào `x`.

Trong

```math
f(x;\theta),
```

`x` có thể là input còn `\theta` là parameter xác định member trong function family.

Trong probability, `X` có thể là random variable. Trong programming, variable là một binding/reference trong execution model.

Các usages liên quan qua idea “symbol đại diện quantity”, nhưng semantics khác nhau. Vì vậy context và domain phải được nói rõ.

## 2. Domain là part of algebra, không phải footnote

Một symbol chỉ meaningful cùng universe values nó được phép nhận.

Nếu `x` là số người:

```math
x\in\mathbb Z_{\ge0}
```

có thể hợp lý.

Nếu `x` là continuous time:

```math
x\in\mathbb R_{\ge0}.
```

Equation

```math
x^2=2
```

không có rational solution nhưng có real solutions.

Equation

```math
x^2=-1
```

không có real solution nhưng có complex solutions.

Do đó solution set không tồn tại độc lập với domain.

## 3. Expression, equation, identity và function khác nhau

Biểu thức (expression / 식)

```math
3x+2
```

là object tạo value khi `x` được gán.

Equation

```math
3x+2=14
```

là constraint; nó đúng chỉ cho một số values.

Identity

```math
(a+b)^2=a^2+2ab+b^2
```

là equality đúng cho mọi values trong domain thích hợp.

Function

```math
f(x)=3x+2
```

là mapping, không chỉ expression bên phải.

Phân biệt này quan trọng vì cách reasoning khác nhau: expression được simplify/evaluate, equation được solve, identity được prove, function được analyze như mapping.

## 4. Dấu bằng là statement về sameness

Dấu `=` không nghĩa “bây giờ tính kết quả”. Nó khẳng định hai expressions represent cùng value/object trong context.

Từ

```math
x+5=12,
```

trừ 5 hai vế:

```math
x+5-5=12-5
```

cho

```math
x=7.
```

Cơ chế sâu hơn “cân hai vế” là: ta apply cùng reversible transformation

```math
T(t)=t-5
```

lên cả hai sides.

Khi transformation one-to-one trên domain đang xét, equality relation được preserve theo hai chiều.

## 5. Equivalence transformation vs implication-only transformation

Không phải algebraic manipulation nào cũng reversible.

Ví dụ

```math
x=2
```

implies

```math
x^2=4,
```

nhưng reverse không đúng vì `x=-2` cũng thỏa squared equation.

Vì vậy squaring có thể **mở rộng** solution set.

Chia hai vế cho expression có thể **thu hẹp** solution set nếu expression có thể bằng zero.

Ví dụ:

```math
x^2=x.
```

Chia cho `x` cho `x=1`, nhưng làm mất root `x=0`.

Cách structure-preserving hơn:

```math
x^2-x=0
```

```math
x(x-1)=0,
```

nên

```math
x=0\quad\text{hoặc}\quad x=1.
```

Khi manipulate equation, câu hỏi cần hỏi là:

> Bước này bảo toàn equivalence hay chỉ tạo implication một chiều?

## 6. Arithmetic laws là rules của structure

Các law nền:

Commutative:

```math
a+b=b+a,
\qquad
ab=ba.
```

Associative:

```math
(a+b)+c=a+(b+c),
```

```math
(ab)c=a(bc).
```

Distributive:

```math
a(b+c)=ab+ac.
```

Identity:

```math
a+0=a,
\qquad
a\cdot1=a.
```

Inverse:

```math
a+(-a)=0,
```

và với `a\ne0`:

```math
a\cdot a^{-1}=1.
```

Những laws này giải thích tại sao symbolic transformations hợp lệ. Abstract algebra sau này chỉ formalize structures có một subset các laws như vậy.

## 7. Distributive law: bridge giữa multiplication và addition

```math
a(b+c)=ab+ac.
```

Hình học: rectangle height `a`, width `b+c` có area bằng tổng area hai rectangles widths `b,c`.

Algebraically, law cho phép chuyển giữa two representations:

```text
factored form ↔ expanded form
```

Hai forms bằng nhau nhưng expose different structure.

Expanded form tốt cho collecting coefficients. Factored form làm zeros/common factors rõ hơn.

Đại số thường là **chọn representation phù hợp với câu hỏi**, không phải luôn “rút gọn nhất”.

## 8. Factorization là reverse engineering structure

Từ

```math
ab+ac
```

nhận ra common factor `a`:

```math
ab+ac=a(b+c).
```

Với polynomial:

```math
x^2-5x+6=(x-2)(x-3).
```

Factored form expose roots ngay.

Cùng object có thể có nhiều useful forms:

```text
expanded
factored
vertex form
matrix form
log form
```

Transformation giữa representations là central skill xuyên suốt Mathematics Library.

## 9. Exponent laws không phải bảng cần thuộc riêng

Với integer positive exponents:

```math
a^m a^n=a^{m+n}
```

vì ta concatenate `m` factors với `n` factors.

Division:

```math
\frac{a^m}{a^n}=a^{m-n}
```

khi `a\ne0`.

Muốn law nhất quán khi `m=n`:

```math
\frac{a^m}{a^m}=1=a^0,
```

nên

```math
a^0=1.
```

Muốn law tiếp tục đúng với negative exponents:

```math
a^{-n}=\frac1{a^n}.
```

Fractional exponents kết nối exponentiation với roots:

```math
a^{1/n}=\sqrt[n]{a}
```

trong domain thích hợp.

Một rule tốt nên được nhìn như **extension chosen to preserve structural consistency**.

## 10. Units là một dạng algebra

Nếu

```math
v=\frac dt,
```

với distance meter và time second, unit:

```text
m/s
```

behaves algebraically.

Nếu

```math
a=\frac{v}{t},
```

unit:

```text
m/s².
```

Dimensional analysis có thể detect impossible formulas trước khi numeric calculation bắt đầu.

Ví dụ cộng

```text
3 meters + 5 seconds
```

không có physical meaning trong ordinary model dù numbers `3+5` tính được.

Đây là reminder rằng symbolic algebra phải respect semantic type của quantities.

## 11. Algebraic rearrangement là solving for perspective

Formula

```math
v=\frac dt
```

có thể rearrange:

```math
d=vt,
```

hoặc

```math
t=\frac dv
```

với `v\ne0`.

Ta không tạo laws mới; ta thay perspective xem quantity nào là unknown.

Trong engineering, finance và software capacity planning, cùng một model được rearrange tùy quantity cần estimate.

## 12. Parameters, constants và variables

Trong

```math
y=ax+b,
```

`x` là independent variable, `y` dependent variable, `a,b` là parameters xác định line.

Nếu đang fit regression, `a,b` là unknown parameters cần estimate từ data.

Nếu đã deploy model, chúng có thể được coi constants trong prediction.

Vai trò symbol phụ thuộc phase của problem.

## 13. Algebra và function composition

Expression nesting như

```math
\sqrt{3x+1}
```

có thể decompose thành functions:

```text
x
→ 3x+1
→ sqrt(.)
```

Đây là composition viewpoint.

Khi solve equation hoặc differentiate, nhìn expression tree giúp biết operation order và inverse/chain rules phải apply theo chiều nào.

Compiler cũng parse source code thành abstract syntax tree. Symbolic algebra system làm transformations trên trees theo rules có điều kiện.

## 14. Algebra và computational graphs

Neural network, spreadsheet formula, differentiable program đều có thể nhìn như computational graph.

Ví dụ:

```math
z=(ax+b)^2
```

có graph:

```text
x → multiply a → add b → square → z
```

Forward evaluation truyền values; reverse-mode AD truyền sensitivities ngược graph.

Algebraic structure vì vậy nối trực tiếp tới automatic differentiation.

## 15. Modeling: ký hiệu chỉ hữu ích nếu semantics rõ

Giả sử total latency:

```math
T=T_{network}+T_{server}+T_{db}.
```

Rearrange:

```math
T_{db}=T-T_{network}-T_{server}.
```

Algebra đúng. Nhưng model có thể sai nếu components overlap, execute concurrently, hoặc measurement definitions khác nhau.

Mathematics không tự đảm bảo decomposition phản ánh system thực.

Luôn tách:

```text
model assumptions
→ algebraic consequences
→ measurements / implementation
```

## 16. Symbolic simplification có thể gây numerical problems

Hai expressions mathematically equal có thể có numerical behavior khác nhau.

Ví dụ near `x=0`, expression

```math
\frac{1-\cos x}{x^2}
```

có thể chịu cancellation trong floating point.

Equivalent identities/series có thể evaluate ổn định hơn.

Vì vậy “algebraically simpler” không luôn “numerically better”. Numerical Methods sẽ formalize issue này bằng conditioning/stability.

## 17. Common pattern: preserve invariant while changing representation

Đại số, row reduction, coordinate changes, Fourier transform, logarithm và probability reparameterization đều share pattern:

```text
same underlying object/problem
→ different representation
→ desired structure becomes easier to see
```

Đây là một trong những mental models quan trọng nhất của toàn Mathematics Library.

## Worked Example: solve nhưng track domain

Giải

```math
\frac{x+1}{x-2}=3.
```

Trước hết domain:

```math
x\ne2.
```

Nhân hai vế với `x-2` hợp lệ trên domain này:

```math
x+1=3(x-2).
```

Expand:

```math
x+1=3x-6.
```

Rearrange:

```math
7=2x
```

nên

```math
x=\frac72.
```

Candidate thỏa domain, nên valid.

Việc ghi domain trước làm reasoning transparent hơn việc “cross multiply” như một ritual.

## Mental Model

> Algebra là **ngôn ngữ của representation-preserving transformations**. Variables giữ quantities chưa cố định; laws mô tả operations nào preserve structure; factorization, expansion, rearrangement và substitution đổi cách nhìn để pattern cần tìm lộ ra. Algebra mạnh nhất khi ta theo dõi domain, reversibility và semantics thay vì chỉ thao tác symbols.

## Common Misconceptions

Variable không luôn là unknown. `=` không phải nút “tính kết quả”. “Chuyển vế đổi dấu” chỉ là shorthand cho reversible operations. Chia/bình phương/lấy căn hai vế có thể thay solution set. Hai expressions mathematically equivalent không nhất thiết có cùng numerical stability. Simplification chỉ có nghĩa khi domain và semantic units vẫn được tôn trọng.