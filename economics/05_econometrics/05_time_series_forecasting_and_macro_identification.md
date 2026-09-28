# Thời gian (time / 시간) Series, Forecasting & Macro Identification — Dependence qua thời gian và shocks

> **Mạch đọc:** Đặt **thời gian (time / 시간) Series, Forecasting & Macro Identification — Dependence qua thời gian và shocks** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. thời gian (time / 시간) chỉ mục (index / 인덱스) tạo dependence** sang **2. Stationarity intuition**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Time-series econometrics xử lý dữ liệu mà observations theo thời gian không độc lập. GDP hôm nay liên quan GDP quý trước; inflation có persistence; asset returns có volatility clustering. Mục tiêu có thể là forecast, describe dynamics hoặc identify structural shock. Ba mục tiêu này cần được tách rõ.

## 1. thời gian (time / 시간) chỉ mục (index / 인덱스) tạo dependence

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

Stationarity làm historical quan hệ (relation / 관계) có ý nghĩa ổn định hơn cho suy luận (inference / 추론)/forecast.

Economic series levels như price mức (level / 수준) hoặc GDP thường nonstationary.

## 3. Trend stationarity vs difference stationarity

Trend-stationary tiến trình (process / 프로세스):

```text
Y_t = deterministic trend + stationary noise
```

Shock tác động (effect / 효과) temporary relative to trend.

Difference-stationary/unit-root tiến trình (process / 프로세스):

```text
Y_t = Y_{t-1} + ε_t
```

Shock has permanent tác động (effect / 효과) on mức (level / 수준).

Detrending và differencing imply different economics.

## 4. đơn vị (unit / 단위) roots

A simple AR(1):

```text
Y_t = ρY_{t-1} + ε_t
```

If `|ρ|<1`, tiến trình (process / 프로세스) mean-reverts. If `ρ=1`, đơn vị (unit / 단위) gốc (root / 루트).

Near-unit-root processes are hard to distinguish from đơn vị (unit / 단위) gốc (root / 루트) in finite samples.

## 5. Spurious regression

Regressing two unrelated trending nonstationary series can produce high R² and significant t-statistics.

This is why “both increased over decades” is not bằng chứng (evidence / 증거) of structural quan hệ (relation / 관계).

## 6. Differencing

First difference:

```text
ΔY_t = Y_t − Y_{t-1}
```

can remove đơn vị (unit / 단위) gốc (root / 루트), but discards long-run mức (level / 수준) thông tin (information / 정보).

Do not difference mechanically if cointegrating quan hệ (relation / 관계) is economically meaningful.

## 7. Autocorrelation

Autocorrelation hàm (function / 함수) measures correlation between Y_t and Y_{t-k}.

Persistence matters for forecasting and tiêu chuẩn (standard / 표준) errors. Residual autocorrelation indicates mô hình (model / 모델) left predictable dynamics unexplained.

## 8. AR các mô hình (models / 모델들)

Autoregression:

```text
Y_t = c + φ1Y_{t-1}+...+φpY_{t-p}+ε_t
```

captures persistence from own lags.

Lag thứ tự (order / 순서) balances omitted dynamics against parameter bất định (uncertainty / 불확실성). thông tin (information / 정보) criteria can help, but economic horizon matters.

## 9. Moving-average tiến trình (process / 프로세스)

MA(q):

```text
Y_t = μ + ε_t + θ1ε_{t-1}+...+θqε_{t-q}
```

Hiện tại (current / 현재) kết quả (outcome / 결과) depends on hiện tại (current / 현재)/past innovations.

ARMA/ARIMA combine autoregressive, moving-average and differencing structures.

## 10. Forecast vs nhân quả (causal / 인과적) mô hình (model / 모델)

A lagged variable may improve forecast without causing kết quả (outcome / 결과). Granger predictability means X's past helps predict Y conditional on thông tin (information / 정보) set; it is not sufficient proof of structural causality.

## 11. Forecast evaluation

Use rolling/expanding out-of-sample evaluation respecting thời gian (time / 시간) thứ tự (order / 순서).

Metrics include MAE, RMSE and forecast log score depending mục tiêu (objective / 목표).

Compare against simple benchmarks such as random walk or seasonal naive. Complex mô hình (model / 모델) should earn improvement.

## 12. Forecast bất định (uncertainty / 불확실성)

Điểm (point / 지점) forecast without interval hides bất định (uncertainty / 불확실성). Horizon longer → bất định (uncertainty / 불확실성) usually widens.

