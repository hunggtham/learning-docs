# Cách phân tích một công ty Hàn Quốc từ đầu đến cuối (Company Analysis Framework / 한국 기업 분석 프레임워크)

File này là entry point thực hành của toàn library. Khi gặp một company mới—dù là nơi định ứng tuyển, supplier, đối tác dự án hay cổ phiếu—đừng bắt đầu bằng stock chart hoặc reputation. Hãy đi từ **legal identity → business model → industry/value chain → financial machine → governance → capital allocation → risk/valuation**.

Mục tiêu không phải tạo một checklist cơ học. Mục tiêu là xây một **causal model** đủ rõ để trả lời: company kiếm tiền bằng cách nào, điều gì làm economics tốt/xấu đi, và điều kiện nào khiến thesis sai.

## Bước 0 — Đặt company vào lịch sử và ecosystem

Hỏi company sinh ra trong phase nào của Korean economy.

Một construction/industrial group hình thành trong reconstruction/HCI era thường có asset base, debt habit và supplier network khác platform sinh trong broadband era. Một IT service affiliate của chaebol có captive demand khác startup SaaS.

Historical origin không quyết định tương lai, nhưng giúp giải thích organizational DNA.

Nếu thuộc major group, đọc [`00_history/08_company_genealogies.md`](./00_history/08_company_genealogies.md) và [`04_chaebol_and_large_business_groups.md`](./04_chaebol_and_large_business_groups.md).

## Bước 1 — Xác định đúng legal entity

Brand không phải legal entity.

Ghi rõ:

- Korean corporate name;
- listed/unlisted;
- stock code nếu listed;
- parent/group;
- major subsidiaries;
- DART corporation code nếu cần;
- consolidated hay separate reporting perimeter.

Nếu thuộc business group, vẽ tối thiểu một tầng lên và xuống:

```text
Controller / Parent
        ↓
Target company
        ↓
Major subsidiaries
```

Câu hỏi đầu tiên luôn là: **entity nào thật sự ký contract, vay debt và tạo profit?**

## Bước 2 — Revenue engine: ai trả tiền, vì cái gì?

Tách revenue theo segment, geography, customer type và product nếu disclosure cho phép.

Base identity:

\[
Revenue = Volume \times Price
\]

Sau đó hỏi:

- volume tăng vì market growth hay share gain?
- price tăng vì pricing power hay inflation?
- mix shift có làm margin đổi không?
- revenue recurring hay one-off?
- customer concentration cao không?

Không phải mọi industry dùng “volume” theo cùng cách.

Platform: users/transactions.

Bank: loans/assets/deposits/fees.

Construction: project progress/backlog.

Shipbuilding: order execution.

SaaS: subscriptions/ARR.

## Bước 3 — Vẽ value chain và bargaining power

Vẽ:

```text
Key inputs → Company process → Customer → End demand
```

Sau đó đánh dấu:

- supplier concentration;
- customer concentration;
- switching cost;
- substitutes;
- regulation;
- logistics/geography;
- pricing power.

Gross margin thường chỉ hiểu được khi biết company đứng ở đâu trong chain.

Một component supplier có technology tốt nhưng nếu only one customer và buyer dễ switch, pricing power vẫn yếu.

## Bước 4 — Xác định unit economics

Company-level revenue/profit có thể che economics của một unit.

Tìm “unit” phù hợp:

- semiconductor: wafer/bit/yield/ASP;
- airline: passenger-km/load factor/yield;
- platform: transaction/user/take rate;
- SaaS: customer/ARR/churn;
- retailer: store/same-store sales;
- bank: loan/NIM/credit cost;
- construction: project margin/PF exposure.

Nếu không tìm được unit economics, analysis thường vẫn còn quá aggregate.

## Bước 5 — Moat phải có mechanism

**Economic Moat / 경제적 해자** có thể đến từ:

- cost advantage;
- scale;
- technology/yield;
- network effect;
- switching cost;
- brand;
- regulation/license;
- distribution;
- data/process know-how.

Không viết “technology tốt” như conclusion. Hỏi:

```text
Technology tạo value gì cho customer?
↓
Customer có willing to pay không?
↓
Competitor khó copy vì sao?
↓
Advantage có hiện trong margin/share/retention không?
```

Moat không monetize được có thể chỉ là technical excellence.

## Bước 6 — Đọc Income Statement, Balance Sheet và Cash Flow cùng nhau

Income statement cho profitability. Balance sheet cho resources/claims. Cash flow cho cash movement.

Một minimum review:

- revenue growth;
- gross/operating margin;
- receivables/inventory;
- operating cash flow vs net income;
- capex;
- debt and maturity;
- interest expense;
- share count;
- dividends/buybacks.

Ba statements phải reconcile. Profit tăng nhưng cash giảm liên tục cần explanation.

## Bước 7 — Reconcile earnings với cash

