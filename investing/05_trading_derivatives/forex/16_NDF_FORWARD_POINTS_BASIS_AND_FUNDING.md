# 16 — NDF, forward points, cross-currency basis và funding

Forex institutional depth không dừng ở spot price. Với nhiều corporate, bank và EM exposures, phần kinh tế quan trọng hơn nằm ở **forward points, FX swaps, NDF, collateral và funding basis**. Đây là nơi tỷ giá gặp money market, balance sheet và capital controls.

Mental model:

```text
Spot FX
+ interest-rate differential
+ funding / collateral
+ balance-sheet constraints
+ convertibility / capital controls
→ forward / swap / NDF pricing
```

## 1. Forward price không phải forecast thuần túy

Trong covered-interest-parity intuition, forward rate được nối với spot và hai interest rates.

Với quote A/B, một representation đơn giản:

```text
F = S × (1 + r_B T) / (1 + r_A T)
```

Convention thực tế phụ thuộc day-count, settlement, compounding và quote direction.

Điều quan trọng là:

```text
Forward ≠ market prediction of future spot
```

Forward chứa financing relationship giữa hai currencies.

## 2. Forward points

Forward thường được quote bằng:

```text
Forward = Spot + Forward Points
```

Forward points phản ánh chủ yếu:

- interest-rate differential;
- tenor;
- funding/balance-sheet conditions;
- basis;
- collateral/credit terms;
- liquidity.

Nếu chỉ nhìn outright forward mà không tách spot và points, trader dễ nhầm carry với directional expectation.

## 3. Premium và discount cần đọc theo quote direction

Một currency có thể trade at forward premium hoặc discount tùy pair convention.

Không học thuộc rule ngôn ngữ. Hãy luôn kiểm tra:

```text
Which currency is base?
Which currency is quote?
Which rate is higher?
What tenor?
```

Sau đó mới interpret forward points.

## 4. Covered interest parity

Covered Interest Parity (CIP) là no-arbitrage relationship giữa:

```text
borrow currency A
→ exchange spot into B
→ invest in B
→ lock future FX with forward
```

và return của việc giữ A trực tiếp.

Trong frictionless textbook market, hai paths phải gần equivalent sau hedge.

## 5. Tại sao CIP có thể lệch

Real markets có:

- balance-sheet costs;
- regulatory capital constraints;
- collateral scarcity;
- counterparty limits;
- funding stress;
- transaction costs;
- segmentation;
- dollar-demand shocks.

Do đó forward pricing có thể chứa **cross-currency basis** thay vì chỉ pure rate differential.

## 6. Cross-currency basis

Cross-currency basis là adjustment cần thêm vào textbook parity relationship để khớp actual funding prices.

Trực giác:

```text
Synthetic USD funding via FX swap
may cost more/less than
direct USD funding
```

Nếu demand for synthetic USD funding tăng mạnh trong stress, basis có thể move significantly.

## 7. Basis không phải directional FX signal đơn giản

Basis widening có thể phản ánh:

- funding pressure;
- dealer balance-sheet scarcity;
- hedging demand;
- regulatory quarter/year-end effects;
- currency-specific liquidity.

Nó không có mapping cố định kiểu:

```text
basis more negative → spot must rise/fall
```

Need separate funding market from spot-direction thesis.

## 8. FX swap là funding instrument

FX swap gồm near leg và far leg.

Institution có thể:

```text
exchange currency today
and reverse exchange later
```

để chuyển funding currency trong một horizon xác định.

Vì vậy FX swap turnover rất lớn dù transaction không mang directional FX view.

## 9. FX swap points vs forward points

Trong nhiều market conventions, swap points là difference giữa far-leg exchange rate và near/spot reference.

Terminology có thể khác theo product/vendor, nên phải đọc specification trước khi so sánh series.

## 10. Tenor structure

Funding/forward curve gồm nhiều maturities:

```text
ON / TN
1W
1M
3M
6M
1Y
...
```

Different tenors phản ánh different expected rates, funding demand và balance-sheet pressure.

Một single 3M forward point không đại diện toàn curve.

## 11. Short-dated FX swaps

Overnight/Tom-Next points có thể nhạy mạnh với:

- settlement calendars;
- policy operations;
- quarter-end;
- reserve/funding demand;
- holidays;
- local market liquidity.

Backtest daily carry mà ignore calendar/short-date mechanics có thể sai financing.

## 12. Settlement dates matter

Spot FX có settlement convention theo pair. Forward maturity phụ thuộc:

- spot date;
- business-day calendars của hai currencies;
- modified-following/other conventions;
- holidays.

Date bug có thể làm forward/P&L lệch dù price formula đúng.

## 13. NDF là gì

**Non-Deliverable Forward (NDF)** là forward được cash-settle thay vì trao đổi principal currencies physically at maturity.

Typical structure:

```text
agree notional + forward rate today
→ observe official/fixing/reference rate at maturity
→ settle net difference in settlement currency
```

Thường settlement currency là freely convertible currency như USD, tùy market/product.

## 14. Tại sao NDF tồn tại

NDF phát triển mạnh ở currencies có một hoặc nhiều constraint:

- limited convertibility;
- capital controls;
- onshore access restrictions;
- offshore hedging demand;
- difficulty delivering local currency offshore.

NDF cho phép express/hedge FX risk mà không cần deliver full local-currency principal offshore.

## 15. NDF không phải CFD

NDF là institutional forward structure với fixing và maturity conventions.

CFD/retail rolling FX là product khác về:

- legal form;
- margining;
- maturity;
- settlement;
- counterparty;
- pricing.

Đừng đồng nhất chỉ vì đều cash-settled.

## 16. NDF fixing

NDF settlement phụ thuộc reference/fixing rate defined trong contract.

Need know:

```text
fixing source
fixing time
valuation date
settlement date
quote convention
settlement currency
```

Một backtest NDF mà dùng arbitrary close price thay fixing có thể sai economics.

## 17. NDF P/L intuition

Simplified:

```text
Contracted Forward Rate
vs
Fixing Rate
→ net settlement
```

Exact payout depends quote convention và contract terms.

Không áp spot P/L formula máy móc nếu product uses inverse/alternative convention.

## 18. Onshore vs offshore price discovery

Một currency có onshore deliverable market và offshore NDF market có thể tạo:

```text
onshore spot/forward
↔ offshore NDF
```

Hai markets influence nhau nhưng access, participant set và policy constraints khác.

Lead-lag relation có thể change theo:

- trading hours;
- policy regime;
- market reform;
- stress;
- foreign access.

## 19. Onshore–offshore basis

Difference giữa NDF-implied pricing và onshore pricing có thể phản ánh:

- capital controls;
- convertibility constraints;
- offshore demand;
- domestic liquidity;
- intervention expectation;
- segmentation.

Không gọi mọi difference là arbitrage opportunity; arbitrage path có thể legally/operationally blocked.

## 20. Capital controls phá textbook arbitrage

Textbook arbitrage giả định capital có thể move freely.

Nếu investor không thể freely:

```text
borrow local currency
move funds offshore
access deliverable forward
repatriate proceeds
```

thì price gap có thể persist.

Constraint chính là part of model, không phải “market inefficiency” đơn giản.

## 21. Funding currency và synthetic borrowing

Institution có thể obtain currency funding trực tiếp qua money market hoặc synthetic qua FX swaps/cross-currency swaps.

Compare:

```text
Direct borrowing cost
vs
Synthetic borrowing cost
```

Difference giúp đọc funding stress và basis.

## 22. Dollar funding channel

USD đóng vai trò funding currency toàn cầu.

Trong stress:

```text
USD funding demand ↑
→ FX swap / basis pressure
→ dealer balance-sheet constraints
→ hedging cost changes
```

Spot USD strength có thể đi cùng nhưng không phải algebraically required.

## 23. Central-bank swap lines

Central-bank FX swap lines có thể reduce foreign-currency funding stress bằng cách cung cấp access to central-bank currency liquidity thông qua official channels.

Learning point:

```text
Funding intervention
≠ spot intervention
```

Một policy action nhắm USD funding conditions không nhất thiết nhắm exchange-rate level trực tiếp.

## 24. Collateral matters

Derivative pricing phụ thuộc collateral terms.

Two trades giống payoff nhưng khác:

- collateral currency;
- margin frequency;
- counterparty credit;
- clearing status;

có thể có different valuation/funding economics.

## 25. Dealer balance-sheet constraints

Dealers không có infinite balance sheet.

Quarter-end/year-end regulatory reporting, leverage ratio và risk limits có thể làm:

```text
balance-sheet capacity scarce
→ intermediation expensive
→ basis / spreads move
```

Calendar effects cần caution khi interpreting short sample.

## 26. Corporate hedging demand

Exporter/importer có natural FX exposure.

Forward demand không necessarily forecast:

```text
Exporter sells foreign currency forward
because future receivable exists
```

