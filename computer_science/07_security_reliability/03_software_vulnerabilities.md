# Bộ nhớ (memory / 메모리), web và injection vulnerabilities

> **Mạch đọc:** Đặt **bộ nhớ (memory / 메모리), web và injection vulnerabilities** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **bộ nhớ (memory / 메모리) corruption** sang **Injection: khi dữ liệu (data / 데이터) bị hiểu thành mã (code / 코드)/command**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Software vulnerability (취약점 / lỗ hổng) xuất hiện khi attacker-controlled đầu vào (input / 입력)/trạng thái (state / 상태) vượt qua giả định (assumption / 가정) của program và đạt tác động (effect / 효과) không được phép. Học từng CVE không đủ; cần nhận ra recurring structures: bộ nhớ (memory / 메모리) ranh giới (boundary / 경계) violations, mã (code / 코드)/dữ liệu (data / 데이터) confusion, trust-boundary kiểm tra hợp lệ (validation / 검증) failures và authorization gaps.

## Bộ nhớ (memory / 메모리) corruption

Trong memory-unsafe languages, out-of-bounds ghi (write / 쓰기), use-after-free, double free và integer overflow có thể corrupt điều khiển (control / 제어)/dữ liệu (data / 데이터). ngăn xếp (stack / 스택) buffer overflow kinh điển có thể overwrite return siêu dữ liệu (metadata / 메타데이터); hiện đại (modern / 현대적) mitigations gồm ngăn xếp (stack / 스택) canaries, ASLR, NX/DEP, CFI, hardened allocators.

Mitigations tăng difficulty nhưng không thay fix gốc (root / 루트) bug. Memory-safe languages loại nhiều classes này by construction/checks, nhưng bản địa (native / 네이티브) libraries/unsafe blocks vẫn là ranh giới (boundary / 경계).

## Injection: khi dữ liệu (data / 데이터) bị hiểu thành mã (code / 코드)/command

SQL injection xảy ra khi attacker đầu vào (input / 입력) được concatenated vào truy vấn (query / 쿼리) cú pháp (syntax / 문법), làm dữ liệu trở thành SQL mã (code / 코드). Parameterized truy vấn (query / 쿼리) giữ truy vấn (query / 쿼리) cấu trúc (structure / 구조) và values separate.

```sql
-- nguy hiểm về pattern
"SELECT ... WHERE name = '" + input + "'"

-- đúng principle
SELECT ... WHERE name = ?
```

Same mẫu (pattern / 패턴) xuất hiện shell injection, LDAP injection, template injection: **mã (code / 코드) and dữ liệu (data / 데이터) channels bị trộn**.

Parameterization không giải động (dynamic / 동적) identifiers/thứ tự (order / 순서) clauses tự động; allowlist/structured APIs cần cho cú pháp (syntax / 문법) positions không parameterizable.

## XSS

Cross-Site Scripting cho attacker-controlled content execute trong trình duyệt (browser / 브라우저) origin ngữ cảnh (context / 맥락). Stored, reflected, DOM-based variants khác nguồn (source / 소스)/luồng (flow / 흐름) nhưng gốc (root / 루트) issue là untrusted dữ liệu (data / 데이터) vào executable HTML/JS ngữ cảnh (context / 맥락) without proper context-sensitive escaping/sanitization.

Đầu ra (output / 출력) encoding phải phù hợp HTML văn bản (text / 텍스트), attribute, JavaScript, URL contexts. CSP là defense-in-depth, không thay correct encoding.

## CSRF

Trình duyệt (browser / 브라우저) tự gửi cookies tới matching site; malicious page có thể trigger yêu cầu (request / 요청) nếu máy chủ (server / 서버) chỉ dựa cookie. SameSite, anti-CSRF đơn vị từ (token / 토큰), origin kiểm tra hợp lệ (validation / 검증) và requiring custom headers/API patterns là mitigations theo ngữ cảnh (context / 맥락).

CSRF khác XSS: XSS chạy mã (code / 코드) trong trusted origin; CSRF lợi dụng ambient authority từ trình duyệt (browser / 브라우저).

## SSRF

Server-Side yêu cầu (request / 요청) Forgery khiến máy chủ (server / 서버) yêu cầu (request / 요청) URL attacker-controlled, có thể reach nội bộ (internal / 내부) siêu dữ liệu (metadata / 메타데이터)/services không công khai (public / 공개). Mitigation cần allowlist destinations/protocols, mạng (network / 네트워크) egress controls, DNS/IP kiểm tra hợp lệ (validation / 검증) cẩn thận và siêu dữ liệu (metadata / 메타데이터) protections.

