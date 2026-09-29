# Economic Hedge vs Hedge Accounting — rủi ro (risk / 위험) management, designation và documentation ranh giới (boundary / 경계)

> **Mạch đọc:** Chapter này nối exposure và economic hedge với accounting eligibility, designation và disclosure. Hãy mang rủi ro (risk / 위험) mục tiêu (objective / 목표) từ các chapter FX/hedging trước, rồi dùng phần `Đọc cùng` để tách rủi ro (risk / 위험) management khỏi chuẩn mực và chính sách (policy / 정책) hiện thực (implementation / 구현).

Chapter cầu nối (bridge / 브리지) này giải thích vì sao một hedge tốt về mặt kinh tế chưa chắc đủ điều kiện để áp dụng hedge accounting, và ngược lại vì sao đạt một accounting designation không tự động chứng minh rằng hedge chính sách (policy / 정책) đang quản trị rủi ro (risk / 위험) tốt.

```text
Business exposure
→ Risk-management objective
→ Economic hedge design
→ Accounting eligibility
→ Formal designation and documentation
→ Ongoing effectiveness / rebalancing
→ Financial-statement presentation and disclosure
```

`as_of_date: 2026-09-27`

Đây là học tập (learning / 학습) material về ranh giới (boundary / 경계) và workflow. Nó không thay thế IFRS/K-IFRS văn bản (text / 텍스트), accounting chính sách (policy / 정책), auditor judgment, tax advice, legal documentation hoặc journal-entry hiện thực (implementation / 구현). Trước khi áp dụng, phải kiểm tra tiêu chuẩn (standard / 표준)/adoption hiện hành, facts-and-circumstances và thực thể (entity / 엔터티) chính sách (policy / 정책).

## 1. Economic hedge và accounting hedge là hai câu hỏi khác nhau

**Economic hedge** hỏi:

```text
Instrument có làm giảm distribution của cash-flow, fair-value,
funding hoặc portfolio risk theo objective của business không?
```

**Hedge accounting** hỏi:

```text
Relationship có được standard cho phép designation không?
Documentation, hedged item, hedging instrument và effectiveness
có đáp ứng qualifying requirements không?
```

Do đó:

```text
economically sensible hedge
≠ automatically qualifying hedge-accounting relationship

qualifying designation
≠ proof that business risk is fully eliminated
```

Một derivative không được designate vẫn có fair-value/accounting consequences theo applicable standards. Không được gọi nó là “không có accounting impact”.

## 2. mục tiêu (objective / 목표) của hedge accounting

IFRS 9 mô tả mục tiêu (objective / 목표) ở mức khái quát là phản ánh trong financial statements ảnh hưởng của risk-management activities khi thực thể (entity / 엔터티) dùng financial instruments để quản trị exposures có thể tác động tới profit or mất mát (loss / 손실), hoặc trong một số trường hợp other comprehensive income.

Điểm cần hiểu:

```text
Risk management defines the economic objective.
Accounting designation defines how a qualifying relationship is represented.
```

Accounting không nên là lý do duy nhất để tạo một hedge không phù hợp với nghiệp vụ (business / 비즈니스) exposure. Ngược lại, treasury không nên bỏ qua accounting volatility, documentation sức chứa (capacity / 용량) hoặc disclosure consequence khi chọn instrument.

## 3. Ba loại hedging relationship ở mức khái niệm

IFRS 9 phân biệt ba nhóm lớn:

```text
Fair value hedge
→ exposure to changes in fair value of a recognised item,
  firm commitment or eligible component attributable to a risk

Cash flow hedge
→ exposure to variability in cash flows associated with an eligible item,
  including certain highly probable forecast transactions

Net investment hedge
→ FX exposure associated with a net investment in a foreign operation
```

Tên category không đủ để chọn treatment. Phải xác định:

```text
hedged item
hedged risk
hedging instrument
designation date
quantity / hedge ratio
time horizon
presentation currency and functional currency context
```

## 4. Qualifying gate trước khi nói tới effectiveness

Một workflow học tập nên kiểm tra theo thứ tự:

```text
1. Is the hedging instrument eligible?
2. Is the hedged item / risk component eligible?
3. Is there a documented risk-management objective?
4. Was the relationship formally designated and documented?
5. Is there an economic relationship?
6. Does credit risk dominate the value changes?
7. Does the designated hedge ratio reflect the actual quantities used?
```

Nếu thất bại (fail / 실패) ở eligibility hoặc documentation, một regression đẹp giữa item và instrument không tự tạo ra qualifying relationship.

## 5. Documentation at inception

IFRS 9 yêu cầu formal designation và documentation khi bắt đầu hedging relationship. Documentation ở mức khái niệm phải xác định:

```text
hedging instrument
hedged item
nature of the hedged risk
risk-management objective and strategy
method used to assess qualifying effectiveness requirements
sources of expected hedge ineffectiveness
method for determining hedge ratio
```

Một trade ticket, email “hedge USD” hoặc broker confirmation riêng lẻ không thay thế full designation bản ghi (record / 레코드).

Operationally, thực thể (entity / 엔터티) cần liên kết:

```text
exposure ID
forecast / contract evidence
approval
trade ID
designation document
valuation source
effectiveness review
accounting close package
```

## 6. Hedged item phải cụ thể

Những mô tả quá rộng dễ che giấu mismatch:

```text
"USD risk"
"future sales"
"foreign investment"
```

Một designation có thể cần cụ thể hơn:

```text
currency
amount or layer
time period
transaction type
risk component
probability / contractual status
business unit or portfolio
```

Economic exposure có thể rộng hơn accounting-eligible hedged item. Ví dụ long-run competitive exposure thường khó map giống một booked payable hoặc highly probable forecast giao dịch (transaction / 트랜잭션).

## 7. Forecast giao dịch (transaction / 트랜잭션) và xác suất (probability / 확률) discipline

Forecast hedge tạo một quản trị (governance / 거버넌스) bài toán (problem / 문제): exposure chưa chắc chắn nhưng derivative đã tồn tại.

Phải tách:

```text
contracted exposure
highly probable forecast exposure
possible pipeline
management aspiration
```

Nếu forecast amount hoặc timing giảm:

```text
hedge notional may exceed qualifying exposure
→ over-hedge / discontinuation question
→ derivative remains economically and operationally real
→ cash, collateral and P/L consequences still exist
```

Forecast-quality lịch sử (history / 이력) vì thế là đầu vào (input / 입력) cho cả treasury chính sách (policy / 정책) và accounting judgment.

## 8. Economic relationship

Economic relationship nghĩa là hedged item và hedging instrument có values thường dịch chuyển theo cách phản ánh cùng underlying rủi ro (risk / 위험) hoặc economically related rủi ro (risk / 위험).

Không nên rút gọn thành:

```text
correlation > threshold
→ automatically effective
```

Cần hiểu cơ chế (mechanism / 메커니즘):

```text
same or related underlying
compatible currency pair
tenor alignment
quantity alignment
pricing convention
market structure
```

Correlation có thể mạnh trong mẫu (sample / 표본) bình thường nhưng gãy trong stress vì basis, liquidity, fixing hoặc counterparty effects.

## 9. Credit rủi ro (risk / 위험) must not dominate

Nếu credit deterioration chi phối changes in giá trị (value / 값), relationship có thể không còn phản ánh hedge economics mong muốn.

Ví dụ:

```text
forward offsets FX risk mechanically
but counterparty credit spread widens sharply
→ instrument fair value changes include a dominant credit component
```

Do đó counterparty monitoring không chỉ là legal/credit side issue; nó có thể ảnh hưởng effectiveness assessment và replacement chiến lược (strategy / 전략).

## 10. Hedge ratio

Designated hedge ratio phải phản ánh quantity của hedged item mà thực thể (entity / 엔터티) thực sự hedge và quantity của hedging instrument thực sự dùng, đồng thời không được tạo imbalance nhằm đạt accounting kết quả (outcome / 결과) không phù hợp với purpose của hedge accounting.

Tách ba ratios:

```text
economic hedge ratio
executed trade ratio
accounting-designated hedge ratio
```

Ba ratios có thể khác, nhưng mọi difference cần đơn vị sở hữu (owner / 오너), rationale và attribution rõ ràng.

## 11. Sources of ineffectiveness

Dùng chung (common / 공통) FX sources gồm:

```text
notional mismatch
timing mismatch
forecast-volume error
different fixing / settlement date
spot vs forward-element treatment
cross-currency basis
option time value
credit risk
liquidity / bid-ask
proxy or cross hedge
```

Một report chỉ ghi “hedge effective” mà không dự báo nguồn (source / 소스) of ineffectiveness là chưa đủ cho quản trị (governance / 거버넌스).

## 12. Rebalancing không phải che giấu forecast lỗi (error / 오류)

Rebalancing điều chỉnh designated quantities để hedge ratio tiếp tục phản ánh relationship khi variables của relationship thay đổi nhưng risk-management mục tiêu (objective / 목표) vẫn còn.

Không được dùng từ `rebalancing` cho mọi hành động:

```text
new speculative view
forecast transaction no longer expected
risk-management objective changed
trade added only to engineer accounting result
```

Mỗi adjustment cần phân biệt:

```text
economic rebalance
accounting rebalancing
partial discontinuation
new designation
trade termination / replacement
```

## 13. Discontinuation ranh giới (boundary / 경계)

Relationship có thể cần discontinue toàn bộ hoặc một phần khi qualifying criteria không còn đáp ứng hoặc risk-management mục tiêu (objective / 목표) thay đổi.

Operational question:

```text
What changed?
When was it known?
Which quantity is affected?
Does the derivative remain outstanding?
What is the new economic exposure?
Is a new designation appropriate?
```

Accounting discontinuation không tự động yêu cầu close derivative; trade quyết định (decision / 결정) và accounting designation là hai điều khiển (control / 제어) paths liên quan nhưng khác nhau.

## 14. Forward elements và option thời gian (time / 시간) giá trị (value / 값)

Economic hedge chi phí (cost / 비용) có thể gồm:

```text
forward points
cross-currency basis
option premium / time value
spread and execution cost
collateral funding
```

Accounting treatment của spot thành phần (component / 컴포넌트), forward element hoặc option thời gian (time / 시간) giá trị (value / 값) phụ thuộc designation và applicable requirements. Chapter này không cung cấp journal entries; mục tiêu là buộc workflow lưu component-level valuation và không gọi toàn bộ carry/premium là “hedge thất bại (failure / 실패)”.

## 15. ánh xạ (mapping / 매핑) vào bốn institutional cases

### Korean exporter
Phần “Korean exporter” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Forecast USD receivable
→ probability, layer, timing and customer evidence
→ forward designation
→ forecast error / over-hedge monitoring
```

### Korean importer
Phần “Korean importer” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
USD payable or forecast purchase
→ contracted vs forecast amount
→ forward/option hedge
→ shipment delay and volume mismatch
```

### Toàn cục (global / 전역) asset manager
Phần “Toàn cục (global / 전역) asset manager” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
foreign asset / benchmark exposure
→ strategic hedge ratio
→ NAV drift and rebalance
→ designation and presentation-currency boundary
```

### Cross-currency funding
Phần “Cross-currency funding” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
debt and economic funding currency
→ CCS / FX-swap components
→ basis, collateral and credit effects
→ fair-value/cash-flow classification requires entity-specific analysis
```

## 16. Minimum documentation pack

Học tập (learning / 학습) sản phẩm tạo ra (artifact / 산출물):

```text
hedge_policy.md
exposure_register.csv
forecast_evidence.md
designation_memo.md
trade_to_exposure_map.csv
valuation_component_report.csv
ineffectiveness_analysis.md
rebalance_discontinuation_log.md
close_review_signoff.md
```

Minimum fields:

```text
exposure owner
accounting owner
approval timestamp
hedged item and risk
instrument and trade ID
currency / amount / tenor
hedge ratio
method and frequency of assessment
known ineffectiveness sources
exception / escalation status
```

