# Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**. Route đi từ latency/capacity trade-off → cache line và locality → mapping, replacement/coherence → virtual memory và performance, để hierarchy được đọc bằng access pattern chứ không chỉ tên tầng.

CPU có thể thực hiện arithmetic trong vài cycles, nhưng DRAM truy cập (access / 접근) có thể tốn hàng chục tới hàng trăm cycles. lưu trữ (storage / 저장소) và mạng (network / 네트워크) còn chậm hơn nhiều. Nếu mỗi thao tác (operation / 연산) phải chờ tầng chậm nhất, CPU sẽ phần lớn idle. bộ nhớ (memory / 메모리) hierarchy giải quyết bằng nhiều tầng sức chứa (capacity / 용량)/độ trễ (latency / 지연 시간)/chi phí (cost / 비용) khác nhau.

## Không có bộ nhớ (memory / 메모리) hoàn hảo

Ta muốn bộ nhớ (memory / 메모리) vừa rất nhanh, rất lớn, rẻ, tiết kiệm điện và non-volatile. Physics/economics không cho tất cả cùng lúc. Vì vậy các hệ thống (systems / 시스템들) dùng registers → L1/L2/L3 bộ nhớ đệm (cache / 캐시) → DRAM → SSD/HDD → remote lưu trữ (storage / 저장소).

Mỗi tầng gần CPU thường nhỏ hơn nhưng nhanh hơn. Cơ chế hiệu quả vì workloads có temporal và spatial locality.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **Bộ nhớ đệm (cache / 캐시) line** tiếp nhận điểm tựa từ **Không có bộ nhớ (memory / 메모리) hoàn hảo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tag, set và associativity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ đệm (cache / 캐시) line

CPU bộ nhớ đệm (cache / 캐시) thường chuyển dữ liệu theo **bộ nhớ đệm (cache / 캐시) line**, ví dụ 64 bytes trên nhiều các hệ thống (systems / 시스템들), không phải từng variable. Khi đọc một int 4 bytes, cả neighboring bytes có thể vào bộ nhớ đệm (cache / 캐시). Sequential array scan tận dụng line; random pointer chasing có thể dùng chỉ vài bytes mỗi line.

Đây là lý do Big O giống nhau nhưng actual speed khác.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **Tag, set và associativity** tiếp nhận điểm tựa từ **Bộ nhớ đệm (cache / 캐시) line** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hit và miss** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tag, set và associativity

Bộ nhớ đệm (cache / 캐시) cần biết bộ nhớ (memory / 메모리) khối (block / 블록) nào đang nằm ở slot nào. Address được tách thành offset, set chỉ mục (index / 인덱스) và tag. Direct-mapped bộ nhớ đệm (cache / 캐시) mỗi khối (block / 블록) có một place; set-associative cho vài candidate ways; fully associative cho bất kỳ slot nhưng hardware lookup đắt hơn.

Xung đột (conflict / 충돌) misses xảy ra khi hot blocks map cùng set dù bộ nhớ đệm (cache / 캐시) tổng còn không gian (space / 공간). Replacement chính sách (policy / 정책) xấp xỉ LRU hoặc variants quyết định victim.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **Hit và miss** tiếp nhận điểm tựa từ **Tag, set và associativity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ghi (write / 쓰기) policies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hit và miss

Bộ nhớ đệm (cache / 캐시) hit phục vụ ở tầng nhanh. Miss cần fetch từ lower mức (level / 수준). Average bộ nhớ (memory / 메모리) truy cập (access / 접근) thời gian (time / 시간) có mô hình tư duy (mental model / 사고 모델):

\[
AMAT = hit\ thời gian (time / 시간) + miss\ tỷ lệ (rate / 비율) \times miss\ penalty
\]

Nested bộ nhớ đệm (cache / 캐시) levels làm formula chi tiết hơn. Một miss tỷ lệ (rate / 비율) nhỏ vẫn đáng kể nếu penalty lớn.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **Ghi (write / 쓰기) policies** tiếp nhận điểm tựa từ **Hit và miss** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ đệm (cache / 캐시) coherence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ghi (write / 쓰기) policies

Write-through gửi ghi (write / 쓰기) xuống lower mức (level / 수준) ngay, đơn giản consistency nhưng tăng traffic. Write-back chỉ cập nhật bộ nhớ đệm (cache / 캐시) line và đánh dirty, flush khi evict, giảm bandwidth nhưng phức tạp hơn. Write-allocate/no-write-allocate quyết định miss khi store có kéo line vào bộ nhớ đệm (cache / 캐시) không.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **Bộ nhớ đệm (cache / 캐시) coherence** tiếp nhận điểm tựa từ **Ghi (write / 쓰기) policies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **False sharing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ đệm (cache / 캐시) coherence

