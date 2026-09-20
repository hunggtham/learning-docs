# Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”

Giải tích (Calculus / 미적분) bắt đầu khi những câu hỏi đơn giản về change và accumulation va vào một vấn đề logic: nhiều quantities ta muốn biết chỉ xuất hiện khi một interval trở nên **cực nhỏ** hoặc khi một process được lặp **cực nhiều lần**.

Vận tốc trung bình trên interval `Δt` là

```math
\frac{\Delta x}{\Delta t}.
```

Nhưng vận tốc **tức thời** tại đúng một thời điểm thì sao? Nếu đặt `Δt=0`, ta chia cho 0. Nếu không đặt bằng 0, ta vẫn chỉ có average trên một interval hữu hạn.

Giới hạn (Limit / 극한) giải quyết đúng khoảng trống đó. Nó cho phép ta nói: “ta không cần đặt interval bằng 0; ta nghiên cứu điều xảy ra khi interval có thể được làm nhỏ tùy ý.”

> Limit không phải phép thế `x=a`. Nó là ngôn ngữ để mô tả behavior khi `x` tiến gần `a` với mức chính xác tùy ý.

## Tại sao “gần” cần definition chính xác?

Trong everyday language, “gần” là mơ hồ. `0.001` có gần 0 không? Với engineering tolerance 1 mm thì có thể gần; với quantum-scale measurement thì không.

Mathematics cần statement không phụ thuộc cảm giác. Khi viết

```math
\lim_{x\to a}f(x)=L,
```

ý nghĩa không phải “`f(x)` trông gần `L` trên graph”, mà là:

> ta có thể yêu cầu output gần `L` đến mức tùy ý, và luôn tìm được một vùng quanh `a` đủ nhỏ để mọi input trong vùng đó tạo output nằm trong tolerance mong muốn.

Đây là một contract giữa **input tolerance** và **output tolerance**.

## Một ví dụ quan trọng: function không cần được định nghĩa tại point

Xét

```math
f(x)=\frac{x^2-1}{x-1}.
```

Tại `x=1`, denominator bằng 0 nên `f(1)` không được định nghĩa.

Nhưng với `x≠1`, factor numerator:

```math
x^2-1=(x-1)(x+1),
```

nên

```math
f(x)=x+1.
```

Khi `x` tiến gần `1`, `x+1` tiến gần `2`. Vì vậy

```math
\lim_{x\to1}f(x)=2.
```

Điểm này rất quan trọng: **limit mô tả neighborhood behavior, không nhất thiết function value tại point**.

Ta thậm chí có thể define lại

```math
f(1)=100
```

mà limit vẫn là `2`, vì một isolated point không thay behavior của nearby values.

## Epsilon–delta: biến “gần” thành contract định lượng

Definition formal của

```math
\lim_{x\to a}f(x)=L
```

là:

> với mọi `ε>0`, tồn tại `δ>0` sao cho nếu

```math
0<|x-a|<\delta,
```

thì

```math
|f(x)-L|<\varepsilon.
```

`ε` đo tolerance ở output. `δ` là tolerance ở input đủ để guarantee output tolerance đó.

Điều kiện `0<|x-a|` loại point `x=a`, vì limit chỉ hỏi behavior quanh point. Nếu function value tại `a` cần tham gia, đó là câu hỏi về continuity.

### Đọc definition như một game

Tưởng tượng một người thách thức chọn bất kỳ `ε>0`, dù cực nhỏ. Nhiệm vụ của ta là đưa ra `δ>0` sao cho mọi `x` thỏa

```math
0<|x-a|<\delta
```

đều buộc `f(x)` nằm trong

```math
(L-\varepsilon,L+\varepsilon).
```

Nếu ta luôn làm được, limit là `L`.

Cách nhìn này giải thích vì sao definition dùng “for every `ε`” trước “there exists `δ`”. Ta không được chọn một tolerance dễ rồi tuyên bố limit tồn tại; phải đáp ứng mọi độ chính xác được yêu cầu.

