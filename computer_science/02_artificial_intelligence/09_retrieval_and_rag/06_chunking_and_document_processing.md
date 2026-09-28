# Chunking và Document Processing cho RAG

> **Mạch đọc:** Đặt **Chunking và Document Processing cho RAG** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao phải chunk?** sang **Fixed-Size Chunking**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


RAG không tìm kiếm (search / 검색) “document” theo nghĩa con người đọc tệp (file / 파일). Nó tìm kiếm (search / 검색) những **retrieval units** đã được tạo trong ingestion chuỗi xử lý (pipeline / 파이프라인). Cách parse và chunk tài liệu quyết định thông tin (information / 정보) nào có thể được retrieve cùng nhau.

## Vì sao phải chunk?

Một PDF 100 trang quá lớn để embed thành one véc-tơ (vector / 벡터) hữu ích. Whole-document embedding làm nhiều topics bị average vào cùng biểu diễn (representation / 표현).

Ngược lại, chunk một câu quá nhỏ có thể mất điều kiện (condition / 조건) và ngữ cảnh (context / 맥락).

Chunking giải sự đánh đổi (trade-off / 트레이드오프):

```text
retrieval precision ↔ contextual completeness
```

## Fixed-Size Chunking

Cách đơn giản chia theo số characters/tokens, ví dụ 500 tokens với overlap 50.

Ưu điểm: dễ implement, predictable kích thước (size / 크기).

Nhược điểm: có thể cắt giữa bảng (table / 테이블), sentence hoặc logical section.

Fixed chunking là baseline tốt, không phải universal best.

## Sentence/Paragraph Chunking

Split theo sentence/paragraph boundaries giữ ngôn ngữ (language / 언어) units tự nhiên hơn.

Nhưng paragraph length biến động mạnh. Một legal paragraph có thể 1000+ tokens, trong khi bullet item chỉ vài tokens.

## Structure-Aware Chunking

Dùng heading hierarchy, section, bảng (table / 테이블), danh sách (list / 목록), mã (code / 코드) khối (block / 블록) và document bố cục (layout / 레이아웃).

Ví dụ Markdown:

```text
# Refund Policy
## Eligibility
...
## Exceptions
...
```

Mỗi chunk có thể inherit heading đường dẫn (path / 경로):

```text
Refund Policy > Eligibility
```

Heading ngữ cảnh (context / 맥락) rất valuable cho embedding và final answer.

## Ngữ nghĩa (semantic / 의미적) Chunking

Có thể detect topic shift bằng embedding similarity giữa sentences/paragraphs. Khi ngữ nghĩa (semantic / 의미적) distance tăng, tạo ranh giới (boundary / 경계).

Phương thức (method / 메서드) này adapt content tốt hơn fixed-size nhưng chi phí (cost / 비용) ingestion tăng và threshold khó tune.

## Overlap

Chunk overlap giúp thông tin (information / 정보) ở ranh giới (boundary / 경계) không bị mất.

Nhưng overlap quá nhiều tạo duplicated chunks, tăng chỉ mục (index / 인덱스) kích thước (size / 크기) và làm top-k chứa gần-identical bằng chứng (evidence / 증거).

Reranker/ngữ cảnh (context / 맥락) dedup cần handle duplicates.

## Parent-Child Chunking

Một strong mẫu (pattern / 패턴):

```text
small child chunk → retrieval precision
large parent section → generation context
```

Chỉ mục (index / 인덱스) small chunks, nhưng khi child match thì return parent/neighbor ngữ cảnh (context / 맥락).

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

Embedding enriched biểu diễn (representation / 표현) improves retrieval.

## Tables

Tables là major RAG thất bại (failure / 실패) nguồn (source / 소스). Naive PDF extraction có thể flatten column thứ tự (order / 순서) sai.

Cần preserve:

```text
header
row labels
units
merged cells
footnotes
```

Có thể convert bảng (table / 테이블) thành Markdown, JSON records hoặc sentence representations tùy truy vấn (query / 쿼리) kiểu (type / 타입).

Nếu người dùng (user / 사용자) hỏi aggregate across rows, SQL/dataframe công cụ (tool / 도구) có thể tốt hơn văn bản (text / 텍스트) RAG.

## PDFs và bố cục (layout / 레이아웃)

PDF stores drawing instructions, không ngữ nghĩa (semantic / 의미적) paragraphs. Multi-column, header/footer, page numbers và OCR errors có thể pollute văn bản (text / 텍스트).

Parsing chất lượng (quality / 품질) cần visually inspect mẫu (sample / 표본) documents. “văn bản (text / 텍스트) extracted successfully” không có nghĩa reading thứ tự (order / 순서) đúng.

## OCR

Scanned docs cần OCR. OCR errors ở IDs/numbers đặc biệt dangerous.

