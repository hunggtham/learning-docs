# Glossary, Formula Conventions và Research Standards

> File này là lớp chuẩn hóa dùng chung cho toàn bộ `investing/`. Mục tiêu không phải thay thế các chapter chuyên sâu mà giúp người đọc dùng cùng một ngôn ngữ, cùng convention công thức và cùng cách phân biệt fact, estimate, assumption và thesis. Khi một khái niệm được giải thích sâu ở domain khác, file này chỉ giữ định nghĩa ngắn và dẫn sang chapter tương ứng.

## 1. Cách đọc terminology trong thư viện

Các thuật ngữ tài chính thường được giữ bằng **English keyword** ở lần xuất hiện đầu tiên vì phần lớn báo cáo doanh nghiệp, broker research, terminal và academic literature dùng English. Phần giải thích chính viết bằng tiếng Việt. Khi nhiều thuật ngữ gần nghĩa nhưng không hoàn toàn giống nhau, thư viện ưu tiên giữ nguyên từ gốc thay vì dịch thành một từ Việt chung làm mất khác biệt.

Ví dụ, `yield`, `return`, `coupon` và `income` không được dùng thay thế tùy ý. `Coupon` là cash flow theo hợp đồng của bond. `Yield` là một rate được suy ra từ price/cash flows theo convention nhất định. `Return` là kết quả đầu tư thực tế trong một period. `Income` chỉ là một thành phần của total return.

Tương tự, `risk` không đồng nghĩa `volatility`. Volatility chỉ đo dispersion của returns quanh mean; risk còn gồm permanent capital loss, default, liquidity, leverage, concentration, operational và behavioral failure.

## 2. Fact, Estimate, Assumption, Scenario và Thesis

Một research note phải phân biệt rõ năm lớp thông tin.

**Fact** là dữ liệu đã xảy ra và có nguồn xác minh, ví dụ revenue quý vừa rồi, policy rate hiện tại hoặc số shares outstanding trong filing.

**Estimate** là con số dự báo từ analyst/company/market, ví dụ consensus EPS năm sau. Estimate phải ghi nguồn và thời điểm vì nó thay đổi.

**Assumption** là input do chính người phân tích đặt vào model, ví dụ gross margin 35% trong base case.

**Scenario** là một tập assumptions nhất quán về economic path, ví dụ recession + easing + credit spread widening.

**Thesis** là claim có thể kiểm chứng về khoảng cách giữa market expectation và outcome bạn cho là có xác suất khác. Thesis không phải câu “company tốt” hoặc “kinh tế xấu”; nó phải nêu driver, catalyst, risk và invalidation.

Một template tối thiểu:

```text
Fact → Interpretation → Assumption → Scenario → Valuation/Expected Return → Position → Invalidation
```

## 3. Nominal và Real

**Nominal** là giá trị chưa điều chỉnh inflation. **Real** là purchasing-power-adjusted value.

Real return chính xác gần:

```text
Real Return = (1 + Nominal Return) / (1 + Inflation) - 1
```

Với tỷ lệ nhỏ có thể dùng approximation:

```text
Real Return ≈ Nominal Return - Inflation
```

Không nên so salary, GDP, bond yield hay portfolio return dài hạn chỉ bằng nominal numbers khi inflation regimes khác nhau.

## 4. Arithmetic Return và Geometric Return

Arithmetic average tính trung bình các period returns. Geometric return phản ánh compounding thực tế.

Nếu capital đi từ 100 → 150 → 100, arithmetic return hai period là `(+50% - 33.3%)/2 ≈ 8.3%`, nhưng geometric total return bằng 0. Đây là lý do volatility làm giảm compound growth.

CAGR:

```text
CAGR = (Ending Value / Beginning Value)^(1/n) - 1
```

Với wealth building, geometric return thường quan trọng hơn arithmetic expected return.

## 5. Volatility, Variance và Standard Deviation

Variance đo average squared deviation quanh mean. Standard deviation là square root của variance và thường được dùng làm volatility.

Annualization gần đúng khi returns độc lập tương đối:

```text
Annual Volatility ≈ Period Volatility × √Periods Per Year
```

