# 05 — Trading & Derivatives

Domain này tập trung vào trading như một hệ thống xác suất có execution cost, operational risk, collateral/margin constraints và portfolio-level exposure, không phải collection pattern vào lệnh. Lộ trình đi từ Forex/risk management tới derivative contracts, systematic research, market microstructure, portfolio of strategies và options/volatility chuyên sâu.

## Thứ tự đọc

[00_MASTER_TRADING_FOREX_RISK.md](./00_MASTER_TRADING_FOREX_RISK.md) là bản tổng quan dài về chart, market structure, Forex, leverage, margin, position sizing, expectancy, XAUUSD, backtest, journal và trading psychology.

[01_DERIVATIVES_FUTURES_OPTIONS_CFD.md](./01_DERIVATIVES_FUTURES_OPTIONS_CFD.md) xây contract-level framework từ forwards/futures, notional, initial/maintenance/variation margin, basis, carry/roll, commodity curves, CTD và settlement tới options core, swaps/OIS/cross-currency swaps/TRS, CDS/credit indices, variance-swap intuition, CFD financing, collateral/netting/wrong-way risk, multi-asset hedge ratios, expiry/roll management, aggregate sensitivities và margin/liquidity stress testing.

[02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md](./02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md) biến idea thành production-capable research process: causal hypothesis, point-in-time data, timestamp/data-quality audit, expectancy/drawdown, look-ahead/survivorship/data-snooping bias, train/validation/test, purging/embargo intuition, walk-forward, parameter surface, placebo tests, transaction/impact/borrow/futures-roll modeling, bootstrap/Monte Carlo, effective sample size, capacity, drift detection, reconciliation, idempotent orders, kill switch và versioned production monitoring.

[03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md](./03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md) đi sâu price-time/queue priority, maker/taker, market/limit/stop/time-in-force, partial/multi-leg fills, quoted/effective/realized spread, depth/hidden/dark liquidity, auctions, venue fragmentation, slippage/impact/capacity, TWAP/VWAP/POV/implementation-shortfall algorithms, adverse selection, price discovery, liquidation cascades, latency/data/API/reconciliation safety, factor/gross/net/Delta/DV01/volatility aggregation, VaR/ES/stress, TCA, fill-probability và adverse-selection diagnostics.

[04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md](./04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md) tập trung vào robustness ở research level: hypothesis, multiple-testing problem, parameter stability, out-of-sample evidence, regime dependence, confidence interval, bootstrap/Monte Carlo, strategy degradation, capacity và cách kết hợp nhiều strategies mà không nhân đôi cùng beta/carry/short-vol factor.

[05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md](./05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md) đi sâu options như bài toán phân phối xác suất và state-contingent risk: forward/carry, Delta/Gamma/Theta/Vega và higher-order Greeks, IV vs realized, volatility risk premium, skew/risk reversal/curvature, term structure/surface dynamics, vol-of-vol, gamma scalping, assignment/pin/jump risk, dollar Greeks, tail-hedge budget, option-data/backtest difficulty và scenario-grid attribution.

## Sau domain này bạn cần làm được gì?

Bạn cần có khả năng đọc một derivative bằng `underlying → payoff → notional/sensitivity → carry/basis → margin/collateral → liquidity/expiry → counterparty/settlement → portfolio interaction`, đồng thời hiểu rằng một strategy chỉ có edge khi signal vẫn dương sau spread, slippage, impact, financing và operational failures. Bạn cũng phải aggregate risk ở cấp book theo beta/FX/rates/volatility/liquidity thay vì đếm trades, stress cả P/L lẫn margin/liquidity, và dùng TCA/reconciliation để phân biệt lỗi signal với lỗi execution.

Với options, bạn cần đọc position bằng `direction + volatility + time + convexity + liquidity + margin`, hiểu vì sao delta-neutral không đồng nghĩa low-risk, và stress P/L trên nhiều spot/IV/time states trước khi giao dịch.

Để gắn research/trading với market cụ thể, chuyển sang [06_markets_korea_vietnam](../06_markets_korea_vietnam/README.md).