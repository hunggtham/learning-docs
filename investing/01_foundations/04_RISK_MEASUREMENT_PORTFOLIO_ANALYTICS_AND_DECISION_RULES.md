# Đo lường rủi ro, phân tích danh mục và quy tắc quyết định

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Lợi suất đơn giản, lợi suất log và lợi suất hình học** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. CAGR và lợi suất thực** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối risk measurement với portfolio analytics và decision rules, để biến biến động thành ngưỡng hành động có thể kiểm chứng.

> Chương này xây lớp định lượng cho quản trị danh mục. Mục tiêu không phải biến nhà đầu tư thành nhà thống kê, mà giúp hiểu các con số như CAGR, volatility, beta, Sharpe, VaR hay rủi ro (risk / 위험) contribution đang đo điều gì, bỏ sót điều gì và nên được dùng thế nào trong quyết định thực tế.

## 1. Lợi suất đơn giản, lợi suất log và lợi suất hình học

Lợi suất đơn giản của một kỳ:

```text
R = Ending Value / Beginning Value - 1
```

Lợi suất log (log return) hữu ích trong một số mô hình thống kê vì có tính cộng theo thời gian, nhưng không nên thay thế trực giác về lợi suất thực tế của nhà đầu tư.

Lợi suất hình học phản ánh quá trình ghép lãi. Nếu danh mục tăng 50% rồi giảm 33,3%, tài sản quay về gần điểm xuất phát dù lợi suất số học trung bình vẫn dương.

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **2. CAGR và lợi suất thực** tiếp nhận điểm tựa từ **1. Lợi suất đơn giản, lợi suất log và lợi suất hình học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Time-Weighted Return và Money-Weighted Return** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **3. Time-Weighted Return và Money-Weighted Return** tiếp nhận điểm tựa từ **2. CAGR và lợi suất thực** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Độ biến động là độ phân tán, không phải toàn bộ rủi ro** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Time-Weighted Return và Money-Weighted Return

Lợi suất theo thời gian (Time-Weighted Return, TWR) loại ảnh hưởng của thời điểm nạp/rút tiền để đánh giá chiến lược hoặc nhà quản lý.

Lợi suất theo dòng tiền (Money-Weighted Return, MWR) phản ánh trải nghiệm thực của nhà đầu tư, vì thời điểm đóng/rút tiền ảnh hưởng kết quả.

Một quỹ có TWR tốt nhưng nhà đầu tư vào đúng đỉnh và rút đúng đáy vẫn có MWR kém.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **4. Độ biến động là độ phân tán, không phải toàn bộ rủi ro** tiếp nhận điểm tựa từ **3. Time-Weighted Return và Money-Weighted Return** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Cụm biến động và thay đổi chế độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Độ biến động là độ phân tán, không phải toàn bộ rủi ro

Độ biến động (volatility) thường được đo bằng độ lệch chuẩn của lợi suất. Nó cho biết mức dao động thông thường nhưng không trực tiếp cho biết xác suất phá sản, thiếu thanh khoản hay mất vốn vĩnh viễn.

Hai tài sản có cùng volatility nhưng một tài sản có phân phối cân đối, tài sản kia có nhiều khoản lời nhỏ và một khoản lỗ cực lớn. Rủi ro thực tế rất khác nhau.

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **5. Cụm biến động và thay đổi chế độ** tiếp nhận điểm tựa từ **4. Độ biến động là độ phân tán, không phải toàn bộ rủi ro** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Mức suy giảm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Cụm biến động và thay đổi chế độ

Biến động tài chính thường có xu hướng tụ thành cụm: giai đoạn yên tĩnh nối tiếp giai đoạn yên tĩnh, giai đoạn căng thẳng nối tiếp căng thẳng.

Do đó dùng một mức volatility dài hạn cố định để sizing có thể đánh giá thấp rủi ro ngay khi chế độ thay đổi.

Nên xem thêm volatility gần đây, volatility trong giai đoạn xấu và kiểm thử kịch bản.

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **6. Mức suy giảm** tiếp nhận điểm tựa từ **5. Cụm biến động và thay đổi chế độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Thời gian phục hồi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Mức suy giảm

