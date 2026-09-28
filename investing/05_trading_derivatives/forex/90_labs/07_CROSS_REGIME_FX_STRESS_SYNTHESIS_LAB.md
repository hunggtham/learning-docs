# Lab 07 — Cross-Regime FX Stress Synthesis

> **Mạch đọc:** Đây là capstone nối các trường hợp (case / 사례) và lab trước thành một khung so sánh cross-regime. Hãy mang bằng chứng (evidence / 증거) từ từng trường hợp (case / 사례) vào cùng các lớp **vulnerability → trigger → amplifier → thị trường (market / 시장) thất bại (failure / 실패) → chính sách (policy / 정책) phản hồi (response / 응답)**, rồi dùng phần `Đọc tiếp` để quay lại đơn vị sở hữu (owner / 오너) lý thuyết (theory / 이론) thay vì gom mọi crisis thành một mẫu (pattern / 패턴).

Lab này là capstone của `80_case_studies/`. Mục tiêu không phải nhớ bảy timeline, mà là phân biệt **vulnerability, trigger, amplifier, thị trường (market / 시장) thất bại (failure / 실패) và chính sách (policy / 정책) phản hồi (response / 응답)** khi nhiều trường hợp (case / 사례) cùng dùng các từ như “intervention”, “funding stress” hoặc “currency crisis”.

```text
Case evidence
→ mechanism classification
→ balance-sheet transmission
→ observable indicators
→ policy constraint
→ reverse stress test
→ decision rule and invalidation
```

Mọi kết luận phải chỉ ra trường hợp (case / 사례) nào hỗ trợ, trường hợp (case / 사례) nào phản ví dụ và phần nào không thể generalize.

## 1. sản phẩm tạo ra (artifact / 산출물) đặc tả hợp đồng (contract / 계약)

Tạo năm đầu ra (output / 출력):

```text
fx_regime_comparison_matrix.md
fx_trigger_amplifier_graph.md
fx_balance_sheet_transmission.md
fx_cross_regime_dashboard.md
fx_reverse_stress_memo.md
```

Mỗi sản phẩm tạo ra (artifact / 산출물) phải phân loại:

```text
Historical fact
Mechanism inference
Current observation
Scenario assumption
Decision rule
Invalidation
Residual uncertainty
```

Không dùng một sự kiện (event / 이벤트) lịch sử làm bằng chứng rằng cùng price mẫu (pattern / 패턴) sẽ lặp lại.

## 2. trường hợp (case / 사례) universe

Dùng đủ bảy trường hợp (case / 사례):

```text
01 ERM 1992
02 Asian Financial Crisis 1997
03 SNB floor removal 2015
04 Global USD funding stress 2020
05 JPY rate divergence and intervention 2022–2024
06 Korea USD funding stress 2008
07 Vietnam FX-management stress 2022–2023
```

Nếu bỏ một trường hợp (case / 사례), phải ghi rõ vì sao cơ chế (mechanism / 메커니즘) của nó không liên quan đến câu hỏi nghiên cứu.

## 3. Regime comparison ma trận (matrix / 행렬)

Điền một hàng cho mỗi trường hợp (case / 사례):

| Dimension | Câu hỏi |
|---|---|
| Regime quy tắc (rule / 규칙) | Fixed band, chính sách (policy / 정책) floor, managed flexibility hay float? |
| Stability cơ chế (mechanism / 메커니즘) | Điều gì giữ hệ thống ổn định trước stress? |
| Hidden vulnerability | ràng buộc (constraint / 제약조건) nào tích tụ nhưng chưa hiện ra trong spot? |
| Trigger | sự kiện (event / 이벤트) nào thay đổi expectation hoặc funding truy cập (access / 접근)? |
| Amplifier | Leverage, mismatch, stop, basis, reserve hay positioning? |
| thị trường (market / 시장) thất bại (failure / 실패) | Price gap, rollover freeze, basis blowout hay bank liquidity stress? |
| chính sách (policy / 정책) công cụ (tool / 도구) | tỷ lệ (rate / 비율), intervention, swap line, reserve, band thay đổi (change / 변경) hay abandonment? |
| chính sách (policy / 정책) ràng buộc (constraint / 제약조건) | Domestic cycle, balance sheet, reserves, inflation hay credibility? |
| Balance-sheet loser | Ai chịu cash-flow hoặc collateral pressure? |
| Non-generalizable element | Phần nào chỉ thuộc institutional setting đó? |

