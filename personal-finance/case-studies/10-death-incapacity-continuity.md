# Case 10 — Khi một người chết hoặc mất khả năng xử lý tài chính: household có tiếp tục vận hành được không?

## Tình huống

Một household có hai người lớn. Một người là người quản lý gần như toàn bộ:

```text
main bank account
rent/mortgage payment
insurance contracts
utility autopay
investment accounts
important passwords/documents
family remittance
```

Người còn lại biết household “ổn về tài chính”, nhưng không biết chi tiết vận hành.

Nếu người quản lý tài chính đột ngột qua đời hoặc mất khả năng ra quyết định, household có thể gặp **operational failure** ngay cả khi net worth đủ lớn.

Case này tập trung vào **financial continuity (재무 연속성)**. Will, inheritance, power of attorney, beneficiary law và probate là jurisdiction-specific; khi áp dụng thực tế phải dùng legal advice/source hiện hành.

## 1. Wealth không đồng nghĩa access

Giả sử household có:

```text
cash/deposits       = 30 triệu KRW
investments         = 120 triệu KRW
housing deposit     = 60 triệu KRW
insurance coverage  = substantial
```

Nhưng người còn lại không biết:

```text
account ở đâu
login/recovery method
payment dates
insurance company
contract numbers
which account receives salary/pension
```

Thì immediate problem không phải net worth. Nó là **access latency**.

```text
assets exist
but
usable liquidity may be temporarily unavailable
```

## 2. Root-account risk

Một email account hoặc phone number thường là recovery root cho nhiều financial services.

Nếu chỉ một người kiểm soát root accounts, sự cố có thể cascade:

```text
phone inaccessible
→ OTP inaccessible
→ bank login blocked
→ brokerage blocked
→ bill/payment management blocked
```

Do đó continuity planning phải nhìn cả financial accounts lẫn identity/recovery infrastructure.

## 3. Household cần operational map

Không nên lưu plaintext password list một cách thiếu an toàn. Nhưng household cần biết **cái gì tồn tại và cách hợp pháp để tiếp cận khi có sự cố**.

Một inventory có thể gồm:

```text
institution
account/product type
owner
beneficiary/dependent relationship
payment role
support contact
where legal documents are stored
recovery/access procedure
```

Mục tiêu là giảm single-person dependency.

## 4. Fixed obligations không dừng khi một người không còn xử lý được

Các nghĩa vụ có thể tiếp tục:

```text
housing payment
loan payment
insurance premium
utilities
childcare/education
family support
subscription/service needed for household
```

Nếu household không biết các payment rail này, missed payment có thể tạo fee, coverage lapse hoặc service disruption.

Vì vậy continuity reserve không chỉ là emergency fund về số tiền. Nó còn là **knowledge redundancy**.

## 5. Insurance phải nối tới beneficiary/access process

Một policy có thể có coverage tốt nhưng household vẫn phải biết:

```text
policy exists
who is insured
who is beneficiary
how to file claim
what documents are needed
```

Nếu beneficiary designation hoặc contact detail lỗi thời, recovery có thể phức tạp hơn.

Chapter [07 — Insurance](../07-insurance.md) giải thích risk transfer; case này thêm operational layer sau insured event.

## 6. Cross-border household phức tạp hơn

Nếu family member, asset hoặc account nằm ở nhiều quốc gia:

```text
language
jurisdiction
time zone
identity verification
currency
transfer restriction
local documentation
```

có thể kéo dài thời gian access.

Một household Korea–Vietnam nên biết ít nhất:

```text
which obligations are in Korea
which are in Vietnam
which account funds each obligation
which person/contact can navigate each country
```

Xem [17 — Cross-Border Personal Finance](../17-cross-border-personal-finance.md).

## 7. Incapacity khác death

Death thường kích hoạt một số legal/insurance processes rõ hơn. Incapacity có thể khó hơn vì owner vẫn còn sống nhưng không thể:

```text
sign
authenticate
communicate
make financial decisions
```

Do đó household nên hiểu rằng beneficiary planning và incapacity planning không hoàn toàn giống nhau.

Chi tiết legal instrument phụ thuộc jurisdiction; Personal Finance chỉ giữ requirement:

> Household phải có một lawful path để critical financial operations tiếp tục khi primary operator không thể thực hiện.

## 8. Continuity stress test

Có thể chạy tabletop exercise:

> Giả sử từ ngày mai người đang quản lý tài chính không thể trả lời bất kỳ câu hỏi nào trong 30 ngày.

Người còn lại có thể xác định trong một giờ:

```text
cash available now
next 30-day obligations
bank accounts
loans
insurance
housing documents
important contacts
family remittance commitments
```

không?

Nếu không, household có operational concentration risk.

## 9. Minimal continuity packet

Một packet an toàn không cần chứa secret credentials trực tiếp. Nó nên cho biết:

```text
household balance-sheet map
monthly obligation map
institution/contact list
insurance inventory
location of legal documents
recovery instructions
country-specific owner/source
review date
```

Security principle:

```text
make existence discoverable
without making secrets casually exposed
```

## 10. Review triggers

Continuity plan nên được review khi:

```text
marriage/divorce
birth/death
move country
buy/sell home
new major account
new debt
insurance change
phone/email recovery change
beneficiary change
```

## 11. Decision boundary

Household không cần mọi người có quyền kiểm soát mọi account. Nhưng phải tránh tình trạng:

```text
one person unavailable
→ entire household cannot identify or service obligations
```

Mức redundancy hợp lý phụ thuộc privacy, relationship, legal structure và security risk.

## 12. Kết luận

Personal finance thường tập trung vào accumulation. Nhưng financial resilience còn bao gồm continuity:

```text
money exists
→ can it be found?
→ can obligations be identified?
→ can authorized people access what they need?
→ can the household operate through the transition?
```

Một balance sheet mạnh nhưng chỉ một người hiểu cách vận hành là một system có hidden single point of failure.