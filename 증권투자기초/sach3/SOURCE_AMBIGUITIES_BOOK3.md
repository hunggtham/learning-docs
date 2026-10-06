# SOURCE AMBIGUITIES — 증권투자기초 Sách 3

> Source authority: `증권투자기초/sach3/raw_md/sach3.md`.
>
> Quy tắc: một vùng OCR không đủ chắc để khôi phục exact value/label thì không được suy đoán từ kiến thức ngoài rồi gọi là source fidelity. Semantic mechanism có thể được đánh `FULL` ở row riêng nếu prose quanh vùng đó xác nhận; exact table/figure/wording row này giữ `SOURCE_AMBIGUITY`.

| ID | Source location | Ambiguity | What is still verifiable | Learning handling |
|---|---|---|---|---|
| SRC-A01 | p.251, KOSPI200 futures market-quote screenshot | nhiều ô price/volume/open-interest OCR vỡ, không đủ để tái tạo bảng quote chính xác | tồn tại nhiều maturity; quote market có price/volume/open interest; surrounding prose explains futures mechanics | không chép lại cells; lesson giữ near/far month, open interest, volume và contract mechanics |
| SRC-A02 | p.264–267, option theoretical-price/Greeks tables and charts | exact cell values/labels bị OCR sai; bảng p.266 có delta/gamma/theta/vega/rho nhưng numbers không đáng tin để reproduce | prose p.263–265 xác nhận pricing inputs và định nghĩa delta/theta/vega; summary p.364 xác nhận gamma/rho | lesson giải thích Greeks + worked examples riêng; không gọi numeric table là verified |
| SRC-A03 | p.268, KOSPI200 option contract specification | contract size/listing/clock fields OCR vỡ và là snapshot lịch sử | đây là exchange-spec table và source itself treats such specs as changeable | lesson chỉ giữ mechanism; toàn bộ contract spec = `TEXTBOOK/SOURCE STATE`, phải check KRX hiện hành nếu giao dịch |
| SRC-A04 | p.293 vs p.373 | acronym IFR được expand thành “Internal Forward Rate” ở p.293 nhưng “Implied Forward Rate” ở comprehensive question p.373 | Korean `내재선도금리`, acronym IFR và no-arbitrage forward-rate mechanism đều nhất quán | lesson dùng `IFR (내재선도금리)`; exact English expansion không được tuyên bố source-unique |
| SRC-A05 | p.297, 10Y Korean Treasury futures specification | một phần fields đọc được nhưng một số units/times/notes OCR không chắc và spec là source-date snapshot | underlying/cash settlement/context of Korean rate futures verifiable | không dùng bảng này làm current contract specification; rate mechanics tách row FULL |
| SRC-A06 | p.308, USD futures specification | OCR làm hỏng một số contract/listing/min-tick fields; snapshot exchange rule có thể đổi | USD futures, physical delivery context, maturity/delivery discussion p.305/p.309 verifiable | exact contract values không được reproduce như current fact |
| SRC-A07 | p.320, pooled credit-product acronyms | loan pool `CLO` đọc rõ; ít nhất một debt/bond acronym OCR thành “Coo”/ký tự hỏng | distinction debt/loan/bond pool và cash-vs-synthetic securitization rõ; synthetic notional can exceed physical pool | lesson dùng standard `CDO/CLO` để nối concept nhưng coverage không coi exact p.320 “CDO” token là OCR-verified |
| SRC-A08 | p.328, crude-oil futures contract screenshot | exact code/unit/delivery-window cells OCR hỏng; historical exchange spec | physical-delivery nature, notional/margin/roll mechanisms confirmed by prose p.322–330 | lesson không reconstruct contract table; formula/mechanism rows separate FULL |
| SRC-A09 | p.352, trust/deposit wrapper acronyms | semantics “security → fund → trust → deposit” readable; ELF readable, nhưng một số acronym trust/deposit bị OCR vỡ | wrapper distinction itself is clear | lesson names wrappers generically and does not invent unverified acronyms |
| SRC-A10 | p.357–359, figures 11-59 to 11-62 / prospectus excerpts | graph labels và nhiều row trong product-description screenshot OCR partial | prose confirms autocall thresholds, knock-in logic, worst-performer settlement, index+FX example | lesson uses prose-confirmed branches only; exact prospectus cells/graphs stay ambiguity |

## Why these do not become `PARTIAL`

Các ambiguity trên là **exact-source artifacts** bị giới hạn bởi OCR/provenance. Learning route đã tách mechanism thành semantic rows khác và giải thích đầy đủ; phần không thể đọc chắc được ghi đúng location thay vì bị lờ đi hoặc “sửa” bằng kiến thức ngoài. Vì repository hiện không chứa PDF/image gốc của Sách 3 để visual-verify, exact cell/label không thể được nâng lên `FULL` một cách trung thực.

## Publication boundary

- `SOURCE_AMBIGUITY` không được dùng như `FULL`.
- Không có lesson nào phụ thuộc vào một con số OCR-bị-vỡ để giải thích mechanism.
- Nếu PDF/image gốc được bổ sung sau này, ưu tiên re-open SRC-A01…A10 và thay status chỉ sau visual verification.
