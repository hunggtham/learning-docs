# Mathematics — source ledger và definition/theorem boundary

> **Owner:** `mathematics/`. Ledger này ưu tiên nguồn tham chiếu công thức/hàm đặc biệt và quy ước; theorem/proof vẫn cần textbook hoặc citation cụ thể tại chapter.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| MATH-NIST-DLMF-01 | NIST Digital Library of Mathematical Functions | định nghĩa, notation, identities và reference values của special functions | https://dlmf.nist.gov/ | Version 1.2.8, release 2026-09-15; kiểm tra 2026-10-09 | Ghi section/version; không dùng một identity ngoài điều kiện hội tụ/miền xác định | analysis/special functions/numerics |
| MATH-NIST-DLMF-02 | NIST DLMF errata/software | errata và implementation notes liên quan DLMF | https://dlmf.nist.gov/errata/ | live page; kiểm tra 2026-10-09 | Code/numeric result cần precision, domain và library version riêng | computational chapters |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| MATH-THEOREM-01 | `REVIEW_REQUIRED` | Theorem phải có giả thiết và proof/reference; không rút điều kiện từ ví dụ số. | Owner chapter theorem |
| MATH-NUMERIC-01 | `NEEDS_SOURCE` | Approximation/error bound cần source, domain và precision; output phần mềm không tự là proof. | Owner numerical chapters |
| MATH-CONVENTION-01 | `NEEDS_SOURCE` | Notation và convention khác nhau giữa textbook; ghi rõ convention khi có nguy cơ mơ hồ. | Owner chapter |

## Quy trình refresh

1. Ghi theorem/identity section và điều kiện áp dụng, không chỉ link trang chủ.
2. Tách mathematical truth tương đối ổn định khỏi implementation/errata/version.
3. Rà lại numerical examples khi DLMF hoặc thư viện tính toán đổi version.
