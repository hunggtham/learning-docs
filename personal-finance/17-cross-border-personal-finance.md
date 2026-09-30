# 17 — Tài chính cá nhân xuyên biên giới (Cross-Border Personal Finance / 국경간 개인재무)

## Định vị

[16 — Korea–Vietnam Practical Map](./16-korea-vietnam-practical-map.md) cho biết concept nào có thể dùng chung và rule nào phải kiểm tra theo từng jurisdiction. Chapter này xử lý bước khó hơn: một household có thể **sống ở một nước, nhận thu nhập bằng một đồng tiền, gửi tiền sang nước khác, sở hữu tài sản ở nhiều nơi và có nghĩa vụ dài hạn ở nhiều hệ thống**.

Đây không phải Forex trading. Câu hỏi trung tâm là: **làm sao để một balance sheet đa quốc gia vẫn có đủ liquidity, đúng currency, đúng nơi và đúng thời điểm để đáp ứng nghĩa vụ?**

## Household có thể có nhiều “đồng tiền” cùng lúc

Một người có thể nhận lương bằng KRW nhưng có nghĩa vụ hỗ trợ gia đình bằng VND, đầu tư bằng USD và có retirement benefit gắn với KRW. Nếu chỉ cộng mọi asset sau khi đổi sang một currency tại tỷ giá hôm nay, ta có net worth snapshot nhưng chưa thấy risk.

Cần phân biệt:

```text
currency of income
currency of daily spending
currency of debt
currency of family obligations
currency of emergency needs
currency of long-term assets
```

Một household không “long KRW” hay “short VND” theo nghĩa trading đơn giản; nó có một tập cash flow tương lai bằng nhiều đồng tiền.

## Đồng tiền chức năng của household

Có thể dùng khái niệm thực hành **đồng tiền chức năng (functional currency / 기능통화)** để chỉ currency mà phần lớn nghĩa vụ sống gần hạn được định giá. Đây không phải định nghĩa kế toán pháp lý; nó là mental model cho personal finance.

Ví dụ, nếu rent, food, transport, insurance và debt payment đều bằng KRW thì KRW thường là operational currency, ngay cả khi household có tài sản lớn bằng VND hoặc USD.

Điều này dẫn tới nguyên tắc:

```text
near-term obligation
→ nên được backed chủ yếu bởi liquidity cùng currency
```

Không phải vì FX luôn biến động xấu, mà vì emergency fund không nên phụ thuộc vào việc tỷ giá và transfer rail đều thuận lợi đúng ngày cần thanh toán.

## Tách bốn bucket currency

Một cách đơn giản để tránh trộn mục đích:

### 1. Operating cash

Tiền vận hành (operating cash / 운영자금) dùng cho chi tiêu ngắn hạn và hóa đơn thường xuyên. Currency nên gần với nơi sống và payment rail thực tế.

### 2. Emergency liquidity

Thanh khoản khẩn cấp (emergency liquidity / 비상 유동성) cần ở nơi có thể truy cập nhanh khi mất việc, cần di chuyển hoặc account chính gặp sự cố. [12 — Emergency Fund](./12-emergency-fund.md) giải thích sizing; cross-border layer thêm câu hỏi **tiền nằm ở đâu và mất bao lâu để dùng được**.

### 3. Known future obligations

Nghĩa vụ tương lai đã biết có thể gồm học phí, hỗ trợ gia đình, mua nhà, thuế hoặc khoản trả nợ. Nếu amount và date tương đối chắc chắn, để toàn bộ funding ở currency khác có thể tạo FX mismatch không cần thiết.

### 4. Long-term capital

Vốn dài hạn (long-term capital / 장기자본) mới là phần có thể chịu biến động currency/market lớn hơn theo một investment policy. Asset allocation và hedge mechanics thuộc [Investing](../investing/README.md), không thuộc chapter này.

## FX exposure ở cấp household

Rủi ro tỷ giá (foreign-exchange risk / 환위험) xuất hiện khi giá trị của income/asset thay đổi so với currency của nghĩa vụ.

Ví dụ khái niệm:

```text
salary: KRW
family support obligation: VND
```

Nếu VND mạnh lên so với KRW, cùng nghĩa vụ VND đòi hỏi nhiều KRW hơn. Ngược lại, nếu KRW mạnh lên, burden giảm. Đây là **household exposure**, không phải trading thesis.

