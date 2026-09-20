# Case Study 02 — Credit và Liquidity Crisis Transmission

> Case này phân biệt ba thứ thường bị trộn thành một: **market loss**, **liquidity stress** và **solvency problem**. Mục tiêu là theo dõi cách một shock nhỏ ở collateral/funding có thể biến thành forced deleveraging, credit contraction, earnings decline và cuối cùng tác động tới real economy.

## 1. Bối cảnh giả định

Giả sử một nhóm financial institutions nắm lượng lớn long-duration securities funded bằng short-term liabilities. Policy rates đã tăng mạnh trong thời gian dài. Mark-to-market losses tăng nhưng chưa tạo default vì assets vẫn trả cash flow nếu held to maturity.

Sau đó deposit outflow hoặc margin/collateral demand tăng bất ngờ.

Câu hỏi quan trọng không phải “assets có lỗ không?” mà là:

```text
Có đủ liquidity để sống tới khi assets mature không?
```

Đây là khác biệt giữa **mark-to-market loss** và **forced realization loss**.

## 2. Liquidity vs Solvency

**Liquidity problem**: entity có assets có thể đủ giá trị dài hạn nhưng không có cash ngay để đáp ứng withdrawal/collateral.

**Solvency problem**: fair/economic value của assets thấp hơn liabilities đủ lớn để equity bị wipe out.

Một liquidity problem có thể biến thành solvency problem nếu forced selling xảy ra ở fire-sale prices.

```text
Liquidity Stress
→ Forced Sales
→ Lower Asset Prices
→ Larger Mark-to-Market Loss
→ Confidence Loss
→ More Withdrawals
→ Solvency Risk
```

Đọc thêm: [Monetary System, Liquidity and Crisis Transmission](../04_economics/04_MONETARY_SYSTEM_LIQUIDITY_AND_CRISIS_TRANSMISSION.md).

## 3. Duration Mismatch

Một institution funded ngắn nhưng asset duration dài chịu mismatch.

Ví dụ:

```text
Liability: demand deposits / short funding
Asset: 10Y fixed-rate bonds / long mortgages
```

Khi rates tăng, asset market value giảm. Nếu liabilities stable, institution có thể chờ. Nếu funding chạy đi, loss bị crystallized.

Duration risk vì vậy có thể trở thành liquidity risk.

## 4. Deposit Flight và Confidence

Deposit run có thể bắt đầu từ concerns về uninsured balances, social information cascade hoặc visible mark-to-market losses.

Digital banking làm withdrawal speed nhanh hơn historical bank-run intuition. Vì vậy liquidity buffer và funding concentration rất quan trọng.

Một bank có diversified sticky deposits khác bank phụ thuộc vài corporate/wealth clients lớn.

## 5. Repo và Haircut Spiral

Trong secured funding, lender áp haircut lên collateral.

Nếu collateral price giảm hoặc volatility tăng:

```text
Haircut ↑
→ Borrower phải post thêm collateral/cash
→ Asset sales ↑
→ Price ↓ thêm
→ Haircut ↑ thêm
```

Đây là **margin/haircut spiral**.

Đọc thêm: [Cash, Money Markets, Structured and Private Markets](../02_asset_classes/06_CASH_MONEY_MARKETS_STRUCTURED_PRODUCTS_AND_PRIVATE_MARKETS.md).

## 6. Dealer Balance Sheet Constraint

Ngay cả khi asset “cheap”, dealer/intermediary có thể không absorb inventory vì capital, funding hoặc risk limits.

Khi balance-sheet capacity giảm, bid-ask spreads widen và market depth giảm. Price có thể overshoot fundamentals vì intermediary constraint.

Liquidity không chỉ là property của asset; nó còn phụ thuộc balance sheet của người tạo market.

## 7. Credit Spread Widening

Khi uncertainty tăng, corporate spreads widen vì:

```text
Expected default loss ↑
Risk premium ↑
Liquidity premium ↑
Funding uncertainty ↑
```

Spread widening làm debt refinancing đắt hơn, tạo second-round effect lên corporate cash flows.

## 8. Maturity Wall

Company có low current leverage nhưng large maturity wall gần có thể stress mạnh khi market access đóng.

Research cần map:

```text
Cash
Revolver
Free Cash Flow
Debt Maturities
Secured Capacity
Covenant Headroom
Refinancing Rate
```

