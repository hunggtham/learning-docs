# Identity, authentication và authorization

Identity systems trả lời ba câu hỏi khác nhau: **ai/đối tượng nào? họ chứng minh identity bằng gì? họ được phép làm gì?** Trộn authentication và authorization là nguyên nhân phổ biến của security bugs.

## Identity

Identity (신원, 아이덴티티) là stable-ish identifier cho user, service, device hoặc workload trong một authority/domain. Username/email có thể thay đổi; internal subject ID thường ổn định hơn.

Identity có lifecycle: provisioning, credential enrollment, role changes, suspension, deletion. Orphaned accounts/keys là risk.

## Authentication

Authentication (인증 / xác thực) xác minh claimant controls credential/factor associated với identity. Password, hardware key, TOTP, certificate, biometric đều là mechanisms với threats khác.

Factors thường phân theo something you know/have/are. MFA mạnh khi factors independent; password + PIN trên cùng channel không necessarily two-factor meaningful.

Authentication event có assurance level/context; “logged in once” không bảo session mãi trustworthy.

## Authorization

Authorization (인가 / phân quyền) quyết định action trên resource có được phép. Model phổ biến:

- RBAC: permissions gắn roles, identities nhận roles.
- ABAC: policy dựa attributes của subject/resource/environment/action.
- ACL: resource liệt kê principals/permissions.
- Capability-based: possession unforgeable token/reference grants authority.

Real systems thường mix.

## Authentication ≠ authorization

Server biết request đến từ user 123 nhưng vẫn phải check user 123 có quyền đọc order 999 không. IDOR/BOLA vulnerabilities xảy ra khi endpoint accepts object ID và chỉ check login, không check ownership/policy.

Every resource access cần complete mediation.

## Sessions

After authentication, server can create session ID stored cookie; session state server-side. Token-based systems carry signed claims (e.g. JWT) nhưng token vẫn cần validation: signature, issuer, audience, expiry, not-before, key rotation và authorization context.

JWT không tự làm system stateless nếu revocation, user state, permissions hoặc refresh tokens cần server data.

## Cookies và browser security

HttpOnly giảm JavaScript access; Secure yêu cầu HTTPS; SameSite controls cross-site sending and helps CSRF defenses. Session cookie should be unpredictable and protected against fixation/stealing.

CSRF exploits browser automatically attaching credentials to cross-site requests; anti-CSRF tokens/SameSite/origin checks mitigate depending architecture. XSS can perform actions as user and steal non-HttpOnly data, so prevention remains critical.

## OAuth 2.0 và OpenID Connect intuition

OAuth 2.0 is authorization framework for delegated access; OpenID Connect adds identity/authentication layer with ID token and standardized endpoints. Using OAuth access token as if it were arbitrary login token without validating intended semantics can be wrong.

Authorization Code + PKCE is common safe flow for public clients. Exact recommendations evolve, so implementation should follow current provider/spec guidance.

## Service identity

Microservices need machine identity too: mTLS certificates, workload identity, short-lived tokens or cloud IAM. Shared static API keys across many services destroy attribution and rotation granularity.

## Least privilege and scope

Token scopes/roles should narrow what holder can do. Short-lived credentials reduce exposure window, but refresh/rotation mechanism becomes critical.

## Mental Model

> **Identity = subject. Authentication = prove/control identity. Authorization = policy decision for action/resource. Session/token = carry evidence/context over time.** Keep these layers explicit.

## Common Misconceptions

**“Authenticated user can access any object ID they know.”** Authentication only says who, not permission.

**“JWT is encrypted.”** Typical JWS JWT is signed but payload readable; JWE is separate encryption form.

**“OAuth = authentication.”** OAuth core delegates authorization; OIDC adds authentication/identity semantics.

## Kết nối

Threat boundaries in [security principles](./00_threat_models_and_security_principles.md), crypto tokens/certs in [cryptography](./01_cryptography_foundations.md), browser channel in [DNS/HTTP/TLS](../06_networks_distributed_systems/03_dns_http_tls_and_web_request.md), application attacks in [vulnerabilities](./03_software_vulnerabilities.md).
