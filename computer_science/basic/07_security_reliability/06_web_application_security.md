# Web application security

Web security không phải danh sách payloads như `' OR 1=1`. Nó bắt đầu từ trust boundaries: browser chạy code từ nhiều origins, server nhận input từ clients không đáng tin, cookies/tokens đi qua network, backend truy cập database và external services. Vulnerability xuất hiện khi data vượt boundary mà assumptions không được enforce.

## Same-Origin Policy

Browser Same-Origin Policy (SOP) giới hạn script từ một origin đọc resources của origin khác. Origin thường được xác định bởi scheme + host + port.

SOP là isolation boundary của web platform. CORS không “bật security”; nó là mechanism server dùng để nới quyền cross-origin read cho origins được phép.

## XSS: data trở thành code

Cross-Site Scripting xảy ra khi attacker-controlled data được interpreter của browser coi là executable script/markup trong context không intended.

Defense cốt lõi là context-aware output encoding và tránh dangerous sinks. HTML text, HTML attribute, JavaScript string và URL contexts cần encoding khác nhau.

Content Security Policy (CSP) thêm defense-in-depth bằng cách giới hạn sources/execution modes, nhưng không thay thế output safety.

## CSRF: browser mang credentials ngoài ý muốn

Cross-Site Request Forgery lợi dụng việc browser tự động gửi credentials như cookies tới target site khi user bị dụ tạo request từ site khác.

Defenses gồm SameSite cookies, anti-CSRF tokens và checking origin/referer trong phù hợp context. Nếu auth dùng bearer token chỉ gửi qua explicit JavaScript header và attacker site không đọc token, threat model khác.

## SQL/command injection

Injection xảy ra khi untrusted data được concatenate vào language/code context. Prepared statements tách query structure khỏi data parameters.

Same principle áp dụng shell command, LDAP, template và expression languages: **data không được trở thành syntax ngoài ý muốn**.

## SSRF và trust vào network location

Server-Side Request Forgery làm backend fetch attacker-controlled destination. Nếu backend có quyền access internal metadata/admin services, attacker piggybacks trust của server.

Defense cần URL validation, network egress policy, allowlist và protection against DNS rebinding/redirect tricks tùy threat model.

## Session security

Session ID/token là bearer capability: ai sở hữu có thể impersonate user trong phạm vi quyền. Tokens cần entropy đủ, secure transport, appropriate lifetime, rotation/revocation strategy.

Cookie flags `Secure`, `HttpOnly`, `SameSite` bảo vệ các threat khác nhau. `HttpOnly` giảm script access nhưng không làm XSS vô hại vì injected script vẫn có thể gửi requests dưới session.

## Authentication không kết thúc ở login

Password reset, email change, MFA recovery và account linking đều là authentication flows. Attacker thường tìm weakest recovery path thay vì phá strongest login path.

Authorization phải check server-side trên mỗi sensitive object/action. Hidden button trong UI không phải access control.

## File upload

Upload file kết hợp content-type ambiguity, parser bugs, path traversal, executable content và storage permissions. Safe design thường tách upload storage khỏi executable web root, rename generated IDs, validate type/content và scan/process trong constrained environment.

## Security headers và browser primitives

HSTS ép HTTPS cho future requests; CSP giới hạn content execution; frame-ancestors/X-Frame-Options giảm clickjacking; Referrer-Policy kiểm soát referrer leakage.

Headers chỉ hiệu quả khi hiểu threat tương ứng, không phải checklist score.

## Common Misconceptions

**“Frontend validation đủ vì user không sửa được UI.”** Client hoàn toàn attacker-controlled.

**“JWT an toàn hơn session.”** JWT chỉ là token format/signing model; lifecycle, storage, revocation và authorization vẫn quyết định security.

**“HTTPS ngăn XSS/SQL injection.”** TLS bảo vệ data in transit, không sửa application logic.

## Mental Model

> Web security là kiểm soát interpreter boundaries, origin boundaries, credential boundaries và authorization boundaries. Mỗi lần data đổi context, phải hỏi ai kiểm soát nó và component tiếp theo sẽ diễn giải nó như data hay code.

## Kết nối

Đọc [threat models](./00_threat_models_and_security_principles.md), [identity/auth](./02_identity_authentication_and_authorization.md), [software vulnerabilities](./03_software_vulnerabilities.md) và [HTTP/TLS](../06_networks_distributed_systems/03_dns_http_tls_and_web_request.md).