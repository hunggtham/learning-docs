# Sociology — source ledger và currentness boundary

> **Owner:** `sociology/` (canonical sociology content). Ledger này định tuyến theory, survey/microdata và population evidence; nó không biến correlation thành causal proof.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| SOC-OECD-01 | OECD Data | chỉ báo xã hội, labor, education, inequality và household theo định nghĩa OECD | https://data.oecd.org/ | portal; series có kỳ/metadata riêng | Ghi indicator, definition, population, country coverage và vintage; không dùng headline như causal evidence | stratification/institutions |
| SOC-WB-01 | World Bank Open Data | population, poverty, education, labor và development indicators | https://data.worldbank.org/ | portal; indicator/revision riêng | Không đồng nhất “country indicator” với social mechanism; ghi methodology và period | population/development |
| SOC-UN-01 | United Nations Data / UN DESA | population, migration, urbanization, gender và social statistics | https://data.un.org/ | portal; series/vintage riêng | Ghi agency, series, projection/estimate và kỳ; không trộn estimate với observed data | demography/urbanization |
| SOC-IPUMS-01 | IPUMS | harmonized census/survey microdata và metadata | https://www.ipums.org/ | collection/release riêng; kiểm tra 2026-10-09 | Phải ghi sample, variable, harmonization và access condition; không coi sample convenience là population truth | methods/microdata |
| SOC-ASA-01 | American Sociological Association | terminology, ethics và discipline-level professional guidance | https://www.asanet.org/ | professional portal; kiểm tra 2026-10-09 | Không dùng association guidance làm evidence cho claim empirical cụ thể | theory/methods boundary |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| SOC-CAUSAL-01 | `REVIEW_REQUIRED` | Claim causal phải nêu design, confounding, unit, time order và alternative explanation; tương quan population-level không đủ. | Owner chapter + research-methods reviewer |
| SOC-GENERALIZE-01 | `NEEDS_SOURCE` | Không viết “xã hội hiện đại/người trẻ/người Hàn” như population đồng nhất nếu chưa có sample, survey year và context. | Owner chapter tương ứng |
| SOC-CURRENT-01 | `NEEDS_SOURCE` | Claim về inequality, migration, platform work, family, politics hoặc public opinion phải có dataset/survey hiện hành và as-of. | Owner chapters 03–05 |
| SOC-CONCEPT-01 | `REVIEW_REQUIRED` | Thuật ngữ theory cần ghi tradition/author và distinction; không dùng một định nghĩa giáo khoa làm consensus toàn ngành. | Owner chapter 00–02 |

## Quy trình refresh

1. Tách theory/khái niệm, operationalization, dữ liệu quan sát và diễn giải trong từng chapter.
2. Mỗi bảng/claim định lượng ghi sample/population, field year, variable definition, uncertainty và source ID.
3. Khi dataset revision hoặc social condition đổi, cập nhật `as-of` và mở review prose; structural audit không đủ.
4. Nếu chưa có evidence đại diện hoặc claim vượt dữ liệu, giữ `NEEDS_SOURCE` và thu hẹp câu chữ.
