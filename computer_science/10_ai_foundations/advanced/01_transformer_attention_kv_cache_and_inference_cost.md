# Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bài toán ban đầu: mô hình (model / 모델) math không tự nói serving hành vi (behavior / 동작)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Transformer khối (block / 블록) và trạng thái (state / 상태) luồng (flow / 흐름)** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Transformer quan trọng không chỉ vì mô hình (model / 모델) chất lượng (quality / 품질) mà vì computation đồ thị (graph / 그래프) ánh xạ tốt lên parallel hardware trong huấn luyện (training / 학습). Autoregressive suy luận (inference / 추론) lại có chi phí (cost / 비용) profile rất khác: prompt được xử lý theo batch lớn hơn, còn decode phải sinh đơn vị từ (token / 토큰) nối tiếp và liên tục đọc mô hình (model / 모델) trạng thái (state / 상태)/KV trạng thái (state / 상태).

Mô hình tư duy (mental model / 사고 모델) của chương này là: **AI suy luận (inference / 추론) serving là một memory-and-scheduling hệ thống (system / 시스템) có mô hình (model / 모델) ngữ nghĩa (semantics / 의미론) ở trên**. tính đúng đắn (correctness / 정확성) cần yêu cầu (request / 요청) nào dùng đúng mô hình (model / 모델)/KV trạng thái (state / 상태); hiệu năng (performance / 성능) phụ thuộc arithmetic intensity, bộ nhớ (memory / 메모리) bandwidth, batching, queueing, fragmentation và scheduler chính sách (policy / 정책).

## 1. Bài toán ban đầu: mô hình (model / 모델) math không tự nói serving hành vi (behavior / 동작)

Cùng mô hình (model / 모델) weights có thể cho thông lượng (throughput / 처리량)/độ trễ (latency / 지연 시간) rất khác tùy:

```text
prompt/context length
output length
concurrent sequences
batching policy
precision/quantization
KV-cache layout
accelerator memory capacity/bandwidth
interconnect
tensor/model parallelism
```

Vì vậy “mô hình (model / 모델) có N parameters” không đủ để sức chứa (capacity / 용량) plan. Cần map tải công việc (workload / 워크로드) phân phối (distribution / 분포) vào tài nguyên (resource / 자원) consumption theo serving phase.

> **Chuyển mạch:** Model math chưa nói rõ serving behavior; transformer block biến token stream thành state, rồi query/key/value attention xác định thông tin nào được trộn ở mỗi bước.

## 2. Transformer khối (block / 블록) và trạng thái (state / 상태) luồng (flow / 흐름)

Đầu vào (input / 입력) tokens được ánh xạ thành vectors. Một transformer khối (block / 블록) điển hình có attention, feed-forward mạng (network / 네트워크), residual paths và normalization.

Attention cho mỗi position tổng hợp thông tin (information / 정보) từ positions khác. Nhưng serving hệ thống (system / 시스템) quan tâm thêm:

```text
weights: mostly read-only model state
activations: temporary computation state
KV cache: per-sequence persistent decode state
scheduler metadata: ownership/lifetime of each sequence
```

Tách các trạng thái (state / 상태) classes này giúp hiểu bộ nhớ (memory / 메모리) pressure.

> **Chuyển mạch:** Ở chặng này của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **2. Transformer khối (block / 블록) và trạng thái (state / 상태) luồng (flow / 흐름)** xác định đầu vào; **3. truy vấn (query / 쿼리), Key, giá trị (value / 값) và attention bất biến (invariant / 불변식)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. Full self-attention có quadratic tương tác (interaction / 상호작용) theo chuỗi (sequence / 시퀀스) length** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. truy vấn (query / 쿼리), Key, giá trị (value / 값) và attention bất biến (invariant / 불변식)

Mỗi đơn vị từ (token / 토큰) biểu diễn (representation / 표현) được dự án (project / 프로젝트) thành Q, K, V. truy vấn (query / 쿼리) của position hiện tại so với keys tạo scores/weights; weighted values tạo attention đầu ra (output / 출력).

Multi-head attention dùng nhiều projections/subspaces. Kiến trúc không hứa một head luôn map tới một human-interpretable concept cụ thể.

