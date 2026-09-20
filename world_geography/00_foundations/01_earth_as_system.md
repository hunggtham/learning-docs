# Trái Đất như một hệ thống

## Từ “một hành tinh” đến một system động

Để hiểu địa lý tự nhiên, không nên tưởng tượng Trái Đất là một quả cầu có bề mặt tĩnh. Nó là **Earth system (hệ Trái Đất / 지구 시스템)** gồm nhiều subsystem trao đổi matter và energy. Khí quyển, đại dương, đá, đất, băng và sinh vật liên kết bằng các feedback. Một thay đổi ở một subsystem có thể truyền sang subsystem khác.

Các sphere thường dùng là **atmosphere (khí quyển / 대기권)**, **hydrosphere (thủy quyển / 수권)**, **lithosphere/geosphere (thạch quyển–địa quyển / 암석권·지권)**, **biosphere (sinh quyển / 생물권)** và **cryosphere (băng quyển / 빙권)**. Đây là abstraction để học; trong thực tế ranh giới giữa chúng không kín.

## Nguồn năng lượng: Mặt Trời và nội nhiệt

Phần lớn process trên bề mặt — gió, chu trình nước, photosynthesis, ocean surface circulation — được dẫn động bởi **solar energy**. Do Trái Đất hình cầu, quay quanh trục nghiêng và quay quanh Mặt Trời, năng lượng phân bố không đều theo latitude và season. Chênh lệch năng lượng này tạo gradient nhiệt, gradient áp suất và cuối cùng sinh ra circulation.

Ngược lại, **internal heat (nội nhiệt / 지구 내부 열)** từ quá trình hình thành hành tinh và phân rã phóng xạ duy trì convection trong mantle, góp phần làm lithospheric plates chuyển động. Vì vậy một cách thô có thể xem geography vật lý có hai “engine”: **Mặt Trời vận hành phần lớn khí hậu–nước–sinh học; nội nhiệt vận hành phần lớn tectonics**.

## Matter cycles và conservation

Nước, carbon, nitrogen và nhiều nguyên tố không biến mất khỏi hệ một cách tùy ý; chúng chuyển giữa reservoir. Đây là application của conservation. Ví dụ water cycle gồm evaporation, condensation, precipitation, infiltration, runoff và storage. Khi đô thị hóa phủ bê tông, tổng lượng nước trong Earth system gần như không đổi, nhưng **partitioning** thay đổi: infiltration giảm, runoff tăng, flood peak có thể tăng.

Trong modeling, một reservoir thường được mô tả bằng mass balance:

\[
\Delta S = I - O
\]

Trong đó \(S\) là storage, \(I\) là inflow và \(O\) là outflow trong khoảng thời gian xét. Công thức đơn giản này xuất hiện trong hồ chứa, groundwater, carbon budget, inventory và cả queueing system trong computing: trạng thái tăng khi input lớn hơn output.

## Feedback: vì sao hệ không phản ứng tuyến tính đơn giản

**Feedback (phản hồi / 피드백)** xảy ra khi kết quả của một process quay lại ảnh hưởng chính process đó. **Negative feedback** làm hệ có xu hướng ổn định; **positive feedback** khuếch đại thay đổi.

Ví dụ ice–albedo feedback: băng sáng phản xạ nhiều sunlight. Khi warming làm băng giảm, bề mặt tối hơn hấp thụ nhiều năng lượng, tăng warming và tiếp tục làm băng giảm. Đây là positive feedback. “Positive” ở đây không có nghĩa tốt; nó có nghĩa cùng chiều khuếch đại.

## Equilibrium và dynamic equilibrium

Nhiều system địa lý không đứng yên mà ở **dynamic equilibrium (cân bằng động / 동적 평형)**: inflow và outflow gần cân bằng trong trung bình dài hạn dù từng thời điểm biến động. Một bãi biển có thể giữ hình dạng tương đối qua năm dù từng hạt cát luôn di chuyển. Một river channel có thể “ổn định” ở macro scale nhưng vẫn xói và bồi liên tục.

Hiểu dynamic equilibrium giúp tránh sai lầm “thấy thay đổi = hệ mất ổn định hoàn toàn”. Ngược lại, một hệ có thể nhìn yên trong thời gian ngắn nhưng đã vượt threshold và đang tích lũy thay đổi.

## Threshold, nonlinearity và tipping behavior

Nhiều process không tuyến tính. Cho đến một điểm, tăng rainfall chỉ làm đất ẩm hơn; khi soil saturation đạt ngưỡng, thêm mưa có thể chuyển nhanh thành overland flow và lũ. Trong slope stability, tăng water pressure trong pore có thể làm effective stress giảm đến threshold và landslide xảy ra.

Đây là connection quan trọng với engineering và software reliability: hệ thường chịu tải tốt đến khi một constraint bị saturate, sau đó behavior thay đổi mạnh. Vì vậy geographic risk không thể chỉ suy từ average condition.

## Spatial heterogeneity

Trái Đất không đồng nhất. Material, elevation, vegetation, population, infrastructure và institutions khác nhau theo không gian. Chính **heterogeneity (tính không đồng nhất / 공간적 이질성)** khiến cùng một forcing tạo kết quả khác nhau. Cùng lượng mưa 200 mm có thể gây ít vấn đề ở vùng đất thấm tốt nhưng lũ nghiêm trọng ở lưu vực đô thị hóa và dốc.

## Mental Model

Hãy hình dung một region như **network of reservoirs + flows + feedbacks**. Reservoir có thể là water, heat, sediment, people, capital hoặc information. Geography hỏi: reservoir nằm ở đâu, flow đi qua đâu, bottleneck nào giới hạn flow, feedback nào ổn định hoặc khuếch đại, và boundary nào ta đang dùng để phân tích.

Xem tiếp: [Plate tectonics](../01_physical_geography/00_plate_tectonics_geologic_time.md), [Khí quyển và khí hậu](../01_physical_geography/02_atmosphere_weather_climate.md), [Nước và lưu vực](../01_physical_geography/04_hydrology_rivers_groundwater.md).
