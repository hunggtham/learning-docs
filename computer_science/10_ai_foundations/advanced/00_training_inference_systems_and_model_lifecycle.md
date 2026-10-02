# Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Training, inference systems và model lifecycle**. Route đi từ artifact/behavior invariant → training dataflow/optimization state → checkpoint/serving → monitoring/drift → reproducible promotion, để model behavior truy được tới artifact và vòng đời.

Foundation ML thường tập trung mô hình (model / 모델), mất mát (loss / 손실) và generalization. môi trường vận hành (production / 운영 환경) AI cần thêm mô hình tư duy (mental model / 사고 모델) các hệ thống (systems / 시스템들): **dữ liệu (data / 데이터), mô hình (model / 모델), optimizer trạng thái (state / 상태) và serving thời gian chạy (runtime / 런타임) đi qua một vòng đời (lifecycle / 생명주기) versioned**, và mỗi stage có bất biến (invariant / 불변식), tài nguyên (resource / 자원) bottleneck, dạng thất bại (failure mode / 실패 모드) và bằng chứng (evidence / 증거) riêng.

Mô hình (model / 모델) weights chỉ là một sản phẩm tạo ra (artifact / 산출물). Một môi trường vận hành (production / 운영 환경) mô hình (model / 모델) thực tế phụ thuộc tokenizer/preprocessing, tính năng (feature / 기능)/dữ liệu (data / 데이터) lược đồ (schema / 스키마), mã (code / 코드), checkpoint trạng thái (state / 상태), thời gian chạy (runtime / 런타임) kernels, hardware, serving cấu hình (config / 설정) và evaluation đặc tả hợp đồng (contract / 계약).

## 1. bất biến (invariant / 불변식) đầu tiên: phải biết chính xác sản phẩm tạo ra (artifact / 산출물) nào tạo ra hành vi (behavior / 동작)

Nếu môi trường vận hành (production / 운영 환경) trả đầu ra (output / 출력) sai, câu “đang dùng mô hình (model / 모델) v42” chưa đủ. Cần biết bundle:

```text
training data/version/provenance
preprocessing/tokenizer/feature code
model architecture + weights
optimizer/checkpoint metadata khi resume training
runtime/library/kernel versions
quantization format
serving config + thresholds
prompt/template nếu system có layer đó
```

Reproducibility bất biến (invariant / 불변식) là: từ sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자) và provenance, nhóm (team / 팀) phải có khả năng giải thích mô hình (model / 모델) nào, dữ liệu (data / 데이터) nào và thời gian chạy (runtime / 런타임) nào tạo hành vi (behavior / 동작) đang quan sát.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, biết phải giữ gì trong **1. bất biến (invariant / 불변식) đầu tiên: phải biết chính xác sản phẩm tạo ra (artifact / 산출물) nào tạo ra hành vi (behavior / 동작)**, ta theo dõi trong **2. huấn luyện (training / 학습) hệ thống (system / 시스템) là dataflow + tối ưu hóa (optimization / 최적화) trạng thái (state / 상태)** cách hệ thống thực hiện và phản hồi qua từng bước. Từ đây, **3. Checkpoint không chỉ là weights** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. huấn luyện (training / 학습) hệ thống (system / 시스템) là dataflow + tối ưu hóa (optimization / 최적화) trạng thái (state / 상태)

Một huấn luyện (training / 학습) step thường là:

```text
storage
→ read/decode/preprocess
→ shuffle/sample/batch
→ host memory
→ accelerator transfer
→ forward
→ loss
→ backward
→ gradient synchronization
→ optimizer update
→ checkpoint/metrics
```

GPU utilization thấp không tự động nghĩa GPU yếu. đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인), dữ liệu (data / 데이터) loader, synchronization hoặc host→thiết bị (device / 장치) transfer có thể làm accelerator starve.

Hiệu năng (performance / 성능) lập luận (reasoning / 추론) phải profile toàn chuỗi xử lý (pipeline / 파이프라인) thay vì chỉ kernel compute.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **2. huấn luyện (training / 학습) hệ thống (system / 시스템) là dataflow + tối ưu hóa (optimization / 최적화) trạng thái (state / 상태)** xác định đầu vào; **3. Checkpoint không chỉ là weights** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. dữ liệu (data / 데이터) thứ tự (ordering / 순서) và randomness cũng là trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Checkpoint không chỉ là weights

