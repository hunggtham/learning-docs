# FORMULA / TABLE / FIGURE AUDIT — 증권투자기초 Sách 3

## Formula contract

Each important formula is checked for purpose, variables/units, assumptions, mechanism, worked use and boundary. PASS-ENRICHMENT is explicitly excluded from source-completeness evidence.

| ID | Source | Formula / purpose | Representation | Variables / units | Assumption / failure boundary | Learning evidence | Result |
|---|---|---|---|---|---|---|---|
| F01 | p.14–16 | Expected value | E(X)=Σxᵢpᵢ / ∫xf(x)dx | X/value + probability/density; same outcome unit | probabilities sum/integrate to 1 | 01 §1 | PASS |
| F02 | p.17–20 | Population/sample variance | σ²=Σ(x−μ)²/n; s²=Σ(x−x̄)²/(n−1) | variance uses squared data unit | population vs sample choice explicit | 01 §2 | PASS |
| F03 | p.18–20 | Standard deviation | σ=√Var(X) | same unit as X | variance non-negative | 01 §2 | PASS |
| F04 | p.22–26 | Correlation | ρ=Cov(X,Y)/(σXσY) | dimensionless, −1…1 | linear association; σ non-zero | 01 §3 | PASS |
| F05 | p.24–26 | Covariance | E[(X−EX)(Y−EY)] | product of X/Y units | same observation/probability system | 01 §3 | PASS |
| F06 | p.27–28 | Linear transformation | E(aX+b)=aEX+b; Var(aX+b)=a²VarX | a rescales units | finite moments | 01 §4 | PASS |
| F07 | p.29 | Combined variance | Var(aX+bY)=a²σX²+b²σY²+2abCov | same return² unit | same horizon; joint covariance defined | 01 §4 | PASS |
| F08 | p.29–31 | Least-squares regression | β̂=Σ(X−X̄)(Y−Ȳ)/Σ(X−X̄)²; α̂=Ȳ−β̂X̄ | β units Y/X; α units Y | linear approximation; residual mechanism stated | 01 §4 | PASS |
| F09 | p.54 | Portfolio expected return | E(rp)=ΣwᵢE(rᵢ) | weights dimensionless; returns same horizon | weights define portfolio exposure | 02 §2 | PASS |
| F10 | p.54–56 | Two-asset portfolio variance | wA²σA²+wB²σB²+2wAwBCovAB | return² | same horizon; covariance regime matters | 02 §2 | PASS |
| F11 | p.57 | Multi-asset portfolio variance | w'Σw | return² | covariance matrix consistent/finite | 02 §2 | PASS |
| F12 | p.60–61; p.74 | Two-asset MVP weight | (σB²−ρσAσB)/(σA²+σB²−2ρσAσB) | dimensionless weight | unconstrained two-asset solution | 02 §3A | PASS |
| F13 | p.64 | CAL | E(rp)=rf+[E(rA)−rf]/σA × σp | return vs volatility same horizon | borrow/lend at rf; scalable risky asset | 02 §5 | PASS |
| F14 | p.83–85 | CML | E(rp)=rf+[E(rm)−rf]/σm × σp | return and σ same horizon | efficient portfolios + CAPM world | 03 §1 | PASS |
| F15 | p.86–88 | Beta | βi=Cov(ri,rm)/Var(rm) | dimensionless | same horizon; market proxy defined | 03 §2 | PASS |
| F16 | p.89–92 | CAPM/SML | E(ri)=rf+βi[E(rm)−rf] | return same horizon/scale | CAPM equilibrium assumptions | 03 §2 | PASS |
| F17 | p.137–139 | MWR | IRR root of investor cash-flow equation | cash flows same currency; r per period | cash-flow timing explicit | 04 §1 | PASS |
| F18 | p.137–139 | TWR | RTW=Π(1+rt)−1 | dimensionless return | break at external cash flows | 04 §1 | PASS |
| F19 | p.139 | Geometric return | 1+r̄g=[Π(1+rt)]^(1/T) | per-period compounded rate | standard real-valued form requires valid growth factors | 04 §1 | PASS |
| F20 | p.139–141 | Sharpe | (rp−rf)/σp | excess return per total volatility | same horizon; σ>0 | 04 §2 | PASS |
| F21 | p.140 | Treynor | (rp−rf)/βp | return per beta unit | diversified portfolio; β≠0 | 04 §2 | PASS |
| F22 | p.141 | Jensen alpha | αp=rp−[rf+βp(rm−rf)] | return | CAPM benchmark and beta horizon consistent | 04 §2 | PASS |
| F23 | p.158 | Cost of equity/CAPM | ke=rf+βe(E(rm)−rf) | return | CAPM benchmark; equity beta | 04 §3 | PASS |
| F24 | p.159 | WACC | E/(D+E)ke + D/(D+E)kd(1−T) | rate | market-value weights; tax-shield assumption | 04 §3 | PASS |
| F25 | p.161–162 | DCF/FCFF | V0=ΣCFt/(1+k)^t + TVT/(1+k)^T | cash flow/value same currency; k per period | cash flow and discount-rate ownership/timing matched | 04 §4 | PASS |
| F26 | p.162 | Residual/terminal value | TVT=FCF(T+1)/(k−g) as learning bridge | currency at T | k>g; stable-growth boundary | 04 §4 | PASS |
| F27 | p.162–163 | EVA | EVA=(ROIC−WACC)×IC = NOPAT−capital charge | currency | ROIC/WACC/IC same operating scope | 04 §4 | PASS |
| F28 | p.230–236; p.362 | Index-futures theoretical price | F≈S[1+(r−q)T] in source-simple convention | index/price; annual rates + year fraction | carry convention/dividend/funding boundary | 05 §2 | PASS |
| F29 | p.230–236 | Basis | basis=futures−spot | price/index points | same underlying/time observation | 05 §2 | PASS |
| F30 | p.251–257 | Long call/put expiry P&L | max(ST−K,0)−premium; max(K−ST,0)−premium | same price/currency after multiplier | expiry; fees/funding excluded | 05 §3 | PASS |
| F31 | p.251–257 | Option breakeven | call K+premium; put K−premium | price units | long option at expiry | 05 §3 | PASS |
| F32 | p.256; p.362–364 | Put-call parity | C−P=S−PV(K) | same currency/strike/maturity | European/no-arbitrage convention; dividend/funding boundary | 05 §2–3 | PASS |
| F33 | p.255–267 | Delta/gamma hedge | hedge units≈option position×delta; gamma drives rebalance | underlying units/delta dimensionless | local/dynamic hedge; gap/transaction cost remain | 05 §3 | PASS |
| F34 | p.301–302 | Duration price sensitivity | ΔP/P≈−DmodΔy | D years; yield decimal; relative price | small yield move; convexity omitted | 06 §1 | PASS |
| F35 | editorial bridge from p.301–302 | BPV/DV01 hedge | DV01≈P×Dmod×0.0001 | currency per bp | enrichment label; source has duration not BPV/DV01 wording | 06 §1 | PASS-ENRICHMENT |
| F36 | p.293; p.365 | IFR/forward-rate relation | (1+long×Tlong)=(1+near×Tnear)(1+f×ΔT) in simple-rate example | annualized rate + year fractions | same compounding/day-count | 06 §1 | PASS |
| F37 | p.305 | FX interest parity | F=S(1+rdT)/(1+rfT) in simple-rate convention | domestic currency per foreign currency | same credit/collateral/funding assumptions | 06 §2 | PASS |
| F38 | p.317 | CDS LGD/protection leg | LGD=1−R; protection≈N×LGD | currency on notional N | simplified settlement; fair spread also needs default timing/discounting | 06 §3 | PASS |
| F39 | p.326 | Commodity carry | F≈S+S(r+s−c)T | commodity price; annualized rates | simple carry; storage/convenience approximated | 06 §4 | PASS |
| F40 | p.327–330 | Commodity return decomposition | Rtotal≈Rprice+Rroll+Rcollateral−fees | return | index-provider convention can differ | 06 §4 | PASS |
| F41 | p.336–337; p.353–359 | Autocall/structured branch payoff | piecewise early-redemption / maturity / KI logic | principal/coupon currency; thresholds vs initial | path/observation dates/worst-of/issuer terms explicit | 07 §2 | PASS |
| F42 | p.347 | Daily-reset leverage | Vt=Vt−1(1+Lrt) schematic | return multiplier L | daily reset/path dependence/volatility drag | 07 §2 | PASS |

