# Parallel Computing trong AI

> **Mạch đọc:** Đặt **Parallel Computing trong AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Parallelism ở nhiều cấp** sang **dữ liệu (data / 데이터) Parallelism**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Deep học tập (learning / 학습) có thể quy mô (scale / 규모) lớn vì phần lớn tensor thao tác (operation / 연산) có thể chạy song song. Nhưng **xử lý song song (parallelism / 병렬 처리)** không phải một kỹ thuật duy nhất. Ta có thể song song theo dữ liệu (data / 데이터), mô hình (model / 모델) dimension, chuỗi xử lý (pipeline / 파이프라인) stage hoặc yêu cầu (request / 요청). Mỗi cách tạo communication mẫu (pattern / 패턴), bộ nhớ (memory / 메모리) footprint và synchronization overhead khác nhau.

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

AI engineer thường quan tâm từ tensor thao tác (operation / 연산) lên cluster và yêu cầu (request / 요청).

## Dữ liệu (data / 데이터) Parallelism

Mỗi thiết bị (device / 장치) giữ một bản đầy đủ của mô hình (model / 모델) và xử lý mini-batch khác nhau.

```text
GPU0: batch A → gradients
GPU1: batch B → gradients
...
all-reduce gradients
optimizer step
```

Ưu điểm: đơn giản và hiệu quả khi mô hình (model / 모델) fit trên mỗi GPU.

Nhược điểm: mỗi thiết bị (device / 장치) vẫn phải chứa full mô hình (model / 모델) và optimizer trạng thái (state / 상태).

## Synchronous và Asynchronous

Synchronous dữ liệu (data / 데이터) parallel chờ tất cả worker rồi mới aggregate. ngữ nghĩa (semantics / 의미론) ổn định nhưng một straggler chậm có thể làm cả group phải chờ.

Asynchronous cập nhật (update / 업데이트) giảm thời gian chờ nhưng tạo stale độ dốc (gradient / 기울기) và làm tối ưu hóa (optimization / 최적화) khó hơn.

Large-scale huấn luyện (training / 학습) hiện đại thường ưu tiên synchronous collective kết hợp interconnect tối ưu.

## Tensor Parallelism

Chia một tensor hoặc ma trận (matrix / 행렬) thao tác (operation / 연산) qua nhiều thiết bị (device / 장치).

Ví dụ split weight ma trận (matrix / 행렬) theo column hoặc row. Mỗi tầng (layer / 계층) cần trao đổi partial kết quả (result / 결과).

Ưu điểm: tầng (layer / 계층) lớn hơn bộ nhớ (memory / 메모리) của một GPU vẫn có thể chạy.

Nhược điểm: communication diễn ra thường xuyên, nên cần interconnect bandwidth cao.

## Chuỗi xử lý (pipeline / 파이프라인) Parallelism

Chia các tầng (layer / 계층) thành nhiều stage:

```text
GPU group 1 → layers 1–N
GPU group 2 → layers N+1–M
...
```

Microbatch đi xuyên chuỗi xử lý (pipeline / 파이프라인).

Có **chuỗi xử lý (pipeline / 파이프라인) bubble** khi một stage idle ở đầu/cuối chuỗi xử lý (pipeline / 파이프라인) hoặc khi tải (load / 로드) không cân bằng.

## Chuỗi (sequence / 시퀀스) Parallelism

Chia chuỗi (sequence / 시퀀스) dimension cho một số thao tác (operation / 연산), giúp giảm activation bộ nhớ (memory / 메모리) và bổ trợ tensor parallelism.

## Expert Parallelism

Mixture-of-Experts tuyến (route / 경로) đơn vị từ (token / 토큰) tới các expert group khác nhau.

Lợi ích: tăng total parameter nhưng active compute trên mỗi đơn vị từ (token / 토큰) thấp hơn dense mô hình (model / 모델) tương đương.

Đổi lại cần all-to-all communication và tải (load / 로드) balancing phức tạp.

## Hybrid Parallelism

Large huấn luyện (training / 학습) thường kết hợp:

```text
data parallel
× tensor parallel
× pipeline parallel
× expert / sequence parallel
```

Cách ánh xạ các chiều parallelism vào topology phần cứng là một bài toán hệ thống (system / 시스템) thiết kế (design / 설계).

## Collective Communication

Các collective phổ biến:

- all-reduce;
- all-gather;
- reduce-scatter;
- broadcast;
- all-to-all.

All-reduce độ dốc (gradient / 기울기) là thao tác (operation / 연산) cốt lõi của dữ liệu (data / 데이터) parallel.

## Chồng lấp Communication và Computation

