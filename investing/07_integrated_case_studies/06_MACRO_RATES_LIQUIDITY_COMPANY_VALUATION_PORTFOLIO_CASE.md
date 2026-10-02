# Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Câu hỏi nghiên cứu** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **2. Trạng thái trước cú sốc** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối macro rates, liquidity, company valuation và portfolio case, để chuyển kịch bản kinh tế thành quyết định phân bổ.

> Đây là worked trường hợp (case / 사례) dùng **số liệu giả định** để nối toàn bộ chuỗi `macro → rates → liquidity → industry → company → valuation → portfolio`. Mục tiêu không phải dự báo giá hay đưa ra khuyến nghị mua/bán, mà luyện cách biến một cú sốc vĩ mô thành các biến có thể đo trong mô hình doanh nghiệp và danh mục.

## 1. Câu hỏi nghiên cứu

Giả sử thị trường đang kỳ vọng lạm phát tiếp tục giảm và chính sách tiền tệ sẽ nới lỏng trong 12 tháng tới. Sau đó một loạt dữ liệu cho thấy lạm phát dịch vụ dai dẳng hơn dự kiến.

Câu hỏi không phải:

> “CPI cao thì cổ phiếu có giảm không?”

Mà là:

> Cú sốc thay đổi đường đi lãi suất, thanh khoản, chi phí vốn và nhu cầu ngành như thế nào; từ đó FCF, định giá và rủi ro danh mục thay đổi bao nhiêu?

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **2. Trạng thái trước cú sốc** tiếp nhận điểm tựa từ **1. Câu hỏi nghiên cứu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Dữ liệu mới gây bất ngờ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Trạng thái trước cú sốc

Giả định trước dữ liệu:

```text
Core CPI kỳ vọng: 2,9%
Fed cuts được phản ánh trong 12 tháng: 100 bp
US 2Y: 3,50%
US 10Y: 4,00%
Real 10Y: 1,70%
Investment-grade credit spread: 90 bp
USD/KRW: 1.320
Điều kiện tài chính: tương đối nới
```

Một doanh nghiệp giả định là **nhà cung cấp thiết bị bán dẫn Hàn Quốc** có:

```text
Doanh thu: 1.000
Tỷ trọng doanh thu xuất khẩu: 65%
EBIT margin: 18%
EBIT: 180
Thuế suất tiền mặt: 24%
D&A: 50
Capex: 70
Tăng vốn lưu động: 20
Nợ: 300
Tỷ lệ nợ thả nổi hoặc cần tái cấp vốn trong 18 tháng: 50%
Số cổ phiếu pha loãng: 100
```

FCF đơn giản hóa trước cú sốc:

```text
NOPAT = 180 × (1 - 24%) = 136,8
FCF ≈ NOPAT + D&A - Capex - ΔNWC
FCF ≈ 136,8 + 50 - 70 - 20
FCF ≈ 96,8
```

Đây là **điểm xuất phát**, không phải giá trị hợp lý.

> **Chuyển mạch:** Ở chặng này của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **2. Trạng thái trước cú sốc** nêu điều cần giải thích; **3. Dữ liệu mới gây bất ngờ** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Lớp 1 — Macro: xác định biến thay đổi thật sự** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Dữ liệu mới gây bất ngờ

Giả định dữ liệu thực tế:

```text
Core CPI: 3,3%
Dịch vụ lõi: tăng tốc
Tăng trưởng tiền lương: cao hơn dự kiến
PMI sản xuất: suy yếu nhẹ
```

Sau dữ liệu, thị trường tái định giá:

```text
Fed cuts trong 12 tháng: từ 100 bp → 40 bp
US 2Y: +50 bp
US 10Y: +70 bp
Real 10Y: +50 bp
Credit spread: +80 bp
USD/KRW: +7%
```

Đây là một shock hỗn hợp:

```text
Lạm phát dai dẳng hơn
+ discount rate cao hơn
+ USD mạnh hơn
+ tín dụng đắt hơn
+ tăng trưởng công nghiệp yếu đi
```

