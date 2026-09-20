# Korean Culture — Bản kiểm toán mức độ bao phủ

> File này không phải chương học riêng. Nó là **bản kiểm toán mức độ bao phủ và độ sâu (coverage + depth audit)** cho toàn bộ `korean_culture/01–33`. Thư mục `kiip/` không nằm trong phạm vi kiểm toán này.

## 1. Đánh giá tổng thể hiện tại

Bộ `korean_culture/` đã vượt qua giai đoạn “thu thập kiến thức theo chủ đề”. Phần chính `01–33` hiện bao phủ phần lớn đời sống văn hoá Hàn Quốc từ lịch sử, quan hệ, ngôn ngữ, gia đình, giáo dục, công sở, tôn giáo, ẩm thực, nhà ở, Hallyu, vùng miền, dân số, Internet, chăm sóc, khí hậu đến dịch vụ.

Điểm mạnh lớn nhất hiện nay là **cơ chế giải thích xuyên chương**. Nhiều hiện tượng được mô hình hoá theo chuỗi:

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

Sau vòng mới nhất, `01`, `02` và `13` đã được tăng sâu; `16` và `17` cũng được đồng bộ. Vì vậy thư viện hiện **không còn thiếu mảng lớn và cũng không còn chapter nền tảng nào ở trạng thái rõ ràng “quá mỏng”**. Hướng phát triển tiếp theo nên chuyển từ mở rộng phạm vi sang **kiểm toán tính nhất quán, ví dụ, nguồn, liên kết chéo và khả năng học theo lộ trình**.

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
| Nền tảng hệ thống văn hoá | `01` | rất mạnh sau vòng mới | đã thêm phương pháp so sánh, biến gây nhiễu, phản thực tế, cấp độ phân tích, age/cohort/period, thiên lệch chọn mẫu và tam giác hoá nguồn |
| Nho giáo, quan hệ, thứ bậc | `02` | rất mạnh sau vòng mới | đã thêm quyền lực chính thức/thực tế, tính chính danh, thứ bậc đa trục, voice/exit/loyalty, vòng đời cố vấn và kiểm toán hệ thứ bậc |
| Ngôn ngữ, kính ngữ, `눈치`, `정`, `체면` | `03` | rất mạnh | đã có giao tiếp đa ngôn ngữ, mơ hồ tác nhân, giao tiếp vòng kín và dịch kỹ thuật |
| Gia đình, họ tộc, vòng đời | `04` + `29` | rất mạnh | đã có chăm sóc, tải vô hình, vòng đời và thay đổi cấu trúc hộ |
| Giáo dục, thi cử, bằng cấp | `05` + `30` | rất mạnh | đã có học tập suốt đời, chuyển nghề, kỹ năng chuyển giao và hệ ghép nối đại học–việc làm |
| Công sở | `06` | rất mạnh | đã có quyền quyết định, bản ghi quyết định, review, incident, postmortem, bus factor và học tập tổ chức |
| Ẩm thực | `07` | rất mạnh | đã có chuỗi cung ứng, chuỗi lạnh, công suất bếp, an toàn, giao hàng và lãng phí |
| Nhà ở, hanok, không gian | `08` + `31` | rất mạnh | đã có vật lý công trình, vận hành, bảo trì, năng lượng, tiếp cận và già hoá tại chỗ |
| Tôn giáo và thế giới quan | `09` | rất mạnh | đã có thiết chế xã hội, thiện nguyện, thế tục hoá, mạng quan hệ, quyền lực và đo lường tôn giáo |
| Nghệ thuật, thủ công, di sản | `10` | rất mạnh | đã có lao động sáng tạo, tài trợ, quyền, bảo quản phòng ngừa và bảo tồn số |
| Lễ Tết, nghi lễ, trò chơi | `11` | rất mạnh | đã có nén nghi lễ, gia đình đa dạng, hiện diện từ xa, thương mại hoá, accessibility và cường độ thực hành |
| Đô thị, tiêu dùng, đời sống số | `12` | rất mạnh | đã có reliability, điểm lỗi duy nhất, dự phòng, suy giảm có kiểm soát, sự cố dây chuyền và đường thay thế |
| Hallyu, truyền thông, nền tảng | `13` | rất mạnh sau vòng mới | đã thêm vòng đời nội dung, danh mục dự án, cửa sổ phát hành, catalog, retention/churn, exploration–exploitation, bản địa hoá nhiều tầng và lợi thế tích luỹ của IP |
| Vùng miền, Jeju, bán đảo | `14` | rất mạnh | đã có việc làm vùng, thiết chế neo, dân số hoạt động, ngưỡng dịch vụ và di cư trở về |
| Dân số, già hoá, di cư | `15` | rất mạnh | đã có hợp đồng thế hệ, độ trễ thiết chế, hội nhập di cư và ngưỡng dịch vụ |
| Liên hệ giữa các hệ thống | `16` | rất mạnh, đã đồng bộ | đã tăng từ 30 lên 36 liên hệ và thêm lớp phản thực tế vào khung đọc hiện tượng |
| Thuật ngữ và bản đồ nguồn | `17` | tốt–rất tốt, đã đồng bộ | đã thêm thuật ngữ mới từ quyền lực, công sở, đô thị, Hallyu, y tế, dịch vụ và mô hình phân tích |
| Phép lịch sự và quan hệ đời thường | `18` | rất mạnh | đã có ngân sách quan hệ, liên kết mạnh/yếu, ranh giới và sửa chữa quan hệ |
| Làm đẹp, thời trang, cơ thể | `19` | rất mạnh | đã có bất cân xứng thông tin, ảnh trước–sau, thuật toán hình ảnh, ranh giới tiêu dùng–y khoa và quyết định theo rủi ro |
| Thể thao, giải trí, fandom | `20` | rất mạnh | đã có dòng người, lối thoát, an toàn đám đông, thị trường vé thứ cấp, quản trị cộng đồng và đo lường tham gia |
| Các lớp lịch sử | `21` | rất mạnh | đã có ký ức gia đình, hạ tầng ký ức, thành phố như bản thảo viết chồng và nguồn gốc tư liệu |
| Tên, tuổi, siêu dữ liệu xã hội | `22` | rất mạnh | đã có danh tính pháp lý/hiển thị, La-tinh hoá và tối thiểu hoá dữ liệu |
| Nghĩa vụ quân sự | `23` | rất mạnh | đã có tái hội nhập, chi phí khởi động lại, chuyển giao kỹ năng và mạng quan hệ |
| Kinh tế, chaebol, nhà ở, dịch chuyển xã hội | `24` | rất mạnh | đã có bảng cân đối hộ, thanh khoản, chi phí cố định và mạng bảo hiểm gia đình |
| Xã hội dân sự và không gian công luận | `25` | mạnh về khung phân tích | mọi dữ kiện chính trị hiện hành phải được kiểm chứng mới trước khi sửa |
| Y tế và văn hoá sức khoẻ | `26` | rất mạnh | đã có health literacy, teach-back, quyết định chung, continuity of care, chuyển tuyến, đối chiếu thuốc và an toàn bệnh nhân |
| Internet, nhắn tin, tiếng lóng, meme | `27` | rất mạnh | đã có thuật toán, thiên lệch tham gia, nguồn gốc, quản trị cộng đồng và khoá mạng lưới |
| Quy ước tên riêng | `28` | tốt | đủ cho vai trò quy chuẩn; không cần mở rộng thành chapter lý thuyết |
| Nuôi dạy con và chăm sóc | `29` | rất mạnh | đã có chất lượng childcare, trẻ ốm, vai trò cha và tải quản lý vô hình |
| Đại học và thanh niên | `30` | rất mạnh | đã có đăng ký môn, GPA, nhóm, phòng nghiên cứu, thực tập và nhà ở sinh viên |
| Căn hộ, khu dân cư | `31` | rất mạnh | đã có quản trị vòng đời, quỹ dự phòng, thông gió, năng lượng và khả năng phục hồi sự cố |
| Mùa, khí hậu, môi trường | `32` | rất mạnh | đã có phân bố khí hậu, hiện tượng học theo mùa, mưa cực đoan, đảo nhiệt và thích nghi |
| Dịch vụ, khách hàng, đánh giá | `33` | rất mạnh | đã có hàng chờ, công suất, đặt chỗ, SLA, phục hồi dịch vụ, bàn giao ngữ cảnh và accessibility |

