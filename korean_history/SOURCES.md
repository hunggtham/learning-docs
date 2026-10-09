# Korean History — source ledger và currentness boundary

> **Owner:** `korean_history/` (canonical history content). Nguồn tiếng Hàn là authority ưu tiên cho tên, niên đại, văn bản và di tích; bản dịch chỉ là lớp hỗ trợ người học.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| KH-NIKH-01 | National Institute of Korean History (국사편찬위원회) | chronology, primary records, historiography và database lịch sử Hàn Quốc | https://db.history.go.kr/ | database portal; kiểm tra 2026-10-09 | Phải ghi database/collection/item và bản tiếng Hàn; không dùng snippet tìm kiếm thay item | chapters 01–29, source map |
| KH-HISTORY-01 | Korean History Integrated System (한국사데이터베이스/한국사) | metadata và route tới corpus lịch sử chính thức | https://www.history.go.kr/ | portal; kiểm tra 2026-10-09 | Portal không đủ cho claim; lưu item/record cụ thể và ngày truy cập | chronology/reference |
| KH-ARCHIVES-01 | National Archives of Korea | hồ sơ hành chính, ảnh, tài liệu hiện đại và archival provenance | https://www.archives.go.kr/eng/ | portal; kiểm tra 2026-10-09 | Ghi collection/item, access condition và provenance; không bỏ qua context của hồ sơ nhà nước | modern/contemporary history |
| KH-KOSIS-01 | Statistics Korea — KOSIS | dân số, kinh tế, xã hội và historical statistics | https://kosis.kr/eng/ | portal; bảng có kỳ/metadata riêng | Ghi table ID, period, definition và revision; không dùng số liệu hiện tại cho giai đoạn lịch sử mà không nêu series | social/economic history |
| KH-UNESCO-01 | UNESCO Memory of the World / World Heritage | status và mô tả registry di sản/tư liệu | https://www.unesco.org/en/memory-world | portal; kiểm tra 2026-10-09 | Registry không thay thế history of production, use hoặc contested interpretation | heritage/place field guide |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| KH-PRIMARY-01 | `NEEDS_SOURCE` | Claim về chiếu chỉ, biên niên, census, chiến tranh hoặc nhân vật phải trỏ tới item/edition cụ thể; chưa có item thì chỉ ghi diễn giải thận trọng. | Owner chapter + `31_glossary_and_reference_map.md` |
| KH-TRANSLATION-01 | `REVIEW_REQUIRED` | Tên riêng, niên hiệu, địa danh và thuật ngữ phải đối chiếu tiếng Hàn, Hán tự/romanization khi cần; bản dịch tiếng Việt không phải authority duy nhất. | Owner `32_naming_translation_conventions.md` + Korean reviewer |
| KH-CONTEMPORARY-01 | `NEEDS_SOURCE` | Claim về xã hội, kinh tế, ký ức công chúng hoặc liên Triều sau 2020 cần nguồn hiện hành và ngày kiểm tra. | Owner chapters 23–29 |
| KH-ARCHAEOLOGY-01 | `REVIEW_REQUIRED` | Di tích/địa điểm cần tách khảo cổ evidence, reconstruction và diễn giải du lịch; không biến plaque/website giới thiệu thành toàn bộ lịch sử. | Owner chapters 34–37 |

## Quy trình refresh

1. Ưu tiên database/corpus tiếng Hàn và lưu item ID, collection, edition hoặc table ID; thêm bản dịch để hỗ trợ đọc.
2. Với số liệu/hiện trạng, ghi kỳ dữ liệu, revision và ngày kiểm tra; với lịch sử xa, ghi niên đại và provenance thay vì gắn nhãn “current”.
3. Khi database/translation hoặc naming convention đổi, cập nhật glossary và các chapter liên quan; đánh dấu `REVIEW_REQUIRED` nếu chưa đọc lại prose.
4. Strict-link audit không thay thế kiểm tra accuracy, translation và tranh luận sử học.
