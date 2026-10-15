# Transformer NLP: Encoder, Decoder và tác vụ (task / 작업) Adaptation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Transformer NLP: encoder, decoder và task adaptation**. Route đi từ encoder-only understanding → decoder-only generation → encoder-decoder transformation → pretraining/objectives → fine-tuning and inference cost, để kiến trúc được chọn theo task.

Transformer kiến trúc (architecture / 아키텍처) là general cơ chế (mechanism / 메커니즘); NLP biến cơ chế (mechanism / 메커니즘) đó thành các mô hình (model / 모델) families khác nhau bằng **masking, pretraining mục tiêu (objective / 목표), pooling/head và fine-tuning chiến lược (strategy / 전략)**. BERT, GPT và T5 không chỉ khác tên — chúng encode thông tin (information / 정보) luồng (flow / 흐름) khác nhau.

## Encoder-Only NLP

Encoder self-attention thường bidirectional. Mỗi đơn vị từ (token / 토큰) có thể attend left/right ngữ cảnh (context / 맥락).

BERT-style pretraining dùng Masked ngôn ngữ (language / 언어) Modeling (MLM): chọn một số tokens, corrupt/mask, predict originals.

Biểu diễn (representation / 표현) tốt cho:

- văn bản (text / 텍스트) classification;
- đơn vị từ (token / 토큰) classification/NER;
- extractive QA;
- sentence-pair scoring;
- embeddings sau task-specific huấn luyện (training / 학습).

Encoder-only không naturally generate long autoregressive văn bản (text / 텍스트), vì huấn luyện (training / 학습)/thông tin (information / 정보) luồng (flow / 흐름) không nhân quả (causal / 인과적).

> Encoder-only phù hợp với việc đọc toàn bộ ngữ cảnh để phân loại hoặc gán nhãn, còn decoder-only dùng mặt nạ nhân quả để tiếp tục chuỗi. Đặt hai lựa chọn cạnh nhau giúp thấy vì sao encoder–decoder cần thêm một nguồn đầu vào và một đích đầu ra riêng.

## Decoder-Only NLP

Nhân quả (causal / 인과적) mask:

\[
P(x_t\mid x_{<t})
\]

Một kiến trúc (architecture / 아키텍처) có thể handle many tasks by expressing đầu vào (input / 입력)/tác vụ (task / 작업) as prefix and generating đầu ra (output / 출력) continuation.

This flexibility scales naturally into LLM/instruction following.

For pure classification, decoder mô hình (model / 모델) may be compute-inefficient compared with smaller encoder but unified triển khai (deployment / 배포) can justify it.

> Encoder–decoder tách việc đọc nguồn khỏi việc sinh đích, nên tự nhiên cho dịch và tóm tắt. Sự khác biệt này dẫn tới câu hỏi rộng hơn: cùng một kiến trúc sẽ học hành vi nào nếu mục tiêu pretraining thay đổi?

## Encoder–Decoder NLP

Encoder reads full nguồn (source / 소스) bidirectionally; decoder generates mục tiêu (target / 대상) causally with cross-attention.

Natural for:

- translation;
- summarization;
- structured transformation;
- conditional generation.

T5/BART families show strong text-to-text paradigm.

> Mục tiêu pretraining tạo ra thiên hướng ban đầu, nhưng head và dữ liệu downstream quyết định cách thiên hướng ấy được dùng. Với classification, bước tiếp theo là gắn một head vào biểu diễn đã học và fine-tune có kiểm soát.

## Pretraining mục tiêu (objective / 목표) Shapes năng lực (capability / 역량)

Same kiến trúc (architecture / 아키텍처) under different objectives learns different hành vi (behavior / 동작).

Nhân quả (causal / 인과적) LM rewards continuation.

Masked LM rewards reconstruct hidden tokens using both sides.

Denoising seq2seq rewards reconstruct entire văn bản (text / 텍스트) from corrupted đầu vào (input / 입력).

Contrastive objectives reward similarity hình học (geometry / 기하학).

Do not infer năng lực (capability / 역량) solely from kiến trúc (architecture / 아키텍처).

> Classification thường gom hidden states thành một biểu diễn cấp câu rồi dự đoán nhãn. Khi nhãn nằm ở từng vị trí trong câu, cùng cơ chế ấy phải được chuyển sang token classification và xử lý ranh giới subword.

## Fine-Tuning for Classification

Encoder đầu ra (output / 출력) can pool `[CLS]` or mean hidden states:

\[
h_{pool}=Pool(H)
\]

Classifier:

\[
p(y\mid x)=softmax(Wh_{pool}+b)
\]

Fine-tuning updates all/partial encoder + head.

Small dataset risks overfit/catastrophic forgetting; lower LR, regularization, adapters can help.