Vì vậy không thể dùng một dấu `+` hoặc `-` cho toàn bộ cổ phiếu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **3. Dữ liệu mới gây bất ngờ** nêu điều cần giải thích; **4. Lớp 1 — Macro: xác định biến thay đổi thật sự** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. Lớp 2 — Rates: tách đầu ngắn, đầu dài và real yield** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Lớp 1 — Macro: xác định biến thay đổi thật sự

Cú sốc ban đầu là lạm phát, nhưng biến đầu tư quan trọng hơn là **điều gì thay đổi trong phân phối (distribution / 분포) của chính sách và tăng trưởng**.

Chuỗi:

```text
Lạm phát dịch vụ dai dẳng
→ ngân hàng trung ương ít dư địa cắt lãi
→ lãi suất thực duy trì cao hơn
→ chi phí vốn tăng
→ điều kiện tài chính chặt hơn
→ nhu cầu và capex có thể giảm với độ trễ
```

Dạng thất bại (failure mode / 실패 모드) của cách đọc đơn giản là chỉ nhìn CPI mà bỏ qua PMI suy yếu. Nếu tăng trưởng giảm nhanh hơn, vài tháng sau thị trường có thể chuyển từ “higher for longer” sang “chính sách (policy / 정책) easing vì suy thoái”.

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **5. Lớp 2 — Rates: tách đầu ngắn, đầu dài và real yield** tiếp nhận điểm tựa từ **4. Lớp 1 — Macro: xác định biến thay đổi thật sự** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Lớp 3 — Liquidity và credit: tại sao rates shock có thể trở thành funding shock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Lớp 2 — Rates: tách đầu ngắn, đầu dài và real yield

US 2Y tăng 50 bp chủ yếu phản ánh thay đổi đường đi kỳ vọng của chính sách (policy / 정책) tỷ lệ (rate / 비율).

US 10Y tăng 70 bp có thể gồm:

```text
Kỳ vọng short rate cao hơn
+ real yield cao hơn
+ term premium cao hơn
```

Với tài sản duration dài, real yield tăng 50 bp có thể quan trọng hơn CPI headline.

Đối với trái phiếu có modified duration 7:

```text
%ΔP ≈ -Duration × ΔYield
≈ -7 × 0,007
≈ -4,9%
```

Con số này là xấp xỉ bậc một; convexity, carry và curve shape có thể làm kết quả khác.

> **Chuyển mạch:** Ở chặng này của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **6. Lớp 3 — Liquidity và credit: tại sao rates shock có thể trở thành funding shock** tiếp nhận điểm tựa từ **5. Lớp 2 — Rates: tách đầu ngắn, đầu dài và real yield** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. dạng thất bại (failure mode / 실패 모드) của phân tích thanh khoản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Lớp 3 — Liquidity và credit: tại sao rates shock có thể trở thành funding shock

Credit spread tăng 80 bp cho thấy chi phí vốn doanh nghiệp không chỉ tăng vì risk-free tỷ lệ (rate / 비율).

Nếu trước cú sốc một doanh nghiệp vay ở:

```text
Risk-free tương ứng: 4,0%
Credit spread: 1,0%
→ Cost of debt ≈ 5,0%
```

Sau cú sốc:

```text
Risk-free: 4,7%
Credit spread: 1,8%
→ Cost of debt ≈ 6,5%
```

Chi phí tái cấp vốn tăng khoảng 150 bp.

Với 150 nợ cần tái định giá/tái cấp vốn:

```text
Chi phí lãi tăng gần đúng
= 150 × 1,5%
= 2,25 mỗi năm
```

2,25 không lớn so với EBIT 180, nhưng đây mới là **direct interest tác động (effect / 효과)**. Tác động lớn hơn có thể đến từ khách hàng cắt capex vì WACC tăng và financing khó hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **7. dạng thất bại (failure mode / 실패 모드) của phân tích thanh khoản** tiếp nhận điểm tựa từ **6. Lớp 3 — Liquidity và credit: tại sao rates shock có thể trở thành funding shock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Lớp 4 — Industry: chuyển financial conditions thành capex cycle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. dạng thất bại (failure mode / 실패 모드) của phân tích thanh khoản

