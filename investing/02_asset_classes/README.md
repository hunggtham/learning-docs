# 02 — Các nhóm tài sản (Asset Classes)

Lĩnh vực này giải thích từng nhóm tài sản theo bản chất kinh tế, nguồn lợi suất, rủi ro và cách chúng phản ứng trong các chế độ kinh tế khác nhau. Mục tiêu không phải thuộc tên sản phẩm, mà hiểu mình đang sở hữu quyền vốn chủ, khoản nợ, tài sản thực, công cụ gần tiền mặt, tài sản tư nhân hay cấu trúc có tính chất phái sinh nào; đồng thời hiểu lớp triển khai có thể làm lợi suất thực tế khác với mức phơi nhiễm lý thuyết.

## Thứ tự đọc

[01_STOCKS_ETF_AND_FUNDS.md](./01_STOCKS_ETF_AND_FUNDS.md) giải thích cổ phiếu từ quyền lợi còn lại của cổ đông, số cổ phiếu pha loãng, cổ tức, mua lại cổ phiếu và các hành động doanh nghiệp tới quyền biểu quyết, quản trị, mức tập trung chỉ số, NAV/iNAV, cơ chế tạo–mua lại ETF, thanh khoản khi căng thẳng, sai lệch bám chỉ số, mô phỏng vật lý/tổng hợp, phòng vệ ngoại hối, ETF đòn bẩy/nghịch đảo, Active Share, đầu tư trực tiếp theo chỉ số và tổng chi phí sở hữu.

[02_BONDS_RATES_AND_CREDIT.md](./02_BONDS_RATES_AND_CREDIT.md) xây tư duy thu nhập cố định từ coupon, YTM/YTW, giá sạch/giá bẩn, duration, DV01, convexity, duration theo điểm kỳ hạn và đường cong lợi suất tới lợi suất nắm giữ và trượt theo đường cong (carry/roll-down), Z-spread/OAS, chênh lệch tín dụng, vỡ nợ, khả năng thu hồi, thanh khoản, thay đổi xếp hạng, khoản vay đòn bẩy, điều khoản bảo vệ, trái phiếu callable/convertible, TIPS, MBS/ABS, nợ chính phủ, ETF trái phiếu, thang đáo hạn, barbell/bullet, khớp nghĩa vụ, phòng vệ lãi suất/tín dụng và phân rã lợi suất trái phiếu.

[03_REAL_ASSETS_AND_ALTERNATIVES.md](./03_REAL_ASSETS_AND_ALTERNATIVES.md) đi sâu định giá bất động sản trực tiếp, NOI/FFO/AFFO, LTV/DSCR, cap rate, cơ chế chuyển lạm phát vào tiền thuê, vàng, đường cong hàng hóa, lợi ích nắm giữ vật chất, đường chi phí, năng lượng, kim loại, nông sản, cơ sở hạ tầng, crypto, stablecoin và tài sản tư nhân với LBO, IRR, MOIC, TVPI, DPI, RVPI, gọi vốn, hạn mức tín dụng quỹ, năm đầu tư, thị trường thứ cấp và hiệu ứng mẫu số.

[04_FACTORS_INDEXING_AND_MULTI_ASSET_BEHAVIOR.md](./04_FACTORS_INDEXING_AND_MULTI_ASSET_BEHAVIOR.md) nâng lên tầng xây danh mục có hệ thống: vốn hóa thị trường so với tỷ trọng bằng nhau, giá trị, chất lượng, khả năng sinh lời, động lượng, biến động thấp, quy mô, cổ tức và smart beta; sau đó đi sâu cách định nghĩa và xếp hạng nhân tố, trung hòa ngành, phân rã lợi suất, chênh lệch định giá của nhân tố, cú sập nhân tố, vòng quay, giới hạn quy mô, carry/trend ngoài cổ phiếu, ngân sách sai lệch bám chỉ số, rủi ro phương pháp luận và triển khai đa nhân tố có kiểm soát rủi ro.

