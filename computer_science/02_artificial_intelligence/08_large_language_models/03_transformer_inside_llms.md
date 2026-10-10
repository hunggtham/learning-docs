# Transformer bên trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Transformer bên trong large language models**. Route đi từ decoder-only stack → self-attention/MLP blocks → residual stream and normalization → depth/width trade-offs → inference memory and latency, để kiến trúc giải thích được hành vi và chi phí chạy.

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

Decoder-only stack cho biết các block được xếp theo chiều sâu; residual stream giải thích thông tin được giữ và cập nhật xuyên qua từng block. Tiếp theo, ta xem attention trộn thông tin giữa các vị trí như thế nào.

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

Attention cho phép mỗi vị trí chọn lọc tín hiệu từ các vị trí khác trong residual stream. Khi đặt cơ chế này vào hệ thống LLM, số lượng đầu attention và cách dùng chung K/V trở thành điểm cần phân tích tiếp.

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

MHA, GQA và MQA khác nhau chủ yếu ở cách các head dùng chung K/V, nên ảnh hưởng trực tiếp đến bộ nhớ và băng thông khi decode. Ngoài attention, phần feed-forward cũng chiếm một lượng lớn tham số của block.

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

Feed-forward network bổ sung biến đổi độc lập theo từng vị trí sau khi attention đã trộn ngữ cảnh, đồng thời thường chứa phần lớn tham số của block. Để hiểu vai trò của nó sâu hơn, ta xem MLP có thể biểu diễn và truy hồi đặc trưng như thế nào.

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

MLP có thể được xem như nơi biến đổi các đặc trưng đã được trộn, nhưng không nên gán mỗi neuron với một “fact” riêng lẻ. Cách đặt normalization quanh MLP và attention quyết định độ ổn định của toàn bộ stack.

## MLP đang làm gì?

Attention chủ yếu tuyến (route / 경로)/mix thông tin (information / 정보) across đơn vị từ (token / 토큰) positions. MLP biến đổi biểu diễn (representation / 표현) tại từng đơn vị từ (token / 토큰) độc lập theo position nhưng dùng chung (shared / 공유) weights.

Một perspective nghiên cứu xem MLP như associative/key-value-like bộ nhớ (memory / 메모리) cho learned features/facts, nhưng không nên literalize rằng mỗi neuron hay row là một fact. kiến thức (knowledge / 지식) phân tán (distributed / 분산) và có tương tác (interaction / 상호작용) qua many layers.

RMSNorm và pre-norm điều chỉnh độ lớn biểu diễn và đường truyền gradient mà không thay đổi vai trò cơ bản của MLP. Sau normalization, mô hình vẫn cần mã hóa quan hệ vị trí giữa các token; đó là vai trò của RoPE.

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

RoPE đưa thông tin vị trí vào phép tính attention bằng cách xoay biểu diễn truy vấn và khóa theo vị trí. Sau khi các block xử lý xong, mô hình cần chiếu biểu diễn cuối cùng về không gian vocabulary để chọn token tiếp theo.

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

Output projection biến hidden state thành logits trên vocabulary; weight tying có thể dùng chung ma trận với embedding để giảm tham số. Khi triển khai, chi phí của bước này khác đáng kể giữa prefill và decode.

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

Output projection thường được tính trên cả prompt trong prefill và từng token mới trong decode, nhưng hai pha có đặc tính song song và độ trễ khác nhau. Decode dựa nhiều vào KV cache, vốn chỉ là trạng thái phục vụ một lần sinh cụ thể.

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

KV cache lưu các key và value đã tính cho ngữ cảnh hiện tại để tránh tính lại, không phải bộ nhớ dài hạn của mô hình. Vì cache tăng theo độ dài ngữ cảnh, ta cần xem riêng chi phí attention khi context kéo dài.

## KV bộ nhớ đệm (cache / 캐시) không phải mô hình (model / 모델) bộ nhớ (memory / 메모리) dài hạn

KV bộ nhớ đệm (cache / 캐시) là cached intermediate attention trạng thái (state / 상태) của hiện tại (current / 현재) ngữ cảnh (context / 맥락)/yêu cầu (request / 요청). Nó biến mất khi session/yêu cầu (request / 요청) kết thúc trừ khi serving hệ thống (system / 시스템) giữ/reuse.

Nó không cập nhật (update / 업데이트) weights, không phải ngữ nghĩa (semantic / 의미적) bộ nhớ (memory / 메모리) cơ sở dữ liệu (database / 데이터베이스).

Ứng dụng (application / 애플리케이션) “bộ nhớ (memory / 메모리)” cần persist văn bản (text / 텍스트)/structured trạng thái (state / 상태) externally rồi đưa lại ngữ cảnh (context / 맥락)/retrieval.

Độ dài context làm tăng cả lượng KV phải lưu và công việc attention phải xử lý, dù mức tăng cụ thể còn phụ thuộc kiến trúc. FlashAttention tối ưu đường truy cập bộ nhớ cho phép tính này mà không đổi kết quả toán học mục tiêu.

## Ngữ cảnh (context / 맥락) length và attention chi phí (cost / 비용)

Huấn luyện (training / 학습) full attention có score ma trận (matrix / 행렬) roughly `T×T`. Longer ngữ cảnh (context / 맥락) làm attention compute/bộ nhớ (memory / 메모리) tăng quadratic trong vanilla form.

