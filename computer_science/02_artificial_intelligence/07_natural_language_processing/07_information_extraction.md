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

> NER không chỉ tìm span; nó cần một bộ type phản ánh mục đích sử dụng. Vì vậy, sau khi nhận diện mention, ta phải quyết định schema theo domain trước khi chọn cách gán nhãn.

## Thực thể (entity / 엔터티) Types phụ thuộc lĩnh vực (domain / 도메인)

General NER: PERSON, ORG, LOCATION.

Finance: ACCOUNT, sản phẩm (product / 제품), giao dịch (transaction / 트랜잭션), AMOUNT.

Medical: DISEASE, DRUG, DOSAGE.

Lược đồ (schema / 스키마) thiết kế (design / 설계) defines what “correct extraction” means. Too broad loses utility; too granular creates annotation inconsistency.

> Schema domain trả lời câu hỏi cần trích xuất loại thực thể nào. Sequence labeling biến quyết định đó thành nhãn theo từng token và làm lộ các ràng buộc ở ranh giới span.

## Chuỗi (sequence / 시퀀스) Labeling

Transformer encoder gives `h_i`; classifier predicts label each đơn vị từ (token / 토큰).

Independent đơn vị từ (token / 토큰) softmax may produce invalid sequences (`I-PER` without `B-PER`). CRF tầng (layer / 계층) các mô hình (models / 모델들) chuyển tiếp (transition / 전이) các ràng buộc (constraints / 제약조건들) jointly.

Hiện đại (modern / 현대적) large encoders often perform well without CRF, but structured decoding can still help small/lĩnh vực (domain / 도메인) tasks.

> Sequence labeling xác định các thực thể, nhưng chưa nói chúng liên hệ với nhau ra sao. Relation extraction nối các span đã nhận diện thành các cạnh có hướng và có ý nghĩa.

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

> Quan hệ giữa hai thực thể là nền cho nhiều sự kiện, nhưng sự kiện còn cần trigger, vai trò và thời điểm. Event extraction vì thế mở rộng cạnh tĩnh thành một cấu trúc có ngữ cảnh.

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

> Event extraction có thể trải qua nhiều câu, nơi đại từ hoặc mention rút gọn trỏ về cùng một đối tượng. Coreference resolution gom các mention đó trước khi điền vai trò và sự kiện đầy đủ.

