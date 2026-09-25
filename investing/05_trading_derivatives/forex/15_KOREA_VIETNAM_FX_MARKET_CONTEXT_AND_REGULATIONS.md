# 15 — Korea / Vietnam FX market context và regulations

> **Time-sensitive chapter.** Phần regulatory phải được kiểm tra lại trước khi dùng cho quyết định thực tế. Nội dung dưới đây được research theo nguồn chính thức đang truy cập ngày **2026-09-25** và phục vụ học cấu trúc thị trường, không thay thế tư vấn pháp lý/thuế/compliance.

Forex không vận hành giống nhau ở mọi quốc gia. Cùng từ “FX” có thể chỉ:

- interbank spot market;
- corporate hedging;
- exchange-traded futures;
- regulated retail FX-margin product;
- OTC derivative;
- simple currency conversion.

Vì vậy trước khi mở tài khoản hoặc backtest một instrument, phải hỏi:

```text
Jurisdiction
→ legal product category
→ permitted intermediary
→ account / remittance rules
→ margin / investor-protection rules
→ tax / reporting
→ actual executable instrument
```

## Part I — Korea

## 1. USD/KRW quote

```text
USD/KRW = KRW per 1 USD
```

Nếu USD/KRW tăng:

```text
USD strengthens vs KRW
KRW weakens vs USD
```

Tiếng Hàn:

- tỷ giá: **환율**;
- ngoại hối: **외환**;
- won mạnh: **원화 강세**;
- won yếu: **원화 약세**;
- rủi ro tỷ giá: **환위험**;
- phòng vệ tỷ giá: **환헤지**.

## 2. Korea FX market không chỉ là retail app

Các layer cần phân biệt:

```text
Seoul wholesale FX market
Bank/customer FX transactions
NDF/offshore KRW markets
Currency futures/derivatives
Retail FX-margin trading
Simple bank currency exchange
```

Rules và participant set khác nhau.

## 3. Seoul FX market structural reform

Bank of Korea và government triển khai **외환시장 구조 개선방안 — improvement measures for FX market structure** để tăng global market access.

Key changes gồm:

- foreign financial institutions đủ điều kiện có thể đăng ký thành **Registered Foreign Institution (RFI)** và tham gia thị trường;
- market infrastructure/practices được điều chỉnh cho broader access;
- trading hours của Seoul FX market được kéo dài.

BOK duy trì portal và danh sách RFI chính thức; list được update theo thời điểm nên không copy một danh sách cố định vào tài liệu.

## 4. Trading hours

Theo BOK market-structure information, từ **July 2024** Seoul FX market operating hours được mở rộng từ session cũ tới:

```text
09:00 Korea time
→ 02:00 next day
```

Mục tiêu là overlap tốt hơn với London và New York hours.

Điều này quan trọng cho data research: backtest USD/KRW trước và sau reform có khác biệt về session/liquidity structure.

## 5. RFI

**Registered Foreign Institution (RFI)** là foreign financial institution đáp ứng requirements và đăng ký với Korean FX authorities để tham gia theo framework mới.

RFI reform làm:

- direct access của global institutions tăng;
- participant mix thay đổi;
- price discovery/liquidity dynamics có thể thay đổi theo giờ.

Do đó historical microstructure trước 2024 không nên assumed identical với current market.

## 6. Seoul Code of Conduct / FX Global Code

Seoul Foreign Exchange Market Committee có code về:

- responsibilities;
- ethics/confidentiality;
- dealing principles;
- documentation;
- order handling;
- operational practices.

BOK cũng có Seoul Register cho market participants công bố Statement of Commitment với FX Global Code.

Đây là institutional-market conduct framework, không phải trading strategy.

## 7. BOK và monetary-policy channel

USD/KRW research thường cần theo dõi:

```text
BOK expected policy path
vs Fed expected policy path
```

Nhưng rate differential chỉ là một channel.

KRW còn nhạy với:

- Korean export cycle;
- semiconductor demand;
- energy import prices;
- foreign equity/bond flows;
- broad USD;
- China/global growth;
- risk sentiment;
- intervention/policy expectations.

## 8. Export/semiconductor channel

Korea có export-heavy industrial structure; semiconductor cycle có thể ảnh hưởng:

```text
export receipts
corporate FX conversion
growth expectations
foreign equity flows
```

Không nên dùng rule đơn giản “semiconductor up → KRW up”, nhưng đây là causal channel cần nghiên cứu.

## 9. Energy import channel