Sai lầm thường gặp:

```text
Credit spread chỉ tăng 80 bp
→ kết luận tác động nhỏ
```

Nhưng cần kiểm tra thêm:

```text
Debt maturity wall
Bank lending standards
Revolver availability
Collateral requirement
Customer financing
Supplier financing
Inventory financing
```

Nếu khách hàng của công ty phụ thuộc vốn vay để mở rộng fab, liquidity tightening có thể tác động vào đơn hàng mạnh hơn chi phí lãi của chính công ty.

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **8. Lớp 4 — Industry: chuyển financial conditions thành capex cycle** tiếp nhận điểm tựa từ **7. dạng thất bại (failure mode / 실패 모드) của phân tích thanh khoản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Lớp 5 — FX: KRW yếu vừa hỗ trợ vừa gây chi phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Lớp 4 — Industry: chuyển financial conditions thành capex cycle

Với thiết bị bán dẫn, cầu không chỉ phụ thuộc nhu cầu chip cuối cùng mà còn phụ thuộc kế hoạch capex của fab.

Chuỗi có thể là:

```text
Real yield / WACC ↑
+ demand uncertainty ↑
→ hurdle rate cho dự án fab ↑
→ dự án biên bị trì hoãn
→ equipment order ↓
→ backlog conversion chậm
→ utilization của nhà cung cấp ↓
→ operating leverage âm
```

Dữ liệu cần theo dõi:

```text
Capex guidance của khách hàng lớn
Backlog / book-to-bill
Lead time
Order cancellation / push-out
Utilization
Memory ASP
Inventory days
HBM qualification / advanced packaging demand
```

Không dùng một chỉ tiêu “semiconductor export” để đại diện toàn bộ ngành.

> **Chuyển mạch:** Ở chặng này của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **9. Lớp 5 — FX: KRW yếu vừa hỗ trợ vừa gây chi phí** tiếp nhận điểm tựa từ **8. Lớp 4 — Industry: chuyển financial conditions thành capex cycle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Lớp 6 — Company: xây shock từ driver, không từ EPS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Lớp 5 — FX: KRW yếu vừa hỗ trợ vừa gây chi phí

USD/KRW tăng 7% thường được mô tả là tích cực cho exporter, nhưng cần nhìn **net FX exposure**.

Giả sử:

```text
65% doanh thu liên quan USD
40% COGS liên quan USD
Một phần capex nhập khẩu bằng USD
20% nợ bằng USD
```

KRW yếu hỗ trợ quy đổi doanh thu nhưng đồng thời tăng chi phí đầu vào, capex và nghĩa vụ nợ ngoại tệ.

Không nên nhân doanh thu với +7%. Hãy xây sensitivity:

```text
FX translation benefit
- imported input cost
- USD debt cost
- hedge effect
= net FX impact
```

Giả định sau phòng vệ, tác động ròng lên doanh thu tương đương khoảng +4%.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **10. Lớp 6 — Company: xây shock từ driver, không từ EPS** tiếp nhận điểm tựa từ **9. Lớp 5 — FX: KRW yếu vừa hỗ trợ vừa gây chi phí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. FCF sau cú sốc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Lớp 6 — Company: xây shock từ driver, không từ EPS

Giả định shock ngành:

```text
Volume / order conversion: -8%
Pricing: +1%
Net FX effect lên revenue: +4%
```

Doanh thu xấp xỉ:

```text
1.000 × 0,92 × 1,01 × 1,04
≈ 966
```

Doanh thu chỉ giảm khoảng 3,4%, nhưng EBIT có thể giảm mạnh hơn do operating leverage.

Giả định EBIT margin từ 18% xuống 15%:

```text
EBIT mới ≈ 966 × 15%
≈ 145
```

So với 180 trước shock:

```text
EBIT giảm gần 19%
```

Đây là lý do doanh thu giảm nhẹ không đồng nghĩa earnings rủi ro (risk / 위험) nhỏ.

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **11. FCF sau cú sốc** tiếp nhận điểm tựa từ **10. Lớp 6 — Company: xây shock từ driver, không từ EPS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Kiểm tra bảng cân đối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. FCF sau cú sốc

