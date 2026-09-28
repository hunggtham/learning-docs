# AI bài toán (problem / 문제) formulation, tìm kiếm (search / 검색) và agents

> **Mạch đọc:** Đặt **AI bài toán (problem / 문제) formulation, tìm kiếm (search / 검색) và agents** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **tác nhân (agent / 에이전트) mô hình (model / 모델)** sang **State-space tìm kiếm (search / 검색)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Artificial Intelligence (AI / 인공지능) rộng hơn machine học tập (learning / 학습). Một cách nhìn nền tảng là xây agents nhận observations, giữ/ước lượng trạng thái (state / 상태) và chọn actions để đạt objectives dưới bất định (uncertainty / 불확실성) và tài nguyên (resource / 자원) các ràng buộc (constraints / 제약조건들).

## Tác nhân (agent / 에이전트) mô hình (model / 모델)

Tác nhân (agent / 에이전트) nhận percepts từ môi trường (environment / 환경) và tạo actions. Rational tác nhân (agent / 에이전트) chọn hành động (action / 동작) expected to best satisfy hiệu năng (performance / 성능) measure dựa trên available thông tin (information / 정보), không nhất thiết “thông minh như người”.

Môi trường (environment / 환경) có thể fully/partially observable, deterministic/stochastic, episodic/sequential, static/động (dynamic / 동적), discrete/continuous.

Phân loại này quyết định thuật toán (algorithm / 알고리즘) family phù hợp.


> **Chuyển mạch:** Từ **tác nhân (agent / 에이전트) mô hình (model / 모델)**, ta sang **State-space tìm kiếm (search / 검색)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## State-space tìm kiếm (search / 검색)

Nhiều AI problems có thể biểu diễn bằng states, actions, chuyển tiếp (transition / 전이) mô hình (model / 모델), initial trạng thái (state / 상태) và goal kiểm thử (test / 테스트).

Đường dẫn (path / 경로) planning, puzzle, planning và game tìm kiếm (search / 검색) đều trở thành đồ thị (graph / 그래프) tìm kiếm (search / 검색) trên implicit trạng thái (state / 상태) không gian (space / 공간).

BFS tìm shortest đường dẫn (path / 경로) theo số edges khi costs bằng nhau; Dijkstra dùng non-negative costs; A* dùng heuristic để hướng tìm kiếm (search / 검색).


> **Chuyển mạch:** Từ **State-space tìm kiếm (search / 검색)**, ta sang **Heuristic** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Heuristic

Heuristic `h(n)` ước lượng remaining chi phí (cost / 비용) tới goal. A* dùng:

\[
f(n)=g(n)+h(n)
\]

với `g(n)` là chi phí (cost / 비용) đã đi.

Nếu heuristic admissible—không overestimate true remaining chi phí (cost / 비용)—A* có optimality guarantee dưới các giả định (assumptions / 가정들) phù hợp. Consistency giúp graph-search hành vi (behavior / 동작) tốt hơn.

Heuristic tốt encode lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) và giảm explored states.


> **Chuyển mạch:** Từ **Heuristic**, ta sang **tìm kiếm (search / 검색) explosion** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tìm kiếm (search / 검색) explosion

Branching factor `b` và độ sâu (depth / 깊이) `d` có thể tạo khoảng `b^d` states. Đây là combinatorial explosion; bộ nhớ (memory / 메모리) thường là bottleneck của BFS/A*.

AI tìm kiếm (search / 검색) vì vậy liên hệ trực tiếp độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론), approximation và heuristics.


> **Chuyển mạch:** Từ **tìm kiếm (search / 검색) explosion**, ta sang **Adversarial tìm kiếm (search / 검색)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Adversarial tìm kiếm (search / 검색)

Game hai người zero-sum có thể dùng minimax: player maximize utility, opponent minimize. Alpha-beta pruning bỏ branches không thể ảnh hưởng quyết định (decision / 결정) cuối.

