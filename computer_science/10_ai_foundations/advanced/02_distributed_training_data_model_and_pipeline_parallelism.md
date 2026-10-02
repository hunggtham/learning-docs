# Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Distributed training: data, model và pipeline parallelism**. Route đi từ device capacity/throughput → data/model/pipeline partitioning → worker-step invariant → communication/synchronization → fault recovery, để scale training không phá convergence.

Mô hình hiện đại có thể quá lớn hoặc quá chậm để huấn luyện trên một accelerator. **Huấn luyện phân tán (distributed training)** chia computation, parameters, gradients, optimizer trạng thái (state / 상태) và activations qua nhiều devices/nodes. Nhưng thêm GPU chỉ hữu ích khi communication, synchronization, bộ nhớ (memory / 메모리) và đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인) không trở thành bottleneck mới.

Mô hình tư duy (mental model / 사고 모델) của chương này là: **phân tán (distributed / 분산) huấn luyện (training / 학습) là một synchronous/asynchronous máy trạng thái (state machine / 상태 머신) của mô hình (model / 모델) trạng thái (state / 상태)**. tính đúng đắn (correctness / 정확성) cần workers cập nhật từ một logically compatible huấn luyện (training / 학습) step/trạng thái (state / 상태); hiệu năng (performance / 성능) phụ thuộc computation-to-communication ratio, topology, straggler hành vi (behavior / 동작), chuỗi xử lý (pipeline / 파이프라인) bubbles và checkpoint/restart debt.

## 1. Bài toán ban đầu: một thiết bị (device / 장치) không đủ sức chứa (capacity / 용량) hoặc thông lượng (throughput / 처리량)

Có hai pressures khác nhau:

```text
memory capacity problem:
model + optimizer + activations không fit một device

throughput/time problem:
model fit nhưng training quá chậm
```

Dữ liệu (data / 데이터) parallelism thường giải thông lượng (throughput / 처리량); tensor/mô hình (model / 모델)/chuỗi xử lý (pipeline / 파이프라인)/sharded-state approaches giúp cả bộ nhớ (memory / 메모리) và compute. Chọn parallelism phải bắt đầu từ pressure nào đang dominate.

