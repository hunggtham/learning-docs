# Economics — Coverage Audit

## Kết luận hiện tại

Economics hiện đã có bốn lớp canonical đủ sâu để đọc liên tục: `00 Foundations`, `01 Microeconomics`, `02 Market Structure & Game Theory` và `03 Macroeconomics`. Macro không còn phải mượn Investing làm giáo trình nền: các nguyên lý general-purpose đã được tách thành canonical chapters, còn `investing/04_economics/` giữ vai trò application layer cho market transmission, liquidity, crisis cases, macro data và nowcasting.

Khoảng trống lớn tiếp theo là `05 Econometrics`, sau đó `04 Applied Economics` và `06 Economic History & Institutions`. Thứ tự triển khai này có chủ đích: Applied Economics chỉ nên mở rộng mạnh sau khi identification, regression và causal inference foundation đã có.

## Coverage matrix

| Module | Trạng thái | Coverage hiện có | Khoảng trống chính |
|---|---|---|---|
| 00 Foundations | Đã có baseline | scarcity, opportunity cost, marginal analysis, incentives, equilibrium, PPF, efficiency/equity, positive/normative, comparative statics | uncertainty formal hơn, institutions và behavioral limits |
| 01 Microeconomics | **Depth pass hoàn tất** | consumer/producer; welfare; externality; public goods/commons; information asymmetry, contracts và principal–agent | advanced general equilibrium, expected utility, intertemporal choice có thể mở rộng sau |
| 02 Market Structure & Game Theory | **Depth pass hoàn tất** | competition/monopoly, market power, oligopoly, Cournot/Bertrand, sequential/repeated games, entry/collusion, auctions, mechanism design | advanced IO estimation và dynamic structural models thuộc Applied/Econometrics |
| 03 Macroeconomics | **Depth pass hoàn tất** | national accounts/measurement; growth/productivity; labor/unemployment/inflation; money/banking/monetary policy; fiscal/business cycles; open economy/FX/crises | advanced DSGE/heterogeneous-agent/structural estimation có thể mở rộng sau; market-specific playbooks giữ ở Investing |
| 04 Applied Economics | Chưa viết | chưa có canonical chapters | labor, public, trade, development, industrial organization và policy cases có causal boundary |
| 05 Econometrics | Chưa viết | statistics background nằm ở Mathematics | measurement, identification, regression, experiments, IV, DiD, panel, time series, robustness và interpretation |
| 06 Economic History & Institutions | Chưa viết | cross-domain material có trong History/Korea/Geography | periodization, institutions, technology, finance, trade, state capacity và comparative cases |

## 01 — Microeconomics depth gate

Canonical sequence:

```text
00 Consumer & Producer Theory
01 Welfare & Market Efficiency
02 Externalities & Policy
03 Public Goods & Common Resources
04 Information Asymmetry & Contracts
```

Depth gate gồm welfare theorem vs fairness; tax incidence qua elasticity; private/social margins; government failure; rivalry/excludability và commons; adverse selection, moral hazard, signaling, screening, principal–agent, incomplete contracts và Bayesian belief.

## 02 — Market Structure & Game Theory depth gate

Canonical sequence:

```text
00 Competition, Monopoly & Market Power
01 Oligopoly & Strategic Interaction
02 Repeated Games, Entry & Collusion
03 Auctions & Mechanism Design
```

Depth gate gồm market definition, markup/elasticity, natural monopoly, price discrimination, Cournot/Bertrand model selection, best response/Nash, credible commitment, repeated-game monitoring, entry deterrence, reputation, winner's curse, revenue equivalence, incentive compatibility, participation constraint và mechanism-design boundary.

## 03 — Macroeconomics depth gate

Canonical sequence:

```text
00 National Accounts & Macro Measurement
01 Long-Run Growth & Productivity
02 Labor, Unemployment & Inflation
03 Money, Banking & Monetary Policy
04 Fiscal Policy & Business Cycles
05 Open Economy, Exchange Rates & Crises
```

Depth gate mới gồm:

- measurement discipline: stock/flow, nominal/real, gross/net, GDP/GNI, price indices, data vintages và revisions;
- long-run growth: Solow transition, productivity, human capital, endogenous growth, convergence, institutions, structural transformation và misallocation;
- labor/inflation: labor-market flows, matching, wage rigidity, expectations, Phillips/NAIRU uncertainty, supply-v-demand inflation và hysteresis;
- monetary system: bank/central-bank balance sheets, deposit creation, capital vs reserves, transmission, real rates, QE, liquidity vs solvency và financial stability;
- fiscal/cycle: state-dependent multipliers, automatic stabilizers, debt dynamics, `r − g`, crowding out/in, accelerator/financial accelerator và policy interaction;
- open economy: balance of payments, `CA = S − I`, nominal/real FX, PPP/UIP/CIP boundaries, trilemma, gross capital flows, currency/maturity mismatch, sudden stops và crisis feedback loops.

Macro general-purpose không duplicate Investing. Các chapter money/fiscal/open-economy cross-link đến `investing/04_economics/` khi người đọc cần liquidity, market monitoring, crisis cases hoặc investment interpretation.

## Tiêu chí chất lượng và dependency

Mỗi chapter mới phải đi từ vấn đề đến intuition, formalism, assumptions, mechanism, prediction/comparative statics, evidence và failure modes. Công thức không được đứng một mình; ký hiệu, domain và điều kiện validity phải đủ để đọc độc lập.

Dependency triển khai ưu tiên hiện tại:

```text
Mathematics
→ Foundations
→ Microeconomics
→ Market Structure & Game Theory
→ Macroeconomics
→ Econometrics foundation
→ Applied Economics
→ Economic History & Institutions
```

Đây là learning route, không phải DAG cứng. History, Geography, Psychology, Korea Business và Investing là bridge layers để test model boundaries.

## Evidence discipline

Economics giữ hai rule bắt buộc:

```text
Model ≠ Evidence
Accounting Identity ≠ Causal Theory
```

Model xác định mechanism, counterfactual và variable cần đo. Identity đảm bảo accounting consistency. Causal claim vẫn cần identification strategy. Một anecdote, concentration ratio, policy timing hay correlation đơn lẻ không đủ để chứng minh market power, fiscal multiplier, monetary-policy effect, external damage hoặc crisis cause.

Macro làm nhu cầu Econometrics rõ hơn vì simultaneity và policy endogeneity xuất hiện ở gần như mọi biến: central bank phản ứng với inflation outlook, fiscal policy phản ứng với recession, exchange rate phản ứng với domestic lẫn global shocks.

## Connection audit

- **Math:** calculus, optimization, probability/statistics, linear algebra, dynamical systems và game theory formalism.
- **History:** World History và Korean History cung cấp sequence về institutions, technology, trade, war, demographics, finance và state capacity.
- **Psychology:** bounded rationality, belief formation, attention và expectation formation.
- **Geography:** resources, transport, spatial interaction, trade networks, development constraints và external exposure.
- **Investing:** application layer cho asset, company, capital flows, liquidity, policy transmission và market monitoring.
- **Korea Business:** case layer cho chaebol, labor, trade, industrial policy, finance và Korean institutions.
- **Computer Science:** auctions, mechanism design, matching, platforms và computational constraints.

## Quy tắc cross-link/migrate từ Investing

Chỉ đưa nội dung vào Economics khi nó có giá trị general-purpose và boundary rõ. Nếu nội dung chủ yếu trả lời “indicator này ảnh hưởng asset/positioning thế nào”, nó tiếp tục ở Investing. Nếu nội dung giải “money creation, current account, debt dynamics hoặc crisis mechanism hoạt động vì sao”, canonical explanation thuộc Economics và Investing nên cross-link về.

Không copy hàng loạt để tạo cảm giác coverage.

## Next audit gates

1. **Mở `05 Econometrics` ngay tiếp theo** theo sequence measurement/data-generating process → identification/counterfactual → regression → experiments → omitted-variable/endogeneity → IV → DiD → panel/fixed effects → RDD nếu phù hợp → time series → robustness/interpretation.
2. Sau Econometrics foundation, mở `04 Applied Economics`: labor → public → trade → development → industrial organization. Mỗi applied chapter phải nêu model, estimand, identification và alternative explanations.
3. `06 Economic History & Institutions` chỉ mở khi macro/applied spine đủ để tránh duplicate chronology của World History hoặc case material của Korea Business.
4. Sau các module chính, quay lại advanced gaps có giá trị thật: intertemporal/uncertainty micro, heterogeneous-agent macro, advanced IO/structural estimation; không mở chỉ để tăng số file.

Chỉ đánh dấu Economics hoàn tất toàn domain khi `04–06` có canonical learning paths, evidence discipline và integration với các domain liên quan.
