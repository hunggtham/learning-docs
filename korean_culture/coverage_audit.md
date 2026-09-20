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
| Ngôn ngữ, kính ngữ, `눈치`, `정`, `체면` | `03` | mạnh | có thể đào sâu giao tiếp đa ngôn ngữ và môi trường toàn cầu |
| Gia đình, họ tộc, vòng đời | `04` + `29` | rất mạnh sau vòng mới | `29` đã thêm cú sốc chăm sóc, tải quản lý vô hình và quyền tự chủ của trẻ |
| Giáo dục, thi cử, bằng cấp | `05` + `30` | rất mạnh sau vòng mới | đã thêm học tập suốt đời, chuyển nghề, kỹ năng chuyển giao và đại học như hệ ghép nối |
| Công sở | `06` | mạnh, đã mở rộng | giữ đồng bộ với `05`, `29`, `30` khi cập nhật kỹ năng và chăm sóc |
| Ẩm thực | `07` | mạnh | có thể bổ sung sâu hơn kinh tế chuỗi cung ứng thực phẩm nếu cần |
| Nhà ở, hanok, không gian | `08` + `31` | mạnh | giữ liên kết với già hoá, di cư và tài chính hộ |
| Tôn giáo và thế giới quan | `09` | mạnh | chỉ thêm phong trào mới khi có nguồn học thuật tốt |
| Nghệ thuật, thủ công, di sản | `10` | mạnh | có thể đào sâu kinh tế sáng tạo và bảo tồn số cùng `13` |
| Lễ Tết, nghi lễ, trò chơi | `11` | mạnh | giữ liên kết với gia đình, du lịch và vùng miền |
| Đô thị, tiêu dùng, đời sống số | `12` | mạnh | đã có hành trình đô thị không rào cản và khả năng tiếp cận số |
| Hallyu, truyền thông, nền tảng | `13` | mạnh | đã có lao động sáng tạo, quyền tác giả, quyền chuyển thể và phân phối giá trị |
| Vùng miền, Jeju, bán đảo | `14` | mạnh | có thể đào sâu quan hệ giữa vùng, việc làm và di chuyển dân số |
| Dân số, già hoá, di cư | `15` | rất mạnh sau vòng mới | đã thêm hợp đồng thế hệ, độ trễ thiết chế, ngưỡng dịch vụ và chuỗi hội nhập di cư |
| Liên hệ giữa các hệ thống | `16` | rất mạnh sau vòng mới | đã mở từ 23 lên 30 mô hình liên hệ và thêm lớp đo lường |
| Thuật ngữ và bản đồ nguồn | `17` | đã đồng bộ vòng mới | đã thêm thuật ngữ từ 05, 12, 15, 22, 26, 29, 30 |
| Phép lịch sự và quan hệ đời thường | `18` | mạnh | ưu tiên đào sâu ranh giới cá nhân, mạng quan hệ và chi phí duy trì quan hệ |
| Làm đẹp, thời trang, cơ thể | `19` | mạnh | số liệu về thủ thuật phải ghi rõ quần thể |
| Thể thao, giải trí, fandom | `20` | mạnh | đã có thể thao thích ứng, giải trí người cao tuổi và bất bình đẳng thời gian |
| Các lớp lịch sử | `21` | mạnh | có thể sâu hơn về ký ức lịch sử trong đời sống thường ngày mà không lặp `korean_history/` |
| Tên, tuổi, siêu dữ liệu xã hội | `22` | rất mạnh sau vòng mới | đã thêm tên pháp lý/hiển thị, La-tinh hoá, danh tính số và tối thiểu hoá dữ liệu |
| Nghĩa vụ quân sự | `23` | khá mạnh | có thể đào sâu tái hội nhập vào học tập/công việc sau nghĩa vụ |
| Kinh tế, chaebol, nhà ở, dịch chuyển xã hội | `24` | mạnh | ưu tiên vòng sâu tiếp theo về bảng cân đối hộ, rủi ro và truyền tài sản liên thế hệ |
| Xã hội dân sự và không gian công luận | `25` | mạnh về khung phân tích | dữ kiện chính trị hiện hành luôn phải kiểm chứng mới |
| Y tế và văn hoá sức khoẻ | `26` | mạnh | đã có khuyết tật, khả năng tiếp cận, chăm sóc giảm nhẹ và cuối đời |
| Internet, nhắn tin, tiếng lóng, meme | `27` | mạnh | có thể đào sâu thuật toán, chất lượng thông tin và quản trị danh tính số |
| Quy ước tên riêng | `28` | tốt | giữ nhất quán Việt–Hàn–Anh |
| Nuôi dạy con và chăm sóc | `29` | rất mạnh sau vòng mới | đã thêm chất lượng chăm trẻ, trẻ ốm, nghỉ chăm con, vai trò cha và tải quản lý vô hình |
| Đại học và thanh niên | `30` | rất mạnh sau vòng mới | đã thêm đăng ký môn, GPA, bài tập nhóm, phòng nghiên cứu, thực tập và nhà ở sinh viên |
| Căn hộ, khu dân cư | `31` | mạnh | đã có thiết kế phổ quát, nhà thông minh hỗ trợ chăm sóc và già hoá tại nơi ở quen thuộc |
| Mùa, khí hậu, môi trường | `32` | mạnh | xu hướng khí hậu phải gắn mốc thời gian |
| Dịch vụ, khách hàng, đánh giá | `33` | mạnh | tiếp tục liên kết điều kiện lao động với `06`, `12`, `24` |

