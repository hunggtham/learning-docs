# Sequence-to-Sequence NLP: từ Translation tới Text-to-Text học tập (learning / 학습)

> **Mạch đọc:** Đặt **Sequence-to-Sequence NLP: từ Translation tới Text-to-Text học tập (learning / 학습)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Conditional ngôn ngữ (language / 언어) Modeling** sang **Neural Machine Translation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Sequence-to-Sequence (Seq2Seq / 시퀀스-투-시퀀스) NLP xử lý tasks nơi đầu vào (input / 입력) là một chuỗi (sequence / 시퀀스) và đầu ra (output / 출력) là một chuỗi (sequence / 시퀀스) khác có thể khác length/alignment. Translation, summarization, grammatical correction, question generation và many structured-to-text tasks thuộc family này.

Kiến trúc (architecture / 아키텍처) đã được giải thích ở [Encoder–Decoder Models](../06_deep_learning_architectures/03_encoder_decoder_models.md); chapter này tập trung vào NLP-specific huấn luyện (training / 학습), decoding và evaluation implications.

## Conditional ngôn ngữ (language / 언어) Modeling

Given nguồn (source / 소스) `x`, đầu ra (output / 출력) chuỗi (sequence / 시퀀스) `y`:

\[
P(y\mid x)=\prod_{t=1}^{T}P(y_t\mid y_{<t},x)
\]

Huấn luyện (training / 학습) minimize conditional negative log-likelihood:

\[
L=-\sum_t\log P(y_t^{true}\mid y_{<t}^{true},x)
\]

Nguồn (source / 소스) điều kiện (condition / 조건) distinguishes seq2seq from unconditional/autoregressive LM continuation.

## Neural Machine Translation

Classical statistical MT used phrase tables, alignment các mô hình (models / 모델들) and ngôn ngữ (language / 언어) các mô hình (models / 모델들). Neural MT learned end-to-end conditional mô hình (model / 모델).

RNN encoder-decoder first, then attention removed fixed-vector bottleneck, then Transformer became dominant.

Translation chất lượng (quality / 품질) requires more than word substitution because word thứ tự (order / 순서), morphology, idioms and discourse differ languages.

## Alignment

Attention weights often correlate source-target alignment but are not guaranteed tường minh (explicit / 명시적) linguistic alignments.

Traditional alignment asks which nguồn (source / 소스) word generated mục tiêu (target / 대상) word. Neural seq2seq may distribute nguồn (source / 소스) thông tin (information / 정보) across states/heads.

For explainable translation, dedicated alignment extraction/các ràng buộc (constraints / 제약조건들) may be needed.

## Bản sao (copy / 복사) cơ chế (mechanism / 메커니즘) / Pointer Networks

Some tasks require reproduce names/numbers/entities not well generated from fixed vocabulary.

Pointer/bản sao (copy / 복사) cơ chế (mechanism / 메커니즘) mixes generation phân phối (distribution / 분포) with attention-based copying from nguồn (source / 소스).

Concept:

\[
P(token)=p_{gen}P_{vocab}+(1-p_{gen})P_{bản sao (copy / 복사)}
\]

Useful summarization, data-to-text and entity-heavy tasks.

Hiện đại (modern / 현대적) subword LMs reduce OOV but chính xác (exact / 정확한) copying still important.

## Summarization

**Extractive** summarization selects nguồn (source / 소스) spans/sentences.

**Abstractive** summarization generates new wording.

Abstractive các mô hình (models / 모델들) rủi ro (risk / 위험) hallucinating facts because generation mục tiêu (objective / 목표) rewards likely summary văn bản (text / 텍스트), not strict entailment.

Faithfulness evaluation therefore separate from fluency/coverage.

## Teacher Forcing và Exposure độ lệch (bias / 편향)

Huấn luyện (training / 학습) sees correct previous mục tiêu (target / 대상). suy luận (inference / 추론) sees own generated lịch sử (history / 이력).

Sequence-level huấn luyện (training / 학습) approaches such as minimum rủi ro (risk / 위험) huấn luyện (training / 학습) or reinforcement học tập (learning / 학습) have been explored, but token-level MLE remains foundation due stability/scalability.

## Beam tìm kiếm (search / 검색)

Beam keeps top `B` partial translations according cumulative score.

Raw log xác suất (probability / 확률) biases short sequences. Length normalization:

\[
score(y)=\frac{\log P(y\mid x)}{len(y)^\alpha}
\]

or other penalties balance length.

Larger beam does not always improve human chất lượng (quality / 품질); mô hình (model / 모델) xác suất (probability / 확률) may prefer generic/short hypotheses.

## Coverage

Seq2seq may under-translate/repeat nguồn (source / 소스). Coverage mechanisms nhánh học (track / 트랙) how much attention each nguồn (source / 소스) position received.

