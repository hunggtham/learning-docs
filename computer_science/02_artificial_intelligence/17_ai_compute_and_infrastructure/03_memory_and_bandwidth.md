# Bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI

> **Mạch đọc:** Đặt **bộ nhớ (memory / 메모리) Hierarchy và Bandwidth trong AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **bộ nhớ (memory / 메모리) Hierarchy** sang **sức chứa (capacity / 용량), Bandwidth và độ trễ (latency / 지연 시간)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Sức chứa (capacity / 용량), Bandwidth và độ trễ (latency / 지연 시간)

Ba khái niệm khác nhau:

```text
capacity  = chứa được bao nhiêu dữ liệu
bandwidth = truyền được bao nhiêu dữ liệu mỗi giây
latency   = phải chờ bao lâu cho một lần truy cập
```

GPU có thể đủ VRAM để fit mô hình (model / 모델) nhưng vẫn bị bandwidth bottleneck.

## Weight bộ nhớ (memory / 메모리)

Với mô hình có `N` parameter, dung lượng xấp xỉ:

```text
FP32 ≈ 4N byte
FP16 ≈ 2N byte
INT8 ≈ 1N byte
INT4 ≈ 0.5N byte
```

Nhưng suy luận (inference / 추론) còn buffer, activation và KV bộ nhớ đệm (cache / 캐시); huấn luyện (training / 학습) còn độ dốc (gradient / 기울기) và optimizer trạng thái (state / 상태).

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

## Optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리)

Adam thường lưu first moment và second moment cho mỗi parameter. Nếu trạng thái (state / 상태) ở FP32, optimizer bộ nhớ (memory / 메모리) có thể lớn hơn weight bộ nhớ (memory / 메모리) nhiều lần.

Optimizer sharding hoặc lower-precision trạng thái (state / 상태) giúp giảm footprint.

## KV bộ nhớ đệm (cache / 캐시)

Autoregressive Transformer cần lưu Key/giá trị (value / 값) của các đơn vị từ (token / 토큰) trước cho mỗi tầng (layer / 계층).

KV bộ nhớ đệm (cache / 캐시) kích thước (size / 크기) xấp xỉ tỉ lệ với:

\[
Layers\times SequenceLength\times KVHeads\times HeadDim\times Precision\times Batch
\]

Vì vậy long ngữ cảnh (context / 맥락) và high tính đồng thời (concurrency / 동시성) có thể tiêu thụ bộ nhớ (memory / 메모리) nhanh hơn weights.

## Multi-Query và Grouped-Query Attention

Giảm số K/V head giúp giảm KV bộ nhớ đệm (cache / 캐시) và bộ nhớ (memory / 메모리) bandwidth trong suy luận (inference / 추론).

Đây là ví dụ một thay đổi kiến trúc (architecture / 아키텍처) xuất phát trực tiếp từ ràng buộc (constraint / 제약조건) hardware/thời gian chạy (runtime / 런타임).

## Bộ nhớ (memory / 메모리) Bandwidth

Nếu mỗi đơn vị từ (token / 토큰) decode phải đọc một phần lớn mô hình (model / 모델) weights, thông lượng (throughput / 처리량) có thể bị giới hạn bởi HBM bandwidth.

Quantization giảm số byte cần đọc nên có thể tăng decode thông lượng (throughput / 처리량) ngay cả khi FLOP count gần như không đổi.

## Arithmetic Intensity

\[
AI=\frac{Operations}{Bytes\ moved}
\]

Arithmetic intensity thấp → thường memory-bound.

Arithmetic intensity cao → thường compute-bound.

## Roofline mô hình (model / 모델)

Hiệu năng (performance / 성능) ceiling xấp xỉ:

```text
min(peak compute,
    memory bandwidth × arithmetic intensity)
```

Roofline giúp suy luận xem nên tối ưu compute hay bộ nhớ (memory / 메모리) traffic.

## Dữ liệu (data / 데이터) Reuse

Phép nhân ma trận (matrix multiplication / 행렬 곱셈) hiệu quả vì cùng tile dữ liệu được reuse cho nhiều multiply-accumulate thao tác (operation / 연산).

Tiling giữ submatrix trong on-chip bộ nhớ (memory / 메모리) để dùng lại trước khi phải fetch dữ liệu mới từ HBM.

## Bộ nhớ đệm (cache / 캐시) Locality

Sequential hoặc coalesced truy cập (access / 접근) tận dụng bộ nhớ đệm (cache / 캐시) và burst tốt hơn random truy cập (access / 접근).

Embedding lookup có irregular bộ nhớ (memory / 메모리) truy cập (access / 접근) nên hành vi (behavior / 동작) khác dense GEMM.

## Truyền dữ liệu giữa CPU RAM và GPU VRAM

PCIe hoặc interconnect có bandwidth hữu hạn. Nếu mỗi yêu cầu (request / 요청) liên tục bản sao (copy / 복사) đầu vào (input / 입력) lớn hoặc mô hình (model / 모델) từ host sang GPU, GPU có thể idle để chờ dữ liệu.

Pinning, prefetch và async transfer giúp overlap compute với dữ liệu (data / 데이터) transfer.

## Offloading

Khi mô hình (model / 모델) không fit GPU bộ nhớ (memory / 메모리), có thể offload weights, optimizer trạng thái (state / 상태) hoặc activation sang CPU hoặc NVMe.

Offloading tăng effective sức chứa (capacity / 용량) nhưng làm độ trễ (latency / 지연 시간) cao hơn vì đường truyền chậm hơn.

