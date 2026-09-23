# Thư viện Kiến thức Đầu tư (Investing Knowledge Library)

Bộ tài liệu này được tổ chức theo từng lĩnh vực (domain) thay vì gom vào một cuốn tổng hợp quá lớn. Mỗi thư mục có mục tiêu học rõ ràng, tài liệu nền tảng và các chương chuyên sâu để chuyển từ kiến thức sang phân tích thực tế.

Ngoài sáu lĩnh vực kiến thức chính, thư viện còn có một file quy chuẩn chung về thuật ngữ, công thức và phương pháp nghiên cứu, cùng một phần bài tập tích hợp (capstone) để nối toàn bộ quá trình từ lý thuyết → phân tích → xây vị thế → thực thi → đánh giá lại.

### Ranh giới với Economics library độc lập

Economics đã bắt đầu được tách tại [`../economics/README.md`](../economics/README.md). Thư viện này giữ phần general-purpose như economic reasoning, consumer/producer theory, market structure, game theory, labor, public, trade, development economics, industrial organization, econometrics và economic history.

`investing/04_economics/` vẫn là nguồn chuyên sâu cho macro, monetary system, capital flows, crisis transmission, public debt, demographics, productivity và policy regime trong bối cảnh đầu tư. Hai nhánh sẽ cross-link và migrate dần; không duplicate hàng loạt nội dung.

## 00 — Thuật ngữ, công thức và quy chuẩn nghiên cứu

[00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md](./00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md)

Đây là tài liệu tham chiếu dùng xuyên suốt toàn bộ thư viện. Nội dung chuẩn hóa cách dùng các khái niệm như lợi suất danh nghĩa và lợi suất thực, CAGR, độ biến động, tương quan, phương sai danh mục, beta, alpha, Sharpe, Sortino, mức suy giảm (drawdown), VaR, Expected Shortfall, định giá dòng tiền, EV, FCFF, FCFE, ROIC, duration, DV01, tổn thất tín dụng kỳ vọng, phân rã lợi suất ngoại tệ, giá trị danh nghĩa của phái sinh, kỳ vọng toán học, chỉ số tham chiếu, dữ liệu đúng thời điểm, thứ bậc nguồn dữ liệu, kịch bản và điều kiện vô hiệu hóa luận điểm.

Quy tắc ngôn ngữ của toàn thư viện cũng nằm ở đây: phần giải thích dùng tiếng Việt; thuật ngữ tiếng Anh chỉ giữ trong ngoặc khi cần tra cứu.

## Cấu trúc lĩnh vực

### 01 — Nền tảng đầu tư (Foundations)

[01_foundations/README.md](./01_foundations/README.md)

Học về tiền, hệ thống tài chính, cơ chế vận hành thị trường, rủi ro danh mục, phân bổ tài sản, tài chính hành vi, đầu tư theo vòng đời, tái cân bằng, lưu ký, vận hành đầu tư và phân tích danh mục. Phần nâng cao bao gồm độ biến động, mức suy giảm, hiệp phương sai, beta, alpha, Sharpe, Sortino, Calmar, VaR, Expected Shortfall, kiểm thử căng thẳng, phân rã kết quả đầu tư, chi phí, thuế, nhật ký quyết định và đánh giá hành vi.

### 02 — Các nhóm tài sản (Asset Classes)

[02_asset_classes/README.md](./02_asset_classes/README.md)

Học cổ phiếu, ETF, quỹ đầu tư, trái phiếu, tín dụng, tài sản thực, hàng hóa, tài sản thay thế, đầu tư theo nhân tố, chỉ số thông minh và rủi ro ngoại tệ. Phần nâng cao nối các tài sản thành một danh mục qua duration, lợi suất nắm giữ và trượt theo đường cong (carry/roll-down), chênh lệch tín dụng, phòng vệ tiền tệ, đóng góp rủi ro, phân bổ bền vững, tiền mặt, MMF, T-bill, sản phẩm cấu trúc, ETN, vốn cổ phần tư nhân, đầu tư mạo hiểm, tín dụng tư nhân và cơ sở hạ tầng.

