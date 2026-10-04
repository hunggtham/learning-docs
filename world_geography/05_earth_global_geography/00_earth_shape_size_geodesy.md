# Hình dạng Trái Đất, trắc địa và đo lường hành tinh

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Hình dạng Trái Đất, trắc địa và đo lường hành tinh**. Route đi từ hình cầu, ellipsoid và geoid → datum/hệ tọa độ → kinh-vĩ độ, khoảng cách và phép chiếu → sai số đo đạc, để mô hình hình học nối trực tiếp với cách lập bản đồ.

## Vì sao “Trái Đất là hình cầu” vừa đúng vừa chưa đủ

Ở quy mô giáo dục cơ bản, mô hình hình cầu giúp giải thích vĩ độ, kinh độ, ngày–đêm và vòng tròn lớn. Nhưng khi đo đạc chính xác, Trái Đất gần một **khối cầu dẹt (oblate spheroid)**: bán kính xích đạo lớn hơn bán kính cực do chuyển động quay và cân bằng vật chất dài hạn.

Ngay cả mô hình spheroid cũng chưa phải bề mặt vật lý thật. Núi, rãnh biển, bồn trầm tích, băng, nước và cấu trúc sâu làm phân bố khối lượng không đồng đều. Vì vậy trắc địa phải làm việc đồng thời với hình học và trường hấp dẫn.

> **Nối mạch:** Cầu là trực giác đầu tiên nhưng Trái Đất thực tế có các bề mặt hình học, trọng lực và địa hình khác nhau. **Ba bề mặt cần phân biệt** đặt nền để hiểu vì sao cùng một điểm có thể có nhiều loại độ cao.

## Ba bề mặt cần phân biệt

**Địa hình thật (topographic surface)** là bề mặt mà con người sống trên đó, gồm núi, thung lũng, đồng bằng và đáy biển.

**Ellipsoid tham chiếu (reference ellipsoid)** là bề mặt toán học trơn dùng để biểu diễn tọa độ và giải các phép tính hình học.

**Geoid** là bề mặt đẳng thế của trường trọng lực gần với mực nước biển trung bình nếu đại dương có thể kéo dài xuyên lục địa trong trạng thái tĩnh.

Ba bề mặt này trả lời ba câu hỏi khác nhau. Địa hình cho biết bề mặt thật; ellipsoid cho một chuẩn tính toán; geoid cho khái niệm “ngang” và độ cao vật lý liên quan trọng lực.

> **Nối mạch:** Độ cao GNSS thường gắn với ellipsoid, còn bản đồ địa hình cần mốc cao và geoid; khác biệt là do hệ quy chiếu chứ không nhất thiết là lỗi đo. **Trắc địa là khoa học về hình dạng, trọng lực và chuyển động** giải thích cơ chế tạo các tham chiếu đó.

## Độ cao: vì sao GNSS và bản đồ địa hình có thể khác nhau

GNSS thường cho **độ cao ellipsoid (ellipsoidal height, h)**. Kỹ thuật và bản đồ địa hình thường quan tâm **độ cao trực chuẩn (orthometric height, H)** so với geoid.

Quan hệ gần đúng:

\[
h = H + N
\]

trong đó \(N\) là undulation của geoid so với ellipsoid.

Nếu chuỗi xử lý (pipeline / 파이프라인) drone ánh xạ (mapping / 매핑) hoặc xây dựng lấy `h` làm “cao hơn mực nước biển” mà không áp mô hình geoid phù hợp, sai số phương đứng có thể lên tới hàng chục mét ở một số nơi.

> **Nối mạch:** Trắc địa nối hình dạng, trọng lực, chuyển động và phép đo thành một hệ thống; để đọc các sai số và cung độ, cần có trực giác về kích thước hành tinh. **Kích thước hành tinh và trực giác quy mô** đưa các đại lượng ấy về thang đo dễ kiểm tra.

## Trắc địa là khoa học về hình dạng, trọng lực và chuyển động

**Trắc địa (geodesy / 측지학)** không chỉ là đo đất. Nó nghiên cứu hình dạng, kích thước, trường trọng lực, định hướng và sự biến đổi theo thời gian của Trái Đất, đồng thời xây các hệ tham chiếu để mọi phép đo vị trí có thể nối với nhau.

Các công cụ hiện đại gồm GNSS, đo cao vệ tinh (satellite altimetry), giao thoa radar (InSAR), vệ tinh trọng lực, laser ranging, VLBI và mạng mốc mặt đất.