> **Chuyển mạch:** Trong **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **2. bất biến (invariant / 불변식) huấn luyện (training / 학습) step: workers phải agree trạng thái (state / 상태) theo thuật toán (algorithm / 알고리즘) đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **1. Bài toán ban đầu: một thiết bị (device / 장치) không đủ sức chứa (capacity / 용량) hoặc thông lượng (throughput / 처리량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. dữ liệu (data / 데이터) parallelism nhân batch công việc (work / 작업), rồi phải reconcile gradients** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. bất biến (invariant / 불변식) huấn luyện (training / 학습) step: workers phải agree trạng thái (state / 상태) theo thuật toán (algorithm / 알고리즘) đặc tả hợp đồng (contract / 계약)

Với synchronous dữ liệu (data / 데이터) parallelism, bất biến (invariant / 불변식) đơn giản hóa là:

> Mỗi logical tối ưu hóa (optimization / 최적화) step phải aggregate gradients theo quy tắc (rule / 규칙) đã định từ workers dùng compatible parameter phiên bản (version / 버전), rồi cập nhật (update / 업데이트) mô hình (model / 모델) trạng thái (state / 상태) theo optimizer ngữ nghĩa (semantics / 의미론).

Nếu worker dùng stale parameter phiên bản (version / 버전) hoặc collective thiếu một subset ngoài giao thức (protocol / 프로토콜), kết quả (result / 결과) có thể không còn tương đương thuật toán (algorithm / 알고리즘) intended.

Phân tán (distributed / 분산) thời gian chạy (runtime / 런타임) vì vậy không chỉ “send tensors”; nó duy trì step membership, thứ tự (ordering / 순서) và trạng thái (state / 상태) phiên bản (version / 버전).

> **Chuyển mạch:** Ở chặng này của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **2. bất biến (invariant / 불변식) huấn luyện (training / 학습) step: workers phải agree trạng thái (state / 상태) theo thuật toán (algorithm / 알고리즘) đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **3. dữ liệu (data / 데이터) parallelism nhân batch công việc (work / 작업), rồi phải reconcile gradients** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. toàn cục (global / 전역) batch kích thước (size / 크기) là thuật toán (algorithm / 알고리즘) parameter, không chỉ các hệ thống (systems / 시스템들) knob** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. dữ liệu (data / 데이터) parallelism nhân batch công việc (work / 작업), rồi phải reconcile gradients

Mỗi worker giữ mô hình (model / 모델) replica và xử lý mini-batch subset. Sau backward pass, gradients được tổng hợp bằng collective như `all-reduce` hoặc reduce-scatter/all-gather composition.

Simplified:

```text
same parameter state
→ each worker forward/backward on local batch
→ aggregate gradients
→ optimizer update
→ next step state
```

Nếu compute per step nhỏ so với độ dốc (gradient / 기울기) bytes, communication dominates và scaling efficiency giảm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **3. dữ liệu (data / 데이터) parallelism nhân batch công việc (work / 작업), rồi phải reconcile gradients** nêu điều cần giải thích; **4. toàn cục (global / 전역) batch kích thước (size / 크기) là thuật toán (algorithm / 알고리즘) parameter, không chỉ các hệ thống (systems / 시스템들) knob** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. Collective communication có topology và đường găng (critical path / 임계 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. toàn cục (global / 전역) batch kích thước (size / 크기) là thuật toán (algorithm / 알고리즘) parameter, không chỉ các hệ thống (systems / 시스템들) knob

Tăng data-parallel workers thường tăng toàn cục (global / 전역) batch nếu per-device batch giữ nguyên. Điều này có thể đổi tối ưu hóa (optimization / 최적화) dynamics, learning-rate schedule và generalization.

Do đó benchmark “8 GPU nhanh hơn 1 GPU” phải phân biệt:

```text
strong scaling: same total problem/batch workload split thinner
weak scaling: work/batch grows with workers
```

Thông lượng (throughput / 처리량) speedup không tự chứng minh same huấn luyện (training / 학습) ngữ nghĩa (semantics / 의미론)/chất lượng (quality / 품질) trajectory.

> **Chuyển mạch:** Trong **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **4. toàn cục (global / 전역) batch kích thước (size / 크기) là thuật toán (algorithm / 알고리즘) parameter, không chỉ các hệ thống (systems / 시스템들) knob** xác định đầu vào; **5. Collective communication có topology và đường găng (critical path / 임계 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. Overlap compute và communication chỉ hiệu quả khi phụ thuộc (dependency / 의존성) cho phép** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Collective communication có topology và đường găng (critical path / 임계 경로)

`all-reduce`, `all-gather`, `reduce-scatter`, broadcast không phải thành phần nguyên thủy (primitive / 기본 요소) zero-cost. thuật toán (algorithm / 알고리즘) có thể dùng ring/cây (tree / 트리)/hierarchical topology.

Within-node interconnect thường nhanh hơn cross-node mạng (network / 네트워크). Efficient thời gian chạy (runtime / 런타임) cố map collectives theo topology:

```text
fast local links first
→ cross-node aggregation
→ local distribution
```

Nếu placement sai, same GPU count có thông lượng (throughput / 처리량) rất khác.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **5. Collective communication có topology và đường găng (critical path / 임계 경로)** xác định đầu vào; **6. Overlap compute và communication chỉ hiệu quả khi phụ thuộc (dependency / 의존성) cho phép** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **7. Straggler biến synchronous step thành barrier độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Overlap compute và communication chỉ hiệu quả khi phụ thuộc (dependency / 의존성) cho phép

Backward pass tạo gradients layer-by-layer. thời gian chạy (runtime / 런타임) có thể bucket và start communication cho earlier gradients trong khi lower layers vẫn compute.

Overlap bất biến (invariant / 불변식):

```text
gradient bucket chỉ được transmit/consume khi values ready
optimizer step chỉ dùng aggregate đúng step
```

Bucket quá lớn trì hoãn communication; quá nhỏ tăng launch/giao thức (protocol / 프로토콜) overhead. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) là schedule phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), không chỉ tăng bandwidth.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **7. Straggler biến synchronous step thành barrier độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **6. Overlap compute và communication chỉ hiệu quả khi phụ thuộc (dependency / 의존성) cho phép** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Tensor/mô hình (model / 모델) parallelism chia thao tác (operation / 연산) nhưng tăng communication frequency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Straggler biến synchronous step thành barrier độ trễ (latency / 지연 시간)

Trong synchronous huấn luyện (training / 학습), step completes theo slowest required worker/collective participant.

Sources:

```text
GPU thermal/power variation
network congestion/retransmission
input pipeline stall
host CPU contention
memory pressure
one node hardware degradation
imbalanced batch/sequence lengths
```

Một worker chậm 20% có thể làm nhiều workers rảnh chờ. Average GPU utilization không đủ; cần per-rank timeline/skew.

> **Chuyển mạch:** Trong **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **8. Tensor/mô hình (model / 모델) parallelism chia thao tác (operation / 연산) nhưng tăng communication frequency** tiếp nhận điểm tựa từ **7. Straggler biến synchronous step thành barrier độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. chuỗi xử lý (pipeline / 파이프라인) parallelism chia layers thành stages** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Tensor/mô hình (model / 모델) parallelism chia thao tác (operation / 연산) nhưng tăng communication frequency

Khi tầng (layer / 계층)/mô hình (model / 모델) không fit một accelerator, ma trận (matrix / 행렬)/tensors có thể shard. Mỗi forward/backward tầng (layer / 계층) thường cần collective exchange.

Sự đánh đổi (trade-off / 트레이드오프):

```text
per-device memory ↓
per-device compute split
↔
collective communication + synchronization ↑
```

Granularity quá nhỏ làm compute kernel ngắn nhưng collective overhead gần như giữ nguyên, dẫn efficiency collapse.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **8. Tensor/mô hình (model / 모델) parallelism chia thao tác (operation / 연산) nhưng tăng communication frequency** xác định đầu vào; **9. chuỗi xử lý (pipeline / 파이프라인) parallelism chia layers thành stages** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **10. chuỗi xử lý (pipeline / 파이프라인) schedule đổi memory-vs-bubble sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. chuỗi xử lý (pipeline / 파이프라인) parallelism chia layers thành stages

Stages nhận micro-batches theo chuỗi xử lý (pipeline / 파이프라인):

```text
Stage 1 → Stage 2 → Stage 3 → Stage 4
```

Bottleneck stage quyết định thông lượng (throughput / 처리량). Fill/drain tạo **chuỗi xử lý (pipeline / 파이프라인) bubbles**.

Partition phải cân compute + activation transfer, không chỉ equal number of layers. Một stage attention/communication-heavy có thể chậm hơn nhiều dù có cùng tầng (layer / 계층) count.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **9. chuỗi xử lý (pipeline / 파이프라인) parallelism chia layers thành stages** xác định đầu vào; **10. chuỗi xử lý (pipeline / 파이프라인) schedule đổi memory-vs-bubble sự đánh đổi (trade-off / 트레이드오프)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **11. Optimizer trạng thái (state / 상태) lớn hơn parameter tệp (file / 파일) trực giác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. chuỗi xử lý (pipeline / 파이프라인) schedule đổi memory-vs-bubble sự đánh đổi (trade-off / 트레이드오프)

Nhiều micro-batches tăng chuỗi xử lý (pipeline / 파이프라인) utilization nhưng giữ nhiều activations in-flight, tăng bộ nhớ (memory / 메모리). Activation checkpointing/recomputation có thể giảm bộ nhớ (memory / 메모리) bằng cách tính lại forward intermediates trong backward.

Sự đánh đổi (trade-off / 트레이드오프):

```text
memory ↓
↔
extra compute ↑
```

Phân tán (distributed / 분산) huấn luyện (training / 학습) thường là tối ưu hóa (optimization / 최적화) multidimensional: bộ nhớ (memory / 메모리) saved ở one technique có thể tạo compute/mạng (network / 네트워크) pressure elsewhere.

> **Chuyển mạch:** Trong **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **10. chuỗi xử lý (pipeline / 파이프라인) schedule đổi memory-vs-bubble sự đánh đổi (trade-off / 트레이드오프)** xác định đầu vào; **11. Optimizer trạng thái (state / 상태) lớn hơn parameter tệp (file / 파일) trực giác** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **12. Sharded optimizer/parameter trạng thái (state / 상태) đổi bộ nhớ (memory / 메모리) thành collectives** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Optimizer trạng thái (state / 상태) lớn hơn parameter tệp (file / 파일) trực giác

Huấn luyện (training / 학습) bộ nhớ (memory / 메모리) không chỉ parameters. Có thể gồm:

```text
parameters
master/low-precision copies
gradients
optimizer moments/state
activations
communication buckets
temporary kernel workspace
allocator fragmentation
```

Adam-like optimizers có multiple trạng thái (state / 상태) tensors. “mô hình (model / 모델) weights 20 GB nên 24 GB GPU đủ” là sai sức chứa (capacity / 용량) mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **12. Sharded optimizer/parameter trạng thái (state / 상태) đổi bộ nhớ (memory / 메모리) thành collectives** tiếp nhận điểm tựa từ **11. Optimizer trạng thái (state / 상태) lớn hơn parameter tệp (file / 파일) trực giác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인) có thể làm GPU đói** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Sharded optimizer/parameter trạng thái (state / 상태) đổi bộ nhớ (memory / 메모리) thành collectives

