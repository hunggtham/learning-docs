# FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment

> **Mạch đọc:** [README](../README.md) là owner của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**; dùng README của thư mục connections để giữ đúng vai trò cầu nối. Từ **1. Trade P/L và settlement exposure là hai lớp khác nhau** đi qua risk taxonomy, confirmation/matching, funding, PvP, netting, payment finality và fail management; mỗi phần nối trade đã khớp với rủi ro thanh khoản và principal phía sau.

Chapter cầu nối (bridge / 브리지) này đi sâu vào phần thường bị bỏ qua sau khi trade đã khớp: hai currency legs có thực sự được thanh toán đúng hạn, đúng amount và với finality hay không. Một trade có đúng direction, đúng price và đúng hedge mục tiêu (objective / 목표) vẫn có thể gây principal mất mát (loss / 손실), liquidity shortfall hoặc operational thất bại (failure / 실패) ở settlement.

```text
Trade execution
→ Confirmation and matching
→ Settlement instruction
→ Funding and liquidity preparation
→ Payment release
→ Final receipt of both currency legs
→ Reconciliation and fail management
```

`as_of_date: 2026-09-28`

Đây là institutional market-plumbing material. chính xác (exact / 정확한) eligibility, cut-off, currency coverage, account cấu trúc (structure / 구조), legal finality và collateral terms phải được kiểm tra với hạ tầng (infrastructure / 인프라), custodian, bank, đặc tả hợp đồng (contract / 계약) và jurisdiction hiện hành.

## 1. Trade P/L và settlement exposure là hai lớp khác nhau

Market-risk view hỏi:

```text
Price moved by how much?
Position gained or lost how much?
```

Settlement-risk view hỏi:

```text
Which currency must be paid?
When does payment become final?
When is the other currency received?
Can one leg be paid without receiving the other?
How much liquidity is needed before netting and settlement?
```

Một position có giá trị thị trường (market value / 시장 가치) gần zero vẫn có gross principal amounts rất lớn cần settle.

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **2. rủi ro (risk / 위험) taxonomy** tiếp nhận điểm tựa từ **1. Trade P/L và settlement exposure là hai lớp khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Principal settlement rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. rủi ro (risk / 위험) taxonomy

Tách ít nhất năm risks:

```text
Principal risk
→ one currency is delivered but the other is not received

Replacement-cost risk
→ failed trade must be replaced at a worse market price

Liquidity risk
→ expected receipt is delayed, but outgoing obligations remain due

Operational risk
→ wrong instruction, cut-off miss, duplicate, system or reconciliation failure

Legal risk
→ netting, collateral or settlement-finality protection is not enforceable as assumed
```

PvP chủ yếu giải quyết principal rủi ro (risk / 위험). Nó không tự động xóa replacement-cost, liquidity, operational hoặc legal rủi ro (risk / 위험).

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **3. Principal settlement rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **2. rủi ro (risk / 위험) taxonomy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Settlement exposure cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Principal settlement rủi ro (risk / 위험)

Principal rủi ro (risk / 위험) xuất hiện khi một institution irrevocably pays currency A nhưng chưa nhận currency B. Exposure có thể bằng full principal, không chỉ mark-to-market.

```text
Pay USD 100m
→ counterparty fails before delivering KRW
→ potential loss is not limited to spread or daily P/L
```

Đây là lý do settlement phương thức (method / 메서드) phải nằm trong counterparty limit và pre-trade quyết định (decision / 결정), không chỉ là back-office detail.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **4. Settlement exposure cửa sổ (window / 윈도우)** tiếp nhận điểm tựa từ **3. Principal settlement rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Payment versus payment — PvP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Settlement exposure cửa sổ (window / 윈도우)

Exposure bắt đầu khi outgoing payment không còn có thể cancel unilaterally và kết thúc khi incoming payment được nhận với finality hoặc khôi phục (recovery / 복구) becomes certain.

```text
Unilateral-cancellation deadline
→ outgoing payment final
→ incoming payment expected
→ incoming payment final
```

