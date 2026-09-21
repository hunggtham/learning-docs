# Nền tảng Reinforcement Learning

**Học tăng cường (Reinforcement Learning — RL / 강화학습)** nghiên cứu cách một agent học cách hành động thông qua tương tác (interaction) với môi trường (environment) để tối đa hóa reward tích lũy theo thời gian. Khác với supervised learning, agent thường không nhận “đáp án đúng” cho từng action; nó quan sát consequence và reward, đôi khi reward chỉ xuất hiện sau nhiều bước.

```text
state s_t
→ agent chọn action a_t
→ environment chuyển sang s_{t+1}
→ nhận reward r_{t+1}
→ lặp lại
```

## Vì sao RL khác Supervised Learning?

Supervised learning thường có dataset tương đối cố định gồm các cặp `(x,y)`. RL khó hơn ở ba điểm quan trọng:

1. phân phối dữ liệu phụ thuộc policy hiện tại;
2. reward có thể bị trì hoãn nhiều bước;
3. agent phải cân bằng exploration và exploitation.

Nếu agent chọn action khác, nó sẽ đi qua trajectory khác và quan sát dữ liệu khác. Vì vậy data collection và learning không còn tách biệt hoàn toàn.

## Reward và Return

Reward `r_t` là tín hiệu phản hồi tại một thời điểm. Objective thường không tối ưu một reward đơn lẻ mà tối ưu **return chiết khấu kỳ vọng (expected discounted return)**:

\[
G_t = r_{t+1}+\gamma r_{t+2}+\gamma^2 r_{t+3}+\cdots
\]

với **hệ số chiết khấu (discount factor)**:

\[
0\le \gamma <1
\]

`γ` điều khiển mức agent coi trọng reward gần so với reward xa. Trong nhiều bài toán horizon vô hạn, discount cũng giúp tổng reward hội tụ.

## Policy

**Policy (정책 / chính sách hành động)** mô tả cách agent chọn action tại một state:

\[
\pi(a\mid s)
\]

Policy xác định có thể viết `a=π(s)`. Policy ngẫu nhiên (stochastic policy) trả về một distribution trên các action.

Policy là thành phần trung tâm vì mục tiêu cuối cùng của RL thường là tìm policy tạo return tốt.

## Value

**State-value function**:

\[
V^\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s]
\]

đo return kỳ vọng nếu đang ở state `s` và tiếp tục làm theo policy `π`.

**Action-value function**:

\[
Q^\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a]
\]

đo return kỳ vọng khi chọn action `a` tại state `s`, sau đó tiếp tục theo policy `π`.

Value không phải immediate reward. Nó ước lượng **hệ quả dài hạn (long-term consequence)**.

## Model-Free và Model-Based RL

**Model-based RL** sử dụng hoặc học một model của environment, chẳng hạn transition và reward, rồi dùng model đó để planning.

**Model-free RL** học value hoặc policy trực tiếp từ experience mà không cần một explicit environment model.

Hai hướng này không loại trừ nhau. Một hệ thống có thể học model để planning nhưng vẫn dùng learned policy hoặc value function để ra quyết định.

## Exploration và Exploitation

Agent phải cân bằng hai mục tiêu:

- **khai thác (exploitation)**: dùng action hiện được ước lượng là tốt nhất;
- **khám phá (exploration)**: thử action để thu thêm thông tin.

Nếu chỉ exploit quá sớm, agent có thể mắc kẹt ở policy chưa tối ưu.

Một strategy đơn giản là **epsilon-greedy**:

```text
với xác suất ε: chọn action ngẫu nhiên
ngược lại: chọn argmax Q(s,a)
```

Đây là baseline dễ hiểu, không phải chiến lược exploration tốt nhất cho mọi bài toán.

## On-Policy và Off-Policy

**On-policy learning** học về chính policy đang tạo ra dữ liệu.

**Off-policy learning** có thể học một target policy khác với behavior policy đang tương tác với environment.

