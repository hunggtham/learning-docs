# RAG Evaluation

> **Mạch đọc:** Đặt **RAG Evaluation** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Evaluation Layers** sang **bản dựng (build / 빌드) a truy vấn (query / 쿼리)–bằng chứng (evidence / 증거) kiểm thử (test / 테스트) Set**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


RAG là multi-stage hệ thống (system / 시스템) nên một final-answer score không đủ để biết thất bại (failure / 실패) nằm ở đâu. Evaluation tốt phải tách **ingestion → retrieval → reranking → ngữ cảnh (context / 맥락) selection → generation → citation**.

## Evaluation Layers

```text
1. corpus/index quality
2. retrieval quality
3. reranking/context quality
4. generation groundedness
5. end-to-end task success
6. latency/cost/reliability
```

Nếu final answer sai, dấu vết (trace / 추적) qua từng tầng (layer / 계층) để tìm nguyên nhân gốc (root cause / 근본 원인).

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

## Retrieval Recall@k

Quan trọng nhất: correct bằng chứng (evidence / 증거) có trong top-k không?

\[
Recall@k=\frac{queries\ with\ relevant\ bằng chứng (evidence / 증거)\ in\ top\ k}{all\ queries}
\]

Nếu Recall@10 thấp, improve retriever/chunking before prompt tuning.

## Precision@k

Đo noise trong candidates/ngữ cảnh (context / 맥락). High recall với quá nhiều distractors có thể hurt generator.

## MRR và nDCG

MRR reward first relevant kết quả (result / 결과) rank cao. nDCG supports graded relevance và multiple relevant docs.

Use chỉ số (metric / 지표) phù hợp truy vấn (query / 쿼리): multi-source question needs more than first-hit chỉ số (metric / 지표).

## Chunk-Level vs Document-Level Recall

Document relevant nhưng retrieved chunk không chứa answer vẫn có thể thất bại (fail / 실패) generation.

Nhánh học (track / 트랙) both:

```text
document recall
answer-bearing chunk recall
```

## Reranker Lift

Compare ranking before và after reranker:

```text
MRR_before → MRR_after
nDCG_before → nDCG_after
```

Nếu reranker không lift, chi phí (cost / 비용) may not be justified.

## Ngữ cảnh (context / 맥락) Recall

Even if candidate set contains bằng chứng (evidence / 증거), ngữ cảnh (context / 맥락) selector may drop it. Evaluate selected final ngữ cảnh (context / 맥락) separately.

This catches token-budget/dedup bugs.

## Answer tính đúng đắn (correctness / 정확성)

Final answer can be exact-match, rubric-scored, human-judged or LLM-judged depending tác vụ (task / 작업).

For chính sách (policy / 정책) QA, rubric can check required clauses individually rather than one holistic score.

## Faithfulness / Groundedness

Break answer into claims and ask whether each claim is entailed by retrieved sources.

Conceptually:

\[
Groundedness=\frac{supported\ claims}{all\ factual\ claims}
\]

This is different from tính đúng đắn (correctness / 정확성) relative to bên ngoài (external / 외부) world.

## Citation Precision

For cited claims, citation should actually hỗ trợ (support / 지원) claim.

```text
citation precision = supported cited claims / cited claims
```

## Citation Recall

How many factual claims that need hỗ trợ (support / 지원) actually have citation?

Useful in research/legal applications.

## Answer Relevance

Grounded answer can still thất bại (fail / 실패) người dùng (user / 사용자) intent. Measure whether answer addresses truy vấn (query / 쿼리) and follows requested format.

## Answerability

Dataset should include questions **not answerable from corpus**. Good RAG should abstain or trạng thái (state / 상태) insufficient bằng chứng (evidence / 증거) rather than hallucinate.

Nhánh học (track / 트랙):

```text
correct abstention rate
false abstention rate
unsupported answer rate
```

## Staleness Evaluation

Include old/new document versions. Verify retriever selects hiện tại (current / 현재)/effective nguồn (source / 소스) and excludes archived docs when appropriate.

This catches version-filter bugs.

## Permission Evaluation

Bảo mật (security / 보안) tests should confirm users cannot retrieve documents outside ACL/tenant.

This is pass/thất bại (fail / 실패) bảo mật (security / 보안) thuộc tính (property / 속성), not soft relevance chỉ số (metric / 지표).

## Multilingual Evaluation

If users truy vấn (query / 쿼리) Korean/Vietnamese/English, create slices per ngôn ngữ (language / 언어) and cross-language retrieval.

Average score can hide one weak ngôn ngữ (language / 언어).

## Bảng (table / 테이블)/Numeric Evaluation

Kiểm thử (test / 테스트) chính xác (exact / 정확한) numeric values, units and bảng (table / 테이블) row relationships. OCR/parser errors often surface here.

## Robustness

Paraphrase queries, add typo, use aliases, abbreviations and long conversational references. Retrieval should not collapse on superficial wording.

## Hard Negatives

Eval corpus should contain near-identical wrong documents:

```text
wrong version
wrong product
wrong country
similar policy title
```

Easy benchmark inflates retrieval chất lượng (quality / 품질).

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

## Chi phí (cost / 비용) Evaluation

Measure per yêu cầu (request / 요청):

```text
embedding tokens
reranker compute
LLM input/output tokens
search infrastructure
```

Advanced chuỗi xử lý (pipeline / 파이프라인) may improve chất lượng (quality / 품질) 1% but double chi phí (cost / 비용); decide based giá trị (value / 값).

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

## Eval-Driven Improvement vòng lặp (loop / 루프)

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

## Human Evaluation

Experts are needed when lĩnh vực (domain / 도메인) nuance matters. Use clear rubric và mẫu (sample / 표본) representative cases. Inter-annotator disagreement can reveal ambiguous chính sách (policy / 정책) or insufficient nguồn (source / 소스) dữ liệu (data / 데이터).

## LLM-as-Judge

LLM judges quy mô (scale / 규모) evaluation, especially relevance/faithfulness, but require calibration against humans. Provide nguồn (source / 소스) bằng chứng (evidence / 증거) to judge and randomize phản hồi (response / 응답) thứ tự (order / 순서) to reduce độ lệch (bias / 편향).

## Golden Set Leakage

If engineers repeatedly tune on same golden set, it becomes development set. Maintain hidden holdout/fresh evals.

## Mô hình tư duy (mental model / 사고 모델)

> RAG evaluation phải trả lời hai câu độc lập: **Did we retrieve the right bằng chứng (evidence / 증거)? Did we use it correctly?**

## Dùng chung (common / 공통) Misconceptions

### “Final answer đúng nên retrieval cũng tốt”

Mô hình (model / 모델) may answer from parametric bộ nhớ (memory / 메모리) by chance.

### “Retrieval recall cao là đủ”

Ngữ cảnh (context / 맥락) noise/generation faithfulness still matter.

### “LLM judge score là ground truth”

Không. Judge itself needs evaluation.

## Liên kết kiến thức (knowledge connection / 지식 연결)

RAG evaluation extends [LLM Evaluation](../08_large_language_models/14_llm_evaluation.md) and becomes prerequisite for tác nhân (agent / 에이전트)/AI kỹ thuật (engineering / 엔지니어링) khả năng quan sát (observability / 관측 가능성).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 information retrieval foundations](./00_information_retrieval_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
