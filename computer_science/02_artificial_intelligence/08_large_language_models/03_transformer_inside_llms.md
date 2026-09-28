# Transformer bên trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)

> **Mạch đọc:** Đặt **Transformer bên trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Decoder-only ngăn xếp (stack / 스택)** sang **Residual stream như “dùng chung (shared / 공유) working biểu diễn (representation / 표현)”**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Ở tầng (layer / 계층) trước, Transformer đã được giải thích như một kiến trúc (architecture / 아키텍처) gồm attention, feed-forward mạng (network / 네트워크), residual liên kết (connection / 연결) và normalization. Khi kiến trúc (architecture / 아키텍처) đó được quy mô (scale / 규모) thành Large ngôn ngữ (language / 언어) mô hình (model / 모델), cơ chế cơ bản không đổi, nhưng **tỷ lệ giữa các thành phần, cách tổ chức attention, positional encoding, normalization, feed-forward khối (block / 블록), bộ nhớ đệm (cache / 캐시) và parallelism** trở thành những quyết định ảnh hưởng trực tiếp tới chất lượng, tốc độ và chi phí.

Chapter này không lặp lại công thức attention từ đầu. Mục tiêu là nhìn Transformer như một **LLM computation engine**: một đơn vị từ (token / 토큰) đi qua mô hình (model / 모델) như thế nào, parameters nằm ở đâu, ngữ cảnh (context / 맥락) được trộn ra sao, và vì sao suy luận (inference / 추론) hành vi (behavior / 동작) khác huấn luyện (training / 학습) hành vi (behavior / 동작).

Xem nền: [Transformer](../06_deep_learning_architectures/05_transformer.md) và [Attention](../06_deep_learning_architectures/04_attention.md).

## Decoder-only ngăn xếp (stack / 스택)

Một decoder-only LLM thường có luồng (flow / 흐름):

```text
Token IDs
   ↓ embedding lookup
Token vectors + positional mechanism
   ↓
Transformer block 1
   ↓
Transformer block 2
   ↓
...
   ↓
Transformer block L
   ↓ final norm
Hidden state at each position
   ↓ output projection / unembedding
Vocabulary logits
   ↓ softmax / sampling
Next token
```

Mỗi khối (block / 블록) thường có hai computation lớn:

```text
Attention sublayer
Feed-Forward / MLP sublayer
```

và residual đường dẫn (path / 경로) chạy xuyên suốt.

## Residual stream như “dùng chung (shared / 공유) working biểu diễn (representation / 표현)”

Với pre-norm kiến trúc (architecture / 아키텍처):

\[
x' = x + Attention(Norm(x))
\]

\[
x'' = x' + MLP(Norm(x'))
\]

Một cách nghĩ hữu ích là residual stream chứa biểu diễn (representation / 표현) hiện tại của mỗi đơn vị từ (token / 토큰). Attention đọc biểu diễn (representation / 표현) của nhiều positions và ghi một cập nhật (update / 업데이트); MLP đọc từng position và ghi một tính năng (feature / 기능) transformation khác.

Đây là mô hình tư duy (mental model / 사고 모델), không phải claim rằng mô hình (model / 모델) có các “register” symbolic rõ ràng. Hidden thông tin (information / 정보) phân tán qua dimensions, layers và đơn vị từ (token / 토큰) positions.

## Attention trộn thông tin giữa positions

Với hidden states `X`, mỗi tầng (layer / 계층) tạo:

\[
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V
\]

Nhân quả (causal / 인과적) mask đảm bảo đơn vị từ (token / 토큰) tại position `t` chỉ dùng positions `≤t`.

Attention đầu ra (output / 출력):

\[
O=softmax\left(\frac{QK^T}{\sqrt{d_h}}+M\right)V
\]

Điều quan trọng ở LLM quy mô (scale / 규모) không chỉ là công thức. Attention là nơi ngữ cảnh (context / 맥락) length tạo chi phí (cost / 비용) theo chuỗi (sequence / 시퀀스) length và là nơi KV bộ nhớ đệm (cache / 캐시) xuất hiện trong generation.

## Multi-Head, GQA và MQA

Classic multi-head attention dùng số truy vấn (query / 쿼리)/Key/giá trị (value / 값) heads giống nhau. Trong autoregressive serving, keys/values của mọi previous tokens phải được giữ trong KV bộ nhớ đệm (cache / 캐시).

