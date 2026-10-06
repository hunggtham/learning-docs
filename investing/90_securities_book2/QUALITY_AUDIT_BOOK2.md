# QUALITY AUDIT — 증권투자기초 Sách 2

## Final verdict

**PENDING FINAL REPOSITORY CHECKS**

This audit does not inherit the previous Book 2 `PASS` claim. Book 2 was re-audited from the content authority `증권투자기초/raw/sach2.md` under the current `BOOK_MD_TO_LEARNING_DOCS_PROMPT.md` contract. The semantic inventory, Korean terminology, source questions, formula/table/figure handling and reverse audit were rebuilt or independently re-checked.

The final verdict is intentionally held until the latest-main clean-branch check, internal-link/heading audit and literal `git diff --check` have completed.

## 1. Source / architecture / ownership

- Content authority: `증권투자기초/raw/sach2.md`.
- No fake `raw_md/sach2.md` was created.
- No normalized source layer was introduced because the existing raw Markdown is sufficient for all readable concepts; unreadable cells are quarantined as ambiguity.
- Source/provenance/QA owner: `증권투자기초/sach2/`.
- Learning owner: `investing/90_securities_book2/`.
- Canonical domain owners remain `investing/01_foundations/` through `07_integrated_case_studies/`; cross-links do not count as source coverage.
- Book 2 follows the same source/provenance-vs-learning separation used by Book 3. Book 1 remains the documented legacy layout under `증권투자기초/output/book1/`; no fourth layout was created.
- Old branch `feat/securities-investment-book2-learning-edition` was not merged. It was only a prose/reference source.

Result: **PASS**.

## 2. SOURCE → output semantic audit

Coverage owner: [SOURCE_COVERAGE_BOOK2.md](../../증권투자기초/sach2/SOURCE_COVERAGE_BOOK2.md).

| Metric | Re-audited state |
|---|---:|
| Semantic units | **250** |
| FULL | **245** |
| PARTIAL | **0** |
| MISSING | **0** |
| SOURCE_AMBIGUITY | **5** |

The inventory no longer uses review-question mega-rows as semantic coverage. Retired exercise rows `B2-U160`–`U164` and `B2-U242`–`U248` were moved to the source-question audit. ID gaps are intentional, not missing knowledge.

Atomic splits/additions include:

- leading / coincident / lagging indicators;
- IFRS / IASC / IAS / K-IFRS roles;
- triple top vs triple bottom;
- round top vs round bottom;
- KOSPI / KOSPI200 / KOSDAQ / S&P 500 / Nikkei 225 source examples;
- callable bond vs puttable bond;
- coupon rate vs current yield vs YTM comparison.

The fixed-income products explicitly required by the audit are independently trackable: convertible, warrant, exchangeable, callable, puttable, ABS, MBS, CMO, floating-rate, reverse floater, preferred, catastrophe, indexed, international, foreign, eurobond and structured-note families.

Result: **PASS** because there are no PARTIAL/MISSING knowledge units and each remaining semantic ambiguity has a source-evidence reason.

## 3. SOURCE_AMBIGUITY / OCR audit

Detailed owner: [SOURCE_AMBIGUITIES_BOOK2.md](../../증권투자기초/sach2/SOURCE_AMBIGUITIES_BOOK2.md).

Unresolved records: **7 total**.

1. pp.24–26 / raw ~L475–520 — exact Korean headings/variable labels for macro subsections 5.1.3–5.1.4.
2. pp.26–28 / raw ~L600–660 — exact headings/labels for macro subsections 5.1.6–5.1.8.
3. pp.68–71 / raw ~L1370–1510 — exact labels/numerators/cells in the ratio block before readable ROI/ROE.
4. pp.126–144 / raw ~L2500–2740 — Diamond Pattern exact figure coordinates/numeric target geometry.
5. pp.247–248 / raw ~L4890–4910 — independent meaning of the separate “Asset-Backed Bond” heading beside ABS.
6. pp.198–216 / raw ~L3830–4260 — exact cells/options/numbers for part of the stock review set.
7. pp.368–390 / raw ~L7120–7950 — exact cells/options/numbers/figures for part of the bond review set.

