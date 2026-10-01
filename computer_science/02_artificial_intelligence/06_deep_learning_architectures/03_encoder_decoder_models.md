# Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Sequence-to-Sequence bài toán (problem / 문제)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Early RNN Seq2Seq** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Encoder–Decoder (인코더–디코더) là architectural mẫu (pattern / 패턴) cho tasks nơi đầu vào (input / 입력) và đầu ra (output / 출력) có structures/lengths khác nhau. Encoder biến đầu vào (input / 입력) thành nội bộ (internal / 내부) biểu diễn (representation / 표현); decoder dùng biểu diễn (representation / 표현) đó để tạo đầu ra (output / 출력).

Mẫu (pattern / 패턴) này xuất hiện trong translation, summarization, speech recognition, ảnh (image / 이미지) captioning, autoencoders và Transformers. “Encoder” và “decoder” không phải một thuật toán (algorithm / 알고리즘) cụ thể; chúng là vai trò trong computation hệ thống (system / 시스템).

## Sequence-to-Sequence bài toán (problem / 문제)

Translation:

```text
English sequence → Korean sequence
```

Đầu vào (input / 입력) length khác đầu ra (output / 출력) length. Per-token aligned classifier không đủ.

Mô hình (model / 모델) factor đầu ra (output / 출력) autoregressively:

\[
P(y_{1:T}\mid x)=\prod_{t=1}^{T}P(y_t\mid y_{<t},x)
\]

Encoder processes `x`; decoder các mô hình (models / 모델들) conditional next-token phân phối (distribution / 분포).

> **Chuyển mạch:** Trong **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Early RNN Seq2Seq** tiếp nhận điểm tựa từ **Sequence-to-Sequence bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) Bottleneck** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Early RNN Seq2Seq

Encoder RNN:

\[
h_t^{enc}=f(x_t,h_{t-1}^{enc})
\]

Final trạng thái (state / 상태):

\[
c=h_T^{enc}
\]

Decoder:

\[
h_t^{dec}=g(y_{t-1},h_{t-1}^{dec},c)
\]

All nguồn (source / 소스) thông tin (information / 정보) compressed into fixed véc-tơ (vector / 벡터) `c`.

For long sentences, this becomes thông tin (information / 정보) bottleneck.

> **Chuyển mạch:** Ở chặng này của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Ngữ cảnh (context / 맥락) Bottleneck** tiếp nhận điểm tựa từ **Early RNN Seq2Seq** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Teacher Forcing in Decoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) Bottleneck

Imagine nguồn (source / 소스) 100 tokens nhưng decoder only gets one véc-tơ (vector / 벡터). Even high-dimensional véc-tơ (vector / 벡터) must preserve all details needed at every đầu ra (output / 출력) step.

As đầu vào (input / 입력) grows, hiệu năng (performance / 성능) degrades. This motivated attention: decoder at each step constructs ngữ cảnh (context / 맥락) from all encoder states dynamically.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Teacher Forcing in Decoder** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) Bottleneck** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Start / End Tokens** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Teacher Forcing in Decoder

Huấn luyện (training / 학습) usually conditions on ground-truth previous mục tiêu (target / 대상):

\[
P(y_t\mid y_{<t}^{true},x)
\]

Suy luận (inference / 추론) conditions on generated tokens.

Mismatch creates exposure độ lệch (bias / 편향), but teacher forcing remains computationally effective and tiêu chuẩn (standard / 표준).

> **Chuyển mạch:** Trong **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Start / End Tokens** tiếp nhận điểm tựa từ **Teacher Forcing in Decoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decoding Algorithms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Start / End Tokens

Decoder needs know when generation begins/ends.

Special tokens:

```text
<BOS> beginning of sequence
<EOS> end of sequence
```

Generation stops when EOS emitted or max length reached.

Hiện đại (modern / 현대적) LLM chat protocols use richer special/điều khiển (control / 제어) tokens but same idea: chuỗi (sequence / 시퀀스) cấu trúc (structure / 구조) encoded by đơn vị từ (token / 토큰) conventions.

> **Chuyển mạch:** Ở chặng này của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Decoding Algorithms** tiếp nhận điểm tựa từ **Start / End Tokens** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Encoder-only kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decoding Algorithms

At each step mô hình (model / 모델) outputs phân phối (distribution / 분포). Choosing final chuỗi (sequence / 시퀀스) requires tìm kiếm (search / 검색).

### Greedy Decoding

\[
y_t=\arg\max_kP(y_t=k\mid context)
\]

Fast but locally best choice may cause poor toàn cục (global / 전역) chuỗi (sequence / 시퀀스).

### Beam tìm kiếm (search / 검색)

Keep top `B` partial hypotheses according cumulative log-probability.

```text
step 1: keep B candidates
step 2: expand each → keep best B
...
```

Beam tìm kiếm (search / 검색) is heuristic tìm kiếm (search / 검색) in chuỗi (sequence / 시퀀스) không gian (space / 공간).

Length normalization often needed because log probabilities sum negative values and may favor short sequences.

### Sampling

For open-ended generation, mẫu (sample / 표본) from phân phối (distribution / 분포). Temperature/top-k/top-p later discussed in LLM generation.

Translation historically favors beam; creative văn bản (text / 텍스트) often sampling.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Encoder-only kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Decoding Algorithms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decoder-only kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Encoder-only kiến trúc (architecture / 아키텍처)

