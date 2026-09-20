# 05 — Options, Volatility Surface, Greeks và Hedging Chuyên Sâu

> Options không chỉ là công cụ “đoán tăng hay giảm”. Chúng là hợp đồng định giá probability distribution, time, volatility và convexity. Chapter này đi từ payoff cơ bản tới volatility surface, Greeks interaction, skew, term structure, hedging và những sai lầm thường gặp khi dùng options để trading hoặc bảo vệ portfolio.

## 1. Option Price phản ánh nhiều biến cùng lúc

Giá option không chỉ phụ thuộc underlying tăng hay giảm. Một premium có thể thay đổi vì spot price, strike, time to expiry, implied volatility, interest rate và dividend assumption.

Do đó việc đúng hướng nhưng vẫn lỗ là hoàn toàn có thể nếu IV giảm hoặc time decay lớn hơn directional gain.

## 2. Intrinsic Value và Time Value

Call intrinsic value:

```text
max(S - K, 0)
```

Put intrinsic value:

```text
max(K - S, 0)
```

Phần premium vượt intrinsic value là time value. Time value phản ánh khả năng option trở nên có giá trị hơn trước expiry.

## 3. Moneyness

Option có thể ITM, ATM hoặc OTM. Nhưng moneyness không chỉ là label. Nó ảnh hưởng Delta, Gamma, Vega và Theta.

ATM options thường có Gamma và Vega sensitivity lớn hơn tương đối so với deep ITM/OTM options.

## 4. Delta

**Delta** đo option price thay đổi xấp xỉ bao nhiêu khi underlying thay đổi 1 unit.

Delta không cố định. Nó thay đổi theo spot, volatility và time.

Một call ATM có thể Delta khoảng 0.5 như intuition, nhưng con số thực tế phụ thuộc model và market conditions.

## 5. Delta không phải Probability tuyệt đối

Delta đôi khi được dùng như approximation của probability kết thúc ITM trong một số assumptions, nhưng không nên coi nó là xác suất khách quan đơn giản.

Model measure, drift assumption và market pricing làm interpretation phức tạp hơn.

## 6. Gamma

**Gamma** đo tốc độ thay đổi của Delta khi underlying thay đổi.

Long option thường long gamma; short option thường short gamma. Long gamma có convexity: movement lớn có thể giúp position nhiều hơn linear exposure.

## 7. Gamma và Rebalancing

Một delta-hedged long-gamma position thường cần mua khi market giảm và bán khi market tăng để giữ delta gần zero. Nếu realized volatility đủ cao so với implied cost, gamma scalping có thể có economics tích cực trước costs.

Nhưng trading friction có thể ăn hết edge.

## 8. Theta

**Theta** đo time decay gần đúng. Long options thường chịu negative theta; short options thường hưởng positive theta.

Nhưng “theta income” không phải free return. Short option nhận theta để chịu gamma/tail risk.

## 9. Vega

**Vega** đo sensitivity với implied volatility.

Long options thường long vega. Nếu IV giảm mạnh sau event, long option có thể mất giá dù underlying move đúng hướng.

Đây là cơ chế phía sau **IV crush**.

## 10. Rho

**Rho** đo sensitivity với interest rate. Rho thường ít được retail trader chú ý ở short-dated equity options nhưng có thể quan trọng hơn với long-dated options hoặc rates-sensitive structures.

## 11. Greeks tương tác chứ không độc lập

Một position có thể long Delta, long Gamma, short Theta và long Vega cùng lúc. Khi spot thay đổi, toàn bộ Greek profile thay đổi.

Vì vậy chỉ nhìn một Greek tại thời điểm entry là chưa đủ.

## 12. Higher-order Greeks

Các desk chuyên nghiệp có thể theo dõi Vanna, Vomma/Volga, Charm hoặc Speed. Người học không cần thuộc hết ngay, nhưng nên hiểu lý do chúng tồn tại: first-order Greeks cũng thay đổi khi spot, volatility và time thay đổi.

## 13. Implied Volatility

**Implied Volatility (IV)** là volatility input khiến model price bằng market price. Nó không phải forecast chắc chắn của realized volatility.

IV phản ánh supply/demand, tail risk premium và uncertainty.

## 14. Realized Volatility vs Implied Volatility

Realized volatility nhìn backward hoặc được estimate từ price path. Implied volatility nhìn từ option price hiện tại.

Một core relative-value question là:

```text
Market đang price bao nhiêu volatility?
Thực tế có khả năng realize bao nhiêu?
```

## 15. Volatility Risk Premium

Equity index options thường có tendency implied volatility cao hơn realized volatility trung bình dài hạn do demand bảo hiểm downside. Chênh lệch này liên quan **volatility risk premium**.

