# Thư viện Kiến thức Tài chính Cá nhân (Personal Finance Knowledge Library)

`personal-finance/` là thư viện chuẩn gốc (canonical / 정본) cho các quyết định tài chính ở cấp cá nhân và hộ gia đình: kiếm tiền, giữ tiền, thanh toán, vay nợ, bảo vệ trước rủi ro, thuế, nhà ở, phương tiện, quỹ dự phòng, chuẩn bị cho tuổi nghỉ hưu, khả năng chống chịu tài chính, các vấn đề xuyên biên giới và cách vận hành household financial system qua các life event lớn. Nó được tách khỏi [Investing](../investing/README.md) vì **quản lý tài chính cá nhân (personal finance / 개인 재무) không đồng nghĩa đầu tư (investing / 투자)**.

Theo OECD, hiểu biết tài chính (financial literacy / 금융 이해력) không chỉ là biết một sản phẩm đầu tư mà còn gồm kiến thức, kỹ năng, thái độ và hành vi giúp cá nhân ra quyết định tài chính, duy trì khả năng chống chịu tài chính (financial resilience / 금융 회복탄력성) và cải thiện well-being. Vì vậy library này không được viết như một danh sách “mua gì để sinh lời”; câu hỏi trung tâm là: **một người biến thu nhập, nghĩa vụ, rủi ro và mục tiêu qua thời gian thành một hệ thống tài chính có khả năng hoạt động cả khi điều kiện bình thường bị phá vỡ như thế nào?**

> Phạm vi của tài liệu là giáo dục. Lãi suất, thuế, bảo hiểm, tín dụng, hưu trí, quyền người tiêu dùng và thủ tục xuyên biên giới phụ thuộc quốc gia, thời điểm và hợp đồng cụ thể; trước quyết định thực tế phải kiểm tra quy định và điều khoản hiện hành tại nơi áp dụng.

Để kiểm tra phần nào đã đủ core, phần nào time-sensitive và phần nào không nên tiếp tục mở rộng chỉ để tăng số file, xem [Coverage & Depth Audit](./COVERAGE_AUDIT.md).

## Ranh giới với Economics và Investing

Ba domain nối nhau nhưng sở hữu các câu hỏi khác nhau:

```text
Personal Finance
  cá nhân/hộ gia đình quản lý tiền, nghĩa vụ, liquidity và resilience
        ↓
Economics
  giải thích cơ chế giá, lạm phát, lãi suất, thị trường và chính sách
        ↓
Investing
  phân bổ vốn vào tài sản, doanh nghiệp và chiến lược với rủi ro kỳ vọng
      ↙        ↘
Stocks      Forex
```

Nếu câu hỏi là “lạm phát hình thành và truyền qua nền kinh tế thế nào?”, owner là [Economics](../economics/README.md). Nếu câu hỏi là “lạm phát làm sức mua của tiền tiết kiệm và khoản vay thay đổi thế nào?”, owner là chapter [04 — Inflation](./04-inflation.md). Nếu câu hỏi là “môi trường lạm phát ảnh hưởng định giá cổ phiếu, trái phiếu hay vị thế ngoại hối thế nào?”, owner là [Investing](../investing/README.md).

Tương tự, library này giải thích quỹ dự phòng (emergency fund / 비상자금), cấu trúc nợ (debt structure / 부채 구조), bảo hiểm (insurance / 보험), bảng cân đối cá nhân (personal balance sheet / 개인 대차대조표), khả năng chống chịu tài chính (financial resilience / 금융 회복탄력성), household FX exposure, life-cycle decisions và review loop. Khi tiền đã thực sự trở thành investable surplus và người học cần asset allocation, valuation, portfolio risk hay trading, hãy chuyển sang Investing thay vì lặp lại nội dung ở đây.

## Ranh giới với Korea Law, Civic & Everyday Life

`personal-finance/` giữ **decision framework** dùng chung. Các thủ tục pháp lý và hành chính cụ thể tại Hàn Quốc đã có canonical owner tại [Korea Law, Civic & Everyday Life](../korea_law_civic_life/README.md), đặc biệt:

- [Housing — 월세, 전세, 보증금](../korea_law_civic_life/06_housing_wolse_jeonse_deposit_and_registration.md)
- [Taxes, social insurance, welfare & healthcare](../korea_law_civic_life/07_taxes_social_insurance_welfare_healthcare.md)
- [Banking, credit & financial consumer protection](../korea_law_civic_life/08_banking_credit_and_financial_consumer.md)

[16 — Korea–Vietnam Practical Map](./16-korea-vietnam-practical-map.md) giải thích cách đi từ concept sang jurisdiction-specific owner/source mà không duplicate các file này.

