# Markov quyết định (decision / 결정) Processes

> **Mạch đọc:** Đặt **Markov quyết định (decision / 결정) Processes** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Markov thuộc tính (property / 속성)** sang **chuyển tiếp (transition / 전이) mô hình (model / 모델)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Markov quyết định (decision / 결정) tiến trình (process / 프로세스)** là mathematical khung phần mềm (framework / 프레임워크) cho sequential quyết định (decision / 결정) making khi trạng thái (state / 상태) hiện tại chứa đủ thông tin (information / 정보) relevant để predict future dynamics dưới hành động (action / 동작).

Một MDP thường được mô tả bởi tuple:

\[
(\mathcal S,\mathcal A,P,R,\gamma)
\]

trong đó:

- `S`: trạng thái (state / 상태) không gian (space / 공간);
- `A`: hành động (action / 동작) không gian (space / 공간);
- `P(s'|s,a)`: chuyển tiếp (transition / 전이) phân phối (distribution / 분포);
- `R(s,a,s')`: reward;
- `γ`: discount factor.

## Markov thuộc tính (property / 속성)

Markov giả định (assumption / 가정):

\[
P(S_{t+1}\mid S_t,A_t,S_{t-1},...) = P(S_{t+1}\mid S_t,A_t)
\]

Nghĩa là nếu trạng thái (state / 상태) biểu diễn (representation / 표현) đầy đủ, quá khứ không cung cấp thêm thông tin (information / 정보) cần cho next chuyển tiếp (transition / 전이).

Điều này là giả định (assumption / 가정) về **biểu diễn (representation / 표현)**, không phải world “không có lịch sử (history / 이력)”. Nếu trạng thái (state / 상태) thiếu thông tin, Markov thuộc tính (property / 속성) thất bại (fail / 실패).

Ví dụ game board hiện tại có thể đủ để quyết định legal moves. Nhưng người dùng (user / 사용자) conversation chỉ giữ latest message thường không đủ trạng thái (state / 상태).

## Chuyển tiếp (transition / 전이) mô hình (model / 모델)

`P(s'|s,a)` nói môi trường (environment / 환경) có thể chuyển sang đâu sau hành động (action / 동작).

Deterministic trường hợp (case / 사례):

\[
s'=T(s,a)
\]

Stochastic trường hợp (case / 사례) cần phân phối (distribution / 분포).

Ví dụ autonomous vehicle braking có kết quả (outcome / 결과) phụ thuộc road điều kiện (condition / 조건), sensor bất định (uncertainty / 불확실성) và other actors.

## Reward hàm (function / 함수)

Reward có thể depend on trạng thái (state / 상태)/hành động (action / 동작)/next trạng thái (state / 상태). mục tiêu (objective / 목표) không phải maximize immediate reward mà expected return.

Một choice reward khác có thể tạo chính sách (policy / 정책) hoàn toàn khác dù dynamics giống nhau.

## Chính sách (policy / 정책)

Chính sách (policy / 정책):

\[
\pi(a|s)
\]

induces a Markov chuỗi (chain / 사슬) over states. Khi chính sách (policy / 정책) fixed, quyết định (decision / 결정) bài toán (problem / 문제) biến thành chính sách (policy / 정책) evaluation bài toán (problem / 문제).

## Trajectory xác suất (probability / 확률)

Một trajectory:

\[
\tau=(s_0,a_0,r_1,s_1,a_1,...)
\]

có xác suất (probability / 확률) phụ thuộc initial trạng thái (state / 상태), chính sách (policy / 정책) và chuyển tiếp (transition / 전이) dynamics:

\[
P(\tau)=P(s_0)\prod_t \pi(a_t|s_t)P(s_{t+1}|s_t,a_t)
\]

Expression này giải thích tại sao chính sách (policy / 정책) ảnh hưởng phân phối (distribution / 분포) dữ liệu (data / 데이터) tác nhân (agent / 에이전트) thu được.

## Finite Horizon và Infinite Horizon

Finite-horizon bài toán (problem / 문제) có số bước giới hạn `T`. Optimal chính sách (policy / 정책) có thể depend on thời gian (time / 시간) remaining.

Infinite-horizon discounted bài toán (problem / 문제) thường tìm stationary chính sách (policy / 정책) dưới các giả định (assumptions / 가정들) thích hợp.

