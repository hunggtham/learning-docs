# Advanced Practice Workbook — Bài tập thực hành chuyên sâu Investing

> Workbook này dùng sau khi đã đọc các chapter chính và Advanced Lab. Mục tiêu không phải kiểm tra trí nhớ, mà buộc người học **xây mô hình, lượng hóa giả định, kiểm thử phản ví dụ, viết điều kiện vô hiệu hóa và tạo đầu ra có thể review**.

Mỗi module đều có bốn lớp: **bối cảnh → dữ liệu giả định → nhiệm vụ → tiêu chí tự chấm**. Không cần dùng đúng con số dưới đây trong thực tế; chúng được thiết kế để luyện cơ chế.

---

# Module 1 — Foundations: từ mục tiêu tới danh mục có thể sống sót

## Bối cảnh

Một nhà đầu tư có:

```text
Tài sản tài chính: 100 triệu KRW
Tiền mặt: 15 triệu KRW
Thu nhập sau thuế: 4 triệu KRW/tháng
Chi tiêu: 2,4 triệu KRW/tháng
Nghĩa vụ chắc chắn sau 18 tháng: 50 triệu KRW
Nghĩa vụ dự kiến sau 5 năm: 120 triệu KRW
Danh mục hiện tại:
- Cổ phiếu toàn cầu 55%
- Cổ phiếu Hàn Quốc 20%
- Vàng 10%
- Trái phiếu 10%
- Tiền mặt 5%
```

## Nhiệm vụ 1 — Kiểm tra bảng cân đối kinh tế

Không được bắt đầu bằng câu hỏi “nên mua ETF nào”. Hãy lập:

```text
Tài sản thanh khoản
Tài sản tăng trưởng
Vốn con người
Nợ / nghĩa vụ
Đồng tiền của từng nghĩa vụ
Thời gian tới nghĩa vụ
```

Sau đó trả lời: nếu cổ phiếu giảm 35% trong sáu tháng và thu nhập mất trong tám tháng, nghĩa vụ 18 tháng có còn được bảo đảm hay không?

## Nhiệm vụ 2 — Tính mức suy giảm có thể chịu

Giả sử phần tiền cho nghĩa vụ 18 tháng không được phép thiếu quá 5%.

Hãy xác định:

```text
Mức lỗ tối đa chấp nhận được của tầng 18 tháng
Tài sản nào được phép nằm trong tầng này
Tài sản nào phải tách sang tầng dài hạn
```

Điểm quan trọng là **rủi ro phải đo theo thất bại của mục tiêu**, không theo biến động trung bình của danh mục.

## Nhiệm vụ 3 — Ma trận căng thẳng

Tạo ít nhất bốn kịch bản:

```text
A. Lạm phát quay lại:
Cổ phiếu -15%, trái phiếu dài -12%, vàng +5%, USD/KRW +10%

B. Suy thoái:
Cổ phiếu -30%, credit spread +350 bp, trái phiếu chính phủ +10%

C. Khủng hoảng thanh khoản:
Cổ phiếu -25%, vàng -8% ban đầu, spread tăng, thu nhập mất 6 tháng

D. Phục hồi mạnh:
Cổ phiếu +25%, trái phiếu -5%, vàng -10%
```

Với mỗi kịch bản, ghi:

```text
Giá trị danh mục
Nghĩa vụ còn được bảo đảm?
Nguồn rủi ro chính
Tài sản nào thực sự đa dạng hóa?
Quy tắc hành động nào được kích hoạt?
```

## Nhiệm vụ 4 — Reverse stress test

Không hỏi “nếu cổ phiếu giảm 30% thì sao?”. Hãy hỏi:

> Tổ hợp nào khiến kế hoạch mua nhà sau 18 tháng thất bại?

Có thể là:

```text
Mất việc 8 tháng
+ KRW mạnh làm tài sản USD giảm khi quy đổi
+ cổ phiếu giảm 30%
+ phải bán tài sản trong lúc thanh khoản kém
```

## Đầu ra bắt buộc

Tạo một file `portfolio_ips.md` gồm:

```text
Mục tiêu
Nghĩa vụ
Ngân sách rủi ro
Tầng thanh khoản
Tỷ trọng mục tiêu
Dải tái cân bằng
Kịch bản căng thẳng
Điều kiện giảm rủi ro
Điều kiện bán
Chu kỳ review
```

## Tự chấm