Điểm chung của chúng là không “nhìn trực tiếp tọa độ”. Chúng đo thời gian truyền tín hiệu, khoảng cách, pha, góc hoặc trường vật lý rồi suy vị trí từ mô hình.

> **Nối mạch:** Kích thước và độ cong của Trái Đất quyết định đường thẳng trên bản đồ không luôn là đường ngắn trên bề mặt. **Great circle, geodesic và đường ngắn nhất** tiếp theo biến trực giác quy mô thành phép chọn tuyến.

## Kích thước hành tinh và trực giác quy mô

Chu vi Trái Đất xấp xỉ bốn mươi nghìn kilomet. Bán kính trung bình khoảng 6.371 km. Những con số này hữu ích để xây trực giác, không phải để học thuộc riêng lẻ.

Một độ vĩ độ tương ứng xấp xỉ hơn 100 km. Vệ tinh quỹ đạo thấp ở độ cao vài trăm kilomet thực ra vẫn rất gần bề mặt so với bán kính hành tinh. Một tuyến bay 10.000 km là rất dài đối với con người nhưng vẫn chỉ là một phần chu vi Trái Đất.

Trực giác quy mô giúp tránh lỗi khi xử lý bản đồ toàn cầu. Một projection tốt cho thành phố chưa chắc phù hợp cho lục địa; công thức phẳng tốt cho vài kilomet chưa chắc phù hợp cho tuyến xuyên Thái Bình Dương.

> **Nối mạch:** Great circle và geodesic cho biết đường tối ưu theo hình học, nhưng muốn tọa độ dùng được phải biết bề mặt và mốc nào đang làm datum. **Datum: ellipsoid chưa đủ** bổ sung lớp trọng lực và quy ước tham chiếu.

## Great circle, geodesic và đường ngắn nhất

Trên mặt cầu, đường ngắn nhất giữa hai điểm là cung **vòng tròn lớn (great circle)**. Trên ellipsoid, khái niệm tổng quát hơn là **geodesic**.

Đường geodesic và đường có bearing không đổi không phải cùng một thứ. Trong Mercator, rhumb line có thể là đường thẳng, còn geodesic dài lại trông cong. Đây là ví dụ kinh điển cho việc bản đồ phẳng thay đổi trực giác hình học.

> **Nối mạch:** Ellipsoid chỉ mô tả hình học; datum còn cần nguồn gốc tọa độ, hướng trục và trọng lực. **Tham chiếu (reference / 참조) frame và epoch** tiếp theo xác định hệ đang đứng ở đâu và tại thời điểm nào.

## Datum: ellipsoid chưa đủ

Một ellipsoid có kích thước đúng nhưng chưa biết “đặt ở đâu” so với Trái Đất. **Datum** giải quyết việc gắn mô hình hình học với hành tinh thật.

Các datum cũ thường được tối ưu cho một vùng và cố định với mảng kiến tạo địa phương. Các khung hiện đại mang tính địa tâm và ngày càng xử lý rõ chuyển động theo thời gian.

Vì vậy hai tọa độ cùng viết bằng độ nhưng thuộc hai datum khác nhau có thể lệch. `Assign CRS` sai không phải lỗi nhỏ; nó làm toàn bộ hình học (geometry / 기하학) được diễn giải trong một thế giới tham chiếu khác.

> **Nối mạch:** Reference frame và epoch làm rõ tọa độ được định nghĩa theo thời gian và chuyển động nào; cùng một điểm có thể đổi tọa độ khi frame thay đổi. **Geocenter và Earth orientation** đi sâu vào tâm khối lượng và hướng quay của Trái Đất.

## Tham chiếu (reference / 참조) frame và epoch

Trái Đất không phải khối cứng. Các mảng kiến tạo dịch chuyển, băng tan làm vỏ nâng, nước ngầm thay đổi tải trọng, động đất dịch chuyển mặt đất và thủy triều rắn làm vỏ co giãn nhỏ.

Do đó trắc địa độ chính xác cao dùng **khung quy chiếu (reference frame)** kèm thời điểm. Một tọa độ centimet-level phải được hiểu cùng **epoch**. Cùng điểm vật lý có thể có tọa độ khác vài centimet sau một năm trong một frame toàn cầu.

Mô hình tư duy (mental model / 사고 모델) phù hợp là: tọa độ chính xác cao không chỉ là `x,y,z`; nó là `x,y,z + frame + epoch`.

> **Nối mạch:** Geocenter và Earth orientation mô tả chuyển động toàn Trái Đất mà hệ tọa độ phải theo dõi. **Đẳng tĩnh và biến dạng dài hạn** chuyển sang cách vỏ Trái Đất phản ứng với tải băng, nước và kiến tạo qua thời gian.

