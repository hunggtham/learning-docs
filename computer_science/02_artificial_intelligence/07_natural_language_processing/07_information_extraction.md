# Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng

> **Mạch đọc:** Đặt **thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Named thực thể (entity / 엔터티) Recognition** sang **thực thể (entity / 엔터티) Types phụ thuộc lĩnh vực (domain / 도메인)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Thông tin (information / 정보) Extraction (IE / 정보 추출 / trích xuất thông tin) chuyển unstructured văn bản (text / 텍스트) thành structured facts/spans/relations/events. Đây là cầu nối giữa NLP và cơ sở dữ liệu (database / 데이터베이스)/kiến thức (knowledge / 지식) đồ thị (graph / 그래프)/nghiệp vụ (business / 비즈니스) workflow.

Thay vì hỏi “mô hình (model / 모델) hiểu câu không?”, IE đặt đầu ra (output / 출력) lược đồ (schema / 스키마) rõ: thực thể (entity / 엔터티) nào xuất hiện, thuộc loại gì, quan hệ (relation / 관계) nào giữa chúng, sự kiện (event / 이벤트) nào xảy ra, trường dữ liệu (field / 필드) nào cần điền.

## Named thực thể (entity / 엔터티) Recognition

NER gán spans types:

```text
Shinhan Bank opened an office in Seoul.
[Shinhan Bank]ORG ... [Seoul]LOC
```

Classical đơn vị từ (token / 토큰) tagging dùng BIO labels:

```text
Shinhan B-ORG
Bank    I-ORG
opened  O
...
Seoul   B-LOC
```

Subword tokenization complicates alignment; evaluation nên entity-span mức (level / 수준) thay đơn vị từ (token / 토큰) accuracy.

## Thực thể (entity / 엔터티) Types phụ thuộc lĩnh vực (domain / 도메인)

General NER: PERSON, ORG, LOCATION.

Finance: ACCOUNT, sản phẩm (product / 제품), giao dịch (transaction / 트랜잭션), AMOUNT.

Medical: DISEASE, DRUG, DOSAGE.

Lược đồ (schema / 스키마) thiết kế (design / 설계) defines what “correct extraction” means. Too broad loses utility; too granular creates annotation inconsistency.

## Chuỗi (sequence / 시퀀스) Labeling

Transformer encoder gives `h_i`; classifier predicts label each đơn vị từ (token / 토큰).

Independent đơn vị từ (token / 토큰) softmax may produce invalid sequences (`I-PER` without `B-PER`). CRF tầng (layer / 계층) các mô hình (models / 모델들) chuyển tiếp (transition / 전이) các ràng buộc (constraints / 제약조건들) jointly.

Hiện đại (modern / 현대적) large encoders often perform well without CRF, but structured decoding can still help small/lĩnh vực (domain / 도메인) tasks.

## Quan hệ (relation / 관계) Extraction

Given entities, predict quan hệ (relation / 관계):

```text
[Company A] acquired [Company B]
```

→ `ACQUIRED_BY/ACQUIRED` edge depending lược đồ (schema / 스키마).

Methods:

- classify thực thể (entity / 엔터티) pair using contextual biểu diễn (representation / 표현);
- span-pair scoring;
- joint thực thể (entity / 엔터티)+quan hệ (relation / 관계) extraction;
- generative structured đầu ra (output / 출력).

Quan hệ (relation / 관계) direction matters.

## Sự kiện (event / 이벤트) Extraction

Sự kiện (event / 이벤트) has trigger + arguments.

Example:

```text
Samsung acquired X for $2B in 2025.
```

Sự kiện (event / 이벤트):

```json
{
  "type": "Acquisition",
  "buyer": "Samsung",
  "target": "X",
  "amount": "$2B",
  "date": "2025"
}
```

Sự kiện (event / 이벤트) extraction needs role assignment and sometimes cross-sentence ngữ cảnh (context / 맥락).

## Coreference Resolution

```text
Alice joined Acme. She became CTO.
```

`She` refers Alice.

Coreference creates thực thể (entity / 엔터티) clusters across mentions, essential for document-level kiến thức (knowledge / 지식) extraction.

LLMs handle many cases via ngữ cảnh (context / 맥락) but formal coreference evaluation still useful.

## Slot Filling

Nghiệp vụ (business / 비즈니스) documents often need fields:

```text
invoice_number
seller
buyer
total_amount
due_date
```

This is constrained extraction. OCR/bố cục (layout / 레이아웃) + NLP may be needed for scanned documents.

Structured lược đồ (schema / 스키마) + kiểm tra hợp lệ (validation / 검증) often more important than open-ended answer chất lượng (quality / 품질).

## Extractive vs Generative IE

Extractive mô hình (model / 모델) selects spans from nguồn (source / 소스), naturally grounded and preserves chính xác (exact / 정확한) văn bản (text / 텍스트).

Generative mô hình (model / 모델) outputs JSON/văn bản (text / 텍스트) fields, flexible normalization but can hallucinate values not present.

For high-stakes chuỗi xử lý (pipeline / 파이프라인), combine:

```text
LLM proposes structured extraction
→ schema validation
→ source-span evidence check
→ deterministic business rules / human review
```

## Thực thể (entity / 엔터티) Linking

NER detects mention `Apple`; linking maps to chuẩn gốc (canonical / 정본) thực thể (entity / 엔터티):

```text
Apple → Apple Inc. (company)
not apple (fruit)
```

Thực thể (entity / 엔터티) linking requires candidate generation + disambiguation using ngữ cảnh (context / 맥락)/kiến thức (knowledge / 지식) cơ sở (base / 기반).

Chuẩn gốc (canonical / 정본) IDs let extracted facts phép nối (join / 조인) databases/kiến thức (knowledge / 지식) graphs.

## Normalization

Extracted string may need normalized giá trị (value / 값):

```text
"Sep 20, 2026" → 2026-09-20
"₩1.2 million" → {currency: KRW, amount: 1200000}
```

Normalization should be deterministic when possible and retain original văn bản (text / 텍스트)/provenance.

## Document bố cục (layout / 레이아웃)

Contracts/invoices forms contain meaning in bố cục (layout / 레이아웃): bảng (table / 테이블) cells, headers, coordinates.

Plain OCR văn bản (text / 텍스트) can lose quan hệ (relation / 관계). Layout-aware các mô hình (models / 모델들) encode bounding boxes/visual features plus văn bản (text / 텍스트).

Multimodal document AI combines vision + NLP.

## Weak Supervision

Manual IE annotation expensive. Weak supervision uses rules/distant KB matches/heuristics to create noisy labels.

Need mô hình (model / 모델)/techniques account label noise; evaluation still requires clean gold set.

## Distant Supervision

If kiến thức (knowledge / 지식) cơ sở (base / 기반) says `(CompanyA, acquired, CompanyB)`, sentences containing both entities are treated positive quan hệ (relation / 관계) examples. But sentence may not express quan hệ (relation / 관계), creating false labels.

This trades annotation quy mô (scale / 규모) for noise.

## Precision vs Recall in Extraction

High precision may be preferred when extracted facts automatically enter DB. High recall may be preferred when humans rà soát (review / 검토) candidates.

Threshold and workflow should reflect downstream chi phí (cost / 비용).

## Evaluation

Entity-level exact-match precision/recall/F1:

\[
Precision=\frac{correct\ predicted\ spans}{predicted\ spans}
\]

\[
Recall=\frac{correct\ predicted\ spans}{gold\ spans}
\]

Partial overlaps can be separately analyzed but should not silently count as chính xác (exact / 정확한).

Quan hệ (relation / 관계)/sự kiện (event / 이벤트) metrics require entities + labels + roles correct; lan truyền lỗi (error propagation / 오류 전파) matters.

## Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) Construction

IE chuỗi xử lý (pipeline / 파이프라인):

```text
Documents
→ entity extraction
→ entity linking
→ relation/event extraction
→ canonicalization
→ provenance
→ Knowledge Graph
```

Every edge should ideally carry nguồn (source / 소스) bằng chứng (evidence / 증거)/thời gian (time / 시간)/confidence, not only triple.

## LLM Structured Extraction

LLMs can few-shot extract new schemas quickly. But robust môi trường vận hành (production / 운영 환경) needs:

- JSON/lược đồ (schema / 스키마) constrained decoding;
- null/unknown hành vi (behavior / 동작);
- bằng chứng (evidence / 증거) quotes/spans;
- field-level confidence/evaluation;
- prompt-injection handling for untrusted docs;
- deterministic kiểm tra hợp lệ (validation / 검증).

“Valid JSON” is not same as “correct extraction”.

## Mô hình tư duy (mental model / 사고 모델)

> thông tin (information / 정보) Extraction converts ngôn ngữ (language / 언어) into typed claims tied to nguồn (source / 소스) bằng chứng (evidence / 증거). The nguồn (source / 소스)/provenance is part of the dữ liệu (data / 데이터), not optional siêu dữ liệu (metadata / 메타데이터).

## Dùng chung (common / 공통) Misconceptions

### “NER is just find proper nouns”

Thực thể (entity / 엔터티) lược đồ (schema / 스키마) can include dates, amounts, products, diseases; ngữ cảnh (context / 맥락) decides types.

### “LLM generated trường dữ liệu (field / 필드) looks plausible, so extraction succeeded”

It may fabricate; extraction should be grounded to nguồn (source / 소스).

### “đơn vị từ (token / 토큰) accuracy is enough for NER”

`O` dominates; entity-span F1 more meaningful.

### “kiến thức (knowledge / 지식) đồ thị (graph / 그래프) can be built by storing every extracted triple”

Need thực thể (entity / 엔터티) resolution, temporal/provenance/confidence and contradiction handling.

## Liên kết kiến thức (knowledge connection / 지식 연결)

IE connects [Knowledge Graphs](../03_knowledge_and_reasoning/06_knowledge_graphs.md), [Transformer NLP](./06_transformer_nlp.md), cơ sở dữ liệu (database / 데이터베이스)/kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) and later LLM công cụ (tool / 도구)/RAG workflows.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 language as data](./00_language_as_data.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