Nhưng premium tồn tại vì short-vol strategy chịu loss lớn trong crash.

## 16. Volatility Smile và Skew

Nếu Black-Scholes assumptions hoàn hảo, cùng expiry có thể có IV tương tự qua strikes. Thực tế IV thay đổi theo strike, tạo smile hoặc skew.

Equity index thường có downside put skew: OTM puts có IV cao hơn vì demand bảo hiểm và crash risk.

## 17. Put Skew nói gì?

Put skew cao có thể phản ánh downside demand, leverage constraints hoặc market-maker inventory. Không nên kết luận đơn giản “skew cao = market chắc chắn crash”.

Skew là price của asymmetry, không phải oracle.

## 18. Term Structure of Volatility

IV thay đổi theo expiry. Normal regime có thể có upward-sloping term structure; event risk có thể làm short-dated IV spike.

Ví dụ earnings event thường concentrated trong expiry bao quanh ngày earnings.

## 19. Event Volatility

Option premium trước earnings, CPI hoặc election có thể chứa event variance. Sau event, uncertainty biến mất và IV có thể collapse.

Long straddle chỉ profitable nếu realized move đủ lớn so với move đã được priced.

## 20. Expected Move

Trader thường dùng ATM straddle price để ước lượng market-implied move. Đây là approximation, không phải confidence interval chính xác tuyệt đối.

Điểm quan trọng là so forecast của bạn với move đã được market price, không chỉ forecast direction.

## 21. Put–Call Parity

Put–call parity nối call, put, spot và present value của strike dưới assumptions chuẩn.

Nó cho thấy options không tồn tại độc lập; nhiều payoff có thể replicated bằng combination của underlying, cash và option khác.

## 22. Synthetic Positions

Long call + short put cùng strike/expiry có thể tạo synthetic long forward gần đúng. Hiểu synthetic positions giúp nhìn options như building blocks thay vì sản phẩm bí ẩn.

## 23. Vertical Spread

Bull call spread mua call strike thấp và bán call strike cao. Strategy giới hạn cả upside lẫn premium cost.

Spread không “an toàn” tuyệt đối; nó chỉ định hình payoff rõ hơn.

## 24. Credit Spread

Credit spread thu premium upfront nhưng thường short convexity trong một range. Max loss có thể giới hạn nếu spread defined-risk.

Positive probability of profit không đồng nghĩa positive expectancy.

## 25. Calendar Spread

Calendar spread sử dụng expiries khác nhau và nhạy với term structure, theta và vega. Nó không chỉ là bet direction.

## 26. Straddle

Long straddle mua call và put cùng strike/expiry, chủ yếu long volatility/gamma và negative theta.

Short straddle làm ngược lại: thu theta nhưng chịu convex tail risk.

## 27. Strangle

Strangle dùng OTM call và put, rẻ hơn straddle nhưng cần move lớn hơn để profitable.

## 28. Covered Call

Covered call = long stock + short call. Nó giảm một phần downside nhờ premium nhưng cap upside.

Không nên gọi covered call là “income miễn phí”; investor đang bán upside convexity.

## 29. Protective Put

Long stock + long put tạo downside floor gần giống insurance. Premium là insurance cost.

Protection càng dài và strike càng gần spot thường càng đắt.

## 30. Collar

Collar kết hợp protective put và short call để giảm insurance cost bằng cách bán một phần upside.

Đây là ví dụ rõ về risk transfer: muốn downside protection rẻ hơn thường phải từ bỏ upside hoặc chấp nhận điều kiện khác.

## 31. Tail Hedge

Tail hedge nhằm trả nhỏ đều đặn để nhận payoff lớn khi crash. Challenge là carry cost có thể kéo dài nhiều năm.

Một hedge chỉ hữu ích nếu investor đủ kỷ luật giữ nó trước khi event xảy ra.

## 32. Dynamic Hedging

Dynamic hedging điều chỉnh underlying exposure khi delta thay đổi. Nó yêu cầu liquidity và transaction cost thấp tương đối.

Trong jump market, continuous hedging assumption thất bại và gap risk vẫn tồn tại.

## 33. Jump Risk

Options models thường giả định price process khá liên tục. Earnings gap hoặc geopolitical shock có thể tạo jumps khiến delta hedge không bảo vệ hoàn hảo.

## 34. Pin Risk

Gần expiry, underlying quanh strike có thể làm assignment outcome không chắc chắn. Short options có thể để lại unexpected position sau expiry.

## 35. Early Exercise

American-style options có thể exercise trước expiry. Dividend, interest rate và deep ITM condition có thể ảnh hưởng optimal exercise.

