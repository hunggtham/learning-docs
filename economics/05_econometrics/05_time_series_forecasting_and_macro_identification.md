# Time Series, Forecasting & Macro Identification — Dependence qua thời gian và shocks

Time-series econometrics xử lý dữ liệu mà observations theo thời gian không độc lập. GDP hôm nay liên quan GDP quý trước; inflation có persistence; asset returns có volatility clustering. Mục tiêu có thể là forecast, describe dynamics hoặc identify structural shock. Ba mục tiêu này cần được tách rõ.

## 1. Time index tạo dependence

Một series:

```text
Y_t, t = 1,...,T
```

có thể phụ thuộc own lags, shocks và other series. Random train-test split thường sai vì future observations không nên dùng để predict past.

## 2. Stationarity intuition

Weak stationarity thường yêu cầu:

```text
E[Y_t] constant
Var(Y_t) constant
Cov(Y_t,Y_{t-k}) depends on k, not t
```

Stationarity làm historical relation có ý nghĩa ổn định hơn cho inference/forecast.

Economic series levels như price level hoặc GDP thường nonstationary.

## 3. Trend stationarity vs difference stationarity

Trend-stationary process:

```text
Y_t = deterministic trend + stationary noise
```

Shock effect temporary relative to trend.

Difference-stationary/unit-root process:

```text
Y_t = Y_{t-1} + ε_t
```

Shock has permanent effect on level.

Detrending và differencing imply different economics.

## 4. Unit roots

A simple AR(1):

```text
Y_t = ρY_{t-1} + ε_t
```

If `|ρ|<1`, process mean-reverts. If `ρ=1`, unit root.

Near-unit-root processes are hard to distinguish from unit root in finite samples.

## 5. Spurious regression

Regressing two unrelated trending nonstationary series can produce high R² and significant t-statistics.

This is why “both increased over decades” is not evidence of structural relation.

## 6. Differencing

First difference:

```text
ΔY_t = Y_t − Y_{t-1}
```

can remove unit root, but discards long-run level information.

Do not difference mechanically if cointegrating relation is economically meaningful.

## 7. Autocorrelation

Autocorrelation function measures correlation between Y_t and Y_{t-k}.

Persistence matters for forecasting and standard errors. Residual autocorrelation indicates model left predictable dynamics unexplained.

## 8. AR models

Autoregression:

```text
Y_t = c + φ1Y_{t-1}+...+φpY_{t-p}+ε_t
```

captures persistence from own lags.

Lag order balances omitted dynamics against parameter uncertainty. Information criteria can help, but economic horizon matters.

## 9. Moving-average process

MA(q):

```text
Y_t = μ + ε_t + θ1ε_{t-1}+...+θqε_{t-q}
```

Current outcome depends on current/past innovations.

ARMA/ARIMA combine autoregressive, moving-average and differencing structures.

## 10. Forecast vs causal model

A lagged variable may improve forecast without causing outcome. Granger predictability means X's past helps predict Y conditional on information set; it is not sufficient proof of structural causality.

## 11. Forecast evaluation

Use rolling/expanding out-of-sample evaluation respecting time order.

Metrics include MAE, RMSE and forecast log score depending objective.

Compare against simple benchmarks such as random walk or seasonal naive. Complex model should earn improvement.

## 12. Forecast uncertainty

Point forecast without interval hides uncertainty. Horizon longer → uncertainty usually widens.

Parameter uncertainty, model uncertainty and future-shock uncertainty all matter.

## 13. Structural breaks

Relations can change after policy regime, crisis, technology shift or measurement revision.

A model fit 1980–2019 may fail after pandemic. Stability tests, rolling coefficients and regime knowledge matter.

## 14. Seasonality

Monthly/quarterly series often have calendar patterns. Seasonal adjustment estimates and removes recurrent components.

Using raw and adjusted series inconsistently can create false dynamics.

## 15. Cointegration

Two I(1) series may have stationary linear combination:

```text
Y_t − βX_t = stationary
```

This means they share a long-run equilibrium relation even though levels individually nonstationary.

Cointegration is statistical long-run comovement, not automatically causal economic equilibrium.

## 16. Error-correction model

If variables cointegrated, short-run changes can respond to lagged deviation from long-run relation:

```text
ΔY_t = α(Y_{t-1} − βX_{t-1}) + short-run dynamics + ε_t
```

`α` describes adjustment speed under model.

## 17. VAR

Vector Autoregression models several variables jointly:

```text
Y_t = A1Y_{t-1}+...+ApY_{t-p}+u_t
```

Reduced-form VAR captures dynamic correlations but shocks `u_t` are generally mixtures of structural economic shocks.

