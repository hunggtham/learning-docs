# RAG Evaluation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **RAG evaluation**. Route đi từ retrieval recall → context relevance/faithfulness → answer correctness → end-to-end query–evidence sets → robustness and cost, để đánh giá tách được lỗi lấy bằng chứng khỏi lỗi sinh câu trả lời.

RAG là multi-stage hệ thống (system / 시스템) nên một final-answer score không đủ để biết thất bại (failure / 실패) nằm ở đâu. Evaluation tốt phải tách **ingestion → retrieval → reranking → ngữ cảnh (context / 맥락) selection → generation → citation**.

## Evaluation Layers

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
1. corpus/index quality
2. retrieval quality
3. reranking/context quality
4. generation groundedness
5. end-to-end task success
6. latency/cost/reliability
```

Nếu final answer sai, dấu vết (trace / 추적) qua từng tầng (layer / 계층) để tìm nguyên nhân gốc (root cause / 근본 원인).

> **Chuyển mạch:** Trong **RAG Evaluation**, **Evaluation Layers** nêu điều cần giải thích; **Bản dựng (build / 빌드) a truy vấn (query / 쿼리)–bằng chứng (evidence / 증거) kiểm thử (test / 테스트) Set** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Retrieval Recall@k** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bản dựng (build / 빌드) a truy vấn (query / 쿼리)–bằng chứng (evidence / 증거) kiểm thử (test / 테스트) Set

Mỗi eval item nên chứa:

```text
query
gold relevant document/chunk IDs
expected answer hoặc key facts
metadata constraints
optional forbidden/stale sources
```

Gold bằng chứng (evidence / 증거) rất valuable vì cho phép evaluate retrieval independent generator.

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **Bản dựng (build / 빌드) a truy vấn (query / 쿼리)–bằng chứng (evidence / 증거) kiểm thử (test / 테스트) Set** nêu điều cần giải thích; **Retrieval Recall@k** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Precision@k** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Retrieval Recall@k

Quan trọng nhất: correct bằng chứng (evidence / 증거) có trong top-k không?

\[
Recall@k=\frac{queries\ with\ relevant\ bằng chứng (evidence / 증거)\ in\ top\ k}{all\ queries}
\]

Nếu Recall@10 thấp, improve retriever/chunking before prompt tuning.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, **Precision@k** tiếp nhận điểm tựa từ **Retrieval Recall@k** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **MRR và nDCG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Precision@k

Đo noise trong candidates/ngữ cảnh (context / 맥락). High recall với quá nhiều distractors có thể hurt generator.

> **Chuyển mạch:** Trong **RAG Evaluation**, **MRR và nDCG** tiếp nhận điểm tựa từ **Precision@k** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chunk-Level vs Document-Level Recall** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MRR và nDCG

MRR reward first relevant kết quả (result / 결과) rank cao. nDCG supports graded relevance và multiple relevant docs.

Use chỉ số (metric / 지표) phù hợp truy vấn (query / 쿼리): multi-source question needs more than first-hit chỉ số (metric / 지표).

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **Chunk-Level vs Document-Level Recall** tiếp nhận điểm tựa từ **MRR và nDCG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reranker Lift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chunk-Level vs Document-Level Recall

Document relevant nhưng retrieved chunk không chứa answer vẫn có thể thất bại (fail / 실패) generation.

Nhánh học (track / 트랙) both:

```text
document recall
answer-bearing chunk recall
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, **Reranker Lift** tiếp nhận điểm tựa từ **Chunk-Level vs Document-Level Recall** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) Recall** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reranker Lift

Compare ranking before và after reranker:

```text
MRR_before → MRR_after
nDCG_before → nDCG_after
```

Nếu reranker không lift, chi phí (cost / 비용) may not be justified.

> **Chuyển mạch:** Trong **RAG Evaluation**, **Ngữ cảnh (context / 맥락) Recall** tiếp nhận điểm tựa từ **Reranker Lift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Answer tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) Recall

Even if candidate set contains bằng chứng (evidence / 증거), ngữ cảnh (context / 맥락) selector may drop it. Evaluate selected final ngữ cảnh (context / 맥락) separately.

