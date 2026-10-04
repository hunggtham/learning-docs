# AI bài toán (problem / 문제) formulation, tìm kiếm (search / 검색) và agents

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **AI problem formulation, search và agents**. Route đi từ state/goal formulation → state-space search/heuristics → adversarial search/planning → utility/uncertainty → agent feedback, để chọn thuật toán theo mục tiêu và chi phí tìm kiếm.

Artificial Intelligence (AI / 인공지능) rộng hơn machine học tập (learning / 학습). Một cách nhìn nền tảng là xây agents nhận observations, giữ/ước lượng trạng thái (state / 상태) và chọn actions để đạt objectives dưới bất định (uncertainty / 불확실성) và tài nguyên (resource / 자원) các ràng buộc (constraints / 제약조건들).

## Tác nhân (agent / 에이전트) mô hình (model / 모델)

Tác nhân (agent / 에이전트) nhận percepts từ môi trường (environment / 환경) và tạo actions. Rational tác nhân (agent / 에이전트) chọn hành động (action / 동작) expected to best satisfy hiệu năng (performance / 성능) measure dựa trên available thông tin (information / 정보), không nhất thiết “thông minh như người”.

Môi trường (environment / 환경) có thể fully/partially observable, deterministic/stochastic, episodic/sequential, static/động (dynamic / 동적), discrete/continuous.

Phân loại này quyết định thuật toán (algorithm / 알고리즘) family phù hợp.

> **Nối mạch:** Agent model xác định trạng thái, hành động và mục tiêu; state-space search duyệt các khả năng đó, còn heuristic ưu tiên nhánh có vẻ gần lời giải nhưng phải được kiểm tra về tính đúng đắn.

## State-space tìm kiếm (search / 검색)

Nhiều AI problems có thể biểu diễn bằng states, actions, chuyển tiếp (transition / 전이) mô hình (model / 모델), initial trạng thái (state / 상태) và goal kiểm thử (test / 테스트).

Đường dẫn (path / 경로) planning, puzzle, planning và game tìm kiếm (search / 검색) đều trở thành đồ thị (graph / 그래프) tìm kiếm (search / 검색) trên implicit trạng thái (state / 상태) không gian (space / 공간).

BFS tìm shortest đường dẫn (path / 경로) theo số edges khi costs bằng nhau; Dijkstra dùng non-negative costs; A* dùng heuristic để hướng tìm kiếm (search / 검색).

> **Nối mạch:** **Heuristic** nối từ **State-space tìm kiếm (search / 검색)** sang **Tìm kiếm (search / 검색) explosion**, vì cơ chế trước tạo đầu vào cho bước sau.

## Heuristic

Heuristic `h(n)` ước lượng remaining chi phí (cost / 비용) tới goal. A* dùng:

\[
f(n)=g(n)+h(n)
\]

với `g(n)` là chi phí (cost / 비용) đã đi.

Nếu heuristic admissible—không overestimate true remaining chi phí (cost / 비용)—A* có optimality guarantee dưới các giả định (assumptions / 가정들) phù hợp. Consistency giúp graph-search hành vi (behavior / 동작) tốt hơn.

Heuristic tốt encode lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) và giảm explored states.

> **Nối mạch:** **Tìm kiếm (search / 검색) explosion** nối từ **Heuristic** sang **Adversarial tìm kiếm (search / 검색)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tìm kiếm (search / 검색) explosion

Branching factor `b` và độ sâu (depth / 깊이) `d` có thể tạo khoảng `b^d` states. Đây là combinatorial explosion; bộ nhớ (memory / 메모리) thường là bottleneck của BFS/A*.

AI tìm kiếm (search / 검색) vì vậy liên hệ trực tiếp độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론), approximation và heuristics.

> **Nối mạch:** **Adversarial tìm kiếm (search / 검색)** nối từ **Tìm kiếm (search / 검색) explosion** sang **Planning**, vì cơ chế trước tạo đầu vào cho bước sau.

## Adversarial tìm kiếm (search / 검색)

Game hai người zero-sum có thể dùng minimax: player maximize utility, opponent minimize. Alpha-beta pruning bỏ branches không thể ảnh hưởng quyết định (decision / 결정) cuối.

