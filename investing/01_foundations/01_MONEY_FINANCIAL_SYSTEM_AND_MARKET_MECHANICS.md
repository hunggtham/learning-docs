# Tiền, hệ thống tài chính và market mechanics

> Mục tiêu của chapter này là xây nền cho toàn bộ thư viện đầu tư. Sau khi đọc xong, bạn không chỉ biết stock, bond hay ETF là gì, mà phải hiểu tiền đi qua hệ thống nào, quyền sở hữu và nghĩa vụ được ghi nhận ở đâu, order được khớp thế nào, chi phí ẩn xuất hiện ở đâu và vì sao market price có thể tách khỏi intrinsic value trong ngắn hạn.

## 1. Bắt đầu từ tiền thay vì bắt đầu từ cổ phiếu

Tiền có ba chức năng cơ bản: phương tiện trao đổi (*medium of exchange*), đơn vị tính toán (*unit of account*) và công cụ lưu trữ sức mua (*store of value*). Chức năng thứ ba không hoàn hảo vì inflation làm sức mua thay đổi theo thời gian. Nếu tài sản tiền mặt tăng danh nghĩa 3% nhưng mức giá chung tăng 5%, nominal wealth tăng nhưng real purchasing power giảm.

Real return có thể tính chính xác bằng:

`Real return = (1 + nominal return) / (1 + inflation) - 1`

Vì vậy đầu tư không đơn giản là “kiếm nhiều tiền hơn”, mà là phân bổ purchasing power hiện tại để đạt purchasing power cao hơn hoặc phù hợp hơn trong tương lai.

Time value of money là nền tảng cho bond pricing, DCF, mortgage và hầu hết valuation. Một khoản tiền nhận hôm nay có giá trị khác cùng nominal amount nhận nhiều năm sau vì tiền hôm nay có thể được đầu tư và compounding. Nếu một dòng tiền tương lai là `CF_t` và discount rate là `r`, present value cơ bản là:

`PV = CF_t / (1 + r)^t`

Discount rate không phải một con số tùy ý. Nó phản ánh time value, inflation expectations và risk premium mà investor yêu cầu.

## 2. Tiền ngân hàng, deposits và credit creation

Trong đời sống hiện đại, phần lớn “tiền” household sử dụng không phải banknotes mà là bank deposits. Khi bank cấp loan, nó thường đồng thời tạo một asset là khoản cho vay và một liability là deposit của khách hàng. Điều này giúp hiểu vì sao credit expansion có thể làm spending power tăng trước khi physical cash thay đổi tương ứng.

Central-bank reserves là một lớp khác với household deposits. Reserves chủ yếu phục vụ settlement giữa banks và tương tác với central bank; retail investor không giữ reserves trực tiếp. Vì vậy câu “central bank in tiền” thường quá đơn giản nếu không phân biệt banknotes, reserves, deposits, lending và asset purchases.

Đối với investor, điều quan trọng không phải thuộc accounting của hệ thống tiền tệ ngay lập tức, mà hiểu rằng money, credit và collateral liên kết với nhau. Khi banks sẵn sàng lend, collateral values cao và credit spreads thấp, financial conditions dễ hơn. Khi lenders thắt standards, collateral giảm và borrowers phải deleverage, cùng nominal policy rate có thể tạo environment tài chính khắt khe hơn nhiều.

## 3. Hệ thống tài chính nối người có vốn với người cần vốn

Households có thể tiết kiệm, companies cần vốn cho factory, R&D hoặc working capital, còn governments cần tài trợ expenditure. Financial system chuyển capital giữa các chủ thể thông qua banks, bond markets, equity markets, funds và derivatives.

Banking là *intermediation*: bank nhận funding và tạo loans. Capital markets cho phép issuer huy động trực tiếp hơn qua equity hoặc debt. Equity investor trở thành residual owner; bond holder là creditor với contractual claim. Preferred shares, subordinated debt và convertible securities nằm ở những vị trí khác nhau trong capital structure.

Nếu company phá sản, claims không ngang nhau. Secured creditors thường đứng trước unsecured creditors; subordinated debt đứng sau senior debt; common equity là residual claim và thường chịu loss đầu tiên. Vì vậy hai securities cùng issuer có thể có risk hoàn toàn khác nhau.

