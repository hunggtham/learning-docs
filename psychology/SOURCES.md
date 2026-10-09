# Psychology — source ledger và evidence/currentness boundary

> **Owner:** `psychology/` canonical content. Ledger này định tuyến nguồn và giới hạn suy luận; mỗi claim evidence quan trọng vẫn cần citation cụ thể tại chapter.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| PSY-NIMH-01 | National Institute of Mental Health (NIMH) | khung thông tin sức khỏe tâm thần, topic pages và research context của cơ quan liên bang Mỹ | https://www.nimh.nih.gov/health/topics | cổng truy cập 2026-10-09 | Không biến topic page thành chẩn đoán hoặc khuyến cáo cá nhân; jurisdiction/chapter scope phải rõ | mental health/psychopathology |
| PSY-PUBMED-01 | NLM — PubMed | bài nghiên cứu, systematic review, meta-analysis và metadata | https://pubmed.ncbi.nlm.nih.gov/ | cổng truy cập 2026-10-09 | Phải lưu PMID/DOI, năm, thiết kế, mẫu và outcome; abstract/search result không đủ cho claim mạnh | evidence synthesis toàn thư viện |
| PSY-NCBI-01 | NLM — NCBI Bookshelf | textbook/chuyên khảo nền tảng được lập chỉ mục | https://www.ncbi.nlm.nih.gov/books/ | cổng truy cập 2026-10-09; edition tùy tựa | Ghi edition/chapter; không dùng một textbook để kết luận về hiệu quả can thiệp hiện tại | foundations và history |
| PSY-WHO-01 | World Health Organization | định nghĩa/khung sức khỏe tâm thần và public-health context | https://www.who.int/health-topics/mental-health | cần kiểm tra claim-specific trước khi dùng | WHO pages không thay guideline quốc gia hay tư vấn lâm sàng; ghi jurisdiction và ngày truy cập | health/public-health boundary |

## Evidence và claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| PSY-INTERVENTION-01 | `NEEDS_SOURCE` | Claim “phương pháp X hiệu quả” cần review/meta-analysis hoặc guideline và chỉ rõ population/outcome; nếu thiếu chỉ mô tả cơ chế/giả thuyết. | Owner intervention chapters |
| PSY-CAUSAL-01 | `REVIEW_REQUIRED` | Tương quan, self-report hoặc nghiên cứu cắt ngang không đủ để viết quan hệ nhân quả. | Owner chapter + evidence reviewer |
| PSY-HEALTH-01 | `NEEDS_SOURCE` | Không chẩn đoán, dự báo nguy cơ cá nhân hoặc khuyên điều trị từ nội dung giáo dục; chuyển sang professional care khi phù hợp. | Owner mental-health/health chapters |

## Quy trình refresh

1. Gắn citation cụ thể tại đoạn claim, không chỉ link tới trang chủ.
2. Ghi loại bằng chứng, ngày xuất bản, mẫu và giới hạn suy rộng.
3. Khi guideline hoặc phân loại thay đổi, cập nhật claim map/correction note và rà lại các chapter downstream; audit link không chứng minh evidence còn phù hợp.
