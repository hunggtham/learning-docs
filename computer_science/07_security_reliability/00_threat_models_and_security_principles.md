# Threat mô hình (model / 모델) và bảo mật (security / 보안) principles

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Threat models và security principles**. Route đi từ security properties → assets/actors/trust boundary → least privilege/defense in depth → secure defaults và attack surface, để biện pháp bảo vệ xuất phát từ mối đe dọa cụ thể.

Bảo mật (security / 보안) không bắt đầu bằng encryption. Nó bắt đầu bằng câu hỏi: **ta đang bảo vệ asset nào, khỏi actor nào, qua attack surface nào, và thuộc tính (property / 속성) nào phải được giữ?** Không có threat mô hình (model / 모델), từ “secure” quá mơ hồ để kiểm chứng.

## Bảo mật (security / 보안) properties

CIA triad là mô hình tư duy (mental model / 사고 모델) cổ điển: Confidentiality giữ bí mật khỏi unauthorized readers; Integrity ngăn/nhận biết unauthorized modification; Availability giữ dịch vụ (service / 서비스)/resources usable khi cần.

Ngoài ra còn authenticity (đúng thực thể), accountability/auditability, non-repudiation trong ngữ cảnh (context / 맥락) phù hợp, privacy và an toàn (safety / 안전). Một hệ thống (system / 시스템) có confidentiality mạnh nhưng availability tệ vẫn không “secure” theo nhu cầu vận hành.

> **Nối mạch:** Security properties nêu điều cần bảo vệ; threat model đặt adversary và assets vào scope, rồi trust boundary chỉ ra nơi assumptions phải được kiểm chứng.

## Threat mô hình (model / 모델)

Threat mô hình (model / 모델) xác định assets, trust boundaries, actors/capabilities, entry points và abuse cases. Internet attacker khác malicious insider; compromised ứng dụng (application / 애플리케이션) tiến trình (process / 프로세스) khác vật lý (physical / 물리적) attacker; nation-state khác opportunistic bot.

Một điều khiển (control / 제어) chỉ có ý nghĩa relative to threat. Disk encryption bảo vệ stolen powered-off laptop nhưng không ngăn malware đọc plaintext khi người dùng (user / 사용자) logged in.

> **Nối mạch:** **Threat mô hình (model / 모델)** đặt tiêu chí; **Trust ranh giới (boundary / 경계)** dùng nó để kiểm tra ranh giới, rồi **Principle of least privilege** mở rộng hệ quả.

## Trust ranh giới (boundary / 경계)

Trust ranh giới (boundary / 경계) là nơi dữ liệu (data / 데이터)/điều khiển (control / 제어) đi từ ngữ cảnh (context / 맥락) có trust các giả định (assumptions / 가정들) khác sang ngữ cảnh (context / 맥락) khác: trình duyệt (browser / 브라우저)→máy chủ (server / 서버), người dùng (user / 사용자) đầu vào (input / 입력)→SQL, app→kernel, dịch vụ (service / 서비스) A→dịch vụ (service / 서비스) B, tenant→dùng chung (shared / 공유) nền tảng (platform / 플랫폼).

Mọi ranh giới (boundary / 경계) cần kiểm tra hợp lệ (validation / 검증)/authentication/authorization theo rủi ro (risk / 위험). “nội bộ (internal / 내부) mạng (network / 네트워크)” không nên mặc định trusted tuyệt đối vì compromised nội bộ (internal / 내부) dịch vụ (service / 서비스) có thể pivot.

> **Nối mạch:** **Trust ranh giới (boundary / 경계)** đặt tiêu chí; **Principle of least privilege** dùng nó để kiểm tra ranh giới, rồi **Defense in độ sâu (depth / 깊이)** mở rộng hệ quả.

## Principle of least privilege

Mỗi định danh (identity / 식별자)/tiến trình (process / 프로세스) chỉ được rights cần thiết, trong phạm vi (scope / 범위)/thời gian (time / 시간) cần thiết. DB ứng dụng (application / 애플리케이션) account không nên DROP toàn lược đồ (schema / 스키마) nếu chỉ CRUD vài tables; bộ chứa (container / 컨테이너) không nên privileged; API đơn vị từ (token / 토큰) không nên admin nếu chỉ read.

Least privilege giảm blast radius nhưng tăng management độ phức tạp (complexity / 복잡도). Good thiết kế (design / 설계) dùng roles/scopes/capabilities để quyền vừa đủ mà không trở thành permission chaos.

> **Nối mạch:** **Defense in độ sâu (depth / 깊이)** nối từ **Principle of least privilege** sang **Secure defaults và fail-safe defaults**, vì cơ chế trước tạo đầu vào cho bước sau.

## Defense in độ sâu (depth / 깊이)

