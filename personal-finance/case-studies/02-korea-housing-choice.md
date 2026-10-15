# Case 02 — Chọn cấu trúc nhà ở tại Hàn Quốc: 월세, 보증금 hay 전세 nhìn từ Personal Finance

## Bối cảnh

Một household đang sống tại Hàn Quốc và chuẩn bị đổi nhà. Có ba lựa chọn minh họa:

```text
A. 월세 thấp deposit, rent cao
B. 월세 deposit lớn hơn, rent thấp hơn
C. 전세-like structure: deposit rất lớn, monthly rent rất thấp hoặc không có
```

Các con số cụ thể khác nhau mạnh theo khu vực, thời điểm và hợp đồng, vì vậy case này không dùng giá thị trường hiện hành. Mục tiêu là học cách nhìn **housing decision như một thay đổi đồng thời của cash flow, liquidity, concentration risk và legal risk**.

## 1. Đừng so chỉ monthly rent

Giả sử:

```text
Option A
Deposit   10m KRW
Rent      1.1m / month

Option B
Deposit   50m KRW
Rent      0.65m / month

Option C
Deposit   180m KRW
Rent      gần 0
```

Nếu chỉ nhìn monthly payment, C có vẻ rẻ nhất. Nhưng 170m KRW thêm so với A bị khóa vào housing deposit. Số tiền đó có opportunity cost, liquidity cost và recovery risk.

Vì vậy cần so:

```text
monthly housing cash flow
+ capital tied up
+ financing cost if deposit is borrowed
+ transaction/moving cost
+ liquidity loss
+ deposit recovery risk
+ legal/operational risk
```

## 2. Capital tied up không phải chi phí giống rent

Deposit vẫn là asset/receivable nếu có thể thu hồi đầy đủ, nên không nên cộng toàn bộ deposit vào “expense”. Nhưng capital bị khóa có economic cost.

Một cách tư duy:

```text
Housing economic burden
≈ explicit rent
+ financing cost of borrowed deposit
+ opportunity cost of own capital
+ expected risk / friction cost
+ transaction and moving cost
```

Không cần biến opportunity cost thành một số tuyệt đối duy nhất. Chỉ cần nhìn được rằng 100m KRW locked capital làm household mất optionality ở nơi khác.

## 3. Borrowed deposit làm thay đổi toàn bộ bài toán

Nếu household phải vay để tăng deposit, rent giảm nhưng debt service xuất hiện.

Ví dụ minh họa:

```text
Rent saving from larger deposit: 450k/month
Additional loan payment/cost:      500k/month
```

Lúc này “deposit lớn để giảm rent” không còn tự động tiết kiệm cash flow.

Ngoài interest, cần xét:

- fixed vs variable rate;
- maturity mismatch giữa loan và lease;
- repayment schedule;
- prepayment fee nếu có;
- khả năng refinance;
- income shock khi đang có debt.

Framework nằm ở [03 Interest](../03-interest.md) và [06 Loans & Debt](../06-loans-debt.md).

## 4. Liquidity concentration

Giả sử household có net worth 230m KRW, trong đó 180m nằm ở housing deposit. Net worth vẫn cao, nhưng 78% tài sản ròng tập trung vào một receivable gắn với một contract/property/counterparty.

Đây là concentration risk.

```text
high net worth
≠ high liquidity
≠ low risk
```

Nếu cùng lúc cần chuyển nhà, mất việc hoặc gửi tiền về gia đình, household có thể thiếu cash dù balance sheet nhìn đẹp.

## 5. Emergency fund không được tính trùng với deposit

Một lỗi thường gặp:

```text
"Tôi có deposit 180m nên không cần giữ nhiều cash."
```

Deposit không phải emergency cash nếu không thể rút ngay mà không phá lease hoặc chịu legal/contractual friction.

Do đó balance sheet nên tách:

```text
Housing deposit receivable
Emergency cash
Other liquid assets
```

Không cộng cùng một asset vào hai vai trò.

## 6. Legal due diligence là một phần của financial risk

Với housing tại Hàn Quốc, risk không chỉ là rent/deposit amount. Cần hiểu owner, registered rights, priority, deposit protection mechanism, contract và timing của các thủ tục liên quan.

Phần sâu thuộc canonical owner:

[Housing — 월세, 전세, 보증금, bảo vệ người thuê và đăng ký bất động sản](../../korea_law_civic_life/06_housing_wolse_jeonse_deposit_and_registration.md)

Personal Finance chỉ giữ nguyên tắc:

```text
large deposit
→ legal claim / counterparty exposure
→ verification and protection process
→ must be included in risk-adjusted housing decision
```

Một option có monthly cost thấp nhưng recovery risk cao không thể được đánh giá chỉ bằng spreadsheet rent.

## 7. Stress test từng option

### Shock A — mất việc 4 tháng

Option A có rent cao nhưng nhiều cash còn lại hơn.

Option C có rent thấp nhưng phần lớn wealth bị khóa trong deposit.

Câu hỏi không phải option nào luôn tốt hơn; câu hỏi là:

```text
Which option leaves enough accessible liquidity under income shock?
```

### Shock B — cần chuyển thành phố sớm

Lease exit friction, deposit-return timing và moving cost trở nên quan trọng. Option có capital locked lớn có thể tạo timing mismatch.

### Shock C — lãi vay tăng

Nếu deposit được finance bằng variable-rate loan, housing cash flow có thể xấu nhanh dù rent không đổi.

### Shock D — KRW giảm so với currency của nghĩa vụ gia đình

Nếu household gửi tiền về Việt Nam, housing deposit càng lớn càng giảm khả năng phản ứng với FX shock. Đây là điểm nối sang [17 Cross-Border Personal Finance](../17-cross-border-personal-finance.md).

## 8. Housing decision matrix

Thay vì xếp hạng một chiều, đánh giá theo nhiều biến:

```text
Monthly cash burden
Upfront capital required
Liquidity after move-in
Debt added
Interest-rate sensitivity
Deposit recovery risk
Expected holding period
Mobility need
Transaction cost
Legal due diligence complexity
Emergency-fund coverage after transaction
```

Hai household cùng income có thể chọn khác nhau vì visa/job stability, family plan, relocation probability, debt capacity hoặc cross-border obligation khác nhau.

## 9. Decision boundary

Một housing option chỉ nên đi qua resilience gate nếu sau khi ký:

```text
emergency liquidity vẫn đủ
+ debt service vẫn chịu được stress
+ deposit/contract risk đã được kiểm tra
+ household không phụ thuộc việc bán investment để trả chi phí thường xuyên
+ vẫn có margin cho moving/repair/family shocks
```

Nếu transaction làm cash buffer gần bằng 0, việc “monthly rent thấp” chưa đủ chứng minh affordability.

## Kết luận

Housing là ví dụ điển hình cho khác biệt giữa **giá hàng tháng** và **cấu trúc tài chính tổng thể**. 월세, deposit lớn hay 전세-like structure đều có trade-off giữa rent, capital lock-up, debt, liquidity và legal risk.

Đọc tiếp [09 Housing](../09-housing.md), [14 Personal Balance Sheet](../14-personal-balance-sheet.md), [15 Financial Resilience](../15-financial-resilience.md) và [16 Korea–Vietnam Practical Map](../16-korea-vietnam-practical-map.md).