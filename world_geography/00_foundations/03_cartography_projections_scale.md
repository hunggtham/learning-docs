# Bản đồ, scale và phép chiếu

## Bản đồ là model của không gian

**Cartography (bản đồ học / 지도학)** không chỉ là vẽ đẹp. Bản đồ là một model nén thực tại không gian để phục vụ task. Bất kỳ map nào cũng phải bỏ bớt chi tiết, chọn symbol, chọn classification và chọn projection. Vì vậy “bản đồ hoàn toàn trung lập” là một lý tưởng khó đạt; cartographer luôn quyết định thứ gì đáng hiển thị.

## Scale: tỷ lệ bản đồ và mức chi tiết

Map scale có thể viết 1:50,000, nghĩa là 1 đơn vị trên bản đồ tương ứng 50,000 đơn vị ngoài thực địa. Trong thuật ngữ cartography, **large-scale map** như 1:10,000 hiển thị khu vực nhỏ nhưng nhiều chi tiết; **small-scale map** như 1:50,000,000 hiển thị khu vực lớn nhưng ít chi tiết. Cách gọi này dễ gây nhầm vì “large-scale” nói đến fraction lớn hơn.

Khi zoom out, dữ liệu cần **generalization (khái quát hóa / 일반화)**. Một river polygon có thể thành line; nhiều building có thể thành urban area. Nếu giữ toàn bộ chi tiết ở mọi zoom, map sẽ nhiễu và performance giảm.

## Vì sao cần projection?

Bề mặt cong không thể trải phẳng mà không distortion. **Map projection (phép chiếu bản đồ / 지도 투영법)** là transformation từ ellipsoid/sphere sang plane. Không có projection giữ đồng thời hoàn hảo area, shape, distance và direction trên toàn thế giới.

Các property thường được ưu tiên gồm:

- **Conformal**: giữ góc và local shape tốt, hữu ích cho navigation.
- **Equal-area**: giữ diện tích, quan trọng khi so sánh quy mô lãnh thổ hoặc thematic map.
- **Equidistant**: giữ một số khoảng cách từ point/line nhất định.
- **Azimuthal**: giữ một số direction từ center.

Mercator là conformal. Nó giúp bearing navigation nhưng làm area phóng đại mạnh ở latitude cao. Greenland vì vậy trông lớn hơn rất nhiều so với thực tế tương đối so với Africa. Vấn đề không phải Mercator “sai”; nó đúng cho property nó bảo toàn nhưng không phù hợp nếu người đọc dùng hình ảnh để so area.

## Projection là trade-off giống data visualization

Trong Data Science, một chart chọn linear hay log scale sẽ làm pattern nổi bật khác nhau. Trong cartography, projection làm điều tương tự với spatial geometry. Vì vậy câu hỏi đúng không phải “projection nào tốt nhất?” mà là **“projection nào phù hợp với task?”**.

Một local engineering map thường dùng projected CRS tối ưu cho region, ví dụ UTM zone. World thematic map về population share nên ưu tiên equal-area hơn Mercator.

## Choropleth và nguy cơ dùng sai denominator

**Choropleth map (bản đồ tô vùng / 단계구분도)** tô administrative regions theo một value. Nó phù hợp với normalized rate như population density, unemployment rate hoặc tỷ lệ vote, nhưng dễ gây hiểu sai nếu tô theo raw count: region lớn về diện tích có thể visually dominate dù count per capita thấp.

Spatial aggregation cũng gây **MAUP — Modifiable Areal Unit Problem**: kết luận thống kê có thể đổi khi ta đổi cách chia zone. Đây là lý do cùng dữ liệu point khi aggregate theo quận hoặc theo grid có thể cho correlation khác nhau.

## Symbolization và classification

Nếu continuous values được chia thành class, method như equal interval, quantile hay natural breaks sẽ làm map khác nhau. Không có method nào luôn đúng. Equal interval giữ interval dễ hiểu nhưng có thể dồn nhiều vùng vào một class; quantile cho số vùng mỗi class tương đối bằng nhau nhưng có thể đặt values gần nhau vào hai class khác nhau.

## Web maps và tiles

Modern web map thường chia thế giới thành **tiles** ở nhiều zoom levels. Web Mercator phổ biến vì dễ tile hóa và tương thích ecosystem, không phải vì nó tối ưu cho area analysis. Đây là ví dụ rất rõ về việc engineering constraint ảnh hưởng geographic representation.

## Mental Model

Bản đồ giống một **API contract** giữa thế giới và người đọc. Projection định nghĩa geometry contract; scale định nghĩa level of detail; symbolization định nghĩa encoding; legend định nghĩa decoding. Nếu một trong các layer này bị hiểu sai, conclusion có thể sai dù underlying data đúng.

## Common Misconceptions

“Map lớn hơn nghĩa là scale lớn hơn” chỉ đúng nếu nói kích thước vật lý tờ giấy, không đúng trong thuật ngữ cartographic scale. “Satellite map không có projection” cũng sai; ảnh phải được georeference và hiển thị trong một CRS để overlay đúng với dữ liệu khác.

Xem tiếp: [GIS và remote sensing](./04_geospatial_data_gis_remote_sensing.md), [Địa lý + Toán và Statistics](../90_connections/00_geography_math_statistics.md).
