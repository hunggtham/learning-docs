# Image Processing Foundations

Trước Deep Learning, Computer Vision dựa nhiều vào **image processing (영상 처리 / xử lý ảnh)**: biến đổi tín hiệu ảnh để làm nổi bật structure hữu ích. Dù modern models học features tự động, các nguyên lý filtering, edges, morphology và frequency vẫn giúp hiểu data pipeline và failure modes.

## Convolution như local filtering

Với image `I` và kernel `K`, convolution/discrete correlation practical form tính weighted sum neighborhood:

\[
Y(i,j)=\sum_m\sum_n K(m,n)I(i+m,j+n)
\]

Một kernel blur trung bình:

\[
\frac{1}{9}
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

làm smooth local variation.

Edge kernel như Sobel approximates spatial derivative. CNN sau này học kernels thay vì hand-design hoàn toàn.

## Padding và Boundary

Kernel gần border thiếu neighbors. Strategies:

- zero padding;
- reflect;
- replicate;
- valid/no padding.

Boundary choice ảnh hưởng output dimension và artifacts.

## Blur và Noise Reduction

Gaussian blur:

\[
G(x,y)=\frac{1}{2\pi\sigma^2}e^{-(x^2+y^2)/(2\sigma^2)}
\]

ưu tiên center pixels và suppress high-frequency noise.

Nhưng blur cũng xóa edges/fine detail. Denoising luôn là signal-vs-detail trade-off.

## Edges và Gradients

Edge là nơi intensity thay đổi nhanh. Image gradient:

\[
\nabla I=(I_x,I_y)
\]

Magnitude:

\[
|\nabla I|=\sqrt{I_x^2+I_y^2}
\]

Direction cho orientation của local change.

Edges từng là core primitive cho object shape detection.

## Canny Edge Detection

Canny pipeline classic:

```text
Gaussian smoothing
→ gradient computation
→ non-maximum suppression
→ double threshold
→ hysteresis tracking
```

Điểm đáng học là pipeline separates noise suppression, local evidence và connectivity reasoning.

## Thresholding

Binary segmentation đơn giản:

\[
B(x,y)=1[I(x,y)>T]
\]

Global threshold fail nếu illumination nonuniform. Adaptive threshold dùng local statistics.

Otsu method chọn threshold để separate classes theo between-class variance assumption.

## Morphological Operations

Với binary mask và structuring element:

- **erosion (침식)** shrink foreground;
- **dilation (팽창)** expand foreground;
- opening = erosion then dilation;
- closing = dilation then erosion.

Dùng để remove small noise, fill holes, connect components.

## Connected Components

Binary mask có thể được group thành connected regions. Component properties như area, centroid, bounding box rất hữu ích cho OCR/inspection pipelines.

## Histograms

Intensity histogram mô tả frequency của pixel values. Histogram equalization redistribute contrast; CLAHE làm local adaptive enhancement.

Nhưng contrast enhancement có thể amplify noise.

## Geometric Transformations

Affine transform:

\[
\begin{bmatrix}x'\\y'\end{bmatrix}=A\begin{bmatrix}x\\y\end{bmatrix}+b
\]

cover translation, rotation, scale, shear.

Perspective/homography cần projective transform để map planes under viewpoint change.

## Interpolation

Resize/warp cần estimate pixel values at non-integer coordinates:

- nearest neighbor;
- bilinear;
- bicubic.

Nearest preserves labels for masks better; bilinear smoother for images. Dùng interpolation sai cho segmentation mask có thể tạo class IDs invalid.

## Frequency Domain

2D Fourier transform decompose image into spatial frequencies. Convolution in spatial domain corresponds multiplication in frequency domain.

Low-pass filters smooth; high-pass emphasize edges.

Frequency view giúp hiểu blur, periodic noise và compression.

## JPEG Intuition

JPEG chia blocks, transform qua DCT, quantize frequency coefficients rồi entropy-code. Loss chủ yếu đến từ quantization; high-frequency details bị bỏ mạnh hơn.

Compression artifacts có thể ảnh hưởng model nếu train/test compression khác nhau.

## Classical Pipeline Example

Document scan:

```text
gray
→ denoise
→ deskew
→ adaptive threshold
→ morphology
→ connected components
→ OCR
```

Một deep model có thể replace vài stage nhưng preprocessing vẫn hữu ích khi acquisition predictable.

## When Classical Processing Still Wins

- deterministic industrial inspection;
- tiny compute budget;
- obvious geometric rule;
- pre/postprocessing around neural model;
- mask cleanup;
- document normalization.

Không phải mọi vision problem cần deep network.

## Differentiable Image Operations

Nhiều processing operations có differentiable equivalents và trở thành layers/augmentations inside neural training.

## Mental Model

> **Image processing thay đổi measurement để structure cần thiết trở nên dễ detect hơn. Deep learning chủ yếu thay hand-designed feature extraction bằng learned representations, không xóa bỏ signal-processing foundations.**

## Common Misconceptions

### “Deep Learning làm image processing lỗi thời”

Không. Resize, normalization, augmentation, filtering và geometric transforms vẫn ở mọi pipeline.

### “Sharpen luôn tăng information”

Sharpen tăng local contrast; không tạo detail thật đã mất.

### “Thresholding là segmentation giống deep segmentation”

Cùng output mask nhưng assumptions/capability rất khác.

## Knowledge Connection

Convolution/filtering là bridge trực tiếp tới CNN; gradient/frequency connect Calculus và Signal Processing.

Xem tiếp: [Feature Representation](./02_feature_representation.md).