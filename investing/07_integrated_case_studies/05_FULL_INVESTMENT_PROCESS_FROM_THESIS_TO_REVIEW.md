# Tình huống tổng hợp 05 — Quy trình đầu tư hoàn chỉnh: từ luận điểm tới đánh giá sau quyết định

> Đây là capstone nối toàn bộ thư viện. Mục tiêu là đi từ một ý tưởng đầu tư đến một quyết định có thể kiểm chứng và sau đó quay lại cải thiện quy trình. Không tập trung vào một mã cụ thể, mà dùng một **doanh nghiệp xuất khẩu chu kỳ niêm yết tại Hàn Quốc hoặc Việt Nam** làm mẫu tư duy. Đây không phải khuyến nghị mua/bán.

## 1. Bắt đầu từ câu hỏi, không bắt đầu từ ticker

Một câu hỏi tốt:

> Thị trường có đang đánh giá sai khả năng phục hồi lợi nhuận của doanh nghiệp trong 12–24 tháng tới không?

Câu hỏi này buộc người phân tích nghiên cứu ba lớp:

```text
Kỳ vọng hiện tại
Cơ chế kinh tế thực
Khoảng cách giữa hai bên
```

Nếu câu hỏi không thể bị bác bỏ bằng dữ liệu, nó chưa phải hypothesis tốt.

## 2. Tách dữ kiện, ước tính, giả định và diễn giải

Mọi research note phải phân biệt:

```text
Dữ kiện (fact)
Ước tính (estimate)
Giả định (assumption)
Diễn giải (interpretation)
Quy tắc quyết định (decision rule)
```

Ví dụ:

```text
US 10Y = 4,5%                    → dữ kiện
Revenue năm tới +8%             → ước tính
EBIT margin phục hồi về 18%      → giả định
Chu kỳ tồn kho đã tạo đáy        → diễn giải
Nếu inventory không giảm 2 quý   → rule / invalidation
```

Trộn các lớp này tạo cảm giác chắc chắn giả.

## 3. Kiểm soát nguồn dữ liệu và tính đúng thời điểm

Với mỗi dữ liệu quan trọng, ghi:

```text
Nguồn
Ngày / kỳ tham chiếu
Publication time
Revision risk
Đây là dữ liệu hiện tại hay point-in-time?
```

Ưu tiên nguồn sơ cấp khi có thể: filing, báo cáo công ty, sở giao dịch, ngân hàng trung ương, cơ quan thống kê và tài liệu pháp lý.

Không được dùng consensus hiện tại để giả lập quyết định quá khứ nếu consensus lịch sử đã thay đổi.

## 4. Xác định thông tin đã được phản ánh trong giá

Trước khi xây mô hình riêng, ghi:

```text
Consensus EPS
Consensus revenue
Current valuation
Recent revisions
Price performance
Sector performance
Positioning proxy nếu có
```

Mục tiêu là tránh phát hiện một điều đúng nhưng đã được thị trường biết hết.

## 5. Xây bản đồ macro có chọn lọc

Không cần phân tích mọi chỉ tiêu. Chỉ giữ các biến ảnh hưởng trực tiếp tới doanh nghiệp:

```text
Global demand
Inflation
Policy path
2Y / 10Y / real yield
USD / local FX
Credit spread
Liquidity / funding
Commodity input
Fiscal / regulatory policy
```

Macro map phải trả lời:

```text
Biến nào là nguyên nhân?
Biến nào chỉ là triệu chứng?
Biến nào dẫn dắt?
Biến nào trễ?
```

## 6. Đi qua rates trước khi nhảy sang cổ phiếu

Một macro shock thường tác động qua lãi suất:

```text
Data surprise
→ policy expectation
→ short-end yield
→ long yield / term premium
→ real yield
→ discount rate
```

Tách ít nhất:

```text
Policy-path effect
Term-premium effect
Inflation-expectation effect
```

Hai lần 10Y tăng 50 bp có thể mang ý nghĩa hoàn toàn khác nếu một lần do tăng trưởng mạnh và một lần do fiscal/term-premium stress.

## 7. Thêm lớp liquidity / credit / funding

Không đủ khi chỉ biết risk-free rate.

Theo dõi:

```text
Credit spread
Bank lending standards
Debt maturity wall
Repo / collateral stress nếu phù hợp
Revolver availability
Foreign-currency funding
Customer financing
Supplier financing
```

Một công ty có ít nợ vẫn có thể chịu shock lớn nếu khách hàng phụ thuộc funding để mua sản phẩm của công ty.

## 8. Xây cây ngành

```text
Demand
→ inventory
→ price
→ utilization
→ margin
→ capex
→ earnings revision
```

Với từng ngành, thay các biến phù hợp. Điều quan trọng là xác định biến **dẫn dắt** và biến **trễ**.

