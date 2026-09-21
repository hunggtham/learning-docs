# Quantization trong AI

**Lượng tử hóa (quantization / 양자화)** làm giảm độ chính xác số dùng để biểu diễn weights, activations hoặc KV cache. Mục tiêu là giảm memory, bandwidth, latency và cost trong khi vẫn giữ chất lượng ở mức chấp nhận được.

Một mô hình được huấn luyện bằng FP32/BF16 không nhất thiết phải infer ở cùng precision. Nhiều workload có thể chạy bằng FP16, INT8, INT4 hoặc mixed precision.

## Từ số thực tới các mức rời rạc

Một quantizer đơn giản ánh xạ giá trị thực `x` sang số nguyên `q`:

\[
q=round(x/s)+z
\]

trong đó `s` là scale và `z` là zero-point.

Dequantization xấp xỉ:

\[
\hat{x}=s(q-z)
\]

Sai số:

\[
e=x-\hat{x}
\]

được gọi là **sai số lượng tử hóa (quantization error)**.

## Symmetric và Asymmetric Quantization

Quantization đối xứng (symmetric) thường dùng zero-point bằng 0 và range cân quanh 0. Cách này đơn giản hơn cho hardware implementation.

Quantization bất đối xứng (asymmetric) cho phép range lệch, hữu ích khi distribution không đối xứng nhưng metadata và phép tính phức tạp hơn.

## Per-Tensor, Per-Channel và Per-Group

Dùng một scale cho cả tensor thì đơn giản nhưng khá thô.

Per-channel dùng scale riêng theo channel đầu vào hoặc đầu ra, thường giữ accuracy tốt hơn.

LLM quantization thường dùng **group-wise quantization**, trong đó mỗi nhóm weights có scale riêng để cân bằng giữa metadata cost và fidelity.

## PTQ và QAT

**Post-Training Quantization (PTQ)** lượng tử hóa sau khi training hoàn tất. Cách này nhanh, rẻ và thường không cần retrain nhiều.

**Quantization-Aware Training (QAT)** mô phỏng quantization ngay trong training để mô hình thích nghi với quantization noise. Chi phí cao hơn nhưng có thể giữ chất lượng tốt hơn ở precision thấp.

## Weight-Only Quantization

LLM inference thường bị giới hạn bởi memory bandwidth. Quantize weights giúp:

```text
model chiếm ít memory hơn
memory transfer nhanh hơn
nhiều model hoặc request fit trên cùng GPU hơn
```

Activation vẫn có thể giữ ở BF16 hoặc FP16.

## Activation Quantization

Activation distribution thay đổi theo input và thường có outlier. Vì vậy quantize activation khó hơn quantize weights.

Calibration dataset thường được dùng để ước lượng range và scale phù hợp.

Nếu calibration data không đại diện cho production workload, chất lượng thực tế có thể giảm mạnh.

## Outlier

Một số channel có magnitude lớn bất thường. Nếu dùng chung một scale, các giá trị nhỏ còn lại sẽ có độ phân giải kém.

Các cách xử lý gồm:

- giữ outlier channel ở precision cao;
- rescale channel;
- dùng per-channel hoặc group quantization.

## KV Cache Quantization

LLM có long context có KV cache rất lớn. Quantize KV cache giúp tăng concurrency nhưng có thể làm giảm chất lượng ở long-context task.

Đây là trade-off ở cấp hệ thống, không chỉ là bài toán nén weights.

## Trực giác về Memory

Với mô hình có `N` parameter:

```text
FP32 ≈ 4N byte
FP16/BF16 ≈ 2N byte
INT8 ≈ 1N byte
INT4 ≈ 0.5N byte
```

Thực tế còn có scale, metadata và runtime buffer nên con số không hoàn toàn chính xác.

## Quantization không tự động làm model nhanh hơn

Nếu hardware hoặc kernel không hỗ trợ low-precision operation hiệu quả, model nhỏ hơn nhưng latency có thể không cải thiện đáng kể.

Speedup phụ thuộc vào:

```text
hardware
kernel implementation
batch size
memory bottleneck hay compute bottleneck
quantize/dequantize overhead
```

## Đánh giá chất lượng

Không nên chỉ so perplexity. Cần task-level evaluation, long-context test, tool-use/output-format test và safety regression test.

Một mức giảm nhỏ ở metric trung bình vẫn có thể che failure nghiêm trọng ở một capability hiếm nhưng quan trọng.

## Mixed Precision

Không cần mọi layer cùng precision. Thành phần nhạy số có thể giữ precision cao hơn.

Mixed precision là một thỏa hiệp kỹ thuật giữa memory, speed và numerical fidelity.

## Quantization trong Training

Low-precision training khác với inference quantization. BF16/FP16 training thường cần gradient scaling hoặc optimizer state ổn định; một số optimizer state vẫn được giữ ở precision cao.

## Mô hình tư duy

```text
Quantization = nén cách biểu diễn số, không trực tiếp thay đổi cấu trúc ngữ nghĩa của model
```

Ta thay cách biểu diễn parameter và activation, không chủ động thay architecture.

## Những nhầm lẫn thường gặp

### “INT4 nghĩa là model nhỏ đúng 4 lần so với FP16”

Không hoàn toàn. Metadata, scale và runtime buffer làm mức giảm thực tế khác lý thuyết.

### “Model đã quantize luôn chạy nhanh hơn”

Không. Chỉ nhanh hơn khi runtime và hardware tận dụng low precision hiệu quả.

### “Benchmark accuracy không đổi nghĩa là không có regression”

Không. Failure theo capability cụ thể vẫn có thể xuất hiện ngoài metric trung bình.

## Liên kết kiến thức

Quantization nối [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md), [Model Serving](./03_model_serving.md), [Latency, Throughput and Cost](./09_latency_throughput_and_cost.md) và [Compute Infrastructure](../17_ai_compute_and_infrastructure/README.md).