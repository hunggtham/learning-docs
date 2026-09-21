# Đánh giá NLP: từ nhãn chính xác tới chất lượng ngôn ngữ mở

**Đánh giá NLP (NLP Evaluation / 자연어 처리 평가)** khó hơn nhiều bài toán ML vì ngôn ngữ cho phép nhiều đầu ra khác nhau nhưng vẫn cùng đúng. Phân loại có nhãn tương đối rõ; dịch, tóm tắt và sinh văn bản có thể có vô số cách diễn đạt hợp lệ. Vì vậy cần chọn metric theo đúng tác vụ, tách điểm tự động khỏi giá trị thực cho người dùng và luôn phân tích loại lỗi cụ thể.

## Phân loại và NER

Phân loại dùng accuracy, precision, recall, F1 và calibration như ML nói chung.

NER nên dùng F1 ở cấp thực thể hoặc span thay vì chỉ token accuracy vì nhãn `O` thường chiếm đa số.

Ví dụ exact match nghiêm ngặt:

```text
Gold: [Seoul National University]
Pred: [National University]
```

sẽ tính là sai dù có phần chồng lấp. Có thể bổ sung phân tích partial match, nhưng quy ước báo cáo phải rõ ràng.

## Macro và Micro F1

**Micro F1** gộp toàn bộ count nên bị lớp phổ biến chi phối.

**Macro F1** tính F1 từng lớp rồi lấy trung bình ngang nhau, nhờ đó làm lộ hiệu năng kém ở lớp hiếm.

Weighted macro dùng số lượng mẫu làm trọng số.

Phân bố nhãn NLP thường mất cân bằng, nên một metric duy nhất hiếm khi đủ.

## BLEU

BLEU đo modified n-gram precision cùng brevity penalty so với một hoặc nhiều bản tham chiếu.

Đây là metric lịch sử hữu ích cho đánh giá dịch máy ở cấp corpus vì rẻ và tái lập được.

Hạn chế chính là: paraphrase hợp lệ có thể bị phạt, khả năng phát hiện lỗi ngữ nghĩa và factuality yếu, tokenization và số lượng reference ảnh hưởng điểm, đồng thời điểm ở cấp từng câu khá nhiễu.

BLEU nên dùng để so trong cùng giao thức chứ không phải thước đo chất lượng ngôn ngữ phổ quát.

## ROUGE

Họ ROUGE nhấn mạnh mức bao phủ và trùng lặp, phổ biến trong tóm tắt.

ROUGE-L dùng **longest common subsequence**. Nó thưởng sự trùng nội dung nhưng không đáng tin để phát hiện mâu thuẫn sự thật.

Hệ thống extractive thường có lợi thế trên ROUGE vì câu trả lời giữ nhiều từ giống nguồn.

## METEOR và chrF

METEOR bổ sung stemming, synonym và heuristic căn chỉnh.

chrF dùng F-score của character n-gram và thường hữu ích cho ngôn ngữ có hình thái phong phú vì ít phụ thuộc ranh giới từ.

Không metric nào thay thế được phân tích lỗi theo bài toán.

## BERTScore

BERTScore so token của candidate và reference bằng độ tương đồng contextual embedding.

Nó nhận ra paraphrase tốt hơn metric chỉ dựa trên chuỗi bề mặt. Tuy nhiên nó phụ thuộc encoder dùng để chấm và có thể cho điểm cao cho câu giống về ngữ nghĩa tổng quát nhưng sai một sự kiện hoặc con số quan trọng.

## Metric được học

Các metric kiểu COMET học từ đánh giá con người và biểu diễn của nguồn/reference, thường tương quan với chất lượng dịch tốt hơn nhiều metric cổ điển.

Nhưng bản thân metric cũng là một model, vì vậy có thể có thiên lệch domain, bị tối ưu lách, thay đổi theo phiên bản hoặc có overlap dữ liệu huấn luyện.