## Đường dẫn (path / 경로) traversal

Đầu vào (input / 입력) như `../../etc/passwd` có thể escape intended directory nếu đường dẫn (path / 경로) phép nối (join / 조인)/canonicalization sai. Safe thiết kế (design / 설계) use generated IDs/lưu trữ (storage / 저장소) APIs, normalize và enforce resolved đường dẫn (path / 경로) under allowed gốc (root / 루트). String prefix check naive có edge cases symbolic links/encoding/nền tảng (platform / 플랫폼).

## Deserialization

Unsafe deserialization of attacker dữ liệu (data / 데이터) can instantiate unexpected đối tượng (object / 객체) graphs or trigger gadget chains in ecosystems supporting polymorphic/đối tượng (object / 객체) deserialization. Prefer simple dữ liệu (data / 데이터) formats + tường minh (explicit / 명시적) schemas/types; never treat untrusted serialized đối tượng (object / 객체) stream as trustworthy mã (code / 코드) cấu trúc (structure / 구조).

## Race vulnerabilities

TOCTOU — thời gian (time / 시간) Of Check To thời gian (time / 시간) Of Use: check permission/đường dẫn (path / 경로)/trạng thái (state / 상태) rồi attacker changes before use. Atomic OS APIs, tệp (file / 파일) descriptors, transactions hoặc locks reduce gap. bảo mật (security / 보안) often requires same atomicity lập luận (reasoning / 추론) as tính đồng thời (concurrency / 동시성) tính đúng đắn (correctness / 정확성).

## Phụ thuộc (dependency / 의존성)/supply chuỗi (chain / 사슬)

Vulnerability can enter through phụ thuộc (dependency / 의존성), bản dựng (build / 빌드) script, gói (package / 패키지) registry compromise or CI secret leakage. Pin versions/check integrity, minimize dependencies, SBOM/scanning, protected CI credentials and reproducible bản dựng (build / 빌드) practices reduce rủi ro (risk / 위험).

## Đầu vào (input / 입력) kiểm tra hợp lệ (validation / 검증) không phải universal sanitizer

Validate ngữ nghĩa (semantic / 의미적) lĩnh vực (domain / 도메인) at ranh giới (boundary / 경계); encode when outputting into cú pháp (syntax / 문법) ngữ cảnh (context / 맥락); parameterize mã (code / 코드)/dữ liệu (data / 데이터); authorize every tài nguyên (resource / 자원) hành động (action / 동작). One “sanitize()” hàm (function / 함수) cannot safely cover SQL, HTML, shell, URL and JSON contexts.

## Mô hình tư duy (mental model / 사고 모델)

> Nhiều vulnerabilities là **ranh giới (boundary / 경계) confusion**: dữ liệu (data / 데이터) becomes mã (code / 코드), untrusted định danh (identity / 식별자) becomes authorized, đường dẫn (path / 경로) escapes không gian tên (namespace / 네임스페이스), bộ nhớ (memory / 메모리) ghi (write / 쓰기) escapes đối tượng (object / 객체). Hãy xác định parser/trình thông dịch (interpreter / 인터프리터) nào sẽ đọc đầu vào (input / 입력) tiếp theo và giữ dữ liệu (data / 데이터) ở đúng channel.

## Dùng chung (common / 공통) Misconceptions

**“ORM ngăn mọi SQL injection.”** Raw queries/động (dynamic / 동적) cú pháp (syntax / 문법) vẫn có thể inject; parameterization principle mới quan trọng.

**“Frontend kiểm tra hợp lệ (validation / 검증) đủ vì người dùng (user / 사용자) không nhập được giá trị xấu.”** Attacker gọi API trực tiếp; máy chủ (server / 서버) must enforce.

**“Escaping HTML một lần bảo vệ mọi ngữ cảnh (context / 맥락).”** JavaScript/URL/attribute contexts có rules khác.

## Kết nối

[Compiler/language parsing](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md) giúp hiểu code-vs-data. [Identity/auth](./02_identity_authentication_and_authorization.md) giải authorization flaws. [Transactions/concurrency](../05_data_databases/02_transactions_acid_and_concurrency_control.md) cung cấp atomic boundaries chống một số race/TOCTOU patterns.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 threat models and security principles](./00_threat_models_and_security_principles.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
