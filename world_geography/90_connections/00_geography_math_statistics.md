# Địa lý kết nối với Toán học và Thống kê

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Địa lý kết nối với Toán học và Thống kê**. Route đi từ geometry/location → scale/units → spatial distributions → sampling/autocorrelation → inference under spatial dependence, để toán giữ được cấu trúc không gian.

## Hình học là ngôn ngữ của vị trí

Tọa độ, khoảng cách, diện tích, phương hướng và phép chiếu đều là các khái niệm hình học. Ở phạm vi địa phương nhỏ có thể xem gần như mặt phẳng, hình học Euclid thường đủ tốt; trên bề mặt toàn cầu cần hình học cầu hoặc mặt elipxoit (ellipsoid). Chọn sai mô hình hình học có thể làm khoảng cách hoặc diện tích sai dù mã chương trình chạy đúng.

Khoảng cách Euclid trên mặt phẳng giữa hai điểm là:

\[
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
\]

Nhưng bài toán địa lý có thể cần khoảng cách vòng tròn lớn trên mặt cầu, khoảng cách theo mạng đường, thời gian di chuyển hoặc **khoảng cách chi phí (cost distance)**. Hai điểm cách nhau 20 km đường thẳng nhưng bị núi ngăn có thể mất nhiều thời gian di chuyển hơn hai điểm cách 50 km dọc cao tốc. Vì vậy thước đo phải phản ánh cơ chế thực của hiện tượng.

> **Chuyển mạch:** Trong **Địa lý kết nối với Toán học và Thống kê**, **Quy mô và tư duy về đơn vị** tiếp nhận điểm tựa từ **Hình học là ngôn ngữ của vị trí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thống kê không gian khác thống kê thông thường ở tính phụ thuộc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy mô và tư duy về đơn vị

Tỷ lệ bản đồ là một tỷ số. Mật độ là lượng trên diện tích. **Độ dốc biến thiên (gradient)** là mức thay đổi trên khoảng cách. Đây là **suy luận thứ nguyên (dimensional reasoning)**: nếu dân số tăng gấp đôi nhưng diện tích cũng tăng gấp đôi, mật độ không đổi. Theo dõi đơn vị giúp phát hiện nhiều sai lầm trước cả khi tính toán.

> **Chuyển mạch:** Ở chặng này của **Địa lý kết nối với Toán học và Thống kê**, **Thống kê không gian khác thống kê thông thường ở tính phụ thuộc** tiếp nhận điểm tựa từ **Quy mô và tư duy về đơn vị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hồi quy và nhiễu không gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thống kê không gian khác thống kê thông thường ở tính phụ thuộc

Trực giác thống kê cổ điển thường giả định các quan sát độc lập. Dữ liệu địa lý thường vi phạm giả định này vì những nơi gần nhau có xu hướng giống nhau hơn do cùng môi trường, quá trình khuếch tán hoặc sự tập cụm. Hiện tượng đó gọi là **tự tương quan không gian (spatial autocorrelation / 공간 자기상관)**.

**Moran’s I** là một chỉ số đo tự tương quan không gian toàn cục. Ý tưởng cốt lõi là so sánh mức giống nhau giữa một quan sát và các láng giềng có trọng số. Ma trận trọng số \(W\) mã hóa quan hệ kề hoặc khoảng cách, nên kết quả phụ thuộc cách định nghĩa “láng giềng”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Địa lý kết nối với Toán học và Thống kê**, **Hồi quy và nhiễu không gian** tiếp nhận điểm tựa từ **Thống kê không gian khác thống kê thông thường ở tính phụ thuộc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xác suất và hiểm họa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hồi quy và nhiễu không gian

Nếu biến kết quả và biến giải thích cùng có xu hướng không gian do một yếu tố thứ ba, hồi quy có thể cho liên hệ gây hiểu lầm. Lập bản đồ phần dư là một bước chẩn đoán quan trọng: nếu phần dư vẫn tập thành cụm, mô hình có thể đã bỏ sót cấu trúc không gian.

Điều này cũng quan trọng trong học máy và kinh tế lượng. Nếu chia ngẫu nhiên mẫu không gian thành tập huấn luyện–kiểm tra, mô hình có thể hưởng lợi từ thông tin của các điểm rất gần nhau và cho kết quả quá lạc quan. **Kiểm định chéo theo không gian (spatial cross-validation)** thường thực tế hơn khi mục tiêu là dự báo sang vùng mới.

