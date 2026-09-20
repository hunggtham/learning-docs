# 04 — Factors, Index Construction và Multi-Asset Behavior

> Chương này giải thích vì sao hai ETF cùng được gọi là “cổ phiếu Mỹ”, “cổ phiếu giá trị” hoặc “ETF công nghệ” vẫn có thể cho kết quả rất khác nhau. Mục tiêu là hiểu các factor, cách index được xây dựng, cơ chế rebalancing và cách các asset class phản ứng khác nhau dưới từng economic regime.

## 1. Beta, Alpha và Factor

Trong cách nói đơn giản, beta là phần return bạn nhận vì chấp nhận rủi ro của một thị trường rộng. Nếu bạn mua broad equity index, phần lớn return dài hạn đến từ equity beta.

Alpha là phần return vượt quá mức có thể giải thích bởi benchmark hoặc các factor đã biết. Alpha khó tạo bền vững vì một strategy được nhiều người phát hiện có thể nhanh chóng bị arbitrage hoặc trở thành crowded trade.

Factor là một đặc tính có thể giải thích khác biệt return giữa các nhóm tài sản. Những factor nổi tiếng trong equities gồm size, value, momentum, quality và low volatility. Factor không phải công thức bảo đảm outperform; chúng là nguồn exposure có historical evidence và economic rationale nhất định.

## 2. Market-Cap Weighting

Nhiều index lớn dùng free-float market capitalization weighting. Company càng lớn thì trọng số càng cao.

Ưu điểm lớn là turnover thấp và index tự điều chỉnh theo market value. Nếu một company tăng mạnh, weight tăng tự nhiên mà fund không phải liên tục mua bán để giữ tỷ lệ cố định.

Nhược điểm là concentration có thể tăng khi một số mega-cap dẫn dắt market. Một index được gọi là “đa dạng hóa 500 công ty” vẫn có thể chịu ảnh hưởng rất lớn từ top 10 names.

Market-cap weighting không cố đánh giá valuation. Company càng đắt theo market value càng có weight lớn, miễn vẫn đáp ứng rule của index.

## 3. Equal Weighting

Equal-weight index cố gắng đặt mỗi constituent ở tỷ trọng tương đương. Điều này giảm dominance của mega caps nhưng làm portfolio nghiêng hơn về smaller companies.

Equal weight phải rebalance định kỳ. Khi một stock tăng quá mạnh, fund bán bớt; khi stock giảm tương đối, fund mua thêm để quay về equal weight. Cơ chế này tạo implicit contrarian behavior.

Nhưng turnover và cost cao hơn. Equal weight cũng có size-factor exposure nên không thể nói outperformance đến hoàn toàn từ “rebalancing thông minh”.

## 4. Value Factor

Value strategy tìm stocks có giá thấp tương đối so với fundamentals như earnings, book value, cash flow hoặc sales.

Economic rationale là market có thể overreact với tin xấu, nhà đầu tư ghét companies có outlook kém và đòi risk premium cao. Nếu business không xấu như feared, valuation re-rating tạo return.

Nhưng value traps tồn tại. Company P/E thấp vì earnings đang ở cyclical peak hoặc business structurally declining có thể tiếp tục rẻ hơn.

Value factor vì vậy khác với việc mua bất kỳ stock P/E thấp nào. Factor portfolio dùng rule trên một universe lớn để phân tán idiosyncratic risk.

## 5. Growth và Duration

Growth stocks có phần lớn valuation nằm ở cash flows tương lai. Vì thế chúng có equity-duration dài hơn và nhạy với discount rates.

Khi long-term real yields tăng mạnh, present value của distant cash flows giảm. Đây là lý do unprofitable growth và long-duration tech thường chịu pressure mạnh trong tightening cycle.

Nhưng rate sensitivity không phải duy nhất. Nếu growth expectations tăng nhanh hơn discount rate, growth stocks vẫn có thể outperform trong rising-yield environment.

## 6. Quality Factor

Quality thường mô tả companies có profitability cao, balance sheet tốt, earnings stability và capital efficiency tốt.

