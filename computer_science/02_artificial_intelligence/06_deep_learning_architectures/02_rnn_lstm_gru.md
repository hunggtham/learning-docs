# RNN, LSTM và GRU: học trạng thái qua thời gian

Mạng nơ-ron hồi quy (**Recurrent Neural Network — RNN / 순환 신경망**) xử lý dữ liệu chuỗi bằng cách tái sử dụng cùng một hàm chuyển trạng thái qua các bước thời gian (timesteps). Thay vì xem từng vị trí là độc lập, mô hình duy trì **trạng thái ẩn (hidden state)** để mang thông tin từ quá khứ sang hiện tại.

RNN là một bước phát triển quan trọng trong lịch sử học sâu vì nó biến chuỗi có độ dài thay đổi thành một quá trình tính toán khả vi có trạng thái. LSTM và GRU được phát triển để giảm khó khăn khi truyền tín hiệu và gradient qua các phụ thuộc dài hạn.

## RNN cơ bản

Cập nhật trạng thái:

\[
h_t=\phi(W_{xh}x_t+W_{hh}h_{t-1}+b_h)
\]

Đầu ra:

\[
y_t=g(W_{hy}h_t+b_y)
\]

Cùng các trọng số `W` được tái sử dụng ở mọi bước thời gian, tức là mô hình **chia sẻ tham số theo thời gian (parameter sharing across time)**.

## Trải mạng theo thời gian

Có thể hình dung RNN được trải ra (unroll) như sau:

```text
x1 → [ô RNN] → h1
       ↓
x2 → [ô RNN] → h2
       ↓
x3 → [ô RNN] → h3
```

Về mặt toán học, độ sâu của đồ thị tính toán tăng theo độ dài chuỗi. Khi huấn luyện, lan truyền ngược phải đi qua đồ thị đã trải này; cơ chế đó gọi là **lan truyền ngược qua thời gian (Backpropagation Through Time — BPTT)**.

## Gradient tiêu biến trong RNN

Gradient đi qua nhiều bước thời gian chứa các tích lặp của Jacobian hồi quy:

\[
\frac{\partial h_t}{\partial h_k}
=\prod_{i=k+1}^{t}\frac{\partial h_i}{\partial h_{i-1}}
\]

Nếu chuẩn của các đạo hàm lặp lại thường nhỏ hơn `1`, gradient có thể giảm rất nhanh và trở nên gần bằng `0`; nếu chúng thường lớn hơn `1`, gradient có thể bùng nổ. Vì vậy RNN cơ bản gặp khó khăn khi học các phụ thuộc cách nhau rất xa trong chuỗi.

## BPTT cắt ngắn

Với chuỗi dài, có thể chỉ lan truyền gradient ngược qua `K` bước gần nhất thay vì toàn bộ lịch sử. Trạng thái ẩn vẫn tiếp tục được truyền về phía trước, nhưng đồ thị gradient được ngắt định kỳ.

Sự đánh đổi là:

```text
ít bộ nhớ và phép tính hơn
↔
khó gán tín hiệu học trực tiếp qua các phụ thuộc dài hơn cửa sổ cắt ngắn
```

Kỹ thuật này được gọi là **BPTT cắt ngắn (truncated BPTT)**.

## LSTM: đường truyền bộ nhớ có các cổng

**Long Short-Term Memory (LSTM / 장단기 메모리)** bổ sung trạng thái ô `c_t` và các **cổng (gates)** để kiểm soát thông tin được giữ, ghi và đưa ra ngoài.

Cổng quên (forget gate):

\[
f_t=\sigma(W_f[x_t,h_{t-1}]+b_f)
\]

Cổng đầu vào (input gate):

\[
i_t=\sigma(W_i[x_t,h_{t-1}]+b_i)
\]

Trạng thái ứng viên (candidate):

\[
\tilde c_t=\tanh(W_c[x_t,h_{t-1}]+b_c)
\]

Cập nhật trạng thái ô:

\[
c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t
\]

Cổng đầu ra (output gate):

\[
o_t=\sigma(W_o[x_t,h_{t-1}]+b_o)
\]

