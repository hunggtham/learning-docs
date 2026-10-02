# Quantization trong AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Quantization trong AI**. Route đi từ floating-point values → scale/zero-point mapping → symmetric/asymmetric schemes → calibration/quantization-aware training → accuracy–memory–latency trade-offs, để giảm bit vẫn giữ task quality.

**Lượng tử hóa (quantization / 양자화)** làm giảm độ chính xác số dùng để biểu diễn weights, activations hoặc KV bộ nhớ đệm (cache / 캐시). Mục tiêu là giảm bộ nhớ (memory / 메모리), bandwidth, độ trễ (latency / 지연 시간) và chi phí (cost / 비용) trong khi vẫn giữ chất lượng ở mức chấp nhận được.

Một mô hình được huấn luyện bằng FP32/BF16 không nhất thiết phải infer ở cùng precision. Nhiều tải công việc (workload / 워크로드) có thể chạy bằng FP16, INT8, INT4 hoặc mixed precision.

## Từ số thực tới các mức rời rạc

Một quantizer đơn giản ánh xạ giá trị thực `x` sang số nguyên `q`:

\[
q=round(x/s)+z
\]

trong đó `s` là quy mô (scale / 규모) và `z` là zero-point.

Dequantization xấp xỉ:

\[
\hat{x}=s(q-z)
\]

Sai số:

\[
e=x-\hat{x}
\]

được gọi là **sai số lượng tử hóa (quantization error)**.

> **Chuyển mạch:** Trong **Quantization trong AI**, **Symmetric và Asymmetric Quantization** tiếp nhận điểm tựa từ **Từ số thực tới các mức rời rạc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Per-Tensor, Per-Channel và Per-Group** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Symmetric và Asymmetric Quantization

Quantization đối xứng (symmetric) thường dùng zero-point bằng 0 và phạm vi (range / 범위) cân quanh 0. Cách này đơn giản hơn cho hardware hiện thực (implementation / 구현).

Quantization bất đối xứng (asymmetric) cho phép phạm vi (range / 범위) lệch, hữu ích khi phân phối (distribution / 분포) không đối xứng nhưng siêu dữ liệu (metadata / 메타데이터) và phép tính phức tạp hơn.

> **Chuyển mạch:** Ở chặng này của **Quantization trong AI**, **Per-Tensor, Per-Channel và Per-Group** tiếp nhận điểm tựa từ **Symmetric và Asymmetric Quantization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PTQ và QAT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Per-Tensor, Per-Channel và Per-Group

Dùng một quy mô (scale / 규모) cho cả tensor thì đơn giản nhưng khá thô.

Per-channel dùng quy mô (scale / 규모) riêng theo channel đầu vào hoặc đầu ra, thường giữ accuracy tốt hơn.

LLM quantization thường dùng **group-wise quantization**, trong đó mỗi nhóm weights có quy mô (scale / 규모) riêng để cân bằng giữa siêu dữ liệu (metadata / 메타데이터) chi phí (cost / 비용) và fidelity.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quantization trong AI**, **PTQ và QAT** tiếp nhận điểm tựa từ **Per-Tensor, Per-Channel và Per-Group** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weight-Only Quantization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PTQ và QAT

**Post-Training Quantization (PTQ)** lượng tử hóa sau khi huấn luyện (training / 학습) hoàn tất. Cách này nhanh, rẻ và thường không cần retrain nhiều.

**Quantization-Aware huấn luyện (training / 학습) (QAT)** mô phỏng quantization ngay trong huấn luyện (training / 학습) để mô hình thích nghi với quantization noise. Chi phí cao hơn nhưng có thể giữ chất lượng tốt hơn ở precision thấp.

> **Chuyển mạch:** Trong **Quantization trong AI**, **Weight-Only Quantization** tiếp nhận điểm tựa từ **PTQ và QAT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Activation Quantization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weight-Only Quantization

LLM suy luận (inference / 추론) thường bị giới hạn bởi bộ nhớ (memory / 메모리) bandwidth. Quantize weights giúp:

```text
model chiếm ít memory hơn
memory transfer nhanh hơn
nhiều model hoặc request fit trên cùng GPU hơn
```

Activation vẫn có thể giữ ở BF16 hoặc FP16.

> **Chuyển mạch:** Ở chặng này của **Quantization trong AI**, **Activation Quantization** tiếp nhận điểm tựa từ **Weight-Only Quantization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Outlier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Activation Quantization

Activation phân phối (distribution / 분포) thay đổi theo đầu vào (input / 입력) và thường có outlier. Vì vậy quantize activation khó hơn quantize weights.

Calibration dataset thường được dùng để ước lượng phạm vi (range / 범위) và quy mô (scale / 규모) phù hợp.

Nếu calibration dữ liệu (data / 데이터) không đại diện cho môi trường vận hành (production / 운영 환경) tải công việc (workload / 워크로드), chất lượng thực tế có thể giảm mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quantization trong AI**, **Outlier** tiếp nhận điểm tựa từ **Activation Quantization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **KV bộ nhớ đệm (cache / 캐시) Quantization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Outlier

Một số channel có magnitude lớn bất thường. Nếu dùng chung một quy mô (scale / 규모), các giá trị nhỏ còn lại sẽ có độ phân giải kém.

