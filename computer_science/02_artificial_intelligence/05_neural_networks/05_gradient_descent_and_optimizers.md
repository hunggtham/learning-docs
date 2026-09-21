# Gradient Descent và Optimizer trong Deep Learning

Sau khi Backpropagation tính gradient, **optimizer** quyết định **các tham số sẽ thay đổi như thế nào**. Đây là phân biệt rất quan trọng: gradient chỉ cung cấp thông tin cục bộ về độ dốc, còn optimizer là chính sách sử dụng thông tin đó qua nhiều bước huấn luyện.

Tối ưu Deep Learning khó vì objective thường phi lồi, số tham số rất lớn, gradient có nhiễu do mini-batch và độ cong của loss khác nhau theo từng hướng. Vì vậy Gradient Descent là nền để hiểu, nhưng training thực tế thường dùng SGD có momentum, Adam/AdamW và learning-rate schedule.

## Gradient Descent

Quy tắc cập nhật cơ bản:

\[
\theta_{t+1}=\theta_t-\eta\nabla_\theta L(\theta_t)
\]

`η` là **tốc độ học (learning rate)**.

Gradient chỉ hướng tăng nhanh nhất cục bộ theo chuẩn Euclid; gradient âm cho hướng giảm nhanh nhất nếu bước dịch chuyển vô cùng nhỏ. Với bước hữu hạn, learning rate quyết định update còn hữu ích hay đã đi quá xa và vượt qua vùng tốt.

## Full Batch, Stochastic và Mini-Batch

Full-batch gradient dùng toàn bộ dataset:

\[
g=\frac1N\sum_i\nabla L_i
\]

nên estimate ổn định hơn nhưng chi phí lớn.

Stochastic Gradient Descent theo nghĩa chặt dùng một mẫu mỗi bước. Trong thực tế, “SGD” thường dùng **mini-batch**:

\[
g_B=\frac1{|B|}\sum_{i\in B}\nabla L_i
\]

Mini-batch gradient là một ước lượng có nhiễu của full gradient. Nhiễu không chỉ là bất lợi; trong một số chế độ, nó còn giúp exploration và tạo implicit regularization.

## Learning Rate là hyperparameter cực kỳ quan trọng

Learning rate quá nhỏ làm training chậm và có thể mất rất lâu ở vùng phẳng.

Learning rate quá lớn có thể gây dao động, divergence hoặc NaN/Inf.

Trong thực tế, learning rate thường quan trọng hơn nhiều chi tiết nhỏ của optimizer.

## Momentum

Momentum tích lũy hướng gradient qua thời gian:

\[
v_t=\beta v_{t-1}+g_t
\]

\[
\theta_{t+1}=\theta_t-\eta v_t
\]

Nó làm mượt gradient nhiễu, tăng tốc ở các hướng mà gradient liên tục cùng chiều và giảm zig-zag trong vùng có độ cong rất khác nhau theo các trục.

Ẩn dụ “quán tính vật lý” hữu ích cho trực giác, nhưng `v_t` chỉ là trạng thái toán học của optimizer.

## Nesterov Momentum

Các phương pháp kiểu Nesterov nhìn trước theo hướng momentum rồi hiệu chỉnh dựa trên gradient ở vị trí dự kiến.

Trực giác là optimizer cố dự đoán nơi tham số sắp tới để phản ứng sớm hơn.

Công thức implementation có thể khác nhau giữa framework, nên nếu cần reproducibility phải kiểm tra chính xác convention được dùng.

## AdaGrad

AdaGrad điều chỉnh learning rate riêng cho từng tham số dựa trên tổng bình phương gradient tích lũy:

\[
s_t=s_{t-1}+g_t^2
\]

\[
\theta_{t+1}=\theta_t-\eta\frac{g_t}{\sqrt{s_t}+\epsilon}
\]

Tham số hiếm khi nhận gradient có thể giữ effective learning rate lớn hơn, hữu ích với feature thưa.

