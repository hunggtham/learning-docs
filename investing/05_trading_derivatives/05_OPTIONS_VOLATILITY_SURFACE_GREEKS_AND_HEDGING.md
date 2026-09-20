# Options, bề mặt biến động, Greeks và hedging

> Option không chỉ là công cụ “đoán tăng hay giảm”. Giá option phản ánh một phân phối xác suất, thời gian, volatility và trạng thái thị trường. Chương này tập trung vào cách đọc option theo **direction + volatility + time + convexity + liquidity + margin**.

# Phần I — Từ spot tới forward

## 1. Spot và forward

Giá option liên quan không chỉ spot hiện tại mà còn forward value của underlying.

Forward chịu ảnh hưởng của:

- interest rate;
- dividend;
- borrow cost;
- storage/carry tùy tài sản.

## 2. Carry

Carry là lợi ích hoặc chi phí kinh tế của việc giữ exposure qua thời gian.

Với equity index, dividend và rate ảnh hưởng forward. Với commodity, storage và convenience yield cũng quan trọng.

## 3. Moneyness theo forward

Khi phân tích option chuyên sâu, ATM theo forward thường có ý nghĩa hơn chỉ so strike với spot.

# Phần II — Giá option và phân phối

## 4. Option là payoff theo trạng thái

Option tạo payoff khác nhau tùy trạng thái giá tương lai.

```text
Call = max(S-K, 0)
Put  = max(K-S, 0)
```

Điều này tạo **convexity**: payoff không tuyến tính với underlying.

## 5. Implied volatility

Implied volatility (IV) là mức volatility làm model phù hợp với market option price.

Nó không phải dự báo chắc chắn của realized volatility.

## 6. Realized volatility

Realized volatility là biến động thực tế xảy ra trong quá trình giá di chuyển.

Một volatility strategy thường đặt cược vào quan hệ:

```text
Implied Volatility
vs
Future Realized Volatility
```

## 7. Volatility risk premium

Trong nhiều thị trường, option protection thường có giá cao hơn realized volatility trung bình vì người mua sẵn sàng trả phí bảo hiểm tail risk.

Khoảng này thường được gọi là **volatility risk premium**.

Nó không phải “free money”; seller nhận premium để chịu risk trong trạng thái xấu.

# Phần III — Greeks bậc một

## 8. Delta

Delta đo thay đổi nhỏ của option value khi underlying thay đổi.

Nó cũng có thể được dùng như một approximation cho directional exposure.

Nhưng Delta thay đổi theo spot, time và IV.

## 9. Gamma

Gamma đo mức Delta thay đổi khi spot thay đổi.

```text
Long Option → thường Long Gamma
Short Option → thường Short Gamma
```

Long Gamma hưởng lợi từ move lớn hơn kỳ vọng nếu có thể hedge phù hợp; short Gamma chịu risk khi market chạy mạnh.

## 10. Theta

Theta đo time decay khi các yếu tố khác giữ nguyên.

Long option thường mất time value theo thời gian. Short option thường thu Theta nhưng đổi lại chịu Gamma/tail risk.

## 11. Vega

Vega đo sensitivity với thay đổi implied volatility.

Long Vega hưởng lợi khi IV tăng; short Vega ngược lại.

## 12. Rho

Rho đo sensitivity với rate.

Nó thường nhỏ hơn Delta/Vega ở option ngắn hạn nhưng đáng chú ý ở long-dated options.

# Phần IV — Greeks bậc cao

## 13. Vanna

Vanna mô tả tương tác giữa Delta và volatility.

Nó giúp hiểu vì sao option exposure có thể đổi khi spot và IV cùng thay đổi.

## 14. Vomma / Volga

Vomma đo độ cong của option value theo volatility, tức Vega thay đổi ra sao khi IV thay đổi.

## 15. Charm

Charm mô tả Delta thay đổi theo thời gian khi spot giữ nguyên.

Gần expiry, các hiệu ứng thời gian có thể trở nên rất mạnh.

## 16. Không dùng Greek riêng lẻ

Greeks là local sensitivity, tức approximation quanh trạng thái hiện tại.

Khi market jump lớn, cần scenario grid thay vì chỉ nhân Greek với move.

# Phần V — Volatility smile và skew

## 17. IV không giống nhau cho mọi strike

Nếu Black-Scholes assumptions hoàn toàn đúng, volatility theo strike có thể phẳng hơn thực tế.

Trong market thật, downside puts và upside calls thường có IV khác nhau.

## 18. Equity skew

Equity index thường có downside put IV cao hơn ATM vì demand bảo hiểm và crash risk.

Đây thường được gọi là negative skew.

## 19. Risk reversal

Risk reversal so IV của call và put ở moneyness tương ứng.

Nó giúp đo asymmetry trong demand và perceived tail risk.

