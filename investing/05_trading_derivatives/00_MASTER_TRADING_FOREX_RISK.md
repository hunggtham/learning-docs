# Bản đồ tổng quan Trading, Forex và quản trị rủi ro

> Tệp (file / 파일) này là bản đồ học tập cho toàn bộ `05_trading_derivatives/`. Mục tiêu không phải thay thế các chapter chuyên sâu, mà giúp người đọc hiểu trading là một hệ thống gồm **tín hiệu → quy mô vị thế → thực thi → chi phí → quản trị danh mục → rà soát (review / 검토)**.

> **Cách đọc dễ hơn:** đừng bắt đầu từ pattern. Hãy bắt đầu bằng một cặp tiền, tính một giao dịch bằng tiền thật, rồi mới thêm regime, backtest và vi cấu trúc. Lộ trình ví dụ số nằm ở [Bắt đầu từ đây — Cổ phiếu và Forex](../START_HERE_STOCKS_AND_FOREX.md).

## 0. Ví dụ đọc một giao dịch bằng tiền

Giả sử mua `10.000 EUR/USD` tại `1,1000` và đóng tại `1,1050`:

```text
Chênh lệch giá = 0,0050 USD/EUR
Lãi trước chi phí ≈ 0,0050 × 10.000 = 50 USD
```

Nếu spread là `1,2 pip` và giá trị gần đúng là `1 USD/pip`:

```text
Chi phí spread ≈ 1,2 USD
Lãi sau spread, trước slippage/financing ≈ 48,8 USD
```

Nếu stop cách điểm vào `30 pip`, lỗ danh nghĩa tại stop gần `30 USD` trước chi phí. Với margin yêu cầu `2%`, broker có thể khóa khoảng `220 USD` cho notional gần `11.000 USD`; **220 USD không phải mức lỗ tối đa**.

Thứ tự cần tính luôn là:

```text
Hướng cặp tiền → notional → giá trị pip → stop bằng tiền
→ spread/slippage/financing → margin → rủi ro danh mục
```

Giá trị pip thực tế thay đổi theo cặp tiền, quy mô, tỷ giá và đồng tiền tài khoản. Khi chưa kiểm tra contract specification của sản phẩm, chỉ nên xem các số trên là ví dụ học tập.

Trading không phải tập hợp các pattern vào lệnh. Một chiến lược chỉ có ý nghĩa khi lợi thế kỳ vọng còn tồn tại sau spread, slippage, financing, drawdown và lỗi vận hành.

## 1. Mô hình tư duy (mental model / 사고 모델) cốt lõi

Trước khi đi vào từng công cụ, hãy giữ một chuỗi vận hành duy nhất: giả thuyết tạo tín hiệu, tín hiệu dẫn tới rule vào/ra, rule quyết định size, execution tạo chi phí, rồi kết quả được review ở cấp danh mục. Chuỗi này là khung để đặt mọi phần sau vào đúng vị trí.

```text
Hypothesis
→ Signal
→ Entry / Exit Rule
→ Position Size
→ Execution
→ Cost
→ P/L Distribution
→ Portfolio Risk
→ Review
```

Nếu thiếu một mắt xích, hệ thống chưa hoàn chỉnh.

## 2. Chart chỉ là biểu diễn dữ liệu giá

Trước khi nói về setup, cần thống nhất chart đang cho ta biết điều gì và không cho ta biết điều gì. Phần này giải quyết câu hỏi: dữ liệu giá được nén thành những trường nào, và vì sao việc nhìn thấy một hình dạng chưa đủ để kết luận có lợi thế giao dịch?

Candlestick, bar hay line chart chỉ là cách hiển thị:

- open;
- high;
- low;
- close;
- volume nếu có.

Chart không tự tạo edge. Edge phải đến từ một quan hệ có khả năng lặp lại và có lý do kinh tế hoặc hành vi hợp lý.

Vì vậy, chart là đầu vào để đặt giả thuyết chứ không phải bằng chứng cuối cùng. Khi đã phân biệt được hai vai trò này, ta mới có thể chọn độ phân giải thời gian phù hợp ở phần tiếp theo.

## 3. Timeframe

Sau khi biết chart chỉ là dữ liệu, ta cần quyết định quan sát dữ liệu ở khoảng thời gian nào. Timeframe thay đổi lượng nhiễu, chi phí và tốc độ ra quyết định, nên đây là lựa chọn về thiết kế hệ thống chứ không phải sở thích nhìn biểu đồ.

Timeframe càng nhỏ:

- noise càng lớn;
- spread/slippage chiếm tỷ trọng cao hơn;
- thực thi (execution / 실행) quan trọng hơn;
- số lượng giao dịch nhiều hơn.

Không có timeframe “tốt nhất”; nó phải phù hợp chiến lược (strategy / 전략), chi phí (cost / 비용) và thời gian của trader.

