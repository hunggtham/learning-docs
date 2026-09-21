# Generative Adversarial Network: học phân bố qua trò chơi đối kháng

**Generative Adversarial Network (GAN / 생성적 적대 신경망 / mạng sinh đối kháng)** học mô hình sinh bằng cách đặt **bộ sinh (generator)** và **bộ phân biệt (discriminator)** vào một trò chơi đối kháng. Generator tạo mẫu giả; discriminator cố phân biệt dữ liệu thật và dữ liệu sinh. Generator được cải thiện để ngày càng khó bị discriminator phát hiện.

GAN quan trọng vì nó cho thấy học sinh dữ liệu không nhất thiết phải dựa trên likelihood tường minh. Phân bố dữ liệu có thể được học thông qua tín hiệu phản hồi do một discriminator hoặc critic cũng được học tạo ra.

## Hai mạng nơ-ron

Generator:

\[
z\sim p(z),\qquad x_{fake}=G_\theta(z)
\]

Discriminator:

\[
D_\phi(x)\in(0,1)
\]

ước lượng đầu vào giống dữ liệu thật hay dữ liệu do generator tạo.

Mục tiêu minimax gốc:

\[
\min_G\max_D
\mathbb E_{x\sim p_{data}}[\log D(x)]
+
\mathbb E_{z\sim p(z)}[\log(1-D(G(z)))]
\]

## Trực giác về discriminator tối ưu

Với phân bố generator `p_g` cố định, discriminator tối ưu có dạng:

\[
D^*(x)=\frac{p_{data}(x)}{p_{data}(x)+p_g(x)}
\]

Khi thay nghiệm này vào hàm mục tiêu, GAN gốc có liên hệ với Jensen–Shannon divergence dưới các giả định lý tưởng hóa.

Vì vậy generator cố làm `p_g` ngày càng khó phân biệt với `p_data`.

## Hàm mất mát Generator không bão hòa

Trong mục tiêu gốc, generator tối thiểu hóa:

\[
\log(1-D(G(z)))
\]

nhưng gradient có thể rất yếu nếu ở giai đoạn đầu discriminator dễ dàng nhận ra mọi mẫu giả.

Một lựa chọn phổ biến hơn là tối đa hóa:

\[
\log D(G(z))
\]

hoặc tối thiểu hóa giá trị âm tương ứng. Điểm cân bằng trực giác tương tự nhưng tín hiệu gradient ở giai đoạn đầu thường mạnh hơn. Đây được gọi là **non-saturating generator loss**.

## Vì sao adversarial loss có thể tạo ảnh sắc nét?

MSE theo pixel có xu hướng lấy trung bình khi tồn tại nhiều đầu ra hợp lý, nên ảnh có thể bị mờ.

Discriminator học một tiêu chí nhiều chiều về việc “dữ liệu này có giống phân bố thật hay không”, cung cấp tín hiệu cảm nhận phong phú hơn sai số từng pixel. Nhờ vậy GAN có thể tạo ảnh sắc nét, nhưng đổi lại quá trình huấn luyện trở thành trò chơi giữa hai mục tiêu liên tục thay đổi.

## Mode Collapse

Generator có thể ánh xạ nhiều latent khác nhau về cùng một hoặc một số ít kiểu đầu ra vẫn đủ để đánh lừa discriminator.

Hiện tượng này gọi là **sụp đổ mode (mode collapse)**. Mẫu riêng lẻ có thể trông rất thật nhưng toàn bộ bộ sinh thiếu đa dạng.

Do đó đánh giá GAN phải xem cả độ chân thực lẫn độ phủ của phân bố, không chỉ nhìn một vài ảnh đẹp.

## Bất ổn trong huấn luyện

Tối ưu GAN không phải tối thiểu hóa một hàm cố định: cả generator và discriminator cùng thay đổi. Có thể xuất hiện dao động, discriminator quá mạnh làm generator thiếu gradient, generator khai thác điểm mù tạm thời của discriminator hoặc toàn bộ quá trình bị phân kỳ.

Sự cân bằng giữa kiến trúc, learning rate, số bước cập nhật của hai bên và regularization có ảnh hưởng lớn tới ổn định.

## Wasserstein GAN

WGAN thay cách nhìn discriminator-xác suất bằng **critic** và sử dụng trực giác Wasserstein-1 / Earth Mover:

\[
W(p_r,p_g)=\sup_{\|f\|_L\le1}
\mathbb E_{p_r}[f(x)]-
\mathbb E_{p_g}[f(x)]
\]

Hàm critic phải thỏa ràng buộc Lipschitz. WGAN ban đầu dùng cắt trọng số; WGAN-GP dùng phạt gradient:

\[
\lambda(\|\nabla_{\hat x}D(\hat x)\|_2-1)^2
\]

Cách này thường cho tín hiệu huấn luyện ổn định hơn trong nhiều cấu hình.

## Conditional GAN

Có thể điều kiện hóa generator và discriminator theo nhãn hoặc ngữ cảnh `y`:

\[
G(z,y),\qquad D(x,y)
\]

nhờ đó sinh dữ liệu theo lớp hoặc điều kiện cụ thể.

GAN ảnh-sang-ảnh có thể dùng ảnh nguồn làm điều kiện, chẳng hạn biên cạnh → ảnh thật hoặc segmentation mask → ảnh.

