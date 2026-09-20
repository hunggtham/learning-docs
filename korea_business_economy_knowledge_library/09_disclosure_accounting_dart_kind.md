# Disclosure, accounting, DART và KIND (기업공시·회계·DART·KIND)

Muốn đi từ “nghe nói công ty này tốt” sang phân tích có thể kiểm chứng, cần biết nơi doanh nghiệp buộc hoặc tự nguyện công bố dữ liệu. Ở Hàn Quốc, hai hệ thống quan trọng là **DART (전자공시시스템)** của Financial Supervisory Service và **KIND (한국거래소 기업공시채널)** của Korea Exchange.

## Disclosure giải quyết vấn đề asymmetric information

Management biết nhiều về business hơn investor, lender và supplier. Đây là **bất cân xứng thông tin (information asymmetry / 정보비대칭)**. Disclosure giảm gap bằng cách yêu cầu công bố periodic reports, material events, ownership changes và các thông tin khác.

Không phải disclosure làm thông tin “hoàn toàn đúng”; nó làm thông tin có format, accountability và audit trail tốt hơn. Chính DART English cũng lưu ý rằng bản tiếng Anh có thể mang tính voluntary và nên đối chiếu filing tiếng Hàn khi cần chính xác pháp lý.

## Các report quan trọng

**사업보고서** là annual business report; **반기보고서** là half-year report; **분기보고서** là quarterly report. Với listed company, đây thường là điểm bắt đầu để hiểu business segments, subsidiaries, shareholder, debt, employees, litigation và financial statements.

**주요사항보고서** hoặc exchange material disclosure báo các sự kiện lớn: capital increase, M&A, asset acquisition/disposal, major contracts và thay đổi tài chính đáng kể tùy trường hợp.

## Consolidated statements

Ba statement cơ bản là:

**Bảng cân đối kế toán (Statement of Financial Position / 재무상태표)** cho biết stock của assets, liabilities và equity tại một thời điểm.

**Báo cáo kết quả kinh doanh (Income Statement / 손익계산서)** cho biết revenue, expense và profit trong một period.

**Báo cáo lưu chuyển tiền tệ (Cash Flow Statement / 현금흐름표)** cho biết cash thực di chuyển qua operating, investing và financing activities.

Một company có net income dương nhưng operating cash flow âm nếu receivables/inventory tăng mạnh. Vì thế profit không phải cash.

## Revenue, operating profit và net income

Doanh thu (Revenue / 매출액) là top line. **Operating profit / 영업이익** đo profit từ operating activities trước nhiều non-operating items. **Net income / 당기순이익** sau interest, tax và các item khác. Margin:

\[
Operating\ Margin=\frac{Operating\ Profit}{Revenue}
\]

Margin tăng có thể do ASP, product mix, cost efficiency hoặc operating leverage. Cần đọc notes để biết mechanism.

## Cash flow và capex

Một semiconductor company có thể ghi operating profit lớn nhưng phải chi capital expenditure (CAPEX / 설비투자) cực lớn. Free cash flow đơn giản thường được mentalize là:

\[
FCF \approx Operating\ Cash\ Flow - Capital\ Expenditure
\]

Đây không phải universal accounting definition nhưng hữu ích để reasoning capital intensity.

## DART vs KIND

DART là repository rộng về corporate filings dưới Financial Supervisory Service. KIND tập trung disclosure của listed companies dưới KRX, gồm timely market disclosures. Khi nghiên cứu listed company, nên dùng cả hai: DART cho report structure sâu, KIND cho event flow và listing context.

## XBRL và data

XBRL (eXtensible Business Reporting Language / 확장성 경영보고언어) biến statement thành machine-readable tags. Với IT/data analysis, đây là cầu nối trực tiếp giữa accounting và programming: thay vì scrape PDF, có thể parse structured financial data khi source hỗ trợ.

## DART nên được đọc như database, không như website tin tức

DART (전자공시시스템) là nơi filing có legal significance. Một company có hàng trăm filings mỗi năm; skill quan trọng là biết document nào answer question nào. Annual/business report cho business model và financials; major-event filing cho financing, M&A, litigation hoặc restructuring; equity ownership filings cho controlling stakes.