Nhưng financial returns có volatility clustering và fat tails, nên square-root-of-time chỉ là approximation chứ không phải law bất biến.

## 6. Covariance và Correlation

Covariance đo hai assets biến động cùng nhau theo đơn vị của returns. Correlation chuẩn hóa covariance về khoảng `-1` tới `+1`.

```text
Correlation(A,B) = Cov(A,B) / (σA × σB)
```

Correlation thấp không tự động tạo diversification nếu hai assets cùng crash trong stress. Vì vậy thư viện thường kết hợp average correlation với downside correlation, factor exposure và scenario stress.

## 7. Portfolio Variance

Với hai assets:

```text
σp² = w1²σ1² + w2²σ2² + 2w1w2Cov(1,2)
```

Ý nghĩa quan trọng nhất không phải nhớ công thức, mà hiểu portfolio risk phụ thuộc cả standalone volatility và interaction giữa assets.

Một asset có volatility cao vẫn có thể giảm total portfolio risk nếu correlation đủ thấp với phần còn lại.

## 8. Beta và Alpha

Beta gần đúng đo sensitivity của asset so benchmark:

```text
Beta = Cov(Rasset, Rbenchmark) / Var(Rbenchmark)
```

Alpha là residual return sau khi account benchmark/factor model. Alpha chỉ meaningful nếu benchmark/model phù hợp và period đủ dài.

Một portfolio outperform market vì nắm nhiều small-cap/value không nên gọi toàn bộ excess return là manager alpha nếu factor exposure giải thích được.

## 9. Sharpe, Sortino và Information Ratio

Sharpe Ratio:

```text
Sharpe = (Portfolio Return - Risk-Free Return) / Portfolio Volatility
```

Sortino thay total volatility bằng downside deviation. Information Ratio dùng active return so tracking error:

```text
IR = Active Return / Tracking Error
```

Các ratios này hữu ích để so process nhưng không thay thế drawdown, tail risk, liquidity và path analysis.

## 10. Drawdown

Drawdown đo percentage decline từ prior peak:

```text
Drawdown = Current Value / Previous Peak - 1
```

Recovery nonlinear:

```text
Loss 10% → cần +11.1%
Loss 20% → cần +25%
Loss 50% → cần +100%
```

Đây là lý do portfolio construction chú trọng survival và geometric compounding chứ không chỉ average return.

## 11. Value at Risk và Expected Shortfall

**VaR** hỏi loss threshold tại confidence level trong một horizon. **Expected Shortfall** hỏi average loss khi đã vượt threshold đó.

Không metric nào là “maximum loss”. Cả hai phụ thuộc distribution/model/data và thường đánh giá thấp jump, liquidity và regime-break risk nếu dùng máy móc.

## 12. Present Value và Discounting

Core valuation principle:

```text
PV = Future Cash Flow / (1 + Discount Rate)^t
```

Value của asset là present value của future cash flows hoặc economic benefits phù hợp với legal claim. Discount rate tăng làm distant cash flows giảm giá trị nhiều hơn, tạo concept duration ở cả bonds lẫn long-duration equities.

## 13. Enterprise Value và Equity Value

Một convention đơn giản:

```text
Enterprise Value = Equity Value + Net Debt + Other Senior Claims - Non-operating Assets
```

Exact bridge phụ thuộc leases, pension deficits, minority interests, investments và industry.

FCFF được discount bằng WACC để ra Enterprise Value. FCFE được discount bằng Cost of Equity để ra Equity Value. Không mix cash flow và discount rate sai layer.

## 14. Free Cash Flow

Một simplified operating definition:

```text
FCFF ≈ EBIT × (1 - Tax Rate)
       + D&A
       - Capex
       - Change in Net Working Capital
```

FCFE có thêm debt flows. Công thức cụ thể phải phù hợp business model; banks và insurers cần framework khác industrial companies.

## 15. ROIC và Reinvestment

Một intuition quan trọng:

```text
Growth ≈ Reinvestment Rate × Return on Incremental Capital
```

Nếu company reinvest nhiều nhưng incremental ROIC dưới cost of capital, growth có thể phá shareholder value. Growth tốt cần cả runway và unit economics.

## 16. Bond Price, Duration và DV01

