# AI problem formulation, search và agents

Artificial Intelligence (AI / 인공지능) rộng hơn machine learning. Một cách nhìn nền tảng là xây agents nhận observations, giữ/ước lượng state và chọn actions để đạt objectives dưới uncertainty và resource constraints.

## Agent model

Agent nhận percepts từ environment và tạo actions. Rational agent chọn action expected to best satisfy performance measure dựa trên available information, không nhất thiết “thông minh như người”.

Environment có thể fully/partially observable, deterministic/stochastic, episodic/sequential, static/dynamic, discrete/continuous.

Phân loại này quyết định algorithm family phù hợp.

## State-space search

Nhiều AI problems có thể biểu diễn bằng states, actions, transition model, initial state và goal test.

Path planning, puzzle, planning và game search đều trở thành graph search trên implicit state space.

BFS tìm shortest path theo số edges khi costs bằng nhau; Dijkstra dùng non-negative costs; A* dùng heuristic để hướng search.

## Heuristic

Heuristic `h(n)` ước lượng remaining cost tới goal. A* dùng:

\[
f(n)=g(n)+h(n)
\]

với `g(n)` là cost đã đi.

Nếu heuristic admissible—không overestimate true remaining cost—A* có optimality guarantee dưới assumptions phù hợp. Consistency giúp graph-search behavior tốt hơn.

Heuristic tốt encode domain knowledge và giảm explored states.

## Search explosion

Branching factor `b` và depth `d` có thể tạo khoảng `b^d` states. Đây là combinatorial explosion; memory thường là bottleneck của BFS/A*.

AI search vì vậy liên hệ trực tiếp complexity theory, approximation và heuristics.

## Adversarial search

Game hai người zero-sum có thể dùng minimax: player maximize utility, opponent minimize. Alpha-beta pruning bỏ branches không thể ảnh hưởng decision cuối.

Ordering moves tốt làm pruning mạnh hơn nhưng không đổi minimax result.

Real games quá lớn nên cần heuristic evaluation, depth limit, Monte Carlo Tree Search hoặc learned policies/value functions.

## Planning

Planning khác simple path search khi actions có preconditions/effects và goals gồm logical conditions. Classical planning có thể search trong state space hoặc plan space.

Robotics/real-world planning thêm uncertainty, continuous state/action và partial observability.

## Utility và uncertainty

Khi outcomes stochastic, “đạt goal hay không” quá đơn giản. Expected utility kết hợp probability và preference/cost.

Decision theory nối probability inference với action selection.

## Reinforcement learning connection

RL xem agent tương tác environment và học policy từ rewards thay vì được cho transition model hoàn chỉnh. State, action, reward và policy vẫn dùng same agent vocabulary.

Chapter ML/RL sâu hơn có thể thành library riêng; ở đây trọng tâm là conceptual bridge.

## Common Misconceptions

**“AI = neural network.”** Search, logic, planning, probabilistic inference và optimization đều là AI foundations lịch sử và hiện tại.

**“Heuristic chỉ là mẹo không có theory.”** Nhiều heuristic search algorithms có formal guarantees tùy property heuristic.

**“Rational agent luôn chọn outcome tốt nhất thực tế.”** Nó chọn theo model/knowledge/objective hiện có; uncertainty có thể khiến outcome xấu.

## Mental Model

> AI bắt đầu bằng việc formalize perception → state/belief → action → objective. Algorithm chỉ có ý nghĩa sau khi problem representation rõ.

## Kết nối

Xem [graph algorithms](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md), [complexity](../01_algorithms_data_structures/11_complexity_reductions_and_np.md), [probability](../../../mathematics/06_probability_statistics/01_probability_foundations.md) và [ML foundations](./02_machine_learning_foundations.md).