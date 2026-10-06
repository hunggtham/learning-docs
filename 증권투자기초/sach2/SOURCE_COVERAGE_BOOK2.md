# SOURCE_COVERAGE_BOOK2 — Sách 2 `증권투자기초`

## Authority và phương pháp

- **Content authority:** [`../raw/sach2.md`](../raw/sach2.md).
- Không tạo `raw_md/sach2.md` giả. Audit này đọc trực tiếp raw OCR hiện có.
- Repo không có thư mục asset/image riêng cho Sách 2; vì vậy nơi OCR không đủ evidence được giữ là `SOURCE_AMBIGUITY`.
- **Learning route:** [`../../investing/90_securities_book2/`](../../investing/90_securities_book2/README.md).
- `FULL` chỉ được dùng khi unit giữ được meaning + relationship/condition/boundary cần thiết; keyword xuất hiện một mình không đủ.
- Một hàng chỉ đại diện cho **một semantic unit có thể fail độc lập**. Product, formula, indicator, pattern, theory và auction mechanism không được gom thành mega-row.
- Source questions được audit riêng trong [`SOURCE_QUESTION_MAP_BOOK2.md`](./SOURCE_QUESTION_MAP_BOOK2.md); câu hỏi không được dùng như semantic row để che nhiều concept.

## Inventory

