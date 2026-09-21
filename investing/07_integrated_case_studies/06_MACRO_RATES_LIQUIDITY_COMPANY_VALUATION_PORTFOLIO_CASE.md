# Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục

> Đây là worked case dùng **số liệu giả định** để nối toàn bộ chuỗi `macro → rates → liquidity → industry → company → valuation → portfolio`. Mục tiêu không phải dự báo giá hay đưa ra khuyến nghị mua/bán, mà luyện cách biến một cú sốc vĩ mô thành các biến có thể đo trong mô hình doanh nghiệp và danh mục.

## 1. Câu hỏi nghiên cứu

Giả sử thị trường đang kỳ vọng lạm phát tiếp tục giảm và chính sách tiền tệ sẽ nới lỏng trong 12 tháng tới. Sau đó một loạt dữ liệu cho thấy lạm phát dịch vụ dai dẳng hơn dự kiến.

Câu hỏi không phải:

> “CPI cao thì cổ phiếu có giảm không?”

Mà là:

> Cú sốc thay đổi đường đi lãi suất, thanh khoản, chi phí vốn và nhu cầu ngành như thế nào; từ đó FCF, định giá và rủi ro danh mục thay đổi bao nhiêu?

## 2. Trạng thái trước cú sốc

Giả định trước dữ liệu:

```text
Core CPI kỳ vọng: 2,9%
Fed cuts được phản ánh trong 12 tháng: 100 bp
US 2Y: 3,50%
US 10Y: 4,00%
Real 10Y: 1,70%
Investment-grade credit spread: 90 bp
USD/KRW: 1.320
Điều kiện tài chính: tương đối nới
```

Một doanh nghiệp giả định là **nhà cung cấp thiết bị bán dẫn Hàn Quốc** có:

```text
Doanh thu: 1.000
Tỷ trọng doanh thu xuất khẩu: 65%
EBIT margin: 18%
EBIT: 180
Thuế suất tiền mặt: 24%
D&A: 50
Capex: 70
Tăng vốn lưu động: 20
Nợ: 300
Tỷ lệ nợ thả nổi hoặc cần tái cấp vốn trong 18 tháng: 50%
Số cổ phiếu pha loãng: 100
```

FCF đơn giản hóa trước cú sốc:

```text
NOPAT = 180 × (1 - 24%) = 136,8
FCF ≈ NOPAT + D&A - Capex - ΔNWC
FCF ≈ 136,8 + 50 - 70 - 20
FCF ≈ 96,8
```

Đây là **điểm xuất phát**, không phải giá trị hợp lý.

## 3. Dữ liệu mới gây bất ngờ

Giả định dữ liệu thực tế:

```text
Core CPI: 3,3%
Dịch vụ lõi: tăng tốc
Tăng trưởng tiền lương: cao hơn dự kiến
PMI sản xuất: suy yếu nhẹ
```

Sau dữ liệu, thị trường tái định giá:

```text
Fed cuts trong 12 tháng: từ 100 bp → 40 bp
US 2Y: +50 bp
US 10Y: +70 bp
Real 10Y: +50 bp
Credit spread: +80 bp
USD/KRW: +7%
```

Đây là một shock hỗn hợp:

```text
Lạm phát dai dẳng hơn
+ discount rate cao hơn
+ USD mạnh hơn
+ tín dụng đắt hơn
+ tăng trưởng công nghiệp yếu đi
```

Vì vậy không thể dùng một dấu `+` hoặc `-` cho toàn bộ cổ phiếu.

## 4. Lớp 1 — Macro: xác định biến thay đổi thật sự

Cú sốc ban đầu là lạm phát, nhưng biến đầu tư quan trọng hơn là **điều gì thay đổi trong distribution của chính sách và tăng trưởng**.

Chuỗi:

```text
Lạm phát dịch vụ dai dẳng
→ ngân hàng trung ương ít dư địa cắt lãi
→ lãi suất thực duy trì cao hơn
→ chi phí vốn tăng
→ điều kiện tài chính chặt hơn
→ nhu cầu và capex có thể giảm với độ trễ
```

