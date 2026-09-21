# Autoencoder: học biểu diễn bằng tái tạo

**Autoencoder (오토인코더 / bộ tự mã hóa)** là kiến trúc học ánh xạ:

\[
x\xrightarrow{Encoder}z\xrightarrow{Decoder}\hat x
\]

với mục tiêu tái tạo đầu vào:

\[
L=L(x,\hat x)
\]

Đây là một trong những cách trực quan nhất để hiểu học biểu diễn mà không cần nhãn do con người cung cấp. Tuy nhiên, “tái tạo tốt” không đồng nghĩa không gian tiềm ẩn có ý nghĩa ngữ nghĩa tốt. Nút thắt, nhiễu, kiến trúc và hàm mục tiêu quyết định loại thông tin nào được giữ lại.

## Autoencoder thiếu chiều

Nếu chiều tiềm ẩn:

\[
d_z<d_x
\]

mạng bị buộc phải nén đầu vào qua một **nút thắt (bottleneck)**.

Autoencoder tuyến tính với sai số bình phương và các ràng buộc phù hợp học một không gian con có quan hệ chặt với PCA. Autoencoder phi tuyến có thể học manifold phi tuyến phức tạp hơn.

Tuy vậy, nếu decoder quá mạnh, latent vẫn có thể mã hóa nhiều chi tiết riêng lẻ của dữ liệu thay vì hình thành biểu diễn trừu tượng hữu ích.

## Hàm mất mát tái tạo

Dữ liệu liên tục đã chuẩn hóa có thể dùng MSE:

\[
L=\|x-\hat x\|_2^2
\]

Dữ liệu nhị phân hoặc pixel được mô hình hóa kiểu Bernoulli từng được huấn luyện bằng BCE.

Trong tái tạo ảnh hiện đại, **hàm mất mát cảm nhận (perceptual loss)** đôi khi phù hợp hơn vì MSE theo pixel phạt mạnh các dịch chuyển nhỏ và có thể khuyến khích ảnh trung bình bị mờ.

Hàm mất mát định nghĩa điều gì được xem là một bản tái tạo “giống” đầu vào.

## Autoencoder dư chiều

Nếu chiều latent lớn hơn đầu vào, mô hình có thể học ánh xạ đồng nhất một cách tầm thường. Khi đó cần thêm điều chuẩn hoặc làm hỏng dữ liệu đầu vào để buộc mạng học cấu trúc hữu ích.

Các biến thể phổ biến gồm:

- autoencoder thưa (sparse autoencoder);
- autoencoder khử nhiễu (denoising autoencoder);
- autoencoder co rút (contractive autoencoder).

## Sparse Autoencoder

Sparse Autoencoder khuyến khích phần lớn activation tiềm ẩn gần `0`:

\[
L=L_{recon}+\lambda R(z)
\]

Tính thưa buộc mô hình chỉ kích hoạt một số đặc trưng giới hạn cho mỗi đầu vào.

Trong nghiên cứu khả năng diễn giải cơ chế của LLM, sparse autoencoder cũng được dùng để thử phân rã activation dày đặc thành các đặc trưng học được thưa hơn. Tuy nhiên việc gán ý nghĩa ổn định cho các đặc trưng này vẫn là vấn đề nghiên cứu, không phải kết quả đảm bảo.

## Denoising Autoencoder

Làm hỏng đầu vào:

\[
\tilde x\sim q(\tilde x\mid x)
\]

rồi huấn luyện:

\[
\tilde x\to Encoder\to z\to Decoder\to \hat x\approx x
\]

Mô hình không thể chỉ sao chép từng giá trị đầu vào mà phải học cấu trúc giúp khôi phục dữ liệu sạch.

Nguyên lý này liên hệ trực tiếp với masked language modeling và diffusion: cố ý loại bỏ hoặc thêm nhiễu vào dữ liệu, sau đó học cách phục hồi thông tin ban đầu.

## Contractive Autoencoder

Contractive Autoencoder phạt độ nhạy của biểu diễn latent đối với thay đổi nhỏ của đầu vào, chẳng hạn bằng chuẩn Jacobian của encoder:

\[
\|\partial f(x)/\partial x\|_F^2
\]

Mục tiêu là tạo biểu diễn ổn định hơn trong lân cận của mỗi mẫu dữ liệu.

## Autoencoder cho phát hiện bất thường

Nếu huấn luyện chủ yếu trên dữ liệu bình thường, mô hình có thể tái tạo các mẫu quen thuộc tốt hơn mẫu bất thường. Khi đó sai số tái tạo:

\[
s(x)=\|x-\hat x\|
\]

có thể được dùng làm **điểm bất thường (anomaly score)**.

Tuy nhiên, autoencoder có năng lực quá lớn đôi khi cũng tái tạo anomaly tốt; ngược lại một số mẫu bình thường nhưng hiếm có thể bị tái tạo kém. Vì vậy điểm số vẫn cần được đánh giá và chọn ngưỡng trên dữ liệu phù hợp.

## Nội suy trong không gian latent

Nếu không gian latent mượt, có thể nội suy:

