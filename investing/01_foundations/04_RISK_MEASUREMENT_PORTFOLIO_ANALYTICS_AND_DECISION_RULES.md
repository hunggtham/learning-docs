# Đo lường rủi ro, phân tích danh mục và quy tắc quyết định

> Chương này xây lớp định lượng cho quản trị danh mục. Mục tiêu không phải biến nhà đầu tư thành nhà thống kê, mà giúp hiểu các con số như CAGR, volatility, beta, Sharpe, VaR hay risk contribution đang đo điều gì, bỏ sót điều gì và nên được dùng thế nào trong quyết định thực tế.

## 1. Lợi suất đơn giản, lợi suất log và lợi suất hình học

Lợi suất đơn giản của một kỳ:

```text
R = Ending Value / Beginning Value - 1
```

Lợi suất log (log return) hữu ích trong một số mô hình thống kê vì có tính cộng theo thời gian, nhưng không nên thay thế trực giác về lợi suất thực tế của nhà đầu tư.

Lợi suất hình học phản ánh quá trình ghép lãi. Nếu danh mục tăng 50% rồi giảm 33,3%, tài sản quay về gần điểm xuất phát dù lợi suất số học trung bình vẫn dương.

## 2. CAGR và lợi suất thực

CAGR phản ánh tốc độ tăng trưởng kép hàng năm:

```text
CAGR = (Ending Value / Beginning Value)^(1/n) - 1
```

Lợi suất thực sau lạm phát:

```text
Real Return = (1 + Nominal Return) / (1 + Inflation) - 1
```

Đánh giá một chiến lược dài hạn nên nhìn cả CAGR, mức suy giảm và sức mua thực.

## 3. Time-Weighted Return và Money-Weighted Return

Lợi suất theo thời gian (Time-Weighted Return, TWR) loại ảnh hưởng của thời điểm nạp/rút tiền để đánh giá chiến lược hoặc nhà quản lý.

Lợi suất theo dòng tiền (Money-Weighted Return, MWR) phản ánh trải nghiệm thực của nhà đầu tư, vì thời điểm đóng/rút tiền ảnh hưởng kết quả.

Một quỹ có TWR tốt nhưng nhà đầu tư vào đúng đỉnh và rút đúng đáy vẫn có MWR kém.

## 4. Độ biến động là độ phân tán, không phải toàn bộ rủi ro

Độ biến động (volatility) thường được đo bằng độ lệch chuẩn của lợi suất. Nó cho biết mức dao động thông thường nhưng không trực tiếp cho biết xác suất phá sản, thiếu thanh khoản hay mất vốn vĩnh viễn.

Hai tài sản có cùng volatility nhưng một tài sản có phân phối cân đối, tài sản kia có nhiều khoản lời nhỏ và một khoản lỗ cực lớn. Rủi ro thực tế rất khác nhau.

## 5. Cụm biến động và thay đổi chế độ

Biến động tài chính thường có xu hướng tụ thành cụm: giai đoạn yên tĩnh nối tiếp giai đoạn yên tĩnh, giai đoạn căng thẳng nối tiếp căng thẳng.

Do đó dùng một mức volatility dài hạn cố định để sizing có thể đánh giá thấp rủi ro ngay khi chế độ thay đổi.

Nên xem thêm volatility gần đây, volatility trong giai đoạn xấu và kiểm thử kịch bản.

## 6. Mức suy giảm

Mức suy giảm (drawdown) đo khoảng giảm từ đỉnh trước đó. Maximum Drawdown là mức giảm sâu nhất trong giai đoạn quan sát.

Drawdown quan trọng vì ảnh hưởng tâm lý, nhu cầu thanh khoản và khả năng phục hồi kép.

```text
Mất 20% → cần +25%
Mất 50% → cần +100%
```

## 7. Thời gian phục hồi

