# Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Security/governance: identity, secrets, policy và software supply chain**. Route đi từ trust boundaries → authentication/authorization → secret lifecycle → policy enforcement → dependency/provenance controls, để security bám vào quyền và đường cung ứng.

## 1. nền tảng (platform / 플랫폼) bảo mật (security / 보안) bắt đầu từ trust ranh giới (boundary / 경계)

Mỗi delivery step có một principal thực hiện hành động (action / 동작): nhà phát triển (developer / 개발자), CI runner, GitOps controller, Kubernetes dịch vụ (service / 서비스) account, cloud tải công việc (workload / 워크로드) định danh (identity / 식별자). Nếu không biết principal nào được quyền làm gì, bảo mật (security / 보안) trở thành tập secret rải rác.

Một mô hình tốt tách định danh (identity / 식별자) của con người và tải công việc (workload / 워크로드), cấp quyền theo role/năng lực (capability / 역량) và ưu tiên credential ngắn hạn. nhật ký kiểm tra (audit log / 감사 로그) phải nối hành động (action / 동작) với định danh (identity / 식별자) thực.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **1. nền tảng (platform / 플랫폼) bảo mật (security / 보안) bắt đầu từ trust ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **2. Authentication khác authorization** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **3. Secret là liability có vòng đời (lifecycle / 생명주기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Authentication khác authorization

Authentication trả lời “ai/what đang gọi”. Authorization trả lời định danh (identity / 식별자) đó được phép làm gì. TLS certificate, OIDC đơn vị từ (token / 토큰) hoặc cloud role có thể chứng minh định danh (identity / 식별자); chính sách (policy / 정책)/RBAC quyết định permission.

PKI và dịch vụ (service / 서비스) định danh (identity / 식별자) được đào sâu ở [canonical PKI, mTLS và service identity](../../computer_science/07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md). DevOps tập trung vào phân phối định danh (identity / 식별자) vào tải công việc (workload / 워크로드) và rotation không downtime.

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **2. Authentication khác authorization** xác định đầu vào; **3. Secret là liability có vòng đời (lifecycle / 생명주기)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. Rotation phải là giao thức (protocol / 프로토콜) tương thích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Secret là liability có vòng đời (lifecycle / 생명주기)

Secret không chỉ là string cần giấu. Nó có creator, bên tiêu thụ (consumer / 소비자), phạm vi (scope / 범위), TTL, rotation và revocation. Static credential sống nhiều năm làm sự cố (incident / 인시던트) khó contain vì không biết bao nhiêu nơi đã bản sao (copy / 복사).

Secret manager/KMS giúp centralize điều khiển (control / 제어) nhưng ứng dụng (application / 애플리케이션) vẫn phải có bootstrap định danh (identity / 식별자) để lấy secret. Đây là “secret zero” bài toán (problem / 문제); tải công việc (workload / 워크로드) định danh (identity / 식별자)/federation thường giảm nhu cầu distribute secret bootstrap dài hạn.

Cơ chế KMS/HSM/envelope encryption xem [canonical secrets và key lifecycle](../../computer_science/07_security_reliability/advanced/06_secrets_kms_hsm_rotation_and_envelope_encryption.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **3. Secret là liability có vòng đời (lifecycle / 생명주기)** xác định đầu vào; **4. Rotation phải là giao thức (protocol / 프로토콜) tương thích** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. chính sách (policy / 정책) as mã (code / 코드) đưa phản hồi (feedback / 피드백) về sớm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Rotation phải là giao thức (protocol / 프로토콜) tương thích

Đổi password/credential ngay lập tức có thể làm dịch vụ (service / 서비스) đang chạy mất truy cập (access / 접근). Rotation an toàn thường có overlap: tạo credential/cert mới, distribute, reload/rollout bên tiêu thụ (consumer / 소비자), verify, rồi revoke old.

Nếu ứng dụng (application / 애플리케이션) chỉ đọc secret khi startup, nền tảng (platform / 플랫폼) phải biết cần restart. Nếu thư viện (library / 라이브러리)/sidecar hot reload được, cần verify liên kết (connection / 연결) mới thực sự dùng credential mới.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **5. chính sách (policy / 정책) as mã (code / 코드) đưa phản hồi (feedback / 피드백) về sớm** tiếp nhận điểm tựa từ **4. Rotation phải là giao thức (protocol / 프로토콜) tương thích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Supply chuỗi (chain / 사슬): nguồn (source / 소스) không phải trust duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. chính sách (policy / 정책) as mã (code / 코드) đưa phản hồi (feedback / 피드백) về sớm

Bảo mật (security / 보안) rà soát (review / 검토) thủ công cho mọi manifest không quy mô (scale / 규모). chính sách (policy / 정책) as mã (code / 코드) encode quy tắc (rule / 규칙) như “môi trường vận hành (production / 운영 환경) tải công việc (workload / 워크로드) không chạy privileged”, “công khai (public / 공개) bucket cần exception”, “ảnh (image / 이미지) phải đến từ registry được tin cậy”.

Chính sách (policy / 정책) có thể chạy ở CI để phản hồi (feedback / 피드백) sớm và ở admission/thời gian chạy (runtime / 런타임) để enforcement. Hai lớp có mục tiêu khác: CI giúp nhà phát triển (developer / 개발자) sửa trước merge; admission bảo vệ môi trường (environment / 환경) trước yêu cầu (request / 요청) cuối cùng.

Chính sách (policy / 정책) cần exception vòng đời (lifecycle / 생명주기). Nếu exception permanent và không đơn vị sở hữu (owner / 오너)/expiry, guardrail dần mất giá trị.

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **5. chính sách (policy / 정책) as mã (code / 코드) đưa phản hồi (feedback / 피드백) về sớm** nêu điều cần giải thích; **6. Supply chuỗi (chain / 사슬): nguồn (source / 소스) không phải trust duy nhất** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. SBOM, provenance và signature giải quyết câu hỏi khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Supply chuỗi (chain / 사슬): nguồn (source / 소스) không phải trust duy nhất

Attack có thể đi qua phụ thuộc (dependency / 의존성), bản dựng (build / 빌드) runner, plugin/hành động (action / 동작), registry hoặc stolen signing key. Vì vậy cần nhìn software supply chuỗi (chain / 사슬) end-to-end:

```text
source → dependency → build environment → artifact → registry → deploy
```

Mỗi arrow cần định danh (identity / 식별자)/integrity bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **6. Supply chuỗi (chain / 사슬): nguồn (source / 소스) không phải trust duy nhất** nêu điều cần giải thích; **7. SBOM, provenance và signature giải quyết câu hỏi khác nhau** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. CI runner là privileged hạ tầng (infrastructure / 인프라)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. SBOM, provenance và signature giải quyết câu hỏi khác nhau

SBOM trả lời sản phẩm tạo ra (artifact / 산출물) chứa thành phần (component / 컴포넌트) nào. Provenance trả lời sản phẩm tạo ra (artifact / 산출물) được bản dựng (build / 빌드) từ nguồn (source / 소스)/tiến trình (process / 프로세스) nào. Signature/attestation giúp verify statement đến từ định danh (identity / 식별자)/key được tin. Không cái nào tự chứng minh software không có vulnerability.

Khi kết hợp, nền tảng (platform / 플랫폼) có thể đặt chính sách (policy / 정책): chỉ deploy sản phẩm tạo ra (artifact / 산출물) từ trusted builder, có provenance hợp lệ, phụ thuộc (dependency / 의존성) scan không vi phạm threshold, signature đúng và ảnh (image / 이미지) digest bất biến.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **8. CI runner là privileged hạ tầng (infrastructure / 인프라)** tiếp nhận điểm tựa từ **7. SBOM, provenance và signature giải quyết câu hỏi khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. bộ chứa (container / 컨테이너)/Kubernetes bảo mật (security / 보안) theo defense in độ sâu (depth / 깊이)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. CI runner là privileged hạ tầng (infrastructure / 인프라)

Runner thường có nguồn (source / 소스) truy cập (access / 접근) và đôi khi publish/deploy permission. Workflow từ pull yêu cầu (request / 요청) chưa tin cậy không nên tự động có môi trường vận hành (production / 운영 환경) credential. Self-hosted runner còn có persistence rủi ro (risk / 위험) nếu job độc hại để lại tiến trình (process / 프로세스)/tệp (file / 파일) cho job sau.

Runner isolation, ephemeral thực thi (execution / 실행) và least-privilege job đơn vị từ (token / 토큰) là môi trường vận hành (production / 운영 환경) bảo mật (security / 보안) concern, không chỉ CI cấu hình (configuration / 구성).

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **9. bộ chứa (container / 컨테이너)/Kubernetes bảo mật (security / 보안) theo defense in độ sâu (depth / 깊이)** tiếp nhận điểm tựa từ **8. CI runner là privileged hạ tầng (infrastructure / 인프라)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. quản trị (governance / 거버넌스) không đồng nghĩa central approval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. bộ chứa (container / 컨테이너)/Kubernetes bảo mật (security / 보안) theo defense in độ sâu (depth / 깊이)

Ảnh (image / 이미지) nên giảm gói (package / 패키지) không cần, chạy non-root khi phù hợp, drop năng lực (capability / 역량), không privileged/mount host socket tùy tiện. Kubernetes thêm RBAC, không gian tên (namespace / 네임스페이스) chính sách (policy / 정책), chính sách mạng (network policy / 네트워크 정책), admission điều khiển (control / 제어) và tải công việc (workload / 워크로드) định danh (identity / 식별자).

Bộ chứa (container / 컨테이너) isolation cơ chế (mechanism / 메커니즘) được giải thích tại [canonical container internals](../../computer_science/03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md). nền tảng (platform / 플랫폼) chapter này chỉ đưa chúng thành secure default.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **10. quản trị (governance / 거버넌스) không đồng nghĩa central approval** tiếp nhận điểm tựa từ **9. bộ chứa (container / 컨테이너)/Kubernetes bảo mật (security / 보안) theo defense in độ sâu (depth / 깊이)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Break-glass truy cập (access / 접근)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. quản trị (governance / 거버넌스) không đồng nghĩa central approval

Quản trị (governance / 거버넌스) tốt làm quy tắc (rule / 규칙) rõ, tự động và observable. Một central nhóm (team / 팀) phải duyệt từng cơ sở dữ liệu (database / 데이터베이스)/không gian tên (namespace / 네임스페이스) làm luồng (flow / 흐름) chậm và khuyến khích bypass. Tốt hơn là nền tảng (platform / 플랫폼) cung cấp SKU/plan đã approved, quota, dữ liệu (data / 데이터) classification trường dữ liệu (field / 필드) và chính sách (policy / 정책) tự động.

Approval thủ công nên dành cho exception/rủi ro (risk / 위험) thật sự cao.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **11. Break-glass truy cập (access / 접근)** tiếp nhận điểm tựa từ **10. quản trị (governance / 거버넌스) không đồng nghĩa central approval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Vulnerability management cần exploitability ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Break-glass truy cập (access / 접근)

Sự cố (incident / 인시던트) đôi khi cần quyền cao tạm thời. Break-glass đường dẫn (path / 경로) nên được thiết kế trước: strong authentication, reason/ticket, time-bound privilege, kiểm tra (audit / 감사) và rà soát (review / 검토) sau sử dụng.

Không có break-glass chính thức thường dẫn tới dùng chung (shared / 공유) admin credential “để phòng khi cần”, rủi ro hơn nhiều.

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **12. Vulnerability management cần exploitability ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **11. Break-glass truy cập (access / 접근)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. cấp cao (senior / 시니어) ghi chú (note / 노트): secure-by-default phải đi cùng usable-by-default** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Vulnerability management cần exploitability ngữ cảnh (context / 맥락)

Không phải CVE severity cao nào cũng có cùng rủi ro (risk / 위험) cho tải công việc (workload / 워크로드). gói (package / 패키지) có thể không được tải (load / 로드), đường dẫn (path / 경로) không reachable hoặc điều khiển (control / 제어) khác giảm exploitability. Ngược lại, vulnerability medium ở Internet-facing auth thành phần (component / 컴포넌트) có thể quan trọng.

Nền tảng (platform / 플랫폼) nên ưu tiên theo asset exposure, exploitability, thời gian chạy (runtime / 런타임) ngữ cảnh (context / 맥락) và nghiệp vụ (business / 비즈니스) criticality, đồng thời vẫn giữ SLA remediation theo chính sách (policy / 정책).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **13. cấp cao (senior / 시니어) ghi chú (note / 노트): secure-by-default phải đi cùng usable-by-default** tiếp nhận điểm tựa từ **12. Vulnerability management cần exploitability ngữ cảnh (context / 맥락)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Threat mô hình (model / 모델) delivery hệ thống (system / 시스템) theo năng lực (capability / 역량) chiếm được** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. cấp cao (senior / 시니어) ghi chú (note / 노트): secure-by-default phải đi cùng usable-by-default

Nếu bảo mật (security / 보안) điều khiển (control / 제어) quá khó dùng, nhóm (team / 팀) tìm đường vòng. nền tảng (platform / 플랫폼) tốt làm secure đường dẫn (path / 경로) nhanh hơn insecure DIY: định danh (identity / 식별자) tự cấp theo tải công việc (workload / 워크로드), secret injection chuẩn, signed sản phẩm tạo ra (artifact / 산출물) tự động, chính sách (policy / 정책) phản hồi (feedback / 피드백) ngay PR.

Bảo mật (security / 보안) và nhà phát triển (developer / 개발자) experience không đối lập; guardrail tốt biến bảo mật (security / 보안) thành thuộc tính (property / 속성) của nền tảng (platform / 플랫폼).

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **14. Threat mô hình (model / 모델) delivery hệ thống (system / 시스템) theo năng lực (capability / 역량) chiếm được** tiếp nhận điểm tựa từ **13. cấp cao (senior / 시니어) ghi chú (note / 노트): secure-by-default phải đi cùng usable-by-default** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. tải công việc (workload / 워크로드) định danh (identity / 식별자) giảm secret phân phối (distribution / 분포) nhưng không xóa authorization bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Threat mô hình (model / 모델) delivery hệ thống (system / 시스템) theo năng lực (capability / 역량) chiếm được

Threat modeling không cần bắt đầu bằng danh sách hàng trăm attack. Với nền tảng (platform / 플랫폼), hãy hỏi nếu một principal hoặc thành phần (component / 컴포넌트) bị compromise thì attacker có thể thay trạng thái (state / 상태) nào.

Nếu nhà phát triển (developer / 개발자) account bị chiếm, attacker có thể merge mã (code / 코드) trực tiếp hay vẫn cần reviewer khác? Nếu CI runner bị chiếm, nó chỉ hiện vật bản dựng (build artifact / 빌드 산출물) hay có thể deploy môi trường vận hành (production / 운영 환경)? Nếu registry đơn vị từ (token / 토큰) lộ, attacker có thể overwrite mutable tag hay sản phẩm tạo ra (artifact / 산출물) được pin digest/signature? Nếu GitOps bot đơn vị từ (token / 토큰) lộ, phạm vi (scope / 범위) là một repo hay toàn organization?

Cách hỏi theo năng lực (capability / 역량) làm blast radius rõ hơn và dẫn tới điều khiển (control / 제어) cụ thể: separation of duties, short-lived đơn vị từ (token / 토큰), environment-scoped role, immutable sản phẩm tạo ra (artifact / 산출물), approval cho high-risk đường dẫn (path / 경로) và kiểm tra (audit / 감사).

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **15. tải công việc (workload / 워크로드) định danh (identity / 식별자) giảm secret phân phối (distribution / 분포) nhưng không xóa authorization bài toán (problem / 문제)** tiếp nhận điểm tựa từ **14. Threat mô hình (model / 모델) delivery hệ thống (system / 시스템) theo năng lực (capability / 역량) chiếm được** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Provenance/signature chỉ mạnh bằng trust chính sách (policy / 정책) của verifier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. tải công việc (workload / 워크로드) định danh (identity / 식별자) giảm secret phân phối (distribution / 분포) nhưng không xóa authorization bài toán (problem / 문제)

Federation/tải công việc (workload / 워크로드) định danh (identity / 식별자) cho phép tải công việc (workload / 워크로드) chứng minh định danh (identity / 식별자) bằng credential ngắn hạn do thời gian chạy (runtime / 런타임)/điều khiển (control / 제어) plane cấp, rồi exchange/assume role để gọi cloud/dịch vụ (service / 서비스) khác. Lợi ích lớn là không cần bake static key vào ảnh (image / 이미지) hoặc Git.

Nhưng nếu dịch vụ (service / 서비스) account có quyền quá rộng, credential ngắn hạn vẫn nguy hiểm trong thời gian hiệu lực. Vì vậy định danh (identity / 식별자) vòng đời (lifecycle / 생명주기) và authorization phạm vi (scope / 범위) phải đi cùng nhau. Audience, subject, role binding và môi trường (environment / 환경) ranh giới (boundary / 경계) cần đủ chặt để đơn vị từ (token / 토큰) của tải công việc (workload / 워크로드) A không được chấp nhận như tải công việc (workload / 워크로드) B.

Mô hình tư duy (mental model / 사고 모델) là: **bootstrap định danh (identity / 식별자) → đơn vị từ (token / 토큰) ngắn hạn → chính sách (policy / 정책) quyết định năng lực (capability / 역량)**. Không nên dừng ở “không còn secret tệp (file / 파일) nên đã secure”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **16. Provenance/signature chỉ mạnh bằng trust chính sách (policy / 정책) của verifier** tiếp nhận điểm tựa từ **15. tải công việc (workload / 워크로드) định danh (identity / 식별자) giảm secret phân phối (distribution / 분포) nhưng không xóa authorization bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. chính sách (policy / 정책) rollout cũng có thể gây outage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Provenance/signature chỉ mạnh bằng trust chính sách (policy / 정책) của verifier

Một sản phẩm tạo ra (artifact / 산출물) có signature nhưng verifier chấp nhận bất kỳ key nào thì signature không tạo trust hữu ích. Một provenance statement ghi builder định danh (identity / 식별자) nhưng chính sách (policy / 정책) không phân biệt trusted builder với laptop cá nhân cũng tương tự.

Verifier cần chính sách (policy / 정책) rõ: sản phẩm tạo ra (artifact / 산출물) digest nào là subject; statement kiểu (type / 타입) nào được chấp nhận; builder/nguồn (source / 소스) định danh (identity / 식별자) nào thuộc trust lĩnh vực (domain / 도메인); chính sách (policy / 정책) nào bắt buộc cho môi trường vận hành (production / 운영 환경); revocation hoặc compromised định danh (identity / 식별자) được xử lý ra sao.

Đây là lý do supply-chain bảo mật (security / 보안) nên được xem như **authorization trên bằng chứng (evidence / 증거)**, không phải checkbox “đã ký ảnh (image / 이미지)”.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **17. chính sách (policy / 정책) rollout cũng có thể gây outage** tiếp nhận điểm tựa từ **16. Provenance/signature chỉ mạnh bằng trust chính sách (policy / 정책) của verifier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Secret exfiltration phản hồi (response / 응답) khác secret rotation bình thường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. chính sách (policy / 정책) rollout cũng có thể gây outage

Admission/chính sách (policy / 정책) engine nằm trên trọng yếu (critical / 중요) điều khiển (control / 제어) đường dẫn (path / 경로). Một quy tắc (rule / 규칙) sai có thể chặn toàn bộ deploy; webhook chậm có thể tăng API độ trễ (latency / 지연 시간); chính sách (policy / 정책) thay đổi toàn cục (global / 전역) có blast radius lớn hơn một ứng dụng (application / 애플리케이션) bản phát hành (release / 릴리스).

Chính sách (policy / 정책) nên có kiểm thử (test / 테스트) fixture, dry-run/kiểm tra (audit / 감사) chế độ (mode / 모드) khi phù hợp, staged rollout và khả năng quan sát (observability / 관측 가능성) về denial/độ trễ (latency / 지연 시간). Exception cũng phải versioned và có expiry. nền tảng (platform / 플랫폼) bảo mật (security / 보안) điều khiển (control / 제어) là môi trường vận hành (production / 운영 환경) software nên cần cùng discipline canary/quay lui (rollback / 롤백) như ứng dụng (application / 애플리케이션).

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **18. Secret exfiltration phản hồi (response / 응답) khác secret rotation bình thường** tiếp nhận điểm tựa từ **17. chính sách (policy / 정책) rollout cũng có thể gây outage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Supply-chain phụ thuộc (dependency / 의존성) cần phân biệt nguồn (source / 소스), gói (package / 패키지) và thực thi (execution / 실행) trust** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Secret exfiltration phản hồi (response / 응답) khác secret rotation bình thường

Rotation định kỳ giả định old credential chưa chắc bị attacker giữ. Khi có bằng chứng exfiltration, cần containment nhanh hơn: xác định phạm vi (scope / 범위), revoke/disable credential cũ, tìm nơi credential đã được dùng, rotate dependent secret/key nếu trust chuỗi (chain / 사슬) bị ảnh hưởng và kiểm tra nhật ký kiểm tra (audit log / 감사 로그) cho misuse.

Nếu cùng một static secret được share cho 20 dịch vụ (service / 서비스), blast radius và forensic khó hơn nhiều. Đây là lợi ích thực tế của per-workload định danh (identity / 식별자) và short-lived credential: containment ranh giới (boundary / 경계) nhỏ hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **18. Secret exfiltration phản hồi (response / 응답) khác secret rotation bình thường** nêu điều cần giải thích; **19. Supply-chain phụ thuộc (dependency / 의존성) cần phân biệt nguồn (source / 소스), gói (package / 패키지) và thực thi (execution / 실행) trust** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. cấp cao (senior / 시니어) walkthrough: pull yêu cầu (request / 요청) từ fork chạm bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Supply-chain phụ thuộc (dependency / 의존성) cần phân biệt nguồn (source / 소스), gói (package / 패키지) và thực thi (execution / 실행) trust

Một phụ thuộc (dependency / 의존성) có thể đến từ nguồn (source / 소스) repository, gói (package / 패키지) registry hoặc nhị phân (binary / 이진)/công cụ (tool / 도구) download. Pin phiên bản (version / 버전) giúp reproducibility nhưng không tự chứng minh gói (package / 패키지) đó là sản phẩm tạo ra (artifact / 산출물) mong muốn. Checksum/signature/provenance có thể bổ sung integrity, còn sandbox/least privilege giảm impact nếu phụ thuộc (dependency / 의존성) thực thi bản dựng (build / 빌드) script độc hại.

Đặc biệt trong CI, trình quản lý gói (package manager / 패키지 관리자) hook, bản dựng (build / 빌드) plugin và third-party hành động (action / 동작) có thể thực thi mã (code / 코드) với credential job. Vì vậy phụ thuộc (dependency / 의존성) rà soát (review / 검토) không chỉ nhìn thời gian chạy (runtime / 런타임) thư viện (library / 라이브러리); build-time phụ thuộc (dependency / 의존성) cũng nằm trong attack surface.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **19. Supply-chain phụ thuộc (dependency / 의존성) cần phân biệt nguồn (source / 소스), gói (package / 패키지) và thực thi (execution / 실행) trust** nêu điều cần giải thích; **20. cấp cao (senior / 시니어) walkthrough: pull yêu cầu (request / 요청) từ fork chạm bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. Confused deputy: principal hợp lệ vẫn có thể làm việc không nên làm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. cấp cao (senior / 시니어) walkthrough: pull yêu cầu (request / 요청) từ fork chạm bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인)

Giả sử repo công khai (public / 공개) nhận PR từ fork. Workflow chạy kiểm thử (test / 테스트) trên mã (code / 코드) chưa tin cậy. Nếu job này có registry ghi (write / 쓰기) đơn vị từ (token / 토큰) hoặc cloud deploy role, contributor có thể sửa kiểm thử (test / 테스트)/bản dựng (build / 빌드) script để exfiltrate đơn vị từ (token / 토큰).

Ranh giới (boundary / 경계) an toàn hơn là tách untrusted xác minh (verification / 확인) khỏi trusted bản phát hành (release / 릴리스). PR job dùng permission tối thiểu, không nhận môi trường vận hành (production / 운영 환경) secret; sau merge vào protected branch, trusted workflow checkout chính xác (exact / 정확한) revision và bản dựng (build / 빌드)/publish bằng định danh (identity / 식별자) riêng. sản phẩm tạo ra (artifact / 산출물) promotion sau đó dựa trên digest/provenance thay vì tin đầu ra (output / 출력) từ untrusted job.

Điểm cốt lõi không phụ thuộc GitHub Actions/Jenkins/GitLab CI: **mã (code / 코드) chưa được trust không được tự động nhận năng lực (capability / 역량) của môi trường vận hành (production / 운영 환경) trust lĩnh vực (domain / 도메인)**.

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **20. cấp cao (senior / 시니어) walkthrough: pull yêu cầu (request / 요청) từ fork chạm bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **21. Confused deputy: principal hợp lệ vẫn có thể làm việc không nên làm** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **22. định danh (identity / 식별자) propagation cần tránh biến dịch vụ (service / 서비스) trung gian thành superuser mù ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Confused deputy: principal hợp lệ vẫn có thể làm việc không nên làm

Một dịch vụ (service / 서비스) trung gian có quyền mạnh có thể bị người dùng (user / 사용자) ít quyền lợi dụng để thực hiện hành động (action / 동작) thay họ. Đây là confused-deputy bài toán (problem / 문제). Ví dụ nền tảng (platform / 플랫폼) provisioner có quyền tạo cơ sở dữ liệu (database / 데이터베이스) ở nhiều account; nếu API chỉ nhận `accountId` từ yêu cầu (request / 요청) mà không kiểm tra caller được phép mục tiêu (target / 대상) account nào, người dùng (user / 사용자) có thể khiến provisioner dùng authority hợp lệ cho mục tiêu không hợp lệ.

Authentication của caller và authentication của provisioner đều có thể đúng, nhưng authorization chuỗi (chain / 사슬) vẫn sai. nền tảng (platform / 플랫폼) phải bind **yêu cầu (request / 요청) intent → caller định danh (identity / 식별자) → allowed mục tiêu (target / 대상)/năng lực (capability / 역량)** trước khi dùng automation định danh (identity / 식별자) mạnh hơn.

Do đó nhật ký kiểm tra (audit log / 감사 로그) nên giữ cả actor gốc và thực thi (execution / 실행) định danh (identity / 식별자). Nếu log chỉ thấy `platform-controller` tạo tài nguyên (resource / 자원), forensic không trả lời ai đã yêu cầu và chính sách (policy / 정책) nào cho phép.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **22. định danh (identity / 식별자) propagation cần tránh biến dịch vụ (service / 서비스) trung gian thành superuser mù ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **21. Confused deputy: principal hợp lệ vẫn có thể làm việc không nên làm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. TOCTOU: chính sách (policy / 정책) check đúng ở thời điểm A có thể sai ở thời điểm B** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. định danh (identity / 식별자) propagation cần tránh biến dịch vụ (service / 서비스) trung gian thành superuser mù ngữ cảnh (context / 맥락)

Trong một yêu cầu (request / 요청) xuyên nhiều dịch vụ (service / 서비스), downstream cần biết authority nào thật sự được chuyển tiếp. Có ba mẫu (pattern / 패턴) khác nhau: dịch vụ (service / 서비스) gọi bằng định danh (identity / 식별자) riêng; dịch vụ (service / 서비스) impersonate/delegate một phần định danh (identity / 식별자) người dùng (user / 사용자); hoặc dịch vụ (service / 서비스) trao đổi đơn vị từ (token / 토큰) thành năng lực (capability / 역량) hẹp hơn.

Không nên forward nguyên đơn vị từ (token / 토큰) quyền rộng qua mọi hop chỉ vì tiện. Mỗi hop cần audience đúng, TTL ngắn và phạm vi (scope / 범위) tối thiểu. Downstream cũng không nên tin một header như `X-User` chỉ vì nó đến từ nội bộ (internal / 내부) mạng (network / 네트워크) nếu ingress/dịch vụ (service / 서비스) trước đó có thể bị compromise.

Mô hình tư duy (mental model / 사고 모델) là **định danh (identity / 식별자) propagation không bằng authority propagation**. Biết yêu cầu (request / 요청) bắt nguồn từ người dùng (user / 사용자) A không tự động nghĩa dịch vụ (service / 서비스) B được phép làm mọi thứ A làm, và ngược lại dịch vụ (service / 서비스) B có quyền riêng cũng không được dùng quyền đó thay A nếu chính sách (policy / 정책) không cho phép.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **23. TOCTOU: chính sách (policy / 정책) check đúng ở thời điểm A có thể sai ở thời điểm B** tiếp nhận điểm tựa từ **22. định danh (identity / 식별자) propagation cần tránh biến dịch vụ (service / 서비스) trung gian thành superuser mù ngữ cảnh (context / 맥락)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Revocation không tức thời nếu verifier/bộ nhớ đệm (cache / 캐시)/session còn trạng thái (state / 상태) cũ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. TOCTOU: chính sách (policy / 정책) check đúng ở thời điểm A có thể sai ở thời điểm B

Time-of-check to time-of-use xuất hiện khi hệ thống kiểm tra chính sách (policy / 정책)/trạng thái (state / 상태) rồi hành động (action / 동작) xảy ra sau đó trên trạng thái (state / 상태) đã thay đổi. Ví dụ chuỗi xử lý (pipeline / 파이프라인) verify sản phẩm tạo ra (artifact / 산출물) digest/signature lúc approve, nhưng deploy step sau lại resolve mutable tag; hoặc nền tảng (platform / 플랫폼) check quota rồi async provision nhiều phút sau trong khi sức chứa (capacity / 용량)/quyền sở hữu (ownership / 소유권) đã đổi.

Cách giảm race là bind quyết định (decision / 결정) với immutable định danh (identity / 식별자)/phiên bản (version / 버전): sản phẩm tạo ra (artifact / 산출물) digest, generation/tài nguyên (resource / 자원) phiên bản (version / 버전), chính sách (policy / 정책) revision, yêu cầu (request / 요청) id và mục tiêu (target / 대상) định danh (identity / 식별자). Với hành động (action / 동작) dài, controller có thể cần revalidate bất biến (invariant / 불변식) trước bước irreversible thay vì tin check ban đầu mãi mãi.

Bảo mật (security / 보안) chính sách (policy / 정책) vì vậy không chỉ là “đã check hay chưa” mà còn là **check cái gì, ở revision nào, và hành động (action / 동작) sử dụng đúng đối tượng (object / 객체) đã được check hay không**.

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **24. Revocation không tức thời nếu verifier/bộ nhớ đệm (cache / 캐시)/session còn trạng thái (state / 상태) cũ** tiếp nhận điểm tựa từ **23. TOCTOU: chính sách (policy / 정책) check đúng ở thời điểm A có thể sai ở thời điểm B** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. ranh giới bảo mật (security boundary / 보안 경계) cần xét control-plane compromise và data-plane compromise khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Revocation không tức thời nếu verifier/bộ nhớ đệm (cache / 캐시)/session còn trạng thái (state / 상태) cũ

Credential ngắn hạn giảm cửa sổ rủi ro nhưng revoke một định danh (identity / 식별자) không bảo đảm mọi liên kết (connection / 연결)/đơn vị từ (token / 토큰) hiện hữu biến mất ngay. JWT self-contained có thể còn hợp lệ tới expiry; TLS liên kết (connection / 연결) đã establish có thể sống lâu; authorization bộ nhớ đệm (cache / 캐시) có TTL; cloud điều khiển (control / 제어) plane có propagation delay.

Sự cố (incident / 인시던트) phản hồi (response / 응답) phải biết revocation ngữ nghĩa (semantics / 의미론) thực tế của từng tầng (layer / 계층). Nếu cần containment nhanh, có thể phải vừa revoke role/key, vừa chặn mạng (network / 네트워크)/session, rotate downstream credential hoặc restart connection-owning tải công việc (workload / 워크로드) tùy threat mô hình (model / 모델).

Đây là lý do TTL, bộ nhớ đệm (cache / 캐시) duration và liên kết (connection / 연결) thời gian tồn tại (lifetime / 수명) là bảo mật (security / 보안) parameter, không chỉ hiệu năng (performance / 성능) parameter.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **24. Revocation không tức thời nếu verifier/bộ nhớ đệm (cache / 캐시)/session còn trạng thái (state / 상태) cũ** đã nêu tiêu chí phân biệt, còn **25. ranh giới bảo mật (security boundary / 보안 경계) cần xét control-plane compromise và data-plane compromise khác nhau** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **26. bảo mật (security / 보안) bằng chứng (evidence / 증거) phải chứng minh bất biến (invariant / 불변식), không chỉ chứng minh công cụ (tool / 도구) đã chạy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. ranh giới bảo mật (security boundary / 보안 경계) cần xét control-plane compromise và data-plane compromise khác nhau

Nếu ứng dụng (application / 애플리케이션) pod bị compromise, attacker có thể lấy tải công việc (workload / 워크로드) đơn vị từ (token / 토큰), gọi phụ thuộc (dependency / 의존성) trong phạm vi (scope / 범위) và đọc dữ liệu (data / 데이터) tiến trình (process / 프로세스) đang thấy. Nếu GitOps/controller/CI bản phát hành (release / 릴리스) định danh (identity / 식별자) bị compromise, attacker có thể thay desired trạng thái (state / 상태) của hàng trăm tải công việc (workload / 워크로드) — blast radius khác hẳn.

Control-plane principal thường cần permission rộng để tự động hóa, nên phải được cô lập, monitor và chia phạm vi (scope / 범위) mạnh hơn: per-environment định danh (identity / 식별자), protected branch, separate signer/builder role, bounded controller permission và high-signal kiểm tra (audit / 감사).

Một thiết kế (design / 설계) “mọi automation dùng chung admin role cho tiện” biến compromise nhỏ thành organizational blast radius. Least privilege có giá trị nhất ở các principal có fan-out lớn.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **25. ranh giới bảo mật (security boundary / 보안 경계) cần xét control-plane compromise và data-plane compromise khác nhau** đã nêu tiêu chí phân biệt, còn **26. bảo mật (security / 보안) bằng chứng (evidence / 증거) phải chứng minh bất biến (invariant / 불변식), không chỉ chứng minh công cụ (tool / 도구) đã chạy** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **27. Rotation chỉ hoàn tất khi chứng minh bên tiêu thụ (consumer / 소비자) đã chuyển sang credential mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. bảo mật (security / 보안) bằng chứng (evidence / 증거) phải chứng minh bất biến (invariant / 불변식), không chỉ chứng minh công cụ (tool / 도구) đã chạy

Scan job xanh không chứng minh sản phẩm tạo ra (artifact / 산출물) môi trường vận hành (production / 운영 환경) chính là sản phẩm tạo ra (artifact / 산출물) đã scan. chính sách (policy / 정책) kiểm thử (test / 테스트) pass không chứng minh môi trường vận hành (production / 운영 환경) admission đang chạy đúng revision. Secret manager tồn tại không chứng minh tải công việc (workload / 워크로드) không còn secret hard-coded.

Bằng chứng (evidence / 증거) chuỗi (chain / 사슬) tốt nối đối tượng (object / 객체) cụ thể: nguồn (source / 소스) revision → bản dựng (build / 빌드) provenance → sản phẩm tạo ra (artifact / 산출물) digest → signature/attestation → triển khai (deployment / 배포) digest → thời gian chạy (runtime / 런타임) định danh (identity / 식별자) → authorization quyết định (decision / 결정). Mỗi bước có thể hỏi “bằng chứng (evidence / 증거) này bound vào subject nào?”.

Khi kiểm tra (audit / 감사)/bảo mật (security / 보안) rà soát (review / 검토) chỉ thu screenshot dashboard hoặc tên sản phẩm mà không bind được tới sản phẩm tạo ra (artifact / 산출물)/tải công việc (workload / 워크로드)/định danh (identity / 식별자) cụ thể, điều khiển (control / 제어) có thể chỉ tồn tại trên giấy. nền tảng (platform / 플랫폼) bảo mật (security / 보안) trưởng thành ưu tiên **verifiable linkage** hơn số lượng bảo mật (security / 보안) công cụ (tool / 도구).

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **26. bảo mật (security / 보안) bằng chứng (evidence / 증거) phải chứng minh bất biến (invariant / 불변식), không chỉ chứng minh công cụ (tool / 도구) đã chạy** nêu điều cần giải thích; **27. Rotation chỉ hoàn tất khi chứng minh bên tiêu thụ (consumer / 소비자) đã chuyển sang credential mới** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **28. Break-glass là một privileged session có vòng đời (lifecycle / 생명주기), không phải một account đặc biệt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Rotation chỉ hoàn tất khi chứng minh bên tiêu thụ (consumer / 소비자) đã chuyển sang credential mới

Có secret mới trong manager và tải công việc (workload / 워크로드) đã restart chưa đủ. bên tiêu thụ (consumer / 소비자) có thể giữ liên kết (connection / 연결) pool cũ, tiến trình (process / 프로세스) khác chưa reload hoặc background worker ít traffic vẫn dùng credential cũ. Nếu revoke old quá sớm, thất bại (failure / 실패) chỉ xuất hiện muộn ở cohort chưa chuyển.

Rotation giao thức (protocol / 프로토콜) tốt cần bằng chứng (evidence / 증거): phiên bản (version / 버전) mới đã được phân phối, liên kết (connection / 연결)/session mới đang dùng credential mới, bên tiêu thụ (consumer / 소비자) inventory không còn tham chiếu (reference / 참조) cũ và old-credential usage giảm về zero trong một khoảng phù hợp. Sau đó revoke mới biến overlap thành cutover có kiểm soát.

Với certificate hoặc key, dual-trust cửa sổ (window / 윈도우) cũng cần giới hạn. Overlap quá dài làm hai credential cùng hợp lệ và kéo dài blast radius. Rotation là di chuyển (migration / 마이그레이션) có deadline, không phải trạng thái “giữ cả cũ lẫn mới cho chắc”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **27. Rotation chỉ hoàn tất khi chứng minh bên tiêu thụ (consumer / 소비자) đã chuyển sang credential mới** xác định đầu vào; **28. Break-glass là một privileged session có vòng đời (lifecycle / 생명주기), không phải một account đặc biệt** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **29. kiểm tra (audit / 감사) chế độ (mode / 모드) và enforce chế độ (mode / 모드) là hai phase khác nhau của chính sách (policy / 정책) rollout** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Break-glass là một privileged session có vòng đời (lifecycle / 생명주기), không phải một account đặc biệt

Một tài khoản admin cố định dùng hàng ngày rồi gọi là break-glass đã mất ý nghĩa. Quyền khẩn cấp nên được cấp theo session/yêu cầu (request / 요청) cụ thể, có TTL, mục tiêu (target / 대상) phạm vi (scope / 범위), reason và ideally approval/elevation độc lập với normal role.

Sau khi sự cố (incident / 인시던트) kết thúc, truy cập (access / 접근) phải tự expire hoặc bị revoke, active session/đơn vị từ (token / 토큰) cần được kiểm tra, hành động (action / 동작) quan trọng được rà soát (review / 검토) và credential/bootstrap đường dẫn (path / 경로) phải rotate nếu exposure rủi ro (risk / 위험) thay đổi. “Ticket đã đóng” không chứng minh quyền cao đã biến mất.

Break-glass đường dẫn (path / 경로) cũng phải được kiểm thử (test / 테스트). Nếu đến sự cố (incident / 인시던트) mới phát hiện MFA thiết bị (device / 장치), khôi phục (recovery / 복구) mã (code / 코드) hoặc định danh (identity / 식별자) provider phụ thuộc chính hệ thống đang outage, emergency truy cập (access / 접근) chỉ tồn tại trên tài liệu.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **28. Break-glass là một privileged session có vòng đời (lifecycle / 생명주기), không phải một account đặc biệt** xác định đầu vào; **29. kiểm tra (audit / 감사) chế độ (mode / 모드) và enforce chế độ (mode / 모드) là hai phase khác nhau của chính sách (policy / 정책) rollout** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **30. Fail-open hay fail-closed là reliability-security sự đánh đổi (trade-off / 트레이드오프) phải quyết định trước outage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. kiểm tra (audit / 감사) chế độ (mode / 모드) và enforce chế độ (mode / 모드) là hai phase khác nhau của chính sách (policy / 정책) rollout

Một chính sách (policy / 정책) mới có thể chạy ở kiểm tra (audit / 감사)/shadow chế độ (mode / 모드) để đo bao nhiêu tải công việc (workload / 워크로드) sẽ bị deny, false positive nằm ở đâu và exception nào cần thiết. Khi bằng chứng (evidence / 증거) đủ, chính sách (policy / 정책) mới chuyển sang enforce theo bản phát hành (release / 릴리스) ring hoặc môi trường (environment / 환경).

Nhưng shadow chế độ (mode / 모드) không được kéo dài vô hạn. Nếu quy tắc (rule / 규칙) chỉ log suốt nhiều tháng mà không đơn vị sở hữu (owner / 오너) hoặc deadline, organization có cảm giác “đã có chính sách (policy / 정책)” nhưng bất biến (invariant / 불변식) chưa được bảo vệ.

Rollout mature là: define bất biến (invariant / 불변식) → kiểm thử (test / 테스트) fixture → kiểm tra (audit / 감사) impact → fix/exception → staged enforce → monitor deny/độ trễ (latency / 지연 시간) → remove temporary tính tương thích (compatibility / 호환성). Policy-as-code cũng cần di chuyển (migration / 마이그레이션) vòng đời (lifecycle / 생명주기) giống API.

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **30. Fail-open hay fail-closed là reliability-security sự đánh đổi (trade-off / 트레이드오프) phải quyết định trước outage** tiếp nhận điểm tựa từ **29. kiểm tra (audit / 감사) chế độ (mode / 모드) và enforce chế độ (mode / 모드) là hai phase khác nhau của chính sách (policy / 정책) rollout** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. định danh (identity / 식별자) vòng đời (lifecycle / 생명주기) phải bao gồm offboarding và stale principal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Fail-open hay fail-closed là reliability-security sự đánh đổi (trade-off / 트레이드오프) phải quyết định trước outage

Nếu admission/chính sách (policy / 정책) dịch vụ (service / 서비스) không reachable, chặn mọi deploy giữ bảo mật (security / 보안) bất biến (invariant / 불변식) nhưng có thể ngăn emergency khôi phục (recovery / 복구). Cho phép mọi yêu cầu (request / 요청) tiếp tục giữ availability của điều khiển (control / 제어) đường dẫn (path / 경로) nhưng mở cửa bypass chính sách (policy / 정책).

Không có lựa chọn universal. trọng yếu (critical / 중요) bất biến (invariant / 불변식) như “sản phẩm tạo ra (artifact / 산출물) phải từ trusted registry” có thể fail-closed; low-risk siêu dữ liệu (metadata / 메타데이터) kiểm tra hợp lệ (validation / 검증) có thể fail-open có kiểm tra (audit / 감사) tùy threat mô hình (model / 모델). Quan trọng là hành vi (behavior / 동작) khi phụ thuộc (dependency / 의존성) chính sách (policy / 정책) hỏng phải tường minh (explicit / 명시적), observable và được game-day kiểm thử (test / 테스트).

Nếu operator chỉ biết ngữ nghĩa (semantics / 의미론) này sau khi webhook outage xảy ra, chính sách (policy / 정책) hệ thống (system / 시스템) đang giấu một dạng thất bại (failure mode / 실패 모드) quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **30. Fail-open hay fail-closed là reliability-security sự đánh đổi (trade-off / 트레이드오프) phải quyết định trước outage** xác định đầu vào; **31. định danh (identity / 식별자) vòng đời (lifecycle / 생명주기) phải bao gồm offboarding và stale principal** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **32. Least privilege cần thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) nhưng không được học mù từ traffic hiện tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. định danh (identity / 식별자) vòng đời (lifecycle / 생명주기) phải bao gồm offboarding và stale principal

