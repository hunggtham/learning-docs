# Derivatives — Futures, Options, CFD và hedging

## 1. Derivative là hợp đồng, không phải lúc nào cũng là ownership

Derivative lấy value từ một underlying như stock index, bond, currency, gold hoặc oil. Điều này khác việc mua common stock và trở thành owner. Derivative exposure có thể rất lớn so với cash posted vì margin và leverage.

Trước mọi derivative trade, phải biết underlying, contract size, multiplier, tick size, settlement, expiry, margin và worst-case behavior. Nếu không đọc contract specification, bạn chưa thực sự biết mình đang trade gì.

## 2. Futures

Futures là standardized exchange-traded contract. Index futures không giao một rổ cổ phiếu vật lý theo cách retail investor tưởng tượng; P/L thường được cash-settled theo contract rules.

Notional value bằng futures price nhân multiplier. Margin chỉ là collateral. Vì vậy một account đặt 10 triệu margin có thể kiểm soát notional lớn hơn nhiều, tạo leverage.

Daily mark-to-market làm profits/losses được ghi nhận thường xuyên. Nếu equity dưới maintenance margin, trader có thể phải nạp thêm hoặc bị liquidate.

Basis là futures price trừ spot. Cost of carry, dividends, interest rates và supply-demand ảnh hưởng basis. Gần expiry, futures thường converge về spot theo cơ chế arbitrage.

## 3. Commodity futures và curve

Commodity futures có term structure. Contango nghĩa contracts xa cao hơn near/spot trong cách mô tả phổ biến. Backwardation là chiều ngược lại.

Funds phải roll contracts. Trong contango, bán near thấp và mua far cao có thể tạo negative roll yield. Vì vậy commodity futures ETF return có thể khác spot commodity đáng kể.

## 4. Options

Call cho buyer quyền mua underlying ở strike. Put cho quyền bán. Buyer trả premium và có max loss bằng premium nếu không có cấu trúc phức tạp khác. Seller nhận premium nhưng có obligation và tail risk.

Option price gồm intrinsic value và time value. Time to expiry và implied volatility rất quan trọng.

Delta đo sensitivity với underlying. Gamma đo delta thay đổi. Theta phản ánh time decay. Vega phản ánh sensitivity với implied volatility.

## 5. IV và event risk

Trước earnings hoặc macro event, implied volatility có thể tăng vì uncertainty. Sau event, uncertainty biến mất và IV có thể collapse.

Do đó long call có thể lỗ dù stock tăng nếu move nhỏ hơn implied và IV crush lớn. Direction đúng chưa đủ; option trader còn phải đúng về magnitude, timing và volatility.

## 6. Basic strategies theo mục tiêu

Long call dùng khi muốn defined downside và bullish convexity. Long put là bearish hoặc hedge. Covered call bán upside trên stock đang sở hữu để nhận premium nhưng giới hạn upside. Protective put mua downside insurance.

Vertical spreads giới hạn cả gain và loss, giảm premium so naked long option. Những structures này nên được hiểu bằng payoff diagram và max loss/max gain trước khi giao dịch.

## 7. Short options và tail risk

Short premium strategies thường có win rate cao vì thu theta, nhưng occasional loss có thể rất lớn. Đây là lý do chỉ nhìn win rate là nguy hiểm.

Naked short call có theoretical unlimited loss. Short put có downside lớn nếu underlying collapse. Margin requirement có thể tăng đúng lúc volatility spike, tạo forced liquidation.

## 8. CFD

CFD là bilateral contract với broker dựa trên price difference. Retail trader thường không sở hữu underlying. Broker structure, overnight financing, spread, stop-out và legal jurisdiction trở thành part of product risk.

CFD thuận tiện cho leverage và shorting nhưng cost có thể lớn nếu giữ dài. Nó không nên được dùng thay cash equity chỉ vì “mua được ít vốn hơn”.

## 9. Hedging

Hedge giảm một risk bằng position khác. Equity portfolio có thể hedge beta bằng index futures hoặc puts. Foreign assets có thể hedge FX bằng forwards/futures hoặc hedged funds.

Hedge không miễn phí. Futures hedge có basis risk. Options hedge trả premium. Currency hedge có carry cost. Over-hedge có thể tạo position ngược ngoài ý muốn.

## 10. Greeks như risk language

Professional options thinking không chỉ hỏi bullish/bearish. Một portfolio có delta gần zero nhưng short gamma và short vega vẫn có thể mất rất lớn khi market gap và volatility tăng.

Greeks là cách phân rã risk. Retail trader không cần advanced stochastic calculus để bắt đầu, nhưng phải hiểu position kiếm/mất tiền từ direction, time và volatility như thế nào.

## 11. Derivatives trong portfolio

Derivatives có ba vai trò chính: hedge, efficient exposure và speculation. Nếu dùng để hedge, size phải liên hệ portfolio exposure. Nếu dùng để speculation, risk budget phải nhỏ và defined.

Leverage là công cụ, không phải edge. Một derivative strategy chỉ hợp lý khi bạn hiểu payoff, margin path và scenario xấu nhất trước khi nhìn expected profit.