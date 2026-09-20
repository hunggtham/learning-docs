# Images, color, rasterization và rendering

Một digital image không phải “màu thật được lưu lại”; nó là sampled/quantized representation của light/color under a color model. Hiểu sampling, color space, alpha và compression giúp giải thích image artifacts, UI rendering và media pipelines.

## Pixel là sample, không phải ô vuông vật lý tuyệt đối

Pixel thường được visualize như square, nhưng mathematically tốt hơn coi nó là sample location/area contribution trên image grid. Rendering reconstructs continuous-looking image từ discrete samples.

Resolution tăng sample density nhưng không tự tạo detail nếu source/optics không có information.

## Sampling và aliasing

Nếu signal có frequencies cao hơn sampling rate có thể capture, chúng fold thành artifacts—aliasing. Jagged edges trong graphics là spatial aliasing.

Anti-aliasing prefilter/multisampling để estimate coverage và giảm high-frequency artifacts.

Connection với Nyquist sampling theorem cho thấy graphics là signal processing theo không gian.

## RGB và additive color

Displays thường dùng RGB primaries theo additive light model. Nhưng numeric RGB values chỉ có meaning đầy đủ cùng color space/transfer function như sRGB, Display-P3.

`(255,0,0)` không phải universal physical red độc lập device/profile.

## Linear light và gamma

sRGB encoded values gần nonlinear để phù hợp perceptual/storage behavior. Lighting/blending calculations nên thường thực hiện trong linear-light space.

Average hai encoded RGB values trực tiếp có thể cho brightness sai.

Đây là ví dụ representation thuận tiện cho storage/display không luôn là representation đúng cho computation.

## Alpha compositing

Alpha biểu diễn coverage/opacity. Compositing source over destination có form linear trong premultiplied representation.

Straight alpha và premultiplied alpha có trade-offs; premultiplied thường tránh fringe artifacts và làm compositing algebra sạch hơn.

Alpha không đơn giản là “transparency percentage” nếu color space và pre-multiplication bị trộn sai.

## Texture mapping

Texture coordinates map surface geometry sang image. Sampling texture khi minify/magnify cần filtering.

Nearest neighbor sharp/blocky; bilinear interpolate nearby texels; mipmaps precompute lower-resolution levels để minification giảm aliasing/bandwidth.

Anisotropic filtering xử lý footprints elongated do viewing angle.

## Lighting models

Local shading model tách ambient/diffuse/specular approximations. Physically Based Rendering (PBR) dùng materials/light models gần physical energy behavior hơn, như microfacet BRDF.

Rendering equation mô tả outgoing radiance tích hợp incoming light từ hemisphere, nhưng exact solution thường quá đắt nên real-time/path tracing dùng approximations/sampling.

## Raster vs ray tracing

Rasterization project geometry rồi determine covered pixels, rất efficient real-time. Ray tracing bắn rays từ camera và follow intersections/reflections, tự nhiên hơn cho shadows/reflections/global effects nhưng compute-intensive.

Modern rendering kết hợp raster + ray tracing techniques.

## Image compression

Lossless formats preserve exact decoded pixels; lossy compression bỏ information ít perceptually important để giảm size.

JPEG dùng transform/quantization phù hợp photographs nhưng artifacts ở text/edges; PNG lossless phù hợp UI/graphics với sharp boundaries; modern codecs có trade-offs khác.

## Common Misconceptions

**“Ảnh 4K luôn đẹp hơn 1080p.”** Source detail, display size/distance, compression và optics đều matter.

**“RGB values là màu tuyệt đối.”** Cần color space/profile và display response.

**“Transparency chỉ là alpha.”** Correct compositing còn phụ thuộc premultiplication, order và color space.

## Mental Model

> Digital imaging là sampling + representation + reconstruction. Mỗi artifact thường truy ngược được tới sampling rate, color encoding, filtering hoặc compositing assumption.

## Kết nối

Đọc [graphics pipeline](./02_computer_graphics_pipeline_and_geometry.md), [information encoding](../00_computation_information/01_information_bits_and_encoding.md) và [Fourier/signals](../../mathematics/09_connections/05_fourier_signals_and_frequency.md).