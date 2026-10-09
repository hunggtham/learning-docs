# NUMA, liên kết phần cứng và khả năng mở rộng của cơ chế nhất quán

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **NUMA, liên kết phần cứng và khả năng mở rộng của cơ chế nhất quán**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao mô hình truy cập đồng nhất không thể mở rộng mãi** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Chính sách chạm đầu tiên và vị trí dữ liệu** để đối chiếu nhận định với dữ liệu và nguồn. Mạch này nối NUMA với interconnect và scalable coherence, để locality của bộ nhớ đi vào topology nhiều socket.

Khi một máy có nhiều lõi xử lý và nhiều bộ điều khiển bộ nhớ, giả định “RAM có cùng độ trễ ở mọi nơi” không còn đúng. **Truy cập bộ nhớ không đồng nhất (Non-Uniform Memory Access — NUMA / 비균일 메모리 접근)** mô tả hệ thống trong đó truy cập bộ nhớ gần lõi hiện tại rẻ hơn truy cập phải đi qua đường liên kết (interconnect) tới nút hoặc socket khác.

## Vì sao mô hình truy cập đồng nhất không thể mở rộng mãi

Nếu mọi lõi chia sẻ một bus bộ nhớ duy nhất, số lõi tăng sẽ làm tranh chấp băng thông và lưu lượng duy trì nhất quán bộ nhớ đệm (cache / 캐시) tăng. Máy chủ nhiều socket vì thế phân bố bộ điều khiển bộ nhớ theo từng nút. Mỗi socket CPU có các kênh bộ nhớ cục bộ, đồng thời có đường liên kết để truy cập bộ nhớ từ xa và trao đổi thông điệp nhất quán.

Độ trễ truy cập từ xa không chỉ là một số nanosecond cố định cộng thêm. Nó còn phụ thuộc vào băng thông của interconnect, cấu trúc liên kết (topology), hàng đợi và lưu lượng do các lõi khác tạo ra.

Uniform access không scale mãi vì distance, bandwidth và coherence traffic tăng theo số core/socket. Vì vậy first-touch quyết định page nằm ở đâu, còn thread/CPU affinity giữ computation gần dữ liệu sau khi placement đã được chọn.

## Chính sách chạm đầu tiên và vị trí dữ liệu

Hệ điều hành thường cấp trang vật lý theo **chính sách chạm đầu tiên (first-touch policy)**: trang được đặt gần nút NUMA của luồng chạm vào nó lần đầu. Nếu một luồng khởi tạo toàn bộ mảng rồi các luồng xử lý ở socket khác mới sử dụng, dữ liệu có thể nằm sai nút dù công việc sau đó được chạy song song.

Vì vậy chiến lược khởi tạo có thể ảnh hưởng hiệu năng không phải vì chi phí tính toán của bước khởi tạo, mà vì nó quyết định vị trí vật lý của dữ liệu. Khởi tạo song song đôi khi là cách phân bố trang bộ nhớ đúng theo nơi dữ liệu sẽ được xử lý.

First-touch biến lúc khởi tạo thành quyết định placement lâu dài. Placement chỉ có ích nếu scheduler giữ thread gần page; khi locality và load balance xung đột, interconnect cùng coherence directory quyết định chi phí còn lại.

## Gắn luồng với CPU

Bộ lập lịch có thể di chuyển luồng giữa các lõi để cân bằng tải CPU. Tuy nhiên việc di chuyển làm mất dữ liệu bộ nhớ đệm (cache / 캐시) đang nóng và có thể biến truy cập bộ nhớ cục bộ thành truy cập từ xa. **Gắn CPU (CPU affinity)** hoặc lập lịch nhận biết NUMA cố giữ phần tính toán gần dữ liệu khi lợi ích về tính cục bộ lớn hơn lợi ích cân bằng tải.

Không nên ghim mọi luồng một cách máy móc. Ghim sai có thể tạo mất cân bằng hoặc khiến bộ lập lịch không phản ứng được khi tải thay đổi.

CPU affinity giảm remote access bằng cách giữ thread gần dữ liệu, nhưng không xóa traffic giữa các node. Interconnect và directory phải xử lý traffic đó; cache line được nhiều node ghi sẽ lộ chi phí qua false sharing ở cấp NUMA.

## Interconnect và thư mục nhất quán

