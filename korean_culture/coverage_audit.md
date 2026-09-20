# Korean Culture — Bản kiểm toán mức độ bao phủ

> File này không phải chương học riêng. Nó là **bản kiểm toán mức độ bao phủ và độ sâu (coverage + depth audit)** cho toàn bộ `korean_culture/01–33`. Thư mục `kiip/` không nằm trong phạm vi kiểm toán này.

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
1. Khái niệm — hiện tượng là gì?
2. Nguyên nhân — vì sao nó xuất hiện hoặc trở nên nổi bật?
3. Cơ chế — thiết chế, điều kiện vật chất và động lực nào duy trì nó?
4. Biến thiên — khác theo thế hệ, vùng, tầng lớp và bối cảnh ra sao?
5. Thay đổi — công nghệ, kinh tế, luật pháp và dân số làm nó đổi thế nào?
6. Ranh giới — khi nào mô hình này không còn giải thích tốt?
```

Sau vòng tăng độ sâu hiện tại, mỗi chương quan trọng còn được đánh giá thêm theo năm câu hỏi nâng cao:

```text
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
| Ngôn ngữ, kính ngữ, `눈치`, `정`, `체면` | `03` | rất mạnh sau vòng mới | đã thêm giao tiếp đa ngôn ngữ, mơ hồ tác nhân, giao tiếp vòng kín và dịch kỹ thuật |
| Gia đình, họ tộc, vòng đời | `04` + `29` | rất mạnh | `29` đã thêm cú sốc chăm sóc, tải quản lý vô hình và quyền tự chủ của trẻ |
| Giáo dục, thi cử, bằng cấp | `05` + `30` | rất mạnh | đã thêm học tập suốt đời, chuyển nghề, kỹ năng chuyển giao và đại học như hệ ghép nối |
| Công sở | `06` | mạnh, đã mở rộng | giữ đồng bộ với `03`, `05`, `29`, `30` khi cập nhật giao tiếp và kỹ năng |
| Ẩm thực | `07` | mạnh | có thể bổ sung sâu hơn kinh tế chuỗi cung ứng thực phẩm nếu cần |
| Nhà ở, hanok, không gian | `08` + `31` | mạnh | giữ liên kết với già hoá, di cư và tài chính hộ |
| Tôn giáo và thế giới quan | `09` | mạnh | chỉ thêm phong trào mới khi có nguồn học thuật tốt |
| Nghệ thuật, thủ công, di sản | `10` | mạnh | có thể đào sâu kinh tế sáng tạo và bảo tồn số cùng `13` |
| Lễ Tết, nghi lễ, trò chơi | `11` | mạnh | giữ liên kết với gia đình, du lịch và vùng miền |
| Đô thị, tiêu dùng, đời sống số | `12` | mạnh | đã có hành trình đô thị không rào cản và khả năng tiếp cận số |
| Hallyu, truyền thông, nền tảng | `13` | mạnh | đã có lao động sáng tạo, quyền tác giả, quyền chuyển thể và phân phối giá trị |
| Vùng miền, Jeju, bán đảo | `14` | rất mạnh sau vòng mới | đã thêm thị trường lao động vùng, thiết chế neo, dân số hoạt động, ngưỡng dịch vụ và di cư trở về |
| Dân số, già hoá, di cư | `15` | rất mạnh | đã thêm hợp đồng thế hệ, độ trễ thiết chế, ngưỡng dịch vụ và chuỗi hội nhập di cư |
| Liên hệ giữa các hệ thống | `16` | rất mạnh | đã có 30 mô hình liên hệ và lớp đo lường; cần đồng bộ thêm các mô hình mới từ `03`, `14`, `21`, `23` |
| Thuật ngữ và bản đồ nguồn | `17` | tốt, cần đồng bộ vòng mới | cần thêm thuật ngữ mới từ giao tiếp đa ngôn ngữ, vùng, ký ức và tái hội nhập |
| Phép lịch sự và quan hệ đời thường | `18` | rất mạnh | đã thêm ngân sách quan hệ, liên kết mạnh/yếu, ranh giới, sửa chữa quan hệ và mệt mỏi quan hệ |
| Làm đẹp, thời trang, cơ thể | `19` | mạnh | số liệu về thủ thuật phải ghi rõ quần thể |
| Thể thao, giải trí, fandom | `20` | mạnh | đã có thể thao thích ứng, giải trí người cao tuổi và bất bình đẳng thời gian |
| Các lớp lịch sử | `21` | rất mạnh sau vòng mới | đã thêm ký ức gia đình, hạ tầng ký ức, thành phố như bản thảo viết chồng và nguồn gốc tư liệu |
| Tên, tuổi, siêu dữ liệu xã hội | `22` | rất mạnh | đã thêm tên pháp lý/hiển thị, La-tinh hoá, danh tính số và tối thiểu hoá dữ liệu |
| Nghĩa vụ quân sự | `23` | rất mạnh sau vòng mới | đã thêm tái hội nhập, chi phí khởi động lại, chuyển giao kỹ năng, mạng quan hệ và chi phí lan truyền |
| Kinh tế, chaebol, nhà ở, dịch chuyển xã hội | `24` | rất mạnh | đã thêm bảng cân đối hộ, thanh khoản, chi phí cố định, tương quan rủi ro và mạng bảo hiểm gia đình |
| Xã hội dân sự và không gian công luận | `25` | mạnh về khung phân tích | dữ kiện chính trị hiện hành luôn phải kiểm chứng mới |
| Y tế và văn hoá sức khoẻ | `26` | mạnh | đã có khuyết tật, khả năng tiếp cận, chăm sóc giảm nhẹ và cuối đời |
| Internet, nhắn tin, tiếng lóng, meme | `27` | rất mạnh | đã thêm đề xuất thuật toán, thiên lệch tham gia, nguồn gốc, quản trị cộng đồng và khóa mạng lưới |
| Quy ước tên riêng | `28` | tốt | giữ nhất quán Việt–Hàn–Anh |
| Nuôi dạy con và chăm sóc | `29` | rất mạnh | đã thêm chất lượng chăm trẻ, trẻ ốm, nghỉ chăm con, vai trò cha và tải quản lý vô hình |
| Đại học và thanh niên | `30` | rất mạnh | đã thêm đăng ký môn, GPA, bài tập nhóm, phòng nghiên cứu, thực tập và nhà ở sinh viên |
| Căn hộ, khu dân cư | `31` | mạnh | đã có thiết kế phổ quát, nhà thông minh hỗ trợ chăm sóc và già hoá tại nơi ở quen thuộc |
| Mùa, khí hậu, môi trường | `32` | mạnh | xu hướng khí hậu phải gắn mốc thời gian |
| Dịch vụ, khách hàng, đánh giá | `33` | mạnh | tiếp tục liên kết điều kiện lao động với `06`, `12`, `24` |

