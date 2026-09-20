# Korean Culture — Coverage Audit

> File này không phải chapter học riêng. Nó là **bản kiểm toán coverage** để tránh việc Master Knowledge Book phát triển theo cảm tính, lặp chủ đề hoặc bỏ sót subsystem quan trọng. Phạm vi audit là các file `01`–`33`, không tính `kiip/`.

## Tiêu chí đánh giá

Một domain được coi là cover tốt khi không chỉ liệt kê fact mà trả lời được sáu câu hỏi:

```text
1. What — hiện tượng/khái niệm là gì?
2. Why — tại sao nó xuất hiện hoặc trở nên salient?
3. Mechanism — institution/material/incentive nào duy trì?
4. Variation — khác theo thế hệ, class, region, setting ra sao?
5. Change — technology/economy/law làm nó đổi thế nào?
6. Boundary — khi nào explanation này không còn đúng?
```

Mỗi chapter cũng nên có ít nhất một `Mental Model`, phần `Common Misconceptions`, keyword Korean–English–Vietnamese và cross-link khi concept phụ thuộc chapter khác.

## Coverage map hiện tại

| Domain | Chapter chính | Trạng thái | Gap còn lại |
|---|---|---|---|
| Cultural-system foundation | `01` | mạnh | tiếp tục timestamp các current statistic khi thêm mới |
| Historical layers | `21` | mạnh | có thể bổ sung sâu memory of colonial/war everyday life nhưng không lặp `korean_history/` |
| Confucianism & hierarchy | `02` | mạnh | cần giữ distinction descriptive vs normative |
| Names, age, metadata | `22` | mạnh | có thể bổ sung naming in digital/global workplace |
| Language, honorifics, relational concepts | `03` | mạnh | pronunciation/dialect để `14`, không trộn grammar textbook |
| Family, kinship, lifecycle | `04` + `29` | mạnh | queer/non-traditional household có thể được bổ sung khi có source phù hợp |
| Education & credential | `05` + `30` | mạnh | vocational pathway, adult reskilling cần theo dõi thêm |
| Workplace | `06` | mạnh | remote/hybrid/global-team change có thể cập nhật theo thời gian |
| Military lifecycle | `23` | khá mạnh | cần tránh biến experience nam giới thành universal citizen experience |
| Economy, housing, mobility | `24` | mạnh sau vòng hiện tại | tax/loan/policy phải để source hiện hành, không hard-code |
| Food & drinking | `07` | mạnh | có thể thêm food safety/allergy/vegetarian adaptation sau |
| Seasons & climate | `32` | mạnh | climate trend cần timestamp nếu đưa số liệu |
| Home, hanok, clothing | `08` + `31` | mạnh | accessibility/universal design trong apartment còn có thể mở rộng |
| Religion & worldview | `09` | mạnh | new religious movements chỉ thêm khi có nguồn học thuật đáng tin |
| Arts, craft, heritage | `10` | mạnh | contemporary museum/gallery ecosystem còn tương đối mỏng |
| Holidays, rites, games | `11` | mạnh | local festivals phân tán sang `14` |
| City, consumption, digital life | `12` | mạnh sau vòng hiện tại | urban accessibility và night economy có thể update thêm |
| Service/review culture | `33` | mạnh | labour condition nên cross-link workplace/economy |
| Internet/messaging/meme | `27` | mạnh sau vòng hiện tại | platform slang cần timestamp vì decay nhanh |
| Hallyu/media/platform | `13` | mạnh | copyright/creator labour có thể tiếp tục sâu hơn |
| Everyday etiquette/relationships | `18` | mạnh | context variation là ưu tiên, tránh rule-list |
| Beauty/fashion/body | `19` | mạnh sau vòng hiện tại | source quantitative về procedure/body image nếu thêm phải population-specific |
| Sports/leisure/fandom | `20` | mạnh sau vòng hiện tại | disability/adaptive sport và senior leisure có thể bổ sung |
| Health/wellness | `26` | mạnh sau vòng hiện tại | end-of-life/palliative care và disability system còn mỏng |
| Regions/Jeju/diaspora | `14` | mạnh | individual regional stereotype phải tiếp tục được chống ecological fallacy |
| Demography/migration | `15` | mạnh sau vòng hiện tại | immigration category/statistic phải định nghĩa denominator |
| Civic/media/public sphere | `25` | mạnh về framework | current political facts cần source mới mỗi lần update |
| Cross-system connections | `16` | mạnh | update khi thêm mechanism mới |
| Glossary/reference map | `17` | tốt | cần sync keyword mới từ 12/15/19/20/24/26/27 |
| Naming convention | `28` | tốt | maintain consistency Việt–Hàn–Anh |

## Các gap quan trọng chưa cần tạo chapter mới

### 1. Disability, accessibility và universal design

Hiện nội dung xuất hiện rải rác trong health, ageing và kiosk/digital divide nhưng chưa được nối thành một model rõ. Không nhất thiết tạo file mới; có thể bổ sung vào `12`, `26`, `31` và `15` theo ba layer:

```text
physical accessibility
→ building / transit / street

digital accessibility
→ kiosk / app / authentication

social accessibility
→ support / communication / stigma
```

Mục tiêu là tránh coi disability chỉ là medical condition; environment quyết định mức participation rất lớn.

### 2. End-of-life, hospice và death literacy

