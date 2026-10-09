# Backend — source ledger và version boundary

> **Owner:** `10_backend/`. Backend concepts là canonical; framework/vendor docs chỉ là implementation evidence và không thay thế cơ chế trong chapter.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| BE-IETF-HTTP-01 | IETF / RFC Editor | HTTP semantics, methods, status, caching/representation boundary | https://www.rfc-editor.org/rfc/rfc9110.html | RFC 9110, June 2022; kiểm tra 2026-10-09 | RFC status và extension có thể đổi; không suy ra framework behavior ngoài semantics RFC | `10_backend/backend_core/`, HTTP/API |
| BE-OWASP-ASVS-01 | OWASP | application-security verification requirements | https://owasp.org/www-project-application-security-verification-standard/ | project page; version phải ghi theo ASVS release dùng | Requirement mapping phải ghi version; không nói “OWASP compliant” nếu chưa audit controls | security/testing chapters |
| BE-POSTGRES-01 | PostgreSQL Global Development Group | behavior của PostgreSQL engine/SQL khi lesson nêu implementation | https://www.postgresql.org/docs/current/ | current manual 18.x hiển thị 2026-10-09 | Ghi major version; syntax/behavior không tự áp dụng cho mọi database | persistence/transaction chapters |
| BE-OTEL-01 | OpenTelemetry | telemetry model/API/SDK semantics | https://opentelemetry.io/docs/ | docs live; version/package phải ghi riêng | Không coi telemetry signal là bằng chứng correctness; implementation có thể khác theo SDK/version | observability chapters |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| BE-FRAMEWORK-01 | `NEEDS_SOURCE` | Claim về Spring/FastAPI/Django/Node runtime phải có docs version cụ thể; không dùng RFC để chứng minh framework default. | Owner branch tương ứng |
| BE-BENCHMARK-01 | `NEEDS_SOURCE` | Benchmark latency/throughput/cost phải có workload, hardware, version, method và date; không copy số benchmark không provenance. | Owner case study |
| BE-SECURITY-01 | `REVIEW_REQUIRED` | Security guidance cần map threat, control và version; prose tổng quát không chứng minh an toàn production. | Owner security chapters |

## Quy trình refresh

1. Ghi version/runtime/database khi claim gắn implementation.
2. Tách chuẩn giao thức khỏi default của một vendor/framework.
3. Recheck docs khi major release, deprecation hoặc security advisory ảnh hưởng chapter; giữ snapshot cũ trong changelog/correction note.
