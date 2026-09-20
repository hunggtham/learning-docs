# Hệ thống tài chính ngoài ngân hàng tại Hàn Quốc (Securities, Insurance, Asset Management / 증권·보험·자산운용)

Nếu chỉ nhìn ngân hàng, ta sẽ bỏ sót một phần rất lớn của cách capital di chuyển trong nền kinh tế Hàn Quốc. Doanh nghiệp không chỉ vay tiền từ bank. Họ còn phát hành bond, issue shares, securitize assets, raise private capital, mua bảo hiểm, dùng derivatives, nhận underwriting từ securities firms và được định giá rủi ro bởi credit-rating agencies. Ở phía đối diện, household và institutional investors đưa tiền vào funds, pension products, insurance contracts và securities accounts. Vì vậy hệ thống tài chính thực tế là một network gồm **banks, securities companies, insurers, asset managers, pension funds, credit-rating agencies, exchanges, clearing systems và regulators**.

Chapter này nối trực tiếp với [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md), nhưng tập trung vào phần **market-based finance / 시장성 금융** và các institution ngoài ngân hàng.

## 1. Tại sao nền kinh tế cần nhiều loại financial intermediary?

Nếu mọi company chỉ có thể vay bank, allocation of capital sẽ phụ thuộc quá nhiều vào balance sheet và risk appetite của banking system. Market-based finance giúp mở thêm kênh vốn cho những firm lớn, firm tăng trưởng cao hoặc project có profile không phù hợp với traditional bank lending.

Một cách nhìn đơn giản:

```text
Household / institution có vốn
          ↓
Bank deposit / fund / insurance / securities account
          ↓
Financial intermediary / market
          ↓
Loan / bond / equity / structured product
          ↓
Company / project / household borrower
```

Mỗi intermediary giải một problem khác nhau. Bank xử lý maturity transformation và credit screening. Securities firm giúp issuance, trading và market making. Asset manager gom vốn rồi đầu tư theo mandate. Insurer nhận premium đổi lấy risk protection và trở thành long-duration investor. Credit-rating agency giảm một phần information asymmetry giữa issuer và bond investor.

## 2. Securities company là gì? (Securities Firm / 증권사)

Một **securities company / 증권회사·증권사** không chỉ là app mua cổ phiếu. Business của họ thường có nhiều engine khác nhau: brokerage, investment banking, underwriting, wealth management, trading, derivatives, structured finance, prime brokerage và đôi khi real-estate/project finance exposure.

Điều này quan trọng vì cùng một securities firm có thể có revenue rất khác theo cycle. Khi stock trading boom, brokerage commissions tăng. Khi IPO/M&A mạnh, investment-banking fees tăng. Khi bond yield hoặc asset prices biến động mạnh, proprietary trading result có thể đổi nhanh. Khi real-estate PF xấu đi, credit cost hoặc valuation loss có thể xuất hiện.

Vì vậy không nên nhìn một 증권사 như “brokerage business” duy nhất.

## 3. Brokerage và transaction economics

**Brokerage / 위탁매매** tạo revenue khi client giao dịch securities. Revenue thường liên quan tới trading volume, fee rate, margin financing và asset mix.

Một mental model:

\[
Brokerage\ Revenue \approx Trading\ Volume \times Effective\ Fee\ Rate
\]

Nhưng fee rate có thể giảm vì competition. Do đó growth của brokerage không chỉ đến từ volume mà còn từ margin lending, overseas securities, wealth products và cross-selling.

Nếu revenue phụ thuộc quá mạnh vào retail trading activity, earnings sẽ cyclical hơn một wealth-management model có recurring assets-under-management fee.

## 4. Investment Banking: underwriting, IPO, bond và M&A

**Investment Banking / IB / 투자은행 업무** là business giúp client huy động vốn hoặc thực hiện transaction.

Khi company IPO, issue corporate bonds, rights issue hoặc làm acquisition, securities firm có thể đóng vai trò arranger, underwriter hoặc advisor.

