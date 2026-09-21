# Quyền chọn, bề mặt biến động, Greeks và phòng vệ

> Quyền chọn không chỉ là công cụ “đoán tăng hay giảm”. Giá quyền chọn phản ánh phân phối xác suất, thời gian, biến động và trạng thái thị trường. Chương này giải thích bằng tiếng Việt cách đọc quyền chọn theo sáu lớp: hướng giá, biến động, thời gian, độ lồi, thanh khoản và ký quỹ. Các thuật ngữ tiếng Anh được giữ trong ngoặc hoặc dưới dạng tên chuẩn như Delta, Gamma, Vega để tiện tra cứu.

# Phần I — Từ giá giao ngay tới giá kỳ hạn

## 1. Giá giao ngay và giá kỳ hạn

Giá quyền chọn không chỉ liên quan **giá giao ngay (spot)** mà còn liên quan **giá kỳ hạn (forward)** của tài sản cơ sở.

Giá kỳ hạn chịu ảnh hưởng bởi:

- lãi suất;
- cổ tức;
- chi phí vay tài sản;
- chi phí lưu kho hoặc lợi ích nắm giữ tùy loại tài sản.

## 2. Lợi ích hoặc chi phí nắm giữ

**Carry** là lợi ích hoặc chi phí kinh tế phát sinh khi giữ mức phơi nhiễm qua thời gian.

Với chỉ số cổ phiếu, lãi suất và cổ tức ảnh hưởng giá kỳ hạn. Với hàng hóa, chi phí lưu kho và **lợi ích tiện ích (convenience yield)** cũng quan trọng.

## 3. Độ gần tiền theo giá kỳ hạn

Khi phân tích chuyên sâu, trạng thái **gần tiền (moneyness)** nên được nhìn so với giá kỳ hạn trong nhiều trường hợp, không chỉ so giá thực hiện với giá giao ngay.

# Phần II — Giá quyền chọn và phân phối xác suất

## 4. Quyền chọn là khoản chi trả phụ thuộc trạng thái

Quyền chọn tạo khoản chi trả khác nhau tùy giá tài sản tại thời điểm đáo hạn.

```text
Call = max(S - K, 0)
Put  = max(K - S, 0)
```

Tính phi tuyến này tạo **độ lồi (convexity)**.

## 5. Biến động hàm ý

**Biến động hàm ý (implied volatility, IV)** là mức biến động khiến mô hình định giá khớp với giá quyền chọn trên thị trường.

IV không phải dự báo chắc chắn về biến động tương lai; nó là một đầu vào ngược suy ra từ giá.

## 6. Biến động thực hiện

**Biến động thực hiện (realized volatility)** là biến động thật xảy ra trong đường giá.

Một chiến lược biến động thường đặt cược vào quan hệ:

```text
Biến động hàm ý
so với
Biến động thực hiện trong tương lai
```

## 7. Phần bù rủi ro biến động

Trong nhiều thị trường, người mua bảo hiểm sẵn sàng trả phí cao để bảo vệ rủi ro đuôi. Vì vậy IV trung bình có thể cao hơn biến động thực hiện trung bình.

Khoảng này thường được gọi là **phần bù rủi ro biến động (volatility risk premium)**.

Nó không phải “tiền miễn phí”; người bán nhận phí để chịu rủi ro trong trạng thái xấu.

# Phần III — Greeks bậc một

## 8. Delta

Delta đo mức giá quyền chọn thay đổi khi giá tài sản cơ sở thay đổi một lượng nhỏ.

Delta cũng thường được dùng như xấp xỉ cho mức phơi nhiễm theo hướng giá, nhưng Delta thay đổi theo giá, thời gian và IV.

## 9. Gamma

Gamma đo mức Delta thay đổi khi giá tài sản cơ sở thay đổi.

```text
Mua quyền chọn → thường Gamma dương
Bán quyền chọn → thường Gamma âm
```

Gamma dương hưởng lợi khi giá di chuyển mạnh hơn kỳ vọng nếu phòng vệ Delta phù hợp. Gamma âm chịu rủi ro khi thị trường chạy mạnh.

## 10. Theta