ROIC, gross profitability, low leverage và earnings quality là các metric thường gặp. Quality companies có thể giữ margin tốt hơn trong downturn và ít phụ thuộc refinancing.

Nhược điểm là quality có thể trở nên expensive. Một company tuyệt vời ở valuation quá cao vẫn có future return thấp.

## 7. Momentum Factor

Momentum dựa trên quan sát rằng assets đã outperform trong một khoảng thời gian có tendency tiếp tục outperform trong ngắn đến trung hạn.

Behavioral explanation gồm underreaction: market cập nhật information chậm; institutional explanation gồm flow và benchmark chasing.

Momentum có thể crash mạnh khi trend đảo đột ngột, đặc biệt sau panic khi losers hồi cực nhanh. Vì vậy momentum premium đi kèm tail risk đặc thù.

## 8. Low Volatility và Minimum Variance

Low-volatility strategies chọn stocks có historical volatility thấp hoặc xây portfolio tối thiểu hóa variance.

Một điều thú vị trong finance là historical low-vol stocks đôi khi có risk-adjusted return tốt hơn mô hình đơn giản dự đoán. Các giải thích gồm leverage constraints và investor preference cho lottery-like stocks.

Tuy nhiên low-vol portfolios thường sector-concentrated vào utilities, staples hoặc defensives và có rate sensitivity riêng.

## 9. Size Factor

Size factor mô tả historical tendency của smaller companies có return cao hơn large caps trong một số period.

Small caps thường ít analyst coverage, financing cost cao và business risk lớn hơn, nên expected risk premium có thể cao hơn.

Nhưng small-cap indices có thể chứa nhiều low-quality companies. Vì vậy size thường được kết hợp với quality hoặc profitability filter trong modern factor strategies.

## 10. Dividend Factor không giống Bond

Dividend ETF có thể tạo income cao nhưng underlying vẫn là equity. Dividend có thể bị cắt, stock price có thể giảm 30–50% và sector concentration có thể lớn.

High dividend yield đôi khi xuất hiện vì stock price sụp. Vì thế yield cao không phải signal an toàn.

Dividend investing phù hợp khi investor muốn cash distribution, nhưng total return vẫn nên là metric chính. Một company giữ earnings và reinvest với ROIC cao có thể tạo wealth tốt hơn company trả dividend cao nhưng business không tăng trưởng.

## 11. Smart Beta

Smart beta là tên thương mại cho rules-based portfolios khác market-cap weighting. Chúng có thể target value, quality, momentum, dividend hoặc combination.

Điểm cần hiểu là smart beta vẫn là active choice ở tầng methodology dù execution thụ động. Investor đang chọn factor exposure và rule set.

Khi so smart-beta ETFs, cần xem factor definition, rebalance frequency, sector constraints, turnover và capacity. Hai “quality ETFs” có thể dùng metric hoàn toàn khác nhau.

## 12. Index Methodology quan trọng hơn tên ETF

Index provider quyết định universe, eligibility, weighting, rebalancing và corporate-action treatment. Fund chỉ cố replicate index đó.

Một thematic ETF tên “AI” có thể nắm semiconductor, software, data-center REIT hoặc industrial automation với tỷ trọng rất khác. Chỉ đọc tên sản phẩm là không đủ.

Methodology document là tài liệu quan trọng nhất để hiểu ETF dài hạn. Nó cho biết chính xác điều gì khiến một stock được thêm, bị loại và được gán bao nhiêu weight.

## 13. Reconstitution và Rebalancing Flow

Index reconstitution là thay đổi constituents. Rebalancing là điều chỉnh weights.

Passive funds tracking index phải giao dịch để theo changes. Nếu stock được thêm vào major index, passive demand có thể tăng quanh effective date. Nhưng market thường anticipate event, nên “được thêm index = chắc chắn tăng” không đúng.

Turnover quanh rebalance tạo transaction costs và có thể ảnh hưởng tracking difference.

## 14. Multi-Asset Regimes