Phù hợp khi bộ nhớ (memory / 메모리) sức chứa (capacity / 용량) là hard ràng buộc (constraint / 제약조건) và tải công việc (workload / 워크로드) chấp nhận overhead.

## Unified bộ nhớ (memory / 메모리)

Unified virtual bộ nhớ (memory / 메모리) giúp lập trình đơn giản hơn, nhưng page di chuyển (migration / 마이그레이션) vẫn có chi phí (cost / 비용). “Unified” không nghĩa mọi bộ nhớ (memory / 메모리) truy cập (access / 접근) có hiệu năng giống nhau.

## Bộ nhớ (memory / 메모리) Fragmentation

Allocation có kích thước thay đổi tạo các khoảng trống trong bộ nhớ (memory / 메모리). LLM serving với nhiều chuỗi (sequence / 시퀀스) length rất dễ gặp fragmentation.

Paged hoặc khối (block / 블록) KV bộ nhớ đệm (cache / 캐시) dùng khối (block / 블록) kích thước cố định để reuse bộ nhớ (memory / 메모리) hiệu quả hơn.

## Phân tán (distributed / 분산) bộ nhớ (memory / 메모리)

Khi mô hình (model / 모델) được shard qua nhiều GPU, mỗi thiết bị (device / 장치) giữ một phần weights hoặc activation. Khi đó communication trở thành một phần của effective bộ nhớ (memory / 메모리) truy cập (access / 접근) đường dẫn (path / 경로).

Tensor parallelism thường trao đổi partial activation ở mỗi tầng (layer / 계층), vì vậy interconnect bandwidth cực kỳ quan trọng.

## Lưu trữ (storage / 저장소) I/O

Large checkpoint có thể mất nhiều phút để tải (load / 로드) nếu lưu trữ (storage / 저장소) hoặc mạng (network / 네트워크) chậm. phân tán (distributed / 분산) huấn luyện (training / 학습) cần parallel checkpointing và serialization hiệu quả.

Tần suất checkpoint có sự đánh đổi (trade-off / 트레이드오프):

```text
thường xuyên hơn → ít mất công khi failure
                 nhưng I/O overhead lớn hơn
```

## Economics của Long ngữ cảnh (context / 맥락)

Ngữ cảnh (context / 맥락) length tăng không chỉ làm attention compute tăng mà còn làm KV bộ nhớ đệm (cache / 캐시) lớn hơn. Serving 100 người dùng (user / 사용자) với ngữ cảnh (context / 맥락) dài có thể memory-bound dù mô hình (model / 모델) weights vẫn fit dễ dàng.

## Precision và bộ nhớ (memory / 메모리)

BF16/FP16 giảm một nửa số byte của weight hoặc activation so với FP32. INT8 và INT4 giảm thêm nữa.

Tuy nhiên conversion, quy mô (scale / 규모) siêu dữ liệu (metadata / 메타데이터) và kernel không được hỗ trợ có thể làm giảm benefit kỳ vọng.

## Batch Sizing có nhận thức về bộ nhớ (memory / 메모리)

Maximum batch không phải mục tiêu cuối. Cần chọn batch cân bằng:

- bộ nhớ (memory / 메모리) headroom;
- thông lượng (throughput / 처리량);
- tail độ trễ (latency / 지연 시간);
- OOM rủi ro (risk / 위험).

Động (dynamic / 동적) tải công việc (workload / 워크로드) cần chừa margin thay vì lấp đầy 100% VRAM.

## OOM thất bại (failure / 실패)

Out-of-memory thường xảy ra vì peak allocation chứ không phải average allocation. Cần profile peak bộ nhớ (memory / 메모리) ở worst-case chuỗi (sequence / 시퀀스) length và batch kích thước (size / 크기).

## Bộ nhớ (memory / 메모리) Leak và Caching

Long-running serving thời gian chạy (runtime / 런타임) có allocator và bộ nhớ đệm (cache / 캐시) nên RSS hoặc VRAM có thể giữ high watermark. Không nên nhầm allocator caching với bộ nhớ (memory / 메모리) leak thật; cần inspect allocation hành vi (behavior / 동작).

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Compute hỏi: cần bao nhiêu phép toán?
Memory hỏi: dữ liệu ở đâu, phải di chuyển bao nhiêu byte và có thể reuse bao nhiêu lần?
```

Trong AI hiện đại, **dữ liệu (data / 데이터) movement cũng là một phần lớn của computation chi phí (cost / 비용)**.

## Những nhầm lẫn thường gặp

### “mô hình (model / 모델) fit VRAM nghĩa là serving ổn”

Không. KV bộ nhớ đệm (cache / 캐시), activation và tính đồng thời (concurrency / 동시성) còn cần thêm bộ nhớ (memory / 메모리).

### “Nhiều VRAM hơn nghĩa là nhanh hơn”

Không. sức chứa (capacity / 용량) và bandwidth là hai đại lượng khác nhau.

### “Unified bộ nhớ (memory / 메모리) loại bỏ transfer bottleneck”

Không. vật lý (physical / 물리적) dữ liệu (data / 데이터) movement vẫn tồn tại.

## Liên kết kiến thức

Xem [GPU Architecture](./02_gpu_architecture.md), [Parallel Computing](./04_parallel_computing.md), [Quantization](../15_ai_engineering/06_quantization.md), [Caching/Batching](../15_ai_engineering/05_caching_and_batching.md).
