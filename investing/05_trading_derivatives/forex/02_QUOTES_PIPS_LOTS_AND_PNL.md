# 02 — Quotes, pips, lots và cơ chế P/L trong Forex

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Cơ sở (base / 기반) currency và quote currency** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Long và short một currency pair nghĩa là gì?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối quotes, pips, lots và PnL, để một thay đổi tỷ giá được chuyển đúng thành quy mô vị thế và lãi/lỗ.

Sau khi hiểu Forex không phải một centralized exchange duy nhất, bước tiếp theo là hiểu **một quote thực sự nói điều gì và biến động của quote biến thành tiền lời/lỗ như thế nào**.

Đây là phần nên có khả năng tự tính bằng tay. Calculator của broker tiện lợi, nhưng nếu không tự suy luận được P/L thì rất dễ nhầm giữa lot, notional, margin và rủi ro (risk / 위험).

Mô hình tư duy (mental model / 사고 모델) của chương:

```text
Currency pair
→ base / quote relationship
→ trade size in base currency
→ price change
→ P/L in quote currency
→ conversion into account currency
```

## 1. Cơ sở (base / 기반) currency và quote currency

Với:

```text
EUR/USD = 1.1200
```

EUR là **đồng tiền cơ sở (base currency, 기준통화)**.

USD là **đồng tiền định giá (quote currency / counter currency, 상대통화)**.

Quote nói rằng:

```text
1 EUR costs 1.1200 USD
```

Cách đọc tổng quát:

```text
A/B = X
```

nghĩa là:

```text
1 unit of A = X units of B
```

Nếu `A/B` tăng, A mạnh lên tương đối với B. Nếu `A/B` giảm, A yếu đi tương đối với B.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **2. Long và short một currency pair nghĩa là gì?** tiếp nhận điểm tựa từ **1. Cơ sở (base / 기반) currency và quote currency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Bid và ask** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Long và short một currency pair nghĩa là gì?

### Long EUR/USD

Bạn nhận exposure:

```text
Long EUR
Short USD
```

Bạn có lợi nếu EUR tăng giá tương đối so với USD.

### Short EUR/USD

Bạn nhận exposure:

```text
Short EUR
Long USD
```

Bạn có lợi nếu EUR giảm giá tương đối so với USD.

Đây là lý do mọi FX position đều chứa **hai currency exposures**. Nói “tôi long EUR” khi thực tế long EUR/USD là chưa đầy đủ; bạn long EUR **against USD**.

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **3. Bid và ask** tiếp nhận điểm tựa từ **2. Long và short một currency pair nghĩa là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Spread** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Bid và ask

Một quote executable có hai phía, ví dụ:

```text
EUR/USD
Bid  1.11998
Ask  1.12003
```

Broker/dealer sẵn sàng:

```text
buy EUR from you at Bid
sell EUR to you at Ask
```

Vì thế:

```text
Buy / open long  → thường khớp gần Ask
Sell / open short → thường khớp gần Bid
```

Nếu ngay lập tức đóng position mà thị trường (market / 시장) không thay đổi, bạn thường chịu spread.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **4. Spread** tiếp nhận điểm tựa từ **3. Bid và ask** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Pip là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Spread

**Chênh lệch mua bán (bid-ask spread, 스프레드)**:

```text
Spread = Ask - Bid
```

Với quote trên:

```text
1.12003 - 1.11998 = 0.00005
```

Nếu pip kích thước (size / 크기) là `0.0001`, spread là:

```text
0.5 pip
```

Spread là một phần giao dịch (transaction / 트랜잭션) chi phí (cost / 비용). Effective chi phí (cost / 비용) còn có thể gồm:

```text
commission
+ slippage
+ financing / rollover
+ market impact
```

Vì vậy một chiến lược (strategy / 전략) gross-profitable có thể net-unprofitable sau chi phí.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **5. Pip là gì?** tiếp nhận điểm tựa từ **4. Spread** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Lot là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Pip là gì?

**Pip** là đơn vị thay đổi giá quy ước.

