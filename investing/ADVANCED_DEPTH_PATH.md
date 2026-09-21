# Advanced Depth Path — Lộ trình học sâu Investing

> File này là bản đồ dành cho giai đoạn sau khi đã đọc các chapter nền tảng. Mục tiêu không phải học thêm thật nhiều thuật ngữ, mà tăng khả năng **nối kiến thức → xây mô hình → dùng dữ liệu → kiểm thử → nhận diện failure mode → ra quyết định → đánh giá lại**.

## Cách sử dụng

Không nên đọc các file Advanced Lab như sách tóm tắt. Với mỗi phần, hãy chọn một danh mục, doanh nghiệp, bộ dữ liệu vĩ mô hoặc chiến lược thật để làm bài tập đi kèm.

Lộ trình khuyến nghị:

```text
01 — Portfolio Design
↓
02 — Asset Pricing
↓
03 — Company Modeling
↓
04 — Macro Transmission
↓
05 — Trading System
↓
06 — Korea / Vietnam Market Thesis
↓
Advanced Practice Workbook
↓
07 — Integrated Case Studies
↓
Full Investment Process Capstone
```

Một phần chỉ được xem là “đã học sâu” khi người đọc đi đủ chuỗi:

```text
Khái niệm (concept)
→ Cơ chế (mechanism)
→ Dữ liệu cần quan sát (data)
→ Cách diễn giải (interpretation)
→ Rủi ro (risk)
→ Điều kiện thất bại (failure mode)
→ Tình huống áp dụng (case study)
→ Đầu ra có thể review
```

## 01 — Thiết kế danh mục nâng cao

[06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md](./01_foundations/06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md)

Trọng tâm:

```text
Bảng cân đối cá nhân
→ khớp nghĩa vụ
→ ngân sách rủi ro
→ MCTR
→ tương quan theo trạng thái
→ kiểm thử căng thẳng
→ kiểm thử ngược
→ nhật ký quyết định
```

Dữ liệu cần biết cách dùng gồm giá trị tài sản, nghĩa vụ theo thời gian và đồng tiền, dòng tiền tiết kiệm, độ biến động, covariance/correlation, drawdown, beta/factor exposure, liquidity bucket và chi phí giao dịch.

Failure mode cần nhận diện gồm giả định tương quan lịch sử ổn định, dùng volatility thay cho khả năng thất bại mục tiêu, không tách tiền cho nghĩa vụ gần, đòn bẩy ẩn và tái cân bằng dựa trên cảm xúc.

**Gate hoàn thành:** phải tạo được `IPS + stress matrix + reverse stress test + rebalancing rules`, đồng thời giải thích được danh mục thất bại trong trạng thái nào.

## 02 — Định giá tài sản và vai trò trong danh mục

[07_ASSET_PRICING_TERM_STRUCTURE_AND_PORTFOLIO_LAB.md](./02_asset_classes/07_ASSET_PRICING_TERM_STRUCTURE_AND_PORTFOLIO_LAB.md)

Trọng tâm:

```text
Dòng tiền
→ phân rã lợi suất kỳ vọng
→ duration
→ carry / roll-down
→ tín dụng / FX
→ phần bù thanh khoản
→ hành vi theo chế độ kinh tế
→ vai trò trong danh mục
```

Dữ liệu tối thiểu phải biết đọc gồm yield curve, real yield, credit spread, default/recovery, NAV/premium-discount, tracking difference, cap rate/NOI, commodity curve, FX forward points, volatility và thanh khoản.

Failure mode gồm so tài sản chỉ bằng lợi suất danh nghĩa, nhầm ETF với asset class, nhìn private NAV ít biến động rồi kết luận rủi ro thấp, nhầm carry cao với expected return cao và bỏ qua embedded option/leverage.

**Gate hoàn thành:** phải so được ít nhất bốn asset class trên cùng một bảng `cash flow → duration → carry → liquidity → regime → failure mode → portfolio role`.

## 03 — Mô hình doanh nghiệp tích hợp

[07_INTEGRATED_COMPANY_MODELING_AND_THESIS_LAB.md](./03_company_analysis/07_INTEGRATED_COMPANY_MODELING_AND_THESIS_LAB.md)

Trọng tâm:

```text
Mô hình kinh doanh
→ động lực doanh thu
→ cầu nối biên lợi nhuận
→ vốn lưu động
→ capex
→ lịch nợ
→ ba báo cáo
→ ROIC
→ định giá
→ theo dõi luận điểm
```

Dữ liệu phải nối từ filings và dữ liệu vận hành tới revenue driver, margin, DSO/DIO/DPO, capex, debt maturity, dilution, ROIC tăng thêm, consensus revision và valuation.

Failure mode gồm dự báo doanh thu bằng CAGR không có driver, dùng EPS mà bỏ qua cash conversion, loại mọi khoản “one-off”, dùng peak earnings để định giá doanh nghiệp chu kỳ, bỏ qua dilution/SBC, và tin vào moat không có bằng chứng kinh tế.

