# Sequence-to-Sequence NLP: từ dịch máy tới học Text-to-Text

**Sequence-to-Sequence (Seq2Seq / 시퀀스-투-시퀀스)** trong NLP xử lý những bài toán mà đầu vào là một chuỗi và đầu ra là một chuỗi khác, có thể khác về độ dài và không có căn chỉnh một-một theo vị trí. Dịch máy, tóm tắt, sửa ngữ pháp, tạo câu hỏi và nhiều tác vụ structured-to-text thuộc họ này.

Kiến trúc cơ bản đã được giải thích ở [Encoder–Decoder Models](../06_deep_learning_architectures/03_encoder_decoder_models.md); chapter này tập trung vào cách huấn luyện, giải mã và đánh giá đặc thù của NLP.

## Mô hình hóa ngôn ngữ có điều kiện

Với chuỗi nguồn `x` và chuỗi đích `y`:

\[
P(y\mid x)=\prod_{t=1}^{T}P(y_t\mid y_{<t},x)
\]

Huấn luyện tối thiểu hóa negative log-likelihood có điều kiện:

\[
L=-\sum_t\log P(y_t^{true}\mid y_{<t}^{true},x)
\]

Điểm khác với mô hình ngôn ngữ tiếp diễn không điều kiện là mọi dự đoán đầu ra còn phụ thuộc chuỗi nguồn `x`.

## Neural Machine Translation

Dịch máy thống kê truyền thống sử dụng bảng cụm từ, mô hình căn chỉnh và mô hình ngôn ngữ. **Neural Machine Translation (NMT)** thay thế nhiều thành phần rời rạc bằng một mô hình có điều kiện được học end-to-end.

Lịch sử phát triển đi từ RNN encoder–decoder, tới attention để loại nút thắt một-vector, rồi Transformer trở thành kiến trúc chủ đạo.

Dịch tốt không chỉ là thay từ vì thứ tự từ, hình thái, thành ngữ, ngữ dụng và cấu trúc diễn ngôn khác nhau giữa các ngôn ngữ.

## Alignment

Trọng số attention thường có tương quan với căn chỉnh nguồn–đích nhưng không đảm bảo là một bản alignment ngôn ngữ tường minh.

Trong mô hình cổ điển, alignment hỏi từ nguồn nào tương ứng với từ đích nào. Trong mô hình neural, thông tin có thể được phân tán qua nhiều hidden state, head và layer.

Nếu cần căn chỉnh có khả năng giải thích hoặc ràng buộc nghiệp vụ, nên dùng cơ chế extraction hoặc constraint riêng thay vì suy ra trực tiếp từ attention map.

## Copy Mechanism và Pointer Network

Một số nhiệm vụ cần sao chép chính xác tên riêng, số, mã hoặc thực thể từ nguồn. **Cơ chế sao chép (copy mechanism)** kết hợp phân bố sinh từ vocabulary với phân bố sao chép dựa trên attention:

\[
P(token)=p_{gen}P_{vocab}+(1-p_{gen})P_{copy}
\]

Cách này hữu ích cho tóm tắt, data-to-text và dữ liệu có nhiều thực thể. Subword LM hiện đại giảm vấn đề OOV nhưng nhu cầu sao chép chính xác vẫn còn.

## Tóm tắt

**Tóm tắt trích xuất (extractive summarization)** chọn câu hoặc đoạn trực tiếp từ nguồn.

**Tóm tắt sinh mới (abstractive summarization)** tạo cách diễn đạt mới.

Mô hình abstractive có nguy cơ hallucination vì mục tiêu sinh thưởng cho văn bản tóm tắt có xác suất cao chứ không trực tiếp bảo đảm mọi mệnh đề được nguồn hỗ trợ.

Vì vậy **độ trung thành (faithfulness)** phải được đánh giá tách khỏi độ trôi chảy và mức bao phủ nội dung.

## Teacher Forcing và Exposure Bias

Trong huấn luyện, decoder nhìn token đích đúng ở bước trước; trong suy luận, nó nhìn chính token đã sinh. Sự khác biệt này tạo exposure bias và lỗi có thể lan truyền dọc chuỗi.

Các phương pháp tối ưu ở cấp chuỗi như minimum-risk training hoặc reinforcement learning đã được nghiên cứu, nhưng token-level maximum likelihood vẫn là nền tảng vì ổn định và dễ mở rộng.

## Beam Search

Beam Search giữ `B` chuỗi ứng viên từng phần có điểm tốt nhất theo tổng log-xác suất.

Log-xác suất thô thường ưu tiên chuỗi ngắn, vì vậy có thể dùng chuẩn hóa độ dài:

\[
score(y)=\frac{\log P(y\mid x)}{len(y)^\alpha}
\]

hoặc các dạng penalty khác.

Beam lớn hơn không phải lúc nào cũng cải thiện chất lượng theo đánh giá con người; phân bố mô hình đôi khi ưu tiên giả thuyết ngắn hoặc chung chung.

## Coverage

Mô hình Seq2Seq có thể bỏ sót phần nguồn hoặc lặp nội dung. Các cơ chế **coverage** theo dõi mức độ mỗi vị trí nguồn đã được attention để giảm bỏ sót và lặp.

Transformer hiện đại giảm một số vấn đề so với kiến trúc cũ nhưng không loại bỏ hoàn toàn lỗi thiếu hoặc lặp thông tin.

## Hợp nhất tác vụ theo Text-to-Text

