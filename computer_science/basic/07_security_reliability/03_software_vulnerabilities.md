# Memory, web và injection vulnerabilities

Software vulnerability (취약점 / lỗ hổng) xuất hiện khi attacker-controlled input/state vượt qua assumption của program và đạt effect không được phép. Học từng CVE không đủ; cần nhận ra recurring structures: memory boundary violations, code/data confusion, trust-boundary validation failures và authorization gaps.

## Memory corruption

Trong memory-unsafe languages, out-of-bounds write, use-after-free, double free và integer overflow có thể corrupt control/data. Stack buffer overflow kinh điển có thể overwrite return metadata; modern mitigations gồm stack canaries, ASLR, NX/DEP, CFI, hardened allocators.

Mitigations tăng difficulty nhưng không thay fix root bug. Memory-safe languages loại nhiều classes này by construction/checks, nhưng native libraries/unsafe blocks vẫn là boundary.

## Injection: khi data bị hiểu thành code/command

SQL injection xảy ra khi attacker input được concatenated vào query syntax, làm dữ liệu trở thành SQL code. Parameterized query giữ query structure và values separate.

```sql
-- nguy hiểm về pattern
"SELECT ... WHERE name = '" + input + "'"

-- đúng principle
SELECT ... WHERE name = ?
```

Same pattern xuất hiện shell injection, LDAP injection, template injection: **code and data channels bị trộn**.

Parameterization không giải dynamic identifiers/order clauses tự động; allowlist/structured APIs cần cho syntax positions không parameterizable.

## XSS

Cross-Site Scripting cho attacker-controlled content execute trong browser origin context. Stored, reflected, DOM-based variants khác source/flow nhưng root issue là untrusted data vào executable HTML/JS context without proper context-sensitive escaping/sanitization.

Output encoding phải phù hợp HTML text, attribute, JavaScript, URL contexts. CSP là defense-in-depth, không thay correct encoding.

## CSRF

Browser tự gửi cookies tới matching site; malicious page có thể trigger request nếu server chỉ dựa cookie. SameSite, anti-CSRF token, origin validation và requiring custom headers/API patterns là mitigations theo context.

CSRF khác XSS: XSS chạy code trong trusted origin; CSRF lợi dụng ambient authority từ browser.

## SSRF

Server-Side Request Forgery khiến server request URL attacker-controlled, có thể reach internal metadata/services không public. Mitigation cần allowlist destinations/protocols, network egress controls, DNS/IP validation cẩn thận và metadata protections.

## Path traversal

Input như `../../etc/passwd` có thể escape intended directory nếu path join/canonicalization sai. Safe design use generated IDs/storage APIs, normalize và enforce resolved path under allowed root. String prefix check naive có edge cases symbolic links/encoding/platform.

## Deserialization

Unsafe deserialization of attacker data can instantiate unexpected object graphs or trigger gadget chains in ecosystems supporting polymorphic/object deserialization. Prefer simple data formats + explicit schemas/types; never treat untrusted serialized object stream as trustworthy code structure.

## Race vulnerabilities

TOCTOU — Time Of Check To Time Of Use: check permission/path/state rồi attacker changes before use. Atomic OS APIs, file descriptors, transactions hoặc locks reduce gap. Security often requires same atomicity reasoning as concurrency correctness.

## Dependency/supply chain

Vulnerability can enter through dependency, build script, package registry compromise or CI secret leakage. Pin versions/check integrity, minimize dependencies, SBOM/scanning, protected CI credentials and reproducible build practices reduce risk.

## Input validation không phải universal sanitizer

Validate semantic domain at boundary; encode when outputting into syntax context; parameterize code/data; authorize every resource action. One “sanitize()” function cannot safely cover SQL, HTML, shell, URL and JSON contexts.

## Mental Model

> Nhiều vulnerabilities là **boundary confusion**: data becomes code, untrusted identity becomes authorized, path escapes namespace, memory write escapes object. Hãy xác định parser/interpreter nào sẽ đọc input tiếp theo và giữ data ở đúng channel.

## Common Misconceptions

**“ORM ngăn mọi SQL injection.”** Raw queries/dynamic syntax vẫn có thể inject; parameterization principle mới quan trọng.

**“Frontend validation đủ vì user không nhập được giá trị xấu.”** Attacker gọi API trực tiếp; server must enforce.

**“Escaping HTML một lần bảo vệ mọi context.”** JavaScript/URL/attribute contexts có rules khác.

## Kết nối

[Compiler/language parsing](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md) giúp hiểu code-vs-data. [Identity/auth](./02_identity_authentication_and_authorization.md) giải authorization flaws. [Transactions/concurrency](../05_data_databases/02_transactions_acid_and_concurrency_control.md) cung cấp atomic boundaries chống một số race/TOCTOU patterns.
