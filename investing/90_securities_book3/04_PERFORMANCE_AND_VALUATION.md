# 4. Đo lường thành quả và định giá doanh nghiệp

CAPM cho ta một mức sinh lợi yêu cầu, nhưng chưa cho biết danh mục thực tế làm tốt đến đâu, cũng chưa nói một doanh nghiệp đáng giá bao nhiêu. Phần này nối hai câu hỏi: đo performance sao cho không bị dòng tiền nạp/rút đánh lừa, rồi chuyển forecast về giá trị hiện tại bằng cash flow và cost of capital.

## 1. Return qua nhiều kỳ

Investment return gồm income và price change: cổ phiếu có dividend + capital gain; trái phiếu có interest + capital gain. Nếu nhà đầu tư nạp/rút tiền giữa các kỳ, hai cách đo có ý nghĩa khác nhau.

**Lợi suất gia quyền theo tiền (money-weighted return, MWR / 금액가중수익률)** là IRR của toàn bộ dòng tiền: tìm \(r\) sao cho giá trị hiện tại của tiền vào bằng giá trị hiện tại của tiền ra. Nó trả lời “với đúng thời điểm số vốn của nhà đầu tư, tài khoản sinh lời thế nào?”. **Lợi suất gia quyền theo thời gian (time-weighted return, TWR / 시간가중수익률)** chia lịch sử tại các thời điểm có dòng tiền, tính holding-period return từng đoạn rồi ghép:

\[
R_{TW}=\prod_t(1+r_t)-1.
\]

Trong ví dụ nguồn, mua một cổ phiếu 5.000 won, năm sau mua thêm ở 5.400, cuối kỳ bán hai cổ phiếu ở 5.500 và nhận dividend, money-weighted return là nghiệm IRR khoảng 8%. Time-weighted return ghép hai holding-period return 12% và 5,45% thành khoảng 18,1% cho toàn kỳ; nếu annualize thì geometric mean khoảng 8,68%, còn arithmetic mean là 8,725%. Vì các cách này trả lời câu hỏi khác nhau, không được so sánh chúng như cùng một đại lượng.

**Trung bình số học (arithmetic mean / 산술평균)** phù hợp mô tả một kỳ điển hình; **trung bình nhân (geometric mean / 기하평균)** phù hợp tăng trưởng lũy kế:

\[
1+\bar r_g=\left[\prod_{t=1}^T(1+r_t)\right]^{1/T}.
\]

Với return dương, geometric mean không vượt arithmetic mean; volatility tạo “drag” lên tăng trưởng ghép.

## 2. Ba thước đo risk-adjusted performance

Với portfolio return (r_p), risk-free (r_f), độ lệch chuẩn (sigma_p) và beta (eta_p): các return phải cùng horizon và cùng scale, (sigma_p) là total volatility cùng horizon, còn (eta_p) không có đơn vị. Sharpe vì thế có dạng “excess return trên một đơn vị volatility”; Treynor có dạng return trên một đơn vị beta, nên trị số của hai chỉ số không được so trực tiếp như cùng đơn vị.

\[
\text{Sharpe}=\frac{r_p-r_f}{\sigma_p},\qquad
\text{Treynor}=\frac{r_p-r_f}{\beta_p}.
\]

**Chỉ số Sharpe (Sharpe ratio / 샤프지수)** dùng tổng rủi ro nên phù hợp khi portfolio là phần lớn tài sản của nhà đầu tư và chưa đa dạng hóa đầy đủ. **Chỉ số Treynor (Treynor ratio / 트레이너지수)** chỉ dùng systematic risk nên hợp lý hơn khi portfolio đã đa dạng hóa và được so với market exposure. **Alpha Jensen (Jensen’s alpha / 젠센의 알파)** so sánh return thực tế với CAPM required return:

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

**Định giá doanh nghiệp (valuation / 기업가치평가)** là ước lượng fair market value của doanh nghiệp dựa trên hoạt động, môi trường cạnh tranh và dòng tiền tương lai. Quy trình nguồn gồm: hiểu đặc tính doanh nghiệp và ngành; dự báo môi trường kinh doanh và financial performance; đo cash flow; chọn discount rate; chuyển các dòng tiền tương lai về hiện tại; kiểm tra kết quả bằng phương pháp khác.

