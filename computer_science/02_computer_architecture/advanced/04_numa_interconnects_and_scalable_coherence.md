# NUMA, liên kết phần cứng và khả năng mở rộng của cơ chế nhất quán

> **Mạch đọc:** Đặt **NUMA, liên kết phần cứng và khả năng mở rộng của cơ chế nhất quán** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao mô hình truy cập đồng nhất không thể mở rộng mãi** sang **Chính sách chạm đầu tiên và vị trí dữ liệu**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi một máy có nhiều lõi xử lý và nhiều bộ điều khiển bộ nhớ, giả định “RAM có cùng độ trễ ở mọi nơi” không còn đúng. **Truy cập bộ nhớ không đồng nhất (Non-Uniform Memory Access — NUMA / 비균일 메모리 접근)** mô tả hệ thống trong đó truy cập bộ nhớ gần lõi hiện tại rẻ hơn truy cập phải đi qua đường liên kết (interconnect) tới nút hoặc socket khác.

## Vì sao mô hình truy cập đồng nhất không thể mở rộng mãi

Nếu mọi lõi chia sẻ một bus bộ nhớ duy nhất, số lõi tăng sẽ làm tranh chấp băng thông và lưu lượng duy trì nhất quán bộ nhớ đệm (cache / 캐시) tăng. Máy chủ nhiều socket vì thế phân bố bộ điều khiển bộ nhớ theo từng nút. Mỗi socket CPU có các kênh bộ nhớ cục bộ, đồng thời có đường liên kết để truy cập bộ nhớ từ xa và trao đổi thông điệp nhất quán.

Độ trễ truy cập từ xa không chỉ là một số nanosecond cố định cộng thêm. Nó còn phụ thuộc vào băng thông của interconnect, cấu trúc liên kết (topology), hàng đợi và lưu lượng do các lõi khác tạo ra.


> **Chuyển mạch:** Từ **Vì sao mô hình truy cập đồng nhất không thể mở rộng mãi**, ta sang **Chính sách chạm đầu tiên và vị trí dữ liệu** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chính sách chạm đầu tiên và vị trí dữ liệu

Hệ điều hành thường cấp trang vật lý theo **chính sách chạm đầu tiên (first-touch policy)**: trang được đặt gần nút NUMA của luồng chạm vào nó lần đầu. Nếu một luồng khởi tạo toàn bộ mảng rồi các luồng xử lý ở socket khác mới sử dụng, dữ liệu có thể nằm sai nút dù công việc sau đó được chạy song song.

Vì vậy chiến lược khởi tạo có thể ảnh hưởng hiệu năng không phải vì chi phí tính toán của bước khởi tạo, mà vì nó quyết định vị trí vật lý của dữ liệu. Khởi tạo song song đôi khi là cách phân bố trang bộ nhớ đúng theo nơi dữ liệu sẽ được xử lý.


> **Chuyển mạch:** Từ **Chính sách chạm đầu tiên và vị trí dữ liệu**, ta sang **Gắn luồng với CPU** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Gắn luồng với CPU

Bộ lập lịch có thể di chuyển luồng giữa các lõi để cân bằng tải CPU. Tuy nhiên việc di chuyển làm mất dữ liệu bộ nhớ đệm (cache / 캐시) đang nóng và có thể biến truy cập bộ nhớ cục bộ thành truy cập từ xa. **Gắn CPU (CPU affinity)** hoặc lập lịch nhận biết NUMA cố giữ phần tính toán gần dữ liệu khi lợi ích về tính cục bộ lớn hơn lợi ích cân bằng tải.

Không nên ghim mọi luồng một cách máy móc. Ghim sai có thể tạo mất cân bằng hoặc khiến bộ lập lịch không phản ứng được khi tải thay đổi.


> **Chuyển mạch:** Từ **Gắn luồng với CPU**, ta sang **Interconnect và thư mục nhất quán** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Interconnect và thư mục nhất quán

