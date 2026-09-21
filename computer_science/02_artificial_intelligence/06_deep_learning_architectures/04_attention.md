# Attention: truy cập thông tin theo mức độ liên quan

**Attention (어텐션 / 주의 메커니즘 / cơ chế chú ý)** giải quyết một hạn chế quan trọng của các mô hình chuỗi-sang-chuỗi thời kỳ đầu: bộ giải mã không nên bị buộc phải nén toàn bộ chuỗi nguồn vào một vector có kích thước cố định. Thay vào đó, tại mỗi bước tạo đầu ra, mô hình có thể tính **mức độ liên quan (relevance)** giữa truy vấn hiện tại và nhiều vị trí bộ nhớ, rồi tổng hợp phần thông tin phù hợp.

Self-attention hiện đại mở rộng ý tưởng này: mỗi token có thể truy cập những token khác dựa trên mối quan hệ phụ thuộc nội dung được mô hình học từ dữ liệu.

## Từ ngữ cảnh cố định tới ngữ cảnh động

Bộ mã hóa RNN tạo các trạng thái:

\[
h_1,h_2,...,h_T
\]

Thay vì chỉ đưa `h_T` cho decoder, attention xây vector ngữ cảnh tại bước `t`:

\[
c_t=\sum_i\alpha_{t,i}h_i
\]

Trọng số `α` phụ thuộc trạng thái decoder và trạng thái encoder:

\[
e_{t,i}=score(s_{t-1},h_i)
\]

\[
\alpha_{t,i}=softmax(e_{t,i})
\]

Nhờ đó decoder có thể quay lại tham chiếu động tới các vị trí nguồn khác nhau ở từng bước sinh.

## Query, Key và Value

Transformer chuẩn hóa cơ chế truy xuất này thành ba vai trò. Với ma trận biểu diễn `X`:

\[
Q=XW_Q,
\quad K=XW_K,
\quad V=XW_V
\]

Có thể dùng mô hình tư duy sau:

- **truy vấn (Query — Q / 쿼리)**: vị trí hiện tại đang tìm loại thông tin nào?
- **khóa (Key — K / 키)**: mỗi mục mô tả mức độ nó phù hợp với truy vấn ra sao?
- **giá trị (Value — V / 값)**: nếu mục được chọn, nội dung nào sẽ được truyền đi?

Đây chỉ là phép so sánh để hiểu cơ chế, không phải thao tác tra cứu key–value database theo nghĩa đen.

## Scaled Dot-Product Attention

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

Công thức này có thể được tách thành năm bước.

### 1. Tính điểm tương đồng

\[
S=QK^T
\]

Nếu độ dài chuỗi là `T`, trong self-attention ta có `S∈R^{T×T}`. Phần tử `S_{ij}` đo mức phù hợp giữa query của token `i` và key của token `j`.

Tích vô hướng thường tăng độ lớn khi số chiều tăng. Nếu các thành phần của Q/K có phương sai xấp xỉ `1`, phương sai của tích vô hướng tăng theo khoảng `d_k`.

### 2. Chia tỷ lệ

\[
\frac{S}{\sqrt{d_k}}
\]

Việc chia cho `√d_k` giúp giữ thang điểm ổn định hơn khi số chiều tăng. Nếu bỏ bước này, softmax dễ trở nên quá nhọn, rơi vào vùng bão hòa và làm gradient yếu đi.

### 3. Áp dụng mặt nạ

Trước softmax, những vị trí không được phép truy cập được gán giá trị `-∞` hoặc một số âm rất lớn trong tính toán số.

Mặt nạ nhân quả (causal mask):

```text
token i chỉ được attention tới token j nếu j ≤ i
```

Mặt nạ padding loại bỏ những token đệm không mang nội dung thật.

### 4. Chuẩn hóa bằng Softmax

\[
A=softmax(S_{masked})
\]

Mỗi hàng ứng với một query và trở thành tập trọng số dương có tổng bằng `1`.

### 5. Trộn các Value

\[
O=AV
\]

Biểu diễn đầu ra ở mỗi vị trí là tổ hợp có trọng số của các vector value.

## Trọng số attention không phải xác suất sự thật

Trọng số attention là các hệ số định tuyến thông tin được học cho mục tiêu của mô hình. Trọng số `0.8` không có nghĩa “token này có 80% xác suất là nguyên nhân” hoặc “nội dung này đúng với xác suất 80%”.

Việc dùng bản đồ attention như lời giải thích duy nhất có nhiều giới hạn vì value đã là biểu diễn được biến đổi, nhiều head và nhiều layer tương tác với nhau, đường residual có thể bỏ qua attention và nhiều phân bố attention khác nhau đôi khi tạo đầu ra gần giống nhau.

## Self-Attention

Trong **self-attention**, Q, K và V đều được tạo từ cùng một chuỗi biểu diễn `X`. Mỗi vị trí cập nhật biểu diễn của chính nó dựa trên những vị trí khác.

