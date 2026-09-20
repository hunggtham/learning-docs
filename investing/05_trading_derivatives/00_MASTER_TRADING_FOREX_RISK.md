# 03 — Trading, Forex, phân tích kỹ thuật và quản trị rủi ro

> File này dành cho người chưa biết trading. Nó không giả định bạn hiểu chart, pip, lot, leverage, margin, stop loss hay backtest. Mục tiêu là giúp bạn nhìn trading như một bài toán xác suất và quản trị vốn trước khi học entry. Nếu chỉ nhớ một điều, hãy nhớ rằng chart đẹp không cứu được một tài khoản dùng position size sai.

## Mục lục

1. Trading thực chất là gì?
2. Edge và expectancy
3. Tại sao người mới thường thua?
4. Chart và candlestick
5. Timeframe và noise
6. Trend, range và market structure
7. Support và resistance
8. Breakout, pullback và mean reversion
9. Volume, liquidity và volatility
10. Indicators
11. SMC/ICT nên hiểu thế nào?
12. Multi-timeframe analysis
13. Forex từ con số 0
14. Pip, point, lot và contract size
15. Leverage và margin
16. Balance, equity, free margin và stop-out
17. Spread, commission, slippage và swap
18. Carry trade
19. Position sizing
20. Stop loss và invalidation
21. Take profit, R-multiple và expectancy
22. Risk of ruin
23. Trading sessions
24. News trading
25. Futures trading
26. Options trading
27. XAUUSD
28. Backtest
29. Forward test
30. Journal
31. Overfitting và statistical bias
32. Psychology và process
33. Xây trading system
34. Execution quality
35. Portfolio heat và correlation
36. Kelly criterion
37. Monte Carlo
38. Profit Factor, Sharpe, Sortino và Calmar
39. MAE/MFE
40. Regime filter
41. Broker safety
42. Trading như một business
43. Lộ trình demo → live

---

## 1. Trading thực chất là gì?

Trading là hoạt động mở và đóng financial positions nhằm khai thác biến động price trong một horizon ngắn hoặc trung bình. Một trade có thể kéo dài vài giây, vài giờ hoặc vài tuần. Thời gian giữ không phải bản chất cốt lõi. Cốt lõi là trader dựa vào một setup có xác suất và payoff có thể lặp lại.

Một lần đoán đúng direction không chứng minh skill. Nếu bạn đoán gold tăng vì chiến tranh và đúng một lần, đó có thể chỉ là luck. Edge phải tồn tại qua một sample đủ lớn sau spread, commission, slippage và swap.

Trader không cần biết lệnh tiếp theo thắng hay thua. Giống insurer không biết chính xác customer nào sẽ claim, trader cần biết distribution của nhiều trades có expected value dương hay không.

## 2. Edge và expectancy

Edge là lợi thế thống kê. Một strategy có edge khi rule rõ ràng, repeatable và expected result sau costs dương.

Expectancy có thể viết:

`E = Win rate × Average win - Loss rate × Average loss`

Nếu win rate 40%, average win 2R và average loss 1R:

`E = 0,4×2 - 0,6×1 = +0,2R/trade`

Strategy vẫn profitable dù phần lớn trades thua.

Nếu win rate 80%, average win 0,25R và average loss 2R:

`E = 0,8×0,25 - 0,2×2 = -0,2R`

Win rate cao không đồng nghĩa edge tốt.

## 3. Tại sao người mới thường thua?

Người mới thường học entry trước risk. Họ tìm indicator, signal group, “smart money point” hoặc setup được quảng cáo 90% win rate. Nhưng account thường chết vì oversizing, leverage, revenge trading và không hiểu variance.

Một strategy tốt vẫn có losing streak. Nếu trader risk 10% mỗi trade, chỉ năm losses liên tiếp khiến account còn `0,9^5 ≈ 59%`. Nếu risk 1%, sau năm losses còn gần 95%.

Một lỗi khác là strategy hopping. Sau ba losses, trader đổi system; vài losses nữa lại đổi. Không system nào có sample đủ để biết edge.

Người mới cũng nhầm short-term luck với skill. Leverage 1:500 có thể làm account double rất nhanh và cũng làm cháy rất nhanh. Outcome vài trades không đánh giá được process.