Điểm chốt là timeframe phải phục vụ rule và ngân sách chi phí. Từ đây, ta có thể hỏi thị trường đang ở trạng thái nào để biết cùng một timeframe có nên được diễn giải như nhau hay không.

## 4. Trend, range và regime

Timeframe chỉ cho biết ta quan sát nhanh hay chậm; nó chưa cho biết môi trường thị trường. Vì vậy, phần này đưa thêm khái niệm regime để giải thích tại sao một setup có thể hoạt động ở giai đoạn này nhưng thất bại ở giai đoạn khác.

Một thị trường có thể ở:

```text
Trend
Range
High Volatility
Low Volatility
Event-Driven State
```

Một setup tốt trong trend có thể hoạt động kém trong phạm vi (range / 범위).

Mental model cần giữ là **setup luôn có điều kiện môi trường**. Sau khi nhận diện regime, ta chuyển sang market structure để mô tả dữ liệu cụ thể hơn thay vì gắn nhãn cảm tính.

## 5. Market structure

Market structure là cách biến diễn biến giá thành một chuỗi quan sát có thứ tự. Mục tiêu của phần này là trả lời: giá đang tạo các đỉnh–đáy và phản ứng quanh vùng thanh khoản như thế nào, trước khi ta gọi đó là breakout hay pullback.

Market structure thường mô tả chuỗi swing high, swing low và cách giá phản ứng quanh vùng có order flow lớn.

Các thuật ngữ như break of cấu trúc (structure / 구조) hoặc thay đổi (change / 변경) of character chỉ nên dùng như cách mô tả dữ liệu, không phải quy luật tất định.

Do đó, structure cung cấp ngôn ngữ để ghi rule và invalidation, chứ không bảo đảm kết quả. Bước kế tiếp là xem những vùng giá nào thường được dùng làm mốc quan sát hành vi đó.

## 6. Support và resistance

Khi đã có chuỗi swing và phản ứng giá, ta cần một cách khoanh vùng nơi cung–cầu từng thay đổi. Support và resistance giải quyết nhu cầu đó, nhưng phải được hiểu như vùng xác suất thay vì đường biên tuyệt đối.

Support/resistance là vùng giá nơi hành vi mua/bán từng thay đổi đáng kể.

Nên nghĩ theo vùng xác suất, không phải một đường chính xác tuyệt đối.

Vùng chỉ trở nên hữu ích khi gắn với điều kiện phản ứng và mức vô hiệu hóa. Từ nền đó, breakout sẽ được đọc như một giả thuyết vượt vùng cần kiểm chứng, không phải tín hiệu tự động.

## 7. Breakout

Breakout đặt câu hỏi liệu việc giá vượt vùng có tạo ra phân phối kết quả tốt hơn sau chi phí hay không. Vì vậy, ta phải đọc nó cùng false break, spread và slippage thay vì chỉ nhìn một cây nến vượt đỉnh.

Breakout chỉ có edge nếu sau chi phí, false break và slippage, outcome phân phối vẫn có expectancy dương.

Kết luận là “vượt vùng” mới chỉ là điều kiện quan sát; expectancy sau chi phí mới là tiêu chí quyết định. Nếu giá không tiếp diễn mà quay lại vùng, ta chuyển sang cách đọc pullback.

## 8. Pullback

Pullback là trường hợp ta không đuổi theo chuyển động đầu tiên mà chờ giá điều chỉnh để kiểm tra liệu trend còn được bảo vệ hay không. Phần này nối breakout với câu hỏi về điểm vào, invalidation và tỷ lệ rủi ro/lợi nhuận.

Pullback strategy thường đánh cược rằng trend chính còn tiếp tục sau điều chỉnh tạm thời.

Điểm quan trọng là định nghĩa trend, vô hiệu hóa (invalidation / 무효화) và rủi ro (risk / 위험)/reward rõ ràng.

Nếu không định nghĩa được ba điều này trước khi vào lệnh, “pullback” chỉ là tên gọi sau sự kiện. Khi trend không còn là giả định hợp lý, mean reversion là mô hình đối chiếu cần được kiểm tra.

## 9. Mean reversion

Mean reversion bắt đầu từ một giả định khác với pullback: thay vì tiếp diễn, giá có thể quay về một mốc tham chiếu sau khi lệch quá xa. Vì vậy, điều kiện quan trọng nhất là biết khi nào thị trường còn trong range và khi nào đã chuyển sang trend.

Mean reversion giả định giá có xu hướng quay về một mức tham chiếu sau khi đi quá xa.

Nó có thể thất bại nặng khi thị trường chuyển từ phạm vi (range / 범위) sang trend.

Ranh giới của mô hình nằm ở regime shift; mean reversion không được xem là quy luật tự nhiên của mọi thị trường. Để đánh giá khả năng quay về, ta cần quan sát chất lượng khớp lệnh và thanh khoản, bắt đầu từ volume và liquidity.

## 10. Volume và liquidity

