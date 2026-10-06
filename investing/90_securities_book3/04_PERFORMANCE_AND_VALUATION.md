# 4. Đo lường thành quả và định giá doanh nghiệp

CAPM cho ta một mức sinh lợi yêu cầu, nhưng chưa cho biết danh mục thực tế làm tốt đến đâu, cũng chưa nói một doanh nghiệp đáng giá bao nhiêu. Phần này nối hai câu hỏi: đo performance sao cho không bị dòng tiền nạp/rút đánh lừa, rồi chuyển forecast về giá trị hiện tại bằng cash flow và cost of capital.

## 1. Return qua nhiều kỳ

Investment return gồm income và price change: cổ phiếu có dividend + capital gain; trái phiếu có interest + capital gain. Nếu nhà đầu tư nạp/rút tiền giữa các kỳ, hai cách đo có ý nghĩa khác nhau.

**Money-weighted return (금액가중수익률)** là IRR của toàn bộ dòng tiền: tìm \(r\) sao cho giá trị hiện tại của tiền vào bằng giá trị hiện tại của tiền ra. Nó trả lời “với đúng thời điểm số vốn của nhà đầu tư, tài khoản sinh lời thế nào?”. **Time-weighted return (시간가중수익률)** chia lịch sử tại các thời điểm có dòng tiền, tính holding-period return từng đoạn rồi ghép:

\[
R_{TW}=\prod_t(1+r_t)-1.
\]

Trong ví dụ nguồn, mua một cổ phiếu 5.000 won, năm sau mua thêm ở 5.400, cuối kỳ bán hai cổ phiếu ở 5.500 và nhận dividend, money-weighted return là nghiệm IRR khoảng 8%. Time-weighted return ghép hai holding-period return 12% và 5,45% thành khoảng 18,1% cho toàn kỳ; nếu annualize thì geometric mean khoảng 8,68%, còn arithmetic mean là 8,725%. Vì các cách này trả lời câu hỏi khác nhau, không được so sánh chúng như cùng một đại lượng.

Arithmetic mean phù hợp mô tả một kỳ điển hình; geometric mean phù hợp tăng trưởng lũy kế:

\[
1+\bar r_g=\left[\prod_{t=1}^T(1+r_t)\right]^{1/T}.
\]

Với return dương, geometric mean không vượt arithmetic mean; volatility tạo “drag” lên tăng trưởng ghép.

## 2. Ba thước đo risk-adjusted performance

Với portfolio return \(r_p\), risk-free \(r_f\), độ lệch chuẩn \(\sigma_p\) và beta \(\beta_p\):

\[
\text{Sharpe}=\frac{r_p-r_f}{\sigma_p},\qquad
\text{Treynor}=\frac{r_p-r_f}{\beta_p}.
\]

Sharpe dùng tổng rủi ro nên phù hợp khi portfolio là phần lớn tài sản của nhà đầu tư và chưa đa dạng hóa đầy đủ. Treynor chỉ dùng systematic risk nên hợp lý hơn khi portfolio đã đa dạng hóa và được so với market exposure. **Jensen’s alpha** so sánh return thực tế với CAPM required return:

\[
r_p-r_f=\alpha_p+\beta_p(r_m-r_f).
\]

\(\alpha>0\) nghĩa là vượt mức CAPM dự báo sau khi điều chỉnh beta; \(\alpha<0\) là thấp hơn. Ví dụ nguồn có \(r_f=5\%\), market 10%, portfolio 13%, \(\sigma_p=4\%\), market \(\sigma=3\%\), correlation 0,5. Tính beta từ covariance rồi tính cả ba chỉ số cho thấy kết luận có thể khác nhau; phương pháp phải khớp mục tiêu đánh giá, benchmark và mức diversification.

### Worked check: ba chỉ số, ba câu hỏi

Giả sử \(r_f=3\%\), portfolio return 11%, \(\sigma_p=12\%\), beta 1,1, market return 9%. Khi đó Sharpe là \((11-3)/12\approx0,67\), Treynor là \((11-3)/1,1\approx7,27\%\) trên một đơn vị beta, còn Jensen alpha là

\[
11\%-[3\%+1,1(9\%-3\%)]=1,4\%.
\]

Sharpe hỏi danh mục kiếm được bao nhiêu trên **tổng biến động**; Treynor hỏi bao nhiêu trên **market risk**; Jensen hỏi return có vượt CAPM hurdle không. Một portfolio có Sharpe thấp nhưng Jensen dương có thể đang mang nhiều idiosyncratic volatility; một portfolio có Sharpe cao nhưng Jensen âm có thể chỉ đang hưởng lợi từ beta thấp. Không được xếp hạng các portfolio bằng một chỉ số duy nhất khi benchmark và diversification khác nhau.

## 3. Định giá là quy trình, không phải một con số xuất hiện từ multiplier

