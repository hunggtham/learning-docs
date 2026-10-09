# Phân cấp bộ nhớ đệm nâng cao, nạp trước và chính sách thay thế

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Phân cấp bộ nhớ đệm nâng cao, nạp trước và chính sách thay thế**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tính cục bộ là giả định, không phải định luật** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Tính kết hợp theo tập và xung đột bộ nhớ đệm (cache / 캐시)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối cache hierarchy với prefetching và replacement, để latency được đọc qua locality, bandwidth và pollution.

Bộ nhớ đệm (cache / 캐시) tồn tại vì bộ xử lý (processor) và bộ nhớ chính có tốc độ rất khác nhau. Khi đi sâu hơn các tầng L1/L2/L3, câu hỏi không còn chỉ là “bộ nhớ đệm (cache / 캐시) nhanh hơn RAM”, mà là cách một hệ thống phân cấp hữu hạn dự đoán dữ liệu nào đáng giữ gần lõi xử lý (core), dữ liệu nào nên chuyển xuống tầng thấp hơn và khi nào nên chủ động đưa dữ liệu về trước khi chương trình yêu cầu.

## Tính cục bộ là giả định, không phải định luật

Bộ nhớ đệm (cache / 캐시) dựa trên **tính cục bộ theo thời gian (temporal locality)** và **tính cục bộ theo không gian (spatial locality)**. Nếu một dòng bộ nhớ đệm (cache / 캐시) (cache line) vừa được sử dụng, có khả năng chính dữ liệu đó hoặc vùng lân cận sẽ sớm được dùng lại. Khối lượng công việc (workload) truy cập tuần tự thường phù hợp với giả định này, trong khi truy cập ngẫu nhiên (random access) trên tập dữ liệu làm việc (working set) lớn có thể phá vỡ nó.

Một dòng bộ nhớ đệm (cache / 캐시) thường chứa nhiều byte hơn đúng đối tượng mà CPU đang cần. Điều này giảm số lần giao dịch bộ nhớ khi chương trình có tính cục bộ theo không gian, nhưng cũng có thể gây **chia sẻ giả (false sharing)** khi nhiều lõi sửa các biến độc lập nhưng các biến đó lại nằm chung một dòng bộ nhớ đệm (cache / 캐시).

Locality tạo cơ hội tái sử dụng, nhưng set associativity quyết định dữ liệu có cùng tranh một vị trí hay không. Sau khi phân biệt conflict miss, ta cần xét cách các tầng cache phối hợp trước khi chọn replacement policy.

## Tính kết hợp theo tập và xung đột bộ nhớ đệm (cache / 캐시)

Bộ nhớ đệm (cache / 캐시) ánh xạ trực tiếp (direct-mapped cache) đơn giản, nhưng nhiều địa chỉ có thể cạnh tranh cùng một vị trí. bộ nhớ đệm (cache / 캐시) kết hợp theo tập (set-associative cache) cho phép mỗi tập có nhiều vị trí (way), nhờ đó giảm xung đột nhưng phải so sánh nhiều thẻ địa chỉ (tag) và chọn dòng bị thay thế phức tạp hơn.

Một lần trượt bộ nhớ đệm (cache / 캐시) (cache miss) vì vậy không chỉ xuất hiện khi dữ liệu “quá lớn”. Ta thường phân biệt trượt bắt buộc (compulsory miss), trượt do thiếu dung lượng (capacity miss) và trượt do xung đột (conflict miss) để hiểu nguyên nhân thật sự làm mất tính cục bộ.

Set associativity giảm conflict miss bằng cách cho một set nhiều ways, nhưng dung lượng và nội dung trùng lặp giữa các tầng vẫn quyết định hiệu quả thực. Inclusive, exclusive và non-inclusive hierarchy đặt các trade-off đó thành policy ở cấp toàn hệ thống.

## Phân cấp bao hàm, loại trừ và không bao hàm