Theta đo tốc độ mất giá trị theo thời gian nếu các yếu tố khác không đổi.

Người mua quyền chọn thường chịu hao mòn giá trị thời gian. Người bán thường thu Theta nhưng đổi lại chịu Gamma và rủi ro đuôi.

## 11. Vega

Vega đo độ nhạy với thay đổi IV.

Vega dương hưởng lợi khi IV tăng; Vega âm ngược lại.

## 12. Rho

Rho đo độ nhạy với lãi suất. Với quyền chọn ngắn hạn tác động thường nhỏ hơn Delta hoặc Vega, nhưng với kỳ hạn dài có thể đáng kể.

# Phần IV — Greeks bậc cao

## 13. Vanna

Vanna mô tả tương tác giữa Delta và biến động, giúp hiểu mức phơi nhiễm theo hướng giá thay đổi khi IV thay đổi.

## 14. Vomma / Volga

Vomma hoặc Volga đo độ cong của giá quyền chọn theo biến động, tức Vega thay đổi ra sao khi IV thay đổi.

## 15. Charm

Charm mô tả Delta thay đổi theo thời gian khi giá cơ sở giữ nguyên. Gần đáo hạn, hiệu ứng thời gian có thể tăng mạnh.

## 16. Không dùng một Greek riêng lẻ

Greeks là các độ nhạy cục bộ quanh trạng thái hiện tại. Khi thị trường nhảy giá lớn, cần dùng lưới kịch bản thay vì chỉ lấy Greek nhân với mức biến động.

# Phần V — Nụ cười và độ lệch biến động

## 17. IV không giống nhau ở mọi giá thực hiện

Trong thị trường thật, quyền chọn bán phía dưới và quyền chọn mua phía trên thường có IV khác nhau.

Đường IV theo giá thực hiện tạo **nụ cười biến động (volatility smile)** hoặc **độ lệch biến động (volatility skew)**.

## 18. Độ lệch ở chỉ số cổ phiếu

Chỉ số cổ phiếu thường có IV của quyền chọn bán ngoài tiền cao hơn vùng gần tiền vì nhu cầu bảo hiểm và rủi ro sụp giảm.

Đây thường được gọi là **độ lệch âm (negative skew)**.

## 19. Chênh lệch biến động mua–bán

**Risk reversal** so sánh IV của quyền chọn mua và quyền chọn bán có độ gần tiền tương ứng.

Chỉ số này giúp đọc sự bất đối xứng trong nhu cầu và nhận thức về rủi ro đuôi.

## 20. Độ cong cánh quyền chọn

**Độ cong (curvature/butterfly)** cho biết các quyền chọn rất xa tiền đắt hay rẻ so với vùng gần tiền, qua đó phản ánh nhu cầu bảo hiểm đuôi và hình dạng phân phối mà thị trường đang định giá.

# Phần VI — Cấu trúc biến động theo kỳ hạn

## 21. Biến động theo thời gian đáo hạn

IV khác nhau giữa các kỳ hạn tạo **cấu trúc kỳ hạn biến động (volatility term structure)**.

Một sự kiện gần có thể làm kỳ hạn ngắn tăng mạnh trong khi kỳ hạn dài ít thay đổi.

## 22. Biến động sự kiện

Báo cáo lợi nhuận, CPI, FOMC hoặc phán quyết pháp lý có thể tập trung bất định vào một thời điểm cụ thể.

Sau sự kiện, phần IV liên quan bất định đó thường giảm nhanh.

## 23. Chênh lệch lịch

**Chênh lệch lịch (calendar spread)** dùng quyền chọn cùng hoặc gần cùng giá thực hiện nhưng khác kỳ hạn.

Lãi/lỗ phụ thuộc cấu trúc kỳ hạn, đường đi của giá và tương quan Vega/Theta giữa hai chân.

# Phần VII — Bề mặt biến động

## 24. Bề mặt biến động là gì?

**Bề mặt biến động (volatility surface)** mô tả IV theo hai chiều chính:

```text
Giá thực hiện / độ gần tiền
×
Kỳ hạn
```

Bề mặt thay đổi liên tục khi giá, dòng lệnh và nhận thức rủi ro thay đổi.

## 25. Hai cách mô tả chuyển động bề mặt

