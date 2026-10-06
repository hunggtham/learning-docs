# 증권투자기초 Book 1 — Source Coverage Matrix

Authority: `증권투자기초/raw_md/sach1.md`. Khi OCR không đủ để xác nhận bảng/công thức/đáp án, ảnh trong `증권투자기초/raw/sach1/` là nguồn đối chiếu. Matrix này được rebuild từ source; không kế thừa trạng thái `FULL` của matrix cũ.

## Audit contract

- Một row = một semantic unit độc lập hoặc một source question. Không gộp nhiều distinction chỉ để làm đẹp coverage.
- `FULL` nghĩa là output chứa đủ bản chất/cơ chế, input hoặc variable, điều kiện và boundary cần thiết cho unit đó.
- Rule có tính thời điểm chỉ được `FULL` về **textbook knowledge** khi lesson ghi rõ SOURCE/TEXTBOOK STATE; `FULL` không có nghĩa số liệu là luật 2026.
- `SOURCE_AMBIGUITY` chỉ dùng khi source + ảnh nguồn vẫn không giải được. Sau image verification của câu 50, Q60/Q61 và answer key chương 2, register hiện tại bằng 0.

## Summary

| Status | Count |
|---|---:|
| FULL | 339 |
| PARTIAL | 0 |
| MISSING | 0 |
| SOURCE_AMBIGUITY | 0 |
| **TOTAL** | **339** |

## Semantic inventory

