# Bản đồ, tỷ lệ, phép chiếu và suy luận không gian

## Bản đồ không phải bản sao thu nhỏ của thế giới

**Bản đồ học (cartography / 지도학)** là quá trình thiết kế một mô hình không gian. Bất kỳ bản đồ nào cũng phải chọn phạm vi, tỷ lệ, phép chiếu, ký hiệu, cách phân lớp dữ liệu và thứ tự ưu tiên thị giác. Vì vậy bản đồ không thể chứa toàn bộ thế giới; nó luôn là một phép **khái quát hóa (generalization)** phục vụ câu hỏi cụ thể.

Điểm này rất quan trọng cho năng lực đọc bản đồ. Một bản đồ có thể chính xác về kỹ thuật nhưng vẫn gây hiểu sai nếu người đọc không biết dữ liệu gì bị bỏ qua, biến nào được chuẩn hóa, ranh giới nào được sử dụng hoặc phép chiếu đang bảo toàn tính chất nào.

## Ba nghĩa khác nhau của “scale”

Trong Địa lý, **quy mô (scale)** có ít nhất ba lớp dễ bị trộn lẫn.

**Tỷ lệ bản đồ (map scale)** như 1:50.000 mô tả quan hệ giữa khoảng cách trên bản đồ và ngoài thực địa. **Quy mô không gian của hiện tượng (spatial scale)** nói về phạm vi mà quá trình hoạt động, ví dụ từ phố, đô thị, lưu vực đến toàn cầu. **Quy mô phân tích (scale of analysis)** là cấp mà ta gom dữ liệu, ví dụ hộ gia đình, quận, tỉnh hay quốc gia.

Một kết luận có thể thay đổi khi đổi quy mô phân tích. Trung bình của tỉnh có thể che cụm nghèo trong vài quận; xu hướng toàn cầu có thể khác xu hướng địa phương. Do đó scale không chỉ là chuyện phóng to–thu nhỏ hình ảnh mà là một phần của logic suy luận.

## Extent, resolution và grain

Ngoài scale, cần phân biệt **phạm vi (extent)** và **độ phân giải (resolution/grain)**. Một raster 30 m phủ cả quốc gia có extent rất lớn nhưng grain tương đối mịn; một raster 1 km phủ một thành phố có extent nhỏ hơn nhưng grain thô hơn.

Khi độ phân giải quá thô, các đối tượng nhỏ bị trộn trong cùng pixel hoặc vùng thống kê. Khi quá mịn so với chất lượng dữ liệu, bản đồ có thể tạo ảo giác chính xác. Độ chi tiết hiển thị nên phù hợp với độ chính xác của phép đo và câu hỏi nghiên cứu.

## Vì sao phép chiếu là bắt buộc?

Không thể trải bề mặt cong của Trái Đất lên mặt phẳng mà giữ hoàn hảo mọi tính chất. **Phép chiếu bản đồ (map projection / 지도 투영법)** là hàm biến đổi từ tọa độ trên ellipsoid/mặt cầu sang mặt phẳng.

Mọi phép chiếu đều đánh đổi giữa diện tích, hình dạng, khoảng cách và phương hướng. Điều quan trọng không phải tìm “projection đúng nhất” mà chọn projection phù hợp với mục tiêu.

**Phép chiếu bảo giác (conformal)** giữ góc và hình dạng cục bộ tốt. **Bảo toàn diện tích (equal-area)** giữ diện tích, hữu ích cho bản đồ so sánh quy mô vùng. **Bảo khoảng cách (equidistant)** chỉ giữ đúng một số quan hệ khoảng cách nhất định. **Phương vị (azimuthal)** có thể giữ hướng chính xác từ một tâm.

Không có phép chiếu nào giữ đồng thời mọi thuộc tính trên toàn cầu.

## Mercator: đúng cho một mục tiêu, sai khi dùng nhầm mục tiêu

Mercator là phép chiếu bảo giác. Nó bảo toàn góc cục bộ và từng rất hữu ích cho hàng hải vì đường rhumb line có hướng la bàn cố định được biểu diễn thành đường thẳng. Tuy nhiên diện tích bị phóng đại mạnh ở vĩ độ cao.

