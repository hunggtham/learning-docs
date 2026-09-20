# Korean Culture — Bản kiểm toán mức độ bao phủ

> File này không phải chương học riêng. Nó là **bản kiểm toán mức độ bao phủ và độ sâu (coverage + depth audit)** cho toàn bộ `korean_culture/01–33`. Thư mục `kiip/` không nằm trong phạm vi kiểm toán này.

## 1. Chuẩn ngôn ngữ hiện hành

Phần nội dung chính `01–33` dùng tiếng Việt làm ngôn ngữ giải thích. Tiếng Anh chỉ giữ như từ khoá bổ sung khi hữu ích cho tra cứu; thuật ngữ văn hoá Hàn được giữ bằng Hangul khi cần.

```text
câu giải thích → tiếng Việt tự nhiên
thuật ngữ cần tra cứu → tiếng Việt (English)
thuật ngữ văn hoá Hàn → giữ Hangul khi cần
câu dài pha tiếng Anh → viết lại hoàn toàn bằng tiếng Việt
```

Các ngoại lệ có chủ đích gồm tên riêng, tên sản phẩm/nền tảng, mã, công thức, từ viết tắt kỹ thuật, tên file và cột **English** trong [`17_glossary_and_reference_map.md`](17_glossary_and_reference_map.md).

## 2. Tiêu chí một chương được coi là đủ sâu

Một chủ đề không được coi là hoàn chỉnh chỉ vì có nhiều dữ kiện. Nó phải giúp người đọc trả lời được ít nhất mười một câu hỏi:

```text
1. Khái niệm — hiện tượng là gì?
2. Nguyên nhân — vì sao nó xuất hiện hoặc trở nên nổi bật?
3. Cơ chế — thiết chế, điều kiện vật chất và động lực nào duy trì nó?
4. Biến thiên — khác theo thế hệ, vùng, tầng lớp và bối cảnh ra sao?
5. Thay đổi — công nghệ, kinh tế, luật pháp và dân số làm nó đổi thế nào?
6. Ranh giới — khi nào mô hình này không còn giải thích tốt?
7. Thất bại — hệ thống hỏng ở đâu khi có ngoại lệ hoặc cú sốc?
8. Chuyển tiếp — hiện tượng thay đổi thế nào qua vòng đời hoặc giữa các thiết chế?
9. Đo lường — ta biết điều này bằng dữ liệu nào và dữ liệu bỏ sót gì?
10. Đánh đổi — lợi ích của cơ chế đi kèm chi phí nào?
11. Liên kết — thay đổi ở chương này phản hồi sang chương nào khác?
```

Mục tiêu là biến mỗi chương từ “mô tả hiện tượng” thành **mô hình giải thích có thể tái sử dụng**.

## 3. Bản đồ mức độ bao phủ hiện tại