Thứ tự (ordering / 순서) moves tốt làm pruning mạnh hơn nhưng không đổi minimax kết quả (result / 결과).

Real games quá lớn nên cần heuristic evaluation, độ sâu (depth / 깊이) limit, Monte Carlo cây (tree / 트리) tìm kiếm (search / 검색) hoặc learned policies/giá trị (value / 값) functions.


> **Chuyển mạch:** Từ **Adversarial tìm kiếm (search / 검색)**, ta sang **Planning** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Planning

Planning khác simple đường dẫn (path / 경로) tìm kiếm (search / 검색) khi actions có preconditions/effects và goals gồm logical conditions. Classical planning có thể tìm kiếm (search / 검색) trong trạng thái (state / 상태) không gian (space / 공간) hoặc plan không gian (space / 공간).

Robotics/real-world planning thêm bất định (uncertainty / 불확실성), continuous trạng thái (state / 상태)/hành động (action / 동작) và partial khả năng quan sát (observability / 관측 가능성).


> **Chuyển mạch:** Từ **Planning**, ta sang **Utility và bất định (uncertainty / 불확실성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Utility và bất định (uncertainty / 불확실성)

Khi outcomes stochastic, “đạt goal hay không” quá đơn giản. Expected utility kết hợp xác suất (probability / 확률) và preference/chi phí (cost / 비용).

Quyết định (decision / 결정) lý thuyết (theory / 이론) nối xác suất (probability / 확률) suy luận (inference / 추론) với hành động (action / 동작) selection.


> **Chuyển mạch:** Từ **Utility và bất định (uncertainty / 불확실성)**, ta sang **Reinforcement học tập (learning / 학습) liên kết (connection / 연결)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Reinforcement học tập (learning / 학습) liên kết (connection / 연결)

RL xem tác nhân (agent / 에이전트) tương tác môi trường (environment / 환경) và học chính sách (policy / 정책) từ rewards thay vì được cho chuyển tiếp (transition / 전이) mô hình (model / 모델) hoàn chỉnh. trạng thái (state / 상태), hành động (action / 동작), reward và chính sách (policy / 정책) vẫn dùng same tác nhân (agent / 에이전트) vocabulary.

Chapter ML/RL sâu hơn có thể thành thư viện (library / 라이브러리) riêng; ở đây trọng tâm là conceptual cầu nối (bridge / 브리지).


> **Chuyển mạch:** Từ **Reinforcement học tập (learning / 학습) liên kết (connection / 연결)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“AI = neural mạng (network / 네트워크).”** tìm kiếm (search / 검색), lô-gic (logic / 논리), planning, probabilistic suy luận (inference / 추론) và tối ưu hóa (optimization / 최적화) đều là AI foundations lịch sử và hiện tại.

**“Heuristic chỉ là mẹo không có lý thuyết (theory / 이론).”** Nhiều heuristic tìm kiếm (search / 검색) algorithms có formal guarantees tùy thuộc tính (property / 속성) heuristic.

**“Rational tác nhân (agent / 에이전트) luôn chọn kết quả (outcome / 결과) tốt nhất thực tế.”** Nó chọn theo mô hình (model / 모델)/kiến thức (knowledge / 지식)/mục tiêu (objective / 목표) hiện có; bất định (uncertainty / 불확실성) có thể khiến kết quả (outcome / 결과) xấu.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> AI bắt đầu bằng việc formalize perception → trạng thái (state / 상태)/belief → hành động (action / 동작) → mục tiêu (objective / 목표). thuật toán (algorithm / 알고리즘) chỉ có ý nghĩa sau khi bài toán (problem / 문제) biểu diễn (representation / 표현) rõ.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Xem [graph algorithms](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md), [complexity](../01_algorithms_data_structures/11_complexity_reductions_and_np.md), [probability](../../mathematics/06_probability_statistics/01_probability_foundations.md) và [ML foundations](./02_machine_learning_foundations.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 knowledge reasoning and probabilistic inference](./01_knowledge_reasoning_and_probabilistic_inference.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
