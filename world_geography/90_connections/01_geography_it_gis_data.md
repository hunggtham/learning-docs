# Địa lý kết nối với IT, GIS, Kỹ thuật dữ liệu và AI

## Dữ liệu không gian phải được xem là kiểu dữ liệu cốt lõi

Trong ứng dụng thông thường, vị trí hay bị lưu đơn giản thành hai cột vĩ độ và kinh độ rồi xử lý thủ công. Cách này đủ cho vài trường hợp đơn giản, nhưng nhanh chóng trở nên nguy hiểm khi hệ thống phải trả lời những câu hỏi như “điểm này có nằm trong khu vực kia không?”, “đối tượng nào gần nhất?”, “hai vùng có giao nhau không?” hoặc “đường nào có chi phí thấp nhất?”. Khi đó vị trí không còn là hai con số rời rạc mà trở thành một **kiểu dữ liệu có quy tắc hình học**.

Các hệ như PostGIS, SQL Server Spatial hay Oracle Spatial cung cấp các kiểu **hình học/địa lý (`geometry`/`geography`)**, phép toán không gian và chỉ mục chuyên dụng. Điểm quan trọng là không gian phải đi vào thiết kế dữ liệu ngay từ đầu, giống như tiền tệ cần đơn vị và ngày–giờ cần múi giờ.

## Hệ quy chiếu tọa độ là một phần của hợp đồng dữ liệu

Một tọa độ không thể được hiểu chỉ từ hai số `x, y`. Cần biết **hệ quy chiếu tọa độ (CRS — Coordinate Reference System / 좌표 참조 체계)**, thứ tự trục, đơn vị và mốc trắc địa. Tọa độ vĩ độ–kinh độ trong WGS84 và tọa độ phẳng tính theo mét là hai cách biểu diễn khác nhau của cùng một vị trí.

Một lỗi rất phổ biến là nhầm `latitude, longitude` với `x, y`. Trong nhiều thư viện hình học, `x` thường tương ứng kinh độ và `y` tương ứng vĩ độ. Nếu đảo thứ tự, một điểm ở Seoul có thể nhảy sang một vị trí hoàn toàn khác nhưng giá trị số vẫn “trông hợp lý”, khiến lỗi khó phát hiện bằng kiểm tra kiểu dữ liệu đơn thuần.

EPSG:4326 thường dùng đơn vị độ. Nếu mã chương trình mặc định mọi tọa độ đều tính bằng mét, vùng đệm `1000` có thể bị hiểu thành 1000 độ. Vì vậy CRS nên được coi như **đơn vị đo** trong hợp đồng API, không phải siêu dữ liệu (metadata) phụ.

## Khoảng cách phẳng và khoảng cách trắc địa không giống nhau

Trên phạm vi nhỏ, phép đo trên mặt phẳng thường đủ tốt. Nhưng khi khoảng cách lớn hoặc gần vùng cực, dùng khoảng cách Euclid trực tiếp trên vĩ độ–kinh độ tạo sai số rõ rệt. Khi cần khoảng cách trên bề mặt Trái Đất, ta dùng khoảng cách trắc địa (geodesic distance) hoặc mô hình ellipsoid.

Điều này ảnh hưởng trực tiếp tới các tính năng “tìm địa điểm gần tôi”, vùng phục vụ, định tuyến và định giá giao hàng. Nếu doanh nghiệp tính phí theo khoảng cách, sai mô hình hình học có thể trở thành lỗi nghiệp vụ chứ không chỉ lỗi bản đồ.

## Tính hợp lệ hình học và quan hệ tô-pô

Một đa giác có thể tự cắt, có lỗ bị đảo hướng hoặc có đường biên không khép kín. Hình học như vậy có thể hiển thị được nhưng gây lỗi khi tính diện tích, giao nhau hoặc chứa điểm. Vì thế pipeline dữ liệu không gian nên có bước kiểm tra **tính hợp lệ hình học (geometry validity)** trước khi phân tích.

Tô-pô (topology) trả lời các quan hệ kiểu “chạm”, “nằm trong”, “giao nhau” hay “kề nhau”. Hai đa giác có thể nhìn như tiếp xúc trên màn hình nhưng thực tế còn một khe nhỏ do sai số dữ liệu; ngược lại, hai đường có thể cắt nhau về hình học nhưng không được phép nối trong mạng đường vì khác cao độ. Đây là ví dụ cho thấy hình học hiển thị và logic nghiệp vụ không phải lúc nào cũng giống nhau.

