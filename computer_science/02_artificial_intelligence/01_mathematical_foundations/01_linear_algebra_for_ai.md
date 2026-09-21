# Đại số tuyến tính cho Trí tuệ nhân tạo

**Đại số tuyến tính (Linear Algebra / 선형대수)** là ngôn ngữ dùng để biểu diễn nhiều đại lượng cùng lúc và mô tả cách chúng được biến đổi. Trong AI hiện đại, một mẫu dữ liệu hiếm khi chỉ là một số. Một ảnh có hàng trăm nghìn điểm ảnh, một câu có thể trở thành hàng chục hoặc hàng nghìn token, một vector nhúng có hàng trăm đến hàng nghìn chiều, còn mạng nơ-ron có thể xử lý hàng nghìn mẫu song song trong một lô. Đại số tuyến tính giúp gom các đại lượng này thành vector, ma trận và tensor để phép tính được mô tả rõ ràng và chạy hiệu quả trên phần cứng.

Điểm quan trọng nhất không phải học thuộc phép nhân ma trận. Ta cần nhìn **ma trận như một phép biến đổi giữa các không gian**, vector như một **biểu diễn**, và tích vô hướng như phép đo **mức độ cùng hướng**. Khi mô hình tư duy này rõ, nhiều công thức trong học máy, embedding và Transformer trở nên tự nhiên hơn.

Xem bản đồ tổng quan: [Toán học cho AI](./00_mathematics_for_ai.md).

## Vô hướng, vector, ma trận và tensor

Một **vô hướng (scalar / 스칼라)** là một giá trị đơn, ví dụ nhiệt độ `23.5`, tốc độ học `0.001` hoặc hàm mất mát `2.3`.

Một **vector (벡터)** là danh sách số có thứ tự. Nếu khách hàng được biểu diễn bằng tuổi, thu nhập và số lần mua hàng, ta có thể viết:

\[
\mathbf{x}=\begin{bmatrix}31\\4200\\7\end{bmatrix}
\]

Vector này không phải chính khách hàng; nó là một biểu diễn được chọn để giữ những thuộc tính được xem là liên quan tới nhiệm vụ.

Một **ma trận (matrix / 행렬)** là bảng số hai chiều. Nếu mỗi hàng là một mẫu và mỗi cột là một đặc trưng:

\[
X=\begin{bmatrix}
31 & 4200 & 7\\
28 & 3500 & 3\\
45 & 6700 & 12
\end{bmatrix}
\]

thì `X` có kích thước `3 × 3`.

Một **tensor (텐서)** trong học sâu thường được hiểu thực dụng là mảng nhiều chiều. Ví dụ một lô ảnh RGB có thể có kích thước:

```text
số mẫu × chiều cao × chiều rộng × số kênh
32 × 224 × 224 × 3
```

PyTorch thường dùng quy ước `N × C × H × W`, trong khi một số framework hoặc định dạng khác dùng `N × H × W × C`. Kích thước tensor không phải chi tiết phụ; nhiều lỗi học máy đơn giản xuất phát từ việc giá trị đúng nhưng các trục bị đặt sai.

## Không gian vector: biểu diễn tồn tại ở đâu?

Một vector không chỉ là danh sách số. Khi viết:

\[
\mathbf{x}\in\mathbb{R}^d
\]

ta nói `x` là một điểm trong không gian vector `d` chiều.

Nếu mô hình embedding ánh xạ một câu thành vector 768 chiều, câu đó được biến thành một điểm trong `R^768`. Tuy nhiên, hình học của không gian này chỉ có ý nghĩa vì hàm mục tiêu huấn luyện đã tạo ra cấu trúc. Nếu không có quá trình học phù hợp, hai câu cùng nghĩa không tự nhiên biến thành hai vector gần nhau.

> **Hình học của không gian nhúng không phải “ý nghĩa có sẵn”; đó là cấu trúc được học từ dữ liệu và hàm mục tiêu.**

## Cộng vector và nhân với vô hướng

Hai phép toán cơ bản của không gian vector là cộng vector và nhân với vô hướng.

\[
\mathbf{a}+\mathbf{b}
\]

có thể được hiểu như kết hợp hai độ dịch chuyển hoặc hai tín hiệu theo từng thành phần.

\[
c\mathbf{x}
\]

làm thay đổi độ lớn của vector.

Trong mạng nơ-ron, **kết nối dư (residual connection)**:

\[
\mathbf{y}=F(\mathbf{x})+\mathbf{x}
\]