## 18. Impulse response

Impulse Response Function traces dynamic response of variables after a shock.

Meaning depends entirely on shock identification. An impulse to reduced-form residual is not automatically “monetary policy shock”.

## 19. Structural VAR identification

SVAR imposes restrictions to recover structural shocks from correlated reduced-form innovations.

Restrictions may be contemporaneous ordering, long-run restrictions, sign restrictions or external instruments.

Every restriction is an economic assumption and should be defended.

## 20. Cholesky ordering

Recursive identification assumes variables earlier in ordering do not respond contemporaneously to later shocks.

Results can change with ordering. Ordering should reflect timing/institution, not convenience.

## 21. Local projections

Local projections estimate response at each horizon directly:

```text
Y_{t+h} = α_h + β_h Shock_t + controls + ε_{t+h}
```

They are flexible/robust to dynamic misspecification but can be noisy at long horizons.

## 22. Policy endogeneity

Observed rate hike is not exogenous shock: central bank raises rates because inflation/output outlook changes.

Regressing future output on rate changes mixes policy effect with information that caused policy.

Macro identification needs surprises, instruments, narrative records, high-frequency windows or structural restrictions.

## 23. High-frequency identification

Around narrow central-bank announcement windows, asset-price changes can isolate unexpected policy news under assumptions that other news is absent.

But announcements contain both policy action and information about central-bank outlook; decomposition may be needed.

## 24. Narrative identification

Historical records can classify policy changes motivated by reasons plausibly unrelated to current macro conditions.

Narrative approach relies heavily on archival judgment and completeness.

## 25. External instruments in macro

Proxy SVAR uses external instrument correlated with target structural shock but orthogonal to other shocks.

This imports IV logic into time-series setting; relevance/exclusion remain central.

## 26. Fiscal multiplier identification

Government spending responds to economy, so simple correlation is endogenous.

Strategies include military/news shocks, institutional timing, regional exposure or structural models. Each identifies different margin/context.

## 27. Event study in financial time series

Event study compares asset returns around event window to expected benchmark.

Narrow windows reduce confounding but may capture anticipation/leakage or concurrent news. Statistical significance depends on event clustering and return model.

## 28. Volatility clustering

Financial returns often show periods of high/low volatility. ARCH/GARCH model conditional variance dynamics.

They forecast risk/variance, not necessarily causal source of volatility.

## 29. Frequency mismatch

Monthly policy variables and quarterly GDP require aggregation/alignment choices. Using future information accidentally creates look-ahead bias.

Mixed-frequency models can use high-frequency indicators without crude aggregation.

## 30. Real-time data and revisions

Macro releases are revised. A forecasting model evaluated on revised final data may look better than what was possible in real time.

Use vintages when evaluating policymaker/investor forecasts.

## 31. Nowcasting

Nowcasting estimates current-quarter conditions before official data complete, using partial releases and high-frequency indicators.

It is a prediction problem; good nowcast does not establish causal interpretation of indicators.

For market-oriented application, see [`investing/04_economics/07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md`](../../investing/04_economics/07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md).

## 32. Look-ahead and survivorship bias

Forecast/backtest must only use information available at prediction date. Revised data, future constituent membership or only surviving firms create artificial performance.

## 33. Multiple horizons

Effect at `h=1` may differ sign from `h=12`. Macro dynamics require path, not single coefficient.

Report cumulative vs point responses clearly.

## 34. Failure modes

Sai lầm thứ nhất là regress trending levels and trust conventional t-statistics.

Sai lầm thứ hai là equate Granger causality with structural causality.

Sai lầm thứ ba là interpret VAR residual as named economic shock without identification.

Sai lầm thứ tư là ignore structural breaks/regime changes.

Sai lầm thứ năm là evaluate forecasts using future/revised information.

Sai lầm thứ sáu là call observed policy change exogenous.

## 35. Mental model

Khi làm time series, hãy hỏi:

1. Objective là forecast hay causal structural effect?
2. Series stationary, trending hay unit-root-like?
3. Differencing có bỏ long-run relation không?
4. Lags và seasonal structure hợp lý không?
5. Model stable qua regimes không?
6. Out-of-sample benchmark là gì?
7. “Shock” được identify bằng assumption/instrument nào?
8. Policy variable có endogenous response không?
9. Data vintage/frequency có look-ahead không?
10. Response dynamics theo horizon có economic mechanism gì?

Time-series tools thêm một lớp model risk lớn. Vì vậy econometric workflow cuối cùng cần robustness, transparent specification, external validity và interpretation discipline thay vì chỉ một preferred estimate.
