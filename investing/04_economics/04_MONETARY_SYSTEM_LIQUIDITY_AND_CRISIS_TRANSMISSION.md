# Hệ thống tiền tệ, thanh khoản và cơ chế truyền dẫn khủng hoảng

> Chương này đi sâu vào “đường ống” của hệ thống tài chính: tiền gửi, dự trữ, repo, collateral, dealer balance sheet, quỹ thị trường tiền tệ, USD funding và các cơ chế làm một cú sốc nhỏ biến thành stress lớn. Mục tiêu là phân biệt rõ **tiền**, **thanh khoản**, **vốn**, **tài sản bảo đảm** và **khả năng trả nợ**.

# Phần I — Các lớp tiền khác nhau

## 1. Tiền mặt, tiền gửi và dự trữ

Ba khái niệm này không giống nhau.

**Tiền mặt (cash/banknotes):** tiền giấy do ngân hàng trung ương phát hành.

**Tiền gửi ngân hàng (bank deposits):** nghĩa vụ của ngân hàng thương mại với khách hàng.

**Dự trữ ngân hàng (bank reserves):** tài sản của ngân hàng thương mại tại ngân hàng trung ương, chủ yếu dùng cho thanh toán giữa các ngân hàng và đáp ứng yêu cầu hệ thống.

Nhà đầu tư cá nhân không trực tiếp giữ reserves.

## 2. Khi ngân hàng cho vay

Khi ngân hàng cấp một khoản vay, nó thường đồng thời tạo:

```text
Asset: Loan
Liability: Deposit
```

Do đó tín dụng ngân hàng có thể mở rộng sức mua trong nền kinh tế mà không cần ngân hàng trung ương in một lượng tiền giấy tương ứng.

## 3. Bảng cân đối ngân hàng trung ương

Một bảng cân đối đơn giản có thể gồm:

```text
Assets:
Government Bonds
Loans / Facilities
FX Reserves

Liabilities:
Bank Reserves
Currency in Circulation
Government Deposits
```

QE, QT hoặc lending facility thay đổi các dòng này theo cơ chế khác nhau.

# Phần II — Hệ thống lãi suất ngắn hạn

## 4. Policy rate không phải mọi lãi suất

Ngân hàng trung ương kiểm soát hoặc định hướng một lãi suất ngắn hạn mục tiêu.

Sau đó chính sách truyền qua:

```text
Policy Rate
→ Money-Market Rates
→ Bank Funding
→ Bond Yields
→ Mortgage / Corporate Rates
```

## 5. Floor system và corridor system

Trong **hệ thống sàn (floor system)**, lượng reserves thường dồi dào và lãi trả trên reserves giúp đặt sàn cho lãi suất ngắn hạn.

Trong **hệ thống hành lang (corridor system)**, lãi vay và lãi gửi tại ngân hàng trung ương tạo vùng mục tiêu để thị trường tiền tệ giao dịch bên trong.

Không cần học thuộc từng tên chương trình; điều quan trọng là hiểu ngân hàng trung ương điều khiển giá của funding ngắn hạn như thế nào.

# Phần III — Repo và collateral

## 6. Repo là gì?

Repo về kinh tế gần với khoản vay có bảo đảm.

```text
Borrower giao collateral
→ nhận cash
→ sau đó mua lại collateral với giá cao hơn
```

Chênh lệch giá phản ánh lãi repo.

## 7. Collateral

Tài sản bảo đảm (collateral) không chỉ giảm rủi ro tín dụng. Nó còn quyết định khả năng một tổ chức có thể vay bao nhiêu.

Tài sản có thanh khoản và chất lượng cao thường cho phép vay với haircut thấp hơn.

## 8. Haircut

Haircut là phần giá trị collateral không được tính khi cho vay.

Ví dụ:

```text
Collateral value = 100
Haircut = 10%
Borrowing capacity ≈ 90
```

Nếu haircut tăng lên 20%, khả năng vay chỉ còn khoảng 80 dù giá tài sản chưa đổi.

## 9. Haircut spiral

Trong stress:

```text
Volatility ↑
→ Haircut ↑
→ Cần thêm collateral / cash
→ Forced Selling ↑
→ Giá ↓
→ Haircut ↑ thêm
```

Đây là một cơ chế khuếch đại khủng hoảng.

# Phần IV — Dealer và market-making

## 10. Dealer balance sheet

Dealer giúp kết nối người mua và người bán, giữ inventory và cung cấp market-making.