**Bám giá thực hiện (sticky strike)** và **bám Delta (sticky delta)** là hai cách gần đúng để mô tả IV thay đổi khi giá cơ sở di chuyển.

Đây chỉ là mô hình gần đúng; hành vi thật có thể thay đổi theo chế độ.

## 26. Biến động của chính biến động

**Biến động của biến động (vol-of-vol)** đo mức IV bản thân nó biến động mạnh tới đâu.

Trong khủng hoảng, cả biến động giá và biến động của IV có thể cùng tăng.

# Phần VIII — Giao dịch Gamma có phòng vệ

## 27. Ý tưởng cơ bản

Người nắm Gamma dương có thể điều chỉnh Delta nhiều lần khi giá di chuyển.

Một mô tả đơn giản:

```text
Gamma dương
→ giá tăng → Delta tăng → bán bớt tài sản cơ sở để phòng vệ
→ giá giảm → Delta giảm → mua lại tài sản cơ sở để phòng vệ
```

Nếu biến động thực hiện đủ lớn so với phí quyền chọn và chi phí giao dịch, quá trình **giao dịch Gamma (gamma scalping)** có thể bù một phần hao mòn thời gian.

## 28. Không phải chênh lệch giá miễn phí

Kết quả phụ thuộc:

- biến động thực hiện;
- IV đã trả;
- tần suất phòng vệ;
- chênh lệch mua–bán;
- trượt giá;
- rủi ro nhảy giá.

# Phần IX — Phòng vệ Delta

## 29. Delta gần 0 không đồng nghĩa không rủi ro

Một vị thế Delta gần 0 vẫn có thể chịu:

- Gamma;
- Vega;
- Theta;
- độ lệch bề mặt;
- rủi ro nhảy giá.

Vì vậy “trung hòa Delta” chỉ mô tả một lớp rủi ro tại thời điểm hiện tại.

## 30. Phòng vệ động

Khi Delta thay đổi, vị thế phòng vệ phải được điều chỉnh. Phòng vệ quá thường làm chi phí tăng; phòng vệ quá ít làm rủi ro theo hướng giá tăng.

# Phần X — Thực hiện quyền, đáo hạn và rủi ro quanh giá thực hiện

## 31. Thực hiện quyền sớm

Quyền chọn kiểu Mỹ có thể bị thực hiện trước đáo hạn, đặc biệt quanh ngày cổ tức hoặc khi giá trị thời gian còn rất thấp.

## 32. Rủi ro pin

Nếu giá cơ sở ở sát giá thực hiện khi đáo hạn, trạng thái thực hiện quyền cuối cùng có thể không chắc chắn và tạo vị thế tài sản cơ sở ngoài ý muốn. Đây thường được gọi là **rủi ro pin (pin risk)**.

## 33. Khoảng nhảy qua đêm hoặc cuối tuần

Vị thế quyền chọn vẫn chịu rủi ro nhảy giá khi thị trường đóng cửa và không thể tái cân bằng Delta.

# Phần XI — Quy đổi Greeks thành giá trị tiền

## 34. Vì sao cần quy đổi?

Greek trên mỗi quyền chọn khó tổng hợp nếu danh mục có nhiều hệ số hợp đồng và số lượng khác nhau.

Có thể chuyển thành:

- Delta theo giá trị tiền;
- Gamma theo giá trị tiền;
- Vega theo giá trị tiền;
- DV01 với sản phẩm lãi suất.

Cách này giúp tổng hợp rủi ro danh mục.

## 35. Hệ số hợp đồng

Luôn nhân Greek với đúng hệ số hợp đồng và số lượng. Sai hệ số có thể làm ước lượng rủi ro sai hàng chục hoặc hàng trăm lần.

# Phần XII — Danh mục quyền chọn

## 36. Tổng hợp theo trạng thái tương lai

Không nên chỉ cộng Delta hiện tại. Hãy kiểm thử nhiều trạng thái:

```text
Giá cơ sở: -10%, -5%, 0, +5%, +10%
×
IV: giảm mạnh, không đổi, tăng mạnh
×
Thời gian: hôm nay / sau một tuần / gần đáo hạn
```

