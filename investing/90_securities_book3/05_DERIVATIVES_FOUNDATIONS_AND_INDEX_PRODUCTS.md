# 5. Nền tảng phái sinh và sản phẩm theo chỉ số

Sách 3 chuyển từ “tài sản tạo ra dòng tiền” sang “hợp đồng định hình exposure”. **Phái sinh (derivatives / 파생상품)** không tự tạo lợi nhuận; nó cho phép chuyển thời điểm giao giá, quyền lựa chọn, hoặc rủi ro giữa các bên. Vì vậy phải đọc đồng thời payoff, giá trị danh nghĩa, margin, daily settlement, liquidity và counterparty.

## 1. Vì sao phái sinh tồn tại?

Thị trường có thể tăng, giảm hoặc biến động mạnh; doanh nghiệp còn chịu FX, interest rate, commodity và credit risk. Phái sinh đáp ứng bốn nhu cầu nguồn nêu: đặt cược/hedge theo hướng giảm; mua quyền hưởng lợi khi đúng nhưng giới hạn lỗ; tạo exposure với vốn ban đầu nhỏ hơn; và tiếp cận tài sản khó nắm giữ trực tiếp như dầu, volatility hay credit.

Ba kiểu nhìn là đủ để bắt đầu:

- **Hợp đồng tương lai/forward (futures·forward / 선물·선도)** khóa giao dịch tương lai. Futures chuẩn hóa và niêm yết trên exchange; forward tùy biến OTC, còn FX forward thường gọi là 선물환.
- **Quyền chọn (option / 옵션)** là quyền, không phải nghĩa vụ. Call cho quyền mua, put cho quyền bán; buyer trả premium, seller nhận premium và gánh nghĩa vụ nếu bị exercise.
- **Hoán đổi (swap / 스왑)** trao đổi các dòng tiền định kỳ (ví dụ fixed rate đổi floating rate), tạo exposure mà không cần mua toàn bộ tài sản.

Phải giữ đúng dấu vị thế trước khi đọc bất kỳ biểu đồ nào. Long futures có lãi khi giá tài sản cơ sở tăng, short futures có lãi khi giá giảm; hai bên có P&L đối nghịch trước phí và sai lệch basis. Long option trả premium để mua quyền một chiều, còn short option nhận premium nhưng đổi lại nhận nghĩa vụ và rủi ro đuôi. Vì vậy “vốn bỏ ra ít” không phải là “rủi ro nhỏ”: với futures, exposure chạy trên notional; với option bán, khoản lỗ có thể tăng nhanh khi underlying đi qua strike.

**Phái sinh niêm yết (exchange-traded derivatives / 장내파생상품)** có chuẩn hóa, clearing và margin; **Phái sinh OTC (over-the-counter derivatives / 장외파생상품)** phù hợp nhu cầu riêng nhưng đòi hỏi đánh giá counterparty, collateral và close-out. “Vốn ký quỹ 10 triệu nhưng exposure 100 triệu” không có nghĩa rủi ro chỉ là 10 triệu: lãi/lỗ chạy trên notional 100 triệu, và daily mark-to-market có thể buộc nộp thêm tiền.

**Đánh dấu theo thị trường hằng ngày (daily mark-to-market / 일일정산)** biến lãi/lỗ chưa thực hiện thành dòng tiền hàng ngày. Nếu equity trong tài khoản xuống dưới maintenance margin, clearing member có thể phát hành margin call; người nắm vị thế phải nộp variation margin hoặc giảm/đóng vị thế. Forced liquidation trong lúc thị trường biến động có thể khóa lỗ ở mức bất lợi. Đây là khác biệt thực hành giữa một payoff cuối kỳ “đúng” và một hedge có thể sống sót qua đường đi của giá.

## 2. Index futures: beta, alpha, hedge và basis

KOSPI200 index futures là ví dụ nguồn dùng xuyên suốt. Nhà đầu tư có thể:

1. **Đầu cơ (speculation / 투기거래)** theo hướng index tăng/giảm.
2. **Beta invest** để nhận market-average return thay vì chọn cổ phiếu riêng.
3. **Alpha/relative-value** mua tài sản kỳ vọng outperform và bán index hoặc tài sản yếu hơn; lợi nhuận là chênh lệch hai return, không phụ thuộc hoàn toàn hướng thị trường.
4. **Phòng hộ (hedge / 헤지거래)** market exposure của danh mục cổ phiếu.
5. **Tái tạo/chênh lệch giá (replication/arbitrage / 복제·차익거래)** index portfolio và futures; nếu nhiều mã được mua bán đồng thời, đó là **program trading (프로그램매매)**.

**Basis (베이시스)** là futures price trừ spot price. Trong ví dụ đơn giản của nguồn, basis dương thường được gọi là contango và basis âm là backwardation; nói chính xác hơn, contango/backwardation mô tả hình dạng đường cong futures theo các kỳ hạn, còn basis còn chứa tác động carry, dividend, storage và convenience yield. Khi đáo hạn, futures hội tụ về spot nên basis về 0. Giá lý thuyết đơn giản theo cost of carry:

\[
F_0=S_0[1+(r-q)T],
\]

với (F_0,S_0) cùng đơn vị index/price, (r) là funding rate năm, (q) là dividend yield năm và (T) là phần năm còn lại (nguồn minh họa 300 điểm, r 3%, q 2%, 6 tháng ⇒ khoảng 301,5). Đây là mô hình carry đơn giản của source; nó giả định compounding/quy ước ngày đã đồng nhất và dividend yield có thể dùng như rate. Với dividend rời rạc, funding curve, borrow constraint hoặc hợp đồng khác convention, công thức phải đổi. Futures market price cao hơn lý thuyết là overpricing, thấp hơn là underpricing. Basis risk tồn tại nếu hedge kết thúc trước expiry hoặc basis biến động khác kỳ vọng.

### Worked check: giá đúng chưa chắc hedge đúng

Giả sử spot index là 300, funding rate 3%, dividend yield 2% và còn nửa năm; công thức đơn giản cho futures khoảng 301,5. Nếu hợp đồng thực tế ở 304, chênh lệch 2,5 điểm không tự động là arbitrage: phải trừ bid–ask, thuế, funding thực tế, dividend không chắc chắn, margin và khả năng mua/rút danh mục index. Với một hedge bán futures, lãi từ futures chỉ bù đúng phần giảm của danh mục nếu beta, thời hạn và basis khớp; beta khác 1 hoặc basis đổi sẽ để lại residual risk.

Tick value = tick size × contract multiplier. Đây là cách chuyển một bước giá nhỏ thành won lãi/lỗ; không được nhìn mỗi phần trăm mà quên multiplier. Margin làm vốn ban đầu nhỏ, nhưng daily settlement làm dòng tiền quản trị khó hơn và có thể gây forced liquidation.

Delta hedge của dealer ELS thường bán futures khi index tăng và mua khi index giảm để bù thay đổi delta của liability. Vì vậy flow futures lớn không tự động là “nhà đầu tư đang bullish”; phải tách directional flow khỏi arbitrage/program hedge.

### Worked check: đọc flow theo synthetic exposure

Giả sử một nhà đầu tư mua 2.000 tỷ cổ phiếu và mua 3.000 tỷ index futures. Nếu chỉ nhìn hai dòng này, ta có thể kết luận họ bullish 5.000 tỷ. Nhưng nếu cùng lúc họ bán synthetic futures trị giá 7.000 tỷ (ví dụ short call và long put cùng strike/maturity), directional exposure ròng là \(2.000+3.000-7.000=-2.000\) tỷ: thiên về short thị trường. Phần còn lại có thể là hedge, arbitrage hoặc delta exposure thay đổi theo strike. Bản tin giao dịch phải được quy đổi về delta/notional ròng trước khi suy ra market view.

