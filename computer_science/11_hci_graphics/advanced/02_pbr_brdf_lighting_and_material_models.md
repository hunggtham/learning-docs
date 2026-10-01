# PBR, BRDF, lighting tích hợp (integration / 통합) và material các mô hình (models / 모델들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **PBR, BRDF, lighting tích hợp (integration / 통합) và material các mô hình (models / 모델들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Rendering equation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **BRDF** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Real-time rendering muốn surface phản ứng với ánh sáng nhất quán dưới nhiều environments. **Physically Based Rendering (PBR)** không có nghĩa mô phỏng vật lý hoàn hảo; nó dùng material/light các mô hình (models / 모델들) có các ràng buộc (constraints / 제약조건들) vật lý đủ tốt để artist parameters behave predictably.

## Rendering equation

Outgoing radiance tại một điểm phụ thuộc emitted light và integral của incoming light từ mọi directions, weighted bởi material phản hồi (response / 응답). Full integral đắt, nên real-time renderer dùng approximations, sampling và precomputation.

Điểm quan trọng là điểm ảnh (pixel / 픽셀) color không chỉ là “màu vật thể”; nó là kết quả tương tác (interaction / 상호작용) giữa hình học (geometry / 기하학), material, light và camera/exposure.

> **Chuyển mạch:** Trong **PBR, BRDF, lighting tích hợp (integration / 통합) và material các mô hình (models / 모델들)**, **BRDF** tiếp nhận điểm tựa từ **Rendering equation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Diffuse và specular** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BRDF

**Bidirectional Reflectance phân phối (distribution / 분포) hàm (function / 함수) (BRDF)** mô tả ánh sáng từ incoming direction được phản xạ về outgoing direction như thế nào.

BRDF vật lý hợp lý thường tôn trọng năng lượng (energy / 에너지) conservation và reciprocity trong mô hình (model / 모델) phù hợp: surface không tự phản xạ nhiều năng lượng hơn nhận được.

> **Chuyển mạch:** Ở chặng này của **PBR, BRDF, lighting tích hợp (integration / 통합) và material các mô hình (models / 모델들)**, **Diffuse và specular** tiếp nhận điểm tựa từ **BRDF** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Metallic workflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Diffuse và specular

Diffuse thành phần (component / 컴포넌트) mô tả light tán xạ rộng; specular tạo highlight phụ thuộc view/light direction. Microfacet mô hình (model / 모델) coi surface gồm nhiều microfacets với phân phối (distribution / 분포) normals.

Roughness điều khiển phân phối (distribution / 분포): surface rough làm highlight rộng/mờ; smooth làm highlight sắc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **PBR, BRDF, lighting tích hợp (integration / 통합) và material các mô hình (models / 모델들)**, **Diffuse và specular** xác định đầu vào; **Metallic workflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Normal ánh xạ (mapping / 매핑)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Metallic workflow

Metal và dielectric phản ứng khác nhau. Dielectric thường có diffuse thành phần (component / 컴포넌트) và specular reflection tương đối nhỏ; conductor/metal hấp thụ/transmit khác và specular color liên quan material.

PBR texture sets như cơ sở (base / 기반) color, metallic, roughness, normal không phải arbitrary filters; chúng parameterize material mô hình (model / 모델).

> **Chuyển mạch:** Trong **PBR, BRDF, lighting tích hợp (integration / 통합) và material các mô hình (models / 모델들)**, **Metallic workflow** xác định đầu vào; **Normal ánh xạ (mapping / 매핑)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Image-based lighting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Normal ánh xạ (mapping / 매핑)

Normal map thay shading normal mà không thêm hình học (geometry / 기하학) thực. Nó tạo illusion chi tiết ánh sáng nhưng silhouette/parallax vẫn không đổi.

Tangent-space transformation phải đúng; sai handedness/normal convention tạo lighting sản phẩm tạo ra (artifact / 산출물) khó hiểu.

> **Chuyển mạch:** Ở chặng này của **PBR, BRDF, lighting tích hợp (integration / 통합) và material các mô hình (models / 모델들)**, **Image-based lighting** tiếp nhận điểm tựa từ **Normal ánh xạ (mapping / 매핑)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tone ánh xạ (mapping / 매핑)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Image-based lighting

Môi trường (environment / 환경) map cung cấp incoming light từ nhiều directions. Prefiltering môi trường (environment / 환경) cho roughness levels và precomputed BRDF terms giúp approximate integral nhanh ở thời gian chạy (runtime / 런타임).

Đây là ví dụ đổi computation thời gian chạy (runtime / 런타임) lấy preprocessing/lưu trữ (storage / 저장소).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **PBR, BRDF, lighting tích hợp (integration / 통합) và material các mô hình (models / 모델들)**, **Tone ánh xạ (mapping / 매핑)** tiếp nhận điểm tựa từ **Image-based lighting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tone ánh xạ (mapping / 매핑)

Lighting computation có thể tạo HDR values vượt display phạm vi (range / 범위). Tone ánh xạ (mapping / 매핑) ánh xạ động (dynamic / 동적) phạm vi (range / 범위) sang đầu ra (output / 출력) display trong khi cố giữ perceptual relationships.

Nếu gỡ lỗi (debug / 디버그) material sau tone ánh xạ (mapping / 매핑)/exposure, cần nhớ visual kết quả (result / 결과) đã qua color chuỗi xử lý (pipeline / 파이프라인); linear-space giá trị (value / 값) và displayed điểm ảnh (pixel / 픽셀) không đồng nhất.

> **Chuyển mạch:** Trong **PBR, BRDF, lighting tích hợp (integration / 통합) và material các mô hình (models / 모델들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Tone ánh xạ (mapping / 매핑)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> PBR là đặc tả hợp đồng (contract / 계약) giữa material parameters và light vận chuyển (transport / 전송) approximation. Material không “có màu” độc lập; nó biến incoming radiance thành outgoing radiance theo mô hình (model / 모델), rồi camera/color chuỗi xử lý (pipeline / 파이프라인) biến radiance thành điểm ảnh (pixel / 픽셀) nhìn thấy.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
