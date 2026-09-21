# Embedding và không gian ngữ nghĩa trong hệ thống LLM

“Embedding” trong bối cảnh LLM có ít nhất ba nghĩa cần tách biệt: **embedding token đầu vào (input token embedding)**, **trạng thái ẩn theo ngữ cảnh (contextual hidden state)** và **đầu ra của mô hình embedding bên ngoài dùng cho truy xuất hoặc đo tương đồng**. Cả ba đều là vector nhưng được tối ưu cho mục tiêu khác nhau.

Nếu trộn ba khái niệm này, ta dễ nghĩ cơ sở dữ liệu vector đang lưu “suy nghĩ của LLM” hoặc embedding token chính là embedding ngữ nghĩa của cả câu. Hai cách hiểu đó đều không chính xác.

## Embedding token đầu vào

Token ID được ánh xạ tới một hàng trong ma trận:

\[
x_t=E[token_t]
\]

với `E∈R^{V×d_model}` được huấn luyện cùng mô hình ngôn ngữ.

Vector này là biểu diễn ban đầu không phụ thuộc ngữ cảnh. Quá trình đưa ngữ cảnh vào biểu diễn xảy ra qua các layer Transformer.

## Trạng thái ẩn theo ngữ cảnh

Sau layer `l`:

\[
h_t^{(l)}=TransformerLayer_l(...)
\]

trạng thái của token phụ thuộc những token khác mà attention được phép nhìn thấy. Cùng một token có thể có vector ẩn khác nhau trong các context khác nhau.

Các trạng thái ẩn nội bộ được tối ưu chủ yếu cho mục tiêu của mô hình ngôn ngữ, không mặc định được tối ưu cho tìm kiếm câu bằng cosine similarity.

## Chiếu ngược ra từ vựng

Trạng thái ẩn cuối được ánh xạ thành logit của vocabulary:

\[
z=W_Uh_t
\]

Nhiều kiến trúc dùng **chia sẻ trọng số (weight tying)** với `W_U=E^T`, nhưng đây không phải quy tắc bắt buộc.

Tích vô hướng giữa trạng thái ẩn và vector đầu ra của token tạo điểm tương thích trước softmax. Điều này tạo quan hệ hình học giữa không gian ẩn và từ vựng, nhưng hành vi cuối cùng vẫn là kết quả của toàn bộ chuỗi layer và context.

## Mô hình embedding bên ngoài

Mô hình truy xuất thường ánh xạ cả query, document hoặc chunk:

\[
f(text)\rightarrow z\in R^d
\]

và được huấn luyện bằng mục tiêu contrastive hoặc retrieval để độ tương đồng vector phản ánh mức liên quan ngữ nghĩa.

Trạng thái ẩn cuối của một chat LLM không tự động là embedding truy xuất tốt. Mô hình embedding chuyên dụng thường vừa tốt hơn cho retrieval vừa rẻ hơn.

## Không gian ngữ nghĩa không phải từ điển các concept

Một vector không có ý nghĩa độc lập với mô hình và objective. Nếu xoay toàn bộ không gian embedding bằng một phép biến đổi bảo toàn tích vô hướng, hành vi dựa trên khoảng cách có thể không đổi. Vì vậy từng chiều riêng lẻ không phải một “trục ngữ nghĩa” cố định.

Ý nghĩa chủ yếu nằm trong quan hệ giữa các vector, subspace và phép tính phía sau.

## Cosine similarity và dot product

Nếu vector đã chuẩn hóa:

\[
q^Td=cos(q,d)
\]

Nếu chưa chuẩn hóa, dot product còn chịu ảnh hưởng độ lớn vector. Một số mô hình có thể sử dụng norm như một phần tín hiệu. Do đó metric trong vector database phải phù hợp với cách mô hình embedding được huấn luyện và khuyến nghị sử dụng.

## Embedding có thể cắt ngắn

Một số mô hình dùng **Matryoshka Representation Learning** để phần prefix của vector vẫn giữ thông tin hữu ích. Ví dụ có thể giảm từ 1024 xuống 256 chiều với suy giảm chất lượng có kiểm soát.

Lợi ích là giảm dung lượng lưu trữ và tăng tốc ANN. Tuy nhiên tính chất này phải được huấn luyện và đánh giá; cắt tùy ý embedding thông thường có thể phá hỏng chất lượng.

## Đánh đổi số chiều embedding

Số chiều cao hơn tăng khả năng biểu diễn nhưng cũng tăng:

- dung lượng lưu trữ;
- băng thông bộ nhớ;
- kích thước chỉ mục ANN;
- độ trễ truy xuất;
- độ phức tạp của hệ thống.

Sau một mức nhất định, tăng chiều có thể chỉ cải thiện nhỏ. Cần đánh giá trên corpus thật.

## Chuẩn hóa và lượng tử hóa embedding

Kho vector lớn có thể lưu bằng FP16, int8 hoặc mã product quantization để giảm bộ nhớ. Đổi lại recall của ANN có thể giảm.

Lượng tử hóa embedding/index khác với lượng tử hóa trọng số LLM, dù cùng dựa trên nguyên lý xấp xỉ số.

