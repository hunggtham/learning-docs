# Images as Data

Computer Vision bắt đầu từ một fact đơn giản: máy không “nhìn thấy vật thể” như con người; nó nhận **numbers arranged on a grid**. Một ảnh RGB thường được biểu diễn thành tensor:

\[
X\in\mathbb{R}^{H\times W\times 3}
\]

mỗi pixel chứa intensity cho Red, Green, Blue.

## Từ scene thật tới pixels

Camera pipeline biến photons thành electrical signal, rồi sampling/quantization thành pixels. Vì vậy image không phải world itself; nó là measurement chịu ảnh hưởng bởi:

- sensor;
- exposure;
- lens;
- white balance;
- compression;
- resolution;
- viewpoint;
- lighting.

Computer Vision phải infer semantic structure từ measurement không hoàn hảo.

## Coordinate System

Image coordinate thường:

```text
origin: top-left
x: column → right
y: row → down
```

Bounding box có thể dùng `(x_min,y_min,x_max,y_max)` hoặc center-width-height. Format mismatch là source bug phổ biến.

## Channels

RGB dùng 3 channels; grayscale 1. Other modalities:

- depth;
- infrared;
- multispectral;
- medical CT/MRI volumes;
- alpha transparency.

Representation phải match sensing process.

## Resolution và Information

Resize ảnh nhỏ hơn giảm compute nhưng có thể mất tiny objects/text. Resize lớn hơn không tạo information mới.

Pixel count tăng quadratically theo spatial dimension. Doubling width/height → ~4× pixels.

## Normalization

Neural models thường transform pixel integers `[0,255]` thành floats, sau đó normalize:

\[
x'=(x-\mu)/\sigma
\]

Normalization ảnh hưởng optimization, không thay semantic content lý tưởng.

## Color Spaces

RGB thuận tiện display/sensors nhưng không phải representation duy nhất. HSV/HSL tách hue/saturation/lightness; YCbCr tách luminance/chrominance và phổ biến trong compression/video.

Choice color space có thể simplify classical algorithms.

## Image as Signal

Image là 2D discrete signal. Neighborhood structure có ý nghĩa: adjacent pixels thường correlated.

Điều này giải thích inductive bias của convolution: local patterns và translation structure.

## Spatial Frequency

Smooth regions chứa low-frequency structure; edges/textures có high-frequency components. Fourier perspective giúp hiểu blur, sharpening và compression.

## Sampling và Aliasing

Nếu downsample quá mạnh mà không low-pass filter, high-frequency details fold thành artifacts — **aliasing**.

Nyquist intuition: sampling rate phải đủ cao relative to signal frequency.

## Noise

Sensor noise, compression artifacts và motion blur làm observation khác true scene. Robust vision model cần data/augmentation reflect deployment conditions.

## Geometry

Perspective projection map 3D world onto 2D image. Same object thay đổi apparent size/shape theo viewpoint. Vision vì vậy phải deal invariance/equivariance.

## Annotation Types

Tasks khác nhau cần labels khác:

```text
classification → image label
object detection → boxes + classes
segmentation → pixel masks
keypoints → landmark coordinates
captioning → text
```

Label representation quyết định supervision granularity và annotation cost.

## Data Augmentation

Transformations như crop, flip, color jitter, rotation tạo additional samples và encode expected invariances.

Nhưng augmentation phải semantics-preserving. Horizontal flip của traffic sign/text hoặc medical laterality có thể đổi meaning.

## Train–Deployment Gap

Vision rất sensitive domain shift:

- indoor vs outdoor;
- daytime vs night;
- camera model khác;
- country/road marking khác;
- synthetic vs real.

Metric trên benchmark không tự đảm bảo deployment quality.

## Image Tokens và Patches

Vision Transformer chia image thành patches rồi flatten/project thành token-like vectors. Điều này nối image representation với Transformer sequence processing.

Nếu patch size `P×P`, số patches roughly:

\[
N=\frac{HW}{P^2}
\]

Smaller patch → more tokens → better fine detail but higher attention cost.

## Mental Model

> **Computer Vision là inference từ measurement pixels về hidden structure của world.**

Một pixel không “là” vật thể; semantic object emerges từ spatial patterns, context và learned representations.

## Common Misconceptions

### “Higher resolution luôn tốt hơn”

Compute/memory increase mạnh và noise cũng có thể tăng; task determines useful resolution.

### “Image augmentation chỉ để tăng dataset size”

Nó còn encode invariance assumptions.

### “Pixel value là objective reality”

Camera processing và lighting ảnh hưởng measurement.

## Knowledge Connection

Images connect Signal Processing, Linear Algebra, Geometry và Deep Learning. Chapter tiếp theo giới thiệu classical image-processing operations giúp hiểu structure trước learned models.

Xem tiếp: [Image Processing Foundations](./01_image_processing_foundations.md).