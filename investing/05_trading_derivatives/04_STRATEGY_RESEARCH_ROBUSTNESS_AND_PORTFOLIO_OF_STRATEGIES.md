# 04 — Strategy Research, Robustness và Portfolio of Strategies

Tài liệu này bổ sung phần còn thiếu giữa “biết backtest” và “có một trading process đáng tin”. Mục tiêu là hiểu cách biến một ý tưởng thành hypothesis, test nó đúng cách, tránh overfitting, đánh giá uncertainty và cuối cùng kết hợp nhiều strategies mà không vô tình nhân đôi cùng một risk.

## 1. Trading idea khác strategy

Một trading idea có thể là “breakout sau consolidation thường tiếp tục chạy”. Strategy cần cụ thể hóa idea thành rules có thể test: market nào, timeframe nào, consolidation được định nghĩa ra sao, breakout tính theo close hay intrabar, stop ở đâu, exit khi nào, position size thế nào và có tránh news không.

Nếu hai người đọc rule nhưng implement khác nhau, strategy chưa đủ rõ.

## 2. Hypothesis trước data mining

Một hypothesis tốt bắt đầu từ economic hoặc behavioral logic. Momentum có thể tồn tại vì underreaction và slow information diffusion. Mean reversion có thể tồn tại vì liquidity shocks và temporary dislocations. Carry có thể tồn tại vì compensation cho crash risk.

Nếu chỉ scan hàng nghìn combinations rồi chọn cái đẹp nhất, bạn dễ tìm noise hơn edge.

## 3. In-sample và Out-of-sample

In-sample dùng để develop idea. Out-of-sample dùng để kiểm tra liệu pattern có tồn tại trên dữ liệu chưa dùng để fit hay không.

Nếu strategy chỉ đẹp trong in-sample nhưng collapse out-of-sample, nhiều khả năng rules đã fit noise.

## 4. Walk-Forward Analysis

Walk-forward chia history thành nhiều đoạn: train trên một cửa sổ, test trên đoạn kế tiếp, rồi roll forward. Nó mô phỏng tốt hơn quá trình thực tế khi trader cập nhật model theo thời gian.

Nhưng walk-forward cũng có thể overfit nếu bạn thử quá nhiều window lengths và chỉ giữ setting đẹp nhất.

## 5. Look-Ahead Bias

Look-ahead xảy ra khi backtest vô tình dùng thông tin chưa tồn tại tại thời điểm trade. Ví dụ dùng final daily high để quyết định entry intraday, hoặc dùng economic data đã revised sau này.

Đây là lỗi cực kỳ nguy hiểm vì backtest có thể trông hoàn hảo.

## 6. Survivorship Bias

Nếu test cổ phiếu chỉ trên constituents hiện tại của một index, bạn bỏ qua companies đã delist hoặc phá sản. Result sẽ đẹp hơn thực tế.

Dataset phải phản ánh universe tồn tại tại từng thời điểm.

## 7. Data Snooping

Nếu test 1.000 strategies, xác suất một số strategy có backtest đẹp do may mắn tăng rất lớn. P-value hay Sharpe đơn lẻ không còn ý nghĩa như khi chỉ test một hypothesis.

Cần tính mental penalty cho số lượng thử nghiệm.

## 8. Parameter Stability

Strategy tốt thường không chỉ hoạt động tại đúng một parameter. Nếu moving average 49 ngày cực tốt nhưng 48 và 50 ngày đều tệ, đó là red flag.

Robust edge thường tạo vùng parameters tương đối ổn, không phải một needle peak.

## 9. Transaction Costs

Backtest phải trừ spread, commission, slippage, funding và borrow fees nếu có. Với high-frequency strategy, cost nhỏ có thể xóa toàn bộ edge.

Cost model nên conservative hơn live average, đặc biệt với volatile periods.

## 10. Market Impact

Account nhỏ có thể vào ra dễ, nhưng strategy không scale vô hạn. Khi order size lớn relative to liquidity, execution tự đẩy price bất lợi.

Capacity là một thuộc tính của strategy.

## 11. Regime Dependence

Một strategy có thể chỉ hoạt động trong trending regime, low-vol regime hoặc high-rate regime. Điều đó không làm strategy xấu, miễn bạn biết source of edge.

Sai lầm là giả định backtest average qua nhiều năm nghĩa edge stable mọi lúc.

## 12. Distribution của Returns

Mean và standard deviation không đủ nếu returns có skew và fat tails. Options strategies thường có nhiều small wins và một số rare large losses.

Cần nhìn histogram, skewness, kurtosis, worst trades và tail scenarios.

## 13. Win Rate không đủ

Strategy win rate 70% vẫn có thể âm nếu average loss quá lớn. Strategy win rate 35% có thể profitable nếu average win lớn.

Expectancy theo R là core metric:

`E = P(win) × AvgWin - P(loss) × AvgLoss`

## 14. Confidence Interval của Expectancy

Sample expectancy chỉ là estimate. Với 30 trades, uncertainty rất lớn. 300 trades cho estimate tốt hơn nhưng vẫn phụ thuộc stationarity.

