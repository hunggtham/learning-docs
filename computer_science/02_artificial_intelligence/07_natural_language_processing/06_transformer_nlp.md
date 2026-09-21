# Transformer trong NLP: Encoder, Decoder và thích ứng tác vụ

Kiến trúc Transformer là một cơ chế tổng quát; NLP biến cơ chế đó thành những họ mô hình khác nhau thông qua **masking, mục tiêu pretraining, pooling/head và chiến lược fine-tuning**. BERT, GPT và T5 không chỉ khác tên; chúng có luồng thông tin và mục tiêu học khác nhau.

## NLP với Encoder-Only

Self-attention của encoder thường hai chiều: mỗi token có thể truy cập ngữ cảnh bên trái và bên phải.

Pretraining kiểu BERT dùng **Masked Language Modeling (MLM)**: chọn một số token, làm hỏng hoặc che chúng rồi dự đoán token gốc.

Biểu diễn thu được phù hợp cho:

- phân loại văn bản;
- phân loại token / NER;
- Question Answering trích xuất;
- chấm điểm cặp câu;
- embedding sau khi được huấn luyện thêm cho mục tiêu phù hợp.

Encoder-only không tự nhiên cho sinh văn bản tự hồi quy dài vì luồng thông tin và mục tiêu huấn luyện không mang tính nhân quả.

## NLP với Decoder-Only

Decoder-only sử dụng causal mask và học:

\[
P(x_t\mid x_{<t})
\]

Một kiến trúc có thể xử lý nhiều tác vụ bằng cách biến đầu vào và yêu cầu thành tiền tố, rồi sinh phần tiếp theo làm đầu ra.

Tính linh hoạt này mở rộng tự nhiên thành LLM và instruction following.

Với tác vụ phân loại thuần túy, decoder lớn có thể tốn compute hơn encoder chuyên dụng, nhưng một hệ thống triển khai thống nhất đôi khi vẫn đáng giá về mặt vận hành.

## NLP với Encoder–Decoder

Encoder đọc toàn bộ nguồn hai chiều; decoder sinh đầu ra nhân quả và dùng cross-attention để truy cập biểu diễn nguồn.

Cấu trúc này tự nhiên cho:

- dịch máy;
- tóm tắt;
- biến đổi có cấu trúc;
- sinh có điều kiện.

Các họ T5 và BART minh họa rõ mô hình text-to-text.

## Mục tiêu Pretraining định hình năng lực

Cùng một kiến trúc dưới các mục tiêu khác nhau có thể học hành vi rất khác.

Causal LM được thưởng khi dự đoán phần tiếp theo. Masked LM học khôi phục token bị che bằng cả hai phía. Denoising Seq2Seq học phục hồi toàn bộ văn bản từ đầu vào bị làm hỏng. Mục tiêu contrastive học hình học tương đồng.

Vì vậy không nên suy năng lực chỉ từ tên kiến trúc; cần xem cả luồng thông tin và objective.

## Fine-Tuning cho phân loại

Đầu ra encoder có thể được pooling từ `[CLS]` hoặc trung bình hidden state:

\[
h_{pool}=Pool(H)
\]

Classifier:

\[
p(y\mid x)=softmax(Wh_{pool}+b)
\]

Fine-tuning có thể cập nhật toàn bộ encoder, một phần encoder hoặc chỉ head.

Tập dữ liệu nhỏ làm tăng nguy cơ overfit và catastrophic forgetting. Learning rate thấp hơn, regularization hoặc adapter có thể giúp.

## Phân loại Token

NER hoặc POS tagging dùng hidden state của từng token:

\[
p(y_i\mid x)=softmax(Wh_i+b)
\]

Subword tạo một vấn đề thực tế: một từ có thể bị chia thành nhiều piece. Pipeline phải quyết định gán nhãn cho piece đầu, mọi piece hay gộp chúng khi đánh giá.

Metric nên tái tạo đúng ranh giới từ hoặc thực thể thay vì chỉ tính accuracy trên token piece.

## Extractive Question Answering

Với đầu vào `[question ; context]`, encoder tạo hidden state cho mọi token. Hai head dự đoán vị trí bắt đầu và kết thúc:

\[
P(start=i),\qquad P(end=j)
\]

Câu trả lời bị giới hạn trong một span của context, giúp giảm tự do sinh và một số dạng hallucination. Tuy nhiên nếu đáp án không có trong context, hệ thống cần mô hình hóa lựa chọn “không có đáp án”; nếu không nó vẫn có thể chọn một span sai.

## Natural Language Inference

**Natural Language Inference (NLI)** nhận premise và hypothesis rồi phân loại entailment, contradiction hoặc neutral.

Dataset NLI hữu ích để nghiên cứu suy luận ngữ nghĩa, nhưng mô hình có thể khai thác artifact trong cách người gán nhãn tạo câu. Điểm benchmark cao không tự động chứng minh khả năng suy luận logic bền vững ngoài phân bố.

## Cross-Encoder cho cặp văn bản

Với relevance hoặc paraphrase:

```text
[CLS] query [SEP] document
```

self-attention chung cho phép token của query tương tác trực tiếp với token của document. Điều này thường cho điểm cặp chính xác hơn nhưng chi phí suy luận tăng theo số cặp ứng viên.