## Epsilon–delta example đơn giản

Chứng minh

```math
\lim_{x\to3}(2x+1)=7.
```

Ta muốn

```math
|(2x+1)-7|<\varepsilon.
```

Simplify:

```math
|2x-6|=2|x-3|.
```

Muốn expression này nhỏ hơn `ε`, chỉ cần

```math
|x-3|<\frac{\varepsilon}{2}.
```

Vậy chọn

```math
\delta=\frac{\varepsilon}{2}.
```

Khi đó

```math
0<|x-3|<\delta
```

suy ra

```math
|(2x+1)-7|=2|x-3|<2\delta=\varepsilon.
```

Proof này cho thấy epsilon–delta không phải nghi thức formal vô nghĩa. Nó explicit hóa sensitivity giữa input và output.

## Limit laws: tại sao ta không phải chứng minh từ đầu mọi lần?

Nếu

```math
\lim_{x\to a}f(x)=L
```

và

```math
\lim_{x\to a}g(x)=M,
```

thì dưới conditions phù hợp:

```math
\lim_{x\to a}[f(x)+g(x)]=L+M,
```

```math
\lim_{x\to a}f(x)g(x)=LM,
```

và nếu `M≠0`,

```math
\lim_{x\to a}\frac{f(x)}{g(x)}=\frac{L}{M}.
```

Các laws này follow từ epsilon–delta structure. Một khi đã được prove, chúng trở thành reusable building blocks.

Đây là pattern chung của mathematics: formal foundation được xây kỹ để later reasoning có thể dùng theorem thay vì re-prove mọi detail.

## Khi direct substitution đúng?

Nếu `f` continuous tại `a`, thì

```math
\lim_{x\to a}f(x)=f(a).
```

Vì vậy với polynomials, many elementary functions và compositions trong domain hợp lệ, direct substitution thường hoạt động.

Ví dụ

```math
\lim_{x\to2}(x^2+3x)=4+6=10.
```

Nhưng direct substitution không phải definition của limit. Nó là shortcut justified bởi continuity.

Khi substitution cho `0/0`, ta không thể conclude limit là `0/0`; đó là **indeterminate form**, signal rằng cần analyze structure sâu hơn.

## Indeterminate form không phải answer

Xét

```math
\lim_{x\to1}\frac{x^2-1}{x-1}.
```

Substitution cho

```math
\frac00.
```

Nhưng `0/0` không phải value. Nó nói numerator và denominator đều vanish nên relative rates matter.

Factorization cho limit `2`.

Một expression khác,

```math
\frac{(x-1)^2}{x-1}=x-1,
```

cũng cho `0/0` khi substitute `1`, nhưng limit là `0`.

Do đó same indeterminate form có thể dẫn tới different limits. Form cho biết “cần thêm analysis”, không quyết định result.

## One-sided limits: approach direction có thể matter

Left-hand limit

```math
\lim_{x\to a^-}f(x)
```

chỉ xét `x<a` tiến tới `a`.

Right-hand limit

```math
\lim_{x\to a^+}f(x)
```

chỉ xét `x>a`.

Two-sided limit tồn tại khi hai one-sided limits tồn tại và bằng nhau.

Xét step function

```math
f(x)=
\begin{cases}
0,&x<0,\\
1,&x\ge0.
\end{cases}
```

Ta có

```math
\lim_{x\to0^-}f(x)=0,
```

nhưng

```math
\lim_{x\to0^+}f(x)=1.
```

Vì hai sides khác nhau,

```math
\lim_{x\to0}f(x)
```

không tồn tại.

Piecewise pricing, tax threshold, activation functions và control logic đều có thể tạo kiểu behavior này.

## Infinite limits: unbounded behavior, không phải “giá trị infinity”

Khi viết

