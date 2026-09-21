# Kỳ vọng, phương sai và các luật giới hạn: từ average đến uncertainty of averages

Kỳ vọng (expectation / 기댓값), phương sai (variance / 분산), luật số lớn (Law of Large Numbers / 대수의 법칙) và định lý giới hạn trung tâm (Central Limit Theorem / 중심극한정리) là bốn concept tạo bridge từ xác suất sang thống kê.

Chúng trả lời bốn câu hỏi khác nhau:

```text
Expectation → center ở đâu?
Variance → spread lớn thế nào?
LLN → average của nhiều observations có ổn định không?
CLT → distribution của normalized aggregate có shape gì?
```

Nếu trộn bốn câu hỏi này thành một collection formulas, rất dễ hiểu sai statistics. Vì vậy chapter này đi từ intuition rồi mới formalize.

## 1. Expectation là weighted center, không phải outcome được hứa hẹn

Với random variable rời rạc `X`, expectation:

```math
E[X]=\sum_x xP(X=x).
```

Với continuous variable có density `f`:

```math
E[X]=\int_{-\infty}^{\infty}x f(x)\,dx
```

khi integral tồn tại.

Ta có thể nhìn expectation như center of mass của probability distribution.

Nếu fair die:

```math
E[X]=\frac{1+2+3+4+5+6}{6}=3.5.
```

`3.5` không phải possible roll. Expectation là long-run average/center của distribution, không phải prediction rằng observation tiếp theo sẽ bằng mean.

## 2. Expected value phụ thuộc payoff, không chỉ probability

Trong decision problem, ta thường quan tâm random payoff `Y=g(X)` hơn raw outcome `X`.

Expected payoff:

```math
E[g(X)]
```

không nói chung bằng

```math
g(E[X]).
```

Ví dụ nếu utility hoặc loss nonlinear, “plug mean vào function” có thể cho answer sai.

Điều này quan trọng trong finance, risk management và machine learning loss functions.

## 3. Linearity of expectation: property mạnh vì không cần independence

Với constants `a,b,c`:

```math
E[aX+bY+c]
=aE[X]+bE[Y]+c.
```

Property này **không cần** `X,Y` independent.

Proof idea trong discrete case:

```math
E[X+Y]
=\sum_{x,y}(x+y)P(X=x,Y=y)
```

split sum thành hai phần, rồi marginalize joint distribution. Kết quả trở thành `E[X]+E[Y]`.

Independence không xuất hiện trong argument.

## 4. Indicator variables biến counting problem thành expectation problem

Indicator `I_A` của event `A`:

```math
I_A=
\begin{cases}
1,& A\text{ xảy ra}\\
0,& \text{ngược lại}
\end{cases}
```

thì

```math
E[I_A]=P(A).
```

Nếu total count

```math
S=\sum_i I_i,
```

thì

```math
E[S]=\sum_iP(I_i=1).
```

Không cần các indicators independent.

Đây là một kỹ thuật trung tâm trong randomized algorithms và combinatorics.

## 5. Worked Example: expected number of collisions

Giả sử `n` items được hash uniform vào `m` buckets. Với mỗi pair `(i,j)`, tạo indicator `I_{ij}=1` nếu chúng cùng bucket.

Probability collision của một pair:

```math
P(I_{ij}=1)=\frac1m.
```

Số collisions pairs:

```math
C=\sum_{i<j}I_{ij}.
```

Do linearity:

```math
E[C]
=\binom n2\frac1m.
```

Ta không cần chứng minh các pair-collision events independent.

## 6. Variance đo squared deviation khỏi center

Nếu `\mu=E[X]`, variance:

```math
Var(X)=E[(X-\mu)^2].
```

Square làm ba việc:

1. deviations âm/dương không cancel;
2. larger deviations bị penalize mạnh hơn;
3. algebra liên hệ đẹp với inner product và least squares.

Equivalent identity:

```math
Var(X)=E[X^2]-E[X]^2.
```

Derivation:

```math
E[(X-\mu)^2]
=E[X^2-2\mu X+\mu^2]
```

```math
=E[X^2]-2\mu E[X]+\mu^2
=E[X^2]-\mu^2.
```

## 7. Standard deviation quay về unit ban đầu

Variance có squared unit. Nếu `X` đo KRW, variance có `KRW^2`.

Standard deviation:

```math
\sigma=\sqrt{Var(X)}
```

trở lại KRW.

Đây là lý do standard deviation dễ interpret hơn variance ở báo cáo thực tế, dù variance thuận tiện hơn về algebra.

## 8. Scaling và shifting

Với constants `a,b`:

```math
Var(aX+b)=a^2Var(X).
```

