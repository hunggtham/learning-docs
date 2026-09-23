# Economics Knowledge Library

`economics/` là thư viện Economics độc lập của repository. Mục tiêu là giải thích cách cá nhân, doanh nghiệp, thị trường, nhà nước và các nền kinh tế lựa chọn và phối hợp dưới điều kiện khan hiếm, thông tin không hoàn hảo và ràng buộc thể chế. Economics ở đây là một domain nền tảng; phần ứng dụng vào tài sản, doanh nghiệp và danh mục vẫn nằm ở [Investing](../investing/README.md).

## Trạng thái hiện tại

Library đang ở giai đoạn **bootstrap**, chưa phải một giáo trình hoàn chỉnh. Ba vùng đầu tiên đã có mặt trong cấu trúc canonical:

- [00 — Foundations](./00_foundations/00_economic_reasoning.md) đã bắt đầu với scarcity, opportunity cost, marginal analysis, incentives, equilibrium, efficiency/equity, positive/normative analysis và comparative statics.
- [01 — Microeconomics](./01_microeconomics/README.md) đã bắt đầu với consumer và producer theory; welfare, market failure và information cần được viết tiếp.
- [02 — Market Structure & Game Theory](./02_market_structure_game_theory/README.md) có bản phác thảo cơ chế và roadmap, nhưng chưa đủ worked examples, evidence, empirical boundary và coverage để đánh dấu hoàn tất.

`03–06` chưa có module độc lập. Trong giai đoạn chuyển tiếp, [Investing Economics](../investing/04_economics/README.md) là nguồn tham chiếu cho macro, monetary system, capital flows, crisis transmission, public debt, demographics, productivity và policy regime trong bối cảnh đầu tư. Không copy hàng loạt nội dung chỉ để đổi vị trí; chỉ migrate khi boundary, prerequisite và internal links đã rõ.

## Learning route và coverage target

Mũi tên biểu thị dependency học tập, không có nghĩa module phía sau đã được viết. Các topic trong mỗi module là coverage target; một topic chỉ được coi là hoàn thành khi có model/assumptions, mechanism, prediction hoặc comparative statics, evidence/giới hạn đo lường và failure modes phù hợp.

```text
00 Foundations

01 Microeconomics
→ consumer
→ producer
→ welfare
→ externality
→ public goods
→ information asymmetry

02 Market Structure & Game Theory
→ perfect competition
→ monopoly
→ oligopoly
→ strategic interaction
→ repeated games
→ auctions
→ mechanism design

03 Macroeconomics
→ national accounts
→ growth
→ unemployment
→ inflation
→ money
→ banking
→ monetary policy
→ fiscal policy
→ business cycle
→ open economy

04 Applied Economics
→ labor
→ public
→ international trade
→ development
→ industrial organization

05 Econometrics
→ identification
→ regression
→ causal inference
→ experiments
→ IV
→ DiD
→ panel
→ time series

06 Economic History & Institutions
```

Trong route này, demand–supply, elasticity, technology, cost và profit là ngôn ngữ nền bên trong consumer/producer; industrial organization được giữ ở Applied Economics vì nó dùng cả market structure lẫn evidence để phân tích ngành và chính sách.

## Các connection làm spine của library

Economics có giá trị nhất khi được đọc như một lớp nối các domain, không như một tập công thức tách rời:

- [Mathematics](../mathematics/README.md) cung cấp calculus, optimization, probability, statistics, linear algebra và dynamical systems cho marginal choice, equilibrium, econometrics và macro dynamics.
- [World History](../world_history/README.md) và [Korean History](../korean_history/README.md) cung cấp sequence về công nghệ, thương mại, chiến tranh, demography, finance và state capacity để kiểm tra giới hạn của mô hình tĩnh.
- [Psychology](../psychology/README.md) mở rộng rational-choice baseline bằng bounded rationality, behavior, belief formation và decision-making.
- [World Geography](../world_geography/README.md) bổ sung không gian, tài nguyên, location, transport, trade networks và development constraints.
- [Investing](../investing/README.md) là application layer cho asset pricing, company analysis, capital flows, risk và policy transmission; không thay thế Economics general-purpose.
- [Korea Business & Economy](../korea_business_economy_knowledge_library/README.md) là case layer để nối theory với chaebol, labor, trade, industrial policy, finance và thể chế kinh tế Hàn Quốc.

Khi một chapter dùng case lịch sử, địa lý, đầu tư hoặc Hàn Quốc, case phải làm rõ mechanism và boundary của mô hình; không được dùng một ví dụ riêng lẻ như bằng chứng cho quy luật phổ quát.

## Quy ước biên soạn

Mỗi chapter đi từ vấn đề cần giải quyết đến intuition, formal model, assumptions, cơ chế nhân quả, prediction/comparative statics, evidence và failure modes. Thuật ngữ quan trọng giữ English keyword và thêm tiếng Hàn khi có liên hệ phù hợp. Positive economics (“điều gì xảy ra?”) phải được tách khỏi normative economics (“nên chọn gì?”), và kết quả cân bằng không được dùng để thay thế cho lịch sử, quyền lực, thể chế hoặc phân phối.

Xem [Coverage Audit](./COVERAGE_AUDIT.md) để theo dõi phần đã bắt đầu, roadmap còn thiếu và các điều kiện migrate từ Investing.