| ID | Source location | Type | Semantic unit | Destination | Status | Evidence / audit note |
|---|---|---|---|---|---|---|
| C1S1-01 | Ch1 §1 pp.13–14 | DEFINITION | `금융시장`: nơi quyền đòi tiền/vốn được chuyển giữa bên dư vốn và thiếu vốn | 01 §1 | FULL | definition + economic purpose |
| C1S1-02 | Ch1 §1 pp.13–14 | MECHANISM | ba chức năng của financial market: transfer, price formation, risk/liquidity allocation | 01 §§1,6 | FULL | mechanism explained, not name-only |
| C1S1-03 | Ch1 §1 pp.14–15 | DISTINCTION | `직접금융` vs `간접금융` theo việc có trung gian đứng trên bảng cân đối hay không | 01 §§2,7 | FULL | boundary + examples |
| C1S1-04 | Ch1 §1 pp.14–15 | CLASSIFICATION | `단기금융시장` vs `자본시장` theo maturity/purpose | 01 §2 | FULL | boundary by maturity/use |
| C1S1-05 | Ch1 §1 p.15, Fig 1-1 | FIGURE | sơ đồ phân loại thị trường tài chính | 01 §§2–4 | FULL | redrawn as conceptual tree |
| C1S1-06 | Ch1 §1 pp.15–17, Table I-1 | TABLE | phân loại tổ chức tài chính theo chức năng | 01 §§4,10 | FULL | groups + examples + how to read |
| C1S1-07 | Ch1 §1 pp.16–18 | INSTITUTION | bank/deposit-taking institutions and balance-sheet intermediation | 01 §4 | FULL | role and funding relation |
| C1S1-08 | Ch1 §1 pp.16–18 | INSTITUTION | insurance, securities and other financial institutions | 01 §4 | FULL | role distinctions |
| C1S1-09 | Ch1 §1 pp.18–20 | RELATIONSHIP | financial market → securities market as subset, not synonym | 01 §§5–6 | FULL | scope relation |
| C1S2-01 | Ch1 §2 pp.20–21 | DEFINITION | `금융투자상품` and investment-risk property `투자성` | 02 §§1–2 | FULL | principal-loss boundary |
| C1S2-02 | Ch1 §2 pp.21–23, Table I-2 | TABLE | loss-to-principal ratio and classification of financial investment products | 02 §2 | FULL | inputs + boundary + product types |
| C1S2-03 | Ch1 §2 pp.21–23 | DISTINCTION | securities vs derivatives by maximum loss/liability relation | 02 §§2–3 | FULL | loss boundary explained |
| C1S2-04 | Ch1 §2 pp.22–24 | CLASSIFICATION | debt securities, equity securities, beneficiary certificates, investment-contract securities, derivatives-linked securities, depositary receipts | 02 §§2–3,7 | FULL | taxonomy kept |
| C1S2-05 | Ch1 §2 p.23 | DEFINITION | `투자계약증권`: return depends substantially on others' efforts | 02 §7 | FULL | legal/economic essence |
| C1S2-06 | Ch1 §2 p.24 | DEFINITION | `파생결합증권`: payoff linked to underlying/indicator | 02 §§3,8 | FULL | payoff mechanism |
| C1S2-07 | Ch1 §2 pp.25–26 | MECHANISM | securitization/denomination, marketability and risk-return trade-off | 02 §4 | FULL | why securities exist |
| C1S2-08 | Ch1 §2 pp.26–27 | CLASSIFICATION | common vs preferred shares | 02 §5 | FULL | rights and priority |
| C1S2-09 | Ch1 §2 p.27 | DISTINCTION | participating vs non-participating preferred shares | 02 §5 | FULL | extra-dividend condition |
| C1S2-10 | Ch1 §2 p.27 | DISTINCTION | cumulative vs non-cumulative preferred shares | 02 §5 | FULL | arrears condition |
| C1S2-11 | Ch1 §2 pp.27–28 | CLASSIFICATION | deferred/subordinated and mixed shares | 02 §5 | FULL | distribution priority |
| C1S2-12 | Ch1 §2 pp.28–29 | DISTINCTION | voting vs non-voting shares | 02 §5 | FULL | governance right |
| C1S2-13 | Ch1 §2 pp.29–30 | DISTINCTION | par-value vs no-par shares | 02 §5 | FULL | legal/accounting distinction |
| C1S2-14 | Ch1 §2 pp.30–34 | CLASSIFICATION | bond taxonomy by issuer, security, interest/payment and embedded rights | 02 §6 | FULL | cash-flow/right logic |
| C1S2-15 | Ch1 §2 pp.30–34 | MECHANISM | bond coupon/principal and creditor priority vs shareholder residual claim | 02 §6 | FULL | cash-flow mechanism |
| C1S3-01 | Ch1 §3 pp.34–35 | DEFINITION | broad vs narrow meaning of `증권시장` | 03 §1 | FULL | scope conditions |
| C1S3-02 | Ch1 §3 pp.35–36 | DISTINCTION | primary `발행시장` vs secondary `유통시장` | 03 §§2,4–5 | FULL | capital flow vs ownership transfer |
| C1S3-03 | Ch1 §3 pp.36–39 | MECHANISM | industrial-capital raising function | 03 §§3,7 | FULL | cause/effect |
| C1S3-04 | Ch1 §3 pp.36–39 | MECHANISM | initial ownership dispersion and public ownership | 03 §§3,7 | FULL | ownership mechanism |
| C1S3-05 | Ch1 §3 pp.36–39 | MECHANISM | price discovery and liquidity | 03 §§3,5,7 | FULL | market mechanism |
| C1S3-06 | Ch1 §3 pp.36–39 | MECHANISM | income/wealth redistribution and economic adjustment functions | 03 §§3,7 | FULL | boundary not guarantee |
| C1S3-07 | Ch1 §3 pp.36–39 | MECHANISM | policy transmission / fiscal-financial policy instrument role | 03 §§3,7 | FULL | system relation |
| C1S3-08 | Ch1 §3 pp.40–41 | INSTITUTION | issuer, investor and underwriter roles | 03 §4.1 | FULL | who bears what |
| C1S3-09 | Ch1 §3 pp.41–42 | PROCESS | lead manager / underwriting syndicate / subscription group flow | 03 §4.2 | FULL | role chain |
| C1S3-10 | Ch1 §3 pp.41–43 | LEGAL_RULE | public vs private offering threshold logic; source 50-person snapshot | 03 §4.3 | FULL | TEXTBOOK STATE |
| C1S3-11 | Ch1 §3 pp.42–44 | PROCESS | firm commitment `총액인수` | 03 §4.4 | FULL | underwriter takes inventory risk |
| C1S3-12 | Ch1 §3 pp.42–44 | PROCESS | standby/residual underwriting `잔액인수` | 03 §4.4 | FULL | residual risk allocation |
| C1S3-13 | Ch1 §3 pp.42–44 | PROCESS | best-efforts/placement `모집주선` | 03 §4.4 | FULL | no same inventory commitment |
| C1S3-14 | Ch1 §3 pp.45–47, Fig 1-2 | FIGURE | secondary-market structure linking investor, broker, KRX and KSD | 03 §§5–6; 04 §§2,6 | FULL | redrawn flow + role boundaries |
| C1S4-01 | Ch1 §4 pp.47–55 | INSTITUTION | financial policy/supervisory layer | 04 §1 | FULL | policy vs supervision |
| C1S4-02 | Ch1 §4 pp.47–55 | INSTITUTION | KOFIA role as association/SRO-support layer | 04 §§1–2 | FULL | role boundary |
| C1S4-03 | Ch1 §4 pp.47–55 | INSTITUTION | KRX role in listing, trading and market supervision | 04 §2 | FULL | venue/operator role |
| C1S4-04 | Ch1 §4 pp.47–55 | INSTITUTION | KSD role in depository/book-entry/settlement | 04 §2 | FULL | post-trade role |
| C1S4-05 | Ch1 §4 pp.47–55 | INSTITUTION | Koscom/market infrastructure role | 04 §2 | FULL | technical infrastructure |
| C1S4-06 | Ch1 §4 pp.54–56 | CLASSIFICATION | six financial-investment businesses | 04 §3 | FULL | dealer/broker/collective/trust/advice/discretion |
| C1S4-07 | Ch1 §4 pp.54–56 | DISTINCTION | investment dealing vs brokerage | 04 §§3,14 | FULL | principal vs agent |
| C1S4-08 | Ch1 §4 pp.54–56 | DISTINCTION | investment advisory vs discretionary management | 04 §§3,14 | FULL | advice vs delegated decision |
| C1S4-09 | Ch1 §4 pp.56–59 | LEGAL_RULE | authorization `인가` vs registration `등록` | 04 §§4,11 | FULL | risk-based entry regime |
| C1S4-10 | Ch1 §4 pp.56–59 | CONDITION | business unit combines business/product/investor scope | 04 §11 | FULL | unit logic |
| C1S4-11 | Ch1 §4 pp.57–59, Table I-3 | TABLE | registration business units and minimum capital snapshot | 04 §11 | FULL | TEXTBOOK STATE + how to read |
| C1S4-12 | Ch1 §4 pp.59–61 | PROCESS | payment/settlement-related business | 04 §§5,12 | FULL | role and conditions |
| C1S4-13 | Ch1 §4 pp.59–61, Table I-4 | TABLE | concurrent business scope | 04 §12 | FULL | conditions + boundaries |
| C1S4-14 | Ch1 §4 pp.59–61 | LEGAL_RULE | ancillary business and notice/limitation logic | 04 §§5,12 | FULL | TEXTBOOK STATE |
| C1S4-15 | Ch1 §4 pp.59–61 | RELATIONSHIP | principal/agent/client asset separation and conflicts | 04 §§6–8,14–15 | FULL | mechanism reconstructed |
| C1S5-01 | Ch1 §5 pp.61–63 | DEFINITION | IPO `기업공개` vs listing `상장` | 05 §§1,4 | FULL | distinct events |
| C1S5-02 | Ch1 §5 pp.61–63 | MECHANISM | IPO purposes: capital raising, ownership dispersion, credibility/governance and marketability | 05 §§1–2 | FULL | benefits + costs |
| C1S5-03 | Ch1 §5 p.63 | PROCESS | new-share offering `신주모집` | 05 §§3,9 | FULL | cash enters company |
| C1S5-04 | Ch1 §5 p.63 | PROCESS | secondary/old-share sale `구주매출` | 05 §§3,9 | FULL | cash goes to existing holder |
| C1S5-05 | Ch1 §5 p.63 | PROCESS | hybrid new + old-share offering | 05 §§3,9 | FULL | split cash-flow |
| C1S5-06 | Ch1 §5 p.63 | THRESHOLD | 25%/30% public-distribution ratios in source examples | 05 §§3,9 | FULL | SOURCE/TEXTBOOK STATE only |
| C1S5-07 | Ch1 §5 pp.63–66 | DISTINCTION | par-value issuance vs market-price issuance | 05 §5.2 | FULL | price basis |
| C1S5-08 | Ch1 §5 pp.64–67 | DEFINITION | capital increase `증자` and why share count can change | 05 §5 | FULL | capital/share relation |
| C1S5-09 | Ch1 §5 pp.64–67 | DISTINCTION | paid-in `유상증자` vs bonus `무상증자` | 05 §5 | FULL | new assets vs capitalization of reserves |
| C1S5-10 | Ch1 §5 pp.64–67 | CLASSIFICATION | shareholder allocation `주주배정` | 05 §5.1 | FULL | preemptive-right logic |
| C1S5-11 | Ch1 §5 pp.64–67 | CLASSIFICATION | third-party allocation `제3자배정` | 05 §5.1 | FULL | control/dilution implications |
| C1S5-12 | Ch1 §5 pp.64–67 | CLASSIFICATION | public-offering capital increase | 05 §5.1 | FULL | distribution mechanism |
| C1S5-13 | Ch1 §5 pp.64–67 | DISTINCTION | combined comprehensive vs parallel paid/bonus increase | 05 §5.1 | FULL | right-loss condition preserved |
| C1S5-14 | Ch1 review Q50 + images 221/231 | FORMULA | theoretical ex-right price uses issue price, not par value | 05 §§5.2,10 | FULL | image-confirmed; ambiguity resolved |
| C1S5-15 | Ch1 review Q50 + image 221 | VARIABLE | `P0` base price, `E` issue price, `r` paid-in increase ratio | 05 §10 | FULL | variables explicit |
| C1S5-16 | Ch1 review Q50 + image 221 | FORMULA | first issue price `P0(1-d)/(1+r d)` | 05 §§5.2,10 | FULL | image-confirmed TEXTBOOK STATE |
| C1S5-17 | Ch1 review Q50 + image 221 | FORMULA | second issue price `P_ref,2(1-d)` | 05 §§5.2,10 | FULL | image-confirmed TEXTBOOK STATE |
| C1S5-18 | Ch1 §5 pp.67–74 | DEFINITION | listing and listing types: new/new-share/change/relisting | 05 §6 | FULL | taxonomy |
| C1S5-19 | Ch1 §5 pp.67–74 | PROCESS | listing review flow from substantive review to approval/listing | 05 §7 | FULL | process reconstructed |
| C1S5-20 | Ch1 §5 pp.67–90 | REQUIREMENT | listing criteria grouped by liquidity/dispersion, business qualification, governance and investor protection | 05 §7 | FULL | numbers kept as snapshot |
| C1S5-21 | Ch1 §5 pp.67–90 | PROCESS | relisting after split/merger/restructuring | 05 §8 | FULL | distinct from new listing |
| C1S5-22 | Ch1 §5 pp.73–90 | LEGAL_RULE | trading suspension and delisting relation | 05 §8 | FULL | condition → action |
| C1S5-23 | Ch1 §5 pp.73–90 | EXCEPTION | final/cleanup trading before delisting in applicable cases | 05 §8 | FULL | boundary + time-sensitive warning |
| C1S5-24 | Ch1 §5/review pp.219–220 | TABLE | first price and ownership-dispersion/listing snapshot | 05 §13 | FULL | how to read result, not current rule |
| C1S5-25 | Ch1 §5 | WORKED_EXAMPLE | ex-right dilution example with correct issue-price variable | 05 §10.1 | FULL | mechanism + boundary |
| C1S6-01 | Ch1 §6 pp.90–96 | DEFINITION | organized secondary stock market and continuous trading | 06 §1 | FULL | market purpose |
| C1S6-02 | Ch1 §6 pp.90–96 | PROCESS | order → broker → venue → match → clearing → settlement | 06 §§2,20 | FULL | end-to-end lifecycle |
| C1S6-03 | Ch1 §6 pp.90–96 | MARKET_RULE | price priority `가격우선` | 06 §3 | FULL | order-book logic |
| C1S6-04 | Ch1 §6 pp.90–96 | MARKET_RULE | time priority `시간우선` | 06 §3 | FULL | tie-break condition |
| C1S6-05 | Ch1 review | MARKET_RULE | customer-order priority `위탁자매매우선` vs proprietary order | 06 §3; 90 traps | FULL | source-question distinction |
| C1S6-06 | Ch1 §6 pp.90–96 | DISTINCTION | single-price auction vs continuous/multiple-price matching | 06 §3 | FULL | when each mechanism applies |
| C1S6-07 | Ch1 §6 pp.96–97 | MARKET_RULE | price-limit mechanism | 06 §4 | FULL | purpose + boundary |
| C1S6-08 | Ch1 §6 pp.96–97 | MARKET_RULE | circuit breaker 3-stage historical mechanism | 06 §§4,7,14 | FULL | SOURCE/TEXTBOOK STATE |
| C1S6-09 | Ch1 §6 pp.96–100, Table I-7 | TABLE | regular/off-hours trading, price limits, CB and trading unit snapshot | 06 §14 | FULL | table reconstructed + warning |
| C1S6-10 | Ch1 §6 pp.97–100 | PROCESS | clearing vs settlement vs depository/book-entry | 06 §5 | FULL | distinct post-trade stages |
| C1S6-11 | Ch1 review Q41 | DISTINCTION | `차감결제`, `집중결제`, `대체결제` vs distractor `차금결제` | 06 §5 | FULL | question-specific gap closed |
| C1S6-12 | Ch1 review Q18 | DISTINCTION | credit financing `신용거래융자` vs stock loan `신용거래대주` | 06 §5 | FULL | money vs securities supplied |
| C1S6-13 | Ch1 review Q44 | DISTINCTION | securities lending `증권대차거래` and source transaction-type labels | 06 §5 | FULL | not ordinary sale / not same as credit stock loan |
| C1S6-14 | Ch1 §6 pp.101–106 | CLASSIFICATION | limit, market, conditional-limit, best-opposite and best-own-side orders | 06 §6 | FULL | execution trade-offs |
| C1S6-15 | Ch1 §6 pp.101–106 | CONDITION | IOC vs FOK | 06 §6 | FULL | partial vs all-or-none immediate execution |
| C1S6-16 | Ch1 §6 pp.101–106 | MARKET_RULE | after-hours closing-price and single-price trading | 06 §§6,14 | FULL | timing is textbook-state |
| C1S6-17 | Ch1 §6 pp.101–106 | MARKET_RULE | Sidecar trigger/pause mechanism | 06 §§7,14 | FULL | purpose + historical thresholds |
| C1S6-18 | Ch1 §6 pp.101–105 | LEGAL_RULE | management designation `관리종목` | 06 §§7,18 | FULL | warning state, not immediate delisting |
| C1S6-19 | Ch1 §6 pp.101–105 | PROCESS | cleanup trading `정리매매` and delisting sequence | 06 §18 | FULL | state transition |
| C1S6-20 | Ch1 §6 pp.98–100 | LEGAL_RULE | treasury-share separate account/disclosure/order constraints | 06 §17 | FULL | source table reconstructed |
| C1S6-21 | Ch1 §6 pp.98–100 | THRESHOLD | treasury-share timing/price/volume snapshot | 06 §17 | FULL | TEXTBOOK STATE |
| C1S6-22 | Ch1 §6 pp.116–121 | DEFINITION | periodic, timely, voluntary, inquiry and fair disclosure | 06 §9 | FULL | classification |
| C1S6-23 | Ch1 §6 pp.116–121 | REQUIREMENT | disclosure qualities: timeliness, accuracy, comprehensibility, fairness | 06 §9 | FULL | four criteria |
| C1S6-24 | Ch1 §6 pp.116–121 | LEGAL_RULE | unfaithful disclosure `불성실공시` | 06 §9 | FULL | conditions/consequences |
| C1S6-25 | Ch1 review Q60 + image 232 | PROCESS | KRX/SRO response to unfaithful disclosure vs accusation distractor | 06 §9 | FULL | answer-key verified |
| C1S6-26 | Ch1 §6 pp.122–140 | INSTITUTION | KOSDAQ purpose and governance/market-operation layers | 06 §10 | FULL | venue role |
| C1S6-27 | Ch1 §6 pp.122–140 | REQUIREMENT | KOSDAQ listing/maintenance criteria groups | 06 §11 | FULL | snapshot numbers not current |
| C1S6-28 | Ch1 §6 pp.134–145 | PROCESS | KOSDAQ management → recovery/suspension/delisting | 06 §11 | FULL | state flow |
| C1S6-29 | Ch1 §6 pp.145–153 | INSTITUTION | KONEX purpose for early-stage SMEs | 06 §12 | FULL | market role |
| C1S6-30 | Ch1 §6 pp.145–153 | INSTITUTION | designated adviser `지정자문인` | 06 §12 | FULL | ongoing support/screening role |
| C1S6-31 | Ch1 §6 pp.145–153 | CONDITION | KONEX investor/participation and lighter-entry safeguards | 06 §§12,19 | FULL | TEXTBOOK STATE |
| C1S6-32 | Ch1 §6 pp.153–163 | INSTITUTION | K-OTC registered vs designated companies | 06 §13 | FULL | two entry paths |
| C1S6-33 | Ch1 §6 pp.153–163 | MARKET_RULE | K-OTC negotiated/relative trading and liquidity/disclosure boundary | 06 §§13,15,19 | FULL | not same mechanism as KRX |
| C1S6-34 | Ch1 §6 pp.82–84 OCR / printed venue section | INSTITUTION | NXT as alternative trading venue alongside KRX | 06 §§13,15,19 | FULL | source-native, not external enrichment |
| C1S6-35 | Ch1 §6 pp.82–84 OCR | TABLE | NXT pre/main/after/closing/block-basket session snapshot | 06 §§13,15 | FULL | hours reconstructed; TEXTBOOK STATE |
| C1S6-36 | Ch1 §6 pp.82–84 OCR | MARKET_RULE | NXT KRX-close reference and venue-routing comparison | 06 §§13,15,19 | FULL | mechanism + boundary |
| C1S7-01 | Ch1 §7 pp.164–166 | DEFINITION | KOSPI200 as index underlying | 07 §1 | FULL | underlying vs traded claim |
| C1S7-02 | Ch1 §7 pp.166–170 | DEFINITION | stock-index futures contract | 07 §2 | FULL | obligation and cash settlement |
| C1S7-03 | Ch1 §7 pp.166–170 | VARIABLE | futures price, multiplier, contract value and tick | 07 §§2,7 | FULL | variables/units |
| C1S7-04 | Ch1 §7 pp.166–170 | MECHANISM | long vs short futures payoff | 07 §§2,7 | FULL | worked payoff logic |
| C1S7-05 | Ch1 §7 pp.166–170 | MECHANISM | margin and daily mark-to-market | 07 §§2,7 | FULL | cash-flow mechanism |
| C1S7-06 | Ch1 §7 pp.170–172 | DISTINCTION | calendar/inter-month spread trading | 07 §2 | FULL | relative-price exposure |
| C1S7-07 | Ch1 §7 pp.172–176 | DEFINITION | call vs put option rights and writer obligations | 07 §3 | FULL | asymmetric rights |
| C1S7-08 | Ch1 §7 pp.172–176 | VARIABLE | strike, premium, maturity and underlying | 07 §§3,7 | FULL | variables explicit |
| C1S7-09 | Ch1 §7 pp.172–176 | FORMULA | call/put intrinsic payoff and profit after premium | 07 §7 | FULL | formula + examples |
| C1S7-10 | Ch1 §7 pp.176–180 | DEFINITION | ELW/call-put warrant structure | 07 §4 | FULL | issuer/product distinction |
| C1S7-11 | Ch1 §7 pp.176–180 | FORMULA | ELW conversion ratio, parity/premium and break-even relations | 07 §§5,9 | FULL | interpretation + boundaries |
| C1S7-12 | Ch1 §7 pp.176–180 | METRIC | gearing/effective gearing intuition | 07 §§5,9 | FULL | not guaranteed return |
| C1S7-13 | Ch1 §7 pp.180–183 | CLASSIFICATION | single-stock futures/options | 07 §6 | FULL | underlying distinction |
| C1S7-14 | Ch1 §7 pp.164–183 | MECHANISM | hedging vs speculation vs arbitrage uses | 07 §8 | FULL | same instrument, different objective |
| C1S7-15 | Ch1 §7 pp.164–183 | EXCEPTION | leverage/margin/liquidity can make losses differ from cash equity | 07 §§7–10 | FULL | risk boundary |
| C1S8-01 | Ch1 §8 pp.184–186 | DEFINITION | dividend income `배당소득` | 08 §1 | FULL | income classification |
| C1S8-02 | Ch1 §8 pp.184–188 | DEFINITION | deemed dividend `의제배당` | 08 §§1,5 | FULL | economic transfer despite form |
| C1S8-03 | Ch1 §8 pp.184–188 | DISTINCTION | cash dividend vs capitalized reserve/profit and deemed-dividend possibility | 08 §5 | FULL | source/basis matter |
| C1S8-04 | Ch1 §8 pp.188–191 | PROCESS | gross-up/dividend tax-credit logic | 08 §2 | FULL | double-tax mechanism; historical rates caveated |
| C1S8-05 | Ch1 §8 pp.188–192 | CONDITION | income recognition timing by distribution/instrument/event | 08 §3 | FULL | date distinctions |
| C1S8-06 | Ch1 §8 pp.192–196 | DEFINITION | securities transaction tax `증권거래세` | 08 §4 | FULL | transfer-based, not profit-based |
| C1S8-07 | Ch1 §8 pp.192–196 | PROCESS | taxpayer/withholding actor differs by trading channel | 08 §4 | FULL | Q57 supported |
| C1S8-08 | Ch1 §8 pp.192–196 | VARIABLE | tax base from transfer value and applicable rate/venue | 08 §§4,11 | FULL | how to read |
| C1S8-09 | Ch1 §8 pp.192–196 | TABLE | historical market transaction-tax rates | 08 §11 | FULL | snapshot only |
| C1S8-10 | Ch1 §8 pp.196–198 | TAX_RULE | capital increase/bonus share tax distinctions | 08 §5 | FULL | source of capitalization matters |
| C1S8-11 | Ch1 review Q27 + answer key | FORMULA | unlisted share valuation weighting 1:1.5 in textbook answer | 08 §11.1 | FULL | TEXTBOOK STATE, not current tax rule |
| C1S8-12 | Ch1 §8 | DEFINITION | interest income `이자소득` kept distinct from dividend income | 08 §10 | FULL | source classification |
| C1S8-13 | Ch1 §8 | PROCESS | four-step tax reading: classify, time, base, liable actor | 08 §7 | FULL | learner replacement mechanism |
| C1S8-14 | Ch1 §8 | EXCEPTION | exemption/deduction/special-case boundaries must be checked by source/time | 08 §§2,6,9 | FULL | no silent 2026 claim |
| C1S9-01 | Ch1 §9 pp.198–200 | DEFINITION | M&A: acquisition vs merger | 09 §1 | FULL | control vs legal combination |
| C1S9-02 | Ch1 §9 pp.198–200 | CAUSE_EFFECT | M&A motives and synergy channels | 09 §§1,5 | FULL | benefit conditions + risks |
| C1S9-03 | Ch1 §9 pp.199–203 | CLASSIFICATION | friendly/hostile/neutral M&A | 09 §9 | FULL | management reaction axis |
| C1S9-04 | Ch1 §9 pp.199–203 | CLASSIFICATION | horizontal/vertical/diversifying M&A | 09 §§2,9 | FULL | industry relation axis |
| C1S9-05 | Ch1 §9 pp.199–203 | CLASSIFICATION | cash/share/mixed/LBO consideration | 09 §§2,6,9 | FULL | risk allocation |
| C1S9-06 | Ch1 §9 pp.199–203 | CLASSIFICATION | old-share/direct/secret/tender vs new-share/CB/BW acquisition | 09 §9 | FULL | transaction form axis |
| C1S9-07 | Ch1 §9 pp.199–203 | CLASSIFICATION | new-company merger/absorption/two-step merger and asset/business acquisition | 09 §9 | FULL | legal-form axis |
| C1S9-08 | Ch1 §9 pp.199–205 | PROCESS | LBO finances acquisition using target assets/cash flow | 09 §§6,12 | FULL | leverage mechanism |
| C1S9-09 | Ch1 §9 pp.199–205 | LEGAL_RULE | tender offer `공개매수` purpose/process | 09 §§3.1,10 | FULL | TEXTBOOK thresholds labeled |
| C1S9-10 | Ch1 §9 pp.199–205 | LEGAL_RULE | large-shareholding report `대량보유상황보고` | 09 §§3.2,10 | FULL | 5%/1%/5-day source snapshot |
| C1S9-11 | Ch1 §9 pp.199–205 | LEGAL_RULE | treasury-share acquisition/disposal in control context | 09 §§3.3,10 | FULL | governance effect |
| C1S9-12 | Ch1 §9 pp.199–205 | LEGAL_RULE | proxy solicitation `의결권대리행사권유` | 09 §§3.4,10 | FULL | shareholder voting mechanism |
| C1S9-13 | Ch1 review Q61 + image 232 | DISTINCTION | mandatory proxy-form contents vs solicitor's purpose distractor | 09 §3.4 | FULL | answer-key verified |
| C1S9-14 | Ch1 §9 pp.198–205 | PROCESS | M&A analysis chain: target/right acquired → consideration → financing → stakeholder rights → integration | 09 §§4,7–8 | FULL | reconstruction-ready |
| C2S1-01 | Ch2 §1 pp.234–238 | DEFINITION | collective investment `집합투자` | 10 §§1,9 | FULL | pooling + no daily directions |
| C2S1-02 | Ch2 §1 pp.234–238 | CONDITION | funds collected from multiple investors and managed collectively | 10 §§1,9 | FULL | statutory boundary |
| C2S1-03 | Ch2 §1 pp.234–238 | CONDITION | manager acts without day-to-day instructions from each investor | 10 §§1,9 | FULL | Q16 supported |
| C2S1-04 | Ch2 §1 pp.234–238 | MECHANISM | diversification/economies of scale/professional management | 10 §§2–5 | FULL | benefit mechanism |
| C2S1-05 | Ch2 §1 pp.238–242 | CLASSIFICATION | public vs private collective-investment vehicle | 10 §§6,9; 11 §3 | FULL | threshold is textbook-state |
| C2S1-06 | Ch2 §1 pp.239–242 | CLASSIFICATION | legal-form family of collective-investment vehicles | 10 §9; 11 §1 | FULL | forms and boundaries |
| C2S1-07 | Ch2 §1 pp.239–242 | EXCEPTION | not every collective vehicle may invest in every asset | 10 §9; 12 §1 | FULL | policy/legal limits |
| C2S2-01 | Ch2 §2 pp.242–247 | CLASSIFICATION | investment trust vs investment company and other legal forms | 11 §1 | FULL | who owns/contractual structure |
| C2S2-02 | Ch2 §2 pp.242–247 | INSTITUTION | asset manager `집합투자업자` | 11 §2 | FULL | investment decision role |
| C2S2-03 | Ch2 §2 pp.242–247 | INSTITUTION | trustee/custodian `신탁업자` | 11 §2 | FULL | asset custody + instruction check |
| C2S2-04 | Ch2 §2 pp.242–247 | INSTITUTION | sales company/distributor | 11 §2 | FULL | subscription/redemption channel |
| C2S2-05 | Ch2 §2 pp.242–247 | INSTITUTION | general administration/valuation/fund-evaluation roles | 11 §2 | FULL | support roles |
| C2S2-06 | Ch2 §2 pp.242–247 | LEGAL_RULE | duty of care and loyalty | 11 §2 | FULL | manager/trustee obligations |
| C2S2-07 | Ch2 §2 pp.248–250 | DEFINITION | NAV/base price `기준가격` | 11 §5 | FULL | economic meaning |
| C2S2-08 | Ch2 §2 pp.248–250 | FORMULA | base price from net assets / total units, normalized per 1,000/5,000 | 11 §5 | FULL | variables + units |
| C2S2-09 | Ch2 §2 pp.248–250 | WORKED_EXAMPLE | monthly contributions buy different units as base price changes | 11 §5 | FULL | unit calculation |
| C2S2-10 | Ch2 §2 pp.248–250 | FORMULA | return from change in base price | 11 §5 | FULL | worked interpretation |
| C2S2-11 | Ch2 §2 pp.249–250 | DISTINCTION | one-time sales charge `수수료` vs recurring remuneration `보수` | 11 §§6,9 | FULL | cost timing |
| C2S2-12 | Ch2 §2 pp.249–250 | CLASSIFICATION | front-end/back-end/redemption fee | 11 §§6,9 | FULL | who receives / when |
| C2S2-13 | Ch2 §2 pp.249–250 | MECHANISM | redemption fee flows back to fund in source rationale | 11 §6 | FULL | protect remaining investors |
| C2S2-14 | Ch2 §2 pp.249–250 | METRIC | TER/total expense concept | 11 §§6,9 | FULL | ongoing cost effect |
| C2S2-15 | Ch2 §2 pp.250–253 | LEGAL_RULE | suitability `적합성` | 11 §8 | FULL | recommendation context |
| C2S2-16 | Ch2 §2 pp.250–253 | LEGAL_RULE | appropriateness `적정성` | 11 §8 | FULL | non-recommended/high-risk sales context |
| C2S2-17 | Ch2 §2 pp.250–253 | LEGAL_RULE | duty to explain and ban on improper solicitation | 11 §8 | FULL | investor-protection chain |
| C2S2-18 | Ch2 §2 pp.255–256 | DISTINCTION | backward pricing vs forward pricing | 11 §§4,10 | FULL | arbitrage/dilution rationale |
| C2S2-19 | Ch2 §2 pp.255–257, Table II-3 | TABLE | subscription request time → base-price date | 11 §§10,13 | FULL | timing reconstructed; textbook-state |
| C2S2-20 | Ch2 §2 pp.257–262 | DEFINITION | redemption `환매` and future-price principle | 11 §§4,10,12 | FULL | mechanism |
| C2S2-21 | Ch2 §2 pp.257–262, Table II-4 | TABLE | redemption request → pricing/payment dates by fund/cutoff | 11 §§10,13 | FULL | conditions + exceptions |
| C2S2-22 | Ch2 §2 pp.257–262 | EXCEPTION | MMF limited same-day redemption in source conditions | 11 §§10,12 | FULL | textbook-state |
| C2S2-23 | Ch2 §2 pp.257–262 | EXCEPTION | illiquid/foreign-asset funds may set longer redemption period | 11 §12 | FULL | 10%/50% snapshot caveated |
| C2S2-24 | Ch2 §2 pp.257–262 | PROCESS | redemption suspension/deferral when valuation/liquidity/fairness fails | 11 §12 | FULL | conditions + investor fairness |
| C2S2-25 | Ch2 §2 pp.260–263 | DISTINCTION | open vs closed fund | 11 §4 | FULL | redemption availability |
| C2S2-26 | Ch2 §2 pp.260–263 | DISTINCTION | additional-unit/open-ended issuance vs unit/fixed issue | 11 §4 | FULL | new subscriptions |
| C2S2-27 | Ch2 §2 pp.249–263, Table classes | TABLE | fee/class comparison and holding-period effect | 11 §9 | FULL | cost reading |
| C2S3-01 | Ch2 §3 pp.263–268 | CLASSIFICATION | security fund by dominant asset: equity/bond/mixed/MMF | 12 §§1–5 | FULL | asset-driven taxonomy |
| C2S3-02 | Ch2 §3 pp.263–268 | CONDITION | equity/bond allocation thresholds in source classification | 12 §§2–5,14 | FULL | TEXTBOOK STATE |
| C2S3-03 | Ch2 §3 pp.263–268 | MECHANISM | interest-rate sensitivity of bond funds | 12 §§3,13 | FULL | Q8/Q24 support |
| C2S3-04 | Ch2 §3 pp.263–268 | MECHANISM | MMF short-maturity/liquidity objective | 12 §5 | FULL | risk boundary |
| C2S3-05 | Ch2 §3 pp.268–283 | CLASSIFICATION | real-estate fund subtypes | 12 §7 | FULL | rental/development/auction/loan etc |
| C2S3-06 | Ch2 §3 p.282+, Fig II-8 | FIGURE | rental real-estate fund cash-flow structure | 12 §§7,15 | FULL | flow reconstructed |
| C2S3-07 | Ch2 §3 pp.283–288 | CLASSIFICATION | REIT structures/types | 12 §7 | FULL | company/management relation |
| C2S3-08 | Ch2 §3, Fig II-9 | FIGURE | REIT business structure | 12 §§7,15 | FULL | roles/cash flows |
| C2S3-09 | Ch2 §3 pp.288–291 | CLASSIFICATION | special-asset funds including ship/commodity/etc. | 12 §8 | FULL | asset-right taxonomy |
| C2S3-10 | Ch2 §3, Fig II-10 ship | FIGURE | ship-fund operating structure | 12 §§8,15 | FULL | flow reconstructed |
| C2S3-11 | Ch2 §3 pp.291–293 | CLASSIFICATION | mixed-asset fund | 12 §9 | FULL | no single dominant asset class |
| C2S3-12 | Ch2 §3 pp.291–293 | CLASSIFICATION | derivatives fund | 12 §9 | FULL | derivative exposure threshold logic |
| C2S3-13 | Ch2 §3 pp.293–294, Table II-10 | TABLE | fund classification by investment target | 12 §14 | FULL | cross-asset comparison |
| C2S3-14 | Ch2 §3 pp.294–296 | DEFINITION | fund of funds `재간접펀드` | 12 §10 | FULL | two-layer structure |
| C2S3-15 | Ch2 §3 pp.294–296 | THRESHOLD | same-manager funds ≤50% source snapshot | 12 §10 | FULL | exceptions noted |
| C2S3-16 | Ch2 §3 pp.294–296 | THRESHOLD | same underlying fund ≤20% source snapshot | 12 §10 | FULL | ETF exceptions noted |
| C2S3-17 | Ch2 §3 pp.294–296 | LEGAL_RULE | FoF cannot invest in another FoF in source rule | 12 §10 | FULL | layering boundary |
| C2S3-18 | Ch2 §3 pp.294–296 | THRESHOLD | private-fund exposure ≤5% source snapshot | 12 §10 | FULL | TEXTBOOK STATE |
| C2S3-19 | Ch2 §3 pp.294–296 | LEGAL_RULE | two-layer sales-fee/remuneration cap rationale | 12 §10 | FULL | double-fee protection |
| C2S3-20 | Ch2 §3 pp.295–297 | DEFINITION | master-feeder `모자펀드` | 12 §10 | FULL | same manager, pooled mother fund |
| C2S3-21 | Ch2 §3 pp.296–298, Table II-11 | TABLE | fund share classes and fee/channel differences | 12 §10; 11 §9 | FULL | A/S source distinction explicit |
| C2S3-22 | Ch2 review Q11 | DISTINCTION | Class A upfront sales charge vs Class S fund-supermarket channel | 12 §10; 90 | FULL | source answer preserved |
| C2S3-23 | Ch2 §3 pp.297–299 | DEFINITION | umbrella/conversion fund | 12 §10 | FULL | switching structure |
| C2S3-24 | Ch2 §3 pp.297–299 | DEFINITION | wrap account relation | 12 §10 | FULL | account vs pooled fund boundary |
| C2S3-25 | Ch2 §3 pp.299–304 | DISTINCTION | active vs passive/index funds | 12 §11 | FULL | selection vs tracking |
| C2S3-26 | Ch2 §3 pp.299–304 | DEFINITION | ETF structure and benchmark tracking | 12 §11 | FULL | tradability + NAV relation |
| C2S3-27 | Ch2 §3 pp.299–304 | METRIC | tracking error `추적오차` | 12 §11; 13 §9 | FULL | lower means closer tracking, not return guarantee |
| C2S3-28 | Ch2 §3 pp.299–304 | DEFINITION | inverse/leveraged ETF | 12 §11 | FULL | daily-target/rebalancing risk |
| C2S3-29 | Ch2 §3 pp.304–309 | CLASSIFICATION | regional/country/sector/style/dividend/value/growth/target-date funds | 12 §§12–13 | FULL | strategy distinctions |
| C2S3-30 | Ch2 §3 pp.304–309 | MECHANISM | target-date glide path reduces equity, raises safer assets over time | 12 §13 | FULL | Q9 support |
| C2S3-31 | Ch2 §3 pp.309–313 | CLASSIFICATION | infrastructure/private equity/hedge and alternative funds | 12 §13 | FULL | strategy/illiquidity distinctions |
| C2S3-32 | Ch2 §3 p.313, Table I-15 | TABLE | KOSDAQ venture fund 15%/35% investment requirements and timing | 12 §14 | FULL | TEXTBOOK STATE |
| C2S3-33 | Ch2 §3 | EXCEPTION | fund names do not prove actual portfolio/style | 12 §13; 13 §13 | FULL | must inspect holdings/prospectus |
| C2S4-01 | Ch2 §4 pp.314–319 | PROCESS | investment-profile assessment combines goal, horizon, income/assets/debt and loss capacity | 13 §§1–2 | FULL | not score-only |
| C2S4-02 | Ch2 §4 pp.314–319 | CLASSIFICATION | five source risk profiles | 13 §8 | FULL | names + interpretation |
| C2S4-03 | Ch2 §4 pp.314–319 | EXCEPTION | source may use 3/4/5/7 profile levels | 13 §8 | FULL | Q13 support |
| C2S4-04 | Ch2 §4 p.319, Table II-16 | TABLE | investment horizon × risk-profile classification | 13 §14 | FULL | matrix reconstructed |
| C2S4-05 | Ch2 §4 p.319, Table II-17 | TABLE | investor type × detailed asset allocation example | 13 §14 | FULL | allocation logic, not advice |
| C2S4-06 | Ch2 §4 pp.320–321, Table II-18 | TABLE | prospectus contents | 13 §§3,12 | FULL | fields grouped by decision use |
| C2S4-07 | Ch2 §4 p.321, Table II-19 | TABLE | simplified prospectus contents | 13 §§3,12 | FULL | screening vs full prospectus |
| C2S4-08 | Ch2 §4 pp.321–322, Table II-20 | TABLE | asset-management report standard fields | 13 §§3,12,15 | FULL | what actual operation shows |
| C2S4-09 | Ch2 §4 pp.323–326, Fig investment process | FIGURE | fund investment process: classify → return/risk → rank → qualitative review → periodic evaluation | 13 §§4–5,11 | FULL | process reconstructed |
| C2S4-10 | Ch2 §4 pp.323–326 | METRIC | fund-level return `펀드별 수익률` | 13 §4 | FULL | base-price return |
| C2S4-11 | Ch2 §4 pp.323–326 | METRIC | manager-average return `운용사별 평균수익률` | 13 §4 | FULL | manager comparison, not risk metric |
| C2S4-12 | Ch2 §4 pp.323–326 | METRIC | category return `유형수익률` | 13 §4 | FULL | peer-group aggregate |
| C2S4-13 | Ch2 §4 pp.326–327 | METRIC | standard deviation as dispersion/risk signal | 13 §9 | FULL | interpretation |
| C2S4-14 | Ch2 §4 pp.326–327 | FORMULA | beta from covariance/benchmark variance | 13 §9 | FULL | variables + beta=1 boundary |
| C2S4-15 | Ch2 §4 pp.326–327 | METRIC | benchmark/category excess return | 13 §§4,9 | FULL | relative performance |
| C2S4-16 | Ch2 §4 pp.326–327 | METRIC | ranking persistence as stability signal | 13 §§4,9 | FULL | Q29 context |
| C2S4-17 | Ch2 §4 pp.326–327 | FORMULA | Sharpe ratio `(Rp-Rf)/σp` | 13 §§4,9 | FULL | variables + worked Q30 |
| C2S4-18 | Ch2 review Q30 | WORKED_EXAMPLE | 10%, 3%, 14% → Sharpe 0.50 | 13 §9; 90 | FULL | calculation explicit |
| C2S4-19 | Ch2 §4 pp.327–333 | PROCESS | periodic review and rebalancing by goals/weights/quality | 13 §5 | FULL | decision loop |
| C2S4-20 | Ch2 §4 pp.327–333 | PROCESS | fund transfer/switching conditions and product exceptions | 13 §5 | FULL | product rule caveat |
| C2S4-21 | Ch2 §4 pp.333–334 | TAX_RULE | 15.4% financial-income rate in source snapshot | 13 §6 | FULL | TEXTBOOK STATE only |
| C2S4-22 | Ch2 §4 pp.333–334 | DISTINCTION | bond-fund taxable gains vs equity-fund separate tax-base price logic | 13 §6 | FULL | source tax distinction |
| C2S4-23 | Ch2 review Q15 | DISTINCTION | NAV loss can coexist with tax under `과표기준가격` in source logic | 13 §6; 90 | FULL | question supported |
| C2S4-24 | Ch2 §4 | PROCESS | document → actual holdings → performance/risk → costs/turnover/personnel review chain | 13 §§12–15 | FULL | learner replacement |
| Q1-01 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 1 | book1/02 | FULL | source answer O; concept available without returning to raw |
| Q1-02 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 2 | book1/02 | FULL | source answer O; concept available without returning to raw |
| Q1-03 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 3 | book1/02 | FULL | source answer X; concept available without returning to raw |
| Q1-04 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 4 | book1/02 | FULL | source answer O; concept available without returning to raw |
| Q1-05 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 5 | book1/02 | FULL | source answer O; concept available without returning to raw |
| Q1-06 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 6 | book1/04 | FULL | source answer O; concept available without returning to raw |
| Q1-07 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 7 | book1/04 | FULL | source answer O; concept available without returning to raw |
| Q1-08 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 8 | book1/02/04 | FULL | source answer O; concept available without returning to raw |
| Q1-09 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 9 | book1/05 | FULL | source answer X; concept available without returning to raw |
| Q1-10 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 10 | book1/02/08 | FULL | source answer X; concept available without returning to raw |
| Q1-11 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 11 | book1/04 | FULL | source answer X; concept available without returning to raw |
| Q1-12 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 12 | book1/05 | FULL | source answer X; concept available without returning to raw |
| Q1-13 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 13 | book1/05 | FULL | source answer X; concept available without returning to raw |
| Q1-14 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 14 | book1/03 | FULL | source answer O; concept available without returning to raw |
| Q1-15 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 15 | book1/05 | FULL | source answer O; concept available without returning to raw |
| Q1-16 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 16 | book1/06 | FULL | source answer O; concept available without returning to raw |
| Q1-17 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 17 | book1/06 | FULL | source answer X; concept available without returning to raw |
| Q1-18 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 18 | book1/06 | FULL | source answer O; concept available without returning to raw |
| Q1-19 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 19 | book1/06 | FULL | source answer O; concept available without returning to raw |
| Q1-20 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 20 | book1/06 | FULL | source answer X; concept available without returning to raw |
| Q1-21 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 21 | book1/06 | FULL | source answer O; concept available without returning to raw |
| Q1-22 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 22 | book1/06 | FULL | source answer O; concept available without returning to raw |
| Q1-23 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 23 | book1/09 | FULL | source answer O; concept available without returning to raw |
| Q1-24 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 24 | book1/06 | FULL | source answer X; concept available without returning to raw |
| Q1-25 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 25 | book1/08 | FULL | source answer X; concept available without returning to raw |
| Q1-26 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 26 | book1/09 | FULL | source answer X; concept available without returning to raw |
| Q1-27 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 27 | book1/08 | FULL | source answer X; concept available without returning to raw |
| Q1-28 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 28 | book1/06 | FULL | source answer O; concept available without returning to raw |
| Q1-29 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 29 | book1/08 | FULL | source answer X; concept available without returning to raw |
| Q1-30 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 30 | book1/08 | FULL | source answer O; concept available without returning to raw |
| Q1-31 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 31 | book1/02 | FULL | source answer ④; concept available without returning to raw |
| Q1-32 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 32 | book1/02 | FULL | source answer ③; concept available without returning to raw |
| Q1-33 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 33 | book1/03 | FULL | source answer ③; concept available without returning to raw |
| Q1-34 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 34 | book1/05 | FULL | source answer ②; concept available without returning to raw |
| Q1-35 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 35 | book1/06 | FULL | source answer ③; concept available without returning to raw |
| Q1-36 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 36 | book1/05 | FULL | source answer ③; concept available without returning to raw |
| Q1-37 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 37 | book1/05 | FULL | source answer ③; concept available without returning to raw |
| Q1-38 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 38 | book1/02 | FULL | source answer ③; concept available without returning to raw |
| Q1-39 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 39 | book1/06 | FULL | source answer ①; concept available without returning to raw |
| Q1-40 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 40 | book1/09 | FULL | source answer ①; concept available without returning to raw |
| Q1-41 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 41 | book1/06 | FULL | source answer ④; concept available without returning to raw |
| Q1-42 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 42 | book1/06 | FULL | source answer ③; concept available without returning to raw |
| Q1-43 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 43 | book1/04 | FULL | source answer ③; concept available without returning to raw |
| Q1-44 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 44 | book1/06 | FULL | source answer ③; concept available without returning to raw |
| Q1-45 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 45 | book1/09 | FULL | source answer ②; concept available without returning to raw |
| Q1-46 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 46 | book1/09 | FULL | source answer ④; concept available without returning to raw |
| Q1-47 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 47 | book1/04/06 | FULL | source answer ④; concept available without returning to raw |
| Q1-48 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 48 | book1/05 | FULL | source answer ④; concept available without returning to raw |
| Q1-49 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 49 | book1/05 | FULL | source answer ②; concept available without returning to raw |
| Q1-50 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 50 | book1/05 | FULL | source answer ①; concept available without returning to raw |
| Q1-51 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 51 | book1/06 | FULL | source answer ①; concept available without returning to raw |
| Q1-52 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 52 | book1/06 | FULL | source answer ④; concept available without returning to raw |
| Q1-53 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 53 | book1/06 | FULL | source answer ②; concept available without returning to raw |
| Q1-54 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 54 | book1/06 | FULL | source answer ①; concept available without returning to raw |
| Q1-55 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 55 | book1/06 | FULL | source answer ②; concept available without returning to raw |
| Q1-56 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 56 | book1/06 | FULL | source answer ②; concept available without returning to raw |
| Q1-57 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 57 | book1/08 | FULL | source answer ④; concept available without returning to raw |
| Q1-58 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 58 | book1/09 | FULL | source answer ④; concept available without returning to raw |
| Q1-59 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 59 | book1/09 | FULL | source answer ①; concept available without returning to raw |
| Q1-60 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 60 | book1/06 | FULL | source answer ④; concept available without returning to raw |
| Q1-61 | Ch1 review pp.211–231 / images 212–232 | REVIEW_QUESTION | Chapter 1 source question 61 | book1/09 | FULL | source answer ④; concept available without returning to raw |
| Q2-01 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 1 | book1/11 | FULL | source answer O; reasoning mapped in lesson/90 |
| Q2-02 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 2 | book1/10/12 | FULL | source answer X; reasoning mapped in lesson/90 |
| Q2-03 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 3 | book1/11 | FULL | source answer X; reasoning mapped in lesson/90 |
| Q2-04 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 4 | book1/11 | FULL | source answer O; reasoning mapped in lesson/90 |
| Q2-05 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 5 | book1/12 | FULL | source answer X; reasoning mapped in lesson/90 |
| Q2-06 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 6 | book1/12 | FULL | source answer O; reasoning mapped in lesson/90 |
| Q2-07 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 7 | book1/12 | FULL | source answer O; reasoning mapped in lesson/90 |
| Q2-08 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 8 | book1/12/13 | FULL | source answer X; reasoning mapped in lesson/90 |
| Q2-09 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 9 | book1/12/13 | FULL | source answer O; reasoning mapped in lesson/90 |
| Q2-10 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 10 | book1/12 | FULL | source answer X; reasoning mapped in lesson/90 |
| Q2-11 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 11 | book1/12/11 | FULL | source answer X; reasoning mapped in lesson/90 |
| Q2-12 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 12 | book1/12/13 | FULL | source answer O; reasoning mapped in lesson/90 |
| Q2-13 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 13 | book1/13 | FULL | source answer X; reasoning mapped in lesson/90 |
| Q2-14 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 14 | book1/13 | FULL | source answer O; reasoning mapped in lesson/90 |
| Q2-15 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 15 | book1/08/13 | FULL | source answer O; reasoning mapped in lesson/90 |
| Q2-16 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 16 | book1/10 | FULL | source answer ③; reasoning mapped in lesson/90 |
| Q2-17 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 17 | book1/11 | FULL | source answer ②; reasoning mapped in lesson/90 |
| Q2-18 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 18 | book1/11 | FULL | source answer ④; reasoning mapped in lesson/90 |
| Q2-19 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 19 | book1/11 | FULL | source answer ①; reasoning mapped in lesson/90 |
| Q2-20 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 20 | book1/11 | FULL | source answer ②; reasoning mapped in lesson/90 |
| Q2-21 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 21 | book1/11 | FULL | source answer ③; reasoning mapped in lesson/90 |
| Q2-22 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 22 | book1/11 | FULL | source answer ③; reasoning mapped in lesson/90 |
| Q2-23 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 23 | book1/12 | FULL | source answer ①; reasoning mapped in lesson/90 |
| Q2-24 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 24 | book1/12 | FULL | source answer ③; reasoning mapped in lesson/90 |
| Q2-25 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 25 | book1/12 | FULL | source answer ④; reasoning mapped in lesson/90 |
| Q2-26 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 26 | book1/12 | FULL | source answer ②; reasoning mapped in lesson/90 |
| Q2-27 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 27 | book1/12 | FULL | source answer ④; reasoning mapped in lesson/90 |
| Q2-28 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 28 | book1/12 | FULL | source answer ③; reasoning mapped in lesson/90 |
| Q2-29 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 29 | book1/13 | FULL | source answer ①; reasoning mapped in lesson/90 |
| Q2-30 | Ch2 review pp.341–351 / images 342–352 | REVIEW_QUESTION | Chapter 2 source question 30 | book1/13 | FULL | source answer ②; reasoning mapped in lesson/90 |

