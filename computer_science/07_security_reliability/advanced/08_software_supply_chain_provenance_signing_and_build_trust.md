# Software supply chain, provenance, signing và build trust

Một production artifact hiếm khi được tạo chỉ từ source code của một repository. Nó phụ thuộc compiler, package manager, third-party dependencies, build scripts, container base image, CI runner, registry, signing key và deployment controller. Vì vậy câu hỏi bảo mật “source code có sạch không?” là chưa đủ. Ta còn phải hỏi **artifact đang chạy được tạo từ đâu, bằng pipeline nào, từ dependency nào, ai có quyền thay đổi pipeline và bằng evidence nào ta chứng minh chuỗi đó**.

Đây là bài toán **software supply chain security**. Chapter này không biến thành catalog sản phẩm SBOM/scanner/signing. Trọng tâm là trust graph, provenance, authority và containment.

Mental model:

```text
source identity
→ dependency resolution
→ build environment
→ build steps
→ artifact digest
→ provenance / attestation
→ signing / authorization
→ registry
→ deployment policy
→ runtime artifact
```

Invariant cần giữ là: **artifact được đưa vào môi trường tin cậy phải có identity nội dung rõ, provenance đủ để kiểm tra policy, và không có actor ngoài authority được phép thay artifact mà vẫn vượt qua verification boundary**.

## 1. Supply chain mở rộng trust boundary

Application có thể không chứa vulnerability rõ ràng nhưng vẫn bị compromise nếu dependency registry, CI credential hoặc build runner bị chiếm quyền. Điều này xảy ra vì build pipeline có authority biến source + dependency thành artifact mà production tin.

Trust graph vì vậy gồm nhiều principal:

```text
developer
repository
CI workflow
runner
package registry
artifact registry
signing service
CD controller
runtime platform
```

Mỗi edge đại diện một capability: push code, approve change, publish package, run build, write registry, sign artifact hoặc deploy.

Security review phải tìm **edge nào đủ quyền thay đổi production outcome**.

## 2. Source identity khác artifact identity

Commit hash nhận diện source tree ở một thời điểm, nhưng artifact còn phụ thuộc toolchain và dependency. Hai build từ cùng commit có thể khác nếu dependency resolution không deterministic, timestamp/environment ảnh hưởng output hoặc build script tải dữ liệu bên ngoài.

Artifact nên có content identity như cryptographic digest. Digest trả lời “bytes này là bytes nào?”, không trả lời “bytes này có an toàn không?”. Đây là distinction quan trọng.

```text
digest → content identity
signature → principal/key đã xác nhận statement nào đó
provenance → artifact được tạo như thế nào
policy → statement nào đủ để cho phép deploy
```

Không khái niệm nào thay thế toàn bộ khái niệm khác.

## 3. Dependency resolution là một security decision

Package manifest thường chỉ mô tả constraint; resolver quyết định version cụ thể và transitive dependencies. Nếu constraint quá rộng hoặc lock state không được bảo vệ, cùng source có thể resolve thành graph khác theo thời gian.

Threat không chỉ là package chứa malware. Namespace confusion, dependency confusion, compromised maintainer, malicious update hoặc registry takeover đều thay đổi graph mà build tiêu thụ.

Vì vậy dependency evidence cần biết package identity, version, source registry, digest khi có thể và relation transitive. **Software Bill of Materials (SBOM)** hữu ích như inventory, nhưng inventory không tự chứng minh artifact được build đúng từ inventory đó.

## 4. Build environment là một principal có quyền lớn

CI runner thường đọc source, secret và dependency rồi ghi artifact. Nếu runner bị compromise, attacker có thể inject bytes sau review mà source repository vẫn sạch.

Đây là lý do build environment phải được xem như security boundary. Isolation, ephemeral execution, least privilege, network egress control và credential scope giảm blast radius.

Một runner có token cho phép push image, ký artifact và deploy production tạo authority concentration quá lớn. Compromise một principal có thể vượt qua nhiều control tưởng như độc lập.

## 5. Reproducible build và hermetic build giải quyết hai câu hỏi khác nhau

**Hermetic build** cố giới hạn input của build vào tập đã khai báo, giảm phụ thuộc môi trường/network ngầm. **Reproducible build** cố bảo đảm cùng input tạo cùng output bit-for-bit hoặc theo contract xác định.

Hermeticity giúp biết input là gì. Reproducibility giúp nhiều builder kiểm chứng output. Một build có thể hermetic nhưng không reproducible nếu timestamp/randomness không được normalize. Một build có thể tình cờ reproducible nhưng vẫn lấy dependency từ nguồn không được trust.

