# Training Dynamics trong Deep Learning: hiểu quá trình mô hình thật sự học

Training Neural Network không chỉ là lặp `forward → backward → optimizer.step()`. Mô hình có thể giảm loss nhưng vẫn học representation kém, diverge sau vài nghìn bước, overfit, collapse hoặc đạt cùng final loss qua những quỹ đạo hoàn toàn khác nhau. **Động lực học huấn luyện (Training Dynamics / 학습 동역학)** nghiên cứu hành vi của quá trình tối ưu theo thời gian.

Hiểu dynamics giúp debug có hệ thống thay vì chỉ thử hyperparameter ngẫu nhiên.

## Vòng lặp training

Một vòng lặp cơ bản:

```text
với mỗi batch dữ liệu:
    prediction = model(batch.x)
    loss = objective(prediction, batch.y)
    gradients = backward(loss)
    optimizer.update(parameters, gradients)
```

Training production thường thêm:

```text
mixed precision
loss scaling
gradient accumulation
clipping
learning-rate schedule
logging
checkpointing
validation
distributed synchronization
```

Mỗi thành phần đều có thể thay đổi dynamics.

## Loss curve nói được gì và không nói được gì?

Training loss giảm chỉ có nghĩa optimizer đang cải thiện objective trên các batch đã quan sát.

Nó không bảo đảm validation tốt hơn, calibration tốt hơn, robustness tăng, representation có ý nghĩa hơn hoặc deployment metric được cải thiện.

Một số pattern hữu ích trên loss curve:

```text
phẳng ngay từ đầu
→ learning rate quá nhỏ, initialization kém, parameter bị freeze hoặc dữ liệu/label lỗi

bùng nổ
→ learning rate quá lớn, lỗi số học hoặc normalization không phù hợp

dao động mạnh
→ learning rate cao hoặc batch quá nhiễu

training giảm nhưng validation tăng
→ overfitting hoặc distribution mismatch

spike đột ngột
→ batch bất thường, overflow hoặc optimizer state không ổn định
```

## Learning-Rate Warmup

Ở đầu training, tham số còn ngẫu nhiên, LayerNorm/residual statistics và optimizer moment chưa ổn định.

Learning rate lớn ngay từ bước đầu có thể làm hệ thống mất ổn định.

Warmup tăng dần learning rate:

\[
\eta_t=\eta_{max}\frac{t}{T_{warmup}}
\]

sau đó mới chuyển sang giai đoạn decay.

Transformer đặc biệt nhạy với tương tác giữa warmup, batch size và initialization.

## Tỷ lệ Update-to-Weight

Không chỉ gradient norm, độ lớn update so với tham số hiện tại cũng rất hữu ích:

\[
ratio=\frac{\|\Delta\theta\|}{\|\theta\|}
\]

Nếu tỷ lệ quá lớn, update có thể phá hỏng cấu trúc đã học. Nếu quá nhỏ, mô hình gần như không di chuyển trong parameter space.

Fine-tuning mô hình pretrained thường cần update nhỏ hơn nhiều so với pretraining từ random initialization.

## Theo dõi Gradient Norm

Gradient norm toàn cục hoặc theo từng layer cho biết phân bố tín hiệu học.

Nếu các layer đầu có norm gần 0 còn các layer cuối rất lớn, có thể có vanishing hoặc đường gradient bị chặn.

Nếu một layer có gradient cực lớn, đây có thể là nguồn của instability hoặc vấn đề scale.

Khi dùng gradient clipping nên theo dõi tỷ lệ step thực sự bị clip. Nếu 90% step đều chạm ngưỡng, cần xem lại threshold, learning rate hoặc nguyên nhân gốc.

## Thống kê Activation

Nên theo dõi mean, standard deviation, max/min và tỷ lệ zero qua các layer.

Dying ReLU thường có zero fraction gần 100%.

Sigmoid/tanh bão hòa tạo activation gần biên và gradient rất nhỏ.

Exploding activation làm standard deviation tăng nhanh qua depth.

Normalization có thể che một phần triệu chứng nhưng không loại bỏ mọi nguyên nhân instability.

## Thứ tự dữ liệu và Shuffling

SGD hoạt động tốt hơn khi batch đủ đại diện cho distribution mục tiêu.

Nếu dữ liệu bị sort theo label, thời gian hoặc domain, nhiều batch liên tiếp sẽ tạo gradient lệch theo cùng một hướng và làm training dao động hoặc drift.

Shuffling giúp gần với giả định IID hơn, nhưng time-series hoặc online learning đôi khi cần giữ thứ tự có chủ đích.