The first five are semantic-inventory ambiguity rows. The last two are question-artifact ambiguities and are not disguised as knowledge units. The repository contains no separate Book 2 image/PDF asset capable of resolving them, so none was guessed.

Result: **PASS WITH DECLARED AMBIGUITY**.

## 4. Korean / English terminology audit

Detailed owner: [TERMINOLOGY_AUDIT_BOOK2.md](../../증권투자기초/sach2/TERMINOLOGY_AUDIT_BOOK2.md).

- Audited terminology rows: **83**.
- Exact Korean terms missing from the six-lesson route after audit: **0**.
- Korean labels invented from unreadable OCR cells: **0**.

Terminology restored or normalized in the learning route includes:

- foundations/macro: `증권`, `증권분석`, `경기순환`, `경제지표`, `재무제표`, `재무비율`;
- return/valuation: `수익률`, `요구수익률`, `자본자산가격결정모형`, `순현재가치`, `배당할인모형`, `가중평균자본비용`, `경제적 부가가치`;
- multiples: `주가수익비율`, `주가순자산비율`, `주가매출비율`;
- technical analysis: `기술적 분석`, `지지선`, `저항선`, `이동평균선`, `봉차트`, `상대강도지수`, `스토캐스틱`, `볼린저밴드`, `엔벨로프`, `다우이론`, `엘리어트 파동이론`;
- strategy/index: `투자전략`, `분산투자`, `주가지수`;
- fixed income: `채권평가`, `전환사채`, `신주인수권부사채`, `교환사채`, `자산유동화증권`, `주택저당증권`, `변동금리채`, `역변동금리채`, `지수연동채권`, `구조화채권`;
- yield/credit/market: `할인율`, `내부수익률`, `만기수익률`, `수익률곡선`, `신용위험`, `부도위험`, `신용등급`, `수정듀레이션`, `볼록성`, `채권지수`, `총수익지수`, `발행시장`, `유통시장`, `환매조건부매매`.

Where the OCR does not reliably preserve a Korean textbook label — e.g. MACD/OBV/VR/P&F, CMO, Callable/Puttable Bond, Preferred Habitat Theory and auction labels — the route keeps the stable English/source term rather than inventing Hangul.

Result: **PASS**.

## 5. Formula / table / figure audit

Detailed owner: [FORMULA_TABLE_FIGURE_AUDIT_BOOK2.md](../../증권투자기초/sach2/FORMULA_TABLE_FIGURE_AUDIT_BOOK2.md).

- Formula/quantitative-contract rows: **43 PASS**.
- Knowledge-bearing table/figure rows: **21**.
- Table/figure rows carrying an explicit ambiguity boundary: **5**.

Reconstructed/re-verified high-risk items include CSI/BSI/CI-vs-DI, BCG, financial-ratio families, compounding/PV, CAPM, NPV/PVGO, DDM/Gordon, FCFE/FCFF, **explicit WACC**, EVA/ROIC, PER/PBR/PSR/EV-EBITDA, SMA/EMA/MACD/RSI/Stochastic/Bollinger/Envelope/OBV/VR/P&F, portfolio variance, stock-index construction, bond valuation, coupon/current yield/YTM, spot/forward relation, Macaulay/modified duration, convexity, total-return bond index, tracking error and repo haircut.

A concrete regression found during this audit was fixed: WACC had previously been described in prose without its explicit source-backed formula. The route now states

`WACC = [E/(D+E)]Re + [D/(D+E)]Rd(1−T)`

with variable ownership, market-value-weight/tax-shield assumptions and the FCFF matching boundary. The FCFF↔FCFE bridge also defines the net-debt sign convention so the OCR wording cannot cause double-counting.

Result: **PASS**.

## 6. Source-question test

Detailed owner: [SOURCE_QUESTION_MAP_BOOK2.md](../../증권투자기초/sach2/SOURCE_QUESTION_MAP_BOOK2.md).

- Recoverable question/concept clusters mapped: **31**.
- PASS: **31**.
- FAIL: **0**.
- Exact review-set ambiguity records: **2**.

The map covers index identification, BCG, valuation multiples, technical indicators, term-structure theories, discounting, coupon/current yield/YTM, duration/modified duration/convexity, credit/rating, primary/secondary markets, auction, repo and bond-index/total-return logic. It summarizes question intent instead of reproducing an answer bank.

