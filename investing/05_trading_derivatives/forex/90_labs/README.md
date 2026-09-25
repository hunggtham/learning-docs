# Forex Practice Labs

Phần này biến các chapter `01–15` thành bài tập có đầu ra cụ thể. Mục tiêu không phải luyện đoán hướng giá, mà luyện **mechanics → hypothesis → data → sizing → execution → review**.

Đọc lý thuyết trước, sau đó làm lab bằng dữ liệu giả định hoặc dữ liệu lịch sử có timestamp rõ ràng. Mọi lab đều phải phân biệt:

```text
Fact
Estimate
Assumption
Scenario
Decision Rule
Observed Result
Post-mortem
```

## Thứ tự thực hành

1. [00_QUOTES_MARGIN_AND_POSITION_SIZING_LAB.md](./00_QUOTES_MARGIN_AND_POSITION_SIZING_LAB.md) — tự tính quote, pip value, P/L, leverage, margin và position size.
2. [01_EVENT_DRIVEN_FX_ANALYSIS_LAB.md](./01_EVENT_DRIVEN_FX_ANALYSIS_LAB.md) — phân tích CPI/FOMC/BOK hoặc event tương tự theo expectation-surprise-transmission.
3. [02_POINT_IN_TIME_BACKTEST_LAB.md](./02_POINT_IN_TIME_BACKTEST_LAB.md) — biến một setup thành backtest point-in-time có cost và robustness checks.
4. [03_PORTFOLIO_FX_RISK_LAB.md](./03_PORTFOLIO_FX_RISK_LAB.md) — phân rã nhiều pair thành currency-factor exposure và stress portfolio heat.
5. [04_KOREA_VIETNAM_FX_CONTEXT_LAB.md](./04_KOREA_VIETNAM_FX_CONTEXT_LAB.md) — nối USD/KRW và USD/VND với rates, external balance, policy constraint và market-access context.

## Chuẩn đầu ra

Mỗi lab phải tạo artifact có thể review. Không chấp nhận câu trả lời chỉ gồm nhận định như “USD mạnh”, “RSI quá mua” hoặc “support giữ được”. Phải thể hiện rõ dữ liệu nào dẫn tới kết luận nào, mức rủi ro bao nhiêu, điều gì làm giả thuyết sai và sau kết quả sẽ attribution thế nào.

Các lab này bổ sung cho [Advanced Practice Workbook](../../../ADVANCED_PRACTICE_WORKBOOK.md), đặc biệt Module 5 — Trading & Derivatives, nhưng đi sâu riêng vào Forex.
