# Core Coverage Audit — World Geography Knowledge Library

## Mục đích

Audit này theo dõi **độ sâu của Knowledge Library cốt lõi**, không đếm số file. Một chủ đề chỉ được xem là vững khi người đọc có thể đi từ khái niệm → cơ chế → mô hình → ví dụ → giới hạn → liên kết mà không cần dựa vào country profile ngắn.

Trạng thái dùng trong audit:

- **Deep**: đủ làm chapter học chính, đã có causal reasoning, limitation và cross-link.
- **Solid**: nền tảng tốt nhưng còn nhánh có thể làm sâu.
- **Depth pass completed**: vừa được nâng đáng kể trong audit gần nhất.
- **Planned/reference**: tồn tại để định vị hoặc roadmap, không tính completed learning content.

## Foundations

| Chủ đề | File chính | Trạng thái | Audit |
|---|---|---|---|
| Geographic thinking, scale, location | [Geographical thinking](./00_foundations/00_geographical_thinking.md) | **Deep** | Pattern→process, relational location, scale–extent–resolution, accessibility, network/flow, autocorrelation, path dependence và uncertainty đã có. |
| Coordinates, time zones | [Coordinates & time](./00_foundations/02_coordinates_time_maps.md) | **Deep** | Latitude/longitude, geodesic, datum/CRS, UTC/time zone và date-line reasoning đã vững. |
| Maps, cartography, projections | [Cartography](./00_foundations/03_cartography_projections_scale.md) | **Deep** | Scale/generalization, projection trade-off, choropleth, classification, MAUP và web-map tile đã có. |
| GIS, geospatial data, remote sensing | [GIS & remote sensing](./00_foundations/04_geospatial_data_gis_remote_sensing.md) | **Deep** | Vector/raster, topology, spatial index/join, DEM, geocoding, uncertainty, remote-sensing measurement/validation đã đủ mạnh. |

## Physical Geography

| Chủ đề | File chính | Trạng thái | Audit |
|---|---|---|---|
| Earth systems | [Earth system](./00_foundations/01_earth_as_system.md) | **Deep** | Stock–flow, feedback, threshold, dynamic equilibrium và spatial heterogeneity. |
| Geological time, plate tectonics | [Plate tectonics](./01_physical_geography/00_plate_tectonics_geologic_time.md) | **Deep** | Driving forces, boundaries, earthquake/volcanism, magma generation và deep time. |
| Geomorphology | [Geomorphology](./01_physical_geography/01_landforms_geomorphology.md) | **Deep** | Weathering, erosion, mass movement, fluvial/coastal/glacial/karst/desert processes. |
| Atmosphere, weather, climate | [Weather & atmosphere](./01_physical_geography/02_atmosphere_weather_climate.md), [Climate system](./01_physical_geography/03_global_climate_system.md) | **Deep** | Energy, pressure, Coriolis, circulation, moisture, monsoon, forecasting, ENSO, paleoclimate. |
| Hydrology | [Hydrology](./01_physical_geography/04_hydrology_rivers_groundwater.md) | **Deep** | Basin balance, hydrograph, groundwater, Darcy, sediment, drought lag, reservoir trade-off, water security. |
| Oceans, coasts | [Oceans & coasts](./01_physical_geography/05_oceans_coasts.md) | **Deep** | Stratification, Ekman/upwelling, circulation, sediment cell, delta/estuary, compound flood, fisheries, ports/cables. |
| Soils, biomes, ecosystems | [Soils/biomes/ecosystems](./01_physical_geography/06_soils_biomes_ecosystems.md) | **Deep** | Soil formation/properties, nutrient cycling, disturbance, succession, fragmentation, degradation. |
| Natural hazards, risk | [Hazards & risk](./01_physical_geography/07_natural_hazards_risk.md) | **Deep** | Hazard–exposure–vulnerability, return period, compound/cascading risk và resilience. |

## Human Geography

| Chủ đề | File chính | Trạng thái | Audit |
|---|---|---|---|
| Population | [Population](./02_human_geography/00_population_demography.md) | **Deep** | Cohort/period, momentum, density, data quality và projection uncertainty. |
| Migration | [Migration](./02_human_geography/01_migration.md) | **Deep** | Aspiration–capability–pathway, selectivity, network, gravity, displacement, remittance và data. |
| Urbanization | [Urbanization](./02_human_geography/02_settlement_urbanization.md) | **Deep** | Agglomeration, bid-rent, transport–land use, polycentric region, housing, informal settlement, infrastructure risk. |
| Culture, language, religion | [Cultural geography](./02_human_geography/03_culture_language_religion.md) | **Deep** | Diffusion, language network, sacred space, cultural landscape, identity/hybridization và classification bias. |
| Political geography, borders | [Political geography](./02_human_geography/04_political_geography_borders.md) | **Deep** | State/nation/territory, border friction, maritime zone, governance scale, geopolitics-as-constraint. |
| Economic geography | [Economic geography](./02_human_geography/05_economic_geography.md) | **Deep** | Location, agglomeration, labor market, GVC, informal economy, finance, path dependence/resilience. |
| Agriculture, food systems | [Agriculture](./02_human_geography/06_agriculture_food_systems.md) | **Deep** | Agroecosystem, land tenure, irrigation, Von Thünen, cold chain, food security, virtual water, fisheries/livestock. |
| Industry, resources, energy | [Industry/Energy/Resources](./02_human_geography/07_industry_energy_resources.md) | **Deep** | Resource vs reserve, supplier tiers, energy conversion/grid, renewables, critical minerals, corridor, just transition. |
| Transport, trade, globalization | [Transport/Trade](./02_human_geography/08_transport_trade_globalization.md) | **Deep** | Generalized cost, mode, node/capacity, container/intermodal, port–hinterland, border friction, resilience, digital infrastructure. |
| Development, inequality | [Development](./02_human_geography/09_development_inequality.md) | **Deep** | Human development, PPP/cost, spatial inequality, accessibility, poverty trap, digital divide, gender/time geography. |