Mức suy giảm (drawdown) đo khoảng giảm từ đỉnh trước đó. Maximum Drawdown là mức giảm sâu nhất trong giai đoạn quan sát.

Drawdown quan trọng vì ảnh hưởng tâm lý, nhu cầu thanh khoản và khả năng phục hồi kép.

```text
Mất 20% → cần +25%
Mất 50% → cần +100%
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **7. Thời gian phục hồi** tiếp nhận điểm tựa từ **6. Mức suy giảm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Hiệp phương sai và tương quan** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Thời gian phục hồi

Hai chiến lược có cùng mức suy giảm tối đa nhưng thời gian phục hồi rất khác nhau. Danh mục giảm 20% và hồi trong ba tháng khác đáng kể danh mục giảm 20% rồi mất năm năm mới quay lại đỉnh.

Vì vậy nên theo dõi cả độ sâu và thời gian nằm dưới đỉnh (time under water).

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **8. Hiệp phương sai và tương quan** tiếp nhận điểm tựa từ **7. Thời gian phục hồi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Phương sai danh mục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Hiệp phương sai và tương quan

Hiệp phương sai cho biết hai tài sản cùng biến động thế nào. Tương quan chuẩn hóa về khoảng `-1` tới `+1`.

```text
Correlation(A,B) = Cov(A,B) / (σA × σB)
```

Tương quan bình quân không đủ. Cần xem tương quan trượt theo thời gian, tương quan khi thị trường giảm và các giai đoạn khủng hoảng.

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **9. Phương sai danh mục** tiếp nhận điểm tựa từ **8. Hiệp phương sai và tương quan** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Beta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Phương sai danh mục

Với hai tài sản:

```text
σp² = wA²σA² + wB²σB² + 2wAwBσAσBρAB
```

Công thức cho thấy rủi ro danh mục không phải tổng cơ học rủi ro từng tài sản. Tương tác giữa các vị thế mới quyết định lợi ích đa dạng hóa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **10. Beta** tiếp nhận điểm tựa từ **9. Phương sai danh mục** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Alpha phụ thuộc benchmark** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Beta

Beta đo độ nhạy tương đối của tài sản so với benchmark:

```text
Beta = Cov(Rasset, Rbenchmark) / Var(Rbenchmark)
```

Beta > 1 nghĩa tài sản thường nhạy hơn thị trường trong dữ liệu quan sát, nhưng beta có thể thay đổi theo chế độ và không mô tả rủi ro nhảy giá hoặc thanh khoản.

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **11. Alpha phụ thuộc benchmark** tiếp nhận điểm tựa từ **10. Beta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Sai lệch bám chỉ số và thông tin (information / 정보) Ratio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Alpha phụ thuộc benchmark

Alpha là phần lợi suất không được giải thích bởi benchmark hoặc mô hình nhân tố đã chọn.

Nếu benchmark không phù hợp, alpha mất ý nghĩa. Ví dụ một danh mục cổ phiếu vốn hóa nhỏ không nên được đánh giá như thể toàn bộ phần vượt trội so với chỉ số vốn hóa lớn là kỹ năng lựa chọn cổ phiếu.

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **12. Sai lệch bám chỉ số và thông tin (information / 정보) Ratio** tiếp nhận điểm tựa từ **11. Alpha phụ thuộc benchmark** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Active Share** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Sai lệch bám chỉ số và thông tin (information / 정보) Ratio

Sai lệch bám chỉ số (Tracking error) đo biến động của lợi suất chủ động so với benchmark.

```text
Information Ratio = Active Return / Tracking Error
```

Một chiến lược có lợi suất vượt trội cao nhưng tracking lỗi (error / 오류) cực lớn có thể có chất lượng kém hơn một chiến lược vượt trội vừa phải nhưng ổn định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **13. Active Share** tiếp nhận điểm tựa từ **12. Sai lệch bám chỉ số và thông tin (information / 정보) Ratio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Sharpe Ratio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Active Share

Active Share đo mức danh mục khác với benchmark về tỷ trọng chứng khoán. Nó không trực tiếp đo hiệu quả hay rủi ro.

Active Share cao chỉ nói danh mục khác chỉ số nhiều. Muốn biết sự khác biệt đó có tạo giá trị hay không vẫn phải xem lợi suất, factor exposure và chi phí.

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **14. Sharpe Ratio** tiếp nhận điểm tựa từ **13. Active Share** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Sortino và Calmar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Sharpe Ratio

Sharpe là bước đầu để so lợi suất vượt risk-free với volatility, nhưng không phải kết luận đầy đủ về chất lượng chiến lược. Trước khi dùng công thức, hãy xác định mẫu lợi suất, tần suất và các đuôi rủi ro có thể bị che khuất.

```text
Sharpe = (Rp - Rf) / σp
```

Sharpe cho biết phần lợi suất vượt lãi suất phi rủi ro trên mỗi đơn vị volatility. Nó hữu ích khi phân phối tương đối cân đối, nhưng có thể đánh giá cao chiến lược có đuôi lỗ lớn hoặc giá ít được cập nhật.

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **15. Sortino và Calmar** tiếp nhận điểm tựa từ **14. Sharpe Ratio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Độ lệch và độ nhọn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Sortino và Calmar

Sortino dùng độ lệch giảm giá thay vì tổng volatility.

Calmar thường so CAGR với Maximum Drawdown.

Hai chỉ số này gần trực giác của nhà đầu tư hơn trong một số trường hợp, nhưng vẫn không thay thế kiểm thử thanh khoản và đuôi phân phối.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **16. Độ lệch và độ nhọn** tiếp nhận điểm tựa từ **15. Sortino và Calmar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. VaR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Độ lệch và độ nhọn

Độ lệch (skewness) cho biết phân phối nghiêng về phía nào. Độ nhọn (kurtosis) giúp nhận diện mức độ đuôi dày.

Một chiến lược bán quyền chọn có thể có skew âm: nhiều khoản lời nhỏ và một số khoản lỗ lớn. Sharpe cao trong giai đoạn bình thường có thể che rủi ro này.

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **17. VaR** tiếp nhận điểm tựa từ **16. Độ lệch và độ nhọn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Expected Shortfall** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. VaR

Giá trị chịu rủi ro (value at risk, VaR) trả lời câu hỏi dạng: “với mức tin cậy 95% trong một ngày, ngưỡng lỗ ước tính là bao nhiêu?”.

VaR không phải mức lỗ tối đa. 5% trường hợp ngoài ngưỡng có thể rất xấu.

Các cách ước lượng gồm lịch sử, tham số và mô phỏng Monte Carlo; mỗi cách có giả định riêng.

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **18. Expected Shortfall** tiếp nhận điểm tựa từ **17. VaR** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Rủi ro thanh khoản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Expected Shortfall

Expected Shortfall tính tổn thất trung bình trong các trường hợp đã vượt VaR. Nó cung cấp thêm thông tin về phần đuôi nhưng vẫn phụ thuộc dữ liệu và mô hình.

Nếu dữ liệu chưa từng có một loại cú sốc nào, mô hình không tự biết cú sốc đó sẽ xảy ra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **19. Rủi ro thanh khoản** tiếp nhận điểm tựa từ **18. Expected Shortfall** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Rủi ro nhảy giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Rủi ro thanh khoản

Rủi ro thanh khoản gồm spread mở rộng, độ sâu giảm, tác động thị trường và khả năng không thể thoát đúng quy mô mong muốn.

Một cách thực tế là so vị thế với giá trị giao dịch bình quân và ước lượng số ngày cần để giảm vị thế trong điều kiện bình thường lẫn căng thẳng.

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **20. Rủi ro nhảy giá** tiếp nhận điểm tựa từ **19. Rủi ro thanh khoản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Rủi ro đòn bẩy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Rủi ro nhảy giá

Rủi ro nhảy giá (gap risk) xuất hiện khi giá vượt qua mức stop mà không giao dịch ở các mức trung gian.

Nó quan trọng với earnings, dữ liệu vĩ mô, sự kiện địa chính trị, cổ phiếu ít thanh khoản và sản phẩm có giới hạn giá.

Stop-loss không loại bỏ gap rủi ro (risk / 위험).

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **21. Rủi ro đòn bẩy** tiếp nhận điểm tựa từ **20. Rủi ro nhảy giá** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Rủi ro tập trung bằng HHI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Rủi ro đòn bẩy

Đòn bẩy làm tổn thất thị trường trở thành rủi ro tồn tại của tài khoản thông qua margin lời gọi (call / 호출) và thanh lý.

Nên kiểm thử đồng thời:

```text
P/L trong kịch bản xấu
Yêu cầu ký quỹ sau khi biến động tăng
Thanh khoản tài sản bảo đảm
Khả năng bổ sung tiền
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **22. Rủi ro tập trung bằng HHI** tiếp nhận điểm tựa từ **21. Rủi ro đòn bẩy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Số vị thế hiệu dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Rủi ro tập trung bằng HHI

