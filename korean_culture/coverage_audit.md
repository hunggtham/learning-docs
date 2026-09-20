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

Sau vòng đánh giá mới nhất, bốn khoảng trống lớn còn thấy rõ trong audit trước — `09`, `11`, `19`, `33` — đã được tăng sâu. Vì vậy thư viện hiện không cần mở thêm chapter lớn. Hướng tốt hơn là **đồng bộ liên kết chéo, thuật ngữ, nguồn và tiếp tục nâng các chương “mạnh nhưng chưa rất mạnh”**.

## 2. Chuẩn ngôn ngữ hiện hành

Phần nội dung chính `01–33` dùng tiếng Việt làm ngôn ngữ giải thích. Tiếng Anh chỉ giữ như từ khoá bổ sung khi hữu ích cho tra cứu; thuật ngữ văn hoá Hàn được giữ bằng Hangul khi cần.

```text
câu giải thích → tiếng Việt tự nhiên
thuật ngữ cần tra cứu → tiếng Việt (English)
thuật ngữ văn hoá Hàn → giữ Hangul khi cần
câu dài pha tiếng Anh → viết lại hoàn toàn bằng tiếng Việt
```

Các ngoại lệ có chủ đích gồm tên riêng, tên sản phẩm/nền tảng, mã, công thức, từ viết tắt kỹ thuật, tên file và cột **English** trong [`17_glossary_and_reference_map.md`](17_glossary_and_reference_map.md).

## 3. Tiêu chí một chương được coi là đủ sâu

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

Một chapter đạt mức **rất mạnh** khi không chỉ mô tả hiện tượng mà còn cho người đọc một mô hình có thể tái sử dụng sang tình huống khác.

## 4. Bản đồ mức độ bao phủ hiện tại

