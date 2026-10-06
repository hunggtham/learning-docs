# Source coverage — Sách 3

Artifact này nối semantic inventory của `sach3/raw_md/sach3.md` với learning route. ID ổn định theo khối nguồn, không coi một heading là một đơn vị duy nhất. Các trang luyện tập và đáp án được dùng cho source-question test; không chép cơ học toàn bộ câu hỏi vào lesson.

Source snapshot: PDF `sach3_ocr.pdf`, 381 pages, rendered at 170 dpi and OCR'd with Tesseract `kor+eng` on 2026-10-04. The generated raw Markdown is provenance only; the earlier `sach3_legacy.md` OCR is not used for semantic interpretation.

| Source ID | Source location | Semantic unit | Type | Target lesson/section | Status | Notes/action |
|---|---|---|---|---|---|---|
| B3-C1-S1-U001 | pp. 12–16 | population, sample, random variable, distribution, arithmetic mean, expected value, discrete/continuous variable | DEFINITION, DISTINCTION | 01 §1 | FULL | Giữ công thức và ví dụ xác suất; thêm worked check về harmonic mean |
| B3-C1-S1-U002 | pp. 16–20 | deviation, variance, standard deviation, sample vs population, return example | FORMULA, EXAMPLE, CONDITION | 01 §2 | FULL | Nêu mẫu số n và n−1; phân biệt standard deviation với downside deviation |
| B3-C1-S1-U003 | pp. 21–26 | scatterplot, correlation, covariance and relation | RELATIONSHIP, TABLE | 01 §3 | FULL | Có giới hạn correlation ≠ causation |
| B3-C1-S1-U004 | pp. 26–31 | linear transform, normalization, combined variance, regression, least squares | MECHANISM, FORMULA | 01 §4 | FULL | Có worked linear-transform exposure; giải thích residual và slope |
| B3-C1-S1-U005 | pp. 33–41 | true/false, exercises, answers and references | EXERCISE | 01 §5 | FULL | Chuyển thành source-question test |
| B3-C1-S2-U001 | pp. 42–51 | Markowitz meaning/assumptions, expected return vs utility, risk attitudes | CONCEPT, ASSUMPTION, DISTINCTION | 02 §1 | FULL | Giữ homogeneous expectations và utility curves; có case ba phương án cùng mean khác phân phối và expected-utility comparison |
| B3-C1-S2-U002 | pp. 52–57 | individual return/risk, two-asset and multi-asset portfolio | FORMULA, MECHANISM | 02 §2 | FULL | Covariance term được reconstruct; có worked check cho MVP và covariance |
| B3-C1-S2-U003 | pp. 57–79 | diversification, systematic/unsystematic risk, efficient frontier, CAL | RELATIONSHIP, CONDITION, EXERCISE | 02 §3 | FULL | Có worked systematic-risk floor; nêu giới hạn phân tán và constraint/no-short boundary |
| B3-C1-S3-U001 | pp. 80–104 | CAPM assumptions, CML, market portfolio, beta, SML, pricing adjustment | MODEL, FORMULA, MECHANISM | 03 §1 | FULL | Phân biệt CML/SML; có worked CML expected-return/covariance check; nối intrinsic value với market price |
| B3-C1-S4-U001 | pp. 105–134 | weak/semi-strong/strong EMH, tests, anomalies, post-EMH discussion | CLASSIFICATION, LEGAL/market rule, EXCEPTION | 03 §2 | FULL | Tách textbook claim và boundary; có worked expectation-surprise và winner/loser reversal source-state cases; thêm survivorship, look-ahead và multiple-testing bias |
| B3-C1-S5-U001 | pp. 135–148 | money/time-weighted return, arithmetic/geometric mean, Sharpe, Treynor, Jensen | FORMULA, COMPARISON | 04 §1 | FULL | Có ví dụ 2 kỳ và worked comparison của ba chỉ số |
| B3-C1-S6-U001 | pp. 149–200 | valuation process, cash flow, cost of capital, DCF, EVA, multiples, exercises | MECHANISM, FORMULA, EXERCISE | 04 §2 | FULL | Cross-link canonical company-analysis owners; EV-to-equity bridge, EVA value-creation case, normalized-EPS/multiple case và terminal-value stress case |
| B3-C2-S1-U001 | pp. 202–226 | why derivatives, hedge/speculation/arbitrage, exchange vs OTC, futures/options/swaps, leverage and margin | CONCEPT, DISTINCTION, WARNING | 05 §1 | FULL | Zero-sum, long/short, mark-to-market, margin call; covered call/short strangle; danh nghĩa ≠ vốn ký quỹ |
| B3-C2-S2-U001 | pp. 227–250 | index futures, beta/alpha exposure, basis, theoretical futures price, strategies, program trading, delta hedge | MECHANISM, FORMULA, MARKET_RULE | 05 §2 | FULL | Reconstruct basis formula and risks; có worked synthetic-flow exposure; phân biệt basis với term-structure contango; thêm calendar spread |
| B3-C2-S2-U002 | pp. 251–288 | index options, volatility, call/put payoff, Greeks/strategies, spreads/straddle/butterfly | FORMULA, CASE, EXERCISE | 05 §3 | FULL | Giữ payoff và breakeven; thêm delta-neutral, put–call parity, simulation/liquidity boundary, tick-cost/foreign-currency margin example và delta/gamma hedge |
| B3-C2-S3-U001 | pp. 289–314 | rate futures/options/swaps, currency forwards/options/swaps, hedge direction, strip/stack | MECHANISM, CONDITION | 06 §1 | FULL | Nêu exposure sign trước khi hedge; có worked IFR và cap/floor/collar, FRA/IFR, payer/receiver/swaption, cash/physical settlement, CTD, duration/BPV, cross-hedge, interest-parity, NDF/FX margin, range forward, KIKO payoff walkthrough |
| B3-C2-S4-U001 | pp. 315–332 | CDS, TRS, CLN, cash/synthetic, CLO/CDO, commodity futures, contango/backwardation, roll and hedge | INSTITUTION, MECHANISM, EXCEPTION | 06 §2 | FULL | Có bảng payoff CDS/TRS/CLN, worked roll-return và margin/notional example; thêm commodity asset-allocation/global-hedge boundary; giải thích counterparty/basis, physical-delivery/negative-price boundary, commercial vs non-commercial và total-return decomposition |
| B3-C2-S5-U001 | pp. 333–381 | OTC design, participants, ELS/ELB/ELF/DLS/DLB, knock-in/out, taxation, questions | INSTITUTION, PAYOFF, TAX_RULE, EXERCISE | 07 | FULL | Tách underlying/principal condition khỏi wrapper security/fund/trust/deposit; có source-state suitability map, coupon drivers, worst-of, funded/unfunded swap, fees; current tax/rules require snapshot |
| B3-C2-S5-U002 | pp. 333–365 | path-dependent OTC options: Asian, barrier, lookback, ladder, cliquet, shout, digital, Bermudan, chooser, rainbow, quanto, leverage | CLASSIFICATION, PAYOFF, BOUNDARY | 07 §2 | FULL | Nêu trade-off payoff–model risk; thêm Lizard/Ejectable/Swing, daily-rebalanced leverage, autocall stepdown và no-knock-in boundary |