## 4. Chart và candlestick

Chart là visualization của historical price. Candlestick chứa open, high, low, close.

Trên M5, mỗi candle đại diện năm phút. Body thể hiện open-close; wicks thể hiện extremes.

Một large bullish candle chỉ nói buying pressure mạnh trong period đó, không nói chắc chắn future price tăng. Candle ngay dưới major resistance khác candle breakout từ consolidation.

Pin bar, engulfing hay doji là descriptions của OHLC relationships. Pattern chỉ có giá trị nếu context và statistics hỗ trợ.

## 5. Timeframe và noise

M1, M5, H1, D1 chỉ là scales khác nhau. Một downtrend M1 có thể chỉ là pullback nhỏ trong uptrend H1.

Timeframe nhỏ cho nhiều observations nhưng nhiều noise. Timeframe lớn ít signals hơn nhưng context ổn định hơn.

Trader nên quy định từng timeframe làm nhiệm vụ gì. Ví dụ H1 cho bias, M15 cho zone, M5 cho entry. Mở quá nhiều timeframes thường tạo confirmation bias: zoom đến khi tìm được signal mình muốn.

## 6. Trend, range và market structure

Uptrend thường được mô tả Higher High và Higher Low. Downtrend có Lower High và Lower Low. Range là price oscillate giữa boundaries mà không có directional structure rõ.

BOS, Break of Structure, và CHoCH/MSS là terms phổ biến nhưng definitions khác nhau giữa communities. Nếu muốn backtest, phải định nghĩa rule objectively.

Ví dụ: “BOS bullish chỉ được công nhận khi M15 candle close trên swing high có ít nhất hai candles hai phía.” Rule có thể không hoàn hảo nhưng repeatable.

Trend-following strategy dễ bị whipsaw trong range. Mean reversion dễ chết trong strong trend. Nhận market regime quan trọng hơn việc tìm nhiều entry patterns.

## 7. Support và resistance

Support là vùng buyers từng đủ mạnh để ngăn hoặc đảo decline. Resistance là vùng sellers từng mạnh.

Nên coi là zones, không phải một pixel. Prior highs/lows, round numbers và congested areas có thể tập trung resting orders, trapped traders và attention.

Resistance sau breakout đôi khi trở thành support do short covering và missed buyers chờ retest. Nhưng không phải level nào cũng retest hoặc hold.

Support/resistance tốt nhất được dùng như location filter, không phải standalone signal.

## 8. Breakout, pullback và mean reversion

Breakout strategy kỳ vọng momentum tiếp tục sau khi price rời range hoặc level. Main risk là false breakout. Filters có thể là close, volume, volatility expansion hoặc retest nhưng không loại hết false signals.

Pullback strategy tham gia trend sau correction để có better entry và clearer invalidation.

Mean reversion kỳ vọng price đi quá xa mean rồi quay lại. Nó thường hợp range/liquid environment hơn strong trend. RSI oversold không tự động là buy signal nếu market đang repricing mạnh.

## 9. Volume, liquidity và volatility

Exchange-traded stocks/futures có centralized volume rõ hơn spot OTC Forex. Forex platforms thường dùng tick volume proxy.

Liquidity là khả năng trade size mà không gây price impact lớn. Liquid market có spread hẹp và depth tốt. Illiquid market có gaps và slippage lớn.

Volatility là magnitude và speed của price changes. ATR đo average range và có thể dùng để normalize stop distance.

Nếu ATR tăng gấp đôi mà stop giữ nguyên, strategy trở nên effectively tighter. Position size phải giảm nếu muốn giữ cùng dollar risk với stop rộng hơn.

## 10. Indicators

Indicator là transformation của price/volume, không phải nguồn thông tin thần bí.

Moving Average làm mượt price và có thể dùng trend filter. RSI đo momentum tương đối; RSI >70 không đồng nghĩa phải short. MACD mô tả momentum/trend relationship. Bollinger Bands kết hợp mean và volatility. VWAP là volume-weighted average price, phổ biến intraday. ATR đo volatility.

Không dùng năm indicators cùng đo momentum rồi gọi đó là năm confirmations. Mỗi tool nên có một nhiệm vụ.

## 11. SMC/ICT nên hiểu thế nào?

