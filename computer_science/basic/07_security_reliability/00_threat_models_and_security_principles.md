# Threat model và security principles

Security (보안 / an toàn thông tin) không bắt đầu bằng encryption. Nó bắt đầu bằng câu hỏi: **ta đang bảo vệ asset nào, khỏi actor nào, qua attack surface nào, và property nào phải được giữ?** Không có threat model, từ “secure” quá mơ hồ để kiểm chứng.

## Security properties

CIA triad là mental model cổ điển: Confidentiality giữ bí mật khỏi unauthorized readers; Integrity ngăn/nhận biết unauthorized modification; Availability giữ service/resources usable khi cần.

Ngoài ra còn authenticity (đúng thực thể), accountability/auditability, non-repudiation trong context phù hợp, privacy và safety. Một system có confidentiality mạnh nhưng availability tệ vẫn không “secure” theo nhu cầu vận hành.

## Threat model

Threat model (위협 모델) xác định assets, trust boundaries, actors/capabilities, entry points và abuse cases. Internet attacker khác malicious insider; compromised application process khác physical attacker; nation-state khác opportunistic bot.

Một control chỉ có ý nghĩa relative to threat. Disk encryption bảo vệ stolen powered-off laptop nhưng không ngăn malware đọc plaintext khi user logged in.

## Trust boundary

Trust boundary là nơi data/control đi từ context có trust assumptions khác sang context khác: browser→server, user input→SQL, app→kernel, service A→service B, tenant→shared platform.

Mọi boundary cần validation/authentication/authorization theo risk. “Internal network” không nên mặc định trusted tuyệt đối vì compromised internal service có thể pivot.

## Principle of least privilege

Mỗi identity/process chỉ được rights cần thiết, trong scope/time cần thiết. DB application account không nên DROP toàn schema nếu chỉ CRUD vài tables; container không nên privileged; API token không nên admin nếu chỉ read.

Least privilege giảm blast radius nhưng tăng management complexity. Good design dùng roles/scopes/capabilities để quyền vừa đủ mà không trở thành permission chaos.

## Defense in depth

Không control nào hoàn hảo. TLS + authentication + authorization + input validation + sandbox + monitoring + backups bảo vệ different failure modes. Layers nên có failure independence tương đối; ba controls cùng phụ thuộc một secret không thật sự độc lập.

## Secure defaults và fail-safe defaults

Default nên deny/least privilege, explicit opt-in cho dangerous access. Error path không được “nếu auth service timeout thì allow”. Fail-open đôi khi cần availability-critical systems, nhưng phải là deliberate risk trade-off.

## Minimize attack surface

Mỗi endpoint, parser, dependency, open port, privilege và feature là potential attack surface. Remove unused services, reduce exposed APIs, patch dependencies, constrain inputs. Simplicity có security value vì fewer states/interactions để reason.

## Complete mediation

Authorization cần check mọi protected access, không chỉ UI path. Hiding button không bảo vệ server API. Cache cũng phải preserve authorization semantics; cache key thiếu tenant/user context có thể leak data.

## Separation of duties

Critical action có thể require multiple independent roles/approvals, giảm abuse hoặc single credential compromise. Deployment approval, key management và financial workflows thường áp dụng.

## Security vs usability/performance

Controls có cost. MFA thêm friction; strong KDF tốn CPU; encryption adds overhead; short session expiry increases reauth. Good engineering quantify threat/cost thay vì bỏ security hoặc maximize friction.

## Mental Model

> Security là **quản lý trust dưới adversarial behavior**. Bắt đầu từ asset → threat → boundary → invariant → control → residual risk, không bắt đầu từ danh sách công nghệ.

## Common Misconceptions

**“Dùng HTTPS là secure.”** TLS bảo channel, không sửa broken authorization, injection hay compromised endpoint.

**“Ở internal network thì trusted.”** Network location chỉ là một signal; identity/authorization vẫn cần.

**“Security là feature thêm cuối.”** Data model, privilege boundary và protocol design quyết định rất nhiều properties từ đầu.

## Kết nối

OS isolation ở [privilege/virtualization](../03_operating_systems/05_privilege_isolation_and_virtualization.md). Cryptographic mechanisms ở [cryptography](./01_cryptography_foundations.md); identity/access ở [authentication/authorization](./02_identity_authentication_and_authorization.md); implementation failures ở [vulnerabilities](./03_software_vulnerabilities.md).
