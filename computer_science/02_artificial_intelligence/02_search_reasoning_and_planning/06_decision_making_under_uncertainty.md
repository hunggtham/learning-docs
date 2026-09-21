# Ra quyết định dưới bất định

Tìm kiếm cổ điển và lập kế hoạch xác định thường giả định hành động dẫn tới trạng thái kế tiếp khá rõ ràng. Thế giới thực hiếm khi như vậy. Cảm biến có nhiễu, hành động có thể thất bại, hành vi người dùng mang tính ngẫu nhiên, nhu cầu tương lai chưa biết và ta thường không quan sát đầy đủ trạng thái ẩn.

**Ra quyết định dưới bất định (Decision Making Under Uncertainty / 불확실성 하의 의사결정)** đặt câu hỏi:

> Khi không biết chắc trạng thái hoặc kết quả, nên chọn hành động nào nếu mỗi kết quả có xác suất và hậu quả khác nhau?

Đây là nơi xác suất, độ hữu dụng, lập kế hoạch và học tăng cường bắt đầu gặp nhau.

Xem trước: [Xác suất cho AI](../01_mathematical_foundations/02_probability_for_ai.md) và [Lập kế hoạch](./05_planning.md).

## Xác suất chưa đủ để ra quyết định

Giả sử mô hình dự đoán:

\[
P(fraud\mid x)=0.20
\]

Có nên chặn giao dịch không?

Chỉ xác suất chưa đủ để trả lời. Cần biết chi phí hoặc độ hữu dụng của hậu quả:

- chặn nhầm có thể làm mất niềm tin khách hàng;
- bỏ sót gian lận gây thiệt hại tiền;
- kiểm tra thủ công có chi phí và giới hạn năng lực xử lý.

Lý thuyết quyết định tách hai thành phần:

```text
niềm tin về điều có thể xảy ra
        +
giá trị / chi phí của hậu quả
        ↓
lựa chọn hành động
```

## Độ hữu dụng

**Hàm hữu dụng (utility function)**:

\[
U(o)
\]

gán giá trị cho kết quả `o`.

Nếu hành động `a` có nhiều kết quả `o` có thể xảy ra:

\[
EU(a)=\sum_o P(o\mid a)U(o)
\]

Nguyên lý **độ hữu dụng kỳ vọng (expected utility)** chọn:

\[
a^*=\arg\max_a EU(a)
\]

Độ hữu dụng không nhất thiết là tiền. Nó có thể mã hóa an toàn, thời gian, mức hài lòng hoặc tổ hợp nhiều mục tiêu.

## Phân loại có xét chi phí

Một quyết định nhị phân có thể dùng ma trận chi phí:

| Thực tế / Hành động | Dự đoán âm | Dự đoán dương |
|---|---:|---:|
| Âm | 0 | `C_FP` |
| Dương | `C_FN` | 0 |

Nếu xác suất dương đã được hiệu chuẩn là `p`, ta chọn hành động có chi phí kỳ vọng thấp hơn.

Chi phí kỳ vọng khi dự đoán dương:

\[
(1-p)C_{FP}
\]

Chi phí kỳ vọng khi dự đoán âm:

\[
pC_{FN}
\]

Chọn dương nếu:

\[
(1-p)C_{FP}<pC_{FN}
\]

suy ra ngưỡng:

\[
p>\frac{C_{FP}}{C_{FP}+C_{FN}}
\]

Ngưỡng `0.5` chỉ tự nhiên khi hai loại chi phí đối xứng.

## Trung lập rủi ro và nhạy cảm rủi ro

Chỉ tối ưu giá trị kỳ vọng tương ứng với cách nhìn **trung lập rủi ro (risk-neutral)** khi độ hữu dụng tuyến tính theo phần thưởng số.

Con người hoặc doanh nghiệp có thể né tránh rủi ro. Mất 100.000 USD với xác suất 1% có thể được đánh giá khác với “mức mất kỳ vọng 1.000 USD” vì rủi ro đuôi, quy định hoặc khả năng sống còn của tổ chức.

Hàm hữu dụng lõm mô hình hóa giá trị biên giảm dần:

\[
U(\mathbb{E}[X])\ge\mathbb{E}[U(X)]
\]

với `U` lõm theo bất đẳng thức Jensen.

Hệ thống AI có thể cần đại lượng rủi ro tường minh thay vì chỉ tối đa phần thưởng trung bình.