This catches token-budget/dedup bugs.

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **Answer tính đúng đắn (correctness / 정확성)** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) Recall** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Faithfulness / Groundedness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Answer tính đúng đắn (correctness / 정확성)

Final answer can be exact-match, rubric-scored, human-judged or LLM-judged depending tác vụ (task / 작업).

For chính sách (policy / 정책) QA, rubric can check required clauses individually rather than one holistic score.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, **Faithfulness / Groundedness** tiếp nhận điểm tựa từ **Answer tính đúng đắn (correctness / 정확성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Citation Precision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Faithfulness / Groundedness

Break answer into claims and ask whether each claim is entailed by retrieved sources.

Conceptually:

\[
Groundedness=\frac{supported\ claims}{all\ factual\ claims}
\]

This is different from tính đúng đắn (correctness / 정확성) relative to bên ngoài (external / 외부) world.

> **Chuyển mạch:** Trong **RAG Evaluation**, **Citation Precision** tiếp nhận điểm tựa từ **Faithfulness / Groundedness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Citation Recall** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Citation Precision

For cited claims, citation should actually hỗ trợ (support / 지원) claim.

```text
citation precision = supported cited claims / cited claims
```

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **Citation Recall** tiếp nhận điểm tựa từ **Citation Precision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Answer Relevance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Citation Recall

How many factual claims that need hỗ trợ (support / 지원) actually have citation?

Useful in research/legal applications.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, **Answer Relevance** tiếp nhận điểm tựa từ **Citation Recall** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Answerability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Answer Relevance

Grounded answer can still thất bại (fail / 실패) người dùng (user / 사용자) intent. Measure whether answer addresses truy vấn (query / 쿼리) and follows requested format.

> **Chuyển mạch:** Trong **RAG Evaluation**, **Answerability** tiếp nhận điểm tựa từ **Answer Relevance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Staleness Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Answerability

Dataset should include questions **not answerable from corpus**. Good RAG should abstain or trạng thái (state / 상태) insufficient bằng chứng (evidence / 증거) rather than hallucinate.

Nhánh học (track / 트랙):

```text
correct abstention rate
false abstention rate
unsupported answer rate
```

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **Staleness Evaluation** tiếp nhận điểm tựa từ **Answerability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Permission Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Staleness Evaluation

Include old/new document versions. Verify retriever selects hiện tại (current / 현재)/effective nguồn (source / 소스) and excludes archived docs when appropriate.

This catches version-filter bugs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, **Permission Evaluation** tiếp nhận điểm tựa từ **Staleness Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multilingual Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Permission Evaluation

Bảo mật (security / 보안) tests should confirm users cannot retrieve documents outside ACL/tenant.

This is pass/thất bại (fail / 실패) bảo mật (security / 보안) thuộc tính (property / 속성), not soft relevance chỉ số (metric / 지표).

> **Chuyển mạch:** Trong **RAG Evaluation**, **Multilingual Evaluation** tiếp nhận điểm tựa từ **Permission Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảng (table / 테이블)/Numeric Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multilingual Evaluation

If users truy vấn (query / 쿼리) Korean/Vietnamese/English, create slices per ngôn ngữ (language / 언어) and cross-language retrieval.

Average score can hide one weak ngôn ngữ (language / 언어).

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **Bảng (table / 테이블)/Numeric Evaluation** tiếp nhận điểm tựa từ **Multilingual Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Robustness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảng (table / 테이블)/Numeric Evaluation

Kiểm thử (test / 테스트) chính xác (exact / 정확한) numeric values, units and bảng (table / 테이블) row relationships. OCR/parser errors often surface here.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, **Robustness** tiếp nhận điểm tựa từ **Bảng (table / 테이블)/Numeric Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hard Negatives** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Robustness

Paraphrase queries, add typo, use aliases, abbreviations and long conversational references. Retrieval should not collapse on superficial wording.

> **Chuyển mạch:** Trong **RAG Evaluation**, **Hard Negatives** tiếp nhận điểm tựa từ **Robustness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **End-to-End độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hard Negatives

Eval corpus should contain near-identical wrong documents:

```text
wrong version
wrong product
wrong country
similar policy title
```

Easy benchmark inflates retrieval chất lượng (quality / 품질).

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **End-to-End độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **Hard Negatives** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## End-to-End độ trễ (latency / 지연 시간)

Break độ trễ (latency / 지연 시간):

```text
query rewrite
embedding
retrieval
rerank
LLM generation
```

p95/p99 matter more than average for UX.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, **Chi phí (cost / 비용) Evaluation** tiếp nhận điểm tựa từ **End-to-End độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Online Metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) Evaluation