Nhược điểm là `s_t` chỉ tăng, nên learning rate có thể giảm quá mạnh về sau.

## RMSProp

RMSProp thay tổng tích lũy vô hạn của AdaGrad bằng trung bình trượt mũ:

\[
s_t=\beta s_{t-1}+(1-\beta)g_t^2
\]

sau đó scale gradient theo `s_t`.

Cách này giúp adaptive step không giảm mãi chỉ vì training kéo dài.

## Adam

Adam kết hợp estimate moment bậc nhất và bậc hai:

\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
\]

\[
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
\]

Sau hiệu chỉnh bias:

\[
\hat m_t=\frac{m_t}{1-\beta_1^t},\qquad
\hat v_t=\frac{v_t}{1-\beta_2^t}
\]

cập nhật:

\[
\theta_{t+1}=\theta_t-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
\]

Adam thích nghi step riêng cho từng tham số và thường dễ dùng với Transformer.

## AdamW và Weight Decay

L2 regularization và weight decay có thể tương đương trong vanilla SGD dưới một số formulation, nhưng không hoàn toàn tương đương khi dùng adaptive optimizer.

**AdamW** tách riêng weight decay khỏi adaptive gradient update:

\[
\theta\leftarrow(1-\eta\lambda)\theta-\eta\cdot AdamUpdate
\]

Đây là một lý do AdamW trở thành lựa chọn rất phổ biến cho Transformer training và fine-tuning.

## Learning-Rate Schedule

Giữ learning rate không đổi từ đầu tới cuối hiếm khi là lựa chọn tốt nhất với training dài.

### Warmup

Bắt đầu với learning rate nhỏ rồi tăng dần. Ở giai đoạn đầu, activation, gradient và optimizer moment chưa ổn định; warmup giúp giảm nguy cơ update quá mạnh, đặc biệt với Transformer hoặc batch lớn.

### Step / Exponential Decay

Giảm learning rate theo milestone hoặc theo hàm mũ.

### Cosine Decay

\[
\eta_t=\eta_{min}+\frac12(\eta_{max}-\eta_{min})
\left(1+\cos\frac{\pi t}{T}\right)
\]

làm learning rate giảm mượt dần tới giá trị thấp.

### One-Cycle

Learning rate tăng rồi giảm trong một chu kỳ, thường kết hợp với schedule cho momentum.

Schedule là một phần của thuật toán tối ưu, không phải cấu hình trang trí.

## Weight Decay không nhất thiết áp dụng cho mọi tham số

Training hiện đại thường không áp weight decay giống nhau cho bias hoặc scale của normalization layer.

Vì vậy muốn tái lập một recipe, chỉ ghi “AdamW, lr=1e-4” là chưa đủ. Còn cần parameter group, weight decay, warmup, batch size và schedule.

## Gradient Clipping

Global norm clipping:

\[
g\leftarrow g\cdot\min(1,c/\|g\|)
\]

giới hạn update cực lớn bất thường.

RNN và Transformer thường sử dụng kỹ thuật này.

Clipping là một cơ chế bảo vệ; nếu gradient liên tục bùng nổ, cần tìm nguyên nhân gốc ở learning rate, normalization, architecture hoặc numerical stability.

## Batch Size và Learning Rate

Batch lớn làm gradient ít nhiễu hơn và thường tận dụng hardware tốt hơn, nhưng dùng nhiều memory hơn.

Hành vi tối ưu cũng thay đổi khi batch size thay đổi.

Quy tắc tuyến tính `lr ∝ batch` chỉ là heuristic trong một số chế độ, không phải định luật chung.

**Gradient accumulation** cho phép mô phỏng effective batch lớn bằng nhiều micro-batch trước khi gọi optimizer step.

Nếu loss scaling hoặc averaging sai, độ lớn gradient tích lũy cũng sai theo.

## Gradient Noise và Generalization

Batch nhỏ tạo gradient nhiều nhiễu hơn và trong một số bài toán có thể hướng optimizer tới các vùng nghiệm bền hơn.

