# Ngôn ngữ như dữ liệu: làm sao biến ngôn ngữ thành đối tượng tính toán?

**Xử lý ngôn ngữ tự nhiên (Natural Language Processing — NLP / 자연어 처리)** bắt đầu từ một mâu thuẫn cơ bản: ngôn ngữ mang tính ký hiệu, phụ thuộc ngữ cảnh, mơ hồ và gắn với đời sống xã hội, trong khi máy tính cần mã rời rạc, số và tensor. Vì vậy bước đầu tiên không phải chọn Transformer mà là quyết định **ta đang coi ngôn ngữ là loại dữ liệu gì và cấu trúc nào sẽ được giữ hoặc mất khi biểu diễn**.

## Văn bản không đồng nghĩa với ý nghĩa

Một chuỗi như:

```text
bank
```

có thể chỉ ngân hàng hoặc bờ sông. Các ký tự thô không chứa sẵn nghĩa cần chọn; ý nghĩa phụ thuộc ngữ cảnh, tri thức thế giới và cách sử dụng.

Hệ thống NLP xử lý những hình thức quan sát được của ngôn ngữ và học các quan hệ thống kê hoặc có cấu trúc để suy ra biểu diễn hữu ích. Không nên đồng nhất độ trôi chảy của đầu ra với mức độ hiểu; khả năng phải được đánh giá qua tác vụ và hành vi cụ thể.

## Các tầng cấu trúc ngôn ngữ

Ngôn ngữ có nhiều tầng tương tác với nhau:

- **ngữ âm học / âm vị học (phonetics / phonology)**: cấu trúc âm thanh;
- **hình thái học (morphology / 형태론)**: cấu tạo từ và morpheme;
- **cú pháp (syntax / 통사론)**: cấu trúc câu;
- **ngữ nghĩa học (semantics / 의미론)**: ý nghĩa;
- **ngữ dụng học (pragmatics / 화용론)**: ý nghĩa trong ngữ cảnh, mục đích và quan hệ giao tiếp;
- **diễn ngôn (discourse)**: quan hệ giữa nhiều câu hoặc nhiều phần của tài liệu.

Mô hình hiện đại thường học nhiều tầng cùng lúc, nhưng việc phân biệt thuật ngữ vẫn hữu ích khi phân tích loại nhiệm vụ và nguyên nhân thất bại.

## Token, Type và Vocabulary

**Token** là một lần xuất hiện của đơn vị sau khi phân đoạn văn bản.

**Type** là loại token duy nhất.

**Bộ từ vựng (vocabulary — `V`)** là tập các token type mà mô hình có thể biểu diễn trực tiếp.

Ví dụ corpus:

```text
AI learns. AI changes.
```

`AI` xuất hiện hai token nhưng chỉ có một type.

Khi dùng tokenization theo subword, “từ” không còn bắt buộc là đơn vị nguyên tử của mô hình.

## Corpus và phân bố dữ liệu

**Corpus** là tập hợp văn bản dùng để phân tích hoặc huấn luyện. Mô hình học phân bố có trong corpus chứ không tiếp cận trực tiếp một “ngôn ngữ phổ quát”.

Thành phần corpus ảnh hưởng phương ngữ, lĩnh vực, phong cách, độ phủ kiến thức, thiên lệch xã hội, tính cập nhật và tỷ lệ giữa các ngôn ngữ. Vì vậy lựa chọn và làm sạch dữ liệu là một phần của thiết kế mô hình.

## Định luật Zipf

Tần suất từ trong ngôn ngữ tự nhiên thường có đuôi dài: một số ít từ xuất hiện cực kỳ nhiều, còn rất nhiều từ xuất hiện hiếm.

Xấp xỉ:

\[
f(r)\propto\frac1{r^s}
\]

với `r` là thứ hạng tần suất.

Hệ quả là vocabulary ở cấp từ rất lớn, từ hiếm và từ ngoài bộ từ vựng thường xuyên xuất hiện, tokenization theo subword trở nên hữu ích và độ mất cân bằng tần suất ảnh hưởng mạnh đến huấn luyện.

## Hình thái học của tiếng Hàn, tiếng Việt và tiếng Anh