### 03 — Phân tích doanh nghiệp (Company Analysis)

[03_company_analysis/README.md](./03_company_analysis/README.md)

Học báo cáo tài chính, kế toán, chất lượng doanh nghiệp, lợi thế cạnh tranh bền vững (moat), chuỗi giá trị, cấu trúc ngành, định giá, DCF, chất lượng lợi nhuận, vốn lưu động, kinh tế đơn vị, mô hình ba báo cáo tài chính và phân tích điều tra kế toán. Phần theo ngành bao gồm ngân hàng, bán dẫn, SaaS, bán lẻ, REIT và nhiều ngành mở rộng. Phần quản trị và phân bổ vốn đi sâu ROIC tăng thêm, chất lượng capex, cổ tức, mua lại cổ phiếu, pha loãng, M&A, goodwill, cổ đông kiểm soát và cơ chế khuyến khích của ban lãnh đạo.

### 04 — Kinh tế học và vĩ mô (Economics)

[04_economics/README.md](./04_economics/README.md)

Học kinh tế vi mô, kinh tế vĩ mô, kinh tế toàn cầu, dòng vốn, khủng hoảng ngân hàng và nợ chính phủ, dữ liệu vĩ mô, ngân hàng trung ương, cơ chế tiền tệ, repo, tài sản thế chấp, nguồn vốn USD và cách điều kiện tài chính truyền vào nền kinh tế. Phần nâng cao bổ sung tư duy theo chế độ kinh tế, các cuộc khủng hoảng lịch sử, tương tác tài khóa–tiền tệ, động lực nợ công, nguồn cung trái phiếu chính phủ, phần bù kỳ hạn, ưu thế tài khóa, nhân khẩu học, năng suất, TFP, thể chế và lãi suất trung tính.

### 05 — Giao dịch và phái sinh (Trading & Derivatives)

[05_trading_derivatives/README.md](./05_trading_derivatives/README.md)

Học Forex, hợp đồng tương lai, quyền chọn, hoán đổi, CFD, đòn bẩy, ký quỹ, tài sản bảo đảm, quy mô vị thế, kỳ vọng toán học, kiểm thử chiến lược, thực thi lệnh, vi cấu trúc sổ lệnh và quản trị rủi ro ở cấp danh mục giao dịch. Phần nghiên cứu nâng cao bao gồm kiểm định ngoài mẫu, walk-forward, thiên lệch dữ liệu, độ ổn định tham số, chi phí giao dịch, tác động thị trường, Monte Carlo, suy giảm chiến lược, danh mục chiến lược, bề mặt biến động, tương tác các Greek, biến động quanh sự kiện, phòng vệ động và an toàn vận hành.

### 06 — Thị trường Hàn Quốc và Việt Nam

[06_markets_korea_vietnam/README.md](./06_markets_korea_vietnam/README.md)

Áp dụng toàn bộ khung kiến thức vào KRX/KOSPI/KOSDAQ và HOSE/HNX/UPCoM. Nội dung bao gồm bản đồ ngành, KRW/VND, BOK/SBV, bán dẫn, ngân hàng, bất động sản, FDI, dòng vốn nước ngoài, cú sốc liên thị trường và quy trình nghiên cứu thực tế. Phần đầu tư xuyên biên giới bổ sung khung bốn loại tiền tệ, phòng vệ ngoại hối, quỹ niêm yết nội địa, nơi thành lập quỹ, tiếp cận thị trường, thanh toán, lưu ký, giới hạn sở hữu nước ngoài, chuyển tiền về nước, thuế khấu trừ và khả năng chống chịu vận hành.

### 07 — Bài tập tích hợp (Integrated Case Studies)

