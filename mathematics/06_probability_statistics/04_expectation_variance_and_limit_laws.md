# Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Expectation là weighted center, không phải kết quả (outcome / 결과) được hứa hẹn** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Expected giá trị (value / 값) phụ thuộc payoff, không chỉ xác suất (probability / 확률)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối expectation, variance và limit laws, để mô tả trung tâm, độ phân tán và hành vi khi kích thước mẫu tăng.

Kỳ vọng (expectation / 기댓값), phương sai (variance / 분산), luật số lớn (Law of Large Numbers / 대수의 법칙) và định lý giới hạn trung tâm (Central Limit Theorem / 중심극한정리) là bốn concept tạo cầu nối (bridge / 브리지) từ xác suất sang thống kê.

Chúng trả lời bốn câu hỏi khác nhau:

```text
Expectation → center ở đâu?
Variance → spread lớn thế nào?
LLN → average của nhiều observations có ổn định không?
CLT → distribution của normalized aggregate có shape gì?
```

Nếu trộn bốn câu hỏi này thành một collection formulas, rất dễ hiểu sai statistics. Vì vậy chapter này đi từ intuition rồi mới formalize.

## 1. Expectation là weighted center, không phải kết quả (outcome / 결과) được hứa hẹn

Với random variable rời rạc `X`, expectation:

```math
E[X]=\sum_x xP(X=x).
```

Với continuous variable có density `f`:

```math
E[X]=\int_{-\infty}^{\infty}x f(x)\,dx
```

khi integral tồn tại.

Ta có thể nhìn expectation như center of mass của xác suất (probability / 확률) phân phối (distribution / 분포).

Nếu fair die:

```math
E[X]=\frac{1+2+3+4+5+6}{6}=3.5.
```

`3.5` không phải possible roll. Expectation là long-run average/center của phân phối (distribution / 분포), không phải prediction rằng observation tiếp theo sẽ bằng mean.

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **2. Expected giá trị (value / 값) phụ thuộc payoff, không chỉ xác suất (probability / 확률)** tiếp nhận điểm tựa từ **1. Expectation là weighted center, không phải kết quả (outcome / 결과) được hứa hẹn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Linearity of expectation: thuộc tính (property / 속성) mạnh vì không cần independence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Expected giá trị (value / 값) phụ thuộc payoff, không chỉ xác suất (probability / 확률)

Trong quyết định (decision / 결정) bài toán (problem / 문제), ta thường quan tâm random payoff `Y=g(X)` hơn raw kết quả (outcome / 결과) `X`.

Expected payoff:

```math
E[g(X)]
```

không nói chung bằng

```math
g(E[X]).
```

Ví dụ nếu utility hoặc mất mát (loss / 손실) nonlinear, “plug mean vào hàm (function / 함수)” có thể cho answer sai.

Điều này quan trọng trong finance, rủi ro (risk / 위험) management và machine học tập (learning / 학습) mất mát (loss / 손실) functions.

> **Chuyển mạch:** Ở chặng này của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **3. Linearity of expectation: thuộc tính (property / 속성) mạnh vì không cần independence** tiếp nhận điểm tựa từ **2. Expected giá trị (value / 값) phụ thuộc payoff, không chỉ xác suất (probability / 확률)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Indicator variables biến counting bài toán (problem / 문제) thành expectation bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Linearity of expectation: thuộc tính (property / 속성) mạnh vì không cần independence

Với constants `a,b,c`:

```math
E[aX+bY+c]
=aE[X]+bE[Y]+c.
```

Thuộc tính (property / 속성) này **không cần** `X,Y` independent.

Proof idea trong discrete trường hợp (case / 사례):

```math
E[X+Y]
=\sum_{x,y}(x+y)P(X=x,Y=y)
```

split sum thành hai phần, rồi marginalize joint phân phối (distribution / 분포). Kết quả trở thành `E[X]+E[Y]`.

Independence không xuất hiện trong argument.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **4. Indicator variables biến counting bài toán (problem / 문제) thành expectation bài toán (problem / 문제)** tiếp nhận điểm tựa từ **3. Linearity of expectation: thuộc tính (property / 속성) mạnh vì không cần independence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Worked Example: expected number of collisions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Indicator variables biến counting bài toán (problem / 문제) thành expectation bài toán (problem / 문제)

