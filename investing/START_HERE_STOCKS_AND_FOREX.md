# Bắt đầu từ đây — Cổ phiếu và Forex

> Lộ trình này dành cho người muốn hiểu **sâu nhưng không bị ngợp**. Mỗi ý đi theo thứ tự: nói bằng ngôn ngữ đời thường → viết thành mô hình → làm một ví dụ số → nêu rủi ro và điều kiện sai.

## Cách dùng file này và các file gần đây

Đây là **bản đồ học**, không phải nguồn thay thế cho toàn bộ thư viện:

```text
START_HERE → hiểu trực giác và thứ tự học
Glossary   → tra nhanh thuật ngữ
Risk/Data  → dùng như checklist trước khi phân tích
Template   → ghi đầu ra của một nghiên cứu
Worked case → xem một hồ sơ đã điền
Domain/Lab → đi sâu cơ chế và kiểm thử
Capstone   → nối thành quy trình hoàn chỉnh
```

Khi hai file giải thích cùng một ý, giữ ví dụ đơn giản ở đây và dùng chapter/lab được chỉ định làm nguồn sâu hơn. Không cần đọc tuần tự tất cả file hỗ trợ.

## 1. Bốn câu cần nhớ trước khi học

1. **Cổ phiếu là quyền sở hữu một phần doanh nghiệp.** Lợi nhuận dài hạn đến từ tiền doanh nghiệp tạo ra và phần giá trị của mỗi cổ phiếu tăng lên; giá thị trường có thể đi trước hoặc đi sau kết quả kinh doanh.
2. **Forex là giá tương đối của hai đồng tiền.** Mua EUR/USD nghĩa là mua EUR và bán USD; không thể phân tích một đồng tiền mà bỏ qua đồng tiền đứng bên kia cặp.
3. **Đòn bẩy chỉ thay đổi kích thước lãi/lỗ, không tạo ra lợi thế.** Nó làm số tiền ký quỹ nhỏ hơn so với giá trị danh nghĩa, nhưng không làm mức lỗ tối đa nhỏ đi.
4. **Một quyết định tốt phải nói được mình sai khi nào.** Nếu không có dữ kiện vô hiệu hóa luận điểm, đó mới chỉ là câu chuyện, chưa phải một kế hoạch đầu tư/giao dịch.

Khi gặp thuật ngữ khó, tra [Từ điển dễ hiểu — Cổ phiếu và Forex](./STOCK_FOREX_PLAIN_LANGUAGE_GLOSSARY.md) trước khi đi sâu vào công thức.

Để kiểm tra quy mô vị thế và khả năng sống sót, dùng thêm [Sổ tay quản trị rủi ro — Cổ phiếu và Forex](./STOCK_FOREX_RISK_PLAYBOOK.md).

Khi bắt đầu nghiên cứu một mã hoặc cặp tiền cụ thể, dùng [Quy trình dữ liệu và nghiên cứu — Cổ phiếu / Forex](./STOCK_FOREX_DATA_RESEARCH_WORKFLOW.md).

## 2. Cổ phiếu và Forex khác nhau ở đâu?

Sau khi có bốn câu nền tảng, ta đặt hai thị trường cạnh nhau để tránh dùng sai trực giác. Bảng dưới đây là công cụ đối chiếu: mỗi dòng trả lời cùng một câu hỏi cho cổ phiếu và Forex, từ đó cho thấy vì sao cách đo lợi suất và rủi ro phải khác nhau.

