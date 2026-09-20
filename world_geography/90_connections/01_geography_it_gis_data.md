# Địa lý kết nối với IT, GIS, Data Engineering và AI

## Spatial data là first-class data type

Trong application thông thường, location hay bị lưu như hai cột latitude/longitude rồi xử lý thủ công. Khi spatial queries tăng, nên dùng geometry/geography type và spatial index. PostGIS, SQL Server Spatial, Oracle Spatial và nhiều engine cung cấp predicates và distance operator.

## CRS bug là một loại unit bug

EPSG:4326 coordinates thường ở degrees; projected CRS có thể ở meters. Nếu code giả định mọi coordinate là meter, buffer 1000 có thể trở thành 1000 degrees — bug logic nghiêm trọng. CRS phải là metadata bắt buộc như unit trong physics.

## Spatial indexing

Exact geometry operation đắt. Spatial index dùng bounding boxes/hierarchical partitions để loại candidates. Đây giống database B-tree giảm search space nhưng optimized cho 2D/ND space. R-tree, quadtree, geohash, S2/H3 là các strategy khác nhau.

## Tile architecture

Web map thường dùng raster/vector tiles theo zoom. Generalization và LOD (level of detail) quyết định payload. Vector tiles cho style client-side; raster tiles render sẵn. Cache key thường gắn zoom/x/y.

## Routing

Road routing là weighted graph shortest path. Weight có thể là distance, time, toll hoặc generalized cost. Dijkstra/A* hoạt động trên graph; geographic heuristic của A* giúp search nhanh nếu admissible. Real routing còn turn restriction, one-way, traffic và time-dependent edge.

## Geofencing

Geofence có thể là circle/polygon. Mobile system cần xử lý GPS noise; nếu trigger ngay tại boundary, user có thể oscillate enter/exit. Hysteresis hoặc dwell time giúp ổn định event.

## Remote sensing + ML

Satellite imagery là raster tensors. CNN/transformer có thể classify land cover, detect object, segment flood/burn scar. Nhưng labels spatially biased và adjacent pixels highly correlated, nên random train/test split có thể leak geography; spatial cross-validation tốt hơn.

## Location privacy

Precise location là sensitive. Even anonymized trajectories có thể re-identify vì home/work patterns. Production system cần minimization, aggregation và access control.

## Spatial ETL

Pipeline thường gồm ingest → validate CRS/geometry → transform → spatial join → aggregate → tile/API. Geometry validity (self-intersection, ring orientation) cần check giống schema validation.

## Digital twin

City/industrial digital twin combine GIS, BIM, sensor và simulation. GIS gives geographic context; BIM gives detailed built asset. Sync temporal state là engineering challenge.

## Mental Model

Spatial software = **data engineering where distance, topology, projection và scale are part of business logic**. Treat them như type system, không phải metadata phụ.

Xem thêm: [GIS foundations](../00_foundations/04_geospatial_data_gis_remote_sensing.md), [Toán và Statistics](./00_geography_math_statistics.md).


## Coordinate reference system là một phần của data contract

Trong software system, spatial coordinate không thể được hiểu đúng chỉ từ hai con số `x, y`. Cần biết **CRS — Coordinate Reference System (좌표 참조 체계 / hệ quy chiếu tọa độ)**. Latitude/longitude trong WGS84 và projected coordinates theo meter là hai representations khác nhau. Nếu mix CRS mà không transform, distance và overlay có thể sai hoàn toàn.

Vì vậy CRS nên được coi giống data type hoặc unit trong API contract. Một field `distance=1000` vô nghĩa nếu không biết meter hay kilometer; một point `(127, 37)` cũng thiếu context nếu không biết axis order và CRS.

## Spatial index

Database bình thường tối ưu query bằng B-tree cho scalar ordering. Geometry không có natural 1-D order phù hợp mọi spatial query, nên spatial databases dùng structures như **R-tree**, GiST hoặc related indexes để prune search space. Query “objects nào intersect vùng này?” vì vậy có thể chạy nhanh mà không scan toàn bộ table.

## Raster và vector là hai data models khác nhau

Vector biểu diễn discrete features bằng point/line/polygon; raster biểu diễn space bằng grid cells. Road network hợp với vector; satellite image hoặc elevation surface thường hợp với raster. Chuyển giữa hai model có thể làm mất information hoặc tạo assumption về resolution.

## Routing như graph + geography

Road routing biến map thành graph: intersection là nodes, road segments là edges, weight có thể là distance, travel time hoặc toll. Dijkstra/A* sau đó tìm path tối ưu theo weight. Nhưng real navigation cần turn restriction, one-way street, time-dependent traffic và road class — tức graph model phải encode geographic rules.

## Geospatial ML

Spatial feature engineering có thể dùng distance tới POI, neighborhood statistics, terrain elevation hoặc land-cover class. Tuy nhiên spatial leakage và sampling bias rất phổ biến. Một model dự báo tốt ở Seoul chưa chắc generalize tới rural province vì feature distribution và spatial process khác nhau.

