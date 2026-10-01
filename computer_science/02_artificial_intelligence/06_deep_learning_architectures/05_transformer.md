# Transformer: Attention + Residual Computation ở quy mô lớn

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Transformer: Attention + Residual Computation ở quy mô lớn**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Đầu vào (input / 입력) biểu diễn (representation / 표현)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Cốt lõi (core / 핵심) Transformer khối (block / 블록)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Transformer (트랜스포머) không chỉ là “mô hình (model / 모델) dùng attention”. Nó là một kiến trúc (architecture / 아키텍처) tổ chức computation thành repeated blocks gồm attention, feed-forward transformation, residual connections và normalization, cho phép chuỗi (sequence / 시퀀스) positions xử lý song song trong huấn luyện (training / 학습) và long-range interactions ngắn đường dẫn (path / 경로) hơn RNN.

Transformer là nền của BERT, GPT, T5, Vision Transformer và phần lớn hiện đại (modern / 현대적) foundation các mô hình (models / 모델들), nên cần hiểu khối (block / 블록) ở mức tensor/cơ chế (mechanism / 메커니즘) chứ không chỉ hình minh họa.

## Đầu vào (input / 입력) biểu diễn (representation / 표현)

Đơn vị từ (token / 토큰) IDs được lookup embedding ma trận (matrix / 행렬):

\[
E\in R^{|V|\times d_{mô hình (model / 모델)}}
\]

Đơn vị từ (token / 토큰) `i`:

\[
x_i=E[token_i]
\]

Sau đó thêm/encode positional thông tin (information / 정보).

Hidden tensor:

\[
X\in R^{B\times T\times d_{mô hình (model / 모델)}}
\]

> **Chuyển mạch:** Input representation đi qua transformer block gồm attention, feed-forward và residual/norm; self-attention là cơ chế trộn thông tin giữa các vị trí.

## Cốt lõi (core / 핵심) Transformer khối (block / 블록)

Một simplified pre-norm khối (block / 블록):

\[
H'=H+Attention(Norm(H))
\]

\[
H''=H'+FFN(Norm(H'))
\]

Lặp `L` layers.

Hai sublayers chính:

1. Attention — mix thông tin (information / 정보) across positions.
2. Feed-Forward mạng (network / 네트워크) — transform each position independently in tính năng (feature / 기능) dimension.

Residual stream carries biểu diễn (representation / 표현) through ngăn xếp (stack / 스택).