| Lĩnh vực | Chương | Trạng thái hiện tại | Việc nên làm tiếp |
|---|---|---|---|
| Nền tảng hệ thống văn hoá | `01` | mạnh | chỉ bổ sung khi có cơ chế xuyên chương mới |
| Nho giáo, quan hệ, thứ bậc | `02` | mạnh | giữ ranh giới giữa mô tả và chuẩn tắc |
| Ngôn ngữ, kính ngữ, `눈치`, `정`, `체면` | `03` | rất mạnh | đã có giao tiếp đa ngôn ngữ, mơ hồ tác nhân, giao tiếp vòng kín và dịch kỹ thuật |
| Gia đình, họ tộc, vòng đời | `04` + `29` | rất mạnh | tiếp tục theo dõi biến đổi chăm sóc và quyền tự chủ |
| Giáo dục, thi cử, bằng cấp | `05` + `30` | rất mạnh | đã có học tập suốt đời, chuyển nghề, kỹ năng chuyển giao và hệ ghép nối đại học–việc làm |
| Công sở | `06` | mạnh | đồng bộ với `03`, `05`, `23`, `29`, `30` khi cập nhật |
| Ẩm thực | `07` | rất mạnh sau vòng mới | đã thêm chuỗi cung ứng, chuỗi lạnh, truy xuất, công suất nhà hàng, giao hàng và lãng phí thực phẩm |
| Nhà ở, hanok, không gian | `08` + `31` | rất mạnh sau vòng mới | đã thêm vỏ công trình, thông gió, âm học, bảo trì, sự cố dây chuyền và vòng đời hạ tầng |
| Tôn giáo và thế giới quan | `09` | mạnh | có thể đào sâu thiết chế tôn giáo hiện đại, từ thiện, thế tục hoá và ranh giới giữa tín ngưỡng–nghi lễ–tổ chức |
| Nghệ thuật, thủ công, di sản | `10` | rất mạnh sau vòng mới | đã thêm kinh tế lao động sáng tạo, tài trợ, cấu trúc quyền, bảo quản phòng ngừa và bảo tồn số |
| Lễ Tết, nghi lễ, trò chơi | `11` | mạnh | có thể đào sâu quá trình giản lược nghi lễ, thương mại hoá và thích nghi trong gia đình đa dạng |
| Đô thị, tiêu dùng, đời sống số | `12` | mạnh | đã có hành trình đô thị không rào cản và khả năng tiếp cận số |
| Hallyu, truyền thông, nền tảng | `13` | mạnh | đã có lao động sáng tạo, quyền tác giả, quyền chuyển thể và phân phối giá trị; giữ đồng bộ với `10` |
| Vùng miền, Jeju, bán đảo | `14` | rất mạnh | đã có thị trường lao động vùng, thiết chế neo, dân số hoạt động, ngưỡng dịch vụ và di cư trở về |
| Dân số, già hoá, di cư | `15` | rất mạnh | đã có hợp đồng thế hệ, độ trễ thiết chế, ngưỡng dịch vụ và chuỗi hội nhập di cư |
| Liên hệ giữa các hệ thống | `16` | rất mạnh | cần đồng bộ các liên hệ mới từ `07`, `08`, `10`, `31`, `32` |
| Thuật ngữ và bản đồ nguồn | `17` | tốt | cần đồng bộ thuật ngữ mới sau mỗi vòng tăng sâu |
| Phép lịch sự và quan hệ đời thường | `18` | rất mạnh | đã có ngân sách quan hệ, liên kết mạnh/yếu, ranh giới, sửa chữa quan hệ và mệt mỏi quan hệ |
| Làm đẹp, thời trang, cơ thể | `19` | mạnh | có thể đào sâu ranh giới tiêu dùng–y khoa, thuật toán hình ảnh và năng lực đọc bằng chứng |
| Thể thao, giải trí, fandom | `20` | mạnh | đã có thể thao thích ứng, giải trí người cao tuổi và bất bình đẳng thời gian |
| Các lớp lịch sử | `21` | rất mạnh | đã có ký ức gia đình, hạ tầng ký ức, thành phố như bản thảo viết chồng và nguồn gốc tư liệu |
| Tên, tuổi, siêu dữ liệu xã hội | `22` | rất mạnh | đã có tên pháp lý/hiển thị, La-tinh hoá, danh tính số và tối thiểu hoá dữ liệu |
| Nghĩa vụ quân sự | `23` | rất mạnh | đã có tái hội nhập, chi phí khởi động lại, chuyển giao kỹ năng, mạng quan hệ và chi phí lan truyền |
| Kinh tế, chaebol, nhà ở, dịch chuyển xã hội | `24` | rất mạnh | đã có bảng cân đối hộ, thanh khoản, chi phí cố định, tương quan rủi ro và mạng bảo hiểm gia đình |
| Xã hội dân sự và không gian công luận | `25` | mạnh về khung phân tích | dữ kiện chính trị hiện hành luôn phải kiểm chứng mới |
| Y tế và văn hoá sức khoẻ | `26` | mạnh | đã có khuyết tật, khả năng tiếp cận, chăm sóc giảm nhẹ và cuối đời |
| Internet, nhắn tin, tiếng lóng, meme | `27` | rất mạnh | đã có đề xuất thuật toán, thiên lệch tham gia, nguồn gốc, quản trị cộng đồng và khóa mạng lưới |
| Quy ước tên riêng | `28` | tốt | giữ nhất quán Việt–Hàn–Anh |
| Nuôi dạy con và chăm sóc | `29` | rất mạnh | đã có chất lượng chăm trẻ, trẻ ốm, nghỉ chăm con, vai trò cha và tải quản lý vô hình |
| Đại học và thanh niên | `30` | rất mạnh | đã có đăng ký môn, GPA, bài tập nhóm, phòng nghiên cứu, thực tập và nhà ở sinh viên |
| Căn hộ, khu dân cư | `31` | rất mạnh sau vòng mới | đã thêm quản trị vòng đời, quỹ dự phòng, nước–đường ống, thông gió, năng lượng và khả năng phục hồi sự cố |
| Mùa, khí hậu, môi trường | `32` | rất mạnh sau vòng mới | đã thêm phân bố khí hậu, phenology, mưa cực đoan, đảo nhiệt, tính dễ tổn thương và thích nghi |
| Dịch vụ, khách hàng, đánh giá | `33` | mạnh | ưu tiên tăng sâu về công suất dịch vụ, xếp hàng, SLA, phục hồi dịch vụ và điều kiện lao động |

