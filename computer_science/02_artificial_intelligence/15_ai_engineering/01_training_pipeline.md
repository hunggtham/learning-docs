# Training Pipeline

Để huấn luyện mô hình có khả năng tái lập, chỉ gọi `model.fit()` là chưa đủ. **Pipeline huấn luyện (training pipeline / 학습 파이프라인)** điều phối snapshot dữ liệu, tiền xử lý, cấu hình, distributed job, checkpoint, đánh giá và đăng ký artifact.

```text
dữ liệu đã version hóa
→ kiểm tra
→ biến đổi
→ huấn luyện
→ checkpoint
→ đánh giá
→ đóng gói artifact
→ đăng ký
```

## Input phải bất biến

Một training run nên trỏ tới dataset/version chính xác, không nên dùng một file mutable kiểu `latest.csv`. Input thay đổi làm mất khả năng tái lập.

Cần ghi lại:

```text
data manifest / hash
commit của feature code
label schema
model config
seed
runtime image
```

## Cấu hình

Nên tách cấu hình khỏi code:

```text
learning_rate
batch_size
architecture
optimizer
data paths
augmentation
precision
checkpoint interval
```

Bản thân config cũng phải được version hóa và lưu cùng training run.

## Kiểm tra dữ liệu trước khi dùng compute đắt tiền

Trước khi cấp GPU, cần kiểm tra schema, số lượng mẫu, null, phân phối class, các leakage gate và tính toàn vẹn của file. Phát hiện lỗi sớm giúp tiết kiệm chi phí lớn.

## Shuffling và Sampling

Distributed training cần chia shard và lấy mẫu đúng cách, đồng thời đủ ổn định để có thể tái lập ở mức hợp lý. Class-balanced sampler thay đổi phân phối training thực tế nên phải được ghi lại rõ ràng.

## Tính xác định

Khả năng tái lập hoàn toàn trên GPU có thể khó do kernel không xác định và parallel reduction. Cần phân biệt:

- tái lập được cấu hình;
- tái lập được kết quả theo nghĩa thống kê;
- kết quả bitwise giống hệt.

Không nên hứa bitwise equality nếu toàn bộ stack không hỗ trợ.

## Checkpoint

Checkpoint thường lưu:

```text
model weights
optimizer state
scheduler state
step / epoch
random states khi cần
mixed-precision scaler
```

Chỉ lưu weights là không đủ để resume training giống trước, vì momentum và state của optimizer đã mất.

## Tần suất Checkpoint

Checkpoint quá thưa làm mất nhiều công sức khi job lỗi. Checkpoint quá dày làm tăng overhead về storage và I/O.

Chu kỳ checkpoint nên dựa trên chi phí của job và xác suất failure.

## Validation trong quá trình Training

Validation định kỳ giúp phát hiện overfitting hoặc divergence. Nhưng validation set lớn cũng có thể trở thành chi phí đáng kể; có thể dùng subset đại diện cho kiểm tra thường xuyên và chạy full evaluation tại các milestone.

## Early Stopping

Dừng huấn luyện nếu validation metric không cải thiện sau một khoảng đủ dài. Cần có `patience` để tránh phản ứng quá mức với nhiễu.

Với foundation model, pretraining thường được lập kế hoạch theo compute/token budget thay vì validation theo epoch kiểu truyền thống.

## Mixed Precision

FP16/BF16 giúp giảm memory và tăng throughput trên accelerator. Một số phép toán nhạy số vẫn có thể cần precision cao hơn.

FP16 thường dùng **loss scaling** để tránh gradient underflow; BF16 có exponent range lớn hơn nên giảm nhu cầu này.

## Gradient Accumulation

Nếu batch mong muốn không vừa memory, có thể cộng dồn gradient qua nhiều microbatch:

```text
zero grad
for k microbatches:
    forward / backward(loss / k)
optimizer step
```

Effective batch tăng mà không cần giữ toàn bộ activation cùng lúc, nhưng latency cho mỗi optimizer step cũng tăng.