## Lộ trình học

### Core route

Lộ trình mặc định đi từ “tiền là gì trong đời sống cá nhân” đến “toàn bộ hệ thống có chịu được shock hay không”:

```text
01 Money
→ 02 Banking
→ 03 Interest
→ 04 Inflation
→ 05 Credit
→ 06 Loans & Debt
→ 07 Insurance
→ 08 Taxes
→ 09 Housing
→ 10 Car Finance
→ 11 Retirement
→ 12 Emergency Fund
→ 13 Financial Scams
→ 14 Personal Balance Sheet
→ 15 Financial Resilience
```

Các chapter có thể đọc riêng, nhưng dependency quan trọng vẫn nên giữ: hiểu lãi suất trước credit/debt; hiểu cash flow, liquidity và debt trước housing/car; hiểu balance sheet trước khi stress-test resilience; chỉ sau resilience gate mới xác định phần vốn nào thực sự là investable surplus.

### Practical extensions

Sau core, chuyển sang application và operating loop:

```text
15 Financial Resilience
→ 16 Korea–Vietnam Practical Map
→ 17 Cross-Border Personal Finance
→ 18 Case Studies
→ 19 Annual Financial Review
```

Chapter 16 không phải legal handbook; nó định tuyến sang owner/source. Chapter 17 không phải Forex course; nó xử lý household currency mismatch, remittance friction, transferability và cross-border liquidity. Chapter 18 dùng case để kết hợp nhiều concept trong một decision. Chapter 19 biến toàn bộ library thành review loop thay vì một syllabus đọc xong rồi bỏ.

## Mục lục

1. [Money](./01-money.md) — tiền trong tài chính cá nhân, dòng tiền, ngân sách, tiết kiệm, sức mua và chi phí cơ hội.
2. [Banking](./02-banking.md) — tài khoản, hệ thống thanh toán, phí, thanh khoản, rủi ro ngân hàng và bảo vệ tiền gửi.
3. [Interest](./03-interest.md) — lãi đơn, lãi kép, APR/APY, giá trị theo thời gian của tiền và lãi suất thực.
4. [Inflation](./04-inflation.md) — sức mua, CPI, lạm phát cá nhân, thu nhập danh nghĩa/thực và liên hệ với lãi suất.
5. [Credit](./05-credit.md) — tín dụng, hồ sơ/điểm tín dụng, hạn mức, utilization, revolving vs installment và giá của tín dụng.
6. [Loans & Debt](./06-loans-debt.md) — cấu trúc khoản vay, amortization, nợ có/không tài sản bảo đảm, DTI và chiến lược giảm nợ.
7. [Insurance](./07-insurance.md) — pooling, premium, deductible, coverage, liability và cách chuyển giao rủi ro tổn thất lớn.
8. [Taxes](./08-taxes.md) — thu nhập trước/sau thuế, thuế suất biên/hiệu dụng, withholding, tax-deferred/tax-advantaged và ranh giới theo quốc gia.
9. [Housing](./09-housing.md) — thuê/mua, mortgage, down payment, chi phí giao dịch, bảo trì, leverage và total cost of housing.
10. [Car Finance](./10-car-finance.md) — depreciation, financing, insurance, maintenance và tổng chi phí sở hữu phương tiện.
11. [Retirement](./11-retirement.md) — hệ thống hưu trí, defined benefit/defined contribution, compounding, longevity và sequence risk.
12. [Emergency Fund](./12-emergency-fund.md) — vai trò của buffer thanh khoản, cách ước lượng quy mô và phân tầng tiền mặt.
13. [Financial Scams](./13-financial-scams.md) — phishing, impersonation, advance-fee, investment scam, account takeover và quy trình ứng phó.
14. [Personal Balance Sheet](./14-personal-balance-sheet.md) — assets, liabilities, net worth, liquid net worth, cash flow và các tỷ lệ để quan sát hệ thống tài chính cá nhân.
15. [Financial Resilience](./15-financial-resilience.md) — income/expense/rate/FX/operational shocks, cash-flow margin, liquidity runway, stress test và resilience gate trước Investing.
16. [Korea–Vietnam Practical Map](./16-korea-vietnam-practical-map.md) — concept-to-jurisdiction routing cho banking, credit, housing, tax, pension, insurance và scam; giữ luật/procedure ở canonical owner.
17. [Cross-Border Personal Finance](./17-cross-border-personal-finance.md) — functional currency, household FX exposure, remittance total cost, transferability, tax-residency boundary, pension portability và multi-country emergency planning.
18. [Case Studies](./18-case-studies.md) — integrated application qua job loss, housing, KRW↔VND obligations, debt-vs-investing, car, scam, home leverage, family finance, cross-border retirement và death/incapacity continuity.
19. [Annual Financial Review](./19-annual-financial-review.md) — yearly operating loop để reconcile cash flow, liquidity, debt, insurance, balance sheet, resilience, security, cross-border assumptions và investable surplus.

