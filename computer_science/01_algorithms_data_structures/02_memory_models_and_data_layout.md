# Bộ nhớ (memory / 메모리) mô hình (model / 모델), locality và dữ liệu (data / 데이터) bố cục (layout / 레이아웃)

> **Mạch đọc:** Đặt **bộ nhớ (memory / 메모리) mô hình (model / 모델), locality và dữ liệu (data / 데이터) bố cục (layout / 레이아웃)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Random-access bộ nhớ (memory / 메모리) mô hình (model / 모델) và address** sang **Spatial và temporal locality**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Cấu trúc dữ liệu (data structure / 자료구조) không tồn tại trong khoảng không trừu tượng. Nó cuối cùng phải chiếm bytes trong bộ nhớ (memory / 메모리). Cùng độ phức tạp (complexity / 복잡도) lớp (class / 클래스), hai representations có thể khác hiệu năng (performance / 성능) rất lớn vì cách CPU bộ nhớ đệm (cache / 캐시), allocator và pointer chasing hoạt động.

## Random-access bộ nhớ (memory / 메모리) mô hình (model / 모델) và address

Bộ nhớ (memory / 메모리) có thể hình dung như một dãy bytes, mỗi byte có address. CPU tải (load / 로드)/store dữ liệu qua addresses. “Random truy cập (access / 접근)” trong mô hình (model / 모델) lý tưởng nghĩa truy cập (access / 접근) address bất kỳ có chi phí (cost / 비용) gần constant, nhưng hardware thật có hierarchy: register → bộ nhớ đệm (cache / 캐시) → DRAM → lưu trữ (storage / 저장소), với độ trễ (latency / 지연 시간) khác nhau nhiều bậc.

Một array của 1 triệu integers contiguous tạo mẫu (pattern / 패턴) địa chỉ đều. CPU prefetcher và bộ nhớ đệm (cache / 캐시) line có thể lấy nhiều neighboring values cùng lúc. Linked danh sách (list / 목록) đặt nodes rải rác, mỗi pointer dereference có thể dẫn tới trượt bộ nhớ đệm (cache miss / 캐시 미스).


> **Chuyển mạch:** Từ **Random-access bộ nhớ (memory / 메모리) mô hình (model / 모델) và address**, ta sang **Spatial và temporal locality** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Spatial và temporal locality

Spatial locality (공간 지역성 / tính cục bộ không gian): nếu vừa truy cập (access / 접근) address x, có khả năng sắp truy cập (access / 접근) addresses gần x. Temporal locality (시간 지역성): dữ liệu vừa dùng có khả năng được dùng lại sớm.

Bộ nhớ đệm (cache / 캐시) hoạt động tốt vì programs thường có locality. Array iteration có spatial locality. vòng lặp (loop / 루프) dùng đi dùng lại small lookup bảng (table / 테이블) có temporal locality.

Thuật toán (algorithm / 알고리즘) thiết kế (design / 설계) và dữ liệu (data / 데이터) bố cục (layout / 레이아웃) có thể tăng locality mà không đổi Big O.


> **Chuyển mạch:** Từ **Spatial và temporal locality**, ta sang **Contiguous biểu diễn (representation / 표현) và linked biểu diễn (representation / 표현)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Contiguous biểu diễn (representation / 표현) và linked biểu diễn (representation / 표현)

Contiguous structures như array cho `O(1)` indexing vì address element `i` có thể tính từ cơ sở (base / 기반) + i×element_size. Đổi lại, insert giữa array cần shift và growth có thể realloc/bản sao (copy / 복사).

Linked structures dùng pointers để nối nodes. Insert/delete tại known nút (node / 노드) có thể `O(1)`, nhưng tìm nút (node / 노드) vẫn cần traversal. Mỗi nút (node / 노드) còn tốn pointer overhead và allocator siêu dữ liệu (metadata / 메타데이터), đồng thời locality kém.

Vì vậy câu “linked danh sách (list / 목록) insert nhanh hơn array” thiếu ngữ cảnh (context / 맥락). Nếu tải công việc (workload / 워크로드) chủ yếu scan, động (dynamic / 동적) array thường tốt hơn đáng kể.