## 17. Monthly close điều khiển (control / 제어) luồng (flow / 흐름)
Phần “17. Monthly close điều khiển (control / 제어) luồng (flow / 흐름)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Exposure register reconciliation
→ trade completeness check
→ valuation and market-data validation
→ qualifying-criteria reassessment
→ ineffectiveness analysis
→ forecast-probability review
→ rebalance/discontinuation decision
→ accounting close and disclosure package
→ independent review / sign-off
```

Treasury, accounting, rủi ro (risk / 위험) and kiểm tra (audit / 감사) may own different steps. A spreadsheet owned by one trader without thay đổi (change / 변경) log, kiểm soát truy cập (access control / 접근 제어) or rà soát (review / 검토) is a quản trị (governance / 거버넌스) weakness even if calculations are correct.

## 18. bằng chứng (evidence / 증거) hierarchy
Phần “18. bằng chứng (evidence / 증거) hierarchy” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Executed contract / legal confirmation
Approved forecast and business evidence
Official market data / valuation source
Documented methodology
System-generated reconciliation
Independent review
Management assertion
```

Assertions do not replace giao dịch (transaction / 트랜잭션) and forecast bằng chứng (evidence / 증거).

## 19. Red flags
Phần “19. Red flags” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
designation created after seeing period-end P/L
hedged item described only as "FX risk"
forecast volume repeatedly misses without policy change
trade amount differs from designated amount without reconciliation
credit or collateral stress omitted from effectiveness review
economic hedge ratio changed but designation was not reviewed
derivative P/L reported without underlying exposure attribution
local K-IFRS / tax / legal conclusion copied from generic IFRS summary
```

## 20. rà soát (review / 검토) questions

1. Economic mục tiêu (objective / 목표) là variance reduction, budget-rate protection hay fair-value rủi ro (risk / 위험) management?
2. Hedged item có eligible và sufficiently specific không?
3. Documentation được hoàn thành khi nào?
4. Economic relationship dựa trên cơ chế (mechanism / 메커니즘) nào?
5. Credit rủi ro (risk / 위험) có thể dominate trong stress nào?
6. Economic, executed và designated hedge ratios khác nhau ở đâu?
7. Forecast giao dịch (transaction / 트랜잭션) bằng chứng (evidence / 증거) có point-in-time và đơn vị sở hữu (owner / 오너) không?
8. Rebalancing khác discontinuation như thế nào trong trường hợp (case / 사례) này?
9. Derivative còn outstanding sau accounting discontinuation thì ai quản trị?
10. tiêu chuẩn (standard / 표준)/adoption/local-policy nào phải verify trước khi áp dụng?

## 21. Sources and cập nhật (update / 업데이트) watch
Phần “21. Sources and cập nhật (update / 업데이트) watch” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- [IFRS Foundation — IFRS 9 Financial Instruments](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/)
- [IFRS Foundation — IFRS 9 project summary](https://www.ifrs.org/content/dam/ifrs/project/fi-hedge-accounting/ifrs-standard/project-summary.pdf)
- [IFRS Foundation — IFRS 9 supporting material](https://www.ifrs.org/supporting-implementation/supporting-materials-by-ifrs-standards/ifrs-9/)
- [IFRS Foundation — IFRIC 16, hedges of a net investment in a foreign operation](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation/)
- [IASB Update July 2026 — Post-implementation Review of IFRS 9 hedge accounting](https://www.ifrs.org/news-and-events/updates/iasb/2026/iasb-update-july-2026/)

IASB đang thực hiện post-implementation rà soát (review / 검토) về hedge-accounting/disclosure requirements trong 2026. Vì vậy, trước khi dùng chapter cho hiện thực (implementation / 구현) thực tế, phải kiểm tra tiêu chuẩn (standard / 표준), amendments, agenda decisions và cục bộ (local / 로컬) adoption mới nhất.

Đọc cùng:

- [Lab 08 — Hedge Accounting Documentation Boundary](../90_labs/08_HEDGE_ACCOUNTING_DOCUMENTATION_BOUNDARY_LAB.md)
- [Institutional FX Hedging Case Studies](../60_institutional_hedging_cases/README.md)
- [FX options, volatility and hedging](../14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)
- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [Systematic risk and attribution project](../70_systematic_project/README.md)

> **Bàn giao:** Sau khi phân biệt economic kết quả (outcome / 결과) với accounting treatment, quay lại institutional trường hợp (case / 사례) hoặc portfolio-risk đơn vị sở hữu (owner / 오너) để kiểm tra hedge effectiveness và residual rủi ro (risk / 위험); không suy ngược từ accounting designation thành bằng chứng hedge đã tối ưu.