Tiếng Anh có khoảng trắng khá gần ranh giới từ nhưng vẫn có biến đổi như `walk`, `walked`, `walking`.

Tiếng Hàn là ngôn ngữ chắp dính, nơi thân từ kết hợp nhiều hậu tố ngữ pháp:

```text
먹었습니다
먹 + 었 + 습니다
```

Nếu token hóa hoàn toàn theo từ, vocabulary dễ trở nên thưa. Phân tích hình thái hoặc subword tokenizer giúp xử lý các biến thể này.

Tiếng Việt dùng khoảng trắng giữa các âm tiết, không phải lúc nào cũng trùng với một đơn vị từ vựng hoàn chỉnh:

```text
trí tuệ nhân tạo
```

Do đó thiết kế tokenization phải xét đặc điểm từng ngôn ngữ. Các tokenizer subword dùng chung nhiều ngôn ngữ chấp nhận đánh đổi một phần tính “thuần ngôn ngữ học” để đổi lấy khả năng mở rộng và học trực tiếp từ dữ liệu.

## Tính mơ hồ

### Mơ hồ từ vựng

Một từ như `bank` có nhiều nghĩa.

### Mơ hồ cú pháp

```text
I saw the man with the telescope.
```

Cụm `with the telescope` có thể bổ nghĩa cho hành động nhìn hoặc cho người đàn ông.

### Mơ hồ tham chiếu

```text
John told Mike that he was late.
```

Đại từ `he` có thể tham chiếu John hoặc Mike nếu không có thêm ngữ cảnh.

Mô hình ngôn ngữ phải dùng ngữ cảnh và tri thức đã học để phân giải những trường hợp này theo xác suất.

## Bag-of-Words

Biểu diễn cổ điển **Bag-of-Words (BoW / túi từ)** đếm số lần token xuất hiện:

\[
x_j=count(token_j)
\]

Cách này bỏ qua thứ tự, nên:

```text
dog bites man
man bites dog
```

có cùng biểu diễn BoW.

Dù có giới hạn này, BoW và TF-IDF vẫn là baseline dễ giải thích và rất mạnh cho nhiều bài toán phân loại hoặc tìm kiếm.

## n-gram

**n-gram** giữ một lượng thứ tự cục bộ:

- unigram: một token;
- bigram: hai token;
- trigram: ba token.

Mô hình ngôn ngữ cổ điển xấp xỉ:

\[
P(w_t\mid w_{<t})\approx P(w_t\mid w_{t-n+1:t-1})
\]

Đây là giả định Markov giúp giảm độ phức tạp nhưng tạo vấn đề dữ liệu thưa khi `n` tăng.

Mô hình ngôn ngữ neural thay bảng n-gram tường minh bằng biểu diễn phân tán và khả năng dùng ngữ cảnh dài hơn.

## TF-IDF

**Term Frequency–Inverse Document Frequency (TF-IDF)** giảm trọng số của những từ xuất hiện ở gần như mọi tài liệu và tăng trọng số tương đối của từ đặc trưng cho tài liệu.

Dạng đơn giản:

\[
TFIDF(t,d)=TF(t,d)\cdot\log\frac{N}{DF(t)}
\]

Một term xuất hiện nhiều trong một tài liệu nhưng hiếm trên toàn corpus sẽ có trọng số cao hơn.

Đây là nền tảng của truy xuất từ khóa và vẫn rất hữu ích khi kết hợp với embedding dày đặc trong tìm kiếm lai (hybrid search).

## Ngôn ngữ có thể được biểu diễn bằng chuỗi, cây hoặc đồ thị

Văn bản thô là chuỗi, nhưng nhiều quan hệ ngôn ngữ có thể biểu diễn bằng cấu trúc khác:

- cây phụ thuộc (dependency tree);
- cây thành phần (constituency tree);
- đồ thị đồng tham chiếu (coreference graph);
- đồ thị vai trò ngữ nghĩa (semantic role graph).

Transformer không bắt buộc phải nhận cây phân tích cú pháp vì attention có thể học nhiều quan hệ từ chuỗi. Tuy nhiên các cấu trúc tường minh vẫn hữu ích khi cần ràng buộc, truy vấn hoặc giải thích rõ ràng.

