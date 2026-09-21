# Knowledge Library — Địa lý thế giới

Bộ tài liệu này được tổ chức theo **khái niệm (concept) → cơ chế (mechanism) → dependency → relationship → application**. Mục tiêu không phải nhớ country list mà hiểu **vì sao địa hình, khí hậu, tài nguyên, dân cư, thành phố, hạ tầng, thương mại và regional role tạo ra pattern hiện nay**.

> **Mental model trung tâm:** Geography = **pattern + process + network/flow + scale + evidence**.

## Cách dùng library

Nếu học từ đầu, bắt đầu ở [Learning Route](./LEARNING_ROUTE.md). Nếu muốn biết chỗ nào còn yếu, xem [Core Coverage Audit](./CORE_COVERAGE_AUDIT.md).

World Atlas là **application layer**, không phải tiêu chí completion. Một file country ngắn không được tính là chapter hoàn chỉnh chỉ vì nó tồn tại.

## Kiến trúc

`00_foundations` xây geographic thinking, scale, location, coordinates, time zones, cartography, projection, GIS, geospatial data và remote sensing.

`01_physical_geography` giải thích tectonics, geomorphology, atmosphere, weather, climate, hydrology, oceans/coasts, soils/ecosystems và hazards/risk.

`02_human_geography` đi từ population–migration–urbanization tới culture, political/economic geography, agriculture, industry/energy/resources, transport/trade và development/inequality.

`03_regions` tổng hợp core mechanism vào regional systems. Region chapter phải giải thích **physical base → resources/water → settlement → economy → transport → urban network → trade → regional role**, không phải country encyclopedia.

`04_global_systems` nghiên cứu system vượt border: climate change, Water–Food–Energy Nexus, chokepoints/resources, global cities, sustainability và [global trade networks](./04_global_systems/05_global_trade_networks.md).

`05_earth_global_geography` mở rộng sang Địa cầu như một vật thể: geodesy, rotation/orbit, continental–ocean structure, relief, planetary circulation, gravity/geoid, magnetic field, reference systems và human footprint.

`06_world_atlas` dùng country/territory như case study có chọn lọc. Xem [Atlas coverage status](./06_world_atlas/03_coverage_status.md).

`90_connections` nối Geography với Math/Statistics, IT/GIS/Data, Economics/Finance và mental models tổng hợp.

## Dependency graph

```mermaid
graph TD
  A[Geographical thinking] --> B[Coordinates / Maps / GIS]
  A --> C[Earth systems]
  C --> D[Plate tectonics / Geomorphology]
  C --> E[Atmosphere / Climate]
  E --> F[Hydrology / Oceans]
  D --> G[Soils / Ecosystems]
  F --> G
  G --> H[Natural hazards / Risk]
  A --> I[Population]
  I --> J[Migration / Urbanization / Culture]
  J --> K[Economic / Political geography]
  K --> L[Agriculture / Industry / Transport]
  L --> M[Development / Inequality]
  D --> N[Regional geography]
  E --> N
  M --> N
  N --> O[Global systems]
  O --> T[Global trade networks]
  B --> P[GIS / Data applications]
  T --> Q[Selective World Atlas]
```

## Chuỗi causal bắt buộc cho chapter ứng dụng

Khi viết region hoặc country profile, ưu tiên chuỗi:

**địa hình / khí hậu / nước → tài nguyên và constraint → phân bố dân cư → production/economy → transport corridor → urban system → trade network → society/institution → regional/global role → hazard/transformation**.

Đây không phải linear determinism. Institution, technology và history có thể thay đổi hoặc đảo chiều từng arrow.

## Trạng thái sau các depth pass gần nhất

### Core và Physical Geography

Earth Systems và Natural Hazards đã được nâng sâu về system boundary, timescale, coupled processes, expected loss, dynamic vulnerability và infrastructure dependency. Các physical chapter riêng lẻ hiện khá cân bằng; priority mới chuyển sang **cross-link QA** giữa tectonics–relief–sediment–hydrology–coast–hazard thay vì rewrite từng file.

### Human Geography

Culture, Political Geography, Economic Geography và Transport/Trade đã qua integration pass trước đó.

Batch mới nhất nối sâu thêm:

**Agriculture ↔ Industry/Energy/Resources ↔ Development/Inequality**

qua shared chain `resource base → energy/water/input → production/processing → corridor/trade → value capture → household access → inequality/resilience`.

Điều này giúp Human Geography hoạt động như một system thay vì tập hợp sector notes.

### Regional Geography

Europe, Africa, North America, Latin America/Caribbean, South/Central/West Asia đã qua depth pass. Oceania/Pacific và Polar Regions vừa được nâng tiếp.

[Oceania/Pacific](./03_regions/09_oceania_pacific.md) giờ nối island type, water/resources, urban primacy, public-service scale, gateway dependency, food/energy imports, cables, fisheries và Australia–Asia network.

[Polar Regions](./03_regions/10_polar_regions.md) giờ nối ice/permafrost với settlement/service nodes, infrastructure, resource economics, shipping reliability, research logistics và global climate/ocean transmission.

### Global Systems

Global Systems hiện có chapter riêng về [Mạng thương mại toàn cầu](./04_global_systems/05_global_trade_networks.md), nối production tiers, resources, ports, inventory, finance, cities và systemic risk.

### Selective Atlas

Không tăng số skeleton. Các compact files chỉ được promote khi đủ chiều sâu.

Batch mới đã nâng:

- [Australia](./06_world_atlas/oceania/australia_new_zealand/AUS_australia.md);
- [Brazil](./06_world_atlas/americas/south_america/BRA_brazil.md);
- [Malaysia](./06_world_atlas/asia/south_eastern_asia/MYS_malaysia.md).

Chúng được chọn vì có learning value về resources, commodity/industrial networks, ports, urban systems và liên hệ East/Southeast Asia.

## Quy tắc chất lượng

Một chapter tốt phải trả lời: khái niệm là gì; mechanism nào tạo pattern; stock/flow/node/boundary nào quan trọng; physical constraint và resource nào tác động; scale nào làm kết luận đổi; evidence đo bằng gì; limitation/misconception ở đâu; chapter nối sang system nào.

Số file, số heading và số dòng không phải metric chất lượng.

## Quy tắc ngôn ngữ

Giải thích chính bằng tiếng Việt tự nhiên. English keyword giữ trong ngoặc khi giúp tra cứu, ví dụ `khả năng tiếp cận (accessibility)`, `tự tương quan không gian (spatial autocorrelation)`, `chuỗi giá trị toàn cầu (global value chain)`.

Code, formula, acronym, proper noun và canonical technical name giữ nguyên nếu dịch làm mất chính xác.

## Roadmap tiếp theo

Ưu tiên mới sau batch hiện tại:

**physical cross-link QA → population/urban/development causal examples → regional prerequisite/application links → selective Thailand/Philippines profiles nếu đủ chiều sâu → Atlas reference cleanup → internal-link validation**.

Không quay lại chiến lược sinh hàng trăm country skeleton.