| Lĩnh vực | Chương | Trạng thái hiện tại | Nhận xét |
|---|---|---|---|
| Nền tảng hệ thống văn hoá | `01` | mạnh | đủ làm khung nhập môn; chỉ thêm khi có mô hình xuyên chương mới |
| Nho giáo, quan hệ, thứ bậc | `02` | mạnh | cơ chế rõ; cần luôn tránh biến mô tả lịch sử thành bản chất dân tộc |
| Ngôn ngữ, kính ngữ, `눈치`, `정`, `체면` | `03` | rất mạnh | đã có giao tiếp đa ngôn ngữ, mơ hồ tác nhân, giao tiếp vòng kín và dịch kỹ thuật |
| Gia đình, họ tộc, vòng đời | `04` + `29` | rất mạnh | đã có chăm sóc, tải vô hình, vòng đời và thay đổi cấu trúc hộ |
| Giáo dục, thi cử, bằng cấp | `05` + `30` | rất mạnh | đã có học tập suốt đời, chuyển nghề, kỹ năng chuyển giao và hệ ghép nối đại học–việc làm |
| Công sở | `06` | mạnh | nội dung tốt; còn có thể tăng sâu về bàn giao tri thức, quyền quyết định và khả năng phục hồi tổ chức |
| Ẩm thực | `07` | rất mạnh | đã có chuỗi cung ứng, chuỗi lạnh, công suất bếp, an toàn, giao hàng và lãng phí |
| Nhà ở, hanok, không gian | `08` + `31` | rất mạnh | đã có vật lý công trình, vận hành, bảo trì, năng lượng, tiếp cận và già hoá tại chỗ |
| Tôn giáo và thế giới quan | `09` | rất mạnh sau vòng mới | đã thêm thiết chế xã hội, thiện nguyện, thế tục hoá, mạng quan hệ, quyền lực và đo lường tôn giáo |
| Nghệ thuật, thủ công, di sản | `10` | rất mạnh | đã có lao động sáng tạo, tài trợ, quyền, bảo quản phòng ngừa và bảo tồn số |
| Lễ Tết, nghi lễ, trò chơi | `11` | rất mạnh sau vòng mới | đã thêm nén nghi lễ, gia đình đa dạng, hiện diện từ xa, thương mại hoá, accessibility và cường độ thực hành |
| Đô thị, tiêu dùng, đời sống số | `12` | mạnh | hạ tầng và khả năng tiếp cận tốt; có thể tăng chiều sâu về độ tin cậy và sự cố đô thị |
| Hallyu, truyền thông, nền tảng | `13` | mạnh | đã có lao động sáng tạo, IP và phân phối giá trị; cần giữ đồng bộ với `10`, `19`, `27` |
| Vùng miền, Jeju, bán đảo | `14` | rất mạnh | đã có việc làm vùng, thiết chế neo, dân số hoạt động, ngưỡng dịch vụ và di cư trở về |
| Dân số, già hoá, di cư | `15` | rất mạnh | đã có hợp đồng thế hệ, độ trễ thiết chế, hội nhập di cư và ngưỡng dịch vụ |
| Liên hệ giữa các hệ thống | `16` | rất mạnh | cần tiếp tục đồng bộ các mô hình mới sau mỗi vòng |
| Thuật ngữ và bản đồ nguồn | `17` | tốt | cần thêm thuật ngữ mới từ `09`, `11`, `19`, `33` |
| Phép lịch sự và quan hệ đời thường | `18` | rất mạnh | đã có ngân sách quan hệ, liên kết mạnh/yếu, ranh giới và sửa chữa quan hệ |
| Làm đẹp, thời trang, cơ thể | `19` | rất mạnh sau vòng mới | đã thêm bất cân xứng thông tin, ảnh trước–sau, thuật toán hình ảnh, ranh giới tiêu dùng–y khoa và quyết định theo rủi ro |
| Thể thao, giải trí, fandom | `20` | mạnh | có thể tăng chiều sâu về tổ chức sự kiện, an toàn, cộng đồng và quyền tiếp cận |
| Các lớp lịch sử | `21` | rất mạnh | đã có ký ức gia đình, hạ tầng ký ức, thành phố như bản thảo viết chồng và nguồn gốc tư liệu |
| Tên, tuổi, siêu dữ liệu xã hội | `22` | rất mạnh | đã có danh tính pháp lý/hiển thị, La-tinh hoá và tối thiểu hoá dữ liệu |
| Nghĩa vụ quân sự | `23` | rất mạnh | đã có tái hội nhập, chi phí khởi động lại, chuyển giao kỹ năng và mạng quan hệ |
| Kinh tế, chaebol, nhà ở, dịch chuyển xã hội | `24` | rất mạnh | đã có bảng cân đối hộ, thanh khoản, chi phí cố định và mạng bảo hiểm gia đình |
| Xã hội dân sự và không gian công luận | `25` | mạnh về khung phân tích | mọi dữ kiện chính trị hiện hành phải được kiểm chứng mới trước khi sửa |
| Y tế và văn hoá sức khoẻ | `26` | mạnh | đã có accessibility, chăm sóc giảm nhẹ và cuối đời; còn có thể tăng health literacy và continuity of care |
| Internet, nhắn tin, tiếng lóng, meme | `27` | rất mạnh | đã có thuật toán, thiên lệch tham gia, nguồn gốc, quản trị cộng đồng và khoá mạng lưới |
| Quy ước tên riêng | `28` | tốt | đủ cho vai trò quy chuẩn; không cần mở rộng thành chapter lý thuyết |
| Nuôi dạy con và chăm sóc | `29` | rất mạnh | đã có chất lượng childcare, trẻ ốm, vai trò cha và tải quản lý vô hình |
| Đại học và thanh niên | `30` | rất mạnh | đã có đăng ký môn, GPA, nhóm, phòng nghiên cứu, thực tập và nhà ở sinh viên |
| Căn hộ, khu dân cư | `31` | rất mạnh | đã có quản trị vòng đời, quỹ dự phòng, thông gió, năng lượng và khả năng phục hồi sự cố |
| Mùa, khí hậu, môi trường | `32` | rất mạnh | đã có phân bố khí hậu, hiện tượng học theo mùa, mưa cực đoan, đảo nhiệt và thích nghi |
| Dịch vụ, khách hàng, đánh giá | `33` | rất mạnh sau vòng mới | đã thêm hàng chờ, công suất, đặt chỗ, SLA, phục hồi dịch vụ, bàn giao ngữ cảnh và accessibility |

## 5. Kết quả của vòng review mới nhất

### `09` — từ “các tôn giáo ở Hàn” thành mô hình thiết chế xã hội

[`09_religion_ritual_worldview.md`](09_religion_ritual_worldview.md) hiện tách rõ:

```text
danh tính tôn giáo
≠ thành viên tổ chức
≠ niềm tin
≠ thực hành nghi lễ
≠ mạng hỗ trợ xã hội
```

Nội dung mới đã thêm:

- tổ chức tôn giáo như mạng cung cấp hỗ trợ xã hội;
- `봉사`, `기부`, `헌금`, `보시` và khác biệt động lực;
- `무종교` và thế tục hoá không đồng nghĩa nghi lễ biến mất;
- cộng đồng tôn giáo như mạng liên kết mạnh/yếu;
- bất cân xứng quyền lực giữa lãnh đạo và thành viên;
- nghi lễ vòng đời như cơ chế chuyển trạng thái;
- tôn giáo số và mô hình tham gia lai;
- giá trị đo lường của khảo sát tôn giáo;
- ranh giới giữa ý nghĩa nghi lễ với chuyên môn y khoa, pháp lý và tài chính.

### `11` — nghi lễ đã được phân tích như giao thức có thể thay phiên bản

[`11_holidays_rites_games_memory.md`](11_holidays_rites_games_memory.md) hiện không còn mặc định “truyền thống hoặc giữ nguyên hoặc biến mất”. Chương đã thêm mô hình:

```text
lõi ý nghĩa
+ giao thức thực hiện
+ vật liệu / lao động
```

Từ đó phân tích:

- nén nghi lễ;
- thương lượng giữa các thế hệ;
- gia đình đa văn hoá và đa tôn giáo;
- hiện diện vật lý so với hiện diện quan hệ;
- tham gia từ xa;
- thương mại hoá với cả lợi ích và rủi ro;
- quà tặng như quan hệ có đi có lại;
- accessibility cho người cao tuổi và người khuyết tật;
- đỉnh nhu cầu do đồng bộ xã hội;
- khả năng chống chịu khi nghi lễ bị gián đoạn;
- cường độ thực hành thay vì chỉ đo “có/không”.

### `19` — làm đẹp đã chuyển thành bài toán thông tin–bằng chứng–rủi ro

[`19_beauty_fashion_body_culture.md`](19_beauty_fashion_body_culture.md) hiện phân tích thêm:

```text
lời hứa tiếp thị
≠ cơ chế sinh học
≠ bằng chứng hiệu quả
≠ hồ sơ rủi ro
```

Nội dung mới gồm:

- bất cân xứng thông tin;
- thiên lệch của ảnh trước–sau;
- người ảnh hưởng, tài trợ và quảng cáo liên kết;
- thuật toán khuếch đại chuẩn đẹp;
- tần suất so sánh xã hội trong môi trường camera liên tục;
- ranh giới tiêu dùng–y khoa theo mức xâm lấn;
- đồng thuận hiểu biết;
- khả năng đảo ngược và nợ bảo trì;
- phân biệt phản ứng thường gặp, biến cố và kết quả không đạt kỳ vọng;
- giá như tín hiệu chứ không phải bảo đảm chất lượng;
- rào cản ngôn ngữ trong du lịch làm đẹp;
- yêu cầu về mẫu số khi đọc số liệu thẩm mỹ.

### `33` — dịch vụ đã chuyển thành hệ thống hàng chờ và phục hồi lỗi

[`33_service_customer_review_quick_response_culture.md`](33_service_customer_review_quick_response_culture.md) hiện có mô hình công suất:

```text
λ = tốc độ khách đến
μ = tốc độ phục vụ
ρ = λ / μ
```

Chương đã thêm:

- hàng chờ và công suất dự phòng;
- hàng chờ số;
- `예약` và `노쇼` như bài toán tài nguyên theo thời gian;
- phản hồi đầu tiên khác thời gian giải quyết;
- mức dịch vụ cam kết (SLA) và nợ kỳ vọng;
- phục hồi dịch vụ sau lỗi;
- bàn giao ngữ cảnh giữa nhiều kênh;
- đánh đổi giữa tiêu chuẩn hoá và cá nhân hoá;
- accessibility của kiosk/QR/app;
- lập lịch lao động theo nhu cầu;
- tam giác hoá bằng chứng khi đo chất lượng;
- dịch vụ như hệ điều khiển phản hồi.

## 6. Những chapter hiện nên ưu tiên nếu tiếp tục tăng chiều sâu

Sau vòng này, không còn khoảng trống cấp “thiếu mảng lớn”. Các ưu tiên tiếp theo chủ yếu là **deepening vòng hai**.

### Ưu tiên A — `06`: công sở như hệ thống tri thức và quyền quyết định

Có thể tăng sâu về:

```text
quyền quyết định
→ giao việc
→ bàn giao
→ tài liệu hoá
→ review
→ xử lý sự cố
→ postmortem
→ tri thức tổ chức
```

Đặc biệt hữu ích là phân biệt người chịu trách nhiệm, người phê duyệt, người tư vấn và người cần được thông báo; đồng thời giải thích tại sao một tổ chức phụ thuộc quá nhiều vào `눈치` hoặc “người lâu năm biết hết” sẽ khó mở rộng.

