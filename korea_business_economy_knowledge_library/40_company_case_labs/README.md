# Company Case Labs — thực hành phân tích doanh nghiệp Hàn Quốc

Folder này là lớp **application** của Korea Business & Economy Knowledge Library. Các chapter trước xây mental model về lịch sử, macro, industry, accounting, governance và capital market; các case lab ở đây buộc người đọc dùng những mental model đó trên một company hoặc business structure cụ thể.

Mục tiêu không phải đưa ra khuyến nghị mua/bán hay target price. Mỗi case được thiết kế như một phòng thí nghiệm: bắt đầu từ legal entity và production function, dựng driver tree, tìm nơi economic profit được tạo ra, nối driver với financial statements, sau đó stress-test balance sheet, governance, funding và valuation assumptions.

## Cách dùng case lab

Không nên đọc case như một bài giới thiệu công ty. Trước mỗi section, hãy tự trả lời câu hỏi rồi mới đọc phần giải thích. Khi gặp số liệu snapshot, luôn giữ ngày tham chiếu. Một con số đúng ở FY2025 không phải structural truth của FY2027.

Workflow chung:

```text
Entity resolution
→ Business architecture / production function
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

Các file sử dụng ba loại dữ liệu. **Structural fact** là đặc điểm tương đối bền như memory semiconductor có fixed-cost intensity cao. **Snapshot fact** là dữ liệu có ngày như revenue một fiscal year cụ thể. **Stylized assumption** là số giả định phục vụ bài tập và luôn phải được nhận diện là giả định.

## Case Map

| Case | Production function trung tâm | Skill chính |
|---|---|---|
| [Samsung Electronics](./00_samsung_electronics_semiconductor_cycle_case.md) | Multi-segment electronics + semiconductor | segment decomposition, cycle, CAPEX |
| [SK hynix](./01_sk_hynix_hbm_memory_case.md) | Memory/HBM capacity | ASP, mix, yield, wafer allocation |
| [Hyundai Motor](./02_hyundai_motor_auto_finance_ev_case.md) | Auto platform + captive finance | units, mix, incentives, finance, transition |
| [NAVER](./03_naver_platform_ai_cloud_case.md) | Digital platform | users, monetization, GMV/TPV, AI/cloud |
| [Korean SME supplier](./04_korean_sme_supplier_case.md) | B2B component supplier | customer concentration, working capital |
| [LG CNS](./05_lg_cns_si_sm_cloud_case.md) | SI/SM + cloud/managed service | utilization, billing, project risk, recurring mix |
| [Shinhan Financial Group](./06_shinhan_financial_group_bank_case.md) | Financial holding / banking | NIM, credit cost, RWA, CET1, capital allocation |
| [LG Energy Solution](./07_lg_energy_solution_battery_case.md) | Battery capacity | GWh, utilization, yield, pass-through, CAPEX |
| [Hanwha Aerospace](./08_hanwha_aerospace_defense_backlog_case.md) | Long-cycle defense contracts | backlog conversion, procurement, working capital |
| [Coupang](./09_coupang_commerce_logistics_case.md) | Commerce + fulfillment network | density, membership, inventory, contribution economics |
| [Construction & PF](./10_korean_construction_pf_case.md) | Project development / construction finance | bridge→본PF, presales, guarantees, refinancing |

## Vì sao cần nhiều case khác nhau?

Không có một template tài chính duy nhất phù hợp mọi business.

```text
Semiconductor
→ capacity × utilization × yield × ASP

Bank
→ earning assets × NIM - credit cost, constrained by capital

Platform
→ users × engagement × monetization

SI/SM
→ billable resources × utilization × rate + recurring service

Defense
→ backlog × conversion × margin × cash timing

Commerce/logistics
→ customers × orders × contribution/order, constrained by density

