# Dữ liệu không gian, GIS và viễn thám

> **Mạch đọc:** Đọc **Dữ liệu không gian, GIS và viễn thám** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **GIS không phải chỉ là phần mềm vẽ bản đồ** sang **Từ thế giới thật tới dữ liệu: observation mô hình (model / 모델)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## GIS không phải chỉ là phần mềm vẽ bản đồ

**GIS — Hệ thống thông tin địa lý (Geographic Information System / 지리정보시스템)** là tập hợp mô hình dữ liệu, hệ quy chiếu, phép toán, cơ sở dữ liệu và trực quan hóa dùng để trả lời câu hỏi có yếu tố không gian.

Nếu câu hỏi chứa “ở đâu?”, “gần gì?”, “nằm trong vùng nào?”, “đi theo tuyến nào?”, “khu vực nào chồng lấn?” hoặc “mẫu có tạo cụm không?”, GIS cung cấp cấu trúc để biến câu hỏi thành phép phân tích có thể kiểm tra.

Quan trọng nhất: **GIS không biến dữ liệu xấu thành kiến thức tốt**. Sai ở đo lường, CRS, thời điểm hay cách lấy mẫu có thể tạo một bản đồ rất đẹp nhưng kết luận sai.

## Từ thế giới thật tới dữ liệu: observation mô hình (model / 모델)

Trước khi chọn véc-tơ (vector / 벡터) hay raster, cần hỏi **ta đang đo cái gì?** Đường bờ biển không có một vị trí duy nhất ở mọi tỷ lệ; “khu đô thị” phụ thuộc định nghĩa; nhiệt độ là trường liên tục nhưng trạm thời tiết chỉ đo tại các điểm.

Chuỗi suy luận nên là:

**hiện tượng thật → cảm biến/điều tra → quan sát → xử lý → mô hình dữ liệu → phân tích → kết luận**.

Mỗi mũi tên đều có giả định và sai số. Đây là **mô hình quan sát (observation model)**, nền tảng để tránh nhầm dữ liệu với thực tại.

## Véc-tơ (vector / 벡터) và raster biểu diễn hai cách nhìn khác nhau

**véc-tơ (vector / 벡터)** dùng điểm, đường, đa giác cho đối tượng rời rạc: trạm, đường, thửa đất, ranh giới. **Raster** chia không gian thành ô, phù hợp trường liên tục hoặc ảnh: độ cao, nhiệt độ, phản xạ quang học.

Không có mô hình “tốt hơn” tuyệt đối. Chuyển véc-tơ (vector / 벡터) sang raster đòi chọn kích thước ô; chuyển raster sang polygon đòi chọn ngưỡng và có thể tạo ranh giới giả. Mỗi phép chuyển đổi đưa thêm giả định.

## CRS là một phần của kiểu dữ liệu

Hai số `x, y` không đủ. Cần **CRS — Coordinate tham chiếu (reference / 참조) hệ thống (system / 시스템)** để biết gốc, đơn vị, datum và phép chiếu. Vĩ độ–kinh độ thường là góc; hệ projected có thể dùng mét.

Nếu dùng buffer `1000` trên dữ liệu độ mà tưởng là mét, lỗi lô-gic (logic / 논리) có thể rất lớn. Vì vậy trong API và cơ sở dữ liệu (database / 데이터베이스), CRS nên được coi như **đơn vị (unit / 단위)/kiểu (type / 타입) đặc tả hợp đồng (contract / 계약)**, không phải siêu dữ liệu (metadata / 메타데이터) tùy chọn.

## Topology: “nối với nhau thế nào?” khác “cách nhau bao xa?”

GIS quan tâm **topology**: đường nào nối nhau, polygon nào kề nhau, điểm có nằm trong polygon không. Hai đoạn đường nhìn chạm trên màn hình nhưng nút (node / 노드) không snap chính xác có thể làm routing bị đứt.

Các quan hệ `within`, `contains`, `intersects`, `touches`, `overlaps` có nghĩa hình học cụ thể. Cần chọn đúng predicate thay vì dùng bounding box như kết quả cuối.

## Spatial phép nối (join / 조인) là phép nối theo quan hệ không gian

Trong SQL thông thường ta phép nối (join / 조인) bằng ID. Trong GIS ta có thể phép nối (join / 조인) “điểm cửa hàng nằm trong quận nào?”, “trường học gần trạm tàu nhất?”, hoặc “đoạn đường nào cắt vùng ngập?”.

**Spatial phép nối (join / 조인)** rất mạnh nhưng dễ nhân bản bản ghi khi một tính năng (feature / 기능) khớp nhiều tính năng (feature / 기능). Vì vậy sau phép nối (join / 조인) cần hiểu cardinality và quy tắc tổng hợp.

## Chỉ mục không gian: lọc ứng viên trước, tính chính xác sau

