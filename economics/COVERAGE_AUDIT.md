# Economics — Coverage Audit

## Kết luận hiện tại

Economics đã có canonical boundary và hiện đã hoàn thiện tương đối sâu ba lớp đầu: `00 Foundations`, `01 Microeconomics` và `02 Market Structure & Game Theory`. Hai module sau không còn ở trạng thái skeleton: chúng đã có learning path, model assumptions, welfare/policy boundary, failure modes và cross-links đủ để đọc liên tục.

Khoảng trống lớn tiếp theo nằm ở `03 Macroeconomics`, `04 Applied Economics`, `05 Econometrics` và `06 Economic History & Institutions`. `investing/04_economics/` tiếp tục là nguồn tham chiếu tạm thời cho macro/policy trong bối cảnh đầu tư; không copy hàng loạt nội dung sang Economics nếu chưa tách được boundary general-purpose.

## Coverage matrix

| Module | Trạng thái | Coverage hiện có | Khoảng trống chính |
|---|---|---|---|
| 00 Foundations | Đã có baseline | scarcity, opportunity cost, marginal analysis, incentives, equilibrium, PPF, efficiency/equity, positive/normative, comparative statics | uncertainty formal hơn, institutions và behavioral limits |
| 01 Microeconomics | **Depth pass hoàn tất** | consumer/producer; welfare theorems, surplus, tax incidence; externality; public goods/commons; information asymmetry, contracts và principal–agent | advanced general equilibrium, uncertainty/expected utility, intertemporal choice có thể mở rộng sau |
| 02 Market Structure & Game Theory | **Depth pass hoàn tất** | competition/monopoly, market power, oligopoly, Cournot/Bertrand, sequential/repeated games, entry/collusion, auctions, mechanism design | advanced IO estimation và dynamic structural models thuộc Applied/Econometrics |
| 03 Macroeconomics | Chưa có module độc lập | reference rải rác trong Investing | national accounts → growth → labor/inflation/money/banking → policy → cycle → open economy |
| 04 Applied Economics | Chưa viết | chưa có canonical chapters | labor, public, trade, development, industrial organization và policy cases có causal boundary |
| 05 Econometrics | Chưa viết | statistics background nằm ở Mathematics | identification, regression, experiments, IV, DiD, panel, time series, robustness, interpretation |
| 06 Economic History & Institutions | Chưa viết | cross-domain material có trong History/Korea/Geography | periodization, institutions, technology, finance, trade, state capacity và comparative cases |

## Nội dung vừa được nâng độ sâu

### 01 — Microeconomics

Canonical sequence hiện là:

```text
00 Consumer & Producer Theory
01 Welfare & Market Efficiency
02 Externalities & Policy
03 Public Goods & Common Resources
04 Information Asymmetry & Contracts
```

Depth gate đã được bổ sung ở các điểm trước đây còn thiếu: welfare theorem không bị đồng nhất với fairness; tax incidence được nối với elasticity; externality phân biệt private/social margins và government failure; public goods phân biệt rivalry/excludability và commons; information asymmetry đi qua adverse selection, moral hazard, signaling, screening, principal–agent, incomplete contracts và Bayesian belief.

### 02 — Market Structure & Game Theory

Canonical sequence hiện là:

```text
00 Competition, Monopoly & Market Power
01 Oligopoly & Strategic Interaction
02 Repeated Games, Entry & Collusion
03 Auctions & Mechanism Design
```

Depth gate đã được bổ sung ở market definition, markup/elasticity, natural monopoly, price discrimination, Cournot/Bertrand model selection, best response/Nash, credible commitment, repeated-game monitoring, entry deterrence, reputation, winner's curse, revenue equivalence, incentive compatibility, participation constraint và mechanism-design boundary.

## Tiêu chí chất lượng và dependency

Mỗi chapter mới phải đi từ vấn đề đến intuition, formalism, assumptions, mechanism, prediction/comparative statics, evidence và failure modes. Công thức không được đứng một mình; ký hiệu, domain và điều kiện validity phải đủ để đọc độc lập.

Dependency ưu tiên hiện tại:

```text
Mathematics
→ Foundations
→ Microeconomics
→ Market Structure & Game Theory
→ Macroeconomics
→ Applied Economics
→ Econometrics
→ Economic History & Institutions
```

Đây là learning route, không phải DAG cứng. Econometrics có thể học song song từ sớm nếu cần kiểm tra empirical claim; History, Geography, Psychology và Investing là bridge layers để test model boundaries.

## Evidence discipline

Từ depth pass này trở đi, Economics phải giữ rule rõ:

```text
Model ≠ Evidence
```

Model xác định mechanism, counterfactual và variable cần đo. Evidence cần identification strategy. Một anecdote, concentration ratio hoặc correlation đơn lẻ không đủ để chứng minh market power, collusion, external damage hay causal policy effect.

Đây là lý do `05 Econometrics` trở thành gate quan trọng trước khi mở rộng nhiều case trong `04 Applied Economics`.

## Connection audit

- **Math:** calculus, optimization, probability/statistics, linear algebra, dynamical systems và game theory formalism là nền cho marginal choice, equilibrium, strategic interaction, econometrics và macro.
- **History:** World History và Korean History cung cấp sequence về thể chế, công nghệ, thương mại, chiến tranh, demography, finance và state capacity.
- **Psychology:** bounded rationality, belief formation, attention và behavior mở rộng rational-choice baseline.
- **Geography:** location, resources, transport, spatial interaction, trade networks và development constraints tạo context cho production và inequality.
- **Investing:** application layer cho asset, company, capital-flow và policy transmission; không phải nơi thay thế Economics general-purpose.
- **Korea Business:** case layer để kiểm tra theory qua chaebol, labor, trade, industrial policy, finance và institutions của Hàn Quốc.
- **Computer Science:** relevant với auctions, mechanism design, platform markets, matching và computational constraints.

## Quy tắc migrate từ Investing

Chỉ migrate một chapter khi:

1. nội dung có giá trị general-purpose ngoài quyết định đầu tư;
2. boundary và prerequisite đã viết rõ;
3. internal links trong Investing có thể redirect mà không tạo vòng lặp;
4. ví dụ asset-market được thay bằng ví dụ tổng quát hoặc đặt ở bridge section;
5. không làm mất context macro/policy cần thiết cho investment.

## Next audit gates

1. **Mở `03 Macroeconomics`** theo sequence national accounts → growth → unemployment/labor → inflation → money/banking → monetary policy → fiscal policy → business cycle → open economy. Đây là ưu tiên trực tiếp tiếp theo.
2. **Mở `05 Econometrics` sớm ở mức foundation** thay vì đợi cuối: measurement → identification → regression → experiment → IV/DiD → panel/time series. Điều này giúp Applied Economics không phát triển thành case notes thiếu causal discipline.
3. Sau khi macro + econometrics foundation có mặt, mở `04 Applied Economics` theo labor/public/trade/development/industrial organization và buộc mọi case chỉ rõ model + identification.
4. `06 Economic History & Institutions` nên được viết sau khi macro/applied spine đủ rõ để tránh duplicate World History và Korea Business.

Chỉ đánh dấu Economics hoàn tất toàn domain khi `03–06` có canonical learning path, chapter cơ chế đủ sâu, evidence discipline và integration với các domain liên quan.