Giá có thể trông “đẹp” trên chart nhưng vẫn khó giao dịch nếu spread rộng, sổ lệnh mỏng hoặc market impact lớn. Phần này giải thích vì sao volume chỉ là một tín hiệu ban đầu và cần được đặt cạnh nhiều thước đo thanh khoản khác.

Volume cao không luôn đồng nghĩa liquidity tốt. Cần nhìn thêm:

- spread;
- độ sâu (depth / 깊이);
- thị trường (market / 시장) impact;
- thời điểm trong ngày.

Khi hiểu thanh khoản theo nhiều lớp, ta mới ước lượng được chi phí và độ trượt trong các trạng thái khác nhau. Đây là tiền đề để đọc volatility, vì biến động quyết định cả khoảng stop lẫn quy mô vị thế.

## 11. Volatility

Volatility không chỉ là một con số mô tả giá rung lắc; nó thay đổi khoảng cách stop, expected move, yêu cầu margin và giá quyền chọn. Câu hỏi của phần này là: khi môi trường biến động đổi, hệ thống phải thay đổi quyết định nào?

Volatility quyết định:

- stop distance hợp lý;
- position kích thước (size / 크기);
- expected move;
- margin rủi ro (risk / 위험);
- option pricing.

Cùng một chiến lược (strategy / 전략) không nên dùng kích thước (size / 크기) giống nhau trong mọi volatility regime.

Vì vậy, volatility là cầu nối từ quan sát thị trường sang risk sizing. Các indicator ở phần sau chỉ nên được giữ lại khi chúng giúp đo hoặc diễn đạt rule này một cách kiểm chứng được.

## 12. Indicator

Indicator là phép biến đổi từ price hoặc volume, nên mục tiêu không phải sưu tầm thật nhiều công cụ mà là hiểu mỗi công cụ đang đo tín hiệu nào. Phần này giúp người mới phân biệt biến mô tả với rule tạo quyết định.

MA, RSI, MACD, ATR hay Bollinger Bands đều là biến đổi của price/volume.

Indicator hữu ích khi nó phục vụ quy tắc (rule / 규칙) rõ ràng, không phải vì thêm nhiều indicator làm hệ thống “chắc chắn” hơn.

Điểm chốt là một indicator chỉ có ý nghĩa trong giả thuyết và điều kiện cụ thể. Các thuật ngữ SMC/ICT tiếp theo cũng cần được xử lý theo nguyên tắc tương tự: chuyển ngôn ngữ mô tả thành rule có thể kiểm tra.

## 13. SMC / ICT

SMC/ICT thường cung cấp từ vựng để mô tả vùng thanh khoản và price action. Trước khi dùng, cần hỏi mỗi thuật ngữ có định nghĩa quan sát được, điều kiện kích hoạt và điểm vô hiệu hóa hay chưa.

Các khái niệm như liquidity sweep, order block, fair value gap có thể dùng như ngôn ngữ mô tả price action.

Nhưng phải chuyển chúng thành quy tắc (rule / 규칙) kiểm chứng được nếu muốn backtest.

Như vậy, tên gọi không tự tạo lợi thế; khả năng kiểm chứng mới quyết định giá trị. Khi rule đã rõ, multi-timeframe có thể được dùng để phân vai context và timing mà không biến thành câu chuyện hindsight.

## 14. Multi-timeframe

Multi-timeframe nối hai nhu cầu thường bị trộn lẫn: timeframe lớn để đặt bối cảnh và timeframe nhỏ để chọn thời điểm. Mục tiêu là phân vai rõ từng khung, không dùng nhiều khung để tìm một câu chuyện phù hợp sau khi giá đã chạy.

Timeframe lớn có thể cung cấp context; timeframe nhỏ dùng cho timing.

Tuy nhiên thêm quá nhiều timeframe dễ tạo hindsight narrative.

Điểm chốt của phần nền tảng là mọi cách đọc chart đều phải quay về rule, chi phí và điều kiện thị trường. Từ đây, ta chuyển sang Forex như một thị trường tương đối, nơi giá luôn là quan hệ giữa hai nền kinh tế.

## 15. Forex là thị trường tương đối

Sau khi xây xong ngôn ngữ chart và regime, ta áp dụng nó vào Forex. Khác với một tài sản đơn lẻ, một cặp tiền luôn biểu diễn quan hệ tương đối; vì vậy người học phải hỏi đồng thời bên nào mạnh lên, bên nào yếu đi và dòng vốn đang phản ứng với chênh lệch nào.

Một cặp tiền luôn so hai nền kinh tế.

```text
EUR/USD
= giá EUR theo USD
```

Phân tích cần nhìn relative rates, relative growth, rủi ro (risk / 위험) sentiment và luồng (flow / 흐름).

Điểm chốt là không thể phân tích EUR/USD chỉ bằng một biểu đồ EUR hoặc USD riêng lẻ. Khi đã hiểu đối tượng đang được so sánh, ta mới tính được đơn vị biến động và quy mô hợp đồng ở phần pip và lot.