Tính giao polygon phức tạp cho hàng triệu đối tượng rất đắt. **Spatial chỉ mục (index / 인덱스)** như R-tree/GiST dùng bounding box hoặc cấu trúc phân cấp để loại phần lớn ứng viên, rồi mới chạy phép hình học chính xác.

Đây là mẫu (pattern / 패턴) tương tự tìm kiếm (search / 검색) engine: bước đầu thu hẹp candidates, bước sau tính score chính xác.

## Distance: planar, geodesic và mạng (network / 네트워크)

Khoảng cách Euclid trên bản đồ phẳng phù hợp phạm vi nhỏ với projection thích hợp. Trên phạm vi lớn cần **geodesic distance** trên ellipsoid/mặt cầu. Đối với đi lại, khoảng cách đúng thường là **mạng (network / 네트워크) distance/thời gian (time / 시간)**, không phải đường chim bay.

Chọn sai distance mô hình (model / 모델) là một lỗi khái niệm, không chỉ lỗi kỹ thuật.

## Raster: resolution, extent và resampling

Raster có kích thước điểm ảnh (pixel / 픽셀), phạm vi và alignment. Hai raster cùng độ phân giải nhưng lệch origin không thể cộng trực tiếp mà không resample.

Khi đổi resolution, **nearest neighbor** phù hợp lớp phân loại; bilinear/cubic phù hợp hơn dữ liệu liên tục nhưng làm thay đổi giá trị. Resampling không tạo thông tin mới; nó chỉ nội suy hoặc tái biểu diễn dữ liệu đã có.

## Viễn thám đo bức xạ chứ không “nhìn thấy đối tượng”

Cảm biến ghi năng lượng điện từ ở các dải bước sóng. Từ đó ta suy lớp phủ đất, độ ẩm, nhiệt bề mặt hoặc thảm thực vật.

**Dấu hiệu phổ (spectral signature)** khác nhau giữa nước, đất, thực vật và vật liệu xây dựng, nhưng bị ảnh hưởng bởi góc Mặt Trời, khí quyển, mùa và độ ẩm. Vì vậy classification là suy luận, không phải nhãn được vệ tinh đọc trực tiếp.

## Bốn loại độ phân giải

Trước khi chọn sensor hoặc sản phẩm raster, cần xác định mình đang tối ưu cho kích thước không gian, tần suất thời gian, dải phổ hay độ nhạy tín hiệu. Bốn loại resolution trả lời bốn câu hỏi khác nhau và không thể thay thế lẫn nhau.

- **Spatial resolution:** kích thước pixel.
- **Temporal resolution:** tần suất quan sát lại.
- **Spectral resolution:** số và độ hẹp dải phổ.
- **Radiometric resolution:** khả năng phân biệt mức tín hiệu.

Không có sensor tốt nhất cho mọi bài toán. Theo dõi cây trồng theo tuần có thể ưu tiên temporal resolution; nhận diện mái nhà cần spatial resolution cao hơn.

## NDVI và giới hạn của chỉ mục (index / 인덱스)

\[
NDVI=\frac{NIR-Red}{NIR+Red}
\]

NDVI tận dụng việc thực vật khỏe thường phản xạ NIR mạnh và hấp thụ đỏ. Nhưng NDVI có thể bão hòa ở tán dày, bị ảnh hưởng nền đất, mây và mùa. Một chỉ mục (index / 인덱스) là **proxy**, không phải biến sinh học cần đo trực tiếp.

## Atmospheric correction, cloud mask và preprocessing

Ảnh thô chứa ảnh hưởng của khí quyển, hình học cảm biến và mây. Trước khi so chuỗi thời gian, cần kiểm tra mức sản phẩm, hiệu chỉnh, mask mây và tính nhất quán giữa cảm biến.

Nếu ảnh năm A dùng surface reflectance còn năm B dùng top-of-atmosphere reflectance, chênh lệch có thể đến từ chuỗi xử lý (pipeline / 파이프라인) thay vì thay đổi bề mặt.

## DEM và dòng chảy

**DEM — Digital Elevation mô hình (model / 모델)** cho phép tính slope, aspect, luồng (flow / 흐름) direction và watershed. Nhưng DEM chứa sink giả, lỗi đo và ảnh hưởng của cây/công trình tùy loại sản phẩm.

Hydrologic preprocessing như fill/breach depression có thể cần thiết, nhưng cũng là quyết định mô hình. Không nên coi mọi dòng suy ra từ DEM là sông thật.

## Mạng (network / 네트워크) phân tích (analysis / 분석) và routing

Bản đồ đường được chuyển thành đồ thị (graph / 그래프) với nút (node / 노드) và edge. Trọng số có thể là thời gian, khoảng cách, phí hoặc tổng chi phí. Routing thực tế còn cần one-way, turn restriction, lịch phà và tốc độ theo thời gian.

**A***, Dijkstra và contraction hierarchy là thuật toán; chất lượng kết quả vẫn phụ thuộc chất lượng đồ thị (graph / 그래프) và chi phí (cost / 비용) mô hình (model / 모델).