ZeRO/FSDP-like families shard optimizer trạng thái (state / 상태), gradients và/hoặc parameters. Mỗi worker không cần giữ full copies mọi trạng thái (state / 상태), nhưng forward/backward có thể cần all-gather/reduce-scatter around layers/steps.

Bất biến (invariant / 불변식) là parameter shard assembled/available đúng phiên bản (version / 버전) tại điểm (point / 지점) computation cần nó; bộ nhớ (memory / 메모리) reclamation không được xảy ra trước collective/users hoàn tất.

Again, this is quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명) giao thức (protocol / 프로토콜) giống phân tán (distributed / 분산) buffer management.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **12. Sharded optimizer/parameter trạng thái (state / 상태) đổi bộ nhớ (memory / 메모리) thành collectives** xác định đầu vào; **13. đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인) có thể làm GPU đói** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **14. dữ liệu (data / 데이터) sharding phải giữ sampling ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인) có thể làm GPU đói

Nếu dữ liệu (data / 데이터) decode/tokenization/augmentation/lưu trữ (storage / 저장소) read không feed accelerator đủ nhanh, GPU utilization thấp dù communication tốt.

Dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) phải xét:

```text
storage throughput
CPU preprocessing
host-to-device transfer
shuffle/sampling semantics
worker shard assignment
prefetch buffers
```