Đối với nhiều currency pair không có JPY ở quote side:

```text
1 pip = 0.0001
```

Ví dụ:

```text
EUR/USD
1.1200 → 1.1201
= +1 pip
```

Đối với nhiều JPY pair:

```text
1 pip = 0.01
```

Ví dụ:

```text
USD/JPY
150.20 → 150.21
= +1 pip
```

Nền tảng (platform / 플랫폼) hiện đại thường quote thêm một decimal nhỏ hơn pip, thường gọi là **pipette / fractional pip**.

Ví dụ:

```text
EUR/USD = 1.12003
```

decimal cuối cùng `0.00001` tương ứng 1/10 pip theo convention phổ biến của pair này.

Không nên hard-code convention mà không kiểm tra đặc tả hợp đồng (contract / 계약) specification, đặc biệt với exotic pair hoặc sản phẩm (product / 제품) khác FX spot convention.

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **6. Lot là gì?** tiếp nhận điểm tựa từ **5. Pip là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Notional là exposure, không phải số tiền ký quỹ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Lot là gì?

Trong retail FX, **lot** thường là cách biểu diễn trade kích thước (size / 크기) theo số units của cơ sở (base / 기반) currency.

Convention rất phổ biến:

```text
1 standard lot = 100,000 base-currency units
0.1 lot         = 10,000 units
0.01 lot        = 1,000 units
```

Ví dụ:

```text
0.1 lot EUR/USD
= 10,000 EUR exposure on base side
```

Nhưng `lot` là **đặc tả hợp đồng (contract / 계약) convention**, không phải định luật tự nhiên. Broker hoặc instrument khác có thể dùng đặc tả hợp đồng (contract / 계약) kích thước (size / 크기) khác. Luôn đọc specification.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **7. Notional là exposure, không phải số tiền ký quỹ** tiếp nhận điểm tựa từ **6. Lot là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Công thức P/L cơ bản khi quote currency là currency bạn muốn tính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Notional là exposure, không phải số tiền ký quỹ

**Giá trị danh nghĩa (notional)** là quy mô kinh tế của position.

Nếu long:

```text
100,000 EUR at EUR/USD = 1.1200
```

Cơ sở (base / 기반) notional là:

```text
100,000 EUR
```

quy đổi theo USD tại thời điểm đó xấp xỉ:

```text
100,000 × 1.1200
= 112,000 USD
```

Nếu broker chỉ yêu cầu margin vài nghìn USD, exposure vẫn là khoảng 112.000 USD. Margin không biến position thành một investment nhỏ hơn; nó chỉ cho phép collateral nhỏ hơn notional.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **8. Công thức P/L cơ bản khi quote currency là currency bạn muốn tính** tiếp nhận điểm tựa từ **7. Notional là exposure, không phải số tiền ký quỹ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Ví dụ EUR/USD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Công thức P/L cơ bản khi quote currency là currency bạn muốn tính

Với pair:

```text
A/B
```

trade kích thước (size / 크기) `Q` units của cơ sở (base / 기반) currency A.

Một long position có P/L theo quote currency B gần bằng:

```text
P/L_B = Q × (Exit Price - Entry Price)
```

Một short position:

```text
P/L_B = Q × (Entry Price - Exit Price)
```

Hoặc dùng signed position:

```text
P/L_B = Signed_Q × (Exit - Entry)
```

với `Signed_Q > 0` cho long và `< 0` cho short.

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **8. Công thức P/L cơ bản khi quote currency là currency bạn muốn tính** cho ta quy tắc; **9. Ví dụ EUR/USD** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **10. Pip giá trị (value / 값) được suy ra, không cần học thuộc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Ví dụ EUR/USD

Long 1 tiêu chuẩn (standard / 표준) lot:

```text
Q = 100,000 EUR
Entry = 1.1200
Exit  = 1.1250
```

Price thay đổi (change / 변경):

```text
1.1250 - 1.1200 = 0.0050
```

Tương đương:

```text
50 pips
```