```math
\lim_{x\to0^+}\frac1x=+\infty,
```

`∞` không phải real number mà function chạm tới. Statement nói:

> với bất kỳ bound `M` lớn đến đâu, ta có thể chọn `x>0` đủ gần 0 để `1/x>M`.

Tương tự,

```math
\lim_{x\to0^-}\frac1x=-\infty.
```

Vì behavior hai sides khác sign, không có single two-sided infinite behavior.

Vertical asymptote thường liên quan kiểu unbounded local behavior này.

## Limits at infinity: long-run behavior

Ký hiệu

```math
\lim_{x\to\infty}f(x)=L
```

không nói `x` “đạt infinity”. Nó nói khi `x` vượt mọi threshold đủ lớn, `f(x)` có thể được ép gần `L` tùy ý.

Ví dụ

```math
\lim_{x\to\infty}\frac{3x^2+1}{x^2-5}=3.
```

Chia numerator và denominator cho `x^2`:

```math
\frac{3+1/x^2}{1-5/x^2}.
```

Khi `x→∞`, terms `1/x^2` và `5/x^2` tiến về 0, để lại ratio `3`.

Điều này phản ánh principle “highest-order terms dominate” cho rational functions ở large magnitude.

## Rates of growth và dominant terms

Limits at infinity cho phép compare growth.

Ví dụ polynomial thấp hơn bị polynomial cao hơn dominate:

```math
\lim_{x\to\infty}\frac{x^2}{x^3}=0.
```

Exponential dominate polynomial:

```math
\lim_{x\to\infty}\frac{x^k}{e^x}=0
```

cho fixed positive integer `k`.

Logarithm grow chậm hơn powers:

```math
\lim_{x\to\infty}\frac{\ln x}{x^a}=0
```

với `a>0`.

Hierarchy này rất quan trọng trong algorithm complexity và asymptotic analysis.

## Continuity: khi function value khớp với local behavior

Function `f` continuous tại `a` nếu

```math
\lim_{x\to a}f(x)=f(a).
```

Viết đầy đủ, điều này ngầm yêu cầu:

- `f(a)` được định nghĩa;
- limit tồn tại;
- limit bằng function value.

Trực giác “vẽ graph không nhấc bút” hữu ích trong `R→R`, nhưng không đủ general. Definition sâu hơn là **small input perturbation tạo arbitrarily small output perturbation** local quanh point.

Epsilon–delta form của continuity là:

```math
|x-a|<\delta\Rightarrow |f(x)-f(a)|<\varepsilon.
```

Khác limit definition ở chỗ `x=a` không cần bị exclude và target output là chính `f(a)`.

## Continuity trên interval

Một function continuous trên interval nếu continuous tại mọi interior point và appropriate one-sided continuity tại endpoints.

Continuous functions có nhiều stability properties. Hai theorem đặc biệt quan trọng trên closed bounded interval `[a,b]` là:

**Extreme Value Theorem:** continuous function đạt minimum và maximum.

**Intermediate Value Theorem:** function nhận mọi value giữa `f(a)` và `f(b)`.

Continuity vì thế không chỉ là “graph mượt”. Nó guarantee existence của values/extrema dưới conditions cụ thể.

## Intermediate Value Theorem và root existence

Nếu `f` continuous trên `[a,b]` và

```math
f(a)f(b)<0,
```

thì `0` nằm giữa `f(a)` và `f(b)`. Intermediate Value Theorem bảo đảm tồn tại ít nhất một `c∈(a,b)` sao cho

```math
f(c)=0.
```

Đây là theoretical foundation của bisection.

Lưu ý theorem chỉ guarantee **existence**, không uniqueness. Function có thể cross zero nhiều lần trong interval.

## Types of discontinuity

### Removable discontinuity

Ví dụ

```math
f(x)=\frac{x^2-1}{x-1}
```

at `x=1` có finite limit `2` nhưng function undefined. Ta có thể “repair” continuity bằng cách define

