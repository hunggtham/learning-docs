# Images as dữ liệu (data / 데이터)

> **Mạch đọc:** Đặt **Images as dữ liệu (data / 데이터)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Từ scene thật tới pixels** sang **Coordinate hệ thống (system / 시스템)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Computer Vision bắt đầu từ một fact đơn giản: máy không “nhìn thấy vật thể” như con người; nó nhận **numbers arranged on a grid**. Một ảnh RGB thường được biểu diễn thành tensor:

\[
X\in\mathbb{R}^{H\times W\times 3}
\]

mỗi điểm ảnh (pixel / 픽셀) chứa intensity cho Red, Green, Blue.

## Từ scene thật tới pixels

Camera chuỗi xử lý (pipeline / 파이프라인) biến photons thành electrical tín hiệu (signal / 신호), rồi sampling/quantization thành pixels. Vì vậy ảnh (image / 이미지) không phải world itself; nó là đo lường (measurement / 측정) chịu ảnh hưởng bởi:

- sensor;
- exposure;
- lens;
- white balance;
- compression;
- resolution;
- viewpoint;
- lighting.

Computer Vision phải infer ngữ nghĩa (semantic / 의미적) cấu trúc (structure / 구조) từ đo lường (measurement / 측정) không hoàn hảo.

## Coordinate hệ thống (system / 시스템)

Ảnh (image / 이미지) coordinate thường:

```text
origin: top-left
x: column → right
y: row → down
```

Bounding box có thể dùng `(x_min,y_min,x_max,y_max)` hoặc center-width-height. Format mismatch là nguồn (source / 소스) bug phổ biến.

## Channels

RGB dùng 3 channels; grayscale 1. Other modalities:

- độ sâu (depth / 깊이);
- infrared;
- multispectral;
- medical CT/MRI volumes;
- alpha transparency.

Biểu diễn (representation / 표현) phải match sensing tiến trình (process / 프로세스).

## Resolution và thông tin (information / 정보)

Resize ảnh nhỏ hơn giảm compute nhưng có thể mất tiny objects/văn bản (text / 텍스트). Resize lớn hơn không tạo thông tin (information / 정보) mới.

Điểm ảnh (pixel / 픽셀) count tăng quadratically theo spatial dimension. Doubling width/height → ~4× pixels.

## Normalization

Neural các mô hình (models / 모델들) thường transform điểm ảnh (pixel / 픽셀) integers `[0,255]` thành floats, sau đó normalize:

\[
x'=(x-\mu)/\sigma
\]

Normalization ảnh hưởng tối ưu hóa (optimization / 최적화), không thay ngữ nghĩa (semantic / 의미적) content lý tưởng.

## Color Spaces

RGB thuận tiện display/sensors nhưng không phải biểu diễn (representation / 표현) duy nhất. HSV/HSL tách hue/saturation/lightness; YCbCr tách luminance/chrominance và phổ biến trong compression/video.

Choice color không gian (space / 공간) có thể simplify classical algorithms.

## Ảnh (image / 이미지) as tín hiệu (signal / 신호)

Ảnh (image / 이미지) là 2D discrete tín hiệu (signal / 신호). Neighborhood cấu trúc (structure / 구조) có ý nghĩa: adjacent pixels thường correlated.

Điều này giải thích inductive độ lệch (bias / 편향) của convolution: cục bộ (local / 로컬) patterns và translation cấu trúc (structure / 구조).

## Spatial Frequency

Smooth regions chứa low-frequency cấu trúc (structure / 구조); edges/textures có high-frequency components. Fourier perspective giúp hiểu blur, sharpening và compression.

## Sampling và Aliasing

Nếu downsample quá mạnh mà không low-pass filter, high-frequency details fold thành artifacts — **aliasing**.

Nyquist intuition: sampling tỷ lệ (rate / 비율) phải đủ cao relative to tín hiệu (signal / 신호) frequency.

## Noise

Sensor noise, compression artifacts và motion blur làm observation khác true scene. Robust vision mô hình (model / 모델) cần dữ liệu (data / 데이터)/augmentation reflect triển khai (deployment / 배포) conditions.

## Hình học (geometry / 기하학)

Perspective projection map 3D world onto 2D ảnh (image / 이미지). Same đối tượng (object / 객체) thay đổi apparent kích thước (size / 크기)/shape theo viewpoint. Vision vì vậy phải deal invariance/equivariance.

## Annotation Types

Tasks khác nhau cần labels khác:

```text
classification → image label
object detection → boxes + classes
segmentation → pixel masks
keypoints → landmark coordinates
captioning → text
```

Label biểu diễn (representation / 표현) quyết định supervision granularity và annotation chi phí (cost / 비용).

## Dữ liệu (data / 데이터) Augmentation

Transformations như crop, flip, color jitter, rotation tạo additional samples và encode expected invariances.

Nhưng augmentation phải semantics-preserving. Horizontal flip của traffic sign/văn bản (text / 텍스트) hoặc medical laterality có thể đổi meaning.

## Train–triển khai (deployment / 배포) Gap

Vision rất sensitive lĩnh vực (domain / 도메인) shift:

- indoor vs outdoor;
- daytime vs night;
- camera mô hình (model / 모델) khác;
- country/road marking khác;
- synthetic vs real.

Chỉ số (metric / 지표) trên benchmark không tự đảm bảo triển khai (deployment / 배포) chất lượng (quality / 품질).

## Ảnh (image / 이미지) Tokens và Patches

Vision Transformer chia ảnh (image / 이미지) thành patches rồi flatten/dự án (project / 프로젝트) thành token-like vectors. Điều này nối ảnh (image / 이미지) biểu diễn (representation / 표현) với Transformer chuỗi (sequence / 시퀀스) processing.

Nếu patch kích thước (size / 크기) `P×P`, số patches roughly:

\[
N=\frac{HW}{P^2}
\]

Smaller patch → more tokens → better fine detail but higher attention chi phí (cost / 비용).

## Mô hình tư duy (mental model / 사고 모델)

> **Computer Vision là suy luận (inference / 추론) từ đo lường (measurement / 측정) pixels về hidden cấu trúc (structure / 구조) của world.**

Một điểm ảnh (pixel / 픽셀) không “là” vật thể; ngữ nghĩa (semantic / 의미적) đối tượng (object / 객체) emerges từ spatial patterns, ngữ cảnh (context / 맥락) và learned representations.

## Dùng chung (common / 공통) Misconceptions

### “Higher resolution luôn tốt hơn”

Compute/bộ nhớ (memory / 메모리) increase mạnh và noise cũng có thể tăng; tác vụ (task / 작업) determines useful resolution.

### “ảnh (image / 이미지) augmentation chỉ để tăng dataset kích thước (size / 크기)”

Nó còn encode invariance các giả định (assumptions / 가정들).

### “điểm ảnh (pixel / 픽셀) giá trị (value / 값) là mục tiêu (objective / 목표) reality”

Camera processing và lighting ảnh hưởng đo lường (measurement / 측정).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Images connect tín hiệu (signal / 신호) Processing, tuyến tính (linear / 선형) Algebra, hình học (geometry / 기하학) và Deep học tập (learning / 학습). Chapter tiếp theo giới thiệu classical image-processing operations giúp hiểu cấu trúc (structure / 구조) trước learned các mô hình (models / 모델들).

Xem tiếp: [Image Processing Foundations](./01_image_processing_foundations.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 image processing foundations](./01_image_processing_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