## Distributed Data Parallel

Với **Distributed Data Parallel (DDP)**, mô hình được replicate trên nhiều device, mỗi device xử lý một shard khác nhau rồi đồng bộ gradient bằng all-reduce.

Communication overhead tăng theo số parameter. Các phần sharding và model parallelism được giải thích sâu hơn ở layer hạ tầng.

## Hyperparameter Search

Grid search, random search hoặc Bayesian optimization có thể tạo rất nhiều training run. Vì vậy cần experiment tracking và budget control.

Test set không được biến thành objective của hyperparameter search.

## Đóng gói Artifact

Training thành công nên tạo ra bundle có thể triển khai:

```text
weights
tokenizer / preprocessor
model config
label map
signature / input schema
metrics
provenance
```

## Bàn giao sang Model Registry

Chỉ những mô hình vượt qua evaluation và quality gate mới nên được đưa vào model registry để xem xét deployment. “Training đã chạy xong” không đồng nghĩa “được phép chạy production”.

## Phục hồi khi lỗi

Pipeline nên có khả năng resume từ checkpoint nhất quán gần nhất. Điều này đặc biệt quan trọng khi dùng spot hoặc preemptible instance.

## Bottleneck ở Data Loader

GPU có thể bị idle nếu CPU decoding, augmentation hoặc storage quá chậm. Cần theo dõi accelerator utilization và thời gian chờ dữ liệu.

Các cách cải thiện gồm:

- prefetch;
- nhiều worker song song;
- định dạng dữ liệu hiệu quả;
- local/cache storage;
- GPU augmentation khi phù hợp.

## Training Throughput

Các metric phổ biến:

```text
samples / sec
tokens / sec
```

Tuy nhiên throughput cao nhất chưa chắc giúp hội tụ nhanh nhất nếu batch size hoặc optimizer làm giảm sample efficiency.

**Time-to-quality** thường có ý nghĩa hơn raw hardware utilization.

## Metadata của Experiment

Mỗi run nên trả lời được:

- thay đổi gì?
- data version nào?
- code/config nào?
- metric nào?
- artifact nào?
- base model hoặc parent nào?
- tốn bao nhiêu compute và chi phí?

## Pretraining Pipeline

Foundation-model pretraining thường bổ sung:

```text
hỗn hợp dữ liệu rất lớn
streaming shard
dedup / filter
checkpoint ở quy mô lớn
distributed optimizer
fault recovery
đánh giá dài hạn
```

Ở quy mô này, một shard bị lỗi hoặc một node chết không được phép làm dừng toàn bộ job.

## Fine-Tuning Pipeline

Pipeline SFT/LoRA cần ghi rõ base-model version, adapter config, prompt/template và tokenizer. Chat template không tương thích có thể gây regression lớn khi serving.

## Bảo mật

Training job thường truy cập dataset lớn và cloud storage nhạy cảm. Nên dùng credential có scope tối thiểu, worker cô lập và tránh đưa secret trực tiếp vào config hoặc checkpoint.

## Mô hình tư duy

> **Training pipeline biến một thí nghiệm tối ưu hóa mang tính nghiên cứu thành quy trình sản xuất artifact mô hình có thể tái lập.**

## Những nhầm lẫn thường gặp

### “Checkpoint chỉ là weights”

Không. Để resume chính xác còn cần state của optimizer, scheduler và các state liên quan khác.

### “Cùng seed thì kết quả chắc chắn giống hệt”

Không. Distributed GPU operation vẫn có thể không xác định.

### “GPU utilization cao nghĩa là pipeline tối ưu”

Không. Time-to-quality và cost-to-quality quan trọng hơn.

## Liên kết kiến thức

Training pipeline là cầu nối giữa [Data Governance](../14_data_for_ai/08_data_governance.md) và vòng đời experiment/model trong MLOps.

Xem tiếp: [Inference Pipeline](./02_inference_pipeline.md).