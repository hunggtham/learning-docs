# Phân tán (distributed / 분산) huấn luyện (training / 학습)

> **Mạch đọc:** Đặt **phân tán (distributed / 분산) huấn luyện (training / 학습)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao cần phân tán (distributed / 분산) huấn luyện (training / 학습)?** sang **dữ liệu (data / 데이터) Parallel huấn luyện (training / 학습)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi mô hình (model / 모델), optimizer trạng thái (state / 상태) hoặc desired batch không fit trên một accelerator, huấn luyện (training / 학습) phải được phân tán qua nhiều thiết bị (device / 장치) hoặc nút (node / 노드). **Huấn luyện phân tán (distributed training / 분산 학습)** không chỉ là chạy cùng một đoạn mã (code / 코드) trên nhiều GPU; nó làm thay đổi bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃), communication mẫu (pattern / 패턴), fault mô hình (model / 모델) và khả năng tái lập.

## Vì sao cần phân tán (distributed / 분산) huấn luyện (training / 학습)?

Ba lý do chính:

```text
model quá lớn cho một device
training quá chậm trên một device
batch / data throughput quá lớn
```

Mỗi lý do dẫn tới chiến lược (strategy / 전략) parallelism khác nhau.

## Dữ liệu (data / 데이터) Parallel huấn luyện (training / 학습)

Mỗi worker giữ một mô hình (model / 모델) replica và xử lý batch riêng. Sau backward pass, độ dốc (gradient / 기울기) được aggregate.

Một synchronous step điển hình:

```text
forward
→ backward
→ all-reduce gradients
→ optimizer step
```

Toàn cục (global / 전역) batch:

\[
B_{toàn cục (global / 전역)}=B_{thiết bị (device / 장치)}\times N_{devices}\times accumulation\_steps
\]

Learning-rate schedule có thể cần điều chỉnh khi toàn cục (global / 전역) batch thay đổi.

## Phân tán (distributed / 분산) dữ liệu (data / 데이터) Parallel

Hiện thực (implementation / 구현) hiệu quả có thể overlap độ dốc (gradient / 기울기) all-reduce với backward pass. Tuy nhiên parameter vẫn được replicate nên bộ nhớ (memory / 메모리) trên mỗi thiết bị (device / 장치) còn cao.

Đây thường là lựa chọn đầu tiên khi mô hình (model / 모델) vẫn fit trên một thiết bị (device / 장치).

## Sharded dữ liệu (data / 데이터) Parallelism

Parameter, độ dốc (gradient / 기울기) và optimizer trạng thái (state / 상태) có thể được shard giữa các worker.

Về mặt khái niệm:

```text
Stage 1: shard optimizer states
Stage 2: + gradients
Stage 3: + parameters
```

Cách này giảm bộ nhớ (memory / 메모리) duplication nhưng tăng communication độ phức tạp (complexity / 복잡도).

## Tensor Parallelism

Large tầng (layer / 계층) được chia qua nhiều GPU. Partial kết quả (result / 결과) của phép nhân ma trận (matrix multiplication / 행렬 곱셈) cần collective communication để ghép lại.

Phù hợp nhất khi có high-speed interconnect, thường trong cùng nút (node / 노드).

## Chuỗi xử lý (pipeline / 파이프라인) Parallelism

Các tầng (layer / 계층) được chia thành nhiều stage. Microbatch chạy xuyên chuỗi xử lý (pipeline / 파이프라인).

Cần schedule để giảm chuỗi xử lý (pipeline / 파이프라인) bubble và cân bằng compute/bộ nhớ (memory / 메모리) giữa các stage.

## 3D Parallelism

Very large mô hình (model / 모델) thường kết hợp dữ liệu (data / 데이터), tensor và chuỗi xử lý (pipeline / 파이프라인) parallelism. Một số hệ thống còn thêm chuỗi (sequence / 시퀀스) hoặc expert parallelism.

Parallel topology phải khớp vật lý (physical / 물리적) mạng (network / 네트워크) topology.

## Communication thành phần nguyên thủy (primitive / 기본 요소)

### All-Reduce

Sau phép all-reduce, mỗi worker nhận tensor đã được reduce, thường dùng để đồng bộ độ dốc (gradient / 기울기).

### Reduce-Scatter + All-Gather

Có thể phân rã all-reduce thành hai thao tác (operation / 연산) này; chúng đặc biệt hữu ích cho sharded trạng thái (state / 상태).

### All-to-All

Quan trọng trong MoE đơn vị từ (token / 토큰) routing.

## Interconnect

GPU link trong cùng nút (node / 노드) thường nhanh hơn mạng (network / 네트워크) giữa nút (node / 노드). Tensor parallel communication diễn ra thường xuyên nên ưu tiên fast cục bộ (local / 로컬) link; dữ liệu (data / 데이터) parallel thường quy mô (scale / 규모) qua nút (node / 노드) hiệu quả hơn.

## Độ dốc (gradient / 기울기) Synchronization

