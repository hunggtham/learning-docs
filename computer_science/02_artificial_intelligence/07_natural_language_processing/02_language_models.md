# Language Model: học xác suất của chuỗi ngôn ngữ

**Mô hình ngôn ngữ (Language Model — LM / 언어 모델)** gán xác suất cho chuỗi hoặc dự đoán token dựa trên ngữ cảnh. Đây là khái niệm cốt lõi đứng sau autocomplete, giải mã tiếng nói, dịch máy và Large Language Model.

Điểm quan trọng là mô hình ngôn ngữ không trực tiếp tối ưu “sự thật” hay “lập luận đúng”. Mục tiêu cơ bản là mô hình hóa phân bố của ngôn ngữ quan sát được. Nhiều năng lực khác xuất hiện vì để dự đoán ngôn ngữ tốt ở quy mô lớn, mô hình phải học rất nhiều cấu trúc về cú pháp, ngữ nghĩa, tri thức và các mẫu lập luận; tuy nhiên mục tiêu huấn luyện và năng lực cuối cùng không phải cùng một khái niệm.

## Xác suất chung và quy tắc chuỗi

Với chuỗi:

\[
x_{1:T}=(x_1,...,x_T)
\]

quy tắc chuỗi cho:

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

Không cần giả định Markov để phân rã này đúng. Phần khó nằm ở việc ước lượng từng phân bố có điều kiện.

Mô hình ngôn ngữ tự hồi quy học:

\[
P_\theta(x_t\mid x_{<t})
\]

## Mô hình ngôn ngữ n-gram

Mô hình n-gram giới hạn ngữ cảnh:

\[
P(x_t\mid x_{<t})\approx P(x_t\mid x_{t-n+1:t-1})
\]

Xác suất có thể được ước lượng từ số đếm:

\[
P(w_t\mid h)=\frac{count(h,w_t)}{count(h)}
\]

Dữ liệu thưa làm nhiều n-gram chưa từng xuất hiện có xác suất bằng `0`. Các kỹ thuật làm trơn như Laplace, Good-Turing và Kneser-Ney phân phối lại khối lượng xác suất. Kneser-Ney đặc biệt sử dụng thống kê về khả năng tiếp nối và là một kỹ thuật kinh điển quan trọng của LM truyền thống.

## Vì sao cần Neural Language Model?

n-gram xem phần lớn ngữ cảnh như ký hiệu rời rạc. Hai câu `the cat sat` và `the dog sat` gần như không chia sẻ thống kê nếu không có cơ chế backoff tường minh.

Neural LM ánh xạ token thành embedding và biểu diễn ngữ cảnh trong không gian liên tục, nhờ đó có thể chia sẻ thống kê giữa những ngữ cảnh tương tự.

Mô hình feed-forward thời kỳ đầu có dạng:

```text
một số token trước đó
→ embedding
→ MLP
→ softmax cho token tiếp theo
```

RNN loại bỏ cửa sổ cố định, còn Transformer cải thiện khả năng truy cập xa và song song hóa huấn luyện.

## Huấn luyện Maximum Likelihood

Với corpus, mô hình tối đa hóa:

\[
\sum_t\log P_\theta(x_t\mid x_{<t})
\]

Điều này tương đương tối thiểu hóa **negative log-likelihood** hoặc cross-entropy:

\[
L=-\frac1T\sum_t\log P_\theta(x_t\mid x_{<t})
\]

Trong teacher forcing, mô hình được cung cấp token thật trước đó khi huấn luyện.

## Perplexity

Nếu cross-entropy trung bình theo log tự nhiên là `H`:

\[
PPL=e^H
\]

Nếu dùng log cơ số 2:

\[
PPL=2^{H_2}
\]

Có thể hình dung perplexity như số nhánh hiệu dụng mà mô hình phải cân nhắc ở mỗi bước.

Perplexity thấp hơn trên cùng tokenizer và cùng phân bố kiểm tra thường cho thấy dự đoán token tốt hơn. Tuy nhiên không thể so sạch PPL giữa các tokenizer khác nhau vì đơn vị token đã thay đổi. PPL thấp cũng không bảo đảm instruction following, factuality hoặc reasoning tốt hơn.

## Masked Language Modeling

Mục tiêu kiểu BERT che một số token rồi dự đoán chúng bằng cả ngữ cảnh bên trái và bên phải:

\[
P(x_i\mid x_{\setminus i})
\]

Đây không phải phân rã tự hồi quy trực tiếp của xác suất chuỗi. Nó phù hợp để học biểu diễn hai chiều mạnh cho các tác vụ mã hóa, phân loại và trích xuất.

## Causal Language Modeling

Mục tiêu kiểu GPT dự đoán mỗi token chỉ từ những token trước đó. Causal mask duy trì:

\[
P(x_t\mid x_{<t})
\]

Ưu điểm là mô hình có thể sinh trực tiếp bằng cách lấy mẫu tuần tự từ phân bố token kế tiếp.

## Prefix và Seq2Seq Language Modeling

Mô hình encoder–decoder sinh chuỗi đích dựa trên chuỗi nguồn:

\[
P(y\mid x)=\prod_tP(y_t\mid y_{<t},x)
\]

Các mô hình kiểu T5 đưa nhiều tác vụ NLP về cùng khuôn dạng text-to-text, tức đầu vào văn bản → đầu ra văn bản.

## Lấy mẫu từ Language Model

Từ logits `z`, temperature thay đổi độ sắc của phân bố:

\[
p_i=softmax(z_i/T)
\]

- `T<1`: phân bố sắc hơn;
- `T>1`: phân bố phẳng hơn.

### Greedy Decoding

