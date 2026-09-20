# Địa lý kết nối với Toán học và Thống kê

## Hình học là ngôn ngữ của vị trí

Tọa độ, khoảng cách, diện tích, phương hướng và phép chiếu đều là các khái niệm hình học. Ở phạm vi địa phương nhỏ có thể xem gần như mặt phẳng, hình học Euclid thường đủ tốt; trên bề mặt toàn cầu cần hình học cầu hoặc mặt elipxoit (ellipsoid). Chọn sai mô hình hình học có thể làm khoảng cách hoặc diện tích sai dù mã chương trình chạy đúng.

Khoảng cách Euclid trên mặt phẳng giữa hai điểm là:

\[
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
\]

Nhưng bài toán địa lý có thể cần khoảng cách vòng tròn lớn trên mặt cầu, khoảng cách theo mạng đường, thời gian di chuyển hoặc **khoảng cách chi phí (cost distance)**. Hai điểm cách nhau 20 km đường thẳng nhưng bị núi ngăn có thể mất nhiều thời gian di chuyển hơn hai điểm cách 50 km dọc cao tốc. Vì vậy thước đo phải phản ánh cơ chế thực của hiện tượng.

## Quy mô và tư duy về đơn vị

Tỷ lệ bản đồ là một tỷ số. Mật độ là lượng trên diện tích. **Độ dốc biến thiên (gradient)** là mức thay đổi trên khoảng cách. Đây là **suy luận thứ nguyên (dimensional reasoning)**: nếu dân số tăng gấp đôi nhưng diện tích cũng tăng gấp đôi, mật độ không đổi. Theo dõi đơn vị giúp phát hiện nhiều sai lầm trước cả khi tính toán.

## Thống kê không gian khác thống kê thông thường ở tính phụ thuộc

Trực giác thống kê cổ điển thường giả định các quan sát độc lập. Dữ liệu địa lý thường vi phạm giả định này vì những nơi gần nhau có xu hướng giống nhau hơn do cùng môi trường, quá trình khuếch tán hoặc sự tập cụm. Hiện tượng đó gọi là **tự tương quan không gian (spatial autocorrelation / 공간 자기상관)**.

**Moran’s I** là một chỉ số đo tự tương quan không gian toàn cục. Ý tưởng cốt lõi là so sánh mức giống nhau giữa một quan sát và các láng giềng có trọng số. Ma trận trọng số \(W\) mã hóa quan hệ kề hoặc khoảng cách, nên kết quả phụ thuộc cách định nghĩa “láng giềng”.

## Hồi quy và nhiễu không gian

Nếu biến kết quả và biến giải thích cùng có xu hướng không gian do một yếu tố thứ ba, hồi quy có thể cho liên hệ gây hiểu lầm. Lập bản đồ phần dư là một bước chẩn đoán quan trọng: nếu phần dư vẫn tập thành cụm, mô hình có thể đã bỏ sót cấu trúc không gian.

Điều này cũng quan trọng trong học máy và kinh tế lượng. Nếu chia ngẫu nhiên mẫu không gian thành tập huấn luyện–kiểm tra, mô hình có thể hưởng lợi từ thông tin của các điểm rất gần nhau và cho kết quả quá lạc quan. **Kiểm định chéo theo không gian (spatial cross-validation)** thường thực tế hơn khi mục tiêu là dự báo sang vùng mới.

## Xác suất và hiểm họa

Chu kỳ lặp lại, xác suất lũ và dự báo đều cần xác suất. Nếu một sự kiện có xác suất hằng năm \(p\), xác suất xảy ra ít nhất một lần trong \(n\) năm là:

\[
1-(1-p)^n
\]

Điều này giải thích vì sao “lũ 100 năm” vẫn có thể xảy ra trong hai năm gần nhau; thuật ngữ đó mô tả xác suất theo năm chứ không phải lịch hẹn chính xác.

## Quy mô tổng hợp và MAUP

Thu nhập trung bình, tỷ lệ bệnh hoặc kết quả bầu cử có thể đổi cách diễn giải khi đổi đơn vị không gian. **Vấn đề đơn vị không gian có thể thay đổi (MAUP — Modifiable Areal Unit Problem)** mô tả việc kết quả thống kê phụ thuộc cách chia vùng và mức tổng hợp. Bản đồ theo tỉnh có thể kể câu chuyện khác bản đồ theo quận dù các sự kiện gốc không đổi.

## Tối ưu hóa vị trí

Chọn vị trí cơ sở, lập tuyến và vùng phục vụ là các bài toán tối ưu hóa. Ví dụ **bài toán p-median** tìm vị trí của \(p\) cơ sở để giảm tổng khoảng cách có trọng số theo nhu cầu; **bài toán phủ tập (set covering)** tìm số cơ sở tối thiểu để phủ nhu cầu trong một ngưỡng. Đây là cầu nối trực tiếp với **Nghiên cứu vận hành (Operations Research)**.

## Lý thuyết đồ thị

Đường bộ, hàng không, sông và mạng thương mại có thể được mô hình hóa bằng đồ thị. Bậc nút, tính trung gian, đường đi ngắn nhất và phát hiện cộng đồng giúp nhận diện trung tâm hoặc điểm nghẽn. Địa lý bổ sung trọng số thực như thời gian đi, chi phí biên giới và công suất.

## Hình học như một mô hình ràng buộc

Vùng đệm, giao nhau, sơ đồ Voronoi và đường đi ngắn nhất không chỉ là thao tác GIS; chúng mã hóa giả định. Vùng đệm 500 m quanh ga giả định khoảng cách hướng tâm có ý nghĩa; vùng phục vụ 10 phút theo mạng giả định người di chuyển dọc hệ đường. Đối tượng toán học phải được chọn theo quá trình thực chứ không theo sự tiện lợi của công cụ.

## Mô hình tư duy

> Toán học cung cấp **cách biểu diễn và các ràng buộc**; địa lý cung cấp **ý nghĩa của không gian**. Đừng áp dụng công thức khoảng cách, hồi quy hoặc chỉ số mạng trước khi xác định đơn vị không gian, hệ quy chiếu, quy mô và quá trình đang nghiên cứu.

Xem thêm: [GIS](../00_foundations/04_geospatial_data_gis_remote_sensing.md), [Mạng giao thông](../02_human_geography/08_transport_trade_globalization.md).
