# Pretraining của Large Language Model

**Pretraining (사전학습 / tiền huấn luyện)** là giai đoạn model học statistical structure từ một lượng dữ liệu rất lớn trước khi được điều chỉnh để làm theo instruction hoặc phục vụ một application cụ thể. Với decoder-only LLM, objective phổ biến là **next-token prediction**: tại mỗi vị trí, model nhận prefix và tối đa hóa xác suất của token tiếp theo.

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

Loss tương ứng thường là negative log-likelihood hay cross-entropy:

\[
\mathcal L=-\sum_t \log P_\theta(x_t\mid x_{<t})
\]

Điểm quan trọng là objective này nhìn có vẻ đơn giản nhưng buộc model phải nén rất nhiều regularity của language và world vào parameters. Muốn dự đoán token tiếp theo tốt, model phải học syntax, semantic association, discourse structure, factual co-occurrence, coding patterns và nhiều dạng reasoning pattern xuất hiện trong training distribution.

## Pretraining không phải database ingestion

Model không biến corpus thành một key-value store hoàn hảo. Training cập nhật hàng tỷ parameters sao cho distribution output phù hợp data. Knowledge vì vậy được **distributed** trong weights. Một fact có thể được encode qua nhiều directions trong representation space và nhiều layers cùng lúc.

Điều này giải thích vì sao model có thể generalize, paraphrase và combine patterns thay vì chỉ replay exact training strings. Đồng thời nó cũng giải thích vì sao retrieval từ parameters không đáng tin như truy vấn database: parameterized knowledge không có guarantee về freshness, provenance hay exact lookup.

## Data pipeline là một phần của model

Pretraining quality không chỉ phụ thuộc architecture. Corpus construction quyết định model nhìn thấy thế giới nào. Raw web data thường phải qua deduplication, quality filtering, language detection, document segmentation, safety filtering và mixture weighting.

Nếu một domain được oversample, model có xu hướng học domain đó mạnh hơn. Nếu corpus chứa duplicated benchmark questions, evaluation có thể bị contamination. Nếu filtering loại quá mạnh một language, capability của language đó giảm.

Vì vậy có thể coi training distribution là một implicit curriculum.

## Token budget và exposure

Dataset thường được đo bằng **token count**, không chỉ số document. Một document dài có nhiều training positions hơn document ngắn. Tokenization cũng ảnh hưởng exposure: cùng một câu tiếng Việt hoặc tiếng Hàn có thể cần nhiều token hơn tiếng Anh tùy vocabulary, làm tăng compute và giảm effective context capacity.

Xem thêm: [LLM Tokenization](./01_llm_tokenization.md).

## Causal masking

Decoder-only model dùng causal mask để token tại vị trí `t` không nhìn thấy future token `x_{>t}` trong training. Điều này làm training task khớp với autoregressive generation.

Trong mỗi sequence, forward pass vẫn có thể xử lý nhiều positions song song vì ground-truth previous tokens đã biết. Inference khác: token mới phải được sinh tuần tự vì output của bước trước trở thành input bước sau.

Sự khác nhau này là lý do training throughput và generation latency có characteristics rất khác.

## Teacher forcing

Trong training autoregressive, model thường nhận **ground-truth previous tokens** thay vì token do chính nó sinh. Cơ chế này gọi là teacher forcing.

Nó làm optimization ổn định và parallelizable nhưng tạo mismatch với inference: khi model sinh sai một token lúc deployment, những bước tiếp theo phải condition trên chính lỗi đó. Error có thể compound.

Instruction tuning và preference training không loại bỏ hoàn toàn mismatch này.

## Packing và sequence construction

Để tận dụng GPU, nhiều short documents có thể được **packed** vào cùng sequence. Implementation phải đảm bảo attention boundary đúng nếu không muốn token của document này vô tình nhìn sang document khác theo cách không mong muốn.

Long-context training cũng làm cost attention tăng mạnh. Với vanilla self-attention, compute/memory attention tăng gần quadratic theo sequence length:

\[
O(n^2)
\]

Do đó context length không phải một setting miễn phí.

## Data mixture

Một LLM tổng quát thường train trên mixture như natural language, code, mathematics, books, technical documents và curated sources. Weight của từng source quyết định gradient contribution.

Ví dụ tăng code data có thể cải thiện programming và đôi khi reasoning có cấu trúc, nhưng nếu mixture mất cân bằng có thể làm giảm language quality ở domain khác. Đây là một optimization đa mục tiêu chứ không chỉ “càng nhiều data càng tốt”.

## Deduplication

Duplicate data làm model gặp cùng pattern quá nhiều lần, tăng memorization và làm quality estimate sai. Dedup có thể ở document-level, paragraph-level hoặc approximate substring level.

Dedup cũng quan trọng cho benchmark integrity. Nếu evaluation set hoặc near-duplicate của nó xuất hiện trong pretraining corpus, score không còn đo pure generalization.

## Memorization và generalization

LLM có thể vừa generalize vừa memorize. Hai hiện tượng không loại trừ nhau.

Rare strings, personally identifying text hoặc repeated sequences có nguy cơ memorization cao hơn. Nhưng phần lớn capability hữu ích đến từ learned abstractions và statistical regularities chứ không phải exact copying.

Khi đánh giá privacy, cần phân biệt:

```text
model biết pattern chung
vs
model có thể reproduce training sequence cụ thể
```

## Pretraining tạo base model, không tạo assistant hoàn chỉnh

Base model được optimize để continue text. Nếu prompt:

```text
User: Explain gradient descent.
Assistant:
```

base model có thể tiếp tục theo pattern đối thoại nếu training data có pattern đó, nhưng không có guarantee sẽ tuân instruction ổn định.

Instruction-following behavior thường được cải thiện qua supervised fine-tuning và preference optimization.

## Domain-adaptive pretraining

Có thể tiếp tục pretraining trên corpus chuyên ngành, ví dụ finance, legal hoặc biomedical data. Đây là **continued pretraining / domain-adaptive pretraining**.

Nó khác SFT. Continued pretraining vẫn tối ưu language-model objective trên raw text, còn SFT tối ưu output được định dạng theo input–response examples.

Continued pretraining hữu ích khi muốn model hấp thụ vocabulary và distribution chuyên ngành sâu hơn, nhưng có thể gây catastrophic forgetting nếu mixture quá hẹp hoặc learning rate quá cao.

## Pretraining và emergent capability

Khi scale model/data/compute tăng, một số capability xuất hiện rõ hơn. Không nên hiểu điều đó như “một module reasoning bí mật tự bật”. Capability observable là kết quả của architecture, data distribution, optimization, scale và evaluation threshold tương tác.

Một benchmark có thể trông như capability xuất hiện đột ngột chỉ vì score vượt một threshold, trong khi underlying performance tăng dần.

## Mental Model

> Pretraining là quá trình **nén distribution của một corpus khổng lồ vào parameters** bằng objective dự đoán token. Model không học một encyclopedia có index; nó học một function tạo probability distribution dựa trên context.

## Common Misconceptions

### “Model đã đọc internet nên biết mọi thứ trên internet”

Training corpus luôn hữu hạn, filtered và có cutoff. Ngay cả text từng xuất hiện trong training cũng không bảo đảm model retrieve chính xác.

### “Pretraining chỉ dạy kiến thức factual”

Nó đồng thời dạy syntax, style, code patterns, semantic relations, procedural patterns và representations hữu ích.

### “Thêm data luôn tốt”

Low-quality, duplicated hoặc mismatched data có thể làm model tệ hơn. Data quality và mixture quan trọng như quantity.

## Knowledge Connection

Pretraining kết nối [Language Models](../07_natural_language_processing/02_language_models.md), [Information Theory](../01_mathematical_foundations/05_information_theory.md), [Optimization](../01_mathematical_foundations/06_optimization.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md).

Xem tiếp: [Scaling Laws](./05_scaling_laws.md).