Underwriter không chỉ “giới thiệu nhà đầu tư”. Họ phải structure deal, assess pricing, market security, coordinate disclosure và trong một số case chịu underwriting risk nếu securities không bán hết.

Một deal tốt cho issuer chưa chắc tốt cho underwriter nếu risk được price quá thấp. Ngược lại, underwriting fee cao nhưng deal fail có thể gây reputation cost.

## 5. Proprietary trading và market risk

Nhiều securities firms giữ bond, equity, derivatives hoặc structured positions trên balance sheet. Khi đó firm không chỉ nhận fee mà còn chịu **market risk / 시장위험**.

Nếu interest rate tăng, giá bond fixed-rate giảm. Nếu volatility tăng, derivative books có thể thay đổi value nhanh. Nếu funding ngắn hạn nhưng asset dài hạn, liquidity risk xuất hiện tương tự bank nhưng cấu trúc khác.

Điểm cần nhớ:

> Securities company có thể nhìn giống “asset-light fee business” ở income statement nhưng thực tế balance sheet vẫn rất quan trọng.

## 6. Structured finance và Project Finance

Korean securities firms có thể tham gia **structured finance / 구조화금융**, securitization hoặc real-estate PF. Đây là khu vực cần đọc kỹ vì return cao thường đi kèm complexity cao.

Một PF structure có thể gồm:

```text
Developer / Sponsor
       ↓ equity
Project SPV
       ↓ bridge financing
Land acquisition / permits
       ↓
Main PF
       ↓
Construction / presales / completion
```

Securities firm có thể arrange loan, provide guarantee, purchase securitized paper hoặc hold mezzanine risk. Vì vậy analyst phải phân biệt direct loan, guarantee, contingent liability và off-balance-sheet commitment.

Xem thêm [`18_construction_real_estate_and_project_finance.md`](./18_construction_real_estate_and_project_finance.md).

## 7. Asset Management là gì? (Asset Management / 자산운용)

**Asset manager / 자산운용사** quản lý tiền của investor theo mandate. Họ không sở hữu toàn bộ asset bằng equity của chính mình; phần lớn tài sản thuộc fund investors.

Business model thường dựa trên **Assets Under Management / AUM / 운용자산** và fee rate:

\[
Management\ Fee \approx AUM \times Fee\ Rate
\]

Do đó revenue có thể tăng vì net inflow hoặc asset price tăng. Ngược lại, market giảm vừa làm AUM giảm vừa có thể gây redemption.

Điểm khác với manufacturing company là asset manager có thể có operating leverage rất cao: thêm AUM không luôn cần tăng headcount tương ứng.

## 8. Active vs Passive

**Active management / 액티브 운용** cố gắng outperform benchmark thông qua security selection, allocation hoặc timing. **Passive management / 패시브 운용** chủ yếu tracking index.

Passive thường fee thấp hơn, nên economics dựa nhiều vào scale. Active có fee cao hơn nhưng phải chứng minh value sau cost.

Điều này tạo pressure dài hạn lên traditional active managers: nếu alpha không bền vững, investor chuyển sang low-cost index products.

## 9. ETF và ecosystem

ETF không chỉ là một ticker trên exchange. Nó là ecosystem gồm sponsor/asset manager, authorized participants, liquidity providers, custodian và underlying market.

ETF price có thể lệch NAV trong ngắn hạn, nhưng creation/redemption mechanism giúp arbitrage kéo price về gần underlying value.

Khi phân tích ETF business của asset manager, câu hỏi không chỉ là “fund performance tốt không” mà còn là:

- AUM growth;
- market share;
- fee compression;
- product differentiation;
- distribution power;
- liquidity và tracking quality.

## 10. Insurance: risk transfer trước, investment sau

**Insurance / 보험** có logic khác bank và securities company. Customer trả premium để transfer một risk contractually defined sang insurer.