Có thể dùng chỉ số Herfindahl–Hirschman (HHI) trên tỷ trọng vị thế như một thước đo đơn giản:

```text
HHI = Σ wi²
```

HHI càng cao thì mức tập trung vốn càng lớn. Tuy nhiên nó không nhìn thấy hai mã khác nhau cùng mang một nhân tố.

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **23. Số vị thế hiệu dụng** tiếp nhận điểm tựa từ **22. Rủi ro tập trung bằng HHI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Đóng góp rủi ro cận biên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Số vị thế hiệu dụng

Một trực giác từ HHI:

```text
Effective Number of Positions ≈ 1 / HHI
```

Danh mục có 20 mã nhưng một mã chiếm 50% sẽ có số vị thế hiệu dụng thấp hơn nhiều so với con số 20.

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **24. Đóng góp rủi ro cận biên** tiếp nhận điểm tựa từ **23. Số vị thế hiệu dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Mức phơi nhiễm nhân tố** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Đóng góp rủi ro cận biên

Đóng góp rủi ro cận biên (Marginal Contribution to risk, MCTR) hỏi tổng rủi ro danh mục thay đổi bao nhiêu nếu tăng nhẹ tỷ trọng một tài sản.

Đóng góp rủi ro thành phần (component risk Contribution) kết hợp MCTR với tỷ trọng để phân rã tổng rủi ro thành từng vị thế.

