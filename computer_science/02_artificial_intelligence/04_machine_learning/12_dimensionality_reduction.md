# Giảm chiều: giữ cấu trúc quan trọng trong một không gian nhỏ hơn

**Giảm chiều (Dimensionality Reduction / 차원 축소)** tìm một biểu diễn có ít chiều hơn nhưng vẫn giữ lại phần cấu trúc quan trọng của dữ liệu. “Quan trọng” có thể nghĩa là giữ phương sai, khoảng cách cục bộ, vùng lân cận, khả năng phân tách hoặc thông tin phục vụ một nhiệm vụ downstream.

Không tồn tại một định nghĩa duy nhất về “biểu diễn tốt”. Mỗi phương pháp bảo tồn một thuộc tính khác nhau, vì vậy cần hiểu hàm mục tiêu của phương pháp thay vì chỉ nhìn một biểu đồ 2D đẹp.

## Vì sao dữ liệu nhiều chiều gây khó?

Dữ liệu nhiều chiều thường kéo theo:

- chi phí tính toán và bộ nhớ lớn;
- nhiều feature dư thừa hoặc nhiễu;
- hiện tượng khoảng cách tập trung;
- khó trực quan hóa;
- mật độ mẫu thấp trong không gian;
- nguy cơ overfitting cao khi dữ liệu hữu hạn.

Tuy nhiên số chiều cao không tự động là xấu. Nếu tín hiệu hữu ích thật sự phân bố trên nhiều chiều, ép dữ liệu xuống quá thấp có thể làm mất thông tin quan trọng.

## PCA nhìn từ phương sai

**Principal Component Analysis (PCA / 주성분 분석)** tìm các hướng trực giao giữ phương sai lớn nhất.

Sau khi center ma trận dữ liệu `X`, covariance là:

\[
\Sigma=\frac1nX^TX
\]

Các principal component là eigenvector của covariance matrix. Thành phần đầu tiên:

\[
v_1=\arg\max_{\|v\|=1}Var(Xv)
\]

Các component sau phải trực giao với component trước và tiếp tục tối đa hóa phần phương sai còn lại.

Chiếu xuống `k` chiều:

\[
Z=XW_k
\]

trong đó các cột của `W_k` là các eigenvector quan trọng nhất.

## PCA nhìn từ bài toán tái tạo

PCA cũng có thể được hiểu theo một cách khác: trong tất cả các không gian con tuyến tính `k` chiều, PCA chọn không gian làm lỗi tái tạo bình phương nhỏ nhất.

Nếu tái tạo:

\[
\hat X=ZW_k^T
\]

thì PCA chọn subspace làm:

\[
\|X-\hat X\|_F^2
\]

nhỏ nhất.

Tối đa hóa phương sai và tối thiểu hóa lỗi tái tạo là hai cách nhìn của cùng một bài toán.

## Liên hệ với SVD

Nếu ma trận đã center có phân rã:

\[
X=U\Sigma V^T
\]

thì các right singular vector trong `V` chính là các hướng principal.

Trong thực tế, SVD thường được dùng để tính PCA vì có tính chất số tốt.

Điểm này nối PCA trực tiếp với low-rank approximation và Đại số tuyến tính.

## Explained Variance

Tỷ lệ phương sai được giải thích:

\[
ratio_j=\frac{\lambda_j}{\sum_i\lambda_i}
\]

thường được dùng để chọn `k`.

Nếu cumulative explained variance đạt 95%, điều đó chỉ có nghĩa các component giữ khoảng 95% phương sai theo cấu trúc covariance tuyến tính. Nó **không** có nghĩa giữ 95% “ý nghĩa” hoặc 95% thông tin hữu ích cho mọi downstream task.

Một hướng có phương sai thấp vẫn có thể cực kỳ quan trọng cho classification nếu tín hiệu target nằm chủ yếu ở hướng đó.

## Chuẩn hóa trước PCA

PCA nhạy với scale vì bản thân variance phụ thuộc đơn vị đo.

Nếu một feature có variance rất lớn chỉ do đơn vị, nó có thể chi phối các component.

Standardization thường hữu ích, nhưng không nên áp dụng tự động trong mọi trường hợp. Quyết định cần dựa trên semantics của feature và điều ta muốn bảo tồn.

## t-SNE

**t-SNE** chủ yếu được dùng để trực quan hóa cấu trúc lân cận cục bộ.

Nó xây các phân phối xác suất biểu diễn similarity theo cặp trong không gian gốc và không gian thấp chiều, rồi tối ưu để giảm KL divergence giữa hai phân phối đó.

Cần nhớ:

- neighborhood cục bộ thường đáng tin hơn khoảng cách toàn cục;
- khoảng cách giữa hai cluster xa nhau trên plot không nhất thiết có ý nghĩa;
- kích thước và hình dạng cluster có thể bị bóp méo;
- kết quả phụ thuộc perplexity, initialization và random seed.

