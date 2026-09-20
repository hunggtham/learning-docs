# Corporate Actions, M&A, Merger, Spin-off và Capital Actions tại doanh nghiệp Hàn Quốc (기업행위·M&A·합병·분할)

Khi đọc một company, rất nhiều thay đổi lớn không xuất hiện từ hoạt động kinh doanh thường ngày mà từ **corporate actions / 기업행위**: merger, acquisition, spin-off, split-off, rights issue, treasury-share transaction, tender offer, asset sale, share swap hoặc restructuring. Những event này có thể thay đổi ownership, earnings perimeter, debt, share count và value distribution giữa các stakeholder chỉ trong một thời gian ngắn.

Vì vậy analyst không thể chỉ đọc revenue và operating profit. Phải hiểu **transaction mechanics** và hỏi: ai đưa tài sản gì vào deal, ai nhận claim gì sau deal, tỷ lệ ownership thay đổi ra sao và value được chuyển giữa các entity như thế nào.

## 1. Corporate action là gì?

Corporate action là quyết định của company làm thay đổi capital structure, ownership, legal perimeter hoặc rights của security holders.

Một mental model:

```text
Before transaction
Assets + liabilities + shareholders
        ↓
Legal / financial action
        ↓
After transaction
New perimeter + new claims + new control structure
```

Điểm khó là accounting result, legal form và economic substance có thể khác nhau. Một transaction được gọi là “merger” chưa chắc economic logic giống acquisition. Một spin-off có thể unlock focus nhưng cũng có thể chuyển asset quality giữa entities.

## 2. M&A: tại sao công ty mua công ty khác?

**Merger & Acquisition / M&A / 인수합병** thường được biện minh bằng growth, synergy, technology, customer access, vertical integration, geographic expansion hoặc restructuring.

Nhưng “synergy” chỉ meaningful nếu map được thành cash flow.

Ví dụ:

```text
Revenue synergy
→ cross-sell / distribution / pricing
→ higher revenue

Cost synergy
→ procurement / headcount / duplicated systems
→ lower cost

Capital synergy
→ better working capital / funding / tax structure
→ lower capital need or funding cost
```

Nếu không convert được synergy thành measurable mechanism, nó vẫn chỉ là narrative.

## 3. Acquisition price và premium

Acquirer thường phải trả premium so với unaffected market price để target shareholders chấp nhận.

Câu hỏi quan trọng:

\[
Value\ Created = Synergy - Premium - Integration\ Cost - Financing\ Cost
\]

Acquisition có thể giúp combined company lớn hơn nhưng vẫn destroy shareholder value nếu premium quá cao.

Growth không đồng nghĩa value creation.

## 4. Purchase price allocation và goodwill

Sau acquisition, accounting phải allocate purchase price vào identifiable assets/liabilities và phần residual thường thành **goodwill / 영업권**.

Simplified:

\[
Goodwill = Purchase\ Consideration - Fair\ Value\ of\ Net\ Identifiable\ Assets
\]

Goodwill lớn không tự động xấu. Nó có thể phản ánh brand, network, human capital hoặc expected synergy không thể recognize riêng. Nhưng goodwill cao làm analyst cần hỏi acquirer có overpay không và impairment risk thế nào.

## 5. Goodwill impairment

Nếu acquired business underperform, goodwill có thể bị impairment. Đây là non-cash charge tại thời điểm recognition nhưng phản ánh prior capital allocation đã thất bại hoặc assumptions suy yếu.

Do đó khi thấy impairment, không nên dừng ở “one-off”. Hãy quay lại hỏi:

- acquisition price ban đầu;
- thesis lúc mua;
- performance thực tế;
- management accountability.

## 6. Accretion/dilution

Management đôi khi nói deal **EPS accretive**. Nhưng EPS accretion không đồng nghĩa deal tạo value.

Một acquirer với high P/E có thể issue expensive-valued stock để mua low-P/E target và làm EPS tăng mechanically dù strategic value không lớn.

