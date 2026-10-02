# Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**. Route đi từ tọa độ và quy ước đo → datum/epoch và hệ quy chiếu → geographic/projected CRS → phép chiếu, sai số và metadata → interoperability, để con số vị trí luôn đi kèm điều kiện đo.

## Tọa độ là kết quả của một quy ước đo lường

Một chuỗi như `37.5665, 126.9780` chưa phải vị trí hoàn chỉnh. Ta còn cần biết đó là latitude–longitude hay longitude–latitude, đơn vị gì, datum nào, epoch nào và dữ liệu được kỳ vọng chính xác đến mức nào.

Trong GIS, **hệ quy chiếu tọa độ (Coordinate Reference system, CRS)** đóng vai trò giống hệ kiểu (type system / 타입 시스템). Nó quy định cách con số liên hệ với không gian thật. Hai array giống nhau về cấu trúc nhưng khác CRS có thể đại diện cho hai nơi khác nhau.

> **Chuyển mạch:** Trong **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Tọa độ là kết quả của một quy ước đo lường** nêu điều cần giải thích; **Geographic CRS và projected CRS** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Datum và tham chiếu (reference / 참조) frame** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Geographic CRS và projected CRS

**Geographic CRS** dùng tọa độ góc trên ellipsoid, thường là latitude và longitude. **Projected CRS** dùng phép chiếu để biến bề mặt cong thành tọa độ phẳng, thường theo mét.

Geographic CRS thuận tiện cho lưu trữ toàn cầu và trao đổi. Projected CRS thuận tiện cho nhiều phép đo cục bộ như diện tích, buffering và thiết kế kỹ thuật.

Không có CRS duy nhất tối ưu cho mọi việc. Một hệ thống tốt tách CRS lưu trữ, CRS phân tích và CRS hiển thị khi cần.

> **Chuyển mạch:** Ở chặng này của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, sau nội dung của **Geographic CRS và projected CRS**, **Datum và tham chiếu (reference / 참조) frame** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Geocentric và Earth-fixed** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Datum và tham chiếu (reference / 참조) frame

**Datum** gắn ellipsoid với Trái Đất. **tham chiếu (reference / 참조) frame** là hiện thực hóa thực tế của hệ tham chiếu bằng mạng trạm, tọa độ và mô hình chuyển động.

Trong hệ tĩnh đơn giản, người dùng thường không phân biệt hai khái niệm. Nhưng ở trắc địa chính xác, frame và epoch là bắt buộc vì vỏ Trái Đất chuyển động.

WGS 84 không nên được hiểu như một nhãn bất biến duy nhất cho mọi thời kỳ. Các realization của hệ toàn cầu được cập nhật để bám theo phép đo tốt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Geocentric và Earth-fixed** tiếp nhận điểm tựa từ **Datum và tham chiếu (reference / 참조) frame** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **EPSG mã (code / 코드) giúp định danh nhưng không sửa được siêu dữ liệu (metadata / 메타데이터) sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Geocentric và Earth-fixed

Một khung toàn cầu thường lấy tâm gần center of mass của Trái Đất và quay cùng hành tinh, tạo hệ **Earth-Centered, Earth-Fixed (ECEF)**. Tọa độ ECEF dùng ba trục Cartesian `X,Y,Z`.

GNSS tính vị trí thuận tiện trong khung ba chiều như vậy. Vĩ độ–kinh độ là một biểu diễn (representation / 표현) được suy ra từ tọa độ địa tâm và ellipsoid.

Mô hình tư duy (mental model / 사고 모델) này giải thích vì sao tọa độ địa lý không phải “đầu ra thô” của vệ tinh; chúng là một lớp chuyển đổi.

> **Chuyển mạch:** Trong **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Geocentric và Earth-fixed** nêu điều cần giải thích; **EPSG mã (code / 코드) giúp định danh nhưng không sửa được siêu dữ liệu (metadata / 메타데이터) sai** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Coordinate transformation là phép biến đổi có điều kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## EPSG mã (code / 코드) giúp định danh nhưng không sửa được siêu dữ liệu (metadata / 메타데이터) sai

Registry EPSG cung cấp mã cho nhiều CRS và transformation. Mã như `EPSG:4326` giúp hệ thống trao đổi định nghĩa nhất quán.

Nhưng mã không có phép thuật. Nếu tệp (file / 파일) thực sự ở một CRS mà bị gán nhãn CRS khác, phần mềm sẽ xử lý sai một cách rất nhất quán.

