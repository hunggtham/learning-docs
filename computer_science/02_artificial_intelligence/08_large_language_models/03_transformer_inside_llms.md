# Transformer bên trong mô hình ngôn ngữ lớn

Ở layer trước, Transformer đã được giải thích như một kiến trúc gồm attention, mạng truyền thẳng (feed-forward network), kết nối tắt (residual connection) và chuẩn hóa (normalization). Khi kiến trúc đó được mở rộng thành **mô hình ngôn ngữ lớn (Large Language Model — LLM)**, cơ chế nền không thay đổi, nhưng tỷ lệ giữa các thành phần, cách tổ chức attention, mã hóa vị trí, normalization, khối MLP, cache và song song hóa trở thành các quyết định ảnh hưởng trực tiếp tới chất lượng, tốc độ và chi phí.

Chapter này không lặp lại công thức attention từ đầu. Mục tiêu là nhìn Transformer như một **động cơ tính toán của LLM**: một token đi qua mô hình như thế nào, tham số nằm ở đâu, context được trộn ra sao và vì sao suy luận khác huấn luyện về mặt hệ thống.

Xem nền: [Transformer](../06_deep_learning_architectures/05_transformer.md) và [Attention](../06_deep_learning_architectures/04_attention.md).

## Ngăn xếp decoder-only

Một LLM chỉ-bộ-giải-mã (decoder-only) thường có luồng:

```text
Token ID
   ↓ tra cứu embedding
Vector token + cơ chế vị trí
   ↓
Transformer block 1
   ↓
Transformer block 2
   ↓
...
   ↓
Transformer block L
   ↓ normalization cuối
Trạng thái ẩn tại mỗi vị trí
   ↓ chiếu đầu ra / unembedding
Logit của vocabulary
   ↓ softmax / sampling
Token tiếp theo
```

Mỗi block thường có hai phần tính toán lớn:

```text
Attention sublayer
Feed-Forward / MLP sublayer
```

và đường residual chạy xuyên suốt.

## Residual stream như biểu diễn làm việc dùng chung

Với kiến trúc **pre-norm**:

\[
x' = x + Attention(Norm(x))
\]

\[
x'' = x' + MLP(Norm(x'))
\]

Một cách nghĩ hữu ích là **residual stream** chứa biểu diễn hiện tại của mỗi token. Attention đọc biểu diễn ở nhiều vị trí rồi ghi một phần cập nhật; MLP đọc từng vị trí và ghi một biến đổi đặc trưng khác.

Đây chỉ là mô hình tư duy, không có nghĩa mô hình sở hữu các “thanh ghi” symbolic rõ ràng. Thông tin ẩn được phân tán qua nhiều chiều, layer và vị trí token.

## Attention trộn thông tin giữa các vị trí

Với trạng thái ẩn `X`, mỗi layer tạo:

\[
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V
\]

**Causal mask** đảm bảo token tại vị trí `t` chỉ dùng các vị trí `≤t`.

Đầu ra attention:

\[
O=softmax\left(\frac{QK^T}{\sqrt{d_h}}+M\right)V
\]

Ở quy mô LLM, điều quan trọng không chỉ là công thức. Attention là nơi độ dài context tạo chi phí theo chiều chuỗi và cũng là nơi xuất hiện **KV cache** trong quá trình sinh.

## MHA, MQA và GQA

Multi-Head Attention cổ điển dùng số head cho Query, Key và Value giống nhau. Trong serving tự hồi quy, Key và Value của mọi token trước phải được giữ trong KV cache.

Nếu mô hình có:

```text
L layer
T token đã cache
Hkv KV head
Dh kích thước mỗi head
2 tensor: K và V
```

kích thước cache tỷ lệ gần đúng với:

\[
2LT H_{kv}D_h\times bytes\_per\_element
\]

Do đó nhiều LLM hiện đại sử dụng:

- **MHA (Multi-Head Attention)**: số Q head bằng số K/V head;
- **MQA (Multi-Query Attention)**: nhiều Q head chia sẻ một K và V head;
- **GQA (Grouped-Query Attention)**: nhiều Q head nhưng chỉ có một số nhóm K/V head.

GQA là một điểm cân bằng phổ biến: giảm bộ nhớ và băng thông KV trong khi giữ chất lượng gần với MHA.

## Feed-Forward Network chứa rất nhiều tham số

FFN cổ điển:

\[
FFN(x)=W_2\phi(W_1x)
\]

Nếu chiều ẩn là `d` và chiều trung gian `d_ff≈4d`, chỉ hai ma trận đã chứa khoảng:

\[
2d\cdot d_{ff}\approx8d^2
\]

tham số mỗi layer.

LLM hiện đại thường dùng MLP có cổng, ví dụ **SwiGLU**:

\[
FFN(x)=W_3\left(SiLU(W_1x)\odot W_2x\right)
\]

Ba phép chiếu tạo tương tác nhân. Chiều trung gian thường được điều chỉnh để giữ ngân sách tham số và FLOP hợp lý.

Attention được nhắc tới nhiều vì trực quan, nhưng FFN/MLP thường chứa tỷ lệ lớn tham số và phép tính của dense LLM.

## MLP đang làm gì?

Attention chủ yếu định tuyến và trộn thông tin giữa các vị trí token. MLP biến đổi biểu diễn tại từng vị trí độc lập về mặt vị trí nhưng dùng chung trọng số.

Một số hướng nghiên cứu diễn giải MLP như dạng bộ nhớ kết hợp (associative memory) cho các feature hoặc fact đã học. Tuy nhiên không nên hiểu theo nghĩa đen rằng mỗi neuron hoặc mỗi hàng ma trận tương ứng một fact; tri thức được phân tán và tương tác qua nhiều layer.

## RMSNorm và Pre-Norm

Nhiều decoder LLM dùng **RMSNorm**:

\[
RMS(x)=\sqrt{\frac1d\sum_i x_i^2+\epsilon}
\]

\[
RMSNorm(x)=g\odot\frac{x}{RMS(x)}
\]

RMSNorm bỏ bước trừ trung bình của LayerNorm và đơn giản hóa phép tính.

Pre-norm đặt normalization trước sublayer, giúp gradient đi qua đường residual identity ổn định hơn trong stack sâu.

## Rotary Position Embedding (RoPE)

Attention tự nó không biết thứ tự token. **RoPE** mã hóa vị trí bằng phép quay trên các thành phần Q/K.

Dạng đơn giản cho một cặp chiều:

\[
\begin{bmatrix}
x'_{2i}\\x'_{2i+1}
\end{bmatrix}
=
\begin{bmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix}
x_{2i}\\x_{2i+1}
\end{bmatrix}
\]

Góc quay phụ thuộc vị trí và tần số.

Lợi ích quan trọng là tích vô hướng sau phép quay có thể mang thông tin về chênh lệch vị trí tương đối.

Các kỹ thuật kéo dài context có thể rescale hoặc nội suy tần số RoPE, nhưng chỉ tăng cấu hình context không đảm bảo chất lượng nếu mô hình chưa được huấn luyện hoặc thích ứng tương ứng.

## Chiếu đầu ra và weight tying

Trạng thái ẩn cuối `h_t` được ánh xạ thành logit vocabulary:

\[
z_t=W_Uh_t+b
\]

với:

\[
W_U\in R^{|V|\times d}
\]

Sau đó:

\[
P(token=k\mid context)=softmax(z_t)_k
\]

Một số mô hình dùng chung ma trận embedding đầu vào và ma trận đầu ra (**weight tying**), tùy convention có thể viết `W_U=E` hoặc dùng chuyển vị.

Weight tying giảm tham số và chia sẻ hình học lexical, nhưng không phải yêu cầu bắt buộc.

## Prefill và Decode là hai workload khác nhau

### Prefill

Mô hình nhận prompt dài `T` và tính biểu diễn cho toàn bộ vị trí. Các phép nhân ma trận lớn có mức song song hóa cao; workload thường thiên về năng lực tính toán.

### Decode

Sau đó mỗi bước chỉ thêm một token. K/V cũ đã được cache; mô hình tính Query và K/V mới rồi attention lên toàn bộ cache.

Decode thường nhạy với băng thông bộ nhớ và độ trễ vì mỗi token phải đọc lượng lớn trọng số + KV cache trong khi lượng công việc mỗi bước nhỏ hơn prefill.

Vì vậy tối ưu inference phải tách:

```text
thông lượng prefill
và
độ trễ decode / token mỗi giây
```

## KV cache không phải bộ nhớ dài hạn của mô hình

KV cache là trạng thái attention trung gian được lưu cho context hoặc request hiện tại. Nó không cập nhật trọng số và không phải cơ sở dữ liệu bộ nhớ ngữ nghĩa.

Nếu ứng dụng cần “nhớ” lâu dài, trạng thái phải được lưu bên ngoài rồi đưa lại qua context hoặc retrieval.

## Độ dài context và chi phí attention

Khi huấn luyện full attention, ma trận điểm có kích thước gần `T×T`. Với attention chuẩn, compute và memory tăng bậc hai theo chiều dài chuỗi.

Trong inference, KV cache tránh tính lại trạng thái cũ, nhưng attention cho mỗi token mới vẫn tăng gần tuyến tính theo số token đã cache, còn bộ nhớ cache cũng tăng tuyến tính.

Vì vậy context window lớn luôn có chi phí hệ thống thật, dù API cho phép gửi lượng context rất lớn.