## Regional Geography

Khung [How to read regions](./03_regions/00_how_to_read_regions.md) là canonical methodology. Regional chapter không được đánh giá bằng số country được nhắc mà bằng khả năng nối causal chain.

| Vùng | Trạng thái | Ghi chú |
|---|---|---|
| East Asia | **Deep** | Reference standard cho Korea/China/Japan, monsoon, coastal industrial corridors, demographic polarization và maritime networks. |
| Southeast Asia | **Deep** | Reference standard cho Vietnam/ASEAN, archipelago–mainland contrast, monsoon/delta, manufacturing và chokepoints. |
| South Asia | **Depth pass completed** | Bổ sung Indus/GBM, groundwater nexus, relative sea level, urban/value-chain, air pollution, migration và Indian Ocean role. |
| Central Asia | **Depth pass completed** | Bổ sung endorheic basins, peak water, pastoral mobility, pipeline lock-in, rail friction và water–energy trade-off. |
| West Asia | **Depth pass completed** | Bổ sung basin-scale water, fossil aquifer, Gulf urban system, energy/value chain, chokepoint resilience và migration. |
| Europe | **Deep** | Physical–historical fragmentation, dense transport/urban networks, industrial/service core và integration logic đã đủ mạnh. |
| Africa | **Deep** | Sahara–Sahel–Congo–Rift–coastal systems, resource/corridor và demographic/urban transformation đã có chiều sâu. |
| North America | **Deep** | Continental scale, climate/relief, river/agriculture, urban belts, resource/transport networks. |
| Latin America & Caribbean | **Deep** | Andes–Amazon–plateau–coast, commodity geography, urbanization, inequality và hazard. |
| Oceania & Pacific | **Deep** | Australia–island systems, ocean distance, resource, climate and maritime connectivity. |
| Polar regions | **Deep** | Cryosphere, albedo, ocean/atmosphere coupling, accessibility và climate feedback. |

## Global Systems

Climate change, Water–Food–Energy nexus, resources/chokepoints, global cities/trade networks và sustainability đều ở trạng thái **Deep**. Điểm mạnh là system-of-systems reasoning: stock/flow, dependency graph, chokepoint, resilience, LCA và governance scale.

## Earth / Global Geography

| Chủ đề | Trạng thái | Audit |
|---|---|---|
| Geodesy, Earth shape/size | **Deep** | Ellipsoid, geoid, datum/frame/epoch, height systems, Earth orientation và measurement systems. |
| Rotation, orbit, seasons, time | **Deep** | Rotation/orbit geometry, seasons, solar time và planetary time relation. |
| Reference systems | **Deep** | Global coordinate/reference frames nối trực tiếp GIS và geodesy. |
| Continents, oceans, basin structure | **Depth pass completed** | Bổ sung crust vs continent, Wilson cycle, passive/active margin, shelf/slope/abyss, strait và bathymetric data provenance. |
| Global relief, hypsometry | **Depth pass completed** | Bổ sung hypsometric reasoning, isostasy, base level, relief energy, DEM/DSM uncertainty, infrastructure cost và settlement relation. |
| Planetary water–energy circulation | **Depth pass completed** | Bổ sung radiation budget, Hadley/eddy transport, gyre, Ekman/upwelling, overturning, residence time, teleconnection và observation systems. |
| Gravity, geoid, magnetic field | **Deep** | Trường trọng lực và từ trường đã được nối với reference system, navigation và Earth structure. |
| Human footprint | **Deep** | Planetary-scale land use, resource flows và anthropogenic footprint đã có. |

## World Atlas

Atlas **không được dùng để bù core**. Trạng thái hoàn chỉnh chỉ áp dụng cho learning profile đủ chiều sâu.

Priority đã có profile sâu hoặc đang được ưu tiên giữ sâu gồm Korea, Vietnam, China, Japan, United States và nhóm major European economies đã depth-pass. Các country file compact/legacy còn lại phải ở trạng thái **planned/reference** cho tới khi được promote, merge hoặc remove.

Xem [Atlas Coverage Status](./06_world_atlas/03_coverage_status.md).

## Kết luận audit

Core Geography hiện không còn lỗ hổng lớn kiểu “chưa có chapter”. Công việc tiếp theo nên tập trung vào:

**cross-link consistency → comparative regional synthesis → selective high-value Atlas depth → cleanup legacy stubs**.

Metric quan trọng là khả năng giải thích relationship và transfer mental model sang case mới, không phải số file.