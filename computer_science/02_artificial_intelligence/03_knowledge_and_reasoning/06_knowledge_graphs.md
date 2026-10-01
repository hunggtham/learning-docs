# Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Đồ thị (graph / 그래프) mô hình dữ liệu (data model / 데이터 모델)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Thực thể (entity / 엔터티) định danh (identity / 식별자)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**kiến thức (knowledge / 지식) đồ thị (graph / 그래프)** biểu diễn entities và relationships bằng đồ thị (graph / 그래프) có typed ngữ nghĩa (semantics / 의미론). Dạng đơn giản nhất là triple:

\[
(subject, predicate, object)
\]

Ví dụ:

```text
(Seoul, capitalOf, SouthKorea)
(Alice, worksAt, CompanyX)
(CompanyX, locatedIn, Seoul)
```

Điểm quan trọng: kiến thức (knowledge / 지식) đồ thị (graph / 그래프) không chỉ là đồ thị (graph / 그래프) cơ sở dữ liệu (database / 데이터베이스) có nhiều edges. Giá trị của nó đến từ định danh (identity / 식별자), lược đồ (schema / 스키마)/ontology, provenance, temporal validity, quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론) và khả năng nối facts từ nhiều nguồn thành một mô hình (model / 모델) có thể truy vấn (query / 쿼리)/reason.

Xem trước: [Knowledge Representation](./00_knowledge_representation.md).

## Đồ thị (graph / 그래프) mô hình dữ liệu (data model / 데이터 모델)

Một đồ thị (graph / 그래프) gồm nodes `V` và edges `E`:

\[
G=(V,E)
\]

Trong KG:

- nút (node / 노드) thường là thực thể (entity / 엔터티)/concept/literal;
- edge có quan hệ (relation / 관계) kiểu (type / 타입);
- nút (node / 노드)/edge có thể có properties/siêu dữ liệu (metadata / 메타데이터).

RDF-like đồ thị (graph / 그래프) biểu diễn edge qua triples. Property-graph các hệ thống (systems / 시스템들) cho phép properties trực tiếp trên nút (node / 노드)/edge.

Hai các mô hình (models / 모델들) có conversion possibilities nhưng truy vấn (query / 쿼리) ngữ nghĩa (semantics / 의미론)/tooling khác nhau.

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Đồ thị (graph / 그래프) mô hình dữ liệu (data model / 데이터 모델)** nêu điều cần giải thích; **Thực thể (entity / 엔터티) định danh (identity / 식별자)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thực thể (entity / 엔터티) định danh (identity / 식별자)

Nếu facts dùng identifiers khác nhau cho cùng real thực thể (entity / 엔터티):

```text
Seoul
서울
SEOUL_CITY_001
```

Hệ thống (system / 시스템) cần ánh xạ (mapping / 매핑)/chuẩn gốc (canonical / 정본) ID.

Nếu không, đồ thị (graph / 그래프) bị split thành duplicate entities. Nếu merge nhầm hai entities, facts bị contamination.

**thực thể (entity / 엔터티) resolution (개체 해결 / thực thể đối sánh)** vì vậy là foundation, không phải cleanup minor.

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **Thực thể (entity / 엔터티) định danh (identity / 식별자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lược đồ (schema / 스키마) và ontology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론)

Edge label `worksAt` cần define:

- subject kiểu (type / 타입) nào hợp lệ;
- đối tượng (object / 객체) kiểu (type / 타입) nào hợp lệ;
- active employment hay historical?
- full-time/contractor có count không?
- temporal validity?

Without ngữ nghĩa (semantics / 의미론), đồ thị (graph / 그래프) may be syntactically connected but semantically ambiguous.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Lược đồ (schema / 스키마) và ontology** tiếp nhận điểm tựa từ **Quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RDF mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lược đồ (schema / 스키마) và ontology

Lược đồ (schema / 스키마) can trạng thái (state / 상태):

```text
Person --worksAt--> Organization
Organization --locatedIn--> Place
```

Ontology adds lớp (class / 클래스) hierarchy/axioms:

