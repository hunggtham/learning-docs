# Cổ phiếu, ETF và quỹ đầu tư

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Cổ phiếu, ETF và quỹ đầu tư**. Route đi từ total return và three-layer stock example → common stock/residual claim → ETFs, index mechanics và funds → liquidity, fees, tax và tracking risk → chọn công cụ theo quyền lợi kinh tế.

> Chương này giải thích cổ phiếu và quỹ từ bản chất quyền sở hữu tới cách triển khai qua ETF. Mục tiêu là nhìn xuyên tên sản phẩm để hiểu tài sản cơ sở, quyền lợi của cổ đông, cơ chế chỉ số, thanh khoản, chi phí và rủi ro thực tế.

> **Cách đọc dễ hơn:** trước mỗi khái niệm, hãy hỏi “nó thay đổi quyền lợi kinh tế hoặc rủi ro của cổ đông như thế nào?”. Nếu cần ví dụ số và lộ trình từ cơ bản đến nâng cao, đọc [Bắt đầu từ đây — Cổ phiếu và Forex](../START_HERE_STOCKS_AND_FOREX.md) trước.

## 0. Ví dụ đọc lợi nhuận cổ phiếu bằng ba lớp

Giả sử ban đầu:

```text
EPS = 2 USD
P/E = 15 lần
Giá cổ phiếu = 2 × 15 = 30 USD
```

Sau một năm, doanh nghiệp tăng EPS lên `2,4 USD` nhưng thị trường chỉ trả `P/E = 12 lần`:

```text
Giá mới = 2,4 × 12 = 28,8 USD
Lợi suất giá ≈ (28,8 / 30) - 1 = -4%
```

Nếu nhận thêm `1 USD` cổ tức:

```text
Tổng lợi suất trước thuế/phí ≈ (28,8 + 1) / 30 - 1 = -0,7%
```

Doanh nghiệp tốt lên về EPS nhưng khoản đầu tư vẫn gần như đi ngang vì **bội số định giá co lại**. Vì vậy luôn tách ba lớp:

```text
Tổng lợi suất ≈ tăng trưởng lợi nhuận trên mỗi cổ phiếu
                 + thay đổi bội số định giá
                 + cổ tức / mua lại ròng
```

Ví dụ này chỉ minh họa cơ chế; không dùng một P/E đơn lẻ để định giá mọi doanh nghiệp.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **0. Ví dụ đọc lợi nhuận cổ phiếu bằng ba lớp** nêu quy tắc; **1. Cổ phiếu phổ thông là quyền lợi còn lại** thử quy tắc trong tình huống, rồi **2. Giá trị doanh nghiệp và giá trị vốn chủ sở hữu** mở rộng hệ quả.

## 1. Cổ phiếu phổ thông là quyền lợi còn lại

Người sở hữu cổ phiếu phổ thông là chủ sở hữu phần còn lại (residual owner). Sau khi doanh nghiệp trả lương, nhà cung cấp, thuế, lãi vay và nghĩa vụ với chủ nợ, phần giá trị còn lại thuộc cổ đông.

Điều này tạo tiềm năng tăng trưởng lớn nhưng cũng khiến cổ đông chịu tổn thất đầu tiên khi doanh nghiệp thất bại.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **2. Giá trị doanh nghiệp và giá trị vốn chủ sở hữu** nối từ **1. Cổ phiếu phổ thông là quyền lợi còn lại** sang **3. Vốn hóa thị trường và free float**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Giá trị doanh nghiệp và giá trị vốn chủ sở hữu

Giá trị doanh nghiệp (Enterprise value, EV) phản ánh giá trị hoạt động dành cho tất cả nhà cung cấp vốn. Giá trị vốn chủ sở hữu (Equity value) là phần thuộc cổ đông.

Một cầu nối đơn giản:

```text
EV ≈ Equity Value + Net Debt + Other Senior Claims - Non-operating Assets
```

Không thể so P/E và EV/EBITDA như thể chúng đo cùng một lớp giá trị.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **3. Vốn hóa thị trường và free float** nối từ **2. Giá trị doanh nghiệp và giá trị vốn chủ sở hữu** sang **4. Basic và diluted shares**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Vốn hóa thị trường và free float

Vốn hóa thị trường:

```text
Market Cap = Share Price × Shares Outstanding
```