Failure mode của cách đọc đơn giản là chỉ nhìn CPI mà bỏ qua PMI suy yếu. Nếu tăng trưởng giảm nhanh hơn, vài tháng sau thị trường có thể chuyển từ “higher for longer” sang “policy easing vì suy thoái”.

## 5. Lớp 2 — Rates: tách đầu ngắn, đầu dài và real yield

US 2Y tăng 50 bp chủ yếu phản ánh thay đổi đường đi kỳ vọng của policy rate.

US 10Y tăng 70 bp có thể gồm:

```text
Kỳ vọng short rate cao hơn
+ real yield cao hơn
+ term premium cao hơn
```

Với tài sản duration dài, real yield tăng 50 bp có thể quan trọng hơn CPI headline.

Đối với trái phiếu có modified duration 7:

```text
%ΔP ≈ -Duration × ΔYield
≈ -7 × 0,007
≈ -4,9%
```

Con số này là xấp xỉ bậc một; convexity, carry và curve shape có thể làm kết quả khác.

## 6. Lớp 3 — Liquidity và credit: tại sao rates shock có thể trở thành funding shock

Credit spread tăng 80 bp cho thấy chi phí vốn doanh nghiệp không chỉ tăng vì risk-free rate.

Nếu trước cú sốc một doanh nghiệp vay ở:

```text
Risk-free tương ứng: 4,0%
Credit spread: 1,0%
→ Cost of debt ≈ 5,0%
```

Sau cú sốc:

```text
Risk-free: 4,7%
Credit spread: 1,8%
→ Cost of debt ≈ 6,5%
```

Chi phí tái cấp vốn tăng khoảng 150 bp.

Với 150 nợ cần tái định giá/tái cấp vốn:

```text
Chi phí lãi tăng gần đúng
= 150 × 1,5%
= 2,25 mỗi năm
```

2,25 không lớn so với EBIT 180, nhưng đây mới là **direct interest effect**. Tác động lớn hơn có thể đến từ khách hàng cắt capex vì WACC tăng và financing khó hơn.

## 7. Failure mode của phân tích thanh khoản

Sai lầm thường gặp:

```text
Credit spread chỉ tăng 80 bp
→ kết luận tác động nhỏ
```

Nhưng cần kiểm tra thêm:

```text
Debt maturity wall
Bank lending standards
Revolver availability
Collateral requirement
Customer financing
Supplier financing
Inventory financing
```

Nếu khách hàng của công ty phụ thuộc vốn vay để mở rộng fab, liquidity tightening có thể tác động vào đơn hàng mạnh hơn chi phí lãi của chính công ty.

## 8. Lớp 4 — Industry: chuyển financial conditions thành capex cycle

Với thiết bị bán dẫn, cầu không chỉ phụ thuộc nhu cầu chip cuối cùng mà còn phụ thuộc kế hoạch capex của fab.

Chuỗi có thể là:

```text
Real yield / WACC ↑
+ demand uncertainty ↑
→ hurdle rate cho dự án fab ↑
→ dự án biên bị trì hoãn
→ equipment order ↓
→ backlog conversion chậm
→ utilization của nhà cung cấp ↓
→ operating leverage âm
```

Dữ liệu cần theo dõi:

```text
Capex guidance của khách hàng lớn
Backlog / book-to-bill
Lead time
Order cancellation / push-out
Utilization
Memory ASP
Inventory days
HBM qualification / advanced packaging demand
```

Không dùng một chỉ tiêu “semiconductor export” để đại diện toàn bộ ngành.

## 9. Lớp 5 — FX: KRW yếu vừa hỗ trợ vừa gây chi phí

USD/KRW tăng 7% thường được mô tả là tích cực cho exporter, nhưng cần nhìn **net FX exposure**.

Giả sử:

```text
65% doanh thu liên quan USD
40% COGS liên quan USD
Một phần capex nhập khẩu bằng USD
20% nợ bằng USD
```

KRW yếu hỗ trợ quy đổi doanh thu nhưng đồng thời tăng chi phí đầu vào, capex và nghĩa vụ nợ ngoại tệ.