Nhưng dealer có giới hạn về:

- capital;
- funding;
- leverage;
- risk limit.

Khi balance-sheet capacity giảm, market depth có thể giảm ngay cả khi tài sản “rẻ”.

## 11. Thanh khoản thị trường không phải đặc tính cố định

Một tài sản bình thường có thể rất thanh khoản nhưng trở nên khó giao dịch khi:

- volatility tăng;
- dealer giảm inventory;
- mọi người cùng muốn bán;
- collateral value giảm.

Do đó liquidity phụ thuộc cả tài sản và hệ thống trung gian.

# Phần V — Money-market funds và cash management

## 12. Quỹ thị trường tiền tệ

Money-market fund (MMF) đầu tư vào tài sản ngắn hạn như Treasury bills, repo hoặc giấy tờ có độ an toàn cao.

Dòng tiền vào/ra MMF có thể thay đổi nhu cầu đối với repo và short-term government debt.

## 13. Treasury cash balance

Tài khoản tiền của chính phủ tại ngân hàng trung ương thường được gọi là Treasury General Account (TGA) ở Mỹ.

Khi chính phủ tăng mạnh số dư này, reserves của hệ thống ngân hàng có thể giảm nếu các yếu tố khác giữ nguyên.

Khi chính phủ chi tiêu từ tài khoản, reserves có thể quay lại hệ thống.

## 14. Reverse repo facility

Reverse repo facility có thể hấp thụ tiền mặt từ các tổ chức đủ điều kiện đổi lấy tài sản bảo đảm.

Dòng tiền giữa MMF, RRP, Treasury bills và deposits có thể thay đổi phân bổ thanh khoản ngắn hạn mà không đồng nghĩa nền kinh tế “thiếu tiền” theo nghĩa đơn giản.

# Phần VI — Treasury issuance và term premium

## 15. Chính phủ phát hành nợ

Nhu cầu tài trợ của chính phủ có thể được đáp ứng qua bills, notes và bonds.

Cơ cấu kỳ hạn phát hành ảnh hưởng lượng duration mà khu vực tư nhân phải nắm.

## 16. Term premium

Nếu thị trường phải hấp thụ nhiều duration hơn trong lúc uncertainty cao, term premium có thể tăng.

```text
Long-Term Issuance ↑
+ Demand không tăng tương ứng
→ Term Premium ↑
→ Long Yield ↑
```

Điều này có thể thắt financial conditions dù policy rate không đổi.

# Phần VII — Bank capital và bank liquidity

## 17. Capital và liquidity khác nhau

**Vốn (capital)** hấp thụ lỗ.

**Thanh khoản (liquidity)** giúp đáp ứng dòng tiền cần chi ngay.

Một ngân hàng có vốn cao vẫn có thể thất bại nếu deposit run quá nhanh và tài sản không bán được.

Ngược lại, một ngân hàng có thanh khoản tạm thời nhưng tài sản mất giá lớn hơn equity có thể về bản chất mất khả năng thanh toán.

## 18. Solvency

**Khả năng thanh toán dài hạn (solvency)** hỏi giá trị kinh tế của tài sản có đủ lớn so với nghĩa vụ hay không.

Liquidity support không tự động sửa insolvency.

## 19. Deposit flight

Tiền gửi có thể rút nhanh do:

- mất niềm tin;
- uninsured concentration;
- lãi suất sản phẩm khác hấp dẫn hơn;
- tin tức lan nhanh qua digital banking.

Tốc độ rút tiền hiện đại có thể nhanh hơn mô hình bank run truyền thống.

## 20. Funding concentration

Ngân hàng có hàng triệu retail deposit nhỏ khác hẳn ngân hàng phụ thuộc vài khách hàng doanh nghiệp lớn.

Funding concentration là một risk factor độc lập.

# Phần VIII — Duration mismatch trong ngân hàng

## 21. Tài sản dài hạn, nghĩa vụ ngắn hạn

Một cấu trúc điển hình:

```text
Liability:
deposits / short-term funding

Asset:
long-duration bonds / mortgages
```

Khi lãi suất tăng, giá thị trường của tài sản dài hạn giảm.

Nếu tiền gửi ổn định, ngân hàng có thể giữ tài sản tới đáo hạn. Nếu người gửi rút nhanh, ngân hàng có thể phải bán và hiện thực hóa lỗ.

## 22. Mark-to-market loss và forced realization

Lỗ đánh dấu theo thị trường chưa chắc làm mất tiền mặt ngay.