## Chỉ mục không gian: giảm số phép toán đắt tiền

Phép toán hình học chính xác thường tốn chi phí hơn so sánh số đơn giản. **Chỉ mục không gian (spatial index)** dùng hộp bao hoặc phân hoạch phân cấp để loại nhanh các ứng viên chắc chắn không liên quan trước khi chạy phép tính chính xác.

Có thể hình dung truy vấn “tìm mọi bệnh viện trong bán kính 5 km” gồm hai bước. Bước đầu dùng hộp bao để lấy một tập nhỏ ứng viên. Bước sau mới tính khoảng cách thật. Đây là cùng tinh thần với nhiều thuật toán tìm kiếm: dùng một bộ lọc rẻ để tránh chạy phép toán đắt trên toàn bộ dữ liệu.

Các cấu trúc thường gặp gồm R-tree, GiST, quadtree, geohash, S2 và H3. Không có cấu trúc nào tốt nhất cho mọi bài toán; lựa chọn phụ thuộc loại hình học, kiểu truy vấn, phân bố dữ liệu và yêu cầu cập nhật.

## Dữ liệu vectơ và dữ liệu lưới là hai mô hình khác nhau

**Dữ liệu vectơ (vector)** biểu diễn đối tượng rời rạc bằng điểm, đường và đa giác. **Dữ liệu lưới (raster)** chia không gian thành các ô có giá trị. Mạng đường, thửa đất và biên giới phù hợp với vectơ; ảnh vệ tinh, nhiệt độ và độ cao thường phù hợp với dữ liệu lưới.

Khác biệt quan trọng nằm ở cách đặt câu hỏi. Với vectơ, ta thường hỏi về đối tượng và quan hệ. Với raster, ta thường hỏi giá trị của trường tại một ô hoặc mẫu phân bố trên bề mặt. Chuyển raster thành vector hay ngược lại luôn thêm giả định về độ phân giải và ranh giới, nên không phải phép biến đổi “miễn phí”.

## Độ phân giải là một phần của ý nghĩa dữ liệu

Raster 10 m, 100 m và 1 km có thể mô tả cùng một biến nhưng không trả lời cùng một câu hỏi. Một khu dân cư nhỏ có thể biến mất ở độ phân giải thô; ngược lại dữ liệu cực chi tiết có thể làm tăng nhiễu và chi phí xử lý.

Đây là phiên bản số của vấn đề quy mô trong địa lý: dữ liệu không chỉ có giá trị, mà còn có **kích thước ô, phạm vi thời gian và đơn vị tổng hợp**. Nếu mô hình học máy được huấn luyện trên dữ liệu 10 m nhưng triển khai trên dữ liệu 100 m, phân bố đặc trưng có thể thay đổi mạnh.

## Kiến trúc ô bản đồ và mức chi tiết

Bản đồ web thường chia thế giới thành các **ô bản đồ (tile)** theo nhiều mức phóng đại. Ở mỗi mức, hệ thống chỉ gửi lượng chi tiết vừa đủ cho màn hình. Cách này giảm băng thông và cho phép bộ nhớ đệm theo `zoom/x/y`.

**Ô lưới (raster tile)** đã được dựng thành ảnh, phù hợp khi giao diện không cần thay đổi cách biểu diễn dữ liệu. **Ô vectơ (vector tile)** giữ hình học và thuộc tính đã được đơn giản hóa, cho phép trình duyệt thay đổi kiểu hiển thị. Đổi lại phía client phải làm nhiều việc hơn.

Mức chi tiết (LOD — Level of Detail) không chỉ là tối ưu hiệu năng. Nó là quyết định về thông tin nào được giữ ở mỗi quy mô. Một đường nhỏ có thể xuất hiện ở zoom cao nhưng biến mất ở zoom thấp; điều này phản ánh quá trình khái quát hóa bản đồ.

## Spatial join: phép nối dữ liệu bằng quan hệ không gian

Trong cơ sở dữ liệu thông thường, ta nối bảng bằng khóa. Trong GIS, nhiều phép nối diễn ra bằng vị trí. Ví dụ: gán mỗi điểm cửa hàng vào quận chứa nó, gán mỗi tai nạn vào đoạn đường gần nhất hoặc tính dân số nằm trong vùng ngập.

