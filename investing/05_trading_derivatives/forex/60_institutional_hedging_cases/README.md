# Institutional FX Hedging trường hợp (case / 사례) Studies

> **Mạch đọc:** Đọc **Institutional FX Hedging trường hợp (case / 사례) Studies** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **trường hợp (case / 사례) studies** sang **Không dùng hedge P/L riêng để đánh giá hedge**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Folder này chuyển Forex từ góc nhìn `trade direction` sang **balance-sheet rủi ro (risk / 위험) management**. Mục tiêu là hiểu doanh nghiệp, asset manager hoặc treasury desk không nhất thiết giao dịch FX để kiếm alpha; họ dùng spot/forward/NDF/swap/options để thay đổi phân phối (distribution / 분포) của cash luồng (flow / 흐름), funding chi phí (cost / 비용) và portfolio return.

Mô hình tư duy (mental model / 사고 모델) chung:

```text
Underlying business / asset exposure
→ Currency cash flows
→ Risk horizon
→ Hedge objective
→ Instrument
→ Hedge ratio / tenor
→ Carry / forward points / basis
→ Execution / liquidity
→ Residual risk
→ Hedge attribution
```

Một hedge tốt không được đánh giá bằng việc derivative có lãi hay lỗ riêng lẻ. Phải đánh giá **hedged item + hedge instrument** cùng nhau.

## Trường hợp (case / 사례) studies

1. [01_KOREAN_EXPORTER_USD_RECEIVABLE_HEDGE.md](./01_KOREAN_EXPORTER_USD_RECEIVABLE_HEDGE.md) — Korean exporter có USD receivables nhưng báo cáo chi phí/lợi nhuận chủ yếu bằng KRW; xây layered forward hedge và xử lý forecast lỗi (error / 오류).
2. [02_KOREAN_IMPORTER_USD_PAYABLE_HEDGE.md](./02_KOREAN_IMPORTER_USD_PAYABLE_HEDGE.md) — importer có USD payables; so sánh unhedged, forward, option và layered hedge khi timing/amount của payable chưa chắc chắn.
3. [03_GLOBAL_ASSET_MANAGER_CURRENCY_HEDGE.md](./03_GLOBAL_ASSET_MANAGER_CURRENCY_HEDGE.md) — portfolio foreign assets; tách local-asset return khỏi FX return, hedge ratio, hedge carry, rebalance và benchmark mismatch.
4. [04_CROSS_CURRENCY_FUNDING_AND_DEBT_HEDGE.md](./04_CROSS_CURRENCY_FUNDING_AND_DEBT_HEDGE.md) — company/financial institution huy động một currency nhưng cần economic funding ở currency khác; nối debt, FX swap/cross-currency swap, basis, collateral và refinancing rủi ro (risk / 위험).


> **Chuyển mạch:** Từ **trường hợp (case / 사례) studies**, ta sang **Không dùng hedge P/L riêng để đánh giá hedge** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Không dùng hedge P/L riêng để đánh giá hedge

Ví dụ exporter long economic USD receivable và short USD forward:

```text
KRW strengthens
→ receivable converts into fewer KRW
→ forward hedge tends to gain
```

Nếu chỉ nhìn derivative P/L, hedge có thể “lãi”; nhưng mục tiêu là giảm variance của combined cash luồng (flow / 흐름).

Ngược lại:

```text
KRW weakens
→ receivable worth more KRW
→ forward hedge tends to lose
```

Derivative mất mát (loss / 손실) không tự động là thất bại (failure / 실패).


> **Chuyển mạch:** Từ **Không dùng hedge P/L riêng để đánh giá hedge**, ta sang **Các loại rủi ro (risk / 위험) phải tách** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Các loại rủi ro (risk / 위험) phải tách

```text
Transaction exposure
Translation exposure
Economic exposure
Forecast-volume risk
Timing risk
Basis risk
Counterparty risk
Liquidity risk
Collateral / margin risk
Funding / rollover risk
```

Không một hedge instrument nào xóa tất cả.


> **Chuyển mạch:** Từ **Các loại rủi ro (risk / 위험) phải tách**, ta sang **Hedge chính sách (policy / 정책) trước hedge trade** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hedge chính sách (policy / 정책) trước hedge trade

Trường hợp (case / 사례) nào cũng phải viết chính sách (policy / 정책) trước:

```text
What exposure is being hedged?
What is the risk horizon?
What volatility/loss is unacceptable?
How certain is amount and timing?
What instruments are legally/operationally available?
What hedge ratio is allowed?
How often is hedge rebalanced?
What is the treatment of over-hedge / under-hedge?
How is hedge effectiveness measured?
```


> **Chuyển mạch:** Từ **Hedge chính sách (policy / 정책) trước hedge trade**, ta sang **Kết nối với các phần khác** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối với các phần khác

- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [Intervention, reserves, REER and valuation](../90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md)
- [Economic hedge vs hedge accounting](../90_connections/02_ECONOMIC_HEDGE_VS_HEDGE_ACCOUNTING.md)
- [FX settlement, PvP, netting and liquidity](../90_connections/03_FX_SETTLEMENT_PVP_NETTING_AND_LIQUIDITY.md)
- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [FX options and hedging](../14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)
- [Systematic risk/attribution project](../70_systematic_project/README.md)


> **Chuyển mạch:** Từ **Kết nối với các phần khác**, ta sang **đầu ra (output / 출력) chuẩn cho mỗi trường hợp (case / 사례)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đầu ra (output / 출력) chuẩn cho mỗi trường hợp (case / 사례)

```text
Exposure map
Cash-flow timeline
Unhedged scenario table
Hedge instruments considered
Hedge ratio and tenor
Forward/carry economics
Stress scenarios
Residual risks
Hedge P/L + underlying P/L attribution
Roll/rebalance rule
Failure modes
Decision review
```

Các trường hợp (case / 사례) là học tập (learning / 학습) artifacts, không phải khuyến nghị hedge ratio hoặc sản phẩm cho một doanh nghiệp cụ thể.

> **Bàn giao:** Sau **đầu ra (output / 출력) chuẩn cho mỗi trường hợp (case / 사례)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 KOREAN EXPORTER USD RECEIVABLE HEDGE](./01_KOREAN_EXPORTER_USD_RECEIVABLE_HEDGE.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
