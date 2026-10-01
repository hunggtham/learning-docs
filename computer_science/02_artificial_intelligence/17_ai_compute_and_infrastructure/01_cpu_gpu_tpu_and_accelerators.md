# CPU, GPU, TPU và AI Accelerator

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **CPU, GPU, TPU và AI Accelerator**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **CPU** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **GPU** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

AI tải công việc (workload / 워크로드) có thể chạy trên nhiều loại compute hardware. Không có accelerator “tốt nhất” cho mọi tác vụ (task / 작업); mỗi kiến trúc (architecture / 아키텍처) tối ưu một mẫu (pattern / 패턴) computation khác nhau.

## CPU

**CPU (Central Processing Unit / 중앙처리장치)** mạnh ở điều khiển (control / 제어) luồng (flow / 흐름), công việc single-thread có độ trễ (latency / 지연 시간) thấp, lô-gic (logic / 논리) tổng quát và software ecosystem lớn.

CPU có ít cốt lõi (core / 핵심) hơn GPU nhưng mỗi cốt lõi (core / 핵심) phức tạp hơn, bộ nhớ đệm (cache / 캐시) hierarchy mạnh và branch prediction tốt.

Phù hợp với:

- preprocessing;
- classical ML;
- orchestration;
- small-model suy luận (inference / 추론);
- irregular tải công việc (workload / 워크로드);
- dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) và điều khiển (control / 제어) plane.

> **Chuyển mạch:** Trong **CPU, GPU, TPU và AI Accelerator**, **GPU** tiếp nhận điểm tựa từ **CPU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TPU và Domain-Specific Accelerator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## GPU

**GPU (Graphics Processing Unit / 그래픽 처리 장치)** có rất nhiều đơn vị thực thi (execution unit / 실행 유닛) và tối ưu thông lượng (throughput / 처리량) cho numerical tải công việc (workload / 워크로드) có tính song song cao.

Deep học tập (learning / 학습) sử dụng phép nhân ma trận (matrix multiplication / 행렬 곱셈), convolution và tensor thao tác (operation / 연산) quy mô lớn nên map rất tốt lên GPU.

Sự đánh đổi (trade-off / 트레이드오프) của GPU:

```text
+ parallel throughput cao
+ AI ecosystem trưởng thành
+ hỗ trợ mixed precision mạnh
- memory đắt
- power consumption cao
- cần batching hoặc parallel work đủ lớn để tận dụng tốt
```

> **Chuyển mạch:** Ở chặng này của **CPU, GPU, TPU và AI Accelerator**, **TPU và Domain-Specific Accelerator** tiếp nhận điểm tựa từ **GPU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NPU trên thiết bị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TPU và Domain-Specific Accelerator

**TPU (Tensor Processing Unit)** là accelerator được thiết kế cho tensor và ma trận (matrix / 행렬) tải công việc (workload / 워크로드). Các vendor khác cũng có NPU, AI ASIC và custom suy luận (inference / 추론) chip.

Hardware chuyên biệt có thể tối ưu:

- ma trận (matrix / 행렬) multiply;
- low precision;
- on-chip bộ nhớ (memory / 메모리) và dataflow;
- power efficiency.

Đổi lại portability và ecosystem thường hẹp hơn GPU.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU, GPU, TPU và AI Accelerator**, **NPU trên thiết bị** tiếp nhận điểm tựa từ **TPU và Domain-Specific Accelerator** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác SIMD và SIMT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NPU trên thiết bị

Điện thoại và laptop ngày càng có **Neural Processing đơn vị (unit / 단위) (NPU)**. NPU hướng tới cục bộ (local / 로컬) suy luận (inference / 추론) tiết kiệm điện cho vision, audio hoặc generative mô hình (model / 모델) nhỏ hơn.

Các ràng buộc (constraint / 제약조건) thường gồm:

- bộ nhớ (memory / 메모리);
- operator được hỗ trợ;
- thermal và power;
- quantization format.