## 16. Pip và lot

Pip và lot biến một thay đổi trên chart thành số tiền có thể lãi hoặc lỗ. Đây là bước nối giữa ngôn ngữ thị trường và kế toán giao dịch, nên phải xác định đúng quy ước của từng sản phẩm trước khi tính risk.

Pip là đơn vị biến động giá quy ước. Lot là quy mô hợp đồng.

Trước khi giao dịch phải biết:

```text
Contract Size
Pip Value
Quote Currency
Account Currency
```

Nếu chưa biết contract size, pip value và đồng tiền tài khoản, mọi phép tính position size phía sau đều có thể sai. Vì vậy, leverage được học sau phần này như một cơ chế khuếch đại notional, không phải điểm bắt đầu.

## 17. Leverage

Đòn bẩy giải thích vì sao một lượng vốn nhỏ có thể kiểm soát notional lớn. Phần này cần được đọc cùng pip value và stop distance để thấy leverage thay đổi yêu cầu vốn như thế nào nhưng không làm cho tín hiệu trở nên tốt hơn.

Đòn bẩy (leverage) cho phép kiểm soát notional lớn bằng capital nhỏ hơn.

Leverage không tạo edge. Nó chỉ phóng đại:

```text
P/L
Drawdown
Margin Risk
Risk of Ruin
```

Leverage vì thế là một bộ khuếch đại của phân phối kết quả: cùng một edge, đòn bẩy cao làm drawdown và nguy cơ cháy tài khoản lớn hơn. Phần margin tiếp theo tách yêu cầu collateral khỏi mức lỗ tối đa để tránh nhầm lẫn phổ biến.

## 18. Margin

Margin là số tài sản broker khóa để duy trì vị thế, không phải số tiền mà thị trường cho phép bạn mất. Hiểu ranh giới này giúp người mới không dùng “margin thấp” như lý do để tăng size.

Margin là collateral broker yêu cầu để giữ position.

```text
Required Margin
≈ Notional / Leverage
```

Margin không phải maximum mất mát (loss / 손실).

Khi margin chỉ là điều kiện duy trì position, ta cần theo dõi equity và free margin để biết vị thế còn chịu được biến động hay đã tiến gần stop-out.

## 19. Equity, free margin và margin level

Ba số đo này nối lãi/lỗ đang chạy với khả năng tiếp tục giữ position. Equity phản ánh giá trị hiện tại, free margin phản ánh phần collateral còn có thể dùng, còn margin level cho biết khoảng cách tương đối tới ngưỡng broker hành động.

```text
Equity = Balance + Floating P/L
```

```text
Margin Level
= Equity / Used Margin × 100%
```

Nếu equity giảm quá mức, broker có thể margin lời gọi (call / 호출) hoặc stop-out theo rules riêng.

Do broker có quy tắc riêng và có thể trượt giá khi thị trường căng thẳng, margin level không thay thế stop-loss hay stress test. Bước kế tiếp là đảo ngược phép tính: bắt đầu từ mức lỗ chấp nhận được để tìm position size.

## 20. Position sizing

Position sizing là nơi giả thuyết giao dịch gặp giới hạn vốn thật. Thay vì hỏi “broker cho phép bao nhiêu?”, ta hỏi “nếu invalidation xảy ra, tôi chấp nhận mất bao nhiêu và cần bao nhiêu đơn vị để đúng mức đó?”.

Quy mô vị thế phải bắt đầu từ mức lỗ chấp nhận được.

```text
Position Size
≈ Allowed Loss / Loss Per Unit at Invalidation
```

Không nên bắt đầu từ “broker cho leverage bao nhiêu”.

Kết quả của phần này là một quy mô được tính từ risk budget, stop và pip value. Khi size đã rõ, stop-loss mới có thể được đánh giá như một lệnh thực thi với rủi ro trượt giá riêng.

## 21. Stop-loss

Stop-loss là điều kiện gửi lệnh thoát khi luận điểm bị vô hiệu, chứ không phải lời hứa rằng giá sẽ khớp đúng tại mức kích hoạt. Phần này nối risk sizing với thực tế thị trường có gap, spread mở rộng và thanh khoản thay đổi.

Stop là một execution instruction, không phải guarantee giá thoát.

Trong gap hoặc sự kiện (event / 이벤트) lớn, fill có thể xa trigger.

Vì stop là lệnh thực thi có thể bị trượt, mức risk phải được tính với kịch bản fill xấu chứ không chỉ với giá trigger trên chart. Để so sánh các trade sau đó, ta quy đổi rủi ro ban đầu thành đơn vị R.

## 22. R-multiple

R-multiple đặt mọi trade lên cùng một thước đo: một R là số tiền đã chấp nhận mất nếu invalidation xảy ra. Nhờ vậy, kết quả không bị đánh lừa bởi việc một trade có notional lớn hơn trade khác.

