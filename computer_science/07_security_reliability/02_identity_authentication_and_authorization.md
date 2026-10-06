# Định danh (identity / 식별자), authentication và authorization

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Identity, authentication và authorization**. Route đi từ identity claims → authentication factors → authorization policy/scope → sessions/cookies → OAuth/OIDC và service identity, để “ai là ai” được tách khỏi “được làm gì”.

Định danh (identity / 식별자) các hệ thống (systems / 시스템들) trả lời ba câu hỏi khác nhau: **ai/đối tượng nào? họ chứng minh định danh (identity / 식별자) bằng gì? họ được phép làm gì?** Trộn authentication và authorization là nguyên nhân phổ biến của bảo mật (security / 보안) bugs.

## Định danh (identity / 식별자)

Định danh (identity / 식별자) là stable-ish identifier cho người dùng (user / 사용자), dịch vụ (service / 서비스), thiết bị (device / 장치) hoặc tải công việc (workload / 워크로드) trong một authority/lĩnh vực (domain / 도메인). Username/email có thể thay đổi; nội bộ (internal / 내부) subject ID thường ổn định hơn.

Định danh (identity / 식별자) có vòng đời (lifecycle / 생명주기): provisioning, credential enrollment, role changes, suspension, deletion. Orphaned accounts/keys là rủi ro (risk / 위험).

> **Nối mạch:** Identity names the subject; authentication proves control of that identity, and authorization next evaluates which actions/resources the authenticated subject may use.

## Authentication

Authentication (인증 / xác thực) xác minh claimant controls credential/factor associated với định danh (identity / 식별자). Password, hardware key, TOTP, certificate, biometric đều là mechanisms với threats khác.

Factors thường phân theo something you know/have/are. MFA mạnh khi factors independent; password + PIN trên cùng channel không necessarily two-factor meaningful.

Authentication sự kiện (event / 이벤트) có assurance mức (level / 수준)/ngữ cảnh (context / 맥락); “logged in once” không bảo session mãi trustworthy.

> **Nối mạch:** **Authorization** nối từ **Authentication** sang **Authentication ≠ authorization**, vì cơ chế trước tạo đầu vào cho bước sau.

## Authorization

Authorization (인가 / phân quyền) quyết định hành động (action / 동작) trên tài nguyên (resource / 자원) có được phép. mô hình (model / 모델) phổ biến:

- RBAC: permissions gắn roles, identities nhận roles.
- ABAC: chính sách (policy / 정책) dựa attributes của subject/tài nguyên (resource / 자원)/môi trường (environment / 환경)/hành động (action / 동작).
- ACL: tài nguyên (resource / 자원) liệt kê principals/permissions.
- Capability-based: possession unforgeable đơn vị từ (token / 토큰)/tham chiếu (reference / 참조) grants authority.

Real các hệ thống (systems / 시스템들) thường mix.

> **Nối mạch:** **Authentication ≠ authorization** nối từ **Authorization** sang **Sessions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Authentication ≠ authorization

Máy chủ (server / 서버) biết yêu cầu (request / 요청) đến từ người dùng (user / 사용자) 123 nhưng vẫn phải check người dùng (user / 사용자) 123 có quyền đọc thứ tự (order / 순서) 999 không. IDOR/BOLA vulnerabilities xảy ra khi endpoint accepts đối tượng (object / 객체) ID và chỉ check login, không check quyền sở hữu (ownership / 소유권)/chính sách (policy / 정책).

Every tài nguyên (resource / 자원) truy cập (access / 접근) cần complete mediation.

> **Nối mạch:** **Sessions** nối từ **Authentication ≠ authorization** sang **Cookies và trình duyệt (browser / 브라우저) bảo mật (security / 보안)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sessions

After authentication, máy chủ (server / 서버) can create session ID stored cookie; session trạng thái (state / 상태) server-side. Token-based các hệ thống (systems / 시스템들) carry signed claims (e.g. JWT) nhưng đơn vị từ (token / 토큰) vẫn cần kiểm tra hợp lệ (validation / 검증): signature, issuer, audience, expiry, not-before, key rotation và authorization ngữ cảnh (context / 맥락).

JWT không tự làm hệ thống (system / 시스템) stateless nếu revocation, người dùng (user / 사용자) trạng thái (state / 상태), permissions hoặc refresh tokens cần máy chủ (server / 서버) dữ liệu (data / 데이터).