Hai chiến lược có cùng mức suy giảm tối đa nhưng thời gian phục hồi rất khác nhau. Danh mục giảm 20% và hồi trong ba tháng khác đáng kể danh mục giảm 20% rồi mất năm năm mới quay lại đỉnh.

Vì vậy nên theo dõi cả độ sâu và thời gian nằm dưới đỉnh (time under water).

## 8. Hiệp phương sai và tương quan

Hiệp phương sai cho biết hai tài sản cùng biến động thế nào. Tương quan chuẩn hóa về khoảng `-1` tới `+1`.

```text
Correlation(A,B) = Cov(A,B) / (σA × σB)
```

Tương quan bình quân không đủ. Cần xem tương quan trượt theo thời gian, tương quan khi thị trường giảm và các giai đoạn khủng hoảng.

## 9. Phương sai danh mục

Với hai tài sản:

```text
σp² = wA²σA² + wB²σB² + 2wAwBσAσBρAB
```

Công thức cho thấy rủi ro danh mục không phải tổng cơ học rủi ro từng tài sản. Tương tác giữa các vị thế mới quyết định lợi ích đa dạng hóa.

## 10. Beta

Beta đo độ nhạy tương đối của tài sản so với benchmark:

```text
Beta = Cov(Rasset, Rbenchmark) / Var(Rbenchmark)
```

Beta > 1 nghĩa tài sản thường nhạy hơn thị trường trong dữ liệu quan sát, nhưng beta có thể thay đổi theo chế độ và không mô tả rủi ro nhảy giá hoặc thanh khoản.

## 11. Alpha phụ thuộc benchmark

Alpha là phần lợi suất không được giải thích bởi benchmark hoặc mô hình nhân tố đã chọn.

Nếu benchmark không phù hợp, alpha mất ý nghĩa. Ví dụ một danh mục cổ phiếu vốn hóa nhỏ không nên được đánh giá như thể toàn bộ phần vượt trội so với chỉ số vốn hóa lớn là kỹ năng lựa chọn cổ phiếu.

## 12. Sai lệch bám chỉ số và Information Ratio

Sai lệch bám chỉ số (Tracking Error) đo biến động của lợi suất chủ động so với benchmark.

```text
Information Ratio = Active Return / Tracking Error
```

Một chiến lược có lợi suất vượt trội cao nhưng tracking error cực lớn có thể có chất lượng kém hơn một chiến lược vượt trội vừa phải nhưng ổn định.

## 13. Active Share

Active Share đo mức danh mục khác với benchmark về tỷ trọng chứng khoán. Nó không trực tiếp đo hiệu quả hay rủi ro.

Active Share cao chỉ nói danh mục khác chỉ số nhiều. Muốn biết sự khác biệt đó có tạo giá trị hay không vẫn phải xem lợi suất, factor exposure và chi phí.

## 14. Sharpe Ratio

```text
Sharpe = (Rp - Rf) / σp
```

Sharpe cho biết phần lợi suất vượt lãi suất phi rủi ro trên mỗi đơn vị volatility. Nó hữu ích khi phân phối tương đối cân đối, nhưng có thể đánh giá cao chiến lược có đuôi lỗ lớn hoặc giá ít được cập nhật.

## 15. Sortino và Calmar

Sortino dùng độ lệch giảm giá thay vì tổng volatility.

Calmar thường so CAGR với Maximum Drawdown.

Hai chỉ số này gần trực giác của nhà đầu tư hơn trong một số trường hợp, nhưng vẫn không thay thế kiểm thử thanh khoản và đuôi phân phối.

## 16. Độ lệch và độ nhọn

Độ lệch (skewness) cho biết phân phối nghiêng về phía nào. Độ nhọn (kurtosis) giúp nhận diện mức độ đuôi dày.

Một chiến lược bán quyền chọn có thể có skew âm: nhiều khoản lời nhỏ và một số khoản lỗ lớn. Sharpe cao trong giai đoạn bình thường có thể che rủi ro này.

## 17. VaR

