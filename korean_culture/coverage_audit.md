# Korean Culture — Bản kiểm toán mức độ bao phủ

> File này không phải chương học riêng. Nó là **bản kiểm toán mức độ bao phủ (coverage audit)** để tránh việc Master Knowledge Book phát triển theo cảm tính, lặp chủ đề hoặc bỏ sót hệ thống con quan trọng. Phạm vi kiểm toán là các file `01`–`33`, không tính `kiip/`.

## Tiêu chí đánh giá

Một lĩnh vực được coi là bao phủ tốt khi không chỉ liệt kê dữ kiện mà trả lời được sáu câu hỏi:

```text
1. Khái niệm (What) — hiện tượng/khái niệm là gì?
2. Nguyên nhân (Why) — tại sao nó xuất hiện hoặc trở nên nổi bật?
3. Cơ chế (Mechanism) — thiết chế, điều kiện vật chất hoặc động lực nào duy trì nó?
4. Biến thiên (Variation) — khác theo thế hệ, tầng lớp, vùng và bối cảnh ra sao?
5. Thay đổi (Change) — công nghệ, kinh tế hoặc pháp luật làm nó đổi thế nào?
6. Ranh giới (Boundary) — khi nào cách giải thích này không còn đúng?
```

Mỗi chương cũng nên có ít nhất một **mô hình tư duy (Mental Model)**, phần **hiểu lầm phổ biến (Common Misconceptions)**, từ khoá Hàn–Anh–Việt và liên kết chéo khi khái niệm phụ thuộc vào chương khác.

## Bản đồ mức độ bao phủ hiện tại

| Lĩnh vực | Chương chính | Trạng thái | Khoảng trống còn lại |
|---|---|---|---|
| Nền tảng hệ thống văn hoá | `01` | mạnh | tiếp tục ghi mốc thời gian cho số liệu hiện hành khi thêm mới |
| Các lớp lịch sử | `21` | mạnh | có thể bổ sung sâu ký ức đời thường về thuộc địa/chiến tranh nhưng không lặp `korean_history/` |
| Nho giáo và thứ bậc | `02` | mạnh | cần giữ rõ ranh giới giữa mô tả và chuẩn tắc |
| Tên, tuổi, siêu dữ liệu xã hội | `22` | mạnh | có thể bổ sung cách gọi tên trong môi trường số/toàn cầu |
| Ngôn ngữ, kính ngữ, khái niệm quan hệ | `03` | mạnh | phát âm/phương ngữ để `14`, không biến chương thành sách ngữ pháp |
| Gia đình, họ tộc, vòng đời | `04` + `29` | mạnh | hộ gia đình phi truyền thống có thể bổ sung khi có nguồn phù hợp |
| Giáo dục và bằng cấp | `05` + `30` | mạnh | lộ trình nghề, đào tạo lại người trưởng thành cần theo dõi thêm |
| Công sở | `06` | mạnh | làm việc từ xa/lai và nhóm toàn cầu có thể cập nhật theo thời gian |
| Vòng đời nghĩa vụ quân sự | `23` | khá mạnh | tránh biến trải nghiệm của nam giới thành trải nghiệm phổ quát của mọi công dân |
| Kinh tế, nhà ở, dịch chuyển xã hội | `24` | mạnh sau vòng hiện tại | thuế/vay/chính sách phải dùng nguồn hiện hành, không ghi cứng |
| Ẩm thực và uống rượu | `07` | mạnh | có thể thêm an toàn thực phẩm, dị ứng và thích nghi ăn chay |
| Mùa và khí hậu | `32` | mạnh | xu hướng khí hậu cần ghi mốc thời gian nếu đưa số liệu |
| Nhà ở, hanok, trang phục | `08` + `31` | mạnh | khả năng tiếp cận và thiết kế phổ quát trong căn hộ còn có thể mở rộng |
| Tôn giáo và thế giới quan | `09` | mạnh | phong trào tôn giáo mới chỉ thêm khi có nguồn học thuật đáng tin |
| Nghệ thuật, thủ công, di sản | `10` | mạnh | hệ sinh thái bảo tàng/phòng trưng bày đương đại còn tương đối mỏng |
| Lễ Tết, nghi lễ, trò chơi | `11` | mạnh | lễ hội địa phương phân tán sang `14` |
| Đô thị, tiêu dùng, đời sống số | `12` | mạnh sau vòng hiện tại | khả năng tiếp cận đô thị và kinh tế ban đêm có thể cập nhật thêm |
| Văn hoá dịch vụ/đánh giá | `33` | mạnh | điều kiện lao động nên liên kết với công sở/kinh tế |
| Internet/nhắn tin/meme | `27` | mạnh sau vòng hiện tại | tiếng lóng nền tảng cần mốc thời gian vì thay đổi nhanh |
| Hallyu/truyền thông/nền tảng | `13` | mạnh | bản quyền và lao động sáng tạo có thể tiếp tục đào sâu |
| Phép lịch sự/quan hệ đời thường | `18` | mạnh | ưu tiên biến thiên theo bối cảnh, tránh danh sách luật cứng |
| Làm đẹp/thời trang/cơ thể | `19` | mạnh sau vòng hiện tại | nếu thêm số liệu về thủ thuật/hình ảnh cơ thể phải chỉ rõ quần thể |
| Thể thao/giải trí/fandom | `20` | mạnh sau vòng hiện tại | thể thao thích ứng cho người khuyết tật và giải trí người cao tuổi có thể bổ sung |
| Y tế/chăm sóc sức khoẻ | `26` | mạnh sau vòng hiện tại | chăm sóc cuối đời, giảm nhẹ và hệ thống hỗ trợ người khuyết tật còn mỏng |
| Vùng miền/Jeju/cộng đồng hải ngoại | `14` | mạnh | tiếp tục tránh suy tính cách cá nhân từ định kiến vùng miền |
| Dân số/di cư | `15` | mạnh sau vòng hiện tại | mọi nhóm thống kê di cư phải định nghĩa rõ mẫu số |
| Xã hội dân sự/truyền thông/không gian công cộng | `25` | mạnh về khung phân tích | dữ kiện chính trị hiện hành cần nguồn mới mỗi lần cập nhật |
| Liên hệ giữa các hệ thống | `16` | mạnh | cập nhật khi thêm cơ chế mới |
| Bảng thuật ngữ/bản đồ nguồn | `17` | tốt | cần đồng bộ từ khoá mới từ 12/15/19/20/24/26/27 |
| Quy ước tên riêng | `28` | tốt | duy trì nhất quán Việt–Hàn–Anh |

