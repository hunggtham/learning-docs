# Variational Autoencoder: không gian latent như một mô hình xác suất

**Variational Autoencoder (VAE / 변분 오토인코더 / bộ tự mã hóa biến phân)** mở rộng autoencoder từ cơ chế nén xác định thành một **mô hình sinh có biến tiềm ẩn (latent-variable generative model)**. Encoder không chỉ tạo một vector latent duy nhất mà xấp xỉ phân bố của biến tiềm ẩn `z` khi biết đầu vào `x`. Decoder định nghĩa khả năng sinh dữ liệu khi biết latent.

Mục tiêu là vừa tái tạo dữ liệu tốt, vừa buộc phân bố latent có cấu trúc gần một prior đơn giản để có thể lấy mẫu và sinh dữ liệu mới.

## Mô hình sinh

Giả sử prior của latent là:

\[
p(z)=\mathcal N(0,I)
\]

Decoder định nghĩa:

\[
p_\theta(x\mid z)
\]

Phân bố chung:

\[
p_\theta(x,z)=p(z)p_\theta(x\mid z)
\]

Xác suất biên của dữ liệu:

\[
p_\theta(x)=\int p(z)p_\theta(x\mid z)dz
\]

Tích phân này thường không thể tính chính xác khi decoder là mạng nơ-ron phức tạp.

## Bài toán suy luận

Posterior thật:

\[
p_\theta(z\mid x)=\frac{p(z)p_\theta(x\mid z)}{p_\theta(x)}
\]

khó tính vì mẫu số chứa tích phân phức tạp.

VAE đưa vào một phân bố encoder:

\[
q_\phi(z\mid x)
\]

để xấp xỉ posterior. Đây là **suy luận biến phân (variational inference)**.

## Evidence Lower Bound — ELBO

Ta tối ưu một cận dưới của log-likelihood:

\[
\log p_\theta(x)
\ge
\mathbb E_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)]
-D_{KL}(q_\phi(z\mid x)\|p(z))
\]

ELBO gồm hai thành phần chính.

### Thành phần tái tạo / likelihood

\[
\mathbb E_q[\log p_\theta(x\mid z)]
\]

khuyến khích latent giữ đủ thông tin để decoder giải thích và tái tạo đầu vào.

### Điều chuẩn KL

\[
D_{KL}(q_\phi(z\mid x)\|p(z))
\]

khuyến khích posterior xấp xỉ không đi quá xa prior.

Hàm mất mát thường được viết dưới dạng:

\[
L_{VAE}=L_{recon}+D_{KL}(q(z\mid x)\|p(z))
\]

với khác biệt về dấu hoặc hệ số tùy quy ước triển khai.

## Vì sao phải kéo latent về gần prior?

Autoencoder thông thường có thể ánh xạ từng ví dụ vào những vùng rời rạc tùy ý. Khi lấy ngẫu nhiên một điểm Gaussian, điểm đó có thể nằm ở vùng decoder chưa bao giờ được huấn luyện.

VAE buộc các posterior latent cùng tương thích hơn với một prior chung, nhờ vậy việc lấy mẫu:

\[
z\sim\mathcal N(0,I)
\]

rồi giải mã có ý nghĩa hơn.

Đổi lại, nếu áp lực KL quá mạnh, mô hình có thể hy sinh chi tiết tái tạo.

## Encoder Gaussian

Encoder thường tạo:

\[
\mu_\phi(x),\qquad \log\sigma_\phi^2(x)
\]

và định nghĩa:

\[
q_\phi(z\mid x)=\mathcal N(\mu,diag(\sigma^2))
\]

Mô hình thường dự đoán log-variance thay vì variance trực tiếp vì log-variance không bị ràng buộc phải dương và thuận tiện hơn về ổn định số; khi cần có thể lấy hàm mũ để thu được variance.

## Reparameterization Trick

Nếu lấy mẫu trực tiếp:

\[
z\sim\mathcal N(\mu,\sigma^2)
\]

nút ngẫu nhiên phụ thuộc vào tham số làm việc truyền gradient theo đường lấy mẫu trở nên khó xử lý.

Ta viết lại:

\[
\epsilon\sim\mathcal N(0,I)
\]

\[
z=\mu+\sigma\odot\epsilon
\]

Khi đó phần ngẫu nhiên nằm ở `ε`, còn `z` vẫn là hàm khả vi của `μ` và `σ`. Kỹ thuật này gọi là **mẹo tái tham số hóa (reparameterization trick)**.

## KL dạng đóng cho Gaussian

Với Gaussian đường chéo so với chuẩn tắc:

\[
D_{KL}(q\|p)=\frac12\sum_j
(\mu_j^2+\sigma_j^2-\log\sigma_j^2-1)
\]

Do đó thành phần KL của VAE chuẩn có thể tính trực tiếp mà không cần Monte Carlo.

## Likelihood của Decoder quyết định hàm tái tạo

Nếu:

\[
p(x\mid z)=\mathcal N(\mu_\theta(z),\sigma^2I)
\]

negative log-likelihood tương ứng gần với MSE dưới các giả định nhất định.

