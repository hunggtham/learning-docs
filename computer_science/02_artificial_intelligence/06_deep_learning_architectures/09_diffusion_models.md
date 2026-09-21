# Diffusion Models: tạo dữ liệu bằng quá trình khử nhiễu có điều kiện

**Diffusion Model (확산 모델 / mô hình khuếch tán)** học phân bố sinh theo một cách khác GAN: thay vì yêu cầu generator tạo ngay một mẫu hoàn chỉnh trong một bước, ta định nghĩa một **quá trình thuận (forward process)** dần phá dữ liệu thành nhiễu, rồi huấn luyện mô hình học **quá trình đảo ngược khử nhiễu (reverse denoising process)** để đi từ nhiễu trở lại dữ liệu có cấu trúc.

Cách phân rã này biến bài toán sinh phức tạp thành một chuỗi bài toán khử nhiễu cục bộ tương đối ổn định.

## Quá trình khuếch tán thuận

Bắt đầu từ dữ liệu thật:

\[
x_0\sim p_{data}
\]

Mỗi bước thêm nhiễu Gaussian:

\[
q(x_t\mid x_{t-1})=
\mathcal N(\sqrt{1-\beta_t}x_{t-1},\beta_t I)
\]

Đặt:

\[
\alpha_t=1-\beta_t,
\qquad
\bar\alpha_t=\prod_{s=1}^{t}\alpha_s
\]

Ta có thể lấy mẫu trực tiếp tại bất kỳ bước thời gian nào:

\[
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,
\qquad \epsilon\sim\mathcal N(0,I)
\]

Khi `t` lớn, tín hiệu gốc bị phá dần và `x_t` tiến gần nhiễu Gaussian.

## Quá trình đảo ngược

Mục tiêu là học:

\[
p_\theta(x_{t-1}\mid x_t)
\]

Nếu mô hình biết thành phần nhiễu hoặc score của dữ liệu, nó có thể khử nhiễu từng bước.

Một tham số hóa phổ biến của DDPM huấn luyện mạng nơ-ron dự đoán nhiễu đã được thêm:

\[
\epsilon_\theta(x_t,t)
\]

với hàm mất mát đơn giản hóa:

\[
L=\mathbb E_{x_0,\epsilon,t}
\left[
\|\epsilon-\epsilon_\theta(x_t,t)\|^2
\right]
\]

Mạng nhận mẫu bị nhiễu cùng mức thời gian và học ước lượng thành phần nhiễu.

## Vì sao dự đoán nhiễu giúp sinh dữ liệu?

Từ:

\[
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
\]

nếu mô hình ước lượng được `ε`, ta có thể suy ra xấp xỉ của dữ liệu sạch `x_0` hoặc trung bình của bước đảo ngược. Lặp nhiều bước sẽ dần khôi phục cấu trúc dữ liệu.

Mô hình đang học một trường khử nhiễu qua nhiều mức noise chứ không phải học một ánh xạ duy nhất từ nhiễu sang ảnh trong một bước.

## Mã hóa timestep

Cùng một ảnh bị nhiễu nhẹ và bị nhiễu gần hoàn toàn cần cách xử lý khác nhau. Vì vậy mô hình nhận thêm embedding của timestep hoặc mức nhiễu.

Các embedding hình sin hoặc Fourier thường biến scalar `t` thành vector rồi đưa vào mạng cùng đặc trưng ảnh.

## Kiến trúc U-Net

Diffusion ảnh truyền thống thường dùng U-Net:

```text
độ phân giải cao
→ encoder giảm kích thước
→ bottleneck
→ decoder tăng kích thước
```

Các kết nối tắt (skip connection) truyền chi tiết không gian từ nhánh giảm kích thước sang nhánh tăng kích thước.

U-Net diffusion hiện đại thường có residual block, attention/cross-attention và normalization. Các kiến trúc Transformer cho diffusion như DiT ngày càng phổ biến ở quy mô lớn.

## Diffusion có điều kiện

Nếu muốn sinh `x` dựa trên văn bản hoặc nhãn `c`:

\[
\epsilon_\theta(x_t,t,c)
\]

bộ mã hóa văn bản tạo embedding và cross-attention đưa điều kiện đó vào mạng khử nhiễu.

