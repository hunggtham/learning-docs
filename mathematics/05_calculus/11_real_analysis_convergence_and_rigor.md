# Real analysis: giới hạn, hội tụ và nền tảng chặt chẽ của calculus

Calculus thường bắt đầu bằng trực giác: một quantity “tiến gần” một value, một curve “trơn”, hoặc một infinite sum “có vẻ ổn định”. **Real analysis (실해석학)** hỏi câu khó hơn: chính xác điều đó có nghĩa gì, và ta chứng minh nó như thế nào mà không dựa vào hình vẽ hay cảm giác?

Mục tiêu của real analysis không phải làm calculus khó hơn. Nó làm rõ những assumptions ẩn phía sau derivative, integral, infinite series, approximation và numerical computation. Khi hiểu analysis, ta biết khi nào một phép đổi limit với integral là hợp lệ, khi nào một sequence thật sự hội tụ, và tại sao một theorem cần các conditions cụ thể.

## Completeness của real numbers

Điểm khác biệt quan trọng giữa rational numbers `Q` và real numbers `R` là **completeness (완비성)**.

Ví dụ sequence các rational approximations của `sqrt(2)` có thể tiến gần một limit không thuộc `Q`. Trong `R`, limit đó tồn tại.

Một formulation quan trọng là least upper bound property: mọi nonempty subset của `R` bị chặn trên đều có supremum trong `R`.

Nếu

```math
S=\{x\in\mathbb R:x^2<2\},
```

thì `S` bị chặn trên và supremum của nó là `sqrt(2)`.

Completeness là nền móng của rất nhiều convergence theorems.

## Sequence và convergence

Một sequence `(a_n)` hội tụ về `L` nếu

```math
\forall \varepsilon>0,\ \exists N\in\mathbb N
```

sao cho

```math
n\ge N\Rightarrow |a_n-L|<\varepsilon.
```

Ý tưởng là ta có thể yêu cầu sai số nhỏ tùy ý; từ một index đủ lớn trở đi sequence luôn nằm trong tolerance đó.

Ví dụ

```math
a_n=\frac1n.
```

Muốn `|1/n|<ε`, chỉ cần chọn `N>1/ε`.

Định nghĩa epsilon này biến câu “1/n tiến về 0” thành một claim có thể chứng minh.

## Bounded và monotone sequence

Nếu sequence tăng dần và bị chặn trên, nó hội tụ. Tương tự, sequence giảm dần và bị chặn dưới cũng hội tụ.

Đây là **monotone convergence theorem** cho sequences và là một biểu hiện trực tiếp của completeness.

Ví dụ iterative algorithms đôi khi tạo sequence objective values giảm dần và bị chặn dưới bởi 0. Điều đó cho biết values hội tụ, dù chưa đủ để kết luận parameters hội tụ tới global optimum.

## Cauchy sequence

Một sequence là Cauchy nếu các terms cuối cùng gần nhau:

```math
\forall\varepsilon>0,\exists N:\ m,n\ge N\Rightarrow |a_m-a_n|<\varepsilon.
```

Điểm hay là định nghĩa không cần biết trước limit là gì.

Trong `R`, mọi Cauchy sequence đều hội tụ. Đây là một dạng khác của completeness.

Trong numerical computation, Cauchy-like stopping criteria rất tự nhiên: nếu successive iterates thay đổi ngày càng nhỏ, ta nghi ngờ algorithm đang ổn định. Tuy nhiên “successive difference nhỏ” trong finite computation không tự động chứng minh convergence về nghiệm đúng; conditioning và error analysis vẫn quan trọng.

## Subsequences và Bolzano–Weierstrass

Một subsequence chọn một số terms theo thứ tự tăng của indices.

Bolzano–Weierstrass theorem nói rằng mọi bounded sequence trong `R^n` đều có một convergent subsequence.