KIND của KRX thiên về listed-company market disclosure, listing status, trading halt, corporate actions và exchange notices. Hai hệ thống bổ sung nhau.

## Business report anatomy

`사업보고서` thường chứa company overview, business segments, major products, raw materials, capacity, sales, risk, directors, shareholders, related-party information và audited statements. Analyst không nên chỉ mở financial tables.

Ví dụ muốn biết semiconductor margin risk, section raw-material/capacity và segment note có thể quan trọng hơn headline revenue.

## Separate vs consolidated statements

Holding parent có separate revenue rất nhỏ nhưng consolidated group revenue rất lớn. Nếu chỉ đọc 별도재무제표 có thể hiểu sai business. Ngược lại, dividend-paying capacity của parent đôi khi phụ thuộc separate cash/dividends received from subsidiaries, nên consolidated alone cũng chưa đủ.

Hai statement answer different questions: consolidated = economic group under control; separate = legal parent entity.

## Income statement quality

Operating profit giúp xem core operations nhưng classification có thể khác industry. Net income gồm finance income/expense, tax và non-operating items. One-off asset sale có thể làm net income cao mà core business không cải thiện.

Vì vậy hãy bridge:

```text
Revenue
→ gross/operating profit
→ finance & other items
→ pre-tax income
→ tax
→ net income
→ parent-attributable income
```

## Cash flow reconciliation

Operating cash flow khác net income vì depreciation, working capital và non-cash items. Capex thường nằm investing cash flow. Free cash flow không phải statutory line item nên analyst phải định nghĩa nhất quán.

Một company growing rapidly có negative FCF vì capex, điều này không tự động xấu; nhưng phải hỏi capex tạo future ROIC nào.

## Footnotes là nơi risk sống

Guarantees, litigation, related-party balances, debt maturity, derivative hedge, pension obligations và commitments thường nằm trong notes. Headline balance sheet có thể nhìn clean trong khi note reveals large contingent exposure.

Construction/PF là ví dụ điển hình: guarantee exposure có thể quan trọng hơn recognized debt.

## Restatement và audit opinion

Audit opinion không phải guarantee company “tốt”, mà nói financial statements có được trình bày fairly theo framework trong material respects hay không. Qualified/adverse/disclaimer opinions là serious signals; even unqualified opinion không loại fraud risk hoàn toàn.

Restatement (정정공시) phải đọc cả original và corrected item để hiểu change materiality.

## Practical workflow với một company mới

Bắt đầu bằng latest annual/quarterly report, xác định entity và segments. Sau đó đọc ownership, related parties và debt. Tiếp theo search major-event filings 2–3 năm. Cuối cùng dùng KIND/IR materials để nối filing với market events. Workflow này nhanh hơn đọc news trước rồi cố confirm sau.

## Mental Model

> Disclosure là “API công khai” của doanh nghiệp. Press release là narrative; filing là payload có schema, legal responsibility và historical trace.

## Common misconceptions

Revenue growth không đồng nghĩa business khỏe nếu receivables, debt và inventory phình nhanh hơn.

Net cash ở parent standalone cũng không nhất thiết phản ánh cash tự do dùng ở toàn group; subsidiary restrictions và NCI matter.

## Practical reading order

Khi mở một 사업보고서, cách đọc hiệu quả là bắt đầu bằng business overview và segment; sau đó ownership/subsidiaries; tiếp theo income/cash flow/balance sheet; cuối cùng notes về debt, related parties, contingencies và commitments. Đọc notes sau cùng không có nghĩa chúng ít quan trọng; nó giúp có mental map trước khi vào chi tiết.

## Sources & connections

Nguồn: Financial Supervisory Service DART/OPEN DART và Korea Exchange KIND.

Xem [10_capital_markets_kospi_kosdaq_konex](./10_capital_markets_kospi_kosdaq_konex.md) và [20_how_to_analyze_a_korean_company](./20_how_to_analyze_a_korean_company.md).
### Nguồn kiểm tra hiện hành

- DART: https://dart.fss.or.kr/
- English DART: https://englishdart.fss.or.kr/
- KIND: https://kind.krx.co.kr/