Indicator `I_A` của sự kiện (event / 이벤트) `A`:

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

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **4. Indicator variables biến counting bài toán (problem / 문제) thành expectation bài toán (problem / 문제)** cho ta quy tắc; **5. Worked Example: expected number of collisions** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **6. Variance đo squared deviation khỏi center** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Worked Example: expected number of collisions

Giả sử `n` items được băm (hash / 해시) uniform vào `m` buckets. Với mỗi pair `(i,j)`, tạo indicator `I_{ij}=1` nếu chúng cùng bucket.

Xác suất (probability / 확률) collision của một pair:

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

> **Chuyển mạch:** Ở chặng này của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **5. Worked Example: expected number of collisions** cho ta quy tắc; **6. Variance đo squared deviation khỏi center** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. tiêu chuẩn (standard / 표준) deviation quay về đơn vị (unit / 단위) ban đầu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Variance đo squared deviation khỏi center

Nếu `\mu=E[X]`, variance:

```math
Var(X)=E[(X-\mu)^2].
```

Square làm ba việc:

1. deviations âm/dương không cancel;
2. larger deviations bị penalize mạnh hơn;
3. algebra liên hệ đẹp với inner sản phẩm (product / 제품) và least squares.

Equivalent định danh (identity / 식별자):

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **7. tiêu chuẩn (standard / 표준) deviation quay về đơn vị (unit / 단위) ban đầu** tiếp nhận điểm tựa từ **6. Variance đo squared deviation khỏi center** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Scaling và shifting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. tiêu chuẩn (standard / 표준) deviation quay về đơn vị (unit / 단위) ban đầu

Variance có squared đơn vị (unit / 단위). Nếu `X` đo KRW, variance có `KRW^2`.

Tiêu chuẩn (standard / 표준) deviation:

```math
\sigma=\sqrt{Var(X)}
```

trở lại KRW.

Đây là lý do tiêu chuẩn (standard / 표준) deviation dễ interpret hơn variance ở báo cáo thực tế, dù variance thuận tiện hơn về algebra.

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **8. Scaling và shifting** tiếp nhận điểm tựa từ **7. tiêu chuẩn (standard / 표준) deviation quay về đơn vị (unit / 단위) ban đầu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Variance của tổng: covariance là nơi dependence xuất hiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Scaling và shifting

Với constants `a,b`:

```math
Var(aX+b)=a^2Var(X).
```

Shift `b` không đổi spread. Scaling by `a` quy mô (scale / 규모) deviations by `a`, nên squared deviations quy mô (scale / 규모) `a^2`.

> **Chuyển mạch:** Ở chặng này của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **9. Variance của tổng: covariance là nơi dependence xuất hiện** tiếp nhận điểm tựa từ **8. Scaling và shifting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Covariance và correlation chỉ tóm tắt tuyến tính (linear / 선형) co-movement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **10. Covariance và correlation chỉ tóm tắt tuyến tính (linear / 선형) co-movement** tiếp nhận điểm tựa từ **9. Variance của tổng: covariance là nơi dependence xuất hiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Law of total expectation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Covariance và correlation chỉ tóm tắt tuyến tính (linear / 선형) co-movement

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

Correlation chuẩn hóa đơn vị (unit / 단위) nhưng vẫn chủ yếu đo tuyến tính (linear / 선형) association.

`Cov=0` không nói chung imply independence.

Một nonlinear phụ thuộc (dependency / 의존성) có thể có zero covariance.

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **11. Law of total expectation** tiếp nhận điểm tựa từ **10. Covariance và correlation chỉ tóm tắt tuyến tính (linear / 선형) co-movement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Law of total variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Law of total expectation

Nếu `Y` chứa thông tin (information / 정보)/ngữ cảnh (context / 맥락):

```math
E[X]=E[E[X\mid Y]].
```

Intuition: tính average trong từng group/ngữ cảnh (context / 맥락) trước, rồi average các group theo weights đúng, sẽ trở lại overall average.

Đây là formal phiên bản (version / 버전) của weighted average và rất hữu ích trong hierarchical lập luận (reasoning / 추론).

> **Chuyển mạch:** Ở chặng này của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **12. Law of total variance** tiếp nhận điểm tựa từ **11. Law of total expectation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. mẫu (sample / 표본) mean là random variable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Nó xuất hiện trong ANOVA intuition, hierarchical các mô hình (models / 모델들) và variance decomposition.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **13. mẫu (sample / 표본) mean là random variable** tiếp nhận điểm tựa từ **12. Law of total variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Tại sao averaging giảm noise?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. mẫu (sample / 표본) mean là random variable

