# Đầu tư xuyên biên giới: tiền tệ, thuế, wrapper và khả năng tiếp cận thị trường

> Khi đầu tư tài sản nước ngoài, lợi nhuận không chỉ đến từ underlying. Người đầu tư còn chịu ảnh hưởng của **tỷ giá, cấu trúc pháp lý của sản phẩm, custody, settlement, thuế, market access và khả năng chuyển tiền**. Một tài sản tốt nhưng implementation kém vẫn có thể tạo kết quả xấu.

> **Dữ liệu động:** thuế suất, ưu đãi tài khoản, withholding, settlement cycle, foreign room, market-access rule và broker support phải được kiểm tra lại theo nguồn chính thức tại thời điểm đầu tư.

# Phần I — Bốn lớp tiền tệ

## 1. Trading currency

Trading currency là đồng tiền dùng để báo giá và giao dịch sản phẩm.

ETF niêm yết tại Hàn Quốc có thể giao dịch bằng KRW.

## 2. Underlying economic currency

Underlying economic currency là đồng tiền gắn với tài sản hoặc dòng tiền cơ bản.

Một ETF KRW theo S&P 500 vẫn có exposure kinh tế lớn với USD nếu không hedge.

## 3. Reporting / home currency

Đây là đồng tiền người đầu tư dùng để đo wealth.

Với người sống và chi tiêu chủ yếu tại Hàn Quốc, KRW có thể là home/reporting currency trong nhiều bài toán.

## 4. Liability currency

Liability currency là đồng tiền của các nghĩa vụ tương lai như:

- tiền thuê nhà;
- mua nhà;
- học phí;
- trả nợ;
- chi tiêu hưu trí.

Currency allocation nên liên hệ với liability, không chỉ return expectation.

# Phần II — Phân rã lợi nhuận FX

## 5. Công thức home-currency return

```text
Home Return
= (1 + Local Asset Return)
× (1 + FX Return)
- 1
```

Ví dụ cổ phiếu tăng 10% bằng local currency nhưng local currency giảm mạnh so home currency thì lợi nhuận thực nhận có thể thấp hơn nhiều.

## 6. Listing currency không xóa FX exposure

Mua một ETF global bằng KRW không tự động loại USD exposure.

Cần kiểm tra underlying và hedge policy.

# Phần III — Natural hedge

## 7. Natural hedge là gì?

Natural hedge xuất hiện khi asset và liability có cùng currency exposure.

Ví dụ có future USD expense thì sở hữu một phần USD asset có thể giảm mismatch.

## 8. Human capital

Thu nhập lao động cũng là một dạng economic exposure.

Người nhận lương KRW đã có “human capital” gắn với Korea; portfolio có thể cần cân nhắc concentration này.

# Phần IV — Currency hedging

## 9. Strategic hedge

Strategic hedge là tỷ lệ hedge dài hạn tương đối ổn định.

Mục tiêu thường là giảm volatility hoặc liability mismatch, không phải dự đoán FX ngắn hạn.

## 10. Dynamic hedge

Dynamic hedge thay tỷ lệ theo valuation, rates hoặc regime.

Nó phức tạp hơn và có nguy cơ market timing sai.

## 11. Hedge không miễn phí

FX hedge có thể chịu:

- forward points;
- interest-rate differential;
- spread;
- roll cost;
- cross-currency basis.

## 12. Hedge ratio

Không nhất thiết hedge 0% hoặc 100%.

Tỷ lệ hợp lý phụ thuộc mục tiêu, horizon, liability và volatility tolerance.

# Phần V — Forward points và basis

## 13. Forward points

Forward FX phản ánh chênh lệch lãi suất giữa hai đồng tiền theo nguyên lý covered interest parity, cùng các yếu tố thị trường khác.

Hedge một currency có lãi suất cao/thấp có thể tạo carry khác nhau.

## 14. Cross-currency basis

Basis phản ánh mất cân bằng funding và demand trong swap market.

Trong stress, cost hedge USD có thể tăng ngay cả khi spot không đổi nhiều.

# Phần VI — Wrapper

## 15. Wrapper là lớp bao quanh underlying

Một exposure có thể được sở hữu qua:

- direct stock;
- ETF;
- mutual fund;
- ETN;
- depositary receipt;
- derivative.

Mỗi wrapper có legal claim và risk khác nhau.

## 16. ETF

ETF thường nắm basket hoặc replicate index.

Cần xem:

- domicile;
- replication;
- securities lending;
- tracking difference;
- tax;
- FX hedge.

