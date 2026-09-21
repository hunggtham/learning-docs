# Phân cấp bộ nhớ đệm nâng cao, nạp trước và chính sách thay thế

Bộ nhớ đệm (cache) tồn tại vì bộ xử lý (processor) và bộ nhớ chính có tốc độ rất khác nhau. Khi đi sâu hơn các tầng L1/L2/L3, câu hỏi không còn chỉ là “cache nhanh hơn RAM”, mà là cách một hệ thống phân cấp hữu hạn dự đoán dữ liệu nào đáng giữ gần lõi xử lý (core), dữ liệu nào nên chuyển xuống tầng thấp hơn và khi nào nên chủ động đưa dữ liệu về trước khi chương trình yêu cầu.

## Tính cục bộ là giả định, không phải định luật

Cache dựa trên **tính cục bộ theo thời gian (temporal locality)** và **tính cục bộ theo không gian (spatial locality)**. Nếu một dòng cache (cache line) vừa được sử dụng, có khả năng chính dữ liệu đó hoặc vùng lân cận sẽ sớm được dùng lại. Khối lượng công việc (workload) truy cập tuần tự thường phù hợp với giả định này, trong khi truy cập ngẫu nhiên (random access) trên tập dữ liệu làm việc (working set) lớn có thể phá vỡ nó.

Một dòng cache thường chứa nhiều byte hơn đúng đối tượng mà CPU đang cần. Điều này giảm số lần giao dịch bộ nhớ khi chương trình có tính cục bộ theo không gian, nhưng cũng có thể gây **chia sẻ giả (false sharing)** khi nhiều lõi sửa các biến độc lập nhưng các biến đó lại nằm chung một dòng cache.

## Tính kết hợp theo tập và xung đột cache

Cache ánh xạ trực tiếp (direct-mapped cache) đơn giản, nhưng nhiều địa chỉ có thể cạnh tranh cùng một vị trí. Cache kết hợp theo tập (set-associative cache) cho phép mỗi tập có nhiều vị trí (way), nhờ đó giảm xung đột nhưng phải so sánh nhiều thẻ địa chỉ (tag) và chọn dòng bị thay thế phức tạp hơn.

Một lần trượt cache (cache miss) vì vậy không chỉ xuất hiện khi dữ liệu “quá lớn”. Ta thường phân biệt trượt bắt buộc (compulsory miss), trượt do thiếu dung lượng (capacity miss) và trượt do xung đột (conflict miss) để hiểu nguyên nhân thật sự làm mất tính cục bộ.

## Phân cấp bao hàm, loại trừ và không bao hàm

Nếu cache cấp cuối (LLC) sử dụng chính sách bao hàm (inclusive), dữ liệu có mặt ở cache nhỏ hơn cũng phải có đại diện tại LLC. Cách này hỗ trợ một số cơ chế nhất quán cache (cache coherence) nhưng làm giảm dung lượng hiệu dụng. Phân cấp loại trừ (exclusive) cố tránh lưu trùng một dòng ở nhiều tầng, đổi lại việc di chuyển dữ liệu phức tạp hơn. Nhiều CPU hiện đại dùng chính sách không hoàn toàn bao hàm cũng không hoàn toàn loại trừ để cân bằng hai phía.

## Chính sách thay thế không thể biết trước tương lai

Về lý thuyết, chính sách thay thế tối ưu (optimal replacement) sẽ loại dòng có lần sử dụng tiếp theo xa nhất, nhưng phần cứng không biết trước chuỗi truy cập tương lai. LRU chính xác cũng tốn chi phí khi độ kết hợp lớn. Vì vậy bộ xử lý thường dùng các phương pháp xấp xỉ như pseudo-LRU, RRIP hoặc chính sách thích nghi.

Bản chất của chính sách thay thế là ước lượng **khoảng cách tái sử dụng (reuse distance)**. Với luồng đọc tuần tự, giữ một dòng vừa đọc quá lâu có thể vô ích; với tập dữ liệu nóng, loại nhầm dòng sẽ làm tỷ lệ trượt cache tăng mạnh.

