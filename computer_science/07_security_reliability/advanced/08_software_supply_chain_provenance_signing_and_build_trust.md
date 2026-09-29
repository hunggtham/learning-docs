# Software supply chuỗi (chain / 사슬), provenance, signing và bản dựng (build / 빌드) trust

Một môi trường vận hành (production / 운영 환경) sản phẩm tạo ra (artifact / 산출물) hiếm khi được tạo chỉ từ mã nguồn (source code / 소스 코드) của một repository. Nó phụ thuộc trình biên dịch (compiler / 컴파일러), trình quản lý gói (package manager / 패키지 관리자), third-party dependencies, bản dựng (build / 빌드) scripts, bộ chứa (container / 컨테이너) cơ sở (base / 기반) ảnh (image / 이미지), CI runner, registry, signing key và triển khai (deployment / 배포) controller. Vì vậy câu hỏi bảo mật “mã nguồn (source code / 소스 코드) có sạch không?” là chưa đủ. Ta còn phải hỏi **sản phẩm tạo ra (artifact / 산출물) đang chạy được tạo từ đâu, bằng chuỗi xử lý (pipeline / 파이프라인) nào, từ phụ thuộc (dependency / 의존성) nào, ai có quyền thay đổi chuỗi xử lý (pipeline / 파이프라인) và bằng bằng chứng (evidence / 증거) nào ta chứng minh chuỗi đó**.

Đây là bài toán **software supply chuỗi (chain / 사슬) bảo mật (security / 보안)**. Chapter này không biến thành danh mục (catalog / 카탈로그) sản phẩm SBOM/scanner/signing. Trọng tâm là trust đồ thị (graph / 그래프), provenance, authority và containment.

Mô hình tư duy (mental model / 사고 모델):

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

Bất biến (invariant / 불변식) cần giữ là: **sản phẩm tạo ra (artifact / 산출물) được đưa vào môi trường tin cậy phải có định danh (identity / 식별자) nội dung rõ, provenance đủ để kiểm tra chính sách (policy / 정책), và không có actor ngoài authority được phép thay sản phẩm tạo ra (artifact / 산출물) mà vẫn vượt qua xác minh (verification / 확인) ranh giới (boundary / 경계)**.

## 1. Supply chuỗi (chain / 사슬) mở rộng trust ranh giới (boundary / 경계)

Ứng dụng (application / 애플리케이션) có thể không chứa vulnerability rõ ràng nhưng vẫn bị compromise nếu phụ thuộc (dependency / 의존성) registry, CI credential hoặc bản dựng (build / 빌드) runner bị chiếm quyền. Điều này xảy ra vì bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인) có authority biến nguồn (source / 소스) + phụ thuộc (dependency / 의존성) thành sản phẩm tạo ra (artifact / 산출물) mà môi trường vận hành (production / 운영 환경) tin.

Trust đồ thị (graph / 그래프) vì vậy gồm nhiều principal:

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

Mỗi edge đại diện một năng lực (capability / 역량): push mã (code / 코드), approve thay đổi (change / 변경), publish gói (package / 패키지), run bản dựng (build / 빌드), ghi (write / 쓰기) registry, sign sản phẩm tạo ra (artifact / 산출물) hoặc deploy.

Bảo mật (security / 보안) rà soát (review / 검토) phải tìm **edge nào đủ quyền thay đổi môi trường vận hành (production / 운영 환경) kết quả (outcome / 결과)**.

## 2. Nguồn (source / 소스) định danh (identity / 식별자) khác sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)

Lần ghi nhận (commit / 커밋) băm (hash / 해시) nhận diện nguồn (source / 소스) cây (tree / 트리) ở một thời điểm, nhưng sản phẩm tạo ra (artifact / 산출물) còn phụ thuộc toolchain và phụ thuộc (dependency / 의존성). Hai bản dựng (build / 빌드) từ cùng lần ghi nhận (commit / 커밋) có thể khác nếu phụ thuộc (dependency / 의존성) resolution không deterministic, timestamp/môi trường (environment / 환경) ảnh hưởng đầu ra (output / 출력) hoặc bản dựng (build / 빌드) script tải dữ liệu bên ngoài.

