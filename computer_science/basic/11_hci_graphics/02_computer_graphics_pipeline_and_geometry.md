# Computer graphics pipeline và geometry

Computer graphics biến mathematical scene representation thành pixels. Pipeline này nối linear algebra, geometry, hardware parallelism và perception. Hiểu nó giúp giải thích game rendering, CAD, data visualization, UI compositing và GPU programming.

## Scene không phải image

Một 3D scene chứa geometry, materials, lights, cameras và transformations. Image cuối là projection của scene từ viewpoint cụ thể.

Do đó rendering là mapping từ world model sang 2D samples.

## Coordinate spaces

Vertex có thể đi qua nhiều coordinate systems:

```text
model/local → world → view/camera → clip → normalized device → screen
```

Transformation matrices giúp compose translation, rotation, scale và projection.

Homogeneous coordinates dùng thêm dimension để translation trở thành matrix multiplication và perspective projection có representation thống nhất.

## Model transformation

Local model coordinates thuận tiện author object quanh origin. Model matrix đặt object vào world.

Nếu parent-child hierarchy, transformation compose: hand transform phụ thuộc arm, arm phụ thuộc body. Scene graph dùng tree để quản lý hierarchical transforms.

## View transformation

Camera transform đổi world coordinates sang coordinate frame nơi camera ở canonical position/orientation.

Thay vì “di chuyển camera”, toán học thường tương đương transform world theo inverse camera transform.

## Projection

Orthographic projection giữ parallel lines và không shrink theo depth; perspective projection làm object xa nhỏ hơn.

Perspective divide sau clip-space transform tạo nonlinear depth effect dù matrix pipeline dùng homogeneous coordinates.

Near/far planes ảnh hưởng depth precision; ratio quá lớn có thể gây z-fighting.

## Clipping

Geometry ngoài view frustum không cần rasterize. Clipping cắt primitives tại boundaries trước screen mapping.

Culling loại geometry chắc chắn không visible, như back-face culling hoặc frustum culling, giảm work.

## Rasterization

Rasterizer xác định pixels/samples covered bởi triangles và interpolate attributes như depth, texture coordinates, normals.

Triangle là primitive phổ biến vì ba điểm luôn định nghĩa plane và hardware tối ưu mạnh.

## Vertex và fragment shaders

Vertex shader xử lý per-vertex transformations/attributes. Fragment/pixel shader tính color/depth cho generated fragments.

Modern GPU pipeline programmable ở nhiều stages. Shader programs chạy massively parallel trên data tương tự.

## Depth buffer

Z-buffer lưu depth gần nhất per pixel/sample để resolve visibility. Precision và ordering có thể tạo artifacts.

Transparency phức tạp hơn vì blending phụ thuộc order; simple z-buffer không giải hoàn toàn overlapping translucent surfaces.

## Common Misconceptions

**“3D graphics là vẽ object 3D lên màn hình.”** Screen chỉ là 2D sample grid; 3D tồn tại trong scene/math representation.

**“GPU chỉ là CPU nhiều core.”** GPU execution/memory model tối ưu throughput/data-parallel workloads với constraints khác CPU.

**“Matrix là syntax graphics.”** Matrix biểu diễn transformations composable; ý nghĩa geometry quan trọng hơn API.

## Mental Model

> Rendering pipeline liên tục đổi representation để biến geometry trong world thành samples trên screen, giữ những properties cần và bỏ work không visible.

## Kết nối

Đọc [vectors/linear algebra](../../../mathematics/04_vectors_linear_algebra/00_vectors.md), [linear transformations](../../../mathematics/04_vectors_linear_algebra/02_linear_transformations.md), [GPU architecture](../02_computer_architecture/05_parallel_computer_architecture.md) và [raster/color/rendering](./03_images_color_rasterization_and_rendering.md).