```text
Doctor subClassOf MedicalProfessional
Hospital subClassOf HealthcareOrganization
```

Reasoner may derive inherited types.

Lược đồ (schema / 스키마) also enables kiểm tra hợp lệ (validation / 검증): edge `Person worksAt Date` likely invalid.

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **RDF mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Lược đồ (schema / 스키마) và ontology** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **RDFS và OWL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RDF mô hình tư duy (mental model / 사고 모델)

RDF represents statements as triples:

```text
subject predicate object
```

Example Turtle-like:

```turtle
:Alice :worksAt :CompanyX .
:CompanyX :locatedIn :Seoul .
```

A URI/IRI identifies resources globally within conventions.

RDF đồ thị (graph / 그래프) can merge datasets when identifiers/vocabularies align.

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **RDFS và OWL** gom các mảnh từ **RDF mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **SPARQL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RDFS và OWL

RDFS provides basic vocabulary for:

- classes;
- subclass;
- properties;
- lĩnh vực (domain / 도메인)/phạm vi (range / 범위).

OWL adds richer ontology constructs based on Description Logics, such as equivalence, cardinality and lớp (class / 클래스) expressions depending profile.

More expressive profile means potentially more expensive lập luận (reasoning / 추론); OWL profiles intentionally offer different trade-offs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **SPARQL** tiếp nhận điểm tựa từ **RDFS và OWL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thuộc tính (property / 속성) đồ thị (graph / 그래프) và Cypher-like truy vấn (query / 쿼리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SPARQL

SPARQL queries RDF đồ thị (graph / 그래프) by đồ thị (graph / 그래프) patterns.

Conceptual truy vấn (query / 쿼리):

```sparql
SELECT ?person
WHERE {
  ?person :worksAt :CompanyX .
  ?person :livesIn :Seoul .
}
```

This is mẫu (pattern / 패턴) matching over triples, not ngữ nghĩa (semantic / 의미적) similarity tìm kiếm (search / 검색).

Đồ thị (graph / 그래프) engines optimize phép nối (join / 조인) orders much like relational DB truy vấn (query / 쿼리) optimizers.

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Thuộc tính (property / 속성) đồ thị (graph / 그래프) và Cypher-like truy vấn (query / 쿼리)** tiếp nhận điểm tựa từ **SPARQL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quan hệ (relation / 관계) as edge vs sự kiện (event / 이벤트) nút (node / 노드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thuộc tính (property / 속성) đồ thị (graph / 그래프) và Cypher-like truy vấn (query / 쿼리)

Thuộc tính (property / 속성) đồ thị (graph / 그래프) may store:

```text
(:Person {id: 1})-[:WORKS_AT {since: 2024}]->(:Company)
```

Truy vấn (query / 쿼리) ngôn ngữ (language / 언어) like Cypher expresses đường dẫn (path / 경로) patterns.

Thuộc tính (property / 속성) graphs are dùng chung (common / 공통) in operational đồ thị (graph / 그래프) applications; RDF/OWL ecosystems emphasize web-scale ngữ nghĩa (semantic / 의미적) standards/ontologies.

Neither mô hình (model / 모델) is universally superior.

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Quan hệ (relation / 관계) as edge vs sự kiện (event / 이벤트) nút (node / 노드)** tiếp nhận điểm tựa từ **Thuộc tính (property / 속성) đồ thị (graph / 그래프) và Cypher-like truy vấn (query / 쿼리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Provenance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quan hệ (relation / 관계) as edge vs sự kiện (event / 이벤트) nút (node / 노드)

Simple edge works for nhị phân (binary / 이진) timeless quan hệ (relation / 관계):

```text
Alice --worksAt--> CompanyX
```

But suppose employment has role, start/end, salary, nguồn (source / 소스).

Represent employment as thực thể (entity / 엔터티)/sự kiện (event / 이벤트):

```text
Alice --participantIn--> Employment123
Employment123 --employer--> CompanyX
Employment123 --role--> Engineer
Employment123 --startDate--> 2025-01-01
```

This avoids awkward edge siêu dữ liệu (metadata / 메타데이터) in triple-only mô hình (model / 모델) and supports n-ary relations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Provenance** tiếp nhận điểm tựa từ **Quan hệ (relation / 관계) as edge vs sự kiện (event / 이벤트) nút (node / 노드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Temporal kiến thức (knowledge / 지식) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Provenance

A fact should often carry nguồn (source / 소스):

```text
claim: CompanyX locatedIn Seoul
source: registry document
retrievedAt: 2026-09-01
confidence: verified
```

When sources xung đột (conflict / 충돌), provenance allows hệ thống (system / 시스템) to compare rather than silently overwrite.

RAG citation and KG provenance solve related trust bài toán (problem / 문제).

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Temporal kiến thức (knowledge / 지식) đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **Provenance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Suy luận (inference / 추론) over đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Temporal kiến thức (knowledge / 지식) đồ thị (graph / 그래프)

Relations thay đổi (change / 변경) over thời gian (time / 시간):

```text
(Alice, worksAt, CompanyX, 2025-01..2026-08)
```

Temporal KG supports historical queries:

> Who was CEO on date T?

Without thời gian (time / 시간), đồ thị (graph / 그래프) may contain contradictory edges that are actually valid in different periods.

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Suy luận (inference / 추론) over đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **Temporal kiến thức (knowledge / 지식) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transitive relations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Suy luận (inference / 추론) over đồ thị (graph / 그래프)

Quy tắc (rule / 규칙):

```text
parentOf(x,y) ∧ parentOf(y,z)
→ grandparentOf(x,z)
```

Ontology:

```text
Cardiologist subClassOf Doctor
Alice type Cardiologist
→ Alice type Doctor
```

Suy luận (inference / 추론) materializes derived triples or answers queries dynamically.

Đồ thị (graph / 그래프) traversal alone is not logical suy luận (inference / 추론) unless quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론) define quy tắc (rule / 규칙).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Transitive relations** tiếp nhận điểm tựa từ **Suy luận (inference / 추론) over đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Symmetric và inverse relations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transitive relations

If quan hệ (relation / 관계) declared transitive:

\[
R(a,b)\land R(b,c)\rightarrow R(a,c)
\]

Examples may include `ancestorOf`, `locatedWithin` under carefully defined ngữ nghĩa (semantics / 의미론).

Do not assume every quan hệ (relation / 관계) transitive. `friendOf` and `parentOf` are not.

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Symmetric và inverse relations** tiếp nhận điểm tựa từ **Transitive relations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) completion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Symmetric và inverse relations

Symmetric:

\[
MarriedTo(a,b)\rightarrow MarriedTo(b,a)
\]

Inverse:

\[
ParentOf(a,b)\leftrightarrow ChildOf(b,a)
\]

Encoding these properties reduces duplicated manual facts and supports truy vấn (query / 쿼리) expansion.

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) completion** tiếp nhận điểm tựa từ **Symmetric và inverse relations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thực thể (entity / 엔터티) embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) completion