[07_integrated_case_studies/README.md](./07_integrated_case_studies/README.md)

Đây là phần tổng hợp cuối. Thay vì học thêm một lĩnh vực lý thuyết mới, mỗi tình huống buộc người đọc nối nhiều lớp kiến thức thành một chuỗi nguyên nhân–kết quả hoàn chỉnh:

- [Cú sốc CPI → Danh mục](./07_integrated_case_studies/01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md): cấu phần lạm phát → hàm phản ứng của ngân hàng trung ương → lợi suất danh nghĩa/lợi suất thực → USD/KRW/VND → lợi nhuận doanh nghiệp và định giá → phòng vệ và thực thi → phân rã kết quả.
- [Khủng hoảng tín dụng và thanh khoản](./07_integrated_case_studies/02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md): lệch kỳ hạn → căng thẳng nguồn vốn → tài sản thế chấp và haircut → bán cưỡng bức → chênh lệch tín dụng → co hẹp tín dụng → phản ứng chính sách → thanh khoản danh mục.
- [Chu kỳ bán dẫn Hàn Quốc](./07_integrated_case_studies/03_SEMICONDUCTOR_CYCLE_KOREA_CASE.md): chi tiêu AI → tồn kho, ASP và công suất sử dụng → cơ cấu HBM → capex và nhà cung cấp → điều chỉnh dự báo lợi nhuận → định giá chuẩn hóa → quy mô vị thế.
- [Chu kỳ bất động sản–ngân hàng Việt Nam](./07_integrated_case_studies/04_VIETNAM_PROPERTY_BANK_CREDIT_CASE.md): pháp lý → bán trước và dòng tiền → tái cấp vốn → ngân hàng, NPL và dự phòng → thanh khoản trong nước và SBV → định giá → khả năng thoát vị thế khi căng thẳng.

## Lộ trình học khuyến nghị

Nếu bắt đầu gần như từ số 0, dùng file `00` như tài liệu tham chiếu rồi học theo:

```text
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07
```

Không cần học thuộc file `00`. Hãy quay lại khi gặp thuật ngữ, công thức hoặc cần kiểm tra quy chuẩn nghiên cứu.

Nếu mục tiêu chính là đầu tư dài hạn:

```text
00 → 01 → 02 → 03 → 04 → 06 → 07
```

Nếu mục tiêu là vĩ mô hoặc Forex:

```text
00 → 01 → 02 → 04 → 05 → 06 → 07
```

Vẫn nên quay lại phần Phân tích doanh nghiệp để hiểu kênh lợi nhuận và vì sao cùng một cú sốc vĩ mô tạo kết quả khác nhau giữa các ngành và doanh nghiệp.

## Cách học để không biến thành đọc thụ động

Sau phần Nền tảng, tự viết tuyên bố chính sách đầu tư (Investment Policy Statement, IPS), kiểm thử danh mục theo ít nhất ba kịch bản và làm một lần phân rã kết quả hàng tháng.

Sau phần Các nhóm tài sản, phân tích một ETF, một ETF trái phiếu, một sản phẩm gần tiền mặt và một sản phẩm cấu trúc hoặc tài sản tư nhân theo quyền lợi pháp lý, nguồn lợi suất, tính thanh khoản, quyền chọn ẩn và rủi ro đi kèm.

Sau phần Phân tích doanh nghiệp, xây mô hình một doanh nghiệp với kịch bản cơ sở/tích cực/tiêu cực, chọn đúng KPI theo ngành, đối chiếu lợi nhuận với dòng tiền và đánh giá lịch sử phân bổ vốn của ban lãnh đạo.

Sau phần Kinh tế, theo dõi một sự kiện CPI/FOMC/BOK từ kỳ vọng đồng thuận tới phản ứng của thị trường, xác định hàm phản ứng, kênh truyền dẫn qua đường cong lợi suất, tỷ giá và tín dụng, đồng thời phân biệt cú sốc chu kỳ với thay đổi cấu trúc.