Nếu mô hình (model / 모델) có:

```text
L layers
T cached tokens
Hkv KV heads
Dh head dimension
2 tensors: K and V
```

Bộ nhớ đệm (cache / 캐시) kích thước (size / 크기) roughly proportional:

\[
2LT H_{kv}D_h\times bytes\_per\_element
\]

Do đó hiện đại (modern / 현대적) LLMs thường dùng:

- **MHA**: Q heads = K/V heads;
- **MQA**: nhiều Q heads chia sẻ một K và V head;
- **GQA**: nhiều Q heads nhưng chỉ một số nhóm K/V heads.

GQA là compromise phổ biến: giảm KV bộ nhớ (memory / 메모리)/bandwidth trong khi giữ chất lượng (quality / 품질) gần multi-head attention.

## Feed-Forward mạng (network / 네트워크) chiếm rất nhiều parameters

Một classic FFN:

\[
FFN(x)=W_2\phi(W_1x)
\]

Nếu hidden width `d` và intermediate width `d_ff≈4d`, chỉ hai matrices đã có khoảng:

\[
2d\cdot d_{ff}\approx8d^2
\]

parameters mỗi tầng (layer / 계층).

Hiện đại (modern / 현대적) LLMs thường dùng gated MLP, ví dụ SwiGLU:

\[
FFN(x)=W_3\left(SiLU(W_1x)\odot W_2x\right)
\]

Ba projections tạo multiplicative gating. Intermediate width thường điều chỉnh để parameter/FLOP ngân sách (budget / 예산) phù hợp.

Attention thường được truyền thông nhiều vì dễ hình dung, nhưng FFN/MLP blocks chứa một phần rất lớn parameter và computation của dense LLM.

## MLP đang làm gì?

Attention chủ yếu tuyến (route / 경로)/mix thông tin (information / 정보) across đơn vị từ (token / 토큰) positions. MLP biến đổi biểu diễn (representation / 표현) tại từng đơn vị từ (token / 토큰) độc lập theo position nhưng dùng chung (shared / 공유) weights.

Một perspective nghiên cứu xem MLP như associative/key-value-like bộ nhớ (memory / 메모리) cho learned features/facts, nhưng không nên literalize rằng mỗi neuron hay row là một fact. kiến thức (knowledge / 지식) phân tán (distributed / 분산) và có tương tác (interaction / 상호작용) qua many layers.

## RMSNorm và Pre-Norm

Many hiện đại (modern / 현대적) decoder LLMs dùng RMSNorm:

\[
RMS(x)=\sqrt{\frac1d\sum_i x_i^2+\epsilon}
\]

\[
RMSNorm(x)=g\odot\frac{x}{RMS(x)}
\]

Nó bỏ mean-centering của LayerNorm và giảm computation nhẹ.

Pre-norm đặt norm trước sublayer, giúp độ dốc (gradient / 기울기) đi qua residual định danh (identity / 식별자) đường dẫn (path / 경로) ổn định hơn trong deep stacks.

## Rotary Position Embedding (RoPE)

Transformer attention tự nó không biết đơn vị từ (token / 토큰) thứ tự (order / 순서). RoPE encode position bằng rotation của Q/K components.

Simplified pairwise rotation:

\[
\begin{bmatrix}
x'_{2i}\\x'_{2i+1}
\end{bmatrix}
=
\begin{bmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix}
x_{2i}\\x_{2i+1}
\end{bmatrix}
\]

Angle depends position and frequency.

Key benefit: dot products after rotation encode relative positional differences naturally.

Ngữ cảnh (context / 맥락) extension methods may rescale/interpolate RoPE frequencies, but simply increasing ngữ cảnh (context / 맥락) cấu hình (config / 설정) can degrade position hành vi (behavior / 동작) nếu mô hình (model / 모델) chưa được trained/adapted appropriately.

## Đầu ra (output / 출력) projection và weight tying

Final hidden trạng thái (state / 상태) `h_t` maps to vocabulary logits:

\[
z_t=W_Uh_t+b
\]

với:

\[
W_U\in R^{|V|\times d}
\]

Then:

\[
P(token=k\mid context)=softmax(z_t)_k
\]

Một số các mô hình (models / 모델들) tie đầu vào (input / 입력) embedding và đầu ra (output / 출력) ma trận (matrix / 행렬):