## 5. Kết quả bổ sung mới nhất

### `01` — từ chương nhập môn thành phương pháp phân tích văn hoá

[`01_cultural_system_history_geography.md`](01_cultural_system_history_geography.md) hiện không chỉ cung cấp nền lịch sử–địa lý mà còn dạy cách kiểm tra một lời giải thích:

```text
quan sát hiện tượng
→ chọn nhóm so sánh
→ tìm lời giải thích thay thế
→ kiểm tra biến gây nhiễu
→ đặt phản thực tế
→ kiểm tra cấp độ phân tích
→ kiểm tra cách chọn mẫu
→ tam giác hoá nguồn
```

Chương cũng tách rõ hiệu ứng tuổi, hiệu ứng thế hệ và hiệu ứng thời kỳ, đồng thời nhấn mạnh nguyên tắc tiết kiệm lời giải thích: nếu luật, giá, thời gian hoặc giao diện đã giải thích đủ hành vi thì không cần thêm “bản chất văn hoá” như một nguyên nhân mơ hồ.

### `02` — thứ bậc đã được tách thành nhiều loại quyền lực

[`02_confucianism_relations_hierarchy.md`](02_confucianism_relations_hierarchy.md) hiện phân biệt:

```text
quyền hành chính
≠ quyền chuyên môn
≠ quyền ngân sách
≠ quyền thông tin
≠ quyền mạng quan hệ
```

