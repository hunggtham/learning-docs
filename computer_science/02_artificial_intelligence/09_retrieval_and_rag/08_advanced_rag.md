# Các mẫu Advanced RAG

RAG cơ bản dùng một query, một lượt retrieval và một bước generation. Workload thực tế thường cần cấu trúc phong phú hơn: câu hỏi mơ hồ, bằng chứng nhiều bước, dữ liệu dị thể, tài liệu thay đổi và yêu cầu độ tin cậy cao. **Advanced RAG** không phải một thuật toán duy nhất; nó là tập hợp các mẫu kiến trúc nhằm cải thiện retrieval, chọn bằng chứng và kiểm soát generation.

## Viết lại Query

Đầu vào hội thoại có thể thiếu thông tin nếu tách khỏi lịch sử:

```text
"còn phí của gói kia thì sao?"
```

Một rewrite model có thể dùng lịch sử để tạo query độc lập. Hệ thống tốt nên giữ nguyên ý định ban đầu và log cả hai dạng.

Bản rewrite không nên âm thầm thêm fact không có trong cuộc trò chuyện.

## Mở rộng Query

Có thể sinh synonym, alias hoặc nhiều cách diễn đạt ngữ nghĩa để tăng recall.

Ví dụ:

```text
"hủy hợp đồng"
→ cancellation
→ contract termination
→ 해지
```

Sau đó hợp nhất kết quả từ các query đã mở rộng. Rủi ro là **trôi chủ đề (topic drift)**, vì vậy expansion nên được giới hạn bằng domain dictionary hoặc reranking.

## Multi-Query Retrieval

Với câu hỏi phức tạp, có thể tạo nhiều query liên quan rồi hợp nhất kết quả. Cách này hữu ích khi một embedding duy nhất không biểu diễn tốt mọi khía cạnh.

```text
câu hỏi người dùng
→ query A
→ query B
→ query C
→ retrieve từng query
→ hợp nhất / rerank
```

## HyDE

**Hypothetical Document Embeddings (HyDE)** tạo một câu trả lời hoặc document giả định từ query, embedding văn bản đó rồi tìm document thật nằm gần nó.

Trực giác là một đoạn giả định dài có thể nằm gần tài liệu relevant hơn query ngắn.

Rủi ro là văn bản giả định có thể đưa thêm assumption sai và làm retrieval lệch hướng. HyDE phải được đánh giá thực nghiệm, không nên mặc định dùng.

## Parent–Child Retrieval

Index child chunk nhỏ để search chính xác, sau đó trả parent context lớn hơn cho generation:

```text
chunk nhỏ tìm đúng điểm cần thiết
→ parent section cung cấp điều kiện xung quanh
```

Mẫu này đặc biệt hữu ích với manual và policy.

## Multi-Vector Retrieval

Một document có thể có nhiều representation:

```text
embedding của raw chunk
embedding của summary
embedding của title
embedding của các câu hỏi mà chunk có thể trả lời
```

Hệ thống có thể retrieve theo bất kỳ representation nào nhưng vẫn trả về source text gốc.

Cách này tách **biểu diễn phục vụ tìm kiếm** khỏi **biểu diễn làm bằng chứng**.

## Summary Index

Với document rất dài, có thể xây hệ thống summary phân cấp:

```text
summary toàn document
summary theo section
leaf chunk
```

Retriever trước tiên route tới document hoặc section liên quan rồi mới search cục bộ.

Cách này giảm search space và hỗ trợ câu hỏi tổng quát.

## Retrieval phân cấp

Corpus có thể tổ chức như:

```text
organization
→ product
→ document
→ section
→ chunk
```

Query được route ở tầng cao trước rồi retrieval ở tầng thấp.

Sai route trở thành failure mode mới, vì vậy nên có fallback global search.

## Routing theo Metadata

Trước semantic search, hệ thống có thể trích constraint có cấu trúc:

```text
language=ko
product=eKYC
country=KR
version=current
```

LLM có thể đề xuất filter, nhưng application phải validate giá trị theo schema được phép.

## Multi-Hop Retrieval

Một số câu trả lời cần chuỗi nguồn:

```text
Policy nào áp dụng cho product X?
→ retrieve định nghĩa product
→ tìm ra policy ID
→ retrieve các clause của policy
```

Controller lặp có thể dùng evidence trung gian để tạo query tiếp theo.

Khi đó kiến trúc bắt đầu giao thoa với Agent.

## Graph RAG

Khi quan hệ giữa entity quan trọng, hệ thống có thể xây graph hoặc Knowledge Graph rồi kết hợp graph traversal với text retrieval.

Phù hợp với:

```text
quan hệ tổ chức
chuỗi dependency
quy định và clause
mạng lưới entity
```