## 17. ETN

ETN thường là unsecured debt claim đối với issuer gắn payoff với index.

Ngoài market exposure còn có issuer credit risk.

## 18. Depositary receipt

Depositary receipt đại diện quyền lợi liên quan cổ phiếu ở thị trường khác nhưng thêm lớp depositary/custody và có thể có liquidity khác underlying.

# Phần VII — Domicile

## 19. Domicile của fund quan trọng

Fund domicile có thể ảnh hưởng:

- withholding;
- treaty;
- legal protection;
- reporting;
- estate/tax treatment.

Không nên chỉ nhìn ticker.

## 20. Local wrapper vs direct foreign asset

Mua sản phẩm niêm yết tại Korea có thể đơn giản hơn về broker/settlement nhưng không nhất thiết tối ưu về fee, tracking hoặc tax.

Direct ownership có thể cho access tốt hơn nhưng thêm operational burden.

# Phần VIII — Custody và beneficial ownership

## 21. Custodian

Custodian giữ hoặc ghi nhận securities theo legal structure.

## 22. Beneficial owner

Người đầu tư có thể là beneficial owner trong khi legal title được giữ qua nominee/custodian.

Cần hiểu quyền:

- voting;
- dividend;
- corporate action;
- asset segregation.

## 23. Broker legal entity

Một brand có thể có nhiều legal entity ở các quốc gia khác nhau.

Protection phụ thuộc entity mà account ký hợp đồng, không chỉ tên thương hiệu.

# Phần IX — Settlement và time-zone risk

## 24. Settlement mismatch

Hai market có thể có settlement cycle khác nhau.

Bán ở một market để mua market khác có thể tạo cash timing mismatch.

## 25. Holiday mismatch

Korea nghỉ nhưng Mỹ mở, hoặc Việt Nam nghỉ khi market khác mở, có thể làm hedge/rebalance không đồng thời.

## 26. Time zone

Price của local wrapper có thể giao dịch khi underlying cash market đang đóng.

Khi đó premium/discount và price discovery có thể biến động hơn.

# Phần X — Corporate actions

## 27. Dividend

Cross-border dividend có thể chịu withholding trước khi tới account.

## 28. Rights / tender / merger

Broker hoặc custodian có thể có deadline xử lý sớm hơn official market deadline.

## 29. Fractional / odd-lot issue

Corporate action có thể tạo phần lẻ và cách xử lý khác nhau theo broker.

# Phần XI — Korea market access

## 30. Local listed products

Nhà đầu tư tại Korea có thể tiếp cận nhiều exposure global qua local ETF/ETN.

Cần nhìn xuyên wrapper tới underlying.

## 31. Direct foreign trading

Broker Hàn Quốc có thể hỗ trợ direct overseas stocks nhưng market availability, FX conversion và tax reporting phụ thuộc dịch vụ hiện hành.

## 32. ISA và tax wrappers

Các tài khoản ưu đãi thuế có rule và limit có thể thay đổi.

Không hard-code con số vào tài liệu dài hạn; luôn kiểm tra cơ quan/broker chính thức.

# Phần XII — Vietnam market access

## 33. Foreign ownership

Một số công ty/ngành có giới hạn sở hữu nước ngoài.

Khi foreign room gần đầy, pricing/liquidity có thể khác bình thường.

## 34. Free float

Market cap lớn nhưng free float thấp có thể làm liquidity thực tế nhỏ hơn tưởng tượng.

## 35. Price limit

Daily price band có thể kéo dài exit time trong stress.

## 36. Settlement / prefunding / access rules

Cơ chế settlement và yêu cầu funding có thể thay đổi theo cải cách thị trường.

Khi giao dịch thật phải kiểm tra VSDC/HOSE/HNX/SSC và broker hiện hành.

# Phần XIII — Capital controls và repatriation

## 37. Convertibility

Không phải mọi currency đều hoàn toàn tự do như nhau.

Cần hiểu khả năng chuyển đổi và chuyển tiền ra/vào theo legal framework.

## 38. Repatriation

Profit trên paper chỉ có giá trị khi cash có thể được chuyển về nơi cần sử dụng trong khuôn khổ pháp lý.

## 39. Documentation

Cross-border transfer có thể yêu cầu chứng từ nguồn vốn, thuế hoặc mục đích giao dịch.

# Phần XIV — Tax framework

## 40. Tax residency

Thuế thường phụ thuộc residency, loại tài sản, account và jurisdiction.