Hai broad groups là **life insurance / 생명보험** và **non-life insurance / 손해보험**.

Insurer nhận premium hôm nay nhưng có thể phải trả claim nhiều năm sau. Vì vậy họ vừa là risk underwriter vừa là long-duration asset allocator.

Mental model:

```text
Premium inflow
   ↓
Reserve / liability recognition
   ↓
Investment portfolio earns return
   ↓
Claims + expenses + capital requirement
```

## 11. Underwriting economics

Đối với non-life insurance, một metric trực quan là **combined ratio**:

\[
Combined\ Ratio = Loss\ Ratio + Expense\ Ratio
\]

Nếu dưới 100%, underwriting business trước investment income đang profitable. Nếu trên 100%, insurer cần investment income hoặc pricing adjustment để bù.

Nhưng không nên mechanical. Product mix, reserve development, catastrophes và regulatory accounting có thể làm ratio biến động.

## 12. Life insurer và duration mismatch

Life insurer bán long-term liabilities. Nếu guarantee cho policyholder một mức return tương đối cao nhưng portfolio yield giảm lâu dài, spread compression xuất hiện.

Đây là **asset-liability management / ALM / 자산부채관리** problem.

Insurer phải match duration, currency và cash-flow characteristics giữa assets và liabilities. Nếu liabilities rất dài nhưng asset duration ngắn hơn, reinvestment risk tăng.

## 13. Float và investment portfolio

Premium được giữ trước khi claim được trả tạo ra **float**. Float có economic value nếu insurer underwrite discipline tốt và đầu tư thận trọng.

Nhưng float không phải “free money”. Nó là liability-backed capital. Nếu claim assumptions sai hoặc asset quality xấu, losses có thể xuất hiện đồng thời ở cả underwriting và investment side.

## 14. Reinsurance

Insurer có thể chuyển một phần risk sang **reinsurer / 재보험사**. Reinsurance giúp giảm tail risk và capital volatility.

Ví dụ, một insurer không muốn giữ toàn bộ exposure của một natural-disaster portfolio nên cede một phần premium để reinsurer gánh một phần loss.

Điều này giống risk-sharing layer chứ không phải loại bỏ risk khỏi system.

## 15. Credit-card, consumer finance và specialized finance

Ngoài bank/securities/insurance, Korea còn có **credit-card companies / 카드사**, capital companies và specialized finance firms.

Economics của credit-card company thường kết hợp merchant fees, revolving/loan income, installment finance và credit losses.

Khi household credit quality xấu, delinquency và provisioning tăng. Vì vậy consumer-finance business nhạy với labor market, household debt, policy rate và regulation.

## 16. Pension funds và institutional capital

Pension capital có investment horizon dài hơn household trading capital. Điều này giúp pension funds trở thành important institutional investor trong domestic và global markets.

Một pension system phải giải đồng thời ba bài toán:

1. liability dài hạn;
2. contribution inflow/outflow;
3. investment return phù hợp risk tolerance.

Nếu demographics aging nhanh, cash-flow structure của pension cũng thay đổi. Vì vậy financial-market structure nối trực tiếp với [`27_demographics_households_and_consumption.md`](./27_demographics_households_and_consumption.md).

## 17. Credit-rating agencies (신용평가사)

Bond investor không thể tự deep-dive mọi issuer. **Credit-rating agency / 신용평가사** giúp chuẩn hóa assessment về default risk tương đối.

Rating thường xem xét business risk, financial risk, leverage, coverage, liquidity, group support và event risk.

Nhưng rating không phải guarantee. Nó có thể lag so với market hoặc không capture tail event tốt. Analyst nên dùng rating như một input, không phải conclusion.

Một pattern quan trọng:

```text
Operating weakness
→ leverage rises
→ rating outlook weakens
→ spread widens
→ refinancing cost rises
→ cash flow weakens further
```

Đây là feedback loop giữa real economy và capital market.

## 18. Regulation và capital adequacy

