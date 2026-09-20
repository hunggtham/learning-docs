# Tình huống 02 — Truyền dẫn khủng hoảng tín dụng và thanh khoản

> Tình huống này phân biệt ba khái niệm thường bị trộn lẫn: **tổn thất thị trường (market loss)**, **căng thẳng thanh khoản (liquidity stress)** và **mất khả năng thanh toán về vốn (solvency problem)**. Mục tiêu là theo dõi cách một cú sốc nhỏ ở tài sản thế chấp hoặc nguồn vốn có thể biến thành giảm đòn bẩy cưỡng bức, co hẹp tín dụng, suy giảm lợi nhuận và cuối cùng tác động tới nền kinh tế thực.

## 1. Bối cảnh giả định

Giả sử một nhóm tổ chức tài chính nắm lượng lớn chứng khoán duration dài nhưng tài trợ bằng các nghĩa vụ ngắn hạn. Lãi suất chính sách đã tăng mạnh trong thời gian dài. Giá trị thị trường của tài sản giảm nhưng chưa nhất thiết tạo vỡ nợ vì dòng tiền hợp đồng vẫn có thể được thu nếu giữ tới đáo hạn.

Sau đó, tiền gửi bị rút nhanh hoặc nhu cầu bổ sung ký quỹ/tài sản thế chấp tăng đột ngột.

Câu hỏi trọng tâm không phải “tài sản đang lỗ bao nhiêu?”, mà là:

```text
Có đủ tiền mặt và tài sản thanh khoản để sống tới khi tài sản đáo hạn không?
```

Đây là khác biệt giữa lỗ theo giá thị trường và lỗ bị buộc phải hiện thực hóa.

## 2. Thanh khoản và khả năng thanh toán

**Vấn đề thanh khoản (liquidity problem)** xảy ra khi tổ chức có tài sản có thể đủ giá trị trong dài hạn nhưng không có đủ tiền ngay để đáp ứng rút tiền, thanh toán hoặc yêu cầu bổ sung tài sản bảo đảm.

**Vấn đề khả năng thanh toán (solvency problem)** xảy ra khi giá trị kinh tế của tài sản thấp hơn nghĩa vụ đủ lớn để vốn chủ sở hữu bị xóa mòn.

Một vấn đề thanh khoản có thể biến thành vấn đề khả năng thanh toán nếu tổ chức buộc phải bán tài sản ở mức giá rất thấp:

```text
Căng thẳng thanh khoản
→ Bán cưỡng bức
→ Giá tài sản giảm
→ Lỗ theo giá thị trường tăng
→ Niềm tin suy giảm
→ Rút tiền tăng
→ Rủi ro mất khả năng thanh toán tăng
```

Đọc thêm: [Hệ thống tiền tệ, thanh khoản và truyền dẫn khủng hoảng](../04_economics/04_MONETARY_SYSTEM_LIQUIDITY_AND_CRISIS_TRANSMISSION.md).

## 3. Chênh lệch kỳ hạn

Một tổ chức tài trợ ngắn hạn nhưng nắm tài sản duration dài chịu chênh lệch kỳ hạn (duration mismatch).

```text
Nghĩa vụ: tiền gửi có thể rút ngay / nguồn vốn ngắn hạn
Tài sản: trái phiếu 10 năm / khoản vay thế chấp dài hạn
```

Khi lãi suất tăng, giá trị thị trường của tài sản giảm. Nếu nguồn vốn ổn định, tổ chức có thể chờ. Nếu nguồn vốn rút đi, khoản lỗ phải được hiện thực hóa. Vì vậy rủi ro lãi suất có thể chuyển thành rủi ro thanh khoản.

## 4. Rút tiền gửi và niềm tin

Rút tiền gửi hàng loạt (deposit flight) có thể bắt đầu từ lo ngại về tiền gửi không được bảo hiểm, hiệu ứng lan truyền thông tin hoặc các khoản lỗ theo giá thị trường trở nên rõ ràng.