P/L:

```text
100,000 × 0.0050
= 500 USD
```

Đây là lý do với `100,000` units EUR/USD, khi pip kích thước (size / 크기) là `0.0001`:

```text
Pip Value
= 100,000 × 0.0001
= 10 USD/pip
```

50 pips × 10 USD = 500 USD.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **9. Ví dụ EUR/USD** cho ta quy tắc; **10. Pip giá trị (value / 값) được suy ra, không cần học thuộc** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **11. JPY pair: vì sao pip giá trị (value / 값) khác?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Pip giá trị (value / 값) được suy ra, không cần học thuộc

Với pair `A/B`:

```text
Pip Value in B
= Base Units × Pip Size
```

Ví dụ `10,000 EUR` trên EUR/USD:

```text
10,000 × 0.0001
= 1 USD/pip
```

Ví dụ `100,000 GBP` trên GBP/USD:

```text
100,000 × 0.0001
= 10 USD/pip
```

Điểm quan trọng là pip giá trị (value / 값) phụ thuộc trade kích thước (size / 크기) và quote convention.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **11. JPY pair: vì sao pip giá trị (value / 값) khác?** tiếp nhận điểm tựa từ **10. Pip giá trị (value / 값) được suy ra, không cần học thuộc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Khi account currency khác quote currency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. JPY pair: vì sao pip giá trị (value / 값) khác?

Long `100,000 USD` trên USD/JPY.

Pip kích thước (size / 크기) thường là:

```text
0.01 JPY per USD
```

Pip giá trị (value / 값) theo JPY:

```text
100,000 × 0.01
= 1,000 JPY/pip
```

Nếu account dùng USD, phải convert 1.000 JPY về USD theo tỷ giá hiện tại.

Giả sử USD/JPY khoảng `150`:

```text
1 USD ≈ 150 JPY
```

thì:

```text
1,000 JPY / 150
≈ 6.67 USD/pip
```

Pip giá trị (value / 값) theo USD do đó thay đổi khi USD/JPY thay đổi. Đây là lý do không nên học thuộc “1 lot luôn = 10 USD/pip”. Điều đó chỉ đúng cho một số cấu trúc pair/account currency nhất định.

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **12. Khi account currency khác quote currency** tiếp nhận điểm tựa từ **11. JPY pair: vì sao pip giá trị (value / 값) khác?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Cross currency pair** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Khi account currency khác quote currency

Giả sử account bằng KRW nhưng trade EUR/USD.

P/L trước hết hình thành theo USD:

```text
EUR/USD trade
→ P/L in USD
```

sau đó nền tảng (platform / 플랫폼) phải quy đổi:

```text
USD P/L
→ KRW P/L
```

Do đó account-level kết quả (outcome / 결과) còn chịu conversion tỷ lệ (rate / 비율).

Mô hình tư duy (mental model / 사고 모델):

```text
Instrument P/L currency
→ account currency conversion
→ final account P/L
```

Nếu account currency khác cả cơ sở (base / 기반) lẫn quote, đừng bỏ qua bước conversion.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **13. Cross currency pair** tiếp nhận điểm tựa từ **12. Khi account currency khác quote currency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Khi nào chia thay vì nhân?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Cross currency pair

Một **cross** là pair không dùng USD trực tiếp, ví dụ EUR/JPY hay EUR/GBP.

Cross tỷ lệ (rate / 비율) có thể được suy ra từ các pair liên quan.

Nếu:

```text
EUR/USD = 1.1200
USD/JPY = 150.00
```

thì approximate no-arbitrage mid cross:

```text
EUR/JPY
≈ EUR/USD × USD/JPY
≈ 1.1200 × 150
≈ 168.00
```

Thực tế executable cross phải xử lý bid/ask đúng phía, giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) và venue differences. Nhưng phép nhân này cho thấy cross tỷ lệ (rate / 비율) không phải một con số tách rời khỏi hệ thống FX.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **14. Khi nào chia thay vì nhân?** tiếp nhận điểm tựa từ **13. Cross currency pair** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Đơn vị (unit / 단위) phân tích (analysis / 분석) giúp tránh nhầm công thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Khi nào chia thay vì nhân?