Sản phẩm tạo ra (artifact / 산출물) nên có content định danh (identity / 식별자) như cryptographic digest. Digest trả lời “bytes này là bytes nào?”, không trả lời “bytes này có an toàn không?”. Đây là distinction quan trọng.

```text
digest → content identity
signature → principal/key đã xác nhận statement nào đó
provenance → artifact được tạo như thế nào
policy → statement nào đủ để cho phép deploy
```

Không khái niệm nào thay thế toàn bộ khái niệm khác.

## 3. Phụ thuộc (dependency / 의존성) resolution là một bảo mật (security / 보안) quyết định (decision / 결정)

Gói (package / 패키지) manifest thường chỉ mô tả ràng buộc (constraint / 제약조건); resolver quyết định phiên bản (version / 버전) cụ thể và transitive dependencies. Nếu ràng buộc (constraint / 제약조건) quá rộng hoặc khóa (lock / 잠금) trạng thái (state / 상태) không được bảo vệ, cùng nguồn (source / 소스) có thể resolve thành đồ thị (graph / 그래프) khác theo thời gian.

Threat không chỉ là gói (package / 패키지) chứa malware. Không gian tên (namespace / 네임스페이스) confusion, phụ thuộc (dependency / 의존성) confusion, compromised maintainer, malicious cập nhật (update / 업데이트) hoặc registry takeover đều thay đổi đồ thị (graph / 그래프) mà bản dựng (build / 빌드) tiêu thụ.

Vì vậy phụ thuộc (dependency / 의존성) bằng chứng (evidence / 증거) cần biết gói (package / 패키지) định danh (identity / 식별자), phiên bản (version / 버전), nguồn (source / 소스) registry, digest khi có thể và quan hệ (relation / 관계) transitive. **Software Bill of Materials (SBOM)** hữu ích như inventory, nhưng inventory không tự chứng minh sản phẩm tạo ra (artifact / 산출물) được bản dựng (build / 빌드) đúng từ inventory đó.

## 4. Bản dựng (build / 빌드) môi trường (environment / 환경) là một principal có quyền lớn

CI runner thường đọc nguồn (source / 소스), secret và phụ thuộc (dependency / 의존성) rồi ghi sản phẩm tạo ra (artifact / 산출물). Nếu runner bị compromise, attacker có thể inject bytes sau rà soát (review / 검토) mà nguồn (source / 소스) repository vẫn sạch.

Đây là lý do bản dựng (build / 빌드) môi trường (environment / 환경) phải được xem như ranh giới bảo mật (security boundary / 보안 경계). Isolation, ephemeral thực thi (execution / 실행), least privilege, mạng (network / 네트워크) egress điều khiển (control / 제어) và credential phạm vi (scope / 범위) giảm blast radius.

Một runner có đơn vị từ (token / 토큰) cho phép push ảnh (image / 이미지), ký sản phẩm tạo ra (artifact / 산출물) và deploy môi trường vận hành (production / 운영 환경) tạo authority concentration quá lớn. Compromise một principal có thể vượt qua nhiều điều khiển (control / 제어) tưởng như độc lập.

## 5. Reproducible bản dựng (build / 빌드) và hermetic bản dựng (build / 빌드) giải quyết hai câu hỏi khác nhau

**Hermetic bản dựng (build / 빌드)** cố giới hạn đầu vào (input / 입력) của bản dựng (build / 빌드) vào tập đã khai báo, giảm phụ thuộc môi trường/mạng (network / 네트워크) ngầm. **Reproducible bản dựng (build / 빌드)** cố bảo đảm cùng đầu vào (input / 입력) tạo cùng đầu ra (output / 출력) bit-for-bit hoặc theo đặc tả hợp đồng (contract / 계약) xác định.

