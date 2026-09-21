# Core Coverage Audit — World Geography Knowledge Library

## Mục đích

Audit này đo **độ sâu, khả năng giải thích và liên kết khái niệm**, không đếm file. Một topic chỉ được coi là vững khi người đọc có thể đi từ concept → mechanism → evidence/model → limitation → cross-link → application mà không phải dựa vào country fact sheet.

Trạng thái dùng ở đây:

- **Deep**: đủ làm tài liệu học chính.
- **Depth pass**: vừa được nâng đáng kể; ưu tiên QA/cross-link hơn rewrite toàn bộ.
- **Solid**: đúng và khá sâu nhưng còn một số bridge quan trọng cần bổ sung.

## Foundations

| Nhóm | Trạng thái | Ghi chú |
|---|---|---|
| Geographic thinking / scale / location | **Deep** | Pattern→process, relational location, accessibility, scale–extent–resolution, network/flow, path dependence, uncertainty. |
| Coordinates / time zones | **Deep** | Angular coordinates, datum/CRS, great-circle logic, UTC/local civil time. |
| Maps / cartography / projections | **Deep** | Generalization, projection trade-off, choropleth, MAUP, classification và web mapping. |
| GIS / geospatial data / remote sensing | **Deep** | Vector/raster, topology, spatial predicates/index, geodesic/network distance, observation pipeline, validation, uncertainty/privacy. |
| Earth systems | **Depth pass** | System boundary, stock–flow, residence time, coupled systems, threshold, cross-scale feedback, critical zone và coupled human–natural systems. |

## Physical Geography

| Nhóm | Trạng thái | Ghi chú |
|---|---|---|
| Geological time / plate tectonics | **Deep** | Plate driving forces, boundaries, magma generation, earthquake mechanics, geologic timescale. |
| Geomorphology | **Deep** | Weathering/erosion/mass movement, fluvial/coastal/glacial/karst/desert systems, sediment routing. |
| Atmosphere / weather | **Deep** | Stability, adiabatic processes, fronts, jets, tropical cyclone, NWP/ensemble, observation bias. |
| Climate | **Deep** | Energy balance, ocean memory, ENSO, classification, proxy/paleoclimate, spatial heterogeneity. |
| Hydrology | **Deep** | Basin balance, hydrograph/baseflow, groundwater/Darcy, sediment, drought lag, reservoir trade-off, water security. |
| Oceans / coasts | **Deep** | Stratification, gyres/Ekman/upwelling, overturning, tides/waves, sediment cells, delta/estuary, ports/cables. |
| Soils / biomes / ecosystems | **Deep** | CLORPT, CEC/pH, nutrient cycling, disturbance, succession, fragmentation, biome dynamics, degradation. |
| Natural hazards / risk | **Depth pass** | Expected loss, dynamic vulnerability, compound/cascading risk, infrastructure dependency, adaptation options, resilience. |

### Physical cross-link còn cần QA

Các chapter riêng lẻ đã sâu; khoảng trống tiếp theo nằm ở **bridge giữa process**. Cần tiếp tục kiểm tra các chuỗi:

**tectonics → relief → sediment → river/delta/coast → settlement/risk**;

**atmosphere/climate → water balance → soil/ecosystem → agriculture → hazard**;

**ocean/coast → port/city → trade → compound coastal risk**.

Mục tiêu của pass sau không phải tăng độ dài từng file mà làm prerequisite/application links rõ hơn.

## Human Geography

| Nhóm | Trạng thái | Ghi chú |
|---|---|---|
| Population | **Deep** | Stock–flow, fertility/mortality, cohort/period, momentum, density, census/registry, projections. |
| Migration | **Deep** | Aspiration–capability–pathway, selectivity, gravity, intervening opportunities, network, displacement, data limits. |
| Urbanization | **Deep** | Agglomeration, site/situation, bid-rent, transport–land-use feedback, polycentric regions, housing/informal settlement, infrastructure risk. |
| Culture / language / religion | **Depth pass** | Physical setting, settlement, language network, migration/diaspora, urbanization, cultural economy và place identity đã được nối. |
| Political geography / borders | **Depth pass** | Terrain/resources, borderland, state morphology, infrastructure integration, chokepoints, multi-level governance và map provenance. |
| Economic geography | **Depth pass** | Physical cost surface, resource/value capture, forward/backward linkages, labor/urban systems, GVC, corridors và Korea–Vietnam. |
| Agriculture / food systems | **Depth pass** | Vừa nâng thành full chain climate/soil/water → energy/input → farm → processing/logistics → trade → household food access/development. |
| Industry / resources / energy | **Depth pass** | Vừa nối resource → energy/water → processing → supplier cluster → city/labor → corridor → trade → value capture → development. |
| Transport / trade / globalization | **Depth pass** | Terrain reliability, corridor development, multimodal network, multi-tier dependency, sea-port-inland chain và Korea–Vietnam network. |
| Development / inequality | **Depth pass** | Vừa nối resource conversion, infrastructure reliability, corridor/value capture, structural transformation, natural capital, just transition và place-based inequality. |