> Token classification dự đoán một nhãn cho mỗi vị trí, còn extractive QA dự đoán hai vị trí bắt đầu và kết thúc của câu trả lời. Cả hai đều dựa vào hidden states, nhưng QA thêm ràng buộc span trong ngữ cảnh.

## Đơn vị từ (token / 토큰) Classification

NER/POS tagging uses per-token hidden trạng thái (state / 상태):

\[
p(y_i\mid x)=softmax(Wh_i+b)
\]

Subword complication: one word may split multiple pieces. Labeling chiến lược (strategy / 전략) must decide first-piece/all-piece aggregation.

Metrics should reconstruct word/thực thể (entity / 엔터티) spans correctly.

> Extractive QA buộc câu trả lời phải nằm trong đoạn văn, vì vậy giảm không gian sinh tự do nhưng không thay thế được suy luận. NLI mở rộng bài toán sang việc đối chiếu quan hệ logic giữa một premise và một hypothesis.

## Extractive Question Answering

Given `[question ; context]`, encoder outputs đơn vị từ (token / 토큰) states. Two heads predict start/end positions:

\[
P(start=i),\qquad P(end=j)
\]

Answer constrained to span in ngữ cảnh (context / 맥락), reducing free-form hallucination but cannot answer if answer absent unless no-answer modeled.

> NLI cho thấy mô hình có thể so sánh hai câu, nhưng việc so sánh đó cần để hai chuỗi cùng nhìn thấy nhau. Sentence-pair cross-encoding thực hiện điều này trực tiếp bằng self-attention trên toàn bộ cặp đầu vào.

## Natural ngôn ngữ (language / 언어) suy luận (inference / 추론)

Đầu vào (input / 입력) premise+hypothesis, classify entailment/contradiction/neutral.

NLI datasets useful for ngữ nghĩa (semantic / 의미적) lập luận (reasoning / 추론) but các mô hình (models / 모델들) may exploit annotation artifacts. High benchmark score does not prove robust logical suy luận (inference / 추론).

> Cross-encoder cho điểm cặp câu chính xác nhưng phải chạy lại cho từng cặp ứng viên. Khi muốn tận dụng mô hình cho nhiều task với ít head riêng, prompt-based fine-tuning chuyển task thành một mẫu dự đoán ngôn ngữ.

## Sentence Pair Cross-Encoding

For relevance/paraphrase:

```text
[CLS] query [SEP] document
```

joint self-attention lets every đơn vị từ (token / 토큰) pair interact, giving accurate scoring but O(number of candidate pairs) suy luận (inference / 추론) chi phí (cost / 비용).

Bi-encoder vs cross-encoder sự đánh đổi (trade-off / 트레이드오프) becomes central retrieval kiến trúc (architecture / 아키텍처).

> Prompt-based fine-tuning giữ phần lớn mô hình cố định và diễn đạt nhãn bằng token hoặc chuỗi đầu ra. Nếu toàn bộ trọng số vẫn quá tốn kém, parameter-efficient fine-tuning giảm số tham số cần cập nhật.

## Prompt-Based Fine-Tuning

Instead of classification head, reformulate tác vụ (task / 작업) as ngôn ngữ (language / 언어) prediction:

```text
Review: ... Sentiment: [MASK]
```

or generation.

Prompting aligns downstream tác vụ (task / 작업) with pretraining mục tiêu (objective / 목표), useful few-shot regimes. Verbalizer choice can độ lệch (bias / 편향) results.

> Adapters, LoRA và prompt tuning giảm chi phí cập nhật nhưng không làm mất giới hạn ngữ cảnh của backbone. Với tài liệu dài, cần chọn chiến lược chia hoặc truy hồi để phần thông tin cần thiết còn được nhìn thấy.

## Parameter-Efficient Fine-Tuning

Rather than cập nhật (update / 업데이트) all weights:

- adapters insert small trainable modules;
- LoRA learns low-rank updates;
- prefix/prompt tuning learns virtual token-like vectors;
- bias-only methods cập nhật (update / 업데이트) subset.

Benefits: bộ nhớ (memory / 메모리)/lưu trữ (storage / 저장소), multi-tenant specialization and reduced forgetting. sự đánh đổi (trade-off / 트레이드오프) can be lower ceiling/task-specific quirks.

> Xử lý tài liệu dài là bài toán phân bổ ngữ cảnh chứ không chỉ là tăng độ dài cửa sổ. Nếu dữ liệu có thuật ngữ và phong cách đặc thù, continued pretraining theo domain có thể giải quyết một phần mất mát đó.

## Long Documents

Vanilla Transformer ngữ cảnh (context / 맥락) finite/quadratic. Strategies:

- truncate;
- sliding windows;
- hierarchical encode chunks then aggregate;
- sparse/long attention;
- retrieval before encoding.

Tác vụ (task / 작업) determines whether cục bộ (local / 로컬) chunking loses discourse quan hệ (relation / 관계).