Các cách xử lý gồm:

- giữ outlier channel ở precision cao;
- rescale channel;
- dùng per-channel hoặc group quantization.

> **Chuyển mạch:** Trong **Quantization trong AI**, **KV bộ nhớ đệm (cache / 캐시) Quantization** tiếp nhận điểm tựa từ **Outlier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác về bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KV bộ nhớ đệm (cache / 캐시) Quantization

LLM có long ngữ cảnh (context / 맥락) có KV bộ nhớ đệm (cache / 캐시) rất lớn. Quantize KV bộ nhớ đệm (cache / 캐시) giúp tăng tính đồng thời (concurrency / 동시성) nhưng có thể làm giảm chất lượng ở long-context tác vụ (task / 작업).

Đây là sự đánh đổi (trade-off / 트레이드오프) ở cấp hệ thống, không chỉ là bài toán nén weights.

> **Chuyển mạch:** Ở chặng này của **Quantization trong AI**, **Trực giác về bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **KV bộ nhớ đệm (cache / 캐시) Quantization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quantization không tự động làm mô hình (model / 모델) nhanh hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác về bộ nhớ (memory / 메모리)

Với mô hình có `N` parameter:

```text
FP32 ≈ 4N byte
FP16/BF16 ≈ 2N byte
INT8 ≈ 1N byte
INT4 ≈ 0.5N byte
```

Thực tế còn có quy mô (scale / 규모), siêu dữ liệu (metadata / 메타데이터) và thời gian chạy (runtime / 런타임) buffer nên con số không hoàn toàn chính xác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quantization trong AI**, **Quantization không tự động làm mô hình (model / 모델) nhanh hơn** tiếp nhận điểm tựa từ **Trực giác về bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đánh giá chất lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quantization không tự động làm mô hình (model / 모델) nhanh hơn

Nếu hardware hoặc kernel không hỗ trợ low-precision thao tác (operation / 연산) hiệu quả, mô hình (model / 모델) nhỏ hơn nhưng độ trễ (latency / 지연 시간) có thể không cải thiện đáng kể.

Speedup phụ thuộc vào:

```text
hardware
kernel implementation
batch size
memory bottleneck hay compute bottleneck
quantize/dequantize overhead
```

> **Chuyển mạch:** Trong **Quantization trong AI**, **Đánh giá chất lượng** tiếp nhận điểm tựa từ **Quantization không tự động làm mô hình (model / 모델) nhanh hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mixed Precision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đánh giá chất lượng

Không nên chỉ so perplexity. Cần task-level evaluation, long-context kiểm thử (test / 테스트), tool-use/output-format kiểm thử (test / 테스트) và an toàn (safety / 안전) regression kiểm thử (test / 테스트).

Một mức giảm nhỏ ở chỉ số (metric / 지표) trung bình vẫn có thể che thất bại (failure / 실패) nghiêm trọng ở một năng lực (capability / 역량) hiếm nhưng quan trọng.

> **Chuyển mạch:** Ở chặng này của **Quantization trong AI**, **Mixed Precision** tiếp nhận điểm tựa từ **Đánh giá chất lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quantization trong huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mixed Precision

Không cần mọi tầng (layer / 계층) cùng precision. Thành phần nhạy số có thể giữ precision cao hơn.

Mixed precision là một thỏa hiệp kỹ thuật giữa bộ nhớ (memory / 메모리), speed và numerical fidelity.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quantization trong AI**, **Quantization trong huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **Mixed Precision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quantization trong huấn luyện (training / 학습)

Low-precision huấn luyện (training / 학습) khác với suy luận (inference / 추론) quantization. BF16/FP16 huấn luyện (training / 학습) thường cần độ dốc (gradient / 기울기) scaling hoặc optimizer trạng thái (state / 상태) ổn định; một số optimizer trạng thái (state / 상태) vẫn được giữ ở precision cao.

> **Chuyển mạch:** Trong **Quantization trong AI**, **Mô hình tư duy** gom các mảnh từ **Quantization trong huấn luyện (training / 학습)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Quantization = nén cách biểu diễn số, không trực tiếp thay đổi cấu trúc ngữ nghĩa của model
```

Ta thay cách biểu diễn parameter và activation, không chủ động thay kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Ở chặng này của **Quantization trong AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “INT4 nghĩa là mô hình (model / 모델) nhỏ đúng 4 lần so với FP16”

Không hoàn toàn. siêu dữ liệu (metadata / 메타데이터), quy mô (scale / 규모) và thời gian chạy (runtime / 런타임) buffer làm mức giảm thực tế khác lý thuyết.

### “mô hình (model / 모델) đã quantize luôn chạy nhanh hơn”

Không. Chỉ nhanh hơn khi thời gian chạy (runtime / 런타임) và hardware tận dụng low precision hiệu quả.

### “Benchmark accuracy không đổi nghĩa là không có regression”

Không. thất bại (failure / 실패) theo năng lực (capability / 역량) cụ thể vẫn có thể xuất hiện ngoài chỉ số (metric / 지표) trung bình.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quantization trong AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Quantization nối [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md), [Model Serving](./03_model_serving.md), [Latency, Throughput and Cost](./09_latency_throughput_and_cost.md) và [Compute Infrastructure](../17_ai_compute_and_infrastructure/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
