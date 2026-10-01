# Threat mô hình (model / 모델) và bảo mật (security / 보안) principles

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Bảo mật (security / 보안) properties** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Threat mô hình (model / 모델)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Bảo mật (security / 보안) không bắt đầu bằng encryption. Nó bắt đầu bằng câu hỏi: **ta đang bảo vệ asset nào, khỏi actor nào, qua attack surface nào, và thuộc tính (property / 속성) nào phải được giữ?** Không có threat mô hình (model / 모델), từ “secure” quá mơ hồ để kiểm chứng.

## Bảo mật (security / 보안) properties

CIA triad là mô hình tư duy (mental model / 사고 모델) cổ điển: Confidentiality giữ bí mật khỏi unauthorized readers; Integrity ngăn/nhận biết unauthorized modification; Availability giữ dịch vụ (service / 서비스)/resources usable khi cần.

Ngoài ra còn authenticity (đúng thực thể), accountability/auditability, non-repudiation trong ngữ cảnh (context / 맥락) phù hợp, privacy và an toàn (safety / 안전). Một hệ thống (system / 시스템) có confidentiality mạnh nhưng availability tệ vẫn không “secure” theo nhu cầu vận hành.

> **Chuyển mạch:** Security properties nêu điều cần bảo vệ; threat model đặt adversary và assets vào scope, rồi trust boundary chỉ ra nơi assumptions phải được kiểm chứng.

## Threat mô hình (model / 모델)

Threat mô hình (model / 모델) xác định assets, trust boundaries, actors/capabilities, entry points và abuse cases. Internet attacker khác malicious insider; compromised ứng dụng (application / 애플리케이션) tiến trình (process / 프로세스) khác vật lý (physical / 물리적) attacker; nation-state khác opportunistic bot.

Một điều khiển (control / 제어) chỉ có ý nghĩa relative to threat. Disk encryption bảo vệ stolen powered-off laptop nhưng không ngăn malware đọc plaintext khi người dùng (user / 사용자) logged in.

> **Chuyển mạch:** Ở chặng này của **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Threat mô hình (model / 모델)** đã nêu tiêu chí phân biệt, còn **Trust ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Principle of least privilege** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trust ranh giới (boundary / 경계)

Trust ranh giới (boundary / 경계) là nơi dữ liệu (data / 데이터)/điều khiển (control / 제어) đi từ ngữ cảnh (context / 맥락) có trust các giả định (assumptions / 가정들) khác sang ngữ cảnh (context / 맥락) khác: trình duyệt (browser / 브라우저)→máy chủ (server / 서버), người dùng (user / 사용자) đầu vào (input / 입력)→SQL, app→kernel, dịch vụ (service / 서비스) A→dịch vụ (service / 서비스) B, tenant→dùng chung (shared / 공유) nền tảng (platform / 플랫폼).

Mọi ranh giới (boundary / 경계) cần kiểm tra hợp lệ (validation / 검증)/authentication/authorization theo rủi ro (risk / 위험). “nội bộ (internal / 내부) mạng (network / 네트워크)” không nên mặc định trusted tuyệt đối vì compromised nội bộ (internal / 내부) dịch vụ (service / 서비스) có thể pivot.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Trust ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **Principle of least privilege** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Defense in độ sâu (depth / 깊이)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Principle of least privilege

Mỗi định danh (identity / 식별자)/tiến trình (process / 프로세스) chỉ được rights cần thiết, trong phạm vi (scope / 범위)/thời gian (time / 시간) cần thiết. DB ứng dụng (application / 애플리케이션) account không nên DROP toàn lược đồ (schema / 스키마) nếu chỉ CRUD vài tables; bộ chứa (container / 컨테이너) không nên privileged; API đơn vị từ (token / 토큰) không nên admin nếu chỉ read.

Least privilege giảm blast radius nhưng tăng management độ phức tạp (complexity / 복잡도). Good thiết kế (design / 설계) dùng roles/scopes/capabilities để quyền vừa đủ mà không trở thành permission chaos.

> **Chuyển mạch:** Trong **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Defense in độ sâu (depth / 깊이)** tiếp nhận điểm tựa từ **Principle of least privilege** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Secure defaults và fail-safe defaults** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Defense in độ sâu (depth / 깊이)

Không điều khiển (control / 제어) nào hoàn hảo. TLS + authentication + authorization + đầu vào (input / 입력) kiểm tra hợp lệ (validation / 검증) + sandbox + monitoring + backups bảo vệ different thất bại (failure / 실패) modes. Layers nên có thất bại (failure / 실패) independence tương đối; ba controls cùng phụ thuộc một secret không thật sự độc lập.

