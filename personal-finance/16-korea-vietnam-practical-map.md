# 16 — Bản đồ tài chính cá nhân Hàn Quốc – Việt Nam (Korea–Vietnam Practical Map / 한–베 개인재무 실전 지도)

## Định vị

Các chapter `01–15` chủ yếu xây mô hình có thể dùng ở nhiều quốc gia: tiền, lãi suất, debt, insurance, housing economics, retirement planning, liquidity và resilience. Nhưng khi một quyết định chạm tới **luật, quyền người tiêu dùng, hệ thống thuế, bảo hiểm xã hội, credit reporting, hợp đồng nhà ở hoặc thủ tục hành chính**, không thể lấy rule của một nước áp thẳng sang nước khác.

Chapter này không cố viết lại hai bộ luật tài chính của Hàn Quốc và Việt Nam. Nó là **bản đồ định tuyến kiến thức (knowledge-routing map / 지식 라우팅 지도)**: concept nào nằm ở Personal Finance, phần Hàn Quốc nên chuyển sang đâu trong repository, phần Việt Nam cần kiểm tra loại nguồn nào, và cách so sánh hai hệ thống mà không biến khác biệt thể chế thành mẹo ghi nhớ rời rạc.

## Quy tắc quan trọng nhất: mechanism trước, jurisdiction sau

Một quyết định vay tiền ở Seoul và một quyết định vay tiền ở Hà Nội đều có cùng các biến nền:

```text
principal
interest rate
fees
maturity
payment schedule
collateral
prepayment conditions
late-payment consequences
```

Nhưng cách công bố chi phí, credit reporting, consumer protection, tax treatment, collateral enforcement và thủ tục tranh chấp có thể khác. Vì vậy workflow đúng là:

```text
hiểu concept chung
→ xác định jurisdiction
→ tìm canonical owner trong repo
→ kiểm tra nguồn chính thức hiện hành
→ đọc hợp đồng cụ thể
→ mới đưa ra quyết định
```

Không nên đảo ngược quy trình bằng cách học thuộc một rate, threshold hoặc deadline rồi xem nó như kiến thức tài chính chung.

## Banking và thanh toán

### Lớp concept dùng chung

[02 — Banking](./02-banking.md) sở hữu các câu hỏi nền: deposit account khác payment account thế nào, liquidity là gì, fee ảnh hưởng ra sao, payment rail tạo settlement risk thế nào và deposit protection khác investment protection ở đâu.

### Hàn Quốc

Nếu cần thủ tục và quyền cụ thể khi sống tại Hàn Quốc, đọc [`korea_law_civic_life/08_banking_credit_and_financial_consumer.md`](../korea_law_civic_life/08_banking_credit_and_financial_consumer.md). File đó đã bao phủ account, KYC/AML, credit, card, loan, consumer protection và dispute routing cho bối cảnh Hàn Quốc.

Một số nguồn chính thức/primary portal nên biết:

- Financial Supervisory Service (`금융감독원`, FSS): https://www.fss.or.kr/
- Financial Consumer Information Portal FINE (`금융소비자정보포털 파인`): https://fine.fss.or.kr/
- Credit4U (`본인신용정보 열람서비스`): https://www.credit4u.or.kr/
- Financial Services Commission (`금융위원회`, FSC): https://www.fsc.go.kr/

Credit4U là ví dụ điển hình cho boundary giữa concept và implementation: Personal Finance giải thích **vì sao cần kiểm tra hồ sơ tín dụng (credit information / 신용정보)**; portal Hàn Quốc mới là nơi kiểm tra dữ liệu thực tế của người dùng trong hệ thống Hàn.

### Việt Nam

Ở Việt Nam, concept banking vẫn giống nhau nhưng institution, reporting system và consumer procedure phải kiểm tra từ cơ quan/tổ chức có thẩm quyền hiện hành. Với câu hỏi liên quan ngân hàng và chính sách tiền tệ, điểm bắt đầu nên là **Ngân hàng Nhà nước Việt Nam (State Bank of Vietnam)** và tài liệu chính thức của tổ chức cung cấp sản phẩm.

Đừng lấy điều kiện mở tài khoản, credit score hoặc hạn mức ở Hàn Quốc để suy ra điều kiện tại Việt Nam. Cùng tên “credit card” hoặc “consumer loan” không có nghĩa contract, fee structure và reporting giống nhau.

## Credit và debt

[05 — Credit](./05-credit.md) và [06 — Loans & Debt](./06-loans-debt.md) sở hữu framework chung:

```text
ability to repay
+ cost of credit
+ debt structure
+ collateral
+ behavior under stress
```