## 4. Những nâng cấp độ sâu đã hoàn thành trong chu kỳ hiện tại

### Giáo dục không còn kết thúc ở đại học

[`05_education_exams_credentials.md`](05_education_exams_credentials.md) hiện không chỉ giải thích `수능`, `학원`, `학벌` mà còn đi sâu vào:

```text
평생교육
→ kỹ năng mất giá với tốc độ khác nhau
→ 재교육 / chuyển nghề
→ bằng cấp vs chứng chỉ vs portfolio vs kinh nghiệm
→ năng lực tái đào tạo
→ chuyển giao học tập
→ AI và kỹ năng kiểm chứng
```

Điểm mới quan trọng là tách **tri thức**, **tín hiệu** và **bằng chứng làm được việc**.

### Đại học như một hệ thống ghép nối

[`30_school_university_youth_campus_culture.md`](30_school_university_youth_campus_culture.md) đã mở rộng từ văn hoá campus sang cơ chế vận hành:

```text
수강신청 → phân bổ tài nguyên
학점 → phản hồi + tín hiệu
조별과제 → chi phí phối hợp
연구실 → cố vấn + bất cân xứng quyền lực
인턴 → thử hai chiều
통학 / 기숙사 / 자취 → địa lý của vốn xã hội
취준 → trạng thái chuyển tiếp vòng đời
```

Điều này giúp nối campus với công sở, nhà ở và thị trường lao động thay vì xem trường đại học như một đảo tách biệt.

### Nuôi con như một hệ thống có ngoại lệ và dự phòng