Theorem này quan trọng trong optimization. Nếu iterates nằm trong một bounded region, ta có thể tìm convergent subsequences; từ đó phân tích cluster points và stationary conditions.

## Limit superior và limit inferior

Không phải sequence nào cũng hội tụ. Ví dụ

```math
a_n=(-1)^n
```

oscillates giữa `-1` và `1`.

Ta có thể mô tả long-term upper và lower behavior bằng

```math
\limsup a_n,
```

và

```math
\liminf a_n.
```

Nếu hai values bằng nhau và finite, sequence hội tụ về common value đó.

## Continuity theo epsilon-delta

Function `f` continuous tại `x_0` nếu

```math
\forall\varepsilon>0,\exists\delta>0:
|x-x_0|<\delta\Rightarrow |f(x)-f(x_0)|<\varepsilon.
```

`ε` là tolerance output; `δ` là tolerance input đủ để đảm bảo output nằm trong tolerance mong muốn.

Continuity có thể hiểu là small input perturbations tạo small output perturbations, nhưng epsilon-delta làm phát biểu này precise.

## Sequential characterization của continuity

Một function continuous tại `x` khi và chỉ khi mọi sequence `x_n→x` đều thỏa

```math
f(x_n)\to f(x).
```

Cách nhìn này đặc biệt hữu ích vì nhiều proofs về continuity có thể chuyển thành proofs về sequences.

## Intermediate Value Theorem

Nếu `f` continuous trên `[a,b]` và một value `y` nằm giữa `f(a)` và `f(b)`, thì tồn tại `c∈[a,b]` sao cho

```math
f(c)=y.
```

Root-finding methods như bisection dựa trên structure này. Nếu `f(a)` và `f(b)` trái dấu, continuity đảm bảo có ít nhất một root giữa chúng.

## Extreme Value Theorem

Nếu `f` continuous trên compact interval `[a,b]`, thì `f` đạt maximum và minimum trên interval đó.

Không chỉ tồn tại supremum abstract; có điểm thực sự đạt nó.

Điều này cho thấy vì sao compactness quan trọng trong optimization: continuity cộng compact feasible set thường cho existence của optimum.

## Compactness

Trong `R^n`, Heine–Borel theorem cho biết một set compact khi và chỉ khi nó closed và bounded.

Compactness có thể hình dung là “không chạy ra infinity và không bỏ mất boundary limit points”.

Nhiều theorem mạnh trở nên đúng trên compact sets: continuous functions uniformly continuous, extrema tồn tại, mọi sequence có convergent subsequence nằm trong set.

## Pointwise và uniform convergence

Cho sequence functions `f_n(x)`.

Pointwise convergence nghĩa là với mỗi `x` cố định,

```math
f_n(x)\to f(x).
```

Nhưng tốc độ convergence có thể khác rất nhiều tùy `x`.

Uniform convergence yêu cầu một `N` chung hoạt động cho toàn domain:

```math
\forall\varepsilon>0,\exists N:
n\ge N\Rightarrow |f_n(x)-f(x)|<\varepsilon
```

cho mọi `x` trong domain.

Uniform convergence mạnh hơn và thường cho phép bảo toàn continuity khi lấy limit.

## Vì sao pointwise convergence có thể gây bất ngờ

Xét

```math
f_n(x)=x^n
```

trên `[0,1]`.

Với `0≤x<1`, `x^n→0`; tại `x=1`, value luôn bằng 1. Limit function là

```math
f(x)=
\begin{cases}
0,&0\le x<1\\
1,&x=1.
\end{cases}
```

Mỗi `f_n` continuous nhưng limit function không continuous. Convergence chỉ pointwise, không uniform.

Đây là ví dụ cho thấy không thể tùy tiện chuyển mọi property qua limit.

## Differentiability mạnh hơn continuity

Nếu `f` differentiable tại một điểm thì nó continuous tại đó. Converse không đúng.