Ma trận (matrix / 행렬) đạt yêu cầu khi hai trường hợp (case / 사례) có cùng headline nhưng khác cơ chế (mechanism / 메커니즘) không bị gộp chung. Ví dụ:

```text
ERM 1992 intervention
≠ JPY 2022 intervention
≠ Vietnam 2022 FX management

Korea 2008 USD shortage
≠ Global 2020 dash for cash
```

## 4. Vulnerability–trigger–amplifier decomposition

Với mỗi trường hợp (case / 사례), viết đúng ba câu:

```text
Vulnerability existed because ...
Trigger changed the state because ...
Amplifier made the move nonlinear because ...
```

Ví dụ format:

```text
Vulnerability: short-term USD funding financed longer/mismatched exposure.
Trigger: offshore rollover capacity contracted.
Amplifier: basis widening and collateral demand forced more USD buying.
```

Không dùng trigger để thay thế vulnerability. Một tỷ lệ (rate / 비율) quyết định (decision / 결정) có thể là trigger, nhưng fragility thường đã tồn tại trước headline.

## 5. Same shock, different regime

Giả sử dùng chung (common / 공통) shock:

```text
US 2Y yield +100 bp
Broad USD +7%
Global equity −15%
Energy price +20%
USD funding spread +120 bp
```

So sánh transmission vào:

```text
USD/JPY
USD/KRW
USD/VND
EUR/USD
EUR/CHF
```

Với mỗi pair, ghi:

```text
rate channel
trade / commodity channel
funding channel
positioning channel
policy/intervention channel
liquidity and execution channel
main falsifier
```

Không ép tất cả pairs đi cùng hướng. JPY có thể phản ứng khác tùy tỷ lệ (rate / 비율) divergence hay carry unwind; VND có thể chuyển adjustment sang reserve, band, liquidity hoặc quote availability.

## 6. Balance-sheet transmission dấu vết (trace / 추적)

Chọn bốn actors:

```text
exporter
importer
bank / dealer
global asset manager
```

Với mỗi actor, dấu vết (trace / 추적):

```text
underlying cash flow
currency denomination
hedge instrument
funding maturity
collateral requirement
mark-to-market
settlement cash need
residual exposure
```

Sau đó stress hai conditions:

```text
A. spot moves but funding remains liquid
B. spot moves less, but funding/collateral market freezes
```

Mục tiêu là chứng minh rằng điều kiện (condition / 조건) B có thể nguy hiểm hơn dù chart spot ít dramatic hơn.

## 7. Policy-tool map

So sánh:

```text
interest-rate defense
spot intervention
forward / swap-market liquidity
central-bank dollar swap line
trading-band widening
policy-floor abandonment
capital-flow / macroprudential measure
```

Với từng công cụ (tool / 도구), ghi:

| trường dữ liệu (field / 필드) | Nội dung |
|---|---|
| mục tiêu (objective / 목표) | volatility, mức (level / 수준), liquidity hay solvency? |
| Transmission | thị trường (market / 시장) nào và balance sheet nào thay đổi? |
| sức chứa (capacity / 용량) | reserve, collateral, credibility hoặc legal truy cập (access / 접근) |
| thời gian (time / 시간) horizon | intraday, weeks hay structural? |
| Side tác động (effect / 효과) | growth, inflation, moral hazard, basis hoặc thị trường (market / 시장) functioning |
| thất bại (failure / 실패) điều kiện (condition / 조건) | khi nào công cụ (tool / 도구) không còn đủ? |

Không đánh giá chính sách (policy / 정책) chỉ bằng spot close cuối ngày.

## 8. Cross-regime monitoring dashboard

Thiết kế dashboard tối thiểu:

```text
spot and realized volatility
forward points
cross-currency basis / FX swap proxy
front-end rate differential
reserve data with publication lag
short-term external debt / rollover proxy
option skew / risk reversal
bid-ask / market depth proxy
trade and commodity exposure
bank funding / collateral indicator
official communication timestamp
```

Với mỗi chỉ số (metric / 지표), ghi:

```text
source
frequency
publication lag
revision risk
what it measures
what it does not measure
```

Một dashboard có nhiều series nhưng không ghi thông tin (information / 정보) thời gian (time / 시간) vẫn không đạt point-in-time tiêu chuẩn (standard / 표준).

## 9. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)

Không hỏi “scenario xấu nhất hợp lý là gì?” trước. Hãy bắt đầu từ thất bại (failure / 실패) điều kiện (condition / 조건):

```text
portfolio loses 10% equity
bank cannot meet USD payment tomorrow
importer breaches budget rate
hedge collateral exceeds available cash
policy reserve buffer falls below internal threshold
```

Sau đó giải ngược:

```text
spot move required
basis widening required
rollover failure required
correlation shift required
liquidity haircut required
```

Tạo ít nhất một reverse stress không cần spot move cực lớn. Điều này kiểm tra xem funding và collateral có đang bị bỏ quên hay không.

## 10. Counterfactual kiểm thử (test / 테스트)

Với ba trường hợp (case / 사례) bất kỳ, thay một điều kiện lịch sử:

```text
ERM: domestic cycle compatible hơn với anchor
Korea 2008: long-term USD funding thay cho short-term rollover
SNB 2015: floor exit communicated gradually
Vietnam 2022: larger usable reserve buffer
JPY 2022: narrower expected rate differential
```

Hỏi:

```text
price path có còn nonlinear không?
policy tool nào vẫn cần?
actor nào đổi từ loser thành survivor?
observable nào sẽ báo regime khác đi?
```

Counterfactual không nhằm viết lại lịch sử; nó kiểm tra bạn có hiểu nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘) hay chỉ nhớ kết quả (outcome / 결과).

## 11. quyết định (decision / 결정) memo

Viết memo tối đa hai trang:

```text
Current regime classification
Closest historical analog and why
Critical differences from that analog
Top three vulnerabilities
Trigger watchlist
Liquidity / execution assumptions
Policy-response tree
Position / hedge limit
Invalidation and kill condition
```

Memo chưa đạt nếu chỉ viết “giống 1997”, “giống 2008” hoặc “central bank sẽ can thiệp”. Phải nêu nút (node / 노드) nào giống, nút (node / 노드) nào khác và dữ liệu nào xác nhận.

## 12. Scoring rubric

| Criterion | Weight | thất bại (failure / 실패) example |
|---|---:|---|
| cơ chế (mechanism / 메커니즘) separation | 25% | gộp mọi crisis thành currency sell-off |
| Balance-sheet dấu vết (trace / 추적) | 20% | chỉ nhìn chart, không có cash/collateral |
| Point-in-time bằng chứng (evidence / 증거) | 15% | dùng dữ liệu công bố sau sự kiện (event / 이벤트) |
| chính sách (policy / 정책) ràng buộc (constraint / 제약조건) | 15% | coi intervention là unlimited |
| thực thi (execution / 실행) realism | 15% | dùng mid price trong gap/liquidity freeze |
| vô hiệu hóa (invalidation / 무효화) | 10% | thesis không có điều kiện sai |

Điểm đạt tối thiểu là `80/100`, đồng thời không được thất bại (fail / 실패) cơ chế (mechanism / 메커니즘) separation hoặc point-in-time bằng chứng (evidence / 증거).

## 13. Đọc tiếp

- [Forex Historical Case Studies](../80_case_studies/README.md)
- [00 — FX funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [01 — Intervention, reserves, REER and valuation](../90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md)
- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [12 — Journal and performance attribution](../12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)

> **Bàn giao:** Sau capstone, quay lại trường hợp (case / 사례) hoặc lab nơi chỉ số (metric / 지표)/vô hiệu hóa (invalidation / 무효화) còn yếu; kết quả cần mở ra một vòng nghiên cứu mới có point-in-time bằng chứng (evidence / 증거), không kết thúc ở bảng điểm tổng hợp.