Trạng thái ẩn:

\[
h_t=o_t\odot\tanh(c_t)
\]

## Vì sao LSTM giúp gradient truyền xa hơn?

Cập nhật trạng thái ô có một đường cộng trực tiếp:

\[
c_t=f_t\odot c_{t-1}+...
\]

Đạo hàm tương ứng là:

\[
\frac{\partial c_t}{\partial c_{t-1}}=f_t
\]

Nếu cổng quên có giá trị gần `1`, thông tin và gradient có thể đi qua nhiều bước với ít lần bị nén bởi hàm phi tuyến hơn so với RNN cơ bản. LSTM không loại bỏ hoàn toàn vấn đề phụ thuộc dài hạn, nhưng cải thiện khả năng học chúng đáng kể.

## Ý nghĩa của các cổng

Có thể hiểu trực giác các cổng như sau: cổng quên quyết định bao nhiêu thông tin cũ được giữ lại; cổng đầu vào quyết định bao nhiêu thông tin ứng viên mới được ghi vào bộ nhớ; cổng đầu ra quyết định phần nào của trạng thái ô được bộc lộ qua trạng thái ẩn.

Các ý nghĩa này chỉ là cách giải thích chức năng. Giá trị của cổng được mô hình học từ dữ liệu chứ không phải các quy tắc ngữ nghĩa được lập trình thủ công.

## GRU

**Gated Recurrent Unit (GRU / 게이트 순환 유닛)** đơn giản hóa LSTM bằng cách hợp nhất một phần cơ chế bộ nhớ và trạng thái ẩn.

Cổng cập nhật (update gate):

\[
z_t=\sigma(W_z[x_t,h_{t-1}])
\]

Cổng đặt lại (reset gate):

\[
r_t=\sigma(W_r[x_t,h_{t-1}])
\]

Trạng thái ứng viên:

\[
\tilde h_t=\tanh(W_h[x_t,r_t\odot h_{t-1}])
\]

Cập nhật:

\[
h_t=(1-z_t)\odot h_{t-1}+z_t\odot\tilde h_t
\]

GRU có ít cổng và ít tham số hơn LSTM. Điều đó có thể làm mô hình nhẹ hơn, nhưng hiệu quả cuối cùng vẫn phụ thuộc dữ liệu và bài toán; không có quy tắc rằng GRU luôn tốt hơn hoặc kém hơn LSTM.

## RNN hai chiều

Nếu bài toán cho phép sử dụng cả ngữ cảnh trước và sau một vị trí, có thể chạy một RNN theo chiều thuận và một RNN theo chiều ngược:

\[
h_t=[\overrightarrow h_t;\overleftarrow h_t]
\]

Đây là **RNN hai chiều (bidirectional RNN)**, hữu ích cho gán nhãn chuỗi, nhận dạng tiếng nói hoặc bộ mã hóa khi toàn bộ đầu vào đã có sẵn.

Nó không thể được dùng trực tiếp theo cùng cách cho sinh tự hồi quy nhân quả nếu token tương lai chưa tồn tại tại thời điểm dự đoán.

## RNN nhiều tầng

Có thể chồng nhiều tầng hồi quy:

```text
chuỗi đầu vào
→ tầng RNN 1
→ tầng RNN 2
→ ...
```

Khi đó đồ thị vừa sâu theo thời gian vừa sâu theo số tầng, khiến tối ưu khó hơn. Dropout, kết nối tắt (residual connection) và các kỹ thuật chuẩn hóa có thể giúp ổn định quá trình huấn luyện.

## Nút thắt biểu diễn chuỗi

Trong mô hình nhiều-đến-một (many-to-one), trạng thái ẩn cuối `h_T` thường phải tóm tắt toàn bộ chuỗi. Khi chuỗi dài, việc ép mọi thông tin vào một vector kích thước cố định tạo ra **nút thắt thông tin (information bottleneck)**.

Các mô hình dịch máy encoder–decoder thời kỳ đầu gặp rõ vấn đề này. Attention giải quyết một phần bằng cách cho bộ giải mã truy cập trực tiếp nhiều trạng thái của bộ mã hóa thay vì chỉ dựa vào một vector cuối cùng.

