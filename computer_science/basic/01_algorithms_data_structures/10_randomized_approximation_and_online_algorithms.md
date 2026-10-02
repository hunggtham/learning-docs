# Randomized, approximation và online algorithms

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Randomized, approximation và online algorithms**. Route đi từ randomness/probability → expected bounds → approximation ratio → adversarial/online decisions → regret/competitive analysis, để trade-off chính xác–chi phí được định lượng.

Không phải mọi bài toán (problem / 문제) đều cho ta toàn bộ đầu vào (input / 입력) trước, đủ thời gian (time / 시간) để tìm optimum, hoặc có deterministic chiến lược (strategy / 전략) vừa đơn giản vừa nhanh. Ba families quan trọng xuất hiện từ chính các các ràng buộc (constraints / 제약조건들) đó: randomized algorithms dùng randomness như một computational tài nguyên (resource / 자원); approximation algorithms chấp nhận nghiệm gần tối ưu khi chính xác (exact / 정확한) tối ưu hóa (optimization / 최적화) quá đắt; online algorithms phải quyết định khi tương lai chưa được biết.

## Randomness không phải sự cẩu thả

Randomized thuật toán (algorithm / 알고리즘) đưa random choices vào computation nhưng vẫn được phân tích bằng xác suất (probability / 확률). Randomness có thể giúp phá adversarial cấu trúc (structure / 구조), đơn giản hóa mã (code / 코드) hoặc cải thiện expected độ phức tạp (complexity / 복잡도).

Randomized quicksort chọn pivot ngẫu nhiên. Với mọi đầu vào (input / 입력) cố định, expected running thời gian (time / 시간) là `O(n log n)` nếu randomness đủ tốt. Worst-case `O(n²)` vẫn tồn tại, nhưng xác suất rơi vào chuỗi pivot cực xấu giảm mạnh.

Điều cần phân biệt là **worst-case over random choices** với **expected chi phí (cost / 비용) over random choices**. Đây là hai statements toán học khác nhau.

### Las Vegas và Monte Carlo

Las Vegas algorithms luôn trả kết quả đúng nhưng thời gian chạy (runtime / 런타임) là random variable. Randomized quicksort là ví dụ điển hình.

Monte Carlo algorithms giới hạn thời gian chạy (runtime / 런타임) rõ hơn nhưng có xác suất (probability / 확률) trả kết quả sai. Bloom filter là một cấu trúc probabilistic: membership truy vấn (query / 쿼리) có thể false positive nhưng không false negative nếu dùng đúng mô hình (model / 모델).

Trong các hệ thống (systems / 시스템들), probabilistic dữ liệu (data / 데이터) structures như Bloom filter, HyperLogLog và Count-Min Sketch được dùng vì bộ nhớ (memory / 메모리) chính xác tuyệt đối có thể quá đắt.

> **Chuyển mạch:** Trong **Randomized, approximation và online algorithms**, **Approximation: khi chính xác (exact / 정확한) optimum quá đắt** tiếp nhận điểm tựa từ **Randomness không phải sự cẩu thả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Online algorithms: quyết định trước khi thấy tương lai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Approximation: khi chính xác (exact / 정확한) optimum quá đắt

Một tối ưu hóa (optimization / 최적화) bài toán (problem / 문제) có thể có tìm kiếm (search / 검색) không gian (space / 공간) tăng exponential. Nếu bài toán (problem / 문제) là NP-hard, chính xác (exact / 정확한) solution cho đầu vào (input / 입력) lớn thường không thực tế trừ khi cấu trúc (structure / 구조) đặc biệt hoặc instance nhỏ.

Approximation thuật toán (algorithm / 알고리즘) cung cấp guarantee định lượng. Ví dụ một 2-approximation cho minimization đảm bảo chi phí (cost / 비용) của solution không vượt quá 2 lần optimum.

Guarantee quan trọng hơn câu “thường chạy tốt”. Nó biến chất lượng solution thành thuộc tính (property / 속성) có thể lập luận (reasoning / 추론).

### Heuristic khác approximation thuật toán (algorithm / 알고리즘)

Heuristic là chiến lược (strategy / 전략) thực dụng nhưng có thể không có worst-case chất lượng (quality / 품질) guarantee. Genetic thuật toán (algorithm / 알고리즘), simulated annealing hoặc greedy tùy bài toán (problem / 문제) có thể rất hữu ích, nhưng không vì thế trở thành approximation thuật toán (algorithm / 알고리즘) theo nghĩa lý thuyết.

Trong kỹ thuật (engineering / 엔지니어링), heuristic hoàn toàn hợp lệ nếu đo được hành vi (behavior / 동작) trên tải công việc (workload / 워크로드). Điều cần tránh là gọi empirical success thành mathematical guarantee.

> **Chuyển mạch:** Ở chặng này của **Randomized, approximation và online algorithms**, **Online algorithms: quyết định trước khi thấy tương lai** tiếp nhận điểm tựa từ **Approximation: khi chính xác (exact / 정확한) optimum quá đắt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Streaming: đầu vào (input / 입력) quá lớn để giữ toàn bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Online algorithms: quyết định trước khi thấy tương lai

Online thuật toán (algorithm / 알고리즘) nhận đầu vào (input / 입력) theo thời gian và phải quyết định mà không biết phần còn lại. bộ nhớ đệm (cache / 캐시) replacement là ví dụ trực quan: khi bộ nhớ đệm (cache / 캐시) đầy, ta phải evict một item trước khi biết yêu cầu (request / 요청) tương lai.

