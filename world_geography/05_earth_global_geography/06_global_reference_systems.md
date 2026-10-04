# Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**. Route đi từ tọa độ và quy ước đo → datum/epoch và hệ quy chiếu → geographic/projected CRS → phép chiếu, sai số và metadata → interoperability, để con số vị trí luôn đi kèm điều kiện đo.

## Tọa độ là kết quả của một quy ước đo lường

Một chuỗi như `37.5665, 126.9780` chưa phải vị trí hoàn chỉnh. Ta còn cần biết đó là latitude–longitude hay longitude–latitude, đơn vị gì, datum nào, epoch nào và dữ liệu được kỳ vọng chính xác đến mức nào.

Trong GIS, **hệ quy chiếu tọa độ (Coordinate Reference system, CRS)** đóng vai trò giống hệ kiểu (type system / 타입 시스템). Nó quy định cách con số liên hệ với không gian thật. Hai array giống nhau về cấu trúc nhưng khác CRS có thể đại diện cho hai nơi khác nhau.

> **Nối mạch:** Tọa độ không tự nhiên xuất hiện; nó phụ thuộc ellipsoid, mốc, trục, đơn vị và quy ước đo. **Geographic CRS và projected CRS** phân biệt cách biểu diễn bề mặt cong và mặt phẳng trước khi chọn datum.

## Geographic CRS và projected CRS

**Geographic CRS** dùng tọa độ góc trên ellipsoid, thường là latitude và longitude. **Projected CRS** dùng phép chiếu để biến bề mặt cong thành tọa độ phẳng, thường theo mét.

Geographic CRS thuận tiện cho lưu trữ toàn cầu và trao đổi. Projected CRS thuận tiện cho nhiều phép đo cục bộ như diện tích, buffering và thiết kế kỹ thuật.

Không có CRS duy nhất tối ưu cho mọi việc. Một hệ thống tốt tách CRS lưu trữ, CRS phân tích và CRS hiển thị khi cần.

> **Nối mạch:** Geographic/projected CRS quy định cách tọa độ được tính và hiển thị, còn datum/frame quy định nó gắn với Trái Đất nào và thời điểm nào. **Geocentric và Earth-fixed** làm rõ hai cách định nghĩa gốc tọa độ và chuyển động.

## Datum và tham chiếu (reference / 참조) frame

**Datum** gắn ellipsoid với Trái Đất. **tham chiếu (reference / 참조) frame** là hiện thực hóa thực tế của hệ tham chiếu bằng mạng trạm, tọa độ và mô hình chuyển động.

Trong hệ tĩnh đơn giản, người dùng thường không phân biệt hai khái niệm. Nhưng ở trắc địa chính xác, frame và epoch là bắt buộc vì vỏ Trái Đất chuyển động.

WGS 84 không nên được hiểu như một nhãn bất biến duy nhất cho mọi thời kỳ. Các realization của hệ toàn cầu được cập nhật để bám theo phép đo tốt hơn.

> **Nối mạch:** Geocentric đặt gốc tại tâm khối lượng, Earth-fixed quay cùng Trái Đất; khác biệt này quan trọng cho vệ tinh và đo đạc. **EPSG mã (code / 코드) giúp định danh nhưng không sửa được siêu dữ liệu (metadata / 메타데이터) sai** nhắc rằng mã chỉ là nhãn cho một cấu hình cụ thể.

## Geocentric và Earth-fixed

Một khung toàn cầu thường lấy tâm gần center of mass của Trái Đất và quay cùng hành tinh, tạo hệ **Earth-Centered, Earth-Fixed (ECEF)**. Tọa độ ECEF dùng ba trục Cartesian `X,Y,Z`.

GNSS tính vị trí thuận tiện trong khung ba chiều như vậy. Vĩ độ–kinh độ là một biểu diễn (representation / 표현) được suy ra từ tọa độ địa tâm và ellipsoid.

Mô hình tư duy (mental model / 사고 모델) này giải thích vì sao tọa độ địa lý không phải “đầu ra thô” của vệ tinh; chúng là một lớp chuyển đổi.

> **Nối mạch:** EPSG code giúp phần mềm nhận CRS, nhưng không thể sửa nhầm epoch, axis order, đơn vị hay metadata nguồn. **Coordinate transformation là phép biến đổi có điều kiện** tiếp theo đòi hỏi biết đầy đủ các điều kiện đó.

## EPSG mã (code / 코드) giúp định danh nhưng không sửa được siêu dữ liệu (metadata / 메타데이터) sai

Registry EPSG cung cấp mã cho nhiều CRS và transformation. Mã như `EPSG:4326` giúp hệ thống trao đổi định nghĩa nhất quán.

