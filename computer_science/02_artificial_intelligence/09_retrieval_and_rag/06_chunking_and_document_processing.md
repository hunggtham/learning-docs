# Chunking và xử lý tài liệu cho RAG

RAG không tìm kiếm “document” theo đúng cách con người đọc một file. Nó tìm những **đơn vị truy xuất (retrieval units)** đã được tạo trong pipeline ingestion. Cách parse và chunk tài liệu quyết định thông tin nào có thể được retrieve cùng nhau.

## Vì sao phải chunk?

Một PDF 100 trang quá lớn để biến thành một vector duy nhất có ý nghĩa. Embedding cả document làm nhiều chủ đề bị trộn trung bình vào cùng representation.

Ngược lại, chunk chỉ một câu có thể quá nhỏ và làm mất điều kiện hoặc context.

Chunking giải bài toán đánh đổi:

```text
độ chính xác khi truy xuất ↔ mức đầy đủ của context
```

## Chunk theo kích thước cố định

Cách đơn giản là chia theo số ký tự hoặc token, ví dụ 500 token với overlap 50 token.

Ưu điểm: dễ triển khai và kích thước dễ dự đoán.

Nhược điểm: có thể cắt giữa bảng, câu hoặc section logic.

Chunk cố định là baseline tốt, không phải lựa chọn tối ưu cho mọi tài liệu.

## Chunk theo câu hoặc đoạn văn

Chia theo ranh giới câu hoặc paragraph giúp giữ đơn vị ngôn ngữ tự nhiên hơn.

Tuy nhiên độ dài paragraph biến động mạnh. Một đoạn pháp lý có thể vượt 1.000 token, trong khi một bullet chỉ có vài token.

## Chunk theo cấu trúc tài liệu

**Chunk theo cấu trúc (structure-aware chunking)** dùng heading hierarchy, section, table, list, code block và layout.

Ví dụ Markdown:

```text
# Refund Policy
## Eligibility
...
## Exceptions
...
```

Mỗi chunk có thể kế thừa đường dẫn heading:

```text
Refund Policy > Eligibility
```

Heading context rất có giá trị cho embedding và câu trả lời cuối.

## Chunk theo ngữ nghĩa

Có thể phát hiện thay đổi chủ đề bằng similarity giữa embedding của các câu hoặc paragraph. Khi semantic distance tăng đủ mạnh, hệ thống tạo boundary mới.

Cách này thích ứng nội dung tốt hơn fixed-size nhưng làm ingestion tốn kém hơn và threshold khó tune.

## Overlap

Overlap giúp tránh mất thông tin ở ranh giới chunk.

Nhưng overlap quá lớn tạo nhiều chunk trùng, làm index phình to và top-k có thể chứa nhiều evidence gần giống nhau.

Reranker hoặc context dedup cần xử lý duplication này.

## Parent–Child Chunking

Một pattern mạnh là:

```text
child chunk nhỏ → retrieval chính xác
parent section lớn → context đầy đủ cho generation
```

Index child chunk nhỏ, nhưng khi child match thì trả thêm parent hoặc neighbor context.

Cách này tách **độ mịn retrieval** khỏi **độ mịn generation**.

## Bổ sung context cho chunk

Một chunk như:

```text
"This must be completed within 7 days."
```

gần như mất nghĩa nếu thiếu heading. Có thể enrich thành:

```text
Document: Account Closure Policy
Section: Identity Verification
Text: This must be completed within 7 days.
```

Representation đã enrich thường giúp retrieval tốt hơn.

## Bảng

Table là nguồn failure lớn trong RAG. PDF extraction đơn giản có thể làm sai thứ tự cột.

Cần cố giữ:

```text
header
row label
đơn vị
merged cell
footnote
```

Có thể chuyển table sang Markdown, JSON record hoặc câu văn tùy loại query.

Nếu người dùng cần aggregate qua nhiều row, SQL hoặc dataframe tool thường phù hợp hơn text RAG.

## PDF và layout

PDF chủ yếu lưu lệnh vẽ chứ không lưu paragraph theo semantics. Tài liệu nhiều cột, header/footer, page number và OCR error có thể làm text bị nhiễu.

Cần kiểm tra trực quan một số sample. “Extract text thành công” không có nghĩa reading order đã đúng.