Smart Money Concepts/ICT dùng terms như liquidity sweep, order block, fair value gap, premium-discount và structure shift.

Liquidity sweep thường mô tả price xuyên prior high/low rồi quay lại. FVG mô tả imbalance ba-candle. Order block thường được trader coi là area trước displacement mạnh.

Vấn đề là definitions chủ quan. Để test, bạn phải biến thành rule. Ví dụ: H1 uptrend, price vào H1 demand, sweep M15 low, M5 close structure shift, entry first retracement, stop dưới sweep, target prior high.

Không tin một concept chỉ vì được gọi “institutional”. Data của cách bạn execute mới quyết định edge.

## 12. Multi-timeframe analysis

Context và execution nên tách. H1 có thể quyết định regime; M15 tìm setup; M5 entry.

M1 lower low không tự động đảo H1 uptrend. Mỗi timeframe có structure riêng.

Việc liên tục đổi timeframe sau khi vào lệnh thường là dấu hiệu bạn chưa có rule rõ.

## 13. Forex từ con số 0

EUR/USD 1,1000 nghĩa 1 EUR = 1,10 USD. EUR là base, USD quote. Buy EUR/USD = long EUR, short USD.

USD/JPY 150 nghĩa 1 USD = 150 JPY. Pair tăng nghĩa USD mạnh tương đối hoặc JPY yếu tương đối.

Major pairs có currencies lớn và thường liquidity tốt. Cross không có USD trực tiếp. Exotic pairs thường spread rộng và country risk cao hơn.

Retail spot Forex thường OTC, không giống centralized stock exchange. Vì vậy broker entity và execution model quan trọng.

## 14. Pip, point, lot và contract size

Với nhiều FX pairs, 1 pip = 0,0001. EUR/USD 1,1000 → 1,1001 là 1 pip. JPY pairs thường 0,01.

Broker có thể quote thêm decimal nhỏ hơn, gọi pipette/point tùy platform.

Standard lot thường = 100.000 units base currency; 0,1 lot = 10.000; 0,01 = 1.000 trong retail FX standard convention.

Với EUR/USD và USD account, 1 standard lot thường khoảng $10/pip trong common setup. Nhưng phải tính theo pair/account currency cụ thể.

XAUUSD contract specs khác broker; không áp FX pip rules máy móc.

## 15. Leverage và margin

Leverage cho phép control notional lớn hơn capital posted. Nếu leverage 1:100, notional $100.000 có thể cần khoảng $1.000 margin theo simplified calculation:

`Margin ≈ Notional / Leverage`

Margin không phải max loss. Account $2.000 control $100.000 notional; market move 1% tương ứng khoảng $1.000 P/L trước costs. Underlying move nhỏ có thể làm equity giảm 50%.

Leverage limit cao không bắt bạn dùng full leverage. Professional risk comes from position size, không từ con số broker quảng cáo.

## 16. Balance, equity, free margin và stop-out

Balance là realized account value sau closed trades. Equity = balance + floating P/L.

Used margin là collateral cho open positions. Free margin = equity trừ used margin.

Margin Level thường:

`Equity / Used Margin × 100%`

Broker có margin-call và stop-out thresholds. Khi margin level thấp, system có thể force-close positions theo policy.

Nếu bạn không biết stop-out rule, chưa nên trade live leveraged products.

## 17. Spread, commission, slippage và swap

Spread là ask-bid. Buy mở tại ask và P/L thường âm ngay khoảng spread.

Commission có thể tính per lot hoặc notional. Raw spread account thường có explicit commission.

Slippage là chênh giữa requested và fill. CPI/FOMC có thể làm liquidity vanish và slippage rất lớn.

Swap là overnight financing adjustment. Có thể positive hoặc negative tùy pair, direction, rate differential và broker markup. Strategy hold nhiều ngày phải tính swap.

## 18. Carry trade

Carry trade vay/fund bằng low-yield currency để long higher-yield currency/assets.

Positive carry không bảo vệ khỏi FX loss lớn. Carry strategies dễ tổn thương khi volatility spike và risk-off gây unwinding.

JPY historically là funding currency trong nhiều regimes do low rates; khi carry unwind, JPY có thể strengthen nhanh.

## 19. Position sizing