Nếu hai pair có cùng quote currency:

```text
EUR/USD
GBP/USD
```

muốn suy ra EUR/GBP:

```text
EUR/GBP
≈ (EUR/USD) / (GBP/USD)
```

Ví dụ:

```text
EUR/USD = 1.1200
GBP/USD = 1.2800
```

thì:

```text
EUR/GBP ≈ 1.1200 / 1.2800
≈ 0.8750
```

Cách tốt nhất không phải học công thức nhân/chia, mà kiểm tra đơn vị như algebra:

```text
USD cancels out
```

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **14. Khi nào chia thay vì nhân?** đã nêu tiêu chí phân biệt, còn **15. Đơn vị (unit / 단위) phân tích (analysis / 분석) giúp tránh nhầm công thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **16. Direct quote và indirect quote** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Đơn vị (unit / 단위) phân tích (analysis / 분석) giúp tránh nhầm công thức

Viết quote như fraction của units:

```text
EUR/USD = USD per EUR
USD/JPY = JPY per USD
```

Nhân:

```text
(USD / EUR) × (JPY / USD)
= JPY / EUR
```

USD bị triệt tiêu, còn lại JPY per EUR → chính là EUR/JPY quote.

Cách đơn vị (unit / 단위) phân tích (analysis / 분석) này đáng tin hơn học thuộc mnemonic.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **15. Đơn vị (unit / 단위) phân tích (analysis / 분석) giúp tránh nhầm công thức** đã nêu tiêu chí phân biệt, còn **16. Direct quote và indirect quote** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **17. Percentage return và pip move không phải cùng một thứ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Direct quote và indirect quote

Khái niệm direct/indirect phụ thuộc home currency của người quan sát.

Nếu home currency là KRW:

```text
USD/KRW
= KRW per USD
```

là cách trực tiếp biểu diễn một USD trị giá bao nhiêu KRW.

Trong tài liệu quốc tế, các pair conventions đã được thị trường (market / 시장) tiêu chuẩn (standard / 표준) hóa theo ticker, nên khi trading tốt hơn hết đọc cơ sở (base / 기반)/quote rõ ràng thay vì phụ thuộc vào từ “direct” có thể gây nhầm theo viewpoint.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **17. Percentage return và pip move không phải cùng một thứ** tiếp nhận điểm tựa từ **16. Direct quote và indirect quote** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Price return của pair và return của currency không hoàn toàn đối xứng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Percentage return và pip move không phải cùng một thứ

EUR/USD tăng:

```text
1.1000 → 1.1100
```

là `100 pips`, nhưng percentage move gần:

```text
(1.1100 / 1.1000) - 1
≈ 0.91%
```

USD/JPY đi `100 pips` nghĩa là thay đổi `1.00` JPY, nhưng percentage move còn tùy starting mức (level / 수준).

Do đó so volatility giữa pair chỉ bằng số pip có thể gây sai. Percentage return hoặc normalized volatility thường phù hợp hơn cho cross-asset/rủi ro (risk / 위험) phân tích (analysis / 분석).

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **18. Price return của pair và return của currency không hoàn toàn đối xứng** tiếp nhận điểm tựa từ **17. Percentage return và pip move không phải cùng một thứ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Gross P/L khác net P/L** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Price return của pair và return của currency không hoàn toàn đối xứng

Nếu EUR/USD tăng 10%, USD/EUR không giảm đúng 10%.

Nếu:

```text
EUR/USD = 1.00 → 1.10
```

EUR/USD tăng 10%.

Inverse:

```text
USD/EUR = 1.00 → 1/1.10 ≈ 0.9091
```

USD/EUR giảm khoảng 9.09%.

Return đơn giản không đối xứng qua inversion. Log return có tính chất thuận tiện hơn:

```text
ln(A/B return) = -ln(B/A return)
```