Flow may be mechanical hedge, not bearish view on that currency.

## 27. Asset-manager hedge ratios

Foreign-bond/equity investors có thể dynamically adjust hedge ratios.

Large changes in hedge demand can affect forward/swap markets even if underlying asset holdings unchanged.

## 28. Hedge return decomposition

For an investor:

```text
Local-asset return
+ spot FX move
+ hedge P/L
+ carry / forward points
+ transaction cost
```

Không report “currency-hedged return” mà ignore hedge roll cost.

## 29. Rolling forwards

Hedge bằng short-tenor forwards requires repeated rolls.

Roll result depends:

- forward curve;
- spot move;
- spread;
- market liquidity;
- timing.

A static one-period model understates operational reality.

## 30. Forward return vs spot return

Strategy research cần xác định object:

```text
spot return?
forward excess return?
retail rolling P/L?
futures return?
NDF return?
```

Các return series không interchangeable.

## 31. Carry from forward discount/premium

Academic FX carry thường construct return từ forward discount/premium.

Retail implementation có thể realize different economics vì:

- broker swap markup;
- triple-swap/calendar rules;
- account currency;
- leverage;
- credit terms.

Bridge từ research instrument sang executable instrument phải explicit.

## 32. Forward curve as information

Forward curve có thể giúp quan sát:

- rate differential;
- basis;
- hedging pressure;
- term structure.

Nhưng không đọc nó như consensus forecast path của spot.

## 33. Data requirements

Institutional study cần fields như:

```text
spot bid/ask
forward points by tenor
money-market rates
OIS / risk-free proxies
cross-currency basis
fixing rates
holiday calendars
collateral convention if relevant
```

Nếu thiếu basis/collateral detail, state approximation rõ ràng.

## 34. Timestamp alignment

Spot, rates và forwards có thể được sampled ở different times.

Using:

```text
spot London close
+ rate New York close
+ forward Asia timestamp
```

có thể manufacture apparent arbitrage.

Need synchronized snapshots or tolerance window.

## 35. Bid/ask parity

No-arbitrage tests nên dùng executable bid/ask, không mid-only.

Mid-price apparent arbitrage có thể disappear after spreads/funding costs.

## 36. Credit and CSA effects

Institutional OTC pricing depends on counterparty and Credit Support Annex (CSA) terms.

A single public forward quote cannot represent every bilateral trade economics exactly.

## 37. NDF backtesting pitfalls

Common errors:

- using spot close instead of official fixing;
- ignoring non-business days;
- assuming onshore deliverability;
- mixing NDF tenors;
- ignoring capital controls;
- using current regime for old history;
- treating offshore NDF as same market as retail CFD.

## 38. Basis backtesting pitfalls

Common errors:

- inconsistent rate benchmarks;
- pre/post benchmark-transition series stitched blindly;
- unsynchronized timestamps;
- wrong quote sign;
- ignoring bid/ask;
- ignoring collateral/funding regime;
- interpreting seasonal balance-sheet effects as structural alpha.

## 39. Research questions worth asking

Good questions:

```text
Does NDF lead onshore spot during local market closure?
Does basis widen around global USD funding stress?
How stable is forward-implied carry after execution cost?
Does hedge demand change around major asset-flow events?
```

Each needs explicit data/identification design.

## 40. Connection to Macro

Cross-link:

- [`04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md`](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [`08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md`](./08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md)
- [`../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md`](../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)
- [`../../../04_economics/README.md`](../../../04_economics/README.md)

Economics owns general monetary/funding mechanism; chapter này owns **FX instrument implementation**.

## 41. Mental checklist

Trước khi interpret forward/NDF/basis, hỏi:

1. Product deliverable hay non-deliverable?
2. Spot/forward quote convention là gì?
3. Tenor và settlement dates?
4. Which interest-rate benchmarks?
5. Is there cross-currency basis?
6. Onshore/offshore access constraints?
7. Which fixing/reference rate?
8. What collateral/counterparty assumptions?
9. Are timestamps synchronized?
10. Is observed flow hedging, funding hay directional speculation?

## 42. Kết luận

Institutional FX pricing không thể hiểu chỉ bằng chart spot. Forward, FX swap, NDF và basis cho thấy Forex đồng thời là **market for relative prices** và **funding infrastructure**.

Nếu không hiểu convertibility, funding và settlement conventions, một researcher có thể gọi một contractual difference là alpha, một capital-control wedge là arbitrage, hoặc một hedging flow là directional signal.