### Calendar spread: giao dịch chênh lệch kỳ hạn

Không phải mọi vị thế futures đều là cược vào hướng của index. Nếu futures gần kỳ hạn ở 300 và futures xa kỳ hạn ở 304, **spread mua** có thể là short near + long far; nhà giao dịch kỳ vọng chênh lệch xa–gần tăng. Nếu spread tăng từ 4 lên 7 điểm, P&L trước multiplier và phí là +3 điểm dù cả hai hợp đồng cùng tăng hoặc cùng giảm. Rủi ro nằm ở việc hai maturity hội tụ khác nhau, thanh khoản không đều và roll/basis thay đổi; calendar spread thường giảm directional beta nhưng không phải arbitrage chắc chắn.

### Delta-neutral và put–call parity trong nguồn

Một short straddle gần ATM có thể bắt đầu delta gần 0: bán 10 call có delta +0,50 và 10 put có delta −0,50 cho tổng delta \((-10\times0,50)+(-10\times-0,50)=0\). Nhưng delta này chỉ đúng tại thời điểm lập vị thế; underlying đi xa strike làm gamma thay đổi, nên dealer phải mua/bán lại underlying. Delta-neutral vì vậy chuyển directional risk thành volatility, gamma, theta và transaction-cost risk.

Put–call parity cho một call và put châu Âu cùng underlying/strike/maturity là (C-P=S-K/(1+r)^T) trong quy ước không cổ tức. (C,P,S,K) là giá theo cùng currency, (r) là funding rate cho cùng horizon và (T) là thời gian đến đáo hạn; parity giả định có thể vay/cho vay và giao dịch các chân với điều kiện tương thích. Ví dụ nguồn dùng \(S=307\), \(K=307,5\), \(C=15\), lãi suất 2,5% và một năm: \(P\approx15-307+307,5/1,025=8\). Nếu giá thị trường lệch khỏi quan hệ sau khi tính dividend, borrow, funding và phí thực thi, đó là tín hiệu cần kiểm tra conversion/reversal—not automatically risk-free arbitrage.

## 3. Index options: quyền, premium và payoff

Call buyer có payoff tại expiry:

\[
\max(S_T-K,0)-\text{premium};
\]

put buyer:

\[
\max(K-S_T,0)-\text{premium}.
\]

Ở đây (S_T) là giá underlying tại đáo hạn, (K) là strike và premium là giá quyền chọn trả/nhận lúc mở vị thế; ba đại lượng phải cùng đơn vị tiền/điểm sau khi áp multiplier. Các công thức là **P&L tại expiry** của long option, chưa gồm fee, funding, tax, early exercise hay mark-to-market trước expiry.

Buyer mất premium tối đa; seller có lợi nhuận tối đa bằng premium nhưng lỗ có thể rất lớn tùy vị thế. Breakeven của long call là \(K+premium\), của long put là \(K-premium\). Đừng gọi “quyền bán ở K” là call: call là quyền mua, put là quyền bán.

Gọi một option là **ITM/ATM/OTM (내가격/등가격/외가격)** phải dựa trên strike và spot hiện tại: call ITM khi \(S>K\), put ITM khi \(S<K\); ATM khi gần bằng nhau, còn OTM là ngược lại. Premium gồm **intrinsic value** (giá trị thực hiện ngay) và **time value** (khả năng trở nên có giá trị trước đáo hạn). Time value thường giảm khi thời gian trôi qua, nhưng volatility tăng có thể làm premium tăng và bù một phần theta. Vì thế không được suy ra P&L từ intrinsic value tại một thời điểm mà bỏ qua implied volatility, spread và thời gian còn lại.

### Worked check: payoff không phải premium

Long call có strike 105 và premium 3. Nếu đáo hạn ở 120, payoff là 15 nhưng P&L ròng chỉ là 12; nếu đáo hạn ở 103, payoff bằng 0 và P&L là −3. Một short call nhìn thấy premium 3 như lợi nhuận tối đa, nhưng khi underlying ở 120, P&L trước chi phí là −12. Bài tính này buộc người học tách **payoff**, **premium** và **P&L**, ba đại lượng thường bị trộn trong quảng cáo sản phẩm.

