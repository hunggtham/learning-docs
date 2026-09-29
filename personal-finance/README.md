# Thư viện Kiến thức Tài chính Cá nhân (Personal Finance Knowledge Library)

`personal-finance/` là thư viện chuẩn gốc (canonical / 정본) cho các quyết định tài chính ở cấp cá nhân và hộ gia đình: kiếm tiền, giữ tiền, thanh toán, vay nợ, bảo vệ trước rủi ro, thuế, nhà ở, phương tiện, quỹ dự phòng và chuẩn bị cho tuổi nghỉ hưu. Nó được tách khỏi [Investing](../investing/README.md) vì **quản lý tài chính cá nhân (personal finance / 개인 재무) không đồng nghĩa đầu tư (investing / 투자)**.

Theo OECD, hiểu biết tài chính (financial literacy / 금융 이해력) bao gồm kiến thức về khái niệm và rủi ro tài chính, cùng kỹ năng và thái độ để áp dụng kiến thức đó vào những quyết định thực tế. Vì vậy library này không được viết như một danh sách “mua gì để sinh lời”; câu hỏi trung tâm là: **một người biến thu nhập, nghĩa vụ, rủi ro và mục tiêu qua thời gian thành một hệ thống tài chính có khả năng chống chịu như thế nào?**

> Phạm vi của tài liệu là giáo dục. Lãi suất, thuế, bảo hiểm, tín dụng, hưu trí và quyền người tiêu dùng phụ thuộc quốc gia, thời điểm và hợp đồng cụ thể; trước quyết định thực tế phải kiểm tra quy định và điều khoản hiện hành tại nơi áp dụng.

## Ranh giới với Economics và Investing

Ba domain nối nhau nhưng sở hữu các câu hỏi khác nhau:

```text
Personal Finance
  cá nhân/hộ gia đình quản lý tiền, nghĩa vụ và rủi ro
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

Tương tự, library này giải thích quỹ dự phòng (emergency fund / 비상자금), cấu trúc nợ (debt structure / 부채 구조), bảo hiểm (insurance / 보험), bảng cân đối cá nhân (personal balance sheet / 개인 대차대조표) và chi phí sở hữu nhà/xe. Khi tiền đã thực sự có thể được phân bổ cho mục tiêu đầu tư và người học cần risk/return, asset allocation, valuation hay trading, hãy chuyển sang Investing thay vì lặp lại nội dung ở đây.

## Lộ trình học

Lộ trình mặc định đi từ “tiền là gì trong đời sống cá nhân” đến “toàn bộ tài sản và nghĩa vụ được nhìn như một hệ thống”:

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
```

Các chapter có thể đọc riêng, nhưng phụ thuộc quan trọng vẫn nên giữ: hiểu lãi suất (interest / 이자) trước khi phân tích tín dụng (credit / 신용) và khoản vay (loan / 대출); hiểu dòng tiền (cash flow / 현금흐름), thanh khoản (liquidity / 유동성) và nợ trước khi bàn về nhà ở hay xe; hiểu bảng cân đối cá nhân trước khi đánh giá một quyết định “có làm mình giàu hơn không”.

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
14. [Personal Balance Sheet](./14-personal-balance-sheet.md) — assets, liabilities, net worth, liquid net worth, cash flow và các tỷ lệ để nhìn hệ thống tài chính cá nhân.

## Mô hình tư duy xuyên suốt

Một quyết định tài chính cá nhân tốt không chỉ tối đa hóa lợi nhuận kỳ vọng (expected return / 기대수익률). Nó phải cân bằng ít nhất năm biến: **dòng tiền (cash flow / 현금흐름), thanh khoản (liquidity / 유동성), khả năng trả nợ (solvency / 지급능력), rủi ro (risk / 위험) và thời hạn (time horizon / 투자기간)**. Hai lựa chọn có cùng “lợi nhuận” có thể rất khác nếu một lựa chọn khóa tiền 10 năm, tạo nghĩa vụ trả nợ cố định hoặc khiến hộ gia đình không còn tiền dự phòng.

Vì vậy câu hỏi thực hành xuyên suốt library là:

```text
Quyết định này thay đổi dòng tiền tháng như thế nào?
→ thay đổi tài sản/nợ trên bảng cân đối ra sao?
→ làm thanh khoản tốt hơn hay xấu đi?
→ tạo rủi ro đuôi hoặc nghĩa vụ cố định nào?
→ kết quả có còn hợp lý khi thu nhập, lãi suất hoặc giá cả thay đổi?
```

Khi năm câu hỏi này đã được trả lời, quyết định mới sẵn sàng được nối sang Economics để hiểu môi trường bên ngoài hoặc sang Investing để đánh giá phân bổ vốn.

## Nguồn nền

- OECD, *PISA 2022 Financial Literacy Framework*: https://www.oecd.org/en/publications/pisa-2022-assessment-and-analytical-framework_dfe0bf9c-en/full-report/component-4.html
- Khan Academy, *Financial Literacy*: https://www.khanacademy.org/college-careers-more/financial-literacy
- Consumer Financial Protection Bureau, consumer tools: https://www.consumerfinance.gov/consumer-tools/

Các nguồn theo quốc gia được dùng để minh họa cơ chế chứ không mặc định áp dụng pháp lý toàn cầu. Chapter nào đụng tới thuế, bảo hiểm tiền gửi, credit reporting hay hưu trí phải nói rõ jurisdiction boundary thay vì biến quy định của một nước thành “quy tắc chung”.