### Human integration hiện tại

Agriculture, energy/resources và development không còn đứng như ba sector riêng. Shared mental model hiện là:

**resource base → infrastructure/energy → productivity → processing/value capture → transport/trade → city/household access → inequality/resilience**.

Pass tiếp theo nên kiểm tra trùng lặp, thêm quantitative examples khi thật sự giúp reasoning và giữ cross-links hai chiều.

## Regional Geography

| Region | Trạng thái | Ghi chú |
|---|---|---|
| East Asia | **Deep** | High interior–monsoon rivers–dense eastern lowlands–industrial maritime networks; Korea route mạnh. |
| Southeast Asia | **Deep** | Mainland/archipelago contrast, monsoon/Mekong, straits, production networks, Vietnam link. |
| South Asia | **Deep** | Himalaya–plain–monsoon–groundwater–megacities–Indian Ocean. |
| Central Asia | **Deep** | Continentality–mountain water–endorheic basin–resources–transit corridors. |
| West Asia | **Deep** | Aridity–water–energy–ports/pipelines–chokepoints–urban systems. |
| Europe | **Depth pass** | River/port corridors, polycentric cities, energy mismatch, industry, aging, tourism và global connectivity. |
| Africa | **Depth pass** | Plateau/basin, rainfall/water, corridors, urbanization, agriculture/resources, value capture và market access. |
| North America | **Depth pass** | Continental freight, Gulf/Pacific gateways, tech clusters, water/energy, cross-border production. |
| Latin America & Caribbean | **Depth pass** | Andes/basins, frontier, resource/value chain, primate cities, migration/tourism, trade gateways. |
| Oceania / Pacific | **Depth pass** | Vừa nâng ocean-as-network, small-island scale, urban primacy, public-service cost, food/energy import dependence, cables, fisheries và Australia–Asia links. |
| Polar regions | **Depth pass** | Physical systems được nối thêm settlement/service centrality, permafrost infrastructure, resource-project economics, fisheries, polar logistics và global climate transmission. |

Regional chapters hiện đều phải dùng cùng chain:

**physical base → water/resources → settlement → economy → transport → urban hierarchy → trade → regional role → hazard/transformation**.

Không dùng regional chapter như country encyclopedia.

## Global Systems

| System | Trạng thái | Ghi chú |
|---|---|---|
| Climate change | **Deep** | Forcing–feedback–ocean inertia–carbon stock/flow–extremes–attribution–adaptation. |
| Water–Food–Energy Nexus | **Deep** | Multi-objective trade-offs, groundwater, desalination, virtual water, urban nexus, resilience. |
| Resources / chokepoints | **Deep** | Dependency graph, substitution, full value chain, route redundancy. |
| Global cities | **Deep** | Network centrality, command functions, megaregions, infrastructure/housing dependencies. |
| Sustainability | **Deep** | Stock–flow, system boundary, externalities, LCA, circularity limits, rebound, resilience/governance. |
| Global trade networks | **Deep** | Production tiers, ports/hinterlands, inventory, finance, resource conversion, city networks, systemic risk và Korea–Vietnam application. |

## Earth / Global Geography

Geodesy, rotation/orbit/seasons, continental–ocean structure, global relief, planetary circulation, gravity/geoid/magnetic field, reference systems và human footprint đều có canonical chapters. Recent depth pass đã cân bằng `continents/ocean basins`, `global relief` và `global circulation` với phần core khác.

## World Atlas

Atlas **không phải core coverage metric**. Inventory rộng không đồng nghĩa learning content hoàn chỉnh.

High-value learning profiles hiện gồm:

- Korea, Vietnam, China, Japan;
- Singapore, Indonesia, Malaysia, India;
- United States;
- Germany, France, United Kingdom, Italy, Netherlands;
- Australia và Brazil;
- một số Africa profiles đã qua depth pass và tiếp tục được QA theo cùng Definition of Done.

Australia, Brazil và Malaysia vừa được promote từ compact reference thành learning profiles. Không tạo file mới trong batch này.

Thailand và Philippines vẫn là **Planned/Reference** cho tới khi có thể viết full learning profile; không nâng bằng skeleton.

## Khoảng trống tiếp theo

1. **Physical cross-link QA**: tectonics/geomorphology ↔ hydrology/sediment ↔ coasts/hazards.
2. **Population–urban–development bridge**: thêm causal examples và quantitative reasoning có chọn lọc, tránh lặp định nghĩa.
3. **Regional cross-link QA**: mỗi region nên trỏ tới core prerequisites và 1–3 Atlas learning cases có giá trị thật.
4. **Selective Atlas**: Thailand/Philippines chỉ promote nếu đạt full profile; long tail giữ Reference/Inventory.
5. **Atlas cleanup**: classify legacy short files thành `reference / merge / remove`; không dùng file count làm metric.
6. **Internal-link validation** sau depth passes lớn, ưu tiên broken relative links và duplicate concept.