# Korean Culture — Bản kiểm toán mức độ bao phủ

> File này không phải chương học riêng. Nó là **bản kiểm toán mức độ bao phủ (coverage audit)** để kiểm soát chất lượng của toàn bộ `korean_culture/01–33`. Thư mục `kiip/` không nằm trong phạm vi kiểm toán này.

## 1. Chuẩn ngôn ngữ đã áp dụng

Vòng chuẩn hoá ngôn ngữ cho phần nội dung chính `01–33` đã được thực hiện theo nguyên tắc:

```text
câu giải thích → tiếng Việt tự nhiên
thuật ngữ cần tra cứu → tiếng Việt (English)
thuật ngữ văn hoá Hàn → giữ Hangul khi cần
câu dài pha tiếng Anh → viết lại hoàn toàn bằng tiếng Việt
```

Ví dụ ưu tiên `cơ chế (mechanism)`, `vòng phản hồi (feedback loop)`, `khả năng tiếp cận (accessibility)` thay vì đặt từ tiếng Anh trực tiếp vào giữa câu tiếng Việt.

Các ngoại lệ được giữ có chủ đích gồm tên riêng, tên sản phẩm/nền tảng, tên file, mã, công thức, từ viết tắt kỹ thuật và cột **English** trong [`17_glossary_and_reference_map.md`](17_glossary_and_reference_map.md). Đây là dữ liệu tra cứu chứ không phải văn xuôi giải thích.

Khi cập nhật chương mới hoặc sửa chương cũ, cần tiếp tục giữ quy ước này; không quay lại kiểu văn xuôi pha Anh–Việt dày đặc.

## 2. Tiêu chí một chương được coi là đủ sâu

Một chủ đề không được coi là hoàn chỉnh chỉ vì có nhiều dữ kiện. Nó phải giúp người đọc trả lời được sáu câu hỏi:

```text
1. Khái niệm (What) — hiện tượng là gì?
2. Nguyên nhân (Why) — vì sao nó xuất hiện hoặc trở nên nổi bật?
3. Cơ chế (Mechanism) — thiết chế, điều kiện vật chất và động lực nào duy trì nó?
4. Biến thiên (Variation) — khác theo thế hệ, vùng, tầng lớp và bối cảnh ra sao?
5. Thay đổi (Change) — công nghệ, kinh tế, luật pháp và dân số làm nó đổi thế nào?
6. Ranh giới (Boundary) — khi nào mô hình này không còn giải thích tốt?
```

Một chương tốt cũng nên có ví dụ đời sống, liên kết chéo, ít nhất một mô hình tư duy, các hiểu lầm phổ biến và cảnh báo khi số liệu/chính sách có thể lỗi thời.

## 3. Bản đồ mức độ bao phủ hiện tại

