# 18 — Case Studies: từ concept sang quyết định thực tế

## Định vị

Các chapter 01–17 xây mental model và boundary. Chapter 18 không thêm một khái niệm tài chính mới; nó là **application layer** để luyện cách kết hợp nhiều concept cùng lúc.

Trong đời thực, một quyết định hiếm khi chỉ thuộc một chapter. Mất việc liên quan cash flow, emergency fund, debt, insurance và liquidity. Mua xe liên quan financing, depreciation, fixed-cost load và opportunity cost. Sống ở Hàn nhưng có nghĩa vụ ở Việt Nam liên quan FX, remittance, tax boundary và multi-country liquidity.

Vì vậy case study được dùng để luyện một invariant:

```text
State
→ constraints
→ cash flow
→ balance sheet
→ liquidity
→ stress scenarios
→ options
→ second-order effects
→ decision boundary
→ review trigger
```

Không bắt đầu bằng “phương án nào sinh lời nhất?”. Bắt đầu bằng **hệ thống có sống sót được không và decision có còn reversible không**.

## Application route

Toàn bộ case nằm trong [`case-studies/`](./case-studies/README.md):

```text
Case 01 — Mất việc sáu tháng
→ runway / expense triage / debt / recovery capacity

Case 02 — Housing tại Hàn Quốc
→ 월세 / 보증금 / 전세-like structure
→ capital lock-up / legal risk / liquidity

Case 03 — Income KRW, obligation VND
→ functional currency / FX mismatch / remittance / multi-country reserve

Case 04 — Trả nợ hay đầu tư
→ guaranteed debt saving / uncertain return / resilience gate

Case 05 — Mua xe sau khi tăng lương
→ total cost / lifestyle inflation / fixed-cost trap

Case 06 — Đã chuyển tiền cho scammer
→ containment / evidence / account security / liquidity recovery
```

## Case 01 — shock về income

[Mất việc sáu tháng](./case-studies/01-six-month-job-loss.md) buộc người đọc phân biệt:

```text
normal spending
vs
emergency burn
```

và:

```text
net worth
vs
liquid runway
```

Case này nên đọc sau [12 Emergency Fund](./12-emergency-fund.md) và [15 Financial Resilience](./15-financial-resilience.md).

## Case 02 — housing không chỉ là rent

[Housing tại Hàn Quốc](./case-studies/02-korea-housing-choice.md) cho thấy monthly housing payment chỉ là một phần của economic burden. Deposit lớn có thể giảm rent nhưng tăng capital lock-up, concentration và legal/counterparty exposure.

Khi cần legal mechanics thực tế, chuyển sang canonical owner [Korea Law, Civic & Everyday Life — Housing](../korea_law_civic_life/06_housing_wolse_jeonse_deposit_and_registration.md).

## Case 03 — cross-border household

[Income KRW, obligation VND](./case-studies/03-krw-income-vnd-obligations.md) làm rõ rằng FX risk tồn tại ngay cả khi household không trade Forex.

```text
income currency ≠ obligation currency
→ household FX exposure
```

Case này là application trực tiếp của [17 Cross-Border Personal Finance](./17-cross-border-personal-finance.md).

## Case 04 — asset side và liability side phải đọc cùng nhau

[Trả nợ hay đầu tư](./case-studies/04-debt-vs-investing.md) ngăn một lỗi phổ biến: chỉ nhìn expected return của asset mà bỏ qua guaranteed cost của liability.

```text
portfolio decision
must be evaluated together with
household debt structure
```

Đây là bridge rõ nhất giữa Personal Finance và Investing.

## Case 05 — income growth không đồng nghĩa wealth growth

[Mua xe sau khi tăng lương](./case-studies/05-car-purchase-income-rise.md) cho thấy salary increase có thể bị fixed cost mới hấp thụ hoàn toàn.

```text
income ↑
+ lifestyle fixed cost ↑
→ savings margin có thể không tăng
```

Case này nối [10 Car Finance](./10-car-finance.md) với [14 Personal Balance Sheet](./14-personal-balance-sheet.md) và [15 Financial Resilience](./15-financial-resilience.md).

## Case 06 — financial incident response

[Đã chuyển tiền cho scammer](./case-studies/06-financial-scam-incident.md) chuyển từ prevention sang containment:

```text
contain
→ secure root accounts
→ assess blast radius
→ preserve evidence
→ recover liquidity
→ review controls
```

Điểm quan trọng là scam không kết thúc khi transfer xong. Identity exposure, account takeover và recovery scam có thể tạo second incident.

## Cách tự tạo case mới

Khi thêm một case sau này, không viết kiểu story rồi đưa moral lesson. Hãy cấu trúc:

```text
1. Initial state
2. Numeric assumptions
3. What looks attractive at first glance
4. Hidden variables
5. Base-case calculation
6. Adverse scenarios
7. Trade-offs
8. Decision boundary
9. What information is missing
10. Links back to canonical concepts
```

Nếu có dữ liệu time-sensitive, phải ghi jurisdiction, source, effective date và scope như policy trong [Coverage Audit](./COVERAGE_AUDIT.md).

## Không dùng case để tạo rule universal

Một case chỉ chứng minh **cách reasoning hoạt động dưới một bộ assumptions**. Nó không chứng minh mọi household nên làm giống nhau.

Ví dụ:

```text
"Case A trả debt trước"
≠
"Mọi người luôn phải trả mọi debt trước khi invest"
```

Nếu income stability, tax, loan rate, liquidity, family obligation hoặc time horizon thay đổi, decision boundary cũng thay đổi.

## Kết luận

Chapter 18 là nơi kiểm tra xem kiến thức từ 01–17 có thực sự trở thành decision skill hay chưa.

Mục tiêu cuối cùng của Personal Finance không phải nhớ từng ratio. Nó là có khả năng nhìn một tình huống mới và tự dựng đúng mô hình:

```text
What changes cash flow?
What changes balance sheet?
What becomes fixed?
What becomes illiquid?
What can fail together?
How long can the system survive?
What remains reversible?
Only then: what should capital do next?
```

Sau khi đi qua application route này, người học có thể chuyển sang [Economics](../economics/README.md) để hiểu external environment và [Investing](../investing/README.md) khi thực sự có investable surplus.