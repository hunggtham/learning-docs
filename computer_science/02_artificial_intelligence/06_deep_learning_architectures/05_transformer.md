# Transformer: Attention + tính toán Residual ở quy mô lớn

**Transformer (트랜스포머)** không chỉ là “mô hình dùng attention”. Đây là một kiến trúc tổ chức tính toán thành các khối lặp gồm attention, mạng truyền thẳng (feed-forward), kết nối tắt (residual connection) và chuẩn hóa (normalization). Thiết kế này cho phép các vị trí trong chuỗi được xử lý song song khi huấn luyện và tạo đường truyền ngắn hơn giữa những token cách xa nhau so với RNN.

Transformer là nền tảng của BERT, GPT, T5, Vision Transformer và phần lớn mô hình nền tảng (foundation model) hiện đại. Vì vậy cần hiểu cấu trúc ở mức tensor và cơ chế tính toán, không chỉ ghi nhớ sơ đồ kiến trúc.

## Biểu diễn đầu vào

Token ID được tra trong ma trận embedding:

\[
E\in R^{|V|\times d_{model}}
\]

Token `i` nhận vector:

\[
x_i=E[token_i]
\]

Sau đó mô hình bổ sung hoặc mã hóa thông tin vị trí.

Tensor trạng thái ẩn thường có dạng:

\[
X\in R^{B\times T\times d_{model}}
\]

trong đó `B` là kích thước batch, `T` là độ dài chuỗi và `d_model` là chiều biểu diễn.

## Khối Transformer cốt lõi

Một khối **pre-norm** đơn giản hóa có thể viết:

\[
H'=H+Attention(Norm(H))
\]

\[
H''=H'+FFN(Norm(H'))
\]

Cấu trúc này được lặp qua `L` tầng.

Hai tầng con chính là:

1. **Attention** — trao đổi thông tin giữa các vị trí trong chuỗi.
2. **Mạng truyền thẳng (Feed-Forward Network — FFN)** — biến đổi đặc trưng ở từng vị trí một cách độc lập.

**Dòng residual (residual stream)** mang biểu diễn xuyên suốt toàn bộ chồng tầng.

## Tầng con Self-Attention

Từ trạng thái ẩn đã chuẩn hóa:

\[
Q=XW_Q,
K=XW_K,
V=XW_V
\]

sau đó:

\[
A=softmax\left(\frac{QK^T}{\sqrt{d_k}}+M\right)
\]

\[
O=AVW_O
\]

`M` là mặt nạ hoặc độ lệch attention.

Attention cho phép token trộn thông tin với token khác. Nếu bỏ cơ chế này, FFN chuẩn chỉ xử lý từng vị trí riêng lẻ và không tự trao đổi thông tin giữa các token.

## Mạng Feed-Forward

FFN của Transformer cổ điển:

\[
FFN(x)=W_2\phi(W_1x+b_1)+b_2
\]

được áp dụng độc lập lên từng token nhưng dùng chung trọng số.

Thiết kế cổ điển thường dùng:

\[
d_{ff}\approx4d_{model}
\]

Các Transformer hiện đại dùng những biến thể có cổng như SwiGLU và tỷ lệ chiều khác.

Có thể nhớ ngắn gọn: attention trộn thông tin **giữa các vị trí**, còn FFN biến đổi thông tin **giữa các chiều đặc trưng** của mỗi vị trí.

## Dòng Residual

Cập nhật residual có dạng:

\[
x\leftarrow x+F(x)
\]

Tầng con không thay thế hoàn toàn biểu diễn hiện tại mà ghi thêm một phần cập nhật vào dòng biểu diễn chung. Điều này giúp gradient truyền ổn định hơn và cho phép nhiều tầng cùng đóng góp dần vào biểu diễn.

Một mô hình tư duy hữu ích là xem residual stream như một “kênh giao tiếp” mà các khối attention và MLP đọc rồi ghi cập nhật trở lại. Đây chỉ là phép so sánh khái niệm, không phải bus phần mềm theo nghĩa đen.

## LayerNorm và RMSNorm

Mẫu pre-norm phổ biến:

```text
x
├───────────────┐
↓ Norm          │
↓ Attention     │
└→ + residual ──┘
↓
├───────────────┐
↓ Norm          │
↓ MLP           │
└→ + residual ──┘
```

Pre-norm thường giúp các Transformer rất sâu dễ tối ưu hơn vì đường residual đồng nhất được giữ tương đối sạch. Nhiều LLM hiện đại dùng **RMSNorm** thay cho LayerNorm.

## Transformer dạng Encoder

Encoder thường dùng self-attention hai chiều: mỗi token không bị mask có thể truy cập những token khác trong chuỗi.