Điều này quan trọng ở phần quantitative research sau này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **19. Gross P/L khác net P/L** tiếp nhận điểm tựa từ **18. Price return của pair và return của currency không hoàn toàn đối xứng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Rollover / financing làm P/L thay đổi theo thời gian giữ lệnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Gross P/L khác net P/L

Ví dụ chiến lược (strategy / 전략) tạo gross profit:

```text
+500 USD
```

nhưng chịu:

```text
spread cost      -80
commission       -20
slippage         -35
overnight carry  -25
```

Net:

```text
500 - 80 - 20 - 35 - 25
= 340 USD
```

Một backtest bỏ chi phí (cost / 비용) đang mô hình hóa một thị trường không tồn tại.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **20. Rollover / financing làm P/L thay đổi theo thời gian giữ lệnh** tiếp nhận điểm tựa từ **19. Gross P/L khác net P/L** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. XAU/USD không phải currency pair theo nghĩa giống EUR/USD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Rollover / financing làm P/L thay đổi theo thời gian giữ lệnh

Leveraged FX position giữ qua rollover có thể phát sinh financing debit hoặc credit tùy sản phẩm (product / 제품), currency-rate relationship và broker terms.

Không nên suy luận đơn giản:

```text
high-yield currency long
→ always receive positive swap
```

vì retail financing còn phụ thuộc:

- broker markup;
- benchmark/tham chiếu (reference / 참조) tỷ lệ (rate / 비율);
- day-count convention;
- holiday/weekend adjustment;
- sản phẩm (product / 제품) cấu trúc (structure / 구조);
- long/short asymmetry.

Luôn đọc swap/financing specification thực tế.

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **21. XAU/USD không phải currency pair theo nghĩa giống EUR/USD** tiếp nhận điểm tựa từ **20. Rollover / financing làm P/L thay đổi theo thời gian giữ lệnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Từ lot đến rủi ro (risk / 위험): còn thiếu stop distance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. XAU/USD không phải currency pair theo nghĩa giống EUR/USD

Retail nền tảng (platform / 플랫폼) thường đặt `XAU/USD` cạnh Forex pairs. XAU là mã (code / 코드) cho gold, nên:

```text
XAU/USD
= USD price per unit of gold defined by contract
```

Đặc tả hợp đồng (contract / 계약) kích thước (size / 크기) có thể khác giữa broker/sản phẩm (product / 제품). Không được áp dụng máy móc:

```text
1 standard FX lot = 100,000 base units
```

cho XAU/USD.

Cần kiểm tra đặc tả hợp đồng (contract / 계약) kích thước (size / 크기), tick kích thước (size / 크기), margin, financing và price nguồn (source / 소스) riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **22. Từ lot đến rủi ro (risk / 위험): còn thiếu stop distance** tiếp nhận điểm tựa từ **21. XAU/USD không phải currency pair theo nghĩa giống EUR/USD** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Công thức sizing từ allowed mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Từ lot đến rủi ro (risk / 위험): còn thiếu stop distance

Giả sử hai trader cùng trade `0.1 lot EUR/USD`.

Trader A stop 10 pips.

Trader B stop 100 pips.

Pip giá trị (value / 값) giả sử 1 USD/pip:

```text
A initial price risk ≈ 10 USD
B initial price risk ≈ 100 USD
```

Cùng lot nhưng rủi ro (risk / 위험) khác 10 lần.

Vì vậy:

```text
Lot Size ≠ Risk
```

Rủi ro (risk / 위험) phải kết hợp:

```text
position size
× distance to invalidation
× pip value
+ gap/slippage risk
```

Đây là cầu nối sang chương leverage và position sizing.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **23. Công thức sizing từ allowed mất mát (loss / 손실)** tiếp nhận điểm tựa từ **22. Từ lot đến rủi ro (risk / 위험): còn thiếu stop distance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Slippage phá vỡ giả định (assumption / 가정) “stop = chính xác (exact / 정확한) mất mát (loss / 손실)”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Công thức sizing từ allowed mất mát (loss / 손실)