## Giá trị của thông tin

Thông tin chỉ hữu ích nếu nó có khả năng thay đổi quyết định đủ để cải thiện độ hữu dụng kỳ vọng.

**Giá trị kỳ vọng của thông tin hoàn hảo (Expected Value of Perfect Information - EVPI)** có thể nhìn gần đúng như:

\[
\mathbb{E}[\max_a U(a,\theta)]
-
\max_a \mathbb{E}[U(a,\theta)]
\]

Nó đặt cận trên cho số tiền hoặc tài nguyên đáng chi để biết hoàn hảo biến bất định `θ`.

Ví dụ, hệ thống y tế có nên yêu cầu thêm một xét nghiệm trước khi khuyến nghị hành động? Xét nghiệm chỉ có giá trị nếu mức cải thiện quyết định kỳ vọng lớn hơn chi phí và độ trễ của xét nghiệm.

## Quyết định tuần tự

Độ hữu dụng kỳ vọng một bước không đủ khi hành động làm thay đổi trạng thái tương lai.

Ta có trạng thái `s_t`, hành động `a_t`, trạng thái kế tiếp `s_{t+1}`.

Hành động ảnh hưởng cả phần thưởng tức thời lẫn các cơ hội tương lai.

Điều này dẫn tới **Quá trình quyết định Markov (Markov Decision Process - MDP / 마르코프 결정 과정)**.

## Tính Markov

Một quá trình có tính Markov nếu trạng thái hiện tại chứa đủ thông tin để phân phối tương lai không còn phụ thuộc trực tiếp vào toàn bộ lịch sử:

\[
P(s_{t+1}\mid s_t,a_t,s_{t-1},...)=P(s_{t+1}\mid s_t,a_t)
\]

Đây là thuộc tính của cách biểu diễn trạng thái đã chọn, không phải tính chất “tự nhiên” của mọi thế giới.

Nếu trạng thái bỏ mất lịch sử liên quan, giả định Markov không còn đúng.

Ví dụ, nếu xác suất hỏng máy phụ thuộc tổng số giờ sử dụng nhưng trạng thái chỉ lưu nhiệt độ hiện tại, biểu diễn trạng thái là chưa đủ.

## Các thành phần của MDP

Một MDP thường được viết:

\[
\mathcal{M}=(S,A,P,R,\gamma)
\]

trong đó:

- `S`: tập trạng thái;
- `A`: tập hành động;
- `P(s'|s,a)`: xác suất chuyển trạng thái;
- `R(s,a,s')`: phần thưởng;
- `γ`: hệ số chiết khấu.

Một **chính sách (policy)**:

\[
\pi(a\mid s)
\]

ánh xạ trạng thái sang phân phối hành động.

Mục tiêu là tìm chính sách tối đa hóa tổng phần thưởng kỳ vọng dài hạn.

## Tổng phần thưởng hồi quy

**Tổng phần thưởng chiết khấu (discounted return)**:

\[
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
\]

`0≤γ<1` thường giúp tổng hữu hạn và làm phần thưởng gần hiện tại có trọng số cao hơn.

Chiết khấu có thể biểu diễn ưu tiên thời gian, bất định về việc quá trình còn tiếp tục hay đơn giản là thuận tiện toán học. Cách diễn giải phụ thuộc miền.

Với chân trời hữu hạn, đôi khi không cần chiết khấu.

## Hàm giá trị trạng thái

Giá trị của chính sách `π`:

\[
V^\pi(s)=\mathbb{E}_\pi[G_t\mid s_t=s]
\]

trả lời:

> Nếu bắt đầu ở trạng thái này và tiếp tục theo chính sách `π`, tổng phần thưởng dài hạn kỳ vọng là bao nhiêu?

## Hàm giá trị hành động

\[
Q^\pi(s,a)=\mathbb{E}_\pi[G_t\mid s_t=s,a_t=a]
\]

Nó đánh giá việc thực hiện `a` trước, rồi tiếp tục theo `π`.

Nếu muốn chính sách tham lam xác định:

\[
\pi(s)=\arg\max_a Q(s,a)
\]

## Phương trình Bellman

Giá trị có thể phân rã đệ quy:

\[
V^\pi(s)=\sum_a\pi(a\mid s)
\sum_{s'}P(s'\mid s,a)
[R(s,a,s')+\gamma V^\pi(s')]
\]

