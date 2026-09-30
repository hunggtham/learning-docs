# Sewage — nước sau khi dùng đi đâu?

Hệ thống cấp nước đưa nước sạch vào thành phố; hệ thống thoát nước và nước thải đưa nước đã dùng, nước mưa và chất ô nhiễm ra khỏi khu dân cư mà không biến sông thành cống. Hai hệ thống có hình dạng mạng gần giống nhau nhưng mục tiêu vật lý trái ngược: cấp nước duy trì áp lực dương để đẩy nước sạch tới người dùng, còn sewer cố tận dụng trọng lực và chỉ bơm khi địa hình bắt buộc.

## 1. Luồng cơ bản

```text
Sink / toilet / shower
      ↓
Building drain
      ↓
Local sewer
      ↓
Interceptor sewer
      ↓
Pump station (khi cần)
      ↓
Wastewater treatment plant
      ↓
Screening + grit removal
      ↓
Primary treatment
      ↓
Biological treatment
      ↓
Secondary clarification
      ↓
Disinfection / advanced treatment
      ↓
River / sea / reuse

Sludge → thickening → digestion/dewatering → disposal or resource recovery
```

Song song với dòng nước là dòng bùn (sludge / 슬러지). Nếu chỉ nhìn nước đầu ra mà bỏ qua sludge, ta mới hiểu nửa hệ thống.

## 2. Combined sewer và separate sewer

Hệ thống cống chung (combined sewer / 합류식 하수도) nhận cả nước thải và nước mưa. Ưu điểm lịch sử là chỉ cần một mạng ống; nhược điểm là mưa lớn có thể làm lưu lượng vượt công suất và gây overflow. Hệ thống cống tách riêng (separate sewer / 분류식 하수도) có mạng sanitary sewer và stormwater riêng, giảm tải cho nhà máy xử lý nhưng đòi hỏi hạ tầng kép và quản lý đấu nối đúng.

Nhiều thành phố không thuộc hoàn toàn một loại. Hạ tầng được xây qua nhiều thập kỷ nên có vùng combined, vùng separate và các dự án retrofit.

## 3. Hàn Quốc: mật độ sewer cao và bài toán đô thị trưởng thành

Seoul công bố tỷ lệ phục vụ sewer 100% theo thống kê cuối 2024 cùng hơn 10.000 km tuyến cống. Với một đô thị đã phủ mạng gần toàn bộ, bài toán chuyển từ “xây cống tới khu chưa có” sang renewal, flood resilience, kiểm soát infiltration/inflow, nâng cấp treatment và thích nghi với mưa cực đoan.

Điểm đáng học từ Hàn Quốc là infrastructure lifecycle: khi coverage gần hoàn chỉnh, chi phí không biến mất; nó chuyển sang bảo trì tài sản ngầm, chống lão hóa, energy efficiency và nâng chuẩn xả thải.

## 4. Việt Nam: coverage và treatment không nên bị đánh đồng

Ở Việt Nam, quản lý thoát nước và xử lý nước thải đô thị chịu khung của Bộ Xây dựng và chính quyền địa phương. Thông tư 15/2021/TT-BXD yêu cầu hạ tầng thu gom phải đồng bộ và kết nối với xử lý phù hợp trước khi xả ra nguồn tiếp nhận.

Một thành phố có cống thoát nước không đồng nghĩa toàn bộ wastewater đã được xử lý tập trung. Cống có thể chủ yếu phục vụ drainage, có đoạn combined, có septic tank ở cấp hộ/tòa nhà, và tỷ lệ nước thực sự đến wastewater treatment plant có thể thấp hơn tỷ lệ dân cư “có thoát nước”. Đây là điểm rất quan trọng khi đọc số liệu.

## 5. So sánh Hàn Quốc ↔ Việt Nam

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| Trọng tâm hạ tầng | Renewal, resilience, advanced treatment | Mở rộng collection và treatment song song với đô thị hóa |
| Mạng cũ | Nhiều tài sản đã vận hành lâu năm, cần rehabilitation | Nhiều thành phố có mạng phát triển không đồng đều, mixed legacy + new build |
| Mưa lớn | Urban flooding, combined-sewer overflow và capacity | Flooding, drainage capacity, lấn chiếm dòng chảy và tốc độ bê tông hóa đều có thể tạo pressure |
| Tổ chức | Utility/municipal systems trưởng thành | Chính quyền địa phương và đơn vị thoát nước theo khung quốc gia, dự án thường theo lưu vực đô thị |

## 6. Vì sao wastewater treatment tốn điện?

Trong xử lý sinh học hiếu khí, vi sinh vật cần oxygen để phân hủy chất hữu cơ. Aeration vì thế có thể là một trong những tải điện lớn của nhà máy. Đây là ví dụ hệ thống giao nhau: sewer phụ thuộc electricity grid; mất điện kéo dài có thể ảnh hưởng pumping và treatment, còn wastewater plant lại có thể thu hồi biogas từ sludge để bù một phần năng lượng.

## 7. Mental model để đọc một thành phố

Khi thấy dự án “nhà máy xử lý 200.000 m³/ngày”, đừng chỉ hỏi công suất plant. Hãy hỏi thêm: catchment nào được đấu nối, interceptor đã xong chưa, inflow vào plant thực tế bao nhiêu, stormwater có đi chung không, sludge đi đâu, và nguồn tiếp nhận yêu cầu chuẩn nào. Nhà máy lớn mà network chưa thu gom đủ vẫn có thể underutilized.

Từ đây, [water supply](../water-supply/README.md) và [electricity grid](../electricity-grid/README.md) tạo thành bộ ba hạ tầng đô thị cơ bản: nước vào, nước ra và năng lượng duy trì cả hai.

## Nguồn chính thức tham chiếu

- Seoul Metropolitan Government — Sewer Statistics 2024: https://news.seoul.go.kr/env/archives/39257
- Bộ Xây dựng Việt Nam — Thông tư 15/2021/TT-BXD về thu gom, thoát nước thải đô thị: https://vbpl.vn/boxaydung/Pages/vbpq-toanvan.aspx?ItemID=152387
