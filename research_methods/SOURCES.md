# Research methods — source ledger và evidence boundary

> **Owner:** `research_methods/`. Ledger này định tuyến reporting/review methodology; không biến checklist reporting thành bằng chứng cho conclusion của nghiên cứu.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| RM-COCHRANE-01 | Cochrane | phương pháp systematic review/intervention và cập nhật review | https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current | Handbook v6.5 (2024); kiểm tra 2026-10-09 | Chỉ áp dụng đúng loại review/phạm vi; ghi version và chapter | evidence synthesis |
| RM-EQUATOR-01 | EQUATOR Network | reporting guideline lookup theo study design/clinical area | https://www.equator-network.org/reporting-guidelines/ | database live; kiểm tra 2026-10-09 | Reporting guideline giúp minh bạch báo cáo, không chứng minh study quality hay causal validity | reporting chapters |
| RM-EQUATOR-02 | EQUATOR Network library | chọn guideline theo RCT, observational, systematic review, qualitative, diagnostic, case report | https://www.equator-network.org/library/ | database live; kiểm tra 2026-10-09 | Phải chọn guideline đúng design và version; không áp checklist sai thiết kế | study design chapters |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| RM-CAUSAL-01 | `NEEDS_SOURCE` | Causal claim cần design/assumptions/evidence riêng; CONSORT/STROBE/PRISMA không tự tạo causality. | Owner causal inference chapters |
| RM-REVIEW-01 | `REVIEW_REQUIRED` | Review phải ghi search date, inclusion, risk of bias, synthesis và certainty; checklist hoàn thành không đủ. | Owner review chapters |
| RM-ETHICS-01 | `NEEDS_SOURCE` | Claim về ethics/consent/privacy cần jurisdiction/institution policy cụ thể, không suy ra từ reporting guideline. | Owner applied research |

## Quy trình refresh

1. Ghi study design, guideline/version và ngày tìm kiếm.
2. Tách reporting quality, internal validity, external validity và certainty of evidence.
3. Khi handbook/guideline đổi, rà lại template và các chapter dùng checklist cũ.
