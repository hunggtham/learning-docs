# Metric spaces, uniform convergence và measure: cây cầu từ calculus sang analysis hiện đại

> **Mạch đọc:** Chapter này nối [Real analysis: giới hạn, hội tụ và nền tảng chặt chẽ của calculus](./11_real_analysis_convergence_and_rigor.md) với topology, probability và functional analysis. Mục tiêu không phải xây một graduate course hoàn chỉnh mà giải thích ba bước abstraction thường xuất hiện sau first real analysis: **metric space → uniform convergence → measure/integration**.

Calculus thường bắt đầu trên `\mathbb R` hoặc `\mathbb R^n`. Ở đó ta đã có khoảng cách, giới hạn, continuity và integral quen thuộc. Analysis hiện đại hỏi một câu tổng quát hơn:

> Ta thật sự cần những cấu trúc nào để các khái niệm “gần”, “hội tụ”, “liên tục” và “tích phân” còn có nghĩa?

Câu hỏi này quan trọng vì cùng một pattern xuất hiện trong không gian hàm, probability distributions, numerical approximation và machine learning. Nếu chỉ gắn analysis với đường số thực, ta khó thấy vì sao các theorem giống nhau lại tái xuất hiện ở những domain rất khác.

## 1. Từ khoảng cách Euclid đến metric space

Một **không gian metric (metric space / 거리 공간)** là một set `X` đi cùng một hàm khoảng cách

```math
d:X\times X\to [0,\infty)
```

thỏa bốn tính chất:

```math
d(x,y)\ge 0,
```

```math
d(x,y)=0 \iff x=y,
```

```math
d(x,y)=d(y,x),
```

và **bất đẳng thức tam giác (triangle inequality / 삼각부등식)**

```math
d(x,z)\le d(x,y)+d(y,z).
```

Điều quan trọng là `x,y` không nhất thiết là điểm hình học. Chúng có thể là vectors, sequences, functions hoặc probability distributions, miễn ta có một notion of distance phù hợp.

Ví dụ trên `\mathbb R^n`, Euclidean metric là

```math
d_2(x,y)=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}.
```

Nhưng ta cũng có Manhattan metric

```math
d_1(x,y)=\sum_{i=1}^{n}|x_i-y_i|
```

và max metric

```math
d_\infty(x,y)=\max_i |x_i-y_i|.
```

Ba metric này đo “gần nhau” theo ba geometry khác nhau. Trên finite-dimensional spaces, chúng cho cùng notion of convergence, nhưng geometry và optimization behavior có thể khác đáng kể.

## 2. Open ball: đơn vị cơ bản của local structure

Với tâm `x` và bán kính `r>0`, **quả cầu mở (open ball / 열린 공)** là

```math
B_r(x)=\{y\in X:d(x,y)<r\}.
```

Open ball thay thế intuition “một khoảng nhỏ quanh điểm”. Từ đây ta xây được open sets, continuity và neighborhoods mà không cần tọa độ.

Một set `U` là open nếu với mọi `x\in U`, tồn tại `r>0` sao cho

```math
B_r(x)\subseteq U.
```

Đây là lý do metric spaces nối tự nhiên sang [Topology: continuity, connectivity và shape](../03_geometry_trigonometry/08_topology_continuity_connectivity.md): metric sinh ra một topology, còn topology giữ notion of neighborhood nhưng bỏ requirement phải đo được numerical distance.

## 3. Convergence chỉ cần distance

Một sequence `x_n` hội tụ đến `x` nếu

```math
\forall \varepsilon>0,\ \exists N\ \text{sao cho}\ n\ge N \Rightarrow d(x_n,x)<\varepsilon.
```

Đây chính là epsilon-definition quen thuộc, nhưng `|x_n-x|` đã được thay bằng metric `d(x_n,x)`.

Mental move quan trọng:

```text
real-number convergence
        ↓ abstraction
metric-space convergence
```

Khi đã hiểu bước này, ta có thể nói một sequence of functions hội tụ trong một function space, hoặc một iterative numerical algorithm hội tụ trong parameter space.

## 4. Cauchy sequence và completeness

Một **dãy Cauchy (Cauchy sequence / 코시 수열)** là sequence mà các phần tử cuối cùng ngày càng gần nhau:

```math
\forall\varepsilon>0,\ \exists N:\ m,n\ge N\Rightarrow d(x_m,x_n)<\varepsilon.
```