## Knowledge-bearing tables and figures

| ID | Source | Artifact | Verification | Handling/evidence | Result |
|---|---|---|---|---|---|
| TF01 | p.19–20 | 12-month return table for sample variance | numeric values/conclusion readable | 01 §2 | VERIFIED |
| TF02 | p.21–26 | scatter/correlation examples | mechanism readable; exact layout unnecessary | 01 §3 | VERIFIED |
| TF03 | p.59–64 | portfolio correlation/frontier/CAL figures | curve meaning reconstructed from prose/formulas | 02 §2–5 | VERIFIED |
| TF04 | p.83–92 | CML/SML figures | axes/slope/intercept reconstructed from prose/formulas | 03 §1–2 | VERIFIED |
| TF05 | p.164 | relative-valuation multiple table | PER/PBR/EV-EBITDA etc readable | 04 §5 | VERIFIED |
| TF06 | p.251 | KOSPI200 futures market quote | exact cells unreliable | SOURCE_AMBIGUITIES SRC-A01 | SOURCE_AMBIGUITY |
| TF07 | p.264–267 | option price/Greeks tables/charts | mechanism readable; exact cells unreliable | SOURCE_AMBIGUITIES SRC-A02 | SOURCE_AMBIGUITY |
| TF08 | p.268 | KOSPI200 option contract specification | historical/time-sensitive + OCR broken | SOURCE_AMBIGUITIES SRC-A03 | SOURCE_AMBIGUITY |
| TF09 | p.297 | 10Y Treasury futures specification | partial OCR + historical spec | SOURCE_AMBIGUITIES SRC-A05 | SOURCE_AMBIGUITY |
| TF10 | p.308 | USD futures specification | partial OCR + historical spec | SOURCE_AMBIGUITIES SRC-A06 | SOURCE_AMBIGUITY |
| TF11 | p.320 | credit pool/acronym table/text | pool semantics readable; exact acronym corrupted | SOURCE_AMBIGUITIES SRC-A07 | SOURCE_AMBIGUITY |
| TF12 | p.328 | crude futures contract screenshot | partial OCR + historical spec | SOURCE_AMBIGUITIES SRC-A08 | SOURCE_AMBIGUITY |
| TF13 | p.336–338 | autocall stepdown payoff/conditions | threshold/coupon/KI prose readable | 07 §2 | VERIFIED |
| TF14 | p.352 | wrapper classification | security/fund/trust/deposit readable; some acronyms broken | SOURCE_AMBIGUITIES SRC-A09 | SOURCE_AMBIGUITY |
| TF15 | p.357–359 | structured prospectus figures | branch prose readable; exact cells partial | SOURCE_AMBIGUITIES SRC-A10 | SOURCE_AMBIGUITY |
| TF16 | p.360–361 | equity-linked deposit examples | KO/digital source rates and logic readable | 07 §2 | VERIFIED-SOURCE-STATE |

## Counts

- Formula rows: **42** (41 source-backed PASS + 1 labeled enrichment).
- Table/figure rows: **16**.
- Table/figure exact-source ambiguities: **9**; every one links to an exact SOURCE_AMBIGUITY record rather than silent reconstruction.
- No formula required by the semantic inventory is left PARTIAL or MISSING.