## Mô hình tư duy xuyên suốt

Một quyết định tài chính cá nhân tốt không chỉ tối đa hóa lợi nhuận kỳ vọng (expected return / 기대수익률). Nó phải cân bằng ít nhất sáu biến: **dòng tiền (cash flow / 현금흐름), thanh khoản (liquidity / 유동성), khả năng trả nợ (solvency / 지급능력), rủi ro (risk / 위험), thời hạn (time horizon / 투자기간) và khả năng chống chịu tài chính (financial resilience / 금융 회복탄력성)**.

Hai lựa chọn có cùng expected return có thể rất khác nếu một lựa chọn khóa tiền 10 năm, tạo nghĩa vụ trả nợ cố định, phụ thuộc một currency khác hoặc khiến household không còn emergency liquidity.

Vì vậy câu hỏi thực hành xuyên suốt library là:

```text
Quyết định này thay đổi monthly cash flow thế nào?
→ thay đổi assets/liabilities trên balance sheet ra sao?
→ làm liquidity tốt hơn hay xấu đi?
→ tạo fixed obligation hoặc tail risk nào?
→ nếu income/rate/price/FX thay đổi, hệ thống có còn hoạt động không?
→ phần vốn còn lại có thật sự chịu được investment horizon không?
```

Khi chuỗi này đã được trả lời, quyết định mới sẵn sàng được nối sang Economics để hiểu external environment hoặc sang Investing để đánh giá allocation/risk-return.

## Từ syllabus sang operating system

Library được thiết kế thành hai vòng:

```text
Learning loop
01 → 15
concept → mechanism → household system

Operating loop
16 → 19
jurisdiction → cross-border → case application → annual review
```

Annual review không phải điểm cuối cố định. Khi có job change, marriage/divorce, birth/death, move country, housing transaction, major debt hoặc fraud incident, household quay lại chapter/case tương ứng rồi chạy lại review.

## Bản đồ ownership ngắn

```text
Money / Banking / Debt / Insurance / Housing / Retirement
→ Personal Finance

Inflation formation / monetary policy / labor / growth
→ Economics

Stocks / bonds / funds / valuation / portfolio / Forex
→ Investing

Korean housing / tax / social insurance / credit procedures
→ Korea Law, Civic & Everyday Life
```

Một chủ đề có thể được nhắc ở nhiều domain nhưng chỉ nên có **một canonical owner cho phần giải thích sâu**. Domain còn lại cross-link và chỉ giữ application layer cần thiết.

## Chính sách với dữ liệu time-sensitive

Các chapter không hard-code tax rate, deposit-insurance limit, credit threshold, pension refund list, social-insurance eligibility, mortgage regulation hoặc filing deadline như rule vĩnh viễn. Khi cần số hiện hành phải ghi rõ:

```text
jurisdiction
+ source chính thức
+ effective date
+ population/product scope
+ last reviewed
```

Nếu chưa có đủ metadata, ưu tiên giải thích mechanism và chỉ đường tới official source. Xem [Coverage Audit](./COVERAGE_AUDIT.md) để biết các nhóm dữ liệu cần xử lý theo policy này.

## Nguồn nền

- OECD, *PISA 2022 Financial Literacy Framework*: https://www.oecd.org/en/publications/pisa-2022-assessment-and-analytical-framework_dfe0bf9c-en/full-report/component-4.html
- OECD, Financial Education: https://www.oecd.org/en/topics/financial-education.html
- OECD, *OECD/INFE Toolkit for Measuring Financial Literacy and Financial Inclusion 2026*.
- OECD, *Consumer Finance Risk Monitor 2026*.
- Khan Academy, *Financial Literacy*: https://www.khanacademy.org/college-careers-more/financial-literacy
- Consumer Financial Protection Bureau, consumer tools: https://www.consumerfinance.gov/consumer-tools/

Các nguồn theo quốc gia được dùng để minh họa cơ chế hoặc định tuyến kiểm tra, không mặc định áp dụng pháp lý toàn cầu. Chapter nào đụng tới thuế, bảo hiểm tiền gửi, credit reporting, housing law, social insurance hay hưu trí phải nói rõ jurisdiction boundary thay vì biến quy định của một nước thành “quy tắc chung”.