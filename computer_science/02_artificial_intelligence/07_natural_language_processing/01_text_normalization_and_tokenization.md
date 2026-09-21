# Chuẩn hóa văn bản và Tokenization

Mô hình văn bản không nhận trực tiếp một “câu” theo cách con người nhìn thấy mà nhận một chuỗi ID rời rạc. **Chuẩn hóa (normalization / 정규화)** quyết định dạng chuẩn của văn bản thô; **tokenization (토큰화 / phân tách token)** quyết định cách chia văn bản thành đơn vị và ánh xạ chúng vào bộ từ vựng.

Đây là một tầng hạ tầng rất quan trọng vì tokenization ảnh hưởng trực tiếp đến độ dài chuỗi, hiệu quả đa ngôn ngữ, chi phí context, kích thước vocabulary, cách xử lý từ chưa gặp, mã nguồn và ranh giới khi sinh văn bản.

## Unicode trước khi nói về Tokenization

Văn bản được biểu diễn bằng Unicode code point rồi mã hóa thành byte, phổ biến nhất là UTF-8. Cùng một ký tự hiển thị có thể có nhiều cấu trúc Unicode khác nhau.

Ví dụ một ký tự có dấu có thể được lưu dưới dạng ký tự đã ghép sẵn hoặc ký tự cơ sở + dấu kết hợp. Các dạng chuẩn hóa Unicode thường gặp:

- **NFC**: ghép theo chuẩn tương đương (canonical compose);
- **NFD**: tách theo chuẩn tương đương (canonical decompose);
- **NFKC/NFKD**: chuẩn hóa tương thích, có thể gộp những ký hiệu khác nhau về hình thức.

Không nên áp dụng NFKC một cách máy móc nếu sự khác biệt ký hiệu có ý nghĩa, chẳng hạn trong code, biểu thức toán hoặc định danh người dùng.

## Chuyển đổi chữ hoa/thường

Đưa toàn bộ về chữ thường có thể giảm độ thưa của vocabulary:

```text
Apple → apple
```

nhưng đồng thời làm mất phân biệt:

```text
US vs us
Apple (công ty) vs apple (quả táo)
```

Mô hình nền tảng hiện đại thường giữ nguyên chữ hoa/thường và để tokenizer cùng mô hình tự học cách sử dụng tín hiệu này.

## Dấu câu và khoảng trắng

Pipeline NLP cũ thường loại dấu câu hoặc stopword. Với LLM, cách làm này có thể phá ngữ pháp, code, số, định dạng và phong cách.

Tokenizer hiện đại thường giữ phần lớn hình thức bề mặt của văn bản và đôi khi mã hóa khoảng trắng đầu token một cách tường minh.

Khoảng trắng đặc biệt quan trọng trong Python, mã nguồn và cấu trúc tài liệu.

## Tokenization theo từ

Cách đơn giản là tách văn bản thành từ rồi gán ID.

Ưu điểm là đơn vị trực quan với con người, nhưng có ba vấn đề lớn: vocabulary rất lớn, từ hiếm/từ mới trở thành ngoài bộ từ vựng (OOV), và ngôn ngữ có hình thái phong phú tạo quá nhiều biến thể.

Nếu mọi từ không biết đều ánh xạ thành `<UNK>`, cấu trúc bên trong từ bị mất hoàn toàn.

## Tokenization theo ký tự

Dùng từng ký tự giúp vocabulary nhỏ và tránh OOV ở cấp từ, nhưng chuỗi trở nên dài hơn rất nhiều. Mô hình phải tự học cấu trúc từ và hình thái qua nhiều bước hơn.

Có thể nhìn sự đánh đổi như sau:

```text
vocabulary nhỏ ↔ chuỗi dài hơn
đơn vị lớn     ↔ nhiều OOV và dữ liệu thưa hơn
```

Subword nằm ở giữa hai cực này.

## Tokenization theo Byte

Nếu biểu diễn UTF-8 dưới dạng byte, vocabulary cơ sở chỉ cần tối đa 256 giá trị trước khi thêm merge và special token. Mọi chuỗi byte đều biểu diễn được nên không cần `<UNK>` cho ký tự lạ.

Tuy nhiên các ngôn ngữ ngoài ASCII thường cần nhiều byte cho một ký tự, làm chuỗi cơ sở dài hơn. Tokenizer kiểu byte-level BPE có thể học merge những chuỗi byte phổ biến thành token lớn hơn.

## Byte Pair Encoding — BPE

BPE bắt đầu từ các đơn vị nhỏ rồi lặp lại việc ghép những cặp kề nhau xuất hiện thường xuyên.

Ví dụ corpus đơn giản:

```text
low lower newest widest
```