Phương trình Bellman nói rằng:

```text
giá trị hiện tại
= phần thưởng tức thời kỳ vọng
+ giá trị tương lai kỳ vọng đã chiết khấu
```

Đây là một trong những cấu trúc quan trọng nhất của học tăng cường.

## Phương trình tối ưu Bellman

Giá trị tối ưu:

\[
V^*(s)=\max_a\sum_{s'}P(s'\mid s,a)
[R(s,a,s')+\gamma V^*(s')]
\]

Giá trị hành động tối ưu:

\[
Q^*(s,a)=\sum_{s'}P(s'\mid s,a)
[R(s,a,s')+\gamma\max_{a'}Q^*(s',a')]
\]

Có thể xem đây là tổng quát hóa ngẫu nhiên của quy hoạch động cho đường đi ngắn nhất.

## Lặp giá trị

Khởi tạo `V_0`, rồi lặp phép cập nhật tối ưu Bellman:

\[
V_{k+1}(s)=\max_a\sum_{s'}P(s'\mid s,a)
[R+\gamma V_k(s')]
\]

Trong MDP hữu hạn có chiết khấu, tính co giúp bảo đảm hội tụ tới `V*` dưới các điều kiện chuẩn.

Sau đó suy ra chính sách bằng cách chọn hành động tham lam theo giá trị.

## Lặp chính sách

**Lặp chính sách (policy iteration)** xen kẽ:

1. **đánh giá chính sách** — tính `V^π`;
2. **cải thiện chính sách** — chọn hành động tốt hơn theo giá trị hiện tại.

Lặp tới khi chính sách ổn định.

Phương pháp có thể cần ít vòng ngoài hơn lặp giá trị nhưng bước đánh giá chính sách có thể tốn kém.

## Tìm kiếm và MDP

Đường đi ngắn nhất xác định có thể xem là trường hợp đặc biệt khi xác suất chuyển trạng thái dồn toàn bộ vào một trạng thái kế tiếp.

Chi phí còn lại trong tìm kiếm có vai trò gần với âm của giá trị dài hạn.

A* dùng heuristic ước lượng chi phí còn lại; RL dùng hàm giá trị ước lượng phần thưởng tương lai.

Liên hệ:

```text
heuristic h(s) → ước lượng chi phí còn lại
value V(s)     → ước lượng phần thưởng tương lai kỳ vọng
```

Dấu và hàm mục tiêu khác nhau nhưng vai trò cấu trúc tương tự.

## Khi mô hình chuyển trạng thái chưa biết

Lập kế hoạch MDP cổ điển giả định `P` và `R` đã biết.

**Học tăng cường (Reinforcement Learning - RL)** trở nên cần thiết khi mô hình môi trường chưa biết hoặc quá đắt để mô tả, và tác nhân phải học giá trị hoặc chính sách từ trải nghiệm.

Do đó:

```text
biết mô hình + tối ưu chính sách → lập kế hoạch trong MDP
không biết mô hình + học từ trải nghiệm → học tăng cường
```

RL dựa trên mô hình học hoặc ước lượng mô hình; RL không mô hình học giá trị/chính sách mà không cần mô hình chuyển trạng thái tường minh.

## Quan sát một phần

Nếu tác nhân không quan sát trực tiếp trạng thái `s`, nó chỉ nhận quan sát `o`.

**Quá trình quyết định Markov quan sát một phần (Partially Observable MDP - POMDP / 부분 관찰 마르코프 결정 과정)** bổ sung mô hình quan sát.

Tác nhân duy trì **niềm tin (belief)**:

\[
b(s)=P(s\mid history)
\]

Niềm tin là phân phối xác suất trên các trạng thái có thể xảy ra.

Về khái niệm, POMDP có thể biến thành MDP trên không gian niềm tin, nhưng không gian này liên tục và rất nhiều chiều nên khó giải.

## Cập nhật niềm tin

Sau hành động `a` và quan sát `o`, lọc Bayes cập nhật:

\[
b'(s')\propto P(o\mid s')\sum_s P(s'\mid s,a)b(s)
\]

Có thể tách thành hai bước:

```text
dự đoán phân phối trạng thái kế tiếp
        ↓
điều kiện hóa theo quan sát mới
```

Đây là định lý Bayes hoạt động theo chuỗi thời gian.

## Ước lượng trạng thái

**Bộ lọc Kalman (Kalman Filter)** giải hiệu quả bài toán ước lượng trạng thái tuyến tính-Gaussian.

Động lực trạng thái ẩn:

\[
x_t=Ax_{t-1}+Bu_t+w_t
\]

Quan sát:

\[
z_t=Hx_t+v_t
\]

với nhiễu Gaussian.

Extended Kalman Filter và Unscented Kalman Filter xử lý các xấp xỉ phi tuyến; particle filter dùng các mẫu để biểu diễn phân phối tổng quát hơn.

Robotics phụ thuộc mạnh vào ước lượng trạng thái trước khi lập kế hoạch và điều khiển.

## Ra quyết định khi mô hình cũng bất định

Ngay cả khi đã mô hình hóa ngẫu nhiên của môi trường, bản thân các tham số mô hình vẫn có thể chưa chắc chắn.

Ra quyết định Bayes tích phân trên phân phối hậu nghiệm:

\[
EU(a)=\int U(a,\theta)p(\theta\mid D)d\theta
\]

Trong thực tế tích phân chính xác thường bất khả thi và cần xấp xỉ.

Bỏ qua bất định tri thức có thể khiến hệ thống quá tự tin khi gặp dữ liệu ngoài phân phối.

## Ra quyết định bền vững

Thay vì tin một mô hình xác suất duy nhất, **tối ưu bền vững (robust optimization)** xem xét một tập mô hình có thể xảy ra:

\[
\max_\pi \min_{P\in\mathcal{P}} J(\pi,P)
\]

Cách này bảo vệ trường hợp xấu nhất trong tập bất định nhưng có thể quá bảo thủ.

**Tối ưu bền vững theo phân phối (Distributionally Robust Optimization)** tối ưu trước các phân phối nằm gần phân phối thực nghiệm theo một thước đo đã chọn.

## Ràng buộc xác suất

Một ràng buộc có thể chỉ cần đúng với xác suất đủ cao:

\[
P(g(x,\xi)\le0)\ge1-\alpha
\]

Ví dụ hệ thống tự hành yêu cầu rủi ro va chạm nhỏ hơn ngưỡng.

**Ràng buộc xác suất (chance constraint)** biến bất định thành yêu cầu an toàn xác suất, nhưng chỉ đáng tin nếu mô hình bất định đủ chính xác.

## CVaR và rủi ro đuôi

Mất mát kỳ vọng có thể che khuất các trường hợp hiếm nhưng thảm họa.

Value-at-Risk mô tả một phân vị của mất mát. **Conditional Value-at-Risk (CVaR)** đo trung bình phần mất mát ở vùng đuôi vượt ngưỡng theo định nghĩa phù hợp.

RL nhạy cảm rủi ro có thể tối ưu mục tiêu kiểu CVaR khi hậu quả hiếm nhưng nghiêm trọng quan trọng hơn hiệu năng trung bình.

## Khám phá và khai thác

Khi kết quả hành động chưa chắc chắn vì chưa thử đủ, hành động có hai loại giá trị:

1. phần thưởng ngay lập tức;
2. thông tin thu được để ra quyết định tốt hơn về sau.

**Bài toán bandit nhiều tay (multi-armed bandit)** là dạng đơn giản nhất của tình huống này.

Mỗi “tay” có phân phối phần thưởng chưa biết. Tác nhân phải cân bằng **khai thác (exploitation)** lựa chọn tốt nhất hiện biết và **khám phá (exploration)** lựa chọn chưa chắc chắn để học thêm.

Đây là giá trị thông tin trong một quá trình tuần tự.

## Bandit nhiều tay

Giả sử tay `a` có trung bình chưa biết `μ_a`.

**Hối tiếc (regret)** sau `T` bước:

\[
R_T=T\mu^*-\sum_{t=1}^{T}\mu_{a_t}
\]

Mục tiêu là giảm hối tiếc, không chỉ tối đa hóa phần thưởng quan sát ngay lập tức.

Các thuật toán gồm ε-greedy, UCB và Thompson Sampling.

Bandit có ứng dụng trong hệ thống gợi ý, quảng cáo và thử nghiệm trực tuyến.

## Upper Confidence Bound

UCB chọn:

\[
a_t=\arg\max_a\left[\hat\mu_a+c\sqrt{\frac{\ln t}{N_a}}\right]
\]

Hạng đầu đại diện cho khai thác. Hạng sau là phần thưởng khám phá theo nguyên lý “lạc quan dưới bất định”: tay ít được thử sẽ có phần thưởng bổ sung lớn hơn.

Ý tưởng này cũng xuất hiện trong lựa chọn nút của MCTS.

## Thompson Sampling

Duy trì phân phối hậu nghiệm cho tham số của từng tay. Ở mỗi bước, lấy một mẫu tham số từ hậu nghiệm rồi hành động tham lam theo “thế giới” vừa được lấy mẫu.

Tay chưa chắc chắn tự nhiên được khám phá nhiều hơn vì hậu nghiệm rộng hơn.

Đây là cách chuyển bất định Bayes thành lựa chọn hành động ngẫu nhiên.

## Bandit theo ngữ cảnh

Trong hệ thống gợi ý, phần thưởng còn phụ thuộc người dùng hoặc ngữ cảnh `x`:

\[
P(r\mid x,a)
\]

Hệ thống chọn hành động theo ngữ cảnh nhưng chỉ quan sát phần thưởng cho hành động đã chọn.

Điều này tạo **phản hồi một phần (partial feedback)**: ta không biết điều gì sẽ xảy ra nếu chọn những gợi ý khác.

Vì vậy đánh giá phản thực trở nên quan trọng.

## Đánh giá khác chính sách

Giả sử nhật ký được tạo bởi chính sách hành vi `μ` nhưng ta muốn ước lượng chính sách mục tiêu `π` mà chưa triển khai.

Một ý tưởng của **lấy mẫu tầm quan trọng (importance sampling)** là dùng trọng số:

\[
w=\frac{\pi(a\mid s)}{\mu(a\mid s)}
\]

Dưới các giả định phù hợp, có thể tái trọng số dữ liệu từ chính sách hành vi sang phân phối mục tiêu.

Nhưng phương sai có thể rất lớn nếu chính sách mục tiêu chọn những hành động mà chính sách cũ hiếm khi thực hiện.

Đây là điểm giao giữa thống kê, suy luận nhân quả và đánh giá RL.

## Thiết kế phần thưởng

Phần thưởng không phải chính thực tế; nó chỉ là tín hiệu đại diện.

Nếu tối ưu số lần nhấp, tác nhân có thể học hành vi tăng lượt nhấp ngắn hạn nhưng làm giảm mức hài lòng dài hạn.

Tối ưu tuần tự làm vấn đề đặc tả phần thưởng nghiêm trọng hơn vì chính sách chủ động thay đổi dữ liệu và trạng thái tương lai.

Đây là cầu nối trực tiếp tới căn chỉnh AI.

## Hậu quả đến muộn

Một hành động có thể cho phần thưởng tức thời thấp nhưng giá trị dài hạn cao.

Ví dụ, mở thêm máy chủ tốn chi phí ngay nhưng giúp tránh sự cố về sau.

Ra quyết định thiển cận chỉ tối đa phần thưởng ngay lập tức sẽ thất bại.

Đệ quy Bellman xử lý hậu quả trì hoãn thông qua giá trị tương lai.

## Gán công trạng

Nếu phần thưởng chỉ xuất hiện sau một chuỗi hành động dài, hành động nào trước đó nên được ghi nhận là nguyên nhân đóng góp?

Đây là **bài toán gán công trạng (credit assignment)** cốt lõi của RL.

Temporal Difference learning truyền thông tin giá trị ngược qua trải nghiệm thay vì chỉ chờ kết quả cuối.

Đánh giá tác nhân LLM cũng gặp vấn đề tương tự: nhiệm vụ thất bại sau 20 lần gọi công cụ không trực tiếp cho biết quyết định nào gây lỗi.

## Lập kế hoạch dưới bất định cho tác nhân

Tác nhân dùng công cụ có thể gặp:

```text
API có thể lỗi
kết quả tìm kiếm không đầy đủ
ý định người dùng chưa rõ
trạng thái bên ngoài thay đổi
```

Một mẫu đáng tin cậy:

```text
ước lượng trạng thái / niềm tin
    ↓
chọn hành động ít rủi ro nhưng giàu thông tin
    ↓
quan sát kết quả
    ↓
cập nhật trạng thái
    ↓
tiếp tục / lập kế hoạch lại
```

Đôi khi hành động tốt nhất tiếp theo là hỏi thêm thông tin thay vì vội thực hiện kế hoạch.

## Hành động khó đảo ngược

Thanh toán, xóa dữ liệu, gửi thông điệp hay triển khai mã đều có hậu quả lớn.

Hệ thống ra quyết định nên phân biệt hành động có thể đảo ngược và khó đảo ngược.

Ví dụ chính sách:

```text
rủi ro thấp, dễ đảo ngược → có thể tự động
rủi ro cao, khó đảo ngược → kiểm tra mạnh hơn / yêu cầu xác nhận
```

Đây là lập kế hoạch có xét độ hữu dụng và rủi ro, không chỉ là quy ước giao diện.

## Bất định mô hình và tính ngẫu nhiên của môi trường

Nhắc lại:

- **bất định ngẫu nhiên (aleatoric uncertainty)**: ngẫu nhiên vốn có;
- **bất định tri thức (epistemic uncertainty)**: mô hình hoặc hệ thống chưa biết đủ.

Chiến lược quyết định cho hai loại khác nhau. Dữ liệu mới có thể giảm bất định tri thức nhưng không loại bỏ nhiễu không thể giảm.

Khám phá nhằm giảm bất định tri thức; chính sách bền vững bảo vệ trước mô hình chưa chắc chắn; hàm hữu dụng nhạy cảm rủi ro phản ánh mức nghiêm trọng của hậu quả.

## Độ hữu dụng kỳ vọng không phải đạo đức

Mã hóa hàm hữu dụng đòi hỏi quyết định kết quả của ai được tính và các đánh đổi được đo thế nào. Toán học tối ưu hàm hữu dụng được cung cấp; nó không tự định nghĩa giá trị đạo đức.

Với AI ảnh hưởng cao tới xã hội, mô hình hữu dụng, ràng buộc công bằng và quản trị là các lựa chọn chuẩn tắc cần con người và thể chế quyết định.

## Mô hình tư duy (mental model)

```text
Xác suất      = điều gì có thể xảy ra?
Độ hữu dụng   = hậu quả quan trọng đến mức nào?
Chính sách    = chọn hành động nào ở mỗi trạng thái / niềm tin?
Giá trị       = độ hữu dụng tương lai kỳ vọng từ đây
MDP           = quyết định tuần tự với chuyển trạng thái ngẫu nhiên
POMDP         = trạng thái bị ẩn một phần; suy luận bằng niềm tin
Khám phá      = hành động một phần để học thêm
Rủi ro        = quan tâm cả phân phối và phần đuôi, không chỉ trung bình
```

## Các hiểu lầm thường gặp

### “Kết quả có xác suất cao nhất nên quyết định hành động”

Không. Hành động phụ thuộc hậu quả. Một sự kiện xác suất thấp nhưng thảm họa có thể chi phối lựa chọn kỳ vọng hoặc nhạy cảm rủi ro.

### “Trạng thái MDP chỉ là quan sát hiện tại”

Trạng thái phải đủ thông tin để thỏa tính Markov. Quan sát có thể chỉ là một phần.

### “Tối đa phần thưởng kỳ vọng nghĩa là chính sách an toàn nhất”

Không nhất thiết. Mục tiêu trung bình có thể chấp nhận tổn thất hiếm nhưng thảm họa nếu rủi ro chưa được mã hóa.

### “Có tác nhân thì tức là đang dùng RL”

Nếu mô hình chuyển và phần thưởng đã biết, chính sách có thể được giải bằng quy hoạch động; đó là lập kế hoạch trong MDP. RL đặc biệt học từ tương tác hoặc dữ liệu khi mô hình, giá trị hoặc chính sách chưa biết.

## Liên kết kiến thức

Ra quyết định dưới bất định hoàn tất cầu nối từ tìm kiếm/lập kế hoạch cổ điển sang học tăng cường. Tìm kiếm xử lý lựa chọn xác định; MDP thêm chuyển trạng thái ngẫu nhiên và giá trị dài hạn; POMDP thêm trạng thái ẩn; RL học hành vi khi mô hình hoặc giá trị chưa biết.

Sau phần Biểu diễn tri thức và Học máy, thư viện sẽ quay lại MDP và phương trình Bellman sâu hơn trong `11_reinforcement_learning/`.