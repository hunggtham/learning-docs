# Measurement, Data & Estimands — Trước regression phải biết mình đang đo gì

Econometrics không bắt đầu bằng việc chọn một model. Nó bắt đầu bằng câu hỏi: **economic concept nào cần đo, population nào đang được nói tới, outcome/treatment là gì, và quantity nào thật sự cần estimate?** Nếu measurement hoặc estimand sai, một regression chạy hoàn hảo về kỹ thuật vẫn trả lời sai câu hỏi.

## 1. Data không phải reality nguyên bản

Một dataset là kết quả của measurement process: definitions, sampling frame, reporting incentives, missing data, timing, revisions và transformations.

Ví dụ “income” có thể là gross labor income, disposable household income, taxable income hoặc total economic resources. “Employment” có thể là payroll job, person employed, hours worked hoặc self-reported labor status.

Trước khi model hóa, phải viết operational definition.

## 2. Unit of observation

Unit có thể là:

```text
person
household
firm
product
county
country
year
person-year
firm-quarter
```

Nếu outcome ở firm level nhưng treatment ở region level, standard error và interpretation phải phản ánh assignment/clustering level.

## 3. Cross-section, time series và panel

Cross-sectional data quan sát nhiều units tại một thời điểm hoặc window ngắn.

Time-series data theo dõi một aggregate/unit qua thời gian.

Panel/longitudinal data theo dõi cùng units qua nhiều periods.

Cấu trúc data quyết định variation nào có thể dùng để identify effect. Panel không tự động causal; nó chỉ mở thêm within-unit variation.

## 4. Population, sample và sampling frame

Population là tập đối tượng target của inference. Sample là phần thực sự quan sát. Sampling frame là danh sách/process từ đó sample được lấy.

Một random sample từ wrong frame vẫn không đại diện target population.

Ví dụ survey online tự nguyện có thể overrepresent người quan tâm topic dù sample size rất lớn.

## 5. Selection into sample

Selection bias xuất hiện khi probability được quan sát liên quan tới variables quan trọng cho question.

Examples:

- wage data chỉ có cho employed workers;
- hospital outcome chỉ có cho patients who seek care;
- app usage data chỉ có users who adopt app;
- firm survival data bỏ firms đã exit.

Cần hỏi missingness/selection xảy ra trước hay sau treatment/outcome.

## 6. Missing data mechanisms

Một taxonomy thường dùng:

- **MCAR**: missingness độc lập với observed/unobserved values;
- **MAR**: conditional on observed variables, missingness không còn phụ thuộc missing value;
- **MNAR**: missingness vẫn phụ thuộc unobserved value.

MCAR rất mạnh. Imputation không “chữa” MNAR nếu mechanism không được model hoặc bounded.

## 7. Measurement error

Observed variable có thể viết:

```text
X_observed = X_true + measurement error
```

Classical measurement error trong regressor thường attenuate slope toward zero trong simple regression, nhưng non-classical error có thể bias bất kỳ hướng nào.

Outcome measurement error thường tăng noise nếu independent, nhưng differential reporting theo treatment có thể tạo bias.

## 8. Construct validity

Economic constructs như productivity, market power, trust, financial stress hoặc skill không quan sát trực tiếp hoàn hảo.

Proxy có construct validity khi nó thật sự capture concept cần nghiên cứu, không chỉ correlate thuận tiện.

Ví dụ test score đo một phần academic skill nhưng không đồng nhất toàn bộ human capital.

## 9. Reliability khác validity

Measurement reliable nghĩa lặp lại cho kết quả ổn định. Valid nghĩa đo đúng construct.

Một scale có thể rất reliable nhưng consistently đo sai thing.

## 10. Nominal, real và index construction

Economic data cần normalization. Nominal revenue tăng có thể do price hoặc quantity. Real variables cần deflator phù hợp.

Index numbers phụ thuộc basket, weights, rebasing và quality adjustment. Không coi index là physical unit trực tiếp.

## 11. Log transformation

Logs thường dùng vì:

```text
log differences ≈ percentage changes
```

và biến multiplicative relation thành additive.

Nhưng log không defined cho zero/negative values; cách thêm constant tùy tiện có thể đổi interpretation.

## 12. Rate, ratio và denominator problem

Một rate thay đổi có thể do numerator hoặc denominator.

Unemployment rate giảm vì employed tăng khác hoàn toàn labor force shrink. Debt/GDP giảm có thể do debt repayment, nominal GDP growth hoặc inflation.

Luôn decomposed denominator trước khi kể causal story.

## 13. Stock, flow và timing alignment

Một stock tại cuối năm không nên tùy tiện regress với flow của period khác mà không xác định timing.

Treatment phải xảy ra trước outcome nếu causal direction yêu cầu như vậy. Data annual có thể che intra-year ordering.

## 14. Data-generating process

Data-generating process (DGP) là conceptual mechanism tạo observed data.

Một model không cần replicate toàn bộ reality; nó phải capture phần DGP cần cho estimand.

Econometric reasoning hỏi:

```text
What variation generated X?
Why did Y move?
Which common causes generated both?
```

## 15. Descriptive parameter vs causal estimand

Descriptive target có thể là:

```text
mean income
median wage
correlation
forecast error
conditional expectation
```

Causal target có thể là average treatment effect.

Không mọi useful question đều causal. Forecasting tomorrow’s demand có thể cần prediction, không cần treatment effect.

## 16. Potential outcomes

