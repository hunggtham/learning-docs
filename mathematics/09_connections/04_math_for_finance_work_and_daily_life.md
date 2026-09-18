# Knowledge Connection — Toán trong tài chính, công việc và đời sống

Các con số business thường là những object toán quen thuộc mang tên khác: rate, growth factor, discount factor, percentile, utilization, probability, expected loss. Sai lầm phổ biến không phải thiếu công thức khó, mà là chọn sai mathematical structure cho con số đang nhìn.

## Growth cộng và growth nhân

Nếu một quantity tăng thêm `d` mỗi period, model additive là

```math
A_n=A_0+nd.
```

Nếu tăng `r` percent của chính current amount mỗi period, process là multiplicative:

```math
A_n=A_0(1+r)^n.
```

Đây là lãi kép (Compound Interest / 복리). Exponential xuất hiện vì cùng growth factor được nhân lặp lại.

Hai investments có arithmetic average return giống nhau không nhất thiết có compound outcome giống nhau. Tăng 50% rồi giảm 50%:

```math
1.5\times0.5=0.75,
```

nên wealth giảm 25%, dù arithmetic average của `+50%` và `-50%` là 0%.

## APR, effective rate và compounding frequency

Nếu nominal annual rate `r` compounded `m` lần mỗi năm, effective annual factor là

```math
\left(1+\frac rm\right)^m.
```

Effective annual rate:

```math
EAR=\left(1+\frac rm\right)^m-1.
```

Vì vậy hai khoản vay cùng headline annual percentage có thể có effective cost khác nếu compounding/fees khác. Khi so sản phẩm tài chính, phải đối chiếu cùng time basis và cash-flow convention.

## Continuous compounding

Limit

```math
\lim_{m\to\infty}\left(1+\frac rm\right)^m=e^r
```

dẫn tới continuous compounding:

```math
A(t)=Pe^{rt}.
```

`e` không xuất hiện vì finance “thích e”; nó xuất hiện từ limit của repeated proportional growth.

## Present value và discounting

Nếu amount hôm nay `P` grow thành `F` sau `n` periods:

```math
F=P(1+r)^n.
```

Invert relation:

```math
P=\frac{F}{(1+r)^n}.
```

Đây là present value (Present Value / 현재가치). Discounting chỉ là inverse của compounding.

Một future cash flow xa hơn bị discount mạnh hơn vì capital có opportunity cost qua nhiều periods.

## Net present value

Với cash flows `C_t` và discount rate `r`:

```math
NPV=\sum_{t=0}^{T}\frac{C_t}{(1+r)^t}.
```

NPV đưa cash flows ở các thời điểm khác nhau về cùng monetary time reference trước khi cộng.

Discount rate không phải universal constant; nó phản ánh assumptions về opportunity cost, financing, risk và context. Thay `r` có thể thay decision.

## Annuity và payment formula

Giả sử loan balance `B_k` sau mỗi period obeys

```math
B_{k+1}=B_k(1+r)-Pmt.
```

Iterate:

```math
B_n=P(1+r)^n-Pmt\left[1+(1+r)+\cdots+(1+r)^{n-1}\right].
```

Bracket là geometric series:

```math
\frac{(1+r)^n-1}{r}.
```

Đặt final balance `B_n=0`:

```math
Pmt=P\frac{r(1+r)^n}{(1+r)^n-1}.
```

Vì vậy fixed loan payment formula là geometric-series result, không phải finance magic.

Interest portion ban đầu lớn vì outstanding principal lớn. Khi principal giảm, interest charge giảm và phần payment trả principal tăng.

## Inflation và real purchasing power

Nếu nominal growth factor là `1+r_n` và price-level factor `1+\pi`, real purchasing-power factor là

```math
1+r_{real}=\frac{1+r_n}{1+\pi}.
```

Do đó

```math
r_{real}=\frac{1+r_n}{1+\pi}-1.
```

Approximation

```math
r_{real}\approx r_n-\pi
```

chỉ tốt khi rates không quá lớn.

## Expected value và risk

Nếu outcome `X` có possible values `x_i` với probabilities `p_i`:

```math
E[X]=\sum_i p_i x_i.
```

Expected value là long-run weighted center, không phải guaranteed outcome.

