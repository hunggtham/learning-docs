# Hệ tọa độ, vị trí và thời gian

## Vị trí không chỉ là hai con số

Trong địa lý, câu hỏi “ở đâu?” nghe đơn giản nhưng thực tế chứa nhiều lớp. Một vị trí có thể được mô tả bằng tên địa danh, địa chỉ, khoảng cách tương đối, tọa độ góc hoặc tọa độ phẳng. Mỗi cách biểu diễn phù hợp với một mục đích khác nhau. Khi cần trao đổi dữ liệu toàn cầu, ta thường dùng **vĩ độ (latitude / 위도)** và **kinh độ (longitude / 경도)**; khi cần đo diện tích, khoảng cách hoặc thi công chính xác, ta thường chuyển sang một **hệ tọa độ chiếu (projected coordinate system)** phù hợp.

Điểm quan trọng là tọa độ không phải thuộc tính tự nhiên tồn tại độc lập. Hai con số chỉ có nghĩa khi biết **hệ quy chiếu tọa độ (Coordinate Reference System, CRS)**, datum, đơn vị, thứ tự trục và trong các hệ động còn cần cả epoch thời gian.

## Vĩ độ và kinh độ là tọa độ góc

**Vĩ độ** đo góc bắc–nam so với mặt phẳng Xích đạo, từ 0° đến ±90°. **Kinh độ** đo góc đông–tây so với kinh tuyến gốc, từ 0° đến ±180°. Chúng là góc, không phải mét.

Một độ vĩ độ có chiều dài khá gần nhau ở nhiều nơi vì các vĩ tuyến được đo dọc kinh tuyến. Một độ kinh độ thì ngắn dần khi tiến về hai cực vì các kinh tuyến hội tụ. Vì vậy không nên lấy chênh lệch vĩ độ–kinh độ rồi dùng trực tiếp như khoảng cách Euclid trên phạm vi lớn.

Trong phần mềm, lỗi còn có thể xuất hiện từ thứ tự trục. Nhiều API quen dùng `longitude, latitude`, trong khi nhiều tài liệu viết `latitude, longitude`. Một hệ thống nên coi thứ tự trục như một **data contract**, không dựa vào trí nhớ của người lập trình.

## Trái Đất thật, ellipsoid và datum

Trái Đất không phải hình cầu hoàn hảo mà gần **khối cầu dẹt (oblate spheroid)**. Để tính toán, trắc địa dùng **ellipsoid tham chiếu (reference ellipsoid)**. Nhưng ellipsoid chỉ mô tả hình học; để gắn nó với Trái Đất thật cần **mốc trắc địa (geodetic datum)**.

Một datum quy định kích thước–hình dạng ellipsoid, cách nó được định hướng và đặt trong không gian, cùng quy ước tọa độ. WGS 84 là một datum/hệ quy chiếu toàn cầu quen thuộc vì được dùng rộng rãi trong GNSS và web mapping.

Hai lớp dữ liệu có cùng các con số nhưng khác datum có thể đại diện cho hai vị trí khác nhau. Ngược lại, cùng một điểm vật lý có thể có bộ tọa độ khác nhau nếu biểu diễn trong hai CRS khác nhau.

## Tọa độ địa tâm và cách GNSS thật sự định vị

GNSS không “đọc vĩ độ–kinh độ trực tiếp”. Vệ tinh phát tín hiệu chứa thông tin thời gian và quỹ đạo. Bộ thu ước lượng khoảng cách tới nhiều vệ tinh rồi giải vị trí trong một khung tọa độ ba chiều gần địa tâm, thường được mô tả bằng **Earth-Centered, Earth-Fixed (ECEF)**. Sau đó vị trí mới được chuyển thành vĩ độ, kinh độ và độ cao ellipsoid.

Điều này giải thích vì sao GNSS cần cả thời gian chính xác lẫn mô hình quỹ đạo. Sai số đồng hồ của bộ thu được giải đồng thời với vị trí khi có đủ vệ tinh quan sát được.

Độ chính xác chịu ảnh hưởng của hình học vệ tinh, khí quyển, phản xạ nhiều đường (multipath), che khuất bởi nhà cao tầng, chất lượng mô hình quỹ đạo và kỹ thuật hiệu chỉnh. Một điểm trên điện thoại vì thế nên được hiểu như **ước lượng có bất định**, không phải chân lý hình học tuyệt đối.

## Khoảng cách trên mặt cong

Trên mô hình mặt cầu, đường ngắn nhất giữa hai điểm nằm trên cung của **vòng tròn lớn (great circle)**. Đây là lý do tuyến bay dài có thể trông cong trên bản đồ Mercator nhưng lại gần tuyến ngắn nhất trên Địa cầu.

Một công thức phổ biến cho khoảng cách mặt cầu là Haversine:

\[
a=\sin^2\left(\frac{\Delta\varphi}{2}\right)+\cos\varphi_1\cos\varphi_2\sin^2\left(\frac{\Delta\lambda}{2}\right)
\]

\[
c=2\arctan2(\sqrt a,\sqrt{1-a}),\qquad d=Rc
\]

Trong đó \(\varphi\) là vĩ độ theo radian, \(\lambda\) là kinh độ và \(R\) là bán kính mô hình. Công thức này phù hợp cho nhiều ứng dụng phổ thông. Khi cần độ chính xác trắc địa cao, phép tính phải dùng ellipsoid thay cho mô hình cầu đơn giản.

Khoảng cách địa lý cũng không phải lúc nào là khoảng cách có ý nghĩa nhất. Đối với vận tải, ta có thể quan tâm **khoảng cách mạng (network distance)**; đối với thương mại, có thể quan tâm thời gian, chi phí hoặc ma sát biên giới; đối với dịch vụ số, có thể quan tâm độ trễ mạng. Vì vậy “gần” là một khái niệm phụ thuộc quá trình đang phân tích.

