# Parallel Computing trong AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Parallel computing trong AI**. Route đi từ instruction/data/model parallelism → partition strategy → synchronization/communication → scaling efficiency → failure and reproducibility, để song song hóa nối với giới hạn hệ thống.

Deep học tập (learning / 학습) có thể quy mô (scale / 규모) lớn vì phần lớn tensor thao tác (operation / 연산) có thể chạy song song. Nhưng **xử lý song song (parallelism / 병렬 처리)** không phải một kỹ thuật duy nhất. Ta có thể song song theo dữ liệu (data / 데이터), mô hình (model / 모델) dimension, chuỗi xử lý (pipeline / 파이프라인) stage hoặc yêu cầu (request / 요청). Mỗi cách tạo communication mẫu (pattern / 패턴), bộ nhớ (memory / 메모리) footprint và synchronization overhead khác nhau.

## Parallelism ở nhiều cấp

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

> **Chuyển mạch:** Trong **Parallel Computing trong AI**, **Parallelism ở nhiều cấp** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Parallelism** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Synchronous và Asynchronous** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Parallel Computing trong AI**, **Dữ liệu (data / 데이터) Parallelism** nêu điều cần giải thích; **Synchronous và Asynchronous** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tensor Parallelism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Synchronous và Asynchronous

Synchronous dữ liệu (data / 데이터) parallel chờ tất cả worker rồi mới aggregate. ngữ nghĩa (semantics / 의미론) ổn định nhưng một straggler chậm có thể làm cả group phải chờ.

Asynchronous cập nhật (update / 업데이트) giảm thời gian chờ nhưng tạo stale độ dốc (gradient / 기울기) và làm tối ưu hóa (optimization / 최적화) khó hơn.

Large-scale huấn luyện (training / 학습) hiện đại thường ưu tiên synchronous collective kết hợp interconnect tối ưu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Parallel Computing trong AI**, **Tensor Parallelism** tiếp nhận điểm tựa từ **Synchronous và Asynchronous** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi xử lý (pipeline / 파이프라인) Parallelism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tensor Parallelism

Chia một tensor hoặc ma trận (matrix / 행렬) thao tác (operation / 연산) qua nhiều thiết bị (device / 장치).

Ví dụ split weight ma trận (matrix / 행렬) theo column hoặc row. Mỗi tầng (layer / 계층) cần trao đổi partial kết quả (result / 결과).

Ưu điểm: tầng (layer / 계층) lớn hơn bộ nhớ (memory / 메모리) của một GPU vẫn có thể chạy.

Nhược điểm: communication diễn ra thường xuyên, nên cần interconnect bandwidth cao.

> **Chuyển mạch:** Trong **Parallel Computing trong AI**, **Tensor Parallelism** xác định đầu vào; **Chuỗi xử lý (pipeline / 파이프라인) Parallelism** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Chuỗi (sequence / 시퀀스) Parallelism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi xử lý (pipeline / 파이프라인) Parallelism

Chia các tầng (layer / 계층) thành nhiều stage:

```text
GPU group 1 → layers 1–N
GPU group 2 → layers N+1–M
...
```

Microbatch đi xuyên chuỗi xử lý (pipeline / 파이프라인).

Có **chuỗi xử lý (pipeline / 파이프라인) bubble** khi một stage idle ở đầu/cuối chuỗi xử lý (pipeline / 파이프라인) hoặc khi tải (load / 로드) không cân bằng.

> **Chuyển mạch:** Ở chặng này của **Parallel Computing trong AI**, **Chuỗi xử lý (pipeline / 파이프라인) Parallelism** xác định đầu vào; **Chuỗi (sequence / 시퀀스) Parallelism** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Expert Parallelism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (sequence / 시퀀스) Parallelism

Chia chuỗi (sequence / 시퀀스) dimension cho một số thao tác (operation / 연산), giúp giảm activation bộ nhớ (memory / 메모리) và bổ trợ tensor parallelism.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Parallel Computing trong AI**, **Chuỗi (sequence / 시퀀스) Parallelism** xác định đầu vào; **Expert Parallelism** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Hybrid Parallelism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Expert Parallelism