Thời gian chạy (runtime / 런타임) có thể truyền độ dốc (gradient / 기울기) của tầng (layer / 계층) trước trong khi backward pass vẫn đang tính tầng (layer / 계층) sau. Overlap này giúp giảm phần communication thời gian (time / 시간) lộ ra ngoài.

Nếu communication chỉ bắt đầu sau khi compute kết thúc, scaling thường kém hơn.

## Straggler

Một GPU hoặc nút (node / 노드) chậm có thể làm synchronous group phải chờ. Nguyên nhân có thể là:

- hardware issue;
- mạng (network / 네트워크) congestion;
- tải công việc (workload / 워크로드) không đều;
- thermal throttling;
- dữ liệu (data / 데이터) loading chậm.

Phân tán (distributed / 분산) huấn luyện (training / 학습) nên monitor timing theo từng rank.

## Tải (load / 로드) Balancing

Chuỗi xử lý (pipeline / 파이프라인) stage cần lượng compute gần cân bằng. MoE expert cần đơn vị từ (token / 토큰) tải (load / 로드) cân bằng. Serving nhiều yêu cầu (request / 요청) cần tuyến (route / 경로) tính đồng thời (concurrency / 동시성) theo available bộ nhớ (memory / 메모리) và sức chứa (capacity / 용량).

## Độ dốc (gradient / 기울기) Accumulation

Nếu vật lý (physical / 물리적) batch trên mỗi GPU nhỏ, có thể accumulate nhiều microbatch trước optimizer step. Đây là kỹ thuật theo thời gian để đạt effective batch lớn hơn, không phải phân tán (distributed / 분산) parallelism theo nghĩa trực tiếp.

## Parallel suy luận (inference / 추론)

Serving có hai dạng chính:

```text
model parallelism   → một request dùng nhiều device
request parallelism → nhiều replica xử lý các request khác nhau
```

Yêu cầu (request / 요청) parallelism quy mô (scale / 규모) thông lượng (throughput / 처리량) tốt khi mô hình (model / 모델) fit một thiết bị (device / 장치). mô hình (model / 모델) parallelism cần khi mô hình (model / 모델) quá lớn hoặc độ trễ (latency / 지연 시간) mục tiêu (target / 대상) yêu cầu nhiều thiết bị (device / 장치) cùng xử lý một yêu cầu (request / 요청).

## Prefill–Decode Disaggregation

LLM serving có thể tách tài nguyên (resource / 자원) pool cho prefill và decode vì hai phase có profile compute/bộ nhớ (memory / 메모리) khác nhau. Đây là một dạng specialized chuỗi xử lý (pipeline / 파이프라인) decomposition trong serving kiến trúc (architecture / 아키텍처).

## Amdahl's Law

Nếu tỷ lệ serial là `s`:

\[
Speedup(N)=\frac{1}{s+\frac{1-s}{N}}
\]

Khi `N` lớn, serial section và communication overhead chi phối. Scale-out không thể tăng vô hạn.

## Strong Scaling và Weak Scaling

**Strong scaling**: bài toán (problem / 문제) kích thước (size / 크기) cố định, tăng thiết bị (device / 장치) để giảm thời gian chạy.

**Weak scaling**: bài toán (problem / 문제) kích thước (size / 크기) tăng cùng số thiết bị (device / 장치), giữ lượng công việc (work / 작업) trên mỗi thiết bị (device / 장치) gần ổn định.

Large AI thường weak-scale mô hình (model / 모델) hoặc dữ liệu (data / 데이터) kích thước (size / 크기) thay vì chỉ dùng nhiều thiết bị (device / 장치) để chạy cùng một job cũ nhanh hơn.

## Mô hình tư duy

```text
Parallelism đổi local work lấy coordination overhead.
```

Lợi ích chỉ xuất hiện khi lượng compute tiết kiệm được lớn hơn communication và synchronization overhead.

## Những nhầm lẫn thường gặp

### “N GPU = nhanh N lần”

Không. Communication, synchronization và serial section làm efficiency giảm.

### “Tensor parallelism và dữ liệu (data / 데이터) parallelism giống nhau”

Không. Tensor parallelism chia mô hình (model / 모델) computation; dữ liệu (data / 데이터) parallelism replicate mô hình (model / 모델) và chia dữ liệu (data / 데이터).

### “phân tán (distributed / 분산) huấn luyện (training / 학습) chỉ cần thêm máy”

Không. Topology, collective, checkpointing và thất bại (failure / 실패) handling trở thành bài toán hạng nhất.

## Liên kết kiến thức

Xem [Distributed Training](./05_distributed_training.md), [Distributed Inference](./06_distributed_inference.md), [Memory/Bandwidth](./03_memory_and_bandwidth.md), [Deep Learning Training](../05_neural_networks/09_deep_learning_training_dynamics.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 compute foundations](./00_compute_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
