# 05 — Trading & Derivatives

Domain này tập trung vào trading như một hệ thống xác suất có execution cost, operational risk và portfolio-level exposure, không phải một collection pattern vào lệnh. Lộ trình đi từ Forex/risk management tới derivatives, systematic research, microstructure, portfolio of strategies và volatility/options chuyên sâu.

## Thứ tự đọc

[00_MASTER_TRADING_FOREX_RISK.md](./00_MASTER_TRADING_FOREX_RISK.md) là bản tổng quan dài về chart, market structure, Forex, leverage, margin, position sizing, expectancy, XAUUSD, backtest, journal và trading psychology.

[01_DERIVATIVES_FUTURES_OPTIONS_CFD.md](./01_DERIVATIVES_FUTURES_OPTIONS_CFD.md) xây nền contract-level từ forwards/futures, notional, margin/variation margin, carry/basis, commodity curves và options payoff tới swaps, interest-rate/cross-currency swaps, TRS, CDS, collateral/netting, wrong-way risk, CFD financing/counterparty, hedge ratios, portfolio sensitivities và scenario-loss sizing.

[02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md](./02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md) biến idea thành production-capable research process: causal hypothesis, point-in-time data, timestamp/data-quality audit, position sizing, expectancy/drawdown, look-ahead/survivorship/data-snooping bias, chronological train/validation/test, purging/embargo intuition, walk-forward, parameter surface, placebo tests, cost/impact/borrow/futures-roll modeling, bootstrap/Monte Carlo, effective sample size, strategy capacity, drift detection, reconciliation, idempotent orders, kill switch và versioned production monitoring.

[03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md](./03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md) đi sâu limit-order book, maker/taker, price-time priority, hidden/dark liquidity, opening/closing auctions, market/limit/stop behavior, spread/slippage/impact/adverse selection, venue fragmentation, TWAP/VWAP/POV execution, broker/latency risk, liquidation cascades, implementation shortfall/TCA, factor aggregation, portfolio heat, gross/net exposure, stress testing, operational reconciliation và kill-switch engineering.

[04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md](./04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md) tập trung vào robustness ở research level: hypothesis, multiple-testing problem, parameter stability, out-of-sample evidence, regime dependence, confidence interval, bootstrap/Monte Carlo, strategy degradation, capacity và cách kết hợp nhiều strategies mà không nhân đôi cùng một beta/carry/short-vol factor.

[05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md](./05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md) đi sâu options như bài toán phân phối xác suất và state-contingent risk: forward/carry, Delta/Gamma/Theta/Vega và higher-order Greeks, IV vs realized, volatility risk premium, skew/risk reversal/curvature, term structure và surface dynamics, vol-of-vol, complex spreads, gamma scalping, assignment/pin/jump risk, dollar Greeks, margin path, beta/FX hedging, tail-hedge budget, option-data/backtest difficulty và scenario-grid attribution.

## Sau domain này bạn cần làm được gì?

Bạn cần có khả năng đọc một derivative bằng `underlying → payoff → notional/sensitivity → margin/collateral → carry/basis → liquidity/expiry → counterparty`, xác định economic hypothesis trước khi code, tính risk/position size trước entry, phân biệt signal edge với execution leakage, đánh giá backtest bằng out-of-sample/robustness/path uncertainty thay vì win rate, quản lý correlated exposures ở cấp book và đưa strategy từ research sang small-live/production với order-safety, reconciliation và kill switch.

Với options, bạn cần đọc một position bằng `direction + volatility + time + convexity + liquidity + margin`, hiểu vì sao delta-neutral không đồng nghĩa low-risk, và stress P/L trên nhiều spot/IV/time states trước khi giao dịch.

Để gắn research/trading với market cụ thể, chuyển sang [06_markets_korea_vietnam](../06_markets_korea_vietnam/README.md).