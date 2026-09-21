# CPU, GPU, TPU và AI Accelerator

AI workload có thể chạy trên nhiều loại compute hardware. Không có accelerator “tốt nhất” cho mọi task; mỗi architecture tối ưu một pattern computation khác nhau.

## CPU

**CPU (Central Processing Unit / 중앙처리장치)** mạnh ở control flow, công việc single-thread có latency thấp, logic tổng quát và software ecosystem lớn.

CPU có ít core hơn GPU nhưng mỗi core phức tạp hơn, cache hierarchy mạnh và branch prediction tốt.

Phù hợp với:

- preprocessing;
- classical ML;
- orchestration;
- small-model inference;
- irregular workload;
- data pipeline và control plane.

## GPU

**GPU (Graphics Processing Unit / 그래픽 처리 장치)** có rất nhiều execution unit và tối ưu throughput cho numerical workload có tính song song cao.

Deep Learning sử dụng matrix multiplication, convolution và tensor operation quy mô lớn nên map rất tốt lên GPU.

Trade-off của GPU:

```text
+ parallel throughput cao
+ AI ecosystem trưởng thành
+ hỗ trợ mixed precision mạnh
- memory đắt
- power consumption cao
- cần batching hoặc parallel work đủ lớn để tận dụng tốt
```

## TPU và Domain-Specific Accelerator

**TPU (Tensor Processing Unit)** là accelerator được thiết kế cho tensor và matrix workload. Các vendor khác cũng có NPU, AI ASIC và custom inference chip.

Hardware chuyên biệt có thể tối ưu:

- matrix multiply;
- low precision;
- on-chip memory và dataflow;
- power efficiency.

Đổi lại portability và ecosystem thường hẹp hơn GPU.

## NPU trên thiết bị

Điện thoại và laptop ngày càng có **Neural Processing Unit (NPU)**. NPU hướng tới local inference tiết kiệm điện cho vision, audio hoặc generative model nhỏ hơn.

Các constraint thường gồm:

- memory;
- operator được hỗ trợ;
- thermal và power;
- quantization format.

## Trực giác SIMD và SIMT

CPU có SIMD vector instruction. GPU thường dùng execution kiểu **SIMT (Single Instruction, Multiple Threads)**: nhiều thread thực thi instruction stream tương tự nhau.

Branch divergence làm GPU kém hiệu quả nếu các thread trong cùng group đi theo control-flow path khác nhau.

## Tensor Core và Matrix Unit

Accelerator hiện đại thường có dedicated matrix-multiply unit tối ưu low-precision hoặc mixed-precision operation.

Tensor shape và precision của model phải phù hợp mới tận dụng được hardware peak.

## Host và Device

GPU thường là device riêng với VRAM hoặc HBM. CPU host chuẩn bị data và launch kernel.

Truyền dữ liệu host-device có cost. Nếu pipeline liên tục copy tensor nhỏ qua lại, lợi thế của accelerator giảm đáng kể.

## Unified Memory

Một số hệ thống có shared hoặc unified memory architecture. Điều này giảm complexity của explicit transfer, nhưng bandwidth và latency semantics vẫn cần được hiểu rõ.

## Chọn Hardware cho Training

Training large model cần xét:

```text
memory capacity
compute throughput
interconnect bandwidth
software / kernel support
reliability
cost và availability
```

Một accelerator đơn lẻ rất nhanh nhưng interconnect yếu có thể thua cluster khác trong distributed training.

## Chọn Hardware cho Inference

Serving cần xem:

- batch và concurrency;
- latency SLO;
- model có fit memory không;
- precision;
- token throughput;
- power và cost.

Small model với QPS thấp có thể kinh tế hơn trên CPU so với dedicated GPU.

## Edge và Cloud

Cloud accelerator cung cấp scale và managed infrastructure. Edge inference giảm network latency, tăng privacy và khả năng offline nhưng bị giới hạn hardware.

Kiến trúc hybrid có thể là:

```text
mô hình nhỏ trên thiết bị
→ gọi cloud large model khi cần
```

## Compiler và Runtime cũng quyết định Performance

Hardware peak chỉ có ý nghĩa nếu framework, compiler và runtime tạo được kernel hiệu quả. Operator không được hỗ trợ có thể fallback sang slow path.

## Benchmarking

Benchmark phải dùng model thật, batch size thật, precision thật và target runtime thật. Peak specification của vendor không thay được workload benchmark.

## Hiệu quả năng lượng

Có thể đo bằng tokens/joule hoặc inferences/watt. Ở datacenter scale, power và cooling trở thành một ràng buộc kinh tế lớn.

## Mô hình tư duy

```text
CPU = control linh hoạt + tính toán tổng quát
GPU = massively parallel tensor throughput
ASIC / TPU / NPU = dataflow chuyên biệt để tăng hiệu quả
```

## Những nhầm lẫn thường gặp

### “GPU luôn nhanh hơn CPU”

Không. Irregular hoặc small workload và host-device transfer overhead có thể làm CPU phù hợp hơn.

### “Accelerator có TFLOPS cao hơn chắc chắn tốt hơn”

Không. Memory, interconnect, kernel và precision/operator support quyết định effective performance.

### “Model chạy được nghĩa là model chạy tối ưu”

Không. Fallback kernel hoặc tensor shape không phù hợp có thể làm utilization thấp.

## Liên kết kiến thức

Xem [GPU Architecture](./02_gpu_architecture.md), [Memory and Bandwidth](./03_memory_and_bandwidth.md), [Parallel Computing](./04_parallel_computing.md) và [Model Serving](../15_ai_engineering/03_model_serving.md).