Một câu hỏi tốt hơn “KRW hay VND sẽ tăng?” là:

```text
Nếu FX đi bất lợi 10–20%, nghĩa vụ thiết yếu có còn funded không?
```

Nếu câu trả lời là không, household có currency mismatch đáng kể.

## Đừng dùng Forex trading để sửa một vấn đề budgeting

Forex trading, derivative hedge hoặc speculative position có risk, margin và operational complexity riêng. Với household, lớp đầu tiên thường đơn giản hơn:

```text
match near-term assets with near-term liabilities
→ diversify timing of transfers
→ avoid excessive concentration in one inaccessible account
→ only then consider explicit hedge if scale/need justifies it
```

Nếu cần forward, futures, options, NDF, basis hoặc execution, owner là [`investing/05_trading_derivatives/forex/`](../investing/05_trading_derivatives/forex/README.md).

## Remittance cost không chỉ là transfer fee

Chi phí chuyển tiền quốc tế (remittance cost / 해외송금 비용) có thể gồm:

```text
explicit transfer fee
+ FX spread
+ intermediary/correspondent fee
+ receiving fee
+ timing/slippage
+ opportunity cost of delayed funds
```

Một dịch vụ quảng cáo “fee 0” vẫn có thể kiếm tiền qua spread. Vì vậy khi so sánh transfer route, cần nhìn **recipient receives how much**, không chỉ nhìn fee line.

Với khoản nhỏ gửi thường xuyên, convenience và speed có thể quan trọng. Với khoản lớn, spread nhỏ cũng trở thành số tiền đáng kể. Không có một rail tốt nhất cho mọi amount/currency/country.

## Transferability là thuộc tính của asset

Một asset có giá trị nhưng khó chuyển quốc gia không tương đương cash global. Cross-border balance sheet nên thêm các field:

```text
asset
market value
currency
country / institution
liquidity time
transferability
tax wrapper / restriction
purpose
```

Ví dụ, retirement account có thể có market value cao nhưng withdrawal bị hạn chế; housing equity có thể lớn nhưng mất nhiều tháng để liquidate; deposit ở một nước có thể không thanh toán hóa đơn ở nước khác ngay lập tức.

Vì vậy:

```text
Net worth ≠ globally usable liquidity
```

## Banking friction: KYC/AML và residency

Chuyển tiền quốc tế đi qua nhiều lớp compliance. Ngân hàng hoặc payment provider có thể yêu cầu chứng minh identity, source of funds, purpose of transfer, tax/residency information hoặc documentation khác theo luật và policy.

Đừng coi mọi request giấy tờ là “lỗi”. Nhưng cũng không nên tự suy ra rằng một transfer được app cho phép thì chắc chắn đã giải quyết mọi tax/reporting obligation. Payment execution và legal/tax compliance là hai lớp khác nhau.

Với người sống ở Hàn Quốc, các procedure cụ thể về account/credit thuộc [`korea_law_civic_life/08_banking_credit_and_financial_consumer.md`](../korea_law_civic_life/08_banking_credit_and_financial_consumer.md). Với Việt Nam, kiểm tra quy định và hướng dẫn chính thức của cơ quan/ngân hàng liên quan tại thời điểm giao dịch.

## Tax residency không đồng nghĩa citizenship hay visa

Tình trạng cư trú thuế (tax residency / 세법상 거주자) là khái niệm pháp lý xác định theo luật thuế và facts áp dụng; nó không nên được suy chỉ từ quốc tịch hoặc tên visa.

Cross-border household cần tách ít nhất:

```text
immigration status
≠ tax residency
≠ bank account residency classification
≠ social-insurance status
```

Chúng có thể ảnh hưởng nhau nhưng không phải một biến duy nhất.

Khi có income, asset sale, interest, dividend, rental income hoặc pension ở hai nước, tax scope và treaty treatment có thể trở nên phức tạp. [08 — Taxes](./08-taxes.md) chỉ cho mental model; con số/rule thực tế phải kiểm tra nguồn thuế chính thức hoặc professional phù hợp.

## Pension và social insurance: portability là câu hỏi riêng

Một người làm việc nhiều năm ở hơn một quốc gia cần hỏi không chỉ “đã đóng bao nhiêu?” mà còn:

```text
quyền lợi có vest chưa?
contribution period có cộng nối được không?
có social-security agreement không?
refund/lump-sum có áp dụng cho mình không?
benefit có thể nhận khi sống ở nước khác không?
currency/tax khi nhận thế nào?
```

Các answers phụ thuộc country pair, nationality/status, thời gian và luật hiện hành. Đối với Hàn Quốc, kiểm tra National Pension Service (`국민연금공단`). Đối với Việt Nam, kiểm tra Bảo hiểm xã hội Việt Nam và văn bản liên quan.

Không hard-code danh sách quốc gia đủ điều kiện refund trong chapter vì đây là data time-sensitive.

## Emergency plan xuyên biên giới

Một emergency plan tốt cần trả lời cả **money** và **access**:

```text
Nếu mất điện thoại ở nước đang sống, tôi truy cập tiền bằng cách nào?
Nếu account chính bị freeze, account backup ở đâu?
Nếu cần bay về nước trong 24 giờ, currency nào sẵn dùng?
Nếu transfer quốc tế delay 3–5 ngày, rent/debt payment có bị trễ không?
Nếu một family member cần tiền khẩn cấp, rail nào đã được verify?
```

Đây là nơi [13 — Financial Scams](./13-financial-scams.md), [12 — Emergency Fund](./12-emergency-fund.md) và [15 — Financial Resilience](./15-financial-resilience.md) hội tụ.

## Family support là một liability mềm nhưng thật

Nhiều household xuyên biên giới có hỗ trợ cha mẹ, con cái hoặc người thân. Về accounting, đây có thể không phải legal liability; về cash-flow planning, nó vẫn là recurring obligation nếu household xem đó là commitment thực tế.

Nên đưa vào plan bằng amount/range thay vì coi là “chi tiêu bất ngờ” mỗi tháng:

```text
base support
+ seasonal/known needs
+ emergency family reserve
```

Điều này làm rõ investable surplus và tránh việc investment plan phải liên tục bị phá để đáp ứng một nghĩa vụ có thể dự báo.

## Cross-border balance-sheet review

Mỗi quý hoặc khi đổi việc/chuyển nước, review:

```text
1. Assets/liabilities theo country và currency.
2. 3–12 tháng obligations theo currency.
3. Emergency liquidity có đúng nơi/currency không.
4. Debt nào có variable rate hoặc FX exposure.
5. Transfer routes còn hoạt động và cost ra sao.
6. Tax/residency/social-insurance facts có thay đổi không.
7. Account access/recovery còn dùng được không.
8. Investable surplus thực sự còn bao nhiêu sau cross-border obligations.
```

Mục tiêu không phải hedge mọi FX fluctuation. Mục tiêu là không để một biến động hoặc friction thông thường phá hỏng payment capacity.

## Khi nào chuyển sang Investing?

Sau khi map household exposure, phần vốn dài hạn có thể được chuyển sang Investing để trả lời:

```text
portfolio nên giữ currency exposure nào?
hedged hay unhedged asset hợp lý trong mục tiêu nào?
foreign stocks/bonds tạo risk gì?
Forex hedge cost và instrument mechanics ra sao?
```

Personal Finance xác định **risk cần quản lý vì đời sống**; Investing quyết định **risk nào đáng giữ để nhận expected return**. Không nên đảo hai bước này.

## Kết luận

Cross-border personal finance biến một balance sheet một-country thành hệ thống gồm **currency + jurisdiction + transferability + timing**. Một tài sản chỉ thực sự hữu ích cho nghĩa vụ khi nó có thể được chuyển thành purchasing power đúng nơi, đúng currency và đúng thời điểm với friction chấp nhận được.

Đây là extension cuối của core route hiện tại. Sau chapter này, hãy dùng [Coverage Audit](./COVERAGE_AUDIT.md) để thấy phần nào đã đủ sâu, phần nào time-sensitive và những expansion nào chỉ nên mở khi có nhu cầu rõ thay vì tiếp tục tăng file không giới hạn.

### Nguồn/owner để kiểm tra hiện hành

- National Pension Service: https://www.nps.or.kr/
- Bảo hiểm xã hội Việt Nam: https://baohiemxahoi.gov.vn/
- Financial Supervisory Service: https://www.fss.or.kr/
- Ngân hàng Nhà nước Việt Nam: https://www.sbv.gov.vn/
- OECD, Financial education: https://www.oecd.org/en/topics/financial-education.html
