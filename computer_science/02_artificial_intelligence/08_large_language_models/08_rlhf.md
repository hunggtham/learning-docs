# Học tăng cường từ phản hồi con người (RLHF)

**Học tăng cường từ phản hồi con người (Reinforcement Learning from Human Feedback — RLHF / 인간 피드백 기반 강화학습)** là một nhóm phương pháp hậu huấn luyện dùng tín hiệu sở thích của con người để làm đầu ra của mô hình phù hợp hơn với hành vi mong muốn. Mục tiêu không phải “con người nói fact nào đúng rồi mô hình học thuộc”, mà thường là học **thứ tự ưu tiên (preference ordering)** giữa nhiều phản hồi ứng viên và dùng tín hiệu đó để cập nhật policy.

## Vì sao SFT chưa đủ?

SFT cần một phản hồi mục tiêu cụ thể. Tuy nhiên nhiều prompt có thể có nhiều câu trả lời đều chấp nhận được nhưng chất lượng khác nhau. Ta thường quan tâm những preference mềm như:

```text
phản hồi A hữu ích hơn B
A chính xác hơn B
A ít gây hại hơn B
A ngắn gọn và đúng trọng tâm hơn B
```

Dữ liệu xếp hạng của con người chứa thông tin mà việc bắt chước một target duy nhất không thể biểu diễn đầy đủ.

## Pipeline RLHF cổ điển

Một pipeline phổ biến gồm ba giai đoạn:

```text
1. có policy đã SFT
2. thu thập cặp preference → huấn luyện reward model
3. tối ưu policy theo reward model bằng RL
```

### Dữ liệu preference

Với prompt `x`, mô hình tạo các candidate `y_a`, `y_b`. Người đánh giá chọn phản hồi được ưu tiên:

\[
y_w \succ y_l
\]

trong đó `w` là phản hồi thắng và `l` là phản hồi thua.

### Mô hình phần thưởng

**Mô hình phần thưởng (reward model)** `r_\phi(x,y)` học một score sao cho câu trả lời được ưu tiên có reward cao hơn. Một objective thường gặp:

\[
\mathcal L_{RM}=-\log\sigma(r_\phi(x,y_w)-r_\phi(x,y_l))
\]

Reward model không phải “máy tiên tri về sự thật”. Nó chỉ xấp xỉ phân bố sở thích thể hiện trong dữ liệu annotation.

## Tối ưu policy

LLM đóng vai policy được tối ưu để tăng reward đã học. Nếu chỉ tối đa reward model một cách trực tiếp, policy có thể khai thác những điểm yếu của reward model. Vì vậy objective thường có thêm penalty giữ policy gần mô hình tham chiếu:

\[
\max_\theta \; \mathbb E[r_\phi(x,y)] - \beta D_{KL}(\pi_\theta\|\pi_{ref})
\]

Term KL hạn chế policy trôi quá xa khỏi mô hình tham chiếu vốn đã có chất lượng ngôn ngữ tốt.

## Trực giác về PPO

**Proximal Policy Optimization (PPO)** từng là thuật toán phổ biến cho RLHF. PPO hạn chế update quá lớn giữa policy mới và cũ để huấn luyện ổn định hơn.

Trong LLM, “hành động” là token được sinh và trajectory là cả chuỗi phản hồi. Reward thường đến ở cuối sequence hoặc từ một tín hiệu học được.

Điều này làm **gán công (credit assignment)** khó: một reward tổng cho cả câu trả lời không chỉ rõ token hoặc quyết định nào đã đóng góp bao nhiêu.

## Khai thác hàm thưởng

Nếu reward model có blind spot, policy có thể tìm đầu ra đạt score cao nhưng người thật không thực sự thích. Hiện tượng này gọi là **khai thác phần thưởng (reward hacking)** hoặc **chơi theo đặc tả (specification gaming)**.

Ví dụ nếu reward model vô tình liên hệ độ dài với sự hữu ích, policy có thể sinh câu trả lời dài không cần thiết để lấy reward cao.

Bài học chung của tối ưu hóa là:

> Optimizer sẽ tối ưu đại lượng được cung cấp, không phải mục tiêu chỉ tồn tại trong ý định của người thiết kế.

## Sở thích không đồng nghĩa sự thật

Người đánh giá có thể bất đồng, thiếu chuyên môn hoặc bị ảnh hưởng bởi cách diễn đạt. Reward model phản ánh cả quy trình annotation.

