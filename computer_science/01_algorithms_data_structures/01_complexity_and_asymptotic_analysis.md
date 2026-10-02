# Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**. Route đi từ input size và cost model → Big-O/Theta/Omega → amortized/average/worst case → trade-off thời gian–bộ nhớ, để so sánh thuật toán trong đúng mô hình tài nguyên.

Nếu hai algorithms đều đúng, ta cần biết chúng quy mô (scale / 규모) thế nào khi đầu vào (input / 입력) lớn. Computational độ phức tạp (complexity / 복잡도) xây một mô hình (model / 모델) đủ đơn giản để bỏ qua chi tiết máy cụ thể nhưng vẫn giữ được tốc độ tăng chi phí theo đầu vào (input / 입력) kích thước (size / 크기).

## Đầu vào (input / 입력) kích thước (size / 크기) là gì?

Trước khi nói `O(n)`, phải định nghĩa `n`. Với array, thường `n` là số elements. Với integer `N`, đầu vào (input / 입력) kích thước (size / 크기) theo lý thuyết (theory / 이론) thường là số bits cần biểu diễn `N`, xấp xỉ `log₂N`, không phải giá trị N. Một vòng lặp (loop / 루프) từ 1 đến N vì vậy exponential theo bit-length đầu vào (input / 입력) nếu N được nhập ở nhị phân (binary / 이진).

Đây là chi tiết dễ bị bỏ qua và có thể làm classification sai hoàn toàn.

> **Chuyển mạch:** Trước khi tính chi phí, phải chốt input size và cost model; Big O cho cận trên tăng trưởng, Big Theta mô tả cùng bậc, còn Big Omega giữ cận dưới để so sánh thuật toán.

## Chi phí (cost / 비용) mô hình (model / 모델)

RAM mô hình (model / 모델) thường giả định các thành phần nguyên thủy (primitive / 기본 요소) operations như read/ghi (write / 쓰기) một machine word hay arithmetic cơ bản có constant chi phí (cost / 비용). Đây là approximation. Big integer arithmetic, trượt bộ nhớ đệm (cache miss / 캐시 미스), disk I/O, mạng (network / 네트워크) RTT không thực sự constant.

Mô hình (model / 모델) không “sai”; nó có phạm vi (scope / 범위). Khi algorithmic growth là bottleneck, RAM mô hình (model / 모델) rất hữu ích. Khi hiệu năng (performance / 성능) phụ thuộc bộ nhớ (memory / 메모리) hierarchy hoặc I/O, ta cần richer mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Big O, Big Theta và Big Omega** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những growth rates thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Big O, Big Theta và Big Omega

Big O mô tả asymptotic upper bound. `T(n) ∈ O(f(n))` nếu tồn tại constants `c, n₀` sao cho `T(n) ≤ c f(n)` với mọi `n ≥ n₀`.

Big Ω là lower bound; Big Θ là tight bound khi cả upper và lower cùng bậc. Vì vậy nói merge sort worst-case `Θ(n log n)` chính xác hơn chỉ nói `O(n log n)`, dù trong kỹ thuật (engineering / 엔지니어링) Big O thường được dùng lỏng để chỉ thứ tự (order / 순서) of growth.

Constants và lower-order terms bị bỏ qua vì asymptotic phân tích (analysis / 분석) quan tâm shape khi n lớn. `3n² + 10n + 100` thuộc `Θ(n²)`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Những growth rates thường gặp** tiếp nhận điểm tựa từ **Big O, Big Theta và Big Omega** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Worst, average và best trường hợp (case / 사례)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những growth rates thường gặp

`O(1)` không có nghĩa “một instruction”; nó nghĩa chi phí (cost / 비용) không tăng theo n trong mô hình (model / 모델). `O(log n)` thường xuất hiện khi mỗi step giảm tìm kiếm (search / 검색) không gian (space / 공간) theo factor. `O(n)` quét đầu vào (input / 입력) một lần. `O(n log n)` phổ biến ở comparison sorting tối ưu. `O(n²)` xuất hiện khi xét mọi cặp. Exponential `O(2^n)` và factorial tăng cực nhanh.

Logarithm xuất hiện tự nhiên khi liên tục chia đôi. Nếu sau k bước còn `n/2^k = 1`, thì `k = log₂n`.

Xem toán sâu hơn tại [Algorithms, Complexity và Logarithms](../../mathematics/07_discrete_cs/01_algorithms_complexity_and_logarithms.md).

> **Chuyển mạch:** Trong **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Những growth rates thường gặp** cho ta quy tắc; **Worst, average và best trường hợp (case / 사례)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Amortized phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Worst, average và best trường hợp (case / 사례)

Worst-case guarantee quan trọng trong latency-sensitive hoặc adversarial ngữ cảnh (context / 맥락). Average-case cần xác suất (probability / 확률) phân phối (distribution / 분포) của inputs; nếu phân phối (distribution / 분포) giả định (assumption / 가정) sai, kết luận có thể vô nghĩa. Best trường hợp (case / 사례) thường ít hữu ích cho guarantee nhưng giúp hiểu hành vi (behavior / 동작).

Bảng băm (hash table / 해시 테이블) lookup có expected/amortized gần `O(1)` dưới các giả định (assumptions / 가정들) băm (hash / 해시) tốt và tải (load / 로드) factor hợp lý, nhưng worst trường hợp (case / 사례) có thể `O(n)`. Balanced BST cho `O(log n)` worst-case lookup. Lựa chọn phụ thuộc cần guarantee nào.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Worst, average và best trường hợp (case / 사례)** cho ta quy tắc; **Amortized phân tích (analysis / 분석)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Không gian (space / 공간) độ phức tạp (complexity / 복잡도) và time-space sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Amortized phân tích (analysis / 분석)