Vốn hóa theo free float chỉ tính phần cổ phiếu thực sự có thể giao dịch công khai. Đây là thông tin quan trọng cho thanh khoản và trọng số chỉ số.

Doanh nghiệp có thị trường (market / 시장) cap lớn nhưng phần lớn cổ phiếu do cổ đông kiểm soát nắm giữ có thể có free float nhỏ hơn nhiều.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **4. Basic và diluted shares** nối từ **3. Vốn hóa thị trường và free float** sang **5. EPS và tăng trưởng trên mỗi cổ phiếu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Basic và diluted shares

Số cổ phiếu cơ bản chỉ tính cổ phiếu hiện tại. Số cổ phiếu pha loãng (diluted shares) xem thêm quyền chọn nhân viên, RSU, trái phiếu chuyển đổi và các công cụ có thể tạo cổ phiếu mới.

Định giá trên mỗi cổ phiếu nên nhìn số pha loãng khi khả năng chuyển đổi có ý nghĩa.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **5. EPS và tăng trưởng trên mỗi cổ phiếu** nối từ **4. Basic và diluted shares** sang **6. Cổ tức**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. EPS và tăng trưởng trên mỗi cổ phiếu

Sau khi phân biệt số cổ phiếu cơ bản và pha loãng, ta có thể tính phần lợi nhuận thực sự thuộc về từng đơn vị sở hữu. EPS là cầu nối từ kết quả doanh nghiệp sang định giá cổ phiếu.

```text
EPS = Net Income Available to Common / Diluted Shares
```

Doanh thu và lợi nhuận tổng có thể tăng trong khi EPS tăng chậm nếu doanh nghiệp phát hành nhiều cổ phiếu.

Nhà đầu tư sở hữu **một phần trên mỗi cổ phiếu**, không sở hữu con số lợi nhuận tổng của công ty.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **6. Cổ tức** nối từ **5. EPS và tăng trưởng trên mỗi cổ phiếu** sang **7. Mua lại cổ phiếu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Cổ tức

Cổ tức là tiền mặt được phân phối từ doanh nghiệp sang cổ đông. Giá thường điều chỉnh quanh ngày không hưởng quyền, nên cổ tức không phải tiền miễn phí.

Một doanh nghiệp trả cổ tức cao nhưng không còn khả năng tái đầu tư hiệu quả có kinh tế khác doanh nghiệp trả cổ tức thấp nhưng tái đầu tư ở ROIC rất cao.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **7. Mua lại cổ phiếu** nối từ **6. Cổ tức** sang **8. Pha loãng và phát hành thêm**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Mua lại cổ phiếu

Mua lại tạo giá trị khi:

```text
Giá mua hợp lý
+ Doanh nghiệp có đủ nguồn vốn
+ Không làm bảng cân đối yếu
+ Số cổ phiếu thực tế giảm
```

Mua lại chỉ để bù lượng cổ phiếu phát hành qua SBC không tạo cùng mức lợi ích cho cổ đông cũ.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **8. Pha loãng và phát hành thêm** nối từ **7. Mua lại cổ phiếu** sang **9. Chia tách cổ phiếu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Pha loãng và phát hành thêm

Phát hành thêm có thể cần thiết để tài trợ tăng trưởng hoặc củng cố vốn, nhưng làm giảm tỷ lệ sở hữu của cổ đông hiện hữu nếu giá trị tạo thêm không đủ lớn.

Phát hành quyền mua, cổ phiếu ưu đãi chuyển đổi, option và warrant đều cần được đưa vào phân tích pha loãng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **9. Chia tách cổ phiếu** nối từ **8. Pha loãng và phát hành thêm** sang **10. Hành động doanh nghiệp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Chia tách cổ phiếu

Chia tách làm tăng số lượng cổ phiếu và giảm giá trên mỗi cổ phiếu theo tỷ lệ tương ứng. Nó không tự thay đổi giá trị doanh nghiệp.

Tâm lý hoặc khả năng tiếp cận của nhà đầu tư cá nhân có thể thay đổi, nhưng bản chất kinh tế không đổi tại thời điểm chia tách.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **10. Hành động doanh nghiệp** nối từ **9. Chia tách cổ phiếu** sang **11. Quyền biểu quyết và quản trị**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Hành động doanh nghiệp