Ngân hàng số làm tốc độ rút tiền nhanh hơn nhiều so với trực giác về các cuộc rút tiền truyền thống. Vì vậy bộ đệm thanh khoản và mức tập trung nguồn tiền gửi rất quan trọng.

## 5. Repo và vòng xoáy haircut

Trong tài trợ có tài sản bảo đảm, bên cho vay thường áp dụng tỷ lệ chiết khấu tài sản thế chấp (haircut).

Nếu giá tài sản giảm hoặc biến động tăng:

```text
Haircut tăng
→ Người vay phải bổ sung tiền mặt/tài sản thế chấp
→ Bán tài sản tăng
→ Giá giảm thêm
→ Haircut tiếp tục tăng
```

Đây là vòng xoáy ký quỹ/haircut.

Đọc thêm: [Tiền mặt, thị trường tiền tệ và sản phẩm cấu trúc](../02_asset_classes/06_CASH_MONEY_MARKETS_STRUCTURED_PRODUCTS_AND_PRIVATE_MARKETS.md).

## 6. Giới hạn bảng cân đối của nhà tạo lập

Ngay cả khi một tài sản có vẻ rất rẻ, nhà tạo lập hoặc trung gian tài chính có thể không đủ khả năng hấp thụ vì giới hạn vốn, nguồn tài trợ hoặc hạn mức rủi ro.

Khi năng lực bảng cân đối giảm, chênh lệch mua bán mở rộng và độ sâu thị trường suy yếu. Giá có thể đi xa khỏi giá trị cơ bản vì trung gian không còn khả năng cung cấp thanh khoản.

Thanh khoản không chỉ là thuộc tính của tài sản; nó còn phụ thuộc vào sức khỏe bảng cân đối của những người tạo thị trường.

## 7. Chênh lệch tín dụng mở rộng

Khi bất định tăng, chênh lệch tín dụng (credit spread) có thể mở rộng do:

```text
Tổn thất vỡ nợ kỳ vọng tăng
Phần bù rủi ro tăng
Phần bù thanh khoản tăng
Bất định nguồn vốn tăng
```

Chênh lệch tín dụng rộng hơn làm tái cấp vốn đắt hơn, từ đó gây tác động vòng hai lên dòng tiền doanh nghiệp.

## 8. Bức tường đáo hạn nợ

Một doanh nghiệp có đòn bẩy hiện tại chưa cao vẫn có thể chịu căng thẳng nếu lượng lớn nợ đáo hạn trong thời gian ngắn.

Cần lập bản đồ:

```text
Tiền mặt
Hạn mức tín dụng dự phòng
Dòng tiền tự do
Lịch đáo hạn nợ
Khả năng vay có bảo đảm
Khoảng đệm covenant
Lãi suất tái cấp vốn
```

Đọc thêm: [Chất lượng lợi nhuận, mô hình và phân tích điều tra](../03_company_analysis/04_EARNINGS_QUALITY_MODELING_AND_FORENSICS.md).

## 9. Cơ chế khuếch đại tài chính

Điều kiện tín dụng có thể khuếch đại chu kỳ qua vòng phản hồi:

```text
Giá tài sản giảm
→ Giá trị tài sản thế chấp giảm
→ Tiêu chuẩn cho vay chặt hơn
→ Vay vốn và đầu tư giảm
→ Tăng trưởng giảm
→ Lợi nhuận giảm
→ Chất lượng tín dụng xấu đi
→ Cho vay tiếp tục bị siết
```

Đây là cơ chế khuếch đại tài chính (financial accelerator). Một cú sốc ban đầu ở một thị trường nhỏ vẫn có thể trở thành suy thoái rộng hơn nếu nó đi qua kênh tín dụng.

## 10. Vốn ngân hàng và thanh khoản ngân hàng

Vốn dùng để hấp thụ tổn thất. Thanh khoản dùng để đáp ứng dòng tiền ra. Hai vấn đề khác nhau.

Một ngân hàng có tỷ lệ vốn cao vẫn có thể gặp khủng hoảng nếu dòng tiền rút quá nhanh và tài sản khó bán. Ngược lại, ngân hàng trung ương có thể cung cấp thanh khoản nhưng không thể xóa tổn thất kinh tế nếu giá trị tài sản thực sự thấp hơn nợ.

