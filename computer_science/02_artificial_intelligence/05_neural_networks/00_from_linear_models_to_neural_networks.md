# Từ mô hình tuyến tính tới Neural Network

**Neural Network (신경망 / mạng nơ-ron)** không xuất hiện vì Linear Regression hay Logistic Regression “sai”, mà vì nhiều quan hệ trong thế giới thực không thể được biểu diễn tốt bằng một ranh giới tuyến tính duy nhất trên raw feature. Ý tưởng cốt lõi của Neural Network là **hợp thành nhiều phép biến đổi và học các biểu diễn trung gian**, thay vì yêu cầu con người thiết kế thủ công toàn bộ feature phi tuyến.

Chương này tạo cầu nối từ Machine Learning cổ điển sang Deep Learning. Khi hiểu vì sao cần cả phép hợp thành hàm và tính phi tuyến, Neural Network sẽ không còn là một “hộp đen có nhiều layer”.

## Một layer tuyến tính thật sự làm gì?

Phép biến đổi affine:

\[
\mathbf z=W\mathbf x+\mathbf b
\]

biến vector đầu vào thành vector mới. Về mặt hình học, nó có thể kết hợp các phép xoay, co giãn, chiếu, shear rồi dịch chuyển.

Nếu xếp chồng hai layer tuyến tính mà không có hàm phi tuyến:

\[
\mathbf h=W_1\mathbf x+b_1
\]

\[
\mathbf y=W_2\mathbf h+b_2
\]

thì:

\[
\mathbf y=W_2W_1\mathbf x+(W_2b_1+b_2)
\]

vẫn chỉ tương đương **một phép biến đổi affine duy nhất**.

Do đó độ sâu (depth) chỉ tăng khả năng biểu diễn nếu giữa các layer có tính phi tuyến hoặc một cơ chế khác khiến chúng không thể rút gọn thành một linear map duy nhất.

## XOR: vì sao một ranh giới tuyến tính không đủ?

XOR có bảng chân trị:

```text
x1 x2 | y
0  0  | 0
0  1  | 1
1  0  | 1
1  1  | 0
```

Không có một đường thẳng trong 2D có thể tách hai điểm positive khỏi hai điểm negative.

Nhưng nếu học được một biểu diễn ẩn phù hợp, bài toán có thể trở nên phân tách tuyến tính trong không gian mới.

Đây là bản chất quan trọng của Neural Network:

> Không nhất thiết phải xây một ranh giới cực kỳ phức tạp ngay trong raw space; có thể học một phép biến đổi đưa dữ liệu sang representation space nơi bài toán trở nên đơn giản hơn.

## Feature thiết kế thủ công và feature học được

Machine Learning cổ điển thường có pipeline:

```text
dữ liệu thô
→ feature engineering theo domain
→ mô hình tuyến tính / tree
```

Ví dụ text classification từng phụ thuộc nhiều vào word count, TF-IDF và n-gram.

Deep Learning chuyển nhiều gánh nặng sang chính mô hình:

```text
dữ liệu gần thô
→ biểu diễn học được
→ biểu diễn sâu hơn
→ đầu ra của task
```

Mạng xử lý ảnh có thể học từ cạnh → texture → bộ phận → biểu diễn cấp vật thể. Transformer học contextual representation của token qua nhiều layer.

Điều này không có nghĩa feature engineering biến mất. Tokenization, normalization, data augmentation, architecture, positional encoding và cách xây context đều vẫn là những quyết định về representation.

## Hợp thành hàm

Một Neural Network có thể viết:

\[
f(x)=f_L(f_{L-1}(...f_2(f_1(x))))
\]

Mỗi layer thường có dạng:

\[
h^{(l)}=\phi(W^{(l)}h^{(l-1)}+b^{(l)})
\]

trong đó `φ` là **hàm kích hoạt (activation function)** tạo tính phi tuyến.

Độ sâu cho phép mô hình tái sử dụng feature trung gian. Thay vì học trực tiếp từ raw pixel tới class, mạng có thể xây một hierarchy của representation.

## Universal Approximation không có nghĩa “mạng học được mọi thứ dễ dàng”

Universal Approximation Theorem nói rằng dưới một số điều kiện, một mạng đủ rộng có thể xấp xỉ hàm liên tục trên miền compact với sai số nhỏ tùy ý.

Nhưng định lý **không** nói rằng:

- gradient descent chắc chắn tìm được tham số đó;
- chỉ cần ít dữ liệu;
- mô hình chắc chắn generalize;
- representation sẽ dễ hiểu;
- tài nguyên tính toán hữu hạn luôn đủ.

Khả năng biểu diễn (expressivity), khả năng huấn luyện (trainability) và khả năng khái quát hóa là ba vấn đề khác nhau.

## Độ rộng và độ sâu

Độ rộng (width) tăng số unit trong một layer; độ sâu (depth) tăng số phép biến đổi được hợp thành.

Một số hàm có thể được biểu diễn gọn bằng mạng sâu nhưng cần số unit rất lớn nếu mạng nông. Depth đặc biệt hiệu quả khi bài toán có cấu trúc hợp thành hoặc phân cấp.

Tuy nhiên sâu hơn không tự động tốt hơn. Optimization, latency, memory và độ ổn định training đều là giới hạn thực tế.

## Tham số và kiến trúc

Tham số gồm trọng số và bias được học từ dữ liệu.

**Kiến trúc (architecture)** xác định computation graph: số layer, hidden dimension, kết nối, activation, normalization, attention, convolution và các cơ chế khác.

