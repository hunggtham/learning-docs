# Knowledge Graphs trong Artificial Intelligence

**Knowledge Graph (지식 그래프 / đồ thị tri thức)** biểu diễn entities và relationships bằng graph có typed semantics. Dạng đơn giản nhất là triple:

\[
(subject, predicate, object)
\]

Ví dụ:

```text
(Seoul, capitalOf, SouthKorea)
(Alice, worksAt, CompanyX)
(CompanyX, locatedIn, Seoul)
```

Điểm quan trọng: Knowledge Graph không chỉ là graph database có nhiều edges. Giá trị của nó đến từ identity, schema/ontology, provenance, temporal validity, relation semantics và khả năng nối facts từ nhiều nguồn thành một model có thể query/reason.

Xem trước: [Knowledge Representation](./00_knowledge_representation.md).

## Graph data model

Một graph gồm nodes `V` và edges `E`:

\[
G=(V,E)
\]

Trong KG:

- node thường là entity/concept/literal;
- edge có relation type;
- node/edge có thể có properties/metadata.

RDF-like graph biểu diễn edge qua triples. Property-graph systems cho phép properties trực tiếp trên node/edge.

Hai models có conversion possibilities nhưng query semantics/tooling khác nhau.

## Entity identity

Nếu facts dùng identifiers khác nhau cho cùng real entity:

```text
Seoul
서울
SEOUL_CITY_001
```

system cần mapping/canonical ID.

Nếu không, graph bị split thành duplicate entities. Nếu merge nhầm hai entities, facts bị contamination.

**Entity resolution (개체 해결 / thực thể đối sánh)** vì vậy là foundation, không phải cleanup minor.

## Relation semantics

Edge label `worksAt` cần define:

- subject type nào hợp lệ;
- object type nào hợp lệ;
- active employment hay historical?
- full-time/contractor có count không?
- temporal validity?

Without semantics, graph may be syntactically connected but semantically ambiguous.

## Schema và ontology

Schema can state:

```text
Person --worksAt--> Organization
Organization --locatedIn--> Place
```

Ontology adds class hierarchy/axioms:

```text
Doctor subClassOf MedicalProfessional
Hospital subClassOf HealthcareOrganization
```

Reasoner may derive inherited types.

Schema also enables validation: edge `Person worksAt Date` likely invalid.

## RDF mental model

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

RDF graph can merge datasets when identifiers/vocabularies align.

## RDFS và OWL

RDFS provides basic vocabulary for:

- classes;
- subclass;
- properties;
- domain/range.

OWL adds richer ontology constructs based on Description Logics, such as equivalence, cardinality and class expressions depending profile.

More expressive profile means potentially more expensive reasoning; OWL profiles intentionally offer different trade-offs.

## SPARQL

SPARQL queries RDF graph by graph patterns.

Conceptual query:

```sparql
SELECT ?person
WHERE {
  ?person :worksAt :CompanyX .
  ?person :livesIn :Seoul .
}
```

This is pattern matching over triples, not semantic similarity search.

Graph engines optimize join orders much like relational DB query optimizers.

## Property Graph và Cypher-like query

Property graph may store:

```text
(:Person {id: 1})-[:WORKS_AT {since: 2024}]->(:Company)
```

Query language like Cypher expresses path patterns.

Property graphs are common in operational graph applications; RDF/OWL ecosystems emphasize web-scale semantic standards/ontologies.

Neither model is universally superior.

## Relation as edge vs event node

Simple edge works for binary timeless relation:

```text
Alice --worksAt--> CompanyX
```

But suppose employment has role, start/end, salary, source.

Represent employment as entity/event:

```text
Alice --participantIn--> Employment123
Employment123 --employer--> CompanyX
Employment123 --role--> Engineer
Employment123 --startDate--> 2025-01-01
```

This avoids awkward edge metadata in triple-only model and supports n-ary relations.

## Provenance