Accrual accounting có thể ghi revenue trước cash collection.

Nếu net income tăng nhưng CFO yếu, kiểm tra:

- receivables;
- inventory;
- contract assets;
- one-off gains;
- provisions;
- capitalization.

Một approximation:

\[
Free\ Cash\ Flow \approx CFO - Capex
\]

Nhưng definition phải adjust theo industry. Với bank/insurer, traditional FCF không dùng giống industrial firm.

## Bước 8 — Build 5–10 year financial bridge

Một năm có thể là peak/trough. Tối thiểu hãy normalize nhiều năm:

```text
Revenue
Operating profit
Margin
CFO
Capex
FCF
Debt
Share count
ROIC/ROE
```

Annotate major events:

- acquisition;
- spin-off;
- factory opening;
- cycle peak/trough;
- accounting change;
- major regulation.

Mục tiêu là distinguish **structural change** và **temporary noise**.

## Bước 9 — Cycle vs structure

Korean corporates có nhiều cyclicals: semiconductors, chemicals, steel, shipbuilding, construction, batteries.

Peak earnings có thể làm P/E rất thấp đúng lúc cycle sắp giảm.

Hãy estimate **normalized earnings / 정상화 이익** thay vì extrapolate một year.

Câu hỏi:

```text
Profit tăng vì:
Cycle?
FX?
Input cost?
Market share?
Technology?
Capacity?
Pricing power?
```

Mỗi driver có persistence khác nhau.

## Bước 10 — Balance sheet và hidden leverage

Headline borrowings chưa chắc là total economic leverage.

Đọc footnotes về:

- leases;
- guarantees;
- PF commitments;
- factoring;
- derivatives;
- unconsolidated affiliates;
- pension obligations;
- related-party receivables.

Một company có debt thấp nhưng large guarantees vẫn có tail risk.

Xem [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md).

## Bước 11 — Governance: entity interest có trùng group interest không?

Xem:

- controlling shareholder;
- related parties;
- board composition;
- treasury shares;
- mergers/spin-offs;
- intercompany transactions;
- succession issues.

Với chaebol affiliate, câu hỏi đặc biệt quan trọng:

> Decision này tối ưu lợi ích của target entity hay chủ yếu phục vụ group/control architecture?

Không mặc định conflict; chỉ cần tách hai levels.

## Bước 12 — Capital allocation

Operating cash flow có thể đi vào:

```text
Maintenance CAPEX
Growth CAPEX
R&D
M&A
Debt repayment
Dividend
Buyback
Cash reserve
```

Management quality thể hiện rõ qua pattern nhiều năm.

Growth chỉ tạo value nếu return trên capital mới vượt cost of capital.

Một approximation:

\[
ROIIC \approx \frac{\Delta NOPAT}{\Delta Invested\ Capital}
\]

Nếu company reinvest rất nhiều nhưng incremental NOPAT thấp, revenue growth có thể destroy value.

## Bước 13 — Management narrative phải convert thành measurable variables

IR deck nói “AI, EV, green, global” chỉ là narrative.

Chuyển thành variables:

```text
Capex bao nhiêu?
Capacity bao nhiêu?
Ramp khi nào?
Customer nào?
Utilization giả định?
ASP / margin?
Required ROIC?
```

Nếu narrative không map được vào cash flow, coi nó là **hypothesis**, không phải fact.

## Bước 14 — Tách Fact, Management Claim và Inference

Research note nên đánh dấu ba tầng:

**Fact:** filing nói capex 5 nghìn tỷ KRW.

**Management claim:** capex sẽ tạo leadership.

**Inference:** utilization phải đạt X để project return vượt hurdle rate.

Trộn ba tầng này là nguồn confirmation bias lớn.

## Bước 15 — Compare đúng peer và đúng tầng value chain

Không compare whole Samsung Electronics với TSMC chỉ vì đều “semiconductor”.

Compare:

- memory với memory;
- foundry với foundry;
- cathode producer với cathode producer;
- cell maker với cell maker;
- SI vendor với SI vendor;
- internet bank với relevant bank/fintech peers.

Peer comparison chỉ có meaning khi economics tương đồng.

## Bước 16 — Macro exposure matrix

Map company với:

- KRW/USD;
- BOK rate;
- oil/commodity;
- China/US demand;
- household debt;
- housing;
- semiconductor cycle;
- regulation.

Không cần tất cả. Chọn variables có causal link.

Xem [`21_economy_to_company_transmission.md`](./21_economy_to_company_transmission.md).

## Bước 17 — Valuation sau khi hiểu economics

Không có metric universal.

**P/E** hữu ích khi earnings tương đối normalized/stable.

**P/B + ROE** thường relevant cho financials.

**EV/EBITDA** giúp compare operating assets với capital structures khác nhau.

**DCF** phù hợp khi có thể model cash flows với assumptions explicit.

