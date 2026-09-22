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

## 14. Threat model delivery system theo capability chiếm được

Threat modeling không cần bắt đầu bằng danh sách hàng trăm attack. Với platform, hãy hỏi nếu một principal hoặc component bị compromise thì attacker có thể thay state nào.

Nếu developer account bị chiếm, attacker có thể merge code trực tiếp hay vẫn cần reviewer khác? Nếu CI runner bị chiếm, nó chỉ build artifact hay có thể deploy production? Nếu registry token lộ, attacker có thể overwrite mutable tag hay artifact được pin digest/signature? Nếu GitOps bot token lộ, scope là một repo hay toàn organization?

Cách hỏi theo capability làm blast radius rõ hơn và dẫn tới control cụ thể: separation of duties, short-lived token, environment-scoped role, immutable artifact, approval cho high-risk path và audit.

## 15. Workload identity giảm secret distribution nhưng không xóa authorization problem

Federation/workload identity cho phép workload chứng minh identity bằng credential ngắn hạn do runtime/control plane cấp, rồi exchange/assume role để gọi cloud/service khác. Lợi ích lớn là không cần bake static key vào image hoặc Git.

Nhưng nếu service account có quyền quá rộng, credential ngắn hạn vẫn nguy hiểm trong thời gian hiệu lực. Vì vậy identity lifecycle và authorization scope phải đi cùng nhau. Audience, subject, role binding và environment boundary cần đủ chặt để token của workload A không được chấp nhận như workload B.

Mental model là: **bootstrap identity → token ngắn hạn → policy quyết định capability**. Không nên dừng ở “không còn secret file nên đã secure”.

## 16. Provenance/signature chỉ mạnh bằng trust policy của verifier

Một artifact có signature nhưng verifier chấp nhận bất kỳ key nào thì signature không tạo trust hữu ích. Một provenance statement ghi builder identity nhưng policy không phân biệt trusted builder với laptop cá nhân cũng tương tự.

Verifier cần policy rõ: artifact digest nào là subject; statement type nào được chấp nhận; builder/source identity nào thuộc trust domain; policy nào bắt buộc cho production; revocation hoặc compromised identity được xử lý ra sao.

Đây là lý do supply-chain security nên được xem như **authorization trên evidence**, không phải checkbox “đã ký image”.

## 17. Policy rollout cũng có thể gây outage

Admission/policy engine nằm trên critical control path. Một rule sai có thể chặn toàn bộ deploy; webhook chậm có thể tăng API latency; policy thay đổi global có blast radius lớn hơn một application release.

Policy nên có test fixture, dry-run/audit mode khi phù hợp, staged rollout và observability về denial/latency. Exception cũng phải versioned và có expiry. Platform security control là production software nên cần cùng discipline canary/rollback như application.

## 18. Secret exfiltration response khác secret rotation bình thường

Rotation định kỳ giả định old credential chưa chắc bị attacker giữ. Khi có bằng chứng exfiltration, cần containment nhanh hơn: xác định scope, revoke/disable credential cũ, tìm nơi credential đã được dùng, rotate dependent secret/key nếu trust chain bị ảnh hưởng và kiểm tra audit log cho misuse.

Nếu cùng một static secret được share cho 20 service, blast radius và forensic khó hơn nhiều. Đây là lợi ích thực tế của per-workload identity và short-lived credential: containment boundary nhỏ hơn.

## 19. Supply-chain dependency cần phân biệt source, package và execution trust

Một dependency có thể đến từ source repository, package registry hoặc binary/tool download. Pin version giúp reproducibility nhưng không tự chứng minh package đó là artifact mong muốn. Checksum/signature/provenance có thể bổ sung integrity, còn sandbox/least privilege giảm impact nếu dependency thực thi build script độc hại.

Đặc biệt trong CI, package manager hook, build plugin và third-party action có thể thực thi code với credential job. Vì vậy dependency review không chỉ nhìn runtime library; build-time dependency cũng nằm trong attack surface.

## 20. Senior walkthrough: pull request từ fork chạm release pipeline

Giả sử repo public nhận PR từ fork. Workflow chạy test trên code chưa tin cậy. Nếu job này có registry write token hoặc cloud deploy role, contributor có thể sửa test/build script để exfiltrate token.

Boundary an toàn hơn là tách untrusted verification khỏi trusted release. PR job dùng permission tối thiểu, không nhận production secret; sau merge vào protected branch, trusted workflow checkout exact revision và build/publish bằng identity riêng. Artifact promotion sau đó dựa trên digest/provenance thay vì tin output từ untrusted job.

Điểm cốt lõi không phụ thuộc GitHub Actions/Jenkins/GitLab CI: **code chưa được trust không được tự động nhận capability của production trust domain**.

## 21. Confused deputy: principal hợp lệ vẫn có thể làm việc không nên làm

Một service trung gian có quyền mạnh có thể bị user ít quyền lợi dụng để thực hiện action thay họ. Đây là confused-deputy problem. Ví dụ platform provisioner có quyền tạo database ở nhiều account; nếu API chỉ nhận `accountId` từ request mà không kiểm tra caller được phép target account nào, user có thể khiến provisioner dùng authority hợp lệ cho mục tiêu không hợp lệ.