Cho observations

```math
X_1,\ldots,X_n.
```

Mẫu (sample / 표본) mean:

```math
\bar X_n=\frac1n\sum_{i=1}^nX_i.
```

Trước khi observe dữ liệu (data / 데이터), `\bar X_n` là random variable. Vì vậy nó có expectation và variance riêng.

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

Do đó tiêu chuẩn (standard / 표준) deviation của mẫu (sample / 표본) mean:

```math
\frac\sigma{\sqrt n}.
```

Đây là nguồn (source / 소스) của square-root law trong sampling bất định (uncertainty / 불확실성).

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **14. Tại sao averaging giảm noise?** tiếp nhận điểm tựa từ **13. mẫu (sample / 표본) mean là random variable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Law of Large Numbers: stabilization của average** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Tại sao averaging giảm noise?

Nếu independent noise terms có positive/negative deviations không systematic, sum tín hiệu (signal / 신호) tăng proportional `n`, trong khi random fluctuation quy mô (scale / 규모) roughly `\sqrt n`.

Vì vậy relative noise giảm roughly như

```math
\frac1{\sqrt n}.
```

Đây là reason sâu hơn đằng sau averaging trong đo lường (measurement / 측정), experiments và mini-batch estimates.

> **Chuyển mạch:** Ở chặng này của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **15. Law of Large Numbers: stabilization của average** tiếp nhận điểm tựa từ **14. Tại sao averaging giảm noise?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. LLN không nói short-run sẽ tự cân bằng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Law of Large Numbers: stabilization của average

LLN nói dưới appropriate các giả định (assumptions / 가정들), mẫu (sample / 표본) average tiến tới expected giá trị (value / 값) khi cỡ mẫu (sample size / 표본 크기) tăng.

Weak LLN có form conceptually:

```math
P(|\bar X_n-\mu|>\varepsilon)\to0.
```

Nghĩa xác suất (probability / 확률) average lệch khỏi `\mu` quá một tolerance cố định trở nên nhỏ.

Strong LLN mạnh hơn: convergence almost surely dưới conditions phù hợp.

Điểm quan trọng không phải memorize theorem variants, mà hiểu message:

> repeated observations có thể noisy, nhưng aggregate average ổn định nếu tiến trình (process / 프로세스) có cấu trúc (structure / 구조) thích hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **16. LLN không nói short-run sẽ tự cân bằng** tiếp nhận điểm tựa từ **15. Law of Large Numbers: stabilization của average** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. CLT hỏi một câu khác LLN** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. LLN không nói short-run sẽ tự cân bằng

Sau 10 tails liên tiếp của fair coin, next toss vẫn xác suất (probability / 확률) heads `0.5`.

LLN nói long-run average converge; nó không tạo một “force” bắt chuỗi (sequence / 시퀀스) ngắn phải compensate ngay.

Đây là lý do gambler's fallacy sai.

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **17. CLT hỏi một câu khác LLN** tiếp nhận điểm tựa từ **16. LLN không nói short-run sẽ tự cân bằng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Tại sao normal phân phối (distribution / 분포) xuất hiện?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. CLT hỏi một câu khác LLN

LLN hỏi:

> average có tiến về `\mu` không?

CLT hỏi:

> nếu zoom vào fluctuations quanh `\mu` theo đúng quy mô (scale / 규모), phân phối (distribution / 분포) của fluctuation trông như thế nào?

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

> **Chuyển mạch:** Ở chặng này của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **18. Tại sao normal phân phối (distribution / 분포) xuất hiện?** tiếp nhận điểm tựa từ **17. CLT hỏi một câu khác LLN** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. CLT không nói raw dữ liệu (data / 데이터) normal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Tại sao normal phân phối (distribution / 분포) xuất hiện?

Một intuition là aggregate của nhiều small contributions độc lập/weakly dependent làm chi tiết phân phối (distribution / 분포) ban đầu bị “average out”, còn mean và variance dominate standardized shape.

Fourier/characteristic-function proofs formalize idea rằng convolution lặp nhiều lần, sau centering/scaling, tiến về Gaussian under broad conditions.