Raw p.149 và p.160 còn đặt DCF/relative valuation trong một taxonomy rộng hơn gồm **định giá bằng quyền chọn thực (real-option valuation / 실물옵션가치평가법)**, **điều chỉnh giá trị sổ sách (book-value adjustment / 장부가치조정법)** và **điều chỉnh giá trị thị trường (market-value adjustment / 시장가치조정법)**. Source nói rõ phần học này chỉ đi sâu DCF và relative valuation, nên ba tên kia là **positioning units**, không có formula contract riêng trong Book 3; mục tiêu là nhận ra chúng là phương pháp khác, không giả vờ source đã dạy chi tiết cơ chế.

Đừng lẫn cash flow kế toán với cash flow dùng cho valuation. Cần xác định cash flow thuộc về ai (firm hay equity), xử lý thuế thực trả, đầu tư tài sản và vốn lưu động; không trộn numerator sau lãi vay với discount rate trước lãi vay. **Chi phí vốn (cost of capital / 자본비용)** là giá phải trả cho vốn; CAPM thường dùng cho cost of equity:

\[
k_e=r_f+\beta_e(E(r_m)-r_f).
\]

Kết hợp debt và equity theo tỷ trọng thị trường cho **chi phí vốn bình quân gia quyền (weighted average cost of capital, WACC / 가중평균자본비용)**. Tính nhất quán giữa dòng tiền và discount rate là điều kiện, không phải chi tiết phụ.

Nếu dùng **dòng tiền tự do cho doanh nghiệp (free cash flow to firm, FCFF / 기업 전체에 귀속되는 여유현금흐름)**, một dạng thực hành thường viết là (FCFF=NOPAT+D&A-Capex-Delta NWC). **FCFE** bắt đầu từ net income và điều chỉnh theo net borrowing, Capex và thay đổi vốn lưu động. Raw Book 3 trực tiếp dạy FCF/FCFF và logic “여유현금흐름”; phần FCFE ở đây là bridge biên tập sang canonical valuation owner, không được dùng để chứng minh source coverage của Sách 3. Đây không phải hai con số để chọn tùy ý: FCFF thuộc về cả debt holder và equity holder nên chiết khấu bằng WACC; FCFE thuộc equity holder nên chiết khấu bằng \(k_e\). WACC minh họa sự khớp đó:

\[
WACC=\frac{E}{D+E}k_e+\frac{D}{D+E}k_d(1-T).
\]

Ở WACC, (E,D) là market value của equity và interest-bearing debt, (k_e,k_d) là required return/cost theo cùng kỳ, và (T) là tax rate dùng cho tax shield theo giả định mô hình. Nguồn nhấn mạnh weight theo **market value**, không phải book weight. Nếu capital structure đổi mạnh qua thời gian hoặc tax shield không dùng được đầy đủ, một WACC cố định là approximation.

Nếu lấy FCFE nhưng dùng WACC, hoặc lấy FCFF nhưng dùng cost of equity, value bị lệch vì một phần rủi ro/vốn đã bị tính hai lần hoặc bỏ sót.

### EV không phải equity value

DCF theo FCFF cho **enterprise value (EV)** — giá trị hoạt động dành cho tất cả nhà cung cấp vốn. Để đi tới equity value, cần bridge có chủ ý:

\[
Equity\ Value=EV+cash+non\text{-}operating\ assets-debt-minority\ interest-other\ claims.
\]

Không được tự động lấy “EV trừ tổng liabilities”: chỉ những khoản nợ và claim kinh tế cần thanh toán cho equity mới thuộc bridge, còn operating liabilities đã đi vào working capital/FCFF. Nếu doanh nghiệp có pension deficit, preferred stock, lease debt, treasury shares hoặc options pha loãng, phải quyết định chúng nằm ở cash flow, debt adjustment hay share count. Cùng một DCF có thể cho giá mỗi cổ phiếu khác nhau chỉ vì bridge hoặc diluted shares bị bỏ sót.

## 4. DCF, FCFF/FCFE và EVA

