# Bộ nhớ (memory / 메모리), web và injection vulnerabilities

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Memory, web và injection vulnerabilities**. Route đi từ memory corruption → injection/XSS/CSRF/SSRF → path/deserialization/race → dependency/supply-chain → input validation, để mỗi lỗi được nối với trust boundary và exploit path.

Software vulnerability (취약점 / lỗ hổng) xuất hiện khi attacker-controlled đầu vào (input / 입력)/trạng thái (state / 상태) vượt qua giả định (assumption / 가정) của program và đạt tác động (effect / 효과) không được phép. Học từng CVE không đủ; cần nhận ra recurring structures: bộ nhớ (memory / 메모리) ranh giới (boundary / 경계) violations, mã (code / 코드)/dữ liệu (data / 데이터) confusion, trust-boundary kiểm tra hợp lệ (validation / 검증) failures và authorization gaps.

## Bộ nhớ (memory / 메모리) corruption

Trong memory-unsafe languages, out-of-bounds ghi (write / 쓰기), use-after-free, double free và integer overflow có thể corrupt điều khiển (control / 제어)/dữ liệu (data / 데이터). ngăn xếp (stack / 스택) buffer overflow kinh điển có thể overwrite return siêu dữ liệu (metadata / 메타데이터); hiện đại (modern / 현대적) mitigations gồm ngăn xếp (stack / 스택) canaries, ASLR, NX/DEP, CFI, hardened allocators.

Mitigations tăng difficulty nhưng không thay fix gốc (root / 루트) bug. Memory-safe languages loại nhiều classes này by construction/checks, nhưng bản địa (native / 네이티브) libraries/unsafe blocks vẫn là ranh giới (boundary / 경계).

> **Chuyển mạch:** Memory corruption phá invariant của address space; injection phá ranh giới khi data bị diễn giải thành code/command, và XSS là trường hợp web-specific của cùng một lỗi boundary.

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

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **Injection: khi dữ liệu (data / 데이터) bị hiểu thành mã (code / 코드)/command** nêu điều cần giải thích; **XSS** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **CSRF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## XSS

Cross-Site Scripting cho attacker-controlled content execute trong trình duyệt (browser / 브라우저) origin ngữ cảnh (context / 맥락). Stored, reflected, DOM-based variants khác nguồn (source / 소스)/luồng (flow / 흐름) nhưng gốc (root / 루트) issue là untrusted dữ liệu (data / 데이터) vào executable HTML/JS ngữ cảnh (context / 맥락) without proper context-sensitive escaping/sanitization.

Đầu ra (output / 출력) encoding phải phù hợp HTML văn bản (text / 텍스트), attribute, JavaScript, URL contexts. CSP là defense-in-depth, không thay correct encoding.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **CSRF** tiếp nhận điểm tựa từ **XSS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SSRF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSRF

Trình duyệt (browser / 브라우저) tự gửi cookies tới matching site; malicious page có thể trigger yêu cầu (request / 요청) nếu máy chủ (server / 서버) chỉ dựa cookie. SameSite, anti-CSRF đơn vị từ (token / 토큰), origin kiểm tra hợp lệ (validation / 검증) và requiring custom headers/API patterns là mitigations theo ngữ cảnh (context / 맥락).

CSRF khác XSS: XSS chạy mã (code / 코드) trong trusted origin; CSRF lợi dụng ambient authority từ trình duyệt (browser / 브라우저).

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **SSRF** tiếp nhận điểm tựa từ **CSRF** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đường dẫn (path / 경로) traversal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SSRF

Server-Side yêu cầu (request / 요청) Forgery khiến máy chủ (server / 서버) yêu cầu (request / 요청) URL attacker-controlled, có thể reach nội bộ (internal / 내부) siêu dữ liệu (metadata / 메타데이터)/services không công khai (public / 공개). Mitigation cần allowlist destinations/protocols, mạng (network / 네트워크) egress controls, DNS/IP kiểm tra hợp lệ (validation / 검증) cẩn thận và siêu dữ liệu (metadata / 메타데이터) protections.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **SSRF** xác định đầu vào; **Đường dẫn (path / 경로) traversal** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Deserialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đường dẫn (path / 경로) traversal

Đầu vào (input / 입력) như `../../etc/passwd` có thể escape intended directory nếu đường dẫn (path / 경로) phép nối (join / 조인)/canonicalization sai. Safe thiết kế (design / 설계) use generated IDs/lưu trữ (storage / 저장소) APIs, normalize và enforce resolved đường dẫn (path / 경로) under allowed gốc (root / 루트). String prefix check naive có edge cases symbolic links/encoding/nền tảng (platform / 플랫폼).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **Đường dẫn (path / 경로) traversal** xác định đầu vào; **Deserialization** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Race vulnerabilities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deserialization

