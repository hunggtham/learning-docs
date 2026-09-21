# Distributed Training

Khi model, optimizer state hoặc desired batch không fit trên một accelerator, training phải được phân tán qua nhiều device hoặc node. **Huấn luyện phân tán (distributed training / 분산 학습)** không chỉ là chạy cùng một đoạn code trên nhiều GPU; nó làm thay đổi memory layout, communication pattern, fault model và khả năng tái lập.

## Vì sao cần Distributed Training?

Ba lý do chính:

```text
model quá lớn cho một device
training quá chậm trên một device
batch / data throughput quá lớn
```

Mỗi lý do dẫn tới strategy parallelism khác nhau.

## Data Parallel Training

Mỗi worker giữ một model replica và xử lý batch riêng. Sau backward pass, gradient được aggregate.

Một synchronous step điển hình:

```text
forward
→ backward
→ all-reduce gradients
→ optimizer step
```

Global batch:

\[
B_{global}=B_{device}\times N_{devices}\times accumulation\_steps
\]

Learning-rate schedule có thể cần điều chỉnh khi global batch thay đổi.

## Distributed Data Parallel

Implementation hiệu quả có thể overlap gradient all-reduce với backward pass. Tuy nhiên parameter vẫn được replicate nên memory trên mỗi device còn cao.

Đây thường là lựa chọn đầu tiên khi model vẫn fit trên một device.

## Sharded Data Parallelism

Parameter, gradient và optimizer state có thể được shard giữa các worker.

Về mặt khái niệm:

```text
Stage 1: shard optimizer states
Stage 2: + gradients
Stage 3: + parameters
```

Cách này giảm memory duplication nhưng tăng communication complexity.

## Tensor Parallelism

Large layer được chia qua nhiều GPU. Partial result của matrix multiplication cần collective communication để ghép lại.

Phù hợp nhất khi có high-speed interconnect, thường trong cùng node.

## Pipeline Parallelism

Các layer được chia thành nhiều stage. Microbatch chạy xuyên pipeline.

Cần schedule để giảm pipeline bubble và cân bằng compute/memory giữa các stage.

## 3D Parallelism

Very large model thường kết hợp data, tensor và pipeline parallelism. Một số hệ thống còn thêm sequence hoặc expert parallelism.

Parallel topology phải khớp physical network topology.

## Communication Primitive

### All-Reduce

Sau phép all-reduce, mỗi worker nhận tensor đã được reduce, thường dùng để đồng bộ gradient.

### Reduce-Scatter + All-Gather

Có thể phân rã all-reduce thành hai operation này; chúng đặc biệt hữu ích cho sharded state.

### All-to-All

Quan trọng trong MoE token routing.

## Interconnect

GPU link trong cùng node thường nhanh hơn network giữa node. Tensor parallel communication diễn ra thường xuyên nên ưu tiên fast local link; data parallel thường scale qua node hiệu quả hơn.

## Gradient Synchronization

Tần suất synchronization ảnh hưởng semantics của optimization. Local SGD hoặc delayed sync giúp giảm communication nhưng cũng thay đổi learning dynamics.

## Communication Compression

Quantize hoặc sparsify gradient có thể giảm network traffic nhưng thêm approximation và overhead. Lợi ích phụ thuộc workload.

## Checkpointing

Large distributed checkpoint có thể đạt quy mô TB. Cần:

- shard-aware format;
- parallel write;
- atomic hoặc consistent checkpoint metadata;
- khả năng resume;
- retention policy.

Chỉ lưu weights thường không đủ để resume training nếu thiếu optimizer, scheduler hoặc RNG state.

## Xử lý Failure

Training job dài có xác suất gặp hardware hoặc node failure cao.

Hệ thống cần:

```text
health checks
checkpoint / restart
elastic membership nếu hỗ trợ
bad-node quarantine
retry policy
```

Khi số node tăng, xác suất một thành phần nào đó hỏng trong suốt job cũng tăng.

## Determinism

Thứ tự distributed reduction có thể thay đổi kết quả floating-point nhỏ. Cùng seed không bảo đảm run giống hệt.

Reproducibility nên ghi lại topology, world size và runtime version.

## Data Loading

Nếu storage không cấp dữ liệu đủ nhanh, accelerator sẽ idle. Distributed data loader cần:

- chia shard sample đúng;
- prefetch;
- cache;
- tránh duplicate sampling;
- deterministic epoch semantics khi cần.

## Chẩn đoán Straggler

Nên theo dõi theo từng rank:

```text
step time
forward / backward time
collective time
data wait
GPU utilization
```

Average có thể che một rank chậm đang làm cả job phải chờ.

## Mixed Precision

BF16, FP16 hoặc FP8 giúp giảm communication và memory bên cạnh compute cost. Tuy nhiên optimizer state hoặc numerical-sensitive operation có thể vẫn cần precision cao hơn.

## Scaling Law và Scaling Efficiency

Ngay cả khi thêm compute cải thiện model quality theo statistical scaling law, distributed system kém hiệu quả vẫn làm lãng phí budget. Algorithmic scaling và systems scaling là hai câu hỏi khác nhau.

## Training Throughput

Có thể đo samples/s hoặc tokens/s. Khi cần, có thể dùng metric kiểu **Model FLOPs Utilization (MFU)** để ước lượng tỷ lệ theoretical compute thực sự phục vụ model work.

Peak utilization cao chưa chắc tốt nếu phần lớn compute đến từ recomputation hoặc padding không hiệu quả.

## Chi phí của Large Batch

Global batch lớn giúp hardware utilization tốt hơn nhưng có thể thay đổi optimization và generalization. Hardware efficiency và statistical efficiency phải được tối ưu cùng nhau.

## Mô hình tư duy

```text
Distributed training = chia compute và state trong khi trả giá bằng communication, synchronization và failure complexity.
```

## Những nhầm lẫn thường gặp

### “Model không fit thì chỉ cần data parallelism”

Không. Data parallel replicate model; muốn giảm model state trên mỗi device cần sharding hoặc model parallelism.

### “Checkpoint weights là đủ để resume”

Không. Optimizer, scheduler, RNG và data position có thể cần thiết.

### “Thêm GPU luôn làm training rẻ hơn”

Không. Thời gian có thể giảm nhưng scaling kém có thể làm tổng accelerator-hour tăng.

## Liên kết kiến thức

Xem [Parallel Computing](./04_parallel_computing.md), [Memory/Bandwidth](./03_memory_and_bandwidth.md), [Cluster & Interconnect](./07_cluster_scheduling_and_interconnect.md), [Training Pipeline](../15_ai_engineering/01_training_pipeline.md).