Đây là cách phát hiện một vị thế vốn nhỏ nhưng đang chi phối rủi ro.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **25. Mức phơi nhiễm nhân tố** tiếp nhận điểm tựa từ **24. Đóng góp rủi ro cận biên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Biên hiệu quả và giới hạn của tối ưu hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **25. Mức phơi nhiễm nhân tố** đã nêu tiêu chí phân biệt, còn **26. Biên hiệu quả và giới hạn của tối ưu hóa** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **27. Co rút ước lượng và tối ưu hóa bền vững** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Biên hiệu quả và giới hạn của tối ưu hóa

Biên hiệu quả (efficient frontier) mô tả các tổ hợp có lợi suất kỳ vọng cao nhất cho một mức rủi ro nhất định theo giả định của mô hình.

Nhưng đầu vào lợi suất kỳ vọng, volatility và tương quan đều có sai số. Tối ưu hóa có thể phóng đại sai số nhỏ thành tỷ trọng cực đoan.

Vì vậy kết quả tối ưu phải được xem như công cụ hỗ trợ, không phải chân lý.

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **26. Biên hiệu quả và giới hạn của tối ưu hóa** đã nêu tiêu chí phân biệt, còn **27. Co rút ước lượng và tối ưu hóa bền vững** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **28. Kiểm thử căng thẳng theo lịch sử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Co rút ước lượng và tối ưu hóa bền vững

Các kỹ thuật co rút (shrinkage) kéo ước lượng cực đoan về mức ổn định hơn. Tối ưu hóa bền vững (robust optimization) đặt giới hạn hoặc khoảng bất định để tránh danh mục quá nhạy với một con số đầu vào.

Trong thực tế, các ràng buộc đơn giản như tỷ trọng tối đa và ngân sách rủi ro thường giúp kết quả ổn định hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **28. Kiểm thử căng thẳng theo lịch sử** tiếp nhận điểm tựa từ **27. Co rút ước lượng và tối ưu hóa bền vững** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Kịch bản giả định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Kiểm thử căng thẳng theo lịch sử