## 11. Công cụ hỗ trợ thanh khoản của ngân hàng trung ương

Ngân hàng trung ương có thể cho vay dựa trên tài sản đủ điều kiện để giảm nhu cầu bán tháo:

```text
Chấp nhận tài sản thế chấp
→ Cung cấp tiền mặt
→ Giảm nhu cầu bán cưỡng bức
→ Ổn định thị trường nguồn vốn
```

Nhưng hỗ trợ thanh khoản không xóa rủi ro tín dụng. Nếu người vay cuối cùng vỡ nợ, tổn thất kinh tế vẫn tồn tại.

## 12. Người cho vay cuối cùng và cứu trợ vốn

**Người cho vay cuối cùng (lender of last resort)** chủ yếu cung cấp thanh khoản tạm thời dựa trên tài sản thế chấp.

**Cứu trợ hoặc tái cấp vốn (bailout/recapitalization)** bổ sung vốn hấp thụ lỗ hoặc chuyển rủi ro sang khu vực công.

Hai biện pháp có tác động phân phối và tài khóa khác nhau. Không nên gọi mọi can thiệp là QE hoặc “in tiền”.

## 13. Vòng xoáy ngân hàng–chính phủ

Ngân hàng thường nắm trái phiếu chính phủ, trong khi chính phủ dựa vào hệ thống ngân hàng để tài trợ nền kinh tế. Trong căng thẳng:

```text
Rủi ro chính phủ tăng
→ Giá trị tài sản ngân hàng giảm
→ Chi phí vốn ngân hàng tăng
→ Tín dụng giảm
→ Kinh tế yếu đi
→ Tình hình tài khóa xấu hơn
→ Rủi ro chính phủ tiếp tục tăng
```

Đây là vòng xoáy ngân hàng–chính phủ (sovereign-bank doom loop).

## 14. Trái phiếu doanh nghiệp và trái phiếu chính phủ

Trong khủng hoảng tín dụng đi kèm suy thoái, lợi suất trái phiếu chính phủ có thể giảm do kỳ vọng nới lỏng và nhu cầu trú ẩn, trong khi chênh lệch tín dụng doanh nghiệp mở rộng mạnh.

Lợi suất trái phiếu doanh nghiệp có thể phân rã gần đúng thành:

```text
Tác động lãi suất
+ Tác động chênh lệch tín dụng
+ Thu nhập nắm giữ
+ Vỡ nợ / Thu hồi
```

Trái phiếu chính phủ tăng giá không đảm bảo trái phiếu doanh nghiệp cũng tăng.

## 15. Truyền dẫn sang cổ phiếu

Cổ phiếu tài chính thường chịu tác động trực tiếp qua nguồn vốn và tổn thất tín dụng. Tác động vòng hai có thể lan sang bất động sản qua tái cấp vốn, doanh nghiệp công nghiệp qua giảm capex, tiêu dùng qua tín dụng chặt hơn, doanh nghiệp nhỏ qua phụ thuộc nguồn vốn và công ty chứng khoán qua thanh khoản/margin.

Lập bản đồ ngành phải dựa trên độ nhạy bảng cân đối chứ không chỉ beta lịch sử.

## 16. Truyền dẫn vào lợi nhuận doanh nghiệp

Một chuỗi thường gặp:

```text
Doanh thu chậm lại
→ Biên lợi nhuận giảm
→ Vốn lưu động xấu đi
→ Dòng tiền hoạt động giảm
→ Chi phí lãi vay tăng
→ Khoảng đệm covenant giảm
→ Cắt capex / Bán tài sản / Pha loãng vốn
```

Kế toán có thể phản ánh chậm hơn căng thẳng thanh khoản. Bảng cân đối thường cho cảnh báo sớm hơn EPS.

## 17. Tín dụng tư nhân và độ trễ định giá

NAV của tín dụng tư nhân hoặc vốn cổ phần tư nhân có thể chưa giảm nhanh như tài sản niêm yết. Đường giá “mượt” không có nghĩa rủi ro kinh tế thấp.