Không suy luận chỉ từ quốc tịch.

## 41. Withholding tax

Dividend/interest có thể bị khấu trừ tại nguồn trước khi tới investor.

Treaty có thể ảnh hưởng mức cuối cùng.

## 42. Capital gains

Treatment khác nhau giữa thị trường, loại tài sản và account.

## 43. Tax wrapper

Một wrapper có lợi thế thuế nhưng có thể có limit, lock-up hoặc eligible products riêng.

## 44. Không tối ưu thuế bằng thông tin cũ

Tax rules thay đổi. Với quyết định thật, cần xác minh professional/official source phù hợp.

# Phần XV — Full cost stack

## 45. Chi phí không chỉ là commission

```text
Commission
+ Spread
+ FX Conversion
+ Custody
+ Fund Fee
+ Tracking Difference
+ Tax
+ Financing
+ Withdrawal / Transfer Cost
```

## 46. FX conversion cost

Broker có thể dùng spread hoặc fee khi đổi KRW/USD/VND.

Cost nhỏ nhưng lặp nhiều lần có thể đáng kể.

## 47. Dividend conversion

Dividend ngoại tệ có thể tự động convert theo rate của broker, tạo thêm cost.

# Phần XVI — Country, currency và factor buckets

## 48. Đừng chỉ phân bổ theo country label

Korean semiconductor có thể chứa:

- Korea beta;
- global tech beta;
- USD/KRW;
- AI capex;
- memory cycle.

## 49. Vietnam bank/property exposure

Có thể chứa:

- domestic credit;
- property collateral;
- VND;
- retail liquidity;
- regulation.

## 50. Look-through

Portfolio nên nhìn xuyên ETF/fund để tránh mua nhiều wrapper nhưng lặp cùng underlying factor.

# Phần XVII — Liability-driven allocation

## 51. Asset currency nên liên hệ spending currency

Nếu future spending chủ yếu bằng KRW, toàn portfolio 100% unhedged foreign currency có thể tạo mismatch lớn.

## 52. Short-horizon liability

Nghĩa vụ gần nên ưu tiên liquidity và currency match hơn expected return cao.

# Phần XVIII — Provider concentration

## 53. Broker concentration

Giữ toàn bộ tài sản tại một broker tạo operational/counterparty concentration.

## 54. Fund provider concentration

Không phải lúc nào cũng xấu nhưng cần hiểu custody, legal segregation và issuer risk với ETN/structured product.

# Phần XIX — Stress test kết hợp

## 55. Cross-border stress

Ví dụ:

```text
Global Equity -20%
USD/KRW +10%
VND yếu
Credit Spread ↑
Market Liquidity ↓
```

Phải tính cả asset move và FX move.

## 56. Reverse stress

Hỏi:

```text
Điều gì có thể khiến tôi không thể bán/chuyển tiền đúng lúc?
```

Có thể là market halt, price limit, holiday mismatch, broker issue hoặc capital-control constraint.

# Phần XX — Operational resilience

## 57. Record keeping

Lưu:

- trade confirmations;
- cost basis;
- FX conversion;
- dividend;
- tax documents;
- corporate actions.

## 58. Beneficiary và succession

Cross-border asset còn liên quan inheritance/succession rules. Với tài sản lớn cần tư vấn pháp lý/thuế chuyên môn theo jurisdiction.

# Phần XXI — Cross-border IPS

## 59. Investment Policy Statement

Một IPS xuyên biên giới nên ghi:

```text
Home Currency
Liability Currencies
Target Country Exposure
FX Hedge Policy
Allowed Wrappers
Liquidity Requirement
Broker / Custody Limits
Tax Verification Process
Rebalancing Rule
```

## 60. Product checklist

Trước khi mua:

```text
Underlying là gì?
Currency exposure nào?
Wrapper/domicile?
Legal claim?
Custody?
Settlement?
Liquidity?
Tax?
Total cost?
How to exit/repatriate?
```

## Kết luận

Cross-border investing không dừng ở việc tìm một tài sản có expected return tốt.

Chuỗi đầy đủ là:

```text
Underlying Economics
→ Currency
→ Wrapper / Domicile
→ Legal Claim
→ Custody / Settlement
→ Tax / Cost
→ Market Access
→ Repatriation
→ Liability Match
```

Một implementation tốt phải bảo đảm exposure mà investor nghĩ mình đang sở hữu cũng là exposure thật về **kinh tế, pháp lý và dòng tiền**.