Không điều khiển (control / 제어) nào hoàn hảo. TLS + authentication + authorization + đầu vào (input / 입력) kiểm tra hợp lệ (validation / 검증) + sandbox + monitoring + backups bảo vệ different thất bại (failure / 실패) modes. Layers nên có thất bại (failure / 실패) independence tương đối; ba controls cùng phụ thuộc một secret không thật sự độc lập.

> **Nối mạch:** **Secure defaults và fail-safe defaults** nối từ **Defense in độ sâu (depth / 깊이)** sang **Minimize attack surface**, vì cơ chế trước tạo đầu vào cho bước sau.

## Secure defaults và fail-safe defaults

Default nên deny/least privilege, tường minh (explicit / 명시적) opt-in cho dangerous truy cập (access / 접근). lỗi (error / 오류) đường dẫn (path / 경로) không được “nếu auth dịch vụ (service / 서비스) hết thời gian chờ (timeout / 타임아웃) thì allow”. Fail-open đôi khi cần availability-critical các hệ thống (systems / 시스템들), nhưng phải là deliberate rủi ro (risk / 위험) sự đánh đổi (trade-off / 트레이드오프).

> **Nối mạch:** **Minimize attack surface** nối từ **Secure defaults và fail-safe defaults** sang **Complete mediation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Minimize attack surface

Mỗi endpoint, parser, phụ thuộc (dependency / 의존성), open cổng (port / 포트), privilege và tính năng (feature / 기능) là potential attack surface. Remove unused services, reduce exposed APIs, patch dependencies, constrain inputs. Simplicity có bảo mật (security / 보안) giá trị (value / 값) vì fewer states/interactions để reason.

> **Nối mạch:** **Complete mediation** nối từ **Minimize attack surface** sang **Separation of duties**, vì cơ chế trước tạo đầu vào cho bước sau.

## Complete mediation

Authorization cần check mọi protected truy cập (access / 접근), không chỉ UI đường dẫn (path / 경로). Hiding button không bảo vệ máy chủ (server / 서버) API. bộ nhớ đệm (cache / 캐시) cũng phải preserve authorization ngữ nghĩa (semantics / 의미론); bộ nhớ đệm (cache / 캐시) key thiếu tenant/người dùng (user / 사용자) ngữ cảnh (context / 맥락) có thể leak dữ liệu (data / 데이터).

> **Nối mạch:** **Separation of duties** nối từ **Complete mediation** sang **Bảo mật (security / 보안) vs usability/hiệu năng (performance / 성능)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Separation of duties

Trọng yếu (critical / 중요) hành động (action / 동작) có thể require multiple independent roles/approvals, giảm abuse hoặc single credential compromise. triển khai (deployment / 배포) approval, key management và financial workflows thường áp dụng.

> **Nối mạch:** **Bảo mật (security / 보안) vs usability/hiệu năng (performance / 성능)** nối từ **Separation of duties** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bảo mật (security / 보안) vs usability/hiệu năng (performance / 성능)

Controls có chi phí (cost / 비용). MFA thêm friction; strong KDF tốn CPU; encryption adds overhead; short session expiry increases reauth. Good kỹ thuật (engineering / 엔지니어링) quantify threat/chi phí (cost / 비용) thay vì bỏ bảo mật (security / 보안) hoặc maximize friction.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Bảo mật (security / 보안) vs usability/hiệu năng (performance / 성능)**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> bảo mật (security / 보안) là **quản lý trust dưới adversarial hành vi (behavior / 동작)**. Bắt đầu từ asset → threat → ranh giới (boundary / 경계) → bất biến (invariant / 불변식) → điều khiển (control / 제어) → residual rủi ro (risk / 위험), không bắt đầu từ danh sách công nghệ.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“Dùng HTTPS là secure.”** TLS bảo channel, không sửa broken authorization, injection hay compromised endpoint.

**“Ở nội bộ (internal / 내부) mạng (network / 네트워크) thì trusted.”** mạng (network / 네트워크) location chỉ là một tín hiệu (signal / 신호); định danh (identity / 식별자)/authorization vẫn cần.

**“bảo mật (security / 보안) là tính năng (feature / 기능) thêm cuối.”** mô hình dữ liệu (data model / 데이터 모델), privilege ranh giới (boundary / 경계) và giao thức (protocol / 프로토콜) thiết kế (design / 설계) quyết định rất nhiều properties từ đầu.

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

OS isolation ở [privilege/virtualization](../03_operating_systems/05_privilege_isolation_and_virtualization.md). Cryptographic mechanisms ở [cryptography](./01_cryptography_foundations.md); định danh (identity / 식별자)/truy cập (access / 접근) ở [authentication/authorization](./02_identity_authentication_and_authorization.md); hiện thực (implementation / 구현) failures ở [vulnerabilities](./03_software_vulnerabilities.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