Các tín hiệu cần chú ý gồm PIK tăng, gia hạn và sửa điều khoản, EBITDA add-back tăng, nới covenant, mức chiết khấu trên thị trường thứ cấp và thời gian thoái vốn kéo dài.

## 18. Giảm đòn bẩy cưỡng bức

Quỹ hoặc nhà giao dịch dùng đòn bẩy có thể phải bán cả tài sản không liên quan để đáp ứng margin call. Vì vậy tài sản chất lượng tốt đôi khi cũng giảm mạnh ở giai đoạn đầu khủng hoảng.

Tương quan tăng đột biến có thể phản ánh nhu cầu tiền mặt, không nhất thiết phản ánh thay đổi cơ bản của mọi tài sản.

## 19. Vàng và tiền mặt trong cú sốc thanh khoản

Vàng có vai trò trú ẩn nhưng vẫn có thể giảm tạm thời khi nhà đầu tư cần tiền mặt. USD và T-bill có thể hưởng lợi từ nhu cầu thanh khoản tùy nguồn gốc cú sốc.

Không nên dùng phản ứng một ngày để kết luận một công cụ phòng vệ “không hoạt động”. Cần phân biệt giai đoạn bán tháo đầu tiên và giai đoạn phản ứng chính sách sau đó.

## 20. Truyền dẫn tới Hàn Quốc

Một cú siết nguồn vốn USD toàn cầu có thể truyền nhanh qua Hàn Quốc:

```text
Căng thẳng nguồn vốn USD
→ USD/KRW tăng
→ Nhà đầu tư nước ngoài giảm rủi ro
→ Cổ phiếu và tín dụng chịu áp lực
→ Điều kiện huy động vốn doanh nghiệp chặt hơn
```

Doanh nghiệp xuất khẩu có doanh thu USD nhưng tác động lên vốn lưu động và tài trợ khác nhau theo từng công ty.

## 21. Truyền dẫn tới Việt Nam

Việt Nam có kênh khác:

```text
Tâm lý tránh rủi ro toàn cầu / USD tăng
→ VND chịu áp lực
→ Dư địa chính sách giảm
→ Kỳ vọng thanh khoản nội địa yếu đi
→ Bất động sản / Chứng khoán / Ngân hàng bị định giá lại
```

Tín dụng ngân hàng trong nước, tái cấp vốn trái phiếu bất động sản và margin bán lẻ có thể chi phối thị trường nội địa.

## 22. Đánh giá các tầng thanh khoản của danh mục

Kiểm thử danh mục không chỉ hỏi lỗ theo giá thị trường. Cần hỏi:

```text
Cần bao nhiêu tiền mặt trong 1 tháng tới?
Margin call có thể lớn tới đâu?
Tài sản nào bán được trong ngày?
Tài sản nào có thể gap hoặc bị khóa giá sàn?
Tài sản nào bị khóa hoặc thuộc thị trường tư nhân?
Chuyển tiền xuyên biên giới có thể chậm ở đâu?
```

Thanh khoản phải là một phần của ngân sách rủi ro.

## 23. Kiểm thử căng thẳng ngược

Thay vì chỉ hỏi “danh mục mất bao nhiêu nếu cổ phiếu giảm 20%?”, hãy hỏi:

> Điều gì phải xảy ra để tôi buộc phải bán tài sản tốt ở đáy?

Các nguyên nhân có thể gồm mất thu nhập, margin call, trả nợ, gọi vốn từ quỹ tư nhân, lệch tiền tệ hoặc sự cố môi giới/lưu ký.

## 24. Thiết kế phòng vệ

Nếu rủi ro là duration lãi suất, cần công cụ phòng vệ duration. Nếu rủi ro là chênh lệch tín dụng tăng mạnh, chỉ phòng vệ bằng trái phiếu chính phủ sẽ không bù hết tổn thất. Nếu rủi ro là khủng hoảng thanh khoản, giữ tiền mặt hoặc T-bill có thể có giá trị hơn một cấu trúc phái sinh phức tạp cần bổ sung ký quỹ.