Ngoài chia tách và cổ tức, còn có sáp nhập, tách doanh nghiệp, phát hành quyền mua, cổ tức đặc biệt, hủy cổ phiếu quỹ và thay đổi cấu trúc vốn.

Mỗi hành động có thể ảnh hưởng số cổ phiếu, quyền biểu quyết, cơ sở thuế, chỉ số và hợp đồng phái sinh.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **11. Quyền biểu quyết và quản trị** nối từ **10. Hành động doanh nghiệp** sang **12. Stewardship và bỏ phiếu ủy quyền**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Quyền biểu quyết và quản trị

Cổ đông không chỉ nhận dòng tiền mà còn có quyền biểu quyết theo cấu trúc cổ phiếu. Một số doanh nghiệp có nhiều lớp cổ phiếu với quyền biểu quyết khác nhau.

Nhà đầu tư cần kiểm tra quyền của cổ đông thiểu số, cơ chế bầu hội đồng quản trị và quyền lực của cổ đông kiểm soát.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **12. Stewardship và bỏ phiếu ủy quyền** nối từ **11. Quyền biểu quyết và quản trị** sang **13. Chỉ số là tập hợp quy tắc**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Stewardship và bỏ phiếu ủy quyền

Quỹ lớn có thể thực hiện vai trò quản trị chủ sở hữu (stewardship) thông qua bỏ phiếu ủy quyền, đối thoại với ban lãnh đạo và chính sách quản trị.

Quỹ thụ động vẫn có quyền cổ đông dù không chủ động chọn từng cổ phiếu.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **13. Chỉ số là tập hợp quy tắc** nối từ **12. Stewardship và bỏ phiếu ủy quyền** sang **14. Chỉ số theo vốn hóa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Chỉ số là tập hợp quy tắc

Một chỉ số phải trả lời:

```text
Ai đủ điều kiện?
Trọng số tính thế nào?
Có giới hạn tập trung không?
Khi nào tái cân bằng?
Dữ liệu nào dùng để thêm / loại cổ phiếu?
```

Tên “thị trường”, “AI”, “tăng trưởng” hay “giá trị” không đủ để hiểu exposure.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **14. Chỉ số theo vốn hóa** nối từ **13. Chỉ số là tập hợp quy tắc** sang **15. Chỉ số tỷ trọng bằng nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Chỉ số theo vốn hóa

Chỉ số theo vốn hóa thị trường đặt tỷ trọng lớn hơn vào doanh nghiệp có thị trường (market / 시장) cap lớn hơn. Ưu điểm là chi phí giao dịch thấp và tự điều chỉnh theo quy mô thị trường.

Nhược điểm là có thể trở nên tập trung khi một số doanh nghiệp tăng giá rất mạnh.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **15. Chỉ số tỷ trọng bằng nhau** nối từ **14. Chỉ số theo vốn hóa** sang **16. Rủi ro tập trung chỉ số**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Chỉ số tỷ trọng bằng nhau

Chỉ số tỷ trọng bằng nhau (equal weight) giảm tập trung ở công ty lớn nhưng cần tái cân bằng thường xuyên hơn, tạo turnover và nghiêng về doanh nghiệp nhỏ hơn.

Nó không đơn giản là “phiên bản tốt hơn” của chỉ số vốn hóa; đó là exposure khác.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **16. Rủi ro tập trung chỉ số** nối từ **15. Chỉ số tỷ trọng bằng nhau** sang **17. ETF là cấu trúc quỹ giao dịch trên sở**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Rủi ro tập trung chỉ số

Chỉ số rộng theo số lượng cổ phiếu vẫn có thể tập trung theo tỷ trọng hoặc nhân tố.

Cần theo dõi:

```text
Top 10 weight
Sector weights
Country weights
Factor exposure
Contribution to index return
```

KOSPI hoặc S&P 500 tăng không đồng nghĩa cổ phiếu trung vị cũng tăng tương ứng.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **17. ETF là cấu trúc quỹ giao dịch trên sở** nối từ **16. Rủi ro tập trung chỉ số** sang **18. NAV và iNAV**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. ETF là cấu trúc quỹ giao dịch trên sở

ETF cho phép mua bán chứng chỉ quỹ trong phiên như cổ phiếu. ETF có thể theo chỉ số hoặc chiến lược chủ động.