Causal framework thường viết mỗi unit có hai potential outcomes:

```text
Y_i(1) = outcome if treated
Y_i(0) = outcome if untreated
```

Individual treatment effect:

```text
τ_i = Y_i(1) − Y_i(0)
```

Fundamental problem: cùng một unit không thể simultaneously quan sát cả hai states tại cùng thời điểm. Causal inference là bài toán xây credible counterfactual cho potential outcome bị thiếu.

## 17. ATE, ATT và LATE

Average Treatment Effect:

```text
ATE = E[Y(1) − Y(0)]
```

Average Treatment Effect on the Treated:

```text
ATT = E[Y(1) − Y(0) | D=1]
```

Instrumental-variable settings có thể identify Local Average Treatment Effect (LATE) cho compliers dưới assumptions cụ thể.

Các estimands không interchangeable. Policy question phải quyết định population nào quan trọng.

## 18. Treatment phải được định nghĩa rõ

“Education”, “policy”, “exposure” hoặc “credit” thường quá mơ hồ.

Treatment cần dose, timing, duration và version. Một year schooling thêm ở primary school có thể khác university. Tax reform có nhiều components cùng lúc.

Nếu treatment có multiple versions, Stable Unit Treatment Value Assumption (SUTVA) có thể bị đe dọa.

## 19. Interference và spillovers

Standard potential-outcomes notation thường giả định outcome của unit i không phụ thuộc treatment của unit j.

Network, vaccination, classroom, labor market và geographic policy thường có spillovers.

Nếu interference tồn tại, estimand phải mở rộng từ own-treatment effect sang direct/indirect/network effects.

## 20. Counterfactual không phải prediction đơn thuần

Prediction hỏi `Y sẽ là bao nhiêu?`. Causal counterfactual hỏi `Y sẽ khác bao nhiêu nếu intervention thay đổi trong khi các điều kiện relevant khác được giữ theo causal structure?`

Một model forecast tốt không nhất thiết estimate causal effect đúng nếu nó dựa vào variables downstream hoặc proxies của selection.

## 21. DAG intuition

Directed acyclic graph (DAG) là công cụ biểu diễn assumptions về causal paths.

Nếu `Z` gây cả treatment `D` và outcome `Y`, `Z` là confounder:

```text
Z → D
Z → Y
```

Conditioning on confounder có thể block backdoor path. Nhưng conditioning on collider có thể tạo bias.

## 22. Collider bias

Nếu:

```text
D → C ← U
```

và ta condition on `C`, D và U có thể trở nên statistically associated dù ban đầu independent.

Examples thường xuất hiện khi sample chỉ gồm hired workers, hospitalized patients hoặc selected applicants.

Không phải “control càng nhiều càng tốt”.

## 23. Bad controls

Control variable nằm sau treatment có thể absorb một phần treatment effect hoặc mở collider path.

Nếu policy `D` làm income `M` tăng và income làm health `Y` tăng, controlling for `M` chuyển estimand từ total effect sang something closer to direct effect.

Control choice phải dựa causal question, không chỉ p-value.

## 24. Sampling uncertainty vs identification uncertainty

Standard error đo sampling uncertainty conditional on model/design. Nó không đo uncertainty về omitted confounders, wrong functional form, invalid instrument hay bad measurement.

Một estimate có SE cực nhỏ vẫn có thể causally wrong.

## 25. Internal và external validity

Internal validity hỏi estimate có credible cho studied sample/context không.

External validity hỏi effect có generalize sang population, time, institution hoặc scale khác không.

Randomization mạnh về internal validity nhưng không tự đảm bảo external validity.

## 26. Statistical significance vs economic significance

Large sample có thể làm tiny effect statistically significant.

Cần report effect size, units, confidence interval và economic magnitude.

Một coefficient `0.002` có thể nhỏ hoặc lớn tùy outcome scale và policy cost.

## 27. Pre-analysis thinking

Trước khi chạy model, nên viết:

```text
Question
Population
Treatment / exposure
Outcome
Estimand
Assignment / source of variation
Main confounders
Measurement risks
Expected mechanism
Falsification / robustness ideas
```

Workflow này ngăn “regression fishing” sau khi nhìn kết quả.

## 28. Failure modes

Sai lầm thứ nhất là dùng dataset lớn để thay cho representative/credible design.

Sai lầm thứ hai là gọi coefficient causal trước khi xác định counterfactual.

Sai lầm thứ ba là control mọi variable available.

Sai lầm thứ tư là dùng statistical significance thay economic magnitude.

Sai lầm thứ năm là không phân biệt ATE, ATT và local effect.

Sai lầm thứ sáu là bỏ timing, missingness và measurement process.

## 29. Mental model

Trước mọi econometric analysis, hãy hỏi:

1. Economic concept chính xác là gì?
2. Unit, population và sampling frame là gì?
3. Variable được đo thế nào, có error/selection nào?
4. Question là description, prediction hay causality?
5. Estimand chính xác là gì?
6. Counterfactual nào bị thiếu?
7. Variation trong treatment đến từ đâu?
8. Confounders/colliders/post-treatment variables nằm ở đâu?
9. Standard error có đang che identification uncertainty không?
10. Result có economic magnitude và external validity ra sao?

Sau khi xác định data và estimand, regression mới trở thành công cụ hữu ích. Chapter tiếp theo xây regression từ conditional expectation và projection, thay vì học OLS như một nút bấm.