Korea phụ thuộc nhiều vào imported energy.

Energy shock có thể:

```text
import bill ↑
→ terms of trade deteriorate
→ inflation pressure ↑
→ corporate/household real income pressure
```

FX response còn phụ thuộc policy and global USD regime.

## 10. Foreign portfolio flows

Foreign buying/selling Korean equities/bonds có thể tạo FX hedging/conversion demand.

Need distinguish:

```text
asset flow
currency hedge ratio
actual FX conversion
```

Foreign investor buying Korean stock không có nghĩa toàn notional immediately buys KRW unhedged.

## 11. Onshore vs offshore KRW

KRW price discovery có thể liên quan:

- onshore USD/KRW market;
- offshore NDF;
- global derivatives.

Different sessions/access rules create lead-lag and basis relationships.

Market reform is intended partly to improve onshore accessibility, so relationships may evolve.

## 12. Retail FX-margin trading in Korea

**FX마진거래** là một specific regulated product category in Korean investor guidance, không đồng nghĩa toàn bộ spot FX market.

Korea Financial Investment Association (KOFIA) describes FX-margin trading as leveraged foreign-currency derivative-style trading with standardized contract conventions and margin.

Important: product terms must be checked at the licensed Korean financial investment company; old/general web examples are not substitute for current contract specification.

## 13. Korean retail intermediary requirement

KOFIA's current investor-warning material states that an individual participating in FX-margin trading must use a **domestic investment intermediary (국내 투자중개업자)** under the Korean capital-markets framework.

KOFIA specifically warns that direct trading with an overseas financial investment business without going through the permitted domestic derivatives/investment intermediary is illegal under the framework it describes, and related remittance may also violate foreign-exchange rules.

Practical learning rule:

```text
Do not assume:
“Broker accepts Korean residents”
=
“Trading route is lawful in Korea.”
```

Verify exact legal entity and Korean intermediary route.

## 14. Korea FX-margin risk disclosures

KOFIA highlights risks including:

- leverage magnifying loss;
- spread/rollover cost;
- counterparty risk;
- system/electronic-trading failure;
- unauthorized intermediaries;
- exaggerated return marketing.

This aligns with the mechanics studied in chapters 03 and 05.

## 15. Domestic license check

Before any real product use, verify:

```text
Exact Korean financial investment company
Permitted derivatives brokerage activity
Account agreement
Margin requirement
FDM / overseas counterparty structure
Remittance route
Investor-protection disclosures
```

Do not verify only brand/domain.

## 16. FX margin vs bank currency exchange

Buying USD at a Korean bank for travel/savings is not the same product as leveraged FX-margin trading.

Different:

```text
purpose
settlement
leverage
legal category
intermediary
risk
```

Do not import FX-margin rules blindly into ordinary bank FX transactions.

## 17. Korea research timeline break

For data studies, mark structural dates such as:

```text
pre-RFI / old hours
→ RFI opening phase
→ July 2024 extended-hours regime
→ later rule/infrastructure changes
```

A strategy's session effect may shift after market reform.

---

# Part II — Vietnam

## 18. USD/VND quote

```text
USD/VND = VND per 1 USD
```

If USD/VND rises:

```text
VND weakens relative to USD
```

Vietnam FX framework has stronger administrative/regulatory structure than free-floating major pairs, so policy regime matters heavily.

## 19. Official regulatory center

The **State Bank of Vietnam (Ngân hàng Nhà nước Việt Nam, SBV)** is the central authority for foreign-exchange management.

Research should begin from:

- Ordinance on Foreign Exchange and amendments;
- implementing decrees;
- SBV circulars;
- current official legal database.

Do not infer Vietnam rules from US/EU/Korean broker practices.

## 20. Authorized credit institutions

Vietnam rules distinguish **tổ chức tín dụng được phép hoạt động ngoại hối — credit institutions authorized for FX activities**.

SBV Circular 02/2021/TT-NHNN framework governs foreign-currency transactions in the domestic FX market between authorized credit institutions and customers.

The circular defines customers to include resident/non-resident organizations and individuals, while transaction permissions vary by customer type and purpose.

## 21. Products in the domestic framework

The regulatory definitions include categories such as:

- spot;
- forward;
- swap;
- options;

but permitted use depends on institution, customer category and regulatory conditions.

Do not assume that because a product type exists in banking regulation, a resident individual may freely use a foreign retail leveraged broker for speculative trading.

## 22. Resident individual transactions

