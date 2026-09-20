# Phái sinh: Futures, Options, Swaps và CFD

> Phái sinh (derivative) là hợp đồng có giá trị phụ thuộc vào một tài sản, chỉ số hoặc biến tham chiếu. Khác với mua cổ phiếu thông thường, phái sinh có thể tạo **nghĩa vụ, đòn bẩy, margin, collateral và payoff phi tuyến**. Vì vậy phải hiểu hợp đồng trước khi dự đoán giá.

# Phần I — Phái sinh là gì?

## 1. Ownership và derivative exposure khác nhau

Mua cổ phiếu thường tạo quyền sở hữu residual claim trong doanh nghiệp.

Mua futures, option hoặc CFD thường tạo **exposure theo hợp đồng**, không nhất thiết tạo quyền sở hữu underlying.

Do đó cần phân biệt:

```text
Underlying Asset
Contract
Legal Counterparty
Settlement
Collateral
```

## 2. Contract specification

Trước khi giao dịch một derivative cần biết:

- underlying;
- contract multiplier;
- tick size;
- tick value;
- expiry;
- settlement;
- trading hours;
- margin;
- currency;
- exercise style nếu là option.

Tên sản phẩm giống nhau không bảo đảm specification giống nhau.

## 3. Notional

Notional là quy mô kinh tế của exposure.

Với futures:

```text
Notional
= Futures Price × Contract Multiplier
```

Margin chỉ là collateral, không phải notional và không phải maximum loss.

# Phần II — Forward và Futures

## 4. Forward

Forward là hợp đồng hai bên cam kết mua/bán tài sản trong tương lai theo mức giá đã thỏa thuận.

Forward thường OTC nên counterparty risk và collateral terms rất quan trọng.

## 5. Futures

Futures được chuẩn hóa và thường giao dịch trên exchange với central clearing.

Standardization giúp thanh khoản tốt hơn nhưng trader phải tuân thủ multiplier, expiry và margin rules của contract.

## 6. Initial margin và maintenance margin

**Initial margin:** collateral cần để mở position.

**Maintenance margin:** mức tối thiểu cần duy trì.

Nếu equity rơi dưới yêu cầu, broker/clearing member có thể yêu cầu bổ sung hoặc đóng position.

## 7. Variation margin và mark-to-market

Futures thường được đánh dấu lại theo giá thị trường mỗi ngày.

```text
Price Move
→ Daily P/L
→ Cash transferred through margin system
```

Điều này làm liquidity management quan trọng dù thesis dài hạn đúng.

## 8. Basis

Basis là chênh lệch giữa futures và spot theo convention.

Nó chịu ảnh hưởng:

- interest rate;
- storage;
- dividend;
- convenience yield;
- borrow cost;
- supply/demand kỹ thuật.

## 9. Convergence

Gần expiry, futures và spot thường hội tụ theo cơ chế settlement/arbitrage, tùy sản phẩm.

Nếu không hiểu settlement, trader có thể giữ contract vào giai đoạn không mong muốn.

## 10. Contango và backwardation

**Contango:** giá futures xa kỳ hạn cao hơn gần kỳ hạn/spot trong một cấu trúc điển hình.

**Backwardation:** giá xa kỳ hạn thấp hơn.

Không nên kết luận bullish/bearish chỉ từ hai từ này. Cần hiểu carry, inventory và scarcity.

## 11. Roll

Trader muốn giữ exposure sau expiry phải chuyển từ contract cũ sang contract mới.

Roll có thể tạo:

- transaction cost;
- basis risk;
- roll yield;
- liquidity risk.

## 12. Commodity futures

Commodity futures còn chịu:

- storage cost;
- inventory;
- seasonality;
- physical delivery;
- convenience yield.

Trader tài chính phải đặc biệt hiểu rule giao hàng vật chất.

## 13. CTD trong bond futures

Một số bond futures cho phép seller giao nhiều loại bond đủ điều kiện. Bond kinh tế nhất để giao được gọi là **cheapest-to-deliver (CTD)**.

Do đó hedge Treasury futures không chỉ phụ thuộc futures price mà còn conversion factor và CTD dynamics.

# Phần III — Options

## 14. Call và Put

Payoff tại expiry:

```text
Call = max(S - K, 0)
Put  = max(K - S, 0)
```

Người mua option trả premium để có quyền. Người bán nhận premium nhưng nhận nghĩa vụ tương ứng.

## 15. Premium

Premium không chỉ là intrinsic value.

Trước expiry, option value còn phụ thuộc:

- time;
- implied volatility;
- rates;
- dividends;
- borrow;
- skew/surface.

## 16. Intrinsic và time value

```text
Option Value
= Intrinsic Value + Time Value
```