> **Nối mạch:** **Cookies và trình duyệt (browser / 브라우저) bảo mật (security / 보안)** nối từ **Sessions** sang **OAuth 2.0 và OpenID Connect intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cookies và trình duyệt (browser / 브라우저) bảo mật (security / 보안)

HttpOnly giảm JavaScript truy cập (access / 접근); Secure yêu cầu HTTPS; SameSite controls cross-site sending and helps CSRF defenses. Session cookie should be unpredictable and protected against fixation/stealing.

CSRF exploits trình duyệt (browser / 브라우저) automatically attaching credentials to cross-site requests; anti-CSRF tokens/SameSite/origin checks mitigate depending kiến trúc (architecture / 아키텍처). XSS can perform actions as người dùng (user / 사용자) and steal non-HttpOnly dữ liệu (data / 데이터), so prevention remains trọng yếu (critical / 중요).

> **Nối mạch:** **OAuth 2.0 và OpenID Connect intuition** nối từ **Cookies và trình duyệt (browser / 브라우저) bảo mật (security / 보안)** sang **Dịch vụ (service / 서비스) định danh (identity / 식별자)**, vì cơ chế trước tạo đầu vào cho bước sau.

## OAuth 2.0 và OpenID Connect intuition

OAuth 2.0 is authorization khung phần mềm (framework / 프레임워크) for delegated truy cập (access / 접근); OpenID Connect adds định danh (identity / 식별자)/authentication tầng (layer / 계층) with ID đơn vị từ (token / 토큰) and standardized endpoints. Using OAuth truy cập (access / 접근) đơn vị từ (token / 토큰) as if it were arbitrary login đơn vị từ (token / 토큰) without validating intended ngữ nghĩa (semantics / 의미론) can be wrong.

Authorization mã (code / 코드) + PKCE is dùng chung (common / 공통) safe luồng (flow / 흐름) for công khai (public / 공개) clients. chính xác (exact / 정확한) recommendations evolve, so hiện thực (implementation / 구현) should follow hiện tại (current / 현재) provider/spec guidance.

> **Nối mạch:** **Dịch vụ (service / 서비스) định danh (identity / 식별자)** nối từ **OAuth 2.0 và OpenID Connect intuition** sang **Least privilege and phạm vi (scope / 범위)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dịch vụ (service / 서비스) định danh (identity / 식별자)

Microservices need machine định danh (identity / 식별자) too: mTLS certificates, tải công việc (workload / 워크로드) định danh (identity / 식별자), short-lived tokens or cloud IAM. dùng chung (shared / 공유) static API keys across many services destroy attribution and rotation granularity.

> **Nối mạch:** **Least privilege and phạm vi (scope / 범위)** nối từ **Dịch vụ (service / 서비스) định danh (identity / 식별자)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Least privilege and phạm vi (scope / 범위)

Đơn vị từ (token / 토큰) scopes/roles should narrow what holder can do. Short-lived credentials reduce exposure cửa sổ (window / 윈도우), but refresh/rotation cơ chế (mechanism / 메커니즘) becomes trọng yếu (critical / 중요).

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Least privilege and phạm vi (scope / 범위)**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> **định danh (identity / 식별자) = subject. Authentication = prove/điều khiển (control / 제어) định danh (identity / 식별자). Authorization = chính sách (policy / 정책) quyết định (decision / 결정) for hành động (action / 동작)/tài nguyên (resource / 자원). Session/đơn vị từ (token / 토큰) = carry bằng chứng (evidence / 증거)/ngữ cảnh (context / 맥락) over thời gian (time / 시간).** Keep these layers tường minh (explicit / 명시적).

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“Authenticated người dùng (user / 사용자) can truy cập (access / 접근) any đối tượng (object / 객체) ID they know.”** Authentication only says who, not permission.

**“JWT is encrypted.”** Typical JWS JWT is signed but payload readable; JWE is separate encryption form.

**“OAuth = authentication.”** OAuth cốt lõi (core / 핵심) delegates authorization; OIDC adds authentication/định danh (identity / 식별자) ngữ nghĩa (semantics / 의미론).

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Threat boundaries in [security principles](./00_threat_models_and_security_principles.md), crypto tokens/certs in [cryptography](./01_cryptography_foundations.md), trình duyệt (browser / 브라우저) channel in [DNS/HTTP/TLS](../06_networks_distributed_systems/03_dns_http_tls_and_web_request.md), ứng dụng (application / 애플리케이션) attacks in [vulnerabilities](./03_software_vulnerabilities.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
