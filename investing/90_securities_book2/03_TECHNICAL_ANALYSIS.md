# 3. Phân tích kỹ thuật và giới hạn của tín hiệu

Sau khi bài 2 mô hình hóa giá trị, Sách 2 chuyển sang câu hỏi khác: giá đã vận động thế nào, và liệu chuỗi giá–khối lượng có cung cấp thông tin về xu hướng hoặc điểm ra quyết định không? Phân tích kỹ thuật (technical analysis / 기술적 분석) xử lý dữ liệu giao dịch; nó không thay thế phân tích dòng tiền. Mỗi tín hiệu dưới đây cần được đọc như một quy tắc mô tả có xác suất và chi phí sai, không như lời tiên tri.

## 1. Biểu đồ, xu hướng và vùng giá

Biểu đồ giá nén thời gian thành các quan sát mở cửa, cao nhất, thấp nhất, đóng cửa và khối lượng. Xu hướng tăng thường được mô tả bằng đỉnh sau cao hơn và đáy sau cao hơn; xu hướng giảm ngược lại; vùng đi ngang cho thấy cung–cầu cân bằng trong khoảng thời gian quan sát. Hỗ trợ và kháng cự (support/resistance / 지지선·저항선) là vùng có phản ứng giá, không phải đường vật lý bất biến. Khi giá phá vùng, cần kiểm tra khối lượng, thời gian duy trì và bối cảnh thị trường.

## 2. Moving average và crossover

Moving average (이동평균선) làm trơn nhiễu bằng trung bình các giá gần nhất. SMA cho trọng số bằng nhau; EMA cho trọng số lớn hơn ở quan sát mới. Crossover giữa đường ngắn và dài được dùng để mô tả thay đổi xu hướng, nhưng bản chất là tín hiệu trễ: dữ liệu phải xảy ra trước khi đường trung bình đổi hướng. Trong thị trường đi ngang, crossover tạo whipsaw; trong cú sốc nhanh, nó có thể bỏ lỡ phần lớn biến động. Quy tắc phải đi kèm stop, kích thước vị thế và chi phí giao dịch.

## 3. Mẫu hình giá

Mẫu hình chỉ có ý nghĩa khi giữ được quan hệ hình học và điều kiện xác nhận. Head-and-shoulders gồm vai trái, đầu, vai phải và neckline; phá neckline là điều kiện xác nhận theo textbook. Double top/bottom và triple top/bottom mô tả nỗ lực thất bại nhiều lần tại một vùng. Round top/bottom nhấn mạnh quá trình chuyển dần giữa bên mua và bên bán. Gap là khoảng trống giữa vùng giá liên tiếp; ý nghĩa phụ thuộc gap tiếp diễn hay gap kiệt sức.

Các mẫu tiếp diễn như flag, pennant, wedge và rectangle mô tả co hẹp sau một nhịp chuyển động. Source cũng nêu Diamond Pattern: biên dao động thường mở rộng rồi thu hẹp, nên cần đọc như sự chuyển từ bất định sang nén giá; hướng phá vỡ chỉ được xác nhận khi giá thoát khỏi biên cùng bối cảnh và khối lượng phù hợp. Đừng biến tên mẫu thành dự báo: cùng hình dạng có thể phá theo hướng khác nhau khi thanh khoản, tin tức hoặc regime đổi. Vì source có hình nhưng ảnh OCR không còn, learning edition giữ cấu trúc bằng prose thay vì bịa tọa độ hay mục tiêu giá.

### Source pattern inventory: không gộp các mẫu độc lập

Raw source tách các mẫu thành các unit riêng. Learning route giữ distinction tối thiểu sau để một mẫu bị thiếu không được che bởi chữ “patterns” chung:

| Mẫu | What / cơ chế | Điều kiện đọc | Boundary |
|---|---|---|---|
| Head-and-shoulders | ba đỉnh, đỉnh giữa cao hơn | neckline phải được phá/xác nhận | chưa phá neckline thì chưa hoàn tất mẫu |
| Double top | hai lần thất bại quanh vùng đỉnh | cần phá vùng đáy trung gian | hai đỉnh gần nhau tự nó chưa đủ |
| Double bottom | hai lần giữ được vùng đáy | cần phá vùng đỉnh trung gian | dễ nhầm với range |
| Triple top / bottom | ba lần kiểm tra cùng vùng | xác nhận vẫn dựa vào breakout | nhiều lần chạm không bảo đảm đảo chiều |
| Round top / bottom | chuyển dịch cung–cầu diễn ra từ từ | cần đọc cả độ dốc và bối cảnh xu hướng | không có một điểm trigger duy nhất |
| Gap | vùng giá không giao nhau giữa hai phiên/kỳ | phải phân biệt breakout/continuation/exhaustion context | tên gap không tự quyết định hướng tiếp theo |
| Flag | consolidation ngắn sau một nhịp mạnh | breakout khỏi kênh nhỏ | thất bại nếu breakout không giữ được |
| Pennant | co hẹp dạng tam giác sau impulse | breakout khỏi vùng nén | không đồng nhất với mọi triangle |
| Wedge | hai biên cùng hội tụ | hướng và vị trí trong trend quyết định cách đọc | rising/falling wedge không phải lệnh tự động |
| Rectangle | range với support/resistance tương đối ngang | breakout phải thoát khỏi range | trong range dễ tạo false break |
| Diamond | biên mở rộng rồi thu hẹp | chỉ xác nhận khi thoát biên | OCR figure không đủ để reconstruct target giá |

## 4. Candlestick chart (봉차트)

Candlestick biểu diễn quan hệ mở–đóng và biên độ trong một kỳ. Thân nến cho biết bên thắng tương đối, bóng nến cho biết giá bị từ chối ở đâu. Các nhóm như engulfing, doji, hammer, shooting star, harami và morning/evening star được dùng để nhận diện đảo chiều hoặc do dự. Một nến đơn không đủ; cần vị trí của nó trong xu hướng, nến xác nhận và khối lượng. Nếu bỏ bối cảnh, cùng một doji có thể chỉ là nhiễu.

Trong source, `Doji` được dùng cho trạng thái mở và đóng gần nhau; `Harami` là nến nhỏ nằm trong biên nến trước; `morning star` và `evening star` là các cụm ba nến thường được đọc như chuyển đổi giữa áp lực bán và mua. Cách reconstruct đúng là giữ cấu trúc nhiều nến và điều kiện xác nhận, không biến tên mẫu thành tín hiệu mua/bán tự động.

## 5. Chỉ báo kỹ thuật (technical indicators / 기술적 지표): động lượng và biến động

MACD so sánh các EMA để mô tả động lượng và giao cắt. RSI chuẩn hóa mức tăng/giảm gần đây thành dao động; vùng “quá mua/quá bán” không đồng nghĩa giá phải đảo chiều, vì xu hướng mạnh có thể duy trì lâu. Stochastic so sánh giá đóng cửa với biên độ gần đây. Bollinger Bands dùng trung bình và độ lệch chuẩn để tạo dải biến động; Envelope dùng khoảng cách phần trăm hoặc quy tắc tương tự. Dải mở rộng cho biết biến động tăng, không cho biết hướng.

OBV (On-Balance Volume) cộng/trừ khối lượng theo hướng đóng cửa để tìm xác nhận hoặc phân kỳ. Volume Ratio (VR) so sánh khối lượng tăng và giảm. Point-and-Figure lọc thời gian để tập trung vào chuyển động theo ngưỡng. Mỗi chỉ báo là phép biến đổi của cùng dữ liệu; dùng nhiều chỉ báo tương quan không tạo thêm độc lập thống kê.

### Công thức và biến cần theo dõi

Các chỉ báo trên không phải nhãn bí truyền; chúng là phép biến đổi có đầu vào rõ ràng:

| Chỉ báo | Dạng tính khái quát | Câu hỏi nó trả lời | Bẫy |
|---|---|---|---|
| SMA | `SMAₙ = (Pₜ + … + Pₜ₋ₙ₊₁)/n` | Giá trung bình đang dốc lên hay xuống? | Độ trễ, nhạy với cửa sổ `n` |
| EMA | `EMAₜ = αPₜ + (1−α)EMAₜ₋₁` | Dữ liệu mới đang đổi động lượng nhanh đến đâu? | `α` khác nhau cho tín hiệu khác nhau |
| RSI | `100 − 100/(1 + average gain/average loss)` | Mức tăng gần đây có áp đảo mức giảm không? | “Quá mua” không phải lệnh bán |
| MACD | `EMA nhanh − EMA chậm`; signal là EMA của MACD | Động lượng ngắn lệch động lượng dài thế nào? | Crossover trễ và nhiễu |
| Bollinger | `SMA ± k·độ lệch chuẩn` | Biến động đang co hay giãn quanh trung bình? | Dải rộng không cho biết hướng |
| OBV | tăng khối lượng khi giá tăng, giảm khi giá giảm | Khối lượng có xác nhận hướng giá không? | Phụ thuộc chất lượng volume |