## Coverage rows split in this audit

Các row cũ gộp quá rộng đã được tách thành unit độc lập, đặc biệt: IPO (`신주모집`/`구주매출`/hybrid), từng dạng `증자`, từng formula/variable của rights issue, listing process/requirements/suspension/delisting; từng trading priority/order/settlement/credit/lending rule; KOSDAQ/KONEX/K-OTC/NXT thành venue + condition + table riêng; futures/options/ELW thành payoff/variable/metric; securities tax thành income/timing/base/taxpayer/exception; M&A thành taxonomy/tender/5%-report/treasury/proxy; fund pricing/redemption thành backward-forward/timing/payment/exception; fund classification thành từng structure/limit; fund taxation thành tax-rate snapshot/tax-base-price distinction.

## SOURCE_AMBIGUITY register

**Không còn open item.** OCR-fragile content vẫn được ghi provenance, nhưng không dùng nhãn ambiguity khi ảnh source giải được:

- Q50: `raw/sach1/221.jpg` + answer `231.jpg` xác nhận `발행가액`, không phải `액면가액`; first-issue denominator được phục hồi.
- Ch1 Q60–61: question page `224.jpg` và answer `232.jpg` xác nhận disclosure/proxy distinctions.
- Ch2 Q29–30: answer images `351.jpg`–`352.jpg` xác nhận Q29 = ① và Sharpe Q30 = 0.50.

## Time-state boundary

Coverage của các ngưỡng/giờ/tax/product rules là coverage của **SOURCE / TEXTBOOK STATE**. Matrix này không gắn `CURRENT VERIFIED STATE` cho một số liệu nào nếu lesson không có official source + snapshot date. Vì task này không cần một current-law compendium, các rule thời điểm được bảo tồn để học/reconstruct source nhưng không bị biến thành quy định 2026.
