# Mô hình (model / 모델) Compression: nhìn toàn bộ bài toán giảm chi phí mô hình

> **Mạch đọc:** Đặt **mô hình (model / 모델) Compression: nhìn toàn bộ bài toán giảm chi phí mô hình** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Mục tiêu của Compression** sang **Low-Rank Factorization**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Nén mô hình (model compression / 모델 압축)** là khái niệm bao trùm các kỹ thuật giảm bộ nhớ (memory / 메모리), compute, bandwidth hoặc độ trễ (latency / 지연 시간) trong khi vẫn giữ chất lượng đủ tốt cho triển khai (deployment / 배포) mục tiêu (target / 대상). Quantization, pruning và distillation là ba nhóm lớn, nhưng compression còn bao gồm low-rank factorization, parameter sharing, đơn giản hóa kiến trúc và tối ưu theo thời gian chạy (runtime / 런타임) cụ thể.

Điểm quan trọng là compression phải được đánh giá theo **mục tiêu của toàn hệ thống (system objective)**, không chỉ theo tệp (file / 파일) kích thước (size / 크기).

## Mục tiêu của Compression

Một dự án (project / 프로젝트) có thể muốn giảm:

```text
weight memory
activation memory
KV-cache memory
FLOPs
memory bandwidth
latency
energy
cost/request
startup time
```

Các mục tiêu này không hoàn toàn đồng nhất. Giảm parameter count chưa chắc giảm độ trễ (latency / 지연 시간) nếu tải công việc (workload / 워크로드) vẫn bị giới hạn bởi bandwidth hoặc kernel chưa tối ưu.

## Low-Rank Factorization

Nếu weight ma trận (matrix / 행렬) `W` có thể được xấp xỉ bằng rank thấp:

\[
W\approx AB
\]

với `A∈R^{m×r}`, `B∈R^{r×n}`, `r << min(m,n)`, số parameter giảm từ `mn` xuống `r(m+n)`.

SVD cho trực giác rằng nhiều phép biến đổi có **effective rank** thấp hơn dimension đầy đủ.

Low-rank adaptation như LoRA dùng ý tưởng liên quan, nhưng mục tiêu chính của LoRA là parameter-efficient fine-tuning, không mặc định là triển khai (deployment / 배포) compression.

## Weight Sharing

Nhiều weight có thể dùng chung một giá trị (value / 값) hoặc parameter khối (block / 블록). Cách này giúp giảm lưu trữ (storage / 저장소) nhưng có thể làm tối ưu hóa (optimization / 최적화) khó hơn.

Compression truyền thống có véc-tơ (vector / 벡터) quantization hoặc codebook; một số hiện đại (modern / 현대적) kiến trúc (architecture / 아키텍처) cũng dùng mô-đun (module / 모듈) lặp lại hoặc dùng chung (shared / 공유) parameter.

## Thiết kế lại kiến trúc (architecture / 아키텍처)

Đôi khi cách tốt nhất không phải compress một mô hình lớn sẵn có mà chọn kiến trúc (architecture / 아키텍처) nhỏ hơn ngay từ đầu:

```text
smaller hidden size
fewer layers
smaller vocabulary
specialized encoder
mixture routing
```

Một mô hình nhỏ được thiết kế đúng mục đích có thể tốt hơn một mô hình lớn bị compress quá mạnh.

## Quantization, Pruning và Distillation

Ba kỹ thuật này tác động vào các chiều khác nhau:

```text
Quantization  → ít bit hơn cho mỗi giá trị
Pruning       → ít parameter hoặc structure hoạt động hơn
Distillation  → một hàm xấp xỉ được học với mô hình nhỏ hơn
```

Có thể kết hợp chúng, nhưng lỗi do từng bước cũng có thể cộng dồn.

## Weight Compression và thời gian chạy (runtime / 런타임) bộ nhớ (memory / 메모리)

Weight tệp (file / 파일) nhỏ không bảo đảm thời gian chạy (runtime / 런타임) bộ nhớ (memory / 메모리) nhỏ vì còn:

- activations;
- optimizer trạng thái (state / 상태) nếu huấn luyện (training / 학습);
- KV bộ nhớ đệm (cache / 캐시);
- temporary workspace;
- mô hình (model / 모델) shard hoặc buffer bị duplicate.