| ID | Source | Type | Semantic unit | Target | Status | Evidence / boundary |
|---|---|---|---|---|---|---|
| B2-U001 | pp.10–14; raw ~L250–330 | DEFINITION | Khái niệm đầu tư: hy sinh tiêu dùng hiện tại để đổi lấy lợi ích tương lai | 01 §1 | **FULL** |  |
| B2-U002 | pp.10–14; raw ~L250–330 | DISTINCTION | Đầu tư thực (real investment / 실물투자) | 01 §1 | **FULL** |  |
| B2-U003 | pp.10–14; raw ~L250–330 | DISTINCTION | Đầu tư tài chính (financial investment / 금융투자) | 01 §1 | **FULL** |  |
| B2-U004 | pp.14–18 | DEFINITION | Chứng khoán như quyền đòi hỏi tài chính | 01 §1 | **FULL** |  |
| B2-U005 | pp.14–18 | DISTINCTION | Cổ phiếu: residual ownership claim | 01 §1 | **FULL** |  |
| B2-U006 | pp.14–18 | DISTINCTION | Trái phiếu: contractual debt claim | 01 §1 | **FULL** |  |
| B2-U007 | pp.18–22 | RELATIONSHIP | Risk–return khác nhau theo loại claim và thứ tự dòng tiền | 01 §1 | **FULL** |  |
| B2-U008 | pp.18–26; raw ~L350–450 | MECHANISM | Chu kỳ kinh doanh và liên hệ với giá chứng khoán | 01 §2 | **FULL** |  |
| B2-U009 | pp.18–26 | CLASSIFICATION | Kitchin cycle: inventory/short cycle | 01 §2 | **FULL** |  |
| B2-U010 | pp.18–26 | CLASSIFICATION | Juglar cycle: investment/equipment cycle | 01 §2 | **FULL** |  |
| B2-U011 | pp.18–26 | CLASSIFICATION | Kondratiev cycle: long-wave horizon | 01 §2 | **FULL** |  |
| B2-U012 | pp.22–24; raw ~L440–475 | VARIABLE | GDP: output measure và transmission sang doanh nghiệp | 01 §2 | **FULL** |  |
| B2-U013 | pp.24–26; raw ~L475–520 | SOURCE_TEXT | Macro indicator subsection 5.1.3–5.1.4: exact Korean headings/variable labels | 01 §2 | **SOURCE_AMBIGUITY** | OCR body/headings không đủ để xác định chính xác hai indicator; không có asset gốc khác trong repo. |
| B2-U014 | pp.24–28; raw ~L500–610 | TERMINOLOGY | Exchange-rate quotation: European/American term labels in source | 01 §2 | **FULL** |  |
| B2-U015 | pp.24–28; raw ~L500–610 | FORMULA | Reciprocal FX quotation: đảo orientation bằng nghịch đảo | 01 §2 | **FULL** |  |
| B2-U016 | pp.24–28; raw ~L500–610 | FORMULA | Cross-rate construction từ hai cặp có đồng tiền chung | 01 §2 | **FULL** |  |
| B2-U017 | pp.24–28 | BOUNDARY | FX quote boundary: base/quote, bid/ask, spread và thời điểm | 01 §2 | **FULL** |  |
| B2-U018 | pp.26–28; raw ~L600–660 | SOURCE_TEXT | Macro indicator subsection 5.1.6–5.1.8: exact headings/labels | 01 §2 | **SOURCE_AMBIGUITY** | OCR không đủ để phục hồi tên mục/biến một cách source-faithful. |
| B2-U019 | pp.28–32; raw ~L610–660 | FORMULA | CSI formula reconstruction từ positive/negative current/expected responses | 01 §3 | **FULL** |  |
| B2-U020 | pp.28–32 | EXAMPLE | CSI worked example cho kết quả 65 | 01 §3 | **FULL** |  |
| B2-U021 | pp.28–32 | BOUNDARY | CSI là survey balance, không phải tín hiệu mua/bán | 01 §3 | **FULL** |  |
| B2-U022 | pp.28–32; raw ~L640–675 | FORMULA | BSI = (positive − negative)/total ×100 +100 | 01 §3 | **FULL** |  |
| B2-U023 | pp.28–32 | EXAMPLE | BSI worked example 300/200 trên 500 → 120 | 01 §3 | **FULL** |  |
| B2-U024 | pp.28–32 | BOUNDARY | BSI 100 threshold chỉ là survey balance boundary | 01 §3 | **FULL** |  |
| B2-U025 | pp.30–34; raw ~L665–720 | DISTINCTION | Composite Index (CI): mức tổng hợp | 01 §3 | **FULL** |  |
| B2-U026 | pp.30–34; raw ~L665–720 | DISTINCTION | Diffusion Index (DI): breadth/độ lan tỏa | 01 §3 | **FULL** |  |
| B2-U027 | pp.30–34 | EXAMPLE | CI tăng nhưng DI yếu: weighted magnitude vs breadth | 01 §3 | **FULL** |  |
| B2-U028 | pp.30–34 | CLASSIFICATION | Leading indicator: thường đổi trước hoạt động thực | 01 §3 | **FULL** |  |
| B2-U029 | pp.34–46; raw ~L720–940 | PROCESS | Industry analysis: định lượng + định tính trước company analysis | 01 §4 | **FULL** |  |
| B2-U030 | pp.40–44; raw ~L930–1020 | FRAMEWORK | Industry life cycle: introduction | 01 §4 | **FULL** |  |
| B2-U031 | pp.40–44; raw ~L930–1020 | FRAMEWORK | Industry life cycle: growth | 01 §4 | **FULL** |  |
| B2-U032 | pp.40–44; raw ~L930–1020 | FRAMEWORK | Industry life cycle: maturity | 01 §4 | **FULL** |  |
| B2-U033 | pp.40–44; raw ~L930–1020 | FRAMEWORK | Industry life cycle: decline | 01 §4 | **FULL** |  |
| B2-U034 | pp.44–50; raw ~L1000–1080 | PROCESS | Company analysis: nối industry position, cost structure, management và capital allocation | 01 §4 | **FULL** |  |
| B2-U035 | pp.48–52; raw ~L1020–1110 | FRAMEWORK | BCG matrix two axes: market growth × relative market share | 01 §4 | **FULL** |  |
| B2-U036 | pp.48–52 | CLASSIFICATION | BCG Question Mark | 01 §4 | **FULL** |  |
| B2-U037 | pp.48–52 | CLASSIFICATION | BCG Star | 01 §4 | **FULL** |  |
| B2-U038 | pp.48–52 | CLASSIFICATION | BCG Cash Cow | 01 §4 | **FULL** |  |
| B2-U039 | pp.48–52 | CLASSIFICATION | BCG Barking Dog | 01 §4 | **FULL** |  |
| B2-U040 | pp.48–52 | BOUNDARY | BCG label không thay profitability/ROIC/valuation analysis | 01 §4 | **FULL** |  |
| B2-U041 | pp.52–58; raw ~L1080–1200 | INSTITUTION | IFRS: framework/standards for recognition, measurement and presentation | 01 §4 | **FULL** |  |
| B2-U042 | pp.54–66; raw ~L1100–1370 | CLASSIFICATION | Balance sheet: resources and obligations at a point in time | 01 §4 | **FULL** |  |
| B2-U043 | pp.54–66 | CLASSIFICATION | Income statement: revenue, costs and profit over a period | 01 §4 | **FULL** |  |
| B2-U044 | pp.54–66 | CLASSIFICATION | Cash-flow statement: profit-to-cash reconciliation | 01 §4 | **FULL** |  |
| B2-U045 | pp.54–66 | PROCESS | Read statements together with notes and accounting boundaries | 01 §4 | **FULL** |  |
| B2-U046 | pp.68–71; raw ~L1370–1510 | FORMULA | Financial-ratio block before ROI/ROE: exact OCR labels/numerators for several ratios | 01 §5 | **SOURCE_AMBIGUITY** | Ratio-family purpose is teachable; exact source formula labels are too corrupted to restore safely. |
| B2-U047 | pp.68–72 | CLASSIFICATION | Liquidity-ratio family: short-term resources vs obligations | 01 §5 | **FULL** |  |
| B2-U048 | pp.68–72 | CLASSIFICATION | Leverage/solvency-ratio family: debt burden vs capital/capacity | 01 §5 | **FULL** |  |
| B2-U049 | pp.68–72 | CLASSIFICATION | Activity/turnover-ratio family: capital tied up vs operating flow | 01 §5 | **FULL** |  |
| B2-U050 | pp.68–72 | CLASSIFICATION | Profitability-ratio family: profit relative to sales/assets/equity | 01 §5 | **FULL** |  |
| B2-U051 | pp.71–74; raw ~L1490–1540 | FORMULA | ROI formula and interpretation | 01 §5 | **FULL** |  |
| B2-U052 | pp.71–74; raw ~L1510–1550 | FORMULA | ROE formula and interpretation | 01 §5 | **FULL** |  |
| B2-U053 | pp.71–76 | RELATIONSHIP | DuPont-style ROE decomposition: margin × asset turnover × equity multiplier | 01 §5 | **FULL** |  |
| B2-U054 | pp.71–76 | BOUNDARY | High ROE can be leverage-driven rather than operating-quality-driven | 01 §5 | **FULL** |  |
| B2-U055 | pp.78–82; raw ~L1600–1680 | FORMULA | Compound value FV = PV(1+r)^n | 02 §1 | **FULL** |  |
| B2-U056 | pp.78–82 | FORMULA | Present value PV = FV/(1+r)^n | 02 §1 | **FULL** |  |
| B2-U057 | pp.78–82 | EXAMPLE | 10% compound-return example | 02 §1 | **FULL** |  |
| B2-U058 | pp.80–84; raw ~L1650–1730 | FORMULA | CAPM expected/required return equation | 02 §1 | **FULL** |  |
| B2-U059 | pp.80–84 | VARIABLE | CAPM risk-free rate Rf | 02 §1 | **FULL** |  |
| B2-U060 | pp.80–84 | VARIABLE | CAPM beta β as systematic sensitivity | 02 §1 | **FULL** |  |
| B2-U061 | pp.80–84 | VARIABLE | CAPM market risk premium E(Rm)-Rf | 02 §1 | **FULL** |  |
| B2-U062 | pp.80–84 | BOUNDARY | CAPM does not capture all idiosyncratic/liquidity/model risk | 02 §1 | **FULL** |  |
| B2-U063 | pp.84–88; raw ~L1760–1810 | FORMULA | NPV: discounted inflows minus initial investment | 02 §2 | **FULL** |  |
| B2-U064 | pp.84–88 | DECISION_RULE | NPV > 0 under the stated hurdle-rate assumptions | 02 §2 | **FULL** |  |
| B2-U065 | pp.84–88 | BOUNDARY | NPV sign changes when cash flow, horizon or discount rate changes | 02 §2 | **FULL** |  |
| B2-U066 | pp.84–88 | CONCEPT | PVGO: value of growth opportunities vs assets in place | 02 §2 | **FULL** |  |
| B2-U067 | pp.84–88 | FORMULA | Dividend Discount Model as PV of dividends + terminal value | 02 §2 | **FULL** |  |
| B2-U068 | pp.84–88 | FORMULA | Gordon model P0 = D1/(k−g) | 02 §2 | **FULL** |  |
| B2-U069 | pp.84–88 | BOUNDARY | Gordon condition k > g and sensitivity as k approaches g | 02 §2 | **FULL** |  |
| B2-U070 | pp.84–88 | EXAMPLE | Gordon worked example and growth-sensitivity check | 02 §2 | **FULL** |  |
| B2-U071 | pp.86–90; raw ~L1800–1840 | DEFINITION | FCFE: cash flow available to equity | 02 §3 | **FULL** |  |
| B2-U072 | pp.86–90 | DEFINITION | FCFF: cash flow available to all capital providers | 02 §3 | **FULL** |  |
| B2-U073 | pp.86–90; raw ~L1810–1822 | RELATIONSHIP | FCFF–FCFE bridge with after-tax interest and net debt flow; sign convention made explicit | 02 §3 | **FULL** | Route defines net debt repayment = repayment − new borrowing to avoid sign ambiguity. |
| B2-U074 | pp.86–90; raw ~L1820–1850 | FORMULA | WACC = E/(D+E)·Re + D/(D+E)·Rd·(1−T), with capital-weight/tax-shield assumptions | 02 §3 | **FULL** | Source formula structure is readable; route defines variables explicitly. |
| B2-U075 | pp.86–90 | BOUNDARY | FCFE ↔ cost of equity; FCFF ↔ WACC matching rule | 02 §3 | **FULL** |  |
| B2-U076 | pp.88–90; raw ~L1825–1860 | FORMULA | EVA = NOPAT − Invested Capital×WACC | 02 §4 | **FULL** |  |
| B2-U077 | pp.88–90 | FORMULA | EVA = Invested Capital×(ROIC−WACC) | 02 §4 | **FULL** |  |
| B2-U078 | pp.88–90 | BOUNDARY | Growth creates value only when incremental return clears cost of capital | 02 §4 | **FULL** |  |
| B2-U079 | pp.90–94; raw ~L1860–1920 | FORMULA | PER = price/EPS | 02 §5 | **FULL** |  |
| B2-U080 | pp.90–94 | BOUNDARY | PER unreliable for negative/cyclical/one-off earnings | 02 §5 | **FULL** |  |
| B2-U081 | pp.94–98; raw ~L1920–2020 | FORMULA | PBR = price/BPS | 02 §6 | **FULL** |  |
| B2-U082 | pp.94–98 | RELATIONSHIP | PBR–ROE relation | 02 §6 | **FULL** |  |
| B2-U083 | pp.94–98 | BOUNDARY | Low PBR does not imply cheap if ROE/assets are poor | 02 §6 | **FULL** |  |
| B2-U084 | pp.98–102; raw ~L2020–2110 | FORMULA | PSR = price/SPS | 02 §7 | **FULL** |  |
| B2-U085 | pp.98–102 | RELATIONSHIP | PSR must be read with profit margin | 02 §7 | **FULL** |  |
| B2-U086 | pp.98–102 | BOUNDARY | Sales growth without margin/cash conversion can destroy value | 02 §7 | **FULL** |  |
| B2-U087 | pp.102–104; raw ~L2110–2190 | DEFINITION | Enterprise Value numerator scope | 02 §8 | **FULL** |  |
| B2-U088 | pp.102–104 | DEFINITION | EBITDA denominator scope | 02 §8 | **FULL** |  |
| B2-U089 | pp.102–104 | FORMULA | EV/EBITDA multiple | 02 §8 | **FULL** |  |
| B2-U090 | pp.102–104 | BOUNDARY | EV/EBITDA ignores capex/working-capital intensity and is not FCF | 02 §8 | **FULL** |  |
| B2-U091 | pp.106–110; raw ~L2200–2300 | CONCEPT | Technical analysis uses market price/volume data | 03 §1 | **FULL** |  |
| B2-U092 | pp.106–110 | MECHANISM | Trend: higher highs/lows vs lower highs/lows | 03 §1 | **FULL** |  |
| B2-U093 | pp.106–110 | CONCEPT | Support as reaction zone | 03 §1 | **FULL** |  |
| B2-U094 | pp.106–110 | CONCEPT | Resistance as reaction zone | 03 §1 | **FULL** |  |
| B2-U095 | pp.106–110 | BOUNDARY | Support/resistance are zones, not immutable lines | 03 §1 | **FULL** |  |
| B2-U096 | pp.110–126; raw ~L2250–2500 | FORMULA | SMA formula | 03 §2 | **FULL** |  |
| B2-U097 | pp.110–126 | FORMULA | EMA recursive weighting formula | 03 §2 | **FULL** |  |
| B2-U098 | pp.110–126 | PROCESS | Short/long moving-average crossover | 03 §2 | **FULL** |  |
| B2-U099 | pp.110–126 | BOUNDARY | Moving-average lag and whipsaw in range regimes | 03 §2 | **FULL** |  |
| B2-U100 | pp.126–144; raw ~L2500–2740 | PATTERN | Head-and-shoulders: neckline confirmation | 03 §3 | **FULL** |  |
| B2-U101 | pp.126–144; raw ~L2500–2740 | PATTERN | Double top: break below intervening support | 03 §3 | **FULL** |  |
| B2-U102 | pp.126–144; raw ~L2500–2740 | PATTERN | Double bottom: break above intervening resistance | 03 §3 | **FULL** |  |
| B2-U103 | pp.126–144; raw ~L2500–2740 | PATTERN | Triple top: three failed tests near a top plus downside confirmation | 03 §3 | **FULL** |  |
| B2-U104 | pp.126–144; raw ~L2500–2740 | PATTERN | Round top: gradual weakening of demand before downside confirmation | 03 §3 | **FULL** |  |
| B2-U105 | pp.126–144; raw ~L2500–2740 | PATTERN | Gap: context-dependent gap classification | 03 §3 | **FULL** |  |
| B2-U106 | pp.126–144; raw ~L2500–2740 | PATTERN | Flag: short consolidation after impulse | 03 §3 | **FULL** |  |
| B2-U107 | pp.126–144; raw ~L2500–2740 | PATTERN | Pennant: contracting consolidation after impulse | 03 §3 | **FULL** |  |
| B2-U108 | pp.126–144; raw ~L2500–2740 | PATTERN | Wedge: converging boundaries | 03 §3 | **FULL** |  |
| B2-U109 | pp.126–144; raw ~L2500–2740 | PATTERN | Rectangle: horizontal range plus breakout | 03 §3 | **FULL** |  |
| B2-U110 | pp.126–144; raw ~L2500–2740 | PATTERN | Diamond pattern: expansion then contraction; target geometry OCR-limited | 03 §3 | **FULL** |  |
| B2-U111 | pp.126–144 | FIGURE | Diamond exact figure coordinates/price target from source image text | 03 §3 | **SOURCE_AMBIGUITY** | OCR retains pattern name but not enough geometry to reproduce a numeric target. |
| B2-U112 | pp.142–154; raw ~L2740–2970 | FIGURE | Candlestick body/shadow/open-high-low-close reading | 03 §4 | **FULL** |  |
| B2-U113 | pp.142–154 | PATTERN | Candlestick pattern: Doji | 03 §4 | **FULL** |  |
| B2-U114 | pp.142–154 | PATTERN | Candlestick pattern: Hammer | 03 §4 | **FULL** |  |
| B2-U115 | pp.142–154 | PATTERN | Candlestick pattern: Shooting star | 03 §4 | **FULL** |  |
| B2-U116 | pp.142–154 | PATTERN | Candlestick pattern: Engulfing | 03 §4 | **FULL** |  |
| B2-U117 | pp.142–154 | PATTERN | Candlestick pattern: Harami | 03 §4 | **FULL** |  |
| B2-U118 | pp.142–154 | PATTERN | Candlestick pattern: Morning star | 03 §4 | **FULL** |  |
| B2-U119 | pp.142–154 | PATTERN | Candlestick pattern: Evening star | 03 §4 | **FULL** |  |
| B2-U120 | pp.142–154 | BOUNDARY | Candlestick requires trend location/confirmation/volume context | 03 §4 | **FULL** |  |
| B2-U121 | pp.154–168; raw ~L2970–3285 | FORMULA | MACD = fast EMA − slow EMA; signal-line relation | 03 §5 | **FULL** |  |
| B2-U122 | pp.154–168 | BOUNDARY | MACD crossover lag/noise boundary | 03 §5 | **FULL** |  |
| B2-U123 | pp.154–168 | FORMULA | RSI normalization from average gain/loss | 03 §5 | **FULL** |  |
| B2-U124 | pp.154–168 | BOUNDARY | RSI overbought/oversold is not automatic reversal | 03 §5 | **FULL** |  |
| B2-U125 | pp.154–168 | FORMULA | Stochastic: close relative to recent high-low range | 03 §5 | **FULL** |  |
| B2-U126 | pp.154–168 | BOUNDARY | Stochastic textbook thresholds are parameter/context dependent | 03 §5 | **FULL** |  |
| B2-U127 | pp.154–168 | FORMULA | Bollinger Bands = moving average ± k·standard deviation | 03 §5 | **FULL** |  |
| B2-U128 | pp.154–168 | BOUNDARY | Band width signals volatility, not direction | 03 §5 | **FULL** |  |
| B2-U129 | pp.154–168 | FORMULA | Envelope as percentage bands around moving average | 03 §5 | **FULL** |  |
| B2-U130 | pp.154–168 | BOUNDARY | Envelope width depends on selected percentage/regime | 03 §5 | **FULL** |  |
| B2-U131 | pp.154–168 | FORMULA | OBV cumulative volume signed by price direction | 03 §5 | **FULL** |  |
| B2-U132 | pp.154–168 | BOUNDARY | OBV divergence depends on volume data quality | 03 §5 | **FULL** |  |
| B2-U133 | pp.154–168 | FORMULA | VR volume-ratio formula with up/down/unchanged volume | 03 §5 | **FULL** |  |
| B2-U134 | pp.154–168 | BOUNDARY | VR thresholds are textbook conventions, not universal triggers | 03 §5 | **FULL** |  |
| B2-U135 | pp.154–168 | PROCESS | Point-and-Figure box/reversal filtering | 03 §5 | **FULL** |  |
| B2-U136 | pp.154–168 | BOUNDARY | P&F output changes with box size and reversal rule | 03 §5 | **FULL** |  |
| B2-U137 | pp.170–180; raw ~L3285–3500 | THEORY | Dow Theory: trend hierarchy and confirmation logic | 03 §6 | **FULL** |  |
| B2-U138 | pp.170–180 | THEORY | Elliott Wave: impulse/corrective wave framework | 03 §6 | **FULL** |  |
| B2-U139 | pp.170–180 | RELATIONSHIP | Fibonacci ratios as Elliott measurement convention | 03 §6 | **FULL** |  |
| B2-U140 | pp.170–180 | BOUNDARY | Pattern/wave labeling is interpretive and non-causal | 03 §6 | **FULL** |  |
| B2-U141 | pp.182–186; raw ~L3500–3600 | STRATEGY | Buy-and-hold | 04 §1 | **FULL** |  |
| B2-U142 | pp.182–186 | STRATEGY | Dollar-cost averaging / periodic fixed-amount investing | 04 §1 | **FULL** |  |
| B2-U143 | pp.182–186 | EXAMPLE | DCA worked price-path example | 04 §1 | **FULL** |  |
| B2-U144 | pp.182–186 | CORPORATE_ACTION | Cash dividend and total-return treatment | 04 §1 | **FULL** |  |
| B2-U145 | pp.182–186 | CORPORATE_ACTION | Stock split and adjusted-price treatment | 04 §1 | **FULL** |  |
| B2-U146 | pp.184–186 | EFFECT | Small-firm effect as empirical effect, not guarantee | 04 §2 | **FULL** |  |
| B2-U147 | pp.184–186 | STRATEGY | Formula plan / rule-based rebalancing | 04 §2 | **FULL** |  |
| B2-U148 | pp.184–186 | EXAMPLE | Formula-plan 50/50 rebalancing example | 04 §2 | **FULL** |  |
| B2-U149 | pp.186–188; raw ~L3590–3630 | FORMULA | Two-asset portfolio variance with covariance/correlation | 04 §3 | **FULL** |  |
| B2-U150 | pp.186–188 | MECHANISM | Diversification from correlation < 1 | 04 §3 | **FULL** |  |
| B2-U151 | pp.186–188 | BOUNDARY | Correlation can rise during stress; many names ≠ diversified exposures | 04 §3 | **FULL** |  |
| B2-U152 | pp.188–198; raw ~L3620–3830 | INDEX | Stock-price index purpose and base normalization | 04 §4 | **FULL** |  |
| B2-U153 | pp.188–198 | INDEX | Price-weighted index mechanics | 04 §4 | **FULL** |  |
| B2-U154 | pp.188–198 | INDEX | Market-cap-weighted index mechanics | 04 §4 | **FULL** |  |
| B2-U155 | pp.188–198 | INDEX | Equal-weighted index mechanics | 04 §4 | **FULL** |  |
| B2-U156 | pp.188–198 | CORPORATE_ACTION | Index divisor adjustment for stock split/corporate action | 04 §4 | **FULL** |  |
| B2-U157 | pp.188–198 | DISTINCTION | Price-return vs total-return index | 04 §4 | **FULL** |  |
| B2-U158 | pp.188–198 | INSTITUTION | KOSPI as a textbook/source index example | 04 §4 | **FULL** | Current constituents/methodology are not asserted. |
| B2-U159 | pp.188–198 | INSTITUTION | S&P 500 as a textbook/source index example | 04 §4 | **FULL** | Current constituents/methodology are not asserted. |
| B2-U165 | pp.217–224; raw ~L4290–4450 | DEFINITION | Bond/fixed-income claim, face value, maturity, coupon | 05 §1 | **FULL** |  |
| B2-U166 | pp.217–224 | CLASSIFICATION | Zero-coupon/discount bond | 05 §1 | **FULL** |  |
| B2-U167 | pp.217–224 | CLASSIFICATION | Coupon bond | 05 §1 | **FULL** |  |
| B2-U168 | pp.217–224 | CLASSIFICATION | Perpetuity conceptual boundary | 05 §1 | **FULL** |  |
| B2-U169 | pp.224–232; raw ~L4450–4600 | FORMULA | Bond price = PV(coupons)+PV(face value) | 05 §1 | **FULL** |  |
| B2-U170 | pp.224–232 | MECHANISM | Bond price moves inversely with required yield | 05 §1 | **FULL** |  |
| B2-U171 | pp.224–232 | RELATIONSHIP | Coupon rate vs market yield determines premium/par/discount | 05 §1 | **FULL** |  |
| B2-U172 | pp.224–232 | EXAMPLE | Two-year coupon-bond price worked example | 05 §6 | **FULL** |  |
| B2-U173 | pp.232–250; raw ~L4600–5000 | PRODUCT | Convertible bond / 전환사채: bond + conversion option; conversion ratio/period | 05 §2–3 | **FULL** |  |
| B2-U174 | pp.232–250; raw ~L4600–5000 | PRODUCT | Bond with warrant / 신주인수권부사채: bond + stock-purchase warrant; not the same as CB | 05 §2–3 | **FULL** |  |
| B2-U175 | pp.232–250; raw ~L4600–5000 | PRODUCT | Exchangeable bond / 교환사채: exchange into specified securities; exchange asset/ratio | 05 §2–3 | **FULL** |  |
| B2-U176 | pp.232–250; raw ~L4600–5000 | PRODUCT | ABS / 자산유동화증권: securitized pool cash flows + waterfall/servicing | 05 §2–3 | **FULL** |  |
| B2-U177 | pp.232–250; raw ~L4600–5000 | PRODUCT | MBS / 주택저당증권: mortgage pool + prepayment/extension risk | 05 §2–3 | **FULL** |  |
| B2-U178 | pp.232–250; raw ~L4600–5000 | PRODUCT | CMO: mortgage cash flows divided into tranches | 05 §2–3 | **FULL** |  |
| B2-U179 | pp.232–250; raw ~L4600–5000 | PRODUCT | Floating-rate bond / 변동금리채: benchmark ± spread with reset/floor/cap | 05 §2–3 | **FULL** |  |
| B2-U180 | pp.232–250; raw ~L4600–5000 | PRODUCT | Reverse floater / 역변동금리채: coupon moves opposite benchmark; leverage/cap/floor | 05 §2–3 | **FULL** |  |
| B2-U181 | pp.232–250; raw ~L4600–5000 | PRODUCT | Preferred stock / 우선주: priority vs common equity with term-dependent rights | 05 §2–3 | **FULL** |  |
| B2-U182 | pp.232–250; raw ~L4600–5000 | PRODUCT | Catastrophe bond: catastrophe trigger can impair coupon/principal | 05 §2–3 | **FULL** |  |
| B2-U183 | pp.232–250; raw ~L4600–5000 | PRODUCT | Indexed bond / 지수연동채권: coupon/principal linked to an index | 05 §2–3 | **FULL** |  |
| B2-U184 | pp.232–250; raw ~L4600–5000 | PRODUCT | International bond / 국제채: cross-border issuance with currency/jurisdiction risk | 05 §2–3 | **FULL** |  |
| B2-U185 | pp.232–250; raw ~L4600–5000 | PRODUCT | Foreign bond / 외국채: foreign issuer in a domestic market | 05 §2–3 | **FULL** |  |
| B2-U186 | pp.232–250; raw ~L4600–5000 | PRODUCT | Eurobond / 유로채: issued outside domestic market of denomination currency | 05 §2–3 | **FULL** |  |
| B2-U187 | pp.232–250; raw ~L4600–5000 | PRODUCT | Structured note / 구조화채권: debt claim plus derivative-linked payoff | 05 §2–3 | **FULL** |  |
| B2-U188 | pp.247–248; raw ~L4890–4910 | PRODUCT | Separate source heading 'Asset-Backed Bond' vs adjacent ABS distinction | 05 §3 | **SOURCE_AMBIGUITY** | Heading exists separately but OCR body does not support a reliable independent definition. |
| B2-U189 | pp.242–250 | PRODUCT | Structured note: interest-rate-linked subtype | 05 §3 | **FULL** |  |
| B2-U190 | pp.242–250 | PRODUCT | Structured note: credit/default/spread-linked subtype | 05 §3 | **FULL** |  |
| B2-U191 | pp.242–250 | PRODUCT | Structured note: equity/equity-index-linked subtype | 05 §3 | **FULL** |  |
| B2-U192 | pp.242–250 | PRODUCT | Structured note: currency/dual-currency subtype | 05 §3 | **FULL** |  |
| B2-U193 | pp.242–250 | PRODUCT | Structured note: commodity-linked subtype | 05 §3 | **FULL** |  |
| B2-U194 | pp.242–250 | BOUNDARY | Structured-note coupon does not imply principal protection | 05 §3 | **FULL** |  |
| B2-U195 | pp.242–250 | EXAMPLE | Indexed-bond principal/coupon adjustment worked table | 05 §6 | **FULL** |  |
| B2-U196 | pp.232–250 | RISK | Embedded option changes cash-flow timing and duration | 05 §7 | **FULL** |  |
| B2-U197 | pp.232–250 | RISK | Seniority/recovery/expected-loss reasoning | 05 §8 | **FULL** |  |
| B2-U198 | pp.250–258; raw ~L5000–5570 | DEFINITION | Discount rate as PV conversion rate | 06 §1 | **FULL** |  |
| B2-U199 | pp.250–258 | FORMULA | IRR as rate making NPV=0 | 06 §1 | **FULL** |  |
| B2-U200 | pp.250–258 | FORMULA | YTM as bond IRR to maturity | 06 §1 | **FULL** |  |
| B2-U201 | pp.250–258 | DISTINCTION | Coupon rate, current yield and YTM answer different return questions | 06 §1 | **FULL** | Individual coupon-rate/current-yield units are tracked separately. |
| B2-U202 | pp.250–258 | BOUNDARY | YTM assumptions: hold-to-maturity, reinvestment, no default | 06 §1 | **FULL** |  |
| B2-U203 | pp.250–258 | EXAMPLE | YTM worked equation for price 964.33 | 06 §1 | **FULL** |  |
| B2-U204 | pp.258–282; raw ~L5575–5950 | CONCEPT | Yield curve / term structure by maturity | 06 §2 | **FULL** |  |
| B2-U205 | pp.258–282 | FORMULA | Spot-rate compounding relation | 06 §2 | **FULL** |  |
| B2-U206 | pp.258–282 | FORMULA | Forward-rate relation from spot rates | 06 §2 | **FULL** |  |
| B2-U207 | pp.258–282 | EXAMPLE | Forward-rate worked example from 1y/2y spot rates | 06 §2 | **FULL** |  |
| B2-U208 | pp.258–282 | THEORY | Expectations Theory / 기대이론 | 06 §2 | **FULL** |  |
| B2-U209 | pp.258–282 | THEORY | Liquidity Premium Theory / 유동성프리미엄이론 | 06 §2 | **FULL** |  |
| B2-U210 | pp.258–282 | THEORY | Market Segmentation Theory / 시장분할이론 | 06 §2 | **FULL** |  |
| B2-U211 | pp.258–282 | THEORY | Preferred Habitat Theory | 06 §2 | **FULL** |  |
| B2-U212 | pp.258–282 | BOUNDARY | Yield-curve shape combines expected rates and term/liquidity premia | 06 §2 | **FULL** |  |
| B2-U213 | pp.274–306; raw ~L5950–6110 | RISK | Default risk | 06 §3 | **FULL** |  |
| B2-U214 | pp.274–306 | INSTITUTION | Credit-rating scale and agency-specific notation | 06 §3 | **FULL** |  |
| B2-U215 | pp.274–306 | DISTINCTION | Investment-grade vs speculative/high-yield boundary | 06 §3 | **FULL** |  |
| B2-U216 | pp.274–306 | RISK | Credit spread includes default, liquidity, tax and risk premia | 06 §3 | **FULL** |  |
| B2-U217 | pp.274–306 | BOUNDARY | Credit rating is relative assessment, not insurance | 06 §3 | **FULL** |  |
| B2-U218 | pp.306–318; raw ~L6100–6310 | FORMULA | Macaulay duration as PV-weighted cash-flow time | 06 §4 | **FULL** |  |
| B2-U219 | pp.306–318 | FORMULA | Modified duration = Macaulay duration/(1+y) for annual convention | 06 §4 | **FULL** |  |
| B2-U220 | pp.306–318 | FORMULA | First-order price sensitivity ΔP/P≈−Dmod·Δy | 06 §4 | **FULL** |  |
| B2-U221 | pp.306–318 | FORMULA | Convexity second-order correction | 06 §4 | **FULL** |  |
| B2-U222 | pp.306–318 | EXAMPLE | Macaulay/modified duration worked example | 06 §4 | **FULL** |  |
| B2-U223 | pp.306–318 | BOUNDARY | Duration approximation is local and assumes yield movement convention | 06 §4 | **FULL** |  |
| B2-U224 | pp.306–318 | BOUNDARY | Callable/MBS cash flows can create changing duration/negative convexity | 06 §4 | **FULL** |  |
| B2-U225 | pp.318–340; raw ~L6310–6700 | STRATEGY | Bond total return decomposed into carry, price/curve, spread and FX | 06 §8 | **FULL** |  |
| B2-U226 | pp.318–340 | INDEX | Bond price index | 06 §5 | **FULL** |  |
| B2-U227 | pp.318–340 | INDEX | Coupon/income component in bond performance index | 06 §5 | **FULL** |  |
| B2-U228 | pp.318–340 | INDEX | Yield-related bond index/measure in source taxonomy | 06 §5 | **FULL** |  |
| B2-U229 | pp.318–340 | INDEX | Bond total-return index | 06 §5 | **FULL** |  |
| B2-U230 | pp.318–340 | BOUNDARY | Bond-index comparison requires same pricing time, universe, currency and reinvestment rule | 06 §5 | **FULL** |  |
| B2-U231 | pp.318–340 | METRIC | Tracking error between portfolio and benchmark | 06 §5 | **FULL** |  |
| B2-U232 | pp.340–366; raw ~L6700–7110 | MARKET | Primary bond market / 발행시장 | 06 §5 | **FULL** |  |
| B2-U233 | pp.340–366 | MARKET | Secondary bond market / 유통시장 | 06 §5 | **FULL** |  |
| B2-U234 | pp.340–366 | AUCTION | Conventional/multiple-price auction | 06 §5 | **FULL** |  |
| B2-U235 | pp.340–366 | AUCTION | Dutch/single-price auction | 06 §5 | **FULL** |  |
| B2-U236 | pp.340–366 | BOUNDARY | Auction mechanism changes bidding incentives; not one generic auction | 06 §5 | **FULL** |  |
| B2-U237 | pp.340–366; raw ~L6960 | MARKET | Repo / 환매조건부매매 as collateralized funding mechanism | 06 §6 | **FULL** |  |
| B2-U238 | pp.340–366 | RISK | Repo haircut as collateral buffer, not elimination of counterparty/market risk | 06 §6 | **FULL** |  |
| B2-U239 | pp.340–366 | EXAMPLE | Worked repo haircut/funding example | 06 §6 | **FULL** |  |
| B2-U240 | pp.340–366; raw ~L7060 | INDEX | KSDA-BLP Korean Bond Index as textbook-state source example | 06 §5 | **FULL** |  |
| B2-U241 | pp.340–366 | BOUNDARY | Institution/index names are textbook-state, not current-state claims | 06 §5 | **FULL** |  |