**Assign CRS** nghĩa “các con số hiện tại nên được diễn giải theo hệ này”. **Reproject** nghĩa “hãy biến đổi các con số để giữ cùng vị trí vật lý trong hệ khác”. Nhầm hai thao tác là lỗi kinh điển.

> **Chuyển mạch:** Ở chặng này của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **EPSG mã (code / 코드) giúp định danh nhưng không sửa được siêu dữ liệu (metadata / 메타데이터) sai** nêu điều cần giải thích; **Coordinate transformation là phép biến đổi có điều kiện** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Vertical datum là một hệ riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coordinate transformation là phép biến đổi có điều kiện

Chuyển giữa hai CRS có thể cần projection formula, datum transformation, grid correction và đôi khi epoch. Không phải mọi transformation đều có độ chính xác giống nhau.

Nếu nguồn (source / 소스) datum và mục tiêu (target / 대상) datum khác, phần mềm có thể dùng transformation xấp xỉ khi thiếu grid tệp (file / 파일) chính xác. Vì vậy chuỗi xử lý (pipeline / 파이프라인) kỹ thuật nên ghi transformation phương thức (method / 메서드) và expected accuracy, đặc biệt khi dùng dữ liệu survey.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Vertical datum là một hệ riêng** tiếp nhận điểm tựa từ **Coordinate transformation là phép biến đổi có điều kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Epoch và động (dynamic / 동적) datum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vertical datum là một hệ riêng

Tọa độ ngang đúng không bảo đảm cao độ đúng. Dữ liệu độ cao có thể dùng ellipsoid, geoid mô hình (model / 모델) hoặc vertical datum quốc gia dựa trên tide gauge/leveling mạng (network / 네트워크).

Khi ghép DEM, GNSS và survey, cần kiểm tra vertical tham chiếu (reference / 참조) riêng. Một chuỗi xử lý (pipeline / 파이프라인) chỉ kiểm tra `EPSG` của horizontal CRS nhưng bỏ vertical datum vẫn có thể gây lỗi lớn.

> **Chuyển mạch:** Trong **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Epoch và động (dynamic / 동적) datum** tiếp nhận điểm tựa từ **Vertical datum là một hệ riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **National grid và cục bộ (local / 로컬) kỹ thuật (engineering / 엔지니어링) CRS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Epoch và động (dynamic / 동적) datum

Ở độ chính xác cao, tọa độ thay đổi theo chuyển động mảng. **động (dynamic / 동적) datum/tham chiếu (reference / 참조) frame** lưu tọa độ kèm epoch và mô hình (model / 모델) vận tốc.

Nếu dữ liệu năm 2010 được so với survey 2030 mà không propagate tọa độ về cùng epoch, sai khác có thể bị hiểu nhầm là biến dạng công trình dù thực chất là chuyển động frame.

Đây là điểm ngày càng quan trọng khi smartphone, autonomous các hệ thống (systems / 시스템들) và precise positioning đạt độ chính xác cao hơn.

> **Chuyển mạch:** Ở chặng này của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **National grid và cục bộ (local / 로컬) kỹ thuật (engineering / 엔지니어링) CRS** tiếp nhận điểm tựa từ **Epoch và động (dynamic / 동적) datum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Toàn cục (global / 전역) grid chỉ mục (index / 인덱스) không thay thế CRS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## National grid và cục bộ (local / 로컬) kỹ thuật (engineering / 엔지니어링) CRS

Các quốc gia thường có national grid hoặc projected CRS tối ưu cho lãnh thổ. Korea và Vietnam đều có hệ thống tọa độ bản đồ/quốc gia phục vụ cadastral, survey và hạ tầng (infrastructure / 인프라).

Dữ liệu web thường đến ở WGS84/Web Mercator, còn dữ liệu hành chính–kỹ thuật có thể ở national CRS. Vì vậy ETL geospatial thực tế phải xử lý transformation thay vì giả định mọi tệp (file / 파일) dùng cùng hệ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Toàn cục (global / 전역) grid chỉ mục (index / 인덱스) không thay thế CRS** tiếp nhận điểm tựa từ **National grid và cục bộ (local / 로컬) kỹ thuật (engineering / 엔지니어링) CRS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Address, place name và coordinate là ba hệ khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Toàn cục (global / 전역) grid chỉ mục (index / 인덱스) không thay thế CRS