Không nên biến hai thuật ngữ thành checkbox giống nhau.

## 6. Provenance là statement về quá trình tạo artifact

Provenance nên trả lời các câu như: source revision nào, builder identity nào, workflow nào, dependency/input nào, thời điểm nào và output digest nào.

Provenance có giá trị khi verifier tin được principal phát hành statement. Nếu attacker vừa sửa artifact vừa sửa provenance trong cùng một database không được bảo vệ, provenance không tạo thêm assurance.

Do đó provenance cần trust root, integrity và policy consumer rõ ràng.

## 7. Signing không làm artifact trở nên tốt

Digital signature chứng minh một key đã ký một message/digest theo cryptographic assumption. Nó không chứng minh signer đáng tin, build không chứa malware hoặc source đã được review.

Mental model:

```text
signature valid
→ holder của signing authority đã xác nhận statement
```

Sau đó policy mới quyết định authority đó có đủ để deploy không.

Nếu signing key nằm ngay trên compromised CI runner, attacker có thể tạo artifact độc hại rồi ký hợp lệ. Security architecture tốt tách build identity, signing authority và deployment verification đủ để một compromise đơn lẻ khó đi hết path.

## 8. Keyless/ephemeral identity vẫn cần trust chain

Một số kiến trúc tránh long-lived signing key trên runner bằng cách cấp short-lived identity dựa trên workload/CI identity rồi ghi transparency evidence. Điều này giảm secret-at-rest risk nhưng không xóa trust.

Ta chuyển trust sang identity provider, workflow claim, certificate issuance, log integrity và verifier policy. Nếu workflow identity quá rộng, attacker vẫn có thể lấy credential hợp lệ từ một job bị chiếm.

Nguyên lý chung giống service identity: **không có credential “không cần trust”; chỉ có trust được chuyển sang boundary khác**.

## 9. Transparency log và append-only evidence

Một transparency log giúp phát hiện hoặc audit các signing/provenance events bằng cách làm history khó sửa âm thầm. Giá trị của nó nằm ở khả năng kiểm chứng inclusion/consistency và nhiều observer có thể phát hiện equivocation tùy thiết kế.

Nhưng log không ngăn artifact độc hại được ký. Nó tăng khả năng quan sát và accountability. Prevention và detection là hai control khác nhau.

## 10. Deployment policy là nơi trust trở thành enforcement

Nếu CI tạo provenance nhưng deployment system không kiểm tra, evidence chỉ là documentation. Enforcement boundary cần quyết định artifact nào được phép chạy dựa trên digest, signer/builder identity, source/workflow constraints, environment và exception policy.

Policy phải xử lý rollout thực tế: emergency hotfix, rollback, multi-region registry, disconnected environment và key rotation. Nếu exception path dễ hơn normal path và không được audit, attacker sẽ nhắm vào exception.

## 11. Mutable tag là naming convenience, không phải identity

Tag như `latest` hoặc semantic version có thể trỏ sang bytes khác theo thời gian tùy registry policy. Digest mới là content identity ổn định hơn.

Deploy bằng mutable reference tạo TOCTOU-style risk: hệ thống review một tag nhưng lúc pull tag đã trỏ artifact khác. Cách reasoning an toàn hơn là resolve reference sang digest tại boundary kiểm soát rồi propagate digest đó qua rollout/evidence.

## 12. Build cache cũng là supply-chain state

Build cache tăng tốc bằng cách reuse output trung gian. Nhưng nếu cache key không bao phủ đủ input hoặc cache có thể bị actor không tin ghi vào, build có thể consume poisoned state.

Cache correctness invariant giống nhiều cache khác:

```text
cache key phải đại diện đủ semantic input
cache value phải đến từ authority được chấp nhận
```

Performance optimization vì vậy mở thêm trust boundary.

## 13. Secret trong pipeline và blast radius

CI thường cần credential để đọc private dependency, push artifact hoặc gọi cloud API. Long-lived secret với scope rộng làm compromise pipeline trở thành compromise infrastructure.

Ưu tiên short-lived credential, workload identity, least privilege và tách environment. Nhưng rotation chỉ hữu ích nếu old capability thực sự mất hiệu lực. Nếu token bị copy vào artifact/log/cache, rotation ở secret store không đủ.

Cross-link với [Secret, KMS, HSM, rotation và envelope encryption](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md).

## 14. Threat: compromised dependency maintainer

