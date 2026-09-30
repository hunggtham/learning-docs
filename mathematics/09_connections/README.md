# 09 — Mathematics Connections

Thư mục này không thêm một nhánh toán mới. Nó dùng các khái niệm chuẩn gốc (canonical / 정본) ở algebra, geometry, linear algebra, calculus, probability/statistics và optimization để giải thích những pattern xuất hiện xuyên Physics, Engineering, Computer Science, AI, Finance và quyết định thực tế.

## Mạch đọc

1. [Rate, change và accumulation](./00_rate_change_and_accumulation.md) — nối đạo hàm, tích phân, stock/flow và tốc độ thay đổi.
2. [Distance, similarity và projection](./01_distance_similarity_and_projection.md) — nối geometry, vector, inner product, least squares và representation.
3. [Uncertainty, information và entropy](./02_uncertainty_information_and_entropy.md) — nối probability với information và coding.
4. [Math for AI, Data and Software](./03_math_for_ai_data_and_software.md) — chọn các mathematical dependency quan trọng cho các hệ thống tính toán hiện đại.
5. [Math for Finance, Work and Daily Life](./04_math_for_finance_work_and_daily_life.md) — nối percentage, compounding, probability và optimization với các bài toán thực tế.
6. [Fourier, signals và frequency](./05_fourier_signals_and_frequency.md) — đổi representation từ time/space sang frequency.
7. [Laplace, Z-transform và dynamic systems](./06_laplace_z_transform_and_dynamic_systems.md) — nối differential equation, transform và control reasoning.
8. [Probability → Calibration → Decision and Risk](./07_probability_calibration_decision_and_risk.md) — nối xác suất (probability / 확률), hiệu chuẩn (calibration / 보정), loss/utility và quyết định dưới bất định (decision under uncertainty / 불확실성하 의사결정).

## Ranh giới

Các route này không thay thế chapter toán gốc. Nếu một route sử dụng Bayes, covariance, derivative, optimization hay stochastic process mà người đọc chưa chắc, hãy quay về chapter tương ứng trong `06_probability_statistics/`, `05_calculus/` hoặc `08_optimization_numerical/`.

Route mới về xác suất và quyết định cố ý dừng trước domain-specific policy. Với đầu tư, đọc tiếp [macro + behavior + evidence → portfolio decision](../../investing/07_integrated_case_studies/08_MACRO_BEHAVIOR_EVIDENCE_TO_PORTFOLIO_DECISION.md); với AI, dùng calibration/evaluation trong owner của Artificial Intelligence; với research, quay về `research_methods/` để kiểm tra measurement và evidence design.

> **Bàn giao:** Các chapter trong thư mục này nên được dùng khi người đọc đã biết từng concept riêng lẻ nhưng chưa thấy chúng kết hợp thành một mental model xuyên lĩnh vực.