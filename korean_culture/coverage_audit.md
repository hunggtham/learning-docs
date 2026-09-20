# Korean Culture — Bản kiểm toán mức độ bao phủ

> File này không phải chương học riêng. Nó là **bản kiểm toán mức độ bao phủ và độ sâu (coverage + depth audit)** cho toàn bộ `korean_culture/01–33`. Thư mục `kiip/` không nằm trong phạm vi kiểm toán này.

## 1. Đánh giá tổng thể hiện tại

Bộ `korean_culture/` đã vượt qua giai đoạn “thu thập kiến thức theo chủ đề”. Cấu trúc hiện tại đã đủ rộng để bao phủ phần lớn đời sống văn hoá Hàn Quốc từ lịch sử, quan hệ, ngôn ngữ, gia đình, giáo dục, công sở, tôn giáo, ẩm thực, nhà ở, Hallyu, vùng miền, dân số, Internet, chăm sóc, khí hậu đến dịch vụ.

Điểm mạnh lớn nhất hiện nay không còn là số lượng chủ đề mà là **cơ chế giải thích xuyên chương**. Nhiều hiện tượng đã được mô hình hoá theo chuỗi:

```text
điều kiện vật chất
→ thiết chế
→ động lực
→ hành vi
→ phản hồi
→ tác động ngoại biên
→ điểm thất bại
→ khả năng thích nghi
```

Sau vòng mới nhất, bốn chương từng được xếp vào nhóm “mạnh nhưng còn khoảng trống cơ chế” — `06`, `12`, `20`, `26` — đã được tăng sâu. Vì vậy thư viện hiện **không còn thiếu một mảng kiến thức lớn cần tạo chapter riêng**. Hướng phát triển tiếp theo nên là đồng bộ liên kết, glossary, nguồn và làm sâu chọn lọc các chapter nền tảng còn ở mức “mạnh”.

## 2. Chuẩn ngôn ngữ hiện hành

Phần nội dung chính `01–33` dùng tiếng Việt làm ngôn ngữ giải thích. Tiếng Anh chỉ giữ như từ khoá bổ sung khi hữu ích cho tra cứu; thuật ngữ văn hoá Hàn được giữ bằng Hangul khi cần.

```text
câu giải thích → tiếng Việt tự nhiên
thuật ngữ cần tra cứu → tiếng Việt (English)
thuật ngữ văn hoá Hàn → giữ Hangul khi cần
câu dài pha tiếng Anh → viết lại hoàn toàn bằng tiếng Việt
```

Các ngoại lệ có chủ đích gồm tên riêng, tên sản phẩm/nền tảng, mã, công thức, từ viết tắt kỹ thuật, tên file và cột **English** trong [`17_glossary_and_reference_map.md`](17_glossary_and_reference_map.md).

