# Nền tảng Image Processing

Trước Deep Learning, Computer Vision dựa nhiều vào **xử lý ảnh (image processing / 영상 처리)**: biến đổi tín hiệu ảnh để làm nổi bật cấu trúc hữu ích. Dù model hiện đại có thể tự học feature, các nguyên lý filtering, edge, morphology và frequency vẫn rất quan trọng để hiểu data pipeline và failure mode.

## Convolution như Local Filtering

Với image `I` và kernel `K`, dạng discrete correlation/convolution thường dùng trong implementation tính weighted sum trên neighborhood:

\[
Y(i,j)=\sum_m\sum_n K(m,n)I(i+m,j+n)
\]

Một mean-blur kernel:

\[
\frac{1}{9}
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

làm mượt local variation bằng cách lấy trung bình vùng lân cận.

Edge kernel như Sobel xấp xỉ spatial derivative. CNN sau này giữ nguyên ý tưởng local filtering nhưng để kernel được học từ data thay vì hand-design hoàn toàn.

## Padding và Boundary

Khi kernel ở gần image border, neighborhood bị thiếu. Các strategy phổ biến:

- zero padding;
- reflection padding;
- replicate padding;
- valid convolution hoặc không padding.

Boundary choice ảnh hưởng output shape và có thể tạo artifact ở mép ảnh.

## Blur và Giảm Noise

Gaussian blur dùng kernel:

\[
G(x,y)=\frac{1}{2\pi\sigma^2}e^{-(x^2+y^2)/(2\sigma^2)}
\]

Pixel gần center có weight cao hơn; high-frequency noise bị suppress.

Nhưng blur cũng làm mất edge và fine detail. Denoising luôn là trade-off giữa giảm noise và giữ signal cần thiết.

## Edge và Gradient

Edge là vùng intensity thay đổi nhanh. Image gradient:

\[
\nabla I=(I_x,I_y)
\]

Magnitude:

\[
|\nabla I|=\sqrt{I_x^2+I_y^2}
\]

Direction biểu diễn orientation của local change.

Trước thời Deep Learning, edge là primitive cốt lõi cho shape detection, contour extraction và feature engineering.

## Canny Edge Detection

Pipeline Canny cổ điển:

```text
Gaussian smoothing
→ tính gradient
→ non-maximum suppression
→ double threshold
→ hysteresis tracking
```

Điểm đáng học không chỉ là thuật toán cụ thể, mà là cách pipeline tách rõ:

```text
giảm noise
→ phát hiện evidence cục bộ
→ giữ edge mạnh
→ nối edge dựa trên connectivity
```

## Thresholding

Binary segmentation đơn giản:

\[
B(x,y)=1[I(x,y)>T]
\]

Global threshold dễ fail khi illumination không đồng đều. Adaptive threshold dùng local statistic nên thích nghi tốt hơn với variation theo vùng.

Otsu method chọn threshold bằng cách tối ưu separation giữa các class theo giả định histogram phù hợp.

## Morphological Operation

Với binary mask và structuring element:

- **erosion (침식 / co)** làm foreground nhỏ lại;
- **dilation (팽창 / giãn)** làm foreground lớn ra;
- **opening** = erosion rồi dilation;
- **closing** = dilation rồi erosion.

Các operation này thường dùng để loại small noise, lấp hole hoặc nối component sau segmentation.

## Connected Component

Binary mask có thể được nhóm thành các **connected region**. Với mỗi component ta có thể tính:

```text
area
centroid
bounding box
perimeter
```

Điều này hữu ích trong OCR, industrial inspection và post-processing mask.

## Histogram

Intensity histogram mô tả distribution của pixel value.

Histogram equalization phân phối lại intensity để tăng contrast. CLAHE thực hiện contrast enhancement cục bộ, giảm vấn đề global histogram khi illumination thay đổi theo vùng.

Tuy nhiên contrast enhancement cũng có thể làm noise nổi rõ hơn.

## Geometric Transformation

Affine transform:

\[
\begin{bmatrix}x'\\y'\end{bmatrix}=A\begin{bmatrix}x\\y\end{bmatrix}+b
\]

bao gồm translation, rotation, scale và shear.

Khi perspective change cần projective transformation hoặc homography để map planar structure giữa hai viewpoint.

## Interpolation

Resize hoặc warp yêu cầu estimate pixel tại non-integer coordinate. Các cách phổ biến:

- nearest neighbor;
- bilinear;
- bicubic.

Nearest neighbor thường phù hợp với segmentation mask vì giữ nguyên discrete label. Bilinear hoặc bicubic phù hợp hơn với natural image vì tạo chuyển tiếp mượt.

Dùng bilinear cho class mask có thể tạo ra class ID không tồn tại.

## Frequency Domain

2D Fourier Transform phân rã image thành các spatial frequency.

Convolution trong spatial domain tương ứng phép nhân trong frequency domain.

- low-pass filter → làm mượt;
- high-pass filter → nhấn mạnh edge và chi tiết.

Góc nhìn frequency giúp hiểu blur, periodic noise, aliasing và compression.

## Trực giác JPEG

JPEG thường:

```text
chia image thành block
→ DCT
→ quantize frequency coefficient
→ entropy coding
```

Phần loss lớn đến từ quantization. High-frequency detail thường bị loại mạnh hơn low-frequency structure.

Nếu compression distribution của train và deployment khác nhau, model có thể gặp domain shift.

## Ví dụ Classical Pipeline

Document scan có thể đi qua:

```text
grayscale
→ denoise
→ deskew
→ adaptive threshold
→ morphology
→ connected component
→ OCR
```

Deep model có thể thay một số stage, nhưng preprocessing vẫn rất hữu ích khi acquisition pipeline có cấu trúc ổn định.

## Khi Classical Image Processing vẫn phù hợp

- industrial inspection có rule rõ;
- compute budget rất nhỏ;
- geometry đơn giản và deterministic;
- pre/post-processing quanh neural model;
- cleanup segmentation mask;
- document normalization.

Không phải mọi vision problem đều cần deep network.

## Differentiable Image Operation

Nhiều image-processing operation có phiên bản differentiable và có thể trở thành layer hoặc augmentation trong neural training.

Điều này cho thấy ranh giới giữa classical processing và learned model không hoàn toàn cứng.

## Mô hình tư duy

> **Image processing biến đổi measurement để structure cần thiết dễ phát hiện hơn. Deep Learning chủ yếu thay hand-designed feature extraction bằng learned representation, nhưng không xóa nền tảng signal processing.**

## Những nhầm lẫn thường gặp

### “Deep Learning làm Image Processing lỗi thời”

Không. Resize, normalization, augmentation, filtering và geometric transform vẫn tồn tại trong hầu hết pipeline.

### “Sharpen làm xuất hiện information mới”

Không. Sharpen tăng local contrast; nó không tái tạo detail thật đã mất khỏi measurement.

### “Thresholding và deep segmentation là cùng một thứ”

Chúng có thể cùng output mask nhưng assumption, representation và capability rất khác nhau.

## Liên kết kiến thức

Convolution và filtering là cầu trực tiếp tới CNN; gradient và frequency nối Computer Vision với Calculus và Signal Processing.

Xem tiếp: [Feature Representation](./02_feature_representation.md).