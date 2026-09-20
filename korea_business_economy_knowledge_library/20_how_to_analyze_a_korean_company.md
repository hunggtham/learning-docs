# Cách phân tích một công ty Hàn Quốc từ đầu đến cuối (Company Analysis Framework / 한국 기업 분석 프레임워크)

File này là “entry point thực hành”. Khi gặp một company mới—dù là supplier, nơi định ứng tuyển, đối tác dự án hay cổ phiếu—đừng bắt đầu bằng chart giá hoặc review trên cộng đồng. Hãy xây mental model từ legal identity đến economics.

## 1. Xác định đúng entity

Ghi chính xác Korean corporate name, corporation code nếu có, listing code, parent group và status listed/unlisted. Tìm DART/KIND. Nếu company thuộc group, vẽ parent–subsidiary relationship tối thiểu một tầng lên và xuống.

Câu hỏi đầu tiên: **company này thật sự bán gì và ai trả tiền cho nó?**

## 2. Hiểu revenue engine

Tách revenue theo product, segment, geography và customer type nếu disclosure có. Với mỗi segment hỏi:

\[
Revenue = Volume \times Price
\]

Sau đó mở rộng: volume do market growth hay share gain? price do product mix hay inflation? recurring hay one-off?

Đối với platform, volume có thể là users/transactions; bank là loan/assets; construction là progress recognition; shipbuilding là order execution.

## 3. Vẽ value chain

Xác định key inputs → company process → customers. Đánh dấu supplier concentration, customer concentration và substitute.

Nếu không biết company đứng ở đâu trong chain, rất khó hiểu margin.

## 4. Tìm moat

Moat (Economic Moat / 경제적 해자) có thể đến từ scale, switching cost, network effect, technology/yield, brand, regulation, distribution hoặc cost advantage. Mỗi moat cần một mechanism cụ thể.

“Company có công nghệ tốt” chưa đủ. Hỏi: technology đó làm customer tiết kiệm bao nhiêu? khó replicate vì patent, know-how hay capex? advantage có thể monetize thành price/margin không?

## 5. Đọc 3 statements cùng nhau

Income statement cho profit, balance sheet cho resources/claims, cash flow cho movement của cash. Kiểm tra:

- revenue và operating margin trend;
- receivables/inventory so với revenue;
- operating cash flow so với net income;
- capex và free cash flow;
- debt maturity và interest expense;
- share issuance/buyback/dividend.

## 6. Tách cycle khỏi structure

Nếu profit tăng, hỏi do cycle hay moat. Semiconductor price recovery, shipbuilding high-price backlog và FX tailwind có thể nâng earnings mà không đồng nghĩa competitive advantage tăng.

Ngược lại, company đầu tư capacity mới có thể temporarily depress FCF dù long-term economics tốt.

## 7. Governance

Xem largest shareholders, related parties, board, treasury shares và major transactions. Với group affiliate, hỏi decision này có lợi cho entity hay chủ yếu cho group.

## 8. Capital allocation

Lập bảng mental:

```text
Operating Cash Flow
  ├─ Maintenance CAPEX
  ├─ Growth CAPEX
  ├─ M&A / Investments
  ├─ Debt repayment
  ├─ Dividend
  └─ Buyback
```

Management quality được thể hiện ở cách capital đi qua cây này qua nhiều năm.

## 9. Valuation

Valuation chỉ có nghĩa sau khi hiểu business. Chọn metric phù hợp: P/E cho stable earnings, P/B/ROE cho financials, EV/EBITDA cho capital structure comparison, DCF khi có khả năng model cash flow.

DCF core:

\[
Enterprise\ Value=\sum_{t=1}^{n}\frac{FCF_t}{(1+WACC)^t}+\frac{Terminal\ Value}{(1+WACC)^n}
\]

DCF không tạo certainty; nó ép ta làm assumptions explicit. Sensitivity table thường có giá trị hơn một target price duy nhất.

## 10. Stress test

Tạo ít nhất ba shock phù hợp business: demand -10%, FX move, input cost +20%, rate +100bp, customer loss, delay factory ramp hoặc regulation change. Xem variable nào làm thesis gãy.

## 11. Employment due diligence

Nếu mục tiêu là ứng tuyển, thêm layer: revenue stability của business unit, headcount trend, turnover, promotion/pay system, project pipeline, outsourcing ratio và skill portability. Một company financially strong chưa chắc role phù hợp career.

## 0. Đặt company vào historical context

