# Images as dữ liệu (data / 데이터)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Images as data**. Route đi từ scene/camera → pixels and channels → coordinate systems → sampling/quantization → visual signal limits, để ảnh được hiểu như dữ liệu đo được chứ không chỉ là bề mặt hiển thị.

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

Scene được lấy mẫu trong một hệ tọa độ cụ thể; tiếp theo, các kênh tách cường độ màu, độ sâu hoặc modality để mô hình biết mỗi pixel đang mang loại tín hiệu nào.

## Coordinate hệ thống (system / 시스템)

Ảnh (image / 이미지) coordinate thường:

```text
origin: top-left
x: column → right
y: row → down
```

Bounding box có thể dùng `(x_min,y_min,x_max,y_max)` hoặc center-width-height. Format mismatch là nguồn (source / 소스) bug phổ biến.

Sau khi cố định cách đọc tọa độ, ta chuyển sang **Channels** để hỏi mỗi pixel chứa loại tín hiệu nào. Sự lựa chọn kênh sẽ dẫn trực tiếp đến câu chuyện về **Resolution và thông tin (information / 정보)**.

## Channels

RGB dùng 3 channels; grayscale 1. Other modalities:

- độ sâu (depth / 깊이);
- infrared;
- multispectral;
- medical CT/MRI volumes;
- alpha transparency.

Biểu diễn (representation / 표현) phải match sensing tiến trình (process / 프로세스).

Channels cho biết tín hiệu được lưu như thế nào, còn **Resolution và thông tin (information / 정보)** cho biết tín hiệu đó được lấy mẫu ở mức chi tiết nào. Trước khi đưa các giá trị ấy vào mô hình, ta cần xét **Normalization**.

## Resolution và thông tin (information / 정보)

Resize ảnh nhỏ hơn giảm compute nhưng có thể mất tiny objects/văn bản (text / 텍스트). Resize lớn hơn không tạo thông tin (information / 정보) mới.

Điểm ảnh (pixel / 픽셀) count tăng quadratically theo spatial dimension. Doubling width/height → ~4× pixels.

Resolution quyết định lượng chi tiết, còn **Normalization** quyết định cách các giá trị được đưa vào quá trình tối ưu hóa. Sau đó, **Color Spaces** mở rộng câu hỏi từ thang giá trị sang loại biểu diễn màu.

## Normalization

Neural các mô hình (models / 모델들) thường transform điểm ảnh (pixel / 픽셀) integers `[0,255]` thành floats, sau đó normalize:

\[
x'=(x-\mu)/\sigma
\]

Normalization ảnh hưởng tối ưu hóa (optimization / 최적화), không thay ngữ nghĩa (semantic / 의미적) content lý tưởng.

Normalization giúp các kênh có thang đo phù hợp cho học máy; **Color Spaces** lại quyết định những đại lượng màu nào được đặt cạnh nhau. Từ lựa chọn đó, ta có thể nhìn ảnh như một **tín hiệu (signal / 신호)** hai chiều.

## Color Spaces

RGB thuận tiện display/sensors nhưng không phải biểu diễn (representation / 표현) duy nhất. HSV/HSL tách hue/saturation/lightness; YCbCr tách luminance/chrominance và phổ biến trong compression/video.

Choice color không gian (space / 공간) có thể simplify classical algorithms.

Khi ảnh được xem như tín hiệu, các pixel lân cận không còn là những con số rời rạc mà tạo thành cấu trúc. **Spatial Frequency** cho ta ngôn ngữ để mô tả cấu trúc mịn, biên và texture đó.

## Ảnh (image / 이미지) as tín hiệu (signal / 신호)

Ảnh (image / 이미지) là 2D discrete tín hiệu (signal / 신호). Neighborhood cấu trúc (structure / 구조) có ý nghĩa: adjacent pixels thường correlated.

Điều này giải thích inductive độ lệch (bias / 편향) của convolution: cục bộ (local / 로컬) patterns và translation cấu trúc (structure / 구조).

Phân tích theo tần số cho thấy chi tiết nhanh hay chậm biến đổi trong không gian. Nhưng những thành phần ấy có thể bị diễn giải sai khi lấy mẫu, nên bước tiếp theo là **Sampling và Aliasing**.

## Spatial Frequency

Smooth regions chứa low-frequency cấu trúc (structure / 구조); edges/textures có high-frequency components. Fourier perspective giúp hiểu blur, sharpening và compression.

Sampling quyết định tần số nào được giữ lại và tần số nào biến thành aliasing. Ngay cả khi lấy mẫu đúng, quan sát vẫn chịu **Noise**, vì vậy ta cần tách nhiễu khỏi tín hiệu mong muốn.

## Sampling và Aliasing

Nếu downsample quá mạnh mà không low-pass filter, high-frequency details fold thành artifacts — **aliasing**.

Nyquist intuition: sampling tỷ lệ (rate / 비율) phải đủ cao relative to tín hiệu (signal / 신호) frequency.

Aliasing là lỗi do cách lấy mẫu, còn noise là sai lệch trong chính phép quan sát. Cả hai đều nhắc rằng ảnh không phải cảnh thật; **Hình học (geometry / 기하학)** giải thích thêm cách cảnh được chiếu lên mặt phẳng ảnh.

## Noise