Hermeticity giúp biết đầu vào (input / 입력) là gì. Reproducibility giúp nhiều builder kiểm chứng đầu ra (output / 출력). Một bản dựng (build / 빌드) có thể hermetic nhưng không reproducible nếu timestamp/randomness không được normalize. Một bản dựng (build / 빌드) có thể tình cờ reproducible nhưng vẫn lấy phụ thuộc (dependency / 의존성) từ nguồn không được trust.

Không nên biến hai thuật ngữ thành checkbox giống nhau.

## 6. Provenance là statement về quá trình tạo sản phẩm tạo ra (artifact / 산출물)

Provenance nên trả lời các câu như: nguồn (source / 소스) revision nào, builder định danh (identity / 식별자) nào, workflow nào, phụ thuộc (dependency / 의존성)/đầu vào (input / 입력) nào, thời điểm nào và đầu ra (output / 출력) digest nào.

Provenance có giá trị khi verifier tin được principal phát hành statement. Nếu attacker vừa sửa sản phẩm tạo ra (artifact / 산출물) vừa sửa provenance trong cùng một cơ sở dữ liệu (database / 데이터베이스) không được bảo vệ, provenance không tạo thêm assurance.

Do đó provenance cần trust gốc (root / 루트), integrity và chính sách (policy / 정책) bên tiêu thụ (consumer / 소비자) rõ ràng.

## 7. Signing không làm sản phẩm tạo ra (artifact / 산출물) trở nên tốt

Digital signature chứng minh một key đã ký một message/digest theo cryptographic giả định (assumption / 가정). Nó không chứng minh signer đáng tin, bản dựng (build / 빌드) không chứa malware hoặc nguồn (source / 소스) đã được rà soát (review / 검토).

Mô hình tư duy (mental model / 사고 모델):

```text
signature valid
→ holder của signing authority đã xác nhận statement
```

Sau đó chính sách (policy / 정책) mới quyết định authority đó có đủ để deploy không.

Nếu signing key nằm ngay trên compromised CI runner, attacker có thể tạo sản phẩm tạo ra (artifact / 산출물) độc hại rồi ký hợp lệ. Bảo mật (security / 보안) kiến trúc (architecture / 아키텍처) tốt tách bản dựng (build / 빌드) định danh (identity / 식별자), signing authority và triển khai (deployment / 배포) xác minh (verification / 확인) đủ để một compromise đơn lẻ khó đi hết đường dẫn (path / 경로).

## 8. Keyless/ephemeral định danh (identity / 식별자) vẫn cần trust chuỗi (chain / 사슬)

Một số kiến trúc tránh long-lived signing key trên runner bằng cách cấp short-lived định danh (identity / 식별자) dựa trên tải công việc (workload / 워크로드)/CI định danh (identity / 식별자) rồi ghi transparency bằng chứng (evidence / 증거). Điều này giảm secret-at-rest rủi ro (risk / 위험) nhưng không xóa trust.

Ta chuyển trust sang định danh (identity / 식별자) provider, workflow claim, certificate issuance, log integrity và verifier chính sách (policy / 정책). Nếu workflow định danh (identity / 식별자) quá rộng, attacker vẫn có thể lấy credential hợp lệ từ một job bị chiếm.

Nguyên lý chung giống dịch vụ (service / 서비스) định danh (identity / 식별자): **không có credential “không cần trust”; chỉ có trust được chuyển sang ranh giới (boundary / 경계) khác**.

## 9. Transparency log và append-only bằng chứng (evidence / 증거)

Một transparency log giúp phát hiện hoặc kiểm tra (audit / 감사) các signing/provenance events bằng cách làm lịch sử (history / 이력) khó sửa âm thầm. Giá trị của nó nằm ở khả năng kiểm chứng inclusion/consistency và nhiều observer có thể phát hiện equivocation tùy thiết kế.

