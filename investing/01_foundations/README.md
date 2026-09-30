# 01 — Nền tảng đầu tư (Foundations)

> **Mạch đọc:** README này là owner của nền tảng đầu tư. Bắt đầu bằng thứ tự đọc để thấy các lớp tiền, rủi ro và vận hành nối nhau ra sao; phần năng lực đầu ra dùng bản đồ đó để kiểm tra người học đã hiểu được gì trước khi đi vào case study.

Lĩnh vực này xây nền tảng tư duy trước khi học từng loại tài sản hoặc chọn cổ phiếu. Mục tiêu là hiểu hệ thống tài chính, cách giá được hình thành, rủi ro danh mục, cách vận hành một kế hoạch đầu tư nhiều năm và cách đánh giá kết quả mà không nhầm may mắn hoặc beta thị trường với kỹ năng.

## Thứ tự đọc

[00_MASTER_FOUNDATIONS_AND_PORTFOLIO.md](./00_MASTER_FOUNDATIONS_AND_PORTFOLIO.md) là bản tổng quan dài, dùng để hình thành bản đồ toàn lĩnh vực.

[01_MONEY_FINANCIAL_SYSTEM_AND_MARKET_MECHANICS.md](./01_MONEY_FINANCIAL_SYSTEM_AND_MARKET_MECHANICS.md) đi sâu về tiền, tiền gửi, dự trữ ngân hàng, cấu trúc vốn, thị trường sơ cấp/thứ cấp, sở giao dịch và thị trường phi tập trung (OTC), môi giới, lưu ký, thanh toán bù trừ, đối tác bù trừ trung tâm (CCP), sổ lệnh, đấu giá, thanh khoản, cơ chế tạo–mua lại ETF, cho vay chứng khoán, bán khống, thanh toán giao dịch và rủi ro thực thi.

[02_PORTFOLIO_RISK_ALLOCATION_AND_BEHAVIOR.md](./02_PORTFOLIO_RISK_ALLOCATION_AND_BEHAVIOR.md) giải thích mức chịu đựng rủi ro, khả năng chịu rủi ro, mức rủi ro cần thiết, khớp tài sản với nghĩa vụ, hiệp phương sai, tương quan, đóng góp rủi ro, tập trung nhân tố, phân bổ chiến lược/chiến thuật, rủi ro thứ tự lợi suất, đòn bẩy, ngân sách rủi ro, thiên lệch hành vi, IPS, nhật ký quyết định và kiểm thử căng thẳng.

[03_LIFECYCLE_ALLOCATION_REBALANCING_AND_INVESTMENT_OPERATIONS.md](./03_LIFECYCLE_ALLOCATION_REBALANCING_AND_INVESTMENT_OPERATIONS.md) đưa kiến thức sang vận hành thực tế: vốn con người (human capital), khớp nghĩa vụ, phân bổ chiến lược và chiến thuật, tái cân bằng, rủi ro thứ tự lợi suất, vị trí thuế của tài sản, lưu ký, chi phí giao dịch và đánh giá danh mục.

[04_RISK_MEASUREMENT_PORTFOLIO_ANALYTICS_AND_DECISION_RULES.md](./04_RISK_MEASUREMENT_PORTFOLIO_ANALYTICS_AND_DECISION_RULES.md) xây lớp định lượng: lợi suất số học, hình học, log và lợi suất thực; độ biến động; hiệp phương sai; tương quan; beta; alpha; nhân tố; sai lệch bám chỉ số; Sharpe, Sortino, Calmar; VaR; Expected Shortfall; rủi ro thanh khoản, nhảy giá và đòn bẩy; biên hiệu quả; tối ưu hóa bền vững; đóng góp rủi ro; phân tích kịch bản và ngưỡng quyết định.

[05_PERFORMANCE_ATTRIBUTION_FEES_TAX_AND_BEHAVIORAL_REVIEW.md](./05_PERFORMANCE_ATTRIBUTION_FEES_TAX_AND_BEHAVIORAL_REVIEW.md) hoàn thiện vòng phản hồi bằng cách phân rã kết quả thành beta thị trường, phân bổ tài sản, lựa chọn chứng khoán, nhân tố, tiền tệ, thu nhập, phí, chênh lệch mua bán, trượt giá, chi phí vốn, thuế và hành vi; đồng thời xây quy trình hiệu chỉnh dự báo, nhật ký quyết định và đánh giá theo tháng/quý/năm.

[06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md](./06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md) là lớp học sâu: chuyển mục tiêu và nghĩa vụ thành bảng cân đối kinh tế, ngân sách rủi ro, MCTR, tương quan theo trạng thái, tầng thanh khoản, kiểm thử cú sốc kết hợp, kiểm thử ngược, quy tắc tái cân bằng và nhật ký quyết định.

