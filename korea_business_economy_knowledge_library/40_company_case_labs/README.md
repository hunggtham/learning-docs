# Phòng thực hành phân tích doanh nghiệp Hàn Quốc (Company Case Labs)

Thư mục này là lớp **thực hành (application)** của bộ tài liệu về doanh nghiệp và kinh tế Hàn Quốc. Các chương trước xây dựng mô hình tư duy (mental model) về lịch sử, kinh tế vĩ mô (macro), ngành, kế toán (accounting), quản trị doanh nghiệp (corporate governance) và thị trường vốn (capital market). Các bài thực hành ở đây buộc người đọc dùng những mô hình đó trên một doanh nghiệp hoặc một cấu trúc kinh doanh cụ thể.

Mục tiêu không phải đưa ra khuyến nghị mua/bán hay giá mục tiêu (target price). Mỗi bài được thiết kế như một phòng thí nghiệm: bắt đầu từ pháp nhân (legal entity) và hàm sản xuất (production function), dựng cây động lực (driver tree), xác định nơi lợi nhuận kinh tế (economic profit) được tạo ra, nối các động lực với báo cáo tài chính (financial statements), rồi kiểm tra sức chịu đựng (stress test) của bảng cân đối kế toán, cơ cấu quản trị, nguồn vốn và các giả định định giá.

## Cách sử dụng các bài thực hành

Không nên đọc một bài như bài giới thiệu công ty. Trước mỗi phần, hãy tự trả lời câu hỏi rồi mới đọc lời giải thích. Khi gặp số liệu tại một thời điểm (snapshot), luôn giữ ngày tham chiếu. Một con số đúng ở năm tài chính 2025 (FY2025) không phải là sự thật cấu trúc bất biến cho FY2027.

Quy trình chung:

```text
Xác định đúng pháp nhân
→ Hiểu kiến trúc kinh doanh và hàm sản xuất
→ Dựng cây động lực doanh thu và chi phí
→ Xác định vị thế trong ngành
→ Chuyển cơ chế kinh tế thành số liệu kế toán
→ Theo dõi quá trình chuyển lợi nhuận thành tiền mặt
→ Đánh giá sức chịu đựng của bảng cân đối kế toán
→ Phân tích quản trị và phân bổ vốn
→ Theo dõi tác động truyền dẫn từ kinh tế vĩ mô
→ Xây dựng kịch bản và kiểm tra sức chịu đựng
→ Hiểu logic định giá
→ Xác định điều kiện làm giả thuyết đầu tư không còn đúng
```

Các file sử dụng ba loại dữ liệu. **Sự thật cấu trúc (structural fact)** là đặc điểm tương đối bền, chẳng hạn ngành bộ nhớ bán dẫn có cường độ chi phí cố định (fixed-cost intensity) cao. **Số liệu tại thời điểm (snapshot fact)** là dữ liệu có ngày cụ thể như doanh thu của một năm tài chính. **Giả định mô phỏng (stylized assumption)** là con số được đặt ra để phục vụ bài tập và phải luôn được nhận diện rõ là giả định.

## Bản đồ các bài thực hành