Đây gọi là **phép nối không gian (spatial join)**. Sai CRS, hình học lỗi hoặc quy tắc “gần nhất” không phù hợp có thể tạo kết quả sai dù câu SQL chạy thành công. Vì vậy spatial join luôn cần kiểm tra cả logic địa lý, không chỉ cú pháp.

## Định tuyến: đồ thị + địa lý + quy tắc nghiệp vụ

Mạng đường có thể được mô hình hóa bằng đồ thị: giao lộ là nút, đoạn đường là cạnh; trọng số có thể là khoảng cách, thời gian, phí hoặc chi phí tổng quát. Dijkstra hoặc A* tìm đường tối ưu theo trọng số.

Dẫn đường thực tế phức tạp hơn vì có đường một chiều, cấm rẽ, làn riêng, cầu vượt, giờ cấm, giao thông biến đổi và loại phương tiện. Một đoạn đường tồn tại về hình học không có nghĩa mọi phương tiện đều được dùng nó.

Vì vậy routing engine thực tế là sự kết hợp giữa **hình học mạng + luật giao thông + chi phí động theo thời gian**.

## Map matching: từ GPS nhiễu về mạng đường

Quỹ đạo GPS không nằm chính xác trên tim đường do sai số đo và đa đường tín hiệu. **Ghép quỹ đạo với bản đồ (map matching)** tìm đoạn đường có xác suất cao nhất mà thiết bị thực sự đi qua.

Chỉ lấy “đường gần nhất” có thể sai tại nút giao nhiều tầng hoặc hai đường chạy song song. Thuật toán tốt thường xét cả khoảng cách, hướng, tốc độ và tính liên tục của tuyến. Đây là ví dụ điển hình cho việc quan sát vị trí luôn chứa bất định.

## Hàng rào địa lý và hiện tượng rung ranh giới

**Hàng rào địa lý (geofencing)** cho phép phát hiện thiết bị vào hoặc rời một vùng. Nhưng GPS dao động quanh ranh giới có thể làm hệ thống phát hàng loạt sự kiện vào–ra giả.

Một chiến lược là dùng **độ trễ chuyển trạng thái (hysteresis)**: ngưỡng vào và ngưỡng ra khác nhau. Cách khác là yêu cầu thiết bị ở trong vùng đủ lâu trước khi kích hoạt. Đây là bài toán giống chống rung công tắc trong điện tử: dữ liệu đo không bao giờ hoàn hảo.

## Không gian luôn đi cùng thời gian

Nhiều hệ thống GIS thực chất là **không gian–thời gian (spatiotemporal)**. Vị trí xe thay đổi theo giây; vùng ngập thay đổi theo giờ; lớp phủ đất thay đổi theo năm. Nếu chỉ lưu “tọa độ hiện tại”, ta mất khả năng phân tích lịch sử và xu hướng.

Thiết kế dữ liệu tốt cần xác định đây là vị trí tức thời, quỹ đạo, snapshot định kỳ hay trạng thái có hiệu lực trong một khoảng thời gian. Trong cơ sở dữ liệu, điều này thường dẫn tới partition theo thời gian kết hợp chỉ mục không gian.

## Viễn thám và học máy: nguy cơ rò rỉ không gian

Ảnh vệ tinh có thể được biểu diễn dưới dạng tensor của dữ liệu lưới. CNN hoặc Transformer có thể phân loại lớp phủ đất, phát hiện đối tượng hoặc phân đoạn vùng ngập.

Tuy nhiên các pixel gần nhau thường rất tương quan. Nếu chia ngẫu nhiên train/test, các điểm kiểm tra có thể nằm ngay cạnh dữ liệu huấn luyện, khiến điểm số quá đẹp. **Rò rỉ không gian (spatial leakage)** làm mô hình có vẻ tổng quát nhưng thất bại khi chuyển sang vùng mới.

Vì vậy kiểm định chéo theo block không gian, theo lưu vực hoặc theo thành phố thường phù hợp hơn khi mục tiêu là dự báo ngoài vùng đã học.

## Đặc trưng không gian và nguy cơ học nhầm vị trí