Sensor noise, compression artifacts và motion blur làm observation khác true scene. Robust vision mô hình (model / 모델) cần dữ liệu (data / 데이터)/augmentation reflect triển khai (deployment / 배포) conditions.

Sau khi tính đến nhiễu, ta phải tính đến biến đổi hình học do viewpoint và phép chiếu. Cách biểu diễn hình học này quyết định loại nhãn cần có trong **Annotation Types**.

## Hình học (geometry / 기하학)

Perspective projection map 3D world onto 2D ảnh (image / 이미지). Same đối tượng (object / 객체) thay đổi apparent kích thước (size / 크기)/shape theo viewpoint. Vision vì vậy phải deal invariance/equivariance.

Hình học của nhiệm vụ quyết định nhãn cần mô tả cả ảnh, hộp, mask hay keypoint. Từ loại nhãn đó, **Dữ liệu (data / 데이터) Augmentation** phải được thiết kế sao cho vẫn giữ nguyên ý nghĩa.

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

Annotation xác định điều mô hình phải học, còn augmentation tạo thêm những biến thiên được xem là hợp lệ. Sự hợp lệ đó chỉ có ý nghĩa nếu phản ánh được **Train–triển khai (deployment / 배포) Gap**.

## Dữ liệu (data / 데이터) Augmentation

Transformations như crop, flip, color jitter, rotation tạo additional samples và encode expected invariances.

Nhưng augmentation phải semantics-preserving. Horizontal flip của traffic sign/văn bản (text / 텍스트) hoặc medical laterality có thể đổi meaning.

Augmentation có thể làm dữ liệu huấn luyện gần hơn với điều kiện triển khai, nhưng không loại bỏ mọi khác biệt về domain. Một cách biểu diễn khác, **Ảnh (image / 이미지) Tokens và Patches**, sẽ đưa ảnh vào các mô hình xử lý chuỗi.

## Train–triển khai (deployment / 배포) Gap

Vision rất sensitive lĩnh vực (domain / 도메인) shift:

- indoor vs outdoor;
- daytime vs night;
- camera mô hình (model / 모델) khác;
- country/road marking khác;
- synthetic vs real.

Chỉ số (metric / 지표) trên benchmark không tự đảm bảo triển khai (deployment / 배포) chất lượng (quality / 품질).

Patch là một cách gom các phép đo cục bộ thành token; kích thước patch đồng thời quyết định chi tiết và chi phí attention. Từ các lựa chọn biểu diễn ấy, **Mô hình tư duy (mental model / 사고 모델)** giúp gom lại điều Computer Vision thực sự đang suy luận.

## Ảnh (image / 이미지) Tokens và Patches

Vision Transformer chia ảnh (image / 이미지) thành patches rồi flatten/dự án (project / 프로젝트) thành token-like vectors. Điều này nối ảnh (image / 이미지) biểu diễn (representation / 표현) với Transformer chuỗi (sequence / 시퀀스) processing.

Nếu patch kích thước (size / 크기) `P×P`, số patches roughly:

\[
N=\frac{HW}{P^2}
\]

Smaller patch → more tokens → better fine detail but higher attention chi phí (cost / 비용).

Mô hình tư duy trên nối từ phép đo, biểu diễn đến suy luận về cấu trúc ẩn. Trước khi mở sang phần kế tiếp, hãy kiểm tra các **Dùng chung (common / 공통) Misconceptions** dễ làm lệch trực giác này.

## Mô hình tư duy (mental model / 사고 모델)

> **Computer Vision là suy luận (inference / 추론) từ đo lường (measurement / 측정) pixels về hidden cấu trúc (structure / 구조) của world.**

Một điểm ảnh (pixel / 픽셀) không “là” vật thể; ngữ nghĩa (semantic / 의미적) đối tượng (object / 객체) emerges từ spatial patterns, ngữ cảnh (context / 맥락) và learned representations.

Các ngộ nhận trên đều xuất phát từ việc nhầm phép đo với thế giới hoặc nhầm biến đổi dữ liệu với thông tin mới. **Liên kết kiến thức (knowledge connection / 지식 연결)** dưới đây đặt chương này vào mạch học rộng hơn.

## Dùng chung (common / 공통) Misconceptions

### “Higher resolution luôn tốt hơn”

Compute/bộ nhớ (memory / 메모리) increase mạnh và noise cũng có thể tăng; tác vụ (task / 작업) determines useful resolution.

### “ảnh (image / 이미지) augmentation chỉ để tăng dataset kích thước (size / 크기)”

Nó còn encode invariance các giả định (assumptions / 가정들).

### “điểm ảnh (pixel / 픽셀) giá trị (value / 값) là mục tiêu (objective / 목표) reality”

Camera processing và lighting ảnh hưởng đo lường (measurement / 측정).

Sau phần ngộ nhận, các liên kết tiếp theo chỉ ra nơi đào sâu về tín hiệu, đại số tuyến tính, hình học và deep learning. Hãy giữ lại ranh giới này: ảnh là phép đo có cấu trúc, không phải bản thân thế giới.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Images connect tín hiệu (signal / 신호) Processing, tuyến tính (linear / 선형) Algebra, hình học (geometry / 기하학) và Deep học tập (learning / 학습). Chapter tiếp theo giới thiệu classical image-processing operations giúp hiểu cấu trúc (structure / 구조) trước learned các mô hình (models / 모델들).

Xem tiếp: [Image Processing Foundations](./01_image_processing_foundations.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
