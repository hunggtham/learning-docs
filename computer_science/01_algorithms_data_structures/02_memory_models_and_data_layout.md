# Memory model, locality và data layout

Data structure không tồn tại trong khoảng không trừu tượng. Nó cuối cùng phải chiếm bytes trong memory. Cùng complexity class, hai representations có thể khác performance rất lớn vì cách CPU cache, allocator và pointer chasing hoạt động.

## Random-access memory model và address

Memory có thể hình dung như một dãy bytes, mỗi byte có address. CPU load/store dữ liệu qua addresses. “Random access” trong model lý tưởng nghĩa access address bất kỳ có cost gần constant, nhưng hardware thật có hierarchy: register → cache → DRAM → storage, với latency khác nhau nhiều bậc.

Một array của 1 triệu integers contiguous tạo pattern địa chỉ đều. CPU prefetcher và cache line có thể lấy nhiều neighboring values cùng lúc. Linked list đặt nodes rải rác, mỗi pointer dereference có thể dẫn tới cache miss.

## Spatial và temporal locality

Spatial locality (공간 지역성 / tính cục bộ không gian): nếu vừa access address x, có khả năng sắp access addresses gần x. Temporal locality (시간 지역성): dữ liệu vừa dùng có khả năng được dùng lại sớm.

Cache hoạt động tốt vì programs thường có locality. Array iteration có spatial locality. Loop dùng đi dùng lại small lookup table có temporal locality.

Algorithm design và data layout có thể tăng locality mà không đổi Big O.

## Contiguous representation và linked representation

Contiguous structures như array cho `O(1)` indexing vì address element `i` có thể tính từ base + i×element_size. Đổi lại, insert giữa array cần shift và growth có thể realloc/copy.

Linked structures dùng pointers để nối nodes. Insert/delete tại known node có thể `O(1)`, nhưng tìm node vẫn cần traversal. Mỗi node còn tốn pointer overhead và allocator metadata, đồng thời locality kém.

Vì vậy câu “linked list insert nhanh hơn array” thiếu context. Nếu workload chủ yếu scan, dynamic array thường tốt hơn đáng kể.

## Array of Structures và Structure of Arrays

Giả sử có points `{x,y,z,type}`. Array of Structures (AoS) lưu toàn bộ record liên tiếp. Structure of Arrays (SoA) lưu riêng arrays x[], y[], z[], type[].

Nếu computation cần tất cả fields của từng point, AoS tự nhiên. Nếu vectorized loop chỉ cần x và y cho hàng triệu points, SoA giảm bytes không cần thiết vào cache và phù hợp SIMD hơn.

Data-oriented design bắt đầu từ access pattern chứ không chỉ object modeling.

## Alignment, padding và object overhead

Hardware thích aligned accesses. Compiler/runtime có thể chèn padding trong structs/objects. Managed runtime còn có object header, class pointer, GC metadata hoặc compressed references. Một object chứa hai ints có thể tốn nhiều hơn 8 bytes.

Hàng triệu tiny objects vì vậy có memory footprint và GC pressure lớn hơn intuition ở source code.

Xem representation chi tiết tại [Numbers & machine representation](../00_computation_information/02_numbers_and_machine_representation.md).

## Stack, heap và lifetime như một mental model

Ở runtime, call stack thường giữ activation records: return address, local data, saved registers. Heap phục vụ allocations có lifetime linh hoạt. Nhưng language semantics không nên đồng nhất tuyệt đối với physical stack/heap: compiler có thể scalar-replace object, allocate closure differently hoặc escape-analyze.

Điểm quan trọng là **lifetime và ownership** quyết định khi memory có thể reclaim. Manual memory management yêu cầu programmer; GC tracing tìm objects reachable; reference counting dựa counts nhưng khó với cycles.

Phần language-level memory được giải thích ở [Types, values, references and memory](../04_programming_languages/01_types_values_references_and_memory.md).

## Pointer chasing và indirection

Abstraction thường thêm indirection: pointer → object → child pointer → value. Mỗi indirection có thể là dependent memory load; CPU khó song song hóa nếu address tiếp theo chỉ biết sau load trước. Tree có theoretical `O(log n)` nhưng B-tree thường outperform binary tree trên storage/cache vì mỗi node chứa nhiều keys, giảm depth và tăng locality.

Đây chính là lý do database indexes thích B/B+ trees.

## Compactness và encoded representations

Bitsets pack booleans thành bits thay vì bytes/objects. Integer compression, dictionary encoding và columnar storage giảm footprint; footprint nhỏ có thể làm data fit cache và tăng speed ngoài lợi ích storage.

Tuy nhiên compression cần CPU decode. Đây là time-space-bandwidth trade-off.

## Mutability và sharing

Immutable persistent data structures có thể share structure giữa versions thay vì copy toàn bộ. Điều này giúp concurrency reasoning nhưng thêm indirection/allocation. Copy-on-write cũng delay duplication cho tới khi mutate.

Data layout vì vậy chịu ảnh hưởng không chỉ bởi performance mà cả semantic requirements như immutability, snapshot và isolation.

## Mental Model

> Data structure có hai mặt: **abstract operations** và **physical representation/access pattern**. Big O mô tả mặt thứ nhất; cache line, pointer, allocation và layout quyết định rất nhiều ở mặt thứ hai.

## Common Misconceptions

**“RAM access luôn O(1), vậy locality không quan trọng.”** `O(1)` là model asymptotic; latency L1 và DRAM khác nhau lớn.

**“Object nhỏ thì memory nhỏ.”** Header, alignment, references và allocator overhead có thể lớn hơn fields.

**“Linked list luôn phù hợp insert/delete nhiều.”** Chỉ khi đã có vị trí/node phù hợp và locality/traversal không chi phối.

## Kết nối

Chapter này là cầu nối từ algorithms sang [memory hierarchy/cache](../02_computer_architecture/02_memory_hierarchy_and_cache.md), đồng thời giải thích vì sao [linear structures](./03_linear_data_structures.md), [hash tables](./04_hashing_and_hash_tables.md), [trees](./05_trees_heaps_and_search_structures.md) có performance thực tế khác với notation đơn giản.