## Từ token rời rạc tới vector liên tục

Token ID chỉ là mã định danh tùy ý, không mang ý nghĩa số học. Embedding biến token thành vector:

\[
token\ id\rightarrow e\in R^d
\]

Từ đây, hình học của không gian vector có thể mã hóa những quan hệ học được giữa token. Sự chuyển từ ký hiệu rời rạc sang biểu diễn liên tục là một nền tảng của NLP hiện đại.

## Context Window như một biên dữ liệu

Tài liệu có thể dài hơn cửa sổ ngữ cảnh của mô hình. Việc cắt ngắn hoặc chia chunk thay đổi những quan hệ mô hình có thể quan sát.

Nếu một đoạn văn bị tách khỏi tiêu đề, nó có thể mất thông tin ngữ cảnh quan trọng. Vấn đề này sẽ xuất hiện lại trong thiết kế chunk của RAG.

Vì vậy xây dựng context cũng là một phần của bài toán biểu diễn dữ liệu.

## Metadata

Tác giả, thời gian, ngôn ngữ, tiêu đề, đường dẫn section và nguồn tài liệu có thể mang thông tin quan trọng. Bỏ metadata có thể làm mất ngữ cảnh; đưa metadata vào không đúng cách cũng có thể gây leakage.

Pipeline NLP nên phân biệt rõ nội dung và metadata, đồng thời duy trì nguồn gốc dữ liệu (provenance).

## Chất lượng dữ liệu văn bản

Những vấn đề phổ biến gồm:

```text
lỗi encoding
HTML boilerplate
lỗi OCR
trùng lặp
spam
văn bản tự sinh chất lượng thấp
PII / bí mật
nhận diện sai ngôn ngữ
```

Chất lượng huấn luyện LLM phụ thuộc mạnh vào lọc, loại trùng và cân bằng dữ liệu chứ không chỉ số lượng token.

## Grounding

Văn bản mô tả thế giới nhưng không phải chính thế giới. Mô hình ngôn ngữ học các mẫu thống kê từ quan sát dạng văn bản. Để đạt độ đúng thực tế, hệ thống còn phụ thuộc chất lượng nguồn, tính cập nhật, truy xuất, công cụ hoặc cơ chế xác minh.

Sự phân biệt này là nền để hiểu hallucination sau này.

## Mô hình tư duy

```text
Thế giới / ý định con người
   ↓ được diễn đạt không hoàn hảo
Tín hiệu ngôn ngữ
   ↓ chuẩn hóa / phân đoạn
Token / cấu trúc
   ↓ biểu diễn vector
Tính toán của mô hình
   ↓
Dự đoán / ngôn ngữ được sinh
```

Mỗi mũi tên đều có thể làm mất thông tin hoặc đưa thêm thiên lệch.

## Những hiểu lầm thường gặp

### “Từ là đơn vị nguyên tử tự nhiên”

Không. Ranh giới từ khác nhau giữa ngôn ngữ; tokenizer hiện đại thường dùng subword hoặc byte.

### “Càng nhiều văn bản thì mô hình càng tốt”

Không nhất thiết. Chất lượng, đa dạng, trùng lặp, cân bằng miền và contamination đều quan trọng.

### “Embedding chứa đầy đủ ý nghĩa của từ”

Không. Nó mã hóa quan hệ thống kê phụ thuộc mô hình, dữ liệu và mục tiêu huấn luyện, không phải toàn bộ ý nghĩa đã grounded trong thế giới.

### “Transformer làm TF-IDF/BM25 trở nên vô dụng”

Không. Các phương pháp lexical vẫn là baseline và thành phần truy xuất rất mạnh, đặc biệt khi kết hợp với dense retrieval.

## Liên kết kiến thức

Biểu diễn ngôn ngữ nối [Mô hình chuỗi](../06_deep_learning_architectures/01_sequence_models.md), [Học biểu diễn](../05_neural_networks/08_representation_learning.md), Xác suất và Lý thuyết thông tin.

Xem tiếp: [Chuẩn hóa văn bản và Tokenization](./01_text_normalization_and_tokenization.md).