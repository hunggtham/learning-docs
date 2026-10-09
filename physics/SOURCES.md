# Physics — source ledger và measurement boundary

> **Owner:** `physics/`. Ledger này định tuyến nguồn cho constants, units và measurement; các claim vật lý/chapter-specific vẫn cần citation phù hợp.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| PHY-NIST-CODATA-01 | NIST Fundamental Physical Constants / CODATA | giá trị hằng số cơ bản và uncertainty | https://physics.nist.gov/cuu/Constants/index.html | CODATA 2022; data content last update May 2024, kiểm tra 2026-10-09 | Phải ghi adjustment/version; không dùng bảng cũ như giá trị hiện hành nếu precision quan trọng | foundations, constants, quantitative examples |
| PHY-NIST-SI-01 | NIST | SI units, conversion và uncertainty expression | https://physics.nist.gov/cuu/Reference/contents.html | cổng kiểm tra 2026-10-09 | Đổi đơn vị không đủ để chứng minh model/measurement; ghi convention và uncertainty | measurement/experiment |
| PHY-NIST-DATA-01 | NIST Physical Reference Data | reference data vật lý/hoá lý | https://www.nist.gov/pml/productsservices/physical-reference-data | cổng kiểm tra 2026-10-09 | Dataset phải ghi species/material, điều kiện, version và ngày truy cập | matter/material chapters |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| PHY-NUMERIC-01 | `NEEDS_SOURCE` | Con số thực nghiệm, constant hoặc uncertainty phải ghi nguồn/version; không lấy số từ memory hoặc snippet. | Owner chapter có số liệu |
| PHY-EXPERIMENT-01 | `REVIEW_REQUIRED` | Claim thực nghiệm cần measurement model, error/uncertainty và miền áp dụng; công thức đẹp không thay thế bằng chứng. | Owner experiment chapters |
| PHY-ASTRO-01 | `NEEDS_SOURCE` | Dữ liệu thiên văn/khí hậu/vũ trụ học cần survey/catalog cụ thể và epoch; không viết snapshot như định luật. | Owner astrophysics chapters |

## Quy trình refresh

1. Ghi source ID, edition/adjustment, đơn vị và uncertainty cạnh bảng/số liệu.
2. Tách định luật/model ổn định khỏi parameter/data time-sensitive.
3. Khi NIST/CODATA có adjustment mới, rà lại toàn bộ examples dùng constants.
