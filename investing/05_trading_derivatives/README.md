# 05 — Trading & Derivatives

Domain này tập trung vào trading như một hệ thống xác suất có execution cost và portfolio risk, không phải một bộ pattern vào lệnh. Bạn sẽ học từ Forex/risk management tới futures/options/CFD, backtest, execution microstructure và quản trị nhiều vị thế.

## Thứ tự đọc

[00_MASTER_TRADING_FOREX_RISK.md](./00_MASTER_TRADING_FOREX_RISK.md) là bản tổng quan dài về chart, market structure, Forex, leverage, margin, position sizing, expectancy, XAUUSD, backtest và journal.

[01_DERIVATIVES_FUTURES_OPTIONS_CFD.md](./01_DERIVATIVES_FUTURES_OPTIONS_CFD.md) giải thích futures, basis, contango/backwardation, options, Greeks, implied volatility, CFD, leverage và hedging.

[02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md](./02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md) nâng sang system design, sample size, overfitting, walk-forward logic, Monte Carlo, MAE/MFE, Sharpe/Sortino/Calmar và risk-of-ruin thinking.

[03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md](./03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md) đi sâu order book, maker/taker, queue priority, spread, slippage, market impact, adverse selection, broker execution, portfolio heat, factor concentration, volatility targeting, expected shortfall và implementation shortfall.

## Sau domain này bạn cần làm được gì?

Bạn cần có khả năng tính position size trước khi vào lệnh, phân biệt signal edge và execution edge, đánh giá một backtest bằng expectancy/drawdown chứ không chỉ win rate, nhận ra các lệnh correlated và quản trị tổng risk của trading book. Bạn cũng cần hiểu khi nào không nên trade vì liquidity, news, broker hoặc system conditions bất thường.

Để gắn trading với market cụ thể, chuyển sang [06_markets_korea_vietnam](../06_markets_korea_vietnam/README.md).