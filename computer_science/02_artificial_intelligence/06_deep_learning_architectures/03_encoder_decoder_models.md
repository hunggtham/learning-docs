# Mô hình Encoder–Decoder: tách hiểu đầu vào và tạo đầu ra

**Encoder–Decoder (인코더–디코더 / bộ mã hóa–bộ giải mã)** là một mẫu kiến trúc dùng cho các bài toán mà đầu vào và đầu ra có cấu trúc hoặc độ dài khác nhau. Bộ mã hóa (encoder) biến đầu vào thành biểu diễn nội bộ; bộ giải mã (decoder) dùng biểu diễn đó để tạo đầu ra.

Mẫu này xuất hiện trong dịch máy, tóm tắt, nhận dạng tiếng nói, tạo chú thích ảnh, autoencoder và Transformer. `Encoder` và `decoder` không phải tên của một thuật toán duy nhất mà là hai vai trò trong một hệ thống tính toán.

## Bài toán chuỗi sang chuỗi

Ví dụ dịch máy:

```text
chuỗi tiếng Anh → chuỗi tiếng Hàn
```

Độ dài đầu vào có thể khác độ dài đầu ra, nên một bộ phân loại gán nhãn từng token theo vị trí tương ứng là không đủ.

Phân phối đầu ra có thể được phân rã tự hồi quy:

\[
P(y_{1:T}\mid x)=\prod_{t=1}^{T}P(y_t\mid y_{<t},x)
\]

Bộ mã hóa xử lý `x`; bộ giải mã mô hình hóa phân phối có điều kiện của token tiếp theo.

## Seq2Seq dùng RNN thời kỳ đầu

Bộ mã hóa RNN:

\[
h_t^{enc}=f(x_t,h_{t-1}^{enc})
\]

Trạng thái cuối:

\[
c=h_T^{enc}
\]

Bộ giải mã:

\[
h_t^{dec}=g(y_{t-1},h_{t-1}^{dec},c)
\]

Trong thiết kế này, toàn bộ thông tin của chuỗi nguồn bị nén vào vector cố định `c`. Khi câu nguồn dài, đây trở thành một **nút thắt thông tin (information bottleneck)**.

## Nút thắt ngữ cảnh

Hãy hình dung chuỗi nguồn có 100 token nhưng bộ giải mã chỉ nhận một vector duy nhất. Dù vector có nhiều chiều, nó vẫn phải giữ đủ mọi chi tiết cần thiết cho tất cả bước sinh đầu ra.

Hiệu năng thường giảm khi đầu vào dài. Đây là một động lực chính dẫn đến attention: ở mỗi bước, bộ giải mã có thể xây ngữ cảnh động từ toàn bộ trạng thái của bộ mã hóa thay vì phụ thuộc hoàn toàn vào một vector cuối.

## Teacher Forcing trong bộ giải mã

Khi huấn luyện, bộ giải mã thường được cung cấp token đích đúng ở bước trước:

\[
P(y_t\mid y_{<t}^{true},x)
\]

Khi suy luận, mô hình phải dựa vào chính các token đã sinh ra trước đó. Sự khác biệt này tạo ra **thiên lệch phơi nhiễm (exposure bias)**: một lỗi sớm có thể làm lịch sử đầu vào cho các bước sau khác với lịch sử mà mô hình thường thấy trong huấn luyện.

Dù vậy, **teacher forcing** vẫn là phương pháp huấn luyện chuẩn và hiệu quả cho nhiều mô hình tự hồi quy.

## Token bắt đầu và kết thúc

Bộ giải mã cần biết khi nào chuỗi bắt đầu và khi nào nên dừng. Hai token đặc biệt thường gặp là:

```text
<BOS>  bắt đầu chuỗi (beginning of sequence)
<EOS>  kết thúc chuỗi (end of sequence)
```

Quá trình sinh dừng khi tạo `<EOS>` hoặc đạt giới hạn độ dài tối đa. Các giao thức chat hiện đại có nhiều token điều khiển phức tạp hơn, nhưng nguyên lý vẫn giống nhau: cấu trúc của cuộc hội thoại hoặc chuỗi được mã hóa bằng quy ước token.

## Thuật toán giải mã

Ở mỗi bước, mô hình tạo một phân phối xác suất. Việc biến các phân phối từng bước thành một chuỗi cuối cùng là một bài toán tìm kiếm.

### Giải mã tham lam (Greedy Decoding)

\[
y_t=\arg\max_kP(y_t=k\mid context)
\]

Cách này nhanh, nhưng lựa chọn tốt nhất tại một bước chưa chắc tạo ra chuỗi tốt nhất về tổng thể.

### Tìm kiếm chùm (Beam Search)

Giữ `B` giả thuyết từng phần tốt nhất theo tổng log-xác suất:

```text
bước 1: giữ B ứng viên
bước 2: mở rộng từng ứng viên → giữ lại B ứng viên tốt nhất
...
```

Beam Search là một dạng tìm kiếm heuristic trong không gian chuỗi. Thường cần chuẩn hóa theo độ dài vì tổng log-xác suất có xu hướng ưu tiên chuỗi ngắn.

