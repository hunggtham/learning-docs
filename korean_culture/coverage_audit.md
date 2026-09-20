# Korean Culture — Bản kiểm toán mức độ bao phủ

> File này không phải chương học riêng. Nó là **bản kiểm toán mức độ bao phủ (coverage audit)** cho toàn bộ `korean_culture/01–33`. Thư mục `kiip/` không nằm trong phạm vi kiểm toán này.

## 1. Chuẩn ngôn ngữ hiện hành

Vòng chuẩn hoá ngôn ngữ cho phần nội dung chính `01–33` đã hoàn tất theo nguyên tắc:

```text
câu giải thích → tiếng Việt tự nhiên
thuật ngữ cần tra cứu → tiếng Việt (English)
thuật ngữ văn hoá Hàn → giữ Hangul khi cần
câu dài pha tiếng Anh → viết lại hoàn toàn bằng tiếng Việt
```

Ví dụ ưu tiên `cơ chế (mechanism)`, `vòng phản hồi (feedback loop)`, `khả năng tiếp cận (accessibility)` thay vì đặt từ tiếng Anh trực tiếp vào giữa câu tiếng Việt.

Các ngoại lệ được giữ có chủ đích gồm tên riêng, tên sản phẩm/nền tảng, mã, công thức, từ viết tắt kỹ thuật, tên file và cột **English** trong [`17_glossary_and_reference_map.md`](17_glossary_and_reference_map.md). Đây là dữ liệu tra cứu, không phải văn xuôi giải thích.

## 2. Tiêu chí một chương được coi là đủ sâu

Một chủ đề không được coi là hoàn chỉnh chỉ vì có nhiều dữ kiện. Nó phải giúp người đọc trả lời được:

```text
1. Khái niệm (What) — hiện tượng là gì?
2. Nguyên nhân (Why) — vì sao nó xuất hiện hoặc trở nên nổi bật?
3. Cơ chế (Mechanism) — thiết chế, điều kiện vật chất và động lực nào duy trì nó?
4. Biến thiên (Variation) — khác theo thế hệ, vùng, tầng lớp và bối cảnh ra sao?
5. Thay đổi (Change) — công nghệ, kinh tế, luật pháp và dân số làm nó đổi thế nào?
6. Ranh giới (Boundary) — khi nào mô hình này không còn giải thích tốt?
```

Một chương tốt cũng nên có ví dụ đời sống, liên kết chéo, mô hình tư duy, hiểu lầm phổ biến và cảnh báo khi số liệu hoặc chính sách có thể lỗi thời.

## 3. Bản đồ mức độ bao phủ hiện tại