Có thể áp lại các giai đoạn như khủng hoảng ngân hàng, cú sốc lạm phát, bán tháo thanh khoản hoặc cú tăng USD.

Nhưng lịch sử không lặp chính xác. Mục tiêu là tìm độ nhạy chứ không giả định tương lai sẽ sao chép quá khứ.

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **29. Kịch bản giả định** tiếp nhận điểm tựa từ **28. Kiểm thử căng thẳng theo lịch sử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Kiểm thử căng thẳng ngược** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **30. Kiểm thử căng thẳng ngược** tiếp nhận điểm tựa từ **29. Kịch bản giả định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Quy tắc quyết định thay vì dự báo điểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Kiểm thử căng thẳng ngược

Kiểm thử ngược (reverse stress test) bắt đầu từ thất bại cần tránh:

> Điều gì phải xảy ra để danh mục buộc phải bán tài sản, vi phạm ký quỹ hoặc không đáp ứng được nghĩa vụ?

Sau đó truy ngược về các cú sốc có thể tạo trạng thái đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **31. Quy tắc quyết định thay vì dự báo điểm** tiếp nhận điểm tựa từ **30. Kiểm thử căng thẳng ngược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Tư duy xác suất và tỷ lệ cơ sở** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Quy tắc quyết định thay vì dự báo điểm

Thay vì dự báo chính xác “S&P sẽ tăng 8%”, có thể dùng quy tắc dạng:

```text
Nếu valuation vượt ngưỡng + earnings revisions xấu → giảm rủi ro vệ tinh
Nếu thanh khoản cá nhân dưới ngưỡng → dừng tăng tài sản rủi ro
Nếu một nhân tố vượt ngân sách rủi ro → tái cân bằng
Nếu thesis bị invalidation → đóng vị thế dù giá chưa giảm
```

Quy tắc giúp giảm phụ thuộc vào dự báo điểm và cảm xúc.

> **Chuyển mạch:** Trong **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **32. Tư duy xác suất và tỷ lệ cơ sở** tiếp nhận điểm tựa từ **31. Quy tắc quyết định thay vì dự báo điểm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Bảng theo dõi rủi ro danh mục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Tư duy xác suất và tỷ lệ cơ sở

Mọi dự báo nên được đặt cạnh tỷ lệ cơ sở (base rate). Nếu một loại doanh nghiệp có lịch sử thất bại cao, luận điểm “lần này khác” cần bằng chứng mạnh hơn.

Cập nhật xác suất khi có dữ liệu mới tốt hơn việc chuyển từ chắc chắn “bull” sang chắc chắn “bear”.

> **Chuyển mạch:** Ở chặng này của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **33. Bảng theo dõi rủi ro danh mục** tiếp nhận điểm tựa từ **32. Tư duy xác suất và tỷ lệ cơ sở** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. mô hình tư duy (mental model / 사고 모델) cuối cùng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đo lường rủi ro, phân tích danh mục và quy tắc quyết định**, **34. mô hình tư duy (mental model / 사고 모델) cuối cùng** gom các mảnh từ **33. Bảng theo dõi rủi ro danh mục** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 34. mô hình tư duy (mental model / 사고 모델) cuối cùng

Sơ đồ này nối đo lường với quyết định: lợi suất tạo ra phân phối, phân phối tương tác qua correlation/factor, rồi thanh khoản, leverage và stress quyết định ngưỡng hành động. Hãy đọc nó như chuỗi review chứ không như danh sách thuật ngữ.

```text
Lợi suất → Phân phối → Tương quan → Nhân tố → Thanh khoản → Đòn bẩy
→ Stress → Đóng góp rủi ro → Ngưỡng quyết định → Đánh giá lại
```

Định lượng không loại bỏ bất định. Nó giúp biến câu “tôi thấy danh mục có vẻ rủi ro” thành các giả định và ngưỡng có thể kiểm tra.

> **Bàn giao:** Sau **34. mô hình tư duy (mental model / 사고 모델) cuối cùng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
