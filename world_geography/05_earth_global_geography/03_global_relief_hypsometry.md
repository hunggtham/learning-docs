# Độ cao toàn cầu, hypsometry và logic của địa hình hành tinh

## Cực trị không quan trọng bằng phân bố

Everest và Mariana giúp hình dung giới hạn cao–sâu, nhưng địa lý hành tinh quan tâm nhiều hơn tới **phân bố (distribution)** của toàn bộ bề mặt. Nếu sắp diện tích Trái Đất theo độ cao từ sâu nhất đến cao nhất, ta có **đường cong cao–sâu (hypsometric curve)**.

Đường cong cho thấy hai miền lớn: phần lớn đáy đại dương quanh một miền sâu và phần lớn lục địa quanh miền cao hơn. Đây là dấu vết thống kê của khác biệt giữa vỏ đại dương và vỏ lục địa.

Một mental model quan trọng: **extreme cho biết giới hạn; distribution cho biết cấu trúc của hệ**.

## Hypsometry là gì?

**Hypsometry** nghiên cứu phân bố diện tích theo độ cao hoặc độ sâu. Ta có thể dùng nó ở quy mô toàn hành tinh, một lưu vực hoặc một vùng núi.

Ở quy mô lưu vực, đường cong hypsometric cho biết tỷ lệ diện tích còn nằm trên từng mức cao độ và có thể cung cấp trực giác về mức độ phân cắt, lịch sử xói mòn và hình thái địa hình. Tuy nhiên không nên biến đường cong thành “máy đo tuổi địa hình” đơn giản, vì kiến tạo, lithology và climate có thể tạo hình dạng tương tự qua cơ chế khác nhau.

## Độ cao là trường thế năng

Địa hình không chỉ là hình dạng. Chênh cao tạo **thế năng trọng trường (gravitational potential energy)**, từ đó điều khiển dòng nước, chuyển động khối, glacier và nhiều dạng vận chuyển trầm tích.

Nước có xu hướng chảy từ potential cao về thấp, nhưng đường đi thực tế còn phụ thuộc địa hình vi mô, độ thấm, cống, kênh và cấu trúc ngầm. Vì vậy DEM rất mạnh nhưng không phải toàn bộ thủy văn.

## Độ cao và khí quyển

Khi lên cao, áp suất khí quyển giảm. Trong tầng đối lưu, nhiệt độ thường giảm theo độ cao nhưng **suất giảm nhiệt (lapse rate)** thay đổi giữa không khí khô, không khí bão hòa và điều kiện khí quyển thực tế.

Một mountain range vì thế tạo **phân đai cao (altitudinal zonation)**: chỉ trong vài kilomet theo phương đứng có thể chuyển qua các điều kiện nhiệt–ẩm tương tự việc di chuyển hàng nghìn kilomet theo vĩ độ.

Điều này nối relief với biome, agriculture, settlement và risk.

## Orographic effect: núi tổ chức lại khí hậu vùng

Khi gió ẩm bị buộc nâng qua núi, không khí giãn nở và nguội, làm tăng khả năng ngưng tụ ở sườn đón gió. Sau khi vượt đỉnh và hạ xuống, không khí có thể nóng lên và khô hơn, tạo **bóng mưa (rain shadow)**.

Vì vậy một dãy núi không chỉ là obstacle giao thông. Nó là một **bộ biến đổi khí hậu (climate transformer)** có thể chia hai phía thành hệ nước, đất và settlement khác nhau.

## Đẳng tĩnh: núi có phần “ẩn” bên dưới

Theo **đẳng tĩnh (isostasy)**, thạch quyển có xu hướng đạt cân bằng nổi trên lớp vật chất sâu có khả năng biến dạng chậm. Vùng vỏ dày và nhẹ có thể có “rễ” sâu giống tảng băng nổi.

Khi xói mòn lấy vật liệu khỏi dãy núi, giảm tải có thể dẫn tới **nâng đẳng tĩnh (isostatic rebound)**. Vì vậy surface lowering do erosion và crustal uplift có thể xảy ra đồng thời.

Điều này phá vỡ trực giác đơn giản “núi chỉ có thể cao lên hoặc thấp xuống”. Relief là kết quả của nhiều quá trình cạnh tranh.

## Base level và relief energy