### Worked check: delta hedge là một quá trình, không phải một con số

Giả sử dealer short 1.000 call, mỗi call có delta 0,50 và contract multiplier là 1. Dealer đang có delta khoảng −500, nên mua 500 đơn vị underlying hoặc exposure tương đương để delta tổng gần 0. Nếu underlying tăng, delta call có thể tăng lên 0,65; dealer lúc đó cần mua thêm khoảng 150 đơn vị. Nếu giá nhảy qua strike trước khi hedge kịp điều chỉnh, gamma làm P&L lệch khỏi mô hình delta tĩnh. Theta, vega, spread và gap risk tiếp tục tồn tại dù delta tại một thời điểm bằng 0.

**Biến động (volatility / 변동성)** là độ lệch chuẩn annualized của return; historical volatility lấy dữ liệu quá khứ, implied volatility là volatility mà giá option đang hàm ý. Vì implied volatility là dự báo/giá thị trường, hai người có thể nhìn cùng dữ liệu nhưng định giá khác. Option premium còn phụ thuộc spot, strike, time to expiry, rate, dividend và volatility.

Black–Scholes tổ chức các input đó thành một mô hình giá option, nhưng không phải máy đọc giá “đúng”: mô hình thường giả định volatility không đổi, giao dịch liên tục, thanh khoản đủ, không có transaction cost và payoff kiểu châu Âu. Option thực tế có volatility smile/skew, early exercise, discrete dividend, jump và bid–ask; vì vậy dealer thường dùng volatility surface và mô hình điều chỉnh. **Implied volatility** là giá trị \(\sigma\) giải ngược từ premium thị trường trong một mô hình, không phải lời tiên tri độc lập về volatility tương lai.

Mô phỏng lịch sử cũng không tự động biến thành bằng chứng. Backtest có thể giả định khớp đúng mid-price, bỏ qua 1 tick spread, margin, ngoại tệ thanh toán hoặc chọn kịch bản tốt nhất trong nhiều lần thử. Nguồn cảnh báo rằng option giá thấp có thể có tick cost rất lớn theo tỷ lệ phần trăm; vị thế càng nhiều chân như butterfly càng dễ mất thanh khoản khi strike chuyển vào vùng ITM. Vì vậy trước khi tin simulation, phải chạy stress về spread, slippage, turnover và khả năng đóng từng chân.

Ví dụ nguồn: option giá 0,20 với tick 0,01 có chi phí một tick bằng 5% giá option. Nếu một chiến lược crossing spread 20 lần, riêng tick cost cộng dồn đã tương đương khoảng 0,20 premium, chưa tính commission và funding. Đây là lý do một backtest có gross return 5–10%/năm có thể biến thành net loss khi turnover cao. Khi OTM option trở thành ITM, thanh khoản và spread có thể đổi; với butterfly hoặc spread ba chân, chỉ cần một chân không đóng được là payoff lý thuyết không còn là P&L thực tế.

Với option quốc tế, margin và settlement có thể tính bằng ngoại tệ. Khi option lãi, collateral cần giữ và quy mô exposure FX cũng thay đổi; một vị thế delta-neutral với underlying vẫn có thể tạo lãi/lỗ do đồng tiền thanh toán. Vì vậy phải tách **underlying delta** khỏi **currency delta**, rồi kiểm tra thêm funding, conversion spread và khả năng rút collateral. Hedge option ở nước ngoài không hoàn tất nếu chỉ hedge giá tài sản mà bỏ qua đồng tiền của margin.

