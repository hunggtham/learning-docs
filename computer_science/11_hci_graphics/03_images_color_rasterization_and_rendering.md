# Images, color, rasterization và rendering

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Images, color, rasterization và rendering**. Route đi từ pixel/sampling → aliasing/color spaces → linear light/alpha → textures/lighting → raster-vs-ray tracing/compression, để ảnh hiển thị được giải thích bằng tín hiệu và pipeline.

Một digital ảnh (image / 이미지) không phải “màu thật được lưu lại”; nó là sampled/quantized biểu diễn (representation / 표현) của light/color under a color mô hình (model / 모델). Hiểu sampling, color không gian (space / 공간), alpha và compression giúp giải thích ảnh (image / 이미지) artifacts, UI rendering và media pipelines.

## Điểm ảnh (pixel / 픽셀) là mẫu (sample / 표본), không phải ô vuông vật lý tuyệt đối

Điểm ảnh (pixel / 픽셀) thường được visualize như square, nhưng mathematically tốt hơn coi nó là mẫu (sample / 표본) location/area contribution trên ảnh (image / 이미지) grid. Rendering reconstructs continuous-looking ảnh (image / 이미지) từ discrete samples.

Resolution tăng mẫu (sample / 표본) density nhưng không tự tạo detail nếu nguồn (source / 소스)/optics không có thông tin (information / 정보).

Pixel là kết quả của sampling, nên aliasing là vấn đề tín hiệu trước khi trở thành vấn đề màu. Sau khi kiểm soát sampling, ta mới có thể diễn giải các kênh RGB.

## Sampling và aliasing

Nếu tín hiệu (signal / 신호) có frequencies cao hơn sampling tỷ lệ (rate / 비율) có thể capture, chúng fold thành artifacts—aliasing. Jagged edges trong graphics là spatial aliasing.

Anti-aliasing prefilter/multisampling để estimate coverage và giảm high-frequency artifacts.

Liên kết (connection / 연결) với Nyquist sampling theorem cho thấy graphics là tín hiệu (signal / 신호) processing theo không gian.

Sampling quyết định ta lấy bao nhiêu thông tin; RGB quyết định biểu diễn thông tin đó. Nhưng RGB chỉ có nghĩa trong một color space và transfer function, dẫn tới phân biệt linear light với gamma.

## RGB và additive color

Displays thường dùng RGB primaries theo additive light mô hình (model / 모델). Nhưng numeric RGB values chỉ có meaning đầy đủ cùng color không gian (space / 공간)/transfer hàm (function / 함수) như sRGB, Display-P3.

`(255,0,0)` không phải universal vật lý (physical / 물리적) red độc lập thiết bị (device / 장치)/profile.

RGB encoded values thuận tiện cho lưu trữ, nhưng phép tính ánh sáng cần linear values. Khi đã tách hai miền, alpha compositing mới giữ được ý nghĩa coverage và màu.

## Tuyến tính (linear / 선형) light và gamma

sRGB encoded values gần nonlinear để phù hợp perceptual/lưu trữ (storage / 저장소) hành vi (behavior / 동작). Lighting/blending calculations nên thường thực hiện trong linear-light không gian (space / 공간).

Average hai encoded RGB values trực tiếp có thể cho brightness sai.

Đây là ví dụ biểu diễn (representation / 표현) thuận tiện cho lưu trữ (storage / 저장소)/display không luôn là biểu diễn (representation / 표현) đúng cho computation.

Compositing đúng phụ thuộc cả color space lẫn cách lưu alpha. Sau khi các lớp được trộn, texture mapping quyết định cách dữ liệu ảnh được lấy lại trên bề mặt hình học.

## Alpha compositing

Alpha biểu diễn coverage/opacity. Compositing nguồn (source / 소스) over destination có form tuyến tính (linear / 선형) trong premultiplied biểu diễn (representation / 표현).

Straight alpha và premultiplied alpha có trade-offs; premultiplied thường tránh fringe artifacts và làm compositing algebra sạch hơn.

Alpha không đơn giản là “transparency percentage” nếu color không gian (space / 공간) và pre-multiplication bị trộn sai.

