# Economics Thư viện kiến thức (knowledge library / 지식 라이브러리)

> **Mạch đọc:** [README](./README.md) là owner của **Economics Thư viện kiến thức (knowledge library / 지식 라이브러리)**. Route học đi từ reasoning và microeconomics → market structure/game theory → macroeconomics → applied economics, econometrics và economic history; mỗi nhánh phải quay về owner, prerequisite và giới hạn bằng chứng của nó.

`economics/` là thư viện Economics độc lập của repository. Mục tiêu là giải thích cách cá nhân, doanh nghiệp, thị trường, nhà nước và các nền kinh tế lựa chọn và phối hợp dưới điều kiện khan hiếm, thông tin không hoàn hảo và ràng buộc thể chế. Economics ở đây là lĩnh vực (domain / 도메인) nền tảng; phần ứng dụng vào tài sản, doanh nghiệp và danh mục vẫn nằm ở [Investing](../investing/README.md).

## Trạng thái hiện tại

Economics cốt lõi (core / 핵심) hiện đã hoàn chỉnh ở cấp chuẩn gốc (canonical / 정본) lộ trình học (learning path / 학습 경로):

- [00 — Foundations](./00_foundations/00_economic_reasoning.md) — scarcity, opportunity chi phí (cost / 비용), marginal phân tích (analysis / 분석), incentives, equilibrium, efficiency/equity và comparative statics.
- [01 — Microeconomics](./01_microeconomics/README.md) — bên tiêu thụ (consumer / 소비자)/producer lý thuyết (theory / 이론) → welfare → externality → công khai (public / 공개) goods/dùng chung (common / 공통) resources → thông tin (information / 정보) asymmetry/contracts.
- [02 — Market Structure & Game Theory](./02_market_structure_game_theory/README.md) — competition/monopoly → oligopoly → repeated games/entry/collusion → auctions/cơ chế (mechanism / 메커니즘) thiết kế (design / 설계).
- [03 — Macroeconomics](./03_macroeconomics/README.md) — đo lường (measurement / 측정) → growth → labor/inflation → money/banking/monetary chính sách (policy / 정책) → fiscal/nghiệp vụ (business / 비즈니스) cycles → open economy/crises.
- [04 — Applied Economics](./04_applied_economics/README.md) — labor → công khai (public / 공개) economics → international trade → development → industrial organization.
- [05 — Econometrics](./05_econometrics/README.md) — đo lường (measurement / 측정)/estimand → regression → experiments/selection → IV/RDD → panel/DiD → thời gian (time / 시간) series/macro identification → robustness/bên ngoài (external / 외부) validity.
- [06 — Economic History & Institutions](./06_economic_history_institutions/README.md) — institutions/trạng thái (state / 상태) sức chứa (capacity / 용량) → money/finance/fiscal states → industrialization/globalization → crises/regime thay đổi (change / 변경)/đường dẫn (path / 경로) dependence.

Từ đây Economics không còn khoảng trống cốt lõi (core / 핵심) bắt buộc. Advanced expansions chỉ nên mở khi phục vụ học tập (learning / 학습) tuyến (route / 경로) cụ thể thay vì tăng số tệp (file / 파일).

[`investing/04_economics/`](../investing/04_economics/README.md) tiếp tục giữ ứng dụng (application / 애플리케이션) tầng (layer / 계층) cho macro dữ liệu (data / 데이터), liquidity, thị trường (market / 시장) transmission, crisis cases, chính sách (policy / 정책) regimes và nowcasting; Economics cross-link thay vì duplicate.

> **Chuyển mạch:** Current state identifies the next learning route; depth work must preserve canonical ownership and add reasoning/evidence rather than duplicate a chapter.

## Học tập (learning / 학습) tuyến (route / 경로)

```text
00 Foundations
→ 01 Microeconomics
→ 02 Market Structure & Game Theory
→ 03 Macroeconomics
→ 05 Econometrics foundation
→ 04 Applied Economics
→ 06 Economic History & Institutions
```