Parameter bất định (uncertainty / 불확실성), mô hình (model / 모델) bất định (uncertainty / 불확실성) and future-shock bất định (uncertainty / 불확실성) all matter.

## 13. Structural breaks

Relations can thay đổi (change / 변경) after chính sách (policy / 정책) regime, crisis, technology shift or đo lường (measurement / 측정) revision.

A mô hình (model / 모델) fit 1980–2019 may thất bại (fail / 실패) after pandemic. Stability tests, rolling coefficients and regime kiến thức (knowledge / 지식) matter.

## 14. Seasonality

Monthly/quarterly series often have calendar patterns. Seasonal adjustment estimates and removes recurrent components.

Using raw and adjusted series inconsistently can create false dynamics.

## 15. Cointegration

Two I(1) series may have stationary tuyến tính (linear / 선형) combination:

```text
Y_t − βX_t = stationary
```

This means they share a long-run equilibrium quan hệ (relation / 관계) even though levels individually nonstationary.

Cointegration is statistical long-run comovement, not automatically nhân quả (causal / 인과적) economic equilibrium.

## 16. Error-correction mô hình (model / 모델)

If variables cointegrated, short-run changes can respond to lagged deviation from long-run quan hệ (relation / 관계):

```text
ΔY_t = α(Y_{t-1} − βX_{t-1}) + short-run dynamics + ε_t
```

`α` describes adjustment speed under mô hình (model / 모델).

## 17. VAR

Véc-tơ (vector / 벡터) Autoregression các mô hình (models / 모델들) several variables jointly:

```text
Y_t = A1Y_{t-1}+...+ApY_{t-p}+u_t
```

Reduced-form VAR captures động (dynamic / 동적) correlations but shocks `u_t` are generally mixtures of structural economic shocks.

## 18. Impulse phản hồi (response / 응답)

Impulse phản hồi (response / 응답) hàm (function / 함수) traces động (dynamic / 동적) phản hồi (response / 응답) of variables after a shock.

Meaning depends entirely on shock identification. An impulse to reduced-form residual is not automatically “monetary chính sách (policy / 정책) shock”.

## 19. Structural VAR identification

SVAR imposes restrictions to recover structural shocks from correlated reduced-form innovations.

Restrictions may be contemporaneous thứ tự (ordering / 순서), long-run restrictions, sign restrictions or bên ngoài (external / 외부) instruments.

Every restriction is an economic giả định (assumption / 가정) and should be defended.

## 20. Cholesky thứ tự (ordering / 순서)

Recursive identification assumes variables earlier in thứ tự (ordering / 순서) do not respond contemporaneously to later shocks.

Results can thay đổi (change / 변경) with thứ tự (ordering / 순서). thứ tự (ordering / 순서) should reflect timing/institution, not convenience.

## 21. cục bộ (local / 로컬) projections

Cục bộ (local / 로컬) projections estimate phản hồi (response / 응답) at each horizon directly:

```text
Y_{t+h} = α_h + β_h Shock_t + controls + ε_{t+h}
```

They are flexible/robust to động (dynamic / 동적) misspecification but can be noisy at long horizons.

## 22. chính sách (policy / 정책) endogeneity

Observed tỷ lệ (rate / 비율) hike is not exogenous shock: central bank raises rates because inflation/đầu ra (output / 출력) outlook changes.

Regressing future đầu ra (output / 출력) on tỷ lệ (rate / 비율) changes mixes chính sách (policy / 정책) tác động (effect / 효과) with thông tin (information / 정보) that caused chính sách (policy / 정책).

Macro identification needs surprises, instruments, narrative records, high-frequency windows or structural restrictions.

## 23. High-frequency identification

Around narrow central-bank announcement windows, asset-price changes can isolate unexpected chính sách (policy / 정책) news under các giả định (assumptions / 가정들) that other news is absent.

But announcements contain both chính sách (policy / 정책) hành động (action / 동작) and thông tin (information / 정보) about central-bank outlook; decomposition may be needed.

## 24. Narrative identification

Historical records can classify chính sách (policy / 정책) changes motivated by reasons plausibly unrelated to hiện tại (current / 현재) macro conditions.

Narrative approach relies heavily on archival judgment and completeness.

## 25. bên ngoài (external / 외부) instruments in macro

Proxy SVAR uses bên ngoài (external / 외부) instrument correlated with mục tiêu (target / 대상) structural shock but orthogonal to other shocks.

This imports IV lô-gic (logic / 논리) into time-series setting; relevance/exclusion remain central.