Nếu đầu ra được mô hình hóa Bernoulli, BCE là dạng thích hợp hơn.

Vì vậy việc chọn hàm mất mát tái tạo thực chất là chọn giả định về mô hình quan sát.

## β-VAE

Có thể điều chỉnh:

\[
L=L_{recon}+\beta D_{KL}
\]

`β>1` tăng áp lực đưa latent về prior và đôi khi tạo biểu diễn có các yếu tố tách biệt hơn, nhưng thường đổi lại bằng chất lượng tái tạo thấp hơn.

Tính **disentanglement** không được đảm bảo chỉ nhờ tăng `β`; khả năng định danh các yếu tố latent còn phụ thuộc giả định dữ liệu và mô hình.

## Posterior Collapse

Nếu decoder quá mạnh, nó có thể gần như bỏ qua latent:

\[
q(z\mid x)\approx p(z)
\]

KL khi đó gần `0` và `z` mang rất ít thông tin về `x`.

Hiện tượng này thường được gọi là **posterior collapse**, đặc biệt dễ xảy ra ở VAE văn bản có decoder tự hồi quy mạnh.

Các biện pháp giảm gồm KL annealing, free bits, decoder yếu hơn hoặc thay đổi kiến trúc và hàm mục tiêu.

## Nội suy latent

Nhờ prior được điều chuẩn, nội suy giữa hai latent của VAE thường mượt hơn autoencoder thông thường.

Tuy nhiên, nội suy tuyến tính trong không gian Gaussian không phải lúc nào cũng là đường đi phù hợp nhất theo hình học xác suất; một số trường hợp dùng nội suy trên mặt cầu (spherical interpolation).

Hình ảnh nội suy mượt cũng không tự động chứng minh các chiều latent tương ứng với khái niệm ngữ nghĩa dễ đọc.

## So sánh VAE, GAN và Diffusion

VAE có mô hình latent xác suất rõ ràng, tối ưu cận dưới ELBO và thường huấn luyện ổn định, nhưng các mô hình pixel cổ điển có thể cho ảnh mờ nếu likelihood hoặc decoder không đủ phù hợp.

GAN học phân bố thông qua trò chơi đối kháng, có thể tạo ảnh sắc nét nhưng dễ gặp mất ổn định và mode collapse.

Diffusion học quá trình khử nhiễu lặp, thường cho chất lượng sinh cao và huấn luyện ổn định hơn GAN, đổi lại việc lấy mẫu truyền thống cần nhiều bước.

Các hệ thống hiện đại thường kết hợp nhiều ý tưởng thay vì tách biệt tuyệt đối.

## Liên hệ với Latent Diffusion

Một hệ thống kiểu Stable Diffusion thường có luồng:

```text
ảnh
→ VAE encoder
→ biểu diễn latent theo không gian
→ diffusion khử nhiễu trong latent
→ VAE decoder
→ ảnh
```

VAE giảm chi phí bằng cách đưa quá trình diffusion từ không gian pixel lớn sang không gian latent nén. Vì vậy VAE vẫn là thành phần quan trọng dù diffusion là cơ chế sinh được nhắc tới nhiều hơn.

## Liên hệ với Variational Inference

VAE không chỉ là “autoencoder có thêm nhiễu”. Nó thực hiện **suy luận biến phân được amortize (amortized variational inference)**: một encoder duy nhất học cách ánh xạ mọi `x` sang tham số posterior xấp xỉ, thay vì phải chạy một bài toán tối ưu riêng cho từng mẫu.

**Amortization** cho phép chia sẻ chi phí và tri thức suy luận trên toàn bộ tập dữ liệu.

## Mô hình tư duy

```text
Encoder: x → phân bố các nguyên nhân latent khả dĩ z
Prior:   giữ không gian latent có cấu trúc và dễ lấy mẫu
Decoder: z → phân bố của quan sát x
ELBO:    cân bằng giải thích dữ liệu và tương thích với prior
```

## Những hiểu lầm thường gặp

### “VAE encoder tạo trực tiếp một latent vector”

Thông thường encoder tạo tham số của một phân bố; latent sau đó được lấy mẫu bằng reparameterization.

### “KL chỉ là regularization chống overfitting”

Không. Nó còn buộc posterior xấp xỉ tương thích với prior và kiểm soát dung lượng thông tin của latent.

### “Loss của VAE luôn là MSE + KL”

Không. Thành phần tái tạo phụ thuộc likelihood đã chọn; MSE chỉ là một trường hợp.

### “VAE bảo đảm latent có các yếu tố con người đọc được”

Không. Disentanglement cần nhiều giả định và thiết kế bổ sung.

## Liên kết kiến thức

VAE kết hợp [Xác suất](../01_mathematical_foundations/02_probability_for_ai.md), [KL Divergence và Lý thuyết thông tin](../01_mathematical_foundations/05_information_theory.md), [Autoencoder](./06_autoencoders.md) và suy luận biến phân.

Xem tiếp: [Generative Adversarial Networks](./08_generative_adversarial_networks.md) và [Diffusion Models](./09_diffusion_models.md).