\[
z(\alpha)=(1-\alpha)z_1+\alpha z_2
\]

rồi giải mã các điểm trung gian.

Autoencoder cơ bản không đảm bảo những vùng nằm giữa các mã huấn luyện sẽ giải mã thành dữ liệu hợp lý. Hạn chế này là một động lực quan trọng cho Variational Autoencoder, nơi phân bố latent được điều chuẩn theo cách xác suất.

## Autoencoder cho dữ liệu chuỗi

Encoder có thể là RNN hoặc Transformer; decoder tái tạo chuỗi. Nút thắt latent có thể đóng vai trò tóm tắt chuỗi.

Tuy nhiên, nếu decoder tự hồi quy quá mạnh, nó có thể dự đoán tốt dựa trên ngữ cảnh trước đó mà gần như bỏ qua latent. Đây là một dạng **bỏ qua biến tiềm ẩn (latent ignoring)** và có quan hệ với posterior collapse trong VAE.

Kiến trúc và hàm mục tiêu phải bảo đảm latent thực sự mang thông tin cần thiết.

## Convolutional Autoencoder

Ảnh thường dùng CNN để mã hóa và giảm kích thước, sau đó decoder tăng kích thước để tái tạo ảnh. Decoder có thể dùng transposed convolution hoặc resize kết hợp convolution.

Transposed convolution có thể tạo **nhiễu dạng bàn cờ (checkerboard artifact)** nếu stride và kích thước kernel tương tác không phù hợp.

## Autoencoder so với PCA

PCA có các đặc điểm: tuyến tính, có nghiệm dựa trên SVD, tối ưu toàn cục cho tái tạo tuyến tính theo sai số bình phương và các thành phần trực giao.

Autoencoder linh hoạt hơn: có thể phi tuyến, được huấn luyện lặp bằng tối ưu số, dùng nhiều loại kiến trúc và hàm mất mát, đồng thời các chiều latent không nhất thiết trực giao hoặc có ý nghĩa định danh duy nhất.

PCA phù hợp khi cấu trúc tuyến tính đã đủ và cần tính ổn định hoặc khả năng giải thích. Autoencoder phù hợp khi dữ liệu và quy mô thực sự biện minh cho biểu diễn phi tuyến.

## Autoencoder không đồng nghĩa codec nén tệp

Autoencoder học có thể là thành phần của hệ thống nén, nhưng nén tệp thực tế còn cần lượng tử hóa (quantization), mô hình xác suất và mã hóa entropy.

Vector latent dạng số thực liên tục chưa phải bitstream đã nén. Mục tiêu **rate–distortion** thường có dạng:

\[
L=Distortion+\lambda Rate
\]

Điều này nối học biểu diễn với Lý thuyết thông tin.

## Nút thắt không chỉ đến từ số chiều

Ngay cả khi latent có nhiều chiều, hệ thống vẫn có thể tạo nút thắt thông tin bằng:

- tính thưa;
- nhiễu;
- lượng tử hóa;
- độ chính xác thấp;
- giới hạn dung lượng kênh;
- prior xác suất.

VAE sử dụng điều chuẩn phân bố thay vì chỉ giảm số chiều.

## Autoencoder và mô hình nền tảng

Masked Autoencoder tái tạo patch ảnh bị che. BERT tái tạo phân phối token bị mask. Denoising Seq2Seq làm hỏng văn bản rồi học khôi phục bản gốc.

Các phương pháp này không hoàn toàn giống autoencoder cổ điển, nhưng chia sẻ nguyên lý chung: **học tự giám sát bằng cách cố ý loại bỏ/làm hỏng thông tin rồi học phục hồi cấu trúc dữ liệu**.

## Mô hình tư duy

> Autoencoder đặt câu hỏi: “Nếu dữ liệu buộc phải đi qua một kênh bị giới hạn, biểu diễn nào giữ đủ cấu trúc để tái tạo đầu vào?”

Chính loại ràng buộc trên kênh quyết định dạng trừu tượng mà mô hình có xu hướng học.

## Những hiểu lầm thường gặp

### “Latent nhỏ hơn thì chắc chắn có ý nghĩa”

Không. Nén kích thước không tự động tạo ngữ nghĩa hữu ích.

### “Sai số tái tạo thấp nghĩa đặc trưng downstream tốt”

Không. Mô hình có thể dành năng lực để giữ chi tiết nhiễu không liên quan tới tác vụ sau đó.

### “Autoencoder tự động sinh được mẫu mới thực tế”

Không. Phân bố latent của autoencoder thường không có hình dạng thuận tiện để lấy mẫu tùy ý.

### “Nén bằng Autoencoder chính là nén tệp”

Không. Hệ thống nén thực tế còn cần lượng tử hóa, mã hóa entropy và mô hình rate.

## Liên kết kiến thức

Autoencoder mở rộng [Học biểu diễn](../05_neural_networks/08_representation_learning.md) và [Giảm chiều](../04_machine_learning/12_dimensionality_reduction.md).

Xem tiếp: [Variational Autoencoder](./07_variational_autoencoders.md), nơi không gian latent trở thành phân bố xác suất có thể lấy mẫu.