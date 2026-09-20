# Tình huống tổng hợp 05 — Quy trình đầu tư hoàn chỉnh: từ luận điểm tới đánh giá sau quyết định

> Đây là capstone nối toàn bộ thư viện. Mục tiêu là đi từ một ý tưởng đầu tư đến một quyết định có thể kiểm chứng và sau đó quay lại cải thiện quy trình. Không tập trung vào một mã cụ thể, mà dùng một **doanh nghiệp xuất khẩu chu kỳ niêm yết tại Hàn Quốc hoặc Việt Nam** làm mẫu tư duy.

## 1. Bắt đầu từ câu hỏi, không bắt đầu từ ticker

Một câu hỏi tốt:

> Thị trường có đang đánh giá sai khả năng phục hồi lợi nhuận của doanh nghiệp trong 12–24 tháng tới không?

Câu hỏi này buộc người phân tích nghiên cứu ba lớp:

```text
Kỳ vọng hiện tại
Cơ chế kinh tế thực
Khoảng cách giữa hai bên
```

## 2. Xác định thông tin đã được phản ánh trong giá

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

## 3. Xây bản đồ vĩ mô liên quan

Không cần phân tích mọi chỉ tiêu. Chỉ giữ các biến ảnh hưởng trực tiếp tới doanh nghiệp:

```text
Global demand
USD
Domestic currency
Rates
Credit
Commodity input
Policy
```

Ví dụ doanh nghiệp xuất khẩu có thể nhạy hơn với global demand và FX hơn với tiêu dùng nội địa.

## 4. Xây cây ngành

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

## 5. Xây cây doanh nghiệp

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

## 6. Kiểm tra bảng cân đối trước định giá

Một doanh nghiệp có upside lớn nhưng không đủ thanh khoản để sống tới lúc chu kỳ phục hồi vẫn có thể là khoản đầu tư tệ.

Kiểm tra:

```text
Cash
Debt maturity
Interest burden
Covenant
Working capital need
Capex commitments
```

## 7. Chuẩn hóa lợi nhuận

Không dùng trực tiếp lợi nhuận đỉnh hoặc đáy chu kỳ.

Xây:

```text
Mid-cycle revenue
Mid-cycle margin
Normalized tax
Maintenance capex
Normalized working capital
```

Sau đó mới định giá.

## 8. Xây ba kịch bản từ driver

```text
Bull:
Demand mạnh hơn + price tốt hơn + utilization cao

Base:
Phục hồi theo consensus nhưng margin tốt hơn nhẹ

Bear:
Demand yếu + inventory cao + refinancing cost tăng
```

Không chỉ đổi P/E giữa ba kịch bản.

## 9. Định giá bằng nhiều phương pháp phù hợp

Có thể dùng:

```text
DCF
Normalized P/E
EV/EBITDA
SOTP
NAV
```

Tùy ngành. Mục tiêu là xem nhiều phương pháp có cùng kể một câu chuyện hay không.

## 10. Reverse DCF

Hỏi:

> Giá hiện tại yêu cầu tăng trưởng, biên lợi nhuận và ROIC như thế nào?

Nếu giá hiện tại đã giả định gần bull case, upside thực có thể thấp dù doanh nghiệp tốt.

## 11. Chuyển định giá thành phân phối lợi suất

Không chỉ ghi target price.

Ví dụ:

```text
Bull: +45%, xác suất 25%
Base: +18%, xác suất 50%
Bear: -30%, xác suất 25%
```

Sau đó tính expectancy gần đúng và đánh giá downside.

## 12. Phân tích rủi ro ngoài mô hình

Một số rủi ro không nằm trong DCF:

```text
Fraud / governance
Liquidity
Policy
FX convertibility
Custody
Gap risk
Key-person
Supply-chain disruption
```

Danh sách này phải ảnh hưởng tới quy mô vị thế.

## 13. Kiểm tra tương quan với danh mục hiện có

Một cổ phiếu riêng lẻ có thể tốt nhưng làm danh mục tập trung hơn.

Ví dụ người đầu tư đã có:

```text
Korea equity ETF
Semiconductor ETF
Tech-heavy salary exposure
```

thì thêm một semiconductor exporter có thể tăng concentration mạnh.

## 14. Từ conviction tới position size

Không dùng conviction một mình.

Quy mô nên phản ánh:

```text
Expected return
Downside
Uncertainty
Liquidity
Correlation
Time horizon
Portfolio risk budget
```

Một thesis 8/10 nhưng illiquid vẫn có thể cần vị thế nhỏ.

## 15. Viết invalidation trước khi mua

Ví dụ:

```text
ASP không hồi như giả định
Inventory không giảm
Margin không cải thiện
Debt refinancing xấu đi
Market share giảm
```

Giá giảm không tự động là invalidation; cơ chế sai mới là invalidation.

## 16. Viết catalyst nhưng không phụ thuộc hoàn toàn vào catalyst