Measure per yêu cầu (request / 요청):

```text
embedding tokens
reranker compute
LLM input/output tokens
search infrastructure
```

Advanced chuỗi xử lý (pipeline / 파이프라인) may improve chất lượng (quality / 품질) 1% but double chi phí (cost / 비용); decide based giá trị (value / 값).

> **Chuyển mạch:** Trong **RAG Evaluation**, **Online Metrics** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thất bại (failure / 실패) Attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Online Metrics

After triển khai (deployment / 배포):

```text
user correction rate
citation clicks
escalation rate
zero-result rate
abstention rate
retrieval latency
feedback
```

Online metrics are noisy and influenced by UX, but reveal real traffic shift.

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **Thất bại (failure / 실패) Attribution** tiếp nhận điểm tựa từ **Online Metrics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Eval-Driven Improvement vòng lặp (loop / 루프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) Attribution

A useful taxonomy:

```text
PARSE_FAILURE
CHUNK_MISS
RETRIEVAL_MISS
RERANK_ERROR
CONTEXT_DROP
GENERATION_UNSUPPORTED
CITATION_ERROR
STALE_SOURCE
ACL_ERROR
```

Every môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) should map to tầng (layer / 계층) where possible.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, **Eval-Driven Improvement vòng lặp (loop / 루프)** tiếp nhận điểm tựa từ **Thất bại (failure / 실패) Attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Eval-Driven Improvement vòng lặp (loop / 루프)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
observe failure
→ label root cause
→ add eval case
→ modify one layer
→ rerun suite
→ compare quality/cost
→ deploy
```

This avoids random prompt tweaking.

> **Chuyển mạch:** Trong **RAG Evaluation**, **Human Evaluation** tiếp nhận điểm tựa từ **Eval-Driven Improvement vòng lặp (loop / 루프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM-as-Judge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human Evaluation

Experts are needed when lĩnh vực (domain / 도메인) nuance matters. Use clear rubric và mẫu (sample / 표본) representative cases. Inter-annotator disagreement can reveal ambiguous chính sách (policy / 정책) or insufficient nguồn (source / 소스) dữ liệu (data / 데이터).

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **LLM-as-Judge** tiếp nhận điểm tựa từ **Human Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Golden Set Leakage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM-as-Judge

LLM judges quy mô (scale / 규모) evaluation, especially relevance/faithfulness, but require calibration against humans. Provide nguồn (source / 소스) bằng chứng (evidence / 증거) to judge and randomize phản hồi (response / 응답) thứ tự (order / 순서) to reduce độ lệch (bias / 편향).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, **Golden Set Leakage** tiếp nhận điểm tựa từ **LLM-as-Judge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Golden Set Leakage

If engineers repeatedly tune on same golden set, it becomes development set. Maintain hidden holdout/fresh evals.

> **Chuyển mạch:** Trong **RAG Evaluation**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Golden Set Leakage** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> RAG evaluation phải trả lời hai câu độc lập: **Did we retrieve the right bằng chứng (evidence / 증거)? Did we use it correctly?**

> **Chuyển mạch:** Ở chặng này của **RAG Evaluation**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Final answer đúng nên retrieval cũng tốt”

Mô hình (model / 모델) may answer from parametric bộ nhớ (memory / 메모리) by chance.

### “Retrieval recall cao là đủ”

Ngữ cảnh (context / 맥락) noise/generation faithfulness still matter.

### “LLM judge score là ground truth”

Không. Judge itself needs evaluation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RAG Evaluation**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

RAG evaluation extends [LLM Evaluation](../08_large_language_models/14_llm_evaluation.md) and becomes prerequisite for Agent/AI Engineering observability.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
