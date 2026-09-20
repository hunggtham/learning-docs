# 05 — Trading & Derivatives

Domain này tập trung vào trading như một hệ thống xác suất có execution cost và portfolio risk, không phải một bộ pattern vào lệnh. Bạn sẽ học từ Forex/risk management tới futures/options/CFD, backtest, execution microstructure, research robustness, volatility và quản trị nhiều strategies.

## Thứ tự đọc

[00_MASTER_TRADING_FOREX_RISK.md](./00_MASTER_TRADING_FOREX_RISK.md) là bản tổng quan dài về chart, market structure, Forex, leverage, margin, position sizing, expectancy, XAUUSD, backtest và journal.

[01_DERIVATIVES_FUTURES_OPTIONS_CFD.md](./01_DERIVATIVES_FUTURES_OPTIONS_CFD.md) giải thích futures, basis, contango/backwardation, options, Greeks, implied volatility, CFD, leverage và hedging.

[02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md](./02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md) nâng sang system design, sample size, overfitting, walk-forward logic, Monte Carlo, MAE/MFE, Sharpe/Sortino/Calmar và risk-of-ruin thinking.

[03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md](./03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md) đi sâu order book, maker/taker, queue priority, spread, slippage, market impact, adverse selection, broker execution, portfolio heat, factor concentration, volatility targeting, expected shortfall và implementation shortfall.

[04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md](./04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md) hoàn thiện research process: hypothesis, in/out-of-sample, walk-forward, look-ahead/survivorship/data-snooping bias, parameter stability, transaction costs, bootstrap/Monte Carlo, strategy degradation, research log, forward test, small-live validation và portfolio of strategies.

[05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md](./05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md) đi sâu options như bài toán probability và convexity: Delta/Gamma/Theta/Vega, realized vs implied volatility, volatility risk premium, skew/smile, term structure, volatility surface, event vol, synthetic positions, spreads, straddles/strangles, collars, dynamic hedging, tail hedges, assignment/pin risk và scenario-grid risk management.

## Sau domain này bạn cần làm được gì?

Bạn cần có khả năng tính position size trước khi vào lệnh, phân biệt signal edge và execution edge, đánh giá một backtest bằng expectancy/drawdown/robustness chứ không chỉ win rate, nhận ra các lệnh và strategies correlated, kiểm soát total risk của trading book, hiểu option payoff dưới nhiều spot/IV/time scenarios và biết khi nào edge có thể đã degradation.

Để gắn trading với market cụ thể, chuyển sang [06_markets_korea_vietnam](../06_markets_korea_vietnam/README.md).