Time-zone difference có thể kéo dài cửa sổ (window / 윈도우). Một trade T+2 không có nghĩa rủi ro (risk / 위험) chỉ tồn tại đúng hai ngày; cần biết chính xác (exact / 정확한) payment cut-offs và finality points.

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **5. Payment versus payment — PvP** tiếp nhận điểm tựa từ **4. Settlement exposure cửa sổ (window / 윈도우)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. PvP khác central clearing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Payment versus payment — PvP

PvP conditions final settlement of one currency on final settlement of the other.

```text
Currency A final payment
if and only if
Currency B final payment
```

Điều này loại principal settlement rủi ro (risk / 위험) cho giao dịch (transaction / 트랜잭션) được settlement cơ chế (mechanism / 메커니즘) bảo vệ. Nhưng participant vẫn có thể chịu:

```text
funding need before pay-in
liquidity shortfall if expected receipt is delayed
replacement-cost risk after failed settlement
operational risk from late or incorrect instruction
counterparty exposure outside eligible trades
```

Không được viết `PvP = no risk`.

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **6. PvP khác central clearing** tiếp nhận điểm tựa từ **5. Payment versus payment — PvP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. CLS as an important example, not a universal answer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. PvP khác central clearing

PvP là settlement điều kiện (condition / 조건). Central counterparty — CCP — interposes itself between participants and changes counterparty cấu trúc (structure / 구조) through novation or equivalent legal cơ chế (mechanism / 메커니즘).

```text
PvP
→ links final payments

CCP
→ becomes buyer to seller and seller to buyer under its rulebook
```

Một hệ thống (system / 시스템) có thể cung cấp PvP mà không là CCP. Vì vậy không suy từ PvP rằng credit exposure đã được mutualized hoặc guaranteed.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **6. PvP khác central clearing** cho ta quy tắc; **7. CLS as an important example, not a universal answer** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **8. Gross bilateral settlement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. CLS as an important example, not a universal answer

CLSSettlement là major PvP hạ tầng (infrastructure / 인프라) cho eligible currencies, participants và trade types. Nó giảm principal settlement rủi ro (risk / 위험) bằng simultaneous linked settlement and payment controls.

Nhưng coverage phụ thuộc:

```text
currency eligibility
product / trade-type eligibility
participant or third-party access
instruction timing
operational readiness
funding schedule
```

Một organization giao dịch currency không được hỗ trợ, trade same-day, hoặc miss cut-off có thể vẫn settle ngoài PvP.

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **7. CLS as an important example, not a universal answer** cho ta quy tắc; **8. Gross bilateral settlement** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **9. Pre-settlement netting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Gross bilateral settlement

Trong gross bilateral settlement, mỗi trade leg có thể được thanh toán riêng qua correspondent accounts.

```text
Trade 1 pay USD / receive KRW
Trade 2 receive USD / pay KRW
```

Nếu settle gross, institution phải fund cả outgoing legs dù economic position gần net zero. Điều này tạo:

```text
higher intraday liquidity need
larger principal exposure
more payment messages
more operational touchpoints
```

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **9. Pre-settlement netting** tiếp nhận điểm tựa từ **8. Gross bilateral settlement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Payment netting vs close-out netting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Pre-settlement netting

Pre-settlement netting offsets eligible obligations before payment:

```text
Gross USD pay 100
Gross USD receive 80
→ Net USD pay 20
```

Benefits:

```text
lower gross payment amount
lower liquidity need
smaller remaining settlement exposure
fewer instructions
```

But netting does not automatically eliminate rủi ro (risk / 위험):

```text
residual net amount still must settle
legal enforceability must hold
matching rules must agree
cut-off and value date must align
disputes can prevent compression
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **10. Payment netting vs close-out netting** tiếp nhận điểm tựa từ **9. Pre-settlement netting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. On-us settlement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Payment netting vs close-out netting

Do not mix:

```text
Payment netting
→ offsets due payments under normal settlement