Q-learning là ví dụ kinh điển của off-policy method, trong khi SARSA là on-policy.

Sự phân biệt này quan trọng vì nó ảnh hưởng cách sử dụng dữ liệu cũ, replay buffer và khả năng học từ behavior khác policy mục tiêu.

## Credit Assignment

Nếu reward tốt chỉ xuất hiện ở cuối một episode dài, action nào ở trước đó thực sự xứng đáng nhận credit?

Đây là **bài toán gán công trạng theo thời gian (temporal credit assignment)**.

Bellman equation, Temporal-Difference learning và policy gradient cung cấp các cách khác nhau để truyền tín hiệu reward ngược về các decision trước đó.

## Reward Specification

Reward chỉ là một **đại diện toán học (proxy)** cho mục tiêu thực. Nếu proxy được thiết kế sai, agent có thể tối ưu một hành vi không mong muốn — hiện tượng thường gọi là **reward hacking** hoặc **specification gaming**.

Ví dụ robot được reward cho “di chuyển nhanh” nhưng không bị phạt khi va chạm có thể học cách di chuyển nguy hiểm.

Bài học tổng quát:

> Optimizer tối ưu metric được định nghĩa, không tự hiểu ý định chưa được mã hóa của designer.

## Sparse Reward

Nếu reward chỉ xuất hiện ở cuối một task dài, learning signal rất yếu. **Reward shaping** thêm intermediate reward để learning dễ hơn.

Tuy nhiên shaping có thể làm lệch objective nếu reward phụ không thật sự phù hợp mục tiêu cuối.

## Episode và Continuing Task

**Episodic task** có terminal state rõ, ví dụ một ván game kết thúc.

**Continuing task** chạy liên tục, ví dụ process control hoặc resource allocation lâu dài.

Cách định nghĩa return, termination và evaluation có thể khác giữa hai loại.

## Partial Observability

Nếu observation hiện tại không đủ để xác định true state, bài toán gần với **Partially Observable Markov Decision Process (POMDP)**.

Agent khi đó có thể cần memory, recurrent state hoặc belief state để tổng hợp information từ nhiều bước trước.

## Offline RL

**Offline RL** hoặc **batch RL** học từ một fixed logged dataset mà không được tiếp tục exploration trong environment.

Điểm khó là policy mới có thể chọn action nằm ngoài vùng được data hỗ trợ. Value function khi đó phải extrapolate sang vùng không có evidence và có thể trở nên rất không đáng tin.

Offline RL vì vậy đặc biệt nhạy với distribution shift và coverage của behavior data.

## RL và LLM Alignment

RL xuất hiện trong post-training của LLM, ví dụ RLHF. Tuy nhiên LLM alignment có cấu trúc riêng:

- action có thể là token hoặc cả sequence;
- reward có thể đến từ human preference hoặc reward model;
- reference-policy constraint thường quan trọng;
- environment khác đáng kể so với robot hoặc game cổ điển.

Không nên đồng nhất toàn bộ Reinforcement Learning với RLHF.

## Mô hình tư duy

> **Supervised learning hỏi “output nào đúng cho input này?”, còn RL hỏi “chuỗi action nào dẫn tới hệ quả dài hạn tốt?”**

## Những nhầm lẫn thường gặp

### “Reward chính là mục tiêu thật”

Không. Reward là encoded objective. Nếu encoding thiếu, optimizer có thể khai thác khoảng trống giữa reward và ý định thật.

### “RL luôn cần robot hoặc game”

Không. RL áp dụng cho mọi sequential decision problem có feedback phù hợp.

### “Exploration càng nhiều càng tốt”

Không. Exploration có chi phí và rủi ro; real-world system thường cần **safe exploration**.

## Liên kết kiến thức

RL nối [Agents](../10_agents_and_ai_systems/00_from_llm_to_agent.md), [Decision Making Under Uncertainty](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md), Probability và Optimization.

Xem tiếp: [Markov Decision Process](./01_markov_decision_processes.md).