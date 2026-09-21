# Parallel Computing trong AI

Deep Learning có thể scale lớn vì phần lớn tensor operation có thể chạy song song. Nhưng **xử lý song song (parallelism / 병렬 처리)** không phải một kỹ thuật duy nhất. Ta có thể song song theo data, model dimension, pipeline stage hoặc request. Mỗi cách tạo communication pattern, memory footprint và synchronization overhead khác nhau.

## Parallelism ở nhiều cấp

```text
instruction-level
thread-level
kernel-level
GPU-level
node-level
cluster-level
request-level
```

AI engineer thường quan tâm từ tensor operation lên cluster và request.

## Data Parallelism

Mỗi device giữ một bản đầy đủ của model và xử lý mini-batch khác nhau.

```text
GPU0: batch A → gradients
GPU1: batch B → gradients
...
all-reduce gradients
optimizer step
```

Ưu điểm: đơn giản và hiệu quả khi model fit trên mỗi GPU.

Nhược điểm: mỗi device vẫn phải chứa full model và optimizer state.

## Synchronous và Asynchronous

Synchronous data parallel chờ tất cả worker rồi mới aggregate. Semantics ổn định nhưng một straggler chậm có thể làm cả group phải chờ.

Asynchronous update giảm thời gian chờ nhưng tạo stale gradient và làm optimization khó hơn.

Large-scale training hiện đại thường ưu tiên synchronous collective kết hợp interconnect tối ưu.

## Tensor Parallelism

Chia một tensor hoặc matrix operation qua nhiều device.

Ví dụ split weight matrix theo column hoặc row. Mỗi layer cần trao đổi partial result.

Ưu điểm: layer lớn hơn memory của một GPU vẫn có thể chạy.

Nhược điểm: communication diễn ra thường xuyên, nên cần interconnect bandwidth cao.

## Pipeline Parallelism

Chia các layer thành nhiều stage:

```text
GPU group 1 → layers 1–N
GPU group 2 → layers N+1–M
...
```

Microbatch đi xuyên pipeline.

Có **pipeline bubble** khi một stage idle ở đầu/cuối pipeline hoặc khi load không cân bằng.

## Sequence Parallelism

Chia sequence dimension cho một số operation, giúp giảm activation memory và bổ trợ tensor parallelism.

## Expert Parallelism

Mixture-of-Experts route token tới các expert group khác nhau.

Lợi ích: tăng total parameter nhưng active compute trên mỗi token thấp hơn dense model tương đương.

Đổi lại cần all-to-all communication và load balancing phức tạp.

## Hybrid Parallelism

Large training thường kết hợp:

```text
data parallel
× tensor parallel
× pipeline parallel
× expert / sequence parallel
```

Cách ánh xạ các chiều parallelism vào topology phần cứng là một bài toán system design.

## Collective Communication

Các collective phổ biến:

- all-reduce;
- all-gather;
- reduce-scatter;
- broadcast;
- all-to-all.

All-reduce gradient là operation cốt lõi của data parallel.

## Chồng lấp Communication và Computation

Runtime có thể truyền gradient của layer trước trong khi backward pass vẫn đang tính layer sau. Overlap này giúp giảm phần communication time lộ ra ngoài.

Nếu communication chỉ bắt đầu sau khi compute kết thúc, scaling thường kém hơn.

## Straggler

Một GPU hoặc node chậm có thể làm synchronous group phải chờ. Nguyên nhân có thể là:

- hardware issue;
- network congestion;
- workload không đều;
- thermal throttling;
- data loading chậm.

Distributed training nên monitor timing theo từng rank.

## Load Balancing

Pipeline stage cần lượng compute gần cân bằng. MoE expert cần token load cân bằng. Serving nhiều request cần route concurrency theo available memory và capacity.

## Gradient Accumulation

Nếu physical batch trên mỗi GPU nhỏ, có thể accumulate nhiều microbatch trước optimizer step. Đây là kỹ thuật theo thời gian để đạt effective batch lớn hơn, không phải distributed parallelism theo nghĩa trực tiếp.

## Parallel Inference

Serving có hai dạng chính:

```text
model parallelism   → một request dùng nhiều device
request parallelism → nhiều replica xử lý các request khác nhau
```

Request parallelism scale throughput tốt khi model fit một device. Model parallelism cần khi model quá lớn hoặc latency target yêu cầu nhiều device cùng xử lý một request.

## Prefill–Decode Disaggregation

LLM serving có thể tách resource pool cho prefill và decode vì hai phase có profile compute/memory khác nhau. Đây là một dạng specialized pipeline decomposition trong serving architecture.

## Amdahl's Law

Nếu tỷ lệ serial là `s`:

\[
Speedup(N)=\frac{1}{s+\frac{1-s}{N}}
\]

Khi `N` lớn, serial section và communication overhead chi phối. Scale-out không thể tăng vô hạn.

## Strong Scaling và Weak Scaling

**Strong scaling**: problem size cố định, tăng device để giảm thời gian chạy.

**Weak scaling**: problem size tăng cùng số device, giữ lượng work trên mỗi device gần ổn định.

Large AI thường weak-scale model hoặc data size thay vì chỉ dùng nhiều device để chạy cùng một job cũ nhanh hơn.

## Mô hình tư duy

```text
Parallelism đổi local work lấy coordination overhead.
```

Lợi ích chỉ xuất hiện khi lượng compute tiết kiệm được lớn hơn communication và synchronization overhead.

## Những nhầm lẫn thường gặp

### “N GPU = nhanh N lần”

Không. Communication, synchronization và serial section làm efficiency giảm.

### “Tensor parallelism và data parallelism giống nhau”

Không. Tensor parallelism chia model computation; data parallelism replicate model và chia data.

### “Distributed training chỉ cần thêm máy”

Không. Topology, collective, checkpointing và failure handling trở thành bài toán hạng nhất.

## Liên kết kiến thức

Xem [Distributed Training](./05_distributed_training.md), [Distributed Inference](./06_distributed_inference.md), [Memory/Bandwidth](./03_memory_and_bandwidth.md), [Deep Learning Training](../05_neural_networks/09_training_dynamics.md).