sử dụng phép cộng vector để giữ một đường truyền thông tin trực tiếp. Đây là ví dụ cho thấy một phép toán rất cơ bản của đại số tuyến tính trở thành thành phần kiến trúc quan trọng trong học sâu.

## Tích vô hướng: từ phép nhân tới mức độ cùng hướng

Với hai vector:

\[
\mathbf{a},\mathbf{b}\in\mathbb{R}^d
\]

**tích vô hướng (dot product)** là:

\[
\mathbf{a}^T\mathbf{b}=\sum_{i=1}^{d}a_i b_i
\]

Công thức này có hai cách hiểu quan trọng.

Thứ nhất, nó là một tổng có trọng số. Nếu `w` là vector trọng số và `x` là vector đặc trưng:

\[
z=\mathbf{w}^T\mathbf{x}
\]

mỗi đặc trưng được nhân với trọng số tương ứng rồi cộng lại. Hồi quy tuyến tính, hồi quy logistic và nơ-ron nhân tạo đều xây trên ý tưởng này.

Thứ hai, tích vô hướng liên hệ với góc giữa hai vector:

\[
\mathbf{a}^T\mathbf{b}=\|\mathbf{a}\|\|\mathbf{b}\|\cos\theta
\]

Khi hai vector cùng hướng, tích vô hướng lớn và dương. Khi gần vuông góc, nó gần 0. Khi ngược hướng, nó âm.

Attention trong Transformer sử dụng tích vô hướng giữa Query và Key để tạo điểm số. Truy xuất vector dày đặc (dense retrieval) cũng thường dùng tích vô hướng để xếp hạng embedding.

## Chuẩn vector: vector lớn tới mức nào?

**Chuẩn (norm / 노름)** đo độ lớn của vector.

Chuẩn L2:

\[
\|\mathbf{x}\|_2=\sqrt{\sum_i x_i^2}
\]

Chuẩn L1:

\[
\|\mathbf{x}\|_1=\sum_i |x_i|
\]

Chuẩn không chỉ dùng để đo khoảng cách. Điều chuẩn (regularization) thường phạt tham số có độ lớn quá cao:

\[
J(\theta)=L(\theta)+\lambda\|\theta\|_2^2
\]

Điều chuẩn L2 hạn chế trọng số quá lớn. Điều chuẩn L1 có xu hướng khiến nhiều hệ số bằng hoặc gần 0, liên quan tới **tính thưa (sparsity)**.

## Khoảng cách và độ tương đồng không giống nhau

Khoảng cách Euclid:

\[
d(\mathbf{a},\mathbf{b})=\|\mathbf{a}-\mathbf{b}\|_2
\]

đo khoảng cách tuyệt đối giữa hai vector.

Độ tương đồng cosine:

\[
\cos(\theta)=\frac{\mathbf{a}^T\mathbf{b}}{\|\mathbf{a}\|\|\mathbf{b}\|}
\]

bỏ qua phần lớn ảnh hưởng của độ lớn và tập trung vào hướng.

Hai embedding cùng hướng nhưng một vector dài gấp đôi vẫn có cosine similarity bằng 1, dù khoảng cách Euclid khác 0.

Trong tìm kiếm vector, thước đo phải phù hợp với cách mô hình embedding được huấn luyện. Không nên mặc định cosine luôn tốt hơn tích vô hướng hay khoảng cách Euclid.

## Ma trận là phép biến đổi tuyến tính

Phép nhân ma trận dễ bị hiểu như thao tác trên bảng số. Mô hình tư duy sâu hơn là:

\[
W:\mathbb{R}^{n}\rightarrow\mathbb{R}^{m}
\]

với:

\[
\mathbf{y}=W\mathbf{x}
\]

Ma trận `W` biến biểu diễn `n` chiều thành biểu diễn `m` chiều.

Nếu:

\[
W\in\mathbb{R}^{m\times n},\quad \mathbf{x}\in\mathbb{R}^{n}
\]

thì:

\[
\mathbf{y}\in\mathbb{R}^{m}
\]

**Suy luận theo kích thước (shape reasoning)** rất quan trọng trong học sâu. Nếu kích thước không khớp, phép nhân không được định nghĩa.

### Nhân ma trận là phép hợp thành

Nếu:

\[
\mathbf{h}=W_1\mathbf{x}
\]

và:

\[
\mathbf{y}=W_2\mathbf{h}
\]

thì:

\[
\mathbf{y}=W_2W_1\mathbf{x}
\]