Điểm so sánh hữu ích giữa Hàn và Việt Nam không phải “nước nào dễ vay hơn” theo một câu tổng quát, mà là những câu hỏi kiểm chứng được:

```text
Ai thu thập/report credit information?
Lender dùng những dữ liệu nào?
APR/interest/fees được disclose ra sao?
Có fixed/variable rate không?
Prepayment cost thế nào?
Late payment ảnh hưởng gì?
Dispute đi qua kênh nào?
```

Các câu trả lời có thể thay đổi theo loại sản phẩm và thời điểm. Vì thế chapter không hard-code một credit score threshold hay một mức DTI thành rule chung.

## Housing: khác biệt thể chế rất lớn

[09 — Housing](./09-housing.md) sở hữu economics của quyết định nhà ở: rent-vs-buy, leverage, down payment, transaction cost, maintenance và concentration risk.

### Hàn Quốc

Hàn Quốc có các cấu trúc thuê như `월세`, `전세`, `보증금`, khiến rủi ro household không chỉ là “monthly rent cao hay thấp” mà còn là **khả năng bảo vệ và thu hồi khoản deposit lớn**. Phần pháp lý/procedural này đã có canonical owner tại [`korea_law_civic_life/06_housing_wolse_jeonse_deposit_and_registration.md`](../korea_law_civic_life/06_housing_wolse_jeonse_deposit_and_registration.md), bao gồm `등기부`, `확정일자`, quyền liên quan deposit và workflow kiểm tra trước khi ký.

Personal Finance chỉ giữ lớp decision:

```text
bao nhiêu liquidity bị khóa trong deposit?
→ opportunity cost là gì?
→ deposit concentration có làm emergency runway giảm không?
→ nếu hoàn trả chậm, household có chịu được không?
```

### Việt Nam

Thị trường thuê/mua, mortgage, giấy tờ sở hữu và thủ tục giao dịch tại Việt Nam có cấu trúc khác. Vì vậy không dùng mô hình `전세` làm template cho Việt Nam. Khi áp dụng [09 — Housing](./09-housing.md), giữ framework về total cost, debt, liquidity và concentration; còn quyền sở hữu, đăng ký, thuế/phí và contract enforcement phải kiểm tra theo quy định Việt Nam hiện hành.

Đây là ví dụ rõ nhất của quy tắc:

```text
same economic question
≠ same legal implementation
```

## Taxes: đừng nhầm personal-finance logic với tax law

[08 — Taxes](./08-taxes.md) giải thích gross/net income, marginal/effective rate, withholding và lý do tax treatment làm thay đổi cash flow. Nó không phải tax code của từng nước.

### Hàn Quốc

Repository đã có owner thực dụng tại [`korea_law_civic_life/07_taxes_social_insurance_welfare_healthcare.md`](../korea_law_civic_life/07_taxes_social_insurance_welfare_healthcare.md), bao gồm `국세`, `지방세`, `원천징수`, `연말정산`, social insurance và các portal/cơ quan liên quan.

Với thuế, status cần xác định bằng luật thuế và facts thực tế; không nên dùng nationality hoặc visa như proxy duy nhất.

### Việt Nam

Ở Việt Nam, hãy tách cùng các lớp:

```text
loại thu nhập
→ tax residency / status theo luật áp dụng
→ withholding nếu có
→ filing/settlement obligation
→ deduction/exemption nếu có
→ chứng từ cần giữ
```

Rate, threshold, deduction và procedure là time-sensitive. Khi cần số cụ thể, phải kiểm tra văn bản và portal chính thức đang có hiệu lực thay vì copy một ví dụ cũ trong tài liệu học.

## Social insurance và retirement

[11 — Retirement](./11-retirement.md) sở hữu câu hỏi dài hạn: pension promise khác retirement asset thế nào, defined benefit/defined contribution khác nhau ra sao, longevity risk và sequence risk hoạt động thế nào.

### Hàn Quốc

Trong bối cảnh Hàn Quốc, `국민연금` và các hệ thống liên quan có rules riêng cho người nước ngoài. Điều kiện participation, social-security agreement hoặc refund/lump-sum không giống nhau cho mọi nationality/status và có thể thay đổi. Vì thế khi cần quyết định thật, kiểm tra **National Pension Service (`국민연금공단`)** và chapter Korea-specific trong repo thay vì ghi nhớ một country list tĩnh.

### Việt Nam

Việt Nam có bảo hiểm xã hội bắt buộc/tự nguyện và chế độ hưu trí theo khuôn khổ pháp luật hiện hành. Một số tình huống của người lao động nước ngoài cũng có thể thuộc phạm vi quy định. Nguồn kiểm tra nên là **Bảo hiểm xã hội Việt Nam** và văn bản pháp luật đang có hiệu lực.