Folder numbering phản ánh taxonomy, không ép thứ tự học tuyệt đối. Econometrics được đặt trước Applied Economics trong học tập (learning / 학습) phụ thuộc (dependency / 의존성) để empirical trường hợp (case / 사례) không biến thành correlation narrative.

> **Chuyển mạch:** **Học tập route** xác định thứ tự prerequisite; **Depth contract** nêu mức giải thích cần đạt, rồi **Connections làm spine** nối các domain bằng causal mechanism thật.

## Độ sâu (depth / 깊이) đặc tả hợp đồng (contract / 계약)

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

Applied chapter thêm incidence và scale-up. Historical chapter thêm enforcement, phân phối (distribution / 분포) of power, persistence cơ chế (mechanism / 메커니즘) và historical-identification limits.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Economics Thư viện kiến thức (knowledge library / 지식 라이브러리)**, sau nội dung của **Độ sâu (depth / 깊이) đặc tả hợp đồng (contract / 계약)**, **Các liên kết (connection / 연결) làm spine của thư viện (library / 라이브러리)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Quy ước biên soạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các liên kết (connection / 연결) làm spine của thư viện (library / 라이브러리)

- [Mathematics](../mathematics/README.md): calculus, tối ưu hóa (optimization / 최적화), xác suất (probability / 확률)/statistics, tuyến tính (linear / 선형) algebra và dynamical các hệ thống (systems / 시스템들).
- [World History](../world_history/README.md) + [Korean History](../korean_history/README.md): chronology, actors, wars và institutional chuỗi (sequence / 시퀀스); Economics không duplicate timeline.
- [Psychology](../psychology/README.md): bounded rationality, hành vi (behavior / 동작), salience, expectations và decision-making.
- [World Geography](../world_geography/README.md): resources, location, vận chuyển (transport / 전송), spatial tương tác (interaction / 상호작용), thị trường (market / 시장) truy cập (access / 접근) và trade networks.
- [Investing](../investing/README.md): asset/company/capital-flow ứng dụng (application / 애플리케이션) tầng (layer / 계층).
- [Korea Business & Economy](../korea_business_economy_knowledge_library/README.md): trường hợp (case / 사례) tầng (layer / 계층) cho labor, chaebol, trade, industrial chính sách (policy / 정책) và Korean institutions.
- [Computer Science](../computer_science/README.md): auctions, cơ chế (mechanism / 메커니즘) thiết kế (design / 설계), platforms, matching, tối ưu hóa (optimization / 최적화) và computational methods.

> **Chuyển mạch:** **Connections làm spine** chỉ ra nơi các lập luận kinh tế gặp nhau; **Quy ước biên soạn** giữ thuật ngữ, evidence và owner nhất quán trước khi sang **Sau cốt lõi**.

## Quy ước biên soạn

Giữ bốn quy tắc (rule / 규칙) xuyên suốt:

```text
Model ≠ Evidence
Accounting Identity ≠ Causal Theory
Estimator ≠ Identification Strategy
Causal Estimate ≠ Policy Recommendation
```

Positive economics phải tách khỏi normative judgment. Historical persistence cũng không tự đồng nghĩa đường dẫn (path / 경로) dependence; formal rules cũng không tự đồng nghĩa effective enforcement.

> **Chuyển mạch:** **Sau cốt lõi** chốt năng lực giải thích và chỉ ra điểm quay lại từng domain owner; đây là boundary của README, không phải một chapter mới.

## Sau cốt lõi (core / 핵심)

Các advanced topics có thể mở sau khi có nhu cầu rõ: intertemporal/bất định (uncertainty / 불확실성) micro, heterogeneous-agent macro, structural IO/econometrics, nhân quả (causal / 인과적) ML, spatial economics, environmental/health economics hoặc deeper financial economics. Ưu tiên repo-wide sau cốt lõi (core / 핵심) Economics nên quay lại các lĩnh vực (domain / 도메인) còn mỏng hơn thay vì tiếp tục nở Economics không giới hạn.

Xem [Coverage Audit](./COVERAGE_AUDIT.md) để theo dõi độ sâu (depth / 깊이) gates và next repo-wide priorities.

> **Bàn giao:** Sau **Sau cốt lõi (core / 핵심)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