Hiện đại (modern / 현대적) Transformers reduce but do not eliminate omissions/repetitions.

## Text-to-Text Unification

T5-style framing casts tasks as:

```text
input text + task prefix → output text
```

Examples:

```text
translate English to German: ...
summarize: ...
```

One conditional generation kiến trúc (architecture / 아키텍처) handles classification, QA, translation, summarization.

This foreshadows instruction-tuned LLMs where natural ngôn ngữ (language / 언어) defines tác vụ (task / 작업).

## Denoising Seq2Seq Pretraining

Corrupt đầu vào (input / 입력) spans and train mô hình (model / 모델) reconstruct original:

```text
corrupted text → encoder
               → decoder → original text
```

This lets encoder-decoder learn ngôn ngữ (language / 언어) from unlabeled corpora before supervised fine-tuning.

BART/T5-style objectives are examples.

## Constrained Decoding

Some applications require đầu ra (output / 출력) format/terminology các ràng buộc (constraints / 제약조건들).

Constrained beam tìm kiếm (search / 검색) can force phrases, lược đồ (schema / 스키마) tokens or grammar.

For structured JSON generation, hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) may constrain next-token choices by grammar/lược đồ (schema / 스키마) rather than hope prompt alone produces valid cấu trúc (structure / 구조).

This connects ngôn ngữ (language / 언어) generation with classical tìm kiếm (search / 검색)/ràng buộc (constraint / 제약조건) satisfaction.

## Multilingual Translation

One mô hình (model / 모델) can handle many ngôn ngữ (language / 언어) pairs with ngôn ngữ (language / 언어) tags/instructions.

Transfer helps low-resource pairs, but sức chứa (capacity / 용량)/dữ liệu (data / 데이터) imbalance can cause interference. Sampling temperature/reweighting often used so high-resource English does not dominate.

Zero-shot translation may emerge between pairs not directly trained, but chất lượng (quality / 품질) varies.

## Evaluation: BLEU

BLEU compares n-gram precision against references with brevity penalty.

Simplified:

\[
BLEU=BP\cdot\exp\left(\sum_nw_n\log p_n\right)
\]

Useful corpus-level MT benchmark, but limitations:

- multiple valid translations;
- weak ngữ nghĩa (semantic / 의미적)/factual sensitivity;
- tokenization matters;
- sentence-level unstable.

Neural metrics like COMET/BERTScore use learned representations but introduce mô hình (model / 모델) độ lệch (bias / 편향).

Human evaluation remains important for adequacy/fluency/faithfulness.

## Sequence-Level lỗi (error / 오류)

A single early decoding lỗi (error / 오류) changes subsequent lịch sử (history / 이력). đơn vị từ (token / 토큰) accuracy does not capture toàn cục (global / 전역) coherence.

Evaluation should inspect:

```text
omission
addition/hallucination
mistranslation
entity/number errors
agreement
terminology consistency
repetition
```

## Lĩnh vực (domain / 도메인) Adaptation

General MT may thất bại (fail / 실패) legal/medical/company terminology. Fine-tuning/adapters, terminology các ràng buộc (constraints / 제약조건들) and retrieval of translation bộ nhớ (memory / 메모리) can help.

But lĩnh vực (domain / 도메인) adaptation can cause catastrophic forgetting general ngôn ngữ (language / 언어); mixing/general dữ liệu (data / 데이터) and controlled fine-tuning matter.

## Mô hình tư duy (mental model / 사고 모델)

> Seq2Seq NLP is conditional ngôn ngữ (language / 언어) modeling plus a source-information truy cập (access / 접근) cơ chế (mechanism / 메커니즘) and a decoding/tìm kiếm (search / 검색) procedure.

Kiến trúc (architecture / 아키텍처) gives xác suất (probability / 확률) phân phối (distribution / 분포); decoding turns phân phối (distribution / 분포) into final chuỗi (sequence / 시퀀스).

## Dùng chung (common / 공통) Misconceptions

### “Beam tìm kiếm (search / 검색) tìm chính xác (exact / 정확한) best translation”

Finite beam is heuristic and mô hình (model / 모델)'s highest-probability chuỗi (sequence / 시퀀스) may not be best human translation.

### “High BLEU means factually faithful summary”

BLEU overlap cannot reliably detect hallucinated facts.

### “Seq2Seq became obsolete after decoder-only LLMs”

Encoder-decoder remains efficient/natural for conditional transformation and widely used; decoder-only unifies via prompting but not universally optimal.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Seq2Seq combines [Language Models](./02_language_models.md), [Encoder–Decoder](../06_deep_learning_architectures/03_encoder_decoder_models.md), [Attention](../06_deep_learning_architectures/04_attention.md), and connects classical tìm kiếm (search / 검색) via decoding.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 language as data](./00_language_as_data.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
