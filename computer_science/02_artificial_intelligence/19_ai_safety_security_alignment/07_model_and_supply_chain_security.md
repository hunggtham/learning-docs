# Bảo mật mô hình và chuỗi cung ứng AI

> **Mạch đọc:** Đặt **Bảo mật mô hình và chuỗi cung ứng AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Kiến thức cần có trước** sang **Chuỗi cung ứng AI gồm những gì?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Hệ thống AI kế thừa rủi ro của chuỗi cung ứng phần mềm và bổ sung thêm các sản phẩm tạo ra (artifact / 산출물) đặc thù như dataset, checkpoint, tokenizer, adapter, prompt bundle và evaluation assets. **Bảo mật chuỗi cung ứng (supply-chain security)** bảo vệ tính toàn vẹn và khả năng truy vết từ nguồn (source / 소스) → bản dựng (build / 빌드)/train → sản phẩm tạo ra (artifact / 산출물) → registry → triển khai (deployment / 배포).

## Kiến thức cần có trước

Nên đọc [Data Poisoning](./05_data_poisoning_backdoors_and_model_attacks.md), [Model Registry](../16_mlops_and_llmops/03_model_registry.md), [CI/CD/CT](../16_mlops_and_llmops/04_ci_cd_ct_for_ai.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

## Chuỗi cung ứng AI gồm những gì?

Một môi trường vận hành (production / 운영 환경) AI hệ thống (system / 시스템) thường phụ thuộc vào:

```text
source code
packages / dependencies
container images
CUDA / runtime libraries
datasets
pretrained checkpoints
adapters / LoRA
tokenizers
prompt templates
evaluation sets
plugins / tools
CI/CD pipeline
artifact registry
model provider API
```

Một thành phần (component / 컴포넌트) bị compromise có thể thay đổi hành vi (behavior / 동작) mà ứng dụng (application / 애플리케이션) mã (code / 코드) chính không hề đổi.

## Mô hình tin cậy theo sản phẩm tạo ra (artifact / 산출물)

Mỗi sản phẩm tạo ra (artifact / 산출물) môi trường vận hành (production / 운영 환경) cần trả lời được:

```text
nó đến từ đâu?
ai tạo hoặc approve?
phiên bản/digest nào?
dữ liệu và code nào tạo ra nó?
đã qua evaluation nào?
được phép dùng trong môi trường nào?
```

Đây là nền của **provenance** và sự cố (incident / 인시던트) phản hồi (response / 응답).

## Digest bất biến

Tag kiểu `latest` tiện cho con người nhưng không đủ để truy vết. môi trường vận hành (production / 운영 환경) triển khai (deployment / 배포) nên pin sản phẩm tạo ra (artifact / 산출물) bằng định danh (identity / 식별자) bất biến:

```text
model:latest        → alias có thể thay đổi
sha256:...          → identity nội dung bất biến
```

Alias vẫn hữu ích nếu lịch sử (history / 이력) luôn trỏ ngược được tới digest cụ thể.

## Chữ ký và attestation

Digital signature hoặc bản dựng (build / 빌드) attestation giúp xác minh sản phẩm tạo ra (artifact / 산출물) đến từ chuỗi xử lý (pipeline / 파이프라인) được tin cậy và không bị thay đổi sau khi tạo.

Chữ ký **không chứng minh sản phẩm tạo ra (artifact / 산출물) an toàn**; nó chứng minh provenance/integrity tương ứng với trust gốc (root / 루트). Nếu chuỗi xử lý (pipeline / 파이프라인) ký đã bị compromise, sản phẩm tạo ra (artifact / 산출물) xấu vẫn có thể được ký hợp lệ.

## Rủi ro phụ thuộc (dependency / 의존성)

Phụ thuộc (dependency / 의존성) ecosystem có thể gặp:

- typo-squatting;
- gói (package / 패키지) maintainer bị compromise;
- phụ thuộc (dependency / 의존성) bắc cầu có lỗ hổng;
- post-install script nguy hiểm;
- ảnh (image / 이미지) nền chứa CVE;
- gói (package / 패키지) bị thay nội dung dưới cùng phiên bản (version / 버전) nếu registry yếu.

Môi trường vận hành (production / 운영 환경) practice nên gồm lockfile, pinned phiên bản (version / 버전)/digest, vulnerability scanning, registry đáng tin và phụ thuộc (dependency / 의존성) tối thiểu.

## Serialization và custom mã (code / 코드)

Một số mô hình (model / 모델) format hoặc loading đường dẫn (path / 경로) có thể thực thi mã (code / 코드) khi deserialize. Vì vậy “tệp (file / 파일) checkpoint” không mặc định là passive dữ liệu (data / 데이터).

Nên ưu tiên safe tensor format khi có thể, tránh `trust_remote_code` hoặc custom loader không cần thiết và dùng sandbox cho sản phẩm tạo ra (artifact / 산출물) chưa được tin cậy.

## Checkpoint và adapter của bên thứ ba

Trước khi dùng checkpoint hoặc adapter ngoài tổ chức:

```text
xác minh nguồn
kiểm tra digest/license
xem metadata
tránh code tùy chỉnh không cần thiết
load trong môi trường cô lập
chạy quality + security regression
chỉ promote qua registry sau approval
```

Adapter nhỏ vẫn có khả năng thay đổi hành vi (behavior / 동작) lớn; kích thước tệp (file / 파일) không tương ứng với mức rủi ro.

## Dataset cũng là supply-chain sản phẩm tạo ra (artifact / 산출물)

Dataset bên thứ ba cần provenance, license, collection phương thức (method / 메서드), chất lượng (quality / 품질) và poisoning rà soát (review / 검토). huấn luyện (training / 학습) manifest phải trỏ được tới snapshot chính xác.

Nếu dataset URL bị cập nhật âm thầm, cùng mã (code / 코드) huấn luyện (training / 학습) có thể tạo mô hình (model / 모델) khác. Vì vậy URL không phải định danh (identity / 식별자) đủ mạnh.

## Prompt và chính sách (policy / 정책) cũng cần versioning

Trong LLM ứng dụng (application / 애플리케이션), hệ thống (system / 시스템) prompt, công cụ (tool / 도구) lược đồ (schema / 스키마), chính sách (policy / 정책) template và ngữ cảnh (context / 맥락) assembly đều tác động hành vi (behavior / 동작). Chúng cần rà soát mã (code review / 코드 리뷰), versioning và regression kiểm thử (test / 테스트) giống sản phẩm tạo ra (artifact / 산출물) khác.

Một sửa đổi prompt trực tiếp trong dashboard mà không có lịch sử (history / 이력) tạo ra hidden trạng thái (state / 상태) trong môi trường vận hành (production / 운영 환경).

## Công cụ (tool / 도구) và plugin supply chuỗi (chain / 사슬)

Tác nhân (agent / 에이전트) công cụ (tool / 도구) có thể có mạng (network / 네트워크)/tệp (file / 파일)/cơ sở dữ liệu (database / 데이터베이스) permission. Một công cụ (tool / 도구) bị compromise có thể vượt qua toàn bộ model-level an toàn (safety / 안전).

Nên dùng:

- allowlist;
- permission phạm vi (scope / 범위) hẹp;
- rà soát mã (code review / 코드 리뷰);
- sandbox;
- mạng (network / 네트워크) allowlist;
- lược đồ (schema / 스키마)/chính sách (policy / 정책) kiểm tra hợp lệ (validation / 검증);
- phiên bản (version / 버전) pinning.

## CI/CD là ranh giới bảo mật (security boundary / 보안 경계)

Nếu attacker điều khiển bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인), họ có thể phát hành sản phẩm tạo ra (artifact / 산출물) xấu ngay cả khi nguồn (source / 소스) repo sạch.

