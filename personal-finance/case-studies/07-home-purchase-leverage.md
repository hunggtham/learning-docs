# Case 07 — Mua nhà bằng leverage: affordability không chỉ là “ngân hàng cho vay bao nhiêu”

## Tình huống

Một household đang cân nhắc mua nhà. Ngân hàng sẵn sàng cho vay đủ lớn để giao dịch có thể thực hiện được, và monthly payment ở base case vẫn nằm trong mức household “có thể trả”. Câu hỏi tưởng như đơn giản là:

> Nếu được approve mortgage, có nên mua ngay không?

Case này dùng để phân biệt **khả năng được cấp tín dụng (credit eligibility / 신용 승인 가능성)** với **khả năng chịu đựng tài chính (financial affordability / 재무 감당 가능성)**.

## Initial state giả định

```text
monthly take-home income        = 6.0 triệu KRW
essential non-housing spending = 2.2 triệu KRW
current rent                   = 1.2 triệu KRW
liquid assets                  = 90 triệu KRW
long-term investments          = 50 triệu KRW
other debt payment             = 0.3 triệu KRW/tháng
```

Household đang xem một căn nhà có:

```text
purchase price                 = 500 triệu KRW
down payment + fees needed     = 100 triệu KRW
mortgage                       = 400 triệu KRW
illustrative payment           = 2.0 triệu KRW/tháng
maintenance/tax/insurance      = 0.5 triệu KRW/tháng
```

Các số trên chỉ là giả định để học reasoning, không phải mortgage quote hay quy định hiện hành.

## 1. Sai lầm đầu tiên: chỉ so rent với mortgage payment

So sánh:

```text
rent = 1.2
mortgage payment = 2.0
```

là thiếu vì homeowner còn có:

```text
maintenance
+ property-related tax/fees
+ insurance
+ repair reserve
+ transaction cost
+ opportunity cost của down payment
+ liquidity lock-up
```

Do đó economic burden nên được nhìn như:

```text
housing cash outflow
+ capital locked
+ leverage risk
+ exit friction
```

chứ không phải chỉ monthly mortgage.

## 2. Down payment có thể làm household yếu đi dù net worth không giảm mạnh

Trước giao dịch:

```text
liquid assets = 90
```

Nếu household cần dùng gần toàn bộ 90 triệu KRW và thêm 10 triệu từ investments để đóng down payment/fees, sau closing có thể còn rất ít liquidity.

Balance sheet có thể vẫn trông “giàu” vì household sở hữu home equity, nhưng:

```text
liquid runway ↓
fixed obligation ↑
asset concentration ↑
transaction reversibility ↓
```

Đây là lý do [Personal Balance Sheet](../14-personal-balance-sheet.md) phải được đọc cùng [Financial Resilience](../15-financial-resilience.md).

## 3. Mortgage approval không phải resilience test

Lender chủ yếu hỏi liệu loan có đáp ứng underwriting criteria của họ. Household phải hỏi thêm:

```text
Nếu income giảm 30% thì sao?
Nếu một người mất việc 6 tháng thì sao?
Nếu interest rate reset tăng thì sao?
Nếu phát sinh repair lớn thì sao?
Nếu phải chuyển thành phố/quốc gia sớm thì sao?
```

### Stress scenario A — income giảm 30%

Take-home income giảm từ:

```text
6.0 → 4.2 triệu KRW/tháng
```

Giả sử fixed housing burden khoảng:

```text
mortgage 2.0
+ maintenance/tax/insurance 0.5
= 2.5
```

và non-housing essentials vẫn 2.2, household đã dùng:

```text
2.5 + 2.2 = 4.7
```

trước other debt và unexpected expenses.

Base case “trả được” nhưng stressed case đã âm cash flow.

## 4. Interest-rate risk phải được nhìn như obligation risk

Nếu mortgage có variable/reset component, household không nên hỏi chỉ:

> Lãi suất hôm nay bao nhiêu?

Mà phải hỏi:

> Payment sẽ ra sao nếu financing cost tăng đáng kể?

Có thể stress bằng payment thay vì dự báo rate chính xác:

```text
Base mortgage payment   = 2.0
Stress mortgage payment = 2.4
Severe                  = 2.7
```

Mục tiêu không phải đoán interest rate tương lai. Mục tiêu là kiểm tra household có break khi obligation tăng hay không.

## 5. Concentration risk

Một căn nhà có thể chiếm phần lớn net worth của household.

Ví dụ sau vài năm:

```text
home equity        = 180 triệu KRW
financial assets   = 60 triệu KRW
```

thì khoảng ba phần tư wealth có thể nằm trong một asset duy nhất, ở một địa điểm duy nhất, với transaction cost cao.

Điều này không tự làm home purchase “xấu”. Nó chỉ nghĩa là risk profile khác với household có wealth phân tán và liquid hơn.

## 6. Exit friction là một phần của decision

Rent thường dễ thay đổi hơn ownership. Khi mua nhà, exit có thể cần:

```text
listing/sale process
+ transaction costs
+ market liquidity
+ loan settlement
+ moving logistics
```

Vì vậy holding period kỳ vọng càng ngắn, transaction friction càng quan trọng.

Một household có khả năng phải đổi việc, đổi visa, chuyển quốc gia hoặc chuyển thành phố nên đặt trọng số lớn hơn cho **optionality (선택 가능성)**.

## 7. Decision boundary

Case này không kết luận “mua” hay “không mua”. Decision boundary nằm ở các biến:

```text
post-closing emergency liquidity
expected holding period
income stability
mortgage structure
stress payment capacity
repair reserve
concentration tolerance
legal/transaction due diligence
```

Hai household có cùng income và cùng house price có thể đi tới lựa chọn khác nhau vì liquidity và job stability khác nhau.

## 8. Một affordability gate thực tế hơn

Trước khi coi house là affordable, household có thể kiểm tra theo thứ tự:

```text
1. Sau down payment/fees còn emergency liquidity không?
2. Monthly cash flow base case còn margin không?
3. Income -30% có còn service được obligations không?
4. Housing cost + other debt có tạo fixed-cost trap không?
5. Có repair/maintenance reserve riêng không?
6. Nếu phải exit sớm, household chịu được transaction loss không?
7. Asset concentration sau mua có chấp nhận được không?
```

Nếu một deal chỉ “works” khi mọi assumption đều thuận lợi, đó là fragility chứ không phải resilience.

## 9. Korea-specific legal boundary

Nếu giao dịch nằm ở Hàn Quốc, financing ratio, mortgage regulation, taxes, registration, tenant/owner rights và các chương trình cụ thể là dữ liệu jurisdiction/time-sensitive.

Case này không hard-code các rule đó. Khi áp dụng thực tế, chuyển sang canonical owner:

- [Korea Law, Civic & Everyday Life — Housing](../../korea_law_civic_life/06_housing_wolse_jeonse_deposit_and_registration.md)
- [Korea–Vietnam Practical Map](../16-korea-vietnam-practical-map.md)

## 10. Kết luận

Mortgage leverage biến một housing decision thành một hệ thống obligation dài hạn.

```text
Bank approval
≠
personal affordability

Monthly payment
≠
total housing burden

Net worth
≠
liquidity
```

Mục tiêu của household không phải mua mức nhà tối đa mà lender cho phép. Mục tiêu là chọn một cấu trúc housing vẫn hoạt động khi đời sống không đi đúng base case.