Chương mới thêm tính chính danh, khi thâm niên mất giá trị dự báo, thứ bậc đa trục, phản ứng lên tiếng–rời bỏ–trung thành, vòng đời của quan hệ cố vấn và bốn lớp để kiểm tra một tổ chức có thật sự “phẳng” hay chỉ đổi cách xưng hô.

Điểm cốt lõi mới là: **thứ bậc không tự động xấu; cần hỏi quyền có đi cùng trách nhiệm, thông tin và kênh phản biện hay không**.

### `13` — Hallyu đã có đầy đủ vòng đời kinh tế của nội dung

[`13_hallyu_media_platforms.md`](13_hallyu_media_platforms.md) hiện đi xa hơn sản xuất–phân phối để mô tả:

```text
ý tưởng
→ tài trợ / bật đèn xanh
→ sản xuất
→ phát hành
→ khai thác theo cửa sổ
→ catalog
→ chuyển thể
→ tái khám phá
→ lưu trữ / bảo tồn
```

Chương đã thêm quản lý danh mục dự án, thu hút–giữ chân–rời bỏ người dùng, giá trị catalog, đánh đổi giữa khai thác công thức cũ và khám phá cái mới, bản địa hoá nhiều tầng, bão hoà chú ý, lợi thế tích luỹ của IP và vấn đề phiên bản/bản chính thức trong lưu trữ số.

### `16` — knowledge graph đã được đồng bộ với các mô hình mới

[`16_connections_mental_models_misconceptions.md`](16_connections_mental_models_misconceptions.md) hiện có **36 liên hệ xuyên chương**, bổ sung:

- quyền lực ↔ thông tin ↔ trách nhiệm;
- bus factor ↔ chăm sóc gia đình ↔ khả năng chống chịu;
- độ tin cậy đô thị ↔ phục hồi dịch vụ ↔ fallback;
- fandom ↔ hàng đợi ↔ tài nguyên khan hiếm;
- health literacy ↔ bất cân xứng thông tin ↔ đồng thuận;
- IP ↔ dữ liệu ↔ vốn ↔ lợi thế tích luỹ.

Khung đọc hiện tượng tăng từ 6 lên **7 lớp**, với lớp phản thực tế để kiểm tra giả thuyết nhân quả.

### `17` — glossary đã được đồng bộ

[`17_glossary_and_reference_map.md`](17_glossary_and_reference_map.md) hiện đã thêm từ khoá về:

- tính chính danh và chủ nghĩa quan hệ;
- `담당자`, `업무분장`, `책임소재`, `인수인계`, `장애`, `사후회고`;
- đường thay thế và cảnh báo khẩn cấp;
- đặt chỗ, no-show và ticketing;
- quyền phái sinh, bản địa hoá và catalog nội dung;
- health literacy và referral;
- phản thực tế, biến gây nhiễu, thiên lệch chọn mẫu, graceful degradation, fallback, informed consent, lợi thế tích luỹ và vòng đời nội dung.

## 6. Việc nên làm tiếp: chuyển từ “tăng depth” sang “quality pass”

Sau vòng này, việc thêm nhiều đoạn mới vào từng chapter có nguy cơ làm tài liệu phình nhưng lợi ích biên giảm. Nên ưu tiên bốn loại kiểm toán.

### A. Kiểm toán trùng lặp

Các chủ đề như khả năng tiếp cận, phản hồi, bất cân xứng thông tin, khả năng chống chịu và nền tảng xuất hiện ở nhiều chapter. Cần giữ một nơi giải thích sâu và nơi khác liên kết, tránh mỗi chapter lặp lại cùng định nghĩa dài.

### B. Kiểm toán ví dụ

Mỗi cơ chế quan trọng nên có ít nhất một ví dụ đời sống Hàn Quốc cụ thể, nhưng ví dụ không được biến thành tuyên bố “mọi người đều làm thế”. Ưu tiên ví dụ cho các chapter trừu tượng như `01`, `02`, `16`.

### C. Kiểm toán nguồn và độ mới

Những chapter có số liệu, luật, y tế, chính trị, khí hậu hoặc nền tảng phải gắn mốc thời gian và nguồn. Không cần web cho mọi câu văn; chỉ những tuyên bố có thể đổi hoặc có tranh luận mới cần cập nhật thường xuyên.

### D. Kiểm toán lộ trình học

README/index nên bảo đảm người đọc có thể chọn:

```text
lộ trình nhập môn
lộ trình đời sống hằng ngày
lộ trình công việc
lộ trình lịch sử–truyền thống
lộ trình xã hội hiện đại
lộ trình phương pháp phân tích
```

mà không phải tự đoán thứ tự giữa 33 chapter.

## 7. Các liên kết chéo bắt buộc phải giữ đồng bộ

```text
01 Phương pháp ↔ 16 Mô hình tư duy ↔ 17 Thuật ngữ/nguồn
02 Quan hệ–quyền lực ↔ 03 Ngôn ngữ ↔ 06 Công sở ↔ 18 Quan hệ đời thường
04 Gia đình ↔ 09 Tôn giáo ↔ 11 Nghi lễ ↔ 29 Nuôi dạy con ↔ 15 Dân số
05 Giáo dục ↔ 30 Đại học ↔ 24 Dịch chuyển xã hội ↔ 06 Công sở
06 Công sở ↔ 23 Quân đội ↔ 24 Kinh tế ↔ 27 Nhắn tin ↔ 29 Chăm sóc ↔ 33 Dịch vụ
07 Ẩm thực ↔ 12 Giao hàng ↔ 15 Di cư ↔ 32 Khí hậu ↔ 33 Dịch vụ
08 Nhà ở ↔ 31 Căn hộ ↔ 26 Y tế ↔ 15 Già hoá ↔ 24 Tài chính hộ ↔ 32 Khí hậu
09 Tôn giáo ↔ 11 Nghi lễ ↔ 04 Gia đình ↔ 18 Quan hệ
10 Nghệ thuật/di sản ↔ 13 Hallyu ↔ 21 Ký ức ↔ 27 Hạ tầng số
12 Đô thị ↔ 14 Vùng ↔ 20 Sự kiện ↔ 27 Internet ↔ 31 Căn hộ ↔ 33 Dịch vụ
13 Hallyu ↔ 10 Nghệ thuật ↔ 19 Làm đẹp ↔ 20 Fandom ↔ 24 Kinh tế ↔ 27 Thuật toán
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