Một insurance loss có thể rare nhưng catastrophic. Decision thường cần expected loss:

```math
E[L]=\sum_i p_i L_i,
```

nhưng variance, tail risk, liquidity constraint và risk tolerance cũng matter.

## Diversification và covariance

Portfolio return với weights `w` và asset return vector `R`:

```math
R_p=w^TR.
```

Variance:

```math
\operatorname{Var}(R_p)=w^T\Sigma w.
```

Không chỉ individual volatility quan trọng; covariance giữa assets quyết định diversification benefit. Hai assets cùng tăng/giảm mạnh cùng lúc không diversify nhiều dù tên ngành khác nhau.

## Percentage point và percent change

Nếu error rate từ 2% xuống 1%, absolute reduction là **1 percentage point**, relative reduction là

```math
\frac{2\%-1\%}{2\%}=50\%.
```

Cả hai statements có thể đúng nhưng trả lời câu hỏi khác nhau. Báo cáo chỉ nói “giảm 50%” mà không cho baseline dễ gây hiểu sai scale.

## Weighted average

Nếu groups có sizes khác nhau, overall mean là

```math
\bar x=\frac{\sum_i n_i\bar x_i}{\sum_i n_i},
```

không phải average đơn giản của group means trừ khi group sizes bằng nhau.

Lỗi này xuất hiện trong salary reports, response times, exam averages và business KPIs.

## Simpson's paradox

Trend có thể đảo khi aggregate groups do group composition thay đổi. Ví dụ treatment tốt hơn trong từng risk group nhưng overall rate thấp hơn nếu treatment group chứa nhiều high-risk cases.

Bài học không phải “statistics lừa người”; aggregation đã bỏ một variable cấu trúc quan trọng.

## Tail latency và percentiles trong IT

Mean latency có thể che slow tail. P95 nghĩa 95% observations không vượt value đó trong empirical interpretation thích hợp; P99 tập trung tail hơn.

Nếu 99 requests mất 100 ms và 1 request mất 10 s, mean khoảng 199 ms nhưng user gặp request 10 s có experience hoàn toàn khác.

Không metric nào đủ một mình: mean liên quan total resource time, percentiles liên quan tail experience, throughput liên quan volume, error rate liên quan reliability.

## Capacity planning bằng dimensional analysis

Giả sử 1 million users, mỗi user 20 requests/day. Average requests per second:

```math
\frac{20\times10^6}{86400}\approx231\;requests/s.
```

Nhưng production capacity không nên provision chỉ theo average. Cần peak factor, burstiness, concurrency và latency distribution.

Little's Law cho stable system:

```math
L=\lambda W,
```

với `L` average number items in system, `\lambda` throughput rate, `W` average time in system. Nếu 200 requests/s và average response time 0.5 s, average in-flight requests khoảng 100.

## Forecast probability và calibration

Forecast “70% chance” không phải promise event sẽ xảy ra. Calibration hỏi: trong nhiều events được forecast khoảng 70%, proportion xảy ra có gần 70% không?

Một forecaster có thể calibrated nhưng không sharp nếu luôn nói probabilities gần base rate. Good probabilistic forecasting cần both calibration và resolution/sharpness.

## Expected value không thay thế utility

Hai gambles cùng expected monetary value có thể khác hoàn toàn với một người nếu downside threatens solvency. Decision theory dùng utility để model nonlinear value of outcomes.

Điều này giải thích tại sao insurance có thể rational dù expected payout nhỏ hơn premium: premium mua reduction của catastrophic tail risk.

## Mental Model

> Khi gặp một con số trong hợp đồng, dashboard hay investment report, hãy phân loại nó trước: level, ratio, rate, growth factor, percentile, probability, expectation hay discounted value. Sau đó mới hỏi denominator, time unit, uncertainty, compounding và assumptions. Phân loại đúng structure thường quan trọng hơn nhớ thêm một công thức.

## Common Misconceptions

Arithmetic average return không đại diện compound wealth growth. Nominal rate không đồng nghĩa effective annual cost. NPV phụ thuộc discount-rate assumptions. Expected value không phải outcome “dự kiến chắc chắn”. Correlation/diversification không đảm bảo protection trong mọi regimes. Percentile không nói average và average không nói tail.
