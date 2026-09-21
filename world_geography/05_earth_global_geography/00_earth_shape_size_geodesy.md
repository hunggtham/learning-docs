# Hình dạng, kích thước và phép đo Địa cầu

## Trái Đất không phải hình cầu toán học

Trong nhiều bài toán cơ bản, Trái Đất được xem như hình cầu vì mô hình này đủ đơn giản và sai số chấp nhận được. Nhưng hình dạng thực gần với **khối cầu dẹt (oblate spheroid)**: bán kính xích đạo lớn hơn bán kính cực do chuyển động quay tạo hiệu ứng ly tâm. Khi cần định vị chính xác, người ta dùng **ellipsoid tham chiếu (reference ellipsoid)** thay vì một bán kính duy nhất.

Ellipsoid vẫn chưa phải “bề mặt vật lý thật”. Núi, rãnh biển và sự phân bố không đều của khối lượng làm trường hấp dẫn biến thiên. Vì vậy trắc địa còn dùng **geoid** — bề mặt đẳng thế của trường hấp dẫn gần tương ứng với mực nước biển trung bình nếu đại dương có thể kéo dài xuyên lục địa và không bị gió, dòng biển hay thủy triều làm nhiễu.

Ba bề mặt cần phân biệt là **địa hình thật**, **ellipsoid toán học** và **geoid vật lý**. GPS thường cho độ cao ellipsoid; độ cao mà kỹ sư gọi là “cao hơn mực nước biển” gần với độ cao trực chuẩn so với geoid. Quan hệ thường được viết gần đúng:

\[
h = H + N
\]

trong đó \(h\) là độ cao ellipsoid, \(H\) là độ cao trực chuẩn và \(N\) là độ cao geoid so với ellipsoid. Nếu bỏ qua sự khác nhau này, một hệ thống khảo sát có thể sai hàng chục mét theo phương thẳng đứng dù tọa độ ngang trông chính xác.

## Kích thước và trực giác về quy mô

Chu vi Trái Đất vào khoảng bốn mươi nghìn kilômét. Con số này quan trọng không phải để học thuộc, mà để tạo trực giác về quy mô. Một độ vĩ độ tương ứng xấp xỉ hơn một trăm kilômét; một chuyến bay xuyên lục địa chỉ bao phủ một phần nhỏ chu vi; vệ tinh quỹ đạo thấp vẫn ở rất gần bề mặt nếu so với bán kính Trái Đất.

Quy mô cũng giải thích vì sao đường thẳng trên bản đồ phẳng có thể không phải đường ngắn nhất trên Địa cầu. Trên mặt cầu, tuyến ngắn nhất là cung của **vòng tròn lớn (great circle)**. Khi bản đồ dùng phép chiếu Mercator, cung đó thường trông cong. Đây không phải máy bay “bay vòng” mà là hệ quả của việc trải mặt cong lên mặt phẳng.

## Trắc địa là gì?

**Trắc địa (geodesy / 측지학)** nghiên cứu hình dạng, kích thước, trường hấp dẫn và chuyển động của Trái Đất cùng cách xác định vị trí trên đó. Trắc địa hiện đại kết hợp GNSS, vệ tinh đo trọng lực, radar giao thoa, đo cao vệ tinh và mạng mốc mặt đất.

Điểm quan trọng là tọa độ không tồn tại độc lập với **datum**. Một datum quy định ellipsoid, vị trí–hướng của ellipsoid so với Trái Đất và trong hệ hiện đại còn có epoch thời gian. Vì các mảng kiến tạo chuyển động vài centimet mỗi năm, một tọa độ centimet-level mà không ghi thời điểm có thể trở nên mơ hồ sau nhiều năm.

## Trái Đất còn biến dạng theo thời gian

Bề mặt không chỉ thay đổi vì động đất. Thủy triều rắn làm vỏ Trái Đất co giãn nhỏ dưới hấp dẫn Mặt Trăng và Mặt Trời; tải băng, nước ngầm và khí quyển làm vỏ uốn; sau khi tấm băng cổ tan, **điều chỉnh đẳng tĩnh hậu băng hà (glacial isostatic adjustment)** khiến một số vùng vẫn đang nâng lên.

Do đó “độ cao tuyệt đối” không phải đại lượng hoàn toàn bất biến. Trong kỹ thuật độ chính xác cao, cần biết hệ quy chiếu, mô hình geoid và thời điểm quan trắc.

## Từ bản đồ học sang phần mềm

Trong ứng dụng GIS, sai datum có thể làm hai lớp dữ liệu lệch nhau dù cùng ghi vĩ độ–kinh độ. Trong xây dựng và drone mapping, nhầm giữa ellipsoid height và orthometric height có thể gây lỗi cao độ. Trong hệ thống toàn cầu, tọa độ nên được coi như một **giá trị có kiểu dữ liệu**, bao gồm CRS và epoch chứ không chỉ hai hoặc ba con số.

## Mô hình tư duy

> Địa cầu có ba lớp hình học: **bề mặt địa hình thật**, **ellipsoid để tính toán** và **geoid gắn với trường hấp dẫn**. Mọi phép đo vị trí chính xác đều là phép đo “so với một mô hình tham chiếu”, không phải đọc trực tiếp một tọa độ tuyệt đối từ thiên nhiên.

Xem tiếp: [Hệ quy chiếu toàn cầu](./06_global_reference_systems.md), [Tọa độ và thời gian](../00_foundations/02_coordinates_time_maps.md).