A fact should often carry source:

```text
claim: CompanyX locatedIn Seoul
source: registry document
retrievedAt: 2026-09-01
confidence: verified
```

When sources conflict, provenance allows system to compare rather than silently overwrite.

RAG citation and KG provenance solve related trust problem.

## Temporal Knowledge Graph

Relations change over time:

```text
(Alice, worksAt, CompanyX, 2025-01..2026-08)
```

Temporal KG supports historical queries:

> Who was CEO on date T?

Without time, graph may contain contradictory edges that are actually valid in different periods.

## Inference over graph

Rule:

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

Inference materializes derived triples or answers queries dynamically.

Graph traversal alone is not logical inference unless relation semantics define rule.

## Transitive relations

If relation declared transitive:

\[
R(a,b)\land R(b,c)\rightarrow R(a,c)
\]

Examples may include `ancestorOf`, `locatedWithin` under carefully defined semantics.

Do not assume every relation transitive. `friendOf` and `parentOf` are not.

## Symmetric và inverse relations

Symmetric:

\[
MarriedTo(a,b)\rightarrow MarriedTo(b,a)
\]

Inverse:

\[
ParentOf(a,b)\leftrightarrow ChildOf(b,a)
\]

Encoding these properties reduces duplicated manual facts and supports query expansion.

## Knowledge Graph completion

KG often incomplete. Link prediction estimates missing triple score:

\[
score(h,r,t)
\]

Embedding methods map entities/relations to vectors and learn scoring function.

Example TransE-like idea:

\[
\mathbf{h}+\mathbf{r}\approx\mathbf{t}
\]

for true triple.

But predicted edge is **hypothesis**, not verified fact. Completion must not silently convert score into truth in high-stakes system.

## Entity embeddings

Graph embeddings place entities in vector space based on topology/relations.

They enable:

- link prediction;
- similarity;
- clustering;
- downstream ML features.

But vector similarity compresses relational structure and can lose explicit interpretability.

This mirrors symbolic ↔ distributed representation trade-off.

## Graph Neural Networks

GNN updates node representation by aggregating neighbors:

\[
\mathbf{h}_v^{(l+1)}=\phi\left(\mathbf{h}_v^{(l)},\operatorname{AGG}\{\mathbf{h}_u^{(l)}:u\in N(v)\}\right)
\]

GNN can learn on graph structure, but it does not replace KG schema/provenance.

Knowledge Graph is data/semantic representation; GNN is learning architecture that may consume graphs.

## Multi-hop queries

Question:

> Which suppliers are located in countries affected by event X?

May require path:

```text
Supplier
→ locatedIn
Country
← affects
Event
```

Graph enables explicit multi-hop retrieval.

But path existence does not automatically mean answer semantically valid; relation directions/types matter.

## Path explosion

If average degree `b`, number paths of length `k` can grow roughly `b^k`.

Graph query needs:

- relation filters;
- direction constraints;
- path length bounds;
- schema;
- ranking.

This is search problem again.

## Knowledge Graph vs relational database

Relational DB excels tabular transactions, constraints and SQL joins.

Graph DB excels variable-length relationship traversal and graph-centric schema.

Many KG facts can be stored relationally; “Knowledge Graph” is semantic/modeling concept, not necessarily requirement for graph database technology.

Choose storage from workload, not branding.

## Knowledge Graph vs vector database

Vector DB retrieves by embedding similarity:

```text
query embedding ≈ document/entity embedding
```

KG retrieves by explicit relationships/constraints:

```text
entity --relation--> entity
```

Vector search answers “what is semantically similar?”

KG query answers “what is explicitly connected according to relation semantics?”

Hybrid system can use both.

## KG + RAG

Text RAG flow:

```text
query → embedding retrieval → chunks → LLM
```

KG-enhanced flow can add:

```text
query
 ↓ entity linking
seed entities
 ↓ graph traversal / structured filters
relevant entities + relations + documents
 ↓
LLM grounded generation
```

