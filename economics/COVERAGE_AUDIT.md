# Economics — Coverage Audit

## Kết luận hiện tại

Economics đã được tách thành một domain canonical ở mức bootstrap. Hai lớp nội dung đầu tiên đã có: economic reasoning và consumer/producer theory. Domain chưa được xem là hoàn tất; các nhánh market structure, game theory, macro độc lập, applied fields, econometrics và economic history vẫn là roadmap.

Quyết định kiến trúc hiện tại là **tách boundary trước, migrate nội dung sau**. `investing/04_economics/` tiếp tục là nguồn tham chiếu cho macro/policy/market-transmission trong bối cảnh đầu tư. Không tạo bản sao chỉ vì hai library cùng dùng thuật ngữ Economics.

## Coverage matrix

| Module | Trạng thái | Nội dung đã có | Khoảng trống chính |
|---|---|---|---|
| 00 Foundations | Đã bắt đầu | scarcity, opportunity cost, marginal analysis, incentives, equilibrium, PPF, efficiency/equity, positive/normative, comparative statics | uncertainty formal hơn, institutions và behavioral limits |
| 01 Microeconomics | Đã bắt đầu | budget, preferences, utility, MRS, income/substitution effects, demand, elasticity, technology, cost, profit, supply, externality boundary | welfare theorem, public goods, asymmetric information, labor choice |
| 02 Market Structure & Game Theory | Chưa viết | Đã có roadmap | competition, monopoly, oligopoly, auctions, repeated games, mechanism design |
| 03 Macroeconomics | Cross-link trước | Macro sâu trong `investing/04_economics/` | national accounts và macro sequence độc lập ngoài investment framing |
| 04 Applied Fields | Chưa viết | Chưa có chapter riêng | labor, public, international trade, development, industrial organization |
| 05 Econometrics | Chưa viết | Mathematics cung cấp probability/statistics | identification, regression, causal inference, panel, time series, robustness |
| 06 Economic History & Institutions | Chưa viết | Có case rải ở history và Korea Business | periodization, institutional change, technology, finance, trade và state capacity |

## Đánh giá chất lượng

- **Boundary:** đạt. README Investing và catalog đã nói rõ phần nào thuộc Economics general-purpose, phần nào vẫn phục vụ investment.
- **Dependency:** đạt ở mức foundation. Mathematics là prerequisite; psychology, history, Korea Business và Investing là các bridge, không phải prerequisite bắt buộc.
- **Causal reasoning:** đạt ở hai module đầu. Mỗi mô hình được yêu cầu nêu objective, constraint, mechanism và assumption.
- **Empirical discipline:** chưa đủ. Econometrics và evidence policy còn phải xây riêng; không nên biến các ví dụ mô hình thành claim thực chứng.
- **Coverage:** chưa hoàn tất. Chưa được gắn nhãn complete cho đến khi có ít nhất một learning path cho market structure/game theory, macro, applied fields và econometrics.

## Quy tắc migrate từ Investing

Chỉ migrate một chapter khi:

1. nội dung có giá trị general-purpose ngoài quyết định đầu tư;
2. boundary và prerequisite đã viết rõ;
3. internal links trong Investing có thể redirect mà không tạo vòng lặp;
4. các ví dụ asset-market được thay bằng ví dụ tổng quát hoặc đặt ở phần bridge;
5. không làm mất context macro/policy cần thiết cho investment.

## Next audit gate

Gate tiếp theo là hoàn thiện welfare, externalities, public goods và asymmetric information trong Microeconomics, sau đó mới mở Market Structure & Game Theory. Mỗi module mới phải có README, ít nhất một chapter cơ chế, checklist assumptions và liên kết ngược tới module prerequisite.
