# Đánh giá RAG

**Sinh có tăng cường truy xuất (Retrieval-Augmented Generation — RAG)** là hệ thống nhiều tầng, vì vậy một điểm số câu trả lời cuối không đủ để biết lỗi nằm ở đâu. Đánh giá tốt phải tách rõ **ingestion → retrieval → reranking → chọn context → generation → citation**, đồng thời giữ được lineage để tái hiện chính xác tài liệu và cấu hình nào đã tạo ra câu trả lời.

## Kiến thức cần có trước

Nên nắm [Information Retrieval](./00_information_retrieval_foundations.md), [Sparse và Dense Retrieval](./01_sparse_and_dense_retrieval.md), [Vector Search](./03_vector_search.md), [RAG Fundamentals](./05_rag_fundamentals.md), [Ranking và Reranking](./07_retrieval_ranking_and_reranking.md) và [LLM Evaluation](../08_large_language_models/14_llm_evaluation.md).

## RAG Evaluation thực sự đang đo gì?

Một pipeline có thể được phân rã:

```text
corpus / parser
→ chunking
→ embedding / index
→ query transform
→ candidate retrieval
→ reranking
→ context selection
→ generation
→ citation / verification
```

Mỗi stage có metric riêng. Nếu chỉ chấm final answer, ta không biết hệ thống sai vì **không tìm thấy evidence**, **tìm thấy nhưng xếp thấp**, **context selector loại nhầm**, hay **LLM không dùng đúng evidence**.

## Hợp đồng đánh giá RAG

Mỗi evaluation suite nên ghi rõ:

```text
corpus snapshot nào?
parser/chunking version nào?
embedding model và index version nào?
retriever/reranker config nào?
ACL/tenant policy nào?
LLM/prompt version nào?
query distribution nào?
source freshness requirement nào?
```

Nếu index đã được rebuild mà report vẫn ghi cùng tên hệ thống, score cũ không còn cùng ý nghĩa.

## Xây tập kiểm thử Query–Evidence

Mỗi item nên có:

```text
query
relevant document IDs
relevant chunk IDs nếu có
fact/claim bắt buộc
metadata constraint
version/effective-date constraint
ACL/tenant context
expected answerability
```

**Gold evidence** rất có giá trị vì cho phép đánh giá retrieval độc lập với generator.

## Retrieval Recall@k

Câu hỏi đầu tiên: evidence đúng có nằm trong top-k không?

\[
Recall@k=\frac{\text{số query có evidence đúng trong top-k}}{\text{tổng số query}}
\]

Nếu `Recall@10` thấp, nên cải thiện parser/chunking/retriever trước khi tune prompt.

## Precision@k

Precision@k đo tỷ lệ result thực sự liên quan trong top-k:

\[
Precision@k=\frac{\text{số result relevant trong top-k}}{k}
\]

Recall cao nhưng precision thấp có thể tạo context nhiều nhiễu, làm tăng token cost và làm generator bỏ sót evidence quan trọng.

## MRR và nDCG

MRR thưởng việc result relevant đầu tiên xuất hiện sớm. nDCG phù hợp khi relevance có nhiều mức và có nhiều document relevant.

Không nên dùng một metric cho mọi query. Câu hỏi cần tổng hợp nhiều nguồn khác bài toán “tìm đúng một policy document”.

## Recall ở cấp Document và Chunk

Document đúng nhưng chunk được retrieve không chứa câu trả lời vẫn có thể làm generation thất bại.

Nên theo dõi:

```text
document recall
answer-containing chunk recall
supporting-evidence coverage
```

Điều này giúp phân biệt lỗi retriever với lỗi chunking.

## Mức cải thiện của Reranker

So sánh ranking trước và sau reranker:

```text
MRR_before → MRR_after
nDCG_before → nDCG_after
Recall@k_before → Recall@k_after
```

Nếu reranker tăng latency/cost nhưng gần như không tăng quality, nó có thể không đáng tồn tại ở production path.

## Context Recall và Context Precision

Candidate set có thể chứa evidence đúng nhưng context selector vẫn loại nhầm vì token budget hoặc dedup.

Có thể theo dõi:

```text
context recall    → evidence cần thiết có được giữ lại không?
context precision → bao nhiêu context thực sự hữu ích?
```