## 37. Lưới kịch bản

**Lưới kịch bản (scenario grid)** cho thấy tính phi tuyến rõ hơn một Greek duy nhất.

## 38. Rủi ro tương quan

Danh mục quyền chọn nhiều tài sản còn chịu rủi ro tương quan giữa các tài sản cơ sở. Sản phẩm “tệ nhất trong rổ” đặc biệt nhạy với tương quan.

# Phần XIII — Phòng vệ rủi ro đuôi

## 39. Mục tiêu của phòng vệ đuôi

**Phòng vệ đuôi (tail hedge)** nhằm giảm tổn thất trong trạng thái cực đoan, không nhất thiết tạo lợi nhuận mỗi tháng.

## 40. Chi phí bảo hiểm

Mua quyền chọn bán lặp lại tạo chi phí nắm giữ âm. Đánh giá phòng vệ cần theo nhiều năm và ở cấp toàn danh mục.

## 41. Ngân sách phòng vệ

Có thể định trước tỷ lệ phí quyền chọn hằng năm dành cho bảo vệ. Điều này tránh mua bảo hiểm quá nhiều sau khi IV đã tăng mạnh.

## 42. Chênh lệch quyền chọn bán

**Put spread** giảm phí bằng cách bán một quyền chọn bán có giá thực hiện thấp hơn, nhưng mức bảo vệ bị giới hạn khi thị trường giảm cực sâu.

## 43. Collar

**Collar** bán quyền chọn mua để tài trợ một phần quyền chọn bán, đổi lại giới hạn mức tăng giá phía trên.

# Phần XIV — Quyền chọn quanh sự kiện

## 44. Biến động giá hàm ý quanh sự kiện

Thị trường quyền chọn có thể được dùng để ước lượng mức biến động giá mà thị trường đang định giá quanh một sự kiện.

Nếu biến động thực tế nhỏ hơn mức đã được định giá, người mua quyền chọn vẫn có thể lỗ dù đoán đúng hướng.

## 45. Sụt IV sau sự kiện

Sau khi bất định biến mất, IV có thể giảm mạnh. Hiện tượng này thường được gọi là **IV crush**.

Lãi/lỗ của quyền chọn mua có thể được nhìn như:

```text
Lợi ích từ hướng giá
+/- ảnh hưởng Vega
- hao mòn Theta
- chi phí thực thi
```

## 46. Quyền chọn quanh báo cáo lợi nhuận

Báo cáo lợi nhuận tạo rủi ro nhảy giá và bất cân xứng thông tin. Kiểm thử chỉ dùng giá đóng cửa ngày trước–sau dễ đánh giá sai giá khớp và động học IV.

# Phần XV — Giao dịch độ lệch biến động

## 47. Độ lệch không chỉ là cược hướng

Mua quyền chọn bán đắt và bán quyền chọn mua rẻ có thể là cược vào bất đối xứng phân phối chứ không chỉ quan điểm giảm giá.

## 48. Độ lệch có thể dốc hơn khi căng thẳng

Khi nhu cầu bảo hiểm giảm giá tăng, IV của quyền chọn bán ngoài tiền có thể tăng nhanh hơn IV gần tiền. Khi đó lãi/lỗ của quyền chọn bán hưởng cả Delta và thay đổi độ lệch.

# Phần XVI — Rủi ro bán biến động

## 49. Thu Theta và chịu tổn thất đuôi

Vị thế bán quyền chọn thường có cấu trúc:

```text
Nhiều khoản lãi nhỏ
+ thỉnh thoảng một khoản lỗ rất lớn
```

Cần kiểm thử các biến động lớn hơn dữ liệu hằng ngày thông thường.

## 50. Ký quỹ tăng trong khủng hoảng

Khi biến động tăng, nhà môi giới hoặc tổ chức bù trừ có thể tăng yêu cầu ký quỹ đúng lúc vị thế bán quyền chọn đang lỗ.

Rủi ro lãi/lỗ và rủi ro thanh khoản vì vậy xuất hiện đồng thời.

# Phần XVII — Dữ liệu và kiểm thử quyền chọn

## 51. Dữ liệu quyền chọn phức tạp hơn dữ liệu giao ngay

