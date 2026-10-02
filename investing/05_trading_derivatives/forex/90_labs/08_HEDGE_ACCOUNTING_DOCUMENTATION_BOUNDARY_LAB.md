# Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. sản phẩm tạo ra (artifact / 산출물) đặc tả hợp đồng (contract / 계약)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. trường hợp (case / 사례) A — Korean exporter forecast receivable** để đem mô hình vào tình huống cụ thể. Mạch này nối hedge accounting với documentation boundary, exposure và effectiveness, để phân biệt phòng hộ kinh tế với cách ghi nhận kế toán.

Lab này operationalize [Economic Hedge vs Hedge Accounting](../90_connections/02_ECONOMIC_HEDGE_VS_HEDGE_ACCOUNTING.md). Mục tiêu là xây documentation/điều khiển (control / 제어) workflow cho một FX hedge mà không nhảy thẳng từ “derivative offset exposure” sang kết luận accounting.

```text
Economic exposure
→ Risk-management objective
→ Executed hedge
→ Eligibility candidate
→ Designation documentation
→ Effectiveness assessment
→ Rebalance / discontinuation decision
→ Close review and sign-off
```

Đây là simulation phục vụ học tập. Không tạo journal entries, tax position, K-IFRS conclusion hoặc legal opinion. Khi dùng dữ liệu thật, phải kiểm tra tiêu chuẩn (standard / 표준)/adoption hiện hành và thực thể (entity / 엔터티) chính sách (policy / 정책) với accounting/kiểm tra (audit / 감사) owners.

## 1. sản phẩm tạo ra (artifact / 산출물) đặc tả hợp đồng (contract / 계약)

Tạo sáu đầu ra (output / 출력):

```text
fx_exposure_register.csv
fx_designation_memo.md
fx_trade_to_exposure_map.csv
fx_ineffectiveness_analysis.md
fx_rebalance_discontinuation_log.md
fx_month_end_close_checklist.md
```

Mỗi sản phẩm tạo ra (artifact / 산출물) phải có:

```text
as_of_timestamp
preparer
reviewer
source system
version
approval state
exception status
```

Không chấp nhận một spreadsheet không có đơn vị sở hữu (owner / 오너), timestamp hoặc thay đổi (change / 변경) lịch sử (history / 이력) như nguồn chuẩn (source of truth / 정본).

> **Chuyển mạch:** Trong **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **1. sản phẩm tạo ra (artifact / 산출물) đặc tả hợp đồng (contract / 계약)** cho ta quy tắc; **2. trường hợp (case / 사례) A — Korean exporter forecast receivable** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **3. Exposure register** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. trường hợp (case / 사례) A — Korean exporter forecast receivable

Giả sử:

```text
Forecast USD receipts Q1 = USD 12m
Probability assessment   = highly probable under simulation assumption
Expected timing          = Jan 4m, Feb 5m, Mar 3m
Natural USD costs        = USD 2m across Q1
Executed forwards        = short USD 8m
Forward maturities       = Jan 3m, Feb 3m, Mar 2m
Functional currency      = KRW
```

Trước tiên tính economic exposure:

```text
gross forecast receipts
− natural USD costs
= net economic USD exposure
```

Sau đó tách:

```text
net economic exposure
executed hedge amount
candidate designated amount
unhedged residual
possible over-hedge under downside forecast
```

Không mặc định toàn bộ `USD 12m` là eligible hedged item chỉ vì sales nhóm (team / 팀) có forecast.

> **Chuyển mạch:** Ở chặng này của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **2. trường hợp (case / 사례) A — Korean exporter forecast receivable** cho ta quy tắc; **3. Exposure register** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **4. Economic mục tiêu (objective / 목표) memo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Exposure register

Tạo một row cho mỗi exposure tầng (layer / 계층):

| trường dữ liệu (field / 필드) | Example question |
|---|---|
| Exposure ID | Có stable identifier không? |
| nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너) | Sales/procurement/treasury đơn vị (unit / 단위) nào chịu trách nhiệm? |
| Currency | USD hay cross exposure khác? |
| Gross amount | Booked hay forecast? |
| Natural offset | USD costs/debt có thực sự cùng timing không? |
| Net amount | Sau netting quy tắc (rule / 규칙) được phê duyệt là bao nhiêu? |
| xác suất (probability / 확률) bằng chứng (evidence / 증거) | đặc tả hợp đồng (contract / 계약), purchase thứ tự (order / 순서), forecast lịch sử (history / 이력) hay assertion? |
| Expected date | Single date hay cửa sổ (window / 윈도우)? |
| Accounting status | Candidate, designated, rejected, discontinued? |
| nguồn (source / 소스) | ERP, CRM, đặc tả hợp đồng (contract / 계약) repository hay manual đầu vào (input / 입력)? |

