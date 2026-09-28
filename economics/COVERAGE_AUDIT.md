# Economics — Coverage Audit

## Kết luận hiện tại

Economics hiện đã có sáu lớp canonical đủ sâu để đọc liên tục: `00 Foundations`, `01 Microeconomics`, `02 Market Structure & Game Theory`, `03 Macroeconomics`, `04 Applied Economics` và `05 Econometrics`. Applied Economics đã được xây sau Econometrics để mọi chapter ứng dụng phải nối theory với estimand, source of variation, identification assumptions, incidence và scale-up thay vì chỉ ghép model với correlation.

Khoảng trống canonical lớn còn lại là `06 Economic History & Institutions`. `investing/04_economics/` tiếp tục là application layer cho macro market transmission, liquidity, crisis cases, macro data và nowcasting; canonical theory/measurement giữ ở Economics.

## Coverage matrix

| Module | Trạng thái | Coverage hiện có | Khoảng trống chính |
|---|---|---|---|
| 00 Foundations | Đã có baseline | scarcity, opportunity cost, marginal analysis, incentives, equilibrium, PPF, efficiency/equity, positive/normative, comparative statics | uncertainty formal hơn, institutions và behavioral limits |
| 01 Microeconomics | **Depth pass hoàn tất** | consumer/producer; welfare; externality; public goods/commons; information asymmetry, contracts và principal–agent | advanced general equilibrium, expected utility, intertemporal choice có thể mở rộng sau |
| 02 Market Structure & Game Theory | **Depth pass hoàn tất** | competition/monopoly, market power, oligopoly, Cournot/Bertrand, sequential/repeated games, entry/collusion, auctions, mechanism design | advanced dynamic/structural games nếu có nhu cầu thực |
| 03 Macroeconomics | **Depth pass hoàn tất** | measurement; growth/productivity; labor/inflation; money/banking/monetary policy; fiscal/business cycles; open economy/FX/crises | heterogeneous-agent/advanced DSGE/structural macro có thể mở rộng sau |
| 04 Applied Economics | **Core depth pass hoàn tất** | labor; public economics; international trade; development; industrial organization | environmental/health/education/urban/spatial can be added only if route needs them |
| 05 Econometrics | **Foundation depth pass hoàn tất** | measurement/estimands; OLS/inference; experiments/selection; IV/RDD; panel/DiD; time series/macro identification; robustness/external validity | causal ML, structural estimation, duration/count/spatial methods are advanced extensions |
| 06 Economic History & Institutions | Chưa viết | cross-domain material có trong History/Korea/Geography | institutions, technology, finance, trade, state capacity, path dependence và comparative cases |

## 04 — Applied Economics depth gate

Canonical sequence:

```text
00 Labor Economics
01 Public Economics
02 International Trade
03 Development Economics
04 Industrial Organization
```

Depth gate gồm:

- **Labor:** derived demand, task substitution/complementarity, labor supply margins, human capital/signaling, search/matching, monopsony, minimum wage, unions, discrimination, migration và equilibrium effects.
- **Public:** tax incidence, taxable-income response, redistribution, social insurance, health/education provision, administrative burden, environmental/corporate/consumption/property taxation và fiscal externalities.
- **Trade:** comparative advantage, factor distribution, gravity, heterogeneous firms, tariffs/quotas, global value chains, trade adjustment, shift-share designs và input-output propagation.
- **Development:** poverty/inequality measurement, credit/risk constraints, health/education, structural transformation, urbanization, infrastructure, institutions/state capacity, aid/cash/industrial policy và scale-up.
- **Industrial Organization:** demand estimation, substitution/diversion, markups, entry, vertical relationships, mergers, procurement, platforms, switching/network effects, innovation và structural counterfactuals.

Applied chapters phải dùng contract sau:

```text
Economic mechanism
→ measurable treatment/exposure + outcome
→ estimand
→ identification problem
→ credible design/evidence
→ incidence/distribution
→ equilibrium/dynamics/scale-up
→ policy/interpretation limits
```

Không coi một paper, raw correlation, exporter premium, concentration ratio hoặc historical anecdote là universal proof.

## Evidence discipline

Giữ ba rule bắt buộc:

```text
Model ≠ Evidence
Accounting Identity ≠ Causal Theory
Estimator ≠ Identification Strategy
```

Thêm một applied rule:

```text
Causal Estimate ≠ Policy Recommendation
```

Policy còn phụ thuộc costs, distributional weights, implementation capacity, legal/institutional constraints, rights, equilibrium response và uncertainty.

## Connection audit

- **Math:** optimization/probability/statistics nền cho models và estimators.
- **History:** sequence và institutional context; không tự đóng vai causal design.
- **Psychology:** behavior, salience, take-up, expectations, heterogeneity.
- **Geography:** spatial exposure, market access, migration, trade/resource shocks và spillovers.
- **Investing:** company/asset/market transmission application layer; không duplicate Applied Economics.
- **Korea Business:** natural case layer cho labor, chaebol, trade, industrial policy và competition structure.
- **Computer Science:** platform markets, auctions, causal computation và reproducible pipelines.

## Next audit gates

1. **Mở `06 Economic History & Institutions`** theo mechanisms thay vì chronology: institutional formation → state capacity/taxation → property/contract systems → money/finance → technology/industrialization → trade/globalization → crises/regime change → comparative development/path dependence.
2. Không copy `world_history/` hoặc `korean_history/`; chỉ cross-link historical sequence và dùng history để test economic mechanisms/institutional persistence.
3. Sau `06`, Economics có thể được coi là complete ở core-domain level. Chỉ quay lại advanced gaps khi có learning value rõ: intertemporal/uncertainty micro, heterogeneous-agent macro, structural IO/econometrics hoặc spatial methods.
4. Sau Economics core, repo-wide content priority quay lại **Research Methods → Sociology**, rồi structural gaps như Frontend canonical entrypoint và audit automation.

Chỉ đánh dấu Economics hoàn tất toàn domain khi `06` có canonical learning path và catalog/integration metadata được đồng bộ.