> **Chuyển mạch:** Từ **Contiguous biểu diễn (representation / 표현) và linked biểu diễn (representation / 표현)**, ta sang **Array of Structures và cấu trúc (structure / 구조) of Arrays** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Array of Structures và cấu trúc (structure / 구조) of Arrays

Giả sử có points `{x,y,z,type}`. Array of Structures (AoS) lưu toàn bộ bản ghi (record / 레코드) liên tiếp. cấu trúc (structure / 구조) of Arrays (SoA) lưu riêng arrays x[], y[], z[], kiểu (type / 타입)[].

Nếu computation cần tất cả fields của từng điểm (point / 지점), AoS tự nhiên. Nếu vectorized vòng lặp (loop / 루프) chỉ cần x và y cho hàng triệu points, SoA giảm bytes không cần thiết vào bộ nhớ đệm (cache / 캐시) và phù hợp SIMD hơn.

Data-oriented thiết kế (design / 설계) bắt đầu từ truy cập (access / 접근) mẫu (pattern / 패턴) chứ không chỉ đối tượng (object / 객체) modeling.


> **Chuyển mạch:** Từ **Array of Structures và cấu trúc (structure / 구조) of Arrays**, ta sang **Alignment, padding và đối tượng (object / 객체) overhead** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Alignment, padding và đối tượng (object / 객체) overhead

Hardware thích aligned accesses. trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) có thể chèn padding trong structs/objects. Managed thời gian chạy (runtime / 런타임) còn có đối tượng (object / 객체) header, lớp (class / 클래스) pointer, GC siêu dữ liệu (metadata / 메타데이터) hoặc compressed references. Một đối tượng (object / 객체) chứa hai ints có thể tốn nhiều hơn 8 bytes.

Hàng triệu tiny objects vì vậy có bộ nhớ (memory / 메모리) footprint và GC pressure lớn hơn intuition ở mã nguồn (source code / 소스 코드).

Xem biểu diễn (representation / 표현) chi tiết tại [Numbers & machine representation](../00_computation_information/02_numbers_and_machine_representation.md).


> **Chuyển mạch:** Từ **Alignment, padding và đối tượng (object / 객체) overhead**, ta sang **ngăn xếp (stack / 스택), vùng nhớ động (heap / 힙) và thời gian tồn tại (lifetime / 수명) như một mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ngăn xếp (stack / 스택), vùng nhớ động (heap / 힙) và thời gian tồn tại (lifetime / 수명) như một mô hình tư duy (mental model / 사고 모델)

Ở thời gian chạy (runtime / 런타임), ngăn xếp lời gọi (call stack / 호출 스택) thường giữ activation records: return address, cục bộ (local / 로컬) dữ liệu (data / 데이터), saved registers. vùng nhớ động (heap / 힙) phục vụ allocations có thời gian tồn tại (lifetime / 수명) linh hoạt. Nhưng ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) không nên đồng nhất tuyệt đối với vật lý (physical / 물리적) ngăn xếp (stack / 스택)/vùng nhớ động (heap / 힙): trình biên dịch (compiler / 컴파일러) có thể scalar-replace đối tượng (object / 객체), allocate closure differently hoặc escape-analyze.

Điểm quan trọng là **thời gian tồn tại (lifetime / 수명) và quyền sở hữu (ownership / 소유권)** quyết định khi bộ nhớ (memory / 메모리) có thể reclaim. Manual bộ nhớ (memory / 메모리) management yêu cầu programmer; GC tracing tìm objects reachable; tham chiếu (reference / 참조) counting dựa counts nhưng khó với cycles.

Phần language-level bộ nhớ (memory / 메모리) được giải thích ở [Types, values, references and memory](../04_programming_languages/01_types_values_references_and_memory.md).


> **Chuyển mạch:** Từ **ngăn xếp (stack / 스택), vùng nhớ động (heap / 힙) và thời gian tồn tại (lifetime / 수명) như một mô hình tư duy (mental model / 사고 모델)**, ta sang **Pointer chasing và indirection** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Pointer chasing và indirection