Tần suất synchronization ảnh hưởng ngữ nghĩa (semantics / 의미론) của tối ưu hóa (optimization / 최적화). cục bộ (local / 로컬) SGD hoặc delayed sync giúp giảm communication nhưng cũng thay đổi học tập (learning / 학습) dynamics.

## Communication Compression

Quantize hoặc sparsify độ dốc (gradient / 기울기) có thể giảm mạng (network / 네트워크) traffic nhưng thêm approximation và overhead. Lợi ích phụ thuộc tải công việc (workload / 워크로드).

## Checkpointing

Large phân tán (distributed / 분산) checkpoint có thể đạt quy mô TB. Cần:

- shard-aware format;
- parallel ghi (write / 쓰기);
- atomic hoặc consistent checkpoint siêu dữ liệu (metadata / 메타데이터);
- khả năng resume;
- retention chính sách (policy / 정책).

Chỉ lưu weights thường không đủ để resume huấn luyện (training / 학습) nếu thiếu optimizer, scheduler hoặc RNG trạng thái (state / 상태).

## Xử lý thất bại (failure / 실패)

Huấn luyện (training / 학습) job dài có xác suất gặp hardware hoặc nút (node / 노드) thất bại (failure / 실패) cao.

Hệ thống cần:

```text
health checks
checkpoint / restart
elastic membership nếu hỗ trợ
bad-node quarantine
retry policy
```

Khi số nút (node / 노드) tăng, xác suất một thành phần nào đó hỏng trong suốt job cũng tăng.

## Determinism

Thứ tự phân tán (distributed / 분산) reduction có thể thay đổi kết quả floating-point nhỏ. Cùng seed không bảo đảm run giống hệt.

Reproducibility nên ghi lại topology, world kích thước (size / 크기) và thời gian chạy (runtime / 런타임) phiên bản (version / 버전).

## Dữ liệu (data / 데이터) Loading

Nếu lưu trữ (storage / 저장소) không cấp dữ liệu đủ nhanh, accelerator sẽ idle. phân tán (distributed / 분산) dữ liệu (data / 데이터) loader cần:

- chia shard mẫu (sample / 표본) đúng;
- prefetch;
- bộ nhớ đệm (cache / 캐시);
- tránh duplicate sampling;
- deterministic epoch ngữ nghĩa (semantics / 의미론) khi cần.

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

BF16, FP16 hoặc FP8 giúp giảm communication và bộ nhớ (memory / 메모리) bên cạnh compute chi phí (cost / 비용). Tuy nhiên optimizer trạng thái (state / 상태) hoặc numerical-sensitive thao tác (operation / 연산) có thể vẫn cần precision cao hơn.

## Scaling Law và Scaling Efficiency

Ngay cả khi thêm compute cải thiện mô hình (model / 모델) chất lượng (quality / 품질) theo statistical scaling law, hệ thống phân tán (distributed system / 분산 시스템) kém hiệu quả vẫn làm lãng phí ngân sách (budget / 예산). Algorithmic scaling và các hệ thống (systems / 시스템들) scaling là hai câu hỏi khác nhau.

## Huấn luyện (training / 학습) thông lượng (throughput / 처리량)

Có thể đo samples/s hoặc tokens/s. Khi cần, có thể dùng chỉ số (metric / 지표) kiểu **mô hình (model / 모델) FLOPs Utilization (MFU)** để ước lượng tỷ lệ theoretical compute thực sự phục vụ mô hình (model / 모델) công việc (work / 작업).

Peak utilization cao chưa chắc tốt nếu phần lớn compute đến từ recomputation hoặc padding không hiệu quả.

## Chi phí của Large Batch

Toàn cục (global / 전역) batch lớn giúp hardware utilization tốt hơn nhưng có thể thay đổi tối ưu hóa (optimization / 최적화) và generalization. Hardware efficiency và statistical efficiency phải được tối ưu cùng nhau.

## Mô hình tư duy

```text
Distributed training = chia compute và state trong khi trả giá bằng communication, synchronization và failure complexity.
```

## Những nhầm lẫn thường gặp

### “mô hình (model / 모델) không fit thì chỉ cần dữ liệu (data / 데이터) parallelism”

Không. dữ liệu (data / 데이터) parallel replicate mô hình (model / 모델); muốn giảm mô hình (model / 모델) trạng thái (state / 상태) trên mỗi thiết bị (device / 장치) cần sharding hoặc mô hình (model / 모델) parallelism.

### “Checkpoint weights là đủ để resume”

Không. Optimizer, scheduler, RNG và dữ liệu (data / 데이터) position có thể cần thiết.

### “Thêm GPU luôn làm huấn luyện (training / 학습) rẻ hơn”

Không. Thời gian có thể giảm nhưng scaling kém có thể làm tổng accelerator-hour tăng.

## Liên kết kiến thức

Xem [Parallel Computing](./04_parallel_computing.md), [Memory/Bandwidth](./03_memory_and_bandwidth.md), [Cluster & Interconnect](./07_cluster_scheduling_and_interconnect.md), [Training Pipeline](../15_ai_engineering/01_training_pipeline.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 compute foundations](./00_compute_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