Multicore CPUs có private caches. Nếu cốt lõi (core / 핵심) A ghi x còn cốt lõi (core / 핵심) B giữ old x, hệ thống (system / 시스템) cần coherence giao thức (protocol / 프로토콜) để quản lý copies. MESI-like protocols theo dõi states và invalidate/share lines.

Coherence không tự giải quyết mọi tính đồng thời (concurrency / 동시성) ngữ nghĩa (semantics / 의미론). ngôn ngữ (language / 언어)/ISA bộ nhớ (memory / 메모리) mô hình (model / 모델) còn quyết định thứ tự (ordering / 순서) và visibility; synchronization primitives tạo happens-before relationships.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **False sharing** tiếp nhận điểm tựa từ **Bộ nhớ đệm (cache / 캐시) coherence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TLB và address translation bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## False sharing

Hai threads cập nhật hai variables khác nhau nhưng cùng bộ nhớ đệm (cache / 캐시) line có thể gây ping-pong invalidations. Logically không share dữ liệu (data / 데이터) nhưng physically share bộ nhớ đệm (cache / 캐시) line — false sharing. Padding/alignment hoặc partition dữ liệu (data / 데이터) có thể giảm.

Đây là ví dụ lớp trừu tượng (abstraction / 추상화) leak từ variable-level program sang cache-line-level hardware.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **TLB và address translation bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **False sharing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prefetching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TLB và address translation bộ nhớ đệm (cache / 캐시)

Virtual addresses phải translate qua page tables. Translation Lookaside Buffer (TLB) bộ nhớ đệm (cache / 캐시) recent virtual→vật lý (physical / 물리적) mappings. TLB miss cần page-table walk, nên large working sets hoặc random accesses có thêm chi phí (cost / 비용) ngoài dữ liệu (data / 데이터) bộ nhớ đệm (cache / 캐시).

Huge pages giảm number of TLB entries cần nhưng tăng allocation/internal-fragmentation trade-offs.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **Prefetching** tiếp nhận điểm tựa từ **TLB và address translation bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prefetching

Hardware/software prefetch đoán dữ liệu sắp dùng và kéo sớm. Sequential patterns dễ đoán; linked structures khó vì next address phụ thuộc tải (load / 로드) hiện tại. Prefetch sai lãng phí bandwidth/bộ nhớ đệm (cache / 캐시) sức chứa (capacity / 용량).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Prefetching** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> hiệu năng (performance / 성능) bộ nhớ (memory / 메모리) phụ thuộc **working set + truy cập (access / 접근) mẫu (pattern / 패턴)**, không chỉ dữ liệu (data / 데이터) kích thước (size / 크기). Hãy hỏi dữ liệu có fit tầng nào, mỗi truy cập (access / 접근) dùng bao nhiêu của bộ nhớ đệm (cache / 캐시) line, có reuse không, và cores có tranh cùng lines không.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“RAM là một tốc độ duy nhất.”** bộ nhớ đệm (cache / 캐시)/TLB/NUMA khiến bộ nhớ (memory / 메모리) truy cập (access / 접근) chi phí (cost / 비용) phụ thuộc location và lịch sử (history / 이력).

**“bộ nhớ đệm (cache / 캐시) chỉ là software bộ nhớ đệm (cache / 캐시) như Redis.”** CPU bộ nhớ đệm (cache / 캐시) là hardware-managed tầng bộ nhớ (memory / 메모리); cùng principle locality nhưng cơ chế (mechanism / 메커니즘) khác.

**“Coherence làm concurrent mã (code / 코드) thread-safe.”** Coherence giữ copies coherent theo giao thức (protocol / 프로토콜); race-free ngữ nghĩa (semantics / 의미론) cần synchronization/bộ nhớ (memory / 메모리) thứ tự (ordering / 순서).

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) hierarchy, bộ nhớ đệm (cache / 캐시) và locality**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Data layout/locality](../01_algorithms_data_structures/02_memory_models_and_data_layout.md) là software side; [virtual memory](../03_operating_systems/03_virtual_memory_and_address_spaces.md) thêm translation; [concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) giải thích bộ nhớ (memory / 메모리) thứ tự (ordering / 순서); [performance](../08_software_systems/02_performance_capacity_and_scalability.md) mở rộng tới whole-system bottlenecks.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