Giá trị chịu rủi ro (Value at Risk, VaR) trả lời câu hỏi dạng: “với mức tin cậy 95% trong một ngày, ngưỡng lỗ ước tính là bao nhiêu?”.

VaR không phải mức lỗ tối đa. 5% trường hợp ngoài ngưỡng có thể rất xấu.

Các cách ước lượng gồm lịch sử, tham số và mô phỏng Monte Carlo; mỗi cách có giả định riêng.

## 18. Expected Shortfall

Expected Shortfall tính tổn thất trung bình trong các trường hợp đã vượt VaR. Nó cung cấp thêm thông tin về phần đuôi nhưng vẫn phụ thuộc dữ liệu và mô hình.

Nếu dữ liệu chưa từng có một loại cú sốc nào, mô hình không tự biết cú sốc đó sẽ xảy ra.

## 19. Rủi ro thanh khoản

Rủi ro thanh khoản gồm spread mở rộng, độ sâu giảm, tác động thị trường và khả năng không thể thoát đúng quy mô mong muốn.

Một cách thực tế là so vị thế với giá trị giao dịch bình quân và ước lượng số ngày cần để giảm vị thế trong điều kiện bình thường lẫn căng thẳng.

## 20. Rủi ro nhảy giá

Rủi ro nhảy giá (gap risk) xuất hiện khi giá vượt qua mức stop mà không giao dịch ở các mức trung gian.

Nó quan trọng với earnings, dữ liệu vĩ mô, sự kiện địa chính trị, cổ phiếu ít thanh khoản và sản phẩm có giới hạn giá.

Stop-loss không loại bỏ gap risk.

## 21. Rủi ro đòn bẩy

Đòn bẩy làm tổn thất thị trường trở thành rủi ro tồn tại của tài khoản thông qua margin call và thanh lý.

Nên kiểm thử đồng thời:

```text
P/L trong kịch bản xấu
Yêu cầu ký quỹ sau khi biến động tăng
Thanh khoản tài sản bảo đảm
Khả năng bổ sung tiền
```

## 22. Rủi ro tập trung bằng HHI

Có thể dùng chỉ số Herfindahl–Hirschman (HHI) trên tỷ trọng vị thế như một thước đo đơn giản:

```text
HHI = Σ wi²
```

HHI càng cao thì mức tập trung vốn càng lớn. Tuy nhiên nó không nhìn thấy hai mã khác nhau cùng mang một nhân tố.

## 23. Số vị thế hiệu dụng

Một trực giác từ HHI:

```text
Effective Number of Positions ≈ 1 / HHI
```

Danh mục có 20 mã nhưng một mã chiếm 50% sẽ có số vị thế hiệu dụng thấp hơn nhiều so với con số 20.

## 24. Đóng góp rủi ro cận biên

Đóng góp rủi ro cận biên (Marginal Contribution to Risk, MCTR) hỏi tổng rủi ro danh mục thay đổi bao nhiêu nếu tăng nhẹ tỷ trọng một tài sản.

Đóng góp rủi ro thành phần (Component Risk Contribution) kết hợp MCTR với tỷ trọng để phân rã tổng rủi ro thành từng vị thế.

Đây là cách phát hiện một vị thế vốn nhỏ nhưng đang chi phối rủi ro.

## 25. Mức phơi nhiễm nhân tố

Rủi ro nên được phân rã theo các nhân tố như:

```text
Beta cổ phiếu
Duration
Chênh lệch tín dụng
USD / KRW / VND
Hàng hóa
Giá trị / Tăng trưởng
Động lượng
Thanh khoản
```

Nhiều mã chứng khoán có thể cùng chịu một nhân tố dù thuộc các quỹ khác nhau.

## 26. Biên hiệu quả và giới hạn của tối ưu hóa

Biên hiệu quả (efficient frontier) mô tả các tổ hợp có lợi suất kỳ vọng cao nhất cho một mức rủi ro nhất định theo giả định của mô hình.

