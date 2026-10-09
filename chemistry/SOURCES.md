# Chemistry — source ledger và nomenclature/data boundary

> **Owner:** `chemistry/`. Ledger này giữ nguồn định nghĩa thuật ngữ và reference data; không biến source portal thành citation chung cho mọi phản ứng.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| CHEM-IUPAC-01 | International Union of Pure and Applied Chemistry | định nghĩa thuật ngữ hóa học và nomenclature | https://goldbook.iupac.org/ | Compendium of Chemical Terminology, 5th ed. entry pages; kiểm tra 2026-10-09 | Ghi term/edition/entry; định nghĩa không tự chứng minh cơ chế hay tính chất của mẫu cụ thể | glossary/foundations |
| CHEM-NIST-WEBBOOK-01 | NIST Chemistry WebBook, SRD 69 | physical/chemical property data của species/reactions | https://webbook.nist.gov/chemistry/ | SRD 69; cổng kiểm tra 2026-10-09 | Ghi species, phase, temperature/conditions và source record; không suy ra mọi mixture/material | thermochemistry/spectroscopy |
| CHEM-NIST-CONST-01 | NIST/CODATA | constants và conversion liên quan chemistry | https://physics.nist.gov/cuu/Constants/index.html | CODATA 2022; kiểm tra 2026-10-09 | Ghi adjustment/version và uncertainty | quantitative chemistry |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| CHEM-PROPERTY-01 | `NEEDS_SOURCE` | Số liệu nhiệt động, phổ, tốc độ hoặc equilibrium phải có compound/condition/source record; không dùng số bảng như universal constant. | Owner chapter data |
| CHEM-REACTION-01 | `REVIEW_REQUIRED` | Cơ chế phản ứng cần điều kiện, substrate và evidence; phương trình cân bằng không đủ chứng minh pathway. | Owner organic/inorganic chapters |
| CHEM-SAFETY-01 | `NEEDS_SOURCE` | Claim về độc tính, exposure, PPE hoặc xử lý hóa chất phải dùng SDS/authority cụ thể; không đưa hướng dẫn thao tác từ textbook chung. | Owner lab/safety content |

## Quy trình refresh

1. Phân biệt thuật ngữ IUPAC, reference data NIST và diễn giải cơ chế của tác giả.
2. Ghi điều kiện đo và uncertainty cạnh mọi số liệu.
3. Khi edition/record đổi, rà lại examples và safety boundary trước publication.
