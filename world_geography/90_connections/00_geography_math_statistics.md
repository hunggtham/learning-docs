# Địa lý kết nối với Toán và Statistics

## Geometry là ngôn ngữ của vị trí

Coordinates, distance, area, direction và projection đều là geometry. Trên small local plane, Euclidean geometry đủ; trên global surface, spherical/ellipsoidal geometry cần thiết. Việc chọn geometry sai có thể làm distance/area sai dù code chạy đúng.

## Scale và dimensional thinking

Map scale là ratio. Density là quantity/area. Gradient là change/distance. Đây là dimensional reasoning: nếu population tăng gấp đôi nhưng area cũng gấp đôi, density không đổi. Units giúp phát hiện sai lầm.

## Spatial statistics khác statistics thường ở dependence

Classical statistical intuition thường assume observations independent. Geographic observations gần nhau thường similar do shared process, gọi là **spatial autocorrelation (공간 자기상관)**. Nếu bỏ qua, standard errors và significance có thể sai.

Moran’s I là một measure global spatial autocorrelation. Ý tưởng cốt lõi: so similarity giữa observation với weighted neighbors. Weight matrix \(W\) encode adjacency/distance; vì vậy result phụ thuộc definition “neighbor”.

## Regression và spatial confounding

Nếu outcome và predictor cùng có spatial trend vì third factor, regression có thể tìm association misleading. Map residuals là diagnostic quan trọng: nếu residual còn cluster, model bỏ sót spatial structure.

## Probability và hazard

Return period, flood probability và forecast đều cần probability. Với event annual probability \(p\), probability ít nhất một lần trong \(n\) năm là:

\[
1-(1-p)^n
\]

Điều này giải thích vì sao “100-year flood” vẫn có thể xảy ra hai năm gần nhau.

## Optimization

Facility location, route planning và service coverage là optimization. Ví dụ **p-median** tìm vị trí p facilities giảm tổng demand-weighted distance; **set covering** tìm số facility tối thiểu để cover demand trong threshold. Đây là bridge trực tiếp tới Operations Research.

## Graph theory

Road, airline, river và trade networks có thể model bằng graph. Degree, betweenness, shortest path và community detection giúp đo hub/chokepoint. Geography bổ sung edge weight thực tế như travel time, border cost và capacity.

## Mental Model

Math cung cấp **representation và constraint**; geography cung cấp **meaning of space**. Đừng dùng công thức distance, regression hay network metric trước khi xác định spatial unit, CRS, scale và process.

Xem thêm: [GIS](../00_foundations/04_geospatial_data_gis_remote_sensing.md), [Transport networks](../02_human_geography/08_transport_trade_globalization.md).


## Distance không chỉ có một định nghĩa

Trong plane geometry, Euclidean distance giữa hai điểm là

\[
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
\]

Nhưng geographic problem có thể cần great-circle distance trên sphere/ellipsoid, network distance theo road, travel time hoặc cost distance. Chọn metric sai có thể làm analysis sai dù calculation hoàn toàn chính xác.

Ví dụ hai điểm cách nhau 20 km straight-line nhưng bị ngăn bởi mountain và chỉ có một pass; travel time có thể dài hơn một cặp điểm cách 50 km dọc expressway. Vì vậy metric phải phản ánh mechanism của phenomenon.

## Spatial autocorrelation

Trong statistics thông thường, observation thường được giả định independent. Spatial data hay vi phạm assumption này: nearby places thường giống nhau hơn distant places do shared environment, diffusion hoặc clustering. Hiện tượng đó gọi là **spatial autocorrelation (tự tương quan không gian / 공간 자기상관)**.

Điều này quan trọng trong ML và econometrics. Nếu train/test split random trên spatial samples, model có thể “nhìn thấy” gần-neighbor information và đánh giá performance quá optimistic. Spatial cross-validation tách vùng địa lý có thể realistic hơn.

## Scale và aggregation

Average income, disease rate hoặc election result có thể thay đổi interpretation khi đổi spatial unit. **MAUP — Modifiable Areal Unit Problem** mô tả việc statistical result phụ thuộc cách chia zone và level of aggregation. Đây là lý do map theo province có thể kể câu chuyện khác map theo district dù raw events giống nhau.

## Geometry như constraint model

Buffer, intersection, Voronoi diagram và shortest path không chỉ là GIS operations; chúng encode assumptions. Buffer 500 m quanh station giả định proximity radial có meaning; network service area 10 phút giả định travel along graph. Mathematical object nên được chọn theo real process chứ không theo tool convenience.

