# 04 — Applied Economics

Applied Economics dùng theory từ Microeconomics, Market Structure/Game Theory và Macroeconomics cùng identification discipline từ Econometrics để phân tích labor, taxation/public policy, trade, development và industries cụ thể. Module này không phải tập hợp case studies. Mỗi chapter phải trả lời đồng thời: **mechanism nào đang hoạt động, estimand nào cần đo, variation nào identify effect, ai chịu incidence, và result có generalize/scale được không?**

## Thứ tự học canonical

1. [Labor Economics](./00_labor_economics.md) — labor demand/supply, human capital, signaling, search/matching, monopsony, minimum wage, unions, discrimination, migration và labor-policy identification.
2. [Public Economics](./01_public_economics.md) — taxation/incidence, redistribution, social insurance, health/education provision, administrative burden, optimal-tax logic và policy evaluation.
3. [International Trade](./02_international_trade.md) — comparative advantage, factor distribution, gravity, firm heterogeneity, tariffs, global value chains, trade adjustment và empirical trade designs.
4. [Development Economics](./03_development_economics.md) — poverty, credit/risk constraints, health/education, structural transformation, infrastructure, institutions/state capacity, industrial policy và scale-up.
5. [Industrial Organization](./04_industrial_organization.md) — demand estimation, substitution, markups, entry, vertical/platform markets, mergers, procurement, innovation và structural/reduced-form IO.

## Applied spine

```text
Economic mechanism
→ treatment / exposure / institutional variation
→ outcome + population
→ estimand
→ identification problem
→ empirical design
→ incidence / distribution
→ equilibrium / dynamics / scale-up
→ policy limits
```

Nếu một chapter chỉ có theory mà không nói data/design, nó chưa đủ applied. Nếu chỉ có empirical correlation mà không có mechanism/counterfactual, nó cũng chưa đủ applied.

## Dependency

Applied Economics nên được đọc sau hoặc song song với:

- [Microeconomics](../01_microeconomics/README.md) cho incentives, welfare và market failures;
- [Market Structure & Game Theory](../02_market_structure_game_theory/README.md) cho strategic interaction, market power và mechanism design;
- [Macroeconomics](../03_macroeconomics/README.md) cho aggregate constraints, fiscal/monetary/open-economy regimes;
- [Econometrics](../05_econometrics/README.md) cho estimands, counterfactuals, OLS/IV/RDD/DiD/time series và robustness.

Folder numbering giữ `04 Applied`, `05 Econometrics`, nhưng implementation order cố ý xây Econometrics trước để module này có evidence discipline ngay từ đầu.

## Evidence contract

Mỗi empirical claim trong Applied Economics phải ghi rõ ít nhất một trong ba trạng thái:

```text
Descriptive evidence
Causal evidence under stated design assumptions
Structural/model-based counterfactual
```

Không trộn ba tầng này.

Một exporter productivity premium là descriptive cho đến khi xử lý selection. Một DiD estimate là causal chỉ nếu parallel trends/counterfactual credible. Một merger simulation là structural counterfactual conditional on estimated demand/conduct assumptions.

## Distribution và general equilibrium

Applied policy gần như luôn tạo winners/losers. Vì vậy average effect không đủ nếu incidence khác mạnh theo income, skill, geography, firm size hoặc market position.

Ngoài ra, effect local/pilot có thể đổi khi scale: wages, prices, rents, firm entry, migration, taxes và political response đều có thể điều chỉnh. Module này phải luôn nêu partial-equilibrium vs general-equilibrium boundary.

## Policy interpretation

Economics có thể estimate consequences, trade-offs và welfare under explicit social assumptions. Một estimate không tự chuyển thành policy recommendation. Policy còn phụ thuộc distributional weights, legal constraints, implementation capacity, rights, political institutions và uncertainty.

## Connections

- [Korea Business & Economy](../../korea_business_economy_knowledge_library/README.md) là case layer để áp dụng labor, trade, industrial policy, firm structure và finance trong bối cảnh Hàn Quốc.
- [Investing](../../investing/README.md) dùng firm/industry/macro results để phân tích assets và companies; không thay thế applied economics.
- [World Geography](../../world_geography/README.md) cung cấp spatial, transport, resource và market-access constraints.
- [World History](../../world_history/README.md) cung cấp institutional/historical sequence nhưng không tự đóng vai causal design.
- [Psychology](../../psychology/README.md) liên quan labor supply, salience, take-up, expectations và behavioral public economics.

## Checklist khi đọc một applied claim

Hãy hỏi: mechanism nào; unit/population nào; outcome/treatment là gì; estimand nào; assignment/source of variation nào; selection/endogeneity nào; design assumptions nào không test được trực tiếp; incidence rơi vào ai; short-run/long-run khác nhau không; equilibrium/scale-up có đổi effect không; result có external validity sang institution khác không.

Applied Economics hoàn tất core khi người đọc không chỉ biết “policy X thường có effect Y”, mà có thể giải thích **vì sao, effect nào được đo, từ variation nào, cho population nào, và kết luận dừng ở đâu**.