Context precision thấp thường làm prompt dài hơn và tăng nguy cơ “lost in the middle”.

## Tính đúng và Groundedness của câu trả lời

Final answer có thể được chấm bằng exact match, rubric, human evaluator hoặc LLM judge tùy tác vụ.

Groundedness đo factual claim có được context hỗ trợ không:

\[
Groundedness=\frac{\text{số factual claim được evidence hỗ trợ}}{\text{tổng số factual claim}}
\]

Metric này **khác correctness đối với thế giới bên ngoài**. Một claim có thể được tài liệu hỗ trợ nhưng tài liệu đã lỗi thời.

## Precision và Recall của Citation

Với citation:

```text
citation precision → citation được gắn có thực sự hỗ trợ claim không?
citation recall    → factual claim cần nguồn có được gắn citation không?
```

Ứng dụng nghiên cứu, pháp lý hoặc enterprise policy thường cần cả hai.

## Answerability và Abstention

Dataset nên chứa cả câu hỏi **không thể trả lời từ corpus**. Hệ thống tốt phải biết abstain hoặc yêu cầu thêm nguồn thay vì bịa.

Theo dõi:

```text
correct abstention rate
false abstention rate
unsupported answer rate
```

Đây là một phần quan trọng của reliability, không chỉ quality.

## Freshness và Temporal Correctness

RAG production thường có nhiều version của cùng tài liệu. Eval cần chứa các case:

```text
policy cũ vs policy hiện hành
record có effective date
query hỏi trạng thái tại một thời điểm lịch sử
index rebuild chưa đồng bộ
```

**Freshness** không chỉ là “document mới nhất”; đôi khi query cần đúng version tại thời điểm cụ thể.

## ACL và Tenant Isolation

Authorization phải được đánh giá như thuộc tính **pass/fail**:

```text
user A không retrieve được tài liệu của tenant B
cache không trả context của tenant khác
reranker không làm mất ACL filter
fallback search vẫn giữ policy
```

Một pipeline có retrieval quality cao nhưng vi phạm ACL là thất bại nghiêm trọng.

## Hard Negative

Eval corpus nên có tài liệu gần giống nhưng sai:

```text
sai version
sai sản phẩm
sai quốc gia
sai tenant
tiêu đề gần giống
policy superseded
```

Hard negative giúp đo khả năng phân biệt thật thay vì chỉ tìm từ khóa dễ.

## Đánh giá đa ngôn ngữ và cross-lingual retrieval

Nếu người dùng dùng Việt, Hàn và Anh, cần slice riêng cho từng ngôn ngữ và query-document khác ngôn ngữ.

Điểm trung bình có thể che việc một embedding model hoạt động tốt tiếng Anh nhưng yếu đáng kể ở tiếng Việt.

## Table, Numeric và Structured Evidence

RAG trên bảng cần test:

```text
đúng hàng/cột
đúng đơn vị
đúng phép tổng hợp
không trộn row khác nhau
citation tới đúng bảng/record
```

Lỗi parser và OCR thường lộ rõ ở nhóm này.

## Robustness

Paraphrase query, thêm typo, alias, abbreviation, context hội thoại và thông tin gây nhiễu. Retrieval không nên sụp chỉ vì thay đổi bề mặt.

Ngược lại, khi một điều kiện quan trọng đổi (`Hàn Quốc` → `Việt Nam`, `2025` → `2026`), retrieval phải **nhạy đúng chỗ** và chuyển sang evidence khác.

## Mô hình triển khai của RAG eval harness

Một harness có thể chạy như sau:

```text
versioned query-evidence cases
→ build/reuse corpus snapshot
→ run retrieval và lưu candidate IDs + scores
→ run reranker và lưu ranking
→ build final context và lưu chunk IDs
→ generate answer
→ claim/citation verification
→ aggregate stage metrics + slices
```

Mỗi run nên lưu đủ metadata:

```text
parser version
chunking version
embedding model
index build ID
retriever parameters
reranker version
LLM/prompt version
ACL context
timestamp
```

Nhờ đó một regression có thể được **replay theo stage** thay vì chỉ nhìn final text.

## Trace-based Root Cause Analysis

Một trace tốt cho một query:

```text
query
→ transformed query
→ candidate IDs + scores
→ reranked IDs + scores
→ selected context IDs
→ generated claims
→ citation mapping
```