Nếu bộ nhớ đệm (cache / 캐시) cấp cuối (LLC) sử dụng chính sách bao hàm (inclusive), dữ liệu có mặt ở bộ nhớ đệm (cache / 캐시) nhỏ hơn cũng phải có đại diện tại LLC. Cách này hỗ trợ một số cơ chế nhất quán bộ nhớ đệm (cache / 캐시) (cache coherence) nhưng làm giảm dung lượng hiệu dụng. Phân cấp loại trừ (exclusive) cố tránh lưu trùng một dòng ở nhiều tầng, đổi lại việc di chuyển dữ liệu phức tạp hơn. Nhiều CPU hiện đại dùng chính sách không hoàn toàn bao hàm cũng không hoàn toàn loại trừ để cân bằng hai phía.

Hierarchy policy quyết định line nào còn chỗ khi nhiều tầng cùng giữ dữ liệu. Replacement không thể biết tương lai nên phải ước lượng reuse distance; prefetch sau đó còn làm thay đổi chính access stream mà replacement quan sát.

## Chính sách thay thế không thể biết trước tương lai

Về lý thuyết, chính sách thay thế tối ưu (optimal replacement) sẽ loại dòng có lần sử dụng tiếp theo xa nhất, nhưng phần cứng không biết trước chuỗi truy cập tương lai. LRU chính xác cũng tốn chi phí khi độ kết hợp lớn. Vì vậy bộ xử lý thường dùng các phương pháp xấp xỉ như pseudo-LRU, RRIP hoặc chính sách thích nghi.

Bản chất của chính sách thay thế là ước lượng **khoảng cách tái sử dụng (reuse distance)**. Với luồng đọc tuần tự, giữ một dòng vừa đọc quá lâu có thể vô ích; với tập dữ liệu nóng, loại nhầm dòng sẽ làm tỷ lệ trượt bộ nhớ đệm (cache / 캐시) tăng mạnh.

Replacement chọn line dựa trên lịch sử đã thấy; prefetch đưa thêm dự đoán về tương lai vào cache. Khi dự đoán sai hoặc quá sớm, bandwidth và cache residency bị tiêu hao, nên bố trí dữ liệu trong phần mềm trở thành biến có thể kiểm soát.

## Bộ nạp trước của phần cứng

**Nạp trước (prefetching / 프리페칭)** dự đoán lần truy cập tương lai và đưa dòng dữ liệu vào bộ nhớ đệm (cache / 캐시) sớm. Bộ nạp trước theo luồng hoặc theo bước nhảy (stream/stride prefetcher) hoạt động tốt với mảng tuần tự. Truy lần theo con trỏ (pointer chasing) khó hơn vì địa chỉ tiếp theo phụ thuộc vào dữ liệu vừa được đọc.

Nạp trước không miễn phí. Nếu quá mạnh, nó có thể chiếm băng thông (bandwidth), làm ô nhiễm bộ nhớ đệm (cache / 캐시) và đẩy dữ liệu nóng ra ngoài. Vì vậy độ chính xác và thời điểm nạp đều quan trọng: dự đoán đúng nhưng quá muộn không che được độ trễ; dự đoán đúng nhưng quá sớm có thể khiến dòng dữ liệu bị loại trước khi được dùng.

### Hardware-prefetch pathology

Một prefetch yêu cầu (request / 요청) chỉ có giá trị khi dòng dữ liệu đến đúng lúc, được dùng trước khi bị loại và không lấy mất tài nguyên có giá trị hơn. Vì vậy cần phân biệt:

```text
prefetch accuracy  = dòng được nạp có thực sự được dùng không
prefetch timeliness = dòng đến trước demand load đủ lâu không
prefetch pollution = dòng nạp sớm đẩy dòng hữu ích ra ngoài bao nhiêu
prefetch coverage   = bao nhiêu demand miss được che phủ
```

Các thất bại (failure / 실패) mẫu (pattern / 패턴) thường gặp:

- **Over-prefetch:** stream detector tiếp tục kéo dữ liệu dù bên tiêu thụ (consumer / 소비자) đã đổi phase, làm tăng bộ nhớ (memory / 메모리) traffic và hàng đợi (queue / 큐) occupancy.
- **bộ nhớ đệm (cache / 캐시) pollution:** dòng được dự đoán đúng nhưng reuse distance dài hơn bộ nhớ đệm (cache / 캐시) residency; nó chỉ chiếm way rồi đẩy out working set nóng.
- **Bandwidth theft:** prefetch dùng chung DRAM/interconnect bandwidth với demand yêu cầu (request / 요청). Khi bandwidth gần bão hòa, độ trễ (latency / 지연 시간) của demand có thể tăng dù prefetch accuracy không thấp.
- **MLP và hàng đợi (queue / 큐) pressure:** nhiều prefetch outstanding làm tăng memory-level parallelism đến mức yêu cầu (request / 요청) hàng đợi (queue / 큐), miss-status holding register hoặc controller bị đầy; demand tải (load / 로드) phải chờ lâu hơn.
- **Phase confusion:** một mẫu (pattern / 패턴) tuần tự trong phase A có thể trở thành random/strided mẫu (pattern / 패턴) ở phase B. Prefetcher cần học lại nhưng trong thời gian đó vẫn tạo yêu cầu (request / 요청) theo lịch sử (history / 이력) cũ.
- **Translation tương tác (interaction / 상호작용):** prefetch dữ liệu (data / 데이터) không tự giải quyết page walk, TLB miss hoặc NUMA placement. Nó có thể đưa dữ liệu đến một bộ nhớ đệm (cache / 캐시) nhưng demand vẫn bị giới hạn bởi address-translation hoặc remote-memory đường dẫn (path / 경로).

Do đó “prefetch đúng” không đồng nghĩa “prefetch có ích”. Một prefetcher có accuracy cao vẫn có thể làm thông lượng (throughput / 처리량) giảm nếu pollution, bandwidth theft hoặc hàng đợi (queue / 큐) pressure lớn hơn độ trễ (latency / 지연 시간) được che phủ.

### Chẩn đoán pathology bằng đối chứng

Không suy ra pathology từ `cache-misses` đơn lẻ. Hãy so sánh cùng tải công việc (workload / 워크로드) và hardware cohort theo các biến thể: prefetch mặc định, chính sách (policy / 정책) giảm aggressiveness nếu có, software prefetch hoặc baseline không prefetch. Timeline cần đặt cạnh nhau:

```text
demand latency / LLC miss latency
→ prefetch requests và useful-prefetch ratio
→ memory bandwidth / read-write queue occupancy
→ LLC eviction / working-set hit rate
→ MLP, stall cycles và effective frequency
```

Nếu tắt hoặc giảm prefetch làm LLC miss count tăng nhưng demand độ trễ (latency / 지연 시간) và useful thông lượng (throughput / 처리량) giảm ít hơn, prefetch trước đó có thể đang tạo pollution hoặc tranh bandwidth. Nếu tải công việc (workload / 워크로드) chỉ nhanh hơn ở cold phase rồi mất lợi thế khi warm, hãy kiểm tra timeliness và phase thay đổi (change / 변경) thay vì chỉ nhìn hit tỷ lệ (rate / 비율). Với NUMA, phải tách cục bộ (local / 로컬)/remote traffic; cùng một miss tỷ lệ (rate / 비율) nhưng remote DRAM độ trễ (latency / 지연 시간) có thể làm tail khác hẳn.

Prefetch pathology cũng nối với power/thermal: yêu cầu (request / 요청) thừa làm bộ nhớ (memory / 메모리) fabric và DRAM hoạt động nhiều hơn, tăng năng lượng (energy / 에너지) per useful kết quả (outcome / 결과) và có thể đẩy controller vào operating điểm (point / 지점) thấp hơn. Vì vậy bộ nhớ đệm (cache / 캐시) tuning cần đánh giá cả useful công việc (work / 작업), bandwidth và sustained hiệu năng (performance / 성능), không chỉ peak IPC.

Prefetch pathology phải được đo bằng demand latency, useful coverage, pollution và bandwidth, không chỉ bằng cache-miss count. Data layout có thể đổi locality và reuse; sau đó cần tách cache coherence khỏi language memory consistency.

## Bố trí dữ liệu trong phần mềm

Cấu trúc “mảng các cấu trúc” (Array of Structures — AoS) thuận tiện cho mô hình đối tượng nhưng có thể tải nhiều trường không cần dùng. “Cấu trúc các mảng” (structure of Arrays — SoA) gom các trường cùng loại thành vùng liên tục, thường phù hợp hơn với xử lý véc-tơ (vectorization) và tính cục bộ của bộ nhớ đệm (cache / 캐시). Đây là một lý do thiết kế hướng dữ liệu (data-oriented design) có thể hiệu quả hơn bố trí hướng đối tượng trên đường chạy nóng (hot path), dù thuật toán cấp cao không thay đổi.

