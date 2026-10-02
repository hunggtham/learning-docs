# Advanced HCI & Computer Graphics

> **Mạch đọc:** [README](./README.md) là owner của **Advanced HCI & Computer Graphics**. Route đi từ frame/GPU synchronization → command buffers/resource barriers → PBR/BRDF/materials, để frame budget nối với pipeline và chất lượng hình ảnh.

Roadmap:

1. [Frame pipeline, GPU synchronization và frame budget](./00_frame_pipeline_gpu_synchronization_and_frame_budget.md)
2. [Modern GPU pipeline, command buffers và resource barriers](./01_gpu_pipeline_command_buffers_and_resource_barriers.md)
3. [PBR, BRDF, lighting integration và material models](./02_pbr_brdf_lighting_and_material_models.md)
4. Shadowing, toàn cục (global / 전역) illumination và ray/đường dẫn (path / 경로) tracing
5. Temporal anti-aliasing, upscaling và frame reconstruction
6. GPU bộ nhớ (memory / 메모리), texture streaming và residency
7. Real-time input-to-photon độ trễ (latency / 지연 시간) và frame pacing
8. tương tác (interaction / 상호작용) đo lường (measurement / 측정), controlled experiments và usability bằng chứng (evidence / 증거)
9. khả năng tiếp cận (accessibility / 접근성) kỹ thuật (engineering / 엔지니어링): ngữ nghĩa (semantics / 의미론), focus, đầu vào (input / 입력) modalities, contrast
10. Human lỗi (error / 오류), safety-critical UI và phản hồi (feedback / 피드백) thiết kế (design / 설계)
11. Visualization perception và misleading encodings
12. XR/spatial interfaces và motion/perception các ràng buộc (constraints / 제약조건들)

Ba chapter đầu xây thực thi (execution / 실행) chuỗi xử lý (pipeline / 파이프라인) rồi nối sang vật lý (physical / 물리적) material/light mô hình (model / 모델). Các phần sau sẽ tiếp tục rendering chất lượng (quality / 품질), GPU bộ nhớ (memory / 메모리) và human-perception/HCI các ràng buộc (constraints / 제약조건들).

> **Bàn giao:** Sau **Advanced HCI & Computer Graphics**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
