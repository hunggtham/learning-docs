# Memory hierarchy, cache và locality

CPU có thể thực hiện arithmetic trong vài cycles, nhưng DRAM access có thể tốn hàng chục tới hàng trăm cycles. Storage và network còn chậm hơn nhiều. Nếu mỗi operation phải chờ tầng chậm nhất, CPU sẽ phần lớn idle. Memory hierarchy giải quyết bằng nhiều tầng capacity/latency/cost khác nhau.

## Không có memory hoàn hảo

Ta muốn memory vừa rất nhanh, rất lớn, rẻ, tiết kiệm điện và non-volatile. Physics/economics không cho tất cả cùng lúc. Vì vậy systems dùng registers → L1/L2/L3 cache → DRAM → SSD/HDD → remote storage.

Mỗi tầng gần CPU thường nhỏ hơn nhưng nhanh hơn. Cơ chế hiệu quả vì workloads có temporal và spatial locality.

## Cache line

CPU cache thường chuyển dữ liệu theo **cache line**, ví dụ 64 bytes trên nhiều systems, không phải từng variable. Khi đọc một int 4 bytes, cả neighboring bytes có thể vào cache. Sequential array scan tận dụng line; random pointer chasing có thể dùng chỉ vài bytes mỗi line.

Đây là lý do Big O giống nhau nhưng actual speed khác.

## Tag, set và associativity

Cache cần biết memory block nào đang nằm ở slot nào. Address được tách thành offset, set index và tag. Direct-mapped cache mỗi block có một place; set-associative cho vài candidate ways; fully associative cho bất kỳ slot nhưng hardware lookup đắt hơn.

Conflict misses xảy ra khi hot blocks map cùng set dù cache tổng còn space. Replacement policy xấp xỉ LRU hoặc variants quyết định victim.

## Hit và miss

Cache hit phục vụ ở tầng nhanh. Miss cần fetch từ lower level. Average Memory Access Time có mental model:

\[
AMAT = hit\ time + miss\ rate \times miss\ penalty
\]

Nested cache levels làm formula chi tiết hơn. Một miss rate nhỏ vẫn đáng kể nếu penalty lớn.

## Write policies

Write-through gửi write xuống lower level ngay, đơn giản consistency nhưng tăng traffic. Write-back chỉ cập nhật cache line và đánh dirty, flush khi evict, giảm bandwidth nhưng phức tạp hơn. Write-allocate/no-write-allocate quyết định miss khi store có kéo line vào cache không.

## Cache coherence

Multicore CPUs có private caches. Nếu core A ghi x còn core B giữ old x, system cần coherence protocol để quản lý copies. MESI-like protocols theo dõi states và invalidate/share lines.

Coherence không tự giải quyết mọi concurrency semantics. Language/ISA memory model còn quyết định ordering và visibility; synchronization primitives tạo happens-before relationships.

## False sharing

Hai threads cập nhật hai variables khác nhau nhưng cùng cache line có thể gây ping-pong invalidations. Logically không share data nhưng physically share cache line — false sharing. Padding/alignment hoặc partition data có thể giảm.

Đây là ví dụ abstraction leak từ variable-level program sang cache-line-level hardware.

## TLB và address translation cache

Virtual addresses phải translate qua page tables. Translation Lookaside Buffer (TLB) cache recent virtual→physical mappings. TLB miss cần page-table walk, nên large working sets hoặc random accesses có thêm cost ngoài data cache.

Huge pages giảm number of TLB entries cần nhưng tăng allocation/internal-fragmentation trade-offs.

## Prefetching

Hardware/software prefetch đoán dữ liệu sắp dùng và kéo sớm. Sequential patterns dễ đoán; linked structures khó vì next address phụ thuộc load hiện tại. Prefetch sai lãng phí bandwidth/cache capacity.

## Mental Model

> Performance memory phụ thuộc **working set + access pattern**, không chỉ data size. Hãy hỏi dữ liệu có fit tầng nào, mỗi access dùng bao nhiêu của cache line, có reuse không, và cores có tranh cùng lines không.

## Common Misconceptions

**“RAM là một tốc độ duy nhất.”** Cache/TLB/NUMA khiến memory access cost phụ thuộc location và history.

**“Cache chỉ là software cache như Redis.”** CPU cache là hardware-managed tầng memory; cùng principle locality nhưng mechanism khác.

**“Coherence làm concurrent code thread-safe.”** Coherence giữ copies coherent theo protocol; race-free semantics cần synchronization/memory ordering.

## Kết nối

[Data layout/locality](../01_algorithms_data_structures/02_memory_models_and_data_layout.md) là software side; [virtual memory](../03_operating_systems/03_virtual_memory_and_address_spaces.md) thêm translation; [concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) giải thích memory ordering; [performance](../08_software_systems/02_performance_capacity_and_scalability.md) mở rộng tới whole-system bottlenecks.