Construction/PF
→ project sales - project cost - financing, amplified by leverage/guarantees
```

Điều cần học không phải thuộc lòng formula. Hãy nhận ra **production function** của company rồi chọn đúng accounting và valuation lens.

## Reading Path 1 — Manufacturing và export economy

```text
Samsung Electronics
→ SK hynix
→ Hyundai Motor
→ LG Energy Solution
→ Hanwha Aerospace
```

Path này cho thấy Korean manufacturing không phải một homogeneous sector. Memory có commodity/technology cycle; auto có product mix và captive finance; battery có capacity ramp; defense có procurement/backlog.

## Reading Path 2 — Digital và service economy

```text
NAVER
→ Coupang
→ LG CNS
```

NAVER giúp hiểu asset-light-ish digital monetization nhưng vẫn có AI/cloud CAPEX. Coupang cho thấy digital company có thể trở thành physical logistics network. LG CNS cho thấy enterprise IT lại phụ thuộc human utilization, project contracts và recurring managed services.

## Reading Path 3 — Financial system và leverage

```text
Shinhan Financial Group
→ Construction & PF
→ Korean SME supplier
```

Bank case cho thấy credit được tạo và priced thế nào. PF case cho thấy credit đi vào project và có thể quay lại financial system qua refinancing/guarantees. SME case cho thấy working capital và bank funding tác động real company ra sao.

## Reading Path 4 — Nếu mục tiêu là hiểu company nơi mình làm việc

Nếu company là Korean SI/SM, supplier hoặc subsidiary của business group:

```text
LG CNS case
→ Korean SME supplier case
→ relevant parent-group / industry case
→ 12_labor
→ 13_business_culture
→ 05_group_structure
→ 08_governance
```

Đừng chỉ hỏi company “lớn hay nhỏ”. Hãy hỏi vị trí của legal entity trong value chain, ai là customer, ai quyết định budget, revenue recurring hay project-based, company có pricing power không và skill/career capital được tích lũy ở layer nào.

## Quan hệ với các chapter khác

Trước khi làm case nên đọc [20_how_to_analyze_a_korean_company](../20_how_to_analyze_a_korean_company.md) và [39_practical_company_analysis_workbook_and_case_patterns](../39_practical_company_analysis_workbook_and_case_patterns.md). Khi cần accounting quay lại [09_disclosure_accounting_dart_kind](../09_disclosure_accounting_dart_kind.md) và [38_forensic_accounting_red_flags_and_earnings_quality](../38_forensic_accounting_red_flags_and_earnings_quality.md). Khi cần hiểu funding, debt và downside, dùng [11_banks_finance_and_corporate_funding](../11_banks_finance_and_corporate_funding.md) cùng [36_credit_ratings_bonds_default_and_restructuring](../36_credit_ratings_bonds_default_and_restructuring.md).

Industry dependencies:

```text
Semiconductor → 14
Auto/Battery → 15
Platform/Commerce → 17 + 33
Construction/PF → 18
Defense → 32
IT/SI/SM → 34
Financial group → 35
```

## Một framework chung để tự tạo case thứ 12

Khi gặp company chưa có trong folder, đừng copy case gần nhất một cách máy móc. Hãy tự dựng:

```text
1. Legal entity là gì?
2. Customer trả tiền cho cái gì?
3. Unit kinh tế tự nhiên là gì? car, wafer, GWh, user, loan, project hay developer-day?
4. Revenue = activity × monetization nào?
5. Cost nào variable, cost nào fixed?
6. Asset/capital nào bắt buộc để scale?
7. Working capital hoạt động ra sao?
8. Debt/capital constraint nằm ở đâu?
9. Macro variable nào truyền trực tiếp nhất?
10. Accounting line nào dễ che economic reality?
11. Scenario nào có causal coherence?
12. Evidence nào sẽ falsify thesis?
```

Nếu trả lời được 12 câu này, bạn đã có skeleton của một company-analysis model.

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

> **Mental Model:** học company analysis không phải học danh sách công ty. Ta đang học một vocabulary của production functions. Khi nhận ra company thuộc loại economic machine nào, ta biết nên nhìn driver, accounting, risk và cash flow ở đâu.