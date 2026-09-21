# World Atlas — Application Layer của World Geography Knowledge Library

## Atlas không phải coverage game

World Atlas dùng country/territory như **case study** để kiểm tra core Geography. Global inventory có thể rộng nhưng profile học tập có tính chọn lọc.

Không tạo thêm country skeleton chỉ để tăng số file.

## Bốn trạng thái nội dung

**Inventory** — chỉ tồn tại trong global list.

**Planned** — đáng có learning profile nhưng chưa đủ nội dung; không tạo skeleton giả hoàn thành.

**Reference** — file ngắn từ batch cũ, chỉ để định vị/ghi mental model sơ bộ; không tính completion.

**Learning profile** — chapter độc lập đạt causal chain và cross-link chuẩn.

Xem [Coverage Status](./03_coverage_status.md).

## Definition of Done

Một Learning Profile cần có:

1. spatial thesis rõ;
2. physical base: relief/tectonics/climate/water;
3. resources và environmental constraints;
4. population/settlement/urban hierarchy;
5. economy/production zones;
6. transport corridors/ports/gateways;
7. trade/external dependencies;
8. society/institution khi có giá trị địa lý;
9. hazards/exposure/vulnerability;
10. regional/global role;
11. misconceptions/limitations;
12. mental model + relative links tới core/region.

Causal chain mặc định:

**physical geography → resources/water → settlement → economy → transport → urban system → trade → society/institution → regional role**.

Một file có đủ heading nhưng chỉ vài câu vẫn không đạt Definition of Done.

## Learning profiles ưu tiên cao

### East/Southeast Asia

Các profile trọng tâm:

- [Republic of Korea](./asia/eastern_asia/KOR_republic_of_korea.md)
- [China](./asia/eastern_asia/CHN_china.md)
- [Japan](./asia/eastern_asia/JPN_japan.md)
- [Viet Nam](./asia/south_eastern_asia/VNM_viet_nam.md)
- [Singapore](./asia/south_eastern_asia/SGP_singapore.md)
- [Indonesia](./asia/south_eastern_asia/IDN_indonesia.md)
- [Malaysia](./asia/south_eastern_asia/MYS_malaysia.md)

Đây là core Atlas route cho Korea–Vietnam vì cho phép so sánh demographic transition, city systems, manufacturing, archipelago/gateway geography và maritime trade.

### Major continental/global cases

- [India](./asia/southern_asia/IND_india.md)
- [United States](./americas/northern_america/USA_united_states.md)
- [Brazil](./americas/south_america/BRA_brazil.md)
- [Australia](./oceania/australia_new_zealand/AUS_australia.md)

Bốn profile này dùng để so monsoon megaregion, continental market, tropical basin/frontier và dry resource-corridor geography.

### Major European economies

Germany, France, United Kingdom, Italy và Netherlands đã được promote thành comparative learning profiles về manufacturing, service, ports, urban networks và European connectivity.

## Atlas promotions gần nhất

Batch gần nhất **không tạo file mới**. Ba compact references được nâng thành full learning profiles:

- Australia;
- Brazil;
- Malaysia.

Mỗi profile đều dùng causal chain physical → resources → settlement → economy → transport → cities → trade → development/regional role.

## Planned, chưa completed

Thailand và Philippines có learning value cao cho Southeast Asia nhưng vẫn giữ Planned/Reference cho tới khi có thể viết full profile. Không tạo bản tóm tắt 10 dòng để đổi trạng thái.

Các energy/chokepoint cases như Saudi Arabia, Iran, Türkiye, UAE, Egypt hay Panama chỉ được ưu tiên khi bổ sung một mechanism chưa được Atlas hiện tại minh họa tốt.

## Africa profiles

Một số Africa files đã qua depth pass và có giá trị về Sahel, Nile, Congo Basin, Great Rift, landlocked corridors và resource belts. Tuy nhiên chúng vẫn cần QA theo cùng Definition of Done; không có khái niệm “Africa completed” chỉ vì đủ file.

## Khi nào nên merge thay vì giữ country file?

Nếu một file chỉ lặp region chapter và không có mechanism riêng, nên merge knowledge vào subregional/comparative chapter. Inventory vẫn giữ tên/mã nên không mất coverage.

## Atlas phải phụ thuộc core

Nếu chưa hiểu monsoon, tectonics, demographic transition, agglomeration, resource conversion hay chokepoint, quay lại core chapter. Country profile không thay core.

Bắt đầu từ [Learning Route](../LEARNING_ROUTE.md), sau đó mới chọn Atlas profile.