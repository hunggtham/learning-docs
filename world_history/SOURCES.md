# World History — source ledger và currentness boundary

> **Owner:** `world_history/` (canonical history content). Ledger này định tuyến loại bằng chứng; nó không biến một cổng nguồn thành bằng chứng cho mọi claim.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| WH-LOC-01 | Library of Congress — Country Studies / Area Handbooks | bối cảnh quốc gia, thể chế và lịch sử hiện đại theo từng hồ sơ; dùng như điểm vào tư liệu thứ cấp | https://www.loc.gov/collections/country-studies/about-this-collection/ | collection portal; kiểm tra 2026-10-09 | Không dùng hồ sơ quốc gia thay cho chuyên khảo hoặc nguồn sơ cấp; phải ghi country/edition/chapter | regional chapters và comparative cases |
| WH-UNESCO-01 | UNESCO Digital Library | báo cáo, tư liệu di sản và lịch sử do UNESCO phát hành | https://unesdoc.unesco.org/ | portal; kiểm tra 2026-10-09 | Phải ghi mã tài liệu, năm và trang; không suy ra consensus lịch sử từ một báo cáo đơn lẻ | cultural/education/history evidence |
| WH-WB-01 | World Bank Open Data | chuỗi chỉ báo dân số, kinh tế và phát triển dùng để đặt lịch sử vào bối cảnh định lượng | https://data.worldbank.org/ | portal; series phải ghi kỳ dữ liệu và ngày tải | Chỉ là dữ liệu quan sát/ước tính theo định nghĩa của indicator; không tự chứng minh quan hệ nhân quả lịch sử | demographic/economic context |
| WH-UN-01 | United Nations — UN Data / DESA Population | dân số, di cư và chỉ báo quốc tế theo series chính thức | https://data.un.org/ | portal; kiểm tra 2026-10-09 | Ghi series, revision/vintage và kỳ; không trộn estimate mới với historical series cũ mà không chú thích | population/migration chapters |
| WH-PRIMARY-01 | National archive, museum hoặc corpus sử liệu của jurisdiction tương ứng | sự kiện, văn bản, nhân vật và testimony ở mức nguồn sơ cấp | https://www.archives.gov/ | portal minh họa của U.S. National Archives; kiểm tra 2026-10-09 | Phải trỏ tới item/collection cụ thể, provenance và bias; URL portal không đủ cho claim trọng tâm | primary-source workbench |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| WH-CAUSAL-01 | `REVIEW_REQUIRED` | Claim nhân quả phải tách chronology khỏi mechanism, scale, competing interpretation và counterfactual; không coi trật tự trước–sau là nguyên nhân. | Owner chapter + reviewer lịch sử |
| WH-QUANT-01 | `NEEDS_SOURCE` | Dân số, GDP, thương mại, chiến tranh và mortality cần series/bảng cụ thể, vintage và định nghĩa; không dùng con số nhớ từ textbook. | Owner chapter tương ứng |
| WH-PRIMARY-02 | `NEEDS_SOURCE` | Trích dẫn nguồn sơ cấp phải có item, bản dịch và bối cảnh; khi chưa có item cụ thể chỉ mô tả ở mức khái quát. | Owner `22_source_workbench.md` |
| WH-CONTEMPORARY-01 | `NEEDS_SOURCE` | Claim từ sau 1991 về biên giới, dân số, xung đột hoặc chính sách có thể thay đổi; phải có nguồn hiện hành và ngày kiểm tra. | Owner modern-world chapters |

## Quy trình refresh

1. Với mỗi claim trọng tâm, ghi source ID, item/chapter/table cụ thể, năm/edition và trang hoặc định danh dữ liệu.
2. Tách nguồn sơ cấp, diễn giải sử học, dataset và suy luận của tác giả; ghi bias/giới hạn của từng lớp.
3. Refresh các claim định lượng và đương đại khi source revision, boundary hoặc series definition đổi; nếu chưa kiểm tra lại, giữ `NEEDS_SOURCE`.
4. Chạy strict-link/diff audit sau khi sửa ledger; audit cấu trúc không thay thế review sử học thủ công.