Điểm tinh tế: definition này không cần biết limit là gì.

Một metric space gọi là **đầy đủ (complete / 완비)** nếu mọi Cauchy sequence đều hội tụ tới một point vẫn nằm trong space.

`\mathbb R` complete, nhưng `\mathbb Q` không complete. Có các rational Cauchy sequences tiến tới `\sqrt 2`, nhưng `\sqrt 2\notin\mathbb Q`.

Completeness là structural guarantee rất mạnh. Nhiều iterative algorithms chứng minh convergence bằng hai bước:

1. chứng minh sequence các iterates là Cauchy;
2. dùng completeness để bảo đảm limit tồn tại trong space.

Đây là nền cho fixed-point methods, differential equations và functional analysis.

## 5. Pointwise convergence của functions

Xét sequence of functions

```math
f_n:X\to\mathbb R.
```

Ta nói `f_n` hội tụ **theo từng điểm (pointwise convergence / 점별수렴)** tới `f` nếu với mỗi fixed `x`:

```math
f_n(x)\to f(x).
```

Formal:

```math
\forall x\in X,\ \forall\varepsilon>0,\ \exists N=N(x,\varepsilon)
```

sao cho

```math
n\ge N\Rightarrow |f_n(x)-f(x)|<\varepsilon.
```

Điểm quan trọng là `N` được phép phụ thuộc vào `x`. Mỗi point có thể convergence với tốc độ khác nhau.

## 6. Uniform convergence: một `N` hoạt động cho toàn domain

Ta nói `f_n` hội tụ **đều (uniform convergence / 균등수렴)** tới `f` nếu

```math
\forall\varepsilon>0,\ \exists N
```

sao cho với **mọi** `x\in X`:

```math
n\ge N\Rightarrow |f_n(x)-f(x)|<\varepsilon.
```

Ở đây `N` không được phụ thuộc vào `x`.

Sự khác biệt nằm ở order of quantifiers:

```text
Pointwise:  for every x → choose N depending on x
Uniform:    choose one N → works for every x
```

Đây không phải chi tiết logic nhỏ. Nó quyết định xem những properties như continuity hay interchange of limit and integral có được bảo toàn hay không.

## 7. Sup norm làm uniform convergence trở thành ordinary convergence

Trên một class of bounded functions, định nghĩa **sup norm (supremum norm / 상한 노름)**:

```math
\|f\|_\infty=\sup_{x\in X}|f(x)|.
```

Khi đó

```math
f_n\to f\ \text{uniformly}
```

chính là

```math
\|f_n-f\|_\infty\to0.
```

Một concept nhìn có vẻ đặc biệt cho functions bỗng trở thành ordinary convergence trong một metric space of functions.

Đây là một ví dụ điển hình cho sức mạnh của abstraction: thay vì nhớ thêm một theorem riêng, ta chọn đúng space và metric để problem trở về pattern quen thuộc.

## 8. Vì sao pointwise convergence có thể làm mất continuity?

Xét trên `[0,1]`:

```math
f_n(x)=x^n.
```

Mỗi `f_n` continuous. Pointwise limit là

```math
f(x)=
\begin{cases}
0,&0\le x<1,\\
1,&x=1.
\end{cases}
```

Limit function không continuous tại `x=1`.

Vấn đề là convergence trở nên arbitrarily slow gần `1`; không có một single `N` kiểm soát toàn interval.

Ngược lại, uniform limit của continuous functions vẫn continuous. Uniform convergence cung cấp mức kiểm soát global đủ mạnh để continuity sống sót qua limiting process.

## 9. Interchanging limit, integral và derivative

Analysis thường gặp expressions như

```math
\lim_{n\to\infty}\int f_n(x)\,dx
```

và muốn đổi thành

```math
\int \lim_{n\to\infty}f_n(x)\,dx.
```

Ta không được tự động swap operations chỉ vì cả hai bên “có vẻ hợp lý”. Cần conditions.

Uniform convergence trên finite interval là một condition mạnh giúp interchange limit và integral trong nhiều elementary settings. Với derivatives, conditions thường chặt hơn: uniform convergence của `f_n` tự nó không đủ để bảo đảm derivatives converge đúng cách.

Mental model:

> Mỗi lần đổi thứ tự hai limiting/accumulation operations, hãy hỏi theorem nào cấp phép việc đổi đó và assumptions là gì.