[07_PERSONAL_FINANCE_CASHFLOW_DEBT_INSURANCE_AND_INVESTING.md](./07_PERSONAL_FINANCE_CASHFLOW_DEBT_INSURANCE_AND_INVESTING.md) bổ sung lớp còn thiếu trước portfolio: dòng tiền, bảng cân đối cá nhân, liquidity ladder, debt economics, catastrophic-risk transfer, future liabilities, human capital và investable surplus. Chapter này cố ý đặt câu hỏi “hệ thống tài chính cá nhân có sống sót được không?” trước câu hỏi “asset allocation tối ưu là gì?”.

> **Chuyển mạch:** Danh sách chapter cho biết nên đi qua những lớp nào; phần kế tiếp đổi sang tiêu chí năng lực, để mỗi chapter được đọc như một công cụ giải thích chứ không phải một danh mục tài liệu.

## Sau lĩnh vực này bạn cần làm được gì?

Bạn cần có khả năng giải thích tiền của mình đi qua hệ thống nào khi mua chứng khoán, phân biệt rủi ro thị trường, thanh khoản, đối tác và vận hành; xây phân bổ theo mục tiêu thay vì theo mã chứng khoán; đo mức tập trung và đóng góp rủi ro; viết IPS; kiểm thử danh mục và phân tích vì sao danh mục lời hoặc lỗ thay vì chỉ nhìn tổng lợi suất.

Trước khi đi tới portfolio optimization, bạn cũng cần tách được cash flow, liquidity, debt, insurance và future liabilities để biết phần vốn nào thật sự có thể đầu tư dài hạn. Nếu chưa làm được, hãy đọc `07_PERSONAL_FINANCE...` trước `02_PORTFOLIO...` dù số thứ tự file đặt nó ở cuối foundations để không phá cấu trúc hiện có.

> **Chuyển mạch:** Khi đã xác định được năng lực cần có, bài tập tích hợp đưa các khái niệm vào cùng một tình huống: nghĩa vụ, thanh khoản, rủi ro và quyết định đầu tư phải được nhìn trong một hệ thống.

## Bài tập tích hợp

Đọc [Cú sốc CPI → Danh mục](../07_integrated_case_studies/01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md) để luyện kiểm thử căng thẳng, lập bản đồ nhân tố, phòng vệ và phân rã kết quả. Sau đó đọc [Khủng hoảng tín dụng và thanh khoản](../07_integrated_case_studies/02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md) để thấy bộ đệm thanh khoản, đòn bẩy, ký quỹ, tài sản thế chấp và rủi ro sống sót tương tác như thế nào.

Để nối portfolio với đời sống thực, dùng [Practical-life decision route](../../psychology/90_connections/07_practical_life_decisions_finance_health_communication_and_career.md), nơi cash runway được đặt cạnh health capacity, negotiation BATNA và career option value thay vì xem chúng như các vấn đề tách rời.

Để chuyển từ đọc sang tự làm, hoàn thành **mô-đun (module / 모듈) 1 — Foundations** trong [Advanced Practice Workbook](../ADVANCED_PRACTICE_WORKBOOK.md). Đầu ra tối thiểu phải có `portfolio_ips.md`, ma trận căng thẳng và một kiểm thử ngược chỉ ra điều kiện làm kế hoạch thất bại.

### Thinking Toolkit bridge

Khi vấn đề không còn là “cơ chế đầu tư hoạt động thế nào?” mà chuyển thành “với uncertainty này tôi nên ra quyết định thế nào?”, dùng [Thinking Toolkit](../../thinking/README.md) như lớp reasoning chung. Các cầu nối trực tiếp nhất là [Probability](../../thinking/probability/README.md) → [Expected Value](../../thinking/expected-value/README.md) → [Risk](../../thinking/risk/README.md) → [Decision Making](../../thinking/decision-making/README.md). Để luyện thay vì chỉ đọc, dùng [calibration/Bayesian updating](../../thinking/practice/01_calibration_and_bayesian_updating.md), [sensitivity analysis](../../thinking/practice/02_sensitivity_analysis_and_uncertainty_decomposition.md), [scenario stress testing](../../thinking/practice/03_scenario_planning_and_stress_testing.md) và [decision journal/postmortem](../../thinking/practice/04_decision_journal_and_postmortem.md).

Ranh giới ownership vẫn giữ nguyên: `investing/` sở hữu market/asset/portfolio mechanics; `thinking/` chỉ cung cấp công cụ reasoning có thể tái sử dụng ở nhiều domain.

Sau khi hoàn thành, chuyển sang [02 — Các nhóm tài sản](../02_asset_classes/README.md).

> **Bàn giao:** Sau **Bài tập tích hợp**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 MASTER FOUNDATIONS AND PORTFOLIO](./00_MASTER_FOUNDATIONS_AND_PORTFOLIO.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