| Bài thực hành | Cơ chế kinh tế trung tâm | Kỹ năng chính |
|---|---|---|
| [Samsung Electronics](./00_samsung_electronics_semiconductor_cycle_case.md) | Điện tử đa phân khúc + bán dẫn | tách phân khúc, chu kỳ, chi tiêu vốn (CAPEX) |
| [SK hynix](./01_sk_hynix_hbm_memory_case.md) | Công suất bộ nhớ/HBM | giá bán bình quân (ASP), cơ cấu sản phẩm, tỷ lệ thành phẩm đạt chuẩn (yield), phân bổ wafer |
| [Hyundai Motor](./02_hyundai_motor_auto_finance_ev_case.md) | Nền tảng ô tô + tài chính nội bộ | sản lượng, cơ cấu sản phẩm, ưu đãi bán hàng, tài chính, chuyển đổi EV |
| [NAVER](./03_naver_platform_ai_cloud_case.md) | Nền tảng số | người dùng, kiếm tiền (monetization), GMV/TPV, AI và đám mây |
| [Nhà cung cấp SME Hàn Quốc](./04_korean_sme_supplier_case.md) | Nhà cung cấp linh kiện B2B | tập trung khách hàng, vốn lưu động (working capital) |
| [LG CNS](./05_lg_cns_si_sm_cloud_case.md) | SI/SM + đám mây và dịch vụ quản lý | tỷ lệ sử dụng nhân lực, đơn giá tính phí, rủi ro dự án, doanh thu lặp lại |
| [Shinhan Financial Group](./06_shinhan_financial_group_bank_case.md) | Tập đoàn tài chính/ngân hàng | biên lãi ròng (NIM), chi phí tín dụng, RWA, CET1, phân bổ vốn |
| [LG Energy Solution](./07_lg_energy_solution_battery_case.md) | Công suất pin | GWh, tỷ lệ sử dụng công suất, yield, cơ chế chuyển giá nguyên liệu, CAPEX |
| [Hanwha Aerospace](./08_hanwha_aerospace_defense_backlog_case.md) | Hợp đồng quốc phòng dài hạn | chuyển đơn hàng tồn đọng thành doanh thu, mua sắm quốc phòng, vốn lưu động |
| [Coupang](./09_coupang_commerce_logistics_case.md) | Thương mại + mạng lưới hoàn tất đơn hàng | mật độ mạng lưới, thành viên, tồn kho, lợi nhuận đóng góp |
| [Xây dựng và PF](./10_korean_construction_pf_case.md) | Phát triển dự án + tài trợ dự án | khoản vay cầu nối → 본PF, bán trước, bảo lãnh, tái cấp vốn |

## Vì sao cần nhiều mô hình doanh nghiệp khác nhau?

Không có một mẫu tài chính duy nhất phù hợp với mọi doanh nghiệp. Mỗi loại hình tạo doanh thu, chi phí và dòng tiền theo một cơ chế khác nhau.

```text
Bán dẫn
→ công suất × tỷ lệ sử dụng × yield × ASP

Ngân hàng
→ tài sản sinh lãi × NIM - chi phí tín dụng, trong giới hạn vốn an toàn

Nền tảng số
→ người dùng × mức độ tương tác × khả năng kiếm tiền

SI/SM
→ nhân lực có thể tính phí × tỷ lệ sử dụng × đơn giá + dịch vụ lặp lại

Quốc phòng
→ đơn hàng tồn đọng × tốc độ chuyển đổi × biên lợi nhuận × thời điểm thu/chi tiền

Thương mại/logistics
→ khách hàng × số đơn hàng × lợi nhuận đóng góp mỗi đơn, phụ thuộc mật độ mạng lưới

Xây dựng/PF
→ doanh thu dự án - chi phí dự án - chi phí tài chính, khuếch đại bởi đòn bẩy và bảo lãnh
```

Điều cần học không phải thuộc lòng công thức. Hãy nhận ra **hàm sản xuất (production function)** của doanh nghiệp rồi chọn đúng cách đọc kế toán và định giá.

## Lộ trình 1 — Sản xuất và nền kinh tế xuất khẩu

```text
Samsung Electronics
→ SK hynix
→ Hyundai Motor
→ LG Energy Solution
→ Hanwha Aerospace
```

Lộ trình này cho thấy sản xuất Hàn Quốc không phải một khu vực đồng nhất. Bộ nhớ có chu kỳ hàng hóa–công nghệ; ô tô chịu tác động của cơ cấu sản phẩm và tài chính nội bộ; pin phụ thuộc quá trình tăng công suất; quốc phòng phụ thuộc mua sắm công và đơn hàng tồn đọng.

## Lộ trình 2 — Kinh tế số và dịch vụ

```text
NAVER
→ Coupang
→ LG CNS
```

NAVER giúp hiểu cách một nền tảng số chuyển quy mô người dùng thành doanh thu, đồng thời vẫn phải đầu tư CAPEX cho AI và đám mây. Coupang cho thấy một công ty số có thể đồng thời là một mạng lưới logistics vật lý rất lớn. LG CNS cho thấy doanh nghiệp CNTT cho khách hàng doanh nghiệp lại phụ thuộc mạnh vào tỷ lệ sử dụng nhân lực, hợp đồng dự án và dịch vụ quản lý có tính lặp lại.

## Lộ trình 3 — Hệ thống tài chính và đòn bẩy

```text
Shinhan Financial Group
→ Xây dựng & PF
→ Nhà cung cấp SME Hàn Quốc
```