**Valuation (기업가치평가)** là ước lượng fair market value của doanh nghiệp dựa trên hoạt động, môi trường cạnh tranh và dòng tiền tương lai. Quy trình nguồn gồm: hiểu đặc tính doanh nghiệp và ngành; dự báo môi trường kinh doanh và financial performance; đo cash flow; chọn discount rate; chuyển các dòng tiền tương lai về hiện tại; kiểm tra kết quả bằng phương pháp khác.

Đừng lẫn cash flow kế toán với cash flow dùng cho valuation. Cần xác định cash flow thuộc về ai (firm hay equity), xử lý thuế thực trả, đầu tư tài sản và vốn lưu động; không trộn numerator sau lãi vay với discount rate trước lãi vay. **Cost of capital** là giá phải trả cho vốn; CAPM thường dùng cho cost of equity:

\[
k_e=r_f+\beta_e(E(r_m)-r_f).
\]

Kết hợp debt và equity theo tỷ trọng thị trường cho **WACC**. Tính nhất quán giữa dòng tiền và discount rate là điều kiện, không phải chi tiết phụ.

Nếu dùng FCFF, một dạng thực hành thường viết là \(FCFF=NOPAT+D\&A-Capex-\Delta NWC\), còn FCFE bắt đầu từ net income và điều chỉnh theo net borrowing, Capex và thay đổi vốn lưu động. Đây không phải hai con số để chọn tùy ý: FCFF thuộc về cả debt holder và equity holder nên chiết khấu bằng WACC; FCFE thuộc equity holder nên chiết khấu bằng \(k_e\). WACC minh họa sự khớp đó:

\[
WACC=\frac{E}{D+E}k_e+\frac{D}{D+E}k_d(1-T).
\]

Nếu lấy FCFE nhưng dùng WACC, hoặc lấy FCFF nhưng dùng cost of equity, value bị lệch vì một phần rủi ro/vốn đã bị tính hai lần hoặc bỏ sót.

### EV không phải equity value

DCF theo FCFF cho **enterprise value (EV)** — giá trị hoạt động dành cho tất cả nhà cung cấp vốn. Để đi tới equity value, cần bridge có chủ ý:

\[
Equity\ Value=EV+cash+non\text{-}operating\ assets-debt-minority\ interest-other\ claims.
\]

Không được tự động lấy “EV trừ tổng liabilities”: chỉ những khoản nợ và claim kinh tế cần thanh toán cho equity mới thuộc bridge, còn operating liabilities đã đi vào working capital/FCFF. Nếu doanh nghiệp có pension deficit, preferred stock, lease debt, treasury shares hoặc options pha loãng, phải quyết định chúng nằm ở cash flow, debt adjustment hay share count. Cùng một DCF có thể cho giá mỗi cổ phiếu khác nhau chỉ vì bridge hoặc diluted shares bị bỏ sót.

## 4. DCF, FCFF/FCFE và EVA

**Discounted cash flow (DCF)** định giá bằng:

\[
V_0=\sum_{t=1}^{T}\frac{CF_t}{(1+k)^t}+\frac{TV_T}{(1+k)^T}.
\]

Discount rate tăng hoặc cash flow kỳ vọng giảm thì value giảm; tăng trưởng bền vững, thời gian sống dài hơn và dòng tiền chắc hơn làm value tăng. Terminal value phải nêu rõ giả định tăng trưởng dài hạn, vì một sai lệch nhỏ ở \(k-g\) có thể chi phối toàn bộ kết quả.

FCFF là dòng tiền cho toàn doanh nghiệp, thường chiết khấu bằng WACC; FCFE là dòng tiền cho cổ đông, chiết khấu bằng cost of equity. Dividend discount model là trường hợp đặc biệt cho equity. Với Gordon growth:

\[
P_0=\frac{D_1}{k_e-g}.
\]

Ví dụ nguồn: dividend kỳ tới 2.500 won, \(k_e=15\%\), tăng trưởng 5% vô hạn ⇒ \(P_0=25.000\) won. Điều kiện \(k_e>g\) là ranh giới toán học bắt buộc.

Terminal value cần được kiểm tra bằng hai cách: perpetual growth \(TV_T=FCF_{T+1}/(k-g)\) và exit multiple dựa trên peer. Nếu 70% giá trị DCF đến từ terminal value, kết luận “cổ phiếu rẻ” thực chất đang phụ thuộc vào vài điểm phần trăm của \(g\), \(k\) và margin dài hạn. Vì vậy nên lập sensitivity table theo \(k\) và \(g\), không chỉ trình bày một điểm base case.

### Worked check: terminal value không được để trong bóng tối

