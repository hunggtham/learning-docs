# Knowledge Layer về Natural Language Processing

Folder này xây nền tảng **xử lý ngôn ngữ tự nhiên (Natural Language Processing — NLP / 자연어 처리)** từ biểu diễn văn bản tới tìm kiếm và đánh giá. Nó không bắt đầu bằng LLM; mục tiêu là hiểu dữ liệu ngôn ngữ, tokenization, language modeling, embedding và Information Retrieval trước khi sang `08_large_language_models/`.

## Bản đồ phụ thuộc

```mermaid
flowchart TD
    A[00 Ngôn ngữ như dữ liệu] --> B[01 Chuẩn hóa & Tokenization]
    B --> C[02 Language Models]
    A --> D[03 Word Embeddings]
    C --> E[04 Contextual Embeddings]
    D --> E
    C --> F[05 Sequence-to-Sequence NLP]
    E --> G[06 Transformer NLP]
    F --> G
    G --> H[07 Information Extraction]
    E --> I[08 Search & Information Retrieval]
    G --> J[09 NLP Evaluation]
    H --> J
    I --> J
```

## Các chapter

**[00 — Language as Data](./00_language_as_data.md)** đi từ cấu trúc ngôn ngữ, corpus và phân bố, tính mơ hồ, hình thái, BoW/TF-IDF tới bước chuyển từ ký hiệu rời rạc sang biểu diễn liên tục.

**[01 — Text Normalization & Tokenization](./01_text_normalization_and_tokenization.md)** trình bày Unicode, chữ hoa/thường, khoảng trắng, tokenization theo từ/ký tự/byte/subword, BPE, WordPiece, Unigram, SentencePiece, hiệu quả đa ngôn ngữ và vấn đề bảo mật/versioning.

**[02 — Language Models](./02_language_models.md)** xây phân rã xác suất theo chain rule, n-gram và smoothing, neural/autoregressive/masked LM, perplexity, sampling và sự phân biệt “xác suất ngôn ngữ ≠ sự thật”.

**[03 — Word Embeddings](./03_word_embeddings.md)** giải thích giả thuyết phân bố, Word2Vec, CBOW, Skip-Gram, negative sampling, GloVe, PMI, fastText và giới hạn của static embedding.

**[04 — Contextual Embeddings](./04_contextual_embeddings.md)** nối ELMo/BERT, biểu diễn token/câu, bi-encoder/cross-encoder, contrastive retrieval, multilingual embedding và embedding version drift.

**[05 — Sequence-to-Sequence NLP](./05_sequence_to_sequence_nlp.md)** tập trung vào dịch máy và tóm tắt, mô hình ngôn ngữ có điều kiện, Beam Search, cơ chế sao chép, constrained decoding, denoising text-to-text pretraining và faithfulness.

**[06 — Transformer NLP](./06_transformer_nlp.md)** phân biệt encoder-only, decoder-only và encoder–decoder bằng luồng thông tin + mục tiêu pretraining, sau đó đi vào fine-tuning, PEFT, thích ứng domain và đa ngôn ngữ.

**[07 — Information Extraction](./07_information_extraction.md)** chuyển văn bản thành entity, relation, event, slot và fact cho Knowledge Graph có provenance; đồng thời trình bày structured extraction bằng LLM cùng validation.

**[08 — Search & Information Retrieval](./08_search_and_information_retrieval.md)** đi từ inverted index, TF-IDF và BM25 tới dense ANN, hybrid retrieval, reranking, chunking, filter và metric retrieval cho RAG.

**[09 — NLP Evaluation](./09_nlp_evaluation.md)** trình bày metric cho classification/NER, BLEU, ROUGE, chrF, BERTScore, metric học được, human/LLM judge, đánh giá đa ngôn ngữ, contamination và error taxonomy.

## Mô hình tư duy

```text
Ngôn ngữ con người
→ chuẩn hóa / tokenization
→ ký hiệu / token
→ biểu diễn thưa / dày đặc / theo ngữ cảnh
→ mô hình ngôn ngữ / tìm kiếm / trích xuất
→ đầu ra có cấu trúc hoặc văn bản được sinh
→ đánh giá theo đúng tác vụ
```

Chất lượng hệ thống NLP không chỉ nằm ở kiến trúc neural. Corpus, tokenizer, retrieval, output schema, decoding và metric đều có thể trở thành nút thắt chính.

## Chuyển tiếp sang Large Language Models

`08_large_language_models/` không giải thích Transformer và tokenization lại từ đầu. Nó tập trung vào điều xảy ra khi language modeling được **mở rộng quy mô (scaling)** theo dữ liệu, tham số và compute, sau đó được post-train để làm theo chỉ dẫn:

```text
Transformer LM
→ pretraining quy mô lớn
→ foundation model
→ supervised / instruction fine-tuning
→ preference alignment như RLHF / DPO
→ in-context learning / prompting
→ hành vi reasoning
→ hallucination / grounding / evaluation
```

Nhờ layer NLP này, các thuật ngữ `token`, `embedding`, `perplexity`, `autoregressive`, `retrieval` và `reranking` đã có cơ chế rõ ràng trước khi bước vào LLM.