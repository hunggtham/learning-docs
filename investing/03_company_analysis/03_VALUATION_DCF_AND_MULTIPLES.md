# Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**. Route đi từ market price và intrinsic value → expectations về growth/cash flow/risk → DCF và multiples → scenarios, sensitivity và reverse valuation → margin of safety, để giá trị là khoảng giả định có thể kiểm tra.

> Định giá (valuation) không phải là tìm ra một “giá đúng” duy nhất. Mục tiêu là chuyển các giả định về dòng tiền, tăng trưởng, rủi ro và phân bổ vốn thành một khoảng giá trị hợp lý, sau đó so khoảng đó với những kỳ vọng đang được phản ánh trong giá thị trường.

## 1. Giá thị trường và giá trị nội tại

Trước khi mở bảng tính, cần phân biệt hai câu hỏi: thị trường đang trả giá bao nhiêu và lợi ích kinh tế tương lai có thể đáng giá bao nhiêu. Khoảng cách giữa hai câu hỏi là nơi định giá tạo ra giả thuyết, không phải một đáp án chắc chắn.

**Giá thị trường (market price)** là mức giá đang được giao dịch. **Giá trị nội tại (intrinsic value)** là giá trị hiện tại ước tính của những lợi ích kinh tế mà người sở hữu tài sản có thể nhận được trong tương lai.

Hai con số này có thể khác nhau vì giá thị trường còn chịu ảnh hưởng của kỳ vọng, thanh khoản, dòng tiền giao dịch, tâm lý và mức bù rủi ro. Ngược lại, giá trị nội tại cũng không phải con số chắc chắn vì dòng tiền tương lai luôn chứa bất định.

Do đó, một mô hình tốt nên tạo ra **khoảng giá trị (valuation range)** và các **kịch bản (scenario)** thay vì cố tạo một mức giá mục tiêu chính xác giả tạo.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **2. Định giá là bài toán về kỳ vọng** tiếp nhận điểm tựa từ **1. Giá thị trường và giá trị nội tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Khung lợi nhuận kỳ vọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Định giá là bài toán về kỳ vọng

Lợi nhuận của nhà đầu tư không chỉ phụ thuộc doanh nghiệp “tốt” hay “xấu”, mà phụ thuộc kết quả thực tế so với những gì giá hiện tại đã kỳ vọng.

Một doanh nghiệp rất tốt vẫn có thể đem lại lợi nhuận thấp nếu thị trường đã định giá nhiều năm tăng trưởng gần như hoàn hảo. Ngược lại, một doanh nghiệp trung bình có thể đem lại lợi nhuận tốt nếu kỳ vọng đang quá bi quan và kết quả thực tế chỉ cần “ít xấu hơn dự kiến”.

Đây là lý do câu hỏi quan trọng không chỉ là “doanh nghiệp tăng trưởng bao nhiêu?”, mà còn là:

```text
Giá hiện tại đang giả định điều gì?
→ Kết quả thực tế có thể khác kỳ vọng đó ở đâu?
→ Khoảng cách giữa kỳ vọng và thực tế có đủ lớn để tạo lợi nhuận không?
```

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **3. Khung lợi nhuận kỳ vọng** tiếp nhận điểm tựa từ **2. Định giá là bài toán về kỳ vọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Giá trị hiện tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Khung lợi nhuận kỳ vọng

Một cách nhìn đơn giản:

```text
Lợi nhuận kỳ vọng
≈ tăng trưởng cơ bản trên mỗi cổ phiếu
+ lợi suất phân phối cho cổ đông
+ thay đổi mức định giá
```

Doanh nghiệp có thể tăng EPS hoặc FCF 12% mỗi năm nhưng cổ đông vẫn nhận lợi nhuận thấp hơn nếu hệ số định giá bị co lại.

Vì vậy cần tách ba nguồn:

- tăng trưởng lợi nhuận hoặc dòng tiền trên mỗi cổ phiếu;
- cổ tức và mua lại cổ phiếu ròng;
- mở rộng hoặc thu hẹp bội số định giá (multiple expansion/compression).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **4. Giá trị hiện tại** tiếp nhận điểm tựa từ **3. Khung lợi nhuận kỳ vọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Nhất quán giữa danh nghĩa và thực** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Giá trị hiện tại

Công thức nền tảng:

```text
PV = CF_t / (1 + r)^t
```

Trong đó `CF_t` là dòng tiền ở thời điểm `t`, còn `r` là tỷ lệ chiết khấu (discount rate).

Tỷ lệ chiết khấu càng cao thì giá trị hiện tại càng thấp, đặc biệt với dòng tiền nằm xa trong tương lai. Đây là trực giác của **độ dài dòng tiền cổ phiếu (equity duration)**: doanh nghiệp tăng trưởng với phần lớn giá trị nằm ở tương lai xa thường nhạy hơn với thay đổi lãi suất thực và tỷ lệ chiết khấu.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **5. Nhất quán giữa danh nghĩa và thực** tiếp nhận điểm tựa từ **4. Giá trị hiện tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Giá trị doanh nghiệp và giá trị vốn chủ sở hữu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Nhất quán giữa danh nghĩa và thực

Dòng tiền danh nghĩa (nominal cash flow) phải được chiết khấu bằng tỷ lệ danh nghĩa. Dòng tiền thực (real cash flow) phải đi cùng tỷ lệ thực.

Lạm phát không chỉ ảnh hưởng doanh thu. Nó còn tác động:

- giá bán;
- chi phí đầu vào;
- tiền lương;
- vốn lưu động;
- chi tiêu vốn;
- thuế;
- tỷ lệ chiết khấu.