### Lấy mẫu (Sampling)

Với sinh nội dung mở, có thể lấy mẫu từ phân phối thay vì luôn chọn token xác suất cao nhất. Các kỹ thuật như temperature, top-k và top-p sẽ được trình bày kỹ hơn trong phần LLM.

Dịch máy truyền thống thường ưu tiên Beam Search; sinh văn bản sáng tạo thường sử dụng lấy mẫu.

## Kiến trúc chỉ có Encoder

Nếu đầu ra là nhãn hoặc biểu diễn thay vì một chuỗi cần sinh, không nhất thiết phải có decoder.

Các mô hình kiểu BERT là **encoder-only**: self-attention hai chiều tạo biểu diễn theo ngữ cảnh để phục vụ phân loại, trích xuất hoặc các tác vụ hiểu ngôn ngữ.

## Kiến trúc chỉ có Decoder

Nếu bài toán là tiếp tục chuỗi dựa trên tiền tố, kiến trúc **decoder-only** là đủ. Các mô hình kiểu GPT sử dụng self-attention nhân quả:

\[
P(x_t\mid x_{<t})
\]

Prompt đóng vai trò chuỗi điều kiện ban đầu, nên không cần một module encoder riêng biệt.

## Transformer Encoder–Decoder

Trong Transformer gốc và các mô hình kiểu T5:

- encoder dùng self-attention hai chiều trên chuỗi nguồn;
- decoder dùng self-attention nhân quả trên chuỗi đích đang sinh;
- cross-attention cho phép decoder truy cập biểu diễn từ encoder.

Cấu trúc này phù hợp tự nhiên với dịch máy và các bài toán sinh có điều kiện.

## Cross-Attention

Trạng thái của decoder tạo truy vấn (query), còn đầu ra của encoder tạo khóa (key) và giá trị (value):

\[
Attention(Q_{dec},K_{enc},V_{enc})
\]

Ở mỗi vị trí đầu ra, decoder có thể truy xuất phần thông tin nguồn phù hợp. Có thể xem **cross-attention** như một cơ chế truy xuất khả vi được học giữa các vị trí của hai chuỗi.

## Không chỉ dành cho văn bản

Tạo chú thích ảnh:

```text
bộ mã hóa ảnh → token/đặc trưng thị giác
        ↓ cross-attention
bộ giải mã văn bản → chú thích
```

Dịch tiếng nói:

```text
bộ mã hóa âm thanh → biểu diễn âm học
bộ giải mã văn bản → văn bản đã dịch
```

Nhiều mô hình đa phương thức hiện đại cũng dùng dạng bộ mã hóa hoặc projection cho modality đầu vào kết hợp với LLM dạng decoder.

## Autoencoder và nút thắt tiềm ẩn

Autoencoder cũng có cấu trúc encoder–decoder:

\[
x\xrightarrow{encoder}z\xrightarrow{decoder}\hat x
\]

Nhưng mục tiêu là tái tạo đầu vào, không phải dịch chuỗi có điều kiện. Cùng một mẫu kiến trúc có thể mang ý nghĩa xác suất và mục tiêu huấn luyện khác nhau.

## Phân loại kiến trúc bằng luồng thông tin

Thay vì chỉ ghi nhớ tên mô hình, nên hỏi:

```text
Encoder được nhìn thấy những vị trí nào?
Decoder được nhìn thấy những vị trí nào?
Decoder truy cập nguồn ở đâu và bằng cơ chế nào?
Quá trình sinh có nhân quả không?
Có nút thắt biểu diễn nào không?
```

Mặt nạ attention và cấu trúc kết nối quyết định luồng thông tin của hệ thống.

## Mô hình tư duy

> Encoder trả lời “đầu vào nên được biểu diễn như thế nào?”. Decoder trả lời “từ biểu diễn đó và những đầu ra đã có, nên tạo phần tiếp theo như thế nào?”.

Cross-attention loại bỏ yêu cầu phải ép mọi chi tiết của chuỗi nguồn vào một vector duy nhất.

## Những hiểu lầm thường gặp

### “Encoder chỉ là embedding layer, decoder chỉ là output layer”

Không. Cả encoder và decoder thường là các mạng nhiều tầng với quá trình tính toán phong phú.

### “Mọi Transformer đều có cả encoder và decoder”

Không. Có ba họ chính: encoder-only, decoder-only và encoder–decoder.

### “Beam Search đảm bảo tìm chuỗi có xác suất cao nhất”

Không. Beam hữu hạn là tìm kiếm heuristic; tìm kiếm chính xác trên toàn bộ không gian chuỗi thường không khả thi.

### “LLM decoder-only không xử lý đầu vào vì không có encoder”

Prompt được đưa qua chính các tầng Transformer nhân quả để tạo biểu diễn theo ngữ cảnh; không cần module encoder tách biệt.

## Liên kết kiến thức

Encoder–Decoder nối [Tìm kiếm](../02_search_reasoning_and_planning/00_state_space_and_search.md), [Mô hình chuỗi](./01_sequence_models.md), [RNN/LSTM](./02_rnn_lstm_gru.md) và trực tiếp dẫn tới [Attention](./04_attention.md).