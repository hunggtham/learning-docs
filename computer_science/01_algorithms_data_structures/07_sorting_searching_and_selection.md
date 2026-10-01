# Sorting, searching và selection

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Sorting, searching và selection**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tuyến tính (linear / 선형) tìm kiếm (search / 검색) và tìm kiếm nhị phân (binary search / 이진 탐색)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Stable sort** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Sorting (정렬 / sắp xếp) tưởng như bài tập cơ bản nhưng nó phơi bày nhiều idea: comparison mô hình (model / 모델), divide-and-conquer, stability, locality, lower bound và sự đánh đổi (trade-off / 트레이드오프) giữa CPU với bộ nhớ (memory / 메모리). Searching và selection tiếp tục cùng câu hỏi: ta khai thác cấu trúc (structure / 구조) nào của dữ liệu (data / 데이터) để tránh công việc (work / 작업) không cần thiết?

## Tuyến tính (linear / 선형) tìm kiếm (search / 검색) và tìm kiếm nhị phân (binary search / 이진 탐색)

Nếu dữ liệu (data / 데이터) không có thứ tự (ordering / 순서)/chỉ mục (index / 인덱스), tìm key thường phải scan `O(n)`. tìm kiếm nhị phân (binary search / 이진 탐색) khai thác sorted thứ tự (order / 순서) để bỏ nửa tìm kiếm (search / 검색) interval mỗi comparison, `O(log n)`.

Tìm kiếm nhị phân (binary search / 이진 탐색) dễ viết sai vì ranh giới (boundary / 경계) ngữ nghĩa (semantics / 의미론). Half-open interval `[lo, hi)` thường giúp bất biến (invariant / 불변식) rõ: candidate positions luôn nằm trong interval, kích thước (size / 크기) là `hi-lo`. Midpoint nên tính tránh overflow ở languages fixed integer, ví dụ `lo + (hi-lo)/2`.

Tìm kiếm nhị phân (binary search / 이진 탐색) không chỉ tìm chính xác (exact / 정확한) key. Lower bound/upper bound tìm first position thỏa predicate monotonic. mẫu (pattern / 패턴) này áp dụng cho “minimum sức chứa (capacity / 용량) đủ”, “earliest thời gian (time / 시간) điều kiện (condition / 조건) true” nếu predicate chuyển false→true một lần.