Nhưng mã không có phép thuật. Nếu tệp (file / 파일) thực sự ở một CRS mà bị gán nhãn CRS khác, phần mềm sẽ xử lý sai một cách rất nhất quán.

**Assign CRS** nghĩa “các con số hiện tại nên được diễn giải theo hệ này”. **Reproject** nghĩa “hãy biến đổi các con số để giữ cùng vị trí vật lý trong hệ khác”. Nhầm hai thao tác là lỗi kinh điển.

> **Nối mạch:** Transformation phụ thuộc CRS nguồn/đích, datum shift, grid, epoch và phép chiếu; đổi hệ không chỉ là đổi tên cột. **Vertical datum là một hệ riêng** tách độ cao hình học khỏi độ cao theo trọng trường.

## Coordinate transformation là phép biến đổi có điều kiện

Chuyển giữa hai CRS có thể cần projection formula, datum transformation, grid correction và đôi khi epoch. Không phải mọi transformation đều có độ chính xác giống nhau.

Nếu nguồn (source / 소스) datum và mục tiêu (target / 대상) datum khác, phần mềm có thể dùng transformation xấp xỉ khi thiếu grid tệp (file / 파일) chính xác. Vì vậy chuỗi xử lý (pipeline / 파이프라인) kỹ thuật nên ghi transformation phương thức (method / 메서드) và expected accuracy, đặc biệt khi dùng dữ liệu survey.

> **Nối mạch:** Vertical datum dựa vào geoid/mốc cao và không thể suy trực tiếp chỉ từ kinh–vĩ độ. **Epoch và động (dynamic / 동적) datum** bổ sung chiều thời gian khi mốc và vỏ Trái Đất chuyển động.

## Vertical datum là một hệ riêng

Tọa độ ngang đúng không bảo đảm cao độ đúng. Dữ liệu độ cao có thể dùng ellipsoid, geoid mô hình (model / 모델) hoặc vertical datum quốc gia dựa trên tide gauge/leveling mạng (network / 네트워크).

Khi ghép DEM, GNSS và survey, cần kiểm tra vertical tham chiếu (reference / 참조) riêng. Một chuỗi xử lý (pipeline / 파이프라인) chỉ kiểm tra `EPSG` của horizontal CRS nhưng bỏ vertical datum vẫn có thể gây lỗi lớn.

> **Nối mạch:** Dynamic datum ghi tọa độ cùng thời điểm và mô hình chuyển động, còn static datum giả định mốc cố định trong phạm vi sử dụng. **National grid và cục bộ (local / 로컬) kỹ thuật (engineering / 엔지니어링) CRS** cho thấy cách quốc gia và dự án tối ưu hệ quy chiếu theo nhu cầu.

## Epoch và động (dynamic / 동적) datum

Ở độ chính xác cao, tọa độ thay đổi theo chuyển động mảng. **động (dynamic / 동적) datum/tham chiếu (reference / 참조) frame** lưu tọa độ kèm epoch và mô hình (model / 모델) vận tốc.

Nếu dữ liệu năm 2010 được so với survey 2030 mà không propagate tọa độ về cùng epoch, sai khác có thể bị hiểu nhầm là biến dạng công trình dù thực chất là chuyển động frame.

Đây là điểm ngày càng quan trọng khi smartphone, autonomous các hệ thống (systems / 시스템들) và precise positioning đạt độ chính xác cao hơn.

> **Nối mạch:** National grid và engineering CRS có thể giảm biến dạng, phù hợp địa hình và công trình, nhưng chỉ dùng đúng trong phạm vi và datum đã công bố. **Toàn cục (global / 전역) grid chỉ mục (index / 인덱스) không thay thế CRS** phân biệt lưới chỉ mục với hệ tọa độ có ý nghĩa đo lường.

## National grid và cục bộ (local / 로컬) kỹ thuật (engineering / 엔지니어링) CRS

Các quốc gia thường có national grid hoặc projected CRS tối ưu cho lãnh thổ. Korea và Vietnam đều có hệ thống tọa độ bản đồ/quốc gia phục vụ cadastral, survey và hạ tầng (infrastructure / 인프라).

Dữ liệu web thường đến ở WGS84/Web Mercator, còn dữ liệu hành chính–kỹ thuật có thể ở national CRS. Vì vậy ETL geospatial thực tế phải xử lý transformation thay vì giả định mọi tệp (file / 파일) dùng cùng hệ.

> **Nối mạch:** Grid index giúp tìm ô và phân mảnh dữ liệu, nhưng không cho biết tọa độ, datum hay phép đo nếu thiếu CRS. **Address, place name và coordinate là ba hệ khác nhau** tiếp theo tách định danh xã hội khỏi vị trí hình học.

## Toàn cục (global / 전역) grid chỉ mục (index / 인덱스) không thay thế CRS