Ví dụ từ `bank` có thể nhận ngữ cảnh khác nhau:

```text
river bank → liên hệ mạnh với river / water
bank loan  → liên hệ mạnh với loan / money
```

Cùng một token ban đầu có thể trở thành biểu diễn theo ngữ cảnh (contextual representation) khác nhau.

## Cross-Attention

Trong **cross-attention**, query đến từ một chuỗi hoặc modality, còn key/value đến từ chuỗi hoặc modality khác:

\[
Q=H_{decoder}W_Q
\]

\[
K=H_{encoder}W_K,
V=H_{encoder}W_V
\]

Cơ chế này thường xuất hiện trong Transformer encoder–decoder và hệ thống đa phương thức.

## Multi-Head Attention

Thay vì chỉ có một attention duy nhất:

\[
head_i=Attention(QW_i^Q,KW_i^K,VW_i^V)
\]

Các head được ghép lại:

\[
MHA=Concat(head_1,...,head_h)W_O
\]

Mỗi head có thể học một không gian chiếu và mẫu tương tác khác nhau. Nếu tổng chiều mô hình là `d_model`, thiết kế phổ biến dùng:

\[
d_{head}=d_{model}/h
\]

Tuy nhiên nhiều mô hình hiện đại không nhất thiết dùng cùng số lượng query head và key/value head.

## Multi-Query Attention và Grouped-Query Attention

Trong suy luận tự hồi quy, bộ nhớ KV cache có thể rất lớn. **Multi-Query Attention (MQA)** chia sẻ một cặp key/value cho nhiều query head. **Grouped-Query Attention (GQA)** sử dụng số key/value head ít hơn số query head nhưng nhiều hơn một.

Mục tiêu là giảm kích thước KV cache và áp lực băng thông bộ nhớ trong khi giữ phần lớn chất lượng của multi-head attention. Nhiều LLM hiện đại sử dụng GQA vì sự đánh đổi này.

## Thông tin vị trí

Self-attention thuần túy dựa trên nội dung, nên bản thân nó không biết thứ tự token. Cần bổ sung thiên lệch hoặc mã hóa vị trí, chẳng hạn:

- mã hóa vị trí hình sin (sinusoidal position encoding);
- embedding vị trí học được;
- độ lệch vị trí tương đối (relative position bias);
- **Rotary Position Embedding (RoPE)**;
- **ALiBi**.

### Trực giác về RoPE

RoPE quay các cặp thành phần của vector Q/K theo góc phụ thuộc vị trí. Nhờ vậy tích vô hướng giữa Q và K mang thông tin về chênh lệch vị trí tương đối.

Nó không đơn giản là cộng một “số thứ tự vị trí” vào embedding, mà thay đổi hình học của phép tương tác giữa Q và K.

## Độ phức tạp của Attention

Self-attention cơ bản tạo ma trận điểm kích thước `T×T`:

\[
O(T^2d)
\]

Do đó chi phí của phần attention tăng bậc hai theo độ dài chuỗi `T`. Với ngữ cảnh dài, đây là nút thắt lớn về tính toán và bộ nhớ.

Các hướng tối ưu gồm:

- **FlashAttention**: tính attention chính xác bằng cách tổ chức truy cập bộ nhớ hiệu quả hơn;
- attention thưa hoặc cục bộ;
- cửa sổ trượt (sliding window);
- xấp xỉ low-rank hoặc kernel;
- mô hình hồi quy hoặc mô hình không gian trạng thái.

Cần phân biệt rõ: FlashAttention không phải phương pháp xấp xỉ attention; mục tiêu chính của nó là giảm truy cập bộ nhớ và tránh vật chất hóa các ma trận trung gian khổng lồ.

## Causal Attention

Trong mô hình ngôn ngữ decoder-only:

\[
A_{ij}=0\quad j>i
\]

Token hiện tại không được nhìn thấy token tương lai. Dù toàn bộ chuỗi huấn luyện có thể được xử lý song song, mặt nạ vẫn bảo toàn phân rã tự hồi quy.

Đây là một ưu thế quan trọng của Transformer so với RNN: song song hóa nhiều vị trí trong huấn luyện mà vẫn giữ ràng buộc nhân quả.

## KV Cache

Khi sinh tự hồi quy, các key/value của token cũ không cần tính lại ở mỗi bước. Chúng được lưu trong **KV cache**:

```text
bước t:
tính Q/K/V cho token mới
→ tái sử dụng K/V của token 1...t-1
→ attention trên K/V đã lưu
```

Bộ nhớ KV cache tăng theo số layer, độ dài chuỗi, số KV head, chiều mỗi head và kiểu dữ liệu. Khi context rất dài, suy luận có thể bị giới hạn bởi băng thông bộ nhớ hơn là số FLOP thuần túy.

## Attention sink và vấn đề ngữ cảnh dài

