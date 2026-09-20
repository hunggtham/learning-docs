# Quy trình nghiên cứu thị trường, nguồn dữ liệu và bản đồ ngành

> Mục tiêu của chương này là biến kiến thức thành **quy trình nghiên cứu có thể lặp lại**. Thay vì đọc tin rồi phản ứng cảm tính, người đọc bắt đầu từ câu hỏi, chọn nguồn dữ liệu phù hợp, phân biệt fact/estimate/opinion, xây driver tree và cập nhật thesis theo lịch rõ ràng.

# Phần I — Bắt đầu bằng câu hỏi

## 1. Question tree

Một nghiên cứu tốt bắt đầu bằng câu hỏi có thể kiểm chứng.

Ví dụ thay vì:

```text
“Semiconductor Hàn Quốc có tốt không?”
```

hãy hỏi:

```text
HBM demand có đang tăng nhanh hơn effective supply không?
→ ASP có được hỗ trợ không?
→ utilization và margin có tiếp tục tăng không?
→ consensus đã phản ánh bao nhiêu?
```

## 2. Câu hỏi phải dẫn tới dữ liệu

Nếu một câu hỏi không chỉ ra dữ liệu nào có thể xác nhận hoặc bác bỏ, nó còn quá mơ hồ.

# Phần II — Thứ tự ưu tiên nguồn

## 3. Source hierarchy

Một thứ tự chung:

```text
Cơ quan quản lý / Sở giao dịch / Ngân hàng trung ương / Cơ quan thống kê
→ Filing / Công bố doanh nghiệp
→ IR / Transcript
→ Data provider chất lượng cao
→ Broker / Research
→ News
→ Social / Community
```

Nguồn cấp dưới vẫn hữu ích cho idea discovery nhưng fact quan trọng nên quay lại nguồn gốc nếu có thể.

## 4. Hàn Quốc

Các nhóm nguồn thường dùng:

- KRX;
- BOK;
- FSC/FSS;
- cơ quan thống kê và thương mại;
- DART/company filings;
- company IR.

## 5. Việt Nam

Các nhóm nguồn thường dùng:

- SSC;
- HOSE/HNX/VSDC;
- SBV;
- cơ quan thống kê;
- hải quan/thương mại;
- company filings/IR.

Tên endpoint hoặc quy định cụ thể có thể thay đổi; cần kiểm tra nguồn chính thức hiện hành.

# Phần III — Fact, estimate và opinion

## 6. Fact

Fact là thông tin đã xảy ra và có thể xác minh, ví dụ doanh thu quý, policy rate hoặc số cổ phiếu.

## 7. Estimate

Estimate là dự báo của analyst, công ty hoặc market consensus.

Estimate phải có timestamp vì nó thay đổi liên tục.

## 8. Opinion

Opinion là cách diễn giải.

Một note tốt không trộn opinion thành fact.

## 9. Assumption

Assumption là đầu vào do chính người nghiên cứu đặt vào model.

Ví dụ:

```text
Base case gross margin = 35%
```

không phải fact nếu chưa xảy ra.

# Phần IV — Driver tree

## 10. Company driver tree

Ví dụ bán dẫn:

```text
End Demand
→ Inventory
→ ASP
→ Utilization
→ Product Mix
→ Gross Margin
→ EPS / FCF
```

## 11. Bank driver tree

```text
Deposit Cost / CASA
→ NIM
→ Loan Growth
→ Pre-Provision Profit
→ Credit Cost
→ Net Income
→ ROE / Book Value
```

## 12. Property driver tree

```text
Legal Progress
→ Presales
→ Collection
→ Construction
→ Handover
→ Revenue / Cash
→ Debt Service
```

# Phần V — Leading và lagging indicators

## 13. Leading indicator

Leading indicator có xu hướng thay đổi trước earnings hoặc economy.

Ví dụ:

- orders;
- inventory;
- deposit rates;
- margin balance;
- export data;
- presales.

## 14. Lagging indicator