## Các khoảng trống quan trọng chưa cần tạo chương mới

### 1. Người khuyết tật, khả năng tiếp cận và thiết kế phổ quát

Hiện nội dung xuất hiện rải rác trong y tế, già hoá và khoảng cách số nhưng chưa được nối thành một mô hình rõ. Không nhất thiết tạo file mới; có thể bổ sung vào `12`, `26`, `31` và `15` theo ba lớp:

```text
khả năng tiếp cận vật lý
→ toà nhà / giao thông / đường phố

khả năng tiếp cận số
→ kiosk / ứng dụng / xác thực

khả năng tiếp cận xã hội
→ hỗ trợ / giao tiếp / kỳ thị
```

Mục tiêu là tránh coi khuyết tật chỉ là tình trạng y khoa; môi trường quyết định mức độ tham gia xã hội rất lớn.

### 2. Chăm sóc cuối đời, hospice và năng lực hiểu về cái chết

`04` đã bao phủ tang lễ, `26` bao phủ y tế chăm sóc nhưng quyết định cuối đời, hospice/chăm sóc giảm nhẹ (palliative care), lập kế hoạch trước và đau buồn của người chăm sóc vẫn mỏng. Đây là khoảng trống quan trọng trong xã hội già hoá.

Nên bổ sung khi có nguồn thiết chế/y khoa tốt; không viết như lời khuyên y tế cá nhân.

### 3. Nghệ thuật đương đại, bảo tàng và không gian văn hoá

`10` mạnh về nghệ thuật truyền thống nhưng nghệ thuật thị giác đương đại, bảo tàng, phòng trưng bày, biennale, biểu diễn độc lập và quỹ văn hoá chưa sâu. Phần này có thể bổ sung vào `10` mà không cần chương mới.

### 4. Lao động sáng tạo và sở hữu trí tuệ

`13` bao phủ Hallyu/nền tảng khá mạnh, nhưng lao động phía sau biên kịch, hoạ sĩ, tác giả webtoon, vũ công, nhà sản xuất, dịch giả và doanh thu bản quyền còn có thể sâu hơn. Nên nối với `06` công sở và `24` kinh tế.

### 5. Khả năng tiếp cận nhà ở và già hoá tại nơi ở quen thuộc

`08/31` giải thích căn hộ khá kỹ, nhưng `무장애`, thang máy, an toàn phòng tắm, nhà ở thân thiện với người cao tuổi và **già hoá tại nơi ở quen thuộc (ageing-in-place)** chưa thành một chuỗi nhân quả rõ. Có thể bổ sung mà không tạo chương riêng.

### 6. Sự thích nghi ẩm thực trong xã hội đa dạng hơn

`07` có nền tảng ẩm thực mạnh, `15` có di cư, nhưng thực phẩm halal, ăn chay, dị ứng, thích nghi bữa ăn ở trường/công sở và thị trường nguyên liệu quốc tế chưa nối rõ. Đây là dấu hiệu văn hoá chuyển từ “một bữa ăn mặc định” sang sở thích và nhu cầu ngày càng đa dạng.

### 7. Làm việc tại nhà, làm việc lai và ranh giới công việc số

`06`, `12`, `27` đã có công cụ và văn hoá nhắn tin, nhưng làm việc lai thay đổi báo cáo, tín hiệu hiện diện, không gian căn hộ và ranh giới ngoài giờ như thế nào vẫn có thể bổ sung.