Để resume huấn luyện (training / 학습) gần tương đương trajectory trước interruption, thường cần:

```text
model parameters
optimizer state
scheduler state
random/RNG state
gradient scaler nếu mixed precision
training step/epoch/data position
parallelism/sharding metadata
```

Chỉ lưu weights có thể tiếp tục từ cùng mô hình (model / 모델) parameters nhưng không phải cùng tối ưu hóa (optimization / 최적화) trạng thái (state / 상태).

Bất biến (invariant / 불변식) khôi phục (recovery / 복구) cần được định nghĩa rõ: “resume usable mô hình (model / 모델)” hay “resume equivalent huấn luyện (training / 학습) trạng thái (state / 상태)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **3. Checkpoint không chỉ là weights** nêu điều cần giải thích; **4. dữ liệu (data / 데이터) thứ tự (ordering / 순서) và randomness cũng là trạng thái (state / 상태)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. phân tán (distributed / 분산) huấn luyện (training / 학습) thêm communication bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. dữ liệu (data / 데이터) thứ tự (ordering / 순서) và randomness cũng là trạng thái (state / 상태)

Shuffle seed, sampler position, dữ liệu (data / 데이터) augmentation randomness và phân tán (distributed / 분산) worker partitioning có thể thay huấn luyện (training / 학습) trajectory.

Reproducibility tuyệt đối trên accelerators đôi khi khó vì nondeterministic kernels, reduction thứ tự (order / 순서) hoặc floating-point hành vi (behavior / 동작). Điều quan trọng là phân biệt:

```text
bitwise reproducibility
statistical reproducibility
model-quality reproducibility
```

Không hứa mức mạnh hơn ngăn xếp (stack / 스택) thực sự đảm bảo.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **4. dữ liệu (data / 데이터) thứ tự (ordering / 순서) và randomness cũng là trạng thái (state / 상태)** nêu điều cần giải thích; **5. phân tán (distributed / 분산) huấn luyện (training / 학습) thêm communication bất biến (invariant / 불변식)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. Straggler quyết định step thời gian (time / 시간) trong synchronous huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. phân tán (distributed / 분산) huấn luyện (training / 학습) thêm communication bất biến (invariant / 불변식)

Dữ liệu (data / 데이터) parallelism replicate mô hình (model / 모델) và aggregate gradients. Tensor/mô hình (model / 모델)/chuỗi xử lý (pipeline / 파이프라인) parallelism chia computation/trạng thái (state / 상태) theo dimension khác.

Mỗi chiến lược (strategy / 전략) cần giữ một bất biến (invariant / 불변식) tương đương với tối ưu hóa (optimization / 최적화) step mong muốn: gradients/parameters phải được combine theo giao thức (protocol / 프로토콜) đúng, không để worker dùng trạng thái (state / 상태) lệch không được mô hình (model / 모델) ngữ nghĩa (semantics / 의미론) cho phép.

Thất bại (failure / 실패) một worker có thể làm collective communication treo hoặc cả job restart. phân tán (distributed / 분산) huấn luyện (training / 학습) vì thế là distributed-systems bài toán (problem / 문제) chứ không chỉ tuyến tính (linear / 선형) algebra.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **6. Straggler quyết định step thời gian (time / 시간) trong synchronous huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **5. phân tán (distributed / 분산) huấn luyện (training / 학습) thêm communication bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Communication topology là lower tầng (layer / 계층) quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Straggler quyết định step thời gian (time / 시간) trong synchronous huấn luyện (training / 학습)

Synchronous step thường phải chờ participants cần thiết. Một GPU/nút (node / 노드) chậm do thermal throttling, mạng (network / 네트워크) congestion, data-loader stall hoặc hardware lỗi (error / 오류) có thể kéo toàn job.

Step độ trễ (latency / 지연 시간) gần với slowest required participant, tương tự tail amplification trong fan-out dịch vụ (service / 서비스).