**Gate hoàn thành:** thay một driver vận hành phải làm thay đổi hợp lý ba báo cáo, FCF, valuation và thesis; phải có bear/base/bull cùng invalidation cụ thể.

## 04 — Nowcasting và truyền dẫn vĩ mô

[07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md](./04_economics/07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md)

Trọng tâm:

```text
Dữ liệu
→ mức bất ngờ
→ phản ứng chính sách
→ đường cong lợi suất
→ thanh khoản / tín dụng
→ FX
→ ngành
→ lợi nhuận
→ định giá
```

Không chỉ đọc CPI/GDP. Phải biết dùng surprise vs consensus, revision, labor/wage/productivity, 2Y/10Y/real yield/breakeven, term premium, lending standards, credit growth/spread, repo/collateral, USD funding và financial conditions.

Failure mode gồm suy luận `CPI ↑ → cổ phiếu ↓`, nhầm level với rate-of-change, bỏ qua điều thị trường đã pricing, không tách demand shock và supply shock, nhầm liquidity support với solvency repair và dùng một chỉ tiêu để gọi tên regime.

**Gate hoàn thành:** phải xây được một `surprise map + nowcast dashboard + policy reaction map + cross-asset transmission table` và nêu được dữ liệu nào sẽ bác bỏ kịch bản.

## 05 — Thiết kế hệ thống giao dịch

[06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md](./05_trading_derivatives/06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md)

Trọng tâm:

```text
Giả thuyết
→ dữ liệu đúng thời điểm
→ backtest
→ kiểm tra độ bền
→ quy mô vị thế
→ margin / liquidity
→ thực thi
→ giám sát live
→ kill switch
→ dừng chiến lược
```

Dữ liệu phải được kiểm soát theo observation time, publication time, revision time, decision time và execution time. Kết quả phải bao gồm expectancy, distribution, drawdown, turnover, slippage, implementation shortfall, factor exposure, capacity và margin stress.

Failure mode gồm look-ahead, survivorship, data snooping, overfit tham số, cost model cố định, full-size ngay sau backtest, nhầm margin với economic exposure, dùng stop như bảo đảm chống gap và đánh giá chiến lược chỉ bằng Sharpe.

**Gate hoàn thành:** phải có `strategy specification + bias audit + OOS/walk-forward + cost-aware test + sizing rule + execution plan + kill switch + retirement rule`.

## 06 — Xây luận điểm thị trường Korea / Vietnam

[07_KOREA_VIETNAM_MARKET_THESIS_AND_SCENARIO_LAB.md](./06_markets_korea_vietnam/07_KOREA_VIETNAM_MARKET_THESIS_AND_SCENARIO_LAB.md)

Trọng tâm:

```text
Chế độ toàn cầu
→ bảng cân đối quốc gia
→ BOK / SBV và ràng buộc chính sách
→ KRW / VND
→ tín dụng / thanh khoản
→ ngành
→ doanh nghiệp
→ định giá
→ market access
→ vị thế
```

Dữ liệu phải nối được xuất khẩu, trade balance, FX, reserve/liquidity, rate/credit, foreign flow, market breadth, margin activity, sector revisions, company balance sheet và valuation. Với thông tin có tính thời điểm như chính sách, thuế, settlement, foreign room hoặc market classification phải kiểm tra nguồn chính thức trước khi dùng thực tế.

Failure mode gồm suy luận “KRW yếu = mọi exporter tốt”, “credit growth = mọi ngân hàng tốt”, nhầm liquidity rally với earnings recovery, dùng index return thay market breadth và bỏ qua custody/FX/tax/access trong cross-border return.

**Gate hoàn thành:** phải tạo được `country dashboard + sector map + company driver tree + valuation + liquidity-aware position plan + invalidation` cho ít nhất một case Hàn Quốc và một case Việt Nam.

## Advanced Practice Workbook — Biến kiến thức thành sản phẩm phân tích

[ADVANCED_PRACTICE_WORKBOOK.md](./ADVANCED_PRACTICE_WORKBOOK.md)

Workbook là bước bắt buộc nếu muốn tăng chiều sâu thực sự. Sáu module tương ứng sáu domain chính và mỗi module phải đi đủ:

```text
Dữ liệu / giả định
→ phép tính / mô hình
→ cách diễn giải
→ kịch bản
→ phản ví dụ
→ failure mode
→ điều kiện vô hiệu hóa
→ đầu ra Markdown
→ tự chấm
```

### Audit workbook

Khi làm bài, không được chỉ điền kết quả. Mỗi câu trả lời cần phân biệt:

```text
Dữ kiện (fact)
Ước tính (estimate)
Giả định (assumption)
Diễn giải (interpretation)
Quyết định / rule
```