Authentication của caller và authentication của provisioner đều có thể đúng, nhưng authorization chain vẫn sai. Platform phải bind **request intent → caller identity → allowed target/capability** trước khi dùng automation identity mạnh hơn.

Do đó audit log nên giữ cả actor gốc và execution identity. Nếu log chỉ thấy `platform-controller` tạo resource, forensic không trả lời ai đã yêu cầu và policy nào cho phép.

## 22. Identity propagation cần tránh biến service trung gian thành superuser mù context

Trong một request xuyên nhiều service, downstream cần biết authority nào thật sự được chuyển tiếp. Có ba pattern khác nhau: service gọi bằng identity riêng; service impersonate/delegate một phần identity user; hoặc service trao đổi token thành capability hẹp hơn.

Không nên forward nguyên token quyền rộng qua mọi hop chỉ vì tiện. Mỗi hop cần audience đúng, TTL ngắn và scope tối thiểu. Downstream cũng không nên tin một header như `X-User` chỉ vì nó đến từ internal network nếu ingress/service trước đó có thể bị compromise.

Mental model là **identity propagation không bằng authority propagation**. Biết request bắt nguồn từ user A không tự động nghĩa service B được phép làm mọi thứ A làm, và ngược lại service B có quyền riêng cũng không được dùng quyền đó thay A nếu policy không cho phép.

## 23. TOCTOU: policy check đúng ở thời điểm A có thể sai ở thời điểm B

Time-of-check to time-of-use xuất hiện khi hệ thống kiểm tra policy/state rồi action xảy ra sau đó trên state đã thay đổi. Ví dụ pipeline verify artifact digest/signature lúc approve, nhưng deploy step sau lại resolve mutable tag; hoặc platform check quota rồi async provision nhiều phút sau trong khi capacity/ownership đã đổi.

Cách giảm race là bind decision với immutable identity/version: artifact digest, generation/resource version, policy revision, request id và target identity. Với action dài, controller có thể cần revalidate invariant trước bước irreversible thay vì tin check ban đầu mãi mãi.

Security policy vì vậy không chỉ là “đã check hay chưa” mà còn là **check cái gì, ở revision nào, và action sử dụng đúng object đã được check hay không**.

## 24. Revocation không tức thời nếu verifier/cache/session còn state cũ

Credential ngắn hạn giảm cửa sổ rủi ro nhưng revoke một identity không bảo đảm mọi connection/token hiện hữu biến mất ngay. JWT self-contained có thể còn hợp lệ tới expiry; TLS connection đã establish có thể sống lâu; authorization cache có TTL; cloud control plane có propagation delay.

Incident response phải biết revocation semantics thực tế của từng layer. Nếu cần containment nhanh, có thể phải vừa revoke role/key, vừa chặn network/session, rotate downstream credential hoặc restart connection-owning workload tùy threat model.

Đây là lý do TTL, cache duration và connection lifetime là security parameter, không chỉ performance parameter.

## 25. Security boundary cần xét control-plane compromise và data-plane compromise khác nhau

Nếu application pod bị compromise, attacker có thể lấy workload token, gọi dependency trong scope và đọc data process đang thấy. Nếu GitOps/controller/CI release identity bị compromise, attacker có thể thay desired state của hàng trăm workload — blast radius khác hẳn.

Control-plane principal thường cần permission rộng để tự động hóa, nên phải được cô lập, monitor và chia scope mạnh hơn: per-environment identity, protected branch, separate signer/builder role, bounded controller permission và high-signal audit.

Một design “mọi automation dùng chung admin role cho tiện” biến compromise nhỏ thành organizational blast radius. Least privilege có giá trị nhất ở các principal có fan-out lớn.

## 26. Security evidence phải chứng minh invariant, không chỉ chứng minh tool đã chạy

Scan job xanh không chứng minh artifact production chính là artifact đã scan. Policy test pass không chứng minh production admission đang chạy đúng revision. Secret manager tồn tại không chứng minh workload không còn secret hard-coded.

Evidence chain tốt nối object cụ thể: source revision → build provenance → artifact digest → signature/attestation → deployment digest → runtime identity → authorization decision. Mỗi bước có thể hỏi “evidence này bound vào subject nào?”.

Khi audit/security review chỉ thu screenshot dashboard hoặc tên sản phẩm mà không bind được tới artifact/workload/identity cụ thể, control có thể chỉ tồn tại trên giấy. Platform security trưởng thành ưu tiên **verifiable linkage** hơn số lượng security tool.

## 27. Rotation chỉ hoàn tất khi chứng minh consumer đã chuyển sang credential mới

Có secret mới trong manager và workload đã restart chưa đủ. Consumer có thể giữ connection pool cũ, process khác chưa reload hoặc background worker ít traffic vẫn dùng credential cũ. Nếu revoke old quá sớm, failure chỉ xuất hiện muộn ở cohort chưa chuyển.