## 36. Assignment Risk

Short option seller có thể bị assigned. Trader phải hiểu settlement convention, contract multiplier và exercise style của exchange cụ thể.

## 37. Cash-settled vs Physically Settled

Index options có thể cash-settled trong khi equity options có thể deliver shares. Economic exposure và operational requirement khác nhau.

## 38. Contract Multiplier

Premium quote nhỏ có thể che giấu notional lớn nếu multiplier cao. Luôn tính:

```text
Contract Exposure = Quoted Premium/Price × Contract Multiplier
```

và stress loss theo underlying move.

## 39. Open Interest và Volume

Open interest cho biết contracts outstanding, volume cho biết activity trong period. Cả hai hỗ trợ đánh giá liquidity nhưng không đủ một mình.

Bid-ask spread và depth vẫn rất quan trọng.

## 40. Market Maker Hedging

Option market makers thường hedge Delta và manage aggregate Greeks. Their flows có thể ảnh hưởng intraday market dynamics nhưng retail narratives về “dealer gamma” thường bị oversimplified.

Không nên biến một estimate dealer positioning thành deterministic prediction.

## 41. Volatility Surface

**Volatility surface** là IV theo cả strike và expiry. Nó cho analyst thấy market price asymmetry và term uncertainty như thế nào.

Surface có thể dịch chuyển, steepen, flatten hoặc twist.

## 42. Surface Risk

Một option strategy tưởng chỉ bet spot có thể thực tế bet surface shape. Ví dụ ratio spread hoặc calendar spread rất nhạy với skew/term-structure changes.

## 43. Hedging Equity Portfolio

Investor có thể dùng index puts, put spreads hoặc futures để giảm beta risk. Nhưng hedge ratio phải dựa trên beta/notional chứ không chỉ portfolio market value.

Approximation:

```text
Hedge Notional ≈ Portfolio Value × Portfolio Beta
```

## 44. Basis Risk trong Hedging

Nếu portfolio gồm Korean semiconductor stocks mà hedge bằng broad KOSPI futures, residual sector risk vẫn còn. Đây là **basis risk**.

## 45. Currency Options

FX options thêm dimension interest-rate differential và currency-specific skew. Hedging USD/KRW exposure bằng options có payoff asymmetry khác forward hedge.

## 46. Volatility Position Sizing

Option premium paid không phải lúc nào cũng là risk duy nhất. Short options, spreads và margin positions có nonlinear risk.

Position sizing phải stress underlying gaps và IV shifts, không chỉ max loss theo model nếu liquidity có thể biến mất.

## 47. Scenario Grid

Một useful option review là grid:

```text
Spot: -10%, -5%, 0%, +5%, +10%
IV: -10 vol, unchanged, +10 vol
Time: today, halfway, near expiry
```

Xem P/L across scenarios giúp hiểu position thật hơn một payoff chart tại expiry.

## 48. Options không tạo Edge tự động

Options chỉ thay đổi payoff distribution. Nếu forecast về probability/volatility không có edge, cấu trúc phức tạp hơn không tự tạo expectancy dương.

## 49. Common Mistake: Cheap OTM Option

Option premium rẻ tuyệt đối không nghĩa cheap theo volatility. Deep OTM lottery-like options có thể có rất high implied volatility.

## 50. Common Mistake: Selling High Win Rate

Short option strategy có thể thắng 90% trades và vẫn blow up nếu 10% losses cực lớn. Vì vậy expectancy và tail loss quan trọng hơn win rate.

## 51. Common Mistake: Ignore IV Rank Context

IV percentile/rank có thể hỗ trợ context nhưng không đủ để quyết định trade. High IV có thể hợp lý nếu event risk thật sự cao.

## 52. Common Mistake: Hold to Expiry mặc định

Greeks become nonlinear mạnh gần expiry, đặc biệt gamma. Trader cần biết mục tiêu của position là capture direction, volatility hay event premium để quyết định exit.

## 53. Options Research Workflow

Một workflow nên đi theo:

```text
Thesis
→ Spot View
→ Volatility View
→ Horizon
→ Desired Payoff
→ Strike/Expiry Selection
→ Greek Profile
→ Liquidity/Spread
→ Scenario Grid
→ Position Size
→ Exit/Adjustment Rule
```

## 54. Kết luận

Options là ngôn ngữ của **probability, convexity và insurance**. Học options đúng cách không bắt đầu từ strategy name mà bắt đầu từ câu hỏi: mình muốn exposure nào với Delta, Gamma, Theta và Vega; market đang price volatility ra sao; và mình sẵn sàng trả hoặc nhận premium để chịu loại risk nào.