KG often incomplete. Link prediction estimates missing triple score:

\[
score(h,r,t)
\]

Embedding methods map entities/relations to vectors and learn scoring hàm (function / 함수).

Example TransE-like idea:

\[
\mathbf{h}+\mathbf{r}\approx\mathbf{t}
\]

for true triple.

But predicted edge is **hypothesis**, not verified fact. Completion must not silently convert score into truth in high-stakes hệ thống (system / 시스템).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Thực thể (entity / 엔터티) embeddings** tiếp nhận điểm tựa từ **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) completion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đồ thị (graph / 그래프) Neural Networks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thực thể (entity / 엔터티) embeddings

Đồ thị (graph / 그래프) embeddings place entities in véc-tơ (vector / 벡터) không gian (space / 공간) based on topology/relations.

They enable:

- link prediction;
- similarity;
- clustering;
- downstream ML features.

But véc-tơ (vector / 벡터) similarity compresses relational cấu trúc (structure / 구조) and can lose tường minh (explicit / 명시적) interpretability.

This mirrors symbolic ↔ phân tán (distributed / 분산) biểu diễn (representation / 표현) sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Đồ thị (graph / 그래프) Neural Networks** tiếp nhận điểm tựa từ **Thực thể (entity / 엔터티) embeddings** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-hop queries** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đồ thị (graph / 그래프) Neural Networks