Giả sử một công ty có FCFF năm 1–3 lần lượt là 100, 110 và 121; WACC là 10%, tăng trưởng dài hạn là 3%. Khi đó \(TV_3=121\times1,03/(0,10-0,03)\approx1.780\). Giá trị hiện tại xấp xỉ \(90,9+90,9+90,9+1.780/1,1^3=1.610\) đơn vị. Nếu chỉ đổi \(g\) xuống 2%, tổng value còn khoảng 1.432; nếu đổi lên 4%, value tăng lên khoảng 1.848. Khoảng dao động này không phải sai số máy tính: nó cho thấy terminal assumption đang mang phần lớn rủi ro mô hình.

Khi lập forecast, hãy tách ba lớp: doanh thu/margin tạo ra FCFF, reinvestment tạo ra tăng trưởng, và WACC phản ánh risk/capital structure. Nếu tăng trưởng cao nhưng không có reinvestment hoặc ROIC vượt WACC, terminal value chỉ là con số đẹp trên bảng tính. Đây là điểm cần kiểm tra chéo bằng multiples, EVA và stress case giảm margin.

**Economic value added (EVA)** đo giá trị tạo thêm sau chi phí vốn:

\[
EVA=(ROIC-WACC)\times IC,
\]

trong đó ROIC là NOPAT chia invested capital. EVA dương khi lợi nhuận trên vốn vượt WACC; tăng doanh thu nhưng ROIC dưới WACC vẫn có thể phá hủy giá trị.

### Worked check: tăng trưởng không đồng nghĩa tạo giá trị

Giả sử NOPAT là 120, invested capital là 1.000 và WACC 10%. ROIC là 12%, nên

\[
EVA=(12\%-10\%)\times1.000=20.
\]

Doanh nghiệp tạo thêm 20 đơn vị sau khi trả chi phí vốn. Nếu mở rộng nhanh nhưng NOPAT chỉ đạt 80 trên cùng 1.000 vốn, ROIC là 8% và EVA là \(-20\); doanh thu có thể tăng nhưng vốn mới tạo ra giá trị âm. Khi phân tích forecast, phải theo dõi cả tốc độ tăng vốn, ROIC biên và WACC, không chỉ tăng trưởng doanh thu hoặc EPS.

## 5. Relative valuation và bẫy “rẻ”

Relative valuation chọn peer, chọn value driver (EPS, book value, sales, EBITDA hoặc cash flow), tính multiple của peer rồi nhân với driver của target. Nó nhanh, dễ giải thích và phản ánh giá thị trường hiện tại; nhưng nếu cả nhóm bị định giá sai hoặc peer khác business risk, multiple sẽ truyền sai lầm sang target. Nó ước lượng **relative value**, không thay thế intrinsic value của DCF.

Quy trình không dừng ở “lấy P/E trung bình”. Cần (1) chọn peer có business model, growth, margin, leverage và accounting policy đủ gần; (2) chọn denominator dương và có ý nghĩa; (3) loại hoặc giải thích outlier; (4) chọn mean/median theo phân phối; (5) nhân multiple với forecast driver của target; và (6) đối chiếu implied growth/margin với DCF. P/E thấp có thể là mispricing, nhưng cũng có thể là dấu của growth thấp, leverage cao hoặc earnings ở đỉnh chu kỳ.

### Worked check: multiple trên earnings nào?

Giả sử median P/E của peer là 12x và EPS dự báo năm tới của target là 500 đồng; implied equity value là 6.000 đồng/cổ phiếu. Nhưng nếu 500 đồng đến từ đỉnh chu kỳ và EPS normalized chỉ 350 đồng, cùng multiple cho value 4.200 đồng. Chênh 1.800 đồng không phải do máy tính; nó là giả định về “earnings bình thường”. Với EV/EBITDA, phải nhân multiple với EBITDA của cả firm rồi bridge qua debt, cash và minority interest; không được lấy EV multiple rồi gọi ngay là equity price.

Một multiple chỉ có ý nghĩa khi driver, thời điểm và accounting policy tương thích giữa peer và target. Trước khi kết luận “rẻ”, hãy reverse-engineer multiple: giá hiện tại đang hàm ý growth, margin, leverage và terminal return nào, rồi đối chiếu với DCF và EVA.

Source-question test yêu cầu phân biệt money/time-weighted, arithmetic/geometric, Sharpe/Treynor/Jensen, hướng tác động của discount rate/growth/uncertainty, Gordon model, EVA và ROIC. Bàn giao: sau khi đã hiểu value và return trên tài sản cơ sở, ta mới có thể đọc phái sinh mà không nhầm premium, margin hay payoff với lợi suất “miễn phí”.

Phần company-analysis canonical đi sâu hơn ở [DCF and multiples](../03_company_analysis/03_VALUATION_DCF_AND_MULTIPLES.md) và [financial statements](../03_company_analysis/01_FINANCIAL_STATEMENTS_AND_ACCOUNTING.md). Ở đây, các owner đó được giữ nguyên; Sách 3 chỉ cung cấp learning bridge từ CAPM sang valuation.
