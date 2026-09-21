# Bảo mật mô hình và chuỗi cung ứng AI

Hệ thống AI kế thừa rủi ro của chuỗi cung ứng phần mềm và bổ sung thêm các artifact đặc thù như dataset, checkpoint, tokenizer, adapter, prompt bundle và evaluation assets. **Bảo mật chuỗi cung ứng (supply-chain security)** bảo vệ tính toàn vẹn và khả năng truy vết từ source → build/train → artifact → registry → deployment.

## Kiến thức cần có trước

Nên đọc [Data Poisoning](./05_data_poisoning_backdoors_and_model_attacks.md), [Model Registry](../16_mlops_and_llmops/03_model_registry.md), [CI/CD/CT](../16_mlops_and_llmops/04_ci_cd_ct_for_ai.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

## Chuỗi cung ứng AI gồm những gì?

Một production AI system thường phụ thuộc vào:

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

Một component bị compromise có thể thay đổi behavior mà application code chính không hề đổi.

## Mô hình tin cậy theo artifact

Mỗi artifact production cần trả lời được:

```text
nó đến từ đâu?
ai tạo hoặc approve?
phiên bản/digest nào?
dữ liệu và code nào tạo ra nó?
đã qua evaluation nào?
được phép dùng trong môi trường nào?
```

Đây là nền của **provenance** và incident response.

## Digest bất biến

Tag kiểu `latest` tiện cho con người nhưng không đủ để truy vết. Production deployment nên pin artifact bằng identity bất biến:

```text
model:latest        → alias có thể thay đổi
sha256:...          → identity nội dung bất biến
```

Alias vẫn hữu ích nếu history luôn trỏ ngược được tới digest cụ thể.

## Chữ ký và attestation

Digital signature hoặc build attestation giúp xác minh artifact đến từ pipeline được tin cậy và không bị thay đổi sau khi tạo.

Chữ ký **không chứng minh artifact an toàn**; nó chứng minh provenance/integrity tương ứng với trust root. Nếu pipeline ký đã bị compromise, artifact xấu vẫn có thể được ký hợp lệ.

## Rủi ro dependency

Dependency ecosystem có thể gặp:

- typo-squatting;
- package maintainer bị compromise;
- dependency bắc cầu có lỗ hổng;
- post-install script nguy hiểm;
- image nền chứa CVE;
- package bị thay nội dung dưới cùng version nếu registry yếu.

Production practice nên gồm lockfile, pinned version/digest, vulnerability scanning, registry đáng tin và dependency tối thiểu.

## Serialization và custom code

Một số model format hoặc loading path có thể thực thi code khi deserialize. Vì vậy “file checkpoint” không mặc định là passive data.

Nên ưu tiên safe tensor format khi có thể, tránh `trust_remote_code` hoặc custom loader không cần thiết và dùng sandbox cho artifact chưa được tin cậy.

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

Adapter nhỏ vẫn có khả năng thay đổi behavior lớn; kích thước file không tương ứng với mức rủi ro.

## Dataset cũng là supply-chain artifact

Dataset bên thứ ba cần provenance, license, collection method, quality và poisoning review. Training manifest phải trỏ được tới snapshot chính xác.

Nếu dataset URL bị cập nhật âm thầm, cùng code training có thể tạo model khác. Vì vậy URL không phải identity đủ mạnh.

## Prompt và policy cũng cần versioning

Trong LLM application, system prompt, tool schema, policy template và context assembly đều tác động behavior. Chúng cần code review, versioning và regression test giống artifact khác.

Một sửa đổi prompt trực tiếp trong dashboard mà không có history tạo ra hidden state trong production.

## Tool và plugin supply chain

Agent tool có thể có network/file/database permission. Một tool bị compromise có thể vượt qua toàn bộ model-level safety.

Nên dùng:

- allowlist;
- permission scope hẹp;
- code review;
- sandbox;
- network allowlist;
- schema/policy validation;
- version pinning.

## CI/CD là security boundary

Nếu attacker điều khiển build pipeline, họ có thể phát hành artifact xấu ngay cả khi source repo sạch.

Bảo vệ pipeline bằng:

```text
branch / review policy
least-privilege token
ephemeral credential
isolated runner
audit log
artifact signing
separation of duties
```

Production nên lấy artifact từ registry được approve thay vì build trực tiếp từ source mỗi lần deploy.

## Promote cùng một artifact qua môi trường

Một pattern an toàn là build/train artifact một lần rồi promote cùng digest từ staging sang production. Nếu rebuild riêng cho từng environment, nội dung có thể khác dù version label giống nhau.

Configuration theo environment vẫn có thể thay đổi, nhưng phải được version và trace riêng.

## SBOM và AI Bill of Materials

**Software Bill of Materials (SBOM)** ghi các package/phần mềm. Với AI có thể mở rộng thành danh sách thành phần của behavior bundle:

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

Mục tiêu là impact analysis: khi một component có vấn đề, biết deployment nào bị ảnh hưởng.

## Mô hình triển khai production

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

Mỗi bước cần metadata để nối thành lineage.

## Rủi ro từ provider bên ngoài

Hosted LLM/embedding API là dependency bên ngoài. Cần theo dõi:

- model/version hoặc alias semantics;
- SLA;
- data-processing policy;
- retention;
- region/residency;
- deprecation timeline;
- fallback/exit strategy.

Provider update có thể thay behavior mà local code không đổi, vì vậy LLMOps phải coi provider identity là một phần của behavior bundle.

## Secret trong build và training

Notebook, CI log hoặc config có thể vô tình chứa API key. Secret scanner, external secret manager và credential ngắn hạn giúp giảm rủi ro.

Artifact không nên chứa credential có thể tái sử dụng ở production.

## Model theft và artifact access

Weights hoặc adapter có thể là tài sản nhạy cảm. Registry cần access control, audit, encryption và hạn chế export phù hợp. Tuy nhiên việc “giấu model” không thay thế các defense ở inference path.

## Reproducibility và security

ML training không phải lúc nào cũng bitwise reproducible, nhưng cần đủ metadata để tái tạo provenance:

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

Reproducibility hỗ trợ forensic investigation khi cần chứng minh model đến từ pipeline nào.

## Failure mode thường gặp

**Mutable tag.** Production chạy `latest`, không biết chính xác artifact nào đang serve.

**Checkpoint load custom code.** Artifact “model” mở rộng attack surface thành code execution.

**CI token quá mạnh.** Runner bị compromise có thể ghi thẳng production registry.

**Adapter không qua gate.** Team coi LoRA là thay đổi nhỏ nên bỏ security eval.

**Dataset provenance mất.** Không thể xác định model nào dùng nguồn dữ liệu bị poison.

**Provider alias đổi hành vi.** Không có regression monitor hoặc rollback bundle.

**Rebuild khi deploy.** Artifact staging và production không còn cùng identity.

## Ứng phó lỗ hổng chuỗi cung ứng

Khi một package, model hoặc dataset bị báo có vấn đề:

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

## Trade-off

Ký artifact, giữ immutable snapshot và security gate làm tăng storage, compute và thời gian release. Tuy nhiên chúng giảm đáng kể cost của rollback, audit và incident investigation.

Không phải mọi thử nghiệm notebook đều cần pipeline enterprise, nhưng artifact được promote lên production phải có identity và provenance đủ mạnh tương ứng với impact.

## Mô hình tư duy

> **Bảo mật chuỗi cung ứng AI là biết chính xác mình đang chạy cái gì, nó đến từ đâu, ai được phép thay đổi nó và bằng chứng nào cho phép nó được promote.**

## Những nhầm lẫn thường gặp

### “Checkpoint không phải executable nên an toàn”

Không. Serialization/custom loader có thể thực thi code, và weights cũng có thể mang backdoor behavior.

### “Pin version là đủ”

Không. Phiên bản bị compromise vẫn nguy hiểm; cần integrity/provenance và vulnerability response.

### “Source repo sạch nghĩa artifact production sạch”

Không. Build runner, registry hoặc dependency có thể bị compromise riêng.

### “Dùng hosted API thì không có supply-chain risk”

Không. Provider model/version và policy vẫn là external dependency ảnh hưởng behavior.

## Liên kết kiến thức

Nên đọc cùng [Data Poisoning](./05_data_poisoning_backdoors_and_model_attacks.md), [Model Registry](../16_mlops_and_llmops/03_model_registry.md), [CI/CD/CT](../16_mlops_and_llmops/04_ci_cd_ct_for_ai.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md), [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md) và [Secure AI System Design](./08_secure_ai_system_design.md).