## Điểm mạnh của RNN

RNN xử lý luồng dữ liệu từng bước và duy trì một trạng thái có kích thước cố định cho mỗi tầng. Khi suy luận trực tuyến, mô hình có thể cập nhật trạng thái khi dữ liệu mới đến mà không cần giữ toàn bộ lịch sử đầu vào trong bộ nhớ.

Đặc tính này phù hợp với một số bài toán chuỗi thời gian, âm thanh trực tuyến, thiết bị biên và hệ thống cần độ trễ thấp.

## Hạn chế của RNN so với Transformer

Trong huấn luyện, trạng thái `h_t` phụ thuộc `h_{t-1}`, nên các bước thời gian khó được tính song song hoàn toàn. Transformer có thể xử lý nhiều vị trí cùng lúc trong một tầng attention.

Ngoài ra, đường truyền thông tin giữa hai vị trí cách xa nhau trong RNN có độ dài `O(T)` bước hồi quy, trong khi self-attention có thể kết nối trực tiếp hai vị trí trong cùng một tầng. Lợi thế về đường truyền gradient và khả năng song song là những nguyên nhân quan trọng khiến Transformer thống trị nhiều bài toán NLP quy mô lớn.

## RNN vẫn còn giá trị

RNN, LSTM và GRU vẫn hữu ích trong nhiều trường hợp như dữ liệu chuỗi thời gian nhỏ hoặc vừa, xử lý streaming, thiết bị nhúng, mô hình có trạng thái liên tục và các miền mà recurrence phù hợp tự nhiên với cấu trúc bài toán.

Các **mô hình không gian trạng thái (state-space models)** hiện đại cũng đưa ý tưởng cập nhật trạng thái tuần tự trở lại với thiết kế hiệu quả hơn cho chuỗi dài.

## Encoder–Decoder dùng RNN

Bộ mã hóa xử lý chuỗi nguồn thành các trạng thái; bộ giải mã sinh chuỗi đích theo từng bước và điều kiện hóa trên thông tin từ bộ mã hóa. Việc bổ sung attention là cầu nối trực tiếp từ kiến trúc RNN encoder–decoder sang các kiến trúc hiện đại hơn.

Xem [Mô hình Encoder–Decoder](./03_encoder_decoder_models.md) và [Attention](./04_attention.md).

## Mô hình tư duy

```text
RNN  = liên tục cập nhật một trạng thái nén của quá khứ
LSTM = trạng thái + các cổng học được để giữ, ghi và đọc thông tin
GRU  = cơ chế cập nhật trạng thái có cổng nhưng gọn hơn LSTM
```

## Những hiểu lầm thường gặp

### “LSTM có thể nhớ vô hạn”

Không. Các cổng giúp duy trì thông tin tốt hơn, nhưng năng lực biểu diễn, nhiễu, độ dài chuỗi và quá trình tối ưu vẫn giới hạn trí nhớ thực tế.

### “GRU ít tham số hơn nên luôn tốt hơn”

GRU thường rẻ hơn về tính toán, nhưng chất lượng phụ thuộc cấu trúc dữ liệu và bài toán.

### “RNN đã lỗi thời vì có Transformer”

Transformer thống trị nhiều bài toán chuỗi quy mô lớn, nhưng recurrence vẫn có lợi khi cần streaming hoặc bị giới hạn tài nguyên.

### “Trạng thái ẩn là bộ nhớ có thể đọc như văn bản”

Không. Nó là một vector biểu diễn phân tán được học từ dữ liệu, không phải bộ nhớ ký hiệu tường minh.

## Liên kết kiến thức

RNN sử dụng trực tiếp [Lan truyền ngược](../05_neural_networks/04_backpropagation.md), [cắt gradient và bộ tối ưu](../05_neural_networks/05_gradient_descent_and_optimizers.md), đồng thời kế thừa ý tưởng trạng thái từ mô hình chuỗi. Attention xuất hiện một phần vì việc nén toàn bộ lịch sử vào trạng thái hồi quy cố định trở thành nút thắt.