[05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md](./05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md) nối các nhóm tài sản thành danh mục hoàn chỉnh: chế độ tăng trưởng/lạm phát, nhân tố duration/tín dụng/thanh khoản, khung bốn loại tiền tệ, phòng vệ FX chiến lược và động, phòng vệ bằng futures/options, ngân sách phòng vệ, risk parity, đóng góp rủi ro cận biên, tỷ lệ đa dạng hóa, xu hướng, carry, mục tiêu biến động, tối ưu hóa bền vững, lớp định giá, phân bổ theo nghĩa vụ, bảng cân đối hộ gia đình, kiểm thử căng thẳng và kiểm thử ngược.

[06_CASH_MONEY_MARKETS_STRUCTURED_PRODUCTS_AND_PRIVATE_MARKETS.md](./06_CASH_MONEY_MARKETS_STRUCTURED_PRODUCTS_AND_PRIVATE_MARKETS.md) đi sâu tiền mặt ngân hàng, MMF, T-bill, CP, CD, repo, quy ước báo giá và số ngày, haircut, vòng xoáy ký quỹ và thang tiền mặt; sau đó giải cấu trúc sản phẩm cấu trúc, ELS, autocallable, worst-of và ETN thành trái phiếu + quyền chọn + rủi ro tương quan/nhà phát hành; cuối cùng đi tới PE, VC, tín dụng tư nhân, bất động sản tư nhân và cơ sở hạ tầng với IRR/MOIC/TVPI/DPI/RVPI/PME, đòn bẩy, PIK, LTV/DSCR, thị trường thứ cấp, gọi vốn và rủi ro thanh khoản.

[07_ASSET_PRICING_TERM_STRUCTURE_AND_PORTFOLIO_LAB.md](./07_ASSET_PRICING_TERM_STRUCTURE_AND_PORTFOLIO_LAB.md) là lớp học sâu dùng một ngôn ngữ chung để so tài sản: nguồn lợi suất, duration kinh tế, carry/roll-down, phần bù thanh khoản, cấu trúc kỳ hạn, định giá tương đối/tuyệt đối, hành vi theo regime và vai trò trong danh mục.

## Sau lĩnh vực này bạn cần làm được gì?

Bạn cần có khả năng nhìn một sản phẩm và xác định `quyền lợi kinh tế → nguồn lợi suất → duration/tín dụng/FX/nhân tố → thanh khoản → đòn bẩy/quyền chọn ẩn → cấu trúc sản phẩm → tổng chi phí → vai trò trong danh mục`.

Với thu nhập cố định, phải tách lợi suất nắm giữ, thay đổi lãi suất, thay đổi chênh lệch tín dụng và vỡ nợ. Với đầu tư nhân tố, phải phân biệt nhãn sản phẩm với cách triển khai thực tế. Với danh mục đa tài sản, phải nhìn đóng góp rủi ro, tiền tệ và nghĩa vụ thay vì chỉ nhìn tỷ trọng vốn. Với sản phẩm phức tạp hoặc tài sản tư nhân, phải nhìn xuyên lợi suất quảng cáo hoặc NAV ít biến động để hiểu quyền lợi pháp lý, đòn bẩy, thời điểm dòng tiền và thanh khoản khi căng thẳng.

## Bài tập tích hợp

Đọc [Cú sốc CPI → Danh mục](../07_integrated_case_studies/01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md) để thấy duration, lợi suất thực, FX, beta cổ phiếu và phòng vệ tương tác trong cùng một cú sốc. Đọc [Khủng hoảng tín dụng và thanh khoản](../07_integrated_case_studies/02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md) để luyện chênh lệch tín dụng, tài sản thế chấp, repo, độ trễ định giá của tài sản tư nhân và thứ bậc thanh khoản.

Sau đó hoàn thành **Module 2 — Asset Classes** trong [Advanced Practice Workbook](../ADVANCED_PRACTICE_WORKBOOK.md). Đầu ra tối thiểu là `asset_comparison_matrix.md`, trong đó mỗi tài sản phải được phân rã theo nguồn lợi suất, duration, tín dụng, FX, thanh khoản, regime thuận lợi/bất lợi và vai trò danh mục.

Sau đó chuyển sang [03 — Phân tích doanh nghiệp](../03_company_analysis/README.md) hoặc [04 — Kinh tế học và vĩ mô](../04_economics/README.md).