Nhưng khi tài sản buộc phải bán:

```text
Unrealized Loss
→ Realized Loss
→ Capital ↓
```

Đây là cầu nối từ duration risk sang liquidity và solvency risk.

# Phần IX — Credit creation và financial accelerator

## 23. Credit không chỉ phụ thuộc policy rate

Ngân hàng quyết định cho vay dựa trên:

- capital;
- funding;
- collateral;
- expected loss;
- regulation;
- risk appetite.

Do đó policy rate giảm không bảo đảm credit tăng ngay.

## 24. Financial accelerator

```text
Asset Price ↓
→ Collateral ↓
→ Lending Standards Tighten
→ Credit ↓
→ Investment / Consumption ↓
→ Earnings ↓
→ Credit Quality ↓
```

Vòng này có thể biến stress tài chính thành suy thoái thực.

# Phần X — Non-bank financial institutions

## 25. NBFI

NBFI gồm funds, insurers, pension funds, finance companies và các tổ chức tài chính không phải ngân hàng truyền thống.

Rủi ro tín dụng hoặc đòn bẩy có thể chuyển khỏi bank balance sheet sang hệ thống này.

## 26. Leverage ẩn

Derivatives, repo hoặc structured products có thể tạo exposure lớn hơn capital bỏ ra.

Khi volatility tăng, margin call có thể buộc các tổ chức bán tài sản khác để lấy cash.

# Phần XI — Global dollar system

## 27. USD funding ngoài Mỹ

Doanh nghiệp và ngân hàng ngoài Mỹ vay USD để tài trợ thương mại hoặc tài sản.

Khi USD funding khan hiếm:

```text
USD Funding Cost ↑
→ FX Hedge Cost ↑
→ Deleveraging ↑
→ Global Credit Tightens
```

## 28. Cross-currency basis

Cross-currency basis phản ánh chi phí hoặc mất cân bằng khi đổi funding giữa các đồng tiền qua swap.

Basis căng có thể là tín hiệu nhu cầu USD lớn hơn bình thường.

# Phần XII — QE và QT

## 29. QE

Nới lỏng định lượng (Quantitative Easing, QE) thường là ngân hàng trung ương mua tài sản dài hạn và tạo reserves.

Các kênh tác động có thể gồm:

- giảm duration supply cho khu vực tư nhân;
- giảm term premium;
- hỗ trợ market functioning;
- portfolio rebalancing.

QE không tương đương phát tiền trực tiếp cho hộ gia đình.

## 30. QT

Thắt chặt định lượng (Quantitative Tightening, QT) làm balance sheet ngân hàng trung ương giảm khi tài sản đáo hạn hoặc được bán.

Ảnh hưởng phụ thuộc:

- tốc độ QT;
- TGA;
- RRP;
- reserve demand;
- Treasury issuance.

## 31. Reserves dồi dào nhưng liquidity vẫn có thể kém

Nhiều reserves không bảo đảm mọi market đều liquid.

Stress có thể nằm ở:

- collateral;
- dealer capacity;
- specific funding market;
- counterparty concern.

# Phần XIII — Emergency facilities

## 32. Lender of last resort

Ngân hàng trung ương có thể cung cấp thanh khoản tạm thời chống lại collateral đủ chuẩn.

Mục tiêu là giảm forced selling do thiếu cash.

## 33. Liquidity facility không phải recapitalization

Cho vay thanh khoản khác với bơm vốn hấp thụ lỗ.

```text
Liquidity Facility
→ giải quyết timing/funding

Recapitalization
→ bổ sung loss-absorbing capital
```

Không nên gọi mọi hỗ trợ là “QE” hoặc “bailout”.

# Phần XIV — Các loại khủng hoảng

## 34. Banking crisis

Có thể bắt đầu từ:

- credit loss;
- duration loss;
- funding run;
- fraud;
- property crash.

Cơ chế và policy response phụ thuộc nguồn gốc.

## 35. Sovereign crisis

Nợ chính phủ có thể trở thành vấn đề khi:

- debt service tăng nhanh;
- investor demand giảm;
- debt bằng foreign currency;
- growth yếu;
- fiscal credibility xấu.

## 36. Currency crisis

FX shock có thể truyền qua:

```text
Currency ↓
→ Imported Inflation ↑
→ FX Debt Burden ↑
→ Rate Pressure ↑
→ Growth ↓
```

## 37. Inflation crisis

Nếu inflation expectations mất neo, ngân hàng trung ương có thể phải giữ policy chặt dù tăng trưởng yếu.

