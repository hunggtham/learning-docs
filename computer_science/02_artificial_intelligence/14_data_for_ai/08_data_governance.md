# Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Quyền sở hữu (ownership / 소유권)** chỉ đường quay lại owner và tài liệu chuẩn khi cần đào sâu; sau đó sang **Dữ liệu (data / 데이터) danh mục (catalog / 카탈로그)** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**dữ liệu (data / 데이터) quản trị (governance / 거버넌스)** là hệ thống chính sách (policy / 정책), quyền sở hữu (ownership / 소유권), siêu dữ liệu (metadata / 메타데이터), kiểm soát truy cập (access control / 접근 제어) và vòng đời (lifecycle / 생명주기) management giúp tổ chức biết dữ liệu (data / 데이터) nào tồn tại, ai chịu trách nhiệm, được dùng cho mục đích gì và mô hình (model / 모델) nào phụ thuộc vào nó.

Quản trị (governance / 거버넌스) không phải paperwork tách rời kỹ thuật (engineering / 엔지니어링). Khi AI dùng dữ liệu (data / 데이터) để train/deploy, quản trị (governance / 거버넌스) trở thành part of độ tin cậy (reliability / 신뢰성), bảo mật (security / 보안) và compliance.

## Quyền sở hữu (ownership / 소유권)

Mỗi trọng yếu (critical / 중요) dataset/nguồn (source / 소스) nên có đơn vị sở hữu (owner / 오너) rõ:

```text
business/domain owner
technical data owner
steward / quality owner
security/privacy contact
```

Nếu không ai chịu trách nhiệm ngữ nghĩa (semantics / 의미론), tính năng (feature / 기능) definition sẽ drift âm thầm.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Quyền sở hữu (ownership / 소유권)** nêu điều cần giải thích; **Dữ liệu (data / 데이터) danh mục (catalog / 카탈로그)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Lineage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) danh mục (catalog / 카탈로그)

Danh mục (catalog / 카탈로그) lưu siêu dữ liệu (metadata / 메타데이터):

- dataset name/description;
- lược đồ (schema / 스키마);
- đơn vị sở hữu (owner / 오너);
- nguồn (source / 소스);
- freshness;
- lineage;
- privacy classification;
- permitted uses;
- chất lượng (quality / 품질) status;
- retention.