Bond price là PV của coupon + principal. Rate sensitivity gần:

```text
%ΔPrice ≈ -Modified Duration × ΔYield
```

Với move lớn hơn cần convexity.

DV01/PV01 đo P/L monetary khi yield đổi 1 basis point. Fixed-income portfolio nên được nhìn qua rate duration, curve/key-rate exposure và spread duration, không chỉ notional.

## 17. Yield Conventions

`Coupon`, `current yield`, `YTM`, `yield-to-call`, `yield-to-worst`, `distribution yield` và money-market quoted yield là các khái niệm khác nhau.

Trước khi so hai yields, luôn kiểm tra:

```text
Cash-flow convention
Day-count convention
Compounding convention
Maturity / call assumption
Credit / liquidity / optionality
Currency
```

## 18. Credit Expected Loss

Simplified:

```text
Expected Loss ≈ PD × LGD × Exposure
```

Trong đó PD = Probability of Default, LGD = Loss Given Default. Credit spread còn chứa risk premium, liquidity premium và technical effects; không được đọc spread như pure default probability.

## 19. FX Return Decomposition

Home-currency return chính xác:

```text
Home Return = (1 + Local Asset Return) × (1 + FX Return) - 1
```

Cần phân biệt:

```text
Trading Currency
Underlying Economic Currency
Reporting Currency
Liability Currency
```

Listing bằng KRW không có nghĩa underlying USD exposure biến mất.

## 20. Futures Notional và Margin

```text
Futures Notional = Futures Price × Contract Multiplier
```

Margin là collateral, không phải capital-at-risk. Position sizing phải dựa scenario loss, notional/sensitivity và margin path chứ không dựa số tiền broker yêu cầu để mở lệnh.

## 21. Options Payoff và Greeks

Basic expiry payoff:

```text
Call = max(S - K, 0)
Put  = max(K - S, 0)
```

Trước expiry, option value còn chịu time, implied volatility, rates, dividends/borrow và surface dynamics.

Delta, Gamma, Theta, Vega, Rho là local sensitivities; chúng không thay thế full scenario grid khi market jump.

## 22. Position Sizing theo Risk Budget

Một framework cơ bản:

```text
Position Size ≈ Allowed Loss / Loss Per Unit Under Invalidation
```

Allowed loss phải được xét cùng portfolio heat, correlation/factor overlap, liquidity, gap risk và leverage. Stop distance không phải một con số technical tách khỏi portfolio context.

## 23. Expectancy

```text
Expectancy = Win Rate × Average Win - Loss Rate × Average Loss
```

Win rate cao không đảm bảo positive expectancy. Một short-vol strategy có thể thắng 90% nhưng mất rất lớn ở tail.

Trading research phải nhìn distribution, drawdown, costs, capacity và robustness.

## 24. Benchmark Convention

Benchmark phải được chọn **trước khi** đánh giá performance, phù hợp opportunity set và investable.

Một benchmark tốt phải giúp trả lời: return đến từ market beta, factor tilt, asset allocation, security selection, currency hay execution?

Không đổi benchmark sau khi strategy underperform để làm kết quả đẹp hơn.

## 25. Time Convention và Point-in-Time Discipline

Mọi research sử dụng historical data phải phân biệt:

```text
Observation Date
Publication Date
Revision Date
Decision Time
Execution Time
```

Data được revise sau này không được đưa ngược vào model như thể investor đã biết tại thời điểm quyết định. Đây là core principle chống look-ahead bias.

## 26. Source Hierarchy

Thứ tự ưu tiên chung:

```text
Official regulator / exchange / central bank / statistics
→ Audited filing / company disclosure
→ Company IR / transcript
→ High-quality data provider
→ Broker / research synthesis
→ News
→ Social / community discussion
```

Higher layer không phải luôn đúng tuyệt đối, nhưng fact nên được neo bằng primary source khi có thể.

## 27. Timestamp Rule cho dữ liệu động

Policy rate, tax rule, settlement cycle, index membership, foreign-room rule, market-access regulation và product specification có thể thay đổi.