So sánh hữu ích không phải “pension Hàn tốt hơn hay Việt tốt hơn”, mà là cấu trúc:

```text
contribution base
eligibility
vesting / qualifying period
benefit formula
portability
withdrawal/refund rule
inflation/indexation
survivor/dependent protection
```

Các biến này giúp đọc bất kỳ pension system nào mà không cần biến chapter thành bảng luật thay đổi hàng năm.

## Insurance

[07 — Insurance](./07-insurance.md) sở hữu mechanism: risk pooling, premium, deductible, exclusion, limit và claims risk. Nhưng sản phẩm health, life, auto, property hoặc mandatory social insurance khác nhau theo quốc gia.

Khi so sánh Hàn–Việt, luôn tách:

```text
public/social insurance
≠ private insurance
≠ employer benefit
≠ self-funded emergency reserve
```

Một khoản bị trừ trên payslip không tự động là “tax”; một benefit của employer cũng không tự động thay thế private coverage cần thiết. Đây là lỗi mental model thường gặp khi chuyển giữa hai hệ thống.

## Scam và consumer protection

Mechanism ở [13 — Financial Scams](./13-financial-scams.md) phần lớn mang tính xuyên biên giới: impersonation, urgency, phishing, remote access, fake investment dashboard, recovery scam. Nhưng reporting/freeze/dispute channel lại phụ thuộc nước, payment rail và provider.

Vì vậy khi sự cố xảy ra:

```text
protect account/payment immediately
→ contact provider through official channel
→ preserve evidence
→ use local official reporting/dispute channel
```

Không trì hoãn việc khóa tài khoản chỉ để tìm “đúng cơ quan hoàn hảo”. Operational containment thường cần xảy ra trước.

## Một bảng so sánh tốt nên so sánh cái gì?

Thay vì so sánh bằng slogan, hãy dùng cùng một bộ câu hỏi cho hai nước:

```text
Banking     → access, fees, deposit protection, dispute
Credit      → data, pricing, repayment, reporting
Tax         → residency, income scope, withholding, filing
Housing     → deposit/down payment, ownership, leverage, legal protection
Retirement  → contribution, eligibility, portability, benefit
Insurance   → public/private layers, exclusions, claims
Scams       → payment rails, freeze/reporting channels
```

Cách này giữ comparison ở cùng một dimension và tránh việc so một legal detail của Hàn với một market outcome của Việt Nam.

## Workflow kiểm tra một rule time-sensitive

Khi gặp một con số như interest cap, tax rate, pension refund condition, deposit-protection limit hoặc filing deadline:

```text
1. Xác định nước và loại sản phẩm.
2. Xác định cơ quan/official owner.
3. Tìm văn bản hoặc hướng dẫn hiện hành.
4. Kiểm tra effective date.
5. Kiểm tra đối tượng áp dụng.
6. Đọc contract/individual facts.
7. Ghi ngày đã kiểm tra nếu đưa rule vào notes.
```

Nếu thiếu một trong các bước trên, coi con số đó là **candidate information**, chưa phải rule có thể dùng cho quyết định.

## Kết luận và hướng đọc tiếp

Personal Finance cung cấp **framework ra quyết định**; hệ thống pháp lý Hàn Quốc hoặc Việt Nam cung cấp **implementation constraints**. Tách hai lớp giúp tài liệu bền hơn theo thời gian và giúp người học biết khi nào một concept có thể chuyển giữa quốc gia, khi nào phải dừng lại để kiểm tra nguồn chính thức.

Khi cuộc sống thực sự đi qua cả hai hệ thống — ví dụ income ở Hàn nhưng gửi tiền, sở hữu tài sản hoặc có nghĩa vụ gia đình tại Việt Nam — vấn đề không còn chỉ là “biết hai bộ rule”. [17 — Cross-Border Personal Finance](./17-cross-border-personal-finance.md) nối chúng thành một balance sheet đa tiền tệ, đa jurisdiction và giải thích currency/liquidity/transfer/tax-residency friction ở cấp household.

### Nguồn/owner để tiếp tục

- Korea Law, Civic & Everyday Life: [`../korea_law_civic_life/README.md`](../korea_law_civic_life/README.md)
- Financial Supervisory Service: https://www.fss.or.kr/
- FINE: https://fine.fss.or.kr/
- Credit4U: https://www.credit4u.or.kr/
- National Pension Service: https://www.nps.or.kr/
- Bảo hiểm xã hội Việt Nam: https://baohiemxahoi.gov.vn/
- Ngân hàng Nhà nước Việt Nam: https://www.sbv.gov.vn/