Nhưng log không ngăn sản phẩm tạo ra (artifact / 산출물) độc hại được ký. Nó tăng khả năng quan sát và accountability. Prevention và detection là hai điều khiển (control / 제어) khác nhau.

## 10. Triển khai (deployment / 배포) chính sách (policy / 정책) là nơi trust trở thành enforcement

Nếu CI tạo provenance nhưng triển khai (deployment / 배포) hệ thống (system / 시스템) không kiểm tra, bằng chứng (evidence / 증거) chỉ là documentation. Enforcement ranh giới (boundary / 경계) cần quyết định sản phẩm tạo ra (artifact / 산출물) nào được phép chạy dựa trên digest, signer/builder định danh (identity / 식별자), nguồn (source / 소스)/workflow các ràng buộc (constraints / 제약조건들), môi trường (environment / 환경) và exception chính sách (policy / 정책).

Chính sách (policy / 정책) phải xử lý rollout thực tế: emergency hotfix, quay lui (rollback / 롤백), multi-region registry, disconnected môi trường (environment / 환경) và key rotation. Nếu exception đường dẫn (path / 경로) dễ hơn normal đường dẫn (path / 경로) và không được kiểm tra (audit / 감사), attacker sẽ nhắm vào exception.

## 11. Mutable tag là naming convenience, không phải định danh (identity / 식별자)

Tag như `latest` hoặc ngữ nghĩa (semantic / 의미적) phiên bản (version / 버전) có thể trỏ sang bytes khác theo thời gian tùy registry chính sách (policy / 정책). Digest mới là content định danh (identity / 식별자) ổn định hơn.

Deploy bằng mutable tham chiếu (reference / 참조) tạo TOCTOU-style rủi ro (risk / 위험): hệ thống rà soát (review / 검토) một tag nhưng lúc pull tag đã trỏ sản phẩm tạo ra (artifact / 산출물) khác. Cách lập luận (reasoning / 추론) an toàn hơn là resolve tham chiếu (reference / 참조) sang digest tại ranh giới (boundary / 경계) kiểm soát rồi propagate digest đó qua rollout/bằng chứng (evidence / 증거).

## 12. Bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시) cũng là supply-chain trạng thái (state / 상태)

Bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시) tăng tốc bằng cách reuse đầu ra (output / 출력) trung gian. Nhưng nếu bộ nhớ đệm (cache / 캐시) key không bao phủ đủ đầu vào (input / 입력) hoặc bộ nhớ đệm (cache / 캐시) có thể bị actor không tin ghi vào, bản dựng (build / 빌드) có thể consume poisoned trạng thái (state / 상태).

Bộ nhớ đệm (cache / 캐시) tính đúng đắn (correctness / 정확성) bất biến (invariant / 불변식) giống nhiều bộ nhớ đệm (cache / 캐시) khác:

```text
cache key phải đại diện đủ semantic input
cache value phải đến từ authority được chấp nhận
```

Hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) vì vậy mở thêm trust ranh giới (boundary / 경계).

## 13. Secret trong chuỗi xử lý (pipeline / 파이프라인) và blast radius

CI thường cần credential để đọc private phụ thuộc (dependency / 의존성), push sản phẩm tạo ra (artifact / 산출물) hoặc gọi cloud API. Long-lived secret với phạm vi (scope / 범위) rộng làm compromise chuỗi xử lý (pipeline / 파이프라인) trở thành compromise hạ tầng (infrastructure / 인프라).

Ưu tiên short-lived credential, tải công việc (workload / 워크로드) định danh (identity / 식별자), least privilege và tách môi trường (environment / 환경). Nhưng rotation chỉ hữu ích nếu old năng lực (capability / 역량) thực sự mất hiệu lực. Nếu đơn vị từ (token / 토큰) bị bản sao (copy / 복사) vào sản phẩm tạo ra (artifact / 산출물)/log/bộ nhớ đệm (cache / 캐시), rotation ở secret store không đủ.