Một công cụ phòng vệ có thể thất bại về vận hành ngay cả khi hướng kinh tế đúng.

## 25. Quyền chọn bảo hiểm trong khủng hoảng

Put mua trước có độ lồi giúp bảo vệ đuôi, nhưng biến động ngụ ý thường rất đắt sau khi căng thẳng đã bắt đầu. Mua bảo hiểm khi “đám cháy” đã bùng lên thường tốn kém.

Phòng vệ đuôi nên được xem như ngân sách bảo hiểm định kỳ của danh mục, không phải một giao dịch ứng biến ở đỉnh hoảng loạn.

## 26. Thực thi trong căng thẳng

Đặc điểm thực thi khi thị trường căng thẳng:

```text
Chênh lệch mua bán rộng hơn
Độ sâu thấp hơn
Trượt giá lớn hơn
Tương quan cao hơn
Stop có thể gap
Yêu cầu ký quỹ tăng
```

Quy mô vị thế trước khủng hoảng quan trọng hơn việc cố tìm một điểm thoát hoàn hảo trong khủng hoảng.

## 27. Điều gì đã nằm trong giá?

Phân tích khủng hoảng tín dụng phải so mức chênh lệch hiện tại và giá cổ phiếu với đường đi tổn thất mà thị trường đang kỳ vọng.

Một doanh nghiệp có thể rất yếu nhưng trái phiếu đã phản ánh xác suất vỡ nợ sâu. Một doanh nghiệp khác có vẻ ổn định nhưng chênh lệch tín dụng vẫn ở mức quá hẹp. Lợi thế nằm ở phân phối kết quả so với giá, không nằm ở nhãn “tốt/xấu”.

## 28. Dòng thời gian khủng hoảng

```text
Giai đoạn 1: Tích tụ đòn bẩy / lệch kỳ hạn
Giai đoạn 2: Tác nhân kích hoạt
Giai đoạn 3: Căng thẳng nguồn vốn / thanh khoản
Giai đoạn 4: Bán cưỡng bức / chênh lệch tín dụng mở rộng
Giai đoạn 5: Co hẹp tín dụng
Giai đoạn 6: Lợi nhuận / việc làm suy yếu
Giai đoạn 7: Phản ứng chính sách
Giai đoạn 8: Sửa chữa bảng cân đối / tái cấp vốn / vỡ nợ
```

Các tài sản tạo đáy ở những giai đoạn khác nhau. Giá thị trường thường đi trước dữ liệu kế toán.

## 29. Phân rã sau khủng hoảng

Cần đánh giá lại:

```text
Có nhận ra kênh nguồn vốn đủ sớm không?
Có nhầm thanh khoản với khả năng thanh toán không?
Chỉ báo bảng cân đối nào đi trước giá cổ phiếu?
Công cụ phòng vệ nào thực sự hiệu quả sau chi phí và ký quỹ?
Đa dạng hóa có thất bại vì các nhân tố hội tụ không?
Phản ứng chính sách có lớn hoặc nhanh hơn dự kiến không?
```

## 30. Checklist dùng lại

```text
Tác nhân kích hoạt
Nguồn vốn
Tài sản thế chấp
Haircut / Ký quỹ
Bộ đệm thanh khoản
Bộ đệm vốn
Lịch đáo hạn
Chênh lệch tín dụng
Tiêu chuẩn cho vay ngân hàng
Nguồn vốn FX
Công cụ chính sách
Dư địa tài khóa
Bên bán cưỡng bức
Thanh khoản danh mục
```

## Kết luận

Khủng hoảng tín dụng không bắt đầu và kết thúc ở một “ngân hàng xấu”. Nó là vấn đề mạng lưới giữa đòn bẩy, tài sản thế chấp, nguồn vốn, niềm tin và chính sách. Nhà đầu tư cần nhìn bảng cân đối và thời điểm dòng tiền trước khi nhìn P/E tiêu đề. Trong khủng hoảng, **khả năng sống sót, thanh khoản và quyền lựa chọn** thường quan trọng hơn việc tối đa hóa lợi suất kỳ vọng.