Time value có xu hướng giảm khi expiry tới gần, nhưng tốc độ không tuyến tính.

## 17. Moneyness

- ITM: in-the-money;
- ATM: at-the-money;
- OTM: out-of-the-money.

Moneyness ảnh hưởng Delta, Gamma, liquidity và probability distribution của payoff.

# Phần IV — Greeks

## 18. Delta

Delta đo độ nhạy option price với thay đổi nhỏ của underlying.

Delta không cố định; nó thay đổi theo spot, time và volatility.

## 19. Gamma

Gamma đo tốc độ Delta thay đổi khi underlying thay đổi.

Long option thường có Gamma dương; short option thường có Gamma âm.

Short Gamma có thể chịu lỗ tăng rất nhanh khi market move lớn.

## 20. Theta

Theta mô tả time decay.

Long option thường trả chi phí thời gian. Short option thường thu time decay nhưng đổi lại nhận tail risk.

## 21. Vega

Vega đo độ nhạy với implied volatility.

Một trader đúng direction vẫn có thể lỗ nếu IV giảm đủ mạnh.

## 22. Rho

Rho đo sensitivity với lãi suất. Với nhiều option ngắn hạn, Rho nhỏ hơn Delta/Vega nhưng có thể quan trọng với expiry dài.

# Phần V — Implied volatility

## 23. IV không phải “mức biến động tương lai chắc chắn”

Implied volatility (IV) là mức volatility làm giá mô hình phù hợp với market option price.

Nó phản ánh cả:

- expected movement;
- risk premium;
- supply/demand option;
- hedging pressure.

## 24. Realized vs implied

**Realized volatility:** biến động thực tế đã xảy ra.

**Implied volatility:** volatility được phản ánh trong giá option.

Một option strategy thường phụ thuộc khoảng cách giữa hai khái niệm này.

## 25. IV crush

Trước event, IV có thể cao vì uncertainty. Sau release, uncertainty giảm làm IV rơi mạnh.

Do đó mua option trước event cần đúng không chỉ direction mà cả magnitude và volatility behavior.

# Phần VI — Các cấu trúc option cơ bản

## 26. Protective put

Long underlying + long put giúp giới hạn downside dưới strike theo payoff lý thuyết.

Chi phí là premium lặp lại.

## 27. Covered call

Long underlying + short call tạo premium nhưng giới hạn một phần upside.

Không phải “income miễn phí”; trader đang bán convexity.

## 28. Vertical spread

Call spread hoặc put spread giới hạn cả cost lẫn payoff.

Nó hữu ích khi muốn exposure có giới hạn rõ hơn so naked option.

## 29. Collar

Long underlying + long put + short call có thể giảm chi phí hedge nhưng đổi lại giới hạn upside.

## 30. Straddle và strangle

Các cấu trúc này tập trung vào magnitude/volatility hơn direction thuần.

P/L phụ thuộc move thực tế so implied move và time decay.

# Phần VII — Rủi ro bán option

## 31. Short option không phải “thu premium đều đặn” đơn giản

Strategy short-vol có thể thắng nhiều lần nhỏ rồi thua rất lớn trong tail event.

```text
High Win Rate
≠ Low Risk
```

## 32. Naked call

Short naked call có downside lý thuyết rất lớn khi underlying tăng mạnh.

## 33. Short put

Short put có exposure gần với cam kết mua underlying ở strike trong downside state.

Cần tính margin và gap risk.

# Phần VIII — Exercise và assignment

## 34. American vs European style

American-style option có thể exercise trước expiry. European-style chỉ exercise tại expiry theo rule.

Tên style không liên quan geography.

## 35. Assignment

Short option có thể bị assignment theo rule của contract.

Trader phải hiểu tác động lên underlying position, cash và margin.

## 36. Pin risk

Gần expiry, giá underlying quanh strike có thể làm position sau expiry không chắc chắn.

Đây là risk vận hành chứ không chỉ risk direction.

# Phần IX — Swaps

## 37. Interest-rate swap

Một rate swap điển hình đổi fixed payment lấy floating payment.

Nó cho phép thay đổi rate exposure mà không cần mua/bán toàn bộ bond portfolio.

## 38. OIS

Overnight Index Swap (OIS) dùng overnight reference rate và thường được dùng để đọc expected policy path.

## 39. Cross-currency swap

Cross-currency swap đổi cash flows giữa hai đồng tiền và có thể gồm principal exchange.

Nó liên quan funding cost và cross-currency basis.

## 40. Total Return Swap

TRS chuyển total economic return của một asset/index giữa hai bên mà không cần chuyển ownership trực tiếp.

Điều này tạo counterparty và collateral risk.

# Phần X — Credit derivatives

## 41. CDS

Credit Default Swap (CDS) chuyển credit risk theo hợp đồng.