Các hệ như geohash, H3, S2 hoặc tile XYZ chia bề mặt thành cell phân cấp. Chúng hữu ích cho spatial indexing, aggregation, caching và phân tán (distributed / 분산) processing.

Nhưng chúng không loại bỏ nhu cầu hiểu datum và hình học (geometry / 기하학). Một H3 cell là cách lập chỉ mục trên bề mặt; nó không tự biến mọi khoảng cách hay diện tích thành chính xác tuyệt đối.

Khi aggregate dữ liệu theo grid, kích thước cell trở thành quy mô (scale / 규모) of phân tích (analysis / 분석) và có thể tạo MAUP dạng lưới.

> **Chuyển mạch:** Trong **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Address, place name và coordinate là ba hệ khác nhau** tiếp nhận điểm tựa từ **Toàn cục (global / 전역) grid chỉ mục (index / 인덱스) không thay thế CRS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ranh giới (boundary / 경계) dataset cũng cần tham chiếu (reference / 참조) hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Address, place name và coordinate là ba hệ khác nhau

Địa chỉ là hệ quy ước xã hội; địa danh là lớp ngôn ngữ–lịch sử; tọa độ là biểu diễn (representation / 표현) hình học. **Geocoding** nối các hệ này nhưng luôn chứa ambiguity.

Một tên địa danh có thể trùng ở nhiều nơi, một địa chỉ có thể đổi sau cải cách hành chính và một polygon địa giới có thể có nhiều phiên bản (version / 버전). Hệ geocoder tốt cần phiên bản (version / 버전), provenance và confidence.

> **Chuyển mạch:** Ở chặng này của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Address, place name và coordinate là ba hệ khác nhau** đã nêu tiêu chí phân biệt, còn **Ranh giới (boundary / 경계) dataset cũng cần tham chiếu (reference / 참조) hệ thống (system / 시스템)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Geospatial interoperability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ranh giới (boundary / 경계) dataset cũng cần tham chiếu (reference / 참조) hệ thống (system / 시스템)

Biên giới hành chính và coastline không chỉ cần CRS mà còn cần thời điểm và nguồn. Cùng một nước có thể có polygon khác nhau giữa statistical dataset, cadastral dataset và generalized web map.

Đối với khu vực tranh chấp, hình học (geometry / 기하학) còn có ngữ nghĩa (semantic / 의미적) khác nhau: claim line, điều khiển (control / 제어) line hoặc administrative ranh giới (boundary / 경계). Không nên chỉ lưu một polygon mà không lưu loại ranh giới (boundary / 경계).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Ranh giới (boundary / 경계) dataset cũng cần tham chiếu (reference / 참조) hệ thống (system / 시스템)** đã nêu tiêu chí phân biệt, còn **Geospatial interoperability** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Geospatial interoperability

Khi nhiều hệ thống trao đổi dữ liệu, cần nhất quán về CRS, hình học (geometry / 기하학) kiểu (type / 타입), axis thứ tự (order / 순서), encoding, precision và thời gian (time / 시간) tham chiếu (reference / 참조). OGC standards, GeoJSON, GeoPackage, WKT và các format khác giải quyết một phần bài toán này.

Nhưng interoperability không chỉ là “tệp (file / 파일) mở được”. Hai hệ có thể đọc cùng tệp (file / 파일) nhưng hiểu khác ngữ nghĩa (semantics / 의미론) của trường dữ liệu (field / 필드) hoặc ranh giới (boundary / 경계). dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) phải bao gồm cả meaning.

> **Chuyển mạch:** Trong **Hệ quy chiếu toàn cầu, datum và hạ tầng tọa độ**, **Mô hình tư duy** gom các mảnh từ **Geospatial interoperability** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Một coordinate bản ghi (record / 레코드) đầy đủ có thể được hình dung như:

`geometry + CRS + datum/frame + axis/unit + vertical reference + epoch + accuracy + provenance`.

Càng tăng yêu cầu chính xác, càng nhiều siêu dữ liệu (metadata / 메타데이터) trở thành dữ liệu cốt lõi thay vì phụ chú.

Xem tiếp: [GIS và dữ liệu không gian](../00_foundations/04_geospatial_data_gis_remote_sensing.md), [Trắc địa](./00_earth_shape_size_geodesy.md), [Cartography](../00_foundations/03_cartography_projections_scale.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