Nếu rủi ro (risk / 위험) ngân sách (budget / 예산) là `R_account` và stop distance `D_pips`:

```text
Required Pip Value
≈ R_account / D_pips
```

Sau đó suy ra cơ sở (base / 기반) units:

```text
Base Units
≈ Required Pip Value / Pip Size
```

nếu P/L quote currency trùng account currency.

Ví dụ muốn rủi ro (risk / 위험) khoảng 100 USD với stop 25 pips trên EUR/USD:

```text
Required Pip Value
= 100 / 25
= 4 USD/pip
```

Vì:

```text
1 EUR unit × 0.0001
= 0.0001 USD/pip
```

nên approximate kích thước (size / 크기):

```text
4 / 0.0001
= 40,000 EUR
≈ 0.4 standard lot
```

Đây mới là lô-gic (logic / 논리) đúng chiều:

```text
Allowed Loss
→ Stop / Invalidation Distance
→ Position Size
```

không phải:

```text
Broker offers 1:100 leverage
→ maximize lot size
```

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **24. Slippage phá vỡ giả định (assumption / 가정) “stop = chính xác (exact / 정확한) mất mát (loss / 손실)”** tiếp nhận điểm tựa từ **23. Công thức sizing từ allowed mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Portfolio exposure có thể ẩn sau nhiều pair** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Slippage phá vỡ giả định (assumption / 가정) “stop = chính xác (exact / 정확한) mất mát (loss / 손실)”

Nếu stop ở 25 pips, expected mất mát (loss / 손실) theo sizing có thể là 100 USD. Nhưng stop thứ tự (order / 순서) không bảo đảm fill đúng trigger price trong mọi thị trường (market / 시장) điều kiện (condition / 조건).

News gap hoặc liquidity vacuum có thể tạo:

```text
planned stop = 25 pips
actual fill = 40 pips away
```

Actual mất mát (loss / 손실) khi đó lớn hơn modeled mất mát (loss / 손실).

Vì vậy rủi ro (risk / 위험) sizing phải có an toàn (safety / 안전) margin cho instrument/sự kiện (event / 이벤트) regime phù hợp, và không được coi stop-loss là hard guarantee.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **25. Portfolio exposure có thể ẩn sau nhiều pair** tiếp nhận điểm tựa từ **24. Slippage phá vỡ giả định (assumption / 가정) “stop = chính xác (exact / 정확한) mất mát (loss / 손실)”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Một cách ghi position rõ ràng hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Portfolio exposure có thể ẩn sau nhiều pair

Giả sử:

```text
Long EUR/USD
Long GBP/USD
Short USD/JPY
```

cả ba đều chứa directional thành phần (component / 컴포넌트) có thể tương đồng: **short USD** theo các đối trọng khác nhau.

Rủi ro (risk / 위험) không nên tính đơn giản:

```text
3 trades × 1% risk = 3 independent risks
```

vì positions có thể cùng chịu USD factor shock.

Cần phân rã exposure theo currencies/factors.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **26. Một cách ghi position rõ ràng hơn** tiếp nhận điểm tựa từ **25. Portfolio exposure có thể ẩn sau nhiều pair** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Những nhầm lẫn cần loại bỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Một cách ghi position rõ ràng hơn

Thay vì chỉ journal:

```text
Long EURUSD 0.5 lot
```

nên có:

```text
Pair: EUR/USD
Direction: Long
Base units: 50,000 EUR
Entry: 1.1200
Stop: 1.1150
Distance: 50 pips
Pip value: ~5 USD/pip if account USD
Planned price loss: ~250 USD before slippage/cost
Macro exposure: long EUR / short USD
Account currency: USD
```

Journal như vậy nối trade notation với actual economic exposure.

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **26. Một cách ghi position rõ ràng hơn** đã nêu tiêu chí phân biệt, còn **27. Những nhầm lẫn cần loại bỏ** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **28. Bài tự kiểm tra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Những nhầm lẫn cần loại bỏ

### “1 lot = 100.000 USD”