Distributed training cũng cần sharding đúng để tránh duplicate hoặc bỏ sót sample.

## Curriculum Learning

Sắp xếp example từ dễ tới khó có thể cải thiện optimization trong một số task.

Nhưng “độ khó” không phải lúc nào cũng định nghĩa được chính xác.

Trong instruction tuning của LLM, tỷ lệ và thứ tự giữa nhiều nguồn dữ liệu hoặc mức chất lượng khác nhau cũng có thể xem như một curriculum.

Data curriculum vì vậy trở thành một hyperparameter của tối ưu hóa.

## Phân phối lấy mẫu

Thành phần dataset quyết định kỳ vọng của gradient.

Nếu nguồn A chiếm 90% batch, objective ngầm ưu tiên A rất mạnh dù công thức loss không đổi.

Reweight hoặc resample source sẽ thay đổi điều mô hình học.

Foundation-model training ở quy mô lớn thường thiết kế rất cẩn thận trọng số cho từng data mixture.

## Dynamics dưới mất cân bằng lớp

Class hiếm tạo rất ít gradient update.

Mô hình có thể nhanh chóng học hành vi của majority class rồi khó phục hồi cho minority class.

Class weighting, balanced sampling, focal loss hoặc pipeline hai giai đoạn đều làm thay đổi phân bố gradient.

Cần theo dõi metric riêng từng class thay vì chỉ nhìn loss tổng.

## Catastrophic Forgetting

Fine-tuning trên một distribution hẹp có thể làm mô hình mất một phần capability đã học từ pretraining.

Các biện pháp thường gồm learning rate nhỏ hơn, trộn lại dữ liệu tổng quát, regularization về base weight, adapter/LoRA, freeze layer hoặc rehearsal.

Đây là vấn đề của training dynamics khi mô hình đi qua nhiều distribution theo thời gian.

## Fine-Tuning và Feature Extraction

Đóng băng encoder rồi chỉ train head mới giúp giữ representation pretrained nhưng có thể thích nghi chưa đủ.

Fine-tuning toàn bộ linh hoạt hơn nhưng tốn compute và tăng rủi ro forgetting hoặc overfitting.

Gradual unfreezing hoặc learning rate khác nhau theo layer tạo ra các điểm trung gian.

## Learning Rate theo từng Layer

Các layer đầu của mô hình pretrained đôi khi chỉ cần update rất nhỏ, trong khi task head mới cần học nhanh hơn.

Một recipe có thể dùng:

```text
embedding / layer đầu → learning rate nhỏ
layer giữa             → learning rate vừa
head mới                → learning rate lớn hơn
```

Không phải quy tắc chung, nhưng phản ánh một nguyên lý: các nhóm tham số có nhu cầu thích nghi khác nhau.

## Scale giữa nhiều Objective

Với multi-task loss:

\[
L=\sum_k\lambda_kL_k
\]

độ lớn raw loss và gradient của mỗi task có thể rất khác.

`λ_k` quyết định ảnh hưởng thật của từng task lên shared representation, không chỉ thay số hiển thị trên dashboard.

Một task có gradient lớn hơn nhiều có thể chi phối toàn bộ training.

Các phương pháp cân bằng động có thể dựa trên uncertainty, gradient norm hoặc mức xung đột giữa các task.

## Xung đột Gradient trong Multi-Task Learning

Nếu:

\[
g_1^Tg_2<0
\]

thì hai task đang muốn update shared parameter theo các hướng đối lập.

Đây là trade-off của representation và objective, không nhất thiết là bug optimizer.

Phân tích geometry của gradient giúp thiết kế task weight hoặc adapter riêng.

## Loss Spike

Large-model training đôi khi xuất hiện spike tạm thời do batch hiếm, optimizer state, precision hoặc dữ liệu lỗi.

Cách xử lý vận hành tốt hơn là lưu batch hoặc source gây spike, inspect activation/gradient norm, checkpoint đủ thường xuyên, bỏ qua hoặc phục hồi khi xuất hiện non-finite value và xem lại clipping, learning rate hoặc dữ liệu.

Khởi động lại một cách mù quáng chỉ làm lãng phí compute.

## Checkpointing

Muốn resume chính xác, checkpoint không nên chỉ chứa model weight mà còn cần:

```text
model parameters
optimizer state
scheduler state
random-generator state
data-loader position / sampler state
mixed-precision scaler state
training step / config
```

Load chỉ weight rồi dùng optimizer mới là một kiểu restart hoặc fine-tuning, không phải exact resume.