Return cũng không xuất hiện từ hư không. Equity return dài hạn cuối cùng phải liên quan tới cash generation, reinvestment và valuation. Bond return đến từ coupon, principal repayment và price change. Gold hay commodity không tạo contractual cash flow, nên return phụ thuộc scarcity, inventories, real rates, monetary regime và supply-demand.

## 4. Primary market: khi capital thực sự được huy động

Primary market là nơi security mới được phát hành. IPO đưa shares mới ra công chúng; seasoned offering và rights offering tăng equity sau IPO; bond issuance tạo debt mới. Trong primary transaction, issuer nhận capital theo cấu trúc giao dịch.

Rights offering đặc biệt quan trọng vì existing shareholders có thể được quyền mua shares mới theo tỷ lệ. Nếu không tham gia, ownership percentage có thể bị dilution. Convertible bonds hoặc warrants cũng có thể tạo future dilution dù share count hiện tại chưa thay đổi.

Corporate actions khác nhau có economic meaning khác nhau. Stock split thay số shares và price per share nhưng không tự tạo enterprise value. Buyback giảm share count nếu shares thực sự được retired hoặc held as treasury stock, nhưng chỉ tạo value khi mua lại với economics hợp lý và không làm balance sheet yếu đi. Dividend chuyển cash từ company sang shareholders; ex-dividend price adjustment không phải “free money”.

## 5. Secondary market và vì sao nó vẫn quan trọng với doanh nghiệp

Secondary market là nơi investors giao dịch securities đã phát hành với nhau. Khi bạn mua Samsung Electronics, một KOSPI ETF hay một cổ phiếu HOSE trong phiên bình thường, phần lớn trường hợp tiền đi tới người bán chứ không trực tiếp tới issuer.

Tuy vậy secondary market ảnh hưởng cost of capital. Một security liquid và có transparent price discovery thường yêu cầu liquidity premium thấp hơn. Higher valuation cũng có thể làm future equity financing ít dilutive hơn. Bond spread thấp làm refinancing rẻ hơn. Vì vậy secondary-market conditions có thể quay lại ảnh hưởng real corporate decisions.

## 6. Exchange-traded và OTC khác nhau ở đâu?

Exchange cung cấp standardized rules, matching, surveillance và thường có centralized clearing. Listed stocks và standardized futures là ví dụ.

Over-the-counter (*OTC*) market là nơi contract được giao dịch trực tiếp hoặc qua dealers thay vì một central limit order book duy nhất. FX forwards, swaps và nhiều bonds có thể giao dịch OTC. CFD retail thường là bilateral claim đối với broker/dealer chứ không phải ownership của underlying security.

Điều này thay đổi risk. Với exchange-traded stock, investor quan tâm market, custody và settlement. Với OTC derivative, legal entity, collateral terms, counterparty quality và close-out rules có thể quan trọng ngang market view.

## 7. Exchange, broker, clearing house, custodian và depository

Broker là gateway của investor nhưng không phải toàn bộ market infrastructure. Một order có thể đi qua broker risk checks và routing trước khi tới venue. Sau execution còn có clearing và settlement.

Central Counterparty (*CCP*) có thể đứng giữa buyer và seller đối với cleared products. Thay vì A trực tiếp phụ thuộc B, cả hai có obligations với clearing house. CCP quản lý risk qua margin, default fund và default-management procedures. Điều này giảm bilateral counterparty complexity nhưng không khiến systemic risk bằng zero.

Custodian giữ securities hoặc records tài sản theo legal structure. Central Securities Depository (*CSD*) hỗ trợ book-entry ownership và settlement. Segregation of client assets là khái niệm quan trọng: tài sản khách hàng cần được xử lý khác với tài sản của broker theo rules áp dụng. Investor nên hiểu mình đang mở account với legal entity nào, assets đứng tên/được custody ra sao và cơ chế bảo vệ khi intermediary gặp vấn đề.

## 8. Từ order tới fill: bid, ask và spread

Bid là mức giá mua tốt nhất hiện tại; ask là giá bán tốt nhất. Spread là khoảng giữa hai mức. Nếu bid 99 và ask 100, một market buyer có thể phải trả gần 100 trong khi market seller nhận gần 99. Spread là cost của immediacy.