Scaling GPU without scaling đầu vào (input / 입력) đường dẫn (path / 경로) chỉ nhân expensive idle sức chứa (capacity / 용량).

> **Chuyển mạch:** Trong **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, cơ chế trong **13. đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인) có thể làm GPU đói** cần được kiểm chứng bằng dấu vết cụ thể; **14. dữ liệu (data / 데이터) sharding phải giữ sampling ngữ nghĩa (semantics / 의미론)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **15. thất bại (failure / 실패) detection trong collective dễ biến một nút (node / 노드) fault thành whole-job stall** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. dữ liệu (data / 데이터) sharding phải giữ sampling ngữ nghĩa (semantics / 의미론)

Mỗi data-parallel worker thường nhận distinct dữ liệu (data / 데이터) shard per step/epoch. Duplicate/missing examples do sampler bug có thể thay huấn luyện (training / 학습) phân phối (distribution / 분포).

Determinism không luôn required, nhưng sampling đặc tả hợp đồng (contract / 계약) phải tường minh (explicit / 명시적). Khi restart worker/world kích thước (size / 크기) đổi, sharding/reseed ngữ nghĩa (semantics / 의미론) có thể đổi trajectory.

Tính đúng đắn (correctness / 정확성) ở đây là **huấn luyện (training / 학습) thuật toán (algorithm / 알고리즘)/dữ liệu (data / 데이터) phân phối (distribution / 분포)**, không chỉ tensors không crash.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **14. dữ liệu (data / 데이터) sharding phải giữ sampling ngữ nghĩa (semantics / 의미론)** nêu điều cần giải thích; **15. thất bại (failure / 실패) detection trong collective dễ biến một nút (node / 노드) fault thành whole-job stall** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Checkpoint là durability giao thức (protocol / 프로토콜) của huấn luyện (training / 학습) trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. thất bại (failure / 실패) detection trong collective dễ biến một nút (node / 노드) fault thành whole-job stall