```math
f(1)=2.
```

### Jump discontinuity

Left và right limits finite nhưng khác nhau. Step functions thường có jumps.

### Infinite discontinuity

Function unbounded quanh point, như `1/x` tại 0.

### Oscillatory failure

Function

```math
f(x)=\sin\frac1x
```

khi `x→0` oscillate ngày càng nhanh giữa `-1` và `1`, nên không approach một value duy nhất.

Ví dụ này quan trọng vì limit có thể fail mà không jump và không blow up.

## Continuous không có nghĩa differentiable

Absolute value

```math
f(x)=|x|
```

continuous tại `0`, nhưng derivative không tồn tại ở đó vì left slope `-1` và right slope `1`.

Differentiability stronger hơn continuity.

Nếu function differentiable tại `a`, nó continuous tại `a`. Converse sai.

Geometrically, derivative cần local linear approximation; continuity chỉ yêu cầu no output jump under arbitrarily small input perturbation.

## Differentiability như local linearity

Limit mở đường cho derivative:

```math
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}.
```

Expression bên trong là average slope trên interval size `h`. Limit hỏi liệu slopes có stabilize về một value khi interval shrink không.

Vì vậy derivative không phải “đặt `h=0`”. Ta không bao giờ divide by zero. Ta analyze ratio cho nonzero `h` rồi lấy limit.

Đây là conceptual reason limits nằm trước derivatives trong calculus.

## Sequence viewpoint của limits

Một cách hiểu khác: nếu mọi sequence `x_n` với

```math
x_n\to a,
```

và `x_n≠a` cuối cùng, đều cho

```math
f(x_n)\to L,
```

thì function limit là `L` trong standard real setting.

Viewpoint này rất hữu ích để prove nonexistence. Nếu ta tìm hai sequences cùng tiến tới `a` nhưng function values tiến tới two different limits, global limit không tồn tại.

Ví dụ với

```math
f(x)=\sin\frac1x,
```

ta chọn sequences làm `1/x` rơi vào peaks `π/2+2πn` và troughs `3π/2+2πn`; function values lần lượt tiến theo subsequences `1` và `-1`. Vì vậy không có single limit tại 0.

## Limits và infinite series

Series

```math
\sum_{n=1}^{\infty}a_n
```

không có nghĩa “thực hiện phép cộng vô hạn xong”. Ta define partial sums

```math
S_N=\sum_{n=1}^N a_n
```

rồi hỏi limit

```math
\lim_{N\to\infty}S_N.
```

Infinite sum tồn tại khi sequence partial sums converge.

Limit vì thế là mechanism biến “infinite process” thành finite mathematical object thông qua convergence.

## Uniform continuity: cùng một `δ` cho cả region

Ordinary continuity cho phép `δ` phụ thuộc cả `ε` và point `a`.

Uniform continuity yêu cầu với mỗi `ε`, một single `δ` hoạt động cho mọi pair points trong domain:

```math
|x-y|<\delta\Rightarrow |f(x)-f(y)|<\varepsilon.
```

Continuous function trên closed bounded interval `[a,b]` luôn uniformly continuous.

Distinction này quan trọng trong analysis vì nó kiểm soát sensitivity globally hơn local pointwise continuity.

## Continuity trong nhiều dimensions

Với function

```math
f:\mathbb R^n\to\mathbb R^m,
```

continuity generalize bằng distance/norm:

```math
\|x-a\|<\delta
\Rightarrow
\|f(x)-f(a)\|<\varepsilon.
```

Ta thấy essence không phụ thuộc one-dimensional graph. Continuity là preservation của nearness.

Topology sau này abstract hóa idea này hơn nữa, thậm chí bỏ explicit metric trong nhiều contexts.

## Limit và numerical computing là hai tầng khác nhau

Mathematical statement

```math
h\to0
```

không bảo computer nên chọn `h` cực nhỏ nhất có thể.