Vì vậy text-to-image thực chất là một hệ thống đa phương thức kết hợp bộ mã hóa điều kiện với mô hình sinh khử nhiễu.

## Classifier Guidance

Một classifier bên ngoài có thể ước lượng:

\[
\nabla_{x_t}\log p(c\mid x_t)
\]

và điều chỉnh hướng đảo ngược về phía lớp mong muốn.

Cách này cải thiện khả năng điều kiện hóa nhưng cần classifier được huấn luyện trên dữ liệu ở nhiều mức nhiễu.

## Classifier-Free Guidance

Trong huấn luyện, cùng một mô hình đôi khi nhận điều kiện và đôi khi bị bỏ điều kiện. Khi suy luận, kết hợp dự đoán có điều kiện và không điều kiện:

\[
\epsilon_{guided}
=\epsilon_{uncond}
+w(\epsilon_{cond}-\epsilon_{uncond})
\]

`w` là hệ số **guidance**.

Tăng guidance thường làm đầu ra bám prompt mạnh hơn nhưng có thể giảm đa dạng hoặc tăng artifact và quá bão hòa. Vì vậy không có quy tắc “càng lớn càng tốt”.

## Cách nhìn Score-Based

**Score function**:

\[
\nabla_x\log p_t(x)
\]

chỉ hướng làm mật độ dữ liệu tăng tại một mức nhiễu `t` nhất định.

Denoising score matching và diffusion có quan hệ rất chặt. Trong biểu diễn thời gian liên tục, quá trình này có thể được mô tả bằng phương trình vi phân ngẫu nhiên (SDE).

Cách nhìn này cho nền tảng xác suất sâu hơn trực giác “mạng chỉ dự đoán nhiễu”.

## Tốc độ lấy mẫu

DDPM gốc thường cần hàng trăm hoặc hàng nghìn bước đảo ngược, chậm hơn generator GAN một bước.

Các kỹ thuật tăng tốc gồm:

- DDIM;
- bộ giải số bậc cao;
- các phương pháp kiểu DPM-Solver;
- distillation và consistency model;
- lịch lấy mẫu ít bước hơn.

Sampler thay đổi cách tích phân quỹ đạo đảo ngược, tạo sự đánh đổi giữa tốc độ, chất lượng và độ đa dạng.

## DDIM

DDIM xây quỹ đạo lấy mẫu không-Markov, có thể gần xác định hơn nhưng dùng cùng mục tiêu huấn luyện cơ bản. Nó cho phép giảm số bước lấy mẫu đáng kể và hỗ trợ các thao tác latent thuận tiện hơn.

Các tham số kiểu `η` có thể điều khiển mức ngẫu nhiên tùy cách triển khai.

## Latent Diffusion

Diffusion trực tiếp trên pixel rất tốn chi phí. Latent Diffusion trước hết nén ảnh:

\[
x\xrightarrow{VAE\ encoder}z
\]

sau đó chạy diffusion trên `z`, rồi giải mã:

\[
z_0\xrightarrow{VAE\ decoder}\hat x
\]

Không gian latent có độ phân giải nhỏ hơn nhiều, làm chi phí U-Net hoặc Transformer giảm đáng kể.

Đây là lý do hiểu VAE rất quan trọng đối với hệ thống text-to-image hiện đại.

## Image-to-Image và Inpainting

Image-to-image thường bắt đầu từ latent của ảnh nguồn, thêm lượng nhiễu có kiểm soát rồi khử nhiễu dưới điều kiện văn bản. Mức nhiễu quyết định đầu ra được phép lệch khỏi ảnh gốc bao xa.

**Inpainting** giữ vùng đã biết và khử nhiễu vùng bị che dựa trên ngữ cảnh xung quanh cùng prompt. **Outpainting** mở rộng canvas theo nguyên lý tương tự.

Đây chủ yếu là các biến thể điều kiện hóa và kiểm soát, không phải những họ mô hình hoàn toàn khác.

## Điều kiện hóa kiểu ControlNet

Các tín hiệu cấu trúc bổ sung như biên cạnh, pose hoặc depth có thể đi qua một nhánh điều khiển song song để tác động lên mô hình diffusion đã pretrain.