Mọi snapshot động nên ghi rõ `as of YYYY-MM-DD` hoặc period. Nếu không có timestamp, người đọc dễ nhầm dữ liệu lịch sử thành rule hiện tại.

## 28. Base / Bull / Bear không phải ±20% tùy ý

Các scenarios phải khác nhau ở **drivers**.

Ví dụ company semiconductor:

```text
Base: ASP recovery vừa phải + utilization cải thiện
Bull: HBM mix tăng nhanh + supply discipline kéo dài
Bear: capacity ramp nhanh + demand miss → ASP giảm
```

Sau đó mới translate drivers thành revenue, margin, cash flow và valuation.

## 29. Catalyst và Invalidation

**Catalyst** là event/data có thể khiến market cập nhật expectation. **Invalidation** là evidence làm thesis không còn đúng.

Catalyst không phải điều kiện bắt buộc để một asset có value, nhưng giúp hiểu path và timing. Invalidation bắt buộc phải có để tránh thesis trở thành niềm tin không thể kiểm chứng.

## 30. Ex-Ante và Ex-Post

Ex-ante là những gì biết/ước tính trước quyết định. Ex-post là outcome sau đó.

Một decision tốt có thể có outcome xấu do uncertainty. Một decision tệ có thể kiếm tiền do luck. Review process phải tách decision quality khỏi outcome bias.

## 31. Performance Attribution Convention

Một review nên tách tối thiểu:

```text
Market / Benchmark
Asset Allocation
Factor Exposure
Security Selection
Currency
Carry / Income
Execution Costs
Fees / Tax
Behavioral Overrides
Residual
```

Tùy strategy có thể thêm duration, curve, spread, volatility hoặc sector effects.

## 32. Cross-Domain Causal Chain

Khi đọc một event, thư viện ưu tiên causal chain thay vì slogan:

```text
Event / Surprise
→ Growth & Inflation Expectations
→ Central-bank Reaction Function
→ Yield Curve / Real Yields
→ USD / Local FX
→ Credit / Liquidity
→ Sector Economics
→ Company Earnings
→ Valuation Multiple
→ Flows / Positioning
→ Asset Price
→ Portfolio P/L
```

Không phải mọi bước đều cùng direction hoặc cùng timing. Đây là lý do cùng một headline có thể tạo outcome khác nhau ở Korea, Vietnam, bonds, equities và FX.

## 33. Research Note Minimum Standard

Một note đủ tốt để lưu lâu dài nên trả lời:

```text
1. Tôi đang phân tích claim nào?
2. Return driver chính là gì?
3. Data nào là fact, estimate và assumption?
4. Market đang price điều gì?
5. Base/bull/bear path khác nhau ở driver nào?
6. Balance sheet/liquidity có chịu được bear case không?
7. Valuation/expected return có đủ bù risk không?
8. Position này duplicate factor nào trong portfolio?
9. Catalyst và invalidation là gì?
10. Review cadence là gì?
```

## 34. Quy tắc liên kết giữa các chapter

Khi một chapter dùng concept đã được giải thích ở nơi khác, ưu tiên link sang file gốc thay vì viết lại toàn bộ. Master notes giữ vai trò overview/bridge; chapter chuyên sâu là source of truth cho detailed mechanics.

Ví dụ:

- duration/credit → `02_asset_classes/02_BONDS_RATES_AND_CREDIT.md`;
- accounting/modeling → `03_company_analysis/01...` và `04_EARNINGS...`;
- macro event reaction → `04_economics/03_MACRO_DATA_PLAYBOOK.md`;
- execution → `05_trading_derivatives/03_EXECUTION...`;
- Korea/Vietnam transmission → `06_markets_korea_vietnam/03_CROSS_MARKET_GLOBAL_SHOCKS.md`.

## 35. Mental model chung

Toàn thư viện có thể được rút về một chuỗi duy nhất:

```text
Legal Claim
→ Cash-flow / Return Driver
→ Economic Regime
→ Market Expectations
→ Valuation
→ Risk & Liquidity
→ Position Size
→ Execution
→ Outcome
→ Attribution
→ Thesis Update
```

Nếu một investment idea không thể đi qua đầy đủ chuỗi này, phần còn thiếu chính là nơi research nên tiếp tục.