Reconcile total register với nghiệp vụ (business / 비즈니스) forecast và treasury position. Difference phải có đơn vị sở hữu (owner / 오너) và explanation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **4. Economic mục tiêu (objective / 목표) memo** tiếp nhận điểm tựa từ **3. Exposure register** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Designation memo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Economic mục tiêu (objective / 목표) memo

Viết mục tiêu (objective / 목표) trước accounting phân tích (analysis / 분석):

```text
Risk being managed
Cash-flow or fair-value objective
Budget-rate / variance tolerance
Time horizon
Allowed instruments
Economic hedge ratio
Rebalance rule
Over-hedge limit
Counterparty / collateral limit
```

Mục tiêu (objective / 목표) chưa đạt nếu viết:

```text
"reduce FX risk"
"avoid losses"
"hedge because USD may fall"
```

Phải nêu measurable exposure và rủi ro (risk / 위험) phân phối (distribution / 분포) cần thay đổi.

> **Chuyển mạch:** Trong **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **5. Designation memo** tiếp nhận điểm tựa từ **4. Economic mục tiêu (objective / 목표) memo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Eligibility gate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Designation memo

Tạo memo với minimum sections:

```text
Hedging instrument
Hedged item
Hedged risk
Relationship type candidate
Risk-management objective
Designation date and time
Designated quantities
Hedge ratio
Assessment method
Expected sources of ineffectiveness
Review frequency
```

Kiểm tra point-in-time:

```text
trade execution timestamp
designation timestamp
forecast evidence timestamp
approval timestamp
```

Không backdate documentation sau khi đã biết period-end kết quả (outcome / 결과).

> **Chuyển mạch:** Ở chặng này của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **6. Eligibility gate** tiếp nhận điểm tựa từ **5. Designation memo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Qualifying-effectiveness assessment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Eligibility gate

Trả lời `yes / no / needs specialist review`:

```text
[ ] Hedging instrument candidate is eligible
[ ] Hedged item / component candidate is eligible
[ ] Forecast transaction evidence is sufficient
[ ] Risk component is specific and measurable
[ ] Formal documentation exists at inception
[ ] Entity accounting policy permits this designation
[ ] Local adoption / transition requirements were checked
```

Nếu một gate chưa đủ bằng chứng (evidence / 증거), ghi `unresolved`; không dùng giả định (assumption / 가정) để tự nâng thành `yes`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **7. Qualifying-effectiveness assessment** tiếp nhận điểm tựa từ **6. Eligibility gate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Sources-of-ineffectiveness bảng (table / 테이블)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Qualifying-effectiveness assessment

Đánh giá ba lớp riêng:

### Economic relationship

```text
same USD/KRW underlying?
compatible settlement/fixing?
matching direction?
tenor sufficiently aligned?
same quantity layer?
```

### Credit-risk dominance

```text
counterparty credit condition
collateral agreement
wrong-way risk
replacement availability
```

### Hedge ratio

```text
actual quantity hedged
actual instrument quantity
designated quantity
reason for any difference
imbalance risk
```

Không dùng một correlation statistic để thay cả ba lớp.

> **Chuyển mạch:** Trong **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **7. Qualifying-effectiveness assessment** nêu điều cần giải thích; **8. Sources-of-ineffectiveness bảng (table / 테이블)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. Month-one scenario** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Sources-of-ineffectiveness bảng (table / 테이블)

Lập bảng:

| nguồn (source / 소스) | Direction | Observable | đơn vị sở hữu (owner / 오너) | Escalation threshold |
|---|---|---|---|---|
| Timing mismatch | forecast vs forward maturity | days mismatch | Treasury | policy-defined |
| Amount mismatch | realised vs designated amount | USD variance | nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너) | policy-defined |
| Forward element | spot vs all-in forward | thành phần (component / 컴포넌트) valuation | Accounting | methodology-defined |
| Credit rủi ro (risk / 위험) | counterparty spread | CVA/credit proxy | rủi ro (risk / 위험) | credit limit |
| Liquidity | bid-ask / unwind chi phí (cost / 비용) | executable quote | Treasury | liquidity threshold |
| Basis | proxy/cross hedge divergence | basis series | thị trường (market / 시장) rủi ro (risk / 위험) | mô hình (model / 모델) threshold |

Threshold là simulation đầu vào (input / 입력); không bản sao (copy / 복사) thành chính sách (policy / 정책) thực tế.

> **Chuyển mạch:** Ở chặng này của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **8. Sources-of-ineffectiveness bảng (table / 테이블)** nêu điều cần giải thích; **9. Month-one scenario** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. Rebalancing cây quyết định (decision tree / 의사결정 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Month-one scenario

Giả sử cuối tháng 1:

```text
Actual receipt             = USD 2.5m
Original Jan forecast      = USD 4.0m
Jan forward maturity       = USD 3.0m
Remaining Q1 forecast      = USD 6.0m
One customer delays USD 2m to Q2
Counterparty spread widens
```

Tính:

```text
forecast error
current over-/under-hedge
cash settlement need
remaining economic exposure
designated relationship quantity affected
```

Sau đó phân loại hành động (action / 동작):

```text
economic trade adjustment
accounting rebalancing candidate
partial discontinuation candidate
new designation candidate
no action but enhanced monitoring
```

Không gộp năm hành động (action / 동작) thành một nút “rebalance”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **10. Rebalancing cây quyết định (decision tree / 의사결정 트리)** tiếp nhận điểm tựa từ **9. Month-one scenario** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Discontinuation log** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Rebalancing cây quyết định (decision tree / 의사결정 트리)

Đi theo thứ tự:

```text
Risk-management objective unchanged?
├── No  → discontinuation / new strategy review
└── Yes
    ├── Economic relationship still exists?
    │   ├── No  → discontinuation review
    │   └── Yes
    └── Hedge ratio no longer reflects actual quantities?
        ├── Yes → rebalancing candidate
        └── No  → continue with documented assessment
```

Đây là học tập (learning / 학습) cây quyết định (decision tree / 의사결정 트리), không thay thế wording đầy đủ của tiêu chuẩn (standard / 표준) hoặc auditor judgment.

> **Chuyển mạch:** Trong **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **11. Discontinuation log** tiếp nhận điểm tựa từ **10. Rebalancing cây quyết định (decision tree / 의사결정 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. trường hợp (case / 사례) B — uncertain importer payable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Discontinuation log

Minimum fields:

```text
relationship ID
affected quantity
reason
date condition became known
decision timestamp
derivative remains open?
new economic owner
replacement / unwind plan
new designation reference if any
reviewer sign-off
```

Accounting discontinuation và derivative termination phải là hai fields riêng.

> **Chuyển mạch:** Ở chặng này của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **11. Discontinuation log** cho ta quy tắc; **12. trường hợp (case / 사례) B — uncertain importer payable** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **13. trường hợp (case / 사례) C — option hedge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. trường hợp (case / 사례) B — uncertain importer payable

Giả sử importer có:

```text
Forecast purchase = USD 10m
Confirmed order   = USD 6m
Possible option   = USD 4m
Forward hedge     = USD 8m
Shipment delay    = possible 45 days
```

Phân lớp exposure:

```text
contracted
highly probable candidate
possible pipeline
```

Đánh giá:

```text
which layer can support a designation candidate?
what evidence is missing?
what happens if only USD 5m ships?
who owns the resulting derivative exposure?
```

Không gọi option-to-purchase hoặc management mục tiêu (target / 대상) là firm exposure.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **12. trường hợp (case / 사례) B — uncertain importer payable** cho ta quy tắc; **13. trường hợp (case / 사례) C — option hedge** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **14. trường hợp (case / 사례) D — cross-currency funding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. trường hợp (case / 사례) C — option hedge

Một importer mua USD lời gọi (call / 호출). Tách valuation thành:

```text
intrinsic value
time value
spot delta
volatility effect
```

Documentation phải ghi:

```text
what component is designated?
how option time value is tracked?
which market-data source is used?
how premium and execution cost are attributed?
```

Lab không yêu cầu journal entries; nó yêu cầu component-level bằng chứng (evidence / 증거) để specialist có thể áp dụng chính sách (policy / 정책) đúng.

> **Chuyển mạch:** Trong **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **13. trường hợp (case / 사례) C — option hedge** cho ta quy tắc; **14. trường hợp (case / 사례) D — cross-currency funding** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **15. Close-control checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. trường hợp (case / 사례) D — cross-currency funding

Một company phát hành KRW debt và dùng CCS để tạo synthetic USD funding. Tách:

```text
debt cash flows
CCS principal exchanges
fixed/floating interest legs
cross-currency basis
collateral cash flows
credit valuation effects
```

Không kết luận relationship kiểu (type / 타입) chỉ từ tên instrument. Ghi `specialist review required` cho classification, designation và đo lường (measurement / 측정) questions phụ thuộc facts.

> **Chuyển mạch:** Ở chặng này của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **14. trường hợp (case / 사례) D — cross-currency funding** cho ta quy tắc; **15. Close-control checklist** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **16. Segregation of duties** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Close-control checklist

```text
[ ] Exposure register reconciled to source systems
[ ] Trade population complete
[ ] Trade-to-exposure mapping has no unexplained orphan
[ ] Forecast probability reviewed by business owner
[ ] Market data and valuation independently checked
[ ] Economic relationship reassessed
[ ] Credit-risk dominance considered
[ ] Hedge ratio reconciled: economic / executed / designated
[ ] Ineffectiveness sources updated
[ ] Rebalance/discontinuation decisions timestamped
[ ] Outstanding derivatives after discontinuation assigned an owner
[ ] Exceptions escalated and signed off
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **16. Segregation of duties** tiếp nhận điểm tựa từ **15. Close-control checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Scoring rubric** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Segregation of duties

Thiết kế RACI cho:

```text
Business forecast owner
Treasury execution
Market-risk review
Counterparty-risk review
Accounting policy owner
Valuation control
Financial close
Internal audit
```

Người execute trade không nên là người duy nhất phê duyệt forecast, valuation và accounting conclusion.

> **Chuyển mạch:** Trong **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **17. Scoring rubric** tiếp nhận điểm tựa từ **16. Segregation of duties** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Đọc tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Scoring rubric

| Criterion | Weight | thất bại (failure / 실패) example |
|---|---:|---|
| Exposure specificity | 20% | hedged item chỉ ghi “USD rủi ro (risk / 위험)” |
| Point-in-time documentation | 20% | memo được tạo sau period end |
| Qualifying-gate lập luận (reasoning / 추론) | 20% | bỏ qua eligibility hoặc credit rủi ro (risk / 위험) |
| Ratio and mismatch reconciliation | 15% | executed/designated amount không khớp nhưng không giải thích |
| Rebalance/discontinuation distinction | 15% | gọi mọi adjustment là rebalance |
| quản trị (governance / 거버넌스) and bằng chứng (evidence / 증거) | 10% | không có đơn vị sở hữu (owner / 오너)/reviewer/nguồn (source / 소스) |

Điểm đạt tối thiểu `80/100`; point-in-time documentation hoặc qualifying-gate lập luận (reasoning / 추론) không được thất bại (fail / 실패).

> **Chuyển mạch:** Ở chặng này của **Lab 08 — Hedge Accounting Documentation ranh giới (boundary / 경계)**, **18. Đọc tiếp** tiếp nhận điểm tựa từ **17. Scoring rubric** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 18. Đọc tiếp

- [Economic Hedge vs Hedge Accounting](../90_connections/02_ECONOMIC_HEDGE_VS_HEDGE_ACCOUNTING.md)
- [Institutional FX Hedging Case Studies](../60_institutional_hedging_cases/README.md)
- [Case 01 — Korean exporter](../60_institutional_hedging_cases/01_KOREAN_EXPORTER_USD_RECEIVABLE_HEDGE.md)
- [Case 02 — Korean importer](../60_institutional_hedging_cases/02_KOREAN_IMPORTER_USD_PAYABLE_HEDGE.md)
- [Case 04 — Cross-currency funding](../60_institutional_hedging_cases/04_CROSS_CURRENCY_FUNDING_AND_DEBT_HEDGE.md)

> **Bàn giao:** Sau **18. Đọc tiếp**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