Các mô hình kiểu T5 đưa nhiều bài toán về cùng khuôn dạng:

```text
văn bản đầu vào + chỉ dẫn tác vụ → văn bản đầu ra
```

Ví dụ:

```text
translate English to German: ...
summarize: ...
```

Một kiến trúc sinh có điều kiện có thể xử lý phân loại, QA, dịch và tóm tắt. Đây là tiền đề trực tiếp cho LLM instruction-tuned, nơi chỉ dẫn bằng ngôn ngữ tự nhiên xác định tác vụ.

## Denoising Seq2Seq Pretraining

Có thể làm hỏng một phần đầu vào rồi huấn luyện mô hình khôi phục văn bản gốc:

```text
văn bản bị làm hỏng → encoder
                     → decoder → văn bản gốc
```

Cách này cho phép encoder–decoder học cấu trúc ngôn ngữ từ corpus không gán nhãn trước khi fine-tuning có giám sát. BART và T5 là những ví dụ tiêu biểu của họ mục tiêu denoising này.

## Giải mã có ràng buộc

Một số ứng dụng yêu cầu đầu ra phải tuân theo định dạng hoặc thuật ngữ cụ thể.

Constrained Beam Search có thể bắt buộc cụm từ, token schema hoặc quy tắc ngữ pháp. Với JSON hoặc output có cấu trúc, hệ thống hiện đại có thể giới hạn token hợp lệ theo grammar/schema thay vì chỉ hi vọng prompt tạo chuỗi đúng.

Điều này nối sinh ngôn ngữ với tìm kiếm và bài toán thỏa ràng buộc cổ điển.

## Dịch đa ngôn ngữ

Một mô hình có thể xử lý nhiều cặp ngôn ngữ bằng tag hoặc instruction. Transfer giữa các ngôn ngữ giúp cặp ít dữ liệu, nhưng chênh lệch dữ liệu có thể làm ngôn ngữ tài nguyên cao chi phối dung lượng mô hình.

Reweighting hoặc lấy mẫu theo temperature thường được dùng để cân bằng nguồn dữ liệu.

Dịch zero-shot giữa cặp không được huấn luyện trực tiếp có thể xuất hiện nhưng chất lượng thay đổi mạnh theo ngôn ngữ và corpus.

## Đánh giá bằng BLEU

BLEU so độ trùng n-gram với bản tham chiếu và dùng brevity penalty:

\[
BLEU=BP\cdot\exp\left(\sum_nw_n\log p_n\right)
\]

BLEU hữu ích ở cấp corpus trong dịch máy, nhưng có nhiều giới hạn: một câu có nhiều bản dịch hợp lệ, metric không nhạy tốt với mọi khác biệt ngữ nghĩa hoặc factuality, tokenization ảnh hưởng mạnh và điểm cấp câu không ổn định.

Các metric neural như COMET hoặc BERTScore sử dụng biểu diễn học được nhưng mang theo thiên lệch của chính mô hình đánh giá. Đánh giá con người vẫn quan trọng cho độ đầy đủ, trôi chảy và trung thành.

## Lỗi ở cấp chuỗi

Một lỗi sớm khi giải mã có thể đổi toàn bộ lịch sử phía sau. Vì vậy token accuracy không phản ánh đầy đủ chất lượng chuỗi.

Error analysis nên xem các nhóm như:

```text
bỏ sót
thêm thông tin / hallucination
dịch sai
sai thực thể hoặc con số
sai hòa hợp ngữ pháp
không nhất quán thuật ngữ
lặp nội dung
```

## Thích ứng Domain

Mô hình dịch tổng quát có thể xử lý kém thuật ngữ pháp lý, y tế hoặc nội bộ công ty. Fine-tuning, adapter, terminology constraint và retrieval từ translation memory có thể giúp.

Tuy nhiên thích ứng quá hẹp có thể gây catastrophic forgetting, nên cần kiểm soát learning rate, trộn dữ liệu tổng quát và đánh giá ngoài domain.

## Mô hình tư duy

> Seq2Seq NLP = mô hình ngôn ngữ có điều kiện + cơ chế truy cập thông tin nguồn + thủ tục giải mã/tìm kiếm.

Kiến trúc tạo phân bố xác suất; thuật toán giải mã quyết định cách biến phân bố đó thành chuỗi cuối cùng.

## Những hiểu lầm thường gặp

### “Beam Search tìm chính xác bản dịch tốt nhất”

Không. Beam hữu hạn là heuristic và chuỗi xác suất cao nhất theo mô hình chưa chắc là bản dịch con người đánh giá tốt nhất.

### “BLEU cao nghĩa tóm tắt trung thành sự thật”

Không. Độ trùng n-gram không đủ để phát hiện mọi hallucination.

### “Seq2Seq lỗi thời sau decoder-only LLM”

Không. Encoder–decoder vẫn tự nhiên và hiệu quả cho nhiều phép biến đổi có điều kiện; decoder-only thống nhất nhiều tác vụ qua prompting nhưng không tối ưu tuyệt đối cho mọi trường hợp.

## Liên kết kiến thức

Seq2Seq kết hợp [Language Model](./02_language_models.md), [Encoder–Decoder](../06_deep_learning_architectures/03_encoder_decoder_models.md), [Attention](../06_deep_learning_architectures/04_attention.md) và liên hệ trực tiếp với tìm kiếm cổ điển thông qua quá trình giải mã.