Bằng chứng (evidence / 증거) cần per-rank/per-stage timing, không chỉ toàn cục (global / 전역) tokens/s.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **7. Communication topology là lower tầng (layer / 계층) quan trọng** tiếp nhận điểm tựa từ **6. Straggler quyết định step thời gian (time / 시간) trong synchronous huấn luyện (training / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Mixed precision và numerical stability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Communication topology là lower tầng (layer / 계층) quan trọng

All-reduce hoặc tensor-parallel communication phụ thuộc PCIe/NVLink/InfiniBand/Ethernet topology, bandwidth và độ trễ (latency / 지연 시간).

Mô hình (model / 모델) có arithmetic intensity cao có thể quy mô (scale / 규모) tốt; mô hình (model / 모델) nhỏ hoặc communication-heavy có thể đạt speedup rất kém khi thêm accelerators.

Hiệu năng (performance / 성능) bất biến (invariant / 불변식) không phải “GPU count gấp đôi thì thông lượng (throughput / 처리량) gấp đôi”. Speedup bị giới hạn bởi compute/communication ratio, synchronization và tải (load / 로드) imbalance.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **8. Mixed precision và numerical stability** tiếp nhận điểm tựa từ **7. Communication topology là lower tầng (layer / 계층) quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. suy luận (inference / 추론) có mục tiêu (objective / 목표) khác huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Mixed precision và numerical stability

FP16/BF16/TF32/low precision tăng thông lượng (throughput / 처리량) và giảm bộ nhớ (memory / 메모리) bandwidth/footprint nhưng đổi numerical hành vi (behavior / 동작).

Mất mát (loss / 손실) scaling, accumulation precision và kernel choice quyết định stability. NaN/Inf có thể xuất hiện khi động (dynamic / 동적) phạm vi (range / 범위) không đủ hoặc optimizer trạng thái (state / 상태) bất ổn.

Đây là liên kết (connection / 연결) giữa numerical biểu diễn (representation / 표현) và các hệ thống (systems / 시스템들) hiệu năng (performance / 성능): chọn precision là một correctness-performance sự đánh đổi (trade-off / 트레이드오프), không chỉ hardware flag.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **9. suy luận (inference / 추론) có mục tiêu (objective / 목표) khác huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **8. Mixed precision và numerical stability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. động (dynamic / 동적)/continuous batching là queueing quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. suy luận (inference / 추론) có mục tiêu (objective / 목표) khác huấn luyện (training / 학습)

Huấn luyện (training / 학습) thường tối ưu thông lượng (throughput / 처리량)/chi phí (cost / 비용) theo samples hoặc tokens processed. Online suy luận (inference / 추론) quan tâm:

```text
p50/p95/p99 latency
throughput
time-to-first-token nếu autoregressive
inter-token latency
memory per request
availability
cost per request/token
```

Một tối ưu hóa (optimization / 최적화) tăng total thông lượng (throughput / 처리량) nhưng làm p99 vượt SLO có thể không phù hợp môi trường vận hành (production / 운영 환경) API.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **10. động (dynamic / 동적)/continuous batching là queueing quyết định (decision / 결정)** tiếp nhận điểm tựa từ **9. suy luận (inference / 추론) có mục tiêu (objective / 목표) khác huấn luyện (training / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. KV bộ nhớ đệm (cache / 캐시) biến ngữ cảnh (context / 맥락) thành memory-capacity bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. động (dynamic / 동적)/continuous batching là queueing quyết định (decision / 결정)

Batching tăng accelerator utilization nhưng yêu cầu (request / 요청) phải chờ batch formation. Continuous batching tái sử dụng slots khi sequences hoàn tất khác thời điểm.

Mô hình tư duy (mental model / 사고 모델):

```text
batch lớn hơn
→ compute efficiency tăng
→ queue/batching wait có thể tăng
→ memory pressure/concurrency thay đổi
```

Batch scheduler vì vậy là một admission/queueing controller tương tự Software các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **11. KV bộ nhớ đệm (cache / 캐시) biến ngữ cảnh (context / 맥락) thành memory-capacity bài toán (problem / 문제)** tiếp nhận điểm tựa từ **10. động (dynamic / 동적)/continuous batching là queueing quyết định (decision / 결정)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Quantization không đồng nghĩa luôn nhanh hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. KV bộ nhớ đệm (cache / 캐시) biến ngữ cảnh (context / 맥락) thành memory-capacity bài toán (problem / 문제)

Autoregressive Transformer lưu key/giá trị (value / 값) states của prior tokens để không recompute toàn prefix mỗi đơn vị từ (token / 토큰).

KV bộ nhớ đệm (cache / 캐시) bộ nhớ (memory / 메모리) tăng theo roughly:

```text
sequence length
× layers
× hidden/head dimensions
× bytes per element
× concurrent sequences
```

Ngữ cảnh (context / 맥락) length dài có thể giảm tính đồng thời (concurrency / 동시성) mạnh dù weights không đổi. Khi bộ nhớ (memory / 메모리) gần đầy, allocator fragmentation hoặc bộ nhớ đệm (cache / 캐시) eviction/offload có thể làm độ trễ (latency / 지연 시간) phase-change.

Suy luận (inference / 추론) bottleneck lúc đó là bộ nhớ (memory / 메모리) sức chứa (capacity / 용량)/bandwidth, không phải raw FLOPS.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **12. Quantization không đồng nghĩa luôn nhanh hơn** tiếp nhận điểm tựa từ **11. KV bộ nhớ đệm (cache / 캐시) biến ngữ cảnh (context / 맥락) thành memory-capacity bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. mô hình (model / 모델) loading và cold start là môi trường vận hành (production / 운영 환경) phase riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Quantization không đồng nghĩa luôn nhanh hơn

INT8/FP8/low-bit weights giảm footprint/bandwidth, nhưng speedup phụ thuộc kernel hỗ trợ (support / 지원), dequantization overhead, packing bố cục (layout / 레이아웃) và hardware thực thi (execution / 실행) units.

Một mô hình (model / 모델) nhỏ fit bộ nhớ đệm (cache / 캐시) tốt sẵn có thể không được lợi nhiều. Quantization cũng có chất lượng (quality / 품질) impact khác theo tầng (layer / 계층)/tác vụ (task / 작업)/dữ liệu (data / 데이터) phân phối (distribution / 분포).

Do đó phải evaluate **chất lượng (quality / 품질) + độ trễ (latency / 지연 시간) + thông lượng (throughput / 처리량) + bộ nhớ (memory / 메모리)** cùng nhau trên triển khai (deployment / 배포) tải công việc (workload / 워크로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **13. mô hình (model / 모델) loading và cold start là môi trường vận hành (production / 운영 환경) phase riêng** tiếp nhận điểm tựa từ **12. Quantization không đồng nghĩa luôn nhanh hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. mô hình (model / 모델) registry là provenance hệ thống (system / 시스템), không chỉ tệp (file / 파일) store** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. mô hình (model / 모델) loading và cold start là môi trường vận hành (production / 운영 환경) phase riêng

Large mô hình (model / 모델) start có thể gồm download sản phẩm tạo ra (artifact / 산출물), checksum, deserialize, allocate bộ nhớ (memory / 메모리), compile kernels/JIT, warm caches và create KV allocator.

Autoscaling chỉ dựa CPU/GPU utilization có thể phản ứng quá chậm nếu new replica mất nhiều phút mới ready.

Sức chứa (capacity / 용량) thiết kế (design / 설계) cần mô hình (model / 모델) warm sức chứa (capacity / 용량), startup thời gian (time / 시간) và triển khai (deployment / 배포) headroom.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **14. mô hình (model / 모델) registry là provenance hệ thống (system / 시스템), không chỉ tệp (file / 파일) store** tiếp nhận điểm tựa từ **13. mô hình (model / 모델) loading và cold start là môi trường vận hành (production / 운영 환경) phase riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Offline chỉ số (metric / 지표) và online kết quả (outcome / 결과) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. mô hình (model / 모델) registry là provenance hệ thống (system / 시스템), không chỉ tệp (file / 파일) store

Registry cần nối sản phẩm tạo ra (artifact / 산출물) với:

```text
code commit/config
dataset snapshot/provenance
evaluation result
approval/deployment status
runtime compatibility
rollback target
```

Phiên bản (version / 버전) weights nhưng không phiên bản (version / 버전) tokenizer/lược đồ (schema / 스키마) có thể tạo silent incompatibility.

“mô hình (model / 모델)” nên được coi là bundle có đặc tả hợp đồng (contract / 계약), không phải một `.bin` đơn lẻ.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **15. Offline chỉ số (metric / 지표) và online kết quả (outcome / 결과) khác nhau** tiếp nhận điểm tựa từ **14. mô hình (model / 모델) registry là provenance hệ thống (system / 시스템), không chỉ tệp (file / 파일) store** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. dữ liệu (data / 데이터)/mô hình (model / 모델) drift không có một chỉ số (metric / 지표) universal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Offline chỉ số (metric / 지표) và online kết quả (outcome / 결과) khác nhau

Kiểm tra hợp lệ (validation / 검증) accuracy/F1/mất mát (loss / 손실) không tự động dự đoán nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과) do threshold, độ trễ (latency / 지연 시간), population shift, người dùng (user / 사용자) adaptation hoặc vòng phản hồi (feedback loop / 피드백 루프).

Triển khai (deployment / 배포) có thể cần shadow, canary hoặc A/B tùy rủi ro (risk / 위험). Nhưng online experiment cũng phải giữ hệ thống (system / 시스템) bất biến (invariant / 불변식): cohort assignment ổn định, exposure logged, an toàn (safety / 안전) các ràng buộc (constraints / 제약조건들) enforce trước mô hình (model / 모델) quyết định (decision / 결정) nếu cần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **15. Offline chỉ số (metric / 지표) và online kết quả (outcome / 결과) khác nhau** nêu điều cần giải thích; **16. dữ liệu (data / 데이터)/mô hình (model / 모델) drift không có một chỉ số (metric / 지표) universal** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. Retraining là chuyển tiếp trạng thái (state transition / 상태 전이) có regression rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. dữ liệu (data / 데이터)/mô hình (model / 모델) drift không có một chỉ số (metric / 지표) universal

Đầu vào (input / 입력) phân phối (distribution / 분포) thay đổi không luôn làm chất lượng (quality / 품질) xấu; chất lượng (quality / 품질) có thể xấu mà simple tính năng (feature / 기능) phân phối (distribution / 분포) không drift rõ.

Khi labels đến chậm, monitoring thường phải kết hợp:

```text
schema/data-quality violations
input distribution
score/confidence distribution
system latency/error
human/business proxy
late-arriving labeled evaluation
```

Không nên gọi một divergence score là “accuracy real-time” nếu không có ground truth.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **16. dữ liệu (data / 데이터)/mô hình (model / 모델) drift không có một chỉ số (metric / 지표) universal** nêu điều cần giải thích; **17. Retraining là chuyển tiếp trạng thái (state transition / 상태 전이) có regression rủi ro (risk / 위험)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. thất bại (failure / 실패) modes cần được phân lớp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Retraining là chuyển tiếp trạng thái (state transition / 상태 전이) có regression rủi ro (risk / 위험)

Retrain hàng ngày không tự động tốt. dữ liệu (data / 데이터) cửa sổ (window / 윈도우), label delay, concept drift, chi phí (cost / 비용) và poisoning/bad-data rủi ro (risk / 위험) cần chính sách (policy / 정책).

Chuỗi xử lý (pipeline / 파이프라인) hợp lý là:

```text
new data
→ train candidate
→ evaluate against fixed + recent slices
→ safety/regression checks
→ approve/canary
→ observe
→ promote hoặc rollback
```

Mỗi retrain tạo sản phẩm tạo ra (artifact / 산출물) mới; auto-promotion càng mạnh thì guardrail/provenance càng phải mạnh.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **18. thất bại (failure / 실패) modes cần được phân lớp** tiếp nhận điểm tựa từ **17. Retraining là chuyển tiếp trạng thái (state transition / 상태 전이) có regression rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. thất bại (failure / 실패) modes cần được phân lớp

Huấn luyện (training / 학습):

```text
input starvation
OOM
NaN/divergence
collective hang
straggler
checkpoint corruption/incompatibility
bad-data regression
```

Suy luận (inference / 추론):

```text
queue overload
OOM/KV exhaustion
cold-start capacity loss
kernel/runtime crash
model/tokenizer mismatch
latency regression
bad model output dưới distribution shift
```

Gom mọi thứ thành “mô hình (model / 모델) issue” làm investigation sai tầng (layer / 계층).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **18. thất bại (failure / 실패) modes cần được phân lớp** nêu điều cần giải thích; **19. bằng chứng vận hành (production evidence / 운영 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. bằng chứng vận hành (production evidence / 운영 증거)

Huấn luyện (training / 학습) bằng chứng (evidence / 증거) nên có:

```text
samples/tokens per second
GPU/accelerator utilization
input-pipeline wait
per-rank step timing
communication time
memory allocated/reserved
loss/gradient statistics
checkpoint duration/failure
```

Suy luận (inference / 추론) bằng chứng (evidence / 증거) nên có:

```text
time-to-first-token / inter-token latency
batching/queue wait
active sequences/concurrency
KV-cache usage/fragmentation
accelerator compute + memory utilization
model/runtime version
OOM/rejection rate
quality/evaluation slices
```

Metrics phải giữ sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자) để regression có thể correlate với mô hình (model / 모델)/thời gian chạy (runtime / 런타임)/cấu hình (config / 설정) rollout.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **19. bằng chứng vận hành (production evidence / 운영 증거)** nêu điều cần giải thích; **20. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. liên kết (connection / 연결) với độ tin cậy (reliability / 신뢰성) và hệ thống (system / 시스템) thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?

GPU utilization thấp có thể do lưu trữ (storage / 저장소)/dữ liệu (data / 데이터) loader/CPU, không phải GPU. suy luận (inference / 추론) p99 tăng có thể do hàng đợi (queue / 큐)/batching, allocator hoặc mạng (network / 네트워크). phân tán (distributed / 분산) huấn luyện (training / 학습) hang có thể do interconnect/collective thư viện (library / 라이브러리). chất lượng (quality / 품질) regression có thể do tokenizer/dữ liệu (data / 데이터) lược đồ (schema / 스키마) chứ không phải weights.

AI các hệ thống (systems / 시스템들) debugging phải đi xuống đúng lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층) như mọi phân tán (distributed / 분산)/software hệ thống (system / 시스템) khác.

> **Chuyển mạch:** Ở chặng này của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, sau nội dung của **20. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?**, **21. liên kết (connection / 연결) với độ tin cậy (reliability / 신뢰성) và hệ thống (system / 시스템) thiết kế (design / 설계)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **22. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. liên kết (connection / 연결) với độ tin cậy (reliability / 신뢰성) và hệ thống (system / 시스템) thiết kế (design / 설계)

Mô hình (model / 모델) serving là dịch vụ (service / 서비스) có finite sức chứa (capacity / 용량). thử lại (retry / 재시도), admission điều khiển (control / 제어), tải (load / 로드) shedding và graceful degradation vẫn áp dụng.

Ví dụ ngữ cảnh (context / 맥락) quá dài làm KV bộ nhớ đệm (cache / 캐시) đầy → hàng đợi (queue / 큐) tăng → hết thời gian chờ (timeout / 타임아웃) → gateway thử lại (retry / 재시도) → duplicate suy luận (inference / 추론) công việc (work / 작업) → overload. Fix không nhất thiết là “GPU mạnh hơn”; có thể cần đơn vị từ (token / 토큰) limit, tính đồng thời (concurrency / 동시성) admission, thử lại (retry / 재시도) ngân sách (budget / 예산) và overload phản hồi (response / 응답).

AI không đứng ngoài Khoa học máy tính (computer science / 컴퓨터 과학) các hệ thống (systems / 시스템들) principles; nó chỉ có tài nguyên (resource / 자원) shape khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **22. Mô hình tư duy** gom các mảnh từ **21. liên kết (connection / 연결) với độ tin cậy (reliability / 신뢰성) và hệ thống (system / 시스템) thiết kế (design / 설계)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Mô hình tư duy

> môi trường vận hành (production / 운영 환경) AI là **versioned dataflow + tối ưu hóa (optimization / 최적화) trạng thái (state / 상태) + phân tán (distributed / 분산) compute + serving hàng đợi (queue / 큐) + evaluation vòng phản hồi (feedback loop / 피드백 루프)**. bất biến (invariant / 불변식) về provenance/khôi phục (recovery / 복구)/tính đúng đắn (correctness / 정확성) phải được giữ qua dữ liệu (data / 데이터)/mô hình (model / 모델)/thời gian chạy (runtime / 런타임) versions; hiệu năng (performance / 성능) bị quyết định bởi compute, bộ nhớ (memory / 메모리), communication và queueing; bằng chứng (evidence / 증거) phải nối mô hình (model / 모델) chất lượng (quality / 품질) với hệ thống (system / 시스템) hành vi (behavior / 동작) thay vì coi weights là toàn bộ hệ thống.

> **Chuyển mạch:** Trong **Huấn luyện (training / 학습), suy luận (inference / 추론) các hệ thống (systems / 시스템들) và mô hình (model / 모델) vòng đời (lifecycle / 생명주기)**, **Kết nối** gom các mảnh từ **22. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [ML foundation](../../basic/10_ai_foundations/02_machine_learning_foundations.md), [Transformer/KV cache](./01_transformer_attention_kv_cache_and_inference_cost.md), [Distributed training](./02_distributed_training_data_model_and_pipeline_parallelism.md), [Capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md) và [Deployment safety](../../09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