Nhiều phép biến đổi tuyến tính liên tiếp có thể gộp thành một phép biến đổi tuyến tính duy nhất. Đây là lý do mạng nơ-ron cần **tính phi tuyến (nonlinearity)**. Nếu bỏ hàm kích hoạt, chồng 100 tầng tuyến tính về khả năng biểu diễn vẫn tương đương một tầng tuyến tính.

## Phép biến đổi affine và hệ số chệch

Trong học máy ta thường có:

\[
\mathbf{y}=W\mathbf{x}+\mathbf{b}
\]

Đây là **phép biến đổi affine**, không hoàn toàn tuyến tính theo định nghĩa toán học nghiêm ngặt vì có thành phần `b`.

Hệ số chệch cho phép đầu ra dịch khỏi gốc tọa độ. Nếu không có `b`, đầu vào bằng 0 luôn được ánh xạ về 0 trong một ánh xạ tuyến tính thuần túy.

Một tầng kết nối đầy đủ của mạng nơ-ron về cơ bản là phép biến đổi affine theo sau bởi hàm kích hoạt:

\[
\mathbf{h}=\phi(W\mathbf{x}+\mathbf{b})
\]

## Tính toán theo lô

Nếu có `B` mẫu và mỗi mẫu có `d` đặc trưng, ta gom chúng thành ma trận:

\[
X\in\mathbb{R}^{B\times d}
\]

Với ma trận trọng số:

\[
W\in\mathbb{R}^{d\times h}
\]

cả lô được biến đổi cùng lúc:

\[
H=XW
\]

thay vì lặp qua từng mẫu.

Đây là liên kết trực tiếp giữa đại số tuyến tính và GPU: các bộ tăng tốc hiện đại được tối ưu mạnh cho phép nhân ma trận lớn.

## Chuyển vị (transpose)

Chuyển vị đổi hàng thành cột:

\[
A^T_{ij}=A_{ji}
\]

Trong attention, nếu:

\[
Q,K\in\mathbb{R}^{n\times d_k}
\]

thì:

\[
QK^T\in\mathbb{R}^{n\times n}
\]

Ma trận kết quả chứa điểm tích vô hướng giữa từng token truy vấn và từng token khóa.

```text
Q       : n × d_k
K^T     : d_k × n
QK^T    : n × n
```

Chỉ cần nhìn kích thước đã thấy attention đang xây quan hệ giữa mọi cặp token trong chuỗi.

## Cơ sở và hệ tọa độ

Một vector được biểu diễn bằng tọa độ theo một **cơ sở (basis)**. Trong cơ sở chuẩn 2D:

\[
\mathbf{e}_1=(1,0),\quad \mathbf{e}_2=(0,1)
\]

và:

\[
\mathbf{x}=x_1\mathbf{e}_1+x_2\mathbf{e}_2
\]

Trong học máy, các chiều đặc trưng hoặc chiều tiềm ẩn cũng có thể xem như các trục tọa độ. Tuy nhiên, mỗi trục của không gian tiềm ẩn đã học thường không có nhãn ngữ nghĩa đơn giản như “tuổi” hay “thu nhập”. Một khái niệm có thể được phân tán trên nhiều chiều.

Điều này giải thích vì sao diễn giải một nơ-ron hoặc một chiều embedding riêng lẻ thường khó.

## Độc lập tuyến tính, hạng và thông tin dư thừa

Một tập vector **độc lập tuyến tính (linearly independent)** nếu không vector nào có thể được tạo bằng tổ hợp tuyến tính của các vector còn lại.

**Hạng (rank)** của ma trận phản ánh số hướng độc lập mà ma trận có thể giữ hoặc tạo ra.

Nếu phép chiếu có hạng thấp, thông tin bị nén vào một không gian con nhỏ hơn.

Cấu trúc hạng thấp xuất hiện ở nhiều nơi:

- PCA tìm không gian con chính;
- xấp xỉ hạng thấp dùng để nén ma trận;
- LoRA biểu diễn cập nhật tham số bằng tích của hai ma trận hạng thấp;
- phân rã ma trận được dùng trong hệ thống gợi ý.

LoRA sử dụng ý tưởng:

\[
\Delta W=BA
\]

với hạng `r` nhỏ hơn nhiều so với chiều gốc. Thay vì huấn luyện toàn bộ `W`, ta chỉ huấn luyện hai ma trận nhỏ `A` và `B`, nhờ đó giảm số tham số phải cập nhật.

## Vector riêng và trị riêng

Với ma trận vuông `A`, nếu:

\[
A\mathbf{v}=\lambda\mathbf{v}
\]