Mixture-of-Experts tuyến (route / 경로) đơn vị từ (token / 토큰) tới các expert group khác nhau.

Lợi ích: tăng total parameter nhưng active compute trên mỗi đơn vị từ (token / 토큰) thấp hơn dense mô hình (model / 모델) tương đương.

Đổi lại cần all-to-all communication và tải (load / 로드) balancing phức tạp.

> **Chuyển mạch:** Trong **Parallel Computing trong AI**, **Hybrid Parallelism** tiếp nhận điểm tựa từ **Expert Parallelism** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Collective Communication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hybrid Parallelism

Large huấn luyện (training / 학습) thường kết hợp:

```text
data parallel
× tensor parallel
× pipeline parallel
× expert / sequence parallel
```

Cách ánh xạ các chiều parallelism vào topology phần cứng là một bài toán hệ thống (system / 시스템) thiết kế (design / 설계).

> **Chuyển mạch:** Ở chặng này của **Parallel Computing trong AI**, **Collective Communication** tiếp nhận điểm tựa từ **Hybrid Parallelism** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chồng lấp Communication và Computation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Collective Communication

Các collective phổ biến:

- all-reduce;
- all-gather;
- reduce-scatter;
- broadcast;
- all-to-all.

All-reduce độ dốc (gradient / 기울기) là thao tác (operation / 연산) cốt lõi của dữ liệu (data / 데이터) parallel.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Parallel Computing trong AI**, **Chồng lấp Communication và Computation** tiếp nhận điểm tựa từ **Collective Communication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Straggler** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chồng lấp Communication và Computation

Thời gian chạy (runtime / 런타임) có thể truyền độ dốc (gradient / 기울기) của tầng (layer / 계층) trước trong khi backward pass vẫn đang tính tầng (layer / 계층) sau. Overlap này giúp giảm phần communication thời gian (time / 시간) lộ ra ngoài.

Nếu communication chỉ bắt đầu sau khi compute kết thúc, scaling thường kém hơn.

> **Chuyển mạch:** Trong **Parallel Computing trong AI**, **Straggler** tiếp nhận điểm tựa từ **Chồng lấp Communication và Computation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tải (load / 로드) Balancing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Straggler

Một GPU hoặc nút (node / 노드) chậm có thể làm synchronous group phải chờ. Nguyên nhân có thể là:

- hardware issue;
- mạng (network / 네트워크) congestion;
- tải công việc (workload / 워크로드) không đều;
- thermal throttling;
- dữ liệu (data / 데이터) loading chậm.

Phân tán (distributed / 분산) huấn luyện (training / 학습) nên monitor timing theo từng rank.

> **Chuyển mạch:** Ở chặng này của **Parallel Computing trong AI**, **Tải (load / 로드) Balancing** tiếp nhận điểm tựa từ **Straggler** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ dốc (gradient / 기울기) Accumulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tải (load / 로드) Balancing

Chuỗi xử lý (pipeline / 파이프라인) stage cần lượng compute gần cân bằng. MoE expert cần đơn vị từ (token / 토큰) tải (load / 로드) cân bằng. Serving nhiều yêu cầu (request / 요청) cần tuyến (route / 경로) tính đồng thời (concurrency / 동시성) theo available bộ nhớ (memory / 메모리) và sức chứa (capacity / 용량).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Parallel Computing trong AI**, **Độ dốc (gradient / 기울기) Accumulation** tiếp nhận điểm tựa từ **Tải (load / 로드) Balancing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parallel suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ dốc (gradient / 기울기) Accumulation

Nếu vật lý (physical / 물리적) batch trên mỗi GPU nhỏ, có thể accumulate nhiều microbatch trước optimizer step. Đây là kỹ thuật theo thời gian để đạt effective batch lớn hơn, không phải phân tán (distributed / 분산) parallelism theo nghĩa trực tiếp.