| Câu hỏi | Cổ phiếu | Forex |
|---|---|---|
| Mình đang nắm gì? | Quyền lợi kinh tế trong doanh nghiệp | Một vị thế mua một đồng và bán một đồng |
| Nguồn lợi nhuận chính | Tăng lợi nhuận/FCF trên mỗi cổ phiếu, cổ tức, thay đổi định giá | Biến động tỷ giá, chênh lệch lãi suất và/hoặc carry sau chi phí |
| Câu hỏi trung tâm | Doanh nghiệp sẽ tạo bao nhiêu tiền cho mỗi cổ phiếu? | Đồng tiền nào mạnh hơn tương đối, trong chế độ nào? |
| Rủi ro lớn | Doanh nghiệp yếu, pha loãng, định giá quá cao, tập trung | Đòn bẩy, spread/slippage, gap, margin, financing, tương quan khi khủng hoảng |
| Nhịp thời gian phù hợp | Thường từ nhiều tháng đến nhiều năm | Có thể từ ngắn hạn đến dài hạn, nhưng chi phí và quy tắc phải phù hợp timeframe |
| Bằng chứng cần giữ | Báo cáo, KPI, dòng tiền, định giá, luận điểm | Dữ liệu đúng thời điểm, rule, chi phí, phân phối kết quả, nhật ký thực thi |

Không có cột nào “dễ hơn”. Cổ phiếu khó ở việc hiểu doanh nghiệp và định giá; Forex khó ở tính tương đối, tốc độ thay đổi và kỷ luật rủi ro.

Kết luận của phần so sánh là không có một bộ rule dùng nguyên xi cho cả hai. Vì vậy, lộ trình tiếp theo đi từ nền tảng chung rồi tách thành nhánh cổ phiếu, Forex và cuối cùng nối chúng lại.

## 3. Lộ trình học theo năm tầng

Năm tầng dưới đây là một đường đi có chủ đích. Mỗi tầng tạo prerequisite cho tầng kế tiếp; hãy đọc mục tiêu và bài kiểm tra của tầng trước khi mở hàng loạt chapter để biết mình cần mang theo mental model nào.

### Tầng A — Nền tảng chung

Tầng đầu tiên giải quyết ngôn ngữ chung về lợi suất, rủi ro và bằng chứng. Hãy học nó trước khi chọn sản phẩm để tránh gọi một tài sản “an toàn” chỉ vì giá ít biến động trong một đoạn ngắn.

Đọc [00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md](./00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md) như quy ước chung, sau đó [01_foundations/00_MASTER_FOUNDATIONS_AND_PORTFOLIO.md](./01_foundations/00_MASTER_FOUNDATIONS_AND_PORTFOLIO.md), [01_foundations/01_MONEY_FINANCIAL_SYSTEM_AND_MARKET_MECHANICS.md](./01_foundations/01_MONEY_FINANCIAL_SYSTEM_AND_MARKET_MECHANICS.md) và [01_foundations/04_RISK_MEASUREMENT_PORTFOLIO_ANALYTICS_AND_DECISION_RULES.md](./01_foundations/04_RISK_MEASUREMENT_PORTFOLIO_ANALYTICS_AND_DECISION_RULES.md).

Mục tiêu không phải nhớ công thức. Bạn cần phân biệt được:

- lợi nhuận danh nghĩa và lợi nhuận sau lạm phát;
- biến động (volatility) và khả năng mất tiền vĩnh viễn;
- rủi ro giá, rủi ro thanh khoản, rủi ro đối tác và rủi ro vận hành;
- dữ kiện đã biết, ước tính, giả định và luận điểm.

**Bài kiểm tra:** giải thích bằng ba câu vì sao một tài sản có lợi suất kỳ vọng cao vẫn có thể không phù hợp với tiền cần dùng trong 12 tháng tới.

Khi trả lời được câu hỏi này, bạn đã có nền để bước vào phân tích cổ phiếu, nơi nguồn lợi suất gắn với doanh nghiệp và số cổ phiếu thực tế.

### Tầng B — Cổ phiếu từ quyền sở hữu đến định giá

Nhánh cổ phiếu đi từ quyền lợi pháp lý tới dòng tiền, chất lượng doanh nghiệp và định giá. Đọc đúng thứ tự giúp người mới không nhảy thẳng vào multiple trước khi hiểu mẫu số và cơ chế tạo tiền.

Đọc theo chuỗi:

1. [02_asset_classes/01_STOCKS_ETF_AND_FUNDS.md](./02_asset_classes/01_STOCKS_ETF_AND_FUNDS.md) — mình thực sự sở hữu gì.
2. [03_company_analysis/README.md](./03_company_analysis/README.md) — bản đồ domain và thứ tự các chapter.
3. [03_company_analysis/01_FINANCIAL_STATEMENTS_AND_ACCOUNTING.md](./03_company_analysis/01_FINANCIAL_STATEMENTS_AND_ACCOUNTING.md) — doanh nghiệp tạo doanh thu, lợi nhuận và tiền như thế nào.
4. [03_company_analysis/02_BUSINESS_QUALITY_MOAT_AND_INDUSTRY.md](./03_company_analysis/02_BUSINESS_QUALITY_MOAT_AND_INDUSTRY.md) — lợi thế có thể giữ được không.
5. [03_company_analysis/03_VALUATION_DCF_AND_MULTIPLES.md](./03_company_analysis/03_VALUATION_DCF_AND_MULTIPLES.md) — mức giá hiện tại đòi hỏi giả định gì.
6. [03_company_analysis/07_INTEGRATED_COMPANY_MODELING_AND_THESIS_LAB.md](./03_company_analysis/07_INTEGRATED_COMPANY_MODELING_AND_THESIS_LAB.md) — nối các phần thành một luận điểm có thể review.

#### Ví dụ nhanh: lợi nhuận của cổ đông không phải lợi nhuận tổng của công ty

Ví dụ này làm rõ vì sao số cổ phiếu là một phần của cơ chế lợi suất trên mỗi cổ phiếu. Hãy đọc công thức như một phép kiểm tra giữa lợi nhuận tổng và phần thực sự thuộc về từng cổ đông.

Giả sử công ty có lợi nhuận ròng 100 triệu USD:

```text
10 triệu cổ phiếu pha loãng → EPS = 10 USD
12 triệu cổ phiếu pha loãng → EPS = 8,33 USD
```

Doanh nghiệp vẫn kiếm 100 triệu USD, nhưng phần lợi nhuận trên mỗi cổ phiếu giảm vì bị pha loãng. Vì vậy cần theo dõi **tăng trưởng trên mỗi cổ phiếu**, không chỉ doanh thu hoặc lợi nhuận tổng.

#### Cách đọc một cổ phiếu dễ hơn

Sau ví dụ pha loãng, ta chuyển từ phép tính sang chuỗi câu hỏi nghiên cứu. Bốn câu hỏi dưới đây nối mô hình kinh doanh, economics, định giá và invalidation thành một hồ sơ có thể review.

Hãy trả lời theo đúng thứ tự:

1. Công ty bán gì, cho ai, và thu tiền bằng cách nào?
2. Một đơn vị doanh thu tạo ra bao nhiêu lợi nhuận và tiền mặt?
3. Động lực nào làm doanh thu, biên lợi nhuận hoặc số cổ phiếu thay đổi?
4. Giá hiện tại đang giả định tăng trưởng, biên lợi nhuận và rủi ro ra sao?
5. Dữ kiện nào sẽ khiến mình giảm vị thế hoặc thừa nhận luận điểm sai?

### Tầng C — Forex từ cặp tiền đến rủi ro thực thi

Nhánh Forex bắt đầu bằng quan hệ giữa hai đồng tiền rồi đi tới pip, margin, expectancy và execution. Đừng mở đầu bằng pattern; hãy hoàn thành phép tính một trade bằng tiền trước khi thêm backtest hoặc regime.

Đọc theo chuỗi:

1. [05_trading_derivatives/README.md](./05_trading_derivatives/README.md) — bản đồ domain và thứ tự các chapter.
2. [05_trading_derivatives/00_MASTER_TRADING_FOREX_RISK.md](./05_trading_derivatives/00_MASTER_TRADING_FOREX_RISK.md) — cơ chế giao dịch và từ vựng.
3. [04_economics/00_BRIDGE_COMPANY_TO_MACRO.md](./04_economics/00_BRIDGE_COMPANY_TO_MACRO.md) — nối dữ liệu vĩ mô với doanh nghiệp và tỷ giá.
4. [04_economics/03_MACRO_DATA_PLAYBOOK.md](./04_economics/03_MACRO_DATA_PLAYBOOK.md) — dữ liệu nào làm thay đổi kỳ vọng.
5. [05_trading_derivatives/02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md](./05_trading_derivatives/02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md) — kiểm thử để không nhầm một câu chuyện đẹp với edge.
6. [05_trading_derivatives/06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md](./05_trading_derivatives/06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md) — sizing, margin, thực thi và kill switch.

#### Ví dụ nhanh: pip, quy mô và đòn bẩy

Ví dụ này biến một biến động trên chart thành lãi/lỗ và số tiền ký quỹ. Mục đích là tách notional, margin và maximum loss trước khi bạn đọc công thức sizing.

Giả sử mua `10.000 EUR/USD` tại `1,1000` và đóng tại `1,1050`:

```text
Biến động = 50 pip
Giá trị gần đúng = 50 pip × 1 USD/pip = 50 USD
```

Nếu broker yêu cầu ký quỹ 2%, số tiền bị khóa khoảng `220 USD` cho notional `11.000 USD`. Con số 220 USD **không phải** mức lỗ tối đa. Nếu giá đi ngược 50 pip, lỗ gần 50 USD; nếu gap hoặc biến động tiếp tục, lỗ có thể lớn hơn dự kiến. Spread, slippage và financing còn làm kết quả xấu đi.

#### Công thức sizing nên đi từ mức lỗ, không đi từ leverage

Sau khi biết một giao dịch có thể mất bao nhiêu, ta đảo ngược bài toán để tìm quy mô. Công thức dưới đây chỉ có ý nghĩa khi pip value, stop và risk budget đã được kiểm tra theo đúng sản phẩm.

```text
Mức rủi ro cho phép = Equity × % rủi ro mỗi giao dịch
Quy mô vị thế ≈ Mức rủi ro cho phép / (Khoảng stop × giá trị mỗi pip)
```

Ví dụ tài khoản 5.000 USD, rủi ro 0,5% và stop 25 pip:

```text
Mức lỗ cho phép = 5.000 × 0,5% = 25 USD
Nếu 10.000 EUR/USD ≈ 1 USD/pip → quy mô khoảng 10.000 EUR
```

Đây là ví dụ minh họa, không phải mức giao dịch được khuyến nghị. Giá trị pip thay đổi theo cặp tiền, quy mô, đồng tiền tài khoản và tỷ giá.

### Tầng D — Nối cổ phiếu với Forex

Khi hai nhánh đã đứng vững, tầng D nối tỷ giá với doanh thu, chi phí, bảng cân đối và định giá. Đây là nơi người học kiểm tra quan hệ nhân quả liên thị trường thay vì dừng ở câu “đồng tiền mạnh là tốt/xấu”.

Khi đã hiểu từng thị trường, chuyển sang các câu hỏi liên thị trường:

- Lãi suất thực và kỳ vọng chính sách ảnh hưởng đồng thời đến định giá cổ phiếu và tỷ giá như thế nào?
- Một cổ phiếu niêm yết bằng KRW nhưng doanh thu bằng USD đang chịu những lớp FX nào?
- Lợi nhuận cổ phiếu bằng VND/KRW có thay đổi thế nào khi quy đổi sang đồng tiền mục tiêu?
- Phòng vệ FX làm giảm rủi ro nào, nhưng thêm carry, basis và chi phí nào?

Đọc [02_asset_classes/05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md](./02_asset_classes/05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md) và [06_markets_korea_vietnam/05_CROSS_BORDER_INVESTING_CURRENCY_TAX_WRAPPERS_AND_MARKET_ACCESS.md](./06_markets_korea_vietnam/05_CROSS_BORDER_INVESTING_CURRENCY_TAX_WRAPPERS_AND_MARKET_ACCESS.md).

