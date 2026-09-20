# Hệ tọa độ, Trái Đất quay và thời gian

## Vấn đề cơ bản: làm sao nói chính xác “ở đâu” trên một bề mặt cong?

Nếu chỉ dùng mô tả như “phía đông ngọn núi” hoặc “gần biển”, việc định vị không thể toàn cầu hóa. Ta cần một reference system chung. **Geographic coordinate system (hệ tọa độ địa lý / 지리 좌표계)** dùng hai góc: latitude và longitude.

**Latitude (vĩ độ / 위도)** đo góc bắc–nam so với Equator. Equator là 0°, poles là ±90°. **Longitude (kinh độ / 경도)** đo góc đông–tây so với Prime Meridian, convention hiện đại đặt qua Greenwich, từ 0° đến ±180°.

Điểm tinh tế là latitude và longitude là **angular coordinates**, không phải khoảng cách mét. Một độ longitude gần Equator dài hơn nhiều so với một độ longitude gần cực vì meridian hội tụ.

## Earth không phải sphere hoàn hảo

Trái Đất gần một **oblate spheroid**: hơi phình ở Equator. Mapping chính xác còn dùng **ellipsoid** và **geodetic datum (trắc địa datum / 측지 기준계)**. GPS phổ biến dùng WGS 84. Nếu hai dataset dùng datum khác nhau mà bị ghép như thể cùng hệ, feature có thể lệch vị trí.

Trong GIS, đây là lỗi kinh điển: coordinates “trông hợp lý” nhưng map layer không align. Vì thế luôn cần biết cả coordinate values lẫn **CRS — Coordinate Reference System (hệ quy chiếu tọa độ / 좌표참조체계)**.

## Great-circle distance

Trên sphere, đường ngắn nhất giữa hai điểm không phải luôn là đường thẳng trên bản đồ phẳng mà là **great-circle route (đường vòng lớn / 대권 항로)**. Đây là lý do flight route trên Mercator map thường cong về phía cực.

Khoảng cách xấp xỉ giữa hai tọa độ có thể tính bằng haversine formula:

\[
a=\sin^2\left(\frac{\Delta\varphi}{2}\right)+\cos\varphi_1\cos\varphi_2\sin^2\left(\frac{\Delta\lambda}{2}\right)
\]
\[
c=2\arctan2(\sqrt a,\sqrt{1-a}),\qquad d=Rc
\]

\(\varphi\) là latitude theo radian, \(\lambda\) là longitude, \(R\) là bán kính Trái Đất xấp xỉ. Model sphere đủ tốt cho nhiều ứng dụng; geodesy chính xác cao dùng ellipsoid.

Connection với IT rất trực tiếp: mobile app “tìm địa điểm gần tôi”, geofencing, route pre-filter, spatial database và logistics đều cần distance model phù hợp. Dùng Euclidean distance trực tiếp trên latitude/longitude có thể gây sai số đáng kể ở phạm vi lớn.

## Rotation, local solar time và time zones

Trái Đất quay khoảng một vòng mỗi ngày, nên về geometry 360° longitude tương ứng khoảng 24 giờ, tức khoảng 15° mỗi giờ. **Local solar time** phụ thuộc vị trí Mặt Trời, nhưng xã hội hiện đại dùng **standard time zones (múi giờ / 표준시)** theo boundary chính trị–hành chính chứ không thuần geometry.

Do đó time zone map không thể suy ra chỉ bằng longitude. Một quốc gia có thể dùng một múi giờ cho toàn lãnh thổ rộng, hoặc dùng half-hour/quarter-hour offsets. **International Date Line** cũng là convention bị bẻ quanh territory để tránh chia ngày bất tiện.

## UTC và timestamp trong IT

**UTC — Coordinated Universal Time** là reference time chuẩn. Geography giúp hiểu vì sao software nên lưu timestamp theo UTC và convert sang local time ở presentation layer. Một datetime không có timezone context dễ trở thành bug khi scheduling qua quốc gia, daylight saving time hoặc historical timezone rule.

Ví dụ `2026-09-20 09:00` là không đủ thông tin. 09:00 ở Seoul và 09:00 ở London là hai instant khác nhau. Trong distributed systems, “time is geographic” vì user, server và business rule tồn tại ở các time zone khác nhau.

## Dateline và bài toán ngày tháng

Khi đi về phía đông qua International Date Line, calendar date thường lùi một ngày; đi về phía tây thì tăng một ngày. Điều này không phải do thời gian vật lý “nhảy”, mà do cách đặt label date cho local civil time.

## Common Misconceptions

Một nhầm lẫn phổ biến là longitude = timezone. Chỉ có quan hệ lịch sử–hình học, không phải mapping một-một. Time zones là socio-political geometry. Nhầm lẫn khác là GPS “đo trực tiếp latitude/longitude”; thực tế receiver suy vị trí từ timing/ranging với vệ tinh trong một reference frame rồi chuyển thành coordinates.

Xem tiếp: [Bản đồ, scale và phép chiếu](./03_cartography_projections_scale.md), [GIS và remote sensing](./04_geospatial_data_gis_remote_sensing.md).
