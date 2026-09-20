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

## Kết luận

ETF và index investing tưởng đơn giản vì execution chỉ cần một lệnh, nhưng phía sau là methodology, factor exposure, weighting rule, rebalancing, currency và regime sensitivity. Khi hiểu các lớp này, bạn có thể phân biệt diversification thật với diversification chỉ trên số lượng ticker, đồng thời biết vì sao cùng một portfolio có thể hoạt động rất khác khi inflation, growth và interest-rate regime thay đổi.