Đọc thêm: [Earnings Quality, Modeling and Forensics](../03_company_analysis/04_EARNINGS_QUALITY_MODELING_AND_FORENSICS.md).

## 9. Financial Accelerator

Credit conditions ảnh hưởng economy qua feedback loop:

```text
Asset Prices ↓
→ Collateral Value ↓
→ Lending Standards Tighten
→ Borrowing / Investment ↓
→ Growth ↓
→ Earnings ↓
→ Credit Quality ↓
→ Lending Tightens More
```

Đây là **financial accelerator**.

Một shock financial có thể trở thành macro recession dù initial problem ở một niche market.

## 10. Bank Capital vs Liquidity

Capital absorbs losses. Liquidity meets cash outflows. Hai vấn đề khác nhau.

Bank có high capital ratio nhưng vẫn fail nếu funding run cực nhanh và assets illiquid. Ngược lại, central-bank liquidity có thể giúp bank liquid nhưng không sửa economic insolvency nếu asset losses vượt equity.

Policy response phải diagnose đúng problem.

## 11. Central-Bank Liquidity Facilities

Central bank có thể cung cấp funding against eligible collateral, giảm need fire-sale.

Mechanism:

```text
Collateral accepted
→ Cash liquidity supplied
→ Forced sale pressure giảm
→ Funding market stabilize
```

Nhưng liquidity support không tự động xóa credit loss. Nếu underlying borrowers default, economic loss vẫn tồn tại.

## 12. Lender of Last Resort vs Bailout

**Lender of last resort** thường nhằm cung cấp temporary liquidity against collateral.

**Bailout/recapitalization** injects loss-absorbing capital hoặc transfers risk.

Hai actions có distributional/fiscal implications khác nhau. Research note nên phân biệt thay vì gọi mọi intervention là “QE” hoặc “money printing”.

## 13. Sovereign–Bank Nexus

Banks thường nắm sovereign bonds; sovereign dựa banks để finance economy. Trong stress:

```text
Sovereign Risk ↑
→ Bank Asset Value ↓
→ Bank Funding Cost ↑
→ Credit ↓
→ Economy ↓
→ Fiscal Position ↓
→ Sovereign Risk ↑
```

Đây là **sovereign-bank doom loop**.

## 14. Credit vs Government Bonds

Trong classic recessionary credit crisis, government yields có thể fall vì easing/flight to quality, trong khi corporate spreads widen mạnh.

Corporate bond return gần:

```text
Rate Effect + Spread Effect + Carry + Default/Recovery
```

Treasury rally không guarantee corporate bond rally.

Đọc thêm: [Bonds, Rates and Credit](../02_asset_classes/02_BONDS_RATES_AND_CREDIT.md).

## 15. Equity Transmission

Financial stocks thường bị hit trực tiếp qua funding/credit losses. Nhưng second-order effects lan tới:

- property qua refinancing;
- industrials qua capex cut;
- consumer qua tighter credit;
- small caps qua funding dependence;
- brokers qua lower turnover/margin liquidation.

Sector map phải dựa balance-sheet sensitivity, không chỉ beta history.

## 16. Earnings Transmission

Company stress thường đi qua sequence:

```text
Revenue slowdown
→ Margin pressure
→ Working-capital deterioration
→ CFO ↓
→ Interest expense ↑
→ Covenant headroom ↓
→ Capex cut / Asset sale / Dilution
```

Accounting can lag liquidity stress. Balance sheet thường cho early warning hơn EPS.

## 17. Private Credit và Valuation Lag

Private credit/private equity NAV có thể chưa mark down nhanh như public markets.

Reported smoothness không có nghĩa economic risk thấp. Warning signals:

```text
PIK interest ↑
Amend-and-extend ↑
EBITDA add-backs ↑
Covenant resets
Secondary discounts
Delayed exits
```

## 18. Forced Deleveraging

Leveraged funds/traders có thể sell unrelated assets để meet margin calls.

Vì vậy safe/good assets đôi khi giảm cùng risky assets trong early crisis. Correlation spike có thể phản ánh funding need, không change in fundamentals.

## 19. Gold và Cash trong Liquidity Shock

Gold có safe-haven narrative nhưng có thể giảm tạm thời khi investors need cash. USD và T-bills có thể benefit from liquidity demand, tùy shock origin.

Không dùng một-day reaction để kết luận hedge “không hoạt động”. Phải phân biệt first-stage liquidation và later policy response.

