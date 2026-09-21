# Word Embedding: từ từ rời rạc tới không gian ngữ nghĩa liên tục

**Nhúng từ (Word Embedding / 단어 임베딩)** ánh xạ các đơn vị từ vựng rời rạc thành vector dày đặc. Trước embedding, biểu diễn one-hot coi mọi từ khác nhau đều không liên quan như nhau. Embedding cho phép mô hình học một không gian hình học trong đó những từ xuất hiện trong ngữ cảnh tương tự có vector liên quan.

Đây là bước chuyển quan trọng từ NLP ký hiệu thưa sang **biểu diễn phân tán (distributed representation)** và là nền trực tiếp của token embedding trong LLM.

## Giới hạn của One-Hot

Giả sử kích thước vocabulary là `V`. Từ thứ `i` được biểu diễn bằng:

\[
e_i\in R^V
\]

với một phần tử bằng `1` và phần còn lại bằng `0`.

Tích vô hướng giữa hai từ khác nhau luôn bằng `0`. Trong hình học này, `cat` không gần `dog` hơn `database`.

Embedding dày đặc:

\[
v_w\in R^d,\quad d\ll V
\]

cho phép mô hình học độ tương đồng từ dữ liệu.

## Giả thuyết phân bố

Một trực giác kinh điển của ngôn ngữ học phân bố là có thể hiểu một từ phần nào qua những từ thường xuất hiện xung quanh nó.

Các phương pháp embedding biến trực giác này thành mục tiêu dựa trên đồng xuất hiện hoặc dự đoán.

Tuy nhiên **tương đồng phân bố (distributional similarity)** không đồng nghĩa hai từ có cùng nghĩa. Từ trái nghĩa như `hot` và `cold` thường xuất hiện trong các ngữ cảnh tương tự nên vector của chúng vẫn có thể gần nhau.

## Word2Vec: Skip-Gram

Với từ trung tâm `w`, Skip-Gram dự đoán các từ ngữ cảnh `c`:

\[
P(c\mid w)=\frac{\exp(v_c'^Tv_w)}{\sum_{j\in V}\exp(v_j'^Tv_w)}
\]

Softmax trên toàn vocabulary rất tốn chi phí khi `V` lớn.

Mục tiêu này buộc vector từ trung tâm chứa thông tin hữu ích để dự đoán những từ thường xuất hiện gần nó.

## CBOW

**Continuous Bag-of-Words (CBOW)** đi theo hướng ngược lại: dùng các từ xung quanh để dự đoán từ trung tâm.

```text
các từ ngữ cảnh
→ tổng hợp embedding
→ dự đoán từ trung tâm
```

CBOW thường nhanh hơn; Skip-Gram từng cho biểu diễn tốt hơn với một số từ hiếm trong các thiết lập cổ điển.

## Negative Sampling

Thay vì tính softmax trên toàn vocabulary, mô hình phân biệt cặp `(word, context)` thật với một số cặp âm được lấy mẫu.

Mục tiêu gần dạng:

\[
\log\sigma(v_c'^Tv_w)
+
\sum_{k=1}^{K}\log\sigma(-v_{n_k}'^Tv_w)
\]

Điều này giảm chi phí tính toán rất mạnh.

Phân bố dùng để lấy negative sample cũng ảnh hưởng hình học cuối cùng của embedding; đây không chỉ là một chi tiết triển khai.

## Liên hệ với PMI

Skip-Gram với negative sampling có liên hệ lý thuyết với việc phân rã một ma trận **Pointwise Mutual Information (PMI)** đã dịch chuyển.

\[
PMI(w,c)=\log\frac{P(w,c)}{P(w)P(c)}
\]

PMI đo mức một cặp xuất hiện cùng nhau nhiều hơn bao nhiêu so với trường hợp hai biến độc lập.

Liên hệ này cho thấy embedding dự đoán neural và các phương pháp ma trận đếm cổ điển không hoàn toàn tách biệt về bản chất.

## GloVe

**GloVe (Global Vectors)** sử dụng trực tiếp thống kê đồng xuất hiện toàn cục. Mô hình học vector sao cho tích vô hướng liên hệ với log của số đếm hoặc tỷ lệ đồng xuất hiện.

Word2Vec nhấn mạnh mục tiêu dự đoán trong ngữ cảnh cục bộ; GloVe nhấn mạnh cấu trúc đếm toàn cục. Cả hai đều tạo **embedding tĩnh (static embedding)** cho mỗi từ.

## Cosine Similarity

\[
cos(a,b)=\frac{a^Tb}{\|a\|\|b\|}
\]

Cosine thường được dùng vì tập trung vào hướng vector thay vì độ lớn. Tuy nhiên metric phù hợp còn phụ thuộc mục tiêu huấn luyện; các mô hình embedding hiện đại có thể được tối ưu trực tiếp cho cosine hoặc dot product.

## Phép tương tự bằng vector

Ví dụ nổi tiếng:

\[
king-man+woman\approx queen
\]

cho thấy một số quan hệ có thể xuất hiện xấp xỉ dưới dạng hướng tuyến tính trong không gian embedding.

Không nên khái quát quá mức. Kết quả phụ thuộc corpus, tiền xử lý và phương pháp học; nhiều quan hệ ngữ nghĩa không thể biểu diễn bằng một offset vector toàn cục đơn giản.

## Giới hạn của Static Embedding: đa nghĩa

`bank` chỉ có một vector Word2Vec dù được dùng trong:

```text
bank loan
river bank
```

Vector tĩnh phải trộn nhiều nghĩa vào cùng một vị trí.

**Embedding theo ngữ cảnh (contextual embedding)** giải quyết phần lớn vấn đề này bằng cách tính biểu diễn phụ thuộc toàn bộ câu hoặc đoạn xung quanh.

## Subword Embedding với fastText

fastText biểu diễn từ từ các n-gram ký tự, giúp xử lý từ hiếm và ngôn ngữ có hình thái phong phú.

Những từ tiếng Hàn, tiếng Việt hoặc các biến thể chia sẻ một phần cấu trúc có thể dùng chung các mảnh subword.

Với từ chưa từng xuất hiện nguyên vẹn, fastText vẫn có thể xây vector từ các n-gram đã biết.

## Embedding Matrix trong mạng nơ-ron

Một embedding layer học được có ma trận:

\[
E\in R^{V\times d}
\]

Token ID chọn một hàng:

\[
x_t=E[token_t]
\]

Về mặt toán học, thao tác này tương đương nhân one-hot:

\[
e_t^TE
\]

nhưng lookup hiệu quả hơn nhiều.

Trong huấn luyện, gradient cập nhật các hàng tương ứng với token xuất hiện và có thể tương tác với các cơ chế chia sẻ trọng số khác.

## Ảnh hưởng của tần suất

Từ phổ biến nhận nhiều cập nhật hơn từ hiếm. Độ lớn và hướng embedding có thể tương quan với tần suất.

Word2Vec thường giảm lấy mẫu các từ cực phổ biến để chúng không chi phối ngữ cảnh.

Thiên lệch xã hội và thống kê trong corpus cũng đi vào hình học embedding, ví dụ liên hệ giữa giới tính và nghề nghiệp.

## Giới hạn của Debiasing đơn giản

Loại bỏ một “hướng giới tính” có thể giảm một chỉ số liên hệ cụ thể nhưng không xóa toàn bộ thiên lệch phân tán trong không gian biểu diễn.

Fairness của embedding cần được đánh giá qua nhiều tác vụ và hành vi downstream chứ không thể giải quyết chỉ bằng một phép chiếu vector.

## Embedding cho tài liệu

Lấy trung bình các word embedding là cách đơn giản để biểu diễn tài liệu nhưng làm mất thứ tự và ngữ cảnh.

Doc2Vec từng mở rộng biểu diễn phân tán lên tài liệu. Hiện nay sentence/document encoder thường dùng Transformer theo ngữ cảnh, pooling và huấn luyện contrastive.

## Embedding và tìm kiếm

Nếu query và document được biểu diễn trong cùng không gian:

\[
score(q,d)=q^Td
\]

nearest-neighbor search có thể tìm tài liệu gần về ngữ nghĩa.

Word embedding tĩnh thường không đủ cho truy xuất hiện đại; sentence embedding được huấn luyện trực tiếp ở cấp query–document phù hợp hơn. Tuy nhiên nguyên lý hình học bắt đầu từ đây.

## Mô hình tư duy

> Embedding biến “danh tính của ký hiệu” thành “vị trí và hướng trong một không gian quan hệ được học”. Hình học chỉ có ý nghĩa vì dữ liệu và mục tiêu huấn luyện đã định hình nó.

## Những hiểu lầm thường gặp

### “Mỗi chiều embedding là một thuộc tính ngữ nghĩa dễ đọc”

Thông thường không. Thông tin được phân tán và hệ trục có thể thay đổi qua nhiều phép biến đổi mà vẫn giữ quan hệ tương đối.

### “Cosine gần 1 nghĩa hai từ đồng nghĩa”

Không. Nó chỉ nói vector gần cùng hướng trong hình học đã học; từ trái nghĩa hoặc từ có ngữ cảnh sử dụng tương tự cũng có thể gần nhau.

### “Word2Vec hiểu ngữ cảnh cho từng lần dùng từ”

Không. Nó dùng ngữ cảnh khi huấn luyện nhưng cuối cùng mỗi từ vẫn có một vector tĩnh.

### “Embedding là sự thật ngữ nghĩa khách quan”

Không. Nó phản ánh corpus, mục tiêu huấn luyện, thiên lệch và phần thông tin bị thiếu.

## Liên kết kiến thức

Word Embedding nối [Học biểu diễn](../05_neural_networks/08_representation_learning.md), [Đại số tuyến tính](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và dẫn tới [Contextual Embeddings](./04_contextual_embeddings.md).