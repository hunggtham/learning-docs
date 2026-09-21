# Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản

> Dữ liệu vĩ mô chỉ hữu ích khi nó làm thay đổi xác suất về tăng trưởng, lạm phát, chính sách, thanh khoản hoặc tín dụng. Mục tiêu của chương này là biến lịch kinh tế từ một danh sách headline thành một quy trình đọc dữ liệu có hệ thống.

Khung tổng quát:

```text
Mốc nền
→ Dự báo đồng thuận
→ Kỳ vọng đã phản ánh trong giá
→ Số liệu thực tế
→ Mức bất ngờ
→ Cấu phần
→ Hàm phản ứng chính sách
→ Yields / FX / Credit
→ Equities / Commodities
```

# Phần I — Cách đọc một release

## 1. Không đọc headline một cách cơ học

Thị trường không phản ứng đơn giản với “CPI cao”, “NFP tốt” hay “GDP mạnh”. Giá phản ứng với:

- số thực tế so với dự báo;
- revisions;
- cấu phần;
- positioning;
- ý nghĩa đối với chính sách tương lai.

Một dữ liệu tốt có thể khiến thị trường giảm nếu nó vẫn thấp hơn điều đã được price trước.

## 2. Baseline, consensus và market pricing

Ba khái niệm này khác nhau.

**Baseline:** nhận định riêng của bạn trước sự kiện.

**Consensus:** dự báo đồng thuận của economist hoặc analyst.

**Market pricing:** kỳ vọng được phản ánh trong futures, yield curve, options hoặc giá tài sản.

Ví dụ consensus dự báo cut 25bp nhưng futures đã phản ánh xác suất đáng kể của 50bp. Nếu ngân hàng trung ương chỉ cut 25bp, quyết định “đúng consensus” vẫn có thể bị xem là hawkish so với giá thị trường.

## 3. Surprise không chỉ là Actual - Forecast

Bất ngờ thống kê cần đọc cùng revisions và xu hướng.

```text
Headline Payroll +200k
nhưng
2 tháng trước bị revise -120k
```

khác hoàn toàn một bản +200k không có revision xấu.

Một release nên được đọc như chuỗi thời gian, không phải một điểm đơn lẻ.

# Phần II — Lạm phát

## 4. CPI

CPI đo thay đổi giá của một giỏ hàng tiêu dùng theo phương pháp thống kê cụ thể.

Cần tách:

```text
Headline
Core
Goods
Shelter
Services
Food
Energy
```

Core loại food và energy vì biến động cao nhưng không đồng nghĩa “lạm phát thật”.

## 5. MoM, YoY và base effect

YoY dễ bị ảnh hưởng bởi mức so sánh năm trước.

Do đó cần nhìn thêm MoM và xu hướng ngắn hạn.

Ví dụ annualized gần đúng:

```text
3-month annualized
≈ (1 + cumulative 3m change)^4 - 1
```

Tốc độ ngắn hạn nhiễu hơn nhưng có thể phát hiện điểm ngoặt sớm hơn YoY.

## 6. Shelter lag

Chỉ số nhà ở chính thức thường phản ứng chậm hơn giá thuê mới ngoài thị trường.

Do đó shelter CPI có thể còn cao ngay cả khi new-market rent đã giảm.

Khi đọc cần hiểu độ trễ của phương pháp đo.

## 7. Services ex housing

Một số analyst dùng dịch vụ ngoài nhà ở, đôi khi gọi không chính thức là “supercore”, để đánh giá áp lực dịch vụ.

Không có chỉ số thần kỳ. Điều quan trọng là biết ngân hàng trung ương đang chú ý chỉ số nào và vì sao.

## 8. PCE

PCE có trọng số và phương pháp khác CPI và thường là thước đo quan trọng trong phân tích Fed.

PCE không nên được đọc tách khỏi cấu phần. Một phần thông tin PCE còn có thể được suy ra trước từ CPI/PPI nên mức bất ngờ thị trường không phải lúc nào cũng lớn.

## 9. PPI và giá nhập khẩu

PPI và import prices giúp theo dõi áp lực giá ở upstream.

Nhưng pass-through tới CPI không 1:1 vì doanh nghiệp có thể:

- hấp thụ chi phí;
- tăng giá bán;
- cải thiện năng suất;
- đổi nhà cung cấp.

## 10. Kỳ vọng lạm phát