Không nên nhân doanh thu với +7%. Hãy xây sensitivity:

```text
FX translation benefit
- imported input cost
- USD debt cost
- hedge effect
= net FX impact
```

Giả định sau phòng vệ, tác động ròng lên doanh thu tương đương khoảng +4%.

## 10. Lớp 6 — Company: xây shock từ driver, không từ EPS

Giả định shock ngành:

```text
Volume / order conversion: -8%
Pricing: +1%
Net FX effect lên revenue: +4%
```

Doanh thu xấp xỉ:

```text
1.000 × 0,92 × 1,01 × 1,04
≈ 966
```

Doanh thu chỉ giảm khoảng 3,4%, nhưng EBIT có thể giảm mạnh hơn do operating leverage.

Giả định EBIT margin từ 18% xuống 15%:

```text
EBIT mới ≈ 966 × 15%
≈ 145
```

So với 180 trước shock:

```text
EBIT giảm gần 19%
```

Đây là lý do doanh thu giảm nhẹ không đồng nghĩa earnings risk nhỏ.

## 11. FCF sau cú sốc

Giả định:

```text
EBIT: 145
Tax: 24%
D&A: 50
Capex: giảm từ 70 xuống 65
ΔNWC: giảm từ 20 xuống 10 do tăng trưởng chậm
```

Tính gần đúng:

```text
NOPAT = 145 × 76% = 110,2
FCF ≈ 110,2 + 50 - 65 - 10
FCF ≈ 85,2
```

FCF giảm từ 96,8 xuống 85,2, tức khoảng 12%.

Điểm đáng chú ý:

```text
Revenue -3,4%
EBIT -19%
FCF -12%
```

Ba con số khác nhau do operating leverage, capex và working capital.

## 12. Kiểm tra bảng cân đối

Trước khi sang valuation, hỏi:

```text
Cash đủ cho bao nhiêu tháng?
Debt maturity tập trung năm nào?
Interest coverage sau shock?
Covenant headroom?
Capex nào là maintenance và capex nào có thể hoãn?
Khách hàng có thể chậm thanh toán không?
```

Nếu EBIT giảm nhưng bảng cân đối vẫn khỏe, vấn đề chủ yếu có thể là valuation/cycle. Nếu refinancing wall gần và covenant mỏng, cùng shock có thể biến thành vấn đề sống sót.

## 13. Lớp 7 — Valuation: tách earnings effect và discount-rate effect

Một sai lầm lớn là chỉ giảm EPS hoặc chỉ tăng WACC. Shock này làm cả hai.

Giả định trước shock:

```text
WACC: 9,0%
Long-term growth: 3,0%
Normalized FCF năm kế tiếp: 100
```

Terminal value đơn giản hóa:

```text
TV = FCF1 / (WACC - g)
= 100 / (9% - 3%)
≈ 1.667
```

Sau shock:

```text
WACC: 10,5%
Long-term growth: 2,5%
Normalized FCF1: 90
```

```text
TV = 90 / (10,5% - 2,5%)
= 90 / 8%
= 1.125
```

Terminal value trong ví dụ giảm khoảng 32,5%.

Đây không phải mục tiêu giá; nó minh họa độ nhạy của valuation khi **cash flow và discount rate cùng xấu đi**.

## 14. Reverse DCF sau shock

Thay vì chỉ hỏi fair value giảm bao nhiêu, hỏi:

> Giá hiện tại đang yêu cầu recovery nhanh tới mức nào?

Kiểm tra ba biến:

```text
Backlog recovery
Normalized EBIT margin
ROIC trên capex mới
```

Nếu giá hiện tại chỉ hợp lý khi margin quay lại 20% rất nhanh và capex khách hàng không giảm, thesis phụ thuộc nhiều giả định đồng thời.

## 15. Multiples: vì sao P/E có thể gây nhầm

Nếu EPS giảm từ 10 xuống 7 nhưng giá chỉ giảm từ 100 xuống 85:

```text
P/E trước = 10x
P/E sau = 12,1x
```

Cổ phiếu “rẻ hơn về giá” nhưng lại **đắt hơn trên earnings mới**.

Với doanh nghiệp chu kỳ cần dùng normalized earnings, EV/EBITDA mid-cycle, DCF hoặc reverse DCF thay vì trailing P/E đơn lẻ.

## 16. Lớp 8 — Portfolio: nhìn factor exposure trước ticker

Giả định danh mục:

```text
Global equity ETF: 35%
Korea equity ETF: 20%
Semiconductor ETF: 15%
Korean equipment company: 10%
Long-duration bonds: 10%
Gold: 5%
Cash: 5%
```

Nhìn theo ticker có vẻ đa dạng. Nhìn theo factor:

```text
Growth / equity beta: cao
Real-yield duration: cao
Semiconductor cycle: rất cao
KRW / Korea: cao
Liquidity stress: trung bình-cao
```

Cú shock real yield + credit + USD có thể làm nhiều vị thế cùng giảm.

## 17. Portfolio stress có số liệu

Giả định trong shock:

```text
Global equity ETF: -12%
Korea equity ETF: -15%
Semiconductor ETF: -22%
Equipment company: -28%
Long-duration bonds: -5%
Gold: +3%
Cash: 0%
```

Tác động gần đúng:

```text
35% × -12% = -4,20%
20% × -15% = -3,00%
15% × -22% = -3,30%
10% × -28% = -2,80%
10% × -5%  = -0,50%
5% × +3%   = +0,15%
5% × 0%    = 0%
```

Tổng stress loss gần đúng:

```text
≈ -13,65%
```

Điểm cần học không phải con số -13,65%, mà là **10% company position chỉ là một phần; concentration thật nằm trong common factors**.

## 18. Hedge phải khớp factor

Nếu mục tiêu chỉ là giảm equity beta, index future có thể hữu ích.

Nếu mục tiêu là giảm duration/rate risk, equity hedge có thể không đủ.

Nếu mục tiêu là giảm KRW risk, cần FX hedge.

Nếu mục tiêu là bảo vệ tail loss nhưng giữ upside, options có thể phù hợp về cơ chế nhưng phải tính premium, skew, expiry và basis risk.

Không tồn tại “hedge tốt nhất” độc lập với risk cần hedge.

## 19. Failure mode của hedge

Một hedge có thể thất bại khi:

```text
Basis thay đổi
Correlation breakdown
Hedge ratio sai
Expiry không khớp horizon
Liquidity biến mất
Option IV quá đắt
FX exposure thực khác exposure ước tính
```

Do đó case study phải ghi cả **hedge failure mode**, không chỉ hedge instrument.

## 20. Data dashboard sau cú sốc

Theo dõi theo tầng:

```text
Macro:
CPI composition, wages, PMI

Rates:
2Y, 10Y, real yield, breakeven, term premium

Liquidity/Credit:
credit spread, lending standards, repo/funding stress

Industry:
memory ASP, inventory, capex guidance, equipment orders

Company:
backlog, revenue mix, margin, working capital, debt maturity

Valuation:
WACC, normalized FCF, reverse DCF assumptions

Portfolio:
factor exposure, stress loss, liquidity bucket, hedge effectiveness
```

Đây là dashboard để **cập nhật xác suất**, không phải để tìm một indicator dự báo hoàn hảo.

## 21. Phân biệt dữ kiện, ước tính và giả định

Ví dụ:

```text
US 10Y +70 bp                    → dữ kiện quan sát
Equipment order sẽ giảm 8%      → ước tính
EBIT margin sẽ xuống 15%         → giả định mô hình
WACC mới là 10,5%                → giả định định giá
Portfolio shock loss -13,65%     → kết quả kịch bản
```

Nếu trộn năm lớp này, research note dễ tạo cảm giác chắc chắn giả.

## 22. Counterfactual: điều gì nếu thesis macro đúng nhưng cổ phiếu vẫn tăng?

Có thể xảy ra nếu:

