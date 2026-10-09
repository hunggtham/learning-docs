# PMP — source ledger và exam/version boundary

> **Owner:** `pmp/` canonical learning chapters. `pmp/raw/` và `pmp/workflow-output/` là provenance/reference layer; không xem chúng là chuẩn gốc thay cho PMI publication.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| PMP-PMI-PMBOK-01 | Project Management Institute | PMBOK principles/performance domains/standard terminology | https://www.pmi.org/standards/pmbok | PMBOK Guide — Eighth Edition; kiểm tra 2026-10-09 | Exam content, terminology và references phải gắn edition; không trộn Seventh/Eighth mà không ghi boundary | canonical PMP chapters |
| PMP-PMI-STANDARDS-01 | PMI Standards & Publications | PMI standards/guides và publication status | https://www.pmi.org/standards/ | cổng kiểm tra 2026-10-09 | “Current” của PMI page không tự chứng minh exam blueprint; kiểm tra exam-specific notice riêng | references/update workflow |
| PMP-PMI-TOC-01 | PMI | table of contents và publication metadata của PMBOK 8 | https://www.pmi.org/-/media/pmi/documents/public/pdf/publications/pmbok-guide-eighth-edition_table-of-contents.pdf | ANSI/PMI 99-001-2025; kiểm tra 2026-10-09 | TOC không thay nội dung đầy đủ và không phải exam question bank | chapter map |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| PMP-EXAM-01 | `NEEDS_SOURCE` | Claim về exam domain, eligibility, application, fee, policy hoặc pass rule phải có PMI exam page/notice đúng thời điểm; PMBOK không đủ. | Owner exam-prep layer |
| PMP-AGILE-01 | `REVIEW_REQUIRED` | Agile/hybrid practice cần source/edition cụ thể; không gán mọi technique cho PMBOK nếu chưa có mapping. | Owner agile chapters |
| PMP-CASE-01 | `NEEDS_SOURCE` | Case/project examples là synthetic unless marked; không trình bày như PMI official scenario hay exam question. | Owner labs/case studies |

## Quy trình refresh

1. Ghi edition/standard và source ID ở mỗi claim chuẩn PMP.
2. Tách PMI standard, exam policy, practice guidance và nội dung tự biên soạn.
3. Khi PMI phát hành edition/blueprint mới, tạo correction note và rà lại toàn bộ exam-facing material.
