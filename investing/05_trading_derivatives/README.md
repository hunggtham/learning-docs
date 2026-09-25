# 05 — Giao dịch và phái sinh (Trading & Derivatives)

Lĩnh vực này xem giao dịch như một hệ thống xác suất có chi phí thực thi, rủi ro vận hành, yêu cầu tài sản bảo đảm/ký quỹ và mức phơi nhiễm ở cấp danh mục; không xem giao dịch chỉ là tập hợp các mẫu hình vào lệnh. Lộ trình đi từ Forex và quản trị rủi ro tới hợp đồng phái sinh, nghiên cứu có hệ thống, vi cấu trúc thị trường, danh mục chiến lược và quyền chọn/biến động chuyên sâu.

## Thứ tự đọc

[00_MASTER_TRADING_FOREX_RISK.md](./00_MASTER_TRADING_FOREX_RISK.md) là bản tổng quan dài về biểu đồ, cấu trúc thị trường, Forex, đòn bẩy, ký quỹ, quy mô vị thế, kỳ vọng toán học, XAUUSD, kiểm thử chiến lược, nhật ký và tâm lý giao dịch.

### Forex — nhánh học chuyên sâu

[forex/README.md](./forex/README.md) tách Forex thành learning path riêng nhưng vẫn nằm dưới `05_trading_derivatives/`. Phần này đi từ cấu trúc thị trường OTC và các instrument, cách đọc quote/pip/lot/P&L, leverage–margin–position sizing, relative macro/rates/carry tới execution, broker, transaction cost, strategy research, portfolio FX risk, microstructure/options và context Korea/Vietnam. Sau core route, [`forex/90_connections/`](./forex/90_connections/) nối institutional FX qua NDF, forward points, cross-currency basis, funding, intervention, reserves và REER/valuation; [forex/90_labs/README.md](./forex/90_labs/README.md) chuyển kiến thức thành lab thực hành; [forex/80_case_studies/README.md](./forex/80_case_studies/README.md) stress-test mental model bằng ERM 1992, Asian Crisis 1997, CHF 2015 và global USD funding stress 2020; [forex/70_systematic_project/README.md](./forex/70_systematic_project/README.md) nối point-in-time data, execution-aware backtest, portfolio risk/attribution và forward-test controls thành systematic research process có thể audit; [forex/COVERAGE_AUDIT.md](./forex/COVERAGE_AUDIT.md) dùng để tránh duplicate chapter khi mở rộng sau này.

[01_DERIVATIVES_FUTURES_OPTIONS_CFD.md](./01_DERIVATIVES_FUTURES_OPTIONS_CFD.md) xây khung theo hợp đồng từ forward/futures, giá trị danh nghĩa, ký quỹ ban đầu/duy trì/biến đổi, basis, carry/roll, đường cong hàng hóa, tài sản rẻ nhất để giao (CTD) và thanh toán tới nền tảng quyền chọn, hoán đổi lãi suất/OIS, hoán đổi tiền tệ, TRS, CDS, chỉ số tín dụng, biến động, CFD, tài sản thế chấp, bù trừ ròng, rủi ro sai chiều, tỷ lệ phòng vệ đa tài sản, quản lý đáo hạn/roll và kiểm thử căng thẳng lãi/lỗ cùng ký quỹ.

[02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md](./02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md) biến một ý tưởng thành quy trình nghiên cứu có thể triển khai thực tế: giả thuyết nhân quả, dữ liệu đúng thời điểm, kiểm tra dấu thời gian và chất lượng dữ liệu, kỳ vọng/mức suy giảm, thiên lệch nhìn trước, thiên lệch sống sót, đào dữ liệu quá mức, tập huấn luyện/xác nhận/kiểm tra, purging/embargo, walk-forward, bề mặt tham số, kiểm định giả, mô hình chi phí/tác động thị trường/vay chứng khoán/roll futures, bootstrap, Monte Carlo, cỡ mẫu hiệu dụng, giới hạn quy mô, phát hiện trôi mô hình, đối soát, chống gửi lệnh trùng và cơ chế dừng khẩn cấp.

[03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md](./03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md) đi sâu ưu tiên giá–thời gian và vị trí trong hàng đợi, maker/taker, market/limit/stop, thời hạn hiệu lực lệnh, khớp một phần và nhiều chân, chênh lệch niêm yết/thực tế, độ sâu thị trường, thanh khoản ẩn/tối, đấu giá, phân mảnh sàn giao dịch, trượt giá, tác động thị trường, giới hạn quy mô, TWAP/VWAP/POV, thuật toán giảm thiếu hụt thực thi, lựa chọn bất lợi, khám phá giá, vòng xoáy thanh lý, độ trễ, an toàn API, đối soát, tổng hợp beta/FX/lãi suất/biến động và phân tích chi phí giao dịch (TCA).

