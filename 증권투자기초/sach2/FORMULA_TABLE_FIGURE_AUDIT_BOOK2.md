# FORMULA / TABLE / FIGURE AUDIT — 증권투자기초 Sách 2

> Authority: `증권투자기초/raw/sach2.md`.
>
> Contract: a knowledge-bearing formula/table/figure is `PASS` only when the learning route gives the reader a way to read it, preserves variables/assumptions that matter, explains the mechanism after the block, states a boundary, and supplies a worked check when a novice would otherwise be unable to use it.

## Formula and quantitative-contract audit

| ID | Source topic | Formula / quantitative relation | Variables / assumption preserved | Learning route | Result |
|---|---|---|---|---|---|
| F01 | compound value | `FV = PV(1+r)^n` | PV/FV, per-period r, n | 02 §1 | PASS |
| F02 | present value | `PV = FV/(1+r)^n` | same period convention | 02 §1 | PASS |
| F03 | CSI | survey-balance reconstruction from positive/negative current/expected responses | OCR limitation explicitly stated; worked 65 | 01 §3 | PASS |
| F04 | BSI | `[(positive-negative)/total]×100+100` | response counts; 100 as neutral balance | 01 §3 | PASS |
| F05 | CI/DI | weighted magnitude vs breadth | weights vs count breadth separated | 01 §3 | PASS |
| F06 | ROI | profit / invested capital | numerator/denominator scope stated generically | 01 §5 | PASS |
| F07 | ROE | after-tax profit / average equity | average-equity convention and leverage boundary | 01 §5 | PASS |
| F08 | DuPont | margin × asset turnover × equity multiplier | same-period consistency | 01 §5 | PASS |
| F09 | CAPM | `E(Ri)=Rf+βi[E(Rm)-Rf]` | Rf, beta, market premium; model boundary | 02 §1 | PASS |
| F10 | NPV | discounted inflows minus investment | cash-flow timing and hurdle rate | 02 §2 | PASS |
| F11 | dividend discount model | PV of dividends + terminal value | D_t, k, horizon/terminal value | 02 §2 | PASS |
| F12 | Gordon growth | `P0=D1/(k-g)` | `D1=D0(1+g)`; `k>g` | 02 §2 | PASS |
| F13 | FCFE/FCFF bridge | `FCFF = FCFE + Interest×(1−T) + net debt repayment` | net debt repayment = debt repaid − new borrowing; equivalent to subtracting Net Borrowing | 02 §3 | PASS |
| F14 | WACC | `[E/(D+E)]Re + [D/(D+E)]Rd(1−T)` | market-value weights, cost of equity/debt, tax-shield assumption; FCFF ownership | 02 §3 | PASS |
| F15 | EVA | `NOPAT - Invested Capital×WACC` | operating scope and capital charge | 02 §4 | PASS |
| F16 | EVA/ROIC | `Invested Capital×(ROIC-WACC)` | value creation requires return > capital cost | 02 §4 | PASS |
| F17 | PER | price / EPS | negative/cyclical earnings boundary | 02 §5 | PASS |
| F18 | PBR | price / BPS | ROE and asset-quality relation | 02 §6 | PASS |
| F19 | PSR | price / sales per share | margin/cash-conversion boundary | 02 §7 | PASS |
| F20 | EV/EBITDA | enterprise value / EBITDA | EV scope; EBITDA ≠ FCF | 02 §8 | PASS |
| F21 | SMA | rolling arithmetic mean | window `n`; lag | 03 §2/§5 | PASS |
| F22 | EMA | `EMA_t=αP_t+(1-α)EMA_{t-1}` | alpha/window dependence | 03 §5 | PASS |
| F23 | RSI | `100-100/(1+avg gain/avg loss)` | window/threshold convention; 30/70 not automatic signal | 03 §5 | PASS |
| F24 | MACD | fast EMA − slow EMA; signal EMA | fast/slow/signal relation; lag | 03 §5 | PASS |
| F25 | Stochastic | close relative to recent high-low range | lookback/threshold dependence | 03 §5 | PASS |
| F26 | Bollinger Bands | `SMA ± k·σ` | k/window; width ≠ direction | 03 §5 | PASS |
| F27 | Envelope | percentage band around moving average | band percentage/regime dependence | 03 §5 | PASS |
| F28 | OBV | cumulative signed volume | sign rule; volume-data quality | 03 §5 | PASS |
| F29 | VR | `[V↑+0.5V=]/[V↓+0.5V=]×100` | up/down/unchanged-volume convention | 03 §5 | PASS |
| F30 | portfolio variance | `w1²σ1²+w2²σ2²+2w1w2ρσ1σ2` | weights, volatility, correlation | 04 §3 | PASS |
| F31 | index construction | divisor / weighting examples | price-weight vs market-cap-weight; corporate actions | 04 §4 | PASS |
| F32 | bond valuation | `P=Σ C/(1+y)^t + F/(1+y)^n` | C/F/y/n; periodicity | 05 §1/§6 | PASS |
| F33 | coupon rate | annual coupon / face value | face-value denominator | 06 §1 | PASS |
| F34 | current yield | annual coupon / current price | excludes capital gain/loss | 06 §1 | PASS |
| F35 | YTM/IRR | price equals PV of coupon+principal at y | hold-to-maturity/reinvestment/no-default boundary | 06 §1 | PASS |
| F36 | spot/forward relation | `(1+s2)^2=(1+s1)(1+f1,2)` | same compounding convention | 06 §2 | PASS |
| F37 | Macaulay duration | PV-weighted cash-flow time | cash-flow timing and YTM | 06 §4 | PASS |
| F38 | modified duration | `D_mod=D_Mac/(1+y)` in annual convention | compounding convention | 06 §4 | PASS |
| F39 | first-order price sensitivity | `ΔP/P≈-D_modΔy` | small/local yield move | 06 §4 | PASS |
| F40 | convexity | duration term + `1/2·Convexity·Δy²` | second-order local approximation | 06 §4 | PASS |
| F41 | bond total return | price change + income, with reinvestment convention | clean/dirty/accrued/reinvestment boundary | 06 §5 | PASS |
| F42 | tracking error | SD(portfolio return − benchmark return) | same universe/time/currency convention | 06 §5 | PASS |
| F43 | repo haircut | cash advance = collateral value × (1−haircut) | collateral value/haircut; margin-call example | 06 §6 | PASS |