```text
HBM/AI demand mạnh hơn nhiều
Backlog được bảo vệ bởi hợp đồng
FX benefit lớn hơn dự kiến
Competitor gặp sự cố nguồn cung
Market share tăng
Valuation trước shock đã rất thấp
```

Do đó `macro đúng` không đồng nghĩa `company call đúng`.

## 23. Counterfactual ngược lại

CPI có thể nhanh chóng giảm lại nhưng công ty vẫn yếu nếu:

```text
Khách hàng cắt capex vì dư công suất
Mất market share
Yield kém
Product qualification chậm
Working capital xấu
Governance / capital allocation yếu
```

Case study tích hợp phải giữ **company-specific risk** độc lập với macro.

## 24. Invalidation theo từng tầng

```text
Macro invalidation:
Lạm phát dịch vụ giảm nhanh, labor cooling mạnh

Rates invalidation:
Real yield giảm dù policy rate chưa đổi

Liquidity invalidation:
Credit spread co, lending standards nới

Industry invalidation:
Capex guidance và equipment order phục hồi

Company invalidation:
Backlog, margin, market share cải thiện vượt giả định

Valuation invalidation:
Price đã phản ánh bear case sâu hơn mô hình
```

Không nên dùng một điều kiện duy nhất cho toàn thesis.

## 25. Post-mortem và attribution

Sau 3–6 tháng, phân rã:

```text
Macro forecast đúng/sai?
Rate path đúng/sai?
Credit/liquidity đúng/sai?
Industry demand đúng/sai?
Company margin đúng/sai?
Valuation multiple thay đổi vì sao?
Portfolio loss đến từ factor nào?
Hedge giảm được bao nhiêu loss?
```

Một quyết định có thể có outcome tốt nhưng logic sai. Attribution giúp tránh học nhầm từ may mắn.

## 26. Bài tập bắt buộc

Không đọc case rồi dừng. Hãy thay ít nhất ba giả định:

```text
A. Real yield chỉ tăng 10 bp thay vì 50 bp
B. USD/KRW không tăng mà giảm 5%
C. Equipment order tăng 5% nhờ AI capex
```

Sau đó tính lại:

```text
Revenue
EBIT
FCF
WACC / valuation sensitivity
Portfolio stress loss
```

Mục tiêu là thấy **kết quả phụ thuộc giả định nào mạnh nhất**.

## 27. Đầu ra chuẩn

Tạo một note gồm:

```text
01_macro_surprise.md
02_rates_curve.md
03_liquidity_credit.md
04_industry_driver_tree.md
05_company_sensitivity.md
06_valuation_sensitivity.md
07_portfolio_stress.md
08_hedge_failure_map.md
09_postmortem_template.md
```

## 28. Liên kết học tiếp

- [Macro Transmission Lab](../04_economics/07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md)
- [Bonds, Rates and Credit](../02_asset_classes/02_BONDS_RATES_AND_CREDIT.md)
- [Monetary System and Liquidity](../04_economics/04_MONETARY_SYSTEM_LIQUIDITY_AND_CRISIS_TRANSMISSION.md)
- [Korea Market Playbook](../06_markets_korea_vietnam/01_KOREA_MARKET_PLAYBOOK.md)
- [Company Modeling Lab](../03_company_analysis/07_INTEGRATED_COMPANY_MODELING_AND_THESIS_LAB.md)
- [Valuation](../03_company_analysis/03_VALUATION_DCF_AND_MULTIPLES.md)
- [Portfolio Lab](../01_foundations/06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md)
- [Advanced Practice Workbook](../ADVANCED_PRACTICE_WORKBOOK.md)

## Kết luận

Một macro shock chỉ trở thành investment analysis khi nó được truyền xuống:

```text
Macro
→ Rates
→ Liquidity / Credit
→ FX
→ Industry
→ Company
→ Cash Flow
→ Valuation
→ Portfolio
→ Hedge / Execution
→ Attribution
```

Nếu không thể chỉ ra dữ liệu, cơ chế, failure mode và độ nhạy ở từng tầng, phân tích vẫn chỉ là narrative.