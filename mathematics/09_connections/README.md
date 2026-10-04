# 09 — Mathematics Connections

Thư mục này không thêm một nhánh toán tách biệt. Nó dùng các khái niệm canonical ở algebra, geometry, linear algebra, calculus, probability/statistics, optimization và discrete mathematics để giải thích những pattern xuất hiện xuyên Physics, Engineering, Computer Science, AI, Finance, Economics và quyết định thực tế.

## Mạch đọc

1. [Rate, change và accumulation](./00_rate_change_and_accumulation.md) — nối đạo hàm, tích phân, stock/flow và tốc độ thay đổi.
2. [Distance, similarity và projection](./01_distance_similarity_and_projection.md) — nối geometry, vector, inner product, least squares và representation.
3. [Uncertainty, information và entropy](./02_uncertainty_information_and_entropy.md) — nối probability với information và coding.
4. [Math for AI, Data and Software](./03_math_for_ai_data_and_software.md) — chọn các mathematical dependency quan trọng cho các hệ thống tính toán hiện đại.
5. [Math for Finance, Work and Daily Life](./04_math_for_finance_work_and_daily_life.md) — nối percentage, compounding, probability và optimization với các bài toán thực tế.
6. [Fourier, signals và frequency](./05_fourier_signals_and_frequency.md) — đổi representation từ time/space sang frequency.
7. [Laplace, Z-transform và dynamic systems](./06_laplace_z_transform_and_dynamic_systems.md) — nối differential equation, transform và control reasoning.
8. [Probability → Calibration → Decision and Risk](./07_probability_calibration_decision_and_risk.md) — nối xác suất, calibration, loss/utility và decision under uncertainty.
9. [Game theory: strategy, equilibrium và incentives](./08_game_theory_strategy_equilibrium_and_incentives.md) — nối probability/optimization với multi-agent interaction, Nash/minimax, repeated games, mechanism design và incentive-aware systems.

## Các bridge quan trọng

```text
Probability
→ calibration
→ expected utility / decision
→ strategic interaction
→ equilibrium / incentives
```

```text
Optimization
→ one decision maker
→ Game Theory
→ multiple decision makers that react to each other
```

```text
Graph / matching
→ feasible allocation
→ preference / incentives
→ stable or strategic allocation
```

Các bridge này giúp tránh ba nhầm lẫn thường gặp: một model dự đoán tốt chưa chắc dẫn đến decision tốt; một decision tối ưu cho một agent chưa chắc tối ưu cho system; và một allocation có cardinality tối đa chưa chắc stable khi participants có preferences.

## Ranh giới

Các route này không thay thế chapter toán gốc. Nếu một route sử dụng Bayes, covariance, derivative, optimization, network matching hay stochastic process mà người đọc chưa chắc, quay về canonical owner trong `06_probability_statistics/`, `05_calculus/`, `07_discrete_cs/` hoặc `08_optimization_numerical/`.

Phần application cũng giữ boundary rõ:

- Investing: đọc tiếp [macro + behavior + evidence → portfolio decision](../../investing/07_integrated_case_studies/08_MACRO_BEHAVIOR_EVIDENCE_TO_PORTFOLIO_DECISION.md).
- Economics: game theory ở đây giữ mathematical structure; market/institution interpretation thuộc `economics/`.
- AI/Data: calibration, evaluation và learning mechanics quay về owner của AI/Data tương ứng.
- Software/Platforms: incentive-aware design ở đây chỉ cung cấp mathematical lens; architecture, security và production behavior thuộc technical libraries.
- Research: measurement, causal design và evidence quality thuộc `research_methods/`.

> **Bàn giao:** Dùng các chapter trong thư mục này khi đã biết từng concept riêng lẻ nhưng cần thấy chúng kết hợp thành một mental model xuyên lĩnh vực.
