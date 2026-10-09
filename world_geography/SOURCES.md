# World Geography — source ledger và currentness boundary

> **Owner:** `world_geography/` (canonical geography content). Ledger này phân biệt dữ liệu không gian, Earth-system evidence và diễn giải địa lý.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| WG-USGS-01 | U.S. Geological Survey | địa hình, địa chất, tài nguyên nước và hazard theo dataset/sản phẩm USGS | https://www.usgs.gov/products/data | data portal; kiểm tra 2026-10-09 | Phải ghi dataset, resolution, geography, release/date; không dùng bản đồ tổng quát để chứng minh số liệu hiện tại | physical geography/atlas |
| WG-NASA-01 | NASA Earthdata | quan sát vệ tinh, khí hậu, bề mặt và Earth-system time series | https://earthdata.nasa.gov/ | portal; dataset có version/date riêng | Ghi product, processing level, spatial/temporal coverage; không diễn giải ảnh vệ tinh như causal evidence nếu thiếu validation | Earth/global systems |
| WG-IPCC-01 | Intergovernmental Panel on Climate Change | tổng hợp evidence về climate change, impacts và adaptation | https://www.ipcc.ch/reports/ | AR6 reports, 2021–2023; kiểm tra 2026-10-09 | Dùng report/chapter/box cụ thể và nêu confidence/scenario; không dùng để thay thế dự báo địa phương hiện hành | climate/global systems |
| WG-UN-01 | United Nations Data / UN agencies | dân số, urbanization, migration, land-use và chỉ báo toàn cầu | https://data.un.org/ | portal; series/vintage phải ghi riêng | Định nghĩa, boundary và revisions khác nhau theo agency; ghi series và kỳ dữ liệu | human geography/regions |
| WG-WB-01 | World Bank Open Data | development, poverty, infrastructure và trade indicators | https://data.worldbank.org/ | portal; indicator có kỳ và revision riêng | Không coi indicator là bản đồ nhân quả; ghi methodology, country coverage và as-of | economic/development geography |
| WG-NATURAL-EARTH-01 | Natural Earth | base map/vector data cho atlas và bản đồ minh họa | https://www.naturalearthdata.com/ | public dataset; ghi release/scale | Không dùng geometry/base map để chứng minh sovereignty, population hoặc current boundary; boundary nhạy cảm cần owner chính thức | `06_world_atlas/` |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| WG-MAP-01 | `REVIEW_REQUIRED` | Bản đồ phải ghi projection, scale, date, source và disputed-boundary treatment; không coi một base map là authority pháp lý. | Owner atlas chapter |
| WG-CLIMATE-01 | `NEEDS_SOURCE` | Nhiệt độ, mực nước biển, hazard, drought và climate trend cần dataset/time window cụ thể; không dùng số liệu không có baseline. | Owner physical/global systems |
| WG-REGION-01 | `REVIEW_REQUIRED` | Claim về “đặc trưng của một khu vực” phải tách physical constraint khỏi institution, history và sampling; tránh geographical determinism. | Owner regional chapter + reviewer |
| WG-CURRENT-01 | `NEEDS_SOURCE` | Population, urban ranking, trade corridor, conflict, border và infrastructure status cần ngày hiệu lực/as-of. | Owner affected chapter |

## Quy trình refresh

1. Mỗi map/table ghi dataset owner, version/release, resolution/definition, geography và ngày tải.
2. Khi source revision, boundary hoặc method đổi, cập nhật claim map và đánh dấu chapter liên quan để review.
3. Tách observation khỏi interpretation; ghi uncertainty, scale và limitation trước khi kết luận.
4. `CORE_COVERAGE_AUDIT.md` chỉ chứng minh coverage; không chứng minh dữ liệu địa lý còn current.
