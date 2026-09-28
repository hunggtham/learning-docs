# Economics Knowledge Library

`economics/` là thư viện Economics độc lập của repository. Mục tiêu là giải thích cách cá nhân, doanh nghiệp, thị trường, nhà nước và các nền kinh tế lựa chọn và phối hợp dưới điều kiện khan hiếm, thông tin không hoàn hảo và ràng buộc thể chế. Economics ở đây là domain nền tảng; phần ứng dụng vào tài sản, doanh nghiệp và danh mục vẫn nằm ở [Investing](../investing/README.md).

## Trạng thái hiện tại

Library hiện đã có bốn lớp canonical đủ để đọc liên tục:

- [00 — Foundations](./00_foundations/00_economic_reasoning.md) xây reasoning baseline: scarcity, opportunity cost, marginal analysis, incentives, equilibrium, efficiency/equity, positive/normative analysis và comparative statics.
- [01 — Microeconomics](./01_microeconomics/README.md) đi từ consumer/producer theory → welfare → externality → public goods/common resources → information asymmetry/contracts.
- [02 — Market Structure & Game Theory](./02_market_structure_game_theory/README.md) đi từ competition/monopoly → oligopoly/strategic interaction → repeated games/entry/collusion → auctions/mechanism design.
- [03 — Macroeconomics](./03_macroeconomics/README.md) đi từ national accounts/measurement → long-run growth → labor/inflation → money/banking/monetary policy → fiscal/business cycles → open economy/exchange rates/crises.

`04 Applied Economics`, `05 Econometrics` và `06 Economic History & Institutions` vẫn là các khoảng trống chính. [`investing/04_economics/`](../investing/04_economics/README.md) tiếp tục giữ application layer cho macro data, liquidity, market transmission, crisis cases, policy regimes và nowcasting; Economics chỉ cross-link thay vì copy các nội dung đó.

## Learning route và coverage target

Mũi tên biểu thị dependency học tập, không có nghĩa module phía sau đã được viết. Một topic chỉ được coi là hoàn thành khi có intuition, model/assumptions, mechanism, comparative statics hoặc prediction, evidence boundary và failure modes phù hợp.

```text
00 Foundations

01 Microeconomics
→ consumer & producer
→ welfare & market efficiency
→ externalities & policy
→ public goods & common resources
→ information asymmetry & contracts

02 Market Structure & Game Theory
→ competition & monopoly
→ oligopoly & strategic interaction
→ repeated games, entry & collusion
→ auctions & mechanism design

03 Macroeconomics
→ national accounts & measurement
→ long-run growth & productivity
→ labor, unemployment & inflation
→ money, banking & monetary policy
→ fiscal policy & business cycles
→ open economy, exchange rates & crises

05 Econometrics
→ measurement
→ identification
→ regression
→ experiments / quasi-experiments
→ IV
→ DiD
→ panel
→ time series

04 Applied Economics
→ labor
→ public
→ international trade
→ development
→ industrial organization

06 Economic History & Institutions
```

Econometrics được đặt trước Applied Economics trong **thứ tự triển khai tiếp theo**, dù numbering vẫn giữ `04` và `05`, vì applied case không nên phát triển thành narrative thiếu identification discipline.

Demand–supply, elasticity, technology, cost và profit là ngôn ngữ nền nằm bên trong Microeconomics; chúng không được tách thành formula notes. Industrial organization được giữ ở Applied Economics vì nó dùng cả market-structure theory lẫn empirical evidence để phân tích industry và policy.

## Các connection làm spine của library

Economics có giá trị nhất khi được đọc như một lớp nối các domain, không như một tập công thức tách rời:

- [Mathematics](../mathematics/README.md) cung cấp calculus, optimization, probability, statistics, linear algebra và dynamical systems cho marginal choice, equilibrium, game theory, econometrics và macro dynamics.
- [World History](../world_history/README.md) và [Korean History](../korean_history/README.md) cung cấp sequence về công nghệ, thương mại, chiến tranh, demography, finance và state capacity để kiểm tra giới hạn của mô hình tĩnh.
- [Psychology](../psychology/README.md) mở rộng rational-choice baseline bằng bounded rationality, behavior, belief formation và decision-making.
- [World Geography](../world_geography/README.md) bổ sung không gian, tài nguyên, location, transport, trade networks và development constraints.
- [Investing](../investing/README.md) là application layer cho asset, company, capital-flow và policy transmission; không thay thế Economics general-purpose.
- [Korea Business & Economy](../korea_business_economy_knowledge_library/README.md) là case layer để nối theory với chaebol, labor, trade, industrial policy, finance và thể chế kinh tế Hàn Quốc.
- [Computer Science](../computer_science/README.md) liên quan trực tiếp ở auctions, mechanism design, platform markets, matching, optimization và computational constraints.

Khi một chapter dùng case lịch sử, địa lý, đầu tư hoặc Hàn Quốc, case phải làm rõ mechanism và boundary của mô hình; không được dùng một ví dụ riêng lẻ như bằng chứng cho quy luật phổ quát.

## Quy ước biên soạn

Mỗi chapter đi từ vấn đề cần giải quyết đến intuition, formal model, assumptions, cơ chế nhân quả, prediction/comparative statics, evidence và failure modes. Thuật ngữ quan trọng giữ English keyword và thêm tiếng Hàn khi có liên hệ phù hợp. Positive economics (“điều gì xảy ra?”) phải được tách khỏi normative economics (“nên chọn gì?”), và kết quả cân bằng không được dùng để thay thế cho lịch sử, quyền lực, thể chế hoặc phân phối.

Không coi model là evidence. Model nói variable nào cần quan sát và counterfactual nào có ý nghĩa; Econometrics quyết định data có đủ để identify causal effect hay không. Với macro, accounting identity cũng không được dùng như causal explanation nếu chưa có behavioral mechanism và regime assumptions.

Xem [Coverage Audit](./COVERAGE_AUDIT.md) để theo dõi phần đã hoàn thiện, phần còn thiếu và các điều kiện migrate/cross-link với Investing.
