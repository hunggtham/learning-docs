# Credit rating, trái phiếu, default và restructuring tại doanh nghiệp Hàn Quốc (Credit Risk / 신용위험·회사채·구조조정)

Một company có thể vẫn báo operating profit nhưng rơi vào crisis nếu debt maturity đến trước cash. Vì vậy muốn hiểu doanh nghiệp, đặc biệt là construction, heavy industry, airline, retail, leveraged holding company hoặc project-heavy business, phải tách **profitability risk** khỏi **credit risk / 신용위험**.

Credit analysis không hỏi trước tiên “company có tăng trưởng không?”. Nó hỏi: **company có đủ cash để trả đúng nghĩa vụ, đúng thời điểm, trong một range scenario hợp lý hay không?**

Chapter này nối accounting, corporate funding, bond market và restructuring thành một flow duy nhất.

## 1. Credit risk là gì?

**Credit risk / 신용위험** là risk borrower hoặc issuer không thực hiện đầy đủ nghĩa vụ contract: interest, principal hoặc payment khác.

Ba khái niệm nên tách:

- **Default probability (PD / 부도확률):** xác suất borrower default.
- **Loss given default (LGD / 부도시손실률):** nếu default thì creditor mất bao nhiêu sau recovery.
- **Exposure at default (EAD / 부도시익스포저):** exposure tại thời điểm default.

Một approximation:

\[
Expected\ Credit\ Loss \approx PD \times LGD \times EAD
\]

Credit analyst không chỉ quan tâm whether default happens mà còn recovery value nếu nó xảy ra.

## 2. Equity investor và creditor nhìn cùng company khác nhau thế nào?

Equity holder hưởng upside sau khi mọi fixed claims được trả. Creditor thường chỉ nhận principal + interest như contract; upside bị giới hạn nhưng downside là loss nếu borrower fail.

Vì vậy equity investor có thể thích aggressive expansion nếu expected upside lớn. Creditor thường quan tâm cash-flow stability, collateral, covenants và downside protection hơn.

Một project có NPV dương nhưng volatility rất cao có thể attractive cho equity nhưng uncomfortable cho creditor nếu project làm leverage tăng mạnh.

## 3. Corporate bond (회사채) hoạt động thế nào?

Khi company phát hành **corporate bond / 회사채**, investor cho issuer vay theo terms đã định: face value, coupon, maturity, ranking và covenant.

Bond price và yield di chuyển ngược chiều. Nếu market yêu cầu yield cao hơn do benchmark rate hoặc credit spread tăng, price của bond cũ giảm.

Yield có thể hiểu gần đúng:

\[
Corporate\ Yield \approx Government\ Benchmark + Credit\ Spread + Liquidity\ Premium + Term\ Premium
\]

Credit spread phản ánh compensation mà investor yêu cầu cho issuer-specific/default risk và uncertainty.

## 4. Spread là một market signal, không phải diagnosis hoàn chỉnh

Nếu credit spread widen nhanh, market đang yêu cầu premium lớn hơn. Nhưng analyst vẫn phải hỏi nguyên nhân:

```text
Benchmark rate tăng?
Sector risk tăng?
Issuer leverage tăng?
Liquidity giảm?
Event risk?
Market-wide risk-off?
```

Spread có thể đi trước rating action, nhưng cũng có thể overshoot trong panic.

## 5. Credit rating là gì? (신용등급)

**Credit rating / 신용등급** là opinion có structure về relative creditworthiness. Rating agencies thường xem business risk, competitive position, financial policy, leverage, coverage, liquidity, group support và event risk.

Rating không phải guarantee. Một AAA-like label không nghĩa loss probability bằng zero. Một low rating cũng không nghĩa default chắc chắn.

Quan trọng hơn là **rating trajectory**:

```text
Stable → Negative outlook → Downgrade
```

hoặc

```text
Weak business → deleveraging → stronger coverage → upgrade potential
```

Direction đôi khi quan trọng hơn static letter grade.

## 6. Investment grade và speculative grade

Market thường phân biệt broad bucket giữa **investment grade** và **speculative/high-yield**. Boundary cụ thể tùy rating scale/methodology.