Trước bước “xác định entity”, hãy hỏi company này sinh ra trong phase nào của Korean economy. Một construction group từ reconstruction era có organizational DNA khác platform sinh sau smartphone. Historical origin thường giải thích asset base, debt habit, supplier network và ownership structure hiện tại.

Đọc [00_history/08_company_genealogies](./00_history/08_company_genealogies.md) nếu company thuộc major group.

## 12. Normalize earnings

Korean cyclicals có thể có peak profit làm P/E nhìn rất thấp. Hãy estimate normalized margin/earnings qua cycle thay vì dùng một năm. Với semiconductor, shipbuilding, chemicals, steel, construction và battery, cycle normalization là bắt buộc.

## 13. Kiểm tra segment và geography

Consolidated revenue che differences. Tách segment, customer, country và currency. Nếu 60% profit đến từ một segment dù chỉ 30% revenue, đó mới là economic engine.

## 14. Đọc footnotes trước khi kết luận debt thấp

Leases, guarantees, PF commitments, factoring và unconsolidated affiliates có thể tạo economic leverage ngoài headline borrowings. Related-party receivables cũng có thể là quasi-financing.

## 15. Reverse-engineer management narrative

IR deck nói “AI, EV, green, global” chưa đủ. Chuyển narrative thành measurable variables: capex bao nhiêu, capacity khi nào online, customer contract nào, utilization giả định gì, target ROIC bao nhiêu. Nếu narrative không map được sang cash flow, hãy coi đó là hypothesis chứ không fact.

## 16. So sánh với competitor đúng tầng value chain

Đừng so Samsung Electronics toàn bộ với TSMC chỉ vì đều semiconductor. So foundry với foundry, memory với memory, device với device. Tương tự battery cell maker không compare trực tiếp với cathode-material producer bằng same margin benchmark.

## 17. Thesis breaker

Mỗi analysis nên có 2–4 conditions khiến thesis sai. Ví dụ “HBM share không tăng”, “PF guarantee crystallizes”, “customer concentration loss”, “new plant utilization <60%”. Thesis breaker giúp chống confirmation bias.

## Mental Model

> Phân tích công ty là quá trình chuyển **tên thương hiệu → legal entity → business model → value chain → financial machine → governance → valuation/risk**.

## Một template ngắn để tái sử dụng

```markdown
# Company

## Identity & Group Structure
## Revenue Engine
## Value Chain & Customers
## Competitive Advantage
## Financial Quality
## Balance Sheet & Funding
## Governance
## Capital Allocation
## Industry & Macro Exposure
## Valuation
## Key Risks / Thesis Breakers
## Employment View (nếu cần)
## Sources: DART / KIND / IR / KFTC / KRX
```

## Connections

Hầu như toàn bộ library converge vào file này. Nếu gặp điểm chưa rõ, quay lại đúng domain file thay vì search rời rạc.

## 18. Build một historical financial bridge

Ít nhất 5 năm, normalize revenue, operating profit, capex, free cash flow, debt và share count. Sau đó annotate major events: acquisition, spin-off, cycle peak/trough, accounting change.

Mục tiêu không phải spreadsheet đẹp mà distinguish structural vs temporary change.

## 19. Reconcile profit với cash

Nếu net income tăng nhưng operating cash flow giảm liên tục, hỏi receivables/inventory/contract assets. Accrual earnings có thể lead cash legitimately, nhưng persistent divergence cần explanation.

\[
Free\ Cash\ Flow \approx CFO - Capex
\]

Definition có thể adjust theo industry; luôn ghi convention.

## 20. Calculate return on incremental capital

Company growth chỉ tạo value nếu return trên vốn mới đủ cao.

\[
ROIIC \approx \frac{\Delta NOPAT}{\Delta Invested\ Capital}
\]

Nếu company reinvest 1 nghìn tỷ và after-tax operating profit chỉ tăng rất ít, growth có thể destroy value despite revenue record.

## 21. Map management incentives

Xem controlling shareholder, executive compensation, stock options, succession và related-party exposure. Incentive không chứng minh behavior, nhưng giúp predict likely capital-allocation preference.

## 22. Separate narrative, evidence và inference

Research note nên phân loại:

**Fact**: filing nói capex 5 nghìn tỷ.

**Management claim**: capex sẽ tạo leadership.

**Inference**: utilization phải đạt X để return attractive.

Trộn ba tầng này là nguồn bias lớn.

## 23. Pre-mortem

Giả sử thesis sai sau hai năm. Những nguyên nhân plausible nào? Cycle reversal, customer loss, regulation, capex overrun, governance, technology substitution hay FX?

Pre-mortem buộc analyst tìm downside trước khi bị sunk-cost attachment vào thesis.