Finite-difference derivative

```math
\frac{f(x+h)-f(x)}{h}
```

có truncation error khi `h` lớn nhưng cancellation/rounding error khi `h` quá nhỏ.

Limit là ideal mathematical object; numerical algorithm phải chọn finite step trong finite precision.

Nhầm hai tầng này dẫn đến misconception kiểu “đặt `h=10^{-100}` sẽ gần derivative hơn”. Trên floating point, `x+h` thậm chí có thể round thành đúng `x`.

## Limits trong asymptotic complexity

Big-O notation cũng nói về long-run growth behavior.

Statement

```math
T(n)=O(g(n))
```

có nghĩa tồn tại constants `C,n_0` sao cho

```math
|T(n)|\le C|g(n)|
```

cho mọi `n≥n_0`.

Limit ratio thường giúp compare growth:

```math
\lim_{n\to\infty}\frac{T(n)}{g(n)}.
```

Nếu ratio tiến tới positive finite constant, hai functions có cùng asymptotic order theo strong intuitive sense.

Vì vậy limit không chỉ là calculus technique; nó là language của asymptotics trong algorithms.

## Knowledge Connection — continuity và robust systems

Trong engineering, continuity là primitive form của robustness: small change input không tạo arbitrary large jump output.

Nhưng continuity không guarantee practical robustness đủ mạnh. Function có thể continuous nhưng derivative cực lớn, nghĩa tiny input noise vẫn tạo large output change.

Để quantify sensitivity ta cần derivatives, Lipschitz constants hoặc condition numbers.

Continuity trả lời “có catastrophic jump do infinitesimal perturbation không?”; conditioning trả lời “amplification mạnh đến mức nào?”.

## Knowledge Connection — continuity và optimization

Continuous objective trên compact feasible set đạt global min/max theo Extreme Value Theorem. Đây là existence guarantee trước khi bàn algorithm nào tìm optimum.

Differentiability cho gradient-based methods thêm local geometry, nhưng existence của optimum và computability của optimum là different questions.

Mathematical optimization tốt cần phân biệt rõ các tầng guarantee này.

## Mental Model

> Limit là một **tolerance contract**: nếu ta yêu cầu output gần target đến bất kỳ mức nào, liệu có thể ép input đủ gần point để guarantee điều đó không? Continuity nói function value tại point đồng ý với local limit. Derivative dùng limit để biến shrinking interval thành instantaneous rate; integral và infinite series dùng limit để biến increasingly fine/long finite approximations thành mathematical object. Limit là cây cầu giữa finite reasoning và idealized infinitesimal/infinite behavior.

## Common Misconceptions

**“`x→a` nghĩa cuối cùng `x=a`.”** Không. Limit nghiên cứu arbitrarily close values; `x=a` có thể bị exclude.

**“Limit luôn bằng function value.”** Chỉ khi function continuous tại point. Hole hoặc intentionally redefined point có thể khác limit.

**“`0/0` là limit bằng 0.”** `0/0` là indeterminate form, không phải answer. Different expressions cho same form có thể có different limits.

**“`∞` là một số real rất lớn.”** Trong standard real calculus, infinity biểu diễn unbounded behavior hoặc extended concept, không phải ordinary real number để algebra tùy ý.

**“Continuous nghĩa smooth.”** Continuous function có thể có corner, nowhere-differentiable behavior hoặc rất irregular shape. Differentiability/smoothness là stronger properties.

**“Muốn numerical derivative tốt chỉ cần lấy `h` càng nhỏ.”** Mathematical limit và floating-point approximation khác nhau. Quá nhỏ có thể làm rounding/cancellation dominate.

**“Graph nhìn có vẻ tiến tới value là đủ chứng minh limit.”** Graph tạo intuition nhưng finite-resolution picture không phải proof; oscillation hoặc narrow behavior có thể bị hình vẽ che mất.