Store page ảnh (image / 이미지) tham chiếu (reference / 참조) hoặc original coordinates để human verify citations khi cần.

## Mã (code / 코드) Documents

Mã (code / 코드) nên chunk theo syntactic units:

```text
class
function
method
module
```

Fixed đơn vị từ (token / 토큰) chunk có thể separate hàm (function / 함수) signature và body.

Include tệp (file / 파일) đường dẫn (path / 경로), symbol name và ngôn ngữ (language / 언어) siêu dữ liệu (metadata / 메타데이터).

## Conversation dữ liệu (data / 데이터)

Chat logs có speaker/turn ngữ nghĩa (semantics / 의미론). Chunking random turns có thể mất question-answer quan hệ (relation / 관계).

Conversation RAG nên keep turn pairs/luồng thực thi (thread / 스레드) cấu trúc (structure / 구조).

## Versioning

Every chunk should dấu vết (trace / 추적) to:

```text
source_document_id
source_version
chunker_version
page/section
content_hash
```

Khi nguồn (source / 소스) cập nhật (update / 업데이트), delete/reindex đúng chunks.

## Content Hashing

Băm (hash / 해시) normalized content giúp skip unchanged chunks và detect duplicates.

But siêu dữ liệu (metadata / 메타데이터) changes may still require reindex if filters/citations depend on siêu dữ liệu (metadata / 메타데이터).

## Deduplication

Near-duplicate documents dùng chung (common / 공통) in chính sách (policy / 정책) repositories. Without dedup, retrieval top-k may return 5 versions same paragraph.

Need distinguish:

```text
exact duplicate
near duplicate
legitimate version history
```

Do not dedup away newer/older phiên bản (version / 버전) ngữ nghĩa (semantics / 의미론) blindly.

## Kiểm soát truy cập (access control / 접근 제어) at Chunk mức (level / 수준)

If different sections have different permissions, document-level ACL may be too coarse. Chunk siêu dữ liệu (metadata / 메타데이터) can carry truy cập (access / 접근) phạm vi (scope / 범위).

Authorization must survive derived artifacts.

## Chunk kích thước (size / 크기) Experiment

Choose chunk kích thước (size / 크기) empirically. bản dựng (build / 빌드) labeled queries and compare retrieval recall/precision for sizes like 200/500/1000 tokens.

No universal “best 512 tokens”. Optimal kích thước (size / 크기) depends document cấu trúc (structure / 구조) and question granularity.

## Neighbor Expansion

After retrieving chunk `i`, include `i-1`, `i+1` when ngữ cảnh (context / 맥락) continuity matters.

This improves completeness but consumes đơn vị từ (token / 토큰) ngân sách (budget / 예산).

## Heading Injection vs Raw văn bản (text / 텍스트)

Embedding may include heading, but final bằng chứng (evidence / 증거) should avoid repeated heading noise. Store separate fields:

```text
embedding_text
raw_display_text
metadata
```

This allows retrieval biểu diễn (representation / 표현) differ from user-facing citation.

## Query-Aware ngữ cảnh (context / 맥락) Extraction

Instead of sending whole chunk, another mô hình (model / 모델) can extract only sentences relevant to truy vấn (query / 쿼리). This reduces tokens but creates a new thất bại (failure / 실패) điểm (point / 지점): extractor may remove crucial exception.

Use for very long chunks with evaluation.

## Chunking and Economics

Smaller chunks mean more vectors:

```text
index size ↑
embedding cost ↑
retrieval candidates ↑
```

Larger chunks mean generation đơn vị từ (token / 토큰) chi phí (cost / 비용) ↑.

Chunking is both chất lượng (quality / 품질) and hạ tầng (infrastructure / 인프라) quyết định (decision / 결정).

## Mô hình tư duy (mental model / 사고 모델)

> Chunking quyết định **atomic đơn vị (unit / 단위) của kiến thức (knowledge / 지식) retrieval**. Nếu đơn vị (unit / 단위) sai, retriever/mô hình (model / 모델) phía sau phải giải bài toán đã bị mất cấu trúc (structure / 구조) từ ingestion.

## Dùng chung (common / 공통) Misconceptions

### “Overlap càng nhiều càng an toàn”

Không. Duplication làm ranking/ngữ cảnh (context / 맥락) waste.

### “PDF văn bản (text / 텍스트) extraction là solved bài toán (problem / 문제)”

Không với bố cục (layout / 레이아웃) phức tạp, scanned docs và tables.

### “Một chunk kích thước (size / 크기) dùng được mọi document kiểu (type / 타입)”

Không. mã (code / 코드), chính sách (policy / 정책), tables và conversations có cấu trúc (structure / 구조) khác nhau.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Chunking nối document parsing/kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) với retrieval. Tiếp theo [Retrieval, Ranking and Reranking](./07_retrieval_ranking_and_reranking.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 information retrieval foundations](./00_information_retrieval_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