Không nên nhìn một biểu đồ t-SNE 2D rồi kết luận “dữ liệu thật sự có 7 cluster”.

## UMAP

**UMAP** sử dụng các ý tưởng từ manifold learning, topology và đồ thị nearest-neighbor để cố giữ cấu trúc cục bộ, thường scale tốt hơn và trong nhiều trường hợp bảo tồn một phần cấu trúc toàn cục tốt hơn t-SNE.

Tuy nhiên UMAP vẫn là một phép chiếu phi tuyến có hyperparameter như `n_neighbors`, `min_dist` và metric.

Biểu đồ đẹp không thay thế được validation định lượng.

## Autoencoder

Autoencoder học một phép nén phi tuyến:

\[
x\xrightarrow{Encoder}z\xrightarrow{Decoder}\hat x
\]

và được train để giảm reconstruction loss:

\[
L(x,\hat x)
\]

Biểu diễn ẩn `z` có số chiều nhỏ hơn và được học trực tiếp từ dữ liệu.

Khác với PCA, autoencoder có thể học mapping phi tuyến.

Tuy nhiên nếu mô hình có capacity quá lớn, latent representation không tự động trở nên dễ diễn giải, disentangled hoặc hữu ích cho downstream task.

Autoencoder là cầu nối trực tiếp sang Representation Learning và Variational Autoencoder.

## Giảm chiều có giám sát

PCA không sử dụng label. Nếu mục tiêu cuối là prediction, một representation có giám sát có thể giữ các hướng liên quan tới target tốt hơn.

**Linear Discriminant Analysis (LDA)** tìm phép chiếu làm tăng độ tách biệt giữa các lớp so với biến thiên bên trong lớp, dưới một số giả định thống kê.

Neural representation learning linh hoạt hơn: hidden representation được tối ưu đồng thời với downstream objective.

## Feature Selection khác với Dimensionality Reduction

**Feature selection** giữ lại một tập con của feature gốc.

**Dimensionality reduction** thường tạo ra feature mới là tổ hợp hoặc phép biến đổi của feature ban đầu.

Feature selection thường dễ diễn giải hơn; component hoặc latent dimension mới có thể gọn hơn nhưng khó gán ý nghĩa trực tiếp.

## Curse và Blessing of Dimensionality

Số chiều cao gây sparsity và làm các metric khoảng cách khó sử dụng, nhưng cũng có thể giúp dữ liệu trở nên dễ phân tách hơn nếu representation giàu và có cấu trúc tốt.

Deep Learning thường chủ động tạo representation nhiều chiều nơi task trở nên dễ hơn, rồi chỉ nén ở những vị trí cần thiết.

Vì vậy mục tiêu không phải “càng ít chiều càng tốt”, mà là:

> Biểu diễn có hình học phù hợp với task và chi phí tài nguyên chấp nhận được.

## Embedding và không gian ẩn

Embedding là một dạng biểu diễn vector cho đối tượng phức tạp hoặc rời rạc như từ, tài liệu, người dùng hay ảnh.

Một document có raw vocabulary lên tới hàng trăm nghìn chiều có thể được chuyển thành vector 768 chiều.

Đây vừa là compression vừa là quá trình tạo một hình học ngữ nghĩa được học.

Retrieval, clustering và classification sau đó hoạt động trên embedding space đó.

## Mô hình tư duy

```text
Quan sát nhiều chiều ban đầu
        ↓ xác định cấu trúc nào quan trọng
Projection / encoder học được
        ↓
Biểu diễn gọn hơn
        ↓
Visualization / retrieval / clustering / prediction / compression
```

## Các hiểu lầm thường gặp

### “PCA giữ nhiều information nhất”

Không chính xác. PCA giữ nhiều phương sai nhất trong lớp phép chiếu tuyến tính, không phải mọi thông tin quan trọng cho mọi task.

### “t-SNE hoặc UMAP cho thấy cluster thì cluster đó là thật”

Không. Phép chiếu có thể nhấn mạnh hoặc tạo cảm giác tách biệt. Cần kiểm tra lại trong representation phù hợp và bằng metric khác.

### “Giảm chiều luôn cải thiện mô hình”

Không. Nó có thể xóa mất tín hiệu hữu ích.

### “Embedding có ít chiều hơn dữ liệu thô nên chỉ là compression”

Không. Embedding còn thay đổi geometry của không gian để encode quan hệ phù hợp với objective huấn luyện.

## Liên kết kiến thức

Xem [Đại số tuyến tính cho AI](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Clustering](./11_clustering.md), và các phần sau về [Representation Learning](../05_neural_networks/08_representation_learning.md) và [Embedding](../08_large_language_models/02_embeddings_and_semantic_space.md).