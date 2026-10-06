# Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**. Route đi từ business model thay vì P/E → revenue tree → margin, working capital, capex và cash flow → balance sheet/valuation → thesis, monitoring và post-investment update, để phân tích kết nối thành một quy trình.

> tệp (file / 파일) này nối các chương kế toán, chất lượng doanh nghiệp, định giá, forensic và quản trị thành một quy trình phân tích hoàn chỉnh. Mục tiêu là có thể đi từ **mô hình kinh doanh → động lực doanh thu → biên lợi nhuận → vốn lưu động → capex → dòng tiền → bảng cân đối → định giá → luận điểm → theo dõi sau đầu tư**.

## 1. Không bắt đầu bằng P/E

Một doanh nghiệp không nên được phân tích bắt đầu từ hệ số định giá. Trước hết phải hiểu cách nó kiếm tiền.

Khung tối thiểu:

```text
Khách hàng là ai?
Doanh nghiệp bán sản phẩm/dịch vụ gì?
Đơn vị kinh tế nào tạo doanh thu?
Chi phí biến đổi nằm ở đâu?
Chi phí cố định nằm ở đâu?
Cần bao nhiêu vốn để tăng trưởng?
```

Nếu chưa trả lời được các câu này, mọi mô hình DCF phía sau chỉ là bảng tính đẹp.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **2. Xây cây động lực doanh thu** nối từ **1. Không bắt đầu bằng P/E** sang **3. Tách tăng trưởng giá, sản lượng và cơ cấu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Xây cây động lực doanh thu

Doanh thu nên được phân rã thành các biến kinh tế có thể theo dõi.

Ví dụ bán lẻ:

```text
Số cửa hàng
× doanh thu mỗi cửa hàng
× tăng trưởng cửa hàng hiện hữu
= doanh thu
```

Phần mềm thuê bao:

```text
Khách hàng đầu kỳ
+ khách hàng mới
- khách hàng rời đi
= khách hàng cuối kỳ

Khách hàng × ARPU
= doanh thu
```

Bán dẫn:

```text
Sản lượng bit / đơn vị
× ASP
× cơ cấu sản phẩm
= doanh thu
```

Cây động lực tốt giúp kiểm tra mô hình bằng dữ liệu vận hành thay vì chỉ nhìn doanh thu tổng.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **3. Tách tăng trưởng giá, sản lượng và cơ cấu** nối từ **2. Xây cây động lực doanh thu** sang **4. Từ doanh thu tới biên gộp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Tách tăng trưởng giá, sản lượng và cơ cấu

Một doanh nghiệp có thể tăng doanh thu 15% nhờ:

```text
Giá +8%
Sản lượng +4%
Cơ cấu sản phẩm +3%
```

Ba nguồn này có chất lượng khác nhau. Tăng giá có thể phản ánh quyền định giá; tăng sản lượng phản ánh nhu cầu; thay đổi cơ cấu có thể làm biên lợi nhuận tăng nhưng khó lặp lại.

Khi không tách được ba phần, rất dễ ngoại suy sai.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **4. Từ doanh thu tới biên gộp** nối từ **3. Tách tăng trưởng giá, sản lượng và cơ cấu** sang **5. Biên hoạt động và đòn bẩy vận hành**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Từ doanh thu tới biên gộp

Biên gộp không phải con số tĩnh. Nó chịu:

```text
Giá bán
- chi phí đầu vào
± cơ cấu sản phẩm
± công suất sử dụng
± năng suất
± tỷ giá
```

Với ngành chu kỳ, công suất sử dụng là biến đặc biệt quan trọng vì chi phí cố định trên mỗi đơn vị thay đổi mạnh.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **5. Biên hoạt động và đòn bẩy vận hành** nối từ **4. Từ doanh thu tới biên gộp** sang **6. Tách chi phí duy trì và chi phí tăng trưởng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Biên hoạt động và đòn bẩy vận hành