## OCR

Tài liệu scan cần OCR. Lỗi OCR ở ID và số đặc biệt nguy hiểm.

Nên lưu page image hoặc tọa độ gốc để người dùng có thể xác minh citation khi cần.

## Tài liệu mã nguồn

Code nên chunk theo đơn vị cú pháp:

```text
class
function
method
module
```

Chunk cố định có thể tách function signature khỏi body.

Nên kèm file path, symbol name và language metadata.

## Dữ liệu hội thoại

Chat log có semantics về speaker và turn. Chunk ngẫu nhiên có thể làm mất quan hệ question–answer.

Conversation RAG nên giữ turn pair hoặc thread structure.

## Versioning

Mỗi chunk nên truy được về:

```text
source_document_id
source_version
chunker_version
page / section
content_hash
```

Khi source thay đổi, hệ thống cần biết chunk nào phải xóa hoặc reindex.

## Content Hash

Hash nội dung đã chuẩn hóa giúp bỏ qua chunk không đổi và phát hiện duplicate.

Tuy nhiên nếu metadata thay đổi, vẫn có thể cần reindex vì filter hoặc citation phụ thuộc metadata.

## Khử trùng lặp

Repository policy thường chứa nhiều tài liệu gần trùng. Nếu không dedup, top-k có thể trả năm version của cùng một paragraph.

Cần phân biệt:

```text
exact duplicate
near duplicate
version history hợp lệ
```

Không nên dedup mù rồi xóa mất semantics của version cũ/mới.

## Kiểm soát truy cập ở cấp chunk

Nếu các section khác nhau có quyền khác nhau, ACL ở document level có thể quá thô. Chunk metadata có thể mang access scope riêng.

Authorization phải được duy trì qua toàn bộ artifact dẫn xuất.

## Thử nghiệm kích thước chunk

Nên chọn chunk size bằng dữ liệu đánh giá. Có thể xây tập query có nhãn rồi so recall/precision giữa 200, 500 và 1.000 token.

Không có “512 token là tốt nhất” cho mọi bài toán. Kích thước phù hợp phụ thuộc cấu trúc tài liệu và độ chi tiết của câu hỏi.

## Mở rộng neighbor

Sau khi retrieve chunk `i`, có thể thêm `i-1`, `i+1` nếu tính liên tục của context quan trọng.

Cách này tăng độ đầy đủ nhưng tiêu tốn token budget.

## Heading cho embedding và text hiển thị

Embedding text có thể thêm heading, nhưng evidence hiển thị cho user không nhất thiết cần lặp heading ở mọi đoạn. Có thể lưu tách:

```text
embedding_text
raw_display_text
metadata
```

Representation dùng cho retrieval nhờ đó có thể khác representation dùng cho citation.

## Trích context theo query

Thay vì gửi toàn bộ chunk, một model khác có thể trích chỉ các câu liên quan. Điều này giảm token nhưng tạo failure point mới: extractor có thể bỏ mất ngoại lệ quan trọng.

Chỉ nên dùng với chunk dài và có evaluation.

## Chunking và kinh tế hạ tầng

Chunk nhỏ làm số vector tăng:

```text
index size ↑
embedding cost ↑
retrieval candidate ↑
```

Chunk lớn làm token generation tăng.

Vì vậy chunking vừa là quyết định chất lượng vừa là quyết định hạ tầng.

## Mô hình tư duy

> Chunking quyết định **đơn vị nguyên tử của tri thức được truy xuất**. Nếu đơn vị này sai, retriever và model phía sau phải xử lý một bài toán đã mất cấu trúc ngay từ ingestion.

## Những hiểu lầm thường gặp

### “Overlap càng nhiều càng an toàn”

Không. Duplication làm lãng phí ranking và context.

### “PDF text extraction đã là bài toán giải xong”

Không với layout phức tạp, scan và table.

### “Một chunk size dùng được cho mọi loại tài liệu”

Không. Code, policy, table và conversation có cấu trúc khác nhau.

## Liên kết kiến thức

Chunking nối document parsing và data engineering với retrieval.

Xem tiếp: [Retrieval, Ranking and Reranking](./07_retrieval_ranking_and_reranking.md).