Một mô hình có thể học “địa chỉ” thay vì học cơ chế. Ví dụ nếu tất cả điểm ngập trong tập huấn luyện nằm ở một quận nhất định, mô hình có thể dùng tọa độ như shortcut thay vì học địa hình và thoát nước.

Đây là lý do đặc trưng không gian phải được dùng có chủ đích. Khoảng cách tới sông, độ cao, độ dốc hoặc mật độ xây dựng thường mang ý nghĩa cơ chế tốt hơn kinh độ–vĩ độ thô.

## Quyền riêng tư vị trí

Vị trí chính xác là dữ liệu nhạy cảm. Một chuỗi vị trí vô danh vẫn có thể suy ra nơi ở và nơi làm việc, từ đó tái nhận diện cá nhân. Vì vậy thiết kế hệ thống nên tuân nguyên tắc **thu thập tối thiểu (data minimization)**: chỉ lấy độ chính xác và tần suất thực sự cần cho chức năng.

Có thể giảm rủi ro bằng tổng hợp theo vùng, làm thô độ chính xác, giới hạn thời gian lưu và kiểm soát quyền truy cập. Nhưng làm thô dữ liệu cũng làm giảm khả năng phân tích, nên đây là một đánh đổi chứ không phải thao tác miễn phí.

## ETL không gian cần kiểm tra nhiều hơn ETL thông thường

Một pipeline không gian thường gồm: thu nhận → chuẩn hóa CRS → kiểm tra hình học → làm sạch thuộc tính → nối không gian → tổng hợp → tạo tile hoặc API.

Các kiểm tra nên bao gồm: tọa độ có nằm trong phạm vi hợp lý không, hình học có hợp lệ không, đơn vị có nhất quán không, dữ liệu có bị đảo kinh–vĩ độ không và trường thời gian có dùng cùng múi giờ không. Đây là tương đương của validation schema trong kỹ thuật dữ liệu, nhưng có thêm lớp địa lý.

## Quan sát hệ thống và kiểm thử GIS

Nhiều lỗi không gian chỉ xuất hiện ở vùng biên hoặc dữ liệu bất thường. Vì vậy unit test nên có các trường hợp gần kinh tuyến 180°, gần cực, đa giác có lỗ, điểm nằm đúng biên và tuyến qua nhiều CRS.

Trong production, nên theo dõi tỷ lệ geometry invalid, latency của spatial query, số lượng tile cache miss và phân bố sai số vị trí. Một hệ thống bản đồ “trông đúng” không đảm bảo backend đang tính đúng.

## Bản sao số

**Bản sao số (digital twin)** của đô thị hoặc công nghiệp có thể kết hợp GIS, BIM, cảm biến và mô phỏng. GIS cung cấp bối cảnh địa lý; BIM cung cấp chi tiết tài sản xây dựng; cảm biến cung cấp trạng thái theo thời gian.

Thách thức lớn không phải chỉ dựng mô hình 3D mà là đồng bộ danh tính đối tượng, phiên bản dữ liệu và trạng thái. Nếu cùng một tòa nhà có ba ID khác nhau trong GIS, BIM và hệ cảm biến, “digital twin” dễ trở thành ba hệ tách rời có giao diện đẹp.

## Những hiểu lầm phổ biến

**“Có latitude/longitude là đã có GIS.”** Không đúng. GIS còn cần CRS, quan hệ không gian, độ chính xác, topology và scale.

**“Khoảng cách gần nhất luôn là đường thẳng.”** Không đúng với mạng đường, địa hình hoặc biên giới.

**“Độ phân giải càng cao càng tốt.”** Không luôn đúng; độ phân giải cao tăng chi phí và có thể thêm nhiễu không liên quan.

**“Model accuracy cao nghĩa là mô hình không gian tốt.”** Không đúng nếu train/test bị rò rỉ không gian.

## Mô hình tư duy

> Phần mềm không gian là **kỹ thuật dữ liệu trong đó khoảng cách, topology, phép chiếu, quy mô và thời gian đều là logic nghiệp vụ**. Đừng coi chúng là lớp hiển thị đặt sau cùng; chúng phải xuất hiện từ schema, API, test đến monitoring.

Xem thêm: [Nền tảng GIS](../00_foundations/04_geospatial_data_gis_remote_sensing.md), [Toán học và Thống kê](./00_geography_math_statistics.md), [Giao thông và toàn cầu hóa](../02_human_geography/08_transport_trade_globalization.md).