Vì vậy Greenland trông lớn bất thường trên bản đồ Mercator toàn cầu. Kết luận đúng không phải “Mercator là bản đồ sai”, mà là **Mercator không phù hợp để so sánh diện tích toàn cầu**.

Web Mercator phổ biến trong bản đồ web chủ yếu vì tính tiện lợi cho tile pyramid và tương thích kỹ thuật. Nó là lựa chọn hiển thị, không phải CRS phân tích tối ưu cho mọi phép đo.

## Distortion có thể đọc bằng Tissot indicatrix

Một cách trực quan để hiểu biến dạng phép chiếu là **Tissot indicatrix**. Ta tưởng tượng các vòng tròn nhỏ giống nhau trên địa cầu; sau phép chiếu chúng có thể trở thành ellipse khác kích thước và hướng. Hình dạng ellipse cho biết biến dạng góc, diện tích và phương hướng cục bộ.

Mental model này hữu ích hơn việc học thuộc danh sách tên projection vì nó giúp hỏi: “bản đồ này đang bóp méo thứ gì và ở đâu?”.

## UTM và bài toán địa phương

**Universal Transverse Mercator (UTM)** chia thế giới thành các múi để giới hạn biến dạng trong từng vùng. Đây là ví dụ của nguyên lý: nếu không thể tối ưu toàn cầu, hãy tối ưu trên extent nhỏ hơn.

Trong khảo sát, kỹ thuật hoặc tính diện tích, chọn CRS địa phương phù hợp thường quan trọng hơn dùng một projection toàn cầu tiện lợi. Tuy nhiên khi dữ liệu trải qua nhiều múi UTM, cần thiết kế hệ phân tích khác thay vì nối các tọa độ phẳng một cách tùy tiện.

## Khái quát hóa khi thay đổi mức zoom

Khi thu nhỏ bản đồ, không thể giữ mọi con đường, sông nhỏ và tòa nhà. Cartography cần **generalization**: chọn lọc, đơn giản hóa, gộp, dịch chuyển ký hiệu hoặc thay đổi cách biểu diễn.

Một thành phố có thể là polygon ở zoom lớn, point ở zoom nhỏ. Một con sông nhiều khúc uốn được đơn giản hóa. Đây không phải “làm sai dữ liệu”; nó là chuyển đổi biểu diễn để giữ cấu trúc quan trọng ở mỗi tỷ lệ.

Nhưng generalization cần nhất quán. Nếu đơn giản hóa quá mạnh, topology có thể bị phá hoặc biên giới có thể trông thay đổi.

## Bản đồ chuyên đề và vấn đề mẫu số

**Bản đồ tô vùng (choropleth map)** phù hợp với biến đã chuẩn hóa theo diện tích, dân số hoặc mẫu số liên quan, chẳng hạn tỷ lệ thất nghiệp hoặc mật độ dân số. Dùng số lượng tuyệt đối dễ khiến vùng lớn hoặc đông dân chi phối thị giác.

Ví dụ bản đồ số ca bệnh tuyệt đối thường phản ánh một phần bản đồ dân số. Nếu câu hỏi là “rủi ro đối với mỗi người”, cần tỷ lệ phù hợp hơn. Tuy nhiên tỷ lệ ở vùng dân số rất nhỏ có thể dao động mạnh, nên cần nhìn cả mẫu số và uncertainty.

## Phân lớp dữ liệu thay đổi câu chuyện

Khi biến liên tục được chia thành màu, lựa chọn **equal interval**, **quantile**, **natural breaks** hoặc threshold chuyên môn có thể làm mẫu hình nổi bật khác nhau.

Quantile phân số vùng gần bằng nhau cho mỗi lớp nhưng có thể tách hai giá trị rất gần nhau. Equal interval trực quan về thang số nhưng có thể dồn phần lớn vùng vào một lớp nếu phân bố lệch. Natural breaks tối ưu theo cụm dữ liệu nhưng khó so sánh giữa nhiều bản đồ nếu breakpoint thay đổi.

Vì vậy legend là một phần của mô hình, không chỉ trang trí.

## MAUP: ranh giới thống kê có thể thay đổi kết luận