## Terminal trạng thái (state / 상태)

Terminal/absorbing trạng thái (state / 상태) có thể kết thúc episode. Sau terminal không có meaningful future actions/rewards.

## MDP và Planning

Nếu `P` và `R` biết rõ, ta có thể solve MDP bằng động (dynamic / 동적) Programming như giá trị (value / 값) iteration/chính sách (policy / 정책) iteration.

Nếu unknown, RL học từ samples.

Do đó:

```text
Known model + optimize policy → planning/control
Unknown model + experience → reinforcement learning
```

Ranh giới (boundary / 경계) này mềm vì model-based RL có thể học mô hình (model / 모델) rồi plan.

## POMDP

Khi tác nhân (agent / 에이전트) không observe full trạng thái (state / 상태), ta có **Partially Observable MDP (POMDP)**. tác nhân (agent / 에이전트) nhận observation `o_t`, không trực tiếp trạng thái (state / 상태) `s_t`.

Có thể maintain belief:

\[
b_t(s)=P(S_t=s\mid history)
\]

Belief trạng thái (state / 상태) biến bất định (uncertainty / 불확실성) về hidden trạng thái (state / 상태) thành trạng thái (state / 상태) biểu diễn (representation / 표현) mới.

## Trạng thái (state / 상태) thiết kế (design / 설계)

Trạng thái (state / 상태) quá nhỏ → non-Markov, tác nhân (agent / 에이전트) khó learn.

Trạng thái (state / 상태) quá lớn → mẫu (sample / 표본) độ phức tạp (complexity / 복잡도) và computation tăng.

Biểu diễn (representation / 표현) học tập (learning / 학습) trong RL tìm trạng thái (state / 상태) features giữ decision-relevant thông tin (information / 정보).

## Hành động (action / 동작) Granularity

Hành động (action / 동작) không gian (space / 공간) cũng là thiết kế (design / 설계) choice. Low-level continuous actions cho điều khiển (control / 제어) chính xác nhưng horizon dài. High-level actions reduce horizon nhưng cần lớp trừu tượng (abstraction / 추상화)/mô hình (model / 모델).

Tác nhân (agent / 에이전트) tools trong LLM các hệ thống (systems / 시스템들) cũng có analogy: `click(x,y)` low-level vs `create_ticket(...)` high-level.

## Discount Factor Interpretation

`γ` có thể hiểu như:

- preference for sooner reward;
- effective horizon;
- mathematical thiết bị (device / 장치) for convergence;
- probability-like continuation interpretation trong một số settings.

Effective horizon roughly grows as `1/(1-γ)` khi γ gần 1, nhưng đây chỉ intuition.

## Reward quy mô (scale / 규모)

Quy mô (scale / 규모) reward ảnh hưởng numerical tối ưu hóa (optimization / 최적화) và hyperparameters dù optimal chính sách (policy / 정책) lý tưởng có thể bất biến (invariant / 불변식) với positive scaling trong một số settings.

## Mô hình tư duy (mental model / 사고 모델)

> **MDP là state-machine có bất định (uncertainty / 불확실성) + rewards + choices. RL học cách điều khiển state-machine đó khi dynamics hoặc optimal chính sách (policy / 정책) chưa biết.**

## Dùng chung (common / 공통) Misconceptions

### “Markov nghĩa là random”

Không. Markov nói future conditionally independent of past given present trạng thái (state / 상태); chuyển tiếp (transition / 전이) có thể deterministic.

### “trạng thái (state / 상태) = observation”

Chỉ đúng trong fully observable setting.

### “MDP chỉ là lý thuyết cho game”

Nó là foundation cho robotics, operations, recommendation, tài nguyên (resource / 자원) allocation và sequential điều khiển (control / 제어).

## Liên kết kiến thức (knowledge connection / 지식 연결)

MDP nối xác suất (probability / 확률), động (dynamic / 동적) Programming, điều khiển (control / 제어) lý thuyết (theory / 이론) và tác nhân (agent / 에이전트) trạng thái (state / 상태) biểu diễn (representation / 표현).

Xem tiếp: [Value Functions and Bellman Equations](./02_value_functions_and_bellman_equations.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 reinforcement learning foundations](./00_reinforcement_learning_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