## 20. Curvature / butterfly

Curvature đo mức wings đắt hay rẻ so ATM.

Nó liên quan tail probability và demand cho far OTM options.

# Phần VI — Term structure

## 21. Volatility theo kỳ hạn

IV khác nhau theo expiry tạo **volatility term structure**.

Near-term event có thể làm front expiry cao trong khi long expiry ít thay đổi.

## 22. Event volatility

Earnings, CPI, FOMC hoặc court decision có thể tập trung uncertainty vào một ngày cụ thể.

Sau event, phần volatility liên quan sự kiện thường biến mất nhanh.

## 23. Calendar spread

Calendar spread tạo exposure giữa option cùng strike nhưng khác expiry.

P/L phụ thuộc term structure, spot path và relative Vega/Theta.

# Phần VII — Volatility surface

## 24. Surface là gì?

Volatility surface là IV theo hai chiều chính:

```text
Strike / Moneyness
×
Expiry
```

Surface thay đổi liên tục khi spot, flow và risk perception đổi.

## 25. Sticky strike vs sticky delta

Các cách mô tả surface dynamics khác nhau giả định IV “đi theo” strike hay delta theo cách khác nhau.

Đây là approximation; market thực có thể đổi regime.

## 26. Vol-of-vol

Volatility của volatility (vol-of-vol) đo mức IV bản thân nó biến động mạnh ra sao.

Trong crisis, cả spot vol và vol-of-vol có thể tăng.

# Phần VIII — Gamma scalping

## 27. Ý tưởng cơ bản

Một trader long Gamma có thể điều chỉnh Delta nhiều lần khi spot di chuyển.

Một mô tả đơn giản:

```text
Long Gamma
→ Spot ↑ → Delta ↑ → sell underlying để hedge
→ Spot ↓ → Delta ↓ → buy underlying để hedge
```

Nếu realized movement đủ lớn so option premium và transaction cost, gamma scalping có thể bù time decay.

## 28. Không phải arbitrage miễn phí

Kết quả phụ thuộc:

- realized volatility;
- implied volatility paid;
- hedge frequency;
- spread;
- slippage;
- jump risk.

# Phần IX — Delta hedging

## 29. Delta-neutral không bằng risk-free

Một position Delta gần 0 vẫn có thể có:

- Gamma;
- Vega;
- Theta;
- skew;
- jump risk.

Do đó “delta neutral” chỉ nói một lớp exposure tại thời điểm hiện tại.

## 30. Dynamic hedging

Khi Delta thay đổi, hedge cần được cập nhật.

Hedging quá thường tăng cost; hedging quá ít tăng directional risk.

# Phần X — Assignment, expiry và pin risk

## 31. Early assignment

American-style option có thể bị exercise trước expiry, đặc biệt quanh dividend hoặc khi time value rất thấp.

## 32. Pin risk

Nếu spot ở gần strike khi expiry, final assignment có thể không chắc chắn và tạo underlying position ngoài ý muốn.

## 33. Weekend / overnight gap

Option position còn chịu jump khi market đóng mà không thể rebalance Delta.

# Phần XI — Dollar Greeks

## 34. Vì sao cần chuyển Greek thành tiền?

Greek theo mỗi option khó tổng hợp nếu position có nhiều multiplier.

Có thể chuyển thành:

- dollar Delta;
- dollar Gamma;
- dollar Vega;
- DV01 nếu liên quan rates.

Điều này giúp portfolio aggregation.

## 35. Contract multiplier

Luôn nhân Greek với contract multiplier và quantity đúng.

Một lỗi multiplier có thể làm risk estimate sai hàng chục hoặc hàng trăm lần.

# Phần XII — Option portfolio

## 36. Tổng hợp theo state

Không nên chỉ cộng Delta hiện tại.

Hãy stress:

```text
Spot -10%, -5%, 0, +5%, +10%
×
IV -10 vol, 0, +10 vol
×
Time: today / +1 week / expiry-near
```

## 37. Scenario grid

Scenario grid cho thấy nonlinear exposure rõ hơn một Greek duy nhất.

## 38. Correlation risk

Multi-asset option book còn chịu correlation giữa underlying.

Worst-of structured products đặc biệt nhạy correlation.

# Phần XIII — Tail hedging

## 39. Mục tiêu của tail hedge

Tail hedge nhằm giảm loss trong trạng thái cực đoan, không nhất thiết kiếm tiền trung bình mỗi tháng.

## 40. Chi phí bảo hiểm

Long put lặp lại tạo negative carry.

Đánh giá hedge cần theo nhiều năm và toàn portfolio, không chỉ hỏi “tháng này put có lời không?”.

## 41. Hedge budget

Có thể định trước tỷ lệ annual premium cho protection.