**Chiết khấu dòng tiền (discounted cash flow, DCF / 현금흐름할인법)** định giá bằng:

\[
V_0=\sum_{t=1}^{T}\frac{CF_t}{(1+k)^t}+\frac{TV_T}{(1+k)^T}.
\]

Trong công thức DCF, (CF_t) là cash flow ở cuối kỳ (t), (k) là discount rate mỗi kỳ, (T) là số kỳ forecast rõ ràng và (TV_T) là terminal value tại cuối kỳ (T). Cash flow và value dùng cùng currency; (k) và growth phải cùng periodicity/scale. Công thức giả định timing dòng tiền và discount convention đã được xác định; mid-year convention, cash flow không đều, inflation/currency khác nhau hoặc leverage thay đổi cần điều chỉnh riêng.

Discount rate tăng hoặc cash flow kỳ vọng giảm thì value giảm; tăng trưởng bền vững, thời gian sống dài hơn và dòng tiền chắc hơn làm value tăng. **Giá trị còn lại/cuối kỳ (terminal/residual value / 잔여가치)** phải nêu rõ giả định tăng trưởng dài hạn, vì một sai lệch nhỏ ở \(k-g\) có thể chi phối toàn bộ kết quả.

FCFF là dòng tiền cho toàn doanh nghiệp, thường chiết khấu bằng WACC; FCFE là dòng tiền cho cổ đông, chiết khấu bằng cost of equity. Dividend discount model là trường hợp đặc biệt cho equity. Với Gordon growth:

\[
P_0=\frac{D_1}{k_e-g}.
\]

Ví dụ nguồn: dividend kỳ tới 2.500 won, \(k_e=15\%\), tăng trưởng 5% vô hạn ⇒ \(P_0=25.000\) won. Điều kiện \(k_e>g\) là ranh giới toán học bắt buộc.

Terminal value cần được kiểm tra bằng hai cách: perpetual growth \(TV_T=FCF_{T+1}/(k-g)\) và exit multiple dựa trên peer. Nếu 70% giá trị DCF đến từ terminal value, kết luận “cổ phiếu rẻ” thực chất đang phụ thuộc vào vài điểm phần trăm của \(g\), \(k\) và margin dài hạn. Vì vậy nên lập sensitivity table theo \(k\) và \(g\), không chỉ trình bày một điểm base case.

### Worked check: terminal value không được để trong bóng tối

Giả sử một công ty có FCFF năm 1–3 lần lượt là 100, 110 và 121; WACC là 10%, tăng trưởng dài hạn là 3%. Khi đó \(TV_3=121\times1,03/(0,10-0,03)\approx1.780\). Giá trị hiện tại xấp xỉ \(90,9+90,9+90,9+1.780/1,1^3=1.610\) đơn vị. Nếu chỉ đổi \(g\) xuống 2%, tổng value còn khoảng 1.432; nếu đổi lên 4%, value tăng lên khoảng 1.848. Khoảng dao động này không phải sai số máy tính: nó cho thấy terminal assumption đang mang phần lớn rủi ro mô hình.

Khi lập forecast, hãy tách ba lớp: doanh thu/margin tạo ra FCFF, reinvestment tạo ra tăng trưởng, và WACC phản ánh risk/capital structure. Nếu tăng trưởng cao nhưng không có reinvestment hoặc ROIC vượt WACC, terminal value chỉ là con số đẹp trên bảng tính. Đây là điểm cần kiểm tra chéo bằng multiples, EVA và stress case giảm margin.

**Giá trị kinh tế gia tăng (economic value added, EVA / 경제적 부가가치)** đo giá trị tạo thêm sau chi phí vốn:

\[
EVA=(ROIC-WACC)\times IC,
\]

trong đó **ROIC (투하자본이익률)** là NOPAT chia invested capital. EVA dương khi lợi nhuận trên vốn vượt WACC; tăng doanh thu nhưng ROIC dưới WACC vẫn có thể phá hủy giá trị.

### Worked check: tăng trưởng không đồng nghĩa tạo giá trị

Giả sử NOPAT là 120, invested capital là 1.000 và WACC 10%. ROIC là 12%, nên