Shift `b` không đổi spread. Scaling by `a` scale deviations by `a`, nên squared deviations scale `a^2`.

## 9. Variance của tổng: covariance là nơi dependence xuất hiện

Với hai random variables:

```math
Var(X+Y)
=Var(X)+Var(Y)+2Cov(X,Y).
```

Trong general sum:

```math
Var\left(\sum_iX_i\right)
=\sum_iVar(X_i)+2\sum_{i<j}Cov(X_i,X_j).
```

Ở đây independence mới quan trọng: nếu independent và finite second moments, covariance terms bằng 0.

Đây là contrast quan trọng:

```text
Expectation of sum → không cần independence
Variance of sum → dependence matter
```

## 10. Covariance và correlation chỉ tóm tắt linear co-movement

Covariance:

```math
Cov(X,Y)
=E[(X-E[X])(Y-E[Y])].
```

Correlation:

```math
\rho_{XY}
=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}.
```

Correlation chuẩn hóa unit nhưng vẫn chủ yếu đo linear association.

`Cov=0` không nói chung imply independence.

Một nonlinear dependency có thể có zero covariance.

## 11. Law of total expectation

Nếu `Y` chứa information/context:

```math
E[X]=E[E[X\mid Y]].
```

Intuition: tính average trong từng group/context trước, rồi average các group theo weights đúng, sẽ trở lại overall average.

Đây là formal version của weighted average và rất hữu ích trong hierarchical reasoning.

## 12. Law of total variance

Một decomposition quan trọng:

```math
Var(X)
=E[Var(X\mid Y)]
+Var(E[X\mid Y]).
```

Interpretation:

```text
Total variation
= average within-group variation
+ between-group variation
```

Nó xuất hiện trong ANOVA intuition, hierarchical models và variance decomposition.

## 13. Sample mean là random variable

Cho observations

```math
X_1,\ldots,X_n.
```

Sample mean:

```math
\bar X_n=\frac1n\sum_{i=1}^nX_i.
```

Trước khi observe data, `\bar X_n` là random variable. Vì vậy nó có expectation và variance riêng.

Nếu iid với

```math
E[X_i]=\mu,
\qquad Var(X_i)=\sigma^2,
```

thì

```math
E[\bar X_n]=\mu
```

và

```math
Var(\bar X_n)=\frac{\sigma^2}{n}.
```

Do đó standard deviation của sample mean:

```math
\frac\sigma{\sqrt n}.
```

Đây là source của square-root law trong sampling uncertainty.

## 14. Tại sao averaging giảm noise?

Nếu independent noise terms có positive/negative deviations không systematic, sum signal tăng proportional `n`, trong khi random fluctuation scale roughly `\sqrt n`.

Vì vậy relative noise giảm roughly như

```math
\frac1{\sqrt n}.
```

Đây là reason sâu hơn đằng sau averaging trong measurement, experiments và mini-batch estimates.

## 15. Law of Large Numbers: stabilization của average

LLN nói dưới appropriate assumptions, sample average tiến tới expected value khi sample size tăng.

Weak LLN có form conceptually:

```math
P(|\bar X_n-\mu|>\varepsilon)\to0.
```

Nghĩa probability average lệch khỏi `\mu` quá một tolerance cố định trở nên nhỏ.

Strong LLN mạnh hơn: convergence almost surely dưới conditions phù hợp.

Điểm quan trọng không phải memorize theorem variants, mà hiểu message:

> repeated observations có thể noisy, nhưng aggregate average ổn định nếu process có structure thích hợp.

## 16. LLN không nói short-run sẽ tự cân bằng

Sau 10 tails liên tiếp của fair coin, next toss vẫn probability heads `0.5`.

LLN nói long-run average converge; nó không tạo một “force” bắt sequence ngắn phải compensate ngay.

Đây là lý do gambler's fallacy sai.

## 17. CLT hỏi một câu khác LLN

LLN hỏi:

> average có tiến về `\mu` không?

CLT hỏi:

> nếu zoom vào fluctuations quanh `\mu` theo đúng scale, distribution của fluctuation trông như thế nào?

Với iid variables có finite variance dưới classical setting:

```math
\frac{\sqrt n(\bar X_n-\mu)}{\sigma}
\Rightarrow N(0,1).
```

Equivalent:

```math
\frac{\bar X_n-\mu}{\sigma/\sqrt n}
\Rightarrow N(0,1).
```

## 18. Tại sao normal distribution xuất hiện?

Một intuition là aggregate của nhiều small contributions độc lập/weakly dependent làm chi tiết distribution ban đầu bị “average out”, còn mean và variance dominate standardized shape.

Fourier/characteristic-function proofs formalize idea rằng convolution lặp nhiều lần, sau centering/scaling, tiến về Gaussian under broad conditions.