Graph RAG có giá trị khi cấu trúc quan hệ thực sự rõ; graph không tự động tốt hơn vector retrieval.

## SQL + RAG

Dữ liệu có cấu trúc thường nên được query bằng SQL, còn phần giải thích không cấu trúc lấy từ text retrieval.

Ví dụ:

```text
SQL → giá trị transaction hiện tại
RAG → policy / giải thích
LLM → tổng hợp
```

Không nên embedding bảng rồi kỳ vọng vector search thực hiện aggregate chính xác.

## RAG có công cụ hỗ trợ

Retriever có thể chỉ là một tool trong nhiều tool:

```text
web search
internal docs
SQL
API
code search
```

Router chọn nguồn dữ liệu theo loại câu hỏi. Cách này robust hơn một vector index dùng cho mọi thứ.

## Corrective RAG

Sau retrieval, hệ thống đánh giá evidence có đủ và relevant không. Nếu không, có thể:

```text
rewrite query
mở rộng search
đổi retriever
search web
hỏi làm rõ
abstain
```

Vòng sửa giúp tránh ép mô hình trả lời khi evidence yếu.

## Mẫu Self-RAG

Mô hình có thể quyết định khi nào cần retrieval và tự đánh giá claim có được support không.

Tuy nhiên self-evaluation vẫn mang tính xác suất; external evidence check vẫn có giá trị.

## Adaptive Retrieval

Không phải query nào cũng cần retrieval. Chào hỏi đơn giản hoặc tác vụ transform thuần túy có thể bỏ qua search.

Router có thể dự đoán:

```text
có cần retrieval không?
nguồn nào?
bao nhiêu kết quả?
```

Cách này giảm latency/cost nhưng sai route có thể làm mất tri thức cần thiết.

## Phân loại Query

Có thể phân query thành:

```text
exact lookup
policy QA
comparison
multi-hop
calculation
current data
```

Mỗi loại dùng chiến lược retrieval khác nhau.

## Nén Context

Chunk sau rerank có thể được nén thành excerpt liên quan query. Điều này giảm token nhưng thêm rủi ro extractor làm mất ngoại lệ quan trọng.

Nên giữ source reference để người dùng có thể mở context đầy đủ.

## Evidence Graph

Với câu trả lời từ nhiều nguồn, có thể tạo mapping rõ:

```text
claim A ← source 1
claim B ← source 2 + source 3
```

Cách này cải thiện citation và verification.

## Giải quyết nguồn mâu thuẫn

Nếu hai nguồn bất đồng, mô hình không nên tự “lấy trung bình”. Hãy dùng metadata:

```text
version
date
authority
status
jurisdiction
```

Hệ thống đôi khi nên trình bày xung đột thay vì bịa một câu trả lời duy nhất.

## Temporal RAG

Corpus nhạy thời gian cần lọc theo khoảng hiệu lực. Query phải lấy source hợp lệ tại thời điểm được hỏi, không chỉ source mới nhất.

Ví dụ:

```text
"policy as of 2025-12-01"
```

cần metadata về khoảng thời gian có hiệu lực.

## Personalized RAG

Retrieval có thể dùng profile, quyền và preference của user. Tuy nhiên personalization không được làm rò dữ liệu chéo người dùng.

Phải tách tín hiệu personalization khỏi logic authorization.

## Caching

Có thể cache query embedding, retrieval result hoặc final answer. Cache key cần bao gồm:

```text
query
user / tenant scope
index version
source version
model / prompt version
```

Nếu thiếu, hệ thống có thể trả dữ liệu lỗi thời hoặc rò thông tin giữa user.

## Observability

Advanced RAG cần trace đầy đủ:

```text
query gốc
query đã rewrite
filter
ID và score retrieval
reranker score
context được chọn
citation
output cuối
```

Không có trace, việc debug “LLM trả lời sai” dễ biến thành đoán mò.

## Mô hình tư duy

> Advanced RAG là **điều phối retrieval dưới bất định**. Chỉ nên thêm độ phức tạp khi một failure mode đã được đo cho thấy cần nó.

## Những hiểu lầm thường gặp

### “Advanced RAG nghĩa là phải thêm agent framework”

Không. Nhiều cải tiến chỉ là kiến trúc retrieval và ranking xác định.

### “Graph RAG luôn tốt hơn vector RAG”

Không. Nó phụ thuộc cấu trúc quan hệ và loại query.

### “Càng nhiều vòng retrieval càng tốt”

Không. Nhiều call hơn làm tăng latency, drift và cost.

## Liên kết kiến thức

Advanced RAG là cầu nối từ retrieval pipeline sang [Agents](../10_agents_and_ai_systems/00_from_llm_to_agent.md).

Xem tiếp: [RAG Evaluation](./09_rag_evaluation.md).