# 03 — Execution, Market Microstructure và Trading Portfolio

> Chương này tập trung vào phần thường chỉ được học sau khi đã giao dịch một thời gian: giá được khớp như thế nào, vì sao spread và liquidity thay đổi, tại sao một strategy có backtest tốt nhưng live kém, và cách quản trị nhiều vị thế như một portfolio thay vì từng lệnh độc lập.

## 1. Trading không kết thúc ở tín hiệu

Một strategy có thể tạo entry signal tốt nhưng vẫn thất bại nếu execution cost lớn hơn edge. Điều này đặc biệt rõ với scalping, nơi expected profit mỗi trade nhỏ.

Nếu setup có expectancy 0,15R trước chi phí nhưng spread, commission và slippage làm mất 0,12R trung bình, phần edge còn lại rất mỏng. Chỉ một thay đổi nhỏ trong liquidity hoặc commission cũng có thể biến strategy thành âm.

Vì vậy trading system gồm ít nhất ba lớp: signal generation, risk sizing và execution. Backtest chỉ meaningful nếu mô phỏng tương đối đúng cả ba.

## 2. Limit Order Book

Ở exchange-traded market, limit order book chứa các lệnh mua và bán chưa khớp ở từng mức giá.

Best bid là giá mua cao nhất. Best ask là giá bán thấp nhất. Spread là khoảng cách giữa hai mức này.

Depth cho biết lượng volume đang chờ ở nhiều mức giá. Một market có top-of-book spread hẹp nhưng depth mỏng vẫn có thể slippage mạnh nếu order lớn.

Order book là trạng thái động. Lệnh có thể được thêm, sửa hoặc hủy liên tục, nên snapshot hiện tại không đảm bảo liquidity vẫn tồn tại một giây sau.

## 3. Maker và Taker

Trader đặt limit order chờ thường cung cấp liquidity và được gọi là maker. Trader dùng market order hoặc marketable limit order để khớp ngay đang lấy liquidity, hay taker.

Một số venues có fee model khác nhau cho maker và taker. Nhưng lower fee không tự động làm maker strategy tốt hơn vì fill probability và adverse selection quan trọng.

Nếu bạn chỉ được fill khi market sắp đi ngược, limit-order execution có thể trông rẻ nhưng economic cost cao.

## 4. Queue Priority

Nếu nhiều limit orders cùng price, venue cần rule xác định lệnh nào được fill trước. Price-time priority là cơ chế phổ biến: price tốt hơn ưu tiên trước, cùng price thì lệnh vào sớm hơn ưu tiên.

Điều này quan trọng với high-frequency hoặc futures traders. Backtest giả định “giá chạm limit là được fill” thường quá lạc quan nếu queue lớn.

Retail swing traders ít nhạy hơn, nhưng vẫn nên biết touch price không luôn đồng nghĩa full fill.

## 5. Market Order và Marketable Limit

Market order ưu tiên execution, chấp nhận khớp qua nhiều levels nếu size lớn.

Marketable limit order đặt limit vượt qua best opposite quote, cho phép khớp ngay nhưng đặt giới hạn giá tệ nhất chấp nhận.

Trong fast market, marketable limit có thể bảo vệ khỏi extreme slippage nhưng cũng có fill risk nếu giá nhảy qua limit.

Không có order type luôn tối ưu. Exit trong emergency thường ưu tiên execution hơn entry bình thường.

## 6. Spread không cố định

Spread phụ thuộc competition giữa liquidity providers, volatility, information risk và trading session.

Khi news sắp ra, market makers đối mặt adverse selection cao vì người trade có thể biết information mới nhanh hơn. Họ widen spread hoặc giảm size quoted.

Trong Asia session, một số FX pairs có spread khác London overlap. Holiday hoặc rollover cũng có thể làm liquidity xấu.

Backtest dùng spread cố định dễ đánh giá quá cao performance.

## 7. Slippage

Slippage là difference giữa expected execution price và actual fill.

Positive slippage có thể xảy ra, nhưng trong stop-loss và fast market, negative slippage phổ biến hơn.

Slippage phụ thuộc size relative to available liquidity, volatility và order type. Strategy với stop rất ngắn nhạy với slippage hơn strategy target lớn.

Một backtest chuyên nghiệp nên test nhiều slippage assumptions.

## 8. Market Impact

Market impact là price movement do chính order của bạn tạo ra hoặc signal tới market.

Retail size trong EUR/USD thường quá nhỏ để tạo direct impact đáng kể, nhưng small-cap stock hoặc illiquid crypto có thể khác.

As account grows, strategy capacity trở thành constraint. Strategy profitable với $5.000 không nhất thiết scale tới $5 million.

Capacity là một phần của edge.

## 9. Adverse Selection

Adverse selection xảy ra khi counterparty có information advantage hoặc order flow cho thấy price sắp move bất lợi.

Market makers kiếm spread nhưng có nguy cơ bị informed traders trade against họ trước price move.

Retail limit trader cũng gặp vấn đề tương tự: nếu buy limit chỉ fill trong lúc sellers aggressive vì bad news, fill rate cao có thể đi cùng future return xấu.