GNN updates nút (node / 노드) biểu diễn (representation / 표현) by aggregating neighbors:

\[
\mathbf{h}_v^{(l+1)}=\phi\left(\mathbf{h}_v^{(l)},\operatorname{AGG}\{\mathbf{h}_u^{(l)}:u\in N(v)\}\right)
\]

GNN can learn on đồ thị (graph / 그래프) cấu trúc (structure / 구조), but it does not replace KG lược đồ (schema / 스키마)/provenance.

Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) is dữ liệu (data / 데이터)/ngữ nghĩa (semantic / 의미적) biểu diễn (representation / 표현); GNN is học tập (learning / 학습) kiến trúc (architecture / 아키텍처) that may consume graphs.

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Multi-hop queries** tiếp nhận điểm tựa từ **Đồ thị (graph / 그래프) Neural Networks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đường dẫn (path / 경로) explosion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-hop queries

Question:

> Which suppliers are located in countries affected by sự kiện (event / 이벤트) X?

May require đường dẫn (path / 경로):

```text
Supplier
→ locatedIn
Country
← affects
Event
```

Đồ thị (graph / 그래프) enables tường minh (explicit / 명시적) multi-hop retrieval.

But đường dẫn (path / 경로) existence does not automatically mean answer semantically valid; quan hệ (relation / 관계) directions/types matter.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Multi-hop queries** xác định đầu vào; **Đường dẫn (path / 경로) explosion** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) vs relational cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đường dẫn (path / 경로) explosion

If average degree `b`, number paths of length `k` can grow roughly `b^k`.

Đồ thị (graph / 그래프) truy vấn (query / 쿼리) needs:

- quan hệ (relation / 관계) filters;
- direction các ràng buộc (constraints / 제약조건들);
- đường dẫn (path / 경로) length bounds;
- lược đồ (schema / 스키마);
- ranking.

This is tìm kiếm (search / 검색) bài toán (problem / 문제) again.

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Đường dẫn (path / 경로) explosion** nêu điều cần giải thích; **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) vs relational cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) vs véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) vs relational cơ sở dữ liệu (database / 데이터베이스)

Relational DB excels tabular transactions, các ràng buộc (constraints / 제약조건들) and SQL joins.

Đồ thị (graph / 그래프) DB excels variable-length relationship traversal and graph-centric lược đồ (schema / 스키마).

Many KG facts can be stored relationally; “kiến thức (knowledge / 지식) đồ thị (graph / 그래프)” is ngữ nghĩa (semantic / 의미적)/modeling concept, not necessarily yêu cầu (requirement / 요구사항) for đồ thị (graph / 그래프) cơ sở dữ liệu (database / 데이터베이스) technology.

Choose lưu trữ (storage / 저장소) from tải công việc (workload / 워크로드), not branding.

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) vs relational cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) vs véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **KG + RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) vs véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)

Véc-tơ (vector / 벡터) DB retrieves by embedding similarity:

```text
query embedding ≈ document/entity embedding
```

KG retrieves by tường minh (explicit / 명시적) relationships/các ràng buộc (constraints / 제약조건들):

```text
entity --relation--> entity
```

Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) answers “what is semantically similar?”

KG truy vấn (query / 쿼리) answers “what is explicitly connected according to quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론)?”

Hybrid hệ thống (system / 시스템) can use both.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) vs véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **KG + RAG** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **GraphRAG term** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KG + RAG

Văn bản (text / 텍스트) RAG luồng (flow / 흐름):

```text
query → embedding retrieval → chunks → LLM
```

KG-enhanced luồng (flow / 흐름) can add:

```text
query
 ↓ entity linking
seed entities
 ↓ graph traversal / structured filters
relevant entities + relations + documents
 ↓
LLM grounded generation
```

Benefits can include tường minh (explicit / 명시적) multi-hop cấu trúc (structure / 구조), siêu dữ liệu (metadata / 메타데이터) filtering and provenance.

But đồ thị (graph / 그래프) construction/maintenance chi phí (cost / 비용) is significant.

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **GraphRAG term** tiếp nhận điểm tựa từ **KG + RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thực thể (entity / 엔터티) linking from văn bản (text / 텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## GraphRAG term

“GraphRAG” is used for multiple architectures, not one standardized thuật toán (algorithm / 알고리즘). dùng chung (common / 공통) idea is augment retrieval/generation with graph-derived entities, communities, relations or paths.

When evaluating GraphRAG, ask exactly:

- đồ thị (graph / 그래프) built how?
- nodes/edges mean what?
- truy vấn (query / 쿼리) chiến lược (strategy / 전략)?
- đồ thị (graph / 그래프) used for retrieval, summarization or lập luận (reasoning / 추론)?
- facts verified how?

Do not treat label as guarantee of better lập luận (reasoning / 추론).

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Thực thể (entity / 엔터티) linking from văn bản (text / 텍스트)** tiếp nhận điểm tựa từ **GraphRAG term** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ontology-aware retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thực thể (entity / 엔터티) linking from văn bản (text / 텍스트)

Before querying KG from natural ngôn ngữ (language / 언어), identify mentions and map to entities.

`Apple` could mean company or fruit.

Thực thể (entity / 엔터티) linking uses ngữ cảnh (context / 맥락) to resolve ambiguity.

A wrong link contaminates entire downstream multi-hop truy vấn (query / 쿼리), so confidence/fallback matter.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Ontology-aware retrieval** tiếp nhận điểm tựa từ **Thực thể (entity / 엔터티) linking from văn bản (text / 텍스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **KG in recommendation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ontology-aware retrieval

If truy vấn (query / 쿼리) asks `medical professional`, ontology may expand subclasses:

```text
Doctor
Nurse
Pharmacist
... ⊑ MedicalProfessional
```

This improves recall without relying only lexical/embedding similarity.

But ontology must match lĩnh vực (domain / 도메인) and hiện tại (current / 현재) definitions.

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **KG in recommendation** tiếp nhận điểm tựa từ **Ontology-aware retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **KG in fraud detection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KG in recommendation

User-item tương tác (interaction / 상호작용) plus item attributes/relations:

```text
User → watched → Movie
Movie → directedBy → Director
Movie → genre → SciFi
```

Đồ thị (graph / 그래프) paths can provide explainable features/recommendations.

Embedding/GNN các mô hình (models / 모델들) can learn from this heterogeneous đồ thị (graph / 그래프).

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **KG in fraud detection** tiếp nhận điểm tựa từ **KG in recommendation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KG in fraud detection

Đồ thị (graph / 그래프) connects:

```text
Account
Device
IP
Merchant
Phone
Transaction
```

Fraud may be relational: many accounts share thiết bị (device / 장치)/IP or money cycles.

Đồ thị (graph / 그래프) algorithms/GNNs detect patterns invisible to per-row classifier.

Still need temporal thứ tự (ordering / 순서) and avoid leakage (future edges).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **KG in fraud detection** nêu điều cần giải thích; **Dữ liệu (data / 데이터) chất lượng (quality / 품질)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Incremental updates** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) chất lượng (quality / 품질)

KG chất lượng (quality / 품질) dimensions:

- thực thể (entity / 엔터티) resolution accuracy;
- quan hệ (relation / 관계) tính đúng đắn (correctness / 정확성);
- coverage;
- temporal freshness;
- provenance;
- lược đồ (schema / 스키마) consistency;
- duplicate/xung đột (conflict / 충돌) tỷ lệ (rate / 비율).

A huge đồ thị (graph / 그래프) with poor định danh (identity / 식별자) is worse than smaller reliable đồ thị (graph / 그래프).

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Dữ liệu (data / 데이터) chất lượng (quality / 품질)** nêu điều cần giải thích; **Incremental updates** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Extraction with LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Incremental updates

Môi trường vận hành (production / 운영 환경) KG evolves continuously. cập nhật (update / 업데이트) chuỗi xử lý (pipeline / 파이프라인) must handle:

```text
new source
→ extract entities/relations
→ resolve identity
→ validate schema
→ preserve provenance
→ reconcile conflicts
→ update indexes/embeddings
```

This is kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) + kiến thức (knowledge / 지식) kỹ thuật (engineering / 엔지니어링), not just AI modeling.

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Extraction with LLM** tiếp nhận điểm tựa từ **Incremental updates** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Question answering over KG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Extraction with LLM