\[
EVA=(12\%-10\%)\times1.000=20.
\]

Doanh nghiệp tạo thêm 20 đơn vị sau khi trả chi phí vốn. Nếu mở rộng nhanh nhưng NOPAT chỉ đạt 80 trên cùng 1.000 vốn, ROIC là 8% và EVA là \(-20\); doanh thu có thể tăng nhưng vốn mới tạo ra giá trị âm. Khi phân tích forecast, phải theo dõi cả tốc độ tăng vốn, ROIC biên và WACC, không chỉ tăng trưởng doanh thu hoặc EPS.

Source còn dùng ba mắt xích để đọc EVA: **NOPAT (세후영업이익)** là lợi nhuận hoạt động sau thuế trước phân phối cho debt/equity; **invested capital (투하자본)** là vốn dùng cho hoạt động, source mô tả từ net working capital + net non-current operating assets; **MVA (market value added / 시장부가가치)** là enterprise value trừ invested capital và bằng present value của EVA tương lai trong logic mô hình. Ba đại lượng phải cùng phạm vi hoạt động; nếu một item financing bị đưa vào NOPAT nhưng lại để ngoài invested capital, ROIC/EVA sẽ mất nhất quán.

## 5. Relative valuation và bẫy “rẻ”

**Định giá tương đối (relative valuation / 상대가치평가법)** chọn peer, chọn value driver (EPS, book value, sales, EBITDA hoặc cash flow), tính multiple của peer rồi nhân với driver của target. Nó nhanh, dễ giải thích và phản ánh giá thị trường hiện tại; nhưng nếu cả nhóm bị định giá sai hoặc peer khác business risk, multiple sẽ truyền sai lầm sang target. Nó ước lượng **relative value**, không thay thế intrinsic value của DCF.

Quy trình không dừng ở “lấy P/E trung bình”. Cần (1) chọn peer có business model, growth, margin, leverage và accounting policy đủ gần; (2) chọn denominator dương và có ý nghĩa; (3) loại hoặc giải thích outlier; (4) chọn mean/median theo phân phối; (5) nhân multiple với forecast driver của target; và (6) đối chiếu implied growth/margin với DCF. P/E thấp có thể là mispricing, nhưng cũng có thể là dấu của growth thấp, leverage cao hoặc earnings ở đỉnh chu kỳ.

### Worked check: multiple trên earnings nào?

Giả sử median P/E của peer là 12x và EPS dự báo năm tới của target là 500 đồng; implied equity value là 6.000 đồng/cổ phiếu. Nhưng nếu 500 đồng đến từ đỉnh chu kỳ và EPS normalized chỉ 350 đồng, cùng multiple cho value 4.200 đồng. Chênh 1.800 đồng không phải do máy tính; nó là giả định về “earnings bình thường”. Với EV/EBITDA, phải nhân multiple với EBITDA của cả firm rồi bridge qua debt, cash và minority interest; không được lấy EV multiple rồi gọi ngay là equity price.

Một multiple chỉ có ý nghĩa khi driver, thời điểm và accounting policy tương thích giữa peer và target. Trước khi kết luận “rẻ”, hãy reverse-engineer multiple: giá hiện tại đang hàm ý growth, margin, leverage và terminal return nào, rồi đối chiếu với DCF và EVA.

Source-question test yêu cầu phân biệt money/time-weighted, arithmetic/geometric, Sharpe/Treynor/Jensen, hướng tác động của discount rate/growth/uncertainty, Gordon model, EVA và ROIC. Bàn giao: sau khi đã hiểu value và return trên tài sản cơ sở, ta mới có thể đọc phái sinh mà không nhầm premium, margin hay payoff với lợi suất “miễn phí”.

Phần company-analysis canonical đi sâu hơn ở [DCF and multiples](../03_company_analysis/03_VALUATION_DCF_AND_MULTIPLES.md) và [financial statements](../03_company_analysis/01_FINANCIAL_STATEMENTS_AND_ACCOUNTING.md). Ở đây, các owner đó được giữ nguyên; Sách 3 chỉ cung cấp learning bridge từ CAPM sang valuation.
