# Chunking và Document Processing cho RAG

RAG không search “document” theo nghĩa con người đọc file. Nó search những **retrieval units** đã được tạo trong ingestion pipeline. Cách parse và chunk tài liệu quyết định information nào có thể được retrieve cùng nhau.

## Vì sao phải chunk?

Một PDF 100 trang quá lớn để embed thành one vector hữu ích. Whole-document embedding làm nhiều topics bị average vào cùng representation.

Ngược lại, chunk một câu quá nhỏ có thể mất condition và context.

Chunking giải trade-off:

```text
retrieval precision ↔ contextual completeness
```

## Fixed-Size Chunking

Cách đơn giản chia theo số characters/tokens, ví dụ 500 tokens với overlap 50.

Ưu điểm: dễ implement, predictable size.

Nhược điểm: có thể cắt giữa table, sentence hoặc logical section.

Fixed chunking là baseline tốt, không phải universal best.

## Sentence/Paragraph Chunking

Split theo sentence/paragraph boundaries giữ language units tự nhiên hơn.

Nhưng paragraph length biến động mạnh. Một legal paragraph có thể 1000+ tokens, trong khi bullet item chỉ vài tokens.

## Structure-Aware Chunking

Dùng heading hierarchy, section, table, list, code block và document layout.

Ví dụ Markdown:

```text
# Refund Policy
## Eligibility
...
## Exceptions
...
```

Mỗi chunk có thể inherit heading path:

```text
Refund Policy > Eligibility
```

Heading context rất valuable cho embedding và final answer.

## Semantic Chunking

Có thể detect topic shift bằng embedding similarity giữa sentences/paragraphs. Khi semantic distance tăng, tạo boundary.

Method này adapt content tốt hơn fixed-size nhưng cost ingestion tăng và threshold khó tune.

## Overlap

Chunk overlap giúp information ở boundary không bị mất.

Nhưng overlap quá nhiều tạo duplicated chunks, tăng index size và làm top-k chứa gần-identical evidence.

Reranker/context dedup cần handle duplicates.

## Parent-Child Chunking

Một strong pattern:

```text
small child chunk → retrieval precision
large parent section → generation context
```

Index small chunks, nhưng khi child match thì return parent/neighbor context.

Điều này tách retrieval granularity khỏi generation granularity.

## Contextual Chunk Enrichment

Một chunk như:

```text
"This must be completed within 7 days."
```

không có meaning nếu missing heading. Có thể enrich:

```text
Document: Account Closure Policy
Section: Identity Verification
Text: This must be completed within 7 days.
```

Embedding enriched representation improves retrieval.

## Tables

Tables là major RAG failure source. Naive PDF extraction có thể flatten column order sai.

Cần preserve:

```text
header
row labels
units
merged cells
footnotes
```

Có thể convert table thành Markdown, JSON records hoặc sentence representations tùy query type.

Nếu user hỏi aggregate across rows, SQL/dataframe tool có thể tốt hơn text RAG.

## PDFs và Layout

PDF stores drawing instructions, không semantic paragraphs. Multi-column, header/footer, page numbers và OCR errors có thể pollute text.

Parsing quality cần visually inspect sample documents. “Text extracted successfully” không có nghĩa reading order đúng.

## OCR

Scanned docs cần OCR. OCR errors ở IDs/numbers đặc biệt dangerous.

Store page image reference hoặc original coordinates để human verify citations khi cần.

## Code Documents

Code nên chunk theo syntactic units:

```text
class
function
method
module
```

Fixed token chunk có thể separate function signature và body.

Include file path, symbol name và language metadata.

## Conversation Data

Chat logs có speaker/turn semantics. Chunking random turns có thể mất question-answer relation.

Conversation RAG nên keep turn pairs/thread structure.

## Versioning

Every chunk should trace to:

```text
source_document_id
source_version
chunker_version
page/section
content_hash
```

Khi source update, delete/reindex đúng chunks.

## Content Hashing

Hash normalized content giúp skip unchanged chunks và detect duplicates.

But metadata changes may still require reindex if filters/citations depend on metadata.

## Deduplication

Near-duplicate documents common in policy repositories. Without dedup, retrieval top-k may return 5 versions same paragraph.

Need distinguish:

```text
exact duplicate
near duplicate
legitimate version history
```

Do not dedup away newer/older version semantics blindly.

## Access Control at Chunk Level

If different sections have different permissions, document-level ACL may be too coarse. Chunk metadata can carry access scope.

Authorization must survive derived artifacts.

## Chunk Size Experiment

Choose chunk size empirically. Build labeled queries and compare retrieval recall/precision for sizes like 200/500/1000 tokens.

No universal “best 512 tokens”. Optimal size depends document structure and question granularity.

## Neighbor Expansion

After retrieving chunk `i`, include `i-1`, `i+1` when context continuity matters.

This improves completeness but consumes token budget.

## Heading Injection vs Raw Text

Embedding may include heading, but final evidence should avoid repeated heading noise. Store separate fields:

```text
embedding_text
raw_display_text
metadata
```

This allows retrieval representation differ from user-facing citation.

## Query-Aware Context Extraction

Instead of sending whole chunk, another model can extract only sentences relevant to query. This reduces tokens but creates a new failure point: extractor may remove crucial exception.

Use for very long chunks with evaluation.

## Chunking and Economics

Smaller chunks mean more vectors:

```text
index size ↑
embedding cost ↑
retrieval candidates ↑
```

Larger chunks mean generation token cost ↑.

Chunking is both quality and infrastructure decision.

## Mental Model

> Chunking quyết định **atomic unit của knowledge retrieval**. Nếu unit sai, retriever/model phía sau phải giải bài toán đã bị mất structure từ ingestion.

## Common Misconceptions

### “Overlap càng nhiều càng an toàn”

Không. Duplication làm ranking/context waste.

### “PDF text extraction là solved problem”

Không với layout phức tạp, scanned docs và tables.

### “Một chunk size dùng được mọi document type”

Không. Code, policy, tables và conversations có structure khác nhau.

## Knowledge Connection

Chunking nối document parsing/data engineering với retrieval. Tiếp theo [Retrieval, Ranking and Reranking](./07_retrieval_ranking_and_reranking.md).