## Knowledge-bearing table / figure audit

| ID | Source artifact | Reconstruction in learning route | Boundary / ambiguity | Result |
|---|---|---|---|---|
| TF01 | business-cycle horizon table | Kitchin/Juglar/Kondratiev table + how to read horizon | durations are textbook approximations, not timing rules | PASS |
| TF02 | CSI/BSI tables | formulas + worked survey examples | exact current survey methodology is not claimed | PASS |
| TF03 | CI/DI comparison | magnitude-vs-breadth worked scenario | weights and breadth can diverge | PASS |
| TF04 | leading/coincident/lagging indicator table | three rows with use and timing boundary | one indicator does not establish causality | PASS |
| TF05 | BCG matrix | four cells reconstructed with capital-allocation questions | label ≠ profitability/valuation | PASS |
| TF06 | financial-statement block | BS/IS/CF roles + cross-reading sequence | accounting framework ≠ economic quality | PASS |
| TF07 | financial-ratio source table | economic families retained | exact corrupted formulas/cells are SRC-A03 | SOURCE_AMBIGUITY |
| TF08 | technical price-pattern figures | each named pattern has structure, confirmation and invalidation boundary | Diamond exact target geometry is SRC-A04 | PASS-WITH-AMBIGUITY |
| TF09 | candlestick groups | seven patterns reconstructed individually | context/confirmation/volume required | PASS |
| TF10 | technical-indicator formulas/charts | SMA/EMA/RSI/MACD/Bollinger/OBV/VR/P&F mechanisms | thresholds are textbook parameters | PASS |
| TF11 | stock-index examples | price-/cap-/equal-weight construction + divisor example | current index constituents/methodology not asserted | PASS |
| TF12 | fixed-income product taxonomy | CB/BW/EB/callable/puttable/ABS/MBS/CMO/FRN/reverse floater/etc split | separate Asset-Backed Bond heading is SRC-A05 | PASS-WITH-AMBIGUITY |
| TF13 | indexed-bond example table | principal/coupon adjustment worked example | index lag/floor/terms must be specified | PASS |
| TF14 | term-structure theories | four theories placed side by side | theory is explanatory lens, not deterministic forecast | PASS |
| TF15 | credit-rating table | investment-grade/speculative boundary and agency notation | rating is relative assessment, not guarantee | PASS |
| TF16 | duration/convexity figure logic | Macaulay/modified worked example + curvature equation | callable/MBS cash flows can change | PASS |
| TF17 | bond-index taxonomy | price/coupon/yield/total-return distinctions | benchmark convention must match portfolio | PASS |
| TF18 | primary/secondary + auction table | market distinction + discriminatory vs uniform-price mechanisms | jurisdiction/prospectus rules can differ | PASS |
| TF19 | repo mechanism | collateral/haircut worked example | haircut does not remove counterparty/liquidity risk | PASS |
| TF20 | stock review figures/options | recoverable concept clusters mapped | exact OCR-broken cells are SRC-A06 | SOURCE_AMBIGUITY |
| TF21 | bond review figures/options | recoverable concept clusters mapped | exact OCR-broken cells are SRC-A07 | SOURCE_AMBIGUITY |

## Result

- Formula/quantitative-contract rows: **43 PASS**.
- Table/figure rows: **21**.
- Table/figure rows with explicit source ambiguity boundary: **5** (TF07, TF08, TF12, TF20, TF21).
- No formula required by the semantic inventory is `PARTIAL` or `MISSING`.