Thiết kế này phù hợp với các bài toán cần biểu diễn hoặc hiểu toàn bộ đầu vào. Các mô hình kiểu BERT dùng chồng encoder và mục tiêu mô hình hóa ngôn ngữ có che token (masked language modeling).

## Transformer dạng Decoder

Decoder-only sử dụng mặt nạ nhân quả:

\[
M_{ij}=-\infty\quad j>i
\]

nên vị trí `i` không thể thấy token tương lai.

Các mô hình kiểu GPT huấn luyện theo phân rã:

\[
P(x_{1:T})=\prod_tP(x_t\mid x_{<t})
\]

Dù có mặt nạ nhân quả, khi huấn luyện toàn bộ vị trí vẫn có thể được tính song song vì chuỗi đích đã có sẵn.

## Transformer Encoder–Decoder

Encoder xây biểu diễn hai chiều của chuỗi nguồn. Decoder thường có ba tầng con:

1. self-attention nhân quả;
2. cross-attention trên đầu ra encoder;
3. FFN.

Cấu trúc này phù hợp với dịch máy, tóm tắt và sinh có điều kiện.

## Kích thước Multi-Head

Ví dụ:

\[
d_{model}=4096,
\quad h=32
\]

thì chiều head cổ điển là:

\[
d_{head}=128
\]

Q/K/V được chiếu rồi đổi hình dạng:

```text
[B, T, D]
→ [B, T, H, Dh]
→ chuyển trục thành [B, H, T, Dh]
```

Khả năng suy luận chính xác về shape tensor là kỹ năng thiết yếu khi triển khai và tối ưu Transformer.

## Mã hóa vị trí

Transformer gốc dùng mã hóa hình sin:

\[
PE(pos,2i)=\sin(pos/10000^{2i/d})
\]

\[
PE(pos,2i+1)=\cos(pos/10000^{2i/d})
\]

LLM hiện đại thường dùng RoPE hoặc cơ chế vị trí tương đối.

Thiết kế vị trí ảnh hưởng trực tiếp tới khả năng mở rộng context. Tăng một con số cấu hình về độ dài tối đa không đồng nghĩa mô hình sẽ hoạt động tốt ở độ dài chưa từng được huấn luyện.

## Số tham số chủ yếu đến từ đâu?

Với một tầng decoder, bỏ qua bias và norm, các phép chiếu attention Q/K/V/O cổ điển dùng xấp xỉ:

\[
4d^2
\]

tham số. MQA/GQA có thể giảm phần K/V.

FFN dùng xấp xỉ:

\[
2d\,d_{ff}
\]

với FFN hai ma trận; FFN có cổng thường có ba ma trận. Trong nhiều LLM, số tham số ở FFN lớn hơn phần attention.

Embedding và đầu chiếu ra vocabulary cũng chiếm lượng tham số đáng kể.

## Chia sẻ trọng số đầu vào và đầu ra

Embedding đầu vào và ma trận chiếu đầu ra có thể dùng chung trọng số:

\[
W_{out}=E^T
\]

Kỹ thuật **weight tying** này giảm số tham số và liên kết hình học của biểu diễn token đầu vào với đầu ra. Nó phổ biến nhưng không bắt buộc.

## Độ phức tạp tính toán

Self-attention có chi phí gần:

\[
O(T^2d)
\]

FFN có chi phí gần:

\[
O(Td^2)
\]

Thành phần nào chiếm ưu thế phụ thuộc quan hệ giữa độ dài chuỗi `T` và chiều mô hình `d`. Context rất dài làm chi phí attention bậc hai nổi bật; với chuỗi ngắn nhưng mô hình rất rộng, các phép chiếu và FFN có thể chiếm nhiều FLOP hơn.

## Huấn luyện song song nhưng sinh tuần tự

Trong huấn luyện, các vị trí trong chuỗi có thể được tính song song dưới causal mask.

Khi sinh, token `t+1` chỉ được xác định sau khi token `t` đã được chọn. Phụ thuộc này tạo nút thắt độ trễ tuần tự.

KV cache tránh tính lại key/value của quá khứ nhưng không loại bỏ tính tuần tự ở cấp token. **Speculative decoding** dùng mô hình nhỏ đề xuất một nhóm token rồi để mô hình đích xác minh theo lô, nhờ đó có thể tăng tốc mà vẫn bảo toàn phân phối đích nếu thuật toán được triển khai đúng.

## Context Window

**Cửa sổ ngữ cảnh (context window)** giới hạn lượng token mô hình xử lý trong một yêu cầu hoặc đoạn huấn luyện.

Context dài hơn làm tăng bộ nhớ attention/KV cache, độ trễ và nhu cầu dữ liệu huấn luyện để mô hình học cách sử dụng vị trí xa.