> Domain adaptation tăng độ phù hợp với văn bản chuyên ngành nhưng phải cân bằng chất lượng, quyền sử dụng và nguy cơ quên năng lực chung. Với nhiều ngôn ngữ, bài toán cân bằng dữ liệu và tokenizer trở thành một dạng domain shift khác.

## Domain-Specific NLP các mô hình (models / 모델들)

Biomedical/legal/financial corpora contain vocabulary/style/entities not well represented general các mô hình (models / 모델들). Continued pretraining on lĩnh vực (domain / 도메인) corpus then tác vụ (task / 작업) fine-tuning can improve.

But lĩnh vực (domain / 도메인) pretraining needs chất lượng (quality / 품질)/copyright/privacy controls and can shift general năng lực (capability / 역량).

> Multilingual Transformer chia sẻ biểu diễn giữa các ngôn ngữ nhưng hiệu năng vẫn phụ thuộc dữ liệu và cấu trúc từng ngôn ngữ. Khi mô hình cần được phục vụ với chi phí thấp hơn, distillation truyền lại hành vi cần thiết cho một student nhỏ hơn.

## Multilingual Transformer

Dùng chung (shared / 공유) tokenizer + parameters across languages enables transfer. High-resource languages may dominate sức chứa (capacity / 용량); scripts/đơn vị từ (token / 토큰) efficiency and corpus balance matter.

Cross-lingual transfer works because dùng chung (shared / 공유) representations align statistical structures, but hiệu năng (performance / 성능) uneven. Evaluate each ngôn ngữ (language / 언어), especially Korean/Vietnamese mục tiêu (target / 대상) use.

> Distillation nén kiến thức vào kiến trúc nhỏ hơn bằng soft targets hoặc các tín hiệu trung gian, nhưng vẫn phải đo lại từng task. Quantization tiếp tục giảm chi phí bộ nhớ và tính toán ở tầng tham số, với các đánh đổi khác.

## Distillation

Teacher Transformer transfers hành vi (behavior / 동작) to smaller student using soft targets/hidden-state losses.

Goal reduce độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리) while retain hiệu năng (performance / 성능). Student kiến trúc (architecture / 아키텍처) can be fewer layers/smaller hidden dimension.

Distillation will reappear in triển khai (deployment / 배포)/suy luận (inference / 추론) tầng (layer / 계층).

> Quantization có thể làm giảm độ chính xác ở các tầng nhạy cảm, nên cần calibration và mixed precision phù hợp. Những lựa chọn nén này chỉ có ý nghĩa khi đặt trong toàn bộ pipeline suy luận, từ đó hình thành mental model của chapter.

## Quantization-aware NLP Preview

Suy luận (inference / 추론) can quantize weights/activations. Some NLP các mô hình (models / 모델들) tolerate INT8/4-bit well; sensitive layers/outliers may require mixed precision/calibration.

Mô hình (model / 모델) compression is hệ thống (system / 시스템) ràng buộc (constraint / 제약조건), not separate from NLP triển khai (deployment / 배포).

> Mental model nối attention mask, mục tiêu pretraining, task head và phương pháp adaptation với hành vi quan sát được. Trước khi kết thúc, các ngộ nhận phổ biến sẽ được đối chiếu với chuỗi nguyên nhân này.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Transformer mechanism
+ attention mask / information flow
+ pretraining objective
+ task head / prompting
+ adaptation method
= NLP model behavior
```

> Các ngộ nhận cho thấy không nên suy ra chất lượng từ tên kiến trúc, kích thước mô hình hay một benchmark đơn lẻ. Phần liên kết kiến thức dưới đây đặt những kết luận đó vào các tài liệu owner để người học kiểm chứng tiếp.

## Dùng chung (common / 공통) Misconceptions

### “BERT và GPT chỉ khác dữ liệu huấn luyện (training data / 학습 데이터)”

Kiến trúc (architecture / 아키텍처) direction/mask and mục tiêu (objective / 목표) differ fundamentally.

### “Encoder mô hình (model / 모델) không generate nên kém hơn”

For classification/retrieval/reranking, encoder can be much more efficient and accurate per compute.

### “Fine-tuning all weights always best”

Small dữ liệu (data / 데이터)/multi-task/serving các ràng buộc (constraints / 제약조건들) may favor PEFT.

### “Multilingual mô hình (model / 모델) means language-independent biểu diễn (representation / 표현) hoàn hảo”

Cross-lingual alignment is imperfect and data-dependent.

> Các liên kết cuối chapter đưa kiến trúc Transformer về các bài encoder–decoder và Seq2Seq, rồi mở sang Information Extraction. Hãy dùng chúng để quay lại phần cần thiết thay vì xem các family mô hình là những lựa chọn độc lập.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Transformer architecture](../06_deep_learning_architectures/05_transformer.md), [Seq2Seq NLP](./05_sequence_to_sequence_nlp.md), and next [Information Extraction](./07_information_extraction.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
