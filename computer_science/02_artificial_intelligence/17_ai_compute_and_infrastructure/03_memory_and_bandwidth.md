# Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Memory hierarchy và bandwidth trong AI**. Route đi từ registers/cache → HBM/DRAM → capacity/bandwidth/latency → data reuse → out-of-memory and serving limits, để bottleneck bộ nhớ được đọc cùng phép tính.

AI tải công việc (workload / 워크로드) xử lý tensor rất lớn. Trong nhiều trường hợp hiệu năng (performance / 성능) không bị giới hạn bởi số phép tính mà bởi việc **đưa dữ liệu tới compute đơn vị (unit / 단위) nhanh đến đâu**. Vì vậy bộ nhớ (memory / 메모리) sức chứa (capacity / 용량), hierarchy và bandwidth là phần cốt lõi của AI hạ tầng (infrastructure / 인프라).

## Bộ nhớ (memory / 메모리) Hierarchy

Một hệ thống có nhiều tầng bộ nhớ (memory / 메모리):

```text
register
→ on-chip cache / shared memory
→ HBM / VRAM
→ host RAM
→ NVMe / local storage
→ network / object storage
```

Tầng gần compute nhanh hơn nhưng nhỏ hơn và đắt hơn. Tối ưu hiệu năng cố giữ dữ liệu nóng (hot data) ở tầng gần nhất có thể.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Sức chứa (capacity / 용량), Bandwidth và độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) Hierarchy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weight bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sức chứa (capacity / 용량), Bandwidth và độ trễ (latency / 지연 시간)

Ba khái niệm khác nhau:

```text
capacity  = chứa được bao nhiêu dữ liệu
bandwidth = truyền được bao nhiêu dữ liệu mỗi giây
latency   = phải chờ bao lâu cho một lần truy cập
```

GPU có thể đủ VRAM để fit mô hình (model / 모델) nhưng vẫn bị bandwidth bottleneck.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Weight bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Sức chứa (capacity / 용량), Bandwidth và độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Activation bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weight bộ nhớ (memory / 메모리)

Với mô hình có `N` parameter, dung lượng xấp xỉ:

```text
FP32 ≈ 4N byte
FP16 ≈ 2N byte
INT8 ≈ 1N byte
INT4 ≈ 0.5N byte
```

Nhưng suy luận (inference / 추론) còn buffer, activation và KV bộ nhớ đệm (cache / 캐시); huấn luyện (training / 학습) còn độ dốc (gradient / 기울기) và optimizer trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Activation bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Weight bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Activation bộ nhớ (memory / 메모리)

Huấn luyện (training / 학습) cần lưu intermediate activation cho backpropagation.

Activation bộ nhớ (memory / 메모리) thường tăng theo:

```text
batch size × sequence length × hidden size × layers
```

**độ dốc (gradient / 기울기) checkpointing** giảm bộ nhớ (memory / 메모리) bằng cách không lưu toàn bộ activation mà recompute một phần trong backward pass.

Sự đánh đổi (trade-off / 트레이드오프):

```text
ít memory hơn ↔ nhiều compute hơn
```

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Activation bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **KV bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리)

Adam thường lưu first moment và second moment cho mỗi parameter. Nếu trạng thái (state / 상태) ở FP32, optimizer bộ nhớ (memory / 메모리) có thể lớn hơn weight bộ nhớ (memory / 메모리) nhiều lần.

Optimizer sharding hoặc lower-precision trạng thái (state / 상태) giúp giảm footprint.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **KV bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **Optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Query và Grouped-Query Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KV bộ nhớ đệm (cache / 캐시)

Autoregressive Transformer cần lưu Key/giá trị (value / 값) của các đơn vị từ (token / 토큰) trước cho mỗi tầng (layer / 계층).

KV bộ nhớ đệm (cache / 캐시) kích thước (size / 크기) xấp xỉ tỉ lệ với:

\[
Layers\times SequenceLength\times KVHeads\times HeadDim\times Precision\times Batch
\]

Vì vậy long ngữ cảnh (context / 맥락) và high tính đồng thời (concurrency / 동시성) có thể tiêu thụ bộ nhớ (memory / 메모리) nhanh hơn weights.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Multi-Query và Grouped-Query Attention** tiếp nhận điểm tựa từ **KV bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) Bandwidth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Query và Grouped-Query Attention

Giảm số K/V head giúp giảm KV bộ nhớ đệm (cache / 캐시) và bộ nhớ (memory / 메모리) bandwidth trong suy luận (inference / 추론).

Đây là ví dụ một thay đổi kiến trúc (architecture / 아키텍처) xuất phát trực tiếp từ ràng buộc (constraint / 제약조건) hardware/thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Bộ nhớ (memory / 메모리) Bandwidth** tiếp nhận điểm tựa từ **Multi-Query và Grouped-Query Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Arithmetic Intensity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) Bandwidth