Danh mục (catalog / 카탈로그) chỉ hữu ích nếu siêu dữ liệu (metadata / 메타데이터) maintained và searchable.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Dữ liệu (data / 데이터) danh mục (catalog / 카탈로그)** nêu điều cần giải thích; **Lineage** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Kiểm soát truy cập (access control / 접근 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lineage

Lineage đồ thị (graph / 그래프):

```text
source tables/files
→ ETL/feature jobs
→ training snapshot
→ model version
→ deployment
```

Khi nguồn (source / 소스) trường dữ liệu (field / 필드) bị lỗi, lineage trả lời các mô hình (models / 모델들) nào bị ảnh hưởng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Kiểm soát truy cập (access control / 접근 제어)** tiếp nhận điểm tựa từ **Lineage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Purpose Limitation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm soát truy cập (access control / 접근 제어)

Least privilege áp dụng dữ liệu (data / 데이터):

```text
who can read raw PII?
who can export?
who can train model?
who can see labels?
```

Role/attribute-based truy cập (access / 접근) nên enforcement ở lưu trữ (storage / 저장소)/dịch vụ (service / 서비스) tầng (layer / 계층), không qua xã hội (social / 사회적) convention.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Kiểm soát truy cập (access control / 접근 제어)** đã nêu tiêu chí phân biệt, còn **Purpose Limitation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Dữ liệu (data / 데이터) Classification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Purpose Limitation

Dữ liệu (data / 데이터) collected for one purpose may not automatically be legitimate for another. quản trị (governance / 거버넌스) records allowed processing purposes và restrictions.

AI experimentation phải respect same các ràng buộc (constraints / 제약조건들) as môi trường vận hành (production / 운영 환경).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Purpose Limitation** đã nêu tiêu chí phân biệt, còn **Dữ liệu (data / 데이터) Classification** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Encryption** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Classification

Dùng chung (common / 공통) classes:

```text
public
internal
confidential
personal data
sensitive personal data
secrets/credentials
regulated domain data
```

Classification drives encryption, retention và sharing policies.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Dữ liệu (data / 데이터) Classification** nêu điều cần giải thích; **Encryption** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Retention và Deletion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Encryption

Protect dữ liệu (data / 데이터):

- at rest;
- in transit;
- key management;
- truy cập (access / 접근) logging.

Encryption does not solve misuse by authorized người dùng (user / 사용자); authorization/kiểm tra (audit / 감사) still needed.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Retention và Deletion** tiếp nhận điểm tựa từ **Encryption** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Provenance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Retention và Deletion

Retention should be purposeful. huấn luyện (training / 학습) snapshot immutability conflicts with deletion requests/compliance; mô hình (model / 모델) vòng đời (lifecycle / 생명주기) needs chiến lược (strategy / 전략) for dữ liệu (data / 데이터) removal and retraining where required.

Deleting raw bản ghi (record / 레코드) does not automatically remove influence from already-trained mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Provenance** tiếp nhận điểm tựa từ **Retention và Deletion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dataset Versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Provenance

For bên ngoài (external / 외부) dữ liệu (data / 데이터), bản ghi (record / 레코드):

- nguồn (source / 소스) URL/provider;
- collection date;
- license/terms;
- transformations;
- consent/legal basis where relevant.

Foundation-model era makes provenance increasingly important for copyright, trust and contamination phân tích (analysis / 분석).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Dataset Versioning** tiếp nhận điểm tựa từ **Provenance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reproducibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dataset Versioning

A phiên bản (version / 버전) should identify chính xác (exact / 정확한) content + processing cấu hình (config / 설정). ngữ nghĩa (semantic / 의미적) phiên bản (version / 버전) labels alone insufficient without immutable manifest/băm (hash / 해시).

```text
dataset_v42
manifest hash
source snapshot ids
transform commit
label schema version
```

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Reproducibility** tiếp nhận điểm tựa từ **Dataset Versioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Contracts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reproducibility

To reproduce mô hình (model / 모델), need more than mã (code / 코드):

```text
training data version
feature code
label version
random seed
model config
software environment
```

Quản trị (governance / 거버넌스) provides dữ liệu (data / 데이터) half of reproducibility chuỗi (chain / 사슬).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Reproducibility** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Contracts** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Privacy Impact** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Contracts

Producer and bên tiêu thụ (consumer / 소비자) agree on lược đồ (schema / 스키마) + ngữ nghĩa (semantics / 의미론) + SLA + thay đổi (change / 변경) tiến trình (process / 프로세스). Breaking changes trigger tường minh (explicit / 명시적) di chuyển (migration / 마이그레이션) instead of silent downstream degradation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Dữ liệu (data / 데이터) Contracts** nêu điều cần giải thích; **Privacy Impact** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Pseudonymization vs Anonymization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Privacy Impact

Before using sensitive dữ liệu (data / 데이터), ask:

- is tính năng (feature / 기능) necessary?
- can aggregate/pseudonymized form công việc (work / 작업)?
- can computation occur locally?
- retention duration?
- cross-border transfer?
- người dùng (user / 사용자) expectations?

Dữ liệu (data / 데이터) minimization reduces both rủi ro (risk / 위험) and mô hình (model / 모델) shortcut opportunities.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Pseudonymization vs Anonymization** tiếp nhận điểm tựa từ **Privacy Impact** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differential Privacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pseudonymization vs Anonymization

Replacing name with ID is pseudonymization, not true anonymization. Linkage/re-identification remains possible.

High-dimensional datasets are difficult to anonymize while preserving utility.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Differential Privacy** tiếp nhận điểm tựa từ **Pseudonymization vs Anonymization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Residency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differential Privacy

Differential Privacy offers formal bound on tác động (effect / 효과) of one bản ghi (record / 레코드). Roughly, cơ chế (mechanism / 메커니즘) `M` is `(ε,δ)`-DP if neighboring datasets produce similar đầu ra (output / 출력) distributions:

\[
P(M(D)\in S)\le e^\epsilon P(M(D')\in S)+\delta
\]

Smaller `ε` stronger privacy but often lower utility/more noise.

DP is mathematical privacy cơ chế (mechanism / 메커니즘), not substitute for truy cập (access / 접근)/bảo mật (security / 보안) controls.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Differential Privacy** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Residency** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Vendor dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Residency

Organizations may require dữ liệu (data / 데이터) remain in specific country/region. Cloud/mô hình (model / 모델) provider selection and cross-region processing become kiến trúc (architecture / 아키텍처) ràng buộc (constraint / 제약조건).

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Dữ liệu (data / 데이터) Residency** nêu điều cần giải thích; **Vendor dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Kiểm tra (audit / 감사) Logs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vendor dữ liệu (data / 데이터)

Third-party datasets/APIs need due diligence:

- license rights;
- collection phương thức (method / 메서드);
- dữ liệu (data / 데이터) chất lượng (quality / 품질);
- privacy commitments;
- retention;
- model-training permissions;
- thay đổi (change / 변경)/termination terms.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Vendor dữ liệu (data / 데이터)** nêu điều cần giải thích; **Kiểm tra (audit / 감사) Logs** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Dữ liệu (data / 데이터) sự cố (incident / 인시던트) phản hồi (response / 응답)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm tra (audit / 감사) Logs

Bản ghi (record / 레코드) who accessed/exported/modified sensitive datasets. Logs themselves sensitive and should be immutable enough for kiểm tra (audit / 감사) use.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Kiểm tra (audit / 감사) Logs** nêu điều cần giải thích; **Dữ liệu (data / 데이터) sự cố (incident / 인시던트) phản hồi (response / 응답)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quản trị (governance / 거버넌스) for RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) sự cố (incident / 인시던트) phản hồi (response / 응답)

If dataset leaked/corrupted:

1. contain truy cập (access / 접근);
2. identify affected dữ liệu (data / 데이터)/các mô hình (models / 모델들);
3. use lineage to find downstream artifacts;
4. invalidate/retrain as needed;
5. preserve bằng chứng (evidence / 증거);
6. cập nhật (update / 업데이트) controls.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Dữ liệu (data / 데이터) sự cố (incident / 인시던트) phản hồi (response / 응답)** nêu điều cần giải thích; **Quản trị (governance / 거버넌스) for RAG** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quản trị (governance / 거버넌스) for tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quản trị (governance / 거버넌스) for RAG

RAG chỉ mục (index / 인덱스) may ingest documents with different ACLs. Retrieval must enforce document permissions **before** results enter mô hình (model / 모델) ngữ cảnh (context / 맥락).

Do not rely on mô hình (model / 모델) to hide unauthorized chunk after retrieval.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Quản trị (governance / 거버넌스) for tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Quản trị (governance / 거버넌스) for RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quản trị (governance / 거버넌스) for Synthetic dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quản trị (governance / 거버넌스) for tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)

Persistent bộ nhớ (memory / 메모리) can become a new dữ liệu (data / 데이터) store. It needs retention, deletion, người dùng (user / 사용자) phạm vi (scope / 범위) and provenance just like databases.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Quản trị (governance / 거버넌스) for tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)** nêu điều cần giải thích; **Quản trị (governance / 거버넌스) for Synthetic dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quản trị (governance / 거버넌스) vs Bureaucracy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quản trị (governance / 거버넌스) for Synthetic dữ liệu (data / 데이터)

