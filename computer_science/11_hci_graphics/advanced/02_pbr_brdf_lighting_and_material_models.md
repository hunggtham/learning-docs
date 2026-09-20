# PBR, BRDF, lighting integration và material models

Real-time rendering muốn surface phản ứng với ánh sáng nhất quán dưới nhiều environments. **Physically Based Rendering (PBR)** không có nghĩa mô phỏng vật lý hoàn hảo; nó dùng material/light models có constraints vật lý đủ tốt để artist parameters behave predictably.

## Rendering equation

Outgoing radiance tại một điểm phụ thuộc emitted light và integral của incoming light từ mọi directions, weighted bởi material response. Full integral đắt, nên real-time renderer dùng approximations, sampling và precomputation.

Điểm quan trọng là pixel color không chỉ là “màu vật thể”; nó là kết quả interaction giữa geometry, material, light và camera/exposure.

## BRDF

**Bidirectional Reflectance Distribution Function (BRDF)** mô tả ánh sáng từ incoming direction được phản xạ về outgoing direction như thế nào.

BRDF vật lý hợp lý thường tôn trọng energy conservation và reciprocity trong model phù hợp: surface không tự phản xạ nhiều năng lượng hơn nhận được.

## Diffuse và specular

Diffuse component mô tả light tán xạ rộng; specular tạo highlight phụ thuộc view/light direction. Microfacet model coi surface gồm nhiều microfacets với distribution normals.

Roughness điều khiển distribution: surface rough làm highlight rộng/mờ; smooth làm highlight sắc.

## Metallic workflow

Metal và dielectric phản ứng khác nhau. Dielectric thường có diffuse component và specular reflection tương đối nhỏ; conductor/metal hấp thụ/transmit khác và specular color liên quan material.

PBR texture sets như base color, metallic, roughness, normal không phải arbitrary filters; chúng parameterize material model.

## Normal mapping

Normal map thay shading normal mà không thêm geometry thực. Nó tạo illusion chi tiết ánh sáng nhưng silhouette/parallax vẫn không đổi.

Tangent-space transformation phải đúng; sai handedness/normal convention tạo lighting artifact khó hiểu.

## Image-based lighting

Environment map cung cấp incoming light từ nhiều directions. Prefiltering environment cho roughness levels và precomputed BRDF terms giúp approximate integral nhanh ở runtime.

Đây là ví dụ đổi computation runtime lấy preprocessing/storage.

## Tone mapping

Lighting computation có thể tạo HDR values vượt display range. Tone mapping ánh xạ dynamic range sang output display trong khi cố giữ perceptual relationships.

Nếu debug material sau tone mapping/exposure, cần nhớ visual result đã qua color pipeline; linear-space value và displayed pixel không đồng nhất.

## Mental Model

> PBR là contract giữa material parameters và light transport approximation. Material không “có màu” độc lập; nó biến incoming radiance thành outgoing radiance theo model, rồi camera/color pipeline biến radiance thành pixel nhìn thấy.