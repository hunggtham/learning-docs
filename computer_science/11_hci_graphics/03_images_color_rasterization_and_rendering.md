# Images, color, rasterization và rendering

> **Mạch đọc:** Đặt **Images, color, rasterization và rendering** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **điểm ảnh (pixel / 픽셀) là mẫu (sample / 표본), không phải ô vuông vật lý tuyệt đối** sang **Sampling và aliasing**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một digital ảnh (image / 이미지) không phải “màu thật được lưu lại”; nó là sampled/quantized biểu diễn (representation / 표현) của light/color under a color mô hình (model / 모델). Hiểu sampling, color không gian (space / 공간), alpha và compression giúp giải thích ảnh (image / 이미지) artifacts, UI rendering và media pipelines.

## Điểm ảnh (pixel / 픽셀) là mẫu (sample / 표본), không phải ô vuông vật lý tuyệt đối

Điểm ảnh (pixel / 픽셀) thường được visualize như square, nhưng mathematically tốt hơn coi nó là mẫu (sample / 표본) location/area contribution trên ảnh (image / 이미지) grid. Rendering reconstructs continuous-looking ảnh (image / 이미지) từ discrete samples.

Resolution tăng mẫu (sample / 표본) density nhưng không tự tạo detail nếu nguồn (source / 소스)/optics không có thông tin (information / 정보).


> **Chuyển mạch:** Từ **điểm ảnh (pixel / 픽셀) là mẫu (sample / 표본), không phải ô vuông vật lý tuyệt đối**, ta sang **Sampling và aliasing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sampling và aliasing

Nếu tín hiệu (signal / 신호) có frequencies cao hơn sampling tỷ lệ (rate / 비율) có thể capture, chúng fold thành artifacts—aliasing. Jagged edges trong graphics là spatial aliasing.

Anti-aliasing prefilter/multisampling để estimate coverage và giảm high-frequency artifacts.

Liên kết (connection / 연결) với Nyquist sampling theorem cho thấy graphics là tín hiệu (signal / 신호) processing theo không gian.


> **Chuyển mạch:** Từ **Sampling và aliasing**, ta sang **RGB và additive color** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## RGB và additive color

Displays thường dùng RGB primaries theo additive light mô hình (model / 모델). Nhưng numeric RGB values chỉ có meaning đầy đủ cùng color không gian (space / 공간)/transfer hàm (function / 함수) như sRGB, Display-P3.

`(255,0,0)` không phải universal vật lý (physical / 물리적) red độc lập thiết bị (device / 장치)/profile.


> **Chuyển mạch:** Từ **RGB và additive color**, ta sang **tuyến tính (linear / 선형) light và gamma** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tuyến tính (linear / 선형) light và gamma

sRGB encoded values gần nonlinear để phù hợp perceptual/lưu trữ (storage / 저장소) hành vi (behavior / 동작). Lighting/blending calculations nên thường thực hiện trong linear-light không gian (space / 공간).

Average hai encoded RGB values trực tiếp có thể cho brightness sai.

Đây là ví dụ biểu diễn (representation / 표현) thuận tiện cho lưu trữ (storage / 저장소)/display không luôn là biểu diễn (representation / 표현) đúng cho computation.


> **Chuyển mạch:** Từ **tuyến tính (linear / 선형) light và gamma**, ta sang **Alpha compositing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Alpha compositing

Alpha biểu diễn coverage/opacity. Compositing nguồn (source / 소스) over destination có form tuyến tính (linear / 선형) trong premultiplied biểu diễn (representation / 표현).

Straight alpha và premultiplied alpha có trade-offs; premultiplied thường tránh fringe artifacts và làm compositing algebra sạch hơn.

Alpha không đơn giản là “transparency percentage” nếu color không gian (space / 공간) và pre-multiplication bị trộn sai.


> **Chuyển mạch:** Từ **Alpha compositing**, ta sang **Texture ánh xạ (mapping / 매핑)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Texture ánh xạ (mapping / 매핑)

Texture coordinates map surface hình học (geometry / 기하학) sang ảnh (image / 이미지). Sampling texture khi minify/magnify cần filtering.

Nearest neighbor sharp/blocky; bilinear interpolate nearby texels; mipmaps precompute lower-resolution levels để minification giảm aliasing/bandwidth.

Anisotropic filtering xử lý footprints elongated do viewing angle.


> **Chuyển mạch:** Từ **Texture ánh xạ (mapping / 매핑)**, ta sang **Lighting các mô hình (models / 모델들)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Lighting các mô hình (models / 모델들)

Cục bộ (local / 로컬) shading mô hình (model / 모델) tách ambient/diffuse/specular approximations. Physically Based Rendering (PBR) dùng materials/light các mô hình (models / 모델들) gần vật lý (physical / 물리적) năng lượng (energy / 에너지) hành vi (behavior / 동작) hơn, như microfacet BRDF.

Rendering equation mô tả outgoing radiance tích hợp incoming light từ hemisphere, nhưng chính xác (exact / 정확한) solution thường quá đắt nên real-time/đường dẫn (path / 경로) tracing dùng approximations/sampling.


> **Chuyển mạch:** Từ **Lighting các mô hình (models / 모델들)**, ta sang **Raster vs ray tracing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Raster vs ray tracing

Rasterization dự án (project / 프로젝트) hình học (geometry / 기하학) rồi determine covered pixels, rất efficient real-time. Ray tracing bắn rays từ camera và follow intersections/reflections, tự nhiên hơn cho shadows/reflections/toàn cục (global / 전역) effects nhưng compute-intensive.

Hiện đại (modern / 현대적) rendering kết hợp raster + ray tracing techniques.


> **Chuyển mạch:** Từ **Raster vs ray tracing**, ta sang **ảnh (image / 이미지) compression** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ảnh (image / 이미지) compression

Lossless formats preserve chính xác (exact / 정확한) decoded pixels; lossy compression bỏ thông tin (information / 정보) ít perceptually important để giảm kích thước (size / 크기).

JPEG dùng transform/quantization phù hợp photographs nhưng artifacts ở văn bản (text / 텍스트)/edges; PNG lossless phù hợp UI/graphics với sharp boundaries; hiện đại (modern / 현대적) codecs có trade-offs khác.


> **Chuyển mạch:** Từ **ảnh (image / 이미지) compression**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Ảnh 4K luôn đẹp hơn 1080p.”** nguồn (source / 소스) detail, display kích thước (size / 크기)/distance, compression và optics đều matter.

**“RGB values là màu tuyệt đối.”** Cần color không gian (space / 공간)/profile và display phản hồi (response / 응답).

**“Transparency chỉ là alpha.”** Correct compositing còn phụ thuộc premultiplication, thứ tự (order / 순서) và color không gian (space / 공간).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Digital imaging là sampling + biểu diễn (representation / 표현) + reconstruction. Mỗi sản phẩm tạo ra (artifact / 산출물) thường truy ngược được tới sampling tỷ lệ (rate / 비율), color encoding, filtering hoặc compositing giả định (assumption / 가정).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [graphics pipeline](./02_computer_graphics_pipeline_and_geometry.md), [information encoding](../00_computation_information/01_information_bits_and_encoding.md) và [Fourier/signals](../../mathematics/09_connections/05_fourier_signals_and_frequency.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 hci human factors and interaction models](./00_hci_human_factors_and_interaction_models.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
