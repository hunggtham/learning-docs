# Macro + hành vi + bằng chứng → quyết định danh mục

> **Mạch đọc:** Chapter này là một tuyến tích hợp (integrated route / 통합 경로), không phải một mô hình dự báo thị trường mới. Kinh tế vĩ mô (macroeconomics / 거시경제학) thuộc `economics/`; xác suất (probability / 확률), hiệu chuẩn (calibration / 보정) và quyết định dưới bất định thuộc `mathematics/`; thiết kế bằng chứng (evidence design / 근거 설계) thuộc `research_methods/`; thiên lệch nhận thức (cognitive bias / 인지 편향) và quyết định dưới rủi ro thuộc `psychology/`; sizing, diversification và portfolio constraints thuộc `investing/`. Chapter này nối các owner đó thành một quy trình trả lời câu hỏi: **từ một câu chuyện macro hoặc market signal, làm thế nào đi tới một thay đổi danh mục có thể giải thích, kiểm tra và review?**

Nếu chưa chắc về xác suất và quyết định, đọc trước [Xác suất → hiệu chuẩn → quyết định và rủi ro](../../mathematics/09_connections/07_probability_calibration_decision_and_risk.md). Nếu chưa chắc về bias và ambiguity, đọc [decision under risk, uncertainty and ambiguity](../../psychology/02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity.md) và [cognitive biases and metacognition](../../psychology/02_learning_and_cognition/04_cognitive_biases_and_metacognition.md).

Điểm xuất phát quan trọng là: **một narrative đúng về nền kinh tế chưa tự động là một trade đúng.** Giữa hai điểm đó còn ít nhất bốn lớp:

```text
macro observation
→ causal/evidence interpretation
→ market expectation already priced
→ portfolio exposure + constraint
→ decision
```

Một thesis có thể đúng về CPI, tăng trưởng hoặc lãi suất nhưng investment outcome vẫn kém vì market đã price trước, timing khác kỳ vọng, exposure không đúng transmission channel hoặc position size quá lớn so với uncertainty.

## 1. Tách observation, interpretation, forecast và action

Mọi investment note nên phân biệt bốn object:

```text
Observation: dữ liệu nào đã xảy ra?
Interpretation: cơ chế nào có thể giải thích dữ liệu?
Forecast: state tương lai nào có xác suất bao nhiêu?
Action: thay đổi exposure nào phù hợp với forecast + constraint?
```

Ví dụ:

```text
Observation: inflation headline giảm ba tháng liên tiếp.
Interpretation: goods disinflation mạnh, shelter lag chậm hơn.
Forecast: xác suất policy rate giảm trong 12 tháng tăng.
Action: cân nhắc duration exposure lớn hơn.
```

Nếu bốn lớp bị viết thành một câu “inflation giảm nên mua bond”, người đọc không biết assumption nào thất bại khi outcome khác dự kiến.

> **Chuyển mạch:** Sau khi tách bốn lớp, cần đánh giá quality của observation trước khi suy luận nguyên nhân.

## 2. Dữ liệu macro là measurement, không phải reality nguyên bản

GDP, CPI, unemployment, PMI, retail sales hoặc money aggregates đều là **phép đo (measurement / 측정)** được xây dựng từ definition, sample, seasonal adjustment, imputation và revision.

Ví dụ một số câu hỏi cần hỏi trước khi dùng một series:

```text
headline hay core?
level hay rate of change?
month-over-month hay year-over-year?
nominal hay real?
seasonally adjusted hay raw?
first release hay revised history?
aggregate hay composition?
```

Điều này nối trực tiếp sang [Research Methods](../../research_methods/01_measurement_sampling_and_survey_design.md): measurement error và sampling frame không biến mất chỉ vì dataset đến từ một cơ quan uy tín.

Một investor có thể đúng rằng “CPI giảm” nhưng sai về cơ chế nếu giảm chủ yếu từ một component biến động, trong khi service inflation còn sticky. Vì vậy data interpretation phải đi từ aggregate xuống composition khi decision phụ thuộc transmission channel.