| Lĩnh vực | Chương | Trạng thái hiện tại | Việc nên làm tiếp |
|---|---|---|---|
| Nền tảng hệ thống văn hoá | `01` | mạnh | chỉ bổ sung khi có cơ chế xuyên chương mới |
| Nho giáo, quan hệ, thứ bậc | `02` | mạnh | giữ ranh giới giữa mô tả và chuẩn tắc |
| Ngôn ngữ, kính ngữ, `눈치`, `정`, `체면` | `03` | mạnh | tránh biến thành sách ngữ pháp tổng quát |
| Gia đình, họ tộc, vòng đời | `04` + `29` | mạnh | tiếp tục theo dõi biến đổi hộ và chăm sóc |
| Giáo dục, thi cử, bằng cấp | `05` + `30` | mạnh | đào tạo lại người trưởng thành còn có thể mở rộng |
| Công sở | `06` | mạnh, đã mở rộng | đã có làm việc từ xa/lai, nhóm toàn cầu và giao tiếp bất đồng bộ |
| Ẩm thực | `07` | mạnh, đã mở rộng | đã có ăn chay, halal, dị ứng và bữa ăn tập thể đa dạng |
| Nhà ở, hanok, không gian | `08` + `31` | mạnh, đã mở rộng | đã thêm thiết kế không rào cản và già hoá tại nơi ở quen thuộc |
| Tôn giáo và thế giới quan | `09` | mạnh | chỉ thêm phong trào mới khi có nguồn học thuật tốt |
| Nghệ thuật, thủ công, di sản | `10` | mạnh, đã mở rộng | đã thêm bảo tàng, giám tuyển, biennale, hội chợ nghệ thuật và nghệ thuật số |
| Lễ Tết, nghi lễ, trò chơi | `11` | mạnh | giữ liên kết với gia đình và vùng miền |
| Đô thị, tiêu dùng, đời sống số | `12` | mạnh, đã mở rộng | đã thêm hành trình đô thị không rào cản, người gặp hạn chế di chuyển và khả năng tiếp cận số |
| Hallyu, truyền thông, nền tảng | `13` | mạnh, đã mở rộng | đã thêm lao động sáng tạo, quyền tác giả, quyền chuyển thể, ghi công và phân phối giá trị |
| Vùng miền, Jeju, bán đảo | `14` | mạnh | tránh biến khác biệt vùng thành định kiến cá nhân |
| Dân số, già hoá, di cư | `15` | mạnh | mọi số liệu phải ghi năm, quần thể và mẫu số |
| Liên hệ giữa các hệ thống | `16` | mạnh | cập nhật khi cơ chế mới xuất hiện |
| Thuật ngữ và bản đồ nguồn | `17` | tốt | tiếp tục đồng bộ thuật ngữ mới |
| Phép lịch sự và quan hệ đời thường | `18` | mạnh | ưu tiên mô tả theo bối cảnh thay vì luật cứng |
| Làm đẹp, thời trang, cơ thể | `19` | mạnh | số liệu về thủ thuật phải ghi rõ quần thể |
| Thể thao, giải trí, fandom | `20` | mạnh, đã mở rộng | đã thêm thể thao thích ứng, khả năng tiếp cận khi xem và giải trí người cao tuổi |
| Các lớp lịch sử | `21` | mạnh | không lặp thư viện `korean_history/` |
| Tên, tuổi, siêu dữ liệu xã hội | `22` | mạnh | có thể cập nhật môi trường số/toàn cầu |
| Nghĩa vụ quân sự | `23` | khá mạnh | tránh coi trải nghiệm nam giới là trải nghiệm phổ quát |
| Kinh tế, chaebol, nhà ở, dịch chuyển xã hội | `24` | mạnh | thuế, vay và chính sách phải dùng nguồn hiện hành |
| Xã hội dân sự và không gian công luận | `25` | mạnh về khung phân tích | dữ kiện chính trị hiện hành luôn phải kiểm chứng mới |
| Y tế và văn hoá sức khoẻ | `26` | mạnh, đã mở rộng | đã thêm khuyết tật, khả năng tiếp cận, chăm sóc giảm nhẹ, hospice và cuối đời |
| Internet, nhắn tin, tiếng lóng, meme | `27` | mạnh | tiếng lóng/nền tảng phải có mốc thời gian |
| Quy ước tên riêng | `28` | tốt | giữ nhất quán Việt–Hàn–Anh |
| Nuôi dạy con và chăm sóc | `29` | mạnh | nối chặt với `04`, `05`, `15`, `26` |
| Đại học và thanh niên | `30` | mạnh | tiếp tục theo dõi thay đổi tuyển dụng |
| Căn hộ, khu dân cư | `31` | mạnh, đã mở rộng | đã thêm thiết kế phổ quát, nhà thông minh hỗ trợ chăm sóc và ageing-in-place |
| Mùa, khí hậu, môi trường | `32` | mạnh | xu hướng khí hậu phải gắn mốc thời gian |
| Dịch vụ, khách hàng, đánh giá | `33` | mạnh | tiếp tục liên kết điều kiện lao động với `06` và `24` |

## 4. Các khoảng trống lớn đã được vá

### Công sở lai và nhóm toàn cầu

