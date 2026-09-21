# Coverage Status — World Atlas

## Coverage phải tách inventory khỏi learning content

Sự tồn tại của `.md` file không đồng nghĩa nội dung hoàn thành. Atlas dùng bốn trạng thái:

- **Inventory**: có tên/mã trong index.
- **Planned**: đáng viết nhưng chưa có full learning content.
- **Reference**: compact legacy note, không tính completion.
- **Learning profile**: đạt Definition of Done và dùng được như chapter ứng dụng.

## Inventory coverage

Inventory toàn cầu đã rộng theo baseline M49 sử dụng trong project. Không cần sinh thêm file để chứng minh completeness của danh sách.

## High-value learning profiles hiện tại

### Korea–Vietnam / East & Southeast Asia

Learning profiles trọng tâm:

- **Republic of Korea**;
- **Viet Nam**;
- **China**;
- **Japan**;
- **Singapore**;
- **Indonesia**;
- **Malaysia**.

Malaysia vừa được promote từ compact reference. Ba ASEAN profiles Singapore–Indonesia–Malaysia hiện cho ba mechanism khác nhau: city-state gateway, tectonic archipelago và two-part manufacturing/resource economy.

### South Asia

- **India** — monsoon–population–urban/manufacturing/service–Indian Ocean system.

### Americas

- **United States** — continental market/resource/transport network;
- **Brazil** — Amazon basin + Atlantic metropolitan belt + interior commodity/resource corridors.

Brazil vừa được promote từ compact reference.

### Europe

Các comparative learning profiles đã có chiều sâu gồm:

- **Germany**;
- **France**;
- **United Kingdom**;
- **Italy**;
- **Netherlands**.

### Oceania

- **Australia** — dry continental interior + coastal metropolitan system + mine/agriculture-to-port corridors + Asian trade network.

Australia vừa được promote và liên kết trực tiếp với regional Oceania chapter.

### Africa

Một số Africa profiles đã qua depth pass và có giá trị case study về Sahel, Nile, Congo Basin, Rift, resource corridors và landlockedness. Tuy nhiên toàn Africa Atlas không được gắn nhãn completed theo file count; QA từng file vẫn cần theo Definition of Done.

## Planned priority — không tạo skeleton trước

Candidates có learning value tiếp theo:

- **Thailand**;
- **Philippines**;
- sau đó mới cân nhắc Saudi Arabia, Iran, Türkiye, UAE, Egypt, Panama hoặc case khác dựa trên mechanism và learning value.

Planned nghĩa là chưa completed. Nếu file legacy đã tồn tại thì giữ Reference/Planned cho tới khi được promote bằng full chapter.

## Legacy short profiles

Các file 3–25 dòng từ giai đoạn coverage được xem là transitional references. Chúng không nằm trong learning route và không được tính completed.

Mỗi file sau audit nhận một trong ba quyết định:

**promote** → viết full learning profile;

**merge** → đưa insight vào regional/comparative chapter;

**remove** → xóa file nếu không tạo learning value ngoài inventory.

Không cần giữ một skeleton chỉ để “mỗi quốc gia có một file”.

## Completion metric

Không dùng số `.md`.

Theo dõi:

- core/region chapters đạt depth standard;
- Atlas learning profiles có causal reasoning;
- quality của prerequisite/application links;
- mức trùng lặp giữa region và country;
- số legacy skeleton được classify/cleanup;
- broken relative links.

## Profile quality gate

Learning profile phải giải thích:

**relief/tectonics/climate/water → resources → settlement/population → production/economy → transport/corridors → urban hierarchy → trade/external dependency → society/institution → hazards → regional role**.

Nếu chỉ có capital, climate, population và vài đoạn economy thì vẫn là Reference.

## Current direction

Core và Regional Geography vẫn có priority cao hơn Atlas long tail. Sau Australia–Brazil–Malaysia, Atlas tạm quay lại trạng thái selective.

Hướng tiếp theo là physical cross-link QA và internal-link validation. Thailand/Philippines chỉ được promote khi có batch đủ chiều sâu, không dùng profile count làm tiêu chí tiến độ.

Xem [Atlas README](./README.md) và [Core Coverage Audit](../CORE_COVERAGE_AUDIT.md).