Cần xử lý:

- giá thực hiện;
- kỳ hạn;
- giá mua/bán;
- báo giá cũ;
- hành động doanh nghiệp;
- thực hiện quyền sớm;
- hệ số hợp đồng;
- nội suy bề mặt biến động.

## 52. Thiên lệch dùng giá giữa

Kiểm thử dùng điểm giữa bid–ask cho mọi lệnh thường quá lạc quan, đặc biệt với quyền chọn ngoài tiền hoặc ít thanh khoản.

## 53. Chuỗi hợp đồng thay đổi liên tục

Chuỗi quyền chọn thay đổi theo ngày. Kiểm thử phải dùng đúng những hợp đồng thực sự tồn tại ở thời điểm lịch sử đó.

## 54. Ước lượng IV

Báo giá lỗi có thể tạo IV vô lý. Cần lọc dữ liệu và kiểm tra tính nhất quán với điều kiện không chênh lệch giá.

# Phần XVIII — Phòng vệ thực tế

## 55. Phòng vệ đúng nhân tố

```text
Beta cổ phiếu
→ futures chỉ số / quyền chọn bán

Rủi ro lãi suất
→ futures lãi suất / hoán đổi

Rủi ro FX
→ hợp đồng kỳ hạn / quyền chọn

Rủi ro biến động
→ quyền chọn / công cụ biến động
```

## 56. Rủi ro cơ sở

**Rủi ro cơ sở (basis risk)** xuất hiện khi công cụ phòng vệ không trùng hoàn toàn với tài sản cần bảo vệ.

Ví dụ phòng vệ cổ phiếu bán dẫn Hàn Quốc bằng Nasdaq futures chỉ giảm một phần beta công nghệ toàn cầu, không loại rủi ro riêng của công ty hoặc Hàn Quốc.

## 57. Phòng vệ quá mức

Phòng vệ quá lớn có thể biến danh mục thành vị thế ngược chiều thay vì chỉ giảm rủi ro.

## 58. Tái cân bằng phòng vệ

Delta hoặc beta thay đổi theo thị trường, vì vậy tỷ lệ phòng vệ phải được đánh giá lại định kỳ hoặc khi trạng thái thay đổi đủ lớn.

# Phần XIX — Phân rã lãi/lỗ

## 59. Lãi/lỗ quyền chọn nên được phân rã

Một khung thực tế:

```text
Ảnh hưởng Delta
Ảnh hưởng Gamma
Theta
Vega / thay đổi IV
Độ lệch / bề mặt
Lãi suất / carry
Chi phí thực thi
Phần còn lại
```

## 60. Đúng hướng nhưng sai công cụ

Nhà đầu tư có thể đoán đúng hướng giá nhưng vẫn lỗ vì trả IV quá cao, chịu hao mòn thời gian hoặc độ lệch biến động di chuyển bất lợi.

Đây là lý do “đúng thị trường” không đồng nghĩa “đúng giao dịch quyền chọn”.

# Phần XX — Quy trình quản trị vị thế quyền chọn

Trước khi mở vị thế, cần trả lời:

```text
Mình đang cược vào hướng giá, biến động hay cả hai?
IV hiện tại cao hay thấp so với lịch sử và sự kiện?
Rủi ro Gamma/Vega/Theta lớn nhất ở đâu?
Có thể bị thực hiện quyền sớm không?
Yêu cầu ký quỹ có thể tăng tới đâu?
Thanh khoản của hợp đồng thế nào?
Nếu giá nhảy mạnh, lưới kịch bản cho thấy gì?
Điều kiện vô hiệu hóa là gì?
```

## Kết luận

Quyền chọn là công cụ nhiều chiều. Một vị thế phải được hiểu đồng thời qua:

```text
Hướng giá
→ biến động
→ thời gian
→ độ lồi
→ bề mặt biến động
→ thanh khoản
→ ký quỹ
→ chi phí phòng vệ
```

Khi các lớp này được tách rõ, những thuật ngữ như Delta, Gamma, Vega hay skew trở thành nhãn kỹ thuật cho cơ chế đã hiểu, thay vì là từ tiếng Anh phải ghi nhớ riêng lẻ.