Chọn token có xác suất cao nhất ở mỗi bước. Cách này xác định và nhanh nhưng dễ tạo chuỗi lặp hoặc lựa chọn cục bộ không tốt về toàn chuỗi.

### Top-k

Chỉ giữ `k` token có xác suất cao nhất rồi chuẩn hóa lại để lấy mẫu.

### Top-p / Nucleus Sampling

Chọn tập token nhỏ nhất có tổng xác suất ít nhất bằng `p`, rồi lấy mẫu trong tập đó. Số candidate tự thay đổi theo độ bất định của phân bố.

Các cấu hình lấy mẫu chủ yếu thay đổi phong cách và độ đa dạng của đầu ra; chúng không bổ sung tri thức mới vào tham số mô hình.

## Exposure Bias

Khi huấn luyện, mô hình điều kiện hóa trên lịch sử token đúng; khi sinh, nó điều kiện hóa trên chính token mình đã sinh. Một lỗi sớm có thể thay đổi toàn bộ ngữ cảnh sau đó và gây lỗi dây chuyền.

Sự lệch này gọi là **exposure bias** và tồn tại trong maximum-likelihood autoregressive training chuẩn. Instruction tuning hoặc post-training bằng RL có thể thay đổi hành vi nhưng không loại bỏ bản chất tự hồi quy.

## Thoái hóa khi sinh

Nếu luôn chọn token xác suất cao nhất hoặc dùng cấu hình lấy mẫu không phù hợp, mô hình có thể lặp, tạo văn bản quá chung chung hoặc mắc vòng lặp.

Nguyên nhân liên quan hình dạng phân bố, mục tiêu huấn luyện và chiến lược giải mã. Repetition penalty có thể giúp nhưng là heuristic và có thể làm méo phân bố gốc.

## Language Model không phải Knowledge Database

Tham số mô hình mã hóa các quan hệ thống kê phân tán; hỏi một sự kiện không tương đương truy xuất chính xác một khóa từ cơ sở dữ liệu.

Hệ quả là tri thức có thể xấp xỉ, các sự kiện mâu thuẫn có thể cùng tồn tại, độ mới bị giới hạn bởi dữ liệu huấn luyện, nguồn gốc thông tin không được lưu tường minh và sự kiện hiếm thường kém tin cậy hơn.

RAG bổ sung khả năng truy cập nguồn bên ngoài có provenance rõ ràng hơn.

## Language Model không phải Truth Model

Corpus chứa cả sự thật, sai lầm, hư cấu, suy đoán và quan điểm. Next-token likelihood thưởng cho tính phù hợp với phân bố văn bản chứ không trực tiếp kiểm tra sự thật ngoài thế giới.

Đây là một nguyên nhân nền tảng của rủi ro hallucination.

## Context và In-Context Learning

Transformer LM có thể điều kiện hóa trên ví dụ hoặc chỉ dẫn nằm trong prompt mà không thay đổi tham số. Cơ chế này gọi là **học trong ngữ cảnh (in-context learning)**.

Nó khác fine-tuning: trong một prompt thông thường, trọng số mô hình giữ nguyên; chỉ trạng thái tính toán thay đổi theo token ngữ cảnh.

Phần LLM sẽ giải thích kỹ hơn.

## Scaling

Khi tăng tham số, dữ liệu và compute, loss của language model thường tuân theo những quan hệ gần dạng power law trong một số miền. Khả năng dự đoán tốt hơn có thể làm các năng lực downstream trông như “xuất hiện đột ngột”, dù một phần hiện tượng emergence phụ thuộc cách đo và ngưỡng metric.

Scaling law sẽ được trình bày riêng trong layer LLM.

## Cách nhìn từ nén dữ liệu

Một mô hình xác suất tốt có thể mã hóa chuỗi hiệu quả bằng arithmetic coding. Độ dài mã kỳ vọng liên hệ với negative log-probability:

\[
code\ length\approx-\log_2P(x)
\]

Cấu trúc càng dự đoán được thì càng có thể nén. Đây là liên hệ trực tiếp giữa language modeling và Lý thuyết thông tin.

## Mô hình tư duy

```text
Mô hình ngôn ngữ không chọn cả câu trong một lần.
Nó lặp lại việc ước lượng:
P(token tiếp theo | toàn bộ ngữ cảnh được phép nhìn thấy)
```

Sức mạnh đến từ biểu diễn ngữ cảnh đã học, dù mục tiêu đầu ra cơ bản vẫn là dự đoán phân bố token.

## Những hiểu lầm thường gặp

### “Perplexity 10 nghĩa luôn có đúng 10 lựa chọn ở mỗi token”

Không. Đó chỉ là trực giác về độ phân nhánh hiệu dụng trung bình hình học.

### “Next-token prediction quá đơn giản nên không thể học ngữ nghĩa”

Mục tiêu đơn giản trên dữ liệu lớn và đa dạng vẫn có thể buộc mô hình học biểu diễn nội bộ rất phong phú.

### “Perplexity thấp bảo đảm câu trả lời đúng sự thật”

Không. Sự thật không phải mục tiêu trực tiếp của likelihood.

### “Temperature làm mô hình thông minh hơn hoặc kém đi”

Không. Nó chỉ thay phân bố lấy mẫu từ cùng logits, không thay trọng số hoặc tri thức đã học.

## Liên kết kiến thức

Language Model nối [Lý thuyết thông tin](../01_mathematical_foundations/05_information_theory.md), [Mô hình chuỗi](../06_deep_learning_architectures/01_sequence_models.md), [Transformer](../06_deep_learning_architectures/05_transformer.md) và chuẩn bị trực tiếp cho phần pretraining LLM.