## Exponential Moving Average của Weight

Duy trì:

\[
\theta_{EMA}\leftarrow\beta\theta_{EMA}+(1-\beta)\theta
\]

EMA làm mượt quỹ đạo tham số và thường cải thiện evaluation trong vision hoặc generative model.

Stochastic Weight Averaging cũng lấy trung bình nhiều checkpoint hoặc weight ở giai đoạn sau để tìm vùng nghiệm rộng hơn.

## Tần suất Validation

Validate quá thường xuyên gây overhead; quá ít lại có thể bỏ lỡ divergence hoặc overfitting và lãng phí nhiều compute.

Tần suất nên phụ thuộc kích thước dataset, chi phí training và tốc độ thay đổi kỳ vọng.

Với pretraining cực lớn, thường có proxy metric chạy thường xuyên và full evaluation suite chạy thưa hơn.

## Reproducibility

Tái lập bitwise hoàn toàn rất khó vì random seed, thứ tự dữ liệu, GPU kernel nondeterministic, thứ tự reduction phân tán, phiên bản library/compiler và rounding ở low precision.

Trong khoa học và production, mục tiêu thực tế thường là tái lập ở mức metric và hành vi thay vì từng bit giống hệt nhau.

Cần log đầy đủ config, code version và data version.

## Dynamics trong Distributed Training

Data parallelism lấy trung bình gradient từ nhiều worker.

Global batch:

\[
B_{global}=B_{device}\times N_{devices}\times accumulation
\]

Thay số GPU có thể làm batch size và optimization dynamics đổi nếu không điều chỉnh recipe.

Precision và thứ tự của communication/reduction cũng có thể tạo khác biệt số học.

Large-scale optimization vì vậy là bài toán kết hợp giữa thuật toán và distributed system.

## Preview về Scaling Law

Khi model, data và compute tăng, loss thường tuân theo các quan hệ gần power-law trong một số regime.

Scaling law giúp phân bổ tài nguyên nhưng không bảo đảm downstream capability, factuality hay safety tăng theo cùng cách.

Phần LLM sẽ phân tích sâu hơn.

## Thứ tự debug có hệ thống

Khi training thất bại, không nên lập tức đổi optimizer. Có thể kiểm tra theo thứ tự:

1. Dữ liệu và label có đúng không?
2. Mô hình có overfit được một tập cực nhỏ không?
3. Forward output có hữu hạn và hợp lý không?
4. Loss implementation có đúng không?
5. Gradient có khác 0 và hữu hạn không?
6. Learning rate và độ lớn update có hợp lý không?
7. Thống kê activation/gradient có ổn định không?
8. Validation split có đúng và không leakage không?
9. Model capacity và regularization có phù hợp không?
10. Có lỗi từ distributed hoặc mixed precision không?

**Overfit một mini-batch rất nhỏ** là diagnostic cực mạnh: nếu mô hình đủ capacity mà vẫn không ghi nhớ nổi vài example, nhiều khả năng pipeline hoặc training implementation đang có lỗi.

## Mô hình tư duy

> Training là một hệ động lực trong parameter space, được điều khiển đồng thời bởi thứ tự dữ liệu, objective, optimizer, schedule, numerical precision và architecture.

Không chỉ final hyperparameter, mà cả quỹ đạo đi tới nghiệm cũng quan trọng.

## Các hiểu lầm thường gặp

### “Loss đang giảm nghĩa training bình thường”

Không. Validation có thể xấu đi, mô hình có thể học shortcut hoặc dữ liệu có leakage.

### “Cùng seed nghĩa hai run giống hệt nhau”

Không. Distributed GPU operation và low-precision arithmetic có thể nondeterministic.

### “Checkpoint chỉ cần weights”

Không nếu muốn resume chính xác. Cần cả optimizer, scheduler, RNG và vị trí data loader.

### “Training instability luôn do learning rate”

Learning rate là nguyên nhân phổ biến nhưng dữ liệu bất thường, precision, normalization, initialization và exploding gradient cũng có thể gây lỗi.

## Liên kết kiến thức

Chương này tổng hợp [Lan truyền tiến](./03_forward_propagation.md), [Backpropagation](./04_backpropagation.md), [Optimizer](./05_gradient_descent_and_optimizers.md), [Initialization/Normalization](./06_initialization_and_normalization.md), [Regularization](./07_regularization.md) và [Đánh giá mô hình](../04_machine_learning/15_model_evaluation.md).

Đây là cầu nối sang `06_deep_learning_architectures/`, nơi kiến trúc cụ thể thay đổi computation graph và training dynamics.