[`29_childhood_parenting_care_institutions.md`](29_childhood_parenting_care_institutions.md) đã vượt khỏi mô hình “cha mẹ đầu tư cho con” và thêm chất lượng chăm trẻ, cú sốc khi trẻ ốm, khác biệt giữa quyền nghỉ chính thức và chi phí không chính thức, vai trò người cha, tải quản lý vô hình, dữ liệu/camera trong nuôi con, quyền tự chủ tăng dần và mạng chăm sóc giữa gia đình–trường–y tế.

### Dân số như hợp đồng giữa các thế hệ

[`15_contemporary_change_demography_migration.md`](15_contemporary_change_demography_migration.md) đã thêm tỷ số phụ thuộc và giới hạn của nó, hợp đồng giữa các thế hệ, độ trễ thiết chế trong già hoá nhanh, nhà ở như hạ tầng vòng đời, di cư như một đường ống nhiều giai đoạn, năng lực hiểu thiết chế của người di cư, thế hệ thứ hai, chuỗi chăm sóc xuyên biên giới và hiệu ứng ngưỡng khi dịch vụ địa phương đóng.

### Danh tính từ quan hệ trực tiếp sang hệ thống số

[`22_names_age_identity_social_metadata.md`](22_names_age_identity_social_metadata.md) đã mở rộng từ tên–tuổi sang:

```text
tên pháp lý
≠ tên hiển thị
≠ danh xưng
≠ biệt danh / tài khoản số
```

Chương cũng nối La-tinh hoá tên, người nước ngoài, danh xưng công sở toàn cầu, nickname, phân nhóm theo tuổi và tối thiểu hoá dữ liệu.

### Kinh tế hộ gia đình đã được tách khỏi khái niệm “thu nhập” đơn giản

[`24_economy_chaebol_housing_status_mobility.md`](24_economy_chaebol_housing_status_mobility.md) hiện phân biệt `thu nhập ≠ dòng tiền ≠ tài sản ≠ thanh khoản`, đồng thời thêm chi phí cố định, khả năng phục vụ nợ, cú sốc thất nghiệp, tương quan giữa hai nguồn thu nhập, gia đình như mạng bảo hiểm tư nhân và nhiều lớp của “độc lập kinh tế”.

### Quan hệ đời thường đã chuyển từ phép lịch sự sang kinh tế của mạng xã hội

[`18_daily_etiquette_gifts_relationships.md`](18_daily_etiquette_gifts_relationships.md) hiện dùng mô hình **ngân sách quan hệ** gồm thời gian, sự chú ý, tiền, sự hiện diện và năng lượng cảm xúc; đồng thời phân tích liên kết mạnh/yếu, cách nói không, mệt mỏi quan hệ, suy giảm quan hệ khi mất không gian chung và sửa chữa quan hệ.

### Internet đã chuyển từ “văn hoá meme” sang mô hình hạ tầng niềm tin

[`27_internet_communities_messaging_slang_memes.md`](27_internet_communities_messaging_slang_memes.md) hiện tách rõ:

```text
phổ biến
≠ đại diện
≠ đáng tin
≠ đúng
```

Nội dung đi sâu vào vòng phản hồi đề xuất, thiên lệch tham gia, phễu lan truyền, cảm xúc mạnh và chỉ số tương tác, phả hệ nguồn, truyền thông tổng hợp, hiệu chuẩn niềm tin, tính độc lập của nguồn, nhiều tài khoản, khóa mạng lưới và quản trị cộng đồng.

### Giao tiếp đa ngôn ngữ đã được tách khỏi “dịch đúng từ”

[`03_language_honorifics_nunchi_jeong_face.md`](03_language_honorifics_nunchi_jeong_face.md) hiện phân tích thêm:

```text
đã nghe
≠ đã hiểu
≠ đã đồng ý
≠ đã cam kết hoàn thành
```

và các cơ chế: chủ ngữ bị lược bỏ, mơ hồ tác nhân, giao tiếp vòng kín, nhật ký quyết định, dịch Hàn–Việt–Anh, trôi thuật ngữ, từ vay mượn trong công sở, phản biện hướng lên và quy tắc khi nào nên dựa vào `눈치` hay phải xác nhận rõ.