Đây là lý do “luôn dùng limit để khỏi mất spread” không phải rule tuyệt đối.

## 10. Liquidity Sweep dưới góc Microstructure

Trong price-action language, traders thường gọi việc price xuyên previous high/low rồi quay lại là liquidity sweep.

Dưới góc microstructure, prior extremes có thể thu hút stop orders và breakout orders. Khi trigger, market orders tăng tạm thời. Nếu resting liquidity hoặc opposite flow hấp thụ được pressure, price có thể reverse.

Không cần giả định một entity bí mật cố ý “săn stop”. Cơ chế order clustering đã đủ giải thích một phần hiện tượng.

## 11. Stop Orders và Gap Risk

Stop order chỉ kích hoạt khi trigger được chạm; execution price sau đó phụ thuộc market.

Nếu stock đóng 100 rồi mở hôm sau ở 80 vì earnings shock, stop 95 không bảo đảm fill ở 95.

Derivative markets có thể trade gần 24 giờ nên gap nhỏ hơn một số cash stocks, nhưng extreme news vẫn tạo jumps.

Position sizing phải tính gap/tail risk, không chỉ historical candle range.

## 12. Volatility Clustering

Volatility có xu hướng cluster: giai đoạn biến động lớn thường được theo sau bởi biến động lớn hơn bình thường, và calm period thường kéo dài một thời gian.

Điều này ảnh hưởng stop distance và size. Fixed 10-pip stop có thể hợp lý ở low-vol regime nhưng vô nghĩa trong high-vol regime.

ATR hoặc realized volatility có thể dùng để normalize risk, nhưng phải tránh overreact với một spike đơn lẻ.

## 13. Intraday Seasonality

Volume và volatility thay đổi theo thời gian trong ngày.

Equity open thường volatile vì overnight information được price. Lunch period có thể quieter. Close có rebalancing và institutional flows.

FX có Asia, London và New York activity patterns. Gold và index futures phản ứng mạnh quanh US macro releases.

Strategy nên backtest đúng session thực sự định trade.

## 14. News Execution

CPI, NFP, FOMC hoặc unexpected geopolitical news có thể làm spreads widen và prices jump.

Một stop-loss trong news event có thể slippage lớn. Limit entry có thể không fill hoặc fill ở đúng thời điểm adverse move bắt đầu.

Nếu strategy không được thiết kế cho news, cách quản trị tốt có thể là giảm size hoặc tránh new entries quanh event.

## 15. Latency

Latency là delay từ khi signal xuất hiện tới khi order đến venue và fill.

Với swing trading, vài trăm milliseconds thường không quan trọng. Với ultra-short-term arbitrage, đó có thể là toàn bộ edge.

Retail trader nên chọn strategy phù hợp infrastructure. Cố cạnh tranh latency với professional HFT là sai game.

## 16. Broker Execution Model

Trong OTC Forex/CFD, broker có thể internalize flow hoặc hedge ra external venues tùy model.

Điều quan trọng hơn marketing label là legal disclosure về execution, conflicts, price source và slippage policy.

ECN/STP/market-maker labels thường bị dùng như marketing. Investor nên đọc best-execution hoặc order-execution documents nếu available.

## 17. Trading Portfolio thay vì từng lệnh

Nếu bạn mở năm trades, risk không phải năm con số độc lập. Correlation làm chúng tương tác.

Long EUR/USD và GBP/USD có shared USD factor. Long Nasdaq, semiconductor ETF và NVDA có shared tech/growth factor. Một USD shock hoặc rate shock có thể làm tất cả stop cùng lúc.

Portfolio risk cần nhìn common drivers.

## 18. Portfolio Heat

Portfolio heat là tổng potential loss nếu open stops bị hit, thường biểu diễn theo % equity.

Nếu bốn positions mỗi trade risk 0,5%, nominal heat là 2%. Nhưng nếu correlated mạnh, thực tế tail loss có thể gần xảy ra đồng thời.

Rule có thể giới hạn both per-trade risk và total heat.

## 19. Correlation không cố định

Historical correlation thay đổi theo regime. EUR/USD và gold có thể cùng phản ánh USD trong một period nhưng tách nhau khi real-yield shock dominates gold.

Trong crisis, correlations thường tăng vì deleveraging.

Do đó correlation matrix là tool hỗ trợ, không phải guarantee diversification.

## 20. Factor Exposure của Trading Book

Trading book có factor exposures giống investment portfolio.

Một trader có thể tưởng đang trade six markets nhưng thực chất tất cả positions đều long risk-on. Khi VIX spike, cả book lỗ.

Hãy mô tả mỗi trade theo drivers: USD, rates, equity beta, commodity, volatility hoặc country risk. Điều này giúp thấy hidden concentration.

## 21. Volatility Targeting

Volatility targeting điều chỉnh size để portfolio risk ổn định hơn khi market volatility thay đổi.

Nếu realized volatility tăng gấp đôi, size có thể giảm. Nếu volatility thấp, size tăng trong giới hạn.

Cách này tránh portfolio tự nhiên trở nên quá leveraged đúng lúc market biến động mạnh.