Điều quan trọng là tài sản cơ sở và phương pháp quản lý, không phải chữ ETF.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **18. NAV và iNAV** nối từ **17. ETF là cấu trúc quỹ giao dịch trên sở** sang **19. Cơ chế tạo và mua lại**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. NAV và iNAV

Giá trị tài sản ròng (NAV) là giá trị tài sản trừ nghĩa vụ trên mỗi chứng chỉ. Giá trị tài sản ròng ước tính trong phiên (iNAV) có thể dùng dữ liệu gần thời gian thực nhưng độ chính xác phụ thuộc tài sản cơ sở.

Nếu tài sản cơ sở đóng cửa hoặc ít giao dịch, iNAV có thể cũ.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **18. NAV và iNAV** đặt đầu vào cho **19. Cơ chế tạo và mua lại**, rồi **20. Thanh khoản ETF có hai lớp** mở rộng hệ quả hoặc giới hạn liên quan.

## 19. Cơ chế tạo và mua lại

Thành viên tạo lập (Authorized Participant, AP) có thể tạo hoặc mua lại lô ETF bằng rổ tài sản hoặc tiền mặt theo quy tắc.

Cơ chế này giúp nhà tạo lập chênh lệch giá và giữ giá ETF gần giá trị tài sản cơ sở trong điều kiện bình thường.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **19. Cơ chế tạo và mua lại** đặt đầu vào cho **20. Thanh khoản ETF có hai lớp**, rồi **21. Premium và discount** mở rộng hệ quả hoặc giới hạn liên quan.

## 20. Thanh khoản ETF có hai lớp

Thanh khoản của ETF gồm:

```text
Thanh khoản chứng chỉ ETF trên sở
Thanh khoản của tài sản cơ sở
```

Khối lượng giao dịch ETF thấp không luôn đồng nghĩa ETF không thanh khoản nếu tài sản cơ sở rất thanh khoản và cơ chế tạo–mua lại hoạt động tốt.

Ngược lại ETF có khối lượng cao nhưng tài sản cơ sở kém thanh khoản vẫn có thể gặp spread lớn trong căng thẳng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **21. Premium và discount** nối từ **20. Thanh khoản ETF có hai lớp** sang **22. Tracking Difference và Tracking lỗi (error / 오류)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Premium và discount

Giá ETF có thể cao hơn NAV (premium) hoặc thấp hơn NAV (discount).

Khi thị trường cơ sở đóng cửa, chênh lệch có thể phản ánh quá trình khám phá giá nhanh hơn NAV cũ thay vì cơ hội chênh lệch giá chắc chắn.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **22. Tracking Difference và Tracking lỗi (error / 오류)** nối từ **21. Premium và discount** sang **23. Sao chép vật lý và tổng hợp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Tracking Difference và Tracking lỗi (error / 오류)

Khi đã hiểu NAV, premium/discount và cơ chế tạo–mua lại, ta cần đo xem quỹ bám mục tiêu tốt đến đâu. Tracking difference nói về độ lệch tích lũy; tracking error nói về mức dao động của độ lệch đó.

**Sai lệch lợi suất (tracking difference)** là chênh lệch lợi suất tích lũy giữa quỹ và chỉ số.

**Sai số bám chỉ số (tracking error)** đo biến động của chênh lệch lợi suất theo thời gian.

Nguyên nhân gồm phí, thuế, tiền mặt, tối ưu hóa rổ, cho vay chứng khoán, chi phí tái cân bằng và FX hedge.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **23. Sao chép vật lý và tổng hợp** tổng hợp từ **22. Tracking Difference và Tracking lỗi (error / 오류)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **24. Cho vay chứng khoán** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. Sao chép vật lý và tổng hợp

ETF vật lý nắm toàn bộ hoặc mẫu tài sản cơ sở. ETF tổng hợp (synthetic ETF) dùng hợp đồng phái sinh để nhận lợi suất chỉ số.

Cấu trúc tổng hợp có thể giảm lỗi bám trong một số thị trường nhưng thêm rủi ro đối tác và tài sản bảo đảm.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **24. Cho vay chứng khoán** tổng hợp từ **23. Sao chép vật lý và tổng hợp** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **25. ETF có phòng vệ và không phòng vệ FX** mở rộng hệ quả hoặc giới hạn liên quan.

## 24. Cho vay chứng khoán

Quỹ có thể cho vay cổ phiếu để kiếm phí. Thu nhập này có thể bù một phần chi phí quỹ.