Benefits can include explicit multi-hop structure, metadata filtering and provenance.

But graph construction/maintenance cost is significant.

## GraphRAG term

“GraphRAG” is used for multiple architectures, not one standardized algorithm. Common idea is augment retrieval/generation with graph-derived entities, communities, relations or paths.

When evaluating GraphRAG, ask exactly:

- graph built how?
- nodes/edges mean what?
- query strategy?
- graph used for retrieval, summarization or reasoning?
- facts verified how?

Do not treat label as guarantee of better reasoning.

## Entity linking from text

Before querying KG from natural language, identify mentions and map to entities.

`Apple` could mean company or fruit.

Entity linking uses context to resolve ambiguity.

A wrong link contaminates entire downstream multi-hop query, so confidence/fallback matter.

## Ontology-aware retrieval

If query asks `medical professional`, ontology may expand subclasses:

```text
Doctor
Nurse
Pharmacist
... ⊑ MedicalProfessional
```

This improves recall without relying only lexical/embedding similarity.

But ontology must match domain and current definitions.

## KG in recommendation

User-item interaction plus item attributes/relations:

```text
User → watched → Movie
Movie → directedBy → Director
Movie → genre → SciFi
```

Graph paths can provide explainable features/recommendations.

Embedding/GNN models can learn from this heterogeneous graph.

## KG in fraud detection

Graph connects:

```text
Account
Device
IP
Merchant
Phone
Transaction
```

Fraud may be relational: many accounts share device/IP or money cycles.

Graph algorithms/GNNs detect patterns invisible to per-row classifier.

Still need temporal ordering and avoid leakage (future edges).

## Data quality

KG quality dimensions:

- entity resolution accuracy;
- relation correctness;
- coverage;
- temporal freshness;
- provenance;
- schema consistency;
- duplicate/conflict rate.

A huge graph with poor identity is worse than smaller reliable graph.

## Incremental updates

Production KG evolves continuously. Update pipeline must handle:

```text
new source
→ extract entities/relations
→ resolve identity
→ validate schema
→ preserve provenance
→ reconcile conflicts
→ update indexes/embeddings
```

This is Data Engineering + Knowledge Engineering, not just AI modeling.

## Extraction with LLM

LLM can convert text to candidate triples:

```text
Text → LLM → structured entities/relations
```

Need validation because model may:

- invent relation;
- merge entities incorrectly;
- omit qualifier/time;
- normalize value wrongly.

Safer pipeline:

```text
LLM extraction
→ schema validation
→ entity resolution
→ source-grounded verification
→ human/review rules for critical facts
```

## Question answering over KG

Methods range from:

- deterministic SPARQL/Cypher;
- semantic parsing NL → query;
- embedding-based relation prediction;
- GNN reasoning;
- LLM tool-calling graph query.

Reliable enterprise pattern: LLM generates structured query, graph engine executes, LLM verbalizes result with provenance.

## Mental Model

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

## Common Misconceptions

### “Knowledge Graph = vector database with relationships”

No. Vector DB centers similarity in embedding space; KG centers explicit typed relations and semantics.

### “If path exists, relationship is meaningful”

Graph path only becomes meaningful through relation semantics, direction and context.

### “Link prediction adds missing facts”

It predicts candidates/scores; external validation may be required before treating as facts.

### “GraphRAG always better than normal RAG”

It adds graph construction/query overhead and is valuable when relational/multi-hop structure actually matters.

## Knowledge Connection

Knowledge Graphs sit at intersection of Databases, Logic, Graph Algorithms, NLP and ML. They are especially important later for RAG and Agents because they provide explicit mutable external knowledge, while embeddings/LLMs provide flexible statistical language understanding.

Xem tiếp: [Symbolic and Neuro-Symbolic AI](./07_symbolic_neurosymbolic_ai.md).