| Lĩnh vực | Chương | Trạng thái hiện tại | Việc nên làm tiếp |
|---|---|---|---|
| Nền tảng hệ thống văn hoá | `01` | mạnh | chỉ bổ sung khi xuất hiện cơ chế xuyên chương mới |
| Nho giáo, quan hệ, thứ bậc | `02` | mạnh | duy trì ranh giới giữa mô tả và chuẩn tắc |
| Ngôn ngữ, kính ngữ, `눈치`, `정`, `체면` | `03` | mạnh | tránh biến thành sách ngữ pháp tổng quát |
| Gia đình, họ tộc, vòng đời | `04` + `29` | mạnh | tiếp tục theo dõi biến đổi hộ gia đình và chăm sóc |
| Giáo dục, thi cử, bằng cấp | `05` + `30` | mạnh | có thể bổ sung đào tạo lại người trưởng thành |
| Công sở | `06` | mạnh, đã mở rộng | đã có làm việc từ xa/lai, nhóm toàn cầu, giao tiếp bất đồng bộ; tiếp tục cập nhật theo thực tế công nghệ |
| Ẩm thực | `07` | mạnh, đã mở rộng | đã thêm ăn chay, halal, dị ứng và bữa ăn tập thể đa dạng; có thể bổ sung an toàn thực phẩm khi cần |
| Nhà ở, hanok, không gian | `08` + `31` | mạnh, đã mở rộng | `31` đã thêm thiết kế không rào cản, an toàn phòng tắm và già hoá tại nơi ở quen thuộc |
| Tôn giáo và thế giới quan | `09` | mạnh | chỉ thêm phong trào mới khi có nguồn học thuật tốt |
| Nghệ thuật, thủ công, di sản | `10` | mạnh, đã mở rộng | đã thêm bảo tàng, giám tuyển, biennale, art fair, không gian độc lập và nghệ thuật số |
| Lễ Tết, nghi lễ, trò chơi | `11` | mạnh | giữ liên kết với gia đình và vùng miền |
| Đô thị, tiêu dùng, đời sống số | `12` | mạnh | khả năng tiếp cận kiosk đã có; có thể mở rộng giao thông tiếp cận và thiết kế đô thị |
| Hallyu, truyền thông, nền tảng | `13` | mạnh | lao động sáng tạo, hợp đồng và phân phối quyền sở hữu trí tuệ vẫn là khoảng trống lớn nhất |
| Vùng miền, Jeju, bán đảo | `14` | mạnh | tránh biến khác biệt vùng thành định kiến tính cách |
| Dân số, già hoá, di cư | `15` | mạnh | mọi số liệu phải ghi năm, quần thể và mẫu số |
| Liên hệ giữa các hệ thống | `16` | mạnh | cập nhật khi cơ chế mới xuất hiện |
| Thuật ngữ và bản đồ nguồn | `17` | tốt | tiếp tục đồng bộ thuật ngữ mới |
| Phép lịch sự và quan hệ đời thường | `18` | mạnh | ưu tiên mô tả theo bối cảnh thay vì luật cứng |
| Làm đẹp, thời trang, cơ thể | `19` | mạnh | số liệu về thủ thuật/hình ảnh cơ thể phải ghi rõ quần thể |
| Thể thao, giải trí, fandom | `20` | mạnh | thể thao thích ứng và giải trí người cao tuổi vẫn có thể mở rộng |
| Các lớp lịch sử | `21` | mạnh | không lặp thư viện `korean_history/` |
| Tên, tuổi, siêu dữ liệu xã hội | `22` | mạnh | có thể cập nhật môi trường số và toàn cầu |
| Nghĩa vụ quân sự | `23` | khá mạnh | tránh coi trải nghiệm nam giới là trải nghiệm phổ quát |
| Kinh tế, chaebol, nhà ở, dịch chuyển xã hội | `24` | mạnh | thuế, vay và chính sách phải dùng nguồn hiện hành |
| Xã hội dân sự và không gian công luận | `25` | mạnh về khung phân tích | dữ kiện chính trị hiện hành luôn phải kiểm chứng mới |
| Y tế và văn hoá sức khoẻ | `26` | mạnh, đã mở rộng | đã thêm khả năng tiếp cận, khuyết tật, chăm sóc giảm nhẹ, hospice, cuối đời và đau buồn |
| Internet, nhắn tin, tiếng lóng, meme | `27` | mạnh | tiếng lóng/nền tảng phải có mốc thời gian |
| Quy ước tên riêng | `28` | tốt | giữ nhất quán Việt–Hàn–Anh |
| Nuôi dạy con và chăm sóc | `29` | mạnh | nối chặt với `04`, `05`, `15`, `26` |
| Đại học và thanh niên | `30` | mạnh | tiếp tục theo dõi thay đổi tuyển dụng và nền tảng trường học |
| Căn hộ, khu dân cư | `31` | mạnh, đã mở rộng | đã vá khoảng trống về accessibility và ageing-in-place |
| Mùa, khí hậu, môi trường | `32` | mạnh | mọi xu hướng khí hậu phải gắn mốc thời gian |
| Dịch vụ, khách hàng, đánh giá | `33` | mạnh | tiếp tục liên kết điều kiện lao động với `06` và `24` |

## 4. Những khoảng trống đã được vá trong vòng gần nhất

### Làm việc lai và ranh giới số