Architecture chính là một inductive bias mạnh.

CNN mã hóa locality và weight sharing. RNN mã hóa recurrence. Transformer mã hóa tương tác phụ thuộc nội dung thông qua attention.

## Neural Network như một chương trình khả vi

Một mô hình tư duy hữu ích là:

> Neural Network là một chương trình có tham số và có thể vi phân (parameterized differentiable program).

Forward pass chạy chương trình để tạo prediction. Loss đo chất lượng prediction. Backpropagation dùng chain rule để tính mức nhạy của loss theo từng tham số. Optimizer sau đó cập nhật tham số.

```text
Đầu vào
 ↓
Computation graph khả vi fθ
 ↓
Dự đoán
 ↓
Loss
 ↓ lan truyền ngược
Gradient
 ↓ optimizer
Tham số θ mới
```

Đây là vòng huấn luyện cốt lõi của Deep Learning.

## Neural Network không phải mô phỏng chính xác não sinh học

Các tên như neuron hay synapse bắt nguồn từ cảm hứng lịch sử, nhưng Neural Network hiện đại không phải mô phỏng sinh học chính xác của não.

Một artificial neuron thường chỉ thực hiện tổng có trọng số rồi qua activation. Transformer còn xa hơn nhiều so với neuron sinh học trực tiếp.

Ẩn dụ sinh học hữu ích ở mức trực giác và lịch sử, nhưng không nên dùng để suy luận hành vi kỹ thuật của mô hình.

## Biểu diễn phân tán

Trong hệ symbolic, một concept có thể ánh xạ tới một ký hiệu rõ ràng. Neural Network thường dùng **biểu diễn phân tán (distributed representation)**: thông tin được mã hóa trong pattern của nhiều dimension hoặc unit cùng lúc.

Một neuron riêng lẻ hiếm khi tương ứng đơn giản với đúng một khái niệm ngữ nghĩa. Ý nghĩa thường nằm trong subspace, direction hoặc activation pattern của nhiều unit.

Cách biểu diễn này hỗ trợ khả năng kết hợp và generalization nhưng làm interpretability khó hơn.

## End-to-End Learning

**Học đầu-cuối (end-to-end learning)** tối ưu một objective xuyên qua nhiều stage cùng lúc.

Ví dụ speech recognition truyền thống từng có pipeline gồm acoustic feature → phoneme model → language model → decoder. Một hệ end-to-end có thể học trực tiếp mapping từ audio tới text với nhiều thành phần được tối ưu chung.

Lợi ích là representation trung gian tự thích nghi với task.

Đổi lại, hệ thống khó modular hóa và debug hơn, thường cần nhiều data/compute hơn và khó xác định chính xác failure xuất phát từ stage nào.

Production system vì vậy vẫn thường dùng kiến trúc lai thay vì biến mọi thứ thành một mạng end-to-end duy nhất.

## Neural Network và đầu ra xác suất

Neural Network thường tạo logit hoặc tham số của một phân phối, không phải “độ chắc chắn tuyệt đối”.

Classification:

\[
p(y\mid x)=softmax(W_{out}h+b)
\]

Trong regression, mạng có thể tạo mean và variance của Gaussian.

Generative model tham số hóa các phân phối phức tạp hơn.

Các nguyên lý về probability và calibration từ Machine Learning vẫn áp dụng đầy đủ.

## Scale: dữ liệu, compute và tham số

Thành công của Deep Learning đến từ sự kết hợp của nhiều yếu tố: dataset lớn, GPU/accelerator phù hợp với matrix computation, initialization và activation tốt hơn, normalization, optimizer tốt hơn, kiến trúc phù hợp từng modality và distributed systems.

Không có một “đột phá Neural Network duy nhất” giải thích toàn bộ sự phát triển này.

## Mô hình tư duy

```text
Mô hình tuyến tính:
raw representation → quyết định đơn giản

Neural Network:
raw representation
→ phép biến đổi học được
→ phép biến đổi học được
→ ...
→ representation nơi task trở nên dễ hơn
→ output head tương đối đơn giản
```

## Các hiểu lầm thường gặp

### “Neural Network chỉ là rất nhiều Logistic Regression”

Không đủ. Mỗi unit có thành phần tuyến tính và phi tuyến, nhưng chính phép hợp thành qua nhiều layer tạo ra hierarchical representation mà một Logistic Regression đơn lẻ không có.

### “Universal approximation nghĩa Neural Network giải được mọi bài toán”

Không. Khả năng biểu diễn không bảo đảm khả năng học, đủ dữ liệu, robustness hay correctness.

### “Deep Learning không cần feature engineering”

Không. Nó giảm nhu cầu thiết kế feature thủ công, nhưng data engineering, representation design và architecture engineering vẫn cực kỳ quan trọng.

### “Càng nhiều layer càng thông minh”

Không. Depth chỉ hữu ích khi architecture, training và data hỗ trợ. Mạng quá sâu có thể khó tối ưu và lãng phí compute.

## Liên kết kiến thức

Chương này nối [Linear Regression](../04_machine_learning/05_linear_regression.md), [Logistic Regression](../04_machine_learning/06_logistic_regression.md), [Giải tích](../01_mathematical_foundations/04_calculus_for_ai.md) và [Tối ưu hóa](../01_mathematical_foundations/06_optimization.md).

Xem tiếp: [Neuron, Perceptron và MLP](./01_neuron_perceptron_and_mlp.md).