Bản ghi (record / 레코드) generator/mô hình (model / 모델)/prompt/nguồn (source / 소스) dataset. Synthetic label does not erase original licensing/privacy obligations automatically.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Quản trị (governance / 거버넌스) for Synthetic dữ liệu (data / 데이터)** nêu điều cần giải thích; **Quản trị (governance / 거버넌스) vs Bureaucracy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Dữ liệu (data / 데이터) Documentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quản trị (governance / 거버넌스) vs Bureaucracy

Bad quản trị (governance / 거버넌스) creates manual gates without reducing rủi ro (risk / 위험). Good quản trị (governance / 거버넌스) creates machine-readable siêu dữ liệu (metadata / 메타데이터), automated chính sách (policy / 정책) checks and clear quyền sở hữu (ownership / 소유권).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Quản trị (governance / 거버넌스) vs Bureaucracy** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Documentation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Documentation

Useful sản phẩm tạo ra (artifact / 산출물):

```text
Dataset Card
- purpose
- population
- collection
- label process
- known limitations
- sensitive fields
- license
- recommended / prohibited uses
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, các dấu vết trong **Dữ liệu (data / 데이터) Documentation** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **quản trị (governance / 거버넌스) turns dữ liệu (data / 데이터) from anonymous files into accountable assets with quyền sở hữu (ownership / 소유권), provenance, permissions and vòng đời (lifecycle / 생명주기).**

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “quản trị (governance / 거버넌스) only matters for regulated companies”

Even small các hệ thống (systems / 시스템들) need lineage/quyền sở hữu (ownership / 소유권) to gỡ lỗi (debug / 디버그) and reproduce.

### “Anonymized dataset is safe forever”

Re-identification rủi ro (risk / 위험) evolves with auxiliary dữ liệu (data / 데이터).

### “If RAG tìm kiếm (search / 검색) engine can truy cập (access / 접근) document, mô hình (model / 모델) may truy cập (access / 접근) it”

User-level authorization still must be enforced.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) for AI**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Dữ liệu (data / 데이터) quản trị (governance / 거버넌스) connects bảo mật (security / 보안), Privacy, MLOps, AI an toàn (safety / 안전) and organizational tiến trình (process / 프로세스). It closes the dữ liệu (data / 데이터) tầng (layer / 계층) and prepares for AI kỹ thuật (engineering / 엔지니어링), where các mô hình (models / 모델들)/dữ liệu (data / 데이터) become môi trường vận hành (production / 운영 환경) services.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