Do đó không nên chỉ cộng lạm phát vào tăng trưởng doanh thu rồi giữ nguyên mọi giả định khác.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **6. Giá trị doanh nghiệp và giá trị vốn chủ sở hữu** tiếp nhận điểm tựa từ **5. Nhất quán giữa danh nghĩa và thực** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Nợ ròng không đơn giản là nợ trừ tiền mặt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Giá trị doanh nghiệp và giá trị vốn chủ sở hữu

Sau khi hiểu giá trị hiện tại và kỳ vọng, ta cần xác định giá trị đó thuộc về ai trong cấu trúc vốn. EV nhìn toàn bộ hoạt động dành cho các bên cung cấp vốn; Equity Value là phần còn lại của cổ đông thường sau các điều chỉnh ưu tiên.

**Giá trị doanh nghiệp (Enterprise Value, EV)** phản ánh giá trị hoạt động kinh doanh dành cho các bên cung cấp vốn. **Giá trị vốn chủ sở hữu (Equity Value)** là phần thuộc cổ đông thường sau khi điều chỉnh các nghĩa vụ ưu tiên hơn.

Một cầu nối đơn giản:

```text
EV
≈ Equity Value
+ Debt
+ Preferred Stock
+ Minority Interest
- Cash và tài sản ngoài hoạt động
```

Cầu nối thực tế có thể cần thêm thuê tài chính, thiếu hụt quỹ hưu trí, khoản đầu tư liên kết, tiền mặt bị hạn chế hoặc nghĩa vụ đặc biệt khác.

Điểm quan trọng là nhìn **bản chất kinh tế** thay vì chỉ dựa tên tài khoản kế toán.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **7. Nợ ròng không đơn giản là nợ trừ tiền mặt** tiếp nhận điểm tựa từ **6. Giá trị doanh nghiệp và giá trị vốn chủ sở hữu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Dòng tiền tự do cho doanh nghiệp — FCFF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Nợ ròng không đơn giản là nợ trừ tiền mặt

Không phải toàn bộ tiền mặt đều có thể dùng để trả cho cổ đông. Doanh nghiệp có thể cần một lượng tiền tối thiểu cho vận hành, hoặc có tiền bị hạn chế sử dụng.

Một số nghĩa vụ như thuê dài hạn, thâm hụt hưu trí hay tài trợ từ nhà cung cấp có thể mang tính chất giống nợ.

Vì vậy cầu nối EV → Equity giá trị (value / 값) phải xét:

```text
Tiền mặt vận hành
Tiền bị hạn chế
Nợ vay
Thuê tài chính
Nghĩa vụ hưu trí
Quyền lợi cổ đông thiểu số
Tài sản đầu tư ngoài hoạt động
```

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **8. Dòng tiền tự do cho doanh nghiệp — FCFF** tiếp nhận điểm tựa từ **7. Nợ ròng không đơn giản là nợ trừ tiền mặt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Dòng tiền tự do cho cổ đông — FCFE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Dòng tiền tự do cho doanh nghiệp — FCFF

FCFF là cầu nối từ hoạt động kinh doanh tới giá trị dành cho cả chủ nợ và cổ đông. Hãy đọc công thức theo thứ tự EBIT sau thuế → tái đầu tư → thay đổi vốn lưu động, rồi kiểm tra xem từng biến có driver vận hành hay không.

```text
FCFF = EBIT(1-T) + D&A - Capex - ΔNWC
```

FCFF là dòng tiền trước khi phân chia cho chủ nợ và cổ đông. FCFF thường được chiết khấu bằng WACC để ra EV.

Dự báo FCFF phải nối với động lực kinh doanh thực tế, ví dụ:

```text
sản lượng × giá bán × cơ cấu sản phẩm
→ doanh thu
→ biên lợi nhuận
→ lợi nhuận hoạt động
→ tái đầu tư
→ FCFF
```

Không nên chỉ kéo doanh thu bằng một CAGR tùy ý.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **9. Dòng tiền tự do cho cổ đông — FCFE** tiếp nhận điểm tựa từ **8. Dòng tiền tự do cho doanh nghiệp — FCFF** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Quy ước giữa năm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Dòng tiền tự do cho cổ đông — FCFE

Một dạng gần đúng:

```text
FCFE
≈ Net Income
+ D&A
- Capex
- ΔNWC
+ Net Borrowing
```

FCFE được chiết khấu bằng **chi phí vốn chủ sở hữu (cost of equity)**.

FCFE phù hợp hơn khi cơ cấu nợ tương đối ổn định. Nếu đòn bẩy thay đổi mạnh, FCFF thường dễ diễn giải hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **10. Quy ước giữa năm** tiếp nhận điểm tựa từ **9. Dòng tiền tự do cho cổ đông — FCFE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Dự báo doanh thu từ động lực cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Quy ước giữa năm

Dòng tiền thực tế phát sinh xuyên suốt năm chứ không phải toàn bộ vào ngày cuối năm. **Quy ước giữa năm (mid-year convention)** giả định trung bình dòng tiền đến vào giữa kỳ.

Điều quan trọng không phải học thuộc một phép điều chỉnh, mà hiểu thời điểm dòng tiền ảnh hưởng trực tiếp đến giá trị hiện tại.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **11. Dự báo doanh thu từ động lực cơ bản** tiếp nhận điểm tựa từ **10. Quy ước giữa năm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Dự báo biên lợi nhuận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Dự báo doanh thu từ động lực cơ bản

Thay vì viết “doanh thu tăng 10%”, nên xây mô hình từ các động lực thực tế.

Ví dụ:

```text
Bán lẻ:
số cửa hàng × doanh thu/cửa hàng × tăng trưởng cửa hàng hiện hữu

SaaS:
ARR đầu kỳ + ARR mới - churn + mở rộng khách hàng hiện hữu

Bán dẫn:
bit shipment × ASP

Ngân hàng:
tài sản sinh lãi × chênh lệch lãi suất + phí
```

Mô hình theo động lực (driver-based model) giúp kịch bản tăng/giảm có nguyên nhân rõ ràng và có thể theo dõi sau đó.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **12. Dự báo biên lợi nhuận** tiếp nhận điểm tựa từ **11. Dự báo doanh thu từ động lực cơ bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Tăng trưởng cần tái đầu tư** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Dự báo biên lợi nhuận

Biên gộp có thể thay đổi theo:

- giá bán;
- cơ cấu sản phẩm;
- chi phí đầu vào;
- tỷ lệ sử dụng công suất;
- hiệu quả quy mô.

Biên hoạt động còn phụ thuộc R&D, SG&A và chi phí cố định.

Biên lợi nhuận cực cao thường khó duy trì mãi nếu lợi nhuận hấp dẫn đối thủ. Nếu mô hình giữ biên rất cao dài hạn, cần giải thích lợi thế cạnh tranh nào cho phép điều đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **13. Tăng trưởng cần tái đầu tư** tiếp nhận điểm tựa từ **12. Dự báo biên lợi nhuận** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. ROIC giảm dần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Tăng trưởng cần tái đầu tư

Một quan hệ trực giác:

```text
Tăng trưởng
≈ Tỷ lệ tái đầu tư
× Lợi nhuận trên vốn đầu tư tăng thêm
```

Nếu doanh nghiệp tăng trưởng 20% nhưng lợi nhuận trên vốn tăng thêm chỉ 5%, lượng vốn cần tái đầu tư sẽ rất lớn.

Tăng trưởng chỉ tạo giá trị khi lợi nhuận trên phần vốn mới đủ cao so với chi phí vốn.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **14. ROIC giảm dần** tiếp nhận điểm tựa từ **13. Tăng trưởng cần tái đầu tư** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Tăng trưởng giảm dần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. ROIC giảm dần

Do cạnh tranh, nhiều doanh nghiệp trưởng thành sẽ thấy ROIC vượt trội giảm dần theo thời gian.

Mô hình cần đặt câu hỏi:

```text
ROIC sẽ hội tụ về chi phí vốn?
Hay vẫn cao hơn nhờ lợi thế cạnh tranh?
Hay giảm xuống dưới chi phí vốn?
```

Một DCF giữ ROIC 30% mãi mãi mà không có lý do kinh tế là dấu hiệu định giá quá lạc quan.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **15. Tăng trưởng giảm dần** tiếp nhận điểm tựa từ **14. ROIC giảm dần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Vốn lưu động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Tăng trưởng giảm dần

Tăng trưởng cao không thể kéo dài vô hạn vì:

- quy mô thị trường;
- cạnh tranh;
- giới hạn công suất;
- quy luật số lớn.

Mô hình nên có một giai đoạn chuyển tiếp từ tăng trưởng cao về tăng trưởng trưởng thành. Không nên để tăng trưởng 30% tới năm thứ 5 rồi đột ngột rơi xuống 3% mà không giải thích cơ chế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **16. Vốn lưu động** tiếp nhận điểm tựa từ **15. Tăng trưởng giảm dần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Capex, khấu hao và chi phí duy trì** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Vốn lưu động

Tăng trưởng có thể hút tiền mặt qua phải thu và hàng tồn kho.

Có thể mô hình bằng:

- DSO;
- DIO;
- DPO;
- hoặc vốn lưu động/doanh thu.

Doanh nghiệp có vốn lưu động âm có thể được khách hàng hoặc nhà cung cấp tài trợ một phần. Nhưng khi tăng trưởng chậm lại, lợi ích này có thể đảo chiều.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **17. Capex, khấu hao và chi phí duy trì** tiếp nhận điểm tựa từ **16. Vốn lưu động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Vốn hóa R&D** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Capex, khấu hao và chi phí duy trì

Trong trạng thái dài hạn ổn định, chi tiêu vốn không thể thấp hơn hao mòn kinh tế mãi mãi.

Doanh nghiệp ít tài sản hữu hình vẫn có thể tái đầu tư rất lớn qua R&D, marketing hay phần mềm. Vì vậy phải nhìn **tái đầu tư kinh tế (economic reinvestment)** chứ không chỉ capex kế toán.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **18. Vốn hóa R&D** tiếp nhận điểm tựa từ **17. Capex, khấu hao và chi phí duy trì** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Thù lao bằng cổ phiếu — SBC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Vốn hóa R&D

Ở phần mềm, dược phẩm hoặc bán dẫn, một phần R&D tạo lợi ích nhiều năm nhưng vẫn được ghi chi phí ngay.

Nhà phân tích đôi khi vốn hóa R&D để so đầu tư và lợi nhuận phù hợp hơn. Tuy nhiên cần giả định tuổi thọ tài sản và khấu hao hợp lý.

Mục tiêu là phản ánh bản chất kinh tế, không phải làm lợi nhuận đẹp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **19. Thù lao bằng cổ phiếu — SBC** tiếp nhận điểm tựa từ **18. Vốn hóa R&D** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Số cổ phiếu pha loãng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Thù lao bằng cổ phiếu — SBC

Thù lao bằng cổ phiếu (stock-based compensation, SBC) là chi phí kinh tế vì gây pha loãng quyền sở hữu.

Nếu cộng SBC trở lại FCF, mô hình phải phản ánh:

- số cổ phiếu pha loãng cao hơn;
- hoặc chi phí mua lại cổ phiếu để bù pha loãng.