[`06_workplace_organization_hoesik.md`](06_workplace_organization_hoesik.md) đã nối `재택근무`, `하이브리드근무`, giao tiếp bất đồng bộ, múi giờ, nhóm toàn cầu, chủ nghĩa hiện diện số và liên lạc sau giờ làm vào cùng một mô hình tổ chức.

### Đa dạng nhu cầu ăn uống

[`07_food_table_fermentation_drinking.md`](07_food_table_fermentation_drinking.md) đã bổ sung ăn chay, halal, dị ứng thực phẩm, bữa ăn tập thể và thị trường nguyên liệu quốc tế.

```text
sở thích cá nhân
≠ hạn chế tôn giáo
≠ dị ứng / chống chỉ định y khoa
```

### Nghệ thuật đương đại và thiết chế văn hoá

[`10_arts_music_performance_craft.md`](10_arts_music_performance_craft.md) đã mở rộng từ di sản truyền thống sang bảo tàng, giám tuyển, biennale, hội chợ nghệ thuật, không gian độc lập và bảo tồn nghệ thuật số.

### Lao động sáng tạo và sở hữu trí tuệ

[`13_hallyu_media_platforms.md`](13_hallyu_media_platforms.md) đã mở rộng từ lưu thông Hallyu sang cấu trúc lao động phía sau sản phẩm: tác giả, biên kịch, trợ lý, vũ công, biên đạo, dịch giả và các nghề hậu trường.

Chương tách rõ:

```text
ghi công (credit)
≠ quyền sở hữu / quyền khai thác
≠ doanh thu thực nhận
```

Ngoài ra đã thêm quyền chuyển thể, bất cân xứng dữ liệu với nền tảng, lao động theo dự án, quyền thương lượng và tác động của nội dung tạo sinh ở mức khái niệm.

### Khuyết tật, khả năng tiếp cận và cuối đời

[`26_health_medicine_wellness_body.md`](26_health_medicine_wellness_body.md) đã thêm mô hình trong đó mức tham gia xã hội phụ thuộc cả khả năng cá nhân và môi trường. Khả năng tiếp cận được tách thành vật lý, thông tin, số và xã hội.

Chương cũng đã thêm chăm sóc giảm nhẹ, hospice, lập kế hoạch chăm sóc trước, điều trị duy trì sự sống ở mức khái niệm và đau buồn sau mất mát.

### Nhà ở không rào cản và già hoá tại nơi ở quen thuộc

[`31_apartment_neighborhood_moving_recycling_everyday_life.md`](31_apartment_neighborhood_moving_recycling_everyday_life.md) đã mở rộng `무장애`, thiết kế phổ quát, an toàn phòng tắm, sự phụ thuộc vào thang máy, nhà thông minh hỗ trợ chăm sóc và già hoá tại nơi ở quen thuộc.

### Thể thao thích ứng và giải trí trong xã hội già hoá

[`20_sports_leisure_fan_culture.md`](20_sports_leisure_fan_culture.md) đã bổ sung thể thao thích ứng, khả năng tiếp cận của khán giả, giải trí người cao tuổi và khoảng cách số trong việc đặt sân, mua vé hoặc tham gia cộng đồng.

### Hành trình đô thị không rào cản

[`12_city_consumption_digital_life.md`](12_city_consumption_digital_life.md) đã nối nhà ở, vỉa hè, giao thông, thang máy, điểm đến, kiosk, xác thực và dịch vụ số thành một hành trình thống nhất.

Mô hình quan trọng là:

```text
nhà
→ lối đi
→ giao thông
→ điểm đến
→ giao diện số
→ dịch vụ
→ quay về nhà
```

Một mắt xích thất bại có thể làm toàn bộ hành trình thất bại.

## 5. Ưu tiên cho các vòng tiếp theo

Sau vòng này, thư viện không còn khoảng trống lớn nào buộc phải tạo chương mới. Nên ưu tiên ba việc.

### Học tập và đào tạo lại trong tuổi trưởng thành