Các độ nhạy (Greeks) trong câu hỏi nguồn phải đọc như derivative của giá option, không phải tên chiến lược: **delta (델타)** là thay đổi option price khi underlying đổi (call khoảng 0→1, put khoảng −1→0); **gamma (감마)** là tốc độ delta đổi khi underlying đổi, nên lớn gần ATM có thể làm hedge phải tái cân bằng nhanh; **theta (세타)** là thay đổi theo thời gian còn lại (thường làm long option mất giá); **vega (베가)** là nhạy với implied volatility (call và put thường cùng dấu); **rho (로)** là nhạy với interest rate. Vì các đại lượng này thay đổi theo spot và thời gian, hedge delta hôm nay không đảm bảo delta hedge ngày mai.

Các cấu trúc nguồn minh họa cách ghép quyền:

- long call/put để giữ upside hoặc downside với loss giới hạn;
- **bull/bear spread (강세/약세 스프레드)** để giới hạn cả maximum gain và maximum loss;
- **straddle (스트래들)** mua call + put cùng strike để đặt cược biến động lớn, với hai breakeven \(K\pm\) tổng premium;
- **butterfly (버터플라이)** dùng ba strike, đổi vùng payoff để có lợi nhuận giới hạn;
- covered call/put-selling nhận premium nhưng nhận rủi ro tail khi thị trường đi xa.

Hai sản phẩm hóa chiến lược cần đọc theo payoff, không theo nhãn “income”. **Covered call (커버드콜)** giữ cổ phiếu và bán call: premium tạo một lớp đệm nhỏ, nhưng upside bị giới hạn ở strike và người giữ cổ phiếu vẫn chịu phần lớn downside. **Short strangle (매도 스트랭글)** bán call OTM và put OTM để thu cả hai khoản time value; nếu underlying nằm trong vùng, premium giữ lại có thể ổn định, nhưng một cú tăng vượt call hoặc giảm dưới put tạo tail loss và margin call. Khi volatility tăng, chính lúc premium hấp dẫn nhất cũng thường là lúc rủi ro gap và chi phí đóng vị thế lớn nhất.

Ví dụ short strangle bán call strike 110 nhận 2 và put strike 90 nhận 2. Nếu expiry ở 100, P&L là +4 trước phí; ở 125, call lỗ 15 nhưng premium chỉ bù 4, P&L −11; ở 75, put lỗ 15 và P&L cũng −11. Đây là cấu trúc có vùng lãi hữu hạn và vùng lỗ mở rộng, không phải “lãi hai chiều”.

Put–call parity là cầu nối giữa option và vị thế tổng hợp: long stock + long put tạo payoff như long call (portfolio insurance); long stock + short call là covered call, có payoff tương đương short put trong điều kiện parity và cùng strike/maturity. Conversion/reversal và index arbitrage khai thác chênh giá giữa spot, futures và option; sau phí, funding, dividend và borrow cost, “arbitrage” vẫn cần kiểm tra khả năng thực thi.

Luôn vẽ payoff tại expiry trước, rồi mới thêm thời gian, volatility, margin và early exercise. Payoff tĩnh không phải P&L đầy đủ trong thời gian sống của option.

## 4. Source-question test và ranh giới

Người học phải tính basis, futures theoretical price, tick value, payoff call/put, breakeven straddle và nhận diện hedge direction. Câu hỏi về “futures cần ít tiền nên ít rủi ro” phải trả lời sai: notional và margin call mới quyết định exposure. Câu hỏi về “option buyer luôn thắng vì có quyền” cũng sai vì premium là chi phí trả trước và thời gian có thể làm option mất giá.

Phần tiếp theo đổi underlying: interest rate, FX, credit và commodities. Giữ invariant: trước khi chọn contract, hãy viết exposure hiện tại, biến động nào gây lỗ, và payoff nào có dấu ngược lại.

Phần canonical về contract mechanics, execution và risk controls nằm ở [Derivatives](../05_trading_derivatives/01_DERIVATIVES_FUTURES_OPTIONS_CFD.md); Sách 3 giữ thêm các ví dụ KOSPI200, basis và delta hedge để người mới nối lý thuyết với thị trường Hàn Quốc.
