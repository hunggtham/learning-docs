# Security và governance: identity, secrets, policy và software supply chain

## 1. Platform security bắt đầu từ trust boundary

Mỗi delivery step có một principal thực hiện action: developer, CI runner, GitOps controller, Kubernetes service account, cloud workload identity. Nếu không biết principal nào được quyền làm gì, security trở thành tập secret rải rác.

Một mô hình tốt tách identity của con người và workload, cấp quyền theo role/capability và ưu tiên credential ngắn hạn. Audit log phải nối action với identity thực.

## 2. Authentication khác authorization

Authentication trả lời “ai/what đang gọi”. Authorization trả lời identity đó được phép làm gì. TLS certificate, OIDC token hoặc cloud role có thể chứng minh identity; policy/RBAC quyết định permission.

PKI và service identity được đào sâu ở [canonical PKI, mTLS và service identity](../../computer_science/07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md). DevOps tập trung vào phân phối identity vào workload và rotation không downtime.

## 3. Secret là liability có lifecycle

Secret không chỉ là string cần giấu. Nó có creator, consumer, scope, TTL, rotation và revocation. Static credential sống nhiều năm làm incident khó contain vì không biết bao nhiêu nơi đã copy.

Secret manager/KMS giúp centralize control nhưng application vẫn phải có bootstrap identity để lấy secret. Đây là “secret zero” problem; workload identity/federation thường giảm nhu cầu distribute secret bootstrap dài hạn.

Cơ chế KMS/HSM/envelope encryption xem [canonical secrets và key lifecycle](../../computer_science/07_security_reliability/advanced/06_secrets_kms_hsm_rotation_and_envelope_encryption.md).

## 4. Rotation phải là protocol tương thích

Đổi password/credential ngay lập tức có thể làm service đang chạy mất access. Rotation an toàn thường có overlap: tạo credential/cert mới, distribute, reload/rollout consumer, verify, rồi revoke old.

Nếu application chỉ đọc secret khi startup, platform phải biết cần restart. Nếu library/sidecar hot reload được, cần verify connection mới thực sự dùng credential mới.

## 5. Policy as Code đưa feedback về sớm

Security review thủ công cho mọi manifest không scale. Policy as Code encode rule như “production workload không chạy privileged”, “public bucket cần exception”, “image phải đến từ registry được tin cậy”.

Policy có thể chạy ở CI để feedback sớm và ở admission/runtime để enforcement. Hai lớp có mục tiêu khác: CI giúp developer sửa trước merge; admission bảo vệ environment trước request cuối cùng.

Policy cần exception lifecycle. Nếu exception permanent và không owner/expiry, guardrail dần mất giá trị.

## 6. Supply chain: source không phải trust duy nhất

Attack có thể đi qua dependency, build runner, plugin/action, registry hoặc stolen signing key. Vì vậy cần nhìn software supply chain end-to-end:

```text
source → dependency → build environment → artifact → registry → deploy
```

Mỗi arrow cần identity/integrity evidence.

## 7. SBOM, provenance và signature giải quyết câu hỏi khác nhau

SBOM trả lời artifact chứa component nào. Provenance trả lời artifact được build từ source/process nào. Signature/attestation giúp verify statement đến từ identity/key được tin. Không cái nào tự chứng minh software không có vulnerability.

Khi kết hợp, platform có thể đặt policy: chỉ deploy artifact từ trusted builder, có provenance hợp lệ, dependency scan không vi phạm threshold, signature đúng và image digest bất biến.

## 8. CI runner là privileged infrastructure

Runner thường có source access và đôi khi publish/deploy permission. Workflow từ pull request chưa tin cậy không nên tự động có production credential. Self-hosted runner còn có persistence risk nếu job độc hại để lại process/file cho job sau.

Runner isolation, ephemeral execution và least-privilege job token là production security concern, không chỉ CI configuration.

## 9. Container/Kubernetes security theo defense in depth

Image nên giảm package không cần, chạy non-root khi phù hợp, drop capability, không privileged/mount host socket tùy tiện. Kubernetes thêm RBAC, namespace policy, network policy, admission control và workload identity.

Container isolation mechanism được giải thích tại [canonical container internals](../../computer_science/03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md). Platform chapter này chỉ đưa chúng thành secure default.

## 10. Governance không đồng nghĩa central approval

Governance tốt làm rule rõ, tự động và observable. Một central team phải duyệt từng database/namespace làm flow chậm và khuyến khích bypass. Tốt hơn là platform cung cấp SKU/plan đã approved, quota, data classification field và policy tự động.

Approval thủ công nên dành cho exception/risk thật sự cao.

## 11. Break-glass access

Incident đôi khi cần quyền cao tạm thời. Break-glass path nên được thiết kế trước: strong authentication, reason/ticket, time-bound privilege, audit và review sau sử dụng.

Không có break-glass chính thức thường dẫn tới shared admin credential “để phòng khi cần”, rủi ro hơn nhiều.

## 12. Vulnerability management cần exploitability context

Không phải CVE severity cao nào cũng có cùng risk cho workload. Package có thể không được load, path không reachable hoặc control khác giảm exploitability. Ngược lại, vulnerability medium ở Internet-facing auth component có thể quan trọng.

Platform nên ưu tiên theo asset exposure, exploitability, runtime context và business criticality, đồng thời vẫn giữ SLA remediation theo policy.

## 13. Senior note: secure-by-default phải đi cùng usable-by-default

Nếu security control quá khó dùng, team tìm đường vòng. Platform tốt làm secure path nhanh hơn insecure DIY: identity tự cấp theo workload, secret injection chuẩn, signed artifact tự động, policy feedback ngay PR.

Security và developer experience không đối lập; guardrail tốt biến security thành property của platform.