Nếu final answer sai, trace cho phép xác định lỗi xuất hiện lần đầu ở stage nào.

## Latency và Tail Latency

Nên phân rã:

```text
query rewrite
embedding
vector/sparse retrieval
rerank
context assembly
LLM prefill
generation
verification
```

Theo dõi p50, p95 và p99. Một reranker chỉ thỉnh thoảng chậm có thể phá SLO dù latency trung bình vẫn đẹp.

## Cost Attribution

Chi phí mỗi request gồm:

```text
embedding compute
search infrastructure
reranker compute
LLM input/output token
verification/judge calls
```

Nên tính **cost per successful grounded answer**, không chỉ cost/request. Một pipeline rẻ nhưng thất bại thường xuyên có thể đắt hơn về mặt business.

## Statistical Uncertainty

Metric retrieval trên sample hữu hạn cũng có uncertainty. Khi so hai retriever trên cùng query set, paired bootstrap có thể giúp ước lượng chênh lệch ổn định tới đâu.

Nếu LLM generation stochastic, nên lặp lại một số case để phân biệt variance của generator với regression của retrieval.

## Online Metrics

Sau deploy có thể theo dõi:

```text
zero-result rate
abstention rate
citation click
user correction
escalation rate
retrieval latency
stale-source incidents
ACL violation blocks
```

Online metric chịu ảnh hưởng UX và selection bias, nên dùng để phát hiện drift chứ không thay thế offline ground truth.

## Failure Taxonomy

Nên tag failure theo layer:

```text
PARSE_FAILURE
CHUNK_MISS
INDEX_STALE
RETRIEVAL_MISS
RERANK_ERROR
CONTEXT_DROP
GENERATION_UNSUPPORTED
CITATION_ERROR
STALE_SOURCE
ACL_ERROR
CACHE_SCOPE_ERROR
```

Mỗi incident đáng kể nên trở thành regression case mới.

## Failure mode của chính evaluation

**Gold evidence quá hẹp.** Hệ thống retrieve một nguồn đúng khác nhưng bị chấm sai.

**Corpus drift không được pin.** Chạy lại cùng eval nhưng index đã khác.

**Chỉ đo answer correctness.** Không phát hiện model trả đúng nhờ parametric memory dù retrieval sai.

**Chỉ đo Recall@k.** Không phát hiện context selector loại evidence hoặc generator hallucinate.

**Không test unanswerable query.** Hệ thống học thói quen luôn trả lời.

**Không test ACL.** Security regression không xuất hiện trong quality dashboard.

## Vòng cải thiện dựa trên eval

```text
quan sát failure
→ gắn root cause stage
→ thêm case vào suite
→ sửa đúng layer
→ chạy lại stage metrics + end-to-end
→ so quality / latency / cost
→ canary
→ monitor production
```

Cách này tốt hơn thay prompt hoặc model ngẫu nhiên.

## Mô hình tư duy

> Đánh giá RAG phải trả lời ba câu riêng: **Ta có tìm đúng evidence không? Ta có giữ và dùng evidence đúng không? Evidence đó có đúng quyền và đúng thời điểm không?**

## Những hiểu lầm thường gặp

### “Final answer đúng nghĩa là retrieval tốt”

Không. Mô hình có thể trả đúng từ parametric memory.

### “Retrieval recall cao là đủ”

Không. Context noise, freshness, ACL và generation faithfulness vẫn quan trọng.

### “Điểm của LLM judge là ground truth”

Không. Bản thân judge cũng cần được đánh giá và version hóa.

### “Vector search đúng là RAG đúng”

Không. RAG còn phụ thuộc parser, chunking, reranking, context selection, generation và verification.

## Liên kết kiến thức

Đánh giá RAG mở rộng [LLM Evaluation](../08_large_language_models/14_llm_evaluation.md), phụ thuộc [Vector Search](./03_vector_search.md), [RAG Fundamentals](./05_rag_fundamentals.md), [Ranking/Reranking](./07_retrieval_ranking_and_reranking.md), và dẫn tới [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [Evaluation Foundations](../18_evaluation_reliability_interpretability/00_evaluation_foundations.md) và [LLMOps](../16_mlops_and_llmops/08_llmops.md).