Bài về ngân hàng cho thấy tín dụng được tạo ra và định giá như thế nào. Bài PF cho thấy tín dụng đi vào dự án và có thể quay trở lại hệ thống tài chính thông qua tái cấp vốn hoặc bảo lãnh. Bài SME cho thấy vốn lưu động và vốn vay ngân hàng tác động trực tiếp đến một doanh nghiệp sản xuất như thế nào.

## Lộ trình 4 — Hiểu doanh nghiệp nơi mình làm việc

Nếu doanh nghiệp thuộc SI/SM, là nhà cung cấp hoặc là công ty con của một tập đoàn Hàn Quốc, có thể đọc theo chuỗi:

```text
LG CNS
→ Nhà cung cấp SME Hàn Quốc
→ Case về tập đoàn mẹ hoặc ngành tương ứng
→ 12_labor
→ 13_business_culture
→ 05_group_structure
→ 08_governance
```

Đừng chỉ hỏi doanh nghiệp “lớn hay nhỏ”. Hãy hỏi pháp nhân đó nằm ở đâu trong chuỗi giá trị (value chain), ai là khách hàng, ai quyết định ngân sách, doanh thu mang tính lặp lại hay theo dự án, doanh nghiệp có quyền định giá (pricing power) hay không và năng lực nghề nghiệp được tích lũy ở tầng nào.

## Quan hệ với các chương khác

Trước khi làm bài thực hành nên đọc [cách phân tích một công ty Hàn Quốc](../20_how_to_analyze_a_korean_company.md) và [workbook phân tích doanh nghiệp](../39_practical_company_analysis_workbook_and_case_patterns.md). Khi cần đọc kế toán, quay lại [DART/KIND và báo cáo tài chính](../09_disclosure_accounting_dart_kind.md) cùng [chất lượng lợi nhuận và dấu hiệu cảnh báo](../38_forensic_accounting_red_flags_and_earnings_quality.md). Khi cần hiểu nguồn vốn, nợ và rủi ro giảm giá trị, dùng [ngân hàng và tài trợ doanh nghiệp](../11_banks_finance_and_corporate_funding.md) cùng [xếp hạng tín dụng, trái phiếu và tái cơ cấu](../36_credit_ratings_bonds_default_and_restructuring.md).

## Khung chung để tự tạo bài thực hành mới

Khi gặp một doanh nghiệp chưa có trong thư mục, không nên sao chép máy móc bài gần nhất. Hãy tự dựng mô hình bằng các câu hỏi sau:

```text
1. Pháp nhân (legal entity) thực sự đang phân tích là gì?
2. Khách hàng trả tiền cho điều gì?
3. Đơn vị kinh tế tự nhiên là gì: xe, wafer, GWh, người dùng, khoản vay, dự án hay ngày công lập trình viên?
4. Doanh thu = mức hoạt động × khả năng kiếm tiền nào?
5. Chi phí nào biến đổi, chi phí nào cố định?
6. Tài sản hoặc vốn nào bắt buộc để mở rộng quy mô?
7. Vốn lưu động vận hành ra sao?
8. Giới hạn về nợ hoặc vốn nằm ở đâu?
9. Biến số kinh tế vĩ mô nào truyền tác động trực tiếp nhất?
10. Khoản mục kế toán nào dễ che khuất thực tế kinh tế?
11. Kịch bản nào có chuỗi nguyên nhân–kết quả hợp lý?
12. Bằng chứng nào sẽ bác bỏ giả thuyết ban đầu?
```

Nếu trả lời được các câu này, ta đã có bộ khung của một mô hình phân tích doanh nghiệp.

## Mental Model — Mô hình tư duy

> Học phân tích doanh nghiệp không phải học thuộc danh sách công ty. Ta đang học một **từ vựng về các cơ chế tạo giá trị (production functions)**. Khi nhận ra doanh nghiệp thuộc loại “cỗ máy kinh tế” nào, ta biết nên nhìn động lực, kế toán, rủi ro và dòng tiền ở đâu.

Một bài phân tích tốt không kết thúc bằng câu “doanh nghiệp này tốt/xấu”. Nó kết thúc bằng một mô hình nhân quả có thể bị kiểm chứng hoặc bác bỏ:

```text
Nếu A xảy ra
→ động lực B thay đổi
→ biên lợi nhuận hoặc dòng tiền C thay đổi
→ bảng cân đối hoặc định giá D thay đổi.

Nếu bằng chứng E không xuất hiện trong khoảng thời gian T
→ giả thuyết ban đầu phải được sửa hoặc loại bỏ.
```