[`06_workplace_organization_hoesik.md`](06_workplace_organization_hoesik.md) hiện đã nối `재택근무`, `하이브리드근무`, giao tiếp bất đồng bộ, múi giờ, nhóm toàn cầu, chủ nghĩa hiện diện số và liên lạc sau giờ làm vào cùng một mô hình tổ chức.

Điểm cốt lõi không còn là “làm ở nhà hay ở văn phòng”, mà là tổ chức chuyển tín hiệu từ **sự hiện diện vật lý** sang **trạng thái công việc, tài liệu và đầu ra** như thế nào.

### Đa dạng nhu cầu ăn uống

[`07_food_table_fermentation_drinking.md`](07_food_table_fermentation_drinking.md) đã bổ sung ăn chay, halal, dị ứng thực phẩm, bữa ăn tập thể và thị trường nguyên liệu quốc tế.

Mô hình quan trọng:

```text
sở thích cá nhân
≠ hạn chế tôn giáo
≠ dị ứng / chống chỉ định y khoa
```

Điều này nối ẩm thực với di cư, trường học, công sở và thiết kế dịch vụ.

### Nghệ thuật đương đại và thiết chế văn hoá

[`10_arts_music_performance_craft.md`](10_arts_music_performance_craft.md) không còn chỉ tập trung vào di sản truyền thống. Nội dung đã mở rộng sang bảo tàng, bảo tàng mỹ thuật, giám tuyển, biennale, hội chợ nghệ thuật, không gian độc lập và bảo tồn nghệ thuật số.

Nhờ đó, chương này hiện giải thích cả **cách nghệ thuật được tạo** và **cách nó được nhìn thấy, lưu trữ, định giá và đưa vào ký ức công cộng**.

### Khuyết tật, khả năng tiếp cận và cuối đời

[`26_health_medicine_wellness_body.md`](26_health_medicine_wellness_body.md) đã thêm mô hình trong đó mức tham gia xã hội phụ thuộc cả khả năng cá nhân và môi trường. Khả năng tiếp cận được tách thành vật lý, thông tin, số và xã hội.

Chương cũng đã bổ sung chăm sóc giảm nhẹ, hospice, lập kế hoạch chăm sóc trước, điều trị duy trì sự sống ở mức khái niệm và quá trình đau buồn sau mất mát. Nội dung này mang tính giải thích văn hoá–thiết chế, không phải lời khuyên y tế cá nhân.

### Nhà ở không rào cản và già hoá tại nơi ở quen thuộc

[`31_apartment_neighborhood_moving_recycling_everyday_life.md`](31_apartment_neighborhood_moving_recycling_everyday_life.md) đã mở rộng `무장애`, thiết kế phổ quát, an toàn phòng tắm, sự phụ thuộc vào thang máy, nhà thông minh hỗ trợ chăm sóc và **già hoá tại nơi ở quen thuộc (ageing-in-place)**.

Nhà ở vì vậy không chỉ được đánh giá bằng diện tích và vị trí, mà còn bằng câu hỏi: **một người có khả năng cơ thể thay đổi theo tuổi có thể tiếp tục tự sử dụng không gian đó đến mức nào?**

## 5. Khoảng trống ưu tiên còn lại

### Lao động sáng tạo và sở hữu trí tuệ

Đây hiện là khoảng trống lớn nhất còn lại. `13` đã mạnh về Hallyu, nền tảng, fandom và lưu thông nội dung nhưng cần sâu hơn về:

- biên kịch, hoạ sĩ, tác giả webtoon, vũ công, biên đạo, nhà sản xuất và dịch giả;
- lao động tự do và lao động theo dự án;
- quyền tác giả, quyền khai thác, quyền chuyển thể và ghi công;
- khác biệt giữa **nội dung thành công** và **người tạo nội dung nhận được bao nhiêu giá trị kinh tế**;
- tác động của nền tảng tới quyền thương lượng của người sáng tạo.

Nội dung này nên nối `13 ↔ 06 ↔ 24` thay vì tạo chương mới.

### Thể thao thích ứng và giải trí trong xã hội già hoá

`20` đã mạnh về baseball, chạy bộ, leo núi, golf, esports và fandom nhưng có thể bổ sung:

```text
khả năng tiếp cận cơ sở thể thao
+ thể thao thích ứng
+ hoạt động người cao tuổi
+ chi phí / giao thông / an toàn
→ ai thực sự có thể tham gia đời sống giải trí?
```

### Khả năng tiếp cận đô thị ở cấp toàn hành trình

`12` đã nhận ra vấn đề kiosk và khoảng cách số; `26` và `31` đã có mô hình tiếp cận rõ. Bước sau nên nối thành **hành trình đô thị hoàn chỉnh**:

```text
nhà
→ vỉa hè
→ xe buýt / tàu điện
→ điểm đến
→ kiosk / ứng dụng
→ dịch vụ
→ trở về nhà
```

Một mắt xích không tiếp cận được có thể làm cả hành trình thất bại.

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
13 Hallyu ↔ 19 Làm đẹp ↔ 20 Fandom ↔ 24 Kinh tế
18 Quan hệ ↔ 03 Ngôn ngữ ↔ 27 Nhắn tin
```

Nếu một chương thay mô hình tư duy mà chương phụ thuộc không được cập nhật, thư viện sẽ dần mâu thuẫn nội bộ.

## 7. Những thứ cố ý không tách thành chương riêng

Không nên chia thư viện thành quá nhiều file nhỏ. Các chủ đề sau hiện vẫn phù hợp hơn khi nằm trong chương lớn:

- quán cà phê → `12`;
- thú cưng → `15`/`18`;
- đám cưới/tang lễ → `04`/`18`;
- buồng chụp ảnh tự động → `19`/`18`;
- nhóm chạy bộ → `20`;
- kiosk → `12`/`15`;
- thực phẩm bổ sung → `26`;
- màu sắc cá nhân → `19`;
- văn hoá đánh giá → `33` + `12`/`27`;
- thiết kế phổ quát → `12`/`26`/`31`;
- chăm sóc cuối đời → `26` + `04`.

Chỉ nên tạo chương mới khi chủ đề có hệ thống nhân quả riêng, đủ chiều sâu và nhiều liên kết chéo đến mức một chương độc lập giúp người đọc hơn là làm tăng chi phí điều hướng.

## 8. Chính sách về độ mới của dữ liệu

Các chương văn hoá rất dễ biến số liệu cũ thành “bản chất Hàn Quốc”. Vì vậy:

- số liệu dân số phải ghi **năm dữ liệu**;
- khảo sát phải ghi **định nghĩa quần thể/mẫu**;
- dự báo phải ghi rõ là **dự báo (projection)**;
- chính sách và pháp luật hiện hành phải dùng nguồn đang có hiệu lực;
- nền tảng và tiếng lóng phải có mốc thời gian vì thay đổi nhanh;
- tuyên bố về hiệu quả y khoa phải dựa trên bằng chứng chuyên môn, không dựa vào độ phổ biến;
- dữ kiện chính trị và không gian công cộng hiện hành phải được kiểm chứng bằng nguồn mới trước khi cập nhật.

## 9. Tiêu chí hoàn thành cho một chương

Một chương được coi là khá hoàn chỉnh khi người đọc có thể:

- giải thích khái niệm bằng lời của mình;
- nêu ít nhất hai cơ chế thay vì chỉ nhớ dữ kiện;
- phân biệt khuôn mẫu nhóm với độ chắc chắn ở từng cá nhân;
- cho ví dụ đời sống;
- nhận ra ít nhất một đánh đổi;
- biết chương nào cần đọc tiếp;
- nhận ra dữ liệu hoặc chính sách nào có thể đã cũ;
- tránh các hiểu lầm phổ biến;
- đọc phần giải thích chủ yếu bằng tiếng Việt mà vẫn có đủ từ khoá Anh–Hàn để tra cứu.

Master Knowledge Book không có trạng thái “vĩnh viễn hoàn thành” vì văn hoá tiếp tục thay đổi. Trạng thái mục tiêu là **phạm vi đủ rộng, cơ chế đủ sâu, thuật ngữ nhất quán, tiếng Việt dễ đọc và đường cập nhật rõ ràng**.