Thông số “hỗ trợ 1 triệu token” chỉ nói về khả năng đưa lượng token đó vào hệ thống; nó không chứng minh mô hình suy luận hoặc truy xuất tốt đồng đều trên toàn bộ một triệu token.

## Transformer như tương tác trên tập hoặc đồ thị

Nếu bỏ thông tin vị trí, self-attention có tính hoán vị tương đương (permutation equivariance) và có thể được nhìn như truyền thông điệp trên đồ thị đầy đủ.

Khi thêm vị trí hoặc quan hệ, Transformer có thể áp dụng cho ảnh dưới dạng patch, âm thanh, protein, phân tử hoặc token đa phương thức. Kiến trúc chỉ yêu cầu các phần tử được biểu diễn thành token và có cách mã hóa cấu trúc quan hệ phù hợp.

## Vì sao Transformer mở rộng quy mô tốt?

Thành công của Transformer đến từ nhiều yếu tố cùng lúc: phép nhân ma trận phù hợp GPU/TPU, khả năng song song hóa theo vị trí khi huấn luyện, residual và normalization giúp chồng nhiều tầng, attention xử lý ngữ cảnh linh hoạt, cùng một họ kiến trúc áp dụng được cho nhiều modality và các mục tiêu tự giám sát cung cấp lượng dữ liệu rất lớn.

Vì vậy không nên giải thích sự thành công của Transformer bằng một yếu tố duy nhất; đó là kết quả đồng thiết kế giữa kiến trúc, dữ liệu, tối ưu hóa, phần cứng và hệ thống.

## Hạn chế

Transformer vẫn có những hạn chế quan trọng: attention bậc hai khi chuỗi dài, độ trễ sinh tự hồi quy, nhu cầu tính toán/bộ nhớ lớn, hành vi thống kê không có cơ chế xác minh sự thật tích hợp sẵn, context hữu hạn và biểu diễn phân tán khó giải thích.

Những giới hạn này thúc đẩy attention hiệu quả hơn, mô hình không gian trạng thái, RAG, công cụ bên ngoài và các tầng xác minh ở cấp hệ thống.

## Transformer so với RNN

| Thuộc tính | RNN/LSTM | Transformer |
|---|---|---|
| Song song hóa vị trí khi huấn luyện | thấp | cao |
| Đường truyền xa | qua nhiều bước hồi quy | kết nối attention trực tiếp |
| Trạng thái khi suy luận | trạng thái hồi quy gọn | KV cache tăng theo context |
| Chi phí ngữ cảnh dài cơ bản | tuyến tính theo từng bước | attention đầy đủ bậc hai |
| Khả năng streaming tự nhiên | cao | cần cache/chunking |

Không có mô hình nào vượt trội tuyệt đối trong mọi ràng buộc triển khai.

## Transformer so với CNN

CNN mã hóa cứng tính cục bộ và chia sẻ theo không gian. Transformer có thể học tương tác toàn cục linh hoạt hơn nhưng có thiên lệch quy nạp yếu hơn, nên thường hưởng lợi mạnh từ pretraining quy mô lớn.

Nhiều kiến trúc thị giác hiện đại kết hợp cả hai ý tưởng thay vì coi chúng loại trừ nhau.

## Mô hình tư duy

```text
Residual stream giữ biểu diễn token
Attention  → token trao đổi thông tin
MLP        → mỗi token biến đổi đặc trưng nội bộ
Norm       → ổn định thang giá trị
Residual   → bảo toàn và tích lũy thông tin/gradient
Lặp lại qua nhiều tầng
```

## Những hiểu lầm thường gặp

### “Transformer chính là Attention”

Không. Attention là thành phần cốt lõi nhưng MLP, residual, normalization, thông tin vị trí và mục tiêu huấn luyện đều cần thiết.

### “Attention cho mô hình thấy lịch sử vô hạn”

Không. Nó chỉ truy cập trong context/cache hiện có và vẫn bị giới hạn bởi tài nguyên tính toán.

### “Decoder-only không có encoder nên không hiểu đầu vào”

Không. Cùng chồng Transformer nhân quả biến đổi prompt thành các biểu diễn theo ngữ cảnh trước khi dự đoán phần tiếp theo.

### “Context càng dài thì câu trả lời luôn càng tốt”

Không. Context thừa hoặc nhiễu có thể làm chất lượng giảm; truy xuất và kỹ thuật xây dựng context vẫn rất quan trọng.

## Liên kết kiến thức

Transformer tổng hợp [Attention](./04_attention.md), [Residual và Backpropagation](../05_neural_networks/04_backpropagation.md), [RMSNorm](../05_neural_networks/06_initialization_and_normalization.md) và [Học biểu diễn](../05_neural_networks/08_representation_learning.md).

Các phần NLP và LLM tiếp theo sẽ xây tokenization, pretraining, scaling, instruction tuning và generation trên cơ chế này.