## 3. Tiêu chí một chapter được coi là đủ sâu

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
11. Liên kết — thay đổi ở chapter này phản hồi sang chapter nào khác?
```

Một chapter đạt mức **rất mạnh** khi không chỉ mô tả hiện tượng mà còn cho người đọc một mô hình có thể tái sử dụng sang tình huống khác.

## 4. Bản đồ mức độ bao phủ hiện tại

| Lĩnh vực | Chapter | Trạng thái hiện tại | Nhận xét |
|---|---|---|---|
| Nền tảng hệ thống văn hoá | `01` | mạnh | đủ làm khung nhập môn; có thể tăng thêm phương pháp so sánh văn hoá và kiểm định nhân quả |
| Nho giáo, quan hệ, thứ bậc | `02` | mạnh | cơ chế rõ; có thể đào sâu quá trình thay đổi thiết chế và khi thâm niên mất quyền giải thích |
| Ngôn ngữ, kính ngữ, `눈치`, `정`, `체면` | `03` | rất mạnh | đã có giao tiếp đa ngôn ngữ, mơ hồ tác nhân, giao tiếp vòng kín và dịch kỹ thuật |
| Gia đình, họ tộc, vòng đời | `04` + `29` | rất mạnh | đã có chăm sóc, tải vô hình, vòng đời và thay đổi cấu trúc hộ |
| Giáo dục, thi cử, bằng cấp | `05` + `30` | rất mạnh | đã có học tập suốt đời, chuyển nghề, kỹ năng chuyển giao và hệ ghép nối đại học–việc làm |
| Công sở | `06` | rất mạnh sau vòng mới | đã có quyền quyết định, bản ghi quyết định, review, incident, postmortem, bus factor và học tập tổ chức |
| Ẩm thực | `07` | rất mạnh | đã có chuỗi cung ứng, chuỗi lạnh, công suất bếp, an toàn, giao hàng và lãng phí |
| Nhà ở, hanok, không gian | `08` + `31` | rất mạnh | đã có vật lý công trình, vận hành, bảo trì, năng lượng, tiếp cận và già hoá tại chỗ |
| Tôn giáo và thế giới quan | `09` | rất mạnh | đã có thiết chế xã hội, thiện nguyện, thế tục hoá, mạng quan hệ, quyền lực và đo lường tôn giáo |
| Nghệ thuật, thủ công, di sản | `10` | rất mạnh | đã có lao động sáng tạo, tài trợ, quyền, bảo quản phòng ngừa và bảo tồn số |
| Lễ Tết, nghi lễ, trò chơi | `11` | rất mạnh | đã có nén nghi lễ, gia đình đa dạng, hiện diện từ xa, thương mại hoá, accessibility và cường độ thực hành |
| Đô thị, tiêu dùng, đời sống số | `12` | rất mạnh sau vòng mới | đã thêm reliability, điểm lỗi duy nhất, dự phòng, suy giảm có kiểm soát, sự cố dây chuyền và đường thay thế |
| Hallyu, truyền thông, nền tảng | `13` | mạnh | đã có lao động sáng tạo, IP và phân phối giá trị; đây là một trong số ít chapter còn có thể tăng sâu vòng hai |
| Vùng miền, Jeju, bán đảo | `14` | rất mạnh | đã có việc làm vùng, thiết chế neo, dân số hoạt động, ngưỡng dịch vụ và di cư trở về |
| Dân số, già hoá, di cư | `15` | rất mạnh | đã có hợp đồng thế hệ, độ trễ thiết chế, hội nhập di cư và ngưỡng dịch vụ |
| Liên hệ giữa các hệ thống | `16` | rất mạnh | cần đồng bộ các mô hình mới từ `06`, `12`, `20`, `26` |
| Thuật ngữ và bản đồ nguồn | `17` | tốt | cần đồng bộ thuật ngữ mới sau vòng hiện tại |
| Phép lịch sự và quan hệ đời thường | `18` | rất mạnh | đã có ngân sách quan hệ, liên kết mạnh/yếu, ranh giới và sửa chữa quan hệ |
| Làm đẹp, thời trang, cơ thể | `19` | rất mạnh | đã có bất cân xứng thông tin, ảnh trước–sau, thuật toán hình ảnh, ranh giới tiêu dùng–y khoa và quyết định theo rủi ro |
| Thể thao, giải trí, fandom | `20` | rất mạnh sau vòng mới | đã thêm dòng người, lối thoát, an toàn đám đông, thị trường vé thứ cấp, quản trị cộng đồng và đo lường tham gia |
| Các lớp lịch sử | `21` | rất mạnh | đã có ký ức gia đình, hạ tầng ký ức, thành phố như bản thảo viết chồng và nguồn gốc tư liệu |
| Tên, tuổi, siêu dữ liệu xã hội | `22` | rất mạnh | đã có danh tính pháp lý/hiển thị, La-tinh hoá và tối thiểu hoá dữ liệu |
| Nghĩa vụ quân sự | `23` | rất mạnh | đã có tái hội nhập, chi phí khởi động lại, chuyển giao kỹ năng và mạng quan hệ |
| Kinh tế, chaebol, nhà ở, dịch chuyển xã hội | `24` | rất mạnh | đã có bảng cân đối hộ, thanh khoản, chi phí cố định và mạng bảo hiểm gia đình |
| Xã hội dân sự và không gian công luận | `25` | mạnh về khung phân tích | mọi dữ kiện chính trị hiện hành phải được kiểm chứng mới trước khi sửa |
| Y tế và văn hoá sức khoẻ | `26` | rất mạnh sau vòng mới | đã thêm health literacy, teach-back, quyết định chung, continuity of care, chuyển tuyến, đối chiếu thuốc và an toàn bệnh nhân |
| Internet, nhắn tin, tiếng lóng, meme | `27` | rất mạnh | đã có thuật toán, thiên lệch tham gia, nguồn gốc, quản trị cộng đồng và khoá mạng lưới |
| Quy ước tên riêng | `28` | tốt | đủ cho vai trò quy chuẩn; không cần mở rộng thành chapter lý thuyết |
| Nuôi dạy con và chăm sóc | `29` | rất mạnh | đã có chất lượng childcare, trẻ ốm, vai trò cha và tải quản lý vô hình |
| Đại học và thanh niên | `30` | rất mạnh | đã có đăng ký môn, GPA, nhóm, phòng nghiên cứu, thực tập và nhà ở sinh viên |
| Căn hộ, khu dân cư | `31` | rất mạnh | đã có quản trị vòng đời, quỹ dự phòng, thông gió, năng lượng và khả năng phục hồi sự cố |
| Mùa, khí hậu, môi trường | `32` | rất mạnh | đã có phân bố khí hậu, hiện tượng học theo mùa, mưa cực đoan, đảo nhiệt và thích nghi |
| Dịch vụ, khách hàng, đánh giá | `33` | rất mạnh | đã có hàng chờ, công suất, đặt chỗ, SLA, phục hồi dịch vụ, bàn giao ngữ cảnh và accessibility |

## 5. Kết quả bổ sung mới nhất

### `06` — công sở đã chuyển từ “thứ bậc” sang hệ thống quyết định và học tập

[`06_workplace_organization_hoesik.md`](06_workplace_organization_hoesik.md) hiện phân biệt:

```text
người thực hiện
≠ người chịu trách nhiệm cuối
≠ người được tham vấn
≠ người cần được thông báo
```

Nội dung mới gồm quyền quyết định, bản ghi lý do của quyết định, rà soát đồng cấp so với đánh giá hiệu suất, vòng xử lý `장애`, hậu kiểm không đổ lỗi, chỉ số thời gian phục hồi, điểm lỗi duy nhất về tri thức, `bus factor` và quá trình biến kinh nghiệm cá nhân thành học tập tổ chức.

Điểm sâu quan trọng là: **một công ty không học chỉ vì một nhân viên “đã rút kinh nghiệm”; tổ chức chỉ học khi bài học đi vào quy trình, công cụ, tài liệu hoặc thiết kế quyền hạn**.

### `12` — đô thị đã có lớp reliability và fallback

[`12_city_consumption_digital_life.md`](12_city_consumption_digital_life.md) giờ tách rõ:

```text
hiệu suất bình thường
≠ độ tin cậy
≠ khả năng phục hồi
```

Chương đã thêm điểm lỗi duy nhất, dự phòng, suy giảm chức năng có kiểm soát, sự cố điện/mạng lan theo chuỗi, đường thay thế, cảnh báo khẩn cấp, mệt mỏi cảnh báo và yêu cầu duy trì phương án không số cho các dịch vụ thiết yếu.

Mô hình mới giúp tránh sai lầm “thành phố rất tiện = thành phố luôn chống chịu tốt”.

### `20` — giải trí đã được nâng thành bài toán quản trị sự kiện và cộng đồng

[`20_sports_leisure_fan_culture.md`](20_sports_leisure_fan_culture.md) hiện thêm:

- thị trường vé thứ cấp và công bằng phân bổ;
- dòng người và điểm nghẽn;
- khác biệt giữa vào sân và thoát người;
- an toàn đám đông như trách nhiệm hệ thống;
- sự kiện như một thành phố tạm thời;
- thời tiết và hoạt động ngoài trời;
- quản trị cộng đồng sở thích;
- chi phí gia nhập của thành viên mới;
- khác biệt giữa số người từng thử, người tham gia thường xuyên, thời lượng, chi tiêu và độ hiển thị trên mạng.

Điểm cốt lõi là chuyển từ “người Hàn thích môn gì?” sang “hạ tầng, lịch, quản trị, an toàn và khả năng tiếp cận nào làm hoạt động đó có thể tồn tại ở quy mô lớn?”.

### `26` — y tế đã có tính liên tục và năng lực hiểu thông tin sức khoẻ

[`26_health_medicine_wellness_body.md`](26_health_medicine_wellness_body.md) hiện thêm:

```text
tìm thông tin
→ hiểu
→ đánh giá
→ áp dụng
```

và các cơ chế: `teach-back`, ra quyết định chung, phân biệt rủi ro tương đối–tuyệt đối, tính liên tục của chăm sóc, chuyển tuyến hai chiều, đối chiếu thuốc, xuất viện như điểm chuyển giao, an toàn bệnh nhân nhiều lớp, rào cản của bệnh nhân nước ngoài và bệnh mạn tính như hệ thống quản lý lặp lại.

Điểm mới quan trọng là xem **thông tin y tế như trạng thái cần được chuyển qua người, cơ sở và thời gian**, chứ không chỉ là một lời khuyên ở một lần khám.

## 6. Đánh giá phần còn thiếu sau vòng này

Không còn gap nào đủ lớn để biện minh cho một chapter mới. Những việc nên làm tiếp thuộc ba nhóm.

### Nhóm A — tăng chiều sâu chọn lọc ở chapter nền

`01`, `02`, `13` vẫn ở mức “mạnh” thay vì “rất mạnh”. Có thể phát triển thêm:

```text
01 → phương pháp so sánh văn hoá, phản chứng, quan hệ nhân quả và biến gây nhiễu
02 → thâm niên khi nào hữu ích, khi nào trở thành chi phí; thay đổi quyền lực theo loại tổ chức
13 → vòng đời nội dung, quyền lực nền tảng, kinh tế hit-driven, rủi ro danh tiếng và khả năng sống dài của IP
```

### Nhóm B — đồng bộ knowledge graph

[`16_connections_mental_models_misconceptions.md`](16_connections_mental_models_misconceptions.md) cần nhận các liên hệ mới:

```text
06 công sở ↔ khả năng quan sát ↔ học tập tổ chức
12 đô thị ↔ redundancy ↔ graceful degradation
20 sự kiện ↔ hàng đợi ↔ an toàn đám đông
26 y tế ↔ state transfer ↔ continuity of care
```

### Nhóm C — đồng bộ glossary và nguồn

[`17_glossary_and_reference_map.md`](17_glossary_and_reference_map.md) nên thêm các thuật ngữ như:

- quyền quyết định (decision right);
- hậu kiểm sự cố (postmortem);
- điểm lỗi duy nhất (single point of failure);
- khả năng phục hồi (resilience);
- suy giảm có kiểm soát (graceful degradation);
- dòng người (crowd flow);
- tính liên tục của chăm sóc (continuity of care);
- đối chiếu thuốc (medication reconciliation);
- năng lực sức khoẻ (health literacy).

## 7. Các liên kết chéo bắt buộc phải giữ đồng bộ

```text
03 Ngôn ngữ ↔ 06 Công sở ↔ 18 Quan hệ ↔ 27 Nhắn tin ↔ 33 Dịch vụ
04 Gia đình ↔ 09 Tôn giáo ↔ 11 Nghi lễ ↔ 29 Nuôi dạy con ↔ 15 Dân số
05 Giáo dục ↔ 30 Đại học ↔ 24 Dịch chuyển xã hội ↔ 06 Công sở
06 Công sở ↔ 23 Quân đội ↔ 24 Kinh tế ↔ 27 Nhắn tin ↔ 29 Chăm sóc ↔ 33 Dịch vụ
07 Ẩm thực ↔ 12 Giao hàng ↔ 15 Di cư ↔ 32 Khí hậu ↔ 33 Dịch vụ
08 Nhà ở ↔ 31 Căn hộ ↔ 26 Y tế ↔ 15 Già hoá ↔ 24 Tài chính hộ ↔ 32 Khí hậu
09 Tôn giáo ↔ 11 Nghi lễ ↔ 04 Gia đình ↔ 18 Quan hệ
10 Nghệ thuật/di sản ↔ 13 Hallyu ↔ 21 Ký ức ↔ 27 Hạ tầng số
12 Đô thị ↔ 14 Vùng ↔ 20 Sự kiện ↔ 27 Internet ↔ 31 Căn hộ ↔ 33 Dịch vụ
13 Hallyu ↔ 19 Làm đẹp ↔ 20 Fandom ↔ 24 Kinh tế ↔ 27 Thuật toán
14 Vùng ↔ 15 Dân số ↔ 24 Kinh tế ↔ 30 Đại học
15 Dân số ↔ 22 Danh tính ↔ 26 Y tế ↔ 29 Chăm sóc
19 Làm đẹp ↔ 26 Sức khoẻ ↔ 27 Hình ảnh số ↔ 33 Dịch vụ
20 Giải trí ↔ 12 Đô thị ↔ 32 Khí hậu ↔ 33 Hàng đợi
21 Lịch sử ↔ 14 Vùng miền ↔ 11 Nghi lễ ↔ 13 Truyền thông ↔ 25 Không gian công luận
23 Quân đội ↔ 05 Giáo dục ↔ 30 Đại học ↔ 06 Công sở
26 Y tế ↔ 03 Giao tiếp ↔ 15 Già hoá ↔ 22 Danh tính ↔ 31 Khả năng tiếp cận
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
- số liệu giáo dục, việc làm, tôn giáo, thẩm mỹ hoặc di cư phải giữ nguyên định nghĩa mẫu và không suy rộng quá phạm vi;
- khi dùng ký ức cá nhân hoặc truyền thông để nói về lịch sử, phải tách chúng khỏi bằng chứng lịch sử ở cấp sự kiện;
- số liệu khí hậu phải ghi địa điểm, giai đoạn quan sát, đường cơ sở và nguồn;
- quy định an toàn thực phẩm, y tế, dịch vụ và quyền người tiêu dùng phải dùng nguồn hiện hành nếu được trình bày như quy tắc áp dụng thực tế;
- khi mô tả an toàn sự kiện hoặc chăm sóc y tế, ưu tiên mô hình khái niệm; quy trình áp dụng thực tế phải kiểm tra hướng dẫn hiện hành của cơ quan chuyên môn.