Metric học được cũng cần được kiểm định.

## Perplexity

Với mô hình ngôn ngữ:

\[
PPL=\exp(crossentropy)
\]

Perplexity hữu ích khi so cùng tokenizer và cùng corpus kiểm tra. Nó đo mức dự đoán token tiếp theo, không trực tiếp đo helpfulness, instruction following hoặc factuality.

## Exact Match

Question Answering và structured extraction thường dùng exact string match.

Metric này phù hợp khi đáp án có dạng chuẩn rõ ràng nhưng quá nghiêm khi nhiều cách định dạng hoặc paraphrase đều hợp lệ.

Quy trình normalization có thể bỏ chữ hoa, dấu câu hoặc article, nhưng chính sách phải phù hợp ngôn ngữ và yêu cầu tác vụ.

## Metric ngữ nghĩa cho QA

Extractive QA thường dùng token F1. Generative QA có thể kết hợp semantic similarity, entailment hoặc judge cùng kiểm tra evidence.

Một đáp án nhìn tổng thể rất giống reference vẫn có thể sai một số tiền, ngày hoặc thực thể quan trọng; embedding similarity trung bình dễ bỏ sót loại lỗi này.

## Faithfulness và chất lượng tổng quát

Một bản tóm tắt có thể rất trôi chảy và đúng chủ đề nhưng không trung thành với nguồn.

Nên tách các trục:

```text
mức bao phủ / relevance
độ trôi chảy / mạch lạc
faithfulness / grounding
factual correctness
style / format
```

Gộp tất cả vào một điểm sẽ che mất sự đánh đổi giữa các thuộc tính.

## Đánh giá của con người

Human evaluation có thể nhận xét tinh tế hơn nhưng cũng có phương sai và thiên lệch.

Thiết kế tốt cần rubric rõ ràng, so sánh mù/ngẫu nhiên, nhiều người chấm cho nhiệm vụ chủ quan, đo mức đồng thuận, lấy mẫu đại diện và cơ chế xử lý edge case.

So sánh theo cặp thường dễ và ổn định hơn yêu cầu người đánh giá cho điểm tuyệt đối 1–5.

## LLM-as-a-Judge

LLM có thể làm judge để đánh giá quy mô lớn với chi phí thấp hơn con người, đặc biệt cho so sánh cặp và rubric có cấu trúc.

Nhưng judge có thể có:

- thiên lệch vị trí;
- thích câu dài hoặc phong cách cụ thể;
- thiên lệch về cùng họ model;
- nhạy với prompt;
- lỗi factual;
- bị nội dung câu trả lời prompt-inject.

Nên hiệu chỉnh judge với nhãn người thật và cung cấp bằng chứng có cấu trúc khi có thể.

## Contamination dữ liệu

Nếu benchmark đã xuất hiện trong pretraining hoặc fine-tuning, điểm số có thể phản ánh memorization hoặc selection thay vì generalization độc lập.

Với dữ liệu huấn luyện đóng, contamination thường khó chứng minh hoàn toàn. Tập mới, riêng tư hoặc chia theo thời gian giúp giảm rủi ro.

Trong thời đại LLM, benchmark cũng cần vòng đời và phiên bản như dữ liệu production.

## Challenge Set

Tập kiểm tra IID trung bình có thể bỏ sót hiện tượng ngôn ngữ quan trọng. Có thể xây tập tập trung vào:

```text
phủ định
đồng tham chiếu
thực thể hiếm
số và ngày
ngữ cảnh dài
code-switch đa ngôn ngữ
lỗi chính tả đối kháng
tính mơ hồ
```

Mỗi tập nhắm tới một năng lực hoặc failure mode cụ thể.

## Robustness

Có thể biến đổi đầu vào mà không thay đổi ý nghĩa:

```text
đổi dấu câu
paraphrase bằng từ đồng nghĩa
lỗi gõ nhẹ
đổi thứ tự định dạng
chèn câu không liên quan
```

Nếu tác vụ bất biến với biến đổi đó, đầu ra nên tương đối ổn định.

Tuy nhiên perturbation phải thực sự giữ nguyên ngữ nghĩa; nếu vô tình đổi nghĩa thì phép đo robustness không còn hợp lệ.

## Đánh giá đa ngôn ngữ

Không nên chỉ dịch benchmark tiếng Anh rồi coi độ khó tương đương. Dịch có thể thay văn hóa, độ mơ hồ, độ dài token và cả mức độ tự nhiên.

Nên dùng dữ liệu và người đánh giá bản ngữ, đồng thời báo cáo theo từng ngôn ngữ.

Với tiếng Hàn và tiếng Việt, khoảng trắng, hình thái và tokenization có thể ảnh hưởng metric dựa trên overlap; metric theo ký tự hoặc ngữ nghĩa có thể bổ sung góc nhìn.

## Bất định thống kê

Khi có thể nên báo cáo confidence interval bằng bootstrap trên đơn vị độc lập.

Nếu nhiều mẫu cùng thuộc một người dùng hoặc tài liệu, nên resample theo user/document thay vì từng row để không đánh giá thấp độ bất định.

Chênh lệch điểm rất nhỏ mà không có khoảng tin cậy không nên quyết định việc triển khai.

## Đánh giá Online

Metric offline không phản ánh toàn bộ tương tác với người dùng. A/B test có thể đo task completion, search success, số lần sửa hoặc thử lại, retention và bỏ cuộc vì latency.

Nhưng metric online cũng có thể tạo động cơ sai như clickbait hoặc trả lời dài quá mức. Vì vậy cần guardrail và nhiều chỉ số bổ sung.

## Phân loại lỗi

Với output sinh, nên phân loại thủ công hoặc bán tự động:

```text
sai thực thể
sai số / ngày
bỏ sót
thêm thông tin không được hỗ trợ
mâu thuẫn
vi phạm instruction
lỗi format
lỗi ngôn ngữ / phong cách
lỗi grounding từ retrieval
```

Thống kê loại lỗi thường giúp cải thiện hệ thống cụ thể hơn nhiều so với chỉ nhìn BLEU hoặc ROUGE.

## Đánh giá có thể tái lập

Cần lưu:

```text
phiên bản model / tokenizer
prompt / template
cấu hình decoding
phiên bản dataset
phiên bản metric
quy tắc normalization
random seed
phiên bản retrieval index nếu có
```

Cấu hình sinh có thể làm điểm thay đổi đáng kể dù model weights không đổi.

## Mô hình tư duy

> Đánh giá NLP là bài toán thiết kế phép đo. Trước tiên phải định nghĩa “hành vi ngôn ngữ tốt” cho tác vụ, sau đó mới chọn nhiều phép đo xấp xỉ nó.

## Những hiểu lầm thường gặp

### “Metric tự động cao nghĩa output tốt cho người dùng”

Không. Metric chỉ đo một phần mục tiêu mong muốn.

### “Embedding metric giải quyết hoàn toàn vấn đề paraphrase”

Không. Nó vẫn có thể bỏ qua lỗi factual, số học hoặc logic nhỏ nhưng nghiêm trọng.

### “Human evaluation là ground truth không nhiễu”

Không. Con người bất đồng và có thiên lệch; rubric và sampling rất quan trọng.

### “Benchmark score chính là năng lực mô hình”

Không. Đó là hiệu năng trên một mẫu bài toán dưới prompt và giao thức đánh giá cụ thể.

## Liên kết kiến thức

Đánh giá NLP mở rộng [Model Evaluation](../04_machine_learning/15_model_evaluation.md) và chuẩn bị cho các layer LLM/RAG, nơi generation mở, judge và grounding trở thành vấn đề trung tâm.