Đây là trade-off khác hoàn toàn liquidity crisis.

# Phần XV — Fiscal dominance

## 38. Khi monetary và fiscal bắt đầu xung đột

Nếu chi phí tài trợ chính phủ tăng mạnh, tightening monetary có thể làm debt service tăng.

**Fiscal dominance** mô tả tình huống ràng buộc tài khóa làm khả năng ưu tiên ổn định giá của ngân hàng trung ương bị hạn chế.

Không phải mọi mức nợ cao đều đồng nghĩa fiscal dominance.

# Phần XVI — Market indicators

## 39. Dashboard thanh khoản

Có thể theo dõi:

```text
Policy Rate
Repo Rates
SOFR / Money-Market Rates
Bank Reserves
TGA
RRP
Treasury Issuance
Credit Spreads
Cross-Currency Basis
Bank Funding Spreads
USD
```

## 40. Dashboard stress

```text
Bid-Ask Spread
Market Depth
Haircut
Margin Requirement
Volatility
Dealer Inventory
Funding Spread
Credit Default Swap
```

Không một chỉ số đơn lẻ đủ để kết luận hệ thống stress.

# Phần XVII — Chuỗi truyền dẫn khủng hoảng

## 41. Cú sốc funding

```text
Funding Cost ↑
→ Leverage ↓
→ Asset Sales ↑
→ Price ↓
→ Collateral ↓
→ Funding Capacity ↓
```

## 42. Cú sốc ngân hàng

```text
Asset Loss
→ Capital Concern
→ Deposit Outflow
→ Liquidity Need
→ Asset Sale / Central-Bank Facility
→ Credit Tightening
→ Real Economy
```

## 43. Cú sốc USD

```text
USD ↑
→ Foreign-Currency Debt Burden ↑
→ Hedge Cost ↑
→ Deleveraging
→ EM / Global Credit Tightening
```

# Phần XVIII — Cách dùng trong đầu tư

## 44. Giá của tiền và lượng thanh khoản là hai lớp khác nhau

Policy rate là **giá của funding ngắn hạn**.

Nhưng điều kiện tài chính còn phụ thuộc:

- lượng funding có sẵn;
- collateral;
- distribution của liquidity;
- willingness to lend.

## 45. Đừng nhầm reserves với broad liquidity

Reserves cao không đồng nghĩa mọi doanh nghiệp hoặc hộ gia đình dễ vay.

Kênh truyền dẫn qua bank capital, credit standards và collateral vẫn rất quan trọng.

## 46. Đừng nhầm central-bank liquidity với solvency repair

Cho vay emergency có thể cho một tổ chức thêm thời gian nhưng không loại bỏ economic loss nếu tài sản thực sự không đủ giá trị.

## 47. Đọc crisis theo bảng cân đối

Khi có stress, hãy hỏi:

```text
Ai đang thiếu cash?
Ai đang thiếu capital?
Ai đang giữ collateral nào?
Ai có maturity mismatch?
Ai có currency mismatch?
Ai là forced seller?
Ai có thể cung cấp liquidity?
```

## 48. Reverse stress test

Thay vì chỉ hỏi “asset giảm 20% thì sao?”, hãy hỏi:

```text
Điều gì có thể buộc một tổ chức bán tài sản tốt ở đáy?
```

Câu trả lời thường liên quan margin, funding, collateral hoặc redemption.

# Phần XIX — Checklist nghiên cứu

## 49. Trước khi kết luận “liquidity đang tốt”

Kiểm tra:

```text
Reserves
Bank Funding
Repo
Collateral
Dealer Capacity
Credit Spreads
Lending Standards
FX Funding
Market Depth
```

## 50. Trước khi kết luận “central bank đã cứu hệ thống”

Hỏi:

```text
Facility giải quyết liquidity hay capital?
Collateral được định giá thế nào?
Ai chịu ultimate credit loss?
Credit creation có phục hồi không?
```

## Kết luận

Hệ thống tiền tệ không thể được hiểu bằng một câu “ngân hàng trung ương bơm tiền” hay “liquidity tăng”.

Cần tách rõ:

```text
Money
Reserves
Deposits
Funding
Collateral
Capital
Credit
Market Liquidity
```

Khủng hoảng thường xuất hiện khi một trong các mắt xích này làm các tổ chức phải bán tài sản, giảm tín dụng hoặc thay đổi hành vi theo cách khuếch đại cú sốc ban đầu.
