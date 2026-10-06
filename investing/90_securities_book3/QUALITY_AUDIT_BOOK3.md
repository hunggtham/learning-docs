# QUALITY AUDIT — 증권투자기초 Sách 3

## Final verdict

**PUBLICATION PASS**

Verdict này không kế thừa 19 row `FULL` cũ. Sách 3 được audit lại từ source authority `증권투자기초/sach3/raw_md/sach3.md`, tách semantic inventory theo knowledge-bearing unit, map lại source questions, kiểm tra formula/table/figure, terminology và source-state boundary.

Publication pass ở đây có nghĩa: learning route có thể thay raw OCR cho mục đích học và giải câu hỏi nguồn; những exact cell/label mà OCR không đủ evidence được cô lập thành `SOURCE_AMBIGUITY`, không bị đoán hoặc gọi là `FULL`.

## 1. Architecture / canonical ownership

- Source + provenance + coverage owner: `증권투자기초/sach3/`.
- Canonical learning owner: `investing/90_securities_book3/`.
- Không tái tạo route mới vì dependency architecture hiện tại vẫn hợp lý.
- Lesson 01–07 giữ source-derived learning content; lesson 08 là synthesis/reconstruction layer.
- Enrichment/canonical bridge không được dùng để chứng minh source completeness. Ví dụ: FCFE bridge, BPV/DV01 label/worked hedge, một số execution/data-bias controls.

Result: **PASS**.

## 2. Semantic coverage: source → output

| Metric | Before | After |
|---|---:|---:|
| Semantic rows | 19 | **312** |
| FULL | 19 inherited/coarse | **302 independently re-checked** |
| PARTIAL | not trustworthy under old granularity | **0** |
| MISSING | not trustworthy under old granularity | **0** |
| SOURCE_AMBIGUITY | not separated rigorously | **10** |

Coverage owner: [SOURCE_COVERAGE_BOOK3.md](../../증권투자기초/sach3/SOURCE_COVERAGE_BOOK3.md).

The split covers statistics, Markowitz/utility/diversification, CAPM/CML/SML, three EMH forms/tests/anomalies, performance, valuation, futures/options, rates, FX, credit, commodity and OTC/structured-product units without grouping independent distinctions into a single `FULL` row.

Result: **PASS** because `PARTIAL=0` and `MISSING=0`; all non-readable exact-source artifacts are explicitly marked ambiguity.

## 3. SOURCE_AMBIGUITY / OCR verification

Remaining exact-source ambiguities: **10**.

1. p.251 KOSPI200 futures quote screenshot cells.
2. p.264–267 option theoretical-price / Greeks table and chart cells.
3. p.268 KOSPI200 option historical contract-spec table.
4. p.293 vs p.373 IFR English expansion: “Internal” vs “Implied”.
5. p.297 10Y Treasury-futures historical contract-spec cells.
6. p.308 USD-futures historical contract-spec cells.
7. p.320 pooled credit-product acronym corrupted by OCR while CLO/mechanism remain readable.
8. p.328 crude-futures historical contract-spec screenshot.
9. p.352 exact acronyms for some trust/deposit wrappers.
10. p.357–359 exact cells/graph labels in structured-product prospectus figures.

Exact locations and handling: [SOURCE_AMBIGUITIES_BOOK3.md](../../증권투자기초/sach3/SOURCE_AMBIGUITIES_BOOK3.md).

Repository branch does not contain the original Book 3 PDF/image set required to visually recover these cells. None was reconstructed from outside knowledge. Mechanisms supported by surrounding prose are tracked in separate `FULL` rows.

Result: **PASS with 10 declared SOURCE_AMBIGUITY rows**.

## 4. Formula / table / figure audit

[FORMULA_TABLE_FIGURE_AUDIT_BOOK3.md](../../증권투자기초/sach3/FORMULA_TABLE_FIGURE_AUDIT_BOOK3.md) contains:

- **42 formula-contract rows**: 41 source-backed PASS + 1 explicitly labeled enrichment (BPV/DV01 bridge; source itself teaches duration).
- **16 knowledge-bearing table/figure rows**.
- **9 table/figure rows** whose exact cells remain `SOURCE_AMBIGUITY`; their mechanisms are verified independently.

