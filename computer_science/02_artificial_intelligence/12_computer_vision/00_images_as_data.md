# Images as dữ liệu (data / 데이터)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Images as dữ liệu (data / 데이터)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ scene thật tới pixels** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Coordinate hệ thống (system / 시스템)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Scene được lấy mẫu thành pixels trong một coordinate system; channels sau đó tách cường độ màu, depth hoặc modality để mô hình biết mỗi pixel mang loại tín hiệu nào.

## Coordinate hệ thống (system / 시스템)

Ảnh (image / 이미지) coordinate thường:

```text
origin: top-left
x: column → right
y: row → down
```

Bounding box có thể dùng `(x_min,y_min,x_max,y_max)` hoặc center-width-height. Format mismatch là nguồn (source / 소스) bug phổ biến.

> **Chuyển mạch:** Ở chặng này của **Images as dữ liệu (data / 데이터)**, **Channels** tiếp nhận điểm tựa từ **Coordinate hệ thống (system / 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Resolution và thông tin (information / 정보)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Channels

RGB dùng 3 channels; grayscale 1. Other modalities:

- độ sâu (depth / 깊이);
- infrared;
- multispectral;
- medical CT/MRI volumes;
- alpha transparency.

Biểu diễn (representation / 표현) phải match sensing tiến trình (process / 프로세스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Images as dữ liệu (data / 데이터)**, **Resolution và thông tin (information / 정보)** tiếp nhận điểm tựa từ **Channels** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Resolution và thông tin (information / 정보)

Resize ảnh nhỏ hơn giảm compute nhưng có thể mất tiny objects/văn bản (text / 텍스트). Resize lớn hơn không tạo thông tin (information / 정보) mới.

Điểm ảnh (pixel / 픽셀) count tăng quadratically theo spatial dimension. Doubling width/height → ~4× pixels.

> **Chuyển mạch:** Trong **Images as dữ liệu (data / 데이터)**, **Normalization** tiếp nhận điểm tựa từ **Resolution và thông tin (information / 정보)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Color Spaces** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Normalization

Neural các mô hình (models / 모델들) thường transform điểm ảnh (pixel / 픽셀) integers `[0,255]` thành floats, sau đó normalize:

\[
x'=(x-\mu)/\sigma
\]

Normalization ảnh hưởng tối ưu hóa (optimization / 최적화), không thay ngữ nghĩa (semantic / 의미적) content lý tưởng.

> **Chuyển mạch:** Ở chặng này của **Images as dữ liệu (data / 데이터)**, **Color Spaces** tiếp nhận điểm tựa từ **Normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảnh (image / 이미지) as tín hiệu (signal / 신호)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Color Spaces

RGB thuận tiện display/sensors nhưng không phải biểu diễn (representation / 표현) duy nhất. HSV/HSL tách hue/saturation/lightness; YCbCr tách luminance/chrominance và phổ biến trong compression/video.

Choice color không gian (space / 공간) có thể simplify classical algorithms.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Images as dữ liệu (data / 데이터)**, **Ảnh (image / 이미지) as tín hiệu (signal / 신호)** tiếp nhận điểm tựa từ **Color Spaces** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Spatial Frequency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảnh (image / 이미지) as tín hiệu (signal / 신호)

Ảnh (image / 이미지) là 2D discrete tín hiệu (signal / 신호). Neighborhood cấu trúc (structure / 구조) có ý nghĩa: adjacent pixels thường correlated.

Điều này giải thích inductive độ lệch (bias / 편향) của convolution: cục bộ (local / 로컬) patterns và translation cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Images as dữ liệu (data / 데이터)**, **Spatial Frequency** tiếp nhận điểm tựa từ **Ảnh (image / 이미지) as tín hiệu (signal / 신호)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sampling và Aliasing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spatial Frequency

Smooth regions chứa low-frequency cấu trúc (structure / 구조); edges/textures có high-frequency components. Fourier perspective giúp hiểu blur, sharpening và compression.

> **Chuyển mạch:** Ở chặng này của **Images as dữ liệu (data / 데이터)**, **Sampling và Aliasing** tiếp nhận điểm tựa từ **Spatial Frequency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Noise** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sampling và Aliasing

Nếu downsample quá mạnh mà không low-pass filter, high-frequency details fold thành artifacts — **aliasing**.

Nyquist intuition: sampling tỷ lệ (rate / 비율) phải đủ cao relative to tín hiệu (signal / 신호) frequency.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Images as dữ liệu (data / 데이터)**, **Noise** tiếp nhận điểm tựa từ **Sampling và Aliasing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Noise

Sensor noise, compression artifacts và motion blur làm observation khác true scene. Robust vision mô hình (model / 모델) cần dữ liệu (data / 데이터)/augmentation reflect triển khai (deployment / 배포) conditions.

> **Chuyển mạch:** Trong **Images as dữ liệu (data / 데이터)**, **Hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **Noise** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Annotation Types** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hình học (geometry / 기하학)

Perspective projection map 3D world onto 2D ảnh (image / 이미지). Same đối tượng (object / 객체) thay đổi apparent kích thước (size / 크기)/shape theo viewpoint. Vision vì vậy phải deal invariance/equivariance.

> **Chuyển mạch:** Ở chặng này của **Images as dữ liệu (data / 데이터)**, **Annotation Types** tiếp nhận điểm tựa từ **Hình học (geometry / 기하학)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Augmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Images as dữ liệu (data / 데이터)**, **Annotation Types** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Augmentation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Train–triển khai (deployment / 배포) Gap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Augmentation

Transformations như crop, flip, color jitter, rotation tạo additional samples và encode expected invariances.

Nhưng augmentation phải semantics-preserving. Horizontal flip của traffic sign/văn bản (text / 텍스트) hoặc medical laterality có thể đổi meaning.

> **Chuyển mạch:** Trong **Images as dữ liệu (data / 데이터)**, **Dữ liệu (data / 데이터) Augmentation** nêu điều cần giải thích; **Train–triển khai (deployment / 배포) Gap** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Ảnh (image / 이미지) Tokens và Patches** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Train–triển khai (deployment / 배포) Gap

Vision rất sensitive lĩnh vực (domain / 도메인) shift:

- indoor vs outdoor;
- daytime vs night;
- camera mô hình (model / 모델) khác;
- country/road marking khác;
- synthetic vs real.

Chỉ số (metric / 지표) trên benchmark không tự đảm bảo triển khai (deployment / 배포) chất lượng (quality / 품질).

> **Chuyển mạch:** Ở chặng này của **Images as dữ liệu (data / 데이터)**, **Ảnh (image / 이미지) Tokens và Patches** tiếp nhận điểm tựa từ **Train–triển khai (deployment / 배포) Gap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảnh (image / 이미지) Tokens và Patches

Vision Transformer chia ảnh (image / 이미지) thành patches rồi flatten/dự án (project / 프로젝트) thành token-like vectors. Điều này nối ảnh (image / 이미지) biểu diễn (representation / 표현) với Transformer chuỗi (sequence / 시퀀스) processing.

Nếu patch kích thước (size / 크기) `P×P`, số patches roughly:

\[
N=\frac{HW}{P^2}
\]

Smaller patch → more tokens → better fine detail but higher attention chi phí (cost / 비용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Images as dữ liệu (data / 데이터)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Ảnh (image / 이미지) Tokens và Patches** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Computer Vision là suy luận (inference / 추론) từ đo lường (measurement / 측정) pixels về hidden cấu trúc (structure / 구조) của world.**

Một điểm ảnh (pixel / 픽셀) không “là” vật thể; ngữ nghĩa (semantic / 의미적) đối tượng (object / 객체) emerges từ spatial patterns, ngữ cảnh (context / 맥락) và learned representations.

> **Chuyển mạch:** Trong **Images as dữ liệu (data / 데이터)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Higher resolution luôn tốt hơn”

Compute/bộ nhớ (memory / 메모리) increase mạnh và noise cũng có thể tăng; tác vụ (task / 작업) determines useful resolution.

### “ảnh (image / 이미지) augmentation chỉ để tăng dataset kích thước (size / 크기)”

Nó còn encode invariance các giả định (assumptions / 가정들).

### “điểm ảnh (pixel / 픽셀) giá trị (value / 값) là mục tiêu (objective / 목표) reality”

Camera processing và lighting ảnh hưởng đo lường (measurement / 측정).

> **Chuyển mạch:** Ở chặng này của **Images as dữ liệu (data / 데이터)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Images connect tín hiệu (signal / 신호) Processing, tuyến tính (linear / 선형) Algebra, hình học (geometry / 기하학) và Deep học tập (learning / 학습). Chapter tiếp theo giới thiệu classical image-processing operations giúp hiểu cấu trúc (structure / 구조) trước learned các mô hình (models / 모델들).

Xem tiếp: [Image Processing Foundations](./01_image_processing_foundations.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
