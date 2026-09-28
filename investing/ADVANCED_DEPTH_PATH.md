# Advanced độ sâu (depth / 깊이) đường dẫn (path / 경로) — Lộ trình học sâu Investing

> **Mạch đọc:** Đặt **Advanced độ sâu (depth / 깊이) đường dẫn (path / 경로) — Lộ trình học sâu Investing** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Cách sử dụng** sang **01 — Thiết kế danh mục nâng cao**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> tệp (file / 파일) này là bản đồ dành cho giai đoạn sau khi đã đọc các chapter nền tảng. Mục tiêu không phải học thêm thật nhiều thuật ngữ, mà tăng khả năng **nối kiến thức → xây mô hình → dùng dữ liệu → kiểm thử → nhận diện dạng thất bại (failure mode / 실패 모드) → ra quyết định → đánh giá lại**.

## Cách sử dụng

Không nên đọc các tệp (file / 파일) Advanced Lab như sách tóm tắt. Với mỗi phần, hãy chọn một danh mục, doanh nghiệp, bộ dữ liệu vĩ mô hoặc chiến lược thật để làm bài tập đi kèm.

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

Dạng thất bại (failure mode / 실패 모드) cần nhận diện gồm giả định tương quan lịch sử ổn định, dùng volatility thay cho khả năng thất bại mục tiêu, không tách tiền cho nghĩa vụ gần, đòn bẩy ẩn và tái cân bằng dựa trên cảm xúc.

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

Dữ liệu tối thiểu phải biết đọc gồm yield curve, real yield, credit spread, default/khôi phục (recovery / 복구), NAV/premium-discount, tracking difference, cap tỷ lệ (rate / 비율)/NOI, commodity curve, FX forward points, volatility và thanh khoản.

Dạng thất bại (failure mode / 실패 모드) gồm so tài sản chỉ bằng lợi suất danh nghĩa, nhầm ETF với asset lớp (class / 클래스), nhìn private NAV ít biến động rồi kết luận rủi ro thấp, nhầm carry cao với expected return cao và bỏ qua embedded option/leverage.

**Gate hoàn thành:** phải so được ít nhất bốn asset lớp (class / 클래스) trên cùng một bảng `cash flow → duration → carry → liquidity → regime → failure mode → portfolio role`.

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

Dạng thất bại (failure mode / 실패 모드) gồm dự báo doanh thu bằng CAGR không có driver, dùng EPS mà bỏ qua cash conversion, loại mọi khoản “one-off”, dùng peak earnings để định giá doanh nghiệp chu kỳ, bỏ qua dilution/SBC, và tin vào moat không có bằng chứng kinh tế.

**Gate hoàn thành:** thay một driver vận hành phải làm thay đổi hợp lý ba báo cáo, FCF, valuation và thesis; phải có bear/cơ sở (base / 기반)/bull cùng vô hiệu hóa (invalidation / 무효화) cụ thể.

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

Dạng thất bại (failure mode / 실패 모드) gồm suy luận `CPI ↑ → cổ phiếu ↓`, nhầm mức (level / 수준) với rate-of-change, bỏ qua điều thị trường đã pricing, không tách demand shock và supply shock, nhầm liquidity hỗ trợ (support / 지원) với solvency repair và dùng một chỉ tiêu để gọi tên regime.

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

Dữ liệu phải được kiểm soát theo observation thời gian (time / 시간), publication thời gian (time / 시간), revision thời gian (time / 시간), quyết định (decision / 결정) thời gian (time / 시간) và thực thi (execution / 실행) thời gian (time / 시간). Kết quả phải bao gồm expectancy, phân phối (distribution / 분포), drawdown, turnover, slippage, hiện thực (implementation / 구현) shortfall, factor exposure, sức chứa (capacity / 용량) và margin stress.

Dạng thất bại (failure mode / 실패 모드) gồm look-ahead, survivorship, dữ liệu (data / 데이터) snooping, overfit tham số, chi phí (cost / 비용) mô hình (model / 모델) cố định, full-size ngay sau backtest, nhầm margin với economic exposure, dùng stop như bảo đảm chống gap và đánh giá chiến lược chỉ bằng Sharpe.

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

Dữ liệu phải nối được xuất khẩu, trade balance, FX, reserve/liquidity, tỷ lệ (rate / 비율)/credit, foreign luồng (flow / 흐름), thị trường (market / 시장) breadth, margin activity, sector revisions, company balance sheet và valuation. Với thông tin có tính thời điểm như chính sách, thuế, settlement, foreign room hoặc thị trường (market / 시장) classification phải kiểm tra nguồn chính thức trước khi dùng thực tế.

Dạng thất bại (failure mode / 실패 모드) gồm suy luận “KRW yếu = mọi exporter tốt”, “credit growth = mọi ngân hàng tốt”, nhầm liquidity rally với earnings khôi phục (recovery / 복구), dùng chỉ mục (index / 인덱스) return thay thị trường (market / 시장) breadth và bỏ qua custody/FX/tax/truy cập (access / 접근) trong cross-border return.

