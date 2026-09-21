# Mô hình chuỗi: dữ liệu có thứ tự cần cách xử lý khác gì?

**Dữ liệu chuỗi (sequence data / 순차 데이터)** khác với một vector đặc trưng cố định không có thứ tự vì **thứ tự và ngữ cảnh (context)** mang ý nghĩa. Câu `dog bites man` khác `man bites dog`; một tập giá trị cảm biến giống nhau nhưng xuất hiện theo thứ tự khác có thể mô tả hai quá trình động hoàn toàn khác nhau. Vì vậy mô hình chuỗi phải xử lý độ dài biến đổi, quan hệ phụ thuộc giữa các vị trí và đôi khi cả hướng nhân quả của thông tin.

Trước khi học RNN hay Transformer, cần hiểu chính bài toán mô hình hóa chuỗi (sequence modeling) đang yêu cầu điều gì.

## Ký hiệu chuỗi

Một chuỗi có thể viết:

\[
x_{1:T}=(x_1,x_2,...,x_T)
\]

Cấu trúc đầu ra có nhiều dạng:

- chuỗi → một đầu ra: sentiment hoặc classification;
- một đầu vào → chuỗi: sinh có điều kiện;
- chuỗi → chuỗi cùng nhịp: tagging;
- chuỗi → chuỗi khác độ dài: translation;
- dự đoán bước tiếp theo theo kiểu tự hồi quy (autoregressive).

Kiến trúc phải phù hợp với cấu trúc đầu ra của bài toán.

## Giả định Markov

Mô hình chuỗi đơn giản nhất có thể giả định tương lai chỉ phụ thuộc vào một phần quá khứ gần.

Markov bậc một:

\[
P(x_t\mid x_{1:t-1})=P(x_t\mid x_{t-1})
\]

Giả định này làm bài toán đơn giản hơn rất nhiều nhưng loại bỏ các phụ thuộc dài hạn.

Tăng bậc Markov cho phép dùng ngữ cảnh dài hơn nhưng số tổ hợp trạng thái tăng rất nhanh.

RNN cố gắng học một **trạng thái ẩn (hidden state)** nén lịch sử trước đó thay vì giữ trực tiếp toàn bộ tổ hợp của nhiều bước quá khứ.

## Phân rã tự hồi quy

Mọi phân phối chung trên chuỗi đều có thể phân rã theo quy tắc xác suất:

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

Language Model sử dụng nguyên lý này. Transformer thay đổi cơ chế tính ngữ cảnh, chứ không thay đổi chính phép phân rã xác suất trên.

Quá trình sinh tự hồi quy lặp lại:

```text
ngữ cảnh
→ dự đoán phân phối của phần tử tiếp theo
→ chọn / lấy mẫu một phần tử
→ nối vào chuỗi
→ lặp lại
```

## Trạng thái của chuỗi

Mô hình hồi quy duy trì trạng thái ẩn:

\[
h_t=f(h_{t-1},x_t)
\]

`h_t` cố gắng nén những thông tin liên quan trong lịch sử `x_{1:t}`.

Cách này gọn nhưng tạo **nút thắt thông tin (information bottleneck)**: toàn bộ lịch sử dài phải truyền qua một vector trạng thái có kích thước cố định.

Attention sau này giảm hạn chế này bằng cách cho phép mô hình truy cập trực tiếp nhiều trạng thái nguồn thay vì ép mọi thông tin vào một vector duy nhất.

## Độ dài biến đổi, Padding và Masking

Khi gom các chuỗi có độ dài khác nhau thành batch, hệ thống thường dùng **padding** để đưa chúng về cùng một chiều dài tensor.

Mô hình và loss phải dùng **mask** để bỏ qua những vị trí padding không mang dữ liệu thật.

Nếu padding vô tình tham gia attention hoặc loss, mô hình có thể học artefact từ chính ký hiệu đệm và metric cũng bị sai.

Batch chuỗi còn có thể dùng **bucketing theo độ dài** để gom những chuỗi gần cùng chiều dài, nhờ đó giảm phần compute lãng phí trên padding.

## Thông tin vị trí là bắt buộc

RNN xử lý phần tử theo thứ tự tuần tự nên bản thân recurrence đã mang thông tin vị trí.

Self-attention thuần túy không có positional information lại có tính đồng biến theo hoán vị: nếu đổi thứ tự token, các tương tác giữa cùng tập token cũng chỉ bị đổi vị trí tương ứng.

Transformer vì vậy phải đưa thông tin vị trí vào rõ ràng, chẳng hạn:

- sinusoidal positional encoding;
- learned position embedding;
- relative position bias;
- RoPE;
- ALiBi.

Thông tin vị trí không phải chi tiết trang trí; nó cung cấp cho mô hình hình học và thứ tự của chuỗi.

## Ngữ cảnh một chiều và hai chiều

Trong mô hình **nhân quả (causal)**, vị trí `t` chỉ được phép nhìn `x_{<t}`. Điều này cần thiết cho sinh tự hồi quy để tránh nhìn thấy token tương lai trong training.

Encoder hai chiều có thể nhìn cả ngữ cảnh bên trái và bên phải, phù hợp hơn với các bài toán hiểu văn bản, classification hoặc masked modeling.

**Attention mask** quyết định luồng thông tin nào được phép đi qua giữa các vị trí.

Hai mô hình có thể có kiến trúc rất giống nhau nhưng khác mask và objective sẽ mang semantics rất khác.

## Teacher Forcing