Assets không có correlation cố định. Correlation phụ thuộc nguồn shock.

Trong growth shock với inflation giảm, equities có thể giảm còn government bonds tăng. Đây là environment nơi stock-bond diversification hoạt động tốt.

Trong inflation shock, yields tăng làm bonds giảm trong khi margins và valuations của equities cũng chịu pressure. Stocks và bonds có thể cùng giảm.

Trong geopolitical supply shock, oil và gold có thể tăng, import-dependent currencies yếu và equities phân hóa theo sector.

Đây là lý do portfolio diversification phải dựa trên economic drivers thay vì chỉ historical correlation matrix.

## 15. Equity và Bond Duration cùng tồn tại

Bond duration là metric rõ ràng về sensitivity với yield. Equity không có contractual maturity nhưng vẫn có duration-like behavior.

Growth company có cash flows xa nên equity duration dài. Value company có current cash generation cao thường duration ngắn hơn.

Khi real yields tăng, long-duration bonds và long-duration equities có thể cùng giảm. Điều này giải thích vì sao portfolio tưởng đa dạng hóa theo tên asset class vẫn có thể concentration vào duration risk.

## 16. Inflation Beta

Commodity producers, energy stocks, TIPS, commodities và gold đều có relationship khác nhau với inflation.

TIPS bảo vệ principal theo inflation index nhưng price vẫn chịu real-yield duration. Commodity futures phản ứng trực tiếp hơn với supply-demand nhưng return còn chịu futures curve. Gold có long-run inflation narrative nhưng short-run driver mạnh thường là real yields và USD.

Không có một “inflation hedge” hoạt động giống nhau trong mọi giai đoạn.

## 17. Currency Exposure là một Asset Factor

Foreign investment tạo thêm currency exposure nếu không hedge.

Một Korean investor mua US equity unhedged đang nắm cả US equity beta và long USD/KRW exposure. Khi KRW yếu, FX hỗ trợ return bằng KRW; khi KRW mạnh, FX kéo return xuống.

Hedging loại bớt currency volatility nhưng có hedge cost và không phải luôn tốt hơn. Với long horizon, currency diversification có thể có giá trị riêng.

## 18. Correlation Breakdown

Historical correlation thường được tính trên data bình thường. Trong crisis, correlations có thể tăng vì deleveraging và liquidity needs khiến nhiều assets bị bán cùng lúc.

Đặc biệt, assets cùng được finance bằng leverage có thể trở nên correlated khi margin calls xuất hiện. Đây là lý do risk model dựa hoàn toàn vào normal-period covariance có thể đánh giá thấp tail risk.

## 19. Factor Crowding

Một factor có thể trở thành crowded nếu quá nhiều capital theo cùng strategy. Khi flows đảo, unwind có thể nhanh và mạnh.

Crowding không làm factor biến mất vĩnh viễn, nhưng làm valuation và short-term risk quan trọng hơn. Momentum, low volatility và carry đều từng có episodes unwind dữ dội.

## 20. Core–Satellite ở tầng Factor

Core có thể là broad market-cap index. Satellite không nhất thiết là single stocks; nó có thể là factor tilts.

Ví dụ investor muốn tăng quality và value exposure có thể giữ core broad ETF rồi thêm một phần nhỏ quality/value funds. Cách này minh bạch hơn việc mua nhiều thematic ETFs không rõ factor overlap.

## 21. Look-Through Analysis

Khi sở hữu nhiều ETFs, hãy nhìn xuyên qua wrapper để xem underlying holdings và factor exposures.

Hai ETFs tên khác nhau có thể top holdings giống đến 70%. Nếu không look-through, investor tưởng diversified nhưng thực tế concentration lớn.

Look-through cũng hữu ích với country ETFs, vì một country index có thể thực chất là bet vào vài sectors. Korea có semiconductor weight lớn; Vietnam có banks và property-related exposures đáng kể.

## 22. Chọn Benchmark phù hợp

Benchmark cần phản ánh opportunity set và risk của strategy.

