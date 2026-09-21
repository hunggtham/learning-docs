# Core Coverage Audit — World Geography Knowledge Library

## Mục đích

Audit này đo **độ sâu và liên kết khái niệm**, không đếm file. Một topic được coi là vững khi có concept → mechanism → model/evidence → limitation → cross-link và có thể dùng để giải thích region/country mà không dựa vào fact list.

Trạng thái dùng ở đây: **Deep** = đủ làm tài liệu học chính; **Depth pass** = vừa được nâng đáng kể và cần QA/link pass hơn là rewrite; **Solid** = đúng và khá sâu nhưng còn scope mở rộng.

## Foundations

| Nhóm | Trạng thái | Ghi chú |
|---|---|---|
| Geographic thinking / scale / location | **Deep** | Pattern→process, relational location, accessibility, scale–extent–resolution, network/flow, path dependence, uncertainty. |
| Coordinates / time zones | **Deep** | Angular coordinates, datum/CRS, great-circle logic, UTC/local civil time. |
| Maps / cartography / projections | **Deep** | Generalization, projection trade-off, choropleth, MAUP, classification và web mapping. |
| GIS / geospatial data / remote sensing | **Deep** | Vector/raster, topology, spatial predicates/index, geodesic/network distance, observation pipeline, validation, uncertainty/privacy. |
| Earth systems | **Depth pass** | Mới mở rộng system boundary, stock–flow, residence time, coupling, threshold, cross-scale feedback, critical zone và coupled human–natural systems. |

## Physical Geography

| Nhóm | Trạng thái | Ghi chú |
|---|---|---|
| Geological time / plate tectonics | **Deep** | Plate driving forces, boundaries, magma generation, earthquake mechanics, geologic timescale. |
| Geomorphology | **Deep** | Weathering/erosion/mass movement, fluvial/coastal/glacial/karst/desert systems và sediment logic. |
| Atmosphere / weather | **Deep** | Vertical structure, stability, adiabatic processes, fronts, jets, tropical cyclone, NWP/ensemble/observation bias. |
| Climate | **Deep** | Energy balance, ocean memory, ENSO, classification, proxy/paleoclimate và spatial heterogeneity. |
| Hydrology | **Deep** | Basin balance, hydrograph/baseflow, groundwater/Darcy, sediment, drought lag, reservoir trade-off, water security. |
| Oceans / coasts | **Deep** | Stratification, gyres/Ekman/upwelling, circulation, tides/waves, sediment cells, delta/estuary, ports/cables. |
| Soils / biomes / ecosystems | **Deep** | CLORPT, CEC/pH, nutrient cycling, disturbance, succession, fragmentation, biome dynamics, degradation. |
| Natural hazards / risk | **Depth pass** | Mới thêm expected loss, loss exceedance, dynamic vulnerability, infrastructure dependency graph, adaptation choices, resilience dimensions và Korea–Vietnam cases. |

## Human Geography

| Nhóm | Trạng thái | Ghi chú |
|---|---|---|
| Population | **Deep** | Stock–flow, fertility/mortality, cohort/period, momentum, density, census/registry, projections. |
| Migration | **Deep** | Aspiration–capability–pathway, selectivity, gravity, intervening opportunities, network, displacement, data limits. |
| Urbanization | **Deep** | Agglomeration, site/situation, bid-rent, transport–land-use feedback, polycentric regions, housing/informal settlement, infrastructure risk. |
| Culture / language / religion | **Depth pass** | Mới nối physical setting, settlement, language network, migration/diaspora, urbanization, cultural economy và place identity. |
| Political geography / borders | **Depth pass** | Mới nối terrain/resources, borderland, state morphology, infrastructure integration, chokepoints, multi-level governance và map provenance. |
| Economic geography | **Depth pass** | Mới nối physical cost surface, resource/value capture, forward/backward linkages, labor/urban systems, GVC, corridors và Korea–Vietnam. |
| Agriculture / food systems | **Deep** | Agroecosystem, land tenure, irrigation, Von Thünen, food security, virtual water, fishery/livestock, climate risk. |
| Industry / resources / energy | **Deep** | Resource vs reserve, supplier tiers, industrial clusters, energy networks, renewables, critical minerals, corridors, just transition. |
| Transport / trade / globalization | **Depth pass** | Mới thêm terrain reliability, corridor development, transport–land-use feedback, multi-tier dependency, sea-port-inland chain và Korea–Vietnam network. |
| Development / inequality | **Deep** | Human development, PPP, spatial inequality, accessibility, poverty trap, digital divide, gender/time geography, environmental constraints. |