Trong training tự hồi quy, mô hình thường nhận token trước đó từ chuỗi ground truth thay vì token mà chính nó vừa sinh:

\[
P(x_t\mid x_{<t}^{true})
\]

Cơ chế này gọi là **Teacher Forcing**.

Khi inference, mô hình lại phải điều kiện hóa trên lịch sử do chính nó sinh. Một lỗi ở bước sớm có thể làm ngữ cảnh những bước sau khác distribution training và lỗi tiếp tục tích lũy. Sự khác biệt này thường được gọi là **exposure bias**.

Scheduled Sampling từng được đề xuất để giảm khoảng cách giữa training và inference, nhưng Language Model hiện đại vẫn chủ yếu dùng Teacher Forcing cho next-token training rồi xử lý hành vi bằng quy mô dữ liệu, objective, fine-tuning và chiến lược inference.

## Sequence-to-Sequence

Trong translation, độ dài input và output có thể khác nhau.

Encoder xây representation của chuỗi nguồn; decoder sinh chuỗi đích theo kiểu tự hồi quy và điều kiện hóa trên thông tin từ encoder.

Các mô hình seq2seq RNN đời đầu nén toàn bộ chuỗi nguồn vào hidden state cuối, tạo một bottleneck lớn. Attention sau đó cho decoder truy cập trực tiếp toàn bộ encoder state theo nhu cầu.

Con đường lịch sử này dẫn trực tiếp tới kiến trúc Transformer.

## Phụ thuộc theo nhiều thang thời gian

Quan hệ phụ thuộc trong chuỗi có thể nằm ở nhiều khoảng cách khác nhau:

- phoneme phụ thuộc các frame âm thanh gần nhau;
- ngữ pháp có thể kéo dài qua nhiều mệnh đề;
- tham chiếu trong tài liệu có thể cách nhau nhiều đoạn;
- seasonality trong time series có thể kéo dài theo ngày, tuần hoặc tháng.

Mô hình cần phạm vi ngữ cảnh phù hợp với task.

RNN về lý thuyết có thể mang lịch sử rất dài nhưng trong thực tế memory và gradient suy giảm. CNN cho sequence có receptive field hữu hạn nếu không tăng depth hoặc dilation. Attention kết nối trực tiếp vị trí xa nhau nhưng self-attention chuẩn có chi phí bậc hai theo chiều dài chuỗi.

## Mô hình không gian trạng thái

Mô hình không gian trạng thái (state-space model) cổ điển có dạng:

\[
h_t=Ah_{t-1}+Bx_t
\]

\[
y_t=Ch_t+Dx_t
\]

Kalman Filter bổ sung các giả định xác suất về nhiễu và trạng thái ẩn.

Các mô hình neural không gian trạng thái có cấu trúc, như họ S4 hoặc Mamba, quay lại ý tưởng recurrence hoặc convolution nhưng tổ chức computation theo cách hiệu quả hơn cho chuỗi dài.

Bức tranh sequence modeling vì vậy rộng hơn rất nhiều so với chỉ “RNN hay Transformer”.

## Time Series và Language khác nhau thế nào?

Cả hai đều là chuỗi nhưng mang các giả định khác nhau.

Time series có thể có timestamp thật, khoảng lấy mẫu không đều, seasonality đã biết, biến ngoại sinh và giá trị liên tục.

Language dùng token rời rạc, thứ tự tương đối và next-token prediction là một objective tự nhiên.

Không nên lấy nguyên một kiến trúc NLP rồi áp vào time series mà bỏ qua semantics của thời gian.

## Đánh giá mô hình chuỗi

Token accuracy có thể bỏ sót chất lượng toàn chuỗi.

Translation có thể dùng BLEU hoặc COMET; speech dùng WER; forecasting dùng MAE, RMSE hoặc probabilistic score; generation thường cần thêm human evaluation hoặc model-based evaluation.

Lỗi có thể tích lũy theo chiều dài chuỗi, vì vậy metric trên từng bước và metric ở cấp sequence có thể cho hai bức tranh rất khác nhau.

## Mô hình tư duy

> Mô hình hóa chuỗi là bài toán biểu diễn thông tin phân bố trên các vị trí có thứ tự, xác định mỗi output được phép nhìn phần ngữ cảnh quá khứ hoặc tương lai nào, rồi học quan hệ phụ thuộc trên đúng thang thời gian của task.

## Các hiểu lầm thường gặp

### “RNN nhớ được toàn bộ sequence”

Không. Hidden state có capacity hữu hạn và thông tin dài hạn có thể suy giảm.

### “Transformer tự biết thứ tự vì token đã nằm đúng thứ tự trong mảng”

Không. Self-attention cần positional signal hoặc mask để cấu trúc thứ tự có ý nghĩa đối với phép tính.

### “Mọi task dạng sequence đều phải autoregressive”

Không. Classification, tagging, denoising và forecasting có thể dùng objective và ngữ cảnh khác nhau.

### “Time series chỉ là text nhưng thay token bằng số”

Không. Thang thời gian thật, giá trị liên tục, sampling không đều và biến ngoại sinh tạo các ràng buộc mô hình hóa riêng.

## Liên kết kiến thức

Mô hình chuỗi nối các ý tưởng về trạng thái và Markov trong [Ra quyết định dưới bất định](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md), [Suy luận xác suất](../03_knowledge_and_reasoning/04_probabilistic_reasoning.md) và Neural Network.

Xem tiếp: [RNN, LSTM và GRU](./02_rnn_lstm_gru.md).