Giả định:

```text
EBIT: 145
Tax: 24%
D&A: 50
Capex: giảm từ 70 xuống 65
ΔNWC: giảm từ 20 xuống 10 do tăng trưởng chậm
```

Tính gần đúng:

```text
NOPAT = 145 × 76% = 110,2
FCF ≈ 110,2 + 50 - 65 - 10
FCF ≈ 85,2
```

FCF giảm từ 96,8 xuống 85,2, tức khoảng 12%.

Điểm đáng chú ý:

```text
Revenue -3,4%
EBIT -19%
FCF -12%
```

Ba con số khác nhau do operating leverage, capex và working capital.

> **Chuyển mạch:** Ở chặng này của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **12. Kiểm tra bảng cân đối** tiếp nhận điểm tựa từ **11. FCF sau cú sốc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Lớp 7 — Valuation: tách earnings tác động (effect / 효과) và discount-rate tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Kiểm tra bảng cân đối

Trước khi sang valuation, hỏi:

```text
Cash đủ cho bao nhiêu tháng?
Debt maturity tập trung năm nào?
Interest coverage sau shock?
Covenant headroom?
Capex nào là maintenance và capex nào có thể hoãn?
Khách hàng có thể chậm thanh toán không?
```

Nếu EBIT giảm nhưng bảng cân đối vẫn khỏe, vấn đề chủ yếu có thể là valuation/cycle. Nếu refinancing wall gần và covenant mỏng, cùng shock có thể biến thành vấn đề sống sót.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **13. Lớp 7 — Valuation: tách earnings tác động (effect / 효과) và discount-rate tác động (effect / 효과)** tiếp nhận điểm tựa từ **12. Kiểm tra bảng cân đối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Reverse DCF sau shock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Lớp 7 — Valuation: tách earnings tác động (effect / 효과) và discount-rate tác động (effect / 효과)

Một sai lầm lớn là chỉ giảm EPS hoặc chỉ tăng WACC. Shock này làm cả hai.

Giả định trước shock:

```text
WACC: 9,0%
Long-term growth: 3,0%
Normalized FCF năm kế tiếp: 100
```

Terminal giá trị (value / 값) đơn giản hóa:

```text
TV = FCF1 / (WACC - g)
= 100 / (9% - 3%)
≈ 1.667
```

Sau shock:

```text
WACC: 10,5%
Long-term growth: 2,5%
Normalized FCF1: 90
```

```text
TV = 90 / (10,5% - 2,5%)
= 90 / 8%
= 1.125
```

Terminal giá trị (value / 값) trong ví dụ giảm khoảng 32,5%.

Đây không phải mục tiêu giá; nó minh họa độ nhạy của valuation khi **cash luồng (flow / 흐름) và discount tỷ lệ (rate / 비율) cùng xấu đi**.

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **14. Reverse DCF sau shock** tiếp nhận điểm tựa từ **13. Lớp 7 — Valuation: tách earnings tác động (effect / 효과) và discount-rate tác động (effect / 효과)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Multiples: vì sao P/E có thể gây nhầm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Reverse DCF sau shock

Thay vì chỉ hỏi fair giá trị (value / 값) giảm bao nhiêu, hỏi:

> Giá hiện tại đang yêu cầu khôi phục (recovery / 복구) nhanh tới mức nào?

Kiểm tra ba biến:

```text
Backlog recovery
Normalized EBIT margin
ROIC trên capex mới
```

Nếu giá hiện tại chỉ hợp lý khi margin quay lại 20% rất nhanh và capex khách hàng không giảm, thesis phụ thuộc nhiều giả định đồng thời.

> **Chuyển mạch:** Ở chặng này của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **14. Reverse DCF sau shock** đã nêu tiêu chí phân biệt, còn **15. Multiples: vì sao P/E có thể gây nhầm** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **16. Lớp 8 — Portfolio: nhìn factor exposure trước ticker** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Multiples: vì sao P/E có thể gây nhầm

Nếu EPS giảm từ 10 xuống 7 nhưng giá chỉ giảm từ 100 xuống 85:

```text
P/E trước = 10x
P/E sau = 12,1x
```

Cổ phiếu “rẻ hơn về giá” nhưng lại **đắt hơn trên earnings mới**.

Với doanh nghiệp chu kỳ cần dùng normalized earnings, EV/EBITDA mid-cycle, DCF hoặc reverse DCF thay vì trailing P/E đơn lẻ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **15. Multiples: vì sao P/E có thể gây nhầm** đã nêu tiêu chí phân biệt, còn **16. Lớp 8 — Portfolio: nhìn factor exposure trước ticker** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **17. Portfolio stress có số liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Lớp 8 — Portfolio: nhìn factor exposure trước ticker

Giả định danh mục:

```text
Global equity ETF: 35%
Korea equity ETF: 20%
Semiconductor ETF: 15%
Korean equipment company: 10%
Long-duration bonds: 10%
Gold: 5%
Cash: 5%
```

Nhìn theo ticker có vẻ đa dạng. Nhìn theo factor:

```text
Growth / equity beta: cao
Real-yield duration: cao
Semiconductor cycle: rất cao
KRW / Korea: cao
Liquidity stress: trung bình-cao
```

Cú shock real yield + credit + USD có thể làm nhiều vị thế cùng giảm.

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **17. Portfolio stress có số liệu** tiếp nhận điểm tựa từ **16. Lớp 8 — Portfolio: nhìn factor exposure trước ticker** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Hedge phải khớp factor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Portfolio stress có số liệu

Giả định trong shock:

```text
Global equity ETF: -12%
Korea equity ETF: -15%
Semiconductor ETF: -22%
Equipment company: -28%
Long-duration bonds: -5%
Gold: +3%
Cash: 0%
```

Tác động gần đúng:

```text
35% × -12% = -4,20%
20% × -15% = -3,00%
15% × -22% = -3,30%
10% × -28% = -2,80%
10% × -5%  = -0,50%
5% × +3%   = +0,15%
5% × 0%    = 0%
```

Tổng stress mất mát (loss / 손실) gần đúng:

```text
≈ -13,65%
```

Điểm cần học không phải con số -13,65%, mà là **10% company position chỉ là một phần; concentration thật nằm trong dùng chung (common / 공통) factors**.

> **Chuyển mạch:** Ở chặng này của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **18. Hedge phải khớp factor** tiếp nhận điểm tựa từ **17. Portfolio stress có số liệu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. dạng thất bại (failure mode / 실패 모드) của hedge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Hedge phải khớp factor

Nếu mục tiêu chỉ là giảm equity beta, chỉ mục (index / 인덱스) future có thể hữu ích.

Nếu mục tiêu là giảm duration/tỷ lệ (rate / 비율) rủi ro (risk / 위험), equity hedge có thể không đủ.

Nếu mục tiêu là giảm KRW rủi ro (risk / 위험), cần FX hedge.

Nếu mục tiêu là bảo vệ tail mất mát (loss / 손실) nhưng giữ upside, options có thể phù hợp về cơ chế nhưng phải tính premium, skew, expiry và basis rủi ro (risk / 위험).

Không tồn tại “hedge tốt nhất” độc lập với rủi ro (risk / 위험) cần hedge.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **19. dạng thất bại (failure mode / 실패 모드) của hedge** tiếp nhận điểm tựa từ **18. Hedge phải khớp factor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. dữ liệu (data / 데이터) dashboard sau cú sốc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. dạng thất bại (failure mode / 실패 모드) của hedge

Một hedge có thể thất bại khi:

```text
Basis thay đổi
Correlation breakdown
Hedge ratio sai
Expiry không khớp horizon
Liquidity biến mất
Option IV quá đắt
FX exposure thực khác exposure ước tính
```

Do đó trường hợp (case / 사례) study phải ghi cả **hedge dạng thất bại (failure mode / 실패 모드)**, không chỉ hedge instrument.

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **19. dạng thất bại (failure mode / 실패 모드) của hedge** nêu điều cần giải thích; **20. dữ liệu (data / 데이터) dashboard sau cú sốc** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. Phân biệt dữ kiện, ước tính và giả định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. dữ liệu (data / 데이터) dashboard sau cú sốc

