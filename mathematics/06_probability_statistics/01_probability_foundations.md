# Nền tảng xác suất: mô hình hóa bất định bằng events, information và assumptions

Xác suất (probability / 확률) không phải là cách làm cho thế giới “ít ngẫu nhiên hơn”. Nó là một language để mô tả **uncertainty có structure**. Trước khi hỏi một probability bằng bao nhiêu, phải hỏi ba câu:

1. outcome space nào đang được model?
2. event nào ta quan tâm?
3. information và assumptions nào đang được dùng?

Một con số như `70%` không có nghĩa nếu event và information set chưa được định nghĩa.

## Sample space: universe của model, không nhất thiết universe của reality

Không gian mẫu (sample space / 표본공간) `\Omega` là set outcomes mà model cho phép.

Với một coin toss:

```math
\Omega=\{H,T\}.
```

Với hai tosses:

```math
\Omega=\{HH,HT,TH,TT\}.
```

Một event (사건) là subset của `\Omega`. Event “exactly one head” là

```math
\{HT,TH\}.
```

Điểm subtle: sample space là modeling choice. Nếu ta model latency chỉ bằng categories `{fast, slow}`, ta đã bỏ nhiều detail so với continuous milliseconds. Probability conclusions chỉ đúng trong representation đã chọn.

## Probability axioms tồn tại để giữ reasoning nhất quán

Probability measure `P` phải thỏa:

```math
P(A)\ge0,
```

```math
P(\Omega)=1,
```

và với pairwise-disjoint events `A_i`:

```math
P\left(\bigcup_iA_i\right)
=
\sum_iP(A_i).
```

Từ ba axioms này, nhiều rules quen thuộc được derive thay vì memorize.

Vì `A` và `A^c` disjoint và union thành `\Omega`:

```math
P(A)+P(A^c)=1,
```

nên

```math
P(A^c)=1-P(A).
```

Với two events:

```math
P(A\cup B)
=P(A)+P(B)-P(A\cap B),
```

vì intersection bị double-count nếu chỉ cộng hai probabilities.

## Equally likely formula là special case

Nếu finite outcomes equally likely:

```math
P(A)=\frac{|A|}{|\Omega|}.
```

Nhưng đây không phải definition chung của probability. Nó chỉ đúng sau khi assumption “equally likely” được justify.

Một loaded die, market return hay server failure không có outcomes tự nhiên equally likely. Probability phải đến từ mechanism, empirical model, symmetry hoặc inference.

## Worked example — inclusion-exclusion từ set reasoning

Trong 1,000 users:

- 420 dùng feature A;
- 350 dùng feature B;
- 120 dùng cả hai.

Probability một randomly sampled user dùng ít nhất một feature:

```math
P(A\cup B)
=
0.42+0.35-0.12
=0.65.
```

Nếu chỉ cộng 0.42 và 0.35, overlap bị count twice. Probability union rule chính là set inclusion-exclusion được normalize thành measure.

## Conditional probability: probability luôn phụ thuộc information

Xác suất có điều kiện (conditional probability / 조건부확률) của `A` khi biết `B` xảy ra:

```math
P(A\mid B)
=
\frac{P(A\cap B)}{P(B)},
\qquad P(B)>0.
```

Interpretation: khi biết `B`, universe relevant thu hẹp từ `\Omega` xuống `B`; ta renormalize probability mass trong `B` về total 1.

Từ definition:

```math
P(A\cap B)=P(A\mid B)P(B).
```

Và đối xứng:

```math
P(A\cap B)=P(B\mid A)P(A).
```

Equate hai expressions để derive Bayes:

```math
P(A\mid B)
=
\frac{P(B\mid A)P(A)}{P(B)}.
```

Bayes không phải magic inversion; nó chỉ là intersection được factor theo hai directions khác nhau.

## Worked Bayes example — base rate matters

Suppose disease prevalence là 1%. Test có sensitivity 95% và false-positive rate 5%.

Trong 10,000 people, expected counts:

```text
Disease:        100
Positive among disease: 95
No disease:   9,900
False positives: 495
```

Among positive tests, disease cases khoảng

```math
\frac{95}{95+495}\approx0.161.
```

Positive test không imply 95% chance disease. Sensitivity `P(+|D)` khác posterior `P(D|+)`. Base rate quyết định denominator.

## Independence: một structural assumption, không phải cảm giác “không liên quan”

Events `A,B` independent nếu

```math
P(A\cap B)=P(A)P(B).
```

Equivalent khi probabilities positive:

```math
P(A\mid B)=P(A).
```

Nghĩa là biết `B` không thay probability của `A` trong model.

Independence khác mutual exclusivity. Nếu `A` và `B` mutually exclusive với positive probabilities, occurrence của `B` làm probability `A` thành zero, nên chúng strongly dependent.

## Pairwise independence chưa chắc mutual independence

Nhiều events có thể pairwise independent nhưng không jointly independent. Vì vậy trong high-dimensional models, statement “independent” phải rõ level và conditioning context.

Conditional independence đặc biệt quan trọng trong Bayesian networks, graphical models và causal inference:

```math
X\perp Y\mid Z.
```

Nó nói sau khi biết `Z`, `X` không cung cấp thêm information về `Y` trong model.