> **Chuyển mạch:** Trong **Parallel Computing trong AI**, **Parallel suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Độ dốc (gradient / 기울기) Accumulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prefill–Decode Disaggregation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parallel suy luận (inference / 추론)

Serving có hai dạng chính:

```text
model parallelism   → một request dùng nhiều device
request parallelism → nhiều replica xử lý các request khác nhau
```

Yêu cầu (request / 요청) parallelism quy mô (scale / 규모) thông lượng (throughput / 처리량) tốt khi mô hình (model / 모델) fit một thiết bị (device / 장치). mô hình (model / 모델) parallelism cần khi mô hình (model / 모델) quá lớn hoặc độ trễ (latency / 지연 시간) mục tiêu (target / 대상) yêu cầu nhiều thiết bị (device / 장치) cùng xử lý một yêu cầu (request / 요청).

> **Chuyển mạch:** Ở chặng này của **Parallel Computing trong AI**, **Prefill–Decode Disaggregation** tiếp nhận điểm tựa từ **Parallel suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Amdahl's Law** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prefill–Decode Disaggregation

LLM serving có thể tách tài nguyên (resource / 자원) pool cho prefill và decode vì hai phase có profile compute/bộ nhớ (memory / 메모리) khác nhau. Đây là một dạng specialized chuỗi xử lý (pipeline / 파이프라인) decomposition trong serving kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Parallel Computing trong AI**, **Amdahl's Law** tiếp nhận điểm tựa từ **Prefill–Decode Disaggregation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Strong Scaling và Weak Scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Amdahl's Law

Nếu tỷ lệ serial là `s`:

\[
Speedup(N)=\frac{1}{s+\frac{1-s}{N}}
\]

Khi `N` lớn, serial section và communication overhead chi phối. Scale-out không thể tăng vô hạn.

> **Chuyển mạch:** Trong **Parallel Computing trong AI**, **Strong Scaling và Weak Scaling** tiếp nhận điểm tựa từ **Amdahl's Law** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Strong Scaling và Weak Scaling

**Strong scaling**: bài toán (problem / 문제) kích thước (size / 크기) cố định, tăng thiết bị (device / 장치) để giảm thời gian chạy.

**Weak scaling**: bài toán (problem / 문제) kích thước (size / 크기) tăng cùng số thiết bị (device / 장치), giữ lượng công việc (work / 작업) trên mỗi thiết bị (device / 장치) gần ổn định.

Large AI thường weak-scale mô hình (model / 모델) hoặc dữ liệu (data / 데이터) kích thước (size / 크기) thay vì chỉ dùng nhiều thiết bị (device / 장치) để chạy cùng một job cũ nhanh hơn.

> **Chuyển mạch:** Ở chặng này của **Parallel Computing trong AI**, **Mô hình tư duy** gom các mảnh từ **Strong Scaling và Weak Scaling** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Parallelism đổi local work lấy coordination overhead.
```

Lợi ích chỉ xuất hiện khi lượng compute tiết kiệm được lớn hơn communication và synchronization overhead.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Parallel Computing trong AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “N GPU = nhanh N lần”

Không. Communication, synchronization và serial section làm efficiency giảm.

### “Tensor parallelism và dữ liệu (data / 데이터) parallelism giống nhau”

Không. Tensor parallelism chia mô hình (model / 모델) computation; dữ liệu (data / 데이터) parallelism replicate mô hình (model / 모델) và chia dữ liệu (data / 데이터).

### “phân tán (distributed / 분산) huấn luyện (training / 학습) chỉ cần thêm máy”

Không. Topology, collective, checkpointing và thất bại (failure / 실패) handling trở thành bài toán hạng nhất.

> **Chuyển mạch:** Trong **Parallel Computing trong AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Distributed Training](./05_distributed_training.md), [Distributed Inference](./06_distributed_inference.md), [Memory/Bandwidth](./03_memory_and_bandwidth.md), [Deep Learning Training](../05_neural_networks/09_deep_learning_training_dynamics.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