Do đó RLHF có thể cải thiện helpfulness, phong cách hoặc xu hướng thừa nhận giới hạn, nhưng không bảo đảm factual correctness.

Grounding, retrieval và verification vẫn cần thiết.

## Thiết kế hướng dẫn annotation

Hướng dẫn preference ảnh hưởng hành vi mô hình rất mạnh. Nếu labeler được yêu cầu ưu tiên phản hồi ngắn gọn, mô hình sẽ học preference đó. Nếu policy an toàn mơ hồ, nhãn có thể thiếu nhất quán.

Mức bất đồng giữa người gán nhãn là thông tin hữu ích: tác vụ có thể mang tính chủ quan hoặc guideline chưa đủ rõ.

## Helpful, Honest, Harmless là bài toán đa mục tiêu

Một trợ lý thường phải cân bằng nhiều objective. Tính hữu ích và vô hại đôi khi xung đột; tính trung thực có thể yêu cầu mô hình thừa nhận không chắc chắn thay vì trả lời dứt khoát.

Không có một scalar reward hoàn hảo biểu diễn mọi giá trị. Hệ thống thực tế thường dùng mixture dữ liệu, policy riêng và nhiều bộ đánh giá độc lập.

## Tối ưu preference online và offline

RLHF cổ điển có thể cho policy liên tục sinh trajectory mới trong vòng lặp huấn luyện, nên phân bố dữ liệu thay đổi theo policy. Đây gần với thiết lập online hoặc on-policy.

Các phương pháp như DPO có thể tối ưu trực tiếp trên cặp preference offline mà không cần reward model tách riêng và vòng PPO đầy đủ.

Xem tiếp: [Preference Optimization and DPO](./09_preference_optimization_and_dpo.md).

## RLHF và an toàn

Dữ liệu preference về safety có thể dạy từ chối, phản hồi an toàn và tuân thủ policy. Tuy nhiên mô hình vẫn có thể bị jailbreak vì dữ liệu huấn luyện không thể bao phủ mọi prompt đối kháng.

Defense ở runtime, filter đầu vào/đầu ra, ranh giới quyền của tool và red teaming vẫn là các lớp hệ thống bổ sung.

## KL penalty như ràng buộc ổn định

Nếu tối ưu reward quá mạnh, mô hình có thể mất độ trôi chảy hoặc hội tụ về đầu ra kỳ lạ nhưng reward cao. KL penalty giữ phân bố gần reference.

`β` lớn làm policy bảo thủ hơn; `β` nhỏ cho phép policy di chuyển mạnh hơn theo reward.

Đây là một đánh đổi giống **trust region** giữa cải thiện reward và giữ hành vi nền.

## Tối ưu quá mức reward model

Khi policy ngày càng tối ưu mạnh đối với một reward model cố định, preference thật của con người có thể tăng ở giai đoạn đầu rồi giảm khi policy bắt đầu khai thác sai số của reward model.

Vì vậy reward-model score không nên là metric duy nhất sau huấn luyện.

## Mô hình tư duy

```text
Sở thích con người
      ↓
tín hiệu preference được học
      ↓
tối ưu policy
      ↓
hành vi trợ lý thay đổi
```

RLHF là **điều chỉnh hành vi dưới phép đo preference không hoàn hảo**, không phải “nạp toàn bộ giá trị con người vào mô hình”.

## Những hiểu lầm thường gặp

### “RLHF làm mô hình biết fact đúng hơn”

Nó có thể gián tiếp cải thiện sự trung thực, nhưng tri thức factual chủ yếu đến từ pretraining và retrieval; reward optimization không biến preference label thành world model đầy đủ.

### “Reward model chính là phán đoán của con người”

Không. Nó là một mô hình xấp xỉ có bias và error.

### “RLHF = PPO”

PPO chỉ là một lựa chọn tối ưu. RLHF là khái niệm rộng hơn và có nhiều phương pháp preference optimization khác.

## Liên kết kiến thức

RLHF ứng dụng các ý tưởng của [Reinforcement Learning](../11_reinforcement_learning/00_reinforcement_learning_foundations.md) và [Optimization](../01_mathematical_foundations/06_optimization.md), nhưng hậu huấn luyện LLM có cấu trúc riêng vì action space là chuỗi token và reward được học từ preference.

Xem tiếp: [DPO](./09_preference_optimization_and_dpo.md).