\[
EV = \sum_{t=1}^{n}\frac{FCF_t}{(1+WACC)^t} + \frac{Terminal\ Value}{(1+WACC)^n}
\]

DCF không tạo certainty. Value lớn nhất là buộc assumptions lộ ra.

Sensitivity table thường hữu ích hơn một target price duy nhất.

## Bước 18 — Reverse valuation

Thay vì hỏi “giá hợp lý bao nhiêu?”, có thể hỏi:

> Current market price đang imply growth/margin/ROIC bao nhiêu?

Đây là **reverse DCF / 역산 DCF**.

Nếu market price yêu cầu margin tăng đến level chưa từng đạt, thesis cần evidence mạnh.

Valuation tốt là test expectation, không chỉ tính number.

## Bước 19 — Stress test

Tạo shocks phù hợp:

```text
Demand -10%
ASP -15%
Input cost +20%
Rate +150bp
KRW move 10%
Customer lost
Plant ramp delay
PF guarantee crystallizes
```

Rồi trace tới cash, covenant và capital raise need.

Stress test nên tập trung variable làm thesis **đổi sign**, không chỉ làm EPS giảm 2%.

## Bước 20 — Thesis breakers

Mỗi analysis nên ghi 2–5 conditions làm thesis sai.

Ví dụ:

- HBM share không tăng;
- new fab utilization <60%;
- top customer chuyển supplier;
- PF guarantee trở thành actual liability;
- regulatory approval fail;
- churn vượt threshold.

Thesis breaker chống sunk-cost/confirmation bias.

## Bước 21 — Pre-mortem

Giả sử sau hai năm analysis sai hoàn toàn.

Hỏi: plausible causes là gì?

```text
Cycle reversal?
Technology substitution?
Customer loss?
Capital misallocation?
Governance?
Regulation?
Funding crisis?
Execution delay?
```

Pre-mortem giúp tìm tail risk trước khi nó thành headline.

## Bước 22 — Employment due diligence nếu mục tiêu là career

Nếu company là nơi định ứng tuyển, thêm layer:

- business-unit stability;
- headcount trend;
- turnover;
- compensation structure;
- promotion system;
- outsourcing ratio;
- project pipeline;
- skill portability;
- manager quality;
- role breadth/depth.

Company financially strong chưa chắc role tốt cho career; company nhỏ chưa chắc learning kém.

Đọc [`12_labor_titles_compensation_and_workplace.md`](./12_labor_titles_compensation_and_workplace.md) và [`13_business_culture_decision_making_and_communication.md`](./13_business_culture_decision_making_and_communication.md).

## Research source hierarchy

Ưu tiên evidence theo thứ tự tương đối:

```text
DART audited filing
↓
KIND / KRX notice
↓
Company IR / earnings call
↓
Regulator / government data
↓
Industry data
↓
News
↓
Community/review
```

Không có nghĩa lower source vô dụng. Employee reviews có thể tốt cho culture signal; news tốt cho context. Nhưng financial fact nên quay về primary source.

## Một reusable research template

```markdown
# Company Name

## 1. Identity & Group Structure
## 2. Historical Context
## 3. Revenue Engine
## 4. Value Chain / Customers / Suppliers
## 5. Unit Economics
## 6. Competitive Advantage
## 7. Financial History
## 8. Cash Flow & Working Capital
## 9. Balance Sheet & Funding
## 10. Governance / Related Parties
## 11. Capital Allocation
## 12. Industry & Macro Exposure
## 13. Valuation / Implied Expectations
## 14. Risks / Stress Test
## 15. Thesis Breakers / Pre-mortem
## 16. Employment View (optional)
## Sources
```

## Mental Model

> Company analysis là process chuyển **brand → legal entity → economic engine → financial machine → governance → expectations**.

Một chain ngắn:

```text
Who controls it?
What does it sell?
Why does customer pay?
Why can't competitor copy?
Where does cash go?
What can break?
What does current price/job offer assume?
```

## Common misconceptions

**“Revenue growth = business tốt hơn.”** Không nếu margin/capital intensity/customer concentration xấu đi.

**“Low P/E = cheap.”** Không nếu earnings đang ở cycle peak.

**“Cash lớn = shareholder value.”** Không nếu capital allocation kém.

**“Chaebol affiliate = parent guarantees everything.”** Sai. Legal entity matters.

**“Good company = good stock.”** Không nếu valuation already prices unrealistic expectations.

**“Good company = good job.”** Không nhất thiết; role/manager/skill path matter.

## Connections

Hầu như toàn bộ library converge vào file này. Khi một assumption chưa rõ, quay lại chapter domain tương ứng thay vì search rời rạc: macro `01`, trade `02`, chaebol `04–05`, SME `06`, governance `08`, disclosure `09`, funding `11`, industries `14–18`, policy `26`, demographics/productivity/innovation `27–29`.