Account $10.000, risk 0,5% → risk amount $50.

Nếu stop 25 pips, acceptable value = $2/pip. Nếu EUR/USD 1 lot ≈ $10/pip, position ≈ 0,2 lot.

`Position size = Risk amount / (Stop distance × Value per point)`

Thứ tự đúng là xác định invalidation/stop từ chart trước, rồi tính size. Không chọn lot trước rồi ép stop để đúng dollar loss.

Stop rộng gấp đôi thì size khoảng một nửa nếu cùng risk.

## 20. Stop loss và invalidation

Stop là nơi thesis/setup không còn hợp lệ hoặc risk vượt rule.

Structural stop nằm ngoài swing/level. Volatility stop dựa ATR. Time stop thoát nếu expected move không xảy ra trong thời gian định trước.

Không dời stop xa hơn chỉ để tránh nhận loss. Dollar risk được kiểm soát bằng position size, không bằng việc đặt stop tùy theo cảm xúc.

Break-even và trailing rules phải được backtest; dời BE quá sớm có thể giết winners.

## 21. Take profit, R-multiple và expectancy

Nếu risk $50, 1R = $50. Win $100 = +2R, loss full stop = -1R.

R giúp so trades bất kể account size.

RR 1:3 không tự động tốt. Break-even win rate lý thuyết khoảng 25% nếu win đúng 3R và loss 1R, nhưng actual costs và missed fills làm khác.

Partial exit có thể giảm volatility nhưng cũng giảm average win. Phải test exact rule.

## 22. Risk of ruin

Risk of ruin tăng khi risk per trade lớn, edge nhỏ và outcomes correlated.

Risk 10%/trade khiến losing streak bình thường trở thành catastrophe. Risk 0,25–0,5% phù hợp hơn cho learning/live validation khi edge chưa chắc chắn.

Daily loss limit như -2R có thể ngăn tilt. Weekly drawdown threshold có thể buộc pause và review.

Không tăng size để “gỡ”. Martingale biến sequence risk thành blow-up risk.

## 23. Trading sessions

Asia active hơn với JPY/AUD/NZD và regional flows. London mở tăng liquidity EUR/GBP. New York có USD macro data và overlap với London.

Gold thường active mạnh London/NY, đặc biệt quanh US data.

Session high/low có thể là liquidity references. Nhưng session behavior không phải law; cần statistics của instrument/setup.

Chọn session phù hợp lifestyle. Strategy yêu cầu trade lúc bạn thiếu ngủ thường không sustainable.

## 24. News trading

Major data làm spread widen và slippage. CPI, NFP, FOMC, central-bank decisions và geopolitical headlines là examples.

Đặt buy-stop/sell-stop hai phía trước news không phải arbitrage. Whipsaw có thể trigger cả hai, spread mở rộng và fills xấu.

Professional news trading cần consensus, whisper, positioning và reaction function, không chỉ đoán Actual.

Người mới nên tránh mở new position ngay trước high-impact events nếu system chưa được thiết kế cho news.

## 25. Futures trading

Futures có standardized multiplier, tick, expiry và margin. P/L tính theo contract spec.

Daily mark-to-market nghĩa loss thực hiện qua margin process. Không thể “cứ giữ đến khi hồi” nếu margin cạn.

Index futures có thể hedge equity beta. Nhưng hedge ratio cần tính; short arbitrary number contracts có thể overhedge.

Basis và roll matters khi giữ qua expiries.

## 26. Options trading

Long call không chỉ là bullish. P/L phụ thuộc underlying move, time và IV. Long put tương tự ở downside.

Theta làm long options decay theo time, vega tạo sensitivity với IV. IV crush sau earnings có thể làm option lỗ dù direction đúng.

Short options nhận premium nhưng tail risk lớn. Covered call và cash-secured put dễ hiểu hơn naked positions nhưng vẫn có opportunity/downside trade-offs.

Options phù hợp defined-risk structures nhưng cần hiểu payoff trước Greeks nâng cao.

## 27. XAUUSD

Gold/USD có volatility lớn và hấp dẫn retail traders. Nó nhạy US real yields, DXY, Fed repricing, geopolitics và central-bank demand.

CPI, NFP và FOMC có thể tạo moves lớn. Spread/slippage cũng tăng.