Catalyst có thể là:

```text
Earnings beat
Inventory normalization
Rate cut
Policy reform
Product qualification
Asset sale
```

Nhưng một tài sản chỉ đáng mua nếu giá trị đủ hấp dẫn ngay cả khi catalyst chậm hơn dự kiến.

## 17. Lập kế hoạch thực thi

Trước lệnh:

```text
Order type
Desired size
Maximum participation
Price limit
Liquidity window
Event calendar
```

Với mã thanh khoản thấp, execution có thể ảnh hưởng đáng kể tới return.

## 18. Tách decision price và execution price

Ghi:

```text
Decision price
Actual average fill
Commission
Spread
Slippage
```

Sau này có thể phân biệt thesis tốt nhưng execution tệ.

## 19. Nếu dùng phái sinh, theo dõi notional và margin

Đừng nhìn margin như vốn đầu tư thật.

Theo dõi:

```text
Notional
Delta / DV01 nếu phù hợp
Margin requirement
Stress margin
Liquidity buffer
```

## 20. Theo dõi thesis bằng KPI dẫn dắt

Không nhìn giá mỗi ngày để quyết định thesis đúng hay sai.

Theo dõi:

```text
Demand indicator
Inventory
Pricing
Utilization
Orders
Revision breadth
Credit / FX nếu liên quan
```

Giá là đầu ra của nhiều yếu tố, không phải bằng chứng duy nhất.

## 21. Cập nhật xác suất thay vì đổi hoàn toàn quan điểm

Nếu dữ liệu mới tốt hơn dự kiến:

```text
Bull probability ↑
Bear probability ↓
```

Không cần chuyển ngay từ “bear” sang “bull” tuyệt đối.

Tư duy xác suất giảm phản ứng cảm xúc.

## 22. Earnings review

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

## 23. Attribution sau một giai đoạn

Phân rã P/L:

```text
Earnings revision
Multiple change
FX
Sector move
Market beta
Execution cost
Position sizing
```

Nếu lời nhờ multiple expansion nhưng thesis earnings sai, không nên tự đánh giá quyết định là hoàn toàn tốt.

## 24. Decision quality khác outcome

Bốn trường hợp:

```text
Quyết định tốt + kết quả tốt
Quyết định tốt + kết quả xấu
Quyết định xấu + kết quả tốt
Quyết định xấu + kết quả xấu
```

Hai trường hợp giữa là nơi học được nhiều nhất.

## 25. Post-mortem

Khi đóng vị thế, trả lời:

```text
Điều gì tôi hiểu đúng?
Điều gì tôi hiểu sai?
Thông tin nào tôi bỏ qua?
Model nào sai?
Position size có hợp lý?
Execution có tốt?
Tôi có phá rule?
```

Không chỉ ghi “profit/loss”.

## 26. Cập nhật playbook

Nếu phát hiện lỗi lặp lại, sửa **quy trình**, không chỉ ghi nhớ cảm xúc.

Ví dụ:

```text
Thường bỏ qua debt maturity
→ thêm debt maturity checklist vào mọi company model
```

Đây là cách knowledge library trở thành hệ thống học sống.

## 27. Bài tập capstone

Chọn một doanh nghiệp thực tế và tạo bộ hồ sơ gồm:

```text
01_macro_map.md
02_sector_driver_tree.md
03_company_model.md
04_valuation.md
05_thesis.md
06_execution_plan.md
07_monitoring_dashboard.md
08_postmortem.md
```

Mỗi file phải liên kết với dữ liệu và giả định cụ thể.

## 28. Liên kết tới Advanced Labs

- [Thiết kế danh mục nâng cao](../01_foundations/06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md)
- [Định giá tài sản và cấu trúc kỳ hạn](../02_asset_classes/07_ASSET_PRICING_TERM_STRUCTURE_AND_PORTFOLIO_LAB.md)
- [Mô hình doanh nghiệp tích hợp](../03_company_analysis/07_INTEGRATED_COMPANY_MODELING_AND_THESIS_LAB.md)
- [Nowcasting và truyền dẫn vĩ mô](../04_economics/07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md)
- [Thiết kế hệ thống giao dịch](../05_trading_derivatives/06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md)
- [Korea–Vietnam market thesis lab](../06_markets_korea_vietnam/07_KOREA_VIETNAM_MARKET_THESIS_AND_SCENARIO_LAB.md)

## Kết luận

Quy trình đầu tư hoàn chỉnh là một vòng lặp:

```text
Question
→ Research
→ Model
→ Valuation
→ Position
→ Execution
→ Monitoring
→ Attribution
→ Review
→ Process Improvement
```

Mục tiêu cuối cùng không phải luôn đúng. Mục tiêu là xây một quy trình có thể **phát hiện khi sai, giới hạn thiệt hại khi sai và học được điều gì sau mỗi quyết định**.