> **Chuyển mạch:** Trong **Sorting, searching và selection**, **Stable sort** tiếp nhận điểm tựa từ **Tuyến tính (linear / 선형) tìm kiếm (search / 검색) và tìm kiếm nhị phân (binary search / 이진 탐색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Insertion sort** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stable sort

Stable sorting giữ relative thứ tự (order / 순서) của elements có equal key. Nếu đã sort employees theo name rồi stable sort theo department, within department name thứ tự (order / 순서) được giữ. Stability là ngữ nghĩa (semantic / 의미적) thuộc tính (property / 속성), không thể nhìn chỉ Big O.

> **Chuyển mạch:** Ở chặng này của **Sorting, searching và selection**, **Insertion sort** tiếp nhận điểm tựa từ **Stable sort** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Merge sort** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Insertion sort

Insertion sort xây sorted prefix, chèn từng element đúng vị trí. Worst O(n²), nhưng simple, in-place và nhanh với arrays nhỏ hoặc nearly sorted. Hybrid môi trường vận hành (production / 운영 환경) sorts thường dùng insertion sort cho tiny partitions vì constants/bộ nhớ đệm (cache / 캐시) tốt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sorting, searching và selection**, **Merge sort** tiếp nhận điểm tựa từ **Insertion sort** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quicksort** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Merge sort

Merge sort chia đôi, sort hai halves, merge. thời gian (time / 시간) Θ(n log n), dễ stable, nhưng array hiện thực (implementation / 구현) thường cần extra O(n) bộ nhớ (memory / 메모리). Linked danh sách (list / 목록) merge sort có thể tận dụng pointer rewiring.

Nó minh họa divide-and-conquer rõ và có predictable worst-case.

> **Chuyển mạch:** Trong **Sorting, searching và selection**, **Quicksort** tiếp nhận điểm tựa từ **Merge sort** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Heapsort** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quicksort

Quicksort partition quanh pivot rồi recursively sort partitions. Average/expected O(n log n), worst O(n²), nhưng in-place variants và locality tốt làm nó rất nhanh thực tế. Random pivot hoặc robust pivot chiến lược (strategy / 전략) giảm nguy cơ bad partitions.

Three-way partition hữu ích khi nhiều duplicates.

> **Chuyển mạch:** Ở chặng này của **Sorting, searching và selection**, **Heapsort** tiếp nhận điểm tựa từ **Quicksort** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Comparison lower bound** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Heapsort

Heapsort bản dựng (build / 빌드) vùng nhớ động (heap / 힙) O(n), rồi repeatedly extract max/min, total O(n log n), in-place và worst-case bounded, nhưng locality/constant thường kém quicksort. Nó cho thấy theoretical guarantees không quyết định toàn bộ kỹ thuật (engineering / 엔지니어링) choice.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sorting, searching và selection**, **Comparison lower bound** tiếp nhận điểm tựa từ **Heapsort** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Comparison lower bound

Trong comparison mô hình (model / 모델), sorting n distinct elements cần Ω(n log n) comparisons worst-case. cây quyết định (decision tree / 의사결정 트리) có ít nhất n! leaves cho permutations; nhị phân (binary / 이진) comparison cây (tree / 트리) height ít nhất log₂(n!) = Θ(n log n).

Counting/radix sort vượt bound bằng cách không chỉ dùng pairwise comparisons; chúng khai thác key biểu diễn (representation / 표현)/phạm vi (range / 범위).

> **Chuyển mạch:** Trong **Sorting, searching và selection**, **Selection** tiếp nhận điểm tựa từ **Comparison lower bound** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bên ngoài (external / 외부) sorting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Selection

Selection hỏi k-th smallest mà không cần full sorting. Quickselect expected O(n) partition tương tự quicksort nhưng chỉ recurse một side. Median-of-medians cho worst-case O(n) nhưng constants lớn.

Nếu chỉ cần top-k streaming, vùng nhớ động (heap / 힙) kích thước (size / 크기) k cho O(n log k) có thể phù hợp hơn sorting toàn bộ O(n log n).

> **Chuyển mạch:** Ở chặng này của **Sorting, searching và selection**, **Bên ngoài (external / 외부) sorting** tiếp nhận điểm tựa từ **Selection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bên ngoài (external / 외부) sorting

Khi dữ liệu (data / 데이터) lớn hơn RAM, I/O dominates. bên ngoài (external / 외부) merge sort tạo sorted runs vừa bộ nhớ (memory / 메모리) rồi multi-way merge từ disk. Đây là lý do truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리) engine có algorithms khác khi sort spills to disk.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sorting, searching và selection**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Bên ngoài (external / 외부) sorting** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Sorting/searching hiệu năng (performance / 성능) đến từ **cấu trúc (structure / 구조) đã có** và **guarantee cần giữ**. Hỏi dữ liệu (data / 데이터) có sorted không, key lĩnh vực (domain / 도메인) gì, có cần stability/in-place/worst-case không, và dữ liệu (data / 데이터) có fit bộ nhớ (memory / 메모리) không.

> **Chuyển mạch:** Trong **Sorting, searching và selection**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Quicksort luôn O(n log n).”** Expected/average dưới pivot các giả định (assumptions / 가정들); worst-case O(n²).

**“tìm kiếm nhị phân (binary search / 이진 탐색) chỉ dùng để tìm number trong sorted array.”** Nó áp dụng cho bất kỳ monotonic predicate trên ordered tìm kiếm (search / 검색) không gian (space / 공간).

**“Sort O(n log n) là tối ưu tuyệt đối.”** Chỉ là lower bound trong comparison mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Sorting, searching và selection**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Sorting dựa [complexity](./01_complexity_and_asymptotic_analysis.md), [algorithm strategies](./08_algorithmic_strategies.md) và [memory locality](./02_memory_models_and_data_layout.md); cơ sở dữ liệu (database / 데이터베이스) có [sort/merge/hash query plans](../05_data_databases/03_indexes_and_query_execution.md) nơi dữ liệu (data / 데이터) kích thước (size / 크기) và I/O thay chi phí (cost / 비용) mô hình (model / 모델).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