> **Chuyển mạch:** Ở chặng này của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Self-Attention Sub-layer** tiếp nhận điểm tựa từ **Cốt lõi (core / 핵심) Transformer khối (block / 블록)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Feed-Forward mạng (network / 네트워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Self-Attention Sub-layer

Given normalized hidden trạng thái (state / 상태):

\[
Q=XW_Q,
K=XW_K,
V=XW_V
\]

then:

\[
A=softmax\left(\frac{QK^T}{\sqrt{d_k}}+M\right)
\]

\[
O=AVW_O
\]

`M` is mask/độ lệch (bias / 편향).

Attention mixes tokens; without it each đơn vị từ (token / 토큰)'s computation would stay cục bộ (local / 로컬) to own position in tiêu chuẩn (standard / 표준) FFN.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Feed-Forward mạng (network / 네트워크)** tiếp nhận điểm tựa từ **Self-Attention Sub-layer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Residual Stream** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Feed-Forward mạng (network / 네트워크)

Classic Transformer FFN:

\[
FFN(x)=W_2\phi(W_1x+b_1)+b_2
\]

applied independently to each đơn vị từ (token / 토큰) position with dùng chung (shared / 공유) weights.

Typically hidden expansion:

\[
d_{ff}\approx4d_{mô hình (model / 모델)}
\]

classic thiết kế (design / 설계), though hiện đại (modern / 현대적) gated FFNs/SwiGLU use different ratios.

Attention mixes **across chuỗi (sequence / 시퀀스)**; FFN mixes **across tính năng (feature / 기능) dimensions**.

> **Chuyển mạch:** Trong **Transformer: Attention + Residual Computation ở quy mô lớn**, **Residual Stream** tiếp nhận điểm tựa từ **Feed-Forward mạng (network / 네트워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LayerNorm / RMSNorm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Residual Stream

Residual addition:

\[
x\leftarrow x+F(x)
\]

means sublayer writes an cập nhật (update / 업데이트) into dùng chung (shared / 공유) residual biểu diễn (representation / 표현) rather than replacing it completely.

This improves độ dốc (gradient / 기울기) luồng (flow / 흐름) and supports composition of many layers.

A useful mechanistic mô hình tư duy (mental model / 사고 모델) is “residual stream as communication bus”: attention/MLP blocks read from and ghi (write / 쓰기) transformations back into stream. Đây là lớp trừu tượng (abstraction / 추상화) hữu ích, không phải literal software bus.

> **Chuyển mạch:** Ở chặng này của **Transformer: Attention + Residual Computation ở quy mô lớn**, **LayerNorm / RMSNorm** tiếp nhận điểm tựa từ **Residual Stream** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Encoder Transformer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LayerNorm / RMSNorm

Pre-Norm hiện đại (modern / 현대적) mẫu (pattern / 패턴):

```text
x
├───────────────┐
↓ Norm          │
↓ Attention     │
└→ + residual ──┘
↓
├───────────────┐
↓ Norm          │
↓ MLP           │
└→ + residual ──┘
```

Pre-norm usually easier optimize deep stacks because định danh (identity / 식별자) residual đường dẫn (path / 경로) remains clean.

Many LLMs use RMSNorm instead of LayerNorm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Encoder Transformer** tiếp nhận điểm tựa từ **LayerNorm / RMSNorm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decoder Transformer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Encoder Transformer

Encoder self-attention is usually bidirectional: every non-masked đơn vị từ (token / 토큰) can attend every other.

Good for biểu diễn (representation / 표현)/understanding tasks.

BERT-style masked-language-model pretraining uses encoder ngăn xếp (stack / 스택).

> **Chuyển mạch:** Trong **Transformer: Attention + Residual Computation ở quy mô lớn**, **Decoder Transformer** tiếp nhận điểm tựa từ **Encoder Transformer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Encoder–Decoder Transformer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decoder Transformer

Decoder-only self-attention uses nhân quả (causal / 인과적) mask:

\[
M_{ij}=-\infty\quad j>i
\]

so position `i` cannot see future tokens.

GPT-style autoregressive mô hình (model / 모델) trains:

\[
P(x_{1:T})=\prod_tP(x_t\mid x_{<t})
\]

All positions can still be processed parallel during huấn luyện (training / 학습) because mục tiêu (target / 대상) chuỗi (sequence / 시퀀스) known and mask enforces causality.

> **Chuyển mạch:** Ở chặng này của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Encoder–Decoder Transformer** tiếp nhận điểm tựa từ **Decoder Transformer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Head Dimensions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Encoder–Decoder Transformer

Encoder builds nguồn (source / 소스) representations bidirectionally.

Decoder khối (block / 블록) contains:

1. nhân quả (causal / 인과적) self-attention;
2. cross-attention over encoder đầu ra (output / 출력);
3. FFN.

Suitable translation/summarization and conditional generation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Multi-Head Dimensions** tiếp nhận điểm tựa từ **Encoder–Decoder Transformer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Positional Encoding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Head Dimensions

If:

\[
d_{mô hình (model / 모델)}=4096,
\quad h=32
\]

then classic head dimension:

\[
d_{head}=128
\]

Q/K/V projected then reshape:

```text
[B, T, D]
→ [B, T, H, Dh]
→ transpose to [B, H, T, Dh]
```

Shape lập luận (reasoning / 추론) is trọng yếu (critical / 중요) for hiện thực (implementation / 구현)/suy luận (inference / 추론) các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Trong **Transformer: Attention + Residual Computation ở quy mô lớn**, **Positional Encoding** tiếp nhận điểm tựa từ **Multi-Head Dimensions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parameter Count Roughly Comes From Where?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Positional Encoding

Original Transformer used sinusoidal:

\[
PE(pos,2i)=\sin(pos/10000^{2i/d})
\]

\[
PE(pos,2i+1)=\cos(pos/10000^{2i/d})
\]

Hiện đại (modern / 현대적) LLMs often use RoPE or relative mechanisms.

Position scheme influences ngữ cảnh (context / 맥락) extension/extrapolation. Extending max ngữ cảnh (context / 맥락) beyond huấn luyện (training / 학습) length is not trivial just changing cấu hình (config / 설정) number.

> **Chuyển mạch:** Ở chặng này của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Parameter Count Roughly Comes From Where?** tiếp nhận điểm tựa từ **Positional Encoding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weight Tying** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parameter Count Roughly Comes From Where?

For decoder tầng (layer / 계층) ignoring biases/norm:

Attention projections roughly:

\[
4d^2
\]

(Q,K,V,O; less with GQA/MQA for K/V).

FFN often roughly:

\[
2d\,d_{ff}
\]

or three matrices for gated FFN.

In many LLMs FFN parameters exceed attention parameters.

Embeddings/đầu ra (output / 출력) head also significant, possibly weight-tied.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Weight Tying** tiếp nhận điểm tựa từ **Parameter Count Roughly Comes From Where?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Computational độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weight Tying

Đầu vào (input / 입력) embedding and đầu ra (output / 출력) unembedding ma trận (matrix / 행렬) may share parameters:

\[
W_{out}=E^T
\]

This reduces parameter count and connects đầu vào (input / 입력)/đầu ra (output / 출력) đơn vị từ (token / 토큰) hình học (geometry / 기하학).

Not universal but dùng chung (common / 공통).

> **Chuyển mạch:** Trong **Transformer: Attention + Residual Computation ở quy mô lớn**, **Computational độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **Weight Tying** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Huấn luyện (training / 학습) Parallelism vs Generation Seriality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Computational độ phức tạp (complexity / 복잡도)

Self-attention roughly:

\[
O(T^2d)
\]

FFN:

\[
O(Td^2)
\]

Depending `T` vs `d`, different thành phần (component / 컴포넌트) dominates.

For long ngữ cảnh (context / 맥락), attention quadratic becomes major. For short ngữ cảnh (context / 맥락) and huge `d`, MLP/projections may dominate FLOPs.

> **Chuyển mạch:** Ở chặng này của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Huấn luyện (training / 학습) Parallelism vs Generation Seriality** tiếp nhận điểm tựa từ **Computational độ phức tạp (complexity / 복잡도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Huấn luyện (training / 학습) Parallelism vs Generation Seriality

Huấn luyện (training / 학습): entire chuỗi (sequence / 시퀀스) positions processed parallel under nhân quả (causal / 인과적) mask.

Generation: đơn vị từ (token / 토큰) `t+1` cannot compute until đơn vị từ (token / 토큰) `t` selected. This sequential phụ thuộc (dependency / 의존성) limits độ trễ (latency / 지연 시간).

KV bộ nhớ đệm (cache / 캐시) avoids recompute past attention K/V, nhưng generation remains autoregressive serial at đơn vị từ (token / 토큰) mức (level / 수준).

Speculative decoding tries generate candidate tokens with smaller mô hình (model / 모델) then verify in batches, improving thông lượng (throughput / 처리량) without changing mục tiêu (target / 대상) phân phối (distribution / 분포) under proper thuật toán (algorithm / 알고리즘).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우)** tiếp nhận điểm tựa từ **Huấn luyện (training / 학습) Parallelism vs Generation Seriality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transformer as Set/Graph-like tương tác (interaction / 상호작용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우)

Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) limits tokens mô hình (model / 모델) can tiến trình (process / 프로세스) in one yêu cầu (request / 요청)/huấn luyện (training / 학습) segment.

Longer ngữ cảnh (context / 맥락) increases:

- attention/bộ nhớ đệm (cache / 캐시) bộ nhớ (memory / 메모리);
- độ trễ (latency / 지연 시간);
- dữ liệu (data / 데이터) requirements to learn use long-range positions.

“Supports 1M tokens” does not imply mô hình (model / 모델) reasons equally well across 1M tokens. Effective ngữ cảnh (context / 맥락) utilization requires evaluation.

> **Chuyển mạch:** Trong **Transformer: Attention + Residual Computation ở quy mô lớn**, **Transformer as Set/Graph-like tương tác (interaction / 상호작용)** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Why Transformer Scales Well** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transformer as Set/Graph-like tương tác (interaction / 상호작용)

Ignoring positions, self-attention is permutation-equivariant and resembles message passing on fully connected đồ thị (graph / 그래프).

Position encoding gives chuỗi (sequence / 시퀀스) cấu trúc (structure / 구조). This explains why Transformer adapts to images (patch tokens), audio, proteins, molecules and multimodal tokens.

Kiến trúc (architecture / 아키텍처) only needs items represented as tokens/elements plus relational/positional thông tin (information / 정보).

> **Chuyển mạch:** Ở chặng này của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Why Transformer Scales Well** tiếp nhận điểm tựa từ **Transformer as Set/Graph-like tương tác (interaction / 상호작용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Limitations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why Transformer Scales Well

Several factors align:

- ma trận (matrix / 행렬) multiplications map well to GPU/TPU;
- huấn luyện (training / 학습) chuỗi (sequence / 시퀀스) positions parallel;
- residual/norm stable deep stacking;
- attention handles flexible ngữ cảnh (context / 맥락);
- same kiến trúc (architecture / 아키텍처) works across modalities/tasks;
- self-supervised objectives provide huge dữ liệu (data / 데이터).

Transformer success is kiến trúc (architecture / 아키텍처) + dữ liệu (data / 데이터) + compute + tối ưu hóa (optimization / 최적화) + các hệ thống (systems / 시스템들) co-design.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Why Transformer Scales Well** đã nêu tiêu chí phân biệt, còn **Limitations** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Transformer vs RNN** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Limitations

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

- quadratic attention at long sequences;
- autoregressive decoding độ trễ (latency / 지연 시간);
- huge bộ nhớ (memory / 메모리)/compute requirements;
- learned statistical hành vi (behavior / 동작) without built-in factual xác minh (verification / 확인);
- finite ngữ cảnh (context / 맥락) and retrieval limitations;
- opaque phân tán (distributed / 분산) representations.

These motivate efficient attention, state-space các mô hình (models / 모델들), RAG, tools and system-level xác minh (verification / 확인).

> **Chuyển mạch:** Trong **Transformer: Attention + Residual Computation ở quy mô lớn**, **Limitations** đã nêu tiêu chí phân biệt, còn **Transformer vs RNN** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Transformer vs CNN** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transformer vs RNN

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Property | RNN/LSTM | Transformer |
|---|---|---|
| huấn luyện (training / 학습) position parallelism | thấp | cao |
| Long-range đường dẫn (path / 경로) | nhiều recurrent steps | direct attention đường dẫn (path / 경로) |
| trạng thái (state / 상태) at suy luận (inference / 추론) | compact recurrent trạng thái (state / 상태) | KV bộ nhớ đệm (cache / 캐시) grows with ngữ cảnh (context / 맥락) |
| Vanilla long-context compute | tuyến tính (linear / 선형) per recurrent step | quadratic full attention huấn luyện (training / 학습) |
| Streaming naturalness | cao | needs caching/chunking |

Không mô hình (model / 모델) universally superior under every triển khai (deployment / 배포) ràng buộc (constraint / 제약조건).

> **Chuyển mạch:** Ở chặng này của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Transformer vs CNN** tiếp nhận điểm tựa từ **Transformer vs RNN** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transformer vs CNN

CNN hardcodes locality/translation cấu trúc (structure / 구조). Transformer can learn toàn cục (global / 전역) pairwise relations but weaker prior, often needs larger dữ liệu (data / 데이터)/pretraining.

Vision architectures increasingly mix both ideas.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transformer: Attention + Residual Computation ở quy mô lớn**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Transformer vs CNN** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Residual stream holds token representations
Attention  → tokens exchange information
MLP        → each token transforms features internally
Norm       → stabilize scale
Residual   → preserve/accumulate information & gradients
Repeat many layers
```

> **Chuyển mạch:** Trong **Transformer: Attention + Residual Computation ở quy mô lớn**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Transformer = Attention”

Attention trọng yếu (critical / 중요) but MLP, residual, normalization, positions and huấn luyện (training / 학습) mục tiêu (objective / 목표) equally necessary kiến trúc (architecture / 아키텍처) components.

### “Attention lets mô hình (model / 모델) see infinite lịch sử (history / 이력)”

Only within ngữ cảnh (context / 맥락)/bộ nhớ đệm (cache / 캐시) cửa sổ (window / 윈도우) and compute các ràng buộc (constraints / 제약조건들).

### “Decoder-only mô hình (model / 모델) has no encoder so it cannot understand đầu vào (input / 입력)”

Same nhân quả (causal / 인과적) ngăn xếp (stack / 스택) transforms prompt tokens into contextual representations before predicting continuation.

### “More ngữ cảnh (context / 맥락) always improves answer”

Irrelevant/noisy ngữ cảnh (context / 맥락) can degrade hiệu năng (performance / 성능); retrieval/ngữ cảnh (context / 맥락) kỹ thuật (engineering / 엔지니어링) matters.

> **Chuyển mạch:** Ở chặng này của **Transformer: Attention + Residual Computation ở quy mô lớn**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Transformer synthesizes [Attention](./04_attention.md), [Residual/Backprop](../05_neural_networks/04_backpropagation.md), [RMSNorm](../05_neural_networks/06_initialization_and_normalization.md), [Representation Learning](../05_neural_networks/08_representation_learning.md).

NLP and LLM folders will build tokenization, pretraining, scaling, instruction tuning and generation on top of this mechanism.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
