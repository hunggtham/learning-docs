# Coverage Status — World Atlas

## Coverage phải tách inventory khỏi learning content

Atlas có inventory rộng và nhiều country/area file từ các batch trước. Sự tồn tại của file **không đồng nghĩa completed content**.

Từ canonical audit hiện tại, Atlas dùng bốn trạng thái:

**Inventory** — tên/mã tồn tại trong global inventory; không yêu cầu chapter riêng.

**Planned** — case có learning value và nằm trong roadmap nhưng chưa đủ chiều sâu.

**Reference** — legacy short file có orientation cơ bản; không nằm trong completion metric.

**Learning profile** — chapter có causal chain đầy đủ và cross-link core; chỉ trạng thái này được tính hoàn chỉnh.

## Definition of Done cho Learning Profile

Profile đủ chuẩn khi:

1. Có spatial thesis rõ: territory được tổ chức bởi cấu trúc nào.
2. Physical base, climate và water được giải thích bằng mechanism.
3. Resource endowment được nối tới khả năng khai thác, processing và network thay vì chỉ liệt kê.
4. Settlement/population được giải thích bằng water, relief, accessibility, history và agglomeration.
5. Economy được nối với production zone, labor, resource, market và institution.
6. Transport được đọc như node–corridor–hinterland–chokepoint network.
7. Society/institution được dùng để giải thích cách constraint vật lý được chuyển thành outcome khác nhau.
8. Hazard được tách thành hazard–exposure–vulnerability.
9. Có misconception/limitation và mental model.
10. Có relative links về core + region; tránh số liệu nhanh lỗi thời nếu không có năm/nguồn.

Một template có đủ heading nhưng chỉ vài câu không đạt Definition of Done.

## Learning profiles ưu tiên cao đã có chiều sâu

Các profile trọng tâm hiện có chiều sâu rõ và tiếp tục được xem là canonical learning cases gồm:

**East Asia:** Republic of Korea, China, Japan.

**Southeast Asia:** Viet Nam là case trọng tâm đã được depth-pass sâu; các ASEAN node khác vẫn được re-audit riêng trước khi gắn nhãn completed.

**North America:** United States.

**Major European economies:** Germany, France, United Kingdom, Italy, Netherlands đã được depth-pass thành selective learning profiles.

Một số Africa profile cũng đã được nâng trong các batch trước và được giữ khi có giá trị cơ chế về Sahel, Nile, Congo Basin, Rift, resource belt hoặc landlocked corridor. Tuy nhiên Atlas không dùng “số Africa profile” như metric ưu tiên mới.

## Planned priority queue

Những case nên được promote tiếp theo **chỉ khi có một batch đủ sâu**, không tạo skeleton trước:

**Korea–Vietnam regional network:** Singapore, Indonesia, Malaysia, Thailand, Philippines.

**Global economy:** India, Brazil, Australia và các economy/corridor có learning value rõ.

**Energy/chokepoint:** Saudi Arabia, Iran, Türkiye, United Arab Emirates, Egypt, Panama và các gateway tương tự.

Planned nghĩa “đáng làm sau”, không phải “đã hoàn thành”.

## Legacy short profiles

Nhiều file 3–25 dòng còn tồn tại từ giai đoạn coverage expansion ở Africa, Americas, Asia và Europe. Các file này mặc định là **Reference**, trừ khi đã được depth-pass rõ.

Không dùng line count như Definition of Done, nhưng một file vài dòng chỉ nêu vị trí/khí hậu chắc chắn không đủ làm learning profile.

Khi cleanup từng subregion, mỗi file nhận một quyết định:

**promote** → learning profile;

**merge** → nhập knowledge vào regional/comparative chapter;

**reference/planned** → giữ navigation nhưng không tính completed;

**remove** → xóa nếu inventory đã đủ và file không thêm learning value.

## Priority theo mechanism, không theo quốc kỳ

Country chỉ đáng ưu tiên nếu giúp học một mechanism có khả năng transfer:

- Korea/Vietnam/China/Japan: demographic transition, manufacturing GVC, port dependency, urban concentration;
- United States: continental market, resource/transport network, urban hierarchy;
- Germany/France/UK/Italy/Netherlands: European production/service/port networks;
- Singapore/Panama/Egypt/Türkiye: gateway/chokepoint logic;
- Gulf exporters: resource–energy–water–trade nexus;
- Brazil/Indonesia: tropical continental/archipelagic scale, commodity/resource and urban networks;
- India: monsoon–population–service/manufacturing–Indian Ocean system.

## Không dùng Atlas để thay Core

Nếu chưa hiểu demographic transition, monsoon, plate tectonics, agglomeration, comparative advantage hoặc chokepoint, phải quay lại core chapter. Profile chỉ minh họa cách nhiều mechanism kết hợp ở một place.

## Completion metric

Metric chính của Atlas là:

**learning profiles có causal depth + cross-link tốt + khả năng transfer mental model**.

Không dùng tổng số `.md`, tỷ lệ country có file hay số heading làm completion metric.