## Audit notes

- Coverage is semantic, not keyword-based: every row has a teaching target and a boundary/relationship in the lesson.
- The source contains OCR noise in symbols and tables. Formulas were reconstructed from page context and checked against the surrounding worked examples; unreadable cells are not silently invented.
- Current Korean tax, exchange rules, margin rates and product specifications are not presented as current facts. Where relevant, the lessons label the source-state claim and direct the reader to official current sources before a real transaction.

## Definition-of-done checks

| Check | Result | Evidence |
|---|---|---|
| Semantic inventory | PASS | 19 stable-ID rows cover pp. 12–381, including formulas, tables, figures, exercises and source-state rules |
| Source-question test | PASS | Lessons explicitly test statistics, portfolio variance, CAPM/SML, EMH tests, return attribution, DCF/EVA, futures/options payoff, hedge direction and structured-product barriers |
| Reconstruction test | PASS | Route README plus eight lessons, including the integrated case lab, reconstruct the dependency graph: uncertainty → portfolio → pricing → valuation → derivative exposure → structured payoff |
| Learner replacement test | PASS with OCR caveat | A learner can study the knowledge-bearing concepts without reopening raw OCR; raw pages remain provenance for unreadable image/table cells |
| Link/whitespace audit | PASS | All Markdown links in the new route resolve; `git diff --check` is clean |

The PASS claims apply to the generated learning route, not to the old `증권투자기초/sach3/raw_md/sach3_legacy.md`; that file is retained as an earlier OCR artifact and is not used as the canonical source for this conversion.