Không thể vừa coi SBC là miễn phí vừa bỏ qua pha loãng.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **20. Số cổ phiếu pha loãng** tiếp nhận điểm tựa từ **19. Thù lao bằng cổ phiếu — SBC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Thuế và lỗ thuế chuyển tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Số cổ phiếu pha loãng

Định giá trên mỗi cổ phiếu nên dùng số cổ phiếu pha loãng đầy đủ (fully diluted share count) khi quyền chọn, chứng quyền hoặc trái phiếu chuyển đổi có ý nghĩa kinh tế.

Doanh nghiệp có thể tăng EV nhưng giá trị trên mỗi cổ phiếu không tăng nếu liên tục phát hành thêm cổ phần.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **21. Thuế và lỗ thuế chuyển tiếp** tiếp nhận điểm tựa từ **20. Số cổ phiếu pha loãng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Khoảng dự báo chi tiết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Thuế và lỗ thuế chuyển tiếp

Thuế suất hiệu dụng có thể khác thuế suất pháp định do:

- cơ cấu địa lý;
- ưu đãi thuế;
- tín dụng thuế;
- lỗ thuế chuyển tiếp (NOL);
- khoản bất thường.

NOL có thể giảm thuế tương lai nhưng không kéo dài vô hạn. Mô hình phải đưa thuế về mức bình thường khi ưu đãi hết hiệu lực.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **22. Khoảng dự báo chi tiết** tiếp nhận điểm tựa từ **21. Thuế và lỗ thuế chuyển tiếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Giá trị cuối kỳ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Khoảng dự báo chi tiết

Khoảng dự báo phải đủ dài để doanh nghiệp tiến gần trạng thái kinh tế ổn định.

Doanh nghiệp tiện ích trưởng thành có thể chỉ cần vài năm. Một nền tảng đang tăng trưởng nhanh có thể cần giai đoạn dài hơn.

Kéo dài mô hình không làm nó chính xác hơn nếu các giả định không còn nền tảng kinh tế.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **23. Giá trị cuối kỳ** tiếp nhận điểm tựa từ **22. Khoảng dự báo chi tiết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Kiểm tra tăng trưởng cuối kỳ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Giá trị cuối kỳ

Mô hình tăng trưởng Gordon:

```text
TV = FCF_(n+1) / (WACC - g)
```

Giá trị cuối kỳ (terminal value) thường chiếm tỷ trọng lớn trong DCF, nên sai lệch nhỏ ở WACC hoặc `g` có thể tạo thay đổi lớn.

Các giả định cuối kỳ phải nhất quán giữa:

```text
Tăng trưởng
ROIC
Tỷ lệ tái đầu tư
Biên lợi nhuận
Chi phí vốn
```

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **24. Kiểm tra tăng trưởng cuối kỳ** tiếp nhận điểm tựa từ **23. Giá trị cuối kỳ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Giá trị cuối kỳ bằng bội số thoát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Kiểm tra tăng trưởng cuối kỳ

Tăng trưởng cuối kỳ không nên cao hơn tăng trưởng danh nghĩa bền vững của nền kinh tế vô hạn trừ khi có lý do đặc biệt.

Nếu tăng trưởng cuối kỳ là 3% và ROIC cuối kỳ là 15%, mô hình phải tái đầu tư đủ vốn để tài trợ mức tăng trưởng đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **25. Giá trị cuối kỳ bằng bội số thoát** tiếp nhận điểm tựa từ **24. Kiểm tra tăng trưởng cuối kỳ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. WACC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Giá trị cuối kỳ bằng bội số thoát

Một cách khác là dùng bội số cuối kỳ như EV/EBITDA hoặc P/E.

Cách này không loại bỏ bất định; nó chỉ chuyển bất định sang câu hỏi “doanh nghiệp sẽ được định giá bao nhiêu lần lợi nhuận ở tương lai?”.

Nên đối chiếu phương pháp Gordon với bội số thoát (exit multiple) để phát hiện giả định không nhất quán.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **26. WACC** tiếp nhận điểm tựa từ **25. Giá trị cuối kỳ bằng bội số thoát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Chi phí vốn chủ sở hữu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. WACC

WACC gom chi phí của các nguồn vốn theo cơ cấu vốn bền vững. Nó chỉ có ý nghĩa khi nhất quán với tiền tệ, lạm phát, đòn bẩy và rủi ro kinh doanh của dòng tiền được chiết khấu.

```text
WACC
= w_e × Cost of Equity
+ w_d × After-tax Cost of Debt
```

Trọng số nên dựa trên cơ cấu vốn bền vững theo giá trị thị trường.

WACC phải nhất quán với:

- tiền tệ;
- lạm phát;
- đòn bẩy;
- rủi ro kinh doanh.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **27. Chi phí vốn chủ sở hữu** tiếp nhận điểm tựa từ **26. WACC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Lãi suất phi rủi ro phải phù hợp tiền tệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Chi phí vốn chủ sở hữu

Theo CAPM:

```text
Cost of Equity
= Risk-free Rate
+ Beta × Equity Risk Premium
```

Beta và phần bù rủi ro cổ phiếu đều là ước tính, không phải hằng số vật lý.

Nếu thêm phần bù rủi ro quốc gia hay quy mô nhỏ, cần tránh tính cùng một rủi ro hai lần nếu nó đã được đưa vào dòng tiền hoặc beta.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **28. Lãi suất phi rủi ro phải phù hợp tiền tệ** tiếp nhận điểm tựa từ **27. Chi phí vốn chủ sở hữu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Rủi ro quốc gia** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Lãi suất phi rủi ro phải phù hợp tiền tệ