Để kiểm tra chuỗi hoàn chỉnh, làm [Case USD funding và FX Hàn Quốc–Việt Nam](./07_integrated_case_studies/07_USD_FUNDING_FX_KOREA_VIETNAM_CROSS_BORDER_CASE.md) sau khi đã hiểu từng nhánh riêng.

### Tầng E — Bài tập có đầu ra

Đọc xong chưa phải là hoàn thành. Tầng cuối biến kiến thức thành hai hồ sơ có thể kiểm tra, trong đó mỗi luận điểm phải có dữ kiện, kịch bản, sizing và điều kiện vô hiệu hóa.

Không chuyển sang sản phẩm thật chỉ vì đã đọc xong. Hãy tạo hai hồ sơ ngắn:

**Hồ sơ cổ phiếu (1–2 trang):** mô hình kinh doanh, 3 động lực chính, bảng cân đối, pha loãng, định giá cơ sở/tích cực/tiêu cực, catalyst, invalidation, rủi ro thanh khoản và lý do không mua.

**Hồ sơ Forex (1–2 trang):** cặp tiền, hướng vị thế, luận điểm tương đối, dữ liệu dẫn dắt, regime, entry/invalidation/exit, quy mô theo mức lỗ, spread/slippage/financing, rủi ro sự kiện và kill switch.

Dùng [Mẫu ghi chú nghiên cứu — Cổ phiếu / Forex](./STOCK_FOREX_RESEARCH_TEMPLATE.md) để không bỏ sót các lớp trên.

Xem [Hồ sơ mẫu đã điền — Cổ phiếu xuất khẩu và Forex](./STOCK_FOREX_WORKED_EXAMPLE.md) nếu bạn muốn xem một bản hoàn chỉnh trước khi tự viết.

Sau hồ sơ mẫu, làm [Module 3 — Company Analysis](./ADVANCED_PRACTICE_WORKBOOK.md) hoặc [Module 5 — Trading & Derivatives](./ADVANCED_PRACTICE_WORKBOOK.md), rồi chuyển sang [Full Investment Process](./07_integrated_case_studies/05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md). Hồ sơ mẫu là cầu nối; capstone mới là nơi kiểm tra toàn bộ quy trình.

Sau mỗi tuần, ghi lại:

```text
Điều mình dự đoán
Điều thực sự xảy ra
Sai ở dữ kiện, cơ chế, thời điểm hay thực thi?
Quy tắc nào cần sửa, và bằng chứng nào cho phép sửa?
```

Khi đã có một hồ sơ cổ phiếu hoặc Forex, chuyển nó vào [Full Investment Process](./07_integrated_case_studies/05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md) để kiểm tra nguồn dữ liệu, định giá, sizing, execution, monitoring và post-mortem trong cùng một quy trình.

## 4. Thứ tự ưu tiên để học sâu mà vẫn dễ hiểu

Mỗi buổi chỉ nên có một câu hỏi lớn:

1. **Cổ phiếu:** “Doanh nghiệp phải làm gì để giá trị trên mỗi cổ phiếu tăng?”
2. **Forex:** “Vì sao đồng tiền A mạnh hơn đồng tiền B trong giai đoạn này?”
3. **Rủi ro:** “Nếu sai, mình mất bao nhiêu và có còn khả năng tiếp tục không?”
4. **Bằng chứng:** “Dữ liệu nào sẽ bác bỏ câu trả lời của mình?”

Không học theo danh sách chỉ báo. Hãy học theo quan hệ nhân quả, sau đó mới chọn chỉ báo đo quan hệ đó.

## 5. Khi nào chưa nên giao dịch Forex hoặc dùng đòn bẩy?

Tạm dừng nếu bạn chưa thể:

- tính lỗ bằng tiền trước khi vào lệnh;
- giải thích margin khác maximum loss;
- mô phỏng spread, slippage, financing và gap;
- nêu giới hạn lỗ ngày/tuần và điều kiện dừng;
- chấp nhận rằng một backtest đẹp không chứng minh edge còn tồn tại.