Không dùng một headline ngành thay cho driver tree.

## 9. Xây cây doanh nghiệp

```text
Volume
× Price
× Mix
= Revenue

Revenue
× Margin
= Operating Profit

Operating Profit
- Tax
+ D&A
- Capex
- ΔNWC
= FCF
```

Chuỗi này tạo cầu nối từ dữ liệu vận hành tới dòng tiền.

Nếu không thể giải thích revenue/margin bằng driver, valuation phía sau chỉ là spreadsheet assumption.

## 10. Xây FX map riêng

Với doanh nghiệp xuyên biên giới, tách:

```text
Currency of revenue
Currency of COGS
Currency of capex
Currency of debt
Hedge program
Reporting currency
Investor base currency
```

Không dùng rule `nội tệ yếu = exporter tốt` nếu chưa biết net FX exposure.

## 11. Kiểm tra bảng cân đối trước định giá

Một doanh nghiệp có upside lớn nhưng không đủ thanh khoản để sống tới lúc chu kỳ phục hồi vẫn có thể thất bại.

Kiểm tra:

```text
Cash
Debt maturity
Fixed / floating debt
Interest burden
Covenant
Working capital need
Capex commitments
Collateral
Revolver / unused facilities
```

Phải tạo **liquidity runway** và **refinancing map**, không chỉ Debt/EBITDA.

## 12. Reverse stress test bảng cân đối

Không chỉ hỏi “bear case lỗ bao nhiêu”. Hãy hỏi:

> Tổ hợp điều kiện nào khiến doanh nghiệp phải pha loãng vốn, bán tài sản hoặc vi phạm covenant?

Ví dụ:

```text
Revenue -15%
+ margin -400 bp
+ receivable days +20
+ refinancing cost +250 bp
```

Nếu chỉ một tổ hợp nhẹ đã phá bảng cân đối, valuation upside không còn là vấn đề chính.

## 13. Chuẩn hóa lợi nhuận

Không dùng trực tiếp lợi nhuận đỉnh hoặc đáy chu kỳ.

Xây:

```text
Mid-cycle revenue
Mid-cycle margin
Normalized tax
Maintenance capex
Normalized working capital
Normalized credit loss nếu phù hợp
```

Sau đó mới định giá.

## 14. Kiểm tra chất lượng lợi nhuận

Trước forecast, kiểm tra:

```text
Receivables
Inventory
Accruals
Capitalized cost
SBC / dilution
Provision
Related-party transaction
One-off recurring item
```

Một lợi nhuận “beat” nhưng cash conversion xấu có thể làm thesis khác hoàn toàn.

## 15. Xây ba kịch bản từ driver

```text
Bull:
Demand mạnh hơn + price tốt hơn + utilization cao

Base:
Phục hồi theo consensus nhưng margin tốt hơn nhẹ

Bear:
Demand yếu + inventory cao + refinancing cost tăng
```

Không chỉ đổi P/E giữa ba kịch bản.

Mỗi scenario phải có:

```text
Macro state
Rate state
Liquidity / credit state
Industry driver
Company driver
FCF
Valuation
```

## 16. Định giá bằng nhiều phương pháp phù hợp

Có thể dùng:

```text
DCF
Normalized P/E
EV/EBITDA
SOTP
NAV
Residual income
```

Tùy ngành. Mục tiêu là xem nhiều phương pháp có cùng kể một câu chuyện hay không.

## 17. Tách cash-flow effect và discount-rate effect

Nếu giá trị giảm, phải biết do:

```text
Revenue / margin / FCF thấp hơn
hay
WACC / required return cao hơn
hay
cả hai
```

Đây là cầu nối trực tiếp từ macro/rates sang valuation.

## 18. Reverse DCF

Hỏi:

> Giá hiện tại yêu cầu tăng trưởng, biên lợi nhuận và ROIC như thế nào?

Nếu giá hiện tại đã giả định gần bull case, upside thực có thể thấp dù doanh nghiệp tốt.

Reverse DCF cũng giúp phát hiện khi thị trường đã pricing một bear case rất sâu.

## 19. Chuyển định giá thành phân phối lợi suất

Không chỉ ghi target price.

Ví dụ:

```text
Bull: +45%, xác suất 25%
Base: +18%, xác suất 50%
Bear: -30%, xác suất 25%
```

Sau đó tính expectancy gần đúng nhưng không quên tail risk và sai số xác suất.

Nếu đầu tư xuyên biên giới, chuyển từng scenario sang **đồng tiền cơ sở** bằng FX assumption và chi phí.

## 20. Phân tích rủi ro ngoài mô hình

Một số rủi ro không nằm gọn trong DCF:

```text
Fraud / governance
Liquidity
Policy / legal
FX convertibility
Custody
Gap risk
Key-person
Supply-chain disruption
Cyber / operational
```