Trước trade phải đọc contract size. Nếu 1 lot = 100 oz theo broker spec, $1 move có P/L rất khác FX pair. Tính tick value, stop dollars và margin trước.

Bắt đầu H1/M15/M5 context tốt hơn scalping M1 với oversized leverage.

## 28. Backtest

Backtest trả lời: nếu thực hiện rule này nhiều lần trong historical data, distribution thế nào?

Record instrument, date, session, context, entry, stop, target, result R, costs, MFE, MAE và screenshot nếu có.

100 trades là starting point thường hữu ích nhưng không phải magic number. Cần nhiều market regimes.

Metrics gồm win rate, average win/loss, expectancy, Profit Factor, max drawdown và losing streak.

Backtest không chứng minh future profitability; nó loại bớt systems không có evidence.

## 29. Forward test

Forward test chạy rule trong live time mà không biết future. Demo kiểm mechanics. Live minimum size kiểm emotion, slippage và actual execution.

Không scale dựa 5 winners. Scale dựa sample đủ và rule adherence ổn.

Nếu live performance khác backtest, tách vấn đề execution, costs, regime và strategy degradation.

## 30. Journal

Journal cần lưu setup, context, entry, stop, target, risk, result R và rule adherence.

Một winner phá rule là bad process. Một -1R loss đúng rule là valid sample.

Weekly review tìm lỗi lặp: overtrade sau loss, cut winners, trade ngoài session, poor sleep, news violations.

Journal biến memory bias thành data.

## 31. Overfitting và statistical bias

Overfitting xảy ra khi thêm quá nhiều filters để historical equity curve đẹp. System có 15 conditions có thể fit noise.

Look-ahead bias dùng information chưa có tại thời điểm trade. Survivorship bias test chỉ assets còn sống. Selection bias chọn period vì biết trước nó phù hợp.

Robust system thường vẫn hoạt động khi parameters thay đổi nhẹ và có economic/behavioral logic.

Out-of-sample và walk-forward testing giúp kiểm tra nhưng không loại uncertainty.

## 32. Psychology và process

Fear thường là size problem. FOMO thường là missing-plan problem. Revenge trading là emotional response to loss.

Thay vì “cố kỷ luật”, thiết kế system: max trades/day, fixed risk, daily stop, news rules và condition không trade khi sleep deprived.

Tilt signs gồm tăng lot, entry sớm, bỏ stop và trade setup không tồn tại. Rule “hai violations → stop session” cụ thể hơn lời hứa bình tĩnh.

Variance cần được chấp nhận trước. Profitable system 45% win vẫn có losing streak dài.

## 33. Xây trading system

System phải định nghĩa market, session, timeframe, context, setup, entry, stop, target, risk, news filter và no-trade conditions.

Ví dụ XAUUSD: trade London và first two hours NY; H1 trend; M15 pullback zone; M5 sweep + structure shift; first retracement entry; stop beyond sweep; target 2R; risk 0,25%; không entry gần CPI/NFP/FOMC.

Đây chưa phải profitable system, nhưng đủ objective để test.

Sau backtest, record expectancy, drawdown và losing streak để biết expected pain trước live.

## 34. Execution quality

Backtest thường assume perfect fills. Live có queue, spread, slippage và latency.

Limit order kiểm price nhưng có fill risk/adverse selection. Momentum breakout đôi khi cần market/stop order vì missing trade cost lớn hơn small slippage.

Stop-market ưu tiên exit; stop-limit có thể không fill trong gap.

Scalping edge nhạy execution hơn swing. Live forward test bắt buộc nếu strategy margin nhỏ.

## 35. Portfolio heat và correlation

Long EUR/USD, GBP/USD và gold có thể cùng là short-USD bet. Ba trades 0,5% không phải ba independent risks.

Portfolio heat là total open risk, nhưng correlation cần được xét. Highly correlated positions có effective risk gần tổng nominal risk.

Nếu đã long Nasdaq và semiconductor ETF, long chip stock tăng concentration.

Risk cap theo factor giúp tránh một macro surprise làm nhiều positions stop cùng lúc.

## 36. Kelly criterion

Kelly criterion tìm fraction tối đa long-run logarithmic growth khi probability và payoff known.