Tính đúng đắn (correctness / 정확성) ở serving tầng (layer / 계층) cần giữ **chuỗi (sequence / 시퀀스) association**: K/V của yêu cầu (request / 요청) A không được nhầm với yêu cầu (request / 요청) B, và positions/thứ tự (order / 순서) phải map đúng logical prefix của chuỗi (sequence / 시퀀스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **3. truy vấn (query / 쿼리), Key, giá trị (value / 값) và attention bất biến (invariant / 불변식)** xác định đầu vào; **4. Full self-attention có quadratic tương tác (interaction / 상호작용) theo chuỗi (sequence / 시퀀스) length** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. Prefill và decode là hai thực thi (execution / 실행) phases khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Full self-attention có quadratic tương tác (interaction / 상호작용) theo chuỗi (sequence / 시퀀스) length

Với chuỗi (sequence / 시퀀스) length `n`, full attention biểu diễn interactions giữa nhiều pairs positions, tạo thành phần (component / 컴포넌트) `n × n` trong naïve formulation.

Optimized kernels như tiled/flash-style attention có thể tránh materialize toàn ma trận (matrix / 행렬) và giảm HBM traffic nhờ tiling/fusion, nhưng không thay mathematical phụ thuộc (dependency / 의존성) của chính xác (exact / 정확한) full attention.

Đây là mẫu (pattern / 패턴) hiệu năng (performance / 성능) quan trọng:

> Cùng algorithmic ngữ nghĩa (semantics / 의미론), dữ liệu (data / 데이터) movement chiến lược (strategy / 전략) có thể thay dominant bottleneck.

> **Chuyển mạch:** Trong **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **4. Full self-attention có quadratic tương tác (interaction / 상호작용) theo chuỗi (sequence / 시퀀스) length** xác định đầu vào; **5. Prefill và decode là hai thực thi (execution / 실행) phases khác nhau** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. KV bộ nhớ đệm (cache / 캐시) đổi recomputation lấy bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Prefill và decode là hai thực thi (execution / 실행) phases khác nhau

**Prefill** xử lý toàn prompt/ngữ cảnh (context / 맥락) mới. Nhiều tokens có thể được tính song song nên accelerator có cơ hội đạt high compute utilization.

**Decode** sinh đơn vị từ (token / 토큰) từng bước. đơn vị từ (token / 토큰) `t+1` phụ thuộc trạng thái (state / 상태)/kết quả (result / 결과) trước, nên một chuỗi (sequence / 시퀀스) có ít parallelism theo thời gian (time / 시간) dimension.

Metrics cần tách:

```text
TTFT — time to first token
prefill throughput
inter-token latency / time per output token
decode throughput
end-to-end request latency
```

Average tokens/s có thể che UX xấu nếu hàng đợi (queue / 큐)/TTFT cao.

> **Chuyển mạch:** Ở chặng này của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **6. KV bộ nhớ đệm (cache / 캐시) đổi recomputation lấy bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **5. Prefill và decode là hai thực thi (execution / 실행) phases khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. KV bộ nhớ đệm (cache / 캐시) có quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명) bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. KV bộ nhớ đệm (cache / 캐시) đổi recomputation lấy bộ nhớ (memory / 메모리)

Nếu decode mỗi bước tính lại K/V cho toàn prefix, công việc (work / 작업) lặp rất lớn. **KV bộ nhớ đệm (cache / 캐시)** giữ K/V của prior tokens cho mỗi tầng (layer / 계층) để đơn vị từ (token / 토큰) mới reuse.

Sự đánh đổi (trade-off / 트레이드오프):

```text
recompute ↓
↔
per-sequence persistent memory ↑
```

KV bộ nhớ (memory / 메모리) tăng với ngữ cảnh (context / 맥락) length, active sequences, layers và KV dimensions/precision. ngữ cảnh (context / 맥락) “được hỗ trợ” không đồng nghĩa có thể phục vụ nhiều long-context requests đồng thời.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **7. KV bộ nhớ đệm (cache / 캐시) có quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명) bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **6. KV bộ nhớ đệm (cache / 캐시) đổi recomputation lấy bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Paged KV bộ nhớ đệm (cache / 캐시) giảm fragmentation bằng indirection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. KV bộ nhớ đệm (cache / 캐시) có quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명) bất biến (invariant / 불변식)