`f(x)=|x|` continuous tại 0 nhưng không differentiable vì left derivative và right derivative khác nhau.

Trong nhiều chiều, differentiability còn mạnh hơn việc tất cả partial derivatives tồn tại. Ta cần một single linear map approximates function theo mọi direction cùng lúc.

## Mean Value Theorem

Nếu `f` continuous trên `[a,b]` và differentiable trên `(a,b)`, tồn tại `c` sao cho

```math
f'(c)=\frac{f(b)-f(a)}{b-a}.
```

Theorem nối local derivative với global change. Nhiều error bounds và uniqueness arguments dựa trên nó.

Ví dụ nếu `|f'(x)|≤M`, thì

```math
|f(x)-f(y)|\le M|x-y|.
```

Đây là một Lipschitz-type bound.

## Riemann integral và partitions

Riemann integration chia interval thành subintervals và xấp xỉ area bằng sums.

Nếu partition là

```math
a=x_0<x_1<\cdots<x_n=b,
```

Riemann sum có dạng

```math
\sum_{i=1}^{n} f(\xi_i)(x_i-x_{i-1}).
```

Integral tồn tại khi các sums hội tụ về cùng value khi mesh của partition tiến về 0, bất kể sample points `ξ_i` được chọn hợp lệ như thế nào.

Continuous functions trên closed bounded interval là Riemann integrable.

## Fundamental Theorem of Calculus dưới góc nhìn analysis

Nếu `f` continuous và

```math
F(x)=\int_a^x f(t)dt,
```

thì

```math
F'(x)=f(x).
```

Đây không chỉ là formula. Nó khẳng định hai processes tưởng khác nhau — local rate và global accumulation — là inverses theo một nghĩa precise dưới appropriate conditions.

## Interchanging limits, derivatives và integrals

Trong applied math ta thường muốn viết

```math
\lim_n\int f_n=\int\lim_n f_n
```

hoặc

```math
\frac{d}{dx}\int f(x,t)dt
=\int\frac{\partial f}{\partial x}(x,t)dt.
```

Các operations này không tự động hợp lệ. Cần conditions như uniform convergence hoặc, trong measure theory, dominated convergence conditions.

Analysis dạy một principle quan trọng: trước khi đổi thứ tự two limiting operations, phải hỏi theorem nào cho phép.

## Normed spaces và convergence không chỉ trong R

Trong vector space có norm `||·||`, ta định nghĩa

```math
x_n\to x
```

nếu

```math
\|x_n-x\|\to0.
```

Điều này mở đường tới functional analysis, optimization và numerical linear algebra. Một algorithm có thể hội tụ theo Euclidean norm, operator norm hoặc function norm tùy problem.

## Mental Model

Real analysis là “type system” cho các thao tác vô hạn. Nó buộc ta xác định domain, notion of distance, convergence mode và assumptions trước khi chuyển limits, derivatives hay integrals qua nhau. Calculus cho ta powerful operations; analysis cho biết operations đó hợp lệ ở đâu.

## Common Misconceptions

“Hội tụ” không chỉ có một loại. Sequence numbers, sequence functions và random variables có nhiều notions of convergence khác nhau. Pointwise convergence cũng không đủ để bảo toàn mọi property.

Một misconception khác là nghĩ epsilon-delta chỉ là formalism không thực dụng. Thực ra robust numerical bounds, stability, conditioning và error guarantees đều dựa trên cùng tư duy: input perturbation bao nhiêu thì output thay đổi bao nhiêu.

## Liên kết kiến thức

Chapter này làm nền chặt chẽ cho [Limits and continuity](./00_limits_and_continuity.md), [Infinite series](./07_infinite_series_power_series_and_convergence.md), [Numerical methods and error](../08_optimization_numerical/02_numerical_methods_and_error.md), [Optimization](../08_optimization_numerical/00_optimization.md) và probability theory ở mức sâu hơn.