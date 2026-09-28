# Trường hợp (case / 사례) 06 — Korea 2008: USD funding stress, forward hedges và rollover rủi ro (risk / 위험)

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 06 — Korea 2008: USD funding stress, forward hedges và rollover rủi ro (risk / 위험)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Bối cảnh trước khủng hoảng** sang **2. Vì sao forward hedge tạo liquidity exposure?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Trường hợp (case / 사례) này bổ sung một cơ chế (mechanism / 메커니즘) khác với Asian Financial Crisis 1997 và toàn cục (global / 전역) USD funding stress 2020. Trọng tâm là cách **exporter forward hedges, foreign-bank-branch funding, maturity mismatch và toàn cục (global / 전역) dollar liquidity** biến một hedge có vẻ hợp lý thành nhu cầu mua USD spot trong lúc thị trường bị thiếu thanh khoản.

```text
Export receipts expected in USD
→ exporter sells USD forward to hedge
→ bank buys USD forward and borrows USD offshore to hedge itself
→ short-term dollar funding / rollover becomes part of the chain
→ global liquidity shock blocks rollover
→ forward positions and funding books must be rebalanced
→ USD demand, KRW volatility and basis stress rise together
```

`as_of_date: 2026-09-27`
Các con số lịch sử là facts từ IMF/Federal Reserve; scenario và ledger cuối trường hợp (case / 사례) là simulation.

## 1. Bối cảnh trước khủng hoảng

Trong giai đoạn trước 2008, Hàn Quốc có dòng vốn liên quan tới:

```text
shipbuilding orders
export receipts
outward investment
foreign-bank-branch funding
covered-interest and forward transactions
```

Một exporter muốn khóa tỷ giá cho khoản USD sẽ nhận trong tương lai có thể bán USD forward cho domestic bank hoặc foreign bank branch. Bank cần hedge lại position nên vay USD ở offshore thị trường (market / 시장), đổi một phần sang KRW và đầu tư/financing trong nước.

Sơ đồ balance-sheet giản lược:

```text
Exporter:       future +USD → sells USD forward
Bank:           buys USD forward → needs future USD
Funding desk:   borrows short-term USD offshore
Local assets:   holds KRW asset or loan against the funding structure
```

Điểm quan trọng: **hedge của exporter không tự động làm hệ thống có thêm USD dài hạn**. Nó có thể tạo một chuỗi trung gian phụ thuộc vào rollover.


> **Chuyển mạch:** Từ **1. Bối cảnh trước khủng hoảng**, ta sang **2. Vì sao forward hedge tạo liquidity exposure?** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Vì sao forward hedge tạo liquidity exposure?

Nếu forward maturity và USD borrowing maturity khớp, bank có thể nghĩ rằng rủi ro đã được khóa. Trong thực tế có nhiều lệch pha:

```text
forward tenor ≠ borrowing tenor
export delivery date uncertain
ship order may be delayed or cancelled
USD funding line may not roll
collateral / margin may change
spot and forward liquidity may diverge
```

Một bank có thể **đúng về currency direction** nhưng vẫn thiếu USD hôm nay để thanh toán khoản vay ngắn hạn. Đây là funding rủi ro (risk / 위험), không phải chỉ là market-view rủi ro (risk / 위험).


> **Chuyển mạch:** Từ **2. Vì sao forward hedge tạo liquidity exposure?**, ta sang **3. Số liệu vulnerability cần đọc đúng cách** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Số liệu vulnerability cần đọc đúng cách

IMF 2008 ghi nhận tổng bên ngoài (external / 외부) liabilities của Korea tăng từ khoảng `US$260.1bn` cuối 2006 lên `US$412.5bn` trong quý I/2008; short-term thành phần (component / 컴포넌트) tăng từ `US$113.7bn` lên `US$176.5bn`. IMF cũng mô tả khoảng một nửa phần tăng short-term borrowing có liên quan đến currency hedging của exporters, đặc biệt shipbuilders.

Không được đọc các con số này như kết luận “toàn bộ bên ngoài (external / 외부) debt là toxic”. Cần tách:

```text
trade-credit backed by future exports
hedge-related borrowing
foreign-bank-branch interoffice funding
portfolio flows
domestic-bank foreign-currency debt
```

Vulnerability nằm ở **maturity, rollover, collateral và liquidity under stress**, không chỉ ở gross debt headline.


> **Chuyển mạch:** Từ **3. Số liệu vulnerability cần đọc đúng cách**, ta sang **4. Crisis transmission** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Crisis transmission

Khi toàn cục (global / 전역) financial crisis làm các wholesale dollar markets co lại:

```text
global banks protect USD liquidity
→ Korean foreign-bank branches face tighter credit lines
→ short-term USD liabilities approach maturity
→ rollover rate falls / tenor shortens
→ banks seek USD in spot and FX swap markets
→ KRW weakens and basis spreads widen
→ margin and collateral needs rise
```