Suy luận (inference / 추론) with KV bộ nhớ đệm (cache / 캐시) avoids recomputing previous states, nhưng per-new-token attention vẫn grows roughly linearly với cached ngữ cảnh (context / 맥락) length, và bộ nhớ đệm (cache / 캐시) bộ nhớ (memory / 메모리) grows linearly.

Long-context mô hình (model / 모델) vì vậy có real các hệ thống (systems / 시스템들) chi phí (cost / 비용) even if API exposes huge ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우).

FlashAttention giảm việc ghi và đọc tensor trung gian bằng cách tính theo các tile phù hợp với bộ nhớ GPU. Đây là tối ưu triển khai cho attention; phần tiếp theo chuyển sang một cách tiết kiệm compute khác là Mixture of Experts.

## FlashAttention

Naive hiện thực (implementation / 구현) materializes large attention ma trận (matrix / 행렬) in high-bandwidth bộ nhớ (memory / 메모리). FlashAttention reorganizes computation thành blocks để reduce bộ nhớ (memory / 메모리) IO and store fewer intermediates, while computing mathematically chính xác (exact / 정확한) attention up to floating-point hành vi (behavior / 동작).

Cốt lõi (core / 핵심) lesson:

> Algorithmic độ phức tạp (complexity / 복잡도) chưa đủ để predict speed; bộ nhớ (memory / 메모리) hierarchy và kernel thiết kế (design / 설계) matter.

This is a direct cầu nối (bridge / 브리지) from AI mathematics to GPU các hệ thống (systems / 시스템들) kỹ thuật (engineering / 엔지니어링).

MoE thay một số MLP dense bằng nhiều expert và một router chọn expert cho từng token. Vì chỉ một phần expert được kích hoạt, cần phân biệt tổng số tham số với số tham số thực sự chạy ở mỗi token.

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

Tổng số tham số quyết định phần lớn dung lượng checkpoint, còn active parameters liên quan trực tiếp hơn đến compute của một token. Quantization tiếp tục thay đổi dung lượng và băng thông, nên cần xem nó tương tác với kiến trúc ra sao.

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

Quantization xấp xỉ các giá trị số trong mô hình để giảm dung lượng và chi phí di chuyển dữ liệu, nhưng mức ảnh hưởng phụ thuộc vào layer và phần cứng. Nhìn tổng thể, mỗi Transformer block có thể được xem như một chương trình học được lặp lại theo chiều sâu.

## Quantization and kiến trúc (architecture / 아키텍처) tương tác (interaction / 상호작용)

Suy luận (inference / 추론) may store weights INT8/INT4 while compute/dequantize into higher precision. Some layers/outliers more sensitive.

Kiến trúc (architecture / 아키텍처) determines quantization hành vi (behavior / 동작): normalization, activation outliers, KV bộ nhớ đệm (cache / 캐시) dtype and expert routing can all matter.

Quantization does not conceptually thay đổi (change / 변경) Transformer hàm (function / 함수) mục tiêu (target / 대상), but approximates numeric thực thi (execution / 실행) to save bộ nhớ (memory / 메모리)/bandwidth.

Mỗi block lặp cùng một kiểu phép biến đổi nhưng dùng tham số riêng ở từng độ sâu, vì vậy biểu diễn được tinh chỉnh qua nhiều bước. Cách nhìn này giúp kiểm tra các ngộ nhận thường gặp về việc LLM “lưu” và “suy nghĩ” như thế nào.

## Transformer khối (block / 블록) as repeated learned program

Even though tầng (layer / 계층) cấu trúc (structure / 구조) repeated, weights usually differ per tầng (layer / 계층). Each tầng (layer / 계층) can refine biểu diễn (representation / 표현) through:

```text
retrieve relevant context via attention
→ transform features via MLP
→ accumulate through residual stream
```

After many layers, final biểu diễn (representation / 표현) has undergone iterative contextual computation.

This is why next-token prediction can involve substantial nội bộ (internal / 내부) computation before one đơn vị từ (token / 토큰) is emitted.

Những ngộ nhận về attention, neuron, tham số và MoE thường xuất hiện khi ta biến một phép ẩn dụ thành khẳng định literal. Mô hình tư duy sau đây gom các cơ chế vừa học thành một chuỗi suy luận có thể áp dụng lại.

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

Mô hình tư duy này nối input token với residual stream, attention, MLP, normalization và output projection, đồng thời giữ rõ ranh giới giữa cơ chế và ẩn dụ. Phần cuối chỉ ra các tài liệu nền để người học tiếp tục đào sâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Residual stream = evolving token state
Attention       = context routing/mixing
MLP/Experts     = feature transformation / nonlinear computation
Norm            = stabilize scale
Position        = encode order/relative distance
Output head     = turn final state into next-token logits
KV cache        = reuse current-context attention states during decode
```

Các liên kết dưới đây đặt bài học vào mạch rộng hơn của LLM: từ token và embedding đến training, inference và evaluation. Nhờ đó, người học có thể quay lại đúng tài liệu khi cần kiểm tra một giả định kỹ thuật.

## Liên kết kiến thức (knowledge connection / 지식 연결)

This chapter ties [Transformer](../06_deep_learning_architectures/05_transformer.md), [Attention](../06_deep_learning_architectures/04_attention.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md) and later [AI Compute & Infrastructure](../17_ai_compute_and_infrastructure/).

Xem tiếp: [Pretraining](./04_pretraining.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