Theo dõi theo tầng:

```text
Macro:
CPI composition, wages, PMI

Rates:
2Y, 10Y, real yield, breakeven, term premium

Liquidity/Credit:
credit spread, lending standards, repo/funding stress

Industry:
memory ASP, inventory, capex guidance, equipment orders

Company:
backlog, revenue mix, margin, working capital, debt maturity

Valuation:
WACC, normalized FCF, reverse DCF assumptions

Portfolio:
factor exposure, stress loss, liquidity bucket, hedge effectiveness
```

Đây là dashboard để **cập nhật xác suất**, không phải để tìm một indicator dự báo hoàn hảo.

> **Chuyển mạch:** Ở chặng này của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **20. dữ liệu (data / 데이터) dashboard sau cú sốc** nêu điều cần giải thích; **21. Phân biệt dữ kiện, ước tính và giả định** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **22. Counterfactual: điều gì nếu thesis macro đúng nhưng cổ phiếu vẫn tăng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Phân biệt dữ kiện, ước tính và giả định

Ví dụ:

```text
US 10Y +70 bp                    → dữ kiện quan sát
Equipment order sẽ giảm 8%      → ước tính
EBIT margin sẽ xuống 15%         → giả định mô hình
WACC mới là 10,5%                → giả định định giá
Portfolio shock loss -13,65%     → kết quả kịch bản
```

Nếu trộn năm lớp này, research ghi chú (note / 노트) dễ tạo cảm giác chắc chắn giả.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **22. Counterfactual: điều gì nếu thesis macro đúng nhưng cổ phiếu vẫn tăng?** tiếp nhận điểm tựa từ **21. Phân biệt dữ kiện, ước tính và giả định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Counterfactual ngược lại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Counterfactual: điều gì nếu thesis macro đúng nhưng cổ phiếu vẫn tăng?

Có thể xảy ra nếu:

```text
HBM/AI demand mạnh hơn nhiều
Backlog được bảo vệ bởi hợp đồng
FX benefit lớn hơn dự kiến
Competitor gặp sự cố nguồn cung
Market share tăng
Valuation trước shock đã rất thấp
```

Do đó `macro đúng` không đồng nghĩa `company call đúng`.

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **23. Counterfactual ngược lại** tiếp nhận điểm tựa từ **22. Counterfactual: điều gì nếu thesis macro đúng nhưng cổ phiếu vẫn tăng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. vô hiệu hóa (invalidation / 무효화) theo từng tầng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Counterfactual ngược lại

CPI có thể nhanh chóng giảm lại nhưng công ty vẫn yếu nếu:

```text
Khách hàng cắt capex vì dư công suất
Mất market share
Yield kém
Product qualification chậm
Working capital xấu
Governance / capital allocation yếu
```

Trường hợp (case / 사례) study tích hợp phải giữ **company-specific rủi ro (risk / 위험)** độc lập với macro.

> **Chuyển mạch:** Ở chặng này của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **24. vô hiệu hóa (invalidation / 무효화) theo từng tầng** tiếp nhận điểm tựa từ **23. Counterfactual ngược lại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Post-mortem và attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. vô hiệu hóa (invalidation / 무효화) theo từng tầng

Một case tích hợp không thể chỉ có một điều kiện vô hiệu hóa chung. Ta cần kiểm tra riêng macro, rates, liquidity, industry và company để biết chính xác tầng nào đã hỏng và tầng nào vẫn còn đứng vững.

```text
Macro invalidation:
Lạm phát dịch vụ giảm nhanh, labor cooling mạnh

Rates invalidation:
Real yield giảm dù policy rate chưa đổi

Liquidity invalidation:
Credit spread co, lending standards nới

Industry invalidation:
Capex guidance và equipment order phục hồi

Company invalidation:
Backlog, margin, market share cải thiện vượt giả định

Valuation invalidation:
Price đã phản ánh bear case sâu hơn mô hình
```