Điểm mới là xem giao tiếp như **hệ thống truyền dữ liệu có quan hệ, ngữ cảnh và trạng thái cam kết**, chứ không chỉ như từ vựng + ngữ pháp.

### Vùng miền đã được nâng thành hệ thống việc làm–hạ tầng–di chuyển

[`14_regions_jeju_local_identity_peninsula.md`](14_regions_jeju_local_identity_peninsula.md) hiện không chỉ nói về phương ngữ và bản sắc. Chương đã thêm:

- nén không gian–thời gian do giao thông;
- đại học, bệnh viện và cơ quan công như thiết chế neo;
- thị trường lao động địa phương và quyết định ở lại/rời đi;
- chuỗi `đại học → thực tập → việc làm → giữ người trẻ`;
- `귀향`, `귀촌`, `귀농` và bản sắc đa địa phương;
- dân số hoạt động khác dân số đăng ký;
- hiệu ứng ngưỡng khi dịch vụ địa phương đóng;
- địa lý do thuật toán định hình;
- tự củng cố không gian qua nhà ở và giáo dục;
- khả năng phục hồi của vùng chuyên môn hoá.

### Lịch sử đã chuyển từ “các lớp quá khứ” sang cơ chế tạo ký ức

[`21_historical_layers_ancient_to_modern.md`](21_historical_layers_ancient_to_modern.md) hiện phân biệt:

```text
sự kiện
≠ ký ức về sự kiện
≠ công dụng của câu chuyện trong hiện tại
```

Chương đã thêm ký ức gia đình, sự im lặng, hạ tầng ký ức, thành phố như bản thảo viết chồng, khác biệt giữa lịch sử trường học–gia đình–truyền thông, vị trí ký ức theo thế hệ, ký ức về công nghiệp hoá và năng lực truy nguồn tư liệu trong thời đại số.

### Nghĩa vụ quân sự đã có toàn bộ pha tái hội nhập

[`23_military_conscription_service_culture.md`](23_military_conscription_service_culture.md) hiện mở rộng từ nhập ngũ–xuất ngũ sang:

```text
trước phục vụ
→ gián đoạn
→ trải nghiệm trong thiết chế
→ xuất ngũ
→ khởi động lại kỹ năng và mạng quan hệ
→ tái hội nhập trường học / công việc
```

Chương tách kỹ năng bền, kỹ năng cần duy trì và kỹ năng biến động nhanh; phân tích chuyển đổi từ chuỗi chỉ huy sang nhóm ngang hàng, phương sai trải nghiệm giữa các đơn vị, mạng đồng đội, chi phí lan truyền sang gia đình và bài toán lập lịch nghề nghiệp.

### Chương liên hệ đã chuyển từ “tổng hợp” sang công cụ phân tích

[`16_connections_mental_models_misconceptions.md`](16_connections_mental_models_misconceptions.md) hiện có 30 liên hệ xuyên chương. Khung phân tích đã được nâng lên sáu lớp:

```text
vật chất
→ thiết chế
→ quan hệ
→ biểu tượng
→ lịch sử
→ đo lường
```

Điều này buộc người đọc hỏi không chỉ “cơ chế là gì?” mà còn “ta biết điều đó bằng dữ liệu nào?”.

## 5. Ưu tiên cho vòng tăng độ sâu tiếp theo

Sau vòng này, nhóm `03`, `14`, `21`, `23` không còn là khoảng trống chính. Nên chuyển sang các chương còn mạnh về mô tả nhưng có thể đào sâu hơn về chuỗi cung ứng, bảo tồn và thích nghi.

### Ưu tiên A — `07`: ẩm thực như hệ thống chuỗi cung ứng

Nên nối:

```text
nông nghiệp / đánh bắt
→ chợ đầu mối
→ chuỗi lạnh
→ nhà hàng / siêu thị / giao hàng
→ an toàn thực phẩm
→ lãng phí thực phẩm
```

Mục tiêu là giải thích vì sao món ăn và thói quen ăn thay đổi khi logistics, hộ gia đình và nhập khẩu thay đổi.

### Ưu tiên B — `10` + `13`: kinh tế sáng tạo và bảo tồn số

Nên đào sâu vòng đời của tác phẩm từ sáng tạo, tài trợ, lưu trữ, quyền khai thác đến bảo tồn; đồng thời tách rõ vật thể gốc, bản sao số, quyền sở hữu và quyền truy cập.