> **Chuyển mạch:** Ở chặng này của **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Secure defaults và fail-safe defaults** tiếp nhận điểm tựa từ **Defense in độ sâu (depth / 깊이)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Minimize attack surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Secure defaults và fail-safe defaults

Default nên deny/least privilege, tường minh (explicit / 명시적) opt-in cho dangerous truy cập (access / 접근). lỗi (error / 오류) đường dẫn (path / 경로) không được “nếu auth dịch vụ (service / 서비스) hết thời gian chờ (timeout / 타임아웃) thì allow”. Fail-open đôi khi cần availability-critical các hệ thống (systems / 시스템들), nhưng phải là deliberate rủi ro (risk / 위험) sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Minimize attack surface** tiếp nhận điểm tựa từ **Secure defaults và fail-safe defaults** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Complete mediation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Minimize attack surface

Mỗi endpoint, parser, phụ thuộc (dependency / 의존성), open cổng (port / 포트), privilege và tính năng (feature / 기능) là potential attack surface. Remove unused services, reduce exposed APIs, patch dependencies, constrain inputs. Simplicity có bảo mật (security / 보안) giá trị (value / 값) vì fewer states/interactions để reason.

> **Chuyển mạch:** Trong **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Complete mediation** tiếp nhận điểm tựa từ **Minimize attack surface** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Separation of duties** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Complete mediation

Authorization cần check mọi protected truy cập (access / 접근), không chỉ UI đường dẫn (path / 경로). Hiding button không bảo vệ máy chủ (server / 서버) API. bộ nhớ đệm (cache / 캐시) cũng phải preserve authorization ngữ nghĩa (semantics / 의미론); bộ nhớ đệm (cache / 캐시) key thiếu tenant/người dùng (user / 사용자) ngữ cảnh (context / 맥락) có thể leak dữ liệu (data / 데이터).

> **Chuyển mạch:** Ở chặng này của **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Separation of duties** tiếp nhận điểm tựa từ **Complete mediation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo mật (security / 보안) vs usability/hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Separation of duties

Trọng yếu (critical / 중요) hành động (action / 동작) có thể require multiple independent roles/approvals, giảm abuse hoặc single credential compromise. triển khai (deployment / 배포) approval, key management và financial workflows thường áp dụng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Bảo mật (security / 보안) vs usability/hiệu năng (performance / 성능)** tiếp nhận điểm tựa từ **Separation of duties** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo mật (security / 보안) vs usability/hiệu năng (performance / 성능)

Controls có chi phí (cost / 비용). MFA thêm friction; strong KDF tốn CPU; encryption adds overhead; short session expiry increases reauth. Good kỹ thuật (engineering / 엔지니어링) quantify threat/chi phí (cost / 비용) thay vì bỏ bảo mật (security / 보안) hoặc maximize friction.

> **Chuyển mạch:** Trong **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Bảo mật (security / 보안) vs usability/hiệu năng (performance / 성능)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> bảo mật (security / 보안) là **quản lý trust dưới adversarial hành vi (behavior / 동작)**. Bắt đầu từ asset → threat → ranh giới (boundary / 경계) → bất biến (invariant / 불변식) → điều khiển (control / 제어) → residual rủi ro (risk / 위험), không bắt đầu từ danh sách công nghệ.

> **Chuyển mạch:** Ở chặng này của **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Dùng HTTPS là secure.”** TLS bảo channel, không sửa broken authorization, injection hay compromised endpoint.

**“Ở nội bộ (internal / 내부) mạng (network / 네트워크) thì trusted.”** mạng (network / 네트워크) location chỉ là một tín hiệu (signal / 신호); định danh (identity / 식별자)/authorization vẫn cần.

**“bảo mật (security / 보안) là tính năng (feature / 기능) thêm cuối.”** mô hình dữ liệu (data model / 데이터 모델), privilege ranh giới (boundary / 경계) và giao thức (protocol / 프로토콜) thiết kế (design / 설계) quyết định rất nhiều properties từ đầu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Threat mô hình (model / 모델) và bảo mật (security / 보안) principles**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

OS isolation ở [privilege/virtualization](../03_operating_systems/05_privilege_isolation_and_virtualization.md). Cryptographic mechanisms ở [cryptography](./01_cryptography_foundations.md); định danh (identity / 식별자)/truy cập (access / 접근) ở [authentication/authorization](./02_identity_authentication_and_authorization.md); hiện thực (implementation / 구현) failures ở [vulnerabilities](./03_software_vulnerabilities.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