## 9. Tiêu chí hoàn thành cho một chapter

Một chapter được coi là khá hoàn chỉnh khi người đọc có thể:

- giải thích khái niệm bằng lời của mình;
- nêu ít nhất hai cơ chế thay vì chỉ nhớ dữ kiện;
- phân biệt khuôn mẫu nhóm với cá nhân;
- cho ví dụ đời sống;
- nhận ra ít nhất một đánh đổi;
- chỉ ra ít nhất một tình huống hệ thống thất bại hoặc ngoại lệ;
- mô tả hiện tượng thay đổi qua vòng đời hoặc giữa các thiết chế;
- biết chapter nào cần đọc tiếp;
- nhận ra dữ liệu hoặc chính sách nào có thể đã cũ;
- xác định phần nào là hạ tầng vật lý, phần nào là thiết chế và phần nào là chuẩn mực;
- biết dữ liệu đang đo trực tiếp hay chỉ dùng biến đại diện;
- nhận ra điểm chuyển giao thông tin và trách nhiệm trong các hệ thống phức tạp;
- tránh các hiểu lầm phổ biến;
- đọc phần giải thích chủ yếu bằng tiếng Việt nhưng vẫn có đủ từ khoá Anh–Hàn để tra cứu.

Master Knowledge Book không có trạng thái “vĩnh viễn hoàn thành”. Trạng thái mục tiêu là **phạm vi đủ rộng, cơ chế đủ sâu, thất bại đủ rõ, thuật ngữ nhất quán, tiếng Việt dễ đọc và đường cập nhật rõ ràng**.