Một small-cap value portfolio không nên chỉ so ngắn hạn với mega-cap growth index rồi kết luận thất bại. Nhưng cũng không được tự chọn benchmark dễ beat.

Benchmark tốt phải được chọn trước và đủ investable để investor thực sự có thể mua thay thế strategy.

## 23. Từ Asset Class tới Portfolio

Khi xây portfolio, câu hỏi không phải asset nào “tốt nhất”, mà asset nào đóng vai trò gì và driver nào đã có quá nhiều exposure.

Nếu income, property và stock portfolio của một household đều nhạy với Korea domestic cycle, global equity hoặc foreign bonds có thể tạo diversification. Nếu tất cả holdings đều long duration, thêm một ticker khác không giải quyết concentration.

Multi-asset thinking là nhìn through product label tới economic exposure.

## 24. Factor Definition không có một chuẩn duy nhất

Một sai lầm phổ biến là coi “value”, “quality” hay “momentum” như những object có definition cố định. Thực tế mỗi provider có thể dùng metric khác nhau. Value có thể dựa P/B, earnings yield, EV/EBITDA, cash-flow yield hoặc composite. Quality có thể dùng ROE, ROIC, gross profitability, leverage, earnings stability hoặc accruals. Momentum có thể dùng 12-1 month return, 6-month return, volatility-adjusted return hoặc bỏ qua recent reversal period theo cách khác.

Vì vậy hai ETF cùng label có thể cho exposure rất khác. Khi so products, cần đọc formula, normalization method, winsorization/outlier treatment, sector-neutralization và weighting rule. Product name chỉ là metadata; factor construction mới là strategy.

## 25. Cross-Sectional Ranking và Z-Score

Nhiều factor indices không dùng raw metric trực tiếp mà rank companies tương đối trong universe. Một cách phổ biến là chuẩn hóa metric thành z-score để biết company nằm cao hay thấp so với peers.

Điểm mạnh là các metric có đơn vị khác nhau có thể được combine. Nhưng result phụ thuộc universe. Một company “quality cao” trong small-cap universe không nhất thiết tương đương quality cao trong mega-cap universe.

Sector-neutral ranking còn thay interpretation. Nếu chọn top quality bên trong từng sector, portfolio vẫn giữ sector balance; nếu rank toàn market, high-quality sectors có thể dominate. Investor cần hiểu mình đang mua stock selection hay sector allocation trá hình.

## 26. Profitability và Investment Factors

Ngoài classic value/size/momentum, academic asset pricing còn nhấn mạnh profitability và investment intensity. Profitability factor phản ánh firms có operating profitability tốt hơn; investment factor quan sát rằng firms đầu tư assets quá aggressive trong một số framework có future return thấp hơn firms đầu tư thận trọng hơn.

Điểm quan trọng không phải học tên model, mà hiểu factor model cố tách return thành systematic characteristics. Khi một fund outperform, analyst nên hỏi bao nhiêu đến từ market beta, value, size, quality/profitability, momentum và bao nhiêu còn lại mới thực sự là residual alpha.

## 27. Multi-Factor Attribution

Một portfolio có return cao không đồng nghĩa stock-picking skill. Ví dụ manager overweight small-cap value trong đúng period small-value outperform. Nếu benchmark chỉ là broad cap-weighted index, active return nhìn rất tốt; nhưng factor regression có thể cho thấy phần lớn return được giải thích bởi known systematic tilts.

Một mental model hữu ích:

`Portfolio Return ≈ Market Beta + Factor Exposures + Security-Specific Alpha + Implementation Friction`

Attribution không nhằm phủ nhận skill. Nó giúp biết return đến từ nguồn nào và nguồn đó có thể lặp lại hay không.

## 28. Factor Neutralization

Một strategy muốn target value có thể vô tình overweight financials/energy và underweight technology. Nếu không neutralize sector, observed value premium một phần có thể thực chất là sector bet.

Sector-neutralization giảm exposure ngoài mục tiêu nhưng cũng làm strategy khác economic meaning ban đầu. Tương tự, beta-neutral hoặc dollar-neutral construction có thể loại market direction nhưng tăng turnover, shorting cost và model dependency.