\[
W_U=E
\]

hoặc transpose tùy convention.

Weight tying reduces parameters and creates dùng chung (shared / 공유) lexical hình học (geometry / 기하학), nhưng không phải yêu cầu (requirement / 요구사항) universal.

## Prefill và Decode là hai tải công việc (workload / 워크로드) khác nhau

### Prefill

Mô hình (model / 모델) nhận toàn prompt dài `T` và computes representations cho tất cả positions. ma trận (matrix / 행렬) multiplications lớn, parallelism cao; tải công việc (workload / 워크로드) thường compute-heavy.

### Decode

Sau đó mỗi step chỉ thêm một đơn vị từ (token / 토큰). K/V cũ bộ nhớ đệm (cache / 캐시) lại; mô hình (model / 모델) tính truy vấn (query / 쿼리)/new K/V cho đơn vị từ (token / 토큰) mới rồi attend toàn bộ nhớ đệm (cache / 캐시).

Decode thường memory-bandwidth/latency-sensitive vì mỗi đơn vị từ (token / 토큰) cần đọc large weights + KV bộ nhớ đệm (cache / 캐시) nhưng batch/chuỗi (sequence / 시퀀스) compute nhỏ hơn.

Do đó tối ưu hóa (optimization / 최적화) suy luận (inference / 추론) phải tách:

```text
prefill throughput
vs
decode latency / tokens per second
```

## KV bộ nhớ đệm (cache / 캐시) không phải mô hình (model / 모델) bộ nhớ (memory / 메모리) dài hạn

KV bộ nhớ đệm (cache / 캐시) là cached intermediate attention trạng thái (state / 상태) của hiện tại (current / 현재) ngữ cảnh (context / 맥락)/yêu cầu (request / 요청). Nó biến mất khi session/yêu cầu (request / 요청) kết thúc trừ khi serving hệ thống (system / 시스템) giữ/reuse.

Nó không cập nhật (update / 업데이트) weights, không phải ngữ nghĩa (semantic / 의미적) bộ nhớ (memory / 메모리) cơ sở dữ liệu (database / 데이터베이스).

Ứng dụng (application / 애플리케이션) “bộ nhớ (memory / 메모리)” cần persist văn bản (text / 텍스트)/structured trạng thái (state / 상태) externally rồi đưa lại ngữ cảnh (context / 맥락)/retrieval.

## Ngữ cảnh (context / 맥락) length và attention chi phí (cost / 비용)

Huấn luyện (training / 학습) full attention có score ma trận (matrix / 행렬) roughly `T×T`. Longer ngữ cảnh (context / 맥락) làm attention compute/bộ nhớ (memory / 메모리) tăng quadratic trong vanilla form.

Suy luận (inference / 추론) with KV bộ nhớ đệm (cache / 캐시) avoids recomputing previous states, nhưng per-new-token attention vẫn grows roughly linearly với cached ngữ cảnh (context / 맥락) length, và bộ nhớ đệm (cache / 캐시) bộ nhớ (memory / 메모리) grows linearly.

Long-context mô hình (model / 모델) vì vậy có real các hệ thống (systems / 시스템들) chi phí (cost / 비용) even if API exposes huge ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우).

## FlashAttention

Naive hiện thực (implementation / 구현) materializes large attention ma trận (matrix / 행렬) in high-bandwidth bộ nhớ (memory / 메모리). FlashAttention reorganizes computation thành blocks để reduce bộ nhớ (memory / 메모리) IO and store fewer intermediates, while computing mathematically chính xác (exact / 정확한) attention up to floating-point hành vi (behavior / 동작).

Cốt lõi (core / 핵심) lesson:

> Algorithmic độ phức tạp (complexity / 복잡도) chưa đủ để predict speed; bộ nhớ (memory / 메모리) hierarchy và kernel thiết kế (design / 설계) matter.

This is a direct cầu nối (bridge / 브리지) from AI mathematics to GPU các hệ thống (systems / 시스템들) kỹ thuật (engineering / 엔지니어링).

## Mixture of Experts (MoE) preview

Not every LLM is dense. MoE khối (block / 블록) has multiple expert FFNs and router sends each đơn vị từ (token / 토큰) to subset experts.

Conceptually:

\[
y=\sum_{e\in TopK(router(x))}p_e(x)Expert_e(x)
\]

Total parameters can be huge while only few experts active per đơn vị từ (token / 토큰), reducing active compute relative dense mô hình (model / 모델) of same total parameter count.

Challenges:

- tải (load / 로드) balancing;
- routing instability;
- expert parallel communication;
- bộ nhớ (memory / 메모리) footprint;
- serving độ phức tạp (complexity / 복잡도).

MoE belongs to kiến trúc (architecture / 아키텍처)/compute specialization and will return in hạ tầng (infrastructure / 인프라) discussions.

## Parameter count vs active parameters

For dense mô hình (model / 모델), nearly all tầng (layer / 계층) parameters participate every đơn vị từ (token / 토큰).

For MoE, total parameters ≠ active parameters per đơn vị từ (token / 토큰). Therefore comparing “mô hình (model / 모델) kích thước (size / 크기)” only by total billions can mislead compute comparisons.

Need ask:

```text
total parameters?
active parameters/token?
training tokens?
architecture?
context?
precision?
```

## Quantization and kiến trúc (architecture / 아키텍처) tương tác (interaction / 상호작용)

Suy luận (inference / 추론) may store weights INT8/INT4 while compute/dequantize into higher precision. Some layers/outliers more sensitive.

Kiến trúc (architecture / 아키텍처) determines quantization hành vi (behavior / 동작): normalization, activation outliers, KV bộ nhớ đệm (cache / 캐시) dtype and expert routing can all matter.

Quantization does not conceptually thay đổi (change / 변경) Transformer hàm (function / 함수) mục tiêu (target / 대상), but approximates numeric thực thi (execution / 실행) to save bộ nhớ (memory / 메모리)/bandwidth.

## Transformer khối (block / 블록) as repeated learned program

Even though tầng (layer / 계층) cấu trúc (structure / 구조) repeated, weights usually differ per tầng (layer / 계층). Each tầng (layer / 계층) can refine biểu diễn (representation / 표현) through:

```text
retrieve relevant context via attention
→ transform features via MLP
→ accumulate through residual stream
```

After many layers, final biểu diễn (representation / 표현) has undergone iterative contextual computation.

This is why next-token prediction can involve substantial nội bộ (internal / 내부) computation before one đơn vị từ (token / 토큰) is emitted.

## Dùng chung (common / 공통) Misconceptions

### “LLM parameters chủ yếu nằm trong attention”

MLP/FFN projections often contain larger share of dense khối (block / 블록) parameters.

### “ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) càng lớn thì mô hình (model / 모델) nhớ tốt hơn proportionally”

Cửa sổ (window / 윈도우) only provides addressable đầu vào (input / 입력) sức chứa (capacity / 용량); actual utilization can degrade with distance/noise.

### “KV bộ nhớ đệm (cache / 캐시) là persistent bộ nhớ (memory / 메모리) của LLM”

It is yêu cầu (request / 요청)/context-specific cached attention trạng thái (state / 상태), not learned or durable bộ nhớ (memory / 메모리).

### “Quantization làm mô hình (model / 모델) trở thành kiến trúc (architecture / 아키텍처) khác”

Usually same kiến trúc (architecture / 아키텍처)/hàm (function / 함수) family executed approximately at lower precision; chất lượng (quality / 품질) mất mát (loss / 손실) depends phương thức (method / 메서드).

### “MoE 1T parameters compute như dense 1T mô hình (model / 모델)”

Only subset experts active each đơn vị từ (token / 토큰), though bộ nhớ (memory / 메모리)/communication still substantial.

## Mô hình tư duy (mental model / 사고 모델)

```text
Residual stream = evolving token state
Attention       = context routing/mixing
MLP/Experts     = feature transformation / nonlinear computation
Norm            = stabilize scale
Position        = encode order/relative distance
Output head     = turn final state into next-token logits
KV cache        = reuse current-context attention states during decode
```

## Liên kết kiến thức (knowledge connection / 지식 연결)

This chapter ties [Transformer](../06_deep_learning_architectures/05_transformer.md), [Attention](../06_deep_learning_architectures/04_attention.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md) and later [AI Compute & Infrastructure](../17_ai_compute_and_infrastructure/).

Xem tiếp: [Pretraining](./04_pretraining.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 from language models to llms](./00_from_language_models_to_llms.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
