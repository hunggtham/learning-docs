# 3. Phân tích kỹ thuật và giới hạn của tín hiệu

Sau khi bài 2 mô hình hóa giá trị, Sách 2 chuyển sang câu hỏi khác: giá đã vận động thế nào, và liệu chuỗi giá–khối lượng có cung cấp thông tin về xu hướng hoặc điểm ra quyết định không? Phân tích kỹ thuật (technical analysis) xử lý dữ liệu giao dịch; nó không thay thế phân tích dòng tiền. Mỗi tín hiệu dưới đây cần được đọc như một quy tắc mô tả có xác suất và chi phí sai, không như lời tiên tri.

## 1. Biểu đồ, xu hướng và vùng giá

Biểu đồ giá nén thời gian thành các quan sát mở cửa, cao nhất, thấp nhất, đóng cửa và khối lượng. Xu hướng tăng thường được mô tả bằng đỉnh sau cao hơn và đáy sau cao hơn; xu hướng giảm ngược lại; vùng đi ngang cho thấy cung–cầu cân bằng trong khoảng thời gian quan sát. Hỗ trợ và kháng cự là vùng có phản ứng giá, không phải đường vật lý bất biến. Khi giá phá vùng, cần kiểm tra khối lượng, thời gian duy trì và bối cảnh thị trường.

## 2. Moving average và crossover

Moving average làm trơn nhiễu bằng trung bình các giá gần nhất. SMA cho trọng số bằng nhau; EMA cho trọng số lớn hơn ở quan sát mới. Crossover giữa đường ngắn và dài được dùng để mô tả thay đổi xu hướng, nhưng bản chất là tín hiệu trễ: dữ liệu phải xảy ra trước khi đường trung bình đổi hướng. Trong thị trường đi ngang, crossover tạo whipsaw; trong cú sốc nhanh, nó có thể bỏ lỡ phần lớn biến động. Quy tắc phải đi kèm stop, kích thước vị thế và chi phí giao dịch.

## 3. Mẫu hình giá

Mẫu hình chỉ có ý nghĩa khi giữ được quan hệ hình học và điều kiện xác nhận. Head-and-shoulders gồm vai trái, đầu, vai phải và neckline; phá neckline là điều kiện xác nhận theo textbook. Double top/bottom và triple top/bottom mô tả nỗ lực thất bại nhiều lần tại một vùng. Round top/bottom nhấn mạnh quá trình chuyển dần giữa bên mua và bên bán. Gap là khoảng trống giữa vùng giá liên tiếp; ý nghĩa phụ thuộc gap tiếp diễn hay gap kiệt sức.

Các mẫu tiếp diễn như flag, pennant, wedge và rectangle mô tả co hẹp sau một nhịp chuyển động. Đừng biến tên mẫu thành dự báo: cùng hình dạng có thể phá theo hướng khác nhau khi thanh khoản, tin tức hoặc regime đổi. Vì source có hình nhưng ảnh OCR không còn, learning edition giữ cấu trúc bằng prose thay vì bịa tọa độ.

## 4. Candlestick

Candlestick biểu diễn quan hệ mở–đóng và biên độ trong một kỳ. Thân nến cho biết bên thắng tương đối, bóng nến cho biết giá bị từ chối ở đâu. Các nhóm như engulfing, doji, hammer, shooting star, harami và morning/evening star được dùng để nhận diện đảo chiều hoặc do dự. Một nến đơn không đủ; cần vị trí của nó trong xu hướng, nến xác nhận và khối lượng. Nếu bỏ bối cảnh, cùng một doji có thể chỉ là nhiễu.

Trong source, `Doji` được dùng cho trạng thái mở và đóng gần nhau; `Harami` là nến nhỏ nằm trong biên nến trước; `morning star` và `evening star` là các cụm ba nến thường được đọc như chuyển đổi giữa áp lực bán và mua. Cách reconstruct đúng là giữ cấu trúc nhiều nến và điều kiện xác nhận, không biến tên mẫu thành tín hiệu mua/bán tự động.

## 5. Chỉ báo động lượng và biến động

MACD so sánh các EMA để mô tả động lượng và giao cắt. RSI chuẩn hóa mức tăng/giảm gần đây thành dao động; vùng “quá mua/quá bán” không đồng nghĩa giá phải đảo chiều, vì xu hướng mạnh có thể duy trì lâu. Stochastic so sánh giá đóng cửa với biên độ gần đây. Bollinger Bands dùng trung bình và độ lệch chuẩn để tạo dải biến động; Envelope dùng khoảng cách phần trăm hoặc quy tắc tương tự. Dải mở rộng cho biết biến động tăng, không cho biết hướng.

OBV (On-Balance Volume) cộng/trừ khối lượng theo hướng đóng cửa để tìm xác nhận hoặc phân kỳ. Volume Ratio (VR) so sánh khối lượng tăng và giảm. Point-and-Figure lọc thời gian để tập trung vào chuyển động theo ngưỡng. Mỗi chỉ báo là phép biến đổi của cùng dữ liệu; dùng nhiều chỉ báo tương quan không tạo thêm độc lập thống kê.

## 6. Dow và Elliott

Dow Theory đặt trọng tâm vào xu hướng chính, xu hướng phụ và dao động ngắn hơn; xác nhận giữa các chỉ số và khối lượng giúp tránh đọc một thị trường đơn lẻ. Elliott Wave diễn tả nhịp động lực và điều chỉnh lồng nhau. Vì việc gán nhãn sóng phụ thuộc cách đếm, nó cần được xem là kịch bản có điều kiện, không là bằng chứng duy nhất. Khi cấu trúc giá không thỏa điều kiện, phải bỏ nhãn thay vì ép dữ liệu vào lý thuyết.

Source cũng dùng nguyên lý sóng cùng dãy Fibonacci `1, 1, 2, 3, 5, 8, ...` và các tỷ lệ 38,2%, 61,8%, 1,618 và 2,618 để minh họa vùng điều chỉnh/mục tiêu. Các tỷ lệ này là mốc hình học được quan sát trong mô hình, không phải định luật cung–cầu. Chúng chỉ có giá trị khi gắn với cấu trúc đỉnh–đáy, điểm vô hiệu hóa và rủi ro vị thế.

## 7. Quy trình kiểm thử một tín hiệu

Trước khi dùng tín hiệu, ghi rõ: dữ liệu có sẵn tại thời điểm nào; quy tắc vào/ra; phí và trượt giá; regime nào làm tín hiệu thất bại; và benchmark nào để so sánh. Kiểm thử ngoài mẫu, tránh look-ahead và ghi nhật ký quyết định. Đây là chỗ nối tới [Systematic Risk, Backtest and Execution](../../investing/05_trading_derivatives/02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md), nơi phần phương pháp thuộc owner canonical được đào sâu.

## Chốt và bàn giao

Invariant là “tín hiệu kỹ thuật mô tả hành vi giá với độ trễ và xác suất; nó không tạo ra giá trị nội tại”. Bài 4 đặt tín hiệu vào chiến lược, danh mục và benchmark, rồi kiểm tra một chiến lược có sống được sau chi phí hay không. Xem [Chiến lược và chỉ số](./04_INVESTMENT_STRATEGIES_AND_INDICES.md).
