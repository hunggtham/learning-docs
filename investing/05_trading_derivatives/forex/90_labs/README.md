# Forex Practice Labs

Phần này biến các chapter `01–15` thành bài tập có đầu ra cụ thể. Mục tiêu không phải luyện đoán hướng giá, mà luyện **mechanics → hypothesis → dữ liệu (data / 데이터) → sizing → thực thi (execution / 실행) → rà soát (review / 검토)**.

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

1. [00_QUOTES_MARGIN_AND_POSITION_SIZING_LAB.md](./00_QUOTES_MARGIN_AND_POSITION_SIZING_LAB.md) — tự tính quote, pip giá trị (value / 값), P/L, leverage, margin và position kích thước (size / 크기).
2. [01_EVENT_DRIVEN_FX_ANALYSIS_LAB.md](./01_EVENT_DRIVEN_FX_ANALYSIS_LAB.md) — phân tích CPI/FOMC/BOK hoặc sự kiện (event / 이벤트) tương tự theo expectation-surprise-transmission.
3. [02_POINT_IN_TIME_BACKTEST_LAB.md](./02_POINT_IN_TIME_BACKTEST_LAB.md) — biến một setup thành backtest point-in-time có chi phí (cost / 비용) và robustness checks.
4. [03_PORTFOLIO_FX_RISK_LAB.md](./03_PORTFOLIO_FX_RISK_LAB.md) — phân rã nhiều pair thành currency-factor exposure và stress portfolio heat.
5. [04_KOREA_VIETNAM_FX_CONTEXT_LAB.md](./04_KOREA_VIETNAM_FX_CONTEXT_LAB.md) — nối USD/KRW và USD/VND với rates, bên ngoài (external / 외부) balance, chính sách (policy / 정책) ràng buộc (constraint / 제약조건) và market-access ngữ cảnh (context / 맥락).

## Chuẩn đầu ra

Mỗi lab phải tạo sản phẩm tạo ra (artifact / 산출물) có thể rà soát (review / 검토). Không chấp nhận câu trả lời chỉ gồm nhận định như “USD mạnh”, “RSI quá mua” hoặc “hỗ trợ (support / 지원) giữ được”. Phải thể hiện rõ dữ liệu nào dẫn tới kết luận nào, mức rủi ro bao nhiêu, điều gì làm giả thuyết sai và sau kết quả sẽ attribution thế nào.

Các lab này bổ sung cho [Advanced Practice Workbook](../../../ADVANCED_PRACTICE_WORKBOOK.md), đặc biệt Mô-đun (module / 모듈) 5 — Trading & Derivatives, nhưng đi sâu riêng vào Forex.