**Gate hoàn thành:** phải tạo được `country dashboard + sector map + company driver tree + valuation + liquidity-aware position plan + invalidation` cho ít nhất một trường hợp (case / 사례) Hàn Quốc và một trường hợp (case / 사례) Việt Nam.

## Advanced Practice Workbook — Biến kiến thức thành sản phẩm phân tích

[ADVANCED_PRACTICE_WORKBOOK.md](./ADVANCED_PRACTICE_WORKBOOK.md)

Workbook là bước bắt buộc nếu muốn tăng chiều sâu thực sự. Sáu mô-đun (module / 모듈) tương ứng sáu lĩnh vực (domain / 도메인) chính và mỗi mô-đun (module / 모듈) phải đi đủ:

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

### Kiểm tra (audit / 감사) workbook

Khi làm bài, không được chỉ điền kết quả. Mỗi câu trả lời cần phân biệt:

```text
Dữ kiện (fact)
Ước tính (estimate)
Giả định (assumption)
Diễn giải (interpretation)
Quyết định / rule
```

Mỗi mô-đun (module / 모듈) phải có ít nhất một bài **reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)** hoặc **counterfactual**. Ví dụ: thay vì chỉ hỏi “nếu yield tăng 100 bp thì sao?”, phải hỏi “điều kiện nào khiến hedge thất bại?” hoặc “kết quả nào quan sát được dù thesis ban đầu sai?”.

Một bài chỉ đạt khi có thể chỉ ra **dạng thất bại (failure mode / 실패 모드)** và dữ liệu xác nhận/bác bỏ, không chỉ tính đúng công thức.

## 07 — trường hợp (case / 사례) studies tích hợp

Các tình huống trong [07_integrated_case_studies](./07_integrated_case_studies/README.md) là nơi kiểm tra tích hợp (integration / 통합). Mỗi trường hợp (case / 사례) phải đi đủ chuỗi:

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

Nếu một trường hợp (case / 사례) dừng ở “macro tốt/xấu cho ngành”, trường hợp (case / 사례) đó chưa đủ sâu.

Ưu tiên worked trường hợp (case / 사례) có số liệu giả định để buộc người đọc tính duration, refinancing chi phí (cost / 비용), earnings sensitivity, valuation sensitivity và portfolio mất mát (loss / 손실) thay vì chỉ đọc narrative.

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

Capstone không được kết thúc bằng mục tiêu (target / 대상) price. Đầu ra cuối phải cho thấy **thesis sai trong điều kiện nào, bảng cân đối có sống sót không, danh mục chịu bao nhiêu mất mát (loss / 손실) trong bear trường hợp (case / 사례) và phần P/L sau đó đến từ thesis hay từ beta/multiple/FX**.

## Ma trận kiểm tra (audit / 감사) chiều sâu toàn thư viện (library / 라이브러리)

| lĩnh vực (domain / 도메인) | Concept | cơ chế (mechanism / 메커니즘) | dữ liệu (data / 데이터) | Interpretation | rủi ro (risk / 위험) | dạng thất bại (failure mode / 실패 모드) | trường hợp (case / 사례) / Practice |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Foundations | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Advanced Lab + Workbook |
| Asset Classes | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Advanced Lab + Workbook |
| Company phân tích (analysis / 분석) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Company Lab + sector cases |
| Economics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Macro Lab + CPI/credit cases |
| Trading & Derivatives | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | hệ thống (system / 시스템) Lab + Workbook |
| Korea / Vietnam | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | thị trường (market / 시장) Lab + country cases |

Dấu ✓ không có nghĩa nội dung đã “xong vĩnh viễn”. Nó có nghĩa thư viện (library / 라이브러리) đã có vị trí chuẩn gốc (canonical / 정본) cho lớp kiến thức đó. Nội dung mới chỉ nên được thêm khi làm sâu cơ chế, dữ liệu, dạng thất bại (failure mode / 실패 모드) hoặc trường hợp (case / 사례), không nên tạo chapter mới chỉ vì gặp một thuật ngữ mới.

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

Không chuyển sang lab tiếp theo nếu chỉ “đọc hiểu”. Hãy tự tạo ít nhất một mô hình, bảng phân tích hoặc trường hợp (case / 사례) thực hành.

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

Nếu tầng đầu giúp trả lời **“khái niệm này là gì?”**, tầng Advanced giúp trả lời **“cơ chế hoạt động thế nào và dữ liệu nào chứng minh?”**, còn Workbook/trường hợp (case / 사례)/Capstone phải giúp trả lời **“dạng thất bại (failure mode / 실패 모드) là gì, tác động tới valuation/danh mục bao nhiêu và làm sao biết mình đang sai?”**.

> **Bàn giao:** Sau **Kết luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 GLOSSARY FORMULAS AND RESEARCH CONVENTIONS](./00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