Kỳ vọng có thể đến từ survey hoặc market breakeven.

Breakeven gần đúng:

```text
Nominal Yield - Real Yield
```

nhưng nó chứa cả inflation risk premium và liquidity premium, nên không phải “dự báo lạm phát thuần”.

# Phần III — Thị trường lao động

## 11. Payrolls

Báo cáo việc làm Mỹ thường có establishment survey và household survey.

Nonfarm payrolls đến từ establishment side; unemployment rate chủ yếu từ household side.

Hai survey có thể phân kỳ trong một thời gian vì phương pháp khác nhau.

## 12. Unemployment rate

Tỷ lệ thất nghiệp tăng có thể do:

- việc làm giảm;
- hoặc nhiều người quay lại labor force nhanh hơn tốc độ tạo việc làm.

Hai trường hợp có ý nghĩa khác nhau.

## 13. Participation và underemployment

Nên xem thêm:

- participation rate;
- employment-population ratio;
- underemployment;
- hours worked.

Một tỷ lệ unemployment duy nhất không mô tả đầy đủ labor market.

## 14. Wage và productivity

Tăng lương không tự động tạo lạm phát nếu năng suất tăng tương ứng.

Một trực giác:

```text
Unit Labor Cost
≈ Wage Growth - Productivity Growth
```

Đây là cầu nối tốt hơn giữa dữ liệu lương và áp lực giá dịch vụ.

## 15. Jobless claims

Initial claims là chỉ báo tần suất cao về người mới xin trợ cấp thất nghiệp. Continuing claims cho biết tình trạng kéo dài.

Dữ liệu tuần rất nhiễu nên nên nhìn xu hướng nhiều tuần.

## 16. JOLTS

JOLTS gồm:

- job openings;
- hires;
- quits;
- layoffs.

Openings-to-unemployed cho biết nhu cầu lao động so với nguồn cung. Quits có thể phản ánh tự tin của người lao động.

# Phần IV — PMI và chu kỳ sản xuất

## 17. PMI/ISM là diffusion index

PMI trên 50 thường nghĩa hoạt động tăng so với kỳ trước; dưới 50 thường nghĩa giảm.

Nhưng cần đọc components:

- new orders;
- production;
- employment;
- prices paid;
- inventories;
- supplier deliveries.

## 18. New orders và inventories

Một quan hệ hữu ích:

```text
New Orders ↑ + Inventories thấp
→ Production có thể phục hồi
```

Ngược lại:

```text
New Orders ↓ + Inventories cao
→ Destocking Risk ↑
```

Điều này đặc biệt hữu ích với manufacturing, semiconductor và shipping.

# Phần V — Tiêu dùng và hộ gia đình

## 19. Retail sales

Retail sales là số danh nghĩa, vì vậy doanh thu tăng có thể chỉ do giá tăng chứ không phải volume.

Cần đọc cùng:

- inflation;
- real disposable income;
- savings;
- credit-card growth;
- delinquency.

## 20. Income, savings và credit

Chi tiêu có thể được tài trợ bằng:

- wage income;
- fiscal transfer;
- asset wealth;
- borrowing.

Tăng chi tiêu nhờ real income thường bền hơn tăng chi tiêu nhờ nợ tăng nhanh.

# Phần VI — Housing

## 21. Housing là sector nhạy lãi suất

Các dữ liệu quan trọng:

- mortgage rates;
- permits;
- starts;
- completions;
- new-home sales;
- existing-home sales;
- inventory;
- affordability.

Permits thường đi trước hoạt động xây dựng; starts cho biết activity hiện tại; completions ảnh hưởng nguồn cung.

## 22. Housing truyền policy sang nền kinh tế

Lãi suất mortgage ảnh hưởng:

```text
Affordability
→ Home Sales
→ Construction
→ Furnishing / Broker Activity
→ Household Wealth
```

# Phần VII — GDP

## 23. GDP theo chi tiêu

```text
GDP = C + I + G + (X - M)
```

Cần phân rã headline tăng trưởng thành:

- consumption;
- fixed investment;
- inventories;
- government;
- net exports.

## 24. Inventory có thể làm GDP nhiễu

Inventory build có thể đẩy GDP lên dù final demand yếu.

Imports trừ trong công thức GDP nhưng nhập khẩu mạnh đôi khi phản ánh domestic demand mạnh, nên không thể kết luận “imports cao là xấu”.