Serving scheduler có thể batch, preempt, swap hoặc free chuỗi (sequence / 시퀀스) trạng thái (state / 상태). bất biến (invariant / 불변식) là:

> KV blocks chỉ được reuse sau khi chuỗi (sequence / 시퀀스) sở hữu chúng thật sự kết thúc/evict theo giao thức (protocol / 프로토콜); bảng trang (page table / 페이지 테이블)/khối (block / 블록) ánh xạ (mapping / 매핑) của chuỗi (sequence / 시퀀스) phải trỏ đúng logical đơn vị từ (token / 토큰) positions.

Một bug allocator/scheduler có thể tạo corruption cross-request dù mô hình (model / 모델) math hoàn hảo. Đây là liên kết (connection / 연결) trực tiếp giữa AI serving và OS-style bộ nhớ (memory / 메모리) management.

> **Chuyển mạch:** Trong **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **8. Paged KV bộ nhớ đệm (cache / 캐시) giảm fragmentation bằng indirection** tiếp nhận điểm tựa từ **7. KV bộ nhớ đệm (cache / 캐시) có quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명) bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Decode thường memory-bandwidth-bound** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Paged KV bộ nhớ đệm (cache / 캐시) giảm fragmentation bằng indirection

Nếu mỗi chuỗi (sequence / 시퀀스) cần một contiguous buffer theo maximum ngữ cảnh (context / 맥락), bộ nhớ (memory / 메모리) waste lớn và resizing khó. Paged/block-based KV quản bộ nhớ đệm (cache / 캐시) theo chunks và dùng ánh xạ (mapping / 매핑) logical đơn vị từ (token / 토큰) phạm vi (range / 범위) → vật lý (physical / 물리적) khối (block / 블록).

Lợi ích:

```text
less external fragmentation
share/reuse blocks easier when semantics allow
allocate incrementally with sequence growth
```

Đổi lại có siêu dữ liệu (metadata / 메타데이터)/indirection chi phí (cost / 비용) và allocator pressure. “Paged” không miễn phí; nó chuyển memory-contiguity bài toán (problem / 문제) thành ánh xạ (mapping / 매핑)/thời gian tồn tại (lifetime / 수명) bài toán (problem / 문제).

