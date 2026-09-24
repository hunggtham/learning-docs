# Economics — Coverage Audit

## Kết luận hiện tại

Economics hiện đã có năm lớp canonical đủ sâu để đọc liên tục: `00 Foundations`, `01 Microeconomics`, `02 Market Structure & Game Theory`, `03 Macroeconomics` và `05 Econometrics`. Econometrics đã được đưa lên trước Applied Economics để mọi chapter ứng dụng sau này phải nói rõ measurement, estimand, source of variation, identification assumptions và uncertainty thay vì chỉ ghép theory với correlation.

Hai khoảng trống lớn còn lại là `04 Applied Economics` và `06 Economic History & Institutions`. `investing/04_economics/` tiếp tục là application layer cho macro market transmission, liquidity, crisis cases, macro data và nowcasting; canonical theory/measurement giữ ở Economics.

## Coverage matrix

| Module | Trạng thái | Coverage hiện có | Khoảng trống chính |
|---|---|---|---|
| 00 Foundations | Đã có baseline | scarcity, opportunity cost, marginal analysis, incentives, equilibrium, PPF, efficiency/equity, positive/normative, comparative statics | uncertainty formal hơn, institutions và behavioral limits |
| 01 Microeconomics | **Depth pass hoàn tất** | consumer/producer; welfare; externality; public goods/commons; information asymmetry, contracts và principal–agent | advanced general equilibrium, expected utility, intertemporal choice có thể mở rộng sau |
| 02 Market Structure & Game Theory | **Depth pass hoàn tất** | competition/monopoly, market power, oligopoly, Cournot/Bertrand, sequential/repeated games, entry/collusion, auctions, mechanism design | advanced IO estimation/dynamic structural models thuộc Applied/Econometrics advanced |
| 03 Macroeconomics | **Depth pass hoàn tất** | measurement; growth/productivity; labor/inflation; money/banking/monetary policy; fiscal/business cycles; open economy/FX/crises | heterogeneous-agent/advanced DSGE/structural macro có thể mở rộng sau |
| 04 Applied Economics | Chưa viết | chưa có canonical chapters | labor, public, trade, development, industrial organization với theory + estimand + identification |
| 05 Econometrics | **Foundation depth pass hoàn tất** | measurement/estimands; OLS/inference; experiments/selection; IV/RDD; panel/DiD; time series/macro identification; robustness/external validity | advanced causal ML, structural estimation, duration/count/spatial methods có thể mở rộng sau |
| 06 Economic History & Institutions | Chưa viết | cross-domain material có trong History/Korea/Geography | periodization, institutions, technology, finance, trade, state capacity và comparative cases |

## 01 — Microeconomics depth gate

```text
00 Consumer & Producer Theory
01 Welfare & Market Efficiency
02 Externalities & Policy
03 Public Goods & Common Resources
04 Information Asymmetry & Contracts
```

Depth gate gồm welfare theorem vs fairness; tax incidence qua elasticity; private/social margins; government failure; rivalry/excludability và commons; adverse selection, moral hazard, signaling, screening, principal–agent, incomplete contracts và Bayesian belief.

## 02 — Market Structure & Game Theory depth gate

```text
00 Competition, Monopoly & Market Power
01 Oligopoly & Strategic Interaction
02 Repeated Games, Entry & Collusion
03 Auctions & Mechanism Design
```

Depth gate gồm market definition, markup/elasticity, natural monopoly, price discrimination, Cournot/Bertrand model selection, best response/Nash, credible commitment, repeated-game monitoring, entry deterrence, reputation, winner's curse, revenue equivalence, incentive compatibility, participation constraint và mechanism-design boundary.

## 03 — Macroeconomics depth gate

```text
00 National Accounts & Macro Measurement
01 Long-Run Growth & Productivity
02 Labor, Unemployment & Inflation
03 Money, Banking & Monetary Policy
04 Fiscal Policy & Business Cycles
05 Open Economy, Exchange Rates & Crises
```

Depth gate gồm stock/flow, nominal/real và data revisions; Solow/productivity/convergence; labor-market flows/expectations/inflation; bank/central-bank balance sheets; monetary/fiscal transmission and state dependence; debt dynamics; current account/FX/capital-flow/crisis balance sheets.

## 05 — Econometrics depth gate

Canonical sequence:

```text
00 Measurement, Data & Estimands
01 Regression, Prediction & Inference
02 Causal Inference, Experiments & Selection
03 Endogeneity, IV & RDD
04 Panel, Fixed Effects & Difference-in-Differences
05 Time Series, Forecasting & Macro Identification
06 Robustness, External Validity & Research Workflow
```

Depth gate gồm:

- measurement process, sampling/selection, missingness, potential outcomes, ATE/ATT/LATE, DAG/collider/bad controls;
- OLS as projection, omitted-variable bias, overlap, functional form, heteroskedastic/clustered inference và prediction-v-causality boundary;
- randomization, ITT/noncompliance, attrition/spillovers, matching/IPW/doubly robust methods và natural experiments;
- endogeneity, IV relevance/exclusion, weak instruments, LATE, sharp/fuzzy RDD, manipulation và local interpretation;
- panel within variation, unit/time FE, parallel trends, event study, staggered adoption, modern DiD concerns và synthetic control;
- stationarity/unit roots, AR/MA, cointegration, forecasting, VAR/SVAR/local projections, structural shocks, policy endogeneity và real-time vintages;
- threat-specific robustness, falsification, sensitivity/bounds, multiple testing, reproducibility, external validity, scale-up và economic significance.

## Evidence discipline

Economics giữ ba rule bắt buộc:

```text
Model ≠ Evidence
Accounting Identity ≠ Causal Theory
Estimator ≠ Identification Strategy
```

Model xác định mechanism. Identity bảo đảm consistency. Estimator xử lý data theo một rule. Causal claim chỉ credible khi source of variation và assumptions tạo được counterfactual hợp lý.

Không coi `p < 0.05`, high `R²`, large N, many controls, strong first stage hay một event study plot là proof độc lập. Design-specific threats phải được nêu rõ.

## Connection audit

- **Math:** calculus, optimization, probability/statistics, linear algebra và dynamical systems là prerequisite trực tiếp cho econometric inference và macro dynamics.
- **History:** World/Korean History cung cấp institutional shocks, sequences và boundary conditions; historical variation chỉ dùng causal khi assignment story credible.
- **Psychology:** decision-making, expectation formation, survey/behavior measurement và treatment heterogeneity.
- **Geography:** spatial exposure, trade networks, resource shocks và spillovers; geography can be treatment/confounder/instrument tùy design.
- **Investing:** application layer cho assets, liquidity, capital flows, policy transmission và nowcasting; backtests phải tránh look-ahead/revised-data bias.
- **Korea Business:** applied institutional cases cho labor, trade, industrial policy, finance và firm structure.
- **Computer Science:** computational optimization, causal ML, matching/auctions/platform data và reproducible pipelines.

## Quy tắc cho Applied Economics từ đây

Mỗi applied chapter mới phải có tối thiểu:

```text
Economic mechanism / model
→ measurable outcome and treatment/exposure
→ estimand
→ identification problem
→ credible empirical designs / evidence
→ alternative explanations
→ distribution / equilibrium / policy limits
```

Không dùng một paper/correlation/country anecdote như universal proof. Nếu evidence contested, tách finding, design và interpretation.

## Quy tắc cross-link/migrate từ Investing

Nội dung general-purpose về mechanisms/measurement thuộc Economics. Nội dung trả lời market indicator ảnh hưởng asset, positioning, liquidity hoặc trade execution thế nào tiếp tục ở Investing. Cross-link thay vì copy.

## Next audit gates

1. **Mở `04 Applied Economics`** theo labor → public → international trade → development → industrial organization. Mỗi chapter phải sử dụng econometric spine mới và không duplicate Micro/Game Theory.
2. **Mở `06 Economic History & Institutions`** sau Applied foundation: tổ chức theo mechanisms/institutions/comparative cases, không copy chronology của World History.
3. Sau khi `04` và `06` đủ mạnh, mới quay lại advanced gaps: intertemporal/uncertainty micro, heterogeneous-agent macro, structural IO/econometrics, spatial/causal ML nếu chúng phục vụ learning route thực.
4. Ngoài Economics, repo-wide content priority sau pass này quay lại **Research Methods → Sociology** như audit trước, đồng thời Frontend/root audit automation vẫn là structural gaps riêng.

Chỉ đánh dấu Economics hoàn tất toàn domain khi `04` và `06` có canonical paths và integration metadata được đồng bộ.
