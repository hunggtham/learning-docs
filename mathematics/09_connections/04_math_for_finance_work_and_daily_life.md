# Liên kết kiến thức (knowledge connection / 지식 연결) — Toán trong tài chính, công việc và đời sống

> **Mạch đọc:** Đọc **liên kết kiến thức (knowledge connection / 지식 연결) — Toán trong tài chính, công việc và đời sống** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Growth cộng và growth nhân** sang **APR, effective tỷ lệ (rate / 비율) và compounding frequency**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Các con số nghiệp vụ (business / 비즈니스) thường là những đối tượng (object / 객체) toán quen thuộc mang tên khác: tỷ lệ (rate / 비율), growth factor, discount factor, percentile, utilization, xác suất (probability / 확률), expected mất mát (loss / 손실). Sai lầm phổ biến không phải thiếu công thức khó, mà là chọn sai mathematical cấu trúc (structure / 구조) cho con số đang nhìn.

## Growth cộng và growth nhân

Nếu một quantity tăng thêm `d` mỗi period, mô hình (model / 모델) additive là

```math
A_n=A_0+nd.
```

Nếu tăng `r` percent của chính hiện tại (current / 현재) amount mỗi period, tiến trình (process / 프로세스) là multiplicative:

```math
A_n=A_0(1+r)^n.
```

Đây là lãi kép (Compound Interest / 복리). Exponential xuất hiện vì cùng growth factor được nhân lặp lại.

Hai investments có arithmetic average return giống nhau không nhất thiết có compound kết quả (outcome / 결과) giống nhau. Tăng 50% rồi giảm 50%:

```math
1.5\times0.5=0.75,
```

nên wealth giảm 25%, dù arithmetic average của `+50%` và `-50%` là 0%.

## APR, effective tỷ lệ (rate / 비율) và compounding frequency

Nếu nominal annual tỷ lệ (rate / 비율) `r` compounded `m` lần mỗi năm, effective annual factor là

```math
\left(1+\frac rm\right)^m.
```

Effective annual tỷ lệ (rate / 비율):

```math
EAR=\left(1+\frac rm\right)^m-1.
```

Vì vậy hai khoản vay cùng headline annual percentage có thể có effective chi phí (cost / 비용) khác nếu compounding/fees khác. Khi so sản phẩm tài chính, phải đối chiếu cùng thời gian (time / 시간) basis và cash-flow convention.

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

## Present giá trị (value / 값) và discounting

Nếu amount hôm nay `P` grow thành `F` sau `n` periods:

```math
F=P(1+r)^n.
```

Invert quan hệ (relation / 관계):

```math
P=\frac{F}{(1+r)^n}.
```

Đây là present giá trị (value / 값). Discounting chỉ là inverse của compounding.

Một future cash luồng (flow / 흐름) xa hơn bị discount mạnh hơn vì capital có opportunity chi phí (cost / 비용) qua nhiều periods.

## Net present giá trị (value / 값)

Với cash flows `C_t` và discount tỷ lệ (rate / 비율) `r`:

```math
NPV=\sum_{t=0}^{T}\frac{C_t}{(1+r)^t}.
```

NPV đưa cash flows ở các thời điểm khác nhau về cùng monetary thời gian (time / 시간) tham chiếu (reference / 참조) trước khi cộng.

Discount tỷ lệ (rate / 비율) không phải universal constant; nó phản ánh các giả định (assumptions / 가정들) về opportunity chi phí (cost / 비용), financing, rủi ro (risk / 위험) và ngữ cảnh (context / 맥락). Thay `r` có thể thay quyết định (decision / 결정).

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

Vì vậy fixed loan payment formula là geometric-series kết quả (result / 결과), không phải finance magic.

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

## Expected giá trị (value / 값) và rủi ro (risk / 위험)

Nếu kết quả (outcome / 결과) `X` có possible values `x_i` với probabilities `p_i`:

```math
E[X]=\sum_i p_i x_i.
```

Expected giá trị (value / 값) là long-run weighted center, không phải guaranteed kết quả (outcome / 결과).

Một insurance mất mát (loss / 손실) có thể rare nhưng catastrophic. quyết định (decision / 결정) thường cần expected mất mát (loss / 손실):

```math
E[L]=\sum_i p_i L_i,
```

nhưng variance, tail rủi ro (risk / 위험), liquidity ràng buộc (constraint / 제약조건) và rủi ro (risk / 위험) tolerance cũng matter.

## Diversification và covariance

Portfolio return với weights `w` và asset return véc-tơ (vector / 벡터) `R`:

```math
R_p=w^TR.
```

Variance:

```math
\operatorname{Var}(R_p)=w^T\Sigma w.
```

Không chỉ individual volatility quan trọng; covariance giữa assets quyết định diversification benefit. Hai assets cùng tăng/giảm mạnh cùng lúc không diversify nhiều dù tên ngành khác nhau.

## Percentage điểm (point / 지점) và percent thay đổi (change / 변경)

Nếu lỗi (error / 오류) tỷ lệ (rate / 비율) từ 2% xuống 1%, absolute reduction là **1 percentage điểm (point / 지점)**, relative reduction là

```math
\frac{2\%-1\%}{2\%}=50\%.
```