Điều này tránh mua bảo hiểm quá nhiều sau khi IV đã tăng mạnh.

## 42. Put spread

Put spread giảm premium bằng cách bán put strike thấp hơn, nhưng bảo vệ bị giới hạn trong tail sâu.

## 43. Collar

Collar dùng short call để tài trợ một phần long put, đổi lại mất upside trên strike call.

# Phần XIV — Event options

## 44. Implied move

Option market có thể được dùng để ước lượng move được price quanh event.

Nếu realized move nhỏ hơn implied move, long option có thể lỗ dù đoán đúng direction.

## 45. IV crush

Sau event, uncertainty biến mất làm IV có thể giảm mạnh.

P/L của long option:

```text
Directional Gain
+/- Vega Effect
- Theta
- Execution Cost
```

## 46. Earnings options

Earnings còn có gap risk và asymmetric information.

Backtest dùng close-to-close đơn giản dễ đánh giá sai fill và IV dynamics.

# Phần XV — Skew trades

## 47. Skew không phải direction thuần

Mua put đắt và bán call rẻ có thể tạo bet vào asymmetry chứ không chỉ bearish view.

## 48. Skew có thể steepen trong stress

Khi demand downside protection tăng, OTM put IV có thể tăng nhanh hơn ATM.

Do đó put P/L có thể hưởng cả Delta và skew move.

# Phần XVI — Short-vol risk

## 49. Theta income và tail loss

Short option thường có P/L profile:

```text
Nhiều khoản lời nhỏ
+ thỉnh thoảng loss rất lớn
```

Cần stress beyond historical daily moves.

## 50. Margin expansion

Khi volatility tăng, broker/clearing margin có thể tăng đúng lúc short option đang lỗ.

P/L risk và liquidity risk xảy ra đồng thời.

# Phần XVII — Data và backtest options

## 51. Option data khó hơn spot data

Cần xử lý:

- strike;
- expiry;
- bid/ask;
- stale quote;
- corporate action;
- early exercise;
- multiplier;
- surface interpolation.

## 52. Mid-price bias

Backtest dùng midpoint cho mọi fill thường quá lạc quan, đặc biệt ở OTM hoặc illiquid options.

## 53. Survivorship của contract

Option chain thay đổi liên tục; phải dùng chain tồn tại thật tại thời điểm đó.

## 54. IV estimation

Bad quotes có thể tạo IV vô lý. Cần filter và arbitrage-consistency checks phù hợp.

# Phần XVIII — Hedging thực tế

## 55. Hedge đúng factor

```text
Equity Beta
→ Index Futures / Put

Rate Risk
→ Rate Futures / Swap

FX Risk
→ Forward / Option

Volatility Risk
→ Options / Vol Instrument
```

## 56. Basis risk

Hedge bằng instrument gần giống nhưng không trùng underlying tạo basis risk.

Ví dụ hedge cổ phiếu bán dẫn Hàn Quốc bằng Nasdaq futures chỉ giảm một phần global-tech beta, không loại company/Korea-specific risk.

## 57. Overhedging

Hedge quá lớn có thể biến portfolio thành position ngược chiều thay vì giảm risk.

## 58. Rebalancing hedge

Delta hoặc beta thay đổi theo market, vì vậy hedge ratio cần review.

# Phần XIX — Attribution

## 59. P/L option nên được phân rã

Một framework:

```text
Delta Effect
Gamma Effect
Theta
Vega / IV
Skew / Surface
Rates / Carry
Execution
Residual
```

## 60. Đúng direction nhưng sai trade

Underlying đi đúng hướng không chứng minh option choice tốt.

Có thể lỗ vì:

- premium quá đắt;
- IV crush;
- expiry quá ngắn;
- spread lớn.

# Phần XX — Checklist trước khi giao dịch option

## 61. Contract

```text
Underlying?
Strike?
Expiry?
Style?
Multiplier?
Settlement?
Liquidity?
```

## 62. Risk

```text
Delta?
Gamma?
Theta?
Vega?
Skew?
Margin?
Assignment?
Gap Risk?
```

## 63. Scenario

```text
Nếu spot không move?
Nếu spot move đúng nhưng IV giảm?
Nếu spot gap mạnh?
Nếu volatility tăng?
Nếu phải exit sớm?
```

## Kết luận

Option nên được nhìn như một hợp đồng phụ thuộc nhiều trạng thái, không chỉ là vé cược direction.

Chuỗi phân tích chuẩn:

```text
Underlying / Forward
→ Payoff
→ IV / Surface
→ Greeks
→ Time
→ Liquidity / Margin
→ Scenario Grid
→ Hedge / Attribution
```

Một option trade tốt cần đúng **giá, volatility, thời gian và cấu trúc payoff**, không chỉ đúng hướng của underlying.