Một bài đạt yêu cầu khi quyết định phân bổ có thể giải thích bằng nghĩa vụ và nguồn rủi ro. Nếu lý do chính vẫn là “tài sản này có vẻ sẽ tăng”, bài chưa đạt.

---

# Module 2 — Asset Classes: so tài sản bằng cùng một ngôn ngữ

## Bối cảnh

Bạn đang so bốn lựa chọn:

```text
A. ETF cổ phiếu toàn cầu
B. Trái phiếu chính phủ 10 năm
C. REIT
D. Vàng
```

Giả định:

```text
Cổ phiếu:
Dividend yield 2%
EPS growth dài hạn 5%
Định giá hiện tại cao hơn trung bình lịch sử 15%

Trái phiếu:
Yield 4%
Modified duration 8

REIT:
NOI yield 5,5%
LTV 42%
Chi phí nợ bình quân 4,8%

Vàng:
Không có dòng tiền
Lợi suất thực hiện tại 2%
USD tương đối mạnh
```

## Nhiệm vụ 1 — Phân rã nguồn lợi suất

Với từng tài sản, viết:

```text
Thu nhập hiện tại
Tăng trưởng cơ bản
Thay đổi định giá có thể có
Carry / roll nếu có
Rủi ro mất vốn
Chi phí triển khai
```

Không dùng một con số “expected return” chưa giải thích nguồn.

## Nhiệm vụ 2 — Duration kinh tế

Xếp bốn tài sản theo độ nhạy với:

```text
Lợi suất thực +100 bp
Lạm phát kỳ vọng +100 bp
USD +10%
Suy thoái lợi nhuận
Credit spread +200 bp
```

Giải thích cơ chế chứ không chỉ ghi dấu `+/-`.

## Nhiệm vụ 3 — Trái phiếu

Với duration bằng 8, nếu lợi suất tăng 75 bp, ước lượng biến động giá gần đúng:

```text
%ΔP ≈ -Duration × ΔYield
```

Sau đó cộng carry một năm để xem tổng lợi suất gần đúng. Mục tiêu là hiểu vì sao “yield cao hơn” không đồng nghĩa năm đầu chắc chắn có lợi suất dương.

## Nhiệm vụ 4 — REIT

Giả sử cap rate thị trường tăng từ 5,5% lên 6,5% trong khi NOI không đổi.

Hãy ước lượng tác động tới giá trị tài sản:

```text
Value ≈ NOI / Cap Rate
```

Sau đó thảo luận vì sao đòn bẩy 42% làm giá trị vốn chủ sở hữu biến động mạnh hơn giá trị tài sản.

## Nhiệm vụ 5 — Portfolio role

Mỗi tài sản phải được gán một vai trò:

```text
Tăng trưởng
Ổn định danh nghĩa
Phòng vệ giảm phát
Phòng vệ lạm phát
Thanh khoản
Đa dạng hóa khủng hoảng
```

Một tài sản có thể có nhiều vai trò nhưng phải nói rõ điều kiện nào làm vai trò đó thất bại.

## Đầu ra bắt buộc

Tạo `asset_comparison_matrix.md` với các cột:

```text
Nguồn lợi suất
Duration
Tín dụng
FX
Thanh khoản
Đòn bẩy
Rủi ro đuôi
Regime thuận lợi
Regime bất lợi
Vai trò danh mục
```

## Tự chấm

Nếu bảng chỉ mô tả đặc điểm sản phẩm mà chưa chỉ ra **cơ chế lợi suất và điều kiện thất bại**, bài chưa đạt.

---

# Module 3 — Company Analysis: từ doanh thu tới giá trị trên mỗi cổ phiếu

## Bối cảnh

Một doanh nghiệp giả định có:

```text
Doanh thu năm hiện tại: 1.000
Số đơn vị bán: 100
ASP: 10
Gross margin: 40%
SG&A: 220
R&D: 80
D&A: 50
Capex: 70
Net working capital: 120
Nợ: 300
Tiền mặt: 100
Số cổ phiếu pha loãng: 100
```

## Nhiệm vụ 1 — Driver tree

Không dự báo doanh thu bằng “+10%”. Hãy xây:

```text
Volume
× ASP
× mix
= Revenue
```

Tạo ba kịch bản:

```text
Bear: volume -5%, ASP -3%, margin -300 bp
Base: volume +5%, ASP +2%, margin +100 bp
Bull: volume +10%, ASP +4%, margin +250 bp
```

## Nhiệm vụ 2 — Cầu nối biên lợi nhuận

Giải thích mỗi thay đổi của gross margin đến từ đâu:

```text
Giá bán
Chi phí đầu vào
Mix
Utilization
Yield / năng suất
FX
```

Nếu bạn chỉ nhập gross margin 43% mà không giải thích, mô hình chưa đạt chuẩn.

## Nhiệm vụ 3 — Working capital

Giả sử doanh thu tăng 10% nhưng phải thu tăng 25% và tồn kho tăng 30%.

Hãy giải thích vì sao lợi nhuận có thể tăng trong khi CFO xấu đi. Sau đó kiểm tra DSO/DIO để xem tăng trưởng có hút tiền bất thường hay không.

## Nhiệm vụ 4 — Incremental ROIC

Giả sử công ty đầu tư thêm 100 vốn và tạo thêm 12 NOPAT.

```text
Incremental ROIC = 12 / 100 = 12%
```

Nếu WACC là 9%, tăng trưởng đang tạo giá trị. Sau đó thử kịch bản NOPAT chỉ tăng 6 và giải thích vì sao doanh thu vẫn tăng nhưng giá trị có thể bị phá hủy.

## Nhiệm vụ 5 — Reverse DCF

Không bắt đầu bằng mục tiêu giá. Hãy hỏi:

> Giá hiện tại yêu cầu doanh nghiệp tăng trưởng bao nhiêu năm và duy trì ROIC bao lâu?

Thử ít nhất ba tổ hợp `growth × margin × ROIC fade` và ghi tổ hợp nào cần giả định quá lạc quan.

## Nhiệm vụ 6 — Chất lượng lợi nhuận

Kiểm tra:

```text
Receivables
Inventory
Deferred revenue
SBC
Capex capitalization
Related-party transactions
Debt maturity
Covenant
```

Mỗi mục phải được đánh dấu:

```text
Bình thường
Cần theo dõi
Rủi ro cao
```

## Đầu ra bắt buộc

Tạo:

```text
integrated_model.md
one_page_thesis.md
bear_base_bull.md
valuation_sensitivity.md
thesis_monitoring_log.md
```

## Tự chấm

Một mô hình đạt yêu cầu khi **thay driver vận hành thì ba báo cáo và định giá tự thay đổi hợp lý**. Nếu chỉ thay EPS trực tiếp, mô hình chưa đủ sâu.

---

# Module 4 — Economics: từ dữ liệu tới tái định giá tài sản

## Bối cảnh

Giả sử thị trường trước CPI đang kỳ vọng:

```text
Headline CPI: 2,8%
Core CPI: 3,0%
Fed cuts trong 12 tháng: 100 bp
US 2Y: 3,5%
US 10Y: 4,0%
USD: trung tính
Credit spread: thấp
```

Dữ liệu thực tế:

```text
Headline CPI: 3,1%
Core CPI: 3,3%
Services ex-housing tăng tốc
Wage growth vẫn cao
```

## Nhiệm vụ 1 — Surprise map

Tách:

```text
Mức bất ngờ tiêu đề
Cấu phần gây bất ngờ
Tính dai dẳng
Ảnh hưởng tới reaction function
```

Không được kết luận chỉ bằng `CPI > consensus`.

## Nhiệm vụ 2 — Đường cong

Viết hai phản ứng khác nhau:

```text
A. 2Y tăng mạnh, 10Y tăng ít
B. 10Y tăng mạnh hơn 2Y
```

Giải thích A có thể phản ánh tái định giá Fed, còn B có thể chứa phần bù kỳ hạn/tài khóa/lạm phát dài hạn lớn hơn.

## Nhiệm vụ 3 — Truyền dẫn sang doanh nghiệp

Chọn ba ngành:

```text
Ngân hàng
Cổ phiếu tăng trưởng dài hạn
Doanh nghiệp nợ cao
```

Với mỗi ngành, đi đủ chuỗi:

```text
Rates
→ funding / discount rate
→ earnings
→ valuation
```

## Nhiệm vụ 4 — Kịch bản chính sách

Xây ba kịch bản:

```text
Soft landing + disinflation
Sticky inflation
Hard landing
```

Với mỗi kịch bản, ghi:

```text
Growth
Inflation
Policy rate
2Y / 10Y
USD
Credit spread
Equity earnings
Valuation multiple
```

## Nhiệm vụ 5 — Nowcast dashboard

Chọn 10 chỉ tiêu thuộc:

```text
Lao động
Tiêu dùng
Nhà ở
Sản xuất
Tín dụng
Giá cả
```

Mỗi chỉ tiêu chấm:

```text
+1 tăng tốc
0 ổn định
-1 giảm tốc
```

Không lấy tổng điểm như “mô hình chân lý”; dùng nó để theo dõi thay đổi hướng theo thời gian.

## Đầu ra bắt buộc

Tạo:

```text
macro_nowcast.md
surprise_map.md
regime_matrix.md
policy_reaction_table.md
cross_asset_transmission.md
```

## Tự chấm

Nếu phân tích chỉ nói “tin tốt/tin xấu cho chứng khoán” mà chưa đi qua **kỳ vọng, lãi suất, tín dụng và lợi nhuận**, bài chưa đạt.

---

# Module 5 — Trading & Derivatives: từ giả thuyết tới hệ thống có thể triển khai

## Bối cảnh

Giả sử có ý tưởng:

> Sau một cú phá đáy ngắn hạn rồi đóng cửa trở lại trên vùng hỗ trợ, giá có xu hướng hồi trong 10 cây nến tiếp theo.

## Nhiệm vụ 1 — Formal specification

Phải định nghĩa:

```text
Universe
Timeframe
Định nghĩa “phá đáy”
Định nghĩa “đóng lại trên hỗ trợ”
Entry
Stop
Exit
Holding period
Position sizing
Trading hours
Event filter
Cost model
```

Nếu hai lập trình viên đọc đặc tả mà triển khai khác nhau, đặc tả chưa đạt.

## Nhiệm vụ 2 — Bias audit

Kiểm tra:

```text
Look-ahead
Survivorship
Timestamp
Data revision
Selection bias
Multiple testing
```

Viết một câu giải thích cho cách mỗi bias có thể làm kết quả đẹp giả.

## Nhiệm vụ 3 — Expectancy

Giả sử:

```text
Win rate = 42%
Average win = 1,8R
Average loss = 1R
```

Tính:

```text
E = 0,42 × 1,8 - 0,58 × 1
```

Sau đó trừ `0,12R` chi phí trung bình. Hỏi lợi thế còn đủ lớn so với sai số ước lượng hay không.

## Nhiệm vụ 4 — Robustness

Thử:

```text
Thay tham số ±10–20%
Dịch tín hiệu 1–2 bar
Ngẫu nhiên hóa một phần entry
Chia theo regime
Tăng chi phí 50%
```

Mục tiêu không phải giữ Sharpe đẹp, mà xem logic có sụp hoàn toàn khi điều kiện thay đổi nhẹ không.

## Nhiệm vụ 5 — Sizing và risk of ruin

So ba mức rủi ro mỗi lệnh:

```text
0,25%
1%
3%
```

Mô phỏng chuỗi 10 lệnh lỗ liên tiếp và tính drawdown. Sau đó giải thích tại sao cùng một edge nhưng sizing khác có thể tạo xác suất sống sót hoàn toàn khác.

## Nhiệm vụ 6 — Execution

Giả sử backtest dùng close, nhưng live phải dùng limit order.

Hãy ghi:

```text
Decision price
Arrival price
Fill price
Spread
Delay
Slippage
Missed fill
```

Sau 50 giao dịch, tính thiếu hụt thực thi (implementation shortfall) để xem lợi thế đang mất ở tín hiệu hay ở execution.

## Nhiệm vụ 7 — Kill switch

Định nghĩa điều kiện dừng tự động cho:

```text
Position mismatch
API failure
Daily loss
Margin stress
Slippage bất thường
Data stale
```

## Đầu ra bắt buộc

Tạo:

```text
strategy_spec.md
bias_audit.md
backtest_report.md
execution_report.md
risk_limits.md
live_monitoring.md
retirement_rule.md
```

## Tự chấm

Nếu chiến lược chỉ được mô tả bằng entry/stop/take-profit mà chưa có dữ liệu, chi phí, capacity, operational risk và tiêu chí dừng, bài chưa đạt.

---

# Module 6 — Korea & Vietnam: từ country view tới vị thế cụ thể

## Bối cảnh

Giả sử xảy ra cú sốc:

```text
US 2Y +80 bp
USD mạnh
Oil +15%
China manufacturing yếu
AI capex vẫn tăng
```

## Nhiệm vụ 1 — Korea transmission

Đi đủ chuỗi:

```text
US rates
→ USD/KRW
→ BOK constraint
→ foreign flows
→ semiconductors / KOSDAQ / banks / importers
→ earnings revision
→ valuation
```