thì `v` là **vector riêng (eigenvector)** và `λ` là **trị riêng (eigenvalue)**.

Diễn giải hình học: `v` là hướng đặc biệt mà phép biến đổi `A` không đổi hướng, chỉ thay đổi độ lớn theo `λ`.

Phân rã trị riêng quan trọng trong phương pháp phổ, chuỗi Markov, phân tích đồ thị và trực giác về PCA.

Không phải mọi ma trận đều có phân rã trị riêng thuận tiện trên số thực, nên trong học máy thực tế ta thường dùng phân rã giá trị kỳ dị tổng quát hơn.

## Phân rã giá trị kỳ dị (SVD)

Mọi ma trận thực `A` đều có thể phân rã:

\[
A=U\Sigma V^T
\]

Trong đó `U` và `V` chứa các hướng trực chuẩn, còn các phần tử đường chéo của `Σ` là **giá trị kỳ dị (singular value)**.

Mô hình tư duy:

```text
tọa độ đầu vào
    ↓ V^T
đổi cơ sở / xoay không gian
    ↓ Σ
co giãn các hướng quan trọng
    ↓ U
đưa sang không gian đầu ra
```

Nếu chỉ giữ `k` giá trị kỳ dị lớn nhất, ta có xấp xỉ hạng thấp:

\[
A\approx U_k\Sigma_kV_k^T
\]

Điều này hữu ích cho nén, khử nhiễu và giảm chiều.

## PCA: tìm các hướng giải thích biến thiên

**Phân tích thành phần chính (Principal Component Analysis - PCA / 주성분 분석)** tìm các hướng trực giao có phương sai lớn nhất trong dữ liệu đã được căn giữa.

Nếu ma trận hiệp phương sai là:

\[
C=\frac{1}{n}X^TX
\]

thì các thành phần chính liên hệ với vector riêng của `C` hoặc vector kỳ dị phải của `X`.

PCA không “tìm đặc trưng quan trọng theo mọi nghĩa”. Nó tối ưu khả năng tái tạo phương sai dưới giả định tuyến tính. Hướng có phương sai lớn chưa chắc là hướng tốt nhất cho phân loại.

## Phép chiếu

Chiếu vector `x` lên vector đơn vị `u`:

\[
proj_{\mathbf{u}}(\mathbf{x})=(\mathbf{x}^T\mathbf{u})\mathbf{u}
\]

Phép chiếu giúp hiểu giảm chiều, bình phương tối thiểu và các phép tổ hợp có trọng số.

Trong bài toán bình phương tối thiểu, dự đoán có thể được nhìn như phép chiếu vector mục tiêu lên không gian cột của ma trận thiết kế.

## Bình phương tối thiểu và phương trình chuẩn

Hồi quy tuyến tính muốn giảm:

\[
\|X\mathbf{w}-\mathbf{y}\|_2^2
\]

Nếu các điều kiện phù hợp và ma trận khả nghịch, nghiệm có thể viết:

\[
\mathbf{w}=(X^TX)^{-1}X^T\mathbf{y}
\]

Trong thực tế, thường không nên tính nghịch đảo ma trận trực tiếp nếu có phương pháp số ổn định hơn như phân rã QR hoặc SVD. Đây là điểm nối sang [Tính toán số](./07_numerical_computation.md).

## Embedding: vector có “ý nghĩa” như thế nào?

**Phép nhúng (embedding / 임베딩)** biến đối tượng rời rạc như token, sản phẩm, người dùng hoặc tài liệu thành vector dày đặc.

Giả sử từ vựng có `V` token và chiều embedding là `d`, bảng embedding có kích thước:

\[
E\in\mathbb{R}^{V\times d}
\]

Mã token chọn một hàng của `E`.

Trong LLM, embedding ban đầu chưa phải “ý nghĩa cuối cùng”. Qua các tầng Transformer, trạng thái ẩn được ngữ cảnh hóa; cùng một token có thể có biểu diễn khác nhau tùy ngữ cảnh.

Hình học ngữ nghĩa hình thành vì hàm mục tiêu huấn luyện buộc mô hình tổ chức các biểu diễn theo cách hữu ích cho dự đoán hoặc phân biệt.

## Attention dưới góc nhìn đại số tuyến tính

Attention tích vô hướng có tỉ lệ:

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

Nếu trạng thái ẩn đầu vào:

\[
X\in\mathbb{R}^{n\times d_{model}}
\]

thì:

\[
Q=XW_Q,\quad K=XW_K,\quad V=XW_V
\]

Ba ma trận trọng số học ba phép chiếu khác nhau từ cùng trạng thái ẩn.

