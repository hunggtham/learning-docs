# Sách 1 — Source coverage matrix

Artifact này là bảng truy nguyên semantic unit của `raw_md/sach1.md` tới learning
edition. `FULL` nghĩa là người học có thể hiểu và áp dụng nội dung từ learning
docs mà không cần mở source để bù knowledge-bearing content. Các rule lịch sử,
OCR ambiguity và current-law boundary được ghi ở cột Notes; chúng không bị âm
thầm thay bằng quy định 2026.

| Source ID | Source location | Semantic unit | Type | Target lesson | Status | Notes/action |
|---|---|---|---|---|---|---|
| CH1-01 | p13–16 | 금융시장: định nghĩa/chức năng | CONCEPT | `01` §§1,6–8 | FULL | mental model và boundary |
| CH1-02 | p14–16 | 직접금융 / 간접금융 | DISTINCTION | `01` §§2,7 | FULL | flow tiền và principal/agent |
| CH1-03 | p14–16 | 단기금융시장 / 자본시장 | CLASSIFICATION | `01` §2 | FULL | phân loại theo kỳ hạn |
| CH1-04 | p16–18 | nhóm tổ chức tài chính | TABLE | `01` §§4,10 | FULL | bảng nhóm và ví dụ |
| CH1-05 | p19–20 | nghĩa rộng/hẹp của 증권시장 | DEFINITION | `03` §§1,8 | FULL | abstract vs organized market |
| CH1-06 | p19–20 | 발행시장 / 유통시장 | DISTINCTION | `01` §5; `03` §§2,5 | FULL | flow vốn/chứng khoán |
| CH1-07 | p19–20 | năm chức năng kinh tế | MECHANISM | `03` §§3,7 | FULL | cause → consequence |
| CH1-08 | p37–39 | 자본집중/소유분산/경제조정 | RELATIONSHIP | `03` §7 | FULL | nối chức năng vào issuance |
| CH1-09 | p40–44 | issuer/investor/underwriter và 간사단/인수단/청약단 | INSTITUTION | `03` §§4.1–4.2 | FULL | role/revenue/risk |
| CH1-10 | p41–43 | 공모 / 사모 và ngưỡng 50 người | LEGAL_RULE | `03` §4.3 | FULL | source snapshot |
| CH1-11 | p42–44 | 총액인수/잔액인수/모집주선 | PROCESS | `03` §4.4 | FULL | risk allocation |
| CH1-12 | p45–47 | KRX–broker–KSD–investor flow | FIGURE | `03` §5; `04` §§2,6 | FULL | reconstructed flow |
| CH1-13 | p21–23 | 금융투자상품, 투자성 và ngoại lệ | DEFINITION | `02` §§1,7 | FULL | condition/exception |
| CH1-14 | p22–23 | loss ratio/product table | TABLE | `02` §2 | FULL | reconstructed decision tree |
| CH1-15 | p23–25 | 증권/투자계약증권/파생결합증권 | CLASSIFICATION | `02` §§2–3,7–8 | FULL | rights and boundary |
| CH1-16 | p25 | fractional capital/marketability/risk-return | MECHANISM | `02` §4 | FULL | why securities exist |
| CH1-17 | p26–30 | stock and preferred-stock rights | CLASSIFICATION | `02` §5 | FULL | participating/cumulative/voting |
| CH1-18 | p30–34 | bond classifications and cash flows | CLASSIFICATION | `02` §6 | FULL | collateral, interest, maturity, hybrids |
| CH1-19 | p34–44 | securities-market structure | PROCESS | `03` §§2–4 | FULL | issuance → circulation |
| CH1-20 | p47–55 | KOFIA/KRX/KSD/Koscom and regulators | INSTITUTION | `04` §§1–2 | FULL | duties and system position |
| CH1-21 | p54–56 | six 금융투자업 | LEGAL_RULE | `04` §§3,11,14 | FULL | principal/agent and revenue model |
| CH1-22 | p56–59 | 인가 vs 등록 | LEGAL_RULE | `04` §§4,11 | FULL | risk-based entry logic |
| CH1-23 | p57–59 | 업무단위/product-investor units/capital | TABLE | `04` §11 | FULL | source capital snapshot |
| CH1-24 | p59–61 | 지급결제/겸영/부수업무 | LEGAL_RULE | `04` §§5,12 | FULL | seven-day notice marked historical |
| CH1-25 | p61–66 | IPO purpose and 신주모집/구주매출/hybrid | PROCESS | `05` §§1–3,9 | FULL | money destination |
| CH1-26 | p63–66 | 액면발행/시가발행 | DISTINCTION | `05` §§5,10 | FULL | source method |
| CH1-27 | p67–74 | 유상/무상/포괄/병행 증자 | CLASSIFICATION | `05` §5 | FULL | rights and dilution |
| CH1-28 | p64–90 | issuance formula and listing requirements | FORMULA | `05` §§6–14 | FULL | SOURCE_AMBIGUITY: OCR formula and historical thresholds explicitly marked |
| CH1-29 | p90–99 | trading methods, priority, one/multi-price | MARKET_RULE | `06` §§2–3 | FULL | order book reasoning |
| CH1-30 | p96–100 | hours, limits, settlement | TABLE | `06` §§4–5,12 | FULL | historical snapshot |
| CH1-31 | p98–100 | 자기주식 rules | LEGAL_RULE | `06` §15 | FULL | account/price/quantity limits |
| CH1-32 | p101–105 | 관리종목/상장폐지/정리매매/overheating | MARKET_RULE | `06` §§7,11,16 | FULL | criteria and lifecycle |
| CH1-33 | p106–115 | order types, IOC/FOK, off-hours, Sidecar | MARKET_RULE | `06` §§6–7 | FULL | condition table |
| CH1-34 | p116–121 | disclosure requirements | LEGAL_RULE | `06` §9 | FULL | four quality requirements |
| CH1-35 | p122–163 | KOSDAQ/KONEX/K-OTC/NXT | MARKET_RULE | `06` §§10–18 | FULL | venue checklists; current rules separate |
| CH1-36 | p164–183 | futures/options/ELW/stock derivatives | FORMULA | `07` §§1–9 | FULL | payoff, leverage, expiry, hedge/speculation |
| CH1-37 | p184–198 | dividend/interest/transaction/capital tax | TAX_RULE | `08` §§1–12 | FULL | taxpayer/event/base/withholding |
| CH1-38 | p198–205 | M&A types/payment/combination | CLASSIFICATION | `09` §§1–2,5–6,9 | FULL | full source taxonomy |
| CH1-39 | p199–205 | 공개매수/reporting/treasury/proxy | LEGAL_RULE | `09` §§3,10 | FULL | source thresholds marked historical |
| CH1-40 | p211–232 | chapter 1 review questions | EXERCISE | `90` | FULL | range-to-lesson mapping |
| CH2-01 | p234–242 | 집합투자 definition/boundaries | DEFINITION | `10` §§1,9 | FULL | four statutory conditions |
| CH2-02 | p242–248 | legal forms and participants | CLASSIFICATION | `11` §§1–2 | FULL | ownership/duties |
| CH2-03 | p248–250 | NAV/기준가격/unit math | FORMULA | `11` §5 | FULL | worked unit calculation |
| CH2-04 | p249–250 | fees/TER/performance fee | TABLE | `11` §§6–7,9 | FULL | fee vs expense |
| CH2-05 | p250–253 | suitability/adequacy/explanation/unfair solicitation | LEGAL_RULE | `11` §§7–8 | FULL | decision flow |
| CH2-06 | p255–262 | pricing/subscription/redemption/deferral/open-close | PROCESS | `11` §§4,8,10 | FULL | timing and exceptions |
| CH2-07 | p263–293 | asset classification/REIT/special/mixed/derivative | CLASSIFICATION | `12` §§1–9,14–15 | FULL | thresholds and flows |
| CH2-08 | p294–298 | fund-of-funds/master-feeder/class/umbrella/wrap | STRUCTURE | `12` §§10,14 | FULL | limits and cost layers |
| CH2-09 | p299–313 | active/passive/ETF/region/infrastructure/PE/hedge | CLASSIFICATION | `12` §§11–13 | FULL | source distinctions |
| CH2-10 | p314–319 | risk profile/time horizon/allocation | PROCESS | `13` §§1–2,8 | FULL | five-level and horizon matrix |
| CH2-11 | p320–322 | prospectus/simplified prospectus/asset report | TABLE | `13` §§3,11 | FULL | field checklist |
| CH2-12 | p323–326 | fund selection/category return/risk | PROCESS | `13` §4 | FULL | like-for-like comparison |
| CH2-13 | p326–327 | standard deviation/beta/benchmark excess | FORMULA | `13` §§4–5,9 | FULL | variables and intuition |
| CH2-14 | p333–334 | fund taxation | TAX_RULE | `13` §§0,6 | FULL | SOURCE STATE vs CURRENT STATE |
| CH2-15 | p341–351 | 30 review questions and Sharpe | EXERCISE | `90`, `13` | FULL | question ranges and worked formula |

## Acceptance

`FULL = 55`, `PARTIAL = 0`, `MISSING = 0`. Remaining `SOURCE_AMBIGUITY` markers
are not unowned gaps: they identify OCR-fragile formulas or historical rules that
must not be silently presented as current law.

Detailed audit, time-sensitive register and reverse-audit notes remain in
[`BOOK1_SOURCE_COVERAGE_AUDIT.md`](./BOOK1_SOURCE_COVERAGE_AUDIT.md).