## Why multiplication appears in repeated trials

Nếu trials independent với success probability `p`, probability của specific sequence có `k` successes và `n-k` failures là

```math
p^k(1-p)^{n-k}.
```

Multiplication đến từ repeated conditional factorization under independence.

Binomial probability thêm combinatorial factor `\binom nk` vì có nhiều sequences tạo cùng count `k`.

Probability và combinatorics gặp nhau ở đây: counting tells how many paths, probability tells weight mỗi path.

## Frequency interpretation và law of large numbers

Nếu repeat một stable random experiment nhiều lần, sample average/frequency thường converge về expectation/probability dưới suitable assumptions.

Điều này giải thích vì sao probability có empirical meaning. Nhưng convergence không nghĩa short-term balancing.

Sau 10 tails liên tiếp của fair coin, next toss vẫn

```math
P(H)=0.5.
```

Belief “heads is now due” là gambler's fallacy: nó nhầm long-run frequency convergence với short-run compensating force.

## Bayesian viewpoint: uncertainty given current information

Bayesian probability dùng probability để encode uncertainty về unknown states/parameters. Khi evidence mới đến:

```math
posterior
\propto
likelihood\times prior.
```

Frequentist framework khác về interpretation của parameters và probability statements, nhưng share axioms và much of the same probability calculus.

Không nên biến hai frameworks thành slogans. Mỗi one answers inference questions với assumptions và procedures khác nhau.

## Expected value: probability-weighted balance point

Cho discrete random variable `X`:

```math
E[X]=\sum_x xP(X=x).
```

Expectation không nhất thiết là possible outcome. Fair die có expectation 3.5 dù không bao giờ roll 3.5.

Expectation là linear:

```math
E[aX+bY]=aE[X]+bE[Y]
```

không cần independence.

Đây là reason expected cost/revenue often easy to decompose.

## Worked Finance example — expected return không đủ mô tả risk

Investment A returns `+10%` chắc chắn. Investment B returns `+30%` với probability 0.5 và `-10%` với probability 0.5.

Both have expected return 10%:

```math
E[R_B]=0.5(0.30)+0.5(-0.10)=0.10.
```

Nhưng distributions khác hoàn toàn. Expected value alone loses variance, tail and path information.

Probability model phải match decision question; một scalar expectation hiếm khi đủ cho risk management.

## Calibration: probability forecast nên được kiểm tra thế nào?

Nếu model đưa probability khoảng 0.7 cho nhiều comparable cases, một calibrated model sẽ thấy event xảy ra roughly 70% trong nhóm đó over repeated samples.

Calibration khác discrimination. Model có thể rank risks tốt nhưng probabilities badly calibrated.

Trong AI classification, medical risk, weather forecast và credit risk, distinction này quan trọng.

## Common-cause dependence trong engineering

Suppose two servers each failure probability 1%. Nếu independent, probability cả hai fail là

```math
0.01^2=0.0001.
```

Nhưng nếu cả hai share same power supply hoặc network, failures correlated. Multiplying 1%×1% underestimates systemic risk.

Independence là assumption phải justify, không phải default convenience.

## Probability zero không luôn nghĩa impossible

Với continuous distribution:

```math
P(X=x)=0
```

cho every exact point, nhưng một realized `X` vẫn nhận một exact value. Probability zero event trong continuous mathematics không đồng nghĩa logical impossibility.

Đây là bridge tới measure-theoretic probability.

## Computer Science, AI và information theory connections

Randomized algorithms analyze expected runtime và failure probability. Hash collisions, Bloom filters, distributed retries và sampling đều dựa probability assumptions.

Machine learning dùng conditional distributions like

```math
P(Y\mid X).
```

Information theory dùng

```math
-\log P(x)
```

để đo surprisal. Rare outcomes carry more information under the model.

## Assumptions và failure modes

Probability statements depend on event definition, conditioning information và model stability. Distribution shift phá historical probabilities. Selection bias làm observed frequencies không represent target population. Hidden variables phá independence. Small samples tạo high uncertainty ngay cả khi point estimate nhìn precise.

Một probability model tốt phải nói cả number **và** assumptions đã tạo number đó.

## Mental Model

> Probability là bookkeeping nhất quán cho uncertainty. Sample space nói những outcomes nào model cho phép; events gom outcomes thành câu hỏi; conditioning thay đổi information set; independence là structural simplification; Bayes chỉ re-express cùng joint probability khi evidence thay đổi. Probability không tồn tại trong vacuum — nó luôn gắn với model và information.

## Common Misconceptions

**“Probability 70% nghĩa event sẽ xảy ra 70 lần trong đúng 100 trials.”** Không; đó là long-run/calibration statement under repeated comparable conditions, không guarantee một block cụ thể.

**“Mutually exclusive nghĩa independent.”** Ngược lại, positive-probability mutually exclusive events are dependent.

**“Sau một streak, random process phải bù.”** Không nếu trials independent.

**“Positive test 95% accurate nghĩa 95% chance disease.”** Posterior còn phụ thuộc base rate và false positives.

**“Hai systems trông unrelated nên failures independent.”** Shared hidden causes có thể tạo dependence mạnh.