Nếu chi phí cố định lớn, doanh thu tăng có thể làm lợi nhuận hoạt động tăng nhanh hơn. Đây là **đòn bẩy vận hành (operating leverage)**.

Nhưng cơ chế này hoạt động hai chiều:

```text
Doanh thu giảm
→ chi phí cố định chưa giảm ngay
→ biên hoạt động co nhanh
```

Vì vậy không nên áp dụng biên lợi nhuận trung bình ổn định cho ngành có đòn bẩy vận hành cao.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **6. Tách chi phí duy trì và chi phí tăng trưởng** nối từ **5. Biên hoạt động và đòn bẩy vận hành** sang **7. Vốn lưu động là cầu nối giữa lợi nhuận và tiền mặt**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Tách chi phí duy trì và chi phí tăng trưởng

R&D, marketing, capex hay chi phí mở cửa hàng có thể vừa duy trì doanh nghiệp hiện tại vừa tạo tăng trưởng mới.

Một doanh nghiệp báo FCF thấp vì đầu tư tăng trưởng có thể vẫn tạo giá trị nếu ROIC tăng thêm cao. Ngược lại FCF cao vì cắt đầu tư cần thiết có thể chỉ là cải thiện ngắn hạn.

Câu hỏi quan trọng:

```text
Nếu ngừng đầu tư hôm nay, dòng tiền hiện tại có duy trì được bao lâu?
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **7. Vốn lưu động là cầu nối giữa lợi nhuận và tiền mặt** nối từ **6. Tách chi phí duy trì và chi phí tăng trưởng** sang **8. Chất lượng doanh thu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Vốn lưu động là cầu nối giữa lợi nhuận và tiền mặt

Doanh thu tăng không bảo đảm tiền mặt tăng. Tăng trưởng có thể hút tiền qua:

```text
Phải thu
Tồn kho
Trả trước
```

Hoặc được tài trợ bởi:

```text
Phải trả
Doanh thu nhận trước
Tiền khách hàng ứng trước
```

Mô hình cần nối DSO, DIO, DPO hoặc tỷ lệ vốn lưu động với tốc độ tăng trưởng.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **8. Chất lượng doanh thu** nối từ **7. Vốn lưu động là cầu nối giữa lợi nhuận và tiền mặt** sang **9. Xây cầu nối lợi nhuận chuẩn hóa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Chất lượng doanh thu

Doanh thu tốt không chỉ là doanh thu tăng.

Cần hỏi:

- tiền đã thu chưa?
- khách hàng có quyền trả lại không?
- doanh thu có phụ thuộc một khách hàng lớn không?
- có chiết khấu bất thường không?
- có dấu hiệu kéo doanh thu từ tương lai về hiện tại không?

Tăng doanh thu cùng phải thu tăng nhanh và tiền mặt yếu là tín hiệu cần điều tra thêm.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **9. Xây cầu nối lợi nhuận chuẩn hóa** nối từ **8. Chất lượng doanh thu** sang **10. Three-statement mô hình (model / 모델) phải tự khóa lô-gic (logic / 논리)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Xây cầu nối lợi nhuận chuẩn hóa

Lợi nhuận báo cáo có thể chứa:

```text
Khoản một lần
Lãi/lỗ bán tài sản
Chi phí tái cấu trúc
Lợi ích thuế
Chi phí pháp lý
Impairment
```

Hãy xây:

```text
Lợi nhuận báo cáo
± điều chỉnh hợp lý
= lợi nhuận chuẩn hóa
```

Nhưng không được loại mọi chi phí “khó chịu”. Nếu tái cấu trúc xuất hiện mỗi năm, nó là một phần kinh tế thực.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **10. Three-statement mô hình (model / 모델) phải tự khóa lô-gic (logic / 논리)** nối từ **9. Xây cầu nối lợi nhuận chuẩn hóa** sang **11. Lập lịch nợ riêng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Three-statement mô hình (model / 모델) phải tự khóa lô-gic (logic / 논리)

Ba báo cáo phải nối được:

```text
Income Statement
→ Net Income
→ Cash Flow Statement
→ Ending Cash
→ Balance Sheet
```

Và:

```text
Capex
→ PPE
→ Depreciation
```

```text
Debt
→ Interest Expense
→ Cash Flow / Ending Debt
```

Nếu bảng cân đối không cân hoặc tiền mặt không nối đúng, mô hình chưa đáng tin.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **11. Lập lịch nợ riêng** nối từ **10. Three-statement mô hình (model / 모델) phải tự khóa lô-gic (logic / 논리)** sang **12. Dự báo lãi vay đúng cơ chế**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Lập lịch nợ riêng

Đừng dùng một dòng “debt” duy nhất. Lập bảng:

```text
Nợ đầu kỳ
+ vay mới
- trả gốc
= nợ cuối kỳ
```

Kèm:

```text
Lãi suất cố định / thả nổi
Kỳ hạn đáo hạn
Tài sản bảo đảm
Covenant
```

Điều này cho phép mô phỏng refinancing stress thay vì chỉ nhìn Debt/EBITDA hiện tại.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **11. Lập lịch nợ riêng** đặt đầu vào cho **12. Dự báo lãi vay đúng cơ chế**, rồi **13. ROIC phải tách quá khứ và phần vốn mới** mở rộng hệ quả hoặc giới hạn liên quan.

## 12. Dự báo lãi vay đúng cơ chế

Chi phí lãi vay nên dựa vào nợ bình quân và lãi suất thực tế, không kéo bằng CAGR tùy ý.

Khi lãi suất thị trường tăng, chi phí lãi thường chỉ tăng khi nợ thả nổi tái định giá hoặc nợ cũ đáo hạn. Đây là độ trễ quan trọng trong phân tích doanh nghiệp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **12. Dự báo lãi vay đúng cơ chế** đặt đầu vào cho **13. ROIC phải tách quá khứ và phần vốn mới**, rồi **14. Reinvestment runway** mở rộng hệ quả hoặc giới hạn liên quan.

## 13. ROIC phải tách quá khứ và phần vốn mới

ROIC lịch sử cao không đảm bảo tăng trưởng mới tạo giá trị.

Theo dõi:

```text
Incremental NOPAT
/ Incremental Invested Capital
= Incremental ROIC
```

Nếu ROIC tăng thêm giảm mạnh khi doanh nghiệp mở rộng, lợi thế kinh tế có thể đang bão hòa.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **14. Reinvestment runway** nối từ **13. ROIC phải tách quá khứ và phần vốn mới** sang **15. Moat phải được kiểm chứng bằng dữ liệu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Reinvestment runway

Doanh nghiệp tốt nhất không chỉ có ROIC cao mà còn có **dư địa tái đầu tư (reinvestment runway)** dài.

Một công ty có ROIC 40% nhưng chỉ tái đầu tư được 5% lợi nhuận có thể tăng trưởng chậm hơn công ty ROIC 20% nhưng tái đầu tư được phần lớn dòng tiền trong nhiều năm.

Giá trị phụ thuộc cả **chất lượng** và **quy mô cơ hội**.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **14. Reinvestment runway** đặt vấn đề; **15. Moat phải được kiểm chứng bằng dữ liệu** đối chiếu bằng chứng, rồi **16. Dấu hiệu moat suy yếu** mở rộng hệ quả hoặc giới hạn liên quan.

## 15. Moat phải được kiểm chứng bằng dữ liệu

Không gọi một thương hiệu là “moat” chỉ vì nổi tiếng.

Tìm bằng chứng:

```text
Retention cao
Pricing power
Market share bền
Gross margin ổn định
ROIC vượt chi phí vốn
CAC payback tốt
Chi phí chuyển đổi cao
Network density tăng
```

Lợi thế cạnh tranh phải xuất hiện trong số liệu kinh tế.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **15. Moat phải được kiểm chứng bằng dữ liệu** đặt vấn đề; **16. Dấu hiệu moat suy yếu** đối chiếu bằng chứng, rồi **17. Quản trị phải nhìn qua phân bổ vốn** mở rộng hệ quả hoặc giới hạn liên quan.

## 16. Dấu hiệu moat suy yếu

Một số tín hiệu:

```text
Chi phí thu hút khách hàng tăng
Retention giảm
Chiết khấu tăng
Biên lợi nhuận giảm
Thị phần giảm dù chi phí marketing tăng
ROIC tăng thêm giảm
R&D phải tăng mạnh chỉ để giữ vị trí
```

Giá cổ phiếu có thể chưa phản ánh ngay sự suy yếu này.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **17. Quản trị phải nhìn qua phân bổ vốn** nối từ **16. Dấu hiệu moat suy yếu** sang **18. Mua lại cổ phiếu chỉ tốt khi giá hợp lý**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Quản trị phải nhìn qua phân bổ vốn

Đánh giá ban lãnh đạo không nên dựa vào cách nói trên cuộc họp.

Hãy kiểm tra lịch sử:

```text
Capex
M&A
Buyback
Dividend
Debt
SBC
```

và hỏi mỗi đồng vốn được dùng có tạo giá trị trên mỗi cổ phiếu hay không.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **18. Mua lại cổ phiếu chỉ tốt khi giá hợp lý** nối từ **17. Quản trị phải nhìn qua phân bổ vốn** sang **19. M&A phải được phân tích như một khoản đầu tư**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Mua lại cổ phiếu chỉ tốt khi giá hợp lý

Buyback tạo giá trị nếu mua dưới giá trị nội tại và không làm bảng cân đối yếu đi.

Nếu công ty mua cổ phiếu ở định giá quá cao rồi phát hành lại qua SBC, lợi ích cho cổ đông cũ có thể rất thấp.

Theo dõi **số cổ phiếu pha loãng thực tế**, không chỉ số tiền buyback.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **19. M&A phải được phân tích như một khoản đầu tư** nối từ **18. Mua lại cổ phiếu chỉ tốt khi giá hợp lý** sang **20. Xây kịch bản từ driver, không từ phần trăm tùy ý**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. M&A phải được phân tích như một khoản đầu tư

Hỏi:

```text
Giá mua bao nhiêu?
EBIT/FCF mua được bao nhiêu?
Synergy cần đạt bao nhiêu?
Dùng nợ hay cổ phiếu?
ROIC sau mua lại so với WACC?
```

Nếu thương vụ chỉ tăng EPS nhờ dùng nợ rẻ nhưng ROIC dưới chi phí vốn, tăng EPS không đồng nghĩa tạo giá trị.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **20. Xây kịch bản từ driver, không từ phần trăm tùy ý** nối từ **19. M&A phải được phân tích như một khoản đầu tư** sang **21. Reverse DCF để đọc kỳ vọng trong giá**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Xây kịch bản từ driver, không từ phần trăm tùy ý

Kịch bản tốt thay đổi các biến nguyên nhân:

```text
Base:
Sản lượng +5%, ASP +2%, biên +100 bp