Where exact option wording or figures are unreadable, the map points to `SRC-A06`/`SRC-A07`; no answer is inferred from corrupted OCR.

Result: **PASS WITH DECLARED QUESTION AMBIGUITY**.

## 7. Output → SOURCE reverse audit

| Learning output | Source scope | Reverse-audit result |
|---|---|---|
| 01 macro / company / statements / ratios | roughly pp.10–76 | source-derived core; CI/DI and ratio explanations reconstruct readable mechanisms; corrupted exact ratio cells remain ambiguity |
| 02 equity valuation / multiples | roughly pp.78–104 | source-derived CAPM/NPV/PVGO/DDM/FCF/WACC/EVA/multiples; worked numbers are pedagogical reconstruction, not new source claims |
| 03 technical analysis | roughly pp.106–180 | source-derived patterns/candles/indicators/Dow/Elliott; pattern geometry not readable enough is not invented |
| 04 strategy / portfolio / stock index | roughly pp.182–216 | source-derived strategy/index/portfolio logic; benchmark/current-index mechanics beyond source are not claimed as current |
| 05 bond instruments | roughly pp.217–250 | source-derived fixed-income taxonomy including independently split callable/puttable; comparison/checklist prose is editorial reconstruction |
| 06 yield / term structure / credit / duration / market / repo / index | roughly pp.250–390 | source-derived formulas/theories/market mechanisms; modern institutional use must be checked in canonical/current sources |

Editorial worked examples, checklists, stress/backtest framing and cross-links are allowed as teaching/reconstruction layers but are not used as evidence for a source row unless the coverage matrix points to a source-backed mechanism.

Result: **PASS**.

## 8. Reconstruction test

A learner can now reconstruct, without reopening another textbook for a missing mechanism:

1. claim type → stock/bond cash-flow priority → risk/return;
2. business cycle → economic indicators → CSI/BSI → CI/DI → industry/company analysis;
3. statements → ratio families → ROI/ROE/DuPont;
4. required return → CAPM → NPV/PVGO → DDM/Gordon → FCFE/FCFF/WACC → EVA;
5. PER/PBR/PSR/EV-EBITDA → denominator/economic driver → failure boundary;
6. price/volume → trend/support/resistance → moving average → price patterns/candles → indicators → Dow/Elliott;
7. strategy → diversification → portfolio variance → index weighting/divisor/total-return distinction;
8. bond cash flow → price → embedded option/product taxonomy → payoff/risk distinction;
9. discount rate/IRR/YTM → spot/forward → term-structure theories;
10. default/credit rating/spread → duration/modified duration/convexity;
11. primary/secondary market → auction → repo → bond-index/total-return benchmark.

Result: **PASS**.

## 9. Learner replacement test

For the source-confirmed scope of Book 2:

- all semantic units are FULL or explicit SOURCE_AMBIGUITY;
- high-risk formulas have variables/assumptions/boundaries and worked checks where needed;
- major technical patterns/indicators are separated enough to detect a missing item;
- fixed-income products are not collapsed into one taxonomy row;
- Korean terminology is present where the learner needs to return to the Korean source;
- source questions are mapped without fabricating unreadable answer choices;
- exact OCR-broken artifacts are disclosed instead of silently repaired.

A learner should only need the raw source for provenance checking or future recovery of the seven ambiguity records, not because a readable core mechanism is absent.

Result: **PASS**.

## 10. Current-state / textbook-state audit

No 2026 market rule, index constituent list, tax rule or regulatory claim was silently inferred from the textbook.

KOSPI/KOSPI200/KOSDAQ/S&P 500/Nikkei 225, KSDA-BLP, rating-agency notation, auction labels, LIBOR examples and other institutional names are treated as **source/textbook-state examples** unless a section explicitly points to a current canonical owner. The route explicitly warns that index composition/methodology, benchmarks, rules and market conventions require current official verification before real-world use.

Result: **PASS**.

## 11. Navigation / links / repository checks

Pending final branch checks:

- internal-link audit;
- heading/navigation audit;
- latest-main branch status;
- changed-file scope;
- literal `git diff --check`.

The final verdict above must not be changed from PENDING until all four pass.
