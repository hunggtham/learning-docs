# Hệ tọa độ, Trái Đất quay và thời gian

## Vấn đề cơ bản: làm sao nói chính xác “ở đâu” trên một bề mặt cong?

Nếu chỉ dùng mô tả như “phía đông ngọn núi” hoặc “gần biển”, việc định vị không thể dùng thống nhất trên toàn cầu. Ta cần một **hệ quy chiếu (reference system)** chung. **Hệ tọa độ địa lý (Geographic Coordinate System / 지리 좌표계)** dùng hai góc cơ bản: vĩ độ và kinh độ.

**Vĩ độ (latitude / 위도)** đo góc bắc–nam so với Xích đạo. Xích đạo là 0°, hai cực là ±90°. **Kinh độ (longitude / 경도)** đo góc đông–tây so với kinh tuyến gốc (Prime Meridian), theo quy ước hiện đại đi qua Greenwich, từ 0° đến ±180°.

Điểm quan trọng là vĩ độ và kinh độ là **tọa độ góc (angular coordinates)**, không phải khoảng cách tính bằng mét. Một độ kinh gần Xích đạo dài hơn nhiều so với một độ kinh gần cực vì các kinh tuyến hội tụ về hai cực.

## Trái Đất không phải hình cầu hoàn hảo

Trái Đất gần một **khối cầu dẹt (oblate spheroid)**: hơi phình ở Xích đạo. Việc lập bản đồ chính xác còn dùng **ellipsoid tham chiếu** và **mốc trắc địa (geodetic datum / 측지 기준계)**. GPS phổ biến dùng WGS 84. Nếu hai bộ dữ liệu dùng mốc trắc địa khác nhau nhưng bị ghép như thể cùng hệ, đối tượng có thể lệch vị trí.

Trong GIS, đây là lỗi kinh điển: tọa độ nhìn có vẻ hợp lý nhưng các lớp bản đồ không khớp nhau. Vì thế luôn cần biết cả giá trị tọa độ lẫn **hệ quy chiếu tọa độ (CRS — Coordinate Reference System / 좌표참조체계)**.

## Khoảng cách theo vòng tròn lớn

Trên mặt cầu, đường ngắn nhất giữa hai điểm không phải lúc nào cũng là đường thẳng khi nhìn trên bản đồ phẳng mà là **đường vòng tròn lớn (great-circle route / 대권 항로)**. Đây là lý do đường bay trên bản đồ Mercator thường trông như cong về phía cực.

Khoảng cách xấp xỉ giữa hai tọa độ có thể tính bằng công thức Haversine:

\[
a=\sin^2\left(\frac{\Delta\varphi}{2}\right)+\cos\varphi_1\cos\varphi_2\sin^2\left(\frac{\Delta\lambda}{2}\right)
\]
\[
c=2\arctan2(\sqrt a,\sqrt{1-a}),\qquad d=Rc
\]

\(\varphi\) là vĩ độ theo radian, \(\lambda\) là kinh độ, \(R\) là bán kính Trái Đất xấp xỉ. Mô hình mặt cầu đủ tốt cho nhiều ứng dụng; trắc địa chính xác cao dùng ellipsoid.

Mối liên hệ với công nghệ thông tin rất trực tiếp: ứng dụng di động “tìm địa điểm gần tôi”, **hàng rào địa lý (geofencing)**, lọc sơ bộ tuyến đường, cơ sở dữ liệu không gian và logistics đều cần mô hình khoảng cách phù hợp. Dùng khoảng cách Euclid trực tiếp trên vĩ độ–kinh độ có thể tạo sai số đáng kể ở phạm vi lớn.

## Trái Đất quay, giờ Mặt Trời địa phương và múi giờ

Trái Đất quay khoảng một vòng mỗi ngày, nên về hình học 360° kinh độ tương ứng khoảng 24 giờ, tức gần 15° mỗi giờ. **Giờ Mặt Trời địa phương (local solar time)** phụ thuộc vị trí Mặt Trời, nhưng xã hội hiện đại dùng **múi giờ tiêu chuẩn (standard time zone / 표준시)** theo ranh giới chính trị–hành chính chứ không thuần túy theo hình học.

Do đó bản đồ múi giờ không thể suy ra chỉ bằng kinh độ. Một quốc gia có thể dùng một múi giờ cho toàn lãnh thổ rộng hoặc dùng độ lệch nửa giờ, một phần tư giờ. **Đường đổi ngày quốc tế (International Date Line)** cũng là một quy ước được uốn quanh lãnh thổ để tránh chia ngày bất tiện.

## UTC và dấu thời gian trong công nghệ thông tin

**UTC — Giờ Phối hợp Quốc tế (Coordinated Universal Time)** là mốc thời gian chuẩn. Địa lý giúp giải thích vì sao phần mềm thường nên lưu **dấu thời gian (timestamp)** theo UTC rồi chuyển sang giờ địa phương ở lớp hiển thị. Một ngày–giờ không có thông tin múi giờ dễ gây lỗi khi lập lịch xuyên quốc gia, xử lý giờ mùa hè hoặc áp dụng quy tắc múi giờ lịch sử.

Ví dụ `2026-09-20 09:00` là chưa đủ thông tin. 09:00 ở Seoul và 09:00 ở London là hai thời điểm khác nhau. Trong hệ thống phân tán, thời gian mang tính địa lý vì người dùng, máy chủ và quy tắc nghiệp vụ tồn tại ở các múi giờ khác nhau.

## Đường đổi ngày và bài toán ngày tháng

Khi đi về phía đông qua Đường đổi ngày quốc tế, ngày trên lịch thường lùi một ngày; đi về phía tây thì tăng một ngày. Điều này không phải do thời gian vật lý “nhảy”, mà do cách con người gán nhãn ngày cho **giờ dân sự địa phương (local civil time)**.

## Những hiểu lầm phổ biến

Một nhầm lẫn phổ biến là kinh độ đồng nghĩa với múi giờ. Hai khái niệm có quan hệ lịch sử–hình học nhưng không ánh xạ một-một. Múi giờ là kết quả của cả địa lý lẫn quyết định xã hội–chính trị. Nhầm lẫn khác là GPS “đo trực tiếp vĩ độ/kinh độ”; thực tế bộ thu suy vị trí từ đo thời gian và khoảng cách tới vệ tinh trong một khung tham chiếu rồi mới chuyển thành tọa độ.

Xem tiếp: [Bản đồ, tỷ lệ và phép chiếu](./03_cartography_projections_scale.md), [GIS và viễn thám](./04_geospatial_data_gis_remote_sensing.md).