LLM can convert văn bản (text / 텍스트) to candidate triples:

```text
Text → LLM → structured entities/relations
```

Need kiểm tra hợp lệ (validation / 검증) because mô hình (model / 모델) may:

- invent quan hệ (relation / 관계);
- merge entities incorrectly;
- omit qualifier/thời gian (time / 시간);
- normalize giá trị (value / 값) wrongly.

Safer chuỗi xử lý (pipeline / 파이프라인):

```text
LLM extraction
→ schema validation
→ entity resolution
→ source-grounded verification
→ human/review rules for critical facts
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Question answering over KG** tiếp nhận điểm tựa từ **Extraction with LLM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Question answering over KG

Methods phạm vi (range / 범위) from:

- deterministic SPARQL/Cypher;
- ngữ nghĩa (semantic / 의미적) parsing NL → truy vấn (query / 쿼리);
- embedding-based quan hệ (relation / 관계) prediction;
- GNN lập luận (reasoning / 추론);
- LLM tool-calling đồ thị (graph / 그래프) truy vấn (query / 쿼리).

Reliable enterprise mẫu (pattern / 패턴): LLM generates structured truy vấn (query / 쿼리), đồ thị (graph / 그래프) engine executes, LLM verbalizes kết quả (result / 결과) with provenance.

> **Chuyển mạch:** Trong **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Question answering over KG** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Entity      = identifiable thing
Relation    = typed semantic connection
Triple      = atomic graph statement
Ontology    = vocabulary + semantic constraints
Provenance  = source of claim
Time        = validity context
Graph query = explicit structured relationship retrieval
Embedding   = learned similarity/score layer
Reasoner    = derives facts from formal semantics/rules
```

> **Chuyển mạch:** Ở chặng này của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “kiến thức (knowledge / 지식) đồ thị (graph / 그래프) = véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) with relationships”

No. véc-tơ (vector / 벡터) DB centers similarity in embedding không gian (space / 공간); KG centers tường minh (explicit / 명시적) typed relations and ngữ nghĩa (semantics / 의미론).

### “If đường dẫn (path / 경로) exists, relationship is meaningful”

Đồ thị (graph / 그래프) đường dẫn (path / 경로) only becomes meaningful through quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론), direction and ngữ cảnh (context / 맥락).

### “Link prediction adds missing facts”

It predicts candidates/scores; bên ngoài (external / 외부) kiểm tra hợp lệ (validation / 검증) may be required before treating as facts.

### “GraphRAG always better than normal RAG”

It adds đồ thị (graph / 그래프) construction/truy vấn (query / 쿼리) overhead and is valuable when relational/multi-hop cấu trúc (structure / 구조) actually matters.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Kiến thức (knowledge / 지식) Graphs sit at intersection of Databases, lô-gic (logic / 논리), đồ thị (graph / 그래프) Algorithms, NLP and ML. They are especially important later for RAG and Agents because they provide tường minh (explicit / 명시적) mutable bên ngoài (external / 외부) kiến thức (knowledge / 지식), while embeddings/LLMs provide flexible statistical ngôn ngữ (language / 언어) understanding.

Xem tiếp: [Symbolic and Neuro-Symbolic AI](./07_symbolic_neurosymbolic_ai.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