Với cổ phiếu, tạm dừng nếu bạn chưa thể:

- đọc dòng tiền cùng với lợi nhuận;
- tính ảnh hưởng pha loãng;
- nói giá hiện tại đòi hỏi giả định gì;
- phân biệt doanh nghiệp tốt với cổ phiếu đang có giá quá cao;
- viết điều kiện vô hiệu hóa luận điểm.

## 6. Tóm tắt một trang

Phần này nén toàn bộ mental model thành ba dòng để ôn nhanh. Hãy dùng nó sau khi đã đi qua các tầng, không dùng nó thay cho phần giải thích phía trước.

```text
Cổ phiếu = quyền sở hữu + dòng tiền doanh nghiệp + định giá + pha loãng
Forex    = giá tương đối + chênh lệch kỳ vọng + chi phí thực thi + đòn bẩy
Quyết định tốt = luận điểm rõ + quy mô phù hợp + invalidation cụ thể + review có bằng chứng
```

Các quy tắc về thuế, broker, ký quỹ, sản phẩm CFD/quyền chọn và quyền tiếp cận thị trường có thể thay đổi theo quốc gia và thời điểm. Trước quyết định thật, luôn kiểm tra nguồn chính thức và điều khoản hiện hành.

## 7. Case nối cổ phiếu và Forex: doanh nghiệp xuất khẩu giả định

Giả sử một doanh nghiệp Hàn Quốc có số liệu đơn giản sau. Đây là **bài tập minh họa**, không phải dự báo cho doanh nghiệp cụ thể:

```text
Doanh thu: 100 triệu USD
Chi phí vận hành: 100 tỷ KRW
Tỷ giá ban đầu: 1.300 KRW/USD
Nợ bằng USD: 50 triệu USD
```

### Bước 1 — Chuyển doanh thu sang đồng tiền báo cáo

Ở tỷ giá 1.300:

```text
Doanh thu quy đổi = 100 triệu × 1.300 = 130 tỷ KRW
Lợi nhuận vận hành sơ bộ = 130 - 100 = 30 tỷ KRW
```

Nếu KRW yếu 10% và tỷ giá lên 1.430, trong giả định cực kỳ đơn giản rằng sản lượng, giá bán, chi phí và phòng vệ không đổi:

```text
Doanh thu quy đổi mới = 100 triệu × 1.430 = 143 tỷ KRW
Lợi nhuận vận hành sơ bộ = 143 - 100 = 43 tỷ KRW
```

Nhìn riêng phần hoạt động, lợi nhuận bằng KRW tăng 13 tỷ. Nhưng đây chưa phải kết luận đầu tư.

### Bước 2 — Đưa khoản nợ USD vào cùng một bảng

Giá trị quy đổi của khoản nợ:

```text
Ban đầu: 50 triệu × 1.300 = 65 tỷ KRW
Sau khi KRW yếu: 50 triệu × 1.430 = 71,5 tỷ KRW
```

Phần nợ tăng 6,5 tỷ KRW trước khi tính lãi và các khoản phòng vệ. Lợi ích hoạt động 13 tỷ có thể bị giảm bởi nợ USD, chi phí nhập khẩu, giá nguyên liệu, thuế, hợp đồng phòng vệ hoặc cầu yếu đi vì sản phẩm đắt hơn với khách hàng nước ngoài.

### Bước 3 — Dịch sang câu hỏi về cổ phiếu

Không hỏi đơn giản “KRW yếu là tốt hay xấu?”. Hãy hỏi:

1. Doanh thu và chi phí thực sự ở đồng tiền nào?
2. Khoản nợ và hợp đồng phòng vệ thay đổi ra sao?
3. Tỷ giá đã được thị trường phản ánh vào giá cổ phiếu chưa?
4. Lợi nhuận tăng có chuyển thành dòng tiền và EPS trên mỗi cổ phiếu không?
5. Điều kiện nào làm hiệu ứng tỷ giá đảo chiều?