Nếu rank chết hoặc mạng (network / 네트워크) partition, peers có thể khối (block / 블록) chờ collective completion tới hết thời gian chờ (timeout / 타임아웃). “GPU utilization 0” trên surviving ranks có nguyên nhân gốc (root cause / 근본 원인) là one missing participant.

Phân tán (distributed / 분산) thời gian chạy (runtime / 런타임) cần membership/thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론): thất bại (fail / 실패) fast job, elastic membership nếu thuật toán (algorithm / 알고리즘) supports, or restart from checkpoint.

Elasticity không trivial vì changing world kích thước (size / 크기) can alter batch/sampler/optimizer các giả định (assumptions / 가정들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **16. Checkpoint là durability giao thức (protocol / 프로토콜) của huấn luyện (training / 학습) trạng thái (state / 상태)** tiếp nhận điểm tựa từ **15. thất bại (failure / 실패) detection trong collective dễ biến một nút (node / 노드) fault thành whole-job stall** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. phân tán (distributed / 분산) checkpoint cần consistent snapshot ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Checkpoint là durability giao thức (protocol / 프로토콜) của huấn luyện (training / 학습) trạng thái (state / 상태)

Checkpoint cần đủ trạng thái (state / 상태) để restart theo guarantee desired:

```text
model parameters
optimizer state
scheduler/step counters
random/sampler state khi reproducibility cần
mixed-precision scaler/state
metadata describing sharding/world layout
```

Nếu chỉ save weights, có thể resume suy luận (inference / 추론) nhưng không thật sự resume optimizer trajectory.

> **Chuyển mạch:** Trong **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **17. phân tán (distributed / 분산) checkpoint cần consistent snapshot ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **16. Checkpoint là durability giao thức (protocol / 프로토콜) của huấn luyện (training / 학습) trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Checkpoint frequency là RPO-vs-I/O sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. phân tán (distributed / 분산) checkpoint cần consistent snapshot ngữ nghĩa (semantics / 의미론)

Khi trạng thái (state / 상태) sharded across workers, checkpoint không được mix shard từ step `N` với shard từ step `N+1` nếu format assumes one logical step.

Possible giao thức (protocol / 프로토콜) families: barrier/snapshot at safe điểm (point / 지점), versioned shard files with manifest/lần ghi nhận (commit / 커밋) marker, sao chép khi ghi (copy-on-write / 쓰기 시 복사)/background upload from immutable snapshot.

Bất biến (invariant / 불변식):

> Published checkpoint manifest chỉ tham chiếu (reference / 참조) a complete logically compatible set of shards.

Đây là same family với filesystem/cơ sở dữ liệu (database / 데이터베이스) crash consistency.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **18. Checkpoint frequency là RPO-vs-I/O sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **17. phân tán (distributed / 분산) checkpoint cần consistent snapshot ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Restart thời gian (time / 시간) là RTO và có thể bottleneck ở checkpoint fan-in/out** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Checkpoint frequency là RPO-vs-I/O sự đánh đổi (trade-off / 트레이드오프)

Checkpoint quá thường xuyên:

```text
storage/network I/O ↑
training step jitter ↑
object store pressure ↑
```

Quá thưa:

```text
failure → recompute many hours
```

Huấn luyện (training / 학습) RPO là amount of compute/trạng thái (state / 상태) progression chấp nhận mất, không chỉ dữ liệu (data / 데이터) bytes.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **19. Restart thời gian (time / 시간) là RTO và có thể bottleneck ở checkpoint fan-in/out** tiếp nhận điểm tựa từ **18. Checkpoint frequency là RPO-vs-I/O sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Scaling efficiency cần tách compute, communication, idle và đầu vào (input / 입력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Restart thời gian (time / 시간) là RTO và có thể bottleneck ở checkpoint fan-in/out

Loading multi-TB checkpoint từ remote lưu trữ (storage / 저장소) cho hundreds workers có thể saturate mạng (network / 네트워크)/lưu trữ (storage / 저장소) and create thundering herd.

Fast checkpoint ghi (write / 쓰기) but slow restore still gives poor độ tin cậy (reliability / 신뢰성). Measure both save and khôi phục (recovery / 복구) đường găng (critical path / 임계 경로).

> **Chuyển mạch:** Trong **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **20. Scaling efficiency cần tách compute, communication, idle và đầu vào (input / 입력)** tiếp nhận điểm tựa từ **19. Restart thời gian (time / 시간) là RTO và có thể bottleneck ở checkpoint fan-in/out** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. mạng (network / 네트워크) pressure có phase thay đổi (change / 변경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Scaling efficiency cần tách compute, communication, idle và đầu vào (input / 입력)

Nếu 8 GPU nhanh 5× 1 GPU, efficiency ~62.5%, nhưng number alone không giải cơ chế (mechanism / 메커니즘).

Per-step decomposition:

```text
useful compute
communication
pipeline bubble/idle
input wait
runtime/launch overhead
checkpoint/background work
```

Amdahl's Law gives intuition that non-scaling/coordination fraction limits speedup. At large quy mô (scale / 규모) even small serial/collective overhead dominates.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **21. mạng (network / 네트워크) pressure có phase thay đổi (change / 변경)** tiếp nhận điểm tựa từ **20. Scaling efficiency cần tách compute, communication, idle và đầu vào (input / 입력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Mixed tải công việc (workload / 워크로드)/cluster contention creates noisy neighbor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. mạng (network / 네트워크) pressure có phase thay đổi (change / 변경)

At small cluster, intra-node links dominate. Cross-node quy mô (scale / 규모) makes NIC/fabric topology important. At larger quy mô (scale / 규모), oversubscription, congestion, collective synchronization and thất bại (failure / 실패) xác suất (probability / 확률) all increase.

A job can have same average bandwidth but worse step p99 due to transient congestion on one collective participant. Tail matters because barrier waits for slowest required đường dẫn (path / 경로).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **22. Mixed tải công việc (workload / 워크로드)/cluster contention creates noisy neighbor** tiếp nhận điểm tựa từ **21. mạng (network / 네트워크) pressure có phase thay đổi (change / 변경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Numerical hành vi (behavior / 동작) may thay đổi (change / 변경) with reduction thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Mixed tải công việc (workload / 워크로드)/cluster contention creates noisy neighbor

Huấn luyện (training / 학습) jobs may share mạng (network / 네트워크)/lưu trữ (storage / 저장소)/CPU điều khiển (control / 제어) plane. Another job's checkpoint or shuffle can slow collectives/đầu vào (input / 입력) đường dẫn (path / 경로).

Tài nguyên (resource / 자원) scheduler that allocates GPUs but ignores fabric/lưu trữ (storage / 저장소) bandwidth can overcommit hidden bottleneck.

Cluster sức chứa (capacity / 용량) đơn vị (unit / 단위) therefore is not simply “number of GPUs”. It includes topology-local groups, NIC bandwidth, host bộ nhớ (memory / 메모리)/CPU and lưu trữ (storage / 저장소) đường dẫn (path / 경로).

> **Chuyển mạch:** Trong **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **23. Numerical hành vi (behavior / 동작) may thay đổi (change / 변경) with reduction thứ tự (order / 순서)** tiếp nhận điểm tựa từ **22. Mixed tải công việc (workload / 워크로드)/cluster contention creates noisy neighbor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Numerical hành vi (behavior / 동작) may thay đổi (change / 변경) with reduction thứ tự (order / 순서)

Floating-point addition is not perfectly associative. Different collective cây (tree / 트리)/thứ tự (order / 순서)/world kích thước (size / 크기) can produce small numerical differences. Usually huấn luyện (training / 학습) tolerates this, but reproducibility expectations must account for it.

“Same seed” does not automatically mean bit-identical phân tán (distributed / 분산) thực thi (execution / 실행) across topology/parallelism changes.

This connects computer arithmetic to phân tán (distributed / 분산) thuật toán (algorithm / 알고리즘) hành vi (behavior / 동작).

> **Chuyển mạch:** Ở chặng này của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **23. Numerical hành vi (behavior / 동작) may thay đổi (change / 변경) with reduction thứ tự (order / 순서)** nêu điều cần giải thích; **24. bằng chứng vận hành (production evidence / 운영 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **25. thất bại (failure / 실패) testing must include partial thất bại (failure / 실패) and slow thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) should align ranks + phases:

```text
Compute:
- kernel/GPU utilization per rank
- forward/backward time
- memory allocated/reserved/fragmentation

Communication:
- collective duration by type/layer/bucket
- bytes and effective bandwidth
- topology/link errors/congestion

Synchronization:
- per-rank step start/end
- straggler skew / idle time

Input:
- data-loader wait/prefetch occupancy
- host-to-device transfer

Reliability:
- checkpoint save/load duration
- checkpoint version/step
- worker failure/timeout/restart timeline
```

Aggregate GPU utilization can hide rank 7 stalling every step while others wait.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **24. bằng chứng vận hành (production evidence / 운영 증거)** nêu điều cần giải thích; **25. thất bại (failure / 실패) testing must include partial thất bại (failure / 실패) and slow thất bại (failure / 실패)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **26. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. thất bại (failure / 실패) testing must include partial thất bại (failure / 실패) and slow thất bại (failure / 실패)

Not only kill a worker. kiểm thử (test / 테스트):

```text
slow one rank
packet loss/latency on one node
input storage slowdown
checkpoint upload partial failure
restart from latest and previous checkpoint
world-size change if elasticity claimed
corrupt/missing shard manifest
```

After khôi phục (recovery / 복구) verify logical huấn luyện (training / 학습) step/trạng thái (state / 상태), optimizer continuity according to đặc tả hợp đồng (contract / 계약) and no silent data-sampler duplication/skip beyond expected ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Trong **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **26. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** tiếp nhận điểm tựa từ **25. thất bại (failure / 실패) testing must include partial thất bại (failure / 실패) and slow thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?

If GPU idle, gốc (root / 루트) may be collective/đầu vào (input / 입력) not compute kernel. If scaling plateaus, inspect compute-to-communication ratio and topology. If OOM after parallelism thay đổi (change / 변경), count optimizer/activation/communication workspace. If job hangs, inspect rank-level collective/membership trạng thái (state / 상태). If restart diverges, checkpoint/sampler/random trạng thái (state / 상태) may be incomplete.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **27. Mô hình tư duy** gom các mảnh từ **26. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Mô hình tư duy

> phân tán (distributed / 분산) huấn luyện (training / 학습) partitions **compute, bộ nhớ (memory / 메모리) and quyền sở hữu trạng thái (state ownership / 상태 소유권)**, then pays communication/synchronization to make those partitions act like one huấn luyện (training / 학습) thuật toán (algorithm / 알고리즘). dữ liệu (data / 데이터) parallelism reconciles gradients; tensor/chuỗi xử lý (pipeline / 파이프라인) parallelism moves activations/parameters across devices; sharding trades bộ nhớ (memory / 메모리) for collectives; checkpointing creates durable huấn luyện (training / 학습) trạng thái (state / 상태). **hiệu năng (performance / 성능) is limited by the slowest synchronized đường dẫn (path / 경로); tính đúng đắn (correctness / 정확성) depends on step/phiên bản (version / 버전)/trạng thái (state / 상태) invariants surviving communication and thất bại (failure / 실패).**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống**, **Kết nối** gom các mảnh từ **27. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Ôn [AI foundations](../../basic/10_ai_foundations/03_neural_networks_and_representation_learning.md), đọc [training/inference lifecycle](./00_training_inference_systems_and_model_lifecycle.md), [transformer/KV serving](./01_transformer_attention_kv_cache_and_inference_cost.md), [GPU execution](../../02_computer_architecture/advanced/06_simd_vector_isa_and_gpu_execution_model.md), [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md), [distributed failure/consensus](../../06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md) và specialized AI thư viện (library / 라이브러리) tại [`../../02_artificial_intelligence/`](../../02_artificial_intelligence/README.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