Cần kiểm tra tỷ lệ chia thu nhập, chất lượng tài sản thế chấp và giới hạn người vay.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **25. ETF có phòng vệ và không phòng vệ FX** nối từ **24. Cho vay chứng khoán** sang **26. ETF đòn bẩy và nghịch đảo**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. ETF có phòng vệ và không phòng vệ FX

ETF niêm yết KRW nhưng nắm tài sản USD không phòng vệ vẫn có exposure USD.

ETF phòng vệ dùng forward/swap để giảm biến động FX, đổi lại có chi phí carry, basis, giao dịch và sai lệch phòng vệ.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **26. ETF đòn bẩy và nghịch đảo** nối từ **25. ETF có phòng vệ và không phòng vệ FX** sang **27. Quỹ mở truyền thống**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. ETF đòn bẩy và nghịch đảo

Các quỹ này thường đặt mục tiêu theo ngày. Do tái cân bằng hàng ngày, lợi suất nhiều ngày phụ thuộc đường đi của giá.

```text
Biến động cao + qua lại nhiều
→ Hao mòn do đường đi có thể lớn
```

Không nên kỳ vọng lợi suất một tháng luôn bằng “2 × lợi suất chỉ số tháng”.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **27. Quỹ mở truyền thống** nối từ **26. ETF đòn bẩy và nghịch đảo** sang **28. Quỹ chủ động và quỹ thụ động**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Quỹ mở truyền thống

Quỹ mở được mua/bán theo NAV sau thời điểm chốt trong ngày thay vì giao dịch liên tục trên sở.

Ưu điểm và nhược điểm khác ETF về spread, thuế, khả năng giao dịch và mức minh bạch trong phiên.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **28. Quỹ chủ động và quỹ thụ động** nối từ **27. Quỹ mở truyền thống** sang **29. Active Share**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Quỹ chủ động và quỹ thụ động

Quỹ thụ động tuân theo quy tắc chỉ số. Quỹ chủ động cho nhà quản lý quyền lựa chọn chứng khoán, tỷ trọng và đôi khi thời điểm.

Quỹ chủ động chỉ đáng trả phí cao hơn nếu lợi thế sau phí và thuế đủ bền vững.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **29. Active Share** nối từ **28. Quỹ chủ động và quỹ thụ động** sang **30. Direct Indexing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Active Share

Active Share đo mức danh mục chủ động khác benchmark về tỷ trọng. Nó không đo trực tiếp chất lượng.

Một quỹ có Active Share thấp nhưng phí cao có thể là “closet chỉ mục (index / 인덱스)”. Một quỹ Active Share cao có thể rất khác benchmark nhưng vẫn hoạt động kém.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **30. Direct Indexing** nối từ **29. Active Share** sang **31. Quỹ của quỹ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Direct Indexing

Đầu tư trực tiếp theo chỉ số (direct indexing) mua trực tiếp nhiều chứng khoán thay vì mua ETF. Nó có thể cho phép tùy chỉnh, loại trừ ngành hoặc quản lý thuế ở một số thị trường.

Đổi lại, cần công nghệ, vốn, nhiều giao dịch và quản trị hành động doanh nghiệp.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **31. Quỹ của quỹ** nối từ **30. Direct Indexing** sang **32. ETF theo chủ đề**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Quỹ của quỹ

Fund-of-funds nắm các quỹ khác. Nó đơn giản hóa phân bổ nhưng có thể tạo lớp phí, trùng lặp holdings và khó nhìn xuyên factor exposure.

Cần tính tổng chi phí tới tài sản cơ sở.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **32. ETF theo chủ đề** nối từ **31. Quỹ của quỹ** sang **33. Trùng lặp ẩn giữa các ETF**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. ETF theo chủ đề

ETF chủ đề thường có câu chuyện hấp dẫn nhưng dễ gặp:

```text
Định nghĩa chủ đề mơ hồ
Tỷ trọng doanh nghiệp thuần chủ đề thấp
Định giá cao sau khi xu hướng đã nổi tiếng
Tập trung ngành
Turnover cao
```

Nhãn marketing không phải định nghĩa kinh tế.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **33. Trùng lặp ẩn giữa các ETF** nối từ **32. ETF theo chủ đề** sang **34. Tổng chi phí sở hữu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Trùng lặp ẩn giữa các ETF