Close-out netting
→ terminates and values obligations after default/termination event
```

Both depend on đặc tả hợp đồng (contract / 계약) and legal enforceability, but solve different states. A bilateral agreement supporting payment netting does not let a researcher assume every default exposure is legally netted exactly as modeled.

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **11. On-us settlement** tiếp nhận điểm tựa từ **10. Payment netting vs close-out netting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Deliverable vs non-deliverable instruments** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. On-us settlement

If both parties hold accounts at the same institution, payments may settle across that institution's books.

This can reduce bên ngoài (external / 외부) payment flows, but protection depends on:

```text
simultaneity / conditional release
credit-line arrangement
legal finality
institution solvency
account and entity structure
```

`Same bank` is not equivalent to `risk-free`.

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **12. Deliverable vs non-deliverable instruments** tiếp nhận điểm tựa từ **11. On-us settlement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. FX swaps have two giá trị (value / 값) dates** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Deliverable vs non-deliverable instruments

Deliverable spot/forward/swap exchanges principal currencies. NDF generally settles a net cash difference in a settlement currency against an agreed fixing.

NDF avoids vật lý (physical / 물리적) delivery of the restricted/non-deliverable currency, but retains:

```text
fixing risk
basis between NDF and onshore exposure
settlement-currency liquidity risk
counterparty / replacement-cost risk
legal and documentation risk
```

Therefore `non-deliverable` does not mean `no settlement risk`; it changes what must settle.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **13. FX swaps have two giá trị (value / 값) dates** tiếp nhận điểm tựa từ **12. Deliverable vs non-deliverable instruments** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Same-day and shortened settlement cycles** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. FX swaps have two giá trị (value / 값) dates

FX swap contains near and far legs:

```text
Near date: exchange currencies
Far date: reverse exchange currencies
```

Operational rủi ro (risk / 위험) can occur on either date. The far leg may be forgotten, mismatched or unfunded after the near leg settles correctly.

Nhánh học (track / 트랙):

```text
near-leg principal
far-leg principal
value dates
roll / extension
counterparty netting set
collateral agreement
```

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **14. Same-day and shortened settlement cycles** tiếp nhận điểm tựa từ **13. FX swaps have two giá trị (value / 값) dates** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Standing settlement instructions — SSI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Same-day and shortened settlement cycles

Shorter settlement reduces market-exposure thời gian (time / 시간) but compresses operations:

```text
less time for affirmation
less time to correct SSI errors
earlier funding decisions
tighter cut-offs
greater automation need
```

Same-day FX may not be eligible for the same PvP tiến trình (process / 프로세스) as ordinary T+1/T+2 trades. Operational feasibility must be checked before promising settlement.

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **15. Standing settlement instructions — SSI** tiếp nhận điểm tựa từ **14. Same-day and shortened settlement cycles** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Confirmation and matching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Standing settlement instructions — SSI

SSI identifies where and how payments should be sent. dùng chung (common / 공통) controls:

```text
authorised source
dual approval for changes
effective date
counterparty and currency scope
independent callback / verification
change log
fraud screening
```

An incorrect or fraudulently changed SSI can redirect full principal even when trade economics are correct.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **16. Confirmation and matching** tiếp nhận điểm tựa từ **15. Standing settlement instructions — SSI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Calendar and cut-off rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Confirmation and matching

Trade fields must match:

```text
counterparty legal entity
currency pair and direction
notional
rate
trade date
value date
settlement accounts
product type
```

Mismatch found after cut-off can force gross bilateral settlement, delay receipt or create a thất bại (fail / 실패).

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **17. Calendar and cut-off rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **16. Confirmation and matching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Funding and intraday liquidity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Calendar and cut-off rủi ro (risk / 위험)

FX giá trị (value / 값) date depends on two currency calendars, weekends and thị trường (market / 시장) conventions.

```text
Currency A holiday
Currency B open
→ expected value date may shift
```

Các hệ thống (systems / 시스템들) must maintain:

```text
currency calendar
local payment-system cut-off
PvP instruction cut-off
correspondent-bank cut-off
daylight-saving treatment
```

Hard-coding `T+2 = two calendar days` is an operational defect.

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **18. Funding and intraday liquidity** tiếp nhận điểm tựa từ **17. Calendar and cut-off rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Liquidity rủi ro (risk / 위험) survives PvP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Funding and intraday liquidity

Settlement requires available currency at the right location and thời gian (time / 시간).

Liquidity plan:

```text
opening cash
confirmed incoming receipts
outgoing pay-ins
netting benefit
credit lines
contingent buffer
timing uncertainty
```

An institution can be solvent but thất bại (fail / 실패) settlement because liquidity is in the wrong currency, account, legal thực thể (entity / 엔터티) or thời gian (time / 시간) zone.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **19. Liquidity rủi ro (risk / 위험) survives PvP** tiếp nhận điểm tựa từ **18. Funding and intraday liquidity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Collateral is not a substitute for PvP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Liquidity rủi ro (risk / 위험) survives PvP

PvP can withhold outgoing payment if incoming payment is not available, preventing principal mất mát (loss / 손실). But the institution may still not receive currency when expected and may need emergency funding or replacement trade.

```text
No principal loss
≠ no cash-flow disruption
```

This distinction matters for import payments, collateral calls, securities settlement and debt dịch vụ (service / 서비스).

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **20. Collateral is not a substitute for PvP** tiếp nhận điểm tựa từ **19. Liquidity rủi ro (risk / 위험) survives PvP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Settlement thất bại (fail / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Collateral is not a substitute for PvP

Collateral can mitigate hiện tại (current / 현재)/replacement-cost credit exposure. It usually does not ensure simultaneous exchange of full principal currencies.

```text
Collateral amount
may be far smaller than
gross principal settlement amount
```

Collateral also creates:

```text
margin timing
eligible-asset constraint
haircut
custody and segregation
wrong-way risk
```

Use collateral and PvP as different controls.

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **21. Settlement thất bại (fail / 실패)** tiếp nhận điểm tựa từ **20. Collateral is not a substitute for PvP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Failed receipt can create downstream thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Settlement thất bại (fail / 실패)

A thất bại (fail / 실패) means a due giao dịch (transaction / 트랜잭션) remains unsettled under the applicable definition and thời gian (time / 시간) ranh giới (boundary / 경계).

Classify nguyên nhân gốc (root cause / 근본 원인):

```text
insufficient funds
incorrect SSI
unmatched trade
missed cut-off
counterparty default
sanctions/compliance hold
system outage
calendar error
```

Do not close a thất bại (fail / 실패) ticket merely because payment arrived later. bản ghi (record / 레코드) duration, liquidity chi phí (cost / 비용), replacement chi phí (cost / 비용), operational cause and recurrence rủi ro (risk / 위험).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **22. Failed receipt can create downstream thất bại (failure / 실패)** tiếp nhận điểm tựa từ **21. Settlement thất bại (fail / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Counterparty limits must include settlement phương thức (method / 메서드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Failed receipt can create downstream thất bại (failure / 실패)

```text
Expected USD receipt fails
→ institution cannot fund securities purchase
→ securities settlement fails
→ penalty / buy-in / client impact
```

Thus FX settlement rủi ro (risk / 위험) can propagate into securities, derivatives collateral, trade finance and corporate payments.

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **22. Failed receipt can create downstream thất bại (failure / 실패)** đã nêu tiêu chí phân biệt, còn **23. Counterparty limits must include settlement phương thức (method / 메서드)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **24. Settlement-method hierarchy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Counterparty limits must include settlement phương thức (method / 메서드)

Counterparty exposure is not only mark-to-market:

```text
pre-settlement replacement-cost exposure
principal settlement exposure
post-settlement receivable
collateral exposure
liquidity dependency
```

A lower limit or additional điều khiển (control / 제어) may be appropriate when counterparty cannot use PvP or robust netting. chính xác (exact / 정확한) chính sách (policy / 정책) depends on institution and regulation.

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **23. Counterparty limits must include settlement phương thức (method / 메서드)** đã nêu tiêu chí phân biệt, còn **24. Settlement-method hierarchy** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **25. KRW and VND ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Settlement-method hierarchy

A học tập (learning / 학습) hierarchy:

```text
1. PvP where available and practicable
2. Pre-settlement netting plus protected settlement method
3. Timing controls / on-us with loss protection where appropriate
4. Gross bilateral settlement with explicit exposure limit and contingency
```

This is not a universal legal ranking. Each step requires eligibility, enforceability and operational phân tích (analysis / 분석).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **25. KRW and VND ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **24. Settlement-method hierarchy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Settlement mô hình dữ liệu (data model / 데이터 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. KRW and VND ngữ cảnh (context / 맥락)

For currencies with onshore/offshore segmentation, capital controls or limited PvP truy cập (access / 접근), settlement thiết kế (design / 설계) may differ from major CLS-eligible pairs.

Check:

```text
deliverable vs NDF product
onshore account access
authorised intermediary
fixing source
settlement currency
local cut-off
convertibility and remittance rule
```

Do not bản sao (copy / 복사) EUR/USD settlement các giả định (assumptions / 가정들) into USD/KRW or USD/VND workflows.

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **25. KRW and VND ngữ cảnh (context / 맥락)** nêu điều cần giải thích; **26. Settlement mô hình dữ liệu (data model / 데이터 모델)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **27. Exposure calculation layers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Settlement mô hình dữ liệu (data model / 데이터 모델)

Minimum bản ghi (record / 레코드):

```text
trade_id
counterparty_legal_entity
product
currency_pair
buy_currency / amount
sell_currency / amount
trade_date
value_date
settlement_method
netting_set
instruction_status
payment_release_time
payment_finality_time
receipt_time
fail_reason
resolution_time
```

Keep sự kiện (event / 이벤트) lịch sử (history / 이력) append-only. Overwriting `status=settled` destroys bằng chứng (evidence / 증거) of prior delay or manual intervention.

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **26. Settlement mô hình dữ liệu (data model / 데이터 모델)** nêu điều cần giải thích; **27. Exposure calculation layers** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **28. Intraday liquidity ladder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Exposure calculation layers

Nhánh học (track / 트랙) at least:

```text
gross principal due
amount subject to netting
post-netting amount
amount protected by PvP
amount settled with timing controls
gross bilateral residual
failed / delayed amount
```

Do not report only final net cash and claim full rủi ro (risk / 위험) mitigation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **28. Intraday liquidity ladder** tiếp nhận điểm tựa từ **27. Exposure calculation layers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Stress scenarios** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Intraday liquidity ladder

Bucket payments by thời gian (time / 시간):

```text
opening
cut-off 1
cut-off 2
PvP pay-in window
local RTGS window
end-of-day
```

For each bucket:

```text
confirmed inflow
probabilistic inflow
mandatory outflow
available credit
buffer
shortfall
```

Stress expected receipts separately from committed outgoing payments.

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **29. Stress scenarios** tiếp nhận điểm tựa từ **28. Intraday liquidity ladder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Stress scenarios

### Counterparty default after outgoing payment

```text
Gross bilateral trade
→ outgoing currency final
→ incoming currency not received
→ principal loss + replacement need
```

### PvP participant misses pay-in

```text
principal protected
→ expected receipt delayed/not settled
→ liquidity and replacement-cost stress
```

### Cut-off miss

```text
eligible trade misses instruction deadline
→ alternative settlement method required
→ exposure and liquidity profile changes
```

### Local-currency payment outage

```text
onshore leg unavailable
→ offshore hedge settles differently or later
→ basis and liquidity mismatch
```

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **30. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)** tiếp nhận điểm tựa từ **29. Stress scenarios** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. điều khiển (control / 제어) khung phần mềm (framework / 프레임워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)

Start from thất bại (failure / 실패):

```text
institution misses USD payment
principal exposure exceeds counterparty limit
client securities trade fails
intraday liquidity buffer goes negative
```

Solve backwards for:

```text
netting failure
receipt delay
cut-off miss
currency-specific funding shock
system outage duration
counterparty default timing
```

At least one reverse stress must occur without a large spot move.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **31. điều khiển (control / 제어) khung phần mềm (framework / 프레임워크)** tiếp nhận điểm tựa từ **30. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Dashboard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. điều khiển (control / 제어) khung phần mềm (framework / 프레임워크)

```text
Pre-trade
→ settlement eligibility, counterparty limit, SSI availability

