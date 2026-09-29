# Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)

> **Mạch đọc:** Đặt **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Scene không phải ảnh (image / 이미지)** sang **Coordinate spaces**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Computer graphics biến mathematical scene biểu diễn (representation / 표현) thành pixels. chuỗi xử lý (pipeline / 파이프라인) này nối tuyến tính (linear / 선형) algebra, hình học (geometry / 기하학), hardware parallelism và perception. Hiểu nó giúp giải thích game rendering, CAD, dữ liệu (data / 데이터) visualization, UI compositing và GPU programming.

## Scene không phải ảnh (image / 이미지)

Một 3D scene chứa hình học (geometry / 기하학), materials, lights, cameras và transformations. ảnh (image / 이미지) cuối là projection của scene từ viewpoint cụ thể.

Do đó rendering là ánh xạ (mapping / 매핑) từ world mô hình (model / 모델) sang 2D samples.


> **Chuyển mạch:** Từ **Scene không phải ảnh (image / 이미지)**, ta sang **Coordinate spaces** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Coordinate spaces

Vertex có thể đi qua nhiều coordinate các hệ thống (systems / 시스템들):

```text
model/local → world → view/camera → clip → normalized device → screen
```

Transformation matrices giúp compose translation, rotation, quy mô (scale / 규모) và projection.

Homogeneous coordinates dùng thêm dimension để translation trở thành phép nhân ma trận (matrix multiplication / 행렬 곱셈) và perspective projection có biểu diễn (representation / 표현) thống nhất.


> **Chuyển mạch:** Từ **Coordinate spaces**, ta sang **mô hình (model / 모델) transformation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình (model / 모델) transformation

Cục bộ (local / 로컬) mô hình (model / 모델) coordinates thuận tiện author đối tượng (object / 객체) quanh origin. mô hình (model / 모델) ma trận (matrix / 행렬) đặt đối tượng (object / 객체) vào world.

Nếu parent-child hierarchy, transformation compose: hand transform phụ thuộc arm, arm phụ thuộc body. Scene đồ thị (graph / 그래프) dùng cây (tree / 트리) để quản lý hierarchical transforms.


> **Chuyển mạch:** Từ **mô hình (model / 모델) transformation**, ta sang **View transformation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## View transformation

Camera transform đổi world coordinates sang coordinate frame nơi camera ở chuẩn gốc (canonical / 정본) position/orientation.

Thay vì “di chuyển camera”, toán học thường tương đương transform world theo inverse camera transform.


> **Chuyển mạch:** Từ **View transformation**, ta sang **Projection** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Projection

Orthographic projection giữ parallel lines và không shrink theo độ sâu (depth / 깊이); perspective projection làm đối tượng (object / 객체) xa nhỏ hơn.

Perspective divide sau clip-space transform tạo nonlinear độ sâu (depth / 깊이) tác động (effect / 효과) dù ma trận (matrix / 행렬) chuỗi xử lý (pipeline / 파이프라인) dùng homogeneous coordinates.

Near/far planes ảnh hưởng độ sâu (depth / 깊이) precision; ratio quá lớn có thể gây z-fighting.


> **Chuyển mạch:** Từ **Projection**, ta sang **Clipping** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Clipping

Hình học (geometry / 기하학) ngoài view frustum không cần rasterize. Clipping cắt primitives tại boundaries trước screen ánh xạ (mapping / 매핑).

Culling loại hình học (geometry / 기하학) chắc chắn không visible, như back-face culling hoặc frustum culling, giảm công việc (work / 작업).


> **Chuyển mạch:** Từ **Clipping**, ta sang **Rasterization** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Rasterization

Rasterizer xác định pixels/samples covered bởi triangles và interpolate attributes như độ sâu (depth / 깊이), texture coordinates, normals.

Triangle là thành phần nguyên thủy (primitive / 기본 요소) phổ biến vì ba điểm luôn định nghĩa plane và hardware tối ưu mạnh.


> **Chuyển mạch:** Từ **Rasterization**, ta sang **Vertex và fragment shaders** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Vertex và fragment shaders

Vertex shader xử lý per-vertex transformations/attributes. Fragment/điểm ảnh (pixel / 픽셀) shader tính color/độ sâu (depth / 깊이) cho generated fragments.

Hiện đại (modern / 현대적) GPU chuỗi xử lý (pipeline / 파이프라인) programmable ở nhiều stages. Shader programs chạy massively parallel trên dữ liệu (data / 데이터) tương tự.


> **Chuyển mạch:** Từ **Vertex và fragment shaders**, ta sang **độ sâu (depth / 깊이) buffer** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ sâu (depth / 깊이) buffer

Z-buffer lưu độ sâu (depth / 깊이) gần nhất per điểm ảnh (pixel / 픽셀)/mẫu (sample / 표본) để resolve visibility. Precision và thứ tự (ordering / 순서) có thể tạo artifacts.

Transparency phức tạp hơn vì blending phụ thuộc thứ tự (order / 순서); simple z-buffer không giải hoàn toàn overlapping translucent surfaces.


> **Chuyển mạch:** Từ **độ sâu (depth / 깊이) buffer**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“3D graphics là vẽ đối tượng (object / 객체) 3D lên màn hình.”** Screen chỉ là 2D mẫu (sample / 표본) grid; 3D tồn tại trong scene/math biểu diễn (representation / 표현).

**“GPU chỉ là CPU nhiều cốt lõi (core / 핵심).”** GPU thực thi (execution / 실행)/bộ nhớ (memory / 메모리) mô hình (model / 모델) tối ưu thông lượng (throughput / 처리량)/data-parallel workloads với các ràng buộc (constraints / 제약조건들) khác CPU.

**“ma trận (matrix / 행렬) là cú pháp (syntax / 문법) graphics.”** ma trận (matrix / 행렬) biểu diễn transformations composable; ý nghĩa hình học (geometry / 기하학) quan trọng hơn API.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Rendering chuỗi xử lý (pipeline / 파이프라인) liên tục đổi biểu diễn (representation / 표현) để biến hình học (geometry / 기하학) trong world thành samples trên screen, giữ những properties cần và bỏ công việc (work / 작업) không visible.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [vectors/linear algebra](../../mathematics/04_vectors_linear_algebra/00_vectors.md), [linear transformations](../../mathematics/04_vectors_linear_algebra/02_linear_transformations.md), [GPU architecture](../02_computer_architecture/05_parallel_computer_architecture.md) và [raster/color/rendering](./03_images_color_rasterization_and_rendering.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 hci human factors and interaction models](./00_hci_human_factors_and_interaction_models.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
