# Retrieval, Ranking và Reranking

> **Mạch đọc:** Đặt **Retrieval, Ranking và Reranking** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Candidate Generation** sang **Reranking**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một retrieval hệ thống (system / 시스템) tốt thường không cố dùng một mô hình (model / 모델) duy nhất để vừa tìm kiếm (search / 검색) toàn corpus vừa đánh giá relevance rất tinh. Thay vào đó, kiến trúc (architecture / 아키텍처) phổ biến là **multi-stage ranking**: first-stage retriever tạo candidate set nhanh, sau đó reranker đắt hơn refine thứ tự (order / 순서).

## Candidate Generation

First-stage mục tiêu (objective / 목표) ưu tiên **recall**:

```text
millions of chunks
→ retrieve top 50–200 candidates
```

Sparse, dense hoặc hybrid retrievers phù hợp vì tìm kiếm (search / 검색) nhanh.

Nếu correct bằng chứng (evidence / 증거) không xuất hiện trong candidates, reranker phía sau không thể cứu.

## Reranking

Reranker score truy vấn (query / 쿼리) và candidate với tương tác (interaction / 상호작용) sâu hơn.

Cross-encoder:

```text
[query ; chunk] → Transformer → relevance score
```

Nó đọc truy vấn (query / 쿼리) và chunk cùng lúc nên hiểu fine-grained match tốt hơn bi-encoder.

Chi phí (cost / 비용) gần proportional số candidates × document length, vì vậy chỉ dùng sau first-stage retrieval.

## Relevance Types

Reranker cần học distinction:

```text
topical relevance
answer relevance
freshness
authority
user scope
```

Một document cùng topic nhưng old phiên bản (version / 버전) không nên rank cao hơn hiện tại (current / 현재) authoritative document.

Some factors tốt hơn xử lý tường minh (explicit / 명시적) siêu dữ liệu (metadata / 메타데이터)/nghiệp vụ (business / 비즈니스) rules thay vì learned reranker.

## Hybrid Fusion

Sparse/dense kết quả (result / 결과) sets có thể merge bằng RRF hoặc learned fusion.

Example:

```text
BM25 top 50
Dense top 50
→ union
→ reranker
→ top 8 context chunks
```

Union increases recall; reranker resolves conflicts.

## Truy vấn (query / 쿼리) Rewriting

Before retrieval, truy vấn (query / 쿼리) có thể được rewrite để:

- resolve pronouns/lịch sử (history / 이력);
- expand abbreviations;
- translate ngôn ngữ (language / 언어);
- decompose multi-part question.

Rewrite itself must be evaluated because it can remove important qualifiers.

## Truy vấn (query / 쿼리) Decomposition

Question:

```text
"So sánh phí và điều kiện hủy của gói A và B"
```

có thể decompose:

```text
A fees
A cancellation conditions
B fees
B cancellation conditions
```

Retrieve each subquery then synthesize.

Useful for multi-hop questions.

## Multi-Hop Retrieval

Some questions require bằng chứng (evidence / 증거) chuỗi (chain / 사슬):

```text
entity A → relation → entity B → property of B
```

One-shot truy vấn (query / 쿼리) may not contain terms needed for second hop. Iterative retrieval uses first bằng chứng (evidence / 증거) to formulate next truy vấn (query / 쿼리).

This begins to resemble agentic tìm kiếm (search / 검색).

## Reranker huấn luyện (training / 학습)

Huấn luyện (training / 학습) examples need truy vấn (query / 쿼리), positive chunk và hard negatives. Hard negatives should be plausible but wrong:

```text
same product, wrong version
same policy, wrong country
same topic, missing condition
```

These cases teach fine distinctions relevant môi trường vận hành (production / 운영 환경).

## Rank vs Score Calibration

Reranker score often only meaningful for thứ tự (ordering / 순서) within truy vấn (query / 쿼리), not absolute xác suất (probability / 확률) of relevance.

If using threshold to abstain, calibrate on labeled dữ liệu (data / 데이터).

## Diversification

Top results may all duplicate same paragraph. **Maximal Marginal Relevance (MMR)** balances relevance and diversity:

