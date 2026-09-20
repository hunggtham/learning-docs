# Data Governance for AI

**Data governance (데이터 거버넌스 / quản trị dữ liệu)** là hệ thống policy, ownership, metadata, access control và lifecycle management giúp tổ chức biết data nào tồn tại, ai chịu trách nhiệm, được dùng cho mục đích gì và model nào phụ thuộc vào nó.

Governance không phải paperwork tách rời engineering. Khi AI dùng data để train/deploy, governance trở thành part of reliability, security và compliance.

## Ownership

Mỗi critical dataset/source nên có owner rõ:

```text
business/domain owner
technical data owner
steward / quality owner
security/privacy contact
```

Nếu không ai chịu trách nhiệm semantics, feature definition sẽ drift âm thầm.

## Data Catalog

Catalog lưu metadata:

- dataset name/description;
- schema;
- owner;
- source;
- freshness;
- lineage;
- privacy classification;
- permitted uses;
- quality status;
- retention.

Catalog chỉ hữu ích nếu metadata maintained và searchable.

## Lineage

Lineage graph:

```text
source tables/files
→ ETL/feature jobs
→ training snapshot
→ model version
→ deployment
```

Khi source field bị lỗi, lineage trả lời models nào bị ảnh hưởng.

## Access Control

Least privilege áp dụng data:

```text
who can read raw PII?
who can export?
who can train model?
who can see labels?
```

Role/attribute-based access nên enforcement ở storage/service layer, không qua social convention.

## Purpose Limitation

Data collected for one purpose may not automatically be legitimate for another. Governance records allowed processing purposes và restrictions.

AI experimentation phải respect same constraints as production.

## Data Classification

Common classes:

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

## Encryption

Protect data:

- at rest;
- in transit;
- key management;
- access logging.

Encryption does not solve misuse by authorized user; authorization/audit still needed.

## Retention và Deletion

Retention should be purposeful. Training snapshot immutability conflicts with deletion requests/compliance; model lifecycle needs strategy for data removal and retraining where required.

Deleting raw record does not automatically remove influence from already-trained model.

## Provenance

For external data, record:

- source URL/provider;
- collection date;
- license/terms;
- transformations;
- consent/legal basis where relevant.

Foundation-model era makes provenance increasingly important for copyright, trust and contamination analysis.

## Dataset Versioning

A version should identify exact content + processing config. Semantic version labels alone insufficient without immutable manifest/hash.

```text
dataset_v42
manifest hash
source snapshot ids
transform commit
label schema version
```

## Reproducibility

To reproduce model, need more than code:

```text
training data version
feature code
label version
random seed
model config
software environment
```

Governance provides data half of reproducibility chain.

## Data Contracts

Producer and consumer agree on schema + semantics + SLA + change process. Breaking changes trigger explicit migration instead of silent downstream degradation.

## Privacy Impact

Before using sensitive data, ask:

- is feature necessary?
- can aggregate/pseudonymized form work?
- can computation occur locally?
- retention duration?
- cross-border transfer?
- user expectations?

Data minimization reduces both risk and model shortcut opportunities.

## Pseudonymization vs Anonymization

Replacing name with ID is pseudonymization, not true anonymization. Linkage/re-identification remains possible.

High-dimensional datasets are difficult to anonymize while preserving utility.

## Differential Privacy

Differential Privacy offers formal bound on effect of one record. Roughly, mechanism `M` is `(ε,δ)`-DP if neighboring datasets produce similar output distributions:

\[
P(M(D)\in S)\le e^\epsilon P(M(D')\in S)+\delta
\]

Smaller `ε` stronger privacy but often lower utility/more noise.

DP is mathematical privacy mechanism, not substitute for access/security controls.

## Data Residency

Organizations may require data remain in specific country/region. Cloud/model provider selection and cross-region processing become architecture constraint.

## Vendor Data

Third-party datasets/APIs need due diligence:

- license rights;
- collection method;
- data quality;
- privacy commitments;
- retention;
- model-training permissions;
- change/termination terms.

## Audit Logs

Record who accessed/exported/modified sensitive datasets. Logs themselves sensitive and should be immutable enough for audit use.

## Data Incident Response

If dataset leaked/corrupted:

1. contain access;
2. identify affected data/models;
3. use lineage to find downstream artifacts;
4. invalidate/retrain as needed;
5. preserve evidence;
6. update controls.

## Governance for RAG

RAG index may ingest documents with different ACLs. Retrieval must enforce document permissions **before** results enter model context.

Do not rely on model to hide unauthorized chunk after retrieval.

## Governance for Agent Memory

Persistent memory can become a new data store. It needs retention, deletion, user scope and provenance just like databases.

## Governance for Synthetic Data

Record generator/model/prompt/source dataset. Synthetic label does not erase original licensing/privacy obligations automatically.

## Governance vs Bureaucracy

Bad governance creates manual gates without reducing risk. Good governance creates machine-readable metadata, automated policy checks and clear ownership.

## Data Documentation

Useful artifact:

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

## Mental Model

> **Governance turns data from anonymous files into accountable assets with ownership, provenance, permissions and lifecycle.**

## Common Misconceptions

### “Governance only matters for regulated companies”

Even small systems need lineage/ownership to debug and reproduce.

### “Anonymized dataset is safe forever”

Re-identification risk evolves with auxiliary data.

### “If RAG search engine can access document, model may access it”

User-level authorization still must be enforced.

## Knowledge Connection

Data governance connects Security, Privacy, MLOps, AI Safety and organizational process. It closes the Data layer and prepares for AI Engineering, where models/data become production services.