Post-trade
→ confirmation, matching, value-date validation

Pre-settlement
→ netting, funding, instruction and cut-off checks

Settlement
→ payment release, finality and receipt monitoring

Post-settlement
→ reconciliation, fail resolution, root-cause review
```

Controls need đơn vị sở hữu (owner / 오너), timestamp, bằng chứng (evidence / 증거) and escalation đường dẫn (path / 경로).

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **32. Dashboard** tiếp nhận điểm tựa từ **31. điều khiển (control / 제어) khung phần mềm (framework / 프레임워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. What not to learn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Dashboard

```text
gross obligations by currency
PvP-protected share
netting compression ratio
gross bilateral residual
largest counterparty principal exposure
intraday peak liquidity need
late/unmatched instruction count
settlement fail amount and duration
manual intervention rate
recurring root cause
```

Dashboard should preserve denominator and amount. A low thất bại (fail / 실패) percentage can still hide a material principal amount.

> **Chuyển mạch:** Ở chặng này của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **33. What not to learn** tiếp nhận điểm tựa từ **32. Dashboard** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. rà soát (review / 검토) questions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. What not to learn

```text
PvP eliminates all FX risk
netting eliminates legal/counterparty risk
same-bank settlement is automatically protected
collateral covers full principal
NDF has no settlement risk
T+1 is operationally safer in every dimension
settlement is only a back-office concern
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **34. rà soát (review / 검토) questions** tiếp nhận điểm tựa từ **33. What not to learn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Sources and cập nhật (update / 업데이트) watch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. rà soát (review / 검토) questions