Đọc bảng theo chuỗi `đầu vào → phép biến đổi → diễn giải → giới hạn`. Nếu thay cửa sổ hoặc nguồn giá, tín hiệu thay đổi; vì vậy không được so sánh hai backtest khi tham số và dữ liệu không cùng định nghĩa.

Trong các ví dụ của source, RSI thường được đọc quanh mốc 70/30 và Stochastic quanh 75/25; Bollinger dùng dải quanh SMA với hệ số độ lệch chuẩn thường là 2; Envelope đặt biên phần trăm cố định quanh SMA. MACD được đọc qua chênh lệch EMA nhanh–chậm, giao cắt với signal line và vị trí so với đường 0. Đây là tham số minh họa của textbook, không phải ngưỡng tự động đúng cho mọi tài sản, khung thời gian hay regime.

### VR và Point-and-Figure: volume và thời gian được xử lý khác nhau

Source tách `Volume Ratio (VR)` khỏi OBV dù cả hai đều dùng volume. Với quy ước thường thấy trong phần này, chia volume thành ngày tăng (`V↑`), ngày giảm (`V↓`) và ngày không đổi (`V=`):

```text
VR = [V↑ + 0,5 × V=] / [V↓ + 0,5 × V=] × 100
```

Nếu một cửa sổ có `V↑ = 600`, `V↓ = 200`, `V= = 200`, thì `VR = (600 + 100)/(200 + 100) × 100 ≈ 233,3%`. Con số này chỉ nói volume đi cùng các phiên tăng lớn hơn volume đi cùng các phiên giảm trong cửa sổ; nó không nói giá chắc chắn sẽ tăng tiếp. Khi mẫu số rất nhỏ, VR nhảy mạnh và dễ bị chi phối bởi một phiên bất thường. Các mốc 70%, 150% hay 450% xuất hiện trong ví dụ textbook phải được xem là ngưỡng minh họa; muốn dùng thật phải khóa cửa sổ, cách phân loại phiên không đổi và kiểm thử ngoài mẫu.

Point-and-Figure (P&F) xử lý khác: thay vì vẽ mọi đơn vị thời gian, nó chỉ ghi chuyển động đủ lớn để đi thêm một box và đổi cột khi đạt ngưỡng reversal. Vì vậy P&F có thể làm rõ vùng tích lũy/phân phối và mức phá vỡ, nhưng đồng thời bỏ qua thứ tự thời gian và gap trong quá trình lọc. Một biểu đồ P&F chỉ có ý nghĩa khi ghi rõ `box size`, `reversal amount`, nguồn giá (close hay high/low) và quy tắc xác nhận. Đổi box size hoặc reversal có thể biến cùng chuỗi giá thành cấu trúc khác; không được so sánh tín hiệu P&F giữa hai backtest nếu các tham số này không giống nhau.

VR và P&F minh họa hai dạng biến đổi dữ liệu: VR giữ thời gian nhưng gom volume theo hướng giá, còn P&F hy sinh thời gian để giữ các chuyển động vượt ngưỡng. Cả hai đều là bộ lọc quan sát, không phải bằng chứng nhân quả; cần nối với xu hướng, thanh khoản và chi phí thực thi trước khi tạo quy tắc giao dịch.

## 6. Dow và Elliott (엘리어트 파동이론)

Dow Theory (다우이론) đặt trọng tâm vào xu hướng chính, xu hướng phụ và dao động ngắn hơn; xác nhận giữa các chỉ số và khối lượng giúp tránh đọc một thị trường đơn lẻ. Elliott Wave diễn tả nhịp động lực và điều chỉnh lồng nhau. Vì việc gán nhãn sóng phụ thuộc cách đếm, nó cần được xem là kịch bản có điều kiện, không là bằng chứng duy nhất. Khi cấu trúc giá không thỏa điều kiện, phải bỏ nhãn thay vì ép dữ liệu vào lý thuyết.

Source cũng dùng nguyên lý sóng cùng dãy Fibonacci `1, 1, 2, 3, 5, 8, ...` và các tỷ lệ 38,2%, 61,8%, 1,618 và 2,618 để minh họa vùng điều chỉnh/mục tiêu. Các tỷ lệ này là mốc hình học được quan sát trong mô hình, không phải định luật cung–cầu. Chúng chỉ có giá trị khi gắn với cấu trúc đỉnh–đáy, điểm vô hiệu hóa và rủi ro vị thế.