`QK^T` tạo ma trận `n × n` chứa độ tương hợp từng cặp. Softmax chuẩn hóa từng hàng thành trọng số. Nhân với `V` tạo tổ hợp có trọng số của các vector giá trị.

Nhìn từ đại số tuyến tính, attention không phải “mô hình nhìn vào từ quan trọng” theo nghĩa nhân hóa; nó là chuỗi phép biến đổi đã học, tích vô hướng từng cặp và phép tổng hợp có trọng số chuẩn hóa.

## Hình học nhiều chiều

Trong không gian nhiều chiều, trực giác 2D có thể gây sai. Một số hiện tượng quan trọng:

- số hướng có thể tăng rất nhanh;
- dữ liệu thường thưa trong không gian bao quanh;
- láng giềng gần nhất khó phân biệt nếu biểu diễn không tốt;
- chuẩn và khoảng cách từng cặp có thể trở nên tập trung;
- cần rất nhiều dữ liệu nếu muốn bao phủ trực tiếp không gian.

Học biểu diễn cố tìm không gian tiềm ẩn nơi cấu trúc liên quan đến nhiệm vụ cô đọng hơn.

Điều này liên hệ với **giả thuyết đa tạp (manifold hypothesis)**: quan sát nhiều chiều có thể nằm gần một đa tạp có cấu trúc với số chiều thấp hơn, dù đây không phải định lý đúng cho mọi tập dữ liệu.

## Broadcasting và ngữ nghĩa của kích thước tensor

Framework học sâu cho phép **broadcasting**: một tensor nhỏ được mở rộng theo quy tắc để thực hiện phép toán với tensor lớn hơn.

Ví dụ:

```text
H: B × d
b: d
H + b
```

`b` được cộng vào mỗi hàng.

Broadcasting rất tiện nhưng cũng dễ tạo lỗi âm thầm nếu các chiều vô tình khớp nhau. Khi gỡ lỗi mô hình, luôn kiểm tra kích thước và ý nghĩa của từng trục, không chỉ kiểm tra xem mã có chạy hay không.

## Mô hình tư duy (mental model)

```text
Vector        = biểu diễn / điểm / hướng
Ma trận       = phép biến đổi giữa các biểu diễn
Tích vô hướng = mức độ cùng hướng hoặc tổ hợp có trọng số
Chuẩn         = độ lớn
Khoảng cách / độ tương đồng = hình học của không gian biểu diễn
Hạng          = số hướng độc lập
SVD / PCA     = tìm cấu trúc và xấp xỉ ít chiều
Tensor        = đóng gói nhiều chiều để tính toán hàng loạt
```

## Các hiểu lầm thường gặp

### “Mỗi chiều embedding mang một ý nghĩa riêng”

Không nhất thiết. Biểu diễn đã học thường mang tính phân tán: một khái niệm có thể được mã hóa bởi tổ hợp của nhiều chiều.

### “Cosine similarity cao nghĩa là hai đối tượng chắc chắn cùng nghĩa”

Không. Độ tương đồng chỉ có ý nghĩa tương đối với mô hình embedding, mục tiêu huấn luyện và miền dữ liệu. Dữ liệu ngoài miền có thể khiến hình học trở nên kém đáng tin.

### “Nhân ma trận chỉ là công thức tính toán”

Cách hiểu sâu hơn là phép hợp thành các biến đổi giữa không gian vector. Đây là mô hình tư duy quan trọng để hiểu mạng nơ-ron và attention.

### “Số chiều càng nhiều càng tốt”

Số chiều lớn tăng khả năng biểu diễn nhưng cũng tăng bộ nhớ, chi phí tính toán và có thể làm việc học khó hơn. Chất lượng biểu diễn quan trọng hơn số chiều đơn thuần.

## Liên kết kiến thức

Đại số tuyến tính nối trực tiếp với mạng nơ-ron, thị giác máy tính, NLP, hệ thống gợi ý, học trên đồ thị và LLM. Khi học một kiến trúc mới, hãy hỏi bốn câu:

1. tensor đang biểu diễn gì;
2. mỗi trục có kích thước và ý nghĩa gì;
3. ma trận nào đang biến không gian nào sang không gian nào;
4. thước đo khoảng cách hoặc tích vô hướng đang mã hóa quan hệ gì.

Xem tiếp: [Xác suất cho AI](./02_probability_for_ai.md), [Giải tích cho AI](./04_calculus_for_ai.md), và phần Transformer trong `06_deep_learning_architectures/`.