## 26. Fiscal multiplier identification

Government spending responds to economy, so simple correlation is endogenous.

Strategies include military/news shocks, institutional timing, regional exposure or structural các mô hình (models / 모델들). Each identifies different margin/ngữ cảnh (context / 맥락).

## 27. sự kiện (event / 이벤트) study in financial thời gian (time / 시간) series

Sự kiện (event / 이벤트) study compares asset returns around sự kiện (event / 이벤트) cửa sổ (window / 윈도우) to expected benchmark.

Narrow windows reduce confounding but may capture anticipation/leakage or concurrent news. Statistical significance depends on sự kiện (event / 이벤트) clustering and return mô hình (model / 모델).

## 28. Volatility clustering

Financial returns often show periods of high/low volatility. ARCH/GARCH mô hình (model / 모델) conditional variance dynamics.

They forecast rủi ro (risk / 위험)/variance, not necessarily nhân quả (causal / 인과적) nguồn (source / 소스) of volatility.

## 29. Frequency mismatch

Monthly chính sách (policy / 정책) variables and quarterly GDP require aggregation/alignment choices. Using future thông tin (information / 정보) accidentally creates look-ahead độ lệch (bias / 편향).

Mixed-frequency các mô hình (models / 모델들) can use high-frequency indicators without crude aggregation.

## 30. Real-time dữ liệu (data / 데이터) and revisions

Macro releases are revised. A forecasting mô hình (model / 모델) evaluated on revised final dữ liệu (data / 데이터) may look better than what was possible in real thời gian (time / 시간).

Use vintages when evaluating policymaker/investor forecasts.

## 31. Nowcasting

Nowcasting estimates current-quarter conditions before official dữ liệu (data / 데이터) complete, using partial releases and high-frequency indicators.

It is a prediction bài toán (problem / 문제); good nowcast does not establish nhân quả (causal / 인과적) interpretation of indicators.

For market-oriented ứng dụng (application / 애플리케이션), see [`investing/04_economics/07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md`](../../investing/04_economics/07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md).

## 32. Look-ahead and survivorship độ lệch (bias / 편향)

Forecast/backtest must only use thông tin (information / 정보) available at prediction date. Revised dữ liệu (data / 데이터), future constituent membership or only surviving firms create artificial hiệu năng (performance / 성능).

## 33. Multiple horizons

Tác động (effect / 효과) at `h=1` may differ sign from `h=12`. Macro dynamics require đường dẫn (path / 경로), not single coefficient.

Report cumulative vs điểm (point / 지점) responses clearly.

## 34. thất bại (failure / 실패) modes

Sai lầm thứ nhất là regress trending levels and trust conventional t-statistics.

Sai lầm thứ hai là equate Granger causality with structural causality.

Sai lầm thứ ba là interpret VAR residual as named economic shock without identification.

Sai lầm thứ tư là ignore structural breaks/regime changes.

Sai lầm thứ năm là evaluate forecasts using future/revised thông tin (information / 정보).

Sai lầm thứ sáu là lời gọi (call / 호출) observed chính sách (policy / 정책) thay đổi (change / 변경) exogenous.

## 35. mô hình tư duy (mental model / 사고 모델)

Khi làm thời gian (time / 시간) series, hãy hỏi:

1. mục tiêu (objective / 목표) là forecast hay nhân quả (causal / 인과적) structural tác động (effect / 효과)?
2. Series stationary, trending hay unit-root-like?
3. Differencing có bỏ long-run quan hệ (relation / 관계) không?
4. Lags và seasonal cấu trúc (structure / 구조) hợp lý không?
5. mô hình (model / 모델) stable qua regimes không?
6. Out-of-sample benchmark là gì?
7. “Shock” được identify bằng giả định (assumption / 가정)/instrument nào?
8. chính sách (policy / 정책) variable có endogenous phản hồi (response / 응답) không?
9. dữ liệu (data / 데이터) vintage/frequency có look-ahead không?
10. phản hồi (response / 응답) dynamics theo horizon có economic cơ chế (mechanism / 메커니즘) gì?

Time-series tools thêm một lớp mô hình (model / 모델) rủi ro (risk / 위험) lớn. Vì vậy econometric workflow cuối cùng cần robustness, transparent specification, bên ngoài (external / 외부) validity và interpretation discipline thay vì chỉ một preferred estimate.

> **Bàn giao:** Sau **35. mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 measurement data and estimands](./00_measurement_data_and_estimands.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