Bảo vệ chuỗi xử lý (pipeline / 파이프라인) bằng:

```text
branch / review policy
least-privilege token
ephemeral credential
isolated runner
audit log
artifact signing
separation of duties
```

Môi trường vận hành (production / 운영 환경) nên lấy sản phẩm tạo ra (artifact / 산출물) từ registry được approve thay vì bản dựng (build / 빌드) trực tiếp từ nguồn (source / 소스) mỗi lần deploy.

## Promote cùng một sản phẩm tạo ra (artifact / 산출물) qua môi trường

Một mẫu (pattern / 패턴) an toàn là bản dựng (build / 빌드)/train sản phẩm tạo ra (artifact / 산출물) một lần rồi promote cùng digest từ staging sang môi trường vận hành (production / 운영 환경). Nếu rebuild riêng cho từng môi trường (environment / 환경), nội dung có thể khác dù phiên bản (version / 버전) label giống nhau.

Cấu hình (configuration / 구성) theo môi trường (environment / 환경) vẫn có thể thay đổi, nhưng phải được phiên bản (version / 버전) và dấu vết (trace / 추적) riêng.

## SBOM và AI Bill of Materials

**Software Bill of Materials (SBOM)** ghi các gói (package / 패키지)/phần mềm. Với AI có thể mở rộng thành danh sách thành phần của hành vi (behavior / 동작) bundle:

```text
base model
dataset versions
adapters
tokenizer
runtime
prompt bundle
embedding model
retrieval index schema
tool versions
evaluation suite
```

Mục tiêu là impact phân tích (analysis / 분석): khi một thành phần (component / 컴포넌트) có vấn đề, biết triển khai (deployment / 배포) nào bị ảnh hưởng.

## Mô hình triển khai môi trường vận hành (production / 운영 환경)

Một đường phát hành đáng tin cậy:

```text
source + data + config
→ controlled build/train
→ immutable artifact
→ digest + signature/attestation
→ registry
→ evaluation/security gate
→ staging
→ canary/shadow
→ production
→ monitoring
```

Mỗi bước cần siêu dữ liệu (metadata / 메타데이터) để nối thành lineage.

## Rủi ro từ provider bên ngoài

Hosted LLM/embedding API là phụ thuộc (dependency / 의존성) bên ngoài. Cần theo dõi:

- mô hình (model / 모델)/phiên bản (version / 버전) hoặc alias ngữ nghĩa (semantics / 의미론);
- SLA;
- data-processing chính sách (policy / 정책);
- retention;
- region/residency;
- deprecation timeline;
- fallback/exit chiến lược (strategy / 전략).

Provider cập nhật (update / 업데이트) có thể thay hành vi (behavior / 동작) mà cục bộ (local / 로컬) mã (code / 코드) không đổi, vì vậy LLMOps phải coi provider định danh (identity / 식별자) là một phần của hành vi (behavior / 동작) bundle.

## Secret trong bản dựng (build / 빌드) và huấn luyện (training / 학습)

Notebook, CI log hoặc cấu hình (config / 설정) có thể vô tình chứa API key. Secret scanner, bên ngoài (external / 외부) secret manager và credential ngắn hạn giúp giảm rủi ro.

Sản phẩm tạo ra (artifact / 산출물) không nên chứa credential có thể tái sử dụng ở môi trường vận hành (production / 운영 환경).

## Mô hình (model / 모델) theft và sản phẩm tạo ra (artifact / 산출물) truy cập (access / 접근)

Weights hoặc adapter có thể là tài sản nhạy cảm. Registry cần kiểm soát truy cập (access control / 접근 제어), kiểm tra (audit / 감사), encryption và hạn chế export phù hợp. Tuy nhiên việc “giấu mô hình (model / 모델)” không thay thế các defense ở suy luận (inference / 추론) đường dẫn (path / 경로).

## Reproducibility và bảo mật (security / 보안)

ML huấn luyện (training / 학습) không phải lúc nào cũng bitwise reproducible, nhưng cần đủ siêu dữ liệu (metadata / 메타데이터) để tái tạo provenance:

```text
code SHA
dataset manifest
container/runtime
config
seed
hardware class
training run ID
artifact digest
```

Reproducibility hỗ trợ forensic investigation khi cần chứng minh mô hình (model / 모델) đến từ chuỗi xử lý (pipeline / 파이프라인) nào.

## Dạng thất bại (failure mode / 실패 모드) thường gặp

**Mutable tag.** môi trường vận hành (production / 운영 환경) chạy `latest`, không biết chính xác sản phẩm tạo ra (artifact / 산출물) nào đang serve.