> **Chuyển mạch:** Trong **CPU, GPU, TPU và AI Accelerator**, **Trực giác SIMD và SIMT** tiếp nhận điểm tựa từ **NPU trên thiết bị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tensor cốt lõi (core / 핵심) và ma trận (matrix / 행렬) đơn vị (unit / 단위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác SIMD và SIMT

CPU có SIMD véc-tơ (vector / 벡터) instruction. GPU thường dùng thực thi (execution / 실행) kiểu **SIMT (Single Instruction, Multiple Threads)**: nhiều luồng thực thi (thread / 스레드) thực thi instruction stream tương tự nhau.

Branch divergence làm GPU kém hiệu quả nếu các luồng thực thi (thread / 스레드) trong cùng group đi theo control-flow đường dẫn (path / 경로) khác nhau.

> **Chuyển mạch:** Ở chặng này của **CPU, GPU, TPU và AI Accelerator**, **Tensor cốt lõi (core / 핵심) và ma trận (matrix / 행렬) đơn vị (unit / 단위)** tiếp nhận điểm tựa từ **Trực giác SIMD và SIMT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Host và thiết bị (device / 장치)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tensor cốt lõi (core / 핵심) và ma trận (matrix / 행렬) đơn vị (unit / 단위)

Accelerator hiện đại thường có dedicated matrix-multiply đơn vị (unit / 단위) tối ưu low-precision hoặc mixed-precision thao tác (operation / 연산).

Tensor shape và precision của mô hình (model / 모델) phải phù hợp mới tận dụng được hardware peak.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU, GPU, TPU và AI Accelerator**, **Host và thiết bị (device / 장치)** tiếp nhận điểm tựa từ **Tensor cốt lõi (core / 핵심) và ma trận (matrix / 행렬) đơn vị (unit / 단위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Unified bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Host và thiết bị (device / 장치)

GPU thường là thiết bị (device / 장치) riêng với VRAM hoặc HBM. CPU host chuẩn bị dữ liệu (data / 데이터) và launch kernel.

Truyền dữ liệu host-device có chi phí (cost / 비용). Nếu chuỗi xử lý (pipeline / 파이프라인) liên tục bản sao (copy / 복사) tensor nhỏ qua lại, lợi thế của accelerator giảm đáng kể.

> **Chuyển mạch:** Trong **CPU, GPU, TPU và AI Accelerator**, **Unified bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Host và thiết bị (device / 장치)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chọn Hardware cho huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Unified bộ nhớ (memory / 메모리)

Một số hệ thống có dùng chung (shared / 공유) hoặc unified bộ nhớ (memory / 메모리) kiến trúc (architecture / 아키텍처). Điều này giảm độ phức tạp (complexity / 복잡도) của tường minh (explicit / 명시적) transfer, nhưng bandwidth và độ trễ (latency / 지연 시간) ngữ nghĩa (semantics / 의미론) vẫn cần được hiểu rõ.

> **Chuyển mạch:** Ở chặng này của **CPU, GPU, TPU và AI Accelerator**, **Chọn Hardware cho huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **Unified bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chọn Hardware cho suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chọn Hardware cho huấn luyện (training / 학습)

Huấn luyện (training / 학습) large mô hình (model / 모델) cần xét:

```text
memory capacity
compute throughput
interconnect bandwidth
software / kernel support
reliability
cost và availability
```

Một accelerator đơn lẻ rất nhanh nhưng interconnect yếu có thể thua cluster khác trong phân tán (distributed / 분산) huấn luyện (training / 학습).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU, GPU, TPU và AI Accelerator**, **Chọn Hardware cho suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Chọn Hardware cho huấn luyện (training / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Edge và Cloud** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chọn Hardware cho suy luận (inference / 추론)

Serving cần xem:

- batch và tính đồng thời (concurrency / 동시성);
- độ trễ (latency / 지연 시간) SLO;
- mô hình (model / 모델) có fit bộ nhớ (memory / 메모리) không;
- precision;
- đơn vị từ (token / 토큰) thông lượng (throughput / 처리량);
- power và chi phí (cost / 비용).

Small mô hình (model / 모델) với QPS thấp có thể kinh tế hơn trên CPU so với dedicated GPU.

> **Chuyển mạch:** Trong **CPU, GPU, TPU và AI Accelerator**, **Edge và Cloud** tiếp nhận điểm tựa từ **Chọn Hardware cho suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trình biên dịch (compiler / 컴파일러) và thời gian chạy (runtime / 런타임) cũng quyết định hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Edge và Cloud

Cloud accelerator cung cấp quy mô (scale / 규모) và managed hạ tầng (infrastructure / 인프라). Edge suy luận (inference / 추론) giảm mạng (network / 네트워크) độ trễ (latency / 지연 시간), tăng privacy và khả năng offline nhưng bị giới hạn hardware.

Kiến trúc hybrid có thể là:

```text
mô hình nhỏ trên thiết bị
→ gọi cloud large model khi cần
```

> **Chuyển mạch:** Ở chặng này của **CPU, GPU, TPU và AI Accelerator**, **Trình biên dịch (compiler / 컴파일러) và thời gian chạy (runtime / 런타임) cũng quyết định hiệu năng (performance / 성능)** tiếp nhận điểm tựa từ **Edge và Cloud** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Benchmarking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trình biên dịch (compiler / 컴파일러) và thời gian chạy (runtime / 런타임) cũng quyết định hiệu năng (performance / 성능)

Hardware peak chỉ có ý nghĩa nếu khung phần mềm (framework / 프레임워크), trình biên dịch (compiler / 컴파일러) và thời gian chạy (runtime / 런타임) tạo được kernel hiệu quả. Operator không được hỗ trợ có thể fallback sang slow đường dẫn (path / 경로).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU, GPU, TPU và AI Accelerator**, **Benchmarking** tiếp nhận điểm tựa từ **Trình biên dịch (compiler / 컴파일러) và thời gian chạy (runtime / 런타임) cũng quyết định hiệu năng (performance / 성능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu quả năng lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Benchmarking

Benchmark phải dùng mô hình (model / 모델) thật, batch kích thước (size / 크기) thật, precision thật và mục tiêu (target / 대상) thời gian chạy (runtime / 런타임) thật. Peak specification của vendor không thay được tải công việc (workload / 워크로드) benchmark.

> **Chuyển mạch:** Trong **CPU, GPU, TPU và AI Accelerator**, **Hiệu quả năng lượng** tiếp nhận điểm tựa từ **Benchmarking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu quả năng lượng

Có thể đo bằng tokens/joule hoặc inferences/watt. Ở datacenter quy mô (scale / 규모), power và cooling trở thành một ràng buộc kinh tế lớn.

> **Chuyển mạch:** Ở chặng này của **CPU, GPU, TPU và AI Accelerator**, **Mô hình tư duy** gom các mảnh từ **Hiệu quả năng lượng** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
CPU = control linh hoạt + tính toán tổng quát
GPU = massively parallel tensor throughput
ASIC / TPU / NPU = dataflow chuyên biệt để tăng hiệu quả
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU, GPU, TPU và AI Accelerator**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “GPU luôn nhanh hơn CPU”

Không. Irregular hoặc small tải công việc (workload / 워크로드) và host-device transfer overhead có thể làm CPU phù hợp hơn.

### “Accelerator có TFLOPS cao hơn chắc chắn tốt hơn”

Không. bộ nhớ (memory / 메모리), interconnect, kernel và precision/operator hỗ trợ (support / 지원) quyết định effective hiệu năng (performance / 성능).

### “mô hình (model / 모델) chạy được nghĩa là mô hình (model / 모델) chạy tối ưu”

Không. Fallback kernel hoặc tensor shape không phù hợp có thể làm utilization thấp.

> **Chuyển mạch:** Trong **CPU, GPU, TPU và AI Accelerator**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [GPU Architecture](./02_gpu_architecture.md), [Memory and Bandwidth](./03_memory_and_bandwidth.md), [Parallel Computing](./04_parallel_computing.md) và [Model Serving](../15_ai_engineering/03_model_serving.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
