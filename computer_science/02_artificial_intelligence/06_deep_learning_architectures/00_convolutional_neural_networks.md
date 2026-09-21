# Convolutional Neural Network: tận dụng cấu trúc không gian

**Convolutional Neural Network (CNN / 합성곱 신경망 / mạng nơ-ron tích chập)** được phát triển vì MLP dày đặc đối xử các chiều đầu vào gần như độc lập, trong khi ảnh có cấu trúc rất mạnh: các pixel gần nhau tạo thành mẫu cục bộ, cùng một cạnh có thể xuất hiện ở nhiều vị trí và cấu trúc thị giác thường hình thành theo tầng từ cạnh → texture → bộ phận → vật thể.

CNN mã hóa hai **thiên lệch quy nạp (inductive bias)** chính: **kết nối cục bộ (local connectivity)** và **chia sẻ trọng số (weight sharing)**.

## Vì sao flatten ảnh vào MLP gây lãng phí?

Ảnh RGB `224×224×3` có 150.528 giá trị. Một dense layer 4.096 unit cần hơn 600 triệu weight chỉ riêng layer đầu tiên.

Quan trọng hơn, flatten làm mất cấu trúc không gian tường minh. Pixel tại `(10,10)` và `(10,11)` vốn ở sát nhau, nhưng sau khi biến thành vector, MLP không được cung cấp một giả định đặc biệt rằng hai vị trí đó có quan hệ cục bộ.

CNN giữ nguyên lưới không gian và xử lý bằng các kernel nhỏ.

## Phép convolution

Một kernel 2D nhỏ, ví dụ `3×3`, trượt qua ảnh. Với một channel:

\[
y_{i,j}=\sum_{u,v}K_{u,v}x_{i+u,j+v}
\]

Nhiều framework Deep Learning thực tế tính **cross-correlation** thay vì lật kernel theo định nghĩa convolution toán học truyền thống, nhưng vẫn dùng tên convolution.

Với input nhiều channel:

\[
W\in R^{C_{out}\times C_{in}\times K_h\times K_w}
\]

mỗi output channel kết hợp một patch cục bộ trên toàn bộ input channel.

## Chia sẻ trọng số

Cùng một kernel được dùng lại ở mọi vị trí không gian. Nếu kernel học mẫu cạnh dọc, nó có thể phát hiện mẫu này ở nhiều nơi trong ảnh.

Số tham số:

\[
C_{out}(C_{in}K_hK_w+1)
\]

không tăng trực tiếp theo chiều rộng hoặc chiều cao ảnh. Đây là lợi thế rất lớn so với dense connection.

## Tính đồng biến theo phép tịnh tiến

Nếu input dịch chuyển, feature map của convolution cũng dịch chuyển tương ứng trong điều kiện lý tưởng và bỏ qua ảnh hưởng biên hoặc stride. Đây là **tính đồng biến (translation equivariance)**, không phải bất biến hoàn toàn.

Pooling hoặc global aggregation có thể làm prediction cuối trở nên bất biến hơn với thay đổi vị trí nhỏ.

## Stride, Padding và Dilation

Kích thước output 1D:

\[
O=\left\lfloor\frac{N+2P-D(K-1)-1}{S}+1\right\rfloor
\]

Trong đó `S` là stride, `P` là padding và `D` là dilation.

- `stride > 1` giảm kích thước không gian;
- padding kiểm soát kích thước và cách xử lý biên;
- dilation mở rộng vùng quan sát mà không cần tăng nhiều tham số kernel.

## Receptive Field

Một unit ở layer sâu phụ thuộc vào một vùng ngày càng lớn của ảnh gốc. Xếp chồng nhiều convolution `3×3` làm **trường tiếp nhận (receptive field)** tăng theo depth.

Layer đầu xử lý pattern cục bộ; layer sâu tích hợp ngữ cảnh rộng hơn.

**Receptive field hiệu dụng (effective receptive field)** có thể nhỏ hơn vùng lý thuyết vì mức đóng góp của các vị trí không phân bố đều.

## Pooling

Max pooling:

\[
y_{i,j}=\max_{(u,v)\in window}x_{i+u,j+v}
\]

Average pooling lấy trung bình trong cửa sổ.

Pooling giảm độ phân giải, mở rộng receptive field hiệu dụng và tạo một mức bất biến cục bộ. CNN hiện đại đôi khi dùng strided convolution thay cho pooling.

**Global Average Pooling** lấy trung bình toàn bộ spatial map theo từng channel và giúp giảm lượng tham số ở classification head.

## Feature phân cấp

Một cách diễn giải kinh điển:

```text
pixel
→ cạnh / hướng
→ texture / hình đơn giản
→ bộ phận
→ feature cấp vật thể
```

Không phải mọi channel đều ánh xạ sạch sang một concept cụ thể, nhưng trực giác phân cấp vẫn hữu ích vì receptive field và khả năng hợp thành tăng theo depth.

## ResNet và Skip Connection

CNN rất sâu khó tối ưu nếu chỉ xếp layer tuần tự.

ResNet block:

\[
y=x+F(x)
\]

thêm đường identity giúp tín hiệu và gradient truyền qua dễ hơn.

Thay vì phải học toàn bộ mapping mới, block chỉ cần học phần hiệu chỉnh còn thiếu `F(x)`.

Residual connection sau đó trở thành nguyên lý rất quan trọng cả trong Transformer.

## Convolution 1×1

Kernel `1×1` không kết hợp các vị trí lân cận nhưng trộn thông tin giữa các channel:

\[
y_{i,j}=W x_{i,j}
\]

Có thể xem đây là linear projection áp dụng độc lập tại từng vị trí, hữu ích để đổi số channel hoặc tạo bottleneck.

## Depthwise Separable Convolution

Convolution chuẩn trộn cả cấu trúc không gian và channel trong cùng một operation.

Depthwise separable convolution tách thành:

1. convolution không gian riêng trên từng channel;
2. pointwise convolution `1×1` để trộn channel.

Cách này giảm compute đáng kể và được dùng trong các kiến trúc kiểu MobileNet.

## BatchNorm và CNN Training

CNN truyền thống thường dùng chuỗi:

```text
Convolution → BatchNorm → ReLU
```

Các kiến trúc mới có thể thay đổi thứ tự, normalization hoặc activation.

BatchNorm hoạt động tốt khi batch ảnh đủ lớn; với detection hoặc segmentation có batch nhỏ, GroupNorm đôi khi phù hợp hơn.

## CNN không chỉ dùng cho ảnh

Convolution 1D có thể dùng với âm thanh, time series hoặc pattern cục bộ trong text.

Convolution 3D phù hợp với video hoặc thể tích y khoa.

Graph convolution mở rộng trực giác tổng hợp lân cận sang cấu trúc không phải lưới, nhưng operation toán học không hoàn toàn giống grid convolution.

## Classification, Detection và Segmentation

Image classification trả một hoặc vài label.

Object detection cần bounding box cùng class.

Segmentation tạo prediction cho từng pixel.

Cùng một CNN backbone có thể cấp feature cho nhiều loại head. Cấu trúc output của task quyết định phần kiến trúc phía sau feature extractor.

## CNN và Vision Transformer

CNN mã hóa mạnh locality và chia sẻ theo phép tịnh tiến.

Vision Transformer chia ảnh thành patch rồi học tương tác toàn cục bằng attention.

CNN thường hiệu quả dữ liệu nhờ inductive bias mạnh; ViT có khả năng scale rất tốt với pretraining lớn. Nhiều hệ vision hiện đại kết hợp cả hai loại bias hoặc đưa locality vào Transformer.

Không có quy tắc đơn giản rằng “Transformer đã thay thế CNN”.

## Mô hình tư duy

> CNN giả định pattern cục bộ quan trọng, cùng một loại pattern có thể xuất hiện ở nhiều vị trí và khái niệm thị giác phức tạp có thể được xây phân cấp từ các feature cục bộ.

## Các hiểu lầm thường gặp

### “Convolution tự động làm mô hình bất biến với phép tịnh tiến”

Không. Convolution chủ yếu có tính đồng biến; pooling, aggregation và augmentation mới góp phần tạo bất biến.

### “CNN kernel là edge filter viết tay”

Không. Computer Vision cổ điển từng dùng filter thủ công; kernel của CNN được học end-to-end.

### “Neuron ở layer sâu luôn đại diện một bộ phận vật thể”

Không. Representation thường phân tán; hierarchy chỉ là mô hình tư duy gần đúng.

### “CNN đã lỗi thời sau Vision Transformer”

Không. CNN vẫn mạnh, hiệu quả và được triển khai rộng rãi; nhiều kiến trúc hiện đại đang hội tụ hoặc lai hóa các ý tưởng của cả hai.

## Liên kết kiến thức

CNN ứng dụng trực tiếp [Representation Learning](../05_neural_networks/08_representation_learning.md), [Regularization và Weight Sharing](../05_neural_networks/07_regularization.md) và [Residual Connection](../05_neural_networks/04_backpropagation.md).

Phần Computer Vision sau này sẽ mở rộng sang detection, segmentation và Vision Transformer.