Neutralization không miễn phí; mỗi constraint thay đổi portfolio economics.

## 29. Value Spread

Không chỉ biết portfolio đang “value” là đủ. Value spread — khoảng cách valuation giữa cheap và expensive groups — giúp biết factor đang rẻ hay đắt tương đối.

Nếu value stocks chỉ rẻ hơn growth một chút so lịch sử, expected premium có thể thấp hơn lúc spread cực rộng. Nhưng spread rộng cũng có thể phản ánh real structural differences. Vì vậy factor valuation là context, không phải timing signal chắc chắn.

## 30. Momentum Turnover và Trading Cost

Momentum thường turnover cao vì winners/losers thay đổi liên tục. Gross backtest có thể hấp dẫn nhưng implementation cost, tax, bid-ask spread và market impact ăn đáng kể return.

Factor càng dựa short lookback và small/illiquid stocks, capacity càng thấp. Một strategy scale tốt trên paper có thể degrade khi AUM lớn. Đây là lý do research phải phân biệt theoretical factor premium và investable factor premium.

## 31. Factor Crash

Factor returns không phân phối “êm”. Momentum có thể crash khi market đảo chiều mạnh; low-vol có thể underperform khi high-beta cyclicals rebound; value có thể chịu nhiều năm structural underperformance; carry có thể unwind khi funding/liquidity shock xảy ra.

Factor crash thường đến từ combination của crowded positioning, leverage, valuation stretch và regime reversal. Vì vậy factor diversification nên xem payoff shape, không chỉ long-run average correlation.

## 32. Factor Timing rất khó

Biết factor có long-run evidence không đồng nghĩa dự báo được năm nào outperform. Investor dễ mua factor sau nhiều năm good performance và bán sau drawdown dài, biến premium lý thuyết thành behavior gap thực tế.

Timing bằng valuation, macro regime hoặc momentum có logic nhất định nhưng cũng thêm model risk. Với nhiều investors, allocation nhỏ, diversified và rebalanced theo policy có thể robust hơn cố dự đoán factor winner mỗi quarter.

## 33. Carry và Trend là Factors ngoài Equity

Factor thinking mở rộng sang multiple asset classes. **Carry** tìm return từ chênh lệch yield/roll khi điều kiện khác không đổi; **trend** hoặc time-series momentum giữ exposure theo persistent price direction.

FX carry có thể long high-yield currency và short low-yield currency nhưng thường chịu crash risk khi funding currency mạnh trong risk-off. Commodity carry liên quan futures curve. Bond carry/roll-down phụ thuộc yield curve. Trend có thể giúp trong persistent crisis nhưng bị whipsaw trong range.

Đây là ví dụ cho thấy factor là return mechanism, không phải loại sản phẩm.

## 34. Factor Correlation thay đổi theo Regime

Value và momentum có thể diversify nhau trong một số period nhưng cùng chịu liquidity shock ở period khác. Quality và low-vol thường có defensive overlap. Size và value có thể cùng nhạy domestic credit/cyclical recovery.

Một multi-factor portfolio nên stress correlation theo regimes chứ không chỉ dùng full-sample average. Hidden common factor thường xuất hiện khi market căng thẳng.

## 35. Tracking Error là “ngân sách active risk”

Một factor tilt càng khác benchmark thì tracking error càng lớn. Điều này không chỉ là số thống kê; nó là behavioral challenge. Portfolio có thể underperform benchmark nhiều năm dù thesis dài hạn chưa sai.

Nếu investor không chịu được 5 năm relative underperformance, allocation active quá lớn so behavioral risk capacity. Factor portfolio vì vậy cần **tracking-error budget**, giống portfolio tổng cần risk budget.

## 36. Index Governance và Methodology Risk

Rules-based không có nghĩa objective tuyệt đối. Index committee/provider vẫn quyết định definitions, rebalance dates, exceptional treatment, corporate actions và methodology changes.