Under the SBV framework retrieved for this chapter, authorized credit institutions may conduct specified FX transactions with resident individuals, including spot and certain forward transactions according to applicable rules.

The legal/economic context is generally tied to the regulated domestic FX system and lawful FX needs; it is not equivalent to an unrestricted global retail CFD/FX account.

Before practical use, check the current consolidated text and the bank's permitted services.

## 23. USD/VND pricing framework

For domestic USD/VND transactions, SBV regulations link spot pricing to the official **central exchange rate (tỷ giá trung tâm)** and the permitted trading band/regime in force.

Because the band/rules can change, this chapter intentionally does not freeze a current percentage.

Research pipeline should version:

```text
central rate
band/regime
policy change dates
actual bank/interbank quotes
```

## 24. Exchange-rate regime matters

USD/VND should not be modeled exactly like EUR/USD.

Possible drivers include:

- SBV policy framework;
- inflation/growth;
- trade balance;
- FDI;
- remittances;
- USD cycle;
- reserves/intervention;
- domestic liquidity/rates;
- capital-flow management.

Administrative rules can create nonlinear behavior near policy boundaries.

## 25. Official vs free-market prices

Vietnam historically has formal regulated FX channels and restrictions on unauthorized currency exchange.

For research, distinguish:

```text
official/interbank/bank quotes
licensed exchange channels
informal/free-market observations
```

Do not merge them into one clean price series without labeling source/legal context.

## 26. Foreign-currency use onshore

Vietnam's foreign-exchange legal framework restricts use of foreign currency within Vietnamese territory except permitted cases.

This affects:

- payments;
- quoting;
- settlement;
- account use.

It is a monetary/legal framework, not just a broker rule.

## 27. Unauthorized exchange risk

Current Vietnamese administrative-sanction rules include penalties for certain unauthorized foreign-currency buying/selling and transactions outside permitted entities/channels.

Therefore “I can find someone/app to exchange/trade” is not equivalent to a legally permitted channel.

## 28. Overseas retail Forex/CFD caution for Vietnam residents

For this library, do **not** state a blanket simple rule such as “all Forex is legal” or “all Forex is illegal”. The legal result depends on:

```text
resident status
product
counterparty
remittance route
purpose
licensed activity
foreign-exchange controls
```

What is clear from the domestic framework is that Vietnam tightly regulates foreign-exchange activities and designates authorized institutions/channels.

Before sending funds to an overseas FX/CFD platform, a Vietnam resident should verify current SBV/foreign-exchange rules and legal remittance purpose rather than rely on broker marketing.

## 29. International Financial Center developments

Vietnam introduced specific 2025 rules for the **International Financial Center (IFC)**, including Decree 329/2025/NĐ-CP and SBV Circular 72/2025/TT-NHNN concerning foreign-exchange/account matters inside that special framework.

Important:

```text
IFC-specific rule
≠ automatic nationwide retail rule
```

Always check scope, eligible entity and effective provisions.

## 30. VND is not just a high-yield/low-yield currency signal

Because of policy regime and capital-flow framework, simple carry models from freely traded G10 FX can fail.

Need model:

```text
policy band / intervention
onshore liquidity
capital controls / convertibility constraints
forward market access
hedging instruments
```

## 31. Vietnam corporate hedging

Import/export businesses may have genuine FX exposures:

```text
USD receivables
USD payables
foreign-currency debt
```

Authorized banks can provide permitted FX products under regulation.

Corporate hedge objective should be cash-flow risk management, not evaluated as standalone speculative P/L.

## 32. Korea–Vietnam business exposure

For a Korea-linked company operating in Vietnam, economic exposures may include:

```text
KRW
USD
VND
```

Even if invoice currency is USD, costs/revenue may be VND and reporting currency KRW.

Need map all three layers.

## 33. Triangular exposure

Example:

```text
Vietnam subsidiary earns VND
purchases imported inputs in USD
parent reports in KRW
```

Risk cannot be summarized by one USD/VND chart.

Need analyze:

```text
transaction exposure
translation exposure
economic exposure
```

## 34. Transaction exposure

Contractual cash flow in foreign currency.

Example: USD payable in 90 days.

Can be hedged with permitted forward/other instrument where legally/operationally available.

## 35. Translation exposure

Financial statements of foreign subsidiary converted into parent reporting currency.

This accounting exposure differs from cash transaction risk.

## 36. Economic exposure

Long-run business competitiveness changes when FX changes.

Example: KRW/VND/USD shifts change relative labor/input/export economics even without explicit FX payable.

## 37. Research source hierarchy for Korea