## FlashAttention

Cài đặt attention ngây thơ có thể materialize ma trận attention lớn trong bộ nhớ băng thông cao. **FlashAttention** tổ chức lại phép tính theo block để giảm I/O bộ nhớ và giảm intermediate phải lưu, trong khi vẫn tính attention tương đương về mặt toán học trong giới hạn số học dấu phẩy động.

Bài học chính:

> Độ phức tạp thuật toán chưa đủ để dự đoán tốc độ; phân cấp bộ nhớ và thiết kế kernel có thể quyết định hiệu năng thực tế.

Đây là cầu nối trực tiếp giữa toán AI và kỹ thuật GPU.

## Mixture of Experts

Không phải mọi LLM đều dense. **Mixture of Experts (MoE)** có nhiều expert FFN và router gửi mỗi token tới một tập con expert:

\[
y=\sum_{e\in TopK(router(x))}p_e(x)Expert_e(x)
\]

Tổng tham số có thể rất lớn nhưng chỉ vài expert hoạt động cho mỗi token, nhờ đó active compute thấp hơn dense model có cùng tổng tham số.

Các khó khăn chính gồm:

- cân bằng tải;
- bất ổn routing;
- giao tiếp khi expert parallel;
- footprint bộ nhớ;
- serving phức tạp hơn.

## Tổng tham số và tham số hoạt động

Trong dense model, gần như toàn bộ tham số của layer tham gia xử lý mỗi token.

Trong MoE, tổng tham số khác số tham số hoạt động trên mỗi token. Do đó so sánh mô hình chỉ bằng “bao nhiêu tỷ tham số” có thể gây hiểu nhầm.

Nên hỏi thêm:

```text
tổng tham số?
tham số hoạt động / token?
số token huấn luyện?
kiến trúc?
context?
precision?
```

## Lượng tử hóa và kiến trúc

Inference có thể lưu trọng số ở INT8 hoặc INT4 rồi giải lượng tử (dequantize) sang precision phù hợp khi tính toán. Một số layer hoặc outlier activation nhạy hơn với sai số lượng tử.

Kiến trúc ảnh hưởng độ nhạy: normalization, activation outlier, dtype của KV cache và expert routing đều có thể quan trọng.

Lượng tử hóa không biến Transformer thành một kiến trúc khác; nó xấp xỉ việc thực thi số để tiết kiệm bộ nhớ và băng thông.

## Transformer block như một chương trình học được lặp lại

Dù cấu trúc block lặp lại, trọng số thường khác nhau giữa các layer. Có thể nhìn mỗi layer như việc tinh chỉnh biểu diễn qua hai bước lớn:

```text
lấy và trộn context phù hợp bằng attention
→ biến đổi feature bằng MLP
→ cộng dồn vào residual stream
```

Sau nhiều layer, biểu diễn cuối đã trải qua nhiều vòng tính toán theo ngữ cảnh. Vì vậy một token đầu ra có thể được tạo sau lượng tính toán nội bộ đáng kể.

## Những hiểu lầm thường gặp

### “Phần lớn tham số LLM nằm trong attention”

Trong dense block, các phép chiếu MLP/FFN thường chiếm tỷ lệ tham số rất lớn.

### “Context window càng lớn thì khả năng nhớ tăng tương ứng”

Context window chỉ là dung lượng đầu vào có thể địa chỉ hóa; khả năng sử dụng thông tin xa có thể suy giảm do khoảng cách và nhiễu.

### “KV cache là bộ nhớ bền vững của LLM”

Nó là cache attention theo request/context, không phải tri thức đã học hay bộ nhớ ứng dụng dài hạn.

### “Quantization tạo ra một kiến trúc mô hình mới”

Thông thường kiến trúc không đổi; phép tính được xấp xỉ ở precision thấp hơn.

### “MoE 1 nghìn tỷ tham số tốn compute như dense model 1 nghìn tỷ tham số”

Chỉ một tập con expert hoạt động trên mỗi token, dù chi phí memory và communication vẫn có thể rất lớn.

## Mô hình tư duy

```text
Residual stream = trạng thái token đang tiến hóa
Attention       = định tuyến và trộn context
MLP / Experts   = biến đổi feature phi tuyến
Norm            = ổn định thang đo
Position        = mã hóa thứ tự / khoảng cách tương đối
Output head     = biến trạng thái cuối thành logit token tiếp theo
KV cache        = tái sử dụng trạng thái attention của context khi decode
```

## Liên kết kiến thức

Chapter này nối [Transformer](../06_deep_learning_architectures/05_transformer.md), [Attention](../06_deep_learning_architectures/04_attention.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md) và [AI Compute & Infrastructure](../17_ai_compute_and_infrastructure/).

Xem tiếp: [Pretraining](./04_pretraining.md).