Không chính xác. Tiêu chuẩn (standard / 표준) lot phổ biến là `100,000 units of base currency`. Với EUR/USD đó là 100.000 EUR; với GBP/USD là 100.000 GBP.

### “1 pip luôn = 10 USD”

Sai. Phụ thuộc pair, trade kích thước (size / 크기) và account currency.

### “Notional = tiền tôi bỏ vào”

Sai khi leveraged. Margin/collateral có thể nhỏ hơn notional rất nhiều.

### “Stop 1% giá = rủi ro (risk / 위험) 1% tài khoản”

Không đúng nếu chưa sizing position dựa trên account rủi ro (risk / 위험).

### “100 pips trên mọi pair có cùng economic rủi ro (risk / 위험)”

Sai. Pip kích thước (size / 크기), pip giá trị (value / 값), volatility và percentage move khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **27. Những nhầm lẫn cần loại bỏ** đã nêu tiêu chí phân biệt, còn **28. Bài tự kiểm tra** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **29. Checklist trước khi sang leverage/margin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Bài tự kiểm tra

### Trường hợp (case / 사례) A

EUR/USD = `1.1000`, bạn long `20,000 EUR`, exit `1.1050`.

```text
Move = 50 pips
Pip value = 20,000 × 0.0001 = 2 USD
P/L ≈ 100 USD
```

### Trường hợp (case / 사례) B

USD/JPY = `150.00`, trade kích thước (size / 크기) `100,000 USD`, move 30 pips.

```text
Pip value = 100,000 × 0.01 = 1,000 JPY
P/L = 30,000 JPY
```

Sau đó mới convert JPY sang account currency.

### Trường hợp (case / 사례) C

Account USD, rủi ro (risk / 위험) ngân sách (budget / 예산) 200 USD, stop 40 pips trên EUR/USD.

```text
Required pip value = 200 / 40 = 5 USD/pip
Base units ≈ 5 / 0.0001 = 50,000 EUR
```

Approximate kích thước (size / 크기) = 0.5 tiêu chuẩn (standard / 표준) lot theo convention 100.000 units.

> **Chuyển mạch:** Trong **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **29. Checklist trước khi sang leverage/margin** tiếp nhận điểm tựa từ **28. Bài tự kiểm tra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nối sang chương tiếp theo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Checklist trước khi sang leverage/margin

Bạn nên tự tính được:

- cơ sở (base / 기반) và quote currency;
- bid/ask và spread;
- pip kích thước (size / 크기);
- cơ sở (base / 기반) units từ lot;
- notional;
- P/L theo quote currency;
- conversion sang account currency;
- cross tỷ lệ (rate / 비율) bằng đơn vị (unit / 단위) phân tích (analysis / 분석);
- pip giá trị (value / 값);
- position kích thước (size / 크기) từ allowed mất mát (loss / 손실) và stop distance.

Nếu calculator là cách duy nhất bạn biết để có đáp án, nên luyện lại mechanics.

> **Chuyển mạch:** Ở chặng này của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, **Nối sang chương tiếp theo** tiếp nhận điểm tựa từ **29. Checklist trước khi sang leverage/margin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết liên quan** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nối sang chương tiếp theo

Pip và lot cho biết **position thay đổi P/L bao nhiêu khi price move**. Nhưng chúng chưa trả lời vì sao account có thể kiểm soát notional lớn hơn vốn, khi nào margin lời gọi (call / 호출)/stop-out xảy ra và mức leverage nào đang ẩn trong danh mục.

→ [03 — Leverage, margin and position sizing](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Quotes, pips, lots và cơ chế P/L trong Forex**, sau nội dung của **Nối sang chương tiếp theo**, **Liên kết liên quan** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết liên quan

- [01 — Market structure and instruments](./01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)
- [Trading & Forex master map](../00_MASTER_TRADING_FOREX_RISK.md)
- [Glossary, formulas and research conventions](../../00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md)

> **Bàn giao:** Sau **Liên kết liên quan**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