Nếu biết tương lai hoàn toàn, Belady's optimal thuật toán (algorithm / 알고리즘) sẽ evict item có lần sử dụng tiếp theo xa nhất. Nhưng hệ thống (system / 시스템) thật không có oracle, nên dùng LRU, LFU, CLOCK hoặc chính sách (policy / 정책) thích nghi.

Competitive phân tích (analysis / 분석) so online thuật toán (algorithm / 알고리즘) với optimal offline thuật toán (algorithm / 알고리즘) biết toàn bộ tương lai. Một competitive ratio mô tả mức tệ nhất tương đối đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Randomized, approximation và online algorithms**, **Streaming: đầu vào (input / 입력) quá lớn để giữ toàn bộ** tiếp nhận điểm tựa từ **Online algorithms: quyết định trước khi thấy tương lai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Randomization trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Streaming: đầu vào (input / 입력) quá lớn để giữ toàn bộ

Streaming algorithms xử lý chuỗi (sequence / 시퀀스) trong một hoặc vài passes với bộ nhớ (memory / 메모리) nhỏ. Câu hỏi chuyển từ “lưu dữ liệu gì?” sang “summary trạng thái (state / 상태) tối thiểu nào vẫn trả lời được truy vấn (query / 쿼리) gần đúng?”

Ví dụ HyperLogLog ước lượng số distinct elements bằng statistical properties của băm (hash / 해시) outputs thay vì giữ set mọi element. Count-Min Sketch ước lượng frequencies bằng nhiều băm (hash / 해시) tables nhỏ.

Đây là điểm nối trực tiếp giữa algorithms, xác suất (probability / 확률), các hệ thống (systems / 시스템들) telemetry và large-scale dữ liệu (data / 데이터) processing.

> **Chuyển mạch:** Trong **Randomized, approximation và online algorithms**, **Randomization trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)** tiếp nhận điểm tựa từ **Streaming: đầu vào (input / 입력) quá lớn để giữ toàn bộ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Adversarial inputs và ranh giới bảo mật (security boundary / 보안 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Randomization trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)

Randomized backoff giảm xác suất (probability / 확률) nhiều clients thử lại (retry / 재시도) đồng thời. Leader election có thể dùng random hết thời gian chờ (timeout / 타임아웃) để tránh symmetry. tải (load / 로드) balancing kiểu “power of two choices” chọn ngẫu nhiên hai servers rồi gửi vào máy chủ (server / 서버) nhẹ hơn, cho kết quả bất ngờ tốt với overhead nhỏ.

Randomness ở đây không nhằm làm hệ thống khó đoán mà để giảm synchronization pathologies và adversarial alignment.

> **Chuyển mạch:** Ở chặng này của **Randomized, approximation và online algorithms**, **Randomization trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)** đã nêu tiêu chí phân biệt, còn **Adversarial inputs và ranh giới bảo mật (security boundary / 보안 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adversarial inputs và ranh giới bảo mật (security boundary / 보안 경계)

Bảng băm (hash table / 해시 테이블) trung bình `O(1)` có thể bị degrade nếu attacker điều khiển keys gây nhiều collisions. Một defense là randomized băm (hash / 해시) seed để attacker khó predict bucket placement.

Nhưng pseudo-randomness cho hiệu năng (performance / 성능) khác cryptographic randomness. bảo mật (security / 보안) cần entropy và unpredictability mạnh hơn; không nên dùng PRNG thường cho keys/tokens.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Randomized, approximation và online algorithms**, **Adversarial inputs và ranh giới bảo mật (security boundary / 보안 경계)** đã nêu tiêu chí phân biệt, còn **Dùng chung (common / 공통) Misconceptions** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Randomized nghĩa là kết quả không đáng tin.”** Las Vegas algorithms luôn đúng; Monte Carlo có lỗi (error / 오류) xác suất (probability / 확률) được định lượng.

**“Approximation chỉ là làm ẩu.”** Approximation thuật toán (algorithm / 알고리즘) có chất lượng (quality / 품질) guarantee. Heuristic không nhất thiết có.

**“Online thuật toán (algorithm / 알고리즘) kém vì thiếu dữ liệu.”** Thiếu tương lai là ràng buộc (constraint / 제약조건) bản chất của nhiều các hệ thống (systems / 시스템들). Online phân tích (analysis / 분석) giúp biết giới hạn có thể đạt.

> **Chuyển mạch:** Trong **Randomized, approximation và online algorithms**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Khi chính xác (exact / 정확한) deterministic computation không phù hợp các ràng buộc (constraints / 제약조건들), hỏi ba câu: randomness có phá cấu trúc (structure / 구조) xấu không, approximate answer có đủ không, và quyết định có buộc phải xảy ra trước khi biết tương lai không?

> **Chuyển mạch:** Ở chặng này của **Randomized, approximation và online algorithms**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Nền xác suất (probability / 확률) xem tại [Probability Foundations](../../../mathematics/06_probability_statistics/01_probability_foundations.md). độ phức tạp (complexity / 복잡도) và NP-hardness được mở rộng tại [Complexity, reductions và NP](./11_complexity_reductions_and_np.md). Các applications hệ thống xuất hiện trong [cache/scalability](../08_software_systems/02_performance_capacity_and_scalability.md) và [reliability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
