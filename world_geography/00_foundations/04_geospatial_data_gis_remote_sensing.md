# Dữ liệu không gian, GIS và viễn thám

## GIS giải quyết vấn đề gì?

Khi câu hỏi chứa “ở đâu”, “gần cái gì”, “nằm trong vùng nào”, “đường nào tối ưu” hoặc “những khu vực nào chồng lấn”, cơ sở dữ liệu thông thường chưa đủ thuận tiện. **GIS — Hệ thống thông tin địa lý (Geographic Information System / 지리정보시스템)** kết hợp dữ liệu, hình học, phân tích và trực quan hóa để làm việc với các quan hệ không gian.

## Dữ liệu vectơ và raster

Hai cách biểu diễn cơ bản là **dữ liệu vectơ (vector)** và **dữ liệu raster (raster)**. Dữ liệu vectơ dùng điểm, đường và đa giác để biểu diễn đối tượng có ranh giới tương đối rõ như trạm, đường, thửa đất hoặc quận. Dữ liệu raster chia không gian thành các ô lưới; mỗi ô chứa một giá trị như độ cao, nhiệt độ hoặc mức phản xạ điện từ.

Dữ liệu vectơ phù hợp với quan hệ tô-pô và việc nhận diện từng đối tượng. Dữ liệu raster phù hợp với **trường liên tục (continuous field)** và mô hình hóa theo từng ô. Nhiều quy trình xử lý chuyển qua lại giữa hai dạng; lựa chọn không phải “cái nào hiện đại hơn” mà phụ thuộc bản chất hiện tượng.

## Hình học, thuộc tính và quan hệ không gian

Một **đối tượng dữ liệu (feature)** không chỉ có hình học mà còn có thuộc tính. Ví dụ một điểm bệnh viện có tên, số giường và chuyên khoa. GIS có thể trả lời “mọi hộ dân có thể đến bệnh viện nào trong 15 phút lái xe?” — đây không còn là lọc dữ liệu đơn giản mà là bài toán khả năng tiếp cận trên mạng lưới.

Các **vị từ không gian (spatial predicate)** như `within`, `contains`, `intersects`, `touches`, `overlaps`, `nearest` có ý nghĩa toán học hoặc tô-pô rõ ràng. Trong PostGIS, chúng trở thành các phép truy vấn cơ bản. **Chỉ mục không gian (spatial index)** như R-tree/GiST thu hẹp không gian tìm kiếm bằng hộp bao trước khi chạy phép tính hình học chính xác.

## Viễn thám: đo từ xa thay vì đến từng điểm

**Viễn thám (remote sensing / 원격탐사)** thu thông tin về bề mặt từ cảm biến trên vệ tinh, máy bay hoặc thiết bị bay không người lái. Cảm biến không “nhìn thấy lớp phủ đất” giống con người; nó đo năng lượng điện từ ở nhiều dải bước sóng. Thảm thực vật, nước, tuyết và bề mặt xây dựng phản xạ hoặc hấp thụ khác nhau, tạo **dấu hiệu phổ (spectral signature)**.

Một chỉ số nổi tiếng là NDVI:

\[
NDVI=\frac{NIR-Red}{NIR+Red}
\]

Thảm thực vật khỏe thường phản xạ mạnh bức xạ cận hồng ngoại (near-infrared, NIR) và hấp thụ ánh sáng đỏ phục vụ quang hợp, nên NDVI thường tăng. Tuy nhiên NDVI không phải “máy đo sức khỏe cây tuyệt đối”; mây, nền đất, hiệu chuẩn cảm biến, mùa và loại thực vật đều ảnh hưởng kết quả.

## Độ phân giải: không chỉ là kích thước điểm ảnh

Viễn thám có nhiều loại **độ phân giải (resolution)**. **Độ phân giải không gian (spatial resolution)** là kích thước điểm ảnh. **Độ phân giải thời gian (temporal resolution)** là tần suất vệ tinh quay lại quan sát. **Độ phân giải phổ (spectral resolution)** liên quan số lượng và độ hẹp của các dải bước sóng. **Độ phân giải bức xạ (radiometric resolution)** là khả năng phân biệt các mức năng lượng.

Cảm biến có điểm ảnh 30 m không phải lúc nào cũng “kém hơn” cảm biến 1 m. Theo dõi mùa vụ trên vùng rộng hoặc xu hướng khí hậu có thể ưu tiên tần suất quan sát lại và tính nhất quán hơn chi tiết cực cao.

## Mô hình số độ cao và phân tích địa hình

**DEM — Mô hình số độ cao (Digital Elevation Model / 수치표고모델)** cho phép tính độ dốc, hướng sườn, lưu vực, vùng quan sát và hướng dòng chảy. Đây là cầu nối giữa hình học và quá trình vật lý: chỉ từ trường độ cao, ta có thể suy ra nhiều cấu trúc thoát nước bằng giả định nước có xu hướng chảy theo hướng giảm thế năng.

## Mã hóa địa chỉ thành tọa độ

**Mã hóa địa lý (geocoding)** chuyển địa chỉ thành tọa độ; **mã hóa địa lý ngược (reverse geocoding)** làm ngược lại. Địa chỉ là dữ liệu xã hội, không hoàn toàn hình học: cách đặt tên đường, đánh số nhà và ranh giới hành chính khác nhau giữa các quốc gia. Vì vậy hệ thống mã hóa địa lý cần dữ liệu tham chiếu và quy tắc địa phương.

## GPS/GNSS và độ bất định

Đo vị trí luôn có sai số. GPS trên điện thoại có thể lệch do tín hiệu phản xạ nhiều đường trong “hẻm đô thị”, trễ khí quyển hoặc hình học vệ tinh không thuận lợi. Trong phân tích, tọa độ không nên mặc định là một điểm chính xác tuyệt đối. Một số bài toán cần vùng đệm bất định hoặc mô hình vị trí theo xác suất.

## GIS trong công nghệ thông tin

Một hệ thống GIS phổ biến có thể gồm cơ sở dữ liệu không gian, máy chủ ô bản đồ, dịch vụ mã hóa địa lý và bản đồ phía giao diện người dùng. Cơ sở dữ liệu lưu hình học cùng chỉ mục không gian; phần máy chủ chạy truy vấn không gian; ô bản đồ hoặc **ô vectơ (vector tile)** giảm dữ liệu truyền; phía trình duyệt hiển thị theo mức phóng đại. Khi hệ thống có hàng triệu đối tượng, kiến trúc cần phân vùng dữ liệu, đơn giản hóa hình học và lưu đệm theo không gian.

## Mô hình tư duy

Hãy coi GIS là **cơ sở dữ liệu + bộ máy hình học + hệ tọa độ + trực quan hóa**, còn viễn thám là **chuỗi đo lường từ tín hiệu điện từ → dữ liệu đã hiệu chuẩn → biến địa lý được suy ra**. Sai ở hệ quy chiếu, phép đo hoặc bước suy luận đều có thể tạo bản đồ đẹp nhưng kết luận sai.

Xem tiếp: [Địa lý + IT/GIS/Data](../90_connections/01_geography_it_gis_data.md), [Khí hậu](../01_physical_geography/03_global_climate_system.md).