Kỹ thuật chia khối (blocking/tiling) trong nhân ma trận cũng dựa trên cùng lập luận: chia bài toán để tập dữ liệu của mỗi khối vừa với bộ nhớ đệm (cache / 캐시), nhờ đó một dòng dữ liệu được tái sử dụng nhiều lần trước khi bị thay thế.

Data layout quyết định dòng nào được tái sử dụng và dòng nào tranh chấp một set, nhưng nó không quy định thứ tự quan sát giữa các core. Phần kế tiếp tách coherence khỏi consistency rồi đưa cả hai vào diagnosis thực tế.

## Nhất quán bộ nhớ đệm (cache / 캐시) không đồng nghĩa với mô hình nhất quán bộ nhớ

Nhất quán bộ nhớ đệm (cache / 캐시) (cache coherence) trả lời cách các lõi thống nhất giá trị của cùng một dòng bộ nhớ đệm (cache / 캐시). Mô hình nhất quán bộ nhớ (memory consistency) trả lời thứ tự mà nhiều thao tác bộ nhớ có thể được phần mềm quan sát. Một hệ thống có coherence vẫn cần mô hình bộ nhớ và hàng rào bộ nhớ (memory fence) phù hợp.

Xem thêm: [Memory consistency, cache coherence và ordering](./00_memory_consistency_cache_coherence_and_ordering.md).

Coherence mô tả việc các cache giữ cùng một location hợp lệ; consistency mô tả ordering mà software được phép suy luận. Khi đọc counter trong hệ thống thật, phải giữ hai contract đó riêng trước khi kết luận bottleneck.

## Suy luận trong hệ thống thực tế

Khi một dịch vụ có mức sử dụng CPU cao nhưng số lệnh hoàn thành mỗi chu kỳ (IPC) thấp và tỷ lệ trượt LLC cao, tăng thêm luồng (thread) có thể làm tình hình tệ hơn vì các tập dữ liệu làm việc cạnh tranh bộ nhớ đệm (cache / 캐시). Khi nhiều luồng cập nhật các bộ đếm nằm sát nhau, chia sẻ giả có thể tạo lưu lượng coherence lớn dù lô-gic (logic / 논리) chương trình không khóa lẫn nhau.

Các bộ đếm hiệu năng (performance counter) như `cache-misses`, `LLC-loads` và `stalled-cycles` chỉ có ý nghĩa khi đặt cạnh kiểu truy cập và kích thước tập dữ liệu làm việc. Không nên kết luận “bộ nhớ đệm (cache / 캐시) là nút thắt cổ chai (bottleneck)” chỉ từ một chỉ số đơn lẻ.

Khi điều tra prefetch, hãy ghi rõ counter là demand hay prefetch traffic nếu phần cứng cung cấp distinction đó. Nếu không có distinction, dùng controlled comparison và hardware sự kiện (event / 이벤트) correlation để tránh gán toàn bộ bộ nhớ (memory / 메모리) traffic cho demand đường dẫn (path / 경로). Kết luận tốt phải chỉ ra được pathology nào chiếm ưu thế: coverage thấp, timeliness kém, pollution, bandwidth theft hay hàng đợi (queue / 큐) pressure.

Diagnosis tốt nối mechanism với bằng chứng: cache policy với reuse distance, prefetch với useful coverage, layout với locality, và coherence với traffic. Mô hình tư duy dưới đây nén các quan hệ đó thành một nguyên tắc tối ưu.

## Mô hình tư duy

> Phân cấp bộ nhớ đệm (cache / 캐시) là một hệ thống dự đoán khả năng tái sử dụng dữ liệu dưới giới hạn dung lượng và băng thông. Tối ưu bộ nhớ đệm (cache / 캐시) không phải làm mọi thứ “nằm trong bộ nhớ đệm (cache / 캐시)”, mà là tổ chức tính toán để dữ liệu có giá trị được tái sử dụng đủ sớm, giảm xung đột và tránh tạo lưu lượng không cần thiết.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