Cơ chế dò tìm quảng bá (snooping) đơn giản phải gửi yêu cầu nhất quán tới nhiều thành phần, nên khó mở rộng khi số lõi tăng. **Nhất quán dựa trên thư mục (directory-based coherence)** lưu siêu dữ liệu về nơi một dòng bộ nhớ đệm (cache / 캐시) đang tồn tại để gửi yêu cầu vô hiệu hóa hoặc truy vấn tới đúng đích.

Thư mục cũng có chi phí: cần thêm siêu dữ liệu, thời gian tra cứu và lưu lượng khi một dòng được chia sẻ rộng. Một dòng bộ nhớ đệm (cache / 캐시) có thể ghi và được nhiều socket cùng truy cập có thể liên tục đổi quyền sở hữu giữa các nút, tạo hiện tượng “ping-pong” và trở thành nút thắt cổ chai.

Directory làm coherence có thể mở rộng hơn snooping, nhưng ownership ping-pong vẫn đắt khi cùng line bị nhiều node cập nhật. Database buffer và JVM heap thường phơi bày pattern này ở workload thực.

## Chia sẻ giả ở cấp NUMA

Chia sẻ giả (false sharing) trong cùng một socket đã tốn kém; qua nhiều socket còn đắt hơn. Hai luồng cập nhật hai bộ đếm khác nhau nhưng nằm chung một dòng bộ nhớ đệm (cache / 캐시) có thể khiến quyền sở hữu của dòng đó di chuyển liên tục giữa các nút NUMA.

Đệm khoảng cách hoặc căn chỉnh dữ liệu (padding/alignment) có thể giúp với các bộ đếm rất nóng, nhưng làm tăng lượng bộ nhớ sử dụng. Quyết định này phải dựa trên đo lường thay vì áp dụng cho mọi cấu trúc.

False sharing biến topology thành chi phí của một biến tưởng như độc lập. Database và JVM có thể giảm chi phí bằng placement, allocator hoặc GC policy, nhưng khi mở rộng vượt một máy, network sẽ thay thế interconnect với latency lớn hơn.

## Cơ sở dữ liệu và JVM

Vùng đệm lớn của cơ sở dữ liệu, vùng nhớ động (heap / 힙) lớn của JVM hoặc hệ thống phân tích trong bộ nhớ có thể trải trên nhiều nút NUMA. Nếu bộ cấp phát, luồng thu gom rác và luồng ứng dụng không nhận biết NUMA, độ trễ có thể tăng dù tổng dung lượng RAM vẫn còn nhiều.

Thu gom rác song song hoặc đồng thời cũng tương tác với topology: các luồng thu gom quét đối tượng ở nút từ xa sẽ tạo thêm lưu lượng băng thông. Vì vậy một số môi trường thực thi và bộ cấp phát cung cấp chính sách nhận biết NUMA để cải thiện tính cục bộ.

DB buffer, JVM heap và GC thread đều biến placement thành một phần của performance contract. So sánh một máy với nhiều máy giúp thấy cùng nguyên tắc locality, ownership và giảm shared state ở hai quy mô khác nhau.

## Mở rộng một máy và mở rộng nhiều máy

NUMA cho thấy một máy chủ lớn không phải một khối đồng nhất. Bên trong nó đã có những đặc tính giống hệ thống phân tán ở quy mô nhỏ: vị trí, topology, truy cập từ xa và chi phí phối hợp.

Mở rộng ra nhiều máy qua mạng có độ trễ lớn hơn rất nhiều, nhưng mô hình tư duy tương tự: đặt tính toán gần dữ liệu, giảm trạng thái dùng chung có thể thay đổi và tránh giao tiếp không cần thiết.

NUMA biến vị trí thành một biến của invariant hiệu năng: dữ liệu phải gần nơi dùng, và shared state phải trả chi phí theo topology. Mô hình đó là điểm nối để đọc các hệ thống phân tán mà không coi một máy lớn là một memory pool đồng nhất.

## Mô hình tư duy

> NUMA biến vị trí thành một phần của mô hình hiệu năng. Bộ nhớ không chỉ có dung lượng; dữ liệu còn nằm tại một vị trí trong topology. Khi hệ thống lớn lên, câu hỏi “dữ liệu ở đâu so với nơi tính toán diễn ra?” trở thành câu hỏi kiến trúc.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