Nếu mỗi đơn vị từ (token / 토큰) decode phải đọc một phần lớn mô hình (model / 모델) weights, thông lượng (throughput / 처리량) có thể bị giới hạn bởi HBM bandwidth.

Quantization giảm số byte cần đọc nên có thể tăng decode thông lượng (throughput / 처리량) ngay cả khi FLOP count gần như không đổi.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Arithmetic Intensity** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) Bandwidth** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Roofline mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Arithmetic Intensity

\[
AI=\frac{Operations}{Bytes\ moved}
\]

Arithmetic intensity thấp → thường memory-bound.

Arithmetic intensity cao → thường compute-bound.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Roofline mô hình (model / 모델)** tiếp nhận điểm tựa từ **Arithmetic Intensity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Reuse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Roofline mô hình (model / 모델)

Hiệu năng (performance / 성능) ceiling xấp xỉ:

```text
min(peak compute,
    memory bandwidth × arithmetic intensity)
```

Roofline giúp suy luận xem nên tối ưu compute hay bộ nhớ (memory / 메모리) traffic.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Roofline mô hình (model / 모델)** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Reuse** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Bộ nhớ đệm (cache / 캐시) Locality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Reuse

Phép nhân ma trận (matrix multiplication / 행렬 곱셈) hiệu quả vì cùng tile dữ liệu được reuse cho nhiều multiply-accumulate thao tác (operation / 연산).

Tiling giữ submatrix trong on-chip bộ nhớ (memory / 메모리) để dùng lại trước khi phải fetch dữ liệu mới từ HBM.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Dữ liệu (data / 데이터) Reuse** nêu điều cần giải thích; **Bộ nhớ đệm (cache / 캐시) Locality** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Truyền dữ liệu giữa CPU RAM và GPU VRAM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ đệm (cache / 캐시) Locality

Sequential hoặc coalesced truy cập (access / 접근) tận dụng bộ nhớ đệm (cache / 캐시) và burst tốt hơn random truy cập (access / 접근).

Embedding lookup có irregular bộ nhớ (memory / 메모리) truy cập (access / 접근) nên hành vi (behavior / 동작) khác dense GEMM.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Bộ nhớ đệm (cache / 캐시) Locality** nêu điều cần giải thích; **Truyền dữ liệu giữa CPU RAM và GPU VRAM** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Offloading** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truyền dữ liệu giữa CPU RAM và GPU VRAM

PCIe hoặc interconnect có bandwidth hữu hạn. Nếu mỗi yêu cầu (request / 요청) liên tục bản sao (copy / 복사) đầu vào (input / 입력) lớn hoặc mô hình (model / 모델) từ host sang GPU, GPU có thể idle để chờ dữ liệu.

Pinning, prefetch và async transfer giúp overlap compute với dữ liệu (data / 데이터) transfer.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Truyền dữ liệu giữa CPU RAM và GPU VRAM** nêu điều cần giải thích; **Offloading** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Unified bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Offloading

Khi mô hình (model / 모델) không fit GPU bộ nhớ (memory / 메모리), có thể offload weights, optimizer trạng thái (state / 상태) hoặc activation sang CPU hoặc NVMe.

Offloading tăng effective sức chứa (capacity / 용량) nhưng làm độ trễ (latency / 지연 시간) cao hơn vì đường truyền chậm hơn.

Phù hợp khi bộ nhớ (memory / 메모리) sức chứa (capacity / 용량) là hard ràng buộc (constraint / 제약조건) và tải công việc (workload / 워크로드) chấp nhận overhead.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Unified bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Offloading** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) Fragmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Unified bộ nhớ (memory / 메모리)

Unified virtual bộ nhớ (memory / 메모리) giúp lập trình đơn giản hơn, nhưng page di chuyển (migration / 마이그레이션) vẫn có chi phí (cost / 비용). “Unified” không nghĩa mọi bộ nhớ (memory / 메모리) truy cập (access / 접근) có hiệu năng giống nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Bộ nhớ (memory / 메모리) Fragmentation** tiếp nhận điểm tựa từ **Unified bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân tán (distributed / 분산) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) Fragmentation

Allocation có kích thước thay đổi tạo các khoảng trống trong bộ nhớ (memory / 메모리). LLM serving với nhiều chuỗi (sequence / 시퀀스) length rất dễ gặp fragmentation.

Paged hoặc khối (block / 블록) KV bộ nhớ đệm (cache / 캐시) dùng khối (block / 블록) kích thước cố định để reuse bộ nhớ (memory / 메모리) hiệu quả hơn.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Phân tán (distributed / 분산) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) Fragmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lưu trữ (storage / 저장소) I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân tán (distributed / 분산) bộ nhớ (memory / 메모리)

