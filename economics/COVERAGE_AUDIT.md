# Economics — Coverage Audit

## Kết luận hiện tại

Economics core hiện đã hoàn chỉnh ở cấp canonical learning path: `00 Foundations`, `01 Microeconomics`, `02 Market Structure & Game Theory`, `03 Macroeconomics`, `04 Applied Economics`, `05 Econometrics` và `06 Economic History & Institutions` đều có learning spine, depth gate, evidence boundary và cross-domain integration.

Điều này không có nghĩa mọi advanced subfield đã được viết. Nó nghĩa người đọc hiện có một route đầy đủ từ first principles → individual/firm choice → strategic markets → aggregate economy → causal empirical methods → applied fields → institutions/history mà không cần nhảy ra ngoài chỉ để lấp các khái niệm core.

## Coverage matrix

| Module | Trạng thái | Coverage hiện có | Advanced gaps chỉ mở khi cần |
|---|---|---|---|
| 00 Foundations | Canonical baseline | scarcity, opportunity cost, marginal analysis, incentives, equilibrium, PPF, efficiency/equity, positive/normative, comparative statics | uncertainty formal hơn, behavioral/institutional foundations |
| 01 Microeconomics | **Core complete** | consumer/producer; welfare; externality; public goods/commons; information asymmetry/contracts | intertemporal choice, expected utility, general equilibrium |
| 02 Market Structure & Game Theory | **Core complete** | monopoly/competition, oligopoly, Cournot/Bertrand, sequential/repeated games, entry/collusion, auctions/mechanism design | dynamic games, advanced mechanism design |
| 03 Macroeconomics | **Core complete** | measurement; growth; labor/inflation; money/banking; monetary/fiscal policy; business cycles; open economy/crises | heterogeneous-agent macro, advanced DSGE/structural macro |
| 04 Applied Economics | **Core complete** | labor; public; trade; development; industrial organization | environmental, health, education, urban/spatial if needed |
| 05 Econometrics | **Foundation complete** | measurement/estimands; OLS; experiments/selection; IV/RDD; panel/DiD; time series/macro identification; robustness/external validity | causal ML, structural estimation, duration/count/spatial methods |
| 06 Economic History & Institutions | **Core complete** | property/contracts/state capacity; money/finance/fiscal states; industrialization/globalization; crises/regimes/path dependence | deeper regional/period case studies via cross-links, not duplicated chronology |

## 06 — Economic History & Institutions depth gate

Canonical sequence:

```text
00 Institutions, Property Rights & State Capacity
01 Money, Finance & Fiscal States
02 Technology, Industrialization & Globalization
03 Crises, Regime Change & Path Dependence
```

Depth gate gồm:

- formal vs informal institutions; rules vs enforcement; property/contract rights; fiscal/information/legal state capacity; credible commitment; rent-seeking và political power;
- money/payment institutions, banking/clearing, public debt, fiscal capacity, corporate forms, financial deepening, regulation và crisis infrastructure;
- Malthusian constraint, energy, general-purpose technologies, diffusion, factory/management organization, transport, structural transformation, globalization, migration và dynamic comparative advantage;
- leverage/amplification, banking/sovereign/currency crises, policy regimes, reconstruction, Lucas critique, hysteresis, lock-in, multiple equilibria và historical identification.

History is used as a mechanism laboratory. Chronology, political actors and detailed event sequence remain canonical in `world_history/` and `korean_history/`.

## Economics-wide evidence discipline

Giữ bốn rules:

```text
Model ≠ Evidence
Accounting Identity ≠ Causal Theory
Estimator ≠ Identification Strategy
Causal Estimate ≠ Policy Recommendation
```

Historical layer thêm:

```text
Persistence ≠ Path Dependence
Formal Rule ≠ Effective Enforcement
```

Một historical association chỉ trở thành causal claim khi assignment/source of variation và alternative persistent channels được xử lý đủ rõ.

## Integration rules

- **History:** Economics cross-link chronology; không copy timeline.
- **Geography:** geography có thể là constraint, treatment, confounder hoặc instrument; phải nêu mechanism.
- **Psychology:** behavior/expectations/salience bổ sung rational baseline.
- **Investing:** market/asset interpretation giữ ở Investing; Economics giữ mechanism và evidence foundation.
- **Korea Business:** contemporary Korean institutional/company cases ở case layer riêng.
- **Computer Science:** computational methods/platforms/auctions được cross-link khi relevant.

## Advanced expansion gate

Không tiếp tục mở Economics theo logic “còn subfield là phải có folder”. Chỉ thêm advanced chapter khi ít nhất một điều kiện đúng:

1. existing chapter cần prerequisite đó để không giải thích nửa chừng;
2. một domain khác phụ thuộc trực tiếp vào nó;
3. topic tạo learning value khác biệt, không duplicate;
4. có thể viết đủ assumptions/evidence/failure modes, không chỉ glossary.

Các ứng viên sau này: intertemporal choice/uncertainty, heterogeneous-agent macro, structural IO, causal ML, spatial/environmental/health economics.

## Repo-wide priority sau Economics

Sau depth pass này, Economics không còn là domain ưu tiên cần mở rộng tiếp ngay. Priority nên quay sang các vùng còn mỏng hơn:

```text
Research Methods
→ Sociology
→ Frontend canonical/root structure
→ repo-wide audit automation
```

Sau đó mới chạy cross-domain review để tìm gaps thật sự thay vì tiếp tục thêm files vào các library đã đủ core.

## Completion criterion

Economics được đánh dấu **core-domain complete** khi:

- tất cả `00–06` có canonical route;
- README + coverage audit + catalog phản ánh source of truth;
- internal boundaries với Investing/History/Korea/Geography rõ;
- theory, evidence và normative conclusions được tách;
- applied chapters có estimand + identification;
- historical chapters có enforcement/power/persistence mechanism.

Các tiêu chí trên hiện đã đạt sau depth pass này, subject to final catalog synchronization on `main`.
