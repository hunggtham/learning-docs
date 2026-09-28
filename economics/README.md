# Economics Knowledge Library

`economics/` là thư viện Economics độc lập của repository. Mục tiêu là giải thích cách cá nhân, doanh nghiệp, thị trường, nhà nước và các nền kinh tế lựa chọn và phối hợp dưới điều kiện khan hiếm, thông tin không hoàn hảo và ràng buộc thể chế. Economics ở đây là domain nền tảng; phần ứng dụng vào tài sản, doanh nghiệp và danh mục vẫn nằm ở [Investing](../investing/README.md).

## Trạng thái hiện tại

Library hiện đã có sáu lớp canonical đủ để đọc liên tục:

- [00 — Foundations](./00_foundations/00_economic_reasoning.md) — scarcity, opportunity cost, marginal analysis, incentives, equilibrium, efficiency/equity và comparative statics.
- [01 — Microeconomics](./01_microeconomics/README.md) — consumer/producer theory → welfare → externality → public goods/common resources → information asymmetry/contracts.
- [02 — Market Structure & Game Theory](./02_market_structure_game_theory/README.md) — competition/monopoly → oligopoly → repeated games/entry/collusion → auctions/mechanism design.
- [03 — Macroeconomics](./03_macroeconomics/README.md) — measurement → growth → labor/inflation → money/banking/monetary policy → fiscal/business cycles → open economy/crises.
- [04 — Applied Economics](./04_applied_economics/README.md) — labor → public economics → international trade → development → industrial organization, với theory + estimand + identification + incidence/equilibrium boundary.
- [05 — Econometrics](./05_econometrics/README.md) — measurement/estimand → regression → experiments/selection → IV/RDD → panel/DiD → time series/macro identification → robustness/external validity.

`06 Economic History & Institutions` là khoảng trống canonical lớn còn lại. Sau khi lớp này hoàn tất, các advanced expansions chỉ nên mở khi phục vụ learning route thực thay vì tăng số file.

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

## Applied route

```text
Labor
→ taxation / redistribution / social insurance
→ international trade
→ development
→ industrial organization
```

Applied chapter chỉ đạt chuẩn khi có đủ:

```text
mechanism / model
→ treatment/exposure + outcome
→ estimand
→ identification problem
→ empirical design
→ incidence / distribution
→ equilibrium / dynamics / scale-up
→ interpretation limits
```

## Các connection làm spine của library

- [Mathematics](../mathematics/README.md): calculus, optimization, probability/statistics, linear algebra và dynamical systems.
- [World History](../world_history/README.md) + [Korean History](../korean_history/README.md): technology, trade, institutions, war, demographics, finance và state capacity qua thời gian.
- [Psychology](../psychology/README.md): bounded rationality, behavior, salience, expectations và decision-making.
- [World Geography](../world_geography/README.md): resources, location, transport, spatial interaction, market access và trade networks.
- [Investing](../investing/README.md): asset/company/capital-flow application layer.
- [Korea Business & Economy](../korea_business_economy_knowledge_library/README.md): case layer cho labor, chaebol, trade, industrial policy và Korean institutions.
- [Computer Science](../computer_science/README.md): auctions, mechanism design, platforms, matching, optimization và computational methods.

Case ở domain khác phải làm rõ mechanism/boundary; không dùng một historical/country/company example như universal proof.

## Quy ước biên soạn

Mỗi chapter đi từ vấn đề → intuition → formal model/estimand → assumptions → mechanism → prediction → evidence/identification → failure modes → connections. Thuật ngữ quan trọng giữ English keyword và thêm tiếng Hàn khi phù hợp.

Giữ ba rule xuyên suốt:

```text
Model ≠ Evidence
Accounting Identity ≠ Causal Theory
Estimator ≠ Identification Strategy
```

Positive economics phải tách khỏi normative judgment. Estimate causal effect cũng không tự động trở thành policy recommendation: distributional weights, implementation capacity, rights, legal constraints và uncertainty vẫn là tầng riêng.

Xem [Coverage Audit](./COVERAGE_AUDIT.md) để theo dõi depth gate và khoảng trống còn lại.