Idea này trở lại trong probability khi đổi expectation và limit, trong optimization khi đổi differentiation và expectation, và trong numerical methods khi interchange discretization với limiting processes.

## 10. Từ Riemann integral đến measure

Riemann integral chia **domain** thành intervals nhỏ rồi cộng rectangle areas. Cách này rất tốt cho nhiều functions quen thuộc, nhưng gặp khó khi sets/functions trở nên irregular.

**Lý thuyết độ đo (measure theory / 측도론)** đổi viewpoint:

> Thay vì bắt đầu bằng partition của trục, ta trước hết hỏi: những subsets nào có thể được gán một “size” nhất quán?

Một **measure (độ đo / 측도)** `\mu` gán size cho measurable sets và thỏa countable additivity. Nếu `A_i` pairwise disjoint:

```math
\mu\left(\bigcup_{i=1}^{\infty}A_i\right)
=
\sum_{i=1}^{\infty}\mu(A_i).
```

Length trên real line, area, volume và probability đều có thể được xem như measures trong appropriate spaces.

## 11. Sigma-algebra: không phải mọi subset đều cần đo được

Một **sigma-algebra (σ-algebra / 시그마 대수)** `\mathcal F` là collection các subsets của `X` đóng dưới:

- complement;
- countable union;
- từ đó cũng đóng dưới countable intersection.

Measure được định nghĩa trên `(X,\mathcal F)`, không nhất thiết trên toàn power set.

Tại sao phải phức tạp vậy? Vì nếu muốn một measure có những properties tự nhiên như translation invariance và countable additivity trên `\mathbb R`, tồn tại pathological subsets không thể gán length nhất quán cùng lúc với tất cả requirements. Sigma-algebra xác định universe of events/sets mà ta cam kết đo được.

Trong probability, đây chính là cấu trúc:

```math
(\Omega,\mathcal F,P).
```

`\Omega` là sample space, `\mathcal F` là measurable events và `P` là probability measure.

## 12. Lebesgue integral: tích lũy theo value structure

Riemann integration gần như hỏi:

> Hàm có giá trị gì trên từng interval nhỏ của domain?

Lebesgue integration gần hơn với câu hỏi:

> Tập các points nơi function có một range of values nhất định lớn đến đâu?

Cách tổ chức này giúp xử lý limits của functions linh hoạt hơn và là ngôn ngữ tự nhiên của modern probability.

Ta không cần xây toàn bộ Lebesgue integral ở chapter này. Điều quan trọng là hiểu vì sao measure theory xuất hiện: **nó được thiết kế để làm limiting operations và integration chơi tốt với nhau trên function spaces phức tạp hơn**.

## 13. Almost everywhere: bỏ qua set có measure zero

Một property đúng **gần khắp nơi (almost everywhere / 거의 모든 곳)** nếu tập nơi nó sai có measure zero.

Ví dụ trên real line, một finite hoặc countable set có Lebesgue measure zero. Vì vậy hai functions có thể khác nhau tại vài points nhưng được xem như “same” object trong nhiều spaces used by analysis.

Điều này dẫn đến một conceptual shift lớn:

```text
pointwise equality
      ↓
functions equal almost everywhere
      ↓
function spaces such as L^p
```

Trong probability, random variables cũng thường được xem equivalent nếu chúng khác nhau chỉ trên event có probability zero.

## 14. Lp spaces: metric cho functions dựa trên average magnitude

Một family quan trọng là

```math
\|f\|_p=
\left(\int |f|^p\,d\mu\right)^{1/p}
```

với `1\le p<\infty`.

`L^2` đặc biệt quan trọng vì có inner product:

```math
\langle f,g\rangle=\int f(x)g(x)\,d\mu(x).
```

Do đó geometry của vectors mở rộng sang functions. Fourier series, least squares và signal processing có thể được nhìn như projection trong an infinite-dimensional inner-product space.

Liên kết trực tiếp:

- [Inner product, orthogonality và projection](../04_vectors_linear_algebra/06_inner_product_orthogonality_and_projection.md)
- [Fourier, signals và frequency](../09_connections/05_fourier_signals_and_frequency.md)
- [Probability foundations](../06_probability_statistics/01_probability_foundations.md)

## 15. Dominated convergence: pattern quan trọng hơn công thức

