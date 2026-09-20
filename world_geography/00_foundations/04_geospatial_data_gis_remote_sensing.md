# Dữ liệu không gian, GIS và viễn thám

## GIS giải quyết vấn đề gì?

Khi câu hỏi chứa “ở đâu”, “gần cái gì”, “nằm trong vùng nào”, “đường nào tối ưu”, “khu vực nào overlap”, database thông thường chưa đủ tiện. **GIS — Geographic Information System (hệ thống thông tin địa lý / 지리정보시스템)** kết hợp dữ liệu, geometry, analysis và visualization để làm việc với spatial relationships.

## Vector và raster

Hai representation cơ bản là **vector** và **raster**. Vector dùng point, line, polygon để biểu diễn object có boundary tương đối rõ: trạm, đường, parcel, district. Raster chia không gian thành grid cells; mỗi cell có value như elevation, temperature hoặc reflectance.

Vector phù hợp topology và object identity. Raster phù hợp continuous field và cell-wise modeling. Nhiều workflow chuyển qua lại giữa hai dạng; lựa chọn không phải “cái nào hiện đại hơn” mà phụ thuộc phenomenon.

## Geometry, attribute và spatial relation

Một feature không chỉ có geometry mà còn attribute. Ví dụ hospital point có name, capacity, specialty. GIS có thể hỏi “mọi hộ dân trong 15 phút lái xe đến hospital nào?” — đây không phải simple filtering mà là network accessibility.

Các spatial predicates như `within`, `contains`, `intersects`, `touches`, `overlaps`, `nearest` có ý nghĩa toán học/topological rõ. Trong PostGIS, chúng trở thành query primitives. Spatial index như R-tree/GiST giảm search space bằng bounding box trước khi chạy exact geometry calculation.

## Remote sensing: đo từ xa thay vì đến từng điểm

**Remote sensing (viễn thám / 원격탐사)** thu thông tin về bề mặt từ sensor trên satellite, aircraft hoặc drone. Sensor không “nhìn thấy land cover” như con người; nó đo electromagnetic energy ở nhiều wavelength bands. Vegetation, water, snow và built-up surfaces phản xạ/ hấp thụ khác nhau, tạo spectral signatures.

Một chỉ số nổi tiếng là NDVI:

\[
NDVI=\frac{NIR-Red}{NIR+Red}
\]

Healthy vegetation thường phản xạ mạnh near-infrared và hấp thụ red cho photosynthesis, nên NDVI tăng. Nhưng NDVI không phải “máy đo sức khỏe cây tuyệt đối”; cloud, soil background, sensor calibration, season và vegetation type đều ảnh hưởng.

## Resolution: không chỉ là pixel nhỏ hay lớn

Remote sensing có nhiều loại resolution. **Spatial resolution** là kích thước pixel. **Temporal resolution** là tần suất revisit. **Spectral resolution** là số và độ hẹp wavelength bands. **Radiometric resolution** là khả năng phân biệt mức năng lượng.

Một sensor pixel 30 m không phải “thấp hơn” 1 m trong mọi task. Theo dõi crop vùng lớn hoặc climate trend có thể ưu tiên revisit và consistency hơn detail cực cao.

## DEM và terrain analysis

**DEM — Digital Elevation Model (mô hình số độ cao / 수치표고모델)** cho phép tính slope, aspect, watershed, viewshed và flow direction. Đây là bridge giữa geometry và physical process: chỉ từ elevation field, ta có thể suy nhiều cấu trúc drainage bằng giả định nước chảy theo gradient thấp nhất.

## Geocoding và reverse geocoding

Geocoding chuyển address thành coordinate; reverse geocoding làm ngược lại. Address là dữ liệu xã hội, không hoàn toàn geometric: street naming, building numbering và administrative boundaries khác giữa quốc gia. Vì vậy geocoder cần reference data và local rules.

## GPS/GNSS và uncertainty

Location measurement luôn có error. GPS phone có thể lệch do multipath ở urban canyon, atmospheric delay hoặc satellite geometry. Trong analysis, coordinate không nên mặc định là exact point. Một số task cần uncertainty buffer hoặc probabilistic location.

## GIS trong IT

Một stack phổ biến có thể gồm spatial database, tile server, geocoding service và frontend map. Database lưu geometry + spatial index; backend chạy spatial query; tile/vector tile giảm payload; frontend render theo zoom. Khi hệ có hàng triệu features, architecture cần partitioning, simplification và caching theo space.

## Mental Model

Hãy coi GIS là **database + geometry engine + coordinate system + visualization**, còn remote sensing là **measurement pipeline từ electromagnetic signal → calibrated data → inferred geographic variable**. Sai ở reference system, measurement hoặc inference đều có thể tạo map đẹp nhưng conclusion sai.

Xem tiếp: [Địa lý + IT/GIS/Data](../90_connections/01_geography_it_gis_data.md), [Khí hậu](../01_physical_geography/03_global_climate_system.md).
