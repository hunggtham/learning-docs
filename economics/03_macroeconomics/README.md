# 03 — Macroeconomics

Macroeconomics nghiên cứu nền kinh tế ở cấp aggregate nhưng không được biến aggregate thành một “actor duy nhất”. Module này bắt đầu từ measurement, đi qua long-run productive capacity, labor/inflation, money/banking, fiscal–monetary stabilization và kết thúc ở open-economy constraints. Mỗi chapter phải tách accounting identity khỏi causal model, short run khỏi long run, và domestic mechanism khỏi application vào financial markets.

## Thứ tự học canonical

1. [National Accounts & Macro Measurement](./00_national_accounts_and_macro_measurement.md) — GDP/GNI, nominal–real, price indices, saving–investment identities, stock–flow, potential output, labor/inflation/productivity measurement và real-time revisions.
2. [Long-Run Growth & Productivity](./01_long_run_growth_and_productivity.md) — production function, Solow, capital deepening, technology, growth accounting, human capital, endogenous growth, convergence, institutions, structural transformation và misallocation.
3. [Labor, Unemployment & Inflation](./02_labor_unemployment_and_inflation.md) — labor-force flows, search/matching, wage setting, Phillips curve, expectations, inflation mechanisms, hysteresis và empirical boundaries.
4. [Money, Banking & Monetary Policy](./03_money_banking_and_monetary_policy.md) — bank/central-bank balance sheets, money creation, capital vs reserves, policy-rate transmission, real rates, QE, credit/exchange-rate channels và financial stability.
5. [Fiscal Policy & Business Cycles](./04_fiscal_policy_and_business_cycles.md) — multipliers, automatic stabilizers, state dependence, debt dynamics, fiscal space, inventory/financial accelerators, RBC/New Keynesian perspectives và fiscal–monetary interaction.
6. [Open Economy, Exchange Rates & Crises](./05_open_economy_exchange_rates_and_crises.md) — balance of payments, `CA = S − I`, nominal/real FX, PPP, interest parity, trilemma, capital flows, currency/maturity mismatch, sudden stops và crisis mechanisms.

## Learning spine

```text
Measurement / accounting identities
→ long-run productive capacity
→ short-run labor and price dynamics
→ money / banking / interest-rate transmission
→ fiscal and monetary stabilization
→ open-economy external constraints
→ empirical identification
```

Module cố ý bắt đầu bằng measurement vì macro rất dễ nhầm identity với theory. `S = I + NX`, government budget constraint hay balance-of-payments equality là accounting structures; chúng không tự nói direction of causality. Causal interpretation phải đi qua behavioral assumptions, institutional regime và evidence.

## Kết quả cần đạt

Sau module này, người học phải có thể phân biệt stock/flow, nominal/real, gross/net và aggregate/per-capita; đọc GDP/inflation/unemployment mà không bỏ revisions hoặc denominator effects; giải thích vì sao capital accumulation khác productivity growth; tách frictional/structural/cyclical unemployment; đọc inflation qua demand, supply, expectations và markups; dựng balance-sheet logic của banks và central bank; đánh giá fiscal multiplier theo state/regime; phân tích debt dynamics qua primary balance và `r − g`; đồng thời đọc current account, exchange rate và capital flows qua external balance-sheet exposures thay vì một headline ratio.

Người học cũng phải biết uncertainty nằm ở đâu. Potential output, neutral rate, NAIRU và expected inflation đều không quan sát trực tiếp; chúng là model-dependent estimates. Không dùng một point estimate như fact tuyệt đối.

## Boundary với Investing Economics

[`investing/04_economics/`](../../investing/04_economics/README.md) tiếp tục giữ application layer cho macro data playbook, liquidity, market transmission, crisis cases, policy regimes, debt/demographics và nowcasting. `economics/03_macroeconomics/` là canonical general-purpose layer: giải mechanism, assumptions và accounting trước khi map sang asset prices hoặc positioning.

Quy tắc là **cross-link, không duplicate**. Khi Investing cần giải thích nguyên lý chung, link về chapter canonical tại đây; khi Economics cần market-specific monitoring hoặc investment interpretation, link sang Investing.

## Boundary với Econometrics

Macro model tạo predictions nhưng nhiều biến endogenous cùng lúc. Ví dụ rate hike thường xảy ra khi inflation/outlook đã thay đổi, nên correlation giữa rate và inflation không đo causal effect của policy. Fiscal spending cũng phản ứng với recession, exchange rate phản ứng với both domestic and global shocks.

Vì vậy bước tiếp theo là [Econometrics](../README.md#learning-route-và-coverage-target): measurement → identification → regression → experiments/quasi-experiments → IV/DiD/panel/time series. Macro evidence cần đặc biệt chú ý simultaneity, expectations, regime changes và real-time data revisions.

## Boundary với Applied Economics và History

Labor, public finance, trade, development và industrial organization sẽ dùng macro constraints nhưng cần micro foundations và causal evidence riêng. Economic History & Institutions sẽ dùng macro sequence để so sánh growth, crises, monetary regimes và state capacity qua thời gian; không duplicate chronology từ World History.

## Checklist khi đọc một macro claim

Trước khi chấp nhận một kết luận, kiểm tra: đại lượng đang đo là gì; accounting identity nào đang dùng; behavioral mechanism nào biến identity thành prediction; horizon short/long run; regime monetary/fiscal/exchange-rate; balance-sheet exposure; expectations; distributional heterogeneity; data vintage; và identification strategy nào có thể phân biệt causal effect với policy response/endogeneity.