Context window lớn không đồng nghĩa mô hình khai thác đồng đều mọi token. Có thể xuất hiện suy giảm khi ngoại suy vị trí, phân tán attention, truy xuất thất bại hoặc hiện tượng **lost in the middle** — thông tin ở giữa context dài được sử dụng kém hơn.

Độ dài context là giới hạn dung lượng, không phải cam kết rằng mọi vị trí đều được nhớ và dùng tốt như nhau.

## Sparse Attention

Nếu mỗi query chỉ truy cập một tập con vị trí, chi phí có thể giảm đáng kể. Cửa sổ cục bộ phù hợp khi ngữ cảnh gần chiếm ưu thế; token toàn cục hoặc mẫu kết nối có cấu trúc giúp giữ các liên hệ xa.

Mẫu attention thưa chính là một dạng **thiên lệch quy nạp (inductive bias)**: nó tăng hiệu quả nhưng có thể vô tình chặn một liên hệ quan trọng.

## Attention như truy xuất khả vi

Có thể hình dung:

```text
vector truy vấn
→ so sánh với các key
→ chuẩn hóa thành trọng số
→ lấy tổ hợp có trọng số của các value
```

Cấu trúc này giống truy xuất, nhưng các vector bộ nhớ nằm bên trong quá trình tính toán của mạng và toàn bộ phép toán khả vi.

RAG về sau thực hiện **truy xuất bên ngoài (external retrieval)** từ kho tài liệu. Attention thực hiện **truy xuất khả vi bên trong (internal differentiable retrieval)** từ token hoặc hidden state.

## Vì sao Attention cải thiện Seq2Seq?

Đường truyền giữa hai token xa nhau trong self-attention có thể chỉ đi qua một tầng, thay vì qua nhiều bước hồi quy. Các vị trí chuỗi có thể được tính song song trong huấn luyện, đồng thời ngữ cảnh động loại bỏ nút thắt một-vector của Seq2Seq RNN thời kỳ đầu.

Đổi lại, attention đầy đủ phải trả chi phí tương tác cặp bậc hai theo độ dài chuỗi.

## Attention và truyền thông điệp trên đồ thị

Có thể xem self-attention như một đồ thị đầy đủ, trong đó mỗi token là một nút và các nút gửi thông tin cho nhau với trọng số cạnh được tính động từ độ tương thích Q/K.

Trực giác này liên hệ Transformer với Graph Neural Network, dù cách tham số hóa và cơ chế tính toán cụ thể khác nhau.

## Ổn định số

Softmax nên được tính bằng kỹ thuật trừ giá trị lớn nhất để tránh tràn số. Các kernel attention cũng phải xử lý cẩn thận mặt nạ `-inf`, kiểu số độ chính xác thấp và phép tích lũy.

FlashAttention tính softmax theo từng block với chuẩn hóa trực tuyến, nhờ đó không cần giữ toàn bộ ma trận điểm trong bộ nhớ và vẫn duy trì ổn định số.

## Mô hình tư duy

> Attention là cơ chế định tuyến phụ thuộc nội dung. Query đặt câu hỏi, các key cạnh tranh về mức phù hợp, value mang thông tin và softmax quyết định tỷ lệ thông tin được truyền.

Self-attention cho phép mỗi token viết lại biểu diễn của chính nó dựa trên những token khác mà mô hình đánh giá là liên quan.

## Những hiểu lầm thường gặp

### “Trọng số attention chính là độ quan trọng hay lời giải thích”

Không. Đó là hệ số định tuyến, không phải bảo đảm về quan hệ nhân quả hoặc giải thích đầy đủ.

### “Attention giải quyết hoàn toàn trí nhớ dài hạn”

Không. Nó cho phép truy cập trực tiếp trong context window nhưng vẫn chịu giới hạn về chi phí và khả năng sử dụng context.

### “Mỗi head có một vai trò được định nghĩa trước”

Không. Vai trò được học, có thể trùng lặp, phân tán và khác nhau giữa các tầng hoặc mô hình.

### “FlashAttention xấp xỉ Attention”

Không. Các phiên bản FlashAttention chuẩn tính cùng cơ chế attention chính xác nhưng tổ chức phép tính và truy cập bộ nhớ hiệu quả hơn.

### “RAG và Attention là một”

Không. Cả hai có trực giác truy xuất, nhưng attention định tuyến biểu diễn nội bộ còn RAG truy xuất tài liệu hoặc chunk từ nguồn ngoài.

## Liên kết kiến thức

Attention kết hợp [Đại số tuyến tính](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Softmax và xác suất](../01_mathematical_foundations/02_probability_for_ai.md), [Tính toán số](../01_mathematical_foundations/07_numerical_computation.md) và [Encoder–Decoder](./03_encoder_decoder_models.md).

Xem tiếp: [Transformer](./05_transformer.md), nơi attention được kết hợp với residual stream, chuẩn hóa và mạng feed-forward thành một kiến trúc có khả năng mở rộng lớn.