Bull:
Sản lượng +8%, ASP +5%, utilization cao hơn

Bear:
Sản lượng -3%, ASP -7%, inventory tăng, biên giảm
```

Sau đó mô hình tự truyền xuống EPS và FCF.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **21. Reverse DCF để đọc kỳ vọng trong giá** nối từ **20. Xây kịch bản từ driver, không từ phần trăm tùy ý** sang **22. Định giá phải nhất quán với giai đoạn chu kỳ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Reverse DCF để đọc kỳ vọng trong giá

Thay vì hỏi “giá trị hợp lý là bao nhiêu?”, có thể hỏi:

> Giá hiện tại yêu cầu doanh nghiệp tăng trưởng và duy trì ROIC thế nào?

Nếu giá chỉ hợp lý khi doanh nghiệp duy trì 25% tăng trưởng 10 năm và biên tăng liên tục, mức kỳ vọng có thể quá cao.

Reverse DCF biến định giá thành bài toán về kỳ vọng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **22. Định giá phải nhất quán với giai đoạn chu kỳ** nối từ **21. Reverse DCF để đọc kỳ vọng trong giá** sang **23. Từ định giá tới lợi suất kỳ vọng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Định giá phải nhất quán với giai đoạn chu kỳ

Công ty chu kỳ thường P/E thấp ở đỉnh lợi nhuận và P/E cao ở đáy.

Vì vậy nên dùng:

```text
Lợi nhuận chuẩn hóa
Mid-cycle margin
Replacement cost
NAV
EV/EBITDA chuẩn hóa
```

thay vì trailing P/E máy móc.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **23. Từ định giá tới lợi suất kỳ vọng** nối từ **22. Định giá phải nhất quán với giai đoạn chu kỳ** sang **24. Luận điểm đầu tư phải có cấu trúc**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Từ định giá tới lợi suất kỳ vọng

Sau khi có khoảng giá trị, xây cầu nối:

```text
Giá hiện tại
→ FCF / EPS tăng trưởng
→ phân phối cho cổ đông
→ mức định giá cuối kỳ
→ lợi suất kỳ vọng
```

Điều này giúp so doanh nghiệp với tài sản thay thế thay vì chỉ nói “upside 20%”.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **24. Luận điểm đầu tư phải có cấu trúc** nối từ **23. Từ định giá tới lợi suất kỳ vọng** sang **25. Catalyst không thay thế giá trị**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Luận điểm đầu tư phải có cấu trúc

Một thesis tốt gồm:

```text
Thị trường đang kỳ vọng gì?
Tôi khác thị trường ở điểm nào?
Dữ liệu nào hỗ trợ?
Catalyst nào có thể làm kỳ vọng đổi?
Điều kiện nào chứng minh tôi sai?
```

Nếu không thể viết ngắn gọn năm phần này, luận điểm có thể chưa đủ rõ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **25. Catalyst không thay thế giá trị** nối từ **24. Luận điểm đầu tư phải có cấu trúc** sang **26. vô hiệu hóa (invalidation / 무효화) phải liên quan cơ chế**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Catalyst không thay thế giá trị

Một doanh nghiệp tốt không cần catalyst ngắn hạn để có giá trị, nhưng catalyst giúp hiểu thời điểm thị trường có thể cập nhật kỳ vọng.

Catalyst có thể là:

```text
Sản phẩm mới
Chu kỳ giá
Giảm capex
Tái cấu trúc
M&A / spin-off
Thay đổi chính sách
Kết quả quý xác nhận thesis
```

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **25. Catalyst không thay thế giá trị** đặt đầu vào cho **26. vô hiệu hóa (invalidation / 무효화) phải liên quan cơ chế**, rồi **27. Bảng theo dõi sau đầu tư** mở rộng hệ quả hoặc giới hạn liên quan.

## 26. vô hiệu hóa (invalidation / 무효화) phải liên quan cơ chế

Không dùng “giá giảm 15%” làm vô hiệu hóa (invalidation / 무효화) nếu luận điểm cơ bản không đổi.

Vô hiệu hóa (invalidation / 무효화) tốt hơn:

```text
Khách hàng chủ chốt rời đi
ASP không phục hồi như giả định
ROIC mới dưới WACC
Nợ không tái cấp vốn được
Biên lợi nhuận cấu trúc giảm
```

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **26. vô hiệu hóa (invalidation / 무효화) phải liên quan cơ chế** đặt đầu vào cho **27. Bảng theo dõi sau đầu tư**, rồi **28. Phân biệt thesis drift và thesis evolution** mở rộng hệ quả hoặc giới hạn liên quan.

## 27. Bảng theo dõi sau đầu tư

Mỗi quý cập nhật:

```text
Driver chính
KPI dẫn dắt
Ước tính doanh thu / EPS
Dòng tiền
Nợ
Định giá
Catalyst
Invalidation
```

Không cần xây lại toàn bộ thesis nếu chỉ một chỉ tiêu phụ thay đổi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **28. Phân biệt thesis drift và thesis evolution** nối từ **27. Bảng theo dõi sau đầu tư** sang **29. Bài tập tích hợp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Phân biệt thesis drift và thesis evolution

Khi dữ liệu mới xuất hiện, luận điểm có thể được cập nhật hoặc bị thay thế. Phần này đặt tiêu chí để phân biệt việc sửa giả định có căn cứ với việc đổi câu chuyện chỉ để tránh thừa nhận thesis ban đầu sai.

**Thesis evolution:** giả định được cập nhật hợp lý khi dữ liệu mới xuất hiện.

**Thesis drift:** người đầu tư thay lý do nắm giữ để tránh thừa nhận luận điểm ban đầu sai.

Nhật ký phiên bản giúp phân biệt hai việc này.

> **Nối mạch:** Trong **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **29. Bài tập tích hợp** nối từ **28. Phân biệt thesis drift và thesis evolution** sang **30. Liên kết đọc tiếp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Bài tập tích hợp

Chọn một doanh nghiệp và hoàn thành:

1. cây doanh thu;
2. cầu nối biên lợi nhuận;
3. lịch vốn lưu động;
4. lịch capex–khấu hao;
5. lịch nợ;
6. three-statement mô hình (model / 모델) 5 năm;
7. FCFF/FCFE;
8. cơ sở (base / 기반)/bull/bear;
9. reverse DCF;
10. one-page thesis;
11. danh sách KPI theo dõi hàng quý.

Nếu làm được bài này mà không dựa vào một bội số duy nhất, người đọc đã tiến từ “đọc báo cáo” sang **phân tích doanh nghiệp tích hợp**.

> **Nối mạch:** Ở chặng này của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, sau nội dung của **29. Bài tập tích hợp**, **30. Liên kết đọc tiếp** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Kết luận** mở rộng hệ quả hoặc giới hạn liên quan.

## 30. Liên kết đọc tiếp

Đây là điểm bàn giao từ mô hình tích hợp sang các nguồn canonical: báo cáo tài chính, business quality, valuation, earnings quality và governance. Chọn link theo phần còn yếu rồi quay lại lab để cập nhật mô hình và thesis.

- [Báo cáo tài chính và kế toán](./01_FINANCIAL_STATEMENTS_AND_ACCOUNTING.md)
- [Chất lượng doanh nghiệp và lợi thế cạnh tranh](./02_BUSINESS_QUALITY_MOAT_AND_INDUSTRY.md)
- [Định giá DCF và bội số](./03_VALUATION_DCF_AND_MULTIPLES.md)
- [Chất lượng lợi nhuận và forensic](./04_EARNINGS_QUALITY_MODELING_AND_FORENSICS.md)
- [Quản trị và phân bổ vốn](./06_GOVERNANCE_CAPITAL_ALLOCATION_MA_AND_MANAGEMENT_QUALITY.md)

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phòng thí nghiệm nâng cao: mô hình doanh nghiệp tích hợp và quản trị luận điểm đầu tư**, **Kết luận** tổng hợp từ **30. Liên kết đọc tiếp** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết luận

Phân tích doanh nghiệp sâu không phải cộng thêm nhiều tỷ số. Chuỗi đúng là:

```text
Mô hình kinh doanh
→ driver vận hành
→ kế toán
→ dòng tiền
→ bảng cân đối
→ ROIC / tái đầu tư
→ định giá
→ kỳ vọng thị trường
→ thesis
→ theo dõi và cập nhật
```

Một mô hình chỉ có giá trị khi nó giúp người đọc hiểu **vì sao** kết quả thay đổi và **điều gì phải xảy ra để luận điểm sai**.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