Least privilege lúc cấp quyền chưa đủ nếu principal không được dọn khi dịch vụ (service / 서비스)/nhóm (team / 팀)/người dùng biến mất. dịch vụ (service / 서비스) account cũ, bot đơn vị từ (token / 토큰) không đơn vị sở hữu (owner / 오너), role dành cho dự án (project / 프로젝트) đã archive tạo attack surface khó nhìn vì không còn traffic bình thường để lộ chúng.

Nền tảng (platform / 플랫폼) nên có inventory principal → đơn vị sở hữu (owner / 오너) → purpose → last-used → phạm vi (scope / 범위) → expiry/rà soát (review / 검토). Unused permission hoặc principal lâu không dùng là tín hiệu (signal / 신호) để thu hẹp, nhưng removal vẫn cần kiểm tra phụ thuộc (dependency / 의존성) batch/DR hiếm khi chạy.

Offboarding là reconciliation bài toán (problem / 문제): source-of-truth về quyền sở hữu (ownership / 소유권) thay đổi thì credential, role binding, repository truy cập (access / 접근) và break-glass membership liên quan phải hội tụ theo.

> **Chuyển mạch:** Trong **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, cơ chế trong **31. định danh (identity / 식별자) vòng đời (lifecycle / 생명주기) phải bao gồm offboarding và stale principal** cần được kiểm chứng bằng dấu vết cụ thể; **32. Least privilege cần thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) nhưng không được học mù từ traffic hiện tại** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **33. nhật ký kiểm tra (audit log / 감사 로그) cũng là bảo mật (security / 보안) asset cần integrity và retention ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Least privilege cần thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) nhưng không được học mù từ traffic hiện tại