### Ưu tiên C — `08` + `31`: nhà ở như hệ thống năng lượng và chăm sóc

Có thể đào sâu sưởi/làm mát, chất lượng không khí trong nhà, già hoá, cảm biến, bảo trì, chi phí năng lượng và cách căn hộ trở thành hạ tầng chăm sóc dài hạn.

### Ưu tiên D — `32`: mùa và khí hậu như ràng buộc đang dịch chuyển

Không chỉ mô tả bốn mùa; cần đi sâu cách thay đổi nhiệt độ, mưa cực đoan, thời gian nở hoa, mùa du lịch và nông nghiệp làm lịch văn hoá phải điều chỉnh. Mọi số liệu khí hậu phải gắn mốc thời gian và nguồn.

## 6. Các liên kết chéo bắt buộc phải giữ đồng bộ

```text
03 Ngôn ngữ ↔ 06 Công sở ↔ 18 Quan hệ ↔ 27 Nhắn tin
04 Gia đình ↔ 29 Nuôi dạy con ↔ 15 Dân số
05 Giáo dục ↔ 30 Đại học ↔ 24 Dịch chuyển xã hội ↔ 06 Công sở
06 Công sở ↔ 23 Quân đội ↔ 24 Kinh tế ↔ 27 Nhắn tin ↔ 29 Chăm sóc
07 Ẩm thực ↔ 15 Di cư ↔ 32 Mùa
08 Nhà ở ↔ 31 Căn hộ ↔ 26 Y tế ↔ 15 Già hoá ↔ 24 Tài chính hộ
09 Tôn giáo ↔ 11 Nghi lễ ↔ 04 Gia đình
10 Nghệ thuật/di sản ↔ 13 Hallyu
12 Đô thị ↔ 14 Vùng ↔ 27 Internet ↔ 31 Căn hộ ↔ 33 Dịch vụ
13 Hallyu ↔ 19 Làm đẹp ↔ 20 Fandom ↔ 24 Kinh tế ↔ 06 Lao động
14 Vùng ↔ 15 Dân số ↔ 24 Kinh tế ↔ 30 Đại học
15 Dân số ↔ 22 Danh tính ↔ 26 Y tế ↔ 29 Chăm sóc
21 Lịch sử ↔ 14 Vùng miền ↔ 11 Nghi lễ ↔ 13 Truyền thông ↔ 25 Không gian công luận
23 Quân đội ↔ 05 Giáo dục ↔ 30 Đại học ↔ 06 Công sở
```

## 7. Chính sách về độ mới của dữ liệu

- số liệu dân số phải ghi **năm dữ liệu**;
- khảo sát phải ghi **định nghĩa quần thể/mẫu**;
- dự báo phải ghi rõ là **dự báo (projection)**;
- chính sách và pháp luật hiện hành phải dùng nguồn đang có hiệu lực;
- nền tảng và tiếng lóng phải có mốc thời gian;
- tuyên bố y khoa phải dựa trên bằng chứng chuyên môn;
- dữ kiện chính trị hiện hành phải được kiểm chứng bằng nguồn mới trước khi cập nhật;
- điều khoản hợp đồng và quyền sở hữu trí tuệ cụ thể phải được kiểm tra theo luật/hợp đồng hiện hành;
- khi thêm số liệu giáo dục, việc làm hoặc di cư phải giữ nguyên định nghĩa mẫu và không suy rộng quá phạm vi;
- khi dùng ký ức cá nhân hoặc truyền thông để nói về lịch sử, phải tách chúng khỏi bằng chứng lịch sử ở cấp sự kiện.

## 8. Tiêu chí hoàn thành cho một chương

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
- tránh các hiểu lầm phổ biến;
- đọc phần giải thích chủ yếu bằng tiếng Việt nhưng vẫn có đủ từ khoá Anh–Hàn để tra cứu.

Master Knowledge Book không có trạng thái “vĩnh viễn hoàn thành”. Trạng thái mục tiêu là **phạm vi đủ rộng, cơ chế đủ sâu, thất bại đủ rõ, thuật ngữ nhất quán, tiếng Việt dễ đọc và đường cập nhật rõ ràng**.