Sông xói mòn theo chênh lệch giữa địa hình và **mực cơ sở (base level)**, thường liên hệ với sea level hoặc hồ lớn. Khi tectonic uplift làm land surface cao lên hoặc sea level thay đổi, gradient river có thể đổi, kích hoạt incision hoặc deposition.

Khái niệm **relief energy** có thể hiểu như lượng chênh cao sẵn có cho gravity-driven process. Vùng relief mạnh thường có river gradient lớn, landslide potential cao và chi phí infrastructure khác với plain.

## Đồng bằng: ít relief nhưng không ít động lực

Lowland và delta có relief nhỏ nhưng là nơi vật chất từ basin tích tụ. Chúng có thể cực kỳ năng động vì river avulsion, sedimentation, subsidence và flooding.

Lợi thế gồm đất bằng, nước và transport; rủi ro gồm flood, waterlogging, salinity và relative sea-level rise. Đây là ví dụ điển hình của chuỗi:

**low relief → accessibility + agriculture + urban concentration → high exposure to hydrologic/coastal hazards**.

## Độ sâu đại dương và áp suất

Trong nước biển, áp suất tăng xấp xỉ khoảng một atmosphere mỗi 10 mét. Ở abyssal depth, áp suất là ràng buộc lớn với sinh vật, cảm biến, tàu lặn và hạ tầng.

Bathymetry còn điều khiển dòng sâu. Ridge, sill và basin có thể hướng hoặc chặn water mass, ảnh hưởng thông khí đại dương và vận chuyển nhiệt.

## DEM, DSM và sai số đo địa hình

**DEM (Digital Elevation Model)** thường biểu diễn trường độ cao của terrain; **DSM (Digital Surface Model)** có thể chứa cả cây và công trình tùy nguồn dữ liệu. Trong ứng dụng đô thị, nhầm terrain với surface có thể làm sai viewshed, drainage hoặc flood model.

Độ phân giải pixel cao không đảm bảo độ chính xác cao. Sai số thẳng đứng, datum, vegetation, interpolation và acquisition method đều quan trọng.

Khi GIS tính slope, aspect hoặc watershed, sai số của DEM có thể được khuếch đại ở các phép đạo hàm không gian. Vì vậy cần xem metadata và kiểm định thực địa khi quyết định có tính kỹ thuật.

## Hypsometry và dân cư

Dân cư toàn cầu tập trung không đồng đều theo độ cao. Nhiều megacity nằm ở coastal plain, river basin hoặc plateau có điều kiện khí hậu–giao thông thuận lợi.

Nhưng không có định luật “thấp = đông dân”. Highland có thể hấp dẫn vì khí hậu mát, phòng thủ lịch sử, đất núi lửa hoặc basin nội sơn. Relief tạo constraint và opportunity; history, technology và institution quyết định kết quả cụ thể.

## Hạ tầng và chi phí relief

Rail, highway, pipeline và urban expansion phản ứng mạnh với slope. Tăng độ dốc làm earthwork, tunnel, bridge và energy cost tăng. Mountain pass vì thế trở thành **network bottleneck**; tunnel mới có thể thay đổi effective distance giữa hai vùng mà khoảng cách hình học không đổi.

Đây là nơi physical geography nối trực tiếp với transport geography.

## Những hiểu lầm phổ biến

“Độ cao càng lớn thì càng lạnh” chỉ là xu hướng nền, không phải quy tắc tuyệt đối cho mọi thời điểm. Inversion có thể làm basin lạnh hơn slope ở một số đêm.

“Đồng bằng là địa hình ổn định” sai: delta và floodplain thường thay đổi rất nhanh về river channel và sediment. “DEM là mặt đất thật” cũng sai; nó là mô hình đo–nội suy có độ phân giải và sai số.

## Mô hình tư duy

> Relief là **trường thế năng + bề mặt điều khiển dòng + ràng buộc cho settlement và infrastructure**. Đọc elevation map bằng cách hỏi ba tầng: nó được tạo bởi tectonic/erosional process nào, nó điều khiển water/climate thế nào, và con người tận dụng hay phải trả chi phí gì cho cấu trúc đó?

Xem tiếp: [Lục địa và bồn đại dương](./02_continents_ocean_basins.md), [Địa mạo](../01_physical_geography/01_landforms_geomorphology.md), [Thủy văn](../01_physical_geography/04_hydrology_rivers_groundwater.md), [Transport](../02_human_geography/08_transport_trade_globalization.md).