## 4. Những nâng cấp độ sâu vừa hoàn thành

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

[`29_childhood_parenting_care_institutions.md`](29_childhood_parenting_care_institutions.md) đã vượt khỏi mô hình “cha mẹ đầu tư cho con” và thêm:

- chất lượng chăm trẻ thay vì chỉ số lượng chỗ;
- cú sốc khi trẻ ốm;
- khác biệt giữa quyền nghỉ chính thức và chi phí không chính thức;
- vai trò người cha như chủ thể chăm sóc;
- tải quản lý vô hình;
- dữ liệu/camera trong nuôi con;
- quyền tự chủ tăng dần của trẻ;
- mạng chăm sóc giữa gia đình–trường–y tế.

### Dân số như hợp đồng giữa các thế hệ

[`15_contemporary_change_demography_migration.md`](15_contemporary_change_demography_migration.md) đã thêm:

```text
cấu trúc tuổi ≠ trạng thái việc làm ≠ nhu cầu chăm sóc
```

và các mô hình:

- tỷ số phụ thuộc và giới hạn của nó;
- hợp đồng giữa các thế hệ;
- độ trễ thiết chế trong già hoá nhanh;
- nhà ở như hạ tầng vòng đời;
- di cư như một đường ống nhiều giai đoạn;
- năng lực hiểu thiết chế của người di cư;
- thế hệ thứ hai và danh tính;
- chuỗi chăm sóc xuyên biên giới;
- hiệu ứng ngưỡng khi dịch vụ địa phương đóng;
- chuỗi nhân quả để đánh giá chính sách.

### Danh tính từ quan hệ trực tiếp sang hệ thống số

[`22_names_age_identity_social_metadata.md`](22_names_age_identity_social_metadata.md) đã mở rộng từ tên–tuổi sang:

```text
tên pháp lý
≠ tên hiển thị
≠ danh xưng
≠ biệt danh / tài khoản số
```

Chương cũng nối La-tinh hoá tên, người nước ngoài, danh xưng công sở toàn cầu, nickname, phân nhóm theo tuổi và tối thiểu hoá dữ liệu.

### Chương liên hệ đã chuyển từ “tổng hợp” sang công cụ phân tích

[`16_connections_mental_models_misconceptions.md`](16_connections_mental_models_misconceptions.md) hiện có 30 liên hệ xuyên chương. Khung phân tích cũng được nâng từ năm lên sáu lớp bằng việc thêm **lớp đo lường**:

```text
vật chất
→ thiết chế
→ quan hệ
→ biểu tượng
→ lịch sử
→ đo lường
```

Điều này buộc người đọc hỏi không chỉ “cơ chế là gì?” mà còn “ta biết điều đó bằng dữ liệu nào?”.

### Glossary đã được đồng bộ

[`17_glossary_and_reference_map.md`](17_glossary_and_reference_map.md) đã nhận thêm các nhóm thuật ngữ mới về:

- học tập suốt đời và chuyển nghề;
- campus và nghiên cứu;
- chăm sóc và nghỉ chăm con;
- khả năng tiếp cận;
- dân số/di cư;
- danh tính số;
- chăm sóc cuối đời;
- các khái niệm phân tích xuyên chương.

## 5. Ưu tiên cho vòng tăng độ sâu tiếp theo

Thư viện hiện không thiếu các chương lớn. Phần tiếp theo nên tập trung vào **failure mode, trade-off và interaction** trong các chương còn mạnh về mô tả nhưng chưa sâu bằng nhóm vừa nâng cấp.

### Ưu tiên A — `24`: kinh tế hộ gia đình và dịch chuyển xã hội

Nên đào sâu:

```text
thu nhập ≠ dòng tiền ≠ tài sản ≠ thanh khoản
```

và quan hệ giữa nợ, nhà ở, giáo dục, kết hôn, hỗ trợ từ cha mẹ, tự kinh doanh, rủi ro thất nghiệp và truyền tài sản giữa thế hệ.

### Ưu tiên B — `18`: quan hệ đời thường và ranh giới

Nên đi sâu cách một mạng quan hệ được duy trì bằng thời gian, quà, phản hồi, `경조사`, chat nhóm và sự có mặt. Cần thêm mô hình **ngân sách quan hệ (relationship budget)** để giải thích vì sao cùng một phép lịch sự có thể là gắn kết hoặc gánh nặng.

### Ưu tiên C — `27`: nền tảng, thuật toán và chất lượng thông tin

Nên tách rõ:

```text
phổ biến
≠ đại diện
≠ đáng tin
≠ đúng
```

và mở rộng cách thuật toán đề xuất, nội dung tạo sinh, danh tính ẩn danh và ảnh chụp màn hình thay cấu trúc niềm tin.

### Ưu tiên D — `21`: ký ức lịch sử trong đời sống thường ngày

Không lặp niên đại `korean_history/`, mà tập trung cách ký ức chiến tranh, công nghiệp hoá, đô thị hoá và dân chủ hoá xuất hiện trong gia đình, địa danh, bảo tàng, phim ảnh và khác biệt thế hệ.

## 6. Các liên kết chéo bắt buộc phải giữ đồng bộ

```text
04 Gia đình ↔ 29 Nuôi dạy con ↔ 15 Dân số
05 Giáo dục ↔ 30 Đại học ↔ 24 Dịch chuyển xã hội ↔ 06 Công sở
06 Công sở ↔ 23 Quân đội ↔ 24 Kinh tế ↔ 27 Nhắn tin ↔ 29 Chăm sóc
07 Ẩm thực ↔ 15 Di cư ↔ 32 Mùa
08 Nhà ở ↔ 31 Căn hộ ↔ 26 Y tế ↔ 15 Già hoá ↔ 24 Tài chính hộ
09 Tôn giáo ↔ 11 Nghi lễ ↔ 04 Gia đình
10 Nghệ thuật/di sản ↔ 13 Hallyu
12 Đô thị ↔ 27 Internet ↔ 31 Căn hộ ↔ 33 Dịch vụ
13 Hallyu ↔ 19 Làm đẹp ↔ 20 Fandom ↔ 24 Kinh tế ↔ 06 Lao động
18 Quan hệ ↔ 03 Ngôn ngữ ↔ 22 Danh tính ↔ 27 Nhắn tin
15 Dân số ↔ 22 Danh tính ↔ 26 Y tế ↔ 29 Chăm sóc
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
- khi thêm số liệu giáo dục, việc làm hoặc di cư phải giữ nguyên định nghĩa mẫu và không suy rộng quá phạm vi.

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
- tránh các hiểu lầm phổ biến;
- đọc phần giải thích chủ yếu bằng tiếng Việt nhưng vẫn có đủ từ khoá Anh–Hàn để tra cứu.

Master Knowledge Book không có trạng thái “vĩnh viễn hoàn thành”. Trạng thái mục tiêu là **phạm vi đủ rộng, cơ chế đủ sâu, thất bại đủ rõ, thuật ngữ nhất quán, tiếng Việt dễ đọc và đường cập nhật rõ ràng**.