Danh sách này phải ảnh hưởng tới uncertainty và quy mô vị thế.

## 21. Kiểm tra tương quan với danh mục hiện có

Một cổ phiếu riêng lẻ có thể tốt nhưng làm danh mục tập trung hơn.

Ví dụ nhà đầu tư đã có:

```text
Korea equity ETF
Semiconductor ETF
Tech-heavy salary exposure
```

thì thêm một semiconductor exporter có thể tăng concentration mạnh.

Phải nhìn theo factor:

```text
Growth
Rates / duration
Credit
USD / KRW / VND
Commodity
Liquidity
China / global demand
```

## 22. Từ conviction tới position size

Không dùng conviction một mình.

Quy mô nên phản ánh:

```text
Expected return
Bear-case loss
Uncertainty
Liquidity
Correlation
Time horizon
Portfolio risk budget
Gap / tail risk
```

Một thesis tốt nhưng thanh khoản kém vẫn có thể cần vị thế nhỏ.

## 23. Sizing bằng stress loss

Một cách thực hành:

```text
Portfolio loss contribution
≈ Position Weight × Stress Return
```

Nếu vị thế 8% có stress return -40%:

```text
Loss contribution ≈ -3,2% danh mục
```

Sau đó hỏi liệu 3,2% có phù hợp risk budget hay không.

## 24. Viết invalidation theo từng tầng trước khi mở vị thế

Ví dụ:

```text
Macro: real yield không đi theo giả định
Industry: inventory không giảm
Company: market share giảm
Balance sheet: refinancing xấu đi
Valuation: price đã phản ánh upside
Portfolio: correlation / concentration vượt ngưỡng
```

Giá giảm không tự động là invalidation; cơ chế sai mới là invalidation.

## 25. Viết catalyst nhưng không phụ thuộc hoàn toàn vào catalyst

Catalyst có thể là:

```text
Earnings surprise
Inventory normalization
Rate / funding change
Policy reform
Product qualification
Asset sale
```

Nhưng thesis phải sống được nếu catalyst chậm hơn dự kiến, miễn liquidity runway đủ.

## 26. Pre-mortem — giả sử quyết định thất bại

Trước thực thi, viết:

> Sáu tháng sau vị thế lỗ lớn. Nguyên nhân hợp lý nhất là gì?

Liệt kê ít nhất năm failure mode:

```text
Macro thesis đúng nhưng company mất share
Rate view sai
Funding stress mạnh hơn dự kiến
Cash conversion xấu
Valuation multiple không mean-revert
FX hedge sai exposure
Liquidity biến mất
```

Pre-mortem giúp tránh một thesis chỉ có đường thắng.

## 27. Lập kế hoạch thực thi

Trước lệnh:

```text
Order type
Desired size
Maximum participation
Price / slippage limit
Liquidity window
Event calendar
Settlement / FX need
```

Với mã thanh khoản thấp, execution có thể ảnh hưởng đáng kể tới return.

## 28. Tách decision price và execution price

Ghi:

```text
Decision price
Arrival price
Actual average fill
Commission
Spread
Slippage
Opportunity cost
```

Sau này có thể phân biệt thesis tốt nhưng execution tệ.

## 29. Nếu dùng phái sinh, theo dõi notional và margin

Đừng nhìn margin như vốn đầu tư thật.

Theo dõi:

```text
Notional
Delta / DV01 nếu phù hợp
Margin requirement
Stress margin
Liquidity buffer
Basis risk
```

## 30. Hedge phải có failure mode

Không chỉ ghi “hedge bằng futures/options/FX forward”. Phải ghi:

```text
Rủi ro nào được hedge?
Hedge ratio?
Horizon?
Basis?
Liquidity?
Cost?
Điều kiện hedge mất hiệu quả?
```

Hedge không khớp factor có thể tạo cảm giác an toàn giả.

## 31. Theo dõi thesis bằng KPI dẫn dắt

Không nhìn giá mỗi ngày để quyết định thesis đúng hay sai.

Theo dõi:

```text
Demand indicator
Inventory
Pricing
Utilization
Orders
Revision breadth
Rates / credit / FX nếu liên quan
Cash conversion
Debt / liquidity
```

Giá là đầu ra của nhiều yếu tố, không phải bằng chứng duy nhất.

## 32. Cập nhật xác suất thay vì đổi hoàn toàn quan điểm

Nếu dữ liệu mới tốt hơn dự kiến:

```text
Bull probability ↑
Bear probability ↓
```

Không cần chuyển ngay từ “bear” sang “bull” tuyệt đối.

Tư duy xác suất giảm phản ứng cảm xúc.

## 33. Earnings review

Sau mỗi quý:

```text
Reported vs estimate
Driver vs estimate
Cash flow
Balance sheet
Guidance
Consensus revision
Valuation
```