Khi issuer bị downgrade qua một threshold quan trọng, investor base có thể thay đổi. Một số institution mandate chỉ cho phép hold securities trên rating level nhất định. Vì vậy downgrade có thể làm spread widen mạnh hơn purely fundamental change.

Đây là **forced-seller effect**.

## 7. Interest coverage

Một metric cơ bản:

\[
Interest\ Coverage = \frac{EBIT}{Interest\ Expense}
\]

Nếu EBIT = 300 tỷ KRW và interest = 100 tỷ, coverage = 3x.

Nhưng 3x không phải universal safe threshold. Cyclical business cần buffer lớn hơn stable utility-like business. Ngoài ra EBIT không phải cash.

Vì vậy cần xem CFO, working capital và capex.

## 8. Net debt và leverage

\[
Net\ Debt = Gross\ Debt - Cash
\]

\[
Net\ Debt/EBITDA
\]

Metric useful nhưng có trap.

Cash có thể restricted. EBITDA có thể peak-cycle. Lease liabilities hoặc guarantees có thể chưa capture đầy đủ. Vì vậy net-debt ratio chỉ là starting point.

## 9. Debt maturity ladder

Credit analysis phải có **maturity ladder / 만기구조**.

Ví dụ:

```text
Year 1: 1.2T KRW
Year 2: 0.4T KRW
Year 3: 0.3T KRW
Year 4+: 2.0T KRW
```

Total debt = 3.9T nhưng immediate refinancing pressure chủ yếu nằm ở Year 1.

Hai companies có cùng leverage nhưng maturity concentration khác sẽ có liquidity risk rất khác.

## 10. Refinancing risk

**Refinancing risk / 차환위험** xuất hiện khi company phụ thuộc vào issuing new debt để repay old debt.

Refinancing bình thường không xấu. Mature companies thường roll debt. Problem xảy ra khi market access mất đúng thời điểm maturity wall lớn.

Causal chain:

```text
Weak earnings
→ rating concern
→ spread rises
→ refinancing cost rises
→ coverage worsens
→ investor confidence falls
→ market access tightens
```

Đây là self-reinforcing credit spiral.

## 11. Liquidity sources vs liquidity uses

Một cách phân tích practical là dựng bảng 12–24 tháng.

**Sources** có thể gồm cash, expected CFO, committed credit lines, asset sale, receivable collection.

**Uses** gồm debt maturity, interest, capex, working capital, dividend và mandatory payments.

Logic:

\[
Liquidity\ Buffer = Available\ Sources - Near\ Term\ Uses
\]

Nếu buffer chỉ dương trong base case nhưng âm khi revenue giảm 10%, company có liquidity fragility.

## 12. Committed vs uncommitted credit line

Không nên coi mọi unused credit line như cash.

**Committed line** thường chắc chắn hơn nhưng vẫn có conditions. **Uncommitted line** có thể bị lender giảm/cancel dễ hơn.

Trong crisis, liquidity quality quan trọng hơn headline amount.

## 13. Covenant

**Covenant / 재무약정** là điều khoản bảo vệ creditor hoặc giới hạn borrower behavior.

Ví dụ:

- maximum leverage;
- minimum interest coverage;
- minimum net worth;
- restriction on additional debt;
- restriction on dividend;
- collateral requirement.

Nếu breach, outcome có thể từ waiver tới higher pricing, collateral demand hoặc acceleration.

Covenant breach không đồng nghĩa bankruptcy nhưng có thể làm negotiation power chuyển sang creditor.

## 14. Secured vs unsecured debt

**Secured debt / 담보부채무** có claim lên collateral cụ thể. **Unsecured debt / 무담보채무** dựa nhiều hơn vào general creditworthiness.

Trong default, recovery hierarchy phụ thuộc legal ranking, collateral value và restructuring terms.

Vì vậy debt amount phải được đọc cùng **priority / seniority / 변제순위**.

## 15. Senior, subordinated và mezzanine

Senior debt được ưu tiên hơn subordinated debt. **Mezzanine** nằm giữa debt và equity về risk/return, thường có option-like terms hoặc higher coupon.

Capital structure có thể hình dung:

```text
Senior secured
Senior unsecured
Subordinated / mezzanine
Preferred equity
Common equity
```

Càng xuống thấp, upside có thể lớn hơn nhưng protection khi distress yếu hơn.

## 16. Convertible bond và bond with warrants