Financial firms khác industrial companies vì leverage là core business. Vì vậy regulation tập trung mạnh vào capital adequacy, liquidity, consumer protection, suitability, market conduct và systemic risk.

Điều này có một implication quan trọng: equity capital của financial institution không chỉ là funding source; nó còn là **loss-absorbing buffer** và regulatory constraint.

Do đó ROE cao nhờ leverage phải luôn được đọc cùng capital ratio và asset quality.

## 19. Financial holding company

Một **financial holding company / 금융지주회사** có thể sở hữu bank, securities, card, insurance, asset-management subsidiaries.

Group logic cho phép cross-selling và capital allocation nhưng cũng tạo complexity. Cash ở regulated subsidiary không thể tùy ý upstream giống ordinary industrial subsidiary.

Vì vậy group-level cash không đồng nghĩa fully fungible cash.

Xem [`05_group_structure_affiliates_holding_companies.md`](./05_group_structure_affiliates_holding_companies.md).

## 20. Cách đọc một Korean financial company

Đừng dùng template manufacturing.

Đối với bank, focus vào NIM, loan growth, deposit mix, credit cost, capital ratio.

Đối với securities firm, focus vào brokerage, IB pipeline, trading exposure, PF/structured exposure, liquidity và leverage.

Đối với insurer, focus vào underwriting margin, reserve quality, ALM, investment yield và capital adequacy.

Đối với asset manager, focus vào AUM, net flow, fee rate, product mix và operating leverage.

Một câu hỏi tổng quát hữu ích là:

> Firm kiếm spread, fee hay underwriting margin? Và balance sheet chịu risk ở đâu?

## 21. Financial sector truyền shock vào real economy như thế nào?

Shock không dừng ở financial market.

```text
Rate / credit shock
      ↓
Funding cost hoặc risk appetite đổi
      ↓
Bank / securities / insurer điều chỉnh balance sheet
      ↓
Credit availability và asset prices đổi
      ↓
Corporate capex / household spending đổi
      ↓
GDP / employment / earnings đổi
```

Do đó financial sector là transmission mechanism chứ không chỉ sector riêng biệt.

## Mental Model

> Bank chủ yếu **transform deposits thành credit**. Securities firms **connect issuers với capital market và intermediate trading risk**. Asset managers **allocate investor capital theo mandate**. Insurers **price risk và invest long-duration liabilities**. Credit-rating agencies **compress information thành risk categories**.

Muốn phân tích một financial company, trước tiên xác định nó đang kiếm tiền bằng **spread, fee, underwriting hoặc balance-sheet risk**; sau đó tìm constraint về capital, liquidity và regulation.

## Common misconceptions

**“Financial company asset-light nên ít risk.”** Sai. Nhiều financial firms có balance-sheet risk rất lớn dù physical assets ít.

**“AUM là revenue.”** Sai. Asset manager chỉ thu fee trên AUM; underlying asset thuộc investor.

**“Insurance premium càng cao càng tốt.”** Chưa đủ. Growth với underpricing có thể tạo loss tương lai.

**“Credit rating cao nghĩa không thể default.”** Sai. Rating là probabilistic assessment và có thể thay đổi.

**“Brokerage app = toàn bộ securities business.”** Sai. IB, trading, structured finance và PF có thể quan trọng ngang hoặc hơn brokerage.

## Liên kết tiếp theo

- [`10_capital_markets_kospi_kosdaq_konex.md`](./10_capital_markets_kospi_kosdaq_konex.md) — market structure và securities.
- [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md) — funding và leverage.
- [`18_construction_real_estate_and_project_finance.md`](./18_construction_real_estate_and_project_finance.md) — PF.
- [`27_demographics_households_and_consumption.md`](./27_demographics_households_and_consumption.md) — household/pension connection.
- [`34_digital_fintech_cloud_and_it_services.md`](./34_digital_fintech_cloud_and_it_services.md) — fintech, digital finance và cloud.