## 3. Surprise quan trọng hơn level khi market đã có kỳ vọng

Market price không phản ứng với data trong chân không. Nó phản ứng với chênh lệch giữa outcome và **kỳ vọng đã được định giá (priced expectation / 가격 반영 기대)**.

Mental model:

```text
market move ≈ new information relative to prior expectation
```

Không phải công thức chính xác, nhưng nó ngăn lỗi “tin tốt → giá phải tăng”. Nếu earnings tăng 10% nhưng consensus kỳ vọng 20%, price có thể giảm. Nếu central bank tăng lãi suất nhưng market đã kỳ vọng tăng mạnh hơn, bond yield hoặc currency có thể phản ứng ngược intuition đơn giản.

Do đó mỗi thesis nên ghi:

```text
what I expect
what market appears to expect
where the disagreement is
what observation would close that disagreement
```

Đây là bước chuyển từ macro knowledge sang investment edge.

## 4. Base rate phải đứng trước câu chuyện nổi bật

Một narrative dễ nhớ thường làm **tỷ lệ nền (base rate / 기저율)** bị bỏ quên. Nếu một signal trong lịch sử thường có nhiều false positive, một instance mới không nên được coi như certainty chỉ vì chart hiện tại trông thuyết phục.

Bayesian reasoning đơn giản:

```text
prior belief
+ strength of new evidence
→ updated belief
```

Không cần giả precision bằng một posterior 63,7% nếu evidence không đủ. Nhưng buộc phải nói prior và direction của update giúp tránh chuyển từ “có tín hiệu” sang “chắc chắn recession” quá nhanh.

Ví dụ yield curve inversion có thể mang information về growth/rates regime, nhưng không cho một clock cố định. Câu hỏi tốt hơn là: signal này thay đổi probability distribution của các regime như thế nào, và portfolio có nhạy với regime nào?

## 5. Correlation không tự tạo causal transmission path

Một macro variable tương quan với asset return trong sample lịch sử không đủ để xây thesis. Cần cơ chế truyền dẫn (transmission mechanism / 전파 메커니즘).

Ví dụ policy rate có thể đi qua:

```text
policy rate
→ funding cost
→ credit conditions
→ household/company demand
→ earnings / default risk
→ discount rate / risk premium
→ asset price
```

Mỗi arrow có độ trễ và có thể bị offset bởi fiscal policy, global liquidity, FX, supply shocks hoặc positioning.

Một thesis nên đánh dấu arrow nào là causal mechanism được hỗ trợ tương đối tốt, arrow nào chỉ là empirical association, và arrow nào là assumption cần monitor.

Điều này giúp khi thesis thất bại ta biết “macro call sai” hay “transmission từ macro sang asset sai”.

## 6. Forecast phải là distribution, không phải một điểm duy nhất

Một quyết định danh mục tốt hiếm khi nên dựa trên một số duy nhất như “Fed cuts 100 bps” hay “USD/KRW sẽ về X”. Nên dùng scenario distribution:

```text
Scenario A — soft landing
Scenario B — renewed inflation
Scenario C — recession / credit stress
Scenario D — growth reacceleration
```

Mỗi scenario cần:

```text
probability range
key drivers
asset transmission
portfolio impact
observations that increase/decrease probability
```

Xác suất không cần giả chính xác tuyệt đối. Mục tiêu là buộc reasoning phải cạnh tranh giữa nhiều state thay vì narrative độc quyền.

## 7. Hiệu chuẩn quan trọng hơn việc nhớ vài dự báo đúng

Investor dễ nhớ những call nổi bật và quên toàn bộ distribution của những call cũ. Vì vậy cần review **hiệu chuẩn dự báo (forecast calibration / 예측 보정)**.

Nếu các event được gắn “70% probability” chỉ xảy ra 30–40% trong nhiều lần đủ tương đồng, confidence đang quá cao. Nếu mọi forecast đều được viết “có thể”, chúng không falsifiable và không thể calibration.