Cập nhật model trước khi đọc quá nhiều bình luận thị trường để giảm anchoring.

## 34. Attribution sau một giai đoạn

Phân rã P/L:

```text
Earnings revision
Multiple change
Rates / credit
FX
Sector move
Market beta
Execution cost
Hedge P/L
Position sizing
```

Nếu lời nhờ multiple expansion nhưng thesis earnings sai, không nên tự đánh giá quyết định là hoàn toàn tốt.

## 35. Decision quality khác outcome

Bốn trường hợp:

```text
Quyết định tốt + kết quả tốt
Quyết định tốt + kết quả xấu
Quyết định xấu + kết quả tốt
Quyết định xấu + kết quả xấu
```

Hai trường hợp giữa là nơi học được nhiều nhất.

## 36. Post-mortem

Khi đóng vị thế hoặc khi thesis hết horizon, trả lời:

```text
Điều gì tôi hiểu đúng?
Điều gì tôi hiểu sai?
Thông tin nào tôi bỏ qua?
Model nào sai?
Failure mode nào đã xảy ra?
Position size có hợp lý?
Execution / hedge có tốt?
Tôi có phá rule?
```

Không chỉ ghi profit/loss.

## 37. Cập nhật playbook

Nếu phát hiện lỗi lặp lại, sửa **quy trình**, không chỉ ghi nhớ cảm xúc.

Ví dụ:

```text
Thường bỏ qua debt maturity
→ thêm debt maturity checklist vào mọi company model
```

Đây là cách knowledge library trở thành hệ thống học sống.

## 38. Quality gate cuối

Capstone chỉ được xem là hoàn thành khi trả lời được cả bảy câu:

```text
1. Concept: Tôi đang phân tích cơ chế kinh tế nào?
2. Mechanism: Shock truyền qua các bảng cân đối và dòng tiền nào?
3. Data: Dữ liệu nào xác nhận / bác bỏ và dữ liệu có point-in-time không?
4. Interpretation: Điều gì đã pricing và interpretation thay thế là gì?
5. Risk: Tôi mất bao nhiêu trong bear / stress case?
6. Failure mode: Thesis, hedge và execution có thể thất bại thế nào?
7. Review: P/L sau đó đến từ thesis, beta, multiple, FX hay may mắn?
```

Nếu thiếu một tầng, hồ sơ chưa đạt mức vận hành.

## 39. Bài tập capstone

Chọn một doanh nghiệp hoặc tài sản thực tế và tạo bộ hồ sơ gồm:

```text
00_source_log.md
01_macro_map.md
02_rates_liquidity_map.md
03_sector_driver_tree.md
04_company_model.md
05_balance_sheet_stress.md
06_valuation.md
07_thesis_and_failure_modes.md
08_portfolio_stress_and_sizing.md
09_execution_and_hedge_plan.md
10_monitoring_dashboard.md
11_attribution_postmortem.md
```

Mỗi file phải liên kết với dữ liệu và giả định cụ thể.

## 40. Liên kết tới Advanced Labs và worked cases

- [Thiết kế danh mục nâng cao](../01_foundations/06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md)
- [Định giá tài sản và cấu trúc kỳ hạn](../02_asset_classes/07_ASSET_PRICING_TERM_STRUCTURE_AND_PORTFOLIO_LAB.md)
- [Mô hình doanh nghiệp tích hợp](../03_company_analysis/07_INTEGRATED_COMPANY_MODELING_AND_THESIS_LAB.md)
- [Nowcasting và truyền dẫn vĩ mô](../04_economics/07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md)
- [Thiết kế hệ thống giao dịch](../05_trading_derivatives/06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md)
- [Korea–Vietnam market thesis lab](../06_markets_korea_vietnam/07_KOREA_VIETNAM_MARKET_THESIS_AND_SCENARIO_LAB.md)
- [Worked case: Macro → Rates → Liquidity → Company → Portfolio](./06_MACRO_RATES_LIQUIDITY_COMPANY_VALUATION_PORTFOLIO_CASE.md)
- [Worked case: USD Funding / FX Korea–Vietnam](./07_USD_FUNDING_FX_KOREA_VIETNAM_CROSS_BORDER_CASE.md)

## Kết luận

Quy trình đầu tư hoàn chỉnh là một vòng lặp:

```text
Question
→ Source / Data
→ Macro
→ Rates / Liquidity
→ Industry
→ Company / Asset Economics
→ Valuation
→ Portfolio / Sizing
→ Execution / Hedge
→ Monitoring
→ Attribution
→ Review
→ Process Improvement
```

Mục tiêu cuối cùng không phải luôn đúng. Mục tiêu là xây một quy trình có thể **phát hiện khi sai, giới hạn thiệt hại khi sai, phân biệt thesis với beta/may mắn và học được điều gì sau mỗi quyết định**.