**Convertible bond / CB / 전환사채** cho holder quyền convert bond thành equity theo terms nhất định. **Bond with warrants / BW / 신주인수권부사채** gắn quyền mua shares.

Đây là hybrid securities: vừa có debt claim vừa có equity optionality.

Issuer có thể dùng vì coupon thấp hơn ordinary debt hoặc vì investor muốn upside. Nhưng existing shareholders cần nhìn dilution potential.

## 17. Guarantees và contingent liabilities

Một company có thể không show full economic leverage qua borrowings nếu đã guarantee debt cho subsidiary/SPV.

Nếu guaranteed borrower fail, contingent obligation có thể trở thành actual cash outflow.

Vì vậy analyst phải đọc footnotes về:

- payment guarantees;
- debt guarantees;
- PF guarantees;
- letters of credit;
- commitments;
- litigation.

Xem [`09_disclosure_accounting_dart_kind.md`](./09_disclosure_accounting_dart_kind.md).

## 18. Cross-default và acceleration

Debt contracts có thể chứa **cross-default**: default ở một obligation có thể trigger default ở obligation khác.

**Acceleration** cho phép creditor yêu cầu payment sớm sau specified event.

Điều này khiến small default đôi khi lan thành liquidity crisis lớn.

## 19. Technical default vs payment default

Company có thể violate covenant dù vẫn trả interest đúng hạn. Đây là **technical default**.

**Payment default** là không trả principal/interest đúng contract.

Technical default vẫn nghiêm trọng vì lender có thể demand renegotiation hoặc additional protection.

## 20. Distress không đồng nghĩa immediate bankruptcy

Khi company distress, nhiều path có thể xảy ra:

```text
Operational turnaround
Asset sale
Equity raise
Debt extension
Covenant waiver
Debt-for-equity swap
Workout
Court-led rehabilitation
Liquidation
```

Do đó từ “khó khăn” tới “bankruptcy” có nhiều intermediate states.

## 21. Workout (워크아웃)

**Workout / 워크아웃** thường là restructuring coordinated với creditors ngoài full liquidation process. Mục tiêu là giữ going-concern value nếu business core vẫn viable nhưng capital structure quá nặng.

Creditor có thể extend maturity, reduce rate, inject liquidity hoặc swap debt thành equity.

Economic logic:

> Nếu going-concern value > liquidation value, restructuring có thể tốt hơn phá sản ngay.

## 22. Court rehabilitation (회생절차)

Court-led rehabilitation giúp freeze/coordinate claims và xây plan để company tiếp tục operate trong khi debt được restructure.

Key question là **viability**. Nếu core business tạo cash nhưng debt burden quá lớn, rehabilitation có rationale. Nếu business model không còn viable, restructuring chỉ trì hoãn liquidation.

## 23. Debt-for-equity swap

Creditor đổi debt thành shares làm debt giảm nhưng ownership chuyển một phần sang creditors.

Balance-sheet logic:

```text
Debt ↓
Equity ↑
Interest burden ↓
Old shareholder dilution ↑
```

Company có thể sống khỏe hơn nhưng old shareholders không nhất thiết benefit tương ứng.

## 24. Asset sale và deleveraging

Sell non-core asset tạo cash để repay debt. Đây là simple restructuring tool nhưng có trade-off.

Nếu bán high-quality asset ở distressed price, balance sheet tốt hơn ngắn hạn nhưng future earnings power giảm.

Vì vậy deleveraging phải xét **asset quality sold** chứ không chỉ debt reduction.

## 25. Rights issue trong distress

Equity raise có thể cứu solvency/liquidity nhưng dilution lớn nếu issue price thấp.

Một company có thể survive while old equity value bị heavily impaired.

Đây là lý do credit recovery và equity return không giống nhau.

## 26. Recovery analysis

Khi default risk cao, hỏi:

```text
Enterprise value trong distress?
Collateral value?
Priority của từng claim?
Administrative/restructuring cost?
Going-concern vs liquidation value?
```

Simple waterfall:

```text
Distressed enterprise value
→ secured creditors
→ senior unsecured
→ subordinated
→ preferred
→ common equity
```

Common equity chỉ nhận residual sau claims trước đó.

## 27. Cyclical company và peak EBITDA trap

