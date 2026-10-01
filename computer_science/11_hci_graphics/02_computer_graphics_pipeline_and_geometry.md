# Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Scene không phải ảnh (image / 이미지)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Coordinate spaces** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Computer graphics biến mathematical scene biểu diễn (representation / 표현) thành pixels. chuỗi xử lý (pipeline / 파이프라인) này nối tuyến tính (linear / 선형) algebra, hình học (geometry / 기하학), hardware parallelism và perception. Hiểu nó giúp giải thích game rendering, CAD, dữ liệu (data / 데이터) visualization, UI compositing và GPU programming.

## Scene không phải ảnh (image / 이미지)

Một 3D scene chứa hình học (geometry / 기하학), materials, lights, cameras và transformations. ảnh (image / 이미지) cuối là projection của scene từ viewpoint cụ thể.

Do đó rendering là ánh xạ (mapping / 매핑) từ world mô hình (model / 모델) sang 2D samples.

> **Chuyển mạch:** Trong **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Coordinate spaces** tiếp nhận điểm tựa từ **Scene không phải ảnh (image / 이미지)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) transformation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coordinate spaces

Vertex có thể đi qua nhiều coordinate các hệ thống (systems / 시스템들):

```text
model/local → world → view/camera → clip → normalized device → screen
```

Transformation matrices giúp compose translation, rotation, quy mô (scale / 규모) và projection.

Homogeneous coordinates dùng thêm dimension để translation trở thành phép nhân ma trận (matrix multiplication / 행렬 곱셈) và perspective projection có biểu diễn (representation / 표현) thống nhất.

> **Chuyển mạch:** Ở chặng này của **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Mô hình (model / 모델) transformation** tiếp nhận điểm tựa từ **Coordinate spaces** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **View transformation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) transformation

Cục bộ (local / 로컬) mô hình (model / 모델) coordinates thuận tiện author đối tượng (object / 객체) quanh origin. mô hình (model / 모델) ma trận (matrix / 행렬) đặt đối tượng (object / 객체) vào world.

Nếu parent-child hierarchy, transformation compose: hand transform phụ thuộc arm, arm phụ thuộc body. Scene đồ thị (graph / 그래프) dùng cây (tree / 트리) để quản lý hierarchical transforms.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **View transformation** tiếp nhận điểm tựa từ **Mô hình (model / 모델) transformation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Projection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## View transformation

Camera transform đổi world coordinates sang coordinate frame nơi camera ở chuẩn gốc (canonical / 정본) position/orientation.

Thay vì “di chuyển camera”, toán học thường tương đương transform world theo inverse camera transform.

> **Chuyển mạch:** Trong **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Projection** tiếp nhận điểm tựa từ **View transformation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Clipping** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Projection

Orthographic projection giữ parallel lines và không shrink theo độ sâu (depth / 깊이); perspective projection làm đối tượng (object / 객체) xa nhỏ hơn.

Perspective divide sau clip-space transform tạo nonlinear độ sâu (depth / 깊이) tác động (effect / 효과) dù ma trận (matrix / 행렬) chuỗi xử lý (pipeline / 파이프라인) dùng homogeneous coordinates.

Near/far planes ảnh hưởng độ sâu (depth / 깊이) precision; ratio quá lớn có thể gây z-fighting.

> **Chuyển mạch:** Ở chặng này của **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Clipping** tiếp nhận điểm tựa từ **Projection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rasterization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Clipping

Hình học (geometry / 기하학) ngoài view frustum không cần rasterize. Clipping cắt primitives tại boundaries trước screen ánh xạ (mapping / 매핑).

Culling loại hình học (geometry / 기하학) chắc chắn không visible, như back-face culling hoặc frustum culling, giảm công việc (work / 작업).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Rasterization** tiếp nhận điểm tựa từ **Clipping** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vertex và fragment shaders** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rasterization

Rasterizer xác định pixels/samples covered bởi triangles và interpolate attributes như độ sâu (depth / 깊이), texture coordinates, normals.

Triangle là thành phần nguyên thủy (primitive / 기본 요소) phổ biến vì ba điểm luôn định nghĩa plane và hardware tối ưu mạnh.

> **Chuyển mạch:** Trong **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Vertex và fragment shaders** tiếp nhận điểm tựa từ **Rasterization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ sâu (depth / 깊이) buffer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vertex và fragment shaders

Vertex shader xử lý per-vertex transformations/attributes. Fragment/điểm ảnh (pixel / 픽셀) shader tính color/độ sâu (depth / 깊이) cho generated fragments.

Hiện đại (modern / 현대적) GPU chuỗi xử lý (pipeline / 파이프라인) programmable ở nhiều stages. Shader programs chạy massively parallel trên dữ liệu (data / 데이터) tương tự.

> **Chuyển mạch:** Ở chặng này của **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Độ sâu (depth / 깊이) buffer** tiếp nhận điểm tựa từ **Vertex và fragment shaders** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ sâu (depth / 깊이) buffer

Z-buffer lưu độ sâu (depth / 깊이) gần nhất per điểm ảnh (pixel / 픽셀)/mẫu (sample / 표본) để resolve visibility. Precision và thứ tự (ordering / 순서) có thể tạo artifacts.

Transparency phức tạp hơn vì blending phụ thuộc thứ tự (order / 순서); simple z-buffer không giải hoàn toàn overlapping translucent surfaces.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Độ sâu (depth / 깊이) buffer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“3D graphics là vẽ đối tượng (object / 객체) 3D lên màn hình.”** Screen chỉ là 2D mẫu (sample / 표본) grid; 3D tồn tại trong scene/math biểu diễn (representation / 표현).

**“GPU chỉ là CPU nhiều cốt lõi (core / 핵심).”** GPU thực thi (execution / 실행)/bộ nhớ (memory / 메모리) mô hình (model / 모델) tối ưu thông lượng (throughput / 처리량)/data-parallel workloads với các ràng buộc (constraints / 제약조건들) khác CPU.

**“ma trận (matrix / 행렬) là cú pháp (syntax / 문법) graphics.”** ma trận (matrix / 행렬) biểu diễn transformations composable; ý nghĩa hình học (geometry / 기하학) quan trọng hơn API.

> **Chuyển mạch:** Trong **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Rendering chuỗi xử lý (pipeline / 파이프라인) liên tục đổi biểu diễn (representation / 표현) để biến hình học (geometry / 기하학) trong world thành samples trên screen, giữ những properties cần và bỏ công việc (work / 작업) không visible.

> **Chuyển mạch:** Ở chặng này của **Computer graphics chuỗi xử lý (pipeline / 파이프라인) và hình học (geometry / 기하학)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [vectors/linear algebra](../../mathematics/04_vectors_linear_algebra/00_vectors.md), [linear transformations](../../mathematics/04_vectors_linear_algebra/02_linear_transformations.md), [GPU architecture](../02_computer_architecture/05_parallel_computer_architecture.md) và [raster/color/rendering](./03_images_color_rasterization_and_rendering.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