Value creation phải xem ROIC trên capital bỏ ra so với cost of capital, không chỉ EPS.

## 7. Financing an acquisition

Acquisition có thể dùng cash, debt, new shares hoặc combination.

Cash-funded deal giảm liquidity. Debt-funded deal tăng leverage và interest burden. Share-funded deal dilute shareholders nhưng giảm refinancing risk.

Câu hỏi đúng là:

> Financing structure có match cash-flow visibility và risk của acquired asset không?

## 8. Merger (합병)

Trong **merger / 합병**, legal entities được combine theo structure cụ thể. Shareholders của entity bị merged có thể nhận shares của surviving/new entity theo **merger ratio / 합병비율**.

Merger ratio là điểm rất nhạy vì nó quyết định economic ownership sau transaction.

Nếu relative valuation giữa entities không fair, value có thể transfer từ shareholder group này sang group khác.

## 9. Related-party merger và governance risk

Khi entities thuộc cùng business group merge, conflict-of-interest risk tăng. Controller có thể có different ownership percentages ở hai entities.

Ví dụ simplified:

```text
Controller owns:
Entity A = 30%
Entity B = 5%
```

Nếu merger terms favor A, controller có thể tăng economic control/value dù group-level story được mô tả là “synergy”.

Vì vậy related-party transaction phải đọc cùng [`08_corporate_governance_ownership_and_control.md`](./08_corporate_governance_ownership_and_control.md).

## 10. Share swap (주식교환)

**Share swap / 주식교환** có thể được dùng để biến company thành wholly owned subsidiary hoặc reorganize group ownership.

Economic effect là target shareholders đổi shares của target lấy shares/cash của parent/acquirer theo terms.

Analyst phải track post-transaction ownership và minority shareholder treatment.

## 11. Spin-off / company split (회사분할)

Korean corporate restructuring thường sử dụng nhiều dạng **company split / 회사분할**. Economic intuition quan trọng hơn việc học tên legal form.

Cần phân biệt hai logic:

### Proportional split / 인적분할

Existing shareholders thường nhận ownership ở các resulting entities theo proportion.

Conceptually:

```text
Old shareholder
   ↓
New Company A + New Company B
```

Shareholder tiếp tục directly own cả hai businesses.

### Physical split / 물적분할

Parent tách business thành subsidiary mới nhưng parent giữ ownership ở subsidiary.

```text
Shareholder
   ↓
Parent
   ↓
New subsidiary
```

Điểm governance-sensitive xuất hiện nếu high-growth division được tách thành subsidiary rồi IPO sau đó. Parent shareholder có indirect exposure nhưng ownership economics có thể thay đổi khi subsidiary issue new shares.

## 12. Tại sao company split?

Rationale có thể gồm focus, separate funding, strategic partnership, risk isolation hoặc preparation for sale/IPO.

Nhưng split không tự tạo value. Nó chỉ thay legal boundary. Value tăng nếu new structure cải thiện incentives, financing, transparency hoặc capital allocation.

## 13. Subsidiary IPO sau split

Khi subsidiary IPO, parent có thể raise capital hoặc monetize stake. Nhưng analyst phải theo dõi:

- parent ownership trước/sau IPO;
- new shares vs secondary shares;
- dilution;
- use of proceeds;
- whether growth asset value shifts away from parent minority shareholders.

Đây là classic case cần tách group value và listed-entity shareholder value.

## 14. Rights issue (유상증자)

**Rights issue / 유상증자** là issuance new shares để raise equity capital.

Company có thể dùng proceeds cho capex, acquisition, debt repayment hoặc liquidity rescue.

Share count tăng nên existing holder bị dilution nếu không participate hoặc nếu issue structure thay economics.

Không nên đánh giá rights issue chỉ là positive/negative. Hỏi:

```text
Tại sao cần vốn?
Issue price thế nào?
Ai tham gia?
Use of proceeds?
Expected return trên vốn mới?
```

## 15. Bonus issue (무상증자)

**Bonus issue / 무상증자** tăng number of shares nhưng không inject new external capital vào business.