`05`, `24` và `30` đã giải thích bằng cấp, thị trường lao động và chuyển tiếp đại học–việc làm. Có thể bổ sung sâu hơn `평생교육`, học lại kỹ năng, chuyển nghề và cách tuổi tác ảnh hưởng quyết định đầu tư vào giáo dục.

### Đồng bộ bảng thuật ngữ

[`17_glossary_and_reference_map.md`](17_glossary_and_reference_map.md) cần tiếp tục nhận các thuật ngữ mới như:

```text
재택근무 / 하이브리드근무
접근성 / 무장애 / thiết kế phổ quát
완화의료 / 호스피스
ageing-in-place
큐레이터 / 비엔날레 / 독립공간
저작권 / 크레딧 / quyền chuyển thể
장애인 스포츠
교통약자 / 디지털 접근성
```

Cột English của glossary vẫn được giữ vì mục đích tra cứu.

### Kiểm toán liên kết chéo và dữ liệu có thời hạn

Sau mỗi vòng mở rộng cần kiểm tra link, thuật ngữ trùng nghĩa và số liệu có mốc thời gian. Đây là công việc bảo trì thư viện, không phải lý do tạo thêm chương.

## 6. Các liên kết chéo bắt buộc phải giữ đồng bộ

```text
04 Gia đình ↔ 29 Nuôi dạy con ↔ 15 Dân số
05 Giáo dục ↔ 30 Đại học ↔ 24 Dịch chuyển xã hội
06 Công sở ↔ 23 Quân đội ↔ 24 Kinh tế ↔ 27 Nhắn tin
07 Ẩm thực ↔ 15 Di cư ↔ 32 Mùa
08 Nhà ở ↔ 31 Căn hộ ↔ 26 Y tế ↔ 15 Già hoá
09 Tôn giáo ↔ 11 Nghi lễ ↔ 04 Gia đình
10 Nghệ thuật/di sản ↔ 13 Hallyu
12 Đô thị ↔ 27 Internet ↔ 31 Căn hộ ↔ 33 Dịch vụ
13 Hallyu ↔ 19 Làm đẹp ↔ 20 Fandom ↔ 24 Kinh tế ↔ 06 Lao động
18 Quan hệ ↔ 03 Ngôn ngữ ↔ 27 Nhắn tin
```

## 7. Chính sách về độ mới của dữ liệu

- số liệu dân số phải ghi **năm dữ liệu**;
- khảo sát phải ghi **định nghĩa quần thể/mẫu**;
- dự báo phải ghi rõ là **dự báo (projection)**;
- chính sách và pháp luật hiện hành phải dùng nguồn đang có hiệu lực;
- nền tảng và tiếng lóng phải có mốc thời gian;
- tuyên bố y khoa phải dựa trên bằng chứng chuyên môn;
- dữ kiện chính trị hiện hành phải được kiểm chứng bằng nguồn mới trước khi cập nhật;
- điều khoản hợp đồng và quyền sở hữu trí tuệ cụ thể phải được kiểm tra theo luật/hợp đồng hiện hành.

## 8. Tiêu chí hoàn thành cho một chương

Một chương được coi là khá hoàn chỉnh khi người đọc có thể:

- giải thích khái niệm bằng lời của mình;
- nêu ít nhất hai cơ chế thay vì chỉ nhớ dữ kiện;
- phân biệt khuôn mẫu nhóm với cá nhân;
- cho ví dụ đời sống;
- nhận ra ít nhất một đánh đổi;
- biết chương nào cần đọc tiếp;
- nhận ra dữ liệu hoặc chính sách nào có thể đã cũ;
- tránh các hiểu lầm phổ biến;
- đọc phần giải thích chủ yếu bằng tiếng Việt nhưng vẫn có đủ từ khoá Anh–Hàn để tra cứu.

Master Knowledge Book không có trạng thái “vĩnh viễn hoàn thành”. Trạng thái mục tiêu là **phạm vi đủ rộng, cơ chế đủ sâu, thuật ngữ nhất quán, tiếng Việt dễ đọc và đường cập nhật rõ ràng**.