Prefer:

```text
Bank of Korea
Ministry of Economy and Finance
Financial Services Commission / Financial Supervisory Service
KOFIA
KRX / licensed intermediaries
```

Then high-quality secondary analysis.

## 38. Research source hierarchy for Vietnam

Prefer:

```text
State Bank of Vietnam
National legal database / official government legal texts
Ministry/Government decrees
Authorized bank official product terms
```

Do not use affiliate broker websites as legal source.

## 39. Regulatory versioning

For every regulatory note, store:

```text
source URL
publication date
effective date
retrieval date
scope
whether amended/repealed/consolidated
```

This is especially important because FX controls evolve.

## 40. Broker/product checklist for a Korea resident

```text
Is this FX-margin, futures, CFD, or currency conversion?
Which Korean legal category?
Which domestic licensed intermediary?
Is direct overseas dealing permitted for this route?
How are funds remitted?
What margin/protection applies?
What is the exact foreign counterparty?
```

## 41. Product checklist for a Vietnam resident

```text
What is the lawful FX purpose?
Which authorized institution?
Which product is permitted for this customer type?
What account/remittance rule applies?
Is an overseas account/platform legally fundable for this activity?
What reporting/document requirements exist?
```

## 42. Do not treat regulation as static strategy edge

A pricing anomaly caused by access restriction can disappear after reform.

Examples:

- Korea RFI access;
- extended trading hours;
- new special financial-center framework in Vietnam.

Structural change should be a breakpoint in backtest.

## 43. Korea/Vietnam chapter is context, not recommendation

This chapter should answer:

```text
What market am I observing?
Who can participate?
Which instrument is legal/available?
Which policy framework shapes the price?
Which data discontinuities matter?
```

It should not rank brokers or tell the reader to open a leveraged account.

## 44. Final learning checklist

After the full Forex path, you should be able to explain:

1. Why FX is a relative price.
2. OTC vs exchange market structure.
3. Spot/forward/swap/futures/options differences.
4. Pips/lots/notional/P&L.
5. Margin/leverage/position sizing.
6. Relative macro and carry.
7. Price action/indicator limitations.
8. Event-study and point-in-time research.
9. Strategy families and robustness.
10. Currency/factor portfolio risk.
11. Journal and attribution.
12. Microstructure/order flow.
13. FX options/volatility.
14. Why Korea and Vietnam require jurisdiction-specific market/regulatory models.

## Sources — Korea

- Bank of Korea — FX Market Structure Improvement Portal: https://www.bok.or.kr/portal/main/contents.do?menuNo=201250
- Bank of Korea — Improvement Measure of FX Market Structure: https://www.bok.or.kr/eng/main/contents.do?menuNo=400416
- Bank of Korea — Registered Foreign Institutions list: https://www.bok.or.kr/eng/bbs/B0000367/view.do?menuNo=400489&nttId=10082323
- Bank of Korea — Seoul FX Market / FX Global Code materials: https://www.bok.or.kr/eng/main/contents.do?menuNo=400365
- Korea Financial Investment Association — FX Margin definition/structure: https://www.kofia.or.kr/wpge/m_73/sub03040401.do
- Korea Financial Investment Association — FX Margin investor precautions: https://www.kofia.or.kr/wpge/m_74/sub03040402.do
- Korea Financial Investment Association — Illegal FX Margin transaction types: https://www.kofia.or.kr/wpge/m_75/sub03040403.do
- Bank of Korea — Foreign Exchange Transaction Regulations / current rules portal: https://www.bok.or.kr/portal/bbs/P0002014/view.do?menuNo=200402

## Sources — Vietnam

- State Bank of Vietnam / National Legal Database — Circular 02/2021/TT-NHNN and current related legal texts: https://vbpl.moj.gov.vn/nganhangnhanuoc/Pages/vbpq-toanvan.aspx?ItemID=147142
- Ordinance / legal framework on foreign exchange and implementing regulations via official national legal database: https://vbpl.moj.gov.vn/
- Government Decree 329/2025/NĐ-CP — International Financial Center FX/banking framework: https://vbpl.vn/TW/Pages/vbpq-print.aspx?ItemID=185119
- SBV Circular 72/2025/TT-NHNN — accounts for FX activities in Vietnam International Financial Center: https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=185798

## Internal links

- [04 — Macro drivers, rates, carry and sessions](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [10 — Backtesting and point-in-time data](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [06 — Markets Korea/Vietnam](../../06_markets_korea_vietnam/README.md)