Nhưng không được biến intuition thành claim universal: heavy tails hoặc strong dependence có thể phá classical CLT các giả định (assumptions / 가정들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **18. Tại sao normal phân phối (distribution / 분포) xuất hiện?** nêu điều cần giải thích; **19. CLT không nói raw dữ liệu (data / 데이터) normal** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. tiêu chuẩn (standard / 표준) lỗi (error / 오류) là bất định (uncertainty / 불확실성) của estimator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. CLT không nói raw dữ liệu (data / 데이터) normal

Nếu income highly skewed, raw observations không trở thành normal chỉ vì cỡ mẫu (sample size / 표본 크기) lớn.

CLT chủ yếu nói phân phối (distribution / 분포) của **normalized sum/mẫu (sample / 표본) mean** gần normal.

Đây là một misconception rất phổ biến.

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **19. CLT không nói raw dữ liệu (data / 데이터) normal** nêu điều cần giải thích; **20. tiêu chuẩn (standard / 표준) lỗi (error / 오류) là bất định (uncertainty / 불확실성) của estimator** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. Worked Example: cần bao nhiêu dữ liệu (data / 데이터) để halve tiêu chuẩn (standard / 표준) lỗi (error / 오류)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. tiêu chuẩn (standard / 표준) lỗi (error / 오류) là bất định (uncertainty / 불확실성) của estimator

Nếu `\sigma` known trong ideal iid setup:

```math
SE(\bar X)=\frac\sigma{\sqrt n}.
```

Trong practice, `\sigma` thường unknown và được estimate bằng mẫu (sample / 표본) tiêu chuẩn (standard / 표준) deviation `s`.

Tiêu chuẩn (standard / 표준) lỗi (error / 오류) khác tiêu chuẩn (standard / 표준) deviation:

```text
SD → spread của observations
SE → spread của estimator qua repeated samples
```

> **Chuyển mạch:** Ở chặng này của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **20. tiêu chuẩn (standard / 표준) lỗi (error / 오류) là bất định (uncertainty / 불확실성) của estimator** cho ta quy tắc; **21. Worked Example: cần bao nhiêu dữ liệu (data / 데이터) để halve tiêu chuẩn (standard / 표준) lỗi (error / 오류)?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **22. Dependence làm effective cỡ mẫu (sample size / 표본 크기) nhỏ hơn nominal cỡ mẫu (sample size / 표본 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Worked Example: cần bao nhiêu dữ liệu (data / 데이터) để halve tiêu chuẩn (standard / 표준) lỗi (error / 오류)?

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

Dữ liệu (data / 데이터) tăng 2× không halve bất định (uncertainty / 불확실성); cần khoảng 4× independent thông tin (information / 정보).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **21. Worked Example: cần bao nhiêu dữ liệu (data / 데이터) để halve tiêu chuẩn (standard / 표준) lỗi (error / 오류)?** cho ta quy tắc; **22. Dependence làm effective cỡ mẫu (sample size / 표본 크기) nhỏ hơn nominal cỡ mẫu (sample size / 표본 크기)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **23. Heavy tails và moment các giả định (assumptions / 가정들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Dependence làm effective cỡ mẫu (sample size / 표본 크기) nhỏ hơn nominal cỡ mẫu (sample size / 표본 크기)

Nếu observations positively correlated, covariance terms làm variance của average giảm chậm hơn `1/n`.

Thời gian (time / 시간) series là ví dụ điển hình: 1,000 measurements mỗi millisecond không tương đương 1,000 independent observations nếu tiến trình (process / 프로세스) thay đổi chậm.

Vì vậy statistical power phụ thuộc **independent thông tin (information / 정보)**, không chỉ row count.

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **23. Heavy tails và moment các giả định (assumptions / 가정들)** tiếp nhận điểm tựa từ **22. Dependence làm effective cỡ mẫu (sample size / 표본 크기) nhỏ hơn nominal cỡ mẫu (sample size / 표본 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Chebyshev inequality: guarantee không cần normality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Heavy tails và moment các giả định (assumptions / 가정들)

Một số distributions có expectation tồn tại nhưng variance vô hạn; một số thậm chí expectation không tồn tại theo usual sense.

Trong heavy-tail regime, mẫu (sample / 표본) mean có thể unstable hơn intuition Gaussian.

Finance returns, tệp (file / 파일) sizes, mạng (network / 네트워크) traffic hoặc wealth distributions có thể có heavy-tail hành vi (behavior / 동작), nên blindly dùng mean/variance/CLT approximation cần caution.

> **Chuyển mạch:** Ở chặng này của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **24. Chebyshev inequality: guarantee không cần normality** tiếp nhận điểm tựa từ **23. Heavy tails và moment các giả định (assumptions / 가정들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. liên kết (connection / 연결) với AI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Chebyshev inequality: guarantee không cần normality

Nếu `X` có finite mean `\mu` và variance `\sigma^2`:

```math
P(|X-\mu|\ge k\sigma)\le\frac1{k^2}.
```

Chebyshev thường loose nhưng rất general. Nó cho thấy variance thực sự điều khiển (control / 제어) một dạng tail xác suất (probability / 확률) mà không cần assume normal phân phối (distribution / 분포).

Applied cho mẫu (sample / 표본) mean iid:

```math
P(|\bar X_n-\mu|\ge\varepsilon)
\le
\frac{\sigma^2}{n\varepsilon^2},
```

đưa intuition trực tiếp tới weak LLN.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, sau nội dung của **24. Chebyshev inequality: guarantee không cần normality**, **25. liên kết (connection / 연결) với AI** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **26. liên kết (connection / 연결) với Finance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. liên kết (connection / 연결) với AI

Huấn luyện (training / 학습) mất mát (loss / 손실) mini-batch là estimator của population/empirical mục tiêu (objective / 목표) độ dốc (gradient / 기울기).

Larger batch thường giảm độ dốc (gradient / 기울기) noise, nhưng returns giảm theo square-root-like hành vi (behavior / 동작) và computation/bộ nhớ (memory / 메모리) chi phí (cost / 비용) tăng.

Độ dốc (gradient / 기울기) estimate variance, correlation giữa samples và non-stationary dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) đều ảnh hưởng tối ưu hóa (optimization / 최적화) dynamics.

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **26. liên kết (connection / 연결) với Finance** tiếp nhận điểm tựa từ **25. liên kết (connection / 연결) với AI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. liên kết (connection / 연결) với Physics và đo lường (measurement / 측정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. liên kết (connection / 연결) với Finance

Expected return không đủ để mô tả rủi ro (risk / 위험).

Hai assets có cùng expected return nhưng khác variance, downside asymmetry hoặc tail rủi ro (risk / 위험) cho quyết định (decision / 결정) rất khác.

Portfolio variance phụ thuộc covariance:

```math
Var(w^TR)=w^T\Sigma w.
```

Diversification benefit xuất hiện khi returns không perfectly positively correlated.

LLN intuition cũng phải dùng cẩn thận trong finance vì returns có dependence, regime changes và heavy tails.

> **Chuyển mạch:** Ở chặng này của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **26. liên kết (connection / 연결) với Finance** nêu điều cần giải thích; **27. liên kết (connection / 연결) với Physics và đo lường (measurement / 측정)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. liên kết (connection / 연결) với Physics và đo lường (measurement / 측정)

Repeated đo lường (measurement / 측정) có thể giảm random noise bằng averaging nếu errors approximately independent và unbiased.

Nhưng systematic độ lệch (bias / 편향) không biến mất khi tăng `n`.

Đây là distinction giữa variance reduction và mô hình (model / 모델)/calibration lỗi (error / 오류).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, các dấu vết trong **27. liên kết (connection / 연결) với Physics và đo lường (measurement / 측정)** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Expectation là probabilistic center; variance là squared bất định (uncertainty / 불확실성) quanh center. Averaging nhiều independent-ish observations làm variance của mean co lại. LLN nói average ổn định về center; CLT mô tả shape của scaled fluctuation quanh center. Bốn concept liên quan nhưng trả lời bốn câu hỏi khác nhau.

> **Chuyển mạch:** Trong **Kỳ vọng, phương sai và các luật giới hạn: từ average đến bất định (uncertainty / 불확실성) of averages**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Expected giá trị (value / 값) là kết quả (outcome / 결과) likely nhất.”** Không nhất thiết.

**“Linearity of expectation cần independence.”** Không.

**“Variance của tổng luôn là tổng variances.”** Chỉ khi covariance terms vanish, ví dụ independence thích hợp.

**“LLN nói random chuỗi (sequence / 시퀀스) phải cân bằng ngay.”** Không.

**“CLT làm raw dữ liệu (data / 데이터) thành normal.”** Không; nó nói về normalized aggregate dưới các giả định (assumptions / 가정들).

**“Nhiều rows luôn đồng nghĩa nhiều thông tin (information / 정보).”** Không nếu observations strongly dependent hoặc biased.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