Một trong những kết quả trung tâm của measure-theoretic integration là **Dominated Convergence Theorem**. Roughly, nếu `f_n→f` pointwise almost everywhere và có một integrable function `g` kiểm soát

```math
|f_n|\le g,
```

thì dưới các conditions thích hợp:

```math
\lim_{n\to\infty}\int f_n\,d\mu
=
\int f\,d\mu.
```

Điều cần nhớ không phải chỉ tên theorem mà là pattern:

```text
pointwise convergence alone
        ✗ insufficient
convergence + a uniform integrable bound
        ✓ enough control to exchange limit and integral
```

Pattern “cần một domination/control condition” xuất hiện rất nhiều trong advanced probability và stochastic analysis.

## 16. Connection với probability

Expectation là integration:

```math
\mathbb E[X]=\int X\,dP.
```

Variance, moments, conditional expectation và stochastic processes vì vậy sống tự nhiên trong measure-theoretic language.

Điều này giải thích vì sao một probability course nâng cao chuyển từ finite outcomes sang sigma-algebra và measure: không phải để làm notation khó hơn, mà để xử lý continuous distributions, infinite sequences of events và random functions trong cùng một framework.

## 17. Connection với numerical analysis và machine learning

Khi một numerical method tạo sequence `x_n`, câu hỏi “converge hay không?” phụ thuộc space và norm đang dùng.

Trong machine learning, empirical quantities cố approximate population quantities. Ta thường cần kiểm soát không chỉ error tại một fixed parameter mà error trên **cả family of models**. Đây là lý do ideas tương tự pointwise-vs-uniform control xuất hiện trong generalization theory.

Không nên đồng nhất uniform convergence trong elementary function analysis với mọi theorem của statistical learning, nhưng structural question giống nhau:

> Ta kiểm soát approximation ở từng point riêng lẻ hay đồng thời trên toàn class?

## 18. Khi nào cần học sâu hơn?

Chapter này đủ làm bridge nếu mục tiêu là software, data, AI, engineering hoặc finance. Nếu đi sâu pure mathematics / mathematical statistics, các bước tiếp theo hợp lý là:

```text
metric spaces
→ compactness and completeness
→ normed / Banach spaces
→ measure and Lebesgue integration
→ Hilbert spaces
→ functional analysis / measure-theoretic probability
```

## Mental Model

> Metric space tách notion “gần nhau” khỏi tọa độ. Uniform convergence tách “mỗi point eventually đúng” khỏi “toàn domain được kiểm soát cùng lúc”. Measure theory tách “size” và “integration” khỏi các intervals đẹp của elementary calculus. Ba bước abstraction này cho phép calculus tiếp tục hoạt động trên functions, distributions và random objects phức tạp.

## Common Misconceptions

**“Pointwise convergence của continuous functions cho continuous limit.”** Sai; cần stronger control như uniform convergence trong theorem phù hợp.

**“Uniform convergence nghĩa mọi point converge với cùng tốc độ chính xác.”** Không; nó nghĩa một `N` chung đủ để đạt bất kỳ tolerance `ε` đã chọn.

**“Measure theory chỉ là cách viết khó hơn của Riemann integral.”** Không; nó mở rộng notion of size/integration và đặc biệt mạnh khi xử lý limits, probability và function spaces.

**“Measure-zero event là impossible event.”** Không nhất thiết. Trong a continuous distribution, một exact point có probability zero nhưng vẫn thuộc sample space.

## Nguồn học miễn phí để đi sâu

- Jiří Lebl, **Basic Analysis: Introduction to Real Analysis** — https://www.jirka.org/ra/ . Volume I/II được tác giả cung cấp miễn phí; phần advanced mở rộng tới metric spaces và multivariable analysis.
- Abakcus, **Free Math Textbooks from University Mathematicians** — https://abakcus.com/book-lists/free-math-textbooks . Dùng như catalog để tìm thêm sách Analysis từ trang tác giả/trường đại học.

> **Bàn giao:** Sau chapter này, nếu mục tiêu là probability/statistics, đọc [Probability Foundations](../06_probability_statistics/01_probability_foundations.md). Nếu mục tiêu là geometry/function spaces, quay lại [Topology](../03_geometry_trigonometry/08_topology_continuity_connectivity.md) và [Inner Product / Projection](../04_vectors_linear_algebra/06_inner_product_orthogonality_and_projection.md).