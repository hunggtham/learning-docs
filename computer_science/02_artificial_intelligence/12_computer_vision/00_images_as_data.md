# Ảnh như Dữ liệu

Computer Vision bắt đầu từ một sự thật đơn giản: máy không “nhìn thấy vật thể” như con người; nó nhận **các con số được sắp xếp trên một lưới (grid)**. Một ảnh RGB thường được biểu diễn thành tensor:

\[
X\in\mathbb{R}^{H\times W\times 3}
\]

Mỗi pixel chứa cường độ (intensity) cho ba kênh Red, Green và Blue.

## Từ Scene thật tới Pixel

Camera biến photon thành tín hiệu điện, sau đó sampling và quantization tạo thành pixel. Vì vậy image không phải bản thân thế giới; nó là một phép đo (measurement) chịu ảnh hưởng của:

- sensor;
- exposure;
- lens;
- white balance;
- compression;
- resolution;
- viewpoint;
- lighting.

Computer Vision phải suy ra semantic structure từ một measurement không hoàn hảo.

## Hệ tọa độ

Image coordinate thường dùng:

```text
gốc tọa độ: góc trên bên trái
x: cột → tăng sang phải
y: hàng → tăng xuống dưới
```

Bounding box có thể dùng `(x_min,y_min,x_max,y_max)` hoặc `(center_x, center_y, width, height)`. Format mismatch là nguồn bug rất phổ biến trong vision pipeline.

## Channel

RGB có ba channel; grayscale thường có một channel. Các modality khác có thể gồm:

- depth;
- infrared;
- multispectral;
- medical CT/MRI volume;
- alpha transparency.

Representation phải phù hợp với sensing process tạo ra dữ liệu.

## Resolution và Information

Resize ảnh nhỏ hơn giúp giảm compute nhưng có thể làm mất vật thể nhỏ, ký tự hoặc edge detail.

Resize ảnh lớn hơn không tự tạo thêm information mới; nó chỉ nội suy từ pixel hiện có.

Số pixel tăng theo bình phương spatial dimension. Nếu tăng gấp đôi cả width và height, số pixel tăng khoảng bốn lần.

## Normalization

Neural model thường chuyển pixel integer `[0,255]` thành float, sau đó normalize:

\[
x'=(x-\mu)/\sigma
\]

Normalization giúp optimization ổn định hơn và đưa scale đầu vào về distribution phù hợp với model training. Nó không tự làm thay đổi semantic content lý tưởng của image.

## Color Space

RGB thuận tiện cho display và nhiều sensor, nhưng không phải representation duy nhất.

- HSV/HSL tách hue, saturation và lightness;
- YCbCr tách luminance và chrominance, phổ biến trong compression/video.

Chọn color space phù hợp có thể làm một số classical image-processing algorithm đơn giản hơn.

## Image như một Signal

Image có thể xem là một **tín hiệu rời rạc hai chiều (2D discrete signal)**. Neighborhood structure có ý nghĩa: pixel gần nhau thường có correlation cao hơn pixel ở xa.

Đây là một lý do quan trọng tạo nên inductive bias của convolution: local pattern và translation structure được tận dụng trực tiếp.

## Spatial Frequency

Vùng mượt chủ yếu chứa low-frequency structure; edge, texture và chi tiết nhỏ chứa nhiều high-frequency component.

Góc nhìn Fourier giúp hiểu blur, sharpening, denoising và compression.

## Sampling và Aliasing

Nếu downsample quá mạnh mà không low-pass filter trước, high-frequency detail có thể bị “gập” thành pattern giả — hiện tượng **aliasing**.

Trực giác từ Nyquist: sampling rate cần đủ cao so với frequency của signal muốn giữ lại.

## Noise

Sensor noise, compression artifact, motion blur hoặc low-light noise làm observation khác với scene thật.

Vision model đáng tin cần training data và augmentation phản ánh điều kiện deployment thực tế, thay vì chỉ ảnh benchmark sạch.

## Geometry

Perspective projection chiếu world 3D lên image 2D. Cùng một object có apparent size và shape khác nhau khi viewpoint thay đổi.

Computer Vision vì vậy phải học hoặc xây được các dạng **invariance** và **equivariance** phù hợp với geometry của task.

## Kiểu Annotation

Các task khác nhau cần loại label khác nhau:

```text
classification → image label
object detection → box + class
segmentation → pixel mask
keypoint detection → landmark coordinate
captioning → text
```

Label representation quyết định mức chi tiết supervision và annotation cost.

## Data Augmentation

Các transformation như crop, flip, color jitter hoặc rotation tạo sample bổ sung và encode assumption về invariance mong muốn.

Tuy nhiên augmentation phải giữ nguyên semantics. Horizontal flip có thể làm đổi ý nghĩa của traffic sign, text hoặc medical laterality.

## Train–Deployment Gap

Vision đặc biệt nhạy với domain shift, ví dụ:

- indoor so với outdoor;
- ban ngày so với ban đêm;
- camera model khác;
- road marking khác quốc gia;
- synthetic data so với real data.

Metric cao trên benchmark không tự bảo đảm chất lượng deployment.

## Image Token và Patch

Vision Transformer chia image thành các patch rồi flatten và project mỗi patch thành vector giống token.

Nếu patch size là `P×P`, số patch xấp xỉ:

\[
N=\frac{HW}{P^2}
\]

Patch nhỏ hơn giữ chi tiết tốt hơn nhưng tạo nhiều token hơn, làm attention cost tăng.

## Mô hình tư duy

> **Computer Vision là quá trình suy luận từ measurement dạng pixel về hidden structure của thế giới.**

Một pixel không “là” vật thể. Semantic object xuất hiện từ spatial pattern, context và learned representation.

## Những nhầm lẫn thường gặp

### “Resolution cao hơn luôn tốt hơn”

Không. Compute và memory tăng nhanh, trong khi noise cũng có thể tăng. Resolution hữu ích phụ thuộc task.

### “Image augmentation chỉ để tăng số lượng dữ liệu”

Không. Nó còn encode invariance assumption mà ta muốn model học.

### “Pixel value là sự thật tuyệt đối”

Không. Camera processing, lighting và sensor đều ảnh hưởng measurement.

## Liên kết kiến thức

Image representation nối Signal Processing, Linear Algebra, Geometry và Deep Learning. Chapter tiếp theo giới thiệu classical image-processing operation để hiểu cấu trúc ảnh trước khi đi sâu vào learned model.

Xem tiếp: [Nền tảng Image Processing](./01_image_processing_foundations.md).