| B2-U249 | pp.30–34 | CLASSIFICATION | Coincident indicator: vận động gần cùng thời điểm với hoạt động thực | 01 §3 | **FULL** |  |
| B2-U250 | pp.30–34 | CLASSIFICATION | Lagging indicator: phản ứng sau khi chu kỳ đã đổi | 01 §3 | **FULL** |  |
| B2-U251 | pp.52–58; raw ~L1080–1200 | INSTITUTION | IASC as historical standard-setting body named by the source | 01 §4 | **FULL** | Textbook-state institutional context only. |
| B2-U252 | pp.52–58; raw ~L1080–1200 | INSTITUTION | IAS as standards named alongside IFRS in the source | 01 §4 | **FULL** | Textbook-state standards context only. |
| B2-U253 | pp.52–58; raw ~L1080–1200 | INSTITUTION | K-IFRS as Korean IFRS-based reporting framework named by the source | 01 §4 | **FULL** | Current regulatory details are outside the source claim. |
| B2-U254 | pp.126–144; raw ~L2500–2740 | PATTERN | Triple bottom: three supported tests near a bottom plus upside confirmation | 03 §3 | **FULL** |  |
| B2-U255 | pp.126–144; raw ~L2500–2740 | PATTERN | Round bottom: gradual recovery of demand before upside confirmation | 03 §3 | **FULL** |  |
| B2-U256 | pp.188–198 | INSTITUTION | KOSPI200 as a textbook/source index example | 04 §4 | **FULL** | Current constituents/methodology are not asserted. |
| B2-U257 | pp.188–198 | INSTITUTION | KOSDAQ as a textbook/source index example | 04 §4 | **FULL** | Current constituents/methodology are not asserted. |
| B2-U258 | pp.188–198 | INSTITUTION | Nikkei 225 as a textbook/source index example | 04 §4 | **FULL** | Current constituents/methodology are not asserted. |
| B2-U259 | pp.232–250; raw ~L4838–4852 | PRODUCT | Callable bond: issuer call right; call schedule, reinvestment risk and negative convexity | 05 §2–3 | **FULL** | Source explicitly labels Callable Bond. |
| B2-U260 | pp.232–250; raw ~L4838–4852 | PRODUCT | Puttable bond: holder put right; put date/price and exercise condition | 05 §2–3 | **FULL** | Source explicitly labels Puttable Bond. |
| B2-U261 | pp.250–258 | FORMULA | Coupon rate = annual coupon / face value | 06 §1 | **FULL** |  |
| B2-U262 | pp.250–258 | FORMULA | Current yield = annual coupon / current market price | 06 §1 | **FULL** | Excludes capital gain/loss to maturity. |

## Coverage result

- Total semantic units: **250**
- `FULL`: **245**
- `PARTIAL`: **0**
- `MISSING`: **0**
- `SOURCE_AMBIGUITY`: **5**

### Ambiguity policy

`SOURCE_AMBIGUITY` không được đổi thành `FULL` chỉ để đạt KPI. Semantic inventory còn các ambiguity về source text/figure/product distinction; ambiguity riêng của hai review-question sets được theo dõi trong [`SOURCE_AMBIGUITIES_BOOK2.md`](./SOURCE_AMBIGUITIES_BOOK2.md) và không bị tính giả thành knowledge unit. Khi có scan/image gốc tốt hơn, re-open đúng artifact thay vì rewrite toàn route.

### Reverse-audit rule

Output không được làm người đọc hiểu rằng textbook-state là current market state. Các tên index, agency, benchmark, auction convention và institutional examples được giữ như **source examples**; nội dung hiện hành phải đi sang canonical owner trong `investing/` và được kiểm tra bằng nguồn đúng thời điểm.