Nếu leverage = debt / peak EBITDA, ratio có thể trông thấp đúng lúc cycle tốt nhất.

Ví dụ debt = 4T, EBITDA peak = 2T → 2x. Nếu normalized EBITDA = 1T → 4x.

Credit analyst phải normalize cycle.

Điều này đặc biệt quan trọng với semiconductors, chemicals, shipping, steel, construction và commodities.

## 28. Working-capital shock

Credit crisis không chỉ đến từ operating loss.

Nếu customer trả chậm, inventory tăng và suppliers yêu cầu cash sooner:

```text
DSO ↑
DIO ↑
DPO ↓
→ cash conversion cycle lengthens
→ funding need rises
```

Company có thể report profit nhưng run out of cash.

## 29. Rating trigger và collateral trigger

Một số contract thay terms khi rating giảm: collateral requirement tăng, derivative margin tăng hoặc funding access giảm.

Do đó downgrade có thể tạo **nonlinear cash need**.

## 30. Group support: có nhưng không được mặc định

Subsidiary thuộc chaebol lớn có thể benefit từ implicit/explicit group support. Nhưng analyst phải phân biệt:

- legal guarantee;
- parent ownership;
- strategic importance;
- historical support;
- regulatory restriction.

Brand name không bằng guarantee.

## 31. Public enterprise và quasi-sovereign perception

Một số public institutions có perceived support mạnh hơn private issuer, nhưng cũng cần đọc legal framework và actual support mechanism.

Không nên tự động coi every public-related entity = sovereign risk.

Xem [`25_public_enterprises_and_state_owned_companies.md`](./25_public_enterprises_and_state_owned_companies.md).

## 32. Stress test credit

Một robust credit stress test có thể dùng:

```text
Revenue -15%
Margin -3pt
DSO +20 days
Rate +150bp
Refinancing spread +250bp
KRW depreciation 10%
Asset-sale proceeds -30% vs book value
```

Sau đó calculate:

- CFO;
- interest coverage;
- debt/EBITDA;
- liquidity buffer;
- covenant headroom;
- maturity gap.

Mục tiêu không phải predict exact crisis mà tìm threshold nơi capital structure bắt đầu fail.

## 33. Credit analysis workflow

Một workflow practical:

```text
1. Business stability
2. Earnings cyclicality
3. Cash conversion
4. Debt amount + hidden obligations
5. Maturity ladder
6. Interest and currency sensitivity
7. Liquidity sources
8. Covenant / collateral
9. Group support
10. Stress scenario
11. Recovery if default
```

## Mental Model

> Equity analysis hỏi **upside còn bao nhiêu**. Credit analysis hỏi **downside tới đâu trước khi creditor mất tiền**.

Credit risk là intersection của:

```text
Business volatility
× leverage
× maturity concentration
× liquidity
× market access
× legal priority
```

Một company có good business nhưng bad capital structure vẫn có thể default. Một company mediocre nhưng debt thấp và liquidity mạnh có thể survive rất lâu.

## Common misconceptions

**“Có lãi thì không default.”** Sai. Default là cash/timing problem.

**“Debt/EBITDA thấp là an toàn.”** Chưa đủ. EBITDA có thể peak-cycle và maturity có thể tập trung.

**“Rating agency đã đánh giá rồi nên không cần tự phân tích.”** Sai. Rating là input, không phải substitute cho analysis.

**“Restructuring tốt cho company thì tốt cho shareholder.”** Không nhất thiết. Debt-for-equity swap hoặc rights issue có thể cứu company nhưng dilute old equity mạnh.

**“Parent group lớn sẽ luôn cứu affiliate.”** Không thể mặc định nếu không có legal/economic incentive rõ.

## Liên kết tiếp theo

- [`09_disclosure_accounting_dart_kind.md`](./09_disclosure_accounting_dart_kind.md) — đọc obligations và footnotes.
- [`10_capital_markets_kospi_kosdaq_konex.md`](./10_capital_markets_kospi_kosdaq_konex.md) — bond/equity market context.
- [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md) — funding structure.
- [`18_construction_real_estate_and_project_finance.md`](./18_construction_real_estate_and_project_finance.md) — PF risk.
- [`20_how_to_analyze_a_korean_company.md`](./20_how_to_analyze_a_korean_company.md) — company-analysis framework.