Buyer trả premium; seller bồi thường theo credit event đã định nghĩa.

CDS spread không phải pure default probability vì còn chứa recovery assumption, liquidity và risk premium.

## 42. Credit indices

CDX/iTraxx hoặc index tương tự gom nhiều tên tín dụng để giao dịch credit exposure rộng hơn.

# Phần XI — Volatility derivatives

## 43. Variance swap

Variance swap tạo exposure trực tiếp hơn với realized variance so option vanilla.

Đây là sản phẩm phức tạp và thường phù hợp với chuyên nghiệp hơn retail.

Điểm học quan trọng là volatility cũng có thể là một “underlying economic exposure”.

# Phần XII — CFD

## 44. CFD là gì?

Contract for Difference là hợp đồng song phương với broker dựa trên thay đổi giá underlying.

Trader thường không sở hữu underlying.

## 45. Financing cost

Position CFD giữ qua đêm có thể chịu financing charge.

Chi phí này có thể làm strategy dài hạn kém hiệu quả dù direction đúng.

## 46. Broker counterparty

Cần hiểu:

- legal entity;
- regulation;
- client-money rule;
- execution model;
- stop-out;
- negative-balance protection nếu có.

## 47. CFD và exchange futures không giống nhau

Futures có contract chuẩn và central clearing. CFD thường bilateral với broker.

Hai sản phẩm cùng track gold nhưng legal risk và cost structure khác nhau.

# Phần XIII — Collateral và counterparty risk

## 48. Collateral

Derivative exposure có thể yêu cầu cash hoặc securities làm collateral.

Collateral requirement tăng trong stress có thể gây forced selling ở asset khác.

## 49. Netting

Legal netting cho phép bù exposure giữa nhiều giao dịch cùng counterparty theo điều kiện hợp đồng.

Nó có thể giảm gross exposure nhưng phụ thuộc enforceability.

## 50. Wrong-way risk

**Wrong-way risk** xảy ra khi counterparty yếu đi đúng lúc exposure với họ tăng.

Ví dụ hedge một credit risk bằng counterparty có sức khỏe phụ thuộc cùng risk đó.

# Phần XIV — Hedge ratio

## 51. Hedge phải khớp risk

```text
Rate Risk
→ DV01 / Rate Futures / Swaps

Equity Beta
→ Index Futures

FX Risk
→ Forward / Futures

Tail Risk
→ Options
```

Sai instrument tạo basis risk.

## 52. Hedge ratio không chỉ theo notional

Hai bond cùng notional nhưng duration khác nhau có rate risk khác nhau.

Hedge nên dựa sensitivity phù hợp như DV01, beta, Delta hoặc FX exposure.

# Phần XV — Expiry và roll management

## 53. Calendar

Derivative trader phải theo dõi:

- last trading day;
- first notice day nếu có;
- settlement date;
- option expiry;
- roll liquidity.

## 54. Liquidity migration

Volume thường chuyển từ front contract sang next contract trước expiry.

Giữ contract cũ quá lâu có thể làm spread/slippage tăng.

# Phần XVI — Rủi ro tổng hợp

## 55. Không nhìn từng position riêng

Một portfolio có thể có:

```text
Long Call
Short Put
Futures
CFD
```

nhưng tổng exposure thật phải tổng hợp theo:

- Delta;
- Gamma;
- Vega;
- DV01;
- FX;
- notional;
- margin.

## 56. Margin stress

Stress test phải hỏi cả P/L và collateral.

Một portfolio có theoretical hedge tốt vẫn có thể chết nếu margin call đến trước khi hedge payout được thực hiện.

## 57. Liquidity stress

Spread, depth và margin requirement thường cùng xấu trong crisis.

Position sizing trước crisis quan trọng hơn cố thoát hoàn hảo khi crisis đã bắt đầu.

# Phần XVII — Checklist trước khi giao dịch phái sinh

## 58. Contract checklist

```text
Underlying?
Multiplier?
Tick Value?
Expiry?
Settlement?
Margin?
Financing?
Counterparty?
Liquidity?
Maximum Plausible Loss?
```

## 59. Portfolio checklist

```text
Notional?
Delta?
Gamma?
Vega?
DV01?
FX?
Margin under stress?
Correlation with other positions?
```

## Kết luận

Phái sinh không nguy hiểm chỉ vì “phức tạp”; rủi ro xuất hiện khi trader không hiểu **quyền và nghĩa vụ hợp đồng, notional, sensitivity, collateral và liquidity**.

Một quy trình tốt luôn đi theo:

```text
Contract
→ Payoff
→ Sensitivity
→ Margin / Collateral
→ Liquidity
→ Counterparty
→ Portfolio Interaction
```

trước khi đi tới dự đoán direction.
