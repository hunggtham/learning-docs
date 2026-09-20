# Địa lý kết nối với IT, GIS, Kỹ thuật dữ liệu và AI

## Dữ liệu không gian phải được xem là kiểu dữ liệu cốt lõi

Trong ứng dụng thông thường, vị trí hay bị lưu đơn giản thành hai cột vĩ độ và kinh độ rồi xử lý thủ công. Khi số truy vấn không gian tăng, nên dùng kiểu **geometry/geography** cùng chỉ mục không gian. PostGIS, SQL Server Spatial, Oracle Spatial và nhiều hệ quản trị khác cung cấp sẵn các phép quan hệ và khoảng cách.

## Hệ quy chiếu tọa độ là một phần của hợp đồng dữ liệu

Một tọa độ không gian không thể được hiểu đúng chỉ từ hai số `x, y`. Cần biết **CRS — hệ quy chiếu tọa độ (Coordinate Reference System / 좌표 참조 체계)**. Tọa độ vĩ độ–kinh độ trong WGS84 và tọa độ phẳng tính theo mét là hai cách biểu diễn khác nhau.

EPSG:4326 thường dùng đơn vị độ. Nếu mã chương trình mặc định mọi tọa độ đều tính bằng mét, vùng đệm `1000` có thể bị hiểu thành 1000 độ — một lỗi logic nghiêm trọng. Vì vậy CRS nên được coi như kiểu dữ liệu hoặc đơn vị trong hợp đồng API, không phải metadata phụ.

## Chỉ mục không gian

Phép toán hình học chính xác có thể tốn chi phí. **Chỉ mục không gian (spatial index)** dùng hộp bao hoặc phân hoạch phân cấp để loại nhanh các ứng viên không liên quan trước khi tính chính xác. Cơ sở dữ liệu thông thường dùng B-tree cho thứ tự một chiều; không gian 2D/ND cần cấu trúc như R-tree, GiST, quadtree, geohash, S2 hoặc H3 tùy bài toán.

## Raster và vector là hai mô hình dữ liệu khác nhau

Vector biểu diễn đối tượng rời rạc bằng điểm, đường và đa giác; raster biểu diễn không gian bằng lưới ô. Mạng đường phù hợp với vector; ảnh vệ tinh và bề mặt độ cao thường phù hợp raster. Chuyển giữa hai mô hình có thể làm mất thông tin hoặc đưa thêm giả định về độ phân giải.

## Kiến trúc ô bản đồ

Bản đồ web thường dùng **ô raster hoặc ô vector (raster/vector tile)** theo nhiều mức phóng đại. Khái quát hóa và **mức chi tiết (LOD — Level of Detail)** quyết định lượng dữ liệu truyền. Ô vector cho phép phía trình duyệt định kiểu; ô raster đã được dựng sẵn. Khóa bộ nhớ đệm thường gắn với `zoom/x/y`.

## Định tuyến = đồ thị + địa lý

Định tuyến đường bộ biến bản đồ thành đồ thị: giao lộ là nút, đoạn đường là cạnh; trọng số có thể là khoảng cách, thời gian, phí hoặc chi phí tổng quát. Dijkstra hoặc A* tìm đường tối ưu theo trọng số. Trong A*, ước lượng khoảng cách địa lý có thể giúp thu hẹp tìm kiếm nếu thỏa điều kiện phù hợp.

Dẫn đường thực tế còn phải mã hóa cấm rẽ, đường một chiều, giao thông biến đổi theo thời gian và phân cấp đường. Nghĩa là mô hình đồ thị phải phản ánh quy tắc địa lý chứ không chỉ nối các điểm.

## Hàng rào địa lý

**Hàng rào địa lý (geofencing)** có thể là vòng tròn hoặc đa giác. Hệ thống di động phải xử lý nhiễu GPS; nếu kích hoạt đúng ngay tại ranh giới, thiết bị có thể liên tục nhảy giữa trạng thái vào–ra. **Độ trễ chuyển trạng thái (hysteresis)** hoặc yêu cầu ở trong vùng đủ lâu giúp sự kiện ổn định hơn.

## Viễn thám và học máy

Ảnh vệ tinh là tensor raster. CNN hoặc Transformer có thể phân loại lớp phủ đất, phát hiện đối tượng hoặc phân đoạn vùng ngập và vết cháy. Tuy nhiên nhãn thường bị lệch không gian và các điểm ảnh liền kề tương quan rất cao. Chia ngẫu nhiên tập huấn luyện–kiểm tra có thể gây **rò rỉ không gian (spatial leakage)**; kiểm định chéo theo vùng thường đáng tin hơn.

**Đặc trưng không gian (spatial feature)** có thể gồm khoảng cách tới điểm quan tâm, thống kê khu lân cận, độ cao hoặc lớp phủ đất. Mô hình tốt ở Seoul chưa chắc tổng quát sang vùng nông thôn vì phân bố đặc trưng và quá trình không gian khác nhau.

## Quyền riêng tư vị trí

Vị trí chính xác là dữ liệu nhạy cảm. Ngay cả quỹ đạo đã bỏ tên vẫn có thể tái nhận diện qua mẫu nhà–nơi làm việc. Hệ thống thực tế cần giảm thu thập không cần thiết, tổng hợp dữ liệu và kiểm soát quyền truy cập.

## ETL không gian

Một chuỗi xử lý thường gồm: thu nhận → kiểm tra CRS và hình học → chuyển đổi → nối không gian → tổng hợp → tạo ô hoặc API. Tính hợp lệ hình học, như đa giác tự cắt hoặc hướng vòng, cần được kiểm tra tương tự kiểm tra schema dữ liệu.

## Bản sao số

**Bản sao số (digital twin)** của đô thị hoặc công nghiệp có thể kết hợp GIS, BIM, cảm biến và mô phỏng. GIS cung cấp bối cảnh địa lý; BIM cung cấp chi tiết tài sản xây dựng. Đồng bộ trạng thái theo thời gian là một thách thức kỹ thuật quan trọng.

## Mô hình tư duy

> Phần mềm không gian là **kỹ thuật dữ liệu trong đó khoảng cách, quan hệ tô-pô, phép chiếu và quy mô là một phần của logic nghiệp vụ**. Hãy đối xử với chúng như hệ kiểu dữ liệu, không phải thông tin phụ.

Xem thêm: [Nền tảng GIS](../00_foundations/04_geospatial_data_gis_remote_sensing.md), [Toán học và Thống kê](./00_geography_math_statistics.md).