## 25. GDP và GDI

GDP đo từ phía sản lượng; GDI đo từ phía thu nhập. Về lý thuyết chúng phản ánh cùng nền kinh tế nhưng thực tế có measurement error.

Cần nhìn xu hướng và revisions.

# Phần VIII — Central bank meeting

## 26. Một cuộc họp có nhiều lớp

Cần đọc:

```text
Decision
Statement
Economic Projections
Rate Path / Dots
Vote Split
Press Conference
```

Không nên chỉ nhìn “hike/cut/hold”.

## 27. Hawkish cut và dovish hike

Một lần cut có thể hawkish nếu guidance cho thấy ít cut hơn về sau.

Một lần hike có thể dovish nếu ngân hàng trung ương ám chỉ chu kỳ tăng đã gần kết thúc.

## 28. Current rate và expected path

Tài sản chiết khấu lãi suất tương lai, không chỉ policy rate hôm nay.

2Y yield và OIS/futures thường giúp đọc repricing ở đầu đường cong.

# Phần IX — Bond market

## 29. Nominal yield, real yield và breakeven

Nominal yield có thể thay đổi do:

- expected policy;
- expected inflation;
- real growth;
- term premium.

Real yield đặc biệt quan trọng với định giá tài sản duration dài.

## 30. 2Y và 10Y

2Y nhạy với expected policy gần hạn.

10Y phản ánh nhiều hơn:

- long-run growth;
- inflation;
- term premium;
- Treasury supply.

Một CPI nóng làm 2Y +15bp, 10Y +5bp khác hẳn một fiscal shock làm 10Y +20bp nhưng 2Y gần như không đổi.

## 31. Yield curve

Đường cong không chỉ được đọc qua độ dốc mà còn cần biết toàn bộ yield đang tăng hay giảm.

```text
Bull Steepening
Bull Flattening
Bear Steepening
Bear Flattening
```

Tên gọi chỉ hữu ích khi hiểu nguyên nhân kinh tế phía sau.

## 32. Term premium

Phần bù kỳ hạn (term premium) là phần bù cho việc nắm duration dài trong bất định.

Nó có thể tăng do:

- fiscal issuance;
- inflation uncertainty;
- QT;
- giảm nhu cầu từ người mua lớn.

Long-end yield tăng vì term premium có thể thắt financial conditions dù Fed không hawkish hơn.

# Phần X — Credit

## 33. Credit spread

Spread tăng có thể phản ánh:

- default risk;
- liquidity risk;
- risk aversion;
- technical selling.

Government yield giảm nhưng high-yield spread tăng mạnh thường là tín hiệu tăng trưởng/tín dụng xấu đi.

## 34. Refinancing calendar

Tác động lãi suất thường có độ trễ vì nợ cố định chỉ repricing khi đáo hạn.

Cần xem maturity wall chứ không chỉ policy rate.

## 35. Bank lending standards

Khảo sát lending standards giúp nối policy tới real economy.

Nếu bank tightening và loan demand cùng giảm, credit impulse có thể yếu ngay cả khi central bank đã dừng hike.

# Phần XI — Financial conditions

## 36. Financial conditions rộng hơn policy rate

Điều kiện tài chính gồm:

- rates;
- credit spreads;
- equity prices;
- FX;
- lending standards;
- property prices.

Hai nền kinh tế cùng policy rate vẫn có thể có financial conditions rất khác.

# Phần XII — FX

## 37. FX luôn là tương đối

Một đồng tiền mạnh hay yếu phải so với đồng còn lại.

Khung cơ bản:

```text
Relative Rates
+ Relative Growth
+ External Balance
+ Carry
+ Risk Flow
+ Positioning
```

## 38. Carry và funding currency

Carry tốt khi volatility thấp nhưng có thể đảo chiều mạnh trong risk-off.

Funding currency đôi khi tăng trong deleveraging dù lãi suất thấp.

# Phần XIII — Commodities

## 39. Oil: demand shock và supply shock

Dầu tăng vì demand mạnh có thể đi cùng growth tốt.

Dầu tăng vì geopolitics hoặc supply disruption có thể tạo:

```text
Inflation ↑
Growth ↓
```

và mang tính stagflationary.

## 40. Industrial metals

Copper và metals chịu ảnh hưởng của:

- China;
- manufacturing;
- inventories;
- mine supply;
- positioning.