## 7. Quy trình kiểm thử một tín hiệu

Trước khi dùng tín hiệu, ghi rõ: dữ liệu có sẵn tại thời điểm nào; quy tắc vào/ra; phí và trượt giá; regime nào làm tín hiệu thất bại; và benchmark nào để so sánh. Kiểm thử ngoài mẫu, tránh look-ahead và ghi nhật ký quyết định. Đây là chỗ nối tới [Systematic Risk, Backtest and Execution](../05_trading_derivatives/02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md), nơi phần phương pháp thuộc owner canonical được đào sâu.

## 8. Worked signal reading

Giả sử giá đóng cửa đi từ 100 → 102 → 101 → 103 → 104. SMA ba kỳ lần lượt chỉ được tính khi đủ ba quan sát: tại ngày 3 là `(100+102+101)/3 = 101`; tại ngày 4 là `(102+101+103)/3 ≈ 102`; tại ngày 5 là `(101+103+104)/3 ≈ 102,67`. Đường trung bình tăng, nhưng nó vẫn chậm hơn giá thật và không nói được cú tăng có bền không. Nếu dùng crossover, ngày bắt đầu tín hiệu phải được ghi rõ để không vô tình dùng dữ liệu tương lai.

Với một mẫu head-and-shoulders, quy trình đọc là: xác định ba đỉnh và hai đáy tương đối, vẽ neckline, đợi giá đóng cửa phá neckline, rồi kiểm tra khối lượng và điểm vô hiệu hóa. Nếu giá quay lại trên neckline, tín hiệu phá vỡ thất bại; không được giữ nguyên mục tiêu chỉ vì hình vẽ ban đầu trông đẹp. Với RSI hoặc Bollinger, cùng nguyên tắc áp dụng: chỉ báo tạo điều kiện quan sát, còn quyết định cần bối cảnh xu hướng và mức lỗ chấp nhận.

## 9. Phân biệt tín hiệu, quy tắc và lợi thế

Một tín hiệu là biến đổi dữ liệu; một quy tắc là tín hiệu cộng điều kiện vào/ra; một lợi thế là chênh lệch kỳ vọng còn lại sau chi phí và sai số. Ví dụ “RSI dưới 30” chỉ là tín hiệu. Quy tắc phải nói tài sản nào, khung thời gian nào, vào ở đâu, thoát khi nào và xử lý gap ra sao. Lợi thế chỉ được tin sau kiểm thử ngoài mẫu, phân tích độ nhạy tham số và kiểm tra turnover. Đây là boundary ngăn việc biến sách kỹ thuật thành danh sách indicator.

## 10. Đo lợi thế sau chi phí

Tỷ lệ thắng không đủ để kết luận một tín hiệu có lợi thế. Cần ghép xác suất, quy mô lời/lỗ và chi phí:

```
Expectancy = p_win × lợi nhuận trung bình − p_loss × lỗ trung bình − chi phí mỗi giao dịch
```

Ví dụ, một quy tắc thắng 45% số giao dịch, lời trung bình 3%, thua 55% với lỗ trung bình 2% và chịu chi phí 0,2% mỗi giao dịch có expectancy khoảng `0,45 × 3% − 0,55 × 2% − 0,2% = 0,05%`. Nếu bỏ chi phí, người học sẽ tưởng lợi thế là 0,25%, tức phóng đại gấp năm lần.

Expectancy dương trên mẫu nhỏ vẫn có thể là nhiễu. Vì vậy phải kiểm tra kích thước mẫu, khoảng tin cậy, thay đổi tham số, regime và kết quả ngoài mẫu; một indicator có expectancy tốt trong giai đoạn xu hướng không mặc nhiên sống được trong thị trường đi ngang. Đây là bước nối từ “tín hiệu” sang “quy tắc có thể chịu chi phí”.


## Chốt và bàn giao

Invariant là “tín hiệu kỹ thuật mô tả hành vi giá với độ trễ và xác suất; nó không tạo ra giá trị nội tại”. Bài 4 đặt tín hiệu vào chiến lược, danh mục và benchmark, rồi kiểm tra một chiến lược có sống được sau chi phí hay không. Xem [Chiến lược và chỉ số](./04_INVESTMENT_STRATEGIES_AND_INDICES.md).
