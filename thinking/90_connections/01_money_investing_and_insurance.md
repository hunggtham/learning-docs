# Case — Tiền, đầu tư, bảo hiểm và quyết định tài chính

Financial decisions thường khó không phải vì thiếu công thức mà vì phải kết hợp uncertainty, time horizon, downside, opportunity cost và behavior.

Trang này không đưa khuyến nghị đầu tư cụ thể. Nó cung cấp reasoning workflow; household mechanics và constraints handoff sang [Personal Finance](../../personal-finance/README.md), còn asset/portfolio mechanics handoff sang [Investing](../../investing/README.md).

## Situation

Bạn có một khoản tiền và đang cân nhắc:

```text
cash
vs
repay debt
vs
insurance / emergency reserve
vs
investment A
vs
investment B
```

Sai lầm phổ biến là hỏi ngay “cái nào return cao nhất?”. Trước khi tối ưu return, cần biết tiền này đang bảo vệ obligation nào, liquidity tối thiểu là bao nhiêu, debt nào đang tồn tại và phần vốn nào thực sự có thể chịu market risk.

## Step 1 — Frame objective

Phân biệt:

```text
capital preservation
liquidity
income
long-term growth
hedging
specific future liability
```

Một asset tốt cho objective này có thể tệ cho objective khác.

Nếu câu hỏi là emergency fund, debt, insurance need, housing, retirement hoặc household resilience, xác định constraint tại [Personal Finance](../../personal-finance/README.md) trước. Chỉ sau đó mới chuyển phần vốn investable sang Investing.

## Step 2 — Opportunity cost

Mọi đồng vốn được phân bổ vào một option làm mất khả năng dùng nó cho option tốt nhất còn lại.

Đặc biệt cần tính:

- debt cost avoided;
- liquidity lost;
- emergency flexibility;
- alternative expected return;
- tax/fee/friction khi relevant.

Handoff: [Opportunity Cost](../opportunity-cost/README.md).

## Step 3 — Probability và forecasting

Không dùng một forecast duy nhất.

```text
base case
upside case
adverse case
tail case
```

Gắn assumptions rõ và tránh false precision. Handoff: [Forecasting](../forecasting/README.md).

## Step 4 — Expected value chưa đủ

Hai option có cùng expected value nhưng downside khác hoàn toàn.

Cần hỏi:

```text
Can I survive the bad state?
Can losses compound?
Is leverage involved?
Are risks correlated?
Can I exit when needed?
```

Handoff: [Risk](../risk/README.md).

Ở household level, “survive the bad state” còn phụ thuộc emergency liquidity, debt service, income stability, insurance coverage và obligations. Đây là lý do một portfolio decision không thể tách khỏi personal balance sheet.

## Step 5 — Insurance logic

Insurance có thể có negative expected monetary value đối với buyer nhưng vẫn rational nếu nó chuyển một tail loss khó chịu đựng thành premium nhỏ, predictable.

Do đó:

```text
expected value
≠ utility
≠ ruin protection
```

Chi tiết về role của insurance trong household risk management handoff sang [Personal Finance — Insurance](../../personal-finance/07-insurance.md). Điều khoản sản phẩm cụ thể vẫn phải đọc contract và nguồn chính thức tương ứng.

## Step 6 — Behavior

Check:

- loss aversion có làm mình giữ asset xấu chỉ vì không muốn realize loss?
- recency có làm extrapolate return gần đây?
- social proof có thay thế analysis?
- sunk cost có làm tăng position dù thesis đã đổi?

Handoff: [Cognitive Bias](../cognitive-bias/README.md).

## Step 7 — Value of information

Trước khi research thêm, hỏi information nào có thể thật sự đổi allocation.

Ví dụ:

```text
fee structure?
liquidity constraint?
debt interest rate?
insurance exclusions?
company cash flow assumption?
```

Không research vô hạn những biến không thay đổi decision.

## Step 8 — Review rule

Trước khi commit, ghi:

```text
thesis
key assumptions
main downside
what would falsify thesis
rebalancing / review condition
```

Điều này giảm hindsight và narrative drift. Với quyết định household lớn, có thể nối sang [Annual Financial Review](../../personal-finance/19-annual-financial-review.md) để review balance sheet, liquidity, debt, protection và long-term allocation theo cùng một vòng phản hồi.

## Toolkit used

[Problem Framing](../problem-framing/README.md) → [Opportunity Cost](../opportunity-cost/README.md) → [Forecasting](../forecasting/README.md) → [Expected Value](../expected-value/README.md) → [Risk](../risk/README.md) → [Value of Information](../value-of-information/README.md) → [Cognitive Bias](../cognitive-bias/README.md) → [Decision Making](../decision-making/README.md).

## Handoff

- Household cash flow, debt, emergency liquidity, insurance, housing, retirement và resilience → [Personal Finance](../../personal-finance/README.md)
- Asset classes, valuation, portfolio construction và market risk → [Investing](../../investing/README.md)
- Economics, rates, inflation, incentives → [Economics](../../economics/README.md)
- Probability/statistics → [Mathematics](../../mathematics/README.md)
- Behavioral mechanisms → [Psychology](../../psychology/README.md)

Một cách đọc ngắn gọn là:

```text
Personal Finance xác định capacity + constraints
→ Thinking làm rõ uncertainty/trade-off
→ Investing xử lý investable capital và market mechanics
→ review outcome rồi update assumptions
```