Rotation protocol tốt cần evidence: version mới đã được phân phối, connection/session mới đang dùng credential mới, consumer inventory không còn reference cũ và old-credential usage giảm về zero trong một khoảng phù hợp. Sau đó revoke mới biến overlap thành cutover có kiểm soát.

Với certificate hoặc key, dual-trust window cũng cần giới hạn. Overlap quá dài làm hai credential cùng hợp lệ và kéo dài blast radius. Rotation là migration có deadline, không phải trạng thái “giữ cả cũ lẫn mới cho chắc”.

## 28. Break-glass là một privileged session có lifecycle, không phải một account đặc biệt

Một tài khoản admin cố định dùng hàng ngày rồi gọi là break-glass đã mất ý nghĩa. Quyền khẩn cấp nên được cấp theo session/request cụ thể, có TTL, target scope, reason và ideally approval/elevation độc lập với normal role.

Sau khi incident kết thúc, access phải tự expire hoặc bị revoke, active session/token cần được kiểm tra, action quan trọng được review và credential/bootstrap path phải rotate nếu exposure risk thay đổi. “Ticket đã đóng” không chứng minh quyền cao đã biến mất.

Break-glass path cũng phải được test. Nếu đến incident mới phát hiện MFA device, recovery code hoặc identity provider phụ thuộc chính hệ thống đang outage, emergency access chỉ tồn tại trên tài liệu.

## 29. Audit mode và enforce mode là hai phase khác nhau của policy rollout

Một policy mới có thể chạy ở audit/shadow mode để đo bao nhiêu workload sẽ bị deny, false positive nằm ở đâu và exception nào cần thiết. Khi evidence đủ, policy mới chuyển sang enforce theo release ring hoặc environment.

Nhưng shadow mode không được kéo dài vô hạn. Nếu rule chỉ log suốt nhiều tháng mà không owner hoặc deadline, organization có cảm giác “đã có policy” nhưng invariant chưa được bảo vệ.

Rollout mature là: define invariant → test fixture → audit impact → fix/exception → staged enforce → monitor deny/latency → remove temporary compatibility. Policy-as-code cũng cần migration lifecycle giống API.

## 30. Fail-open hay fail-closed là reliability-security trade-off phải quyết định trước outage

Nếu admission/policy service không reachable, chặn mọi deploy giữ security invariant nhưng có thể ngăn emergency recovery. Cho phép mọi request tiếp tục giữ availability của control path nhưng mở cửa bypass policy.

Không có lựa chọn universal. Critical invariant như “artifact phải từ trusted registry” có thể fail-closed; low-risk metadata validation có thể fail-open có audit tùy threat model. Quan trọng là behavior khi dependency policy hỏng phải explicit, observable và được game-day test.

Nếu operator chỉ biết semantics này sau khi webhook outage xảy ra, policy system đang giấu một failure mode quan trọng.

## 31. Identity lifecycle phải bao gồm offboarding và stale principal

Least privilege lúc cấp quyền chưa đủ nếu principal không được dọn khi service/team/người dùng biến mất. Service account cũ, bot token không owner, role dành cho project đã archive tạo attack surface khó nhìn vì không còn traffic bình thường để lộ chúng.

Platform nên có inventory principal → owner → purpose → last-used → scope → expiry/review. Unused permission hoặc principal lâu không dùng là signal để thu hẹp, nhưng removal vẫn cần kiểm tra dependency batch/DR hiếm khi chạy.

Offboarding là reconciliation problem: source-of-truth về ownership thay đổi thì credential, role binding, repository access và break-glass membership liên quan phải hội tụ theo.

## 32. Least privilege cần runtime evidence nhưng không được học mù từ traffic hiện tại

Quan sát permission thực sự được dùng giúp phát hiện wildcard hoặc quyền thừa. Tuy nhiên “30 ngày không gọi action X” không chứng minh action X vô dụng nếu nó chỉ cần cho quarterly restore, certificate rotation hoặc disaster recovery.

Permission reduction nên kết hợp observed usage với declared capability/runbook và rare-path test. Mục tiêu là giảm quyền tới tập cần thiết cho cả normal path lẫn recovery path, không tối ưu policy theo traffic sample ngắn.

Đây là cùng bài toán observability: absence of use chỉ có ý nghĩa khi detector/window bao phủ behavior cần bảo vệ.

## 33. Audit log cũng là security asset cần integrity và retention boundary

Audit log hữu ích chỉ khi attacker hoặc principal bị điều tra không dễ sửa/xóa chính evidence của mình. Nếu CI admin có thể vừa deploy vừa xóa audit record cùng account, forensic trust bị yếu.

High-value audit trail nên có write/read/delete permission tách biệt phù hợp, retention/immutability theo threat model, clock/source identity rõ và export sang boundary khó bị cùng compromise. Không phải mọi application log cần WORM, nhưng privileged control-plane action cần evidence mạnh hơn debug log thông thường.

Security control cuối cùng vẫn cần khả năng chứng minh: **ai đã làm gì, lên subject nào, bằng authority nào, policy revision nào và evidence đó còn đáng tin không**.