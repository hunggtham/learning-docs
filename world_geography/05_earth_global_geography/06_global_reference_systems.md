# Hệ quy chiếu toàn cầu và thế giới số

## Một tọa độ chỉ có ý nghĩa trong một hệ quy chiếu

Chuỗi `37.5665, 126.9780` trông giống một vị trí, nhưng để sử dụng chính xác cần biết thứ tự trục, đơn vị, datum và CRS. Trong phần lớn ứng dụng web, người ta ngầm hiểu WGS 84 latitude/longitude; trong kỹ thuật, ngầm hiểu như vậy có thể gây lỗi.

**Hệ quy chiếu tọa độ (CRS)** mô tả cách ánh xạ tọa độ số sang vị trí trên/so với Trái Đất. CRS địa lý dùng góc; CRS chiếu phẳng dùng đơn vị tuyến tính như mét.

## Hệ quy chiếu toàn cầu và địa phương

WGS 84 phù hợp làm hệ toàn cầu cho GNSS và trao đổi dữ liệu. Nhưng đo đạc địa phương có thể dùng datum hoặc phép chiếu tối ưu cho một quốc gia/vùng để giảm biến dạng. Không có CRS duy nhất tối ưu cho mọi bài toán.

Ví dụ, tính diện tích thửa đất nên dùng một hệ chiếu phù hợp vùng thay vì lấy công thức phẳng trực tiếp trên độ vĩ–kinh. Ngược lại, lưu vị trí người dùng toàn cầu trong một hệ địa phương sẽ bất tiện.

## EPSG code là khóa tra cứu, không phải phép thuật

Mã EPSG giúp định danh CRS, nhưng hai lớp cùng EPSG vẫn có thể gặp vấn đề nếu dữ liệu bị gán nhãn sai từ đầu. `Assign CRS` và `Reproject` là hai thao tác khác nhau: thao tác đầu nói “các con số này đang thuộc hệ nào”; thao tác sau biến đổi con số giữa hai hệ.

Gán sai CRS rồi reproject có thể tạo kết quả rất sai nhưng vẫn sinh ra file hợp lệ về kỹ thuật.

## Trục và thứ tự tọa độ

Một số tiêu chuẩn định nghĩa trục latitude–longitude, trong khi nhiều API web quen longitude–latitude hoặc `x,y`. Đây là nguồn bug kinh điển. Hệ thống nên ghi rõ contract thay vì dựa vào trí nhớ của lập trình viên.

## Thời gian là chiều thứ tư của hệ quy chiếu

Mảng kiến tạo chuyển động và các datum động hiện đại có epoch. Với ứng dụng centimet-level, cùng một điểm vật lý có tọa độ thay đổi theo thời gian trong hệ cố định toàn cầu. Vì thế coordinate transformation có thể cần cả vận tốc và epoch.

Đây là điểm giao giữa trắc địa và software engineering: dữ liệu không chỉ có schema không gian mà còn có **version/epoch**.

## Hệ thống ô và chỉ mục toàn cầu

Ngoài latitude/longitude, hệ thống số thường chia Trái Đất thành ô hoặc mã phân cấp như geohash, H3, S2 hay tile XYZ. Mục tiêu không phải thay CRS, mà giúp lập chỉ mục, tổng hợp và cache theo không gian.

Ô càng nhỏ cho độ chi tiết cao nhưng tăng số lượng đối tượng. Một hệ lưới toàn cầu luôn có trade-off về hình dạng ô, diện tích, hàng xóm và độ méo.

## Địa chỉ không phải tọa độ

Địa chỉ là hệ thống xã hội. Nó thay đổi khi đường đổi tên, địa giới thay đổi hoặc quy tắc đánh số khác nhau. Geocoding là quá trình ánh xạ giữa hai hệ: **ngôn ngữ–hành chính của địa chỉ** và **hình học của tọa độ**. Vì vậy kết quả geocoder cần confidence và provenance, không nên coi như chân lý tuyệt đối.

## Mô hình tư duy

> Dữ liệu toàn cầu cần một **hợp đồng không gian**: datum/CRS, trục, đơn vị, epoch và quy tắc biến đổi. Sai một trong các lớp này có thể tạo lỗi lớn dù tất cả phép toán phía sau đều đúng.

Xem tiếp: [Địa lý + IT/GIS/Data](../90_connections/01_geography_it_gis_data.md), [Bản đồ và phép chiếu](../00_foundations/03_cartography_projections_scale.md).