Dòng tiền KRW danh nghĩa không nên được chiết khấu tùy tiện bằng lãi suất phi rủi ro USD mà bỏ qua khác biệt lạm phát và ngoại hối.

Với doanh nghiệp đa quốc gia, có thể:

- mô hình từng khu vực;
- hoặc chuyển đổi dòng tiền bằng một khung tiền tệ nhất quán.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **29. Rủi ro quốc gia** tiếp nhận điểm tựa từ **28. Lãi suất phi rủi ro phải phù hợp tiền tệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Chi phí nợ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Rủi ro quốc gia

Rủi ro quốc gia (country risk) có thể đến từ:

- chính trị;
- pháp lý;
- kiểm soát vốn;
- rủi ro chủ quyền;
- khả năng chuyển đổi ngoại tệ;
- quản trị.

Có thể phản ánh bằng kịch bản dòng tiền hoặc phần bù chiết khấu. Không nên đồng thời phạt cùng một rủi ro ở cả hai nơi mà không kiểm soát.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **30. Chi phí nợ** tiếp nhận điểm tựa từ **29. Rủi ro quốc gia** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Phản hồi giữa đòn bẩy và giá trị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Chi phí nợ

Chi phí nợ nên phản ánh chi phí vay biên hiện tại, không chỉ lãi coupon lịch sử.

Doanh nghiệp căng thẳng có thể phải tái cấp vốn ở lợi suất thị trường cao hơn nhiều so với lãi suất kế toán đang ghi nhận.

Khi phân tích cần xem cả:

```text
chi phí vay mới
lịch đáo hạn
khả năng tái cấp vốn
khả năng sử dụng lá chắn thuế
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **31. Phản hồi giữa đòn bẩy và giá trị** tiếp nhận điểm tựa từ **30. Chi phí nợ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Phân tích độ nhạy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Phản hồi giữa đòn bẩy và giá trị

WACC không nhất thiết cố định nếu đòn bẩy thay đổi lớn.

Khi giá trị doanh nghiệp giảm mạnh, chi phí nợ và chi phí vốn chủ sở hữu có thể cùng tăng. Với doanh nghiệp đòn bẩy cao, phương pháp **giá trị hiện tại điều chỉnh (Adjusted Present value, APV)** hoặc phân tích kịch bản có thể rõ hơn một WACC duy nhất.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **32. Phân tích độ nhạy** tiếp nhận điểm tựa từ **31. Phản hồi giữa đòn bẩy và giá trị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Biểu đồ độ nhạy kiểu tornado** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Phân tích độ nhạy

Tối thiểu nên kiểm tra:

- WACC;
- tăng trưởng cuối kỳ;
- tăng trưởng doanh thu;
- biên lợi nhuận;
- ROIC;
- tỷ lệ tái đầu tư.

Nếu giá trị thay đổi từ 50 lên 150 chỉ vì một thay đổi rất nhỏ trong giả định, chính độ nhạy đó là một thông tin rủi ro quan trọng.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **33. Biểu đồ độ nhạy kiểu tornado** tiếp nhận điểm tựa từ **32. Phân tích độ nhạy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Phân tích kịch bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Biểu đồ độ nhạy kiểu tornado

Biểu đồ tornado giúp xếp hạng biến nào ảnh hưởng mạnh nhất đến giá trị.

Ví dụ:

```text
Sản lượng
Giá bán
Biên lợi nhuận
WACC
Tăng trưởng cuối kỳ
Capex
Vốn lưu động
```

Nó giúp tập trung thời gian nghiên cứu vào biến có tác động lớn thay vì tối ưu những biến ít quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **34. Phân tích kịch bản** tiếp nhận điểm tựa từ **33. Biểu đồ độ nhạy kiểu tornado** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Định giá theo xác suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Phân tích kịch bản

Cơ sở (base / 기반)/Bull/Bear phải khác nhau ở **cơ chế**, không chỉ cộng trừ 20% giá trị.

Ví dụ bán dẫn:

```text
Base:
ASP phục hồi vừa phải
+ utilization tăng
+ nguồn cung có kỷ luật

Bull:
HBM mix tăng mạnh
+ thiếu công suất
+ pricing power cao hơn