**Checkpoint tải (load / 로드) custom mã (code / 코드).** sản phẩm tạo ra (artifact / 산출물) “mô hình (model / 모델)” mở rộng attack surface thành mã (code / 코드) thực thi (execution / 실행).

**CI đơn vị từ (token / 토큰) quá mạnh.** Runner bị compromise có thể ghi thẳng môi trường vận hành (production / 운영 환경) registry.

**Adapter không qua gate.** nhóm (team / 팀) coi LoRA là thay đổi nhỏ nên bỏ bảo mật (security / 보안) eval.

**Dataset provenance mất.** Không thể xác định mô hình (model / 모델) nào dùng nguồn dữ liệu bị poison.

**Provider alias đổi hành vi.** Không có regression monitor hoặc quay lui (rollback / 롤백) bundle.

**Rebuild khi deploy.** sản phẩm tạo ra (artifact / 산출물) staging và môi trường vận hành (production / 운영 환경) không còn cùng định danh (identity / 식별자).

## Ứng phó lỗ hổng chuỗi cung ứng

Khi một gói (package / 패키지), mô hình (model / 모델) hoặc dataset bị báo có vấn đề:

```text
1. xác định component/digest bị ảnh hưởng
2. truy lineage để tìm model/deployment liên quan
3. chặn promotion mới
4. rollback hoặc disable artifact bị ảnh hưởng
5. patch/rebuild từ nguồn tin cậy
6. chạy lại quality + security evaluation
7. rollout có kiểm soát
8. xác minh artifact cũ đã bị retire khi cần
```

Không có provenance thì bước 2 trở thành điều tra thủ công chậm và dễ sót.

## Sự đánh đổi (trade-off / 트레이드오프)

Ký sản phẩm tạo ra (artifact / 산출물), giữ immutable snapshot và bảo mật (security / 보안) gate làm tăng lưu trữ (storage / 저장소), compute và thời gian bản phát hành (release / 릴리스). Tuy nhiên chúng giảm đáng kể chi phí (cost / 비용) của quay lui (rollback / 롤백), kiểm tra (audit / 감사) và sự cố (incident / 인시던트) investigation.

Không phải mọi thử nghiệm notebook đều cần chuỗi xử lý (pipeline / 파이프라인) enterprise, nhưng sản phẩm tạo ra (artifact / 산출물) được promote lên môi trường vận hành (production / 운영 환경) phải có định danh (identity / 식별자) và provenance đủ mạnh tương ứng với impact.

## Mô hình tư duy

> **Bảo mật chuỗi cung ứng AI là biết chính xác mình đang chạy cái gì, nó đến từ đâu, ai được phép thay đổi nó và bằng chứng nào cho phép nó được promote.**

## Những nhầm lẫn thường gặp

### “Checkpoint không phải executable nên an toàn”

Không. Serialization/custom loader có thể thực thi mã (code / 코드), và weights cũng có thể mang backdoor hành vi (behavior / 동작).

### “Pin phiên bản (version / 버전) là đủ”

Không. Phiên bản bị compromise vẫn nguy hiểm; cần integrity/provenance và vulnerability phản hồi (response / 응답).

### “nguồn (source / 소스) repo sạch nghĩa sản phẩm tạo ra (artifact / 산출물) môi trường vận hành (production / 운영 환경) sạch”

Không. bản dựng (build / 빌드) runner, registry hoặc phụ thuộc (dependency / 의존성) có thể bị compromise riêng.

### “Dùng hosted API thì không có supply-chain rủi ro (risk / 위험)”

Không. Provider mô hình (model / 모델)/phiên bản (version / 버전) và chính sách (policy / 정책) vẫn là bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) ảnh hưởng hành vi (behavior / 동작).

## Liên kết kiến thức

Nên đọc cùng [Data Poisoning](./05_data_poisoning_backdoors_and_model_attacks.md), [Model Registry](../16_mlops_and_llmops/03_model_registry.md), [CI/CD/CT](../16_mlops_and_llmops/04_ci_cd_ct_for_ai.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md), [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 ai safety foundations](./00_ai_safety_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