Một index có thể thay methodology sau khi market structure thay đổi. Điều này tạo **methodology risk**: exposure bạn mua hôm nay có thể evolve. Investor nên đọc methodology-change notices nếu product là holding lớn dài hạn.

## 37. Turnover, Tax và Rebalance Premium

Rebalancing có thể tạo buy-low/sell-high behavior nhưng turnover gây spread, tax realization và market impact. Một backtest factor trước cost thường overstated so investable return.

Khi comparing two factor ETFs, hãy xem turnover cùng với tracking difference, không chỉ expense ratio. ETF 0,15% fee nhưng turnover thấp có thể hiệu quả hơn ETF 0,10% fee nhưng implementation friction lớn.

## 38. Capacity và Crowding

Factor strategy trên large liquid equities có capacity lớn hơn micro-cap strategy. Khi AUM tăng, rebalance orders có thể trở thành significant percentage of daily volume, khiến price move trước hoặc trong execution.

Crowding còn tạo anticipatory trading: market participants front-run predictable index rebalances. Điều này không xóa factor edge hoàn toàn nhưng chuyển một phần premium từ fund investors sang liquidity providers/front-runners.

## 39. Active Share và Factor Exposure không giống nhau

Active Share cao nghĩa holdings khác benchmark nhiều, nhưng không nói risk factor khác bao nhiêu. Một portfolio có Active Share cao vẫn có beta/sector/factor gần benchmark nếu individual names offset.

Ngược lại, derivatives overlay có thể tạo factor exposure lớn mà holdings nhìn gần benchmark. Vì vậy holdings-based và returns-based analysis nên dùng bổ sung nhau.

## 40. Factor Portfolio Construction

Một multi-factor portfolio có thể combine value, quality và momentum theo hai cách lớn. **Mixing** giữ separate sleeves rồi combine; **integrated scoring** rank each stock trên nhiều factors cùng lúc.

Mixing minh bạch và dễ attribution nhưng có thể long và short implicit exposures giữa sleeves. Integrated scoring tránh một số offset nhưng phụ thuộc weighting formula hơn.

Không có construction luôn tối ưu. Điều quan trọng là biết portfolio cuối cùng có exposure gì sau khi combine.

## 41. Risk-Controlled Factor Tilt

Factor tilt thực tế nên có constraints về single-stock weight, sector deviation, liquidity, turnover và tracking error. Nếu không, optimizer có thể tập trung vào những names cực đoan để maximize score.

Một strategy robust thường chấp nhận “ít pure factor hơn” để đổi lấy investability tốt hơn. Đây là khác biệt giữa academic portfolio và product có thể scale ngoài đời thật.

## 42. Factor Due-Diligence Checklist

Trước khi mua factor ETF hoặc systematic fund, hãy xác định universe, factor definition, weighting, rebalance, turnover, sector/country constraints, concentration, historical drawdown, factor crash behavior, expense ratio, tracking difference, AUM/liquidity và overlap với holdings hiện tại.

Sau đó hỏi câu quan trọng nhất: factor này giải quyết vai trò gì trong portfolio? Nếu câu trả lời chỉ là “backtest tốt hơn broad index”, thesis chưa đủ.

## 43. Mental Model nâng cao

Có thể nhìn toàn bộ chapter bằng chuỗi:

`Economic rationale → measurable characteristic → portfolio construction → implementation cost → regime sensitivity → factor crowding → realized investor return`

Historical premium nằm ở đầu chuỗi; return mà investor thực sự nhận nằm ở cuối chuỗi. Khoảng cách giữa hai bên có thể rất lớn nếu product construction, cost hoặc behavior kém.

## Kết luận

ETF và index investing tưởng đơn giản vì execution chỉ cần một lệnh, nhưng phía sau là methodology, factor exposure, weighting rule, rebalancing, currency và regime sensitivity. Khi hiểu các lớp này, bạn có thể phân biệt diversification thật với diversification chỉ trên số lượng ticker, đồng thời biết vì sao cùng một portfolio có thể hoạt động rất khác khi inflation, growth và interest-rate regime thay đổi.