\[
MMR=\lambda Sim(q,d)-(1-\lambda)\max_{d'\in S}Sim(d,d')
\]

Useful when truy vấn (query / 쿼리) needs multiple aspects.

But diversity can hurt if người dùng (user / 사용자) only needs one chính xác (exact / 정확한) fact.

## Ngữ cảnh (context / 맥락) Selection

After rerank, do not blindly take top-k. ngữ cảnh (context / 맥락) builder may consider:

```text
relevance
source diversity
version/authority
token budget
redundancy
neighbor context
```

This is a constrained selection bài toán (problem / 문제).

## Lost-in-the-Middle tác động (effect / 효과)

LLMs may attend unevenly to long contexts. trọng yếu (critical / 중요) bằng chứng (evidence / 증거) placed among many distractors can be underused.

Ngữ cảnh (context / 맥락) thứ tự (ordering / 순서) matters. dùng chung (common / 공통) patterns place strongest bằng chứng (evidence / 증거) early or group by subquestion.

## Duplicate Suppression

Near-duplicate chunks waste tokens and can độ lệch (bias / 편향) mô hình (model / 모델) as if repeated fact were stronger bằng chứng (evidence / 증거).

Dedup candidate set using content băm (hash / 해시) or ngữ nghĩa (semantic / 의미적) similarity.

## Freshness Boost

For time-sensitive corpora, ranking can combine relevance with freshness:

\[
score = relevance + \alpha \cdot freshness
\]

But newest document is not always authoritative. phiên bản (version / 버전) status is better tín hiệu (signal / 신호) when available.

## Authority Boost

Chính sách (policy / 정책) hierarchy can be tường minh (explicit / 명시적):

```text
official regulation > internal wiki > chat note
```

Encode nguồn (source / 소스) authority siêu dữ liệu (metadata / 메타데이터) rather than hoping embedding mô hình (model / 모델) infer it.

## Reranking chi phí (cost / 비용)

If 100 candidates × 1000 tokens each go through cross-encoder, độ trễ (latency / 지연 시간) may dominate. Options:

```text
reduce candidates
shorten chunks
use smaller reranker
batch scoring
late interaction
cache repeated queries
```

Chất lượng (quality / 품질)/chi phí (cost / 비용) curve must be measured.

## LLM Reranking

LLM can rerank by reading candidate summaries and truy vấn (query / 쿼리). It handles nuanced criteria but is expensive and can be position-biased.

Use when candidate count small and giá trị (value / 값) high, with deterministic thứ tự (ordering / 순서)/IDs.

## Retrieval Confidence

Low top scores or flat score phân phối (distribution / 분포) may indicate no good bằng chứng (evidence / 증거). hệ thống (system / 시스템) can broaden tìm kiếm (search / 검색), fallback lexical, ask clarification or abstain.

This is better than always force answer.

## Offline Evaluation

Need labeled truy vấn (query / 쿼리)→relevant chunk/document pairs. Metrics:

```text
Recall@k
MRR
nDCG
Precision@k
```

Compare stages:

```text
first-stage recall
reranked nDCG
final context recall
```

## Mô hình tư duy (mental model / 사고 모델)

> Retrieval chuỗi xử lý (pipeline / 파이프라인) giống funnel: **wide recall first, precise relevance later, ngữ cảnh (context / 맥락) các ràng buộc (constraints / 제약조건들) cuối**.

## Dùng chung (common / 공통) Misconceptions

### “Reranker có thể sửa retriever bỏ sót bằng chứng (evidence / 증거)”

Không nếu bằng chứng (evidence / 증거) không vào candidate set.

### “Top-k càng lớn càng tốt”

Không. Noise và đơn vị từ (token / 토큰) chi phí (cost / 비용) tăng.

### “Newest = most correct”

Không nếu draft/newer document không authoritative.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Ranking connects IR metrics, cross-encoder NLP, tối ưu hóa (optimization / 최적화) và ngữ cảnh (context / 맥락) kỹ thuật (engineering / 엔지니어링).

Xem tiếp: [Advanced RAG](./08_advanced_rag.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 information retrieval foundations](./00_information_retrieval_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