Với long-context LLM serving, KV bộ nhớ đệm (cache / 캐시) có thể chiếm bộ nhớ (memory / 메모리) nhiều hơn weights.

## Compression Ratio

\[
Compression\ Ratio=\frac{Original\ kích thước (size / 크기)}{Compressed\ kích thước (size / 크기)}
\]

Tỷ lệ này chỉ phản ánh lưu trữ (storage / 저장소); cần xem thêm chất lượng (quality / 품질), độ trễ (latency / 지연 시간) và chi phí (cost / 비용).

## Pareto Frontier

Compression là một bài toán tối ưu nhiều mục tiêu (multi-objective optimization).

Ta muốn mô hình nằm trên **Pareto frontier** giữa:

```text
quality ↔ latency ↔ memory ↔ cost
```

Một mô hình không Pareto-efficient nếu tồn tại mô hình khác vừa rẻ hơn vừa tốt hơn.

## Benchmark trên đúng Hardware

Kết quả compression phải được benchmark trên hardware và thời gian chạy (runtime / 런타임) mục tiêu. Một INT4 kernel có thể rất nhanh trên GPU này nhưng kém hiệu quả trên CPU hoặc accelerator khác.

Benchmark trong paper không thể thay thế môi trường vận hành (production / 운영 환경) benchmark.

## Đánh giá sau Compression

Evaluation cần kiểm tra:

- chất lượng tác vụ (task / 작업) tổng thể;
- calibration;
- long-tail trường hợp (case / 사례);
- long ngữ cảnh (context / 맥락);
- multilingual hành vi (behavior / 동작);
- structured đầu ra (output / 출력) hoặc công cụ (tool / 도구) calling;
- an toàn (safety / 안전) ràng buộc (constraint / 제약조건);
- độ trễ (latency / 지연 시간) và chi phí (cost / 비용).

## Specialized Small mô hình (model / 모델)

Một mô hình nhỏ chuyên biệt theo lĩnh vực (domain / 도메인) kết hợp retrieval hoặc công cụ (tool / 도구) có thể vượt generic large mô hình (model / 모델) trên narrow tải công việc (workload / 워크로드) với chi phí (cost / 비용) thấp hơn nhiều.

Vì vậy compression không chỉ là bước hậu xử lý sau huấn luyện (training / 학습); nó còn liên quan tới mô hình (model / 모델) selection và hệ thống (system / 시스템) kiến trúc (architecture / 아키텍처).

## Edge triển khai (deployment / 배포)

Thiết bị mobile hoặc embedded có ràng buộc (constraint / 제약조건) mạnh về RAM, power và thermal. Compression khi đó phải xét cùng operator hỗ trợ (support / 지원), hardware acceleration và gói (package / 패키지) kích thước (size / 크기).

## Khi nào không nên Compression?

Nếu suy luận (inference / 추론) volume thấp và kỹ thuật (engineering / 엔지니어링) độ phức tạp (complexity / 복잡도) cao, compression có thể không đáng. Không nên tối ưu trước khi profiling chỉ ra bottleneck thật sự.

## Mô hình tư duy

```text
Compression = giữ lại hàm hữu ích trong khi giảm chi phí vật lý để lưu trữ và thực thi nó
```

## Những nhầm lẫn thường gặp

### “mô hình (model / 모델) tệp (file / 파일) nhỏ hơn nghĩa là hệ thống (system / 시스템) nhanh hơn”

Không nhất thiết. thời gian chạy (runtime / 런타임) bottleneck mới quyết định hiệu năng (performance / 성능) thực tế.

### “Compression chỉ là quantization”

Không. Quantization chỉ là một family trong nhiều kỹ thuật compression.

### “Compress một lần là xong”

Không. mô hình (model / 모델), dữ liệu (data / 데이터) và thời gian chạy (runtime / 런타임) thay đổi có thể làm sự đánh đổi (trade-off / 트레이드오프) thay đổi, vì vậy cần đánh giá lại.

## Liên kết kiến thức

Xem [Quantization](./06_quantization.md), [Pruning and Distillation](./07_pruning_and_distillation.md), [Latency, Throughput and Cost](./09_latency_throughput_and_cost.md) và [AI Compute](../17_ai_compute_and_infrastructure/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 ai engineering](./00_ai_engineering.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
