# Economics Knowledge Library

`economics/` là thư viện Economics độc lập của repository. Mục tiêu là giải thích cách cá nhân, doanh nghiệp, thị trường, nhà nước và các nền kinh tế lựa chọn và phối hợp dưới điều kiện khan hiếm, thông tin không hoàn hảo và ràng buộc thể chế. Economics ở đây là domain nền tảng; phần ứng dụng vào tài sản, doanh nghiệp và danh mục vẫn nằm ở [Investing](../investing/README.md).

## Trạng thái hiện tại

Economics core hiện đã hoàn chỉnh ở cấp canonical learning path:

- [00 — Foundations](./00_foundations/00_economic_reasoning.md) — scarcity, opportunity cost, marginal analysis, incentives, equilibrium, efficiency/equity và comparative statics.
- [01 — Microeconomics](./01_microeconomics/README.md) — consumer/producer theory → welfare → externality → public goods/common resources → information asymmetry/contracts.
- [02 — Market Structure & Game Theory](./02_market_structure_game_theory/README.md) — competition/monopoly → oligopoly → repeated games/entry/collusion → auctions/mechanism design.
- [03 — Macroeconomics](./03_macroeconomics/README.md) — measurement → growth → labor/inflation → money/banking/monetary policy → fiscal/business cycles → open economy/crises.
- [04 — Applied Economics](./04_applied_economics/README.md) — labor → public economics → international trade → development → industrial organization.
- [05 — Econometrics](./05_econometrics/README.md) — measurement/estimand → regression → experiments/selection → IV/RDD → panel/DiD → time series/macro identification → robustness/external validity.
- [06 — Economic History & Institutions](./06_economic_history_institutions/README.md) — institutions/state capacity → money/finance/fiscal states → industrialization/globalization → crises/regime change/path dependence.

Từ đây Economics không còn khoảng trống core bắt buộc. Advanced expansions chỉ nên mở khi phục vụ learning route cụ thể thay vì tăng số file.

[`investing/04_economics/`](../investing/04_economics/README.md) tiếp tục giữ application layer cho macro data, liquidity, market transmission, crisis cases, policy regimes và nowcasting; Economics cross-link thay vì duplicate.

## Learning route

```text
00 Foundations
→ 01 Microeconomics
→ 02 Market Structure & Game Theory
→ 03 Macroeconomics
→ 05 Econometrics foundation
→ 04 Applied Economics
→ 06 Economic History & Institutions
```

Folder numbering phản ánh taxonomy, không ép thứ tự học tuyệt đối. Econometrics được đặt trước Applied Economics trong learning dependency để empirical case không biến thành correlation narrative.

## Depth contract

Một chapter Economics đạt chuẩn khi có:

```text
Problem / question
→ intuition
→ formal model / estimand
→ assumptions
→ mechanism
→ prediction / comparative statics
→ evidence / identification
→ failure modes
→ distribution / equilibrium / institutional boundary
```

Applied chapter thêm incidence và scale-up. Historical chapter thêm enforcement, distribution of power, persistence mechanism và historical-identification limits.

## Các connection làm spine của library

- [Mathematics](../mathematics/README.md): calculus, optimization, probability/statistics, linear algebra và dynamical systems.
- [World History](../world_history/README.md) + [Korean History](../korean_history/README.md): chronology, actors, wars và institutional sequence; Economics không duplicate timeline.
- [Psychology](../psychology/README.md): bounded rationality, behavior, salience, expectations và decision-making.
- [World Geography](../world_geography/README.md): resources, location, transport, spatial interaction, market access và trade networks.
- [Investing](../investing/README.md): asset/company/capital-flow application layer.
- [Korea Business & Economy](../korea_business_economy_knowledge_library/README.md): case layer cho labor, chaebol, trade, industrial policy và Korean institutions.
- [Computer Science](../computer_science/README.md): auctions, mechanism design, platforms, matching, optimization và computational methods.

## Quy ước biên soạn

Giữ bốn rule xuyên suốt:

```text
Model ≠ Evidence
Accounting Identity ≠ Causal Theory
Estimator ≠ Identification Strategy
Causal Estimate ≠ Policy Recommendation
```

Positive economics phải tách khỏi normative judgment. Historical persistence cũng không tự đồng nghĩa path dependence; formal rules cũng không tự đồng nghĩa effective enforcement.

## Sau core

Các advanced topics có thể mở sau khi có nhu cầu rõ: intertemporal/uncertainty micro, heterogeneous-agent macro, structural IO/econometrics, causal ML, spatial economics, environmental/health economics hoặc deeper financial economics. Ưu tiên repo-wide sau core Economics nên quay lại các domain còn mỏng hơn thay vì tiếp tục nở Economics không giới hạn.

Xem [Coverage Audit](./COVERAGE_AUDIT.md) để theo dõi depth gates và next repo-wide priorities.