Nếu shipbuilder forward positions bị điều chỉnh vì đặc tả hợp đồng (contract / 계약) cancellation, delayed delivery hoặc hedge ratio thay đổi, expected future USD inflow không còn giống giả định ban đầu. Một số position phải được close hoặc roll trong thị trường (market / 시장) đang thiếu USD.

Đây là vòng phản hồi (feedback loop / 피드백 루프):

```text
funding stress
→ USD demand
→ KRW depreciation
→ larger KRW value of USD liabilities
→ balance-sheet pressure
→ less willingness to extend funding
→ more USD demand
```


> **Chuyển mạch:** Từ **4. Crisis transmission**, ta sang **5. Forward hedge không đồng nghĩa spot supply ổn định** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. Forward hedge không đồng nghĩa spot supply ổn định

Trong điều kiện bình thường, exporter forward selling có thể tạo cảm giác rằng hệ thống luôn có nguồn USD tương lai. Nhưng khi forward đặc tả hợp đồng (contract / 계약) được unwind:

```text
expected export receipt delayed/cancelled
→ original forward hedge no longer matches underlying
→ exporter/bank must buy or roll USD
→ spot demand appears exactly when liquidity is weak
```

Điều này giải thích vì sao phải tách:

```text
underlying exposure
hedge notional
hedge maturity
funding maturity
cash settlement requirement
```

Không được gọi mọi forward luồng (flow / 흐름) là “speculation”. Nhưng cũng không được coi hedge luồng (flow / 흐름) là liquidity-neutral trong mọi trạng thái.


> **Chuyển mạch:** Từ **5. Forward hedge không đồng nghĩa spot supply ổn định**, ta sang **6. Covered interest parity và basis** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. Covered interest parity và basis

Một participant có thể quan sát deviation giữa implied won tỷ lệ (rate / 비율) từ FX forward và cục bộ (local / 로컬) KRW tỷ lệ (rate / 비율). Tuy nhiên, deviation không tự động là arbitrage-free profit:

```text
CIP deviation
− balance-sheet cost
− credit limit
− collateral
− tenor mismatch
− capital / regulatory constraint
− execution cost
```

Trong stress, chính các điều kiện cần để arbitrage đóng wedge có thể biến mất. Bank không thể giả định rằng USD borrowing sẽ luôn available ở tỷ lệ (rate / 비율) dùng trong spreadsheet.

Vì vậy, basis cần được đọc như một biến của **funding scarcity và balance-sheet sức chứa (capacity / 용량)**, không chỉ như pricing lỗi (error / 오류).


> **Chuyển mạch:** Từ **6. Covered interest parity và basis**, ta sang **7. chính sách (policy / 정책) phản hồi (response / 응답) và USD swap line** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. chính sách (policy / 정책) phản hồi (response / 응답) và USD swap line

Federal Reserve ghi nhận BOK đã dùng reserves để giảm dollar shortage và thiết lập dollar liquidity swap line với Fed vào tháng 10/2008. Swap line cho phép BOK nhận USD ngắn hạn rồi cung ứng lại cho financial institutions khi private dollar funding thị trường (market / 시장) bị suy giảm.

Cơ chế khái quát:

```text
Fed ↔ BOK swap line
→ BOK receives USD against KRW collateral/transaction
→ BOK lends USD through an auction or facility
→ private rollover pressure is reduced
→ funding market can reopen gradually
```

Swap line giải quyết **liquidity backstop**; nó không biến mọi borrower thành solvent, không xóa currency mismatch, và không đảm bảo KRW sẽ lập tức quay về mức cũ.


> **Chuyển mạch:** Từ **7. chính sách (policy / 정책) phản hồi (response / 응답) và USD swap line**, ta sang **8. Phân biệt 2008 với 1997 và 2020** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 8. Phân biệt 2008 với 1997 và 2020

| trường hợp (case / 사례) | Primary stress | Distinctive cơ chế (mechanism / 메커니즘) | Lesson |
|---|---|---|---|
| Asian Crisis 1997 | currency mismatch + sudden stop | cục bộ (local / 로컬) banking/borrower fragility và fixed-regime pressure | foreign-currency debt có thể khuếch đại banking crisis |
| Korea 2008 | USD rollover + forward-hedge plumbing | exporter forwards nối với foreign-bank-branch short-term funding | hedge chuỗi (chain / 사슬) có thể tạo maturity/liquidity rủi ro (risk / 위험) |
| toàn cục (global / 전역) USD stress 2020 | toàn cục (global / 전역) dash for cash | offshore dollar shortage, swaps và collateral demand | reserve currency funding có thể căng ngoài domestic hệ thống (system / 시스템) |