### Ưu tiên B — `12`: đô thị như hệ thống có độ tin cậy

Có thể nối tàu điện, bus, thanh toán, giao hàng, điện, dữ liệu, kiosk và cảnh báo khẩn cấp vào một mô hình **độ tin cậy đô thị (urban reliability)**. Mục tiêu không phải thêm danh sách tiện ích mà hỏi điều gì xảy ra khi một lớp hạ tầng ngừng hoạt động.

### Ưu tiên C — `20`: giải trí như hạ tầng cộng đồng và an toàn

Có thể tăng sâu về quản trị đám đông, phân phối vé, quyền tiếp cận, lao động tình nguyện, chấn thương, an toàn sự kiện và cách câu lạc bộ/nhóm sở thích tạo liên kết xã hội ngoài công sở–gia đình.

### Ưu tiên D — `26`: năng lực hiểu thông tin sức khoẻ và tính liên tục chăm sóc

Không cần thêm nhiều bệnh. Nên đào sâu:

```text
triệu chứng
→ chọn điểm chăm sóc
→ chẩn đoán
→ điều trị
→ theo dõi
→ bàn giao giữa cơ sở
```

và cách người bệnh đánh giá nguồn trực tuyến, hiểu rủi ro, chuẩn bị câu hỏi và giữ thông tin khi chuyển giữa các cơ sở.

## 7. Các liên kết chéo bắt buộc phải giữ đồng bộ

```text
03 Ngôn ngữ ↔ 06 Công sở ↔ 18 Quan hệ ↔ 27 Nhắn tin ↔ 33 Dịch vụ
04 Gia đình ↔ 09 Tôn giáo ↔ 11 Nghi lễ ↔ 29 Nuôi dạy con ↔ 15 Dân số
05 Giáo dục ↔ 30 Đại học ↔ 24 Dịch chuyển xã hội ↔ 06 Công sở
06 Công sở ↔ 23 Quân đội ↔ 24 Kinh tế ↔ 27 Nhắn tin ↔ 29 Chăm sóc
07 Ẩm thực ↔ 12 Giao hàng ↔ 15 Di cư ↔ 32 Khí hậu ↔ 33 Dịch vụ
08 Nhà ở ↔ 31 Căn hộ ↔ 26 Y tế ↔ 15 Già hoá ↔ 24 Tài chính hộ ↔ 32 Khí hậu
09 Tôn giáo ↔ 11 Nghi lễ ↔ 04 Gia đình ↔ 18 Quan hệ
10 Nghệ thuật/di sản ↔ 13 Hallyu ↔ 21 Ký ức ↔ 27 Hạ tầng số
12 Đô thị ↔ 14 Vùng ↔ 27 Internet ↔ 31 Căn hộ ↔ 33 Dịch vụ
13 Hallyu ↔ 19 Làm đẹp ↔ 20 Fandom ↔ 24 Kinh tế ↔ 27 Thuật toán
14 Vùng ↔ 15 Dân số ↔ 24 Kinh tế ↔ 30 Đại học
15 Dân số ↔ 22 Danh tính ↔ 26 Y tế ↔ 29 Chăm sóc
19 Làm đẹp ↔ 26 Sức khoẻ ↔ 27 Hình ảnh số ↔ 33 Dịch vụ
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
- số liệu giáo dục, việc làm, tôn giáo, thẩm mỹ hoặc di cư phải giữ nguyên định nghĩa mẫu và không suy rộng quá phạm vi;
- khi dùng ký ức cá nhân hoặc truyền thông để nói về lịch sử, phải tách chúng khỏi bằng chứng lịch sử ở cấp sự kiện;
- số liệu khí hậu phải ghi địa điểm, giai đoạn quan sát, đường cơ sở và nguồn;
- quy định an toàn thực phẩm, y tế, dịch vụ và quyền người tiêu dùng phải dùng nguồn hiện hành nếu được trình bày như quy tắc áp dụng thực tế.

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
- tránh các hiểu lầm phổ biến;
- đọc phần giải thích chủ yếu bằng tiếng Việt nhưng vẫn có đủ từ khoá Anh–Hàn để tra cứu.

Master Knowledge Book không có trạng thái “vĩnh viễn hoàn thành”. Trạng thái mục tiêu là **phạm vi đủ rộng, cơ chế đủ sâu, thất bại đủ rõ, thuật ngữ nhất quán, tiếng Việt dễ đọc và đường cập nhật rõ ràng**.