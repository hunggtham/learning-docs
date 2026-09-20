# Randomized, approximation và online algorithms

Không phải mọi problem đều cho ta toàn bộ input trước, đủ time để tìm optimum, hoặc có deterministic strategy vừa đơn giản vừa nhanh. Ba families quan trọng xuất hiện từ chính các constraints đó: randomized algorithms dùng randomness như một computational resource; approximation algorithms chấp nhận nghiệm gần tối ưu khi exact optimization quá đắt; online algorithms phải quyết định khi tương lai chưa được biết.

## Randomness không phải sự cẩu thả

Randomized algorithm (무작위 알고리즘) đưa random choices vào computation nhưng vẫn được phân tích bằng probability. Randomness có thể giúp phá adversarial structure, đơn giản hóa code hoặc cải thiện expected complexity.

Randomized quicksort chọn pivot ngẫu nhiên. Với mọi input cố định, expected running time là `O(n log n)` nếu randomness đủ tốt. Worst-case `O(n²)` vẫn tồn tại, nhưng xác suất rơi vào chuỗi pivot cực xấu giảm mạnh.

Điều cần phân biệt là **worst-case over random choices** với **expected cost over random choices**. Đây là hai statements toán học khác nhau.

### Las Vegas và Monte Carlo

Las Vegas algorithms luôn trả kết quả đúng nhưng runtime là random variable. Randomized quicksort là ví dụ điển hình.

Monte Carlo algorithms giới hạn runtime rõ hơn nhưng có probability trả kết quả sai. Bloom filter là một cấu trúc probabilistic: membership query có thể false positive nhưng không false negative nếu dùng đúng model.

Trong systems, probabilistic data structures như Bloom filter, HyperLogLog và Count-Min Sketch được dùng vì memory chính xác tuyệt đối có thể quá đắt.

## Approximation: khi exact optimum quá đắt

Một optimization problem có thể có search space tăng exponential. Nếu problem là NP-hard, exact solution cho input lớn thường không thực tế trừ khi structure đặc biệt hoặc instance nhỏ.

Approximation algorithm (근사 알고리즘) cung cấp guarantee định lượng. Ví dụ một 2-approximation cho minimization đảm bảo cost của solution không vượt quá 2 lần optimum.

Guarantee quan trọng hơn câu “thường chạy tốt”. Nó biến chất lượng solution thành property có thể reasoning.

### Heuristic khác approximation algorithm

Heuristic là strategy thực dụng nhưng có thể không có worst-case quality guarantee. Genetic algorithm, simulated annealing hoặc greedy tùy problem có thể rất hữu ích, nhưng không vì thế trở thành approximation algorithm theo nghĩa lý thuyết.

Trong engineering, heuristic hoàn toàn hợp lệ nếu đo được behavior trên workload. Điều cần tránh là gọi empirical success thành mathematical guarantee.

## Online algorithms: quyết định trước khi thấy tương lai

Online algorithm (온라인 알고리즘) nhận input theo thời gian và phải quyết định mà không biết phần còn lại. Cache replacement là ví dụ trực quan: khi cache đầy, ta phải evict một item trước khi biết request tương lai.

Nếu biết tương lai hoàn toàn, Belady's optimal algorithm sẽ evict item có lần sử dụng tiếp theo xa nhất. Nhưng system thật không có oracle, nên dùng LRU, LFU, CLOCK hoặc policy thích nghi.

Competitive analysis so online algorithm với optimal offline algorithm biết toàn bộ tương lai. Một competitive ratio mô tả mức tệ nhất tương đối đó.

## Streaming: input quá lớn để giữ toàn bộ

Streaming algorithms xử lý sequence trong một hoặc vài passes với memory nhỏ. Câu hỏi chuyển từ “lưu dữ liệu gì?” sang “summary state tối thiểu nào vẫn trả lời được query gần đúng?”

Ví dụ HyperLogLog ước lượng số distinct elements bằng statistical properties của hash outputs thay vì giữ set mọi element. Count-Min Sketch ước lượng frequencies bằng nhiều hash tables nhỏ.

Đây là điểm nối trực tiếp giữa algorithms, probability, systems telemetry và large-scale data processing.

## Randomization trong distributed systems

Randomized backoff giảm probability nhiều clients retry đồng thời. Leader election có thể dùng random timeout để tránh symmetry. Load balancing kiểu “power of two choices” chọn ngẫu nhiên hai servers rồi gửi vào server nhẹ hơn, cho kết quả bất ngờ tốt với overhead nhỏ.

Randomness ở đây không nhằm làm hệ thống khó đoán mà để giảm synchronization pathologies và adversarial alignment.

## Adversarial inputs và security boundary

Hash table trung bình `O(1)` có thể bị degrade nếu attacker điều khiển keys gây nhiều collisions. Một defense là randomized hash seed để attacker khó predict bucket placement.

Nhưng pseudo-randomness cho performance khác cryptographic randomness. Security cần entropy và unpredictability mạnh hơn; không nên dùng PRNG thường cho keys/tokens.

## Common Misconceptions

**“Randomized nghĩa là kết quả không đáng tin.”** Las Vegas algorithms luôn đúng; Monte Carlo có error probability được định lượng.

**“Approximation chỉ là làm ẩu.”** Approximation algorithm có quality guarantee. Heuristic không nhất thiết có.

**“Online algorithm kém vì thiếu dữ liệu.”** Thiếu tương lai là constraint bản chất của nhiều systems. Online analysis giúp biết giới hạn có thể đạt.

## Mental Model

> Khi exact deterministic computation không phù hợp constraints, hỏi ba câu: randomness có phá structure xấu không, approximate answer có đủ không, và quyết định có buộc phải xảy ra trước khi biết tương lai không?

## Kết nối

Nền probability xem tại [Probability Foundations](../../mathematics/06_probability_statistics/01_probability_foundations.md). Complexity và NP-hardness được mở rộng tại [Complexity, reductions và NP](./11_complexity_reductions_and_np.md). Các applications hệ thống xuất hiện trong [cache/scalability](../08_software_systems/02_performance_capacity_and_scalability.md) và [reliability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md).