# Forex Practice Labs

> **Mạch đọc:** Đọc **Forex Practice Labs** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Thứ tự thực hành** sang **Chuẩn đầu ra**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

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
6. [05_FX_OPTIONS_QUANTITATIVE_LAB.md](./05_FX_OPTIONS_QUANTITATIVE_LAB.md) — định giá vanilla FX options, kiểm tra Greeks, scenario P/L, volatility surface và delta-hedging ledger.
7. [06_VIETNAM_FX_MANAGEMENT_STRESS_LAB.md](./06_VIETNAM_FX_MANAGEMENT_STRESS_LAB.md) — phân rã reserve/intervention, chính sách (policy / 정책) sự đánh đổi (trade-off / 트레이드오프), band widening và importer/exporter hedge stress.
8. [07_CROSS_REGIME_FX_STRESS_SYNTHESIS_LAB.md](./07_CROSS_REGIME_FX_STRESS_SYNTHESIS_LAB.md) — so sánh bảy historical regimes bằng vulnerability, trigger, amplifier, balance-sheet transmission và reverse stress.
9. [08_HEDGE_ACCOUNTING_DOCUMENTATION_BOUNDARY_LAB.md](./08_HEDGE_ACCOUNTING_DOCUMENTATION_BOUNDARY_LAB.md) — lập exposure register, designation memo, ineffectiveness phân tích (analysis / 분석) và rebalance/discontinuation controls.


> **Chuyển mạch:** Từ **Thứ tự thực hành**, ta sang **Chuẩn đầu ra** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chuẩn đầu ra

Mỗi lab phải tạo sản phẩm tạo ra (artifact / 산출물) có thể rà soát (review / 검토). Không chấp nhận câu trả lời chỉ gồm nhận định như “USD mạnh”, “RSI quá mua” hoặc “hỗ trợ (support / 지원) giữ được”. Phải thể hiện rõ dữ liệu nào dẫn tới kết luận nào, mức rủi ro bao nhiêu, điều gì làm giả thuyết sai và sau kết quả sẽ attribution thế nào.

Các lab này bổ sung cho [Advanced Practice Workbook](../../../ADVANCED_PRACTICE_WORKBOOK.md), đặc biệt mô-đun (module / 모듈) 5 — Trading & Derivatives, nhưng đi sâu riêng vào Forex. Lab 05 là quantitative extension của chapter 14; Lab 06 là institutional/regime extension của chapter 15 và trường hợp (case / 사례) 07; Lab 07 là synthesis gate của historical trường hợp (case / 사례) tầng (layer / 계층); Lab 08 là documentation/điều khiển (control / 제어) extension của hedge-accounting ranh giới (boundary / 경계). Các lab dùng simulation trước, còn thị trường (market / 시장) dữ liệu (data / 데이터) thật phải giữ point-in-time snapshot và convention siêu dữ liệu (metadata / 메타데이터).

> **Bàn giao:** Sau **Chuẩn đầu ra**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 QUOTES MARGIN AND POSITION SIZING LAB](./00_QUOTES_MARGIN_AND_POSITION_SIZING_LAB.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