Nhưng đầu vào lợi suất kỳ vọng, volatility và tương quan đều có sai số. Tối ưu hóa có thể phóng đại sai số nhỏ thành tỷ trọng cực đoan.

Vì vậy kết quả tối ưu phải được xem như công cụ hỗ trợ, không phải chân lý.

## 27. Co rút ước lượng và tối ưu hóa bền vững

Các kỹ thuật co rút (shrinkage) kéo ước lượng cực đoan về mức ổn định hơn. Tối ưu hóa bền vững (robust optimization) đặt giới hạn hoặc khoảng bất định để tránh danh mục quá nhạy với một con số đầu vào.

Trong thực tế, các ràng buộc đơn giản như tỷ trọng tối đa và ngân sách rủi ro thường giúp kết quả ổn định hơn.

## 28. Kiểm thử căng thẳng theo lịch sử

Có thể áp lại các giai đoạn như khủng hoảng ngân hàng, cú sốc lạm phát, bán tháo thanh khoản hoặc cú tăng USD.

Nhưng lịch sử không lặp chính xác. Mục tiêu là tìm độ nhạy chứ không giả định tương lai sẽ sao chép quá khứ.

## 29. Kịch bản giả định

Kịch bản giả định cho phép kết hợp nhiều biến:

```text
Cổ phiếu -20%
Lợi suất 10Y +80bp
Credit spread +150bp
USD +10%
Dầu +25%
Thanh khoản giảm một nửa
```

Đây thường là cách tốt hơn để kiểm tra các mối phụ thuộc mà dữ liệu bình thường không cho thấy.

## 30. Kiểm thử căng thẳng ngược

Kiểm thử ngược (reverse stress test) bắt đầu từ thất bại cần tránh:

> Điều gì phải xảy ra để danh mục buộc phải bán tài sản, vi phạm ký quỹ hoặc không đáp ứng được nghĩa vụ?

Sau đó truy ngược về các cú sốc có thể tạo trạng thái đó.

## 31. Quy tắc quyết định thay vì dự báo điểm

Thay vì dự báo chính xác “S&P sẽ tăng 8%”, có thể dùng quy tắc dạng:

```text
Nếu valuation vượt ngưỡng + earnings revisions xấu → giảm rủi ro vệ tinh
Nếu thanh khoản cá nhân dưới ngưỡng → dừng tăng tài sản rủi ro
Nếu một nhân tố vượt ngân sách rủi ro → tái cân bằng
Nếu thesis bị invalidation → đóng vị thế dù giá chưa giảm
```

Quy tắc giúp giảm phụ thuộc vào dự báo điểm và cảm xúc.

## 32. Tư duy xác suất và tỷ lệ cơ sở

Mọi dự báo nên được đặt cạnh tỷ lệ cơ sở (base rate). Nếu một loại doanh nghiệp có lịch sử thất bại cao, luận điểm “lần này khác” cần bằng chứng mạnh hơn.

Cập nhật xác suất khi có dữ liệu mới tốt hơn việc chuyển từ chắc chắn “bull” sang chắc chắn “bear”.

## 33. Bảng theo dõi rủi ro danh mục

Một bảng tối thiểu có thể gồm:

```text
Tỷ trọng
Đóng góp volatility
Beta
Duration / DV01 nếu có
FX exposure
Credit exposure
Thanh khoản
Maximum Drawdown lịch sử
Kịch bản stress
```

Mục tiêu là nhìn thấy rủi ro chung giữa các vị thế.

## 34. Mental model cuối cùng

```text
Lợi suất → Phân phối → Tương quan → Nhân tố → Thanh khoản → Đòn bẩy
→ Stress → Đóng góp rủi ro → Ngưỡng quyết định → Đánh giá lại
```

Định lượng không loại bỏ bất định. Nó giúp biến câu “tôi thấy danh mục có vẻ rủi ro” thành các giả định và ngưỡng có thể kiểm tra.