Quan sát permission thực sự được dùng giúp phát hiện wildcard hoặc quyền thừa. Tuy nhiên “30 ngày không gọi hành động (action / 동작) X” không chứng minh hành động (action / 동작) X vô dụng nếu nó chỉ cần cho quarterly restore, certificate rotation hoặc disaster khôi phục (recovery / 복구).

Permission reduction nên kết hợp observed usage với declared năng lực (capability / 역량)/runbook và rare-path kiểm thử (test / 테스트). Mục tiêu là giảm quyền tới tập cần thiết cho cả normal đường dẫn (path / 경로) lẫn khôi phục (recovery / 복구) đường dẫn (path / 경로), không tối ưu chính sách (policy / 정책) theo traffic mẫu (sample / 표본) ngắn.

Đây là cùng bài toán khả năng quan sát (observability / 관측 가능성): absence of use chỉ có ý nghĩa khi detector/cửa sổ (window / 윈도우) bao phủ hành vi (behavior / 동작) cần bảo vệ.

> **Chuyển mạch:** Ở chặng này của **Bảo mật (security / 보안) và quản trị (governance / 거버넌스): định danh (identity / 식별자), secrets, chính sách (policy / 정책) và software supply chuỗi (chain / 사슬)**, **32. Least privilege cần thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) nhưng không được học mù từ traffic hiện tại** đã nêu tiêu chí phân biệt, còn **33. nhật ký kiểm tra (audit log / 감사 로그) cũng là bảo mật (security / 보안) asset cần integrity và retention ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 33. nhật ký kiểm tra (audit log / 감사 로그) cũng là bảo mật (security / 보안) asset cần integrity và retention ranh giới (boundary / 경계)