## Độ cao: ellipsoid khác mực nước biển

GNSS thường cho **độ cao ellipsoid (ellipsoidal height)**, trong khi bản đồ địa hình và kỹ thuật thường cần độ cao so với một bề mặt gần mực nước biển trung bình, tức **độ cao trực chuẩn (orthometric height)** liên quan đến geoid.

Quan hệ gần đúng:

\[
h = H + N
\]

với \(h\) là độ cao ellipsoid, \(H\) là độ cao trực chuẩn và \(N\) là độ cao geoid so với ellipsoid. Nếu một pipeline drone hoặc khảo sát dùng nhầm hai loại độ cao, sai số phương đứng có thể lớn dù tọa độ ngang đúng.

## Trái Đất quay và thời gian địa phương

Trái Đất quay khoảng một vòng mỗi ngày. Về hình học, 360° tương ứng gần 24 giờ, nên 15° kinh độ tương ứng khoảng một giờ của **giờ Mặt Trời địa phương (local solar time)**.

Nhưng xã hội hiện đại không dùng giờ Mặt Trời cho từng kinh tuyến. Chúng ta dùng **múi giờ dân sự (civil time zone)** có ranh giới bị điều chỉnh theo quốc gia, vùng hành chính và nhu cầu kinh tế. Vì vậy kinh độ chỉ giải thích nền hình học của múi giờ, không quyết định trực tiếp múi giờ pháp lý.

## UTC, offset và timezone không phải một thứ

**UTC (Coordinated Universal Time)** là chuẩn thời gian dùng làm mốc toàn cầu. Một **UTC offset** như `+09:00` chỉ mô tả chênh lệch tại một thời điểm; nó không chứa toàn bộ lịch sử và quy tắc của timezone.

Một timezone như `Asia/Seoul` hoặc `Europe/London` là tập quy tắc có thể bao gồm thay đổi lịch sử, daylight saving time và quyết định chính trị. Vì vậy hệ thống phần mềm không nên lưu timezone chỉ bằng offset nếu cần lập lịch dài hạn.

Ví dụ, `2026-09-21 09:00` chưa xác định một thời điểm duy nhất nếu thiếu timezone. `2026-09-21T09:00+09:00` xác định instant rõ hơn, nhưng nếu là lịch họp lặp lại nhiều năm, tên vùng timezone vẫn có giá trị vì quy tắc tương lai có thể đổi.

## Đường đổi ngày quốc tế

**Đường đổi ngày quốc tế (International Date Line)** nằm gần kinh tuyến 180° nhưng không trùng hoàn toàn với một đường thẳng hình học. Nó uốn quanh các lãnh thổ và nhóm đảo để giảm bất tiện hành chính.

Khi vượt đường này, ngày trên lịch thay đổi một ngày. Không có “nhảy thời gian vật lý”; thay đổi nằm ở hệ thống nhãn ngày dân sự.

## Epoch: tọa độ cũng có thời gian

Ở độ chính xác mét, ta thường bỏ qua việc lục địa chuyển động. Ở độ chính xác centimet, điều đó không còn hợp lý. Các mảng kiến tạo dịch chuyển vài centimet mỗi năm; động đất có thể làm tọa độ thay đổi đột ngột.

Do đó các **hệ quy chiếu động (dynamic reference frame)** gắn tọa độ với một **epoch**. Một tọa độ độ chính xác cao nhưng không ghi thời điểm có thể thiếu thông tin quan trọng.

Đây là một mental model hữu ích cho IT: một vị trí chính xác cao giống record có `value + schema + version`. `latitude/longitude` chỉ là value; CRS là schema; epoch là version theo thời gian.

## Múi giờ, bản đồ và các bẫy dữ liệu

Một dataset timezone là dữ liệu polygon xã hội–pháp lý chứ không phải kết quả trực tiếp của toán học thiên văn. Biên giới có thể thay đổi, quy tắc daylight saving có thể bị sửa và cùng một quốc gia có thể dùng nhiều timezone hoặc một timezone rất rộng.

Tương tự, geocoding địa chỉ thành tọa độ không phải phép toán thuần hình học. Địa chỉ thay đổi theo ngôn ngữ, cải cách hành chính, cách đánh số và quy tắc địa phương. Kết quả geocoder nên có provenance và mức tin cậy.

## Mô hình tư duy

Hãy coi vị trí như một cấu trúc nhiều lớp:

**đối tượng thật → hệ tham chiếu → tọa độ → phép biểu diễn → thời điểm → ý nghĩa ứng dụng**.

Một lỗi ở bất kỳ lớp nào cũng có thể làm dữ liệu trông hợp lệ nhưng đặt sai nơi, sai cao độ hoặc sai thời gian.

## Những hiểu lầm phổ biến

GPS không “dùng la bàn để tìm vị trí”; la bàn điện tử và GNSS là cảm biến khác nhau. WGS 84 không đồng nghĩa với mọi bản đồ web; bản đồ web thường lưu vị trí theo WGS 84 nhưng hiển thị qua Web Mercator. Kinh độ không ánh xạ một-một với timezone. Và cùng một cặp tọa độ không có ý nghĩa đầy đủ nếu không biết CRS.

Xem tiếp: [Bản đồ, tỷ lệ và phép chiếu](./03_cartography_projections_scale.md), [GIS và viễn thám](./04_geospatial_data_gis_remote_sensing.md), [Trắc địa và hình dạng Trái Đất](../05_earth_global_geography/00_earth_shape_size_geodesy.md).