## 20. Korea Transmission

Một global dollar/credit squeeze có thể đi nhanh qua Korea:

```text
USD Funding Stress
→ USD/KRW ↑
→ Foreign Risk Reduction
→ Equity/credit pressure
→ Corporate funding tighter
```

Exporters có USD revenue nhưng financing/working-capital effects vary. Highly leveraged domestic sectors có thể chịu indirect pressure.

Đọc thêm: [Korea Market Playbook](../06_markets_korea_vietnam/01_KOREA_MARKET_PLAYBOOK.md).

## 21. Vietnam Transmission

Vietnam có channel khác:

```text
Global Risk-Off / USD ↑
→ VND pressure
→ Policy room tighter
→ Domestic liquidity expectations weaker
→ Property / Broker / Bank risk repriced
```

Domestic bank credit, property bond refinancing và retail margin can dominate local market even when direct global wholesale funding exposure differs Korea.

Đọc thêm: [Vietnam Market Playbook](../06_markets_korea_vietnam/02_VIETNAM_MARKET_PLAYBOOK.md).

## 22. Liquidity Bucket Review

Portfolio stress test không chỉ hỏi mark-to-market loss. Hỏi:

```text
Cash needed next 1 month?
Margin calls under stress?
Which assets can sell same day?
Which can gap/limit down?
Which are private/locked?
Which foreign transfers can delay?
```

Liquidity hierarchy là part of risk budget.

## 23. Reverse Stress Test

Thay vì hỏi “portfolio mất bao nhiêu nếu stocks -20%?”, hỏi:

> Điều gì phải xảy ra để tôi buộc phải bán tài sản tốt ở đáy?

Possible triggers:

```text
Job/income loss
Margin call
Debt repayment
Capital call
Currency mismatch
Broker/custody interruption
```

Reverse stress test giúp phát hiện structural fragility.

## 24. Hedge Design

Nếu risk là rate duration, use duration hedge. Nếu credit spread blowout, Treasury hedge không cover all loss. Nếu liquidity crisis, having cash/T-bills may be more valuable than complex hedge requiring margin.

A hedge can fail operationally even if economic direction correct.

## 25. Option Hedge trong Crisis

Long puts gain convexity nhưng option IV often expensive after stress begins. Buying insurance after fire starts can be costly.

Tail hedge should be evaluated as recurring portfolio insurance budget, not emergency trade improvised at peak panic.

## 26. Execution under Stress

Stress execution features:

```text
Spread wider
Depth thinner
Slippage larger
Correlation higher
Stops gap
Margin requirements rise
```

Position sizing before crisis matters more than perfect exit during crisis.

Đọc thêm: [Execution & Microstructure](../05_trading_derivatives/03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md).

## 27. What Is Priced?

Credit crisis analysis must compare current spreads and equity prices with expected loss path.

A company can be economically weak but bond already price deep default probability. Another can look stable but spread still near cycle tights.

Investment edge lies in distribution vs price, not headline quality alone.

## 28. Crisis Timeline

Một useful framework:

```text
Stage 1: Hidden leverage / maturity mismatch builds
Stage 2: Trigger
Stage 3: Funding / liquidity stress
Stage 4: Forced sales / spread widening
Stage 5: Credit contraction
Stage 6: Earnings / employment deterioration
Stage 7: Policy response
Stage 8: Repair / recapitalization / defaults
```

Assets bottom at different stages. Market price usually leads accounting data.

## 29. Post-Crisis Attribution

Review questions:

```text
Did we identify funding channel early?
Did we confuse liquidity with solvency?
Which balance-sheet indicators led equity price?
Which hedges worked after cost/margin?
Did diversification fail because factors converged?
Was policy response larger/faster than expected?
```

## 30. Reusable Crisis Checklist

```text
Trigger
Funding source
Collateral
Haircuts / Margin
Liquidity buffer
Capital buffer
Maturity wall
Credit spreads
Bank lending standards
FX funding
Policy facilities
Fiscal capacity
Forced sellers
Portfolio liquidity
```

## Kết luận

Credit crisis không bắt đầu và kết thúc ở “bank xấu”. Nó là một network problem giữa leverage, collateral, funding, confidence và policy. Investor cần nhìn balance sheets và cash-flow timing trước khi nhìn headline P/E. Trong crisis, **survival, liquidity và optionality** thường quan trọng hơn việc tối đa hóa expected return.