`R` là lượng rủi ro ban đầu.

Ví dụ rủi ro (risk / 위험) 100 USD:

```text
-1R = -100 USD
+2R = +200 USD
```

R giúp so trade khác nhau bằng cùng đơn vị rủi ro.

Khi đã có đơn vị chung, ta có thể hỏi một hệ thống thắng–thua có tạo kỳ vọng dương sau khi tính cả kích thước thắng và thua hay không. Đó là câu hỏi của expectancy.

## 23. Expectancy

Expectancy không dự đoán trade kế tiếp; nó kiểm tra phân phối kết quả trong một mẫu đủ lớn. Công thức dưới đây nối win rate với quy mô lãi/lỗ để tránh kết luận sai rằng thắng nhiều lần luôn có nghĩa là có edge.

```text
Expectancy
= Win Rate × Average Win
- Loss Rate × Average Loss
```

Win tỷ lệ (rate / 비율) cao không bảo đảm có edge.

Vì vậy, trước khi tăng size, cần kiểm tra expectancy có còn dương sau cost và ở các regime khác nhau. Nếu edge mỏng hoặc trade tương quan cao, nguy cơ không sống sót sẽ được mô tả bằng risk of ruin.

## 24. Risk of ruin

Risk of ruin chuyển câu hỏi từ “lợi nhuận kỳ vọng bao nhiêu?” sang “xác suất tài khoản không còn khả năng tiếp tục là bao nhiêu?”. Phần này buộc ta nhìn đồng thời risk/trade, edge, độ dài drawdown và tương quan giữa các lệnh.

Risk of ruin tăng khi:

- rủi ro (risk / 위험)/trade lớn;
- edge nhỏ;
- drawdown kéo dài;
- correlation giữa trade cao.

Survival quan trọng hơn tối đa hóa short-term return.

Điểm chốt là một hệ thống phải sống đủ lâu để edge có cơ hội xuất hiện. Điều kiện thanh khoản và biến động trong từng phiên sẽ làm phân phối đó khác nhau, nên ta tiếp tục với sessions.

## 25. Sessions

Các phiên Asia, London và New York không chỉ là nhãn thời gian; chúng đại diện cho khác biệt về thanh khoản, overlap và thời điểm dữ liệu kinh tế được công bố. Mục tiêu là biết khi nào cost và volatility có thể đổi trước khi áp dụng cùng một rule.

Forex có đặc điểm khác nhau theo Asia, London và New York session.

Liquidity và volatility thường thay đổi quanh overlap và dữ liệu (data / 데이터) bản phát hành (release / 릴리스).

Do đó, một backtest cần giữ timestamp và điều kiện phiên, nếu không kết quả có thể trộn các môi trường không giống nhau. News event là trường hợp mà sự thay đổi đó diễn ra rất nhanh.

## 26. News event

News event tạo ra một bài toán thực thi riêng: thông tin mới có thể làm spread rộng, slippage tăng và mức ký quỹ thay đổi trước khi lệnh stop được khớp. Phần này giúp lập kế hoạch trước release thay vì phản ứng sau khi giá đã gap.

CPI, NFP, central-bank decision hoặc geopolitical shock có thể làm:

- spread widen;
- slippage tăng;
- stop gap;
- margin thay đổi.

Sự kiện (event / 이벤트) trading đòi hỏi thực thi (execution / 실행) plan trước bản phát hành (release / 릴리스).

Kết luận là không nên dùng cùng một giả định fill và size cho ngày bình thường với ngày có event lớn. XAUUSD là ví dụ tiếp theo cho tài sản có nhiều driver cùng lúc và không thể rút gọn thành một quy tắc đơn.

## 27. XAUUSD

Vàng thường được dùng như hedge hoặc tài sản trú ẩn, nhưng giá của nó phản ứng với nhiều biến: real yield, USD, nhu cầu ngân hàng trung ương, địa chính trị và positioning. Phần này dạy cách giữ nhiều giả thuyết cùng lúc thay vì gắn vàng với một câu chuyện lạm phát duy nhất.

Gold chịu ảnh hưởng của:

- real yield;
- USD;
- central-bank demand;
- geopolitics;
- inflation regime;
- positioning.

Không dùng quy tắc đơn giản “inflation tăng → gold tăng”.

Vì vậy, khi giao dịch XAUUSD hãy ghi rõ driver nào đang chi phối và điều kiện nào làm luận điểm sai. Nếu chuyển sang futures, ta thêm lớp hợp đồng chuẩn hóa, expiry và settlement vào phân tích.

## 28. Futures

Futures đưa khái niệm notional và margin vào một hợp đồng có quy tắc giao dịch, đáo hạn và thanh toán rõ ràng. Người mới cần phân biệt giá biến động bao nhiêu với mỗi tick có giá trị tiền bao nhiêu.

Futures là hợp đồng chuẩn hóa trên exchange.

Cần hiểu:

- multiplier;
- tick;
- expiry;
- margin;
- settlement;
- basis;
- roll.

Các tham số này quyết định P/L, collateral và chi phí chuyển kỳ; bỏ qua một tham số có thể làm sai cả position sizing. Options tiếp tục cùng câu chuyện nhưng payoff phi tuyến và nhạy với nhiều biến hơn.

## 29. Options

Options không chỉ là “mua call hoặc put”; chúng là hợp đồng có payoff phi tuyến, trong đó giá còn phụ thuộc thời gian, biến động, lãi suất và các Greek. Bắt đầu bằng payoff khi đáo hạn giúp ta hiểu sau đó vì sao giá trước đáo hạn không chỉ đi theo hướng của tài sản cơ sở.

Option tạo payoff phi tuyến.

```text
Call = max(S-K, 0)
Put  = max(K-S, 0)
```

Trước expiry, giá option còn phụ thuộc volatility, thời gian (time / 시간), rates và Greeks.

Điểm chốt là cùng một hướng giá có thể tạo P/L khác nhau tùy IV, theta và cấu trúc vị thế. CFD là trường hợp đối chiếu về cấu trúc pháp lý và đối tác, nơi điều khoản broker cần được đọc trước payoff.

## 30. CFD

CFD thường không phải hợp đồng niêm yết trên exchange mà là thỏa thuận song phương với broker. Vì vậy, rủi ro không chỉ nằm ở hướng giá mà còn ở pháp nhân, financing, stop-out, execution model và jurisdiction.

CFD thường là bilateral contract với broker.

Cần kiểm tra:

- legal thực thể (entity / 엔터티);
- financing chi phí (cost / 비용);
- spread;
- mô hình thực thi (execution model / 실행 모델);
- stop-out;
- jurisdiction.

Trước khi so CFD với futures hoặc spot, hãy ghi rõ quyền và nghĩa vụ hợp đồng, cách tính funding và điều kiện đóng cưỡng bức. Sau lớp sản phẩm, ta chuyển sang kiểm thử xem một rule có còn hoạt động khi tái tạo dữ liệu và execution quá khứ hay không.

## 31. Backtest

Backtest là thí nghiệm lịch sử có kỷ luật: chỉ dùng thông tin mà trader thật sự có thể biết tại từng thời điểm và mô phỏng chi phí đủ thực tế. Nó không phải giấy chứng nhận rằng chiến lược sẽ thắng trong tương lai.

Backtest phải cố tái tạo thông tin và execution có thể có thật tại thời điểm quá khứ.

Sai lầm phổ biến:

- look-ahead độ lệch (bias / 편향);
- survivorship độ lệch (bias / 편향);
- dữ liệu (data / 데이터) snooping;
- bỏ giao dịch (transaction / 트랜잭션) chi phí (cost / 비용);
- bỏ slippage.

Nếu bỏ một trong các bias hoặc cost trên, expectancy và drawdown có thể bị thổi phồng. Vì vậy, sau backtest cần một giai đoạn ngoài mẫu hoặc forward test trước khi đưa vốn đáng kể vào hệ thống.

## 32. Forward test

Forward test kiểm tra rule trong dữ liệu mới hoặc môi trường mô phỏng gần thực tế sau khi logic đã được khóa. Mục đích là phát hiện drift, lỗi thực thi và kỳ vọng không còn đúng, không phải tiếp tục chỉnh rule cho vừa kết quả.

Sau backtest nên có out-of-sample hoặc forward test trước khi dùng capital đáng kể.

Hãy ghi lại điều kiện, phiên bản rule và cost trong giai đoạn này; nếu thay đổi giữa chừng, đó là thí nghiệm mới. Trading journal là nơi lưu chuỗi bằng chứng đó.

## 33. Trading journal

Journal biến mỗi trade thành dữ liệu để review thay vì ký ức chọn lọc. Hãy ghi cả lý do vào lệnh, risk đã định, execution thực tế và vi phạm rule để phân biệt lỗi chiến lược với lỗi kỷ luật.

Journal nên ghi:

```text
Setup
Reason
Risk
Expected Outcome
Actual Execution
MAE / MFE
Result
Rule Violation
Lesson
```

Sau một chuỗi đủ dài, journal cho biết MAE/MFE, cost và lỗi lặp lại ở đâu. Khi nhiều trade cùng phơi nhiễm một factor, review phải nâng lên cấp danh mục thay vì chỉ xem từng lệnh.

## 34. Psychology

Tâm lý là lớp thực thi của một hệ thống có edge. Nó không thể biến một rule không có kỳ vọng dương thành strategy tốt, nhưng có thể phá hỏng strategy tốt nếu hành vi thực tế khác với giả định khi nghiên cứu.

Tâm lý không thể sửa một strategy không có edge.

Nhưng một chiến lược (strategy / 전략) có edge vẫn có thể thất bại nếu trader:

- tăng kích thước (size / 크기) sau mất mát (loss / 손실);
- bỏ quy tắc (rule / 규칙);
- revenge trade;
- stop quá sớm;
- overtrade.

Vì vậy, journal và giới hạn risk phải được thiết kế để nhận diện hành vi trước khi drawdown trở thành khủng hoảng. Portfolio heat tiếp tục câu hỏi đó ở cấp tổng exposure.

## 35. Portfolio heat

Portfolio heat đo tổng rủi ro có thể cùng phát sinh nếu nhiều trade thực chất là một factor ẩn. Nhìn từng risk/trade riêng lẻ có thể bỏ qua việc các vị thế cùng nhạy với USD, lãi suất hoặc thanh khoản.

Nhiều trade riêng lẻ có thể cùng chịu một factor.

Ví dụ long EUR/USD, long GBP/USD và long gold có thể cùng là short-USD exposure.

Cần nhìn tổng rủi ro (risk / 위험), không chỉ rủi ro (risk / 위험)/trade.

Điểm chốt là sizing phải xét cả tương quan và stress chung, không chỉ công thức của từng lệnh. Kelly là một khung lý thuyết để nói về sizing theo growth, nhưng phải được thu nhỏ khi edge ước lượng không chắc.

## 36. Kelly

Kelly criterion trả lời bài toán lý thuyết: với một phân phối và edge đã biết chính xác, tỷ lệ vốn nào tối đa hóa log-growth? Trong trading thật, các giả định đó hiếm khi hoàn hảo nên cần đọc Kelly như giới hạn tham khảo, không phải mệnh lệnh dùng hết vốn.

Kelly criterion cho sizing tối ưu theo growth trong điều kiện giả định hoàn hảo.

Thực tế thường dùng fractional Kelly vì:

- edge estimate không chắc;
- phân phối (distribution / 분포) có fat tail;
- drawdown tâm lý lớn.

Fractional Kelly tạo khoảng đệm cho sai số ước lượng và fat tail. Monte Carlo tiếp theo giúp nhìn nhiều thứ tự trade và phân phối drawdown, nhưng không thể cứu dữ liệu nguồn kém.

## 37. Monte Carlo

Monte Carlo không dự đoán thứ tự trade sẽ xảy ra; nó mô phỏng nhiều thứ tự hợp lý để cho thấy cùng một expectancy có thể tạo các đường vốn và drawdown rất khác nhau. Đây là công cụ kiểm tra độ bền của giả định, không phải máy tạo edge.

Monte Carlo giúp kiểm tra nhiều thứ tự trade khác nhau để thấy drawdown distribution và risk of ruin.

Nó không sửa được mẫu (sample / 표본) kém chất lượng.

Sau khi biết phân phối rủi ro, ta quay về dữ liệu từng trade để xem giá đã đi ngược hoặc đi thuận bao xa trước khi đóng: đó là vai trò của MAE và MFE.

## 38. MAE và MFE

MAE và MFE biến đường đi trong trade thành dữ liệu để sửa stop và exit. Một trade có thể kết thúc cùng P/L nhưng đã chịu mức adverse excursion rất khác, nên kết quả cuối cùng không đủ để hiểu chất lượng rule.

**Maximum Adverse Excursion (MAE)** đo mức đi ngược lớn nhất trước khi trade đóng.

**Maximum Favorable Excursion (MFE)** đo mức có lợi lớn nhất.

Hai chỉ số (metric / 지표) giúp cải thiện stop và exit quy tắc (rule / 규칙).

Hãy dùng chúng để kiểm tra stop có quá chặt hay exit có bỏ lỡ phần lợi nhuận hợp lý, rồi đối chiếu với profit factor và drawdown thay vì tối ưu một metric riêng lẻ.

## 39. Profit factor

Profit factor cho biết tổng lãi gộp lớn bao nhiêu so với tổng lỗ gộp, nhưng không nói mẫu có đủ lớn, ổn định hay chịu được cost hay không. Vì vậy, công thức cần được đọc cùng các chỉ số về đường vốn và rủi ro đuôi.

```text
Profit Factor
= Gross Profit / Gross Loss
```

Cần đọc cùng cỡ mẫu (sample size / 표본 크기), drawdown và chi phí (cost / 비용).

Nếu profit factor chỉ đẹp trước phí hoặc dựa trên ít trade, nó không đủ làm bằng chứng. Các ratio Sharpe/Sortino/Calmar tiếp tục bổ sung góc nhìn về return trên risk nhưng cũng có giới hạn riêng.

## 40. Sharpe / Sortino / Calmar

Ba ratio này nén mối quan hệ giữa return và một cách đo risk khác nhau: biến động tổng, downside hoặc drawdown. Chúng giúp so sánh có điều kiện, không thay thế việc đọc tail risk, thanh khoản và leverage của hệ thống.

Các ratio này mô tả return so với risk theo góc khác nhau nhưng không thay thế:

- tail rủi ro (risk / 위험);
- liquidity;
- leverage;
- operational rủi ro (risk / 위험).

Do đó, không chọn strategy chỉ vì một ratio cao. Cần hỏi ratio đó được tạo trong regime nào và có còn đúng khi điều kiện thị trường đổi hay không.

## 41. Regime dependence

Regime dependence là phép kiểm tra xem edge có phải chỉ là sản phẩm của một môi trường cụ thể. Một strategy có thể rất tốt khi trend rõ nhưng suy yếu trong range hoặc khi liquidity cạn, vì vậy phân tích phải chỉ ra điều kiện tạo và phá edge.

Một strategy có thể kiếm tiền chỉ trong một regime.

Cần biết edge phụ thuộc:

- trend;
- volatility;
- carry;
- liquidity;
- macro môi trường (environment / 환경).

Điểm chốt là cần ghi rõ phạm vi áp dụng và điều kiện vô hiệu hóa, thay vì quảng bá một kết quả trung bình cho mọi thời kỳ. Trước khi chạy bất kỳ rule nào, còn một lớp rủi ro nền tảng là broker và khả năng giữ tài sản.

## 42. Broker safety

Broker safety đặt câu hỏi liệu kết quả trên giấy có thể chuyển thành tiền rút được hay không. Hãy kiểm tra pháp nhân, quy tắc custody/margin, cơ chế stop-out, phí và khả năng rút tiền trước khi tối ưu setup.

Trước khi quan tâm setup, cần hiểu broker legal entity, custody/margin rules và khả năng rút tiền.

Một strategy tốt không bù được rủi ro đối tác hoặc vận hành không được hiểu rõ. Sau khi hoàn tất lớp nền này, bản đồ dưới đây chỉ rõ chapter chuyên sâu nào nên được mở tiếp theo.

## 43. Từ master map tới chapter chuyên sâu

Phần này là điểm bàn giao, không phải một danh sách link độc lập. Mỗi chapter trả lời một lớp câu hỏi đã được mở trong master map: cấu trúc hợp đồng, nghiên cứu hệ thống, thực thi, độ bền hoặc quyền chọn.

Đọc tiếp:

- [01_DERIVATIVES_FUTURES_OPTIONS_CFD.md](./01_DERIVATIVES_FUTURES_OPTIONS_CFD.md): hợp đồng phái sinh;
- [02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md](./02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md): nghiên cứu hệ thống;
- [03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md](./03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md): thực thi và microstructure;
- [04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md](./04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md): robustness và portfolio of strategies;
- [05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md](./05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md): options và volatility.

Hãy chọn đúng chapter theo lỗ hổng hiện tại, giữ lại mental model ở các phần trước và quay về master map sau mỗi vòng học để cập nhật câu hỏi còn thiếu.

## Kết luận

Ta có thể khép toàn bộ bài bằng cách nối lại các lớp: giả thuyết tạo edge, sizing giới hạn tổn thất, execution biến ý định thành fill, risk control giữ khả năng sống sót và discipline bảo đảm quy tắc được thực hiện.

Trading nên được xem là một hệ thống xác suất:

```text
Edge
× Position Sizing
× Execution Quality
× Risk Control
× Discipline
```

Leverage không tạo lợi thế. Pattern không thay thế expectancy. Và một strategy chỉ đáng dùng khi nó sống sót sau chi phí, stress và sai số thực tế.

Nếu chưa thể giải thích trade theo chuỗi trên bằng số liệu và điều kiện cụ thể, hãy quay lại phần còn thiếu thay vì tăng leverage hoặc thêm pattern.

## Đi tiếp theo một đường duy nhất

Đường đi dưới đây là chu trình triển khai một ý tưởng Forex từ giả thuyết đến review. Mỗi bước có owner rõ ràng; không nên bỏ qua nghiên cứu, thực thi hoặc template chỉ vì một backtest ban đầu trông đẹp.

Sau master map, giữ đúng thứ tự này cho một ý tưởng Forex:

```text
Hypothesis
→ 02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md
→ 03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md
→ 06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md
→ STOCK_FOREX_RESEARCH_TEMPLATE.md
→ 07_integrated_case_studies/05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md
```

Dùng [Quy trình dữ liệu và nghiên cứu — Cổ phiếu / Forex](../STOCK_FOREX_DATA_RESEARCH_WORKFLOW.md) trước khi lấy dữ liệu; dùng [Sổ tay quản trị rủi ro — Cổ phiếu và Forex](../STOCK_FOREX_RISK_PLAYBOOK.md) trước khi mô phỏng sizing. Các pattern chỉ là cách mô tả tín hiệu, không phải điểm bắt đầu của lộ trình.

Khi hoàn thành chu trình, quay lại master map và ghi rõ điều kiện tiếp tục, điều kiện dừng và dữ liệu cần cập nhật. Đó là điểm kết thúc của một vòng học và cũng là điểm bắt đầu của vòng review tiếp theo.