Không gộp ba trường hợp (case / 사례) thành một bài “USD shortage”. Cùng là dollar stress nhưng nút (node / 노드) gây đứt, chính sách (policy / 정책) công cụ (tool / 도구) và balance-sheet transmission khác nhau.


> **Chuyển mạch:** Từ **8. Phân biệt 2008 với 1997 và 2020**, ta sang **9. Balance-sheet trường hợp (case / 사례) exercises** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 9. Balance-sheet trường hợp (case / 사례) exercises

### Trường hợp (case / 사례) A — Shipbuilder

Giả sử shipbuilder sẽ nhận `USD 100m` sau 12 tháng và đã bán forward `USD 80m`:

```text
hedged amount = 80m
unhedged amount = 20m
delivery date uncertain
```

Hãy stress:

```text
USD strengthens 15%
delivery delayed 6 months
contract cancelled 25%
forward points widen
counterparty asks for additional collateral
```

Tách:

```text
economic exposure
derivative mark-to-market
cash settlement
volume mismatch
timing mismatch
counterparty / collateral risk
```

### Trường hợp (case / 사례) B — Foreign bank branch

Branch có:

```text
long USD forward from exporter
short-term USD borrowing from headquarters
KRW asset funded after spot conversion
```

Lập maturity ladder `1w / 1m / 3m / 6m / 1y`. Sau đó giả định:

```text
1-month USD line rolls at only 40%
3-month basis widens by 150 bp
KRW falls 10%
collateral haircut increases
```

Tính USD cash gap và ghi rõ position nào cần unwind trước. Không net tất cả maturities thành một con số duy nhất.

### Trường hợp (case / 사례) C — chính sách (policy / 정책) analyst

So sánh ba công cụ:

```text
use reserves directly
provide USD through swap line
impose / tighten macroprudential limits on short-term FX funding
```

Với từng công cụ, ghi:

```text
immediate objective
balance-sheet channel
who receives liquidity
what risk remains
possible unintended effect
observable data
```


> **Chuyển mạch:** Từ **9. Balance-sheet trường hợp (case / 사례) exercises**, ta sang **10. Research exercise: event-study ledger** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 10. Research exercise: event-study ledger

Tạo bảng cho các mốc stress năm 2008:

```text
date / timestamp
global funding event
USD/KRW spot
1m / 3m FX swap or basis proxy
Korean bank external borrowing
foreign-bank-branch rollover signal
shipbuilding/export news
reserve or policy response
first reaction
follow-through
alternative explanation
```

Nếu dữ liệu (data / 데이터) intraday không tồn tại, ghi rõ frequency và publication lag. Không suy ra chính xác (exact / 정확한) intervention kích thước (size / 크기) từ reserve thay đổi (change / 변경) hoặc từ chart spot.


> **Chuyển mạch:** Từ **10. Research exercise: event-study ledger**, ta sang **11. rủi ro (risk / 위험) checklist** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 11. rủi ro (risk / 위험) checklist

```text
[ ] Forward hedge có underlying thật và amount/timing chắc chắn không?
[ ] Forward maturity có khớp funding maturity không?
[ ] USD liquidity có phải rollover-dependent không?
[ ] Spot, forward points và basis có được tách không?
[ ] Counterparty/collateral risk có được ghi không?
[ ] Exporter hedge unwind có thể tạo spot USD demand không?
[ ] Swap line là liquidity backstop hay solvency rescue?
[ ] Gross external debt đã được phân rã theo instrument chưa?
[ ] Không gọi CIP deviation là risk-free arbitrage
[ ] Không đồng nhất 2008 Korea với 1997 hoặc 2020
```


> **Chuyển mạch:** Từ **11. rủi ro (risk / 위험) checklist**, ta sang **12. Sources** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 12. Sources

- [IMF — Republic of Korea 2008 Article IV Consultation, Country Report 08/297](https://www.imf.org/external/pubs/ft/scr/2008/cr08297.pdf)
- [IMF — Macroprudential Policy, Korea case](https://www.elibrary.imf.org/view/journals/001/2011/238/article-A001-en.xml)
- [IMF — FX Funding Risks and Exchange Rate Volatility: Korea’s Case](https://www.elibrary.imf.org/view/journals/001/2012/268/article-A001-en.xml)
- [Federal Reserve — The Policy Response to the Crisis in Korea and Other Emerging Market Economies](https://www.federalreserve.gov/newsevents/speech/bernanke20100530a.htm)
- [Federal Reserve — Liquidity Swaps](https://www.federalreserve.gov/monetarypolicy/liquidity_swaps200906.htm)

Đọc cùng:

- [00 — FX funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [05 — Execution, brokers, costs and risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

> **Bàn giao:** Sau **12. Sources**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 ERM 1992 STERLING CRISIS](./01_ERM_1992_STERLING_CRISIS.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