Cross-link với [Secret, KMS, HSM, rotation và envelope encryption](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md).

## 14. Threat: compromised phụ thuộc (dependency / 의존성) maintainer

Giả sử phụ thuộc (dependency / 의존성) hợp lệ bị maintainer account compromise và publish phiên bản (version / 버전) mới chứa backdoor. Signature của registry/gói (package / 패키지) có thể vẫn hợp lệ nếu attacker dùng authority thật.

Điều khiển (control / 제어) hữu ích nằm ở nhiều lớp: phiên bản (version / 버전) pinning giảm automatic uptake; phụ thuộc (dependency / 의존성) rà soát (review / 검토)/diff tạo human/automated bằng chứng (evidence / 증거); sandbox/bản dựng (build / 빌드) isolation giảm build-time blast radius; thời gian chạy (runtime / 런타임) least privilege giảm post-deploy năng lực (capability / 역량); detection có thể phát hiện hành vi (behavior / 동작) bất thường.

Không điều khiển (control / 제어) đơn lẻ chứng minh phụ thuộc (dependency / 의존성) “safe”. Defense-in-depth phải cắt attack đường dẫn (path / 경로) ở nhiều edge.

## 15. Threat: compromised CI workflow

Nếu attacker sửa workflow để tải nhị phân (binary / 이진) bên ngoài rồi inject vào sản phẩm tạo ra (artifact / 산출물), nguồn (source / 소스) ứng dụng (application / 애플리케이션) có thể gần như không đổi. Branch protection chỉ có giá trị nếu workflow/cấu hình (config / 설정) cũng nằm trong rà soát (review / 검토) ranh giới (boundary / 경계) và actor không thể bypass chính sách (policy / 정책).

Provenance có thể giúp nếu nó ghi workflow định danh (identity / 식별자)/revision và triển khai (deployment / 배포) chính sách (policy / 정책) chỉ chấp nhận approved workflow. Nhưng nếu attacker có quyền thay cả approved chính sách (policy / 정책), trust gốc (root / 루트) đã bị compromise.

Câu hỏi quan trọng luôn là: **ai có quyền thay quy tắc (rule / 규칙) xác định cái gì được tin?**

## 16. Supply chuỗi (chain / 사슬) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) giao nhau ở thay đổi (change / 변경) tiến trình (process / 프로세스)

Bảo mật (security / 보안) không sở hữu toàn bộ workflow kỹ thuật (engineering / 엔지니어링). Rà soát mã (code review / 코드 리뷰), branch chiến lược (strategy / 전략), tính tương thích (compatibility / 호환성), triển khai (deployment / 배포) an toàn (safety / 안전) và quay lui (rollback / 롤백) thuộc Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학); Bảo mật (security / 보안) sở hữu trust/authority/bằng chứng (evidence / 증거) của sản phẩm tạo ra (artifact / 산출물) đường dẫn (path / 경로).

Cross-link với [deployment safety](../../09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md) và [architecture decisions/evolution](../../09_software_engineering/advanced/00_architecture_decisions_evolution_and_socio_technical_constraints.md).

Một rollout canary không chứng minh sản phẩm tạo ra (artifact / 산출물) trusted; một signature hợp lệ không chứng minh rollout safe. Hai lập luận (reasoning / 추론) paths bổ sung nhau.

## 17. Sự cố (incident / 인시던트) phản hồi (response / 응답) cần provenance đồ thị (graph / 그래프)

Khi phát hiện gói (package / 패키지) X bị compromise, câu hỏi môi trường vận hành (production / 운영 환경) không phải chỉ “repo nào khai báo X?”. Cần biết:

```text
version/digest nào bị ảnh hưởng?
artifact nào được build từ nó?
artifact đó đã được deploy ở environment nào?
cohort nào đang chạy?
credential/build runner nào có liên quan?
artifact nào cần revoke/quarantine/rebuild?
```

