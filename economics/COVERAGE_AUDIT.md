# Economics — Coverage Audit

## Kết luận hiện tại

Economics đã có canonical boundary nhưng vẫn ở mức **bootstrap**. Nội dung thực sự hiện có là `00 Foundations`, `01 Microeconomics` và một bản phác thảo/roadmap cho `02 Market Structure & Game Theory`. `03 Macroeconomics`, `04 Applied Economics`, `05 Econometrics` và `06 Economic History & Institutions` chưa có module độc lập hoàn chỉnh.

Quyết định kiến trúc là **tách boundary trước, migrate nội dung sau**. `investing/04_economics/` tiếp tục là nguồn tham chiếu cho macro, monetary system, capital flows, crisis transmission, public debt, demographics, productivity và policy regime trong bối cảnh đầu tư. Không tạo bản sao chỉ vì hai library cùng dùng thuật ngữ Economics.

## Coverage matrix

| Module | Trạng thái | Coverage target | Khoảng trống chính |
|---|---|---|---|
| 00 Foundations | Đã bắt đầu | scarcity, opportunity cost, marginal analysis, incentives, equilibrium, PPF, efficiency/equity, positive/normative, comparative statics | uncertainty formal hơn, institutions và behavioral limits |
| 01 Microeconomics | Đã bắt đầu | consumer, producer, welfare, externality, public goods, information asymmetry | welfare theorem, market failure và policy trade-off chưa có chapter riêng |
| 02 Market Structure & Game Theory | Roadmap / phác thảo chưa hoàn chỉnh | perfect competition, monopoly, oligopoly, strategic interaction, repeated games, auctions, mechanism design | derivation, worked examples, evidence, policy boundary và empirical links |
| 03 Macroeconomics | Chưa có module độc lập; đang cross-link | national accounts, growth, unemployment, inflation, money, banking, monetary policy, fiscal policy, business cycle, open economy | sequence macro tổng quát ngoài investment framing |
| 04 Applied Economics | Chưa viết | labor, public, international trade, development, industrial organization | toàn bộ chapter và case có causal boundary |
| 05 Econometrics | Chưa viết | identification, regression, causal inference, experiments, IV, DiD, panel, time series | measurement, assumptions, robustness và interpretation |
| 06 Economic History & Institutions | Chưa viết | economic history, institutional change, technology, finance, trade và state capacity | periodization, comparative cases và links với History/Geography/Korea |

## Tiêu chí chất lượng và dependency

Mỗi chapter mới phải đi từ vấn đề đến intuition, formalism, assumptions, mechanism, prediction/comparative statics, evidence và failure modes. Công thức không được đứng một mình; ký hiệu, domain và điều kiện validity phải đủ để đọc độc lập. Ví dụ lịch sử, Hàn Quốc, địa lý hoặc đầu tư là application/case layer, không thay thế cho model hoặc bằng chứng.

Dependency hiện tại là Mathematics → Foundations → Microeconomics → Market Structure/Game Theory → Macroeconomics → Applied Economics → Econometrics → Economic History & Institutions. Đây là một learning route ưu tiên, không phải điều kiện cứng cho mọi chapter: History, Geography, Psychology và Investing có thể được đọc song song như bridge layers.

## Connection audit

- **Math:** calculus, optimization, probability/statistics, linear algebra và dynamical systems là nền cho marginal choice, equilibrium, econometrics và macro.
- **History:** World History và Korean History cung cấp sequence về thể chế, công nghệ, thương mại, chiến tranh, demography, finance và state capacity.
- **Psychology:** bounded rationality, belief formation và behavior mở rộng rational-choice baseline.
- **Geography:** location, resources, transport, spatial interaction, trade networks và development constraints tạo context cho production và inequality.
- **Investing:** application layer cho asset, company, capital-flow và policy transmission; không phải nơi thay thế Economics general-purpose.
- **Korea Business:** case layer để kiểm tra theory qua chaebol, labor, trade, industrial policy, finance và institutions của Hàn Quốc.

## Quy tắc migrate từ Investing

Chỉ migrate một chapter khi:

1. nội dung có giá trị general-purpose ngoài quyết định đầu tư;
2. boundary và prerequisite đã viết rõ;
3. internal links trong Investing có thể redirect mà không tạo vòng lặp;
4. ví dụ asset-market được thay bằng ví dụ tổng quát hoặc đặt ở phần bridge;
5. không làm mất context macro/policy cần thiết cho investment.

## Next audit gates

1. Hoàn thiện Microeconomics theo chuỗi welfare → externality → public goods → information asymmetry.
2. Nâng `02` từ skeleton thành module có derivation, evidence và empirical boundary cho đủ bảy topic.
3. Mở Macro độc lập theo national accounts → growth → labor/inflation/money/banking → policy → cycle → open economy, đồng thời cross-link Investing.
4. Viết Applied Economics, Econometrics và Economic History & Institutions theo route trong [README](./README.md).

Chỉ đánh dấu library hoàn tất khi các module mới có learning path, chapter cơ chế, checklist assumptions, evidence discipline và liên kết ngược tới prerequisite tương ứng.