## 4. Những nâng cấp độ sâu mới nhất

### `07` — ẩm thực đã trở thành một hệ thống vật chất hoàn chỉnh

Chương [`07_food_table_fermentation_drinking.md`](07_food_table_fermentation_drinking.md) không còn chỉ giải thích món ăn và phép tắc. Nó hiện đi theo hai chuỗi song song:

```text
chuỗi vật chất:
nông nghiệp / đánh bắt / nhập khẩu
→ thu mua
→ chợ đầu mối
→ chuỗi lạnh
→ bếp / siêu thị / nhà hàng
→ giao hàng
→ người ăn
→ rác / tái chế

chuỗi thông tin:
xuất xứ
→ thành phần
→ hạn dùng
→ truy xuất
→ thương hiệu
→ đánh giá
```

Chương cũng phân tích công suất bếp, cú sốc cầu do quán lan truyền, bếp trung tâm, bao bì, lãng phí thực phẩm, an toàn thực phẩm và đánh đổi giữa hiệu quả–dự phòng của nguồn cung.

### `08` — nhà ở đã chuyển từ “không gian” sang hệ môi trường

[`08_home_space_hanok_clothing_aesthetics.md`](08_home_space_hanok_clothing_aesthetics.md) hiện nối `온돌`, hanok và căn hộ với vật lý công trình:

```text
vỏ công trình
+ cách nhiệt
+ cửa sổ
+ thông gió
+ độ ẩm
+ âm học
+ ánh sáng
+ khả năng tiếp cận
→ trải nghiệm sống
```

Điểm quan trọng là nhà ở được đọc như một hệ thống nhiệt–không khí–ánh sáng–âm thanh–chăm sóc, không chỉ như kiểu trang trí. Chương cũng thêm cầu nhiệt, ngưng tụ, quyền riêng tư âm học, làm việc tại nhà, khả năng thích nghi với cơ thể theo vòng đời và trang phục như lớp điều nhiệt di động.

### `31` — căn hộ đã có vòng đời vận hành và thất bại

[`31_apartment_neighborhood_moving_recycling_everyday_life.md`](31_apartment_neighborhood_moving_recycling_everyday_life.md) đã mở rộng từ văn hoá cư dân sang **vận hành hệ thống dùng chung**:

```text
chi phí hiện tại
+ bảo trì phòng ngừa
+ quỹ sửa chữa dài hạn
+ đường ống / bơm / thang máy
+ thông gió / năng lượng
+ quản trị minh bạch
+ dự phòng sự cố
→ độ tin cậy của nơi ở
```

Chương mới phân biệt chi phí thấy ngay với chi phí bị trì hoãn, giải thích sự cố dây chuyền khi điện/nước/thang máy lỗi, và nhấn mạnh rằng tuổi của công trình lẫn tuổi của cư dân có thể cùng tăng nên cần cải tạo kép.

### `32` — mùa đã chuyển thành bài toán thích nghi khí hậu

[`32_seasons_climate_environment_daily_rhythm.md`](32_seasons_climate_environment_daily_rhythm.md) hiện tách rõ:

```text
thời tiết ngắn hạn
≠ khí hậu dài hạn
≠ ký ức cá nhân về “mùa bình thường”
```

Nội dung mới gồm phân bố thay vì chỉ trung bình, hiện tượng học theo mùa (phenology), cường độ mưa và ngưỡng thoát nước, đảo nhiệt đô thị, nắng nóng ban đêm, lao động ngoài trời, nông nghiệp, nghề cá, rủi ro du lịch, thích nghi so với giảm phát thải, khả năng phục hồi, mệt mỏi cảnh báo và bất bình đẳng khí hậu.