Giả sử dependency hợp lệ bị maintainer account compromise và publish version mới chứa backdoor. Signature của registry/package có thể vẫn hợp lệ nếu attacker dùng authority thật.

Control hữu ích nằm ở nhiều lớp: version pinning giảm automatic uptake; dependency review/diff tạo human/automated evidence; sandbox/build isolation giảm build-time blast radius; runtime least privilege giảm post-deploy capability; detection có thể phát hiện behavior bất thường.

Không control đơn lẻ chứng minh dependency “safe”. Defense-in-depth phải cắt attack path ở nhiều edge.

## 15. Threat: compromised CI workflow

Nếu attacker sửa workflow để tải binary bên ngoài rồi inject vào artifact, source application có thể gần như không đổi. Branch protection chỉ có giá trị nếu workflow/config cũng nằm trong review boundary và actor không thể bypass policy.

Provenance có thể giúp nếu nó ghi workflow identity/revision và deployment policy chỉ chấp nhận approved workflow. Nhưng nếu attacker có quyền thay cả approved policy, trust root đã bị compromise.

Câu hỏi quan trọng luôn là: **ai có quyền thay rule xác định cái gì được tin?**

## 16. Supply chain và Software Engineering giao nhau ở change process

Security không sở hữu toàn bộ workflow engineering. Code review, branch strategy, compatibility, deployment safety và rollback thuộc Software Engineering; Security sở hữu trust/authority/evidence của artifact path.

Cross-link với [deployment safety](../../09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md) và [architecture decisions/evolution](../../09_software_engineering/advanced/00_architecture_decisions_evolution_and_socio_technical_constraints.md).

Một rollout canary không chứng minh artifact trusted; một signature hợp lệ không chứng minh rollout safe. Hai reasoning paths bổ sung nhau.

## 17. Incident response cần provenance graph

Khi phát hiện package X bị compromise, câu hỏi production không phải chỉ “repo nào khai báo X?”. Cần biết:

```text
version/digest nào bị ảnh hưởng?
artifact nào được build từ nó?
artifact đó đã được deploy ở environment nào?
cohort nào đang chạy?
credential/build runner nào có liên quan?
artifact nào cần revoke/quarantine/rebuild?
```

SBOM + provenance + deployment inventory tạo graph để trả lời. Nếu mỗi hệ thống giữ identifier khác nhau mà không có digest/revision chung, incident containment chậm vì không join được evidence.

Cross-link với [Detection engineering, forensics và incident evidence](./07_detection_engineering_forensics_and_incident_evidence.md).

## 18. Revocation khó hơn signing

Ký artifact là event đơn giản; thu hồi trust sau compromise khó hơn. Artifact đã được mirror, cached hoặc chạy offline. Key rotation không tự dừng workload đang chạy.

Effective revocation cần policy propagation, deployment inventory, runtime replacement/quarantine và evidence rằng old artifact không còn active. Đây là cùng distinction giữa credential revocation và capability thực tế.

## 19. Production evidence

Một supply-chain system nên cho phép reconstruct:

```text
runtime workload
→ artifact digest
→ registry object
→ provenance statement
→ builder/workflow identity
→ source revision
→ dependency/input graph
→ policy decision
```

Evidence cần versioned và query được. Log chỉ ghi “deployment succeeded” không đủ để điều tra provenance. Ngược lại log mọi file/dependency mà không có stable identifiers sẽ tạo data volume lớn nhưng khó join.

## 20. Lower layers thực sự quyết định trust

Cuối cùng signing key nằm trong software process, TPM/HSM hoặc service; runner chạy trên OS/hypervisor; registry lưu bytes trên storage; network mang artifact; identity provider cấp credential. Supply-chain trust không nổi trên phần cứng.

Nếu attacker kiểm soát lower layer có authority đọc signing key hoặc thay verifier, higher-level policy có thể mất ý nghĩa. Đây không có nghĩa phải trust mọi layer như nhau; nghĩa là threat model phải nói rõ layer nào nằm trong trusted computing base.

## 21. Mental model cuối

Software supply chain là một **authority graph quanh quá trình biến source thành executable state**. Digest cho identity, provenance cho history, signature cho cryptographic assertion, SBOM cho inventory, policy cho enforcement, detection cho evidence và incident response cho containment. Không thành phần nào tự đủ.

Khi review pipeline, đừng hỏi “đã bật signing chưa?”. Hãy hỏi: **principal nào có thể thay bytes production, evidence nào nối bytes đó về source/build, verifier tin ai, trust root có thể bị bypass bằng path nào, và khi một principal bị compromise ta cắt capability đó nhanh tới đâu?**