If đầu ra (output / 출력) is label/biểu diễn (representation / 표현), decoder unnecessary.

BERT-like các mô hình (models / 모델들) are encoder-only: bidirectional self-attention creates contextual representations for classification/extraction.

> **Chuyển mạch:** Trong **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Decoder-only kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Encoder-only kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Encoder–Decoder Transformer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decoder-only kiến trúc (architecture / 아키텍처)

If tác vụ (task / 작업) is autoregressive continuation conditioned on prefix, decoder-only kiến trúc (architecture / 아키텍처) sufficient.

GPT-family uses nhân quả (causal / 인과적) self-attention:

\[
P(x_t\mid x_{<t})
\]

Đầu vào (input / 입력) prompt itself acts conditioning prefix; no separate encoder.

> **Chuyển mạch:** Ở chặng này của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Encoder–Decoder Transformer** tiếp nhận điểm tựa từ **Decoder-only kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cross-Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Encoder–Decoder Transformer

Các mô hình (models / 모델들) like original Transformer/T5-style:

- encoder: bidirectional self-attention over nguồn (source / 소스);
- decoder: nhân quả (causal / 인과적) self-attention over generated mục tiêu (target / 대상);
- cross-attention: decoder queries encoder representations.

This matches translation/conditional generation naturally.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Cross-Attention** tiếp nhận điểm tựa từ **Encoder–Decoder Transformer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Beyond văn bản (text / 텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cross-Attention

Decoder hidden trạng thái (state / 상태) provides queries; encoder outputs provide keys/values:

\[
Attention(Q_{dec},K_{enc},V_{enc})
\]

At each mục tiêu (target / 대상) position, decoder retrieves relevant nguồn (source / 소스) thông tin (information / 정보).

Cross-attention is learned differentiable retrieval across nguồn (source / 소스) positions.

> **Chuyển mạch:** Trong **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Beyond văn bản (text / 텍스트)** tiếp nhận điểm tựa từ **Cross-Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Latent Bottleneck Autoencoders** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Beyond văn bản (text / 텍스트)

Ảnh (image / 이미지) captioning:

```text
Image encoder → visual tokens/features
        ↓ cross-attention
Text decoder → caption
```

Speech translation:

```text
audio encoder → acoustic representation
text decoder → translated text
```

Multimodal các mô hình (models / 모델들) often use encoder/projection + LLM decoder patterns.

> **Chuyển mạch:** Ở chặng này của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Latent Bottleneck Autoencoders** tiếp nhận điểm tựa từ **Beyond văn bản (text / 텍스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thông tin (information / 정보) luồng (flow / 흐름) là cách phân loại hữu ích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Latent Bottleneck Autoencoders

Autoencoder also encoder-decoder:

\[
x\xrightarrow{encoder}z\xrightarrow{decoder}\hat x
\]

Nhưng goal là reconstruct đầu vào (input / 입력), not conditional chuỗi (sequence / 시퀀스) translation. Same kiến trúc (architecture / 아키텍처) mẫu (pattern / 패턴), different mục tiêu (objective / 목표)/probabilistic ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Latent Bottleneck Autoencoders** xác định đầu vào; **Thông tin (information / 정보) luồng (flow / 흐름) là cách phân loại hữu ích** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thông tin (information / 정보) luồng (flow / 흐름) là cách phân loại hữu ích

Thay vì nhớ mô hình (model / 모델) names, hỏi:

```text
Which positions can encoder see?
Which positions can decoder see?
Where can decoder access source?
Is generation causal?
What representation bottleneck exists?
```

Attention mask/connectivity defines thông tin (information / 정보) luồng (flow / 흐름).

> **Chuyển mạch:** Trong **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Thông tin (information / 정보) luồng (flow / 흐름) là cách phân loại hữu ích** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Encoder answers “đầu vào (input / 입력) nên được biểu diễn như thế nào?”; decoder answers “từ biểu diễn (representation / 표현) + outputs trước đó, tạo đầu ra (output / 출력) tiếp theo thế nào?”.

Cross-attention removes need to squeeze all nguồn (source / 소스) details into one fixed véc-tơ (vector / 벡터).

> **Chuyển mạch:** Ở chặng này của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Encoder = embedding tầng (layer / 계층), decoder = đầu ra (output / 출력) tầng (layer / 계층)”

Không. Encoder/decoder thường là multi-layer networks with rich computation.

### “Every Transformer has encoder and decoder”

Có encoder-only, decoder-only và encoder-decoder families.

### “Beam tìm kiếm (search / 검색) guarantees highest-probability chuỗi (sequence / 시퀀스)”

Finite beam is heuristic; chính xác (exact / 정확한) tìm kiếm (search / 검색) over huge chuỗi (sequence / 시퀀스) không gian (space / 공간) infeasible.

### “Decoder-only LLM cannot tiến trình (process / 프로세스) đầu vào (input / 입력) because no encoder”

Prompt tokens are encoded through same nhân quả (causal / 인과적) Transformer ngăn xếp (stack / 스택); no separate encoder mô-đun (module / 모듈) required.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Encoder–Decoder các mô hình (models / 모델들): tách hiểu đầu vào (input / 입력) và tạo đầu ra (output / 출력)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Encoder–Decoder nối [Search](../02_search_reasoning_and_planning/00_state_space_and_search.md), [Sequence Models](./01_sequence_models.md), [RNN/LSTM](./02_rnn_lstm_gru.md) và trực tiếp dẫn tới [Attention](./04_attention.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