Nếu economic pie không đổi, chia thành nhiều shares không tự tạo intrinsic value.

Price per share adjust tương ứng về lý thuyết.

Đây là nơi retail investors dễ nhầm “nhiều shares hơn = giàu hơn”.

## 16. Share buyback (자사주 매입)

Company dùng cash mua lại shares. Buyback tạo value khi shares undervalued và business không có higher-return use of cash.

Nhưng buyback ở overvaluation có thể destroy value.

Một formula intuition:

```text
If intrinsic value > repurchase price
→ remaining shareholders gain

If intrinsic value < repurchase price
→ remaining shareholders lose
```

## 17. Treasury shares (자기주식)

Treasury shares là shares company đã repurchase và giữ. Chúng có accounting/governance implications khác outstanding shares thông thường.

Analyst cần đọc treatment khi company cancels, disposes hoặc uses them trong transaction.

**Treasury-share cancellation / 자사주 소각** giảm share count economically khác với simply holding treasury shares.

## 18. Dividend và special dividend

Dividend chuyển cash từ company sang shareholders.

Regular dividend có thể signal stable distribution policy. Special dividend có thể đến từ asset sale hoặc excess cash.

Nhưng dividend cao trong company leverage lớn có thể weaken creditor protection.

Do đó payout phải đọc trong capital-allocation context.

## 19. Tender offer (공개매수)

**Tender offer / 공개매수** là offer mua shares từ shareholders theo price/terms công khai. Nó có thể dùng cho takeover, delisting hoặc ownership consolidation.

Important variables:

- offer price;
- target ownership threshold;
- financing;
- conditionality;
- treatment nếu không tender.

## 20. Delisting và going private

Going-private transaction có thể giúp company tránh public-market cost và quản lý dài hạn hơn, nhưng minority shareholders cần đánh giá exit price và fairness.

Một company delist không có nghĩa business xấu; transaction có thể driven by ownership strategy.

## 21. Asset sale và carve-out

Company có thể bán business unit hoặc assets thay vì shares của whole company.

Carve-out giúp isolate business nhưng tax, employee transfer, contracts và shared infrastructure làm transaction complex.

Analyst cần hỏi seller mất earnings nào và cash proceeds dùng làm gì.

## 22. Holding-company conversion

Group có thể restructure thành holding-company architecture để clarify control, ownership và business boundaries.

Nhưng simplification trên diagram không bảo đảm economic simplification. Intercompany stakes, dividends và related-party transactions vẫn cần theo dõi.

Xem [`05_group_structure_affiliates_holding_companies.md`](./05_group_structure_affiliates_holding_companies.md).

## 23. Strategic investment và minority stake

Mua 10–20% strategic stake không giống acquisition. Investor có exposure nhưng không full control.

Accounting treatment và governance rights phụ thuộc influence/control level.

Cần distinguish:

```text
Financial investment
Strategic minority
Significant influence
Joint control
Control
```

## 24. Joint venture (JV / 합작법인)

JV hữu ích khi partners chia technology, market access hoặc capital. Nhưng decision rights phải rõ.

50/50 ownership nghe “công bằng” nhưng có deadlock risk nếu governance weak.

Key questions:

- ai appoint CEO?
- reserved matters?
- funding obligations?
- IP ownership?
- exit mechanism?

## 25. M&A integration risk

Deal close chỉ là beginning.

Integration failure có thể đến từ IT systems, culture, customer churn, employee departures, duplicated processes hoặc incompatible incentives.

Một synergy model nên có timeline:

```text
Day 1 legal close
→ 100-day integration
→ systems/process integration
→ synergy realization
→ normalized economics
```

Nếu management claim synergy ngay trong Year 1 nhưng integration complexity rất cao, assumption có thể aggressive.

## 26. Culture integration

Korea-specific group culture, hierarchy, evaluation và communication style có thể làm cross-border acquisition khó hơn financial model thể hiện.

Xem [`13_business_culture_decision_making_and_communication.md`](./13_business_culture_decision_making_and_communication.md).

