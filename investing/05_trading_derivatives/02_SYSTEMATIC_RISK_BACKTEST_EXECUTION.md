# Systematic risk, backtest và execution

## 1. Từ setup sang system

Một setup chỉ mô tả entry context. Một trading system hoàn chỉnh còn cần stop, exit, sizing, session, news filter, maximum exposure và rules khi system không phù hợp regime.

System phải đủ rõ để hai người đọc cùng rule có thể tạo kết quả gần nhau. Nếu “vào khi chart trông mạnh”, bạn chưa có rule có thể test.

## 2. Expectancy

Expectancy kết hợp win rate, average win và average loss. Một system win 40% vẫn profitable nếu average win đủ lớn. Một system win 80% vẫn có thể âm nếu occasional loss quá lớn.

Hãy ghi results theo R thay vì chỉ dollars. R chuẩn hóa trades theo initial risk và giúp so execution giữa account sizes.

## 3. Position sizing

Stop placement nên dựa invalidation hoặc volatility. Sau đó position size được tính từ risk amount.

Nếu risk budget là 0,5% account và stop xa gấp đôi, size phải giảm khoảng một nửa. Không kéo stop tùy tiện để khớp lot đã chọn.

## 4. Portfolio heat

Risk per trade không đủ khi có nhiều correlated positions. Long EUR/USD, GBP/USD và gold có thể cùng mang short-USD factor. Tổng nominal risk 1,5% có thể gần một macro bet duy nhất.

Portfolio heat cần xem common factor, notional và correlations. Khi exposures cùng direction, giảm size hoặc chọn trade có quality tốt nhất.

## 5. Backtest design

Backtest phải dùng rule cố định và include realistic costs. Data sample cần nhiều regimes, không chỉ period đẹp nhất.

Ghi entry, stop, exit, R, MFE, MAE, session và relevant context. Nếu rule thay giữa sample, hãy đánh dấu version và test lại.

Look-ahead bias xuất hiện khi dùng information chưa available tại trade time. Survivorship bias bỏ failed companies. Optimization bias fit parameters quá sát history.

## 6. Out-of-sample và walk-forward

Không nên optimize và đánh giá trên cùng data. Chia development sample và validation sample giúp phát hiện overfitting.

Walk-forward kiểm tra strategy qua các windows theo thời gian. Mục tiêu không phải tạo perfect equity curve mà xem behavior có ổn khi regime thay đổi không.

## 7. Monte Carlo

Historical sequence chỉ là một ordering của wins/losses. Monte Carlo reshuffle hoặc simulate để xem possible drawdowns và losing streaks.

Nếu account chỉ sống được historical max drawdown chính xác, sizing quá aggressive. Risk management phải chịu được bad-but-plausible sequence xấu hơn history.

## 8. Metrics

Profit Factor là gross wins chia gross losses. Sharpe đo excess return relative volatility. Sortino chỉ penalize downside deviation. Calmar so annualized return với max drawdown.

Không metric nào đủ một mình. Short-vol strategies có thể high Sharpe lâu rồi chịu tail loss. Hãy xem payoff distribution và maximum adverse scenarios.

## 9. Execution

Backtest fill không giống live fill. Spread widen, slippage và queue priority ảnh hưởng result.

Limit order kiểm soát price nhưng có non-fill/adverse selection. Market order ưu tiên execution. Stop-market ưu tiên exit; stop-limit có risk không fill.

Scalping edge nhỏ đặc biệt nhạy costs. Swing strategy ít trades hơn nhưng chịu overnight gap risk.

## 10. Regime

Trend system có thể underperform sideways regime. Mean reversion có thể blow up trong persistent trend. Carry chịu unwind khi volatility spike.

Regime filter phải có causal logic và đơn giản. Thêm quá nhiều filters để xóa historical losses tạo overfit.

## 11. Forward test

Sau backtest, chạy demo hoặc paper live để kiểm timing và data handling. Sau đó dùng minimum real size để kiểm psychology và actual execution.

Scale dựa sample và process consistency, không dựa vài winning trades.

## 12. Journal và review

Journal nên tách strategy error khỏi execution error. Một losing trade đúng rule là statistical sample, không phải mistake. Một winning trade phá rule là execution failure.

Weekly review xem setup nào có expectancy, time nào errors cao, slippage ra sao và whether market regime thay đổi.

Trading improvement đến từ feedback loop: rule → data → review → controlled change → retest, không đến từ việc đổi strategy theo cảm xúc.