## Coreference Resolution

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
Alice joined Acme. She became CTO.
```

`She` refers Alice.

Coreference creates thực thể (entity / 엔터티) clusters across mentions, essential for document-level kiến thức (knowledge / 지식) extraction.

LLMs handle many cases via ngữ cảnh (context / 맥락) but formal coreference evaluation still useful.

> Khi các mention đã được gom thành một thực thể, hệ thống có thể điền những trường nghiệp vụ cụ thể. Slot filling biến cấu trúc tham chiếu ấy thành các giá trị mà quy trình downstream cần.

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

> Slot filling thường có schema hẹp và tiêu chí kiểm tra rõ, nên cần cân nhắc lấy nguyên văn hay sinh giá trị đã chuẩn hóa. Đó là điểm phân chia giữa extractive và generative IE.

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

> Generative IE linh hoạt nhưng có thể tạo giá trị không xuất hiện trong nguồn; extractive IE giữ được bằng chứng nguyên văn. Dù chọn cách nào, các mention vẫn cần được map về thực thể chuẩn để nối dữ liệu.

## Thực thể (entity / 엔터티) Linking

NER detects mention `Apple`; linking maps to chuẩn gốc (canonical / 정본) thực thể (entity / 엔터티):

```text
Apple → Apple Inc. (company)
not apple (fruit)
```

Thực thể (entity / 엔터티) linking requires candidate generation + disambiguation using ngữ cảnh (context / 맥락)/kiến thức (knowledge / 지식) cơ sở (base / 기반).

Chuẩn gốc (canonical / 정본) IDs let extracted facts phép nối (join / 조인) databases/kiến thức (knowledge / 지식) graphs.

> Entity linking xác định ID chuẩn, còn normalization quy định biểu diễn thống nhất của ngày, tiền tệ và các giá trị. Hai bước này bổ sung cho nhau: cùng một thực thể có thể xuất hiện với nhiều cách viết.

## Normalization

Extracted string may need normalized giá trị (value / 값):

```text
"Sep 20, 2026" → 2026-09-20
"₩1.2 million" → {currency: KRW, amount: 1200000}
```

Normalization should be deterministic when possible and retain original văn bản (text / 텍스트)/provenance.

> Normalization nên giữ lại chuỗi gốc và provenance để có thể kiểm tra ngược. Với tài liệu biểu mẫu, muốn chuẩn hóa đúng còn phải biết giá trị nằm ở ô, hàng hay cột nào trong layout.

## Document bố cục (layout / 레이아웃)

Contracts/invoices forms contain meaning in bố cục (layout / 레이아웃): bảng (table / 테이블) cells, headers, coordinates.

Plain OCR văn bản (text / 텍스트) can lose quan hệ (relation / 관계). Layout-aware các mô hình (models / 모델들) encode bounding boxes/visual features plus văn bản (text / 텍스트).

Multimodal document AI combines vision + NLP.

> Layout cung cấp tín hiệu không gian mà văn bản phẳng làm mất, nhưng nhãn layout thủ công tốn kém. Weak supervision cho phép tạo nhãn ban đầu từ quy tắc và nguồn nhiễu để mở rộng dữ liệu.

## Weak Supervision

Manual IE annotation expensive. Weak supervision uses rules/distant KB matches/heuristics to create noisy labels.

Need mô hình (model / 모델)/techniques account label noise; evaluation still requires clean gold set.

> Weak supervision tạo nhãn từ nhiều tín hiệu không hoàn hảo, trong đó distant supervision là trường hợp dựa vào tri thức ngoài như knowledge base. Cách này tăng quy mô nhưng đưa thêm nhiễu có hệ thống.

## Distant Supervision

If kiến thức (knowledge / 지식) cơ sở (base / 기반) says `(CompanyA, acquired, CompanyB)`, sentences containing both entities are treated positive quan hệ (relation / 관계) examples. But sentence may not express quan hệ (relation / 관계), creating false labels.

This trades annotation quy mô (scale / 규모) for noise.

> Distant supervision đánh đổi chi phí gán nhãn lấy false positive do giả định xa. Vì vậy, ngưỡng precision–recall phải được chọn theo việc dữ liệu trích xuất sẽ được dùng tiếp như thế nào.

## Precision vs Recall in Extraction

High precision may be preferred when extracted facts automatically enter DB. High recall may be preferred when humans rà soát (review / 검토) candidates.

Threshold and workflow should reflect downstream chi phí (cost / 비용).

> Precision và recall mô tả đánh đổi vận hành, nhưng cần một bộ metric và giao thức đánh giá để biết lỗi nằm ở span, type, relation hay role. Phần Evaluation đặt các lựa chọn đó vào phép đo cụ thể.

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

> Evaluation cho biết pipeline làm đúng đến đâu và lỗi lan truyền qua các tầng thế nào. Khi các span, link và quan hệ đã đủ tin cậy, chúng có thể được ghép thành knowledge graph có provenance.

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

> Knowledge graph không chỉ là tập triple; mỗi cạnh cần bằng chứng, thời gian và độ tin cậy. LLM structured extraction có thể giúp tạo cấu trúc nhanh, nhưng phải chịu các ràng buộc đó ngay từ đầu.

## LLM Structured Extraction

LLMs can few-shot extract new schemas quickly. But robust môi trường vận hành (production / 운영 환경) needs:

- JSON/lược đồ (schema / 스키마) constrained decoding;
- null/unknown hành vi (behavior / 동작);
- bằng chứng (evidence / 증거) quotes/spans;
- field-level confidence/evaluation;
- prompt-injection handling for untrusted docs;
- deterministic kiểm tra hợp lệ (validation / 검증).

“Valid JSON” is not same as “correct extraction”.

> LLM có thể sinh JSON hợp lệ mà vẫn trích xuất sai hoặc bịa giá trị. Vì vậy, mental model của IE phải đặt schema, bằng chứng và validation cùng một chuỗi kiểm soát.

## Mô hình tư duy (mental model / 사고 모델)

> thông tin (information / 정보) Extraction converts ngôn ngữ (language / 언어) into typed claims tied to nguồn (source / 소스) bằng chứng (evidence / 증거). The nguồn (source / 소스)/provenance is part of the dữ liệu (data / 데이터), not optional siêu dữ liệu (metadata / 메타데이터).

> Mental model này xem extraction là chuyển ngôn ngữ thành claim có type và provenance, không phải chỉ là sinh văn bản. Các ngộ nhận sau đây kiểm tra những điểm dễ bị bỏ qua trong chuỗi đó.

## Dùng chung (common / 공통) Misconceptions

### “NER is just find proper nouns”

Thực thể (entity / 엔터티) lược đồ (schema / 스키마) can include dates, amounts, products, diseases; ngữ cảnh (context / 맥락) decides types.

### “LLM generated trường dữ liệu (field / 필드) looks plausible, so extraction succeeded”

It may fabricate; extraction should be grounded to nguồn (source / 소스).

### “đơn vị từ (token / 토큰) accuracy is enough for NER”

`O` dominates; entity-span F1 more meaningful.

### “kiến thức (knowledge / 지식) đồ thị (graph / 그래프) can be built by storing every extracted triple”

Need thực thể (entity / 엔터티) resolution, temporal/provenance/confidence and contradiction handling.

> Các ngộ nhận cho thấy chất lượng IE phụ thuộc schema, bằng chứng, resolution và xử lý mâu thuẫn, không chỉ phụ thuộc model. Phần liên kết kiến thức đặt những nguyên tắc này cạnh các chủ đề NLP liên quan để học tiếp có định hướng.

## Liên kết kiến thức (knowledge connection / 지식 연결)

IE connects [Knowledge Graphs](../03_knowledge_and_reasoning/06_knowledge_graphs.md), [Transformer NLP](./06_transformer_nlp.md), Database/Data Engineering and later LLM tool/RAG workflows.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