Lagging indicator thường xác nhận điều đã diễn ra.

Ví dụ NPL hoặc reported EPS có thể đi sau credit/inventory turning point.

## 15. Không mặc định indicator luôn dẫn

Lead/lag có thể thay đổi theo regime, nên cần kiểm tra lịch sử và cơ chế kinh tế.

# Phần VI — Expectations và revisions

## 16. Giá phản ứng với thay đổi kỳ vọng

Một doanh nghiệp báo EPS rất cao vẫn có thể giảm nếu guidance thấp hơn kỳ vọng.

## 17. Revision breadth

Không chỉ nhìn một company. Nếu nhiều analyst cùng nâng EPS ở nhiều doanh nghiệp trong sector, cycle có thể đang mở rộng.

## 18. What was priced?

Trước event cần ghi:

- valuation;
- consensus;
- recent performance;
- positioning proxy;
- option implied move nếu có.

# Phần VII — Sector map Hàn Quốc

## 19. Semiconductor

Theo dõi:

```text
ASP
Inventory
HBM
Utilization
Capex
Exports
USD/KRW
EPS Revisions
```

## 20. Autos / EV

```text
Global Unit Sales
Mix
Incentives
FX
Inventory
Battery Cost
```

## 21. Batteries

```text
EV Demand
Utilization
Raw Materials
Customer Contracts
Capacity Expansion
```

## 22. Shipbuilding / Industrials

```text
Orderbook
Newbuild Price
Steel / Labor Cost
Delivery
FX
```

## 23. Financials

```text
NIM
Credit Cost
Capital
PF Exposure
Turnover / Brokerage
```

## 24. Platforms / Gaming / Biotech

Cần theo dõi user/monetization, title pipeline hoặc clinical milestone tùy sector.

# Phần VIII — Sector map Việt Nam

## 25. Banks

```text
Credit Growth
NIM
CASA
Group-2 / NPL
Provision Coverage
Capital
Property Exposure
```

## 26. Property

```text
Legal
Presales
Cash Collection
Debt Maturity
Bond Refinancing
Handover
```

## 27. Securities companies

```text
Turnover
Margin Lending
Funding Cost
Proprietary Book
IB
```

## 28. Industrial parks

```text
FDI
Occupancy
Lease Price
Land Bank
Infrastructure
```

## 29. Consumer

```text
Income
Traffic
Ticket
Same-Store Sales
Inventory
Margin
```

## 30. Public investment / materials

```text
Budget
Disbursement
Project Progress
Steel / Cement Demand
Input Cost
```

# Phần IX — FX, flow và breadth dashboard

## 31. FX

Theo dõi USD/KRW và USD/VND cùng nguyên nhân:

- rates;
- external balance;
- oil;
- flows;
- policy.

## 32. Foreign flow

Phân biệt:

```text
Passive Flow
Active Allocation
Risk-Off Reduction
FX Hedge Effect
```

## 33. Breadth

Index tăng nhưng breadth giảm có thể cho thấy leadership hẹp.

## 34. Liquidity

Theo dõi turnover, spread và margin/credit conditions phù hợp từng market.

# Phần X — Earnings workflow

## 35. Trước earnings

Ghi:

```text
Consensus Revenue / EPS
Key KPI Expectation
Valuation
Recent Revisions
Important Questions
```

## 36. Khi earnings ra

Tách:

```text
Reported Number
vs Consensus
vs Prior Guidance
```

Sau đó đi vào driver.

## 37. Sau earnings

Cập nhật:

- model;
- valuation;
- catalyst;
- invalidation;
- confidence level.

# Phần XI — Central-bank workflow

## 38. BOK / SBV event

Trước event:

```text
Current Policy
Consensus
FX
Inflation
Growth
Market Pricing
```

Sau event:

```text
Decision
Statement
Guidance
Rates
FX
Sector Reaction
```

# Phần XII — Fiscal / regulatory workflow

## 39. Announcement không bằng implementation

Một chính sách tích cực cần đi qua:

```text
Announcement
→ Legal Rule
→ Implementation
→ Company-Level Effect
→ Cash Flow
```

## 40. Timestamp rule

Regulation phải ghi ngày hiệu lực và nguồn.

Không dùng knowledge note cũ như current rule nếu chưa kiểm tra.

# Phần XIII — Catalyst và invalidation

## 41. Catalyst

Catalyst là event/data có thể khiến market thay đổi expectation.

## 42. Invalidation

Invalidation là evidence làm mechanism của thesis sai.

Price đi ngược vài phiên chưa chắc là invalidation.

# Phần XIV — Watchlist

## 43. Watchlist không chỉ là ticker list

Mỗi entry nên có:

```text
Ticker / Sector
Thesis
Key Driver
Valuation
Catalyst
Invalidation
Next Data Point
```

## 44. Priority

Chia theo:

- active research;
- waiting for trigger;
- monitoring;
- rejected thesis.

# Phần XV — Daily / weekly / monthly / quarterly cadence

## 45. Daily

Chỉ cập nhật dữ liệu tần suất cao:

- price/FX;
- flows;
- major news;
- event outcomes.

Không viết lại thesis mỗi ngày.

## 46. Weekly

Review:

- breadth;
- sector leadership;
- earnings revisions;
- key commodity/FX;
- upcoming catalysts.

## 47. Monthly

Review macro, valuation, credit/liquidity và sector dashboard.

## 48. Quarterly

Đi sâu filings, earnings model, balance sheet và capital allocation.

# Phần XVI — Decision log

## 49. Trước quyết định

Ghi:

```text
Information Set
Thesis
Expected Return Distribution
Main Risk
Position Size Logic
Invalidation
```

## 50. Sau quyết định

Review decision quality riêng với outcome.

Không sửa lại lý do sau khi biết kết quả.

# Phần XVII — Research notebook

## 51. Cấu trúc cho một security

```text
01_business.md
02_sector_drivers.md
03_financials.md
04_valuation.md
05_events.md
06_thesis_log.md
```

Có thể áp dụng trong Obsidian hoặc repository Markdown.

## 52. Country dashboard

Tách Korea và Vietnam thành dashboard riêng nhưng có một bảng global variables chung.

# Phần XVIII — Bias và data hygiene

## 53. Confirmation bias

Chủ động tìm evidence chống thesis.

## 54. Recency bias

Một quarter tốt không tự động thay structural economics.

## 55. Source copying

Không biến broker narrative thành fact nếu chưa kiểm tra dữ liệu gốc.

## 56. Stale data

Mọi dữ liệu động phải có thời điểm.

# Phần XIX — Research tới position size

## 57. Confidence không đủ

Position size phải xét:

- downside;
- liquidity;
- balance sheet;
- factor overlap;
- uncertainty;
- portfolio exposure.

## 58. Thesis quality và liquidity quality là hai thứ khác nhau

Một thesis rất tốt ở cổ phiếu illiquid vẫn có thể chỉ phù hợp size nhỏ.

# Phần XX — Template research chuẩn

## 59. Company note

```text
Business:
Sector Driver:
Leading Indicators:
Financial Quality:
Balance Sheet:
Valuation:
What is priced:
Catalyst:
Invalidation:
Position Risk:
Next Review:
```

## 60. Country / sector note

```text
Macro Regime:
Rates / FX:
Credit / Liquidity:
Flow / Breadth:
Earnings Revision:
Valuation:
Main Scenario:
Alternative Scenario:
```

## Kết luận

Research tốt không được đo bằng số lượng tin đã đọc mà bằng khả năng trả lời:

```text
Tôi đang cố chứng minh điều gì?
Dữ liệu nào thực sự liên quan?
Nguồn nào đáng tin nhất?
Điều gì đã được price?
Evidence nào sẽ làm tôi đổi ý?
```

Khi quy trình này được lặp lại đều đặn, knowledge library trở thành một **hệ thống ra quyết định** thay vì kho tài liệu thụ động.