1. When does unilateral cancellation become impossible?
2. When is each currency payment final?
3. Which trades are PvP eligible and which are not?
4. What residual remains after netting?
5. How much intraday currency liquidity is needed?
6. What risks survive PvP?
7. Is netting legally enforceable in relevant jurisdictions?
8. What happens if expected receipt is delayed but outgoing obligations remain due?
9. Which downstream settlements depend on the FX receipt?
10. Which operational chỉ số (metric / 지표) would reveal a deteriorating tiến trình (process / 프로세스) before a mất mát (loss / 손실)?

> **Chuyển mạch:** Trong **FX Settlement, PvP, Netting & Liquidity — từ executed trade đến final payment**, **34. rà soát (review / 검토) questions** nêu điều cần giải thích; **35. Sources and cập nhật (update / 업데이트) watch** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 35. Sources and cập nhật (update / 업데이트) watch

- [BIS — Uncovering FX settlement risk: new measures from the 2025 Triennial Survey](https://www.bis.org/publications/qr-202606/uncovering-fx-settlement-risk-new-measures-2025-bis-triennial-survey)
- [BIS — FX settlement risk: an unsettled issue](https://www.bis.org/publications/qr-202212/fx-settlement-risk-unsettled-issue)
- [CPMI — Facilitating increased adoption of payment versus payment](https://www.bis.org/publications/facilitating-increased-adoption-payment-versus-payment-pvp-final-report)
- [BCBS — Supervisory guidance for managing FX settlement-related risks](https://www.bis.org/committees/bcbs/basel-consolidated-guidelines/module/rma/20)
- [CLSSettlement](https://www.cls-group.com/products/settlement/clssettlement)

The 2025 BIS methodology and thị trường (market / 시장) coverage figures are historical snapshots, not timeless constants. rà soát (review / 검토) PvP coverage, currency/sản phẩm (product / 제품) eligibility, cut-offs and legal frameworks before hiện thực (implementation / 구현).

Đọc cùng:

- [01 — Market structure and instruments](../01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)
- [05 — Execution, brokers, costs and operational risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [00 — FX funding, NDF, basis and forward curve](./00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [04 — Cross-currency funding and debt hedge](../60_institutional_hedging_cases/04_CROSS_CURRENCY_FUNDING_AND_DEBT_HEDGE.md)
- [02 — Backtest engine and execution model](../70_systematic_project/02_BACKTEST_ENGINE_AND_EXECUTION_MODEL.md)

> **Bàn giao:** Sau **35. Sources and cập nhật (update / 업데이트) watch**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