Bear:
cầu yếu
+ tồn kho tăng
+ công suất mới vào sớm
+ ASP giảm
```

Sau đó mới chuyển các cơ chế này thành doanh thu, biên lợi nhuận, FCF và giá trị.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **35. Định giá theo xác suất** tiếp nhận điểm tựa từ **34. Phân tích kịch bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Monte Carlo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Định giá theo xác suất

Khi một doanh nghiệp có nhiều đường đi hợp lý, không nên ép tất cả vào một forecast duy nhất. Định giá theo xác suất buộc người phân tích nói rõ khả năng, giá trị và mức thiệt hại của từng kịch bản.

```text
Expected Value = Σ p_i × Value_i
```

Xác suất vẫn là phán đoán. Mục tiêu của phương pháp này là buộc người phân tích nói rõ phân phối kết quả thay vì ngầm giả định một tương lai duy nhất.

Một kịch bản xác suất thấp nhưng thiệt hại rất lớn vẫn có thể quyết định quy mô vị thế.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **36. Monte Carlo** tiếp nhận điểm tựa từ **35. Định giá theo xác suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Reverse DCF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Monte Carlo

Monte Carlo lấy mẫu nhiều biến không chắc chắn từ các phân phối giả định để tạo phân phối giá trị.

Nó hữu ích để hình dung độ bất định, nhưng không tự biến một mô hình yếu thành mô hình tốt. Nếu phân phối đầu vào được đoán sai, đầu ra chỉ tạo cảm giác chính xác giả.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **37. Reverse DCF** tiếp nhận điểm tựa từ **36. Monte Carlo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Reverse DCF và thời gian duy trì lợi thế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Reverse DCF

Sau khi xây DCF xuôi, ta đảo chiều từ giá thị trường để đọc kỳ vọng đang được nhúng trong giá. Cách này hữu ích vì nó biến câu hỏi “giá đúng là bao nhiêu?” thành “thị trường đang yêu cầu doanh nghiệp đạt điều gì?”.

**DCF ngược (reverse DCF)** bắt đầu từ giá hiện tại rồi giải xem thị trường đang cần những giả định nào để mức giá đó hợp lý.

Câu hỏi chuyển từ:

```text
“Giá trị là bao nhiêu?”
```

sang:

```text
“Giá hiện tại đang giả định tăng trưởng, biên lợi nhuận và ROIC như thế nào?”
```

Đây là một trong những cách tốt nhất để đọc kỳ vọng đã được phản ánh trong giá.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **38. Reverse DCF và thời gian duy trì lợi thế** tiếp nhận điểm tựa từ **37. Reverse DCF** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. P/E** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Reverse DCF và thời gian duy trì lợi thế

Không chỉ giải một CAGR doanh thu. Có thể giải đồng thời:

- biên lợi nhuận cuối kỳ;
- tốc độ ROIC giảm dần;
- tỷ lệ tái đầu tư;
- thời gian duy trì lợi nhuận vượt chi phí vốn.

Một giá thị trường có thể đang giả định lợi thế cạnh tranh tồn tại 15 năm thay vì 5 năm. Đây thường là thông tin có ý nghĩa hơn một P/E đơn lẻ.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **39. P/E** tiếp nhận điểm tựa từ **38. Reverse DCF và thời gian duy trì lợi thế** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. PEG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. P/E

P/E hữu ích khi lợi nhuận có ý nghĩa và tương đối ổn định.

P/E kết hợp nhiều yếu tố:

- hoạt động;
- tài trợ;
- thuế;
- chu kỳ.

P/E thấp có thể phản ánh đỉnh lợi nhuận chu kỳ hoặc rủi ro cao. P/E cao có thể hợp lý nếu ROIC và tăng trưởng cao có thể duy trì lâu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **40. PEG** tiếp nhận điểm tựa từ **39. P/E** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. EV/EBITDA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. PEG

PEG là phép tham khảo nhanh nối P/E với tốc độ tăng trưởng, nhưng không thể thay thế chất lượng tăng trưởng, ROIC, rủi ro và thời gian duy trì. Hãy dùng nó để mở câu hỏi, không dùng làm kết luận.

```text
PEG = P/E / Growth
```

PEG quá đơn giản vì bỏ qua:

- chất lượng tăng trưởng;
- ROIC;
- biên lợi nhuận;
- rủi ro;
- thời gian duy trì tăng trưởng.

Chỉ nên dùng như phép tham khảo nhanh.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **41. EV/EBITDA** tiếp nhận điểm tựa từ **40. PEG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. EV/EBIT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. EV/EBITDA

EV/EBITDA giúp so giá trị hoạt động trước khấu hao, tài trợ và thuế.

Ưu điểm là ít bị khác biệt cơ cấu nợ làm méo so sánh. Nhược điểm là bỏ qua capex và vốn lưu động.

Do đó một doanh nghiệp thâm dụng vốn không mặc nhiên xứng đáng cùng EV/EBITDA với doanh nghiệp ít tài sản.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **42. EV/EBIT** tiếp nhận điểm tựa từ **41. EV/EBITDA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. EV/Sales** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. EV/EBIT

EV/EBIT đã trừ khấu hao nên có thể phản ánh hao mòn tài sản tốt hơn khi D&A gần với mức tiêu hao kinh tế.

Tuy nhiên vẫn cần chú ý khấu hao tài sản mua lại và khác biệt kế toán.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **43. EV/Sales** tiếp nhận điểm tựa từ **42. EV/EBIT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. P/B** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. EV/Sales

EV/Sales hữu ích khi lợi nhuận hiện tại âm, nhưng doanh thu chỉ có giá trị nếu doanh nghiệp có khả năng tạo biên lợi nhuận và dòng tiền tốt trong tương lai.

Cần so cùng:

- biên gộp;
- giữ chân khách hàng;
- đơn vị (unit / 단위) economics;
- nhu cầu tái đầu tư.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **44. P/B** tiếp nhận điểm tựa từ **43. EV/Sales** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. FCF Yield** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. P/B

P/B đặc biệt hữu ích với ngân hàng, bảo hiểm và doanh nghiệp mà vốn sổ sách liên quan trực tiếp tới tài sản sinh lời.

Quan hệ chính:

```text
ROE bền vững > Cost of Equity
→ P/B hợp lý có thể > 1
```

Nếu ROE thấp hơn chi phí vốn kéo dài, chiết khấu P/B có thể hợp lý.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **45. FCF Yield** tiếp nhận điểm tựa từ **44. P/B** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Lợi suất phân phối cho cổ đông** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. FCF Yield

FCF yield đặt dòng tiền tự do cạnh giá trị vốn chủ sở hữu hoặc EV. Trước khi so sánh, phải chuẩn hóa FCF và loại các khoản giải phóng vốn lưu động hoặc cắt capex chỉ xảy ra một lần.

```text
FCF Yield = FCF / Equity Value
```

Hoặc dùng phiên bản theo EV nếu giữ nhất quán.

Cần chuẩn hóa FCF để loại bỏ:

- giải phóng tồn kho tạm thời;
- vốn lưu động bất thường;
- cắt capex không bền vững.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **46. Lợi suất phân phối cho cổ đông** tiếp nhận điểm tựa từ **45. FCF Yield** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. So sánh doanh nghiệp tương đồng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Lợi suất phân phối cho cổ đông

Có thể nhìn:

```text
cổ tức
+ mua lại cổ phiếu ròng
= shareholder yield
```

Tuy nhiên mua lại bằng nợ hoặc mua cổ phiếu ở mức giá quá cao vẫn có thể phá hủy giá trị.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **46. Lợi suất phân phối cho cổ đông** đã nêu tiêu chí phân biệt, còn **47. So sánh doanh nghiệp tương đồng** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **48. Bội số lịch sử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. So sánh doanh nghiệp tương đồng

Doanh nghiệp so sánh nên tương đồng về:

- tăng trưởng;
- biên lợi nhuận;
- ROIC;
- rủi ro;
- địa lý;
- mô hình kinh doanh;
- chuẩn kế toán.

Không nên chỉ lấy trung bình bội số. Cần giải thích tại sao doanh nghiệp xứng đáng mức cao hơn hoặc thấp hơn nhóm.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **47. So sánh doanh nghiệp tương đồng** đã nêu tiêu chí phân biệt, còn **48. Bội số lịch sử** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **49. Định giá từng phần — SOTP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Bội số lịch sử

Khoảng bội số lịch sử là dữ liệu tham khảo, không phải luật giá trị hợp lý.

Lãi suất, mức trưởng thành, lợi thế cạnh tranh và cơ cấu ngành có thể thay đổi. Một doanh nghiệp suy yếu về moat có thể xứng đáng bội số thấp hơn quá khứ dù P/E hiện tại đã dưới trung bình 10 năm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **49. Định giá từng phần — SOTP** tiếp nhận điểm tựa từ **48. Bội số lịch sử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. NAV** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Định giá từng phần — SOTP

SOTP phù hợp khi doanh nghiệp có các mảng với economics và bội số khác nhau. Bài toán không dừng ở cộng giá trị từng mảng; phải điều chỉnh nợ, thuế, chi phí tập đoàn, minority interest và chiết khấu holding.

**Tổng giá trị từng phần (sum-of-the-parts, SOTP)** định giá từng mảng rồi điều chỉnh:

- nợ công ty mẹ;
- thuế;
- chi phí tập đoàn;
- quyền lợi thiểu số;
- chiết khấu công ty nắm giữ.

Không nên gán bội số của doanh nghiệp thuần túy cho từng mảng nếu mảng đó không thể tách độc lập hoặc phụ thuộc lớn vào tập đoàn.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **50. NAV** tiếp nhận điểm tựa từ **49. Định giá từng phần — SOTP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Chi phí thay thế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. NAV

Giá trị tài sản ròng (Net Asset value, NAV) thường dùng với bất động sản, holding company hoặc công ty đầu tư.

NAV cần điều chỉnh:

- giá trị tài sản thực tế;
- nợ;
- thuế;
- thanh khoản;
- thời gian hiện thực hóa;
- rủi ro pháp lý.

Giá trị sổ sách của quỹ đất không bằng giá trị có thể thu hồi nếu pháp lý chưa hoàn tất.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **51. Chi phí thay thế** tiếp nhận điểm tựa từ **50. NAV** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Giá trị thanh lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. Chi phí thay thế

Với ngành hàng hóa hoặc thâm dụng vốn, chi phí xây mới công suất tương đương có thể là mốc tham khảo.

Nếu giá trị thị trường cao hơn nhiều chi phí thay thế, công suất mới có thể được xây và kéo lợi nhuận về mức bình thường, trừ khi rào cản gia nhập rất cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **52. Giá trị thanh lý** tiếp nhận điểm tựa từ **51. Chi phí thay thế** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. Ngân hàng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Giá trị thanh lý

Với doanh nghiệp căng thẳng, cần giảm giá trị phải thu, hàng tồn kho và tài sản cố định theo khả năng bán thực tế, sau đó trừ chi phí đóng cửa và các nghĩa vụ ưu tiên.

Giá trị sổ sách vốn chủ sở hữu có thể không có nhiều ý nghĩa nếu tài sản khó chuyển thành tiền.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **53. Ngân hàng** tiếp nhận điểm tựa từ **52. Giá trị thanh lý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **54. Bảo hiểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Ngân hàng

FCFF công nghiệp thường không phù hợp với ngân hàng.

Một trực giác từ mô hình lợi nhuận thặng dư:

```text
Value
≈ Book Value
+ PV[(ROE - Cost of Equity) × Beginning Book Equity]
```

ROE bền vững cao hơn chi phí vốn tạo giá trị. Tăng trưởng có thể phá giá trị nếu ROE dưới chi phí vốn.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **54. Bảo hiểm** tiếp nhận điểm tựa từ **53. Ngân hàng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **55. REIT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. Bảo hiểm

Có thể dùng P/B, ROE, embedded giá trị (value / 값) hoặc appraisal giá trị (value / 값) tùy loại hình.

Cần chú ý:

- đủ dự phòng;
- lợi nhuận bảo hiểm cốt lõi;
- duration danh mục đầu tư;
- vốn pháp định;
- rủi ro thiên tai hoặc bồi thường.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **55. REIT** tiếp nhận điểm tựa từ **54. Bảo hiểm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. SaaS và doanh nghiệp tăng trưởng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. REIT

REIT thường được đánh giá bằng:

- FFO/AFFO;
- NAV;
- cap tỷ lệ (rate / 비율);
- đáo hạn nợ;
- tỷ lệ lấp đầy;
- tăng trưởng giá thuê.

P/E thường kém hữu ích vì khấu hao bất động sản có thể làm lợi nhuận kế toán thấp hơn dòng tiền kinh tế.

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **56. SaaS và doanh nghiệp tăng trưởng** tiếp nhận điểm tựa từ **55. REIT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. Doanh nghiệp hàng hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. SaaS và doanh nghiệp tăng trưởng

P/E ngắn hạn có thể không hữu ích nếu doanh nghiệp đang ưu tiên tăng trưởng.

Cần nhìn:

- ARR;
- retention;
- gross margin;
- CAC payback;
- SBC và pha loãng;
- con đường tới FCF.

Tăng trưởng cao nhưng đơn vị (unit / 단위) economics yếu không tự động xứng đáng bội số cao.

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **57. Doanh nghiệp hàng hóa** tiếp nhận điểm tựa từ **56. SaaS và doanh nghiệp tăng trưởng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **58. Biotech và doanh nghiệp giai đoạn sớm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. Doanh nghiệp hàng hóa

Cần phân tích:

- trữ lượng;
- đường cong chi phí;
- giả định giá hàng hóa;
- capex;
- thuế và royalty;
- hedge book;
- bảng cân đối.

Không nên kéo giá giao ngay đang ở đỉnh chu kỳ vào toàn bộ thời gian dự báo.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **58. Biotech và doanh nghiệp giai đoạn sớm** tiếp nhận điểm tựa từ **57. Doanh nghiệp hàng hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **59. Giá trị trên mỗi cổ phiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. Biotech và doanh nghiệp giai đoạn sớm

Khi kết quả phụ thuộc các mốc nhị phân, nên dùng dòng tiền hoặc kịch bản điều chỉnh xác suất thay vì một DCF duy nhất.

Các biến quan trọng gồm:

- xác suất thành công thử nghiệm;
- thời gian ra thị trường;
- nhu cầu vốn;
- pha loãng;
- runway tiền mặt;
- đối thủ và chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **59. Giá trị trên mỗi cổ phiếu** tiếp nhận điểm tựa từ **58. Biotech và doanh nghiệp giai đoạn sớm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **60. Bẫy giá trị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 59. Giá trị trên mỗi cổ phiếu

Doanh nghiệp có thể tăng doanh thu, EBITDA và EV nhưng cổ đông vẫn không hưởng lợi nếu số cổ phiếu tăng nhanh.

Luôn kết thúc bằng:

```text
Enterprise Value
→ Equity Value
→ Fully Diluted Shares
→ Value Per Share
```

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **59. Giá trị trên mỗi cổ phiếu** đã nêu tiêu chí phân biệt, còn **60. Bẫy giá trị** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **61. Biên an toàn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. Bẫy giá trị

Một cổ phiếu “rẻ” có thể tiếp tục rẻ nếu:

- ROIC thấp;
- ngành suy giảm;
- nợ lớn;
- FCF kém;
- quản trị yếu;
- pha loãng liên tục;
- tài sản khó hiện thực hóa.

Do đó mức bội số thấp không phải luận điểm đầu tư tự thân.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **60. Bẫy giá trị** đã nêu tiêu chí phân biệt, còn **61. Biên an toàn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **62. Mẫu đầu ra cho một bài định giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 61. Biên an toàn

Biên an toàn là phần đệm cho sai số mô hình và rủi ro thực thi, không chỉ là khoảng cách số học giữa giá trị nội tại và giá thị trường. Mô hình càng nhạy và dòng tiền càng khó dự báo thì phần đệm cần càng lớn.

**Biên an toàn (margin of safety)** không chỉ là lấy giá trị nội tại trừ giá thị trường.

Nó còn phụ thuộc độ chắc chắn của mô hình. Doanh nghiệp ổn định với dòng tiền dễ dự báo có thể cần biên thấp hơn doanh nghiệp chu kỳ, đòn bẩy hoặc nhị phân.

Biên an toàn phải phản ánh:

```text
độ bất định của dòng tiền
rủi ro bảng cân đối
rủi ro thanh khoản
rủi ro quản trị
độ nhạy định giá
```

> **Chuyển mạch:** Trong **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **62. Mẫu đầu ra cho một bài định giá** tiếp nhận điểm tựa từ **61. Biên an toàn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 62. Mẫu đầu ra cho một bài định giá

Một bài định giá hoàn chỉnh nên có:

```text
1. Động lực doanh thu
2. Biên lợi nhuận và tái đầu tư
3. FCFF / FCFE
4. Cơ cấu vốn
5. WACC / Cost of Equity
6. Base / Bull / Bear
7. Terminal assumptions
8. DCF
9. Multiples / SOTP / NAV nếu phù hợp
10. Reverse DCF
11. Độ nhạy
12. Giá trị trên mỗi cổ phiếu
13. Biên an toàn
14. Điều kiện làm luận điểm sai
```

> **Chuyển mạch:** Ở chặng này của **Định giá doanh nghiệp: DCF, bội số và phân tích kịch bản**, **Kết luận** gom các mảnh từ **62. Mẫu đầu ra cho một bài định giá** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết luận

Định giá tốt không phải là làm bảng tính phức tạp nhất. Mục tiêu là hiểu **giá hiện tại đang giả định điều gì**, doanh nghiệp cần tạo bao nhiêu dòng tiền để biện minh cho mức giá đó và yếu tố nào có thể làm kết quả lệch khỏi kỳ vọng.

Một mô hình hữu ích phải giúp người đọc trả lời được ba câu hỏi:

```text
Giá trị được tạo từ đâu?
Kỳ vọng nào đang được phản ánh trong giá?
Điều gì phải thay đổi để giá trị hoặc luận điểm đầu tư thay đổi?
```

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