## Pipeline tìm kiếm ngữ nghĩa

```text
Tài liệu
→ chia đoạn
→ embedding
→ index vector + metadata

Query
→ embedding bằng mô hình tương thích
→ ANN search
→ filter / rerank
```

Không nên trộn vector sinh bởi các phiên bản embedding khác nhau trong cùng không gian nếu chưa chứng minh chúng tương thích.

## Truy xuất bất đối xứng

Vai trò query và document khác nhau. Một số mô hình yêu cầu prefix tác vụ như:

```text
query: ...
passage: ...
```

hoặc dùng encoder/projection khác nhau cho hai phía. Bỏ prefix yêu cầu có thể làm chất lượng giảm đáng kể.

## Tìm kiếm lai

Dense embedding đôi khi yếu với ID chính xác, tên riêng, số hoặc từ khóa hiếm. BM25 và sparse retrieval lại mạnh ở khớp từ chính xác.

**Tìm kiếm lai (hybrid search)** kết hợp sparse và dense signal, đặc biệt hữu ích với mã nguồn, tài liệu sản phẩm, pháp lý hoặc corpus doanh nghiệp.

## Tinh chỉnh embedding

Cặp dương và âm theo domain có thể điều chỉnh geometry của không gian.

Ví dụ hard negative:

```text
query: đặt lại PIN thẻ doanh nghiệp
negative: đặt lại mật khẩu ngân hàng cá nhân
```

Hai câu gần về ngữ nghĩa chung nhưng khác tác vụ, buộc mô hình học ranh giới tinh hơn. Cần kiểm soát **false negative** để không đẩy xa những tài liệu thực sự liên quan.

## Embedding và quyền riêng tư

Vector không được đảm bảo là dữ liệu ẩn danh. Các tấn công có thể suy ra thuộc tính, membership hoặc một phần nội dung nguồn tùy mô hình và mức truy cập.

Không nên công khai vector store chỉ vì “nó chỉ chứa số”. Kiểm soát truy cập, mã hóa và chính sách dữ liệu vẫn cần thiết.

## Đảo ngược embedding

Nghiên cứu đã cho thấy trong một số điều kiện có thể tái tạo hoặc suy luận đặc điểm của dữ liệu nguồn từ embedding. Khả năng cụ thể phụ thuộc mô hình và threat model, nhưng nguyên tắc an toàn là coi embedding tạo từ dữ liệu nhạy cảm cũng là dữ liệu nhạy cảm dẫn xuất.

## Bộ nhớ LLM và bộ nhớ vector

Ứng dụng có thể lưu note hoặc sự kiện cũ dưới dạng văn bản + embedding rồi truy xuất về sau. Vector database là hệ thống bộ nhớ ngoài; trọng số LLM không thay đổi chỉ vì ta thêm một bản ghi.

```text
hội thoại / sự kiện
→ bản ghi văn bản
→ embedding / index

query tương lai
→ truy xuất bản ghi
→ đưa vào context
→ LLM
```

Sự phân biệt này tránh cách nói nhân hóa như “LLM đã nhớ vĩnh viễn” khi thực tế ứng dụng chỉ lưu bộ nhớ ngoài.

## Knowledge Graph và embedding

Knowledge Graph lưu entity và relation rõ ràng; embedding hỗ trợ truy xuất mờ theo ngữ nghĩa. Hệ thống kiểu GraphRAG có thể kết hợp neighborhood từ graph với passage truy xuất bằng vector.

Quan hệ tường minh và độ tương đồng dense bổ sung cho nhau.

## Mô hình tư duy

```text
Token embedding
= mã học được ban đầu cho danh tính token

Contextual hidden state
= biểu diễn token sau khi tính toán với ngữ cảnh

Retrieval embedding
= biểu diễn văn bản được huấn luyện để khoảng cách phục vụ truy xuất
```

Tất cả đều là vector, nhưng mục đích của vector đến từ objective đã tạo ra nó.

## Những hiểu lầm thường gặp

### “Có thể lấy bất kỳ hidden state nào của LLM đưa vào vector DB để semantic search”

Có thể về mặt kỹ thuật, nhưng không đảm bảo hiệu quả. Objective truy xuất chuyên dụng rất quan trọng.

### “Khoảng cách vector là xác suất liên quan”

Không. Nếu cần xác suất, điểm similarity phải được hiệu chỉnh và kiểm chứng thực nghiệm.

### “Embedding loại bỏ tính nhạy cảm của văn bản”

Không. Hãy coi embedding dẫn xuất từ dữ liệu nhạy cảm là dữ liệu cần bảo vệ.

### “Embedding càng nhiều chiều thì RAG càng tốt”

Luôn có đánh đổi giữa chất lượng, lưu trữ và ANN. Trong thực tế lỗi retrieval còn thường bị chi phối bởi chunking, dữ liệu và reranking hơn là chỉ số chiều.

## Liên kết kiến thức

Xem [Contextual Embeddings](../07_natural_language_processing/04_contextual_embeddings.md), [Information Retrieval](../07_natural_language_processing/08_search_and_information_retrieval.md) và layer [Retrieval & RAG](../09_retrieval_and_rag/).