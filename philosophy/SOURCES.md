# Philosophy — source ledger và interpretation boundary

> **Owner:** `philosophy/` (canonical philosophy content). Ledger này định tuyến primary text, scholarly interpretation và evidence từ các domain liên quan; không trình bày một reading như consensus toàn ngành.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| PHIL-SEP-01 | Stanford Encyclopedia of Philosophy | scholarly overview, bibliography và tranh luận triết học theo entry/author | https://plato.stanford.edu/ | entry revision/date phải ghi; portal kiểm tra 2026-10-09 | Entry là secondary interpretation; không dùng một entry để tuyên bố consensus nếu tranh luận còn mở | theory/history tracks |
| PHIL-IEP-01 | Internet Encyclopedia of Philosophy | introductory scholarly overview and references | https://iep.utm.edu/ | entry/date phải ghi | Dùng để định hướng và so sánh; claim trọng tâm nên quay về primary text/scholarly source | beginner routes |
| PHIL-PHILPAPERS-01 | PhilPapers | bibliography/discovery of papers, books và positions | https://philpapers.org/ | database portal; record/version riêng | Search result không phải evidence; lưu publication/DOI/edition cụ thể | reading maps |
| PHIL-PRIMARY-01 | Authoritative primary-text edition/library archive | text, translation, historical context của tác phẩm cụ thể | https://archive.org/ | edition/scan/translation phải ghi | Internet Archive là host/discovery; provenance và edition của tác phẩm phải được kiểm tra riêng | primary text chapters |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| PHIL-INTERPRET-01 | `REVIEW_REQUIRED` | Tách text, historical context, scholarly interpretation và suy luận của người học; không gọi một interpretation là ý nghĩa duy nhất. | Owner chapter + reviewer |
| PHIL-TRANSLATION-01 | `NEEDS_SOURCE` | Thuật ngữ dịch phải ghi language/edition/translator khi sắc thái ảnh hưởng lập luận. | Owner glossary/primary text |
| PHIL-CONSENSUS-01 | `NEEDS_SOURCE` | Claim “triết học cho rằng…” cần tradition/school và source cụ thể; không dùng overview portal làm authority toàn ngành. | Owner theory chapter |

## Quy trình refresh

1. Ghi edition, translator, entry revision hoặc DOI cho claim trọng tâm.
2. Tách mô tả lập trường khỏi phê bình, historical context và inference.
3. Khi entry/text edition đổi, kiểm tra lại translation, terminology và cross-domain boundary.
4. Giữ `NEEDS_SOURCE` khi chưa có primary/scholarly source phù hợp.