Đây là cách nối `Forex → doanh thu/chi phí → bảng cân đối → EPS/FCF → định giá`, thay vì dừng ở một câu chuyện vĩ mô.

## 8. Bài tập tự kiểm tra có đáp án gợi ý

### Bài 1 — Cổ phiếu và pha loãng

Doanh thu tăng 10%, lợi nhuận ròng tăng 10%, nhưng số cổ phiếu pha loãng cũng tăng 10%.

**Câu hỏi:** EPS thay đổi gần bao nhiêu nếu mọi thứ khác giữ nguyên?

**Gợi ý:**

```text
EPS mới / EPS cũ ≈ 1,10 / 1,10 = 1,00
```

EPS gần như không tăng. Kết luận cần kiểm tra thêm chất lượng dòng tiền và lý do phát hành cổ phiếu.

### Bài 2 — Forex và chi phí vào lệnh

Bạn mua 10.000 EUR/USD, giá trị khoảng 1 USD/pip. Stop cách điểm vào 30 pip, spread là 1,2 pip.

**Câu hỏi:** trước slippage và financing, rủi ro gần đúng là bao nhiêu nếu stop được khớp đúng?

**Gợi ý:**

```text
Lỗ tại stop ≈ 30 USD
Chi phí spread ≈ 1,2 USD
Tổng gần đúng ≈ 31,2 USD
```

Nếu tài khoản là 5.000 USD, con số này tương đương khoảng 0,624% trước các chi phí khác. Vì vậy không nên gọi “rủi ro 30 pip” là đủ; phải đổi nó thành tiền và tỷ lệ trên equity.

### Bài 3 — Case doanh nghiệp xuất khẩu

Trong case ở trên, lợi nhuận vận hành sơ bộ tăng 13 tỷ KRW nhưng nợ USD tăng 6,5 tỷ KRW.

**Câu hỏi:** có thể kết luận EPS tăng 10% không?

**Đáp án ngắn:** chưa thể. Cần biết lãi vay, thuế, chi phí đầu vào bằng USD, hedge, số cổ phiếu, doanh thu thực tế, giá bán, volume và phần thay đổi đã được thị trường định giá.

## 9. Những cặp khái niệm dễ nhầm

Bảng này là bài kiểm tra phân biệt, không phải danh sách định nghĩa. Với mỗi dòng, hãy tự tạo một ví dụ số hoặc tình huống để chứng minh vì sao hai vế không thể dùng thay cho nhau.

| Dễ nhầm | Cách tách ra |
|---|---|
| Công ty tốt / cổ phiếu tốt | Công ty tốt nhưng giá quá cao vẫn có thể là khoản đầu tư kém |
| Margin / mức lỗ tối đa | Margin là tiền ký quỹ; mức lỗ phụ thuộc quy mô, giá và gap |
| Win rate / expectancy | Win rate cao vẫn lỗ nếu khoản thua trung bình lớn hơn nhiều |
| KRW yếu / cổ phiếu xuất khẩu tăng | Cần tính cả nợ, nguyên liệu, hedge, cầu và định giá đã phản ánh |
| Backtest đẹp / edge thật | Backtest phải vượt qua bias, chi phí, ngoài mẫu và thay đổi regime |
| Volatility thấp / rủi ro thấp | Tài sản ít giao dịch hoặc định giá cũ có thể che giấu rủi ro |
| Cổ tức / lợi nhuận miễn phí | Giá thường điều chỉnh quanh ngày không hưởng quyền; cần nhìn tổng lợi suất |

Nếu chưa giải thích được từng dòng trong bảng bằng một ví dụ số, hãy quay lại tầng tương ứng thay vì nhảy sang sản phẩm phức tạp hơn.

## 10. Kế hoạch 4 tuần, mỗi buổi 30–45 phút

Kế hoạch bốn tuần chuyển lộ trình thành nhịp học có đầu ra. Mỗi tuần có một câu hỏi trung tâm và một sản phẩm cuối tuần; nếu chưa tạo được sản phẩm, hãy lặp lại tầng tương ứng thay vì mở thêm chủ đề.