Spread không cố định. Nó thường rộng hơn khi liquidity thấp, volatility cao, news uncertainty lớn hoặc market maker inventory risk tăng. Vì vậy một strategy có vẻ profitable trên close prices có thể mất edge sau spread và slippage.

Order book chứa resting limit orders. *Depth* cho biết quantity tại nhiều price levels. Một security có daily volume cao nhưng depth thấp ở thời điểm bạn trade vẫn có thể tạo market impact lớn.

## 9. Market, limit, stop và stop-limit orders

Market order ưu tiên khả năng được fill, không bảo đảm exact price. Trong liquid market bình thường, slippage có thể nhỏ; khi gap hoặc panic, fill có thể rất xa last price.

Limit order đặt price constraint. Buyer không muốn trả cao hơn limit; seller không muốn bán thấp hơn limit. Đổi lại, order có thể không fill hoặc chỉ fill một phần.

Stop order trở thành executable order khi trigger được chạm theo rules của venue/broker. Nó hữu ích để automate risk control nhưng không bảo đảm loss giới hạn chính xác tại stop price. Stop-limit kiểm soát price tốt hơn nhưng có risk không thoát được nếu market chạy qua limit.

Time-in-force như DAY, GTC, IOC hay FOK mô tả thời gian và điều kiện order tồn tại. Naming/rules có thể khác giữa markets và brokers, nên investor phải đọc specification thực tế thay vì suy đoán từ tên.

## 10. Matching, price-time priority và auctions

Nhiều electronic exchanges dùng logic gần với price-time priority: price tốt hơn được ưu tiên; trong cùng price, order vào trước thường được ưu tiên trước. Điều này giải thích vì sao đặt limit price giống best bid không có nghĩa bạn sẽ fill ngay: trước bạn có thể có một queue lớn.

Markets cũng dùng auctions cho opening, closing hoặc volatility interruptions. Auction gom orders rồi xác định clearing price tối đa hóa executable volume theo rules. Closing auction đặc biệt quan trọng với index funds vì benchmark thường dùng official close; index rebalance có thể tạo volume rất lớn vào cuối phiên.

## 11. Liquidity không chỉ là volume

Liquidity có nhiều dimensions: spread hẹp, depth lớn, khả năng trade size đáng kể mà không move price nhiều, và khả năng market hồi phục sau order imbalance. Daily turnover chỉ là một chỉ báo.

Slippage là khác biệt giữa expected và executed price. Market impact là phần price movement do chính order của bạn gây ra. Nếu position quá lớn so average traded value, exit risk có thể lớn hơn entry risk. Vì vậy position sizing phải gắn với liquidity chứ không chỉ conviction.

Một practical rule là luôn hỏi: nếu thesis sai trong một ngày xấu, mình có thể giảm position bằng cách nào? Nếu câu trả lời phụ thuộc “chắc sẽ có người mua”, liquidity risk chưa được quản lý.

## 12. Price discovery, information và flows

Market price là equilibrium tạm thời giữa participants có information, horizon, leverage và constraints khác nhau. Nó không phải phép đo trực tiếp intrinsic value.

Pension fund có thể bán vì rebalancing; ETF phải mua vì index inclusion; leveraged fund có thể liquidate vì margin; market maker hedge inventory; company buyback shares; retail investors chase momentum. Những flows này có thể move price dù fundamental cash-flow forecast chưa thay đổi.

Do đó price movement nên được phân rã thành ít nhất bốn câu hỏi: fundamentals có đổi không, discount rate có đổi không, positioning/flows có đổi không, và liquidity có đổi không. Đây là cách tránh suy luận “giá giảm nên business xấu” hoặc “giá tăng nên thesis đúng”.

## 13. ETF NAV, premium/discount và creation-redemption

ETF share giao dịch trên exchange nhưng fund đồng thời sở hữu hoặc replicate một basket. Net Asset Value (*NAV*) phản ánh value của assets trừ liabilities trên mỗi share theo methodology.

