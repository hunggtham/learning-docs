# Contextual Embedding: ý nghĩa thay đổi theo ngữ cảnh

Word embedding tĩnh gán một vector duy nhất cho mỗi từ hoặc loại token. Nhưng ngôn ngữ có hiện tượng đa nghĩa và ý nghĩa phụ thuộc ngữ cảnh: `bank` trong `river bank` khác `bank loan`. **Embedding theo ngữ cảnh (Contextual Embedding / 문맥 임베딩)** tính biểu diễn của token như một hàm của toàn bộ ngữ cảnh xung quanh.

Transformer thực hiện điều này bằng self-attention: token ban đầu có thể bắt đầu từ cùng một embedding lookup, nhưng qua nhiều layer nó trao đổi thông tin với token gần và xa rồi trở thành hidden state riêng cho ngữ cảnh hiện tại.

## Static và Contextual Embedding

Embedding tĩnh:

\[
e(w)=v_w
\]

Embedding theo ngữ cảnh:

\[
h_i=f_\theta(x_1,...,x_T,i)
\]

Cùng token ID ở vị trí hoặc ngữ cảnh khác nhau có thể nhận `h_i` khác nhau.

## ELMo: contextualization bằng mô hình ngôn ngữ hai chiều

ELMo là một cột mốc trước Transformer. Nó dùng nhiều tầng LSTM hai chiều và kết hợp hidden state từ nhiều layer để tạo biểu diễn token.

Ý tưởng quan trọng là các layer khác nhau có thể chứa những loại thông tin ngôn ngữ khác nhau, và biểu diễn phụ thuộc ngữ cảnh giúp cải thiện nhiều tác vụ downstream.

## Biểu diễn trong BERT

BERT dùng Transformer encoder hai chiều và được pretrain bằng masked language modeling.

Đầu vào thường kết hợp embedding token/subword, vị trí và segment/type tùy implementation. Sau mỗi Transformer layer, vector của token được contextualize thêm.

Các hidden state cuối hoặc một số layer được chọn có thể dùng cho phân loại, Question Answering, Named Entity Recognition và nhiều tác vụ khác.

## Biểu diễn Token và biểu diễn Câu

Tác vụ cấp token dùng hidden state của từng token.

Tác vụ cấp câu hoặc tài liệu cần một cơ chế **gộp (pooling)**, ví dụ:

- biểu diễn `[CLS]`;
- mean pooling;
- max pooling;
- attention pooling;
- mô hình sentence embedding được fine-tune riêng.

`[CLS]` thô của BERT không tự động là sentence embedding ngữ nghĩa tốt nhất. Mục tiêu huấn luyện quyết định chất lượng biểu diễn dùng cho similarity.

## Sentence-BERT và Sentence Embedding tương phản

**Cross-encoder** xử lý đồng thời hai văn bản trong cùng Transformer nên có thể học tương tác token rất chi tiết, nhưng không phù hợp để quét toàn bộ corpus vì mỗi cặp query–document cần một forward pass riêng.

**Bi-encoder** mã hóa độc lập:

\[
q=f(qtext),\quad d=g(document)
\]

rồi tính:

\[
s(q,d)=cos(q,d)
\]

Document vector có thể tính trước và lưu trong chỉ mục ANN. Các phương pháp kiểu Sentence-BERT dùng huấn luyện contrastive để biến embedding được pooling thành biểu diễn thích hợp cho similarity hoặc retrieval.

## Bi-Encoder và Cross-Encoder

Bi-encoder:

```text
query → vector ┐
               ├→ độ tương đồng
 doc  → vector ┘
```

Ưu điểm là truy xuất nhanh; hạn chế là mỗi văn bản phải được nén độc lập vào một vector.

Cross-encoder:

```text
[query ; document]
        ↓ Transformer xử lý chung
      điểm relevance
```

Cách này thường chính xác hơn ở cấp cặp nhưng rất tốn chi phí.

Một kiến trúc truy xuất hiện đại phổ biến là:

```text
bi-encoder lấy top K ứng viên
→ cross-encoder xếp hạng lại
```

Đây cũng là kiến trúc nền của nhiều hệ thống RAG.

## Hình học của Contextual Token

Hidden state của một token có thể trộn thông tin từ vựng, cú pháp, ngữ nghĩa và vị trí. Nhiều nghiên cứu probing quan sát thấy các layer khác nhau có xu hướng mã hóa những loại tín hiệu khác nhau, nhưng không nên coi đây là một hierarchy tuyệt đối và sạch.

Việc một probe có thể giải mã một thuộc tính từ hidden state không chứng minh mô hình thực sự sử dụng thuộc tính đó theo quan hệ nhân quả.

## Chọn Layer

Layer cuối được tối ưu gần nhất với mục tiêu pretraining, nhưng layer trung gian có thể tốt hơn cho một số nhiệm vụ ngôn ngữ.

Một số phương pháp ghép hoặc học trọng số trên nhiều layer. Không có quy tắc “layer cuối luôn tốt nhất”.

## Pooling và thiên lệch theo độ dài

Mean pooling lấy trung bình các token nên tài liệu dài có thể làm loãng đoạn nổi bật. `[CLS]` phụ thuộc mạnh vào mục tiêu đã huấn luyện. Max pooling ưu tiên activation lớn nhất ở mỗi chiều.