Khi mô hình (model / 모델) được shard qua nhiều GPU, mỗi thiết bị (device / 장치) giữ một phần weights hoặc activation. Khi đó communication trở thành một phần của effective bộ nhớ (memory / 메모리) truy cập (access / 접근) đường dẫn (path / 경로).

Tensor parallelism thường trao đổi partial activation ở mỗi tầng (layer / 계층), vì vậy interconnect bandwidth cực kỳ quan trọng.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Lưu trữ (storage / 저장소) I/O** tiếp nhận điểm tựa từ **Phân tán (distributed / 분산) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Economics của Long ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lưu trữ (storage / 저장소) I/O

Large checkpoint có thể mất nhiều phút để tải (load / 로드) nếu lưu trữ (storage / 저장소) hoặc mạng (network / 네트워크) chậm. phân tán (distributed / 분산) huấn luyện (training / 학습) cần parallel checkpointing và serialization hiệu quả.

Tần suất checkpoint có sự đánh đổi (trade-off / 트레이드오프):

```text
thường xuyên hơn → ít mất công khi failure
                 nhưng I/O overhead lớn hơn
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Economics của Long ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **Lưu trữ (storage / 저장소) I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Precision và bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Economics của Long ngữ cảnh (context / 맥락)

Ngữ cảnh (context / 맥락) length tăng không chỉ làm attention compute tăng mà còn làm KV bộ nhớ đệm (cache / 캐시) lớn hơn. Serving 100 người dùng (user / 사용자) với ngữ cảnh (context / 맥락) dài có thể memory-bound dù mô hình (model / 모델) weights vẫn fit dễ dàng.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Precision và bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Economics của Long ngữ cảnh (context / 맥락)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batch Sizing có nhận thức về bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Precision và bộ nhớ (memory / 메모리)

BF16/FP16 giảm một nửa số byte của weight hoặc activation so với FP32. INT8 và INT4 giảm thêm nữa.

Tuy nhiên conversion, quy mô (scale / 규모) siêu dữ liệu (metadata / 메타데이터) và kernel không được hỗ trợ có thể làm giảm benefit kỳ vọng.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Batch Sizing có nhận thức về bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Precision và bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **OOM thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batch Sizing có nhận thức về bộ nhớ (memory / 메모리)

Maximum batch không phải mục tiêu cuối. Cần chọn batch cân bằng:

- bộ nhớ (memory / 메모리) headroom;
- thông lượng (throughput / 처리량);
- tail độ trễ (latency / 지연 시간);
- OOM rủi ro (risk / 위험).

Động (dynamic / 동적) tải công việc (workload / 워크로드) cần chừa margin thay vì lấp đầy 100% VRAM.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **OOM thất bại (failure / 실패)** tiếp nhận điểm tựa từ **Batch Sizing có nhận thức về bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) Leak và Caching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OOM thất bại (failure / 실패)

Out-of-memory thường xảy ra vì peak allocation chứ không phải average allocation. Cần profile peak bộ nhớ (memory / 메모리) ở worst-case chuỗi (sequence / 시퀀스) length và batch kích thước (size / 크기).

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Bộ nhớ (memory / 메모리) Leak và Caching** tiếp nhận điểm tựa từ **OOM thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) Leak và Caching

Long-running serving thời gian chạy (runtime / 런타임) có allocator và bộ nhớ đệm (cache / 캐시) nên RSS hoặc VRAM có thể giữ high watermark. Không nên nhầm allocator caching với bộ nhớ (memory / 메모리) leak thật; cần inspect allocation hành vi (behavior / 동작).

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Mô hình tư duy** gom các mảnh từ **Bộ nhớ (memory / 메모리) Leak và Caching** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Compute hỏi: cần bao nhiêu phép toán?
Memory hỏi: dữ liệu ở đâu, phải di chuyển bao nhiêu byte và có thể reuse bao nhiêu lần?
```

Trong AI hiện đại, **dữ liệu (data / 데이터) movement cũng là một phần lớn của computation chi phí (cost / 비용)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “mô hình (model / 모델) fit VRAM nghĩa là serving ổn”

Không. KV bộ nhớ đệm (cache / 캐시), activation và tính đồng thời (concurrency / 동시성) còn cần thêm bộ nhớ (memory / 메모리).

### “Nhiều VRAM hơn nghĩa là nhanh hơn”

Không. sức chứa (capacity / 용량) và bandwidth là hai đại lượng khác nhau.

### “Unified bộ nhớ (memory / 메모리) loại bỏ transfer bottleneck”

Không. vật lý (physical / 물리적) dữ liệu (data / 데이터) movement vẫn tồn tại.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [GPU Architecture](./02_gpu_architecture.md), [Parallel Computing](./04_parallel_computing.md), [Quantization](../15_ai_engineering/06_quantization.md), [Caching/Batching](../15_ai_engineering/05_caching_and_batching.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