Cả hai statements có thể đúng nhưng trả lời câu hỏi khác nhau. Báo cáo chỉ nói “giảm 50%” mà không cho baseline dễ gây hiểu sai quy mô (scale / 규모).

## Weighted average

Nếu groups có sizes khác nhau, overall mean là

```math
\bar x=\frac{\sum_i n_i\bar x_i}{\sum_i n_i},
```

không phải average đơn giản của group means trừ khi group sizes bằng nhau.

Lỗi này xuất hiện trong salary reports, phản hồi (response / 응답) times, exam averages và nghiệp vụ (business / 비즈니스) KPIs.

## Simpson's paradox

Trend có thể đảo khi aggregate groups do group composition thay đổi. Ví dụ treatment tốt hơn trong từng rủi ro (risk / 위험) group nhưng overall tỷ lệ (rate / 비율) thấp hơn nếu treatment group chứa nhiều high-risk cases.

Bài học không phải “statistics lừa người”; aggregation đã bỏ một variable cấu trúc quan trọng.

## Tail độ trễ (latency / 지연 시간) và percentiles trong IT

Mean độ trễ (latency / 지연 시간) có thể che slow tail. P95 nghĩa 95% observations không vượt giá trị (value / 값) đó trong empirical interpretation thích hợp; P99 tập trung tail hơn.

Nếu 99 requests mất 100 ms và 1 yêu cầu (request / 요청) mất 10 s, mean khoảng 199 ms nhưng người dùng (user / 사용자) gặp yêu cầu (request / 요청) 10 s có experience hoàn toàn khác.

Không chỉ số (metric / 지표) nào đủ một mình: mean liên quan total tài nguyên (resource / 자원) thời gian (time / 시간), percentiles liên quan tail experience, thông lượng (throughput / 처리량) liên quan volume, lỗi (error / 오류) tỷ lệ (rate / 비율) liên quan độ tin cậy (reliability / 신뢰성).

## Sức chứa (capacity / 용량) planning bằng dimensional phân tích (analysis / 분석)

Giả sử 1 million users, mỗi người dùng (user / 사용자) 20 requests/day. Average requests per second:

```math
\frac{20\times10^6}{86400}\approx231\;requests/s.
```

Nhưng môi trường vận hành (production / 운영 환경) sức chứa (capacity / 용량) không nên provision chỉ theo average. Cần peak factor, burstiness, tính đồng thời (concurrency / 동시성) và độ trễ (latency / 지연 시간) phân phối (distribution / 분포).

Little's Law cho stable hệ thống (system / 시스템):

```math
L=\lambda W,
```

với `L` average number items in hệ thống (system / 시스템), `\lambda` thông lượng (throughput / 처리량) tỷ lệ (rate / 비율), `W` average thời gian (time / 시간) in hệ thống (system / 시스템). Nếu 200 requests/s và average phản hồi (response / 응답) thời gian (time / 시간) 0.5 s, average in-flight requests khoảng 100.

## Forecast xác suất (probability / 확률) và calibration

Forecast “70% chance” không phải promise sự kiện (event / 이벤트) sẽ xảy ra. Calibration hỏi: trong nhiều events được forecast khoảng 70%, proportion xảy ra có gần 70% không?

Một forecaster có thể calibrated nhưng không sharp nếu luôn nói probabilities gần cơ sở (base / 기반) tỷ lệ (rate / 비율). Good probabilistic forecasting cần both calibration và resolution/sharpness.

## Expected giá trị (value / 값) không thay thế utility

Hai gambles cùng expected monetary giá trị (value / 값) có thể khác hoàn toàn với một người nếu downside threatens solvency. quyết định (decision / 결정) lý thuyết (theory / 이론) dùng utility để mô hình (model / 모델) nonlinear giá trị (value / 값) of outcomes.

Điều này giải thích tại sao insurance có thể rational dù expected payout nhỏ hơn premium: premium mua reduction của catastrophic tail rủi ro (risk / 위험).

## Mô hình tư duy (mental model / 사고 모델)

> Khi gặp một con số trong hợp đồng, dashboard hay investment report, hãy phân loại nó trước: mức (level / 수준), ratio, tỷ lệ (rate / 비율), growth factor, percentile, xác suất (probability / 확률), expectation hay discounted giá trị (value / 값). Sau đó mới hỏi denominator, thời gian (time / 시간) đơn vị (unit / 단위), bất định (uncertainty / 불확실성), compounding và các giả định (assumptions / 가정들). Phân loại đúng cấu trúc (structure / 구조) thường quan trọng hơn nhớ thêm một công thức.

## Dùng chung (common / 공통) Misconceptions

Arithmetic average return không đại diện compound wealth growth. Nominal tỷ lệ (rate / 비율) không đồng nghĩa effective annual chi phí (cost / 비용). NPV phụ thuộc discount-rate các giả định (assumptions / 가정들). Expected giá trị (value / 값) không phải kết quả (outcome / 결과) “dự kiến chắc chắn”. Correlation/diversification không đảm bảo protection trong mọi regimes. Percentile không nói average và average không nói tail.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 rate change and accumulation](./00_rate_change_and_accumulation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