### Tuần 1 — Nền tảng và ngôn ngữ

Tuần đầu xây vốn từ và cách đo rủi ro chung cho cả hai thị trường. Mục tiêu không phải thuộc nhiều thuật ngữ mà là nói được mình đang sở hữu gì và có thể mất gì.

```text
Buổi 1: đọc bốn câu cốt lõi + glossary
Buổi 2: quyền lợi kinh tế, lợi suất, volatility, drawdown
Buổi 3: margin, leverage, pip, spread, financing
Buổi 4: tự giải thích một ví dụ cổ phiếu và một ví dụ Forex bằng lời của mình
```

**Đầu ra:** một trang “tôi đang sở hữu gì, lợi suất đến từ đâu, rủi ro nằm ở đâu”.

### Tuần 2 — Cổ phiếu

Tuần thứ hai đưa khung chung vào doanh nghiệp: doanh thu, biên, dòng tiền, pha loãng và multiple. Mỗi buổi cần nối một lớp mới với câu hỏi “giá trị trên mỗi cổ phiếu tăng bằng cơ chế nào?”.

```text
Buổi 1: mô hình kinh doanh và driver tree
Buổi 2: doanh thu → biên lợi nhuận → EBIT → FCF
Buổi 3: pha loãng, ROIC, bảng cân đối và working capital
Buổi 4: EPS × multiple, kịch bản và invalidation
```

**Đầu ra:** một hồ sơ cổ phiếu ngắn, chưa cần kết luận mua/bán.

### Tuần 3 — Forex

Tuần thứ ba đưa khung chung vào cặp tiền và thực thi. Hãy ưu tiên phép tính lỗ bằng tiền, rồi mới thử rule paper trade và event filter.

```text
Buổi 1: cặp tiền, base/quote, session và regime
Buổi 2: một giao dịch mẫu từ notional đến lỗ bằng tiền
Buổi 3: expectancy, drawdown, risk of ruin và chi phí
Buổi 4: viết rule paper trade, event filter và kill switch
```

**Đầu ra:** một đặc tả paper trade có entry, stop, sizing, chi phí và điều kiện dừng.

### Tuần 4 — Nối hai thị trường và review

Tuần cuối kiểm tra xem bạn có thể theo một cú sốc từ macro tới tỷ giá, doanh nghiệp và danh mục hay chưa. Post-mortem phải chỉ ra sai ở dữ kiện, cơ chế, timing hay execution.

```text
Buổi 1: hoàn thành worked example doanh nghiệp xuất khẩu
Buổi 2: chọn một case macro → rates → FX → cổ phiếu
Buổi 3: làm lại case với kịch bản bất lợi
Buổi 4: post-mortem: mình sai ở dữ kiện, cơ chế, timing hay execution?
```

**Đầu ra:** một hồ sơ tích hợp có bảng kịch bản và bảng failure mode.

## 11. Cổng hoàn thành trước khi học tiếp

Đây là cổng tự kiểm tra, không phải lời khuyên phải giao dịch. Chỉ chuyển sang công cụ phức tạp hơn khi các năng lực dưới đây đã trở thành phản xạ có thể giải thích bằng số liệu.

Chỉ chuyển sang quyền chọn, CFD, hệ thống tự động hoặc đòn bẩy cao khi bạn có thể:

- giải thích một vị thế bằng tiền, không chỉ bằng phần trăm hoặc pip;
- tính được EPS sau pha loãng và lợi suất sau chi phí cơ bản;
- viết ít nhất một kịch bản làm luận điểm sai;
- phân biệt margin, notional, maximum loss và risk of ruin;
- chỉ ra dữ liệu nào là fact, estimate và assumption;
- review một kết quả mà không đổi câu chuyện chỉ để hợp thức hóa P/L.

Nếu chưa đạt một mục, quay lại đúng tầng còn yếu. Học chậm hơn một chút nhưng có đầu ra sẽ hiệu quả hơn việc mở thêm nhiều sản phẩm cùng lúc.
