# Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Information extraction**. Route đi từ text spans → named entities/types → relations/events → structured outputs → domain schema/evaluation, để NLP biến văn bản tự do thành dữ liệu có thể kiểm tra.

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

> **Chuyển mạch:** Trong **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Thực thể (entity / 엔터티) Types phụ thuộc lĩnh vực (domain / 도메인)** tiếp nhận điểm tựa từ **Named thực thể (entity / 엔터티) Recognition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi (sequence / 시퀀스) Labeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thực thể (entity / 엔터티) Types phụ thuộc lĩnh vực (domain / 도메인)

General NER: PERSON, ORG, LOCATION.

Finance: ACCOUNT, sản phẩm (product / 제품), giao dịch (transaction / 트랜잭션), AMOUNT.

Medical: DISEASE, DRUG, DOSAGE.

Lược đồ (schema / 스키마) thiết kế (design / 설계) defines what “correct extraction” means. Too broad loses utility; too granular creates annotation inconsistency.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Thực thể (entity / 엔터티) Types phụ thuộc lĩnh vực (domain / 도메인)** cho ta quy tắc; **Chuỗi (sequence / 시퀀스) Labeling** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Quan hệ (relation / 관계) Extraction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (sequence / 시퀀스) Labeling

Transformer encoder gives `h_i`; classifier predicts label each đơn vị từ (token / 토큰).

Independent đơn vị từ (token / 토큰) softmax may produce invalid sequences (`I-PER` without `B-PER`). CRF tầng (layer / 계층) các mô hình (models / 모델들) chuyển tiếp (transition / 전이) các ràng buộc (constraints / 제약조건들) jointly.

