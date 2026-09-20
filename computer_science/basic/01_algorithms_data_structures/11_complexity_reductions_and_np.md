# Complexity, reductions và NP

Big-O trả lời “runtime tăng thế nào với input size”, nhưng complexity theory (복잡도 이론) hỏi sâu hơn: **một problem về bản chất cần bao nhiêu tài nguyên để giải, và các problems liên hệ với nhau qua khả năng chuyển đổi như thế nào?** Đây là nơi xuất hiện P, NP, NP-hard, reductions và lower bounds.

## Problem khác algorithm

Một algorithm là một procedure cụ thể. Một computational problem là tập mọi instances và output hợp lệ tương ứng. Sorting là problem; merge sort và quicksort là algorithms.

Complexity class phân loại problems, không phân loại một đoạn code cụ thể. Khi nói SAT thuộc NP, ta đang nói về decision problem Boolean satisfiability, không phải performance của một implementation SAT solver cụ thể.

## Decision problems như dạng chuẩn để reasoning

Nhiều optimization problems có thể chuyển sang decision form. Thay vì “tìm route ngắn nhất”, hỏi “có route dài không quá K hay không?”. Decision form giúp định nghĩa classes và reductions sạch hơn.

Điều này không có nghĩa practical software chỉ dùng yes/no. Nó là abstraction lý thuyết để so sánh difficulty.

## P: giải được trong polynomial time

P chứa decision problems có deterministic algorithm chạy polynomial time theo input size, ví dụ `O(n)`, `O(n²)`, `O(n^5)`.

Polynomial không đồng nghĩa “nhanh trong thực tế”. `n^100` là polynomial nhưng vô dụng cho input vừa phải. P chủ yếu biểu thị một boundary lý thuyết giữa growth polynomial và nhiều dạng combinatorial explosion.

## NP: solution có thể verify nhanh

NP chứa decision problems mà nếu ai đó đưa một certificate cho answer YES, ta có thể verify certificate trong polynomial time.

Ví dụ với Hamiltonian cycle, certificate là một thứ tự vertices. Verifier kiểm tra mỗi vertex xuất hiện đúng một lần và consecutive vertices có edges phù hợp.

> NP không có nghĩa “non-polynomial”. Tên lịch sử là nondeterministic polynomial time.

Mọi problem trong P cũng thuộc NP vì nếu tự giải nhanh được thì tất nhiên có thể verify nhanh.

## Reduction: dùng problem A để biểu diễn problem B

Polynomial-time reduction từ A sang B nghĩa là có transformation polynomial time biến instance của A thành instance của B sao cho answer được bảo toàn.

Nếu A reduce sang B, ta có thể dùng solver cho B để giải A sau bước transform. Vì vậy B ít nhất “khó như” A theo reduction đó.

Reduction là một trong những ideas xuyên suốt CS: compiler lowering, serialization, database query rewriting và protocol translation đều có bóng dáng “đổi representation nhưng bảo toàn meaning”, dù formal reduction trong complexity có definition chặt hơn.

## NP-hard và NP-complete

Một problem là NP-hard nếu mọi problem trong NP có thể polynomial-time reduce sang nó. Nó không nhất thiết thuộc NP hoặc thậm chí là decision problem.

Một problem là NP-complete nếu vừa thuộc NP vừa NP-hard. SAT là problem NP-complete lịch sử đầu tiên qua Cook–Levin theorem.

Để chứng minh problem X NP-complete, pattern điển hình là: chứng minh X ∈ NP, rồi chọn một problem Y đã biết NP-complete và reduce **Y → X**.

Hướng reduction thường bị nhầm. Nếu reduce X → Y, điều đó chỉ cho thấy Y ít nhất khó như X, không chứng minh X khó.

## P versus NP

Câu hỏi P = NP hay không vẫn chưa được giải quyết. Nếu P = NP, mọi problem có certificate verify polynomial cũng có thể solve polynomial về mặt asymptotic. Nếu P ≠ NP, tồn tại problems verify nhanh nhưng solve không có polynomial algorithm.

Không nên suy diễn rằng “NP-complete nghĩa là không thể giải”. Instances nhỏ, structure đặc biệt, parameterization, approximation, heuristics và exponential algorithms tối ưu hóa vẫn có thể cực kỳ hữu ích.

SAT solvers hiện đại giải nhiều industrial instances rất lớn vì real-world structure khác worst-case adversarial instances.

## Lower bounds và comparison sorting

Một lower bound nói không algorithm nào trong model nhất định có thể vượt một cost asymptotic nào đó.

Comparison-based sorting có lower bound `Ω(n log n)` comparisons vì có `n!` permutations và mỗi comparison phân nhánh tối đa hai outcomes. Decision tree phải có ít nhất `n!` leaves, nên height ít nhất `log₂(n!) = Ω(n log n)`.

Counting sort có thể `O(n+k)` vì nó không bị giới hạn trong comparison model; nó khai thác structure của keys. Vì vậy lower bound luôn phụ thuộc computational model và assumptions.

## Parameterized complexity

Có problem exponential theo `n` nhưng practical nếu một parameter `k` nhỏ. Fixed-parameter tractable (FPT) algorithms có form như `f(k) * poly(n)`.

Cách nhìn này quan trọng trong practice: difficulty không chỉ phụ thuộc raw input size mà còn cấu trúc instance.

## Common Misconceptions

**“NP là các bài toán cần exponential time.”** Chưa biết điều đó cho mọi NP-complete problem; chính P vs NP hỏi liệu polynomial algorithms có tồn tại hay không.

**“NP-hard nghĩa là không giải được.”** Nó nói về worst-case complexity dưới reductions, không cấm practical solvers, approximation hay special cases.

**“Một algorithm O(n²) luôn tốt hơn O(2^n).”** Với input nhỏ và constants khác nhau, không nhất thiết. Complexity mô tả scaling, không thay benchmark.

## Mental Model

> Complexity theory không chỉ hỏi “algorithm này tốn bao lâu”, mà xây bản đồ giữa problems: problem nào biến được thành problem nào, boundary tài nguyên nằm ở đâu, và limitation nào đến từ bản chất chứ không phải implementation yếu.

## Kết nối

Đọc cùng [asymptotic analysis](./01_complexity_and_asymptotic_analysis.md), [algorithmic strategies](./08_algorithmic_strategies.md) và [randomized/approximation algorithms](./10_randomized_approximation_and_online_algorithms.md). Nền logic/computability nằm tại [Computability](../00_computation_information/04_computability_and_limits.md) và [Automata/Formal Languages](../../mathematics/07_discrete_cs/07_automata_formal_languages_and_computability.md).