## Bộ nạp trước của phần cứng

**Nạp trước (prefetching / 프리페칭)** dự đoán lần truy cập tương lai và đưa dòng dữ liệu vào cache sớm. Bộ nạp trước theo luồng hoặc theo bước nhảy (stream/stride prefetcher) hoạt động tốt với mảng tuần tự. Truy lần theo con trỏ (pointer chasing) khó hơn vì địa chỉ tiếp theo phụ thuộc vào dữ liệu vừa được đọc.

Nạp trước không miễn phí. Nếu quá mạnh, nó có thể chiếm băng thông (bandwidth), làm ô nhiễm cache và đẩy dữ liệu nóng ra ngoài. Vì vậy độ chính xác và thời điểm nạp đều quan trọng: dự đoán đúng nhưng quá muộn không che được độ trễ; dự đoán đúng nhưng quá sớm có thể khiến dòng dữ liệu bị loại trước khi được dùng.

## Bố trí dữ liệu trong phần mềm

Cấu trúc “mảng các cấu trúc” (Array of Structures — AoS) thuận tiện cho mô hình đối tượng nhưng có thể tải nhiều trường không cần dùng. “Cấu trúc các mảng” (Structure of Arrays — SoA) gom các trường cùng loại thành vùng liên tục, thường phù hợp hơn với xử lý véc-tơ (vectorization) và tính cục bộ của cache. Đây là một lý do thiết kế hướng dữ liệu (data-oriented design) có thể hiệu quả hơn bố trí hướng đối tượng trên đường chạy nóng (hot path), dù thuật toán cấp cao không thay đổi.

Kỹ thuật chia khối (blocking/tiling) trong nhân ma trận cũng dựa trên cùng lập luận: chia bài toán để tập dữ liệu của mỗi khối vừa với cache, nhờ đó một dòng dữ liệu được tái sử dụng nhiều lần trước khi bị thay thế.

## Nhất quán cache không đồng nghĩa với mô hình nhất quán bộ nhớ

Nhất quán cache (cache coherence) trả lời cách các lõi thống nhất giá trị của cùng một dòng cache. Mô hình nhất quán bộ nhớ (memory consistency) trả lời thứ tự mà nhiều thao tác bộ nhớ có thể được phần mềm quan sát. Một hệ thống có coherence vẫn cần mô hình bộ nhớ và hàng rào bộ nhớ (memory fence) phù hợp.

Xem thêm: [Memory consistency, cache coherence và ordering](./00_memory_consistency_cache_coherence_and_ordering.md).

## Suy luận trong hệ thống thực tế

Khi một dịch vụ có mức sử dụng CPU cao nhưng số lệnh hoàn thành mỗi chu kỳ (IPC) thấp và tỷ lệ trượt LLC cao, tăng thêm luồng (thread) có thể làm tình hình tệ hơn vì các tập dữ liệu làm việc cạnh tranh cache. Khi nhiều luồng cập nhật các bộ đếm nằm sát nhau, chia sẻ giả có thể tạo lưu lượng coherence lớn dù logic chương trình không khóa lẫn nhau.

Các bộ đếm hiệu năng (performance counter) như `cache-misses`, `LLC-loads` và `stalled-cycles` chỉ có ý nghĩa khi đặt cạnh kiểu truy cập và kích thước tập dữ liệu làm việc. Không nên kết luận “cache là nút thắt cổ chai (bottleneck)” chỉ từ một chỉ số đơn lẻ.

## Mô hình tư duy

> Phân cấp cache là một hệ thống dự đoán khả năng tái sử dụng dữ liệu dưới giới hạn dung lượng và băng thông. Tối ưu cache không phải làm mọi thứ “nằm trong cache”, mà là tổ chức tính toán để dữ liệu có giá trị được tái sử dụng đủ sớm, giảm xung đột và tránh tạo lưu lượng không cần thiết.