Nhật ký kiểm tra (audit log / 감사 로그) hữu ích chỉ khi attacker hoặc principal bị điều tra không dễ sửa/xóa chính bằng chứng (evidence / 증거) của mình. Nếu CI admin có thể vừa deploy vừa xóa kiểm tra (audit / 감사) bản ghi (record / 레코드) cùng account, forensic trust bị yếu.

High-value kiểm tra (audit / 감사) trail nên có ghi (write / 쓰기)/read/delete permission tách biệt phù hợp, retention/immutability theo threat mô hình (model / 모델), clock/nguồn (source / 소스) định danh (identity / 식별자) rõ và export sang ranh giới (boundary / 경계) khó bị cùng compromise. Không phải mọi ứng dụng (application / 애플리케이션) log cần WORM, nhưng privileged control-plane hành động (action / 동작) cần bằng chứng (evidence / 증거) mạnh hơn gỡ lỗi (debug / 디버그) log thông thường.

Bảo mật (security / 보안) điều khiển (control / 제어) cuối cùng vẫn cần khả năng chứng minh: **ai đã làm gì, lên subject nào, bằng authority nào, chính sách (policy / 정책) revision nào và bằng chứng (evidence / 증거) đó còn đáng tin không**.

> **Bàn giao:** Sau **33. nhật ký kiểm tra (audit log / 감사 로그) cũng là bảo mật (security / 보안) asset cần integrity và retention ranh giới (boundary / 경계)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