### `10` — nghệ thuật đã có kinh tế lao động và bảo tồn số

[`10_arts_music_performance_craft.md`](10_arts_music_performance_craft.md) hiện phân tích tác phẩm qua toàn bộ chuỗi lao động và vòng đời:

```text
sáng tạo
→ sản xuất
→ tài trợ
→ vận chuyển
→ lắp đặt
→ trưng bày
→ ghi công / quyền
→ bảo quản
→ lưu trữ / tái tạo
```

Chương tách rõ `uy tín ≠ khả năng hiển thị ≠ doanh số ≠ thu nhập ròng`, phân biệt sở hữu vật thể với quyền tác giả/quyền khai thác, và thêm bảo quản phòng ngừa, checksum, di chuyển định dạng, mô phỏng môi trường cũ, nguồn gốc/chứng thực và khả năng tiếp cận nghệ thuật.

## 5. Những nâng cấp quan trọng từ các vòng trước vẫn phải giữ

`03` đã có giao tiếp vòng kín, mơ hồ tác nhân và dịch Hàn–Việt–Anh. `05` và `30` đã có học tập suốt đời, chuyển nghề và đại học như hệ ghép nối. `14` đã có việc làm–hạ tầng–dân số vùng. `15` đã có hợp đồng thế hệ và hội nhập di cư. `18` đã có ngân sách quan hệ. `21` đã tách sự kiện–ký ức–công dụng hiện tại. `23` đã có pha tái hội nhập sau nghĩa vụ. `24` đã có kinh tế bảng cân đối hộ. `27` đã có hạ tầng niềm tin trên Internet. `29` đã có hệ chăm sóc với cú sốc và dự phòng.

Những mô hình này không nên bị rút gọn lại khi chỉnh sửa về sau.

## 6. Ưu tiên cho vòng tăng độ sâu tiếp theo

Thư viện hiện không thiếu chủ đề lớn. Nên tiếp tục tăng độ sâu ở những chương còn thiên về mô tả.

### Ưu tiên A — `33`: dịch vụ như hệ thống công suất và phục hồi lỗi

Nên đi sâu:

```text
nhu cầu đến
→ hàng đợi
→ công suất nhân sự / hệ thống
→ thời gian phục vụ
→ lỗi
→ khiếu nại
→ phục hồi dịch vụ
→ đánh giá
```

Đặc biệt cần phân biệt tốc độ trung bình, thời gian chờ ở đuôi phân bố, SLA, quyền của khách hàng và tải lao động cảm xúc phía sau trải nghiệm “nhanh”.

### Ưu tiên B — `09`: tôn giáo như thiết chế xã hội hiện đại

Không chỉ mô tả tín ngưỡng. Nên đào sâu quan hệ giữa niềm tin, thành viên tổ chức, nghi lễ, từ thiện, mạng hỗ trợ, giáo dục, tài chính tổ chức, thế tục hoá và cách thực hành thay theo thế hệ.

### Ưu tiên C — `11`: nghi lễ như giao thức có thể giản lược

Nên phân tích vì sao cùng một lễ có thể rút ngắn, thuê ngoài, chuyển địa điểm hoặc số hoá nhưng vẫn giữ chức năng nhận diện gia đình. Cần tách **hình thức nghi lễ** khỏi **chức năng xã hội**.

### Ưu tiên D — `19`: làm đẹp như thị trường thông tin và rủi ro

Nên tăng chiều sâu về ranh giới mỹ phẩm–thủ thuật–y khoa, bằng chứng hiệu quả, quảng cáo, thuật toán hình ảnh, bộ lọc, tiêu chuẩn cơ thể và chênh lệch quyền lực thông tin giữa người dùng với nhà cung cấp.

## 7. Các liên kết chéo bắt buộc phải giữ đồng bộ