## Các liên kết chéo cần giữ đồng bộ

Các cặp sau phải luôn được rà soát cùng nhau khi cập nhật:

```text
04 Gia đình ↔ 29 Nuôi dạy con ↔ 15 Dân số
05 Giáo dục ↔ 30 Đại học ↔ 24 Dịch chuyển xã hội
06 Công sở ↔ 23 Quân đội ↔ 24 Kinh tế
07 Ẩm thực ↔ 32 Mùa ↔ 15 Di cư
08 Nhà ở ↔ 31 Căn hộ ↔ 24 Nhà ở–tài chính
09 Tôn giáo ↔ 11 Nghi lễ ↔ 04 Gia đình
10 Di sản ↔ 13 Hallyu
12 Đô thị ↔ 27 Internet ↔ 33 Dịch vụ
13 Hallyu ↔ 19 Làm đẹp ↔ 20 Fandom
15 Dân số ↔ 26 Y tế ↔ 31 Nhà ở
18 Quan hệ ↔ 03 Ngôn ngữ ↔ 27 Nhắn tin
```

Nếu một chương thay mô hình tư duy nhưng cặp liên quan không được cập nhật, thư viện sẽ dần mâu thuẫn nội bộ.

## Những thứ cố ý không biến thành chương riêng

Bộ sách không nên tách vô hạn thành các file cực nhỏ. Một chủ đề chỉ nên thành chương độc lập nếu nó có **hệ thống nhân quả riêng**, nhiều liên kết chéo và đủ chiều sâu để đọc như một đơn vị hoàn chỉnh.

Các chủ đề sau hiện nên giữ trong chương liên quan:

- văn hoá quán cà phê → `12`;
- văn hoá thú cưng → `15`/`18`;
- đám cưới/tang lễ → `04`/`18`;
- buồng chụp ảnh tự động → `19`/`18`;
- nhóm chạy bộ → `20`;
- kiosk → `12`/`15`;
- thực phẩm bổ sung → `26`;
- màu sắc cá nhân → `19`;
- văn hoá đánh giá → `33` + `12`/`27`.

Tách chúng thành chương riêng lúc này sẽ tăng chi phí điều hướng hơn giá trị học tập.

## Chính sách về độ mới của dữ liệu

Các chương văn hoá dễ vô tình biến số liệu cũ thành “bản chất Hàn Quốc”. Vì vậy:

- số liệu dân số phải ghi **năm dữ liệu**;
- khảo sát phải ghi **định nghĩa quần thể/mẫu**;
- dự báo phải ghi rõ là **dự báo (projection)**;
- chính sách/pháp luật hiện hành phải dùng nguồn đang có hiệu lực;
- nền tảng/tiếng lóng phải có mốc thời gian vì thay đổi nhanh;
- tuyên bố về hiệu quả y khoa phải dựa trên bằng chứng chuyên môn, không dựa vào độ phổ biến;
- thông tin chính trị/không gian công cộng hiện hành phải được kiểm chứng bằng nguồn mới trước khi cập nhật.

## Kiểm toán chiều sâu

Sau các vòng nâng cấp gần đây, các chương từng mỏng nhất `01`, `04`, `05`, `08`, `11`, `12`, `13`, `14`, `15`, `19`, `20`, `24`, `26`, `27` đã được mở rộng đáng kể. Vấn đề chính của thư viện hiện tại không còn là “thiếu chương lớn”, mà là ba việc:

1. **đồng bộ bảng thuật ngữ/liên kết chéo** với từ khoá mới;
2. **bổ sung khoảng trống xuyên chủ đề** như khả năng tiếp cận, cuối đời, lao động sáng tạo;
3. **duy trì độ mới** cho số liệu, nền tảng và chính sách.

Điều này có nghĩa giai đoạn tiếp theo nên ưu tiên **đào sâu + giữ tính nhất quán**, không ưu tiên tạo thêm hàng loạt file.

## Tiêu chí hoàn thành (Definition of Done) cho một chương

Một chương được coi “khá hoàn chỉnh” khi người đọc sau khi đọc có thể:

- giải thích khái niệm bằng lời của mình;
- nêu ít nhất hai cơ chế, không chỉ dữ kiện;
- phân biệt khuôn mẫu của nhóm với độ chắc chắn ở từng cá nhân;
- cho ví dụ đời sống hằng ngày;
- nhận ra ít nhất một đánh đổi (trade-off);
- biết chương nào cần đọc tiếp;
- nhận ra số liệu/chính sách nào có thể đã cũ;
- tránh 2–4 hiểu lầm phổ biến.

Master Knowledge Book không có trạng thái “vĩnh viễn hoàn thành”, vì văn hoá thay đổi. Mục tiêu thực tế là **phạm vi đủ rộng, cơ chế đủ sâu, thuật ngữ nhất quán và đường cập nhật rõ ràng**.