> **Chuyển mạch:** Trong **Địa lý kết nối với Toán học và Thống kê**, **Xác suất và hiểm họa** tiếp nhận điểm tựa từ **Hồi quy và nhiễu không gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy mô tổng hợp và MAUP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xác suất và hiểm họa

Chu kỳ lặp lại, xác suất lũ và dự báo đều cần xác suất. Nếu một sự kiện có xác suất hằng năm \(p\), xác suất xảy ra ít nhất một lần trong \(n\) năm là:

\[
1-(1-p)^n
\]

Điều này giải thích vì sao “lũ 100 năm” vẫn có thể xảy ra trong hai năm gần nhau; thuật ngữ đó mô tả xác suất theo năm chứ không phải lịch hẹn chính xác.

> **Chuyển mạch:** Ở chặng này của **Địa lý kết nối với Toán học và Thống kê**, **Quy mô tổng hợp và MAUP** gom các mảnh từ **Xác suất và hiểm họa** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Tối ưu hóa vị trí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy mô tổng hợp và MAUP

Thu nhập trung bình, tỷ lệ bệnh hoặc kết quả bầu cử có thể đổi cách diễn giải khi đổi đơn vị không gian. **Vấn đề đơn vị không gian có thể thay đổi (MAUP — Modifiable Areal Unit Problem)** mô tả việc kết quả thống kê phụ thuộc cách chia vùng và mức tổng hợp. Bản đồ theo tỉnh có thể kể câu chuyện khác bản đồ theo quận dù các sự kiện gốc không đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Địa lý kết nối với Toán học và Thống kê**, **Tối ưu hóa vị trí** gom các mảnh từ **Quy mô tổng hợp và MAUP** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Lý thuyết đồ thị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tối ưu hóa vị trí

Chọn vị trí cơ sở, lập tuyến và vùng phục vụ là các bài toán tối ưu hóa. Ví dụ **bài toán p-median** tìm vị trí của \(p\) cơ sở để giảm tổng khoảng cách có trọng số theo nhu cầu; **bài toán phủ tập (set covering)** tìm số cơ sở tối thiểu để phủ nhu cầu trong một ngưỡng. Đây là cầu nối trực tiếp với **Nghiên cứu vận hành (Operations Research)**.

> **Chuyển mạch:** Trong **Địa lý kết nối với Toán học và Thống kê**, **Lý thuyết đồ thị** tiếp nhận điểm tựa từ **Tối ưu hóa vị trí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hình học như một mô hình ràng buộc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lý thuyết đồ thị

Đường bộ, hàng không, sông và mạng thương mại có thể được mô hình hóa bằng đồ thị. Bậc nút, tính trung gian, đường đi ngắn nhất và phát hiện cộng đồng giúp nhận diện trung tâm hoặc điểm nghẽn. Địa lý bổ sung trọng số thực như thời gian đi, chi phí biên giới và công suất.

> **Chuyển mạch:** Ở chặng này của **Địa lý kết nối với Toán học và Thống kê**, **Hình học như một mô hình ràng buộc** tiếp nhận điểm tựa từ **Lý thuyết đồ thị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hình học như một mô hình ràng buộc

Vùng đệm, giao nhau, sơ đồ Voronoi và đường đi ngắn nhất không chỉ là thao tác GIS; chúng mã hóa giả định. Vùng đệm 500 m quanh ga giả định khoảng cách hướng tâm có ý nghĩa; vùng phục vụ 10 phút theo mạng giả định người di chuyển dọc hệ đường. Đối tượng toán học phải được chọn theo quá trình thực chứ không theo sự tiện lợi của công cụ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Địa lý kết nối với Toán học và Thống kê**, **Mô hình tư duy** gom các mảnh từ **Hình học như một mô hình ràng buộc** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Toán học cung cấp **cách biểu diễn và các ràng buộc**; địa lý cung cấp **ý nghĩa của không gian**. Đừng áp dụng công thức khoảng cách, hồi quy hoặc chỉ số mạng trước khi xác định đơn vị không gian, hệ quy chiếu, quy mô và quá trình đang nghiên cứu.

Xem thêm: [GIS](../00_foundations/04_geospatial_data_gis_remote_sensing.md), [Mạng giao thông](../02_human_geography/08_transport_trade_globalization.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
