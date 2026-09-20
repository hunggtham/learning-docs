# Bản đồ, tỷ lệ và phép chiếu

## Bản đồ là mô hình của không gian

**Bản đồ học (cartography / 지도학)** không chỉ là việc vẽ bản đồ đẹp. Bản đồ là một **mô hình (model)** nén thực tại không gian để phục vụ một mục đích cụ thể. Bất kỳ bản đồ nào cũng phải bỏ bớt chi tiết, chọn ký hiệu, cách phân loại và phép chiếu. Vì vậy “bản đồ hoàn toàn trung lập” là một lý tưởng khó đạt; người làm bản đồ luôn phải quyết định thứ gì đáng hiển thị.

## Tỷ lệ bản đồ và mức chi tiết

**Tỷ lệ bản đồ (map scale)** có thể viết 1:50.000, nghĩa là 1 đơn vị trên bản đồ tương ứng 50.000 đơn vị ngoài thực địa. Trong bản đồ học, **bản đồ tỷ lệ lớn (large-scale map)** như 1:10.000 hiển thị khu vực nhỏ nhưng nhiều chi tiết; **bản đồ tỷ lệ nhỏ (small-scale map)** như 1:50.000.000 hiển thị khu vực lớn nhưng ít chi tiết. Cách gọi này dễ gây nhầm vì “tỷ lệ lớn” nói đến phân số tỷ lệ có giá trị lớn hơn.

Khi thu nhỏ phạm vi hiển thị, dữ liệu cần **khái quát hóa (generalization / 일반화)**. Một vùng sông dạng đa giác có thể được biểu diễn thành đường; nhiều tòa nhà có thể gộp thành khu đô thị. Nếu giữ toàn bộ chi tiết ở mọi mức phóng đại, bản đồ sẽ nhiễu và hiệu năng hiển thị giảm.

## Vì sao cần phép chiếu?

Bề mặt cong không thể trải phẳng mà không gây **biến dạng (distortion)**. **Phép chiếu bản đồ (map projection / 지도 투영법)** là phép biến đổi từ ellipsoid hoặc mặt cầu sang mặt phẳng. Không có phép chiếu nào giữ đồng thời hoàn hảo diện tích, hình dạng, khoảng cách và phương hướng trên toàn thế giới.

Các tính chất thường được ưu tiên gồm:

- **Bảo giác (conformal)**: giữ góc và hình dạng cục bộ tốt, hữu ích cho hàng hải và định hướng.
- **Bảo toàn diện tích (equal-area)**: giữ diện tích, quan trọng khi so sánh quy mô lãnh thổ hoặc lập bản đồ chuyên đề.
- **Bảo khoảng cách (equidistant)**: giữ một số khoảng cách từ điểm hoặc đường xác định.
- **Phương vị (azimuthal)**: giữ một số phương hướng tính từ tâm.

Mercator là phép chiếu bảo giác. Nó hữu ích cho định hướng hàng hải nhưng phóng đại diện tích mạnh ở vĩ độ cao. Greenland vì vậy trông lớn hơn rất nhiều so với thực tế khi đặt cạnh châu Phi. Vấn đề không phải Mercator “sai”; nó đúng đối với tính chất mà nó bảo toàn nhưng không phù hợp nếu người đọc dùng hình ảnh để so sánh diện tích.

## Phép chiếu là một sự đánh đổi giống trực quan hóa dữ liệu

Trong khoa học dữ liệu, lựa chọn thang tuyến tính hay logarit khiến các mẫu dữ liệu nổi bật khác nhau. Trong bản đồ học, phép chiếu tạo hiệu ứng tương tự đối với hình học không gian. Vì vậy câu hỏi đúng không phải “phép chiếu nào tốt nhất?” mà là **“phép chiếu nào phù hợp với mục đích?”**.

Một bản đồ kỹ thuật địa phương thường dùng hệ quy chiếu phẳng tối ưu cho khu vực, ví dụ một múi UTM. Bản đồ chuyên đề thế giới về tỷ trọng dân số nên ưu tiên phép chiếu bảo toàn diện tích hơn Mercator.

## Bản đồ tô vùng và nguy cơ dùng sai mẫu số

**Bản đồ tô vùng (choropleth map / 단계구분도)** tô các đơn vị hành chính theo một giá trị. Nó phù hợp với tỷ lệ đã chuẩn hóa như mật độ dân số hoặc tỷ lệ thất nghiệp, nhưng dễ gây hiểu sai nếu tô theo số lượng tuyệt đối: vùng lớn về diện tích có thể lấn át thị giác dù số lượng bình quân đầu người thấp.

Việc tổng hợp dữ liệu theo vùng còn gây **vấn đề đơn vị không gian có thể thay đổi (MAUP — Modifiable Areal Unit Problem)**: kết luận thống kê có thể đổi khi ta đổi cách chia vùng. Đây là lý do cùng dữ liệu điểm khi tổng hợp theo quận hoặc theo lưới có thể cho tương quan khác nhau.

## Ký hiệu hóa và phân lớp

Nếu giá trị liên tục được chia thành lớp, các phương pháp như khoảng bằng nhau (equal interval), phân vị (quantile) hay ngắt tự nhiên (natural breaks) sẽ tạo ra bản đồ khác nhau. Không có phương pháp nào luôn đúng. Khoảng bằng nhau dễ đọc nhưng có thể dồn nhiều vùng vào một lớp; phân vị giúp số vùng mỗi lớp tương đối bằng nhau nhưng có thể đặt hai giá trị gần nhau vào hai lớp khác nhau.

## Bản đồ web và ô bản đồ

Bản đồ web hiện đại thường chia thế giới thành các **ô bản đồ (tile)** ở nhiều mức phóng đại. Web Mercator phổ biến vì dễ chia ô và tương thích với hệ sinh thái công cụ, không phải vì nó tối ưu cho phân tích diện tích. Đây là ví dụ rõ ràng về việc ràng buộc kỹ thuật ảnh hưởng cách biểu diễn địa lý.

## Mô hình tư duy

Bản đồ giống một **hợp đồng giao diện (API contract)** giữa thế giới và người đọc. Phép chiếu định nghĩa quy tắc hình học; tỷ lệ định nghĩa mức chi tiết; ký hiệu hóa định nghĩa cách mã hóa; chú giải định nghĩa cách giải mã. Nếu một lớp trong chuỗi này bị hiểu sai, kết luận có thể sai dù dữ liệu gốc đúng.

## Những hiểu lầm phổ biến

“Bản đồ lớn hơn nghĩa là tỷ lệ lớn hơn” chỉ đúng nếu nói kích thước vật lý của tờ giấy, không đúng trong thuật ngữ tỷ lệ bản đồ. “Bản đồ vệ tinh không có phép chiếu” cũng sai; ảnh cần được **gán tham chiếu địa lý (georeference)** và hiển thị trong một hệ quy chiếu tọa độ để chồng khớp với dữ liệu khác.

Xem tiếp: [GIS và viễn thám](./04_geospatial_data_gis_remote_sensing.md), [Địa lý + Toán và Thống kê](../90_connections/00_geography_math_statistics.md).