Lớp trừu tượng (abstraction / 추상화) thường thêm indirection: pointer → đối tượng (object / 객체) → child pointer → giá trị (value / 값). Mỗi indirection có thể là dependent bộ nhớ (memory / 메모리) tải (load / 로드); CPU khó song song hóa nếu address tiếp theo chỉ biết sau tải (load / 로드) trước. cây (tree / 트리) có theoretical `O(log n)` nhưng B-tree thường outperform nhị phân (binary / 이진) cây (tree / 트리) trên lưu trữ (storage / 저장소)/bộ nhớ đệm (cache / 캐시) vì mỗi nút (node / 노드) chứa nhiều keys, giảm độ sâu (depth / 깊이) và tăng locality.

Đây chính là lý do cơ sở dữ liệu (database / 데이터베이스) indexes thích B/B+ trees.


> **Chuyển mạch:** Từ **Pointer chasing và indirection**, ta sang **Compactness và encoded representations** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Compactness và encoded representations

Bitsets pack booleans thành bits thay vì bytes/objects. Integer compression, dictionary encoding và columnar lưu trữ (storage / 저장소) giảm footprint; footprint nhỏ có thể làm dữ liệu (data / 데이터) fit bộ nhớ đệm (cache / 캐시) và tăng speed ngoài lợi ích lưu trữ (storage / 저장소).

Tuy nhiên compression cần CPU decode. Đây là time-space-bandwidth sự đánh đổi (trade-off / 트레이드오프).


> **Chuyển mạch:** Từ **Compactness và encoded representations**, ta sang **Mutability và sharing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mutability và sharing

Immutable persistent dữ liệu (data / 데이터) structures có thể share cấu trúc (structure / 구조) giữa versions thay vì bản sao (copy / 복사) toàn bộ. Điều này giúp tính đồng thời (concurrency / 동시성) lập luận (reasoning / 추론) nhưng thêm indirection/allocation. sao chép khi ghi (copy-on-write / 쓰기 시 복사) cũng delay duplication cho tới khi mutate.

Dữ liệu (data / 데이터) bố cục (layout / 레이아웃) vì vậy chịu ảnh hưởng không chỉ bởi hiệu năng (performance / 성능) mà cả ngữ nghĩa (semantic / 의미적) requirements như immutability, snapshot và isolation.


> **Chuyển mạch:** Từ **Mutability và sharing**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> cấu trúc dữ liệu (data structure / 자료구조) có hai mặt: **abstract operations** và **vật lý (physical / 물리적) biểu diễn (representation / 표현)/truy cập (access / 접근) mẫu (pattern / 패턴)**. Big O mô tả mặt thứ nhất; bộ nhớ đệm (cache / 캐시) line, pointer, allocation và bố cục (layout / 레이아웃) quyết định rất nhiều ở mặt thứ hai.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“RAM truy cập (access / 접근) luôn O(1), vậy locality không quan trọng.”** `O(1)` là mô hình (model / 모델) asymptotic; độ trễ (latency / 지연 시간) L1 và DRAM khác nhau lớn.

**“đối tượng (object / 객체) nhỏ thì bộ nhớ (memory / 메모리) nhỏ.”** Header, alignment, references và allocator overhead có thể lớn hơn fields.

**“Linked danh sách (list / 목록) luôn phù hợp insert/delete nhiều.”** Chỉ khi đã có vị trí/nút (node / 노드) phù hợp và locality/traversal không chi phối.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Chapter này là cầu nối từ algorithms sang [memory hierarchy/cache](../02_computer_architecture/02_memory_hierarchy_and_cache.md), đồng thời giải thích vì sao [linear structures](./03_linear_data_structures.md), [hash tables](./04_hashing_and_hash_tables.md), [trees](./05_trees_heaps_and_search_structures.md) có hiệu năng (performance / 성능) thực tế khác với notation đơn giản.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 algorithmic thinking and correctness](./00_algorithmic_thinking_and_correctness.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