Sự đánh đổi bi-encoder ↔ cross-encoder là nền tảng của kiến trúc retrieval và reranking.

## Fine-Tuning dựa trên Prompt

Thay vì thêm classification head riêng, có thể chuyển tác vụ về dự đoán ngôn ngữ:

```text
Review: ... Sentiment: [MASK]
```

hoặc sinh văn bản.

Cách này giúp tác vụ downstream gần hơn với mục tiêu pretraining và có thể hữu ích khi dữ liệu ít. Tuy nhiên lựa chọn verbalizer — token nào đại diện nhãn nào — có thể tạo thiên lệch đáng kể.

## Parameter-Efficient Fine-Tuning

Thay vì cập nhật toàn bộ trọng số, có thể dùng:

- adapter: chèn module nhỏ có thể huấn luyện;
- LoRA: học cập nhật low-rank;
- prefix/prompt tuning: học vector giống token ảo;
- bias-only: chỉ cập nhật một phần tham số.

**PEFT (Parameter-Efficient Fine-Tuning)** giảm bộ nhớ và dung lượng lưu trữ, tiện cho nhiều biến thể chuyên biệt trên cùng base model và có thể giảm forgetting. Đổi lại, một số tác vụ có thể cần năng lực thích ứng cao hơn full fine-tuning mới đạt trần chất lượng tốt nhất.

## Tài liệu dài

Transformer cơ bản có context hữu hạn và attention bậc hai. Các chiến lược thường gặp:

- cắt ngắn;
- sliding window;
- mã hóa từng chunk rồi tổng hợp phân cấp;
- sparse/long attention;
- retrieval trước khi mã hóa.

Cách chia phải phù hợp tác vụ; chunking cục bộ có thể làm mất quan hệ diễn ngôn kéo dài qua nhiều phần tài liệu.

## Mô hình NLP chuyên Domain

Y sinh, pháp lý và tài chính có thuật ngữ, phong cách và loại thực thể khác văn bản tổng quát. Tiếp tục pretraining trên corpus domain rồi fine-tune cho tác vụ cụ thể có thể cải thiện kết quả.

Tuy nhiên domain pretraining vẫn cần kiểm soát chất lượng, bản quyền, riêng tư và khả năng làm lệch năng lực tổng quát.

## Transformer đa ngôn ngữ

Tokenizer và tham số dùng chung cho nhiều ngôn ngữ cho phép transfer xuyên ngôn ngữ. Nhưng ngôn ngữ nhiều dữ liệu có thể chiếm phần lớn dung lượng học; script, hiệu quả token và tỷ lệ corpus đều ảnh hưởng.

Cross-lingual transfer xuất hiện vì biểu diễn chung học được nhiều cấu trúc tương đồng, nhưng hiệu năng không đồng đều. Hệ thống nhắm tới tiếng Hàn hoặc tiếng Việt nên đánh giá riêng từng ngôn ngữ thay vì chỉ dựa vào điểm tiếng Anh.

## Distillation

**Chưng cất mô hình (knowledge distillation)** dùng teacher Transformer truyền hành vi sang student nhỏ hơn thông qua soft target, hidden-state loss hoặc các tín hiệu khác.

Mục tiêu là giảm latency và memory trong khi giữ càng nhiều chất lượng càng tốt. Student có thể dùng ít layer hoặc hidden dimension nhỏ hơn.

Distillation sẽ xuất hiện lại trong phần AI Engineering.

## Quantization trong NLP

Suy luận có thể lượng tử hóa trọng số và activation. Nhiều mô hình chịu được INT8 hoặc 4-bit khá tốt, nhưng layer nhạy hoặc outlier có thể cần mixed precision và calibration.

Nén mô hình không phải chuyện tách rời NLP; nó là một ràng buộc triển khai ảnh hưởng trực tiếp lựa chọn model và kiến trúc hệ thống.

## Mô hình tư duy

```text
Cơ chế Transformer
+ mask / luồng thông tin
+ mục tiêu pretraining
+ task head hoặc prompting
+ phương pháp thích ứng
= hành vi của mô hình NLP
```

## Những hiểu lầm thường gặp

### “BERT và GPT chỉ khác dữ liệu huấn luyện”

Không. Hướng attention, causal mask và objective khác nhau về bản chất.

### “Encoder không sinh văn bản nên kém hơn”

Không. Với phân loại, retrieval hoặc reranking, encoder nhỏ có thể hiệu quả hơn nhiều trên mỗi đơn vị compute.

### “Fine-tuning toàn bộ trọng số luôn tốt nhất”

Không. Dữ liệu nhỏ, nhiều tác vụ và ràng buộc serving có thể làm PEFT phù hợp hơn.

### “Mô hình đa ngôn ngữ tạo biểu diễn hoàn toàn độc lập ngôn ngữ”

Không. Alignment xuyên ngôn ngữ luôn không hoàn hảo và phụ thuộc dữ liệu.

## Liên kết kiến thức

Xem [Kiến trúc Transformer](../06_deep_learning_architectures/05_transformer.md), [Seq2Seq NLP](./05_sequence_to_sequence_nlp.md) và tiếp theo [Information Extraction](./07_information_extraction.md).