**Vấn đề đơn vị không gian có thể thay đổi (Modifiable Areal Unit Problem, MAUP)** xuất hiện khi kết quả thống kê thay đổi do cách ta chia vùng hoặc mức aggregation.

Cùng dữ liệu hộ gia đình, tương quan có thể khác khi gộp theo phường, quận hoặc tỉnh. Đây không phải lỗi tính toán; nó phản ánh việc aggregation làm mất thông tin và tạo cấu trúc mới.

Liên quan là **ngụy biện sinh thái (ecological fallacy)**: suy đặc điểm cá nhân từ trung bình vùng. “Quận thu nhập cao” không có nghĩa mọi cư dân đều giàu.

## Bản đồ point, proportional symbol, dasymetric và density

Không phải mọi biến nên tô polygon. Điểm phù hợp với sự kiện hoặc cơ sở; **proportional symbol** phù hợp với tổng lượng tại địa điểm; **dot density** giúp trực quan phân bố tương đối; **dasymetric mapping** dùng thông tin bổ sung để phân bố giá trị trong vùng hợp lý hơn.

Chọn kiểu bản đồ là chọn mô hình dữ liệu. Nếu hiện tượng liên tục như nhiệt độ, ép nó vào biên giới hành chính có thể làm mất cấu trúc. Nếu hiện tượng thuộc từng đơn vị pháp lý như mức thuế địa phương, polygon lại có ý nghĩa trực tiếp.

## Uncertainty cũng cần được cartography hóa

Bản đồ thường hiển thị estimate nhưng giấu uncertainty. Điều đó dễ tạo cảm giác ranh giới và giá trị chính xác tuyệt đối.

Có thể thể hiện uncertainty bằng transparency, hatching, confidence interval, ensemble spread hoặc tách một bản đồ phụ. Trong disaster map, vùng dự báo xác suất khác bản đồ quan sát đã xác nhận; người đọc cần biết hai lớp này không cùng mức chắc chắn.

## Bản đồ và quyền lực lựa chọn

Tên địa danh, đường biên, projection, center point và biến được chọn đều có thể mang ý nghĩa xã hội–chính trị. Điều này không có nghĩa mọi bản đồ đều là tuyên truyền. Nó có nghĩa người đọc cần biết **provenance**: ai tạo, từ dữ liệu nào, thời điểm nào, với quy ước gì.

Trong các vùng có tranh chấp, một đường ranh giới có thể đại diện cho claim, line of control, administrative boundary hoặc dataset convention. Cartography tốt phải phân biệt các lớp đó thay vì trộn chúng.

## Web maps, tiles và vector tiles

Bản đồ web thường dùng **tile pyramid**: thế giới được chia thành các ô theo nhiều mức zoom. Raster tile là ảnh; **vector tile** chứa geometry và attribute đã được cắt/đơn giản hóa để client render.

Hệ tile làm bản đồ tải nhanh nhưng cũng tạo giới hạn. Dữ liệu phải được generalize theo zoom; label cần collision handling; cache có thể khiến dữ liệu cũ tồn tại; feature tại biên tile cần xử lý để không bị đứt.

## Cartography như một pipeline

Một bản đồ có thể được hiểu như chuỗi:

**measurement → cleaning → CRS transformation → aggregation/model → classification → symbolization → rendering → interpretation**.

Lỗi ở đầu pipeline không được sửa bằng thiết kế đẹp ở cuối. Ngược lại, dữ liệu chính xác vẫn có thể truyền tải sai nếu classification hoặc visual hierarchy không phù hợp.

## Mô hình tư duy

Bản đồ là một **mô hình nén không gian**. Mỗi bản đồ nên được đọc bằng năm câu hỏi: nó phục vụ câu hỏi gì, dùng dữ liệu nào, ở scale/extent nào, phép chiếu và aggregation nào, và uncertainty/provenance được thể hiện ra sao?

Xem tiếp: [GIS và viễn thám](./04_geospatial_data_gis_remote_sensing.md), [Tọa độ và thời gian](./02_coordinates_time_maps.md), [Địa lý + Toán và Thống kê](../90_connections/00_geography_math_statistics.md).