Một thao tác (operation / 연산) đôi khi đắt nhưng hiếm. động (dynamic / 동적) array `append` thường constant; khi hết sức chứa (capacity / 용량) phải allocate array lớn hơn và bản sao (copy / 복사) nhiều elements. Nếu sức chứa (capacity / 용량) tăng theo factor, tổng bản sao (copy / 복사) qua n appends vẫn `O(n)`, nên amortized chi phí (cost / 비용) mỗi append là `O(1)`.

Amortized không phải average theo random đầu vào (input / 입력). Nó là guarantee trung bình trên chuỗi (sequence / 시퀀스) operations, thường không cần xác suất (probability / 확률).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Không gian (space / 공간) độ phức tạp (complexity / 복잡도) và time-space sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Amortized phân tích (analysis / 분석)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lower bounds** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Không gian (space / 공간) độ phức tạp (complexity / 복잡도) và time-space sự đánh đổi (trade-off / 트레이드오프)

Memoization dùng thêm bộ nhớ (memory / 메모리) để tránh tính lại. băm (hash / 해시) chỉ mục (index / 인덱스) dùng lưu trữ (storage / 저장소) để giảm truy vấn (query / 쿼리) thời gian (time / 시간). bộ nhớ đệm (cache / 캐시) dùng RAM để giảm I/O. Bloom filter dùng probabilistic false positives để tiết kiệm không gian (space / 공간).

Vì vậy thời gian (time / 시간) và không gian (space / 공간) không độc lập. Nhiều thiết kế (design / 설계) thực tế là chuyển chi phí từ tài nguyên (resource / 자원) này sang tài nguyên (resource / 자원) khác.

> **Chuyển mạch:** Trong **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Lower bounds** tiếp nhận điểm tựa từ **Không gian (space / 공간) độ phức tạp (complexity / 복잡도) và time-space sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ phức tạp (complexity / 복잡도) và actual hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lower bounds

Không phải cứ mã (code / 코드) thông minh là vượt mọi bound. Comparison sorting có lower bound `Ω(n log n)` trong comparison mô hình (model / 모델) vì cần phân biệt `n!` possible orderings và mỗi nhị phân (binary / 이진) comparison cung cấp tối đa một bit branch thông tin (information / 정보).

Nhưng counting sort có thể `O(n+k)` vì nó không bị giới hạn bởi comparison mô hình (model / 모델); nó khai thác keys trong finite phạm vi (range / 범위). Lower bound luôn gắn với các giả định (assumptions / 가정들)/mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Độ phức tạp (complexity / 복잡도) và actual hiệu năng (performance / 성능)** tiếp nhận điểm tựa từ **Lower bounds** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ phức tạp (complexity / 복잡도) của recursive algorithms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ phức tạp (complexity / 복잡도) và actual hiệu năng (performance / 성능)

Một linked danh sách (list / 목록) insert có theoretical `O(1)` nếu đã có pointer, nhưng traversal và poor locality có thể làm nó chậm hơn array-based cấu trúc (structure / 구조). `O(n)` contiguous scan có thể cực nhanh nhờ bộ nhớ đệm (cache / 캐시)/prefetch. cơ sở dữ liệu (database / 데이터베이스) `O(log n)` B-tree lookup có thể bị disk/mạng (network / 네트워크) độ trễ (latency / 지연 시간) chi phối.

Asymptotic phân tích (analysis / 분석) trả lời “growth”. Benchmarking trả lời “trên hiện thực (implementation / 구현)/tải công việc (workload / 워크로드)/hardware này”. Cả hai cần nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Độ phức tạp (complexity / 복잡도) của recursive algorithms** tiếp nhận điểm tựa từ **Độ phức tạp (complexity / 복잡도) và actual hiệu năng (performance / 성능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ phức tạp (complexity / 복잡도) của recursive algorithms

Recurrence mô tả chi phí (cost / 비용) qua subproblems. Merge sort:

\[
T(n)=2T(n/2)+\Theta(n)
\]

Hai subproblems n/2 và merge tuyến tính (linear / 선형) dẫn tới `Θ(n log n)`. Có thể lập luận (reasoning / 추론) bằng recursion cây (tree / 트리): mỗi mức (level / 수준) tổng công việc (work / 작업) ~n, có log n levels.

> **Chuyển mạch:** Trong **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Độ phức tạp (complexity / 복잡도) của recursive algorithms** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> độ phức tạp (complexity / 복잡도) là **shape của chi phí (cost / 비용) khi quy mô (scale / 규모)**, không phải stopwatch. Luôn hỏi: `n` là gì, chi phí (cost / 비용) mô hình (model / 모델) là gì, trường hợp (case / 사례) nào đang nói, và các giả định (assumptions / 가정들) nào làm bound đúng?

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“O(1) luôn nhanh hơn O(n).”** Với n nhỏ hoặc constants/hardware khác nhau, không nhất thiết. Big O nói asymptotic growth.

**“O(n) nghĩa chính xác n operations.”** Không. Nó là upper-order growth lớp (class / 클래스).

**“Average O(1) băm (hash / 해시) lookup nghĩa worst trường hợp (case / 사례) O(1).”** Không; collisions và adversarial inputs có thể làm chuỗi (chain / 사슬)/probe dài.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간)/không gian (space / 공간) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Độ phức tạp (complexity / 복잡도) giải thích algorithmic scaling; [memory layout](./02_memory_models_and_data_layout.md) giải thích constant factors và locality; [performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md) mở rộng từ một thuật toán (algorithm / 알고리즘) sang end-to-end hệ thống (system / 시스템) với queues, I/O và tính đồng thời (concurrency / 동시성).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