The contract now covers variables, unit/scale, assumption, mechanism/example and failure boundary for the formulas that control the route: variance/covariance, regression, portfolio variance/MVP/CAL, beta/CML/SML, MWR/TWR, Sharpe/Treynor/Jensen, WACC/DCF/terminal value/EVA, futures basis/theoretical price, option payoff/breakeven/parity/delta-gamma hedge, duration, IFR, FX parity, CDS LGD, commodity carry/roll return and autocall branch payoff.

Result: **PASS**.

## 5. Korean / English terminology audit

[TERMINOLOGY_AUDIT_BOOK3.md](../../증권투자기초/sach3/TERMINOLOGY_AUDIT_BOOK3.md) verifies **117 source-confirmed Korean terms** that are now present at useful occurrences in the learning route; missing audited terms: **0**.

Examples newly normalized or made explicit include:

- statistics: `모집단`, `표본`, `확률변수`, `기하평균`, `조화평균`, `공분산`, `상관계수`, `최소자승법`;
- portfolio/CAPM: `기대효용`, `최소분산 포트폴리오`, `자본배분선`, `시장포트폴리오`, `자본시장선`, `베타`, `증권시장선`;
- performance/valuation: `금액가중수익률`, `시간가중수익률`, `가중평균자본비용`, `여유현금흐름`, `잔여가치`, `경제적 부가가치`, `투하자본이익률`;
- derivatives: `장내파생상품`, `장외파생상품`, `일일정산`, `미결제약정`, `실물인수도`, `내가격/등가격/외가격`, `델타/감마/세타/베가`;
- rates/FX/commodity: `내재선도금리`, `최저인도가 채권`, `스트립헤지`, `스택헤지`, `교차헤지`, `범위 선물환`, `편의수익`, `콘탱고`, `백워데이션`;
- structured products: `주가연계증권`, `숙려기간`, `자체헤징`, `아웃소싱`, `낙인/낙아웃`.

Unverified Korean wording is not invented. NDF, for example, keeps the source description around `실물인수도`, `매매차액` and `현금결제` rather than inserting an unverified source acronym expansion.

Result: **PASS**.

## 6. Structured-product audit

The route now separates, rather than conflates:

- underlying;
- wrapper;
- issuer;
- principal condition;
- coupon driver;
- barrier;
- path dependence;
- maturity / early redemption;
- liquidity;
- issuer/counterparty risk;
- fees / hedge economics;
- tax/source-state rule;
- suitability.

ELS/ELB/DLS/DLB are compared product-by-product. Security/fund/trust/deposit wrappers are a separate layer. `원금보장` in the textbook taxonomy is explicitly not translated into government guarantee or immunity from issuer default.

A substantive semantic bug was corrected: the p.360 `주가연계예금` knock-out example no longer borrows a principal-loss branch from an ELS/barrier note. In the source example the +20% barrier locks/caps the deposit return branch; it is not the trigger for principal loss.

Coupon is consistently separated from expected return and after-tax realized return.

Result: **PASS**.

## 7. Source-question test

[SOURCE_QUESTION_MAP_BOOK3.md](../../증권투자기초/sach3/SOURCE_QUESTION_MAP_BOOK3.md) maps **172** source review/exercise/comprehensive questions or validation items:

`source question → required semantic units → lesson/section`

- mapped: **172**
- PASS: **172**
- FAIL: **0**

This includes statistics, portfolio, CAPM, EMH, performance, valuation, the integrated Chapter 1 set and all 30 comprehensive derivatives questions. The artifact summarizes question intent rather than copying the source into an answer bank.

Result: **PASS**.

## 8. Reverse audit: output → source

| Learning output | Source owner / provenance | Reverse-audit result |
|---|---|---|
| 01 Statistics | pp.12–41 | source-derived core; enrichment not used as coverage evidence |
| 02 Portfolio | pp.42–79 | source-derived Markowitz/utility/MVP/frontier/CAL |
| 03 CAPM/EMH | pp.80–134 | source-derived CAPM + EMH; modern data-bias controls remain enrichment |
| 04 Performance/valuation | pp.135–200 | source-derived performance/DCF/EVA/relative valuation; FCFE explicitly labeled bridge |
| 05 Index derivatives | pp.202–288 | source-derived mechanics; exact historical exchange specs quarantined |
| 06 Rates/FX/credit/commodity | pp.289–332 | source-derived mechanics; BPV/DV01 explicitly enrichment; historical specs quarantined |
| 07 OTC/structured | pp.333–381 | source-derived taxonomy/payoff/risk; rules/tax kept source-state |
| 08 Integrated case lab | cross-chapter synthesis | editorial reconstruction layer; creates no new source claim |

