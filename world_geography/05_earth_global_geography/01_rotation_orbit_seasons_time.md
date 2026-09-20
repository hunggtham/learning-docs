# Chuyển động quay, quỹ đạo, mùa và thời gian

## Hai chuyển động nền tảng

Trái Đất vừa **tự quay quanh trục** vừa chuyển động quanh Mặt Trời. Chuyển động quay tạo chu kỳ ngày–đêm, ảnh hưởng Coriolis và là nền hình học của kinh độ–thời gian. Chuyển động quỹ đạo kết hợp với độ nghiêng trục tạo mùa.

Một hiểu lầm phổ biến là mùa hè xảy ra vì Trái Đất “gần Mặt Trời hơn”. Nguyên nhân chính là **độ nghiêng trục (axial tilt)** khoảng 23,4° làm góc chiếu và thời lượng ban ngày thay đổi theo mùa. Khi Bắc bán cầu nghiêng về phía Mặt Trời, tia sáng tới trực diện hơn và ngày dài hơn; Nam bán cầu đồng thời trải qua mùa ngược lại.

Khoảng cách Trái Đất–Mặt Trời vẫn biến đổi vì quỹ đạo hơi elip, nhưng hiệu ứng này nhỏ hơn tác động của độ nghiêng đối với mùa ở vĩ độ trung bình và cao.

## Ngày Mặt Trời và ngày sao

Nếu đo Trái Đất quay so với các sao xa, một vòng quay hoàn tất hơi ngắn hơn 24 giờ. Nhưng trong thời gian đó Trái Đất cũng đã đi một đoạn trên quỹ đạo, nên cần quay thêm một góc nhỏ để Mặt Trời trở lại cùng kinh tuyến. Khoảng 24 giờ dân sự gần với **ngày Mặt Trời trung bình (mean solar day)**.

Sự khác nhau này cho thấy thời gian không tách rời hình học thiên văn. Hệ giờ hiện đại dùng đồng hồ nguyên tử và UTC để tạo thang thời gian ổn định, trong khi chuyển động quay thực của Trái Đất có dao động nhỏ.

## Vĩ độ và độ dài ngày

Gần Xích đạo, độ dài ngày ít thay đổi trong năm. Càng về cực, biên độ mùa của thời lượng chiếu sáng càng lớn. Trong vòng cực có thể xuất hiện **ngày cực** và **đêm cực**. Điều này ảnh hưởng nhiệt, sinh thái, nhịp sống, thiết kế năng lượng Mặt Trời và mùa du lịch.

Cùng lượng bức xạ ngày không có nghĩa cùng nhiệt độ tức thời. Đại dương, tuyết–băng, mây và nhiệt dung bề mặt làm hệ có quán tính; vì thế thời điểm nóng nhất thường trễ hơn hạ chí và lạnh nhất trễ hơn đông chí.

## Kinh độ, giờ địa phương và múi giờ

Về hình học, 360° quay trong khoảng 24 giờ tương ứng gần 15° kinh độ mỗi giờ. Nhưng **múi giờ dân sự** là sản phẩm của cả địa lý và thể chế: ranh giới được điều chỉnh theo quốc gia, vùng hành chính và nhu cầu kinh tế. Vì vậy không thể suy múi giờ chính xác chỉ từ kinh độ.

**Đường đổi ngày quốc tế** cũng là quy ước. Nó gần kinh tuyến 180° nhưng uốn để tránh chia cắt một số lãnh thổ và nhóm đảo. Khi vượt đường này, nhãn ngày thay đổi dù thời gian vật lý không “nhảy”.

## Tiến động và các chu kỳ dài

Trục quay không giữ hướng tuyệt đối mãi mãi. **Tiến động (precession)** làm hướng trục thay đổi chậm trong hàng chục nghìn năm; độ nghiêng và độ lệch tâm quỹ đạo cũng biến đổi. Các chu kỳ thiên văn này thay đổi phân bố bức xạ theo mùa và vĩ độ, góp phần vào biến thiên khí hậu dài hạn khi tương tác với băng, carbon và đại dương.

Điều này không mâu thuẫn với biến đổi khí hậu hiện đại: thang thời gian và cơ chế cưỡng bức khác nhau. Học địa lý cần luôn đặt một cơ chế vào đúng **thang thời gian (timescale)**.

## Liên hệ với hệ thống số

Phần mềm phân tán thường lưu timestamp theo UTC và chuyển sang giờ địa phương khi hiển thị. Lịch sử múi giờ và quy tắc giờ mùa hè làm chuyển đổi phức tạp; không nên hard-code offset cố định như “Seoul luôn +9” cho mọi địa điểm và mọi thời kỳ. Cơ sở dữ liệu múi giờ IANA tồn tại vì quy tắc dân sự thay đổi theo không gian và thời gian.

## Mô hình tư duy

> **Tự quay** tổ chức ngày, hướng chuyển động và kinh độ; **quỹ đạo + độ nghiêng trục** tổ chức mùa; **thể chế** biến thời gian thiên văn thành múi giờ dân sự. Khi xử lý thời gian toàn cầu, phải giữ cả ba lớp này trong đầu.

Xem tiếp: [Hệ tọa độ và thời gian](../00_foundations/02_coordinates_time_maps.md), [Khí quyển và khí hậu](../01_physical_geography/02_atmosphere_weather_climate.md).