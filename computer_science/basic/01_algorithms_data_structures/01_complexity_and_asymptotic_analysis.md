# Time/space complexity và asymptotic analysis

Nếu hai algorithms đều đúng, ta cần biết chúng scale thế nào khi input lớn. Computational complexity (계산 복잡도 / độ phức tạp tính toán) xây một model đủ đơn giản để bỏ qua chi tiết máy cụ thể nhưng vẫn giữ được tốc độ tăng chi phí theo input size.

## Input size là gì?

Trước khi nói `O(n)`, phải định nghĩa `n`. Với array, thường `n` là số elements. Với integer `N`, input size theo theory thường là số bits cần biểu diễn `N`, xấp xỉ `log₂N`, không phải giá trị N. Một loop từ 1 đến N vì vậy exponential theo bit-length input nếu N được nhập ở binary.

Đây là chi tiết dễ bị bỏ qua và có thể làm classification sai hoàn toàn.

## Cost model

RAM model thường giả định các primitive operations như read/write một machine word hay arithmetic cơ bản có constant cost. Đây là approximation. Big integer arithmetic, cache miss, disk I/O, network RTT không thực sự constant.

Model không “sai”; nó có scope. Khi algorithmic growth là bottleneck, RAM model rất hữu ích. Khi performance phụ thuộc memory hierarchy hoặc I/O, ta cần richer model.

## Big O, Big Theta và Big Omega

Big O mô tả asymptotic upper bound. `T(n) ∈ O(f(n))` nếu tồn tại constants `c, n₀` sao cho `T(n) ≤ c f(n)` với mọi `n ≥ n₀`.

Big Ω là lower bound; Big Θ là tight bound khi cả upper và lower cùng bậc. Vì vậy nói merge sort worst-case `Θ(n log n)` chính xác hơn chỉ nói `O(n log n)`, dù trong engineering Big O thường được dùng lỏng để chỉ order of growth.

Constants và lower-order terms bị bỏ qua vì asymptotic analysis quan tâm shape khi n lớn. `3n² + 10n + 100` thuộc `Θ(n²)`.

## Những growth rates thường gặp

`O(1)` không có nghĩa “một instruction”; nó nghĩa cost không tăng theo n trong model. `O(log n)` thường xuất hiện khi mỗi step giảm search space theo factor. `O(n)` quét input một lần. `O(n log n)` phổ biến ở comparison sorting tối ưu. `O(n²)` xuất hiện khi xét mọi cặp. Exponential `O(2^n)` và factorial tăng cực nhanh.

Logarithm xuất hiện tự nhiên khi liên tục chia đôi. Nếu sau k bước còn `n/2^k = 1`, thì `k = log₂n`.

Xem toán sâu hơn tại [Algorithms, Complexity và Logarithms](../../mathematics/07_discrete_cs/01_algorithms_complexity_and_logarithms.md).

## Worst, average và best case

Worst-case guarantee quan trọng trong latency-sensitive hoặc adversarial context. Average-case cần probability distribution của inputs; nếu distribution assumption sai, kết luận có thể vô nghĩa. Best case thường ít hữu ích cho guarantee nhưng giúp hiểu behavior.

Hash table lookup có expected/amortized gần `O(1)` dưới assumptions hash tốt và load factor hợp lý, nhưng worst case có thể `O(n)`. Balanced BST cho `O(log n)` worst-case lookup. Lựa chọn phụ thuộc cần guarantee nào.

## Amortized analysis

Một operation đôi khi đắt nhưng hiếm. Dynamic array `append` thường constant; khi hết capacity phải allocate array lớn hơn và copy nhiều elements. Nếu capacity tăng theo factor, tổng copy qua n appends vẫn `O(n)`, nên amortized cost mỗi append là `O(1)`.

Amortized không phải average theo random input. Nó là guarantee trung bình trên sequence operations, thường không cần probability.

## Space complexity và time-space trade-off

Memoization dùng thêm memory để tránh tính lại. Hash index dùng storage để giảm query time. Cache dùng RAM để giảm I/O. Bloom filter dùng probabilistic false positives để tiết kiệm space.

Vì vậy time và space không độc lập. Nhiều design thực tế là chuyển chi phí từ resource này sang resource khác.

## Lower bounds

Không phải cứ code thông minh là vượt mọi bound. Comparison sorting có lower bound `Ω(n log n)` trong comparison model vì cần phân biệt `n!` possible orderings và mỗi binary comparison cung cấp tối đa một bit branch information.

Nhưng counting sort có thể `O(n+k)` vì nó không bị giới hạn bởi comparison model; nó khai thác keys trong finite range. Lower bound luôn gắn với assumptions/model.

## Complexity và actual performance

Một linked list insert có theoretical `O(1)` nếu đã có pointer, nhưng traversal và poor locality có thể làm nó chậm hơn array-based structure. `O(n)` contiguous scan có thể cực nhanh nhờ cache/prefetch. Database `O(log n)` B-tree lookup có thể bị disk/network latency chi phối.

Asymptotic analysis trả lời “growth”. Benchmarking trả lời “trên implementation/workload/hardware này”. Cả hai cần nhau.

## Complexity của recursive algorithms

Recurrence mô tả cost qua subproblems. Merge sort:

\[
T(n)=2T(n/2)+\Theta(n)
\]

Hai subproblems n/2 và merge linear dẫn tới `Θ(n log n)`. Có thể reasoning bằng recursion tree: mỗi level tổng work ~n, có log n levels.

## Mental Model

> Complexity là **shape của cost khi scale**, không phải stopwatch. Luôn hỏi: `n` là gì, cost model là gì, case nào đang nói, và assumptions nào làm bound đúng?

## Common Misconceptions

**“O(1) luôn nhanh hơn O(n).”** Với n nhỏ hoặc constants/hardware khác nhau, không nhất thiết. Big O nói asymptotic growth.

**“O(n) nghĩa chính xác n operations.”** Không. Nó là upper-order growth class.

**“Average O(1) hash lookup nghĩa worst case O(1).”** Không; collisions và adversarial inputs có thể làm chain/probe dài.

## Kết nối

Complexity giải thích algorithmic scaling; [memory layout](./02_memory_models_and_data_layout.md) giải thích constant factors và locality; [performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md) mở rộng từ một algorithm sang end-to-end system với queues, I/O và concurrency.