## Regional Geography

| Region | Trạng thái | Ghi chú |
|---|---|---|
| East Asia | **Deep** | High interior–monsoon rivers–dense eastern lowlands–industrial maritime networks; Korea route mạnh. |
| Southeast Asia | **Deep** | Mainland/archipelago contrast, monsoon/Mekong, straits, production networks, Vietnam link. |
| South Asia | **Deep** | Himalaya–plain–monsoon–groundwater–megacities–Indian Ocean. |
| Central Asia | **Deep** | Continentality–mountain water–endorheic basin–resources–transit corridors. |
| West Asia | **Deep** | Aridity–water–energy–ports/pipelines–chokepoints–urban systems. |
| Europe | **Depth pass** | Mới mở rộng river/port corridors, polycentric cities, energy mismatch, industry, aging, tourism và global connectivity. |
| Africa | **Depth pass** | Mới chuẩn hóa plateau/basin, rainfall/water, corridors, urbanization, agriculture/resources, value capture và market access. |
| North America | **Depth pass** | Mới mở rộng continental freight, Gulf/Pacific gateways, tech clusters, water/energy, cross-border production. |
| Latin America & Caribbean | **Depth pass** | Mới mở rộng Andes/basins, frontier, resource/value chain, primate cities, migration/tourism, trade gateways. |
| Oceania / Pacific | **Solid** | Cơ chế island/archipelago đã tốt; tiếp theo cần thêm production/trade/urban connection để ngang nhóm trên. |
| Polar regions | **Solid** | Physical/polar systems mạnh; còn có thể nối sâu hơn research/logistics/resources/global circulation. |

## Global Systems

| System | Trạng thái | Ghi chú |
|---|---|---|
| Climate change | **Deep** | Forcing–feedback–ocean inertia–carbon stock/flow–extremes–attribution–adaptation. |
| Water–Food–Energy Nexus | **Deep** | Multi-objective trade-offs, groundwater, desalination, virtual water, urban nexus, resilience. |
| Resources / chokepoints | **Deep** | Dependency graph, substitution, full value chain, route redundancy. |
| Global cities | **Deep** | Network centrality, command functions, megaregions, infrastructure/housing dependencies. |
| Sustainability | **Deep** | Stock–flow, system boundary, externalities, LCA, circularity limits, rebound, resilience/governance. |
| Global trade networks | **New deep chapter** | Production tiers, ports/hinterlands, inventory, finance, resource conversion, city networks, systemic risk và Korea–Vietnam application. |

## Earth / Global Geography

Geodesy, rotation/orbit/seasons, continental–ocean structure, global relief, planetary circulation, gravity/geoid/magnetic field, reference systems và human footprint hiện đều có canonical chapters. Recent depth pass đã nâng `continents/ocean basins`, `global relief` và `global circulation` lên mức cân bằng hơn với core.

## World Atlas

Atlas **không phải core coverage metric**. Inventory có thể đầy đủ, nhưng learning profile chỉ tính khi đủ causal chain.

High-value learning profiles hiện ưu tiên/đã nâng: Korea, Vietnam, China, Japan, United States, Singapore, Indonesia, India và major European economies; một số Africa depth profiles tiếp tục cần QA theo cùng Definition of Done.

## Khoảng trống tiếp theo

1. Oceania/Pacific và Polar regional chapters cần integration pass để ngang độ sâu các regions vừa nâng.
2. Agriculture–Energy–Development cross-link cần QA để giảm lặp và tăng prerequisite/application links.
3. Brazil, Australia, Malaysia, Thailand, Philippines là candidates Atlas có giá trị cao, nhưng chỉ promote khi viết được full learning profile.
4. Legacy short Atlas files cần classify `planned/reference/merge/remove`, không nâng hàng loạt.
5. Internal-link validation và duplicate concept audit nên chạy sau các depth pass lớn.