Với tài liệu dài, embedding theo chunk thường hữu ích hơn ép toàn bộ tài liệu vào một vector duy nhất. Tuy nhiên chunking lại tạo các đánh đổi về ngữ cảnh, ranh giới và provenance.

## Chuẩn hóa Vector

Embedding thường được chuẩn hóa L2:

\[
\hat z=\frac{z}{\|z\|}
\]

Khi đó dot product giữa hai vector đã chuẩn hóa bằng cosine similarity:

\[
\hat q^T\hat d=cos(q,d)
\]

Chỉ mục ANN có thể giả định một metric cụ thể, vì vậy bước preprocessing phải phù hợp với cách mô hình embedding được huấn luyện và khuyến nghị sử dụng.

## Huấn luyện Contrastive

Cặp query–document dương cần có điểm cao hơn các cặp âm. Một loss kiểu InfoNCE:

\[
L_i=-\log\frac{e^{s(q_i,d_i^+)/\tau}}
{e^{s(q_i,d_i^+)/\tau}+\sum_j e^{s(q_i,d_j^-)/\tau}}
\]

Negative sample trong cùng batch giúp tính toán hiệu quả, nhưng **false negative** — tài liệu thực ra liên quan nhưng bị coi là âm — có thể làm hỏng hình học học được.

**Hard negative** là những tài liệu khá giống nhưng không đúng, giúp mô hình học ranh giới relevance tinh hơn.

## Thích ứng theo Domain

Embedding model tổng quát có thể không hiểu tốt thuật ngữ hoặc quan hệ chuyên ngành. Fine-tuning trên cặp query–document của domain có thể cải thiện truy xuất.

Tuy nhiên fine-tuning quá hẹp có thể làm suy giảm khả năng ngữ nghĩa tổng quát. Đánh giá cần dùng tập query đại diện cho tình huống triển khai thật.

## Multilingual Embedding

Encoder đa ngôn ngữ cố đưa các câu tương đương từ nhiều ngôn ngữ vào cùng không gian vector. Khi alignment đủ tốt, có thể thực hiện truy xuất xuyên ngôn ngữ:

```text
query tiếng Việt
→ vector
→ truy xuất tài liệu tiếng Hàn / tiếng Anh
```

Chất lượng alignment không đồng đều giữa ngôn ngữ và domain; hiệu quả tokenizer và mức cân bằng dữ liệu cũng ảnh hưởng lớn.

## Giới hạn Context

Embedding model có context tối đa. Tài liệu dài hơn có thể bị cắt và mất phần cuối mà pipeline không báo rõ nếu không kiểm tra.

Hệ thống production nên tường minh:

```text
đếm token
→ chunk / tóm tắt / mã hóa phân cấp
→ giữ source span và provenance
```

## Embedding Drift và Versioning

Đổi model hoặc phiên bản embedding làm hình học vector thay đổi. Không nên trộn corpus vector được tạo bằng model cũ với query vector của model mới trừ khi đã kiểm chứng tương thích.

Re-embedding và re-indexing có thể tốn chi phí lớn, nên phiên bản mô hình phải được lưu cùng metadata của vector store.

## Tương đồng ngữ nghĩa không đồng nghĩa Relevance

Hai đoạn văn có thể giống về chủ đề nhưng không trả lời đúng intent của query. Relevance còn phụ thuộc mục đích, độ mới, độ tin cậy, quyền truy cập và metadata.

Vì vậy dense embedding thường nên kết hợp lexical search, filter và reranker khi bài toán yêu cầu.

## Mô hình tư duy

> Static embedding hỏi: “ký hiệu này thường liên hệ với điều gì?”. Contextual embedding hỏi: “ký hiệu hoặc đoạn văn này trong ngữ cảnh hiện tại đang biểu diễn điều gì?”.

Với retrieval, sentence embedding thêm một câu hỏi nữa: “nên nén toàn bộ văn bản thành vector nào để độ tương đồng phản ánh đúng mục tiêu relevance?”.

## Những hiểu lầm thường gặp

### “Bất kỳ output nào của BERT cũng dùng làm embedding tìm kiếm tốt”

Không. Hidden state hoặc pooling thô có thể không được huấn luyện cho semantic similarity. Nên dùng mô hình có objective retrieval/sentence embedding phù hợp.

### “Cross-encoder tốt hơn nên dùng cho toàn corpus”

Không thực tế ở quy mô lớn vì chi phí theo từng cặp quá cao. Nó thường được dùng để rerank một tập ứng viên nhỏ.

### “Cosine similarity 0.9 nghĩa tài liệu có 90% xác suất liên quan”

Không. Similarity score không tự động là xác suất đã được calibration.

### “Cùng không gian đa ngôn ngữ nghĩa mọi ngôn ngữ có chất lượng ngang nhau”

Không. Dữ liệu, tokenizer và mức độ đại diện của từng ngôn ngữ tạo chênh lệch đáng kể.

## Liên kết kiến thức

Contextual Embedding kết hợp [Transformer](../06_deep_learning_architectures/05_transformer.md), [Học biểu diễn tương phản](../05_neural_networks/08_representation_learning.md) và chuẩn bị cho [Truy xuất thông tin](./08_search_and_information_retrieval.md), RAG và embedding trong LLM.