Unsafe deserialization of attacker dữ liệu (data / 데이터) can instantiate unexpected đối tượng (object / 객체) graphs or trigger gadget chains in ecosystems supporting polymorphic/đối tượng (object / 객체) deserialization. Prefer simple dữ liệu (data / 데이터) formats + tường minh (explicit / 명시적) schemas/types; never treat untrusted serialized đối tượng (object / 객체) stream as trustworthy mã (code / 코드) cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **Race vulnerabilities** tiếp nhận điểm tựa từ **Deserialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phụ thuộc (dependency / 의존성)/supply chuỗi (chain / 사슬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Race vulnerabilities

TOCTOU — thời gian (time / 시간) Of Check To thời gian (time / 시간) Of Use: check permission/đường dẫn (path / 경로)/trạng thái (state / 상태) rồi attacker changes before use. Atomic OS APIs, tệp (file / 파일) descriptors, transactions hoặc locks reduce gap. bảo mật (security / 보안) often requires same atomicity lập luận (reasoning / 추론) as tính đồng thời (concurrency / 동시성) tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **Race vulnerabilities** xác định đầu vào; **Phụ thuộc (dependency / 의존성)/supply chuỗi (chain / 사슬)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Đầu vào (input / 입력) kiểm tra hợp lệ (validation / 검증) không phải universal sanitizer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phụ thuộc (dependency / 의존성)/supply chuỗi (chain / 사슬)

Vulnerability can enter through phụ thuộc (dependency / 의존성), bản dựng (build / 빌드) script, gói (package / 패키지) registry compromise or CI secret leakage. Pin versions/check integrity, minimize dependencies, SBOM/scanning, protected CI credentials and reproducible bản dựng (build / 빌드) practices reduce rủi ro (risk / 위험).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **Phụ thuộc (dependency / 의존성)/supply chuỗi (chain / 사슬)** xác định đầu vào; **Đầu vào (input / 입력) kiểm tra hợp lệ (validation / 검증) không phải universal sanitizer** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đầu vào (input / 입력) kiểm tra hợp lệ (validation / 검증) không phải universal sanitizer

Validate ngữ nghĩa (semantic / 의미적) lĩnh vực (domain / 도메인) at ranh giới (boundary / 경계); encode when outputting into cú pháp (syntax / 문법) ngữ cảnh (context / 맥락); parameterize mã (code / 코드)/dữ liệu (data / 데이터); authorize every tài nguyên (resource / 자원) hành động (action / 동작). One “sanitize()” hàm (function / 함수) cannot safely cover SQL, HTML, shell, URL and JSON contexts.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Đầu vào (input / 입력) kiểm tra hợp lệ (validation / 검증) không phải universal sanitizer** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Nhiều vulnerabilities là **ranh giới (boundary / 경계) confusion**: dữ liệu (data / 데이터) becomes mã (code / 코드), untrusted định danh (identity / 식별자) becomes authorized, đường dẫn (path / 경로) escapes không gian tên (namespace / 네임스페이스), bộ nhớ (memory / 메모리) ghi (write / 쓰기) escapes đối tượng (object / 객체). Hãy xác định parser/trình thông dịch (interpreter / 인터프리터) nào sẽ đọc đầu vào (input / 입력) tiếp theo và giữ dữ liệu (data / 데이터) ở đúng channel.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“ORM ngăn mọi SQL injection.”** Raw queries/động (dynamic / 동적) cú pháp (syntax / 문법) vẫn có thể inject; parameterization principle mới quan trọng.

**“Frontend kiểm tra hợp lệ (validation / 검증) đủ vì người dùng (user / 사용자) không nhập được giá trị xấu.”** Attacker gọi API trực tiếp; máy chủ (server / 서버) must enforce.

**“Escaping HTML một lần bảo vệ mọi ngữ cảnh (context / 맥락).”** JavaScript/URL/attribute contexts có rules khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리), web và injection vulnerabilities**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Compiler/language parsing](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md) giúp hiểu code-vs-data. [Identity/auth](./02_identity_authentication_and_authorization.md) giải authorization flaws. [Transactions/concurrency](../05_data_databases/02_transactions_acid_and_concurrency_control.md) cung cấp atomic boundaries chống một số race/TOCTOU patterns.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
