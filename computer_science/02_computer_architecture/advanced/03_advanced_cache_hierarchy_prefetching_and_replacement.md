# Advanced cache hierarchy, prefetching và replacement

Cache tồn tại vì processor và memory có tốc độ rất khác nhau. Nhưng khi đi sâu hơn L1/L2/L3, câu hỏi không còn là “cache nhanh hơn RAM” mà là cách một hierarchy hữu hạn dự đoán dữ liệu nào đáng giữ gần core, dữ liệu nào nên đẩy xuống tầng thấp hơn và khi nào nên chủ động kéo dữ liệu về trước khi chương trình yêu cầu.

## Locality là giả định, không phải định luật

Cache dựa trên **temporal locality** và **spatial locality**. Nếu một cache line vừa được dùng, có khả năng nó hoặc vùng lân cận sẽ được dùng lại. Workload tuần tự thường phù hợp giả định này; random access trên working set lớn có thể phá vỡ nó.

Một cache line thường chứa nhiều byte hơn đúng object mà CPU đang cần. Điều đó giảm số transaction nếu access có spatial locality, nhưng cũng gây **false sharing** khi nhiều core sửa các biến độc lập nằm chung line.

## Set associativity và conflict miss

Cache direct-mapped đơn giản nhưng nhiều address có thể cạnh tranh cùng slot. Set-associative cache cho mỗi set nhiều ways, giảm conflict nhưng cần so sánh nhiều tags và chọn victim phức tạp hơn.

Miss vì vậy không chỉ do dữ liệu “quá lớn”. Ta thường phân biệt compulsory miss, capacity miss và conflict miss để hiểu cơ chế gây mất locality.

## Inclusive, exclusive và non-inclusive hierarchy

Nếu LLC inclusive, line trong cache nhỏ hơn cũng phải có representation ở LLC. Điều này hỗ trợ một số coherence mechanism nhưng tiêu tốn effective capacity. Exclusive hierarchy cố tránh duplicate line giữa levels, đổi lại movement phức tạp hơn. Nhiều CPU hiện đại dùng policy non-inclusive/non-exclusive để cân bằng.

## Replacement không thể biết tương lai

Optimal replacement về lý thuyết sẽ loại line có lần dùng tiếp theo xa nhất, nhưng hardware không biết future access. LRU chính xác cũng đắt khi associativity lớn. Processor dùng approximation như pseudo-LRU, RRIP hoặc adaptive policies.

Điểm quan trọng là replacement policy đang cố ước lượng **reuse distance**. Với streaming workload, giữ line vừa đọc lâu có thể vô ích; với hot working set, eviction sai làm miss rate tăng mạnh.

## Hardware prefetcher

**Prefetching (프리페칭)** dự đoán future access và đưa line vào cache sớm. Stream/stride prefetcher hoạt động tốt với array tuần tự. Pointer chasing khó hơn vì address tiếp theo phụ thuộc dữ liệu vừa load.

Prefetch không miễn phí. Prefetch quá mạnh có thể chiếm bandwidth, pollute cache và đẩy hot data ra ngoài. Vì vậy prefetch accuracy và timeliness đều quan trọng: đúng nhưng quá muộn không che latency; đúng nhưng quá sớm có thể bị evict trước khi dùng.

## Software và data layout

Array of Structures thuận tiện về object model nhưng có thể tải nhiều field không dùng. Structure of Arrays gom cùng field liên tục, thường phù hợp vectorization và cache locality hơn. Đây là lý do data-oriented design có thể vượt object-oriented layout trong hot path dù thuật toán cấp cao giống nhau.

Blocking/tiling trong matrix multiplication cũng là cache reasoning: chia problem để working set của block vừa cache, nhờ đó cùng line được reuse nhiều lần trước khi bị thay thế.

## Cache coherence không đồng nghĩa consistency

Coherence trả lời các core thống nhất giá trị của một cache line như thế nào. Memory consistency trả lời ordering giữa nhiều memory operations được software quan sát ra sao. Một hệ thống có coherence vẫn cần memory model và fences phù hợp.

Xem thêm: [Memory consistency, cache coherence và ordering](./00_memory_consistency_cache_coherence_and_ordering.md).

## Production reasoning

Khi service có CPU utilization cao nhưng IPC thấp và LLC miss cao, tăng thread có thể làm tệ hơn vì working set cạnh tranh cache. Khi nhiều thread cập nhật counters nằm sát nhau, false sharing có thể tạo coherence traffic dù logic không khóa nhau.

Performance counter như cache-misses, LLC-loads và stalled-cycles chỉ có ý nghĩa khi đặt cạnh access pattern và working-set size. Không nên kết luận “cache là bottleneck” chỉ từ một metric đơn lẻ.

## Mental Model

> Cache hierarchy là một hệ thống dự đoán reuse dưới giới hạn capacity và bandwidth. Tối ưu cache không phải làm mọi thứ “nằm trong cache”, mà là tổ chức computation để dữ liệu có giá trị được reuse đủ sớm, giảm conflict và tránh tạo traffic không cần thiết.