Bạn nên nghĩ theo range thay vì tin một con số exact.

## 15. Bootstrap và Monte Carlo

Bootstrap resample historical trades để tạo nhiều possible equity paths. Monte Carlo giúp ước lượng distribution của drawdown, losing streak và terminal equity.

Mục tiêu không phải dự báo tương lai chính xác mà kiểm tra strategy có sống được qua bad sequences hay không.

## 16. Risk of Ruin

Risk of ruin tăng khi edge nhỏ, variance lớn và position sizing cao. Một profitable strategy vẫn có thể phá sản nếu sizing quá lớn trước khi law of large numbers phát huy tác dụng.

## 17. Fractional Kelly

Kelly cho theoretical optimal growth khi edge và odds biết chính xác. Trong trading, estimates không chính xác nên full Kelly thường quá aggressive.

Fractional Kelly hoặc fixed conservative risk thường thực tế hơn.

## 18. Drawdown Budget

Trước khi live, define drawdown level mà strategy hoặc trader phải giảm size, pause hoặc review. Rule này nên viết trước khi emotional stress xuất hiện.

Drawdown stop không nhất thiết nghĩa strategy “hỏng”; nó là circuit breaker để tránh compounding errors.

## 19. Strategy Degradation

Edge có thể giảm vì competition, market structure thay đổi hoặc participant behavior thích nghi. Theo dõi rolling expectancy, hit rate, slippage và opportunity frequency giúp detect degradation.

Không nên kill strategy chỉ vì vài losses, nhưng cũng không nên giữ mãi vì backtest lịch sử đẹp.

## 20. Research Log

Mỗi experiment nên ghi hypothesis, data, rules, parameters, result và conclusion. Điều này ngăn bạn vô thức retest cùng idea đến khi tìm ra version đẹp.

Research discipline quan trọng không kém coding.

## 21. Forward Test

Sau backtest, demo hoặc paper trading giúp test execution assumptions và operational issues. Nó cũng kiểm tra whether bạn thực sự có thể follow rules.

## 22. Small Live Test

Live capital nhỏ là bước khác paper trading vì psychology và real fills khác. Mục tiêu giai đoạn này là validate process, không maximize profit.

## 23. Portfolio of Strategies

Nhiều strategies có thể giảm dependency vào một edge duy nhất, nhưng chỉ khi return streams thực sự khác nhau.

Trend strategy trên EURUSD và trend strategy trên GBPUSD có thể vẫn cùng USD factor. Strategy count không bằng diversification.

## 24. Strategy Correlation

Hãy tính correlation của daily hoặc trade-level returns. Nhưng correlation trung bình chưa đủ; cần xem crisis correlation vì strategies có thể cùng fail trong volatility spike.

## 25. Factor Decomposition

Một strategy có thể ẩn exposures như equity beta, short volatility, long carry hoặc USD trend. Nếu nhiều strategies cùng factor, portfolio risk tập trung.

## 26. Volatility Scaling

Volatility scaling điều chỉnh position size theo estimated risk. Khi volatility tăng, size giảm; khi volatility giảm, size tăng.

Nhược điểm là volatility thường spike sau price move, nên scaling có thể giảm exposure gần lows.

## 27. Equal Capital vs Equal Risk

Chia capital đều không tạo equal risk. Strategy high-volatility đóng góp nhiều hơn. Risk allocation nên nhìn contribution to portfolio drawdown.

## 28. Convexity và Tail Risk

Short-vol strategies thường nhìn ổn trong normal periods nhưng có negative convexity. Trend following hoặc long options có thể có convex payoff hơn trong crisis.

Portfolio of strategies nên xem payoff shape, không chỉ average correlation.

## 29. Operational Risk

Strategy tốt vẫn có thể fail vì API error, broker outage, wrong symbol, duplicate order hoặc time-zone bug. Automation cần position reconciliation, order validation và kill switch.

Manual trader cũng có operational risk: nhập sai lot, nhầm direction hoặc trade sai account.

## 30. Post-Trade Attribution

Sau trade, tách result thành signal quality, sizing, execution và management. Một losing trade đúng process khác một loss do execution mistake.

## 31. Monthly Strategy Review

Review nên tập trung distribution và process, không chỉ net P/L. Hỏi edge có còn xuất hiện không, costs có đổi không, regime có khác không và rule violations bao nhiêu.

## 32. Khi nào nên thay rule

Chỉ thay rule khi có evidence hoặc logic mới. Không thay chỉ vì recent losses. Mỗi modification cần versioning để biết performance đến từ version nào.

## 33. Research Mindset

Strategy research là quá trình falsification: cố tìm lý do idea sai. Nếu hypothesis sống sót nhiều tests độc lập, confidence mới tăng.

Cách tư duy này trái với confirmation bias, nơi trader chỉ tìm chart đẹp để chứng minh system đúng.

## 34. Kết luận

Một strategy đáng tin không phải strategy có equity curve đẹp nhất. Nó là strategy có logic hợp lý, rules rõ, cost realistic, parameter ổn định, out-of-sample performance chấp nhận được và sizing đủ bảo thủ để sống qua uncertainty.