> **Chuyển mạch:** Ở chặng này của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **9. Decode thường memory-bandwidth-bound** tiếp nhận điểm tựa từ **8. Paged KV bộ nhớ đệm (cache / 캐시) giảm fragmentation bằng indirection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Batching đổi độ trễ (latency / 지연 시간) lấy thông lượng (throughput / 처리량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Decode thường memory-bandwidth-bound

Mỗi decode step của một chuỗi (sequence / 시퀀스) cần đọc lượng lớn weights và KV trạng thái (state / 상태) để tạo tương đối ít new đầu ra (output / 출력). Arithmetic intensity có thể thấp hơn prefill, làm HBM/bộ nhớ (memory / 메모리) bandwidth dominate.

Roofline-style lập luận (reasoning / 추론) hữu ích:

```text
compute demand / bytes moved thấp
→ bandwidth-bound

batching increases reuse/amortization
→ arithmetic intensity/utilization improve
```

Đây là lý do theoretical FLOPS cao không tự bảo đảm low đơn vị từ (token / 토큰) độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **10. Batching đổi độ trễ (latency / 지연 시간) lấy thông lượng (throughput / 처리량)** tiếp nhận điểm tựa từ **9. Decode thường memory-bandwidth-bound** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Scheduler là admission controller cho GPU bộ nhớ (memory / 메모리) + compute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Batching đổi độ trễ (latency / 지연 시간) lấy thông lượng (throughput / 처리량)

Batch nhiều sequences giúp amortize weight reads và tăng accelerator utilization. Nhưng scheduler có thể giữ yêu cầu (request / 요청) chờ để tạo batch lớn hơn.

Sự đánh đổi (trade-off / 트레이드오프):

```text
larger batch
→ throughput ↑ đến một mức
→ queue + per-step latency/memory ↑
```

Continuous batching chèn/rút sequences động để tận dụng slots tốt hơn fixed batch, nhưng tạo scheduling độ phức tạp (complexity / 복잡도): sequences có lengths khác nhau, finish khác nhau và bộ nhớ (memory / 메모리) footprint thay đổi mỗi decode step.

> **Chuyển mạch:** Trong **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **11. Scheduler là admission controller cho GPU bộ nhớ (memory / 메모리) + compute** tiếp nhận điểm tựa từ **10. Batching đổi độ trễ (latency / 지연 시간) lấy thông lượng (throughput / 처리량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Head-of-line blocking có thể xuất hiện trong batch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Scheduler là admission controller cho GPU bộ nhớ (memory / 메모리) + compute

Một yêu cầu (request / 요청) long-context có thể tiêu KV bộ nhớ (memory / 메모리) gấp nhiều lần yêu cầu (request / 요청) ngắn. Nếu scheduler admit chỉ theo yêu cầu (request / 요청) count, một vài long requests có thể OOM hoặc làm tính đồng thời (concurrency / 동시성) collapse.

Useful admission chi phí (cost / 비용) mô hình (model / 모델) cần consider:

```text
prompt tokens
max/expected output tokens
KV bytes per token
batch/parallelism mode
current free blocks
latency class / priority / tenant quota
```

Đây là weighted admission, giống general software các hệ thống (systems / 시스템들) nhưng tài nguyên (resource / 자원) đơn vị (unit / 단위) là tokens/KV/GPU sức chứa (capacity / 용량).

> **Chuyển mạch:** Ở chặng này của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **12. Head-of-line blocking có thể xuất hiện trong batch** tiếp nhận điểm tựa từ **11. Scheduler là admission controller cho GPU bộ nhớ (memory / 메모리) + compute** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. ngữ cảnh (context / 맥락) length làm giảm effective sức chứa (capacity / 용량) theo nhiều chiều** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Head-of-line blocking có thể xuất hiện trong batch

Nếu batch chính sách (policy / 정책) ép requests cùng bước theo slowest/longest member, một long chuỗi (sequence / 시퀀스) có thể làm short requests chờ. Continuous scheduling giảm một số form nhưng không xóa all interference.

Multi-tenant serving cần fairness: thông lượng (throughput / 처리량) tối đa toàn GPU có thể xung đột (conflict / 충돌) với p99 SLO của interactive requests.

Separate pools/classes hoặc weighted scheduling có thể cần khi workloads khác mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **13. ngữ cảnh (context / 맥락) length làm giảm effective sức chứa (capacity / 용량) theo nhiều chiều** tiếp nhận điểm tựa từ **12. Head-of-line blocking có thể xuất hiện trong batch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Quantization giảm bytes nhưng tạo accuracy/kernel sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. ngữ cảnh (context / 맥락) length làm giảm effective sức chứa (capacity / 용량) theo nhiều chiều

Ngữ cảnh (context / 맥락) dài:

```text
KV memory ↑
attention work ↑
prefill compute ↑
possible batch size ↓
number of concurrent sequences fit in memory ↓
```

Sức chứa (capacity / 용량) planning phải dùng **phân phối (distribution / 분포)** ngữ cảnh (context / 맥락)/đầu ra (output / 출력) length, không chỉ maximum ngữ cảnh (context / 맥락) advertised.

Một p99 100k-token tải công việc (workload / 워크로드) khác hoàn toàn tải công việc (workload / 워크로드) median 1k dù cùng mô hình (model / 모델)/ngữ cảnh (context / 맥락) limit.

> **Chuyển mạch:** Trong **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **14. Quantization giảm bytes nhưng tạo accuracy/kernel sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **13. ngữ cảnh (context / 맥락) length làm giảm effective sức chứa (capacity / 용량) theo nhiều chiều** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Tensor/mô hình (model / 모델) parallelism đổi cục bộ (local / 로컬) bộ nhớ (memory / 메모리) bài toán (problem / 문제) thành communication bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Quantization giảm bytes nhưng tạo accuracy/kernel sự đánh đổi (trade-off / 트레이드오프)

Giảm precision weights/activations/KV có thể giảm footprint/bandwidth và tăng thông lượng (throughput / 처리량) nếu hardware/kernel đường dẫn (path / 경로) hỗ trợ tốt.

Nhưng:

```text
quality/calibration can change
conversion/dequant cost exists
unsupported kernel may be slower
some tensors are more sensitive than others
```

“4-bit” không tự động nhanh hoặc đủ chất lượng (quality / 품질). Phải benchmark end-to-end tải công việc (workload / 워크로드) + chất lượng (quality / 품질) metrics.

> **Chuyển mạch:** Ở chặng này của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **15. Tensor/mô hình (model / 모델) parallelism đổi cục bộ (local / 로컬) bộ nhớ (memory / 메모리) bài toán (problem / 문제) thành communication bài toán (problem / 문제)** tiếp nhận điểm tựa từ **14. Quantization giảm bytes nhưng tạo accuracy/kernel sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Prefix reuse/bộ nhớ đệm (cache / 캐시) chỉ đúng khi ngữ nghĩa (semantic / 의미적) định danh (identity / 식별자) đúng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Tensor/mô hình (model / 모델) parallelism đổi cục bộ (local / 로컬) bộ nhớ (memory / 메모리) bài toán (problem / 문제) thành communication bài toán (problem / 문제)

Nếu mô hình (model / 모델) không fit một thiết bị (device / 장치) hoặc muốn tăng compute sức chứa (capacity / 용량), weights/operations có thể shard qua accelerators.

Mỗi tầng (layer / 계층) có thể cần collective communication. Decode độ trễ (latency / 지연 시간) lúc đó gồm:

```text
kernel compute
+
interconnect collective
+
synchronization/skew
```

Thêm GPU có thể chậm hơn nếu per-step công việc (work / 작업) nhỏ nhưng communication dominates. Topology/locality trở thành lower lớp trừu tượng (abstraction / 추상화) quyết định hành vi (behavior / 동작).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **16. Prefix reuse/bộ nhớ đệm (cache / 캐시) chỉ đúng khi ngữ nghĩa (semantic / 의미적) định danh (identity / 식별자) đúng** tiếp nhận điểm tựa từ **15. Tensor/mô hình (model / 모델) parallelism đổi cục bộ (local / 로컬) bộ nhớ (memory / 메모리) bài toán (problem / 문제) thành communication bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. mô hình (model / 모델) rollout phải phiên bản (version / 버전) cả serving trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Prefix reuse/bộ nhớ đệm (cache / 캐시) chỉ đúng khi ngữ nghĩa (semantic / 의미적) định danh (identity / 식별자) đúng

Nếu serving hệ thống (system / 시스템) reuse KV cho dùng chung (common / 공통) prefix, key phải bind đúng mô hình (model / 모델) phiên bản (version / 버전), tokenizer, prompt bytes/tokens, positional ngữ nghĩa (semantics / 의미론) và any adapter/ngữ cảnh (context / 맥락) affecting computation.

Bộ nhớ đệm (cache / 캐시) hit với wrong ngữ nghĩa (semantic / 의미적) key là tính đúng đắn (correctness / 정확성) bug, không phải stale-performance issue.

Đây là same family với bộ nhớ đệm (cache / 캐시) vô hiệu hóa (invalidation / 무효화): reuse chỉ an toàn khi định danh (identity / 식별자)/vô hiệu hóa (invalidation / 무효화) đặc tả hợp đồng (contract / 계약) đúng.

> **Chuyển mạch:** Trong **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **17. mô hình (model / 모델) rollout phải phiên bản (version / 버전) cả serving trạng thái (state / 상태)** tiếp nhận điểm tựa từ **16. Prefix reuse/bộ nhớ đệm (cache / 캐시) chỉ đúng khi ngữ nghĩa (semantic / 의미적) định danh (identity / 식별자) đúng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. OOM không phải thất bại (failure / 실패) duy nhất của bộ nhớ (memory / 메모리) pressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. mô hình (model / 모델) rollout phải phiên bản (version / 버전) cả serving trạng thái (state / 상태)

Nếu mô hình (model / 모델) weights/cấu hình (config / 설정)/adapters đổi, existing KV bộ nhớ đệm (cache / 캐시) được tạo từ phiên bản (version / 버전) cũ thường không thể tùy ý reuse với phiên bản (version / 버전) mới.

Triển khai (deployment / 배포) cần ranh giới (boundary / 경계):

```text
request pinned to model version
KV state belongs to same version
new requests route gradually
old in-flight requests drain or migrate only if explicitly supported
```

Canary mô hình (model / 모델) serving vì vậy là giao thức (protocol / 프로토콜)/trạng thái (state / 상태) rollout, không chỉ tải (load / 로드) new tệp (file / 파일).

> **Chuyển mạch:** Ở chặng này của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **18. OOM không phải thất bại (failure / 실패) duy nhất của bộ nhớ (memory / 메모리) pressure** tiếp nhận điểm tựa từ **17. mô hình (model / 모델) rollout phải phiên bản (version / 버전) cả serving trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. thử lại (retry / 재시도) suy luận (inference / 추론) có thể gây duplicate expensive công việc (work / 작업)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. OOM không phải thất bại (failure / 실패) duy nhất của bộ nhớ (memory / 메모리) pressure

Trước OOM, allocator fragmentation, KV eviction/swap, lower batch kích thước (size / 크기) và hàng đợi (queue / 큐) growth có thể làm p99 xấu.

Phase mô hình (model / 모델):

```text
ample memory → batch efficiently
near capacity → fragmentation/admission tighter
pressure → preemption/eviction/swap/recompute
overload → queue/timeout/retry/OOM
```

Monitor free bộ nhớ (memory / 메모리) alone không đủ; cần khối (block / 블록) fragmentation, active tokens/sequences và hàng đợi (queue / 큐) age.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **19. thử lại (retry / 재시도) suy luận (inference / 추론) có thể gây duplicate expensive công việc (work / 작업)** tiếp nhận điểm tựa từ **18. OOM không phải thất bại (failure / 실패) duy nhất của bộ nhớ (memory / 메모리) pressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. thử lại (retry / 재시도) suy luận (inference / 추론) có thể gây duplicate expensive công việc (work / 작업)

Máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) không chứng minh generation đã dừng. thử lại (retry / 재시도) long prompt có thể chạy prefill lần nữa và consume expensive GPU thời gian (time / 시간).

If streaming phản hồi (response / 응답), partial đầu ra (output / 출력) complicates ngữ nghĩa (semantics / 의미론) further. Serving gateway cần deadline/cancellation propagation và thử lại (retry / 재시도) ngân sách (budget / 예산); deterministic bad yêu cầu (request / 요청) không nên thử lại (retry / 재시도) như transient vận chuyển (transport / 전송) thất bại (failure / 실패).

AI serving obey same thử lại (retry / 재시도)→overload vòng phản hồi (feedback loop / 피드백 루프) as other phân tán (distributed / 분산) các hệ thống (systems / 시스템들), nhưng công việc (work / 작업) đơn vị (unit / 단위) đắt hơn nhiều.

> **Chuyển mạch:** Trong **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **19. thử lại (retry / 재시도) suy luận (inference / 추론) có thể gây duplicate expensive công việc (work / 작업)** nêu điều cần giải thích; **20. bằng chứng vận hành (production evidence / 운영 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. hiệu năng (performance / 성능) experiment phải giữ chất lượng (quality / 품질) + tải công việc (workload / 워크로드) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) nên tách scheduler/mô hình (model / 모델)/hardware:

```text
Workload:
- prompt/output length distributions
- active sequences/tokens
- tenant/priority mix

Scheduler:
- queue wait / TTFT
- batch size over time
- admitted/rejected/preempted requests
- KV blocks used/free/fragmentation

Model phases:
- prefill latency/throughput
- decode token latency/throughput

Hardware:
- accelerator utilization
- HBM bandwidth/memory occupancy
- interconnect collective time
- kernel occupancy/stalls where tooling supports

Reliability:
- OOM/retry/cancellation/late completion
- model-version/KV ownership
```

Một GPU-utilization 100% đồ thị (graph / 그래프) không nói thông lượng (throughput / 처리량) useful hay hàng đợi (queue / 큐) health.

> **Chuyển mạch:** Ở chặng này của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **20. bằng chứng vận hành (production evidence / 운영 증거)** nêu điều cần giải thích; **21. hiệu năng (performance / 성능) experiment phải giữ chất lượng (quality / 품질) + tải công việc (workload / 워크로드) ngữ nghĩa (semantics / 의미론)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **22. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. hiệu năng (performance / 성능) experiment phải giữ chất lượng (quality / 품질) + tải công việc (workload / 워크로드) ngữ nghĩa (semantics / 의미론)

Tối ưu hóa (optimization / 최적화) suy luận (inference / 추론) không chỉ “tokens/s cao hơn”. Compare phải giữ:

```text
same model/task or documented model change
same quality/evaluation threshold
same context/output distribution
same TTFT/token-latency SLO
same concurrency/tenant mix
```

Nếu quantization tăng thông lượng (throughput / 처리량) nhưng chất lượng (quality / 품질) vượt lỗi (error / 오류) ngân sách (budget / 예산), tối ưu hóa (optimization / 최적화) không đạt nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **22. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** tiếp nhận điểm tựa từ **21. hiệu năng (performance / 성능) experiment phải giữ chất lượng (quality / 품질) + tải công việc (workload / 워크로드) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?

Nếu TTFT cao nhưng decode nhanh, look hàng đợi (queue / 큐)/prefill. Nếu đơn vị từ (token / 토큰) độ trễ (latency / 지연 시간) cao ở large batch, inspect bandwidth/interconnect/scheduler. Nếu OOM dưới long ngữ cảnh (context / 맥락), KV sức chứa (capacity / 용량)/admission quyết định. Nếu one tenant hurts all, fairness is missing. Nếu same mô hình (model / 모델) different hardware behaves oddly, dữ liệu (data / 데이터) movement/kernel hỗ trợ (support / 지원) may dominate theoretical FLOPS.

> **Chuyển mạch:** Trong **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **23. Mô hình tư duy** gom các mảnh từ **22. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Mô hình tư duy

> Transformer suy luận (inference / 추론) là tương tác (interaction / 상호작용) giữa **mô hình (model / 모델) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), per-sequence KV trạng thái (state / 상태), scheduler và bộ nhớ (memory / 메모리) hierarchy**. KV bộ nhớ đệm (cache / 캐시) đổi recomputation lấy persistent bộ nhớ (memory / 메모리); batching đổi độ trễ (latency / 지연 시간) lấy thông lượng (throughput / 처리량); quantization đổi precision/chất lượng (quality / 품질) lấy bytes; parallelism đổi cục bộ (local / 로컬) compute lấy communication. **Serving tính đúng đắn (correctness / 정확성) cần giữ yêu cầu (request / 요청)/mô hình (model / 모델)/KV quyền sở hữu (ownership / 소유권); serving hiệu năng (performance / 성능) cần quản hàng đợi (queue / 큐), bộ nhớ (memory / 메모리) bandwidth và admission như một các hệ thống (systems / 시스템들) bài toán (problem / 문제).**

> **Chuyển mạch:** Ở chặng này của **Transformer internals, attention, KV bộ nhớ đệm (cache / 캐시) và suy luận (inference / 추론) chi phí (cost / 비용)**, **Kết nối** gom các mảnh từ **23. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Ôn [AI neural/transformer foundation](../../basic/10_ai_foundations/03_neural_networks_and_representation_learning.md), đọc [training/inference lifecycle](./00_training_inference_systems_and_model_lifecycle.md), [distributed training](./02_distributed_training_data_model_and_pipeline_parallelism.md), [GPU execution model](../../02_computer_architecture/advanced/06_simd_vector_isa_and_gpu_execution_model.md), [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và specialized AI thư viện (library / 라이브러리) tại [`../../02_artificial_intelligence/`](../../02_artificial_intelligence/README.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