Nhưng không được biến intuition thành claim universal: heavy tails hoặc strong dependence có thể phá classical CLT assumptions.

## 19. CLT không nói raw data normal

Nếu income highly skewed, raw observations không trở thành normal chỉ vì sample size lớn.

CLT chủ yếu nói distribution của **normalized sum/sample mean** gần normal.

Đây là một misconception rất phổ biến.

## 20. Standard error là uncertainty của estimator

Nếu `\sigma` known trong ideal iid setup:

```math
SE(\bar X)=\frac\sigma{\sqrt n}.
```

Trong practice, `\sigma` thường unknown và được estimate bằng sample standard deviation `s`.

Standard error khác standard deviation:

```text
SD → spread của observations
SE → spread của estimator qua repeated samples
```

## 21. Worked Example: cần bao nhiêu data để halve standard error?

Vì

```math
SE\propto\frac1{\sqrt n},
```

muốn

```math
SE_{new}=\frac12SE_{old},
```

cần

```math
\frac1{\sqrt{n_{new}}}
=\frac12\frac1{\sqrt{n_{old}}}.
```

Suy ra

```math
n_{new}=4n_{old}.
```

Data tăng 2× không halve uncertainty; cần khoảng 4× independent information.

## 22. Dependence làm effective sample size nhỏ hơn nominal sample size

Nếu observations positively correlated, covariance terms làm variance của average giảm chậm hơn `1/n`.

Time series là ví dụ điển hình: 1,000 measurements mỗi millisecond không tương đương 1,000 independent observations nếu process thay đổi chậm.

Vì vậy statistical power phụ thuộc **independent information**, không chỉ row count.

## 23. Heavy tails và moment assumptions

Một số distributions có expectation tồn tại nhưng variance vô hạn; một số thậm chí expectation không tồn tại theo usual sense.

Trong heavy-tail regime, sample mean có thể unstable hơn intuition Gaussian.

Finance returns, file sizes, network traffic hoặc wealth distributions có thể có heavy-tail behavior, nên blindly dùng mean/variance/CLT approximation cần caution.

## 24. Chebyshev inequality: guarantee không cần normality

Nếu `X` có finite mean `\mu` và variance `\sigma^2`:

```math
P(|X-\mu|\ge k\sigma)\le\frac1{k^2}.
```

Chebyshev thường loose nhưng rất general. Nó cho thấy variance thực sự control một dạng tail probability mà không cần assume normal distribution.

Applied cho sample mean iid:

```math
P(|\bar X_n-\mu|\ge\varepsilon)
\le
\frac{\sigma^2}{n\varepsilon^2},
```

đưa intuition trực tiếp tới weak LLN.

## 25. Connection với AI

Training loss mini-batch là estimator của population/empirical objective gradient.

Larger batch thường giảm gradient noise, nhưng returns giảm theo square-root-like behavior và computation/memory cost tăng.

Gradient estimate variance, correlation giữa samples và non-stationary data pipeline đều ảnh hưởng optimization dynamics.

## 26. Connection với Finance

Expected return không đủ để mô tả risk.

Hai assets có cùng expected return nhưng khác variance, downside asymmetry hoặc tail risk cho decision rất khác.

Portfolio variance phụ thuộc covariance:

```math
Var(w^TR)=w^T\Sigma w.
```

Diversification benefit xuất hiện khi returns không perfectly positively correlated.

LLN intuition cũng phải dùng cẩn thận trong finance vì returns có dependence, regime changes và heavy tails.

## 27. Connection với Physics và measurement

Repeated measurement có thể giảm random noise bằng averaging nếu errors approximately independent và unbiased.

Nhưng systematic bias không biến mất khi tăng `n`.

Đây là distinction giữa variance reduction và model/calibration error.

## Mental Model

> Expectation là probabilistic center; variance là squared uncertainty quanh center. Averaging nhiều independent-ish observations làm variance của mean co lại. LLN nói average ổn định về center; CLT mô tả shape của scaled fluctuation quanh center. Bốn concept liên quan nhưng trả lời bốn câu hỏi khác nhau.

## Common Misconceptions

**“Expected value là outcome likely nhất.”** Không nhất thiết.

**“Linearity of expectation cần independence.”** Không.

**“Variance của tổng luôn là tổng variances.”** Chỉ khi covariance terms vanish, ví dụ independence thích hợp.

**“LLN nói random sequence phải cân bằng ngay.”** Không.

**“CLT làm raw data thành normal.”** Không; nó nói về normalized aggregate dưới assumptions.

**“Nhiều rows luôn đồng nghĩa nhiều information.”** Không nếu observations strongly dependent hoặc biased.
