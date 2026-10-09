# Korea Business & Economy — source ledger và market/currentness boundary

> **Owner:** `korea_business_economy_knowledge_library/` (canonical Korea business/economy content). Ledger này tách official statistics, regulation, filings, market data và author analysis.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| KBE-BOK-01 | Bank of Korea | monetary policy, national accounts, balance of payments và economic statistics | https://www.bok.or.kr/eng/main/main.do | release/series/date phải ghi; kiểm tra 2026-10-09 | Data revision, base year, seasonal adjustment và policy date phải ghi; không biến forecast thành fact | macro/history/case labs |
| KBE-KOSIS-01 | Statistics Korea — KOSIS | Korean population, labor, industry, household và regional statistics | https://kosis.kr/eng/ | table ID/period/revision phải ghi | Indicator definition và revision có thể đổi; portal landing page không đủ | company/industry/society |
| KBE-FSS-01 | Financial Supervisory Service — DART | Korean listed-company filings, disclosures và audit information | https://dart.fss.or.kr/ | filing/report date và company phải ghi | Filing là issuer disclosure, không tự xác nhận truth of projections; status và restatement cần ghi | company case labs |
| KBE-KRX-01 | Korea Exchange | listing, market structure, index/market data và notices | https://global.krx.co.kr/ | release/data timestamp phải ghi | Market snapshot cần as-of/timezone; không suy valuation/strategy từ one snapshot | markets/cases |
| KBE-KFTC-01 | Korea Fair Trade Commission | competition, consumer/business regulation và enforcement notices | https://www.ftc.go.kr/eng/ | notice/law/date phải ghi | Chỉ áp dụng đúng jurisdiction/effective date; website overview không thay legal text | institutions/business policy |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| KBE-MARKET-01 | `NEEDS_SOURCE` | Price, market cap, ranking, growth, exchange status và market share phải có as-of, source table/filing và definition. | Owner market/company chapter |
| KBE-POLICY-01 | `NEEDS_SOURCE` | Tax, competition, ownership, labor, subsidy và financial regulation cần legal/agency notice đúng ngày hiệu lực. | Owner policy chapter |
| KBE-COMPANY-01 | `REVIEW_REQUIRED` | Case study phải tách issuer-reported fact, analyst inference và scenario; không dùng annual-report marketing language làm causal proof. | Owner company case lab |
| KBE-FORECAST-01 | `REVIEW_REQUIRED` | Forecast/consensus phải ghi vintage, model, assumptions và uncertainty; không trình bày như realized result. | Owner macro/industry chapter |

## Quy trình refresh

1. Ghi table/filing/notice ID, period/as-of, jurisdiction, effective date và ngày truy cập.
2. Tách official observation, issuer disclosure, regulation, forecast và author analysis.
3. Khi BOK/KOSIS/KRX/DART/FSC/KFTC revise data hoặc policy, cập nhật affected lessons và mở manual review.
4. Không dùng structural audit để xác nhận market/policy/company claims còn current.
