# Computer Science — source ledger và specification/version boundary

> **Owner:** `computer_science/` (canonical CS content). Ledger này tách theory/invariant, standards, implementation documentation và benchmark evidence.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| CS-ACM-01 | ACM Digital Library | peer-reviewed CS papers, proceedings và surveys | https://dl.acm.org/ | publication/DOI/year phải ghi | Abstract/metadata không đủ cho claim; ghi design, dataset và limitations của paper | theory/empirical chapters |
| CS-IEEE-01 | IEEE Computer Society Digital Library | computing standards, papers và technical surveys | https://www.computer.org/csdl | publication/standard/version phải ghi | Không dùng society landing page làm evidence cho implementation claim | systems/software tracks |
| CS-RFC-01 | IETF / RFC Editor | internet protocol specifications and status | https://www.rfc-editor.org/ | RFC number/status/date phải ghi | RFC status (Proposed/Internet Standard/Obsolete) và implementation support phải tách | networks/distributed systems |
| CS-NIST-01 | NIST Computer Security Resource Center | security terminology, frameworks và publications | https://csrc.nist.gov/publications | publication/revision phải ghi | Guidance không tự là law/guarantee; claim cần scope và threat model | security/reliability |
| CS-ISO-01 | ISO/IEC standards catalogue | formal standards khi chapter ghi standard number/edition | https://www.iso.org/standards.html | standard number/edition phải ghi | Catalogue không thay normative text hoặc conformance evidence | software/process/data |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| CS-BENCHMARK-01 | `NEEDS_SOURCE` | Benchmark cần workload, input distribution, hardware, compiler/runtime, dataset, method và uncertainty; không dùng một con số generic. | Owner case study/performance |
| CS-IMPLEMENTATION-01 | `NEEDS_SOURCE` | Claim về API, default, complexity thực tế hoặc guarantee cần version/config/source code/test evidence; theory không đủ. | Owner chapter/tool |
| CS-STANDARD-01 | `REVIEW_REQUIRED` | Standard/spec phải ghi status, edition và conformance boundary; implementation có thể deviate hoặc chưa support. | Owner standards chapter |
| CS-CAUSAL-01 | `REVIEW_REQUIRED` | Performance/security/reliability case phải tách observation, hypothesis, intervention và causal evidence. | Owner lab/reviewer |

## Quy trình refresh

1. Gắn DOI/RFC/standard/version hoặc reproducible artifact cho claim trọng tâm.
2. Tách invariant lý thuyết khỏi implementation, version/config và measured result.
3. Khi RFC/standard/library/tool deprecate hoặc đổi default, mở review cho chapter phụ thuộc.
4. Không coi build/unit/keyword audit là evidence cho benchmark, security hay distributed guarantee.