Texture sampling giải quyết việc lấy ảnh ở các footprint khác nhau; lighting tiếp tục quyết định ảnh hưởng của ánh sáng lên bề mặt sau khi texture đã cung cấp tham số material.

## Texture ánh xạ (mapping / 매핑)

Texture coordinates map surface hình học (geometry / 기하학) sang ảnh (image / 이미지). Sampling texture khi minify/magnify cần filtering.

Nearest neighbor sharp/blocky; bilinear interpolate nearby texels; mipmaps precompute lower-resolution levels để minification giảm aliasing/bandwidth.

Anisotropic filtering xử lý footprints elongated do viewing angle.

Lighting model xác định cách material phản ứng với incoming light; rasterization và ray tracing là hai chiến lược khác nhau để tìm các tương tác cần tính.

## Lighting các mô hình (models / 모델들)

Cục bộ (local / 로컬) shading mô hình (model / 모델) tách ambient/diffuse/specular approximations. Physically Based Rendering (PBR) dùng materials/light các mô hình (models / 모델들) gần vật lý (physical / 물리적) năng lượng (energy / 에너지) hành vi (behavior / 동작) hơn, như microfacet BRDF.

Rendering equation mô tả outgoing radiance tích hợp incoming light từ hemisphere, nhưng chính xác (exact / 정확한) solution thường quá đắt nên real-time/đường dẫn (path / 경로) tracing dùng approximations/sampling.

Raster và ray tracing đổi chi phí tính toán lấy các loại hiệu ứng khác nhau. Ảnh kết quả vẫn là dữ liệu cần lưu trữ hoặc truyền đi, nên compression trở thành bước tiếp theo.

## Raster vs ray tracing

Rasterization dự án (project / 프로젝트) hình học (geometry / 기하학) rồi determine covered pixels, rất efficient real-time. Ray tracing bắn rays từ camera và follow intersections/reflections, tự nhiên hơn cho shadows/reflections/toàn cục (global / 전역) effects nhưng compute-intensive.

Hiện đại (modern / 현대적) rendering kết hợp raster + ray tracing techniques.

Compression giữ hoặc bỏ thông tin theo mục tiêu fidelity và kích thước. Các ngộ nhận sau đây nhắc rằng chất lượng cảm nhận không chỉ do số pixel hay tên codec quyết định.

## Ảnh (image / 이미지) compression

Lossless formats preserve chính xác (exact / 정확한) decoded pixels; lossy compression bỏ thông tin (information / 정보) ít perceptually important để giảm kích thước (size / 크기).

JPEG dùng transform/quantization phù hợp photographs nhưng artifacts ở văn bản (text / 텍스트)/edges; PNG lossless phù hợp UI/graphics với sharp boundaries; hiện đại (modern / 현대적) codecs có trade-offs khác.

Sampling, encoding, filtering và compositing là các điểm có thể tạo artifact. Vì vậy cần truy ngược artifact về đúng giả định thay vì chỉ tăng resolution.

## Dùng chung (common / 공통) Misconceptions

**“Ảnh 4K luôn đẹp hơn 1080p.”** nguồn (source / 소스) detail, display kích thước (size / 크기)/distance, compression và optics đều matter.

**“RGB values là màu tuyệt đối.”** Cần color không gian (space / 공간)/profile và display phản hồi (response / 응답).

**“Transparency chỉ là alpha.”** Correct compositing còn phụ thuộc premultiplication, thứ tự (order / 순서) và color không gian (space / 공간).

## Mô hình tư duy (mental model / 사고 모델)

> Digital imaging là sampling + biểu diễn (representation / 표현) + reconstruction. Mỗi sản phẩm tạo ra (artifact / 산출물) thường truy ngược được tới sampling tỷ lệ (rate / 비율), color encoding, filtering hoặc compositing giả định (assumption / 가정).

## Kết nối

Đọc [graphics pipeline](./02_computer_graphics_pipeline_and_geometry.md), [information encoding](../00_computation_information/01_information_bits_and_encoding.md) và [Fourier/signals](../../mathematics/09_connections/05_fourier_signals_and_frequency.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