Hai ETF tên khác nhau có thể cùng nắm nhiều cổ phiếu lớn hoặc cùng mang beta công nghệ/tăng trưởng.

Nên phân tích holdings và factor exposure thay vì chỉ nhìn tên quỹ.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **34. Tổng chi phí sở hữu** nối từ **33. Trùng lặp ẩn giữa các ETF** sang **35. Checklist phân tích ETF**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Tổng chi phí sở hữu

Tổng chi phí không chỉ là expense ratio:

```text
Phí quản lý
Spread
Trượt giá
Tracking difference
Thuế
FX conversion / hedge
Securities lending economics
Chi phí cơ hội
```

Quỹ có phí quản lý thấp hơn chưa chắc cho lợi suất ròng tốt hơn.

> **Nối mạch:** Ở chặng này của **Cổ phiếu, ETF và quỹ đầu tư**, **35. Checklist phân tích ETF** nối từ **34. Tổng chi phí sở hữu** sang **36. Mô hình tư duy cuối cùng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Checklist phân tích ETF

Checklist này gom toàn bộ câu hỏi từ chỉ số, holdings và factor tới chi phí, FX, lending và hành vi khi căng thẳng. Hãy dùng nó sau khi hiểu cơ chế ETF, không dùng như danh sách kiểm tra tên sản phẩm đơn thuần.

```text
Chỉ số / chiến lược cơ sở
Phương pháp trọng số
Top holdings
Mức tập trung ngành/quốc gia
Factor exposure
Sao chép vật lý / tổng hợp
AUM
Spread
Thanh khoản tài sản cơ sở
Tracking difference / error
Phí / thuế
FX hedge
Lending
Hành vi trong giai đoạn căng thẳng
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cổ phiếu, ETF và quỹ đầu tư**, **36. Mô hình tư duy cuối cùng** tổng hợp từ **35. Checklist phân tích ETF** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Đi tiếp theo một đường duy nhất** mở rộng hệ quả hoặc giới hạn liên quan.

## 36. Mô hình tư duy cuối cùng

Sơ đồ cuối cùng bóc ETF thành từng lớp kinh tế: quyền sở hữu, quy tắc chỉ số, cấu trúc quỹ, cơ chế giao dịch và kết quả ròng sau chi phí. Hãy dùng nó để giải thích một ETF cụ thể bằng câu hoàn chỉnh trước khi chuyển sang chapter doanh nghiệp hoặc danh mục.

```text
Cổ phiếu → Quyền sở hữu / Dòng tiền / Pha loãng
Chỉ số → Quy tắc lựa chọn và trọng số
Quỹ → Cách quản lý
ETF → Cấu trúc giao dịch và tạo–mua lại
Kết quả thực → Tài sản cơ sở + FX + Chi phí + Thuế + Thực thi
```

Mục tiêu là nhìn xuyên lớp bao bì để hiểu chính xác mình đang sở hữu exposure nào và đang trả chi phí gì để sở hữu nó.

> **Nối mạch:** Trong **Cổ phiếu, ETF và quỹ đầu tư**, **Đi tiếp theo một đường duy nhất** tổng hợp từ **36. Mô hình tư duy cuối cùng** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Đi tiếp theo một đường duy nhất

Sau chapter này, không cần đọc thêm ETF ngay. Chọn một trong hai nhánh:

```text
Cổ phiếu doanh nghiệp
→ 03_company_analysis/01_FINANCIAL_STATEMENTS_AND_ACCOUNTING.md
→ 03_company_analysis/07_INTEGRATED_COMPANY_MODELING_AND_THESIS_LAB.md
→ STOCK_FOREX_RESEARCH_TEMPLATE.md

ETF / danh mục
→ 02_asset_classes/04_FACTORS_INDEXING_AND_MULTI_ASSET_BEHAVIOR.md
→ 02_asset_classes/05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md
→ 01_foundations/06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md
```

Nếu muốn xem bản đơn giản trước khi tự làm, dùng [Hồ sơ mẫu đã điền — Cổ phiếu xuất khẩu và Forex](../STOCK_FOREX_WORKED_EXAMPLE.md). Nếu muốn đi sâu, dùng [Advanced Practice Workbook — Module 3](../ADVANCED_PRACTICE_WORKBOOK.md).

> **Bàn giao:** Sau **Đi tiếp theo một đường duy nhất**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