## Spatial autocorrelation và thống kê không gian

Dữ liệu gần nhau thường không độc lập. **Moran's I** hoặc các công cụ cluster giúp đo spatial autocorrelation, nhưng cluster thống kê không tự nói nguyên nhân.

Nếu train/kiểm thử (test / 테스트) machine học tập (learning / 학습) bằng cách chia ngẫu nhiên điểm ảnh (pixel / 픽셀) liền kề, mô hình có thể hưởng lợi từ **spatial leakage** và đánh giá quá lạc quan. Spatial cross-validation theo khối (block / 블록) hoặc vùng thường phù hợp hơn cho khả năng tổng quát địa lý.

## Geocoding và địa chỉ là dữ liệu xã hội

**Geocoding** chuyển địa chỉ thành tọa độ. Địa chỉ không phải format toàn cầu thống nhất: thứ tự thành phần, tên đường, số nhà và đơn vị hành chính khác nhau theo quốc gia.

Một geocoder trả điểm không có nghĩa vị trí chính xác tới cửa. Cần lưu chất lượng (quality / 품질) score hoặc match kiểu (type / 타입) nếu ứng dụng nhạy với sai số.

## GNSS và bất định (uncertainty / 불확실성)

GNSS suy vị trí từ tín hiệu vệ tinh trong hệ tham chiếu. Sai số đến từ khí quyển, multipath, hình học (geometry / 기하학) vệ tinh và môi trường đô thị.

Đối với geofencing nhỏ, một tọa độ nên được hiểu cùng **bất định (uncertainty / 불확실성) radius**. Nếu lô-gic (logic / 논리) nghiệp vụ kích hoạt đúng tại ranh giới, hysteresis hoặc dwell thời gian (time / 시간) giúp giảm trạng thái vào–ra liên tục do nhiễu.

## Dữ liệu thời gian–không gian

Nhiều hiện tượng thay đổi theo thời gian: traffic, nhiệt độ, vị trí tàu, sử dụng đất. Lưu chỉ hình học (geometry / 기하학) hiện tại sẽ mất lịch sử.

Thiết kế **spatiotemporal dữ liệu (data / 데이터)** cần timestamp/validity interval và cân nhắc đối tượng (object / 객체) thay đổi hình học. Câu hỏi “ở đâu?” thường phải đi cùng “khi nào?”.

## Kiểm tra hợp lệ (validation / 검증): accuracy không chỉ là một số

Bản đồ phân loại cần ground truth và confusion ma trận (matrix / 행렬). Với dữ liệu điểm, positional accuracy khác attribute accuracy. Với polygon, ranh giới có thể uncertain dù lớp (class / 클래스) đúng.

Kiểm tra hợp lệ (validation / 검증) mẫu (sample / 표본) phải đại diện không gian; chỉ lấy mẫu gần đường sẽ độ lệch (bias / 편향) vùng dễ tiếp cận.

## Ethics và privacy của location dữ liệu (data / 데이터)

Quỹ đạo vị trí có thể tái nhận dạng dù bỏ tên vì nhà–nơi làm việc tạo dấu vết riêng. Nên giảm độ chính xác hoặc tổng hợp khi mục tiêu không cần vị trí chi tiết, giới hạn retention và phân quyền truy cập.

Bản đồ cũng có thể làm lộ vị trí nhạy cảm. “Có thể vẽ” không đồng nghĩa “nên công bố”.

## Workflow GIS đáng tin cậy

1. Xác định hiện tượng và câu hỏi.
2. Kiểm tra nguồn (source / 소스), thời gian, CRS, resolution và bất định (uncertainty / 불확실성).
3. Làm sạch hình học (geometry / 기하학)/attribute.
4. Chọn phép toán phù hợp với quy mô (scale / 규모).
5. kiểm tra hợp lệ (validation / 검증) bằng dữ liệu độc lập.
6. Trực quan hóa mà không che bất định (uncertainty / 불확실성).
7. Ghi lại provenance để có thể tái lập.

## Mô hình tư duy

> GIS là **đo lường (measurement / 측정) mô hình (model / 모델) + coordinate hệ thống (system / 시스템) + spatial cơ sở dữ liệu (database / 데이터베이스) + phân tích (analysis / 분석) + visualization**. Viễn thám là chuỗi **bức xạ → cảm biến → preprocessing → tính năng (feature / 기능)/proxy → kiểm tra hợp lệ (validation / 검증)**. Luôn hỏi dữ liệu đã trải qua biến đổi nào trước khi trở thành điểm ảnh (pixel / 픽셀) hoặc polygon mà bạn nhìn thấy.

Xem tiếp: [Bản đồ và phép chiếu](./03_cartography_projections_scale.md), [Địa lý + IT/GIS/Data](../90_connections/01_geography_it_gis_data.md), [Thủy văn](../01_physical_geography/04_hydrology_rivers_groundwater.md).
