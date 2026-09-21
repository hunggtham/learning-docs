# Deep Reinforcement Learning

**Deep Reinforcement Learning (Deep RL / 심층 강화학습)** kết hợp Reinforcement Learning với neural network để xử lý state hoặc action space quá lớn cho tabular method. Neural network có thể đóng vai trò function approximator cho value, Q-function, policy hoặc environment model.

```text
pixel / sensor / embedding
        ↓
biểu diễn neural
        ↓
Q-value / policy / value / model
        ↓
RL objective
```

## Vì sao Deep RL khó hơn Supervised Deep Learning?

Supervised learning thường train trên dataset tương đối stationary. Trong RL:

- policy thay đổi → phân phối dữ liệu thay đổi;
- target có thể bootstrap từ chính network;
- reward có thể delayed hoặc sparse;
- exploration quyết định data nào sẽ xuất hiện trong tương lai;
- sample liên tiếp có temporal correlation;
- objective và target distribution liên tục thay đổi.

Vì vậy tăng capacity của neural network không tự giải quyết bài toán RL; function approximation còn tạo thêm vấn đề stability mới.

## DQN: Deep Q-Network

DQN xấp xỉ:

\[
Q(s,a;\theta)
\]

bằng neural network. Input có thể là image hoặc feature vector, output là Q-value cho từng discrete action.

Ba ý tưởng engineering quan trọng:

1. **experience replay**;
2. **target network**;
3. ổn định reward, gradient và optimization.

Loss cơ bản:

\[
L(\theta)=\mathbb E[(r+\gamma\max_{a'}Q(s',a';\theta^-)-Q(s,a;\theta))^2]
\]

## Vì sao Experience Replay quan trọng?

Các state hoặc frame liên tiếp thường tương quan rất mạnh. Nếu SGD train trực tiếp trên sequence liên tiếp, mini-batch có ít diversity và gradient noisy theo trajectory hiện tại.

Replay buffer giúp:

```text
lưu transition lịch sử
→ sample ngẫu nhiên mini-batch
→ phá bớt temporal correlation
→ tái sử dụng experience
```

**Prioritized Experience Replay** sample transition có TD error lớn thường xuyên hơn, nhưng cần correction để giảm sampling bias.

## Target Network

Nếu cùng một network vừa tạo target vừa bị update mỗi gradient step, ta gặp **moving target problem**:

```text
network thay đổi
→ target thay đổi
→ network liên tục đuổi theo prediction của chính nó
```

Một target network được freeze hoặc update chậm giúp giảm feedback instability.

## Double DQN

Double DQN giảm overestimation bằng cách dùng online network để chọn action nhưng target network để evaluate action đó:

\[
a^*=\arg\max_a Q(s',a;\theta)
\]

\[
y=r+\gamma Q(s',a^*;\theta^-)
\]

Selection và evaluation được tách ra nên positive noise ít bị khuếch đại hơn.

## Dueling Network

Dueling architecture phân rã:

\[
Q(s,a)=V(s)+A(s,a)
\]

kèm normalization để decomposition có thể xác định.

Ý tưởng hữu ích khi nhiều action tại một state có effect tương tự: network có thể học state value chung trước rồi học phần difference giữa các action.

## Policy-Based Deep RL

Policy network trực tiếp output action distribution hoặc parameter của action distribution.

PPO, SAC và nhiều actor–critic method phù hợp tự nhiên với continuous hoặc high-dimensional action space hơn Q-table hoặc discrete argmax.

## Representation Learning trong RL

Deep RL agent không chỉ học control mà còn phải học representation của state.

Nếu reward sparse, signal để học representation cũng rất yếu. Vì vậy auxiliary objective hoặc self-supervised objective có thể được dùng để học feature về dynamics, object hoặc temporal structure trước hoặc cùng RL objective.

## World Model

Model-based Deep RL có thể học dynamics:

\[
\hat s_{t+1}=f_\phi(s_t,a_t)
\]

hoặc latent dynamics, sau đó planning hoặc improve policy trên model đã học.

Lợi ích lớn là potential sample efficiency vì model có thể “tưởng tượng” nhiều transition mà không cần tương tác thật.

Rủi ro là **model bias**: nếu learned model sai, planner có thể khai thác chính lỗi của model, đặc biệt khi đi xa khỏi training distribution.

## Imagination và Latent Planning

Thay vì simulate raw pixel, world-model agent có thể học latent state `z_t`, rồi dự đoán latent transition và reward.

Planning trong latent space rẻ hơn nếu representation giữ đúng information cần cho control.

Nếu latent representation bỏ mất một factor quan trọng, imagined trajectory có thể trông hợp lý nhưng dẫn tới policy sai trong environment thật.

## Exploration trong Không gian lớn

Random action exploration thường rất kém hiệu quả khi reward sparse và state space lớn.

Các hướng phổ biến gồm:

- intrinsic motivation;
- curiosity hoặc prediction error;
- count / pseudo-count bonus;
- entropy maximization;
- uncertainty-driven exploration.

Tuy nhiên intrinsic reward cũng có thể bị exploit. Ví dụ agent có thể tìm một nguồn noise khó dự đoán rồi ở đó mãi vì curiosity reward cao.

## Sparse Reward và Hindsight

**Hindsight Experience Replay (HER)** relabel một failed trajectory bằng goal mà agent thực sự đã đạt được.

Ví dụ robot cố đưa object tới A nhưng cuối cùng tới B. Thay vì bỏ trajectory, ta có thể học rằng trajectory đó là successful experience cho goal B.

HER đặc biệt hữu ích cho goal-conditioned task.

## Distribution Shift

Khi policy được cải thiện, agent bắt đầu tới những state mới. Function approximator có thể chưa từng thấy vùng đó nên prediction kém.

Prediction sai lại dẫn policy tới distribution mới hơn nữa. Đây là feedback loop rất đặc trưng của RL và là nguồn instability quan trọng.

## Sim-to-Real

Robotics thường train trong simulation rồi deploy lên physical system. Difference giữa simulator và thực tế tạo **sim-to-real gap**.

Các kỹ thuật giảm gap gồm:

- domain randomization;
- system identification;
- fine-tuning bằng real data;
- safety constraint;
- robust control.

Simulation success không tự động bảo đảm real-world success.

## Offline Deep RL

Offline Deep RL học hoàn toàn từ logged data có sẵn.

Thách thức lớn nhất là policy mới có thể chọn out-of-distribution action mà dataset không support. Q-value của những action này dễ chỉ là extrapolation error.

Offline RL method thường cố:

```text
giữ policy gần data support
hoặc
học conservative value estimate
```

để tránh khai thác vùng không có evidence.

## Safe RL

Một số bài toán không thể chỉ tối đa hóa reward mà còn có constraint:

\[
\max_\pi \mathbb E[G] \quad \text{s.t.}\quad \mathbb E[C_i]\le d_i
\]

Trong đó `C_i` là cost hoặc risk signal.

Real-world system không thể exploration tự do qua catastrophic action chỉ để học rằng action đó nguy hiểm.

## Multi-Agent Deep RL

Khi nhiều agent cùng học, environment trở thành non-stationary từ góc nhìn từng agent vì policy của các agent khác cũng thay đổi.

Một strategy phổ biến là **centralized training, decentralized execution**: training critic có nhiều global information hơn, nhưng khi deploy mỗi actor chỉ dùng local observation.

## Đánh giá Deep RL

Một training run với một random seed không đủ đáng tin vì variance có thể rất lớn.

Cần nhiều seed và uncertainty estimate. Nên report ít nhất:

- sample efficiency;
- final return;
- stability;
- compute hoặc environment step;
- safety violation;
- generalization sang environment thay đổi.

## Reward Hacking

Optimizer mạnh sẽ tìm loophole trong reward nếu environment cho phép.

Ví dụ agent được reward mỗi lần chạm checkpoint và tìm ra vòng lặp để trigger checkpoint liên tục mà không hoàn thành mục tiêu thật.

Đây là **specification problem**, không phải “agent có ý xấu”.

## Deep RL và Game

Game là research environment tốt vì rules, reward và simulator rõ, rẻ và reset được.

Nhưng success trong game không tự chuyển sang open-world domain nơi state, reward và objective mơ hồ hơn rất nhiều.

## RLHF và LLM Post-Training

Một số kỹ thuật Deep RL như PPO đã được dùng cho LLM alignment. Nhưng LLM setting có nhiều điểm khác:

- action là token hoặc token sequence;
- pretrained policy đã có capability rất mạnh;
- reward model thường học từ preference;
- KL/reference constraint giúp policy không drift quá xa SFT/base model;
- environment thường là preference process chứ không phải physics simulator.

Modern preference optimization có thể không cần full RL loop trong một số pipeline, nhưng RL vẫn cung cấp mental model quan trọng cho policy optimization.

## Deadly Triad một lần nữa

Deep RL thường kết hợp:

```text
function approximation
+ bootstrapping
+ off-policy data
```

Do đó replay buffer, target network, double estimator và stabilization không phải các “hack phụ”; chúng xử lý structural instability của bài toán.

## Compute và Reproducibility

Deep RL result phụ thuộc mạnh vào:

```text
random seed
environment version
wrapper
reward preprocessing
observation preprocessing
evaluation policy
```

Muốn reproducibility, phải version toàn environment pipeline chứ không chỉ model code.

## Mô hình tư duy

> **Deep RL không chỉ là “neural network + reward”; nó là một feedback system nơi policy quyết định chính dữ liệu mà model sẽ thấy tiếp theo.**

Đây là khác biệt sâu so với ordinary supervised learning.

## Những nhầm lẫn thường gặp

### “Deep RL là con đường chung để tạo intelligence”

Không. Nó rất mạnh cho sequential decision problem nhưng sample cost, reward specification và safety khiến nhiều task phù hợp hơn với supervised learning, planning hoặc normal software.

### “Simulation thành công nghĩa là real-world thành công”

Không. Sim-to-real gap có thể rất lớn.

### “Reward cao chứng minh behavior tốt”

Chỉ khi reward thực sự đo đúng intended behavior và environment không có loophole quan trọng.

### “Neural network lớn hơn sẽ sửa RL instability”

Không. Data-feedback loop, off-policy shift và bootstrapping instability vẫn tồn tại.

## Liên kết kiến thức

Deep RL nối [Neural Networks](../05_neural_networks/README.md), MDP/Bellman theory, Optimization, Agents và Safety. Đây là điểm kết thúc nền tảng RL; các layer Safety/Alignment phía sau sẽ quay lại reward specification, policy constraint và evaluation.