Authorized Participants (*APs*) có thể create hoặc redeem ETF shares bằng basket/cash theo rules. Cơ chế arbitrage này thường giúp market price bám NAV, nhưng không phải lúc nào cũng hoàn hảo. Khi underlying đóng cửa, illiquid hoặc stressed, ETF price có thể khác indicative NAV đáng kể.

Vì vậy premium không có nghĩa ETF “tốt hơn”, discount không tự động là bargain. Cần biết underlying đang price được không, NAV stale không, spread bao nhiêu và creation/redemption hoạt động bình thường không.

## 14. Settlement, clearing và failed settlement

Trade date là ngày execution; settlement là lúc cash và securities obligations được hoàn tất theo cycle của market/product. Chu kỳ có thể T+1, T+2 hoặc khác và có thể thay đổi theo regulation.

Investor không nên hard-code một cycle cho mọi market. Quan trọng hơn là hiểu unsettled cash, buying power và withdrawable cash không phải cùng một khái niệm.

Settlement fails, operational errors hoặc holiday mismatch có thể tạo risk trong cross-border portfolios. Đây là lý do operational knowledge quan trọng với investor dùng nhiều brokers/currencies.

## 15. Margin, collateral và leverage

Margin là collateral, không phải maximum loss. Futures trader có thể post một phần notional nhưng chịu P/L trên toàn exposure. Khi mark-to-market loss làm equity xuống dưới maintenance threshold, broker/clearing system có thể yêu cầu thêm collateral hoặc liquidate.

Trong leveraged account, path matters. Một position cuối cùng quay về entry price vẫn có thể bị forced liquidation giữa đường nếu drawdown vượt collateral capacity.

Leverage vì vậy phải được đánh giá qua notional exposure, stress loss và liquidity of collateral, không chỉ qua “margin required”.

## 16. Short selling và securities lending

Để short cash stock, trader thường phải borrow shares, bán chúng rồi sau này mua lại để return lender. Borrow fee, availability và recall risk là part of economics.

Short seller có asymmetric risk vì downside của long stock giới hạn ở zero nhưng short loss về lý thuyết có thể tăng khi price tăng. Short squeeze xảy ra khi rising price, recalls hoặc risk limits buộc shorts cover, tạo additional buying.

Regulation về short selling khác theo jurisdiction và có thể thay đổi. Framework vĩnh viễn là: locate/borrow có tồn tại không, borrow cost là bao nhiêu, collateral requirement thế nào và forced-cover conditions là gì.

## 17. Circuit breakers, price limits và market interruptions

Markets dùng circuit breakers, volatility interruptions hoặc daily price limits để quản lý disorderly trading. Những cơ chế này không loại bỏ risk; chúng thay đổi timing của price discovery.

Price limit có thể khiến investor không exit được dù stop level đã bị xuyên về economic value. Trading halt có thể giữ position qua news mới. Vì vậy “có stop-loss” không đồng nghĩa luôn có khả năng thực thi stop.

## 18. Operational và counterparty risk

Investor thường tập trung market direction nhưng có thể mất tiền vì wrong account, wrong contract, phishing, broker failure, withdrawal restriction hoặc misunderstanding of product terms.

Các controls nền tảng gồm 2FA, withdrawal whitelist nếu có, kiểm legal entity, đọc client-asset treatment, test withdrawal với amount nhỏ, lưu transaction records và tránh giữ excess collateral ở high-risk venues chỉ vì leverage cao.

## 19. Một execution checklist thực tế

Trước khi đặt order, hãy xác định security/contract chính xác, venue, currency, position size, average daily liquidity, spread, expected slippage, order type, maximum acceptable execution price và exit plan. Với derivatives, thêm multiplier, tick value, expiry, settlement method, margin và overnight financing.

Sau execution, kiểm fill price, fees, settlement status và actual exposure. Nếu trade lớn, so implementation price với decision price để học market-impact cost.

## 20. Mental model cuối cùng

Mỗi lần nhìn một sản phẩm tài chính, hãy tách nó thành năm layer:

`Economic claim → Legal/counterparty structure → Market/liquidity → Execution/settlement → Portfolio risk`

Nếu không giải thích được cả năm layer, bạn chưa thực sự hiểu sản phẩm dù biết ticker và chart. Market mechanics không phải kiến thức phụ của investing; nó là cơ chế biến thesis thành exposure thực tế.