Nhưng volatility targeting có thể tạo procyclical selling trong crisis nếu áp dụng máy móc.

## 22. Risk Parity trong Trading

Risk parity ở mức đơn giản là phân bổ risk thay vì capital bằng nhau.

Một position gold với ATR lớn có notional nhỏ hơn EUR/USD để đóng góp cùng mức risk.

Nhưng equal volatility không đồng nghĩa equal tail risk. Gap, liquidity và correlation vẫn cần xét.

## 23. Expected Shortfall

Value at Risk hỏi loss threshold trong một confidence level, nhưng không nói losses beyond threshold lớn tới đâu.

Expected Shortfall ước lượng average loss trong tail vượt VaR. Đây là metric hữu ích hơn khi quan tâm extreme downside.

Retail trader không cần model phức tạp, nhưng tư duy tail loss quan trọng: maximum observed loss trong backtest không phải maximum possible loss.

## 24. Drawdown Control

Drawdown control có thể gồm giảm risk sau khi equity drawdown vượt threshold.

Ví dụ normal risk 0,5% mỗi trade, giảm còn 0,25% khi drawdown >8R và dừng review nếu >12R. Con số phải dựa strategy statistics, không tùy ý.

Mục tiêu là giảm probability risk-of-ruin khi system có thể đang out of regime hoặc execution bị lỗi.

## 25. Recovery Math

Loss 10% cần gain 11,1% để hồi. Loss 50% cần gain 100%.

Đây là lý do drawdown control có giá trị nonlinear. Protecting downside giúp compounding hơn chỉ cố maximize gross return.

## 26. Pyramiding

Pyramiding là tăng position khi trade đi đúng hướng theo rule.

Cách này khác averaging down. Trader thêm risk vào confirmed move, nhưng phải tính total stop risk sau mỗi add.

Nếu mỗi add có stop riêng mà combined loss vượt risk budget, pyramid trở thành hidden leverage.

## 27. Scaling Out

Partial exits giảm position theo milestones.

Ưu điểm là lock một phần gain và giảm psychological pressure. Nhược điểm là có thể giảm average winner và expectancy nếu strategy cần rare large trends.

Không có answer chung. Backtest exit distribution quyết định.

## 28. MAE/MFE và Execution Review

MAE cho biết trade đi ngược tối đa; MFE cho biết đi thuận tối đa.

Kết hợp với execution data, bạn có thể thấy stop bị hit vì spread widening hay thesis thật sự invalid. Bạn cũng có thể đo whether limit entries improve average price nhưng reduce fill quality.

Execution review phải tách signal edge khỏi fill edge.

## 29. Implementation Shortfall

Implementation shortfall đo difference giữa theoretical decision price và actual portfolio outcome sau execution costs.

Nếu strategy signal tại 100 nhưng average fill 100,4 và exit slippage thêm 0,3, actual return có thể khác đáng kể model.

Theo dõi implementation shortfall giúp biết live underperformance đến từ strategy hay execution.

## 30. Journal ở cấp Portfolio

Ngoài journal từng trade, nên có daily portfolio journal.

Ghi total heat, main factor exposures, high-impact events, realized P/L, slippage và rule violations. Sau đó review whether losses cluster quanh một factor hoặc session.

Một portfolio journal có thể phát hiện hidden issue mà xem từng trade riêng lẻ không thấy.

## 31. Kill Switch

Kill switch là điều kiện dừng trading khi system hoặc infrastructure bất thường.

Ví dụ data feed lỗi, spreads gấp nhiều lần bình thường, broker rejects orders liên tục hoặc daily loss vượt hard limit.

Professional risk management luôn có scenario “không được trade”.

## 32. Strategy Capacity

Capacity là mức capital tối đa strategy có thể triển khai mà không làm edge suy giảm quá nhiều.

Scalping illiquid instrument capacity thấp. Daily trend strategy trên liquid futures capacity cao hơn.

Nếu account tăng, strategy có thể phải chuyển timeframe, instrument hoặc execution style.

## 33. Live vs Backtest Decomposition

Khi live kém backtest, phân rã difference thành signal drift, cost drift, execution drift và behavior drift.

Signal drift nghĩa market regime thay đổi. Cost drift là spread/commission tăng. Execution drift là fill/slippage khác model. Behavior drift là trader không tuân rule.

Chẩn đoán đúng mới sửa đúng.

## 34. Khi nào nên bỏ một Strategy?

Không nên bỏ system chỉ vì losing streak nằm trong expected distribution.

Nhưng nếu live drawdown vượt historical/Monte Carlo range đáng kể, market mechanics thay đổi hoặc edge logic không còn tồn tại, cần stop và re-research.

Strategy retirement nên dựa data và economic rationale, không chỉ cảm xúc.

## Kết luận

Execution và portfolio risk là nơi một strategy từ “ý tưởng trên chart” trở thành trading system thực. Trader cần hiểu order book, spread, slippage, liquidity, broker structure và factor correlation. Một setup có edge nhỏ chỉ sống được nếu implementation cost được kiểm soát và tổng risk của nhiều positions được quản trị như một portfolio, không phải như các lệnh độc lập.