Sau phần Giao dịch, kiểm thử một chiến lược duy nhất, làm kiểm định ngoài mẫu và thử nghiệm tiến về phía trước, tính kỳ vọng và mức suy giảm, kiểm tra chi phí thực thi thực tế và kiểm thử vị thế phái sinh theo cả lãi/lỗ lẫn yêu cầu ký quỹ.

Sau phần Hàn Quốc/Việt Nam, tạo sổ nghiên cứu cho một cổ phiếu Hàn Quốc và một cổ phiếu Việt Nam, ghi rõ chu kỳ ngành, tiền tệ, tiếp cận thị trường, rủi ro bảng cân đối, định giá, chất xúc tác và điều kiện vô hiệu hóa luận điểm.

Cuối cùng, dùng phần 07 như bài kiểm tra tích hợp: trước khi đọc lời giải tiếp theo, tự viết chuỗi nguyên nhân–kết quả và dữ liệu cần kiểm tra.

## Mẫu ghi chú nghiên cứu chuẩn

Một ghi chú hoàn chỉnh nên trả lời tối thiểu:

```text
1. Quyền lợi pháp lý và bản chất kinh tế của tài sản là gì?
2. Nguồn tạo lợi suất chính là gì?
3. Dữ kiện, ước tính và giả định nào đang được dùng?
4. Thị trường đang phản ánh kỳ vọng nào vào giá?
5. Cây động lực và chỉ báo dẫn dắt là gì?
6. Kịch bản cơ sở / tích cực / tiêu cực khác nhau ở cơ chế nào?
7. Bảng cân đối và thanh khoản có chịu được kịch bản xấu không?
8. Định giá và lợi suất kỳ vọng có đủ bù rủi ro không?
9. Vị thế đang trùng lặp nhân tố nào trong danh mục?
10. Phòng vệ, thực thi và tổng chi phí ra sao?
11. Chất xúc tác và điều kiện vô hiệu hóa là gì?
12. Chu kỳ đánh giá lại và kế hoạch phân rã kết quả là gì?
```

## Mô hình tư duy toàn thư viện

```text
Quyền lợi pháp lý
→ Hệ thống tài chính
→ Nhóm tài sản / Cấu trúc sản phẩm
→ Xây dựng danh mục
→ Kinh tế doanh nghiệp / Ngành
→ Chế độ vĩ mô
→ Kỳ vọng thị trường
→ Định giá / Lợi suất kỳ vọng
→ Rủi ro / Thanh khoản / Quy mô vị thế
→ Thực thi / Phòng vệ
→ Phân rã kết quả
→ Đánh giá và cập nhật luận điểm
```

Mục tiêu cuối cùng không phải dự báo mọi biến động giá. Mục tiêu là xây một hệ thống tư duy đủ rõ để biết mình đang sở hữu gì, lợi suất đến từ đâu, rủi ro nằm ở đâu, thị trường đang kỳ vọng điều gì, điều kiện nào làm luận điểm sai và bằng chứng nào cần được cập nhật.

## Quy tắc cập nhật

Các nguyên lý nền tảng, kế toán, định giá, lý thuyết danh mục và vi cấu trúc thị trường có thể dùng lâu dài. Các phần về lãi suất chính sách, thuế, thanh toán, giới hạn sở hữu nước ngoài, phân loại chỉ số, thông số sản phẩm và quy định pháp lý phải được kiểm tra lại theo nguồn chính thức trước khi ra quyết định thật.

Dữ liệu vĩ mô mang tính thời điểm phải ghi rõ ngày hoặc kỳ tham chiếu. Khi nội dung trùng giữa tài liệu tổng quan và chương chuyên sâu, tài liệu tổng quan chỉ giữ vai trò bản đồ; chương chuyên sâu là nguồn tham chiếu chính về cơ chế.