Các cặp phổ biến dần được ghép thành subword. Khi suy luận, từ mới được phân rã thành những mảnh đã biết.

Kích thước vocabulary là một sự đánh đổi:

- vocabulary lớn → chuỗi ngắn hơn nhưng embedding/output matrix lớn hơn;
- vocabulary nhỏ → chuỗi dài hơn nhưng các mảnh được tái sử dụng nhiều hơn.

## WordPiece

WordPiece cũng tạo subword nhưng tiêu chí chọn hoặc ghép khác BPE cổ điển và từng được sử dụng rộng trong họ BERT.

Một quy ước hiển thị quen thuộc là:

```text
play ##ing
```

`##` chỉ là ký hiệu tiếp nối của một implementation, không phải thuộc tính bắt buộc của mọi tokenizer subword.

## Unigram Language Model Tokenization

Tokenizer kiểu **Unigram** bắt đầu với tập candidate lớn rồi loại dần các mảnh sao cho xác suất phân đoạn corpus vẫn tốt.

Một chuỗi có thể có nhiều cách phân đoạn; tokenizer chọn cách có xác suất cao, và **subword regularization** có thể lấy mẫu nhiều cách phân đoạn khi huấn luyện để tăng độ bền.

## SentencePiece

SentencePiece có thể làm việc trực tiếp với văn bản thô mà không cần bước tách từ theo khoảng trắng riêng và hỗ trợ cả BPE lẫn Unigram. Khoảng trắng có thể được biểu diễn bằng ký hiệu như `▁`.

Điều này hữu ích cho hệ thống đa ngôn ngữ vì quy tắc ranh giới từ rất khác nhau giữa các ngôn ngữ.

## Tokenizer như một cơ chế nén được học

Chuỗi xuất hiện thường xuyên có xu hướng được gom thành token lớn; mẫu hiếm bị phân rã thành mảnh nhỏ hơn. Có thể xem tokenizer là cơ chế phân bổ dung lượng vocabulary theo tần suất corpus.

Điều này tạo thiên lệch phân bố: ngôn ngữ ít xuất hiện khi huấn luyện tokenizer có thể cần nhiều token hơn để biểu diễn cùng lượng nội dung, làm tăng chi phí và tiêu tốn context nhiều hơn.

## Hiệu quả Token đa ngôn ngữ

Nếu một câu tiếng Anh cần 10 token nhưng câu tiếng Việt hoặc tiếng Hàn tương đương cần 18 token, cùng lượng ý nghĩa phải dùng nhiều bước tính toán hơn.

Vì vậy khi triển khai đa ngôn ngữ nên đo số token trên ký tự, từ hoặc đơn vị nội dung cho các ngôn ngữ mục tiêu thay vì chỉ giả định tokenizer hoạt động đồng đều.

## Tokenization tiếng Hàn

Tiếng Hàn có hình thái chắp dính nên vocabulary thuần theo khoảng trắng rất dễ thưa. Subword giúp chia thân từ và hậu tố theo thống kê.

Bộ phân tích hình thái có thể tách morpheme tường minh và vẫn hữu ích trong NLP cổ điển. LLM đa ngôn ngữ quy mô lớn thường ưu tiên tokenizer subword hoặc byte tổng quát để tránh pipeline riêng cho từng ngôn ngữ.

Lựa chọn phụ thuộc mô hình, corpus và bài toán.

## Tokenization tiếng Việt

Trong tiếng Việt, khoảng trắng tách âm tiết chứ không phải lúc nào cũng tách một từ vựng hoàn chỉnh:

```text
trí_tuệ
nhân_tạo
```

NLP tiếng Việt truyền thống có thể phân đoạn từ trước. LLM subword có thể tự học các cụm đa âm tiết phổ biến, nhưng hiệu quả còn phụ thuộc dữ liệu huấn luyện tokenizer.

## Biểu diễn số

Một chuỗi số như:

```text
20260920
```

có thể bị chia thành những nhóm chữ số không mang cấu trúc số học rõ ràng. Vì vậy khả năng tính toán số học không được đảm bảo chỉ từ tokenization.

Các hệ thống cần tính toán chính xác thường kết hợp biểu diễn chuyên biệt hoặc công cụ calculator/code execution.

## Tokenization cho Code

Ngôn ngữ lập trình phụ thuộc dấu câu, thụt lề, identifier và khoảng trắng. Tokenizer chủ yếu huấn luyện trên văn bản tự nhiên có thể phân mảnh identifier và cú pháp code kém hiệu quả.

Mô hình chuyên code thường hưởng lợi từ tokenizer và corpus có độ phủ tốt với cú pháp lập trình và các mẫu identifier phổ biến.

## Special Token

Ví dụ:

```text
<BOS>  bắt đầu chuỗi
<EOS>  kết thúc chuỗi
<PAD>  token đệm
<MASK> token che trong masked modeling
<SEP>  phân cách
```

Mô hình chat còn có token điều khiển vai trò system/user/assistant.

Các token này là một phần của giao thức mô hình. Nếu tự tạo prompt không đúng template đã huấn luyện, chuỗi token thực tế khác với phân bố mô hình đã quen và hành vi có thể thay đổi đáng kể.

## ID Token chỉ là mã định danh

Token ID `50256` không có ý nghĩa “lớn hơn” token ID `42`; chúng chỉ là chỉ số hàng trong embedding matrix.

Không nên dùng ID token thô như một đặc trưng số liên tục.

## Tokenization và Context Window

Giới hạn context được tính theo token, không phải ký tự hoặc từ.

Khi chia tài liệu, cần đo bằng đúng tokenizer của mô hình. “500 từ” có thể tạo số token rất khác nhau giữa ngôn ngữ, code, JSON, bảng và văn xuôi.

## Tokenization và quá trình sinh

Mô hình dự đoán token chứ không trực tiếp dự đoán một từ hoàn chỉnh. Một từ có thể cần nhiều bước giải mã.

Xác suất của một chuỗi ký tự phụ thuộc cách chuỗi đó được phân đoạn thành token, vì vậy ranh giới tokenizer ảnh hưởng cả lấy mẫu và phân tích log-probability.

## Xử lý Byte chưa hoàn chỉnh

Tokenizer có byte fallback có thể biểu diễn mọi chuỗi Unicode, nhưng một token trung gian có thể chỉ chứa một phần byte của ký tự UTF-8. Không nên nối chuỗi hiển thị của từng token theo cách thủ công; hãy để thư viện tokenizer giải mã đầy đủ chuỗi ID.

## Chuẩn hóa và bảo mật

Unicode có nhiều ký tự nhìn gần giống nhau, ví dụ chữ `a` Latin và `а` Cyrillic. Kẻ tấn công có thể dùng homoglyph, ký tự zero-width hoặc góc cạnh chuẩn hóa để đánh lừa bộ lọc.

Pipeline nhạy cảm về bảo mật cần chính sách canonicalization và phát hiện Unicode-aware nhưng vẫn phải tránh phá văn bản đa ngôn ngữ hợp lệ.

## Leakage từ quá trình huấn luyện Tokenizer

Vocabulary của tokenizer có thể phản ánh tần suất hoặc artifact của corpus. Quan trọng hơn, nếu tokenizer được huấn luyện bằng dữ liệu tương lai hoặc tập kiểm tra, nó tạo một phụ thuộc tiền xử lý không sạch.

Vì vậy tokenizer cũng phải được version cùng dữ liệu và giao thức đánh giá.

## Phiên bản Tokenizer là một phần khả năng tương thích của Model

Embedding và output matrix được đánh chỉ số bằng vocabulary. Thay đổi token ID hoặc cách phân đoạn mà không huấn luyện lại sẽ phá ý nghĩa của trọng số mô hình.

Tokenizer phải được đóng gói, version và triển khai cùng model artifact.

## Mô hình tư duy

```text
Byte thô / Unicode
   ↓ chính sách chuẩn hóa
Văn bản đã chuẩn hóa
   ↓ thuật toán phân đoạn + vocabulary đã học
Các token piece
   ↓ ID
Tra cứu embedding
   ↓
Biểu diễn neural
```

Tokenization là giao diện cấu trúc giữa văn bản con người và tính toán của mô hình. Các tokenizer byte hiện đại có thể bảo toàn nội dung thô gần như thuận nghịch, nhưng cách phân đoạn vẫn tác động mạnh tới hiệu quả học và chi phí.

## Những hiểu lầm thường gặp

### “1 token xấp xỉ 1 từ”

Không. Số token thay đổi mạnh theo ngôn ngữ và chuỗi cụ thể.

### “Tokenizer chỉ ảnh hưởng tốc độ, không ảnh hưởng chất lượng”

Không. Nó ảnh hưởng độ dài chuỗi, cách chia sẻ hình thái, hiệu quả đa ngôn ngữ và đơn vị mà mô hình phải dự đoán.

### “Lowercase và bỏ dấu câu luôn làm dữ liệu sạch hơn”

Không. Với LLM hiện đại, cách làm này có thể phá cú pháp và ngữ cảnh hữu ích.

### “Có thể đổi tokenizer nếu vocabulary size giống nhau”

Không. ID và cách phân đoạn phải khớp chính xác với embedding/output matrix đã huấn luyện.

## Liên kết kiến thức

Tokenization chuẩn bị nền cho [Language Models](./02_language_models.md), [Word Embeddings](./03_word_embeddings.md) và phần LLM về context/tokenization sau này.