Mỗi module phải có ít nhất một bài **reverse stress test** hoặc **counterfactual**. Ví dụ: thay vì chỉ hỏi “nếu yield tăng 100 bp thì sao?”, phải hỏi “điều kiện nào khiến hedge thất bại?” hoặc “kết quả nào quan sát được dù thesis ban đầu sai?”.

Một bài chỉ đạt khi có thể chỉ ra **failure mode** và dữ liệu xác nhận/bác bỏ, không chỉ tính đúng công thức.

## 07 — Case studies tích hợp

Các tình huống trong [07_integrated_case_studies](./07_integrated_case_studies/README.md) là nơi kiểm tra integration. Mỗi case phải đi đủ chuỗi:

```text
Macro shock / question
→ Rates / yield curve
→ Liquidity / credit / funding
→ FX
→ Industry economics
→ Company driver
→ Earnings / cash flow
→ Valuation
→ Portfolio exposure
→ Hedge / execution
→ Attribution / review
```

Nếu một case dừng ở “macro tốt/xấu cho ngành”, case đó chưa đủ sâu.

Ưu tiên worked case có số liệu giả định để buộc người đọc tính duration, refinancing cost, earnings sensitivity, valuation sensitivity và portfolio loss thay vì chỉ đọc narrative.

## 08 — Capstone: quy trình đầu tư hoàn chỉnh

[05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md](./07_integrated_case_studies/05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md)

Trọng tâm:

```text
Câu hỏi
→ nghiên cứu
→ mô hình
→ định giá
→ phân phối lợi suất
→ vị thế
→ thực thi
→ theo dõi
→ phân rã kết quả
→ post-mortem
→ cải thiện quy trình
```

Capstone không được kết thúc bằng target price. Đầu ra cuối phải cho thấy **thesis sai trong điều kiện nào, bảng cân đối có sống sót không, danh mục chịu bao nhiêu loss trong bear case và phần P/L sau đó đến từ thesis hay từ beta/multiple/FX**.

## Ma trận audit chiều sâu toàn library

| Domain | Concept | Mechanism | Data | Interpretation | Risk | Failure mode | Case / Practice |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Foundations | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Advanced Lab + Workbook |
| Asset Classes | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Advanced Lab + Workbook |
| Company Analysis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Company Lab + sector cases |
| Economics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Macro Lab + CPI/credit cases |
| Trading & Derivatives | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | System Lab + Workbook |
| Korea / Vietnam | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Market Lab + country cases |

Dấu ✓ không có nghĩa nội dung đã “xong vĩnh viễn”. Nó có nghĩa library đã có vị trí canonical cho lớp kiến thức đó. Nội dung mới chỉ nên được thêm khi làm sâu cơ chế, dữ liệu, failure mode hoặc case, không nên tạo chapter mới chỉ vì gặp một thuật ngữ mới.

## Chuẩn đầu ra sau mỗi Advanced Lab

```text
Portfolio lab      → IPS + stress matrix + reverse stress test
Asset lab          → asset comparison matrix + regime/failure map
Company lab        → integrated model + one-page thesis + sensitivity
Macro lab          → nowcast dashboard + surprise map + transmission table
Trading lab        → strategy specification + test report + kill switch
Market lab         → country/sector thesis dashboard + company transmission
Workbook           → bộ bài thực hành có số liệu + self-review
Capstone           → complete investment dossier + attribution/post-mortem
```

## Quy tắc học sâu

Không chuyển sang lab tiếp theo nếu chỉ “đọc hiểu”. Hãy tự tạo ít nhất một mô hình, bảng phân tích hoặc case thực hành.

Độ sâu không đến từ số trang đã đọc mà từ khả năng:

```text
Giải thích cơ chế
→ chọn đúng dữ liệu
→ lượng hóa giả định
→ kiểm tra phản ví dụ
→ xác định điều kiện sai
→ đo tác động lên valuation / portfolio
→ cập nhật quyết định khi dữ liệu mới xuất hiện
```

Có thể tự đánh giá theo năm mức:

```text
1. Biết thuật ngữ
2. Áp dụng cơ học
3. Phân tích nhiều biến và dữ liệu
4. Phản biện, stress và nhận diện failure mode
5. Vận hành một quy trình lặp lại có attribution
```

## Kết luận

Toàn bộ thư viện Investing hiện nên được dùng theo ba tầng:

```text
Tầng 1 — Domain Knowledge
01 → 06

Tầng 2 — Advanced Application
Advanced Labs

Tầng 3 — Deliberate Practice & Integration
Workbook → Case Studies → Capstone
```

Nếu tầng đầu giúp trả lời **“khái niệm này là gì?”**, tầng Advanced giúp trả lời **“cơ chế hoạt động thế nào và dữ liệu nào chứng minh?”**, còn Workbook/Case/Capstone phải giúp trả lời **“failure mode là gì, tác động tới valuation/danh mục bao nhiêu và làm sao biết mình đang sai?”**.