Cơ chế dò tìm quảng bá (snooping) đơn giản phải gửi yêu cầu nhất quán tới nhiều thành phần, nên khó mở rộng khi số lõi tăng. **Nhất quán dựa trên thư mục (directory-based coherence)** lưu siêu dữ liệu về nơi một dòng bộ nhớ đệm (cache / 캐시) đang tồn tại để gửi yêu cầu vô hiệu hóa hoặc truy vấn tới đúng đích.

Thư mục cũng có chi phí: cần thêm siêu dữ liệu, thời gian tra cứu và lưu lượng khi một dòng được chia sẻ rộng. Một dòng bộ nhớ đệm (cache / 캐시) có thể ghi và được nhiều socket cùng truy cập có thể liên tục đổi quyền sở hữu giữa các nút, tạo hiện tượng “ping-pong” và trở thành nút thắt cổ chai.


> **Chuyển mạch:** Từ **Interconnect và thư mục nhất quán**, ta sang **Chia sẻ giả ở cấp NUMA** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chia sẻ giả ở cấp NUMA

Chia sẻ giả (false sharing) trong cùng một socket đã tốn kém; qua nhiều socket còn đắt hơn. Hai luồng cập nhật hai bộ đếm khác nhau nhưng nằm chung một dòng bộ nhớ đệm (cache / 캐시) có thể khiến quyền sở hữu của dòng đó di chuyển liên tục giữa các nút NUMA.

Đệm khoảng cách hoặc căn chỉnh dữ liệu (padding/alignment) có thể giúp với các bộ đếm rất nóng, nhưng làm tăng lượng bộ nhớ sử dụng. Quyết định này phải dựa trên đo lường thay vì áp dụng cho mọi cấu trúc.


> **Chuyển mạch:** Từ **Chia sẻ giả ở cấp NUMA**, ta sang **Cơ sở dữ liệu và JVM** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cơ sở dữ liệu và JVM

Vùng đệm lớn của cơ sở dữ liệu, vùng nhớ động (heap / 힙) lớn của JVM hoặc hệ thống phân tích trong bộ nhớ có thể trải trên nhiều nút NUMA. Nếu bộ cấp phát, luồng thu gom rác và luồng ứng dụng không nhận biết NUMA, độ trễ có thể tăng dù tổng dung lượng RAM vẫn còn nhiều.

Thu gom rác song song hoặc đồng thời cũng tương tác với topology: các luồng thu gom quét đối tượng ở nút từ xa sẽ tạo thêm lưu lượng băng thông. Vì vậy một số môi trường thực thi và bộ cấp phát cung cấp chính sách nhận biết NUMA để cải thiện tính cục bộ.


> **Chuyển mạch:** Từ **Cơ sở dữ liệu và JVM**, ta sang **Mở rộng một máy và mở rộng nhiều máy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mở rộng một máy và mở rộng nhiều máy

NUMA cho thấy một máy chủ lớn không phải một khối đồng nhất. Bên trong nó đã có những đặc tính giống hệ thống phân tán ở quy mô nhỏ: vị trí, topology, truy cập từ xa và chi phí phối hợp.

Mở rộng ra nhiều máy qua mạng có độ trễ lớn hơn rất nhiều, nhưng mô hình tư duy tương tự: đặt tính toán gần dữ liệu, giảm trạng thái dùng chung có thể thay đổi và tránh giao tiếp không cần thiết.


> **Chuyển mạch:** Từ **Mở rộng một máy và mở rộng nhiều máy**, ta sang **Mô hình tư duy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy

> NUMA biến vị trí thành một phần của mô hình hiệu năng. Bộ nhớ không chỉ có dung lượng; dữ liệu còn nằm tại một vị trí trong topology. Khi hệ thống lớn lên, câu hỏi “dữ liệu ở đâu so với nơi tính toán diễn ra?” trở thành câu hỏi kiến trúc.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 memory consistency cache coherence and ordering](./00_memory_consistency_cache_coherence_and_ordering.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
