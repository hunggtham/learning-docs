# Biology — source ledger và currentness boundary

> **Owner:** `biology/` (canonical biology content). Ledger này ghi nơi kiểm tra bằng chứng; nó không thay thế citation ở chapter có claim chuyên biệt.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| BIO-NIH-01 | National Institutes of Health (NIH) | phạm vi/ngữ cảnh nghiên cứu y-sinh của NIH; định vị nguồn chính thức | https://www.nih.gov/about-nih/nih-almanac/about-nih | trang truy cập kiểm tra 2026-10-09 | Không dùng trang giới thiệu NIH làm bằng chứng cho một claim sinh học cụ thể; claim phải trỏ bài/review/dataset cụ thể | `biology/` và các chapter có health boundary |
| BIO-NCBI-01 | National Library of Medicine — NCBI Bookshelf | sách/chuyên khảo sinh học-y sinh được lập chỉ mục | https://www.ncbi.nlm.nih.gov/books/ | cổng truy cập kiểm tra 2026-10-09; edition tùy tựa sách | Phải ghi tựa, edition/chapter và ngày truy cập; edition mới có thể thay đổi cách trình bày/khuyến cáo | chapter nền tảng và health overview |
| BIO-PUBMED-01 | NLM — PubMed | bài nghiên cứu/review và metadata | https://pubmed.ncbi.nlm.nih.gov/ | cổng truy cập kiểm tra 2026-10-09 | Từ khóa tìm kiếm không phải bằng chứng; phải lưu PMID/DOI, loại nghiên cứu và năm xuất bản cho claim quan trọng | chapter cần evidence synthesis |
| BIO-NIH-02 | NIH/NLM — MedlinePlus | giải thích sức khỏe phổ thông và giới hạn chuyển từ biology sang health | https://medlineplus.gov/ | cổng truy cập kiểm tra 2026-10-09 | Không dùng làm chẩn đoán/điều trị; claim lâm sàng cần guideline/cơ quan chuyên môn cụ thể | Human Health chapters |

## Quy tắc claim và freshness

- Claim về cơ chế cơ bản có thể ổn định nhưng vẫn phải chỉ rõ textbook/review nếu là điểm trọng tâm của chapter.
- Claim về người, bệnh, nguy cơ, can thiệp, biomarker, thuốc hoặc hướng dẫn sức khỏe là **high-stakes**: cần nguồn lâm sàng hiện hành, ngày kiểm tra và boundary; nếu thiếu dùng `NEEDS_SOURCE`.
- Không biến một nghiên cứu đơn lẻ thành quy luật phổ quát. Ghi thiết kế nghiên cứu, quần thể, outcome và giới hạn suy rộng khi claim dựa trên evidence mới.

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| BIO-HEALTH-01 | `NEEDS_SOURCE` | Các con số nguy cơ, screening, dinh dưỡng, exercise hoặc self-monitoring chưa có guideline/nguồn y tế hiện hành riêng thì chỉ viết ở mức khái niệm, không đưa ngưỡng hành động. | Owner Human Health chapter; bổ sung nguồn cơ quan y tế phù hợp |
| BIO-RESEARCH-01 | `REVIEW_REQUIRED` | Chapter tổng hợp phải kiểm tra xem bằng chứng có phải review/meta-analysis hay chỉ một nghiên cứu; không dùng heading/keyword audit thay cho đọc bài. | Owner chapter và reviewer domain |
| BIO-TAXONOMY-01 | `NEEDS_SOURCE` | Tên loài, phân loại, tình trạng bảo tồn và dữ liệu sinh thái phải có database/registry cụ thể cùng ngày truy cập. | Owner chapter tương ứng; xác minh trước publication |

## Quy trình refresh

1. Gắn source ID và citation cụ thể tại chapter khi claim vượt quá kiến thức nền.
2. Với health/evidence claim, ghi ngày kiểm tra và tái kiểm tra khi guideline, phân loại hoặc dữ liệu mới thay đổi.
3. Giữ boundary rõ giữa biology education, public-health information và clinical advice; nếu không đủ nguồn thì giữ `NEEDS_SOURCE`.