Không nên dùng một điều kiện duy nhất cho toàn thesis.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **25. Post-mortem và attribution** tiếp nhận điểm tựa từ **24. vô hiệu hóa (invalidation / 무효화) theo từng tầng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Bài tập bắt buộc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Post-mortem và attribution

Sau 3–6 tháng, phân rã:

```text
Macro forecast đúng/sai?
Rate path đúng/sai?
Credit/liquidity đúng/sai?
Industry demand đúng/sai?
Company margin đúng/sai?
Valuation multiple thay đổi vì sao?
Portfolio loss đến từ factor nào?
Hedge giảm được bao nhiêu loss?
```

Một quyết định có thể có kết quả (outcome / 결과) tốt nhưng lô-gic (logic / 논리) sai. Attribution giúp tránh học nhầm từ may mắn.

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **26. Bài tập bắt buộc** tiếp nhận điểm tựa từ **25. Post-mortem và attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Đầu ra chuẩn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Bài tập bắt buộc

Không đọc trường hợp (case / 사례) rồi dừng. Hãy thay ít nhất ba giả định:

```text
A. Real yield chỉ tăng 10 bp thay vì 50 bp
B. USD/KRW không tăng mà giảm 5%
C. Equipment order tăng 5% nhờ AI capex
```

Sau đó tính lại:

```text
Revenue
EBIT
FCF
WACC / valuation sensitivity
Portfolio stress loss
```

Mục tiêu là thấy **kết quả phụ thuộc giả định nào mạnh nhất**.

> **Chuyển mạch:** Ở chặng này của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **27. Đầu ra chuẩn** tiếp nhận điểm tựa từ **26. Bài tập bắt buộc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Liên kết học tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Đầu ra chuẩn

Tạo một ghi chú (note / 노트) gồm:

```text
01_macro_surprise.md
02_rates_curve.md
03_liquidity_credit.md
04_industry_driver_tree.md
05_company_sensitivity.md
06_valuation_sensitivity.md
07_portfolio_stress.md
08_hedge_failure_map.md
09_postmortem_template.md
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, sau nội dung của **27. Đầu ra chuẩn**, **28. Liên kết học tiếp** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Liên kết học tiếp

Các tài liệu sau mở rộng từng tầng của worked case theo đúng thứ tự đã thực hành. Đọc tiếp theo nhu cầu còn yếu sẽ hiệu quả hơn việc quay lại toàn bộ thư viện một cách rời rạc.

- [Macro Transmission Lab](../04_economics/07_MACRO_TRANSMISSION_NOWCASTING_AND_POLICY_LAB.md)
- [Bonds, Rates and Credit](../02_asset_classes/02_BONDS_RATES_AND_CREDIT.md)
- [Monetary System and Liquidity](../04_economics/04_MONETARY_SYSTEM_LIQUIDITY_AND_CRISIS_TRANSMISSION.md)
- [Korea Market Playbook](../06_markets_korea_vietnam/01_KOREA_MARKET_PLAYBOOK.md)
- [Company Modeling Lab](../03_company_analysis/07_INTEGRATED_COMPANY_MODELING_AND_THESIS_LAB.md)
- [Valuation](../03_company_analysis/03_VALUATION_DCF_AND_MULTIPLES.md)
- [Portfolio Lab](../01_foundations/06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md)
- [Advanced Practice Workbook](../ADVANCED_PRACTICE_WORKBOOK.md)

> **Chuyển mạch:** Trong **Tình huống tích hợp 06 — Từ cú sốc lạm phát và lãi suất tới thanh khoản, doanh nghiệp, định giá và danh mục**, **Kết luận** gom các mảnh từ **28. Liên kết học tiếp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết luận

Một macro shock chỉ trở thành investment phân tích (analysis / 분석) khi nó được truyền xuống:

```text
Macro
→ Rates
→ Liquidity / Credit
→ FX
→ Industry
→ Company
→ Cash Flow
→ Valuation
→ Portfolio
→ Hedge / Execution
→ Attribution
```

Nếu không thể chỉ ra dữ liệu, cơ chế, failure mode và độ nhạy ở từng tầng, phân tích vẫn chỉ là narrative.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