SBOM + provenance + triển khai (deployment / 배포) inventory tạo đồ thị (graph / 그래프) để trả lời. Nếu mỗi hệ thống giữ identifier khác nhau mà không có digest/revision chung, sự cố (incident / 인시던트) containment chậm vì không phép nối (join / 조인) được bằng chứng (evidence / 증거).

Cross-link với [Detection engineering, forensics và incident evidence](./07_detection_engineering_forensics_and_incident_evidence.md).

## 18. Revocation khó hơn signing

Ký sản phẩm tạo ra (artifact / 산출물) là sự kiện (event / 이벤트) đơn giản; thu hồi trust sau compromise khó hơn. Sản phẩm tạo ra (artifact / 산출물) đã được mirror, cached hoặc chạy offline. Key rotation không tự dừng tải công việc (workload / 워크로드) đang chạy.

Effective revocation cần chính sách (policy / 정책) propagation, triển khai (deployment / 배포) inventory, thời gian chạy (runtime / 런타임) replacement/quarantine và bằng chứng (evidence / 증거) rằng old sản phẩm tạo ra (artifact / 산출물) không còn active. Đây là cùng distinction giữa credential revocation và năng lực (capability / 역량) thực tế.

## 19. Bằng chứng vận hành (production evidence / 운영 증거)

Một supply-chain hệ thống (system / 시스템) nên cho phép reconstruct:

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

Bằng chứng (evidence / 증거) cần versioned và truy vấn (query / 쿼리) được. Log chỉ ghi “triển khai (deployment / 배포) succeeded” không đủ để điều tra provenance. Ngược lại log mọi tệp (file / 파일)/phụ thuộc (dependency / 의존성) mà không có stable identifiers sẽ tạo dữ liệu (data / 데이터) volume lớn nhưng khó phép nối (join / 조인).

## 20. Lower layers thực sự quyết định trust

Cuối cùng signing key nằm trong software tiến trình (process / 프로세스), TPM/HSM hoặc dịch vụ (service / 서비스); runner chạy trên OS/hypervisor; registry lưu bytes trên lưu trữ (storage / 저장소); mạng (network / 네트워크) mang sản phẩm tạo ra (artifact / 산출물); định danh (identity / 식별자) provider cấp credential. Supply-chain trust không nổi trên phần cứng.

Nếu attacker kiểm soát lower tầng (layer / 계층) có authority đọc signing key hoặc thay verifier, higher-level chính sách (policy / 정책) có thể mất ý nghĩa. Đây không có nghĩa phải trust mọi tầng (layer / 계층) như nhau; nghĩa là threat mô hình (model / 모델) phải nói rõ tầng (layer / 계층) nào nằm trong trusted computing cơ sở (base / 기반).

## 21. Mô hình tư duy (mental model / 사고 모델) cuối

Software supply chuỗi (chain / 사슬) là một **authority đồ thị (graph / 그래프) quanh quá trình biến nguồn (source / 소스) thành executable trạng thái (state / 상태)**. Digest cho định danh (identity / 식별자), provenance cho lịch sử (history / 이력), signature cho cryptographic assertion, SBOM cho inventory, chính sách (policy / 정책) cho enforcement, detection cho bằng chứng (evidence / 증거) và sự cố (incident / 인시던트) phản hồi (response / 응답) cho containment. Không thành phần nào tự đủ.

Khi rà soát (review / 검토) chuỗi xử lý (pipeline / 파이프라인), đừng hỏi “đã bật signing chưa?”. Hãy hỏi: **principal nào có thể thay bytes môi trường vận hành (production / 운영 환경), bằng chứng (evidence / 증거) nào nối bytes đó về nguồn (source / 소스)/bản dựng (build / 빌드), verifier tin ai, trust gốc (root / 루트) có thể bị bypass bằng đường dẫn (path / 경로) nào, và khi một principal bị compromise ta cắt năng lực (capability / 역량) đó nhanh tới đâu?**