[04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md](./04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md) tập trung vào độ bền của nghiên cứu: giả thuyết, vấn đề kiểm định nhiều lần, độ ổn định tham số, bằng chứng ngoài mẫu, phụ thuộc chế độ thị trường, khoảng tin cậy, bootstrap/Monte Carlo, suy giảm chiến lược, giới hạn quy mô và cách kết hợp nhiều chiến lược mà không nhân đôi cùng một beta, carry hay rủi ro bán biến động.

[05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md](./05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md) đi sâu quyền chọn như bài toán phân phối xác suất và rủi ro phụ thuộc trạng thái: giá kỳ hạn và carry, Delta/Gamma/Theta/Vega cùng các Greek bậc cao, biến động ngụ ý so với biến động thực tế, phần bù rủi ro biến động, skew, risk reversal, độ cong, cấu trúc kỳ hạn, bề mặt biến động, vol-of-vol, gamma scalping, assignment, pin risk, jump risk, Greek theo giá trị tiền, ngân sách phòng vệ đuôi và khó khăn khi kiểm thử quyền chọn.

[06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md](./06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md) là lớp học sâu nối giả thuyết, dữ liệu đúng thời điểm, kiểm thử độ bền, sizing, portfolio heat, capacity, execution half-life, TCA, margin stress, forward test, production monitoring, drift detection, kill switch và tiêu chí dừng chiến lược.

## Sau lĩnh vực này bạn cần làm được gì?

Bạn cần có khả năng đọc một công cụ phái sinh bằng chuỗi `tài sản cơ sở → cấu trúc chi trả → giá trị danh nghĩa/độ nhạy → carry/basis → ký quỹ/tài sản thế chấp → thanh khoản/đáo hạn → đối tác/thanh toán → tương tác với danh mục`.

Một chiến lược chỉ thực sự có lợi thế khi tín hiệu vẫn tạo kỳ vọng dương sau chênh lệch mua bán, trượt giá, tác động thị trường, chi phí vốn và lỗi vận hành. Bạn cũng phải tổng hợp rủi ro ở cấp danh mục theo beta, FX, lãi suất, biến động và thanh khoản thay vì chỉ đếm số lệnh; đồng thời kiểm thử cả lãi/lỗ lẫn khả năng đáp ứng ký quỹ.

Với quyền chọn, cần đọc vị thế bằng `hướng giá + biến động + thời gian + độ lồi + thanh khoản + ký quỹ`, hiểu vì sao trung hòa Delta không đồng nghĩa ít rủi ro và kiểm thử nhiều trạng thái giá/IV/thời gian trước khi giao dịch.

Với institutional Forex, cần tách `spot direction` khỏi `funding/hedging economics`: forward points, NDF, basis, collateral, reserve/intervention regime và hedge roll có thể đổi economics dù chart spot nhìn tương tự.

## Bài tập tích hợp

Nếu đang học riêng Forex, hoàn thành [Forex Practice Labs](./forex/90_labs/README.md), đọc [Forex Historical Case Studies](./forex/80_case_studies/README.md), các [Institutional Connections](./forex/90_connections/) và đi qua [Systematic FX Implementation Project](./forex/70_systematic_project/README.md) trước hoặc song song với Module 5. Các lớp này lần lượt kiểm tra khả năng tự tính/explain, stress mental model dưới regime cực đoan, hiểu funding/policy institutional mechanics và biến research thành process point-in-time/execution-aware có risk controls.

Đọc [Cú sốc CPI → Danh mục](../07_integrated_case_studies/01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md) để luyện thực thi quanh sự kiện, ghép đúng công cụ phòng vệ, rủi ro IV và phân rã kết quả sau sự kiện. Đọc [Khủng hoảng tín dụng và thanh khoản](../07_integrated_case_studies/02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md) để luyện căng thẳng ký quỹ/tài sản thế chấp, giảm đòn bẩy cưỡng bức, thứ bậc thanh khoản và thực thi trong khủng hoảng.

Sau đó hoàn thành **Module 5 — Trading & Derivatives** trong [Advanced Practice Workbook](../ADVANCED_PRACTICE_WORKBOOK.md). Đầu ra tối thiểu phải có đặc tả chiến lược, bias audit, báo cáo backtest, báo cáo thực thi, giới hạn rủi ro, điều kiện kill switch và quy tắc dừng chiến lược.

Sau đó chuyển sang [06 — Thị trường Hàn Quốc và Việt Nam](../06_markets_korea_vietnam/README.md).