Thiết kế này tách điều khiển ngữ nghĩa bằng văn bản khỏi điều khiển hình học và bố cục.

## So sánh Diffusion, VAE và GAN

| Họ mô hình | Tín hiệu huấn luyện | Lấy mẫu | Đánh đổi điển hình |
|---|---|---|---|
| VAE | ELBO / tái tạo + KL | một lần qua decoder | latent mượt, mô hình xác suất rõ, đôi khi ảnh mềm hơn |
| GAN | critic đối kháng | một lần qua generator | sắc nét và nhanh, nhưng khó huấn luyện và có mode collapse |
| Diffusion | khử nhiễu / score | nhiều bước | ổn định và chất lượng cao, truyền thống chậm hơn |

Hệ thống hiện đại thường lai ghép nhiều cơ chế, nên bảng này mô tả nguyên lý chứ không phải ranh giới tuyệt đối giữa sản phẩm.

## Diffusion cho dữ liệu ngoài ảnh

Diffusion và score-based model đã được áp dụng cho âm thanh, video, 3D, phân tử và hành động liên tục. Các biến thể diffusion rời rạc điều chỉnh quá trình cho token hoặc biến phân loại.

Ngôn ngữ rời rạc vẫn chủ yếu do Transformer tự hồi quy thống trị vì cơ chế làm hỏng/phục hồi token và bài toán giải mã có những đánh đổi khác ảnh liên tục.

## Dữ liệu, bản quyền và an toàn

Hành vi của mô hình sinh phản ánh phân bố huấn luyện. Memorization vẫn có thể xảy ra; mô hình có thể tái tạo phong cách, khái niệm hoặc thiên lệch có trong dữ liệu. Vì vậy nguồn gốc dữ liệu và loại trùng rất quan trọng.

Bộ lọc an toàn có thể đặt ở dữ liệu huấn luyện, prompt, latent/quá trình sinh hoặc đầu ra. Đây là bài toán cấp hệ thống, không thể giải quyết chỉ bằng phương trình diffusion.

## Mô hình tư duy

```text
Huấn luyện:
dữ liệu thật → thêm mức nhiễu đã biết → mô hình học dự đoán cách loại nhiễu

Sinh:
nhiễu ngẫu nhiên → khử một ít → khử một ít → ... → mẫu có cấu trúc
```

Ở mỗi mức nhiễu, mô hình học hướng cục bộ đưa mẫu về những vùng có mật độ dữ liệu hợp lý hơn.

## Những hiểu lầm thường gặp

### “Diffusion lưu ảnh rồi tìm ảnh gần nhất”

Không. Quá trình sinh chạy động lực khử nhiễu đã học. Memorization là một rủi ro riêng, không phải cơ chế định nghĩa của diffusion.

### “Dự đoán noise chỉ là mẹo tùy ý”

Không. Nó xuất phát từ cách tham số hóa quá trình xác suất đảo ngược và score matching, đồng thời tạo hàm mục tiêu ổn định.

### “Càng nhiều bước diffusion càng tốt”

Không. Chất lượng còn phụ thuộc sampler, bậc phương pháp, mô hình và lịch nhiễu; sampler hiện đại có thể đạt chất lượng tốt với ít bước hơn.

### “Guidance scale chỉ điều khiển chất lượng ảnh”

Không. Nó đánh đổi độ bám điều kiện với độ đa dạng và artifact.

### “Stable Diffusion chạy trực tiếp trên pixel”

Không. Các hệ thống latent diffusion tiêu biểu chạy phần lớn quá trình khử nhiễu trong không gian latent do VAE nén, sau đó mới giải mã về pixel.

## Liên kết kiến thức

Diffusion tổng hợp [Xác suất](../01_mathematical_foundations/02_probability_for_ai.md), [Tính toán số](../01_mathematical_foundations/07_numerical_computation.md), [Autoencoder/VAE](./06_autoencoders.md), [Attention](./04_attention.md) và điều kiện hóa đa phương thức.

Phần `13_speech_audio_and_multimodal/` sẽ nối diffusion với các hệ thống nền tảng văn bản, ảnh, âm thanh và video.