## 27. Employee consequences

M&A và split có thể thay employer legal entity, reporting line, compensation, location hoặc promotion path.

Đối với career analysis, transaction không chỉ là stock-market event.

Hỏi:

- team thuộc entity nào sau deal?
- duplicate functions có bị rationalize?
- core capability được giữ ở đâu?
- decision center chuyển về đâu?

## 28. Event study mindset

Khi corporate action được announce, tách ba layers:

**Fact:** deal terms chính thức.

**Management claim:** synergy, strategic rationale.

**Market reaction:** price changes.

Market reaction không tự chứng minh deal tốt/xấu. Nó là aggregate expectation tại một thời điểm.

## 29. Pro forma analysis

Để hiểu post-deal company, xây **pro forma / 추정 결합** view.

```text
Standalone A revenue/profit/debt
+ Standalone B
+ Expected synergy
- Integration cost
+ Financing impact
= Pro forma combined company
```

Sau đó check leverage, share count và interest coverage.

## 30. Per-share analysis

Deal có thể tăng total profit nhưng EPS hoặc intrinsic value per share giảm nếu dilution lớn.

Do đó luôn chuyển từ company-level value sang **per-share economics**.

## 31. Event checklist cho DART/KIND

Khi thấy announcement về corporate action, đọc theo flow:

```text
1. Transaction type
2. Counterparty / related party?
3. Valuation basis
4. Exchange ratio / issue price
5. Financing
6. Ownership before/after
7. Accounting perimeter
8. Use of proceeds
9. Governance approval
10. Conditions / timeline
11. Minority-shareholder effect
12. Balance-sheet effect
```

## 32. Red flags

Một số signal cần deep-dive thêm:

- repeated acquisitions nhưng ROIC giảm;
- large goodwill accumulation;
- related-party merger với complex ratio;
- split rồi subsidiary IPO liên tục;
- frequent emergency equity issuance;
- asset sale để finance ordinary operations;
- buyback nhưng không cancel trong governance-sensitive context;
- acquisition funded bằng short-term debt.

Red flag không phải proof wrongdoing; nó là reason để mở footnotes và transaction documents.

## Mental Model

> Corporate action là **reallocation of ownership claims** chứ không chỉ là headline event.

Khi đọc bất kỳ deal nào, hãy vẽ hai sơ đồ:

```text
BEFORE: assets → liabilities → owners
AFTER : assets → liabilities → owners
```

Sau đó hỏi ba câu:

1. Ai control cái gì sau transaction?
2. Ai chịu thêm risk?
3. Value per share/claim của mỗi stakeholder thay đổi thế nào?

## Common misconceptions

**“M&A làm revenue lớn hơn nên deal tốt.”** Sai. Premium và financing có thể destroy value.

**“Spin-off tự unlock value.”** Không. Legal separation chỉ tạo option; value phụ thuộc incentives, funding và ownership treatment.

**“Bonus issue làm shareholder giàu hơn.”** Không. Number of shares tăng nhưng pie không tự lớn hơn.

**“Buyback luôn tốt.”** Không. Repurchase overvalued shares destroy value.

**“Related-party transaction trong cùng group không quan trọng vì owner cuối giống nhau.”** Sai với listed entities có different minority shareholders.

## Liên kết tiếp theo

- [`05_group_structure_affiliates_holding_companies.md`](./05_group_structure_affiliates_holding_companies.md)
- [`08_corporate_governance_ownership_and_control.md`](./08_corporate_governance_ownership_and_control.md)
- [`09_disclosure_accounting_dart_kind.md`](./09_disclosure_accounting_dart_kind.md)
- [`10_capital_markets_kospi_kosdaq_konex.md`](./10_capital_markets_kospi_kosdaq_konex.md)
- [`20_how_to_analyze_a_korean_company.md`](./20_how_to_analyze_a_korean_company.md)
- [`36_credit_ratings_bonds_default_and_restructuring.md`](./36_credit_ratings_bonds_default_and_restructuring.md)