```text
03 Ngôn ngữ ↔ 06 Công sở ↔ 18 Quan hệ ↔ 27 Nhắn tin
04 Gia đình ↔ 29 Nuôi dạy con ↔ 15 Dân số
05 Giáo dục ↔ 30 Đại học ↔ 24 Dịch chuyển xã hội ↔ 06 Công sở
06 Công sở ↔ 23 Quân đội ↔ 24 Kinh tế ↔ 27 Nhắn tin ↔ 29 Chăm sóc
07 Ẩm thực ↔ 12 Giao hàng ↔ 15 Di cư ↔ 32 Khí hậu ↔ 33 Dịch vụ
08 Nhà ở ↔ 31 Căn hộ ↔ 26 Y tế ↔ 15 Già hoá ↔ 24 Tài chính hộ ↔ 32 Khí hậu
09 Tôn giáo ↔ 11 Nghi lễ ↔ 04 Gia đình
10 Nghệ thuật/di sản ↔ 13 Hallyu ↔ 21 Ký ức ↔ 27 Hạ tầng số
12 Đô thị ↔ 14 Vùng ↔ 27 Internet ↔ 31 Căn hộ ↔ 33 Dịch vụ
13 Hallyu ↔ 19 Làm đẹp ↔ 20 Fandom ↔ 24 Kinh tế ↔ 06 Lao động
14 Vùng ↔ 15 Dân số ↔ 24 Kinh tế ↔ 30 Đại học
15 Dân số ↔ 22 Danh tính ↔ 26 Y tế ↔ 29 Chăm sóc
21 Lịch sử ↔ 14 Vùng miền ↔ 11 Nghi lễ ↔ 13 Truyền thông ↔ 25 Không gian công luận
23 Quân đội ↔ 05 Giáo dục ↔ 30 Đại học ↔ 06 Công sở
31 Căn hộ ↔ 32 Khí hậu ↔ 26 Sức khoẻ ↔ 15 Già hoá
```

## 8. Chính sách về độ mới của dữ liệu

- số liệu dân số phải ghi **năm dữ liệu**;
- khảo sát phải ghi **định nghĩa quần thể/mẫu**;
- dự báo phải ghi rõ là **dự báo (projection)**;
- chính sách và pháp luật hiện hành phải dùng nguồn đang có hiệu lực;
- nền tảng và tiếng lóng phải có mốc thời gian;
- tuyên bố y khoa phải dựa trên bằng chứng chuyên môn;
- dữ kiện chính trị hiện hành phải được kiểm chứng bằng nguồn mới trước khi cập nhật;
- điều khoản hợp đồng và quyền sở hữu trí tuệ cụ thể phải được kiểm tra theo luật/hợp đồng hiện hành;
- khi thêm số liệu giáo dục, việc làm hoặc di cư phải giữ nguyên định nghĩa mẫu và không suy rộng quá phạm vi;
- khi dùng ký ức cá nhân hoặc truyền thông để nói về lịch sử, phải tách chúng khỏi bằng chứng lịch sử ở cấp sự kiện;
- số liệu khí hậu phải ghi địa điểm, giai đoạn quan sát, đường cơ sở và nguồn; không dùng một mùa gần đây để suy xu hướng dài hạn;
- quy định an toàn thực phẩm, xuất xứ và ghi nhãn phải dùng nguồn hiện hành thay vì suy từ thói quen văn hoá.

## 9. Tiêu chí hoàn thành cho một chương

Một chương được coi là khá hoàn chỉnh khi người đọc có thể:

- giải thích khái niệm bằng lời của mình;
- nêu ít nhất hai cơ chế thay vì chỉ nhớ dữ kiện;
- phân biệt khuôn mẫu nhóm với cá nhân;
- cho ví dụ đời sống;
- nhận ra ít nhất một đánh đổi;
- chỉ ra ít nhất một tình huống hệ thống thất bại hoặc ngoại lệ;
- mô tả hiện tượng thay đổi qua vòng đời hoặc giữa các thiết chế;
- biết chương nào cần đọc tiếp;
- nhận ra dữ liệu hoặc chính sách nào có thể đã cũ;
- phân biệt dữ kiện, ký ức, diễn giải và truyền thông khi chủ đề liên quan lịch sử;
- xác định phần nào của hệ thống là hạ tầng vật lý, phần nào là thiết chế và phần nào là chuẩn mực;
- tránh các hiểu lầm phổ biến;
- đọc phần giải thích chủ yếu bằng tiếng Việt nhưng vẫn có đủ từ khoá Anh–Hàn để tra cứu.

Master Knowledge Book không có trạng thái “vĩnh viễn hoàn thành”. Trạng thái mục tiêu là **phạm vi đủ rộng, cơ chế đủ sâu, thất bại đủ rõ, thuật ngữ nhất quán, tiếng Việt dễ đọc và đường cập nhật rõ ràng**.