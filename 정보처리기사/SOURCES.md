# 정보처리기사 — source ledger và exam/version boundary

> **Owner:** `정보처리기사/` (canonical certification output). Ledger này giữ ranh giới giữa syllabus chính thức, standards/implementation references và tài liệu học được chuẩn hóa từ raw sources.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| IPE-QNET-01 | Q-Net / 한국산업인력공단 | exam qualification, schedule, application, result và official notices | https://www.q-net.or.kr/ | portal; từng exam cycle/notice phải ghi | Không coi portal landing page là syllabus; lưu notice/guide đúng mã kỳ và ngày hiệu lực | `output/`, exam planning |
| IPE-KCA-01 | 한국데이터산업진흥원 / DataQ | database/SQL-related certification terminology and notices khi claim thuộc SQLD boundary | https://www.dataq.or.kr/ | notice/cycle riêng; kiểm tra 2026-10-09 | Không dùng DataQ làm authority cho toàn bộ 정보처리기사 nếu notice không nói vậy | database cross-link |
| IPE-ISO-01 | ISO | standard terminology/quality/security/process concepts khi chapter nêu standard cụ thể | https://www.iso.org/standards.html | standard number/edition phải ghi | Catalogue không thay text/official interpretation; không gọi textbook summary là conformance | subjects 01–05 |
| IPE-NIST-01 | NIST Computer Security Resource Center | security terminology/frameworks khi claim trỏ tới NIST publication | https://csrc.nist.gov/publications | publication/revision phải ghi | NIST guidance không tự trở thành Korean exam scope hoặc legal obligation | security/system management |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| IPE-SYLLABUS-01 | `NEEDS_SOURCE` | Subject scope, weighting, question style, pass rule và terminology phải theo official exam guide/notice của đúng kỳ; raw PDF cũ chỉ là provenance, không phải current authority. | Owner `output/`; bổ sung Q-Net notice cụ thể |
| IPE-CURRENT-01 | `NEEDS_SOURCE` | Framework/API/tool/version claims (Java, DB, OS, security) cần version/date; không dùng exam text để khẳng định behavior hiện tại. | Owner subject lesson |
| IPE-STANDARD-01 | `REVIEW_REQUIRED` | ISO/NIST/IEEE concept phải ghi standard/publication number và boundary; không suy chứng nhận/conformance từ định nghĩa. | Owner relevant subject + reviewer |
| IPE-RAW-01 | `REVIEW_REQUIRED` | Raw/source-derived content phải tách khỏi Vietnamese explanation và kiểm tra translation/duplicate; generated output không thay thế source provenance. | Owner `raw/`, `raw_md/`, `output/` |

## Quy trình refresh

1. Trước mỗi kỳ học/thi, lấy official Q-Net notice/guide cụ thể, ghi exam cycle, ngày hiệu lực và mapping sang subject/lesson.
2. Tách “đúng theo đề cương kỳ thi” khỏi “đúng theo implementation hiện hành”; versioned tech claim cần source riêng.
3. Khi source raw được thay thế, giữ provenance, cập nhật output có scope rõ và chạy `scripts/audit_learning_output.py`.
4. Nếu chưa có official notice hoặc source-specific evidence, giữ `NEEDS_SOURCE`; không suy đoán từ heading/keyword audit.