## CycleGAN

Khi không có các cặp mẫu tương ứng trực tiếp, CycleGAN học hai ánh xạ `G:X→Y`, `F:Y→X` và thêm điều kiện nhất quán chu trình:

\[
F(G(x))\approx x
\]

\[
G(F(y))\approx y
\]

Ràng buộc này khuyến khích giữ cấu trúc, nhưng không bảo đảm ánh xạ đúng về ngữ nghĩa; mô hình vẫn có thể khai thác những lối tắt khó nhận thấy.

## StyleGAN

Họ StyleGAN tái thiết kế generator bằng mạng ánh xạ (mapping network), điều biến phong cách ở nhiều tầng và điều khiển đa tỉ lệ, tạo ra chất lượng ảnh rất cao.

Ý nghĩa kiến trúc quan trọng là thông tin latent được đưa vào nhiều mức của generator thay vì chỉ xuất hiện ở đầu vào.

## Đánh giá GAN

**Fréchet Inception Distance (FID)** so sánh trung bình và hiệp phương sai của biểu diễn Inception giữa dữ liệu thật và dữ liệu sinh:

\[
FID=\|\mu_r-\mu_g\|^2+
Tr(\Sigma_r+\Sigma_g-2(\Sigma_r\Sigma_g)^{1/2})
\]

FID thấp thường tốt hơn, nhưng kết quả phụ thuộc bộ trích đặc trưng và kích thước mẫu, đồng thời không tách hoàn hảo độ chân thực với độ đa dạng.

Các thước đo Precision/Recall dành cho mô hình sinh cố tách chất lượng mẫu và độ phủ phân bố. Đánh giá của con người vẫn có thể cần thiết tùy bài toán.

## GAN và mô hình Likelihood tường minh

GAN định nghĩa một phân bố sinh ngầm thông qua phép lấy mẫu `z→G(z)`; thường không có mật độ `p_G(x)` dễ tính trực tiếp.

VAE và diffusion có mô hình xác suất huấn luyện tường minh hơn theo những cách khác nhau.

Một ưu điểm của GAN là sau khi huấn luyện, generator thường tạo mẫu chỉ bằng một forward pass, nhanh hơn quy trình diffusion nhiều bước truyền thống.

## Adversarial Training như một hàm mất mát được học

Một trực giác sâu của GAN là discriminator đóng vai trò **hàm mất mát được học (learned loss)** và liên tục thích ứng với điểm yếu của generator.

Thay vì con người thiết kế hoàn toàn tiêu chí giống nhau theo pixel, hệ thống học tiêu chí phân biệt dữ liệu thật và giả. Đổi lại, hàm mất mát trở nên không tĩnh vì chính discriminator cũng đang thay đổi.

## GAN khác Adversarial Example

Từ `adversarial` trong GAN nói về trò chơi đối kháng generator–discriminator. **Adversarial example** là đầu vào được cố ý biến đổi để làm mô hình dự đoán sai. Hai khái niệm cùng có yếu tố đối kháng nhưng là hai chủ đề khác nhau.

## Vì sao Diffusion thay GAN trong nhiều bài toán sinh ảnh?

Diffusion thường dễ huấn luyện ổn định hơn, bao phủ nhiều mode tốt hơn và thích hợp với điều kiện hóa quy mô lớn. GAN truyền thống thường cần cân bằng tinh tế giữa hai mạng.

Tuy nhiên GAN vẫn hữu ích khi cần sinh một lần với độ trễ thấp hoặc trong các miền chuyên biệt. Các mục tiêu đối kháng cũng tiếp tục xuất hiện trong thích ứng miền, học biểu diễn và nhiều bài toán khác.

## Mô hình tư duy

```text
Generator: đề xuất một mẫu tổng hợp
Discriminator/Critic: học điều gì phân biệt mẫu đó với dữ liệu thật
Phản hồi: ép generator tiến gần phân bố dữ liệu
```

Điểm đặc biệt là chính tiêu chí đánh giá cũng được học thông qua cạnh tranh.

## Những hiểu lầm thường gặp

### “GAN chỉ sao chép ảnh huấn luyện”

Không. Cơ chế định nghĩa là học ánh xạ từ latent sang mẫu; memorization có thể xảy ra nhưng không phải bản chất của GAN.

### “Ảnh sắc nét nghĩa phân bố sinh tốt”

Không. Mode collapse có thể cho ảnh rất đẹp nhưng cực kỳ thiếu đa dạng.

### “Độ chính xác discriminator nên tiến tới 100%”

Không. Ở cân bằng lý tưởng khi hai phân bố trùng nhau, discriminator không thể phân biệt và đầu ra gần `0.5`.

### “WGAN chỉ đổi tên loss”

Không. Nó thay khái niệm khoảng cách/phân kỳ và ràng buộc critic, làm thay đổi bản chất tín hiệu gradient.

## Liên kết kiến thức

GAN nối trực giác [Tìm kiếm đối kháng và trò chơi](../02_search_reasoning_and_planning/03_adversarial_search_and_games.md), [Tối ưu hóa](../01_mathematical_foundations/06_optimization.md), [Xác suất và học phân bố](../01_mathematical_foundations/02_probability_for_ai.md) và [Học biểu diễn](../05_neural_networks/08_representation_learning.md).

Xem tiếp: [Diffusion Models](./09_diffusion_models.md).