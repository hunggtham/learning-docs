# Information Extraction: biến text tự do thành structure có thể dùng

Information Extraction (IE / 정보 추출 / trích xuất thông tin) chuyển unstructured text thành structured facts/spans/relations/events. Đây là cầu nối giữa NLP và database/knowledge graph/business workflow.

Thay vì hỏi “model hiểu câu không?”, IE đặt output schema rõ: entity nào xuất hiện, thuộc loại gì, relation nào giữa chúng, event nào xảy ra, field nào cần điền.

## Named Entity Recognition

NER gán spans types:

```text
Shinhan Bank opened an office in Seoul.
[Shinhan Bank]ORG ... [Seoul]LOC
```

Classical token tagging dùng BIO labels:

```text
Shinhan B-ORG
Bank    I-ORG
opened  O
...
Seoul   B-LOC
```

Subword tokenization complicates alignment; evaluation nên entity-span level thay token accuracy.

## Entity Types phụ thuộc domain

General NER: PERSON, ORG, LOCATION.

Finance: ACCOUNT, PRODUCT, TRANSACTION, AMOUNT.

Medical: DISEASE, DRUG, DOSAGE.

Schema design defines what “correct extraction” means. Too broad loses utility; too granular creates annotation inconsistency.

## Sequence Labeling

Transformer encoder gives `h_i`; classifier predicts label each token.

Independent token softmax may produce invalid sequences (`I-PER` without `B-PER`). CRF layer models transition constraints jointly.

Modern large encoders often perform well without CRF, but structured decoding can still help small/domain tasks.

## Relation Extraction

Given entities, predict relation:

```text
[Company A] acquired [Company B]
```

→ `ACQUIRED_BY/ACQUIRED` edge depending schema.

Methods:

- classify entity pair using contextual representation;
- span-pair scoring;
- joint entity+relation extraction;
- generative structured output.

Relation direction matters.

## Event Extraction

Event has trigger + arguments.

Example:

```text
Samsung acquired X for $2B in 2025.
```

Event:

```json
{
  "type": "Acquisition",
  "buyer": "Samsung",
  "target": "X",
  "amount": "$2B",
  "date": "2025"
}
```

Event extraction needs role assignment and sometimes cross-sentence context.

## Coreference Resolution

```text
Alice joined Acme. She became CTO.
```

`She` refers Alice.

Coreference creates entity clusters across mentions, essential for document-level knowledge extraction.

LLMs handle many cases via context but formal coreference evaluation still useful.

## Slot Filling

Business documents often need fields:

```text
invoice_number
seller
buyer
total_amount
due_date
```

This is constrained extraction. OCR/layout + NLP may be needed for scanned documents.

Structured schema + validation often more important than open-ended answer quality.

## Extractive vs Generative IE

Extractive model selects spans from source, naturally grounded and preserves exact text.

Generative model outputs JSON/text fields, flexible normalization but can hallucinate values not present.

For high-stakes pipeline, combine:

```text
LLM proposes structured extraction
→ schema validation
→ source-span evidence check
→ deterministic business rules / human review
```

## Entity Linking

NER detects mention `Apple`; linking maps to canonical entity:

```text
Apple → Apple Inc. (company)
not apple (fruit)
```

Entity linking requires candidate generation + disambiguation using context/knowledge base.

Canonical IDs let extracted facts join databases/knowledge graphs.

## Normalization

Extracted string may need normalized value:

```text
"Sep 20, 2026" → 2026-09-20
"₩1.2 million" → {currency: KRW, amount: 1200000}
```

Normalization should be deterministic when possible and retain original text/provenance.

## Document Layout

Contracts/invoices forms contain meaning in layout: table cells, headers, coordinates.

Plain OCR text can lose relation. Layout-aware models encode bounding boxes/visual features plus text.

Multimodal document AI combines vision + NLP.

## Weak Supervision

Manual IE annotation expensive. Weak supervision uses rules/distant KB matches/heuristics to create noisy labels.

Need model/techniques account label noise; evaluation still requires clean gold set.

## Distant Supervision

If knowledge base says `(CompanyA, acquired, CompanyB)`, sentences containing both entities are treated positive relation examples. But sentence may not express relation, creating false labels.

This trades annotation scale for noise.

## Precision vs Recall in Extraction

High precision may be preferred when extracted facts automatically enter DB. High recall may be preferred when humans review candidates.

Threshold and workflow should reflect downstream cost.

## Evaluation

Entity-level exact-match precision/recall/F1:

\[
Precision=\frac{correct\ predicted\ spans}{predicted\ spans}
\]

\[
Recall=\frac{correct\ predicted\ spans}{gold\ spans}
\]

Partial overlaps can be separately analyzed but should not silently count as exact.

Relation/event metrics require entities + labels + roles correct; error propagation matters.

## Knowledge Graph Construction

IE pipeline:

```text
Documents
→ entity extraction
→ entity linking
→ relation/event extraction
→ canonicalization
→ provenance
→ Knowledge Graph
```

Every edge should ideally carry source evidence/time/confidence, not only triple.

## LLM Structured Extraction

LLMs can few-shot extract new schemas quickly. But robust production needs:

- JSON/schema constrained decoding;
- null/unknown behavior;
- evidence quotes/spans;
- field-level confidence/evaluation;
- prompt-injection handling for untrusted docs;
- deterministic validation.

“Valid JSON” is not same as “correct extraction”.

## Mental Model

> Information Extraction converts language into typed claims tied to source evidence. The source/provenance is part of the data, not optional metadata.

## Common Misconceptions

### “NER is just find proper nouns”

Entity schema can include dates, amounts, products, diseases; context decides types.

### “LLM generated field looks plausible, so extraction succeeded”

It may fabricate; extraction should be grounded to source.

### “Token accuracy is enough for NER”

`O` dominates; entity-span F1 more meaningful.

### “Knowledge graph can be built by storing every extracted triple”

Need entity resolution, temporal/provenance/confidence and contradiction handling.

## Knowledge Connection

IE connects [Knowledge Graphs](../03_knowledge_and_reasoning/06_knowledge_graphs.md), [Transformer NLP](./06_transformer_nlp.md), Database/Data Engineering and later LLM tool/RAG workflows.