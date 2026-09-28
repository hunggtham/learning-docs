# Kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence

> **Mạch đọc:** Đặt **kiến thức (knowledge / 지식) Graphs trong Artificial Intelligence** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **đồ thị (graph / 그래프) mô hình dữ liệu (data model / 데이터 모델)** sang **thực thể (entity / 엔터티) định danh (identity / 식별자)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론)

Edge label `worksAt` cần define:

- subject kiểu (type / 타입) nào hợp lệ;
- đối tượng (object / 객체) kiểu (type / 타입) nào hợp lệ;
- active employment hay historical?
- full-time/contractor có count không?
- temporal validity?

Without ngữ nghĩa (semantics / 의미론), đồ thị (graph / 그래프) may be syntactically connected but semantically ambiguous.

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

## RDFS và OWL

RDFS provides basic vocabulary for:

- classes;
- subclass;
- properties;
- lĩnh vực (domain / 도메인)/phạm vi (range / 범위).

OWL adds richer ontology constructs based on Description Logics, such as equivalence, cardinality and lớp (class / 클래스) expressions depending profile.

More expressive profile means potentially more expensive lập luận (reasoning / 추론); OWL profiles intentionally offer different trade-offs.

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

## Thuộc tính (property / 속성) đồ thị (graph / 그래프) và Cypher-like truy vấn (query / 쿼리)

Thuộc tính (property / 속성) đồ thị (graph / 그래프) may store:

```text
(:Person {id: 1})-[:WORKS_AT {since: 2024}]->(:Company)
```

Truy vấn (query / 쿼리) ngôn ngữ (language / 언어) like Cypher expresses đường dẫn (path / 경로) patterns.

Thuộc tính (property / 속성) graphs are dùng chung (common / 공통) in operational đồ thị (graph / 그래프) applications; RDF/OWL ecosystems emphasize web-scale ngữ nghĩa (semantic / 의미적) standards/ontologies.

Neither mô hình (model / 모델) is universally superior.

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

## Temporal kiến thức (knowledge / 지식) đồ thị (graph / 그래프)

Relations thay đổi (change / 변경) over thời gian (time / 시간):

```text
(Alice, worksAt, CompanyX, 2025-01..2026-08)
```

Temporal KG supports historical queries:

> Who was CEO on date T?

Without thời gian (time / 시간), đồ thị (graph / 그래프) may contain contradictory edges that are actually valid in different periods.

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

## Transitive relations

If quan hệ (relation / 관계) declared transitive:

\[
R(a,b)\land R(b,c)\rightarrow R(a,c)
\]

Examples may include `ancestorOf`, `locatedWithin` under carefully defined ngữ nghĩa (semantics / 의미론).

Do not assume every quan hệ (relation / 관계) transitive. `friendOf` and `parentOf` are not.

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

## Thực thể (entity / 엔터티) embeddings

Đồ thị (graph / 그래프) embeddings place entities in véc-tơ (vector / 벡터) không gian (space / 공간) based on topology/relations.

They enable:

- link prediction;
- similarity;
- clustering;
- downstream ML features.

But véc-tơ (vector / 벡터) similarity compresses relational cấu trúc (structure / 구조) and can lose tường minh (explicit / 명시적) interpretability.

This mirrors symbolic ↔ phân tán (distributed / 분산) biểu diễn (representation / 표현) sự đánh đổi (trade-off / 트레이드오프).

## Đồ thị (graph / 그래프) Neural Networks

GNN updates nút (node / 노드) biểu diễn (representation / 표현) by aggregating neighbors:

\[
\mathbf{h}_v^{(l+1)}=\phi\left(\mathbf{h}_v^{(l)},\operatorname{AGG}\{\mathbf{h}_u^{(l)}:u\in N(v)\}\right)
\]

GNN can learn on đồ thị (graph / 그래프) cấu trúc (structure / 구조), but it does not replace KG lược đồ (schema / 스키마)/provenance.

Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) is dữ liệu (data / 데이터)/ngữ nghĩa (semantic / 의미적) biểu diễn (representation / 표현); GNN is học tập (learning / 학습) kiến trúc (architecture / 아키텍처) that may consume graphs.

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

## Đường dẫn (path / 경로) explosion

If average degree `b`, number paths of length `k` can grow roughly `b^k`.

Đồ thị (graph / 그래프) truy vấn (query / 쿼리) needs:

- quan hệ (relation / 관계) filters;
- direction các ràng buộc (constraints / 제약조건들);
- đường dẫn (path / 경로) length bounds;
- lược đồ (schema / 스키마);
- ranking.

This is tìm kiếm (search / 검색) bài toán (problem / 문제) again.

## Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) vs relational cơ sở dữ liệu (database / 데이터베이스)

Relational DB excels tabular transactions, các ràng buộc (constraints / 제약조건들) and SQL joins.

Đồ thị (graph / 그래프) DB excels variable-length relationship traversal and graph-centric lược đồ (schema / 스키마).

Many KG facts can be stored relationally; “kiến thức (knowledge / 지식) đồ thị (graph / 그래프)” is ngữ nghĩa (semantic / 의미적)/modeling concept, not necessarily yêu cầu (requirement / 요구사항) for đồ thị (graph / 그래프) cơ sở dữ liệu (database / 데이터베이스) technology.

Choose lưu trữ (storage / 저장소) from tải công việc (workload / 워크로드), not branding.

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

## GraphRAG term

“GraphRAG” is used for multiple architectures, not one standardized thuật toán (algorithm / 알고리즘). dùng chung (common / 공통) idea is augment retrieval/generation with graph-derived entities, communities, relations or paths.

When evaluating GraphRAG, ask exactly:

- đồ thị (graph / 그래프) built how?
- nodes/edges mean what?
- truy vấn (query / 쿼리) chiến lược (strategy / 전략)?
- đồ thị (graph / 그래프) used for retrieval, summarization or lập luận (reasoning / 추론)?
- facts verified how?

Do not treat label as guarantee of better lập luận (reasoning / 추론).

## Thực thể (entity / 엔터티) linking from văn bản (text / 텍스트)

Before querying KG from natural ngôn ngữ (language / 언어), identify mentions and map to entities.

`Apple` could mean company or fruit.

Thực thể (entity / 엔터티) linking uses ngữ cảnh (context / 맥락) to resolve ambiguity.

A wrong link contaminates entire downstream multi-hop truy vấn (query / 쿼리), so confidence/fallback matter.

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

## KG in recommendation

User-item tương tác (interaction / 상호작용) plus item attributes/relations:

```text
User → watched → Movie
Movie → directedBy → Director
Movie → genre → SciFi
```

Đồ thị (graph / 그래프) paths can provide explainable features/recommendations.

Embedding/GNN các mô hình (models / 모델들) can learn from this heterogeneous đồ thị (graph / 그래프).

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

## Question answering over KG

Methods phạm vi (range / 범위) from:

- deterministic SPARQL/Cypher;
- ngữ nghĩa (semantic / 의미적) parsing NL → truy vấn (query / 쿼리);
- embedding-based quan hệ (relation / 관계) prediction;
- GNN lập luận (reasoning / 추론);
- LLM tool-calling đồ thị (graph / 그래프) truy vấn (query / 쿼리).

Reliable enterprise mẫu (pattern / 패턴): LLM generates structured truy vấn (query / 쿼리), đồ thị (graph / 그래프) engine executes, LLM verbalizes kết quả (result / 결과) with provenance.

## Mô hình tư duy (mental model / 사고 모델)

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

## Dùng chung (common / 공통) Misconceptions

### “kiến thức (knowledge / 지식) đồ thị (graph / 그래프) = véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) with relationships”

No. véc-tơ (vector / 벡터) DB centers similarity in embedding không gian (space / 공간); KG centers tường minh (explicit / 명시적) typed relations and ngữ nghĩa (semantics / 의미론).

### “If đường dẫn (path / 경로) exists, relationship is meaningful”

Đồ thị (graph / 그래프) đường dẫn (path / 경로) only becomes meaningful through quan hệ (relation / 관계) ngữ nghĩa (semantics / 의미론), direction and ngữ cảnh (context / 맥락).

### “Link prediction adds missing facts”

It predicts candidates/scores; bên ngoài (external / 외부) kiểm tra hợp lệ (validation / 검증) may be required before treating as facts.

### “GraphRAG always better than normal RAG”

It adds đồ thị (graph / 그래프) construction/truy vấn (query / 쿼리) overhead and is valuable when relational/multi-hop cấu trúc (structure / 구조) actually matters.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Kiến thức (knowledge / 지식) Graphs sit at intersection of Databases, lô-gic (logic / 논리), đồ thị (graph / 그래프) Algorithms, NLP and ML. They are especially important later for RAG and Agents because they provide tường minh (explicit / 명시적) mutable bên ngoài (external / 외부) kiến thức (knowledge / 지식), while embeddings/LLMs provide flexible statistical ngôn ngữ (language / 언어) understanding.

Xem tiếp: [Symbolic and Neuro-Symbolic AI](./07_symbolic_neurosymbolic_ai.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 knowledge representation](./00_knowledge_representation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