Hiện đại (modern / 현대적) large encoders often perform well without CRF, but structured decoding can still help small/lĩnh vực (domain / 도메인) tasks.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Chuỗi (sequence / 시퀀스) Labeling** cho ta quy tắc; **Quan hệ (relation / 관계) Extraction** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Sự kiện (event / 이벤트) Extraction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Sự kiện (event / 이벤트) Extraction** tiếp nhận điểm tựa từ **Quan hệ (relation / 관계) Extraction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Coreference Resolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, sau nội dung của **Sự kiện (event / 이벤트) Extraction**, **Coreference Resolution** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Slot Filling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coreference Resolution

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
Alice joined Acme. She became CTO.
```

`She` refers Alice.

Coreference creates thực thể (entity / 엔터티) clusters across mentions, essential for document-level kiến thức (knowledge / 지식) extraction.

LLMs handle many cases via ngữ cảnh (context / 맥락) but formal coreference evaluation still useful.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Slot Filling** tiếp nhận điểm tựa từ **Coreference Resolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Extractive vs Generative IE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Extractive vs Generative IE** tiếp nhận điểm tựa từ **Slot Filling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thực thể (entity / 엔터티) Linking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Thực thể (entity / 엔터티) Linking** tiếp nhận điểm tựa từ **Extractive vs Generative IE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thực thể (entity / 엔터티) Linking

NER detects mention `Apple`; linking maps to chuẩn gốc (canonical / 정본) thực thể (entity / 엔터티):

```text
Apple → Apple Inc. (company)
not apple (fruit)
```

Thực thể (entity / 엔터티) linking requires candidate generation + disambiguation using ngữ cảnh (context / 맥락)/kiến thức (knowledge / 지식) cơ sở (base / 기반).

Chuẩn gốc (canonical / 정본) IDs let extracted facts phép nối (join / 조인) databases/kiến thức (knowledge / 지식) graphs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Normalization** tiếp nhận điểm tựa từ **Thực thể (entity / 엔터티) Linking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Document bố cục (layout / 레이아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Normalization

Extracted string may need normalized giá trị (value / 값):

```text
"Sep 20, 2026" → 2026-09-20
"₩1.2 million" → {currency: KRW, amount: 1200000}
```

Normalization should be deterministic when possible and retain original văn bản (text / 텍스트)/provenance.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Document bố cục (layout / 레이아웃)** tiếp nhận điểm tựa từ **Normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weak Supervision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Document bố cục (layout / 레이아웃)

Contracts/invoices forms contain meaning in bố cục (layout / 레이아웃): bảng (table / 테이블) cells, headers, coordinates.

Plain OCR văn bản (text / 텍스트) can lose quan hệ (relation / 관계). Layout-aware các mô hình (models / 모델들) encode bounding boxes/visual features plus văn bản (text / 텍스트).

Multimodal document AI combines vision + NLP.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Weak Supervision** tiếp nhận điểm tựa từ **Document bố cục (layout / 레이아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Distant Supervision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weak Supervision

Manual IE annotation expensive. Weak supervision uses rules/distant KB matches/heuristics to create noisy labels.

Need mô hình (model / 모델)/techniques account label noise; evaluation still requires clean gold set.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Distant Supervision** tiếp nhận điểm tựa từ **Weak Supervision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Precision vs Recall in Extraction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Distant Supervision

If kiến thức (knowledge / 지식) cơ sở (base / 기반) says `(CompanyA, acquired, CompanyB)`, sentences containing both entities are treated positive quan hệ (relation / 관계) examples. But sentence may not express quan hệ (relation / 관계), creating false labels.

This trades annotation quy mô (scale / 규모) for noise.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Precision vs Recall in Extraction** tiếp nhận điểm tựa từ **Distant Supervision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Precision vs Recall in Extraction

High precision may be preferred when extracted facts automatically enter DB. High recall may be preferred when humans rà soát (review / 검토) candidates.

Threshold and workflow should reflect downstream chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Evaluation** tiếp nhận điểm tựa từ **Precision vs Recall in Extraction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) Construction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) Construction** tiếp nhận điểm tựa từ **Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM Structured Extraction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **LLM Structured Extraction** tiếp nhận điểm tựa từ **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) Construction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM Structured Extraction

LLMs can few-shot extract new schemas quickly. But robust môi trường vận hành (production / 운영 환경) needs:

- JSON/lược đồ (schema / 스키마) constrained decoding;
- null/unknown hành vi (behavior / 동작);
- bằng chứng (evidence / 증거) quotes/spans;
- field-level confidence/evaluation;
- prompt-injection handling for untrusted docs;
- deterministic kiểm tra hợp lệ (validation / 검증).

“Valid JSON” is not same as “correct extraction”.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **LLM Structured Extraction** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> thông tin (information / 정보) Extraction converts ngôn ngữ (language / 언어) into typed claims tied to nguồn (source / 소스) bằng chứng (evidence / 증거). The nguồn (source / 소스)/provenance is part of the dữ liệu (data / 데이터), not optional siêu dữ liệu (metadata / 메타데이터).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “NER is just find proper nouns”

Thực thể (entity / 엔터티) lược đồ (schema / 스키마) can include dates, amounts, products, diseases; ngữ cảnh (context / 맥락) decides types.

### “LLM generated trường dữ liệu (field / 필드) looks plausible, so extraction succeeded”

It may fabricate; extraction should be grounded to nguồn (source / 소스).

### “đơn vị từ (token / 토큰) accuracy is enough for NER”

`O` dominates; entity-span F1 more meaningful.

### “kiến thức (knowledge / 지식) đồ thị (graph / 그래프) can be built by storing every extracted triple”

Need thực thể (entity / 엔터티) resolution, temporal/provenance/confidence and contradiction handling.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) Extraction: biến văn bản (text / 텍스트) tự do thành cấu trúc (structure / 구조) có thể dùng**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

IE connects [Knowledge Graphs](../03_knowledge_and_reasoning/06_knowledge_graphs.md), [Transformer NLP](./06_transformer_nlp.md), Database/Data Engineering and later LLM tool/RAG workflows.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