Tuy nhiên lý thuyết rất phức tạp; không nên biến điều này thành quy tắc “batch nhỏ luôn generalize tốt hơn”.

Throughput phần cứng và normalization cũng ảnh hưởng mạnh.

## Bề mặt loss phi lồi

Objective của mạng sâu chứa saddle point, vùng phẳng, symmetry và nhiều minimum tương đương chức năng.

Mục tiêu thực tế không phải tìm “global minimum tuyệt đối” về toán học; ta cần một nghiệm có loss thấp, generalization tốt và đạt được trong ngân sách compute.

Do symmetry của tham số, nhiều điểm rất khác nhau trong parameter space vẫn biểu diễn gần như cùng một hàm.

## Sharpness và Flatness

Trực giác phổ biến là nghiệm bền trước perturbation nhỏ của tham số có thể generalize tốt hơn.

Tuy nhiên sharpness thô phụ thuộc cách tham số hóa và scale, nên phải diễn giải cẩn thận.

Các phương pháp như SAM tối ưu objective có xét neighborhood, nhưng không có một metric flatness duy nhất giải thích generalization cho mọi mô hình.

## Mixed Precision và Loss Scaling

Với FP16, gradient nhỏ có thể underflow.

**Loss scaling** nhân loss với hệ số `s` trước backward:

\[
L'=sL
\]

Gradient được tính ở scale lớn hơn rồi chia lại trước optimizer update.

Dynamic loss scaling tự thay đổi `s` nếu phát hiện overflow.

BF16 có exponent range lớn hơn nên ít nhạy với underflow hơn, dù mantissa có độ chính xác thấp hơn.

## Bộ nhớ của Optimizer State

Adam phải lưu parameter, gradient, first moment và second moment, nên optimizer state có thể chiếm nhiều lần dung lượng parameter.

Với LLM rất lớn, đây là chi phí cực đáng kể.

Distributed training dùng sharding kiểu ZeRO hoặc FSDP để chia các state này qua nhiều thiết bị.

Tối ưu hóa vì vậy nối trực tiếp với hạ tầng tính toán.

## Chọn Optimizer

Không tồn tại một lựa chọn thắng tuyệt đối.

- SGD + momentum: mạnh trong nhiều vision/classical deep network, dùng ít optimizer memory hơn.
- AdamW: rất phổ biến với Transformer và fine-tuning.
- Adafactor hoặc 8-bit optimizer: giảm bộ nhớ state cho mô hình lớn.
- Optimizer chuyên biệt khác có các trade-off riêng.

Recipe phải được đánh giá cùng architecture, data và schedule.

## Mô hình tư duy

```text
Backpropagation = đo độ dốc hiện tại
Optimizer        = nhớ lịch sử + chính sách scale/cập nhật
Scheduler        = thay đổi chính sách bước học theo thời gian
```

## Các hiểu lầm thường gặp

### “Adam luôn tốt hơn SGD vì hội tụ nhanh hơn”

Không. Tốc độ hội tụ, generalization cuối cùng và loại task có thể khác nhau.

### “Learning rate càng nhỏ càng an toàn”

Không. Quá nhỏ có thể làm training quá chậm hoặc không tới được nghiệm tốt trong ngân sách hữu hạn.

### “Weight decay chỉ là L2 đổi tên”

Không hoàn toàn, đặc biệt với adaptive optimizer. Decoupled weight decay như AdamW có hành vi khác việc cộng trực tiếp L2 penalty vào gradient.

### “Optimizer tự xử lý exploding gradient”

Không. Adaptive scaling không bảo đảm điều đó; clipping, initialization, normalization và architecture vẫn quan trọng.

## Liên kết kiến thức

Xem [Tối ưu hóa](../01_mathematical_foundations/06_optimization.md), [Backpropagation](./04_backpropagation.md), [Initialization và Normalization](./06_initialization_and_normalization.md) và [Training Dynamics](./09_deep_learning_training_dynamics.md).