# Company Case Labs — thực hành phân tích doanh nghiệp Hàn Quốc

Folder này là lớp **application** của Korea Business & Economy Knowledge Library. Các chapter trước xây mental model về lịch sử, macro, industry, accounting, governance và capital market; các case lab ở đây buộc người đọc dùng những mental model đó trên một company cụ thể.

Mục tiêu không phải đưa ra khuyến nghị mua/bán hay target price. Mỗi case được thiết kế như một phòng thí nghiệm: bắt đầu từ legal entity và business model, dựng driver tree, tìm nơi economic profit được tạo ra, nối driver với financial statements, sau đó stress-test balance sheet, governance và valuation assumptions.

## Cách dùng case lab

Không nên đọc case như một bài giới thiệu công ty. Trước mỗi section, hãy tự trả lời câu hỏi rồi mới đọc phần giải thích. Khi gặp số liệu snapshot, luôn giữ ngày tham chiếu. Một con số đúng ở FY2025 không phải structural truth của FY2027.

Workflow chung:

```text
Entity resolution
→ Business architecture
→ Revenue / cost driver tree
→ Industry position
→ Accounting translation
→ Cash conversion
→ Balance-sheet capacity
→ Governance / capital allocation
→ Macro transmission
→ Scenario / stress test
→ Valuation logic
→ Thesis breakers
```

Các file sử dụng ba loại dữ liệu. **Structural fact** là đặc điểm tương đối bền như Samsung Electronics có DX và DS, hoặc memory semiconductor có fixed-cost intensity cao. **Snapshot fact** là dữ liệu có ngày như revenue FY2025. **Stylized assumption** là số giả định phục vụ bài tập và luôn được ghi rõ là giả định.

## Các case

1. [Samsung Electronics — multi-engine conglomerate inside one listed entity](./00_samsung_electronics_semiconductor_cycle_case.md): học cách tách DX, DS, SDC và Harman; tránh dùng consolidated profit như một business duy nhất; phân tích memory cycle, foundry economics và capital allocation.
2. [SK hynix — HBM, memory cycle và capacity allocation](./01_sk_hynix_hbm_memory_case.md): học cách đi từ AI compute demand tới HBM mix, wafer allocation, yield, ASP, depreciation, CAPEX và FCF.
3. [Hyundai Motor — auto manufacturing, mix, captive finance và EV transition](./02_hyundai_motor_auto_finance_ev_case.md): nối units, ASP/mix, incentives, FX, warranty, finance subsidiary và transition CAPEX.
4. [NAVER — search, commerce, fintech, content, cloud và AI](./03_naver_platform_ai_cloud_case.md): phân biệt user scale với monetization, GMV với revenue, payment volume với fintech revenue và AI narrative với incremental economics.
5. [Korean SME supplier — customer concentration và cash conversion](./04_korean_sme_supplier_case.md): một case giả lập nhưng sát cấu trúc supplier Hàn Quốc, dùng để học bargaining power, annual price-down, tooling, receivable, inventory và customer relocation risk.
6. [LG CNS — SI/SM, cloud, AX và project economics](./05_lg_cns_si_sm_cloud_case.md): đọc IT-service company bằng utilization, billing rate, backlog, fixed-price risk, subcontracting, recurring SM/cloud và captive-vs-external demand.

## Quan hệ với các chapter khác

Trước khi làm case nên đọc [20_how_to_analyze_a_korean_company](../20_how_to_analyze_a_korean_company.md) và [39_practical_company_analysis_workbook_and_case_patterns](../39_practical_company_analysis_workbook_and_case_patterns.md). Khi cần accounting quay lại [09_disclosure_accounting_dart_kind](../09_disclosure_accounting_dart_kind.md) và [38_forensic_accounting_red_flags_and_earnings_quality](../38_forensic_accounting_red_flags_and_earnings_quality.md). Khi cần hiểu funding, debt và downside, dùng [11_banks_finance_and_corporate_funding](../11_banks_finance_and_corporate_funding.md) cùng [36_credit_ratings_bonds_default_and_restructuring](../36_credit_ratings_bonds_default_and_restructuring.md).

## Quy tắc quan trọng nhất

Một company case không kết thúc ở câu “doanh nghiệp này tốt/xấu”. Output tốt hơn là một causal model có thể bị falsify:

```text
Nếu A xảy ra
→ driver B thay đổi
→ margin/cash C thay đổi
→ balance sheet hoặc valuation D thay đổi.

Nếu evidence E không xuất hiện trong thời gian T
→ giả thuyết ban đầu phải được sửa hoặc bỏ.
```

Đây là cách chuyển knowledge thành analytical skill.