Không được kết luận “KRW yếu tốt cho exporter” nếu chưa xét nhu cầu toàn cầu, chi phí nhập khẩu và dòng vốn.

## Nhiệm vụ 2 — Vietnam transmission

Đi đủ chuỗi:

```text
USD mạnh
→ USD/VND pressure
→ SBV room
→ domestic liquidity / credit
→ property / banks / brokers
→ earnings / refinancing
→ valuation
```

Sau đó thêm kênh dầu và China để xem shock chồng lấn.

## Nhiệm vụ 3 — Sector scorecard

Chọn ít nhất 5 ngành ở mỗi nước và chấm:

```text
Growth sensitivity
Rate sensitivity
FX sensitivity
Oil sensitivity
China sensitivity
Liquidity sensitivity
Balance-sheet strength
Valuation
```

Không cộng điểm máy móc; bảng dùng để làm rõ nguồn rủi ro.

## Nhiệm vụ 4 — Earnings revision map

Với mỗi ngành, ghi:

```text
Leading KPI
Consensus direction
Revision breadth
Valuation regime
Catalyst
Invalidation
```

Mục tiêu là phân biệt “câu chuyện tốt” với “kỳ vọng đang được nâng lên thực sự”.

## Nhiệm vụ 5 — Cross-border implementation

Nếu mua sản phẩm từ Hàn Quốc nhưng tài sản cơ sở ở Mỹ hoặc Việt Nam, phải ghi:

```text
Trading currency
Underlying currency
Reporting currency
Liability currency
Wrapper
Domicile
Custody
Tax verification
Settlement
Liquidity
```

## Nhiệm vụ 6 — Position sizing theo thanh khoản

Không dùng cùng tỷ trọng cho KOSPI large-cap và cổ phiếu Việt Nam có free float thấp.

Hãy đặt:

```text
Max position / ADV
Stressed exit days
Price-limit scenario
FX shock
Broker/custody contingency
```

## Đầu ra bắt buộc

Tạo:

```text
korea_dashboard.md
vietnam_dashboard.md
sector_scorecard.md
shock_transmission.md
cross_border_checklist.md
position_risk_sheet.md
```

## Tự chấm

Nếu luận điểm thị trường chỉ dựa vào một headline như “Fed cắt lãi”, “AI tăng” hoặc “Việt Nam tăng trưởng cao”, bài chưa đủ sâu.

---

# Module 7 — Final Review: kiểm tra xem bạn đang học hay chỉ đang đọc

Sau khi hoàn thành sáu module, chọn **một quyết định đầu tư duy nhất** và tạo hồ sơ hoàn chỉnh:

```text
Câu hỏi nghiên cứu
Nguồn dữ liệu
Dữ kiện / ước tính / giả định
Macro regime
Industry map
Company / asset economics
Valuation
Expected return distribution
Risk map
Position size
Execution plan
Monitoring dashboard
Catalyst
Invalidation
Exit / rebalance rule
Attribution plan
Post-mortem template
```

Một hồ sơ tốt phải cho phép người khác đọc và trả lời được:

1. Bạn tin điều gì?
2. Thị trường đang kỳ vọng điều gì?
3. Khoảng cách giữa hai bên nằm ở đâu?
4. Nếu bạn sai, dấu hiệu nào xuất hiện trước?
5. Bạn có thể mất bao nhiêu trước khi luận điểm được kiểm chứng?
6. Thanh khoản và cấu trúc tài khoản có cho phép sống sót tới thời điểm đó không?
7. Sau kết quả, bạn sẽ phân biệt kỹ năng với may mắn thế nào?

## Rubric tự chấm 5 mức

**Mức 1 — Biết thuật ngữ:** giải thích được khái niệm nhưng chưa áp dụng.

**Mức 2 — Áp dụng cơ học:** tính được công thức nhưng chưa hiểu giả định.

**Mức 3 — Phân tích:** nối được nhiều biến và tạo kịch bản.

**Mức 4 — Phản biện:** chủ động tìm phản ví dụ, điều kiện vô hiệu hóa và sai số mô hình.

**Mức 5 — Vận hành:** có quy trình lặp lại, dữ liệu đúng thời điểm, sizing, execution, monitoring và post-mortem.

Mục tiêu của toàn bộ thư viện không phải đạt “Mức 5” ở mọi lĩnh vực ngay lập tức. Mục tiêu là biết rõ mình đang ở mức nào và phần còn thiếu là kiến thức, mô hình, dữ liệu, kỹ năng thực thi hay kỷ luật quyết định.