`04` đã cover funeral, `26` cover care medicine nhưng end-of-life decision, hospice/palliative care, advance planning và caregiver grief vẫn mỏng. Đây là gap quan trọng trong ageing society.

Nên bổ sung khi có source institutional/medical tốt; không viết như medical advice.

### 3. Contemporary art, museum và cultural venue

`10` mạnh về traditional art nhưng contemporary visual art, museum, gallery, biennale, independent performance và cultural foundation chưa sâu. Phần này có thể bổ sung vào `10` mà không cần chapter mới.

### 4. Creator labour và intellectual property

`13` cover Hallyu/platform mạnh, nhưng labour phía sau writer, animator, webtoon creator, dancer, producer, translator và copyright revenue còn có thể sâu hơn. Nên nối với `06` workplace và `24` economy.

### 5. Accessibility của housing và ageing-in-place

`08/31` giải thích apartment rất kỹ, nhưng `무장애`, elevator, bathroom safety, senior-friendly housing và ageing-in-place chưa thành một causal chain rõ. Có thể bổ sung mà không tạo chapter riêng.

### 6. Food adaptation trong society đa dạng hơn

`07` có foundation food mạnh, `15` có migration, nhưng halal/vegetarian/allergy, school/workplace meal adaptation và international ingredient market chưa nối rõ. Đây là dấu hiệu culture chuyển từ “default meal assumption” sang heterogeneous preference.

### 7. Work from home / hybrid / digital nomad boundary

`06`, `12`, `27` đã có tool và messaging culture, nhưng hybrid work thay reporting, presence signal, apartment space và after-hours boundary như thế nào vẫn có thể bổ sung.

## Cross-link gaps cần giữ đồng bộ

Các cặp sau phải luôn được review cùng nhau khi update:

```text
04 Family ↔ 29 Parenting ↔ 15 Demography
05 Education ↔ 30 Campus ↔ 24 Mobility
06 Workplace ↔ 23 Military ↔ 24 Economy
07 Food ↔ 32 Seasons ↔ 15 Migration
08 Home ↔ 31 Apartment ↔ 24 Housing
09 Religion ↔ 11 Rites ↔ 04 Family
10 Heritage ↔ 13 Hallyu
12 City ↔ 27 Internet ↔ 33 Service
13 Hallyu ↔ 19 Beauty ↔ 20 Fandom
15 Demography ↔ 26 Health ↔ 31 Housing
18 Relationships ↔ 03 Language ↔ 27 Messaging
```

Nếu một chapter thay mental model nhưng cặp liên quan không được update, library sẽ dần mâu thuẫn nội bộ.

## Những thứ cố ý không biến thành chapter riêng

Bộ sách không nên tách vô hạn thành các file cực nhỏ. Một chủ đề chỉ nên thành chapter độc lập nếu nó có **causal system riêng**, nhiều cross-link và đủ depth để đọc như một unit.

Các topic sau hiện nên giữ embedded:

- cafe culture → `12`;
- pet culture → `15`/`18`;
- wedding/funeral → `04`/`18`;
- self-photo booth → `19`/`18`;
- running crew → `20`;
- kiosk → `12`/`15`;
- supplement → `26`;
- personal color → `19`;
- review culture → `33` + `12`/`27`.

Tách chúng thành chapter riêng lúc này sẽ tăng navigation cost hơn learning value.

## Data freshness policy

Các chapter văn hoá dễ vô tình biến số liệu cũ thành “bản chất Hàn Quốc”. Vì vậy:

- demographic statistic phải ghi **data year**;
- survey phải ghi **population/sample definition**;
- projection phải ghi rõ **projection**;
- current policy/law phải dùng source hiện hành;
- platform/slang phải có timestamp vì decay nhanh;
- medical efficacy claim phải dựa evidence chuyên môn, không dựa popularity;
- political/current public-sphere claim phải được verify bằng nguồn mới trước khi update.

## Depth audit

Sau các vòng nâng cấp gần đây, các chapter từng mỏng nhất `01`, `04`, `05`, `08`, `11`, `12`, `13`, `14`, `15`, `19`, `20`, `24`, `26`, `27` đã được mở rộng đáng kể. Vấn đề chính của library hiện tại không còn là “thiếu chapter lớn”, mà là ba việc:

1. **sync glossary/cross-links** với keyword mới;
2. **bổ sung gap transversal** như accessibility, end-of-life, creator labour;
3. **duy trì freshness** cho số liệu, platform và policy.

Điều này có nghĩa giai đoạn tiếp theo nên ưu tiên **deepening + consistency**, không ưu tiên tạo thêm hàng loạt file.

## Definition of Done cho một chapter

Một chapter được coi “khá hoàn chỉnh” khi người đọc sau khi đọc có thể:

- giải thích concept bằng lời của mình;
- nêu ít nhất hai mechanism, không chỉ fact;
- phân biệt pattern group với individual certainty;
- cho ví dụ daily life;
- nhận ra ít nhất một trade-off;
- biết chapter nào cần đọc tiếp;
- nhận ra statistic/policy nào có thể outdated;
- tránh 2–4 misconception phổ biến.

Master Knowledge Book không có trạng thái “vĩnh viễn hoàn thành”, vì culture thay đổi. Mục tiêu thực tế là **coverage đủ rộng, mechanism đủ sâu, terminology nhất quán và update path rõ ràng**.