## Geocenter và Earth orientation

Khung tọa độ địa tâm cần biết tâm khối lượng và cách trục tọa độ định hướng so với Trái Đất quay. Nhưng tốc độ quay và hướng trục quay có dao động nhỏ.

**Earth Orientation Parameters (EOP)** mô tả các hiệu ứng như polar motion và sai khác giữa thời gian dựa trên quay Trái Đất với thang thời gian nguyên tử. Những hiệu ứng này nhỏ đối với bản đồ phổ thông nhưng quan trọng trong định vị vệ tinh, thiên văn và geodesy chính xác.

> **Nối mạch:** Đẳng tĩnh và biến dạng cho thấy mặt đất có lịch sử tải và chuyển động, không phải nền cố định. **Trắc địa và biến đổi khí hậu** dùng phép đo đó để theo dõi băng tan, mực biển và sụt/nâng đất.

## Đẳng tĩnh và biến dạng dài hạn

Thạch quyển phản ứng với tải trọng. Khi một tấm băng lớn tan, lớp vỏ từng bị nén có thể nâng lên hàng nghìn năm sau đó. Đây là **điều chỉnh đẳng tĩnh hậu băng hà (glacial isostatic adjustment)**.

Tương tự, trầm tích, hồ chứa lớn, khai thác nước ngầm hoặc biến đổi khối lượng có thể tạo biến dạng nhỏ. Vì thế “mặt đất” không phải khung bất biến tuyệt đối.

> **Nối mạch:** Biến đổi khí hậu cần chuỗi đo nhất quán để tách tín hiệu dài hạn khỏi nhiễu và chuyển động nền. **Ứng dụng cho Korea, Vietnam và kỹ thuật** đưa các khái niệm đó vào địa hình, hạ tầng và đo đạc thực tế.

## Trắc địa và biến đổi khí hậu

Geodesy cung cấp bằng chứng trực tiếp về nhiều thay đổi hành tinh. Satellite altimetry theo dõi mực nước biển; GNSS theo dõi chuyển động vỏ; gravimetry có thể suy mất băng và thay đổi nước lục địa; InSAR theo dõi sụt lún.

Điểm quan trọng là mỗi cảm biến đo một đại lượng khác. Không nên lấy một lớp dữ liệu để thay thế mọi lớp khác; sức mạnh nằm ở việc kết hợp các phép đo độc lập.

> **Nối mạch:** Ứng dụng Korea–Vietnam cho thấy datum, GNSS, geoid, biến dạng và mực biển ảnh hưởng trực tiếp đến bản đồ, xây dựng và quản lý rủi ro. **Mô hình tư duy** cô đọng cách nối phép đo hành tinh với quyết định kỹ thuật.

## Ứng dụng cho Korea, Vietnam và kỹ thuật

Ở bán đảo Triều Tiên và Việt Nam, GNSS hỗ trợ xây dựng, hạ tầng, bản đồ, logistics, nông nghiệp chính xác và quan trắc biến dạng. Tại các đồng bằng thấp, đặc biệt khu vực có khai thác nước ngầm hoặc trầm tích mềm, cần phân biệt mực nước biển dâng toàn cầu với **chuyển động mặt đất địa phương**.

Một thành phố có thể trải nghiệm relative sea-level rise nhanh hơn trung bình toàn cầu nếu mặt đất đồng thời sụt. Đây là điểm nối trực tiếp giữa geodesy, hydrology, urbanization và climate rủi ro (risk / 위험).

> **Nối mạch:** **Mô hình tư duy** khép chuỗi hình cầu–bề mặt → độ cao và trắc địa → quy mô, geodesic và datum → frame, epoch, geocenter, biến dạng → khí hậu và ứng dụng kỹ thuật. Kết luận bàn giao owner **World Geography** theo [README](../README.md), để nối sang thời gian, địa hình và hệ quy chiếu toàn cầu.

## Mô hình tư duy

Trắc địa là hệ thống nối **hành tinh vật lý → trường trọng lực → mô hình tham chiếu → phép đo → tọa độ**. Không có tọa độ chính xác “không cần bối cảnh”; mọi vị trí đều được đo so với một frame có quy ước và thời điểm.

Xem tiếp: [Hệ quy chiếu toàn cầu](./06_global_reference_systems.md), [Trọng lực, geoid và từ trường](./05_gravity_geoid_magnetic_field.md), [Tọa độ và thời gian](../00_foundations/02_coordinates_time_maps.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