Decision journal nên lưu:

```text
forecast date
information set at that time
probability / confidence band
market-implied expectation if available
position taken
invalidation condition
subsequent outcome
```

Quan trọng: đánh giá forecast bằng information có sẵn tại thời điểm quyết định, không dùng hindsight data revision.

## 8. Một forecast tốt chưa chắc tạo alpha nếu đã priced

Đây là boundary giữa **dự báo thế giới (world forecast / 세계 예측)** và **dự báo return (return forecast / 수익률 예측)**.

Ví dụ ta dự báo đúng inflation giảm, nhưng market đã price disinflation mạnh hơn. Asset return phụ thuộc surprise relative to price, không chỉ state kinh tế cuối cùng.

Ta cần hai probability layer:

```text
P(economic state | evidence)
P(asset payoff | economic state, current price, positioning, liquidity)
```

Layer thứ hai thường khó hơn. Nó chứa valuation, term premium, credit spread, positioning, optionality và liquidity condition.

Vì vậy không nên nói “macro đúng = trade đúng”.

## 9. Từ thesis sang exposure: hỏi asset thực sự nhạy với factor nào

Portfolio không sở hữu narrative; nó sở hữu **exposure (노출)**.

Một equity position có thể đồng thời mang exposure tới:

```text
growth
rates / duration
currency
commodity input
credit conditions
country risk
sector cycle
company-specific execution
```

Nếu thesis là “lower rates”, mua một company high-growth có leverage lớn không chỉ là rate exposure; credit risk và earnings execution có thể dominate.

Trước action, map:

```text
thesis
→ expected factor movement
→ instrument sensitivity
→ unwanted secondary exposures
→ hedge / diversification need
```

Đây là bridge giữa macro và portfolio construction.

## 10. Position size phải phản ánh uncertainty, không chỉ conviction wording

Người viết thesis thường dùng từ “high conviction”, nhưng sizing cần một rule rõ hơn.

Position size nên phụ thuộc ít nhất:

```text
expected payoff distribution
confidence / calibration quality
loss if wrong
correlation with existing portfolio
liquidity
time horizon
ability to rebalance
portfolio constraints
```

Một thesis có upside lớn nhưng downside phá hỏng portfolio không nên được size như một bet độc lập. Diversification không chỉ giảm volatility; nó bảo vệ khả năng tiếp tục ra quyết định khi một model sai.

Portfolio foundations đã sở hữu mechanics này tại [portfolio risk, allocation and behavior](../01_foundations/02_PORTFOLIO_RISK_ALLOCATION_AND_BEHAVIOR.md) và [risk measurement, analytics and decision rules](../01_foundations/04_RISK_MEASUREMENT_PORTFOLIO_ANALYTICS_AND_DECISION_RULES.md).

## 11. Risk không đồng nghĩa volatility

**Rủi ro (risk / 위험)** đối với investor có nhiều lớp:

```text
market volatility
permanent capital loss
liquidity loss
leverage / margin risk
currency mismatch
concentration
model risk
behavioral error
forced-sale risk
```

Một asset có historical volatility thấp vẫn có tail risk lớn nếu price stale hoặc liquidity biến mất trong stress. Ngược lại một asset volatile nhưng position nhỏ và unlevered có thể ít gây existential risk hơn.

Do đó decision phải xem **risk to plan**, không chỉ standard deviation.

## 12. Thiên lệch nhận thức thường xuất hiện sau khi đã có position

Psychology quan trọng nhất không phải danh sách bias để học thuộc, mà là hiểu bias xuất hiện tại điểm nào trong workflow.

Ví dụ:

```text
before position: confirmation bias khi chỉ tìm evidence ủng hộ thesis
after gains: overconfidence và outcome bias
after losses: loss aversion, disposition effect, escalation of commitment
under uncertainty: ambiguity aversion hoặc narrative substitution
under social pressure: herding và authority effects
```