Thứ tự (ordering / 순서) moves tốt làm pruning mạnh hơn nhưng không đổi minimax kết quả (result / 결과).

Real games quá lớn nên cần heuristic evaluation, độ sâu (depth / 깊이) limit, Monte Carlo cây (tree / 트리) tìm kiếm (search / 검색) hoặc learned policies/giá trị (value / 값) functions.

> **Nối mạch:** **Planning** nối từ **Adversarial tìm kiếm (search / 검색)** sang **Utility và bất định (uncertainty / 불확실성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Planning

Planning khác simple đường dẫn (path / 경로) tìm kiếm (search / 검색) khi actions có preconditions/effects và goals gồm logical conditions. Classical planning có thể tìm kiếm (search / 검색) trong trạng thái (state / 상태) không gian (space / 공간) hoặc plan không gian (space / 공간).

Robotics/real-world planning thêm bất định (uncertainty / 불확실성), continuous trạng thái (state / 상태)/hành động (action / 동작) và partial khả năng quan sát (observability / 관측 가능성).

> **Nối mạch:** **Utility và bất định (uncertainty / 불확실성)** nối từ **Planning** sang **Reinforcement học tập (learning / 학습) liên kết (connection / 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Utility và bất định (uncertainty / 불확실성)

Khi outcomes stochastic, “đạt goal hay không” quá đơn giản. Expected utility kết hợp xác suất (probability / 확률) và preference/chi phí (cost / 비용).

Quyết định (decision / 결정) lý thuyết (theory / 이론) nối xác suất (probability / 확률) suy luận (inference / 추론) với hành động (action / 동작) selection.

> **Nối mạch:** **Reinforcement học tập (learning / 학습) liên kết (connection / 연결)** nối từ **Utility và bất định (uncertainty / 불확실성)** sang **Dùng chung (common / 공통) Misconceptions**, vì policy học phải được đọc cùng giả định và giới hạn.

## Reinforcement học tập (learning / 학습) liên kết (connection / 연결)

RL xem tác nhân (agent / 에이전트) tương tác môi trường (environment / 환경) và học chính sách (policy / 정책) từ rewards thay vì được cho chuyển tiếp (transition / 전이) mô hình (model / 모델) hoàn chỉnh. trạng thái (state / 상태), hành động (action / 동작), reward và chính sách (policy / 정책) vẫn dùng same tác nhân (agent / 에이전트) vocabulary.

Chapter ML/RL sâu hơn có thể thành thư viện (library / 라이브러리) riêng; ở đây trọng tâm là conceptual cầu nối (bridge / 브리지).

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Reinforcement học tập (learning / 학습) liên kết (connection / 연결)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“AI = neural mạng (network / 네트워크).”** tìm kiếm (search / 검색), lô-gic (logic / 논리), planning, probabilistic suy luận (inference / 추론) và tối ưu hóa (optimization / 최적화) đều là AI foundations lịch sử và hiện tại.

**“Heuristic chỉ là mẹo không có lý thuyết (theory / 이론).”** Nhiều heuristic tìm kiếm (search / 검색) algorithms có formal guarantees tùy thuộc tính (property / 속성) heuristic.

**“Rational tác nhân (agent / 에이전트) luôn chọn kết quả (outcome / 결과) tốt nhất thực tế.”** Nó chọn theo mô hình (model / 모델)/kiến thức (knowledge / 지식)/mục tiêu (objective / 목표) hiện có; bất định (uncertainty / 불확실성) có thể khiến kết quả (outcome / 결과) xấu.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> AI bắt đầu bằng việc formalize perception → trạng thái (state / 상태)/belief → hành động (action / 동작) → mục tiêu (objective / 목표). thuật toán (algorithm / 알고리즘) chỉ có ý nghĩa sau khi bài toán (problem / 문제) biểu diễn (representation / 표현) rõ.

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Xem [graph algorithms](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md), [complexity](../01_algorithms_data_structures/11_complexity_reductions_and_np.md), [probability](../../mathematics/06_probability_statistics/01_probability_foundations.md) và [ML foundations](./02_machine_learning_foundations.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