Giá hàng hóa vừa là chỉ báo kinh tế vừa là input cost.

## 41. Gold

Các biến chính:

- real yields;
- USD;
- central-bank demand;
- geopolitics;
- confidence in policy regime.

Không dùng quy tắc cơ học “inflation ↑ → gold ↑”.

# Phần XIV — Lỗi đọc dữ liệu phổ biến

## 42. Revision

Dữ liệu kinh tế thường được sửa đổi.

Không nên xây thesis lớn trên một print đầu tiên nếu series vốn có revision lớn.

## 43. Seasonality

Seasonal adjustment không hoàn hảo. Các kỳ nghỉ, thời tiết hoặc lịch Tết có thể làm dữ liệu méo.

## 44. Base effect

Khi YoY thay đổi mạnh, luôn kiểm tra mốc so sánh năm trước và momentum gần đây.

## 45. Measurement error

Dữ liệu survey là ước tính, không phải đo toàn bộ nền kinh tế với độ chính xác tuyệt đối.

Nên tìm xác nhận từ nhiều series độc lập.

# Phần XV — Positioning và phản hồi giá

## 46. Positioning

Tin xấu có thể làm thị trường tăng nếu nhà đầu tư đã còn bi quan hơn trước release.

Tin tốt có thể làm thị trường giảm nếu positioning quá crowded long.

## 47. Reflexivity

Giá tài sản có thể quay lại ảnh hưởng economy:

```text
Equity / Property ↑
→ Wealth / Collateral ↑
→ Spending / Credit ↑
```

và chiều ngược lại.

# Phần XVI — Regime matrix

## 48. Growth và inflation surprise

Một ma trận đơn giản:

```text
Growth ↑ / Inflation ↓
→ Goldilocks-like

Growth ↑ / Inflation ↑
→ Overheating risk

Growth ↓ / Inflation ↓
→ Easing / Deflationary risk

Growth ↓ / Inflation ↑
→ Stagflationary risk
```

Credit và liquidity có thể làm ma trận này mất tác dụng nếu hệ thống tài chính đang stress.

# Phần XVII — Quy trình đọc một sự kiện

## 49. Trước release

Ghi lại:

```text
Consensus
Prior / Revision Risk
Market Pricing
Yield Curve
FX
Positioning
Option Implied Move
Your Baseline
```

## 50. Ngay sau release

Đừng chỉ nhìn headline. Kiểm tra:

```text
Actual vs Consensus
Composition
Revisions
2Y
10Y
Real Yield
USD
Credit Spread
Equity Breadth
```

## 51. Sau vài giờ / cuối ngày

Hỏi:

```text
Market đang diễn giải release thành growth shock,
inflation shock hay policy shock?
```

Theo dõi xem phản ứng ban đầu có được xác nhận bởi nhiều tài sản hay không.

## 52. Sau vài ngày

Kiểm tra:

- analyst revisions;
- policy communication;
- credit conditions;
- sector performance;
- whether positioning reversed.

## 53. Event note chuẩn

```text
Event:
Consensus:
Actual:
Revision:
Composition:
What was priced:
Reaction function change:
2Y / 10Y / Real Yield:
FX:
Credit:
Equities:
Commodities:
My interpretation:
What would invalidate it:
```

# Phần XVIII — Chuỗi nhân quả cốt lõi

## 54. Inflation event

```text
CPI Surprise
→ Persistence Assessment
→ Reaction Function
→ Expected Policy Path
→ 2Y / Real Yield
→ USD
→ Equity Multiple / Credit
```

## 55. Growth event

```text
Growth Surprise
→ Earnings Expectation
→ Policy Expectation
→ Yields / FX
→ Cyclicals vs Defensives
```

## 56. Credit event

```text
Funding Stress
→ Spread Widening
→ Lending Tightening
→ Growth Revision
→ Policy Response
```

## Kết luận

Đọc macro data tốt không phải đoán headline. Mục tiêu là hiểu **thông tin mới đã thay đổi phân phối xác suất như thế nào** và thị trường đang phản ánh sự thay đổi đó qua bond, FX, credit và equity ra sao.

Chuỗi quan trọng nhất cần ghi nhớ là:

```text
Actual
→ Surprise
→ Composition
→ Reaction Function
→ Yields / FX / Credit
→ Earnings / Valuation
→ Asset Reaction
```
