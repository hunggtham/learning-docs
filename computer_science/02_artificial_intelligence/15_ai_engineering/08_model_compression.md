# Model Compression: nhìn toàn bộ bài toán giảm chi phí mô hình

**Nén mô hình (model compression / 모델 압축)** là khái niệm bao trùm các kỹ thuật giảm memory, compute, bandwidth hoặc latency trong khi vẫn giữ chất lượng đủ tốt cho deployment target. Quantization, pruning và distillation là ba nhóm lớn, nhưng compression còn bao gồm low-rank factorization, parameter sharing, đơn giản hóa kiến trúc và tối ưu theo runtime cụ thể.

Điểm quan trọng là compression phải được đánh giá theo **mục tiêu của toàn hệ thống (system objective)**, không chỉ theo file size.

## Mục tiêu của Compression

Một project có thể muốn giảm:

```text
weight memory
activation memory
KV-cache memory
FLOPs
memory bandwidth
latency
energy
cost/request
startup time
```

Các mục tiêu này không hoàn toàn đồng nhất. Giảm parameter count chưa chắc giảm latency nếu workload vẫn bị giới hạn bởi bandwidth hoặc kernel chưa tối ưu.

## Low-Rank Factorization

Nếu weight matrix `W` có thể được xấp xỉ bằng rank thấp:

\[
W\approx AB
\]

với `A∈R^{m×r}`, `B∈R^{r×n}`, `r << min(m,n)`, số parameter giảm từ `mn` xuống `r(m+n)`.

SVD cho trực giác rằng nhiều phép biến đổi có **effective rank** thấp hơn dimension đầy đủ.

Low-rank adaptation như LoRA dùng ý tưởng liên quan, nhưng mục tiêu chính của LoRA là parameter-efficient fine-tuning, không mặc định là deployment compression.

## Weight Sharing

Nhiều weight có thể dùng chung một value hoặc parameter block. Cách này giúp giảm storage nhưng có thể làm optimization khó hơn.

Compression truyền thống có vector quantization hoặc codebook; một số modern architecture cũng dùng module lặp lại hoặc shared parameter.

## Thiết kế lại Architecture

Đôi khi cách tốt nhất không phải compress một mô hình lớn sẵn có mà chọn architecture nhỏ hơn ngay từ đầu:

```text
smaller hidden size
fewer layers
smaller vocabulary
specialized encoder
mixture routing
```

Một mô hình nhỏ được thiết kế đúng mục đích có thể tốt hơn một mô hình lớn bị compress quá mạnh.

## Quantization, Pruning và Distillation

Ba kỹ thuật này tác động vào các chiều khác nhau:

```text
Quantization  → ít bit hơn cho mỗi giá trị
Pruning       → ít parameter hoặc structure hoạt động hơn
Distillation  → một hàm xấp xỉ được học với mô hình nhỏ hơn
```

Có thể kết hợp chúng, nhưng lỗi do từng bước cũng có thể cộng dồn.

## Weight Compression và Runtime Memory

Weight file nhỏ không bảo đảm runtime memory nhỏ vì còn:

- activations;
- optimizer state nếu training;
- KV cache;
- temporary workspace;
- model shard hoặc buffer bị duplicate.

Với long-context LLM serving, KV cache có thể chiếm memory nhiều hơn weights.

## Compression Ratio

\[
Compression\ Ratio=\frac{Original\ Size}{Compressed\ Size}
\]

Tỷ lệ này chỉ phản ánh storage; cần xem thêm quality, latency và cost.

## Pareto Frontier

Compression là một bài toán tối ưu nhiều mục tiêu (multi-objective optimization).

Ta muốn mô hình nằm trên **Pareto frontier** giữa:

```text
quality ↔ latency ↔ memory ↔ cost
```

Một mô hình không Pareto-efficient nếu tồn tại mô hình khác vừa rẻ hơn vừa tốt hơn.

## Benchmark trên đúng Hardware

Kết quả compression phải được benchmark trên hardware và runtime mục tiêu. Một INT4 kernel có thể rất nhanh trên GPU này nhưng kém hiệu quả trên CPU hoặc accelerator khác.

Benchmark trong paper không thể thay thế production benchmark.

## Đánh giá sau Compression

Evaluation cần kiểm tra:

- chất lượng task tổng thể;
- calibration;
- long-tail case;
- long context;
- multilingual behavior;
- structured output hoặc tool calling;
- safety constraint;
- latency và cost.

## Specialized Small Model

Một mô hình nhỏ chuyên biệt theo domain kết hợp retrieval hoặc tool có thể vượt generic large model trên narrow workload với cost thấp hơn nhiều.

Vì vậy compression không chỉ là bước hậu xử lý sau training; nó còn liên quan tới model selection và system architecture.

## Edge Deployment

Thiết bị mobile hoặc embedded có constraint mạnh về RAM, power và thermal. Compression khi đó phải xét cùng operator support, hardware acceleration và package size.

## Khi nào không nên Compression?

Nếu inference volume thấp và engineering complexity cao, compression có thể không đáng. Không nên tối ưu trước khi profiling chỉ ra bottleneck thật sự.

## Mô hình tư duy

```text
Compression = giữ lại hàm hữu ích trong khi giảm chi phí vật lý để lưu trữ và thực thi nó
```

## Những nhầm lẫn thường gặp

### “Model file nhỏ hơn nghĩa là system nhanh hơn”

Không nhất thiết. Runtime bottleneck mới quyết định performance thực tế.

### “Compression chỉ là quantization”

Không. Quantization chỉ là một family trong nhiều kỹ thuật compression.

### “Compress một lần là xong”

Không. Model, data và runtime thay đổi có thể làm trade-off thay đổi, vì vậy cần đánh giá lại.

## Liên kết kiến thức

Xem [Quantization](./06_quantization.md), [Pruning and Distillation](./07_pruning_and_distillation.md), [Latency, Throughput and Cost](./09_latency_throughput_and_cost.md) và [AI Compute](../17_ai_compute_and_infrastructure/README.md).