Một checklist “đừng bias” thường yếu. Tốt hơn là thiết kế process:

```text
pre-register invalidation conditions
write opposing case
separate thesis review from P&L review
use position-size limits
review forecast calibration
record information available at decision time
```

Process thay environment để bias khó tác động hơn.

## 13. P&L không phải bằng chứng đầy đủ về chất lượng quyết định

Một decision tốt có thể thua vì low-probability outcome xảy ra; một decision kém có thể thắng nhờ may mắn. Đây là khác biệt giữa **chất lượng quyết định (decision quality / 의사결정 품질)** và **kết quả (outcome / 결과)**.

Review nên tách:

```text
Was the evidence valid?
Was the forecast calibrated?
Was the market expectation understood?
Was transmission logic coherent?
Was sizing consistent with uncertainty?
Was execution within risk limits?
Then: what outcome occurred?
```

Nếu chỉ dùng P&L làm teacher, process dễ học sai từ một sample nhỏ.

## 14. Decision journal cần lưu cả điều làm ta đổi ý

Một thesis không nên chỉ có entry condition. Nó cần **điều kiện cập nhật (update condition / 업데이트 조건)** và **điều kiện vô hiệu hóa (invalidation condition / 무효화 조건)**.

Ví dụ:

```text
Thesis: disinflation + weaker growth will lower long-end yields.

Increase confidence if:
- core services inflation broadens downward
- labor demand cools without wage reacceleration
- credit spreads remain contained

Decrease confidence if:
- inflation breadth reaccelerates
- term premium rises independently
- fiscal supply dominates duration demand

Invalidate / redesign if:
- mechanism assumed in thesis no longer explains price behavior
```

Điều kiện phải liên quan mechanism, không phải “sell if price falls 5%” trừ khi strategy thực sự price-based.

## 15. Worked case — inflation giảm nhưng long bond vẫn giảm giá

Giả sử thesis đầu tiên là:

```text
inflation ↓
→ central bank easing expectation ↑
→ long yield ↓
→ long-duration bond price ↑
```

Sau đó inflation đúng là giảm, nhưng long yield lại tăng.

Không nên kết luận ngay “market irrational”. Tách các arrow:

```text
inflation ↓            confirmed
policy expectation ↓   maybe confirmed
term premium ↑         possible offset
fiscal issuance ↑      possible supply pressure
real growth ↑          possible offset
positioning unwind     possible market mechanism
```

Forecast về inflation có thể đúng nhưng mapping `inflation → long yield` thiếu variables. Decision review cần update model, không rewrite history thành “trade chỉ sai timing”.

## 16. Worked case — recession call đúng nhưng equity short vẫn lỗ

Một recession call có thể đúng về economic state nhưng short equity thất bại nếu:

```text
recession đã priced trước
policy response mạnh hơn kỳ vọng
index composition nghiêng về companies ít cyclical hơn
earnings expectations đã reset
short timing có carry / squeeze cost
```

Đây là ví dụ `world forecast ≠ asset return forecast`.

Portfolio action phải xét price và expectation. Economic knowledge là input, không phải trading signal tự động.

## 17. Worked case — macro uncertainty cao nhưng portfolio vẫn cần action

Không hành động cũng là một decision. Nếu uncertainty rất cao, response không nhất thiết là “cash 100%”. Có thể:

```text
reduce concentration
lower leverage
shorten decision horizon
use staged entry
hold optional liquidity
rebalance toward target
hedge specific tail exposure
```

Đây là tư duy **robust decision (강건한 의사결정)**: tìm portfolio vẫn chấp nhận được trên nhiều scenario thay vì tối ưu mạnh cho một forecast mong manh.

## 18. Evidence hierarchy cho investment thesis

Không phải evidence nào cũng ngang nhau. Một route thực dụng:

```text
accounting / contractual fact
high-quality measurement
causal or quasi-causal evidence where relevant
longitudinal historical relation
cross-sectional association
market-implied information
expert judgment
anecdote / narrative
```