Trading không biết probability chính xác và distributions thay đổi, nên full Kelly rất aggressive. Estimation error dễ dẫn overbetting.

Fractional Kelly hoặc simple fixed risk thường thực tế hơn.

Bài học chính: size phải liên hệ edge và uncertainty, không phải confidence cảm tính.

## 37. Monte Carlo

Cùng set 100 outcomes nhưng order khác tạo drawdown khác. Backtest equity curve chỉ là một sequence.

Monte Carlo reshuffle/simulate sequences để ước lượng range of drawdowns và losing streaks.

Historical max streak 6 không nghĩa future không có 10. Sizing phải survive bad-but-plausible paths.

## 38. Profit Factor, Sharpe, Sortino và Calmar

Profit Factor = gross profit / gross loss. >1 nghĩa sample gross positive trước uncertainty.

Sharpe đo excess return per volatility nhưng penalize upside/downside như nhau. Sortino tập trung downside deviation. Calmar so annualized return với max drawdown.

Không optimize một metric. High Sharpe short-volatility strategy có thể giấu crash risk.

R-based expectancy và drawdown vẫn là language trực quan cho retail trader.

## 39. MAE/MFE

MAE là maximum adverse excursion; MFE maximum favorable excursion.

Nếu winners thường MAE <0,4R nhưng stop 1,2R, có thể nghiên cứu stop efficiency. Nếu trades thường đạt +2R rồi reverse trước target +3R, exit logic có thể cần review.

Đừng optimize trực tiếp trên same sample rồi tin ngay. Candidate rule phải được out-of-sample test.

MAE/MFE giúp biến stop/target từ cảm giác thành data.

## 40. Regime filter

Trend systems hoạt động tốt hơn directional regimes. Mean reversion tốt hơn stable ranges. Carry tốt hơn low-volatility risk-on. Breakout dễ fail trong chop.

Regime filter có thể dựa volatility, trend strength, macro event hoặc cross-asset condition.

Filter phải có simple rationale. 12 filters để loại mọi historical loss thường là overfit.

Hỏi: edge của strategy đến từ hiện tượng nào và khi nào hiện tượng đó biến mất?

## 41. Broker safety

Với OTC Forex/CFD, broker risk là real risk. Kiểm legal entity, regulator, client-money segregation, margin-closeout, negative-balance policy, dispute mechanism và withdrawal terms.

Một brand có nhiều entities. Protection của offshore entity có thể khác entity regulated ở major jurisdiction.

Test withdrawal trước khi tăng deposit. Leverage cực cao, guaranteed return, managed account opaque hoặc yêu cầu gửi crypto tới ví cá nhân là red flags.

Dùng 2FA và bảo vệ email/account credentials.

## 42. Trading như một business

Net P/L phải trừ commission, spread, slippage, swap, data/platform costs và applicable tax.

Opportunity cost của time cũng quan trọng. Strategy 3%/năm nhưng cần sáu giờ chart mỗi ngày có thể kém passive investing + career income.

Capacity giới hạn scale. Small-cap scalp có thể không handle large capital; liquid futures có capacity khác.

Review như business: phân biệt strategy error, execution error và variance. Không đổi model vì ba bad days.

## 43. Lộ trình demo → live

Giai đoạn một học mechanics: pair, pip, lot, margin, P/L và orders. Nếu chưa tự tính được risk, không live.

Giai đoạn hai chọn một market và một setup. Backtest ít nhất một sample đủ lớn và nhiều regimes. Không sửa rule giữa sample để cứu results.

Giai đoạn ba forward-test demo. Sau khi execution ổn, live với minimum size và risk nhỏ như 0,25–0,5% nếu phù hợp strategy.

Vài chục live trades đầu dùng để validate execution, không phải làm giàu. Scale chỉ khi data live nằm trong range expected.

Không trade bằng emergency fund, tiền thuê nhà hoặc debt. Tách investment account và trading account. Một trade lỗ không được biến thành investment chỉ vì không muốn accept loss.

Trading tốt là process quản trị uncertainty, không phải tìm cách luôn đúng.

## Nguồn nền tảng

CFTC Retail Forex Advisory: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html

FINRA Order Types: https://www.finra.org/investors/investing/investment-products/stocks/order-types