Result: **PASS**.

## 9. Reconstruction test

A learner can reconstruct the required chains without opening another textbook for missing mechanism:

1. distribution → expected value/variance/covariance → regression;
2. covariance/correlation → portfolio variance → diversification → MVP → efficient frontier → CAL;
3. market portfolio → CML → beta → SML/CAPM → pricing adjustment;
4. EMH form → information set → test design → anomaly/interpretation boundary;
5. cash-flow timing → MWR/TWR → risk-adjusted performance;
6. operating cash flow → cost of capital → WACC → DCF/terminal value → EVA/relative valuation;
7. exposure sign → futures basis/carry → option payoff/Greeks/parity → hedge residual risk;
8. rate/FX exposure → IFR/interest parity → cap/floor/collar/swap → KIKO branch payoff;
9. credit event → CDS/TRS/CLN → cash/synthetic securitization;
10. commodity spot/carry → curve → roll return → collateral return;
11. underlying + wrapper + issuer → structured payoff → barrier/path dependence → early redemption/principal/counterparty/liquidity/tax boundary.

Exact OCR-broken historical screenshot cells are not needed to reconstruct these mechanisms and remain explicit ambiguity.

Result: **PASS**.

## 10. Learner-replacement test

For the pedagogical scope of Book 3, the route now satisfies the replacement test:

- concepts needed by mapped source questions are present;
- important formulas have variables/units/assumptions/boundaries;
- worked checks force sign/numeric reasoning;
- Korean terms needed to return to the source are present;
- source-state rules are distinguished from current rules;
- exact historical tables that cannot be recovered are disclosed rather than hidden.

The only reason to reopen the raw/PDF is provenance checking or recovery of the ten exact ambiguous artifacts—not because a core learning mechanism is missing.

Result: **PASS**.

## 11. Current-state / source-state audit

No attempt was made to make every textbook rule “current as of 2026” merely to obtain a pass.

**Current official-state claims newly asserted as current: 0.**

The following remain explicitly `TEXTBOOK/SOURCE STATE` or historical examples unless separately verified later:

- KRX margin / contract specifications / listing details;
- p.337–338 `숙려기간`, loss threshold, age threshold and investor-classification process;
- tax and withholding examples;
- exchange/product eligibility rules;
- historical coupon, rate, notional and contract examples.

Thus the learning route does not present textbook-state regulation as current legal/trading guidance.

Result: **PASS**.

## 12. Link and whitespace audit

- Markdown link occurrences checked: **32**.
- Unique relative targets checked on branch: **21**.
- Broken relative targets: **0**.
- Publication rerun initially found **3 non-printing control bytes** that corrupted escaped LaTeX symbols: one `\\rho` occurrence in `02_PORTFOLIO_THEORY.md` and two `\\beta` occurrences in `04_PERFORMANCE_AND_VALUATION.md`. They were corrected on this branch.
- All **17 Book 3 files** were then rescanned for control characters, trailing whitespace and merge-conflict markers: **0 issues**.

A literal `git diff --check` was attempted through a container checkout, but the execution environment could not resolve `github.com`, so `git clone` failed before Git could run the command. The branch contents were therefore checked independently by fetching every Book 3 text file and scanning the full contents; after the formula-symbol fixes above, the equivalent whitespace/control/conflict check is clean. If the merge workflow requires the literal CLI result rather than equivalent content validation, run `git diff --check main...codex/securities-book3-docs-only` from a networked checkout/CI.

Branch comparison at audit time: Book 3 branch is ahead of `main` with Book 3 work but also behind current `main`; synchronize/rebase according to repository workflow before merge. This is a Git integration state, not a semantic publication failure.

## Acceptance summary

| Gate | Result |
|---|---|
| SOURCE → output semantic audit | PASS |
| output → SOURCE reverse audit | PASS |
| source-question test | PASS — 172/172 |
| reconstruction test | PASS |
| learner replacement test | PASS |
| formula audit | PASS |
| table/figure audit | PASS with 9 exact artifact ambiguities declared |
| KR/EN terminology audit | PASS — 117 source-confirmed terms |
| current/source-state audit | PASS |
| link audit | PASS — 0 broken |
| whitespace/control/conflict equivalent of diff-check | PASS — 17 files, 0 issues; literal CLI blocked by checkout network |
| PARTIAL | **0** |
| MISSING | **0** |
| SOURCE_AMBIGUITY | **10** |

# PUBLICATION PASS