Các hệ như geohash, H3, S2 hoặc tile XYZ chia bề mặt thành cell phân cấp. Chúng hữu ích cho spatial indexing, aggregation, caching và phân tán (distributed / 분산) processing.

Nhưng chúng không loại bỏ nhu cầu hiểu datum và hình học (geometry / 기하학). Một H3 cell là cách lập chỉ mục trên bề mặt; nó không tự biến mọi khoảng cách hay diện tích thành chính xác tuyệt đối.

Khi aggregate dữ liệu theo grid, kích thước cell trở thành quy mô (scale / 규모) of phân tích (analysis / 분석) và có thể tạo MAUP dạng lưới.

> **Nối mạch:** Address, place name và coordinate có thể mô tả cùng một nơi nhưng khác ngôn ngữ, thời điểm, độ chính xác và mục đích. **Ranh giới (boundary / 경계) dataset cũng cần tham chiếu (reference / 참조) hệ thống (system / 시스템)** áp dụng nguyên tắc metadata đó cho polygon và ranh giới.

## Address, place name và coordinate là ba hệ khác nhau

Địa chỉ là hệ quy ước xã hội; địa danh là lớp ngôn ngữ–lịch sử; tọa độ là biểu diễn (representation / 표현) hình học. **Geocoding** nối các hệ này nhưng luôn chứa ambiguity.

Một tên địa danh có thể trùng ở nhiều nơi, một địa chỉ có thể đổi sau cải cách hành chính và một polygon địa giới có thể có nhiều phiên bản (version / 버전). Hệ geocoder tốt cần phiên bản (version / 버전), provenance và confidence.

> **Nối mạch:** Boundary dataset cần CRS, datum, thời điểm, nguồn pháp lý và quy tắc topology; đường biên thiếu tham chiếu không thể ghép an toàn. **Geospatial interoperability** chuyển từ metadata riêng lẻ sang khả năng các hệ thống trao đổi cùng nghĩa.

## Ranh giới (boundary / 경계) dataset cũng cần tham chiếu (reference / 참조) hệ thống (system / 시스템)

Biên giới hành chính và coastline không chỉ cần CRS mà còn cần thời điểm và nguồn. Cùng một nước có thể có polygon khác nhau giữa statistical dataset, cadastral dataset và generalized web map.

Đối với khu vực tranh chấp, hình học (geometry / 기하학) còn có ngữ nghĩa (semantic / 의미적) khác nhau: claim line, điều khiển (control / 제어) line hoặc administrative ranh giới (boundary / 경계). Không nên chỉ lưu một polygon mà không lưu loại ranh giới (boundary / 경계).

> **Nối mạch:** Interoperability cần CRS rõ, schema tương thích, axis/units nhất quán, provenance và quy tắc biến đổi có thể tái lập. **Mô hình tư duy** cô đọng cách đọc toàn bộ hạ tầng tọa độ.

## Geospatial interoperability

Khi nhiều hệ thống trao đổi dữ liệu, cần nhất quán về CRS, hình học (geometry / 기하학) kiểu (type / 타입), axis thứ tự (order / 순서), encoding, precision và thời gian (time / 시간) tham chiếu (reference / 참조). OGC standards, GeoJSON, GeoPackage, WKT và các format khác giải quyết một phần bài toán này.

Nhưng interoperability không chỉ là “tệp (file / 파일) mở được”. Hai hệ có thể đọc cùng tệp (file / 파일) nhưng hiểu khác ngữ nghĩa (semantics / 의미론) của trường dữ liệu (field / 필드) hoặc ranh giới (boundary / 경계). dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) phải bao gồm cả meaning.

> **Nối mạch:** **Mô hình tư duy** khép chuỗi quy ước tọa độ → geographic/projected CRS → datum/frame, geocentric/Earth-fixed → EPSG và transformation → vertical/epoch/dynamic datum → national/local grid → index, address, boundary và interoperability. Kết luận bàn giao owner **World Geography** theo [README](../README.md), để nối sang GIS và dữ liệu vùng.

## Mô hình tư duy

Một coordinate bản ghi (record / 레코드) đầy đủ có thể được hình dung như:

`geometry + CRS + datum/frame + axis/unit + vertical reference + epoch + accuracy + provenance`.

Càng tăng yêu cầu chính xác, càng nhiều siêu dữ liệu (metadata / 메타데이터) trở thành dữ liệu cốt lõi thay vì phụ chú.

Xem tiếp: [GIS và dữ liệu không gian](../00_foundations/04_geospatial_data_gis_remote_sensing.md), [Trắc địa](./00_earth_shape_size_geodesy.md), [Cartography](../00_foundations/03_cartography_projections_scale.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