Hierarchy không tuyệt đối. Market data có thể rất informative về expectation nhưng không chứng minh causality; historical relation có thể break under regime change; expert judgment có context mà model không có.

Mục tiêu là ghi rõ evidence type và limitation, thay vì trộn chúng thành một confidence score mơ hồ.

## 19. Regime change và distribution shift

Historical backtest giả định một mức ổn định nào đó trong data-generating process. Nhưng monetary regime, regulation, market microstructure, demographics hoặc fiscal behavior có thể thay đổi.

Khi **dịch chuyển phân phối (distribution shift / 분포 이동)** xảy ra, calibration cũ có thể hỏng.

Warning signs:

```text
relationships đổi sign / magnitude
forecast error có bias kéo dài
volatility/correlation structure thay đổi
policy reaction function thay đổi
market participants / regulation thay đổi
```

Response nên là giảm confidence, widen scenario set và re-estimate mechanism; không tiếp tục tăng leverage chỉ vì signal “đáng lẽ phải mean-revert”.

## 20. Portfolio decision là policy, không phải chuỗi reaction

Một danh mục bền vững cần **chính sách quyết định (decision policy / 의사결정 정책)**:

```text
target allocation
allowed deviation
rebalancing rule
position-size limit
liquidity reserve
leverage limit
scenario stress
review cadence
exception process
```

Nếu mỗi headline tạo một action mới, portfolio trở thành output của attention chứ không phải strategy.

Macro research nên update probability/scenario. Portfolio policy quyết định update nào đủ lớn để thay exposure.

## 21. Template từ macro evidence tới action

Có thể dùng template sau cho mọi thesis:

```text
1. Question
What exact state or transition am I estimating?

2. Observation
What data exists as of this decision date?

3. Measurement quality
Definition, revision, sample, lag, composition?

4. Mechanism
What causal/transmission chain links data to asset payoff?

5. Prior / base rate
What happened in comparable cases and how comparable are they?

6. Forecast distribution
What scenarios and probability ranges?

7. Market expectation
What appears already priced?

8. Disagreement
Where exactly does my view differ from market expectation?

9. Exposure mapping
Which instrument expresses that disagreement, and what else does it expose me to?

10. Position sizing
How do uncertainty, downside, correlation and liquidity constrain size?

11. Update conditions
What evidence increases/decreases confidence?

12. Invalidation
What would show the mechanism or thesis is wrong?

13. Review
Separate forecast quality, decision quality and outcome.
```

## 22. Ranh giới và canonical owners

Chapter này không thay thế các owner sau:

- [Macroeconomics](../../economics/03_macroeconomics/README.md): measurement, growth, inflation, monetary/fiscal policy, cycles và open economy.
- [Research Methods](../../research_methods/README.md): measurement, sampling, research design, evidence synthesis và reproducibility.
- [Mathematics Probability/Statistics](../../mathematics/06_probability_statistics/01_probability_foundations.md): probability mechanics và statistical inference.
- [Probability → Calibration → Decision](../../mathematics/09_connections/07_probability_calibration_decision_and_risk.md): probabilistic forecast, calibration, expected loss và value of information.
- [Psychology Decision under Risk](../../psychology/02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity.md): human decision behavior under uncertainty.
- [Portfolio Risk, Allocation and Behavior](../01_foundations/02_PORTFOLIO_RISK_ALLOCATION_AND_BEHAVIOR.md): portfolio construction và behavioral controls.
- [Full Investment Process](./05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md): end-to-end investing workflow.

> **Bàn giao:** Sau chapter này, macro data không nên được đọc như một trade instruction. Người đọc nên có thể đi từ measurement → evidence → probabilistic belief → priced expectation → exposure → sizing → review. Để luyện một shock cụ thể, quay lại [Inflation shock: từ CPI tới portfolio](./01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md) hoặc [Macro, rates, liquidity, valuation và portfolio](./06_MACRO_RATES_LIQUIDITY_COMPANY_VALUATION_PORTFOLIO_CASE.md).